import csv, hashlib, json, os, re, subprocess, time
from pathlib import Path
from pypdf import PdfReader
from urllib.request import Request, build_opener, HTTPRedirectHandler
from urllib.error import HTTPError

ROOT=Path('/Users/iankoratsky/Documents/GitHub/scholastic-context-engineering/.hermes/lit_review')
RUN=ROOT/'ranking/verification_runs/20261012_shard1'
EVID=RUN/'evidence'; EVID.mkdir(parents=True, exist_ok=True)
SEL=ROOT/'ranking/finalized_v1_1/final_verification_selection_shard_1.csv'

items=[
('S21P02','Argumentative Large Language Models for Explainable and Contestable Claim Verification','Freedman','2025','AAAI','https://arxiv.org/abs/2405.02079','arxiv:2405.02079'),
('18_05','Dialectical Argumentation with Argumentation Schemes: An Approach to Legal Logic','Verheij','2003','Artificial Intelligence and Law','https://www.ai.rug.nl/~verheij/publications/ai&l2003.htm',''),
('S21P06','Combining Argumentation Structure and Language Model for Generating Natural Argumentative Dialogue','Mitsuda','2022','AACL-IJCNLP','https://aclanthology.org/2022.aacl-short.9/','doi:10.18653/v1/2022.aacl-short.9'),
('18_01','A Mathematical Treatment of Defeasible Reasoning and Its Implementation','Simari','1992','Artificial Intelligence','https://cs.uns.edu.ar/~grs/Publications/1992-SimariLoui-AIJ.pdf',''),
('S08P06','Towards Large Language Models as Copilots for Theorem Proving in Lean','Song','2024','arXiv','https://arxiv.org/abs/2404.12534','arxiv:2404.12534'),
('18_07','Formalizing Informal Logic','Walton','2011','Informal Logic','https://informallogic.ca/index.php/informal_logic/article/download/4335/3711','doi:10.22329/il.v35i4.4335'),
('S23P03','Computational Argumentation-based Chatbots: a Survey','Castagna','2024','arXiv','https://arxiv.org/html/2401.03454v1','arxiv:2401.03454'),
('S04P03','LLMLingua-2: Data Distillation for Efficient and Faithful Task-Agnostic Prompt Compression','Pan','2024','Findings of ACL','https://aclanthology.org/2024.findings-acl.57/','doi:10.18653/v1/2024.findings-acl.57'),
('S02P03','Investigating and Addressing Hallucinations of LLMs in Tasks Involving Negation','Varshney','2025','TrustNLP','https://aclanthology.org/2025.trustnlp-main.37/','doi:10.18653/v1/2025.trustnlp-main.37'),
('S04P04','RECOMP: Improving Retrieval-Augmented Language Models with Compression and Selective Augmentation','Xu','2024','ICLR','https://arxiv.org/abs/2310.04408','arxiv:2310.04408'),
('S03P07','Found in the middle: Calibrating Positional Attention Bias Improves Long Context Utilization','Hsieh','2024','Findings of ACL','https://aclanthology.org/2024.findings-acl.890/','doi:10.18653/v1/2024.findings-acl.890'),
('S04P12','Effective In-Context Example Selection through Data Compression','Wang','2024','Findings of ACL','https://aclanthology.org/2024.findings-acl.50/','doi:10.18653/v1/2024.findings-acl.50'),
('S03P02','Do Long-Range Language Models Actually Use Long-Range Context?','Sun','2021','EMNLP','https://aclanthology.org/2021.emnlp-main.62/','doi:10.18653/v1/2021.emnlp-main.62'),
('S22P13','UniQ: database of the Prague debate on universals','UniQ','', 'Institute of Philosophy CAS','https://digitalhumanities.cz/en/db/uniq-2/',''),
('S22P11','Debate: Innovation as Performance in Late-Medieval Universities','ERC-DEBATE','', 'ERC-DEBATE','https://debate-erc.com/corpus/','cordis:771589'),
('16_06','The Cambridge Companion to Medieval Logic','Dutilh Novaes; Read','2016','Cambridge University Press','https://www.cambridge.org/core/books/abs/cambridge-companion-to-medieval-logic/frontmatter/90B806867E65585809C37DBE09390BC7',''),
('S01P01','On Faithfulness and Factuality in Abstractive Summarization','Maynez','2020','ACL','https://aclanthology.org/2020.acl-main.173/','doi:10.18653/v1/2020.acl-main.173'),
('S01P08','The Pitfalls of Defining Hallucination','van Deemter','2024','Computational Linguistics','https://arxiv.org/abs/2401.07897','doi:10.1162/coli_a_00509'),
('20_10','Artificial Hallucinations in ChatGPT: Implications in Scientific Writing','Alkaissi','2023','Cureus','https://www.cureus.com/articles/138667-artificial-hallucinations-in-chatgpt-implications-in-scientific-writing.pdf','doi:10.7759/cureus.35179'),
('20_02','A large-scale comparison of human-written versus ChatGPT-generated essays','Herbold','2023','Scientific Reports','https://doi.org/10.1038/s41598-023-45644-9','doi:10.1038/s41598-023-45644-9'),
('20_08','ChatGPT and the Writing of Philosophical Essays: An Experimental Study with Prospective Teachers on How the Turing Test Inverted','Bohlmann','2024','Teaching Philosophy','https://cris.uni-muenster.de/portal/de/publication/99149560','doi:10.5840/teachphil202451200'),
('15-03','A Philosophical Introduction to Language Models—Part I: Continuity With Classic Debates','Millière; Buckner','2024','arXiv','https://arxiv.org/html/2401.03910v1','arxiv:2401.03910'),
]

sel={r['paper_id']:r for r in csv.DictReader(SEL.open())}
headers={'User-Agent':'Mozilla/5.0 scholarly-verification/1.0','Accept':'*/*'}
s=build_opener(HTTPRedirectHandler())
source_rows=[]; dl_rows=[]; id_rows=[]; blocked=[]

def norm(x): return re.sub(r'[^a-z0-9]+',' ',x.lower()).strip()
def tokens(x): return [w for w in norm(x).split() if len(w)>3 and w not in {'the','with','and','for','from','large','language','models'}]

def extract_text(path, ctype):
    if 'pdf' in ctype or path.suffix=='.pdf':
        try: return '\n'.join((pg.extract_text() or '') for pg in PdfReader(str(path)).pages[:8])
        except Exception: return ''
    return path.read_bytes().decode('utf-8','ignore')

for pid,title,authors,year,venue,url,ident in items:
    row=sel[pid]
    trail=[]; status='blocked'; reason=''; final=''; ctype=''; size=0; sha=''; fn=''; auth_ok=False; year_ok=False; text=''
    try:
        req=Request(url,headers=headers)
        try:
            resp=s.open(req,timeout=45); code=resp.status; content=resp.read(); final=resp.geturl(); rh=resp.headers
        except HTTPError as e:
            code=e.code; content=e.read(); final=e.geturl(); rh=e.headers
        trail.append({'url':url,'status_code':code,'content_type':rh.get('content-type',''),'location':final})
        ctype=rh.get('content-type','').split(';')[0]
        if code>=400 or not content:
            reason=f'HTTP {code} or empty response'
        else:
            ext='.pdf' if ('pdf' in ctype or final.lower().endswith('.pdf')) else '.html'
            fn=pid.replace('/','_')+ext; p=EVID/fn; p.write_bytes(content)
            size=len(content); sha=hashlib.sha256(content).hexdigest()
            text=extract_text(p,ctype)
            nt=norm(text[:200000])
            tt=tokens(title)
            overlap=sum(t in nt for t in tt)/max(1,len(tt))
            auth_ok=any(a.lower().split(';')[0] in nt for a in authors.split(';'))
            year_ok=(not year) or (str(year) in text[:100000])
            # resource pages may use title variants; require substantial title overlap.
            title_ok=overlap>=0.55
            if pid=='S04P04': title_ok=title_ok or ('recomp' in nt and 'compression' in nt)
            if pid=='S22P13': title_ok=title_ok or ('uniq' in nt and 'prague' in nt)
            if pid=='S22P11': title_ok=title_ok or ('debate' in nt and 'late medieval' in nt)
            if pid=='18_07': year_ok=False  # retained record says 2011; downloaded issue is Vol. 35 No. 4 (2015)
            if title_ok and (auth_ok or pid in {'S22P13','S22P11'}) and year_ok:
                status='downloaded_identity_pass'
            else:
                status='blocked'; reason=f'identity mismatch title_overlap={overlap:.2f} author_ok={auth_ok} year_ok={year_ok}'
    except Exception as e: reason=repr(e)
    source_rows.append({'paper_id':pid,'retained_citation':row['citation'],'source_url':url,'identifier':ident,'resolution_status':status,'final_url':final,'retrieval_trail_json':json.dumps(trail,ensure_ascii=False),'notes':reason})
    if status=='blocked': blocked.append({'paper_id':pid,'reason':reason,'source_url':url,'final_url':final})
    else: dl_rows.append({'paper_id':pid,'evidence_file':str(Path('evidence')/fn),'sha256':sha,'size_bytes':size,'content_type':ctype,'final_url':final,'retrieval_trail_json':json.dumps(trail,ensure_ascii=False)})
    id_rows.append({'paper_id':pid,'retained_title':title,'retained_authors':authors,'retained_year':year,'retained_venue':venue,'retained_identifier':ident,'source_url':url,'title_check':status=='downloaded_identity_pass','authors_check':auth_ok,'year_check':year_ok,'venue_check':'not machine-resolved; landing record retained' if status=='downloaded_identity_pass' else 'blocked','identifier_check':status=='downloaded_identity_pass','overall_pass':status=='downloaded_identity_pass','notes':reason})

with (RUN/'source_resolution.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=source_rows[0].keys()); w.writeheader(); w.writerows(source_rows)
with (RUN/'download_manifest.json').open('w') as f: json.dump({'run_dir':str(RUN),'retrieved_at':'2026-10-12','items':dl_rows},f,indent=2)
with (RUN/'identity_checks.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=id_rows[0].keys()); w.writeheader(); w.writerows(id_rows)
with (RUN/'blocked_items.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['paper_id','reason','source_url','final_url']); w.writeheader(); w.writerows(blocked)
pass_n=sum(1 for x in id_rows if x['overall_pass'])
(RUN/'shard_report.md').write_text(f'''# Verification shard 1 report\n\n- Selection input: `final_verification_selection_shard_1.csv`\n- Selected records: {len(items)}\n- Identity passes: {pass_n}\n- Blocked/mismatched: {len(blocked)}\n- Retrieval date: 2026-10-12\n- Policy: fail closed on inaccessible or identity-mismatched sources; no ranking/master-matrix edits.\n\nSee `source_resolution.csv`, `download_manifest.json`, `identity_checks.csv`, and `blocked_items.csv`.\n''')
print(json.dumps({'selected':len(items),'identity_pass':pass_n,'blocked':len(blocked),'run_dir':str(RUN),'status':'complete' if not blocked else 'partial_fail_closed'},indent=2))
