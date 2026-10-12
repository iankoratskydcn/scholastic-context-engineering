# Adversarial review — hallucination-mitigation ranking

## Verdict

**FAIL — structurally valid, but not release-ready as a hallucination-mitigation ranking.** The direct hallucination papers are generally placed at the top, yet the score semantics drift across generic factuality, provenance/authorship detection, formal reasoning, corpus infrastructure, argument structure, and language-quality evaluation. The CSVs do not consistently distinguish reducing unsupported/invalid model outputs from studying whether text is factual, fluent, stylistically human, or formally representable.

## Verification performed

- Compared `review_hallucination_mitigation_category.csv` and `review_hallucination_mitigation_global.csv` with `remaining_nonbenchmark.csv` and `ranking_protocol.md`.
- Confirmed all three CSVs contain 124 data rows; the two review files have exactly the expected 124 paper IDs, with no missing, extra, or duplicate IDs.
- Confirmed scores are integers in `0–100`, explanations/evidence are non-empty, and category/global rows agree on shared metadata, scores, explanations, and evidence.
- Confirmed category ranks are contiguous and unique within every category, global ranks are unique `1–124`, required rank columns are blank/populated in the correct files, and global ordering is monotone by score with canonical-ID tie handling.
- Confirmed the protocol's 1–3 sentence explanation constraint is met.

These checks establish format and rank integrity only; they do not establish that the scores measure hallucination mitigation.

## Findings

### 1. High — the ranking conflates hallucination mitigation with generic factuality, provenance, and language quality

The stated viewpoint is “Mitigating hallucination in precise philosophical and deductive reasoning,” but many explanations use broad wording such as “reducing unsupported claims or invalid steps” without identifying an intervention, verifier, refusal/abstention behavior, premise check, contradiction test, or hallucination-specific outcome (`review_hallucination_mitigation_category.csv:31–38, 41–47, 76–88`). The ranking therefore treats several distinct constructs as interchangeable:

- factuality/reference correctness (`20_10`, `20_11`);
- authorship/provenance detection (`20_01`, `20_03`, `20_07`, `20_08`, `20_09`);
- genre, style, and linguistic quality (`20_02`, `20_04`, `20_05`);
- formal expressivity or historical logic (`16_*`, `18_*`);
- corpus/HTR/search infrastructure (`22_*`, `24_*`).

The source summaries explicitly warn against this collapse. Category 20 separates fluency, format compliance, factuality, and authorship detection (`summaries/20_ai_academic_writing_summaries.md:3–5, 7–9, 11–13`), while the hallucination summary distinguishes premise validation, logical-error localization, factuality, and formal proof validity (`summaries/02_logic_hallucination_summaries.md:9–11, 17–19, 41–47`). The reviewer should score direct hallucination mechanism/mitigation separately from adjacent reliability value.

### 2. High — direct hallucination precedents are not separated from formal or conceptual transfer

Category 2 is tightly aligned with the viewpoint: false-premise, negation, false-entailment, perturbation robustness, and logical-consistency detection papers score 97–100 (`S02P02–S02P09`). In contrast, category 18 assigns 89–98 to formal defeasible-logic and argumentation papers, and category 23 assigns 90–95 to formal dialogue/argumentation surveys (`review_hallucination_mitigation_global.csv:4–15, 47–60, 72–74`). Those papers are valuable design precedents, but their evidence says they presuppose structured inputs and do not evaluate LLM hallucination or natural-language extraction (`summaries/18_toulmin_defeasible_summaries.md:4–33`; `summaries/23_disputatio_dialectical_ai_summaries.md`). A formal proof calculus can support mitigation, but it is not itself evidence that a model hallucinates less. Scores need an explicit directness penalty or a decomposed rubric for (a) demonstrated hallucination mitigation, (b) verifier/formal transfer, and (c) domain/context transfer.

### 3. High — generic explanations do not justify fine-grained scores

At least 40 rows use the same evidence basis: `source artifact describes a scholarly, formal, conceptual, survey, normative, or comparative study without a benchmark-producing artifact` (`review_hallucination_mitigation_category.csv:49–75, 97–122`; corresponding global rows). This text only establishes absence of a new benchmark; it does not establish hallucination mitigation, factuality, formal validity, or transfer value. The repeated explanation templates likewise cannot explain distinctions such as 98 versus 89 within category 18 or 83 versus 74 within category 24.

The protocol requires evidence pointing to source summary or paper evidence and explanations naming the concrete feature that drove the rank. Replace the generic strings with paper-specific evidence: e.g. formal defeaters and burden-of-proof semantics, executable reduction rules, HTR error rate, linked-data identifiers, or the exact human-evaluation design—and state whether the feature is direct mitigation or only upstream transfer.

### 4. High — high scores are assigned to papers whose evidence explicitly denies direct hallucination relevance

Several high-ranked rows are scored as if formalization or infrastructure directly reduces model hallucinations even though the source summaries describe a different contribution. Examples:

- `18_06` receives 98 for Carneades, although its summary says the model presupposes structured arguments and does not extract them from language or evaluate LLM answers (`summaries/18_toulmin_defeasible_summaries.md:15–16`).
- `S23P01–S23P03` receive 90–95 for formal dialogue/argumentation work, while the category evidence identifies no benchmark and no LLM mitigation experiment (`review_hallucination_mitigation_category.csv:107–109`).
- `S22P07`, `S22P09–S22P15`, and several category-24 rows receive 39–44 or 74–83 using “domain-specific evidence relevant to reliable reasoning,” although the digital-humanities summary explicitly says linked data, searchable corpora, transmission projects, and HTR do not recover or validate scholastic inferences (`summaries/22_scholastic_digital_humanities_ai_summaries.md:27–37, 39–61`).

These may be useful prerequisites or novelty constraints, but the explanation must not imply demonstrated mitigation. Reclassify them as indirect transfer/infrastructure and lower confidence where the score depends on an untested bridge.

### 5. High — category 20 contains direct factuality evidence but is mixed with non-mitigation studies

The category-20 cluster ranges from fabricated-reference audits (`20_10`, `20_11`) to authorship detection, stylistic convergence, essay quality, and normative authorship analysis (`20_01–20_13`). The source summary gives materially different constructs and limitations: fabricated references directly motivate claim/reference audits, while essay quality, rhetorical moves, style, and authorship classification do not measure factuality or invalid inference (`summaries/20_ai_academic_writing_summaries.md:7–9, 15–21, 27–37, 39–53`).

The current scores (58–64) and mostly identical generic evidence do not show whether the reviewer is rewarding direct hallucination detection, evaluation-design caution, or philosophical-domain adjacency. Split this cluster into at least: citation/reference hallucination; factuality/provenance detection; language/genre quality; and normative/accountability work. Do not let the latter categories contribute as if they were mitigation methods.

### 6. Moderate-high — context and compression papers are treated as hallucination mitigation without outcome evidence

The 15 rows in categories 3–4 score 59–69 and are described as providing “context utilization and retrieval robustness” or “context selection/compression with possible faithfulness impact” (`review_hallucination_mitigation_category.csv:16–30`). These are plausible risk factors and intervention surfaces, but “possible faithfulness impact” is not evidence of reduced hallucination. The explanations do not identify whether the cited studies measured unsupported claims, entailment, citation support, logical validity, or merely retrieval/efficiency/answer accuracy. The ranking should mark these as indirect context-reliability mechanisms unless the source evidence reports hallucination- or faithfulness-specific outcomes.

### 7. Moderate — evidence confidence is overconfident for indirect and uncertain records

Most rows are labeled `high`, including conceptual analyses, historical works, corpus infrastructure, and records whose evidence basis explicitly says no benchmark or empirical evaluation is established (`review_hallucination_mitigation_category.csv:49–75, 97–122`). Confidence should express confidence in the comparative hallucination-mitigation score, not merely confidence that a citation belongs in the review. `S02P08` and `S10P10` are appropriately low-confidence, but similar uncertainty applies to many cross-category comparisons and to rows where the source summary says the method is not a hallucination detector or does not evaluate LLM behavior.

### 8. Moderate — no explicit negative-evidence accounting

Explanations are overwhelmingly positive (“provides ... for reducing unsupported claims”) and omit limitations that directly affect mitigation transfer. The source summaries identify important negatives: NLI is only a proxy for proof (`summaries/02_logic_hallucination_summaries.md:17–19`); formal argument systems presuppose structured arguments and do not validate extraction (`summaries/18_toulmin_defeasible_summaries.md:15–18, 29–31`); linked data does not encode premises, conclusions, or validity (`summaries/22_scholastic_digital_humanities_ai_summaries.md:27–29`); and authorship detection does not establish factuality or argument validity (`summaries/20_ai_academic_writing_summaries.md:27–37`). A defensible score must balance direct strength against these transfer threats.

## Recommended disposition

- Preserve the CSV structure and rank arithmetic; no mechanical defect was found.
- Re-score or annotate every paper with a directness class: **direct hallucination mitigation/detection**, **factuality or citation reliability**, **formal verifier/argument representation**, **context/retrieval risk factor**, **corpus/infrastructure prerequisite**, or **generic language/provenance quality**.
- Replace the 40 generic evidence bases and repeated explanations with source-specific evidence and explicit limitations.
- Revisit the global ordering after separating direct mitigation from indirect transfer; in particular, audit the relative placement of category 2, category 18, category 20, category 22–24, and context-compression rows.
- Treat the current output as a structured draft, not an authoritative hallucination-mitigation ranking.
