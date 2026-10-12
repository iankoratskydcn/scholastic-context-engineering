# Slide Description: Benchmark Architecture for the Scholastic Context Engine

## Slide title

**How We Evaluate the Scholastic Context Engine**

## Core message

**Composite benchmarks diagnose each stage; one integrated benchmark tests the complete pipeline; one generic reasoning benchmark provides external calibration.**

## Recommended visual layout

Use a **three-column architecture** with a horizontal flow arrow across the bottom.

```text
┌────────────────────────┐   ┌────────────────────────┐   ┌────────────────────────┐
│  1. COMPOSITE BATTERY  │   │  2. INTEGRATED TEST     │   │  3. GENERIC CONTROL     │
│                        │   │                        │   │                        │
│  Diagnose each stage:  │   │  Test the full chain:   │   │  Calibrate against      │
│  • attribution         │   │                        │   │  general reasoning:     │
│  • argument structure  │   │  authentic sources     │   │                        │
│  • deduction           │   │  → claims + attribution│   │  FOLIO or equivalent    │
│  • provenance          │   │  → argument forms     │   │                        │
│  • retrieval           │   │  → proof skeletons     │   │  External comparability │
│  • compression         │   │  → provenance          │   │  and sanity check       │
│  • synthesis           │   │  → compression         │   │                        │
│  • strength            │   │  → synthesis           │   │  NOT proof of the       │
│  • disputation         │   │  → strength            │   │  project-specific       │
│                        │   │  → disputation         │   │  capabilities           │
│  Shows WHERE the       │   │                        │   │                        │
│  system fails.         │   │  Shows WHETHER the     │   │                        │
│                        │   │  system works as a     │   │                        │
│                        │   │  complete system.      │   │                        │
└────────────────────────┘   └────────────────────────┘   └────────────────────────┘
                 ───────────────►  triangulated evidence  ◄───────────────
```

## Column 1: Composite stage battery

Label this column **“Diagnose the parts”**.

Show the benchmark families as compact stacked tags:

- Claim extraction and attribution
- Argument components and relations
- Deduction and proof structure
- Premise selection
- Provenance and citation faithfulness
- Context selection and compression
- Cross-source evidence aggregation
- Argument strength comparison
- Counterargument and reply generation
- Scholastic disputation structure
- Cross-tradition transfer

Small caption:

> **Separate metrics reveal the failure location.**

Mention the currently verified controls in a small footer:

> FOLIO · LongPiBench · PCBench · MISSCI PLUS · LeanDojo/ReProver · ITTB/UD Latin-ITTB

## Column 2: Integrated end-to-end benchmark

Make this the visually dominant column because it represents the project’s contribution.

Display the pipeline as a vertical or diagonal chain:

```text
authentic sources
      ↓
claims + attribution
      ↓
argument forms + skeletons
      ↓
provenance-linked selection
      ↓
dependency-safe compression
      ↓
cross-source synthesis
      ↓
strength comparison
      ↓
quaestio → objections → sed contra → respondeo → replies
```

Under the chain, show the required test conditions:

- raw context
- selected context
- compressed context
- distractor context
- dependency-ablation context

Small caption:

> **One benchmark tests whether the stages compose without losing truth, structure, or provenance.**

## Column 3: Generic reasoning control

Label this column **“Calibrate the system”**.

Primary example:

> **FOLIO**
>
> Natural-language premises, first-order logic labels, explanations, and executable verification.

Caption:

> **Useful for external comparison—but not sufficient evidence of scholarly provenance, cross-source synthesis, or scholastic disputation.**

## Bottom banner

Use a strong concluding statement across the full slide:

> **The battery tells us where the system breaks. The integrated benchmark tells us whether the system works. The generic control tells us how its reasoning compares.**

## Speaker notes

The evaluation should not collapse every capability into a single score. A composite battery gives us diagnostic resolution: if the final disputation is weak, we can determine whether the cause was attribution, premise selection, compression, provenance loss, or response generation. The integrated benchmark then tests the actual research claim: that structured, source-grounded intermediate representations improve reasoning over authentic scholarly material. A generic benchmark such as FOLIO provides an external sanity check and makes the system comparable to general reasoning systems, but it cannot validate the project-specific capabilities by itself.

The integrated benchmark should be project-owned because no verified existing benchmark covers the complete chain from authentic source text through attribution, argument form, provenance, dependency-preserving compression, cross-source synthesis, strength comparison, and full scholastic disputation. Report stage metrics, end-to-end pass criteria, and ablation deltas separately rather than pooling them into one number.

## Design guidance

- Make the middle column approximately **40% of the slide width**.
- Use three distinct colors: diagnostic blue, integrated purple, calibration gray.
- Use arrows only for the integrated pipeline; avoid implying that the external benchmarks form one linear pipeline.
- Place a small warning icon beside the generic-control column: **“Not sufficient alone.”**
- Keep the slide text sparse; the detailed benchmark names belong in speaker notes or a follow-up slide.
- The visual hierarchy should make the project-owned integrated benchmark—not the generic benchmark—the central contribution.
