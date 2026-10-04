import importlib.util,json,shutil,tempfile,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1];s=importlib.util.spec_from_file_location('lineage',R/'scripts/audit_explicit_source_lineage.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class ExplicitLineageTests(unittest.TestCase):
 def test_only_record_specific_lineage_is_counted(self):
  x=m.build();self.assertEqual(x,json.loads((R/'analysis/explicit-source-lineage-audit.json').read_text()));self.assertEqual(x['tm_group_count'],162);self.assertEqual(x['explicit_edition_lineage_count'],3);self.assertEqual(x['edition_lineage_not_record_specific_count'],159);self.assertEqual(x['independently_collated_lineage_count'],0)
 def test_g12_identity_drift_is_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d)/'repo';shutil.copytree(R,root,ignore=shutil.ignore_patterns('.git','__pycache__'));p=root/'analysis/g12-reference-fingerprint-audit.json';x=json.loads(p.read_text());x['exact_match_tm_id']='TM0';p.write_text(json.dumps(x));
   with self.assertRaises(ValueError):m.build(root)
if __name__=='__main__':unittest.main()
