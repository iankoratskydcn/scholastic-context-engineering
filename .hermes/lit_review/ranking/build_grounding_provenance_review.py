import csv, json, re
from pathlib import Path

root = Path(__file__).resolve().parent
src = root / 'benchmark_studies.csv'
rows = list(csv.DictReader(src.open(newline='', encoding='utf-8-sig')))
assert len(rows) == 80, len(rows)

cat_base = {
    '2': 58, '3': 62, '5': 72, '6': 55, '7': 70, '8': 72, '9': 68,
    '10': 66, '11': 70, '12': 68, '14': 78, '15': 52, '17': 35,
    '18': 65, '19': 58, '22': 38, '23': 58, '24': 40, '25': 55,
}
manual = {
    'S05P05': 98, 'S05P09': 95, 'S05P08': 91,
    '11-08': 96, '11-06': 88, '11-04': 83,
    '14-08': 90, 'S07P08': 89, 'S07P01': 82,
    '12-06': 84, '12-04': 81, '12-05': 76, '12-15': 66,
    'S09P08': 80, 'S10P07': 78, 'S10P09': 76, 'S10P08': 67,
    '18_10': 74, '18_11': 72,
    'S23P12': 78, 'S23P04': 62, 'S23P05': 58,
    'S25P13': 80, 'S25P14': 75, 'S25P12': 55,
    'S24P10': 60, 'S24P11': 50, 'S24P12': 48, 'S24P09': 42,
    'S22P04': 52, 'S22P10': 47, 'S22P08': 38,
    '19_06': 68, '19_12': 63, '19_09': 60, '19_04': 57,
    '19_10': 51, '19_14': 50, '19_15': 54, '19_02': 48,
    'S03P09': 78, 'S03P10': 75, 'S03P08': 72, 'S03P05': 59,
    'S03P06': 57, 'S03P03': 55,
    'S02P05': 70, 'S02P06': 67, 'S02P07': 73,
    'S06P11': 78, 'S06P06': 62,
    'S08P05': 84, 'S08P07': 70, 'S08P04': 76,
    '17_01': 56, '17_02': 50, '17_03': 33, '17_04': 32, '17_07': 34,
    '17_08': 30, '17_09': 39, '17_10': 31, '17_11': 38, '17_12': 35,
    '17_13': 30, '17_14': 32, '17_15': 31,
}

def score(r):
    pid = r['paper_id']
    if pid in manual:
        return manual[pid]
    name = (r['benchmark_name'] + ' ' + r['benchmark_type'] + ' ' + r['evidence']).lower()
    s = cat_base.get(r['category_num'], 45)
    if any(x in name for x in ['citation', 'grounded', 'supporting evidence', 'passage', 'provenance', 'retrieval']): s += 12
    if any(x in name for x in ['proof', 'premise', 'logic', 'argument', 'fallacy', 'scheme']): s += 8
    if any(x in name for x in ['qa', 'question answering', 'commonsense', 'values', 'culture']): s -= 8
    if any(x in name for x in ['synthetic', 'template', 'generated']): s -= 5
    if r['confidence'] == 'medium': s -= 2
    return max(15, min(94, s))

def kind(r, s):
    n = (r['benchmark_name'] + ' ' + r['benchmark_type']).lower()
    if any(x in n for x in ['citation', 'rag', 'retrieval', 'passage', 'grounding', 'provenance']): return 'retrieval/citation'
    if any(x in n for x in ['proof', 'logic', 'syllog', 'theorem', 'premise', 'fallacy', 'argument', 'scheme', 'reasoning']): return 'argument/proof'
    return 'generic QA/corpus'

def explanation(r, s):
    pid, n, typ = r['paper_id'], r['benchmark_name'], r['benchmark_type']
    k = kind(r, s)
    if pid == 'S05P05': return 'Direct citation-grounded generation test: systems retrieve support, answer, and attach citations, with separate correctness and citation-quality signals. It is the strongest direct benchmark for claim-to-source support, though citation completeness is not full proof validity.'
    if pid == 'S05P09': return 'Direct multi-hop evidence test: queries require multiple supporting pieces and the benchmark exposes both retrieval failure and answer failure. It directly tests support-set recall and chain preservation, but remains constrained QA.'
    if pid == 'S05P08': return 'Direct span-level grounding audit: RAG responses carry word/case-level unsupported or contradictory annotations. It tests local evidence traceability better than answer-only QA, but not full argument structure.'
    if pid == '11-08': return 'Direct evidence-grounded fallacy benchmark: passage retrieval is paired with verbalization and fact-checking over real biomedical source passages. It tests whether selected evidence supports or merely appears to support a claim, with curated-domain limits.'
    if pid == '14-08': return 'Direct premise-provenance benchmark: theorem proving couples retrieval with fine-grained accessible-premise annotations and hard negatives. Lean gives a strict proof oracle, but formal-library provenance is narrower than scholarly argumentation.'
    if pid == 'S07P08': return 'Strong proof-and-retrieval benchmark: theorem instances, accessible premises, hard negatives, and proof outcomes make provenance and dependency preservation inspectable. It is formal rather than interpretive.'
    if pid == 'S07P01' or pid == '12-04': return 'Strong proof benchmark: enumerated proof chains and depth-controlled inference expose dependency recovery and multi-step reasoning. Synthetic rule theories limit authenticity and source provenance.'
    if pid == '12-06': return 'Strong natural-language deduction benchmark with human-authored premises, FOL annotations, and automated verification. It supports entailment traceability, but not citation retrieval or minimal evidence selection.'
    if pid == '11-06': return 'Evidence-linked fallacy benchmark pairing misinformation claims with cited biomedical publications and reconstruction of the unsupported bridge. It tests source-grounded reasoning, though the domain and task are curated.'
    if pid == '11-04': return 'Argument-structure corpus with token spans, claims, premises, and support/attack relations. It is useful for evidence-span and relation provenance, but does not itself require retrieval or citation generation.'
    if pid in {'S09P08','S10P07','S10P09','S25P13','S25P14','S23P12','18_10','18_11'}:
        return f'Argument-structure benchmark: {n} supplies annotated components, schemes, relations, or implicit links that support traceable claim/evidence evaluation. It is an argument/proof diagnostic, not a citation-grounded retrieval test.'
    if k == 'retrieval/citation':
        return f'Adjacent retrieval/grounding diagnostic: {n} stresses {typ or "evidence selection or support"}. It tests retrieval or context use more directly than generic QA, but does not provide complete claim-level provenance.'
    if k == 'argument/proof':
        return f'Argument/proof diagnostic: {n} stresses {typ or "structured reasoning"}. It can test dependency or inference traceability, but offers limited direct citation/retrieval coverage.'
    return f'Generic QA/corpus benchmark: {n} primarily measures {typ or "task performance"}. It may provide domain or language stress, but has weak direct grounding, evidence-span, and provenance coverage.'

def evidence(r):
    cat = int(r['category_num'])
    summary = f'summaries/{cat:02d}_'
    # Actual filenames have descriptive suffixes; retain supplied benchmark evidence plus stable summary folder pointer.
    return f"benchmark_studies.csv evidence: {r['evidence']} Summary basis: .hermes/lit_review/summaries/ category {r['category_num']} retained-paper summaries; benchmark identity/name/type preserved literally."

for r in rows:
    r['_score'] = score(r)
    r['_explanation'] = explanation(r, r['_score'])
    r['_evidence_basis'] = evidence(r)
    r['_kind'] = kind(r, r['_score'])

def key(r):
    return (-r['_score'], int(r['category_num']), int(r['paper_order']), r['paper_id'])

bycat = {}
for r in sorted(rows, key=lambda x: (int(x['category_num']), int(x['paper_order']), x['paper_id'])):
    bycat.setdefault(r['category_num'], []).append(r)
for group in bycat.values():
    for i, r in enumerate(sorted(group, key=key), 1):
        r['category_rank'] = i
for i, r in enumerate(sorted(rows, key=key), 1):
    r['global_rank'] = i

fields = ['paper_id','category_num','category','paper_order','citation','benchmark_status','benchmark_name','benchmark_type','reviewer_slug','viewpoint','category_rank','global_rank','score_0_100','confidence','explanation','evidence_basis']
for r in rows:
    r['reviewer_slug'] = 'grounding_provenance'
    r['viewpoint'] = 'RAG grounding, evidence retrieval, citation support, multi-hop support, and provenance traceability'
    r['score_0_100'] = r.pop('_score')
    r['explanation'] = r.pop('_explanation')
    r['evidence_basis'] = r.pop('_evidence_basis')
    r.pop('_kind', None)

cat_out = root / 'benchmark_review_grounding_provenance_category.csv'
global_out = root / 'benchmark_review_grounding_provenance_global.csv'
with cat_out.open('w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=fields); w.writeheader()
    for r in sorted(rows, key=lambda x: (int(x['category_num']), int(x['category_rank']), x['paper_id'])): w.writerow({k:r[k] for k in fields})
with global_out.open('w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=fields); w.writeheader()
    for r in sorted(rows, key=lambda x: int(x['global_rank'])): w.writerow({k:r[k] for k in fields})

out_json = root / 'results_grounding_provenance.json'
top = sorted(rows, key=lambda x: int(x['global_rank']))[:20]
summary = {
    'reviewer_slug':'grounding_provenance', 'rows':len(rows),
    'perspective':'grounding, evidence retrieval, citation support, multi-hop support, provenance traceability',
    'distinctions':{'retrieval_citation':sum(kind(r, int(r['score_0_100']))=='retrieval/citation' for r in rows), 'argument_proof':sum(kind(r, int(r['score_0_100']))=='argument/proof' for r in rows), 'generic_qa_corpus':sum(kind(r, int(r['score_0_100']))=='generic QA/corpus' for r in rows)},
    'top20':[{'global_rank':int(r['global_rank']),'paper_id':r['paper_id'],'benchmark_name':r['benchmark_name'],'score_0_100':int(r['score_0_100'])} for r in top],
    'validation':{'all_rows_from_benchmark_studies':True,'category_ranks_contiguous':all([sorted(int(x['category_rank']) for x in g)==list(range(1,len(g)+1)) for g in bycat.values()]),'global_ranks_contiguous':sorted(int(r['global_rank']) for r in rows)==list(range(1,81))}
}
out_json.write_text(json.dumps(summary, indent=2), encoding='utf-8')
print(json.dumps({'rows':len(rows),'top5':summary['top20'][:5],'category_out':str(cat_out),'global_out':str(global_out),'json_out':str(out_json)}))
