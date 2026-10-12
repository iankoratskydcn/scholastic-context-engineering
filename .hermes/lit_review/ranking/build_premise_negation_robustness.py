import csv, json, os
from collections import defaultdict

BASE = os.path.dirname(__file__)
SRC = os.path.join(BASE, 'benchmark_studies.csv')
SLUG = 'premise_negation_robustness'
VIEW = 'implicit-premise, negation, contradiction, false-premise, and logical-error robustness for philosophical reasoning'

# Scores reflect directness and diagnostic isolation of premise/negation/error behavior.
SCORES = {
    'S02P07': 99, 'S02P05': 97, 'S02P06': 95,
    '12-06': 94, '12-05': 93, '12-04': 92, 'S07P01': 91,
    '11-12': 90, '12-03': 89, '12-11': 87, '12-15': 86,
    '11-05': 85, 'S06P06': 84, '12-07': 83, '12-08': 72, '12-12': 81,
    '11-06': 80, '11-08': 79, '11-01': 78, '11-04': 76,
    '14-08': 74, 'S08P05': 73, 'S08P07': 71, 'S07P08': 70, 'S08P04': 70,
    'S10P12': 69, 'S25P14': 68, 'S09P08': 67, 'S25P13': 67,
    '18_11': 66, '18_10': 64, 'S10P07': 63, 'S10P09': 62,
    'S10P08': 58, '19_02': 60, '19_04': 59, '19_06': 57, '19_12': 56,
    '19_15': 55, '19_09': 53, '19_10': 51, '19_14': 50,
    'S25P12': 54, '15-08': 52, '15-05': 44, '15-02': 42, '15-06': 38,
    'S23P12': 48, 'S23P04': 46, 'S23P05': 45,
    '17_01': 47, '17_02': 45, '17_03': 35, '17_04': 31, '17_07': 30,
    '17_08': 29, '17_09': 32, '17_10': 28, '17_11': 34, '17_12': 36,
    '17_13': 30, '17_14': 27, '17_15': 28,
    'S05P09': 43, 'S05P08': 41, 'S05P05': 39,
    'S03P09': 37, 'S03P10': 35, 'S03P08': 33, 'S03P03': 29, 'S03P05': 28, 'S03P06': 27,
    'S06P11': 49,
    'S22P04': 25, 'S22P02': 18, 'S22P08': 17,
    'S24P10': 22, 'S24P11': 20, 'S24P12': 19, 'S24P09': 16,
}

DIRECT = {
    'S02P07': 'PCBench has four premise-error types and three difficulty levels, directly isolating premise critique.',
    'S02P05': 'FalseQA uses human-written false premises plus explanations and revised true-premise controls, directly testing refusal, correction, and contradiction handling.',
    'S02P06': 'KG-FPQ explicitly varies false-premise confusability and task format at scale, making premise acceptance and factual contradiction measurable.',
    '12-06': 'FOLIO pairs human-authored premise sets with FOL annotations and verification, enabling controlled negation, contradiction, and invalid-inference probes.',
    '12-05': 'LogicNLI is designed to diagnose first-order logical reasoning and robustness, making contradiction and quantifier/negation failures visible.',
    '12-04': 'ProofWriter supplies true/false/unknown labels, open- and closed-world variants, proof traces, and abduction; premise omission and contradiction are separable.',
    'S07P01': 'ProofWriter exposes implication chains and proof/abduction structure, supporting premise sufficiency, negation, and derivation-error diagnosis.',
    '11-12': 'SMARTYPAT-BENCH combines fine-grained fallacy labels with symbolic Prolog oracles, directly testing logical-error recognition against controlled cases.',
    '12-03': 'RuleTaker controls rule depth and true/false/unknown conclusions, giving strong premise and contradiction stress but limited authentic prose.',
    '12-11': 'SylloBase tests categorical syllogism validity with paraphrased and manually rewritten items, useful for premise order, negation, and invalid-form errors.',
    '12-15': 'The abductive syllogism dataset labels deductive versus abductive readings, contradictions, and belief categories, directly separating inference modes.',
    '11-05': 'LOGICOM pairs logical and fallacious arguments in multi-round persuasion, exposing susceptibility to contradiction and fallacious premises.',
    'S06P06': 'Counterfactual variants stress premise changes and consistency across alternate worlds, useful for detecting premise anchoring and contradiction errors.',
    '12-07': 'PrOntoQA controls first-order proof depth and generated worlds, isolating multi-step premise tracking while remaining synthetic.',
    '12-12': 'NeuBAROCO includes indeterminate psychological syllogisms and multilingual items, testing uncertainty and invalid-premise handling.',
    '11-06': 'MISSCI reconstructs implicit fallacies from misinformation claims and biomedical sources, linking premise errors to evidence-grounded reasoning.',
    '11-08': 'MISSCI PLUS adds passage grounding to fallacy reconstruction, testing whether models reject unsupported or contradictory premises.',
    '11-01': 'LOGIC and LOGIC_CLIMATE label fallacy types, providing broad logical-error coverage but weaker explicit premise-negation controls.',
    '11-04': 'The debate extension annotates claims, premises, support, and attack relations, enabling contradiction and premise-link analysis in political text.',
}

def generic(r):
    n = r['benchmark_name'] or r['citation']
    typ = r['benchmark_type'] or 'benchmark resource'
    s = SCORES[r['paper_id']]
    if s >= 60:
        return f'{n} provides {typ} material with some premise, inference, or contradiction structure, but evidence does not show a dedicated negation/false-premise diagnostic at the same granularity as premise-critique benchmarks.'
    if s >= 35:
        return f'{n} offers adjacent reasoning or argument material, but its primary task is {typ}; premise, negation, and contradiction robustness are indirect or confounded with broader task knowledge.'
    return f'{n} primarily evaluates {typ}, not logical premise handling. It supplies little direct evidence for implicit-premise, negation, contradiction, or logical-error robustness.'

def confidence(r):
    return 'high' if r['paper_id'] in DIRECT or r['paper_id'] in {'14-08','S08P05','S08P07','S10P12','S25P14','S09P08','S25P13','18_11'} else ('medium' if SCORES[r['paper_id']] >= 35 else 'low')

with open(SRC, newline='') as f:
    rows = list(csv.DictReader(f))
assert len(rows) == 80
for r in rows:
    assert r['paper_id'] in SCORES, r['paper_id']
    r['score_0_100'] = SCORES[r['paper_id']]
    r['reviewer_slug'] = SLUG
    r['viewpoint'] = VIEW
    r['confidence'] = confidence(r)
    r['explanation'] = DIRECT.get(r['paper_id'], generic(r))
    r['evidence_basis'] = f"benchmark_studies.csv evidence: {r['evidence']}; retained paper/summary evidence used for benchmark task identity and labels."

key = lambda r: (-r['score_0_100'], int(r['category_num']), int(r['paper_order']), r['paper_id'])
global_rows = sorted(rows, key=key)
for i, r in enumerate(global_rows, 1):
    r['global_rank'] = i

bycat = defaultdict(list)
for r in global_rows:
    bycat[r['category_num']].append(r)
for cat, rs in bycat.items():
    for i, r in enumerate(rs, 1):
        r['category_rank'] = i

fields = ['paper_id','category_num','category','paper_order','citation','benchmark_status','benchmark_name','benchmark_type','reviewer_slug','viewpoint','category_rank','global_rank','score_0_100','confidence','explanation','evidence_basis']
# Category artifact preserves universe order, grouped by source category; global artifact sorted by score.
cat_rows = sorted(rows, key=lambda r: (int(r['category_num']), int(r['paper_order']), r['paper_id']))
for name, data in [('benchmark_review_premise_negation_robustness_category.csv', cat_rows), ('benchmark_review_premise_negation_robustness_global.csv', global_rows)]:
    with open(os.path.join(BASE, name), 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        w.writeheader(); w.writerows(data)

counts = defaultdict(int)
for r in rows:
    score = int(r['score_0_100'])
    if score >= 80: band='direct_high'
    elif score >= 60: band='direct_or_structural'
    elif score >= 35: band='adjacent'
    else: band='weak_or_unrelated'
    counts[band] += 1
out = {
    'reviewer_slug': SLUG,
    'viewpoint': VIEW,
    'benchmark_universe': 'benchmark_studies.csv',
    'rows': 80,
    'diagnostic_definition': ['implicit-premise recovery', 'explicit negation and quantifier handling', 'false-premise rejection/correction', 'contradiction and inconsistency detection', 'logical-error/fallacy diagnosis', 'separation of premise failure from answer failure'],
    'top_15': [{'rank': i, 'paper_id': r['paper_id'], 'benchmark_name': r['benchmark_name'], 'score_0_100': r['score_0_100']} for i,r in enumerate(global_rows[:15],1)],
    'bands': dict(counts),
    'interpretation': 'False-premise and premise-critique benchmarks rank highest because they directly manipulate premise truth and error type. Formal NLI/proof benchmarks follow because labels, proof traces, and true/false/unknown controls isolate contradiction and negation. Generic cultural, retrieval, long-context, OCR, and QA resources are capped when premise robustness is not the measured object.'
}
with open(os.path.join(BASE, 'results_premise_negation_robustness.json'), 'w') as f:
    json.dump(out, f, indent=2, ensure_ascii=False); f.write('\n')

with open(os.path.join(BASE, 'notes_premise_negation_robustness.md'), 'w') as f:
    f.write('# Premise, negation, contradiction, logical-error robustness\n\n')
    f.write('Ranking rule: reward benchmarks that manipulate premise truth, expose explicit negation/quantifier structure, label contradiction/unknown, provide proof or attack traces, or isolate fallacy/logical-error types. Penalize generic QA, retrieval, cultural knowledge, long-context, OCR, and language resources when premise robustness is incidental.\n\n')
    f.write('Top direct diagnostics: PCBench, FalseQA, KG-FPQ, FOLIO, LogicNLI, ProofWriter, SMARTYPAT-BENCH, RuleTaker, SylloBase, and the abductive syllogism dataset. FalseQA and KG-FPQ test rejection/correction of false premises; PCBench adds typed premise errors; FOLIO/LogicNLI/ProofWriter provide structured contradiction and derivation checks.\n\n')
    f.write('Limits: synthetic rule/proof benchmarks maximize diagnostic control but underrepresent authentic philosophical prose; argument/fallacy corpora improve implicit-premise realism but often lack exhaustive negation counterfactuals. Use this perspective with argument-form, grounding, and scholarly-text-fit reviews rather than alone.\n')
