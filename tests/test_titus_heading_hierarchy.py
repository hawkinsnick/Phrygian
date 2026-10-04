import importlib.util, json, shutil, tempfile, unittest
from pathlib import Path
R = Path(__file__).resolve().parents[1]
s = importlib.util.spec_from_file_location("hierarchy", R / "scripts/audit_titus_heading_hierarchy.py")
m = importlib.util.module_from_spec(s); s.loader.exec_module(m)

class TitusHeadingHierarchyTests(unittest.TestCase):
    def test_exact_explicit_edges_replay(self):
        x = m.build()
        self.assertEqual(x, json.loads((R / "analysis/titus-heading-hierarchy-audit.json").read_text()))
        self.assertEqual(x["explicit_colisted_parent_edge_count"], 23)
        self.assertEqual(x["relation_counts"], {"suffix_heading_of_colisted_integer_heading": 18, "roman_subdivision_of_colisted_letter_heading": 5})
        self.assertIsNone(x["certified_physical_relationship_count"])
    def test_absent_parent_is_not_synthesized(self):
        x = m.build(); pairs = {(e["provenance_label_reported"], e["parent_label"], e["child_label"]) for e in x["edges"]}
        self.assertIn(("M", "1d", "1dI"), pairs); self.assertNotIn(("W", "5", "5a"), pairs)
    def test_deleted_parent_removes_edges(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "repo"; shutil.copytree(R, root, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            p = root / "research/titus-heading-catalogue.json"; x = json.loads(p.read_text())
            x["entries"] = [e for e in x["entries"] if e["source_heading_id"] != "Phryg._Old-Phryg._M_1d"]
            p.write_text(json.dumps(x)); self.assertEqual(m.build(root)["explicit_colisted_parent_edge_count"], 21)
