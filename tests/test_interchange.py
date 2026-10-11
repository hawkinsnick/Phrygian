import copy,importlib.util,json,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];s=importlib.util.spec_from_file_location('interchange',ROOT/'scripts/build_interchange.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class InterchangeTests(unittest.TestCase):
 def fixture(self,root):
  for p in ['imports/ud-phrygian-kul.json','research/k01-catalogue-concordance.json','research/identity-graph.json']:
   out=root/p;out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes((ROOT/p).read_bytes())
 def test_committed_replay_and_complete_reference_roundtrip(self):
  m.replay();d=m.build();x=json.loads(d[m.OUTPUTS[2]]);self.assertEqual(x['coverage']['reference_sentence_records'],203);self.assertEqual(x['coverage']['distinct_source_tm_ids'],162);self.assertEqual(x['coverage']['reference_tokens'],1921);self.assertEqual(x['coverage']['canonical_reading_admissions'],0)
 def test_duplicate_source_sentence_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   r=Path(d);self.fixture(r);p=r/'imports/ud-phrygian-kul.json';x=json.loads(p.read_text());x['records'].append(copy.deepcopy(x['records'][0]));p.write_text(json.dumps(x))
   with self.assertRaisesRegex(ValueError,'duplicate'):m.build(r)
 def test_rights_and_independent_review_promotion_rejected(self):
  for mutation in ['license','review']:
   with tempfile.TemporaryDirectory() as d:
    r=Path(d);self.fixture(r);p=r/'imports/ud-phrygian-kul.json';x=json.loads(p.read_text())
    if mutation=='license':x['license']='NOASSERTION'
    else:x['records'][0]['independent_epigraphic_review']=True
    p.write_text(json.dumps(x))
    with self.assertRaises(ValueError):m.build(r)
 def test_source_blob_drift_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   r=Path(d);self.fixture(r);p=r/'imports/ud-phrygian-kul.json';x=json.loads(p.read_text());x['records'][0]['source_blob_sha']='unverified';p.write_text(json.dumps(x))
   with self.assertRaisesRegex(ValueError,'pin'):m.build(r)
 def test_graph_rejects_dangling_and_unproven_certain_identity(self):
  graph=json.loads(m.build()[m.OUTPUTS[1]]);e=next(x for x in graph['edges'] if x['edge_id'].startswith('PHR-INTEROP-'));e['object']='TM:invented'
  with self.assertRaisesRegex(ValueError,'dangling'):m.validate_graph(graph)
  graph=json.loads(m.build()[m.OUTPUTS[1]]);e=next(x for x in graph['edges'] if x['edge_id'].startswith('PHR-INTEROP-'));e['predicate']='same_as';e['assertion_status']='CERTAIN'
  with self.assertRaisesRegex(ValueError,'automatic certain'):m.validate_graph(graph)
 def test_graph_requires_namespace_and_evidence(self):
  for bad in ['namespace','evidence']:
   graph=json.loads(m.build()[m.OUTPUTS[1]])
   if bad=='namespace':graph['nodes'][0]['id']='unqualified'
   else:graph['edges'][0]['evidence_locator']=''
   with self.assertRaises(ValueError):m.validate_graph(graph)
 def test_k01_toc_label_and_factual_promotion_rejected(self):
  for mutation in ['label','promotion','duplicate']:
   with tempfile.TemporaryDirectory() as d:
    r=Path(d);self.fixture(r);p=r/'research/k01-catalogue-concordance.json';x=json.loads(p.read_text())
    if mutation=='label':x['records'][-1]['inscription_fragment_labels']=['IX']
    elif mutation=='promotion':x['records'][0]['critical_reading_admitted']=True
    else:x['records'].append(copy.deepcopy(x['records'][0]))
    p.write_text(json.dumps(x))
    with self.assertRaisesRegex(ValueError,'K01'):m.build(r)
 def test_negative_label_assertion_retained_and_no_new_physical_object(self):
  graph=json.loads(m.build()[m.OUTPUTS[1]]);self.assertTrue(any(e['predicate']=='not_same_as' and e['subject']=='edition_siglum:OIP135-XI' for e in graph['edges']));old=json.loads((ROOT/'research/identity-graph.json').read_text());self.assertEqual([n for n in graph['nodes'] if n['type']=='physical_object'],[n for n in old['nodes'] if n['type']=='physical_object'])
 def test_k01_denominators_and_unplaced_fragment_preserved(self):
  d=json.loads((ROOT/'research/k01-catalogue-concordance.json').read_text());self.assertEqual(len(d['records']),8);self.assertEqual(len({x for r in d['records'] for x in r['identification_numbers']}),14);self.assertTrue(all(r['physical_object_count'] is None and not r['critical_reading_admitted'] for r in d['records']));self.assertEqual(d['records'][-1]['inscription_fragment_labels'],['XI']);self.assertEqual(d['excluded_fragment_label']['label'],'IX');self.assertEqual(d['records'][-1]['placement_status'],'UNPLACED_POSSIBLE_INSCRIPTION');self.assertTrue(any(x['status']=='COUNT_POLICY_UNRESOLVED' for x in d['source_disagreements']))
if __name__=='__main__':unittest.main()
