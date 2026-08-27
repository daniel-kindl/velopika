from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STRICT_MARKER = "<!-- ste-class: ste-strict -->"
EXEMPT_MARKER = "<!-- ste-class: ste-exempt -->"
WORD_RE = re.compile(r"[A-Za-z0-9]+(?:[-/][A-Za-z0-9]+)*")
SENTENCE_RE = re.compile(r"(?<=[.!?])\s+")
CONTRACTION_RE = re.compile(
    r"\b(?:can't|couldn't|didn't|doesn't|don't|hadn't|hasn't|haven't|"
    r"isn't|mustn't|shouldn't|wasn't|weren't|won't|wouldn't|you'll|you're|you've|"
    r"we'll|we're|we've|they'll|they're|they've|it's|that's|there's)\b",
    re.IGNORECASE,
)

PROCEDURE_PATHS = {
    Path("docs/build/windows.md"),
    Path("CONTRIBUTING.md"),
}

SCAN_PATHS = [
    Path("README.md"),
    Path("CONTRIBUTING.md"),
    Path("AGENTS.md"),
    Path("CLAUDE.md"),
    Path("SECURITY.md"),
]

for base in (Path("docs"), Path("patches"), Path("tools/ste")):
    SCAN_PATHS.extend(path.relative_to(ROOT) for path in (ROOT / base).rglob("*.md"))


def load_json_yaml(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def strip_markdown(text: str) -> list[str]:
    blocks: list[str] = []
    current: list[str] = []
    in_code = False

    def flush() -> None:
        if current:
            blocks.append(" ".join(current).strip())
            current.clear()

    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("```"):
            flush()
            in_code = not in_code
            continue
        if in_code or not line:
            flush()
            continue
        if line.startswith("<!--") or line.startswith("#"):
            flush()
            continue
        if line.startswith("|") or re.match(r"^[-:| ]+$", line):
            flush()
            continue
        if re.match(r"^[-*+]\s+", line) or re.match(r"^\d+[.)]\\?\s+", line):
            flush()
            cleaned = re.sub(r"^[-*+]\s+", "", line)
            cleaned = re.sub(r"^\d+[.)]\\?\s+", "", cleaned)
            blocks.append(cleaned)
            continue
        current.append(line)
    flush()
    return blocks


def sentence_word_count(sentence: str) -> int:
    sentence = re.sub(r"https?://\S+", "URL", sentence)
    sentence = re.sub(r"`[^`]+`", "TERM", sentence)
    return len(WORD_RE.findall(sentence))


def check_text(path: Path, errors: list[str]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    first = "\n".join(text.splitlines()[:5])
    if STRICT_MARKER not in first and EXEMPT_MARKER not in first:
        errors.append(f"{path}: missing STE class marker")
        return
    if EXEMPT_MARKER in first:
        return

    for match in CONTRACTION_RE.finditer(text):
        errors.append(f"{path}: contraction is not permitted: {match.group(0)}")

    limit = 20 if path in PROCEDURE_PATHS else 25
    for block in strip_markdown(text):
        if block.startswith("<http") or block.startswith("Reference:"):
            continue
        for sentence in SENTENCE_RE.split(block):
            count = sentence_word_count(sentence)
            if count > limit:
                sample = sentence.replace("\n", " ")[:120]
                errors.append(f"{path}: {count} words exceed {limit}: {sample}")


def check_terminology(errors: list[str]) -> None:
    path = ROOT / "docs/language/terminology.yaml"
    data = load_json_yaml(path)
    seen: set[str] = set()
    for entry in data.get("terms", []):
        for field in ("term", "type", "approved_meaning", "subject_field"):
            if not entry.get(field):
                errors.append(f"{path.relative_to(ROOT)}: missing {field}")
        key = entry.get("term", "").casefold()
        if key in seen:
            errors.append(f"{path.relative_to(ROOT)}: duplicate term {entry.get('term')}")
        seen.add(key)


def check_exceptions(errors: list[str]) -> None:
    path = ROOT / "docs/language/exceptions.yaml"
    data = load_json_yaml(path)
    for entry in data.get("exceptions", []):
        for field in ("path", "class", "reason"):
            if not entry.get(field):
                errors.append(f"{path.relative_to(ROOT)}: missing {field}")
        if entry.get("class") != "ste-exempt":
            errors.append(f"{path.relative_to(ROOT)}: invalid exception class")


def main() -> int:
    errors: list[str] = []
    for path in sorted(set(SCAN_PATHS)):
        if (ROOT / path).is_file():
            check_text(path, errors)
    check_terminology(errors)
    check_exceptions(errors)

    if errors:
        for error in errors:
            print(f"STE-LINT: {error}")
        print(f"STE-LINT: FAIL ({len(errors)} findings)")
        return 1
    print("STE-LINT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
