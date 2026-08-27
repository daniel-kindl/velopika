from __future__ import annotations

import os
import re
import sys

PATTERN = re.compile(r"^(feat|fix|docs|build|ci|test|refactor|perf|security|chore)(\([a-z0-9._/-]+\))?!?: [a-z0-9].+")


def main() -> int:
    title = os.environ.get("PR_TITLE", "").strip()
    if not title:
        print("PR-TITLE: no pull-request title was supplied")
        return 1
    if not PATTERN.fullmatch(title):
        print("PR-TITLE: use type(scope): imperative summary")
        return 1
    print("PR-TITLE: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
