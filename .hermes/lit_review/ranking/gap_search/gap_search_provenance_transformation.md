# Gap search: provenance retention through text transformations

Date: 2026-10-12

## Scope and protocol

Target gap: benchmarks that preserve or measure source-span, citation, claim, or dependency lineage across extraction, summarization, selection, compression, and final generation. The search followed the repository protocol in `ranking/gap_benchmark_search_protocol.md`: scholarly identity and benchmark/resource mechanism were required; paper-only claims were not treated as artifact evidence; adjacent controls were retained when they clarify the gap.

Search routes: ACL Anthology, arXiv, official project/repository pages, and web search for provenance, attribution, citation, summarization faithfulness, RAG, source tracing, and compression. Search date: October 12, 2026.

## Results

The CSV contains 11 records: 5 strong/direct provenance or attribution resources (TROVE, AttributionBench, ALCE, KILT, RAGTruth), 2 direct/near-direct transformation studies (Attribution–Compression Frontier and Traceable Text), 2 useful atomic/semantic controls (FActScore and FEQA), 1 factuality control (FRANK), and 1 unresolved search lead (FaithJudge) retained solely to preserve the failure trail.

### Highest-value direct or near-direct resources

1. **TROVE** is the closest match for fine-grained output-to-source lineage: it traces generated sentences to source sentences and classifies the relation. It does not yet cover a controlled chain of extraction → selection → compression → generation.
2. **The Attribution–Compression Frontier** is the closest match for the requested transformation path. Its stated comparison includes reranking, extractive selection, abstractive summarization, and token pruning, with citation attribution measured across budgets. It is a 2026 preprint and artifact/reproducibility status remains unresolved.
3. **AttributionBench** evaluates claim-level support by cited evidence and is a reusable final-stage attribution testbed, but does not represent lineage as a multi-stage graph.
4. **ALCE** evaluates retrieval plus cited answer generation, including citation correctness/completeness. It is strong for the final generation boundary, weaker for intermediate transformations.
5. **KILT** makes provenance a first-class output/evaluation object using a fixed knowledge snapshot and supporting passage IDs. It is primarily retrieval/task provenance, not arbitrary text transformation lineage.
6. **RAGTruth** provides word- and case-level unsupported/contradictory span annotations in RAG outputs. It is a strong failure-localization resource, but mostly labels provenance loss rather than preserving positive lineage links.
7. **Traceable Text** provides phrase-level provenance links and human-auditability framing for summaries, but is an interaction/evaluation resource rather than a broad benchmark suite.

### Controls that should not be mistaken for lineage benchmarks

- **FActScore** decomposes outputs into atomic facts and verifies support. It is useful as a claim layer, but it does not preserve source identity or transformation ancestry.
- **FRANK** and **FEQA** test factual consistency/faithfulness of summaries. A summary can pass these tests while losing exact source-span or citation lineage, so they are controls for semantic faithfulness rather than provenance retention.

## Gap diagnosis

No located benchmark spans the full requested pipeline with a common example-level lineage graph linking: source extraction spans → selected evidence units → compressed representation → generated claims → final citations. Existing resources cluster at two endpoints:

- **Retrieval/final answer:** KILT, ALCE, AttributionBench, RAGTruth.
- **Summary/source relation:** TROVE, Traceable Text, FRANK, FEQA.
- **Compression intervention:** Attribution–Compression Frontier, currently preprint-level evidence.

The missing benchmark design is therefore a transformation-chain suite with fixed source documents, gold extraction spans, selection masks, multiple compression operators, claim-level output annotations, citation/span links, and per-stage conservation metrics. The suite should separately score (a) semantic entailment, (b) exact source-span recoverability, (c) citation correctness/completeness, and (d) dependency/claim lineage continuity. Existing factuality metrics alone are insufficient because they can reward a correct paraphrase that is no longer auditable to the original span.

## Failed, blocked, and unresolved searches

- A search lead named **FaithJudge** appeared relevant to RAG faithfulness, but no stable official scholarly page, authorship, identifier, or artifact was successfully opened. It is retained as `PT06` with `benchmark_status=uncertain`; do not rank or implement it until independently verified.
- For the 2026 **Attribution–Compression Frontier**, the official arXiv paper page was found, but no verified code/data artifact was established during this pass. Artifact access and license are therefore explicitly marked unresolved/not verified.
- For all resources, paper access was not treated as evidence of dataset/code license. The CSV records license status as `not verified` unless a license artifact was directly checked.

## Source URLs consulted

- https://aclanthology.org/2025.acl-long.577/
- https://aclanthology.org/2024.findings-acl.886/
- https://aclanthology.org/2023.emnlp-main.398/
- https://aclanthology.org/2021.naacl-main.200/
- https://aclanthology.org/2024.acl-long.585/
- https://aclanthology.org/2023.emnlp-main.741/
- https://aclanthology.org/2020.emnlp-main.173/
- https://aclanthology.org/2020.acl-main.173/
- https://arxiv.org/abs/2609.14245
- https://arxiv.org/abs/2409.13099
- https://github.com/declare-lab/TROVE
- https://github.com/OSU-NLP-Group/AttributionBench
- https://github.com/princeton-nlp/ALCE
- https://github.com/facebookresearch/KILT
- https://github.com/ParticleMedia/RAGTruth
- https://github.com/shmsw25/FActScore
- https://github.com/amazon-science/summary-reference-free-evaluation
- https://github.com/EdinburghNLP/faithful-summ

## Evidence status

Evidence level: **probable/high for the eight ACL/arXiv-identified resources with opened scholarly identities; medium for the 2026 compression preprint because artifact access is unresolved; low/unproven for the unresolved FaithJudge lead**. No claim is made that the list is exhaustive.
