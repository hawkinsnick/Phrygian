"""Extract heading identifiers only from a lawfully inspected local TITUS HTML file.

No inscription readings, translations, images or source commentary are emitted.
Heading counts include subparts/alternate headings and are not physical objects.
"""
import argparse,hashlib,json,re
from collections import Counter
from html import unescape
from pathlib import Path
URL='https://titus.uni-frankfurt.de/texte/etcs/phrygian/phrygt.htm'
def inspect(raw):
 text=raw.decode('utf-8');period=None;provenance=None;entries=[];seen=set()
 for level,body in re.findall(r'<span id=h([234])>(.*?)</sPAN>',text,re.S|re.I):
  anchor=re.search(r'<A NAME="([^"]+)"',body,re.I)
  if not anchor:raise ValueError('heading anchor missing')
  label=unescape(re.sub(r'<[^>]*>','',body)).replace('\xa0','').strip()
  if level=='2':period=label.removeprefix('Period: ');provenance=None
  elif level=='3':provenance=label.removeprefix('Provenance: ')
  else:
   if not period or anchor[1] in seen:raise ValueError('missing period or duplicate heading anchor')
   seen.add(anchor[1]);entries.append({'source_heading_id':anchor[1],
    'period_label_reported':period,'provenance_label_reported':provenance,
    'inscription_label_reported':label.removeprefix('Inscription: '),
    'url':URL+'#'+anchor[1], 'tm_identity':None,'canonical_admission_granted':False,
    'independent_epigraphic_review':False})
 return {'format':'phrygian-titus-heading-catalogue-v1','source_url':URL,'source_sha256':hashlib.sha256(raw).hexdigest(),
  'heading_count':len(entries),'period_heading_counts':dict(Counter(e['period_label_reported'] for e in entries)),
  'redistribution_scope':'Identifier/heading metadata only; full source HTML and inscription readings are not redistributed.',
  'boundary':'Source headings include subdivisions and alternatives. No unique-object total, TM join, exhaustive discovery or independent witness count is implied.',
  'entries':entries}
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('source',type=Path);a=p.parse_args();print(json.dumps(inspect(a.source.read_bytes()),ensure_ascii=False,indent=2))
