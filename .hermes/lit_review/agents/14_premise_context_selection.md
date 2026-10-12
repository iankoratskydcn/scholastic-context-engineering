# Subtopic 14 — Premise selection and proof-relevant context selection

**Search date:** 2026-10-11  
**Scope:** premise selection, proof-relevant retrieval, argument/proof structure, context compression, and LLM reasoning.  
**Retention rule:** 18 papers retained after checking a paper landing page, abstract, or full-text PDF from a scholarly/first-party venue. “Direct overlap” means the paper selects formal premises/lemmas or proof-state context for theorem proving; “adjacent” means it selects/compresses general retrieved context but does not perform proof-relevant premise selection.

## Scholar-first search variants

Google Scholar-oriented searches were run first (via indexed Scholar results), followed by primary paper pages for verification. Variants:

1. `premise selection proof-relevant retrieval argument structure`
2. `premise selection context compression theorem proving`
3. `proof-relevant context selection language models reasoning`
4. `argument structure premise retrieval LLM reasoning`
5. `context selection automated theorem proving neural`
6. `premise retrieval mathematical reasoning language model`
7. `proof-relevant retrieval theorem proving`
8. `context compression chain of thought reasoning`

Scholar indexing was useful for discovering author/title clusters, but paper claims below are based on the linked paper/venue pages rather than Scholar snippets.

## Retained papers

| # | Paper / year | Evidence checked | Relevance and overlap |
|---:|---|---|---|
| 1 | **DeepMath — Deep Sequence Models for Premise Selection** — Irving et al., NeurIPS 2016 | [NeurIPS paper page](https://papers.neurips.cc/paper_files/paper/2016/hash/f197002b9a0853eca5e046d9ca4663d5-Abstract.html) | **Direct overlap.** Neural premise selection for ATP over Mizar; frames selection as retrieving a small axiom subset for a conjecture and combines learned representations with existing methods. Foundational precedent for learned proof-relevant context selection. |
| 2 | **Premise Selection for Theorem Proving by Deep Graph Embedding** — Wang, Tang, Wang & Deng, NeurIPS 2017 / ICLR publication record | [OpenReview/PDF](https://openreview.net/pdf?id=r1xwKoR9Y7) | **Direct overlap.** Embeds goal and premise formula graphs and scores relevance, making logical/structural form an explicit retrieval signal rather than relying only on token similarity. |
| 3 | **Graph Representations for Higher-Order Logic and Theorem Proving** — Paliwal et al., ICLR 2019 | [OpenReview/PDF](https://openreview.net/pdf?id=iUGUc3HJ_3f) | **Direct overlap.** Uses graph representations of goals and premises with a learned premise-relevance scorer inside tactic/proof search; important precedent for argument/proof structure as retrieval context. |
| 4 | **Learning to Prove Theorems via Interacting with Proof Assistants** — Bansal et al., ICML 2019 | [arXiv record](https://arxiv.org/abs/1905.09381) | **Direct overlap.** Learns tactic and premise guidance from proof-assistant interaction; relevant because the selected context is proof-state-specific and action-conditioned, not a static document retrieval result. |
| 5 | **Formal Premise Selection With Language Models** — Tworkowski et al., AITP 2022 | [AITP paper PDF](https://aitp-conference.org/2022/abstract/AITP_2022_paper_32.pdf) | **Direct overlap — especially close.** First selects a handful of premises from a database of roughly 100K premises, then presents them with proof states to a language model that constructs the next proof step. This is the clearest prior formulation of “proof-relevant context selection → LLM reasoning.” |
| 6 | **TextGraphs-16 Natural Language Premise Selection Task: Zero-Shot Premise Selection with Prompting Generative Language Models** — Kovriguina, Teucher & Wardenga, 2022 | [ACL Anthology](https://aclanthology.org/2022.textgraphs-1.15/) | **Direct overlap, natural-language side.** Tests prompting GPT-3 for premise ranking; vanilla prompting did not beat SBERT similarity, but merging prompt-based and semantic rankings improved results. Useful caution against assuming an LLM is automatically a better selector. |
| 7 | **Machine-Learned Premise Selection for Lean** — Piotrowski, Fernández Mir & Ayers, 2023 | [arXiv](https://arxiv.org/abs/2304.00994) | **Direct overlap.** An online random-forest model integrated into Lean’s `suggest_premises` tactic; demonstrates low-latency, proof-assistant-native premise recommendation. |
| 8 | **LeanDojo: Theorem Proving with Retrieval-Augmented Language Models** — Yang et al., NeurIPS 2023 | [arXiv](https://arxiv.org/abs/2306.15626) | **Direct overlap — especially close.** Extracts fine-grained premise annotations from Lean proofs and introduces ReProver, an LLM-based prover augmented with retrieval over a large math library. The paper explicitly identifies premise selection as a key bottleneck and evaluates retrieval-augmented proving. |
| 9 | **Magnushammer: A Transformer-Based Approach to Premise Selection** — Mikuła et al., ICLR 2024 | [arXiv](https://arxiv.org/abs/2303.04488) and [ICLR paper](https://proceedings.iclr.cc/paper_files/paper/2024/file/ab5f5f22e3e09f4424592ffb06840ab0-Paper-Conference.pdf) | **Direct overlap — especially close.** Contrastive transformer retrieval plus reranking for proof-state/premise pairs; reports strong gains over Sledgehammer and further gains when paired with an LM prover. Direct evidence that retrieval quality propagates to proof success. |
| 10 | **Towards Large Language Models as Copilots for Theorem Proving in Lean** — Song, Yang & Anandkumar, 2024 | [arXiv](https://arxiv.org/abs/2404.12534) | **Direct overlap.** Lean Copilot includes LLM-based premise selection alongside tactic suggestion and proof search, making proof-relevant context selection an interactive assistant function. |
| 11 | **Graph Sequence Learning for Premise Selection** — Holden & Korovin, Journal of Symbolic Computation 128 (2025) | [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0747717124000804) | **Direct overlap.** Generates sequences of axioms (“axiom captioning”) using graph-neural and language-model components to capture inter-axiom and conjecture-axiom relations; reports a 14% improvement in solved problems over baseline. |
| 12 | **Tree-Based Premise Selection for Lean4** — Wang, Dong & Wen, NeurIPS 2025 | [OpenReview/PDF](https://openreview.net/pdf?id=omyNP89YW6) | **Direct overlap.** Uses expression-tree structure, Weisfeiler–Lehman similarity, tree-edit distance, constant-node Jaccard similarity, and adaptive fusion to rank Lean premises. Strong structural analogue to argument-form-aware retrieval. |
| 13 | **Assisting Mathematical Formalization with A Learning-based Premise Retriever** — (arXiv 2501.13959), 2025 | [arXiv](https://arxiv.org/abs/2501.13959) | **Direct overlap.** Contrastive premise retrieval with a domain-specific tokenizer and fine-grained similarity; aimed at retrieving Mathlib theorems from proof states and supporting formalization. |
| 14 | **Learning an Effective Premise Retrieval Model for Efficient Mathematical Formalization** — 2025 | [OpenReview/PDF](https://openreview.net/pdf/ec313b0b95dba96e7bb145dc4a3b376cd9f4e8e1.pdf) | **Direct overlap.** Formal-state dense retrieval (CFR) followed by context-aware reranking (CAR), integrated into an augmented theorem-proving pipeline. Particularly relevant to selecting context using both the current proof state and premise structure. |
| 15 | **LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving** — Gao et al., 2026 | [arXiv](https://arxiv.org/abs/2605.13137) | **Direct overlap — closest current match.** Explicitly defines “global premise retrieval”: recovering a scattered set of lemmas needed for an entire theorem, rather than only one tactic step. Its reasoning mode uses sketch–retrieve–reflect cycles; reported retrieval and downstream proof-success gains make it a strong comparator for proof-relevant context selection. |
| 16 | **RECOMP: Improving Retrieval-Augmented LMs with Compression and Selective Augmentation** — Xu, Shi & Choi, ICLR 2024 | [arXiv](https://arxiv.org/abs/2310.04408) and [OpenReview](https://openreview.net/pdf?id=mlJLVigNHp) | **Adjacent, not direct.** Extractive and abstractive compressors select useful sentences from retrieved documents and can return an empty context when retrieval adds no value. It supplies a general selective-context objective, but is not proof-aware and does not preserve formal proof dependencies. |
| 17 | **LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models** — Jiang et al., EMNLP 2023 | [ACL Anthology](https://aclanthology.org/2023.emnlp-main.825/) | **Adjacent, not direct.** Token-level coarse-to-fine prompt compression with a budget controller and distribution alignment; evaluates reasoning-heavy datasets but does not identify proof-relevant premises or certify dependency preservation. |
| 18 | **LongLLMLingua: Accelerating and Enhancing LLMs in Long Context Scenarios via Prompt Compression** — Jiang et al., ACL 2024 | [ACL Anthology PDF](https://aclanthology.org/2024.acl-long.91.pdf) | **Adjacent, not direct.** Compresses long contexts while addressing key-information density and position bias; useful baseline for context-budget management, but selection is not argument- or proof-structure-aware. |

## Synthesis for the project

### What is already covered by prior work

1. **Premise selection is an established ATP/ITP bottleneck.** Papers 1–4, 7–15 repeatedly define the task as reducing a very large theorem/lemma library to a small set usable by a prover.
2. **Proof-relevant retrieval is not merely semantic similarity.** Graph/tree methods (2, 3, 11, 12) use formula or expression structure; LeanDojo/ReProver (8) uses accessible-premise analysis and hard negatives; formal-state retrievers (13, 14) condition on the current proof state.
3. **LLM reasoning is commonly downstream of selection.** The clearest pipeline is paper 5: retrieve ~8 premises from ~100K, then give them plus the proof state to an LM. LeanDojo/ReProver (8), Magnushammer (9), and Lean Copilot (10) reinforce this decomposition.
4. **Whole-proof/global retrieval is newer and more distinct.** LeanSearch v2 (15) explicitly targets the joint premise set for an entire theorem, contrasting with step-local premise selection. This is the nearest prior art for selecting context by proof-level relevance.
5. **Generic context compression is adjacent rather than equivalent.** RECOMP and LLMLingua-family methods optimize relevance, cost, or long-context perception, but they do not preserve a proof dependency graph, argument roles, theorem applicability conditions, or formal validity.

### Direct-overlap flags

- **Highest direct overlap:** 5 (Formal Premise Selection With Language Models), 8 (LeanDojo/ReProver), 9 (Magnushammer), 14 (Learning an Effective Premise Retrieval Model), and 15 (LeanSearch v2).
- **Direct structural overlap:** 2, 3, 11, and 12, because they use graph/tree/structural representations of mathematical statements or proof states.
- **Direct interactive-assistant overlap:** 7 and 10.
- **Adjacent context-compression overlap only:** 16–18. These are relevant to a context-budget or compression module, but not to proof-relevant selection unless augmented with dependency-aware constraints.

### Apparent novelty boundary

The literature supports a narrow novelty claim, not a broad “premise selection is new” claim: **a system that classifies argument/proof forms and selects a minimal, proof-relevant context using those form labels, while retaining enough structure for an LLM to reason, is not directly represented by the retained papers.** Existing direct-overlap systems primarily rank formal premises by goal/proof-state similarity, graph/tree structure, accessibility, or learned proof-use labels. Existing compression systems primarily remove tokens/sentences for cost and long-context performance. The unfilled combination is an explicit **argument-form → proof-obligation → context-selection policy**, ideally evaluated on proof success, dependency recall, and compression faithfulness rather than retrieval metrics alone.

## Verification notes and limitations

- All 18 retained items have a linked scholarly or first-party paper page/PDF and were checked for title/abstract/relevance; no citation is included solely from memory.
- Search results surfaced some 2026 records. Dates above are the publication/preprint years shown by the linked records as of **October 11, 2026**.
- “Proof-relevant retrieval” is not a uniformly standardized term in the literature; the report maps it to premise selection, proof-state retrieval, global premise retrieval, and retrieval-augmented theorem proving.
- Generic context compression papers are retained as adjacent comparators, not claimed as theorem-proving prior art.
