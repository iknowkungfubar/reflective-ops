#!/usr/bin/env python3
"""Scan public repository text files for common secrets and personal-data patterns."""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TEXT_SUFFIXES = {
    ".md", ".txt", ".py", ".json", ".yml", ".yaml", ".toml", ".cff", ".gitignore",
    ".gitattributes", ".editorconfig"
}
TEXT_NAMES = {"LICENSE", "VERSION", "Makefile"}

SKIP_RELATIVE = {
    Path("scripts/public_release_scan.py"),
    Path("tests/test_public_release_scan.py"),
}

PATTERNS = {
    "email address": re.compile(r"(?<![\w.+-])[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}(?![\w.-])"),
    "Unix user home path": re.compile(r"(?<![A-Za-z0-9_])/(?:home|Users)/[A-Za-z0-9._-]+(?:/|$)"),
    "Windows user home path": re.compile(r"(?i)\b[A-Z]:\\Users\\[A-Za-z0-9._ -]+\\"),
    "private key header": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{20,}\b|\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "Slack token": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b"),
    "JWT-like token": re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b"),
    "generic embedded credential": re.compile(
        r"""(?ix)
        \b(?:api[_-]?key|access[_-]?token|auth[_-]?token|secret|password)
        \s*[:=]\s*
        ["'][^"'\\\n]{8,}["']
        """
    ),
}

def is_text_candidate(path: Path) -> bool:
    return path.name in TEXT_NAMES or path.suffix.lower() in TEXT_SUFFIXES

def load_private_denylist() -> list[str]:
    configured = os.environ.get("REFLECTIVEOPS_PRIVATE_DENYLIST")
    if not configured:
        return []
    path = Path(configured).expanduser()
    if not path.is_file():
        raise FileNotFoundError("configured private denylist file does not exist")
    terms = []
    for line in path.read_text(encoding="utf-8").splitlines():
        term = line.strip()
        if term and not term.startswith("#"):
            terms.append(term)
    return terms

def scan_file(path: Path, denylist: list[str]) -> list[str]:
    rel = path.relative_to(ROOT)
    if rel in SKIP_RELATIVE:
        return []
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return []

    findings: list[str] = []
    for label, pattern in PATTERNS.items():
        for match in pattern.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            findings.append(f"{rel}:{line}: possible {label}")

    lower = text.casefold()
    for term in denylist:
        if term.casefold() in lower:
            findings.append(f"{rel}: contains a term from the private local denylist")

    return findings

def run_scan(root: Path = ROOT) -> list[str]:
    denylist = load_private_denylist()
    findings: list[str] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or ".git" in path.parts:
            continue
        if is_text_candidate(path):
            findings.extend(scan_file(path, denylist))
    return findings

def main() -> int:
    try:
        findings = run_scan()
    except FileNotFoundError as exc:
        print(f"Public release scan configuration error: {exc}")
        return 2

    if findings:
        print("Public release scan FAILED")
        for finding in findings:
            print(f"- {finding}")
        return 1

    print("Public release scan passed: no configured secret/PII patterns detected")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
