# Video Learning Workflow

A portable workflow for planning, producing, reviewing, versioning, and preparing educational or science-communication videos for release. It supports one video, a series, or an ongoing program and keeps the creator in control of major decisions and final publication.

The package follows the open [Agent Skills](https://agentskills.io) layout (`SKILL.md` plus optional `references/`, `scripts/`, and `assets/`). It is not tied to Codex: the same folder works in Codex, Claude Code, and WorkBuddy-compatible environments, with small differences in installation and project-memory filenames.

Current version: **1.1.0** (see [CHANGELOG.md](CHANGELOG.md)).

## Quick start

```text
# 1. Register the skill where each client discovers it
python scripts/install.py --scope user --targets codex,claude,workbuddy

# 2. Initialize a project: starter documents + project memory
python scripts/init_project.py --project <project-root> [--force]

# 3. Optional: build a package for WorkBuddy Open Platform review
python scripts/export_workbuddy.py --output dist/video-learning-workflow-openplatform.zip
```

Requirements: Python 3.10+ for the helper scripts. The workflow itself is plain Markdown and has no runtime dependency. Windows users can initialize without Python via `scripts/init_project.ps1 [-ProjectRoot <path>] [-Force]`.

When the initializer runs, it writes `AGENTS.md`, `CLAUDE.md`, and `CODEBUDDY.md` into the project root. Each is a short pointer to this skill and the project status, so later sessions load the workflow without repeating the request:

| Client | Skill location | Project memory |
|---|---|---|
| Codex | `~/.agents/skills/` (recommended) or `~/.codex/skills/`; project: `<project>/.agents/skills/` | `AGENTS.md` |
| Claude Code | `~/.claude/skills/` or `<project>/.claude/skills/` | `CLAUDE.md` |
| WorkBuddy / CodeBuddy code workspace | `~/.codebuddy/skills/` or `<project>/.codebuddy/skills/` | `CODEBUDDY.md` or `AGENTS.md` |

Two different WorkBuddy paths exist, and they are easy to confuse:

- **Local use only:** in the desktop app use **技能 > 添加技能 > 上传技能**. This imports the skill into *your* WorkBuddy. It does not publish it, and other users cannot see or install it.
- **Public marketplace listing:** register and pass qualification review on the [WorkBuddy Open Platform](https://open.workbuddy.cn) (入驻 → 创建技能 → 提交审核 → 审核通过后发布). Upload the ZIP produced by `scripts/export_workbuddy.py` there, not in the desktop app. Only after platform review and publication can other users find and install it.

The export script adds the Chinese/English descriptions and `config.yaml` that the Open Platform validates, without polluting the canonical `SKILL.md`.

## What the workflow does

The workflow first clarifies the audience, outcomes, scope, delivery formats, and constraints. It then creates the lightest useful project workspace and proceeds through discovery, design, prototyping, production, review, versioning, and release preparation. It distinguishes facts, decisions, assumptions, and open questions; coordinates specialist skills when they exist; and pauses before any public publication.

Start a new project by describing the video idea and asking the AI to use `video-learning-workflow`. In Codex, invoke it as `$video-learning-workflow`; in Claude Code, use `/video-learning-workflow`. Managed projects also carry memory files, so the next session can pick up the workflow and current status automatically.

## Package contents

- `SKILL.md`: entry point, routing, operating rules, installation, and publication boundary.
- `references/workflow.md`: lifecycle, decisions, task handoffs, and change control.
- `references/teaching-design.md`: learning outcomes, teaching-method selection, and series learning architecture.
- `references/project-structure.md`: project folders, documentation, portability, and Git guidance.
- `references/quality-git-release.md`: review criteria, recovery checkpoints, rights, accessibility, and release preparation.
- `assets/project-starter/`: project, series, episode, task, review, and release templates plus host memory files.
- `scripts/install.py`: copies the canonical skill into Codex, Claude Code, and WorkBuddy/CodeBuddy discovery paths.
- `scripts/init_project.py` / `scripts/init_project.ps1`: initialize a project and write project-scoped memory.
- `scripts/export_workbuddy.py`: build a WorkBuddy Open Platform submission ZIP (for review/publication, not local import).
- `CHANGELOG.md`: release history.

The AI may prepare and validate a release package, but it must present the exact release details and wait for the creator's confirmation before publication.

## License

Licensed under the MIT License. See [LICENSE](LICENSE).
