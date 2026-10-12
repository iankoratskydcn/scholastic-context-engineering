# All 80 Benchmark Studies — Ranked Review

- Universe: all 80 benchmark-producing studies in `benchmark_studies.csv`.
- Ranking: mean score across 25 benchmark perspectives in `benchmark_master_matrix.csv`.
- Important: repeated records may refer to the same benchmark family/version; family duplicates are retained here for provenance but should not be counted as independent tests.
- Artifact status is separate from scholarly ranking and is fail-closed.

## Final battery status
- **FOLIO** — deductive/formalization control — `verified_optional_fallback` — include_core_now
- **LongPiBench** — context stress — `verified` — include_core
- **PCBench** — premise critique / invalid inference — `verified` — include_core
- **MISSCI PLUS** — grounding / fallacy provenance — `verified_with_reproducibility_caveat` — include_core_with_caveat
- **LeanDojo/ReProver** — formal proof compatibility / premise selection — `verified_heavy_control` — include_core_secondary
- **Index Thomisticus Treebank / UD_Latin-ITTB** — authentic scholastic text — `verified` — include_core_transfer_gate
- **QT-SCHEMES** — argument-form / scheme extraction — `blocked_pending_license` — pending_not_core
- **741-topic argument-tree corpus** — dialectical argument trees — `blocked_identity_mismatch` — pending_not_core
- **ALCE** — citation-level provenance — `blocked_dataset_license` — pending_not_core

## Ranked benchmarks

### 1. `12-06` — FOLIO
**Citation:** Han et al. (2022/2024), FOLIO: Natural Language Reasoning with First-Order Logic
**Type:** human-authored FOL reasoning benchmark
**Aggregate mean score:** 86.6400
**Exact-task assessment:** FOLIO is a direct project test: retained evidence shows premise relations, proof/deduction structure, or proof-relevant selection. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** authentic formal reasoning. Score reflects distinct failure-mode coverage and pairability.
**Artifact/battery status:** `verified_optional_fallback`; `include_core_now`
**Evidence basis:** Introduces 1,430 conclusions over 487 premise sets with natural-language problems, FOL annotations, and automated verification.; retained category summary/paper evidence

### 2. `S07P01` — ProofWriter
**Citation:** Tafjord, Dalvi Mishra & Clark (2021), “ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language.”
**Type:** introduces_benchmark
**Aggregate mean score:** 85.0400
**Exact-task assessment:** ProofWriter is a direct project test: retained evidence shows premise relations, proof/deduction structure, or proof-relevant selection. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** controlled proof depth, abduction, open/closed-world reasoning. Score reflects distinct failure-mode coverage and pairability.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Introduces the ProofWriter rule-theory/proof dataset and evaluation setting.; retained category summary/paper evidence

### 3. `12-04` — ProofWriter
**Citation:** Tafjord, Dalvi, and Clark (2021), ProofWriter
**Type:** proof/abduction benchmark
**Aggregate mean score:** 84.9600
**Exact-task assessment:** ProofWriter is a direct project test: retained evidence shows premise relations, proof/deduction structure, or proof-relevant selection. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** same ProofWriter family; redundant record. Score reflects distinct failure-mode coverage and pairability.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Introduces True/False/Unknown datasets with closed/open-world variants, enumerated proofs, implications, abduction, and depth settings.; retained category summary/paper evidence

### 4. `14-08` — LeanDojo/ReProver
**Citation:** Yang et al. (2023), LeanDojo: Theorem Proving with Retrieval-Augmented Language Models
**Type:** retrieval-augmented theorem-proving benchmark/dataset
**Aggregate mean score:** 83.2800
**Exact-task assessment:** LeanDojo/ReProver is a direct project test: retained evidence shows premise relations, proof/deduction structure, or proof-relevant selection. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** proof-relevant premise retrieval and exact proving. Score reflects distinct failure-mode coverage and pairability.
**Artifact/battery status:** `verified_heavy_control`; `include_core_secondary`
**Evidence basis:** Introduces LeanDojo data extraction and fine-grained premise annotations alongside the ReProver retrieval-augmented proving benchmark.; retained category summary/paper evidence

### 5. `S09P08` — QT-SCHEMES
**Citation:** Ruiz-Dolz, Kikteva & Lawrence (2025), “Mining Complex Patterns of Argumentative Reasoning in Natural Language Dialogue.”
**Type:** introduces_dataset_or_corpus_used_as_benchmark
**Aggregate mean score:** 81.3200
**Exact-task assessment:** QT-SCHEMES is a direct project test: retained evidence shows the stated benchmark resource. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** front-end scheme extraction; high-information anchor. Score reflects distinct failure-mode coverage and pairability.
**Artifact/battery status:** `blocked_pending_license`; `pending_not_core`
**Evidence basis:** Introduces 441 arguments annotated with 24 schemes for classification evaluation.; retained category summary/paper evidence

### 6. `S25P13` — QT-SCHEMES
**Citation:** Ruiz-Dolz, Kikteva & Lawrence (2025), “Mining Complex Patterns of Argumentative Reasoning in Natural Language Dialogue”
**Type:** argument-scheme mining corpus/benchmark
**Aggregate mean score:** 80.8800
**Exact-task assessment:** QT-SCHEMES is a direct project test: retained evidence shows argument structure, scheme, support/attack, or dialectical form. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** Shared benchmark family/version record; retain for identity completeness but do not count as new battery coverage.
**Artifact/battery status:** `blocked_pending_license`; `pending_not_core`
**Evidence basis:** Introduces QT-SCHEMES: 441 dialogue arguments annotated with 24 schemes, and evaluates Transformer/LLM scheme mining. Source artifact: summaries/25_ai_philosophy_dialectical_methods_summaries.md; retained category summary/paper evidence

### 7. `11-08` — MISSCI PLUS
**Citation:** Glockner et al. (2025), Grounding Fallacies Misrepresenting Scientific Publications in Evidence
**Type:** passage-grounded fallacy benchmark
**Aggregate mean score:** 79.2000
**Exact-task assessment:** MISSCI PLUS is a direct project test: retained evidence shows argument structure, scheme, support/attack, or dialectical form. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** scholarly passage grounding, fallacy reconstruction, fact checking. Score reflects distinct failure-mode coverage and pairability.
**Artifact/battery status:** `verified_with_reproducibility_caveat`; `include_core_with_caveat`
**Evidence basis:** Introduces MISSCI PLUS with real study passages, passage retrieval, verbalization, and fact-checking evaluation.; retained category summary/paper evidence

### 8. `S08P05` — Isabelle proof-state/relevant-premise pairs
**Citation:** Mikuła et al. (2024), “Magnushammer.”
**Type:** introduces_dataset_or_corpus_used_as_benchmark
**Aggregate mean score:** 78.7200
**Exact-task assessment:** Isabelle proof-state/relevant-premise pairs is a direct project test: retained evidence shows premise relations, proof/deduction structure, or proof-relevant selection. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** cross-prover premise-selection control. Score reflects distinct failure-mode coverage and pairability.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Releases reusable proof-state/relevant-premise pairs for premise-selection evaluation.; retained category summary/paper evidence

### 9. `12-05` — LogicNLI
**Citation:** Tian et al. (2021), Diagnosing the First-Order Logical Reasoning Ability Through LogicNLI
**Type:** FOL natural-language inference benchmark
**Aggregate mean score:** 78.1200
**Exact-task assessment:** LogicNLI is a direct project test: retained evidence shows premise relations, proof/deduction structure, or proof-relevant selection. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** controlled FOL robustness/generalization. Score reflects distinct failure-mode coverage and pairability.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Introduces LogicNLI to diagnose logical reasoning, robustness, generalization, and interpretability apart from commonsense inference.; retained category summary/paper evidence

### 10. `S23P12` — 741-topic argument-tree corpus
**Citation:** Peldszus & Stede (2019), “Determining Relative Argument Specificity and Stance for Complex Argumentative Structures”
**Type:** stance and argument-specificity classification
**Aggregate mean score:** 77.2800
**Exact-task assessment:** 741-topic argument-tree corpus is a direct project test: retained evidence shows argument structure, scheme, support/attack, or dialectical form. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** argument-tree component, stance, specificity, dependency extraction. Score reflects distinct failure-mode coverage and pairability.
**Artifact/battery status:** `blocked_identity_mismatch`; `pending_not_core`
**Evidence basis:** Uses a large manually curated corpus of complex argument trees for model evaluation; treated as a dataset benchmark contribution. Source artifact: summaries/23_disputatio_dialectical_ai_summaries.md; retained category summary/paper evidence

### 11. `S08P04` — LeanDojo dataset/benchmark
**Citation:** Yang et al. (2023), “LeanDojo.”
**Type:** introduces_benchmark
**Aggregate mean score:** 77.0800
**Exact-task assessment:** LeanDojo dataset/benchmark is a direct project test: retained evidence shows premise relations, proof/deduction structure, or proof-relevant selection. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** same LeanDojo family; redundant record. Score reflects distinct failure-mode coverage and pairability.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Introduces proof dataset/toolkit, premise annotations, and theorem collection.; retained category summary/paper evidence

### 12. `S07P08` — LeanDojo dataset/benchmark
**Citation:** Yang et al. (2023), “LeanDojo.”
**Type:** introduces_benchmark
**Aggregate mean score:** 77.0000
**Exact-task assessment:** LeanDojo dataset/benchmark is a direct project test: retained evidence shows premise relations, proof/deduction structure, or proof-relevant selection. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** same LeanDojo family; redundant record. Score reflects distinct failure-mode coverage and pairability.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Introduces open Lean interaction data, premise annotations, and 98,734 theorem/proof instances.; retained category summary/paper evidence

### 13. `11-04` — ElecDeb60To16 extension
**Citation:** Goffredo et al. (2023), Argument-based Detection and Classification of Fallacies in Political Debates
**Type:** annotated political-debate corpus
**Aggregate mean score:** 77.0000
**Exact-task assessment:** ElecDeb60To16 extension is a direct project test: retained evidence shows argument structure, scheme, support/attack, or dialectical form. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** Fallacy/grounding adjunct; retain when failure diagnosis needs this narrower slice.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Extends ElecDeb60To16 with fallacy spans, claims, premises, support/attack relations, and six categories.; retained category summary/paper evidence

### 14. `S10P07` — US2016G1tvWALTON corpus
**Citation:** Visser et al. (2021), “Annotating Argument Schemes.”
**Type:** introduces_dataset_or_corpus_used_as_benchmark
**Aggregate mean score:** 76.3200
**Exact-task assessment:** US2016G1tvWALTON corpus is a direct project test: retained evidence shows the stated benchmark resource. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** front-end Walton scheme and premise/conclusion extraction. Score reflects distinct failure-mode coverage and pairability.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Establishes an annotated Walton-scheme corpus for scheme-classification evaluation.; retained category summary/paper evidence

### 15. `18_11` — implicit-reasoning causal-link materials
**Citation:** Singh, Inoue, Mim, Naitoh & Inui (2021), “Annotating Implicit Reasoning in Arguments with Causal Links,” arXiv:2110.13692.
**Type:** benchmark/dataset/corpus or evaluation resource
**Aggregate mean score:** 75.8000
**Exact-task assessment:** implicit-reasoning causal-link materials is a direct project test: retained evidence shows argument structure, scheme, support/attack, or dialectical form. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** implicit-premise and causal-link extraction. Score reflects distinct failure-mode coverage and pairability.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** introduces a dataset or corpus used as an evaluation resource; retained category summary/paper evidence

### 16. `18_10` — Deep argumentative structures corpus
**Citation:** Reisert, Inoue, Okazaki & Inui (2017), “A Corpus of Deep Argumentative Structures as an Explanation to Argumentative Relations,” arXiv:1712.02480.
**Type:** benchmark/dataset/corpus or evaluation resource
**Aggregate mean score:** 75.3200
**Exact-task assessment:** Deep argumentative structures corpus is a direct project test: retained evidence shows argument structure, scheme, support/attack, or dialectical form. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** deep argumentative relation extraction. Score reflects distinct failure-mode coverage and pairability.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** introduces a dataset or corpus used as an evaluation resource; retained category summary/paper evidence

### 17. `11-06` — MISSCI
**Citation:** Glockner et al. (2024), MISSCI: Reconstructing Fallacies in Misrepresented Science
**Type:** misinformation/fallacy reconstruction dataset
**Aggregate mean score:** 74.9200
**Exact-task assessment:** MISSCI is a direct project test: retained evidence shows argument structure, scheme, support/attack, or dialectical form. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** Fallacy/grounding adjunct; retain when failure diagnosis needs this narrower slice.
**Artifact/battery status:** `verified_with_reproducibility_caveat`; `include_core_with_caveat`
**Evidence basis:** Introduces a dataset/task pairing misinformation claims with cited biomedical publications and implicit fallacy reconstruction.; retained category summary/paper evidence

### 18. `S25P14` — argument-scheme evaluation set (annotated/generated enthymemes)
**Citation:** Bezou-Vrakatseli, Cocarascu & Modgil (2025), “Can Large Language Models Understand Argument Schemes?”
**Type:** argument-scheme classification evaluation
**Aggregate mean score:** 74.6800
**Exact-task assessment:** argument-scheme evaluation set (annotated/generated enthymemes) is a direct project test: retained evidence shows argument structure, scheme, support/attack, or dialectical form. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** enthymeme and scheme transfer. Score reflects distinct failure-mode coverage and pairability.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Constructs/uses manually annotated and generated enthymeme evaluation material for zero-/few-shot/CoT comparison; not presented as a named broad benchmark. Source artifact: summaries/25_ai_philosophy_dialectical_methods_summaries.md; retained category summary/paper evidence

### 19. `S10P09` — EthiX
**Citation:** Bezou-Vrakatseli, Cocarascu & Modgil (2024), “EthiX.”
**Type:** introduces_benchmark
**Aggregate mean score:** 74.1600
**Exact-task assessment:** EthiX is a direct project test: retained evidence shows the stated benchmark resource. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** authentic scheme/topic transfer. Score reflects distinct failure-mode coverage and pairability.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Introduces 686 manually curated Kialo arguments across 22 topics and eight Walton classes.; retained category summary/paper evidence

### 20. `11-12` — SMARTYPAT-BENCH
**Citation:** Xu et al. (2026), Socrates or Smartypants: Testing Logic Reasoning Capabilities of Large Language Models with Logic Programming-Based Test Oracles
**Type:** fallacy benchmark with symbolic test oracle
**Aggregate mean score:** 71.9200
**Exact-task assessment:** SMARTYPAT-BENCH is a direct project test: retained evidence shows argument structure, scheme, support/attack, or dialectical form. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** symbolic-oracle fallacy control. Score reflects distinct failure-mode coverage and pairability.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Introduces SMARTYPAT-BENCH with 502 Reddit posts/fine-grained labels and SMARTYPAT controlled generation with Prolog oracles.; retained category summary/paper evidence

### 21. `12-03` — RuleTaker
**Citation:** Clark, Tafjord, and Richardson (2020), Transformers as Soft Reasoners over Language
**Type:** synthetic rule-deduction benchmark
**Aggregate mean score:** 71.4000
**Exact-task assessment:** RuleTaker is a direct project test: retained evidence shows premise relations, proof/deduction structure, or proof-relevant selection. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** Formal/deductive adjunct; controlled or narrow coverage makes it secondary to FOLIO, ProofWriter, and LeanDojo.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Introduces theorem-prover-generated natural-language theories, facts/rules, assertions, and depth-controlled labels.; retained category summary/paper evidence

### 22. `12-07` — PrOntoQA
**Citation:** Saparov and He (2022), Language Models Are Greedy Reasoners (PrOntoQA)
**Type:** synthetic proof-depth benchmark
**Aggregate mean score:** 69.6400
**Exact-task assessment:** PrOntoQA is a direct project test: retained evidence shows premise relations, proof/deduction structure, or proof-relevant selection. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** Formal/deductive adjunct; controlled or narrow coverage makes it secondary to FOLIO, ProofWriter, and LeanDojo.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Introduces generated first-order worlds whose chains and symbolic proofs test proof depth and chain-of-thought faithfulness.; retained category summary/paper evidence

### 23. `S05P09` — MultiHop-RAG
**Citation:** Tang and Yang (2024), “MultiHop-RAG: Benchmarking Retrieval-Augmented Generation for Multi-Hop Queries”
**Type:** multi-hop RAG benchmark/dataset
**Aggregate mean score:** 69.1200
**Exact-task assessment:** MultiHop-RAG is a direct project test: retained evidence shows evidence grounding, premise critique, citation, or provenance. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** multi-hop support retrieval. Score reflects distinct failure-mode coverage and pairability.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Artifact 05 § Verified papers § 9: explicitly says MultiHop-RAG introduces a dataset with knowledge base, multi-hop queries, answers, and supporting evidence.; retained category summary/paper evidence

### 24. `12-15` — abductive syllogism dataset
**Citation:** Abe et al. (2024–2026), Abductive Reasoning with Syllogistic Forms in Large Language Models
**Type:** abductive/deductive syllogism benchmark
**Aggregate mean score:** 68.8800
**Exact-task assessment:** abductive syllogism dataset is a direct project test: retained evidence shows premise relations, proof/deduction structure, or proof-relevant selection. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** Formal/deductive adjunct; controlled or narrow coverage makes it secondary to FOLIO, ProofWriter, and LeanDojo.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Converts a syllogistic dataset into abduction and releases labeled premises/hypotheses, deductive and abductive labels, form metadata, contradictions, and belief categories.; retained category summary/paper evidence

### 25. `12-11` — SylloBase
**Citation:** Li et al. (2023), Hence, Socrates is mortal (SylloBase)
**Type:** natural-language categorical syllogism benchmark
**Aggregate mean score:** 68.6000
**Exact-task assessment:** SylloBase is a direct project test: retained evidence shows premise relations, proof/deduction structure, or proof-relevant selection. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** Formal/deductive adjunct; controlled or narrow coverage makes it secondary to FOLIO, ProofWriter, and LeanDojo.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Introduces template-generated/paraphrased syllogisms plus 1,000 manually rewritten test samples.; retained category summary/paper evidence

### 26. `S02P07` — PCBench
**Citation:** Li et al. (2025), “Don’t Take the Premise for Granted: Evaluating the Premise Critique Ability of Large Language Models”
**Type:** premise-critique benchmark
**Aggregate mean score:** 68.0800
**Exact-task assessment:** PCBench is a useful adjacent diagnostic: retained evidence shows evidence grounding, premise critique, citation, or provenance, but not the complete scholastic source-to-structured-context pipeline. Best used alongside an authentic scholarly benchmark.
**Battery/complementarity assessment:** premise-error taxonomy and critique. Score reflects distinct failure-mode coverage and pairability.
**Artifact/battery status:** `verified`; `include_core`
**Evidence basis:** Artifact 02 § Verified papers § 7: explicitly identifies PCBench with four error types and three difficulty levels, used to evaluate 15 LLMs.; retained category summary/paper evidence

### 27. `11-01` — LOGIC; LOGIC_CLIMATE
**Citation:** Jin et al. (2022), Logical Fallacy Detection
**Type:** fallacy-detection dataset/challenge set
**Aggregate mean score:** 68.0400
**Exact-task assessment:** LOGIC; LOGIC_CLIMATE is a useful adjacent diagnostic: retained evidence shows argument structure, scheme, support/attack, or dialectical form, but not the complete scholastic source-to-structured-context pipeline. Best used alongside an authentic scholarly benchmark.
**Battery/complementarity assessment:** Fallacy/grounding adjunct; retain when failure diagnosis needs this narrower slice.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Explicitly introduces the LOGIC dataset and LOGIC_CLIMATE challenge set for logical fallacy detection.; retained category summary/paper evidence

### 28. `S05P05` — ALCE
**Citation:** Gao et al. (2023), “Enabling Large Language Models to Generate Text with Citations (ALCE)”
**Type:** citation-grounded generation benchmark
**Aggregate mean score:** 68.0000
**Exact-task assessment:** ALCE is a direct project test: retained evidence shows evidence grounding, premise critique, citation, or provenance. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** citation-backed downstream answer generation. Score reflects distinct failure-mode coverage and pairability.
**Artifact/battery status:** `blocked_dataset_license`; `pending_not_core`
**Evidence basis:** Artifact 05 § Verified papers § 5: explicitly calls ALCE an end-to-end benchmark for retrieving support and generating cited answers, with automatic citation/quality metrics.; retained category summary/paper evidence

### 29. `S10P12` — Annotated/generated Walton-scheme sets
**Citation:** Bezou-Vrakatseli, Cocarascu & Modgil (2025), “Can Large Language Models Understand Argument Schemes?”
**Type:** introduces_dataset_or_corpus_used_as_benchmark
**Aggregate mean score:** 66.8400
**Exact-task assessment:** Annotated/generated Walton-scheme sets is a useful adjacent diagnostic: retained evidence shows argument structure, scheme, support/attack, or dialectical form, but not the complete scholastic source-to-structured-context pipeline. Best used alongside an authentic scholarly benchmark.
**Battery/complementarity assessment:** Scheme-classification adjunct; useful for diversity, but overlaps front-end extraction anchors.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Assembles annotated/generated arguments including enthymemes for systematic LLM scheme evaluation; treated as a dataset resource.; retained category summary/paper evidence

### 30. `S25P12` — MARS
**Citation:** Wang & Song (2024), “MARS: Benchmarking the Metaphysical Reasoning Abilities of Language Models with a Multi-task Evaluation Dataset”
**Type:** metaphysical reasoning benchmark
**Aggregate mean score:** 66.2400
**Exact-task assessment:** MARS is a direct project test: retained evidence shows argument structure, scheme, support/attack, or dialectical form. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** philosophical downstream reasoning breadth. Score reflects distinct failure-mode coverage and pairability.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Explicitly introduces a multi-task metaphysical reasoning evaluation dataset/benchmark and evaluates 20 language models. Source artifact: summaries/25_ai_philosophy_dialectical_methods_summaries.md; retained category summary/paper evidence

### 31. `S02P05` — FalseQA
**Citation:** Hu et al. (2023), “Won’t Get Fooled Again: Answering Questions with False Premises”
**Type:** false-premise question benchmark
**Aggregate mean score:** 65.2000
**Exact-task assessment:** FalseQA is a useful adjacent diagnostic: retained evidence shows evidence grounding, premise critique, citation, or provenance, but not the complete scholastic source-to-structured-context pipeline. Best used alongside an authentic scholarly benchmark.
**Battery/complementarity assessment:** human-written false-premise rejection. Score reflects distinct failure-mode coverage and pairability.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Artifact 02 § Verified papers § 5: explicitly identifies FalseQA as a benchmark containing 2,365 human-written false-premise questions, explanations, and revised true-premise questions.; retained category summary/paper evidence

### 32. `19_12` — AnaloBench
**Citation:** Ye et al., 2024 — “AnaloBench: Benchmarking the Identification of Abstract and Long-context Analogies.”
**Type:** benchmark/dataset/corpus or evaluation resource
**Aggregate mean score:** 65.2000
**Exact-task assessment:** AnaloBench is a useful adjacent diagnostic: retained evidence shows abductive or analogical multi-step reasoning, but not the complete scholastic source-to-structured-context pipeline. Best used alongside an authentic scholarly benchmark.
**Battery/complementarity assessment:** Reasoning adjunct with limited direct pipeline overlap; use only when abduction/analogy is an explicit target.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** explicitly introduces a named benchmark; retained category summary/paper evidence

### 33. `S23P04` — tree-structured debate corpus
**Citation:** Bolton, Calderwood, Christensen, Kafrouni & Drori (2020), “High Quality Real-Time Structured Debate Generation”
**Type:** structured debate generation
**Aggregate mean score:** 65.1200
**Exact-task assessment:** tree-structured debate corpus is a direct project test: retained evidence shows argument structure, scheme, support/attack, or dialectical form. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** Secondary diagnostic; adds limited orthogonal coverage to core extraction, proof, context, grounding, or output tests.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Introduces/uses a tree-structured debate corpus with argument metadata for generation evaluation. Source artifact: summaries/23_disputatio_dialectical_ai_summaries.md; retained category summary/paper evidence

### 34. `19_06` — E-KAR
**Citation:** Chen et al., 2022 — “E-KAR: A Benchmark for Rationalizing Natural Language Analogical Reasoning.”
**Type:** benchmark/dataset/corpus or evaluation resource
**Aggregate mean score:** 65.0800
**Exact-task assessment:** E-KAR is a direct project test: retained evidence shows abductive or analogical multi-step reasoning. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** Reasoning adjunct with limited direct pipeline overlap; use only when abduction/analogy is an explicit target.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** explicitly introduces a named benchmark; retained category summary/paper evidence

### 35. `12-12` — NeuBAROCO
**Citation:** Ozeki et al. (2023), Evaluating Large Language Models with NeuBAROCO
**Type:** psychological syllogism benchmark
**Aggregate mean score:** 64.6800
**Exact-task assessment:** NeuBAROCO is a direct project test: retained evidence shows premise relations, proof/deduction structure, or proof-relevant selection. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** Formal/deductive adjunct; controlled or narrow coverage makes it secondary to FOLIO, ProofWriter, and LeanDojo.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Uses the NeuBAROCO syllogism dataset as an LLM benchmark, including English/Japanese items and indeterminate cases; dataset predates this evaluation paper.; retained category summary/paper evidence

### 36. `S06P11` — FAITHCOT-BENCH / FINE-COT
**Citation:** Shen et al. (2026), “FAITHCOT-BENCH: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning.”
**Type:** annotated trajectory benchmark
**Aggregate mean score:** 64.6400
**Exact-task assessment:** FAITHCOT-BENCH / FINE-COT is a direct project test: retained evidence shows annotated trajectory benchmark. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** trajectory faithfulness audit. Score reflects distinct failure-mode coverage and pairability.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Introduces FINE-COT: 1,000+ annotated trajectories across four domains with unfaithfulness labels and detector evaluation.; retained category summary/paper evidence

### 37. `19_04` — InAbHyD
**Citation:** Sun & Saparov, 2025 — “Language Models Do Not Follow Occam’s Razor: A Benchmark for Inductive and Abductive Reasoning.”
**Type:** benchmark/dataset/corpus or evaluation resource
**Aggregate mean score:** 64.1600
**Exact-task assessment:** InAbHyD is a direct project test: retained evidence shows abductive or analogical multi-step reasoning. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** Reasoning adjunct with limited direct pipeline overlap; use only when abduction/analogy is an explicit target.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** explicitly introduces a named benchmark; retained category summary/paper evidence

### 38. `S08P07` — MALLS
**Citation:** Yang et al. (2024), “MALLS/LogicLLaMA.”
**Type:** introduces_dataset_or_corpus_used_as_benchmark
**Aggregate mean score:** 64.0800
**Exact-task assessment:** MALLS is a direct project test: retained evidence shows premise relations, proof/deduction structure, or proof-relevant selection. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** Secondary diagnostic; adds limited orthogonal coverage to core extraction, proof, context, grounding, or output tests.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Introduces a 28K sentence-level NL–FOL dataset used for training/evaluation.; retained category summary/paper evidence

### 39. `S23P05` — Tree-of-Debate scientific comparison set
**Citation:** Kargupta, Agarwal, August & Han (2025), “Tree-of-Debate: Multi-Persona Debate Trees Elicit Critical Thinking for Scientific Comparative Analysis”
**Type:** scientific comparative-analysis evaluation
**Aggregate mean score:** 63.7200
**Exact-task assessment:** Tree-of-Debate scientific comparison set is a direct project test: retained evidence shows argument structure, scheme, support/attack, or dialectical form. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** Secondary diagnostic; adds limited orthogonal coverage to core extraction, proof, context, grounding, or output tests.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Builds a paper/persona debate evaluation set and evaluates against baselines with expert comparison. Source artifact: summaries/23_disputatio_dialectical_ai_summaries.md; retained category summary/paper evidence

### 40. `11-05` — LOGICOM
**Citation:** Payandeh et al. (2024), How Susceptible are LLMs to Logical Fallacies?
**Type:** multi-round persuasion/susceptibility benchmark
**Aggregate mean score:** 63.3600
**Exact-task assessment:** LOGICOM is a useful adjacent diagnostic: retained evidence shows argument structure, scheme, support/attack, or dialectical form, but not the complete scholastic source-to-structured-context pipeline. Best used alongside an authentic scholarly benchmark.
**Battery/complementarity assessment:** Fallacy/grounding adjunct; retain when failure diagnosis needs this narrower slice.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Introduces LOGICOM and releases 5k+ paired logical/fallacious arguments for multi-round persuasion evaluation.; retained category summary/paper evidence

### 41. `S10P08` — NLAS-multi
**Citation:** Ruiz-Dolz, Taverner, Lawrence & Reed (2024), “NLAS-multi.”
**Type:** introduces_dataset_or_corpus_used_as_benchmark
**Aggregate mean score:** 62.5600
**Exact-task assessment:** NLAS-multi is a useful adjacent diagnostic: retained evidence shows cross-cultural or multilingual variation, but not the complete scholastic source-to-structured-context pipeline. Best used alongside an authentic scholarly benchmark.
**Battery/complementarity assessment:** Scheme-classification adjunct; useful for diversity, but overlaps front-end extraction anchors.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Introduces multilingual generated arguments spanning 20 schemes, 50 topics, two stances, English/Spanish.; retained category summary/paper evidence

### 42. `S05P08` — RAGTruth
**Citation:** Niu et al. (2024), “RAGTruth: A Hallucination Corpus for Developing Trustworthy Retrieval-Augmented Language Models”
**Type:** RAG hallucination corpus/benchmark
**Aggregate mean score:** 62.3200
**Exact-task assessment:** RAGTruth is a useful adjacent diagnostic: retained evidence shows evidence grounding, premise critique, citation, or provenance, but not the complete scholastic source-to-structured-context pipeline. Best used alongside an authentic scholarly benchmark.
**Battery/complementarity assessment:** word/case-level hallucination audit. Score reflects distinct failure-mode coverage and pairability.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Artifact 05 § Verified papers § 8: explicitly says RAGTruth provides nearly 18,000 RAG responses with case- and word-level hallucination annotations and benchmarks detection methods.; retained category summary/paper evidence

### 43. `S06P06` — Counterfactual reasoning task suite
**Citation:** Wu et al. (2024), “Reasoning or Reciting? Exploring the Capabilities and Limitations of Language Models Through Counterfactual Tasks.”
**Type:** multi-task benchmark
**Aggregate mean score:** 62.1600
**Exact-task assessment:** Counterfactual reasoning task suite is a useful adjacent diagnostic: retained evidence shows multi-task benchmark, but not the complete scholastic source-to-structured-context pipeline. Best used alongside an authentic scholarly benchmark.
**Battery/complementarity assessment:** Secondary diagnostic; adds limited orthogonal coverage to core extraction, proof, context, grounding, or output tests.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Introduces 11 counterfactual variants spanning arithmetic, logic, code, spatial, music, chess, and related tasks.; retained category summary/paper evidence

### 44. `19_09` — ANALOGICAL
**Citation:** Wijesiriwardene et al., 2023 — “ANALOGICAL: A Novel Benchmark for Long Text Analogy Evaluation in Large Language Models.”
**Type:** benchmark/dataset/corpus or evaluation resource
**Aggregate mean score:** 61.4000
**Exact-task assessment:** ANALOGICAL is a useful adjacent diagnostic: retained evidence shows abductive or analogical multi-step reasoning, but not the complete scholastic source-to-structured-context pipeline. Best used alongside an authentic scholarly benchmark.
**Battery/complementarity assessment:** Reasoning adjunct with limited direct pipeline overlap; use only when abduction/analogy is an explicit target.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** explicitly introduces a named benchmark; retained category summary/paper evidence

### 45. `12-08` — BIG-bench logical deduction/syllogism tasks
**Citation:** Srivastava et al. (2022), Beyond the Imitation Game (BIG-bench)
**Type:** multi-task benchmark suite
**Aggregate mean score:** 60.3200
**Exact-task assessment:** BIG-bench logical deduction/syllogism tasks is a direct project test: retained evidence shows argument structure, scheme, support/attack, or dialectical form. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** Formal/deductive adjunct; controlled or narrow coverage makes it secondary to FOLIO, ProofWriter, and LeanDojo.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Introduces the collaborative BIG-bench suite, including logical deduction, categorical/formal syllogism, and fallacy tasks.; retained category summary/paper evidence

### 46. `19_15` — complex-analogy benchmark
**Citation:** Das & Balke, 2025 — “From Prototypical to Relational: How LLMs Navigate Complex Analogies.”
**Type:** benchmark/dataset/corpus or evaluation resource
**Aggregate mean score:** 60.1600
**Exact-task assessment:** complex-analogy benchmark is a useful adjacent diagnostic: retained evidence shows abductive or analogical multi-step reasoning, but not the complete scholastic source-to-structured-context pipeline. Best used alongside an authentic scholarly benchmark.
**Battery/complementarity assessment:** Reasoning adjunct with limited direct pipeline overlap; use only when abduction/analogy is an explicit target.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** explicitly introduces a named benchmark; retained category summary/paper evidence

### 47. `S03P10` — LongPiBench
**Citation:** Tian et al. (2025), “Distance between Relevant Information Pieces Causes Bias in Long-Context LLMs”
**Type:** multi-piece long-context positional-bias benchmark
**Aggregate mean score:** 59.0800
**Exact-task assessment:** LongPiBench is a direct project test: retained evidence shows long-context retrieval, multi-hop tracing, or positional/context stress. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** multi-piece dependency and positional stress. Score reflects distinct failure-mode coverage and pairability.
**Artifact/battery status:** `verified`; `include_core`
**Evidence basis:** Artifact 03 § Verified papers retained § 10: explicitly says the paper introduces LongPiBench for multiple relevant information pieces separated by varying distances.; retained category summary/paper evidence

### 48. `S02P06` — KG-FPQ
**Citation:** Zhu et al. (2025), “KG-FPQ: Evaluating Factuality Hallucination in LLMs with Knowledge Graph-based False Premise Questions”
**Type:** knowledge-graph false-premise benchmark
**Aggregate mean score:** 58.8800
**Exact-task assessment:** KG-FPQ is a useful adjacent diagnostic: retained evidence shows evidence grounding, premise critique, citation, or provenance, but not the complete scholastic source-to-structured-context pipeline. Best used alongside an authentic scholarly benchmark.
**Battery/complementarity assessment:** Secondary diagnostic; adds limited orthogonal coverage to core extraction, proof, context, grounding, or output tests.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Artifact 02 § Verified papers § 6: explicitly says the paper builds KG-FPQ, approximately 178k questions across domains, confusability levels, and task formats.; retained category summary/paper evidence

### 49. `15-08` — AMAeval
**Citation:** Galatolo et al. (2025), Beyond Ethical Alignment: Evaluating LLMs as Artificial Moral Assistants
**Type:** moral-reasoning benchmark/framework
**Aggregate mean score:** 58.2000
**Exact-task assessment:** AMAeval is a direct project test: retained evidence shows abductive or analogical multi-step reasoning. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** Philosophical-output adjunct; weak structural diagnostics compared with direct argument/proof/grounding tests.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Introduces AMAeval and a formal Artificial Moral Assistant framework evaluating deductive/abductive reasoning chains and assessment.; retained category summary/paper evidence

### 50. `S03P09` — NoLiMa
**Citation:** Modarressi et al. (2025), “NoLiMa: Long-Context Evaluation Beyond Literal Matching”
**Type:** semantic long-context retrieval benchmark
**Aggregate mean score:** 57.6800
**Exact-task assessment:** NoLiMa is a direct project test: retained evidence shows long-context retrieval, multi-hop tracing, or positional/context stress. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** semantic retrieval under low lexical overlap. Score reflects distinct failure-mode coverage and pairability.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Artifact 03 § Verified papers retained § 9: explicitly says NoLiMa is a benchmark minimizing literal overlap and testing latent association at long context lengths.; retained category summary/paper evidence

### 51. `19_10` — StoryAnalogy
**Citation:** Yuan et al., 2023 — “StoryAnalogy: Deriving Story-level Analogies from Large Language Models to Unlock Analogical Understanding.”
**Type:** benchmark/dataset/corpus or evaluation resource
**Aggregate mean score:** 57.5600
**Exact-task assessment:** StoryAnalogy is a useful adjacent diagnostic: retained evidence shows abductive or analogical multi-step reasoning, but not the complete scholastic source-to-structured-context pipeline. Best used alongside an authentic scholarly benchmark.
**Battery/complementarity assessment:** Reasoning adjunct with limited direct pipeline overlap; use only when abduction/analogy is an explicit target.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** introduces a dataset or corpus used as an evaluation resource; retained category summary/paper evidence

### 52. `S03P08` — RULER
**Citation:** Hsieh et al. (2024), “RULER: What’s the Real Context Size of Your Long-Context Language Models?”
**Type:** long-context evaluation benchmark
**Aggregate mean score:** 56.5600
**Exact-task assessment:** RULER is a useful adjacent diagnostic: retained evidence shows long-context retrieval, multi-hop tracing, or positional/context stress, but not the complete scholastic source-to-structured-context pipeline. Best used alongside an authentic scholarly benchmark.
**Battery/complementarity assessment:** generic multi-needle/multi-hop context control. Score reflects distinct failure-mode coverage and pairability.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Artifact 03 § Verified papers retained § 8: explicitly describes RULER as extending needle-in-a-haystack evaluation with multiple needles, multi-hop tracing, and aggregation across 13 tasks.; retained category summary/paper evidence

### 53. `19_14` — KnowledgePrompts 15K proportional-analogy dataset
**Citation:** Wijesiriwardene et al., 2025 — “KnowledgePrompts: Exploring the Abilities of Large Language Models to Solve Proportional Analogies via Knowledge-Enhanced Prompting.”
**Type:** benchmark/dataset/corpus or evaluation resource
**Aggregate mean score:** 55.2000
**Exact-task assessment:** KnowledgePrompts 15K proportional-analogy dataset is a useful adjacent diagnostic: retained evidence shows abductive or analogical multi-step reasoning, but not the complete scholastic source-to-structured-context pipeline. Best used alongside an authentic scholarly benchmark.
**Battery/complementarity assessment:** Reasoning adjunct with limited direct pipeline overlap; use only when abduction/analogy is an explicit target.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** introduces a dataset or corpus used as an evaluation resource; retained category summary/paper evidence

### 54. `15-02` — InterIDEAS
**Citation:** Yang et al. (2025), InterIDEAS: Philosophical Intertextuality via LLMs
**Type:** philosophical intertextuality dataset
**Aggregate mean score:** 54.8000
**Exact-task assessment:** InterIDEAS is a direct project test: retained evidence shows evidence grounding, premise critique, citation, or provenance. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** Philosophical-output adjunct; weak structural diagnostics compared with direct argument/proof/grounding tests.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Introduces a philosophical intertextuality dataset combining authentic texts, bibliometric relations, LLM processing, RAG, and human evaluation.; retained category summary/paper evidence

### 55. `17_01` — LogiQA
**Citation:** LogiQA: A Challenge Dataset for Machine Reading Comprehension with Logical Reasoning
**Type:** benchmark/dataset/corpus or evaluation resource
**Aggregate mean score:** 53.8000
**Exact-task assessment:** LogiQA is a useful adjacent diagnostic: retained evidence shows cross-cultural or multilingual variation, but not the complete scholastic source-to-structured-context pipeline. Best used alongside an authentic scholarly benchmark.
**Battery/complementarity assessment:** Cultural or multilingual robustness adjunct; valuable for transfer audits, not a core pipeline test.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** explicitly introduces a named benchmark; retained category summary/paper evidence

### 56. `19_02` — (unnamed benchmark/resource)
**Citation:** Bai et al., 2024 — “Advancing Abductive Reasoning in Knowledge Graphs through Complex Logical Hypothesis Generation.”
**Type:** introduces_dataset_or_corpus_used_as_benchmark
**Aggregate mean score:** 53.7200
**Exact-task assessment:** is a useful adjacent diagnostic: retained evidence shows abductive or analogical multi-step reasoning, but not the complete scholastic source-to-structured-context pipeline. Best used alongside an authentic scholarly benchmark.
**Battery/complementarity assessment:** Reasoning adjunct with limited direct pipeline overlap; use only when abduction/analogy is an explicit target.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** introduces a dataset or corpus used as an evaluation resource; retained category summary/paper evidence

### 57. `S03P05` — LongBench
**Citation:** Bai et al. (2024), “LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding”
**Type:** bilingual multitask long-context benchmark
**Aggregate mean score:** 52.8000
**Exact-task assessment:** LongBench is a useful adjacent diagnostic: retained evidence shows long-context retrieval, multi-hop tracing, or positional/context stress, but not the complete scholastic source-to-structured-context pipeline. Best used alongside an authentic scholarly benchmark.
**Battery/complementarity assessment:** Long-context adjunct; pair with dependency-bearing tasks rather than treat as standalone evidence.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Artifact 03 § Verified papers retained § 5: explicitly says the paper introduces a bilingual, multitask benchmark across QA, summarization, few-shot learning, and other tasks.; retained category summary/paper evidence

### 58. `17_02` — LogiQA 2.0
**Citation:** LogiQA 2.0—An Improved Dataset for Logical Reasoning in Natural Language Understanding
**Type:** benchmark/dataset/corpus or evaluation resource
**Aggregate mean score:** 51.6400
**Exact-task assessment:** LogiQA 2.0 is a limited adjacent resource: retained evidence only supports cross-cultural or multilingual variation; exact scholastic reasoning/context-engineering fit is limited. Treat as supplemental, not a primary gate.
**Battery/complementarity assessment:** Cultural or multilingual robustness adjunct; valuable for transfer audits, not a core pipeline test.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** introduces a dataset or corpus used as an evaluation resource; retained category summary/paper evidence

### 59. `S22P04` — Index Thomisticus Treebank
**Citation:** McGillivray, Passarotti, and Ruffolo, “The Index Thomisticus Treebank Project: Annotation, Parsing and Valency Lexicon” (2009)
**Type:** Medieval Latin dependency-parsing treebank
**Aggregate mean score:** 51.0800
**Exact-task assessment:** Index Thomisticus Treebank is a direct project test: retained evidence shows scholarly-language data and source-text structure. This most directly exercises the project’s inspectable reasoning, structure recovery, grounding, or context-selection path.
**Battery/complementarity assessment:** Secondary diagnostic; adds limited orthogonal coverage to core extraction, proof, context, grounding, or output tests.
**Artifact/battery status:** `verified`; `include_core_transfer_gate`
**Evidence basis:** Introduces the dependency-annotated Aquinas treebank used for parser evaluation. Source artifact: summaries/22_scholastic_digital_humanities_ai_summaries.md; retained category summary/paper evidence

### 60. `S24P10` — Quranic Arabic PropBank
**Citation:** Hawwari, Diab, and Zaghouani, “A Pilot PropBank Annotation for Quranic Arabic”
**Type:** predicate-argument semantic-role labeling
**Aggregate mean score:** 49.6400
**Exact-task assessment:** Quranic Arabic PropBank is a useful adjacent diagnostic: retained evidence shows scholarly-language data and source-text structure, but not the complete scholastic source-to-structured-context pipeline. Best used alongside an authentic scholarly benchmark.
**Battery/complementarity assessment:** Language-resource adjunct for Arabic coverage; supports preprocessing audits, not end-to-end reasoning battery.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Introduces a pilot PropBank with 7,227 verbal occurrences and annotation evaluation. Source artifact: summaries/24_islamic_comparative_scholastic_ai_summaries.md; retained category summary/paper evidence

### 61. `15-05` — frame/symbol-grounding zero-shot benchmark
**Citation:** Oka (2025), Evaluating LLMs on the Frame and Symbol Grounding Problems
**Type:** philosophical AI benchmark
**Aggregate mean score:** 46.5600
**Exact-task assessment:** frame/symbol-grounding zero-shot benchmark is a useful adjacent diagnostic: retained evidence shows evidence grounding, premise critique, citation, or provenance, but not the complete scholastic source-to-structured-context pipeline. Best used alongside an authentic scholarly benchmark.
**Battery/complementarity assessment:** Adjacent capability or scale boundary; useful as optional stress evidence, but adds little to minimal integrated battery.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Designs zero-shot tasks operationalizing the frame and symbol-grounding problems and evaluates 13 models.; retained category summary/paper evidence

### 62. `S03P03` — Long Range Arena (LRA)
**Citation:** Tay et al. (2021), “Long Range Arena: A Benchmark for Efficient Transformers”
**Type:** long-context sequence-processing benchmark
**Aggregate mean score:** 46.2000
**Exact-task assessment:** Long Range Arena (LRA) is a useful adjacent diagnostic: retained evidence shows long-context retrieval, multi-hop tracing, or positional/context stress, but not the complete scholastic source-to-structured-context pipeline. Best used alongside an authentic scholarly benchmark.
**Battery/complementarity assessment:** Adjacent capability or scale boundary; useful as optional stress evidence, but adds little to minimal integrated battery.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Artifact 03 § Verified papers retained § 3: explicitly says the paper introduces a unified benchmark with tasks spanning roughly 1K–16K tokens.; retained category summary/paper evidence

### 63. `S03P06` — ∞Bench
**Citation:** Zhang et al. (2024), “∞Bench: Extending Long Context Evaluation Beyond 100K Tokens”
**Type:** ultra-long-context evaluation suite
**Aggregate mean score:** 45.7600
**Exact-task assessment:** ∞Bench is a useful adjacent diagnostic: retained evidence shows long-context retrieval, multi-hop tracing, or positional/context stress, but not the complete scholastic source-to-structured-context pipeline. Best used alongside an authentic scholarly benchmark.
**Battery/complementarity assessment:** Adjacent capability or scale boundary; useful as optional stress evidence, but adds little to minimal integrated battery.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Artifact 03 § Verified papers retained § 6: explicitly says the paper proposes an evaluation suite for contexts beyond 100K tokens.; retained category summary/paper evidence

### 64. `S24P09` — OpenITI-derived Classical Arabic corpus
**Citation:** Yousef et al., “Enhancing State-of-the-Art NLP Models for Classical Arabic”
**Type:** NER/relationship/onomastic NLP
**Aggregate mean score:** 43.4800
**Exact-task assessment:** OpenITI-derived Classical Arabic corpus is a limited adjacent resource: retained evidence only supports scholarly-language data and source-text structure; exact scholastic reasoning/context-engineering fit is limited. Treat as supplemental, not a primary gate.
**Battery/complementarity assessment:** Language-resource adjunct for Arabic coverage; supports preprocessing audits, not end-to-end reasoning battery.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Introduces expert-annotated Classical Arabic resources and evaluates models; corpus is a reusable evaluation resource. Source artifact: summaries/24_islamic_comparative_scholastic_ai_summaries.md; retained category summary/paper evidence

### 65. `S24P12` — HAQA and QUQA
**Citation:** Alnefaie, Atwell, and Alsalka, “HAQA and QUQA: Constructing Two Arabic Question-Answering Corpora for the Quran and Hadith”
**Type:** Quran/Hadith question answering
**Aggregate mean score:** 43.0400
**Exact-task assessment:** HAQA and QUQA is a limited adjacent resource: retained evidence only supports scholarly-language data and source-text structure; exact scholastic reasoning/context-engineering fit is limited. Treat as supplemental, not a primary gate.
**Battery/complementarity assessment:** Language-resource adjunct for Arabic coverage; supports preprocessing audits, not end-to-end reasoning battery.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Introduces two reusable QA corpora with 1,598 and 3,382 QA pairs. Source artifact: summaries/24_islamic_comparative_scholastic_ai_summaries.md; retained category summary/paper evidence

### 66. `15-06` — AwareBench/AwareEval
**Citation:** Li et al. (2024), I Think, Therefore I am: AwareBench
**Type:** awareness/self-model benchmark
**Aggregate mean score:** 42.8400
**Exact-task assessment:** AwareBench/AwareEval is a limited adjacent resource: retained evidence only supports philosophical or metaphysical reasoning/text relations; exact scholastic reasoning/context-engineering fit is limited. Treat as supplemental, not a primary gate.
**Battery/complementarity assessment:** Adjacent capability or scale boundary; useful as optional stress evidence, but adds little to minimal integrated battery.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Introduces AwareBench with five dimensions and releases AwareEval questions for model evaluation.; retained category summary/paper evidence

### 67. `S24P11` — Quran–Hadith Classical Arabic dataset
**Citation:** Altammami and Atwell, “Challenging the Transformer-based Models with a Classical Arabic Dataset: Quran and Hadith”
**Type:** semantic relatedness
**Aggregate mean score:** 42.2800
**Exact-task assessment:** Quran–Hadith Classical Arabic dataset is a limited adjacent resource: retained evidence only supports scholarly-language data and source-text structure; exact scholastic reasoning/context-engineering fit is limited. Treat as supplemental, not a primary gate.
**Battery/complementarity assessment:** Language-resource adjunct for Arabic coverage; supports preprocessing audits, not end-to-end reasoning battery.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Introduces an expert-constructed cross-domain Quran/Hadith dataset for transformer evaluation. Source artifact: summaries/24_islamic_comparative_scholastic_ai_summaries.md; retained category summary/paper evidence

### 68. `S22P08` — eFontes Medieval Latin corpus
**Citation:** Nowak, Ziębura, Wróbel, and Smywiński-Pohl, “eFontes: Part of Speech Tagging and Lemmatization of Medieval Latin Texts: A Cross-Genre Survey” (2024)
**Type:** POS/lemmatization/morphology evaluation
**Aggregate mean score:** 41.2800
**Exact-task assessment:** eFontes Medieval Latin corpus is a useful adjacent diagnostic: retained evidence shows scholarly-language data and source-text structure, but not the complete scholastic source-to-structured-context pipeline. Best used alongside an authentic scholarly benchmark.
**Battery/complementarity assessment:** Adjacent capability or scale boundary; useful as optional stress evidence, but adds little to minimal integrated battery.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Introduces a Medieval Latin corpus and evaluates transformer annotation models across genres. Source artifact: summaries/22_scholastic_digital_humanities_ai_summaries.md; retained category summary/paper evidence

### 69. `17_11` — Global MMLU
**Citation:** Global MMLU: Understanding and Addressing Cultural and Linguistic Biases in Multilingual Evaluation
**Type:** benchmark/dataset/corpus or evaluation resource
**Aggregate mean score:** 41.1600
**Exact-task assessment:** Global MMLU is a limited adjacent resource: retained evidence only supports cross-cultural or multilingual variation; exact scholastic reasoning/context-engineering fit is limited. Treat as supplemental, not a primary gate.
**Battery/complementarity assessment:** Cultural or multilingual robustness adjunct; valuable for transfer audits, not a core pipeline test.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** explicitly introduces a named benchmark; retained category summary/paper evidence

### 70. `17_09` — SeaEval
**Citation:** SeaEval for Multilingual Foundation Models: From Cross-Lingual Alignment to Cultural Reasoning
**Type:** benchmark/dataset/corpus or evaluation resource
**Aggregate mean score:** 40.6000
**Exact-task assessment:** SeaEval is a limited adjacent resource: retained evidence only supports cross-cultural or multilingual variation; exact scholastic reasoning/context-engineering fit is limited. Treat as supplemental, not a primary gate.
**Battery/complementarity assessment:** Cultural or multilingual robustness adjunct; valuable for transfer audits, not a core pipeline test.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** explicitly introduces a named benchmark; retained category summary/paper evidence

### 71. `17_12` — CQ-Bench
**Citation:** Can LLMs Grasp Implicit Cultural Values? Benchmarking LLMs’ Cultural Intelligence with CQ-Bench
**Type:** benchmark/dataset/corpus or evaluation resource
**Aggregate mean score:** 40.4800
**Exact-task assessment:** CQ-Bench is a limited adjacent resource: retained evidence only supports cross-cultural or multilingual variation; exact scholastic reasoning/context-engineering fit is limited. Treat as supplemental, not a primary gate.
**Battery/complementarity assessment:** Cultural or multilingual robustness adjunct; valuable for transfer audits, not a core pipeline test.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** explicitly introduces a named benchmark; retained category summary/paper evidence

### 72. `17_14` — DRISHTIKON
**Citation:** DRISHTIKON: A Multimodal Multilingual Benchmark for Testing Language Models’ Understanding on Indian Culture
**Type:** benchmark/dataset/corpus or evaluation resource
**Aggregate mean score:** 39.6800
**Exact-task assessment:** DRISHTIKON is a limited adjacent resource: retained evidence only supports cross-cultural or multilingual variation; exact scholastic reasoning/context-engineering fit is limited. Treat as supplemental, not a primary gate.
**Battery/complementarity assessment:** Cultural or multilingual robustness adjunct; valuable for transfer audits, not a core pipeline test.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** explicitly introduces a named benchmark; retained category summary/paper evidence

### 73. `17_04` — GeoMLAMA
**Citation:** GeoMLAMA: Geo-Diverse Commonsense Probing on Multilingual Pre-Trained Language Models
**Type:** benchmark/dataset/corpus or evaluation resource
**Aggregate mean score:** 39.6000
**Exact-task assessment:** GeoMLAMA is a limited adjacent resource: retained evidence only supports cross-cultural or multilingual variation; exact scholastic reasoning/context-engineering fit is limited. Treat as supplemental, not a primary gate.
**Battery/complementarity assessment:** Cultural or multilingual robustness adjunct; valuable for transfer audits, not a core pipeline test.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** explicitly introduces a named benchmark; retained category summary/paper evidence

### 74. `17_15` — SANSKRITI
**Citation:** SANSKRITI: A Comprehensive Benchmark for Evaluating Language Models’ Knowledge of Indian Culture
**Type:** benchmark/dataset/corpus or evaluation resource
**Aggregate mean score:** 39.4800
**Exact-task assessment:** SANSKRITI is a limited adjacent resource: retained evidence only supports cross-cultural or multilingual variation; exact scholastic reasoning/context-engineering fit is limited. Treat as supplemental, not a primary gate.
**Battery/complementarity assessment:** Cultural or multilingual robustness adjunct; valuable for transfer audits, not a core pipeline test.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** explicitly introduces a named benchmark; retained category summary/paper evidence

### 75. `17_03` — Mickey
**Citation:** Common Sense Beyond English: Evaluating and Improving Multilingual Language Models for Commonsense Reasoning
**Type:** benchmark/dataset/corpus or evaluation resource
**Aggregate mean score:** 38.9200
**Exact-task assessment:** Mickey is a limited adjacent resource: retained evidence only supports cross-cultural or multilingual variation; exact scholastic reasoning/context-engineering fit is limited. Treat as supplemental, not a primary gate.
**Battery/complementarity assessment:** Cultural or multilingual robustness adjunct; valuable for transfer audits, not a core pipeline test.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** introduces a dataset or corpus used as an evaluation resource; retained category summary/paper evidence

### 76. `S22P02` — CREMMA Medii Aevi
**Citation:** Clérice, Vlachou-Efstathiou, and Chagué, “CREMMA Medii Aevi: Literary Manuscript Text Recognition in Latin” (2023)
**Type:** Medieval Latin HTR dataset
**Aggregate mean score:** 38.6800
**Exact-task assessment:** CREMMA Medii Aevi is a limited adjacent resource: retained evidence only supports scholarly-language data and source-text structure; exact scholastic reasoning/context-engineering fit is limited. Treat as supplemental, not a primary gate.
**Battery/complementarity assessment:** Adjacent capability or scale boundary; useful as optional stress evidence, but adds little to minimal integrated battery.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** Introduces a reusable Medieval Latin manuscript HTR dataset and evaluates recognition models. Source artifact: summaries/22_scholastic_digital_humanities_ai_summaries.md; retained category summary/paper evidence

### 77. `17_07` — CDEval
**Citation:** CDEval: A Benchmark for Measuring the Cultural Dimensions of Large Language Models
**Type:** benchmark/dataset/corpus or evaluation resource
**Aggregate mean score:** 38.4800
**Exact-task assessment:** CDEval is a limited adjacent resource: retained evidence only supports cross-cultural or multilingual variation; exact scholastic reasoning/context-engineering fit is limited. Treat as supplemental, not a primary gate.
**Battery/complementarity assessment:** Cultural or multilingual robustness adjunct; valuable for transfer audits, not a core pipeline test.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** explicitly introduces a named benchmark; retained category summary/paper evidence

### 78. `17_13` — Arab-culture commonsense dataset
**Citation:** Commonsense Reasoning in Arab Culture
**Type:** benchmark/dataset/corpus or evaluation resource
**Aggregate mean score:** 37.5600
**Exact-task assessment:** Arab-culture commonsense dataset is a limited adjacent resource: retained evidence only supports cross-cultural or multilingual variation; exact scholastic reasoning/context-engineering fit is limited. Treat as supplemental, not a primary gate.
**Battery/complementarity assessment:** Cultural or multilingual robustness adjunct; valuable for transfer audits, not a core pipeline test.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** introduces a dataset or corpus used as an evaluation resource; retained category summary/paper evidence

### 79. `17_08` — WorldValuesBench
**Citation:** WorldValuesBench: A Large-Scale Benchmark Dataset for Multi-Cultural Value Awareness of Language Models
**Type:** benchmark/dataset/corpus or evaluation resource
**Aggregate mean score:** 36.8400
**Exact-task assessment:** WorldValuesBench is a limited adjacent resource: retained evidence only supports cross-cultural or multilingual variation; exact scholastic reasoning/context-engineering fit is limited. Treat as supplemental, not a primary gate.
**Battery/complementarity assessment:** Cultural or multilingual robustness adjunct; valuable for transfer audits, not a core pipeline test.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** explicitly introduces a named benchmark; retained category summary/paper evidence

### 80. `17_10` — LLM-GLOBE
**Citation:** LLM-GLOBE: A Benchmark Evaluating the Cultural Values Embedded in LLM Output
**Type:** benchmark/dataset/corpus or evaluation resource
**Aggregate mean score:** 36.6000
**Exact-task assessment:** LLM-GLOBE is a limited adjacent resource: retained evidence only supports cross-cultural or multilingual variation; exact scholastic reasoning/context-engineering fit is limited. Treat as supplemental, not a primary gate.
**Battery/complementarity assessment:** Cultural or multilingual robustness adjunct; valuable for transfer audits, not a core pipeline test.
**Artifact/battery status:** `not separately artifact-verified in final battery`; `not selected in final battery`
**Evidence basis:** explicitly introduces a named benchmark; retained category summary/paper evidence

## Interpretation

- Highest aggregate score does not mean best standalone benchmark for the complete pipeline.
- Use the final battery recommendation and adversarial reports to distinguish authentic text, synthetic controls, formal proof controls, context stress, grounding, and argument-structure tests.
- Do not double-count ProofWriter, QT-SCHEMES, or LeanDojo family duplicates.
