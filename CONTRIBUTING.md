<!-- ste-class: ste-strict -->
# Contributing to Velopika

Use one branch for one related change.
Start a feature branch from `dev`.
Use the form `feature/<issue>-<slug>` when an issue number exists.

Use Conventional Commits for commit and pull-request titles.
Use the form `type(scope): imperative summary`.

Before you request review:

1. Run the applicable repository checks.
2. Run the applicable tests.
3. Update the patch ledger when the change touches Chromium integration points.
4. Classify changed English text with the Velopika language policy.
5. Run the required STE checks.
6. Record security effects when a trust boundary changes.
7. Add rollback information when the change can affect persisted state or release behavior.

A human must review each merge.
Agents must not merge changes without human approval.
Do not put signing keys, production secrets, or private credentials in repository or agent context.

Read [the branch model](docs/release/branch-model.md) for release rules.
Read [the language policy](docs/language/STE.md) before you change project-owned English text.
