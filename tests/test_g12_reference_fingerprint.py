import importlib.util,json,shutil,tempfile,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1];s=importlib.util.spec_from_file_location('fingerprint',R/'scripts/audit_g12_reference_fingerprint.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class G12FingerprintTests(unittest.TestCase):
 def test_unique_exact_match_without_promotion(self):
  x=m.build();self.assertEqual(x,json.loads((R/'analysis/g12-reference-fingerprint-audit.json').read_text()));self.assertEqual(x['tm_group_count'],162);self.assertEqual(x['exact_match_count'],1);self.assertEqual(x['exact_match_tm_id'],'TM1001271');self.assertEqual(x['top_ranked_groups'][0]['jaccard_4gram_score'],1.0);self.assertFalse(x['external_catalogue_identity_certified']);self.assertFalse(x['physical_line_alignment_established'])
 def test_candidate_text_mutation_is_rejected(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp)/'repo';shutil.copytree(R,root,ignore=shutil.ignore_patterns('.git','__pycache__'));p=root/'imports/ud-phrygian-kul.json';x=json.loads(p.read_text());next(r for r in x['records'] if r['trismegistos_id']=='TM1001271')['text']+='x';p.write_text(json.dumps(x));
   with self.assertRaises(ValueError):m.build(root)
