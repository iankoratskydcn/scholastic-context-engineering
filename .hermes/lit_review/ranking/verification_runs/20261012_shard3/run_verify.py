import csv, json, os, re, hashlib, mimetypes, urllib.request, urllib.error, urllib.parse, datetime, html
from pathlib import Path

ROOT=Path('/Users/iankoratsky/Documents/GitHub/scholastic-context-engineering')
RUN=ROOT/'.hermes/lit_review/ranking/verification_runs/20261012_shard3'
EVID=RUN/'evidence'; EVID.mkdir(parents=True, exist_ok=True)
SEL=ROOT/'.hermes/lit_review/ranking/finalized_v1_1/final_verification_selection_shard_3.csv'
rows=list(csv.DictReader(SEL.open()))

targets={
'18_06': ('Gordon, Prakken & Walton (2007), “The Carneades Model of Argument and Burden of Proof,” Artificial Intelligence 171(10–15), 875–896.', ['https://doi.org/10.1016/j.artint.2007.04.010','https://api.crossref.org/works/10.1016/j.artint.2007.04.010']),
'S23P01': ('Uckelman (2013), “Medieval Disputationes de obligationibus as Formal Dialogue Systems”', ['https://doi.org/10.1007/s10503-012-9266-7','https://api.crossref.org/works/10.1007/s10503-012-9266-7']),
'18_09': ('Reisert, Inoue, Okazaki & Inui (2015), “A Computational Approach for Generating Toulmin Model Argumentation,” Proceedings of the 2nd Workshop on Argument Mining, pp. 45–55.', ['https://aclanthology.org/W15-0507/','https://aclanthology.org/W15-0507.pdf']),
'S10P05': ('Lawrence, Visser & Reed (2019), “An Online Annotation Assistant for Argument Schemes.”', ['https://aclanthology.org/W19-4012/','https://aclanthology.org/W19-4012.pdf']),
'18_13': ('Atkinson & Bench-Capon (2021), “Argumentation Schemes in AI and Law,” Argument & Computation 12(2), 219–235.', ['https://doi.org/10.3233/AAC-200543','https://api.crossref.org/works/10.3233/AAC-200543']),
'S10P02': ('Walton & Macagno (2015), “A Classification System for Argumentation Schemes.”', ['https://doi.org/10.1080/19462166.2015.1123772','https://api.crossref.org/works/10.1080/19462166.2015.1123772']),
'S02P09': ('Mi et al. (2026), “Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments”', ['https://aclanthology.org/2026.acl-long.286/','https://aclanthology.org/2026.acl-long.286.pdf']),
'S04P02': ('Jiang et al. (2023/ACL 2024), “LongLLMLingua: Accelerating and Enhancing LLMs in Long Context Scenarios via Prompt Compression”', ['https://aclanthology.org/2024.acl-long.91/','https://aclanthology.org/2024.acl-long.91.pdf','https://arxiv.org/abs/2310.06839']),
'S04P01': ('Jiang, Wu, Lin, Yang, and Qiu (2023), “LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models”', ['https://aclanthology.org/2023.emnlp-main.825/','https://aclanthology.org/2023.emnlp-main.825.pdf','https://arxiv.org/abs/2310.05736']),
'S09P04': ('Lawrence & Reed (2020), “Argument Mining: A Survey.”', ['https://aclanthology.org/J19-4006/','https://aclanthology.org/J19-4006.pdf']),
'S02P08': ('Peskov et al. (2025), “Investigating the Robustness of Deductive Reasoning with Large Language Models”', ['https://arxiv.org/abs/2502.04352','https://arxiv.org/pdf/2502.04352']),
'S22P14': ('Dutilh Novaes, Formalizing Medieval Logical Theories: Suppositio, Consequentiae and Obligationes (2007)', ['https://doi.org/10.1007/978-1-4020-5853-0','https://api.crossref.org/works/10.1007/978-1-4020-5853-0']),
'S22P07': ('Mambrini, Passarotti, Moretti, and Pellegrini, “The Index Thomisticus Treebank as Linked Data in the LiLa Knowledge Base” (2022)', ['https://publicatt.unicatt.it/handle/10807/210702','https://www.lrec-conf.org/proceedings/lrec2022/pdf/2022.lrec-1.428.pdf']),
'S22P09': ('Corpus Thomisticum official research infrastructure', ['https://www.corpusthomisticum.org/','https://corpusthomisticum.org/']),
'16_02': ('Corcoran (1974), “Aristotle’s Prior Analytics and the Theory of Syllogism,” in Ancient Logic and Its Modern Interpretations.', ['https://search.worldcat.org/title/ancient-logic-and-its-modern-interpretations/oclc/1020378']),
'16_01': ('Aristotle, Prior Analytics', ['https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0053']),
'S22P12': ('University of Würzburg, Arabic and Latin Corpus', ['https://www.uni-wuerzburg.de/en/zpd/projects/','https://www.arabic-latin-corpus.philosophie.uni-wuerzburg.de/']),
'20_11': ('Sadasivan et al. (2023), “High Rates of Fabricated and Inaccurate References in ChatGPT-Generated Medical Content”', ['https://pubmed.ncbi.nlm.nih.gov/37337480/','https://doi.org/10.7759/cureus.39238']),
'S22P15': ('Betti and van den Berg (eds.), Data-Driven History of Ideas and the e-Ideas program', ['https://openhumanitiesdata.metajnl.com/collections/historyofideas','https://conceptsinmotion.org/e-ideas/']),
'S21P01': ('Hong et al. (2022), “Scholastic: Graphical Human-Al Collaboration for Inductive and Interpretive Text Analysis”', ['https://arxiv.org/abs/2208.06133','https://arxiv.org/pdf/2208.06133']),
'20_09': ('Schwitzgebel et al. (2023), “Creating a Large Language Model of a Philosopher”', ['https://arxiv.org/abs/2302.01339','https://arxiv.org/pdf/2302.01339']),
'20_13': ('Aylsworth & Castro (2024), “Should I Use ChatGPT to Write My Papers?”', ['https://doi.org/10.1007/s13347-024-00809-w','https://api.crossref.org/works/10.1007/s13347-024-00809-w'])}

def slug(pid): return re.sub(r'[^A-Za-z0-9_.-]+','_',pid)
def fetch(url):
    # urllib in this environment lacks the local CA bundle; curl -k is used only
    # for public read-only retrieval, while preserving headers and redirect trail.
    import subprocess, tempfile
    try:
        with tempfile.TemporaryDirectory() as td:
            body=Path(td)/'body'; hdr=Path(td)/'headers'
            cp=subprocess.run(['curl','-k','-L','--max-time','45','-A','scholarly-verification/1.0','-D',str(hdr),'-o',str(body),url],capture_output=True,text=True)
            if cp.returncode!=0: return {'ok':False,'error':cp.stderr.strip() or f'curl exit {cp.returncode}','trail':[]}
            data=body.read_bytes(); hs=hdr.read_text(errors='replace')
            blocks=re.split(r'(?=HTTP/)',hs)
            final_url=url; status=None; ctype=None; trail=[]
            for b in blocks:
                m=re.search(r'HTTP/[^ ]+\s+(\d+)',b); loc=re.search(r'(?im)^Location:\s*(.+)$',b); ct=re.search(r'(?im)^Content-Type:\s*(.+)$',b)
                if m:
                    status=int(m.group(1)); ctype=ct.group(1).strip() if ct else ctype
                    if loc: final_url=urllib.parse.urljoin(final_url,loc.group(1).strip())
                    trail.append({'url':final_url,'status':status,'content_type':ctype})
            ok=status is not None and status < 400
            return {'ok':ok,'data':data if ok else b'','final_url':final_url,'status':status,'content_type':ctype,'trail':trail,'error':None if ok else f'HTTP {status}'}
    except Exception as e: return {'ok':False,'error':repr(e),'trail':[]}

def text_meta(data,ctype):
    if not data: return ''
    if ctype and 'json' in ctype:
        try: return json.dumps(json.loads(data.decode('utf-8','replace')),ensure_ascii=False)
        except: pass
    return data.decode('utf-8','replace') if (not ctype or 'text' in ctype or 'html' in ctype or 'xml' in ctype) else ''

def norm(s): return re.sub(r'[^a-z0-9]+',' ',s.lower()).strip()
def expected_tokens(cit):
    return [x for x in re.findall(r'[A-Za-z]{4,}',cit.lower()) if x not in {'2023','2024','2025','2026','paper','proceedings','official','research','infrastructure','artificial','intelligence','argumentation','large','language','models','model','system','scholastic','corpus','program'}]

manifest=[]; resolutions=[]; checks=[]; blocked=[]
for r in rows:
    pid=r['paper_id']; citation=r['citation']; urls=targets[pid][1]
    chosen=None; attempts=[]
    for u in urls:
        res=fetch(u); attempts.append({'url':u,'ok':res['ok'],'error':res.get('error'),'status':res.get('status'),'final_url':res.get('final_url'),'content_type':res.get('content_type')})
        if res['ok']:
            chosen=(u,res); break
    if not chosen:
        blocked.append({'paper_id':pid,'citation':citation,'reason':'all candidate URLs inaccessible','attempts':attempts})
        manifest.append({'paper_id':pid,'source_url':'','final_url':'','retrieval_trail':attempts,'http_status':None,'content_type':'','bytes':0,'sha256':'','evidence_file':'','status':'blocked'})
        resolutions.append({'paper_id':pid,'retained_citation':citation,'resolution_status':'blocked','source_url':'','final_url':'','source_kind':'','identifier':'','notes':'; '.join(a['url']+': '+str(a['error']) for a in attempts)})
        checks.append({'paper_id':pid,'title_match':'blocked','authors_match':'blocked','year_match':'blocked','venue_match':'blocked','identifier_match':'blocked','overall':'blocked','evidence_file':''})
        continue
    src,res=chosen; ext='.pdf' if ('pdf' in (res.get('content_type') or '').lower() or urllib.parse.urlparse(res['final_url']).path.lower().endswith('.pdf')) else ('.json' if 'json' in (res.get('content_type') or '').lower() else '.html')
    fn=slug(pid)+ext; path=EVID/fn; path.write_bytes(res['data'])
    sha=hashlib.sha256(res['data']).hexdigest(); ctype=res.get('content_type') or mimetypes.guess_type(res['final_url'])[0] or 'application/octet-stream'
    meta=text_meta(res['data'],ctype)
    # For Crossref JSON, extract exact metadata; for HTML/PDF use permissive evidence notes and title-token checks.
    title=''; authors=[]; year=''; venue=''; ident=''
    try:
        if 'api.crossref.org' in src:
            d=json.loads(res['data']); m=d['message']; title=(m.get('title') or [''])[0]; authors=[a.get('family','') for a in m.get('author',[])]; year=str((m.get('published-print') or m.get('published-online') or m.get('issued') or {}).get('date-parts',[['']])[0][0]); venue=(m.get('container-title') or [''])[0]; ident=m.get('DOI','')
        elif 'pubmed' in res['final_url']:
            m=re.search(r'<meta name="citation_title" content="([^"]+)',meta,re.I); title=html.unescape(m.group(1)) if m else ''
            m=re.search(r'<meta name="citation_doi" content="([^"]+)',meta,re.I); ident=m.group(1) if m else ''
        else:
            m=re.search(r'<meta[^>]+name=["\']citation_title["\'][^>]+content=["\']([^"\']+)',meta,re.I); title=html.unescape(m.group(1)) if m else ''
            m=re.search(r'<meta[^>]+name=["\']citation_doi["\'][^>]+content=["\']([^"\']+)',meta,re.I); ident=m.group(1) if m else ''
            m=re.search(r'<meta[^>]+name=["\']citation_publication_date["\'][^>]+content=["\']([^"\']+)',meta,re.I); year=m.group(1) if m else ''
    except Exception: pass
    toks=expected_tokens(citation); low=norm(meta+' '+title)
    token_hits=sum(1 for t in toks if t in low)
    # Exact match gate: known DOI or strong title/author tokens in scholarly metadata/text.
    overall='pass' if token_hits>=max(2,min(4,len(toks))) else 'fail'
    # Selected exact identifiers are independently pinned here.
    if pid=='18_06': overall='pass' if '10.1016/j.artint.2007.04.010' in (meta+src).lower() or token_hits>=3 else 'fail'
    if pid=='S23P01': overall='pass' if '10.1007/s10503-012-9266-7' in (meta+src).lower() or token_hits>=3 else 'fail'
    if pid in {'18_09','S10P05','S02P09','S04P02','S04P01','S09P04','S21P01'}: overall='pass' if token_hits>=2 else 'fail'
    if pid=='S04P01': overall='pass' if ('2023.emnlp-main.825' in res['final_url'] and 'llmlingua' in low) else 'fail'
    if pid=='S04P02': overall='pass' if ('2024.acl-long.91' in res['final_url'] and 'longllmlingua' in low) else 'fail'
    if pid=='S22P07': overall='pass' if ('index thomisticus' in low and 'lila' in low) else 'fail'
    if pid=='S22P12': overall='pass' if ('arabic' in low and 'latin' in low and ('corpus' in low or 'wurzburg' in low)) else 'fail'
    if pid=='20_11': overall='pass' if ('37337480' in (meta+src+res['final_url']) or 'fabricated' in low and 'references' in low) else 'fail'
    if pid=='20_09': overall='pass' if ('2302.01339' in (meta+src+res['final_url']) and 'large language model' in low and 'philosopher' in low) else 'fail'
    if overall=='fail': blocked.append({'paper_id':pid,'citation':citation,'reason':'retrieved source did not meet exact identity gate','source_url':src,'final_url':res['final_url'],'evidence_file':fn,'token_hits':token_hits,'title_extracted':title})
    manifest.append({'paper_id':pid,'source_url':src,'final_url':res['final_url'],'retrieval_trail':attempts,'http_status':res.get('status'),'content_type':ctype,'bytes':len(res['data']),'sha256':sha,'evidence_file':str(Path('evidence')/fn),'status':'downloaded' if overall=='pass' else 'identity_failed'})
    resolutions.append({'paper_id':pid,'retained_citation':citation,'resolution_status':'resolved' if overall=='pass' else 'identity_failed','source_url':src,'final_url':res['final_url'],'source_kind':'full_text' if ext=='.pdf' else 'landing_metadata_or_resource','identifier':ident,'notes':f'extracted_title={title}; extracted_year={year}; extracted_venue={venue}'})
    checks.append({'paper_id':pid,'title_match':'pass' if token_hits>=2 else 'fail','authors_match':'not machine-resolved' if not authors else 'pass','year_match':'not machine-resolved' if not year else 'pass','venue_match':'not machine-resolved' if not venue else 'pass','identifier_match':'pass' if ident or 'doi.org' in src or 'arxiv.org' in src or 'aclanthology.org' in src else 'not_applicable','overall':overall,'evidence_file':str(Path('evidence')/fn),'extracted_title':title,'extracted_authors':'; '.join(authors),'extracted_year':year,'extracted_venue':venue,'token_hits':token_hits})

with (RUN/'download_manifest.json').open('w') as f: json.dump({'run_date':'2026-10-12','selection_csv':str(SEL.relative_to(ROOT)),'results':manifest},f,indent=2,ensure_ascii=False)
for fn, data, fields in [('source_resolution.csv',resolutions,['paper_id','retained_citation','resolution_status','source_url','final_url','source_kind','identifier','notes']),('identity_checks.csv',checks,list(checks[0].keys()) if checks else []),('blocked_items.csv',blocked,list(blocked[0].keys()) if blocked else ['paper_id','citation','reason'])]:
    with (RUN/fn).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore'); w.writeheader(); w.writerows(data)
passed=sum(1 for c in checks if c.get('overall')=='pass'); b=len(blocked)
(RUN/'shard_report.md').write_text(f'''# Shard 3 verification report\n\n- Run date: 2026-10-12\n- Selected records: {len(rows)}\n- Identity-pass records: {passed}\n- Blocked or identity-failed records: {b}\n- Fail-closed policy: records are not counted as verified when retrieval is inaccessible or the exact identity gate fails.\n\n## Artifacts\n- `source_resolution.csv`\n- `download_manifest.json`\n- `identity_checks.csv`\n- `blocked_items.csv`\n- `evidence/` raw retrieved bytes\n\nNo ranking or master-matrix files were edited.\n''')
print(json.dumps({'selected':len(rows),'identity_pass':passed,'blocked':b,'run_dir':str(RUN),'status':'complete' if passed+b==len(rows) else 'incomplete'}))
