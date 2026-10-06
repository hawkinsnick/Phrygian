#!/usr/bin/env python3
import argparse,json,pathlib
R=pathlib.Path(__file__).resolve().parents[1]
FILES={"records":"data/records.json","tm":"research/tm-reconciliation-ledger.json","titus":"research/titus-heading-catalogue.json","disagreements":"research/disagreement-register.json","sources":"data/sources.json"}
def rows(k):
 v=json.loads((R/FILES[k]).read_text(encoding="utf-8"))
 if isinstance(v,list):return v
 for key in ("records","items","sources","headings"): 
  if isinstance(v.get(key),list):return v[key]
 return [v]
p=argparse.ArgumentParser();p.add_argument("resource",choices=FILES);p.add_argument("--text",default="");p.add_argument("--limit",type=int,default=50);a=p.parse_args();q=a.text.casefold();x=[r for r in rows(a.resource) if not q or q in json.dumps(r,ensure_ascii=False).casefold()][:a.limit];print(json.dumps({"resource":a.resource,"records":x,"boundary":"Attributed evidence/reference data only; source dependence and rights remain controlling."},ensure_ascii=False,indent=2))
