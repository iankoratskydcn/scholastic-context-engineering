# Common-ground and shared-premise detection benchmark search

**Scope.** Search conducted on 2026-10-12 for scholarly benchmark-producing papers and official artifacts addressing: (1) agreement/disagreement between opposing lines, (2) claim compatibility/strengthening/weakening, (3) shared key points or convergence across pro/con arguments, (4) implicit warrants/shared assumptions, and (5) common-ground belief-state tracking as an adjacent control.

**Search outcome.** Eight retained records are listed in `gap_search_common_ground_detection.csv`. The strongest direct gap fills are:

1. **ArgCMV (Gurjar et al., EMNLP 2025)** — closest match to synthesis from shared ground. It contains long, authentic r/ChangeMyView debate threads with explicit pro/con pools, argument-to-key-point mappings, cross-user convergence, and a pairwise shared-key-point detection/generation formulation. It is still not a formal shared-premise benchmark: key points are stance-specific and model-assisted.
2. **ClaimDiff (Ko et al., Findings ACL 2023)** — claim pairs from different articles on the same contentious issues, with strengthen/weaken labels and extractive rationales. This is a strong benchmark for claim compatibility and inspectable comparison, but it does not label common premises or mutual acceptance directly.
3. **Agreement/disagreement corpora and tasks** — Rosenthal & McKeown's ABCD benchmark, Gokcen & de Marneffe's IAC experiments, and Skeppstedt et al.'s shared-task corpus provide established pair-level agreement/disagreement evaluation over authentic online debate/forum data. They detect relation polarity rather than extracting the exact proposition or premise jointly accepted.
4. **Argument Reasoning Comprehension Task (Habernal et al., NAACL 2018)** — 1,970 authentic argument instances requiring selection of the implicit warrant from two opposing candidates. This is the closest reusable benchmark for hidden assumptions, but it is single-argument rather than cross-line common-ground detection.

**Adjacent controls.** Markowska et al. (EMNLP 2023) and Soubki et al. (ACL 2024, COMMON-TOM) provide explicit proposition, belief, and common-ground update representations over natural spoken conversations. They are not argument/opposition benchmarks, but their labels are useful for designing an interpretable shared-commitment state layer. They should not be counted as direct argument common-ground benchmarks.

## Record-level notes

- **CGD-01 — Unshared task (Dis)agreement in online debates.** 27 debate threads plus a 2,000-sentence evaluation set; labels topic-independent agreement/disagreement expressions and reports classifier results. Direct relation layer, not premise extraction.
- **CGD-02 — ABCD / IAC / AWTP comparison.** Three-way agreement/disagreement/none classification with quote-response inputs and thread structure. The ABCD corpus is naturally derived from debate-side labels; IAC uses human scalar agreement annotations.
- **CGD-03 — ClaimDiff.** Official GitHub artifact exposes ClaimDiff-S and ClaimDiff-W JSON files with claim pairs, relation labels, and rationales. The full test distribution includes unrelated pairs. Strong comparison benchmark; no explicit common-ground label.
- **CGD-04 — ArgCMV.** Official repository exposes anonymized Reddit IDs, stance, topic, key points, and key-point mismatch fields. The paper describes separate pro/con key-point extraction, argument mapping, manual validation, and a shared-key-point pairwise baseline.
- **CGD-05 — ARCT.** Official ACL paper and UKPLab repository. Inputs are premise, claim, topic, and two plausible warrants implying opposite claims; output is the correct warrant. It operationalizes implicit reasoning assumptions rather than shared premises between opposing arguments.
- **CGD-06 — Finding Common Ground.** Common-ground annotation and proposition tracking in natural spoken conversations. Useful representation control; not adversarial argumentation.
- **CGD-07 — COMMON-TOM.** Naturalistic common-ground QA over CALLHOME-derived spoken dialogue with explicit belief/common-ground modeling. Useful evaluation pattern for distinguishing private belief from mutual commitment; not an opposing-argument benchmark.
- **CGD-08 — IAC disagreement detection.** Human agreement scores on quote-response pairs and semantic alignment features. Directly relevant to accepting/rejecting prior argumentative content, but no proposition-level shared-premise labels.

## Evidence and limitations

- Exact identities were verified against ACL Anthology landing pages/PDFs, arXiv HTML/PDF where used, and official GitHub repositories. URLs are retained in the CSV.
- Artifact access and licensing are kept separate. Where a paper or repository license was not verified in retained evidence, the CSV says so rather than inferring a license from paper access.
- `web_extract` was unavailable in this runtime because the configured extraction backend rejected URL extraction. I preserved this as a retrieval failure and used scholarly search results plus direct `curl` retrieval of official ACL pages/PDF metadata instead. Search snippets were not treated as the sole basis for artifact-access claims.
- No exact benchmark was found that directly labels the intersection of premises accepted by two explicitly opposed argument lines and evaluates synthesis from that intersection. The gap remains open. ArgCMV is the nearest direct resource; ClaimDiff and the agreement/IAC family are complementary relation/comparison resources; ARCT is the nearest implicit-assumption resource.

## Recommended benchmark composition

A new benchmark could compose the retained mechanisms: use authentic pro/con threads (ArgCMV/ABCD/IAC), align explicit and implicit argument units (ARCT), annotate pairwise agreement plus proposition-level relation (IAC/ABCD), and add a gold set of shared premises/key points with rationales and a synthesis target. COMMON-TOM's separate private-belief versus common-ground labels provide a useful schema constraint for distinguishing "both arguments mention it" from "both lines commit to it."

## Retained source URLs

- https://aclanthology.org/W16-2818/
- https://aclanthology.org/W15-4625/
- https://aclanthology.org/2023.findings-acl.289/
- https://github.com/kaistAI/ClaimDiff
- https://aclanthology.org/2025.emnlp-main.1110/
- https://github.com/scuba-illinois/ArgCMV
- https://aclanthology.org/N18-1175/
- https://github.com/UKPLab/argument-reasoning-comprehension-task
- https://aclanthology.org/2023.findings-emnlp.551/
- https://github.com/cogstates
- https://aclanthology.org/2024.findings-acl.880/
- https://github.com/cogstates/common-tom
- https://aclanthology.org/P15-2016/
