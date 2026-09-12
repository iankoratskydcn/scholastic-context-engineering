"""Deterministic, solver-free validation of modus ponens and modus tollens."""
from __future__ import annotations

from dataclasses import dataclass
import re

from scholastic_pipeline.schema import ArgumentUnit, EvidenceSpan, ValidationResult, ValidationStatus


@dataclass(frozen=True)
class Formalization:
    """A proposed formal sketch; its provenance must come from source evidence."""
    expression: str
    provenance: tuple[EvidenceSpan, ...] = ()


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


def validate(argument: ArgumentUnit, formalization: Formalization | str, taxonomy_match: object | None = None) -> ValidationResult:
    """Validate exactly MP or MT; enrichment is deliberately ignored."""
    form = Formalization(formalization) if isinstance(formalization, str) else formalization
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
