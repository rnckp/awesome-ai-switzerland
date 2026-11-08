"""Check README HTTP links, separating likely broken URLs from inconclusive checks."""

import argparse
import os
import re
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from functools import cache
from html import unescape
from pathlib import Path
from urllib.parse import quote, unquote, urldefrag, urlsplit

import requests
from rich.console import Console
from rich.progress import track

console = Console()
REQUEST_TIMEOUT = 30
MAX_WORKERS = 10
MAX_ATTEMPTS = 3
RETRY_DELAY = 2
USER_AGENT = "Mozilla/5.0 (compatible; Link-Checker/1.0)"
GITHUB_API = "https://api.github.com"
GITHUB_RESERVED = {
    "about", "apps", "collections", "enterprise", "events", "explore",
    "features", "issues", "login", "marketplace", "notifications", "orgs",
    "pricing", "pulls", "search", "settings", "sponsors", "topics", "trending",
}  # fmt: skip


def extract_urls_from_markdown(file_path: Path) -> list[str]:
    """Extract HTTP(S) destinations from Markdown, HTML and plain text.

    Quotes and angle brackets delimit HTML attributes, so adjacent markup is
    never included. Balanced URL parentheses are retained; Markdown closing
    parentheses and surrounding prose punctuation are discarded. Fragments
    are removed because HTTP requests cannot validate client-side routes.
    """
    content = file_path.read_text(encoding="utf-8")
    urls = []
    seen = set()
    for match in re.finditer(r"""https?://[^\s<>"'\[\]`]+""", content):
        url = unescape(match[0])
        # Stop at the first unmatched closing parenthesis (Markdown syntax).
        depth = 0
        for index, char in enumerate(url):
            if char == "(":
                depth += 1
            elif char == ")":
                if depth == 0:
                    url = url[:index]
                    break
                depth -= 1
        url = urldefrag(url.rstrip(".,;:!?"))[0]
        if urlsplit(url).netloc and url not in seen:
            seen.add(url)
            urls.append(url)
    return urls


def classify_status(status_code: int) -> str:
    if 200 <= status_code < 400:
        return "reachable"
    if status_code in (404, 410):
        return "likely broken"
    return "needs review"


def request_once(url: str) -> tuple[str, int, str]:
    """Return outcome, HTTP code and explanation from one HEAD/GET pass.

    Retry failed HEAD checks with a streamed GET: some servers reject HEAD.
    Do not download response bodies (links can point at large datasets).
    """
    headers = {"User-Agent": USER_AGENT}
    for method in (requests.head, requests.get):
        try:
            with method(
                url,
                timeout=REQUEST_TIMEOUT,
                allow_redirects=True,
                headers=headers,
                stream=True,
            ) as response:
                code = response.status_code
                outcome = classify_status(code)
            if outcome == "reachable":
                return outcome, code, ""
            result = (
                outcome,
                code,
                {
                    401: "Authentication required; not evidence of a dead link",
                    403: "Access denied or bot protection; check in a browser",
                    404: "HTTP 404; verify the destination before removing",
                    410: "HTTP 410; resource reported gone",
                    429: "Rate limited; retry later",
                }.get(code, "Server or HTTP error; retry or check manually"),
            )
        except requests.exceptions.Timeout:
            result = ("needs review", 0, "Timeout; retry later")
        except requests.exceptions.TooManyRedirects:
            result = ("needs review", 0, "Redirect loop; check in a browser")
        except requests.exceptions.RequestException as error:
            result = (
                "needs review",
                0,
                f"Connection/request error: {type(error).__name__}",
            )
    return result


def is_transient(outcome: str, code: int) -> bool:
    """Timeouts, connection errors, rate limits and 5xx may succeed on retry."""
    return outcome == "needs review" and (code == 0 or code == 429 or code >= 500)


@cache
def github_token() -> str | None:
    """Token for the GitHub API: GITHUB_TOKEN, GH_TOKEN or `gh auth token`."""
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        return token
    try:
        result = subprocess.run(
            ["gh", "auth", "token"], capture_output=True, text=True, timeout=10
        )
    except (OSError, subprocess.SubprocessError):
        return None
    return result.stdout.strip() or None if result.returncode == 0 else None


def github_api_status(path: str) -> int | None:
    headers = {"User-Agent": USER_AGENT, "Accept": "application/vnd.github+json"}
    if token := github_token():
        headers["Authorization"] = f"Bearer {token}"
    try:
        return requests.get(
            f"{GITHUB_API}/{path}", timeout=REQUEST_TIMEOUT, headers=headers
        ).status_code
    except requests.exceptions.RequestException:
        return None


def check_github_api(url: str) -> tuple[str, int, str] | None:
    """Verify github.com URLs through the API, which github.com's web frontend
    often answers with 5xx under load. Return None if inconclusive.

    Account and repository URLs are checked exactly. For other repository
    paths only the repository is verified, except tree/blob paths, whose
    path is looked up (the ref may contain slashes, so a few splits are tried).
    """
    split = urlsplit(url)
    if split.netloc.lower() not in ("github.com", "www.github.com"):
        return None
    parts = [unquote(part) for part in split.path.split("/") if part]
    if not parts or parts[0].lower() in GITHUB_RESERVED:
        return None
    owner = quote(parts[0])
    if len(parts) == 1:
        api_paths = [f"users/{owner}"]
    else:
        repo = f"repos/{owner}/{quote(parts[1])}"
        api_paths = [repo]
        if len(parts) > 3 and parts[2] in ("tree", "blob"):
            refs = parts[3:]
            api_paths = []
            for split_at in range(1, min(len(refs), 4) + 1):
                ref = quote("/".join(refs[:split_at]), safe="")
                path = quote("/".join(refs[split_at:]))
                if path:
                    api_paths.append(f"{repo}/contents/{path}?ref={ref}")
                elif parts[2] == "tree":
                    api_paths.append(f"{repo}/contents?ref={ref}")
    statuses = [github_api_status(path) for path in api_paths]
    if 200 in statuses:
        return "reachable", 200, ""
    if all(status == 404 for status in statuses):
        return "likely broken", 404, "HTTP 404 via GitHub API; verify before removing"
    return None


def check_url(url: str) -> tuple[str, str, int, str]:
    """Return URL, outcome, HTTP code and explanation.

    Transient failures are retried with backoff. For github.com, whose web
    frontend often answers with 5xx under load, the GitHub API decides instead.
    """
    for attempt in range(MAX_ATTEMPTS):
        outcome, code, detail = request_once(url)
        if not is_transient(outcome, code):
            return url, outcome, code, detail
        if api_result := check_github_api(url):
            return (url, *api_result)
        if attempt < MAX_ATTEMPTS - 1:
            time.sleep(RETRY_DELAY * 2**attempt)
    return url, outcome, code, detail


def check_all_links(urls):
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # map preserves input order for stable report diffs.
        return list(
            track(
                executor.map(check_url, urls),
                total=len(urls),
                description="Checking links",
                console=console,
            )
        )


def generate_report(results, output_path=Path("link-check-report.md")):
    total = len(results)
    reachable = sum(outcome == "reachable" for _, outcome, _, _ in results)
    broken = sum(outcome == "likely broken" for _, outcome, _, _ in results)
    review = total - reachable - broken
    rate = reachable / total * 100 if total else 0
    lines = [
        "# Link Check Report",
        "",
        f"**Checked at:** {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        f"**Total URLs checked:** {total}  ",
        f"**Reachable:** {reachable}  ",
        f"**Likely broken (404/410):** {broken}  ",
        f"**Needs review:** {review}  ",
        f"**Reachable rate:** {rate:.1f}%",
        "",
        "HTTP reachability does not verify page content, licensing, downloads or "
        "JavaScript routes. Fragments and internal anchors are not checked. "
        "Access blocks, rate limits, server errors and connection failures are "
        "inconclusive, not proof of dead links. Even 404/410 results should be "
        "confirmed before removing a resource.",
        "",
    ]
    for category in ("likely broken", "needs review"):
        rows = [r for r in results if r[1] == category]
        lines += [f"## {category.capitalize()}", ""]
        if not rows:
            lines += ["None.", ""]
            continue
        lines += ["| URL | HTTP status | Detail |", "| --- | :---: | --- |"]
        for url, _, code, detail in rows:
            safe_url = url.replace("|", "%7C")
            safe_detail = detail.replace("|", r"\|").replace("\n", " ")
            lines.append(
                f"| [{safe_url}](<{safe_url}>) | {code or '-'} | {safe_detail} |"
            )
        lines.append("")
    output_path.write_text("\n".join(lines), encoding="utf-8")
    console.print(
        f"Checked {total}: {reachable} reachable, {broken} likely broken, {review} need review."
    )
    console.print(f"Report saved to {output_path}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("readme", type=Path, nargs="?", default=Path("README.md"))
    parser.add_argument(
        "-o", "--output", type=Path, default=Path("link-check-report.md")
    )
    args = parser.parse_args(argv)
    if not args.readme.is_file():
        console.print(f"File not found: {args.readme}")
        return 1
    results = check_all_links(extract_urls_from_markdown(args.readme))
    generate_report(results, args.output)
    # An inconclusive automated check alone should not fail CI.
    return 1 if any(r[1] == "likely broken" for r in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
