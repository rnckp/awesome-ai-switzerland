# Contributing

Additions, corrections, and dead-link reports are welcome.

1. Confirm that the resource concerns the Swiss AI Apertus model family.
2. Link to the original repository, model card, documentation, paper, or application. Prefer stable resource URLs over search results and tracking links.
3. Add one concise description explaining what the resource provides. Group related sizes or quantizations in one entry.
4. Identify the model generation when relevant: 1.0 / `2509`, 1.1 Mini, or 1.5. Label experimental support and text-only conversions.
5. Keep official Swiss AI resources separate from third-party contributions. Organization membership alone does not make a research prototype a supported release.
6. Provide evidence of an Apertus integration. Generic API compatibility, copied model cards, and unsupported marketing claims are insufficient by themselves.
7. Check that links resolve and that their contents support the description. Disclose any relationship to the project you submit.

For corrections, include the current link, replacement or evidence, and the date checked. Avoid popularity counts, copied benchmark rankings, and prices that will quickly become stale.

## Updating with an AI agent

Ask the agent to read and follow [the maintenance skill](https://github.com/rnckp/awesome-swiss-ai/blob/main/.agent/skills/update-awesome-swiss-ai/SKILL.md). For example: “Use `.agent/skills/update-awesome-swiss-ai/SKILL.md` to refresh the Apertus resources, verify changed links, and update the research notes.” The file is portable agent guidance; it does not need an authenticated connector.

## Publishing the website

In the repository's **Settings → Pages → Build and deployment**, select **GitHub Actions** as the source. The Pages workflow builds on pushes to `main` and can also be run manually from Actions.

`_config.yml` configures `README.md` as the homepage and relative Markdown links for conversion to HTML destinations. Edit the Markdown sources, not generated files. The Pages workflow (`.github/workflows/pages.yml`) checks the generated homepage, stylesheet file and URL against the Pages base path, research notes, contribution guidelines, licence, one homepage anchor and selected tooling exclusions before deployment; it does not audit all links. If the repository or Pages path changes, review the config and workflow checks together. Agent instructions, Python helpers, tests and default maintenance reports are excluded from the site.

For helper setup, report commands and offline checks, use the [maintenance helper documentation](https://github.com/rnckp/awesome-swiss-ai/blob/main/src/README.md).
