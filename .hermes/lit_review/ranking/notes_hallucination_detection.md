# Hallucination / invalid-inference benchmark ranking

Perspective: direct detection of unsupported premises, hallucinated facts, invalid entailments, fallacies, and unfaithful inference traces. Generic QA, retrieval, culture, and corpus utility receive low scores unless benchmark has explicit support/fallacy/proof labels.

Top direct fits: PCBench, FalseQA, KG-FPQ, ProofWriter, RuleTaker, SMARTYPAT-BENCH, LogicNLI, FOLIO, SylloBase, PrOntoQA.

Caveats: synthetic rule/proof suites isolate inference well but do not establish real-world factuality; RAG/citation suites detect unsupported content but may not localize invalid reasoning; argument-scheme corpora expose structure/implicit warrants without truth labels.

Input rows: 80. Output rows: 80. Global ranks: 1–80.
