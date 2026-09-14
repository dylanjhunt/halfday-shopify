# Waves 2 and 3: implementation and review handoff

**Scope update:** Dylan confirmed Yotpo stays. Caffine Functions is not being added and review replacement work is inactive. The original Walmart/Target syndication request remains separately deferred. See the [current Yotpo maintenance plan](wave-3/yotpo-maintenance.md).

The follow-up pass verified four published desktop product pages, Peach review pagination/form opening, and Strawberry's no-review fallback. The empty Yotpo price metadata is confirmed on all four samples; its fix remains unpublished. CLI confirmed the preview capacity is still full. Automatic approval review prevented another direct Klaviyo-origin check because the account identity could be another client; no account refresh was claimed. Halfday identity/login must be established before account work resumes.

September 14, 2026. Branch **`djh/wave-3-review-prep`** includes the existing Wave 2 email package, current main through `9ac3fc5` and the work below. Main's three newer Shopify/Locksmith commits were incorporated into the development branch. **No main push, production theme upload, app setting change, order, signup or email send was performed.**

Wave 1 PR #2 remains open and its development theme `142755430600` is preserved. The live Git-connected theme remains `142757101768`. These waves are prepared for review, not fully released or operationally certified.

## What is completed

| Area | Concrete work | Evidence / review |
| --- | --- | --- |
| Wave 2 email creative | Three welcome messages, one browse fallback and one relaunch campaign; responsive HTML, plain text, subjects and preheaders | [Five-email preview](wave-2/preview/index.html), [implementation outline](wave-2/implementation-outline.md) |
| Signup and offer | Proposed footer/list correction, popup/success copy, no-offer alternative and conditional verified-offer version | [Signup specification](wave-2/signup-and-offer.md) |
| Eligibility and release | Welcome property cases, consumer/operational exclusions, browse-event contract, campaign cohorts, draft staging and rollback | [Eligibility and cutover](wave-2/eligibility-and-cutover.md) |
| Faire connection | Read current direction/location/payment/tag/cancellation/fulfillment settings; traced one existing order's ShipStation fulfillment updates | [Operations audit](wave-3/operations-audit-2026-09-14.md) |
| Product mapping | Recorded all 12 linked Faire listings, both sides' SKUs, every Shopify product ID/barcode, shipping weights/package and five unlinked legacy listings | [Catalog worksheet](wave-3/catalog-map.json) |
| Catalog checks | Offline validator checks identifiers, GTIN checksum, quantity types and approval evidence; preserves intentional SKU aliases | [Run instructions](wave-3/README.md), [validation result](../reports/wave-3-catalog-validation-2026-09-14.json) |
| Reviews | Verified Yotpo aggregate baseline and pixel warning; retain the provider and check onsite health | [Maintenance plan](wave-3/yotpo-maintenance.md); migration research archived |
| Local theme repair | Fixed undefined variant reference in Yotpo price metadata using the product's selected/first available variant; no JS or style changes | `sections/Product-review-new.liquid`; [Theme Check comparison](../reports/wave-3-theme-check-2026-09-14.json) |

## Findings that change the implementation plan

- **Faire is connected.** A general reconnect is unnecessary and could disturb existing mappings. Twelve products are linked; five older listings need a disposition decision. Two slim-can SKU aliases already work as explicit mappings and must be preserved.
- **Fulfillment is currently Faire → Shopify only.** The overview's OFF summary is incomplete. An existing order shows ShipStation writing fulfillment back into Shopify, but that does not prove tracking reaches Faire. Confirm the owner and other writers before changing the direction. Cancellations currently sync neither way.
- **Shipping fields need confirmation.** All four slim-can records and Watermelon have zero Shopify weight. All 12 linked products use the default Seeding Kit package; the other seven have 10 lb product weight. Check the actual logistics source before replacing values.
- **The review library exists.** Yotpo reports 724 collected / 706 published reviews, 4.81 average, and 9,610 requests sent for All time. The difference needs reconciliation. Retain Yotpo and its original data; no migration is planned. Its Customer Events Pixel warning concerns shared tracking, not proof that onsite reviews fail.
- **Klaviyo still needs Halfday login.** The store-specific launch ends at login. September 7 remains the last verified account configuration. Current Faire order tags `Faire` and `Wholesale` provide concrete fields to investigate for exclusions; they are not automatically profile properties.

## What cannot be tested or applied solely in a dev theme

| Remaining work | Required next input | Prepared next action |
| --- | --- | --- |
| Klaviyo native template/flow staging and live-setting refresh | Sign in to the Halfday account | Recheck sources, consent, events and queues; create isolated templates/flow copies with every action Draft |
| Offer and CTA choice | Confirm usable Amazon offer/ASIN destinations, or approve no-offer copy; settle Postscript/SMS ownership | Finalize message/form copy and exact link list before review |
| Signup, authentication and inbox QA | Approved test inbox and permission for controlled signup/test delivery | Run the documented eligibility, consent, headers and rendering checks; do not test on a real customer |
| Cin7/ShipStation route proof | Read access to the existing Cin7 organization and ShipStation account; owner review if expanded permissions are necessary | Trace the same historical order, inventory location and job IDs; do not reconnect or replay orders |
| Faire corrections and product cleanup | Confirm fulfillment/cancellation authority, sample deduction, five legacy listings and approved pack/weight/dimension data | Prepare exact setting and mapping diff, then a controlled test plan |
| TikTok / AfterShip / Amazon route | Account access, exact AfterShip product, shipping mode and operations owner | Trace an existing order to the actual fulfillment/tracking source without triggering a shipment |
| Yotpo account health | Access to request settings and confirmation of eligible order types/pixel ownership | Inspect existing request rules and product coverage; no export, import or provider change |
| Theme rendering QA | A spare theme slot or identification of an existing unpublished theme that can be safely reused | Push the exact reviewed branch through CLI, test review metadata/visuals/clicks/loading and compare performance |
| Release | Approval of the completed theme/account change packet | Publish only the specifically approved changes; no automatic merge when this preparation finishes |

Shopify rejected explicit new unpublished-theme creation because the store is at its **20-theme limit**. No theme was removed and no existing preview was overwritten. The price-reference fix is locally checked only. Shared product records, app configuration, consent, flows and fulfillment are not isolated by a theme preview.

## Verification and limits

- Theme Check comparison: 122 inherited errors remain; warnings decrease from 385 to 384. No new offenses. Only the undefined `variant` warning was removed. This is not a clean whole-theme lint pass or a browser regression pass for the new repair.
- Catalog worksheet: all 12 GTINs pass format/checksum, no duplicate identifier errors, two SKU aliases explicitly flagged. All 12 mappings remain unapproved for pack/operations use; checksum validity does not verify product identity or review-family eligibility.
- Five automated validator tests cover valid/invalid GTINs, alias retention, missing approval evidence, invalid quantities, duplicate/unlinked IDs and malformed input.
- The five email browser layouts were audited previously at mobile/desktop widths. No fresh inbox delivery, native Klaviyo compilation, real event preview or consumer conversion measurement has been performed.
- Read-only order evidence establishes a historical Shopify/Faire/ShipStation connection, not complete end-to-end health. No new stock push, order backfill, customer export, review import or vendor communication was performed.

## Review order

1. Restore account access and confirm product/operations ownership while reviewing the email copy and offer.
2. Stage Klaviyo drafts, complete native previews and prepare the controlled signup test.
3. Verify historical integration records, finish the catalog map and agree exact routing corrections.
4. Verify the retained Yotpo review experience and account eligibility rules. Preview any theme changes in an isolated slot. Retailer syndication is separately deferred.
5. Review and authorize each production cutover separately. Keep actual channel sales, email intent clicks, onsite review visibility and retailer syndication as separate outcomes.

No GA, Google Ads or GTM work was added. Existing decisions to retain accessiBe and health articles remain in force. Outstanding team fact and app-ownership questions from Wave 1 are still pending; this pass does not silently resolve them.
