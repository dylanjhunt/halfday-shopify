# Wave 1 handoff

Checked September 10, 2026. Core theme implementation and the agreed contrast work are audited and ready for closeout. This is not a claim that every change is live or that all app/content dependencies are resolved.

## Release status

- Main is `2893a6f`, including merged PR #1: performance and responsive improvements, native controls, keyboard focus, image cleanup and prior SEO/link repairs.
- [PR #2](https://github.com/dylanjhunt/halfday-shopify/pull/2) is still **open** at `c380c42`. It contains the final contrast treatment and verified brand-only Agentready embed, plus audit/decision records. Its implementation passed 15 route comparisons and targeted desktop/mobile checks, with no new Theme Check findings. It has not been released to main.
- Seven native Shopify redirects are live and verified. The Peach Product Title typo was separately approved, saved and verified on September 9.
- Agentready Apply has a durable 34/34 receipt. Accurate brand/policy Agent JSON is prepared in development. Product/collection approvals and JSON-LD remain off. The live embed remains off as of the last September 9 readback; PR #2's release will enable the reviewed brand-only embed.

## Items carried forward

| Item | Current disposition | Blocks Wave 2 preparation? |
| --- | --- | --- |
| Strawberry calories, tea base, sugar specificity, caffeine and homepage nutrition range | Await the team’s approved facts. Exact locations and wording are in `docs/product-facts-for-leslie.md` on PR #2. Do not invent replacement values. | No; avoid disputed claims in draft emails. |
| Signifyd and Postscript ownership | Dylan is confirming. No removal or unsupported script scoping. | Postscript decision gates SMS changes, not email planning. |
| HelloFresh/Subscribe campaign status and Cranberry disposition | Dylan is confirming. Preserve existing destinations pending decisions. | Campaign-specific changes wait; general newsletter planning can proceed. |
| Search Console | Dylan is requesting access. Preserve overlapping article URLs until traffic/link evidence is available. | No. |
| Agentready expansion | Brand-only delivery verified. Contact settings UI inconsistency remains reported; product offers, JSON-LD ownership and MCP/ACP catalog behavior still need separate verification. | No. Do not present full catalog activation as complete. |
| accessiBe and health articles | Keep accessiBe and leave the articles unchanged, per Dylan. | No; these are resolved scope decisions. |
| Existing product setup | Products already exist. Preserve assortment and staff/sample rules; no catalog rebuild is required. | No. |

Wave 1 can be tracked as **implementation complete, final release and external follow-ups outstanding**. The remaining work is recorded rather than silently removed from scope. Wave 2 preparation can proceed without waiting for every response.

## Development handoff

Wave 2 preparation branch: `djh/wave-2-klaviyo-prep`, based on main `2893a6f`. It contains planning documents only. The shared development theme `142755430600` currently carries PR #2's unpublished changes. Do not push this branch's older theme files over it. After PR #2 merges, update/rebase the Wave 2 branch onto main and read back the development theme before the next theme edit or upload. Main remains the live deployment branch.
