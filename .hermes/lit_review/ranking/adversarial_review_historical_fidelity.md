# Adversarial review — historical-fidelity ranking

**Reviewed files**
- `review_historical_fidelity_category.csv`
- `review_historical_fidelity_global.csv`
- `remaining_nonbenchmark.csv`
- `ranking_protocol.md`

## Verdict: REVISE

The ranking artifacts pass structural and ordering checks, and the broad historical-fidelity ordering is substantively plausible. They do not yet satisfy the protocol's evidence/explanation-quality requirement because many rows use generic, non-pointing evidence and large groups reuse boilerplate explanations that do not identify the paper-specific feature driving the score.

## Blockers

### B1 — 40 rows have non-pointing generic `evidence_basis`

Both ranking files contain the same 40 rows whose evidence is exactly:

> source artifact describes a scholarly, formal, conceptual, survey, normative, or comparative study without a benchmark-producing artifact

This is a classification statement, not a pointer to a source summary or paper evidence. It fails the protocol requirement that `evidence_basis` point to source-summary/paper evidence rather than reviewer intuition alone. The affected rows include high-ranked historical-logics and defeasible-logic papers (`16_01`, `16_02`, `16_04`, `16_14`, `18_05`, `18_03`, `16_06`, `18_04`, `16_08`, `16_10`, `18_02`, `18_06`, `18_01`, `16_12`, `17_05`, `18_08`, `18_07`, `16_03`, `16_05`, `16_07`, `18_13`, `16_09`, `17_06`, `18_09`, `16_13`, `18_14`) and all 13 rows in category 20 (`20_01`–`20_13`). Replace each with a concrete summary section, source finding, or named methodological contribution.

### B2 — Explanation quality is materially boilerplate and not consistently paper-specific

The files have only 46 unique explanations for 124 papers. The most consequential repeated groups are:

- 11 category-18 papers share one sentence about defeasible/argumentation formalisms, despite differing in implementation, semantics, burden of proof, Toulmin theory, and argument mining.
- All 13 category-20 papers share one sentence and score 35, despite the summaries distinguishing authorship detection, factuality, citation fabrication, evaluator reliability, normative agency, and research-quality evaluation.
- 12 category-4 compression papers share one sentence, although the source summaries distinguish lexical pruning, query-aware compression, latent memory, protected spans, tool documentation, and example selection.
- 9 category-1 hallucination papers share one sentence even though their contributions range from taxonomy and definitions to audits, uncertainty, and mitigation.

These sentences often name a category-level feature, but do not meet the protocol's stronger requirement to name the concrete feature that drove each paper's individual rank. This also makes the fine-grained score differences difficult to audit. Rewrite explanations at paper level, especially for the repeated groups, and state why the item is above/below nearby papers under the historical-fidelity perspective.

## Non-blockers / passed checks

- Exactly 124 rows in each ranking file.
- Exact paper-ID coverage against `remaining_nonbenchmark.csv`; no missing, extra, or duplicate IDs.
- Metadata fields (`category_num`, `category`, `paper_order`, `citation`) match the source inventory for every row.
- `reviewer_slug` and `viewpoint` are consistent across all rows.
- Scores are integer-valued and within 0–100; observed range is 23–100.
- Category file has blank `global_rank`; global file has blank `category_rank`.
- Category ranks are unique and contiguous within every category; global ranks are unique and contiguous 1–124.
- Global ordering is score-descending and, for equal scores, follows canonical numeric category/paper order. There are no score inversions or rank-order violations.
- Category and global files agree on scores, explanations, evidence, and confidence for all 124 IDs.
- Explanations and evidence fields are non-empty; explanations are within the stated 1–3 sentence limit under a manual/rough sentence-count check.

## Historical-fidelity substance check

The high end is directionally well aligned with the viewpoint. The top sample prioritizes primary or formal reconstructions that preserve local concepts and procedures: `16_01` (*Prior Analytics*), `S23P01` medieval obligationes as formal dialogue, `S24P01` Avicennan proof search, `16_02` Corcoran's historically disciplined Aristotelian reconstruction, and `S24P02` al-Barakāt's logical diagrams. Their source summaries explicitly support provenance-preserving formalization, dialogue states/rules, executable proof search, and resistance to anachronistic translation.

The low end is also directionally plausible: `S04P11`–`S04P01` are context-compression methods whose summaries explicitly lack tradition-specific semantics and inspectable argument/provenance preservation; `20_01`–`20_13` concern academic prose, authorship, citation fabrication, or evaluation safeguards rather than historical logic modeling. The concern is not their low placement, but the unsupported uniformity of the category-20 score/explanation and the generic evidence basis.

No clear numerical ranking defect was found. The principal risk is auditability: a reviewer cannot tell whether close score distinctions reflect actual paper-level historical-fidelity judgments or category-template assignment.

## Sampled IDs and evidence

| ID | Rank/score | Evidence checked | Result |
|---|---:|---|---|
| `16_01` | global 1 / 100 | `16_historical_logics_summaries.md` §1: source-layer treatment, syllogistic vocabulary, proof practice, preservation of textual/translation uncertainty | Substantively justified, but evidence field in CSV is generic and must be repaired |
| `S23P01` | global 2 / 100 | `23_disputatio_dialectical_ai_summaries.md` §1: positum, Opponent/Respondent rules, dialogue states, terminal evaluation | Strong direct fit; paper-specific CSV evidence is adequate |
| `S24P01` | global 3 / 99 | `24_islamic_comparative_scholastic_ai_summaries.md` §1: Avicennan proof-search states/transitions formalized as an Abstract State Machine | Strong direct fit; paper-specific CSV evidence is adequate |
| `18_05` | global 8 / 96 | No paper-specific evidence in CSV; category-18 summary record supports defeasible/argumentation relevance but the explanation/evidence are generic | Plausible placement, insufficient audit trail |
| `S10P02` | global 61 / 75 | Category-level Walton-scheme explanation; source evidence only says foundational taxonomy | Plausible adjacent fit, but explanation should identify scheme/critical-question contribution |
| `20_06` | global 97 / 35 | `20_ai_academic_writing_summaries.md` §6: Thelwall's repeated GPT-4 research-quality evaluations and weak/stability-sensitive correlations | Low placement plausible, but same score/explanation as unrelated authorship/citation studies is under-justified |
| `20_11` | global 109 / 35 | `20_ai_academic_writing_summaries.md` §11: fabricated/inaccurate references and claim-level citation-integrity warning | Low placement plausible, but its evidence field is generic and does not mention this concrete finding |
| `S04P11` | global 124 / 23 | `04_context_compression_summaries.md` §11: recurrent KV-memory compression, opaque internal state, no inspectable proposition/provenance retention | Low placement directionally justified; explanation remains category boilerplate |

## Required revision

1. Replace all 40 generic evidence fields with concrete source-summary sections or paper findings.
2. Rewrite repeated explanations at paper level, beginning with categories 20, 18, 4, and 1.
3. Preserve the current IDs, row counts, score range, unique ranks, and canonical tie ordering unless the paper-specific evidence reveals a substantive score change.
4. Re-run the same structural checks after revision and spot-check high, middle, and low ranks again.
