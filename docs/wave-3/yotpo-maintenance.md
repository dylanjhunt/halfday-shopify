# Retain Yotpo: current work and QA

September 14, 2026. Dylan confirmed to leave Yotpo in place and not add Caffine Functions. Provider replacement, review migration and request-system cutover are inactive. The [earlier migration packet](reviews-migration-plan.md) is retained only as historical research. The client's original Walmart/Target syndication request remains separately deferred; keeping the onsite widget does not establish retailer distribution.

## Completed read-only checks

The account baseline from the earlier September 14 inspection remains 724 collected reviews, 706 published, 4.81 average and 9,610 requests sent for All time. It was not refreshed in this pass. The disconnected Customer Events Pixel notice remains an account-level follow-up; no reconnect was attempted.

This pass checked the **published storefront at 1280 × 720**. The browser initially inherited the pending Wave 1 development preview; Exit preview was used before the results below were recorded. These are current production observations, not validation of the unpublished price repair.

| Product | Rendered summary | Readable review rows in the initial page | Other checks |
| --- | --- | --- | --- |
| [Lemon Tea](https://drinkhalfday.com/products/lemon-tea) | 4.5 / 2 ratings shown as reviews | 1 | Header rating link scrolls to review content; desktop panel visually inspected |
| [Peach Tea](https://drinkhalfday.com/products/peach-tea) | 4.8 / 57 | 5 | Next Page changes 1 → 2; Previous returns 2 → 1. Write a Review opens score/title/body/name/email fields; nothing entered or submitted |
| [Watermelon Half & Half](https://drinkhalfday.com/products/watermelon-half-half) | 4.8 / 56 | 5 | Correct Shopify product ID attached to widget; review rows render |
| [Strawberry Half & Half Slim Can](https://drinkhalfday.com/products/strawberry-half-half-slim-can) | No published rating in the header; Reviews fallback | 0 | Fallback reaches `#Reviews` about 110px below viewport top; first-review prompt visually inspected |

All four samples have no horizontal document overflow at the tested desktop width. The visible header and review-section summaries agree on the three rated products. The no-review widget contains decorative stars and a first-review invitation, while the product header correctly uses the Reviews fallback instead of a fabricated rating. No mobile, full keyboard, tracking, submission or whole-store regression pass is claimed here.

[Machine-readable check record](../../reports/yotpo-retained-provider-2026-09-14.json).

Lemon's aggregate count of two and one readable text review are not automatically a missing-review defect. The other record may be rating-only or governed by account display settings. One additional DOM row was a hidden vendor template and was excluded from the count. Verify the actual product records in Yotpo before adjusting counts or display rules; do not unhide vendor template markup.

## Confirmed repair pending preview

All four published widgets emit an empty `data-price` while retaining the correct product ID and USD currency. The source refers to an undefined `variant`. The existing development-branch change in `sections/Product-review-new.liquid` uses `product.selected_or_first_available_variant.price` and leaves the widget IDs, markup, loader, styles and purchase links intact.

The prior Theme Check comparison removed exactly that undefined-object warning, adding no findings. Shopify CLI rechecked the theme list in this pass: live theme `142757101768`, pending Wave 1 development theme `142755430600`, and 19 unpublished themes remain. No new preview slot is available under the previously returned 20-theme limit. No theme was overwritten or removed. The repair still needs rendered-price and visual/interaction checks in an approved isolated preview before merging to main.

## Remaining maintenance work

1. Preview the price fix on a rated product and the zero-review product, at desktop/mobile widths; confirm rating links, pagination, form opening and empty state. Do not submit a review during this check.
2. With account access, reconcile Lemon's rating/text-review count and inspect current product grouping/IDs. Do not repurpose another flavor's reviews or rewrite the source data.
3. Confirm current request eligibility against Shopify's staff/sample/wholesale orders. Public consumer purchases go to Amazon, so a Shopify order is not evidence of a consumer purchase. Do not change invitation rules or release queued requests during the audit.
4. Confirm ownership and purpose of the disconnected Customer Events Pixel before any shared tracking change. It does not provide Amazon purchase attribution.
5. Existing theme CSS hides review dates and footer controls (`assets/custom.css` around lines 795–808). Consider restoring useful date/context visibility in a separately previewed change; do not broadly unhide vendor controls without checking their purpose, layout and keyboard behavior.

No migration export, Bazaarvoice workspace or new review app is required to finish this retained-provider maintenance. Those have been removed from the active completion gates. Klaviyo, fulfillment access and approved logistics facts remain the separate blockers in the [combined handoff](../waves-2-3-progress-2026-09-14.md).
