# Halfday Shopify theme

This repository is the Shopify Online Store theme for Halfday Iced Tea, not a headless storefront or Shopify app. Store: `halfday-tonics.myshopify.com`; public site: `https://drinkhalfday.com`. Baseline: live theme `141825474760`, "HALFDAY 2.0 - PDP Update - 10 Mar 2025", downloaded September 7, 2026. Theme metadata identifies customized Dawn 15.2.0.

## Workflow

- Use Shopify CLI for theme operations. Read `README.md` and `docs/modernization-roadmap.md` for project status and the current delivery sequence. The dated store and Klaviyo audits are supporting evidence.
- `npm ci` installs the pinned local CLI. `npm run theme:list`, `npm run theme:check`, `npm run theme:dev`, `npm run theme:push:dev` are the normal commands.
- Wave 1 implementation is authorized on branch `dev/wave-1` and a Shopify development theme. Track completed work, verification and pending decisions in `docs/wave-1-progress.md`. The user permits production repairs for confirmed broken functionality; otherwise keep all changes in the development theme until release approval. Shared product/app data is not isolated by theme previews.
- `npm run theme:pull` refuses a dirty working tree. Pull and commit current merchant edits before changing code. Review JSON templates and `config/settings_data.json` carefully: these contain merchant settings.
- The default environment identifies only this store. Never infer a production deployment from a request for local development. Do not add `allow-live`, `publish`, or a live theme ID to default write commands.
- Git tracks theme files, not products, menus, pages, metafields/metaobjects, app settings, inventory, fulfillment, or customer data. Those need separate verification in Shopify/apps.
- Keep credentials, CLI sessions, customer/order exports, and local settings out of Git. No automatic GitHub or production synchronization is configured.

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

- Public product pages primarily link to Amazon. Shopify inventory at a 3PL must not be presented as Amazon availability. Preserve real Shopify inventory checks on actual Shopify purchase paths.
- Audit priorities: availability messaging, 4-packs/slim cans, Klaviyo, SEO/AEO, legacy content, Cin7/ShipStation/AfterShip/Faire, and Yotpo-to-Bazaarvoice planning. Do not activate flows, uninstall apps, or alter integrations as part of an audit.
- GA and Google Ads are deferred until Dylan confirms access. Klaviyo access is available and was audited; see `docs/klaviyo-audit-2026-09-07.md`. Dylan confirmed GTM was unused/empty and asked not to pursue it; leave it alone unless scope changes.
- Run Theme Check and distinguish inherited findings from regressions. Verify relevant desktop/mobile pages, keyboard navigation, variant/media interactions, Amazon destinations, and protected staff flows as applicable. Do not place orders or subscribe real people during tests.
- Separate confirmed defects, hypotheses, and access-dependent checks. Theme code cannot establish integration health, conversion performance, or retailer review syndication.
