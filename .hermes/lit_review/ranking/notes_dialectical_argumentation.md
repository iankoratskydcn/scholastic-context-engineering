# Dialectical argumentation benchmark ranking

Scope: all 80 rows in `benchmark_studies.csv`; reviewer slug `dialectical_argumentation`.

Ranking prioritizes: explicit argument schemes and critical questions; support/attack or rebuttal relations; defeasible/implicit reasoning; objection/reply or debate-tree structure; diagnostic annotations and provenance.

Required separation:
- **Regulated dialogue:** none of supplied benchmarks fully implements scholastic quaestio/disputatio role semantics, fixed move legality, determination, and one-to-one replies. S23P04 and S23P05 are generic structured-debate analogues, not regulated dialogue.
- **Argumentation-direct:** QT-SCHEMES, Walton corpora, EthiX, complex argument trees, deep argumentative structures, and support/attack debate corpora.
- **Synthetic/formal logic:** ProofWriter, RuleTaker, LogicNLI, FOLIO, PrOntoQA, BIG-bench logic, syllogism sets, and LeanDojo provide deductive/proof controls but not authentic support/attack dialogue.
- **Adjacent controls:** long-context, RAG, cultural, philosophical, analogy, and scholastic NLP resources test infrastructure or transfer conditions; they should be combined with direct argumentation benchmarks.

Scores are 0–100; ties use numeric category and paper order, then literal paper ID.
