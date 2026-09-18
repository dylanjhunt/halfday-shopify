# Wave 3 operations audit

September 14, 2026. Read-only Shopify/app UI. No orders, inventory, listings, integration settings, consent or permissions changed. No test order was sent. Account notices describing updates/defaults were observed, not actions performed during this audit.

## Confirmed route and configuration

Faire is already connected. Its overview shows 12 products published, inventory and order sync on, pricing/content sync off. The overview's **Fulfillment OFF** summary is misleading: the detailed Orders settings select **Faire to Shopify only**. Treat the selected detailed setting as the authoritative configuration. Shopify's app-information page also displayed “0 active” under channel connections; that label does not override the functioning embedded account and its settings.

| Setting | Current observed value | Implication |
| --- | --- | --- |
| Inventory direction | Shopify → Faire | Do not assume Cin7 writes this Shopify inventory until that route is traced |
| Inventory location | Founders Market & Co., location `62666473672`; 1 of 2 locations selected | Do not add the other location or sum all locations during a resync |
| Orders | Accepted Faire orders → Shopify | Preserve original channel order key and deduplication |
| Imported payment status | Paid | A Shopify paid badge is not proof of a Faire payout or a new Shopify charge |
| Order naming | Faire order number | Useful cross-system correlation key |
| Tags | `Faire`, `Wholesale` | Concrete operational exclusions to evaluate in Klaviyo; don't assume order tags automatically become profile properties |
| Commission/processing fee | Notes | Do not introduce fee line items or change accounting presentation |
| Cancellations | Neither direction | A cancellation in one system is not automatically propagated by this connector |
| Fulfillment | Faire → Shopify only | ShipStation-origin Shopify tracking is not configured to flow back through this connector |
| Tester/sample deduction | Unchecked | Intentional policy or gap needs the operations owner; don't enable automatically |
| Product matching | Automatic by SKU enabled | Existing manual aliases must survive; don't rebuild mappings from string equality |
| New catalog imports | Draft | Preserve this review step |
| Selling-method default | Sell individually; each Shopify listing represents a single item | Default only; per-product overrides may exist. A sellable item may itself be a pack, so confirm quantities before calling this an error |
| Pricing/content sync | Off | No general catalog overwrite during this cleanup |
| Performance sharing | On | Existing app setting, untouched |

Sources: [Faire preferences](https://admin.shopify.com/store/halfday-tonics/apps/faire-sell-wholesale/preferences), [detailed order settings](https://admin.shopify.com/store/halfday-tonics/apps/faire-sell-wholesale/preferences/orders), [selling methods](https://admin.shopify.com/store/halfday-tonics/apps/faire-sell-wholesale/preferences/selling-methods), [product linking](https://admin.shopify.com/store/halfday-tonics/apps/faire-sell-wholesale/products).

## Existing-order trace

One existing Faire order, `#YHFKAPJ7NH`, was inspected in Shopify. It has two fulfilled groups. Its August 28 timeline records ShipStation marking two items fulfilled from Founders Market & Co. twice, consistent with those two groups. Products include Classic Half & Half, Peach, Raspberry and Sweet Tea. No customer details are included here.

This establishes **Faire → Shopify order presence** and **ShipStation → Shopify fulfillment updates** for that historical order. Two fulfillment groups are not evidence of duplicate shipping. The trace does **not** establish who sent the order into ShipStation, Cin7's participation, physical 3PL shipment correctness, stock deductions, current ongoing sync health or whether tracking reached Faire. Those require the matching record in the other systems.

## Catalog findings

The [catalog map](catalog-map.json) records all 12 linked Faire products and both sides' SKUs. Each Shopify product's ID, barcode and shipping fields were also read directly in its admin page. All 12 GTINs pass checksum validation; the worksheet retains their exact text. That is identifier-format validation, not approved package mapping. Two aliases differ:

| Product | Faire SKU | Shopify SKU |
| --- | --- | --- |
| Classic Half & Half (Slim Can) | `CLASSICHALFHALF_SLIM_12PKCASE` | `REF-HIT12PK` |
| Peach Tea (Slim Can) | `PEACHTEA_SLIM_12PKCASE` | `REF-PIT12PK` |

These are existing explicit matches, not proven errors. Removing them to “clean up” SKU names could break linking.

Faire flags five unlinked listings:

1. Cranberry Black Tea 12-Pack. Keep pending the already-requested discontinued-product decision.
2. Green Tea with Honey & Ginseng 12-Pack. Compare with the already linked Green listing before linking or republishing.
3. Lemon Black Tea 12-Pack. Verify formula, package and GTIN against current Lemon. Similar flavor name is insufficient.
4. Peach Green Tea 12-Pack. Compare with existing standard Peach; do not automatically link to slim can.
5. Raspberry Iced Tea 12-Pack. Compare with the already linked Raspberry entry; preserve legacy order references.

Do not automatically choose “Not sold on Shopify,” relink, delete or publish these five. They may be retired or historical duplicates, but account evidence does not settle that decision.

Peach Slim Can's Shopify product `8335577710792` currently has SKU `REF-PIT12PK`, barcode `10850064555230`, `sample-only`, physical-product weight **0.0 lb**, and the default **Seeding Kit** package. Inventory showed 81 available at Founders Market & Co. and zero at the other location at inspection time. These are Shopify units, not cans or Amazon availability.

The broader check found **all four slim-can records and Watermelon at 0.0 lb**. The other seven linked records show 10.0 lb. **All 12 use the store-default Seeding Kit package (12 × 6 × 4 in, 0 lb)**. This is a concrete data-consistency question, not proof of bad shipping labels: Cin7, ShipStation or the 3PL may override Shopify weight/package values. Ask which system is authoritative and request approved packed weights/dimensions before changing anything. The map links every source product for review. No weights, quantities or identifiers were inferred or changed.

## Access and remaining evidence

| System | Evidence now | Needed to finish |
| --- | --- | --- |
| Cin7 Core | Shopify launch repeats existing-organization gate | Access to the already connected organization, Shopify/ShipStation integration settings, job history and matching order; do not reconnect |
| ShipStation | Shopify launch requests expanded customer/product/order/gift-card permissions | Existing account read access or owner-reviewed permission update; no scope expansion accepted |
| Faire | Account connected; detailed settings and linked products readable | Corresponding fulfilled/cancelled records on Faire, ownership decision for tracking/cancellation direction and five legacy products |
| TikTok / AfterShip / Amazon | TikTok channel installed; AfterShip and Bazaarvoice not in inspected installed-app pages | Exact AfterShip product/account, TikTok shipping mode, Amazon MCF/FBA configuration and a matching historical order; external setup may exist |
| Shopify | Two active locations; published main `142757101768` | 3PL owner confirms location role, unit of measure and order-source exclusions |

## Proposed corrections, held for review

1. If Shopify/ShipStation is the shipping-status authority, evaluate **Shopify → Faire** fulfillment return with the owner. Check existing direct writers first; don't turn on both directions as a default. Use a historical partial-fulfillment record and a controlled future test to prove carrier/tracking mapping.
2. Agree cancellation ownership and warehouse cutoffs before enabling propagation. Cancelling in Shopify must not be assumed to recall an already-released 3PL shipment.
3. Reconcile the five unlinked products against GTIN, package, formula and recent order history. Preserve the two slim-can aliases.
4. Confirm whether sample inventory should deduct, and correct the zero-weight/default-package mapping only from approved logistics data.
5. Trace the existing Cin7 route before any reconnect, inventory push or backfill.

## Route acceptance tests

For each channel, record source order ID, connector job ID, receiving order ID, source SKU, mapped SKU, ordered sellable quantity, units per sellable, location, inventory before/after, fulfillment ID, carrier/status/tracking and last sync timestamps. Keep PII in the appropriate operational system, not Git.

| Case | Expected evidence |
| --- | --- |
| Ordinary order | One accepted source order creates one intended downstream order; no second competing importer |
| Case/pack order | Warehouse units match approved quantity conversion; no 12× or 24× inflation |
| Partial fulfillment | Each group returns once, with correct items and tracking; remaining items stay open |
| Retry/replay | Same source key updates the existing record rather than another order or shipment |
| Cancellation before/after warehouse release | Correct downstream status and documented cutoff/manual exception |
| Return | Approved destination and disposition; stock only returns when policy and receipt permit |
| Staff/sample | Intended restricted route; not reclassified as Amazon consumer stock or sent consumer marketing |
| TikTok order fulfilled by Amazon | Correct shipping mode, connector SKU/ASIN and fulfillment acknowledgement; tracking accepted by TikTok; no additional 3PL shipment |

Vendor references checked September 14: [Cin7 Shopify processing modes](https://help.core.cin7.com/hc/en-us/articles/11796986460431-Download-orders-from-Shopify), [Cin7 ShipStation models](https://help.core.cin7.com/hc/en-us/articles/9034569837839-ShipStation-Integration), [Faire inventory deduction conditions](https://www.faire.com/support/articles/37632468706331), [AfterShip MCF integration](https://support.aftership.com/en/feed/articles/15325912-amazon-multi-channel-fulfillment-mcf-integration), [Amazon TikTok MCF shipping modes](https://supplychain.amazon.com/learn/amazon-mcf-for-tiktok-shop). Supported vendor behavior is not confirmation of Halfday's configuration.
