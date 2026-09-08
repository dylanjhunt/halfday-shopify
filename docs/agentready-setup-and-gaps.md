# Agentready setup and SEO/AEO follow-up

September 7, 2026 (Toronto). **34 reviewed Concierge decisions are saved; application is pending approval of Core billing.** Shopify passkey verification cleared and both embedded and full Agentready dashboards were inspected. The current Free Audit plan cannot apply the setup. The displayed Core offer is a 14-day trial followed by $9/month. No trial or charge was started. No Agentready settings have been applied to store output, no embed was enabled, and no production policy was changed. This is a setup-progress and verified gap report, not a completed post-setup audit.

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

## Resume after plan approval

1. Obtain approval of the displayed Core trial/renewal. Resume the saved review rather than scanning again and overwriting the edited proposals.
2. Apply the reviewed decisions, then complete logo, privacy/legal links and catalog/buying configuration from the source sheet. Resolve the numeric return-window limitation before emitting policy schema.
3. Confirm scope for public products, staff/sample exclusions, Amazon offer treatment and schema ownership. Review every proposed automated content change against store facts.
4. Generate only accurate, applicable output. Public documentation describes free manual generation, but the actual authenticated Free Audit plan explicitly gates applying/publishing behind a trial. Follow the observed plan permissions; do not claim that the documented free generation path works here.
5. Use Shopify CLI to synchronize any theme embed changes into the dev branch. Inspect generated JSON-LD in development before enabling conflicting output on the live theme. The user authorized Agentready setup; release of unrelated Wave 1 theme changes remains separate.
6. Verify delivered HTML and discovery paths for home, a flavor PDP, a variety PDP, a retail-only slim-can PDP, FAQ and protected staff pages. Check parsing, matching visible facts, no leaked protected products, correct policies, no duplicate/conflicting offers, and no unnecessary shopper JavaScript.
7. Re-run the app audit and record configured, generated, enabled, observed and validated states separately. Produce the actual post-setup gap list with evidence and dependencies.

Official references: [Agentready onboarding](https://joinagentready.com/docs/getting-started), [structured-data lifecycle](https://joinagentready.com/docs/structured-data), [policy setup](https://app.joinagentready.com/portal/add-policies), [discovery files](https://joinagentready.com/docs/agents-md-and-llms-txt). Agentready's score is a diagnostic, not proof of search placement. [Google's guidance](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) prioritizes ordinary SEO, useful content and accurate facts; it does not require special AI files or markup for generative search.
