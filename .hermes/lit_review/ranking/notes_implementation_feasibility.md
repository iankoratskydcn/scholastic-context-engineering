# Implementation/access feasibility review

- Scope: all 80 rows in `benchmark_studies.csv`; reviewer slug `implementation_feasibility`.
- Score meaning: solo-run feasibility, not scientific importance. Dimensions: artifact/access certainty, license clarity, format, tooling, compute, annotation burden, reproducible metrics, controlled-experiment ease.
- Paper availability separated from benchmark artifact access. Source rows often prove only that a paper introduces or uses a benchmark; absent artifact/license evidence is treated as unverified and lowers confidence/score.
- Highest-feasibility families: RuleTaker/ProofWriter/FOLIO/LogiQA/SylloBase, FalseQA, ALCE/RAGTruth/MultiHop-RAG, LongBench/RULER, and compact argument-scheme resources such as QT-SCHEMES.
- Main blockers: Lean/Isabelle environments, ultra-long-context compute, subjective human/judge protocols, specialist Medieval Latin/Classical Arabic preprocessing, multimodal inputs, and unclear artifact licensing.
- Duplicate benchmark families remain separate rows per protocol (for example ProofWriter, LeanDojo, QT-SCHEMES).
- Self-validation: 80/80 source rows covered; global ranks 1–80; category ranks contiguous; no source identifiers merged.
