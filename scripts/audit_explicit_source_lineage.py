"""Count only TM groups with an explicit source-level edition lineage."""
import argparse,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PATHS=['research/source-inspection-2026-10-02.json','analysis/g12-reference-fingerprint-audit.json','imports/ud-phrygian-kul.json']
def build(root=ROOT):
 root=Path(root);inspection=json.loads((root/PATHS[0]).read_text());g12=json.loads((root/PATHS[1]).read_text());ud=json.loads((root/PATHS[2]).read_text())
 ids=sorted({r['trismegistos_id'] for r in ud['records']})
 rows=[{'trismegistos_id':x['trismegistos_id'],'edition':x['editor'],'edition_number':x['edition_number'],'evidence_locator':x['source_locator'],'lineage_status':'UPSTREAM_DOCUMENTATION_EXPLICIT_DEPENDENT'} for x in inspection['assertions']]
 if g12['exact_match_count']!=1 or g12['exact_match_tm_id']!='TM1001271':raise ValueError('G-12 exact correspondence changed')
 rows.append({'trismegistos_id':'TM1001271','edition':'Oreshko & Alagöz 2023','edition_number':'G-12','evidence_locator':'UD README G-12 edition note plus licensed publisher text fingerprint','lineage_status':'PRIMARY_TEXT_TO_DEPENDENT_UD_EXPLICIT'})
 if sorted(x['trismegistos_id'] for x in rows)!=['TM1001271','TM1002268','TM1002269'] or not set(x['trismegistos_id'] for x in rows)<=set(ids):raise ValueError('explicit lineage join changed')
 return {'format':'phrygian-explicit-source-lineage-audit-v1','input_hashes':{p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in PATHS},'tm_group_count':len(ids),'explicit_edition_lineage_count':len(rows),'edition_lineage_not_record_specific_count':len(ids)-len(rows),'independently_collated_lineage_count':0,'canonical_admission_count':0,'records':sorted(rows,key=lambda x:x['trismegistos_id']),'boundary':'Only three TM groups currently have record-specific edition lineage explicit in inspected project evidence. The remaining groups may derive principally from sources named by UD, but a corpus-level statement is not a record-level join. Explicit lineage documents dependence; it does not independently validate a reading, period, object identity or provenance.'}
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();out=json.dumps(build(),ensure_ascii=False,indent=2)+'\n';target=ROOT/'analysis/explicit-source-lineage-audit.json'
 if a.check:
  if json.loads(target.read_text())!=build():raise SystemExit('Explicit source-lineage audit stale')
  print('Three explicit edition lineages remain distinct from 159 unjoined TM groups.')
 else:print(out,end='')
