# Halfday modernization roadmap

**Current three-wave plan. First Wave 1 release published by Dylan on September 8, 2026. The combined tablet, performance and accessibility follow-through is live as of September 9. Catalog/app dependencies remain open.** This replaces the earlier five-wave grouping; the work is grouped around site readiness, email relaunch, and operations/reviews.

[Verified audit](focused-audit-2026-09-07.md) · [Wave 1 checklist and preview](wave-1-progress.md) · [LCP/CLS findings](lcp-cls-follow-up-2026-09-08.md)

| Wave | Outcome | Estimated hands-on time | Status |
| --- | --- | --- | --- |
| 1. Site cleanup, speed and shopping experience | Current content, clear buying paths, lighter pages and concrete SEO repairs | 14–20 hours | Combined theme work live at bb0169f; catalog/app and editorial decisions open |
| 2. Klaviyo cleanup and relaunch | Correct signup/offer journey, refreshed welcome/browse messaging and eligible campaign audience | 8–12 hours | Not started |
| 3. Fulfillment connections and reviews | Verified channel routing, routine sync repairs and Bazaarvoice migration | 6–10 hours | Vendor/access inputs needed |

**Planning total: 28–42 hours**, targeting 1–2 calendar weeks for directly controlled work once approved product information, access and decisions are available. This is a focused first pass using existing assets and integrations, not an allowance for a full redesign, 32 article rewrites, unlimited flows or custom integration repair. Track vendor waiting and retailer syndication separately.

## Wave 1: site cleanup, speed and shopping experience

1. Correct misleading stock messaging and purchase paths without weakening Shopify inventory checks or Locksmith access controls.
2. Defer offscreen testimonial/footer video, size posters/images, prioritize the first PDP image, scope route assets, reserve image/widget space and measure LCP and CLS. Preserve used brand typography. The homepage already passes field Core Web Vitals; a download reduction is not proof of better LCP or INP.
3. Review measured app costs, especially Signifyd, Postscript/Klaviyo overlap and the hardcoded accessiBe script. Retain needed operations apps, Stockist and Yotpo pending dependencies. Shared app settings are not isolated by the dev theme.
4. Preserve the existing product setup. Resolve the documented Strawberry nutrition/ingredient contradictions and missing caffeine answer; broaden 4-pack/slim-can merchandising only for a specifically confirmed public assortment. Do not convert logistics cases into consumer products.
5. Improve mobile/desktop flavor and format discovery, product information hierarchy, primary purchase CTAs, comparison content and accessibility while preserving Halfday's brand.
6. Fix verified broken/internal links, search descriptions, product/organization schema, FAQ content and test/utility discovery. Retain useful blog content and queue claim review/consolidation decisions.

**September 8 progress:** Dylan published Git-connected theme **142757101768**, `halfday-shopify/main`, at `2c8ff4f`. All 455 downloaded live files match that release. The initial performance, accessibility, metadata, link, image and stylesheet improvements are now the production baseline. The obsolete Shogun product assignments were also cleared with approval.

**Latest release, September 9:** the tablet-label and LCP work is merged and live at **`bb0169f`**, tag **`baseline/live-wave-1-2026-09-09`**. Shopify's overnight Locksmith changes were preserved. All 455 live files match main; 15-route regression checks passed before and after deployment. Live desktop/tablet/mobile samples were visually inspected. See the [release record](wave-1-release-2026-09-09.md).

The [combined performance audit](wave-1-lcp-completion-2026-09-08.md) measured about 69% less Shop All initial transfer and median lab LCP from 4.18s to 3.53s; product LCP remains variable. These are September 8 lab measurements, not new production field results. New work stays on **`djh/wave-1-agentready-verification`** and development theme **142755430600**.

Agentready Apply now succeeds with a durable 34/34 receipt. Brand-only Agent JSON with the correct retailer description and policies is verified and prepared in development. Live embed and JSON-LD remain off; catalog approvals stay off pending retailer-safe output checks. The contact settings UI still does not consistently reflect/save the email that is present in generated support output. [Latest app findings](agentready-product-feedback.md).

**September 9 release update:** Dylan merged PR #1 at `2893a6f`. New contrast and brand-only Agentready delivery work uses `djh/wave-1-contrast-agentready` and remains development-only.

**Latest autonomous pass:** additional homepage native accordion, keyboard-focus and responsive image repairs are audited in the development theme. Seven native legacy redirects are imported and verified live as 301s to working destinations. The [completion decision list](wave-1-completion-questions.md) contains exact catalog, app and editorial questions plus verification evidence. PR #1 is merged at `2893a6f`; the latest follow-up is development-only.

**Open to finish Wave 1:** exact product fact confirmations; Signifyd/Postscript ownership; expired campaign and Cranberry decisions; Search Console access for consolidation; and Agentready catalog/JSON-LD/channel verification. Dylan approved the contrast pass, which is implemented in development. Keep accessiBe and leave the health articles unchanged. The new brand-only Agentready and contrast changes await an authorized release of the development PR. Klaviyo signup/offer activation belongs to Wave 2.

**Acceptance:** documented before/after evidence, no new Theme Check offenses, verified Amazon buying links and relevant mobile/desktop interactions, approved product content and an exact release diff. Dylan confirmed all customer buying redirects to Amazon, so authenticated staff/sample checkout is not a release gate. Preserve its legacy code and access controls. Each follow-through release still requires approval before merging/pushing main.

## Wave 2: Klaviyo cleanup and relaunch

1. Repair general-footer routing from HelloFresh Sample Campaign to Halfday Newsletter for new signups after checking consent/bridges. Do not migrate historical members wholesale.
2. Verify NEWERA15/Amazon redemption and align popup, success and welcome copy/destinations. The branded sending domain is already active; validate delivered authentication with an approved test instead of rebuilding it.
3. Test welcome eligibility, including the legacy A-Game exclusion and `rc_active_subscriber` missing/false/true values. Improve text/button accessibility in image-heavy emails.
4. Test main popup timing and eligible targeting, especially desktop. Settle the optional SMS/Postscript handoff; the alternate popup is custom-trigger only.
5. Validate the existing two-hour browse reminder with real event data and eligible products. Shopify order suppression cannot detect an Amazon purchase.
6. Rebuild current consented/engaged audiences for a controlled relaunch. Review the 26,960-member sunset segment's lack of a recent sending-opportunity condition before any suppression. Do not activate manual queues or all old order flows.

**Acceptance:** approved offer, controlled signup/event/rendering checks, correct consent/exclusions and selected messages ready for approved activation. Deliverability, sales and engagement are monitored outcomes, not guaranteed uplift.

## Wave 3: fulfillment connections and reviews

1. Map Shopify, Amazon, TikTok/AfterShip and Faire to order owner, fulfillment route and inventory/tracking source. Validate SKU/case and location mappings using representative existing records.
2. Resolve existing Cin7 organization access and trace current Cin7/ShipStation/3PL routes. An access gate or installed app alone does not establish broken sync.
3. Reconnect Faire or make routine configuration corrections only after confirming direction, ownership and duplicate prevention. Estimate specific deeper faults separately.
4. Coordinate Bazaarvoice onboarding, catalog/GTIN matching, supported review import and onsite rendering. Preserve Yotpo until the replacement is verified. Track Walmart/Target syndication acceptance separately from installing an onsite widget.
5. Complete regression checks, handover and the release checklist.

**Acceptance:** documented operational ownership and successful supported verification of the selected routes/review migration. No fixed completion date is promised for vendor onboarding or unknown integration repairs.

## Working boundaries

- GitHub main is connected to the live theme. Use Shopify CLI with development/unpublished themes and descriptive feature/fix branches. A main push is a production deployment and needs release authorization. Production repair is permitted for confirmed broken functionality; otherwise development only. Authorized Agentready setup and Shogun assignment cleanup changed shared settings/data; the September 9 theme release changed neither; separate Agentready shared-setting tests and restoration are documented.
- Product records, menus, metafields, article content and app settings are shared store data. Theme previews do not isolate their mutation.
- GA setup, Google Ads and full attribution implementation remain deferred until Dylan confirms readiness. GTM was empty/unused and is excluded.
- Amazon clicks are intent signals, not confirmed sales. Use actual channel data before claiming conversion lift.
- Request approved product facts/assets, content decisions, operations contacts and Bazaarvoice inputs early. Track delivery work separately from client/vendor turnaround.
