# Subtopic 1 — LLM hallucination surveys and taxonomies

**Research date:** 2026-10-11

**Scope.** Survey/taxonomy papers on hallucination in NLG, LLMs, and foundation models, with foundational work retained where it supplies the terminology or error structure needed by this project. Google Scholar was used as a discovery route where indexed results were available; metadata and findings were verified from publisher/ACL Anthology/arXiv landing pages and, where available, the linked PDF text. Search-result snippets were not used as sole evidence.

## Query variants used

1. `large language model hallucination survey taxonomy`
2. `hallucination survey natural language generation taxonomy`
3. `LLM hallucination definition detection mitigation survey`
4. `hallucination in large foundation models survey`
5. `factuality faithfulness hallucination abstractive summarization survey`
6. `hallucination taxonomy large language models ACM`
7. `hallucination audit NLP definitions survey`
8. `hallucination multimodal foundation models survey`
9. `logic definition hallucination NLG`
10. `hallucination mitigation techniques LLM survey`

## Retained papers (9)

### 1. Maynez et al. (2020)

**Citation.** Joshua Maynez, Shashi Narayan, Bernd Bohnet, and Ryan McDonald. 2020. “On Faithfulness and Factuality in Abstractive Summarization.” *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics (ACL 2020)*, 1906–1919. DOI: [10.18653/v1/2020.acl-main.173](https://doi.org/10.18653/v1/2020.acl-main.173). Paper/PDF: [ACL Anthology](https://aclanthology.org/2020.acl-main.173/), [PDF](https://aclanthology.org/2020.acl-main.173.pdf). Source route: Google Scholar query 5 → ACL Anthology metadata/PDF; cross-checked against the cited PDF and later taxonomy papers.

**Finding.** The paper separates factuality from faithfulness and shows that abstractive summaries can be fluent yet unsupported by the source. Its experiments and analysis motivate distinguishing source contradiction from unsupported additions rather than treating all factual errors as one class.

**Relation to project.** Supplies an early operational distinction between source-grounded correctness and general-world factuality; useful for classifying text spans by whether an argument is entailed by supplied premises, contradicted, or merely unsupported.

**Limitation addressed.** The project can address the paper’s task-specific scope by lifting its source/claim relation into a cross-tradition argument representation and by preserving the premise–conclusion skeleton instead of relying only on aggregate factuality scores.

---

### 2. Ji et al. (2023)

**Citation.** Ziwei Ji, Nayeon Lee, Rita Frieske, Tiezheng Yu, Dan Su, Yan Xu, Etsuko Ishii, Ye Jin Bang, Andrea Madotto, and Pascale Fung. 2023. “Survey of Hallucination in Natural Language Generation.” *ACM Computing Surveys* 55(12), 1–38. DOI: [10.1145/3571730](https://doi.org/10.1145/3571730). Paper/PDF route: [arXiv 2202.03629](https://arxiv.org/abs/2202.03629), [PDF](https://arxiv.org/pdf/2202.03629). Source route: Google Scholar query 2 → ACM DOI/arXiv landing page → PDF.

**Finding.** This broad survey organizes hallucination work across abstractive summarization, dialogue, generative QA, data-to-text, machine translation, visual-language generation, and LLMs, covering definitions, metrics, mitigation, and task-specific failure modes. It provides the field’s standard intrinsic/extrinsic distinction: output contradicts the source versus output is unsupported by the source.

**Relation to project.** The intrinsic/extrinsic split is a direct seed taxonomy for span-level labeling, while the task survey identifies why one universal hallucination detector is insufficient for heterogeneous argument forms.

**Limitation addressed.** The project adds a reasoning-centric layer missing from task-by-task inventories: identify claims, premises, warrants, and conclusion structure before judging support or contradiction.

---

### 3. Rawte et al. (2023)

**Citation.** Vipula Rawte, Swagata Chakraborty, Agnibh Pathak, Anubhav Sarkar, S. M. Towhidul Islam Tonmoy, Aman Chadha, Amit Sheth, and Amitava Das. 2023. “The Troubling Emergence of Hallucination in Large Language Models — An Extensive Definition, Quantification, and Prescriptive Remediations.” *Proceedings of EMNLP 2023*, 2541–2573. DOI: [10.18653/v1/2023.emnlp-main.155](https://doi.org/10.18653/v1/2023.emnlp-main.155). Paper/PDF: [ACL Anthology](https://aclanthology.org/2023.emnlp-main.155/), [PDF](https://aclanthology.org/2023.emnlp-main.155.pdf), [arXiv 2310.04988](https://arxiv.org/abs/2310.04988). Source route: Google Scholar query 1/3 → ACL Anthology metadata/PDF → arXiv abstract cross-check.

**Finding.** The paper argues that LLM hallucination needs more nuanced categorization and proposes two high-level orientations, “factual mirage” and “silver lining,” alongside definitions, quantification, and remediation discussion. Its central contribution is treating hallucination as a family of phenomena whose evaluation and mitigation depend on the type of mismatch.

**Relation to project.** Supports a taxonomy-first pipeline and cautions against collapsing unsupported, false, and useful-but-nonliteral generation into a single label.

**Limitation addressed.** The project can make the taxonomy more mechanically testable by mapping each span to explicit premises, inferential relation, and confidence/verification status rather than broad orientation labels.

---

### 4. Huang et al. (2024/2025 publication)

**Citation.** Lei Huang, Weijiang Yu, Weitao Ma, Weihong Zhong, Zhangyin Feng, Haotian Wang, Qianglong Chen, Weihua Peng, Xiaocheng Feng, Bing Qin, and Ting Liu. 2024 arXiv version; accepted/published as 2025. “A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions.” *ACM Transactions on Information Systems*. DOI: [10.1145/3703155](https://doi.org/10.1145/3703155). Paper/PDF route: [arXiv 2311.05232](https://arxiv.org/abs/2311.05232), [PDF](https://arxiv.org/pdf/2311.05232). Source route: Google Scholar query 1/6 → arXiv v2 landing page/PDF → DOI record.

**Finding.** The survey presents an LLM-specific taxonomy, then organizes causes, detection methods, benchmarks, mitigation, and limits of retrieval-augmented generation. The text explicitly frames hallucination as plausible but nonfactual content and highlights knowledge-boundary failures, long-tail knowledge, changing world knowledge, and the fact that retrieval does not automatically remove hallucination.

**Relation to project.** This is the closest general survey to the project’s goal: it connects hallucination to information support and knowledge boundaries, which can be represented as premise availability, entailment, contradiction, or unresolved status.

**Limitation addressed.** Its catalog remains primarily method- and benchmark-oriented; the project addresses cross-tradition argument form and compact context construction, making reasoning structure explicit before retrieval or verification.

---

### 5. Tonmoy et al. (2024)

**Citation.** S. M. Towhidul Islam Tonmoy, S. M. A. T. Zaman, Vikram Kumar, et al. 2024. “A Comprehensive Survey of Hallucination Mitigation Techniques in Large Language Models.” arXiv:2401.01313. [arXiv landing page](https://arxiv.org/abs/2401.01313), [PDF](https://arxiv.org/pdf/2401.01313). Source route: Google Scholar query 10 → arXiv record/PDF; author/record cross-check via DBLP search result.

**Finding.** The survey reviews more than 32 mitigation techniques and organizes them by dataset use, task, feedback mechanism, retriever type, and other intervention dimensions. It is especially useful for distinguishing pre-generation grounding, retrieval augmentation, decoding/control, and post-generation verification as different places where hallucination can be reduced.

**Relation to project.** Gives the project a mitigation vocabulary for evaluating whether compact, high-signal context reduces unsupported reasoning before generation rather than only detecting errors after generation.

**Limitation addressed.** Mitigation taxonomies do not by themselves explain the argument structure being protected; the project adds a deductive skeleton and span-level provenance so mitigation can target a specific premise, warrant, or conclusion.

---

### 6. Venkit et al. (2024)

**Citation.** Pranav Narayanan Venkit, Tatiana Chakravorti, Vipul Gupta, Heidi Biggs, Mukund Srinath, Koustava Goswami, Sarah Rajtmajer, and Shomir Wilson. 2024. “An Audit on the Perspectives and Challenges of Hallucinations in NLP.” *Proceedings of EMNLP 2024*, 6528–6548. DOI: [10.18653/v1/2024.emnlp-main.375](https://doi.org/10.18653/v1/2024.emnlp-main.375). Paper/PDF/data: [ACL Anthology](https://aclanthology.org/2024.emnlp-main.375/), [PDF](https://aclanthology.org/2024.emnlp-main.375.pdf). Source route: Google Scholar query 7 → ACL Anthology page/PDF.

**Finding.** The audit examines 103 peer-reviewed NLP publications and surveys 171 practitioners, finding substantial disagreement about what “hallucination” means and calling for explicit definitions and frameworks. This is evidence that taxonomy instability is not merely terminological: it affects how studies define, measure, and communicate the problem.

**Relation to project.** Strong justification for an explicit ontology and schema before classification; the project can make labels auditable by storing the textual evidence and argument relation behind each decision.

**Limitation addressed.** The audit reports field-level disagreement but does not supply a compact cross-tradition argument grammar; the project targets that missing intermediate representation.

---

### 7. Sahoo et al. (2024)

**Citation.** Pranab Sahoo, Prabhash Meharia, Akash Ghosh, Sriparna Saha, Vinija Jain, and Aman Chadha. 2024. “A Comprehensive Survey of Hallucination in Large Language, Image, Video and Audio Foundation Models.” *Findings of EMNLP 2024*, 11709–11724. DOI: [10.18653/v1/2024.findings-emnlp.685](https://doi.org/10.18653/v1/2024.findings-emnlp.685). Paper/PDF: [ACL Anthology](https://aclanthology.org/2024.findings-emnlp.685/), [PDF](https://aclanthology.org/2024.findings-emnlp.685.pdf). Source route: Google Scholar query 8 → ACL Anthology metadata/PDF.

**Finding.** This survey extends definition, taxonomy, detection, and mitigation beyond text to image, video, and audio foundation models, emphasizing that hallucination is a cross-modal reliability problem. Its framework is useful for separating modality-specific symptoms from general grounding failures.

**Relation to project.** The project is text-centered, but the paper supports a modality-neutral abstraction: a generated claim should be checked against the evidence channel and the intended task relation.

**Limitation addressed.** Multimodal breadth leaves less room for fine-grained textual inference; the project narrows to language spans and recovers the argument skeleton needed for high-signal textual context.

---

### 8. van Deemter (2024)

**Citation.** Kees van Deemter. 2024. “The Pitfalls of Defining Hallucination.” *Computational Linguistics* 50(2), 807–816. DOI: [10.1162/coli_a_00509](https://doi.org/10.1162/coli_a_00509). Paper/PDF: [MIT Press record](https://direct.mit.edu/coli/article/50/2/807/119144/The-Pitfalls-of-Defining-Hallucination), [ACL-hosted PDF](https://aclanthology.org/anthology-files/pdf/cl/2024.cl-2.10.pdf), [arXiv 2401.07897](https://arxiv.org/abs/2401.07897). Source route: Google Scholar query 9 → arXiv/MIT Press → PDF inspection.

**Finding.** The paper critiques coarse hallucination/omission classifications and proposes a logic-based synthesis using whether the input entails the output and whether the output entails the input, with further distinctions for contradiction, independence, tautology, and contradiction. It argues that even this synthesis has limits for ambiguity, pragmatics, and open-ended LLM tasks.

**Relation to project.** Directly aligned with the project’s deductive-skeleton objective: premise–conclusion entailment is a principled backbone for classifying additions, omissions, contradictions, and logical independence.

**Limitation addressed.** The paper focuses on logical relation but does not operationalize a scalable cross-tradition span classifier or context compressor; the project supplies the extraction and compact representation layer while retaining the logic distinctions.

---

### 9. Xu, Jain, and Kankanhalli (2024)

**Citation.** Ziwei Xu, Sanjay Jain, and Mohan Kankanhalli. 2024. “Hallucination Is Inevitable: An Innate Limitation of Large Language Models.” arXiv:2401.11817. [arXiv landing page](https://arxiv.org/abs/2401.11817), [PDF](https://arxiv.org/pdf/2401.11817). Source route: Google Scholar query 3 → arXiv paper page/PDF.

**Finding.** The paper frames hallucination as an inherent limitation rather than only an implementation defect, arguing from the mismatch between next-token generation and the requirement to know when a claim is unsupported. It motivates calibrated uncertainty and abstention instead of assuming that more scale alone eliminates fabrication.

**Relation to project.** Supports retaining an “unknown/insufficient support” state in the classifier rather than forcing every span into true/false or supported/contradicted.

**Limitation addressed.** The inevitability argument is high-level and not a complete taxonomy; the project turns the implication into an explicit span-level status plus a compressed evidence record suitable for downstream reasoning.

## Synthesis for the attached review

Across the retained literature, the stable design requirements are: (1) define hallucination relative to a source, world knowledge, or task intent; (2) distinguish contradiction from unsupported addition and omission; (3) preserve uncertainty/independence rather than forcing binary labels; (4) separate detection, mitigation, and evaluation; and (5) record enough evidence to make a classification auditable. The strongest bridge to this project is the combination of Ji et al.’s intrinsic/extrinsic distinction, van Deemter’s entailment-based logic, Huang et al.’s knowledge-boundary taxonomy, and Venkit et al.’s warning that definitions remain inconsistent.

## Failed or thin searches

- **Google Scholar direct access:** exact-title and broad Scholar queries were discoverable through web search, but Google Scholar result pages were not reliably fetchable in this environment (blocked/unstable). Therefore Scholar was used for discovery where indexed, while authoritative metadata and paper text were verified through ACL Anthology, ACM/DOI pages, MIT Press, arXiv, and linked PDFs.
- **Exact 2025/2026 survey filtering:** searches for only 2025–2026 surveys returned fewer directly inspectable, stable primary pages than 2023–2024 surveys; several results were duplicates, future-dated crawls, or broad multimodal surveys. The retained set therefore prioritizes stable primary papers through 2024 plus foundational 2020 work.
- **“Taxonomy” without “hallucination”:** this produced many factuality, attribution, uncertainty, and benchmark papers that were not surveys/taxonomies; they were excluded unless their main contribution was a reusable definition or classification framework.
- **Mitigation-only searches:** these produced method papers and benchmark papers rather than taxonomies. Tonmoy et al. was retained as the survey-level exception because its intervention taxonomy directly informs the project’s context-grounding objective.
