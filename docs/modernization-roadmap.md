# Halfday modernization roadmap

**Internal delivery plan · September 7, 2026 · Planning estimates, pending implementation kickoff**

Modernize Halfday's existing Shopify store so it is easier to shop, faster to load, simpler to maintain, and reliable across email, retail, and fulfillment. Keep the brand's personality and useful existing work. Use native Shopify sections, editable content, and minimal JavaScript as the default.

This is the single delivery roadmap. The [focused performance, app, Klaviyo and SEO audit](focused-audit-2026-09-07.md) supplies the current findings and supersedes the earlier generic scope. The [store/theme audit](initial-audit-2026-09-07.md) and [initial Klaviyo inventory](klaviyo-audit-2026-09-07.md) remain supporting snapshots. Setup is complete: Shopify CLI, downloaded live-theme baseline, local Git, and Claude project guidance. Implementation has not started, and no live settings or theme code have been changed.

**Evidence update:** the homepage passes field Core Web Vitals, but offscreen video accounts for most captured transfer. The sending domain is already active. The concrete email work is offer/list/eligibility repair and a controlled restart audience. SEO work starts with eight broken destinations, blank structured descriptions on 14 products, conflicting slim-can facts and public test/utility URLs. See the focused audit for measurements, source files, exact account IDs and remaining verification limits.

## Schedule at a glance

| Wave | Simple outcome | Estimated hands-on time |
| --- | --- | --- |
| 1. Fix the essentials | Correct misleading stock messages, signup routing, and obvious journey problems | 2–4 hours |
| 2. Make the site faster | Improve loading and LCP; remove or replace measured app/theme overhead | 6–10 hours |
| 3. Improve the shopping experience | Launch the right new products and improve mobile browsing and conversion paths | 6–10 hours |
| 4. Strengthen email and search | Refresh core Klaviyo journeys and improve SEO/AEO foundations | 8–12 hours |
| 5. Connect and finish | Validate fulfillment/Faire, configure the review replacement, and finish QA | 6–10 hours, conditional on vendor readiness |

**Working estimate: 28–46 hands-on hours, roughly 4–6 eight-hour workdays.** Aim to deliver the ready work over **1–2 calendar weeks**, assuming access, approved assets/copy, and prompt decisions. This uses the completed audit and existing theme, product records, and email assets. It includes focused implementation and relevant QA; it does not reserve whole days for routine fixes or count client/vendor waiting as development time. The first four waves account for 22–36 hours and can progress while operations and review vendors respond.

Wave 5 is the least certain: its allowance covers checking existing connections, straightforward configuration, and a standard review-widget/import setup when the vendors are ready. Bazaarvoice onboarding, retailer syndication, and unresolved Cin7/3PL issues have no verified completion date yet. Keep those milestones open separately if they outlast the site work. Identify a concrete fault before estimating integration repair; do not promise that any unknown repair fits inside the allowance.

This estimate covers focused modernization of the existing theme and integrations. A full rebrand/replatform, custom integration middleware, new photography or extensive copywriting, bulk legacy-page rebuilding, and major data repairs need separate estimates if selected. The 32-article editorial review is not a promise to rewrite the entire blog inside Wave 4. Keep those discoveries in this roadmap with an owner and next action. Use the completed performance baseline and remaining integration checks to refine effort.

### Internal effort allocation

| Wave | Included effort |
| --- | --- |
| 1 | Stock/CTA/schema corrections on known affected templates: 1–2h; footer routing and eligibility test: 0.5–1h; links, spot QA, and dependency checklist: 0.5–1h |
| 2 | Implement deferred testimonial/footer videos and sized posters: 3–5h; targeted asset/app configuration work: 1–2h; matched before/after measurements and regression checks: 2–3h |
| 3 | Existing product records and approved assets: 2–3h; focused mobile/navigation/PDP improvements: 3–5h; legacy-page triage and content QA: 1–2h |
| 4 | Welcome/browse validation and consented restart audience: 4–6h; priority metadata, links, utility-page discovery and FAQ fixes: 3–4h; final checks: 1–2h. Product/schema work begins in Waves 1 and 3. |
| 5 | Existing integration/routing checks and routine corrections: 2–3h; standard Bazaarvoice setup and import checks: 3–5h; final site QA and handover: 1–2h |

These are estimates for the concrete first pass, not fixed-price commitments or a cap that makes unfinished work complete. If a task needs a deeper rebuild, record the finding and a specific additional estimate before expanding implementation.

**Out of scope for now:** GA setup, Google Ads, and full attribution implementation await Dylan's confirmation. GTM was confirmed empty/unused and is excluded. Their absence does not block storefront improvements; conversion-lift claims and paid-media launch readiness remain limited until measurement is available.

## Wave 1 — Fix the essentials

**Lead:** Dylan/theme development, with ecommerce, lifecycle, and operations owners. **Estimate:** 2–4 hours.

- Use the completed audits and performance baseline to fix known issues directly. Capture affected states before editing.
- Confirm the intended purchase channel for the affected products and correct the variety-pack sold-out messaging and related schema. Do not invent Amazon availability or weaken inventory checks on actual Shopify purchases. Complete catalog-wide channel mapping with the new formats in Wave 3.
- Correct footer form TPsGns routing from HelloFresh Sample Campaign to Halfday Newsletter for new general signups after checking any bridge and consent. Reconcile popup code NEWERA15 with the Amazon Save 15% destination: exact Shopify discount search returned no result, and Amazon eligibility is unverified. Test form → list → welcome eligibility with an approved test profile. Do not migrate the historic HelloFresh list wholesale.
- Fix verified stale preview links and confusing destinations; check navigation, key CTAs, and protected product visibility.
- Prepare one dependency checklist for product assets/mapping, Cin7 access, 3PL contacts, and Bazaarvoice onboarding. Assign owners so they can begin providing inputs while site work proceeds; detailed app, catalog, and routing work sits in its respective wave.

**Done when:** the priority stock/signup problems have been tested, affected public and restricted purchase paths behave correctly, key links are corrected, and each dependency has an owner. Theme changes are reviewed in a development preview before an authorized release.

## Wave 2 — Make the site faster

**Lead:** theme development, with app owners. **Estimate:** 6–10 hours.

- Defer video sources in `Index-object-testimonials-new` and the global footer's `Index-object-instagram-new` snippets. Start with sized posters, load playable video only when needed, and avoid downloading duplicate offscreen video copies. Video request blocking reduced median local homepage transfer from 42.25 MB to 7.62 MB. Use that as opportunity evidence, not a shipped saving or a guaranteed LCP improvement.
- Replace master-sized posters with responsive card sizes; address the approximately 2 MiB homepage image-saving estimate. The mobile hero is already eager and high priority. Add high priority only to the initially visible PDP image, then verify variant switching and zoom. Review the ten observed font requests without removing used brand faces.
- Use the runtime app evidence below. Prioritize vendor-supported Signifyd scoping, Postscript/Klaviyo SMS ownership and the hardcoded accessiBe injection. Keep Yotpo until migration is verified. Extend measurements to the locator/slim-can route when touching those features; the completed home/PDP/Shop All repeat runs provide the baseline.
- Move global `find-us.css` to the locator route. Map actual jQuery/Swiper consumers before replacing simple controls. Preserve functioning sliders and protected shopping paths. Removing unloaded backup files is housekeeping, not a performance claim.
- Triage inherited Theme Check findings in touched, active code; clean reusable components and inspect upstream Dawn compatibility. A wholesale theme replacement is not assumed in this estimate.

**Done when:** before/after results use the same routes and test conditions, straightforward fixes for the highest-impact measured bottlenecks are delivered, every audited app has a documented decision, and affected shopping, forms, reviews, locator, and access controls pass regression checks. Record deeper replacement work and remaining third-party limits with a specific next action/estimate. Final speed acceptance is repeated after subsequent waves add content or widgets.

### Speed and LCP acceptance

Maintain good field Core Web Vitals at the 75th percentile, assessed separately for mobile and desktop: **LCP ≤2.5 seconds, INP ≤200 ms, CLS ≤0.1**. The September 7 homepage field report already passes: mobile LCP 1.4s, INP 187ms, CLS 0; desktop LCP 1.2s, INP 109ms, CLS 0.02. Improve heavy initial downloads and slow-device lab behavior while preserving those results. [Google's Core Web Vitals guidance](https://web.dev/articles/vitals)

Capture available Shopify performance reporting and public field data, plus at least three comparable lab runs per priority page using documented device/network conditions and median results. Keep cold and repeat-visit results separate; control consent and login state when comparing app changes. Record LCP element/timing, CLS, lab responsiveness indicators, transferred JS/CSS, requests, long tasks, and screenshots. Lab TBT is a diagnostic, not a substitute for field INP. If field data is unavailable, say so; do not substitute a Lighthouse score and call it a field result.

Set route-specific byte/execution budgets after the baseline, require no unexplained regressions at later releases, and prioritize visible loading and responsiveness over a perfect score. Reference: [LCP optimization](https://web.dev/articles/optimize-lcp) and [Shopify theme performance practices](https://shopify.dev/docs/storefronts/themes/best-practices/performance).

### App audit and easy-replacement decisions

For each app/service record its owner, purpose, cost if accessible, recent use, data/integration dependencies, loaded routes, storefront requests/bytes/execution, consent behavior, and removal/rollback procedure. Assign **keep, configure/load selectively, replace, retire, or investigate**. Separate maintenance/cost savings from measured speed savings.

| Candidate from the audit | First investigation | Potential action, subject to testing |
| --- | --- | --- |
| Global custom JS with jQuery/Swiper | Map active consumers and execution; distinguish used sliders from dead code | Remove unused initialization; use CSS scroll snap or small native controls for simple cases; retain a library where its features justify it |
| Global CSS and locator assets | Confirm which routes need the styles and whether they block rendering | Load locator/section assets only where needed and remove proven-unused rules |
| Signifyd | Median homepage ~213 KiB / 304ms main-thread work; request-blocking median TBT 747ms versus 928ms baseline, with variable runs | Review vendor-supported scoping on Amazon/retail discovery routes; preserve fraud coverage on Shopify purchase paths |
| Klaviyo / Postscript | Klaviyo ~262 KiB; Postscript ~209 KiB despite absence from initial installed-app list. Main popup has optional SMS | Confirm SMS owner and capture handoff. Main popup is timed; alternate popup is custom-trigger only, so automatic duplication is not established |
| Yotpo / planned Bazaarvoice | ~206 KiB on homepage; reviews do render on tested PDP | Retain until migration works; scope loading to real review surfaces where supported and compare replacement cost |
| Stockist | No homepage requests identified in these captures | Keep and measure the locator route before considering replacement |
| accessiBe injection | ~230 KiB; hardcoded hidden trigger with background processing enabled | Confirm continued need, retire injection if approved, and fix actual native accessibility defects |
| Locksmith and old EasyLockdown files | Map active restrictions versus unused backup code | Preserve access controls; retire confirmed unused remnants. Deleting an unloaded backup is maintenance cleanup, not a speed win |
| Cin7, ShipStation, finance/admin tools and other installed apps | Determine whether they inject storefront code at all | Keep necessary operational apps; retire unused services only after ownership/data review |

No app is labeled slow solely because it is installed. Test replacements one at a time with equivalent functionality. Theme previews share live app configuration, so a preview does not automatically isolate an app uninstall or setting change. Use supported test settings/conditional code and an explicit rollback plan for global changes. Avoid adding another optimization, popup, or testing app without a demonstrated need.

## Wave 3 — Improve the shopping experience

**Lead:** ecommerce/theme development, with content and operations. **Estimate:** 6–10 hours using the existing product records, with approved assets, copy, and product mapping ready.

- Finish the existing slim-can and 4-pack records: correct sellable pack versus logistics case, SKU/GTIN, channel, retailer/Amazon destination, imagery, nutrition, claims, display fields, and collection placement. Avoid duplicate products. Resolve Strawberry slim-can's 45-versus-40 calories and green/black-versus-black tea conflict from approved facts. Align its retail-only CTA with appropriate schema; populate the 14 blank structured product descriptions from the same approved content source.
- Make mobile navigation, flavor/format discovery, product comparison, and the next purchase action clear. Use one obvious primary CTA appropriate to the product and clear secondary retail options. Preserve Halfday's playful typography, colors, and visual identity while improving spacing, legibility, and consistency.
- Improve PDP hierarchy: flavor/format, pack quantity, verified benefits and nutrition, purchase destination, shipping/retail expectations where relevant, reviews, and useful FAQs. Keep key content editable in Shopify.
- Review popup timing and interference, tap targets, keyboard/focus behavior, contrast, image text, and layout movement. Consider a lightweight mobile sticky CTA only when it solves an observed problem without obscuring content.
- Triage legacy Shogun pages and template assignments. Move simple active content into existing native sections where practical; retire confirmed-unused pages with a URL/redirect plan and retained reference copy. Check campaign destinations before retirement. Record any substantial page rebuild separately with its actual page count and estimate.

**Done when:** approved new formats are discoverable on their intended channels, representative mobile/desktop journeys work, restricted products remain protected, and content/design/redirect QA is complete. These are usability and merchandising improvements; revenue lift requires subsequent measurement.

### CRO priorities and measurement

Halfday's public site primarily sends customers to Amazon/retail, while Shopify also handles other order types. Measure these journeys separately. An Amazon click is a purchase-intent signal, not a confirmed sale.

| Hypothesis to validate | Improvement to prioritize | Success signal when measurement is available |
| --- | --- | --- |
| Stock labels and unclear destinations interrupt buying intent | Channel-correct badges and explicit purchase CTAs | Eligible PDP sessions reaching the intended destination; fewer dead ends |
| Format/pack ambiguity makes selection harder | Clear format navigation, pack labels, and product comparison | Collection-to-PDP progression and destination clicks by format/device |
| The mobile PDP makes the next action hard to find | Better information order and an accessible primary CTA | Mobile CTA engagement, with speed/layout and navigation guardrails |
| Signup friction or audience routing wastes interest | A valid offer, fewer competing prompts, correct list/flow route | Consented unique subscribers per eligible form viewer; expected flow entry |
| Missing or unclear reassurance creates doubt | Visible relevant reviews, factual FAQs, clear retailer options | Purchase-path progression; later sales outcomes where attributable |

Use existing Shopify/Klaviyo reporting and qualitative checks now where their coverage is verified. Specify denominators, eligible audience, device split, date windows, and staff/sample exclusions. Once analytics access and implementation are authorized, validate the event chain before running one hypothesis at a time. Track actual Shopify orders only for the relevant Shopify funnel; use Amazon/retailer purchase attribution only if supported access/data becomes available. Do not infer it from outbound clicks or Klaviyo's Shopify revenue panel.

Observe releases for at least 2–4 weeks after launch and longer if traffic is insufficient; compare periods with promotion/traffic differences noted. Use A/B testing only when volume and instrumentation can support a meaningful decision. Ongoing experiment execution is a follow-on cadence, not a promised conversion uplift inside the build estimate.

## Wave 4 — Strengthen email and search

**Lead:** lifecycle marketer and theme/content owners. **Estimate:** 8–12 hours, refreshing existing content and flows rather than creating a new email program from scratch.

- Preserve the active `send.drinkhalfday.com` sending domain. Validate authentication with an approved delivered test, not a new domain setup. After Wave 1 offer/routing repair, test welcome XruESR's `rc_active_subscriber=false`, no-Shopify-orders and legacy A-Game exclusions against missing/false/true properties and staff/sample cases. Make the primary benefit and CTA readable as email text rather than only images.
- Adjust main popup XDLfXK from its current two-second/all-audience display after offer correction. Last-seven-day submission rates were 0.25% desktop and 3.06% mobile; test eligible-audience targeting and later engagement-based timing. Verify optional SMS consent/handoff. Keep custom-trigger WtiUL4 until its test-page dependencies are resolved.
- Validate draft browse flow RX4C7p: Viewed Product → 2h → one email, 30-day re-entry. Fix its preview-text typo, add eligible public-product/channel filters and render a real event to check product links. Its Shopify order suppression cannot detect Amazon purchases. Do not release manual queues or activate all legacy cart/replenishment flows.
- Rebuild current consented engagement/new-subscriber audiences for a controlled new-format campaign. Historical sends include deactivated segments plus the full newsletter. Review the 26,960-member sunset segment before suppression: it requires one email ever but no recent sending opportunity, a material issue given the campaign gap. Broader re-engagement content is a follow-on after the initial audience test.
- Repair eight verified 404 destinations, including the old Shop page, retired Cranberry links, malformed relative blog links and FAQ anchors. Hide popup-testing and retained staff/menu utility collections from search appropriately, preserving dependencies and access checks. Fill missing descriptions on retained customer pages, including Watermelon and real shopping collections; do not optimize utility pages being hidden.
- Rewrite FAQ answers around actual purchase channels, caffeine by format and approved current nutrition. Fix Organization identity/social fields and complete the product/schema corrections begun in Waves 1 and 3. This provides concrete SEO/AEO content improvements without another app. [Google's guidance for AI search features](https://developers.google.com/search/docs/appearance/ai-features)
- Queue the overlapping 2022 blog articles and outdated health/product claims for editorial review. Use Search Console/backlink evidence when available to choose consolidation targets. Full article rewriting is separate from this wave's first-pass fixes.

**Done when:** selected journeys pass event/audience/content checks and are approved for activation, priority templates have accurate crawlable content, and legacy routes have intentional destinations. Inbox delivery, rankings, and AI citations are outcomes to monitor, not guaranteed deliverables.

## Wave 5 — Connect and finish

**Lead:** operations/3PL and ecommerce, supported by developer and review vendor. **Estimate:** 6–10 hands-on hours for existing-connection checks, routine configuration, and a standard review setup with vendor inputs ready. Unknown sync/data repairs and vendor waiting need separate estimates/dates once identified.

- Validate the channel map started in Wave 1: Shopify, Amazon, TikTok/AfterShip, and Faire → order owner → Cin7/ShipStation or other fulfillment route → inventory and tracking updates. Document one authoritative stock source and intended route per channel, SKU/case mapping, stock locations, buffers, cancellations, returns, and retry/duplicate handling.
- Resolve access to the existing Cin7 organization; the observed launch gate is not proof of broken sync. Trace representative existing orders with private customer details kept outside Git. Reconnect Faire or adjust routing only after confirming direction and duplicate prevention. Any paid/test order requires its own authorization.
- Confirm the actual AfterShip/TikTok/Amazon fulfillment arrangement and its owner. Do not infer the integration route from the app list. Document unresolved vendor-side work with a named owner and next checkpoint.
- Configure Bazaarvoice with the approved catalog/GTIN and Walmart/Target matches, run the supported eligible review export/import, reconcile counts/ratings/media, and verify onsite rendering. Begin coordination in Wave 1. Track retailer syndication acceptance separately until it is confirmed. If the vendor requires custom feed work or extensive manual product matching, estimate that work after inspecting its requirements. Keep Yotpo until the replacement and agreed retailer destinations are verified; do not equate an onsite widget launch with completed syndication.
- Finish performance/functional regression QA after the new content and review widget. Document the app decisions, reusable sections, content workflow, integration map, remaining debt, and rollback/release process. Establish shared Git hosting if Dylan supplies the preferred organization, and maintain CLI preview/review before releases.

**Done when:** the agreed channel routes and Faire behavior are verified, review migration is reconciled and verified at the agreed destinations, and the team can operate and update the store. If vendor dependencies remain, hand over completed storefront work with a clearly open integration/review milestone; do not mark the whole wave complete.

## Delivery controls and inputs

Each wave produces a focused change set, before/after evidence, a short acceptance checklist, and a release/rollback record. Preserve the original Git baseline; pull/reconcile current merchant edits before theme work. Validate affected mobile/desktop and keyboard flows and run Theme Check for code changes, distinguishing the inherited 126 errors/361 warnings from new regressions. Check actual runtime issues rather than treating every inherited warning as a customer-facing defect.

| Needed from | Input / decision | Needed by |
| --- | --- | --- |
| Leslie / ecommerce owner | Purchase channel per format, priority formats, offer and brand/content approval | Wave 1; final assets before Wave 3 |
| Content owner | Approved product imagery, nutrition/claims, pack copy, retailer/Amazon URLs | Before Wave 3 |
| Lifecycle owner | Audience/exclusion and offer decisions, sender-domain access, test-profile approval | Wave 1; sender/flow work before Wave 4 |
| Operations / 3PL | Existing Cin7 organization access, route owners, SKU/case mapping, representative orders | Begin Wave 1; required for Wave 5 completion |
| Bazaarvoice / retailer contacts | Onboarding, review import eligibility, GTIN matches, syndication acceptance | Begin Wave 1; external completion date tracked separately |
| Dylan | Consolidated wave review, release authorization, any later analytics/ads access confirmation | At each delivery gate |

## Email draft for Leslie

Hey Leslie,

I’ve gone through the site and Klaviyo and put together a plan based on your list. There’s useful work already in place, so we can build on that and clean up what needs attention. I’d break it into five waves:

1. **Quick fixes (2-4 hours)**
   Sort out the out-of-stock messaging on products that send people to Amazon, fix the footer email signup so it goes to the right welcome flow, and clean up incorrect links. We’ll also check that this doesn’t affect staff orders or anything being purchased through Shopify.

2. **Site speed and app cleanup (6-10 hours)**
   The videos lower down the page are downloading a lot of data before people get to them. We’ll change how those load, resize the larger images and clean up code that doesn’t need to run on every page. We’ll also review Signifyd, the SMS setup and the accessibility tool to see what can be simplified while keeping the features we need.

3. **Product updates and shopping experience (6-10 hours)**
   Get the 4-packs and slim cans showing with the right images, product details and links. We’ll also tidy up the navigation and product pages so it’s easier to find a flavour or format and know where to buy it, while keeping the Halfday look and feel.

4. **Klaviyo and SEO (8-12 hours)**
   Make sure the signup offer and welcome emails send people to the right place, refresh the browse reminder and sort out who should receive the relaunch emails. The sending domain is already set up. On the site, we’ll fix broken links, keep testing pages out of search, and update the product information, search descriptions and FAQs so they match what you’re selling now.

5. **Integrations and reviews (6-10 hours)**
   Get a clear picture of how Cin7, ShipStation, Faire and TikTok/Amazon fulfillment are connected, then address any straightforward setup issues. We’ll also work through the Bazaarvoice setup and check the review migration before removing Yotpo.

That puts the initial work at around 28-46 hours. I’d aim to get it through over 1-2 weeks once we have the images, product details and access we need. If we find anything more involved with the integrations, I’ll flag it with a separate estimate. Bazaarvoice and the retailer side may take longer depending on their turnaround.

We can pick up Google Analytics and Ads once access is sorted.
