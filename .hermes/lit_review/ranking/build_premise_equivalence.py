import csv
from pathlib import Path

root = Path('/Users/iankoratsky/Documents/GitHub/scholastic-context-engineering')
rank = root / '.hermes/lit_review/ranking'
infile = rank / 'benchmark_studies.csv'
rows = list(csv.DictReader(infile.open(newline='')))

# Suitability for proposition-level equivalence, paraphrase identity, and cross-source
# claim/evidence matching. Scores are not general benchmark prestige scores.
scores = {
    'S02P07': 94,  # PCBench
    '11-08': 91,   # MISSCI PLUS
    'S05P08': 88,  # RAGTruth
    'S05P05': 85,  # ALCE
    '12-05': 83,   # LogicNLI
    '12-06': 81,   # FOLIO
    'S02P05': 79,  # FalseQA
    'S07P01': 78,   # ProofWriter
    '12-04': 78,   # ProofWriter duplicate/version
    'S18P10': 76,
    'S18P11': 75,
    '15-02': 73,   # InterIDEAS
    '11-06': 72,   # MISSCI
    'S05P09': 71,  # MultiHop-RAG
    'S02P06': 70,  # KG-FPQ
    '12-03': 69,   # RuleTaker
    '12-07': 68,   # PrOntoQA
    'S09P08': 67,
    'S10P08': 66,
    'S10P07': 64,
    'S10P12': 63,
    'S25P14': 63,
    'S25P13': 62,
    'S23P12': 61,
    'S23P04': 60,
    'S23P05': 59,
    'S06P11': 58,
    'S06P06': 57,
    'S03P05': 56,
    'S03P09': 55,
    'S03P08': 54,
    'S03P10': 53,
    'S03P03': 52,
    'S03P06': 51,
    'S08P05': 50,
    'S07P08': 49,
    'S08P04': 49,
    'S14P08': 48,
    'S08P07': 47,
    'S07P01': 78,
    'S15P05': 46,
    'S15P06': 45,
    'S15P08': 44,
    'S25P12': 43,
    'S19P04': 42,
    'S19P06': 41,
    'S19P02': 40,
    'S19P09': 39,
    'S19P10': 38,
    'S19P12': 37,
    'S19P14': 36,
    'S19P15': 35,
    '17_01': 34,
    '17_02': 33,
    '11-01': 32,
    '11-04': 31,
    '11-05': 30,
    'S10P09': 29,
    'S10P10': 28,
    'S03P05': 56,
    '17_03': 27,
    '17_04': 26,
    '17_07': 25,
    '17_08': 24,
    '17_09': 23,
    '17_10': 22,
    '17_11': 21,
    '17_12': 20,
    '17_13': 19,
    '17_14': 18,
    '17_15': 17,
    'S22P02': 16,
    'S22P04': 15,
    'S22P08': 14,
    'S24P09': 13,
    'S24P10': 12,
    'S24P11': 11,
    'S24P12': 10,
    'S07P08': 49,
}
# Correct aliases in source IDs where the inventory uses hyphen/underscore IDs.
scores.update({'14-08':48, '18_10':76, '18_11':75,
                '10-07':64, '10-08':66, '10-09':29, '10-12':63,
                '19_02':40, '19_04':42, '19_06':41, '19_09':39,
                '19_10':38, '19_12':37, '19_14':36, '19_15':35})
for r in rows:
    scores.setdefault(r['paper_id'], 10)

focus = {
    'S02P07': 'Directly tests whether a model can identify and explain malformed or unsupported premises across controlled error types; this is the closest retained diagnostic for premise-level failure, but it is not a cross-source equivalence task.',
    '11-08': 'Grounded fallacy annotations connect claims about scientific publications to supporting evidence and expose misrepresentation across source and claim levels. It is highly relevant to cross-source matching, although the target is fallacy reconstruction rather than binary proposition identity.',
    'S05P08': 'RAGTruth provides span-level claim and evidence annotations for unsupported or contradicted generated statements, making source-to-claim alignment and provenance auditable. It is an excellent grounding diagnostic but does not isolate paraphrase equivalence.',
    'S05P05': 'ALCE evaluates citation correctness and entailment between generated claims and cited source passages, directly exercising claim-to-source support matching. It is less useful for premise-premise equivalence because the task is generation with citations.',
    '12-05': 'LogicNLI isolates entailment, contradiction, and neutral relations under controlled first-order logic, which gives a clean proposition-identity boundary. Its synthetic logical language limits ecological validity for scholarly prose.',
    '12-06': 'FOLIO pairs natural-language premise sets with first-order-logic labels and explanations, enabling premise/conclusion entailment checks with human-authored language. It tests inference more than independent-source claim matching.',
    'S02P05': 'FalseQA tests whether systems notice false premises rather than blindly answer, useful for detecting polarity and premise validity errors. It is a question-answering diagnostic, not a pairwise equivalence benchmark.',
    'S07P01': 'ProofWriter supplies natural-language rules, facts, proofs, and open-world reasoning labels, supporting controlled entailment and contradiction checks. Its generated rule worlds are valuable diagnostics but are not authentic cross-document claims.',
    '12-04': 'The ProofWriter benchmark provides explicit proof traces and natural-language facts/rules for entailment-style reasoning. It is useful for verifying normalized propositions, but duplicate use should be tracked as a shared benchmark family with S07P01.',
    '18_10': 'Deep argumentative-structure annotations expose claims, relations, and implicit support across argument spans, which can test whether matched propositions preserve argumentative function. It lacks a dedicated same-premise/different-wording label.',
    '18_11': 'Causal-link annotations target implicit reasoning between argument components and can reveal when two source statements connect to the same underlying proposition. The resource is adjacent rather than a direct equivalence benchmark.',
    '15-02': 'InterIDEAS is the strongest retained resource for philosophical intertextuality and cross-source conceptual alignment. Its likely limitation is that intertextual similarity is broader than proposition-level truth-conditional equivalence.',
}

def sid_key(r):
    try:
        return (int(r['category_num']), int(r['paper_order']), r['paper_id'])
    except ValueError:
        return (999, 999, r['paper_id'])

# Ensure all rows have deterministic scores. Use category-specific baseline for non-direct resources.
for r in rows:
    if r['paper_id'] not in scores:
        bt = (r['benchmark_type'] + ' ' + r['category']).lower()
        scores[r['paper_id']] = 20 if any(x in bt for x in ['argument', 'logic', 'reason', 'ground', 'retriev', 'context']) else 10

# Add short, concrete explanations for every retained benchmark.
def explain(r):
    if r['paper_id'] in focus:
        return focus[r['paper_id']]
    name = r['benchmark_name'] or r['benchmark_type'] or 'This resource'
    t = (r['benchmark_type'] + ' ' + r['category']).lower()
    if any(x in t for x in ['long-context', 'context', 'retrieval', 'rag']):
        return f'{name} can stress retrieval or context placement around evidence, which is useful for a common-ground pipeline. It does not directly label whether two propositions from different sources are equivalent.'
    if any(x in t for x in ['logic', 'deduct', 'syllog', 'proof', 'reason']):
        return f'{name} provides a controlled reasoning or entailment diagnostic that can calibrate proposition normalization. Its formal or synthetic setting is not a direct cross-source claim-matching evaluation.'
    if any(x in t for x in ['argument', 'fallac', 'debate', 'scheme']):
        return f'{name} exposes argumentative spans or relations that can support claim alignment and dependency checks. It lacks a dedicated annotation for same-premise equivalence across independent sources.'
    if any(x in t for x in ['corpus', 'text', 'cultur', 'multilingual', 'arabic', 'latin']):
        return f'{name} offers authentic or cross-lingual text coverage relevant to source variation. It is primarily a corpus or downstream reasoning resource, not a premise-equivalence benchmark.'
    return f'{name} is an adjacent diagnostic for the pipeline, but its labels do not directly measure whether two source statements assert the same premise.'

# Rank globally by score then immutable tie-break.
for r in rows:
    r['reviewer_slug'] = 'premise_equivalence'
    r['viewpoint'] = 'Premise equivalence and cross-source claim matching for common-ground construction'
    r['score_0_100'] = str(scores[r['paper_id']])
    r['confidence'] = 'high' if scores[r['paper_id']] >= 70 else ('medium' if scores[r['paper_id']] >= 40 else 'low')
    r['explanation'] = explain(r)
    r['evidence_basis'] = r['evidence']

global_rows = sorted(rows, key=lambda r: (-int(r['score_0_100']), sid_key(r)))
for i, r in enumerate(global_rows, 1):
    r['global_rank'] = str(i)
# category ranks contiguous by category, with same global ordering within category
by_cat = {}
for r in sorted(global_rows, key=lambda r: (int(r['category_num']), -int(r['score_0_100']), sid_key(r))):
    by_cat.setdefault(r['category_num'], []).append(r)
for cat, rs in by_cat.items():
    for i, r in enumerate(rs, 1):
        r['category_rank'] = str(i)

cols = ['paper_id','category_num','category','paper_order','citation','benchmark_status','benchmark_name','benchmark_type','reviewer_slug','viewpoint','category_rank','global_rank','score_0_100','confidence','explanation','evidence_basis']
for suffix, ordered in [('global', global_rows), ('category', sorted(rows, key=lambda r: (int(r['category_num']), int(r['category_rank']))))]:
    out = rank / f'benchmark_review_premise_equivalence_{suffix}.csv'
    with out.open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction='ignore')
        w.writeheader(); w.writerows(ordered)

# Human-readable research note with external benchmark discovery.
report = rank / 'benchmark_review_premise_equivalence.md'
report.write_text('''# Premise equivalence and cross-source claim matching\n\n## Result\n\nThe retained 80-study benchmark inventory contains no purpose-built benchmark whose primary task is pairwise matching of claims that can be resolved by the same fact-check or premise. The strongest retained proxies are PCBench, MISSCI PLUS, RAGTruth, ALCE, LogicNLI, FOLIO, FalseQA, and ProofWriter; they cover premise critique, source grounding, entailment/contradiction, and proof traces but not the full cross-source equivalence decision.\n\nThe recommended common-ground battery should therefore combine a direct claim-matching resource with proposition-level NLI and source-grounding diagnostics. Treat semantic similarity alone as insufficient: matching claims may have low surface similarity, while high lexical overlap can conceal polarity, quantifier, temporal, or entity changes.\n\n## External benchmarks found\n\n| Benchmark/resource | What it tests | Fit for common ground | Main caveat | Scholarly source |\n|---|---|---|---|---|\n| Claim Matching Beyond English (Kazemi et al., ACL 2021) | Whether two textual messages containing claims can be served by one fact-check; multilingual WhatsApp tipline/public-group messages paired with fact-checked claims | **Direct** cross-source claim matching; best starting point for “same premise” clustering | Fact-check serviceability is broader than strict truth-conditional equivalence; social-media domain | https://aclanthology.org/2021.acl-long.347/ |\n| MultiClaim (Shaar et al., 2023) | Multilingual previously fact-checked claim retrieval | **Direct/near-direct** retrieval of paraphrased or reformulated claims across languages | Retrieval relevance is not an explicit equivalence label; inspect split and cluster construction | https://arxiv.org/abs/2305.07991 |\n| SciFact (Wadden et al., EMNLP 2020) | Select scientific abstracts that support/refute a claim and identify rationale sentences | **Direct for scholarly common ground**; source selection plus support/refute and rationale spans | Claim-to-evidence verification, not claim-pair matching; scientific abstracts only | https://aclanthology.org/2020.emnlp-main.609/ |\n| AVeriTeC (Schlichtkrull et al., NeurIPS 2023) | Real-world claim verification using web evidence and structured evidence annotations | **Direct for web-scale source alignment** and evidence provenance | Verdict/evidence task rather than premise identity; web snapshot and licensing details matter | https://proceedings.neurips.cc/paper_files/paper/2023/hash/cd86a30526cd1aff61d6f89f107634e4-Abstract.html |\n| FEVER (Thorne et al., NAACL 2018) | SUPPORTS/REFUTES/NOT ENOUGH INFO with Wikipedia evidence retrieval | Strong baseline for evidence selection and polarity checks | Claims are largely constructed from Wikipedia sentences; limited paraphrase diversity | https://aclanthology.org/N18-1074/ |\n| VitaminC (Schuster et al., NAACL 2021) | Contrastive fact verification over changed Wikipedia revisions | **High diagnostic value** for minimal edits, negation, and subtle premise changes | Revision-based Wikipedia setting; not independent scholarly sources | https://aclanthology.org/2021.naacl-main.52/ |\n| SciNLI (Sadat & Caragea, ACL 2022) | Entailment, contradiction, and neutral relations in scientific text | **High proposition-level calibration** for scholarly paraphrase and polarity | NLI pairs are not necessarily cross-source claims or evidence chains | https://aclanthology.org/2022.acl-long.511/ |\n| PAWS / PAWS-X (Zhang et al., NAACL/EMNLP 2019) | Adversarial paraphrase identification with high lexical-overlap non-paraphrases; PAWS-X adds cross-lingual coverage | **High adversarial control** for false matches and multilingual paraphrase | Sentence paraphrase, not factual/source-grounded claim equivalence | https://aclanthology.org/N19-1131/ |\n| STS Benchmark (SemEval 2017 Task 1) | Graded semantic similarity for sentence pairs | Useful weak baseline and retrieval prefilter | Similarity is not entailment; cannot decide contradiction or changed quantification | https://aclanthology.org/S17-2001/ |\n| MultiNLI (Williams et al., ACL 2018) | Broad-genre entailment, contradiction, and neutral classification | Robust general NLI calibration and genre transfer | Premise/hypothesis relation is not the same as same-source claim matching | https://aclanthology.org/N18-1101/ |\n\n## Recommended evaluation stack\n\n1. **Candidate generation:** STS-B or a dense retriever, measured by Recall@k against claim clusters.\n2. **Equivalence decision:** Claim Matching Beyond English and MultiClaim, scored with pair F1/AUROC and cluster purity; include hard negatives with changed polarity, entity, time, quantity, and modality.\n3. **Scholarly grounding:** SciFact and SciNLI, scored for evidence retrieval, rationale span F1, and entailment/contradiction/neutral accuracy.\n4. **Adversarial robustness:** VitaminC and PAWS/PAWS-X for minimal edits and lexical-overlap traps.\n5. **Web provenance:** AVeriTeC and FEVER for source selection, citation support, and auditable evidence chains.\n\n## Scope and limitations\n\nThe two CSVs rank the existing 80 benchmark studies from `benchmark_studies.csv`; they do not silently add external resources to the immutable inventory. External resources above were separately searched and recorded because the retained inventory lacks a direct claim-matching benchmark. Scores are suitability scores for this narrow viewpoint, not overall benchmark quality.\n\n## Sources consulted\n\n- ACL Anthology records for SciFact, Claim Matching Beyond English, VitaminC, SciNLI, PAWS, and MultiNLI.\n- NeurIPS proceedings record for AVeriTeC.\n- arXiv record for MultiClaim.\n- SemEval 2017 Task 1 record for STS Benchmark.\n''')
print('wrote', len(rows), 'rows')
