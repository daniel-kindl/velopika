<!-- ste-class: ste-strict -->
# ADR-004: Version and branch policy

## Status

Accepted.

## Context

Velopika needs product versions that do not depend on Chromium milestone numbers.
The source flow must keep development, release stabilization, and stable source separate.

## Decision

Use SemVer for Velopika product versions.
Use Conventional Commits for commits and pull-request titles.
Use `feature/* -> dev -> release/x.y.z -> main` as the normal source flow.
Use `hotfix/x.y.z` from `main` for urgent stable corrections.
Require human approval before each merge.

## Consequences

Release records contain both the Velopika version and Chromium revision.
Direct product development on `main` or a release branch is not permitted.

## Related requirements

See `docs/release/branch-model.md`.
