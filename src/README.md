# Maintenance helpers

The [main README](../README.md) is the Awesome AI Switzerland directory. This small Python
package contains its maintenance scripts.

## Setup and commands

Use [uv](https://docs.astral.sh/uv/). The package supports Python 3.13+;
`.python-version` selects Python 3.14 by default. Run these commands from the
repository root:

```sh
make install       # Install dependencies and the local package in .venv
make count-sources # Write count_sources.md and print the counts
make check-links   # Write link-check-report.md (requires network access)
make reports       # Run both helpers
make check         # Lint, check formatting and run offline tests
make format        # Format Python files
make help          # List all targets
```

- `awesome_ai_switzerland/count_sources.py` counts top-level resource bullets
  with external Markdown links under level-two headings, grouped by section
  and heading path. Secondary links, nested
  bullets, table rows and fenced examples do not add entries. The model table
  is therefore excluded from the counts. Separate cross-references
  count again; these are not counts of unique datasets or publishers.
- `awesome_ai_switzerland/link_checker.py` checks unique HTTP(S) URLs using HEAD
  with a streamed GET fallback. It reports reachable, likely broken (404/410)
  and `needs review` (inconclusive) results. It removes URL fragments before
  checking and does not validate local links, content or licenses.
  The command exits with status 1 for likely broken links or a missing input;
  inconclusive checks alone do not cause failure.

Both helpers default to `README.md` in the current working directory, so the
default reports cover only the main README. The default report paths at the
repository root are ignored by Git and excluded from Pages. Override the input
or output to check another document or write elsewhere:

```sh
uv run --locked count-sources README.md --output /tmp/counts.md
uv run --locked check-links README.md --output /tmp/links.md
make check-links ARGS='README.md --output /tmp/links.md'
```

Use `--help` with either command for options. `make lint`, `make format-check`
and `make test` also work separately. The tests make no network requests.
`make check` validates the Python helpers; it does not check documentation links
or build the website. The [Pages workflow](../.github/workflows/pages.yml)
separately builds the site and checks selected output files and exclusions.
