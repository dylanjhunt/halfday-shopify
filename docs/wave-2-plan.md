# Wave 2: Klaviyo cleanup and relaunch

Prepared September 10, 2026. Estimated hands-on work remains **8–12 hours**, excluding client responses, offer/account access, and time observing a relaunch. This plan uses the September 7 account audit; recheck the named forms/flows before editing because the account may have changed.

The outcome is one clear signup-to-welcome journey, one appropriate browse-interest reminder, and a defined audience for a controlled email relaunch. Preserve the existing sending domain and useful brand assets.

## 1. Fix signup routing and align the offer

- Recheck footer form `TPsGns`, currently audited as submitting to HelloFresh Sample Campaign `TPaapC`, against newsletter list `XNd8tH` and welcome flow `XruESR`. Inspect any bridge before proposing a routing change.
- Prepare new general-footer signups for Halfday Newsletter with an explicit source property. Keep campaign-specific forms separate. Do not move historic HelloFresh members into a live welcome journey.
- Reconcile the 15% promise across footer, main popup `XDLfXK`, success message and all three welcome emails. The audited popup says `NEWERA15`, while the email discount links point to Lemon ASIN `B0B4F5NJB6`. Confirm the actual Amazon redemption mechanism, eligible products and approved destination before promising a discount.
- Prepare a non-discount copy alternative if the offer cannot be substantiated. Do not create a Shopify discount for an Amazon purchase journey.
- Review popup audience/timing and desktop presentation. The alternate popup `WtiUL4` was custom-trigger only, not a proven automatic duplicate. Preserve SMS settings until Postscript/Klaviyo ownership is confirmed.

Deliverables: current routing map, before/after setting specification, approved offer wording and destinations, mobile/desktop form preview. Save app changes as drafts where supported; an app editor is not isolated by a Shopify development theme.

## 2. Refresh welcome and browse messages

- Use the existing three-email welcome series `XruESR` as the starting point. Preserve the working version before edits. Clarify the benefit and buying CTA using real email text/buttons alongside existing artwork.
- Check the legacy A-Game welcome exclusion and `rc_active_subscriber` missing/false/true cases. Preserve intentional deduplication and distinguish consumer, staff/sample and wholesale eligibility.
- Review each Amazon link and any existing attribution parameters. Shopify order history does not establish Amazon purchase history.
- Prepare the draft browse flow `RX4C7p`: correct “Don't shy away from of a little fiber,” verify its two-hour delay/30-day re-entry/Smart Sending configuration, and add public-product eligibility with a safe dynamic-content fallback.
- Render the browse message from an actual eligible Viewed Product event. Exclude staff/sample records. Position it as a browse-interest reminder, not Amazon cart or purchase recovery.
- Keep older manual queues, Shopify order/replenishment flows and historical recipients untouched.

Deliverables: three reviewed welcome messages, one draft browse message, an eligibility matrix, event-backed dynamic-content previews and a documented activation diff. Do not introduce disputed nutrition claims while the team confirms them.

## 3. Validate the audience and prepare a controlled relaunch

- Recheck the active branded sending domain `send.drinkhalfday.com`; it was already configured. Do not rebuild DNS without a demonstrated issue and confirmed owners.
- Define current consented new-subscriber/engaged audiences with relevant source and staff/sample exclusions. The audited 26,960-member sunset segment did not require a recent opportunity to engage, so it is not a bulk-suppression instruction.
- With an explicitly approved test inbox, verify one signup through consent, list/source assignment and exactly one expected welcome entry. Inspect delivered authentication, mobile/image-blocked rendering, links, preferences and unsubscribe behavior.
- Record the exact messages, audience, offer and settings to activate. Obtain release approval before publishing forms, enabling messages, sending a campaign or releasing queued recipients.
- Define the initial reporting baseline: form submit rate by device, eligible flow entries, delivered messages, bounces, complaints, unsubscribes and clicks. Separate Amazon outbound intent from confirmed retailer sales.

Deliverables: audience definitions/counts, QA results, a concrete activation checklist and rollback notes. Do not promise a conversion lift or choose a winner from the small historical samples.

## Inputs needed before the relevant steps

1. **Offer owner:** is there a current Amazon 15% offer, how is it redeemed, which ASINs qualify, and is Lemon the intended destination for every welcome email? If not, approve the proposed non-discount alternative.
2. **SMS/campaign ownership:** Dylan is already confirming Postscript and the status of HelloFresh/Subscribe. Do not repeat those questions until a concrete dependency needs the answer.
3. **Controlled testing:** identify an approved test inbox and explicitly authorize test signup/email delivery before generating real profile or send events.
4. **Activation:** review the finished offer, messages, audience and settings together before publishing or sending.

Work that can start without those answers: read-only inventory refresh, mapping current routing/eligibility, evaluating existing creative, drafting both offer variants, and preparing the QA matrix. No live Klaviyo configuration or sending was changed during this preparation.

## Scope and branch workflow

- GA and Google Ads remain deferred. GTM remains excluded. Search Console is a separate SEO dependency.
- Fulfillment routing and Bazaarvoice/Yotpo migration remain Wave 3.
- Keep accessiBe and the health articles as instructed.
- Use `djh/wave-2-klaviyo-prep` for preparation. Rebase onto the final Wave 1 main release before theme implementation. Use Shopify CLI and a verified development/unpublished theme; never push main without release authorization.
- PR #2 owns the current unpublished development-theme state. Do not overwrite it from this preparation branch.

References: [Wave 1 handoff](wave-1-handoff-2026-09-10.md), [Klaviyo audit](klaviyo-audit-2026-09-07.md), [focused audit](focused-audit-2026-09-07.md), [overall roadmap](modernization-roadmap.md).
