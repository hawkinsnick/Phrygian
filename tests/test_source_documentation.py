import importlib.util,json,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('reconciliation',R/'scripts/reconcile_source_documentation.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class DocumentationTests(unittest.TestCase):
 def setUp(self):
  self.document=(R/'imports/ud-phrygian-kul-readme.md').read_text();self.ref=json.loads((R/'imports/ud-phrygian-kul.json').read_text())['records']
 def test_replay_and_preserve_reference_layer(self):
  actual=m.reconcile(self.document,self.ref)
  self.assertEqual(actual,json.loads((R/'research/source-documentation-reconciliation-v1.json').read_text()))
  for a in actual['assertions']:
   self.assertFalse(a['canonical_admission_granted']);self.assertFalse(a['independent_epigraphic_review'])
  self.assertEqual(json.loads((R/'data/records.json').read_text()),[])
 def test_missing_tm_reference_rejected(self):
  with self.assertRaises(ValueError):m.reconcile(self.document,[r for r in self.ref if r['trismegistos_id']!='TM1002268'])
 def test_duplicate_documentation_join_rejected(self):
  with self.assertRaises(ValueError):m.reconcile(self.document+'\n| test | 34.2 | TM 1002268 |',self.ref)
 def test_no_guessed_editions(self):
  self.assertEqual(m.reconcile('Undocumented inscription TM1002268 resembles 34.2',self.ref)['assertions'],[])
if __name__=='__main__':unittest.main()
