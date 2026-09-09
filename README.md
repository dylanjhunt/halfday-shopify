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

Start with the [focused performance, app, Klaviyo and SEO audit](docs/focused-audit-2026-09-07.md) for verified findings from 15 performance runs, 71 public pages and authenticated account inspection. The [modernization roadmap](docs/modernization-roadmap.md) is the single delivery plan for CRO, speed/LCP, app cleanup, content, email/search, integrations, and reviews, including estimates and an email draft for Leslie. The [initial store audit](docs/initial-audit-2026-09-07.md) and [Klaviyo account audit](docs/klaviyo-audit-2026-09-07.md) remain supporting snapshots. Evidence is in `reports/`. Dylan published `halfday-shopify/main` (theme `142757101768`) on September 8, 2026. **GitHub main is live: pushing to main deploys to production.** The latest released baseline is `baseline/live-wave-1-follow-through-2026-09-08` (`a99ed7f`); `dev/wave-1` retains the first implementation history. See the [progress checklist and preview](docs/wave-1-progress.md) for changes, validation and outstanding decisions. Further Wave 1 work stays on `djh/wave-1-responsive-follow-up` and development theme `142755430600`. Agentready shared settings have been configured; full activation is blocked by [verified app issues](docs/agentready-product-feedback.md).

Latest development checkpoint: [combined tablet, LCP and Wave 1 readiness report](docs/wave-1-lcp-completion-2026-09-08.md). The named development branch is ready for combined review; main is unchanged.

## Daily development

```sh
cd /Users/dylanhunt/Documents/development/Halfday
npm ci
npm run theme:list
git fetch origin
git switch --no-track -c djh/describe-the-change origin/main
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

Before new work, check the working tree, fetch GitHub and inspect `theme:list`. Download live theme `142757101768` into a separate temporary directory with explicit `--theme` and `--path`. Compare against `baseline/live-wave-1-2026-09-08` or the latest recorded release, then reconcile any merchant JSON/settings changes through a development branch. Do not pull live over unpublished work.

Use a named `djh/...` branch and Shopify CLI development preview for every new change. Push that branch explicitly (`git push -u origin djh/describe-the-change`). **Never push or merge into main without release approval: its Shopify theme is already live.** Before an authorized release, refresh the live snapshot, review the exact diff and validate the unpublished preview. Record each released baseline.

Dylan confirmed customer buying routes to Amazon. Verify Amazon destinations and attribution parameters; staff/sample checkout is not a release gate. Preserve existing access controls and legacy native purchase code.

## Repository boundaries

Shopify's native theme folders live at the repository root. This is a Liquid/CSS/JavaScript theme with no frontend build step. Node dependencies are developer tooling and are not sent to the storefront. `.shopifyignore` excludes project documentation, reports, scripts, and tooling from theme sync.

GitHub repository: [dylanjhunt/halfday-shopify](https://github.com/dylanjhunt/halfday-shopify), configured as `origin`. `main` is connected to production; `dev/wave-1` retains the initial implementation history. The original theme remains available at `baseline/live-2026-09-07`, and the first published Wave 1 release is `baseline/live-wave-1-2026-09-08`.

Products, menus, pages, metafields/metaobjects, app configuration, inventory, and fulfillment do not come down with `theme pull`. Keep those changes documented separately; preserve merchant-managed theme JSON in version control. Never commit credentials or customer/order exports.

Launch `claude` from this directory. Claude Code automatically reads the root `CLAUDE.md`; `/memory` can be used to inspect loaded project guidance. `AGENTS.md` directs other agents to the same conventions. No permissive auto-approval settings or third-party agent installation was added. Setup follows [Claude's project memory documentation](https://code.claude.com/docs/en/memory).

`buffer context`, requested by the supplied managed instruction, was attempted; Buffer CLI is not installed. It is not required for this Shopify workflow.

Environment configuration follows [Shopify theme environments](https://shopify.dev/docs/storefronts/themes/tools/cli/environments). Command references: [theme pull](https://shopify.dev/docs/api/shopify-cli/theme/theme-pull), [theme dev](https://shopify.dev/docs/api/shopify-cli/theme/theme-dev), [theme push](https://shopify.dev/docs/api/shopify-cli/theme/theme-push).

Wave 1 motion lifecycle verification: `node scripts/test-motion.cjs`. Sanitized performance summaries can be regenerated with `python3 scripts/summarize-wave-1-pass-2.py /path/to/lighthouse-json-directory`.

Wave 1 regression verification: `python3 scripts/verify-regressions.py` compares 15 public live/development routes, Amazon attribution links, tracking loaders and protected code. The third checkpoint in the progress checklist records browser interaction checks, visual comparisons and tracking transport limits.
