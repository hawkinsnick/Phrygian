"""Replay explicit edition/TM joins from licensed upstream documentation."""
import hashlib,json,re
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def reconcile(document,reference):
    rows=[];seen=set()
    for editor,number,tm in re.findall(r'^\|\s*([^|]+?)\s*\|\s*([0-9]+\.[0-9]+)\s*\|\s*TM\s+([0-9]+)\s*\|',document,re.M):
        tm='TM'+tm
        if tm in seen:raise ValueError('duplicate edition/TM assertion')
        seen.add(tm)
        ids=[r['record_id'] for r in reference if r['trismegistos_id']==tm]
        if not ids:raise ValueError('documented TM ID absent from pinned reference layer')
        rows.append({'trismegistos_id':tm,'editor':editor,'edition_number':number,
                     'reference_record_ids':ids,'period':'New Phrygian',
                     'period_evidence':'Upstream README introduces this table as New Phrygian additions.',
                     'source_locator':'README Edition table','canonical_admission_granted':False,
                     'independent_epigraphic_review':False})
    return {'format':'phrygian-source-documentation-reconciliation-v1',
            'documentation_path':'imports/ud-phrygian-kul-readme.md',
            'documentation_sha256':hashlib.sha256(document.encode()).hexdigest(),
            'assertions':rows,'explicit_tm_joins':len(rows),
            'canonical_admissions':0,'boundary':'Explicit upstream table joins only; no fuzzy text matching, physical identity certification or independent collation. Source editions remain attribution targets.'}
if __name__=='__main__':
    print(json.dumps(reconcile((R/'imports/ud-phrygian-kul-readme.md').read_text(),json.loads((R/'imports/ud-phrygian-kul.json').read_text())['records']),ensure_ascii=False,indent=2))
