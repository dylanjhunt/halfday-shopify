# Reviews: historical migration packet

**Inactive after Dylan’s decision to retain Yotpo.** Do not execute the replacement, export/import, request cutover or app-removal steps below. They are historical research, not the current delivery plan. Caffine Functions is not being added. The original retailer-syndication request remains separately deferred. Current work is in [Yotpo maintenance](yotpo-maintenance.md).

September 14, 2026. No review imports, exports containing reviewer data, invitations, widget changes or pixel reconnections were performed in the live account.

## Verified account baseline

Halfday's embedded Yotpo dashboard shows **9,610 requests sent, 724 collected reviews, 706 published reviews and 4.81 average rating** with All time selected. These aggregate values are a reconciliation starting point, not a complete export or per-product coverage count. The 18-review difference needs status reconciliation; do not assume it is spam or discard it. Shopify's app detail displayed a $15/month plan, not a verified current billing invoice.

The dashboard says it has lost connection to the **Customer Events Pixel**. This is a conversion-measurement warning, not proof that onsite reviews fail. Reconnecting it changes shared tracking and does not create Amazon purchase attribution. Keep it pending tracking ownership and migration decisions.

The embedded Manage reviews and Go to Yotpo Reviews actions did not expose the detailed export interface in the current browser. Export completeness, review-request scheduling and current per-product published counts remain unverified. No export was fabricated or inferred from public reviews.

[Halfday Yotpo dashboard](https://admin.shopify.com/store/halfday-tonics/apps/yotpo-social-reviews). Earlier public evidence: Lemon had two reviews and a 4.5 rating on September 7; that is a dated sample, not the September 14 total.

## Local theme repair

`sections/Product-review-new.liquid` references `variant.price` without a local variant. The local change uses `product.selected_or_first_available_variant.price`. It retains the widget's product ID, URLs, currency, review content, loader and all existing styling. It adds no JavaScript and changes no purchase CTA or Product JSON-LD.

Theme Check: **122 errors / 385 warnings → 122 errors / 384 warnings**, no new offenses. The removed warning is the undefined variant. The widget value remains Shopify product metadata, not a verified Amazon offer.

This fix is **not deployed and not browser-verified against Shopify**. A new unpublished theme could not be created because the store is at its 20-theme limit. Pending Wave 1 theme `142755430600` and live `142757101768` were preserved. The next review must confirm the emitted price, review counts/ratings, star/anchor clicks, load/empty states and mobile/desktop visuals in an isolated theme.

## Bazaarvoice readiness

There is no verified Halfday Bazaarvoice workspace, staging deployment, contract/import approval or retailer match list in the available evidence. Do not install a guessed loader or treat Agentready's SEO work as Bazaarvoice onboarding.

The vendor's current authenticity policy permits a one-time authentic legacy import within the contract window, requires all approvable content regardless of rating, and prohibits ongoing imports under that legacy allowance. Preserve original review text, submission dates, authorship and contextual disclosures. Confirm the current Halfday contract and vendor import specification before preparing the actual upload. [Bazaarvoice authenticity policy](https://www.bazaarvoice.com/legal/authenticity-policy/).

Do not scrape Amazon or retailer reviews to fill the export. Do not import only five-star/published records without reconciling all source statuses with Bazaarvoice. Sampling, incentives and staff relationships need their original labels; changing product format does not automatically authorize sharing reviews across products.

## Import reconciliation specification

Prepare the vendor-approved full export in restricted storage, not this repository. Keep a separate non-PII summary by product/status/star score/locale. Required mapping review:

| Source information | Migration treatment |
| --- | --- |
| Original review ID and product ID | Immutable migration key and approved Bazaarvoice product mapping; prevent repeat imports |
| Title/body/rating/date/locale | Preserve original values, formatting meaning and date/timezone; no copy edits or sentiment filtering |
| Moderation/published state | Map explicitly; reconcile 724 collected vs 706 published against export scope and dates |
| Verified purchase, staff, sample, incentive and source | Preserve evidence and disclosures; do not manufacture verified-buyer status |
| Author/contact/origin data | Include only as vendor-approved and authorized; never put PII or authentication in Git |
| Media | Preserve authorized original links/rights; reconcile missing or inaccessible assets |
| Merchant responses | Confirm supported import mapping and preserve original context |
| Product identifiers | Shopify product/variant, SKU, GTIN, package quantity, formula and retailer IDs; keep standard/slim/case records distinct |

Acceptance requires source count = accepted + excluded-with-reason + unresolved for each scope. Compare rating distributions and per-product counts, not only a rounded global average. Export and destination counts may differ for legitimate moderation or locale reasons; each difference needs a record. Keep the original export unchanged for rollback.

## Onsite and retailer release sequence

1. Obtain the approved Bazaarvoice workspace, product-feed schema and staging deployment. Confirm Walmart/Target program eligibility, commercial scope and specific product matches separately.
2. Finalize the [catalog map](catalog-map.json), including consumer pack vs logistics case, GTIN and retailer ID. Do not normalize away leading GTIN zeros or assign a case barcode to a can. [Bazaarvoice catalog requirements](https://docs.bazaarvoice.com/articles/?_escaped_fragment_=ratings-reviews%2Fxml-schema-and-data-requirements).
3. Have the vendor validate the complete legacy dataset and unresolved records before consuming the one-time import opportunity. Record import job receipt and status reconciliation.
4. Install only the verified staging integration in a new unpublished theme. Keep Yotpo as the live provider until review. Assign one onsite rating-schema owner; check both source and rendered DOM for duplicate Product/aggregateRating data.
5. QA rated product, no-review product, mixed-rating product, changed formula/package, collection stars and protected staff pages. Check pagination/filtering, review text, keyboard/focus, anchor behavior, mobile layout, empty/error state and load size. Compare before/after transfer and LCP/CLS under the same conditions; a vendor switch is not automatically a performance win.
6. Coordinate review-request cutoff before activating the new request system. Determine which Shopify orders are staff/sample/wholesale; Amazon consumer purchases cannot be inferred from Shopify. Ensure old queued requests aren't unexpectedly released.
7. Publish only after approved onsite QA. Obtain separate Walmart and Target acceptance evidence on each agreed retailer product. Onsite visibility does not prove retailer syndication.
8. Remove Yotpo code/app only after export retention, migrated coverage, request cutover, retailer acceptance requirements and rollback window are approved. Restore the old provider if migration QA fails; do not keep both systems sending requests.

## Concrete vendor/owner questions

- Which Halfday Bazaarvoice workspace/contract and staging deployment should we use, and does it include legacy import plus both retailer destinations?
- What exact product/GTIN/retailer-ID list and review-family rules are approved for standard cans, slim cans, consumer packs and cases?
- Can the owner provide access to Yotpo's full export/request settings and approve any necessary reviewer-data transfer to Bazaarvoice?
- Who owns request timing/eligible order types and the cutoff for the old request queue?
- Is the Yotpo pixel intentionally disconnected, and should it stay that way during migration?

These are specific remaining gates. No message has been sent to the vendor or team.
