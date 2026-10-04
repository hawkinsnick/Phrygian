"""Lossless offline replay of the pinned UD reference, never epigraphic admission."""
import argparse
import hashlib
import json
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
COLUMNS = ('id','form','lemma','upos','xpos','feats','head','deprel','deps','misc')

def parse_conllu(text):
    sentences = []
    seen = set()
    for block in re.split(r'\n\s*\n', text.strip()):
        comments, rows = [], []
        for line in block.splitlines():
            if line.startswith('#'):
                comments.append(line)
                continue
            fields = line.split('\t')
            if len(fields) != 10:
                raise ValueError('CoNLL-U row must have ten columns')
            if not re.fullmatch(r'\d+(?:[-.]\d+)?', fields[0]):
                raise ValueError('invalid token ID')
            rows.append(dict(zip(COLUMNS, fields)))
        metadata = {}
        for line in comments:
            match = re.fullmatch(r'# (sent_id|text) = (.*)', line)
            if match:
                if match[1] in metadata:
                    raise ValueError('duplicate sentence metadata')
                metadata[match[1]] = match[2]
        sid = metadata.get('sent_id', '')
        if not re.fullmatch(r'TM\d+[a-z]?-\d+', sid) or sid in seen or 'text' not in metadata:
            raise ValueError('missing/invalid/duplicate sentence identity or source text')
        seen.add(sid)
        ids = [r['id'] for r in rows]
        if len(set(ids)) != len(ids):
            raise ValueError('duplicate token ID')
        words = [r for r in rows if r['id'].isdigit()]
        if [int(r['id']) for r in words] != list(range(1, len(words)+1)):
            raise ValueError('nonconsecutive integer token IDs')
        ref_diagnostics = []
        for row in words:
            if not row['head'].isdigit() or int(row['head']) > len(words):
                raise ValueError('head outside sentence')
            refs = [x[4:] for x in row['misc'].split('|') if x.startswith('Ref=')]
            if refs != [sid+'-'+row['id']]:
                ref_diagnostics.append({'token_id':row['id'],'expected_ref':sid+'-'+row['id'],'reported_refs':refs})
        surface = ''.join(r['form'] + ('' if 'SpaceAfter=No' in r['misc'].split('|') else ' ') for r in words).rstrip(' ')
        sentences.append({'sent_id':sid,'trismegistos_id':sid.split('-')[0],
                          'source_text':metadata['text'],'comments':comments,'rows':rows,
                          'token_ref_diagnostics':ref_diagnostics,
                          'integer_token_count':len(words),'reconstructed_token_surface':surface,
                          'token_surface_equals_source_text':surface == metadata['text'],
                          'independent_epigraphic_review':False,'canonical_admission_granted':False})
    return sentences

def replay(root=ROOT):
    root = Path(root)
    source = root/'data/upstream/ud-phrygian-kul/xpg_kul-ud-test.conllu'
    raw = source.read_bytes()
    # A Git blob hash includes its type and length, unlike SHA-256 byte hashes.
    blob_sha = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    reference = json.loads((root/'imports/ud-phrygian-kul.json').read_text())
    if blob_sha != reference['source_blob_sha']:
        raise ValueError('pinned source Git blob hash mismatch')
    sentences = parse_conllu(raw.decode('utf-8'))
    projected = [{'record_id':'UD-'+s['sent_id'],'source_id':reference['source_id'],
                  'source_locator':s['sent_id'],'trismegistos_id':s['trismegistos_id'],
                  'text':s['source_text'],'token_count':s['integer_token_count'],
                  'source_file':reference['source_file'],'source_blob_sha':blob_sha,
                  'source_assertion':True,'independent_epigraphic_review':False} for s in sentences]
    if projected != reference['records']:
        raise ValueError('reference JSON does not exactly replay from pinned CoNLL-U')
    ledger = json.loads((root/'research/tm-reconciliation-ledger.json').read_text())
    groups = {}
    for row in projected:
        groups.setdefault(row['trismegistos_id'],[]).append(row)
    if len(ledger['records']) != len(groups) or len({r['trismegistos_id'] for r in ledger['records']}) != len(groups):
        raise ValueError('ledger identity inventory mismatch')
    for item in ledger['records']:
        rows = groups.get(item['trismegistos_id'],[])
        if item['source_sentence_ids'] != [r['record_id'] for r in rows] or item['sentence_count'] != len(rows) or item['token_count'] != sum(r['token_count'] for r in rows):
            raise ValueError('ledger sentence/token mapping mismatch')
        if item['canonical_epigraphic_admission'] or item['independent_epigraphic_review']:
            raise ValueError('reference ledger cannot grant epigraphic admission')
    counts = {'sentences':len(sentences),'tokens':sum(s['integer_token_count'] for s in sentences),'distinct_trismegistos_ids':len(groups)}
    if counts != reference['counts']:
        raise ValueError('declared reference counts do not replay')
    return {'format':'phrygian-lossless-reference-replay-v1','source_path':source.relative_to(root).as_posix(),
            'source_sha256':hashlib.sha256(raw).hexdigest(),'source_blob_sha':blob_sha,
            'counts':counts,'reference_json_exact_replay':True,'tm_ledger_exact_replay':True,
            'token_ref_diagnostic_count':sum(len(s['token_ref_diagnostics']) for s in sentences),
            'token_surface_difference_count':sum(not s['token_surface_equals_source_text'] for s in sentences),
            'boundary':'Source text and token segmentation are distinct upstream representations. Differences are diagnostic, not silent corrections or independent witnesses.',
            'sentences':[{'sent_id':s['sent_id'],'integer_token_count':s['integer_token_count'],
                          'token_rows_sha256':hashlib.sha256(json.dumps(s['rows'],ensure_ascii=False,separators=(',',':')).encode()).hexdigest(),
                          'token_ref_diagnostics':s['token_ref_diagnostics'],
                          'surface_difference':None if s['token_surface_equals_source_text'] else {'source_text':s['source_text'],'reconstructed_token_surface':s['reconstructed_token_surface']},
                          'canonical_admission_granted':False} for s in sentences]}

if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--check',action='store_true',help='require committed replay artifact to match current inputs')
    args = p.parse_args()
    result = replay()
    output = json.dumps(result,ensure_ascii=False,indent=2)+'\n'
    if args.check:
        if (ROOT/'analysis/reference-replay.json').read_text() != output:
            raise SystemExit('Reference replay artifact is stale')
        print('Pinned UD bytes, 203 sentence projections and TM ledger replay exactly.')
    else:
        print(output,end='')
