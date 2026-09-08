# Halfday Shopify theme

Halfday's customized Dawn 15.2.0 theme, downloaded from the active theme on September 7, 2026.

| Item | Value |
| --- | --- |
| Store | `halfday-tonics.myshopify.com` |
| Storefront | https://drinkhalfday.com |
| Downloaded theme | `141825474760` — HALFDAY 2.0 - PDP Update - 10 Mar 2025 |
| Untouched baseline | Git commit `ed05175`; tag `baseline/live-2026-09-07` |
| Toolchain | Shopify CLI 4.6.1 (pinned locally); Node 24.19.0 used for setup |
| Claude Code | Installed version 2.1.207; shared project context in `CLAUDE.md` |

Start with the [focused performance, app, Klaviyo and SEO audit](docs/focused-audit-2026-09-07.md) for verified findings from 15 performance runs, 71 public pages and authenticated account inspection. The [modernization roadmap](docs/modernization-roadmap.md) is the single delivery plan for CRO, speed/LCP, app cleanup, content, email/search, integrations, and reviews, including estimates and an email draft for Leslie. The [initial store audit](docs/initial-audit-2026-09-07.md) and [Klaviyo account audit](docs/klaviyo-audit-2026-09-07.md) remain supporting snapshots. Evidence is in `reports/`. Wave 1 is merged into `main` as an unpublished release candidate; `dev/wave-1` retains its implementation history. See the [progress checklist and preview](docs/wave-1-progress.md) for changes, validation and outstanding decisions. The production theme is unchanged. Agentready shared settings have been configured; full activation is blocked by [verified app issues](docs/agentready-product-feedback.md).

## Daily development

```sh
cd /Users/dylanhunt/Documents/development/Halfday
npm ci
npm run theme:list
git switch main
git switch -c feature/describe-the-change
npm run theme:dev
```

Shopify CLI uses your Shopify account session and opens a login flow if needed. No theme password is stored in this repository. `theme:dev` uploads local files into the account's development theme and starts Shopify's local preview server; it changes remote development files. Stop the server with Ctrl-C.

```sh
npm run theme:check
npm run theme:push:dev
npm run theme:open:dev
```

During setup, `shopify theme info --environment development` resolved development theme `142755430600`, named `Development (deb269-MacBook-Pro-4)`. Development themes are account/session resources; resolve again rather than hardcoding this ID for another collaborator. Wave 1 has now been pushed to this development theme; the current preview is linked in the progress checklist. Development previews share real store data and apps; they are not isolated test stores.

The initial Theme Check result is **126 errors and 361 warnings**, recorded in `reports/theme-check-baseline.json`. These are inherited, not setup regressions. Do not suppress the whole baseline or claim checks pass. The second Wave 1 checkpoint fixes four errors, including both dynamic-tag parser errors, and reports 122 errors / 404 warnings. The warning increase comes from existing mega-menu code becoming parseable; see the progress checklist for the comparison. Locksmith findings require app-aware review. `theme:push:dev` is deliberately not a production release command.

## Synchronize merchant changes

Before new work, check the working tree and `theme:list`. While `main` contains unpublished Wave 1 work, download the live theme to a separate temporary directory using Shopify CLI with explicit `--theme` and `--path`. Compare it with `baseline/live-2026-09-07`, then bring any newer merchant changes into a feature branch. Do not pull the older live theme directly over `main`.

The pull wrapper refuses a dirty tree but can still overwrite committed changes. After an approved release, record the released baseline and reconcile merchant edits against that version. Before publishing, refresh the live snapshot, reconcile JSON/settings edits, validate the connected unpublished preview and review the exact diff. Production publishing requires an explicitly authorized release task.

Start each subsequent wave or focused fix from `main` on a descriptive `feature/...` or `fix/...` branch. Preview and verify that branch on an unpublished theme, then merge reviewed changes into `main`. A Git merge is not publishing permission. Once Shopify is connected, inspect the actual branch/theme mapping before pushing because a connected theme may synchronize automatically.

## Repository boundaries

Shopify's native theme folders live at the repository root. This is a Liquid/CSS/JavaScript theme with no frontend build step. Node dependencies are developer tooling and are not sent to the storefront. `.shopifyignore` excludes project documentation, reports, scripts, and tooling from theme sync.

GitHub repository: [dylanjhunt/halfday-shopify](https://github.com/dylanjhunt/halfday-shopify), configured as `origin`. `main` contains the Wave 1 release candidate and `dev/wave-1` retains the completed implementation history. The original live theme remains available at `baseline/live-2026-09-07`. Dylan will arrange the Shopify connection, followed by the final audit and separate publishing approval.

Products, menus, pages, metafields/metaobjects, app configuration, inventory, and fulfillment do not come down with `theme pull`. Keep those changes documented separately; preserve merchant-managed theme JSON in version control. Never commit credentials or customer/order exports.

Launch `claude` from this directory. Claude Code automatically reads the root `CLAUDE.md`; `/memory` can be used to inspect loaded project guidance. `AGENTS.md` directs other agents to the same conventions. No permissive auto-approval settings or third-party agent installation was added. Setup follows [Claude's project memory documentation](https://code.claude.com/docs/en/memory).

`buffer context`, requested by the supplied managed instruction, was attempted; Buffer CLI is not installed. It is not required for this Shopify workflow.

Environment configuration follows [Shopify theme environments](https://shopify.dev/docs/storefronts/themes/tools/cli/environments). Command references: [theme pull](https://shopify.dev/docs/api/shopify-cli/theme/theme-pull), [theme dev](https://shopify.dev/docs/api/shopify-cli/theme/theme-dev), [theme push](https://shopify.dev/docs/api/shopify-cli/theme/theme-push).

Wave 1 motion lifecycle verification: `node scripts/test-motion.cjs`. Sanitized performance summaries can be regenerated with `python3 scripts/summarize-wave-1-pass-2.py /path/to/lighthouse-json-directory`.

Wave 1 regression verification: `python3 scripts/verify-regressions.py` compares 15 public live/development routes, Amazon attribution links, tracking loaders and protected code. The third checkpoint in the progress checklist records browser interaction checks, visual comparisons and tracking transport limits.
