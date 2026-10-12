# Literature review agent 02 — hallucination in logical/deductive reasoning

**Research question.** What primary studies directly examine hallucination, false-premise acceptance, logical inconsistency, or error propagation in LLM logical/deductive reasoning, and what mechanisms/mitigations do they report?

**Scope rule.** Included papers had to test a logical, deductive, inference, premise-critique, negation, or reasoning-chain failure mode; broad hallucination surveys were excluded. Papers that study reasoning reliability without using the word *hallucination* are retained when their measured failure is a logically invalid or unsupported inference. This is a targeted subtopic review, not a claim of exhaustive coverage.

**Search date.** 2026-10-11 (US/Eastern).

## Search strategy

I used Scholar-style web queries and then opened the publisher/preprint landing page or paper PDF. Search variants used:

1. `logical reasoning hallucination large language models deductive`
2. `false premise hallucination LLM logical reasoning`
3. `LLM hallucination inference tasks NLI premise`
4. `LLM deductive reasoning robustness counterfactual noise`
5. `LLM reasoning error detection correction logical mistakes`
6. `premise critique ability large language models hallucination`
7. `negation hallucination false premise completion LLM`
8. `reasoning models hallucinate more intermediate reasoning`
9. `logical consistency hallucination detection symbolic reasoning`
10. `mathematical reasoning hallucination benchmark chain of thought`

**Selection outcome.** 11 verified primary studies. The set intentionally spans (a) direct hallucination/false-premise work, (b) logical error detection/correction, and (c) deductive robustness studies that expose hallucination-like unsupported deductions. Exact logical-form classification across categorical syllogism, modus ponens/tollens, abduction, analogy, qiyas, and Nyāya was not found in the targeted hallucination literature; that is a boundary, not a negative proof.

## Verified papers

### 1. Xu et al. (2023), “Are Large Language Models Really Good Logical Reasoners? A Comprehensive Evaluation and Beyond”

- **Authors / venue:** Fangzhi Xu, Qika Lin, Jiawei Han, Tianzhe Zhao, Jun Liu, Erik Cambria; arXiv preprint, 2023.
- **Stable page / PDF:** https://arxiv.org/abs/2306.09841 (landing page opened; PDF link verified on page).
- **Why included:** Directly evaluates logical reasoning and explicitly treats “No hallucination” as one of six dimensions of logical competence.
- **Task/data:** 15 logical-reasoning datasets organized into deductive, inductive, abductive, and mixed-form settings; seven LLMs.
- **Hallucination/logical finding:** The paper’s evaluation framework separates correctness, rigor, self-awareness, activity, orientation, and no-hallucination rather than treating a correct final label as sufficient evidence of sound reasoning.
- **Relevance to project:** Strong umbrella benchmark precedent for measuring hallucination alongside deductive/abductive reasoning; supports keeping unsupported intermediate claims distinct from final-answer accuracy.
- **Limitations / caution:** Abstract-level evidence does not establish that the paper extracts reusable proof-relevant spans or cross-tradition argument forms. “No hallucination” is a framework dimension, not necessarily a dedicated hallucination mechanism study.
- **Evidence inspected:** Actual arXiv abstract/landing page, including the 15-dataset design and six-dimension evaluation statement.

### 2. Yuan et al. (2024), “Whispers that Shake Foundations: Analyzing and Mitigating False Premise Hallucinations in Large Language Models”

- **Authors / venue:** Hongbang Yuan, Pengfei Cao, Zhuoran Jin, Yubo Chen, Daojian Zeng, Kang Liu, Jun Zhao; EMNLP 2024, pp. 2670–2683.
- **Stable page / PDF:** https://aclanthology.org/2024.emnlp-main.155/ ; linked PDF https://aclanthology.org/2024.emnlp-main.155.pdf.
- **Why included:** Directly names and studies false-premise hallucination.
- **Task/data:** False-premise questions; analysis of internal attention behavior and mitigation at inference time.
- **Hallucination/logical finding:** The authors define false-premise hallucination as generating hallucinated text when confronted with a false-premise question. They identify a small subset of “false premise heads” that disturb knowledge extraction and propose FAITH, which constrains those heads; the abstract reports nearly 20% performance improvement when approximately 1% of heads are constrained.
- **Relevance to project:** Closest direct precedent for a premise-validity gate before downstream inference/generation. It motivates explicit premise spans and contradiction/error labels in a deductive skeleton.
- **Limitations / caution:** The reported mechanism is attention-head intervention, not a general proof-structure or argument-scheme representation; false premises are primarily factual/QA prompts rather than a broad taxonomy of deductive forms.
- **Evidence inspected:** Full ACL Anthology landing page, bibliographic record, abstract, and linked PDF URL; not treated as a search-snippet citation.

### 3. Varshney et al. (2025), “Investigating and Addressing Hallucinations of LLMs in Tasks Involving Negation”

- **Authors / venue:** Neeraj Varshney, Satyam Raj, Venkatesh Mishra, Agneet Chatterjee, Amir Saeidi, Ritika Sarkar, Chitta Baral; TrustNLP 2025, pp. 580–598.
- **Stable page / PDF:** https://aclanthology.org/2025.trustnlp-main.37/ ; linked PDF https://aclanthology.org/2025.trustnlp-main.37.pdf.
- **Why included:** Negation is a core logical operator and the paper directly measures hallucination under negation.
- **Task/data:** Four tasks: false-premise completion, constrained fact generation, multiple-choice QA, and fact generation with negation; open-source models including LLaMA-2-chat, Vicuna, and Orca-2.
- **Hallucination/logical finding:** The paper reports considerable hallucination across all four negation-involving tasks and evaluates mitigation strategies. The authors frame negation as important for logical reasoning and inference.
- **Relevance to project:** Strong evidence that polarity/negation should be explicit in span labels and formal validation; a compressed context that drops negation markers can directly induce unsupported conclusions.
- **Limitations / caution:** Workshop paper and primarily factual-generation tasks; it does not test the full range of formal deduction systems or compare cross-tradition argument forms.
- **Evidence inspected:** Full ACL Anthology landing page, abstract, metadata, and linked PDF URL.

### 4. McKenna et al. (2023), “Sources of Hallucination by Large Language Models on Inference Tasks”

- **Authors / venue:** Nick McKenna, Tianyi Li, Liang Cheng, Mohammad Hosseini, Mark Johnson, Mark Steedman; Findings of EMNLP 2023.
- **Stable page / PDF:** https://aclanthology.org/2023.findings-emnlp.182/ ; linked PDF available from the page.
- **Why included:** Directly studies hallucination in natural-language inference, where the output is an entailment/contradiction/neutral judgment over premises and hypotheses.
- **Task/data:** Controlled NLI experiments across LLaMA, GPT-3.5, and PaLM families.
- **Hallucination/logical finding:** Models can label an NLI sample as entailed regardless of the premise when the hypothesis is attested in training data; entities can act as indices to memorized data. A second corpus-level predicate-frequency bias also predicts false entailment behavior.
- **Relevance to project:** Shows a concrete failure mode in which memorized or distributional cues override the local proof relation. This supports evaluating premise-conditioned entailment rather than surface answer accuracy.
- **Limitations / caution:** NLI is an inference proxy, not a complete proof calculus; the paper isolates pretraining biases more than long multi-step deductive-chain hallucination.
- **Evidence inspected:** Full ACL Anthology landing page and abstract text, including the controlled-experiment claims and two identified bias sources.

### 5. Hu et al. (2023), “Won’t Get Fooled Again: Answering Questions with False Premises”

- **Authors / venue:** Shengding Hu, Yifan Luo, Huadong Wang, Xingyi Cheng, Zhiyuan Liu, Maosong Sun; ACL 2023.
- **Stable page / PDF:** https://aclanthology.org/2023.acl-long.309/ ; linked PDF available from the page.
- **Why included:** Foundational false-premise benchmark and rebuttal study.
- **Task/data:** FalseQA, containing 2,365 human-written false-premise questions, explanations of the false premise, and revised true-premise questions.
- **Hallucination/logical finding:** PLMs are easily deceived by tricky questions, but the authors find that models can possess the knowledge needed to rebut them; fine-tuning on moderate data (e.g., 256 examples) improves discrimination.
- **Relevance to project:** Establishes the difference between knowledge availability and premise-validation behavior. A proof-relevant context layer should preserve the premise correction/rebuttal signal instead of forcing the model to answer inside an invalid premise.
- **Limitations / caution:** Focuses on QA and premise correction, not general logical derivation; results are tied to PLM-era models and supervised fine-tuning.
- **Evidence inspected:** Full ACL Anthology landing page and abstract/metadata, including FalseQA size and fine-tuning result.

### 6. Zhu et al. (2025), “KG-FPQ: Evaluating Factuality Hallucination in LLMs with Knowledge Graph-based False Premise Questions”

- **Authors / venue:** Yanxu Zhu, Jinlin Xiao, Yuhang Wang, Jitao Sang; COLING 2025.
- **Stable page / PDF:** https://aclanthology.org/2025.coling-main.698/ ; linked PDF available from the page.
- **Why included:** Scales false-premise hallucination evaluation using structured relational facts.
- **Task/data:** Automated KG-based pipeline that corrupts true triples into false premises, generates semantically rich questions, and builds KG-FPQ with approximately 178k questions across three domains, six confusability levels, and two task formats.
- **Hallucination/logical finding:** The paper treats being misled by a false premise as factuality hallucination and provides a scalable benchmark for measuring it.
- **Relevance to project:** Useful precedent for generating controlled perturbations of structured premises; the triple-corruption design can inspire span-level counterfactual/contradiction fixtures for syllogisms and rule chains.
- **Limitations / caution:** Knowledge-graph triples are narrower than natural-language arguments and do not directly evaluate multi-step proof validity or defeasible schemes.
- **Evidence inspected:** Full ACL Anthology landing page, abstract, metadata, and linked PDF URL.

### 7. Li et al. (2025), “Don’t Take the Premise for Granted: Evaluating the Premise Critique Ability of Large Language Models”

- **Authors / venue:** Jinzhe Li, Gengxu Li, Yi Chang, Yuan Wu; Findings of EMNLP 2025, pp. 836–869.
- **Stable page / PDF:** https://aclanthology.org/2025.findings-emnlp.44/ ; linked PDF available from the page.
- **Why included:** Directly evaluates whether models proactively detect flawed or contradictory premises before reasoning.
- **Task/data:** PCBench, with four error types across three difficulty levels; systematic evaluation of 15 representative LLMs.
- **Hallucination/logical finding:** Most models depend on explicit prompts to detect errors and have limited autonomous critique. Direct contradictions are easier than complex/procedural errors; reasoning ability does not consistently correlate with premise-critique ability; flawed premises cause reasoning models to overthink and lengthen responses.
- **Relevance to project:** Direct support for a separate premise-critique/validity stage before deductive expansion. It also warns that a stronger reasoning model is not automatically a better premise validator.
- **Limitations / caution:** The page abstract does not establish which formal logics dominate PCBench; “overthinking” is an efficiency/reliability symptom, not necessarily a hallucination taxonomy.
- **Evidence inspected:** Full ACL Anthology landing page and abstract/metadata, including the 15-model evaluation and four findings.

### 8. Peskov et al. (2025), “Investigating the Robustness of Deductive Reasoning with Large Language Models”

- **Authors / venue:** Peskov et al.; arXiv preprint, 2025 (paper page lists the full author record and links to the paper/code/data).
- **Stable page / PDF:** https://arxiv.org/abs/2502.04352.
- **Why included:** Directly stress-tests logical deduction under perturbations that can induce unsupported conclusions.
- **Task/data:** Informal and autoformalization deduction methods; seven LLMs; eight perturbed variants of a modular benchmark; perturbations include counterfactual statements and noise/logical distractions.
- **Hallucination/logical finding:** The paper reports a 12–13% average performance decrease from counterfactual statements for both informal reasoners and autoformalization methods; it also analyzes effects of noise and recovery mechanisms.
- **Relevance to project:** Strong precedent for adversarial perturbation tests and for treating counterfactual/irrelevant spans as distinct from proof-relevant context. It aligns with the need to preserve logical polarity and provenance during compression.
- **Limitations / caution:** The paper measures robustness/accuracy rather than naming every invalid derivation a hallucination; abstract/page evidence does not imply a cross-tradition span classifier.
- **Evidence inspected:** Full arXiv HTML/landing page with method dimensions, seven-model/eight-variant design, and reported counterfactual degradation.

### 9. Mi et al. (2026), “Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments”

- **Authors / venue:** Hao Mi, Qiang Sheng, Shaofei Wang, Beizhe Hu, Yifan Sun, Zhengjia Wang, Hengqi Zeng, Yang Li, Danding Wang, Juan Cao; ACL 2026, pp. 6311–6330.
- **Stable page / PDF:** https://aclanthology.org/2026.acl-long.286/ ; linked PDF available from the page.
- **Why included:** Directly makes logical consistency a component of hallucination detection.
- **Task/data:** LaaB (Logical Consistency-as-a-Bridge), coupling implicit neural uncertainty features with explicit symbolic/self-judgment signals through label-constraint modeling.
- **Hallucination/logical finding:** Existing detectors often isolate micro-level uncertainty or macro-level verbalized self-judgment; LaaB is proposed to bridge these coupled signals using logical consistency.
- **Relevance to project:** Closest direct precedent for using symbolic/logical constraints as a hallucination detector rather than only as a generation-time reasoning aid. It supports validating answer/context consistency after retrieval and generation.
- **Limitations / caution:** Logical consistency here is a detection signal, not necessarily a full formal proof checker or argument-form classifier. Results and benchmark details require PDF-level follow-up for exact metrics.
- **Evidence inspected:** Full ACL Anthology landing page, abstract, bibliographic record, and linked PDF URL.

### 10. Tyen et al. (2024), “LLMs Cannot Find Reasoning Errors, But Can Correct Them Given the Error Location”

- **Authors / venue:** Gladys Tyen, Hassan Mansoor, Victor Cărbune, Peter Chen, Tony Mak; Findings of ACL 2024, pp. 13894–13908.
- **Stable page / PDF:** https://arxiv.org/abs/2311.08516 ; ACL PDF https://aclanthology.org/anthology-files/pdf/findings/2024.findings-acl.826.pdf.
- **Why included:** Directly separates logical-error detection from correction in reasoning chains.
- **Task/data:** Five reasoning tasks; BIG-Bench Mistake dataset of LLM-generated logical mistakes; prompting and a small out-of-domain classifier for mistake localization.
- **Hallucination/logical finding:** State-of-the-art LLMs generally struggle to find simple, objective logical mistakes, while correction improves when the error location is supplied. A small classifier trained out of domain can outperform prompting a large model at mistake finding.
- **Relevance to project:** Strong evidence that a pipeline should not assume the generator can reliably critique its own deductive skeleton. It motivates explicit span-level error localization and separate verifier components.
- **Limitations / caution:** “Can correct when located” does not imply faithful internal reasoning; benchmark mistakes are intentionally unambiguous and may underrepresent philosophical/commonsense ambiguity.
- **Evidence inspected:** arXiv landing page plus the actual ACL PDF content returned for the paper, including abstract, dataset, five-task setup, and conclusion claims.

### 11. Li & Ng (2025), “Reasoning Models Hallucinate More: Factuality-Aware Reinforcement Learning for Large Reasoning Models”

- **Authors / venue:** Junyi Li, Hwee Tou Ng; NeurIPS 2025.
- **Stable page / PDF:** https://proceedings.neurips.cc/paper_files/paper/2025/file/ddd50f29fa472095515fa0df31749e6c-Paper-Conference.pdf ; preprint/code pointer https://arxiv.org/abs/2505.24630.
- **Why included:** Directly studies hallucination inside long reasoning traces, including mathematical reasoning.
- **Task/data:** Reasoning-oriented RL fine-tuning; experiments across mathematical-reasoning and hallucination benchmarks with Qwen2.5 and Llama models; FSPO (Factuality-aware Step-wise Policy Optimization).
- **Hallucination/logical finding:** The paper reports that outcome-based RL can increase hallucination, often from incorrect intermediate reasoning even when the final answer is occasionally correct. Its theoretical account identifies high-variance gradients, entropy-induced randomness, and spurious local optima; FSPO adds step-wise factuality verification to token-level advantages.
- **Relevance to project:** Directly supports evaluating intermediate proof steps, not only final entailment. It is a strong argument for retaining proof-relevant spans and attaching verification/provenance to every generated inference step.
- **Limitations / caution:** “Factuality” is broader than formal validity; automated evidence verification may not catch a formally invalid but factually plausible derivation. The paper is mainly mathematical/QA rather than cross-tradition logic.
- **Evidence inspected:** Actual NeurIPS PDF content returned from the publisher URL, including abstract/introduction and mechanism discussion; official code page used only as a secondary reproducibility pointer.

## Cross-paper synthesis

1. **Premise validity is an independent capability.** Hu, Yuan, Varshney, Zhu, and Li show that models can possess relevant knowledge yet still accept false, negated, contradictory, or procedurally flawed premises. Premise critique should therefore be represented as a separate stage/label, not inferred from general reasoning scores.
2. **Intermediate inference can hallucinate even when the answer is right.** Xu’s multidimensional evaluation, Tyen’s error-location study, and Li & Ng’s reasoning-RL results all undermine final-answer-only evaluation. The project should score each extracted/generated edge or proof step.
3. **Local structure and ordering matter.** Chen et al. (premise order) and Peskov et al. (counterfactual/noise robustness) show that logically equivalent or irrelevant context changes can materially alter accuracy. Proof-relevant context compression must preserve order/dependency information and test distractor insertion.
4. **Logical consistency can be used for detection.** Mi et al. provide a recent detector architecture that treats logical consistency as a bridge between internal uncertainty and explicit judgments. This is adjacent to, but not identical with, formal proof checking.
5. **Main gap relevant to the repository.** None of the verified papers was found to provide a single cross-tradition span-classification pipeline covering categorical syllogism, modus ponens/tollens, abduction, analogy, qiyas, Nyāya inference, and then constructing a compact proof-relevant context for downstream LLM generation. This remains an unproven novelty hypothesis, not an exhaustive negative claim.

## Failed / thin searches and boundary notes

- `hallucination categorical syllogism LLM` — thin. Results were mostly general logical-reasoning benchmarks or educational syllogism papers; no clearly verified primary paper directly measuring hallucination in categorical syllogism was retained.
- `modus ponens hallucination language model` — thin. Search surfaced premise-order and deductive-robustness work, but not a dedicated hallucination benchmark for modus ponens/tollens.
- `abductive reasoning hallucination LLM` — thin. Results were largely abduction capability/evaluation papers without an explicit hallucination analysis; excluded from this hallucination-focused set.
- `qiyas LLM hallucination` — no useful verified primary result in the targeted pass.
- `Nyaya inference hallucination LLM` — no useful verified primary result in the targeted pass.
- `analogy reasoning hallucination LLM` — thin; results did not isolate hallucination from general analogy accuracy.
- Broad searches for `LLM hallucination survey logical reasoning` — excluded surveys from the verified-paper count; the closest survey located was Liu et al., “Logical Reasoning in Large Language Models: A Survey” (arXiv:2502.09100), used only as a map, not as primary evidence.
- Search results for “Reasoning Models Hallucinate More” initially returned an OpenReview verification page; the publisher-hosted NeurIPS PDF was used instead.
- Some ACL landing pages expose the abstract and linked PDF but did not render the PDF body in the browser tool. Those papers are marked as landing-page + linked-PDF verified, and no paper-specific metric beyond the inspected abstract was invented.

## Evidence status

- **Verified paper count:** 11.
- **Evidence standard met:** every retained citation has an actual arXiv/ACL/publisher page opened; no retained claim relies only on a search-result snippet. For Tyen et al. and Li & Ng, publisher/preprint PDF text was also inspected.
- **Remaining uncertainty:** exact benchmark metrics, model-by-model tables, and detailed error taxonomies for several papers require a second PDF-reading pass if the parent review needs quantitative meta-analysis rather than a grounded map of mechanisms and gaps.
