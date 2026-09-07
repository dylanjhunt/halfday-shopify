# Halfday — Klaviyo account audit

Read-only inspection on September 7, 2026 after Dylan received account access. Account shown: **Halfday**. No form, flow, audience, campaign, consent, integration, or sending settings were changed. No emails were sent and no profiles were subscribed/exported. GA and Google Ads remain deferred. GTM was confirmed unused by Dylan and is excluded from further work.

## Main recommendation

**Correct the footer form's audience destination before expanding lifecycle sending.** The live theme embeds form `TPsGns`; its [Klaviyo report](https://www.klaviyo.com/forms/TPsGns/reports/overview) identifies its destination as **HelloFresh Sample Campaign**. The one live welcome flow triggers on **Halfday Newsletter**. That mismatch can prevent normal footer subscribers from receiving the intended welcome journey unless another automation moves them between lists; no such bridge was verified.

The existing account is not an empty rebuild. Shopify sync is enabled, five forms are live, and a three-email welcome flow is live and already links to Amazon. Retain useful assets, clean the routing/filter logic, and relaunch selected flows only after event and audience tests.

## Inventory

All three pages of the [Flows list](https://www.klaviyo.com/flows) were inspected: **42 total, 1 Live, 4 Manual, 37 Draft**. Row-level inventory is in `reports/klaviyo-flow-inventory.json`. Flow-level status can conceal message-specific settings; message status was inspected in the active welcome flow, not all 42 flows.

| Status | Flow | Trigger / issue |
| --- | --- | --- |
| Live | [FE] Welcome Series (`XruESR`) | Added to Halfday Newsletter; three live emails |
| Manual | 1. [A-Game] - Welcome Series (`XeYvCE`) | Same newsletter list; legacy welcome path |
| Manual | Browse Abandonment - Standard (`Sm78pv`) | Viewed Product |
| Manual | Hub- Customer Winback (`Ubn55r`) | Placed Order |
| Manual | Post-Purchase Followup - Order Count Split (`UW9f7s`) | Placed Order |
| Draft | [FE] Browse Abandonment (`RX4C7p`) | Viewed Product; recently updated in the UI |
| Draft | [FE] Abandoned Cart (`TpipgU`) | Checkout Started |
| Draft | [FE] Post Purchase (Order Fulfilled) (`QZA7Hn`) | Fulfilled Order |
| Draft | [FE] Post-Purchase (Placed Order) (`SijWa7`) | Placed Order |
| Draft | [FE] Customer Winback Series (`YpSaRv`) | Placed Order |
| Draft | [FE] Replenishment (Repeat Trigger) (`XGT2nM`) | Due to Reorder (Repeat), an integration-specific dependency to verify |
| Draft | [FE] Replenishment Reminder (`RGQSDU`) | Placed Order |
| Draft | [FE] Sunset Flow (`SAX2ty`) | Added to [FE] Eligible for Sunset Flow list |
| Draft | Two incomplete shells (`QZ2YC3`, `RU9JVq`) | Trigger not set up |

There are numerous older A-Game, Hans, Hub, BFCM, test, clone, and duplicate welcome/cart/post-purchase flows. Establish one owner and canonical flow per purpose. Manual flows warrant a check for queued profiles; do not switch them to Live or release recipients as a cleanup shortcut. Retain historical assets until their content and dependency value is assessed.

All two pages of signup forms were inspected: **16 forms, 5 Live, 11 Draft**. The live forms are:

| Form | ID | Next check |
| --- | --- | --- |
| Multi-step email - New Site | `XDLfXK` | Targeting, A/B variants, destination list, offer |
| Multi-step email - New Site - No Image | `WtiUL4` | Targeting overlap with the other popup |
| Halfday LP Subscribe | `XLuRNz` | Current landing-page purpose and list routing |
| Halfday New Site - Footer | `TPsGns` | Confirmed HelloFresh destination mismatch |
| Halfday LP Form | `Xc2KrW` | Current campaign use and list routing |

Footer report, **last 7 days**: 688 views, 5 submits, 0.73% submit rate, and $0 in the selected Placed Order revenue report. These are a small recent sample; they do not prove no Amazon sales occurred. The form is live and showed a January 29, 2025 publish date. Do not treat form-list totals from an unspecified window as equivalent to this report.

## Shopify integration: present and configured

The [Shopify integration](https://www.klaviyo.com/integration/shopify) shows:

- Enabled for `halfday-tonics.myshopify.com`; added April 14, 2021.
- App embed enabled; **Add Viewed Product tracking** checked; **Track behavioral events** checked.
- **Sync Shopify email subscribers to Klaviyo** checked, destination **Halfday Newsletter**.
- Shopify text-message subscriber sync unchecked. Postscript is separately listed as Enabled; determine the intended SMS owner before enabling another sync or messaging stream.
- Shopify Markets sync unchecked. The optional “Enable Shopify access” control is also unchecked; its description concerns Shopify surfaces interacting with Klaviyo data and does not mean the ecommerce integration is disabled.
- Historical orders, customers, and products marked synced.
- Checkout Started, Placed Order, Ordered Product, and Fulfilled Order most recent events all displayed **3 days ago**, with zero events today. Compare this with actual expected Shopify activity before diagnosing a sync problem; the public storefront primarily sends shoppers to Amazon.

The integrations list also shows Meta Ads, Postscript, and Klaviyo MCP Server as Enabled. No settings or credentials were opened/changed for those apps. No automatic Amazon purchase feed was established in this audit.

The separate Shopify-admin launch of Klaviyo requested broader app data access. Direct account access works without accepting that prompt; leave the pending update for the account owner's review if a future feature needs it.

## Live welcome flow: what already works and what needs review

[FE] Welcome Series (`XruESR`) triggers when added to **Halfday Newsletter** (`XNd8tH`), with **No re-entry** selected. Observed profile filters are all joined with AND:

1. Placed Order zero times over all time.
2. Received Email zero times over all time where Flow equals the old **1. [A-Game] - Welcome Series** (`XeYvCE`).
3. Profile property **`rc_active_subscriber` is false** (Boolean).

The last two are legacy dependencies to validate. Test profiles with the property missing, false, and true; do not assume a missing property behaves like false. Confirm whether `rc_active_subscriber` is still maintained by the current subscription stack. The Shopify order exclusion can also exclude staff/sample/wholesale customers, while it cannot be assumed to know Amazon purchasing history. The old-flow exclusion may be intentional deduplication; preserve it until the migration policy is clear.

The flow contains three live emails:

| Timing | Message | Observations |
| --- | --- | --- |
| Day 0 | [JB] Welcome Series, Email #1 - Welcome to A New Era of Iced Tea | Subject promises 15% off; Save 15% links to Amazon ASIN `B0B4F5NJB6`; other links go to Shop All / Why Halfday |
| Day 2, 12 PM | [JB] Welcome Series, Email #2 - Why Halfday | “Save 15% on Amazon” link goes to the same ASIN; educational links remain onsite |
| Day 5, 12 PM | [JB] Welcome Series, Email #3 - Meet Our Founders | Live status/timing verified; full message content not inspected |

For the first two messages, UTM tracking is enabled and Smart Sending is unchecked. Sender is Halfday / `hey@drinkhalfday.com`. Previews show `utm_source=Klaviyo`, `utm_medium=flow`, campaign names, and Amazon `maas` parameters. This is existing link tagging, not proof of attribution accuracy or discount eligibility. Validate the real offer, attribution-account ownership, and whether sending all new subscribers to the Lemon ASIN is intentional. Do not copy recipient-specific preview tokens into reusable links.

Last-30-days UI metrics: email 1 shows 44% open rate (40) and 12.1% click rate (11); email 2 shows 32.6% open rate (30) and 1.1% click rate (1). Neither showed a Placed Order result in the inspected panel. These small aggregates establish reported engagement, not a reliable test winner or an Amazon conversion measure; mail privacy and bot activity can affect engagement metrics.

## Recommended relaunch sequence

1. **Resolve form → list → flow routing.** Confirm the general footer belongs in Halfday Newsletter, record any intentional HelloFresh campaign segmentation, and prepare the corrected form settings. Test a controlled consented signup and confirm the profile/list/source and expected single welcome entry before publishing changes.
2. **Define source properties and exclusions.** Separate homepage popup, footer, HelloFresh/other landing campaigns, organic acquisition, staff/sample, wholesale, and any supported SMS source. Distinguish flow-organizing tags from profile properties and actual trigger/list membership. Test the legacy subscription Boolean and old-flow exclusion rather than removing them blindly.
3. **Validate the live welcome offer and all three emails.** Confirm the Amazon offer and destinations, mobile/image-blocked readability, accessible image alternatives, preference/unsubscribe behavior, sender-domain authentication, and message filters. Preserve a record of the working version before changing it.
4. **Choose one browse-interest flow.** The existing FE draft can be assessed first. Verify identifiable Viewed Product events, public-product exclusions, recent-message frequency, and Amazon/retailer destinations. Do not interpret an outbound click as a completed purchase.
5. **Separate commerce from retail-interest journeys.** Shopify cart, post-purchase, and replenishment flows are useful only for the channels whose events are actually supplied. Confirm staff/sample exclusions and the Repeat event producer. Do not activate every old DTC flow for an Amazon-led storefront.
6. **Review manual queues and overlapping forms/flows.** Decide whether to retain or retire legacy variants after content review. Avoid backfilling old lists into live messages without a consent/eligibility plan.
7. **Finish deliverability and event QA.** Review sender-domain authentication, suppression, complaint/bounce rates, form consent behavior, event delivery/deduplication, and app permissions as needed. No test send, profile submission, or domain/DNS verification was performed in this audit.

This is an implementation-ready findings list, not authorization to activate flows or change audiences. Keep current sending stable while a focused first change is prepared and tested.
