#!/usr/bin/env python3
import json,pathlib
R=pathlib.Path(__file__).resolve().parents[1]
req=["research/rights-source-matrix.json","research/disagreement-register.json","research/residual-blocker-ledger.json","research/source-dependence-graph.json","research/tm-coverage-benchmark.json","research/tm-reconciliation-ledger.json","research/browser-sources.json","scripts/research_api.py","scripts/export_research_layer.py"]
missing=[p for p in req if not (R/p).exists()];assert not missing,missing
records=json.loads((R/"data/records.json").read_text());tm=json.loads((R/"research/tm-reconciliation-ledger.json").read_text());pre=json.loads((R/"research/pre-expert-maximum.json").read_text())
assert len(records)==0
assert tm["counts"]["distinct_tm_ids"]==162 and tm["counts"]["source_sentences"]==203 and tm["counts"]["tokens"]==1921
assert tm["counts"]["canonical_admissions"]==0 and tm["counts"]["independently_reviewed"]==0
print(json.dumps({"status":"PASS","canonical_records":0,"tm_reference_ids":162,"reference_sentences":203,"tokens":1921,"controls":len(req),"boundary":"Method parity does not equal critical-edition completeness."}))
