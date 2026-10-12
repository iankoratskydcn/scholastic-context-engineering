# Dialectical-AI ranking repair

## Scope

Repaired only `review_dialectical_ai_category.csv`, `review_dialectical_ai_global.csv`, and this repair record. Protocol and all other ranking files were left untouched.

## Changes

- Rewrote all 124 explanations with an explicit typed directness label: `protocol-direct`, `argumentation-adjacent`, `infrastructure-adjacent`, or `generic`.
- Distinguished regulated interactive disputation from adjacent support/attack graphs, argument schemes, generic debate, corpus/provenance resources, and formal proof/search.
- Qualified `S21P05` and `S21P06` as strong generic support/attack or structured-dialogue analogues lacking the full quaestio, objection, distinction, determination, and ordered-reply sequence.
- Added the `S23P03` versus `S23P02` rationale: S23P03 remains higher for current chatbot applicability, while S23P02 is at least co-equal on protocol directness because of its locutions, commitment, critical-question, and termination rules.
- Preserved all scores, IDs, metadata, and rank fields because the evidence supported the existing numerical ordering and no score change was necessary.

## Verification

- Both CSVs contain 124 rows and the same 124 unique IDs as before.
- Scores remain integers in 0–100; category/global ranks remain unique and contiguous.
- Category and global row ID sets are unchanged and explanations are identical by ID across both files.
- Every explanation contains exactly one typed directness label and is non-empty.
- No files outside the two target CSVs and this repair record were modified.
