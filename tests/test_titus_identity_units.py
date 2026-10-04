import importlib.util,json,shutil,tempfile,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location('units',R/'scripts/audit_titus_identity_units.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class TitusIdentityUnitTests(unittest.TestCase):
 def test_exact_source_label_classes_replay(self):
  x=m.build();self.assertEqual(x,json.loads((R/'analysis/titus-identity-unit-audit.json').read_text(encoding='utf-8')))
  self.assertEqual(x['heading_count'],305);self.assertEqual(x['numeric_stem_group_count'],272);self.assertEqual(x['multi_heading_numeric_stem_group_count'],12)
  self.assertEqual(x['label_class_counts'],{'integer':263,'letter_suffix':33,'qualified':1,'range':1,'roman_subdivision':5,'trailing_punctuation':2});self.assertIsNone(x['certified_physical_inscription_count'])
 def test_range_and_qualifier_are_not_silently_normalized(self):
  labels={(e['label'],e['class']) for e in m.build()['exceptional_labels']};self.assertIn(('1-7','range'),labels);self.assertIn(('11(?)','qualified'),labels)
 def test_changed_heading_invalidates_committed_audit(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp)/'repo';shutil.copytree(R,root,ignore=shutil.ignore_patterns('.git','__pycache__'));p=root/'research/titus-heading-catalogue.json';x=json.loads(p.read_text(encoding='utf-8'));x['entries'][0]['inscription_label_reported']='1-8';p.write_text(json.dumps(x),encoding='utf-8');self.assertNotEqual(m.build(root),m.build())
