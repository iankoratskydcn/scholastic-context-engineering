# Novelty-threat ranking repair

## Scope and semantics

- Preserved the CSV schema and every literal `paper_id`.
- Added explicit classification in `viewpoint`: `adjacent novelty threat` for component-level overlap and `background novelty threat` for conceptual, foundational, historical, or enabling work.
- Reserved `direct novelty threat` for a source that implements the same integrated system boundary. No retained source met that stricter end-to-end criterion in this repair.
- Replaced category boilerplate with paper-specific evidence drawn from the corresponding numbered section of each summary artifact, followed by an explicit limitation.

## Score calibration

Scores now express threat to the integrated scholastic context-engineering claim, not merely importance of an isolated component. Strong adjacent comparators remain high but are no longer presented as direct duplication. In particular: `S04P03=90`, `S21P05=88`, `S23P01=82`, `S21P01=8`, `S22P03=14`, and all `16_*` historical-logic rows are background scores from 8–11 reflecting formal or historical usefulness without an LLM context-engineering implementation.

## Ranking integrity

Recomputed `category_rank` and `global_rank` from numeric `score_0_100` descending order, with ties broken by `(numeric category_num, numeric paper_order, literal paper_id)` as required by `ranking_protocol.md`. The category file remains in canonical category/paper order; the global file is rank ordered.
