import json,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
class PreExpertMaximum(unittest.TestCase):
 def test_boundary(self):
  x=json.loads((R/"research/pre-expert-maximum.json").read_text())
  s=json.loads((R/"analysis/current-status.json").read_text())
  ref=json.loads((R/"imports/ud-phrygian-kul.json").read_text())
  self.assertIn(x["target"],{"PRE_EXPERT_MAXIMUM","LINEAR_A_METHOD_PARITY_PRE_EXPERT_MAXIMUM"})
  self.assertEqual(len(ref["records"]),203)
  self.assertEqual(ref["counts"]["distinct_trismegistos_ids"],162)
  self.assertEqual(s["canonical_epigraphic_record_count"],0)
  self.assertEqual(s["committed_reference_record_count"],203)
  self.assertTrue(x["remaining_nonexpert_work"])
  self.assertTrue(x["human_only_boundary"])
  ledger=json.loads((R/"research/tm-reconciliation-ledger.json").read_text())
  self.assertEqual(ledger["counts"]["distinct_tm_ids"],162)
  self.assertEqual(ledger["counts"]["source_sentences"],203)
  self.assertEqual(ledger["counts"]["canonical_admissions"],0)
  self.assertEqual(sum(r["sentence_count"] for r in ledger["records"]),203)
  self.assertTrue(all(r["authoritative_edition_locator"] is None for r in ledger["records"]))
if __name__=="__main__":unittest.main()
