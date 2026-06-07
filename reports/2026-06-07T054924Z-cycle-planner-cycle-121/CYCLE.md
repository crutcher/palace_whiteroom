---
agent: cycle-planner
invoked_at: 2026-06-07T054924Z
scope: cycle-121 dispatch plan
status: pending
---

# Cycle 121 dispatch plan

**Position:** FIRST primary cycle of meta-batch-39 (cycles 121/122/123; batch-39 meta fires after c123 finalize). Post-OUT-OF-BAND-RESCOPE session restart (3 new directives 2026-06-07 loaded). c120 finalize `09b011f`; batch-38 meta `73b225e`; out-of-band rescope meta.

## Goals selected this cycle

Open the **lift-through + constructive-kernels campaign** (batch-39 active head — the rescope ENDS the batch-36/37/38 plateau). This cycle fires a 9-dispatch WIDE wave that lifts the shared mesh→fe_space→smoother→Krylov substrate ONCE across the related HIGH fronts: the **geometric-multigrid preconditioner is THE LEAD** (item-1; discharges RE9/RE1/RE5/RE7 by composing them by name), with its coupled constructive **kernel-impls** (DIRECTIVE-3: the relaxation-smoother impl-2b and libCEED-quadrature impl-2a and eigsolve impl-2c, each kernel-API/impl-linked), an **AMR substrate opener** (item-3 grounded consumer-(2)), and the two **cheap LOW openers** (item-5: RE10-interpolator grounding + waveguide-mode drift cleanup). Item-4 (re-discharge tail) stays consumer-gated — its consumers (multigrid, eigsolve-impl) land THIS cycle, so the RE re-check fires at c122. MPI/sharding stays OUT (DIRECTIVE-1 boundary).

## Linter baseline (c120 finalize, on disk)

`files=369, typed=308, untyped=61, roots=39, reachable=139, detritus=132, STRONGER=27, rank_violations=0, unresolved=0, promotion_frontier=6`. (Re-confirmed against the live `graded_stack_lint.py --json` detritus list this cycle: `L1/fe_space_hierarchy`, `L1/interpolator`, `L4/preconditioning-framework`, `L3/chebyshev`, `L3/jacobi-smoother`, `L1/normalize`, `L1/reciprocal`, `L2/elementwise_product` all currently detritus — exactly the RE-discharge targets the multigrid LEAD grounds.)

## Source-path verification (palace-codemap, this cycle)

All cited Palace paths verified on disk via the codemap (the planner has historically drifted on `linalg/*` paths):
- `palace/linalg/gmg.cpp:126` `GeometricMultigridSolver::Mult`, `:172` `VCycle`, ctor `:16`. ✓
- `palace/linalg/distrelaxation.cpp:13` `DistRelaxationSmoother` ctor (folds `ChebyshevSmoother`/`ChebyshevSmoother1stKind`). ✓
- `palace/linalg/ams.cpp:51` `HypreAmsSolver::ConstructAuxiliaryMatrices` (discrete-gradient + Nedelec interpolation). ✓
- `palace/fem/multigrid.hpp:78` `ConstructFiniteElementSpaceHierarchy`, `:106`/`:117` `AddLevel`. ✓
- `palace/linalg/errorestimator.cpp:273` `GradFluxErrorEstimator` ctor, `:391` `CurlFluxErrorEstimator` ctor, `:573-576` template instantiations. ✓
- `palace/drivers/basesolver.cpp:153` `BaseSolver::SolveEstimateMarkRefine` (hpp decl `basesolver.hpp:59`); `main.cpp:304` flagged-OUT call. ✓ (the plan's `:188-272` is a sub-range of the method body — codemap shows the method starts `:153`; producer on-disk-confirms the exact body bound.)
- `palace/linalg/divfree.cpp:117` (`Grad` discrete-gradient interpolator); `palace/drivers/boundarymodesolver.cpp:319-323` (`GetDiscreteInterpolator` discrete-curl `Bz`). ✓

## Deliverable-presence verification

Per the MANDATORY pre-dispatch deliverable-presence check (paste-inline-evidence). D1/D3/D4/D5/D6/D7 are **open by construction** (fresh chapters with no prior-cycle on-disk node — no multigrid/relaxation/libceed-impl/eigsolve-impl/amr column exists; `ls feature/*multigrid* L1/*relax* L1/*amr*` → only the existing `L4/preconditioning-framework.md` RE1 member). D2/D8/D9 have prior-cycle history (migrated c120 FINDINGS / firing watch) — checked:

- **D2 `FiniteElementSpaceHierarchy` concepts-page** — `ls book/src/concepts/FiniteElementSpaceHierarchy.md` → NOT present (open). In-chapter §Record-definition exists at `L1/fe_space_hierarchy.md:120-123`. Watch `record-FiniteElementSpaceHierarchy-promote-watch` NOW FIRING (multigrid column = 2nd firm consumer). NOT a no-op. ✓
- **D8 `re10-interpolator-ground`** — edges NOT yet present: `book/src/L1/interpolator.md` prose ALREADY names both consumers (`:23` `L1/divfree-projector` consumer-comment; `:249-250` boundary-mode discrete-curl; `:266` divfree `Grad` step) but NEITHER carries a `depends-on` edge. `L1/interpolator` reads detritus on disk (confirmed in the live linter list). OQ `re10-interpolator-has-faithful-reachable-consumer-missed-ground` MIGRATED → c121 item-1 (NOT closed). NOT a no-op. ✓
- **D9 `waveguide-mode-drift-cleanup`** — `grep -m1 'rank:' book/src/feature/waveguide-mode.L0.md` → `rank: rough-in` (the stale value; the L1/L4 siblings firmed c118 D5). OQ `waveguide-mode-column-promotion-index-cell-drift` MIGRATED → c121 (NOT closed). NOT a no-op. ✓

STOP-PROPOSING negative-list check: none of D1-D9 names a disqualified L3-backfill slug (`lu_solve`/`back_solve`/`ls-update-column`/`nleps_*`). The redirect's no-forced-rectangular-*vocabulary*-pull-up is honored — these are GROUNDED feature consumers + DIRECTIVE-3 kernel-impls + a fired RE-discharge, not rectangular floors. The STOP-PROPOSING posture on the in-scope deferred set is LIFTED by DIRECTIVE-2.

## Dispatches

1. **(`layer-intro-author`, `geometric-multigrid-preconditioner` feature-surface column [LEAD], deps: none)** — Author the L4(+L1) preconditioner composition-root column composing BY NAME via faithful `depends-on (composes)` edges: the V-cycle (`linalg/gmg.cpp:126`/`:172`), the firm `L4/preconditioning-framework`, the relaxation smoother (D3's kernel-impl, canonical slug `book/src/L1/multigrid-relaxation-smoother.md`), the `fe_space_hierarchy` level-stack (`fem/multigrid.hpp:78-126`), the `L3/chebyshev`/`L2/jacobi-smoother` smoother legs. THE named consumer that GROUNDS RE9/RE1/RE5/RE7. Single-machine-valid (read RAP/`Par*` single-rank; parallelism by composition). Forward-references D3's canonical slug (stated in both scopes). **Rationale:** batch-39 item-1, THE LEAD, highest fan-out (discharges 4 of 10 REs by composition).

2. **(`layer-intro-author`, `FiniteElementSpaceHierarchy` concepts-page promote + multigrid→fe_space_hierarchy GROUND edge, deps: 1)** — Promote `FiniteElementSpaceHierarchy` from `L1/fe_space_hierarchy.md:120-123` §Record-definition → `concepts/FiniteElementSpaceHierarchy.md` (multigrid column = 2nd firm consumer; the ≥2-consumer bar) + author the faithful `D1-column → L1/fe_space_hierarchy` `depends-on` edge. Needs D1's column node on disk. **Rationale:** fires `record-FiniteElementSpaceHierarchy-promote-watch`; GROUNDS RE9.

3. **(`harvester`, `multigrid-relaxation-smoother` kernel-impl [DIRECTIVE-3 item-2b], deps: none)** — Author the constructive relaxation realization (`linalg/distrelaxation.cpp:13` Hiptmair/distributive smoother) as a `kernel-impl` node (canonical slug `book/src/L1/multigrid-relaxation-smoother.md`, role-label `kernel-impl`), linked `realizes-kernel-api` (`reference`-class, NOT `depends-on`) to the KEPT `book/src/L1-L0/triangular-solve-obstruction.md` (role-label it `kernel-api`). Sequential-obstruction noted for the GS recurrence. **Rationale:** the coupled kernel-impl (the multigrid smoother IS the relaxation consumer); GROUNDS RE1 smoother leg.

4. **(`abstractor`, `libceed-quadrature-kernel-impl` [DIRECTIVE-3 item-2a], deps: none)** — Author the matrix-free FE operator-application-as-tensor-contractions impl (basis-eval × quad-weight × geometry-factor × coefficient, inside the firm `fe_assemble` fold) as a `kernel-impl` node (role-label `kernel-impl`), linked `realizes-kernel-api` (`reference`-class) to `book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md` (role-label it `kernel-api`). **Rationale:** opens the constructive-kernel frontier; the shared contraction substrate D6 probes.

5. **(`abstractor`, `eigsolve-kernel-impl` [DIRECTIVE-3 item-2c], deps: none)** — Author the constructive Lanczos/Arnoldi/Krylov-Schur eigsolve impl in our existing `L4/krylov-step`/`L3/krylov-step` vocabulary as a `kernel-impl` node, linked `realizes-kernel-api` (`reference`-class) to `book/src/L3/eigsolve.md` (partial-obstruction; role-label `kernel-api`). NOTE: `lanczos_step` is NOT on disk — author it as a same-cycle constituent OR seed it `roadmap_goal` rank-0 and depend-on it (clean-gate the choice). **Rationale:** opens the eigsolve-impl; becomes the RE3 deflate / RE8 krylov-iteration consumer next cycle.

6. **(`combinator-miner`, shared smoother/Krylov/contraction substrate probe, deps: none)** — Mine the recurrent core shared across D3 (relaxation) / D4 (contraction) / D5 (Krylov) — the shared tensor-contraction / iteration substrate the wide wave is designed to lift ONCE. Replace-and-propagate (NOT mine-and-strand) if a combinator surfaces; else a finding about the substrate. Reads D3/D4/D5's substrate framing but OWNS no shared file region. **Rationale:** the shared-exploration-lifting amortization that motivates the wide wave.

7. **(`abstractor`, `amr-flux-recovery-estimators` substrate opener [DIRECTIVE-2 item-3], deps: none)** — Open the AMR front with the ZZ flux-recovery estimator vocabulary cohort: `GradFluxErrorEstimator` (`errorestimator.cpp:273`, electrostatic) + `CurlFluxErrorEstimator` (`:391`, magnetostatic). Sketch the estimate→mark→refine driver loop (`basesolver.cpp:153` `SolveEstimateMarkRefine`, flagged-OUT `main.cpp:304`) + Dörfler bulk-marking (`utils/dorfler.cpp`, read single-rank) as the consuming context (roadmap_goal-class for the loop if not cleanly composable yet). MFEM-opaque mesh-refinement leaves stay obstruction-documented (NOT forced). **Rationale:** batch-39 item-3, a whole in-scope-adjacent feature opened; new vocabulary cohort.

8. **(`layer-intro-author`, `re10-interpolator-ground` [item-5a cheap opener], deps: none)** — Author the two faithful `depends-on (kind: uses)` edges → `book/src/L1/interpolator.md`: `book/src/L1/divfree-projector.md → book/src/L1/interpolator.md` (`palace/linalg/divfree.cpp:117`, within-L1 primary) + `book/src/L4/waveguide_mode_reduce.md → book/src/L1/interpolator.md` (`palace/drivers/boundarymodesolver.cpp:319-323`, L4→L1 altitude-skip per RE2/RE8/c110). FULL `book/src/L1/...` paths (disambiguate bare-basename AMBIG). DISCHARGES RE10 (+2 reachable; STRONGER→25). **Rationale:** the c120 FINDING-1 migrated grounding; honesty/liveness.

9. **(`layer-intro-author`, `waveguide-mode-drift-cleanup` [item-5b cheap opener], deps: none)** — Flip `book/src/feature/waveguide-mode.L0.md` off stale `rank: rough-in` to firm + reconcile `book/src/feature/index.md` + `book/src/feature/output-product.md` stale-`seed` cells (KEEP `feature_root: seed` — GC-root marker). SOLE owner of `feature/index.md` + `feature/output-product.md` this cycle. **Rationale:** the c120 FINDING-2 migrated cleanup; consistency hygiene.

## Overlap analysis

- **D1 ↔ D2:** OVERLAPPING → SEQUENTIAL. D2 reads D1's just-landed column node and appends the inbound `depends-on` edge to it (+ the concepts-page consumer). Order D1→D2.
- **D1 ↔ D3:** coupled (D1 composes D3's smoother) but DISJOINT files (D1 = `feature/*.{L4,L1}.md` new column; D3 = `book/src/L1/multigrid-relaxation-smoother.md` + `book/src/L1-L0/triangular-solve-obstruction.md`). D1 FORWARD-REFERENCES D3's canonical slug — the per-report integrator wires the live link when both land. Canonical slug `book/src/L1/multigrid-relaxation-smoother.md` stated in BOTH scopes (cross-report forward-reference slug-divergence guard). PARALLEL (forward-ref ordering only).
- **D1 ↔ D4/D5/D6/D7:** disjoint files; D1 may navigationally reference the kernel-impls but does not edit their files. PARALLEL.
- **D3 ↔ D4 ↔ D5:** three disjoint kernel-impl chapters (relaxation / libceed / eigsolve) each editing its own new `kernel-impl` file + role-labeling a DISTINCT `kernel-api` obstruction theme (`triangular-solve-obstruction` / `fe-assemble-libceed-boundary-obstruction` / `L3/eigsolve`). NO shared file region. PARALLEL.
- **D6 ↔ D3/D4/D5:** D6 (combinator-miner) is a probe/proposal — OWNS no shared file region this cycle (it reads the substrate framing; if it proposes a combinator the integrator routes the replace-and-propagate, but no co-cycle file collision). PARALLEL.
- **D7:** disjoint AMR files (`errorestimator`/`basesolver`/`dorfler` new chapters). PARALLEL.
- **D8 ↔ D9:** DISJOINT. D8 edits L1/L4 op files (`L1/divfree-projector.md`, `L4/waveguide_mode_reduce.md`, `L1/interpolator.md`); D9 edits `feature/waveguide-mode.L0.md` + SOLE-owns `feature/index.md` + `feature/output-product.md`. No overlap.
- **D2 ↔ D8/D9 (index files):** NO collision. D2 touches `concepts/` (new page) + the D1 column; D9 SOLE-owns `feature/index.md` + `feature/output-product.md`; D8 touches no index/feature-matrix file. No consolidated-tally divergence (D9 is the sole index-cell writer this cycle; the dual-registration partition does not apply — only one feature-matrix writer).

## Sequencing schedule

- **Wave 1 (parallel):** D1, D3, D4, D5, D6, D7, D8, D9 (8 dispatches). All disjoint or forward-reference-only. D1 forward-references D3's canonical slug (both stated); the per-report integrator wires the link at landing.
- **Wave 2 (after wave-1 reports land):** D2 (dep D1 — needs the multigrid column node on disk to promote the concepts-page consumer + add the inbound `depends-on` edge).

9 dispatches total — within the 12 cap and realistic for serial integration (8 of 9 are single-file or new-chapter landings; D2 is one promote + one edge).

## Open questions / caveats

- **`lanczos_step` is NOT on disk** (referenced by batch-39 item-2c / item-4a/4b). D5 must either author it as a same-cycle constituent of the eigsolve-impl OR seed it `roadmap_goal` rank-0 and `depends-on` it (clean-gate). Flagged for the c122+ re-discharge-tail planner: item-4a (deflate/RE3) and item-4b (krylov-iteration/RE2/RE8) couple to whatever D5 chooses for `lanczos_step`.
- **RE re-check fires NEXT cycle (c122), not this one.** Building the multigrid LEAD (D1/D2) + the kernel-impls (D3/D4/D5) FIRES the RE9/RE1/RE5/RE7/RE10 promotion conditions, but the authoritative RE-discharge confirmation runs on the LANDED tree. The c122 planner MUST re-run the linter + re-check the RE set against the new edges (per the every-batch RE-premise-re-check standing duty). Expected after c121: RE10 discharged (D8), RE9 grounded (D2), RE1/RE5/RE7 grounded transitively via D1's smoother-leg composition — STRONGER should drop materially (27 → ~20 or lower); re-measure, do not assume.
- **AMR loop composability (D7).** The estimate→mark→refine driver loop is flagged-OUT in Palace (`main.cpp:304`) and the Dörfler marker is distributed; D7 reads single-rank and may find the loop not cleanly composable in existing vocabulary yet — in which case it lands the flux-recovery estimator cohort firm + the loop as a `roadmap_goal` rank-0 chapter (NOT a forced firm claim), per the redirect's clean-gate. This is the correct outcome, not a miss.
- **DIRECTIVE-1 boundary respected:** no MPI-associated dispatch (`linalg/rap.{hpp,cpp}` `ParOperator`/RAP, `utils/geodata.cpp` distribution, MPI collectives) is in this plan. The multigrid (D1) and AMR (D7) read their `Par*`/RAP/distributed-Dörfler dependencies single-rank (parallelism by composition). Sharding-into-component-blocks remains a `roadmap_goal` future note only — NOT dispatched.
- **Kernel-API/impl integrity (D3/D4/D5):** each kernel-impl KEEPS its kernel-api obstruction theme (do NOT downgrade/delete); the `realizes-kernel-api` link is `reference`-class (free, navigational — NOT `depends-on`, so it does NOT constrain rank or carry liveness). `lowering-verifier` audits the impl-realizes-API correspondence — a c122 candidate once the impls land (not dispatched this cycle to keep the wave producer-focused; flag for the c122 planner).
- **Cadence note:** batch-39 meta fires after c123. If the RE-discharge re-check at c122 surfaces a pattern (e.g. a kernel-api/impl integrity drift, or a forced-edge smell in the multigrid grounding) not yet in the friction-ledger, the c122/c123 planner should note it for the batch-39 meta.
