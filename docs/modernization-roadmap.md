# Halfday modernization roadmap

**Internal delivery plan · September 7, 2026 · Planning estimates, pending implementation kickoff**

Modernize Halfday's existing Shopify store so it is easier to shop, faster to load, simpler to maintain, and reliable across email, retail, and fulfillment. Keep the brand's personality and useful existing work. Use native Shopify sections, editable content, and minimal JavaScript as the default.

This is the single delivery roadmap. The [store/theme audit](initial-audit-2026-09-07.md) and [Klaviyo audit](klaviyo-audit-2026-09-07.md) remain the evidence snapshots; this document replaces their separate priority sequences. Setup is complete: Shopify CLI, downloaded live-theme baseline, local Git, and Claude project guidance. Implementation has not started, and no live settings or theme code have been changed.

## Schedule at a glance

| Wave | Simple outcome | Estimated hands-on time | Target window |
| --- | --- | --- | --- |
| 1. Fix the essentials | Correct misleading stock messages, signup routing, and obvious journey problems | 3–5 business days | Week 1 |
| 2. Make the site faster | Improve loading and LCP; remove or replace measured app/theme overhead | 5–7 business days | Weeks 2–3 |
| 3. Improve the shopping experience | Launch the right new products and improve mobile browsing and conversion paths | 5–7 business days | Weeks 3–4 |
| 4. Strengthen email and search | Relaunch useful Klaviyo journeys and improve SEO/AEO foundations | 4–6 business days | Weeks 5–6 |
| 5. Connect and finish | Validate fulfillment/Faire, complete the review migration, and hand over a maintainable store | 5–8 business days | Weeks 6–8 |

**Plan for approximately 6–8 calendar weeks, with 22–33 hands-on business days.** Windows are planning ranges, not five independent deadlines. They allow for review and QA and assume one primary implementer with timely content, lifecycle, and operations support. Allow one consolidated client review per wave, typically returned within two business days. Begin vendor coordination in Wave 1 so it can progress alongside site work. Cin7/3PL access, Bazaarvoice onboarding, retailer acceptance, and content production can extend the affected milestones beyond eight weeks; the hands-on estimates exclude waiting for those parties.

This estimate covers focused modernization of the existing theme and integrations. A full rebrand/replatform, new custom integration middleware, extensive new content production, or a major vendor-driven data repair needs a separate estimate. Recheck scope and remaining effort at the end of each wave.

**Out of scope for now:** GA setup, Google Ads, and full attribution implementation await Dylan's confirmation. GTM was confirmed empty/unused and is excluded. Their absence does not block storefront improvements; conversion-lift claims and paid-media launch readiness remain limited until measurement is available.

## Wave 1 — Fix the essentials

**Lead:** Dylan/theme development, with ecommerce, lifecycle, and operations owners. **Estimate:** 3–5 business days.

- Establish a repeatable mobile/desktop speed and UX baseline for home, Shop All, Variety Packs, a representative PDP, a slim-can page, and the store locator. Record current app/script loading and the primary customer paths before changing them.
- Define each product's intended purchase channel: Amazon, retailer discovery, Shopify purchase, or restricted staff/sample. Correct the confirmed variety-pack sold-out messaging and related schema to match that model. Do not invent Amazon availability or weaken inventory checks on actual Shopify purchases.
- Correct the footer signup destination after confirming the intended newsletter list, consent, and valid offer. Test form → list → welcome eligibility with an approved test profile. Preserve suppression and avoid enrolling historical lists into live flows by accident.
- Fix verified stale preview links and confusing destinations; check navigation, key CTAs, and protected product visibility.
- Start the product/pack mapping sheet, app ownership inventory, Cin7 organization-access request, 3PL routing discovery, and Bazaarvoice/retailer onboarding. Assign the person who can resolve each dependency.

**Done when:** the priority stock/signup problems have been tested, public and restricted purchase paths behave correctly, the baseline is saved, and each dependency has an owner. Theme changes are reviewed in a development preview before an authorized release.

## Wave 2 — Make the site faster

**Lead:** theme development, with app owners. **Estimate:** 5–7 business days.

- Measure the actual LCP element and its loading sequence on priority routes. Address the limiting factor: server response, resource discovery, image download, or render delay. Inspect the homepage's separate desktop/mobile priority images before changing preload behavior.
- Use correct image sizes/formats, responsive sources, dimensions, and deliberate loading priority. Keep the visible hero eager; lazy-load suitable offscreen media. Review font families/weights, loading, and layout shifts while preserving Halfday typography.
- Audit all 22 installed apps plus theme-injected services. Attribute cost using network and performance recordings; app count alone does not establish a slowdown. Apply the app decisions below.
- Reduce unnecessary global CSS/JS and conditionally load section/route features. Investigate the existing jQuery/Swiper bundle, global locator styles, repeated sliders, and duplicate loaders. Replace simple behavior with native HTML/CSS or small vanilla JS where it preserves functionality.
- Triage inherited Theme Check findings in touched, active code; clean reusable components and inspect upstream Dawn compatibility. A wholesale theme replacement is not assumed in this estimate.

**Done when:** before/after results use the same routes and test conditions, the principal measured bottlenecks are addressed, every audited app has a documented decision, and shopping, forms, reviews, locator, and access controls pass regression checks. Record any remaining third-party limits and the next action. Final speed acceptance is repeated after subsequent waves add content or widgets.

### Speed and LCP acceptance

Target good field Core Web Vitals at the 75th percentile, assessed separately for mobile and desktop: **LCP ≤2.5 seconds, INP ≤200 ms, CLS ≤0.1**. These are targets, not current Halfday results or a guaranteed outcome. [Google's Core Web Vitals guidance](https://web.dev/articles/vitals)

Capture available Shopify performance reporting and public field data, plus at least three comparable lab runs per priority page using documented device/network conditions and median results. Keep cold and repeat-visit results separate; control consent and login state when comparing app changes. Record LCP element/timing, CLS, lab responsiveness indicators, transferred JS/CSS, requests, long tasks, and screenshots. Lab TBT is a diagnostic, not a substitute for field INP. If field data is unavailable, say so; do not substitute a Lighthouse score and call it a field result.

Set route-specific byte/execution budgets after the baseline, require no unexplained regressions at later releases, and prioritize visible loading and responsiveness over a perfect score. Reference: [LCP optimization](https://web.dev/articles/optimize-lcp) and [Shopify theme performance practices](https://shopify.dev/docs/storefronts/themes/best-practices/performance).

### App audit and easy-replacement decisions

For each app/service record its owner, purpose, cost if accessible, recent use, data/integration dependencies, loaded routes, storefront requests/bytes/execution, consent behavior, and removal/rollback procedure. Assign **keep, configure/load selectively, replace, retire, or investigate**. Separate maintenance/cost savings from measured speed savings.

| Candidate from the audit | First investigation | Potential action, subject to testing |
| --- | --- | --- |
| Global custom JS with jQuery/Swiper | Map active consumers and execution; distinguish used sliders from dead code | Remove unused initialization; use CSS scroll snap or small native controls for simple cases; retain a library where its features justify it |
| Global CSS and locator assets | Confirm which routes need the styles and whether they block rendering | Load locator/section assets only where needed and remove proven-unused rules |
| Klaviyo forms; Shopify Forms; Messaging/Postscript | Check collection-channel ownership, overlapping prompts, loaders, and form targeting | Consolidate duplicate experiences and retain the required email/SMS and consent functions |
| Yotpo / planned Bazaarvoice | Measure current widget cost and compare the proposed replacement on a preview | Retain Yotpo until migration works; load the chosen integration efficiently and verify reviews remain discoverable |
| Stockist | Measure map/locator loading and document required search/filter features | Load on the locator route or on appropriate interaction; consider a native directory only if it meets the actual requirements |
| accessiBe injection | Establish runtime cost and inspect the site's underlying accessibility | Fix native markup/interactions; assess whether the service is still needed with the owner |
| Locksmith and old EasyLockdown files | Map active restrictions versus unused backup code | Preserve access controls; retire confirmed unused remnants. Deleting an unloaded backup is maintenance cleanup, not a speed win |
| Cin7, ShipStation, finance/admin tools and other installed apps | Determine whether they inject storefront code at all | Keep necessary operational apps; retire unused services only after ownership/data review |

No app is labeled slow solely because it is installed. Test replacements one at a time with equivalent functionality. Theme previews share live app configuration, so a preview does not automatically isolate an app uninstall or setting change. Use supported test settings/conditional code and an explicit rollback plan for global changes. Avoid adding another optimization, popup, or testing app without a demonstrated need.

## Wave 3 — Improve the shopping experience

**Lead:** ecommerce/theme development, with content and operations. **Estimate:** 5–7 business days after assets and product mapping are ready.

- Finish the existing slim-can and 4-pack records: correct sellable pack versus logistics case, SKU/GTIN, channel, retailer/Amazon destination, imagery, nutrition, claims, display fields, and collection placement. Avoid duplicate products. Verify the sampled “Silm Can” typo, 12-pack copy, and mismatched asset references.
- Make mobile navigation, flavor/format discovery, product comparison, and the next purchase action clear. Use one obvious primary CTA appropriate to the product and clear secondary retail options. Preserve Halfday's playful typography, colors, and visual identity while improving spacing, legibility, and consistency.
- Improve PDP hierarchy: flavor/format, pack quantity, verified benefits and nutrition, purchase destination, shipping/retail expectations where relevant, reviews, and useful FAQs. Keep key content editable in Shopify.
- Review popup timing and interference, tap targets, keyboard/focus behavior, contrast, image text, and layout movement. Consider a lightweight mobile sticky CTA only when it solves an observed problem without obscuring content.
- Inventory legacy Shogun pages and template assignments. Migrate useful active content into native sections; retire unused pages with a URL/redirect plan and retained reference copy. Check campaign destinations before retirement.

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

**Lead:** lifecycle marketer and theme/content owners. **Estimate:** 4–6 business days.

- Rationalize the 42 Klaviyo flows and 16 forms into a clear owner/purpose map. Review sender authentication, consent, exclusions, offer validity, audience targeting, manual queues, and legacy filters before changing statuses.
- Refresh and validate the existing welcome series first, then a focused browse-interest and re-engagement journey where events and audiences support them. Prioritize up to three core journeys in this wave; inventory the remainder for later work. Shopify cart/order/replenishment triggers are not assumed to represent Amazon purchases. Preserve staff/sample/wholesale exclusions.
- Validate a controlled signup, relevant onsite events, flow eligibility, suppression, rendering, and Amazon/retailer destinations. Existing Amazon links already have parameters; this work verifies destinations and naming without claiming end-to-end attribution. Do not release manual queues as a cleanup shortcut.
- Correct page descriptions, factual product/schema content, organization identity/social links, canonical internal URLs, heading structure, useful alt text, and redirects. Check key templates, sitemap/robots behavior, and broken destinations; add Search Console inspection only when access is available.
- Improve SEO/AEO through clear product facts, answerable questions, helpful visible copy, and accurate structured data. Avoid unsupported stock/price/health claims or special “AI optimization” scripts. [Google's guidance for AI search features](https://developers.google.com/search/docs/appearance/ai-features)

**Done when:** selected journeys pass event/audience/content checks and are approved for activation, priority templates have accurate crawlable content, and legacy routes have intentional destinations. Inbox delivery, rankings, and AI citations are outcomes to monitor, not guaranteed deliverables.

## Wave 5 — Connect and finish

**Lead:** operations/3PL and ecommerce, supported by developer and review vendor. **Estimate:** 5–8 hands-on business days; external milestones may take longer.

- Validate the channel map started in Wave 1: Shopify, Amazon, TikTok/AfterShip, and Faire → order owner → Cin7/ShipStation or other fulfillment route → inventory and tracking updates. Document one authoritative stock source and intended route per channel, SKU/case mapping, stock locations, buffers, cancellations, returns, and retry/duplicate handling.
- Resolve access to the existing Cin7 organization; the observed launch gate is not proof of broken sync. Trace representative existing orders with private customer details kept outside Git. Reconnect Faire or adjust routing only after confirming direction and duplicate prevention. Any paid/test order requires its own authorization.
- Confirm the actual AfterShip/TikTok/Amazon fulfillment arrangement and its owner. Do not infer the integration route from the app list. Document unresolved vendor-side work with a named owner and next checkpoint.
- Complete Bazaarvoice catalog/GTIN and Walmart/Target matching, eligible review export/import, count/rating/media reconciliation, onsite QA, and retailer syndication verification. Begin this coordination in Wave 1. Keep Yotpo until the replacement and agreed retailer destinations are verified; do not equate an onsite widget launch with completed syndication.
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

## Slack draft for Leslie

Hi Leslie — I’ve pulled everything into a five-wave plan to modernize the Halfday site:

1. **Fix the essentials — 3–5 business days:** clean up stock messaging, email signup issues, and key links.
2. **Make the site faster — 5–7 business days:** improve loading speed and review apps for easy cleanup or replacements.
3. **Improve shopping — 5–7 business days:** get the new formats onto the site and make the mobile shopping experience clearer and easier to convert.
4. **Strengthen email and search — 4–6 business days:** refresh the core Klaviyo flows and improve SEO and AI-search readiness.
5. **Connect and finish — 5–8 business days:** validate fulfillment and Faire, complete the review migration, and finish QA.

I’d plan for **roughly 6–8 weeks overall**, assuming timely access, assets, and approvals. We’ll start coordinating with the 3PL and Bazaarvoice immediately; their turnaround may extend those pieces. Google Analytics and Ads will be scoped once access is ready; GTM is excluded for now.
