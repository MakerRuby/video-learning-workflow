# Quality, Git, and Release

## Acceptance dimensions

Use separate checks for conformance (does the deliverable meet requirements?) and fitness (does it work for the intended viewer and use?). Scale the review to risk; do not claim a check was performed without evidence.

| Dimension | Example checks | Evidence |
|---|---|---|
| Factual | Claims match sources; dates/units/causal language correct; uncertainty represented | Claim/source log and subject review |
| Instructional | Outcomes observable; sequence intelligible; prerequisites supplied; questions answered; examples transfer | Outcome map, target-viewer walkthrough, short recall/application check |
| Narrative/creative | Hook earns attention; pacing supports comprehension; presenter/dialogue roles work; ending fulfills its promise | Timed animatic and review notes |
| Visual | Text readable on target screen; diagrams have clear reading order; no collisions/crops; style continuity | Frame review at intended display size and platform preview |
| Audio | Speech intelligible; levels consistent; music/effects do not mask speech; sync correct | Full playback on representative devices/headphones |
| Accessibility | Accurate captions; meaningful on-screen text; essential sound conveyed where needed; contrast and reading time adequate | Caption inspection and accessibility review |
| Technical | Correct aspect/dimensions/frame rate/codec/audio; complete playback; no blank, corrupt, or unintended frames | Export metadata and full/targeted playback |
| Rights/privacy | Permission/license/provenance for media, music, fonts, likeness, voice, and participant data | Asset register, releases, attribution where required |
| Platform | Current official constraints; safe areas, thumbnail, metadata, caption behavior, upload preview | Dated official-source check and actual platform preview |
| Handoff | Project opens; dependencies/assets are present or documented; versions map to export | Clean-open test and release manifest |

Create must-pass criteria separately from scored refinements. A critical factual error, broken file, missing required permission, or obscured essential instruction is not averaged away by a high aesthetic score. Record accepted exceptions and their owner.

## Review method

For each review issue, record ID, exact timecode/frame/document location, expected behavior, observed behavior, severity, affected requirement, proposed fix, owner, and status. Separate blocker/defect, in-scope refinement, and optional idea. Review representative samples early and all final deliverables before release. Watch/listen at normal speed in the target context; automated checks supplement human review.

For learning fit, test with a representative viewer when feasible. Use a small, relevant prompt or task tied to the learning outcome. A view count or positive reaction alone does not prove comprehension. Treat small-sample feedback as a signal with limitations.

## Git checkpoint policy

Suggest meaningful commits at accepted baselines, not every keystroke. Example checkpoint messages:

- `baseline: approve series bible and EP01 scope`
- `baseline: approve EP01 script v1.2`
- `prototype: accept 30-second style and format sample`
- `baseline: accept rough cut structure`
- `release: EP01 horizontal and vertical exports`

Before a major experiment, check status and create a branch or snapshot if appropriate. After review, merge/retain accepted work and preserve useful alternatives. For recovery, describe the target and impact first. Do not run destructive commands such as hard reset or force-push without explicit authorization. Git is version control, not the only backup strategy.

## Rights, privacy, and accessibility

Maintain provenance and permissions as assets enter the project, not only before export. Flag unclear rights for creator review. Avoid uploading confidential or identifiable material to external services unless the creator's permissions and applicable tool policy allow it. Provide captions and accessible equivalents for essential information; account for small-screen reading and viewers who cannot hear narration. Treat jurisdiction-specific legal conclusions as requiring appropriate review rather than guessing.

## Release preparation and confirmation boundary

Recheck changeable platform requirements against current official documentation near upload and record source/date. Prepare a release manifest with:

- exact platform/account and target audience;
- exact file name/version, aspect ratio, duration, captions, thumbnail, and checksum if useful;
- title, description, references/credits, tags, chapters, disclosure, and accessibility options;
- visibility, schedule, monetization or audience settings as applicable;
- factual/rights/technical/preview checks and unresolved exceptions;
- intended publication action and rollback/correction contact or process.

The AI may prepare and validate the package and may upload or save a draft when tools and authorization permit. Before the final action that makes the release public or otherwise publishes it, show the complete release manifest and wait for explicit creator confirmation for that specific release. A prior general instruction to help publish is not confirmation of the final package. After confirmation and execution, verify the resulting platform state and record the URL/status/time; report any discrepancy.
