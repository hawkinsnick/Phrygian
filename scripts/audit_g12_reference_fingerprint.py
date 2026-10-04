"""Rank the licensed G-12 reading against all UD TM groups without certifying identity."""
import argparse, json, re, unicodedata
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def normalized(s):
 s=''.join(c for c in unicodedata.normalize('NFD',s.lower()) if unicodedata.category(c)!='Mn')
 s=s.replace('ś','s').replace('ṣ','s').replace('vac','')
 return ''.join(re.findall('[a-z]+',s))
def grams(s,n=4):return {s[i:i+n] for i in range(max(0,len(s)-n+1))}
def build(root=ROOT):
 root=Path(root);comparison=json.loads((root/'analysis/g12-edition-comparison.json').read_text());records=json.loads((root/'imports/ud-phrygian-kul.json').read_text())['records'];primary=normalized(' '.join(x['literal_text'] for x in comparison['primary_edition_lines']));groups=defaultdict(str)
 for row in records:groups[row['trismegistos_id']]+=normalized(row.get('text',''))
 pg=grams(primary);rank=[]
 for tm,text in groups.items():
  tg=grams(text);union=pg|tg;rank.append({'trismegistos_id':tm,'normalized_character_count':len(text),'shared_4gram_count':len(pg&tg),'jaccard_4gram_score':round(len(pg&tg)/len(union),12) if union else 0,'exact_normalized_text_match':text==primary})
 rank.sort(key=lambda x:(x['jaccard_4gram_score'],x['shared_4gram_count'],x['trismegistos_id']),reverse=True);exact=[x for x in rank if x['exact_normalized_text_match']]
 if [x['trismegistos_id'] for x in exact]!=['TM1001271']:raise ValueError('G-12 exact-match uniqueness changed')
 return {'format':'phrygian-g12-reference-fingerprint-audit-v1','algorithm':{'normalization':'Unicode NFD; remove combining marks; lowercase; map ś and ṣ to s; remove literal vac; retain ASCII letters only; concatenate in source order','comparison':'set Jaccard similarity of character 4-grams plus exact normalized-string equality'},'primary_normalized_character_count':len(primary),'tm_group_count':len(groups),'exact_match_count':len(exact),'exact_match_tm_id':'TM1001271','top_ranked_groups':rank[:10],'external_catalogue_identity_certified':False,'physical_line_alignment_established':False,'independent_witness_added':False,'boundary':'Exact normalized transcription correspondence makes the candidate digital-text join reproducible. UD cites the publisher edition and is therefore dependent evidence. This audit does not inspect or certify the Trismegistos object page, equate seven physical lines with ten UD sentences, validate the reading, or admit a canonical record.'}
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();output=json.dumps(build(),ensure_ascii=False,indent=2)+'\n';target=ROOT/'analysis/g12-reference-fingerprint-audit.json'
 if a.check:
  if target.read_text()!=output:raise SystemExit('G-12 fingerprint audit stale')
  print('G-12 uniquely matches TM1001271 reference text without identity certification.')
 else:print(output,end='')
