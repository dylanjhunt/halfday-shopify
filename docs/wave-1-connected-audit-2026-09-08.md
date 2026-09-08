# Wave 1 connected-theme release audit

September 8, 2026. Audited commit `2c8ff4f` on `main`, connected to unpublished Shopify theme **142757101768**, `halfday-shopify/main`.

[Connected preview](https://drinkhalfday.com/?preview_theme_id=142757101768) · [Sanitized audit evidence](../reports/wave-1-connected-audit-2026-09-08.json)

**Result: no new functional regression found in the public journeys tested. The Wave 1 changes are present and functioning on the Git-connected theme.** This is a conditional release assessment: authenticated staff/sample ordering and identified signup/conversion validation remain unverified. The theme was not published or modified during this audit.

## Sync and automated checks

- All **455 native theme files** downloaded from the connected theme match `main` byte for byte. Nothing is missing or extra. All **447 live-theme files** still match `baseline/live-2026-09-07`, so no newer merchant edits were found.
- **15 live/preview route comparisons pass**, including an explicit rendered Shopify theme ID check. Amazon destinations and full attribution parameters, Klaviyo embed IDs, external loaders, integration markers and protected native code are preserved.
- **22 routes/endpoints checked for Wave 1 features:** no rendered Liquid errors or invalid JSON-LD. Product descriptions are present without unsupported Shopify offers on retailer-directed PDPs. Key public search/social descriptions agree. HTTPS image metadata uses the selected image dimensions. Utility `noindex,follow`, repaired article links and the curated `/agents.md`, `/llms.txt` and `/llms-full.txt` outputs are present.
- Homepage and Why Halfday each retain **32 server-rendered stylesheet links**. Unused rating/bulk-order stylesheet files are absent on their inactive routes. Client-inserted app styles can increase the browser DOM count.
- Theme Check remains **122 inherited errors / 391 warnings**, with exactly the same finding signatures as the last verified checkpoint. The motion lifecycle harness passes. This is not a clean Theme Check result.

Re-run the route check with:

```sh
python3 scripts/verify-regressions.py --theme-id 142757101768 --output /private/tmp/halfday-connected-regression.json
```

## Browser interaction and layout checks

Checked representative layouts at **390px and 1440px**. No horizontal overflow was found on the checked public layouts.

- Desktop Shop opens by click/Enter and closes with Escape; Learn opens correctly. Product carousel Next reaches 2/8.
- Mobile drawer and Variety Packs submenu work. Its CTA reaches Classic Variety without the old preview URL. The product format control switches the displayed options; selecting Lemon Tea reaches its PDP.
- Classic Variety gallery Next reaches 2/2; Lemon gallery Next reaches 2/5. Each checked PDP retains one high-priority gallery image and the existing Amazon CTA.
- Homepage initially has no video elements. Scrolling to Instagram loads media and visible video plays. The motion harness additionally covers focus, tab visibility, reduced motion, reuse and editor cleanup.
- FAQ Orders reaches `#faq_orders` below the header; Enter opens the returns answer. Mobile footer Enter/Space open/close controls, and all desktop lists return after resizing.
- Store locator search for the sample ZIP **10001** returns nearby retailers.
- Contact preserves its desktop photo/form layout, mobile artwork and form endpoint. Mobile does not select the hidden desktop photo. Name-to-Email keyboard focus works. Contact/Why Halfday retain the prior content-image frames, and Why Halfday's crop-aware mobile sizing is present.
- Signup popup opens after keyboard activation and closes normally. Footer signup UI renders. No contact, signup or review form was submitted.
- Anonymous staff collection shows no products. Its native empty cart drawer opens/closes. This does not validate eligible staff inventory, quantity rules, discounts or checkout.

## Fresh mobile lab samples

One sequential Lighthouse 13.4.1 sample per page/theme, fresh anonymous Chrome profiles. Values are individual samples, not medians or field metrics. Preview infrastructure and third-party timing differ from production.

| Metric | Live home | Connected home | Live Lemon PDP | Connected Lemon PDP |
| --- | ---: | ---: | ---: | ---: |
| Total transfer | 43.10 MB | 6.83 MB | 38.28 MB | 15.12 MB |
| Media transfer | 35.62 MB | 0 MB | 31.71 MB | 8.96 MB |
| LCP | 27.52s | 6.89s | 12.26s | 9.41s |
| CLS | 0 | 0.000113 | 0.041457 | 0.000208 |
| Total blocking time | 1,041ms | 1,561ms | 1,313ms | 898ms |
| Performance score | 33 | 36 | 38 | 41 |
| Console errors | 1 | 0 | 1 | 0 |

The homepage transfer reduction is approximately **84%** in this comparison. The old header `DetailsDisclosure` error reproduces in both live runs and is absent in both connected runs. The PDP's previously fixed header layout shift remains resolved in the connected sample. No HTTP 4xx/5xx responses were recorded in either connected run.

**LCP and main-thread work remain unfinished.** These samples do not establish consistent responsiveness or an acceptable LCP. Homepage TBT is worse in this sample, even though total transfer is much smaller. Prior repeated runs were also variable. The PDP still transfers approximately 8.96 MB of media during this audit; inspect native gallery-video delivery separately from the already-deferred testimonial/footer videos before the next performance change.

Klaviyo onsite analytics returns **200/202**, and Postscript page events return **200**, in both live and connected captures. Signifyd requests also complete. These checks establish transport continuity, not payload correctness, identified profiles, consent eligibility or Amazon conversion attribution.

## Existing issues and final release limits

1. **Authenticated staff/sample QA remains the main functional sign-off gap.** Use an eligible account to verify visibility, variant/quantity/inventory rules, cart and the checkout handoff. No orders were placed in this audit.
2. **App/performance work remains:** investigate measured Signifyd cost and native gallery media. Keep SMS/offer ownership and Yotpo migration decisions in their existing waves. Do not infer safe app removal from these timings.
3. **Existing accessibility/SEO debt:** live and preview both report color contrast, missing alt text in app/media output and non-crawlable app/menu controls. The missing iframe title in preview is Shopify's preview toolbar. Collection HTML still contains duplicate H1s; the HelloFresh/Subscribe pages lack a main H1. These templates were not changed by the merge. Subscribe description/purpose and expired campaign copy remain content follow-up items.
4. **Existing content/app dependencies remain open:** approved 4-pack/slim-can facts and discovery decisions; Agentready's shared visibility fixes and re-audit. Its theme embed remains disabled. This audit did not change shared app settings or certify those earlier app defects as resolved.
5. **Release is separate:** no publishing action occurred. These results apply to the exact synced theme/commit checked. Any subsequent merchant, app or Git changes require checking the affected paths again. GA/Ads remain deferred and GTM excluded.

Audit documentation and the parameterized verifier are kept on `feature/wave-1-release-audit`. Storefront code on `main` is unchanged.
