# Agentready setup and SEO/AEO follow-up

**Current status, September 9:** no-return/custom policy controls and saved-plan recovery are improved. The saved 34-change Apply still fails with `unsupported_field`; Dylan is working on it. A controlled development-only Agent JSON test passed sampled product/staff exclusions with catalog paused and no approved handles, using homepage output as a positive control. Both output switches and both theme embeds are restored off. The curated app-served discovery index is regenerated and public, with the correct retailer description and no catalog records. Approved product output, JSON-LD, MCP/ACP and post-sync description precedence still need verification. See [current feedback and evidence](agentready-product-feedback.md) and [release record](wave-1-release-2026-09-09.md).

## September 8 setup history

The entries below retain the original observations. Their defect status is superseded by the September 9 recheck above.

September 8, 2026. **Core trial active; safe configuration completed manually; full activation blocked by verified app defects.** The reviewed Concierge Apply failed twice. Brand settings and scoped content settings subsequently saved through the individual screens. The production theme was not changed. Agentready’s shared settings and curated app-served discovery index were updated. The app embed was tested only in development, then disabled after it emitted protected staff collection data. Both app render switches are now off.

**Urgent remaining issue:** a staff product’s public app markdown URL still returns details even with both render switches off, the live embed off, Include Products unchecked and all 45 selectable product rows explicitly hidden. A final anonymous response at 12:08 UTC had `Age: 0`, so the finding was not simply an old browser preview. The available configuration has not resolved this. Agentready needs an endpoint-level exclusion/shutdown fix before full activation. No customer/order data was encountered.

[Product/UX issue report](agentready-product-feedback.md) · [Implementation verification](../reports/agentready-implementation-verification.json)

## Current implementation

| Area | Saved / verified result | Remaining limit |
| --- | --- | --- |
| Brand | Halfday Iced Tea, sourced description/tagline, existing logo, support email/contact link, three social profiles, US market and business understanding | Generated Agent JSON retained a different Shopify description while JSON-LD used the saved description. |
| Organization | Generic Organization selected; local storefront, private address and phone not exposed | Test output added a shipping service to IN and US; India’s source is unexplained. |
| Policies | Saved no-return summary with Terms Section 21 URL in the text; shipping URL/summary directs buyers to retailer estimates; returns schema off; shipping estimates unconfirmed | Returns override rejects the valid Terms URL based on policy-type validation. Numeric window cannot express no returns; 0 retained with return output disabled. Privacy/Terms native-policy fields miss existing custom pages. |
| Page types | Our Story → AboutPage; Hellofresh, Popup testing and PTO → Hidden from AI. Contact and FAQ auto-detected | Normal settings list 12 published pages and 26 unpublished exclusions, unlike Concierge’s 25 proposals. FAQ body is in theme sections and was not extracted. |
| Agents guide wizard | Four public tea collections and eight public flavors, accurate retailer/policy guidance, sizing marked not applicable | Generated template still includes generic Shopify checkout instructions and truncated policy summaries. It was not pasted/published. |
| App LLMs index | Generated and verified; All Rights Reserved; 11 utility/staff collections and 22 pages excluded; products and blogs disabled; all 45 selectable products also hidden explicitly | Index exclusions do not close the direct product endpoint. Saved description override ignored. Locator summary included script text, so that page was excluded from this index; native guide retains the locator link. |
| Shopify discovery guide | Added a curated `templates/agents.md.liquid` through CLI to dev theme 142755430600. It supplies public product/collection links, retailer buying context, support, full policy links and dynamic Shopify discovery endpoints | Development only. Served correctly at all three root discovery paths. It is a maintained theme file, not an automatically refreshed Agentready export. |
| Theme embed | Added through CLI, inspected, then disabled. No app data blocks remain on the checked dev home, Sweet Tea or protected staff collection | Do not activate until AR-00, policy, channel and schema conflicts are resolved. |
| Sync/audit | App reported a full-sync time of September 8, 7:54:31 AM after settings saves. A fresh audit completed at 80/B with 16 findings: 4 critical, 2 high, 7 medium, 3 low | A sync timestamp and readiness score do not prove every product output exists or is safe. Several new findings are the intentionally disabled outputs. |
| Regression checks | 15 live/dev routes passed Amazon URL/attribution, loader, Klaviyo ID, markup and protected-code checks. Merchant settings match baseline apart from the new disabled embed | Existing functional/visual QA limits from Wave 1 still apply; no new shopper JavaScript was added. |
| Theme Check | 122 errors / 404 warnings, inherited counts unchanged | Six false-positive UndefinedObject warnings for Shopify’s documented `agents` object are scoped out in this one file with an explanatory comment; emitted endpoints were verified. |

## Remaining work in order

1. **Agentready app fix:** apply one visibility policy to direct markdown, JSON, MCP, indexes and theme output; invalidate caches and verify anonymous protected requests fail. Output-off needs an actual public endpoint shutdown path.
2. **Agentready data fixes:** accept a return-policy section within Terms; support no-return categories; resolve unexplained shipping regions, description precedence, empty FAQ extraction and short/full discovery-file differences. See reproducible issues and acceptance recommendations in the product report.
3. **Retest on development:** public flavor, variety and slim-can pages; protected product/collection paths; policy accuracy; matching Organization IDs; no conflicting Shopify price/availability for Amazon purchases. Preserve existing theme schema until replacement output is proven.
4. **Finish store SEO content:** confirm consumer packs/slim-can facts, improve public product descriptions/meta and consistent taxonomy, resolve legacy campaign/blog content. Internal merchandise findings should not dictate consumer search work.
5. **Release separately:** review the dev guide and FAQ additions, then publish only the approved exact theme diff. Do not publish the full Wave 1 theme as part of app activation. GA/Ads remain deferred and GTM excluded.

## Earlier preparation snapshot (superseded by implementation above)

The following saved review and baseline findings describe the state before the user started the Core trial. They remain evidence, not the current billing or activation status.

## Saved Agentready setup review

- **Seven brand decisions:** approve Halfday Iced Tea, support email and the three verified social profiles. Replace the AI tagline with “Classic iced tea flavors with prebiotic fiber.” Replace the generated About text with a concise description of Halfday and its Amazon/retailer buying routes, excluding unsupported claims about artificial aftertaste and blanket nutrition values.
- **Two policy decisions:** change the return source from the empty native refund URL to `/pages/terms-of-service` and retain the damaged/incorrect-order exception. Change the shipping source to `/pages/faq` and use seller-specific delivery guidance instead of universal checkout/free-Prime claims. These are saved proposals, not published policy changes.
- **Return-field limitation:** clearing the app's numeric return-window field still displays “0-day window.” The editor exposes no “returns not permitted” category. Before enabling generated markup, verify that this becomes `MerchantReturnNotPermitted`, not an inaccurate finite window. If it cannot represent the policy faithfully, keep that structured output disabled and use the policy link/summary through a supported alternative.
- **25 page decisions:** Contact → ContactPage; FAQ → FAQPage; Our Story → AboutPage; Find In Store and Privacy Policy → WebPage. Select “Hidden from AI (promo)” for 15 URLs verified to return 404 and five campaign/test/redirect URLs. This is app discovery classification, not page deletion, Shopify unpublication or access control. [Per-page evidence](../reports/agentready-page-decisions.json).
- The review explicitly states that nothing has been written yet. The Core trial step is the current gate. No paid AI batches or product-copy mutations were run.

## Authenticated audit: what still needs work

Agentready reports **80/B**, setup **0/4**, storefront **not configured**. The full checklist has **21 items** (3 critical, 3 high, 11 medium, 4 low). It reports a 25-product readiness sample but a 46-active-product optimization scan, so denominators must not be combined. The score is not evidence that Agentready markup is live.

| Priority | Verified finding | Concrete next action |
| --- | --- | --- |
| P1 | Publishing/configuration gated by billing; embed off and no full sync recorded | Approve the chosen plan, apply the reviewed decisions, configure remaining fields, inspect generated output in development, then verify delivery. |
| P1 | No-return policy editor retains a numeric 0-day window | Verify the generated return category before delivery. Do not publish finite-window/free-return claims. |
| P1 | Catalog scope includes merchandise, staff items, free samples and logistics records | Exclude inappropriate items from public agent output using supported app controls. Do not change staff prices, inventory or publication merely to improve the score. |
| P1 | Eight product records lack a meta-description override | Watermelon Half & Half is the clear public flavor priority; four slim-can records require channel/fact review; three 24-pack logistics records should not be promoted as consumer packs. A missing override is not always missing rendered metadata: Strawberry already has a storefront fallback from its body. |
| P2 | App flags 20 duplicate “Variety 12-Pack” titles | Expanded list consists of merchandise/logistics items, including polo, hats, shirts, pins, stickers, a balance board and an 8 Case Shipper. This is copied internal metadata, not 20 public variety-pack SEO pages. Separate internal cleanup from consumer search priorities. |
| P2 | 23/25 descriptions counted thin; broader scan flags 45/46 | Compare product body with visible template/metafield copy first. Reconcile customer-facing facts into a consistent source without padding every item to satisfy a word-count threshold. |
| P2 | 5/25 missing taxonomy; 7/25 missing images; generic category/color/material advice | Review exact public beverage records after filtering merchandise. Choose the actual beverage taxonomy and relevant attributes. Do not invent material/color for tea or make zero-priced staff gear sellable. |
| P2 | Missing brand logo, policy links/summaries, contact and social fields | Reviewed identity/policy proposals cover most of these after application; add the verified store logo and privacy/terms references in Settings once unlocked. |
| P2 | Storewide shipping times/regions not confirmed | Preserve seller-specific delivery guidance. Do not assert a single Halfday shipping rate/window for Amazon-directed consumer pages. |
| P2 | Live homepage scan flags 45 unlabeled controls, 7 alt-text gaps and 23 images without dimensions | Recheck individual elements against the dev improvements already completed. Preserve empty alt text on decorative media; do not add labels indiscriminately or confuse live/development audits. |
| P3 | Standard storefront events not detected by a homepage heuristic | Informational finding, not proof that analytics is broken. Earlier network checks verified Klaviyo/Postscript transport. GA/Ads are deferred and GTM excluded. No event shim was added. |

Additional product SEO overrides flagged: Sweet Tea title shared by three records, Tropical Tea title/description shared by two records, five missing title overrides and one short description. Map duplicates to actual public routes before editing. A product-name fallback can be valid. “Catalog requirements failing” includes internal apparel and samples; it is not proof that all Halfday beverages are excluded from Shopify Catalog.

### Storefront verification result

Agentready's check finds two JSON-LD blocks on the homepage (Organization/WebSite) and two on Sweet Tea (Organization/Product), all HTTP 200. Despite a green “Verified live” heading, the explanatory text says **none of the schema found is Agentready's**. Treat this as proof of pre-existing theme schema, not completed Agentready activation. Its “custom discovery template” labels also do not establish Agentready ownership: direct public reads show Shopify commerce instructions. Re-observe actual response content after activation.

## Facts ready for onboarding

| Field | Grounded value / treatment | Source |
| --- | --- | --- |
| Brand | Halfday; storefront name Halfday Iced Tea | [Storefront](https://drinkhalfday.com/) |
| Legal entity | Halfday Tonics Inc. | [Terms, Overview](https://drinkhalfday.com/pages/terms-of-service) |
| Description | Halfday makes prebiotic iced teas in classic flavors, available through Amazon and retail stores. | Storefront shopping links and product copy |
| Website | `https://drinkhalfday.com` | Storefront canonical identity |
| Customer support | `hey@drinkhalfday.com`; contact page `/pages/contact` | [Contact](https://drinkhalfday.com/pages/contact) |
| Wholesale | `orders@drinkhalfday.com` | [FAQ, Company](https://drinkhalfday.com/pages/faq) |
| Social profiles | Instagram and TikTok `drinkhalfday`; X `https://twitter.com/drinkhalfday` | Storefront footer |
| Return policy URL | `https://drinkhalfday.com/pages/terms-of-service`, Section 21 | Published terms, updated February 24, 2025 |
| Return terms | Product returns and exchanges are not accepted. Damaged-in-transit or incorrect orders should be reported immediately to support. Warranty applies to direct Halfday or authorized-retailer purchases. | Terms, Section 21 |
| Return schema | Use a “returns not permitted” category if supported, not a finite return window. Do not invent fees, refund methods, return labels or a 30-day promise. | [Schema.org return policy](https://schema.org/MerchantReturnPolicy) |
| Privacy | `https://drinkhalfday.com/pages/privacy-policy` | Footer policy link |
| Shipping | Customer-facing purchases route to Amazon/retailers. Use the seller's delivery estimate; no universal free shipping/rate/transit claim. The legacy FAQ's 3–5-day estimate is not enough to establish current seller-specific service. | Storefront CTAs; [FAQ](https://drinkhalfday.com/pages/faq) |
| Location | Do not create a customer-facing LocalBusiness/retail location from the legal mailing address or a 3PL location. Retailer stockists are not owned Halfday stores. | Store model and existing locator |
| Product/offer facts | Preserve verified SKU/GTIN values and purchase URLs. Shopify stock is not Amazon stock. Suppress inappropriate Shopify offers on Amazon-directed pages. Preserve staff/sample access restrictions. | Existing Wave 1 audit and template mapping |

Do not apply Halfday's return terms as an Amazon-wide policy. Orders through other sellers follow the seller's policies. Do not infer automatic refunds from the instruction to contact support.

## Fresh public baseline findings

1. **Refund and shipping endpoints have no policy body.** Both `/policies/refund-policy` and `/policies/shipping-policy` return HTTP 200 but their main content contains only the page title. The usable return terms are in Section 21 of `/pages/terms-of-service`. Configure Agentready with that actual source rather than treating a 200 response as a complete policy. If its fields require native Shopify policy content, copy the existing approved terms faithfully during authenticated setup; do not generate new legal promises.
2. **Root discovery files already exist.** `/llms.txt` and `/agents.md` return Markdown containing Shopify commerce instructions and links to privacy/terms. The observed files do not supply Halfday's return terms, support email, flavors or Amazon buying context. Their existence is not evidence that Agentready is configured. Inspect Agentready's supported publication path and verify which content is actually served after setup; do not assume an app can replace a Shopify-owned route.
3. **No blanket crawl block observed.** The current `robots.txt` allows public content and blocks private/transactional routes and filter/preview traps. No new robots override is needed from this evidence. Do not relax protected routes to raise an app score.
4. **Offers require channel-aware setup.** Agentready's documented input includes Shopify price and availability. That can recreate the misleading offers already repaired in the development theme. Inspect exclusions and offer controls before bulk generation. Treat unpublishable staff/sample items and logistics cases separately from consumer products.
5. **Schema ownership must be reconciled.** The theme emits Organization/Product/Article data and Yotpo supplies existing review data. Compare entity IDs, prices, availability and reviews against Agentready output. Avoid adding contradictory Product nodes or invented review aggregates. Only remove an existing emitter after its replacement is verified.
6. **Content issues remain outside app setup.** Resolve slim-can calories/ingredients/caffeine, consumer 4-packs versus logistics cases, missing caffeine answer, stale campaign pages, and overlapping blog content. Agentready cannot resolve conflicting source facts by itself. No bulk AI rewrite of nutrition, health claims or old articles is justified by the current evidence.

The checked public endpoint summaries are in [baseline evidence](../reports/agentready-public-baseline.json). Raw public captures are temporary; no authenticated tokens or customer information are retained.

## Completed theme improvements

- Added two visible, crawlable answers to the development FAQ: returns/exchanges and damaged/incorrect orders. Both link to the published policy and preserve the support destination. Existing questions are retained.
- Changes are confined to `templates/page.faqs.json`; no additional JavaScript or schema emitter. Uploaded only that template through Shopify CLI to development theme `142755430600` with remote deletion disabled.
- Refreshed the live theme with CLI in a separate temporary directory; it still matches `main`. Theme Check remains at 122 errors / 404 warnings, with inherited findings unchanged in count.
- Browser QA confirms 19 FAQ questions, one H1, development assets, keyboard opening of the return answer and mouse opening of the damaged-order answer. Both show the intended policy-backed text; no forms submitted.

## Original plan before trial approval (historical)

1. Obtain approval of the displayed Core trial/renewal. Resume the saved review rather than scanning again and overwriting the edited proposals.
2. Apply the reviewed decisions, then complete logo, privacy/legal links and catalog/buying configuration from the source sheet. Resolve the numeric return-window limitation before emitting policy schema.
3. Confirm scope for public products, staff/sample exclusions, Amazon offer treatment and schema ownership. Review every proposed automated content change against store facts.
4. Generate only accurate, applicable output. Public documentation describes free manual generation, but the actual authenticated Free Audit plan explicitly gates applying/publishing behind a trial. Follow the observed plan permissions; do not claim that the documented free generation path works here.
5. Use Shopify CLI to synchronize any theme embed changes into the dev branch. Inspect generated JSON-LD in development before enabling conflicting output on the live theme. The user authorized Agentready setup; release of unrelated Wave 1 theme changes remains separate.
6. Verify delivered HTML and discovery paths for home, a flavor PDP, a variety PDP, a retail-only slim-can PDP, FAQ and protected staff pages. Check parsing, matching visible facts, no leaked protected products, correct policies, no duplicate/conflicting offers, and no unnecessary shopper JavaScript.
7. Re-run the app audit and record configured, generated, enabled, observed and validated states separately. Produce the actual post-setup gap list with evidence and dependencies.

Official references: [Agentready onboarding](https://joinagentready.com/docs/getting-started), [structured-data lifecycle](https://joinagentready.com/docs/structured-data), [policy setup](https://app.joinagentready.com/portal/add-policies), [discovery files](https://joinagentready.com/docs/agents-md-and-llms-txt). Agentready's score is a diagnostic, not proof of search placement. [Google's guidance](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) prioritizes ordinary SEO, useful content and accurate facts; it does not require special AI files or markup for generative search.
