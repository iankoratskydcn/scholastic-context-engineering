# S24P01 adversarial relevance review

## Scope and verdict

- **Paper:** Hodges (2010), “Ibn Sīnā on Analysis: 1. Proof Search. Or: Abstract State Machines as a Tool for History of Logic.”
- **Identity:** passed. Exact DOI metadata and the downloaded repository PDF agree with the retained record (`next7_retry/identity_checks.csv:3`; DOI `10.1007/978-3-642-15025-8_18`).
- **Aggregate rank:** 24.
- **Verdict:** **retain_high**.
- **Confidence:** high.

`retain_high` is stage-specific. This paper is a strong demonstrated precedent for historically grounded formal/proof reconstruction and provenance-linked state transitions. It is **not** a complete cross-tradition context-engineering or LLM pipeline.

## Demonstrated mechanism

Hodges translates and interprets Ibn Sīnā’s *Qiyās* §9.6, whose 64 problems concern completing and analyzing syllogisms. The paper states that it extracts the essential ingredients of an Abstract State Machine from the Arabic source and gives a translation of the passage (PDF text lines 16789–16797). It then makes the procedure explicit rather than leaving it as historical description:

- formal syllogistic sentences and entailment relations;
- goal–datum pairs with missing-premise gap sites and left/right edges;
- synthesis by replacing adjacent premises with a strongest consequence;
- ramification over candidate fills;
- selection and success/failure reports;
- prior/next page links that preserve the search path and permit reconstruction of the connected syllogism;
- an asynchronous multi-agent ASM for cases requiring alternative determinate middle terms.

The review section describes these state transitions directly (PDF text lines 17871–18010). Appendix C gives the ASM signature and rules, including `datum`, `gapsite`, `edges`, `fill`, `previous`, `next`, and the `Describe`, `Synthesise`, `Ramify`, and `Select` modules (PDF text lines 18726–18839). The logical part was implemented in Perl 5 and run on all 64 problems; the paper reports discrepancies at Problems 23, 33, 51, 61, and 62, with Problem 33 outside the algorithm’s domain and the other discrepancies discussed as possible manuscript or edition errors (PDF text lines 18742–18751).

## Hostile pipeline test

### Source-span extraction

**Partial/direct only.** The source-to-model link is unusually strong for a historical study: the Arabic passage is translated, interpreted, and mapped to formal ingredients. However, the author performs the extraction manually. There is no automatic sentence/span detector, alignment system, annotation protocol, or corpus-scale extraction evaluation.

### Cross-tradition formal reasoning

**Direct for one Islamic logical procedure; transfer beyond it.** The work is specifically grounded in Ibn Sīnā’s Arabic-Persian logic and preserves the distinction between the historical text, translation, interpretation, and formal ASM. It does not compare traditions or classify kalām, Jewish, or Christian scholastic forms.

### Proof-search state transitions

**Direct and strong.** This is the paper’s core contribution. It does not merely discuss proof search: it exposes state variables, transition modules, branching, failure, and dependency links, and provides executable rules. The model is inspectable at the level needed to audit how a proof candidate was constructed.

### Dependency/provenance-preserving context selection/compression

**Direct dependency representation; no context compression.** The goal, datum, gap, candidate fill, strongest-consequence reduction, and previous/next page links preserve proof-search dependencies. This is a strong formal analogue for dependency-safe context construction. It does not select or compress natural-language source passages under a token budget, nor does it test proof sufficiency after deletion or compression.

### Downstream inspectable philosophical reasoning

**Direct for inspectable symbolic reasoning; absent for LLM evaluation.** The output is a reconstructed syllogistic proof/search result with explicit success/failure conditions and a recoverable connected syllogism. There is no language-model generation, philosophical QA, human evaluation, or downstream reasoning benchmark.

### Novelty threat

**High for the formal/provenance stage.** Any claim that the project is the first to turn a historically situated Islamic logical procedure into an executable, inspectable proof-search state machine is contradicted. The paper is a concrete benchmark for what source-grounded formal reconstruction, missing-premise handling, and dependency-preserving search can look like.

The novelty threat is lower for automated context engineering: no learned extractor, retriever, compressor, cross-tradition classifier, or LLM is demonstrated.

## Limitations and failure boundaries

1. The domain is narrow: Avicennan categorical/propositional syllogistic analysis, not open-ended scholastic argument.
2. The source procedure is reconstructed by expert interpretation; ambiguous or missing historical instructions are completed by the author’s modeling choices.
3. The author explicitly reports five discrepancies against the Cairo text’s solutions; one falls outside the modeled domain, while the others may reflect transcription or edition problems.
4. The `hasils`/determinate-sentence source is partly external to the historical procedure, and the multi-agent “Active Intellect” construction is an ASM abstraction rather than a demonstrated historical implementation.
5. There is no automatic source-span lineage, context budget, sufficiency/minimality metric, cross-tradition validation, or downstream LLM evaluation.

## Adjudication

Retain as **high** because the demonstrated mechanism is concrete, source-grounded, executable, and directly relevant to the project’s formal/provenance stage. Do not describe it as evidence that the integrated pipeline already solves natural-language extraction, proof-aware compression, comparative classification, or philosophical LLM reasoning.

## Evidence

- `ranking/verification_runs/next7_retry/identity_checks.csv:3`
- `ranking/verification_runs/next7_retry/raw/S24P01.pdf.txt:16782-16818`
- `ranking/verification_runs/next7_retry/raw/S24P01.pdf.txt:16946-16969`
- `ranking/verification_runs/next7_retry/raw/S24P01.pdf.txt:17871-18010`
- `ranking/verification_runs/next7_retry/raw/S24P01.pdf.txt:18726-18751`
- Downloaded PDF: `ranking/verification_runs/next7_retry/evidence/S24P01.pdf`, pp. 354–404
