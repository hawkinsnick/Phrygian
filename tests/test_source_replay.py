import importlib.util,json,shutil,tempfile,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def module(name):
 s=importlib.util.spec_from_file_location(name,R/'scripts'/f'{name}.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
replay=module('replay_reference');g12=module('reconcile_g12')
class ReplayTests(unittest.TestCase):
 def test_committed_outputs_replay(self):
  self.assertEqual(replay.replay(),json.loads((R/'analysis/reference-replay.json').read_text()))
  self.assertEqual(g12.reconcile(),json.loads((R/'analysis/g12-edition-comparison.json').read_text()))
 def test_upstream_anomalies_are_retained_not_repaired(self):
  x=replay.replay();self.assertEqual(x['token_ref_diagnostic_count'],12)
  self.assertEqual(x['token_surface_difference_count'],6)
  parsed=replay.parse_conllu((R/'data/upstream/ud-phrygian-kul/xpg_kul-ud-test.conllu').read_text())
  a=next(s for s in parsed if s['sent_id']=='TM757149a-1')
  self.assertEqual(a['rows'][0]['misc'],'Ref=TM757149a-1-2')
  self.assertFalse(a['canonical_admission_granted'])
 def test_primary_line_units_and_markup_survive(self):
  x=g12.reconcile();self.assertEqual(len(x['primary_edition_lines']),7)
  self.assertEqual(x['ud_candidate_sentence_count'],10)
  self.assertTrue(x['primary_edition_lines'][3]['superscript_spans'])
  self.assertIn('<sup>',x['primary_edition_lines'][3]['source_html'])
  self.assertFalse(x['physical_line_alignment_established'])
 def test_duplicate_sentence_and_malformed_columns_rejected(self):
  raw=(R/'data/upstream/ud-phrygian-kul/xpg_kul-ud-test.conllu').read_text();first=raw.split('\n\n')[0]
  with self.assertRaises(ValueError):replay.parse_conllu(first+'\n\n'+first)
  with self.assertRaises(ValueError):replay.parse_conllu(first.replace('\t',' ',1))
 def test_mutated_source_and_reference_and_ledger_rejected(self):
  for relative in ['data/upstream/ud-phrygian-kul/xpg_kul-ud-test.conllu','imports/ud-phrygian-kul.json','research/tm-reconciliation-ledger.json','data/source-evidence/g12-belleten-2023-text.html']:
   with tempfile.TemporaryDirectory() as tmp:
    root=Path(tmp)/'repo';shutil.copytree(R,root,ignore=shutil.ignore_patterns('.git','__pycache__'))
    p=root/relative
    if relative.endswith('conllu') or relative.endswith('html'):p.write_bytes(p.read_bytes()+b' ')
    else:
     x=json.loads(p.read_text())
     if relative.startswith('imports'):x['records'][0]['text']+='?'
     else:x['records'][0]['source_sentence_ids']=[]
     p.write_text(json.dumps(x))
    with self.assertRaises(ValueError):(g12.reconcile if relative.endswith('html') else replay.replay)(root)
