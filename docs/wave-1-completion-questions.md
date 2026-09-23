# Wave 1: completion status and decisions

Updated September 9, 2026. Dylan merged PR #1 at main `2893a6f`. The new contrast and brand-only Agentready changes are on `djh/wave-1-contrast-agentready` and CLI development theme **142755430600**. No new production release was performed in this follow-up.

## Dylan's decisions and updated scope

- Products already exist. Do not recreate them or change public assortment/access automatically. The remaining task is correcting confirmed content and deciding on any specifically requested new merchandising. See [the exact fact list for Leslie](product-facts-for-leslie.md).
- Signifyd, Postscript, expired campaigns and Cranberry: Dylan will confirm.
- accessiBe: **keep**. Health articles: **leave unchanged**. These are no longer open approval questions or Wave 1 completion blockers.
- Dark-green contrast treatment: **approved and implemented in development**, including yellow-panel headings, primary/mobile-card buttons, footer embedded-form button and footer link hover. Desktop/mobile checks and 15-route regression passed; other merchant settings and attributed Amazon links are preserved. No new JavaScript.
- Search Console: Dylan will request access. Do not consolidate article URLs before that evidence arrives.
- Agentready: deployed Apply fix verified with a durable 34/34 receipt; accurate brand/policy output prepared in development. Product output and JSON-LD remain off. Contact-field UI mismatch is reported separately.
- Peach display-title typo: **completed with Dylan's explicit approval** on September 9. Saved `Peach Tea (Slim Can)` in the Product Title metafield and verified it after an admin reload. No other product fields were changed.

The original numbered questions below are retained to match Dylan's numbered reply. Items 5, 8 and 9 are resolved by the decisions above; 1 is narrowed to preserving existing setup and confirming only specific merchandising changes.

## Completed without further input

- Replaced the homepage benefits accordion's mouse-only div controls with native details/summary. Enter, Space and pointer operation work, the first answer starts open, and the browser keeps one answer open per section. Removed the old accordion click handler and obsolete fragment special case. Existing copy, section settings, CTA and desktop row geometry are preserved. Older browsers without named-detail grouping can still open/close each answer independently.
- Restored the theme's disabled keyboard focus indicators. The accordion uses a title outline that avoids its existing overlapping answer spacing. No layout dimensions or normal resting colors were changed.
- Replaced separate desktop/mobile benefits images with one lazy responsive picture, preserving both artworks and the existing frames. Added a single-image fallback and appropriately sized decorative icons. The optional video branch now uses the existing visibility-aware video component rather than autoplay markup. No new JavaScript dependency.
- Verified 15 live/development routes, preserved attributed Amazon destinations and tracking loaders, ran the motion lifecycle and JavaScript syntax checks, and read back all four changed files through Shopify CLI. Theme Check has **122 inherited errors / 385 warnings**, three fewer warnings and zero added findings. Desktop 1280px and mobile 390px visual/keyboard samples passed without horizontal overflow. No new speed improvement is claimed from this pass.
- Confirmed all 455 files in the fresh live snapshot still match main `bb0169f`.
- Rechecked the installed app menu: 23 apps. Signifyd opens a separate account login. Postscript and accessiBe still have storefront integrations but are not named in that menu. No app was removed based on menu absence.
- Recorded Shopify's last-30-days field baseline: **LCP P75 1,292ms; INP P75 96ms; CLS P75 0.01**. This window mostly predates our release and cannot measure its effect yet.
- Imported [seven native URL redirects](../reports/wave-1-legacy-redirects.csv) after browser access recovered. Shopify confirmed seven additions, and anonymous HTTP checks verified all seven return **301** to the intended destination with **200** destination responses. The old shop/malformed URLs now reach Shop All or home; four old FAQ paths reach the current FAQ anchors. These shared store repairs are live independently of the development theme. Source articles were not changed. [Redirect verification](../reports/wave-1-legacy-redirects-after.json).

[Theme verification](../reports/wave-1-final-follow-up-verification.json) · [15-route comparison](../reports/wave-1-final-follow-up-regression.json) · [App/field observations](../reports/wave-1-owner-dependencies-2026-09-09.json) · [Redirect 404 evidence](../reports/wave-1-legacy-redirects-before.json)

## Questions for Dylan / Leslie

| # | Specific question | What the answer unlocks |
| --- | --- | --- |
| 1 | Which **4-pack and slim-can flavors/SKUs** should be public now, and which are Target-only, Amazon, or both? Identify the consumer pack for each and the intended retailer link; flag records that must remain staff/sample/logistics-only. | Public merchandising, format navigation, collection placement and the correct buying CTA without exposing internal cases. |
| 2 | Where is the **approved product fact sheet and final imagery**, and who can resolve the Strawberry slim-can conflicts: **45 versus 40 calories**, **green + black tea versus black tea**, and caffeine per can? Include can size, cans per consumer pack, SKU/GTIN, ingredients, sugar and fiber by format. A folder or sheet link is enough. | Consistent product pages, comparison tables, FAQ answers, alt text and structured content. Existing conflicting site copy cannot decide which facts are correct. |
| 3 | Who owns **Signifyd**, and can they provide account access or a vendor-confirmed decision on whether public Amazon-directed browsing still needs its device script? | Supported script scoping or retirement. Its login is separate from Shopify, and we must preserve any required Shopify order coverage. The owner question is drafted below. |
| 4 | Is **Postscript still the active SMS platform**, or should Klaviyo own SMS going forward? Who can confirm existing opt-in forms, automations and consent handoffs? | Remove redundant capture/loading only after ownership is clear. This is an app-cleanup decision; sending/relaunch stays Wave 2. |
| 5 | Should **accessiBe remain**, or should we retire the overlay and maintain accessibility directly in the theme? Is there an existing owner or service commitment we need to preserve? | A concrete keep/remove decision for the hardcoded storefront loader and Accessibility link. No replacement overlay is proposed. |
| 6 | Are **HelloFresh and Subscribe** still active campaigns? Their configured giveaway ended March 31, 2025. If retired, is **Shop All** the desired destination, or is a current newsletter landing page replacing them? | Retire or replace expired content, then fix the remaining campaign H1/description and source-page cleanup intentionally. |
| 7 | Is **Cranberry permanently discontinued**? If so, may its four old article links use a discontinued-flavor note and point readers to **Shop All**, rather than suggesting a different flavor is Cranberry? | Resolve the remaining product-specific broken destination without misleading visitors. |
| 8 | Who should approve the older **health/nutrition content**, especially the [ulcerative-colitis article](https://drinkhalfday.com/blogs/news/ulcerative-colitis-and-gut-health) and [tooth-extraction article](https://drinkhalfday.com/blogs/news/when-can-i-drink-soda-after-tooth-extraction-1)? Should those posts be retained for rewrite or retired? | A documented editorial decision on condition-specific advice and outdated product claims. Theme repairs do not validate those claims. |
| 9 | Can we use the existing **dark green** for orange-on-yellow headings and low-contrast button/footer text where needed, retaining orange as an accent? Or does the brand require a different approved contrast treatment? | The broader contrast pass changes the visual system, beyond the already released announcement fix and current focus-ring repair. |
| 10 | Can we get **Search Console** access to choose which overlapping kombucha/green-tea-shot articles to retain, or should those URL consolidations be deferred beyond Wave 1? | Evidence-based consolidation. Recommendation until data is available: keep the existing URLs and do not guess which has the strongest traffic/backlinks. This does not reopen GA, Ads or GTM. |

**Agentready:** Apply is now verified. Brand-only Agent JSON is prepared in development, with the live embed still off. Remaining work is catalog/JSON-LD/channel verification and the reported contact-field UI inconsistency. [Latest app report](agentready-product-feedback.md).

## App-owner request, ready to forward

“Our public shopping journey sends customers to Amazon, while Shopify retains separate staff/sample paths. Does the current Signifyd configuration require device collection on public discovery pages? If it can be scoped, please provide the supported setting or implementation and how we retain required Shopify-order coverage. We measured repeated CPU cost from imgs.signifyd.com and cdn-scripts.signifyd.com, so we want to review its scope before removing any code.”

Signifyd documents use of browsing/device behavior in its protection products; no supported Shopify-specific route-scoping setting was verified in this audit. [Signifyd account protection](https://www.signifyd.com/account-protection/). Shopify also notes that app code can need separate cleanup after uninstall; an absent app menu entry does not establish an inactive storefront integration. [Shopify uninstall guidance](https://help.shopify.com/en/manual/apps/uninstalling-apps).

## Scope disposition

Stockist and Locksmith have active storefront functions. Keep Yotpo until Bazaarvoice's replacement/import is verified in Wave 3. Keep operations apps until the route ownership work in Wave 3. Klaviyo offer/signup/flow activation is Wave 2; GA and Ads remain deferred and GTM excluded. No customer, order, subscription or campaign state was changed in this pass.

The extra theme changes are ready in development. Wave 1 is not entirely complete while catalog facts, the outstanding campaign/app decisions and Agentready catalog checks remain outstanding. Historical progress entries retain their original wording; this status and the current roadmap supersede older blockers that have already been repaired.

PR #1 is merged. New follow-up work uses `djh/wave-1-contrast-agentready` based on that merged main.
