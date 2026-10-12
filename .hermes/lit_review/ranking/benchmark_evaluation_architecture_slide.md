# Slide: How We Evaluate the Scholastic Context Engine

## Slide purpose

Explain that evaluation uses three complementary layers:

1. **Composite stage benchmarks** diagnose individual capabilities.
2. **One integrated project-owned benchmark** tests the complete Scholastic Context Engine workflow.
3. **One generic reasoning benchmark** calibrates the system against established general reasoning performance.

## Suggested slide title

**A Layered Benchmark Strategy: Diagnose, Test, Calibrate**

## Core visual

Use a three-layer horizontal architecture or funnel:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  1. COMPOSITE STAGE BATTERY                                                 │
│  Diagnose each capability independently                                      │
│                                                                             │
│  Attribution · Argument structure · Deduction · Premise selection            │
│  Compression · Provenance · Cross-source synthesis · Strength comparison    │
│  Objections/replies · Scholastic structure · Cross-tradition transfer       │
└─────────────────────────────────────────────────────────────────────────────┘
                                      ↓
┌─────────────────────────────────────────────────────────────────────────────┐
│  2. INTEGRATED PROJECT-OWNED BENCHMARK                                      │
│  Test the complete pipeline on authentic scholarly sources                   │
│                                                                             │
│  Sources → Claims → Forms → Skeletons → Provenance → Compression             │
│          → Synthesis → Strength comparison → Full disputation               │
└─────────────────────────────────────────────────────────────────────────────┘
                                      ↓
┌─────────────────────────────────────────────────────────────────────────────┐
│  3. GENERIC REASONING CONTROL                                                │
│  Calibrate against an established external benchmark                        │
│                                                                             │
│  Example: FOLIO                                                             │
│  General deductive competence ≠ proof of provenance, synthesis, or          │
│  scholastic faithfulness                                                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Layer 1: Composite stage battery

### Label

**Composite stage battery — Where does the system fail?**

### Content

Show small benchmark-family labels arranged along the pipeline:

- **Claims and attribution:** claim ownership, reported speech, citation faithfulness
- **Argument structure:** components, relations, schemes, alternative parses
- **Deduction:** FOLIO, P-FOLIO, ProofWriter, LeanDojo/ReProver
- **Selection and compression:** premise selection, LongPiBench, LLMLingua, dependency ablations
- **Grounding and provenance:** RAGTruth, evidence graphs, citation alignment
- **Synthesis:** multi-document reasoning, common ground, premise equivalence
- **Strength:** pairwise argument quality, expert comparison, partial-order judgments
- **Dialogue and disputation:** counterarguments, objections, replies, dialogue-game transitions
- **Authentic transfer:** Index Thomisticus Treebank / UD Latin-ITTB, multilingual and cross-tradition resources

### Supporting sentence

> Composite benchmarks provide diagnostic coverage and separate failure attribution.

## Layer 2: Integrated benchmark

### Label

**Integrated project-owned benchmark — Does the whole system work?**

### Content

Show the complete workflow as a single connected arrow:

```text
authentic multi-source text
→ attribution-aware claims
→ argument forms
→ premise/conclusion graph
→ provenance links
→ selected context
→ compressed context
→ novel synthesis
→ strength comparison
→ objections / sed contra / respondeo / replies
```

Add a small callout listing required evaluation conditions:

- raw context;
- selected context;
- compressed context;
- distractor context;
- dependency-ablation context;
- alternative valid parses;
- source-span lineage;
- intermediate reasoning artifacts;
- final grounded disputation.

### Supporting sentence

> The integrated benchmark tests the project’s actual contribution: structured, provenance-preserving reasoning over authentic scholarly material.

## Layer 3: Generic reasoning control

### Label

**Generic reasoning control — How does it compare to established reasoning systems?**

### Content

Use **FOLIO** as the illustrative external control:

- natural-language premise sets;
- first-order logic labels;
- executable verification;
- established comparison point for deductive reasoning.

Add a warning icon or contrasting color around this statement:

> Strong generic reasoning is necessary, but it does not establish provenance tracking, cross-source synthesis, argument-strength comparison, or scholastic-output faithfulness.

## Bottom-line callout

Place a bold banner across the bottom:

> **Composite benchmarks diagnose. The integrated benchmark tests. The generic benchmark calibrates.**

## Speaker notes

The evaluation should not be reduced to a single pooled score. Each benchmark family answers a different question. The composite battery tells us which component fails. The integrated benchmark tests whether the components remain coherent when composed around authentic philosophical and scholastic sources. The generic benchmark gives us an external sanity check against established reasoning evaluations.

The key methodological point is that FOLIO—or any other generic reasoning benchmark—cannot stand in for the full Scholastic Context Engine. A model may solve formal reasoning problems while losing attribution, provenance, implicit premises, source dependencies, or the structure of a scholastic disputation. Conversely, a system may produce persuasive prose while failing formal validity or evidence preservation. The layered design exposes both types of failure.

## Optional short version for the slide itself

### **Layered evaluation**

**Diagnose:** Composite benchmarks for attribution, argument structure, deduction, provenance, compression, synthesis, strength, and disputation.

**Test:** One integrated benchmark over authentic sources, intermediate artifacts, provenance, dependency ablations, and full scholastic outputs.

**Calibrate:** One generic reasoning benchmark such as FOLIO for external comparison.

> **Diagnose the parts. Test the whole. Calibrate against the field.**
