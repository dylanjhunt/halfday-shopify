# Wave 3 review package

September 14, 2026. These are observed configurations and implementation specifications. No integration settings, orders, inventory or review data have been changed.

- [Operations audit and route acceptance tests](operations-audit-2026-09-14.md): Faire settings, historical order trace, access gates and proposed corrections.
- [Catalog worksheet](catalog-map.json): all 12 linked Faire products, existing SKU aliases and five unlinked legacy entries. Unknown values remain null.
- [Yotpo maintenance](yotpo-maintenance.md): active retained-provider work and QA. The [migration packet](reviews-migration-plan.md) is historical and inactive.
- [Combined Wave 2/3 status](../waves-2-3-progress-2026-09-14.md): completed work and required inputs.

## Validate the worksheet

From the repository root:

```sh
python3 -B scripts/validate-wave-3-catalog.py docs/wave-3/catalog-map.json
python3 -B scripts/test-wave-3-catalog.py
```

The checker runs offline. It checks required keys, duplicate IDs, GTIN format/check digit, quantity types and approval evidence. It flags SKU aliases for preservation instead of rewriting them. Exit 0 means the worksheet passes static checks, not that products are approved to sync or import. `approved_rows` must remain zero until approved identifiers, quantities, Cin7 mapping and evidence are recorded. A valid GTIN checksum does not establish brand ownership or whether it identifies a can, consumer pack or logistics case.

Keep GTINs and product IDs as strings. Do not remove leading zeros or substitute guessed values for nulls. Do not put customer/reviewer exports or credentials in the worksheet. This is an internal working schema, not an accepted Cin7, Faire or Bazaarvoice import format.

## Next execution order after access

1. Trace the existing Faire order in Cin7, ShipStation and Faire. Establish who owns inventory and fulfillment updates before proposing configuration edits.
2. Confirm pack/case quantities and each legacy listing's disposition; complete the missing catalog evidence and rerun validation.
3. Maintain Yotpo and verify its current product mapping, review rendering and request eligibility. No migration/export is needed merely to retain it. Keep retailer syndication separately deferred.
4. Preview theme changes in a dedicated unpublished theme, including the local Yotpo price-reference repair. Compare review interactions, empty/loading states and mobile/desktop visuals.
5. Present the exact integration, review-maintenance and theme release changes for approval. Test orders, live sends, resyncs, app removal and main publication remain separate actions.
