---
verifies: ../CYCLE.md
critiqued_at: 2026-06-02T064500Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-06-02T065200Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "L4 index cohort refresh" (cycle-059 D2)

## Critique

### Checks run

**citation-validity — pass.** The report's load-bearing factual claims are the two count-owner `## Status` reads and the source-witness citations carried in the new prose. Spot-checked both on disk: `book/src/L4/fold_solve.md` `## Status` heading is at line 155 with `firm` asserted at the cited line 157 (the firm-on-positive-structure escape paragraph, in-range; the `:157` pinpoint lands on the status-value prose, not the heading — acceptable, the value is what is being cited). `book/src/L4/solve_family.md` `## Status` heading is at line 142 with `rough-in (test-coverage-bounded)` at the cited line 144 (in-range, value correct, unchanged this cycle). The 6 other firm-cohort `## Status` reads in §Supporting evidence (krylov-step, iterate-while, iterate-while-with-prev, chebyshev, ksp_solve, eigsolve) are consistent with the index dep-map's firm rows. Source-witness citations carried into the new prose (`transientsolver.cpp:33-99`, `timeoperator.cpp:312,410`, `drivensolver.cpp:231-398`) are transcribed verbatim from the firm `fold_solve.md` chapter (an inherited-citation sub-case — the chapter is the authoritative home; the index prose re-states, does not re-derive). No bare claim without a pointer. Prose-only index touch, so no YAML `verified_against:` block to round-trip.

**surface-or-evidence — pass.** Not a refinement of an operator/theme's semantic surface — this is a prose-hygiene re-statement of an index Part-overview to register an already-firm chapter (`fold_solve` firmed cycle-058 D1). The "surface" being changed is the index narrative, and the evidence is the on-disk chapter `## Status` lines it is re-describing. No rotation_claim is asserted by the index page itself; the page reflects the firmness established in the chapters. Correct shape for a layer-intro-author cohort refresh.

**rotation-quality — pass (not the operative concern for this report-kind).** The index does not assert a new rotation; it re-states the existing batch-17 two-combinator MAP/FOLD framing (solve_family = independent MAP, fold_solve = state-threaded FOLD, both §3.7 `iterate_while` children, no third parent abstraction). That framing is faithfully reproduced from the firm chapters and the cycle-058 cycle-record (`two_combinator_factoring` field). The "a map is the degenerate fold whose step ignores the accumulator" gloss in edit 1's `[new]` is accurate and matches the chapter. No renaming-only smell — nothing new is being rotated here.

**variant-axis-coverage — pass.** The `fold_solve` schedule-source axis (fixed-list ⊂ state-generated greedy) is not silently dropped: edit 3's `[new]` carries it forward as an explicit open generalization with the OQ slug `fold-solve-greedy-schedule-source-generalization`, which resolves in `scaffolding/open-questions.md:808`. This matches the chapter's own §Variant-axes treatment (schedule-source declared THE load-bearing axis, state-generated form scoped to the OQ). No hidden branch.

**cross-reference-integrity — warning.** All live-links in the new prose resolve on disk EXCEPT `../L3/fold_solve.md` (edit 3 `[new]`), which does NOT exist yet — it is the cycle-059 D1 same-cycle co-land. The report flags this explicitly (§Open questions, and §Summary line 28) as valid only because D1 lands the file before finalize-rebuild. This is the standard same-cycle D1<->D2 forward-reference pattern (the cycle-058 cycle-record documents the identical D1<->D2 co-land resolving cleanly at the single finalize build). It is NOT a defect in the report's authoring — it is a genuine cross-cycle ordering dependency the report correctly surfaces and that the integrator's serial-per-report-then-finalize ordering handles by design. Marked `warning` (not `pass`) purely to surface the live dependency for the integrator: if D1's per-report apply is reordered AFTER finalize, `linkcheck2` breaks this link. All other targets verified present: `L4/{fold_solve,solve_family,iterate-while,chebyshev,ksp_solve,eigsolve}.md` and `L4-L3/fold-solve-time-step-dissolution.md`. The three `[old]` anchors each match the current index.md exactly (grep count = 1 each), so the edits apply cleanly with no stale-anchor risk.

**edge-label-fidelity — pass (not applicable).** No L_{n+1}->L_n edge label is carried by this index-prose report; the L4>L3 reference (`fold-solve-time-step-dissolution`) is a pointer to an existing firm theme, with the prose's "L3 image landed this cycle, status partial-obstruction" matching the cycle-record. No edge-label-vs-prose mismatch possible.

**plan-kind-consistency — pass.** Declared shape is a prose-only index cohort refresh (frontmatter `status: pending`, three `edit:` blocks, no `new:`). Content matches: stale prose loci at ~32/~40/~62 are re-stated; the already-firm dep-map TABLE row at line 82 is correctly NOT re-touched (verified: row 82 status cell = `firm`, authored cycle-058 — re-touching it would be redundant). The c057-meta count-owner guard is correctly honored — the firm count is registered from each linked chapter's `## Status` line, not from the drift-prone index cells, exactly as the dispatch plan (`priorities.md:80`) instructs. No mis-classification.

**skill-uptake-survey — warning.** The report's shape (count-owner discipline reading `## Status` from linked chapters, plus an on-disk live-link upgrade of a previously-plain-text/rough-in reference to `fold_solve`) implies two relevant procedures: the c057-meta count-owner guard (cited inline as "c057-meta count-owner guard" — acknowledged, though it is a codified guard, not a `skills/` SKILL.md), and `upgrade-plain-text-ref-to-live-link-when-target-on-disk` (the edit-3 transition of `fold_solve` from a bare-slug rough-in thread-opener to a live-linked firm reference is exactly that skill's pattern). Neither `skills/`-promoted skill is named by invocation. Non-blocking (pure telemetry) — the count-owner guard's intent is plainly followed regardless of the missing skill citation.

### Issues found

1. **`../L3/fold_solve.md` live-link is a same-cycle forward reference (cross-reference-integrity, edit 3 `[new]`, index.md ~line 62).** Severity: low / informational. The link target does not exist on disk at critique time; it is the cycle-059 D1 co-land. The report explicitly flags the dependency and the required apply-order (D1 before finalize-rebuild). Not an authoring defect — it is a live integrator-ordering dependency to honor. If for any reason D1 does not land this cycle, this link must fall back to plain-text (or a stub) per the `rough-in-forward-reference-must-be-plain-text-not-live-link` convention.

2. **Citation pinpoints `fold_solve.md:157` / `solve_family.md:144` target status-section prose, not the `## Status` heading line (citation-validity, §Summary line 32-34 + §Supporting evidence).** Severity: cosmetic. The `## Status` headings are at lines 155 and 142 respectively; the cited lines (157, 144) land a few lines into the status section on the status-value prose. The values claimed (`firm`, `rough-in (test-coverage-bounded)`) are correct and in-range, so this is not drift — just a pinpoint that names the value-prose rather than the heading. No correction strictly required; noted for precision.

3. **No `skills/` skill invocation named for the link-upgrade / count-owner pattern (skill-uptake-survey).** Severity: telemetry-only. `upgrade-plain-text-ref-to-live-link-when-target-on-disk` matches edit-3's promotion of the `fold_solve` reference; the count-owner guard is cited by name but as a meta-codified guard rather than a SKILL.md. Surfaced for uptake telemetry; the underlying disciplines are correctly followed.

## Repair

### Fixes attempted

- **Finding 1 (cross-reference-integrity, warning): `../L3/fold_solve.md` live-link in edit-block 3 `[new]` is a same-cycle forward reference to D1's co-landed file.**
  - **Decision**: not-needed (resolved-by-construction).
  - **Rationale**: This is the standard by-design D1↔D2 same-cycle forward-reference pattern — D1 authored `book/src/L3/fold_solve.md` this cycle and it applies before the finalize-rebuild, so `linkcheck2` resolves the link. The cycle-058 cycle-record documents the identical D1↔D2 co-land resolving cleanly at the single finalize build. NOT an authoring defect: the report itself surfaces the dependency (§Open questions line 76, §Summary line 28) and correctly states the required apply-order. Downgrading the live-link to plain-text would be WRONG here (per the integrator's "Integration may materialize implied components as stubs" / live-link-preferred policy, and because D1's file lands this cycle). No edit applied. Integrator-ordering note carried forward below.

- **Finding 2 (citation-validity, cosmetic): pinpoints `fold_solve.md:157` / `solve_family.md:144` land on the status-value prose a few lines below the `## Status` heading (headings at :155 / :142).**
  - **Decision**: not-needed (cosmetic, in-range).
  - **Rationale**: The cited line numbers land inside the status section on the status-value prose; the values claimed (`firm`, `rough-in (test-coverage-bounded)`) are correct and in-range. No drift — the pinpoint names the value being read rather than the heading, which is acceptable for a count-owner `## Status` read. Optional tightening only; not a repair-authority concern. No edit applied.

- **Finding 3 (skill-uptake-survey, warning): link-upgrade + count-owner-guard disciplines followed but not cited by promoted-skill invocation name.**
  - **Decision**: not-needed (telemetry-only).
  - **Rationale**: Pure uptake telemetry. The disciplines (`upgrade-plain-text-ref-to-live-link-when-target-on-disk`; the c057-meta count-owner guard) are correctly followed — edit-3 promotes the `fold_solve` bare-slug rough-in reference to a live-linked firm reference exactly per the skill's pattern, and the firm count is registered from each linked chapter's `## Status` line, not the index cells. Non-blocking; the missing invocation-name citation changes nothing about the report's correctness. No edit applied.

### Unrepairable findings

None. All findings are by-design / cosmetic-in-range / telemetry-only; none requires mechanical surgery, and none exceeds repair authority into substantive authoring.

## Suggested resolution

`overall_status: ready`. Notes for the integrator:

- **Integrator-ordering note (load-bearing):** apply D1 (`reports/<...>-l3-fold-solve` → `book/src/L3/fold_solve.md`) **before** D2's per-report apply, and in any case **before the finalize `cargo make book` rebuild**. The edit-3 `[new]` live-link `../L3/fold_solve.md` resolves only once D1's file is on disk. The report flags this explicitly; this is the standard same-cycle D1↔D2 co-land (cycle-058 precedent). If — and only if — D1 fails to land this cycle, the link must fall back to plain-text (or a stub) per `rough-in-forward-reference-must-be-plain-text-not-live-link`; that fallback is a finalize-build-repair contingency, not an action for this report.
- The three `[old]` anchors each match index.md exactly (grep count = 1 each per the critic); edits apply cleanly with no stale-anchor risk. The dep-map TABLE row at `index.md:82` is correctly NOT re-touched.
