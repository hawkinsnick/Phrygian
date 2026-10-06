#!/usr/bin/env python3
import argparse,csv,json,pathlib
R=pathlib.Path(__file__).resolve().parents[1];p=argparse.ArgumentParser();p.add_argument("layer",choices=["canonical","tm-reference"]);p.add_argument("format",choices=["json","jsonl","csv"]);p.add_argument("output");a=p.parse_args();src="data/records.json" if a.layer=="canonical" else "research/tm-reconciliation-ledger.json";v=json.loads((R/src).read_text());rows=v if isinstance(v,list) else v.get("records",[]);out=pathlib.Path(a.output)
if a.format=="json":out.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
elif a.format=="jsonl":out.write_text("".join(json.dumps(x,ensure_ascii=False)+"\n" for x in rows),encoding="utf-8")
else:
 with out.open("w",encoding="utf-8",newline="") as f:
  w=csv.DictWriter(f,fieldnames=["record_json"]);w.writeheader()
  for x in rows:w.writerow({"record_json":json.dumps(x,ensure_ascii=False)})
m={"layer":a.layer,"format":a.format,"records":len(rows),"canonical":a.layer=="canonical","losses":[] if a.format!="csv" else ["Nested structure serialized into record_json."],"rights":"See research/rights-source-matrix.json; export does not relicense components."};out.with_suffix(out.suffix+".manifest.json").write_text(json.dumps(m,indent=2)+"\n")
