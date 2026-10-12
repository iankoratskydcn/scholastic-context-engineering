# Overall suite value review

## Decision
No single benchmark validates proposed pipeline. Use battery, not winner-take-all ranking. Scores weight pipeline coverage, complementarity, novelty-threat detection, failure diagnosis, scholarly relevance, minimal-battery utility.

## Minimal battery
1. **QT-SCHEMES** (`S09P08`, `S25P13`) — authentic dialogue argument schemes; preserve both source records, run artifact once.
2. **FOLIO** (`12-06`) — human-authored premises, FOL labels, automated verification; authenticity anchor.
3. **ProofWriter** (`S07P01`, `12-04`) — controlled proof depth, open/closed world, abduction; synthetic diagnostic anchor.
4. **LeanDojo/ReProver** (`14-08`, `S07P08`, `S08P04`) — premise retrieval, hard negatives, exact proof checking; formal selection anchor.
5. **MISSCI PLUS** (`11-08`) — real scientific passages, retrieval, fallacy grounding, fact checking; scholarly provenance anchor.
6. **LongPiBench** (`S03P10`) — distance among multiple relevant pieces; direct context-selection/position threat.
7. **RULER or NoLiMa** (`S03P08` / `S03P09`) — generic long-context control; choose one under budget, retain LongPiBench for multi-piece stress.

## Combine, do not use alone
- QT-SCHEMES + FOLIO: informal scheme recovery plus formal validity/authentic text.
- ProofWriter + FOLIO: synthetic depth controls plus human-authored transfer.
- LeanDojo/ReProver + LongPiBench: premise relevance plus positional/context assembly stress.
- MISSCI PLUS + ALCE/MultiHop-RAG: scholarly evidence grounding plus generic citation/multi-hop controls.
- LongPiBench + RULER/NoLiMa: multi-piece dependency stress plus context-window/semantic-retrieval controls.
- Walton/EthiX/NLAS-multi: use as diversity/robustness bundle, not isolated standalone evidence.
- Shared records for ProofWriter, LeanDojo, and QT-SCHEMES are duplicate/version views in source universe; preserve identities, deduplicate execution by artifact family.

## Exclusions from minimal battery
Cultural/multilingual, manuscript OCR, morphology, generic QA, and broad awareness/philosophy benchmarks remain optional boundary tests. They add scholarly or domain coverage but do not directly validate integrated extraction, structure recovery, provenance-preserving selection, and inspectable reasoning.

## Self-validation
- 80 source rows retained.
- Category/global CSVs contain same 80 literal paper IDs.
- Global ranks 1–80; category ranks contiguous within category.
- Tie ordering: score descending, numeric category, paper order, literal paper ID.
- Input identity fields copied unchanged.
