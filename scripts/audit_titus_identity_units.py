"""Classify TITUS heading labels without converting them into inscription counts."""
import argparse,hashlib,json,re
from collections import Counter,defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE='research/titus-heading-catalogue.json'

def build(root=ROOT):
 root=Path(root);raw=(root/SOURCE).read_bytes();catalogue=json.loads(raw)
 classes=Counter();groups=defaultdict(list);exceptions=[]
 patterns=[('integer',r'\d+'),('letter_suffix',r'\d+[A-Za-z]'),('roman_subdivision',r'\d+[a-z][IV]+'),('qualified',r'\d+\(\?\)'),('range',r'\d+-\d+'),('trailing_punctuation',r'\d+\.')]
 for entry in catalogue['entries']:
  label=entry['inscription_label_reported'];kind=next((name for name,pattern in patterns if re.fullmatch(pattern,label)),'other');classes[kind]+=1
  match=re.match(r'(\d+)',label)
  if match:groups[(entry['period_label_reported'],entry['provenance_label_reported'],match.group(1))].append(label)
  if kind in {'qualified','range','trailing_punctuation','other'}:exceptions.append({'source_heading_id':entry['source_heading_id'],'label':label,'class':kind})
 multi=[{'period_label_reported':k[0],'provenance_label_reported':k[1],'numeric_stem':k[2],'headings':v} for k,v in groups.items() if len(v)>1]
 return {'format':'phrygian-titus-identity-unit-audit-v1','source_path':SOURCE,'source_sha256':hashlib.sha256(raw).hexdigest(),'heading_count':len(catalogue['entries']),'label_class_counts':dict(sorted(classes.items())),'numeric_stem_group_count':len(groups),'multi_heading_numeric_stem_group_count':len(multi),'multi_heading_numeric_stem_groups':multi,'exceptional_labels':exceptions,'certified_physical_inscription_count':None,'boundary':'Heading labels, numeric stems, ranges, letter suffixes and Roman subdivisions are source representation units. This mechanical audit does not decide which headings share a stone, text, copy, face, line, edition or physical inscription; it never expands the range 1-7 into seven records.'}

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();output=json.dumps(build(),ensure_ascii=False,indent=2)+'\n';target=ROOT/'analysis/titus-identity-unit-audit.json'
 if a.check:
  if target.read_text(encoding='utf-8')!=output:raise SystemExit('TITUS identity-unit audit stale')
  print('TITUS identity-unit classes replay without physical-count inference.')
 else:print(output,end='')
