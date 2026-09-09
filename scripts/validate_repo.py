#!/usr/bin/env python3
"""Validate public ReflectiveOps repository structure using only the standard library."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

REQUIRED_ROOT = {
    "README.md",
    "LICENSE",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "DISCLAIMER.md",
    "AGENTS.md",
    "VERSION",
}

ALLOWED_FRONTMATTER_TOP_LEVEL = {
    "name",
    "description",
    "license",
    "compatibility",
    "metadata",
}

def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing opening YAML frontmatter delimiter")
    try:
        end = lines[1:].index("---") + 1
    except ValueError as exc:
        raise ValueError("missing closing YAML frontmatter delimiter") from exc

    result: dict[str, object] = {}
    metadata: dict[str, str] = {}
    in_metadata = False

    for raw in lines[1:end]:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw.startswith("metadata:"):
            in_metadata = True
            result["metadata"] = metadata
            continue
        if in_metadata and raw.startswith("  "):
            key, sep, value = raw.strip().partition(":")
            if not sep:
                raise ValueError(f"invalid metadata line: {raw}")
            metadata[key.strip()] = value.strip().strip('"').strip("'")
            continue
        in_metadata = False
        key, sep, value = raw.partition(":")
        if not sep:
            raise ValueError(f"unsupported frontmatter line: {raw}")
        result[key.strip()] = value.strip().strip('"').strip("'")

    return result

def main() -> int:
    errors: list[str] = []

    for rel in sorted(REQUIRED_ROOT):
        if not (ROOT / rel).exists():
            errors.append(f"missing required root file: {rel}")

    symlinks = [p.relative_to(ROOT) for p in ROOT.rglob("*") if p.is_symlink()]
    if symlinks:
        errors.append("symlinks are not permitted: " + ", ".join(map(str, symlinks)))

    skills_dir = ROOT / "skills"
    skill_dirs = sorted(p for p in skills_dir.iterdir() if p.is_dir()) if skills_dir.exists() else []
    if not skill_dirs:
        errors.append("no skills found")

    skill_names = set()
    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            errors.append(f"{skill_dir.name}: missing SKILL.md")
            continue
        try:
            fm = parse_frontmatter(skill_file)
        except ValueError as exc:
            errors.append(f"{skill_dir.name}: {exc}")
            continue

        unknown = set(fm) - ALLOWED_FRONTMATTER_TOP_LEVEL
        if unknown:
            errors.append(f"{skill_dir.name}: unsupported top-level frontmatter keys: {sorted(unknown)}")

        name = str(fm.get("name", ""))
        description = str(fm.get("description", ""))
        license_name = str(fm.get("license", ""))
        compatibility = str(fm.get("compatibility", ""))
        metadata = fm.get("metadata", {})

        if name != skill_dir.name:
            errors.append(f"{skill_dir.name}: frontmatter name must exactly match directory name")
        if not NAME_RE.fullmatch(name):
            errors.append(f"{skill_dir.name}: invalid skill name")
        if not 1 <= len(name) <= 64:
            errors.append(f"{skill_dir.name}: name must be 1-64 characters")
        if not 1 <= len(description) <= 1024:
            errors.append(f"{skill_dir.name}: description must be 1-1024 characters")
        if license_name != "Apache-2.0":
            errors.append(f"{skill_dir.name}: license must be Apache-2.0")
        if len(compatibility) > 500:
            errors.append(f"{skill_dir.name}: compatibility exceeds 500 characters")
        if not isinstance(metadata, dict) or metadata.get("project") != "reflectiveops":
            errors.append(f"{skill_dir.name}: metadata.project must be reflectiveops")
        if not isinstance(metadata, dict) or not metadata.get("version"):
            errors.append(f"{skill_dir.name}: metadata.version is required")

        body = skill_file.read_text(encoding="utf-8")
        mandatory_phrases = [
            "Do not diagnose",
            "competing",
            "personal information",
            "user's decision authority",
        ]
        for phrase in mandatory_phrases:
            if phrase.lower() not in body.lower():
                errors.append(f"{skill_dir.name}: missing mandatory safety concept: {phrase}")

        skill_names.add(name)

    eval_file = ROOT / "evals" / "cases.json"
    if not eval_file.exists():
        errors.append("missing evals/cases.json")
    else:
        try:
            data = json.loads(eval_file.read_text(encoding="utf-8"))
            cases = data.get("cases", [])
            ids = set()
            for case in cases:
                cid = case.get("id")
                if not cid:
                    errors.append("eval case missing id")
                elif cid in ids:
                    errors.append(f"duplicate eval id: {cid}")
                ids.add(cid)
                if case.get("skill") not in skill_names:
                    errors.append(f"{cid}: unknown skill {case.get('skill')}")
                if case.get("synthetic") is not True:
                    errors.append(f"{cid}: eval must be explicitly synthetic")
                if len(case.get("assertions", [])) < 2:
                    errors.append(f"{cid}: needs at least two behavioral assertions")
        except (json.JSONDecodeError, AttributeError) as exc:
            errors.append(f"invalid evals/cases.json: {exc}")

    if errors:
        print("Repository validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Repository validation passed: {len(skill_names)} skills")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
