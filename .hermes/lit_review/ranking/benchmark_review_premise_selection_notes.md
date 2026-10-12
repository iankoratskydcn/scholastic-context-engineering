# Premise-selection ranking notes

Scope: all 80 benchmark studies. Viewpoint ranks direct ability to test proof-relevant premise/evidence selection, necessary/sufficient/redundant facts, distractor control, and dependency preservation.

## Distinctions
- Formal-library retrieval: LeanDojo/ReProver, LeanDojo, and Isabelle premise pairs are strongest direct retrieval analogues; kernel/proof checking does not equal natural-language evidence selection.
- Natural-language evidence selection: MultiHop-RAG, FOLIO, ALCE, and RAGTruth test support integration, grounding, citation, or premise validity, but vary in explicit minimality.
- Synthetic proof controls: ProofWriter, RuleTaker, PrOntoQA, and LogicNLI expose necessary facts, distractors, depth, and proof dependencies with weaker scholarly authenticity.
- Adjacent context/argument resources: long-context, argument mining, debate, and scholarly corpora support stress tests or data construction but do not themselves prove minimal sufficient context.

## Verification
- Input rows: 80; category/global outputs: 80 each.
- Exact paper-ID set preserved; no duplicate IDs.
- Category ranks contiguous within category; global ranks 1–80.
- Scores integer 0–100; global order descending score with protocol tie-break `(numeric category_num, numeric paper_order, literal paper_id)`.
- Explanations/evidence non-empty; formal-library and natural-language regimes explicitly separated.
