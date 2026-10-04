"""Compare attributed primary excerpts to the preserved dependent UD records."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATHS = ['research/new-phrygian-primary-dossier.json',
         'research/source-inspection-2026-10-02.json', 'imports/ud-phrygian-kul.json']


def build(root=ROOT):
    root = Path(root)
    dossier, inspection, ud = [json.loads((root / p).read_text()) for p in PATHS]
    records = {r['record_id']: r for r in ud['records']}
    joins = {a['trismegistos_id']: a for a in inspection['assertions']}
    rows = []
    for item in dossier['records']:
        source = records[item['reference_record_id']]
        join = joins[item['trismegistos_id']]
        if (source['trismegistos_id'] != item['trismegistos_id'] or
                join['editor'] != item['edition'] or join['edition_number'] != item['ud_number']):
            raise ValueError('Primary dossier/upstream join drift')
        excerpt = item['primary_excerpt']
        # Only remove the edition's explicit end-of-line hyphen and fold whitespace.
        folded = ' '.join(excerpt.replace('-\n', '').split())
        target = ' '.join(source['text'].split())
        row = {'trismegistos_id': item['trismegistos_id'],
               'reference_record_id': source['record_id'],
               'ud_text_sha256': hashlib.sha256(source['text'].encode()).hexdigest(),
               'primary_excerpt_sha256': hashlib.sha256(excerpt.encode()).hexdigest(),
               'status': item['reading_status'],
               'exact_after_line_break_fold': folded == target,
               'independent_epigraphic_review': False,
               'canonical_admission': False}
        if item['trismegistos_id'] == 'TM1002269':
            if folded != target:
                raise ValueError('Short published reading no longer matches preserved UD text')
            row['printed_edition_line_count'] = len(excerpt.splitlines())
            row['catalogue_number'] = item['primary_catalogue_number']
            row['survey_inventory_number'] = item['survey_inventory_number']
            if not item.get('competing_reading', {}).get('condition'):
                raise ValueError('Competing restoration lost')
        elif item['trismegistos_id'] == 'TM1002268':
            fragment = excerpt.replace('[…]', '').strip()
            row['fragment_is_contiguous_in_ud'] = fragment in target
            words = iter(target.split())
            row['fragment_words_occur_in_ud_order'] = all(word in words for word in fragment.split())
            row['fragment_word_count'] = len(fragment.split())
            row['ud_whitespace_word_count'] = len(target.split())
            formula = item['general_formula']['excerpt']
            row['general_formula_exact_after_whitespace_fold'] = ' '.join(formula.split()) == target
            row['general_formula_matches_after_terminal_comma_omission'] = ' '.join(formula.split()).removesuffix(',') == target
            row['general_formula_printed_page'] = item['general_formula']['printed_page']
            row['object_specific_reading_support'] = False
            if not row['general_formula_matches_after_terminal_comma_omission']:
                raise ValueError('General-formula correspondence changed; reinspect source')
            if folded == target or not row['fragment_words_occur_in_ud_order']:
                raise ValueError('Anfosso fragment discrepancy changed; reinspect evidence')
        else:
            raise ValueError('Unexpected primary comparison')
        rows.append(row)
    if sorted(r['trismegistos_id'] for r in rows) != ['TM1002268', 'TM1002269']:
        raise ValueError('Primary comparison set changed')
    return {'format': 'phrygian-new-primary-comparison-v1',
            'input_hashes': {p: hashlib.sha256((root/p).read_bytes()).hexdigest() for p in PATHS},
            'normalization': 'Remove only hyphen immediately followed by newline; fold whitespace. Preserve case, underdots, brackets, spelling and punctuation.',
            'records': rows,
            'boundary': 'Replay verifies project excerpts against pinned UD data; it cannot refetch or authenticate publication bytes, collate stones, resolve the discrepant join or certify external identities.'}


def verify_source_pdf(path, root=ROOT):
    """Verify a privately acquired source copy without redistributing it."""
    item = json.loads((Path(root)/PATHS[0]).read_text())['records'][0]
    data = Path(path).read_bytes()
    if len(data) != item['source_file']['bytes'] or hashlib.sha256(data).hexdigest() != item['source_file']['sha256']:
        raise ValueError('Source PDF differs from inspected bytes; reinspect before updating fingerprint')
    for page, excerpt in [(item['general_formula']['pdf_page_one_based'], item['general_formula']['excerpt']),
                          (item['pdf_page_one_based'], item['primary_excerpt'])]:
        text = subprocess.check_output(['pdftotext', '-f', str(page), '-l', str(page), '-layout', str(path), '-'], text=True)
        if ' '.join(excerpt.split()) not in ' '.join(text.split()):
            raise ValueError('Attributed excerpt absent from registered PDF page')
    return {'source_sha256': item['source_file']['sha256'], 'verified_pdf_pages': [18, 19],
            'boundary': 'Byte identity and embedded-text presence only; no independent witness or catalogue certification.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--source-pdf', type=Path, help='Privately acquired Anfosso PDF; requires Poppler pdftotext')
    args = parser.parse_args()
    result = build()
    if args.source_pdf:
        print(json.dumps(verify_source_pdf(args.source_pdf), indent=2))
    if args.check:
        if json.loads((ROOT/'analysis/new-primary-comparison.json').read_text()) != result:
            raise SystemExit('New primary comparison stale')
        print('Short edition match and Anfosso fragment discrepancy verified; no independent admission.')
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))
