# Literature Review Agent 04 — Context Engineering, Context Compression, Prompt Compression

## Required fields
- **Topic:** Context engineering for LLM reasoning: prompt/context compression, selective context, latent-memory compression, and reasoning-relevant context selection.
- **Research question:** Which methods reduce the context supplied to an LLM while preserving task-relevant information, and which methods specifically extract or classify logical/argument structure before selecting context?
- **Scope:** Primary papers only; emphasis on methods that compress, select, or encode inference-time context. Generic model/weight compression, ordinary summarization, and retrieval-only methods are excluded except where needed for novelty analysis.
- **Search date:** 2026-10-11.
- **Paper count:** 12 verified papers.
- **Verification standard:** Each paper below was opened at its arXiv, ACL Anthology, NeurIPS, ICLR, or OpenReview paper page/PDF; links are DOI or Google Scholar links, not search snippets.

## Search variants (Scholar-first)
1. `"prompt compression" large language model`
2. `"context compression" LLM`
3. `"compressing prompts" LLM inference`
4. `"long context" "prompt compression"`
5. `"selective context" language model`
6. `"gist tokens" prompt compression`
7. `"soft prompt" context compression`
8. `"retrieval" "compression" language model context`
9. `"argument structure" extraction context selection reasoning LLM`
10. `"argument component selection" language models reasoning`

## Verified primary papers

### 1. LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models
- **Authors/year:** Jiang, Wu, Lin, Yang, Qiu (2023).
- **Link:** [Google Scholar](https://scholar.google.com/scholar?q=%22LLMLingua%3A+Compressing+Prompts+for+Accelerated+Inference+of+Large+Language+Models%22)
- **What it does:** Coarse-to-fine prompt compression with a budget controller, iterative token-level compression, and instruction tuning for distribution alignment.
- **Reasoning relevance:** Compression is not merely length truncation: token interdependence and a budget are modeled to preserve downstream task behavior, including reasoning prompts.
- **Limitation/overlap:** Selection is token/likelihood based; it does not first recover an explicit argument graph, proof structure, claims, premises, or logical dependencies.

### 2. LongLLMLingua: Accelerating and Enhancing LLMs in Long Context Scenarios via Prompt Compression
- **Authors/year:** Jiang et al. (2023; ACL 2024 publication).
- **Link:** [Google Scholar](https://scholar.google.com/scholar?q=%22LongLLMLingua%3A+Accelerating+and+Enhancing+LLMs+in+Long+Context+Scenarios+via+Prompt+Compression%22)
- **What it does:** Query-aware coarse/fine compression, document reordering, dynamic compression ratios, and subsequence recovery.
- **Reasoning relevance:** Explicitly targets key-information density, position bias, long-context QA, multi-document reasoning, and CoT-like contexts.
- **Limitation/overlap:** The importance signal is query-conditioned model likelihood/contrastive perplexity; it is not an explicit logical-form or argument-structure extractor.

### 3. LLMLingua-2: Data Distillation for Efficient and Faithful Task-Agnostic Prompt Compression
- **Authors/year:** Pan et al. (2024).
- **Link:** [Google Scholar](https://scholar.google.com/scholar?q=%22LLMLingua-2%3A+Data+Distillation+for+Efficient+and+Faithful+Task-Agnostic+Prompt+Compression%22)
- **What it does:** Distills an LLM into a smaller bidirectional encoder that performs token classification for extractive compression; trains on an LLM-derived compression dataset.
- **Reasoning relevance:** This is the clearest learned *classification* formulation in the compression set: each token is retained or removed using full bidirectional context and an end-task-oriented distillation target.
- **Limitation/overlap:** The labels are token-retention decisions, not argument roles or logical relations. It therefore overlaps at the decision layer (classification before selection), but not at the representation layer required by explicit argument-skeleton extraction.

### 4. RECOMP: Improving Retrieval-Augmented LMs with Compression and Selective Augmentation
- **Authors/year:** Xu, Shi, Choi (2023; ICLR 2024).
- **Link:** [Google Scholar](https://scholar.google.com/scholar?q=%22RECOMP%3A+Improving+Retrieval-Augmented+LMs+with+Compression+and+Selective+Augmentation%22)
- **What it does:** Trains extractive and abstractive compressors using downstream LM performance; can return an empty string when retrieved evidence is unhelpful.
- **Reasoning relevance:** End-task supervision directly teaches the compressor what retrieved evidence helps the generator, and selective augmentation avoids adding distractors.
- **Limitation/overlap:** Extractive selection is sentence-level and abstractive compression is summary generation; neither explicitly extracts claims, premises, warrants, supports/attacks, or a logical skeleton.

### 5. Compressing Context to Enhance Inference Efficiency of Large Language Models (Selective Context)
- **Authors/year:** Li, Dong, Lin, Guerin (2023; EMNLP 2023).
- **Link:** [DOI](https://doi.org/10.18653/v1/2023.emnlp-main.391)
- **What it does:** Prunes redundant tokens, phrases, or sentences using lexical-unit surprisal/information criteria; evaluates long papers, news, and conversations.
- **Reasoning relevance:** Provides a model-agnostic baseline for reducing irrelevant context while preserving generation quality and faithfulness.
- **Limitation/overlap:** Redundancy/information pruning is not reasoning-structure extraction. It can remove a locally low-surprisal premise that is globally essential to an argument.

### 6. Adapting Language Models to Compress Contexts (AutoCompressors)
- **Authors/year:** Chevalier, Wettig, Ajith, Chen (2023; EMNLP 2023).
- **Link:** [Google Scholar](https://scholar.google.com/scholar?q=%22Adapting+Language+Models+to+Compress+Contexts%22)
- **What it does:** Fine-tunes LMs to turn long segments into compact summary vectors/soft prompts, recursively conditioning later segments on prior compressed memory.
- **Reasoning relevance:** Tests compressed demonstrations, retrieval-augmented LM use, and passage reranking; demonstrates latent context can substitute for raw text.
- **Limitation/overlap:** Latent vectors provide no inspectable argument units or provenance. The method is representational compression, not explicit extraction followed by context selection.

### 7. In-context Autoencoder for Context Compression in a Large Language Model (ICAE)
- **Authors/year:** Ge, Hu, Wang, Wang, Chen, Wei (2023; ICLR 2024).
- **Link:** [Google Scholar](https://scholar.google.com/scholar?q=%22In-context+Autoencoder+for+Context+Compression+in+a+Large+Language+Model%22)
- **What it does:** Adds a lightweight compressor that maps long context into compact memory slots directly usable by the base LLM; combines autoencoding/language-modeling pretraining with instruction tuning.
- **Reasoning relevance:** Shows a practical latent-memory route with low parameter overhead and measurable latency/GPU-memory benefits.
- **Limitation/overlap:** Memory slots are opaque and not argument/logical forms. No explicit claim-premise relation extraction or selective retention stage is reported.

### 8. Learning to Compress Prompts with Gist Tokens
- **Authors/year:** Mu et al. (2023; NeurIPS 2023).
- **Link:** [Google Scholar](https://scholar.google.com/scholar?q=%22Learning+to+Compress+Prompts+with+Gist+Tokens%22)
- **What it does:** Trains models to encode prompts into a small number of learned gist tokens, achieving large prompt-length reductions while preserving task behavior.
- **Reasoning relevance:** Establishes a reusable prompt-compression primitive for few-shot demonstrations and repeated instructions, with decoder and encoder-decoder evaluations.
- **Limitation/overlap:** The gist representation is learned end-to-end; it does not classify argument components or select context based on a symbolic/logical intermediate representation.

### 9. SelfCP: Compressing Over-Limit Prompt via the Frozen Large Language Model Itself
- **Authors/year:** Gao, Cao, Li (2024).
- **Link:** [Google Scholar](https://scholar.google.com/scholar?q=%22SelfCP%3A+Compressing+Over-Limit+Prompt+via+the+Frozen+Large+Language+Model+Itself%22)
- **What it does:** Uses the target frozen LLM plus a small connector/learnable embeddings to convert over-limit prompt regions into dense memory tokens while leaving allowed prompt text unmodified.
- **Reasoning relevance:** Hybrid compression preserves a local raw context window and compresses overflow, making it relevant to context engineering under hard limits.
- **Limitation/overlap:** Compression boundaries are positional/overflow-driven, not derived from argument or logical structure; dense tokens are opaque.

### 10. Concise and Precise Context Compression for Tool-Using Language Models
- **Authors/year:** Xu et al. (2024; Findings of ACL 2024).
- **Link:** [DOI](https://doi.org/10.18653/v1/2024.findings-acl.974)
- **What it does:** Combines selective retention of exact tool/parameter names with block-wise soft compression of documentation and variable compression ratios.
- **Reasoning relevance:** Demonstrates a mixed strategy: preserve execution-critical spans verbatim, compress explanatory material into soft representations.
- **Limitation/overlap:** The retained units are schema-critical identifiers, not argumentative units. This is a useful design analogy for preserving reasoning-critical claims/propositions exactly, but not evidence of argument-aware compression.

### 11. Compressed Context Memory for Online Language Model Interaction
- **Authors/year:** Kim, Yeom, Yun, Song (2023; ICLR 2024).
- **Link:** [Google Scholar](https://scholar.google.com/scholar?q=%22Compressed+Context+Memory+for+Online+Language+Model+Interaction%22)
- **What it does:** Recursively compresses attention key/value memory during online interaction using a conditional LoRA, enabling streaming/unbounded context with substantially smaller memory.
- **Reasoning relevance:** Targets multi-turn and streaming context engineering rather than one-shot prompt rewriting; useful for persistent context state.
- **Limitation/overlap:** KV compression occurs inside the model state and has no explicit extract/classify/select argument pipeline or user-auditable provenance.

### 12. Effective In-Context Example Selection through Data Compression
- **Authors/year:** (Findings of ACL 2024).
- **Link:** [DOI](https://doi.org/10.18653/v1/2024.findings-acl.50)
- **What it does:** Frames few-shot example selection as data compression, selecting a compact set of demonstrations that preserves task-relevant information.
- **Reasoning relevance:** Directly concerns context selection rather than token deletion and is relevant to choosing a minimal reasoning scaffold.
- **Limitation/overlap:** It compresses the *example set*; it does not extract argument/logical forms from each example before selection.

## Dedicated novelty-threat analysis: argument/logical-form extraction before context selection

### Threat definition
A true overlap would require a pipeline with both stages:
1. **Structure extraction/classification:** identify argument or logical units (e.g., claims, premises, warrants, evidence, support/attack relations, proof steps, predicates, or a formal program); and
2. **Context selection/compression:** retain, summarize, or serialize only the structure/components needed by a downstream LLM reasoning step.

### Closest adjacent primary work (not counted as compression papers)
- **ECASE: Enhancing Argument Structure Extraction with Efficient Leverage of Contextual Information** (Luo et al., Findings EMNLP 2023). [DOI](https://doi.org/10.18653/v1/2023.findings-emnlp.507) — explicitly models argumentative information and avoids over-attending to uninformative contextual sentences, but its goal is argument-structure extraction, not compressing a context for a separate downstream LLM reasoner.
- **Harnessing Toulmin’s theory for zero-shot argument explication** (Gupta, Zuckerman, O’Connor, ACL 2024). [DOI](https://doi.org/10.18653/v1/2024.acl-long.552) — prompts an LLM to output claim–reason–warrant triples, which is highly relevant to an argument-skeleton intermediate representation, but does not propose a subsequent context-compression/selection system for reasoning.
- **Natural Language Reasoning in Large Language Models: Analysis and Evaluation** (Gemechu et al., Findings ACL 2025). [DOI](https://doi.org/10.18653/v1/2025.findings-acl.192) — formalizes argument-component selection and evaluates LLM limitations on argumentative reasoning; this is an evaluation/selection task, not a deployed prompt-compression pipeline.

### True overlap vs generic compression
- **Generic compression (most of the 12 papers):** selects tokens/sentences by likelihood, surprisal, redundancy, task loss, or learned latent encodings. These methods may preserve semantics or end-task accuracy, but they do not expose or operate over an argument/logical representation.
- **Partial overlap:** LLMLingua-2 is a token-classification compressor; RECOMP has learned sentence selection; LongLLMLingua is query-aware selection; the tool-documentation paper preserves exact execution-critical spans. These establish precedents for classification, query-conditioned selection, and protected spans, but not for argument-structure extraction.
- **True overlap found:** no verified primary paper in the reviewed set combines explicit claim/premise/warrant or logical-form extraction with a downstream context-compression/selection stage whose purpose is to support LLM reasoning. The closest components exist separately: argument-structure extraction/explication on one side and prompt/context compression on the other.
- **Novelty implication:** A system that extracts an inspectable argument skeleton, scores/selects its reasoning-critical components, preserves provenance, and then emits a compact LLM context would be differentiated from latent-memory compression and token/sentence pruning. The novelty claim should be narrowed to the *composition and reasoning-oriented selection objective*, not to compression alone.
- **Main threat to novelty:** if the proposed system only classifies tokens/sentences as useful and produces a shorter prompt, LLMLingua-2, LongLLMLingua, RECOMP, and Selective Context are strong prior art. The argument/logical intermediate representation and explicit preservation of inferential dependencies must be central and experimentally ablated.

## Synthesis for the project
1. **Compression families:** (a) lexical extractive pruning; (b) query/task-aware token or sentence selection; (c) abstractive textual summaries; (d) learned latent/soft-token memory; (e) recurrent KV-memory compression; and (f) example-set selection.
2. **Reasoning-sensitive design requirements:** query awareness, protection of dependency-bearing spans, preservation of negation/numerical qualifiers, provenance back to source spans, and evaluation on compositional/multi-hop reasoning—not only semantic similarity or summarization metrics.
3. **Recommended project distinction:** represent each source as a compact argument skeleton (claim/premise/warrant/evidence plus support/attack or dependency edges), rank components against the task, then serialize selected components with source-span pointers. Compare against LLMLingua-2, LongLLMLingua, RECOMP, Selective Context, and a summarizer; ablate structure extraction, edge preservation, and provenance.
4. **Evaluation warning:** reported compression ratios are not directly comparable because papers vary in tokenization, latent-token accounting, preprocessing cost, and whether compressor latency is included in end-to-end latency.

## Failed searches / negative results
- `"argument-aware prompt compression"` — no directly matching primary paper located in the reviewed Scholar/arXiv/ACL results.
- `"logical form context compression LLM"` — returned logical-form generation and semantic parsing papers, but no verified system that compresses context after extracting logical forms for downstream LLM reasoning.
- `"argument skeleton prompt compression"` — no directly matching primary paper located.
- `"claim premise warrant context compression"` — returned argument mining/explication papers, but no compression pipeline combining them with prompt compression.
- `"proof compression prompt context language model"` — returned chain-of-thought and proof-generation work, not a verified context-selection compressor based on extracted proof structure.
- `"reasoning-aware prompt compression"` — results were mostly generic prompt compression or recent/unverified preprints; no additional established primary system met the inclusion criteria.
- Searches for vendor/product terminology such as `context compaction API`, `agent memory compression`, and `LLM conversation summarization` were excluded as non-academic/system documentation rather than primary papers.

## Evidence and limitations
- All 12 counted papers were opened on a primary paper page or PDF and their abstracts/method descriptions were read. The novelty-threat adjacent papers were also opened on ACL Anthology pages.
- Several arXiv records have later conference versions; the Scholar links are used as stable discovery links, while DOI links are used where the proceedings exposed a DOI.
- No claim is made that the negative-result searches prove nonexistence; they indicate that no qualifying paper was found under the stated variants and scope.
