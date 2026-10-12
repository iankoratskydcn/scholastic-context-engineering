# Adversarial review — argument-form taxonomy ranking

## Verdict

**REVISE before accepting.** The two CSVs pass the mechanical ranking checks, but the substantive reasoning is not yet sufficiently paper-specific or form-sensitive for the stated viewpoint. The ranking often treats generic argument mining, structured knowledge, context engineering, or hallucination work as evidence about argument forms/deductive skeletons without identifying the actual form-level object, rule, premise–conclusion relation, scheme, defeater, proof trace, or derivation that transfers to the project.

## Mechanical checks

- Reviewed:
  - `ranking/review_argument_form_taxonomy_category.csv`
  - `ranking/review_argument_form_taxonomy_global.csv`
  - `ranking/remaining_nonbenchmark.csv`
  - `ranking/ranking_protocol.md`
- Both review files contain exactly 124 rows and exactly the 124 input paper IDs; no duplicates or missing IDs were found.
- Scores are integers in the required 0–100 range.
- Category ranks are unique within each category; global ranks are unique from 1–124.
- Equal-score tie breaks follow canonical `paper_id` order in both files.
- Explanations and evidence fields are non-empty, and the referenced summary files exist under `.hermes/lit_review/summaries/` (the CSV paths are relative to the `lit_review` root, not the `ranking` directory).
- No mechanical protocol defect was found.

## Findings

### 1. High — explanations are category templates, not concrete paper-level ranking reasons

The protocol requires a 1–3 sentence explanation naming the concrete feature that drove each paper's rank. Instead, the 124 rows collapse to only 20 unique explanation strings. Whole categories receive identical prose even when the source summaries explicitly distinguish direct predecessors, near misses, conceptual boundary-setting, annotation resources, and non-argumentative infrastructure.

Examples:

- `review_argument_form_taxonomy_category.csv:2-10` gives all nine hallucination papers the same explanation, despite the summaries distinguishing factuality taxonomies, conceptual definitions, calibration/abstention arguments, and lack of argument-form structure.
- `:19-30` gives all twelve compression papers the same explanation, although the summaries distinguish token pruning, latent memory, retrieval compression, and tool-context compression; none is itself an argument-form taxonomy or deductive-skeleton representation.
- `:49-62` gives all fourteen historical-logic papers the same explanation, despite materially different objects: syllogistic derivations, medieval consequence, relational syllogisms, Indian inference, Mohist disputation, and formal-language methodology.
- `:65-75` gives all eleven Toulmin/defeasible papers the same explanation, although some provide executable defeat semantics, some provide argument graphs and burdens of proof, some provide NLP extraction, and others are conceptual surveys.

The same templating appears in `review_argument_form_taxonomy_global.csv`. This makes the numerical ordering largely unauditable: the explanation does not say why one paper outranks another within the same category or why an indirect paper receives its particular cross-category position.

**Required correction:** rewrite explanations at paper level. Each should identify the actual transferable object and its limitation, for example: “provides a formal reduction calculus and derivation traces for Aristotelian syllogisms, but requires historical-schema adaptation”; or “uses scheme-conditioned RAG to translate natural-language arguments into computational arguments, making it a direct novelty comparator for scheme-aware context selection.”

### 2. High — generic argument mining is not separated from argument-form or deductive-skeleton reasoning

`S09P04` and `S09P05` are scored 88 and 82 (`category.csv:33-34`; `global.csv:21,33`). Their shared explanation says only that they provide “an extraction precedent for structured argument representations.” That is generic argument mining, not evidence that they encode or validate deductive skeletons.

The inspected source summary for Lawrence & Reed states that the survey covers components, relations, and schemes, but explicitly identifies the gap between component/relation classification and valid nonmonotonic inference (`summaries/09_argument_mining_summaries.md:10-12`). The same summary describes Lauscher et al. as a motivation for evidence interpretation and retrieval, while noting that it does not show that mined structure improves proof selection or context compression (`:12-13`).

These papers can be useful **landscape/baseline references**, but the current explanations overstate their transfer. The ranking should distinguish at least:

1. component/relation mining;
2. scheme/form classification;
3. explicit premise–conclusion or warrant reconstruction;
4. formal/deductive or defeasible proof evaluation;
5. use of the structure for context selection or compression.

Without that separation, generic extraction is being scored as though it were deductive-skeleton work.

### 3. High — Walton & Macagno is mischaracterized and likely over-ranked at global rank 1

`S10P02` is rank 1 with score 97 in both files (`category.csv:35`; `global.csv:2`). Its explanation calls it a “close precedent for argument-form taxonomy.” The source summary gives a more qualified result: it is a foundational taxonomy/methodology paper, explicitly distinguishes taxonomy classification from textual argument classification and from deductive validity, and is “not prior art for a learned context router” (`summaries/10_walton_schemes_nlp_summaries.md:7`).

A high score may be defensible for conceptual importance, but global rank 1 is not supported by the current project-relevance rationale because the paper does not provide an NLP classifier, extraction pipeline, deductive skeleton, retrieval mechanism, or context-budget objective. The explanation omits the exact limitation that should constrain its rank.

**Required correction:** either lower it relative to papers that actually instantiate or evaluate argument forms/proof structures, or explicitly justify a top conceptual-prior rank while labeling it as taxonomy groundwork rather than a direct system comparator.

### 4. High — the strongest direct novelty threat is substantially under-ranked

`S10P10` (Trajano et al.) receives score 68, category rank 4, and global rank 57 (`category.csv:38`; `global.csv:58`). Its explanation says only that it informs scheme classification and reconstruction of implicit premises.

The inspected summary identifies this paper as the **strongest direct novelty threat**: it classifies natural-language arguments by scheme, supplies scheme descriptions/examples as context to an LLM, uses retrieval-augmented generation, and translates arguments into computational representations (`summaries/10_walton_schemes_nlp_summaries.md:23`). It directly overlaps with the proposed combination of argument-form inference plus scheme-conditioned context. The summary's remaining gap is adaptive/uncertainty-aware retrieval, critical-question-aware compression, or explicit token-budget optimization—not absence of relevance.

A score of 68 and global rank 57 places this direct comparator below broad conceptual sources and many indirect context/knowledge papers. That ordering is difficult to reconcile with the stated viewpoint. The ranking needs either a materially higher placement or a paper-specific explanation of why its direct overlap is outweighed.

### 5. Medium-high — indirect scaffolding papers are presented as deductive-skeleton evidence without enough qualification

Several papers receive medium scores while their explanations imply a direct relation to normalized argument representations:

- `S13P01–S13P03` score 58, 55, and 52 (`category.csv:41-43`; `global.csv:68-75`). Their shared explanation says structured entities/relations/evidence “can support normalized argument representations.” The summaries instead describe internal knowledge-enhanced pretraining, KG injection, and joint embeddings; they explicitly note that these methods do not expose a query-specific evidence graph or guarantee traceable support (`summaries/13_knowledge_graphs_summaries.md:5-12`). These are context/evidence scaffolds, not argument-form or deductive-skeleton precedents.
- `S01P01–S01P09` and `S04P01–S04P12` use generic statements about validating links or preserving premises (`category.csv:2-10,19-30`). The supplied source summaries concern hallucination definitions or context compression; they do not establish an argument-form ontology, scheme classifier, or proof object.
- `S22P01–S22P15` are mostly corpus/transcription/provenance resources (`category.csv:97-106`). Their low scores are directionally sensible, but the explanation still says they are needed before historical arguments can be extracted without identifying which resource provides argument-form labels, derivations, or proof alignment. Most provide prerequisites, not evidence for the taxonomy itself.

These papers should be marked as indirect enabling infrastructure, with scores and explanations reflecting distance from the target object. Do not let “structured,” “evidence,” “reasoning,” or “skeleton” substitute for a demonstrated form-level representation.

### 6. Medium — evidence basis is auditable only at coarse summary-section granularity

The evidence fields satisfy the literal requirement by pointing to summary files and retained-paper sections, but nearly every row ends with the same phrase: “inspected source-artifact summary and its stated contribution/limitation.” The basis does not identify the paper-specific evidence within the summary, nor does it preserve the key limitation that often determines rank.

This is especially problematic for the direct-comparator and generic-mining cases above. For example, the Trajano row should point to the summary's scheme-conditioned RAG/translation description and direct novelty-threat statement; S09P04 should point to the component/relation-versus-valid-inference limitation; and S13P01 should point to the lack of query-specific traceable evidence. The report does not require external web verification because the local summaries are the declared evidence source, but the CSV should provide enough detail to reproduce the ranking judgment from those summaries.

## Sample evidence matrix

| Paper | Current rank/score | What the local summary actually supports | Adversarial assessment |
|---|---:|---|---|
| S10P02 Walton & Macagno | global 1 / 97 | Foundational scheme taxonomy; explicitly separates taxonomy, textual scheme classification, and deductive validity; not a learned context router (`summaries/10_walton_schemes_nlp_summaries.md:7`). | High conceptual value, but current rationale overstates direct system relevance. |
| S10P10 Trajano et al. | global 57 / 68 | Scheme classification + scheme descriptions/examples as LLM context + RAG + computational-argument translation; strongest direct novelty threat (`summaries/10_walton_schemes_nlp_summaries.md:23`). | Under-ranked for this viewpoint unless an explicit counterweight is added. |
| S09P04 Lawrence & Reed | global 20 / 88 | Survey of components/relations/schemes; extraction is not valid nonmonotonic inference (`summaries/09_argument_mining_summaries.md:10-12`). | Generic mining/landscape source, not a direct deductive-skeleton method. |
| S09P05 Lauscher et al. | global 32 / 82 | Scholarly argument units/relations motivate evidence interpretation, but no proof-selection, compression, or LLM reasoning experiment (`summaries/09_argument_mining_summaries.md:12-13`). | Useful adjacent survey; score/rationale should state the missing proof layer. |
| S13P01 ERNIE | global 67 / 58 | Knowledge-enhanced pretraining; no query-specific evidence graph or claim traceability (`summaries/13_knowledge_graphs_summaries.md:5-6`). | Indirect scaffold, not an argument-form precedent. |
| 18_06 Carneades | global 9 / 92 | Argument graphs, premises, assumptions, exceptions, audiences, proof standards, burdens, and critical questions; structured arguments are presupposed rather than extracted (`summaries/18_toulmin_defeasible_summaries.md:15-16`). | Strong representational precedent; explanation should name these concrete fields and extraction limitation. |
| 16_01 Aristotle, *Prior Analytics* | global 2 / 96 | Terms, premises, figures, moods, conversion, reduction, demonstration, and derivation structure; historical encoding must preserve source/translation uncertainty (`summaries/16_historical_logics_summaries.md:5`). | Strong deductive-form source; current generic historical-logic sentence underspecifies why it ranks here. |

## Recommended repair rubric

Re-score or at least rewrite each row using explicit dimensions:

- **Form object:** scheme, syllogistic mood, rule, premise–conclusion pattern, Toulmin role, defeater, dialogue transition, or none.
- **Skeleton explicitness:** whether the source exposes a derivation/proof graph, warrant edge, attack/defeat relation, or only latent/undifferentiated context.
- **Operational evidence:** extraction/classification, formal validation, proof search, retrieval/context selection, compression, or none.
- **Transfer distance:** direct argument-form/deductive-skeleton precedent, adjacent argument mining, enabling evidence infrastructure, or conceptual background.
- **Novelty threat:** whether the paper already combines form inference with retrieval, context construction, or LLM reasoning.
- **Limitation:** what the source does not provide and why that matters for the project.

The current files can be retained as mechanically valid drafts, but they should not be treated as an adversarially defensible final ranking until the explanations and the top cross-category ordering are revised against these dimensions.
