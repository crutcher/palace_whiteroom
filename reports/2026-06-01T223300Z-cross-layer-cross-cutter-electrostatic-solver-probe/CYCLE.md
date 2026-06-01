---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-01T223300Z
scope: solver test-load FIRST PROBE — electrostatic pipeline clean-describability against the existing shared spine
status: pending
integrated_at: 2026-06-02T010000Z
integration_commit: 9633c134b333932b31f2823c558398fafdaa9750
integration_notes: "cycle-052 D6 — applied clean (electrostatic solver test-load FIRST PROBE; NO book mutation — inner third maps cleanly, outer skeleton + ends recorded as 4 spine work-items; single-witness generality caveat carried; 5 OQs promoted). Build-relevant: no."
---

# CYCLE: Cross-layer observation — electrostatic-solver-probe (spine-coverage finding)

## Summary

Probing the simplest of the 5 pipelines — `ElectrostaticSolver::Solve` (`palace/drivers/electrostaticsolver.cpp:20-98`) — for clean describability in the existing shared vocabulary, the **inner third of the pipeline maps cleanly** (the per-terminal linear solve is exactly `ksp_solve`; the `E = -∇V` step is `apply_linop`; the energy products in `PostprocessTerminals` are `dot` / `bilinear-form`), but the **outer structural skeleton and the two ends do NOT map** — there is no shared-spine vocabulary for (a) the **outer parametric sweep over terminals** that re-solves the *same operator* against a *family of RHS vectors* and collects per-member solutions, (b) **FE operator assembly from integrators** (`GetStiffnessMatrix` → `BilinearForm + DiffusionIntegrator + Assemble`), (c) **boundary-condition elimination / excitation-vector construction** (`GetExcitationVector` → `ProjectBdrCoefficient` + `EliminateRHS`), or (d) the **capacitance-matrix reduction** (the `O(n²)` energy-product accumulation over the solution family). This is **NOT clean** at the top level. Per the dispatch contract and the redirect's strict-low-priority observation-first rule, I author NO `book/` entry; the value is the spine-coverage finding below, which I record as **four spine work-items feeding future combinator-miner / abstractor dispatches** — without forcing the spine to fit, and without preempting the refactor-pass lead.

## Observation kind

**Coverage gap** — the electrostatic pipeline's top-level shape references operators (a parametric-sweep driver, an FE-assembly primitive, a BC-elimination primitive, a capacitance reduction) that **have no entry at any layer** in the shared spine. The existing spine covers the *inner linear-solve kernel* and the *BLAS-1 / operator-action* leaves, but not the *driver skeleton* that wraps them into a solver pipeline. The gap is honestly a finding **about the spine** (what shared vocabulary is missing), not a defect in the solver — the solver is the test-load probing the spine, exactly as the redirect intends.

## Specific finding

The driver body (`electrostaticsolver.cpp:20-98`) decomposes into six structural steps. Mapping each against the existing shared vocabulary:

| Driver step | Source | Maps to existing spine vocabulary? |
|---|---|---|
| 1. Assemble system operator `K = GetStiffnessMatrix()` | `:30`, def `palace/models/laplaceoperator.cpp:184-223` | **NO** — `BilinearForm k(...); k.AddDomainIntegrator<DiffusionIntegrator>(epsilon_func); k.Assemble(...)`. No FE-assembly-from-integrators operator exists. (`assemble-diagonal` is diagonal *extraction* from an already-assembled operator — the opposite direction; `bilinear-form` is a matrix-weighted *reduction* `xᴴMy`, not assembly.) |
| 2. Construct linear solver `ksp.SetOperators(*K,*K)` | `:34-35` | **CLEAN (construction-absorbed)** — folds into `ksp_solve`'s constructed-`Solver[A]` opaque argument (L1 §"Constructed-operator absorption", `book/src/L1/index.md`). |
| 3. **Outer loop over terminals** `for (const auto &[idx,data] : laplace_op.GetSources())` | `:60-89` | **NO** — re-solves the *same* `K` against a *family* of RHS vectors `{RHS_idx}`, collecting per-member solutions `V[step]`. This is a **parametric solve-sweep / map-over-RHS-family** shape. No such combinator exists at any layer. (Distinct from `ksp_solve`'s *inner* `solve_loop` over Krylov iterations — this is an *outer* loop over independent problems sharing an operator.) |
| 4. Build per-terminal RHS `GetExcitationVector(idx,*K,V[step],RHS)` | `:68`, def `laplaceoperator.cpp:225-253` | **NO** — `ProjectBdrCoefficient(one, source_marker)` (set `V=1` on terminal, `0` elsewhere) + `EliminateRHS(X,RHS)` (eliminate essential/Dirichlet dofs to form RHS). No BC-elimination / excitation-construction primitive exists. |
| 5. Inner linear solve `ksp.Mult(RHS, V[step])` | `:69` | **CLEAN** — exactly `ksp_solve`. `V[step] = ksp_solve(K, RHS_idx)`. The firm L4→L0 `ksp_solve` chain describes this verbatim. |
| 6a. Field recovery `E=0.0; Grad.AddMult(V[step],E,-1.0)` (`E = -∇V`) | `:78-79` | **CLEAN** — `apply_linop` accumulating variant (`AddMult` with `α=-1`). `E = apply_linop(Grad, V[step]) · (-1)`. |
| 6b. Energy / norm postprocess `Norml2(...)`, `MeasureAndPrintAll` | `:73-75`, `:80` | **CLEAN (leaf-level)** — `Norml2` is `nrm2`; the energy measures decompose to `dot` / `bilinear-form` (see 7). |
| 7. **Capacitance-matrix reduction** `PostprocessTerminals` | `:100-191` | **PARTIALLY** — the per-entry kernel `C(i,j) = linalg::Dot(comm, V_gf, D_gf)` with `D_gf = M_elec · V_gf` (`:118-126`) is exactly **`bilinear-form`** `Vⱼᴴ K Vᵢ` (the energy product; comment at `:119-121` confirms `Cᵢᵢ = VᵢᵀKVᵢ`). But the **`O(n²)` double-loop accumulation over the solution family into a dense `C` matrix**, plus the in-place `C.Invert()` (`:139`, LAPACK), have **no spine vocabulary** — this is a **Gram-matrix-style reduction over a vector family** (cf. the existing L2 `gram` operator, which is the closest analog but is built for Krylov-basis orthogonalization, not a solution-family energy-product matrix). |

**Maps cleanly (inner kernel + leaves):** steps 2, 5, 6a, 6b, and the `bilinear-form` kernel of step 7. The entire *inner linear solve and its immediate field/energy postprocessing* is already firm vocabulary.

**Does NOT map (outer skeleton + two ends):** steps 1, 3, 4, and the reduction-structure of 7. These are the **driver-level** and **FE-assembly-level** vocabulary the spine lacks.

MPI/Par* note (per scope): `ParGridFunction`, `ParOperator`, `Mpi::Print`, `linalg::Dot(comm,...)`, `GlobalSum` are read single-rank; the `comm` argument and `Mpi::Print` logging are flag-once-and-skip distribution surface, not part of the L1 shape. The `SetFromTrueDofs` / `ParallelProject` true-dof restriction (`:118`, `laplaceoperator.cpp:247`) is the single-rank prolongation identity at our scope.

## Recommendation

**Defer all four to future dispatches — this probe's deliverable is the finding, not an entry.** Per the redirect (solvers are strictly-low-priority test-load; advance a layer only when *cleanly describable*; what a solver can't cleanly say is a finding about the spine), I propose **no `book/` mutation** this cycle — the clean inner-kernel mapping is already covered by firm `ksp_solve`/`apply_linop`/`bilinear-form`, and the four gaps are NOT cleanly describable in existing vocabulary, so forcing entries would distort the spine. The four gaps become ranked spine work-items:

1. **Parametric solve-sweep combinator (step 3)** — HIGHEST fan-out. A `solve_family` / `map-solve-over-rhs` combinator: *fix operator `A`, map `ksp_solve(A, ·)` over an RHS family, collect the solution family*. This recurs across pipelines (driven solver sweeps over frequencies; eigenmode over modes; electrostatic/magnetostatic over terminals/ports) → **dispatch a `combinator-miner`** to mine it across ≥2 pipelines before authoring (do not mine-and-strand; replace-and-propagate per the redirect). It is plausibly a clean `map`-over-a-family at L4 with the shared-operator capture as the load-bearing structural feature (operator assembled *once*, outside the sweep — `electrostaticsolver.cpp:30` vs the loop at `:60`).
2. **Capacitance/Gram-family reduction (step 7 structure)** — MEDIUM-HIGH fan-out. The `O(n²)` energy-product matrix over a solution family. Check against the existing **L2 `gram`** operator first (the closest existing analog) — this may be a *variant-axis extension of `gram`* (general matrix-weight `K` instead of identity; solution-family instead of Krylov-basis) rather than a new operator. **Dispatch `same-layer-cross-cutter` or `combinator-miner`** to test the `gram`-unification hypothesis before authoring a new entry. The per-entry kernel is already `bilinear-form` (rough-in).
3. **FE operator assembly from integrators (step 1)** — MEDIUM fan-out, LARGE scope. `BilinearForm + integrator + Assemble → operator`. This is the mesh/FE-assembly surface (in scope per CLAUDE.md) and underlies *every* pipeline's operator construction. It is a substantial sub-spine of its own (integrator vocabulary, FE-space, quadrature) → **dispatch `abstractor`/`harvester` on the assembly surface as a dedicated thread**, NOT folded into the solver probe. Likely lands as its own operator family, not a solver-pipeline concern.
4. **BC-elimination / excitation-vector construction (step 4)** — MEDIUM fan-out. `ProjectBdrCoefficient + EliminateRHS`. Couples to the FE-assembly surface (item 3) — the essential-dof elimination is the assembly-side companion to the RHS construction. Sequence after item 3.

Suggested ordering: item 1 (combinator-miner, cross-pipeline) is the highest-value standalone next step and is solver-driver-shaped (not FE-assembly-shaped), so it advances the *driver spine* the redirect cares about. Items 3/4 are a separate FE-assembly thread. Item 2 is a cheap `gram`-unification probe.

## Proposed-changes

NONE. No `book/` mutation proposed this cycle (observation-first probe; the clean mappings are already firm, the gaps are not cleanly describable). The deliverable is this finding + the OQ-ledger appends below (for `integrator-per-report` to promote).

## Supporting evidence

- `palace/drivers/electrostaticsolver.cpp:20-98` — `ElectrostaticSolver::Solve`: operator assembly `:30`, solver construction `:34-35`, source/terminal count `:39-40`, RHS+solution storage `:43-44`, **outer terminal loop `:60-89`**, per-terminal RHS build `:68`, **inner solve `:69`**, field recovery `E=-∇V` `:78-79`, energy-norm print `:73-75`/`:80`, error-estimate update `:84`, capacitance postprocess `:96`.
- `palace/drivers/electrostaticsolver.cpp:100-191` — `PostprocessTerminals`: **capacitance kernel** `C(i,i)=Dot(V_gf, M_elec·V_gf)` `:118-126`, off-diagonal `Cᵢⱼ=Dot(...)` `:133-136`, **`O(n²)` double loop** `:111-137`, in-place `Cinv.Invert()` (LAPACK) `:139`, CSV output (root-only, flag-skip) `:141-190`.
- `palace/models/laplaceoperator.cpp:184-223` — `GetStiffnessMatrix`: `BilinearForm k(...); k.AddDomainIntegrator<DiffusionIntegrator>(epsilon_func); k.Assemble(...)` — FE-assembly-from-integrators (gap item 3).
- `palace/models/laplaceoperator.cpp:225-253` — `GetExcitationVector`: `ProjectBdrCoefficient(one, source_marker)` `:238`, `EliminateRHS(X, RHS)` `:252` — BC-elimination (gap item 4).
- Existing spine vocabulary checked for coverage:
  - `book/src/L4/ksp_solve.md` (firm) — covers step 5 (inner solve) verbatim; its `solve_loop` is the *inner* Krylov iteration, NOT the outer terminal sweep (the distinction is the crux of gap item 1).
  - `book/src/L1/apply_linop.md` (firm) — covers step 6a (`Grad.AddMult`, accumulating variant) and the `M_elec · V_gf` application inside step 7.
  - `book/src/L1/bilinear-form.md` (rough-in) — covers the step-7 per-entry kernel `Vⱼᴴ K Vᵢ` exactly (its law 8 energy-norm-squared `nrm2_M(x)²=bilinear_form(x,M,x)` is literally `Cᵢᵢ`); the off-diagonal `VⱼᴴKVᵢ` is the general bilinear form.
  - `book/src/L1/nrm2.md` / `book/src/L1/dot.md` (firm) — cover the `Norml2` / `Dot` leaves.
  - `book/src/L2/gram.md` (firm) — closest analog to the step-7 reduction *structure*; the `gram`-unification hypothesis for gap item 2.
  - `book/src/L1/assemble-diagonal.md` (firm) — confirmed NOT an assembly-from-integrators operator (it extracts `diag(A)` from an assembled `A`; opposite direction to gap item 1's need).
  - L1/L2/L3/L4 directory listings + L1 `index.md` dep-map scan — confirmed **no** entry for a parametric solve-sweep, FE-assembly-from-integrators, BC-elimination/excitation, or capacitance/solution-family-Gram reduction at any layer.

## Open questions / caveats

To append to `scaffolding/open-questions.md` (intake; meta-phase migrates actionable items to the plan):

- `electrostatic-outer-terminal-sweep-needs-solve-family-combinator` — the electrostatic pipeline's outer loop (`electrostaticsolver.cpp:60-89`) is a *fix-operator, map-`ksp_solve`-over-RHS-family, collect-solutions* shape with no spine vocabulary. HIGHEST-fan-out spine gap from this probe. Mine across ≥2 pipelines (driven freq-sweep, eigenmode mode-loop, magnetostatic port-loop) via combinator-miner before authoring — likely a clean L4 `map`-over-family with shared-operator capture. Feeds a future combinator-miner dispatch.
- `capacitance-reduction-may-be-gram-variant-axis-extension` — the `PostprocessTerminals` `O(n²)` energy-product matrix (`:111-137`) per-entry kernel is firm `bilinear-form`, but the family-reduction structure may unify with the existing L2 `gram` operator (general matrix-weight + solution-family axes) rather than warranting a new operator. Cheap same-layer-cross-cutter / combinator-miner probe; do not author a new entry until the `gram`-unification hypothesis is tested.
- `fe-assembly-from-integrators-is-an-unspined-surface` — `GetStiffnessMatrix` (`laplaceoperator.cpp:184-223`) and `GetExcitationVector` (`:225-253`) are FE-assembly-from-integrators + BC-elimination, in scope (mesh/FE-space) but with NO spine entry at any layer. A substantial dedicated sub-spine (integrator/FE-space/quadrature vocabulary), NOT a solver-pipeline concern — needs its own abstractor/harvester thread, sequenced independently of the solver test-load.

Caveats to verify before acting:
- The "highest fan-out" ranking of the solve-family combinator (item 1) is asserted from the cross-pipeline recurrence intuition (terminals/ports/frequencies/modes all loop-and-collect); a combinator-miner should *confirm* the shape recurs in ≥2 pipelines before it is authored — I probed only electrostatic. Do not author from this single witness.
- The `gram`-unification hypothesis (item 2) is structural, not verified — `gram` is built for Krylov-basis orthogonalization (`book/src/L2/gram.md`); whether its variant axes cleanly extend to "solution-family energy-product matrix with general weight" needs a real read of `gram.md`, which I did not do in depth (only confirmed it exists as the closest analog).
- `MeasureAndPrintAll` (`:80`) and `GradFluxErrorEstimator` (`:48-51`, `:84`) were not decomposed — they are postprocessing/error-estimation surface beyond the core solve skeleton; flagged as out-of-probe-scope, not claimed clean or unclean. A future deeper probe should check whether the error-estimator hides additional spine gaps.
- This is the FIRST solver probe; the finding is electrostatic-specific. The four gaps are *hypothesized* to generalize to the other 4 pipelines but that is unverified — the redirect's "advance only when cleanly describable across the shared spine" bar means the cross-pipeline confirmation (especially item 1) is load-bearing before any entry lands.
