# Klaviyo account audit and isolated staging

September 14, 2026. Halfday account identity was confirmed after Dylan switched accounts. This replaces earlier login-blocked status. **No existing live flow, message, form, consent setting, audience or sending configuration was changed. No emails or signups were sent.**

Dylan asked to retain the existing welcome design and stop rebuilding it. The local email redesign is inactive. Future live changes are recommendations for review, not instructions to activate anything automatically.

## Account additions

| Object | ID / status | What changed |
| --- | --- | --- |
| Footer routing staging | [S4DvQh](https://www.klaviyo.com/forms/S4DvQh), Draft | Copied `TPsGns`, retained its design, changed the copy's submit destination from HelloFresh to Halfday Newsletter `XNd8tH`. Not published or embedded. |
| Unused welcome reference copy | [RpHH9D](https://www.klaviyo.com/flow/RpHH9D/edit), Draft | Created before the scope correction, then named `[Halfday W2 UNUSED] Welcome reference copy - DO NOT ACTIVATE`. Copied content retained; no replacement template assigned. |
| Unused standalone template | [QSSEVw](https://www.klaviyo.com/email-editor/QSSEVw/edit) | Imported Welcome 01 before the scope correction. Not connected to any message or campaign. No further redesign/imports planned. |

Footer destination persisted after leaving and reopening the editor, including the linked mobile button. Its form-list summary still displayed HelloFresh, so the saved editor value, not that summary, is the verification evidence. The clone automatically has its own hidden `Source` value, `[Halfday W2 STAGING] Footer routing only - DO NOT PUBLISH`. No new custom property was added. Prefer applying the reviewed destination-only correction to the original form later, preserving its source attribution. Publishing/replacing the clone requires explicit source and embed review.

The original footer remained **Live → HelloFresh Sample Campaign `TPaapC`** after staging. Linked desktop/mobile blocks share content within the cloned form; this does not imply editing the original form. [Klaviyo linked-block behavior](https://help.klaviyo.com/hc/en-us/articles/44513639011099).

## Verified findings and proposed changes

| Finding | Specific recommendation | Release dependency |
| --- | --- | --- |
| General footer `TPsGns` submits to HelloFresh instead of newsletter | Review the staged destination-only correction to `XNd8tH`; preserve the original design and Source. Do not move historical members. | Check list bridges and run one authorized signup before release. |
| Newsletter uses single opt-in; its “Unsubscribe from all email marketing” option is unchecked, while the account-wide equivalent is checked | Review whether this list exception is intentional; align it with the agreed unsubscribe behavior. Do not silently change opt-in mode. | Confirm intent, then test only with an approved identity. |
| Welcome `XruESR` excludes missing/other `rc_active_subscriber` cases unless its filter evaluates them as false | Test missing, Boolean false/true and string values; preserve current filter until the property owner and intended eligibility are known. | Native eligibility evidence; no bulk profile normalization. |
| Browse `RX4C7p` has no trigger filters and only Shopify checkout/order exclusions | Add a verified product-ID allowlist and independent consent/operational-profile exclusions in a future isolated draft. Keep Amazon purchase uncertainty explicit. | Approved product universe and verified property types; preview accepted/rejected cases. |
| Public Peach events include `Employee Shop` in Categories | Do not exclude that category wholesale: it would exclude valid consumer products. Separate product eligibility from staff/wholesale identity. | Establish the actual operational profile mapping; Faire order tags are not automatically profile properties. |
| Existing browse preview text says “Don't shy away from of a little fiber” | Proposed minimal correction: “Don't shy away from a little fiber”. Retain existing design. | Review with the eventual browse change packet; no existing message edited. |
| Welcome subject still offers 15% off; offer redemption has not been verified | Validate the offer, eligible Amazon destinations and existing attribution links before changing any wording or sending paths. | Team offer confirmation. No new discount or tracking IDs invented. |

List-specific unsubscribe settings can differ from account settings. Suppression/consent checks must account for the intended list scope, rather than assuming global suppression alone represents every opt-out. [Unsubscribe behavior](https://help.klaviyo.com/hc/en-us/articles/115005078267), [suppression behavior](https://help.klaviyo.com/hc/en-us/articles/115005246108).

## Live and draft baseline

- **Welcome `XruESR`: Live.** Trigger: Halfday Newsletter `XNd8tH`; no re-entry. AND filters: Placed Order zero over all time; Received Email zero over all time where Flow is legacy `XeYvCE`; `rc_active_subscriber is false`. First two messages observed Live. First subject: `Get 15% OFF Your New Favorite Iced Tea! 😎`; second: `3-5g of Sugar + Fiber = A Happy Gut 🍋☀️`. Two-day delay is noon in the recipient's local timezone; the next three-day/noon delay was visible, but its timezone was not separately inspected.
- **Legacy welcome `XeYvCE`: Manual.** Queue counts and list bridges remain unverified. Do not release or clear queues. The older draft `Yfzwx4` remains untouched.
- **Browse `RX4C7p`: Draft.** Viewed Product metric `Sk3snx`; re-entry after 30 days; no trigger filters; Checkout Started zero and Placed Order zero since entry. Two-hour delay. Email `TKuvBS` is Draft, subject `Go ahead - trust your gut. 🍋`; Smart Sending checked with 16-hour window; UTM tracking checked, custom parameters unchecked. No settings changed.
- **Newsletter `XNd8tH`: 14,985 members observed.** This is membership, not an approved campaign audience or deliverable recipient count.
- **Popup `XDLfXK`: Live**, submitting to Halfday Newsletter and SMS Subscribers. The alternate `WtiUL4` is Draft. No form timing, targeting, consent or design edited.

## Actual browse-event evidence

Read-only event detail panels for metric `Sk3snx` exposed these exact field names: `ProductID`, `Name`, `URL`, `ImageURL`, `Price`, `CompareAtPrice`, `Value`, `Brand`, `Categories`. Display values were verified; raw JSON types, native filter operand types and template bindings still need validation.

| Event | ProductID displayed | URL | Categories displayed |
| --- | --- | --- | --- |
| Fan Favorites | `8143536226504` | `https://drinkhalfday.com/products/fan-favorites` | Employee Shop; Menu - USE THIS ONE; Variety Packs |
| Peach Tea | `8143502573768` | `https://drinkhalfday.com/products/peach-tea` | Employee Shop; Iced Teas; Menu; Menu - USE THIS ONE; Shop All |

Both display Brand `Halfday Tonics`, Price `$35.99`, CompareAtPrice `$0.00`, Value `35.99`, and product-specific images on the storefront's `/cdn/shop/files/` path. These Shopify prices are not evidence of an Amazon offer. No recipient identities or tokenized preview URLs are included here.

Metric daily counts displayed September 8–14: **13, 7, 2, 4, 5, 0, 0**. These are captured events, not total visits. September 14 is partial; zero counts alone do not establish a tracking outage. Two event samples establish field names, not full catalog coverage or end-to-end rendering.

## Signup measurement baseline

Popup report `XDLfXK`, UI timeframe **Last 7 days**, read September 14:

- 17 submissions / 1,586 viewed users, displayed submit rate **1.07%**.
- 7 / 1,586 engaged with all steps, **0.44%**. This does not mean the other 10 failed email signup; the second step is a separate funnel step.
- Desktop: 904 views, 7 submissions, **0.77%**. Mobile: 680 views, 10 submissions, **1.47%**. Device rows account for 1,584 of 1,586 views; do not silently force totals to match.
- Report conversion metric is **Shopify Placed Order**, with $0 revenue. It cannot establish Amazon revenue or the commercial value of these signups.

Keep these counts as a baseline. Correct routing and settle the offer before a separate popup timing experiment. The sample is too small to declare a winning design or device strategy.

## Remaining review and testing

1. Confirm offer terms and destinations, intended newsletter unsubscribe scope, operational identity/property ownership and SMS ownership.
2. Read legacy/manual queue totals and list bridge definitions; validate native property types and allowed-product coverage without changing recipients.
3. Prepare minimal diffs using the existing creative. The unused welcome clone/template are not release candidates.
4. Use an approved test inbox for signup, consent, eligibility, inbox authentication and final tracked-link checks. None has been run in this pass. A dev theme does not isolate Klaviyo events or sending.
5. Review and authorize each live change separately. Keep all staged actions Draft. Manual is not a substitute for non-sending staging. [Flow statuses](https://help.klaviyo.com/hc/en-us/articles/360017706091).

No production changes are authorized by completion of this audit. No flow activation, audience backfill, suppression, real signup, email send, campaign schedule or theme publication occurred.
