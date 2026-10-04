import importlib.util,json,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location('titus',R/'scripts/inspect_titus_catalogue.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class TitusCatalogueTests(unittest.TestCase):
 def test_catalogue_is_discovery_metadata_only(self):
  x=json.loads((R/'research/titus-heading-catalogue.json').read_text())
  self.assertEqual(x['heading_count'],len(x['entries']));self.assertEqual(len({r['source_heading_id'] for r in x['entries']}),len(x['entries']))
  self.assertEqual(x['period_heading_counts'],{'Old-Phryg.':194,'Mys.':7,'Neo-Phryg.':104})
  for r in x['entries']:
   self.assertIsNone(r['tm_identity']);self.assertFalse(r['canonical_admission_granted']);self.assertNotIn('reading',r)
 def test_nested_text_is_never_emitted(self):
  raw=b'<span id=h2>Period: Old-Phryg.<A NAME="old"></A></sPAN><span id=h3>Provenance: M<A NAME="m"></A></sPAN><span id=h4>Inscription: 1a<A NAME="m1a"></A></sPAN><span id=anopht16>PRIVATE_READING</span>'
  x=m.inspect(raw);self.assertEqual(x['heading_count'],1);self.assertNotIn('PRIVATE_READING',json.dumps(x))
  with self.assertRaises(ValueError):m.inspect(raw+raw)
