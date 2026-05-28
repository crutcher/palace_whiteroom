---
verifies: ../REPORT.md
critiqued_at: 2026-05-28T040500Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-28T041500Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: pass-after-repair
follow_up_agent: null
---

# META: verification of "Re-anchor L4/index.md — strike SUPERSEDED 'no L3 row needed' verdict"

## Critique

### Checks run

**citation-validity — warning.** Nearly all of this report's load-bearing citations resolve in-range and support their claims. Verified directly: (1) the stale text at `book/src/L4/index.md:40` is present verbatim and the report's `[old]` block matches it byte-for-byte ("…the kernel body's primitive sequence is identity-in-form, so no intermediate L3 `krylov-step` row is needed."); (2) `book/src/L3/krylov-step.md` exists on disk (40,486 bytes / 225 lines); (3) the SUPERSEDED annotation lives at `krylov-step-typed-wrapper-dissolution.md:218` as claimed; (4) the carry-forward flag chain `integrator-signals.md:58, 91, 150, 184` all resolve and describe the flag accurately; (5) `integrator-signals.md:162` carries the "category error" / "wrapper-dissolution RHS rendered as a layer-coherent operator entry" language quoted in the proposed `[new]` text and the report's §"No LHS/RHS shape adjustment"; (6) `L3-L2/krylov-step-body-identity.md` exists. **The one defect**: the Discipline-notes section (CYCLE.md:37) cites `integrator-signals.md:218` and `integrator-signals.md:218` again for the "category error" framing and the line-218 annotation. But `integrator-signals.md:218` is the "No deferrals, no rejections, no rework loops" clean-streak line — NOT the category-error text. The category-error language is at `integrator-signals.md:162`; the line-218 annotation the note means is in the **theme file** (`krylov-step-typed-wrapper-dissolution.md:218`), a different file. The note conflates two files' line-218 and mis-attributes the signals-file citation. The proposed-changes block itself is unaffected (it cites only the theme file correctly), so this is a supporting-prose citation slip, not a defect in the applied surface.

**surface-or-evidence — pass.** This is a refinement-shaped proposal (modifies existing L4/index.md surface text) and it carries the surface change in the `[old]`/`[new]` edit block. The supersession evidence (the firm `L3/krylov-step.md` already on disk; the codified CLAUDE.md invariant; the canonical theme-file annotation it mirrors) is retroactive-evidence-backed and the prose frames it as propagating an already-enacted supersession to a stale cross-reference. Not a pure rotation_claim. Pass.

**rotation-quality — pass / not the operative axis.** This report does not assert a new algebraic/structural rotation; it is a cross-reference cleanup of an existing firm theme. The rotation already lives in `krylov-step-typed-wrapper-dissolution` (wrapper-machinery dissolution → L3 value-threading), which is genuinely state-hiding/compression, not a rename. The edit preserves that rotation's direction (high→low, L4 form lowering to L3) and only re-anchors a trailing consequence clause. No 1:1-rename concern applies. Pass.

**variant-axis-coverage — pass.** No new operator/theme with orthogonal variant axes is introduced. The Form-A/Form-B presentation axis and the variant-absorption axes of `krylov-step` are untouched by this single-bullet edit and are out of scope for it. Not applicable to this cross-reference-cleanup report-kind. Pass.

**cross-reference-integrity — pass.** All link targets in the proposed `[new]` text resolve: `../L3/krylov-step.md` exists; `../L4-L3/krylov-step-typed-wrapper-dissolution.md` exists (with the §"Audit of cycle-002 identity-in-form claim" section the new text anchors to); the cited harvester report `reports/2026-05-27T215300Z-harvester-l3-krylov-step/CYCLE.md` directory exists. The CLAUDE.md invariant slug "Identity-lowerings still require both L levels" is a real §Methodology invariants bullet. No dangling references introduced.

**edge-label-fidelity — pass.** The report consistently discusses the L4>L3 edge (the `krylov-step-typed-wrapper-dissolution` theme is L4>L3; the re-anchor points at the L3 entry that is the dissolution's image). The prose matches the edge it claims throughout. One internal naming wobble worth noting (non-blocking): the dep-map row at `L4/index.md:49` describes the theme's "Lowers to" as "L2 `krylov-step` … via `krylov-step-typed-wrapper-dissolution` (L4>L3 firm …)", and the proposed `[new]` text describes the firm L3 image. These are mutually consistent (L4>L3>L2 chain), and the edit does not touch the dep-map row, so no fidelity violation — just flagging that the page mixes L4>L3 and the transitive L4>L3>L2 framing in adjacent rows.

**plan-kind-consistency — pass.** The declared shape is a lifter re-anchor / single-edit cross-reference cleanup, and the content matches exactly: one `edit:` block touching one bullet, narrative preserved, no new authoring, no rough-in placeholders. The frontmatter `status: pending` is appropriate pre-integration. Kind and content shape are consistent.

**skill-uptake-survey — warning.** The report's shape implies two relevant skills could have been invoked-and-cited: `verify-citation-range` (the report performs a "VERIFY-BEFORE-DISPATCH" line-40 presence check — exactly that skill's job) and `verify-refinement-surface` (this is a refinement-surface edit). The report does the verification work (it confirms the stale text and the L3 entry's existence) but does not name either skill's invocation. Pure telemetry surface; non-blocking. Flagging that a citation-range verification of the supporting-prose citations (which would have caught the `integrator-signals.md:218` mis-attribution noted above) was apparently not run against the Discipline-notes block.

### Issues found

1. **Mis-attributed citation in Discipline notes (CYCLE.md:37).** The note cites `integrator-signals.md:218` for the "category error" framing ("the difference between 'L3 `krylov-step`' and 'L2 `krylov-step` …' is the layer rendering, not the operational content"). That text is actually at `integrator-signals.md:162`. `integrator-signals.md:218` is the unrelated "No deferrals, no rejections, no rework loops" clean-streak line. The note also says "the theme's line-218 annotation" in the same breath — the line-218 that carries the SUPERSEDED/category-error annotation is in `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:218`, a different file. The note conflates a signals-file line number with a theme-file line number. Severity: low (supporting-prose only; the applied `[old]`/`[new]` edit cites the theme file correctly and is unaffected). Candidate fix: change the Discipline-note citation from `integrator-signals.md:218` to `integrator-signals.md:162` (signals "category error" source) and/or to `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:218` (theme annotation), disambiguating which file each line-218 refers to.

2. **Metadata size mismatch for `L3/krylov-step.md` (CYCLE.md:18 vs CYCLE.md:42).** The Summary (line 18) and the integrator-signals lineage describe the L3 entry as "~105 lines"; the Supporting-evidence block (line 42) calls it "~40KB". The on-disk file is 225 lines / 40,486 bytes. The "~40KB" figure is correct; "~105 lines" is stale (it traces to the cycle-010 `integrator-signals.md:162` "(~105 lines)" figure, which was the entry's size at initial landing before subsequent growth). Severity: trivial (does not affect the edit; the line-count is descriptive only). Candidate fix: drop the "~105 lines" parenthetical or update to "~225 lines / ~40KB".

3. **Out-of-scope follow-up flag — VERIFIED ACCURATE (not an issue; recorded as confirmation).** The report's Open-questions §"Out-of-scope" flag (CYCLE.md:52) claims the theme body still phrases the old conclusion as live at `krylov-step-typed-wrapper-dissolution.md:20` and `:220`. Confirmed by direct read: line 20 contains "…so **no L3 `krylov-step` row is promoted by this theme**…" and line 220 contains "…the assertion holds, the framing is sharpened, **no L3 row needed**." Both are inside the theme body and both phrase the superseded conclusion without the inline SUPERSEDED hedge that line 218 carries. The follow-up recommendation (a separate `lifter` dispatch to re-anchor lines 20 and 220) is well-founded and correctly scoped out of this single-edit invocation. No action needed on this report; the flag is a true positive for the planner's queue.

4. **Skill-invocation not surfaced (telemetry, CYCLE.md throughout).** Neither `verify-citation-range` nor `verify-refinement-surface` is named despite the report performing both kinds of work. Severity: trivial / non-blocking. A citation-range pass over the supporting-prose block would have caught issue 1.

---

## Repair

### Fixes attempted

- **Finding (Issue 1, citation-validity warning)**: Discipline-notes (CYCLE.md:37) cited `integrator-signals.md:218` for the "category error" framing, but that text is at `integrator-signals.md:162`; line 218 is the unrelated "No deferrals, no rejections, no rework loops" clean-streak line. The note also conflated the signals-file line-218 with the theme-file annotation at `krylov-step-typed-wrapper-dissolution.md:218`.
  - **Decision**: repaired.
  - **Action**: Edited CYCLE.md §"Discipline notes" → "Why the change" bullet (CYCLE.md:37). Changed `integrator-signals.md:218` → `integrator-signals.md:162` (the signals-file "category error" source, verified by direct read of lines 158-169) and disambiguated the theme-file annotation as `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:218` (verified by direct read of theme line 218, which carries the SUPERSEDED + category-error language). Mechanical citation-offset correction; no content authored. The applied `[old]`/`[new]` surface edit cites the theme file correctly and was already unaffected.

- **Finding (Issue 2, citation-validity warning / trivial size mismatch)**: "~105 lines" (CYCLE.md:18) vs "~40KB" (CYCLE.md:42); actual `book/src/L3/krylov-step.md` is 225 lines / 40,486 bytes. The "~105 lines" figure was stale (traces to the cycle-010 `integrator-signals.md:162` initial-landing size).
  - **Decision**: repaired.
  - **Action**: CYCLE.md:18 "~105 lines" → "225 lines"; CYCLE.md:42 "~40KB" → "225 lines / ~40KB" for paired-figure consistency. Mechanical metadata correction; descriptive only, does not affect the applied edit.

- **Finding (Issue 3, out-of-scope follow-up flag — confirmed accurate, not a defect)**: The L4-L3 theme body (`krylov-step-typed-wrapper-dissolution.md:20` and `:220`) still phrases the old "no L3 row needed" conclusion as live; critic confirmed both passages present by direct read. This is a valid cycle-013 follow-up, not a defect in this report.
  - **Decision**: repaired (OQ-capture hardening only — no authoring).
  - **Action**: Strengthened CYCLE.md §"Open questions / caveats" out-of-scope bullet so the integrator-per-report reliably promotes it: added an explicit suggested OQ slug `krylov-step-theme-body-no-l3-row-drift-cycle-013`, routed to cycle-013+ planner, and noted the critic's direct-read confirmation. Repairer does NOT write `scaffolding/open-questions.md` (integrator-per-report is the sole appender, append-only); this surfaces the OQ candidate in the report so the integrator promotes it. Verified no existing OQ in `scaffolding/open-questions.md` covers the theme-body line-20/line-220 residual (the existing krylov-step-chain OQs cover the cycle-006→cycle-008 trajectory reconciliation, all answered/closed).

- **Finding (Issue 4, skill-uptake-survey warning — telemetry)**: Neither `verify-citation-range` nor `verify-refinement-surface` was named.
  - **Decision**: not-needed (informational telemetry only).
  - **Rationale**: Pure non-blocking telemetry per the critic. No surface or evidence defect; naming a skill post-hoc would be authoring telemetry the producer did not record. Left as-is.

### Unrepairable findings

None. All flagged findings were mechanical/surgical (citation-offset correction, metadata correction, OQ-capture hardening) or informational telemetry. No substantive authoring was required; no contradiction with existing artifact content surfaced.

## Suggested resolution

`overall_status: pass-after-repair` (ready). The applied `[old]`/`[new]` edit was already correct (critic confirmed byte-for-byte match) and is unaffected by the repairs — all fixes were to supporting prose / metadata.

Integrator notes:
- Apply the single `edit:book/src/L4/index.md` block as proposed; surface is correct.
- Promote the out-of-scope OQ candidate `krylov-step-theme-body-no-l3-row-drift-cycle-013` (theme-body line-20/line-220 stale "no L3 row needed" phrasing) to `scaffolding/open-questions.md`, routed to cycle-013+ planner / `lifter`. This is the one true-positive follow-up; it is low-cost and non-blocking.
