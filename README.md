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

Start with the [modernization roadmap](docs/modernization-roadmap.md): the single delivery plan for CRO, speed/LCP, app cleanup, content, email/search, integrations, and reviews, including estimates and a Slack draft for Leslie. The [initial store audit](docs/initial-audit-2026-09-07.md) and [Klaviyo account audit](docs/klaviyo-audit-2026-09-07.md) are supporting evidence snapshots. Evidence is in `reports/`. No storefront theme code was changed during setup, auditing, or planning.

## Daily development

```sh
cd /Users/dylanhunt/Documents/development/Halfday
npm ci
npm run theme:list
git switch -c feature/describe-the-change
npm run theme:dev
```

Shopify CLI uses your Shopify account session and opens a login flow if needed. No theme password is stored in this repository. `theme:dev` uploads local files into the account's development theme and starts Shopify's local preview server; it changes remote development files. Stop the server with Ctrl-C.

```sh
npm run theme:check
npm run theme:push:dev
npm run theme:open:dev
```

During setup, `shopify theme info --environment development` resolved development theme `142755430600`, named `Development (deb269-MacBook-Pro-4)`. Development themes are account/session resources; resolve again rather than hardcoding this ID for another collaborator. No local theme files have been pushed during this setup. Development previews share real store data and apps; they are not isolated test stores.

The initial Theme Check result is **126 errors and 361 warnings**, recorded in `reports/theme-check-baseline.json`. These are inherited, not setup regressions. Do not suppress the whole baseline or claim checks pass. Triage active code first; the two dynamic-tag syntax findings require runtime validation, and Locksmith findings require app-aware review. `theme:push:dev` is deliberately not a production release command.

## Synchronize merchant changes

Before new work, commit/stash changes and pull the latest live theme:

```sh
npm run theme:pull
git diff --stat
git diff -- config/settings_data.json templates sections
git add assets config layout locales sections snippets templates
git commit -m "chore: sync current Shopify theme changes"
```

The pull wrapper refuses a dirty tree and follows whichever theme is currently live. Check `theme:list` first if another theme may have been published. Pulling over a clean feature branch can still overwrite committed feature changes; synchronize on `main` and merge the resulting commit into the feature branch. Git gives you recovery, not conflict-free automatic sync.

For a one-off comparison, pull the relevant remote theme to a separate temporary directory using an explicit `--theme` and `--path`, then diff it with this checkout. Before release, refresh the live snapshot, reconcile merchant JSON/settings edits, validate a development preview, and review the exact diff. Production publishing requires an explicitly authorized release task; no live push or publish shortcut is configured here.

## Repository boundaries

Shopify's native theme folders live at the repository root. This is a Liquid/CSS/JavaScript theme with no frontend build step. Node dependencies are developer tooling and are not sent to the storefront. `.shopifyignore` excludes project documentation, reports, scripts, and tooling from theme sync.

Git is local on `main`. No GitHub repository, remote, Shopify GitHub connection, CI deployment, or automatic publishing has been created. A Git host/organization can be selected later if shared remote version control is wanted.

Products, menus, pages, metafields/metaobjects, app configuration, inventory, and fulfillment do not come down with `theme pull`. Keep those changes documented separately; preserve merchant-managed theme JSON in version control. Never commit credentials or customer/order exports.

Launch `claude` from this directory. Claude Code automatically reads the root `CLAUDE.md`; `/memory` can be used to inspect loaded project guidance. `AGENTS.md` directs other agents to the same conventions. No permissive auto-approval settings or third-party agent installation was added. Setup follows [Claude's project memory documentation](https://code.claude.com/docs/en/memory).

`buffer context`, requested by the supplied managed instruction, was attempted; Buffer CLI is not installed. It is not required for this Shopify workflow.

Environment configuration follows [Shopify theme environments](https://shopify.dev/docs/storefronts/themes/tools/cli/environments). Command references: [theme pull](https://shopify.dev/docs/api/shopify-cli/theme/theme-pull), [theme dev](https://shopify.dev/docs/api/shopify-cli/theme/theme-dev), [theme push](https://shopify.dev/docs/api/shopify-cli/theme/theme-push).
