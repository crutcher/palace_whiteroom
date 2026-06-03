---
verifies: ../CYCLE.md
critiqued_at: 2026-06-03T03:05:00Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-03T03:40:00Z
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
overall_status: ready
follow_up_agent: null
---

# META: verification of lifecycle-root feature column (the composition-root spine ROOT, first meta-feature)

## Critique

### Checks run

**citation-validity — warning.** Verified every L0 anchor against `palace/main.cpp`, `palace/drivers/basesolver.cpp`, and `palace/drivers/basesolver.hpp` via palace-codemap `read_range`. The **front half of `main` is exact**: `main` at `:158`; config-load `IoData iodata(argv[1], false)` at `:231` (verbatim); the driver-dispatch `switch (iodata.problem.type)` lambda at `:257`, `switch` at `:258`, and **all six `ProblemType` branches land exactly** — DRIVEN `:261`, EIGENMODE `:264`, ELECTROSTATIC `:267`, MAGNETOSTATIC `:270`, TRANSIENT `:273`, BOUNDARYMODE `:276`; mesh build `mesh::Load` `:287` / `Preprocess` `:288` / `Partition` `:290` / `RefineMesh` `:291` all confirmed. The `basesolver.cpp` AMR anchors are exact or within 1: initial `Solve(mesh)`+`Norml2` `:174-175` (verbatim), the AMR `while` `:190` (verbatim), mark/Dörfler `:221-232` (`// Mark.` at 220), refine `:235-244` (`// Refine.` at 236). `basesolver.hpp` seam confirmed: `class BaseSolver` `:31`, pure-virtual `Solve(...) const = 0` (declaration spans `:42-43`, the report cites `:43-44` — +1), `Preprocess` `:53-54`, `SolveEstimateMarkRefine` `:59`. **However, a consistent downward drift exists in the back half of both files** (see Issues): the `solver->SolveEstimateMarkRefine(mesh)` call is at **304**, not the cited `:306`; the timing/finalize block runs `:306-324`, not `:309-330`; `SaveMetadata` is `:314-316`, not `:319-321`; `ceed::Finalize()` is `:320`, not `:325`. In `basesolver.cpp` the re-solve `std::tie(indicators, ntdof) = Solve(mesh)` + `err = Norml2` is at **266-267**, not the cited `:271`/`:271-272`; the completion print runs `:268-275`, not `:273-275`. The enclosing frontmatter ranges (`main.cpp:158-330`, `basesolver.cpp:153-276`) still bound the real material, so the claims are not unsupported — but the load-bearing pinpoint anchors in the back half are off by +2 to +5 lines. Marked warning, not fail: the structure is faithfully read, only the trailing line numbers drifted.

**surface-or-evidence — pass (adapted check).** Per the FEATURE-SURFACE SPINE adaptation, the feature's surface IS the feature, evidenced by the L0 driver-source range plus constituent down-links. For this ROOT the constituents correctly include both (a) driver-agnostic vocabulary (`fold_solve` firm, `fe_assemble`/`ksp_solve` firm) and (b) the per-driver feature columns it composes (`electrostatic.*` on disk, `magnetostatic.*` D1-this-cycle). The compositional claim `lifecycle = fold_solve (dispatch (problem_type cfg)) ∘ build_mesh` is evidenced by the `main.cpp` switch + `SolveEstimateMarkRefine` source range and the down-links. This is a legitimate feature-surface evidence shape, not a bare rotation_claim. Pass.

**rotation-quality — pass (no-op).** Correctly no-ops: a composition-root feature chapter asserts no L_{n+1}→L_n algebraic/reduction rotation; it carries only the compositional claim. The report explicitly scopes this out ("Rotation / variant-axis claims no-op"). Not applicable to the composition-root feature-surface kind. The one structural characterization that COULD be a rotation-shaped overclaim — "the AMR loop IS `fold_solve` state-generated" — I verified separately and it holds (see below); it is a faithful constituent identification, not a manufactured rotation.

**variant-axis-coverage — pass (no-op).** Correctly no-ops on a composition-root: there is no variant-axis catalogue at this chapter (the variant axes live in the constituent `fold_solve` entry, which the report references). The six `ProblemType` branches are dispatch specializations, not hidden variant branches of a single operator — the report enumerates all six (including BOUNDARYMODE) explicitly and routes the three un-authored ones to plain text. No hidden branches. Pass.

**cross-reference-integrity — warning.** Relative link resolution from `feature/lifecycle.L4.md`: `../L4/fold_solve.md`, `../L4/solve_family.md`, `./electrostatic.{L4,L1,L0}.md` all RESOLVE on disk. The named constituent slugs exist and are firm where claimed: `fold_solve.md` (`## Status: firm`), `fe_assemble.md` (`firm`), `ksp_solve.md` (`firm`) — the report's firmness assertions are accurate. The plain-text discipline for eigenmode/driven/transient is **correct** (verified: they appear only as plain text + `*(forthcoming — not yet authored)*`, never as `[...](...)` — a live link to those missing files would be a hard `linkcheck2` error). The warning is the **`magnetostatic.{L0,L1,L4}.md` live links, which are MISSING on disk this moment** — they are D1's same-cycle slug. Per the FEATURE-SURFACE SPINE directive note, D1 lands them before integrator-finalize's build, so this is a same-cycle ordering dependency rather than a defect in THIS report; flagged so the integrator sequences D1 before finalize (if D1's magnetostatic files do not land, these six links become dead-link build breakage).

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried (composition-root, not a lowering theme). The L1↔L4 "same meta-feature, differ in vocabulary" framing (L1 ch §"L1 vs L4") discusses exactly the L1 and L4 lifecycle forms it names; the down-direction note correctly defers L1→L0 to the constituent ops' mutation-rotation themes (high→low discipline honored). No mismatched edge. Pass.

**plan-kind-consistency — pass.** Declared `kind: feature-surface`, `status: seed (composition-root)`. Content shape matches: three composition-root chapters carrying only the compositional claim, with constituents linked rather than re-derived. The distinct status string `seed (composition-root)` vs the per-driver `seed (exemplar)` is a deliberate sub-kind marker the report flags for batch-22 codification — appropriate self-classification, not a mis-tag. Pass.

**skill-uptake-survey — pass.** The report references palace-codemap `read_range` for L0 confirmation (the appropriate localization path) and on-disk `## Status` reads for constituent firmness (not stale index/cycle-record cells) — good practice. No feature-surface-specific skill exists yet (the kind is pre-codification), so there is no skill to cite-invoke; the citation-confirmation procedure used is sound. Pure telemetry surface, non-blocking. Pass.

### Key adjudications requested

**Does the `fold_solve`-as-AMR-loop characterization hold up? YES — faithful, not a stretch.** I read `book/src/L4/fold_solve.md`: its `schedule-source` variant axis (lines 12, 150) defines `state-generated` as "the carry GENERATES the next input + the loop bound from accumulated state, a greedy/error-terminated march," with driven-PROM SweepAdaptive as the witness. The AMR `while` in `SolveEstimateMarkRefine` (`basesolver.cpp:190`, `while (use_amr && !ExhaustedResources(it, ntdof) && err >= refinement.tol)`) is a textbook instance: the carry `{mesh, indicators, ntdof, err, it}` generates the next iterate (mark `:220-233` → refine `:236-245` → rebalance → re-solve `:266`) AND the termination bound (`!ExhaustedResources && err >= tol`) from accumulated state. Each iterate's input is the prior iterate's output; the iterates do not commute. This is exactly `fold_solve`'s state-generated form — NOT the fixed-list transient form, and NOT a `solve_family` map. The report's claim that this is a **second, driver-agnostic state-generated-fold witness** (strengthening the axis from 1 to 2) is correct and is a genuine finding for the `fold-solve-greedy-schedule-source-generalization` OQ. The report correctly did NOT edit `fold_solve.md` (out of one-chapter scope) and routed the witness as an OQ for a future `fold_solve` lifter.

**Meta-feature novelty — confirmed as a codification finding, not a defect.** This is genuinely the first feature chapter whose stage-(2) constituents are OTHER feature columns (per-driver specializations) rather than vocabulary ops. The adapted surface-or-evidence check extends cleanly (constituents = feature columns + the driver-agnostic firm fold). The report's flag for batch-22 (name the ROOT/meta-feature sub-kind vs the per-driver leaf sub-kind; nest the ROOT above the columns in the Feature Part SUMMARY ordering) is correctly routed to D1 (index owner) + meta-phase. Not a defect.

**BoundaryModeSolver 6th branch — confirmed real.** `case ProblemType::BOUNDARYMODE: return std::make_unique<BoundaryModeSolver>(...)` is verbatim at `main.cpp:276`. The report's observation that this is a 6th `ProblemType` branch beyond the "5 sim drivers" framing is accurate and correctly routed (the FEATURE-SURFACE SPINE directive's "5 drivers + boundary-mode" split is reconciled by this). Correctly-routed finding.

### Issues found

1. **Back-half line-number drift in `palace/main.cpp` citations** (`lifecycle.L0.md` §"The lifecycle, in source" stage 5–6, §Status, and the report Summary / Supporting-evidence; `lifecycle.L1.md` + `lifecycle.L4.md` I/O sections). Severity: low-moderate (warning). Confirmed actual lines: `solver->SolveEstimateMarkRefine(mesh)` is at **304** (cited `:306`); timing summary comment at **306** (cited `:309`); `SaveMetadata(...)` at **314-316** (cited `:319-321`); `ceed::Finalize()` at **320** (cited `:325`); the finalize block ends ~`:324` (frontmatter/prose cite `:330`). The front-half anchors (`:231`, `:257-280`, the 6 branch lines, `:287-302`) are exact, so the drift is isolated to the post-`SolveEstimateMarkRefine` tail. Repair: shift the back-half `main.cpp` pinpoints down by ~2 (call site) to ~5 (SaveMetadata/Finalize) lines; the enclosing `main.cpp:158-330` frontmatter range still bounds the material but its upper bound overshoots the true `main` end (~`:324`).

2. **Back-half line-number drift in `palace/drivers/basesolver.cpp` citations** (`lifecycle.L0.md` stage 5 bullet "re-solve + estimate"; `lifecycle.L1.md`/`lifecycle.L4.md` stage-3 L0 tail; report Summary). Severity: low (warning). The re-solve `std::tie(indicators, ntdof) = Solve(mesh)` + `err = indicators.Norml2(comm)` is at **266-267** (cited `:271`/`:271-272`); the completion print runs **268-275** (cited `:273-275`). The earlier anchors in the same range (initial solve `:174-175`, `while` `:190`, mark `:221-232`, refine `:235-244`) are exact. Repair: shift the re-solve pinpoint from `:271` to `:266`.

3. **`magnetostatic.{L0,L1,L4}.md` live links currently dead on disk** (`lifecycle.{L0,L1,L4}.md` prose + down-link tables, six links). Severity: conditional (warning). These are D1's same-cycle canonical slug; per the FEATURE-SURFACE SPINE directive D1 lands them before the finalize build, so they are a same-cycle ORDERING dependency, not an authoring defect in this report. Not for repair here — flagged for the integrator to sequence D1's magnetostatic column ahead of `integrator-finalize`'s `cargo make book`. If D1 slips, these become hard `linkcheck2` breakage.

4. **(Non-blocking, observational) `basesolver.hpp` pure-virtual `Solve` cited `:43-44`, declaration spans `:42-43`.** Severity: trivial. The `= 0` is on `:43`; the report's `:43-44` is +1 past the declaration. The seam is correctly identified; cosmetic.

### Notes for downstream

- The `fold_solve` state-generated 2nd-witness finding (OQ `fold-solve-greedy-schedule-source-generalization` now has 2 witnesses) and the `seed (composition-root)` vs `seed (exemplar)` status-string question are correctly left as OQ/meta-phase routing — the report did not over-reach into editing `fold_solve.md` or the status vocabulary. No surface-authoring defect there.
- Index/SUMMARY deferral to D1 is correct and expected; absence of `feature/index.md` edits in this report is by design (D1 owns them), not a coverage gap.

---

## Repair

### Fixes attempted

- **Finding**: Back-half line-number drift in `palace/main.cpp` citations (call site, SaveMetadata, ceed/slepc Finalize) — post-`SolveEstimateMarkRefine` pinpoints drift +2 to +5 lines.
  - **Decision**: repaired
  - **Action**: Re-confirmed each via palace-codemap `read_range` (`main.cpp:300-330`, re-read with `start_line=302` to pin exact lines), then corrected every drifted `main.cpp` pinpoint in CYCLE.md across the L0 stage-5/6 prose, L0 I/O section, L4 I/O section, the Summary L0-anchors list, and the Supporting-evidence block:
    - `solver->SolveEstimateMarkRefine(mesh)` call: `:306` → **`:304`** (verbatim `solver->SolveEstimateMarkRefine(mesh);` at 304, confirming the critic's pinpoint).
    - `SaveMetadata` block: `:319-321` → **`:314-316`** (`SaveMetadata(BlockTimer::GlobalTimer())` 314, `peak_mem` 315, `peak_node_mem` 316).
    - `ceed::Finalize()`: `:325` → **`:320`** (verbatim at 320).
    - timing/finalize block range: `:309-330`/`:309-318` → **`:306-324`** / `:306-313` (timing-summary comment at 306; block ends at the slepc tear-down, `main` closes at `:328`).
    - `slepc::Finalize()`: secondarily corrected `:328` → `:323` → **`:324`** (read 319-330 confirmed `slepc::Finalize();` at 324, the `#if` at 323).
- **Finding**: Back-half line-number drift in `palace/drivers/basesolver.cpp` re-solve + completion-print pinpoints.
  - **Decision**: repaired
  - **Action**: Re-confirmed via `read_range` (`basesolver.cpp:262-276`, re-read `264-276`). Corrected in CYCLE.md across the L0 stage-5 bullet, the L1 stage-3 L0 tail, the L4 stage-3 L0 tail, the Summary L0-anchors list, and the Supporting-evidence block:
    - re-solve `std::tie(indicators, ntdof) = Solve(mesh)` + `err = Norml2(...)`: `:271`/`:271-272` → **`:266-267`** (`std::tie(...) = Solve(mesh);` at 266, `err = indicators.Norml2(comm);` at 267).
    - completion print: `:273-275` → **`:269-275`** (the `Mpi::Print("\nCompleted ...")` begins at 269, the AMR `while` body closes at 268).
  - **Note**: The enclosing frontmatter macro-ranges (`main.cpp:158-330`, `basesolver.cpp:153-276`) were confirmed correct and left untouched — only the sub-anchors drifted, exactly as the critic scoped. Front-half anchors (`:231`, `:257-280`, the 6 branch lines, `:287-302`, `:174-175`, `:190`, `:221-232`, `:235-244`) were verified-exact by the critic and not re-touched.

- **Finding**: `magnetostatic.{L0,L1,L4}.md` live links currently dead on disk (six links).
  - **Decision**: not-needed
  - **Rationale**: These are D1's same-cycle canonical slug. D1 authors the magnetostatic column this cycle and the plan sequences D1 before `integrator-finalize`'s `cargo make book`, so the links resolve at build time. This is a same-cycle apply-ordering dependency, not an authoring defect in this report — no repair edit warranted. **Integrator note carried below.**

- **Finding (observational, non-blocking)**: `basesolver.hpp` pure-virtual `Solve` cited `:43-44`, declaration spans `:42-43` (+1, the `= 0` on `:43`).
  - **Decision**: not-needed (critic marked trivial/cosmetic, not a warning-driving defect). The seam is correctly identified; left as-is to stay within mechanical-and-surgical scope (the critic did not flag this in `checks:`).

### Unrepairable findings

None. The two warning-level checks both resolve: citation-validity drifts are mechanically repaired; the cross-reference-integrity warning is a same-cycle ordering dependency (not-needed), not an authoring defect.

The correctly-routed meta-phase items — the `fold_solve` state-generated 2nd-witness, the `seed (composition-root)` vs `seed (exemplar)` status-string sub-kind question, the meta-feature novelty codification, and the `BoundaryModeSolver` 6th-branch reconciliation — are left in the report's Open-questions block for batch-22 meta-phase / D1, as the critic routed them. They require substantive methodology/codification decisions outside repair authority and are NOT defects in this report.

## Suggested resolution

`ready`. The back-half citation drift is fully repaired against codemap-confirmed lines; all other checks pass or no-op.

**Integrator note**: sequence D1 (magnetostatic column author) **before** `integrator-finalize`'s `cargo make book` so the six `feature/magnetostatic.{L4,L1,L0}.md` live links resolve. The plan already sequences D1 ahead of finalize; this is a reminder, not a new constraint. If D1's magnetostatic files slip, the six links become hard `linkcheck2` breakage. The OQ-routed meta-feature sub-kind + `fold_solve` 2nd-witness findings are for batch-22 meta-phase, not this integration.
