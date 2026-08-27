<!-- ste-class: ste-strict -->
# Project baseline

Velopika is a personal Chromium-based desktop browser.
The owner is the primary user during v0.x development.
Public distribution is not a v0.1 requirement.

## Product direction

Use Chromium as inherited browser infrastructure.
Keep the fork close to upstream.
Put product behavior in a small Velopika layer when Chromium architecture permits it.
Preserve Chromium sandboxing, site isolation, certificate handling, renderer protection, and exploit mitigation.

Use Windows 10 and Windows 11 on x64 Intel or AMD PCs as the first platform.
Use a pinned supported stable Chromium revision for the initial browser baseline.
Keep the Velopika SemVer version independent from the Chromium milestone.

Do not send automatic remote telemetry.
Keep diagnostic and crash data local unless the user starts an export.
Use a local-only user profile in v0.1.
Do not add accounts or cloud sync in v0.1.

Use different user-data directories for dev, dogfood, and stable channels.
Use standard Chromium Incognito in v0.1.
Support usual Chromium extensions and developer-mode sideloading.

## Development direction

Use Conventional Commits and SemVer.
Use `feature/* -> dev -> release/x.y.z -> main` for the normal source flow.
Use `hotfix/x.y.z` from `main` for urgent stable corrections.
A human must review and approve each merge.
Agents must not merge autonomously.

Record each durable Chromium integration point in the patch ledger.
Keep each product change small and reversible.
Use existing Chromium services, preferences, feature flags, Views, WebUI, and test harnesses before parallel infrastructure.

## Language direction

All Velopika-owned technical English uses ASD-STE100 Issue 9 as the mandatory baseline.
Use `ste-strict` for final technical and engineering text.
Use an approved STE baseline before Claude `/humanizer` processes user-facing `ste-humanized` text.
Use `ste-exempt` only for permitted fixed or external text.

## First build gate

The repository is ready for the first browser build when project controls and build instructions are complete.
The next engineering task must fetch the pinned Chromium revision, compile stock Chromium, and launch it with an isolated development profile.
