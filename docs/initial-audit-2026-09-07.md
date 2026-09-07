# Halfday — initial store and theme audit

**Date:** September 7, 2026. **Status:** initial evidence-based audit complete; app-side verification and implementation remain separate work.

**Recommendation:** first correct the mismatch between Amazon merchandising and Shopify inventory, then finish the existing slim-can/4-pack catalog setup. Follow with Klaviyo validation, SEO/content cleanup, and measured performance work. Preserve Yotpo until review migration is verified. Confirm fulfillment ownership before reconnecting any integrations.

GA, GTM, and Google Ads are explicitly deferred until Dylan confirms access. No analytics setup, ad activation, campaign changes, live theme edits, orders, subscriptions, app uninstalls, or integration-setting changes were performed.

## Evidence and limits

- Downloaded all **447 theme files** from live theme `141825474760`; untouched Git baseline `ed05175`. Theme metadata: Dawn 15.2.0. Shopify listed 19 themes before the development-environment check, including numerous old drafts.
- Read Shopify theme dashboard, installed apps, first 50 catalog rows, Peach Slim Can details, and first page of the Pages inventory. These were bounded samples, not full database exports.
- Inspected the rendered homepage, Lemon Tea PDP, Shop All, and Variety Packs. Rechecked asynchronously loaded Yotpo and Klaviyo content rather than treating initial empty containers as final failures.
- Captured 13 public HTTP responses, including key content/product pages, robots.txt, sitemap.xml, and the stale footer URL. See `reports/public-storefront-baseline.json`; rerun with `python3 scripts/audit-public.py`. HTML text counts include hidden/template content and are not proof of visible UI defects.
- Ran Shopify CLI Theme Check; full findings in `reports/theme-check-baseline.json`, paths normalized relative to the project.
- No Lighthouse run, mobile device/keyboard matrix, field Core Web Vitals report, Search Console inspection, email event test, retailer review match, or end-to-end fulfillment test was completed. No conversion, revenue-lift, or speed-score claims are made.

## Prioritized next steps

Effort bands are planning estimates after inputs/access are ready: S = up to one focused day; M = roughly 2–4 days; L = multiple workstreams or external vendor dependency.

| Priority | Work | Evidence / business reason | Owner and dependency | Acceptance criteria | Effort |
| --- | --- | --- | --- | --- | --- |
| P1 | Separate Amazon messaging from Shopify stock rules | Visible sold-out badges and conflicting product schema | Theme developer + operations: approve channel model | Amazon-directed cards/PDPs do not claim 3PL stock is Amazon stock; actual Shopify/staff purchasing still enforces correct inventory | M |
| P1 | Complete slim-can and 4-pack merchandising | Existing active products, incomplete display fields, sample-only tags | Content + ecommerce + operations: approved consumer pack/SKU/retailer mapping | Correct products appear in intended public collections; images, copy, nutrition, destinations, and access rules verified | M |
| P1 | Resolve Klaviyo access and validate existing flows | Embed/form render; app launch requests new data access | Account owner + lifecycle marketer | Existing integration, events, consent, forms, offers, exclusions, and flow statuses tested before activation | M |
| P1 | Map fulfillment and inventory ownership | Cin7 and ShipStation installed; Cin7 launch hits existing-organization gate | Operations/3PL + integration owners | One documented source of truth and order route per channel; existing order traced through stock, fulfillment, tracking, cancellation/return | L |
| P2 | Clean SEO and old navigation | Empty product descriptions in JSON-LD, missing page descriptions, stale preview links | Theme/content + Search Console owner when available | Accurate schema/content, canonical internal links, redirect checks, crawl/index review | M |
| P2 | Reduce verified performance overhead | Global 287 KB JS bundle, 173 KB custom CSS, route-specific assets loaded globally | Theme developer | Repeatable before/after mobile lab and field baselines; fewer unnecessary bytes/execution with relevant flows intact | M |
| P2 | Migrate reviews to Bazaarvoice | Yotpo works on tested PDP; retailer syndication is not yet verified | Ecommerce + Bazaarvoice + retailer contacts | Review export/import reconciled, product matches approved, onsite rendering and retailer destinations verified before Yotpo removal | L |
| P2 | Verify Faire resync | Faire publishing channel present on Peach Slim Can | Wholesale + operations | Product/case mapping and sync direction checked; no duplicate orders or double stock deductions | M |
| P3 | Inventory and retire legacy pages/drafts | Hidden Shogun pages and many historical theme drafts | Content + ecommerce | URL/dependency inventory, retained backup, redirects or intentional retirement, no active campaign links broken | M |

No P0 checkout outage was established. Public PDPs currently function primarily as routes to Amazon/retail, while Shopify also contains staff/sample/wholesale inventory.

## 1. Availability messaging: confirmed problem

On [Variety Packs](https://drinkhalfday.com/collections/variety-packs), **Classic Variety** and **Fruity Variety** visibly display `SOLD OUT`. The Classic Variety PDP still has an Amazon destination. Amazon stock was not checked, so this audit does not assert it is in stock there.

The cause is visible in `snippets/card-product.liquid:182` and `:774`: when a custom badge is absent, `card_product.available == false` produces the Shopify sold-out badge. Products with a custom `NEW`/`BEST SELLER` badge can conceal the same underlying inventory state, making the presentation inconsistent.

The mismatch also reaches search engines. The [Classic Variety PDP](https://drinkhalfday.com/products/classic-variety) emits a Shopify `Offer` of USD 35.99 with `OutOfStock`; its visible main CTA points to Amazon. `sections/main-product.liquid:1053` uses Shopify's `product | structured_data`. Removing badges alone would leave this contradiction.

Recommended implementation: define an explicit merchandising/purchase channel per product (Amazon, retailer-only, Shopify, staff/sample). Use it for badges, CTA destinations, and offer/schema decisions. An Amazon URL is an initial signal, but do not treat all products with blank URLs as ordinary DTC products. Do not manufacture Amazon stock or price values. Preserve native inventory checks in `snippets/buy-buttons.liquid:65` for legitimate Shopify checkout paths and preserve Locksmith access restrictions. Preview/test a single flavor, sold-out variety, retail-only slim can, and staff/sample item before release.

## 2. New content: products exist, readiness is incomplete

Shopify's catalog already contains active **Peach Tea (Slim Can)**, **Tropical Tea (Slim Can)**, **Classic Half & Half (Slim Can)**, and **Strawberry Half & Half (Slim Can)**. Several 24-pack case records with 4-pack naming also exist, including Raspberry, Green, Lemon, Tropical, H&H, and a Peach `6x4` case. These logistics case records must not automatically become consumer 4-pack listings.

[Peach Slim Can admin](https://admin.shopify.com/store/halfday-tonics/products/8335577710792) shows:

- Active, using Default product, published to Online Store, Faire: Sell Wholesale, and TikTok.
- Tagged `sample-only`, and assigned to public-looking collections plus staff/sample collections. This indicates a channel/access decision is needed; it does not prove the tag alone hides the product.
- Display-title metafield says **“Peach Tea (Silm Can)”**; product title itself is spelled correctly.
- Amazon PDP URL is blank. Several theme colors, grid image fields, and icon fields appeared unfilled. Logo reference appears to be a Watermelon-named asset and needs visual review.
- Short detail says **Single 12-Pack • 12 fl oz per can**. Ingredient and comparison references point to existing Peach entries; validate against the new package/formula rather than assuming they match.

The sampled public Shop All grid displays eight established flavors, not these slim-can products. Collection rendering contains Locksmith filtering (`sections/main-collection-product-grid.liquid:164`); inspect those rules and collection membership before changing visibility. No access-control rules were changed.

Prepare a merchandising sheet with consumer pack quantity, sellable unit/case quantity, SKU, UPC/GTIN, ASIN, Walmart/Target product IDs and URLs, channel eligibility, imagery, nutrition, approved claims, product metafields, and collection placement. Audit existing records before adding duplicates. Confirm whether the client wants retail discovery pages, Amazon links, or Shopify checkout for each new format.

## 3. Klaviyo: installed and rendering; flow health unverified

Klaviyo is installed; its app embed is enabled in `config/settings_data.json:161`. The public page includes the Klaviyo loader, and the footer form (`sections/footer.liquid:186`, form `TPsGns`) rendered an email input and `GET 15% OFF` button after asynchronous loading. No signup was submitted. Rendering proves neither consent capture nor event delivery.

Launching Klaviyo from Shopify opened an **Update data access** screen. Requested access includes staff/contributor data, gift card/store-credit data, server pixels, and Online Store editing, among other scopes. That update was not approved. The owner should review the exact scopes or provide access directly to the existing Klaviyo account; then audit flows there.

For the relaunch, inventory current flow status, triggers, filters, list/segment definitions, suppression, sender setup, offer validity, and destinations. Prioritize welcome, browse interest, re-engagement, and replenishment where appropriate. Validate events with a controlled consented test profile and confirm no duplicate collection. Onsite activity and Viewed Product have distinct roles in Klaviyo's tracking model. [Klaviyo onsite tracking](https://help.klaviyo.com/hc/en-us/articles/115005076767)

The footer's first-order discount promise needs to agree with the intended purchase channel and a real redeemable offer. Amazon outbound clicks are not proof of purchases, and Shopify order-triggered flows cannot be assumed to capture Amazon purchases. Keep customer-facing retail marketing separate from staff/sample/wholesale orders. Leave Amazon attribution and Google tracking implementation for the later authorized tracking phase.

## 4. Reviews: retain the working source during migration

The claim that reviews never appear is **not supported by the tested PDP**. Lemon Tea initially had empty review containers, then rendered **two reviews and a 4.5 rating**, including review text. Yotpo is installed, enabled, and referenced in product cards, PDP rating snippets, `sections/Product-review-new.liquid`, and theme CSS.

Before removing Yotpo, audit review coverage across all old/new product IDs, export the review dataset with permitted provenance/media, and reconcile counts and ratings against the import. Avoid collecting two sets of review requests during cutover. Fix undefined `variant` usage in `sections/Product-review-new.liquid:22` if that widget remains during transition; Theme Check flags it.

Bazaarvoice migration requires catalog/product matching, not just a widget replacement. Build GTIN/SKU/brand and retailer-ID mappings separately for can/pack/case formats; confirm which existing reviews are eligible to migrate and syndicate. Bazaarvoice describes product identifier matching as essential to syndication, and Walmart lists Bazaarvoice for its review network. Halfday-specific Walmart and Target eligibility, contracts, product-family rules, and onboarding still need confirmation. [Bazaarvoice data requirements](https://docs.bazaarvoice.com/articles/?_escaped_fragment_=ratings-reviews%2Fxml-schema-and-data-requirements), [Walmart partner page](https://marketplace.walmart.com/solutions-providers/bazaarvoice/)

Acceptance: approved catalog matches, tested onsite widget on desktop/mobile, accessible rendering, no duplicate rating schema, reconciled review totals, successful retailer syndication confirmation, and a rollback/export before removing Yotpo code/app.

## 5. SEO and AEO

Working foundations: the sampled public URLs return HTTP 200 after redirects, canonical tags are present, robots.txt and sitemap.xml are reachable, main PDPs have descriptive page titles/meta descriptions and visible ingredients/benefits, and Organization/Product schema exists. Search visibility and indexing have not been verified in Search Console.

Confirmed cleanup:

- Shop All and Contact returned no meta description. Write useful page-specific descriptions.
- Sampled Lemon, Green, and Classic Variety Product JSON-LD has an empty `description`, despite visible custom metafield content. Align the source product description/schema with factual public copy, and align offers with the actual purchase channel.
- Organization schema contains empty `sameAs` entries; on several content pages its URL changes to that page. Use a stable brand entity and valid profile URLs.
- The footer Flavors link uses `/en-test/products/lemon-iced-tea`; it **redirects successfully** to `/products/lemon-tea`, so it is stale rather than a confirmed 404. Public HTML also contains old `preview_theme_id=140338692296` links. Find their menu/metaobject source and replace with canonical production destinations. Menus/metaobjects are not included in the Git theme snapshot.
- Homepage main message is an H2 beneath a logo H1; several content pages have no textual H1 in the HTTP extract. Review the rendered heading hierarchy, including desktop/mobile duplicates, before changing markup.
- Many images have empty/missing alt text (homepage HTTP sample: 117 images, 7 missing alt, 109 empty). Some are decorative or duplicated sliders. Audit meaningful product/retailer images and link names rather than blindly filling every alt attribute.

AEO work should make approved answers explicit: what Halfday is, fiber/sugar/calories per format, ingredients, caffeine, pack sizes, where to buy, and how retail/Amazon ordering works. Use clear question/answer headings, internal links, stable product identifiers, and visible factual content. Validate claims with the client. Google says no special AI markup is needed; prioritize ordinary discoverability and helpful content rather than an extra “AI SEO” script. [Google AI features guidance](https://developers.google.com/search/docs/appearance/ai-features)

## 6. Speed and maintainability

These are code/HTML measurements, **not compressed transfer bytes or Core Web Vitals**:

| Asset / page | Observed size or behavior |
| --- | --- |
| `assets/custom.js` | 286,789 bytes; jQuery 1.12.4 + Swiper 11.1.10 + custom behavior; 15 `new Swiper` occurrences, including commented code |
| `assets/custom.css` | 173,265 bytes; global |
| `assets/base.css` | 80,725 bytes |
| `assets/find-us.css` | 25,330 bytes, included globally by `layout/theme.liquid:319` |
| Homepage HTML | 387,728 bytes; 22 external script tags before dynamically injected scripts |
| Lemon PDP HTML | 360,315 bytes; 26 external script tags before dynamically injected scripts |

The theme already defers core JS, uses native Shopify sections, and uses responsive image helpers in many places. Preserve those strengths. Opportunities include conditional locator CSS, correctly scoped collection quick-add scripts (`sections/main-collection-product-grid.liquid:10–17` currently includes them outside meaningful conditions), unnecessary cart assets on public Amazon routes, shared card stylesheet duplication, slider initialization only where needed, and reducing jQuery dependence gradually.

Hero code renders separate desktop/mobile images with high fetch priority and uses undefined `img.width` (`sections/Index-top-image-over-text-new.liquid:22–33`). Verify actual network selection and replace with explicit responsive sizing/picture behavior as appropriate. Do not lazy-load the main LCP image. The layout also loads Typekit plus Shopify font declarations/preloads; check actual rendered font use before removing variants. accessiBe is injected globally at `layout/theme.liquid:419`; measure its cost and address accessibility in markup regardless of overlay use.

Recommended sequence: capture three comparable mobile lab runs per representative route, record request/JS/font/image breakdown, obtain Shopify field LCP/INP/CLS where available, change one class of overhead at a time, and repeat relevant measurements. Preserve navigation, product galleries, Amazon CTAs, forms, reviews, store locator, and staff checkout. Shopify recommends minimizing JS, using native browser features, and optimizing resource loading. [Shopify performance guidance](https://shopify.dev/docs/storefronts/themes/best-practices/performance)

Theme Check reports **126 errors / 361 warnings**: 120 missing-translation errors, two dynamic-HTML-tag parse errors, two Locksmith `content_for_header` findings, one invalid section schema, and one unsupported render-filter argument. The dynamic-tag reports may be checker limitations and are not proof of broken live HTML. Triage `snippets/product-variant-options.liquid:70`, `sections/email-signup-banner.liquid:402`, and active routes first. The many unused/undefined-variable warnings deserve targeted cleanup, not a wholesale rewrite or blanket suppression.

## 7. Legacy Shogun and app footprint

No Shogun references were found in the pulled theme's active code; Shopify Pages does contain Shogun-generated bodies in hidden records: Subscription Landing Page, homie, Email Signup, variety pack, Gut Health, Coming Soon, and old our story. The initial page list also contains visible current Subscribe/PTO pages and hidden older promotion/signup pages. Thus Shogun is **legacy page content**, not the identified active theme engine. Hidden status does not establish whether old links/backlinks need redirects.

Create a URL inventory with visibility, current template, owner/campaign use, traffic/backlinks when available, replacement, and redirect decision. Keep current Dawn sections and migrate only content that still serves a purpose. Do not delete legacy theme drafts until compared/backed up and owners confirm no active use.

The installed-app list contains 22 apps, including Klaviyo, Yotpo, Cin7 Core, ShipStation, Stockist, Locksmith, Flow, Forms, and operational/custom integrations. EasyLockdown backup files remain in the theme while Locksmith is active. Removing a backup file may improve maintainability without affecting runtime speed; establish inclusion/dependency first. AfterShip and Bazaarvoice were not visible in that installed-app list; this does not establish whether they are configured externally. Faire is visible as a publishing channel.

## 8. Operations and integration verification plan

**Observed:** Cin7 Core and ShipStation are installed. Opening Cin7 from Shopify returned “A shop with the name 'halfday-tonics' is already connected to Cin7 Core organisation.” This is an access/connection-entry gate, not evidence that existing order sync is broken. Access the existing organization rather than reconnecting or overwriting it.

Shopify contains public retail products, staff/sample products, logistics case SKUs, and negative/zero inventory records. Their quantities are not necessarily Amazon stock. No warehouse-sync success is inferred from an installed app or a stock number.

| System / path | Next evidence to obtain | Pass condition |
| --- | --- | --- |
| Cin7 → Shopify inventory | Existing organization, SKU/unit mappings, location mappings, buffers, last sync, failed jobs, owning process | Known SKU agrees with the approved available-stock calculation and correct location |
| Shopify/Cin7 → ShipStation → 3PL | Determine whether orders enter ShipStation directly or through Cin7; inspect one existing fulfilled order and tracking return | One order/fulfillment owner; no duplicate import; correct tracking/status returned |
| TikTok → AfterShip → Amazon fulfillment | Confirm exact AfterShip product/account and connector, SKU/ASIN mapping, Amazon fulfillment route, exclusions | One route, acknowledged fulfillment, tracking accepted, no duplicate 3PL shipment |
| Faire ↔ Shopify/Cin7 | Existing brand channel/account, inventory and order-sync switches, linked SKU/case quantities, fulfillment-return rules | Correct order and case quantities; single inventory deduction; fulfilled/tracking states reconcile |
| Staff/sample/wholesale | Tag and access rules, pricing/discount rules, allowed warehouse/channel destinations | Protected items stay protected and marketing/retail reporting is not polluted |

Trace existing orders with redacted identifiers first. If a transaction test is needed later, agree a controlled test with operations before placing an order. Include cancellation, partial fulfillment, return, and duplicate/retry cases. Cin7 supports more than one ShipStation connection model, so the route must be inspected rather than assumed. [Cin7 Shopify overview](https://help.core.cin7.com/hc/en-us/articles/9034589848335-Introduction-to-Shopify), [Cin7 ShipStation integration](https://help.core.cin7.com/hc/en-us/articles/9034569837839-ShipStation-Integration)

Faire documents that inventory deductions depend on enabled inventory/order sync and product linking. Verify the existing configuration before a resync so historic orders are not re-imported or counted twice. [Faire order sync](https://www.faire.com/support/articles/37632468706331)

## Inputs needed for the implementation phase

1. Client/content owner: approved slim-can and consumer 4-pack assortment, pack/case definitions, imagery, ingredients/nutrition, retail destinations, and which channels may sell each SKU.
2. Lifecycle owner: existing Klaviyo account access or an owner-reviewed decision on the pending Shopify data-access update; approved offers and intended flow audiences.
3. Operations/3PL: access to the existing Cin7 organization and ShipStation account, AfterShip/TikTok/Amazon fulfillment configuration, Faire sync settings, SKU/location map, and example existing orders.
4. Review owner: Yotpo export permissions, Bazaarvoice onboarding/contact, Walmart/Target identifier and syndication requirements.
5. Optional shared development: desired Git hosting organization/repository. Local Git and Shopify CLI workflows are ready now.

The first implementation batch should address channel-aware availability, complete one slim-can product as the reusable content model, and clean stale navigation/schema. Follow with measured asset reductions and app migrations once their dependencies are verified. GA/GTM/Google Ads stay deferred.
