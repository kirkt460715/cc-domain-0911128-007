import json
import unittest
from pathlib import Path


class StudyInputTests(unittest.TestCase):
    def test_domain_references_and_units(self):
        data=json.loads((Path(__file__).resolve().parents[1]/'fixtures/study-input.json').read_text())
        from equipment_domain.catalog import Catalog
        Catalog(data['document'])
        p=data['study']
        self.assertEqual(set(p['dimensions']),set(p['bounds']))
        self.assertLessEqual(sum(v[0] for v in p['bounds'].values()),1)
        self.assertGreaterEqual(sum(v[1] for v in p['bounds'].values()),1)
