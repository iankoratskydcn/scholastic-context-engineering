# Long-context benchmark ranking notes

- Scope: all 80 rows in `benchmark_studies.csv`; benchmark identity fields preserved literally.
- Ranking lens: direct context-length/position/semantic-retrieval stress first; then multi-piece or proof-relevant dependency selection; then generic reasoning/grounding; unrelated corpus resources last.
- Key distinction: LongBench/LRA/∞Bench/RULER/NoLiMa/LongPiBench are generic or controlled long-context stressors. LeanDojo/ReProver and Isabelle premise pairs are dependency-aware selection benchmarks with exact proof feedback, but formal-library rather than scholarly-prose inputs.
- Highest direct stress: LongPiBench, NoLiMa, RULER, LongBench, ∞Bench, LRA. Highest proof/selection transfer: LeanDojo/ReProver, LeanDojo, Isabelle premise pairs, ProofWriter, FOLIO, MultiHop-RAG, AnaloBench.
- Limit: retained summaries support paper-specific task properties, but do not establish verified artifact access/licensing for every benchmark.
