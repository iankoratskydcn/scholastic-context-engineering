import csv, json
from pathlib import Path

base = Path('/Users/iankoratsky/Documents/GitHub/scholastic-context-engineering/.hermes/lit_review/ranking')
infile = base / 'benchmark_studies.csv'
slug = 'scholarly_text_fit'
viewpoint = 'Scholarly and philosophical text authenticity'

scores = {
'S22P04':100,'S24P10':98,'S24P11':97,'S22P08':96,'S22P02':95,'S24P09':94,'15-02':93,'12-06':92,
'S10P07':91,'S23P12':90,'18_10':89,'18_11':88,'S23P04':87,'S09P08':86,'S25P13':85,'S25P14':84,
'S11P08':83,'11-08':83,'11-04':82,'11-06':81,'S24P12':80,'S25P12':79,'15-05':78,'15-08':77,'S23P05':76,
'14-08':74,'S08P04':73,'S08P05':72,'S07P08':70,'S07P01':68,'12-04':67,'12-05':66,'12-11':65,'12-12':64,
'12-15':63,'11-01':62,'S10P09':61,'S10P12':60,'S06P11':58,'12-08':57,'19_06':56,'19_04':55,'19_12':54,
'19_09':53,'19_15':52,'19_10':51,'19_14':50,'19_02':49,'S10P08':47,'17_15':46,'17_14':45,'17_13':44,
'17_01':43,'17_02':42,'17_09':41,'17_11':40,'17_12':39,'17_08':38,'17_07':37,'17_10':36,'17_04':35,'17_03':34,
'15-06':33,'S08P07':32,'S06P06':31,'12-03':30,'12-07':29,'S02P05':28,'S02P07':27,'S02P06':26,'S05P05':25,
'S05P08':24,'S05P09':23,'S03P09':22,'S03P10':21,'S03P05':20,'S03P08':19,'S03P03':18,'S03P06':17,
'S25P12':79,'S25P13':85,'S25P14':84,'11-05':48,'11-12':46,
}
# Correct keys for rows whose source IDs are S-prefixed.
scores.update({'S10P08':47,'S10P09':61,'S10P12':60,'S06P11':58,'S06P06':31,'S08P07':32,'S05P05':25,'S05P08':24,'S05P09':23,
'S03P09':22,'S03P10':21,'S03P05':20,'S03P08':19,'S03P03':18})

explanations = {
'S22P04':'Direct authentic medieval scholarly text: Aquinas material is dependency-annotated at sentence/tree level, preserving Latin scholastic terminology and source structure; adaptation burden is mainly mapping parser relations to the project schema.',
'S24P10':'Authentic Quranic Arabic corpus with predicate-argument annotations and 7,227 verbal occurrences; strong provenance and historical-language fit, though PropBank roles need supplementation with tradition-specific argument forms.',
'S24P11':'Expert-constructed Quran/Hadith Classical Arabic material retains primary religious-text provenance and cross-domain distinctions; semantic-relatedness labels require added claim and dialectical annotation.',
'S22P08':'Authentic Medieval Latin corpus spanning genres, with evaluated POS/lemmatization resources; preserves historical language variation but offers indirect reasoning labels and requires substantial structural annotation.',
'S22P02':'Reusable Medieval Latin manuscript corpus grounded in scanned historical witnesses; excellent authenticity and preservation value, but HTR output must be converted into claims, evidence, and argument relations.',
'S24P09':'OpenITI-derived Classical Arabic resources are close to authentic scholarly and religious textual traditions with expert annotations; provenance and argument-structure layers remain to be added.',
'15-02':'Combines authentic philosophical texts with bibliometric intertextual relations and human evaluation; unusually strong philosophical-text authenticity, though the task targets intertextuality more than proof or dialectic.',
'12-06':'FOLIO uses human-authored premise sets with explicit FOL annotations and automated verification; authentic natural-language reasoning is preserved, but philosophical/historical tradition coverage is limited.',
'S10P07':'Manually annotated Walton-scheme corpus exposes authentic argumentative language and scheme labels; strong form fit, but source texts are not specifically scholastic and provenance depth is limited.',
'S23P12':'Large manually curated complex argument-tree corpus preserves real argumentative structure, stance, and specificity; adaptation to scholastic texts is moderate and mainly needs tradition-aware labels.',
'18_10':'Deep argumentative structures corpus contains natural argumentative text with nested relations; good authenticity and structural value, but source tradition and provenance are less specialized than scholastic corpora.',
'18_11':'Causal-link annotations target implicit reasoning in real arguments; useful for reconstructing omitted premises while requiring additional source-critical and cross-tradition distinctions.',
'S23P04':'Tree-structured debate corpus carries real debate structure and argument metadata; supports dialectical adaptation, but generated/evaluation framing and non-scholastic topics reduce historical authenticity.',
'S09P08':'QT-SCHEMES contains dialogue arguments annotated with 24 schemes, giving authentic argumentative interaction and strong scheme coverage; limited historical-text provenance and only 441 arguments.',
'S25P13':'QT-SCHEMES is a compact argument-mining resource with 441 dialogue arguments and 24 scheme labels; useful dialectical evidence, but dialogue is not equivalent to historical scholastic prose.',
'S25P14':'Manually annotated and generated enthymeme material exposes implicit premises and scheme classification; generated portions raise authenticity concerns and require tradition-preserving adaptation.',
'11-08':'MISSCI PLUS grounds fallacy work in real scientific-study passages with retrieval and fact-checking; strong scholarly-text grounding, but biomedical publication discourse is adjacent to philosophy and dialectic.',
'11-04':'Annotated political-debate corpus includes claims, premises, support/attack, and fallacy spans from real discourse; authentic argument structure is strong, while genre and tradition differ from scholastic texts.',
'11-06':'Pairs misinformation claims with cited biomedical publications and implicit-fallacy reconstruction; excellent source/evidence grounding, but scientific misinformation is not historical philosophical argument.',
'S24P12':'Quran/Hadith QA corpora retain authentic religious source domains and explicit source distinctions; question answering is shallower than argument reconstruction and needs provenance-aware claim labels.',
'S25P12':'MARS directly targets metaphysical reasoning and is philosophically aligned; benchmark-task construction may be synthetic and lacks the historical textual provenance needed for tradition-sensitive evaluation.',
'15-05':'Operationalizes the philosophical frame and symbol-grounding problems; conceptually authentic to philosophy, but zero-shot prompts are generic and not tied to recoverable source-text arguments.',
'15-08':'AMAeval evaluates moral reasoning chains with deductive and abductive structure; philosophical relevance is high, but benchmark scenarios are framework-driven rather than authentic historical scholarship.',
'S23P05':'Scientific comparative-analysis debate set tests multi-persona reasoning over papers; source-linked academic context helps, but persona/debate construction adds synthetic mediation.',
'14-08':'LeanDojo/ReProver provides theorem-proving premise retrieval and proof dependencies; excellent formal context selection diagnostic, but formal Lean artifacts are not natural scholarly or philosophical prose.',
'S08P04':'LeanDojo proof data and premise annotations expose theorem dependencies; strong structural control benchmark, yet formalized mathematics imposes high adaptation burden and erases textual tradition distinctions.',
'S08P05':'Isabelle proof-state and relevant-premise pairs are highly traceable and dependency-rich; useful for compression/provenance controls, but machine-formal proof states are far from authentic historical text.',
'S07P08':'LeanDojo interaction data offers large-scale theorem/proof instances and premise annotations; validates formal reasoning and selection, not authenticity of philosophical or historical language.',
'S07P01':'ProofWriter exposes natural-language rules, proofs, and abduction with exact derivations; valuable synthetic structural control, but generated rule worlds do not preserve scholarly text or traditions.',
'12-04':'ProofWriter supplies enumerated proofs, open/closed-world settings, and abduction; high reasoning diagnosticity but explicitly synthetic rule theories with no historical or philosophical provenance.',
'12-05':'LogicNLI diagnoses first-order reasoning in natural language; some surface naturalness, yet task worlds are logic-focused and lack authentic scholarly source chains.',
'12-11':'SylloBase offers natural-language categorical syllogisms with paraphrases and manually rewritten tests; useful form control, but template origin and limited context reduce text authenticity.',
'12-12':'NeuBAROCO includes English/Japanese syllogism items and indeterminate cases; natural-language variation helps, but psychological syllogism prompts are not authentic scholarly argument sources.',
'12-15':'Abductive/deductive syllogism labels and contradiction metadata support reasoning-form tests; dataset conversion and belief categories impose synthetic abstraction over source text.',
'11-01':'LOGIC and LOGIC_CLIMATE provide fallacy labels in natural language; useful argumentative control, but task emphasis is classification and source-tradition authenticity is not established.',
'S10P09':'Manually curated Kialo arguments and eight Walton classes provide real user-authored argumentation; authenticity is better than generation, but platform debate is contemporary and non-scholastic.',
'S10P12':'Annotated/generated Walton sets include enthymemes useful for implicit-premise recovery; generated material and mixed provenance lower authenticity despite strong scheme alignment.',
'S06P11':'Annotated reasoning trajectories expose faithfulness failures across domains; traceability is valuable, but trajectories are model outputs rather than authentic scholarly texts.',
'12-08':'BIG-bench includes logical deduction, syllogism, and fallacy tasks; broad coverage gives controls, but heterogeneous task construction and generic evaluation limit scholarly authenticity.',
'19_06':'E-KAR evaluates natural-language analogical reasoning with rationales; argument-like explanations help, but benchmark items are task-engineered rather than historical or philosophical sources.',
'19_04':'InAbHyD targets inductive and abductive hypothesis reasoning; useful adjacent diagnostic, but benchmark instances are not grounded in scholarly text or tradition-specific evidence.',
'19_12':'AnaloBench tests abstract and long-context analogy identification; context stress is useful, yet examples are benchmark-constructed and not authentic philosophical intertextuality.',
'19_09':'ANALOGICAL evaluates long-text analogies and offers context stress; long documents help adaptation, but benchmark content is not established as historical or scholarly source text.',
'19_15':'Complex-analogy benchmark probes relational analogies; reasoning depth is relevant, but its task framing is synthetic and lacks provenance or tradition distinctions.',
'19_10':'StoryAnalogy derives story-level analogies; supports narrative transfer only indirectly and does not provide authentic scholarly argument or historical provenance.',
'19_14':'KnowledgePrompts contains proportional analogies with knowledge enhancement; useful analogy control, but prompt-style instances are generic and not scholarly text.',
'19_02':'Knowledge-graph hypothesis generation supports abductive reasoning over structured facts; high adaptation burden and little direct evidence of authentic philosophical or historical prose.',
'S10P08':'NLAS-multi covers 20 Walton schemes across bilingual generated arguments; broad scheme variety is useful, but generation weakens authenticity and can flatten tradition-specific distinctions.',
'17_15':'SANSKRITI targets Indian cultural knowledge and is potentially useful for cultural context controls; it is generic benchmark QA rather than authentic philosophical or scholastic text.',
'17_14':'DRISHTIKON tests multilingual Indian-culture understanding; cultural breadth helps adaptation checks, but multimodal QA does not preserve source-text argument structure.',
'17_13':'Arab-culture commonsense data supplies regional context; it is not a scholarly corpus and offers little provenance, dialectic, or philosophical-text authenticity.',
'17_01':'LogiQA uses natural-language logical reasoning questions; useful generic reasoning control, but question passages are not authentic scholarly or philosophical source texts.',
'17_02':'LogiQA 2.0 improves logical reasoning data scale and quality; remains exam-style QA with limited provenance and no historical-tradition preservation.',
'17_09':'SeaEval includes multilingual and cultural reasoning; useful cross-cultural control, but generic evaluation prompts do not expose authentic scholarly argument chains.',
'17_11':'Global MMLU broadens multilingual/cultural evaluation; coverage is generic QA and cannot directly test source provenance or scholastic distinctions.',
'17_12':'CQ-Bench probes implicit cultural values; culturally relevant but primarily judgment/QA items rather than authentic philosophical or historical texts.',
'17_08':'WorldValuesBench evaluates multicultural value awareness at scale; value coverage is adjacent, while synthetic question framing limits scholarly authenticity.',
'17_07':'CDEval measures cultural dimensions in model outputs; useful bias diagnostic but not a corpus of authentic philosophical or legal argumentation.',
'17_10':'LLM-GLOBE evaluates cultural values embedded in outputs; output judgments are generic and offer little source span, provenance, or tradition-specific argument structure.',
'17_04':'GeoMLAMA probes geo-diverse commonsense knowledge; regional variation is useful as a control, but benchmark statements are generic and non-scholarly.',
'17_03':'Mickey evaluates multilingual commonsense reasoning; broad language coverage does not substitute for authentic historical or philosophical source text.',
'15-06':'AwareBench/AwareEval asks awareness and self-model questions; philosophical vocabulary is present, but items are generic and lack source-grounded argument provenance.',
'S08P07':'MALLS/LogicLLaMA maps sentences to first-order logic; explicit formalization supports structure checks, but sentence-level data is not authentic scholarly discourse.',
'S06P06':'Counterfactual suite spans logic and other domains; it tests reasoning robustness, yet heterogeneous engineered tasks are far from historical/philosophical text authenticity.',
'12-03':'RuleTaker uses theorem-prover-generated theories and depth-controlled labels; excellent synthetic deduction control, but no authentic source text or tradition preservation.',
'12-07':'PrOntoQA generates first-order worlds and proof chains; isolates proof depth and faithfulness while explicitly sacrificing scholarly-text authenticity.',
'S02P05':'FalseQA uses human-written false-premise questions and explanations; natural language is authentic at sentence level, but benchmark purpose is premise critique rather than scholarly argument recovery.',
'S02P07':'PCBench tests premise critique across error types and difficulty levels; useful boundary condition, but generic questions lack historical source provenance and dialectical structure.',
'S02P06':'KG-FPQ scales knowledge-graph false-premise questions across domains; factuality focus and generated/structured premises make it a weak fit for authentic scholarly text.',
'S05P05':'ALCE tests retrieval and citation generation; citation grounding is relevant, but benchmark answers and web evidence are generic rather than philosophical or historical scholarship.',
'S05P08':'RAGTruth provides hallucination annotations over RAG responses; useful grounding control, but model responses are not authentic source texts and argument structure is secondary.',
'S05P09':'MultiHop-RAG supplies multi-hop questions and supporting evidence; evidence chains are relevant, yet QA framing and knowledge-base construction limit scholarly authenticity.',
'S03P09':'NoLiMa tests semantic retrieval at long context; useful context control, but no inherent philosophical, historical, or scholarly-text content.',
'S03P10':'LongPiBench isolates distance between relevant information pieces; positional-bias diagnostic is valuable, but content is benchmark-engineered rather than authentic scholarship.',
'S03P05':'LongBench covers bilingual long-context QA and summarization; context stress is relevant, while heterogeneous generic tasks lack argument/provenance authenticity.',
'S03P08':'RULER tests long-context retrieval, tracing, and aggregation; excellent context control but synthetic task structure and weak scholarly-text fit.',
'S03P03':'LRA measures long-range sequence processing across generic tasks; it provides no direct scholarly or philosophical text authenticity.',
'S03P06':'∞Bench stresses contexts beyond 100K tokens; scale is useful for long-source controls, but content and tasks are not inherently scholarly or philosophical.',
'11-05':'LOGICOM uses paired logical and fallacious arguments in multi-round persuasion; argument manipulation is relevant, but instances are benchmark-constructed rather than historically sourced.',
'11-12':'SMARTYPAT-BENCH combines Reddit posts with symbolic Prolog oracles; real user text helps authenticity, but platform discourse and oracle generation do not preserve scholarly traditions.',
}

with infile.open(newline='', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))
assert len(rows) == 80
missing = [r['paper_id'] for r in rows if r['paper_id'] not in scores or r['paper_id'] not in explanations]
assert not missing, missing

for r in rows:
    r['reviewer_slug'] = slug
    r['viewpoint'] = viewpoint
    r['score_0_100'] = str(scores[r['paper_id']])
    r['confidence'] = 'high' if r['paper_id'] in {'S22P04','S24P10','S24P11','S22P08','S22P02','S24P09','15-02','12-06','S10P07','S23P12','18_10','18_11','S23P04','S09P08','S25P13','S25P14','11-08','11-04','11-06','S24P12'} else 'medium'
    r['explanation'] = explanations[r['paper_id']]
    r['evidence_basis'] = 'benchmark_studies.csv evidence: ' + r['evidence']

key = lambda r: (-int(r['score_0_100']), int(r['category_num']), int(r['paper_order']), r['paper_id'])
global_sorted = sorted(rows, key=key)
for i, r in enumerate(global_sorted, 1): r['global_rank'] = str(i)
cat_sorted = sorted(rows, key=lambda r: (int(r['category_num']), -int(r['score_0_100']), int(r['paper_order']), r['paper_id']))
for cat in sorted({r['category_num'] for r in rows}, key=int):
    rank = 0
    for r in [x for x in cat_sorted if x['category_num'] == cat]:
        rank += 1
        r['category_rank'] = str(rank)

cols = ['paper_id','category_num','category','paper_order','citation','benchmark_status','benchmark_name','benchmark_type','reviewer_slug','viewpoint','category_rank','global_rank','score_0_100','confidence','explanation','evidence_basis']
for name in [f'benchmark_review_{slug}_category.csv', f'benchmark_review_{slug}_global.csv']:
    with (base / name).open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rows:
            w.writerow({c:r[c] for c in cols})

top15 = [{'rank': i, 'paper_id': r['paper_id'], 'benchmark_name': r['benchmark_name'], 'score': int(r['score_0_100'])} for i,r in enumerate(global_sorted[:15],1)]
result = {
    'reviewer_slug': slug,
    'viewpoint': viewpoint,
    'benchmark_universe': 'benchmark_studies.csv',
    'rows': len(rows),
    'scoring_definition': ['authentic scholarly/philosophical source text', 'source provenance and traceability', 'preservation of historical/tradition distinctions', 'argument/dialectical structure', 'adaptation burden penalty', 'synthetic or generic QA penalty'],
    'top_15': top15,
    'notes': 'Scores rank text authenticity perspective, not general benchmark prestige. Authentic Medieval Latin, Classical Arabic, Quran/Hadith, philosophical, and manually annotated argument corpora lead; formal rule worlds and generic QA remain controls.',
}
(base / f'results_{slug}.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

notes = '''# Scholarly/philosophical text fit review\n\n- Viewpoint: authentic philosophical, historical, legal, dialectical, argument-mining, or academic text fit.\n- Highest scores: authentic Medieval Latin, Classical Arabic, Quran/Hadith, philosophical intertextuality, and manually annotated argument corpora.\n- Middle scores: real debate/science/fallacy corpora and natural-language logic with useful structure but weaker tradition provenance.\n- Lower scores: formal theorem/rule worlds, generated analogy/scheme tasks, generic cultural QA, RAG/long-context controls, and premise/factuality tests.\n- Adaptation rule: do not erase source language, genre, citation chain, or tradition-specific distinctions when projecting into claim/evidence/argument schemas.\n- Validation: 80 input rows, 25 categories, contiguous category ranks, unique global ranks 1-80, deterministic tie-break `(category_num, paper_order, paper_id)`.\n'''
(base / f'notes_{slug}.md').write_text(notes, encoding='utf-8')
print(json.dumps({'rows':len(rows), 'top':top15[:5], 'files':[f'benchmark_review_{slug}_category.csv',f'benchmark_review_{slug}_global.csv',f'results_{slug}.json',f'notes_{slug}.md']}))
