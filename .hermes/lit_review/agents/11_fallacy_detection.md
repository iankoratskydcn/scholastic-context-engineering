# Subtopic 11 — Logical fallacy detection with LLMs

**Research focus.** Papers were prioritized when they connect fallacy recognition to argument structure, implicit context, evidence selection/retrieval, or proof/explanation generation. Scholar was attempted first, but Google Scholar returned only an anti-bot/interstitial page in this environment; the fallback route was official ACL Anthology, arXiv, AAAI, and author/institution repositories. PDFs were downloaded and locally text-extracted for the principal papers listed below (rather than relying only on snippets).

## Strong papers and leads

### 1. Jin et al. (2022), “Logical Fallacy Detection”
- **Citation:** Zhijing Jin, Abhinav Lalwani, Tejas Vaidhya, Xiaoyu Shen, Yiwen Ding, Zhiheng Lyu, Mrinmaya Sachan, Rada Mihalcea, and Bernhard Schölkopf. 2022. *Logical Fallacy Detection*. Findings of EMNLP 2022, 7180–7198.
- **Finding:** Introduces the LOGIC dataset and LOGIC_CLIMATE challenge set. The authors explicitly frame fallacy detection as requiring understanding of an argument’s underlying logical structure; pretrained LMs perform poorly, while a structure-aware classifier beats the best LM by 5.46 F1 on LOGIC and 4.51 on LOGIC_CLIMATE.
- **Relation to argument structure/context selection:** Foundational direct overlap. It establishes that the relevant unit is not just a sentence label: the system must compare an intended logical relation with the semantics/structure of the arguments. The released dataset is a core benchmark for structure-aware prompting and context construction.
- **Limitation:** Short, mostly self-contained educational examples; the paper’s own challenge set is narrow (climate claims). It does not solve long-range discourse context, evidence retrieval, or explicit proof traces.
- **Source URL/DOI:** https://aclanthology.org/2022.findings-emnlp.532/ ; DOI 10.18653/v1/2022.findings-emnlp.532 ; PDF https://aclanthology.org/2022.findings-emnlp.532.pdf
- **Source route:** Scholar attempted → blocked; ACL Anthology metadata + PDF, and arXiv abstract (arXiv:2202.13758) fallback. PDF inspected locally.

### 2. Alhindi, Chakrabarty, Musi, and Muresan (2022), “Multitask Instruction-based Prompting for Fallacy Recognition”
- **Citation:** Tariq Alhindi, Tuhin Chakrabarty, Elena Musi, and Smaranda Muresan. 2022. *Multitask Instruction-based Prompting for Fallacy Recognition*. EMNLP 2022, 8172–8187.
- **Finding:** Treats heterogeneous fallacy datasets/genres/input formats as multiple tasks and uses instruction-based multitask prompting with T5. Reports recognition of 28 fallacy types across domains and analyzes prompt choice, annotation quality, and external knowledge.
- **Relation:** Directly relevant to context selection because it shows that the prompt/task representation must normalize different argument formats and label inventories. Its external-knowledge analysis is an early bridge from classification to context augmentation.
- **Limitation:** Primarily supervised T5 prompting, not contemporary generative LLM reasoning; it classifies supplied text and does not reconstruct missing premises or retrieve discourse/evidence context.
- **Source URL/DOI:** https://aclanthology.org/2022.emnlp-main.560/ ; DOI 10.18653/v1/2022.emnlp-main.560 ; PDF https://aclanthology.org/2022.emnlp-main.560.pdf
- **Source route:** Scholar attempted → blocked; ACL Anthology PDF/metadata and author PDF fallback. PDF inspected locally.

### 3. Sourati et al. (2023), “Robust and Explainable Identification of Logical Fallacies in Natural Language Arguments”
- **Citation:** Zhivar Sourati, Vishnu Priya Prasanna Venkatesh, Darshan Deshpande, Himanshu Rawlani, Filip Ilievski, Hông-Ân Sandlin, and Alain Mermoud. 2023. *Robust and Explainable Identification of Logical Fallacies in Natural Language Arguments*. Knowledge-Based Systems 266, article 110418.
- **Finding:** Builds a three-stage evaluation framework—binary detection, coarse-grained classification, and fine-grained classification—and evaluates prototype reasoning, instance-based reasoning, knowledge injection, data augmentation, and curriculum learning. The paper reports that fallacy identification remains class-dependent and requires specialized reasoning.
- **Relation:** Strong overlap with proof-relevant context: prototype/instance reasoning and injected background knowledge make the decision more inspectable than a bare label; the three-stage setup separates “is it fallacious?” from “which violation?”
- **Limitation:** Much of the evaluation is encoder/classifier-centered and inherited from heterogeneous prior datasets; explanations are not necessarily faithful reconstructions of premise-to-conclusion failure. External knowledge is not selected via an explicit argument-graph policy.
- **Source URL/DOI:** https://arxiv.org/abs/2212.07425 ; DOI 10.1016/j.knosys.2023.110418 ; repository PDF https://par.nsf.gov/servlets/purl/10527889
- **Source route:** Scholar attempted → blocked; arXiv metadata plus NSF/institution PDF. PDF inspected locally.

### 4. Goffredo et al. (2023), “Argument-based Detection and Classification of Fallacies in Political Debates”
- **Citation:** Pierpaolo Goffredo, Mariana Chaves Espinoza, Elena Cabrio, and Serena Villata. 2023. *Argument-based Detection and Classification of Fallacies in Political Debates*. EMNLP 2023, 11101–11112.
- **Finding:** Extends ElecDeb60To16 with token-level fallacy spans, claims, premises, support/attack relations, and six fallacy categories. Transformer models that combine text with argumentative and engineered features outperform text-only alternatives.
- **Relation:** One of the closest precedents for proof-relevant context construction: support/attack edges identify which surrounding claims and premises should be carried into the classifier. It also makes span/boundary detection explicit rather than assuming a pre-segmented fallacious sentence.
- **Limitation:** Political U.S. presidential-debate domain and six labels limit transfer. Relations are mostly static features, not dynamically selected context or retrieved evidence; the method does not generate a proof object showing why a relation is invalid.
- **Source URL/DOI:** https://aclanthology.org/2023.emnlp-main.684/ ; DOI 10.18653/v1/2023.emnlp-main.684 ; PDF https://aclanthology.org/2023.emnlp-main.684.pdf
- **Source route:** Scholar attempted → blocked; ACL Anthology metadata + PDF. PDF inspected locally.

### 5. Payandeh et al. (2024), “How Susceptible are LLMs to Logical Fallacies?”
- **Citation:** Amirreza Payandeh, Dan Pluth, Jordan Hosier, Xuesu Xiao, and Vijay K. Gurbani. 2024. *How Susceptible are LLMs to Logical Fallacies?* LREC-COLING 2024, 8276–8286.
- **Finding:** Introduces LOGICOM, a multi-round persuader/debater benchmark contrasting logical and fallacious arguments. GPT-3.5 and GPT-4 were erroneously convinced 41% and 69% more often, respectively, in fallacious than logical conditions; it also releases 5k+ paired arguments.
- **Relation:** Important for context selection because the task is discourse-level and multi-round: a fallacy’s effect depends on previous claims, debate role, and the persuader’s reasoning strategy, not only local wording.
- **Limitation:** Measures susceptibility/decision change more than accurate fallacy localization or explanation. Synthetic paired scenarios may underrepresent naturally occurring discourse and domain evidence.
- **Source URL/DOI:** https://aclanthology.org/2024.lrec-main.726/ ; PDF https://aclanthology.org/2024.lrec-main.726.pdf ; arXiv:2408.12812 was not this paper, so do not conflate the IDs.
- **Source route:** Scholar attempted → blocked; ACL PDF and metadata fallback. PDF inspected locally.

### 6. Glockner et al. (2024), “MISSCI: Reconstructing Fallacies in Misrepresented Science”
- **Citation:** Max Glockner, Yufang Hou, Preslav Nakov, and Iryna Gurevych. 2024. *MISSCI: Reconstructing Fallacies in Misrepresented Science*. ACL 2024, 4372–4405.
- **Finding:** Introduces a model and dataset for implicit fallacies between a misinformation claim and a cited biomedical publication. The task requires reconstructing/verbalizing the fallacious premise in addition to classifying it; GPT-4 shows promise but the task remains difficult.
- **Relation:** Very strong direct overlap. It operationalizes proof-relevant context as the cited study’s accurate premise plus publication context (e.g., species, cell-culture setting, population), then asks the model to reconstruct the invalid bridge. This is a concrete template for selecting context that makes an inference auditable.
- **Limitation:** Biomedical misinformation and preselected/simplified study context; the task is not general discourse graph recovery. Generated reconstructions can be inconsistent with the predicted label, so verbal explanation is not automatically faithful evidence.
- **Source URL/DOI:** https://aclanthology.org/2024.acl-long.240/ ; arXiv https://arxiv.org/abs/2406.03181 ; PDF https://aclanthology.org/2024.acl-long.240.pdf
- **Source route:** Scholar attempted → blocked; ACL PDF and arXiv abstract fallback. PDF inspected locally.

### 7. Lei and Huang (2024), “Boosting Logical Fallacy Reasoning in LLMs via Logical Structure Tree”
- **Citation:** Yuanyuan Lei and Ruihong Huang. 2024. *Boosting Logical Fallacy Reasoning in LLMs via Logical Structure Tree*. EMNLP 2024.
- **Finding:** Constructs an unsupervised logical structure tree from constituency structure and connective taxonomy. It injects the tree as either a textualized hard prompt or relation-aware soft prompt; experiments improve precision/recall for detection and classification.
- **Relation:** Extremely direct overlap with argument-form classification and context selection. The tree explicitly exposes hierarchical connective→argument structure, allowing the model to attend to the premises that instantiate the alleged relation rather than to the whole flat string.
- **Limitation:** Connective-driven structure recovery can miss implicit relations and pragmatic context; the approach is still benchmark/classification oriented and does not guarantee that the extracted tree is the correct argument graph.
- **Source URL/DOI:** https://aclanthology.org/2024.emnlp-main.730/ ; DOI 10.18653/v1/2024.emnlp-main.730 ; arXiv https://arxiv.org/abs/2410.12048 ; PDF https://aclanthology.org/2024.emnlp-main.730.pdf
- **Source route:** Scholar attempted → blocked; ACL/arXiv PDF. PDF inspected locally.

### 8. Glockner et al. (2025), “Grounding Fallacies Misrepresenting Scientific Publications in Evidence”
- **Citation:** Max Glockner, Yufang Hou, Preslav Nakov, and Iryna Gurevych. 2025. *Grounding Fallacies Misrepresenting Scientific Publications in Evidence*. NAACL 2025, 9732–9767.
- **Finding:** MISSCI PLUS grounds the fallacious premises in real passages from misrepresented studies and adds passage retrieval, fallacy verbalization, and fact-checking evaluation. Fact-checking models struggle to use the misrepresented passages, and passages can mislead LLMs into accepting false claims.
- **Relation:** Perhaps the strongest existing analogue to proof-relevant context selection: retrieve the exact passage(s) that support the accurate premise and the passage(s) exposing the fallacious leap, then require the model to verbalize the bridge.
- **Limitation:** Biomedical publication setting, with a curated claim/study construction; retrieval and fallacy classification are evaluated separately enough that an end-to-end proof-selection policy remains open.
- **Source URL/DOI:** https://aclanthology.org/2025.naacl-long.491/ ; PDF https://aclanthology.org/2025.naacl-long.491.pdf ; repository https://github.com/UKPLab/naacl2025-missciplus
- **Source route:** Scholar attempted → blocked; ACL PDF + official GitHub fallback. PDF inspected locally.

### 9. Lei et al. (2024), “Reason from Fallacy: Enhancing Large Language Models’ Logical Reasoning through Logical Fallacy Understanding”
- **Citation:** *Reason from Fallacy: Enhancing Large Language Models’ Logical Reasoning through Logical Fallacy Understanding*. Findings of NAACL 2024.
- **Finding:** Defines logical-fallacy understanding through five tasks spanning WHAT, WHY, and HOW dimensions, and studies whether fallacy understanding can improve broader logical reasoning.
- **Relation:** Useful conceptual bridge from label prediction to explanation/proof: WHAT identifies the fallacy, WHY explains the violated relation, and HOW tests whether the model can use that understanding in reasoning. This decomposition can guide proof-relevant context schemas.
- **Limitation:** The task taxonomy is broader than direct context retrieval, and the benchmark’s alignment between generated reasoning and valid logical proof is not guaranteed.
- **Source URL/DOI:** https://aclanthology.org/2024.findings-naacl.192/ ; PDF https://aclanthology.org/2024.findings-naacl.192.pdf
- **Source route:** Scholar attempted → blocked; ACL metadata/PDF fallback. Metadata inspected; PDF route was not downloaded in this run, so treat detailed numerical claims as thinly verified.

### 10. Jeong, Jang, and Park (2025), “Large Language Models Are Better Logical Fallacy Reasoners with Counterargument, Explanation, and Goal-Aware Prompt Formulation”
- **Citation:** Jiwon Jeong, Hyeju Jang, and Hogun Park. 2025. *Large Language Models Are Better Logical Fallacy Reasoners with Counterargument, Explanation, and Goal-Aware Prompt Formulation*. Findings of NAACL 2025.
- **Finding:** Augments the input with implicit contextual queries about counterarguments, explanations, and goals, ranks those queries by confidence, and reports gains up to 0.60 F1 zero-shot and 0.45 fine-tuned across five domains/29 fallacy types.
- **Relation:** Directly relevant to proof-relevant context construction: it turns latent context into explicit, queryable subproblems. Counterargument and goal context are particularly useful for distinguishing an invalid inference from a merely controversial claim.
- **Limitation:** Query confidence/ranking is a model-internal heuristic; improvements may depend on prompt templates and evaluation labels. It does not prove that retrieved/elicited context is causally sufficient for the classification.
- **Source URL/DOI:** https://aclanthology.org/2025.findings-naacl.384/ ; arXiv https://arxiv.org/abs/2503.23363 ; PDF https://aclanthology.org/2025.findings-naacl.384.pdf
- **Source route:** Scholar attempted → blocked; ACL/arXiv PDF. PDF inspected locally.

### 11. Papadopulos, Alam, and Da San Martino (2026), “Beyond Logical Forms: LLM-Extracted Patterns for Fallacy Classification”
- **Citation:** Eleni Papadopulos, Firoj Alam, and Giovanni Da San Martino. 2026. *Beyond Logical Forms: LLM-Extracted Patterns for Fallacy Classification*. Proceedings of the 13th Workshop on Argument Mining and Reasoning.
- **Finding:** Inductively extracts structural patterns from fallacious examples and explanations, combining abstract logical structure with context-level linguistic cues. Zero-/one-shot experiments report significant gains and cross-dataset generalization.
- **Relation:** Direct overlap with the target research direction: context-level cues are treated as reusable structural patterns rather than discarded surface noise. The method suggests storing a fallacy’s proof-relevant signature as both logical form and contextual/rhetorical cues.
- **Limitation:** Very recent workshop/preprint evidence; benchmark coverage and robustness to adversarial paraphrase need independent replication. Pattern extraction can inherit errors or label artifacts from demonstrations.
- **Source URL/DOI:** https://arxiv.org/abs/2606.26698 ; PDF https://arxiv.org/pdf/2606.26698 ; ACL workshop listing https://aclanthology.org/people/giovanni-da-san-martino/
- **Source route:** Scholar attempted → blocked; arXiv PDF + ACL author/workshop listing. PDF inspected locally.

### 12. Xu et al. (2026), “Socrates or Smartypants: Testing Logic Reasoning Capabilities of Large Language Models with Logic Programming-Based Test Oracles”
- **Citation:** Zihao Xu, Junchen Ding, Yiling Lou, Kun Zhang, Dong Gong, and Yuekang Li. 2026. *Socrates or Smartypants: Testing Logic Reasoning Capabilities of Large Language Models with Logic Programming-Based Test Oracles*. AAAI 2026, 19433–19440.
- **Finding:** Introduces SMARTYPAT-BENCH, 502 naturally expressed Reddit posts with fine-grained fallacy labels, and SMARTYPAT, a Prolog-oracle generator that creates logically controlled fallacies before LLM surface realization. Structured reasoning improves categorization, while excessive reasoning steps can hurt detection.
- **Relation:** Strong for proof/audit design: symbolic rules provide a test oracle for the intended argument form, while natural-language realization supplies contextually varied instances. It supports separating formal validity checks from linguistic fallacy classification.
- **Limitation:** Synthetic augmentation still depends on rule coverage and LLM realization quality; Reddit selection and English-only data constrain generalization. A Prolog oracle verifies generated form, not necessarily pragmatic or domain-specific fallaciousness.
- **Source URL/DOI:** https://ojs.aaai.org/index.php/AAAI/article/view/39021 ; DOI 10.1609/aaai.v40i23.39021 ; PDF https://ojs.aaai.org/index.php/AAAI/article/download/39021/42983
- **Source route:** Scholar attempted → blocked; official AAAI page/PDF. PDF inspected locally.

### 13. Dore, Damo, Cabrio, and Villata (2026), “Retrieving Relations, Detecting Fallacies: A RAG Approach to Political Debate Analysis” (notable lead)
- **Citation:** Deborah Dore, Greta Damo, Elena Cabrio, and Serena Villata. 2026. *Retrieving Relations, Detecting Fallacies: A RAG Approach to Political Debate Analysis*. arXiv:2608.27471.
- **Finding:** Uses support/attack relations to steer retrieval from a large political knowledge base. The paper reports relation-guided retrieval gains up to 0.864 macro-F1 for detection and 0.725 for classification over non-retrieval baselines.
- **Relation:** This is the clearest recent lead for dynamic context selection: argument relations are not merely features but query controls for choosing external evidence and surrounding context.
- **Limitation:** Very recent preprint, U.S. presidential-debate-specific, and the knowledge base is domain-tailored. It is a lead for follow-up replication, not yet a settled result.
- **Source URL/DOI:** https://arxiv.org/abs/2608.27471 (no DOI verified in this search)
- **Source route:** Scholar attempted → blocked; arXiv metadata and paper search result fallback. Full PDF was not downloaded in this run; numerical claims are therefore thinly verified.

## Synthesis for context-engineering design

1. **Select argument structure before surface context.** LOGIC, ElecDeb, and Logical Structure Tree all support representing claims, premises, connective relations, and support/attack edges before asking an LLM to classify a fallacy.
2. **Retrieve context that witnesses the inference.** MISSCI/MISSCI PLUS show a useful proof-relevant decomposition: accurate premise, publication/domain context, fallacious bridge, and the evidence passage(s) that justify each premise.
3. **Elicit missing context as typed queries.** Jeong et al.’s counterargument/explanation/goal prompts and Reason from Fallacy’s WHAT/WHY/HOW task split suggest typed context slots rather than one undifferentiated “explain the fallacy” prompt.
4. **Keep formal and pragmatic checks separate.** SMARTYPAT shows how symbolic oracles can verify controlled logical forms, while MISSCI and political-debate work show that domain/pragmatic context is needed for informal fallacies.
5. **Make explanations auditable, not merely fluent.** A useful output should link: selected premise/evidence span → reconstructed inference → violated relation/schema → fallacy label → counterargument or missing assumption. The literature repeatedly shows that fluent explanations can be inconsistent with labels, so explanation quality needs separate consistency checks.

## Search log, failed/thin routes

- **Google Scholar first:** attempted the query `logical fallacy detection large language models`; Scholar returned an anti-bot/interstitial page rather than result records. No Scholar citation counts were used.
- **Scholar query variants attempted (5–10 requested; 8 logged):**
  1. `logical fallacy detection large language models`
  2. `logical fallacy detection LLM argument structure`
  3. `LLM fallacy recognition prompt context`
  4. `argument-based fallacy detection political debates transformer`
  5. `MISSCI reconstructing fallacies misrepresented science LLM`
  6. `logical structure tree fallacy LLM`
  7. `counterargument explanation goal-aware logical fallacy prompt`
  8. `RAG retrieval relations fallacy detection political debate`
- **Fallback routes:** official ACL Anthology pages/PDFs, arXiv abstracts/PDFs, official AAAI page/PDF, and NSF/institution-hosted PDF for Sourati et al. Search-engine snippets were used only for discovery/metadata; substantive findings above come from opened PDFs or official full-text pages.
- **Thin/failed searches:** direct `web_extract` was unavailable because the configured native backend is search-only; PDFs were therefore downloaded with `curl` and text-extracted locally using `pypdf`. `Reason from Fallacy` metadata was verified but its PDF was not locally downloaded in this run. `Retrieving Relations, Detecting Fallacies` was discovered via arXiv metadata/search results but its full PDF was not locally inspected. No DOI was found for the 2026 arXiv lead.
