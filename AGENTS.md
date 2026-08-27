<!-- ste-class: ste-strict -->
# Agent instructions

Inspect the current implementation before you edit files.
Keep each task limited to one related change.
Prefer product-owned code in `//velopika` when Chromium architecture permits it.
Keep Chromium integration points small and named.
Preserve Chromium sandboxing, site isolation, certificate handling, and update security.
Add tests with implementation work when applicable.
Update the patch ledger for each durable Chromium integration point.
Classify each changed English text before you change it.
Obey `docs/language/STE.md` and `docs/language/terminology.yaml`.
Do not use `/humanizer` for `ste-strict` text.
Do not expose secrets, signing keys, credentials, or personal browsing data.
Do not merge without human approval.

At task completion, report changed files, commands, results, risks, and follow-up work.
