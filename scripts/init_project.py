#!/usr/bin/env python3
r"""Initialize a project workspace for the video-learning-workflow skill.

Copies the starter documents into the project root and merges a short
project-memory block into AGENTS.md, CLAUDE.md, and CODEBUDDY.md so each
supported client loads the skill in later sessions.

Existing files are left alone unless --force is given. Memory files are merged
in place (the block between the video-learning-workflow markers is replaced);
other existing files are backed up before replacement when --force is used.

Examples:
    python scripts/init_project.py --project E:/myproject/new-course
    python scripts/init_project.py --project . --force
"""

from __future__ import annotations

import argparse
import shutil
from datetime import datetime
from pathlib import Path

MEMORY_FILES = ("AGENTS.md", "CLAUDE.md", "CODEBUDDY.md")
PLACEHOLDER = "__SKILL_ROOT__"
START_MARK = "<!-- video-learning-workflow:start -->"
END_MARK = "<!-- video-learning-workflow:end -->"


def skill_root() -> Path:
    return Path(__file__).resolve().parent.parent


def marker_block(template_text: str) -> str:
    start = template_text.find(START_MARK)
    end = template_text.find(END_MARK)
    if start < 0 or end < 0:
        raise ValueError(f"memory template is missing the workflow markers: {START_MARK!r}")
    return template_text[start : end + len(END_MARK)].strip()


def merge_memory(destination: Path, block: str) -> str:
    """Merge the workflow block into an existing memory file."""
    text = destination.read_text(encoding="utf-8")
    start = text.find(START_MARK)
    end = text.find(END_MARK)
    if start >= 0 and end > start:
        updated = text[:start] + block + text[end + len(END_MARK) :]
        destination.write_text(updated, encoding="utf-8")
        return "updated"
    if text and not text.endswith("\n"):
        text += "\n"
    separator = "\n" if text else ""
    destination.write_text(text + separator + block + "\n", encoding="utf-8")
    return "appended"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, default=Path.cwd())
    parser.add_argument("--force", action="store_true", help="replace existing project documents")
    args = parser.parse_args()

    source = skill_root()
    templates = source / "assets" / "project-starter"
    project = args.project.resolve()
    if not (source / "SKILL.md").is_file():
        parser.error(f"SKILL.md not found under {source}")
    if not templates.is_dir():
        parser.error(f"starter templates not found under {templates}")
    project.mkdir(parents=True, exist_ok=True)

    stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    created: list[str] = []
    merged: list[str] = []
    skipped: list[str] = []
    backed_up: list[str] = []

    for item in sorted(templates.iterdir()):
        if not item.is_file():
            continue
        destination = project / item.name
        template_text = item.read_text(encoding="utf-8").replace(PLACEHOLDER, str(source))

        if item.name in MEMORY_FILES:
            block = marker_block(template_text)
            if destination.exists():
                merged.append(f"{item.name} ({merge_memory(destination, block)})")
            else:
                destination.write_text(template_text, encoding="utf-8")
                created.append(item.name)
            continue

        if destination.exists():
            if not args.force:
                skipped.append(item.name)
                continue
            backup = destination.with_name(f"{destination.name}.bak-{stamp}")
            shutil.copy2(destination, backup)
            backed_up.append(str(backup))
        destination.write_text(template_text, encoding="utf-8")
        created.append(item.name)

    print(f"Project initialized: {project}")
    print(f"Created: {', '.join(created) if created else '(none)'}")
    if merged:
        print(f"Memory blocks merged: {', '.join(merged)}")
    if skipped:
        print(f"Skipped (already exists; use --force to replace): {', '.join(skipped)}")
    if backed_up:
        print(f"Backups: {', '.join(backed_up)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
