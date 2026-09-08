# Halfday modernization roadmap

**Current three-wave plan. Wave 1 authorized for development on September 7, 2026.** This replaces the earlier five-wave grouping; the work is grouped around site readiness, email relaunch, and operations/reviews.

[Verified audit](focused-audit-2026-09-07.md) · [Wave 1 checklist and preview](wave-1-progress.md)

| Wave | Outcome | Estimated hands-on time | Status |
| --- | --- | --- | --- |
| 1. Site cleanup, speed and shopping experience | Current content, clear buying paths, lighter pages and concrete SEO repairs | 14–20 hours | In progress on development theme |
| 2. Klaviyo cleanup and relaunch | Correct signup/offer journey, refreshed welcome/browse messaging and eligible campaign audience | 8–12 hours | Not started |
| 3. Fulfillment connections and reviews | Verified channel routing, routine sync repairs and Bazaarvoice migration | 6–10 hours | Vendor/access inputs needed |

**Planning total: 28–42 hours**, targeting 1–2 calendar weeks for directly controlled work once approved product information, access and decisions are available. This is a focused first pass using existing assets and integrations, not an allowance for a full redesign, 32 article rewrites, unlimited flows or custom integration repair. Track vendor waiting and retailer syndication separately.

## Wave 1: site cleanup, speed and shopping experience

1. Correct misleading stock messaging and purchase paths without weakening Shopify inventory checks or Locksmith access controls.
2. Defer offscreen testimonial/footer video, size posters/images, prioritize the first PDP image, scope route assets and measure the result. Preserve used brand typography. The homepage already passes field Core Web Vitals; a download reduction is not proof of better LCP or INP.
3. Review measured app costs, especially Signifyd, Postscript/Klaviyo overlap and the hardcoded accessiBe script. Retain needed operations apps, Stockist and Yotpo pending dependencies. Shared app settings are not isolated by the dev theme.
4. Finish 4-pack/slim-can merchandising using approved consumer-pack, SKU/GTIN, nutrition, imagery, channel and access decisions. Existing case records must not automatically become consumer products.
5. Improve mobile/desktop flavor and format discovery, product information hierarchy, primary purchase CTAs, comparison content and accessibility while preserving Halfday's brand.
6. Fix verified broken/internal links, search descriptions, product/organization schema, FAQ content and test/utility discovery. Retain useful blog content and queue claim review/consolidation decisions.

**Acceptance:** reviewable development preview, documented before/after measurements, no new Theme Check offenses, verified public and protected buying paths, approved product content and an exact release diff. Keep unfinished content, app and access-dependent items visible on the checklist.

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

- Wave 1 is authorized on a development branch/theme. Production repair is permitted for confirmed broken functionality; otherwise development only. No production theme changes have been made. Authorized Agentready setup changed shared app settings; the current theme follow-up is development-only.
- Product records, menus, metafields, article content and app settings are shared store data. Theme previews do not isolate their mutation.
- GA setup, Google Ads and full attribution implementation remain deferred until Dylan confirms readiness. GTM was empty/unused and is excluded.
- Amazon clicks are intent signals, not confirmed sales. Use actual channel data before claiming conversion lift.
- Request approved product facts/assets, content decisions, operations contacts and Bazaarvoice inputs early. Track delivery work separately from client/vendor turnaround.
