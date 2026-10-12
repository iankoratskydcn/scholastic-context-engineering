# Philosophical reasoning evaluation benchmarks

- **Slug:** `philosophical_reasoning_eval`
- **Search date:** 2026-10-12 (US/Eastern)
- **Records:** 11 retained resources
- **Scope:** Scholarly benchmarks or evaluation datasets for philosophy-specific reasoning, philosophical QA/theory transfer, source-grounded philosophical text analysis, or inspectable argument evaluation.
- **Retention rule:** Retain resources only when the paper exposes intermediate reasoning structure, expert/rubric labels, source-grounding relations, formalization/proof labels, or staged theory-application judgments. Exclude generic philosophy knowledge QA whose labels are only answer correctness, and conceptual papers without an evaluation artifact.

## Retained resources

1. **Oka — frame/symbol-grounding zero-shot benchmark.** Converts two classical AI-philosophy problems into behavioral tasks: relevance filtering/plan revision and integration of a novel symbol/object into coherent meanings. Useful for adversarial philosophical-problem evaluation, but scores remain behavioral proxies rather than evidence of intrinsic grounding.
2. **AMAeval — Artificial Moral Assistant evaluation.** Explicitly evaluates deductive and abductive moral reasoning chains and chain assessment, not just agreement with a moral verdict. Strong direct baseline for inspectable normative reasoning.
3. **MARS — metaphysical reasoning benchmark.** Separates action changes, state changes, and situational transitions into three labeled tasks. Useful for staged reasoning diagnostics; it is a metaphysics-domain benchmark rather than a discourse-argument benchmark.
4. **PrinciplismQA.** Philosophy-grounded clinical-ethics benchmark with expert-validated knowledge and open-ended dilemma items. The open-ended track requires multi-principle trade-off navigation, making it relevant to source/rubric-grounded moral QA. Treat clinical deployment claims separately from philosophical reasoning claims.
5. **Rated conceptual arguments.** Expert-rated critiques of philosophical and adjacent conceptual position texts. Its central contribution is inspectable argument quality: centrality, strength, correctness, clarity, irrelevant/dead weight, single-issue focus, and overall quality. This is the best retained resource for evaluating critique quality where no settled philosophical answer exists.
6. **InterIDEAS.** Source-grounded philosophical intertextuality resource combining authentic texts, bibliographic relations, retrieval, LLM extraction, and human validation. Useful for evaluating retrieval and attribution of philosophical relations, but not a complete proof-validity benchmark.
7. **Rawls/Nozick theory-transfer evaluation.** A controlled novel scenario scored separately for recall, application, and reflection. Useful for testing whether models transfer philosophical theories instead of reproducing definitions; coverage is narrow and should be treated as a focused evaluation set.
8. **SylloBase.** Natural-language categorical syllogism benchmark with paraphrases and manually rewritten tests. It is a formal-reasoning control with explicit validity labels, not a broad philosophical QA benchmark.
9. **FOLIO.** Human-authored natural-language first-order reasoning with formal annotations and executable verification. Included as a formalization/deduction control; it should not be presented as philosophy-domain data.
10. **QT-SCHEMES.** 441 dialogue arguments with 24 argumentation-scheme annotations. Useful for premise/conclusion and inference-form recovery before philosophical answer generation.
11. **Walton-scheme LLM evaluation sets.** Manually annotated/generated enthymemes evaluated under multiple prompting regimes. Useful for measuring inspectable argument-form classification and testing whether form recognition predicts downstream philosophical critique quality.

## Exclusions and boundary decisions

- **MMLU philosophy and similar generic philosophy QA:** excluded because they primarily expose answer-choice correctness, with no inspectable derivation, source attribution, argument structure, or expert reasoning rubric.
- **Philosophia-QA / synthetic philosophy Q&A collections:** excluded because the accessible description identifies synthetic question-answer pairs but does not establish independently inspectable reasoning labels or validated source-grounding annotations.
- **AwareBench/AwareEval:** excluded from the retained CSV because it measures behavioral self-model/awareness dimensions; it is philosophy-adjacent but does not primarily expose philosophical reasoning or source-grounded argument labels.
- **Greatest Good Benchmark and other moral-preference-only suites:** excluded when they score final judgments without premise-level or trade-off reasoning annotations. AMAeval and PrinciplismQA were retained because they expose staged reasoning or open-ended trade-off evaluation.
- **Philosopher-style imitation studies:** excluded as benchmarks unless they provide inspectable argument or grounding labels. Style/authorship discrimination alone is not philosophical reasoning evaluation.
- **General argument-mining resources:** QT-SCHEMES and Walton-scheme sets were retained only as transfer controls because their explicit argument-form labels are directly useful for inspectable philosophical reasoning. They are not philosophy-domain QA by themselves.

## Recommended use

Use the retained resources as a **battery**, not one pooled score:

- **Philosophical problem and theory transfer:** Oka, MARS, Rawls/Nozick, PrinciplismQA.
- **Normative reasoning with inspectable intermediate structure:** AMAeval, PrinciplismQA, rated conceptual arguments.
- **Source-grounded philosophical text processing:** InterIDEAS.
- **Argument-form and proof controls:** QT-SCHEMES, Walton-scheme sets, SylloBase, FOLIO.

For a source-grounded philosophical answer generator, report separately: retrieval/attribution precision, premise and conclusion span recovery, inference/scheme accuracy, formal validity or chain correctness, expert critique quality, theory-transfer performance, and final-answer quality. Include raw-context, proof-relevant-selected-context, compressed-context, and distractor conditions where the benchmark supports them.

## Sources

- Oka: https://arxiv.org/html/2506.07896v1
- AMAeval: https://arxiv.org/html/2508.12754v1
- MARS: https://arxiv.org/html/2406.02106v2
- PrinciplismQA: https://aclanthology.org/2026.findings-acl.1806.pdf
- Rated conceptual arguments: https://arxiv.org/html/2607.27499v1
- InterIDEAS: https://aclanthology.org/2025.emnlp-main.1180/
- Rawls/Nozick theory transfer: https://journals.ub.uni-koeln.de/index.php/phidi/article/view/11663
- SylloBase: https://aclanthology.org/2023.findings-acl.148/
- FOLIO: https://arxiv.org/abs/2209.00840
- QT-SCHEMES: https://aclanthology.org/2025.acl-long.368/
- Walton-scheme LLM evaluation: https://aclanthology.org/2025.findings-acl.702/
