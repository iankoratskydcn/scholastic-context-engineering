# Subtopic 12 — Syllogistic and deductive-reasoning benchmarks for LLMs

- **Research date:** 2026-10-12
- **Scope:** Benchmarks, datasets, and foundational experimental tests for categorical syllogisms, first-order/deductive reasoning over natural-language theories, proof production, premise-order/content effects, and LLM evaluation protocols.
- **Verified paper count:** 15
- **Primary discovery route:** Google Scholar was attempted first with the variants recorded below. Scholar pages were partly noisy/blocked by result ranking and sometimes returned author profiles or support pages rather than stable paper records. Candidate papers were retained only after opening an ACL Anthology, arXiv, publisher, proceedings, PubMed, or paper-PDF page. Search snippets alone were not used as paper verification.
- **Key novelty question:** Does the project need a benchmark that tests only answer accuracy, or one that separately tests validity, proof/derivation, invariance under logically irrelevant changes, premise selection, and human-like content/order biases across multiple deductive forms?

## Required fields

- **Topic:** syllogistic and deductive-reasoning benchmarks for LLMs.
- **Paper count:** 15 verified papers/reports.
- **Novelty threat:** answer-only syllogism/deduction evaluation, synthetic proof-depth testing, FOL formalization, and human-like syllogistic bias testing all have substantial prior art; differentiation should come from proof certificates, minimal-premise/context annotations, invariance tests, richer unknown/contradiction labels, and cross-tradition coverage.
- **Search failures:** Google Scholar was noisy/partly blocked for stable paper retrieval; direct Scholar extraction failed; one OpenReview PDF was excluded after browser verification blocked full-paper inspection. Detailed failures are recorded below.

## Scholar-first search variants

1. `syllogistic reasoning large language models benchmark`
2. `deductive reasoning benchmark LLM logical deduction`
3. `syllogism language models dataset`
4. `RuleTaker ProofWriter FOLIO logical reasoning`
5. `natural language syllogistic reasoning benchmark SylloBase`
6. `NeuBAROCO syllogism language models human biases`
7. `first-order logic reasoning benchmark natural language LLM`
8. `PrOntoQA chain-of-thought deductive reasoning`
9. `BIG-bench logical deduction syllogisms formal fallacies`
10. `premise order effect LLM syllogistic reasoning`

Scholar was useful for locating canonical titles and related-work clusters, but not consistently usable as a stable full-text retrieval route. Fallback discovery used ACL Anthology, arXiv, IJCAI, NeurIPS proceedings, BIG-bench task pages/PDFs, PubMed, and opened paper PDFs.

## Retained verified papers

### 1. Syllogistic Inference
- **Authors/year/venue:** P. N. Johnson-Laird and Bruno G. Bara, 1984, *Cognition*.
- **Link:** https://www.sciencedirect.com/science/article/abs/pii/0010027784900350
- **What was verified:** The paper reviews psychological theories of syllogistic inference and reports experiments on syllogisms and three-term series problems, including effects of the arrangement/figure of terms.
- **Benchmark value:** Foundational human test regime: 64 categorical syllogistic forms when premise-term arrangement is considered, with figure and validity as controlled factors.
- **Novelty threat:** Any LLM benchmark that claims to introduce controlled figure/mood manipulation should acknowledge this classical experimental design.

### 2. Believability and syllogistic reasoning
- **Authors/year/venue:** J. Oakhill, P. N. Johnson-Laird, A. Garnham, 1989, *Cognition*.
- **Link:** https://pubmed.ncbi.nlm.nih.gov/2721132/
- **What was verified:** The abstract states that the experiments investigate where believability effects enter syllogistic reasoning: premise interpretation, alternative representations, or filtering of putative conclusions.
- **Benchmark value:** Foundational content/belief-bias test. It motivates matched neutral, believable, and unbelievable content rather than accuracy-only scoring.
- **Novelty threat:** A benchmark using real-world plausibility or belief-consistency conditions is not novel merely because the evaluated agents are LLMs.

### 3. Transformers as Soft Reasoners over Language (RuleTaker)
- **Authors/year/venue:** Peter Clark, Oyvind Tafjord, Kyle Richardson, 2020, IJCAI.
- **Links:** https://www.ijcai.org/Proceedings/2020/537 ; https://arxiv.org/abs/2002.05867
- **What was verified:** RuleTaker generates natural-language theories of facts/rules and assertions, with theorem-prover-derived labels. The paper reports high accuracy and generalization to deeper rule chains than seen in training.
- **Benchmark value:** Canonical controlled deductive benchmark with explicit reasoning depth and closed-world evaluation; an essential baseline for multihop rule inference.
- **Limitations:** Synthetic grammar, small vocabulary, and narrow rule language; does not test categorical syllogistic moods or open-ended argument interpretation.

### 4. ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language
- **Authors/year/venue:** Oyvind Tafjord, Bhavana Dalvi, Peter Clark, 2021, Findings of ACL.
- **Link:** https://aclanthology.org/2021.findings-acl.317.pdf
- **What was verified:** The PDF describes True/False/Unknown reasoning under closed- and open-world variants, enumerated proofs, implication enumeration, and single-fact abduction. Datasets include D0, D1, D2, D3, and D5 depth settings, with 100k questions per D* dataset.
- **Benchmark value:** Moves beyond answer classification to proof generation, all-implication enumeration, open-world uncertainty, and abduction.
- **Limitations:** Still largely templated and Datalog-like; proof correctness is exact for the generated theory but not a test of nuanced human argument interpretation.

### 5. Diagnosing the First-Order Logical Reasoning Ability Through LogicNLI
- **Authors/year/venue:** Jidong Tian et al., 2021, EMNLP.
- **Link:** https://aclanthology.org/2021.emnlp-main.303/
- **What was verified:** LogicNLI is an NLI-style FOL benchmark designed to disentangle logical reasoning from commonsense inference and diagnose accuracy, robustness, generalization, and interpretability. Experiments evaluate BERT, RoBERTa, and XLNet.
- **Benchmark value:** Explicit diagnostic framing rather than a single aggregate score; useful for separating logical competence from lexical/world-knowledge shortcuts.
- **Limitations:** Synthetic or controlled logical language and pre-LLM model regime; does not cover classical syllogistic figure/mood effects directly.

### 6. FOLIO: Natural Language Reasoning with First-Order Logic
- **Authors/year/venue:** Simeng Han et al., 2022 arXiv; published in EMNLP 2024 proceedings version.
- **Links:** https://arxiv.org/abs/2209.00840 ; https://aclanthology.org/2024.emnlp-main.1229.pdf
- **What was verified:** FOLIO contains 1,430 unique conclusions paired with 487 premise sets, human-authored natural-language problems, FOL annotations, and automatic FOL-engine verification. It evaluates both NL reasoning and NL-to-FOL translation.
- **Benchmark value:** Stronger naturalness and logical diversity than RuleTaker/LogicNLI; supports separate entailment and formalization evaluation.
- **Limitations:** Binary/three-way conclusion validity is not a complete proof-quality or argument-structure measure; expert annotation and formal encoding can still impose one intended interpretation.

### 7. Language Models Are Greedy Reasoners: A Systematic Formal Analysis of Chain-of-Thought (PrOntoQA)
- **Authors/year/venue:** Abulhair Saparov and He He, 2022 arXiv; related OOD work in NeurIPS 2023.
- **Link:** https://arxiv.org/abs/2210.01240
- **What was verified:** PrOntoQA is generated from synthetic first-order world models, allowing model chain-of-thought to be parsed into symbolic proofs and analyzed by reasoning depth. The benchmark is designed to test whether apparent reasoning follows valid deductive chains rather than shallow heuristics.
- **Benchmark value:** Foundational test for proof-depth and chain-of-thought faithfulness in synthetic deduction; standard benchmark in solver-augmented LLM work.
- **Limitations:** Restricted ontology and repeated modus-ponens-style chains; conclusions do not approximate the full variety of categorical syllogisms or natural argument forms.

### 8. Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models (BIG-bench)
- **Authors/year/venue:** Aarushi Srivastava et al., 2022, BIG-bench paper.
- **Links:** https://arxiv.org/abs/2206.04615 ; https://github.com/google/BIG-bench
- **What was verified:** BIG-bench is a collaborative suite of 200+ tasks, including `logical_deduction`, categorical/formal syllogism tasks, logical fallacy detection, and formal fallacies with negation. The task documentation defines categorical syllogism mood/figure and uses generated formal syllogisms with correct/incorrect deductions.
- **Benchmark value:** Broad LLM benchmark context and standardized zero/few-shot evaluation; its task family exposes logical deduction, formal fallacies, and syllogistic validity in one ecosystem.
- **Limitations:** Task-level scoring can conflate parse/format compliance with reasoning; some tasks are binary even when Unknown/indeterminate would be analytically useful.

### 9. FaiRR: Faithful and Robust Deductive Reasoning over Natural Language
- **Authors/year/venue:** Jinhyuk Lee et al., 2022, ACL.
- **Link:** https://aclanthology.org/2022.acl-long.77/
- **What was verified:** The paper introduces FaiRR, a modular faithful/robust reasoner over natural-language rule bases, with independently modeled components for reasoning and robustness.
- **Benchmark value:** Important bridge between benchmark accuracy and faithful deductive derivations; relevant to evaluating whether selected facts/rules actually support an answer.
- **Limitations:** Rule-based benchmark regime remains controlled and does not model categorical quantifier moods, belief bias, or cross-tradition argumentation.

### 10. Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning
- **Authors/year/venue:** Liangming Pan et al., 2023, Findings of EMNLP.
- **Link:** https://aclanthology.org/2023.findings-emnlp.248/
- **What was verified:** Logic-LM translates natural-language problems into symbolic form, executes a deterministic solver, and uses solver errors for self-refinement. It evaluates ProofWriter, PrOntoQA, FOLIO, LogicalDeduction, and AR-LSAT.
- **Benchmark value:** Establishes a common evaluation bundle for deductive benchmarks and makes the parser-vs-solver distinction measurable.
- **Novelty threat:** A project claiming that symbolic execution plus LLM formalization is itself a new benchmark methodology must distinguish its contribution from Logic-LM.

### 11. Hence, Socrates is mortal: A Benchmark for Natural Language Syllogistic Reasoning (SylloBase)
- **Authors/year/venue:** Yiran Li et al., 2023, Findings of ACL.
- **Link:** https://aclanthology.org/2023.findings-acl.148/
- **What was verified:** SylloBase uses template-generated syllogisms, GPT-3 paraphrases, and 1,000 manually rewritten test samples. Reported baselines include T5 generation and RoBERTa multiple-choice accuracy, with the best reported multi-choice accuracy of 72.77%.
- **Benchmark value:** Direct LLM/NLP benchmark for diverse natural-language categorical syllogistic reasoning; includes explicit paraphrase/naturalness stress rather than only symbolic strings.
- **Limitations:** GPT-3 paraphrasing and template origin can introduce artifacts; benchmark emphasis is answer prediction, not proof generation or premise-order invariance.

### 12. Evaluating Large Language Models with NeuBAROCO: Syllogistic Reasoning Ability and Human-like Biases
- **Authors/year/venue:** Kentaro Ozeki et al., 2023, NALOMA.
- **Link:** https://aclanthology.org/2023.naloma-1.1.pdf
- **What was verified:** NeuBAROCO is a syllogism dataset originally designed for psychological experiments; the paper evaluates LLM logical reasoning and human-like biases, including English/Japanese problems and cases where the relation is neither entailment nor contradiction.
- **Benchmark value:** Connects LLM evaluation to established cognitive syllogism experiments and tests bias patterns, not just aggregate accuracy.
- **Limitations:** Dataset provenance and translated/multilingual conditions need careful separation; human-bias resemblance is not evidence of valid deduction.

### 13. Exploring Reasoning Biases in Large Language Models Through Syllogism: Insights from the NeuBAROCO Dataset
- **Authors/year/venue:** Kentaro Ozeki et al., 2024, Findings/ACL-related publication.
- **Link:** https://arxiv.org/abs/2408.04403
- **What was verified:** The paper presents NeuBAROCO as English/Japanese syllogistic problems and reports that LLMs show reasoning biases similar to humans, plus additional error tendencies and difficulty on neither-entailment-nor-contradiction cases.
- **Benchmark value:** Follow-up evidence that evaluation should include content effects and indeterminate cases, not only valid/invalid classification.
- **Limitations:** Closely related to the 2023 NALOMA paper; treat them as distinct reports but not independent benchmark families.

### 14. A Systematic Comparison of Syllogistic Reasoning in Humans and Language Models
- **Authors/year/venue:** 2023 arXiv preprint.
- **Link:** https://arxiv.org/abs/2311.00445
- **What was verified:** The study compares PaLM 2 models and humans on syllogisms. It reports scaling-related improvements, but also sensitivity to irrelevant variable ordering and confident syllogistic fallacies.
- **Benchmark value:** Strong precedent for paired human/model evaluation and invariance tests. It supports measuring premise/term-order effects separately from accuracy.
- **Limitations:** Model family and prompt protocol are time-specific; human comparison does not establish that human error patterns are the desired target for an LLM benchmark.

### 15. Abductive Reasoning with Syllogistic Forms in Large Language Models
- **Authors/year/venue:** Hirohiko Abe et al., Springer/HAR 2024–2025 publication; arXiv record 2026.
- **Links:** https://arxiv.org/abs/2603.06428 ; https://github.com/kmineshima/abduction-syllogism-llm
- **What was verified:** The paper converts a syllogistic dataset into an abduction task and compares abductive and deductive judgments. The released data include English premises/hypotheses, gold abductive and deductive labels, syllogistic figure/form metadata, contradiction labels, and belief-consistency categories.
- **Benchmark value:** Important extension beyond entailment: tests whether a model distinguishes deductive validity from explanatory adequacy/abductive plausibility.
- **Limitations:** Abduction is not deduction; include it as an adjacent contrast rather than silently pooling its score with deductive benchmarks. Publication-year metadata differ between the Springer record and arXiv version and should be checked before final bibliography export.

## Cross-paper synthesis and novelty threats

1. **Accuracy-only novelty is weak.** SylloBase, NeuBAROCO, BIG-bench syllogism tasks, LogicNLI, FOLIO, RuleTaker, ProofWriter, and PrOntoQA already cover substantial answer-level evaluation.
2. **Controlled depth is already established.** RuleTaker/ProofWriter and PrOntoQA provide theorem-prover-backed synthetic theories with explicit depth, closed/open-world variants, and proof annotations.
3. **Naturalness is already addressed by multiple routes.** SylloBase paraphrases/template data and FOLIO uses human-authored natural language; a new benchmark needs a clear reason to add another paraphrase-only layer.
4. **Human-like bias tests are established.** Johnson-Laird/Bara, Oakhill et al., NeuBAROCO, and the PaLM 2 comparison establish figure, mood, believability/content, and premise/term-order effects as testable dimensions.
5. **Proof and formalization are separable targets.** ProofWriter evaluates proofs and implications; PrOntoQA parses chains into symbolic proofs; Logic-LM evaluates natural-language-to-symbolic translation plus solver execution; FOLIO supports NL-FOL translation. A new benchmark should report at least answer accuracy, derivation validity, and formalization/parsing failures separately.
6. **Indeterminate and inconsistency handling is a gap worth targeting.** Binary benchmarks can hide the distinction among contradiction, unknown, and parsing failure. ProofWriter OWA, NeuBAROCO neither-cases, and FOLIO’s formal annotations provide precedents for richer labels.
7. **Potentially differentiated contribution:** a cross-tradition benchmark that pairs categorical syllogisms with rule-based/FOL deduction, includes proof certificates and minimal-premise annotations, tests invariance under premise order and irrelevant-content substitutions, and reports answer validity, proof validity, robustness, and belief/content effects separately.

## Search failures and exclusions

- Google Scholar broad queries frequently surfaced author profiles, Scholar help/support pages, or irrelevant benchmark records rather than stable paper results. Scholar was retained as the first discovery route but not treated as sufficient verification.
- Direct extraction of Google Scholar URLs failed in the configured `web_extract` backend because it is search-only; the failure was bypassed with the web search/open route.
- The OpenReview PDF for **Evaluating LLMs on Syllogistic Reasoning: A Human–Model Accuracy Comparison under Premise Order Effects** redirected to an OpenReview browser-verification page. It was not counted among the 15 retained papers because the full paper could not be independently inspected through the available route.
- Some search results mixed multiple versions of NeuBAROCO and the Abe et al. abduction work. They were retained as distinct reports only when the opened records had distinct titles/contributions; the report warns where versions are closely related.
- Excluded generic reasoning papers that did not materially evaluate deductive/syllogistic tasks, including broad CoT surveys and general arithmetic benchmarks. Generic prompting papers may be useful for methods, but they are not benchmark/foundational-test papers for this subtopic.
- **Stopping rule:** stopped at 15 verified papers after covering (i) classical human syllogistic tests, (ii) direct natural-language syllogism benchmarks, (iii) synthetic theorem-prover-backed deduction, (iv) FOL/NLI benchmarks, (v) proof/solver evaluation, and (vi) bias/invariance and abductive contrasts.

## Source list

1. https://www.sciencedirect.com/science/article/abs/pii/0010027784900350
2. https://pubmed.ncbi.nlm.nih.gov/2721132/
3. https://www.ijcai.org/Proceedings/2020/537
4. https://aclanthology.org/2021.findings-acl.317.pdf
5. https://aclanthology.org/2021.emnlp-main.303/
6. https://arxiv.org/abs/2209.00840
7. https://arxiv.org/abs/2210.01240
8. https://arxiv.org/abs/2206.04615
9. https://aclanthology.org/2022.acl-long.77/
10. https://aclanthology.org/2023.findings-emnlp.248/
11. https://aclanthology.org/2023.findings-acl.148/
12. https://aclanthology.org/2023.naloma-1.1.pdf
13. https://arxiv.org/abs/2408.04403
14. https://arxiv.org/abs/2311.00445
15. https://arxiv.org/abs/2603.06428
