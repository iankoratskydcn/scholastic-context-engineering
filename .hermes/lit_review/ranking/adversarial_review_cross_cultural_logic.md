# Adversarial review — cross-cultural logic ranking

## Verdict

**REVISE — substantive ranking and evidence problems.** The two CSVs satisfy the basic row-count/ID/rank-shape checks, but the review is not defensible as a tradition-sensitive ranking. It repeatedly substitutes topic labels for paper-specific relevance, treats culturally situated reasoning as formal non-Western logic, and uses boilerplate evidence that cannot support the fine-grained order.

## Checks performed

- Compared both review CSVs with `remaining_nonbenchmark.csv` and `ranking_protocol.md`.
- Verified 124 rows in each output, matching paper-ID sets, required columns, populated/blank rank columns, integer scores in range, and unique ranks in the relevant file.
- Read the category 16, 17, and 24 source summaries and agent evidence, with particular attention to whether a source studies formal logic, culturally situated reasoning, Islamic scholastic material, or only enabling infrastructure.
- Tested score/rank ordering. Category ranks are consistent with descending score and source/canonical ordering. Global ties also follow the apparent category/paper ordering; no rank-shape defect was found.

## Findings

### BLOCKER-1 — Category 24 is scored by label, not by evidence

All 13 retained category-24 rows receive 97–99 and the exact same explanation: “Provides Islamic logical, juridical, textual, or computational evidence…”. The source summary explicitly distinguishes direct Islamic formalization (S24P01–S24P04), Christian scholastic stylometry (S24P05–S24P06), Islamic text mining/corpus infrastructure (S24P07–S24P08), Biblical/Hebrew infrastructure (S24P13–S24P14), a conceptual Islamic KG proposal (S24P15), a survey (S24P16), and a general argument-mining survey (S24P17). These are not interchangeable levels of directness, validation, or transfer. The near-ceiling scores flatten the distinction between direct historical formalization and merely adjacent infrastructure and drive the global top 16 almost entirely from category membership.

**Required correction:** score each paper on demonstrated project relevance, novelty threat, methodological transfer, and likely usefulness. Separate direct formalization, reusable infrastructure, adjacent comparative material, surveys, and duplicates; do not use “Islamic” or “scholastic” as a proxy for evidence.

### BLOCKER-2 — Clear tradition and scope conflations in category 24

The explanation is factually misleading for several rows:

- **S24P05/S24P06:** Stephen Langton is Christian scholastic material; the summary says the work is authorship/transmission stylometry, not Islamic logic or argument mining.
- **S24P13:** computational Biblical-text analysis is comparative enabling infrastructure, not Islamic logic.
- **S24P14:** ONLP/YAP targets Modern Hebrew morphosyntactic parsing and does not model medieval Jewish disputation.
- **S24P17:** Lawrence and Reed is a general argument-mining survey, explicitly not an Islamic or scholastic system.

This is precisely the Western-logic/cross-tradition conflation the review was required to detect: Christian, Jewish, Biblical, generic NLP, and Islamic sources are collapsed into one “Islamic” evidence bucket.

**Required correction:** retain the source IDs, but rewrite explanations to name the actual tradition and task, and lower scores where the contribution is only transferable infrastructure or a survey.

### BLOCKER-3 — Cross-cultural reasoning is repeatedly presented as “non-Western logic” without preserving the source caveat

The category-17 evidence says the literature is mostly cultural commonsense, values, pragmatics, multilingual evaluation, and Chinese exam data—not competing formal logics. It explicitly warns not to generalize LogiQA to “Chinese reasoning,” and states that ArabCulture, DRISHTIKON, SANSKRITI, WorldValuesBench, and similar resources are not evidence for a unitary Arab, Indian, or other non-Western logic. Nevertheless, both output files give the two category-17 rows 96–97 and use the same explanation that they directly support avoiding collapse into “a single normative template,” without stating that their formal-logic relevance is low or indirect.

**Required correction:** distinguish at least: formal validity, culturally situated commonsense, value-conditioned judgment, pragmatic inference, multimodal cultural understanding, and translation robustness. Do not award near-ceiling scores to cultural-evaluation papers merely because they are culturally diverse.

### MAJOR-4 — Category 16 also overstates transfer from historical logic scholarship

Every category-16 row receives the same explanation (“Directly reconstructs a historical logical tradition or its formal apparatus…”) and 95–97, despite substantial differences among Aristotle, histories of medieval logic, Indian logic scholarship, Islamic intellectual history, and bibliographic/conceptual works. Historical reconstruction is valuable background, but the summaries do not establish an NLP system, comparative representation, expert-annotated corpus, or validated transfer into context engineering. The ranking therefore conflates historical importance with demonstrated project usefulness and gives generic historical scholarship scores comparable to, or higher than, actual culturally authored evaluation resources.

**Required correction:** identify the concrete transferable artifact or method for each paper and discount works whose contribution is historical orientation only. Preserve high scores only where the source supplies an executable formal procedure, representation, corpus method, or directly testable evaluation design.

### MAJOR-5 — Evidence bases are non-auditable for the highest-ranked rows

The category-16 and category-17 evidence bases are boilerplate: “source artifact describes a scholarly, formal, conceptual, survey, normative, or comparative study without a benchmark-producing artifact.” That does not point to a specific summary section, result, formal procedure, dataset, or limitation. It cannot substantiate why one row outranks another. Category-24 evidence is better but still repeats the same broad rationale across heterogeneous sources.

This violates the protocol requirement that `evidence_basis` point to source summary or paper evidence rather than reviewer intuition alone.

**Required correction:** cite the relevant summary item and concrete evidence, e.g. “formal reconstruction of Avicenna’s proof-search states and transitions,” “native-speaker ArabCulture benchmark across 13 countries,” or “Modern Hebrew joint parsing, not historical argument modeling.”

### MAJOR-6 — Explanations do not support the actual within-category ordering

There are only 20 unique explanations for 124 rows, and most category members share one sentence. Identical explanations cannot explain why S24P01 outranks S24P07, why S16P01 outranks S16P04, or why S17P05 outranks S17P06. The protocol requires 1–3 sentences naming the concrete feature that drove the ranking; a category slogan is not a paper-specific ranking rationale.

**Required correction:** make each explanation row-specific and identify the feature that distinguishes the score: directness to the project, artifact maturity, language/tradition coverage, formal-vs-cultural task fit, validation strength, or transfer limitation.

### MAJOR-7 — Confidence is materially overstated

The outputs assign `high` confidence to 110/124 rows, including conceptual proposals, broad surveys, adjacent Hebrew/Biblical/Christian infrastructure, duplicate records, and papers whose evidence basis is boilerplate. High confidence is not justified for claims about cross-tradition transfer or formal logical relevance when the underlying summaries explicitly state those limitations.

**Required correction:** use medium confidence for indirect or scope-limited relevance, and low/medium where the source is a proposal, emerging benchmark, duplicate publication, or has unresolved cultural-validity confounds.

### MINOR-8 — Duplicate study is ranked as independent support

S24P05 and S24P06 are the open/protocol and Cambridge-published versions of the same Langton stylometry study. The protocol says not to merge or invent paper IDs, so retaining both rows is correct; however, the review must mark them as duplicate evidence and must not let the pair inflate the apparent breadth or confidence of category 24. Both currently receive the same near-ceiling score as direct Islamic formalizations.

**Required correction:** retain both IDs but explicitly label the shared study, cap their combined evidentiary weight, and rank them as one research contribution for synthesis purposes.

### MINOR-9 — Source ID format is inherited-invalid and should be surfaced

`remaining_nonbenchmark.csv` contains IDs such as `16_01`, `12-01`, and `20_02`, while `ranking_protocol.md` specifies `S<category number, 2 digits>P<paper order, 2 digits>`. The reviewer correctly preserved the source IDs rather than renaming them, but the final ranking package should record this input validation exception. Any downstream consumer assuming the stated canonical ID grammar will fail or sort inconsistently.

**Required correction:** repair the upstream artifact or add an explicit compatibility exception; do not silently normalize IDs in these reviewer files.

## Positive findings

- Both CSVs contain exactly 124 rows and the same paper-ID set as `remaining_nonbenchmark.csv`.
- Required columns are present; category/global rank fields are populated in the intended file and blank in the other.
- Scores are integer values in the 0–100 range and ranks are unique in each relevant ranking.
- The evidence summaries themselves contain the right cautions: cultural benchmarks are not formal alternative logics; translation, language proficiency, knowledge, annotation, and reasoning are confounded; Islamic/Christian/Jewish computational work is sparse and heterogeneous. The ranking should be revised to preserve those cautions rather than erase them.

## Release recommendation

Do not accept the current ranking as final. Re-score at minimum categories 16, 17, and 24; rewrite all boilerplate explanations/evidence bases for those categories; mark the Langton duplicate; and recalibrate confidence. Then re-run the protocol checks and an adversarial pass specifically asking whether cultural difference has been mislabeled as logical difference and whether Western formal logic has been treated as the default yardstick.
