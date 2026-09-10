# Eligibility, dynamic content and release plan

September 10, 2026. These are implementation specifications. No segments, properties, triggers or queues have been changed.

## Welcome eligibility

Audited flow `XruESR`: added to `XNd8tH`, no re-entry, Placed Order zero over all time AND no email from legacy welcome `XeYvCE` AND Boolean `rc_active_subscriber` false. Preserve these production filters until their business purpose and evaluation are tested.

| Profile case | Proposed outcome | Evidence needed before applying |
| --- | --- | --- |
| Newly consented newsletter subscriber; explicitly false subscription property; no exclusions | One welcome journey | Native list entry and consent confirmed; no bridge or duplicate flow |
| Subscription property missing | Evaluate explicitly; don't equate missing with false | Preview profile against current filters; establish property owner. If absence simply means ordinary consumer, separately approve `(false OR not set)` |
| Subscription property Boolean true | Remains excluded | Current subscription ownership, not an assumption of Amazon subscription |
| String `"false"`, blank or unexpected property type | Hold for evaluation | Do not cast or rewrite historical properties globally |
| Previously received `XeYvCE` | Retain legacy exclusion | No surprise re-welcome; migration is a separate approved policy |
| Already received new welcome | No repeat | Verify no-re-entry plus legacy/manual overlaps |
| Staff/sample/wholesale identity | Exclude from consumer welcome/browse/campaign | Actual profile tags/list/property mapping from the account; public form use does not override identity |
| Suppressed, unsubscribed or unconfirmed double opt-in | No marketing send | Native channel eligibility and consent process |
| Shopify Placed Order exists | Preserve current exclusion for now | Determine whether order is consumer or operational; not an Amazon purchase proxy |
| Historical HelloFresh member | Leave in original journey | No import or backfill to trigger a welcome |

Use native profile filters for rules that must remain true before each message. Trigger filters are evaluated on entry, while profile filters are evaluated again before actions. Do not introduce an “email received zero from this flow” profile filter on a three-message flow, which could disqualify a recipient after email 1. [Klaviyo filter behavior](https://help.klaviyo.com/hc/en-us/articles/115002779051).

## Browse reminder `RX4C7p`

Keep the existing two-hour delay, 30-day re-entry and 16-hour Smart Sending as initial settings. Recheck them in the account before editing. Keep Checkout Started zero and Placed Order zero since entry as the audited baseline, while recognizing these only represent captured Shopify events.

Add explicit email marketing eligibility and operational-profile exclusions. Product eligibility must be an allowlist of verified public consumer product IDs from actual Viewed Product event data. Do not use Shopify inventory availability as Amazon availability. Do not use only a blacklist for staff/sample handles, a URL containing `/products/`, or public accessibility as catalog approval.

### Event mapping contract

No real event was available in this turn because login blocked the account recheck. None of the following field names are invented Klaviyo variables. Capture the exact keys/types in the account preview before implementing dynamic tags:

| Semantic value | Required validation | Failure behavior |
| --- | --- | --- |
| Viewed product identity | Actual event product ID matches approved public allowlist | Do not enter/send the reminder |
| Product page URL | HTTPS, exact `drinkhalfday.com` host, approved product path; no private tokens | Use static collection fallback only for an otherwise eligible product |
| Product title | Nonempty approved public display name | Omit product card; use static fallback |
| Image | HTTPS approved Shopify CDN asset, correct product; explicit dimensions/alt | Omit image; keep readable copy and CTA |
| Amazon destination | Approved matching ASIN and tracking destination | Use verified public product page, not a guessed retailer URL |
| Consent / identity / recency | Verified profile and platform event timestamp | Ineligible/unknown profile or stale event is not a generic-send fallback |

The local browse email is a complete static creative fallback. It contains no dynamic fields and does not certify event mapping. The dynamic version remains blocked until an actual eligible event can be previewed. Staff/sample or unknown products must fail eligibility, even when generic creative could render. When title/URL is available for an eligible product, proposed card copy is **Take another look at [VERIFIED PRODUCT TITLE]**, CTA **View this flavor**, with the validated public product URL. Omit prices, inventory claims and nutrition figures.

If product approval is revoked during the two-hour delay, the entry-time allowlist alone will not stop a queued message. Add a supported send-time check if available; otherwise pause the draft/live reminder and resolve affected waiting recipients before a catalog change. Do not promise send-time catalog validation until tested.

## Campaign audience specification

Prepare two disjoint review cohorts; don't create membership by an email-open signal alone:

1. **Recently engaged:** can receive email marketing AND explicit subscribed consent AND approved consumer identity AND at least one verified email click in the last 60 days. Exclude known automated/security-scanner clicks where the account exposes that evidence. A click alone is not proof of a purchase.
2. **New subscribers:** same consent/identity rules AND signup within 30 days AND known approved general source AND not in cohort 1. Hold recipients currently in welcome, or who received marketing within 48 hours, out of the first campaign so it doesn't collide with onboarding.

Apply the welcome/recent-send exclusions to both cohorts at send time. Use actual current account fields/events to implement these rules and record counts for eligible, excluded, overlapping and final unique recipients. Counts are **not available**, not zero. These 60-day/30-day/48-hour windows are proposed conservative launch settings, not measured winners.

Exclude suppression, missing consent, known staff/sample/wholesale and unresolved source/identity records. Do not assume every historical newsletter/HelloFresh member is marketable. The existing sunset segment `YA5dwU` is not an instruction to suppress 26,960 profiles. A future inactivity review should require a recent delivered opportunity to engage and account for recent consent; do not delete or bulk suppress in this wave.

## Controlled cutover, once authorized

1. Recheck live account, filters, forms, list consent settings and all older manual queues; preserve templates, settings, links, IDs and counts in a private rollback record. Do not export customer records into Git.
2. Stage **new standalone templates and cloned flows with every action Draft**. Avoid editing a shared template referenced by a live message. Draft creative and native previews can be tested without sending; they do not prove actual signup or delivery. Manual is not an isolated sandbox because recipients can queue. [Klaviyo status behavior](https://help.klaviyo.com/hc/en-us/articles/360017706091).
3. Resolve source/list bridges before changing footer routing. Preview exact eligible/ineligible profile cases; authorize one test inbox and test actions separately. A dev theme does not isolate the installed Klaviyo integration or list events.
4. Review one release packet: chosen offer option, HTML/text, exact destination/attribution list, source mapping, consent settings, profile/product filters, audience counts, statuses, queued-recipient treatment and scheduled time. No automatic approval from finishing local QA.
5. Prefer updating the canonical welcome through the platform's verified draft/version workflow if available. If a clone is needed, route only the new approved form submissions to its verified new-source cohort and exclude those from the old flow atomically in a controlled window. Document how already-waiting old recipients finish. If a supported overlap-free cutover cannot be demonstrated, pause new acquisition entry for the agreed window and test it; do not activate two overlapping welcomes or guess at pending-recipient behavior.
6. Activate approved signup/welcome changes first. Observe controlled test consent/list/source and exactly one welcome. Then activate the browse reminder only after event mapping passes. Start the campaign only after audience approval and suppression/queue counts have been refreshed.
7. Rollback: pause the newly activated path first, restore the recorded original form route/offer and canonical message version, verify one intended path, and review waiting recipients without bulk release or deletion. Never reactivate old and new welcome paths together blindly.

## Reporting and stop conditions

Record a same-length pre-release baseline and first 24-hour/72-hour/7-day windows, with date range, denominators and device split: form views/submissions, eligible flow entries/skips by reason, delivered messages, unique human-like clicks, bounces, complaints and unsubscribes. Keep email clicks, retailer outbound clicks and confirmed retailer purchases separate.

Pause rollout immediately for duplicate welcome sends, staff/sample leakage, wrong offer/ASIN, broken preference/unsubscribe or consent routing. Review any complaint in the initial controlled cohort before expansion; compare bounce and unsubscribe rates with the account baseline and its current deliverability alerts. Don't set a claim of success from tiny samples or automate suppression from opens alone. No recurring monitor or campaign is scheduled by this document.
