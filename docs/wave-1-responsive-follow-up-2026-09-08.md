# Wave 1 responsive follow-up

Development branch: `djh/wave-1-responsive-follow-up`. Preview theme: **142755430600**. This CSS refinement follows the authorized release at `a99ed7f` and is not included in live main.

## Completed

The tablet release audit exposed an existing cramped flavor selector. At 1024px, Watermelon's rendered label needed 85px inside a 61.33px tile and extended beyond its link toward the panel edge. Raspberry also exceeded its tile width.

For widths 990–1280px, use three flavor columns with the existing 8px gap and 13px labels. At 1024px each tile is now 84.44px; at 990px it is 80.66px. All eight labels fit their links within normal subpixel rounding. No JavaScript, markup, product content, destination or app configuration changed. The panel gains a third row and purchase buttons move down accordingly; this is intentional to keep flavor choices readable.

## Verification

- Browser checks at **990, 1024, 1280, 1281, 1440 and 390px**: no horizontal page overflow. The new three-column/13px rule applies only through 1280px; the 1281px and 1440px four-column/14px display and 390px three-column/14px display are preserved.
- Keyboard selection of Watermelon opens the correct product. The existing Variety Packs tab displays six variety options on that page; selecting Classic Variety with Enter opens its product. These are the existing tab and link behaviors.
- The change is three CSS lines including its explanatory comment. No new dependencies, animation or runtime work. It is a CRO/readability correction; no LCP gain is claimed.
- Theme Check remains 122 inherited errors / 391 warnings with zero added offenses. The final CSS downloaded from Shopify development matches the local file byte for byte. Git whitespace checks pass. The release comparison remains separately preserved in `reports/wave-1-release-regression.json` against the previous production baseline.

## Remaining Wave 1 dependencies

- Agentready's last verified Apply attempt failed with `unsupported_field`; protected-resource exclusion still needs an output-enabled test after the app fixes. Its output and embed remain off in the released settings.
- App ownership and supported Signifyd scoping need confirmation before changing shared integrations. Preserve Yotpo pending Bazaarvoice migration.
- Approved consumer-pack facts, imagery and retailer destinations are still needed for 4-pack/slim-can merchandising. Existing case records are not substitutes.
- Health/nutrition claims, Subscribe page purpose and retired-content destinations need editorial decisions.
- LCP remains variable. The released reduction in initial video transfer and improved review spacing are verified; a consistent LCP or field-CWV gain is not established.

GA/Ads remain deferred, GTM excluded and Klaviyo activation in Wave 2.
