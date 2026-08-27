<!-- ste-class: ste-strict -->
# ADR-001: Platform and upstream channel

## Status

Accepted.

## Context

Velopika needs one primary platform and one supported Chromium baseline before the first build.
A solo project must keep the initial test matrix small.

## Decision

Use Windows 10 and Windows 11 on x64 Intel or AMD PCs as the first platform.
Use a Windows 10 virtual machine as an additional validation host.
Use a pinned supported stable Chromium branch for dogfood and stable development.

The initial source pin is Chromium 152.0.7977.55 at revision `5659715958734a5ca90fda5d3c5249daf2b28c3d`.

## Consequences

The first build, packaging, and test procedures target Windows x64.
A subsequent Chromium update needs an explicit revision change and validation result.

## Related requirements

See `docs/PROJECT.md` and `chromium.version`.
