# Final relevance adjudication

Scope: 18 identity-pass aggregate-top papers. Identity failures `18_03`, `18_02` excluded. Rankings, identity artifacts, master matrix unchanged.

Rule: `retain_high` only when both reviewers support concrete direct stage/threat and evidence suffices. `retain_mid` for relevant stage-bounded work or disagreement requiring conservative retention. `demote` for joint demotion/adjacent mechanism. `insufficient_evidence` on any unresolved evidence blocker.

## Counts

- reviewed: 18
- retain_high: 5
- retain_mid: 9
- accepted: 14
- demote: 2
- insufficient_evidence: 2
- demoted_or_blocked: 4
- disagreements: 5

## Adjudications

| ID | A | B | Final | Disagreement | Rationale |
|---|---|---|---|---|---|
| S21P02 | retain_high | retain_high | retain_high | none | Both direct: argument-framework construction + contestable claim verification. Evidence concrete, no blocker. |
| S21P05 | retain_high | retain_high | retain_high | none | Both direct: raw debate text to typed support/attack knowledge base with formal/queryable semantics. Evidence sufficient; scope bounded. |
| 18_06 | insufficient_evidence | insufficient_evidence | insufficient_evidence | none | Both fail closed. Preserved artifact only landing/locator metadata; Carneades mechanism not independently evidenced. |
| 18_04 | retain_mid | retain_mid | retain_mid | none | Both relevant, but symbolic DeLP proof/defeat backend only. No open-text extraction or context selection. |
| 18_05 | retain_mid | retain_mid | retain_mid | none | Both relevant, stage-bounded to argument schemes/dialectical formalization. No learned extraction or compression. |
| S10P10 | retain_high | retain_high | retain_high | none | Both direct: scheme-conditioned LLM translation from natural-language arguments to computational arguments. Abstract-only, but concrete stage claim sufficient; confidence bounded. |
| S23P01 | retain_high | retain_mid | retain_mid | retain_high vs retain_mid | Relevant formal dialogue protocol, but reviewer disagreement high vs mid and no extraction/compression. Stage-bounded. |
| S21P06 | retain_mid | retain_mid | retain_mid | none | Both relevant, but supplied argument structure conditions generation; no source mining/provenance/proof gate. |
| S21P10 | demote | demote | demote | none | Both demote. Socratic/fallacy tutoring is adjacent pedagogy, not source extraction, proof, provenance, or compression. |
| 18_09 | insufficient_evidence | retain_mid | insufficient_evidence | insufficient_evidence vs retain_mid | Reviewer A blocks and reviewer B retains only from unavailable landing evidence. Abstract/full text absent; unresolved evidence blocker. |
| 18_01 | retain_mid | retain_mid | retain_mid | none | Both relevant formal defeasible reasoning/proof substrate; no natural-language evidence extraction or compression. |
| 18_08 | retain_mid | retain_mid | retain_mid | none | Both relevant conceptual Toulmin/defeasible-scheme bridge; no operational extractor, selector, or evaluation. |
| S10P05 | retain_mid | retain_high | retain_mid | retain_mid vs retain_high | Reviewer disagreement high vs mid. Concrete annotation/span/form-labeling mechanism, but abstract-only and no downstream proof/selection. |
| S21P07 | retain_high | retain_high | retain_high | none | Both direct: evaluated span/component and support/attack extraction from text. High only for front-end stage. |
| S08P06 | demote | retain_high | retain_mid | demote vs retain_high | Relevant prover-backed premise selection/proof checking, but reviewer disagreement high vs demote and formal-premise stage is bounded; no prose extraction/compression. |
| S10P04 | retain_high | retain_high | retain_high | none | Both direct: scheme-aware extraction of scheme names, premises, and explicit/implicit conclusions. Abstract-only and domain-bounded. |
| 18_13 | demote | demote | demote | none | Both demote. Survey/historical lineage only; no demonstrated operational mechanism. |
| S24P02 | demote | retain_mid | retain_mid | demote vs retain_mid | Reviewer disagreement demote vs mid. Concrete historical proof/correctness mechanism, but narrow and no NLP/context pipeline; stage-bounded. |

## Evidence paths

- `S21P02` — A: .hermes/lit_review/ranking/verification_runs/20261012_shard1/evidence/S21P02.html: Abstract; full-text sections describing ArgLLM argumentation frameworks and formal reasoning | B: verification_runs/20261012_shard1/evidence/S21P02.html; Abstract
- `S21P05` — A: .hermes/lit_review/ranking/verification_runs/20261012_shard2/evidence/S21P05_2ef91a6836e0f564.pdf: p.1 Abstract; §§3-5 framework, argument mining, fuzzy semantics, and querying | B: verification_runs/20261012_shard2/evidence/S21P05_2ef91a6836e0f564.pdf; p.1 Abstract, §§1-2
- `18_06` — A: .hermes/lit_review/ranking/verification_runs/20261012_shard3/evidence/18_06.html: article locator/landing metadata only; no preserved full text | B: verification_runs/20261012_shard3/evidence/18_06.html; article locator metadata
- `18_04` — A: .hermes/lit_review/ranking/verification_runs/20261012_shard4/evidence/18_04.pdf: p.1 Abstract; §§2-5 DeLP representation, dialectical trees, warrant, and implementation | B: verification_runs/20261012_shard4/evidence/18_04.pdf; p.1 Abstract/Introduction, §§ on warrant and dialectical trees
- `18_05` — A: .hermes/lit_review/ranking/verification_runs/20261012_shard1/evidence/18_05.html: Abstract and manuscript description | B: verification_runs/20261012_shard1/evidence/18_05.html; Abstract
- `S10P10` — A: .hermes/lit_review/ranking/verification_runs/20261012_shard2/evidence/S10P10_f9b9417a5ff5ca54.json: abstract | B: verification_runs/20261012_shard2/evidence/S10P10_f9b9417a5ff5ca54.json; Crossref abstract
- `S23P01` — A: .hermes/lit_review/ranking/verification_runs/20261012_shard3/evidence/S23P01.html: Abstract; Introduction; sections on formal dialogue systems and obligationes; Conclusion | B: verification_runs/20261012_shard3/evidence/S23P01.html; article page/abstract and sections on formal dialogue
- `S21P06` — A: .hermes/lit_review/ranking/verification_runs/20261012_shard1/evidence/S21P06.html: Abstract | B: verification_runs/20261012_shard1/evidence/S21P06.html; ACL landing abstract
- `S21P10` — A: .hermes/lit_review/ranking/verification_runs/20261012_shard2/evidence/S21P10_9499203c847ba743.pdf: p.1 Abstract; §§3-5 LFTutor and automatic/human evaluation | B: verification_runs/20261012_shard2/evidence/S21P10_9499203c847ba743.pdf; p.1 Abstract, §§1-2
- `18_09` — A: .hermes/lit_review/ranking/verification_runs/20261012_shard3/evidence/18_09.html: ACL landing/metadata; abstract field empty | B: verification_runs/20261012_shard3/evidence/18_09.html; ACL landing page and abstract
- `18_01` — A: .hermes/lit_review/ranking/verification_runs/20261012_shard1/evidence/18_01.pdf: p.125 Abstract; §§1-7 formal system, specificity, warrant, termination, and implementation | B: verification_runs/20261012_shard1/evidence/18_01.pdf; p.1 Abstract, §§1 and implementation/theory sections
- `18_08` — A: .hermes/lit_review/ranking/verification_runs/20261012_shard2/evidence/18_08_f5b9a40a5a1e386e.html: opening overview and sections connecting Toulmin themes to AI | B: verification_runs/20261012_shard2/evidence/18_08_f5b9a40a5a1e386e.html; Abstract/overview
- `S10P05` — A: .hermes/lit_review/ranking/verification_runs/20261012_shard3/evidence/S10P05.html: ACL abstract | B: verification_runs/20261012_shard3/evidence/S10P05.html; ACL landing abstract
- `S21P07` — A: .hermes/lit_review/ranking/verification_runs/20261012_shard4/evidence/S21P07.pdf: p.74 Abstract; §§2-4 representation, decoupled architecture, and evaluation | B: verification_runs/20261012_shard4/evidence/S21P07.pdf; p.1 Abstract/Introduction, §§3-5, p.10 Evaluation
- `S08P06` — A: .hermes/lit_review/ranking/verification_runs/20261012_shard1/evidence/S08P06.html: Abstract | B: verification_runs/20261012_shard1/evidence/S08P06.html; Abstract
- `S10P04` — A: .hermes/lit_review/ranking/verification_runs/20261012_shard2/evidence/S10P04_da389caa6875bba2.json: abstract | B: verification_runs/20261012_shard2/evidence/S10P04_da389caa6875bba2.json; Crossref abstract
- `18_13` — A: .hermes/lit_review/ranking/verification_runs/20261012_shard3/evidence/18_13.json: abstract | B: verification_runs/20261012_shard3/evidence/18_13.json; Crossref abstract
- `S24P02` — A: .hermes/lit_review/ranking/verification_runs/20261012_shard4/evidence/S24P02.html: Abstract; Conclusion/keywords metadata; full text access gate | B: verification_runs/20261012_shard4/evidence/S24P02.html; article title/abstract/landing metadata

## Validation

- 18 unique identity-pass inputs covered exactly once.
- Accepted rows: retain_high/retain_mid only.
- No accepted row has identity failure or insufficient_evidence.
