# Continuation-candidate relevance review: ranks 39–47 plus S24P01

## Scope and decision rule

Reviewed exactly the six identity-passed candidates requested from aggregate ranks 39–47—`S09P04`, `S09P05`, `S03P07`, `S04P10`, `S02P08`, and `S04P12`—plus newly identity-passed `S24P01`. `S24P01` is recorded as aggregate rank 3 in the existing historical-fidelity ranking, but is included here as the separately requested continuation candidate because its exact identity was newly corroborated under `verification_runs/next7_retry`.

The hostile pipeline test is the integrated project composition: **cross-tradition argument/form classification; explicit deductive or argument-skeleton extraction with provenance; selection or compression of reasoning-critical components under a sufficiency/minimality objective; and downstream LLM philosophical-reasoning evaluation**. A paper is not treated as a full-pipeline duplicate merely because it covers one stage.

Each row in `continuation_relevance_38_47.csv` records the demonstrated stage, the strongest available mechanism evidence, transfer that is only inferred, novelty overlap, missing boundaries, and a hostile countertest that removes title/venue/category prestige.

## Verdict distribution

| Verdict | Count |
|---|---:|
| retain_high | 3 |
| retain_mid | 4 |
| demote | 0 |
| false_positive | 0 |
| insufficient_evidence | 0 |
| **Reviewed** | **7** |

`retain_high` means a strong demonstrated threat to a core pipeline component, not exact duplication of the complete integrated scholastic pipeline. `retain_mid` means useful bounded prior art—typically taxonomy, selection, or downstream robustness evaluation—with no demonstrated proof-aware end-to-end composition.

## Candidate findings

### S09P04 — retain_mid

Lawrence and Reed define argument mining as automatic identification and extraction of inferential structure and survey components, relations, schemes, corpora, and evaluation. This materially constrains novelty claims around argument-mining decomposition and structured argument analysis, but the survey does not implement an extractor, provenance layer, compressor, or downstream LLM evaluation. The hostile countertest leaves a strong taxonomy and boundary precedent, not a paper-owned pipeline mechanism.

Evidence: `summaries/09_argument_mining_summaries.md` § Lawrence and Reed (2020); `verification_runs/20261012_shard3/evidence/S09P04.html` lines 6, 21, and 26–44.

### S09P05 — retain_mid

Lauscher et al. survey scholarly-document argument mining across ADUs, claims, premises, data, warrants, rebuttals, support/contradiction/same-claim relations, evidence extraction, and claim-evidence traversal. The full text directly surfaces domain adaptation, enthymemes, subjective interpretation, and long-range context as prior challenges relevant to this project. It remains a survey/position paper: no new integrated extractor, proof object, compressor, or LLM reasoning experiment is demonstrated.

Evidence: `summaries/09_argument_mining_summaries.md` § Lauscher et al. (2021); `verification_runs/20261012_shard4/evidence/S09P05.pdf` pp. 1–3 and 6–8, especially the extracted sections on annotation schemes, argument units/relations, challenges, and applications.

### S03P07 — retain_high

Hsieh et al. identify U-shaped positional-attention bias, introduce a calibration mechanism that improves middle-position retrieval, and report downstream RAG gains. This is direct, demonstrated prior art against broad claims about relevance-aware long-context utilization and making buried evidence usable. It does not preserve proof dependencies, track source spans, or select context under logical sufficiency/minimality, so it is high for the context/retrieval stage rather than a full-pipeline duplicate.

Evidence: `summaries/03_context_degradation_summaries.md` §7; `verification_runs/20261012_shard1/evidence/S03P07.html` lines 6, 30–32, 37, and 41–65.

### S04P10 — retain_high

Xu et al. demonstrate mixed exact/soft compression for tool documentation: selective compression retains execution-critical tool and parameter names as raw tokens, while block compression produces fixed-length soft summaries with variable ratios. Results on API-Bank and APIBench remain comparable to an upper-bound baseline at up to 16× compression. The mechanism directly threatens generic claims about protected critical content, adaptive compression, and quality–efficiency trade-offs, but not proof-aware or provenance-bearing compression.

Evidence: `summaries/04_context_compression_summaries.md` §10; `verification_runs/20261012_shard2/evidence/S04P10_ba12c0ca3e182ad3.html` lines 6, 30–38, and 42–67.

### S02P08 — retain_mid

Peskov et al. provide a concrete robustness framework using adversarial noise and counterfactual statements to generate seven perturbed datasets, comparing formal/informal reasoners by reasoning format, formalization syntax, and error-recovery feedback. This is a meaningful threat to novelty claims around adversarial deductive-robustness evaluation and formal-vs-informal reasoner comparisons. The paper does not construct source-grounded arguments or proof-critical contexts, and the underlying benchmark/release is not clearly established, so it remains mid rather than high.

Evidence: `summaries/02_logic_hallucination_summaries.md` §8; `verification_runs/20261012_shard3/evidence/S02P08.html` lines 20–30, 120–145, and 210–250; `remaining_nonbenchmark.csv` line 14.

### S04P12 — retain_mid

Sun et al. frame few-shot example selection as data compression and use BM25 recall followed by influence-aware meta-gradient/Fisher reranking, reporting an average 5.90% improvement across five datasets and four GPT-2 sizes. This is direct component-level precedent for relevance-aware selection and information-preserving example choice, but selected demonstrations are not source-grounded premises or proof components and no sufficiency, provenance, or scholastic transfer is shown. The mechanism survives the hostile test, but its object is too distant from proof-aware evidence construction for retain_high.

Evidence: `summaries/04_context_compression_summaries.md` §12; `verification_runs/20261012_shard1/evidence/S04P12.html` lines 6, 24–31, and 35–53.

### S24P01 — retain_high

Hodges provides the strongest direct historical/formal precedent in this set. The paper translates and closely reads Ibn Sīnā’s Qiyās 9.6, extracts the essential ingredients of an Abstract State Machine, and confirms that the passage specifies a proof-search algorithm for syllogisms, including analysis, missing-premise completion, and state/transition structure. It does not automate cross-tradition extraction or evaluate an LLM, but it is a concrete, provenance-preserving demonstration that historical logical procedure can be reconstructed as an inspectable proof-search mechanism.

Evidence: exact identity pass in `verification_runs/next7_retry/identity_checks.csv` line 3; full downloaded PDF text in `verification_runs/next7_retry/raw/S24P01.pdf.txt` lines 16703–16729, 16735–16778, 16839–16860, and 16946–16957; summary in `summaries/24_islamic_comparative_scholastic_ai_summaries.md` §1.

## Overall adjudication

Three papers merit `retain_high`: `S03P07` for calibrated long-context retrieval, `S04P10` for protected mixed exact/soft compression, and `S24P01` for historically faithful proof-search formalization. Four merit `retain_mid`: `S09P04` and `S09P05` for argument-mining boundaries and scholarly argument representations, `S02P08` for adversarial deductive-robustness evaluation, and `S04P12` for example-selection prior art.

None demonstrates the complete integrated pipeline. The high items threaten distinct core components; the mid items should remain visible as bounded precedents and should not be described as proof-aware scholastic context-engineering systems. No candidate was evidence-blocked or a false positive, and no ranking, master, or identity file was edited.
