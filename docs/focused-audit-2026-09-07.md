# Halfday: verified performance, app, Klaviyo and SEO findings

**September 7, 2026. Read-only follow-up audit.** This replaces the generic speed/email/SEO recommendations in the earlier roadmap with specific work supported by measurements, account settings and a full public sitemap crawl. No live theme, app, discount, flow, audience, DNS or publishing settings were changed. No email was sent or profile subscribed.

The priorities are: stop offscreen video downloads; resolve the signup offer and audience mismatch; correct the product information/schema; repair broken content links; and rebuild campaign audiences before resuming sending. A new theme, new sending domain, blanket app uninstall, or new SEO app is not the starting point.

## What was checked

- All **71 HTML URLs** in the public sitemaps: home, 15 products, 10 collections, 12 pages, a blog index and 32 articles. All returned HTTP 200. Additionally checked 14 old/malformed internal destinations, following redirects. Sitemap presence and HTTP 200 do not establish Google indexing or traffic.
- **15 local mobile Lighthouse runs:** three each on home, Lemon PDP, Shop All, home with video requests blocked, and home with Signifyd requests blocked. Lighthouse 13.4.1, fresh temporary Chrome profiles, simulated mobile throttling, sequential runs. One attempted combined blocking run did not block the intended resources and is excluded.
- Independent Google PageSpeed Insights mobile/desktop tests and homepage real-user data; Shopify's 30-day performance dashboard.
- Theme source responsible for video/Instagram rendering, images, styles, scripts, navigation, FAQ anchors and structured data; runtime third-party requests beyond the installed-app inventory.
- Klaviyo branded sending domain, deliverability report, campaign history, main and alternate popup targeting/display/success content, audience sizes and sunset criteria, draft browse-flow rules/message, and the final welcome email. Earlier verified flow/form inventory and welcome filters remain in the [account audit](klaviyo-audit-2026-09-07.md).
- Shopify discount search for the exact popup code `NEWERA15`; public SPF/DMARC and sending-domain DNS.

## 1. Performance: good field vitals, excessive background downloads

The homepage **currently passes real-user Core Web Vitals**. Do not describe it as failing LCP for actual visitors based on a synthetic score.

| Source / population | LCP | INP | CLS |
| --- | --- | --- | --- |
| PageSpeed homepage URL, mobile, latest 28-day field window | 1.4s | 187ms | 0 |
| PageSpeed homepage URL, desktop, latest 28-day field window | 1.2s | 109ms | 0.02 |
| Shopify dashboard, all-device aggregate, 30 days | 1.292s | 96ms | 0.01 |

The independent PageSpeed **mobile lab** test scored 38/100, with LCP 10.4s, TBT 1,200ms and 58,405 KiB transferred; desktop scored 55/100. These are single synthetic runs under different conditions from the field data. [Saved PageSpeed report](https://pagespeed.web.dev/analysis/https-drinkhalfday-com/n806elrtam?form_factor=mobile)

Local repeated mobile results also varied considerably:

| Route, three runs each | Median transferred data | Median simulated LCP (range) | Median TBT |
| --- | --- | --- | --- |
| Home | 40.3 MiB | 27.95s (3.91–29.21s) | 928ms |
| Lemon PDP | 35.1 MiB | 20.16s (14.22–24.86s) | 1,362ms |
| Shop All | 39.4 MiB | 3.73s (2.59–25.19s) | 1,105ms |

These wide lab ranges are not a precise estimate of a visitor's wait. The reliable finding across sources is the enormous media payload and material script work. Raw observed navigation timings and simulated metrics are both retained separately in the report. Improving the slow-device experience while preserving the good field results is the right objective.

### P1: defer testimonial and footer video loading

In a representative homepage run, **34.7 MB of 42.3 MB transferred was media**, with 381 requests overall. Videos also loaded on the PDP and collection route. One 1080p video request alone transferred 11.4 MB in the first run.

The source is concrete:

- `snippets/Index-object-testimonials-new.liquid:47` renders autoplaying, looping videos with master-sized posters.
- `snippets/Index-object-instagram-new.liquid:72` and `:109` do the same. The snippet renders the item list twice for its looping strip, including duplicate video elements.
- `sections/footer-group.json:15` includes the Instagram section globally, explaining why this is not just a homepage problem.

**Change:** render appropriately sized static posters first. Use the existing Dawn deferred-media approach or a small visibility/click enhancement to attach video sources only when needed. Avoid autoplaying multiple invisible slides and duplicate video copies. Pause media outside the visible area and respect reduced motion. Keep the visual content and brand treatment.

**Evidence of opportunity:** blocking Shopify video requests locally reduced median homepage transfer from **42.25 MB to 7.62 MB, about 82%**. This is a diagnostic upper bound for deferring those requests, not a deployed improvement. TBT did not improve consistently in the video-only comparison, so do not claim the video fix alone resolves JavaScript responsiveness.

**Verify:** before scrolling, offscreen video URLs should not download; posters and controls must still work; intended videos play on demand; repeat home/PDP/collection measurements. [Browser guidance on deferred video loading](https://web.dev/articles/lazy-loading-video)

### P2: fix oversized lower-page images and prioritize the PDP's first image

Lighthouse estimated about **2 MiB of image savings** on the homepage. A testimonial poster was 2160×2860 and about 419 KB before headers, despite a much smaller rendered size. The duplicated Instagram strip adds further image work.

**Change:** replace `image_size: 'master'` posters and blanket large image widths with sizes based on the actual card dimensions and device density. Supply accurate `sizes`; use Shopify's image transformations and lazy-load offscreen content.

The homepage mobile hero is already discoverable in the initial HTML, eager and `fetchpriority="high"`. The tested mobile run downloaded its mobile hero at about 167 KB. The source's `img.width` reference is undefined, but **the tests do not establish that both desktop and mobile heroes downloaded**. Correct the markup without claiming that unverified double-download saving.

The Lemon PDP's LCP image is eager/discoverable but lacks high fetch priority. Add priority to the initially visible product image only in `snippets/product-thumbnail.liquid`, through the gallery's first-media path. Keep other gallery images lower priority; preserve zoom and variant switching. Measure after the video change rather than adding broad preloads.

### P3: reduce small global theme costs after the large media fix

Move `find-us.css` out of `layout/theme.liquid:319` and into the locator route. Scope collection quick-add assets and public-route cart assets after verifying protected Shopify buying paths. Map consumers before separating jQuery/Swiper from `custom.js`. The current bundle transfers about 78 KB compressed in the first run, much less than its 287 KB source size; it is not the largest payload problem.

Review Typekit and Shopify font declarations together. Ten font requests transferred about 155 KB in a representative run. Preserve used Strippy/Museo faces; remove only verified unused declarations/weights. Do not claim the whole font payload can disappear.

## 2. App cleanup: decisions based on runtime cost

The following are **homepage medians across three baseline runs**. CPU numbers are measured main-thread work attributed by Lighthouse, not each vendor's contribution to simulated TBT. Third-party bytes do not include the much larger first-party Shopify-hosted videos.

| Service | Transfer / CPU | Recommendation |
| --- | --- | --- |
| Signifyd | ~213 KiB / 304ms; first run reached 1,786ms | Highest-priority app configuration review. Confirm why fraud profiling runs on public Amazon/retail discovery pages and whether vendor-supported scoping is possible. Keep coverage on actual Shopify order paths. Do not uninstall fraud protection as an audit shortcut. |
| Postscript | ~209 KiB / 45ms | Confirm the active SMS program and the handoff from Klaviyo's SMS signup step. If Postscript is still the sender, keep one intentional capture/sending arrangement. If unused, retire its injection after consent/data ownership is settled. Its SDK loads despite not appearing in the initial 22-app list. |
| accessiBe | ~230 KiB / 41ms | Hardcoded at `layout/theme.liquid:419`, with hidden trigger and background processing enabled. Review continued need with the owner; remove the injection if retired and fix actual accessibility defects in the theme. No replacement overlay is proposed. |
| Yotpo | ~206 KiB / 58ms | Still renders reviews on the tested PDP. Limit loading to real review surfaces where supported; preserve until Bazaarvoice import, onsite output and retailer requirements are verified. A new review vendor is not automatically faster. |
| Klaviyo | ~262 KiB / 61ms | Keep the functioning collection/flow infrastructure. Adjust the two-second popup and SMS overlap. There is no evidence here that removing Klaviyo is a sensible speed trade. |
| Facebook | ~175 KiB / 63ms | Retain pending ownership/measurement review; no ad or tracking settings changed. |
| Google tag loader | ~171 KiB / 31ms | A direct GA4 `gtag/js?id=G-8MPJFZBSD7` request exists. Lighthouse labels its domain “Google Tag Manager”; this is not proof that the user's empty GTM container is in use. Preserve until the later analytics phase. |
| Stockist | No homepage requests identified in these captures | Keep the locator and measure its route before recommending replacement. It is not an established homepage culprit. |
| Cin7, ShipStation and other operations/admin apps | No attribution as homepage blockers established | Retain needed operations tools. Installed-app count is not a measure of browser load or evidence that they should be removed. |

With Signifyd-only request blocking, median local TBT fell from **928ms to 747ms** and the median performance score rose from **36 to 63**. The unblocked runs were variable and collection periods differed, so treat this as prioritization evidence, not a guaranteed 181ms production saving. A feature-preserving vendor configuration needs its own comparison.

**Easy replacements worth implementing first:** deferred native video/posters, route-only locator CSS, semantic FAQ anchors/native scrolling, and simple native controls where a slider dependency is unnecessary. Keep Locksmith access checks. Old unloaded EasyLockdown backup files are housekeeping, not proven speed savings. No new performance or SEO app is needed for these changes.

## 3. Klaviyo: fix the offer, entry rules and restart audience

### Keep the existing sending setup

`send.drinkhalfday.com` is **Active**, Marketing, Dynamic in Klaviyo. DNS delegates it to Klaviyo nameservers; root DMARC exists as `v=DMARC1; p=none`. Do not add a new sending domain or change root SPF simply because the brand uses Klaviyo. The root SPF also references Google and MailerSend; establish those owners before any later cleanup. Delivered-message authentication and click-domain alignment still need a consented test message, which this read-only audit did not send. [Klaviyo domain documentation](https://help.klaviyo.com/hc/en-us/articles/115000357752)

For Aug 8–Sep 7, the welcome-flow summary reports **36.40% opens**, 4.78% clicks, one bounce, three unsubscribes and no complaints. These are the individual flow’s rates; the all-message inbox-provider report has a different population. Klaviyo flags the **1.10% unsubscribe rate** as Poor. Those are only three people, so fix expectations/targeting and monitor rather than declare a statistically established creative problem. Deliverability score is unavailable because volume is below its 1,000-email threshold, not because authentication failed.

### P1: reconcile the 15% offer across popup, footer and welcome

- Main live popup `XDLfXK` advertises 15% off. Its success step says **“Use NEWERA15 for 15% off.”**
- Exact Shopify discount search returned **no `NEWERA15` result**. That does not determine whether a similarly named Amazon promotion exists.
- All three live welcome emails' Save 15% links point to Amazon ASIN **B0B4F5NJB6**. UTM/maas parameters already exist; Amazon offer eligibility and account ownership remain unverified.

**Change:** settle the actual redemption mechanism first. If the offer is on Amazon, make the popup, success state and emails say where/how it works and link to the approved eligible destination. If it cannot be verified, replace the discount promise with an approved non-discount signup benefit until an offer is ready. Do not simply create a Shopify code for a journey that ends on Amazon. Offer a useful flavor/format choice rather than routing every discount CTA to Lemon by default unless that restriction is intentional.

### P1: correct footer routing without moving a historic list wholesale

The global footer form **TPsGns** submits to **HelloFresh Sample Campaign (TPaapC)**; welcome **XruESR** triggers from **Halfday Newsletter (XNd8tH)**. The newsletter has **14,969** members and HelloFresh **15,696**; these are memberships, not deduplicated consented recipient totals.

**Change:** route new general-footer email consent to Halfday Newsletter and retain a source property for the footer. Keep the dedicated HelloFresh campaign form separate. Inspect any bridging automation and test one approved signup through consent/list/eligibility. Do not bulk move the 15,696-member HelloFresh list or backfill welcome messages to fix new signups.

Use profile properties for audience logic, for example `signup_source=footer|popup|hellofresh|pto`, and an approved customer-type mapping for consumer/staff/sample/wholesale. Flow tags can organize the account but do not fix list membership, event triggers or consent.

### P2: change the main popup deliberately; do not delete a supposed duplicate

Main popup `XDLfXK` shows after **2 seconds**, on all devices and to **all audience members**, excluding four campaign URLs. Dismissal cooldown is five days; it stays hidden after submission. It has email and optional SMS steps. Storing UTM parameters on consent is currently unchecked; leave attribution implementation for the later authorized phase.

Last seven days: **19 submits / 1,347 views (1.41%)**. Desktop: **2/791 (0.25%)**; mobile: **17/556 (3.06%)**. Nine visitors engaged with all steps; this is not proof that the other ten email submissions were lost.

**Change:** target eligible unsubscribed visitors and start with a later, engagement-based display condition, such as 8–10 seconds or meaningful scroll, after offer correction. This timing is a test hypothesis, not a proven optimum. Review the desktop creative separately given the observed split. Verify the email signup succeeds independently of optional SMS, remove duplicated privacy/terms wording in the SMS copy, and settle the Postscript/Klaviyo handoff before expanding SMS.

The second live popup **WtiUL4** is **custom-trigger only** and had **zero views** in the same window. It is not proven to compete automatically. Its public testing page provides an obvious dependency to review before archiving it.

### P2: repair welcome eligibility and launch one appropriate browse reminder

Welcome filters currently require zero Shopify orders ever, no receipt of the old A-Game welcome, and Boolean **`rc_active_subscriber=false`**. Preserve intentional deduplication; establish whether the subscription property is maintained and how missing values are handled before retiring/replacing the legacy rule. Test missing/false/true values and staff/sample cases. Do not treat Shopify order history as Amazon purchase history.

The existing draft **[FE] Browse Abandonment (RX4C7p)** is already a one-email flow: **Viewed Product → wait 2h**, re-entry after **30 days**, Smart Sending **16h**, with zero Checkout Started and zero Placed Order since entry. There are **no product trigger filters**. The email preview text contains **“Don't shy away from of a little fiber.”** Several product links render blank in its generic preview, which explicitly warns that dynamic content may be incomplete.

**Change:** correct that typo, add explicit public-product/channel eligibility, exclude staff/sample/wholesale behavior, and render the email with a real eligible Viewed Product event before activating it. Verify dynamic product name/image/destination and a safe fallback. Keep it as a browse-interest reminder; its Shopify checkout/order suppression cannot detect a completed Amazon purchase. Do not promise it is “abandoned Amazon cart recovery.”

All three welcome discount links and the founders message were inspected. The founders message is live at day five and reports one click in 30 days; its body and CTA are heavily image-based. Retain useful brand art, but make the primary benefit, offer conditions and CTA available as real email text/buttons. Replace the footer's Twitter login-redirect URL with the approved public profile link. Do not call the generic preview's preference placeholder a broken live unsubscribe link without a delivered test.

### P2: rebuild the restart audience before another broad campaign

No campaigns appeared in the last-30-day view. The recent all-time history shows **Amazon Spring Sale (Reschedule), sent March 25, 2026**, with **133 clicks / 0.95%**, and an **April 16 Watermelon HH Launch draft**. Past campaign audiences include multiple now-deactivated engagement segments plus the full newsletter list. These are not a ready-to-use relaunch audience.

The existing **[FE] Eligible for Sunset Flow (YA5dwU)** contains **26,960** profiles. Its criteria are subscribed, created at least 160 days ago, received at least one email ever, and no opens/clicks/Shopify orders in 160 days. It **does not require recent opportunities to engage**. Klaviyo separately recommends 318 profiles for suppression; that suggestion is a different population and was not acted on.

**Change:** recreate current engaged/new-subscriber audiences with actual consent, source and staff/sample exclusions. Assess recent clicks and qualified onsite activity; don't rely only on privacy-inflated opens. Audit sunset criteria before suppressing anyone, especially given the sending gap. Start a controlled relaunch campaign for the approved new formats and retail/Amazon destinations to the eligible audience, review bounce/complaint/unsubscribe/click results, then expand deliberately. Do not activate Shopify purchase/replenishment flows for Amazon consumers without a corresponding event source.

## 4. SEO: repair discovery and factual consistency before adding more articles

### P1: fix product schema and visible product facts together

**14 of 15 sitemap product pages have an empty Product JSON-LD description.** Visible marketing copy comes from custom fields while `sections/main-product.liquid:1053` calls Shopify's default structured-data filter. Six variety/mix pages emit a **$35.99 OutOfStock Shopify Offer** despite the public Amazon-led journey. This is not fixed by hiding the badge.

The Strawberry slim-can page links to **Find In Store**, yet emits an **InStock $32.28 Shopify Offer**. Its visible content also conflicts: **45 calories** near the top versus **40** in the comparison, and **Green & Black Tea** versus an ingredients list naming brewed black tea.

**Change:** establish an approved per-format fact record and purchase channel, then use it consistently for visible content and schema. Populate descriptions from the same approved source, retain verified SKU/GTIN/brand data, and include only applicable, accurate offers/reviews. Do not copy 3PL stock into Amazon availability. Google's merchant-listing eligibility requires a page where the shopper can purchase, not just an outbound link to a seller; select appropriate product markup for each channel instead of forcing merchant eligibility. [Google merchant-listing requirements](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing)

### P1: remove non-customer pages from search discovery

These URLs are in the sitemap, return 200 and have no robots noindex in the captured HTML/headers:

- `/pages/popup-testing` with two popup test controls.
- `/collections/staff-variety-packs` and `/collections/zb252lh3pgnv3b` (Staff All Flavors), which render empty/thin public collection shells.
- `/collections/menu`, `/collections/menu-duplicate` (title **Menu - USE THIS ONE**), `/collections/flavours-new-2-0`, and `/collections/frontpage`.

**Change:** hide the test page from search or unpublish it if retired. Check collection dependencies in menus, discounts and staff workflows before hiding or consolidating utility collections. Use intentional noindex rules for retained utility collections; do not assume Shopify's `seo.hidden` support for pages/products also applies to collections. Remove retired resources from public publication/sitemaps where appropriate. A noindex is not an access control; preserve Locksmith. [Shopify search-visibility options](https://help.shopify.com/en/manual/promoting-marketing/seo/hide-a-page-from-search-engines)

### P1: repair the actual broken content links

The additional link check found **eight distinct 404 destinations**:

| Destination | Where found | Concrete fix |
| --- | --- | --- |
| `/pages/shop` | 12 blog articles | Replace article CTAs with `/collections/shop-all`; add an appropriate legacy redirect |
| `/products/cranberry-black-tea` | 4 articles | Update to the approved relevant current product/collection, or explain retirement; do not silently relabel a different flavor as Cranberry |
| `/blogs/news/drinkhalfday.com` and `/blogs/news/drinkhalfday.com/pages/shop` | Malformed relative links in 2 and 1 articles | Correct the missing URL scheme/path in the source content |
| `/pages/faq_general`, `/pages/faq_products`, `/pages/faq_orders`, `/pages/faq_company` | FAQ category links | Change `href="faq_general"` etc. to actual `#faq_general` anchors and update JS selectors. Current desktop JS intercepts clicks, masking the malformed crawler/no-JS destinations |

Old Lemon, Green, Peach and variety-sampler product links and `/collections/new-2-0` redirect successfully. Update their source links to the final URL during cleanup, but don't report them as broken pages. Evidence includes source-page lists in the [link-check report](../reports/seo-internal-link-check-2026-09-07.json).

### P2: make the existing useful pages answer the right questions

**14 sitemap pages lack a nonempty meta description:** all ten collections, blog index, Contact, Subscribe and Watermelon Half & Half. Focus on retained customer-facing pages; do not write optimized descriptions for utility pages being hidden. Existing flavor descriptions are already populated and should not be presented as a from-scratch task.

Use descriptive search titles such as **“Shop Halfday Prebiotic Iced Tea | Flavors & Packs”** for Shop All and **“Halfday Iced Tea Variety Packs”** for the variety collection, with approved pack/channel descriptions. Remove repeated brand suffixes where the theme already appends the store name. Replace generic collection headings with meaningful category names; keep brand slogans as supporting text.

The FAQ still says people can purchase directly from the website and gives general 3–5-day shipping expectations. Its caffeine answer references a question titled **“Is there caffeine in Halfday”** that is absent from the captured FAQ content, uses “bottle,” and contains spelling mistakes.

**Change:** add clear answers for current purchase channels, retailer-specific shipping/support, exact caffeine by flavor/format, consumer pack size versus shipping case, approved sugar/calorie/fiber values and where to find the slim cans. Link the locator and relevant products directly in the answers. Keep the answers in crawlable text and draw repeated facts from the same approved source. This is the concrete AEO work; no special AI script or promised search placement is warranted.

Fix `sections/header.liquid:508` Organization markup to use a stable homepage identity/`@id`, valid nonempty social links and consistent URL across pages. Add meaningful linked-image alternatives and descriptive link labels where the content needs them; leave truly decorative images empty. Native theme corrections cover this without a schema app.

### P2: consolidate and refresh the old blog before commissioning more

There are **32 public articles**, all with a 2022 `dateModified` in their Article schema. The two **“Kombucha 101: What Does Kombucha Taste Like?”** URLs both self-canonicalize and have substantially overlapping text, but are not byte-identical. Other overlaps include two kombucha-timing and two green-tea-shot articles.

**Change:** choose the strongest retained URL after Search Console/backlink data is available, combine useful unique content, redirect the redundant URL and update internal links. Don't select a winner solely because one slug ends in `-1` or delete posts based on age alone.

Sampled articles still refer to **Halfday Tea Tonics**, **Peach Green Tea**, bottles and old product destinations. The ulcerative-colitis and tooth-extraction posts also make condition-specific dietary/product recommendations. Have the appropriate content reviewer check those claims and decide whether they belong on the brand site; this audit does not validate the medical advice. Prioritize current iced-tea ingredients, format facts and purchase guidance over expanding unrelated health/shot-recipe topics. Existing traffic and query demand were not available, so no ranking-loss or keyword-volume claim is made.

## Recommended implementation order

1. **Offer and signup repair:** resolve NEWERA15/Amazon eligibility, align popup/footer/welcome wording, correct new-footer routing, verify welcome entry and exclusions.
2. **Media cleanup:** defer both testimonial and global Instagram videos, size posters/images, then rerun matched measurements. Review Signifyd scoping and SMS ownership alongside this work.
3. **Product facts and schema:** reconcile the slim-can contradictions and channel-specific offers; fill the 14 blank structured descriptions from approved content.
4. **Search cleanup:** fix the eight broken destinations, hide test/utility discovery appropriately, improve retained collection titles/descriptions and rewrite the channel/caffeine FAQ answers.
5. **Lifecycle restart:** validate one browse reminder, rebuild current engagement/consent audiences, review sunset logic, then prepare the new-format campaign. Do not relaunch all old order flows.
6. **Follow-through:** selective app retirement after dependencies are clear; blog consolidation based on performance data and editorial review; Bazaarvoice work remains dependent on vendor/catalog readiness.

The earlier hourly waves remain preliminary implementation allowances. In particular, the combined email/SEO allowance does not include rewriting 32 articles, a custom integration, or an unlimited email program. The findings above define the first changes; vendor decisions and broader editorial work should be estimated separately once selected.

## Evidence and remaining limits

- [Performance data: 15 sanitized runs](../reports/performance-audit-2026-09-07.json); raw Lighthouse JSON stays in `/private/tmp/halfday-lighthouse-20260907/` and is not committed because it contains transient browser/request details. Temporary tooling did not modify storefront dependencies.
- [Full public SEO crawl](../reports/seo-crawl-2026-09-07.json), [legacy/internal link checks](../reports/seo-internal-link-check-2026-09-07.json), [public mail DNS](../reports/mail-dns-audit-2026-09-07.json), [Klaviyo and field-data observations](../reports/focused-account-observations-2026-09-07.json).
- Reproduce the crawl with `python3 scripts/audit-seo.py`; summarize saved Lighthouse runs with `python3 scripts/summarize-performance.py <raw-directory>`. For a Lighthouse baseline, use the documented version, `--only-categories=performance,seo,accessibility`, `--chrome-flags='--headless=new --no-first-run --no-default-browser-check'`, default mobile simulation, and three sequential fresh-profile runs per route. Diagnostic groups use a single `--blocked-url-patterns='*cdn/shop/videos/*'` or `'*signifyd.com/*'` argument.
- No Search Console inspection, delivered-email authentication test, live signup, Amazon discount redemption, complete billing/license audit, or controlled integration transaction was performed. Dynamic browse links require event-specific rendering. GA and Google Ads implementation remain deferred; GTM remains excluded.
