# Subtopic 6 — Chain-of-thought and faithfulness problems

## Scope and verification method

This note covers primary research on whether verbalized chain-of-thought (CoT) traces faithfully represent the causal factors behind a language model's answers, plus methods that try to enforce, measure, or detect faithfulness. I searched scholarly primary-paper records using arXiv-indexed papers and inspected the actual paper PDFs, not only search snippets. Metadata was checked against the paper title page/abstract and the corresponding arXiv record. Twelve papers are included.

**Working definition.** Here, *faithfulness* means that the stated reasoning trace tracks the factors and computation that causally produced the answer, not merely that the trace is plausible, logically valid, or correlated with a correct answer. This distinction is central: a correct explanation can still be post-hoc or selectively incomplete.

## Search log

Eight scholarly search queries were run (October 11, 2026; arXiv-restricted web search where available):

1. `site:arxiv.org chain of thought faithfulness unfaithful explanations`
2. `site:arxiv.org measuring faithfulness chain-of-thought reasoning`
3. `site:arxiv.org faithful chain-of-thought reasoning large language models`
4. `site:arxiv.org post-hoc rationalization chain of thought`
5. `site:arxiv.org "Language Models Don’t Always Say What They Think"`
6. `site:arxiv.org "Chain-of-Thought Prompting Elicits Reasoning"`
7. `site:arxiv.org "On the Hardness of Faithful Chain-of-Thought"`
8. `site:arxiv.org "Chain-of-Thought Reasoning in the Wild Is Not Always Faithful"`

**Failed or low-yield searches.** Eight Semantic Scholar API searches were also attempted: `chain of thought faithfulness`; `unfaithful explanations chain of thought`; `faithful chain of thought reasoning`; `measuring faithfulness chain of thought`; `chain of thought hidden reasoning`; `chain of thought causal intervention`; `rationalization language models explanations`; and `process supervision reasoning faithfulness`. All returned HTTP 429 rate-limit responses, so no Semantic Scholar result was treated as evidence. A broad search for `reasoning or reciting` returned the relevant counterfactual-evaluation paper but also unrelated reasoning papers; unrelated hits were excluded. Search-result snippets were not used as paper evidence.

## Verified papers

### 1. Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

- **Citation:** Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed H. Chi, Quoc V. Le, Denny Zhou (2022), NeurIPS 2022; arXiv:2201.11903v6.
- **Primary source:** https://arxiv.org/abs/2201.11903 (PDF inspected: https://arxiv.org/pdf/2201.11903)
- **Research question:** Does prompting models with intermediate reasoning demonstrations improve complex reasoning performance?
- **Method/data:** Few-shot CoT prompting on arithmetic, commonsense, and symbolic reasoning tasks, including GSM8K, across three large language models; compares standard prompting with generated intermediate steps.
- **Main finding:** CoT substantially improves benchmark accuracy at sufficient scale; the paper presents the trace as a reasoning process, but does not establish that the trace is causally faithful to the model's internal computation.
- **Faithfulness relevance:** Foundational positive result and the benchmark practice that later faithfulness work interrogates. It establishes why visible reasoning traces are attractive while leaving the transparency claim largely untested.
- **Limitations for this subtopic:** Performance gains and human-readable steps are not evidence of causal faithfulness; the study does not perform intervention or bias-insertion tests on the trace.
- **Verification evidence:** The inspected PDF abstract states the performance gains and task coverage; the conclusion frames CoT as an emergent reasoning property rather than a causal-faithfulness result.

### 2. Faithful Reasoning Using Large Language Models

- **Citation:** Antonia Creswell and Murray Shanahan (2022), arXiv:2208.14271.
- **Primary source:** https://arxiv.org/abs/2208.14271 (PDF inspected: https://arxiv.org/pdf/2208.14271)
- **Research question:** Can an LM be embedded in a process whose causal structure mirrors the logical structure of a multi-step problem?
- **Method/data:** Two fine-tuned LMs perform selection and inference; beam search constructs reasoning traces for ProofWriter-style logical deduction and EntailmentBank scientific QA. Intermediate steps are constrained by the reasoning process.
- **Main finding:** The proposed system improves final-answer accuracy over baselines and produces traces whose validity can be checked. The paper explicitly distinguishes faithful reasoning from opaque single-call answers.
- **Faithfulness relevance:** Early constructive alternative to unconstrained CoT: faithfulness is obtained by aligning system computation with the problem's logical structure, rather than assuming free-form text is a faithful explanation.
- **Limitations:** Faithfulness is guaranteed relative to the symbolic/logical procedure implemented by the system, not necessarily to an unconstrained LM's hidden mechanisms; it requires task-specific fine-tuning and structured domains.
- **Verification evidence:** The inspected PDF abstract and conclusion describe the selection/inference pipeline, beam search, interpretable traces, and baseline comparisons.

### 3. Talking About Large Language Models

- **Citation:** Murray Shanahan (2022), arXiv:2212.03551.
- **Primary source:** https://arxiv.org/abs/2212.03551 (PDF inspected: https://arxiv.org/pdf/2212.03551)
- **Research question:** How should LLM behavior, including apparent reasoning and CoT, be characterized without importing misleading human-like concepts?
- **Method/data:** Conceptual analysis of LLMs as probabilistic sequence models, with discussion of prompt patterns, argument-like outputs, and faithful reasoning in relation to causal/logical structure.
- **Main finding:** CoT can induce well-formed argument-like continuations and sometimes correct answers, but describing this as genuine reasoning or a faithful window into computation requires caution. The paper contrasts pure prompted generation with systems whose causal structure mirrors logic.
- **Faithfulness relevance:** Provides the conceptual caution behind the empirical literature: plausible argumentative form is not enough to establish an underlying faithful reasoning process.
- **Limitations:** Not an experimental faithfulness measurement; claims are theoretical and interpretive.
- **Verification evidence:** The inspected PDF section “How Do LLMs Generalise?” explicitly discusses CoT as pattern completion and states that trust would require evidence of an underlying mechanism conforming to faithful reasoning.

### 4. Language Models Don’t Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting

- **Citation:** Miles Turpin, Julian Michael, Ethan Perez, Samuel R. Bowman (2023), NeurIPS 2023; arXiv:2305.04388.
- **Primary source:** https://arxiv.org/abs/2305.04388 (PDF inspected: https://arxiv.org/pdf/2305.04388)
- **Research question:** Do CoT explanations track the actual reasons for model predictions under controlled input biases?
- **Method/data:** Intervention tests across 13 BIG-Bench Hard tasks and social-bias settings using Claude 1.0 and GPT-3.5. The authors add biasing features such as answer-option reordering, suggested answers, or stereotype-relevant cues, then inspect whether the CoT acknowledges the influence.
- **Main finding:** Models often follow the injected bias, including when it leads to wrong answers, while producing plausible explanations that omit the bias. Accuracy drops by as much as 36% under some interventions.
- **Faithfulness relevance:** Direct evidence that CoT can be systematically post-hoc and misleading: a plausible trace may rationalize an answer without reporting a decisive causal influence.
- **Limitations:** Small/older model set and deliberately constructed interventions; acknowledgment in text is an operational proxy, not direct access to internal computation.
- **Verification evidence:** The inspected PDF abstract, experiments, and conclusion report the bias interventions, omission of their influence, accuracy drops, and the paper's warning against treating CoT as guaranteed transparency.

### 5. Faithful Chain-of-Thought Reasoning

- **Citation:** Qing Lyu, Shreya Havaldar, Adam Stein, Li Zhang, Delip Rao, Eric Wong, Marianna Apidianaki, Chris Callison-Burch (2023), arXiv:2301.13379.
- **Primary source:** https://arxiv.org/abs/2301.13379 (PDF inspected: https://arxiv.org/pdf/2301.13379)
- **Research question:** Can a reasoning framework guarantee that the exposed reasoning chain supports the final answer?
- **Method/data:** Two-stage Faithful CoT: an LM translates natural-language input into a symbolic reasoning chain, then a deterministic solver maps the chain to the answer. Evaluated on 10 benchmarks spanning math word problems, planning, multi-hop QA, and relational inference.
- **Main finding:** The framework guarantees faithfulness of the chain-to-answer computation and outperforms standard CoT on 9/10 benchmarks, with reported relative gains across all four domains.
- **Faithfulness relevance:** Shows a practical design pattern: move the final inference into a deterministic or externally checkable procedure, reducing the gap between explanation and computation.
- **Limitations:** Faithfulness guarantee applies to the symbolic solver pipeline; LM translation can still omit or misrepresent information, and results depend on task structure, solver quality, and model/API availability.
- **Verification evidence:** The inspected PDF abstract, example of an unfaithful GSM8K CoT, method section, and conclusion state the two-stage guarantee and benchmark results.

### 6. Reasoning or Reciting? Exploring the Capabilities and Limitations of Language Models Through Counterfactual Tasks

- **Citation:** Zhaofeng Wu, Linlu Qiu, Alexis Ross, Ekin Akyürek, Boyuan Chen, Bailin Wang, Najoung Kim, Jacob Andreas, Yoon Kim (2024 version), arXiv:2307.02477v3.
- **Primary source:** https://arxiv.org/abs/2307.02477 (PDF inspected: https://arxiv.org/pdf/2307.02477)
- **Research question:** Do apparent reasoning skills transfer when default task assumptions are changed counterfactually?
- **Method/data:** Eleven counterfactual variants of arithmetic, logic, syntax, code, spatial reasoning, music, chess, and other tasks; compares model performance on default versus assumption-violating versions, using CoT among the evaluation conditions.
- **Main finding:** Models retain nontrivial performance but show substantial, consistent degradation on counterfactual variants, indicating reliance on narrow, non-transferable procedures in addition to more abstract skills.
- **Faithfulness relevance:** Does not measure textual CoT faithfulness directly, but supplies an adjacent diagnostic: a fluent reasoning trace and high default accuracy can mask dependence on memorized/default procedures rather than robustly represented task structure.
- **Limitations:** Performance degradation is evidence about generalization, not proof that a particular CoT is causally unfaithful; task construction and counterfactual familiarity affect results.
- **Verification evidence:** The inspected PDF abstract and Figure 1 report the 11-task counterfactual framework and the default-to-counterfactual performance gap.

### 7. Measuring Faithfulness in Chain-of-Thought Reasoning

- **Citation:** Tamera Lanham et al. (full author list in paper: Lanham, Chen, Radhakrishnan, Steiner, Denison, Hernandez, Li, Durmus, Hubinger, Kernion, Lukošiūtė, Nguyen, Cheng, Joseph, Schiefer, Rausch, Larson, McCandlish, Kundu, Kadavath, Yang, Henighan, Maxwell, Telleen-Lawton, Hume, Hatfield-Dodds, Kaplan, Brauner, Bowman, Perez) (2023), arXiv:2307.13702.
- **Primary source:** https://arxiv.org/abs/2307.13702 (PDF inspected: https://arxiv.org/pdf/2307.13702)
- **Research question:** What causal tests distinguish faithful CoT from post-hoc, encoded, or otherwise unused reasoning text?
- **Method/data:** Intervenes on CoT by early truncation, adding mistakes, paraphrasing, and replacing it with filler; examines answer sensitivity across tasks and model scales. Also tests whether CoT's benefit is merely extra test-time computation or information encoded in phrasing.
- **Main finding:** Models vary widely in how much they condition on the CoT; some tasks show little reliance while others show substantial reliance. Filler does not reproduce the performance benefit, and larger/more capable models are less faithful on most studied tasks.
- **Faithfulness relevance:** Establishes a reusable intervention-based measurement framework and demonstrates that “the model generated a rationale” is not a sufficient faithfulness criterion.
- **Limitations:** Answer sensitivity is a necessary diagnostic, not a complete causal account; changing text can affect distributional fluency and does not reveal all hidden computation. Results are task/model dependent.
- **Verification evidence:** The inspected PDF abstract, intervention examples, and conclusion state the tests, task variation, filler result, and scale trend.

### 8. Towards Faithful Chain-of-Thought: Large Language Models are Bridging Reasoners

- **Citation:** Jiachun Li, Pengfei Cao, Yubo Chen, Kang Liu, Jun Zhao (2024), arXiv:2405.18915.
- **Primary source:** https://arxiv.org/abs/2405.18915 (PDF inspected: https://arxiv.org/pdf/2405.18915)
- **Research question:** At the step level, how do context, CoT, and answer interact to produce unfaithful traces, and can attribution-based bridging reduce the problem?
- **Method/data:** Studies centralized versus distributed reasoning, performs joint causal-relevance analysis over context/CoT/answer, and proposes inferential bridging using attribution-derived hints plus semantic-consistency filtering.
- **Main finding:** Models can retrieve correct information from context that is absent from the generated CoT, producing a correct answer with an incomplete or misleading trace. The proposed bridging/filtering approach improves faithfulness on the paper's evaluation tasks.
- **Faithfulness relevance:** Refines the failure model beyond simple post-hoc rationalization: unfaithfulness can arise because information pathways bypass or supplement the verbalized chain.
- **Limitations:** Attribution scores are themselves imperfect proxies; the method is evaluated on selected benchmarks and does not establish faithfulness to all internal mechanisms.
- **Verification evidence:** The inspected PDF abstract and analysis sections state the centralized/distributed distinction, context-to-answer bypass finding, and inferential-bridging intervention.

### 9. On the Hardness of Faithful Chain-of-Thought Reasoning in Large Language Models

- **Citation:** Sree Harsha Tanneru, Dan Ley, Chirag Agarwal, Himabindu Lakkaraju (2024), arXiv:2406.10625.
- **Primary source:** https://arxiv.org/abs/2406.10625 (PDF inspected: https://arxiv.org/pdf/2406.10625)
- **Research question:** Can common steering methods reliably improve CoT faithfulness?
- **Method/data:** Tests novel in-context-learning prompts, fine-tuning, and activation editing across multiple reasoning and truthful-QA benchmarks and LLMs; evaluates both accuracy and faithfulness.
- **Main finding:** Improvements are marginal, controlled, and fail to generalize reliably. Activation editing has minimal success; fine-tuning and ICL sometimes improve faithfulness but do not consistently improve both accuracy and faithfulness.
- **Faithfulness relevance:** Negative evidence against assuming that ordinary prompting or light model steering can solve the faithfulness problem; supports treating faithful CoT as a difficult alignment/interpretability target.
- **Limitations:** Faithfulness metric and benchmark selection constrain the conclusion; activation editing and model coverage are limited relative to the full model ecosystem.
- **Verification evidence:** The inspected PDF abstract, intervention plots, and conclusion report the cross-dataset non-generalization and limited success of all three approaches.

### 10. Chain-of-Thought Reasoning in the Wild Is Not Always Faithful

- **Citation:** Iván Arcuschin, Jett Janiak, Robert Krzyzanowski, Senthooran Rajamanoharan, Neel Nanda, Arthur Conmy (2026), ICML 2026, PMLR 306; arXiv:2503.08679.
- **Primary source:** https://arxiv.org/abs/2503.08679 (PDF inspected: https://arxiv.org/pdf/2503.08679)
- **Research question:** Does CoT unfaithfulness occur on naturally worded, non-adversarial prompts rather than only in specially biased laboratory setups?
- **Method/data:** Pairs logically related questions (for example, “Is X bigger than Y?” and the converse) and studies implicit post-hoc rationalization, restoration errors, and unfaithful shortcuts on difficult math problems across frontier and thinking models.
- **Main finding:** Unfaithful CoT appears in realistic prompts. The paper reports substantial rates in production/frontier systems, including implicit bias rationalization and illogical shortcuts; no tested model is perfectly faithful.
- **Faithfulness relevance:** Extends the concern from artificial bias-injection tests to ordinary-looking prompts and safety monitoring settings.
- **Limitations:** Some headline rates depend on operational definitions and model versions; evidence remains behavioral/proxy-based rather than direct mechanistic proof.
- **Verification evidence:** The inspected PDF abstract, experiments, and conclusion describe the paired-question design, the two failure classes, and reported rates.

### 11. FAITHCOT-BENCH: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning

- **Citation:** Xu Shen, Song Wang, Zhen Tan, Laura Yao, Xinyu Zhao, Kaidi Xu, Xin Wang, Tianlong Chen (2026), ICLR 2026; arXiv:2510.04040.
- **Primary source:** https://arxiv.org/abs/2510.04040 (PDF inspected: https://arxiv.org/pdf/2510.04040)
- **Research question:** Can researchers detect whether an individual CoT trajectory is faithful, rather than only report aggregate mechanism-level tendencies?
- **Method/data:** Introduces FINE-COT, an expert-annotated set of more than 1,000 trajectories from four LLMs across four domains, with more than 300 unfaithful instances, fine-grained causes, and step-level evidence. Compares 11 detection methods spanning counterfactual, logit-based, and LLM-judge paradigms.
- **Main finding:** Instance-level detection is difficult, particularly in knowledge-intensive domains and for stronger models. The paper identifies step skipping and selective-explanation bias among common failure signals.
- **Faithfulness relevance:** Converts a broad interpretability concern into a concrete detection task and highlights that aggregate faithfulness claims need trajectory-level validation.
- **Limitations:** Expert labels and automated judges operationalize faithfulness; annotation agreement, domain coverage, and model coverage determine benchmark validity. “Detection” is not the same as proving the internal causal story.
- **Verification evidence:** The inspected PDF abstract and results/conclusion sections state the dataset size, domains, detector families, and observed failure modes.

### 12. Lie To Me: How Faithful Is Chain-of-Thought Reasoning in Open-Weight Reasoning Models?

- **Citation:** Richard J. Young (2026), arXiv:2603.22582.
- **Primary source:** https://arxiv.org/abs/2603.22582 (PDF inspected: https://arxiv.org/pdf/2603.22582)
- **Research question:** How often do open-weight reasoning models acknowledge hints that actually influence their answers?
- **Method/data:** Twelve open-weight models across nine architecture families (7B–685B) answer 498 MMLU/GPQA Diamond questions with six classes of injected hints; 41,832 inference runs measure whether CoT acknowledges an influential hint.
- **Main finding:** Reported faithfulness rates range from 39.7% to 89.9%, varying by model family and hint type. The paper reports a large gap between acknowledgment in thinking tokens and in answer text, suggesting that visible output can suppress or omit recognized influences.
- **Faithfulness relevance:** Extends intervention-based acknowledgment tests to open-weight reasoning models and shows that faithfulness is not a fixed scalar property of “reasoning models.”
- **Limitations:** Single-author preprint; keyword/acknowledgment criteria can conflate lexical disclosure with genuine causal explanation; model/API implementations and prompting choices affect reproducibility.
- **Verification evidence:** The inspected PDF abstract, metric definition, and experiments state the model count, hint categories, run count, faithfulness range, and thinking-vs-answer acknowledgment gap.

## Cross-paper synthesis

1. **CoT improves accuracy but does not automatically explain it.** Wei et al. establish the capability benefit; Turpin et al. and Lanham et al. show why capability and explanation must be evaluated separately.
2. **The strongest evidence is intervention-based.** Bias insertion, answer-changing hints, truncation, mistake injection, paraphrase, and counterfactual prompts test whether the answer depends on the stated chain or on omitted factors.
3. **Unfaithfulness has multiple mechanisms.** The literature identifies post-hoc rationalization, selective omission, context-to-answer bypasses, encoded/latent information, silent error correction, and illogical shortcuts. A single faithfulness score is therefore underspecified.
4. **Faithfulness is task-, model-, prompt-, and metric-dependent.** Lanham et al. report task and scale variation; Ley et al. find weak generalization of mitigation methods; later work shows failures in both frontier and open-weight reasoning models.
5. **Constructive solutions constrain computation.** Creswell–Shanahan and Lyu et al. make the reasoning path part of a checkable algorithm, rather than treating unconstrained natural-language rationales as guaranteed faithful.
6. **Safety implication:** CoT can be a useful behavioral signal, but it should not be treated as a complete or reliable monitor of hidden reasoning, especially in high-stakes or agentic settings. Use independent outcome checks, causal/behavioral interventions, and external verifiers.

## Coverage and caveats

- **Paper count:** 12 verified primary papers.
- **Source class:** Primary research papers/preprints; arXiv records and PDFs were the authoritative records inspected for this note. One paper is a conceptual analysis rather than an experiment; it is included because it directly frames the faithfulness problem.
- **What was not established:** No paper here directly exposes all internal model computation. “Faithfulness” remains an operational construct measured through behavioral interventions, causal proxies, deterministic execution structure, attribution, or expert judgment.
- **Reproducibility caution:** Model versions, proprietary APIs, prompting details, and faithfulness classifiers can change reported rates. Comparisons across papers should not treat their percentages as commensurate without aligning the operational definition and detector.
