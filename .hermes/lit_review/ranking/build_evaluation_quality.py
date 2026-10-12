import csv, json, re
from pathlib import Path

ROOT = Path(__file__).parent
IN = ROOT / 'benchmark_studies.csv'
OUT_CAT = ROOT / 'benchmark_review_evaluation_quality_category.csv'
OUT_GLOB = ROOT / 'benchmark_review_evaluation_quality_global.csv'
OUT_JSON = ROOT / 'results_evaluation_quality.json'
OUT_NOTES = ROOT / 'notes_evaluation_quality.md'

rows = list(csv.DictReader(IN.open(encoding='utf-8-sig', newline='')))
assert len(rows) == 80, len(rows)

# Evidence-driven priors: evaluation rigor, not topical relevance or release size.
exact = {
    'ProofWriter': 95, 'LeanDojo': 94, 'FOLIO': 93, 'RuleTaker': 91,
    'LogicNLI': 90, 'RULER': 90, 'LongBench': 88, 'ALCE': 88,
    'RAGTruth': 87, 'MultiHop-RAG': 86, 'LOGIC; LOGIC_CLIMATE': 85,
    'QT-SCHEMES': 84, 'EthiX': 84, 'NeuBAROCO': 84, 'LogiQA': 82,
    'LogiQA 2.0': 83, 'BIG-bench logical deduction/syllogism tasks': 83,
    'FalseQA': 81, 'PCBench': 81, 'KG-FPQ': 79, 'PrOntoQA': 82,
    'SylloBase': 80, 'SMARTYPAT-BENCH': 83, 'MISSCI': 80,
    'MISSCI PLUS': 82, 'MALLS/LogicLLaMA': 78,
    'Isabelle proof-state/relevant-premise pairs': 86,
    'US2016G1tvWALTON corpus': 82, 'NLAS-multi': 72,
    'Annotated/generated Walton-scheme sets': 70,
    'ElecDeb60To16 extension': 78, 'Counterfactual reasoning task suite': 78,
    'FAITHCOT-BENCH / FINE-COT': 80, 'Long Range Arena (LRA)': 84,
    '∞Bench': 80, 'NoLiMa': 83, 'LongPiBench': 84,
    'InterIDEAS': 68, 'frame/symbol-grounding zero-shot benchmark': 58,
    'AwareBench/AwareEval': 62, 'AMAeval': 67, 'MARS': 73,
    'Deep argumentative structures corpus': 76,
    'implicit-reasoning causal-link materials': 79,
    'InAbHyD': 76, 'E-KAR': 74, 'ANALOGICAL': 72,
    'StoryAnalogy': 67, 'AnaloBench': 75,
    'KnowledgePrompts 15K proportional-analogy dataset': 65,
    'complex-analogy benchmark': 68,
    'Mickey': 67, 'GeoMLAMA': 70, 'CDEval': 65,
    'WorldValuesBench': 64, 'SeaEval': 70, 'LLM-GLOBE': 63,
    'Global MMLU': 72, 'CQ-Bench': 66,
    'Arab-culture commonsense dataset': 60, 'DRISHTIKON': 64,
    'SANSKRITI': 64, 'CREMMA Medii Aevi': 72,
    'Index Thomisticus Treebank': 78, 'eFontes Medieval Latin corpus': 74,
    'tree-structured debate corpus': 68, 'Tree-of-Debate scientific comparison set': 63,
    '741-topic argument-tree corpus': 80, 'OpenITI-derived Classical Arabic corpus': 70,
    'Quranic Arabic PropBank': 75, 'Quran–Hadith Classical Arabic dataset': 66,
    'HAQA and QUQA': 68,
}

def num(x):
    m = re.search(r'\d+', str(x)); return int(m.group()) if m else 999

def summary_path(r):
    c = int(r['category_num'])
    # category summary naming follows repository convention
    names = {
      2:'02_logic_hallucination_summaries.md',3:'03_context_degradation_summaries.md',
      5:'05_rag_grounding_summaries.md',6:'06_cot_faithfulness_summaries.md',
      7:'07_neurosymbolic_summaries.md',8:'08_logic_theorem_provers_summaries.md',
      9:'09_argument_mining_summaries.md',10:'10_walton_schemes_nlp_summaries.md',
      11:'11_fallacy_detection_summaries.md',12:'12_deductive_benchmarks_summaries.md',
      14:'14_premise_context_selection_summaries.md',15:'15_philosophy_summaries.md',
      17:'17_cross_cultural_logic_summaries.md',18:'18_toulmin_defeasible_summaries.md',
      19:'19_abduction_analogy_summaries.md',22:'22_scholastic_digital_humanities_ai_summaries.md',
      23:'23_disputatio_dialectical_ai_summaries.md',24:'24_islamic_comparative_scholastic_ai_summaries.md',
      25:'25_ai_philosophy_dialectical_methods_summaries.md'}
    return names.get(c, f'{c:02d}_summaries.md')

def score(r):
    name = r['benchmark_name']
    if name in exact: return exact[name]
    # fallback by evidence/property rather than dataset size
    s = 55
    text = ' '.join(r.values()).lower()
    if any(k in text for k in ['annotat', 'manual', 'expert']): s += 8
    if any(k in text for k in ['proof', 'logic', 'argument', 'fallac']): s += 6
    if any(k in text for k in ['multilingual', 'cross-cultural', 'culture']): s += 2
    if 'synthetic' in text or 'generated' in text: s -= 4
    if 'benchmark' in r['benchmark_status']: s += 2
    return max(0, min(100, s))

def explanation(r, s):
    n = r['benchmark_name'] or 'Unnamed resource'
    t = (r['benchmark_type'] + ' ' + r['evidence']).lower()
    if n in {'ProofWriter','RuleTaker','PrOntoQA'}:
        return 'Controlled synthetic theories expose proof depth, rule composition, and exact labels; generated instances reduce ecological validity but improve repeatability and leakage control.'
    if n in {'LeanDojo','LeanDojo/ReProver','Isabelle proof-state/relevant-premise pairs'}:
        return 'Formal proof states, premise annotations, and checker-backed outcomes provide strong objective metrics and reproducible dependency-level diagnostics; domain transfer to prose reasoning remains limited.'
    if n in {'FOLIO','LogicNLI','LogiQA','LogiQA 2.0','BIG-bench logical deduction/syllogism tasks','NeuBAROCO','SylloBase'}:
        return 'Explicit logical labels and held-out evaluation support accuracy and robustness comparisons; natural-language or template construction gives useful diagnosis, but annotation and contamination details are less uniform than formal proof suites.'
    if n in {'RULER','LongBench','Long Range Arena (LRA)','∞Bench','NoLiMa','LongPiBench'}:
        return 'Multiple controlled context lengths, positions, or retrieval demands isolate long-context failure modes; task heterogeneity and mostly synthetic retrieval limits direct argument-pipeline validity.'
    if n in {'ALCE','RAGTruth','MultiHop-RAG','MISSCI','MISSCI PLUS'}:
        return 'Evidence/citation or hallucination annotations enable grounded metrics and error analysis; quality depends on source attribution and task-specific annotation, with limited philosophical-text coverage.'
    if n in {'QT-SCHEMES','US2016G1tvWALTON corpus','EthiX','ElecDeb60To16 extension','741-topic argument-tree corpus','Deep argumentative structures corpus','implicit-reasoning causal-link materials'}:
        return 'Human-authored argument structure and span/relation labels support agreement-aware component and scheme metrics; smaller or domain-specific corpora constrain statistical power and cross-domain generalization.'
    if n in {'LOGIC; LOGIC_CLIMATE','SMARTYPAT-BENCH','MISSCI PLUS'}:
        return 'Fine-grained labels plus controlled or source-grounded cases support error-stratified evaluation and adversarial diagnosis; coverage and artifact reproducibility need verification.'
    if n in {'FAITHCOT-BENCH / FINE-COT','Counterfactual reasoning task suite'}:
        return 'Perturbation-based tasks test invariance or trajectory faithfulness beyond answer accuracy; annotation burden and model/judge dependence limit certainty.'
    if n in {'CREMMA Medii Aevi','Index Thomisticus Treebank','eFontes Medieval Latin corpus','Quranic Arabic PropBank','OpenITI-derived Classical Arabic corpus'}:
        return 'Expert linguistic annotation and reusable structured labels support reproducible span or relation metrics; evaluation is rigorous for language tooling but only an indirect test of reasoning-pipeline quality.'
    if n in {'NLAS-multi','Annotated/generated Walton-scheme sets'}:
        return 'Broad scheme coverage supports controlled classification comparisons, but generated examples and unclear independent splits weaken authenticity and leakage resistance.'
    if n in {'Mickey','GeoMLAMA','CDEval','WorldValuesBench','SeaEval','LLM-GLOBE','Global MMLU','CQ-Bench','Arab-culture commonsense dataset','DRISHTIKON','SANSKRITI'}:
        return 'Cross-cultural coverage enables stratified comparison, but cultural validity, translation, annotator agreement, and contamination controls are less diagnostic for formal argument recovery.'
    if n in {'InterIDEAS','frame/symbol-grounding zero-shot benchmark','AwareBench/AwareEval','AMAeval','MARS'}:
        return 'Task-specific philosophical evaluation offers topical relevance, but limited independent validation, subjective scoring, or unclear split/leakage controls reduce statistical usefulness.'
    if n in {'InAbHyD','E-KAR','ANALOGICAL','StoryAnalogy','AnaloBench','KnowledgePrompts 15K proportional-analogy dataset','complex-analogy benchmark'}:
        return 'Structured analogy or abduction labels support targeted error analysis and controlled baselines; transfer to scholastic proof and provenance is indirect, with variable annotation and split evidence.'
    if n in {'tree-structured debate corpus','Tree-of-Debate scientific comparison set'}:
        return 'Debate-tree or expert-comparison structure supports multi-step and stance-sensitive evaluation, but small/domain-specific sets and human-judge dependence limit reproducibility.'
    if n in {'Quran–Hadith Classical Arabic dataset','HAQA and QUQA'}:
        return 'Domain-authored Arabic resources provide grounded evaluation material, but QA/relatedness targets and limited agreement or split evidence make them indirect diagnostics of argument structure.'
    return 'Reusable labeled material offers a possible evaluation target, but evidence for independent splits, leakage controls, agreement, and objective metrics is incomplete; treat as an adjacent diagnostic.'

for r in rows:
    r['_score'] = score(r)
    r['_explanation'] = explanation(r, r['_score'])
    r['_summary'] = summary_path(r)
    r['_confidence'] = 'high' if r['confidence']=='high' and r['_score']>=80 else ('medium' if r['_score']>=65 else 'low')

# Canonical tie-breaking required by protocol.
for r in rows:
    r['_key'] = (-r['_score'], num(r['category_num']), num(r['paper_order']), r['paper_id'])
global_rows = sorted(rows, key=lambda r:r['_key'])
for i,r in enumerate(global_rows, 1): r['global_rank'] = i
by_cat = {}
for r in sorted(rows, key=lambda x:(num(x['category_num']),num(x['paper_order']),x['paper_id'])):
    by_cat.setdefault(r['category_num'], []).append(r)
for cat, rr in by_cat.items():
    rr.sort(key=lambda r:(-r['_score'],num(r['paper_order']),r['paper_id']))
    for i,r in enumerate(rr,1): r['category_rank'] = i

cols=['paper_id','category_num','category','paper_order','citation','benchmark_status','benchmark_name','benchmark_type','reviewer_slug','viewpoint','category_rank','global_rank','score_0_100','confidence','explanation','evidence_basis']
def emit(path, seq):
    with path.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=cols); w.writeheader()
        for r in seq:
            out={c:r.get(c,'') for c in cols}
            out['reviewer_slug']='evaluation_quality'; out['viewpoint']='evaluation quality and diagnostic rigor'
            out['score_0_100']=r['_score']; out['confidence']=r['_confidence']; out['explanation']=r['_explanation']
            out['evidence_basis']=f"{r['_summary']}; benchmark evidence: {r['evidence']}"
            w.writerow(out)
emit(OUT_CAT, sorted(rows,key=lambda r:(num(r['category_num']),r['category_rank'])))
emit(OUT_GLOB, global_rows)

payload={
 'input_rows':len(rows),'output_rows':len(rows),'reviewer_slug':'evaluation_quality',
 'viewpoint':'evaluation quality and diagnostic rigor','category_path':str(OUT_CAT),
 'global_path':str(OUT_GLOB),'top_global':[{'rank':r['global_rank'],'paper_id':r['paper_id'],'benchmark_name':r['benchmark_name'],'score':r['_score']} for r in global_rows[:10]],
 'score_range':[min(r['_score'] for r in rows),max(r['_score'] for r in rows)],
 'qa':{'missing_global_ranks':[i for i in range(1,81) if i not in {r['global_rank'] for r in rows}], 'duplicate_paper_ids':len(rows)-len({r['paper_id'] for r in rows}), 'category_rows':{k:len(v) for k,v in by_cat.items()}}
}
OUT_JSON.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
OUT_NOTES.write_text('''# Evaluation-quality ranking notes\n\n- Perspective: evaluation quality and diagnostic rigor. Scores reward diagnostic task design, annotation/label validity, split and leakage controls, perturbation coverage, baselines, objective metrics, reproducibility, and statistical usefulness. Dataset size or release status alone does not raise score.\n- Strongest candidates: formal checker-backed proof suites (LeanDojo, ProofWriter, FOLIO/LogicNLI), controlled long-context suites (RULER/LongPiBench), and grounded argument corpora with explicit spans/relations (QT-SCHEMES, Walton, argument-tree resources).\n- Caveat: many records are adjacent resources, not direct tests of full source-to-proof scholastic context engineering. Synthetic suites score for control and repeatability but lose authenticity; small expert corpora score for structural labels but lose statistical power.\n- Tie rule: global ranks sorted by score descending, then numeric category number, numeric paper order, literal paper_id.\n- Evidence basis preserves supplied benchmark evidence and points to retained category summaries.\n''',encoding='utf-8')
print(json.dumps(payload,indent=2,ensure_ascii=False))
