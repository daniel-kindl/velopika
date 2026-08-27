<!-- ste-class: ste-strict -->
# ADR-003: Upstream and patch policy

## Status

Accepted.

## Context

Chromium changes frequently and includes important security updates.
A large local patch surface can make safe updates too difficult.

## Decision

Prefer product-owned code in `//velopika/` when Chromium architecture permits it.
Use small named Chromium integration points when product-owned code cannot operate alone.
Record each durable Chromium integration point in the patch ledger.
Do not combine product work with unrelated Chromium refactors.
Preserve Chromium security boundaries.

## Consequences

Each deep Chromium change needs a reason, test coverage, security effect, and removal condition.
Chromium update work is a primary maintenance function.

## Related requirements

See `docs/architecture/source-boundary.md` and `patches/ledger/README.md`.
