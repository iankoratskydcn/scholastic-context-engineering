# Subtopic 13 — Knowledge graphs and structured knowledge as LLM scaffolding

**Scope.** Scholar-oriented sweep of methods that use knowledge graphs (KGs), graph-structured evidence, or explicit knowledge integration as scaffolding around language models. The retained set spans foundational knowledge-enhanced pretraining, graph–LM joint reasoning, KG prompting, and current graph-RAG / faithful-reasoning systems.

**Search routes.** Eight queries were run against scholarly web indexes and then checked against a direct arXiv, ACL Anthology, AAAI, PMLR, or conference landing page: (1) `knowledge graphs large language models retrieval augmentation paper`; (2) `structured knowledge graph LLM reasoning paper`; (3) `knowledge graph enhanced language models paper`; (4) `graph retrieval augmented generation LLM paper`; (5) `LLM scaffolding structured knowledge paper`; (6) `knowledge graph prompting large language models paper`; (7) `entity-centric retrieval language models knowledge graph paper`; (8) `survey knowledge graphs large language models 2024 paper`. Search hits were deduplicated by title and retained only when a primary scholarly page exposed the title plus abstract or paper text.

## Verified paper set

### 1. ERNIE: Enhanced Representation through Knowledge Integration — Sun et al. (2019)
- **Finding.** Introduces knowledge-enhanced language representation using entity-level and phrase-level masking, so pretraining can absorb structured/entity knowledge rather than only token co-occurrence.[10]
- **Relation.** Foundational *internal scaffold*: structured knowledge is injected during pretraining, not retrieved at inference time.
- **Limitation.** Knowledge is tied to pretraining data and masking design; the approach does not provide an explicit, inspectable evidence graph for each generation.
- **Novelty overlap.** High overlap on “structured knowledge improves representation,” but lower overlap with runtime context engineering, provenance, and controllable retrieval.

### 2. K-BERT: Enabling Language Representation with Knowledge Graph — Liu et al. (AAAI 2020)
- **Finding.** Injects KG triples into sentences and uses a knowledge-rich tree plus visible matrices to limit attention interference, extending BERT with domain knowledge.[9]
- **Relation.** Direct precedent for treating a KG as a structured side-context that scaffolds language understanding.
- **Limitation.** Triple expansion and sentence-level injection can increase sequence/branching complexity; the method is primarily encoder-side and does not solve open-ended generation grounding.
- **Novelty overlap.** High overlap on graph-to-text context construction; distinct from newer approaches that retrieve only a query-relevant subgraph or constrain reasoning paths.

### 3. KEPLER: A Unified Model for Knowledge Embedding and Pre-trained Language Representation — Wang et al. (2020)
- **Finding.** Unifies language representation learning with KG embedding, jointly optimizing textual and relational objectives so entity representations encode both language and graph structure.[11]
- **Relation.** Establishes a shared latent space between language and structured knowledge—an important precursor to graph-conditioned LLM scaffolding.
- **Limitation.** Joint embeddings do not automatically guarantee faithful multi-hop generation or expose the exact graph facts used at inference.
- **Novelty overlap.** Medium overlap: shared representations are an upstream alternative to explicit prompt/retrieval scaffolds.

### 4. QA-GNN: Reasoning with Language Models and Knowledge Graphs for Question Answering — Yasunaga et al. (NAACL 2021)
- **Finding.** Addresses KGQA by identifying relevant KG knowledge and reasoning jointly over question/context nodes and retrieved graph nodes with a graph neural network and LM representations.[12]
- **Relation.** Strong direct precedent for a *query-specific graph scaffold* that connects language evidence to symbolic entities and relations.
- **Limitation.** Designed around multiple-choice/QA settings and a bounded retrieved subgraph; transfer to unconstrained generation and noisy enterprise KGs is not established by the paper.
- **Novelty overlap.** High overlap on entity linking, graph retrieval, and joint reasoning; newer graph-RAG work generalizes the scaffold to document graphs and generation.

### 5. GreaseLM: Graph REASoning Enhanced Language Models for Question Answering — Zhang et al. (ICLR 2022)
- **Finding.** Interleaves LM representations with graph reasoning so a model can reason over textual narratives and the world knowledge represented in a KG.[13]
- **Relation.** Demonstrates iterative bidirectional exchange between language and graph modules rather than one-shot graph concatenation.
- **Limitation.** The architecture is task-specific and graph-dependent; it requires curated graph construction/retrieval and does not directly address citation-level provenance in free-form answers.
- **Novelty overlap.** High overlap on graph–LM co-reasoning; its main distinction from prompt-based scaffolds is learned cross-modal fusion.

### 6. Knowledge Graph Prompting for Multi-Document Question Answering — Wang et al. (AAAI 2024; arXiv:2308.11730)
- **Finding.** Uses a KG extracted from multiple documents to support the pre-train/prompt/predict paradigm for multi-document QA, where cross-document relations are central.[3]
- **Relation.** Very close to structured context engineering: construct a graph from a document set, serialize relevant structure, and prompt the LLM.
- **Limitation.** Performance depends on extraction quality and the prompt representation; the evidence path may still be mediated by the LLM rather than formally verified.
- **Novelty overlap.** Very high overlap on graph-structured context as an LLM scaffold, especially for cross-document synthesis.

### 7. MindMap: Knowledge Graph Prompting Sparks Graph of Thoughts in Large Language Models — Wen, Wang, Sun (ACL 2024)
- **Finding.** Uses KG prompting to induce graph-like thought organization, targeting knowledge incorporation, hallucination reduction, and more explainable reasoning.[2]
- **Relation.** Connects external structured knowledge with an internal reasoning scaffold: the graph is not only evidence but also a representation for organizing intermediate thoughts.
- **Limitation.** “Graph of thoughts” remains dependent on model-generated transformations and benchmark behavior; graph completeness, consistency, and causal faithfulness are not guaranteed.
- **Novelty overlap.** High overlap on graph-structured intermediate context; novelty is strongest where the scaffold shapes reasoning topology rather than only retrieval.

### 8. KnowGPT: Knowledge Graph based Prompting for Large Language Models — Feng et al. (NeurIPS 2024)
- **Finding.** Presents KG-based prompting to address hallucination and knowledge gaps by retrieving/organizing structured domain knowledge for LLM prompts.[1]
- **Relation.** Directly frames KGs as an inference-time prompt scaffold, including domain terminology and relations that ordinary semantic retrieval can miss.
- **Limitation.** KG quality, entity linking, and path selection remain bottlenecks; prompting a graph does not by itself prove that the answer follows from it.
- **Novelty overlap.** Very high overlap with the target subtopic; the differentiator is systematic KG prompting rather than model pretraining or graph neural fusion.

### 9. KAPALM: Knowledge grAPh enhAnced Language Models for Fake News Detection — Ma et al. (Findings EMNLP 2023)
- **Finding.** Combines coarse- and fine-grained graph knowledge with language modeling for fake-news detection.[8]
- **Relation.** Shows that structured knowledge can act as a task-specific scaffold for credibility-sensitive classification, not only QA or generation.
- **Limitation.** Domain/task-specific labels and graph sources limit generalization to broad LLM context construction; classification gains do not establish generation faithfulness.
- **Novelty overlap.** Medium overlap: relevant as evidence that graph scaffolds improve decisions, but peripheral to general-purpose LLM orchestration.

### 10. Knowledge Graph-Enhanced Large Language Models via Path Selection — Liu et al. (Findings ACL 2024)
- **Finding.** Selects useful KG paths before feeding graph knowledge to an LLM, targeting factuality while controlling irrelevant or excessive graph context.[7]
- **Relation.** Directly advances the “retrieve, compress, and serialize a minimal reasoning scaffold” pattern.
- **Limitation.** Path selection can encode heuristic or learned biases; a selected path may be locally plausible while omitting competing evidence or alternative relations.
- **Novelty overlap.** Very high overlap on relation-aware context selection; novelty is the explicit path-selection bottleneck between KG retrieval and LLM prompting.

### 11. GRAG: Graph Retrieval-Augmented Generation — Hu et al. (Findings NAACL 2025)
- **Finding.** Extends RAG to networked documents (citation graphs, social graphs, KGs), arguing that chunk-independent retrieval misses topological information and proposing graph-aware retrieval/generation.[4]
- **Relation.** Generalizes KG scaffolding to graph-structured corpora: topology becomes part of the retrieved context, not merely metadata.
- **Limitation.** Graph traversal and neighborhood expansion risk context bloat and noise; gains depend on graph quality and the relation between topology and answer relevance.
- **Novelty overlap.** Very high overlap with graph-RAG as structured context engineering; broader than KG-only methods because the nodes can be documents and the edges can be arbitrary relations.

### 12. Knowledge Graph-Guided Retrieval Augmented Generation — Zhu et al. (NAACL 2025)
- **Finding.** Uses a KG to guide retrieval toward related evidence instead of isolated semantic chunks, explicitly targeting hallucination reduction and relational completeness.[5]
- **Relation.** Strong direct match for KG-guided scaffolding: the graph mediates which textual evidence reaches the LLM.
- **Limitation.** Requires reliable graph construction/linking and may propagate graph errors; relational guidance does not eliminate generation-time unsupported claims.
- **Novelty overlap.** Very high overlap with the target concept; relative novelty is the KG-guided retriever/controller rather than pure KG prompting or joint representation learning.

### 13. Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models — Luo et al. (ICML 2025 / PMLR)
- **Finding.** Constrains reasoning over a KG to improve faithfulness, addressing weaknesses in retrieval-based and agent-based KG-enhanced reasoning.[6]
- **Relation.** Moves beyond “show the model a graph” toward enforcing graph-valid reasoning trajectories—a stronger form of scaffolding.
- **Limitation.** Hard constraints can reduce recall or flexibility when the KG is incomplete, ambiguous, or mismatched to the question; graph-faithful reasoning is only as good as graph coverage.
- **Novelty overlap.** Very high overlap and a likely frontier direction: structured knowledge becomes a constraint on the reasoning process, not just an input context.

## Cross-paper synthesis

1. **Three scaffold locations.** The literature separates into (a) **pretraining-time internalization** (ERNIE, KEPLER), (b) **learned graph–LM fusion** (K-BERT, QA-GNN, GreaseLM), and (c) **inference-time retrieval/prompt/control** (MindMap, KnowGPT, path selection, GRAG, KG-guided RAG, graph-constrained reasoning). For context-engineering purposes, the third family is most directly reusable because the KG can be updated without retraining the base LLM.
2. **The recurring pipeline.** Most current systems implement some version of: entity/link extraction → graph/subgraph or path retrieval → graph serialization or graph module → LLM generation/reasoning. The main research bottleneck has shifted from “can structured knowledge help?” to “which subgraph/path should be exposed, in what representation, and how can the answer be verified?”
3. **Topology is increasingly treated as information.** GRAG and KG-guided RAG explicitly argue that independent semantic chunks omit relationships. This supports treating adjacency, relation type, path length, and provenance as first-class context fields rather than flattening everything into text.
4. **Prompting is weaker than constraint.** KG prompting can improve organization and factuality, but MindMap/KnowGPT/path-selection methods still rely on the LLM to interpret and obey the scaffold. Graph-constrained reasoning is the clearest move toward enforceable validity, with the tradeoff of incomplete-KG brittleness.
5. **Shared limitations.** Across the set: entity resolution errors, stale/incomplete graphs, relation extraction noise, graph-to-text serialization loss, context-window cost, benchmark dependence, and weak evidence that generated claims are fully entailed by the supplied graph. Few papers jointly evaluate retrieval quality, reasoning faithfulness, provenance, latency, and maintenance cost under realistic changing KGs.

## Novelty overlap assessment for this project

The crowded baseline is **“retrieve a relevant KG neighborhood and place it in an LLM prompt.”** A differentiated contribution should therefore emphasize one or more of: (i) explicit provenance and claim-to-edge traceability; (ii) adaptive subgraph construction that optimizes relevance, coverage, and token budget; (iii) conflict/version handling for changing structured knowledge; (iv) hard or testable graph-consistency checks after generation; (v) compositional scaffolds that combine KG edges with document evidence, schemas, constraints, and tool state; or (vi) evaluation beyond answer accuracy, including unsupported-claim rate, path faithfulness, retrieval recall, cost, and update robustness.

## Sources / verification ledger

The 13 primary scholarly landing pages used for title/abstract or paper-text verification are recorded in the research ledger as [1]–[13].

[1] KnowGPT, arXiv: https://arxiv.org/abs/2312.06185  
[2] MindMap, ACL Anthology: https://aclanthology.org/2024.acl-long.558/  
[3] Knowledge Graph Prompting for Multi-Document QA, AAAI: https://ojs.aaai.org/index.php/AAAI/article/view/29889  
[4] GRAG, ACL Anthology: https://aclanthology.org/2025.findings-naacl.232/  
[5] KG-Guided RAG, ACL Anthology: https://aclanthology.org/2025.naacl-long.449/  
[6] Graph-constrained Reasoning, PMLR: https://proceedings.mlr.press/v267/luo25t.html  
[7] Path Selection, ACL Anthology: https://aclanthology.org/2024.findings-acl.376/  
[8] KAPALM, ACL Anthology: https://aclanthology.org/2023.findings-emnlp.263/  
[9] K-BERT, AAAI: https://aaai.org/papers/02901-k-bert-enabling-language-representation-with-knowledge-graph/  
[10] ERNIE, arXiv: https://arxiv.org/abs/1904.09223  
[11] KEPLER, arXiv: https://arxiv.org/abs/1911.06136  
[12] QA-GNN, ACL Anthology: https://aclanthology.org/2021.naacl-main.45/  
[13] GreaseLM, arXiv: https://arxiv.org/abs/2201.08860

## Sources

The source URLs above are the direct primary scholarly landing pages used for verification. The numbered references are local cross-references to that list; URLs are preserved verbatim so the route and identifier remain auditable.
