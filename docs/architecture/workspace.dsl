workspace "Scholastic Context Engineering" "Current repository architecture — observed from src/, tests/, schemas/, fixtures/, and docs/evidence/." {
    !identifiers hierarchical

    model {
        researcher = person "Researcher / Developer" "Runs the local evidence-first pipeline and inspects provenance-bearing results."

        pipeline = softwareSystem "Scholastic Context Engineering" "Standalone, dependency-free Python pipeline for provenance-bearing argument extraction, validation, graph assembly, deterministic retrieval, and evidence-bound generation." {
            ingestion = container "Ingestion & Structuring" "Strict UTF-8 ingestion, exact source spans, paragraph structure, quarantine handling." "Python / scholastic_pipeline.ingestion" {
                ingest = component "Text Ingestion" "ingest_text() validates bytes, identity, revisions, and emits exact spans." "Python"
                structure = component "Document Structuring" "structure_document() splits accepted text while preserving offsets." "Python"
            }
            schema = container "Canonical Schema" "Frozen immutable envelopes shared by all stages." "Python / scholastic_pipeline.schema" {
                envelopes = component "Typed Envelopes" "EvidenceSpan, documents, propositions, arguments, validation, graph, retrieval records." "Python dataclasses"
                identity = component "Stable Identity & Bounds" "Deterministic IDs, provenance requirements, schema version, resource ceilings." "Python"
            }
            extraction = container "Argument Extraction" "Canary and production extraction of typed premise/conclusion arguments plus taxonomy matches." "Python / scholastic_pipeline.extraction" {
                extractor = component "Canary / Structured Extractor" "extract_argument() and extract_structured_document() abstain fail-closed." "Python"
                taxonomy = component "Taxonomy Boundary" "Consumes an explicit TaxonomySnapshot and preserves provenance scope." "Python"
            }
            formal = container "Formal Validation" "Deterministic, solver-free validation of modus ponens and modus tollens." "Python / scholastic_pipeline.formal" {
                formalization = component "Formalization" "Normalizes a strict implication and keeps execution/source provenance." "Python"
                validator = component "Structural Validator" "validate() returns VALID, INVALID, UNKNOWN, UNSUPPORTED, or ILL_POSED." "Python"
            }
            assembly = container "Graph Assembly" "Converts validated arguments into provenance-bearing edge occurrences." "Python / scholastic_pipeline.assembly" {
                events = component "Edge Event Assembly" "assemble_edge_events() emits one occurrence per premise without upgrading status." "Python"
            }
            backend = container "Reference SQLite Backend" "Transactional occurrence-preserving store for graph generations." "Python / scholastic_pipeline.backends.reference" {
                store = component "Generation Store" "SQLite generations and occurrences tables with completion and provenance gates." "Python / SQLite"
            }
            retrieval = container "Deterministic Retrieval" "Bounded token-overlap retrieval over admissible graph edge occurrences." "Python / scholastic_pipeline.retrieval" {
                retrieve = component "Retriever" "retrieve() validates scope, revisions, budgets, statuses, and stable ordering." "Python"
            }
            generation = container "Evidence-Bound Generation" "Produces supported or explicitly unverified claims; refuses unsupported or unsafe contexts." "Python / scholastic_pipeline.generation" {
                claims = component "Claim Boundary" "Claims require exact citations when supported; refusals cannot contain claims." "Python"
                safety = component "Generation Safety" "Rejects stale, forged, out-of-scope, over-budget, or instruction-injected evidence." "Python"
            }
        }

        evidence = softwareSystem "Versioned Evidence & Fixtures" "Repository-local raw evidence, schemas, fixtures, and verification artifacts." "External"
        testSuite = softwareSystem "Contract & Adversarial Tests" "Pytest contracts, integration canaries, boundary tests, and security tests." "External"

        researcher -> pipeline "Runs and inspects" "uv run pytest / Python API"
        evidence -> pipeline "Supplies frozen source text, schemas, and fixtures" "Local files"
        pipeline -> evidence "Emits provenance references and verification artifacts" "JSON / Markdown"
        testSuite -> pipeline "Exercises contracts and hostile boundaries" "pytest"

        pipeline.ingestion -> pipeline.schema "Creates typed document envelopes"
        pipeline.schema -> pipeline.extraction "Provides immutable input records"
        pipeline.extraction -> pipeline.formal "Passes ArgumentUnit, taxonomy, and Formalization"
        pipeline.schema -> pipeline.formal "Provides canonical records and provenance"
        pipeline.formal -> pipeline.assembly "Provides ValidationResult"
        pipeline.extraction -> pipeline.assembly "Provides accepted ArgumentUnit"
        pipeline.assembly -> pipeline.backend "Appends GraphEdgeEvent occurrences"
        pipeline.backend -> pipeline.retrieval "Provides GraphSnapshot occurrences"
        pipeline.schema -> pipeline.retrieval "Provides RetrievalRequest and provenance records"
        pipeline.retrieval -> pipeline.generation "Provides RetrievalContext with exact citations"
        pipeline.schema -> pipeline.generation "Provides EvidenceSpan and immutable boundaries"
    }

    views {
        systemContext pipeline "systemContext" {
            include researcher
            include pipeline
            include evidence
            include testSuite
            autoLayout lr
            description "Current repository boundary and its local evidence/test collaborators."
        }

        container pipeline "containerView" {
            include researcher
            include *
            include evidence
            include testSuite
            autoLayout lr
            description "Observed logical pipeline stages implemented under src/scholastic_pipeline."
        }

        component pipeline.extraction "extractionComponents" {
            include researcher
            include *
            autoLayout lr
            description "Evidence-bound extraction seam and its immediate typed/formal collaborators."
        }

        styles {
            element "Person" {
                shape person
                background #2563eb
                color #ffffff
            }
            element "Software System" {
                background #0f172a
                color #ffffff
            }
            element "Container" {
                background #0f766e
                color #ffffff
            }
            element "Component" {
                background #0e7490
                color #ffffff
            }
            element "External" {
                background #64748b
                color #ffffff
            }
        }
    }
}
