"""Replay the licensed publisher text, retaining HTML editorial markup."""
import argparse, hashlib, json, re
from html.parser import HTMLParser
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class Text(HTMLParser):
    def __init__(self):
        super().__init__();self.parts=[];self.superscripts=[];self.start=None
    def handle_starttag(self,tag,attrs):
        if tag=='sup': self.start=sum(map(len,self.parts))
    def handle_endtag(self,tag):
        if tag=='sup' and self.start is not None:
            self.superscripts.append({'start':self.start,'end':sum(map(len,self.parts))});self.start=None
    def handle_data(self,data):self.parts.append(data)
def reconcile(root=ROOT):
    root=Path(root);register=json.loads((root/'research/g12-primary-edition.json').read_text())
    source=register['source'];path=root/source['snapshot_path'];raw=path.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=source['snapshot_sha256']:raise ValueError('G-12 source snapshot changed')
    lines=[]
    for fragment in re.findall(r'<p>(.*?)</p>',raw.decode(),re.S):
        p=Text();p.feed(fragment);text=''.join(p.parts)
        number=re.match(r'([1-7])\. ',text)
        if not number:raise ValueError('Unexpected publisher line label')
        lines.append({'line':int(number[1]),'source_html':fragment,'literal_text':text,
                      'superscript_spans':p.superscripts,'source_locator':'Edition of the text, Text., line '+number[1]})
    if [l['line'] for l in lines]!=list(range(1,8)):raise ValueError('G-12 seven-line inventory is incomplete/duplicated')
    ref=json.loads((root/'imports/ud-phrygian-kul.json').read_text())
    candidate=register['ud_candidate_join'];rows=[r for r in ref['records'] if r['trismegistos_id']==candidate['trismegistos_id']]
    return {'format':'phrygian-g12-edition-comparison-v1','source':source,'primary_edition_lines':lines,
     'ud_candidate_sentence_ids':[r['record_id'] for r in rows],
     'ud_candidate_sentence_count':len(rows),'primary_physical_line_count':7,
     'identity_join_status':candidate['status'],'physical_line_alignment_established':False,
     'independent_epigraphic_review':False,'canonical_admission_granted':False,
     'representation_differences':['Seven edition lines versus ten UD sentences; these are different units.','Publisher ś/Ś and underdots versus UD S/Ṣ convention; do not rewrite source letters.','Publisher line 4 has raised letters, retained in HTML and superscript spans.','Publisher vacat and punctuation remain in source text; UD linguistic tokenization is a separate representation.'],
     'boundary':'This replays a published reading; it neither adjudicates its correctness nor treats the dependent UD dataset as an independent witness.'}
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args()
    output=json.dumps(reconcile(),ensure_ascii=False,indent=2)+'\n'
    if args.check:
        if (ROOT/'analysis/g12-edition-comparison.json').read_text()!=output:raise SystemExit('G-12 comparison is stale')
        print('Licensed G-12 seven-line source and candidate UD comparison replay exactly.')
    else:print(output,end='')
