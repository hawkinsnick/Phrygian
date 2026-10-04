import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('new_primary', ROOT/'scripts/reconcile_new_primary.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class PrimaryComparisonTests(unittest.TestCase):
    def test_published_checkpoint(self):
        actual = module.build()
        self.assertEqual(actual, json.loads((ROOT/'analysis/new-primary-comparison.json').read_text()))
        rows = {r['trismegistos_id']: r for r in actual['records']}
        self.assertFalse(rows['TM1002268']['exact_after_line_break_fold'])
        self.assertEqual(rows['TM1002268']['fragment_word_count'], 3)
        self.assertFalse(rows['TM1002268']['general_formula_exact_after_whitespace_fold'])
        self.assertTrue(rows['TM1002268']['general_formula_matches_after_terminal_comma_omission'])
        self.assertFalse(rows['TM1002268']['object_specific_reading_support'])
        self.assertTrue(rows['TM1002269']['exact_after_line_break_fold'])
        self.assertEqual(rows['TM1002269']['printed_edition_line_count'], 2)

    def mutated_dossier(self, mutate):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for rel in module.PATHS:
                dest = root/rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT/rel, dest)
            path = root/module.PATHS[0]
            dossier = json.loads(path.read_text())
            mutate(dossier)
            path.write_text(json.dumps(dossier))
            with self.assertRaises(ValueError):
                module.build(root)

    def test_damaged_letter_cannot_be_normalized_away(self):
        self.mutated_dossier(lambda d: d['records'][1].update(
            primary_excerpt=d['records'][1]['primary_excerpt'].replace('μ̣', 'μ')))

    def test_alternative_reading_cannot_disappear(self):
        self.mutated_dossier(lambda d: d['records'][1].pop('competing_reading'))

    def test_upstream_number_cannot_become_primary_catalogue_number(self):
        self.mutated_dossier(lambda d: d['records'][1].update(ud_number='2'))

    def test_general_formula_cannot_be_changed_to_fragment(self):
        self.mutated_dossier(lambda d: d['records'][0]['general_formula'].update(
            excerpt=d['records'][0]['primary_excerpt']))

    def test_unregistered_pdf_is_rejected_before_extraction(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'wrong.pdf'
            path.write_bytes(b'Unregistered source bytes')
            with self.assertRaises(ValueError):
                module.verify_source_pdf(path)


if __name__ == '__main__':
    unittest.main()
