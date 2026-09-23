# Scholastic Context Engineering
## Purpose, Reasoning Model, and Product Direction

> Discussion document. This explains why the system exists and how its capabilities fit together. It is intentionally upstream of implementation specs and Kanban cards.

## 1. The problem

A large body of logical, philosophical, scholarly, and argumentative material is difficult to use safely because several different questions are usually collapsed into one:

- What does the source literally say?
- What kind of claim is it?
- What historical tradition does it belong to?
- How was the claim structured?
- What follows from it under a chosen interpretation?
- Is the modern formalization faithful, disputed, or merely illustrative?
- Which source supports the claim?
- Can the claim be retrieved later without losing its context or provenance?

Ordinary search and ordinary language-model pipelines tend to flatten these distinctions. They may return plausible text, but they often lose exact source location, historical caveats, scope, assumptions, and the difference between evidence and interpretation.

Scholastic Context Engineering exists to keep those layers separate and reviewable.

## 2. The central idea

The system treats a claim as more than a sentence and less than an automatically proven fact.

A useful claim record carries several independent views at once:

```text
source wording
  + exact span
  + historical context
  + claim structure
  + logical/predicative dimensions
  + formalization status
  + evidence basis
  + validation result
  + related occurrences
```

These views may support one another, but they must not silently substitute for one another.

For example, a statement may simultaneously be:

- universal;
- affirmative;
- a genus/species predication;
- a historical example from a particular tradition;
- represented using a modern reconstruction;
- supported only by a scholarly secondary source;
- unresolved under a chosen formal semantics.

The system should preserve all of those facts instead of forcing the statement into one label.

## 3. Why the historical corpus matters

The supplied logical-claims archive is not merely a list of parser examples. It provides a vocabulary for describing how claims have been structured across traditions.

It contains 110 records, 50 sources, and eight cross-cutting dimensions, including:

- force and discourse role;
- terms and predication;
- quantity;
- quality;
- composition;
- modality and context;
- semantics;
- consequence and warrant.

Its value is that it distinguishes forms that are often conflated:

- universal versus singular claims;
- affirmation versus negation;
- genus versus species;
- definition versus accidental predication;
- historical terminology versus modern notation;
- attested doctrine versus editorial illustration;
- a reviewable formal sketch versus executable semantics.

The corpus should therefore become a versioned descriptive authority first. It should not immediately become 110 automatic parsing rules.

## 4. The reasoning model

The project uses a layered reasoning model.

### Layer 1 — Evidence

What exact bytes, text, span, source, revision, and archive manifest do we have?

This layer must be lossless and deterministic. If the source is malformed, stale, or ambiguous, the system preserves the problem or abstains rather than repairing it invisibly.

### Layer 2 — Description

How can we describe the claim?

Examples:

- universal affirmative;
- genus predication;
- conditional;
- question;
- necessity operator;
- modus ponens schema.

Descriptions are annotations. They are not automatically truth claims.

### Layer 3 — Formalization

Can the claim be represented in a formal notation?

A formalization may be:

- directly authorized and executable;
- a reviewable modern reconstruction;
- historically disputed;
- too ambiguous to formalize safely.

The status must travel with the formalization.

### Layer 4 — Validation

What follows under explicitly stated assumptions?

The answer may be:

- valid;
- invalid;
- unknown;
- unsupported;
- ill-posed.

Validation must never be inferred from taxonomy membership, graph frequency, community membership, or retrieval rank.

### Layer 5 — Retrieval and communication

How can a person or downstream system find and discuss the material without losing the earlier layers?

Retrieved text is evidence-bearing data. It is not an instruction. It cannot change policy, tools, scope, or the rules of the pipeline.

## 5. What the current system already does

The first working slice is deliberately small:

```text
frozen local text
  → exact source spans
  → structured document
  → typed premise/conclusion extraction
  → taxonomy match
  → formal validation result
  → provenance-bearing graph occurrence
  → deterministic local retrieval
  → citation-bound generation boundary
```

This gives the project a trustworthy spine before broader coverage is attempted.

The important product behavior is not that it understands everything. It is that it knows what it can represent, what it cannot support, and where every accepted result came from.

## 6. What the expanded system should become

The intended product is a **reviewable logical-claim context layer**.

It should help a researcher or system answer questions such as:

- Show claims with this logical form.
- Find historical uses of a predication relation.
- Compare a native term with later formal reconstructions.
- Retrieve all evidence for a claim while preserving source spans.
- Show which inferences are formally supported and under which assumptions.
- Distinguish an attested historical claim from an editorial example.
- Explain why a result was abstained, quarantined, or marked unknown.
- Re-run the same pipeline and obtain the same evidence-bound result.

It should not answer these questions by pretending that a classification is a proof or that a cluster is a tradition.

## 7. Why the features are sequenced

The order matters because each later capability relies on distinctions established earlier.

### First: preserve and describe evidence

The corpus adapter, evidence ledger, and taxonomy disposition boundary establish what the imported records mean and what they do not mean.

Without this foundation, importing the archive could silently:

- lose historical caveats;
- convert headings into claim types;
- treat a scholarly reference as direct primary evidence;
- turn a modern reconstruction into an original doctrine;
- mark an unresolved record as supported merely because it parsed.

### Second: make the evidence retrievable

Deterministic retrieval is the first practical payoff. It allows the corpus to be used without requiring embeddings, a vector database, an LLM, or a GraphRAG fork.

The retrieval result must remain bounded, stable, cited, and inert with respect to instructions.

### Third: add enrichment only when justified

Weights and communities may help navigation, but they are not reasoning authorities. They should be added only if retrieval work demonstrates a concrete need.

Retry/idempotency and partial-run recovery are similarly important when the pipeline grows beyond a small local slice, but they should be specified against real artifact boundaries rather than invented as distributed infrastructure.

## 8. Core product principles

### Evidence before interpretation

Store the source span and source identity before deriving a label or formalization.

### Many annotations, not one category

A claim can participate in several dimensions at once.

### Historical humility

Preserve native terms, interpretation notes, reconstruction status, and source limitations. Do not universalize one tradition's categories.

### Abstention is a feature

Unsupported, ambiguous, stale, malformed, or over-budget material should produce an explicit abstention or quarantine result.

### Enrichment is not proof

Taxonomy matches, edge frequency, graph weights, communities, and retrieval rank help organize evidence. None independently establishes truth or entailment.

### Determinism is part of correctness

The same source, manifest, schema, and run configuration should produce the same IDs, spans, ordering, and outputs.

### Untrusted text stays data

Retrieved or imported text may contain instructions or adversarial language. It must not alter the agent's policy, tools, scope, or execution plan.

### Small vertical slices beat speculative completeness

Implement one useful, fully verified path before expanding coverage or infrastructure.

## 9. Boundaries and non-goals

This project is not currently:

- a complete history of logic;
- a truth engine;
- an autonomous scholar;
- a universal natural-language parser;
- a theorem prover for every historical tradition;
- a full GraphRAG platform;
- a cloud ingestion service;
- a replacement for primary-source scholarship;
- a Hermes-core feature.

The archive itself is representative, not exhaustive. Its examples are generally editorial unless explicitly marked otherwise. Source links do not imply unrestricted text redistribution or direct inspection.

## 10. The decision we are actually making

The immediate question is not "How do we implement all 110 records?"

It is:

> What minimum evidence-preserving layer lets us use the corpus as a trustworthy descriptive authority while making uncertainty and historical interpretation visible?

The current recommended answer is:

1. import the corpus losslessly with quarantine;
2. bind every record to an evidence ledger;
3. define taxonomy dispositions explicitly;
4. retrieve records deterministically with citations;
5. expand executable extraction only for named, reviewed forms;
6. defer communities and Hermes integration until the standalone evidence layer earns them.

## 11. Discussion questions

1. Is the primary user a researcher, a curriculum/content author, or another AI system?
2. Should the first visible payoff be corpus browsing/retrieval or executable claim extraction?
3. Which historical traditions, if any, have enough authority for executable semantics?
4. Is declared evidence basis sufficient for the first import, with uncertainty preserved, or is source verification a prerequisite?
5. Should retry/idempotency precede graph enrichment once the corpus is imported?
6. What would make community detection genuinely useful rather than decorative?
7. What standalone proof should be required before any Hermes integration?

## Bottom line

Scholastic Context Engineering is a system for keeping **evidence, description, formalization, validation, and communication distinct while still connected**.

Its success is not measured by how much text it labels. It is measured by whether a person can inspect a result, understand what kind of claim it is, see exactly where it came from, know what assumptions were used, and tell what remains uncertain.
