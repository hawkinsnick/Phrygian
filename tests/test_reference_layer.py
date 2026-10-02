import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class ReferenceLayerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ref = json.loads((ROOT / "imports/ud-phrygian-kul.json").read_text())
        cls.status = json.loads((ROOT / "analysis/current-status.json").read_text())
        cls.canonical = json.loads((ROOT / "data/records.json").read_text())

    def test_declared_counts_match_records(self):
        records = self.ref["records"]
        self.assertEqual(len(records), self.ref["counts"]["sentences"])
        self.assertEqual(sum(r["token_count"] for r in records), self.ref["counts"]["tokens"])
        self.assertEqual(len({r["trismegistos_id"] for r in records}), self.ref["counts"]["distinct_trismegistos_ids"])

    def test_reference_is_not_independent_review(self):
        self.assertTrue(all(r["source_assertion"] is True for r in self.ref["records"]))
        self.assertTrue(all(r["independent_epigraphic_review"] is False for r in self.ref["records"]))

    def test_canonical_layer_remains_gated(self):
        self.assertEqual(self.canonical, [])
        self.assertIn("independently_verified_critical_edition", self.status["blocked_claims"])

if __name__ == "__main__":
    unittest.main()
