# Gap search: stage-conditioned retrieval for disputation

## Scope
Search target: benchmarks or reusable evaluation resources for retrieving objections, counterarguments, rebuttals, counterevidence, or role/stage-conditioned evidence in structured disputation. Search followed `gap_benchmark_search_protocol.md`: scholarly identity and task mechanism were required; paper access was kept separate from artifact and license status; adjacent controls were retained instead of being promoted to direct matches.

## Result
- **10 records** in the companion CSV.
- **3 direct gap fills:** ArguAna Counterargs; Knowledge-Enhanced Evidence Retrieval for Counterargument Generation; Touché/CLEF 2025 Retrieval-Augmented Debating (RAD25).
- **6 strong adjacent resources:** ConQRet; Touché 2020; PerspectiveArg2024; RPC-Bench; ArgumenText; ArgBench.
- **1 control-only resource:** DialFact.
- **0 false positives** retained.

The clearest direct precedent is **RAD25**: its four-turn protocol changes the retrieval target by local dialogue state—counterarguments to the user's utterance versus supporting evidence for the attacked system response—before generating the next response. ArguAna supplies the strongest older counterargument-ranking baseline, while Jo et al. supplies sentence-level counterevidence retrieval. None of the direct matches exposes a complete scholastic taxonomy such as objection → sed contra → response → rebuttal with explicit move legality and per-objection coverage labels. That remains an open benchmark gap.

## Record notes

### Direct gap fills
1. **ArguAna Counterargs (Wachsmuth, Syed & Stein, 2018)** — argument-level best-counterargument retrieval with candidate-pool variants; authentic iDebate material; direct negative construction and ranking baseline.
2. **Knowledge-Enhanced Evidence Retrieval for Counterargument Generation (Jo et al., 2021)** — statement-to-counterevidence retrieval and sentence selection, with knowledge-enhanced inference; direct evidence-selection precedent, but not a multi-turn protocol.
3. **Touché/CLEF 2025 RAD25** — stage-conditioned multi-turn retrieval and response generation over ClaimRev arguments; closest match to role-aware disputation retrieval found.

### Strong adjacent resources
4. **ConQRet (Dhole, Shu & Agichtein, 2025)** — stance-conditioned retrieval-augmented argumentation with groundedness and argument-quality evaluation; no dialogue-stage labels.
5. **Touché 2020** — graded argument retrieval over controversial topics; a useful retrieval infrastructure/control benchmark but not stage-conditioned.
6. **PerspectiveArg2024** — retrieval conditioned on explicit or implicit socio-cultural perspective; transferable conditioning design, but perspective is not a discourse role.
7. **RPC-Bench (Chen et al., 2026)** — authentic review–rebuttal exchanges with fine-grained comprehension/claim-verification QA; useful for rebuttal-stage context and obligation labels, but not ranking retrieval.
8. **ArgumenText (Stab et al., 2018)** — open-domain argument retrieval from heterogeneous sources; useful candidate-pool control, without polarity or turn-stage labels.
9. **ArgBench (Ajjour et al., 2026)** — umbrella suite over 33 datasets and 46 computational-argumentation tasks; useful for controls and component-task discovery, not a dedicated stage-conditioned retrieval benchmark.

### Control only
10. **DialFact (Gupta et al., 2021)** — dialogue-conditioned evidence retrieval and supported/refuted/insufficient labels; useful separation control, but fact-checking is not counterargument or rebuttal retrieval.

## Search and evidence log

### Queries / source families
- `argument retrieval counterargument benchmark dataset`
- `counterevidence retrieval counterargument generation benchmark`
- `retrieval augmented debating Touché 2025`
- `perspective argument retrieval shared task`
- `review rebuttal benchmark dataset retrieval`
- `computational argumentation benchmark retrieval rebuttal`
- ACL Anthology, arXiv, Webis/Touché official task pages, and official GitHub repositories were prioritized.

### Opened or retained scholarly/official sources
- ACL Anthology: P18-1023 (ArguAna), 2021.findings-emnlp.264 (counterevidence retrieval), 2024.argmining-1.14 (PerspectiveArg2024), N18-5005 (ArgumenText), 2026.acl-long.1277 (RPC-Bench), and 2026.findings-acl.1099 (ArgBench).
- arXiv: 2412.05206 (ConQRet) and 2110.08222 (DialFact).
- Official Webis/Touché pages for ArguAna Counterargs, Touché 2020, RAD25, and ArgBench data.
- Official GitHub pages for KENLI, ConQRet, PerspectiveArg2024, DialFact, RPC-Bench, and ArgBench data.

### Failed / blocked searches preserved
- A batch `web_extract` attempt against ACL, Webis, GitHub, and Touché URLs failed because the active extraction backend reported that native web search was available but URL extraction required an unavailable configured backend. This did not get silently converted into positive artifact claims.
- Several artifact/license states remain explicitly qualified in the CSV: public paper access is not treated as proof of dataset access or license; per-dataset licenses in ArgBench and inherited resources require separate checks; RAD25 and Touché pages did not state a license in the retained evidence.
- No dedicated benchmark was found that simultaneously provides (a) typed disputation stages, (b) objection/rebuttal role labels, (c) retrieval rankings or evidence relevance judgments, and (d) full provenance-preserving artifacts. This is recorded as an evidence-based gap, not as proof that no such resource exists.

## Recommended use in the benchmark battery
- Use **ArguAna** for direct counterargument ranking and hard-negative evaluation.
- Use **Jo et al.** for sentence-level counterevidence selection.
- Use **RAD25** for stage-conditioned routing and response generation.
- Add **ConQRet** and **Touché 2020** as retrieval/grounding controls.
- Use **RPC-Bench** to seed rebuttal-specific claim-response obligations, but do not label it a retrieval benchmark.
- Treat **ArgBench** as an umbrella inventory/control suite, then inspect its component datasets for any counterargument or perspective tasks before claiming coverage.

CSV companion: `gap_search_disputation_retrieval.csv`
