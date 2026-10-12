# Subtopic 21 — Scholastic Method and AI: Verified Paper Summaries

**Verification date:** 2026-10-12  
**Paper count:** 10 retained papers  
**Scope note:** The retained set contains no verified paper that directly implements the medieval scholastic *quaestio/disputatio* sequence as an AI or LLM architecture. The papers below are therefore summarized by their exact or adjacent relation to the project: structured argument extraction, objection/contestability handling, formal argument semantics, debate dialogue, or question-driven critical reasoning.

## 1. Hong et al. (2022), “Scholastic: Graphical Human-Al Collaboration for Inductive and Interpretive Text Analysis”

Hong et al. present *Scholastic*, a human–AI text-analysis interface that combines machine-in-the-loop clustering with researcher-applied codes, structured metadata, hierarchical document and word clusters, and interactive visualizations for inductive and interpretive analysis.[1] The paper is an important verification of a likely false positive: “Scholastic” is the name of an HCI/ML system, not a reference to medieval scholastic method, and the system does not represent a *quaestio*, objections, distinctions, a *respondeo*, or replies. Its exact relevance is consequently low, although it offers a useful precedent for human-guided construction of structured context over a text corpus rather than treating documents as undifferentiated input.[1]

## 2. Freedman et al. (2025), “Argumentative Large Language Models for Explainable and Contestable Claim Verification”

Freedman et al. develop Argumentative Large Language Models (ArgLLMs), which augment language models with an explicit argumentation layer for explainable and contestable claim verification.[2][11] The system constructs argumentation frameworks and applies formal reasoning to evaluate claims, making contestability and explanation first-class properties rather than relying only on an unstructured generated answer. This is a strong adjacent precedent for a scholastic-AI project because objections can be treated as contesting reasons that must be represented and answered; however, the paper does not implement the ordered medieval workflow of question, objection list, distinctions, determination, and targeted replies, nor does it define a scholastic *respondeo* stage.[2][11]

## 3. Castagna, Sassoon, and Parsons (2024), “Can formal argumentative reasoning enhance LLMs performances?”

Castagna, Sassoon, and Parsons introduce MQArgEng, a proof-of-concept pipeline that inserts computational-argumentation semantics as an argumentation-engine plug-in for an LLM.[3] The reported preliminary MT-Bench experiments indicate moderate gains across most topical categories, supporting the premise that an external formal argument layer can improve LLM reasoning or conversation without retraining the base model. The paper is therefore a high-value comparator for compact philosophical context built around explicit argument relations, but its argumentation engine remains generic: it does not encode scholastic objections, distinctions, authorities, determination, or an ordered reply structure, and it should not be treated as a direct implementation of the scholastic method.[3]

## 4. Sanayei et al. (2025), “Can LLMs Judge Debates? Evaluating Non-Linear Reasoning via Argumentation Theory Semantics”

Sanayei et al. test whether LLMs can approximate Computational Argumentation Theory semantics when judging dialogue-formatted debates.[4] Using QuAD-style argumentative structures, the study asks models to rank or assess arguments without directly receiving the underlying graph and finds that performance worsens as inputs become longer or discourse flow is disrupted, while stronger prompting can partly reduce positional and length biases. Its direct contribution to a scholastic-AI design is methodological: it shows why extracting a compact argument graph or other explicit structure may be preferable to asking an LLM to recover non-linear relations from a long debate transcript. The work evaluates argument acceptability and ranking, not scholastic determination or the ordered resolution of objections.[4]

## 5. Alfano et al. (2026), “LLM-based Argument Mining meets Argumentation and Description Logics: a Unified Framework for Reasoning about Debates”

Alfano et al. propose a unified pipeline that uses LLM-assisted argument mining to turn raw debate text into a fuzzy argumentative knowledge base, representing arguments as entities with support or attack relations and initial strengths, applying quantitative argumentation semantics, and embedding the resulting structures into fuzzy description logic for query answering.[5] The full framework separates tasks such as argument tagging, entity extraction, quantitative bipolar argumentation framework extraction, and fuzzy argument-box construction, making it the closest recent technical comparator in this set for span classification, explicit relational context, formal propagation, and queryable reasoning. Its novelty threat is nevertheless adjacent rather than direct: the framework models debates and formal support/attack networks, not the scholastic *quaestio*, enumerated objections, distinctions, determination, or reply ordering.[5]

## 6. Mitsuda, Higashinaka, and Saito (2022), “Combining Argumentation Structure and Language Model for Generating Natural Argumentative Dialogue”

Mitsuda, Higashinaka, and Saito combine a hand-crafted argumentation structure with a language model that rewrites propositions—using keywords and stance information—into the next natural-language utterance while preserving argumentative context.[6] Their manual evaluation reports improved naturalness without loss of argumentation consistency, establishing a clear separation between a structured argumentative skeleton and surface-language realization. That separation parallels a scholastic-AI architecture in which a system first extracts or constructs a deductive/disputational skeleton and only then generates polished philosophical prose. The paper remains an adjacent dialogue-generation precedent: it does not model objections, distinctions, determination, or scholastic replies as explicit protocol stages.[6]

## 7. Sazid et al. (2022), “A Unified Representation and a Decoupled Deep Learning Architecture for Argumentation Mining of Students’ Persuasive Essays”

Sazid et al. propose a unified representation and decoupled deep-learning architecture for identifying non-argumentative units, premises, claims, major claims, and relations such as support, attack, for, and against in students’ persuasive essays.[7] The paper is relevant because it demonstrates how text spans can be assigned argument roles and converted into a compact relational representation rather than being processed as undifferentiated prose. That capability could support extraction of premises, claims, and counter-considerations from scholastic texts, but the source domain is monologic essay argument mining: it has no dialogue moves, explicit objection/reply pairs, distinction phase, authority handling, or scholastic resolution stage. It is therefore a medium-strength structural precedent rather than a direct novelty threat.[7]

## 8. Macagno (2021), “Argumentation Schemes in AI: A Literature Review. Introduction to the Special Issue”

Macagno reviews AI research using Walton-style argumentation schemes and characterizes schemes as dialectical instruments with premises, conclusions, and critical questions.[8] The review explains how critical questions can challenge a scheme’s applicability or shift the burden of proof back to a proponent, and it surveys applications spanning argument mining, representation, multi-agent systems, law, policy, healthcare, economics, and education. This is the strongest conceptual bridge in the set between scholastic-style dialectical organization and computational implementation: critical questions, defeasible presumptions, burden shifting, nested arguments, and dialogue protocols function as partial computational analogues of objections and replies. The limitation is decisive for novelty: the article is a literature review of argumentation schemes, not an LLM system and not a full implementation of the medieval *quaestio/disputatio* sequence.[8]

## 9. Walton (2016), “Some Artificial Intelligence Tools for Argument Evaluation: An Introduction”

Walton surveys AI tools for evaluating defeasible arguments in legal and everyday conversational settings, emphasizing approaches that go beyond deductive logic and Bayesian rules through argument graphs, argumentation schemes, and systems such as Carneades.[9] The paper supplies foundational prior art for using an intermediate argument representation between natural-language discourse and formal evaluation, which is directly relevant to extracting and checking the reasoning skeleton of scholastic texts. It predates current LLMs and does not address automatic extraction of scholastic components, medieval textual organization, or an explicit question–objection–determination–reply protocol. Its relevance is thus foundational and conceptual rather than a direct system-level overlap.[9]

## 10. Shi et al. (2026), “Tackling the Root of Misinformation by Teaching Laypeople about Logical Fallacies via Socratic Questioning and Critical Argumentation”

Shi et al. introduce LFTutor, an LLM-based tutoring system that combines intent-driven Socratic questioning with critical argumentation to teach users to identify logical fallacies.[10] The study reports automatic and human-evaluation gains over baseline LLMs that lack the pedagogical strategies, showing that question-driven challenge and reflective response can be operationalized as a controlled interaction pattern. This is relevant to a scholastic-AI project as a nearby design precedent for generating objections, eliciting commitments, and prompting replies instead of producing a single unsupported answer. Its method is Socratic pedagogy rather than medieval scholastic disputation, and the opened record does not define a *quaestio*, formal objection list, distinction stage, *respondeo*, or determination data structure.[10]

## Synthesis

Across all ten verified papers, the direct duplicate risk remains low: none operationalizes the complete medieval scholastic sequence as an AI/LLM reasoning architecture. The high-risk adjacent convergence is clear, however. Existing work already covers explicit argument representations, support/attack relations, formal argumentation semantics, contestability, debate judging, argument mining, structured dialogue generation, and question-driven critical reasoning. A defensible novelty claim should therefore center on making the scholastic sequence itself a first-class computational object: identify and normalize the question, enumerate objections, distinguish senses or cases, locate authorities and reasons, produce a determination, and attach targeted replies to each objection with provenance.

## Sources

[1] https://arxiv.org/abs/2208.06133
[2] https://ojs.aaai.org/index.php/AAAI/article/view/33637
[3] https://arxiv.org/abs/2405.13036
[4] https://arxiv.org/abs/2509.15739
[5] https://arxiv.org/abs/2603.02858
[6] https://aclanthology.org/2022.aacl-short.9
[7] https://aclanthology.org/2022.argmining-1.6
[8] https://philpapers.org/archive/MACASI-11.pdf
[9] https://philpapers.org/rec/WALSAI-4
[10] https://aclanthology.org/2026.acl-long.2209
[11] https://arxiv.org/abs/2405.02079
