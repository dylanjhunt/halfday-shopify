# Wave 1 follow-through release audit

Dylan authorized merging the audited changes and then continuing development on September 8, 2026. Release candidate: `290f345`, following published baseline `2c8ff4f`. This report and the fresh regression evidence do not change theme behavior.

## Release decision

Ready to release the six theme files covering on-demand product gallery video, responsive collection banners, reserved review space, isolated rating styles and unique product-information anchors. No release-blocking regression was found in the checks below.

## Final checks

- Fresh Shopify CLI snapshots: all **455 live files match main** and all **455 development files match the release candidate**. No merchant drift to reconcile. Live role: `142757101768`; development role: `142755430600`.
- The [fresh 15-route comparison](../reports/wave-1-release-regression.json) passed explicit assertions for preview identity, Liquid rendering, Amazon URLs and attribution parameters, external loaders, Klaviyo embeds, product data IDs and forms. Library hashes, protected purchase/Locksmith files and merchant settings are unchanged.
- Theme Check: **122 inherited errors and 391 warnings**, zero added offenses compared with the preceding verified candidate. JavaScript syntax, motion lifecycle harness and Git whitespace checks pass.
- Extended browser checks: Lemon Tea at 1024px and 768px has no horizontal page overflow, real Yotpo stars/count and hidden fallback. At 1024px the gallery initially contains no video; Enter on Play video instantiates one native controlled video, and the next-slide button pauses it. Its media reaches readyState 4.
- Strawberry slim-can zero-review fallback remains visible and keyboard navigation at 390px settles at the Reviews section, about 110px below the viewport top. No horizontal overflow.
- Shop All at 390px renders one H1 and one banner image, selecting the mobile artwork. Desktop/mobile gallery, collection and review visual checks are also documented in the [gallery pass](wave-1-follow-through-2026-09-08.md) and [review pass](wave-1-review-layout-2026-09-08.md).

## Limits and next work

The two latest fresh mobile preview measurements had LCP 4.86s/5.26s and CLS 0.000153/0.001416, with no initial video transfer. LCP is still variable and unresolved; no field-CWV or conversion gain is claimed. Preserving tracking loaders and URL parameters does not prove downstream event receipt. GA/Ads remain deferred and GTM excluded. Native authenticated staff checkout is outside the release gate as directed; its code and access protections are preserved. External video/model fixtures and populated native-rating metafields were not available for full interaction testing.

The tablet audit found the existing Watermelon flavor label crowded against the edge of the flavor selector. Address this as a separate development change after release. Agentready Apply (`unsupported_field`), app ownership/scoping, approved catalog facts and editorial decisions remain open.

After pushing main, verify the connected Shopify theme by a fresh download and public storefront smoke checks. Record the actual release commit and verification in the next development branch; do not treat a successful Git push alone as deployment proof.

## Deployment verified

Merged and pushed main at **`a99ed7f`**. Shopify theme `142757101768` remains live with processing complete; a fresh post-push download matches all **455 theme files** at main. The release tag is `baseline/live-wave-1-follow-through-2026-09-08`. After exiting browser preview, public Lemon Tea renders the new ProductDetails anchor, no initial gallery video and the unchanged attributed Amazon purchase link. No separate Shopify publish action was needed.

Continued work is isolated on `djh/wave-1-responsive-follow-up` and development theme `142755430600`.
