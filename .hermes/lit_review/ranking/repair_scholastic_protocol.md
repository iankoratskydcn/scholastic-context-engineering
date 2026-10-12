# Repair record: scholastic-protocol ranking

## Scope

Repaired `review_scholastic_protocol_category.csv` and `review_scholastic_protocol_global.csv` for the explicit medieval scholastic protocol:
`quaestio → objections → sed contra → respondeo/determination → distinctions → replies`.
Literal paper IDs and source order are preserved.

## Rubric

Scores measure protocol fit, not general importance, citation prestige, or broad reasoning usefulness.

- **Protocol-direct (70–100):** the source models a contestable question or formal dialogue with explicit challenge/response structure. Full credit requires named or operationally recoverable coverage of the stages; an analogue missing named stages is capped below the direct top tier.
- **Argumentation-adjacent (50–69):** typed claims, premises, attacks, rebuttals, schemes, deduction, or proof machinery transfers to objections/determination but does not implement the complete scholastic sequence.
- **Formal-historical (60–84):** historical logic or scholastic-domain formalization provides source-faithful or executable reasoning material. It is not promoted to full protocol fit unless stage coverage is explicit.
- **Infrastructure (30–52):** corpus, treebank, HTR, retrieval, context, compression, or knowledge-organization support. Useful upstream, but not itself a disputation protocol.
- **Generic (0–49):** thematic philosophy, hallucination, culture, or evaluation relevance without a concrete stage mechanism.

Each explanation identifies what is present and what is missing. Confidence is calibrated to that narrower claim; low scores can still have high confidence as negative-fit findings.

## Explicit overrides

- **S21P01** (*Scholastic*) is a sharply demoted false positive (score 5): its HCI interface name does not establish any of the six stages.
- **S23P01** is distinguished from generic debate/argumentation: it is the closest formal-dialogue analogue (score 82), but remains below a full protocol-direct item because the evidence does not establish named `sed contra`, `respondeo`, or reply-to-objection stages.
- The prior 100-point block is removed; generic Toulmin/defeasible-logic, argument-mining, and debate items are capped according to their actual stage coverage.

## Deterministic ranking

Category ranks sort by `score_0_100` descending, then `paper_order`, then literal `paper_id`. Global ranks sort by `score_0_100` descending, then numeric `category_num`, then numeric `paper_order`, then literal `paper_id`, matching the canonical tuple rule.

## Validation targets

Both CSVs must contain exactly 124 unique source IDs, scores in 0–100, unique ranks, non-empty explanations/evidence, matching non-ranking fields, and no edits outside the two CSVs and this repair record.
