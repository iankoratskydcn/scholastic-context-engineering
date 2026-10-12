import csv, json
from pathlib import Path

root = Path('/Users/iankoratsky/Documents/GitHub/scholastic-context-engineering/.hermes/lit_review/ranking')
infile = root / 'benchmark_studies.csv'
slug = 'novelty_claim_validation'

rows = list(csv.DictReader(infile.open(encoding='utf-8-sig', newline='')))

# Score = ability to falsify claimed integrated benefits, expose regressions,
# separate architecture effects from prompt/model effects, and validate claims.
profiles = {
    'PCBench': (100, 'high', 'Direct premise-critique cases with typed errors and difficulty levels can falsify claim validation, premise filtering, and unsupported-claim rejection; controlled perturbations help separate architecture gains from prompt effects.'),
    'FalseQA': (98, 'high', 'Human-written false-premise questions plus corrected premises directly test whether the system challenges bad inputs instead of producing fluent answers; paired items support clean regression and prompt controls.'),
    'ProofWriter': (97, 'high', 'Explicit facts, rules, proof chains, and True/False/Unknown labels expose extraction, dependency preservation, proof recovery, and invalid-inference regressions; synthetic controls isolate reasoning from world knowledge.'),
    'FOLIO': (96, 'high', 'Human-authored premise sets with FOL annotations and verification test natural-language-to-formal reasoning under realistic wording; supports claim validation beyond prompt-sensitive answer matching.'),
    'LogicNLI': (95, 'high', 'Logic-grounded entailment, contradiction, and unknown labels diagnose robustness and generalization; factorized cases can reveal whether gains come from context engineering or language-model priors.'),
    'RAGTruth': (94, 'high', 'Case- and word-level hallucination labels expose unsupported spans in retrieved generation, directly testing provenance and claim validation rather than only final-answer accuracy.'),
    'ALCE': (93, 'high', 'End-to-end retrieval plus cited generation tests evidence selection, citation correctness, and answer support; useful architecture-level falsification when evaluated with citation and answer metrics separately.'),
    'MultiHop-RAG': (92, 'high', 'Multi-hop questions with supporting evidence stress dependency-preserving selection and composition; exact evidence-chain scoring can expose regressions hidden by aggregate answer accuracy.'),
    'LongPiBench': (91, 'high', 'Separated relevant information pieces directly stress positional bias and dependency-aware context selection; strong threat to claims that compression preserves multi-piece reasoning.'),
    'RULER': (90, 'high', 'Multiple needles, multi-hop tracing, and aggregation across tasks expose retrieval and context-position regressions; controlled length and position sweeps distinguish architecture effects from model context limits.'),
    'NoLiMa': (89, 'high', 'Long-context semantic association with reduced literal overlap threatens superficial retrieval and prompt-matching explanations; useful for testing genuine selection and reasoning under context rot.'),
    '∞Bench': (83, 'medium', 'Beyond-100K evaluation can reveal long-context scalability failures and regressions, but broad task heterogeneity makes causal attribution to the integrated architecture weaker.'),
    'LongBench': (80, 'medium', 'Bilingual multitask long-context coverage checks broad regression and robustness, but mixed tasks and end scores provide less isolation of provenance, proof, or claim-validation mechanisms.'),
    'Long Range Arena (LRA)': (76, 'medium', 'Controlled long-range sequence tasks stress context handling and position sensitivity, yet mostly test generic sequence processing rather than scholarly claims or inspectable reasoning.'),
    'FAITHCOT-BENCH / FINE-COT': (92, 'high', 'Annotated reasoning trajectories with instance-level unfaithfulness labels directly test whether inspectable reasoning reflects actual decision support; strong threat to claims based on plausible chains or prompt-only CoT.'),
    'Counterfactual reasoning task suite': (88, 'high', 'Counterfactual variants across reasoning domains expose recitation, shortcut, and prompt-following behavior; paired interventions help determine whether improvements are genuine reasoning changes.'),
    'LeanDojo dataset/benchmark': (87, 'high', 'Theorem/proof instances with premise annotations provide executable proof validity and premise-selection checks; excellent component and regression test, though formal Lean differs from scholarly prose.'),
    'LeanDojo': (87, 'high', 'Theorem/proof instances with premise annotations provide executable proof validity and premise-selection checks; excellent component and regression test, though formal Lean differs from scholarly prose.'),
    'LeanDojo/ReProver': (88, 'high', 'Retrieval-augmented theorem proving combines premise selection with proof completion and executable verification; directly threatens claims about integrated retrieval, compression, and reasoning.'),
    'Isabelle proof-state/relevant-premise pairs': (84, 'medium', 'Proof-state and relevant-premise pairs isolate premise selection and formal validity, exposing retrieval regressions while offering less evidence about natural-language extraction or cross-tradition reasoning.'),
    'MALLS': (78, 'medium', 'NL-to-FOL pairs test formalization and logical normalization, useful for component validation; limited depth and synthetic framing weaken claims about full integrated scholarly reasoning.'),
    'QT-SCHEMES': (89, 'high', 'Real dialogue arguments annotated with 24 schemes directly test argument-form extraction and classification, making scheme-level regressions and prompt-induced label shifts visible.'),
    'US2016G1tvWALTON corpus': (86, 'high', 'Annotated Walton schemes test argument-form classification with interpretable labels; useful falsification of cross-tradition/form claims, though corpus scope and scheme ambiguity constrain broad claims.'),
    'NLAS-multi': (72, 'medium', 'Multilingual generated arguments test cross-lingual scheme recognition, but generation artifacts and templating make it vulnerable to prompt and lexical shortcuts.'),
    'EthiX': (82, 'high', 'Manually curated Kialo arguments across topics and Walton classes provide authentic structured argument cases; can expose scheme and stance regressions, with limited scholarly-depth coverage.'),
    'Annotated/generated Walton-scheme sets': (75, 'medium', 'Enthymeme-oriented annotated and generated sets challenge implicit-premise handling, but mixed provenance and generated material reduce confidence in architecture-level conclusions.'),
    'LOGIC; LOGIC_CLIMATE': (81, 'high', 'Fallacy labels plus a climate challenge set test invalid inference and domain shift; useful falsification of claim validation, though classification can miss full evidence dependency.'),
    'ElecDeb60To16 extension': (84, 'high', 'Argument spans, claims, premises, support/attack links, and fallacy categories expose structured extraction and relation regressions on political debate text.'),
    'LOGICOM': (79, 'high', 'Paired logical/fallacious arguments in multi-round persuasion expose susceptibility to invalid framing and robustness regressions; still partly tests social persuasion rather than scholarly proof.'),
    'MISSCI': (87, 'high', 'Misinformation claims paired with cited biomedical publications and implicit-fallacy reconstruction directly test source grounding, claim validation, and hidden-premise recovery.'),
    'MISSCI PLUS': (91, 'high', 'Real study passages with retrieval, verbalization, and fact-checking provide an unusually direct integrated test of evidence selection, grounded claims, and fallacy reconstruction.'),
    'SMARTYPAT-BENCH': (88, 'high', 'Fine-grained fallacy labels with Prolog-controlled test oracles distinguish valid reasoning from fluent pattern matching and support strong regression detection.'),
    'RuleTaker': (85, 'high', 'Depth-controlled rule theories isolate entailment and contradiction failures with reproducible labels; strong causal diagnostic, but synthetic language limits transfer to scholarly claims.'),
    'PrOntoQA': (86, 'high', 'Generated worlds and symbolic proof chains provide depth and counterfactual controls for testing reasoning faithfulness; powerful falsification of shortcut claims but weak authenticity.'),
    'BIG-bench logical deduction/syllogism tasks': (68, 'medium', 'Logical and syllogism tasks broaden regression coverage, but task heterogeneity and weak shared diagnostics make integrated architectural attribution difficult.'),
    'SylloBase': (80, 'high', 'Categorical syllogisms with paraphrase and manually rewritten tests expose validity and lexical-belief shortcuts; useful component threat, less coverage of provenance or context selection.'),
    'NeuBAROCO': (73, 'medium', 'Bilingual syllogism items and indeterminate cases test cross-lingual validity and belief bias, but primarily measure narrow deductive classification.'),
    'abductive syllogism dataset': (78, 'medium', 'Labeled deductive and abductive syllogisms with contradictions and belief categories test inference-mode discrimination; useful diagnostic, but limited integrated pipeline coverage.'),
    'InterIDEAS': (67, 'medium', 'Authentic philosophical texts, bibliometric relations, RAG, and human evaluation offer relevance to intertextual grounding, but task outcomes are broad and attribution to reasoning architecture is difficult.'),
    'frame/symbol-grounding zero-shot benchmark': (63, 'medium', 'Philosophical grounding tasks can challenge semantic understanding and prompt sensitivity, but zero-shot design and broad constructs make claim falsification indirect.'),
    'AwareBench/AwareEval': (58, 'medium', 'Awareness and self-model questions probe model behavior under prompting, yet weakly test evidence preservation, proof structure, or scholarly claim validation.'),
    'AMAeval': (75, 'medium', 'Formal moral-assistant tasks with deductive and abductive chains test inspectable multi-step judgment; useful adjacent threat, though normative framing and model-judged assessment can confound attribution.'),
    'LogiQA': (69, 'medium', 'Natural-language logical reasoning items provide broad robustness regression coverage, but answer-level scoring hides extraction, evidence, and context-selection failure modes.'),
    'LogiQA 2.0': (69, 'medium', 'Improved logical reasoning data broadens robustness checks, but benchmark-level answers remain a coarse proxy for integrated claim validation.'),
    'Mickey': (61, 'medium', 'Multilingual commonsense reasoning probes language and cultural transfer, useful for prompt/model confounds, but not direct evidence for provenance or proof recovery.'),
    'GeoMLAMA': (60, 'medium', 'Geo-diverse commonsense probes expose cultural and language shortcuts; mainly an adjacent bias diagnostic rather than a direct integrated-architecture test.'),
    'CDEval': (57, 'medium', 'Cultural-dimension evaluation can reveal model priors and prompt sensitivity, but does not directly validate structured claims, evidence spans, or proof skeletons.'),
    'WorldValuesBench': (55, 'medium', 'Multicultural value awareness tests cultural regression and model priors, yet task construct is distant from context engineering and formal claim validation.'),
    'SeaEval': (59, 'medium', 'Cross-lingual and cultural reasoning coverage can expose language-specific regressions, but broad suite scores weakly isolate the proposed pipeline.'),
    'LLM-GLOBE': (54, 'medium', 'Cultural-value outputs reveal latent model bias and prompt effects, useful as a confound check but not a direct test of integrated evidence reasoning.'),
    'Global MMLU': (58, 'medium', 'Global subject coverage enables model/prompt robustness comparisons and cultural bias checks, but aggregate QA accuracy is a weak proxy for provenance-aware reasoning.'),
    'CQ-Bench': (56, 'medium', 'Implicit cultural-value questions test contextual interpretation and model priors, but offer little direct diagnosticity for claim extraction or proof validity.'),
    'Arab-culture commonsense dataset': (55, 'medium', 'Arab-culture commonsense cases can expose language/culture regressions, yet narrow QA outcomes do not validate the integrated scholastic reasoning pipeline.'),
    'DRISHTIKON': (53, 'medium', 'Multimodal Indian-culture understanding checks modality and cultural robustness, but is distant from text-only evidence, provenance, and formal reasoning claims.'),
    'SANSKRITI': (52, 'medium', 'Indian-culture knowledge coverage can reveal model prior and prompt effects, but provides little direct threat to context selection or claim validation.'),
    'Deep argumentative structures corpus': (82, 'high', 'Complex argumentative structures provide relation-level diagnostics for support, attack, and dependency recovery; strong component threat, though annotation scope may limit scholarly transfer.'),
    'implicit-reasoning causal-link materials': (85, 'high', 'Causal links for implicit reasoning directly stress hidden-premise and dependency reconstruction, useful for falsifying claims that compression preserves inferential structure.'),
    'InAbHyD': (83, 'high', 'Inductive and abductive reasoning cases test hypothesis selection and Occam-style shortcuts; controlled alternatives can separate genuine inference from prompt/model heuristics.'),
    'E-KAR': (76, 'medium', 'Rationalization of natural-language analogies tests relational explanation and evidence for analogical mapping, but only partially covers claims, provenance, and dialectical structure.'),
    'ANALOGICAL': (75, 'medium', 'Long-text analogy evaluation stresses cross-document relation finding and context selection; useful integrated threat, but answer/rationale scoring may be difficult to attribute.'),
    'StoryAnalogy': (68, 'medium', 'Story-level analogies probe long-range relational understanding and distractor handling, but generated narrative structure weakens direct claim-validation conclusions.'),
    'AnaloBench': (79, 'high', 'Abstract and long-context analogy identification stresses semantic retrieval beyond lexical overlap, exposing context-selection and genuine-reasoning claims.'),
    'KnowledgePrompts 15K proportional-analogy dataset': (63, 'medium', 'Knowledge-enhanced proportional analogies probe prompt and knowledge effects, but dataset framing and narrow task reduce evidence for full architecture benefits.'),
    'complex-analogy benchmark': (74, 'medium', 'Complex relational analogies test multi-step mapping and shortcut resistance, useful adjacent validation but not direct provenance or formal claim checking.'),
    'CREMMA Medii Aevi': (42, 'medium', 'Medieval Latin HTR authenticity supports upstream text-ingestion regression checks, but recognition accuracy only indirectly threatens downstream reasoning claims.'),
    'Index Thomisticus Treebank': (64, 'high', 'Aquinas dependency annotations directly support scholarly syntax and dependency-preservation checks, making upstream extraction regressions visible even though it is not an end-to-end reasoning test.'),
    'eFontes Medieval Latin corpus': (49, 'medium', 'Medieval Latin POS, lemmatization, and morphology coverage tests scholarly preprocessing robustness, but has limited direct claim-validation or reasoning diagnosticity.'),
    'tree-structured debate corpus': (73, 'medium', 'Tree-structured debate metadata tests argument organization and generation consistency, useful for dialectical skeleton regressions but vulnerable to generation-quality confounds.'),
    'Tree-of-Debate scientific comparison set': (77, 'medium', 'Scientific comparative-analysis debates with expert comparison stress multi-perspective synthesis and dialectical reasoning; useful integrated validation, though evaluation may be subjective.'),
    '741-topic argument-tree corpus': (81, 'high', 'Manually curated complex argument trees provide interpretable stance and specificity structure for testing dependency-preserving compression and dialectical reconstruction.'),
    'OpenITI-derived Classical Arabic corpus': (60, 'medium', 'Classical Arabic expert resources test multilingual scholarly ingestion and entity relations, useful cross-tradition robustness but not direct end-to-end claim validation.'),
    'Quranic Arabic PropBank': (63, 'medium', 'Predicate-argument annotations expose semantic-role extraction and dependency errors in a non-Western scholarly tradition; strong upstream/cross-tradition diagnostic, limited downstream proof coverage.'),
    'Quran–Hadith Classical Arabic dataset': (57, 'medium', 'Expert cross-domain semantic-relatedness cases test culturally specific retrieval and representation, but answer-level similarity is a weak proxy for claim validation.'),
    'HAQA and QUQA': (61, 'medium', 'Quran/Hadith QA tests source-specific retrieval and answer grounding in authentic texts, useful cross-tradition regression coverage but limited proof and argument-form diagnostics.'),
    'MARS': (86, 'high', 'Multi-task metaphysical reasoning directly targets philosophical reasoning and can expose gains that vanish under task, prompt, or model changes; strong claim-validation value despite likely subjective components.'),
    'argument-scheme evaluation set (annotated/generated enthymemes)': (83, 'medium', 'Annotated and generated enthymemes test scheme recognition and implicit-premise recovery, directly challenging claims about inspectable argument structure while requiring careful provenance controls.'),
}

def key_candidates(r):
    return [r.get('benchmark_name','').strip(), r.get('benchmark_type','').strip()]

def profile(r):
    name = r.get('benchmark_name','').strip()
    if name in profiles: return profiles[name]
    # Fallback by category for unnamed or blank resources.
    cat = r.get('category','').lower()
    if 'cross-cultural' in cat: return (55, 'medium', 'Cross-cultural reasoning coverage can expose language, culture, and prompt confounds, but broad QA outcomes weakly test provenance-aware integrated reasoning.')
    if 'scholastic digital' in cat: return (52, 'medium', 'Scholarly-language resources can expose upstream ingestion and dependency regressions, but do not by themselves validate downstream claim reasoning.')
    if 'abductive' in cat or 'analogical' in cat: return (70, 'medium', 'Abductive or analogical cases test non-deductive inference and shortcut resistance, but provide partial coverage of provenance and integrated pipeline behavior.')
    if 'dialectical' in cat: return (70, 'medium', 'Dialectical material tests argument organization and multi-perspective reasoning, but broad or subjective evaluation can weaken causal attribution.')
    return (50, 'low', 'Adjacent benchmark provides limited regression evidence; task outcome does not directly isolate integrated context engineering, claim validation, or prompt/model effects.')

for r in rows:
    score, conf, expl = profile(r)
    r['_score'] = score
    r['_confidence'] = conf
    r['_explanation'] = expl
    r['_evidence_basis'] = f"{r['evidence']} Novelty/claim-validation basis: {expl}"

# deterministic tie order required by protocol
order_key = lambda r: (int(r['category_num']), int(r['paper_order']), r['paper_id'])
rows_sorted = sorted(rows, key=lambda r: (-r['_score'],) + order_key(r))
for i, r in enumerate(rows_sorted, 1): r['_global_rank'] = i

cat_groups = {}
for r in rows_sorted: cat_groups.setdefault(r['category_num'], []).append(r)
for group in cat_groups.values():
    group.sort(key=lambda r: (-r['_score'], int(r['paper_order']), r['paper_id']))
    for i, r in enumerate(group, 1): r['_category_rank'] = i

fields = ['paper_id','category_num','category','paper_order','citation','benchmark_status','benchmark_name','benchmark_type','reviewer_slug','viewpoint','category_rank','global_rank','score_0_100','confidence','explanation','evidence_basis']
viewpoint = 'novelty threat and claim validation'
for r in rows_sorted:
    r['reviewer_slug'] = slug
    r['viewpoint'] = viewpoint

for suffix, data in [('global', rows_sorted), ('category', sorted(rows_sorted, key=lambda r: (int(r['category_num']), r['_category_rank'])) )]:
    out = root / f'benchmark_review_{slug}_{suffix}.csv'
    with out.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in data:
            w.writerow({
                'paper_id': r['paper_id'], 'category_num': r['category_num'], 'category': r['category'],
                'paper_order': r['paper_order'], 'citation': r['citation'], 'benchmark_status': r['benchmark_status'],
                'benchmark_name': r['benchmark_name'], 'benchmark_type': r['benchmark_type'], 'reviewer_slug': slug,
                'viewpoint': viewpoint, 'category_rank': r['_category_rank'], 'global_rank': r['_global_rank'],
                'score_0_100': r['_score'], 'confidence': r['_confidence'], 'explanation': r['_explanation'],
                'evidence_basis': r['_evidence_basis']
            })

summary = {
    'reviewer_slug': slug,
    'viewpoint': viewpoint,
    'input': 'benchmark_studies.csv',
    'rows': len(rows_sorted),
    'global_rank_rule': 'score descending; ties by numeric category_num, numeric paper_order, literal paper_id',
    'category_rank_rule': 'contiguous within category; score descending; ties by paper_order then paper_id',
    'top_15': [
        {'global_rank': r['_global_rank'], 'paper_id': r['paper_id'], 'benchmark_name': r['benchmark_name'], 'score_0_100': r['_score']}
        for r in rows_sorted[:15]
    ],
    'score_bands': {
        '90_100': sum(r['_score'] >= 90 for r in rows_sorted),
        '80_89': sum(80 <= r['_score'] < 90 for r in rows_sorted),
        '70_79': sum(70 <= r['_score'] < 80 for r in rows_sorted),
        'below_70': sum(r['_score'] < 70 for r in rows_sorted),
    },
    'notes': [
        'High scores favor benchmarks that can falsify integrated architecture claims, expose evidence/proof/context regressions, and separate genuine reasoning from prompt or model effects.',
        'Synthetic formal benchmarks remain high when executable labels/oracles provide strong causal diagnosis; authenticity and cross-tradition fit are treated separately.',
        'Upstream scholarly NLP resources score lower unless they directly expose dependency/provenance failures relevant to downstream claim validation.',
        'Duplicate benchmark records are retained as separate immutable studies per protocol.'
    ]
}
(root / f'results_{slug}.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

notes = f'''# Novelty-threat and claim-validation review

- Input: `benchmark_studies.csv`; rows ranked: {len(rows_sorted)}.
- High score means benchmark can threaten claimed integrated benefits, expose regressions, test architecture versus components, or distinguish genuine reasoning from prompt/LLM effects.
- Strongest direct threats: PCBench, FalseQA, ProofWriter, FOLIO, LogicNLI, RAGTruth, ALCE, MultiHop-RAG, LongPiBench, RULER, NoLiMa, FAITHCOT-BENCH, MISSCI PLUS, LeanDojo/ReProver, QT-SCHEMES, and MARS.
- Synthetic logic/proof benchmarks score high when oracle-backed and factorized; they isolate causal failure modes even when they lack scholarly authenticity.
- Authentic scholarly and argument resources score high when they expose spans, dependencies, schemes, support/attack, implicit premises, citations, or multi-piece evidence; generic cultural/QA suites score lower because end scores do not isolate the pipeline.
- Duplicate/version records retained exactly and ranked separately.
- Evidence basis preserves each input evidence statement, followed by explicit novelty/claim-validation rationale.
'''
(root / f'benchmark_review_{slug}_notes.md').write_text(notes, encoding='utf-8')
print(json.dumps({'rows': len(rows_sorted), 'global': str(root/f'benchmark_review_{slug}_global.csv'), 'category': str(root/f'benchmark_review_{slug}_category.csv'), 'json': str(root/f'results_{slug}.json')}))
