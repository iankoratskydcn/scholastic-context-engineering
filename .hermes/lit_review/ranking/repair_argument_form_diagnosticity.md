# Repair / notes — Argument-form and deductive-skeleton diagnosticity

- Ranked all 80 literal benchmark-study rows from `benchmark_studies.csv`; no IDs merged.
- Score priority: explicit argument schemes/components and proof/dependency traces; then diagnostic controls, authentic text, and feasibility.
- Formal/synthetic benchmarks remain valuable for isolated deductive-skeleton tests but are discounted for transfer to authentic scholastic prose.
- Long-context, generic RAG, cultural, OCR/POS, and generic QA resources are boundary controls unless they expose recoverable argument structure.
- QT-SCHEMES, Walton-scheme corpora, EthiX, FOLIO, argument-tree resources, ProofWriter, LogicNLI, and LeanDojo lead for this perspective; each differs in authenticity versus formal skeleton control.
- Output schema includes protocol-required benchmark identity fields plus reviewer fields.
- Validation: 80 input rows, 80 category rows, 80 global rows; global ranks 1–80; category ranks contiguous within each category; scores constrained to 0–100; JSON parses.
