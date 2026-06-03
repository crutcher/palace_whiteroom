---
agent: layer-intro-author
invoked_at: 2026-06-03T030410Z
scope: transient simulation feature-surface column (book/src/feature/transient.{L4,L1,L0}.md)
status: pending
integrated_at: 2026-06-03T214500Z
integration_commit: 03d43ae
integration_notes: "cycle-073 D3. Applied clean — new feature/transient.{L4,L1,L0}.md (status seed); the FOLD-pipeline second-order-in-time wave system, single fe_assemble down-link stands for a thrice-applied K/C/M assemble-fold. index/SUMMARY rows deferred-to-D2 (cohort owner, resolved same-cycle). Build exit 0, linkcheck2 clean."
---

# CYCLE: transient feature-surface column (leaf driver, FOLD-pipeline)

## Summary

Authors the **transient simulation feature-surface column** — three composition-root chapters `book/src/feature/transient.{L4,L1,L0}.md` — under the FEATURE-SURFACE SPINE directive (cycle-073, D3). This is a **leaf feature column** (per-driver sub-kind), uniform `status: seed`.

The transient column is the spine's **first fold-pipeline witness** — the structural complement to the existing electrostatic/magnetostatic *map*-pipeline columns. Where those compose [`solve_family`](../L4/solve_family.md) (an independent map over an RHS family), transient composes [`fold_solve`](../L4/fold_solve.md) (a state-threaded fold where each step's input is the prior step's output). Transient is in fact `fold_solve`'s **default / primary witness** (`book/src/L4/fold_solve.md:113`), so the column composes firm vocabulary end-to-end:

- **L4 body** = `fold_solve` (firm c058) ∘ `fe_assemble` (firm; three operators K/C/M). Output = time-domain field-state trajectory.
- **L1 body** = the pure-function form: `fe_assemble` (firm) + a pure `scanl_state` state-threaded fold over a mutation-lifted per-step advance (the fold combinator's home is L4/L3; no separate L1 fold entry — recorded inline).
- **L0** = the cited driver source `transientsolver.cpp:24-116` (`TransientSolver::Solve`) + `timeoperator.cpp` (K/C/M assembly `:65-67`, ODE op/integrator construction once `:311-373`, the opaque ODE step `:407-413`).

The per-step body bottoms out in the opaque MFEM `ODESolver::Step` (internally an implicit linear solve) — the column quantifies over it (no per-step `ksp_solve` cap, unlike the fixed-operator map drivers); the opacity is recorded at the lowering layer (`obstruction (opaque-library-ownership)`), not in this column.

Chapter bodies are staged as sibling files in this report dir (`transient.L4.md`, `transient.L1.md`, `transient.L0.md`) to avoid nested-fence truncation; the integrator copies them verbatim to `book/src/feature/`.

## Ownership / deferral notes

- **I author ONLY the 3 chapter files** `book/src/feature/transient.{L4,L1,L0}.md`.
- **DEFERRED to D2** (the layer-intro-author on the driven column, SOLE index/SUMMARY owner for the driver-column cohort this cycle): my `book/src/feature/index.md` matrix row + my `# Feature surfaces — entry points` `book/src/SUMMARY.md` rows. I emit NO index.md or SUMMARY.md edits. D2 must add a `transient` row to the feature × level matrix (`feature/index.md` table, after the `lifecycle` row or in the planned-drivers position per D2's chosen ordering — within-column level order high→low, the deliberate non-alpha exception) and the three `transient.{L4,L1,L0}` SUMMARY entries under the Feature Part. The three transient files link sibling driver columns by canonical relative slug; `driven` / `eigenmode` are forward-referenced via canonical slug (electrostatic/magnetostatic/lifecycle already on disk as live links).

## Proposed changes

Three new-file creations. Each file's verbatim body is the identically-named staged sibling in this report directory — integrator: copy verbatim.

```edit:book/src/feature/transient.L4.md
[new file — copy verbatim from reports/2026-06-03T030410Z-layer-intro-author-transient-feature/transient.L4.md]
```

```edit:book/src/feature/transient.L1.md
[new file — copy verbatim from reports/2026-06-03T030410Z-layer-intro-author-transient-feature/transient.L1.md]
```

```edit:book/src/feature/transient.L0.md
[new file — copy verbatim from reports/2026-06-03T030410Z-layer-intro-author-transient-feature/transient.L0.md]
```

SUMMARY.md wiring for these three files is DEFERRED to D2 (see ownership note). If D2 does not land this cycle, integrator-finalize should wire the three transient chapters into the `# Feature surfaces — entry points` Part itself (high→low within column) to keep the files reachable.

## Supporting evidence

Constituent chapters composed (all firm, surveyed from on-disk `## Status` / frontmatter `firmness:` this dispatch — NOT from index cells):

- `book/src/L4/fold_solve.md` — `firmness: firm` (frontmatter line 4; `## Status: firm` body). Transient is its **default / primary fold witness** (named `book/src/L4/fold_solve.md:113`; the fixed-list schedule surface). Citations for transient already carried in that entry's §Specializations / §Evidence (`transientsolver.cpp:33,35,36,77,89,93,98,99`; `timeoperator.cpp:312,410`).
- `book/src/L4/fe_assemble.md` — `firmness: firm`. The assemble-fold combinator; transient assembles three operators (K/C/M).
- `book/src/L1/fe_assemble.md` — `## Status: firm` (line 200).
- `book/src/L1/ksp_solve.md` — `## Status: firm` (NOT composed by transient — noted as the contrast: transient has no per-step ksp_solve cap; the implicit solve is inside the opaque ODE step).
- `book/src/L3/fold_solve.md` — exists (`partial-obstruction`); referenced from the L1 chapter's fold-home note.

L0 source ranges — all self-verified on-disk via palace-codemap `read_range` this dispatch (close-brace discipline applied on END lines), and run through `tools/citecheck/citecheck.py --scan` (L4: 15 ok / 0 failing; L1: 8 ok / 0 failing; L0: 10 ok / 0 failing):

- `palace/drivers/transientsolver.cpp:25-27` — `TransientSolver::Solve` signature (return type `:25`, name+params `:26`, opening `{` `:27`; line 24 is blank); method spans `:24-116` (closing `}` read at `:116`).
- `transientsolver.cpp:30-31` — `GetTimeExcitation(false)` / `(true)` (J(t), dJ/dt); def `:118`.
- `transientsolver.cpp:32` — `SpaceOperator space_op(iodata, mesh)`; `:33` — `TimeOperator time_op(...)` (built once).
- `transientsolver.cpp:35` — `delta_t = iodata.solver.transient.delta_t`; `:36` — `n_step = config::GetNumSteps(...)` (fixed schedule).
- `transientsolver.cpp:77` — `for (int step = 0; step < n_step; step++)` (the fold loop; spans `:77-109`); `:89` — `time_op.Init()` (seed s0); `:93` — `time_op.Step(t, delta_t)` (per-step fold body).
- `transientsolver.cpp:98` — `time_op.GetE()`; `:99` — `time_op.GetB()`; `:104` — `post_op.MeasureAndPrintAll(step, E, B, t, J_coef(t))`; `:114` — `post_op.MeasureFinalize(indicator)`; `:115` — `return {indicator, space_op.GlobalTrueVSize()}`.
- `transientsolver.hpp:21-30` — class decl; `Solve` decl `:26-27`, `GetTimeExcitation` `:24`.
- `palace/models/timeoperator.cpp:65-67` — `K = GetStiffnessMatrix(DIAG_ZERO)` / `C = GetDampingMatrix(DIAG_ZERO)` / `M = GetMassMatrix(DIAG_ONE)` (K/C/M assembled once).
- `timeoperator.cpp:311-313` — `IMPLICIT` type + `op = make_unique<TimeDependentFirstOrderOperator>(...)` (op built once); `:320/327/335/360` — the integrator-selection `switch` cases (GeneralizedAlpha / SDIRK23 / ARKStep / CVODE; library-owned, constructed once).
- `timeoperator.cpp:407-413` — `TimeOperator::Step(double &t, double &dt)`; `:410` — `ode->Step(sol, t, dt)` (the opaque MFEM ODESolver advance of the persistent `sol` field-state; closing `}` at `:413`).

Cross-references to the spine:
- Sibling map-pipeline columns: `book/src/feature/electrostatic.L4.md`, `magnetostatic.L4.md` (on disk; live links). The transient column is their fold-pipeline complement.
- `lifecycle` column (on disk) is the top-level ROOT the per-feature columns hang under.

## Open questions / caveats

- **Transient assembles THREE operators (K/C/M), not one** — the `fe_assemble` down-link in the matrix/table is a single row but stands for three assemble-folds (the second-order-in-time wave system). This is faithfully a single `fe_assemble` *combinator* applied three times; flagged so the matrix-row author (D2) does not read it as a single-operator assemble like the electrostatic/magnetostatic columns. Not a defect — a structural note on the fold-pipeline shape.
- **No per-step `ksp_solve` cap in the transient surface.** Unlike the fixed-operator map drivers, the implicit linear solve is *inside* the opaque MFEM ODE step (`ode->Step`), so it is not a user-visible composed constituent — the column quantifies over the opaque step. The implicit-solve-inside-the-integrator is recorded as `obstruction (opaque-library-ownership)` at the L4>L3 `fold-solve-time-step-dissolution` theme, not surfaced as a transient-column constituent. (No new OQ warranted — this is exactly the `fold_solve` opaque-per-step-body design already firm at c058.)
- **L4 term coefficients (`conductivity_term`, `permittivity_mass`) are sketched, not firm L4 ops.** The L4/L1 composition pseudocode names the C and M weak-form terms by descriptive coefficient names (`conductivity_term cfg`, `permittivity_mass cfg`) paralleling the firm `curl_curl (reluctivity cfg)` for K. These are illustrative term-list entries for `fe_assemble`, not asserted-firm L4 term combinators — consistent with the composition-root discipline (the column composes the firm *assemble* combinator; the per-term weak forms are `fe_assemble`'s opaque term inputs). No new chapter implied.
- **Whether eigenmode (the next fold/map driver) or driven (the state-generated-schedule fold) lands next** is D2/planner territory; the transient column establishes the fixed-list fold-pipeline pattern that the driven SweepAdaptive column will generalize (the `schedule-source: state-generated` axis of `fold_solve`, already recorded at `book/src/L4/fold_solve.md:115`). No action here.
