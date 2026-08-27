<!-- ste-class: ste-strict -->
# ADR-002: Profile and state boundary

## Status

Accepted.

## Context

The first browser build must not damage an existing Chrome or Chromium profile.
Velopika v0.1 does not need accounts or cloud sync.

## Decision

Use a different user-data directory for each Velopika build channel.
Keep dev, dogfood, and stable profile data separate.
Use a local-only profile in v0.1.
Keep Chromium and Windows encryption mechanisms.
Do not add a custom master password in v0.1.

## Consequences

Build and run procedures must always identify the profile path.
Profile backup and restore become required before daily-default status.

## Related requirements

See `docs/PROJECT.md`.
