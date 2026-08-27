<!-- ste-class: ste-strict -->
# Bootstrap quality gates

The bootstrap stage uses four required gate groups.

## Repository checks

- Required project files exist.
- Tracked files do not contain a Chromium source checkout.
- Tracked files do not contain the ASD-STE100 PDF or controlled dictionary.
- Machine-readable project data parses correctly.
- Python bootstrap tools compile.
- PowerShell bootstrap tools parse on Windows CI.

## Language checks

- Changed technical Markdown uses `ste-strict` classification.
- Procedure sentences have 20 words or less where the linter can identify them.
- Descriptive sentences have 25 words or less where the linter can identify them.
- Project-owned technical text does not use contractions.
- Terminology data contains the required fields.
- A semantic STE review is still necessary when context controls correctness.

The deterministic linter does not prove complete ASD-STE100 compliance.

## Security checks

- Repository checks search for common secret patterns.
- CodeQL checks supported source code.
- Dependency review checks pull-request dependency changes.
- GitHub secret scanning must be enabled in repository settings.

## Documentation checks

- Markdown files have no trailing whitespace.
- Relative Markdown links resolve when the target is in this repository.
- The Windows build procedure points to the pinned Chromium revision.

Future Chromium changes add compile, browser, WebUI, performance, and compatibility gates.
