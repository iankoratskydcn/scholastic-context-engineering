# HR / Student-Hiring Pipeline Evidence Pack

## Authoritative interview sources

- `/Users/iankoratsky/.hermes/attachments/HR App (1).docx` — Laura Hemphill interview, August 11, 2026
- `/Users/iankoratsky/.hermes/attachments/Call with Mayra Morfin (1).docx` — Mayra Morfin interview, August 13, 2026
- `/Users/iankoratsky/.hermes/attachments/Call with Daisy Matos.docx` — Daisy Matos interview, August 20, 2026

## Existing derived artifacts

- `/Users/iankoratsky/.hermes/attachments/student_hiring_pipeline.md`
- `/Users/iankoratsky/.hermes/attachments/mayra_student_hiring_flow.md`
- `/Users/iankoratsky/.hermes/attachments/daisy_finance_stage.md`

## Verification rule

Treat interview transcripts as primary evidence. Treat derived Markdown as provisional summaries. Every finding must cite exact transcript line ranges or exact derived-artifact sections. Preserve uncertainty and contradictions. Do not invent policy, approvals, system integrations, statuses, or ownership. Read-only: no production edits, no commits, no external mutations.

## Three pipeline segments

1. Mayra: faculty intake, renewal/new appointment branching, response chasing, identity/detail resolution, HR worksheet entry, change requests.
2. Laura/HR: screening, offer-letter preparation and signatures, student signing, Oracle entry, approval queue, new-hire preboarding, verification, changes/reappointments.
3. Daisy/Finance: chartfield/account verification, funding remediation, distributions, fringe/FTE/pay-period calculations, Oracle costing, status marking, active-appointment monitoring and termination.

## Required distinction

Separate:

- directly confirmed interview evidence;
- corroborated cross-interview behavior;
- second-hand descriptions;
- design proposals from Ian;
- unresolved questions.

## Output contract

Each verifier must return one JSON object with:

- `perspective`
- `verdict` (`pass`, `pass_with_caveats`, `blocked`, or `contradiction_found`)
- `findings` (array with `id`, `claim`, `status`, `evidence`, `risk`, `recommendation`)
- `missing_or_ambiguous`
- `source_coverage`
- `output_path`

Write the complete JSON to the assigned output path and reload it before reporting completion.
