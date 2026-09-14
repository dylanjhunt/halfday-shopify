# Wave 2 implementation outline

**September 14 scope update:** Existing welcome design stays; replacement creative below is historical and inactive. Halfday access is restored. A footer routing fix is staged separately, with no live changes. [Current audit and exact account additions](account-audit-and-staging-2026-09-14.md).

Original preparation record, September 10, 2026. Branch: `djh/wave-2-klaviyo-prep`. **Local preparation only; nothing imported, published, scheduled or sent in Klaviyo. No production theme or shared Shopify data changed.**

## Work completed in this branch

| Deliverable | Concrete result | Review location |
| --- | --- | --- |
| Three welcome emails | Day 0 welcome, day 2 flavor discovery, day 5 story; subject, preheader, readable body, primary and secondary CTAs | [Browser preview](preview/index.html), [copy source](content.json) |
| Browse reminder | Complete static fallback creative with the stray “from” wording eliminated; no cart, purchase, stock or numerical nutrition claims | [Preview](preview/browse-01.html) |
| Relaunch campaign | One unscheduled message for the proposed eligible audience | [Preview](preview/campaign-01.html) |
| Email source files | Five responsive HTML sources with native Klaviyo footer tags and five matching plain-text versions | `klaviyo/`, `plain-text/` |
| Signup copy | Footer, popup, success, error and double-opt-in alternative; no-offer version and conditional verified-offer copy | [Signup and offer](signup-and-offer.md) |
| Routing specification | Known form/list IDs, proposed footer destination and new source property, campaign preservation | [Signup and offer](signup-and-offer.md) |
| Eligibility and relaunch | Missing/false/true property cases; deduplication, staff/sample exclusions, product allowlist contract, two audience cohorts, cutover and rollback | [Eligibility and cutover](eligibility-and-cutover.md) |
| QA plan | Specific local, draft-only and controlled-live checks with explicit untested status | [QA checklist](qa.md) |

Email artwork has not been copied out of the account. The local templates are a text-first design option in Halfday green/yellow, with email-safe fallback fonts and no JavaScript, web fonts, tracking pixels or remote image dependencies. The text wordmark is a review treatment, not an approved replacement for the actual logo. Dylan subsequently requested preserving the existing welcome design instead of this replacement. Do not continue these imports or redesigns. Browser previews are not Outlook/Gmail/Apple Mail certification.

All draft discovery CTAs use public Halfday pages rather than silently recycling the all-Lemon discount link. That routing is a proposal requiring offer/destination review. Existing live links and tracking are untouched. These drafts are not proof of Amazon attribution.

## What cannot be completed in a Shopify dev theme

| Work | Why theme preview does not isolate it | Next safe step |
| --- | --- | --- |
| Native event binding and eligibility | Real field names verified, but display values do not prove native types or send eligibility | Validate profile/filter types and preview the retained design without sending |
| Actual form/list/source routing | Submissions update shared profiles, consent, lists and may trigger live flows | First inspect bridges and clone into Draft; later an explicitly approved test identity/window |
| Missing subscription property and staff/sample filters | Need real account properties, types and native eligibility evaluation | Redacted field mapping plus native previews; no bulk profile edits |
| HTML template compilation, unsubscribe/preferences and mailing address | Klaviyo renders tags and recipient-specific URLs | Native draft preview; actual link/action tests only with approved test identity |
| Delivery, SPF/DKIM/DMARC and inbox layout | Need a real delivered message; active sending-domain UI alone isn't proof | Authorized test inbox/send, then inspect received headers and clients |
| Amazon offer and attribution | Requires actual offer terms and approved tracking destinations | Confirm mechanism/ASINs; test redemption to the relevant stage without placing an order |
| Popup timing/audience experiment | Changes the shared production form and exposure | Review draft layout, then approve one isolated experiment and observation period |
| Campaign counts and suppression | Depend on current consent, activity and exclusion data | Read-only final cohort counts; no mass suppression |
| Form/flow activation or campaign send | Directly affects visitors/subscribers | Approve the finished release packet and controlled rollout |

Klaviyo can support non-sending draft templates and flows, but they still live in the production account. A full signup-to-inbox test cannot be certified solely from a dev theme. All local work here can be reviewed without that account access.

## Current evidence and blockers

- September 14, latest: account access restored and Halfday identity verified. Footer draft S4DvQh contains only the proposed destination change; live forms and flows remain untouched. Real browse fields, current consent settings and signup metrics were inspected. The initial login block is resolved. Wave 3's verified Faire order tags still require profile mapping. The complete package continues on `djh/wave-3-review-prep`; see the [combined handoff](../waves-2-3-progress-2026-09-14.md).
- September 10: opening Klaviyo showed another authorized client account. Switching through its account menu to **Halfday (`V2taSu`)** led to a fresh login screen. No Halfday settings were refreshed or changed. All account IDs/settings in this package remain explicitly sourced to the September 7 audit.
- September 10: public Shop All and Our Story destinations loaded; public collection still presents Amazon purchase links and the footer still promises up to 15% off. That does not verify a working signup offer. [Shop All](https://drinkhalfday.com/collections/shop-all), [Our Story](https://drinkhalfday.com/pages/our-story).
- Confirm the Amazon offer or approve the no-offer option. Existing questions about Postscript and campaign ownership remain pending; no duplicate request has been sent.
- Before sending anything, name a test inbox and authorize the test signup/delivery. No real profiles or sends were created.
- Wave 1 PR #2 was still open when checked during this preparation. Main remains live; the existing dev theme belongs to that pending release. No theme push was needed for this email work.

## Next execution order

1. Finish native eligibility, queue and list-bridge checks using the refreshed account evidence.
2. Retain the existing welcome design, resolve the offer and consent intent, and review the isolated footer draft.
3. Run native template and event/profile previews; review final routing/filter/link diff.
4. Run approved test signup and inbox checks; release signup/welcome, then browse, then the campaign with separate gates.

The overall Wave 2 estimate remains 8–12 hours of hands-on work. This package completes the local copy/specification portion; account verification, staging, inbox QA and approved activation remain. Waiting for answers and observing results are separate from hands-on time.

## Rebuild and preview

Run `python3 scripts/build-wave-2-preview.py` from the repo, then open `docs/wave-2/preview/index.html` locally. Optional local server: `python3 -m http.server 8766 --bind 127.0.0.1 --directory docs/wave-2`, then `http://127.0.0.1:8766/preview/`.

`docs/**` and `scripts/**` are already excluded by `.shopifyignore`. No theme runtime files or dependencies were added. Do not attach the inactive replacement templates to live messages. Future changes must preserve the existing welcome design and receive separate release review.
