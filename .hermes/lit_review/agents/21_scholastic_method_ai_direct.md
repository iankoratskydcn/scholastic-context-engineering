# Novelty sweep — scholastic method + AI (direct exact-match angle)

**Search date:** 2026-10-12  
**Scope:** direct combinations of “scholastic method”/scholastic reasoning with AI, LLMs, machine learning, and computational argumentation; then adjacent systems that operationalize disputation-like structure (objections, replies, support/attack, critical questions, dialogue protocols, argument graphs).

## Bottom line

The direct area is thin. I found **no verified paper that explicitly operationalizes the medieval scholastic method (quaestio/disputatio, objections, respondeo/determination, distinctions) as an AI/LLM reasoning architecture**. The only exact-token arXiv hit, *Scholastic*, is a human–AI text-analysis interface and uses “scholastic” as a project name, not as medieval disputation. The closest threat set is computational argumentation and argumentative-dialogue work: these operationalize support/attack, critical questions, argument graphs, structured debate, or formal defeasible reasoning, but generally do not map the full scholastic sequence.

The strongest novelty threat to this project is therefore **adjacent methodological convergence**, not a direct duplicate: an LLM extracts arguments and relations, a formal argumentation layer evaluates them, and a dialogue layer generates or judges exchanges. The project remains differentiated if it makes the scholastic sequence itself explicit and useful for compact philosophical context: question → objections → distinctions → determination → replies, with provenance and deductive skeleton extraction.

## Verified papers and findings

### 1. Hong et al. (2022), “Scholastic: Graphical Human-Al Collaboration for Inductive and Interpretive Text Analysis”
- **Citation:** Matt-Heun Hong, Lauren A. Marsh, Jessica L. Feuston, Janet Ruppert, Jed R. Brubaker, and Danielle Albers Szafir. 2022. *Scholastic: Graphical Human-Al Collaboration for Inductive and Interpretive Text Analysis*. To appear at ACM UIST 2022; arXiv:2208.06133. DOI: 10.1145/3526113.3545681.
- **Finding:** The system uses a machine-in-the-loop clustering algorithm, scholar-applied codes, structured metadata, hierarchical document/word clusters, and interactive visualizations to scaffold inductive and interpretive text analysis. It is not a scholastic disputation system.
- **Relation to project:** Relevant only as a naming/false-positive check and as a precedent for human-guided structured context construction over text corpora.
- **Limitation:** No objections, replies, quaestiones, distinctions, disputation protocol, or formal argument evaluation.
- **Source route:** arXiv abstract page, opened and read: https://arxiv.org/abs/2208.06133
- **Novelty-threat ranking:** **Low / false positive**.

### 2. Freedman et al. (2025), “Argumentative Large Language Models for Explainable and Contestable Claim Verification”
- **Citation:** Gabriel Freedman et al. 2025. *Argumentative Large Language Models for Explainable and Contestable Claim Verification*. Proceedings of the AAAI Conference on Artificial Intelligence 39(14):14930–14939. DOI: 10.1609/aaai.v39i14.33637; arXiv:2405.02079.
- **Finding:** ArgLLMs augment LLMs with argumentative reasoning by constructing argumentation frameworks, then use formal reasoning for claim verification. The paper explicitly targets explanations and contestability and defines properties for evaluating contestability.
- **Relation to project:** Strong adjacent precedent for extracting a structured argument layer before generation/evaluation. Its contestability framing is close to handling objections and replies.
- **Limitation:** The architecture is an argumentation framework for claim verification, not a scholastic quaestio/disputatio workflow; no explicit distinction phase or ordered respondeo/reply structure.
- **Source route:** arXiv abstract page, opened and read; it identifies the AAAI 2025 venue and DOI: https://arxiv.org/abs/2405.02079
- **Novelty-threat ranking:** **High adjacent threat**.

### 3. Castagna, Sassoon, and Parsons (2024), “Can formal argumentative reasoning enhance LLMs performances?”
- **Citation:** Federico Castagna, Isabel Sassoon, and Simon Parsons. 2024. *Can formal argumentative reasoning enhance LLMs performances?* arXiv:2405.13036. DOI: 10.48550/arXiv.2405.13036.
- **Finding:** Presents MQArgEng, a pipeline that introduces computational argumentation semantics as an argumentation-engine plugin for LLMs; preliminary MT-Bench experiments report moderate gains in most topical categories.
- **Relation to project:** Directly supports the project’s premise that a formal argument layer can improve LLM reasoning/conversation without retraining. It is a clear comparator for compact context built around argument relations.
- **Limitation:** Proof-of-concept and feasibility study; it does not model scholastic objections, distinctions, or replies as a named protocol.
- **Source route:** arXiv abstract page, opened and read: https://arxiv.org/abs/2405.13036
- **Novelty-threat ranking:** **High adjacent threat**.

### 4. Sanayei et al. (2025), “Can LLMs Judge Debates? Evaluating Non-Linear Reasoning via Argumentation Theory Semantics”
- **Citation:** Reza Sanayei et al. 2025. *Can LLMs Judge Debates? Evaluating Non-Linear Reasoning via Argumentation Theory Semantics*. Findings of EMNLP 2025; arXiv:2509.15739. DOI: 10.48550/arXiv.2509.15739.
- **Finding:** Evaluates whether LLMs can approximate Computational Argumentation Theory using QuAD semantics. Models rank arguments from dialogue-formatted debates without the underlying graph; performance degrades with longer inputs and disrupted discourse flow, while advanced prompting partly mitigates positional/length bias.
- **Relation to project:** Strong evidence that argument-graph reconstruction and compact structured context matter for non-linear debate reasoning.
- **Limitation:** Focuses on judging argument acceptability/ranking, not generating scholastic determinations or resolving objections through ordered replies.
- **Source route:** arXiv abstract page, opened and read: https://arxiv.org/abs/2509.15739
- **Novelty-threat ranking:** **High adjacent threat**.

### 5. Alfano et al. (2026), “LLM-based Argument Mining meets Argumentation and Description Logics: a Unified Framework for Reasoning about Debates”
- **Citation:** Gianvincenzo Alfano et al. 2026. *LLM-based Argument Mining meets Argumentation and Description Logics: a Unified Framework for Reasoning about Debates*. arXiv:2603.02858. DOI: 10.48550/arXiv.2603.02858.
- **Finding:** Extracts a fuzzy argumentative knowledge base from raw debate text; represents arguments as entities with support/attack relations and initial strengths; applies quantitative argumentation semantics; and embeds results into fuzzy description logic for query answering. The full paper describes separate LLM-assisted tasks for argument tagging, entity extraction, QBAF extraction, and FABox construction.
- **Relation to project:** Very close on span classification, explicit support/attack structure, formal propagation, and compact queryable context. It is the most technically relevant recent comparator.
- **Limitation:** Debate graphs and description logic are not scholastic method; no quaestio, objection list, distinction, determination, or reply ordering.
- **Source route:** arXiv abstract and HTML/full-text page, opened and read: https://arxiv.org/abs/2603.02858
- **Novelty-threat ranking:** **Very high adjacent threat**.

### 6. Mitsuda, Higashinaka, and Saito (2022), “Combining Argumentation Structure and Language Model for Generating Natural Argumentative Dialogue”
- **Citation:** Koh Mitsuda, Ryuichiro Higashinaka, and Kuniko Saito. 2022. *Combining Argumentation Structure and Language Model for Generating Natural Argumentative Dialogue*. Proceedings of AACL-IJCNLP 2022 (Volume 2: Short Papers), 65–71. DOI: 10.18653/v1/2022.aacl-short.9.
- **Finding:** Combines a hand-crafted argumentation structure with a language model; the model rewrites propositions containing keywords and stance into the next utterance while preserving context. Manual evaluation found improved naturalness without losing argumentation consistency.
- **Relation to project:** Precedent for separating a structured argumentative skeleton from surface realization, which parallels extracting a deductive/scholastic skeleton before philosophical prose generation.
- **Limitation:** Dialogue generation is not scholastic disputation; the paper does not implement objections, replies, distinctions, or a determination stage.
- **Source route:** ACL Anthology page, opened and read: https://aclanthology.org/2022.aacl-short.9/
- **Novelty-threat ranking:** **Medium-high adjacent threat**.

### 7. Sazid et al. (2022), “A Unified Representation and a Decoupled Deep Learning Architecture for Argumentation Mining of Students’ Persuasive Essays”
- **Citation:** Muhammad Tawsif Sazid et al. 2022. *A Unified Representation and a Decoupled Deep Learning Architecture for Argumentation Mining of Students’ Persuasive Essays*. Proceedings of the 9th Workshop on Argument Mining, 2022.
- **Finding:** Jointly represents non-argumentative units, premises, claims, major claims, and relations including support/attack and for/against links in an end-to-end machine-learning pipeline.
- **Relation to project:** Relevant precedent for classifying text spans by underlying argument role and constructing a compact relational representation rather than treating prose as undifferentiated text.
- **Limitation:** Essay argument mining lacks dialogue moves, objections, replies, distinctions, and a scholastic resolution phase.
- **Source route:** ACL Anthology page, opened and read: https://aclanthology.org/2022.argmining-1.6/
- **Novelty-threat ranking:** **Medium adjacent threat**.

### 8. Macagno (2021), “Argumentation schemes in AI: A literature review. Introduction to the special issue”
- **Citation:** Fabrizio Macagno. 2021. *Argumentation schemes in AI: A literature review. Introduction to the special issue*. Argument & Computation 12(3):287–302. DOI: 10.3233/AAC-210020.
- **Finding:** Reviews AI work using Walton-style argumentation schemes. The paper characterizes schemes as dialectical instruments with premises, conclusions, and critical questions; critical questions can shift the burden of proof back to the proponent. It reports a screened corpus and notes applications in argument mining, representation, argument support, multiagent systems, law, policy, healthcare, economics, and education.
- **Relation to project:** This is the key bridge from scholastic-style dialectical structure to computational implementation: critical questions, burden shifting, defeasible presumptions, nested arguments, and dialogue protocols are close functional analogues to objections and replies.
- **Limitation:** It is a literature review of argumentation schemes, not an LLM system and not a direct implementation of medieval scholastic method. The paper’s historical lineage is dialectical/argumentation-scheme based rather than a full quaestio architecture.
- **Source route:** PhilPapers-hosted PDF, opened and read: https://philpapers.org/archive/MACASI-11.pdf
- **Novelty-threat ranking:** **High conceptual threat / strong prior-art map**.

### 9. Walton (2016), “Some Artificial Intelligence Tools for Argument Evaluation: An Introduction”
- **Citation:** Douglas Walton. 2016. *Some Artificial Intelligence Tools for Argument Evaluation: An Introduction*. Argumentation 30(3):317–340. DOI: 10.1007/s10503-015-9387-x.
- **Finding:** Describes computational systems for defeasible argumentation as tools for evaluating legal and everyday conversational arguments, beyond deductive logic and Bayesian rules. Keywords include argument graphs, schemes, and the Carneades Argumentation System.
- **Relation to project:** Foundational comparator for formal evaluation of real arguments and for using argument graphs/schemes as an intermediate representation between natural-language discourse and reasoning.
- **Limitation:** Predates LLMs and does not implement scholastic textual organization or machine extraction of quaestio components.
- **Source route:** PhilPapers record, opened and read: https://philpapers.org/rec/WALSAI-4
- **Novelty-threat ranking:** **Medium conceptual prior art**.

### 10. Shi et al. (2026), “Tackling the Root of Misinformation by Teaching Laypeople about Logical Fallacies via Socratic Questioning and Critical Argumentation”
- **Citation:** Minjing Shi, Junling Wang, Jingwei Ni, Sankalan Pal Chowdhury, and Mrinmaya Sachan. 2026. *Tackling the Root of Misinformation by Teaching Laypeople about Logical Fallacies via Socratic Questioning and Critical Argumentation*. Proceedings of ACL 2026 (Volume 1: Long Papers), 47821–47868. DOI: 10.18653/v1/2026.acl-long.2209.
- **Finding:** Introduces LFTutor, an LLM-based tutoring system that combines intent-driven Socratic questioning and critical argumentation to teach logical-fallacy identification; automatic and human evaluations report gains over baseline LLMs without the pedagogical strategies.
- **Relation to project:** Relevant because it operationalizes question-driven challenge and reflective response in an LLM system, showing a nearby route for objection-generation and reply elicitation.
- **Limitation:** Socratic pedagogy is not scholastic disputation; there is no explicit quaestio/objection/respondeo/determination data structure in the opened record.
- **Source route:** ACL Anthology page, opened/read through search result metadata and abstract: https://aclanthology.org/2026.acl-long.2209/
- **Novelty-threat ranking:** **Medium adjacent threat**.

## Novelty assessment for this project

1. **Direct duplicate risk: low.** The exact phrase “scholastic method” did not yield a verified AI/LLM paper that operationalizes medieval disputation. The arXiv paper titled *Scholastic* is unrelated to scholastic method.
2. **Argument-structure convergence risk: high.** ArgLLMs, MQArgEng, QuAD debate judging, and the Alfano et al. framework already cover explicit argument representations, attack/support relations, formal semantics, contestability, and graph-based evaluation.
3. **Distinctive opportunity:** make the scholastic sequence a first-class computational object rather than a generic argument graph: identify the question, normalize the thesis, enumerate objections, locate authorities/reasons, extract distinctions, produce the determination, and attach targeted replies to each objection. A verified novelty claim should be limited to this explicit end-to-end operationalization unless further evidence is found.

## Failed / blocked searches

### Google Scholar first-pass (8 query variants)
Google Scholar returned its bot-check page rather than results for every query in this environment (IP/time page; no result list could be inspected). The attempted variants were:

1. `"scholastic method" AI`
2. `"scholastic method" LLM`
3. `"scholastic method" "machine learning"`
4. `"scholastic" "computational argumentation"`
5. `"scholastic reasoning" AI`
6. `scholastic disputation LLM`
7. `quaestio objection reply "large language model"`
8. `scholastic method argumentation AI`

### Other routes
- **ACL Anthology:** no direct “scholastic method” hit found; useful adjacent hits were argumentative dialogue, argument mining, and Socratic critical-argumentation systems.
- **arXiv:** exact-token hit was the unrelated *Scholastic* HCI/ML system; relevant adjacent computational-argumentation/LLM papers were found and opened.
- **PhilPapers:** direct scholastic-method + AI results were not found; PhilPapers was useful for opened records/PDFs on AI argument evaluation and argumentation schemes.
- **JSTOR/publisher pages:** no verified direct-match paper located in the available sweep; publisher access/search was not productive enough to treat snippets as evidence.
- **Fallback web search:** surfaced the same adjacent computational-argumentation cluster and a non-scholarly product page claiming an AI “Magister”; excluded from the paper count because it is not a paper and does not establish academic prior art.

## Sources

1. https://arxiv.org/abs/2208.06133
2. https://arxiv.org/abs/2405.02079
3. https://arxiv.org/abs/2405.13036
4. https://arxiv.org/abs/2509.15739
5. https://arxiv.org/abs/2603.02858
6. https://aclanthology.org/2022.aacl-short.9/
7. https://aclanthology.org/2022.argmining-1.6/
8. https://philpapers.org/archive/MACASI-11.pdf
9. https://philpapers.org/rec/WALSAI-4
10. https://aclanthology.org/2026.acl-long.2209/
