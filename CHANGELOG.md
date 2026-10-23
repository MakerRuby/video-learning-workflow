# Changelog

## 1.1.0

- Reworked the package for the open Agent Skills layout so one canonical folder works in Codex, Claude Code, and WorkBuddy-compatible clients.
- Added `scripts/install.py` to copy the skill into each client's discovery paths (`codex`, `claude`, `workbuddy`, `generic`); `--force` refuses to replace a folder that is not this skill.
- Added `scripts/init_project.py` (cross-platform) and `scripts/init_project.ps1` (Windows, no Python) to seed starter documents and merge project-memory blocks into `AGENTS.md`, `CLAUDE.md`, and `CODEBUDDY.md`.
- Memory blocks are delimited by `<!-- video-learning-workflow:start -->` / `<!-- video-learning-workflow:end -->`, so re-running the initializer refreshes the block without touching surrounding project rules.
- Added `assets/project-starter/` host memory templates.
- Added `scripts/export_workbuddy.py` for WorkBuddy Open Platform submission, with the extra metadata and `config.yaml` that the platform validates.
- Clarified that uploading a ZIP in the WorkBuddy desktop app installs the skill locally only; a public marketplace listing requires Open Platform registration, review, and approval.
- Added `.gitignore` for Python caches and build output.

## 1.0.0

- Initial release: lifecycle, teaching design, project structure, quality/Git/release references, and project starter templates.
