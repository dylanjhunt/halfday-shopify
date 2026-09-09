# Halfday Shopify theme

This repository is the Shopify Online Store theme for Halfday Iced Tea, not a headless storefront or Shopify app. Store: `halfday-tonics.myshopify.com`; public site: `https://drinkhalfday.com`. Original baseline: theme `141825474760`, "HALFDAY 2.0 - PDP Update - 10 Mar 2025", downloaded September 7, 2026. Theme metadata identifies customized Dawn 15.2.0.

## Workflow

- Use Shopify CLI for theme operations. Read `README.md` and `docs/modernization-roadmap.md` for project status and the current delivery sequence. The dated store and Klaviyo audits are supporting evidence.
- `npm ci` installs the pinned local CLI. `npm run theme:list`, `npm run theme:check`, `npm run theme:dev`, `npm run theme:push:dev` are the normal commands.
- **Production:** Dylan published Git-connected theme `142757101768`, `halfday-shopify/main`, on September 8, 2026. Pushing to GitHub `main` automatically changes the live storefront. Treat any main merge/push as a production deployment requiring explicit release authorization.
- Published baseline: `baseline/live-wave-1-follow-through-2026-09-08` (`a99ed7f`), audited and deployed with Dylan’s authorization. The first Wave 1 release is retained at `baseline/live-wave-1-2026-09-08` (`2c8ff4f`). The original pre-work theme remains at `baseline/live-2026-09-07` and Shopify theme `141825474760` as a rollback reference.
- Continue Shopify CLI work on descriptive `djh/...` branches (older work uses `feature/...` or `fix/...`) and development/unpublished themes. Current follow-through branch: `djh/wave-1-responsive-follow-up`; development theme: `142755430600` (re-resolve its role each session). Preserve audit history and track work in `docs/wave-1-progress.md`. Production repair is allowed only for confirmed broken functionality; otherwise preview and review before an authorized release.
- Pull live into a separate temporary directory using explicit `--theme` and `--path`, compare with the published baseline and reconcile merchant edits through the development branch. Never pull over uncommitted or unpublished work. Shared product/app data is not isolated by theme previews.
- The default environment identifies only this store. Never infer a production deployment from a request for local development. Do not add `allow-live`, `publish`, or a live theme ID to default write commands.
- Git tracks theme files, not products, menus, pages, metafields/metaobjects, app settings, inventory, fulfillment, or customer data. Those need separate verification in Shopify/apps.
- Keep credentials, CLI sessions, customer/order exports, and local settings out of Git. Git remote `origin` points to `https://github.com/dylanjhunt/halfday-shopify.git`. The main branch is connected to the live theme. Push only named development branches until a production release is authorized.

## Shopify architecture and simplicity

- Preserve Shopify's native directories: `layout`, `templates`, `sections`, `snippets`, `assets`, `config`, `locales`. Use Liquid, semantic HTML, CSS, JSON templates, and small vanilla JavaScript enhancements.
- Prefer existing sections, blocks, snippets, theme settings, product metafields, and metaobjects. Keep merchant content editable. Use `render` with explicit arguments for new reusable snippets.
- Make focused changes. Do not reformat the downloaded theme wholesale, introduce a framework/build pipeline, duplicate components, or rewrite Dawn without a demonstrated need.
- Inspect template assignments and dependencies before removing legacy files. Preserve Locksmith's access controls and employee/staff ordering behavior.
- Use Shopify routes, translation keys, responsive `image_url`/`image_tag`, and native forms. Preserve `content_for_header`, `content_for_layout`, editor lifecycle behavior, and app blocks.

## Brand and performance

- Match Halfday's playful nostalgic iced-tea identity: existing Strippy/Museo typography, deep green `#004600`, orange `#ff5528`, yellow `#ffe700`, and product-specific colors. Favor clear hierarchy, clean spacing, legible copy, and simple shopping choices.
- Add JavaScript only for behavior HTML/CSS/Liquid cannot provide. Prefer progressive enhancement and native controls; no new jQuery, animation, carousel, or UI dependencies without a concrete need.
- The existing `assets/custom.js` bundles jQuery and Swiper. Reduce dependencies incrementally after mapping their consumers; don't delete them blindly.
- Scope CSS/JS to the sections/routes that need them. Defer noncritical JS, avoid render-blocking third parties, repeated listeners, global polling, and duplicate asset loads. Measure before and after.
- Keep the main above-the-fold image eager with appropriate priority; lazy-load offscreen images/video, provide responsive sizes and dimensions, and minimize font variants.
- Support keyboard access, visible focus, accessible names, meaningful alt text, and reduced motion. Accessibility overlays do not replace accessible markup.

## Business context and validation

- Dylan confirmed on September 8 that customer ordering redirects to Amazon. Validate Amazon purchase links; authenticated staff/sample checkout is not a release gate for this roadmap. Preserve existing Locksmith and legacy native purchase code unless a separate change is authorized. Public product pages link to Amazon. Shopify inventory at a 3PL must not be presented as Amazon availability. Preserve real Shopify inventory checks on actual Shopify purchase paths.
- Audit priorities: availability messaging, 4-packs/slim cans, Klaviyo, SEO/AEO, legacy content, Cin7/ShipStation/AfterShip/Faire, and Yotpo-to-Bazaarvoice planning. Do not activate flows, uninstall apps, or alter integrations as part of an audit.
- GA and Google Ads are deferred until Dylan confirms access. Klaviyo access is available and was audited; see `docs/klaviyo-audit-2026-09-07.md`. Dylan confirmed GTM was unused/empty and asked not to pursue it; leave it alone unless scope changes.
- Run Theme Check and distinguish inherited findings from regressions. Verify relevant desktop/mobile pages, keyboard navigation, variant/media interactions, Amazon destinations, and protected staff flows as applicable. Do not place orders or subscribe real people during tests.
- Separate confirmed defects, hypotheses, and access-dependent checks. Theme code cannot establish integration health, conversion performance, or retailer review syndication.
