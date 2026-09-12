"""Deterministic, solver-free validation of modus ponens and modus tollens."""
from __future__ import annotations

from dataclasses import dataclass, field
import hashlib
import re

from scholastic_pipeline.schema import ArgumentUnit, EvidenceSpan, TaxonomyMatch, ValidationResult, ValidationStatus


@dataclass(frozen=True)
class Formalization:
    """Canonical formal sketch tied to one execution and source revision."""
    expression: str
    provenance: tuple[EvidenceSpan, ...] = ()
    run_id: str = ""
    confidence: float = 1.0
    uncertainty: tuple[str, ...] = ()
    diagnostics: tuple[str, ...] = ()
    status: str = "ACCEPTED"
    schema_version: str = "0.1"
    record_id: str = field(init=False)

    def __post_init__(self) -> None:
        run = self.run_id or ("" if not self.provenance else "unknown")
        object.__setattr__(self, "run_id", run)
        if not isinstance(self.expression, str):
            raise ValueError("formalization expression is required")
        if not self.provenance:
            raise ValueError("formalization requires provenance")
        if not 0 <= self.confidence <= 1 or self.schema_version != "0.1":
            raise ValueError("invalid formalization envelope")
        payload = (self.expression, self.provenance, self.run_id, self.confidence,
                   self.uncertainty, self.diagnostics, self.status, self.schema_version)
        object.__setattr__(self, "record_id", "formalization-" + hashlib.sha256(repr(payload).encode()).hexdigest()[:24])


_ATOM = r"[^&|→¬\-]+"
_IMPLICATION = re.compile(rf"^\s*({_ATOM.strip()})\s*(?:->|→)\s*({_ATOM.strip()})\s*$")


def _clean(value: str) -> str:
    return " ".join(value.strip().split())


def _parse(expression: str) -> tuple[str, str, str] | None:
    match = _IMPLICATION.fullmatch(expression.replace("→", "->"))
    if not match:
        return None
    antecedent, consequent = (_clean(part) for part in match.groups())
    if not antecedent or not consequent or "&" in antecedent or "|" in antecedent:
        return None
    return antecedent, consequent, f"{antecedent} -> {consequent}"


def _text(value: object) -> str:
    return _clean(value.text) if hasattr(value, "text") else _clean(str(value))


def _negated(atom: str) -> str:
    return f"¬{atom}"


def validate(argument: object, formalization: Formalization | str, taxonomy_match: object | None = None) -> ValidationResult:
    """Validate a canonical extraction bundle without reconstructing its premises."""
    from scholastic_pipeline.extraction import ExtractionBundle
    bundle = argument if isinstance(argument, ExtractionBundle) else None
    if isinstance(argument, ExtractionBundle):
        if argument.argument is None or argument.taxonomy is None:
            raise ValueError("formal validation requires an accepted extraction with taxonomy match")
        if taxonomy_match is not None and taxonomy_match != argument.taxonomy:
            raise ValueError("taxonomy match does not match extraction")
        if argument.taxonomy.run_id != argument.run_id or argument.taxonomy.run_id != argument.argument.run_id:
            raise ValueError("taxonomy and extraction run IDs must match")
        argument = argument.argument
    elif not isinstance(argument, ArgumentUnit):
        raise TypeError("formal validation requires ExtractionBundle")
    if not isinstance(formalization, (Formalization, str)):
        raise TypeError("formalization must be Formalization or str")
    form = Formalization(formalization) if isinstance(formalization, str) else formalization
    if bundle is not None:
        if form.run_id != bundle.run_id:
            raise ValueError("formalization and extraction run IDs must match")
        expected = {(s.source_id, s.revision) for s in bundle.argument.provenance}
        actual = {(s.source_id, s.revision) for s in form.provenance}
        taxonomy_sources = {(s.source_id, s.revision) for s in bundle.taxonomy.provenance}
        if not actual <= expected or taxonomy_sources != expected:
            raise ValueError("formalization, taxonomy, and extraction provenance must match")
    elif taxonomy_match is not None:
        if not isinstance(taxonomy_match, TaxonomyMatch):
            raise TypeError("taxonomy_match must be TaxonomyMatch")
        if taxonomy_match.run_id != argument.run_id or not {(s.source_id, s.revision) for s in taxonomy_match.provenance} <= {(s.source_id, s.revision) for s in argument.provenance}:
            raise ValueError("taxonomy and argument provenance must match")
    if form.run_id not in ("", "unknown") and form.run_id != argument.run_id:
        raise ValueError("formalization and argument run IDs must match")
    if not argument.provenance or not form.provenance:
        raise ValueError("formal validation requires provenance on argument and formalization")
    parsed = _parse(form.expression)
    provenance = tuple(dict.fromkeys(argument.provenance + form.provenance))
    if parsed is None:
        status = ValidationStatus.UNSUPPORTED if not _clean(form.expression) else ValidationStatus.UNKNOWN
        obligations = ("formalization must be a single strict implication",)
    else:
        antecedent, consequent, normalized = parsed
        premises = tuple(_text(p) for p in argument.premises)
        conclusion = _text(argument.conclusion)
        mp = len(premises) == 2 and premises == (normalized, antecedent) and conclusion == consequent
        mt = len(premises) == 2 and premises == (normalized, _negated(consequent)) and conclusion == _negated(antecedent)
        status = ValidationStatus.VALID if mp or mt else ValidationStatus.INVALID
        obligations = ("modus ponens: A -> B and A entail B",
                       "modus tollens: A -> B and ¬B entail ¬A")
    return ValidationResult(
        run_id=argument.run_id, provenance=provenance, validation_status=status,
        normalized_form=normalized if parsed else _clean(form.expression),
        proof_obligations=obligations,
        diagnostics=("deterministic structural check; no solver used",
                     "taxonomy/community/frequency are not proof"),
    )


validate_formalization = validate
__all__ = ["Formalization", "validate", "validate_formalization"]
