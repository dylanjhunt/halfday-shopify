# Wave 1 release and Agentready verification, September 9, 2026

## Released to production

Dylan authorized pushing the combined Wave 1 work to main. Release **`bb0169f42a4490dae91d45824fac7819fbfa30b5`** is pushed to GitHub main and live on Shopify theme **142757101768**, `halfday-shopify/main`. Immutable tag: **`baseline/live-wave-1-2026-09-09`**. Further work is on **`djh/wave-1-agentready-verification`**, development theme **142755430600**.

The release includes tablet flavor-label spacing, correctly sized product/gallery and hover images, deferred collection promotional videos, conditional cart-drawer CSS, announcement contrast, gallery/list semantics and empty article-heading cleanup. The Adobe font experiments were reverted before release. Earlier gallery, review-layout, SEO, accessibility and performance repairs remain included.

Before merging, a fresh fetch found Shopify's overnight Locksmith update `b17447a`. Its four changed snippets were merged into the development branch and re-uploaded through CLI for verification, preserving the merchant/app changes. No live theme was overwritten by a CLI push.

## Release evidence

- Fresh pre-release downloads matched all 455 live files to `b17447a` and all 455 development files to the prepared candidate before reconciliation.
- Theme Check after reconciliation: **122 inherited errors / 388 warnings**, unchanged from the audited candidate. This is not a clean Theme Check pass.
- All 15 public live/development routes passed regression checks before and after release: Amazon destinations and attribution parameters, expected external loaders, Klaviyo identifiers, markup and protected-code comparisons. [Pre-release report](../reports/wave-1-release-regression-2026-09-09.json), [post-release report](../reports/wave-1-post-release-2026-09-09.json).
- A fresh Shopify CLI pull after deployment matched **all 455 live theme files exactly to main `bb0169f`**. Local temporary snapshots: `/private/tmp/halfday-release-20260909/live-before`, `dev-before`, and `live-after`.
- Exited the browser preview before live QA. Inspected Shop All at desktop width and followed the Green Tea link by keyboard. Live Green Tea was visually checked at desktop, 1024px tablet and 390px mobile widths. Tablet labels fit, gallery layout and Amazon/store-locator CTAs remained intact, with no horizontal overflow observed.
- These checks supplement the [combined visual/performance audit](wave-1-lcp-completion-2026-09-08.md). They do not prove every interaction on every device or analytics event receipt. No orders or signups were submitted.
- No new speed benchmark was measured during deployment. September 8 evidence remains: Shop All initial transfer about 69% lower and median lab LCP 4.18s to 3.53s; product LCP remained variable. Do not present those as new production field results.

The pre/post reports intentionally retain the comparison baseline used at execution, `baseline/live-wave-1-follow-through-2026-09-08`. Future regression runs use the new September 9 tag.

## Agentready recheck

See the [updated app feedback](agentready-product-feedback.md) for detailed acceptance gaps. The saved 34-change Concierge run still returns `unsupported_field`; Dylan confirmed the fix is being worked on. No further Apply retries were made after that confirmation.

The latest UI supports explicit catalog approvals, separate output formats, catalog pausing, no-return policies, valid custom policy URLs and recovery to the saved plan. A controlled test enabled only Agent JSON and only the development theme embed while the catalog was paused and approved handles were blank. The homepage emitted a valid brand/policy block, while Lemon Tea and the protected staff collection emitted no Agentready blocks. Both sampled product markdown endpoints returned 404 with private/no-store caching. Production remained off throughout.

All temporary controls were restored: both format switches off; development embed disabled and CLI read back byte-for-byte against the committed config; production embed off; catalog pause restored to its original off state; approved handles blank and channel approvals off. Product inclusion remains off, with all 45 selectable products explicitly hidden. The curated discovery file was regenerated after restoration and returned 200, with the correct retailer-aware description, policies and All Rights Reserved, and no product detail links or staff markers. This discovery file is separate from the disabled theme output.

## Remaining Wave 1 dependencies

1. Agentready Apply fix, current sync/description precedence, retailer-safe product output, schema ownership and approved-catalog/channel verification before activation.
2. Approved consumer 4-pack/slim-can facts and assets, including SKU/GTIN, nutrition and channel details.
3. App ownership and vendor-supported scoping, particularly Signifyd; decisions on Postscript/Klaviyo overlap and accessiBe. No speculative app removals were made.
4. Editorial decisions on health/nutrition claims, retired Cranberry content and legacy campaign destinations.

Klaviyo signup, offers, welcome/browse messages and audience activation remain Wave 2. GA/Ads remain deferred and GTM excluded. Main is live; subsequent theme changes require development preview and a separately authorized release.
