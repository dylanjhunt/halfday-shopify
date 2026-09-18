# Wave 2 QA and acceptance

**Updated September 14:** existing welcome design retained. [Account evidence](account-audit-and-staging-2026-09-14.md) and [staging manifest](staging-manifest.json) supersede earlier access status. Original local checks below date to September 10.

A local browser pass proves layout only. It does not prove Klaviyo rendering, inbox delivery, consent routing or attribution.

## Local checks

| Check | Status / evidence |
| --- | --- |
| Generate five HTML sources, five previews and five matching plain-text drafts | Passed: `python3 scripts/build-wave-2-preview.py` |
| No JavaScript, tracking pixels, remote image/font dependencies or live submit actions | Passed: inspected all 10 HTML files and five plain-text versions |
| Required footer tags in import sources; explicit inert footer in previews | Passed: inspected all 10 HTML files and five plain-text versions |
| Responsive review at 390px and 1280px; no horizontal clipping | Passed: all five emails visually inspected at 390px and 1280px; page width matched viewport. Signup preview also checked at both widths. Primary links measure 50px high after button refinement. |
| Every message primary/secondary destination matches copy source | Passed: inspected all 10 HTML files and five plain-text versions |
| No unverified numeric nutrition/discount claims in generated creative | Passed: inspected all 10 HTML files and five plain-text versions |
| Theme/app production files untouched | Passed: only `docs/**` and `scripts/build-wave-2-preview.py` changed; main remains `2893a6f`; no Shopify CLI push |

## Account and draft-only checks, no sends

| Test | Expected result | Current status |
| --- | --- | --- |
| Confirm account identity and original IDs | Halfday; named form/list/flow settings match or differences recorded | Passed September 14: Halfday account, exact original IDs rechecked |
| Standalone template import/native preview | Historical redesign check, no longer an active deliverable | Redesign stopped. One unused standalone template imported; no full native/inbox certification |
| Existing artwork | Correct brand assets, good alt text, explicit dimensions; body/CTA remain useful with images blocked | Existing design retained; no redesign work planned |
| Welcome timing/filter preview | Day 0, day 2/day 5 noon as audited; actual timezone recorded; missing/false/true/string cases reviewed | Current filters and two-day recipient-local noon verified; native property cases and second timezone still pending |
| Draft browse event preview | One verified public product event; exact ID/title/URL/image mapping; staff/sample/unknown product rejected | Two real event panels inspected; exact fields verified. Native binding and rejection cases pending |
| Missing image/title/URL | Eligible product renders static fallback; no empty links or fabricated product | Contract prepared; native preview pending |
| Shared template/flow dependencies | Editing new draft cannot alter live messages; every cloned action Draft, no queued recipients | One unused flow clone is Draft; standalone template unassigned. Footer route persisted in isolated Draft; no sends |
| Legacy and list bridge inventory | Exactly one intended welcome route; older manual queues preserved | Legacy XeYvCE remains Manual; queue totals and bridges still unverified |
| Audience logic/counts | Consented consumers only; no overlap or inferred Amazon orders; counts recorded with timestamp | Definitions prepared; counts unavailable |

## Controlled live-account tests requiring an approved identity/window

1. New general footer signup: correct consent flow, source property and newsletter list; one welcome entry; no HelloFresh spillover. If double opt-in is enabled, unconfirmed signup sends no marketing message.
2. Existing subscriber repeats signup: no duplicate welcome, no unexpected consent/source destruction. Don't test this on a real customer.
3. Suppressed/unsubscribed, legacy welcome recipient, staff/sample/wholesale and subscription true cases: expected exclusions using test identities or native profile previews. No bulk mutation to create test fixtures.
4. Approved subscriber visits a verified consumer product: event payload correct, two-hour delay/re-entry/Smart Sending apply; operational product event cannot send the reminder. A generic fallback must not bypass eligibility.
5. Received email: correct sender/reply-to, subject/preheader, authentication alignment and mailing address; Gmail/Apple Mail/Outlook as available; desktop/mobile/dark mode/images off; all links work and preferences/unsubscribe affect only the approved test profile.
6. Attribution links: correct final page/ASIN and approved preserved parameters after Klaviyo tracking redirect. No claim of Amazon order tracking unless independently verified.
7. Welcome/browse/campaign collision: no duplicate welcome, expected Smart Sending and recent-send exclusions; existing manual queues not released.
8. Rollback rehearsal: exact original version/settings available; designated new path can be paused; no automatic release of queued recipients or simultaneous old/new welcome activation.

None of these controlled tests have been run. Browsing the public site as an anonymous visitor or rendering local HTML is not a substitute.

## Release record to complete

Record approved copy option, template/flow/form IDs, list/source diff, exact filter expressions and property types, product allowlist IDs, timing/timezone, consent mode, audience counts, exact approved URL/attribution mapping, test evidence, queue treatment, activation timestamp/owner and rollback IDs. Keep PII, credentials and recipient preview links out of Git.

Klaviyo reference for native organization/unsubscribe/preference tags and case-sensitive event fields: [Message personalization reference](https://help.klaviyo.com/hc/en-us/articles/4408802648731). The local builder only substitutes visible preview footer labels; it is not a template-language validator.
