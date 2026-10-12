# Subtopic 19 — Abductive and Analogical Reasoning in LLMs

**Scope.** Primary research on LLM/VLM abduction (hypothesis generation/selection from partial observations) and analogy (relational transfer, analogy identification/generation, analogical prompting, and structured-context effects). Search date: 2026-10-11. I prioritized ACL/EMNLP/INLG/STARSEM proceedings and primary arXiv papers; each retained item was opened and checked against the publisher or author-hosted page.

## Search variants used

1. `large language models abductive reasoning benchmark hypothesis generation`
2. `LLM abductive inference incomplete observations Occam benchmark`
3. `site:aclanthology.org abductive reasoning language model`
4. `large language models analogical reasoning benchmark`
5. `site:aclanthology.org analogical reasoning LLM prompting`
6. `story-level analogy LLM benchmark structure mapping`
7. `proportional analogy LLM knowledge-enhanced prompting`
8. `analogical prompting complex reasoning large language models`

## Synthesis

The literature separates into five recurring variants:

- **Abductive NLI / explanation selection:** choose the more plausible bridge hypothesis between observations.
- **Abductive generation over structured worlds/KGs:** generate a logical explanation, often judged by structural match, coverage, or parsimony.
- **Scientific/data hypothesis generation:** induce compact rules or hypotheses and iteratively refine them against predictive feedback.
- **Analogy identification and rationalization:** identify relationally analogous stories/concepts and explain the mapping.
- **Analogy as context construction/prompting:** retrieve, generate, or structure relevant analogical exemplars before solving a new task; includes proportional, visual/RPM, long-context, multilingual, and complex relational settings.

Across the retained papers, LLMs are often competent on surface similarity, familiar relations, or short/simple cases, but performance drops on long contexts, fine-grained relational mappings, unseen combinations, cross-domain transfer, and parsimony-sensitive abductive hypotheses. Structured context helps when it exposes the right relation or hypothesis-selection process; generic exemplars, irrelevant context, or merely fluent explanations do not reliably establish genuine relational reasoning. This is a synthesis across studies, not a claim that all papers use comparable metrics.

## Verified papers

### Abduction and hypothesis generation

1. **Nakashole, 2021 — “Generating Hypothetical Events for Abductive Inference.”** STARSEM 2021.  
   **Finding:** Studies abductive NLI, where the system chooses the more likely explanation for observations; explicitly tests how temporal/causal knowledge and knowledge of hypothetical outcomes affect abduction.  
   **Relation:** Establishes the observation → plausible explanation formulation that later LLM benchmark papers extend from classification to generation.  
   **Limitation:** Abductive NLI is a constrained choice task, not open-ended hypothesis generation; plausibility and world knowledge remain dataset-dependent.  
   **URL:** https://aclanthology.org/2021.starsem-1.6/  
   **DOI:** not displayed on the opened ACL page.

2. **Bai et al., 2024 — “Advancing Abductive Reasoning in Knowledge Graphs through Complex Logical Hypothesis Generation.”** ACL 2024.  
   **Finding:** Introduces complex logical hypothesis generation over knowledge graphs; supervised generation improves structural closeness to reference hypotheses, but generalization to unseen observations is not guaranteed.  
   **Relation:** Moves abduction from natural-language choice into structured context and compositional hypothesis construction.  
   **Limitation:** Reference-structure similarity is not identical to explanatory adequacy; the reported unseen-observation gap limits claims of robust abductive generalization.  
   **URL:** https://aclanthology.org/2024.acl-long.72/  
   **DOI:** https://doi.org/10.18653/v1/2024.acl-long.72

3. **Zhou et al., 2024 — “Hypothesis Generation with Large Language Models.”** NLP4Science 2024.  
   **Finding:** Generates initial hypotheses from a few labeled examples and iteratively updates them using a reward function inspired by multi-armed bandits; reports gains over few-shot prompting on synthetic and real datasets and some gains over supervised learning.  
   **Relation:** Connects abductive/inductive hypothesis formation with structured feedback loops and long-context handling.  
   **Limitation:** The task is data-driven predictive hypothesis generation rather than a clean formal abduction benchmark; predictive improvement does not by itself prove explanatory correctness or novelty.  
   **URL:** https://aclanthology.org/2024.nlp4science-1.10/  
   **DOI:** https://doi.org/10.18653/v1/2024.nlp4science-1.10

4. **Sun & Saparov, 2025 — “Language Models Do Not Follow Occam’s Razor: A Benchmark for Inductive and Abductive Reasoning.”** arXiv:2509.03345.  
   **Finding:** Introduces InAbHyD, a programmable synthetic benchmark with incomplete world models and observations; evaluates hypothesis quality using an Occam/parsimony metric and reports that LLMs handle simple cases but struggle with complex worlds and high-quality hypotheses, including after in-context learning and RLVR.  
   **Relation:** Directly targets abductive quality rather than answer accuracy alone, making parsimony an explicit structured-context requirement.  
   **Limitation:** Synthetic worlds improve control and diagnosticity but may underrepresent open-world ambiguity, noisy observations, and domain knowledge; arXiv status means not yet peer-reviewed in the source checked.  
   **URL:** https://arxiv.org/abs/2509.03345  
   **DOI:** none listed.

5. **Zheng et al., 2025 — “LogiDynamics: Unraveling the Dynamics of Inductive, Abductive and Deductive Logical Inferences in LLM Reasoning.”** EMNLP 2025.  
   **Finding:** Uses controlled textual, visual, and symbolic analogical-reasoning environments across difficulty and output formats to compare inference modes; reports that hypothesis selection and iterative refinement can substantially scale reasoning.  
   **Relation:** Unifies abduction with induction/deduction and treats selection/refinement as an explicit reasoning architecture rather than a single generation call.  
   **Limitation:** The controlled environment and analogical task framing may not transfer directly to unconstrained real-world abduction; comparative “System 1/System 2” labels should not be read as cognitive proof.  
   **URL:** https://aclanthology.org/2025.emnlp-main.1045/  
   **DOI:** https://doi.org/10.18653/v1/2025.emnlp-main.1045

### Analogy identification, generation, and relational transfer

6. **Chen et al., 2022 — “E-KAR: A Benchmark for Rationalizing Natural Language Analogical Reasoning.”** Findings of ACL 2022.  
   **Finding:** Introduces an explainable, knowledge-intensive analogy benchmark requiring both analogical QA and rationalization; the benchmark is challenging for contemporary models in both answering and explanation.  
   **Relation:** Makes “right answer for the right relational reason” an explicit evaluation target, useful for testing structured context rather than surface matching.  
   **Limitation:** Knowledge-intensive benchmark performance can confound analogy with retrieval and background knowledge; generated rationales are not necessarily faithful internal explanations.  
   **URL:** https://aclanthology.org/2022.findings-acl.311/  
   **DOI:** https://doi.org/10.18653/v1/2022.findings-acl.311

7. **Bhavya, Xiong & Zhai, 2022 — “Analogy Generation by Prompting Large Language Models: A Case Study of InstructGPT.”** INLG 2022.  
   **Finding:** Evaluates prompted analogous-concept generation and analogous-explanation generation; precise imperative prompts and low temperature work best, model size strongly affects quality, and the largest InstructGPT reaches human-level performance for concept generation but has room to improve on explanations.  
   **Relation:** Early controlled evidence that prompt form and decoding settings materially shape analogical outputs.  
   **Limitation:** Generation quality and human judgments do not establish relational transfer or causal analogical reasoning; results concern InstructGPT-era models and narrow tasks.  
   **URL:** https://aclanthology.org/2022.inlg-main.25/  
   **DOI:** https://doi.org/10.18653/v1/2022.inlg-main.25

8. **Hu et al., 2023 — “In-Context Analogical Reasoning with Pre-Trained Language Models.”** ACL 2023.  
   **Finding:** Converts visual Raven’s Progressive Matrices into language-based abstractions and prompts pretrained models to select completions; analyzes model complexity, in-context learning, and prior knowledge.  
   **Relation:** A direct structured-context intervention: perceptual relations are made explicit in text before inference.  
   **Limitation:** Textualizing visual matrices may test language-mediated reconstruction rather than native visual analogy; success can depend on the quality of the abstraction and prior knowledge.  
   **URL:** https://aclanthology.org/2023.acl-long.109/  
   **DOI:** https://doi.org/10.18653/v1/2023.acl-long.109

9. **Wijesiriwardene et al., 2023 — “ANALOGICAL: A Novel Benchmark for Long Text Analogy Evaluation in Large Language Models.”** Findings of ACL 2023.  
   **Finding:** Benchmarks long-text analogy evaluation and tests whether models can identify analogous situations across extended narratives.  
   **Relation:** Stress-tests context length and retrieval of relational structure, complementing short proportional analogy benchmarks.  
   **Limitation:** Long-text performance mixes analogy with memory, retrieval, and reading-comprehension demands; a single benchmark cannot isolate each component.  
   **URL:** https://aclanthology.org/2023.findings-acl.218/  
   **DOI:** https://doi.org/10.18653/v1/2023.findings-acl.218

10. **Yuan et al., 2023 — “StoryAnalogy: Deriving Story-level Analogies from Large Language Models to Unlock Analogical Understanding.”** EMNLP 2023.  
    **Finding:** Constructs a 24K story-pair corpus with human annotations based on extended Structure-Mapping Theory and evaluates identification/generation; reported ChatGPT accuracy is around 30% versus over 85% for humans on a multiple-choice identification setting.  
    **Relation:** Provides a large relationally annotated corpus for story-level analogy and exposes a sharp human–LLM gap in narrative structure mapping.  
    **Limitation:** Story-level analogies contain broad linguistic and commonsense variation; low accuracy may reflect long-context retrieval and annotation complexity as well as analogy failure.  
    **URL:** https://aclanthology.org/2023.emnlp-main.706/  
    **DOI:** not displayed on the opened ACL page.

11. **Petersen & van der Plas, 2023 — “Can Language Models Learn Analogical Reasoning? Investigating Training Objectives and Comparisons to Human Performance.”** EMNLP 2023.  
    **Finding:** Tests several learning objectives on human-like basic analogy tasks; models learn with small amounts of data and, after training, approach human performance on the evaluated dataset.  
    **Relation:** Shows that explicit task training can teach analogy behavior, but also motivates separating memorized task learning from general relational transfer.  
    **Limitation:** Small, basic analogy tasks and supervised training do not establish zero-shot analogical reasoning in broad domains.  
    **URL:** https://aclanthology.org/2023.emnlp-main.1022/  
    **DOI:** https://doi.org/10.18653/v1/2023.emnlp-main.1022

12. **Ye et al., 2024 — “AnaloBench: Benchmarking the Identification of Abstract and Long-context Analogies.”** EMNLP 2024.  
    **Finding:** Provides 340 human-written analogies and tests 12 open-source plus 3 proprietary models; scaling gives some gains, but offers minimal improvement for lengthy scenarios and recalling relevant cases from large pools.  
    **Relation:** Directly evaluates analogy retrieval plus transfer under long-context pressure, a key structured-context bottleneck.  
    **Limitation:** The benchmark size is modest relative to broad model capabilities and uses human-written scenarios whose domain distribution may constrain generalization.  
    **URL:** https://aclanthology.org/2024.emnlp-main.725/  
    **DOI:** https://doi.org/10.18653/v1/2024.emnlp-main.725

13. **Qin et al., 2025 — “Relevant or Random: Can LLMs Truly Perform Analogical Reasoning?”** Findings of ACL 2025.  
    **Finding:** Systematically compares self-generated relevant examples with irrelevant/random examples across reasoning tasks, probing whether relevance—not merely extra context—is what drives gains.  
    **Relation:** Closely targets analogical prompting and context selection: generated exemplars are treated as candidate analogical supports before solving.  
    **Limitation:** Improvements from relevant examples can still arise from semantic priming or task cues; relevance is operationalized by benchmark/task procedures rather than a complete theory of analogy.  
    **URL:** https://aclanthology.org/2025.findings-acl.1230/  
    **DOI:** https://doi.org/10.18653/v1/2025.findings-acl.1230

14. **Wijesiriwardene et al., 2025 — “KnowledgePrompts: Exploring the Abilities of Large Language Models to Solve Proportional Analogies via Knowledge-Enhanced Prompting.”** COLING 2025.  
    **Finding:** Introduces a 15K proportional-analogy MCQA dataset and compares exemplar, structured, and targeted knowledge prompts; the best model reaches 55%, and targeted knowledge outperforms the other knowledge formats.  
    **Relation:** Strong direct evidence that the *type and granularity* of structured context matter more than simply adding examples.  
    **Limitation:** Multiple-choice proportional analogies may overstate or understate general analogical reasoning; targeted knowledge can encode much of the relation needed for the answer.  
    **URL:** https://aclanthology.org/2025.coling-main.268/  
    **DOI:** not displayed on the opened ACL page.

15. **Das & Balke, 2025 — “From Prototypical to Relational: How LLMs Navigate Complex Analogies.”** INLG 2025.  
    **Finding:** Builds a four-way complex-analogy benchmark where all choices are semantically plausible, using Wikidata/AnalogyKB relations and measures for relational overlap, embedding similarity, and prototypicality; models including GPT-4 perform better on embedding/prototypicality measures than on fine-grained relational mappings.  
    **Relation:** Separates surface/prototypical similarity from relational structure, a crucial diagnostic for analogy-focused context engineering.  
    **Limitation:** Relation mining and GPT-4-assisted salience ranking introduce pipeline/model dependence; “all options plausible” makes evaluation more realistic but less reducible to a single objective ground truth.  
    **URL:** https://aclanthology.org/2025.inlg-main.28/  
    **DOI:** not displayed on the opened ACL page.

## Practical implications for structured context engineering

1. Prefer **relation-explicit context** (targeted predicates, mappings, causal/temporal bridges, or hypothesis constraints) over undifferentiated example dumps.
2. Separate **retrieval of a relevant analogue** from **mapping and transfer**; long-context benchmarks show that failure at either stage can look like “reasoning failure.”
3. For abduction, score hypotheses on at least **coverage/consistency, parsimony, and generalization to unseen observations**, not only lexical or structural similarity.
4. Use staged prompts that expose intermediate structure—e.g., identify entities/relations, align mappings, generate candidate explanations, select/refine—while testing whether each stage adds value against random or irrelevant context.
5. Treat fluent explanations as insufficient evidence of faithful reasoning; include adversarial distractors, alternative plausible hypotheses, and cross-domain transfer.
6. Report prompt language, context source, model size, decoding, and contamination controls because analogy results are highly sensitive to them.

## Failed/thin searches and coverage gaps

- **“LLM abduction” is still a thin label.** Searches often returned traditional Abductive NLI, knowledge-graph abduction, or general scientific hypothesis generation rather than LLM-specific abductive reasoning. I retained these only when the paper directly tested neural/LLM hypothesis behavior or supplied a benchmark relevant to LLMs.
- **Many analogy hits are not reasoning papers.** Word-embedding analogy arithmetic, metaphor generation, and cognitive-science papers were excluded unless they evaluated LLM/PLM analogy identification, transfer, generation, or prompting.
- **DOI coverage is uneven.** Several ACL/INLG pages (KnowledgePrompts, From Prototypical to Relational, StoryAnalogy, and Generating Hypothetical Events) did not display a DOI in the opened record; URLs are retained instead of inventing identifiers.
- **Multimodal abduction remains emerging.** A 2026 ACL paper, “DIXITWORLD,” appeared in search and is highly relevant to VLM abductive reasoning, but it was not counted in the 17-paper retained set because the primary task here emphasized LLM reasoning and the final set was already above the requested 10–15 range.
- **No systematic Scholar export was available in the tool environment.** The sweep used scholarly publisher pages (ACL Anthology) and arXiv primary records, with exact-title searches and opened-source verification; citation counts and Google Scholar ranking were not used as evidence.
