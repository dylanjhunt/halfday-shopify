# Agentready implementation and UX findings

## September 8, 19:29 UTC: recheck after app updates

- **AR-00 mitigation improved:** the previously exposed staff markdown URL and a public Lemon Tea control both return 404 with `private, no-store`. Both app output switches and the embed are off. This confirms the output-off endpoint behavior is repaired in this configuration. Protected exclusions with output enabled remain unverified; do not close the entire visibility issue yet.
- **Concierge Apply still fails:** re-reviewed the saved 34 proposals (7 brand, 2 policy, 25 page types) and made one Apply attempt. It returned “Apply was not confirmed” with `Reason: unsupported_field`. No durable Shopify write was confirmed. Show the rejected field/path and a per-change result, validate field support before enabling Apply, and migrate older saved plan payloads when field names change. Keep successful and failed writes distinguishable.
- **Recovery loses the attempt view:** “Reload saved attempt” returned to the welcome screen with “Analyze my store,” rather than a saved-attempt status or the reviewed plan. Preserve the run/attempt identifier, show its durable result and offer a direct return to the reviewed proposals. Do not imply a fresh scan is required to recover.
- **Plan state disagrees:** embedded Shopify overview says Growth; standalone says Core trial and locks Schema issues as requiring Growth. Read one canonical entitlement state and label any store/account distinction explicitly.
- **Embedded primary CTA:** “Review my setup plan” produced no visible navigation or new tab. The existing standalone Concierge tab provided a workaround. Use a reliable embedded navigation/deep link and expose a fallback link if a new window cannot open.
- **Priority relevance remains weak:** the embedded overview still leads a tea store with “category, color_family, material.” Filter merchant-facing priorities to the approved public beverage catalog and show the affected records and why each attribute matters before presenting it as the most important next step.

Go live was checked after the failed attempt and still showed Embed off / Output off. No output activation, rescan, app plan change or repeated Apply was performed. [Minimal evidence](../reports/agentready-visibility-recheck-2026-09-08.json). Earlier findings below are retained as history and remain open unless superseded above.


Observed September 8, 2026 while setting up Halfday, a Shopify brand site whose public product CTAs direct shoppers to Amazon. Core trial active. This is a working report, updated during implementation. Findings describe observed behavior, not inferred backend causes. No report has been sent externally.

## Highest priority

### AR-00: Protected catalog data remains publicly readable through app endpoints

**Severity:** Critical release blocker. **Status:** Reproduced with anonymous HTTP requests, not just a generated preview.

On the development theme, enabling the embed emitted `data-agentready="collection"` and CollectionPage/ItemList JSON-LD on a Locksmith-protected staff collection. The visible page remained protected, but the app added the staff product name, ID and URL to its HTML. The embed was immediately disabled again through Shopify CLI; the production embed was never saved or enabled.

Separately, the app's direct `/apps/agentready/products/<handle>.md` endpoint returned HTTP 200 for a staff jacket, including price, variants and `sales-sample` / `sample-only` tags. This happened with the production embed off and LLMs “Include Products” unchecked. No customer/order data was encountered. Full response content is not included here; retain minimal reproducible evidence internally.

**Final mitigation check:** turned off both shared render switches, explicitly hid all 45 selectable product rows, saved curation and regenerated. The protected markdown URL still returned HTTP 200 at 12:08 UTC, with `Age: 0` and `Cache-Control: public, max-age=900`. No cookies were sent. This remains unresolved by the available settings. Do not describe Output off as a public-data shutdown. The UI's stated five-minute app-proxy cache also does not describe this endpoint's observed 15-minute cache header. Minimal evidence is in `reports/agentready-implementation-verification.json`.

**Improve:** Enforce one server-side visibility policy across theme output, indexes, markdown detail endpoints, JSON, MCP/tools, caches and search. Online Store publication alone must not imply public eligibility. Respect Locksmith rules or require an explicit safe product allowlist when access rules cannot be resolved. Provide a merchant emergency switch that blocks public app endpoints, invalidates cached responses and reports completion. Test a protected product by direct handle with no cookies and test that exclusion works after cache invalidation.

**Related draft issue:** The default agents.md generator listed Employee Shop, Sample Only and staff collections, and featured two staff merchandise products. Explicit priority collections and featured tea handles removed these from the draft, but draft curation is not endpoint access control.

### AR-01: Concierge cannot confirm Apply

**Severity:** High, blocks the onboarding completion path. **Status:** Reproduced twice, including after reloading the saved attempt.

Steps: review the seven brand fields, two policies and 25 page classifications; approve 34 changes; complete billing; choose Apply my approved changes. Result: “Apply was not confirmed” and “AgentReady did not confirm a durable Apply result. No Shopify write is proven by this response; reload the saved attempt before deciding whether to retry.” Returning to the saved attempt starts at Brand details. The individual Brand settings screen still showed empty values. A reloaded retry produced the same result. Manual brand settings subsequently saved successfully.

**Improve:** Persist an idempotent apply job with a visible receipt and per-item states: queued, applied, failed, unchanged. Resume at the failed step. Show the actual validation or service error, a support reference, last-attempt time and a safe retry of failed items only. Provide a direct “Continue in settings” route with reviewed values prefilled. Do not ask merchants to infer whether Shopify was written. Test billing-return navigation and retries without duplicate writes.

### AR-02: Valid return policy rejected because it lives in Terms

**Severity:** High, prevents saving the authoritative source. **Status:** Confirmed in Returns & shipping.

Halfday's published Terms of Service contains the actual returns terms in Section 21. Entering `https://drinkhalfday.com/pages/terms-of-service` as the returns override and saving produced: “This link reads like a different policy type. Use the public returns or refund-policy page.” Other changes on the same screen remained unsaved. Concierge had allowed this same source during review.

**Improve:** Validate page content and the cited section, not just the URL slug. Support a policy section within Terms, an optional source excerpt and a reviewed override when the heuristic is wrong. Warn without blocking valid sources. Use the same validation rules in Concierge and settings, before billing and before Apply. Save independent valid sections separately.

### AR-03: No explicit “returns not accepted” policy model

**Severity:** High, risks inaccurate commerce data. **Status:** Confirmed in available form controls; emitted behavior still needs verification.

The returns form offers a numerical window, fees and methods, but no “returns not accepted” category. It defaults to 30 days. Clearing the number returns to 30; the reviewed Concierge proposal displays a 0-day window. Halfday's policy is no product returns/exchanges, with immediate contact for damaged or incorrect orders. Zero days is an ambiguous substitute for no returns.

**Improve:** Start with Accepted / Not accepted / Seller-specific / Unknown. Map Not accepted to `MerchantReturnNotPermitted`, omit the numerical window, and retain damage/incorrect-order exceptions separately. Show the exact generated policy beside the plain-English preview. Keep unverified defaults out of every discovery output, not only JSON-LD.

### AR-04: Buying-channel and protected-catalog setup are missing

**Severity:** High, correctness and potential unwanted product discovery. **Status:** Configuration gap observed; no leakage claimed.

Structured data offers ProductGroup with per-variant Shopify price/availability or Product with AggregateOffer. There is no visible “sold on Amazon / retailer” choice or offer suppression control. “Only include products published to your Online Store” is useful but insufficient for Halfday: Locksmith-protected staff merchandise can still be published to that channel. The audit includes staff, sample and logistics records alongside public tea products.

**Improve:** Ask where shoppers buy during onboarding. Support brand catalog pages with external retailer links, without treating 3PL stock as retailer availability. Add per-product, collection, tag and template exclusions; identify access-control integrations; show an explicit public inclusion preview before syncing or enabling discovery. Default uncertain protected items to excluded. Support a safe brand/content-only activation path.

## Data presentation and onboarding improvements

### AR-05: “Verified live” can mean Agentready is absent

**Severity:** High confidence/diagnostic issue. The prior check showed a green “Verified live” heading, then stated “Schema found, but none of it is AgentReady’s on your homepage or product page.” Existing theme Organization/WebSite/Product schema had passed the generic type check.

**Improve:** Separate URL fetched, any valid schema found, Agentready schema found and exact current version verified. Use a warning state when the app's own output is absent. Name the checked theme and show timestamps. A dev-preview check should be distinct from production.

### AR-06: Readiness denominators obscure the work that matters

The initial audit used 25 sampled products while the optimizer and catalog requirements scanned 46 active products. Twenty duplicate “Variety 12-Pack” titles were staff merchandise/logistics records, not twenty consumer variety packs. The overview showed 100% catalog coverage / 25 products synced alongside “Not synced yet.”

**Improve:** Show the same scope selector throughout: public consumer catalog, protected/internal, unpublished, or all. Label sampled versus complete counts, denominator and snapshot time. Split data prepared, published and verified. Do not equate generated rows with completed synchronization or public coverage. Prioritize fixes by public traffic/relevance, not only raw counts.

### AR-07: Imported facts and confirmed facts need distinct provenance

AI-drafted onboarding copy included claims we removed during review. Manual Brand settings calls saved business information “owner-confirmed facts,” although an authorized implementer entered it from the store.

**Improve:** Use sourced / suggested / reviewed / published states. Show the source URL and relevant excerpt for each claim. Record who reviewed it and when. Include business model, core offerings, audience and market in the same initial review, so the seven-field Concierge does not leave a second required Brand questionnaire.

### AR-08: Legal policy discovery assumes native Shopify policies

Privacy and Terms are marked missing in the policy settings even though real content is published as Shopify pages. Only returns and shipping have editable override URLs.

**Improve:** Discover footer-linked legal pages and offer reviewed overrides for all policy types. Distinguish empty native policy bodies from HTTP 200 pages. Let merchants connect existing policy content without duplicating legal documents.

### AR-09: Activation copy overstates crawl and search outcomes

The embed-off state says “Hidden from AI agents,” although the public store and existing theme schema are readable. The overview says the storefront is in strong shape for AI discovery while activation and a complete sync are missing. Output help says both JSON-LD and Agent JSON must be enabled to publish schema, without explaining their actual dependency.

After mitigation, a fresh audit completed at 80/100 with 16 findings. One says “Your live structured data stopped reaching your storefront,” although the Agentready embed was never enabled on production in this setup. Use Never activated / Intentionally paused / Previously verified, now missing as distinct states.

**Improve:** Say “Agentready output is not enabled on your live theme.” Keep accessibility/crawl status separate from app installation. Explain whether each output is independent and allow selective activation. Present readiness as a diagnostic score with evidence, not proof of recommendations, rankings or traffic.

### AR-10: Generated data conflicts with confirmed facts and defaults

**Severity:** High. Development homepage JSON-LD used the saved brand description, while Agent JSON still used the original Shopify description. Organization JSON-LD emitted a Standard shipping service to `IN` and `US`, despite delivery estimates remaining unconfirmed and the configured business market being United States. The source of India was not established. No shipping settings in Shopify were changed.

**Improve:** Show provenance beside every derived field. Build all output formats from the same normalized facts and version. Do not infer public shipping commitments from unrelated operational locations or unreviewed defaults. Expose exactly which fields the shipping-confirmation switch suppresses, including Organization ShippingService versus OfferShippingDetails.

### AR-11: LLMs generation ignores a saved description override and leaks script text into summaries

**Severity:** Medium. The saved LLMs-only description override remained visible in settings, but the generated 2.8 KB file at `/apps/agentready/llms.txt` used the Brand description plus tagline instead. The Find In Store summary included Stockist loading text and JavaScript from the page body. The full file omitted the Pages section even though the shorter index included it and described the full file as the same document with complete descriptions.

**Improve:** Apply the stated description precedence and test it after regeneration. Strip script/style/placeholder content before summarization and prefer meaningful rendered content. Give merchants a draft preview and diff before publishing. Make short/full-file scope consistent or explain differences accurately.

### AR-12: Copyright permissions should not default to a Creative Commons license

**Severity:** High product-policy concern, no unintended license was published in this run. The LLMs License field defaults to CC-BY-NC-SA 4.0 when blank. We selected All Rights Reserved before generation.

**Improve:** Default to existing rights/no new license grant. Explain the choices neutrally and require a deliberate rights-holder decision before publishing a new license. Avoid reducing a legal license to “display + training” labels without clarifying its actual scope.

### AR-13: Guided setup and page settings disagree on scope

Concierge offered 25 page decisions, including many URLs that returned 404. The regular Pages screen later showed 12 published pages and explicitly hid 26 unpublished pages. It detected Contact and FAQ, but missed Our Story. We saved AboutPage for Our Story and hid the three currently published promo/test pages in that screen.

**Improve:** Use the same published-resource scope and source snapshot in both flows. Do not ask merchants to classify inaccessible drafts by default. Display why a page is missing or excluded, and what “Hidden from AI” does across each output. A classification should not be mistaken for noindex, unpublishing or access control.

### AR-14: Theme-built FAQ content is missed

Agentready detects the FAQ URL, but “Add FAQ data” is still required. The preview emitted a generic WebPage with an empty content summary rather than the visible FAQ questions. Halfday's FAQ content lives in theme section blocks, not the Shopify page body.

**Improve:** Extract visible questions from the rendered storefront or explain that theme-section content needs import. Show the exact questions before publishing and distinguish detected FAQ page type from populated FAQPage schema. Keep answers aligned with visible text and warn about stale duplicate copies.

## Recommended onboarding order

1. Identify business model, where purchases happen, target market and protected/internal catalog scope.
2. Discover existing brand facts, legal pages, theme schema and access-control apps. Explain what is already present.
3. Review sourced brand/product/policy facts, including no-return and retailer-specific cases. Validate all inputs here.
4. Show exactly what will change: app settings, Shopify records, discovery endpoints and theme. Allow independent brand/content and commerce activation.
5. Preview generated data with excluded-item examples and duplicate-schema warnings before enabling the embed on a selected theme.
6. Apply with a durable receipt and resumable failures. Verify exact output on the chosen theme, then offer an explicitly separate live release.
7. Present a short, scoped remaining-work list with evidence, owner, relevance and an appropriate next action. Keep recommendations and measured search outcomes separate.

## Verification notes

No application source code or backend logs were inspected. Email values omitted by the browser's text inspection were visible in screenshots, so that tooling behavior is not reported as an app defect. Pointer automation difficulties with styled switches are not considered confirmed app defects without normal-user reproduction.
