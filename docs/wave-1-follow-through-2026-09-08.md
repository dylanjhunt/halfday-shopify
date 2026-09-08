# Wave 1 follow-through after publication

Dylan published `halfday-shopify/main`, theme **142757101768**, on September 8, 2026. Shopify CLI confirmed its live role, and a fresh download matched all **455 files** at `2c8ff4f`. This is now the benchmark, tagged `baseline/live-wave-1-2026-09-08`. The previous live theme **141825474760** remains unpublished as a rollback reference.

This follow-through is on **`feature/wave-1-follow-through`**, using Shopify CLI development theme **142755430600**. Main and production were not changed. [Development preview](https://drinkhalfday.com/?preview_theme_id=142755430600).

## Completed in this preview

| Item | Result |
| --- | --- |
| Product gallery media | Removed a second immediate media render that bypassed Dawn's existing deferred-media template. Shopify gallery video now loads after a click or keyboard Enter, has native controls, and pauses when leaving its slide. The visible play prompt is scoped to product galleries. No new dependency. |
| Collection images | Shop All and Variety Packs now render one responsive picture using their existing mobile/desktop image metafields. The browser chooses the relevant artwork; the hero remains eager/high priority and keeps the same frame/crop. Existing video/mixed-media fallback behavior is retained. |
| Collection headings | One H1 contains the existing breakpoint-specific merchant headings. Text, font, color and measured dimensions are unchanged at 390px and 1440px. |
| Live-main workflow | Updated Claude/project guidance, README and the roadmap. New feature branches start without tracking main. The regression checker now compares protected code/settings with the published baseline and confirms the development theme differs from the current live theme. |

Customer ordering routes to Amazon, as Dylan confirmed. Authenticated staff/sample checkout is not a release gate. Existing native purchase and Locksmith code remain intact.

## Verification

- Product gallery: first render contains **zero video elements**, compared with one previously. Desktop keyboard Enter and mobile click load and play exactly one Shopify video with controls; moving to the next slide pauses it. First-image/title geometry matches before and after at 390px and 1440px, without mobile overflow.
- Collection: one image and one H1 on Shop All and Variety Packs. Shop All selects `collection-hero.jpg` on mobile and `Rectangle_3166.jpg` on desktop. Heading rectangles, typography and color match. Mobile category expansion and desktop navigation to Variety Packs work; screenshots retain the design.
- The [15-route regression check](../reports/wave-1-follow-through-regression.json) preserves Amazon destinations and attribution parameters, Klaviyo embed IDs, integration markers, external script loaders and protected/native purchase code. This is not proof of downstream analytics receipt or Amazon sales.
- Theme Check remains **122 inherited errors / 391 warnings**, with no added offenses. JavaScript syntax, the existing motion lifecycle harness and whitespace checks pass. Theme Check is not a clean pass.
- Five development files were read back byte-for-byte, including the unchanged shared video snippet. The final theme-code diff contains four files. [Verification and performance evidence](../reports/wave-1-follow-through-verification.json).

## Performance findings and limits

Lighthouse 13.4.1, default mobile simulation, fresh browser profiles, no request blocking. The initial comparison used one public live sample and two development samples. The preview includes Shopify tooling and third-party activity varies, so it cannot isolate causality for LCP/TBT.

| Lemon product page | Published public sample | Development sample 1 | Development sample 2 |
| --- | --- | --- | --- |
| Initial transferred data | 14.70 MB | 6.15 MB | 6.05 MB |
| Initial video transfer | 8.96 MB | 0 MB | 0 MB |
| LCP | 3.55s | 26.83s | 12.26s |
| CLS | 0.04335 | 0 | 0.04339 |
| TBT | 2,270ms | 1,174ms | 4,664ms |

The verified improvement is removal of the unrequested gallery-video transfer. It is not a verified LCP improvement. The slower preview LCP readings remain visible here rather than being discarded. Both use the same first gallery image with eager loading and high priority. The baseline layout-shift trace identifies late Yotpo rating rendering; the image/header fixes do not eliminate that separate widget behavior. All five console-error audits pass.

A follow-up comparison temporarily restored the original product CSS, JavaScript and media snippet on the **same development theme and URL**, then restored the final edits:

| Same preview comparison | Original product code | Restored final edits |
| --- | --- | --- |
| Initial transferred data | 15.20 MB | 6.21 MB |
| Initial video transfer | 8.96 MB | 0 MB |
| LCP | 5.02s | 3.79s |
| CLS | 0.000473 | 0.000130 |
| TBT | 2,444ms | 2,011ms |

This pair did not reproduce a consistent slowdown. It also does not establish a reliable LCP improvement given the earlier outliers. All results are retained. The final development code was restored and read back; no baseline experiment changed production.

Raw Lighthouse data remains outside Git at `/private/tmp/halfday-wave1-finish/`. Only sanitized summaries are committed. Measurements cover initial navigation, not video consumption after the shopper presses Play.

## Open Wave 1 work

1. **LCP and review-widget CLS:** investigate remaining script/font/render delays and establish a supported approach to Signifyd scoping. The review slot needs a deliberate zero-review state before reserving space. App configuration and future review migration affect the whole store.
2. **4-packs and slim cans:** approved consumer versus logistics-case records, SKU/GTIN, nutrition/caffeine facts, imagery, intended channel and Amazon destinations. These decisions gate public format merchandising and comparison copy.
3. **App cleanup:** Signifyd owner/vendor scoping, Postscript versus Klaviyo SMS ownership, and accessiBe ownership. Yotpo remains until Bazaarvoice migration is verified. No app was uninstalled or globally disabled in this pass.
4. **Agentready:** recheck endpoint visibility/exclusions and rendered store data when Dylan's app fixes are ready. Keep the documented safeguards meanwhile.
5. **Editorial decisions:** approved health/nutrition claims, Subscribe page purpose, and destinations for retired Cranberry/overlapping content. Do not invent claims or redirect useful content without a destination decision.

The published first release and this development follow-through are concrete completed work. Wave 1 as a whole still has the dependencies above. Klaviyo signup/offer work belongs to Wave 2; GA/Ads remain deferred and GTM excluded. The next main merge/push is a production deployment and requires release authorization.
