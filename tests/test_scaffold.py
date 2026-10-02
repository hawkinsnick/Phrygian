import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

class ScaffoldTests(unittest.TestCase):
    def test_project(self):
        p=json.loads((ROOT/"project.json").read_text())
        self.assertEqual(p["record_unit"],"source_attributed_inscription_reading")

    def test_empty_records_are_explicit(self):
        self.assertEqual(json.loads((ROOT/"data/records.json").read_text()),[])

if __name__=="__main__":
    unittest.main()
