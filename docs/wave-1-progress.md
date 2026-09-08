# Wave 1 progress

**Status: in progress, second development checkpoint available. September 7, 2026.**

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
| FAQ navigation | Native topic anchors and keyboard-operable details replace the legacy FAQ scroll/click scripts. | All four targets resolve; 17 questions retained. Enter opens/closes answers, and mobile Orders lands below the header. |
| FAQ copy | Draft where-to-buy and shipping answers match Amazon/retailer journeys. Correct recyclable/APO/FPO and spelling errors. | Theme JSON only. Nutrition, caffeine, health and fulfillment-policy claims still require the content review below. |
| Legacy links | Repair old shop and malformed relative links while rendering articles. Normalize the footer's old `/en-test/` flavor destination and remove redundant homepage template-preview parameters. | Server-side theme output; shared article/menu records remain unchanged. Retired Cranberry content needs an editorial destination decision. |

## First checkpoint measurements and checks

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

## Second checkpoint: performance, navigation and accessibility

All changes below are uploaded to development theme **142755430600** on `dev/wave-1`. The live snapshot was refreshed and still matched `main`. Production and shared app/store data remain unchanged.

| Completed | Result and verification |
| --- | --- |
| Defer carousels and marquees | One shared IntersectionObserver initializes content when visible and pauses autoplay offscreen, in hidden tabs, during keyboard focus and with reduced motion. Desktop/mobile quote pairs initialize together only at their visible breakpoint. Initial mobile preview: zero initialized Swipers and zero video elements. Product carousel Next advances 1/8 to 2/8; galleries remain immediately available. |
| Remove continuous polling | Removed the sitewide 100ms landing-page link loop. A MutationObserver runs only inside the relevant HelloFresh content panel to handle its asynchronously inserted links. Landing-page header scrolling is also scoped to landing pages. |
| Native FAQ | Replaced approximately 180 lines of global, overlapping FAQ handlers with native details/summary and ordinary anchor links. The mobile topic list remains visible; no dropdown script is required. Reworked scoped CSS to retain Halfday typography, colors and spacing. Verified 17 questions, keyboard expansion, four topic targets, no horizontal overflow at 390px and 1440px. |
| Safe anchor navigation | Removed the footer handler that interpreted ordinary URLs as fragment selectors. Valid local anchors use the browser; legacy accordions open only if the target exists. Clicking footer Flavors reaches Lemon Tea. |
| Repair header disclosures | Shop now uses the native details/summary markup expected by Dawn. This fixes the constructor/scroll errors from trying to close a nonexistent details element. Enter opens Shop, Escape closes it, expanded state and backdrop clear correctly, and the visible menu carousel initializes. Hover remains available; menu category previews also respond to focus. Optional search-modal close is guarded when the modal is absent. |
| Responsive hero | A single picture selects the mobile or desktop artwork, has explicit responsive sizes and keeps eager/high priority. It also works if only one image setting is populated. Verified the 390px layout and desktop layout with loaded images and no overflow. |
| Headings and link names | Homepage content supplies the H1 instead of the logo. FAQ banner has a configurable H1. Product image links, retailer links, mobile locator icon and footer logo now have accessible names; product detail links identify the product. Decorative video posters have explicit empty alt text. Homepage Lighthouse link-name audit now passes. |
| Theme validity | Fixed two Liquid/HTML parser errors, the invalid password-section schema property and an unsupported filter in swatch render arguments. Removed unused undefined header arguments. No new runtime dependency or build tool. |

### Second checkpoint evidence

Three previous-checkpoint runs and three delivered-theme runs without concurrent preview navigation, same Lighthouse 13.4.1 mobile settings and preview URL:

| Median | Previous checkpoint | Delivered theme |
| --- | --- | --- |
| Theme custom.js attributed main-thread work | 1,450ms | 121ms |
| Total transferred data | 6.96 MB | 6.84 MB |
| Initial video/media transfer | 0 MB | 0 MB |
| Simulated LCP | 4.34s | 4.13s |
| Total blocking time | 1,092ms | 1,054ms |
| Performance score | 48 | 50 |
| Accessibility score | 86 | 89 |
| SEO score | 77 | 85 |

**Theme JavaScript work fell about 92%; consistent whole-page LCP improvement is not established.** An intermediate batch reached 3.79s LCP. A later batch during browser QA regressed to 28–32s simulated LCP; three additional runs without concurrent navigation returned to 3.53–4.20s. The cause of that variability is unproven. All four batches are retained in the [performance evidence](../reports/wave-1-performance-pass-2.json), rather than reporting only the best runs. These are lab results, not field CWV or conversion results. Initial media transfer does not measure post-scroll video use.

In the three isolated delivered-theme runs, median reported main-thread attribution was approximately **Signifyd 3,445ms, Klaviyo 354ms, accessiBe 244ms, Postscript 209ms and Yotpo 175ms**. These are observed CPU costs, not guaranteed uninstall savings. Signifyd is the first owner review: confirm its order-risk role and supported storefront scoping before changing it. Do not strip fraud scripts out of `content_for_header`. Klaviyo/Postscript ownership and offer cleanup remain part of the lifecycle plan; Yotpo stays until the review migration has an approved export/replacement path.

- [Rendered route checks](../reports/wave-1-preview-checks.json): all 13 representative routes pass; development assets are present and no Liquid errors render. Native product gallery Next advances 1/5 to 2/5, with one high-priority gallery image and the existing Amazon destination retained.
- [Theme Check comparison](../reports/wave-1-theme-check-pass-2-comparison.json): **122 errors, 404 warnings**. Four inherited errors are fixed. Parsing the formerly invalid mega-menu exposes 52 existing warnings in its untouched Locksmith/generated logic; nine older warnings disappear. This is not a clean Theme Check pass and does not mean 43 new code defects were introduced.
- `node scripts/test-motion.cjs` passes the lazy initialization, focus, tab visibility, reduced-motion, instance reuse and editor-unload lifecycle checks. Reduced motion is covered by the behavior harness; a real OS/browser preference walkthrough remains part of release QA.
- JavaScript syntax and Git whitespace checks pass. A separate fresh Lighthouse console audit reports zero errors. Two unsourced MutationObserver errors appeared in the long-lived interactive browser session and did not reproduce in that fresh audit; the known header stack stopped recurring after its repair.
- Raw captures remain under `/private/tmp/halfday-wave1-next/`; only sanitized performance summaries are committed. No customer data, credentials or anonymous preview cookies are exported.

## Third checkpoint: interaction, visual and tracking regression review

Completed September 7, 2026 (Toronto), on `dev/wave-1` and development theme **142755430600**. A fresh CLI download of the live theme still matched `main`. All changes below are theme-scoped and uploaded through Shopify CLI. Production and shared store/app data remain unchanged.

| Completed | Result and verification |
| --- | --- |
| Shop pointer regression | Hover opened the native disclosure, so the first mouse click immediately closed it. Preserve the first click after hover; subsequent clicks toggle normally. Real browser checks: first click opens, second closes, Enter opens, Escape closes. Learn opens by mouse. Category previews now clear stale timers and are scoped to their menu. |
| Header visual regression | Native summary inherited extra right padding and shifted Learn 11px. Restore the original spacing. Live and development now both place Shop at x=40 and Learn at x=141.14 at 1440px. |
| Legacy mobile navigation | The Variety Packs CTA used a retired `/en-test/` product path plus old preview theme ID `140338692296`. Normalize three verified old destinations and remove only internal `preview_theme_id` parameters when rendering header links. Other query parameters and external URLs are preserved. Mobile drawer CTA reaches Classic Variety while retaining the current development assets. Shared menus/metaobjects are untouched. |
| Footer keyboard and resize | Mobile menu headings use buttons with expanded state and visible focus. Enter opens About; Space closes it. Returning from 390px to 1440px shows all three desktop link groups even after closing a mobile group. Respect reduced motion for the footer animation, smooth scrolling and decorative spin. |
| Landing-page broken social link | Correct the LP footer's concatenated TikTok/Twitter URL to the existing X profile destination in development section settings. No campaign or app setting changes. |

### Regression coverage

- **15 live/development routes pass** the [markup comparison](../reports/wave-1-regression-markup.json): HTTP 200, verified development assets, no rendered Liquid errors, identical Amazon destinations including attribution query parameters, unchanged Klaviyo embed IDs, no removed external script loaders or product data IDs. Integration-marker presence matches. No legacy internal preview links remain in these development pages. Re-run with `python3 scripts/verify-regressions.py`.
- Theme settings, Locksmith snippet and native product/cart scripts remain byte-for-byte identical to `main`. The bundled jQuery, marquee and Swiper library code is unchanged. Removed hidden cart forms on Amazon-directed cards are the earlier intended change; primary product/contact/landing-page and protected staff form signatures remain intact.
- **Desktop/mobile hero comparison:** at 1440px and 390px, live/development hero, heading-wrapper and CTA-wrapper rectangles match exactly. Screenshots retain the artwork, crop, typography and colors; neither viewport has horizontal overflow. This is representative visual QA, not a pixel comparison of every page or browser.
- **Real interactions checked:** desktop Shop/Learn, menu category switching, keyboard open/close, mobile drawer and Variety Packs CTA, Classic Variety gallery Next (1/2 to 2/2), footer keyboard/resize, and Stockist locator search for ZIP 10001 returning stores. Previous checkpoint covers FAQ questions/topic anchors, product carousel Next, Lemon gallery and video visibility behavior.
- **Signup UI:** the existing offer teaser opens its email dialog by keyboard and Close dismisses it; the preview toolbar overlaps pointer clicks at that location. HelloFresh's asynchronously loaded first-name/email/phone/consent form appears. Nothing was entered or submitted. Its current form contains no `h6 a` links, so the scoped link observer has no live target to exercise in this form version.
- **Tracking transport:** a fresh anonymous homepage capture has the same successful Klaviyo onsite analytics (200/202), Postscript page-event (200) and Signifyd loader (200) requests as the earlier live baseline, with zero console errors. The [sanitized network summary](../reports/wave-1-tracking-transport.json) retains endpoint/status counts only. HTTP success verifies transport, not event payload correctness, identified profiles, purchases or complete attribution. Amazon links retain their destinations and parameters; external checkout completion was not tested.
- **Checks:** motion lifecycle harness and JS syntax pass. [Theme Check comparison](../reports/wave-1-regression-theme-check.json) remains **122 errors / 404 warnings**, with zero added or removed findings against checkpoint two. Git whitespace checks pass. Existing Theme Check debt remains.

Release still needs authenticated staff/sample ordering QA, a real reduced-motion preference walkthrough and conversion/identified-user validation. GA/Ads remain deferred and GTM excluded. The HelloFresh page still advertises an offer ending March 31, 2025; its disposition belongs to the campaign/content review rather than silently extending an expired offer.

## Still to tackle / decisions needed

### Agentready / SEO follow-up

Dylan authorized Agentready onboarding and configuration. Shopify currently requires a passkey verification before the app can be inspected; app setup and the post-setup audit remain pending. See the [source sheet and baseline gap list](agentready-setup-and-gaps.md). Public checks found title-only native refund/shipping policy endpoints; the actual return terms are in Section 21 of the Terms of Service. Root AI discovery files already exist but the observed content lacks Halfday-specific return/support/Amazon context.

Added two policy-backed answers to the development FAQ, bringing it from 17 to 19 visible questions: returns/exchanges and damaged/incorrect orders. Existing terms are unchanged, and both answers link to their source. Uploaded only the FAQ template through CLI. Browser verification confirms keyboard/mouse expansion, correct answer text, one H1 and development assets. Theme Check stays at 122 errors / 404 warnings; no JS added. Production and app configuration are unchanged.

| Item | Next step / dependency |
| --- | --- |
| 4-packs | Confirm the consumer 4-pack versus 24-pack logistics-case records, SKU/GTIN, approved imagery, channel and purchase links. Do not expose case SKUs as consumer packs. |
| Slim cans | Confirm 45 versus 40 calories, tea ingredients, caffeine, approved images and the sample-only/access restrictions before making products publicly discoverable. Fix display-title/content fields after those decisions. |
| CRO/content hierarchy | Finish format discovery, product comparisons and primary CTA placement using the approved catalog. Current public product CTAs and gallery behavior are preserved. |
| Apps | Review Signifyd scoping with its owner; settle Postscript/Klaviyo SMS ownership; decide whether accessiBe remains needed. Shared app settings affect production and are not isolated by this preview. No speculative uninstall. |
| Further speed work | The theme animation/polling pass is complete. LCP remains variable; isolate app costs in a supported staging setup, review font delivery and remaining route assets, and repeat production measurements after any approved release. |
| SEO/content | Homepage/FAQ headings and key link names are improved. Review remaining page titles/headings/alt text; confirm Subscribe page purpose; review nutrition/caffeine and old health claims. Choose retired Cranberry and overlapping blog destinations using content/Search Console evidence when available. |
| Store-data cleanup | After preview approval, decide whether to migrate theme-level article fixes into source content and add redirects. Noindex does not remove retained utility URLs from Shopify's sitemap. |
| Release QA | Owner walkthrough of authenticated staff/sample buying, desktop/mobile content review, reduced-motion setting check, and final production comparison/merchant-diff refresh. |

The signup/offer and lifecycle work belongs to Wave 2 of the latest three-wave plan. GA/Ads remain deferred; GTM remains excluded.
