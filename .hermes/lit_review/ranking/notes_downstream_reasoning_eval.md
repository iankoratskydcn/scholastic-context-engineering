# Downstream inspectable reasoning evaluation

Perspective: rank benchmark task designs for comparing generated outputs on validity, faithfulness, groundedness, explanation fidelity, proof correctness, and inspectability. Model architecture not scored.

Method: combine existing task-design reviews with weights: formal/checker-backed validity 24%, grounding/provenance 22%, argument-form diagnosticity 19%, dialectical structure 15%, evaluation rigor 14%, context stress 6%. Small task-design adjustments reward explicit proof/citation controls and penalize resources focused on cultural knowledge or linguistic preprocessing without reasoning traces.

Interpretation: high rank means evaluator can inspect why an output passes/fails, not merely score answer accuracy. Synthetic formal suites score high for proof correctness and controlled diagnosis; authentic argument/RAG resources score high for explanation and evidence fidelity; long-context suites are complementary stress tests.

Scope: all 80 rows from `benchmark_studies.csv`; literal identity fields preserved.
