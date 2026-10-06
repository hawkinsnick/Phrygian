#!/usr/bin/env python3
import json, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
GRAPH=ROOT/"research"/"identity-graph.json"
ALLOWED_STATUS={"CERTAIN","SOURCE_ASSERTED","PROJECT_RECONCILED","PROBABLE","DISPUTED","REJECTED","UNKNOWN"}
REQUIRED={"edge_id","subject","predicate","object","assertion_status","authority","evidence_locator","checked_date"}

def main():
    data=json.loads(GRAPH.read_text(encoding="utf-8"))
    nodes={n["id"] for n in data.get("nodes",[])}
    errors=[]
    seen=set()
    for e in data.get("edges",[]):
        missing=REQUIRED-set(e)
        if missing: errors.append(f"{e.get('edge_id','?')}: missing {sorted(missing)}")
        if e.get("edge_id") in seen: errors.append(f"duplicate edge_id {e.get('edge_id')}")
        seen.add(e.get("edge_id"))
        if e.get("assertion_status") not in ALLOWED_STATUS: errors.append(f"{e.get('edge_id')}: bad status")
        if e.get("subject") not in nodes: errors.append(f"{e.get('edge_id')}: missing subject node")
        if e.get("object") not in nodes: errors.append(f"{e.get('edge_id')}: missing object node")
        if e.get("subject")==e.get("object"): errors.append(f"{e.get('edge_id')}: self edge")
    if errors:
        print("\n".join(errors)); return 1
    print(f"identity graph OK: {len(nodes)} nodes, {len(seen)} provenance-bearing edges")
    return 0
if __name__=="__main__": sys.exit(main())
