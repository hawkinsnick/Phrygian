#!/usr/bin/env python3
"""Loss-aware interchange of the frozen reference view; never admit canonical texts."""
import argparse,copy,hashlib,json,re
from pathlib import Path
from xml.etree import ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];TEI='http://www.tei-c.org/ns/1.0';XML='http://www.w3.org/XML/1998/namespace'
OUTPUTS=('interchange/epidoc/ud-reference.xml','research/interoperability-identity-graph.json','interchange/export-manifest.json')
def digest(b):return hashlib.sha256(b).hexdigest()
def encode(d):return (json.dumps(d,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
def node(parent,tag,text=None,**attrs):
 x=ET.SubElement(parent,'{'+TEI+'}'+tag,attrs);x.text=text;return x
def validate_graph(graph):
 ids=[x['id'] for x in graph['nodes']]
 if len(ids)!=len(set(ids)):raise ValueError('duplicate identity node')
 allowed={'project_record','physical_object','text_bearing_surface','text','edition_assertion','place','museum_collection','bibliographic_work','external_catalogue_record','image_or_drawing'}
 for x in graph['nodes']:
  if ':' not in x['id'] or x['type'] not in allowed:raise ValueError('invalid identity namespace/type')
 seen=set();types={'same_as','probably_same_as','not_same_as','part_of','surface_of','text_on','edition_of','derived_from','located_at','found_at','held_by','published_as','catalogued_as','supersedes'};statuses={'CERTAIN','SOURCE_ASSERTED','PROJECT_RECONCILED','PROBABLE','DISPUTED','REJECTED','UNKNOWN'}
 for e in graph['edges']:
  if not all(e.get(k) for k in ['edge_id','subject','predicate','object','assertion_status','authority','evidence_locator','checked_date']):raise ValueError('missing identity provenance')
  if e['edge_id'] in seen:raise ValueError('duplicate identity edge')
  seen.add(e['edge_id'])
  if e['subject'] not in ids or e['object'] not in ids:raise ValueError('dangling identity edge')
  if e['subject']==e['object'] or e['predicate'] not in types or e['assertion_status'] not in statuses:raise ValueError('invalid identity assertion')
  if e['edge_id'].startswith('PHR-INTEROP-') and (e['predicate']=='same_as' or e['assertion_status']=='CERTAIN'):raise ValueError('automatic certain identity prohibited')
 return True
def build(root=ROOT):
 root=Path(root);paths=['imports/ud-phrygian-kul.json','research/k01-catalogue-concordance.json','research/identity-graph.json'];raw={p:(root/p).read_bytes() for p in paths};source=json.loads(raw[paths[0]]);k01=json.loads(raw[paths[1]]);graph=copy.deepcopy(json.loads(raw[paths[2]]));rows=source['records']
 if source['license']!='CC-BY-SA-4.0':raise ValueError('unsupported reference rights')
 ids=[r['record_id'] for r in rows]
 if len(set(ids))!=len(ids) or any(not re.fullmatch(r'[A-Za-z_][A-Za-z0-9_.-]*',x) for x in ids):raise ValueError('duplicate/invalid reference identifier')
 if any(r['independent_epigraphic_review'] is not False or r['source_assertion'] is not True or r['source_blob_sha']!=source['source_blob_sha'] for r in rows):raise ValueError('unsupported reference evidence promotion/pin')
 cats=k01['records']
 if len(cats)!=8 or {r['catalogue_number'] for r in cats}!={str(x) for x in range(13,21)} or len({r['record_id'] for r in cats})!=8:raise ValueError('invalid K01 catalogue coverage')
 if any(r['critical_reading_admitted'] is not False or r['independently_reviewed'] is not False or r['physical_object_count'] is not None for r in cats):raise ValueError('K01 metadata evidence promotion prohibited')
 if next(r for r in cats if r['catalogue_number']=='20')['inscription_fragment_labels']!=['XI'] or any('IX' in r['inscription_fragment_labels'] for r in cats):raise ValueError('K01 excluded/discrepant fragment label')
 ET.register_namespace('',TEI);tei=ET.Element('{'+TEI+'}TEI',{'{'+XML+'}id':'Phrygian-UD-reference'});h=node(tei,'teiHeader');fd=node(h,'fileDesc');ts=node(fd,'titleStmt');node(ts,'title','Phrygian frozen UD linguistic reference interchange');pub=node(fd,'publicationStmt');node(pub,'publisher','Phrygian corpus project');avail=node(pub,'availability');node(avail,'licence','UD-derived reference content: CC BY-SA 4.0. No project restriction supersedes upstream share-alike.',target='https://creativecommons.org/licenses/by-sa/4.0/');sd=node(fd,'sourceDesc');b=node(sd,'bibl');node(b,'ref',source['source_repository'],target='https://github.com/'+source['source_repository']);node(b,'idno',source['source_blob_sha'],type='git-blob');node(b,'note',source['caveat']);text=node(tei,'text');body=node(text,'body');div=node(body,'div',type='edition',subtype='source-attributed-derivative-reference')
 existing={x['id'] for x in graph['nodes']}
 def add(n,t,label):
  if n not in existing:graph['nodes'].append({'id':n,'type':t,'label':label});existing.add(n)
 def edge(s,p,o,loc,authority):
  graph['edges'].append({'edge_id':'PHR-INTEROP-'+str(len(graph['edges'])+1).zfill(4),'subject':s,'predicate':p,'object':o,'assertion_status':'SOURCE_ASSERTED','authority':authority,'evidence_locator':loc,'checked_date':'2026-10-11'})
 ud='bibliography:UD-Phrygian-KUL';add(ud,'bibliographic_work',source['source_repository'])
 for i,row in enumerate(rows):
  d=node(div,'div',type='textpart',subtype='ud-source-sentence',**{'{'+XML+'}id':row['record_id']});node(d,'ab',row['text'],type='attributed-reference-text');node(d,'note',json.dumps(row,ensure_ascii=False,sort_keys=True,separators=(',',':')),type='native-record-json');n='project:'+row['record_id'];add(n,'project_record',row['record_id']);tm='TM:'+row['trismegistos_id'].removeprefix('TM');add(tm,'external_catalogue_record',row['trismegistos_id']);loc='imports/ud-phrygian-kul.json#/records/'+str(i);edge(n,'derived_from',ud,loc,'UD-Phrygian-KUL source attribution');edge(n,'catalogued_as',tm,loc,'UD source TM identifier; not physical-object certification')
 inventory='excavation_inventory:KERKENES-K03.168';add(inventory,'external_catalogue_record','Kerkenes K03.168; publication inventory label')
 for i,row in enumerate(k01['records']):
  n='project:'+row['record_id'];add(n,'project_record',row['record_id']);cat='edition_siglum:OIP135-CAT-'+row['catalogue_number'];add(cat,'external_catalogue_record','OIP135 cat.'+row['catalogue_number']);loc='research/k01-catalogue-concordance.json#/records/'+str(i);edge(n,'catalogued_as',cat,loc,'OIP135 p.'+str(row['evidence'][0]['printed_page'])+' and p.79');edge(n,'published_as','publication:OIP135',loc,'OIP135 catalogue');edge(n,'catalogued_as',inventory,loc,'OIP135 inventory association; no object identity inferred')
  for ident in row['identification_numbers']:
   x='excavation_inventory:KERKENES-'+ident;add(x,'external_catalogue_record',ident);edge(n,'catalogued_as',x,loc,'OIP135 catalogue and inventory concordance')
 for label in ['IX','XI']:add('edition_siglum:OIP135-'+label,'external_catalogue_record','OIP135 fragment '+label)
 edge('edition_siglum:OIP135-XI','not_same_as','edition_siglum:OIP135-IX','research/k01-catalogue-concordance.json#/excluded_fragment_label','OIP135 pp.67/70/79; different published catalogue labels, not a physical-object assertion')
 graph['status']='FROZEN_REFERENCE_AND_K01_METADATA_INTEROPERABILITY';graph['scope']='203 derivative sentence records and eight source catalogue entries plus preserved legacy graph; no added physical objects, certified joins, readings or independent reviews.';validate_graph(graph)
 ET.indent(tei,space='  ');xml=ET.tostring(tei,encoding='utf-8',xml_declaration=True)+b'\n';ns={'t':TEI};tei=ET.fromstring(xml);roundtrip=[json.loads(x.text) for x in tei.findall('.//t:note[@type="native-record-json"]',ns)]
 if roundtrip!=rows or [x.text for x in tei.findall('.//t:ab',ns)]!=[r['text'] for r in rows]:raise ValueError('reference roundtrip loss')
 manifest={'schema_version':'1.0','input_sha256':{p:digest(b) for p,b in raw.items()},'builder_sha256':digest(Path(__file__).read_bytes()),'outputs_sha256':{OUTPUTS[0]:digest(xml),OUTPUTS[1]:digest(encode(graph))},'coverage':{'reference_sentence_records':len(rows),'reference_tokens':sum(r['token_count'] for r in rows),'distinct_source_tm_ids':len({r['trismegistos_id'] for r in rows}),'k01_source_catalogue_entries':len(k01['records']),'canonical_reading_admissions':0,'new_verified_physical_objects':0,'new_independent_reviews':0},'mapping':{'native_record_unit':'source_sentence; source_catalogue_entry; legacy graph units retained separately','reversible_fields':'All native reference record fields through native-record-json notes; exact source text through ab; no normalization.','lossy_fields':[],'not_mapped':'Unacquired source corpus, restricted primary critical text/images, unknown object identity, layout and graphical uncertainty absent from source.','rights':'UD reference XML is a CC-BY-SA-4.0 derivative with attribution; metadata graph contains project-authored factual identifiers and source assertions. OIP source payload is not redistributed.','validation_commands':['python scripts/build_interchange.py','python scripts/validate_upstream_epidoc.py --schema PATH --compiler PATH'],'conformance_scope':'Frozen reference view only; applicable upstream validation receipt required. Not complete epigraphic corpus coverage.'}}
 return {OUTPUTS[0]:xml,OUTPUTS[1]:encode(graph),OUTPUTS[2]:encode(manifest)}
def replay(root=ROOT,write=False):
 for p,b in build(root).items():
  target=Path(root)/p
  if write:target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(b)
  elif not target.exists() or target.read_bytes()!=b:raise ValueError('stale interchange artifact: '+p)
def main():
 a=argparse.ArgumentParser();a.add_argument('--write',action='store_true');args=a.parse_args();replay(write=args.write);print('PASS: exact frozen-reference roundtrip and source-qualified identity graph; no canonical admission')
if __name__=='__main__':main()
