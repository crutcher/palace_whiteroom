---
verifies: ../REPORT.md
critiqued_at: 2026-06-02T231500Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: warning
  skill-uptake-survey: pass
repaired_at: 2026-06-02T233000Z
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

# META: verification of "Formalize frequency_sweep at L4" (cycle-070 D1)

## Critique

### Checks run

**citation-validity — pass.** `python3 tools/citecheck/citecheck.py --scan CYCLE.md --quiet` returned `27 ok, 0 failing (27 citations checked)`. I then read the load-bearing L0 anchors directly via `palace-codemap read_range` against `reference/palace/palace/drivers/drivensolver.cpp`. Every pinpoint lands: `:80` = `omega_sample = iodata.solver.driven.sample_f`; `:91`/`:92`/`:93` = `GetStiffnessMatrix`/`GetDampingMatrix`/`GetMassMatrix` (the once-assembled `{K,C,M}` basis); `:168-170` = the `for (std::size_t omega_i = …; omega_i < omega_sample.size(); omega_i++)` statement (comment `// Frequency loop.` at 167, `for` keyword at 168, condition at 170 — the range captures the for-statement correctly); `:172` = `omega = omega_sample[omega_i]`; `:175` = `A2 = GetExtraSystemMatrix(...)`; `:176` = `A = GetSystemMatrix(1.0+0.0i, 1i*omega, -omega*omega+0.0i, K,C,M,A2)`; `:180` = `ksp.SetOperators(*A, *P)`; `:194` = `GetExcitationVector(excitation_idx, omega, RHS)`; `:196` = `ksp.Mult(RHS, E)`. The firm-vocabulary endpoint citations resolve in-range (`assemble_frequency_operator.md` is firm, 481 lines so `:17-31`/`:264-283` are in bounds; `solve_family.md:65,90,137,146,163`; `ksp_solve.md:36-40`). No `verified_against:` YAML block is present, so the round-trip sub-check no-ops.

**The load-bearing non-law verified.** The operator-VARYING claim ("SetOperators INSIDE the loop", no hoist) is exactly what the source shows: `GetSystemMatrix(...)` (`:176`) and `ksp.SetOperators(*A, *P)` (`:180`) both sit inside the `for (omega_i)` body that opens at 167-170; the `{K,C,M}` basis at `:91-93` is the only thing hoisted outside. The citations genuinely support "SetOperators inside the loop" and the negation of `solve_family`'s hoist law.

**surface-or-evidence — pass.** This is a new-operator firm authoring (new file `book/src/L4/frequency_sweep.md`), not a refinement of an existing operator/theme — the surface/evidence dichotomy for refinement-shaped proposals does not bind. The entry authors fresh L4 surface AND grounds it in positive L0 evidence (the single driven loop) + firm-vocabulary endpoints. Applicable shape satisfied.

**rotation-quality — pass.** The entry is an L4 vocabulary operator, not itself a lowering; the rotation it *records in-line* (deferring the theme to D2) is the L4→L3 `map`-collapse-to-explicit-for-loop, asserted **substantive** (not identity-in-form): the typed `map` combinator + typed `operator-capture = per-element` axis collapse to a positional `for` loop with `GetSystemMatrix`/`SetOperators` placed inside the body by hand. That is a genuine compaction (typed map-combinator → hand-written accumulating loop), not a rename. The L4 form is strictly more abstract than the L3 image it lowers to. Pass.

**variant-axis-coverage — pass.** Four axes declared and each dispositioned: `operator-capture` (`per-element`, the load-bearing axis, explicitly claimed and contrasted against `solve_family`'s `fixed`); `operand-source` (`affine-in-ω rebuild`, absorbed into the named `assemble_frequency_operator` verb); `element-type` (`complex`, pinned with rationale — the `{iω,−ω²}` weights + `ComplexOperator` basis); `family-index-domain` (`frequency`, absorbed into `[Scalar]`). No hidden branch: the adaptive driven sweep (`SweepAdaptive`, `:231`) is explicitly scoped OUT (it is `fold_solve`'s state-generated fold, not a `frequency_sweep` member), and the single-witness-driven scope is argued as permanent-by-design across all 5 pipelines. Coverage is explicit.

**cross-reference-integrity — warning.** All `[link]` references resolve on disk: the 9 L4 chapters (`assemble_frequency_operator`, `ksp_solve`, `iterate-while`, `solve_family`, `fold_solve`, `chebyshev`, `krylov-step`, `eigsolve`, `linear_combination`), the 4 concept pages (`state-stratification`, `solve-monad`, `derived-view-hoisting`, `variant-absorption`), `L3/ksp_solve.md`, and `design/l4_calculus.md` all exist. The forward-referenced `../L4-L3/frequency-sweep-dissolution.md` does NOT yet exist on disk, but it is authored by cycle-070 D2 this same cycle (`reports/2026-06-02T223001Z-abstractor-frequency-sweep-dissolution-L4-L3/CYCLE.md`) under the **identical canonical slug** `frequency-sweep-dissolution` — cross-report-forward-reference consistency CONFIRMED (D1's `lowers_to`/`## Lowers to` live-link and D2's authored slug match; the planner-stated slug is honored, not invented). The report itself flags the file-ordering race and the stub-materialization fallback. The fence-parity build-readiness guard PASSES: `grep -n '^```'` shows 10 fences (5 balanced pairs); the main `edit:book/src/L4/frequency_sweep.md` fence (lines 38–666) ENCLOSES the full firm apparatus — `# frequency_sweep` (57), `## Signature` (133), `## Algebraic laws` (291), `## Status` (524), `## Evidence` (598) all inside the fence. No firm-body-outside-fence defect. The shared parent guard PASSES: D1 did NOT author a shared `map_solve` parent — it is explicitly framed as the driven feature's OWN single-witness form (batch-21 meta decision 4 honored throughout). **The warning is the index.md tally classification** (see Issue 1) plus a minor SUMMARY alpha-insert note (see Issue 2).

**edge-label-fidelity — pass.** The entry carries the `lowers_to`/`## Lowers to` edge to `frequency-sweep-dissolution` labeled L4>L3; the prose discusses exactly that edge (the L4 `map` collapsing to the L3 explicit per-ω for-loop with rebuild+SetOperators inside). No edge-label/prose mismatch. The contrast-sibling references to `solve_family` and `fold_solve` are correctly framed as same-layer (L4) siblings, not lowering edges.

**plan-kind-consistency — warning.** The declared kind is firm L4 operator, and the content shape matches: full Signature + Semantics + Algebraic-laws (with explicit non-laws) + Status + Evidence, no rough-in placeholders, the firm-on-positive-structure escape argued explicitly and correctly (syntactic-identity map laws on a positive loop + firm endpoints, NOT test-gated convergence semantics — the `eigsolve` distinction is correctly invoked). The firmness claim is well-supported. The warning is a **tally-classification** mismatch adjacent to plan-kind: the entry is self-described as an "outer-driver combinator" (matching the cohort `ksp_solve`/`eigsolve`/`fold_solve`/`solve_family`), yet the SOLE-OWNER tally fragment bumps the **base** `Firm at L4 (13 + 4 outer-driver)` → `(14 + 4 outer-driver)` rather than the outer-driver sub-tally → `(13 + 5 outer-driver)`. By the existing taxonomy a firm outer-driver combinator belongs in the `+N outer-driver` bucket. See Issue 1.

**skill-uptake-survey — pass.** The report's shape (L0 citation verification on a single driver loop) implies `verify-citation-range` / the `tools/citecheck` mechanical path; the report explicitly documents invoking `tools/citecheck/citecheck.py --anchor` + `palace-codemap read_range` against on-disk source ("All returned `[ok]`"). The firmness-tier reasoning implies the `partly-constructive` / `rough-in (test-coverage-bounded)` invariants, which are cited. Telemetry present; no gap.

### Issues found

1. **L4/index.md tally-bucket classification (cross-reference-integrity / plan-kind-consistency, medium severity).** `CYCLE.md` §"Tally edit fragments" + §"Index ownership" instruct the integrator to bump the firm header `**Firm at L4 (13 + 4 outer-driver)**` → `**Firm at L4 (14 + 4 outer-driver)**` (book/src/L4/index.md line 32). But `frequency_sweep` is, by the entry's own one-line ("the driven per-ω frequency-sweep **outer-driver combinator**") and by cohort placement (sibling of `ksp_solve`/`eigsolve`/`fold_solve`/`solve_family`), an **outer-driver** combinator — the `+4 outer-driver` sub-tally is where it belongs, so the coherent bump is `(13 + 5 outer-driver)`, not `(14 + 4 outer-driver)`. (Caveat for the repairer/integrator to adjudicate: confirm whether the existing `+4 outer-driver` enumerates `ksp_solve`+`eigsolve`+`fold_solve`+`solve_family`; if `solve_family` is excluded because it is `rough-in`, the firm outer-driver count may differ — but `frequency_sweep` is firm AND an outer-driver, so it lands in the outer-driver bucket regardless of which base it should increment.) As written, the bump under-counts the outer-driver cohort and over-counts the non-outer-driver firm base. Location: `CYCLE.md:705-707` (header fragment) and `CYCLE.md:698`.

2. **SUMMARY.md alpha-insert is only locally coherent (cross-reference-integrity, low severity).** The `edit:book/src/SUMMARY.md` block (`CYCLE.md:672-675`) anchors on `- [fold_solve](./L4/fold_solve.md)` and inserts `- [frequency_sweep](./L4/frequency_sweep.md)` after it. `fold_solve` < `frequency_sweep` < `solve_family` alphabetically, so the insert is alpha-correct *relative to fold_solve*. But the existing SUMMARY L4 list is NOT alpha-sorted: `solve_family` is at line 21, BEFORE `fold_solve` at line 22. So the resulting list (`solve_family`, `fold_solve`, `frequency_sweep`) is still not globally alphabetical, and `frequency_sweep` lands after `solve_family` rather than before it. The 2-line context block matches existing adjacent lines so the edit will APPLY cleanly (no build break) — this is a directive-3 alpha-ordering coherence note, not a fence/build defect. The pre-existing `solve_family`/`fold_solve` mis-order is not D1's to fix, but D1's "alpha-insert" claim (`CYCLE.md:697`) overstates the result. Location: `CYCLE.md:672-675`.

3. **Forward-reference live-link to a not-yet-on-disk file (cross-reference-integrity, low/informational — already self-flagged).** `lowers_to:` frontmatter and `## Lowers to` prose live-link `../L4-L3/frequency-sweep-dissolution.md`, which does not exist on disk until cycle-070 D2's apply lands. Slug consistency with D2 is confirmed (both use `frequency-sweep-dissolution`), so this is purely an apply-ordering concern, not a wrong reference. The report self-flags it (§Open questions) and names the stub-materialization fallback per the "Integration may materialize implied components as stubs" invariant. Recorded for the integrator's apply-ordering awareness (order D2 with/before D1's finalize, or stub on dead-link). Location: `CYCLE.md:48-49`, `CYCLE.md:476-477`, `CYCLE.md:720`.

## Repair

### Fixes attempted

- **Finding 1 — L4/index.md tally-bucket classification** (critic: bump should be `(13 + 5 outer-driver)`, not `(14 + 4 outer-driver)`).
  - **Decision**: not-needed (the original CYCLE.md bump is correct; the critic's proposed fix would corrupt the count).
  - **Verification**: read the on-disk `book/src/L4/index.md` §"Vocabulary cohort". The header taxonomy is `Firm at L4 (13 + 4 outer-driver)` where:
    - the base **`13`** = the 13 genuinely-**firm operator CHAPTERS** in the cohort bullet list (lines 34–47 enumerate 14 bullets; `solve_family` at line 46 is `rough-in (test-coverage-bounded)` per the "Rough-in at L4 (1)" section line 57, so firm chapters = 14 − 1 = **13**). This base already INCLUDES the firm outer-driver *combinators* `ksp_solve`/`eigsolve`/`fold_solve` (they each carry a firm cohort bullet).
    - the **`+4 outer-driver`** = the **4 `solve-monad` outer-driver VOCABULARY ANCHORS** — the section explicitly labeled `**`solve-monad` outer-driver vocabulary (4)**` at line 49 (`solve_loop` / `restart_cycle` / `Outcome` / `EigOutcome`; table rows at lines 87+). These are non-chapter vocabulary anchors, NOT operator chapters.
  - The critic's premise — that `+4 outer-driver` enumerates `ksp_solve`+`eigsolve`+`fold_solve`+`solve_family` — is incorrect: those firm outer-driver combinators live in the base `13`, and the `+4` is the `solve-monad` vocabulary-anchor sub-tally. `frequency_sweep` is a firm operator **chapter** (own `.md` + own cohort bullet), NOT a `solve-monad` vocabulary anchor, so it correctly increments the base `13 → 14` and leaves `+4 outer-driver` unchanged. Applying the critic's `(13 + 5 outer-driver)` would (a) wrongly inflate the vocabulary-anchor count to 5 with no 5th anchor, and (b) drop the firm-chapter count by one. **No edit applied; original CYCLE.md fragment `(14 + 4 outer-driver)` is the correct bump.**

- **Finding 2 — SUMMARY.md alpha-insert only locally coherent.**
  - **Decision**: not-needed (transitional-state-acceptable; local placement is sane and the edit applies cleanly).
  - **Verification**: read the on-disk `book/src/SUMMARY.md` L4 list (lines 8–22). The list is currently **chronological by landing order, NOT alphabetical** (`assemble_frequency_operator`, `krylov-step`, …, `solve_family` (21), `fold_solve` (22)). The directive-3 global alpha re-sort is a deferred dedicated wave; the alpha-LOCAL convention is "alpha within the kind grouping as it currently stands". The CYCLE.md insert anchors on `fold_solve` (the current list tail, line 22) and appends `frequency_sweep` after it — i.e. at the chronological tail, where the newest landing belongs in the pre-reorg chronological state. This is sane: `frequency_sweep` is cycle-070's landing and sits after cycle-069's `fold_solve`/`solve_family` cohort. The 2-line context anchor (`- [fold_solve](./L4/fold_solve.md)` + the new line) matches the on-disk tail, so the edit APPLIES cleanly with no build break. The pre-existing `solve_family`-before-`fold_solve` non-alpha ordering is not this report's to fix (out of scope; the global re-sort wave owns it). No mis-placement to repair.

- **Finding 3 — forward-link to not-yet-on-disk `frequency-sweep-dissolution.md`.**
  - **Decision**: not-needed (apply-ordering only; no content fix).
  - **Rationale**: the slug `frequency-sweep-dissolution` is consistent with cycle-070 D2's authored slug (critic confirmed). The live-link is momentarily dangling only if D2's per-report apply lands after D1's; resolved at integration by ordering D2 with/before D1's finalize, or by the stub-materialization fallback ("Integration may materialize implied components as stubs"). Already self-flagged in CYCLE.md §Open questions. Recorded for the integrator's apply-ordering awareness; no repairer edit warranted.

### Unrepairable findings

None. All three critic findings resolve to not-needed on verification against the on-disk artifact:
- Finding 1 — the original bump is correct; the proposed fix would corrupt the tally (verified against on-disk `L4/index.md` taxonomy).
- Finding 2 — transitional chronological-state placement is sane; pre-existing non-alpha order is out of scope.
- Finding 3 — apply-ordering concern, deferred to the integrator (stub-materialization fallback available); already self-flagged.

## Suggested resolution

`overall_status: ready`. No repairer edits to CYCLE.md were required.

Two integrator-awareness notes (NOT blockers):
1. **Apply finding-1's tally fragment AS WRITTEN** (`Firm at L4 (13 + 4 outer-driver)` → `(14 + 4 outer-driver)`, `book/src/L4/index.md` line 32). The critic's suggested `(13 + 5 outer-driver)` is INCORRECT and must NOT be applied — `frequency_sweep` is a firm operator chapter incrementing the base `13`, not a 5th `solve-monad` vocabulary anchor.
2. **Order cycle-070 D2 (frequency-sweep-dissolution) with/before D1's finalize**, or stub the `../L4-L3/frequency-sweep-dissolution.md` target on a dead-link at finalize-time build-repair, so the `lowers_to` live-link resolves.
