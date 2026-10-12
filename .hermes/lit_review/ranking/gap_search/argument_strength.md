# Argument-strength benchmark gap search

## Scope

Search target: benchmarks evaluating argument strength, defeat, ranking, dominance, incomparability, burden of proof, critical-question outcomes, or expert judgments of which argument is better supported.

The inventory separates three constructs that are often conflated:

1. **Natural-language quality/preference benchmarks** — human or expert judgments of convincingness, quality, winningness, evidence strength, or better claims.
2. **Dialectical/structured argument benchmarks** — explicit support/attack, schemes, critical questions, defeat, burdens, or debate outcomes.
3. **Formal ranking/semantics benchmarks** — abstract or value-based argumentation frameworks where strength, acceptability, ranking, ties, or uncertainty are computed from a graph.

## Search and verification notes

Discovery was conducted against ACL Anthology records, official benchmark/repository pages, arXiv records, and official computational-argumentation competition pages. Records were retained only when the source record or official artifact supplied enough evidence to identify the task, labels, and resource identity. Search vocabulary included:

- `argument quality ranking pairwise convincingness benchmark dataset`
- `argument strength defeat ranking dominance incomparability benchmark`
- `critical questions argumentation benchmark dataset`
- `ICCMA ArgStrength ranking semantics benchmark`

The CSV preserves source and artifact URLs, benchmark status, evidence notes, and limitations. `formal_proxy` records are not substitutes for natural-language strength evaluation; they are included because they directly operationalize defeat, ranking, acceptance, or incomplete attacks.

## Main findings

### Strongest direct natural-language matches

- **Webis-ArgQuality-20 (AS04)** is the closest multidimensional quality resource: 1,271 arguments and 41,859 pairwise judgments, aggregated for rhetorical, logical, dialectical, and overall quality. It is still scalar quality aggregation rather than explicit attack/defeat or partial-order labeling.
- **IBM-ArgQ (AS01)** provides 14,000 pairwise argument-quality judgments plus 6,300 pointwise arguments. It is a direct pairwise preference benchmark, but the target is quality/convincingness, not whether one argument defeats another under a specified burden or critical question.
- **ClaimRev/Kialo (AS19)** is the largest ranking-oriented candidate in this search: more than 377,000 claim-revision pairs, with better-claim classification and ranking over revisions. It is highly useful for pairwise preference and ranking stress tests, but claim revision quality is not equivalent to defeasible support strength.
- **UKPConvArg and Passage Convincingness (AS18, AS02)** establish the older pairwise-convincingness paradigm: compare arguments/passages with opposing stances and infer a ranking from wins. These resources do not expose explicit defeats, proof obligations, or an abstain/incomparable outcome.
- **Winning-argument and debate-evaluation resources (AS10, AS17, AS20)** add outcome and preference signals, but winningness is audience- and protocol-dependent and may diverge from logical or dialectical support.

### Critical-question and structured argument resources

- **CQs-Gen (AS08)** is a useful adjacent benchmark: roughly 5,000 manually annotated critical questions with useful/unhelpful/invalid judgments. Its labels say whether a question challenges an argument, not whether the challenge succeeds, changes its burden status, defeats it, or leaves the pair incomparable.
- **ArgBench (AS09)** is a broad 46-task/33-dataset suite spanning argument mining, perspective, quality, reasoning, and generation. It can provide component tasks and baselines, but it is not a dedicated strength/defeat benchmark and mixes heterogeneous constructs and metrics.
- **ART (AS15)** tests reconstruction of warrants and argument components. It is relevant for reasoning-side validity but does not supply pairwise strength or defeat outcomes.
- **CEDAR (AS10)** exposes rich Chinese debate annotations, including evidence, roles, modality, and debate results. Debate-result prediction is an outcome proxy rather than an argument-level defeat or dominance relation.

### Formal defeat/ranking resources

- **ICCMA (AS11)** supplies machine-readable abstract/structured argumentation instances and solver tasks for acceptance and extension computation under formal semantics. It is the strongest formal defeat/acceptance benchmark family found, but it lacks natural-language arguments and expert judgments of relative support.
- **ArgStrength 2021 (AS12–AS13)** directly targets ranking individual arguments, including audience/value-sensitive ranking and incomplete argumentation frameworks. These are the best formal matches for strength, uncertainty, and possible incomparability. They remain graph-level solver benchmarks rather than human-labeled argument-quality corpora.
- **Ranking-semantics comparison (AS14)** evaluates formal rank-ordering semantics. It supports semantic validation and sensitivity analysis but is not a maintained natural-language benchmark and does not encode burdens of proof or expert support judgments.

## Gap assessment

No qualifying single benchmark was found that jointly provides:

1. authentic natural-language arguments;
2. explicit support and attack/defeat links;
3. argumentation-scheme or critical-question annotations;
4. burden/proof-standard or audience context;
5. expert pairwise judgments of which argument is better supported;
6. graded dominance/strength labels; and
7. a first-class **incomparable/underdetermined/abstain** outcome.

The literature is therefore split between **human preference/quality ranking** and **formal defeat/ranking semantics**. The most defensible evaluation battery should combine:

- Webis-ArgQuality-20, IBM-ArgQ, ClaimRev, and UKPConvArg/Passage Convincingness for human pairwise preference and ranking;
- CQs-Gen, ArgBench, ART, or CEDAR for critical-question, structured-reasoning, and debate-context controls; and
- ICCMA plus ArgStrength for formal defeat, acceptance, ranking, and incomplete-attack controls.

A new composed benchmark would need paired or set-valued judgments with labels such as `A_dominates_B`, `B_dominates_A`, `mutual_defeat`, `both_supported`, `neither_supported`, and `incomparable`, together with the applicable burden, audience, scheme, and critical-question state. Pairwise quality datasets should not be relabeled as defeat data without collecting those missing annotations.

## Negative/failure ledger

- Searches combining `natural language`, `argument strength`, `incomparability`, and `benchmark` returned quality/convincingness and formal ranking resources, but no verified corpus with explicit expert-labeled incomparability.
- Searches for `critical question outcome benchmark` found critical-question generation and scheme resources, but not a benchmark whose gold label records whether a critical question defeats or merely weakens an argument.
- Formal ranking competitions expose graph-level uncertainty and ties, but their artifacts do not provide authentic scholarly/debate text or human support judgments.
- Debate winner datasets were retained as adjacent controls because winner labels can reflect persuasion, audience preference, or adjudication protocol rather than defeasible support.

## Files

- `argument_strength.csv` — 20 retained records with controlled benchmark status, task/label descriptions, artifact/source URLs, directness, limitations, and evidence notes.
- `argument_strength.md` — this synthesis and gap assessment.
