import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def test_project():
    p=json.loads((ROOT/"project.json").read_text())
    assert p["record_unit"]=="source_attributed_inscription_reading"
def test_empty_records_are_explicit():
    assert json.loads((ROOT/"data/records.json").read_text())==[]
