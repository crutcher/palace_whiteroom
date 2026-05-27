# Skill: summary-md-surgical-insert

**Audience**: `integrator-per-report` (primary). Per-cycle writers of `book/src/SUMMARY.md`.

**Purpose**: register new chapter rows in `book/src/SUMMARY.md` under multi-writer waves without collision. Codifies the discipline observed across cycles 003–005 (scaling 2 → 5 → 5 concurrent writers with zero conflict).

## When to invoke

- A report you are applying creates `book/src/L<n>/<slug>.md` or `book/src/L<n>-L<m>/<slug>.md` or `book/src/concepts/<slug>.md`.
- The report's `## Proposed changes` blocks contain a SUMMARY.md edit (the report-proposed case), or it does not (the auto-fix case authorized by integrator-per-report's gate `SUMMARY-chapter-registration-auto-fix`).
- Other per-report integrators in the same cycle may also be editing SUMMARY.md (cycle-005 high-water-mark: 5 concurrent writers).

## Procedure

1. **Re-read SUMMARY.md fresh just before the Edit.** Do NOT trust an earlier view — previous per-report integrators in this cycle may have inserted rows you have not seen yet. Use `Read` on `book/src/SUMMARY.md` immediately before the `Edit` call.

2. **Locate the literal-string anchor.** Identify the sibling-chapter row or Part heading the insert should be adjacent to. Examples:
   - For a new L<n> firm operator: anchor on the alphabetically-prior sibling chapter row under the `# L<n>` Part heading.
   - For a new L<n+1>>L<n> theme: anchor on the alphabetically-prior sibling theme row under the `# L<n+1>>L<n>` Part heading.
   - For a new concepts page: anchor on the alphabetically-prior concept row under the Concepts section, or append at end of Concepts before the next Part heading.
   - For a Part-heading rename (e.g., `# L0 — Cited Palace Source` → `# L0 — Cited Palace Source + Reference Notes`): full literal-string match on the prior heading.

3. **Edit with literal-string anchor, not byte offset.** Use the `Edit` tool with `old_string` = the literal full row of the sibling anchor (or the heading line for renames). Append the new row after the anchor (or replace, for heading renames). NEVER use byte offsets — they go stale the moment another writer inserts upstream.

4. **Record in STAGING.md Notes.** When you are the first per-report integrator in a cycle and other dispatches may follow, include in your staging row's `Notes:` a line like:

   > SUMMARY edit applied as surgical N-line insert rather than full-file replacement to preserve append-points for subsequent in-cycle integrators.

   Subsequent in-cycle integrators read your Notes and echo the discipline.

## Failure modes

- **Byte-offset Edit:** stale anchor when previous per-report integrator inserted upstream. Symptom: Edit fails with "string not found". Recovery: re-read disk, re-locate the literal anchor, retry.
- **Full-file replacement:** silently overwrites previous in-cycle integrator's row insert. Symptom: missing chapter rows after rebuild. Recovery: caught by integrator-finalize's book rebuild + cross-reference check; avoid by using surgical Edit always.
- **Multiple-anchor-matches:** the literal anchor string occurs more than once in SUMMARY.md (e.g., a slug name appears in two Parts). Symptom: Edit fails for non-unique old_string. Recovery: expand the anchor to include the prior 2-3 lines for uniqueness (Part heading + sibling chapter row).
- **Concepts-page-not-proposed:** the report creates `concepts/<slug>.md` but does not propose a SUMMARY edit. Recovery: apply the auto-fix per integrator-per-report's `SUMMARY-chapter-registration-auto-fix` gate, record as `applied-discretionarily` in the staging row.

## Discipline

- **Re-read disk every time.** Even within one role invocation.
- **Literal-string anchors only.** No byte offsets, no line numbers.
- **Surgical Edit, never full-file Write.** SUMMARY.md is a multi-writer shared file.
- **Preserve append-points.** Every Edit should leave the file usable by the next per-report integrator.
- **Notes-channel propagation.** The discipline is self-perpetuating via the STAGING.md Notes field — first per-report integrator establishes the discipline in writing; subsequent integrators echo it.

## Cross-references

- Friction-ledger pattern `summary-md-serial-write-discipline` (recurrence-3 across cycles 003–005).
- Friction-ledger pattern `wave-conflict-philosophy-scales` (the parent positive pattern that this skill is part of).
- Role spec `.claude/agents/integrator-per-report.md` §Process step 5 (the `SUMMARY-chapter-registration-auto-fix` gate that authorizes the auto-fix case).
- Role spec `.claude/agents/integrator-per-report.md` §Discipline (the "Re-read disk at every Edit" bullet).

## Provenance

- Promoted: cycle-005 meta-phase (2026-05-27).
- Pattern observed: cycle-003 (2 writers), cycle-004 (5 writers under single-pass integrator), cycle-005 (5 writers under split integrator).
- Originated: cycle-005 dispatch #1 (`harvester-krylov-step-L2`) staging-row Notes-channel discipline declaration.
