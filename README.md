# Video Learning Workflow

An AI collaboration workflow for planning, producing, reviewing, versioning, and preparing educational or science-communication videos for release. It supports a single video, a series, or an ongoing program, and keeps the creator in control of major decisions and final publication.

## Use

This package is plain Markdown and has no runtime dependencies. In an AI environment that supports skills, install or link this folder using that environment's skill mechanism. In other environments, provide `SKILL.md` and the relevant files from `references/` as reusable instructions. Product-specific metadata is intentionally optional.

Start a new project by describing the video idea and ask the AI to use this workflow. The workflow first clarifies the audience, outcomes, scope, delivery formats, and constraints; then it creates an appropriate project workspace from `assets/project-starter/` and proceeds through design, prototype, production, review, and release preparation.

## Package contents

- `SKILL.md`: entry point, routing, operating rules, and publication boundary.
- `references/workflow.md`: lifecycle, decisions, task handoffs, and change control.
- `references/teaching-design.md`: learning outcomes, teaching-method selection, and series learning architecture.
- `references/project-structure.md`: project folders, documentation, portability, and Git guidance.
- `references/quality-git-release.md`: review criteria, recovery checkpoints, rights, accessibility, and release preparation.
- `assets/project-starter/`: reusable project, series, episode, task, review, and release templates.

The AI may prepare and validate a release package, but must pause and present the exact release details for the creator's confirmation before publication.

## License

Licensed under the MIT License. See [LICENSE](LICENSE).
