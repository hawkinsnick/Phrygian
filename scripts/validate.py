from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parents[1]
p=json.loads((ROOT/"project.json").read_text())
c=json.loads((ROOT/"schemas/interoperability-contract.json").read_text())
r=json.loads((ROOT/"data/records.json").read_text())
assert p["project"]=="Phrygian"
assert c["contract"]=="hawkinsnick-epigraphic-corpus-interoperability"
assert c["version"]=="1.1.0"
assert c["principles"]["uncertainty_preserved"] is True
assert isinstance(r,list)
print("Phrygian scaffold validation passed.")
