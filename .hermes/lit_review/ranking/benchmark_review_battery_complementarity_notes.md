# Battery complementarity review

## Verdict

Minimal sufficient battery: 10 unique benchmark families, with 11 records if retaining both ALCE and MultiHop-RAG for output/retrieval separation. Do not count duplicate QT-SCHEMES, ProofWriter, or LeanDojo records as extra coverage.

## Minimal core

1. **S09P08 QT-SCHEMES** — front-end scheme extraction over dialogue arguments.
2. **S23P12 741-topic argument-tree corpus** — component, stance, specificity, and dependency extraction.
3. **12-06 FOLIO** — authentic multi-step formal reasoning with FOL verification.
4. **S07P01 ProofWriter** — controlled proof depth, abduction, and open/closed-world diagnosis.
5. **14-08 LeanDojo/ReProver** — proof-relevant premise selection plus exact downstream proof.
6. **S03P10 LongPiBench** — dispersed multi-piece evidence and positional dependency stress.
7. **S03P09 NoLiMa** — semantic retrieval when lexical overlap is weak.
8. **11-08 MISSCI PLUS** — scholarly passage grounding, fallacy reconstruction, verbalization, and fact checking.
9. **S05P09 MultiHop-RAG** — dependency-aware support retrieval.
10. **S05P05 ALCE** — citation-backed downstream answer generation.

Optional 11th: **S25P12 MARS** for philosophical-output breadth; **S06P11 FAITHCOT-BENCH** for trajectory faithfulness; **S03P08 RULER** for generic context-window control.

## Pairing map

- Front-end extraction: QT-SCHEMES + 741-topic argument trees; add 18_10/18_11 when implicit relations matter.
- Formal reasoning: FOLIO + ProofWriter + LeanDojo/ReProver. Authenticity, controlled depth, and exact proof are separated.
- Long context: LongPiBench + NoLiMa; add RULER only as generic scale control.
- Grounding: MISSCI PLUS + MultiHop-RAG; add ALCE when cited output is required.
- Downstream output: ALCE + MARS; require source-span/citation checks from MISSCI PLUS.

## Redundancy

- QT-SCHEMES appears as S09P08 and S25P13. Same resource; S25P13 is identity-preserved but not new coverage.
- ProofWriter appears as S07P01 and 12-04. Same family; retain one primary record.
- LeanDojo appears as 14-08, S07P08, and S08P04. Same dataset/tool family across perspectives; use 14-08 primary, optionally one cross-perspective replication.
- Walton resources overlap: US2016G1tvWALTON, EthiX, NLAS-multi, and S25P14. Use US2016G1tvWALTON + EthiX for authentic diversity; avoid all four in minimal suite.
- Generic context suites LRA, LongBench, and ∞Bench are scale controls, not replacements for dependency-bearing LongPiBench/NoLiMa.
- RAGTruth, FalseQA, KG-FPQ, and LOGICOM are narrower hallucination diagnostics; use for targeted error analysis, not core coverage.

## Design rule

Every core item must add a distinct observable: extraction, structure, proof validity, premise selection, dependency under context stress, grounded retrieval, or inspectable output. Remove any item whose removal leaves all those observables covered by another family.
