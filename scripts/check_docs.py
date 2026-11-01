#!/usr/bin/env python3
"""Public-repository checks for the CHASI specification repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SELF = Path(__file__).resolve()
MAX_FILE_BYTES = 1_048_576
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
PRIVATE_KEY_RE = re.compile(
    rb"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"
)
TOKEN_RES = [
    re.compile(rb"gh[pousr]_[A-Za-z0-9]{30,}"),
    re.compile(rb"AKIA[0-9A-Z]{16}"),
    re.compile(rb"Bearer\s+[A-Za-z0-9._-]{32,}"),
]
LOCAL_PATH_RE = re.compile(rb"/Users/|/private/tmp/")
REQUIRED = [
    "LICENSE",
    "MAINTAINERS.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CODE_OF_CONDUCT.md",
    "README.md",
    "README-zh.md",
]


def files():
    return [
        path
        for path in ROOT.rglob("*")
        if path.is_file() and ".git" not in path.parts
    ]


def main() -> int:
    failures = []
    for name in REQUIRED:
        if not (ROOT / name).is_file():
            failures.append("missing required file: " + name)

    for path in files():
        relative = path.relative_to(ROOT)
        if path.stat().st_size > MAX_FILE_BYTES:
            failures.append("file exceeds 1 MiB: " + str(relative))
        content = path.read_bytes()
        if PRIVATE_KEY_RE.search(content):
            failures.append("private key marker: " + str(relative))
        for pattern in TOKEN_RES:
            if pattern.search(content):
                failures.append("possible credential: " + str(relative))
        if path.resolve() != SELF and path.suffix in {".md", ".json", ".yml", ".yaml", ".py"}:
            if LOCAL_PATH_RE.search(content):
                failures.append("local absolute path: " + str(relative))

    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        for target in LINK_RE.findall(path.read_text(encoding="utf-8")):
            target = target.strip().split("#", 1)[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            if not (path.parent / target).resolve().exists():
                failures.append(
                    "broken relative link: "
                    + str(path.relative_to(ROOT))
                    + " -> "
                    + target
                )

    for directory in ("architecture", "specs", "profiles", "method"):
        for path in sorted((ROOT / directory).glob("*.md")):
            if path.name.endswith("-zh.md"):
                pair = path.with_name(path.name[:-6] + ".md")
            else:
                pair = path.with_name(path.stem + "-zh.md")
            if not pair.exists():
                failures.append("missing language pair: " + str(path.relative_to(ROOT)))

    readmes = [
        (ROOT / "README.md").read_text(encoding="utf-8"),
        (ROOT / "README-zh.md").read_text(encoding="utf-8"),
    ]
    for path in sorted((ROOT / "profiles").glob("*.md")):
        for index, text in enumerate(readmes):
            if path.name not in text:
                failures.append(
                    "profile missing from "
                    + ("README.md" if index == 0 else "README-zh.md")
                    + ": "
                    + path.name
                )

    if failures:
        for failure in failures:
            print("FAIL", failure)
        return 1
    print("PASS docs checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
