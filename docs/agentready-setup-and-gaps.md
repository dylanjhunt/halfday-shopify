# Agentready setup and SEO/AEO follow-up

September 7, 2026 (Toronto). **Onboarding pending Shopify passkey verification.** Agentready is installed per Dylan, but its authenticated settings, current plan, score and onboarding have not yet been inspected. No Agentready setting, feed, app embed or production policy has been changed in this checkpoint. This is the verified setup source sheet and baseline gap list, not a completed post-setup audit.

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

## Completed while onboarding access is pending

- Added two visible, crawlable answers to the development FAQ: returns/exchanges and damaged/incorrect orders. Both link to the published policy and preserve the support destination. Existing questions are retained.
- Changes are confined to `templates/page.faqs.json`; no additional JavaScript or schema emitter. Uploaded only that template through Shopify CLI to development theme `142755430600` with remote deletion disabled.
- Refreshed the live theme with CLI in a separate temporary directory; it still matches `main`. Theme Check remains at 122 errors / 404 warnings, with inherited findings unchanged in count.
- Browser QA confirms 19 FAQ questions, one H1, development assets, keyboard opening of the return answer and mouse opening of the damaged-order answer. Both show the intended policy-backed text; no forms submitted.

## Resume onboarding after verification

1. Inspect the app's actual onboarding, plan and existing configuration. Record the baseline score/gaps. Keep the current plan unless Dylan approves a paid change.
2. Configure brand, support, legal/policy links and concise catalog/buying context from the source sheet. Preserve absent/unknown numeric policy fields rather than inserting defaults.
3. Confirm scope for public products, staff/sample exclusions, Amazon offer treatment and schema ownership. Review every proposed automated content change against store facts.
4. Generate only accurate, applicable output. Agentready's documentation says free manual generation has a six-hour cooldown, so confirm inputs before consuming a run.
5. Use Shopify CLI to synchronize any theme embed changes into the dev branch. Inspect generated JSON-LD in development before enabling conflicting output on the live theme. The user authorized Agentready setup; release of unrelated Wave 1 theme changes remains separate.
6. Verify delivered HTML and discovery paths for home, a flavor PDP, a variety PDP, a retail-only slim-can PDP, FAQ and protected staff pages. Check parsing, matching visible facts, no leaked protected products, correct policies, no duplicate/conflicting offers, and no unnecessary shopper JavaScript.
7. Re-run the app audit and record configured, generated, enabled, observed and validated states separately. Produce the actual post-setup gap list with evidence and dependencies.

Official references: [Agentready onboarding](https://joinagentready.com/docs/getting-started), [structured-data lifecycle](https://joinagentready.com/docs/structured-data), [policy setup](https://app.joinagentready.com/portal/add-policies), [discovery files](https://joinagentready.com/docs/agents-md-and-llms-txt). Agentready's score is a diagnostic, not proof of search placement. [Google's guidance](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) prioritizes ordinary SEO, useful content and accurate facts; it does not require special AI files or markup for generative search.
