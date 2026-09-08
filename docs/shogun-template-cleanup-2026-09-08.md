# Shogun product template cleanup

Completed September 8, 2026, following Dylan's approval to remove the unused Shogun product assignments.

Inspected all 66 product records in Shopify admin, including active, unlisted, draft, and archived products. Found 39 products assigned to `shogun.custom`, with Shopify reporting that the template was unavailable in the current theme. Changed those 39 assignments to **Default product**. The other 27 products already used the default template.

Only the product Theme template field was edited. Product status, publishing, collections, tags, inventory, prices, descriptions, and purchase options were not edited. This is shared Shopify product data, not a theme-file change. No theme was published.

## Updated products

- 2026 Influencer Seeding Box
- 24pk STD 4-Pack 12oz Green Iced Tea
- 24pk STD 4-Pack 12oz Lemon Iced Tea
- Halfday Cranberry Notecard
- Halfday Cranberry Shipping Box
- Halfday Yellow Box
- Halfday Yellow Cooler Bag
- 24pk Case (6x4) Peach Iced Tea
- Half & Half Postcard
- 24pk STD 4-Pack 12oz H&H Iced Tea
- Peach Pins - Bag
- Halfday Hot Grill Summer Hat
- Halfday Tan W/Green Brim Hat
- Halfday Stickers
- Lemon Pins - Bag
- Women's Marmot Black Jacket
- Men's Marmot Black Jacket
- Halfday Balance Board
- Halfday Cream Hoodie (Men's Sizing)
- Puffin Can Coolers
- Black Halfday T-Shirt, Men's
- White Halfday T-Shirt (Men's)
- Black Halfday T-Shirt w/Yellow Pocket (Men's)
- Halfday Grey Baseball Hat
- Halfday Blue Baseball Hat
- 8 Case Shipper
- Halfday Peach Socks
- Halfday Lemon Socks
- Halfday GOT Bag Backback
- Halfday Black Baseball Hat
- Peach & Lemon
- Refresher Variety
- Lemon Tea
- Halfday Beanie
- Halfday Yellow Trucker Hat
- White Halfday T-Shirt, Small
- Green Tea
- Peach Tea
- Black Halfday Polo

## Verification

- Saved three assignments individually and 36 through the native bulk editor in groups of five or fewer. Each bulk save returned to the saved state; product records were also spot-checked after saving.
- Reopened Peach Tea, Black Halfday Polo, 2026 Influencer Seeding Box, White Halfday T-Shirt, Small, Lemon Tea, and Refresher Variety and confirmed Default product with no missing-template notice. Green Tea also displayed Product saved and Default product after its individual save.
- Fetched Lemon Tea, Peach Tea, Green Tea, and Refresher Variety on both production and the Git-connected preview theme `142757101768`. All eight responses returned HTTP 200, with no Liquid errors. Amazon destinations and attribution query parameters matched between live and preview, and no product data IDs were missing from the preview comparison. See `reports/shogun-template-cleanup-check.json`.
- Theme code contains no Shogun-specific dependency or product-template-suffix behavior that needs migrating. The suffix is used in a generic body class; the store-locator suffix condition applies only to pages.
- Existing hidden Shogun page bodies were outside this product-assignment cleanup and were not deleted. This does not retire those legacy pages or uninstall an app.

Shopify's bulk editor displayed missing assignments as `product` even before cleanup. Selecting that option explicitly registered an edit; the first saved batch was verified on the actual product record before continuing. A larger batch stalled while loading more records, so the remaining changes were saved in smaller groups.
