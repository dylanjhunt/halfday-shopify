# Wave 1 progress

**Status: the combined Wave 1 tablet, performance, accessibility and semantic work is live. Catalog/app and editorial dependencies remain open.**

- Live: theme **142757101768**, `halfday-shopify/main`, release **`bb0169f`**; tag **`baseline/live-wave-1-2026-09-09`**.
- Current branch: **`djh/wave-1-agentready-verification`**. Development theme: **142755430600**. Future theme releases need separate authorization.
- [September 9 release and verification](wave-1-release-2026-09-09.md): all 455 live files match main; 15-route checks pass before/after deployment; live desktop/tablet/mobile samples inspected. Overnight Shopify/Locksmith changes preserved.
- Agentready UI and sampled catalog safeguards improved. Apply still returns `unsupported_field`; Dylan is working on it. Both output switches and embeds restored off; curated discovery index regenerated without catalog records. [Current app findings](agentready-product-feedback.md).
- Historical checkpoints below retain their original scope and are superseded by this current status. Amazon buying routes and protected legacy code are preserved.

## September 9: approved Peach typo correction

Dylan explicitly approved the live product metafield spelling correction. Saved Product Title on Peach Tea (Slim Can), Shopify product `8335577710792`, from `Peach Tea (Silm Can)` to `Peach Tea (Slim Can)`. A fresh admin reload confirmed the corrected value; Save was disabled, indicating no pending edits. No other product fields, theme code, publication or access settings were changed. This closes the previously blocked typo item below.

## September 9: decisions, contrast and Agentready Apply follow-up

Dylan confirmed keeping accessiBe and the health articles, approved dark-green contrast fixes, and will confirm Signifyd, Postscript, expired campaigns and Cranberry while requesting Search Console. Existing products are preserved; [client fact list](product-facts-for-leslie.md) gives exact locations for contradictory and missing details.

Implemented CSS-only contrast fixes on the existing development branch: green/yellow panel headings (8.89:1), white/green primary and mobile-card buttons plus footer Klaviyo button (11.19:1), and green underlined footer link hover. Desktop 1280px and mobile 390px samples passed; no overflow, no form submissions, Amazon attribution intact. Shopify CLI readback matches CSS and config. [15-route verification](../reports/wave-1-contrast-regression.json).

Agentready Apply now shows a persistent 34/34 receipt. Brand-only development output has the correct current description and policies, with no catalog approvals, no JSON-LD, no live embed activation and no protected catalog output in sampled checks. The development embed remains enabled for this verified configuration. Dylan merged PR #1 at `2893a6f`; this follow-up is isolated on `djh/wave-1-contrast-agentready`. [Output evidence](../reports/agentready-post-apply-output-2026-09-09.json). Its contact form still has a presentation/save inconsistency, while output support email is correct.

No product data changed. The proposed Peach metafield spelling correction was rejected by automatic approval review as a live product edit outside the development workflow; the unsaved edit was discarded. No main push was performed in this follow-up.

## Latest autonomous completion pass, September 9

Additional development fixes now cover the homepage benefits accordion, responsive benefits artwork/icons, optional video deferral and restored keyboard focus indicators. Four remote files match local; 15-route checks pass; Theme Check reports 122 inherited errors / 385 warnings with no added findings. Main remains `bb0169f`.

Seven native legacy redirects were imported after browser access recovered. Shopify confirmed seven additions; anonymous requests verify all seven now return **301** to the intended working destinations. [After verification](../reports/wave-1-legacy-redirects-after.json). Rechecked app inventory and the Shopify 30-day field baseline. [Completion details and specific questions](wave-1-completion-questions.md) track every remaining dependency. Agentready Apply is still being worked on; it was not retried this pass.

## Implemented and released

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

Updated September 8, 2026. Core trial is active. Concierge Apply failed twice, so brand, policy summaries, page types and discovery curation were saved through individual settings. See [current setup and remaining work](agentready-setup-and-gaps.md) and the [Agentready product/UX report](agentready-product-feedback.md).

**Dylan is implementing the reported app fixes.** Full activation remains pending verification of those fixes. Testing the embed through Shopify CLI on development exposed staff collection data in page HTML. The embed was disabled again; both shared app output switches are off. A direct staff-product markdown URL remains publicly readable despite all products being explicitly excluded. This requires an app endpoint visibility fix. Production theme code and existing store access rules were not changed. Shared Agentready settings and its curated app-served discovery index were updated.

The curated native AI guide is implemented on development at `/agents.md`, `/llms.txt` and `/llms-full.txt`, using only public tea links, verified support/terms and retailer buying guidance. Earlier development FAQ additions still provide 19 visible questions including returns and damaged/incorrect orders. No new shopper JavaScript was added. The final 15-route regression check passes and Theme Check remains 122 errors / 404 warnings. [Verification evidence](../reports/agentready-implementation-verification.json).

| Item | Next step / dependency |
| --- | --- |
| 4-packs | Confirm the consumer 4-pack versus 24-pack logistics-case records, SKU/GTIN, approved imagery, channel and purchase links. Do not expose case SKUs as consumer packs. |
| Slim cans | Confirm 45 versus 40 calories, tea ingredients, caffeine, approved images and the sample-only/access restrictions before making products publicly discoverable. Fix display-title/content fields after those decisions. |
| CRO/content hierarchy | Finish format discovery, product comparisons and primary CTA placement using the approved catalog. Current public product CTAs and gallery behavior are preserved. |
| Apps | Review Signifyd scoping with its owner; settle Postscript/Klaviyo SMS ownership; decide whether accessiBe remains needed. Shared app settings affect production and are not isolated by this preview. No speculative uninstall. |
| Further speed work | Animation/polling and brand-font preload cleanup are complete. The story/Why Halfday can strips now use sized images with appropriate priorities. LCP remains variable; isolate app costs in a supported staging setup, Contact/content split-image cleanup is complete; repeat production measurements after any approved release. |
| SEO/content | Homepage/FAQ headings and key link names are improved. Review remaining page titles/headings/alt text; confirm Subscribe page purpose; review nutrition/caffeine and old health claims. Choose retired Cranberry and overlapping blog destinations using content/Search Console evidence when available. |
| Store-data cleanup | After preview approval, decide whether to migrate theme-level article fixes into source content and add redirects. Noindex does not remove retained utility URLs from Shopify's sitemap. |
| Release QA | Owner walkthrough of authenticated staff/sample buying, desktop/mobile content review, reduced-motion setting check, and final production comparison/merchant-diff refresh. |

The signup/offer and lifecycle work belongs to Wave 2 of the latest three-wave plan. GA/Ads remain deferred; GTM remains excluded.


## September 8: continued roadmap work while Agentready fixes are underway

Development theme **142755430600**, branch `dev/wave-1`. Refreshed the live theme through Shopify CLI and compared all native theme files to `main`: no merchant drift. The development files being edited also matched the local checkout. No shared app or store data changed in this pass.

| Completed | What changed |
| --- | --- |
| Consistent search and social descriptions | Extracted one small Liquid fallback snippet used by search, Open Graph and Twitter metadata. Collection/Contact descriptions now agree across channels; existing merchant descriptions still take precedence. Locksmith visibility checks remain around output. |
| Retailer pricing metadata | Removed optional Shopify price/currency Open Graph tags from the current retailer-directed product pages. Their Shopify/3PL prices do not establish Amazon or retailer offers. Cart code, product events and actual Shopify inventory checks are untouched. |
| Clear page headings | Contact, Our Story and Why Halfday now have one H1 each. Section settings allow H1/H2 and default to H2 elsewhere. Scoped CSS preserves existing typography, size, alignment and color. |
| Smaller can images | Story/Why Halfday marquee images use a maximum 864px source with responsive candidates for their 184px mobile / 288px desktop slots. Removed ten high-priority requests per strip. The leading Why Halfday set stays eager; loop copies and the below-fold Story strip are lazy. Existing links, animation library and loop structure remain. |
| Accessible flavor and form links | Populated editable flavor-specific accessible names on all ten configured product links across the two pages. Contact's existing translated labels now use the theme's visually-hidden utility instead of display:none. Form names, endpoints, consent behavior and submission logic are unchanged. |
| Correct font preload | Replaced two identical unused Assistant font preloads with one Strippy WOFF2 preload matching the brand font-face source. Museo/Adobe fonts, font weights and font-display behavior are retained. |

### Verification

- [12-route metadata/image verification](../reports/wave-1-roadmap-preview.json): retained merchant descriptions, matching collection/Contact search and social descriptions, no retailer-page Shopify price metadata, exactly one Strippy font preload and no rendered Liquid errors. Both can strips output the expected responsive sizes and loading priorities.
- [15-route regression comparison](../reports/wave-1-regression-markup.json): Amazon destinations and attribution parameters, Klaviyo embed IDs, integration markers and external loaders are preserved. Protected/cart scripts and bundled libraries remain unchanged. This verifies markup preservation, not complete analytics attribution or Amazon purchase events.
- Browser review at **390px and 1440px**: all three pages have one H1 and no horizontal overflow. Original heading metrics also match at the original 842px viewport after the tag changes. Desktop Contact and mobile Why Halfday screenshots retain the current design. Keyboard Enter on the Sweet Tea can link reaches `/products/sweet-tea`.
- [Theme Check comparison](../reports/wave-1-roadmap-theme-check.json): **122 inherited errors / 402 warnings**, zero added offenses and two undefined-image-variable warnings removed. This is not a clean Theme Check pass.
- Shopify did not retain Contact's new heading setting on the first combined section/template upload. Reapplying the template after the schema upload resolved it; browser verification confirms H1. Future additions should upload section schema before JSON values and check the rendered result.
- No JavaScript was added or changed. No new LCP, conversion or full-page transfer improvement is claimed from this pass; the verified changes are image sizing/loading priority and the removal of unused font preloads. Existing app costs remain the largest unresolved speed item.

### Remaining sequence

1. Recheck Agentready endpoint visibility, exclusions, rendered data and onboarding only after Dylan's fixes are ready. Keep the current app embed/output safeguards until verification passes.
2. Complete approved catalog merchandising once 4-pack/case, slim-can nutrition, channel and access decisions are supplied. This gates format comparisons and additional public product discovery.
3. Secondary-page split images and social-preview dimensions are now complete in the quick-wins checkpoint below. Remaining accessibility/content reviews should prioritize verified defects and preserve contact and purchase flows.
4. Resolve app ownership/scoping decisions, beginning with measured Signifyd cost, then SMS overlap and the review migration dependencies. No speculative uninstall.
5. Complete authenticated staff/sample ordering and release QA, refresh the merchant diff, then request approval for the exact production release. Wave 2 lifecycle activation is separate from this theme pass.


## September 8: LCP and CLS follow-up

[Detailed findings, measurements and next steps](lcp-cls-follow-up-2026-09-08.md).

- Fixed a **36px product-header jump** by resolving the logo's actual image aspect ratio. Lemon PDP lab CLS fell from a 0.041498 baseline median to 0.000208 in the final confirmation; three earlier after-change samples were also below 0.0006.
- Corrected custom product-card dimensions/srcsets and supplied the featured carousel's real image width. Preserved artwork, crop, hover media, Amazon links and gallery navigation.
- Added the mobile homepage source dimensions, changed the FAQ to one responsive picture with first-section priority, and made 22 Contact retailer logos lazy/low priority.
- Final homepage mobile LCP: **4.04s, 4.22s, 29.78s**. LCP remains unstable; no reliable improvement claimed. An unproven extra-font-hint experiment was reverted; all samples are retained.
- Theme Check: **122 inherited errors / 397 warnings**, no added findings. Nine-route image checks, 15-route integration/link regression checks and relevant desktop/mobile interactions pass.
- No new JavaScript, production theme changes or shared app/data edits. Signifyd scoping, rendering dependencies and late review-widget space remain the next performance items, alongside the existing catalog and authenticated-release dependencies.


## September 8: three Wave 1 quick wins completed

Development theme **142755430600**, branch `dev/wave-1`. Fresh live/development downloads matched their committed baselines for all five changed files. All five final remote files were read back and match local code. No production or shared store/app data changes.

| Completed | Result |
| --- | --- |
| Secondary-page image cleanup | Contact and Why Halfday use one responsive picture per content image instead of hidden desktop/mobile duplicates. Offscreen images are lazy; first-section artwork remains eager. Contact's desktop-only photo selects an inline empty source on mobile. Source candidates respect original resolution, and mobile sizing accounts for the existing cover crop. The original image settings, artwork and visible frame dimensions are retained. |
| Card and quick-order stylesheet cleanup | Featured product loops include card styles once per section, after the first product allowed by Locksmith. Native rating styles load only when enabled; volume-pricing/quick-order styles load only in bulk mode. Price, native purchase-control and app review styles remain available. Homepage stylesheet tags fall **71 to 32**, Why Halfday **106 to 32**, and Shop All/Variety **36 to 32**. Three unused CSS files are absent from those routes, totaling 14,044 uncompressed source bytes. Duplicate URLs were already browser-cacheable, so fewer tags do not equal the same number of saved requests. |
| Social-preview image metadata | Select the existing custom product image or page fallback once, then use its actual dimensions and HTTPS for both image URLs. Custom product images report **750 × 902**, rather than the unrelated product-page image dimensions. Existing selected artwork remains unchanged. All image fields retain the Locksmith resource visibility check; existing alt text is included when present. |

Verification: [quick-wins evidence](../reports/wave-1-quick-wins-verification.json). Contact/Why Halfday retain their mobile and desktop image-frame dimensions at **390px/1440px**; screenshots retain the crop/design and lazy artwork loads in view. Homepage card text, color and dimensions match before/after, including existing Yotpo ratings; carousel Next advances to **2/8**. Contact keyboard focus moves from Name to Email and the form endpoint is unchanged. No forms were submitted.

All **10 social-image checks** match the actual PNG dimensions over HTTPS. The [15-route regression comparison](../reports/wave-1-regression-markup.json) preserves Amazon URLs including attribution parameters, Klaviyo embeds, integration markers and external loaders. Native cart/product scripts, bundled libraries and Locksmith code remain unchanged. This is markup/interaction verification, not proof of downstream analytics receipt or authenticated ordering.

No JavaScript added or changed. This pass does not claim a measured LCP/CLS improvement. App scoping, approved catalog facts, Agentready fixes and authenticated release QA remain the major dependencies.

[Final Theme Check comparison](../reports/wave-1-quick-wins-theme-check.json): **122 inherited errors / 391 warnings**, no new offenses and six inherited warnings removed. Git whitespace checks pass.


## September 8: merge into main

Dylan authorized merging the implemented Wave 1 work into `main`. The working tree was clean and `main` was an ancestor of `dev/wave-1`, so no conflict resolution or theme-code changes were needed. A merge commit preserves the wave boundary. The original live theme remains at `baseline/live-2026-09-07`; the regression checker now uses that immutable reference instead of the moving `main` branch.

The merged `main`, completed `dev/wave-1` branch and original baseline tag are being pushed to Dylan’s supplied repository, [dylanjhunt/halfday-shopify](https://github.com/dylanjhunt/halfday-shopify). No Shopify files were uploaded and no theme was published during this merge/push task. Dylan will connect Shopify, then request the final audit before publishing. Existing catalog, app and authenticated-ordering dependencies remain open. Subsequent work starts on a descriptive feature/fix branch from `main` and is reviewed in an unpublished theme before merging.


## September 8: Git-connected preview audited

Dylan connected `main` to unpublished theme **142757101768**, `halfday-shopify/main`. [Final connected-theme audit](wave-1-connected-audit-2026-09-08.md) confirms all 455 theme files match release commit `2c8ff4f`, with no live merchant drift. Fifteen live/preview regression routes and 22 feature endpoints pass; representative desktop/mobile interactions are verified. Both fresh preview browser audits have zero console errors and very low CLS. LCP/TBT remain inconsistent; authenticated staff/sample ordering is still unverified. No theme code, app settings or publishing state changed during this audit.
# September 8: legacy product template assignments

With Dylan's approval, inspected all 66 products and switched 39 obsolete `shogun.custom` assignments to Default product. The remaining 27 already used the default. Saved in Shopify admin, verified product-record samples, and checked four affected tea routes on live and the Git-connected preview. All returned HTTP 200 without Liquid errors; Amazon links and attribution parameters matched. No theme was published. Details: `docs/shogun-template-cleanup-2026-09-08.md`.


## September 8: published baseline and continued Wave 1 development

Dylan published `halfday-shopify/main`; Shopify CLI confirms its live role and a fresh pull matches all 455 files at `2c8ff4f`. Created the immutable published baseline tag and moved follow-through onto `feature/wave-1-follow-through`, with no upstream to main. Updated shared Claude guidance, README, the roadmap and regression comparisons for the live-main workflow.

The [follow-through report](wave-1-follow-through-2026-09-08.md) records the additional gallery video deferral, responsive collection banner and single-H1 cleanup, browser checks, exact remote file verification and performance limits. All new theme edits are in development theme `142755430600`. Main remains unchanged. Outstanding catalog, app, Agentready and editorial dependencies remain visible in the roadmap.


## September 8: review layout and Agentready recovery

Completed a further three-file theme pass on `feature/wave-1-follow-through`: reserved the product rating slot with an editable Reviews fallback, separated Dawn/Yotpo star styles and conditional native-rating CSS, and made the gallery skip-link target unique. No JavaScript changed. Rated-product title geometry is retained at 390px/1440px; the zero-review fallback reaches the review section by keyboard.

Two fresh mobile preview runs recorded CLS **0.000153 / 0.001416** and LCP **4.86s / 5.26s**. No reliable LCP gain is claimed. Fifteen regression routes preserve links/loaders/settings, Theme Check has zero added offenses (122 inherited errors / 391 warnings), and final remote files match local code.

Agentready output-off endpoint blocking now passes the staff and public-product checks. A reviewed 34-proposal setup Apply still failed with `unsupported_field`; recovery returned to the welcome screen. Embed and output switches remain off. The app report includes the error, recovery behavior, conflicting plan labels and ineffective embedded CTA. [Details and evidence](wave-1-review-layout-2026-09-08.md).


## September 8: combined tablet and LCP work ready for review

Continued on **`djh/wave-1-responsive-follow-up`** and Shopify CLI development theme **142755430600**. [Combined completion and remaining-dependency report](wave-1-lcp-completion-2026-09-08.md).

- Deferred collection promotional video using the existing component. Initial Shop All media transfer is now zero in three lab runs; total transfer median fell **19.75 → 6.07 MB**, with LCP median **4.18 → 3.53s**.
- Sized contained product images and card hover images correctly. The sampled leading Lemon image fell from **155.5 → 65 KB**. Lemon LCP samples are **3.83 / 4.15 / 10.44s**, so consistent product LCP improvement is not established. Homepage median is effectively unchanged. Both Adobe-font experiments were reverted; all samples remain in the evidence.
- Removed unused drawer card CSS for the current configuration, deferred quantity styles, repaired gallery/list semantics, improved announcement contrast, corrected collection card heading levels and removed a verified empty article H1. The tablet flavor-label refinement remains intact.
- Fifteen live/preview routes preserve Amazon attribution URLs, Klaviyo embeds, external loaders, forms, protected code and settings. All 71 sitemap URLs pass the technical checks after three rate-limited requests passed a sequential retry. Relevant desktop/mobile geometry and keyboard/media interactions pass. No purchases or subscriptions were submitted.
- Theme Check: **122 inherited errors / 388 warnings**, no added offenses. Motion lifecycle, JavaScript syntax and whitespace checks pass. Fresh CLI downloads match all **455 development files** to local and all **455 live files** to main `a99ed7f`.

This is development work prepared for a combined merge, not a production deployment. Catalog facts, campaign/editorial decisions, app ownership/scoping and Agentready fixes remain the Wave 1 dependencies. Broader brand-contrast choices and app-owned accessibility findings are documented. Klaviyo activation remains Wave 2; GA/Ads deferred and GTM excluded.

## September 9: combined release and app recheck

Published `bb0169f` with authorization, preserving Shopify's overnight `b17447a` changes. Recorded release baseline, post-release route evidence and Agentready controlled-test/restoration evidence. See [release record](wave-1-release-2026-09-09.md). No further theme changes or app activation are pending locally. Remaining dependencies are approved catalog facts/assets, app ownership/scoping, Agentready final fixes/output validation, and editorial decisions. Wave 2 remains Klaviyo signup/offer and lifecycle relaunch.
