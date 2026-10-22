# Project Structure and Portability

## Choose the lightest useful structure

The skill package is reusable guidance; a project workspace contains project-specific source, decisions, media, and outputs. Do not mix project-specific assets into the reusable skill. Create only documents that have content or a clear future use.

Suggested layout for a series or ongoing program:

```text
project/
  README.md                 # entry point, status, links, folder map
  project-brief.md          # purpose, audience, constraints, success
  requirements.md           # requirement IDs, priority, owner, acceptance
  decisions.md              # consequential choices and change history
  evidence/                 # source log, research notes, expert review
  series/
    series-bible.md         # positioning, audience, arc, continuity
    visual-audio-style.md   # reusable visual, voice, sound rules
    terminology.md          # preferred terms, definitions, forbidden ambiguity
    learning-map.md         # goals, dependencies, recurrence and question ledger
  shared/
    templates/
    reusable-assets/        # only where licensing and provenance are recorded
  episodes/
    EP01-topic/
      brief.md
      script/
      storyboard/
      assets/               # provenance/rights record required
      audio/
      edit/
      exports/
      review/
      release/
  releases/                 # final release records, if useful across episodes
```

For one video, use `README.md`, `project-brief.md`, and one episode folder; omit the `series/` layer unless recurring rules are already known. For long-running work, add a roadmap, batch plan, maintenance/review schedule, and retrospective log only when needed.

## README and source of truth

Keep README short. It should identify project scale/current phase, point to authoritative documents, state the latest approved baseline/version, list active blockers and next action, and explain folders. Put detailed requirements in `requirements.md`, rationale in `decisions.md`, and stable series rules in the series bible. Avoid duplicate copies of the same rule.

Label each material statement as confirmed, assumed, open, or recommended where ambiguity could affect work. A decision record should capture ID/date, choice, alternatives considered, rationale, owner, affected requirements/artifacts, and status. A change log should link to the superseded decision rather than erase it.

## Naming and versions

Use stable episode IDs and human-readable slugs. Use filenames that identify episode, artifact, version, and state where helpful, for example `EP02_script_v1.3_approved.md`. Prefer explicit status in a manifest over ambiguous names like `final-final2`. Record which script, audio, graphics, and edit versions produced each export. Keep separate editable sources and release exports.

## Cross-AI use

The canonical guidance is plain Markdown. For another AI that supports skill bundles, copy the skill folder and use its supported discovery mechanism. For a system without skills, provide `SKILL.md` plus only the references required for the task as context/instructions. Product-specific metadata under `agents/` is optional and should be ignored outside compatible hosts. The core guidance must not depend on proprietary tool names, a specific editor, cloud drive, or a specific model.

At each new AI session, point the AI to README/status, then the relevant brief, current approved baseline, linked assets, and applicable reference. Ask it to confirm the task and input versions before making changes. If the environment cannot read files or call another skill, ask for the needed excerpt or state the limitation; do not pretend it did so.

## Git and media storage

Recommend Git for text-first artifacts and editable, reasonably sized project files when the creator can use it: requirements, scripts, prompts, storyboards, subtitle files, structured data, design specs, source graphics, and release records. A Git commit is a named, reviewable recovery point. Useful checkpoints include approved project/series baseline, approved script, approved storyboard/style prototype, accepted rough cut, and release package.

Do not assume Git is the right store for large raw footage, generated media, caches, or rendered masters. Check repository limits, privacy, licensing, backup, and available large-file support before adding binaries. Keep a manifest of external media with stable identifier/path, version/checksum if practical, origin, license/permission, and dependent project. An untracked file is not protected by a Git commit. A remote repository is not automatically a backup or authorization to upload sensitive files.

Before proposing a restore/revert, identify the target checkpoint and affected files, inspect working-tree changes, and preserve current state. Prefer a new branch or copied snapshot for exploration. Never silently rewrite shared history or discard uncommitted work. If Git is unavailable or unwanted, maintain dated snapshots and a version/dependency manifest with equivalent discipline.
