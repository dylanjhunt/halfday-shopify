# LCP and CLS follow-up, September 8, 2026

Work is on `dev/wave-1` and development theme **142755430600**. Production theme code, app settings and shared store data were not changed. Fresh live and development downloads matched `main` and `2de8851` before edits.

## What matters for Halfday

LCP measures when the largest visible image/text paints. Aim for **2.5 seconds or less** at the 75th percentile of real visits. The image needs early discovery, the right priority and suitable dimensions, but CSS/fonts and script work can still delay its paint after download. [Google: optimize LCP](https://web.dev/articles/optimize-lcp).

CLS measures unexpected movement. Aim for **0.1 or less** at the 75th percentile. Reserve image, logo and embedded-content space before loading; preserve layout during font and widget updates. A navigation Lighthouse run cannot cover every later shift caused by scrolling, popups or interactions. [Google: optimize CLS](https://web.dev/articles/optimize-cls).

The earlier field-data audit showed the live homepage passing Core Web Vitals. The numbers below are local mobile lab simulations against a preview, not updated field results.

## Implemented and verified

- **Product header space:** the product-specific logo used the metafield wrapper's missing aspect ratio. Its rendered height attribute was absent. The loading trace showed the main page moving from y=63 to y=99 as the header grew by 36.125px. Read the logo's image value for its aspect ratio, URL and alt text in both header layouts. The final loaded logo rectangles remain identical at 390px and 1440px.
- **Product-card image metadata:** replace the malformed custom-primary-image srcset and empty width/height with Shopify `image_tag` output from the actual image object. Resolve hover-image dimensions from its value too. Supply the featured carousel's actual 256px image slot rather than a generic two-column estimate. Keep the card aspect ratio, crop, artwork, links, hover media and buying logic.
- **Responsive hero dimensions:** give the homepage picture's mobile source its own width/height, matching its different artwork aspect ratio. Existing reserved hero geometry and eager/high priority remain.
- **FAQ banner:** one picture selects the mobile/desktop artwork. This avoids rendering two image elements and promotes the first-section banner from low to high priority. It has explicit widths/sizes and retains the existing desktop/mobile aspect ratios and crop.
- **Contact retailer logos:** below-fold logos are lazy/low priority instead of high priority. Their raster source is capped at 168px tall for the existing maximum 56px display height. SVG logos remain vector artwork. All 22 rendered logo instances and their existing links remain.

No new JavaScript, app removal, tracking change or production release. The extra Adobe preconnect/earlier-font-preload experiment was reverted because the first measurement batch did not establish a benefit. The prior single Strippy preload remains exactly as committed before this pass. All experimental samples are retained in the report.

## Measurements

Lighthouse 13.4.1, sequential fresh profiles, default mobile simulation. No network/app blocking. The first before/experimental homepage captures overlapped routine CLI/markup checks; shared workstation and third-party variation are limits. Interactive preview navigation did not run during measurement batches.

| Metric | Before, three runs | Final development |
| --- | --- | --- |
| Homepage LCP | 4.39s median; 4.16–6.91s range | 4.22s median; 4.04–29.78s range, three runs |
| Homepage CLS | 0.000112 median | 0.000041 median, three runs |
| Lemon PDP LCP | 5.90s median; 5.50–26.80s range | 4.72s, one final confirmation |
| Lemon PDP CLS | 0.041498 median | 0.000208, one final confirmation; earlier three after-change samples ranged 0.000151–0.000511 |

**The header CLS repair is verified. Consistent LCP improvement is not established.** The initial after-change batch with the font experiment had 11.36s median homepage LCP; after reverting it, two homepage runs returned to about 4 seconds but one still reached 29.78s. That does not establish the font hints as the cause of the outliers. Keep investigating the render delay rather than describing a lower median as a reliable speed gain. TBT also remains variable.

In the slow homepage traces, the hero was downloaded substantially before it painted. The report retains unthrottled LCP subpart durations separately from simulated metrics; these are different measurement models and must not be directly added or compared. A smaller hero download alone cannot remove script/CSS/font render delay.

[All measurements, including experiments and outliers](../reports/wave-1-cwv-performance.json). Raw Lighthouse data stays in `/private/tmp/halfday-cwv/performance/`; no browser sessions, cookies or customer data were added to Git.

## Remaining work, in order

1. **Signifyd scoping:** its scripts remain a major measured CPU cost. Confirm vendor-supported profiling rules for public Amazon/retailer discovery pages while preserving genuine Shopify/staff checkout coverage. Earlier audit request-blocking tests identified an opportunity; they are not a supported production configuration or a guaranteed saving. Do not filter app scripts out of `content_for_header`.
2. **Render-blocking dependencies:** card/quick-order stylesheet deduplication and conditional loading are complete in the subsequent quick-wins pass. Adobe's font CSS/import chain and late Yotpo typography remain candidates for controlled testing. Preserve Halfday's brand fonts and avoid introducing font-swap shifts to improve a score.
3. **Review-widget space:** desktop Yotpo can add a rating row and move the product heading about 42px after hydration. Reserve a confirmed slot with an explicit zero-review behavior as part of review migration planning. This pass does not add empty space to every product or invent review counts.
4. **Remaining secondary media:** Contact/content split-image cleanup is complete in the subsequent quick-wins pass. Browser checks confirm breakpoint source selection, retained frame dimensions and crop-aware sizing. Measure representative content pages after any approved release.
5. **Release validation:** authenticated staff/sample ordering, agreed catalog/content decisions and exact merchant diff review are still required. Recheck real-user CWV after an approved production release; preview lab results cannot establish field improvement.

## Regression checks

- [Nine-route image checks](../reports/wave-1-cwv-markup.json): positive logo/card dimensions, valid width descriptors, a single FAQ picture and 22 lazy/low-priority Contact logos. Public and protected staff route responses remain valid.
- [15-route regression checks](../reports/wave-1-regression-markup.json): Amazon URLs including attribution parameters, Klaviyo embed IDs, external script loaders, integration markers and protected/native cart code preserved.
- [Browser review](../reports/wave-1-cwv-browser.json): homepage/FAQ geometry and product-logo geometry retained at 390px and 1440px; mobile FAQ image loaded without horizontal overflow; product card Enter navigates to Lemon Tea; gallery Next moves 1/5 to 2/5. Asynchronous Yotpo insertion is recorded separately from theme geometry.
- [Theme Check](../reports/wave-1-cwv-theme-check.json): **122 inherited errors / 397 warnings**, no added findings, five undefined-image-variable warnings removed. This is not a clean Theme Check pass.
