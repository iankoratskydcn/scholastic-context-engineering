# Benchmark battery recommendation

- Reconciled: 2026-10-12 UTC.
- Gate: exact identity plus preserved downloadable artifact evidence; unresolved license, identity, or artifact issues remain blocked.

## Decision

**Use six verified benchmarks now; keep three high-value candidates pending.** No verified benchmark covers the full integrated pipeline.

## Verified core
### deductive/formalization control — `12-06` FOLIO
- Status: **verified_optional_fallback**
- Artifact/license: verified / CC BY-SA 4.0
- Decision: include_core_now
- Why: Human-authored natural-language premises with FOL annotations and executable verification; best verified fallback for form/deduction testing.

### context stress — `S03P10` LongPiBench
- Status: **verified**
- Artifact/license: verified / MIT
- Decision: include_core
- Why: Official artifact downloaded and integrity-checked; directly stresses separated relevant information under distance/position changes.

### premise critique / invalid inference — `S02P07` PCBench
- Status: **verified**
- Artifact/license: verified / MIT
- Decision: include_core
- Why: Public 1,200-record artifact parsed successfully; isolates false/defective-premise critique.

### grounding / fallacy provenance — `11-08` MISSCI PLUS
- Status: **verified_with_reproducibility_caveat**
- Artifact/license: verified dataset splits / Apache-2.0 repository; dataset terms require care
- Decision: include_core_with_caveat
- Why: Authentic scientific passages, evidence retrieval, verbalization, and fact-checking; code README says implementation is incomplete.

### formal proof compatibility / premise selection — `14-08` LeanDojo/ReProver
- Status: **verified_heavy_control**
- Artifact/license: verified Zenodo/GitHub family / library/license details require pinning
- Decision: include_core_secondary
- Why: Executable prover boundary and proof-relevant premise retrieval; heavy Lean/elan setup and formal-only transfer limits.

### authentic scholastic text — `S22P04` Index Thomisticus Treebank / UD_Latin-ITTB
- Status: **verified**
- Artifact/license: verified / CC BY-NC-SA 3.0
- Decision: include_core_transfer_gate
- Why: Verified Medieval Latin/Aquinas artifact; authentic-text gate, though native task is linguistic annotation rather than reasoning.

## Pending candidates
- `S09P08` QT-SCHEMES: **blocked_pending_license** — Strongest semantic form benchmark, but official repository has no declared license; fail closed.
- `S23P12` 741-topic argument-tree corpus: **blocked_identity_mismatch** — Matrix citation is wrong; ACL identity is Durmus, Ladhak, and Cardie, not Peldszus and Stede. No artifact verified.
- `S05P05` ALCE: **blocked_dataset_license** — Artifact is accessible and parses, but dataset licensing/provenance is unresolved under fail-closed policy.

## Interpretation rules
- Do not pool scores across these resources as one benchmark score.
- Report separate metrics for form/deduction, context retention, premise critique, grounding, formal premise selection, and scholastic-text transfer.
- Run raw, selected, compressed, distractor, and dependency-ablation conditions where the task exposes the required intermediate artifact.
- Treat LeanDojo as a formal control, not evidence of natural-language scholastic understanding.
- Treat ITTB as an authentic-text transfer gate, not as a complete argument-reasoning benchmark.
- The missing validated layer is an artifact-backed benchmark combining authentic scholastic text, argument forms, provenance, dependency-preserving compression, and downstream inspectable reasoning.
