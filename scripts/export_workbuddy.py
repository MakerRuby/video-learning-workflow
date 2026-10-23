#!/usr/bin/env python3
"""Build a package for the WorkBuddy Open Platform (marketplace submission).

This is NOT the "Add Skill > Upload Skill" local import in the WorkBuddy
desktop app. That local import installs the skill only for the current user.
Public listing requires registering at open.workbuddy.cn, passing developer
qualification review, creating the skill there, submitting it for platform
review, and publishing after approval.

WorkBuddy rejects skill packages with more than two directory levels
(root/subdirectory/file). The canonical skill keeps starter documents under
assets/project-starter/; this exporter flattens them into assets/ and rewrites
the bundled setup scripts so the uploaded package still initializes projects.

The Open Platform also validates extra metadata such as description_zh,
description_en, version, and author. Those fields do not belong in the
canonical SKILL.md, so this script writes a separate package while leaving
the source untouched.

Example:
    python scripts/export_workbuddy.py --output dist/video-learning-workflow-openplatform.zip
"""


import argparse
import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

SKILL_NAME = "video-learning-workflow"
VERSION = "1.1.1"
AUTHOR = "video-learning-workflow contributors"
CATEGORY = "productivity"
DESCRIPTION_ZH = "规划、制作、审核、版本管理并发布教育或科普视频的完整工作流，支持单条视频、系列课程和长期栏目。"
DESCRIPTION_EN = (
    "Plan, produce, review, version, and prepare educational or "
    "science-communication videos, for a single video, a series, or an "
    "ongoing program."
)
TRIGGERS = [
    "教育视频",
    "科普视频",
    "教学视频",
    "视频脚本",
    "视频分镜",
    "课程视频",
    "educational video",
    "science communication video",
    "video script",
    "storyboard",
]


def skill_root() -> Path:
    return Path(__file__).resolve().parent.parent


def split_frontmatter(text: str) -> tuple[str, str]:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.DOTALL)
    if not match:
        raise ValueError("SKILL.md must start with YAML frontmatter")
    return match.group(1), match.group(2)


def scalar(frontmatter: str, key: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", frontmatter)
    if not match:
        return None
    value = match.group(1).strip()
    if value.startswith(("'", '"')) and value.endswith(("'", '"')):
        value = value[1:-1]
    return value


def yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def workbuddy_skill_md(body: str, description: str) -> str:
    triggers = "\n".join(f"  - {yaml_quote(t)}" for t in TRIGGERS)
    # The package flattens assets/project-starter/ to assets/.
    body = body.replace("assets/project-starter/", "assets/")
    return (
        "---\n"
        f"name: {SKILL_NAME}\n"
        f"display_name: 教育视频工作流\n"
        f"display_name_en: Video Learning Workflow\n"
        f"description: {yaml_quote(description)}\n"
        f"description_zh: {yaml_quote(DESCRIPTION_ZH)}\n"
        f"description_en: {yaml_quote(DESCRIPTION_EN)}\n"
        f"category: {CATEGORY}\n"
        f"version: {yaml_quote(VERSION)}\n"
        f"author: {yaml_quote(AUTHOR)}\n"
        "triggers:\n"
        f"{triggers}\n"
        "---\n\n"
        + body.lstrip("\n")
    )


def config_yaml(description: str) -> str:
    triggers = "\n".join(f"  - {yaml_quote(t)}" for t in TRIGGERS)
    return (
        f"name: {SKILL_NAME}\n"
        f"version: {yaml_quote(VERSION)}\n"
        f"description: {yaml_quote(description)}\n"
        f"description_zh: {yaml_quote(DESCRIPTION_ZH)}\n"
        f"category: {CATEGORY}\n"
        f"author: {yaml_quote(AUTHOR)}\n"
        "triggers:\n"
        f"{triggers}\n"
    )


def flatten_assets(source: Path, destination: Path) -> None:
    """Copy starter documents to assets/<file> (no nested directory)."""
    starter = source / "assets" / "project-starter"
    destination.mkdir(parents=True, exist_ok=True)
    if not starter.is_dir():
        return
    for item in sorted(starter.iterdir()):
        if item.is_file():
            shutil.copy2(item, destination / item.name)


def rewrite_packaged_script(path: Path) -> None:
    """Point bundled setup scripts at the flattened assets directory."""
    text = path.read_text(encoding="utf-8")
    text = text.replace('source / "assets" / "project-starter"', 'source / "assets"')
    text = text.replace("assets/project-starter", "assets")
    text = text.replace(r"assets\project-starter", "assets")
    path.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--force", action="store_true", help="overwrite the output ZIP")
    args = parser.parse_args()

    source = skill_root()
    skill_md = source / "SKILL.md"
    if not skill_md.is_file():
        print(f"error: SKILL.md not found under {source}", file=sys.stderr)
        return 1

    frontmatter, body = split_frontmatter(skill_md.read_text(encoding="utf-8"))
    description = scalar(frontmatter, "description")
    if not description:
        print("error: description is missing from SKILL.md frontmatter", file=sys.stderr)
        return 1

    output = args.output.resolve()
    if output.exists() and not args.force:
        print(f"error: {output} exists; pass --force to replace it", file=sys.stderr)
        return 1
    output.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp:
        package = Path(tmp) / SKILL_NAME
        package.mkdir()

        for item in ("references", "scripts"):
            origin = source / item
            if origin.is_dir():
                shutil.copytree(
                    origin,
                    package / item,
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store"),
                )
        flatten_assets(source, package / "assets")

        (package / "SKILL.md").write_text(
            workbuddy_skill_md(body, description), encoding="utf-8"
        )
        (package / "config.yaml").write_text(config_yaml(description), encoding="utf-8")
        readme = source / "README.md"
        if readme.is_file():
            text = readme.read_text(encoding="utf-8").replace(
                "assets/project-starter/", "assets/"
            )
            (package / "README.md").write_text(text, encoding="utf-8")
        license_file = source / "LICENSE"
        if license_file.is_file():
            shutil.copy2(license_file, package / "LICENSE")

        for script_name in ("init_project.py", "init_project.ps1"):
            script = package / "scripts" / script_name
            if script.is_file():
                rewrite_packaged_script(script)

        # WorkBuddy only accepts root/<one directory>/<file>.
        for path in sorted(package.rglob("*")):
            if path.is_file():
                relative = path.relative_to(package)
                if len(relative.parts) > 2:
                    raise ValueError(
                        "WorkBuddy package has a directory level deeper than two: "
                        f"{relative.as_posix()}"
                    )

        temp_zip = output.with_suffix(output.suffix + ".tmp")
        with zipfile.ZipFile(temp_zip, "w", zipfile.ZIP_DEFLATED) as archive:
            for path in sorted(package.rglob("*")):
                if path.is_file():
                    archive.write(path, path.relative_to(Path(tmp)).as_posix())
        temp_zip.replace(output)

    print(f"WorkBuddy package written: {output}")
    print("Submit this ZIP on the WorkBuddy Open Platform (open.workbuddy.cn) for review; publishing requires approval.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
