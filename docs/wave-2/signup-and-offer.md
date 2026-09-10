# Signup and offer specification

September 10, 2026. Proposed copy and settings, not saved to Klaviyo or Shopify.

## Current journey and intended change

| Entry | September 7 evidence | Proposed release |
| --- | --- | --- |
| General footer `TPsGns` | HelloFresh Sample Campaign `TPaapC` | New general signups join Halfday Newsletter `XNd8tH`, after preserving the list's consent process and checking for bridge automations |
| Main popup `XDLfXK` | Live, 2-second delay, all devices/all visitors, email then optional SMS; success displays `NEWERA15` | Align offer with welcome; propose 8-second delay as a test candidate; target eligible visitors who are not already subscribed; preserve campaign exclusions and 5-day dismissal cooldown |
| Alternate popup `WtiUL4` | Custom-trigger only, no views in audited period | Retain until its caller and campaign owner are established; no assumed duplicate removal |
| HelloFresh, Subscribe and other campaign forms | Separate campaign journeys | Keep separate; no historical list migration or surprise welcome sends |
| Newsletter welcome `XruESR` | Three live messages | Refresh together with signup wording and destinations after isolated draft/inbox QA |

The popup delay is a proposed first experiment, not a proven improvement. Don't change timing, audience and design together if the objective is to identify which improves signup rate. First fix the routing/offer defect; then compare timing with the same eligible audience and copy. Keep mobile and desktop reporting separate. Do not add theme JavaScript to replicate Klaviyo behavior.

## Option A: email news, no discount promise

This is the complete copy used in the local preview. It still needs approval before replacing the existing offer.

| Surface | Proposed copy |
| --- | --- |
| Footer heading | Make time for tea. |
| Footer description | Get flavor news and more from Halfday in your inbox. |
| Footer button | Sign me up |
| Popup heading | Your next tea break starts here. |
| Popup description | Get flavor news and more from Halfday in your inbox. |
| Field label / placeholder | Email address / Your email address |
| Popup button | Keep me in the loop |
| Email-step disclosure | By signing up, you agree to receive marketing emails from Halfday. You can unsubscribe at any time. Privacy policy. |
| Success | Thanks for joining us. Take a look at the flavors while you wait for your first email. |
| Success CTA | Explore the flavors → `https://drinkhalfday.com/collections/shop-all` |
| Invalid email | Please enter a valid email address. |
| Submission failure | That didn't go through. Please try again. |

Link Privacy policy to the existing store policy. Preserve verified double/single opt-in settings, current required consent controls and suppression handling. If double opt-in is enabled, success becomes: **Check your inbox to confirm your signup. Once you're confirmed, we'll send you more from Halfday.** Never show success until the platform confirms the relevant submission result. The preview is only the email step; it does not remove or alter the live SMS step.

## Option B: confirmed Amazon offer

Do not paste this option into a sending template until each bracketed field is supplied and tested. `NEWERA15` is observed copy, not a validated redeemable offer.

- Heading: **A little extra for your first tea break.**
- Description: **Sign up for Halfday emails and get [APPROVED SAVINGS] on [ELIGIBLE AMAZON PRODUCTS].**
- Button: **Send me the details**
- Success: **You're in. Here's how to use your offer: [VERIFIED REDEMPTION STEPS].**
- Welcome 1 subject: **Welcome to Halfday. Here's your [APPROVED SAVINGS] offer.**
- Welcome 1 insert: **Thanks for joining us. Get [APPROVED SAVINGS] on [ELIGIBLE AMAZON PRODUCTS]. [VERIFIED REDEMPTION STEPS]. [EXPIRY AND MATERIAL LIMITS].**
- Welcome 1 CTA: **Use your offer on Amazon** → `[VERIFIED AMAZON DESTINATION WITH EXISTING APPROVED ATTRIBUTION]`.
- Welcome 2/3: only repeat a still-valid offer; no invented countdown, expiry or scarcity. Use the no-offer body otherwise.

Required evidence: owner, promotion type (code, coupon, Subscribe & Save or another mechanism), exact amount/up-to wording, eligible ASINs/pack sizes, eligibility restrictions, expiry/timezone if any, destination and redemption steps. Never describe recurring Subscribe & Save terms as a general first-order code. The storefront currently also advertises Subscribe & Save; that does not establish that the signup promotion is the same offer.

## Source properties and consent

Proposed new field: `halfday_signup_source_v2`, string with values `footer` or `popup`. Attach to the respective submit action after confirming supported form behavior. Treat it as most recent form source, not immutable first-touch attribution. Retain native source/consent history. Do not replace existing `$source`, original acquisition metadata or past campaign properties.

Do not infer `consumer=true` merely from submitting a public form. Existing staff, sample, wholesale and subscription identities must still be excluded as specified in the eligibility plan. No bulk property writes or historical reclassification in this wave.

## Link and offer release gates

Local drafts intentionally route discovery to public Shopify pages, where shoppers select their own Amazon product. This is a proposed change from the audited all-Lemon discount CTA and needs review. It is not evidence that direct Amazon attribution is preserved.

Before release, inventory every existing image and text link per email, including its UTM/maas parameters. Keep a private exact-link rollback record; exclude recipient-specific preview tokens from Git. Preserve approved attribution on retained Amazon URLs. If new destinations need different Amazon tracking links, obtain them from the offer owner instead of fabricating identifiers. Configure Klaviyo message UTMs once and inspect the rendered URL to avoid duplicate parameters. GA/Ads/GTM setup remains out of scope.

Sources: [September 7 focused audit](../focused-audit-2026-09-07.md), [current public collection and footer](https://drinkhalfday.com/collections/shop-all) checked September 10. Account recheck is blocked by fresh Klaviyo login.
