# Subtopic 9 — Argument mining, argument components, and scheme classification

## Scope and novelty-threat question

**Question:** What prior work detects argument components, mines support/attack relations, classifies argumentation schemes or logical structure, and—most importantly—uses that representation for proof-relevant context selection, prompt/context compression, or LLM reasoning?

**Bottom line (verified through primary papers):** The argument-mining literature has mature representations for components (claims/premises), directed relations (support/attack/justification/refutation), and finer-grained argumentation schemes. I found **no inspected paper that combines all three of** (i) scheme/logical-form classification, (ii) proof-relevant context selection or compression, and (iii) LLM reasoning in one system. The closest overlaps are split across neighboring lines: scheme classification/reconstruction; retrieval plus contrastive arguments for fact verification; and proof-tree fact filtering for entailment QA. This leaves a plausible novelty space for a system that classifies argument form/scheme and uses the resulting deductive skeleton to select or compress context for proof-oriented LLM reasoning.

## Verified papers

### 1. Feng & Hirst (2011), “Classifying Arguments by Scheme”
- **Primary:** Vanessa Wei Feng and Graeme Hirst. *Classifying Arguments by Scheme*. ACL-IJCNLP 2011, pp. 987–996. [ACL PDF](https://aclanthology.org/P11-1099.pdf)
- **Scholar:** [Google Scholar lookup](https://scholar.google.com/scholar?q=%22Classifying+Arguments+by+Scheme%22+Feng+Hirst)
- **Finding / exact evidence:** Given arguments with premises and conclusions identified, the paper classifies five common schemes using scheme-specific features; reported accuracies are 63–91% one-against-others and 80–94% pairwise. It explicitly motivates scheme classification as a route to reconstructing implicit premises (“enthymemes”): first classify the scheme, then fit stated propositions to its template and infer missing propositions.
- **Relation to target:** **Near-direct conceptual overlap** on underlying argument form and proof-relevant missing-premise reconstruction. It supplies the representation (scheme template) but does not retrieve/select context, compress prompts, or use an LLM.
- **Limitation:** Small Araucaria-derived corpus; five schemes only; assumes argument/premise/conclusion detection upstream; the authors note low annotator agreement and corpus-size limitations.

### 2. Lawrence & Reed (2016), “Argument Mining Using Argumentation Scheme Structures”
- **Primary:** John Lawrence and Chris Reed. *Argument Mining Using Argumentation Scheme Structures*. COMMA 2016, pp. 379–390. [Primary PDF](https://www.arg.tech/people/chris/publications/2016/comma2016-schememining.pdf)
- **Scholar:** [Google Scholar lookup](https://scholar.google.com/scholar?q=%22Argument+Mining+Using+Argumentation+Scheme+Structures%22)
- **Finding / exact evidence:** Scheme structure is used to classify proposition types and assign their roles, even from segmented text without prior argumentative structure. Reported component F-scores are 0.78–0.91; the paper states this can identify not only that a scheme occurs but also the roles of its component parts.
- **Relation to target:** **Closest pre-LLM representation overlap** for component detection + scheme structure. The output is structurally useful for deductive skeleton extraction, but no context selection/compression or downstream proof task is evaluated.
- **Limitation:** Restricted scheme set and corpus; noisy/partially unanalysed text; performance is component-role recognition rather than validated proof construction or retrieval utility.

### 3. Stab & Gurevych (2017), “Parsing Argumentation Structures in Persuasive Essays”
- **Primary:** Christian Stab and Iryna Gurevych. *Parsing Argumentation Structures in Persuasive Essays*. Computational Linguistics 43(3), 2017, pp. 619–659. DOI: 10.1162/COLI_a_00295. [ACL page](https://aclanthology.org/J17-3005/)
- **Scholar:** [Google Scholar lookup](https://scholar.google.com/scholar?q=%22Parsing+Argumentation+Structures+in+Persuasive+Essays%22)
- **Finding / exact evidence:** Jointly identifies token-level argument components and directed relations with Integer Linear Programming, globally optimizing component types and relations. The paper defines claims/premises and relations as justifications or refutations, and reports gains over heuristic baselines on two discourse types.
- **Relation to target:** **Core relation-mining precedent.** Its globally coherent graph is a natural deductive-skeleton substrate and is closer than local span classification to proof-relevant selection. It predates LLM context selection and does not classify Walton-style schemes.
- **Limitation:** Persuasive-essay domains; graph labels are mainly claim/premise plus support/attack, not fine-grained inference forms; global optimization is not a proof-validity guarantee.

### 4. Lawrence & Reed (2020), “Argument Mining: A Survey”
- **Primary survey:** John Lawrence and Chris Reed. *Argument Mining: A Survey*. Computational Linguistics 45(4), 2019/2020 issue, pp. 765–818. DOI: 10.1162/coli_a_00364. [ACL page](https://aclanthology.org/J19-4006/)
- **Scholar:** [Google Scholar lookup](https://scholar.google.com/scholar?q=%22Argument+Mining%3A+A+Survey%22+Lawrence+Reed)
- **Finding / exact evidence:** Defines argument mining as identifying and extracting inference/reasoning structure; reviews argument/non-argument detection, component identification, relation mining, scheme analysis, datasets, and applications such as retrieval and decision support.
- **Relation to target:** **Landscape anchor, not a novelty overlap.** It confirms that component/relation extraction and scheme-level analysis are established lines, but does not provide a unified context-selection/compression method.
- **Limitation:** Survey rather than a new evaluated system; pre-dates the current LLM/RAG wave and therefore cannot establish novelty against later prompt-compression work.

### 5. Lauscher et al. (2021), “Argument Mining for Scholarly Document Processing: Taking Stock and Looking Ahead”
- **Primary survey:** Anne Lauscher et al. *Argument Mining for Scholarly Document Processing: Taking Stock and Looking Ahead*. ACL 2021 Workshop on Scholarly Document Processing. [ACL PDF](https://aclanthology.org/2021.sdp-1.7.pdf)
- **Scholar:** [Google Scholar lookup](https://scholar.google.com/scholar?q=%22Argument+Mining+for+Scholarly+Document+Processing%22)
- **Finding / exact evidence:** Surveys scholarly-document argument mining, including argumentative discourse units, component types, and relations such as support, contradict, same-claim, detail, and sequence; highlights evidence interpretation and persuasion in scientific writing.
- **Relation to target:** **Near miss for proof-relevant scientific context.** Scholarly argument structure could guide evidence retrieval, but the paper is a survey and does not operationalize structure-aware context selection or LLM prompting.
- **Limitation:** Scientific-document coverage is sparse and domain-specific; labels vary across corpora; no experiment showing that mined structure improves proof selection or compression.

### 6. Fan et al. (2024), “FRVA: Fact-Retrieval and Verification Augmented Entailment Tree Generation for Explainable Question Answering”
- **Primary:** Yue Fan, Hu Zhang, Ru Li, Yujie Wang, Hongye Tan, Jiye Liang. *FRVA: Fact-Retrieval and Verification Augmented Entailment Tree Generation for Explainable Question Answering*. Findings of ACL 2024, pp. 9111–9128. [ACL PDF](https://aclanthology.org/2024.findings-acl.540.pdf)
- **Scholar:** [Google Scholar lookup](https://scholar.google.com/scholar?q=%22FRVA%3A+Fact-Retrieval+and+Verification+Augmented+Entailment+Tree+Generation%22)
- **Finding / exact evidence:** Uses a fact-retrieval module to filter irrelevant facts and reduce proof search, then performs deductive–abductive bidirectional reasoning with verification and contrastive learning. Reports state-of-the-art fact selection and structural correctness on EntailmentBank.
- **Relation to target:** **Direct overlap on proof-relevant context selection and explicit deductive skeletons.** It is the strongest adjacent precedent for selecting only facts useful to a proof. However, it does not mine natural-language argument components/schemes; its inputs are fact statements and entailment trees.
- **Limitation:** EntailmentBank-style controlled facts; concatenates filtered facts into long sequences; termination conditions can miss multi-intermediate proofs; no argument-scheme classification.

### 7. Yue et al. (2024), “Retrieval Augmented Fact Verification by Synthesizing Contrastive Arguments” (RAFTS)
- **Primary:** Zhenrui Yue, Huimin Zeng, Lanyu Shang, Yifan Liu, Yang Zhang, Dong Wang. *Retrieval Augmented Fact Verification by Synthesizing Contrastive Arguments*. ACL 2024, pp. 10331–10343. [ACL page](https://aclanthology.org/2024.acl-long.556/)
- **Scholar:** [Google Scholar lookup](https://scholar.google.com/scholar?q=%22Retrieval+Augmented+Fact+Verification+by+Synthesizing+Contrastive+Arguments%22)
- **Finding / exact evidence:** Combines demonstration retrieval, document retrieval/re-ranking, and in-context prompting that synthesizes supporting and refuting arguments from retrieved evidence. The authors report gains including outperforming GPT-based baselines with a smaller 7B model.
- **Relation to target:** **Direct overlap on argument-shaped context and LLM reasoning, but not mined schemes.** It shows that retrieved evidence can be transformed into contrastive argument branches before inference. It does not classify component spans, relations, or argumentation schemes, and selection is relevance-based rather than proof-skeleton-based.
- **Limitation:** Does not study domain shift robustness of retrieval or example selection; contrastive branches are generated, not verified as formal argument structures; no prompt compression measurement.

### 8. Ruiz-Dolz, Kikteva & Lawrence (2025), “Mining Complex Patterns of Argumentative Reasoning in Natural Language Dialogue”
- **Primary:** Ramon Ruiz-Dolz, Zlata Kikteva, John Lawrence. *Mining Complex Patterns of Argumentative Reasoning in Natural Language Dialogue*. ACL 2025, pp. 7419–7435. [ACL page](https://aclanthology.org/2025.acl-long.368/)
- **Scholar:** [Google Scholar lookup](https://scholar.google.com/scholar?q=%22Mining+Complex+Patterns+of+Argumentative+Reasoning+in+Natural+Language+Dialogue%22)
- **Finding / exact evidence:** Introduces QT-SCHEMES, 441 arguments annotated with 24 schemes, and evaluates Transformer and LLM prompting for scheme/family classification. Schemes encode premise-to-conclusion patterns; the paper explicitly connects them to argument quality, fallacy identification, misinformation detection, and enthymeme reconstruction.
- **Relation to target:** **Closest current scheme-classification precedent.** It provides the exact kind of fine-grained argument-form representation that could drive proof-relevant context selection. It does not use scheme labels to retrieve or compress context, nor does it test downstream LLM reasoning over selected proof context.
- **Limitation:** Only 441 of 891 annotated arguments belong to a scheme; class imbalance and expensive annotation make results unstable; textbook-like pretraining transfers poorly to natural debate.

### 9. Bezou-Vrakatseli, Cocarascu & Modgil (2025), “Can Large Language Models Understand Argument Schemes?”
- **Primary:** Elfia Bezou-Vrakatseli, Oana Cocarascu, Sanjay Modgil. *Can Large Language Models Understand Argument Schemes?* Findings of ACL 2025, article 702. [ACL page](https://aclanthology.org/2025.findings-acl.702/)
- **Scholar:** [Google Scholar lookup](https://scholar.google.com/scholar?q=%22Can+Large+Language+Models+Understand+Argument+Schemes%3F%22)
- **Finding / exact evidence:** Systematically evaluates seven LLMs on Walton-taxonomy scheme classification under zero-shot, few-shot, and chain-of-thought prompting, with formal definitions and generated descriptions. It frames scheme classification as understanding the reasoning process and as useful for argument assessment, generation, and enthymeme handling.
- **Relation to target:** **Direct overlap on scheme classification + LLM reasoning prompt formats.** It establishes that scheme labels can be queried in LLM reasoning setups. It does not select/compress external context based on the predicted scheme or produce a proof graph.
- **Limitation:** Classification benchmark, not end-to-end proof/context selection; model behavior varies by prompt and scheme; no demonstrated improvement in downstream reasoning or retrieval efficiency.

### 10. Mushtaq & Cabessa (2025), “Argument Mining with Fine-Tuned Large Language Models”
- **Primary:** Muhammad Mushtaq and Jérôme Cabessa. *Argument Mining with Fine-Tuned Large Language Models*. COLING 2025, pp. 7037–7049. [ACL PDF](https://aclanthology.org/2025.coling-main.442.pdf)
- **Scholar:** [Google Scholar lookup](https://scholar.google.com/scholar?q=%22Argument+Mining+with+Fine-Tuned+Large+Language+Models%22+Mushtaq+Cabessa)
- **Finding / exact evidence:** Models component classification (ACC), relation identification (ARI), relation classification (ARC), and joint end-to-end AM as text generation with eight open-weight LLMs on PE, AbstRCT, and CDCP. Structural/context tags improve some tasks; joint modeling can hurt individual-task performance.
- **Relation to target:** **Direct overlap on LLM-based component/relation extraction**, useful as an implementation baseline for constructing the deductive skeleton. It does not classify argumentation schemes and does not use extracted structure to select or compress proof context.
- **Limitation:** Fine-tuning benchmark setting; results depend on model/hyperparameter choices and formatting guardrails; no proof-validity or retrieval/compression evaluation.

## Novelty-threat scan

### Direct overlaps
1. **Scheme representation used to recover latent reasoning:** Feng & Hirst (2011) explicitly classify a scheme, fit propositions to its template, and infer missing enthymeme premises. This is a direct overlap with “argument form → proof-relevant latent structure,” but not with retrieval/context compression or LLMs.
2. **Structure-aware proof context selection:** FRVA (2024) retrieves and filters irrelevant facts to reduce proof search and constructs verified entailment trees. This is a direct overlap with “proof-relevant context selection,” but not with natural-language argument mining or scheme classification.
3. **Argument-shaped RAG for LLM reasoning:** RAFTS (2024) retrieves documents and demonstrations, synthesizes supporting/refuting arguments, and feeds them to an LLM. This is a direct overlap with “argument representation → LLM reasoning context,” but the representation is generated contrastive prose, not mined components/schemes or a verified deductive skeleton.
4. **LLM scheme classification:** Bezou-Vrakatseli et al. (2025) directly tests LLMs on scheme classification with few-shot and chain-of-thought prompting. It does not close the loop into selection/compression or proof construction.

### Near misses
- **Lawrence & Reed (2016) and Ruiz-Dolz et al. (2025):** rich scheme/component representations, but no retrieval or context-budget objective.
- **Stab & Gurevych (2017) and Mushtaq & Cabessa (2025):** component/relation graphs, but no scheme/logical-form classification and no proof-context selection.
- **FRVA (2024):** proof-tree retrieval and verification, but controlled fact statements rather than argument-component mining.
- **RAFTS (2024):** retrieval and LLM prompting, but no explicit component/relation/scheme graph and no compression beyond relevance ranking.
- **Scholarly-document surveys:** motivate evidence/argument structure for scientific retrieval, but do not demonstrate structure-aware context selection.

### Negative result / novelty conclusion
Within the 10 inspected papers and the search variants below, I found **no exact prior system** that: (a) detects/classifies argument components and relations, (b) classifies the underlying argument scheme or logical form, and (c) uses that representation to select/compress only proof-relevant context for LLM reasoning. The strongest novelty risk is conceptual recombination of existing pieces, especially Feng & Hirst’s scheme-to-enthymeme reconstruction, FRVA’s proof-relevant fact filtering, and RAFTS’s retrieval-plus-contrastive-argument prompting. Any claimed novelty should therefore be phrased as the **integrated closed loop and proof-oriented context objective**, not as the individual components.

## Search log

Search date: 2026-10-11 (US/Eastern). Primary discovery route was Google Scholar-oriented web search; each result was opened through an ACL, author, journal, or proceedings route where available. Search variants (8 core + 5 novelty-focused):

1. `Google Scholar argument mining argument scheme classification logical structure proof context selection`
2. `Google Scholar argument mining premise conclusion scheme classification LLM reasoning context compression`
3. `Google Scholar argument component detection argument structure retrieval prompt context`
4. `Google Scholar computational argumentation proof relevant context selection language models`
5. `Google Scholar argument mining deductive structure entailment retrieval augmentation`
6. `Google Scholar argument scheme classification large language models reasoning prompts`
7. `Google Scholar argument graph context compression reasoning`
8. `Google Scholar rhetorical structure argument mining evidence selection proof`
9. `argument mining retrieval augmented generation argument graph proof context selection paper`
10. `argument scheme retrieval context selection language model paper`
11. `argumentative structure prompt compression LLM paper`
12. `argument mining evidence selection reasoning context paper`
13. `argument graph retrieval augmented generation explainable paper`

### Search outcomes
- Search consistently retrieved mature AM work on component detection, relation mining, and scheme classification.
- Novelty-focused searches retrieved RAFTS (retrieval + contrastive arguments), FRVA (proof-relevant fact filtering + entailment trees), and ArgRAG (argumentation-based RAG), but not a paper combining mined schemes/components with proof-context compression for LLM reasoning.
- Papers were considered **verified** only after opening a primary PDF/page and inspecting abstract, method/conclusion/limitation text. Search-result snippets were used for discovery, not as sole evidence.
- Fallback routes used: ACL Anthology PDFs/pages, author-hosted COMMA PDF, and PMLR proceedings page. DOI recorded where directly verified (Stab & Gurevych; Lawrence & Reed survey); ACL anthology IDs are retained for the remaining papers.

## Reusable design implications

1. Treat the output as a layered representation: spans/components → directed support/attack relations → scheme/logical form → explicit/implicit premises and conclusion.
2. Use relation/scheme structure to score context by proof utility, not only semantic similarity: required premises, attack coverage, support paths, missing links, and contradiction closure.
3. Preserve a compact proof skeleton when compressing context: node IDs, component type, relation type, scheme label, premise/conclusion role, and provenance span.
4. Evaluate against both retrieval metrics (recall of proof-supporting components) and reasoning metrics (valid proof tree, answer correctness, contradiction handling), since AM F1 alone does not establish proof utility.
5. Explicitly test domain transfer: Ruiz-Dolz et al. show textbook-like scheme data transfers poorly to natural debate, a warning for any scheme-conditioned context selector.
