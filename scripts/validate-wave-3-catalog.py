"""Offline checks for the internal Wave 3 catalog map. Never syncs or imports.

GTIN format/checksum checks do not verify ownership, package identity, formula,
review-family eligibility or a retailer's acceptance. Missing data stays missing.
"""
import argparse
import json
import re
from pathlib import Path


def valid_gtin(value):
    if not isinstance(value, str) or not re.fullmatch(r'(?:[0-9]{8}|[0-9]{12}|[0-9]{13}|[0-9]{14})', value):
        return False
    if set(value) == {'0'}:
        return False
    total = sum(int(d) * (3 if i % 2 == 0 else 1) for i, d in enumerate(reversed(value[:-1])))
    return int(value[-1]) == (-total) % 10


def validate(data):
    errors, attention = [], []
    identifiers, sku_targets, gtins = set(), {}, {}
    if not isinstance(data, dict):
        return {'errors': ['catalog must be an object'], 'attention': [], 'approved_rows': 0}
    products = data.get('products', [])
    if not isinstance(products, list) or not products:
        return {'errors': ['products must be a nonempty list'], 'attention': [], 'approved_rows': 0}
    approved = 0
    for i, row in enumerate(products, 1):
        if not isinstance(row, dict):
            errors.append(f'row {i}: product must be an object')
            continue
        row_errors_before = len(errors)
        ident = row.get('faire_product_id')
        label = ident if isinstance(ident, str) and ident.strip() else f'row {i}'
        if not isinstance(ident, str) or not ident.strip() or ident in identifiers:
            errors.append(f'{label}: missing or duplicate Faire product identifier')
        if isinstance(ident, str):
            identifiers.add(ident)
        for field in ('title', 'faire_sku', 'shopify_sku'):
            if not isinstance(row.get(field), str) or not row[field].strip():
                errors.append(f'{label}: missing {field}')
        if row.get('faire_sku') != row.get('shopify_sku'):
            attention.append(f'{label}: SKU alias needs preserving; do not rebuild this match by SKU equality')
        sku = row.get('shopify_sku')
        if isinstance(sku, str) and sku.strip():
            if sku in sku_targets:
                attention.append(f'{label}: Shopify SKU also linked by {sku_targets[sku]}; inspect duplicate catalog intent')
            sku_targets[sku] = label
        value = row.get('gtin')
        if value is not None:
            if not valid_gtin(value):
                errors.append(f'{label}: GTIN format/check digit invalid; preserve as text and confirm source')
            else:
                normalized = value.zfill(14)
                if normalized in gtins:
                    attention.append(f'{label}: GTIN also appears on {gtins[normalized]}; verify duplicate/package mapping')
                gtins[normalized] = label
        for field in ('units_per_sellable', 'sellable_per_case'):
            value = row.get(field)
            if value is not None and (type(value) is not int or value < 1):
                errors.append(f'{label}: {field} must be a positive whole number or null')
        status = row.get('mapping_status')
        if status not in ('observed_not_approved', 'approved', 'excluded'):
            errors.append(f'{label}: unknown mapping_status')
        if status == 'approved':
            needed = ['shopify_product_id', 'gtin', 'units_per_sellable', 'sellable_per_case', 'cin7_sku', 'approved_by', 'approved_at', 'approval_evidence']
            missing = [f for f in needed if row.get(f) in (None, '')]
            if missing:
                errors.append(f'{label}: cannot mark approved without {", ".join(missing)}')
            elif len(errors) == row_errors_before:
                approved += 1
        elif status == 'observed_not_approved':
            attention.append(f'{label}: observed mapping only; package/operations approval remains open')
    unlinked = data.get('unlinked', [])
    if not isinstance(unlinked, list):
        errors.append('unlinked must be a list')
        unlinked = []
    for i, row in enumerate(unlinked, 1):
        if not isinstance(row, dict):
            errors.append(f'unlinked row {i}: product must be an object')
            continue
        ident = row.get('faire_product_id')
        if not isinstance(ident, str) or not ident.strip() or ident in identifiers:
            errors.append(f'{ident}: unlinked ID missing or also present elsewhere')
        if isinstance(ident, str):
            identifiers.add(ident)
    return {'rows': len(products), 'unlinked_rows': len(unlinked), 'approved_rows': approved,
            'errors': errors, 'attention': attention,
            'limit': 'Static checks only. No sync, product authenticity, retailer acceptance or review-family approval is established.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', type=Path)
    args = parser.parse_args()
    result = validate(json.loads(args.path.read_text()))
    print(json.dumps(result, indent=2))
    raise SystemExit(1 if result['errors'] else 0)
