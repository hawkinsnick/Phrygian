from pathlib import Path
import json, sys
p=Path(sys.argv[1])
m=json.loads(p.read_text(encoding="utf-8"))
assert m["source_policy"] == {
 "attribution_required": True,
 "rights_review_required": True,
 "redistribute_only_if_permitted": True
}
assert m["interoperability"] == {
 "contract":"hawkinsnick-epigraphic-corpus-interoperability",
 "version":"1.1.0"
}
print("Factory manifest safeguards passed.")
