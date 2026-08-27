from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def main() -> int:
    errors: list[str] = []
    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        for number, line in enumerate(text.splitlines(), 1):
            if line.rstrip() != line:
                errors.append(f"{rel}:{number}: trailing whitespace")
        for target in LINK_RE.findall(text):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target_path = target.split("#", 1)[0]
            if not target_path:
                continue
            resolved = (path.parent / target_path).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                continue
            if not resolved.exists():
                errors.append(f"{rel}: unresolved link {target}")
    if errors:
        for error in errors:
            print(f"MARKDOWN: {error}")
        print(f"MARKDOWN: FAIL ({len(errors)} findings)")
        return 1
    print("MARKDOWN: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
