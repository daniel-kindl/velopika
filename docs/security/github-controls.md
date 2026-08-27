<!-- ste-class: ste-strict -->
# GitHub security controls

The repository must use these GitHub controls before normal development starts:

- Pull-request protection for `main` and `dev`.
- Required status checks.
- Human approval before merge.
- Private vulnerability reporting.
- Dependabot.
- Dependency review.
- CodeQL.
- Secret scanning.
- Signed commits where the repository plan can enforce them.

The repository contains workflow and configuration files for Dependabot, dependency review, and CodeQL.
Some account controls need repository administrator settings and cannot be enabled by source files.

For `main`, prevent direct source changes and require an approved release pull request.
For `dev`, prevent direct source changes and require an approved feature pull request.

Do not enable automatic merge for agent work.
Do not give release signing material to GitHub Actions or agents.
