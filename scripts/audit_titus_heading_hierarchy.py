"""Derive only explicit co-listed TITUS heading-parent relations."""
import argparse, hashlib, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "research/titus-heading-catalogue.json"

def build(root=ROOT):
    root = Path(root)
    raw = (root / SOURCE).read_bytes()
    entries = json.loads(raw)["entries"]
    by_scope = {}
    for entry in entries:
        key = (entry["period_label_reported"], entry["provenance_label_reported"])
        by_scope.setdefault(key, {})[entry["inscription_label_reported"]] = entry["source_heading_id"]
    edges = []
    for (period, provenance), labels in by_scope.items():
        for child, child_id in labels.items():
            parent = None
            relation = None
            if re.fullmatch(r"\d+[a-z][IV]+", child):
                parent = re.sub(r"[IV]+$", "", child)
                relation = "roman_subdivision_of_colisted_letter_heading"
            elif re.fullmatch(r"\d+[A-Za-z]", child):
                parent = re.sub(r"[A-Za-z]$", "", child)
                relation = "suffix_heading_of_colisted_integer_heading"
            if parent in labels:
                edges.append({"period_label_reported": period, "provenance_label_reported": provenance,
                              "parent_label": parent, "parent_heading_id": labels[parent],
                              "child_label": child, "child_heading_id": child_id, "relation": relation})
    edges.sort(key=lambda x: x["child_heading_id"])
    counts = {kind: sum(e["relation"] == kind for e in edges) for kind in
              ["suffix_heading_of_colisted_integer_heading", "roman_subdivision_of_colisted_letter_heading"]}
    return {"format": "phrygian-titus-heading-hierarchy-audit-v1", "source_path": SOURCE,
            "source_sha256": hashlib.sha256(raw).hexdigest(), "explicit_colisted_parent_edge_count": len(edges),
            "relation_counts": counts, "edges": edges, "certified_physical_relationship_count": None,
            "boundary": "Edges encode label morphology only where the proposed parent heading is independently present in the same TITUS period/provenance scope. They do not assert that parent and child are parts of one stone, one inscription, one text, one face, or one edition. No absent parent is synthesized and ranges are not expanded."}

if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__); p.add_argument("--check", action="store_true"); a = p.parse_args()
    output = json.dumps(build(), ensure_ascii=False, indent=2) + "\n"
    target = ROOT / "analysis/titus-heading-hierarchy-audit.json"
    if a.check:
        if target.read_text(encoding="utf-8") != output: raise SystemExit("TITUS heading-hierarchy audit stale")
        print("Explicit co-listed TITUS heading hierarchy replays without physical inference.")
    else: print(output, end="")
