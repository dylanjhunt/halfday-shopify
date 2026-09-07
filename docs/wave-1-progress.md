# Wave 1 progress

**Status: in progress, first development checkpoint available. September 7, 2026.**

- Branch: `dev/wave-1`.
- Development theme: `142755430600`, Development (deb269-MacBook-Pro-4).
- [Preview](https://halfday-tonics.myshopify.com?preview_theme_id=142755430600) · [Theme editor](https://halfday-tonics.myshopify.com/admin/themes/142755430600/editor).
- Latest live theme was pulled before edits; it matched the committed baseline. No merchant changes needed merging.
- **Production changes: none.** No products, menus, articles, metafields, app settings, subscribers or inventory records were modified. This checkpoint is entirely theme-scoped.

## Implemented in development

| Item | Change | Verification |
| --- | --- | --- |
| Deferred video | Testimonial/Instagram video sources stay in inert templates until their cards enter the viewport. Pause when offscreen or the tab is hidden; retain posters for reduced motion and playback rejection. | Browser: zero loaded video elements initially; visible footer videos load/play; loaded videos pause after returning to top. Three Lighthouse preview runs transferred zero video bytes before scrolling. |
| Sized posters/images | Responsive, lazy posters and card images replace master-sized/undefined-width output in the two media snippets. | Rendered posters retain the original card geometry. No new image-processing dependency. |
| Duplicate Instagram markup | Remove the second server-rendered item list; the existing marquee already creates its own loop copy. | Preview retains the strip and its links. Offscreen loop copies do not start video downloads. |
| Product-image priority | Only the first visible gallery image gets high fetch priority. | Lemon, Classic Variety and Strawberry slim-can HTML each contain one high-priority image; mobile gallery Next works. |
| Locator stylesheet | Load `find-us.css` only on the `page.find-us` template. | Absent from home/PDP/collection/FAQ; present on Find In Store. |
| Amazon stock messaging | Suppress native/custom sold-out badges and hidden Shopify cart forms on Amazon-directed cards. Retain non-stock custom badges. Employee collections and sample-only products retain native inventory behavior. | Variety collection shows BEST SELLER/NEW badges, no native cart forms. Native buy-button/quantity inventory logic and Locksmith files are unchanged. Authenticated staff ordering still needs an owner walkthrough before release. |
| Product schema | External-CTA templates without a Shopify buy block use existing visible copy for descriptions and omit unsupported Shopify offers. Native structured data remains for templates with Shopify buying. | Valid JSON on Lemon, Classic Variety and retail-only Strawberry; populated descriptions, no fabricated price/availability. Yotpo still emits its separate existing review markup. |
| Organization schema | Stable homepage identity and nonempty social links. | Included in rendered JSON checks. |
| Utility-page discovery | `noindex,follow` for the popup test page and the six named staff/menu utility collections. | Test page and staff collection verified. Access controls/publication/sitemap membership are unchanged; noindex is not an access restriction. |
| Search descriptions | Theme fallbacks for retained shopping collections, blog, Contact and product short copy when merchant SEO description is absent. | Existing merchant descriptions take precedence. Shop All/Variety descriptions verified in preview. |
| FAQ fragments | Valid `#faq_*` links with matching existing desktop/mobile scroll selectors. | All four resolve to existing targets; mobile Orders reaches its section at the header offset. |
| FAQ copy | Draft where-to-buy and shipping answers match Amazon/retailer journeys. Correct recyclable/APO/FPO and spelling errors. | Theme JSON only. Nutrition, caffeine, health and fulfillment-policy claims still require the content review below. |
| Legacy links | Repair old shop and malformed relative links while rendering articles. Normalize the footer's old `/en-test/` flavor destination and remove redundant homepage template-preview parameters. | Server-side theme output; shared article/menu records remain unchanged. Retired Cranberry content needs an editorial destination decision. |

## Measurements and checks

Three alternating cold-profile mobile Lighthouse homepage comparisons, version 13.4.1:

| Median | Live | Development |
| --- | --- | --- |
| Transferred data | 39.99 MB | 6.81 MB |
| Initial video transfer | 32.32 MB | 0 MB |
| Simulated LCP | 3.87s | 4.68s |
| TBT | 875ms | 1,074ms |
| Performance score | 55 | 48 |

**Initial transfer is about 83% lower. LCP/TBT and the overall score did not improve in this comparison.** Preview infrastructure and third-party variability differ from production; do not call this a field-speed or responsiveness improvement. The initial loading problem is addressed, and script/render work remains. The live site's previously measured real-user Core Web Vitals passed. These tests do not measure post-scroll total video consumption.

The comparison verifies the development asset is present only in preview runs. A playback guard and FAQ copy were updated during the window; initial video deferral/poster sizing were unchanged. Raw captures remain in `/private/tmp/halfday-wave-1-performance/`; sanitized results are in [performance comparison](../reports/wave-1-performance-comparison.json).

- [Rendered preview checks](../reports/wave-1-preview-checks.json): representative home, collection, PDP, FAQ, locator and utility routes, with preview identity checked. The verifier preserves Shopify's anonymous preview cookie across redirects without saving it.
- Theme Check: **126 errors, 361 warnings**, identical to the inherited baseline, **no new offenses**. [Comparison](../reports/wave-1-theme-check-comparison.json). This is not a clean Theme Check pass.
- JavaScript syntax checked with Node. Git whitespace checks completed before commit.
- No order, signup, review migration, app uninstall, campaign activation or production release was performed.

## Still to tackle / decisions needed

| Item | Next step / dependency |
| --- | --- |
| 4-packs | Confirm the consumer 4-pack versus 24-pack logistics-case records, SKU/GTIN, approved imagery, channel and purchase links. Do not expose case SKUs as consumer packs. |
| Slim cans | Confirm 45 versus 40 calories, tea ingredients, caffeine, approved images and the sample-only/access restrictions before making products publicly discoverable. Fix display-title/content fields after those decisions. |
| CRO/content hierarchy | Finish format discovery, product comparisons and primary CTA placement using the approved catalog. Current public product CTAs and gallery behavior are preserved. |
| Apps | Review Signifyd scoping with its owner; settle Postscript/Klaviyo SMS ownership; decide whether accessiBe remains needed. Shared app settings affect production and are not isolated by this preview. No speculative uninstall. |
| Further speed work | Investigate remaining script/main-thread costs and route asset loading; preserve the byte reduction while seeking repeatable LCP/TBT improvements. Compare matched preview/baseline conditions before attributing a vendor's cost. |
| SEO/content | Review retained page titles/headings/alt text; confirm Subscribe page purpose; review nutrition/caffeine and old health claims. Choose retired Cranberry and overlapping blog destinations using content/Search Console evidence when available. |
| Store-data cleanup | After preview approval, decide whether to migrate theme-level article fixes into source content and add redirects. Noindex does not remove retained utility URLs from Shopify's sitemap. |
| Release QA | Owner walkthrough of authenticated staff/sample buying, desktop/mobile content review, reduced-motion setting check, and final production comparison/merchant-diff refresh. |

The signup/offer and lifecycle work belongs to Wave 2 of the latest three-wave plan. GA/Ads remain deferred; GTM remains excluded.
