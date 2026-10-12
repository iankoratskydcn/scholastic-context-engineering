# Cross-source synthesis benchmark gap search

## Scope
Search target: benchmarks or reusable evaluation resources for constructing a new argument/hypothesis by combining premises or evidence from multiple unrelated documents/authors. Adjacent resources were retained when they expose a necessary subtask: cross-document evidence aggregation, source attribution, synthesis-vs-copy diagnostics, or best-explanation selection.

Protocol read: `.hermes/lit_review/ranking/gap_benchmark_search_protocol.md`.

## Search coverage
Queries run on 2026-10-12 included:

- `scholarly benchmark cross-document argument synthesis multiple sources novel argument`
- `benchmark multi-document synthesis evidence aggregation argument generation dataset`
- `benchmark combining evidence from multiple unrelated documents reasoning`
- `scientific literature multi-document summarization synthesis benchmark novel hypothesis`
- `cross-document reasoning benchmark entity relation multi-hop evidence`
- `argument synthesis benchmark premises from multiple documents NLP`
- `multi-source question answering benchmark supporting evidence documents scholarly`
- `benchmark literature-based discovery hypothesis generation multiple papers`

## Results
- 11 records retained after screening.
- Direct gap fills: SEAMuS/CDEKS, FAMuS, MDA-QA, ResearchBench.
- Strong adjacent resources: M3SciQA, DiscoveryBench, MultiHop-RAG, RoMQA, WikiHowQA, multi-document synthesis evaluation, and cross-document relation extraction.
- No located benchmark fully combines unrelated scholarly sources, attributed premise extraction, explicit argument/warrant/proof skeletons, and open-ended novel thesis generation in one artifact. This is an evidence-backed gap statement, not a claim that no such resource exists.
- The strongest design pattern is compositional: use MDA-QA or M3SciQA for multi-paper dependence, SEAMuS/FAMuS for inspectable cross-source argument/event alignment, ResearchBench for inspiration-to-hypothesis composition, and MultiHop-RAG/cross-document RE for evidence-path retrieval.

## Failed, blocked, or incomplete searches
- Exact phrase `argument synthesis benchmark premises from multiple documents NLP` returned no direct scholarly benchmark in the search results; results were broadened to cross-document relation extraction, multi-document QA, and scientific hypothesis benchmarks.
- `web_extract` was unavailable in this runtime because the configured OpenAI native backend is search-only; evidence was therefore retained from official ACL/arXiv search records and opened landing-page metadata where available.
- A candidate abductive-syllogism record found in the existing local benchmark matrix was not retained because its exact scholarly landing page and artifact identity were not independently re-opened during this sweep.
- Artifact access and license were not inferred from paper access. Rows mark these fields as unverified where the official source did not explicitly establish them.

## Evidence and limitations
The direct candidates still fall short of the complete target: SEAMuS/FAMuS focus on event frames and cross-source argument extraction; MDA-QA and M3SciQA are QA-shaped; ResearchBench evaluates inspiration retrieval and hypothesis composition but does not require explicit premise-to-warrant proof structures. The remaining rows are controls or reusable components rather than end-to-end matches.

Duplicate/version note: SEAMuS is a cross-document extension/reannotation related to FAMuS; treat them as one benchmark family, not independent evidence of two complete solutions. ResearchBench is tracked by arXiv identity because the search surfaced the preprint and repository; verify final venue/version before master-matrix merge.
