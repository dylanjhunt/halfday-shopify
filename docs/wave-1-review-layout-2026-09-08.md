# Wave 1 review layout and Agentready follow-up

New changes remain on `feature/wave-1-follow-through`, development theme **142755430600**. Shopify CLI confirms **142757101768** is live; its fresh 455-file snapshot matches `main`. No production theme code changed.

## Completed theme work

- **Reserved review space:** the product header now reserves its existing rating row before Yotpo inserts content. Rated products retain the measured final title position on mobile and desktop. This addresses the earlier approximately 42px desktop heading movement.
- **Useful empty/loading state:** an editable “Reviews” link fills the slot until a real rating/count is present. Products with no reviews show that link rather than empty stars or a blank gap. Keyboard navigation lands at the review section below the header. This is an intentional improvement to the zero-review presentation, not a claim that those products have ratings.
- **Scoped star styles:** Dawn's `.rating-star` rules also matched Yotpo's individual star elements. Restrict them to direct children of Dawn's `.rating` component. Load the native rating stylesheet on the main product section only when its native rating block and rating data are present. Yotpo retains its own stars, click handlers and full review widget.
- **Unique product anchors:** both product-information columns previously had the same ID. The gallery's skip link now has one destination, the information/purchase column following the gallery. Native form and variant scripts, Locksmith rules and Amazon URLs remain unchanged.

No JavaScript was added or changed. The fallback label is a text setting in the existing Review New block. Its target is the existing `Reviews` section; preserve that target when migrating review vendors.

Yotpo documents synced review-count/average fields for custom displays, but those fields and the cached summary were empty on all five checked tea/variety products. We did not invent counts, add aggregate-rating schema or enable shared sync settings. [Yotpo metafield documentation](https://support.yotpo.com/docs/yotpo-reviews-rich-snippets).

## Verification

- Browser checks at **390px and 1440px** cover Lemon Tea's loaded rating layout, Watermelon ratings, the Strawberry slim-can zero-review state, keyboard fallback navigation and the gallery skip link. Lemon's desktop H1 remains at y=197px; mobile remains at y=116.13px. Mobile ratings retain right alignment. Zero-review links reach the review section at about y=110px, below the sticky header.
- [15-route regression comparison](../reports/wave-1-review-regression.json) preserves Amazon URLs/attribution, tracking/app loaders, Klaviyo embeds, merchant settings and protected/native purchase code. This does not prove downstream tracking receipt.
- Theme Check remains **122 inherited errors / 391 warnings**, with no added offenses. Whitespace checks pass. Four files were read back and matched, including the restored unchanged locale file. The final theme diff for this pass contains three files.
- [Verification evidence](../reports/wave-1-review-verification.json).

Two sequential fresh mobile Lighthouse 13.4.1 preview runs, with no app/request blocking:

| Metric | Run 1 | Run 2 |
| --- | --- | --- |
| CLS | 0.000153 | 0.001416 |
| LCP | 4.86s | 5.26s |
| TBT | 3,056ms | 1,226ms |
| Initial video transfer | 0 | 0 |
| Console-error audit | Pass | Pass |

The earlier baseline included review-related CLS around 0.043, but also much lower samples. These results support the layout repair; they do not establish a field-CWV improvement or a consistent LCP gain. Small Yotpo/internal icon shifts remain in the traces. The larger remaining performance work concerns render delays and app costs, especially supported Signifyd scoping.

## Agentready recheck

The prior anonymous staff-product markdown request now returns **404**, `Cache-Control: private, no-store`, with no product details. A public Lemon Tea control endpoint also returns 404. Both output switches and the theme embed remain off. This verifies the output-off mitigation; it does not yet prove protected-resource exclusions with output enabled.

Reviewed the saved Concierge plan again: seven brand fields, two source-backed policy summaries and 25 page classifications, totaling 34 approved proposals. One Apply attempt returned **“Apply was not confirmed” / `unsupported_field`**. No durable Shopify write was confirmed. “Reload saved attempt” returned to the welcome/Analyze screen. No new analysis or repeated Apply was started. Go live still reports Embed off and Output off afterward.

The embedded Shopify overview shows Growth, while the standalone dashboard shows Core trial and locks Growth features. Its “Review my setup plan” button produced no visible navigation or new tab in this session. These findings and suggested fixes are in the [Agentready feedback report](agentready-product-feedback.md). [Minimal recheck evidence](../reports/agentready-visibility-recheck-2026-09-08.json).

## Remaining

- Resolve the Agentready unsupported-field/recovery issue, then verify scoped output on development before activating it.
- Confirm Signifyd scoping and app/SMS ownership. No app was uninstalled or globally disabled in this pass.
- Supply approved 4-pack/slim-can facts, imagery and channel destinations for catalog/CRO work.
- Resolve the existing claims, Subscribe-purpose and retired-content decisions. The sampled blog card image source descriptors/alt text rendered correctly, so no speculative image-object rewrite was made.
- LCP remains unresolved; these changes are not authorization to merge or push main. Klaviyo activation belongs to Wave 2; GA/Ads remain deferred and GTM excluded.
