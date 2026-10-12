# Subtopic 17 — Cross-cultural / non-Western logic in AI and NLP

**Research status:** targeted scholarly sweep completed; 15 papers/sources retained. Sources were checked by opening the arXiv, ACL Anthology, IJCAI, IEEE/DOI, or project pages and recording the canonical URL and DOI where available. Search date: 2026-10-11.

## Scope and search variants

The query was interpreted broadly but operationally: work that evaluates or models reasoning, commonsense, values, pragmatics, or logical reading comprehension across languages/cultural groups, with special attention to Chinese, Arab, Indian, African, Iranian, Southeast Asian, and globally multilingual settings. “Non-Western logic” is not treated as a single homogeneous logic; most NLP papers operationalize culture through situated commonsense, values, exams, or pragmatic interpretation rather than formal alternative logics.

Search variants used:

1. `cross-cultural reasoning NLP dataset non-Western logic`
2. `non-Western logic artificial intelligence natural language processing`
3. `cultural values language models benchmark reasoning`
4. `Chinese reasoning logic dataset NLP`
5. `Arabic reasoning benchmark NLP culture`
6. `Indian logic artificial intelligence language model`
7. `multilingual commonsense reasoning cultural bias benchmark`
8. `cross-cultural argumentation mining NLP logic`
9. `Global MMLU cultural linguistic bias multilingual evaluation`
10. `Indian culture language-model benchmark reasoning`

## Retained literature

### A. Direct logical-reasoning and culturally situated examination data

1. **LogiQA: A Challenge Dataset for Machine Reading Comprehension with Logical Reasoning** — Liu et al. (IJCAI 2020). A logical-reasoning MRC benchmark built from Chinese civil-service examination questions. It is one of the clearest bridges between a non-Western institutional context and NLP reasoning evaluation, although the paper does not claim a distinct “Chinese logic.” Canonical sources: arXiv:2007.08124; IJCAI proceedings; DOI 10.5555/3491440.3491941. [1][2]

2. **LogiQA 2.0—An Improved Dataset for Logical Reasoning in Natural Language Understanding** — Liu et al. (IEEE/ACM TASLP, 2023). Reannotates and extends LogiQA, covering deductive, inductive, and abductive reasoning, with Chinese-origin examination material and English translation. It is useful for studying translation effects and whether reasoning performance survives movement from Chinese source contexts into English. DOI 10.1109/TASLP.2023.3293046. [3]

3. **Common Sense Beyond English: Evaluating and Improving Multilingual Language Models for Commonsense Reasoning** — Ponti et al. (ACL-IJCNLP 2021). Introduces the Mickey corpus (561k sentences across 11 languages) and evaluates multilingual models on commonsense reasoning beyond English. It treats linguistic coverage as necessary but shows that simple multilinguality is not equivalent to culturally balanced reasoning. DOI 10.18653/v1/2021.acl-long.102. [4]

4. **GeoMLAMA: Geo-Diverse Commonsense Probing on Multilingual Pre-Trained Language Models** — Yin et al. (EMNLP 2022). Probes region-specific relational knowledge in English, Chinese, Hindi, Persian, and Swahili, covering American, Chinese, Indian, Iranian, and Kenyan cultural concepts. The paper directly tests whether models encode geographically diverse commonsense and reports that language choice is not a reliable proxy for the culture being probed. DOI 10.18653/v1/2022.emnlp-main.132. [5]

### B. Cultural values, commonsense, and cross-cultural reasoning evaluation

5. **Cultural Bias and Cultural Alignment of Large Language Models** — Tao, Viberg, Baker, and Kizilcec (PNAS Nexus 2024). Compares outputs from five GPT models with nationally representative survey data and studies cultural bias/alignment across countries. This is a high-value empirical source for the claim that model “reasoning” can reflect culturally uneven value priors, though it evaluates value alignment more than formal logic. DOI 10.1093/pnasnexus/pgae346. [6]

6. **Understanding the Capabilities and Limitations of Large Language Models for Cultural Commonsense** — Shen et al. (arXiv 2024). Examines whether LLMs possess culturally grounded commonsense rather than only generic English commonsense. The work is directly relevant to cross-cultural inference and exposes a gap between conventional benchmark competence and culturally situated understanding. arXiv:2405.04655. [7]

7. **CDEval: A Benchmark for Measuring the Cultural Dimensions of Large Language Models** — Wang et al. (Workshop on Cross-Cultural Considerations in NLP 2024). Uses six cultural dimensions across seven domains, with automated generation followed by human verification, to evaluate cultural behavior in LLMs. It is broader than logic but relevant for measuring whether model decisions and explanations are culturally invariant or culturally misaligned. DOI 10.18653/v1/2024.c3nlp-1.1. [8]

8. **WorldValuesBench: A Large-Scale Benchmark Dataset for Multi-Cultural Value Awareness of Language Models** — Zhao et al. (LREC-COLING 2024). Constructs over 20 million demographic-context/value-question examples from World Values Survey data. It evaluates prediction of value responses conditioned on demographic context, offering a large-scale alternative to English-centered “universal values” tests. ACL canonical record: 2024.lrec-main.1539. [9]

9. **SeaEval for Multilingual Foundation Models: From Cross-Lingual Alignment to Cultural Reasoning** — Wang et al. (NAACL 2024). Benchmarks multilingual foundation models on standard NLP, reasoning, and cultural comprehension. The paper reports inconsistency across semantically equivalent multilingual prompts and unbalanced multilingual capability, making it especially useful for testing whether reasoning is stable across language/cultural realizations. DOI 10.18653/v1/2024.naacl-long.22. [10]

10. **LLM-GLOBE: A Benchmark Evaluating the Cultural Values Embedded in LLM Output** — Karinshak et al. (arXiv 2024). Uses the GLOBE cultural-psychology framework to evaluate cultural value systems embedded in model outputs. This is an important measurement paper for latent value structure, but it is not a formal logic benchmark. arXiv:2411.06032. [11]

11. **Global MMLU: Understanding and Addressing Cultural and Linguistic Biases in Multilingual Evaluation** — Singh et al. (ACL 2025; arXiv preprint 2024). Studies culturally sensitive subsets of MMLU, translation/annotation effects, and how rankings change when evaluation is made more culturally diverse. It supports the methodological point that translating a Western benchmark is insufficient for global reasoning evaluation. arXiv:2412.03304; ACL canonical record 2025.acl-long.919. [12]

12. **Can LLMs Grasp Implicit Cultural Values? Benchmarking LLMs’ Cultural Intelligence with CQ-Bench** — Liu et al. (arXiv/OpenReview 2025). Tests inference of implicit cultural values in conversational contexts, moving beyond explicit factual questions toward context-sensitive cross-cultural reasoning. It is one of the closest recent benchmarks to pragmatic, socially embedded reasoning. arXiv:2504.01127. [13]

13. **Commonsense Reasoning in Arab Culture** — Sadallah et al. (ACL 2025). Builds a native-speaker-written and validated Modern Standard Arabic dataset spanning 13 Arab countries, 12 daily-life domains, and 54 subtopics. Zero-shot evaluations show that models struggle across regional Arab cultures and vary by region; this is a direct non-Western cultural-reasoning benchmark rather than a machine-translated English test. DOI 10.18653/v1/2025.acl-long.380. [14]

14. **DRISHTIKON: A Multimodal Multilingual Benchmark for Testing Language Models’ Understanding on Indian Culture** — Maji et al. (EMNLP 2025; arXiv). Centers evaluation exclusively on Indian culture and uses multilingual/multimodal questions. It extends cultural reasoning beyond text-only language benchmarks, but its primary target is cultural understanding rather than formal logical validity. arXiv:2509.19274; ACL canonical record 2025.emnlp-main.68. [15]

15. **SANSKRITI: A Comprehensive Benchmark for Evaluating Language Models’ Knowledge of Indian Culture** — Maji et al. (2025). A benchmark for Indian cultural knowledge and context-sensitive model evaluation. It is adjacent to reasoning rather than a logic dataset, but useful for separating cultural knowledge, cultural inference, and formal reasoning in future taxonomy design. arXiv:2506.15355; DOI 10.48550/arXiv.2506.15355. [16]

## Synthesis for the taxonomy

- **Strongest direct precedent:** Chinese civil-service reasoning data (LogiQA/LogiQA 2.0) and geo-diverse commonsense probing (GeoMLAMA). These provide concrete reasoning tasks with non-Western or geographically differentiated source contexts. [1][3][5]
- **Current dominant framing:** “Cross-cultural logic” is usually operationalized as cultural commonsense, values, pragmatics, or multilingual consistency—not as competing formal systems of inference. [4][7][8][9][10][13][14]
- **Key methodological distinction:** language, culture, and reasoning are confounded in many datasets. A model can fail because of translation, low-resource language competence, missing cultural knowledge, unfamiliar social norms, or actual reasoning failure. Global MMLU, SeaEval, and GeoMLAMA are particularly useful for disentangling these effects. [5][10][12]
- **Taxonomy implication:** retain separate axes for (a) formal logical validity, (b) culturally situated commonsense, (c) value-conditioned judgment, (d) pragmatic/implicit-value inference, and (e) multilingual/translation robustness. Do not label all culturally different answers as different “logics.”

## Explicitly thin areas / negative findings

1. **Very little formal comparative work on non-Western logical systems in contemporary NLP.** The retained literature rarely implements or tests Buddhist, Jain, Nyaya, Islamic, African, Chinese classical, or other named traditions as formal inference systems. Most papers measure cultural knowledge or values instead.
2. **Chinese coverage is overrepresented relative to other traditions, but mainly through exam-derived datasets.** LogiQA provides strong task evidence, yet it should not be generalized from civil-service questions to “Chinese reasoning” as a whole. [1][3]
3. **Sparse coverage of African, Indigenous, Pacific, Central Asian, and Latin American reasoning traditions.** Swahili appears in GeoMLAMA, and global benchmarks include broader language coverage, but few studies build native-speaker, culturally authored logical-reasoning datasets for these regions. [5][12]
4. **Arabic work is emerging but recent and mostly commonsense/cultural rather than formal logic.** The Arab Culture benchmark is a notable correction to Anglocentric evaluation, but the area remains small. [14]
5. **India has rapidly growing cultural benchmarks, but formal reasoning and culturally grounded reasoning are still usually separated.** DRISHTIKON and SANSKRITI are valuable cultural-evaluation resources, not evidence for a unitary “Indic logic.” [15][16]
6. **Argumentation and discourse logic are underdeveloped cross-culturally.** The sweep found substantially more work on cultural values and commonsense than on culturally varied argument schemes, defeasible reasoning, rhetoric, fallacy interpretation, or debate norms.
7. **Dataset validity remains a bottleneck.** Machine translation, small annotator pools, demographic proxies, and LLM-generated items can turn cultural evaluation into an artifact of wording or annotation. Native-speaker authorship/validation and measurement invariance should be treated as acceptance criteria.
8. **Longitudinal and causal evidence is thin.** Most studies are static benchmarks; few establish whether culturally grounded training improves reasoning transfer, reduces bias without erasing local variation, or changes behavior in deployment.

## Bottom line

The literature supports a **cross-cultural reasoning/evaluation** subfield, but not yet a mature comparative science of “non-Western logic” in AI/NLP. The defensible taxonomy should distinguish formal logic from culturally situated reasoning and explicitly mark the latter as the better-supported research area. The strongest next-step research gap is native-authored, multilingual, culturally grounded benchmarks that include explicit reasoning traces or argument structures while controlling for translation and general language proficiency.

## Sources

[1] https://arxiv.org/abs/2007.08124
[2] https://doi.org/10.5555/3491440.3491941
[3] https://doi.org/10.1109/TASLP.2023.3293046
[4] https://aclanthology.org/2021.acl-long.102
[5] https://aclanthology.org/2022.emnlp-main.132
[6] https://arxiv.org/abs/2311.14096
[7] https://arxiv.org/abs/2405.04655
[8] https://aclanthology.org/2024.c3nlp-1.1
[9] https://aclanthology.org/2024.lrec-main.1539
[10] https://aclanthology.org/2024.naacl-long.22
[11] https://arxiv.org/abs/2411.06032
[12] https://arxiv.org/abs/2412.03304
[13] https://arxiv.org/abs/2504.01127
[14] https://aclanthology.org/2025.acl-long.380
[15] https://aclanthology.org/2025.emnlp-main.68
[16] https://arxiv.org/abs/2506.15355
