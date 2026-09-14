"""Run offline with python3 -B scripts/test-wave-3-catalog.py."""
import copy
import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('catalog', Path(__file__).with_name('validate-wave-3-catalog.py'))
catalog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(catalog)


class CatalogChecks(unittest.TestCase):
    def setUp(self):
        self.row = {
            'faire_product_id': 'example', 'title': 'Example',
            'faire_sku': 'ALIAS', 'shopify_sku': 'SKU',
            'mapping_status': 'observed_not_approved', 'gtin': '10850064555230',
        }

    def test_gtin_text_and_checksum(self):
        for value in ('6291041500213', '10850064555230', '012345678905'):
            self.assertTrue(catalog.valid_gtin(value), value)
        for value in ('10850064555231', '00000000000000', 10850064555230, '1.085006455523e13', '１２３４５６７８', '123'):
            self.assertFalse(catalog.valid_gtin(value), value)

    def test_alias_is_preserved_and_pending_is_not_approval(self):
        result = catalog.validate({'products': [self.row]})
        self.assertEqual(result['errors'], [])
        self.assertEqual(result['approved_rows'], 0)
        self.assertTrue(any('SKU alias' in x for x in result['attention']))

    def test_approval_requires_evidence_and_valid_quantities(self):
        self.row['mapping_status'] = 'approved'
        self.assertTrue(catalog.validate({'products': [self.row]})['errors'])
        self.row.update(shopify_product_id='1', units_per_sellable=12, sellable_per_case=1,
                        cin7_sku='SKU', approved_by='Example owner', approved_at='2026-09-14',
                        approval_evidence='Example signed mapping')
        self.assertEqual(catalog.validate({'products': [self.row]})['approved_rows'], 1)
        for invalid in (True, 0, -1, 1.5):
            self.row['units_per_sellable'] = invalid
            result = catalog.validate({'products': [self.row]})
            self.assertTrue(result['errors'])
            self.assertEqual(result['approved_rows'], 0)

    def test_duplicate_and_unlinked_identity_conflicts(self):
        self.assertTrue(catalog.validate({'products': [self.row, copy.deepcopy(self.row)]})['errors'])
        self.assertTrue(catalog.validate({'products': [self.row], 'unlinked': [{'faire_product_id': 'example'}]})['errors'])

    def test_malformed_records_report_errors(self):
        for data in ([], {}, {'products': []}, {'products': [None]},
                     {'products': [{'faire_product_id': [], 'shopify_sku': {}}]},
                     {'products': [self.row], 'unlinked': {}},
                     {'products': [self.row], 'unlinked': [None]}):
            self.assertTrue(catalog.validate(data)['errors'])


if __name__ == '__main__':
    unittest.main()
