# Adversarial benchmark review — scholarly authenticity and reasoning depth

**Scope.** Top 20 candidates by `aggregate_mean_global_rank` in `benchmark_master_matrix.csv`; the matrix was not modified. Review tests whether high aggregate scores reflect authentic scholarly/argument text, reliable annotations, implicit-premise/inferential depth, and cross-tradition transfer.

## Verdict: REVISE / retain as a stratified suite

The aggregate ranking is useful but overstates comparability. The top set mixes authentic human-authored argument corpora, synthetic controlled reasoning benchmarks, and formal-library theorem-proving proxies. These classes should not be interpreted as one continuum of “scholarly reasoning quality.” Authentic corpora are strongest for ecological validity and annotation realism; synthetic/formal resources are strongest for causal diagnosis and exact proof/dependency checks.

**Reviewed:** 20 records. **Adversarial disposition:** 14 retain_high, 6 retain_mid. **Authenticity classes:** authentic_scholarly_text=3, synthetic_controlled=4, authentic_argument_corpus=8, formal_library_proxy=4, mixed_authentic_synthetic=1.

## Main findings

1. **FOLIO is the strongest authenticity/depth compromise.** Its human-authored premises, FOL annotations, and verification support real-text deductive evaluation, but it remains mostly monotonic/deductive and does not cover scholastic dialectical stages, defeasible attack, or implicit warrants.
2. **ProofWriter, RuleTaker, and LogicNLI are synthetic controls, not scholarly-text benchmarks.** Their proof/depth labels are excellent for isolating inference failures, but the aggregate should mark them as formal diagnostic proxies rather than evidence that a system understands historical or philosophical prose.
3. **LeanDojo and Magnushammer are formal-library proxies.** They are exceptionally valuable for premise selection, dependency preservation, and executable verification, but theorem-prover premises are not equivalent to source spans, warrants, or provenance in natural-language scholarship. LeanDojo appears repeatedly under different records/perspectives and must be family-deduplicated for suite claims.
4. **QT-SCHEMES, Walton corpora, EthiX, the 741-topic argument trees, and ElecDeb are the best direct argument-structure resources in this set.** They expose schemes, support/attack, stance, or tree structure over human-authored/curated material. None alone supplies complete annotation of implicit premises, validity, provenance, and cross-tradition scholastic distinctions.
5. **MISSCI/MISSCI PLUS are authentic evidence-grounded diagnostics, not general argument benchmarks.** Their cited scientific passages and fallacy reconstruction are valuable for provenance and misrepresentation, but the genre-specific task should not be promoted to full dialectical reasoning coverage.
6. **Cross-tradition relevance remains weak across the top 20.** Most authentic resources are contemporary English political, ethical, scientific, or dialogue data; formal resources are tradition-neutral. A separate primary-text suite spanning Aristotelian, medieval Latin, Islamic, Jewish, Nyaya, or Mohist materials is still required.
7. **Annotation quality is the unresolved acceptance risk.** “Annotated” or “manually curated” establishes supervision exists, not that scheme boundaries, implicit premises, support/attack, adjudication, agreement, or leakage controls are adequate. The final verification gate should require annotation protocol, agreement statistics, split construction, and artifact identity for every retained-high item.

## Recommended suite composition

- **Authentic core:** FOLIO; QT-SCHEMES; US2016G1tvWALTON; EthiX; 741-topic argument trees; ElecDeb; MISSCI PLUS/MISSCI; causal-link materials.
- **Formal diagnostic controls:** ProofWriter; RuleTaker; LogicNLI; LeanDojo/ReProver; Magnushammer.
- **Do not pool as independent evidence:** S07P01 with 12-04 (ProofWriter family); S07P08 with S08P04 and 14-08 (LeanDojo family); S09P08 with S25P13 (QT-SCHEMES family).
- **Required missing layer:** authentic, multilingual/cross-tradition primary or scholarly texts with span-level claims, implicit premises/warrants, provenance, and dialectical-role annotations.

## Record-level judgments

| Rank | ID | Resource | Authenticity | Depth | Verdict |
|---:|---|---|---|---|---|
| 10.2800 | 12-06 | FOLIO | authentic_scholarly_text (91) | high (88) | retain_high |
| 11.7600 | S07P01 | ProofWriter | synthetic_controlled (96) | high (97) | retain_high |
| 12.5600 | 12-04 | ProofWriter | synthetic_controlled (95) | high (98) | retain_high |
| 14.4400 | S09P08 | QT-SCHEMES | authentic_argument_corpus (88) | high (94) | retain_high |
| 16.1200 | 14-08 | LeanDojo/ReProver | formal_library_proxy (84) | high (97) | retain_high |
| 16.3200 | S25P13 | QT-SCHEMES | authentic_argument_corpus (87) | high (94) | retain_high |
| 19.2400 | 11-08 | MISSCI PLUS | authentic_scholarly_text (86) | high (85) | retain_high |
| 20.4800 | 12-05 | LogicNLI | synthetic_controlled (67) | medium (82) | retain_mid |
| 21.4000 | S08P05 | Isabelle proof-state/relevant-premise pairs | formal_library_proxy (78) | high (82) | retain_mid |
| 21.9600 | S07P08 | LeanDojo dataset/benchmark | formal_library_proxy (82) | high (89) | retain_mid |
| 22.1600 | S10P07 | US2016G1tvWALTON corpus | authentic_argument_corpus (84) | high (83) | retain_high |
| 22.2800 | S23P12 | 741-topic argument-tree corpus | authentic_argument_corpus (86) | high (91) | retain_high |
| 22.3600 | 11-04 | ElecDeb60To16 extension | authentic_argument_corpus (82) | medium (79) | retain_high |
| 23.4400 | S08P04 | LeanDojo dataset/benchmark | formal_library_proxy (80) | high (89) | retain_mid |
| 24.0400 | 18_11 | implicit-reasoning causal-link materials | authentic_argument_corpus (78) | medium (92) | retain_high |
| 24.4000 | 18_10 | Deep argumentative structures corpus | authentic_argument_corpus (81) | high (93) | retain_high |
| 24.4000 | 11-06 | MISSCI | authentic_scholarly_text (83) | medium (81) | retain_high |
| 24.9600 | S10P09 | EthiX | authentic_argument_corpus (79) | medium (88) | retain_high |
| 26.8400 | 11-12 | SMARTYPAT-BENCH | mixed_authentic_synthetic (60) | medium (87) | retain_mid |
| 27.0400 | 12-03 | RuleTaker | synthetic_controlled (18) | high (81) | retain_mid |

## Acceptance conditions before treating the ranking as final

- Resolve exact paper/resource identity and artifact access for every retained-high item; do not infer license or reproducibility from paper availability.
- Add a benchmark-family/version field and avoid counting repeated records as independent coverage.
- Verify annotation protocol, annotator expertise, agreement, adjudication, split/leakage controls, and whether “implicit” labels are human-judged or generated.
- Report separate aggregate views for authentic scholarly text, authentic argument corpora, synthetic controls, and formal-library proxies.
- Pair authentic benchmarks with explicit context perturbation tests: premise omission, warrant omission, distractor insertion, provenance corruption, polarity/negation changes, and long-context position shifts.
- Keep the status provisional until the protocol’s full-text/artifact verification gate is executed.
