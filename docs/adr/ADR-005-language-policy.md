<!-- ste-class: ste-strict -->
# ADR-005: Language policy

## Status

Accepted.

## Context

Velopika requires controlled technical English for durable engineering information.
User-facing text also needs natural wording after the technical meaning is stable.

## Decision

Use ASD-STE100 Issue 9 as the mandatory baseline for Velopika-owned technical English.
Use `ste-strict` for final technical and engineering text.
Use an approved STE baseline before `/humanizer` processes `ste-humanized` user-facing text.
Use `ste-exempt` only for permitted external or fixed text.
Treat an unresolved STE violation as a blocking defect.

## Consequences

Repository checks include deterministic STE checks and terminology validation.
Semantic review remains necessary when meaning or context controls STE correctness.

## Related requirements

See `docs/language/STE.md` and `docs/language/terminology.yaml`.
