# Wave 1 performance and readiness checkpoint

All changes in this checkpoint are on `djh/wave-1-responsive-follow-up`, alongside the tablet flavor labels. Shopify CLI preview: [development theme 142755430600](https://drinkhalfday.com/?preview_theme_id=142755430600). Main remains at the published `a99ed7f` baseline. This checkpoint prepares a combined release; it does not publish one.

## Completed

| Improvement | Result and boundaries |
| --- | --- |
| Collection promotional video | Reused the existing visibility-aware video component for the collection's three promotional video branches. Videos are instantiated only when visible, pause offscreen, and retain a poster without JavaScript or with reduced motion. Hidden desktop/mobile alternatives do not both start. No additional video library or loader. |
| Product image sizing | The main product gallery now sizes contained images for the actual drawn image inside Halfday's frame. Added smaller responsive candidates. Cropped lifestyle slides and other Dawn gallery consumers keep their existing sizing. Artwork, frame geometry and priority are retained. Blank leading product-image alt text falls back to the product name. |
| Card hover media | Secondary images can select 240–640px sources instead of starting at 720px, using the same slot sizes as the primary image. Existing images, hover CSS, links and video branch are retained. |
| Cart CSS and font experiment | The drawer's quantity stylesheet is nonblocking; collection-card CSS loads there only when a drawer collection is configured. Native cart code is preserved. Both broad and product-only nonblocking Adobe-font experiments were reverted after inconsistent results. The existing licensed embed and brand typography remain. |
| Accessible galleries and collection lists | Corrected gallery list nesting and Swiper's slide role. Injected collection promotions are list items, and collection card titles use H2 directly below the page H1. Other card consumers keep H3. Keyboard gallery navigation and video playback remain functional. The only change to the custom JavaScript bundle is the Swiper accessibility option; libraries and event logic are unchanged. |
| Announcement readability | Preserve the merchant's chosen text color when it meets 4.5:1 contrast. Otherwise select a readable brand green, white or black against the existing background. The orange collection announcement now uses black text. Copy, links and bar height are unchanged. |
| Tablet flavor selection | The previously committed 990–1280px refinement remains on this branch. Three columns and slightly smaller labels keep Watermelon and Raspberry inside their links. This intentionally adds a flavor row and moves purchase buttons down. See the [responsive audit](wave-1-responsive-follow-up-2026-09-08.md). |

The collection video was a separate remaining source of early transfer after the previous gallery-video release. The earlier PDP fix did not cover these promotional videos.

## Verification

- At 390px and 1440px, the main product image retains its frame and the product heading retains its geometry. Settled 768px product layout also matches live. No horizontal overflow in these checks. Asynchronous ratings can change the collection card row height while loading; comparisons must use settled content.
- Keyboard Enter plays the product video with controls. Leaving that slide pauses it. List items retain correct roles after Swiper initializes.
- At 390px, the collection promotion retains its 350 × 462px frame. It has no video element on initial load, plays after scrolling into view, and pauses after returning to the top. The hidden desktop alternative remains unloaded. Desktop list and promotion layout are also checked.
- Existing motion lifecycle checks cover lazy initialization, visibility, focus, reduced motion and editor cleanup. No new runtime dependency was introduced.
- The [15-route live/development comparison](../reports/wave-1-lcp-regression.json) checks Amazon URLs including attribution parameters, Klaviyo embed IDs, external loaders, forms, integration markers, protected code and merchant settings. These checks do not prove downstream analytics receipt, full attribution or Amazon sales. No orders or signups are submitted.
- Fresh Shopify CLI downloads match all **455 development files** to local code and all **455 live files** to `main` at `a99ed7f`. No merchant drift or production changes. [File/lint verification](../reports/wave-1-lcp-verification.json).
- Desktop/mobile announcement links inherit the resolved readable color; the Green Tea bar retains brand green against mint. Collection card H2s retain 27.5px typography and their existing line heights. Keyboard selection of Green Tea reaches its correct product.
- Theme Check has **122 inherited errors / 388 warnings**, zero added offenses against the pre-change development baseline. This is not a clean lint pass. Three existing warnings were removed. JavaScript syntax and Git whitespace checks pass.

## Measurements

See [sanitized Lighthouse evidence](../reports/wave-1-lcp-performance.json). All runs use fresh mobile browser profiles on the same development theme, without blocking apps. Raw reports remain outside Git under `/private/tmp/halfday-lcp-finish/performance/` because request/session details do not belong in the repository.

The evidence distinguishes `before` (tablet branch baseline), `font-experiment` (isolated broad font experiment), `after` (earlier combined candidate with broad font loading), `product-font-candidate` (the rejected product-only font experiment), and `final` (the retained implementation, including collection video deferral with the original font loader). Home/collection performance captures precede the final semantic card-heading and desktop announcement-link inheritance refinements; browser checks confirm unchanged mobile geometry. Slow samples are retained. Observed LCP breakdown timings and Lighthouse's simulated LCP use different timing models and must not be added together.

| Route | Baseline mobile LCP median (2 runs) | Retained mobile LCP median (3 runs) | Initial transfer, baseline → retained median |
| --- | --- | --- | --- |
| Homepage | 4.20s | 4.13s | 6.80 → 6.73 MB |
| Shop All | 4.18s | 3.53s | 19.75 → 6.07 MB |
| Lemon Tea | 5.65s | 4.15s | 6.18 → 6.06 MB |

Shop All's retained LCP samples are 2.89s, 3.53s and 3.72s, compared with baseline 4.21s and 4.14s. Initial promotional-video transfer falls from 10.63/15.64 MB to **zero in all three retained runs**. This is a 13.68 MB median reduction in total initial transfer, about 69%. The collection median LCP is about 15% lower in this local sample; it is not a field Core Web Vitals claim. Homepage LCP is effectively unchanged.

Lemon's retained samples are **3.83s, 4.15s and 10.44s**. The median is lower, but the outlier means product LCP remains unreliable. Its leading can image now selects 375px instead of 713px in the mobile lab profile, about **65 KB instead of 155.5 KB** transferred (58% less). All nine retained runs record CLS below 0.002 and pass the console-error audit. These are lab observations, not field monitoring.

The rejected product-only font samples were 4.36s, 8.99s and 28.84s. An earlier candidate also had 28.90s/31.08s homepage/collection outliers. These are retained as evidence, not treated as successful optimizations. Signifyd CPU and general third-party variation remain relevant; these experiments do not isolate the cause of each slow run.

## Final SEO and accessibility findings

The [fresh sitemap crawl](../reports/wave-1-seo-closure.json) covers 71 URLs. Three requests were initially rate-limited during the final refresh; all passed a later, sequential retry, with the failures retained in the report history. All return 200 on the verified preview with parseable JSON-LD and no Liquid errors or `/en-test/` links. The crawl exposed an empty `<h1><span></span></h1>` in the prebiotics/probiotics article body; the theme now removes that exact empty artifact while retaining the real article H1 and shared source record.

Six retained utility/staff collections intentionally have noindex and no description. Popup Testing remains noindex. HelloFresh and Subscribe are legacy campaign pages with missing H1s; Subscribe also lacks a description. Their configured giveaway ended March 31, 2025. Updating or retiring those campaigns requires the existing content/offer decision rather than adding fresh promotional search copy.

This is not a complete WCAG audit. Remaining automated findings include app-owned Yotpo ARIA, Klaviyo popup image alt text and iframe titles. Existing orange/white button and footer combinations and orange-on-yellow headings also need a broader brand contrast pass; the announcement fix is deliberately scoped. Track those visual-system changes and app-rendered markup separately from this measured LCP release.

## Remaining Wave 1 disposition

| Area | Completed or next dependency |
| --- | --- |
| Theme speed and CLS | Initial/offscreen video, responsive images, image priorities, unused/repeated style loading, font preloads, logo geometry, review spacing and this final rendering pass are implemented. LCP still needs real-world monitoring after an approved release. Rewriting dependencies or removing operational scripts without knowing their owners is not a safe remaining theme-only task. |
| App cleanup | The measured Signifyd CPU cost is actionable evidence for the app owner. Confirm whether fraud/device collection is required on public Amazon-directed browsing, and obtain a supported route-scoping configuration with coverage for actual Shopify orders. Do not strip app scripts from `content_for_header`. Settle Postscript versus Klaviyo SMS ownership and accessiBe ownership before removal. Stockist and Locksmith have active storefront purposes; Yotpo remains until Bazaarvoice is validated. |
| Catalog and CRO | Public Amazon buying paths, stock messaging, discovery labels and accessible controls are repaired. New 4-pack/slim-can merchandising and format comparisons require approved consumer-pack versus logistics-case records, SKU/GTIN, nutrition/caffeine/ingredients, imagery and channel destinations. Existing 24-can case records do not establish a consumer 4-pack. |
| SEO and AEO | Existing theme metadata, channel-appropriate product data, social metadata, headings, broken legacy links, FAQ/policy answers and utility noindex rules are retained. Final sitemap verification is recorded separately. Health/nutrition claims, Subscribe purpose and retired Cranberry/overlapping-blog destinations need editorial or search-performance decisions. No bulk claim rewrite or speculative redirect. |
| Agentready | Last verified September 8 setup Apply failed with `unsupported_field`; reviewed proposals are not confirmed applied. Output-off public/staff endpoint blocking passes. Output-enabled protected exclusions, durable saves and duplicate/conflicting schema still need verification after the app fixes are ready. Embed/output safeguards remain off. The app feedback report records recovery and plan-label issues. |
| Release | Review this combined development theme, refresh the live merchant diff, then merge/push main when the combined release is authorized. Main is live. Authenticated staff/sample checkout is not a release gate per Dylan; its code and access controls are preserved. |

Wave 1 is not marked entirely complete while the catalog, app, Agentready and editorial dependencies remain. Klaviyo offer/signup/flow activation belongs to Wave 2. Fulfillment and review migration belong to Wave 3. GA/Ads remain deferred and GTM excluded.

## App-owner handoff ready to use

Signifyd: “Our public shopping journey sends customers to Amazon, while Shopify retains separate staff/sample order paths. Please confirm which storefront pages need device collection for the current fraud configuration and whether your supported integration can scope it accordingly without losing required Shopify-order coverage. We measured repeated main-thread CPU costs from `imgs.signifyd.com` and `cdn-scripts.signifyd.com`; the raw timing varies. Please identify the supported setting or implementation before we change anything.”

SMS: confirm the system of record and consent/event handoff for Postscript and Klaviyo, including any active forms, flows and revenue dependencies. Accessibility: confirm who owns accessiBe and what obligations or workflow it serves before retiring the overlay. Reviews: obtain Bazaarvoice catalog/GTIN matching, import support, onsite rendering and retailer acceptance before removing Yotpo. These are prepared questions, not messages sent or app changes made.

Technical references: [Shopify performance guidance](https://shopify.dev/docs/storefronts/themes/best-practices/performance), [Adobe's supported embed codes](https://helpx.adobe.com/fonts/web/web-design-and-development/embed-codes.html), and [Liquid color contrast](https://shopify.dev/docs/api/liquid/filters/color_contrast).
