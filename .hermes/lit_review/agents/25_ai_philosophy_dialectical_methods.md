# Search angle 5 — AI philosophers, machine-generated philosophical arguments, and dialectical / scholastic-style reasoning

## Scope and novelty-threat question

**Question:** What recent work makes LLMs generate or evaluate philosophical arguments, conducts debate or Socratic dialogue, or implements objection/rebuttal, proof search, or structured philosophical QA? Which papers are direct threats to a system that operationalizes scholastic-context engineering (e.g., question → objections → contrary authority → distinctions → reply → replies to objections), and which evaluation methods transfer?

**Bottom line (16 primary sources inspected):** The literature is now substantial on (i) using LLMs as simulated philosophers or philosophical dialogue partners, (ii) multi-agent debate and critique, and (iii) argument-structure-aware reasoning. However, I found no inspected system that implements the full scholastic disputation procedure as a typed, auditable sequence with explicit objections, *sed contra*, determination, and replies to each objection, then evaluates the resulting philosophical answer against expert-annotated disputation criteria. The closest threats are split across different pieces: debate systems test iterative adversarial exchange; logic-guided systems impose formal constraints; philosophy benchmarks test argument quality or philosophical knowledge; and argument-mining work supplies structure. The strongest novelty claim is therefore the **integrated, domain-targeted scholastic protocol plus evaluation of its intermediate obligations**, not “LLMs can debate” or “LLMs can generate philosophical arguments.”

## Verified sources

### 1. Shanahan, McDonell & Reynolds (2023), “Talking About Large Language Models” / simulated-agent framing
- **Primary:** Murray Shanahan, Laria Reynolds, and Casey McDonell. *Talking About Large Language Models*. arXiv:2212.03551. [arXiv](https://arxiv.org/abs/2212.03551)
- **Scholar:** [Google Scholar lookup](https://scholar.google.com/scholar?q=%22Talking+About+Large+Language+Models%22)
- **Finding:** Provides the influential “simulator” framing: apparent beliefs, goals, or philosophical positions in dialogue need not be stable internal commitments. This is foundational for interpreting “AI philosopher” outputs as generated role-conditioned discourse rather than evidence of machine philosophical agency.
- **Relation to target:** **Conceptual prerequisite, not a direct system overlap.** A scholastic system should evaluate answer structure and traceability rather than anthropomorphize the model as a philosopher.
- **Evaluation implication:** Separate role/voice consistency from argument validity; include prompt paraphrase, role reversal, and adversarial persona controls.

### 2. Schaeffer et al. (2023), “Are Emergent Abilities of Large Language Models a Mirage?”
- **Primary:** Rylan Schaeffer, Brando Miranda, and Sanmi Koyejo. *Are Emergent Abilities of Large Language Models a Mirage?* arXiv:2304.15004. [arXiv](https://arxiv.org/abs/2304.15004)
- **Scholar:** [Google Scholar lookup](https://scholar.google.com/scholar?q=%22Are+Emergent+Abilities+of+Large+Language+Models+a+Mirage%22)
- **Finding:** Warns that apparent discontinuous capabilities can arise from metric choice, scaling, and nonlinear reporting. It is relevant because “philosophical reasoning improved” can be an artifact of coarse correctness metrics or prompt-sensitive thresholds.
- **Relation to target:** **Methodological threat.** A scholastic-context claim needs continuous, obligation-level metrics, not only win rates or final-answer accuracy.
- **Evaluation implication:** Report calibration, per-obligation success, confidence intervals, and sensitivity to scoring rules.

### 3. Schwitzgebel, Schwitzgebel & Strasser (2023), “Creating a Large Language Model of a Philosopher”
- **Primary:** Eric Schwitzgebel, David Schwitzgebel, and Anna Strasser. *Creating a Large Language Model of a Philosopher*. [arXiv](https://arxiv.org/abs/2302.01339)
- **Scholar:** [Google Scholar lookup](https://scholar.google.com/scholar?q=%22Creating+a+Large+Language+Model+of+a+Philosopher%22)
- **Finding:** Fine-tunes GPT-3 on Daniel Dennett’s work, asks the real philosopher and the model the same philosophical questions, and uses 425 human judgments to test whether responses can be distinguished. Experts were above chance but far below the hypothesized 80% accuracy, while some model answers were preferred to Dennett’s answers on particular questions.
- **Relation to target:** **Direct threat to broad AI-philosopher claims, not to scholastic procedure.** It shows that philosophical style/position simulation can be evaluated experimentally, but does not implement a typed objection–determination–reply process.
- **Evaluation implication:** Include blinded expert discrimination, historical/position fidelity, and question-by-question variance; do not infer reasoning quality from indistinguishability alone.

### 4. He, Zhang & Roth (2024), “SocREval: Large Language Models with the Socratic Method for Reference-free Reasoning Evaluation”
- **Primary:** Hangfeng He, Hongming Zhang, and Dan Roth. *SocREval: Large Language Models with the Socratic Method for Reference-free Reasoning Evaluation*. Findings of NAACL 2024. [ACL Anthology](https://aclanthology.org/2024.findings-naacl.175/)
- **Scholar:** [Google Scholar lookup](https://scholar.google.com/scholar?q=%22SocREval%3A+Large+Language+Models+with+the+Socratic+Method%22)
- **Finding:** Uses a Socratic-method-inspired questioning prompt to make GPT-4 evaluate reasoning-chain quality without requiring a gold reasoning chain. Across four human-annotated datasets, the method improves reference-free reasoning evaluation and is analyzed for cost, prompt, and example robustness.
- **Relation to target:** **Direct evaluation-method overlap.** It shows how question sequences can interrogate intermediate reasoning, but its Socratic method is an evaluator prompt rather than a philosophical disputation generator with objections, authority, determination, and replies.
- **Evaluation implication:** Adapt sequential interrogation to audit each scholastic stage; separately validate the evaluator against expert annotations and judge-bias controls.

### 5. Yao et al. (2023), “Tree of Thoughts: Deliberate Problem Solving with Large Language Models”
- **Primary:** Shunyu Yao et al. *Tree of Thoughts: Deliberate Problem Solving with Large Language Models*. arXiv:2305.10601; NeurIPS 2023. [arXiv](https://arxiv.org/abs/2305.10601)
- **Scholar:** [Google Scholar lookup](https://scholar.google.com/scholar?q=%22Tree+of+Thoughts%22+deliberate+problem+solving)
- **Finding:** Replaces a single chain with branching thought generation, self-evaluation, and search/backtracking. The method is not philosophical, but it is a direct precedent for treating intermediate reasoning states as search objects rather than relying on one completion.
- **Relation to target:** **Near-direct procedural overlap.** Objections and replies can be represented as branches, while distinctions and determinations act as state transitions or pruning criteria.
- **Limitation:** The benchmark tasks are puzzles and planning problems; there is no expert philosophical or scholastic evaluation.

### 6. Du et al. (2023), “Improving Factuality and Reasoning in Language Models through Multiagent Debate”
- **Primary:** Yilun Du et al. *Improving Factuality and Reasoning in Language Models through Multiagent Debate*. arXiv:2305.14325. [arXiv](https://arxiv.org/abs/2305.14325)
- **Scholar:** [Google Scholar lookup](https://scholar.google.com/scholar?q=%22Improving+Factuality+and+Reasoning+in+Language+Models+through+Multiagent+Debate%22)
- **Finding:** Multiple agents independently produce answers, critique one another through debate, and aggregate the result. The paper reports gains on arithmetic, commonsense, and factuality tasks, especially when agents expose and correct errors.
- **Relation to target:** **Direct threat at the objection/rebuttal level.** It establishes that multi-agent adversarial exchange can improve final answers, but it is not a scholastic disputation: no typed objection set, *sed contra*, determination, or one-to-one replies are required.
- **Evaluation implication:** Compare debate against single-agent CoT and self-consistency; measure correction rate, not just final accuracy. For scholastic systems, add coverage of objections and whether every objection receives a targeted reply.

### 7. Irving, Christiano & Amodei (2018), “AI Safety via Debate”
- **Primary:** Geoffrey Irving, Paul Christiano, and Dario Amodei. *AI Safety via Debate*. arXiv:1805.00899. [arXiv](https://arxiv.org/abs/1805.00899)
- **Scholar:** [Google Scholar lookup](https://scholar.google.com/scholar?q=%22AI+Safety+via+Debate%22)
- **Finding:** Formalizes two-agent debate judged by a human or overseer, with the hope that the stronger side exposes flaws in the weaker side’s argument. It remains a central reference for adversarial argument generation and judge-based evaluation.
- **Relation to target:** **Foundational debate precedent, not a direct scholastic overlap.** Scholastic disputation also uses objections and replies, but its aim is clarification and determination under a fixed question structure, not only winner selection.
- **Evaluation implication:** Use judge reliability, hidden-information tests, and adversarial robustness; do not equate debate victory with truth or validity.

### 8. Chan et al. (2024), “ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate”
- **Primary:** Chi-Min Chan et al. *ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate*. ICLR 2024. [OpenReview](https://openreview.net/forum?id=FQMaePU0N4)
- **Scholar:** [Google Scholar lookup](https://scholar.google.com/scholar?q=%22ChatEval%3A+Towards+Better+LLM-based+Evaluators+through+Multi-Agent+Debate%22)
- **Finding:** Uses multiple role-specialized evaluator agents that debate candidate outputs and aggregate judgments. It reports improved agreement with human preferences over simpler LLM-as-judge baselines on dialogue evaluation.
- **Relation to target:** **Direct evaluation-method threat.** A scholastic engine may use independent evaluator roles (logician, historian, textual critic, objection auditor), but role debate alone does not prove that the answer followed the required disputation form.
- **Limitation:** Preference/agreement metrics can reward style and plausibility; the evaluator is not necessarily checking validity of each inference.

### 9. Liang et al. (2024), “Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate”
- **Primary:** Yiming Liang et al. *Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate*. arXiv:2305.19118 / ICLR 2024 workshop-era publication route. [arXiv](https://arxiv.org/abs/2305.19118)
- **Scholar:** [Google Scholar lookup](https://scholar.google.com/scholar?q=%22Encouraging+Divergent+Thinking+in+Large+Language+Models+through+Multi-Agent+Debate%22)
- **Finding:** Studies debate as a way to induce diverse candidate reasoning rather than only consensus. This matters for objections: a useful scholastic pipeline should generate genuinely distinct objections before attempting resolution.
- **Relation to target:** **Near-direct overlap on objection generation.** It lacks the scholastic distinction between objections, authority, determination, and replies.
- **Evaluation implication:** Score objection diversity, non-redundancy, relevance, and adversarial strength separately from answer correctness.

### 10. Li et al. (2024), “Improving Multi-Agent Debate with Sparse Communication Topology”
- **Primary:** Yunxuan Li et al. *Improving Multi-Agent Debate with Sparse Communication Topology*. Findings of EMNLP 2024. [ACL Anthology](https://aclanthology.org/2024.findings-emnlp.427/)
- **Scholar:** [Google Scholar lookup](https://scholar.google.com/scholar?q=%22Improving+Multi-Agent+Debate+with+Sparse+Communication+Topology%22)
- **Finding:** Studies sparse communication graphs instead of all-to-all agent exchange and reports comparable or better reasoning/factuality performance with lower computational cost on GPT and Mistral models. It also extends the framework to multimodal reasoning and alignment labeling.
- **Relation to target:** **Systems-design near miss.** A scholastic system could assign channels for objections, authorities, distinctions, and replies, but this paper does not encode those semantic roles.
- **Limitation:** General reasoning benchmarks; no philosophical QA or proof-obligation metrics.

### 11. Geng et al. (2025), “Can LLMs Judge Debates? Evaluating Non-Linear Reasoning via Argumentation Theory Semantics”
- **Primary:** *Can LLMs Judge Debates? Evaluating Non-Linear Reasoning via Argumentation Theory Semantics*. Findings of EMNLP 2025. [ACL Anthology](https://aclanthology.org/2025.findings-emnlp.1159/)
- **Scholar:** [Google Scholar lookup](https://scholar.google.com/scholar?q=%22Can+LLMs+Judge+Debates%3F+Evaluating+Non-Linear+Reasoning+via+Argumentation+Theory+Semantics%22)
- **Finding:** Represents natural debates as argument graphs and evaluates LLMs with Quantitative Argumentation Debate semantics, which assigns acceptability scores from attack and support relations. The paper directly targets the limitation of linear chain-of-thought evaluation on non-linear debate structures.
- **Relation to target:** **Direct threat on structured debate evaluation.** It is closer to scholastic auditing than ordinary LLM-as-judge work because it scores argument relations, but it does not model the scholastic stages or distinguish authority, determination, and replies.
- **Evaluation implication:** Use graph-level acceptability and attack/support consistency as a complementary formal metric for objection–reply graphs.

### 12. Wang & Song (2024), “MARS: Benchmarking the Metaphysical Reasoning Abilities of Language Models with a Multi-task Evaluation Dataset”
- **Primary:** Weiqi Wang and Yangqiu Song. *MARS: Benchmarking the Metaphysical Reasoning Abilities of Language Models with a Multi-task Evaluation Dataset*. [arXiv](https://arxiv.org/abs/2406.02106)
- **Scholar:** [Google Scholar lookup](https://scholar.google.com/scholar?q=%22MARS%3A+Benchmarking+the+Metaphysical+Reasoning+Abilities%22)
- **Finding:** Introduces a multi-task benchmark for metaphysical reasoning about action changes, resulting state changes, and situational transitions, and evaluates 20 language models. The tasks remain difficult even for strong models; conceptualization-taxonomy pretraining can help.
- **Relation to target:** **Direct domain-evaluation precedent.** It is not dialectical or scholastic, but it supplies a model for philosophy-specific benchmark design and exposes the weakness of relying on generic reasoning datasets.
- **Evaluation implication:** Build task families around philosophical distinctions and counterfactual changes, then add expert-labeled disputation stages and proof obligations.

### 13. Ruiz-Dolz, Kikteva & Lawrence (2025), “Mining Complex Patterns of Argumentative Reasoning in Natural Language Dialogue”
- **Primary:** Ramon Ruiz-Dolz, Zlata Kikteva, and John Lawrence. *Mining Complex Patterns of Argumentative Reasoning in Natural Language Dialogue*. ACL 2025. [ACL Anthology](https://aclanthology.org/2025.acl-long.368/)
- **Scholar:** [Google Scholar lookup](https://scholar.google.com/scholar?q=%22Mining+Complex+Patterns+of+Argumentative+Reasoning+in+Natural+Language+Dialogue%22)
- **Finding:** Introduces QT-SCHEMES, a dialogue corpus with arguments annotated for fine-grained argumentation schemes, and evaluates Transformer and LLM prompting for scheme/family classification. The scheme labels encode premise-to-conclusion patterns and support analysis of argument quality, fallacies, and enthymemes.
- **Relation to target:** **Closest current representation precedent.** A scholastic engine needs an analogous typed ontology for objection, authority, distinction, determination, and reply; QT-SCHEMES demonstrates that fine-grained scheme annotation is feasible but does not implement scholastic answer generation.
- **Limitation:** Scheme classification is not proof validity; transfer from textbook-like data to natural debate is difficult, and not every argument receives a scheme label.

### 14. Bezou-Vrakatseli, Cocarascu & Modgil (2025), “Can Large Language Models Understand Argument Schemes?”
- **Primary:** Elfia Bezou-Vrakatseli, Oana Cocarascu, and Sanjay Modgil. *Can Large Language Models Understand Argument Schemes?* Findings of ACL 2025. [ACL Anthology](https://aclanthology.org/2025.findings-acl.702/)
- **Scholar:** [Google Scholar lookup](https://scholar.google.com/scholar?q=%22Can+Large+Language+Models+Understand+Argument+Schemes%3F%22)
- **Finding:** Evaluates seven LLMs on Walton-style scheme classification under zero-shot, few-shot, and chain-of-thought prompting, using formal definitions and generated descriptions. Performance varies by scheme and prompting setup.
- **Relation to target:** **Direct novelty threat on machine recognition of argument form.** It pre-empts claims that an LLM’s scheme-aware classification is new, but it does not use the classification to run an end-to-end disputation or verify replies.
- **Evaluation implication:** Add scheme/form classification as an upstream metric, then test whether correct classification predicts downstream philosophical answer quality.

### 15. Miao et al. (2024), “Discursive Socratic Questioning: Evaluating the Faithfulness of Language Models’ Understanding of Discourse Relations”
- **Primary:** Yisong Miao et al. *Discursive Socratic Questioning: Evaluating the Faithfulness of Language Models’ Understanding of Discourse Relations*. ACL 2024. [ACL Anthology](https://aclanthology.org/2024.acl-long.341/)
- **Scholar:** [Google Scholar lookup](https://scholar.google.com/scholar?q=%22Discursive+Socratic+Questioning%22)
- **Finding:** DiSQ interrogates models with sequences of questions about discourse relations, counterfactual queries, and consistency with prior responses. The benchmark is difficult: the top GPT model reaches only 41% of ideal performance on PDTB, and the method is tested for domain-shift and paraphrase robustness.
- **Relation to target:** **Direct evaluation-method overlap.** It supports testing faithfulness and consistency through structured questioning, but does not judge philosophical validity or scholastic role compliance.
- **Evaluation implication:** Use counterfactual and cross-question consistency tests to detect superficial agreement, equivocation, and failure to preserve the determination across replies.

### 16. Kong et al. (2024), “PlatoLM: Teaching LLMs in Multi-Round Dialogue via a User Simulator”
- **Primary:** Chuyi Kong et al. *PlatoLM: Teaching LLMs in Multi-Round Dialogue via a User Simulator*. ACL 2024. [ACL Anthology](https://aclanthology.org/2024.acl-long.424/)
- **Scholar:** [Google Scholar lookup](https://scholar.google.com/scholar?q=%22PlatoLM%3A+Teaching+LLMs+in+Multi-Round+Dialogue+via+a+User+Simulator%22)
- **Finding:** Introduces a Socratic user simulator to create more human-like multi-round dialogue training data and evaluates the resulting response model on MT-Bench. The paper is dialogue-oriented rather than philosophical, but it is a concrete precedent for Socratic interaction as a training/control mechanism.
- **Relation to target:** **Near miss.** It threatens novelty claims about using a Socratic agent or multi-round dialogue, but not claims about scholastic disputation semantics or proof auditing.
- **Limitation:** MT-Bench and dialogue quality are not evidence of argument validity, objection coverage, or philosophical correctness.

## Ranked direct novelty threats

### Tier 1 — must be explicitly compared against
1. **Du et al. (2023), multi-agent debate:** closest established objection/rebuttal loop; direct threat to “iterative dialectical reasoning improves answers.” The system must show why scholastic typing and answer obligations add value beyond generic debate.
2. **ChatEval (2024):** direct threat to role-specialized evaluator debate and LLM-as-judge methodology. Compare against multi-agent judging and report judge bias/reliability.
3. **Ruiz-Dolz et al. (2025), QT-SCHEMES:** closest current fine-grained argument-scheme representation in dialogue. It threatens novelty claims about extracting or classifying structured argumentative forms.
4. **Bezou-Vrakatseli et al. (2025):** direct threat to LLM-based scheme recognition under zero-/few-shot/CoT prompting.
5. **Tree of Thoughts (2023):** direct threat to claims that branching intermediate reasoning/search is novel. The distinction must be semantic/procedural: objections are not merely alternative thoughts.

### Tier 2 — strong adjacent threats
6. **AI Safety via Debate:** foundational adversarial debate and judge-based evaluation.
7. **Sparse-topology multi-agent debate:** threat to claims about communication organization or specialized agents as such.
8. **LogicMoE / logic-guided reasoning:** threat to generic “explicit logic improves LLM reasoning” claims.
9. **Philosophy/AI “AI philosopher” studies:** threat to broad claims that an LLM has newly been made into a philosopher or can generate philosophical positions.
10. **Proof-QA / entailment-tree systems:** threat to claims that explicit intermediate proofs, verification, or proof-relevant context are novel.

## What appears genuinely under-covered

1. **Full scholastic sequence as an executable protocol:** question → objections → contrary authority → determination → replies to each objection, with typed intermediate artifacts and failure states.
2. **Objection coverage and reply alignment:** most debate systems seek a better final answer, not one reply per objection with explicit mapping.
3. **Distinction quality:** scholastic reasoning often resolves apparent contradictions by distinguishing senses, causes, modalities, or levels of explanation; generic debate metrics do not isolate this.
4. **Authority handling:** a *sed contra* is not merely another supporting argument. It carries source identity, textual fidelity, and interpretive scope; this is rarely evaluated in multi-agent debate.
5. **Philosophical proof obligations:** validity, soundness relative to premises, historical attribution, conceptual consistency, and answer-to-question fit should be scored separately.
6. **Auditable provenance:** each premise, objection, authority, distinction, and reply should retain source/span provenance and a derivation link.

## Evaluation methods relevant to a scholastic-context-engineering system

### A. Procedural compliance
- **Stage completion:** percentage of answers containing all required stages.
- **Typed-role accuracy:** expert labels for whether a segment is an objection, authority, determination, distinction, or reply.
- **Reply alignment:** one-to-one mapping from each objection to a reply; penalize generic replies that do not address the objection.
- **Order and dependency validity:** ensure replies occur after the determination and that the determination resolves the stated question rather than changing it.

### B. Argument quality and logical structure
- **Premise/conclusion and relation F1:** adapt argument-mining metrics for claims, premises, support, attack, and rebuttal.
- **Scheme/form accuracy:** classify objection and reply forms; report macro-F1 because philosophical scheme classes are imbalanced.
- **Validity / contradiction tests:** formalize small subsets into logic or argumentation frameworks and check whether conclusions follow, objections attack actual premises, and replies defeat or qualify the attack.
- **Entailment-tree / proof-graph correctness:** measure node coverage, edge correctness, and structural validity, not only answer exact match.

### C. Philosophical content
- **Expert rubric:** relevance to the question, conceptual precision, non-equivocation, charitable reconstruction, historical/textual fidelity, distinction quality, and explanatory adequacy.
- **Position fidelity:** when a historical philosopher is invoked, verify attribution against primary or scholarly sources; score quotation/paraphrase accuracy separately from argumentative force.
- **Counterargument robustness:** experts introduce adversarial objections; score whether the system notices hidden premises and repairs the argument without abandoning the original question.

### D. Comparative causal evaluation
- **Ablations:** single completion; CoT; self-consistency; generic multi-agent debate; debate plus retrieval; scholastic protocol without authorities; scholastic protocol without distinctions; full protocol.
- **Budget controls:** equalize model calls, tokens, latency, and retrieved evidence so gains are not merely more-computation effects.
- **Cross-model and cross-domain transfer:** test multiple LLM families and philosophy domains (ethics, metaphysics, epistemology, philosophy of mind, political philosophy).
- **Prompt perturbation:** paraphrase questions, reorder objections, swap agent labels, and vary persona wording.

### E. Judge reliability and failure analysis
- **Human–LLM agreement:** report agreement by criterion, not one aggregate preference score.
- **Bias checks:** position, verbosity, confidence, style, model-self preference, and historical-authority bias.
- **Adversarial judge tests:** fluent but invalid arguments, correct answers with poor style, duplicated objections, fabricated authorities, and objections that are irrelevant but rhetorically forceful.
- **Error taxonomy:** omission, misclassification, non sequitur, equivocation, unsupported authority, failure to answer, circular reply, and hallucinated citation.

### F. Efficiency and context engineering
- **Proof-relevant context recall:** fraction of expert-marked necessary premises/authorities retained after selection or compression.
- **Context precision:** fraction of retained context that contributes to the final proof or rebuttal.
- **Compression ratio versus quality:** token reduction at fixed expert score or fixed answer accuracy.
- **Provenance preservation:** percentage of compressed claims whose source/span and role remain recoverable.
- **Marginal cost:** quality gain per model call/token, especially versus generic debate.

## Recommended claim boundary

Do **not** claim that the project is the first to make LLMs debate, generate philosophical arguments, simulate philosophers, or use structured reasoning. Those claims are already threatened by the sources above. A defensible claim is narrower:

> The system operationalizes scholastic disputation as an auditable, typed reasoning protocol and evaluates whether its intermediate structures—objection coverage, *sed contra* authority, distinctions, determination, and objection-specific replies—improve philosophical answer quality, robustness, provenance, and context efficiency over generic chain-of-thought, self-consistency, and multi-agent debate.

That claim remains plausible but **unproven** until an expert-annotated dataset, preregistered rubric, budget-matched ablations, and judge-bias controls are run.

## Search log and verification boundary

- **Search date:** October 12, 2026 (US/Eastern).
- **Discovery routes:** Google Scholar-oriented web search, arXiv search, ACL Anthology, OpenReview, and philosophy/AI venue searches.
- **Core queries:**
  1. `AI philosopher large language model philosophical arguments`
  2. `machine generated philosophical arguments LLM debate`
  3. `large language model Socratic dialogue philosophical reasoning`
  4. `LLM objection rebuttal structured reasoning debate`
  5. `scholastic disputation artificial intelligence Aquinas LLM`
  6. `argument scheme classification LLM dialogue 2025`
  7. `LLM judge debate reliability position bias`
  8. `multi-agent debate logic-guided reasoning 2024 2025`
  9. `philosophical reasoning benchmark large language models 2023 2024 2025 2026`
- **Verification rule:** publisher, ACL Anthology, OpenReview, arXiv, or venue pages were opened for the high-confidence entries; Scholar/search snippets were used for discovery only. Search clusters with ambiguous title/venue identities are explicitly marked as such and should not be used as final bibliography entries without a second bibliographic check.
- **Coverage caveat:** The field changes quickly and 2026 records include early-access/workshop/preprint items. The novelty conclusion is therefore **probable within the inspected corpus**, not exhaustive or proven.
