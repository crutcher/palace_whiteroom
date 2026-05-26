# Open questions ledger

Cross-cycle ledger of open questions about the target source or methodology. Replaces the old `questions.md` (which stays in place as the archive of seed questions from BOOTSTRAP).

**Format** (one section per question):

```yaml
---
slug: short-kebab-case
opened_at: cycle-NNN | YYYY-MM-DD
opened_by: <agent-name> | human
last_revisited: cycle-NNN | null
status: open | investigating | answered | dropped
answered_at: cycle-NNN  (when status=answered)
answered_in: <commit-sha> | <slice-path> | <ledger-pattern>  (when status=answered)
---
```

Each section: **slug**, **question text** (1–3 sentences), **context** (where this surfaced and why), and **status**.

**Discipline:**
- Any agent appends; never edits existing sections (except status).
- Integrator promotes per-report REPORT.md "Open questions / caveats" sections into this ledger on landing.
- Meta-phase reviews open questions periodically and may drop stale ones (status `dropped` with reason) or promote into friction-ledger / skill-candidates.
- Cycle-planner reads as a priority input — long-open questions get attention.

## Open

(bootstrap: migrate currently-open questions from `questions.md` here as Phase B continues)

## Investigating

(empty)

## Answered

(empty — will accumulate)

## Dropped

(empty — will accumulate)
