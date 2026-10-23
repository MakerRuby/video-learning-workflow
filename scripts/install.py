#!/usr/bin/env python3
"""Install the video-learning-workflow skill into one or more AI client locations.

The skill folder is the canonical source. This script copies it; it never edits
or deletes the source folder and never removes an unrelated skill.

Examples:
    python scripts/install.py --scope user --targets codex,claude,workbuddy
    python scripts/install.py --scope project --project . --targets codex,claude
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

SKILL_NAME = "video-learning-workflow"

# Host -> (user-relative skills dir, project-relative skills dir)
TARGETS = {
    "codex": (Path(".agents") / "skills", Path(".agents") / "skills"),
    "claude": (Path(".claude") / "skills", Path(".claude") / "skills"),
    "workbuddy": (Path(".codebuddy") / "skills", Path(".codebuddy") / "skills"),
    "generic": (Path(".agents") / "skills", Path(".agents") / "skills"),
}


def skill_root() -> Path:
    return Path(__file__).resolve().parent.parent


def is_this_skill(folder: Path) -> bool:
    """Return True only when folder is an existing copy of this skill."""
    skill_md = folder / "SKILL.md"
    if not skill_md.is_file():
        return False
    try:
        text = skill_md.read_text(encoding="utf-8")
    except OSError:
        return False
    match = re.search(r"(?m)^name:\s*([^\s#]+)\s*$", text)
    return bool(match and match.group(1).strip().strip("'\"") == SKILL_NAME)


def copytree(source: Path, destination: Path, force: bool) -> str:
    if destination.exists():
        if not force:
            return f"skipped (exists): {destination}"
        if not is_this_skill(destination):
            raise FileExistsError(
                f"refusing to replace {destination}: it is not an existing "
                f"{SKILL_NAME} install (no matching SKILL.md name)"
            )
        shutil.rmtree(destination)
    shutil.copytree(
        source,
        destination,
        ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"),
    )
    return f"installed: {destination}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scope", choices=("user", "project"), default="user")
    parser.add_argument("--project", type=Path, default=Path.cwd())
    parser.add_argument("--targets", default="codex,claude,workbuddy")
    parser.add_argument("--force", action="store_true", help="replace an existing copy")
    args = parser.parse_args()

    targets = [t.strip().lower() for t in args.targets.split(",") if t.strip()]
    unknown = [t for t in targets if t not in TARGETS]
    if unknown:
        parser.error(f"unknown target(s): {', '.join(unknown)}")

    source = skill_root()
    if not (source / "SKILL.md").is_file():
        print(f"error: SKILL.md not found under {source}", file=sys.stderr)
        return 1

    base = Path.home() if args.scope == "user" else Path(args.project).resolve()
    failures = 0
    for target in targets:
        relative = TARGETS[target][0 if args.scope == "user" else 1]
        destination = base / relative / SKILL_NAME
        try:
            print(f"[{target}] {copytree(source, destination, args.force)}")
        except OSError as exc:
            failures += 1
            print(f"[{target}] error: {exc}", file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())

