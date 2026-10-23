---
name: video-learning-workflow
description: Plan, produce, review, version, and prepare educational or science-communication videos with an AI collaborator, from an initial idea through platform-ready deliverables. Use for a single video, a series, or an ongoing video program.
license: MIT
metadata:
  short-description: Cross-client workflow for AI-assisted educational video projects
  version: "1.1.1"
---

# Video Learning Workflow

Act as the creator's production and instructional-design partner. Guide decisions, maintain a reliable project state, create reviewable artifacts, coordinate available specialist skills, and help the creator make informed choices. The creator remains the authority on goals, audience, content stance, major creative direction, and final publication.

This package uses the open Agent Skills layout: a required `SKILL.md` plus optional `references/`, `scripts/`, and `assets/`. The guidance is client-neutral. Codex, Claude Code, WorkBuddy, and other compatible hosts differ mainly in where they install skills and which project-memory filename they load; use the host adapter you need, and never claim access to a tool, account, or media capability that is not actually available.

## Start and route

1. Inspect the project workspace and its README or status document before asking for information already recorded. If this is a new project, begin with discovery; do not start production from a vague premise.
2. Identify scale: `single`, `series`, or `ongoing`. Keep one shared lifecycle and activate only the governance and templates the scale needs. Read [project structure](references/project-structure.md).
3. Identify the requested phase and next decision. Read [workflow and decision rules](references/workflow.md). Do not force a full lifecycle when the creator asks for a bounded task, but flag missing upstream decisions that could invalidate the work.
4. Before instructional design, read [teaching design](references/teaching-design.md). Before setting up project files or Git, read [project structure](references/project-structure.md) and [quality, Git, and release](references/quality-git-release.md) as applicable.
5. Discover relevant specialist skills in the current environment for research, instructional design, writing, image/video generation, audio, editing, subtitles, accessibility, or publishing. Read and invoke only skills that are available and materially useful. The workflow owns coordination and project consistency; a specialist skill owns its specialist execution. Resolve conflicts in favor of creator-approved project requirements, and report material conflicts.
6. On first use in a project whose root has no project memory file, run the project initializer described below before other work. It seeds project memory and starter documents, so later sessions in each supported host know to load this skill without being re-invoked by hand.

## Installation and project initialization

Keep one canonical skill folder and let each host discover or install it in its own location. Do not add host-specific frontmatter to this `SKILL.md`; when a marketplace requires extra metadata, export a separate host package instead.

Install the same folder for the hosts you use (run from the skill folder):

```text
python scripts/install.py --scope user --targets codex,claude,workbuddy
python scripts/install.py --scope project --project <project-root> --targets codex,claude,workbuddy
```

`--targets` accepts `codex`, `claude`, `workbuddy`, and `generic`. `generic` copies into `<project>/.agents/skills/`, the shared alias for clients that follow the Agent Skills standard. The script copies the skill and never edits the canonical source. `--force` replaces only the destination folder for this skill, and only after confirming that folder contains a `SKILL.md` for the same skill name.

Default discovery locations:

| Host | User skills | Project skills | Project memory file |
|---|---|---|---|
| Codex | `~/.agents/skills/` | `<project>/.agents/skills/` | `AGENTS.md` |
| Claude Code | `~/.claude/skills/` | `<project>/.claude/skills/` | `CLAUDE.md` |
| WorkBuddy / CodeBuddy | `~/.codebuddy/skills/` | `<project>/.codebuddy/skills/` | `AGENTS.md` or `CODEBUDDY.md` |

Initialize a project once from any operating system with Python 3:

```text
python scripts/init_project.py --project <project-root> [--force]
```

The initializer copies the starter documents into the project root and writes (or merges into existing) thin memory blocks in `AGENTS.md`, `CLAUDE.md`, and `CODEBUDDY.md`, substituting the resolved skill path. The memory blocks are wrapped in `<!-- video-learning-workflow:start -->`/`<!-- video-learning-workflow:end -->` markers, so re-running the initializer refreshes them without touching the rest of the file. They say when to load `video-learning-workflow`, where the project starts, and that publication needs explicit confirmation; they do not duplicate the workflow.

On Windows, `scripts/init_project.ps1 [-ProjectRoot <path>] [-Force]` performs the same project initialization without Python. With `-Force`, each existing file is backed up to `<name>.bak-<timestamp>` before replacement; without it, existing files are left untouched.

WorkBuddy separates local import from public distribution. Adding a ZIP through the desktop app (Skills > Add Skill > Upload Skill) installs it only for that user. To publish to the marketplace, register on the WorkBuddy Open Platform, create the skill there, submit it for review, and publish only after approval. The Open Platform accepts only two directory levels (root/subdirectory/file), so the exporter flattens `assets/project-starter/` into `assets/` and rejects any deeper path. Build that submission package with the extra metadata the Open Platform expects:

```text
python scripts/export_workbuddy.py --output <path>/video-learning-workflow-openplatform.zip
```

If a session cannot run the setup scripts, copy the starter templates into the project root manually and replace the `__SKILL_ROOT__` placeholder in each memory file with the resolved skill folder path.

## Core operating rules

- Distinguish confirmed facts, creator decisions, assumptions, open questions, and recommendations in project records. Never silently promote an assumption to a decision.
- Ask the few highest-impact questions first. Offer a recommendation, alternatives, rationale, and consequences. Keep routine reversible work moving within the agreed scope.
- Before substantial production, establish a project/series blueprint and an episode design brief covering learning goals, audience, scope, format, presenter/character approach, opening and ending, teaching methods, visual/audio direction, platform deliverables, risks, and acceptance evidence. Use a representative sample to validate uncertain execution details instead of specifying every animation before seeing it.
- Map each important learning goal to content, a teaching move, an audiovisual treatment, and observable evidence. Select methods for fit; never insert every named method by default. Read [teaching design](references/teaching-design.md).
- Track requirements to artifacts and acceptance checks. Keep version identifiers and dependencies explicit so feedback can be localized and related deliverables can be regenerated.
- At phase transitions, report completed artifacts and versions, checks and evidence, open issues/assumptions, and the next decision or action. Do not report vague percent-complete when accepted work can be counted.
- For material changes, summarize reason, affected requirements/artifacts, reusable work, rework, schedule/cost/quality implications, and lower-cost alternatives before proceeding when the change exceeds the creator's delegated authority.
- Recommend Git or equivalent snapshots when useful. Before any restore, reset, overwrite, or destructive history operation, state the exact scope and preserve uncommitted work; do not execute destructive recovery without explicit authorization.
- Prepare upload/package details and perform allowed pre-publication checks. **Stop before final publication and present the exact platform, account, asset/version, public-facing text, visibility/schedule settings, and validation status. Publish only after the creator explicitly confirms that specific release.**

## Minimum useful artifacts

Scale these to the project; do not create empty paperwork. A single-video project may use one brief and a compact checklist. Series/ongoing projects should have a README/status entry point, shared series rules, episode folders, decision/change records, and release records. Starter templates are in `assets/project-starter/` in the repository (flattened to `assets/` in the Open Platform export).

At minimum, maintain:

- Project-scoped memory files at the project root, so each host loads this skill and the project status without per-session prompting.
- Project status/README and project brief.
- Requirements and deliverables with priorities and acceptance evidence.
- Source/evidence log for substantive claims.
- Episode design brief, script, and storyboard or equivalent audiovisual plan.
- Decision and issue/change records when decisions or changes occur.
- Review/acceptance record and release checklist for each delivered version.

## Reference routing

- Use [workflow and decision rules](references/workflow.md) for phases, gates, question strategy, task handoffs, status, and change control.
- Use [teaching design](references/teaching-design.md) for method selection, learning-goal mapping, presenter/persona design, and cross-episode learning.
- Use [project structure](references/project-structure.md) to create or adapt a workspace and decide what to track in Git.
- Use [quality, Git, and release](references/quality-git-release.md) for acceptance, review, recovery points, rights/accessibility checks, and publication preparation.
