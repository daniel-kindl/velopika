from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REQUIRED = [
    ".github/CODEOWNERS",
    ".github/dependabot.yml",
    ".github/pull_request_template.md",
    ".github/workflows/bootstrap.yml",
    ".github/workflows/codeql.yml",
    ".github/workflows/dependency-review.yml",
    "AGENTS.md",
    "CLAUDE.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "README.md",
    "SECURITY.md",
    "chromium.version",
    "docs/PROJECT.md",
    "docs/build/windows.md",
    "docs/language/STE.md",
    "docs/language/terminology.yaml",
    "docs/language/exceptions.yaml",
    "patches/ledger/TEMPLATE.yaml",
    "tools/bootstrap/check-windows.ps1",
    "tools/ste/lint.py",
]

SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{30,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
]

TEXT_SUFFIXES = {".md", ".py", ".ps1", ".yml", ".yaml", ".json", ".txt", ".version", ""}


def main() -> int:
    errors: list[str] = []
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    pin_path = ROOT / "chromium.version"
    try:
        pin = json.loads(pin_path.read_text(encoding="utf-8"))
        revision = pin.get("revision", "")
        if not re.fullmatch(r"[0-9a-f]{40}", revision):
            errors.append("chromium.version has an invalid revision")
        if pin.get("platform") != "Windows" or pin.get("architecture") != "x64":
            errors.append("chromium.version has an unexpected platform or architecture")
    except Exception as exc:
        errors.append(f"chromium.version does not parse: {exc}")

    prohibited_names = {"ASD-STE100_ISSUE9.pdf", "ASD-STE100.pdf"}
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        if path.name in prohibited_names:
            errors.append(f"prohibited standard file: {rel}")
        if rel.startswith("src/") or rel.startswith("chromium/src/"):
            errors.append(f"Chromium source is vendored: {rel}")
        if path.stat().st_size > 2_000_000:
            errors.append(f"unexpected large bootstrap file: {rel}")
        if path.suffix.lower() in TEXT_SUFFIXES:
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            for pattern in SECRET_PATTERNS:
                if pattern.search(text):
                    errors.append(f"possible secret in {rel}")

    if errors:
        for error in errors:
            print(f"QUALITY: {error}")
        print(f"QUALITY: FAIL ({len(errors)} findings)")
        return 1
    print("QUALITY: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
