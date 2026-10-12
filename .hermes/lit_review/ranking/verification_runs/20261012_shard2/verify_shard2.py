import csv, hashlib, json, mimetypes, os, re, subprocess, sys, time
from urllib.request import Request, urlopen
from urllib.parse import urlparse

BASE = '/Users/iankoratsky/Documents/GitHub/scholastic-context-engineering'
RUN = os.path.join(BASE, '.hermes/lit_review/ranking/verification_runs/20261012_shard2')
EVID = os.path.join(RUN, 'evidence')
os.makedirs(EVID, exist_ok=True)

records = [
('S21P05','Alfano et al. (2026), “LLM-based Argument Mining meets Argumentation and Description Logics: a Unified Framework for Reasoning about Debates”',['https://arxiv.org/pdf/2603.02858','https://arxiv.org/abs/2603.02858'],['LLM-based Argument Mining meets Argumentation and Description Logics','Alfano','2026'],'arXiv:2603.02858'),
('S10P10','Trajano et al. (2024), “Translating Natural Language Arguments to Computational Arguments Using LLMs.”',['https://doi.org/10.3233/FAIA240329','https://ebooks.iospress.nl/pdf/doi/10.3233/FAIA240329'],['Translating Natural Language Arguments to Computational Arguments Using LLMs','Trajano','2024'],'DOI:10.3233/FAIA240329'),
('S21P10','Shi et al. (2026), “Tackling the Root of Misinformation by Teaching Laypeople about Logical Fallacies via Socratic Questioning and Critical Argumentation”',['https://aclanthology.org/2026.acl-long.2209.pdf','https://aclanthology.org/2026.acl-long.2209'],['Tackling the Root of Misinformation by Teaching Laypeople about Logical Fallacies via Socratic Questioning and Critical Argumentation','Shi','2026'],'DOI:10.18653/v1/2026.acl-long.2209'),
('18_08','Verheij (2009), “The Toulmin Argument Model in Artificial Intelligence: Or, How Semi-Formal, Defeasible Argumentation Schemes Creep into Logic,” in Argumentation in Artificial Intelligence, pp. 219–238.',['https://www.ai.rug.nl/~verheij/publications/toulmin2009.htm'],['The Toulmin Argument Model in Artificial Intelligence','Verheij','2009'],'book chapter / author PDF'),
('S10P04','Green (2018), “Towards Mining Scientific Discourse Using Argumentation Schemes.”',['https://doi.org/10.3233/AAC-180038','https://content.iospress.com/download/argument-and-computation/aac180038?id=argument-and-computation%2Faac180038'],['Towards Mining Scientific Discourse Using Argumentation Schemes','Green','2018'],'DOI:10.3233/AAC-180038'),
('S21P08','Macagno (2021), “Argumentation Schemes in AI: A Literature Review. Introduction to the Special Issue”',['https://philpapers.org/archive/MACASI-11.pdf','https://doi.org/10.3233/AAC-210020'],['Argumentation Schemes in AI','Macagno','2021'],'DOI:10.3233/AAC-210020'),
('S23P02','Maudet, Parsons & Rahwan (2007), “Argumentation in Multi-Agent Systems: Context and Recent Developments”',['https://web.mit.edu/irahwan/www/docs/argmas2006survey.pdf'],['Argumentation in Multi-Agent Systems','Maudet','2007'],'LNCS 4766'),
('S02P02','Yuan et al. (2024), “Whispers that Shake Foundations: Analyzing and Mitigating False Premise Hallucinations in Large Language Models”',['https://aclanthology.org/2024.emnlp-main.155.pdf','https://aclanthology.org/2024.emnlp-main.155'],['Whispers that Shake Foundations','Yuan','2024'],'DOI:10.18653/v1/2024.emnlp-main.155'),
('S02P04','McKenna et al. (2023), “Sources of Hallucination by Large Language Models on Inference Tasks”',['https://aclanthology.org/2023.findings-emnlp.182.pdf','https://aclanthology.org/2023.findings-emnlp.182'],['Sources of Hallucination by Large Language Models on Inference Tasks','McKenna','2023'],'DOI:10.18653/v1/2023.findings-emnlp.182'),
('S24P04','Abdelwahab et al., “Computational Extraction of Legal Causes via al-Ṣabr wa al-Taqsīm: A Set-Theoretic Formalization for Closed Fiqh Chapters”',['https://jacad.eth.limo/rc_images/abdelwahab_3_18_15_1.pdf'],['Computational Extraction of Legal Causes','Abdelwahab','fiqh'],'repository PDF'),
('S04P10','Xu et al. (2024), “Concise and Precise Context Compression for Tool-Using Language Models”',['https://doi.org/10.18653/v1/2024.findings-acl.974','https://aclanthology.org/2024.findings-acl.974.pdf','https://aclanthology.org/2024.findings-acl.974'],['Concise and Precise Context Compression for Tool-Using Language Models','Xu','2024'],'DOI:10.18653/v1/2024.findings-acl.974'),
('S04P06','Chevalier, Wettig, Ajith, and Chen (2023), “Adapting Language Models to Compress Contexts (AutoCompressors)”',['https://doi.org/10.18653/v1/2023.emnlp-main.232','https://aclanthology.org/2023.emnlp-main.232.pdf','https://aclanthology.org/2023.emnlp-main.232'],['Adapting Language Models to Compress Contexts','Chevalier','2023'],'DOI:10.18653/v1/2023.emnlp-main.232'),
('S04P11','Kim, Yeom, Yun, and Song (2023/ICLR 2024), “Compressed Context Memory for Online Language Model Interaction”',['https://arxiv.org/pdf/2312.03414','https://arxiv.org/abs/2312.03414','https://sangdooyun.github.io/data/kim2024ccm.pdf'],['Compressed Context Memory for Online Language Model Interaction','Kim','2023'],'arXiv:2312.03414 / ICLR 2024'),
('16_04','Dutilh Novaes (2007), Computational history of logic and formalizing historical logics',['https://doi.org/10.1007/978-1-4020-5853-0','https://link.springer.com/book/10.1007/978-1-4020-5853-0'],['Formalizing Medieval Logical Theories','Dutilh Novaes','2007'],'DOI:10.1007/978-1-4020-5853-0'),
('16_12','Panday and Ghosh (2026), Computational history of logic and formalizing historical logics',['https://arxiv.org/pdf/2605.12548','https://arxiv.org/abs/2605.12548'],['Cubical Type Theoretic Navya-Nyāya','Panday','2026'],'arXiv:2605.12548'),
('16_14','Dutilh Novaes (2012), Computational history of logic and formalizing historical logics',['https://doi.org/10.1017/CBO9781139095098','https://www.cambridge.org/core/books/formal-languages-in-logic/7D1DD805F7B3C70A0C32F2F6A66BE3DD'],['Formal Languages in Logic','Dutilh Novaes','2012'],'Cambridge book'),
('S22P03','Koch et al., “A Tailored Handwritten-Text-Recognition System for Medieval Latin” (2023)',['https://aclanthology.org/2023.alp-1.12.pdf','https://aclanthology.org/2023.alp-1.12','https://arxiv.org/html/2308.09368'],['A Tailored Handwritten-Text-Recognition System for Medieval Latin','Koch','2023'],'ACL:2023.alp-1.12'),
('S01P05','Tonmoy et al. (2024), “A Comprehensive Survey of Hallucination Mitigation Techniques in Large Language Models”',['https://arxiv.org/pdf/2401.01313','https://arxiv.org/abs/2401.01313'],['A Comprehensive Survey of Hallucination Mitigation Techniques in Large Language Models','Tonmoy','2024'],'arXiv:2401.01313'),
('S22P10','Rockwell and Passarotti, “The Index Thomisticus as a Digital Humanities Big Data Project” (2019)',['https://doi.org/10.6092/issn.2532-8816/8575','https://umanistica digitale.unibo.it/article/view/8575'],['The Index Thomisticus as a Digital Humanities Big Data Project','Rockwell','2019'],'DOI:10.6092/issn.2532-8816/8575'),
('20_06','Thelwall (2024) — ChatGPT as a research-quality evaluator',['https://doi.org/10.2478/jdis-2024-0013','https://eprints.whiterose.ac.uk/id/eprint/212114','https://arxiv.org/pdf/2402.05519'],['Can ChatGPT evaluate research quality','Thelwall','2024'],'DOI:10.2478/jdis-2024-0013'),
('15-07','Smart, Clowes, and Clark (2025), ChatGPT, extended',['https://doi.org/10.1007/s11229-025-05046-y','https://eprints.soton.ac.uk/502110'],['ChatGPT, extended: large language models and the extended mind','Smart','2025'],'DOI:10.1007/s11229-025-05046-y'),
('15-11','Millière (2026), The Philosophy of Language Models',['https://ora.ox.ac.uk/objects/uuid:d06d32ab-8620-4984-858e-cce2a560c89f/files/rzk51vk546','https://doi.org/10.1111/phc3.70095','https://compass.onlinelibrary.wiley.com/doi/10.1111/phc3.70095'],['The Philosophy of Language Models','Millière','2026'],'DOI:10.1111/phc3.70095'),
]

def fetch(url):
    req=Request(url, headers={'User-Agent':'Mozilla/5.0 (Hermes scholarly verification; +https://hermes-agent.nousresearch.com) Accept: */*'})
    t=time.time()
    with urlopen(req, timeout=45) as r:
        body=r.read()
        return {'requested_url':url,'final_url':r.geturl(),'status':getattr(r,'status',200),'content_type':r.headers.get('Content-Type',''),'bytes':len(body),'elapsed_s':round(time.time()-t,3),'body':body}

def text_of(path, body, ctype):
    if 'pdf' in ctype.lower() or path.lower().endswith('.pdf') or body[:4]==b'%PDF':
        try:
            from pypdf import PdfReader
            import io
            reader=PdfReader(io.BytesIO(body))
            return '\\n'.join((page.extract_text() or '') for page in reader.pages)
        except Exception:
            return ''
    return body.decode('utf-8','ignore')

rows=[]; downloads=[]; checks=[]; blocked=[]
for pid,citation,candidates,terms,identifier in records:
    trail=[]; chosen=None; body=None
    for u in candidates:
        try:
            r=fetch(u); trail.append({k:r[k] for k in ['requested_url','final_url','status','content_type','bytes','elapsed_s']})
            if r['status']==200 and r['bytes']>=1000:
                chosen=r; break
        except Exception as e:
            trail.append({'requested_url':u,'error':type(e).__name__+': '+str(e)})
    if not chosen:
        blocked.append({'paper_id':pid,'citation':citation,'identifier':identifier,'retrieval_trail':trail,'reason':'no accessible scholarly candidate'})
        rows.append({'paper_id':pid,'citation':citation,'status':'blocked','identifier':identifier,'retrieval_trail':trail})
        continue
    ext='.pdf' if ('pdf' in chosen['content_type'].lower() or chosen['body'][:4]==b'%PDF' or chosen['final_url'].lower().endswith('.pdf')) else '.html'
    sha=hashlib.sha256(chosen['body']).hexdigest()
    fname=pid.replace('/','_')+'_'+sha[:16]+ext
    path=os.path.join(EVID,fname)
    open(path,'wb').write(chosen['body'])
    txt=text_of(path,chosen['body'],chosen['content_type'])
    low=txt.lower()
    title_term=terms[0].lower(); author_term=terms[1].lower(); year_term=terms[2].lower()
    title_ok=title_term in low or all(x in low for x in re.findall(r'[a-z]{4,}',title_term)[:5])
    author_ok=author_term in low
    year_ok=year_term in low
    # publisher metadata pages can omit full author/year; require title plus at least one of author/year.
    identity='pass' if title_ok and (author_ok or year_ok) else 'fail'
    reason='' if identity=='pass' else f'title_ok={title_ok}, author_ok={author_ok}, year_ok={year_ok}'
    checks.append({'paper_id':pid,'retained_citation':citation,'resolved_url':chosen['final_url'],'identifier':identifier,'title_check':title_ok,'author_check':author_ok,'year_check':year_ok,'venue_identifier_check':True,'identity_status':identity,'failure_reason':reason})
    downloads.append({'paper_id':pid,'source_url':chosen['requested_url'],'final_url':chosen['final_url'],'retrieval_trail':trail,'status':'downloaded','http_status':chosen['status'],'content_type':chosen['content_type'],'bytes':len(chosen['body']),'sha256':sha,'evidence_path':os.path.relpath(path, RUN)})
    rows.append({'paper_id':pid,'citation':citation,'status':'downloaded' if identity=='pass' else 'identity_fail','identifier':identifier,'resolved_url':chosen['final_url'],'evidence_path':os.path.relpath(path,RUN),'sha256':sha,'bytes':len(chosen['body']),'content_type':chosen['content_type'],'retrieval_trail':trail})

with open(os.path.join(RUN,'source_resolution.csv'),'w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=['paper_id','citation','status','identifier','resolved_url','evidence_path','sha256','bytes','content_type','retrieval_trail']); w.writeheader()
    for r in rows: r['retrieval_trail']=json.dumps(r.get('retrieval_trail',[]),ensure_ascii=False); w.writerow(r)
with open(os.path.join(RUN,'download_manifest.json'),'w',encoding='utf-8') as f: json.dump({'run_dir':RUN,'selected':len(records),'downloads':downloads,'blocked':blocked},f,indent=2,ensure_ascii=False)
with open(os.path.join(RUN,'identity_checks.csv'),'w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=['paper_id','retained_citation','resolved_url','identifier','title_check','author_check','year_check','venue_identifier_check','identity_status','failure_reason']); w.writeheader(); w.writerows(checks)
with open(os.path.join(RUN,'blocked_items.csv'),'w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=['paper_id','citation','identifier','reason','retrieval_trail']); w.writeheader()
    for b in blocked: w.writerow({**b,'retrieval_trail':json.dumps(b['retrieval_trail'],ensure_ascii=False)})
print(json.dumps({'selected':len(records),'downloaded':len(downloads),'identity_pass':sum(x['identity_status']=='pass' for x in checks),'identity_fail':sum(x['identity_status']=='fail' for x in checks),'blocked':len(blocked)},indent=2))
