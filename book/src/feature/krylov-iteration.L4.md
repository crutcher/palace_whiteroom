---
kind: feature-surface
feature: krylov-iteration
level: L4
feature_root: seed
rank: rough-in
edges:
  depends-on:
    - target: L3/krylov-step
      kind: composes                  # the per-step Arnoldi/CG basis-extension body the iteration folds (firm); DISCHARGES RE8
    - target: L3/fold_solve
      kind: composes                  # the state-threaded fold outer-driver — the carry-threaded sweep spine (partial-obstruction); DISCHARGES RE8
    - target: L3/orthogonalize
      kind: composes                  # the basis-orthogonalization auxiliary stage (MGS/CGS/CGS2) keeping the Krylov basis orthonormal (partial-obstruction); DISCHARGES RE2
    - target: L4/iterate-while
      kind: composes                  # the iteration combinator the outer driver IS (firm) — the L4 surface the L3 fold lowers from
    - target: L4/ksp_solve
      kind: composes                  # the Krylov-solve cap the iteration spine sits under (firm) — the consumer that drives the per-step fold
    - target: palace/linalg/iterative.cpp:421-464
      kind: cites-evidence            # CgSolver::Mult outer loop `for (; it < max_it && !converged; it++)` (:427) folding the per-step krylov-step body
    - target: palace/linalg/iterative.cpp:563-705
      kind: cites-evidence            # GmresSolver::Mult outer restart loop (:563) + inner Arnoldi/orthogonalize loop (:615) — the restart-shape outer fold over the basis-extension step
  reference:
    - feature/eigenmode.L4
    - feature/driven.L4
    - feature/geometric-multigrid-preconditioner.L4
    - L3/eigsolve-impl
    - L3/lanczos_step
    - concepts/sequential-obstruction
    - concepts/solver-as-operator
    - semantics/index
---

# Krylov-iteration spine — L4 composition-root

The **Krylov / Arnoldi iteration spine**, presented at L4 as a single composition of the firm
and rankable L3 **iteration-rotation** vocabulary. This chapter is a *composition root* of the
**infrastructure / shared-substrate** sub-kind (the [Infrastructure grouping](./infrastructure.md),
alongside the [geometric-multigrid preconditioner](./geometric-multigrid-preconditioner.L4.md))
— NOT a driver-leaf entry point and NOT an output product. It is the **iteration-rotation
parallel** of the GMG column: where GMG composes the *smoother* vocabulary into the V-cycle, this
column composes the *iteration-view* vocabulary into the Krylov outer-fold. It does not introduce
a new combinator; it wires the already-decomposed L3 iteration-rotation vocabulary into the
iterative-solve spine that every preconditioned Krylov solve in every driver hangs under, and
links DOWN to each composed piece. (Sub-kind: **driver-agnostic infrastructure** — the shared
iteration substrate under the solve, the solve-side analog of the driver-agnostic
[`energy-fields`](./energy-fields.L4.md) postprocess; not reciprocal-cross-linked to a single
producing driver, links generically to the set of drivers that compose it.)

This is the DIRECTIVE-2 item-4b grounded consumer: it is the *future faithful feature column
composing the L3 iteration-rotation form BY NAME* that the RE2 (`L3/orthogonalize`) and RE8
(`L3/krylov-step`, `L3/fold_solve`) baseline-exceptions name as their EXACT discharge trigger.
Building this column GROUNDS RE2 / RE8 by composing those nodes by name.

## The composition

At L4 the iteration spine is the composition (Haskell-style; the semantic surface
[`semantics/index`](../semantics/index.md) notation):

    -- input  = an iterative-solve specification (operator + preconditioner + orthogonalization variant + stopping predicate)
    -- output = the iterate trajectory's terminal carry (the converged solve / basis)
    krylov_iteration :: IterSpec -> Solve SimState (Krylov, SimState)
    krylov_iteration spec =
      let step  = krylov_step_for spec      -- (1) the per-step basis-extension body   ── L3/krylov-step (firm)
          aux   = orthogonalize_for spec    -- (2) the auxiliary orthogonalize stage    ── L3/orthogonalize (partial-obstruction)
      in  fold_iteration step aux spec      -- (3) the outer fold over the step          ── L3/fold_solve / L4/iterate-while

    -- the outer fold is the iterate_while / foldl driver (NOT a new vocabulary op; the loop
    -- structure read off iterative.cpp:427 (CG) / :563 (GMRES restart) / :615 (inner Arnoldi)):
    fold_iteration step aux spec =
      iterate_while
        (\(K, s) -> not (converged s spec))     -- stopping predicate (the convergence test)
        (\(K, s) -> let (K', s', _) = step (spec.op, K, s)   -- ONE basis-extension step (krylov-step)
                    in  (aux_apply aux K', s'))               -- orthogonalize the new column against the basis

Three composed stages, each a link DOWN to L3 iteration-rotation vocabulary:

1. **The per-step basis-extension body** — [`krylov-step`](../L3/krylov-step.md) (**firm**,
   c010). The value-threaded per-step kernel `(op, K, s) -> (K', s', outputs)`: one
   `apply_linop`, the optional auxiliary (orthogonalize / scalar-generate), the iterate-and-scalar
   update, the demand-prunable readout, the counter increment. The body **lifts** (every primitive
   is whole-tensor by signature shape); its outer-loop sequentiality is the documented
   [`sequential-obstruction`](../concepts/sequential-obstruction.md). **This is the named consumer
   that DISCHARGES RE8** (the `L3/krylov-step` unconsumed iteration-view). L0: the CG step body
   `iterative.cpp:434-463` folded by the outer `for (; it < max_it && !converged; it++)` (`:427`).

2. **The auxiliary orthogonalize stage** — [`orthogonalize`](../L3/orthogonalize.md)
   (**partial-obstruction**, c112). The `op.orthog (V_prefix, w)` auxiliary stage that keeps the
   Arnoldi/GMRES basis orthonormal — the variant-split partial-obstruction: CGS/CGS2 lift to the
   batched `H = Vᴴw` / `w' = w − VH` global statements, the MGS `j`-loop is a witnessed
   `sequential-obstruction`. **This is the named consumer that DISCHARGES RE2** (the
   `L3/orthogonalize` unconsumed iteration-view). L0: the GMRES inner Arnoldi/orthogonalize loop
   `iterative.cpp:615-632` (`OrthogonalizeIteration` + the caller's `Norml2`/`scal`).

3. **The outer fold over the step** — [`fold_solve`](../L3/fold_solve.md)
   (**partial-obstruction**, c058) lowered from [`iterate-while`](../L4/iterate-while.md) (**firm**).
   The state-threaded fold outer-driver: the carry-threaded sweep where each step's input is the
   prior step's output (the carry-threading `sequential-obstruction`; the schedule does not
   commute). **This is the named consumer that DISCHARGES RE8** (the `L3/fold_solve` unconsumed
   iteration-view). At L4 the outer fold is the `iterate_while` combinator the
   [`ksp_solve`](../L4/ksp_solve.md) cap drives; the L3 `fold_solve` is its iteration-rotation
   image (the explicit value-threaded tail recursion). L0: the CG outer loop `iterative.cpp:427`;
   the GMRES outer restart loop `iterative.cpp:563` (the restart-shape fold over the inner
   basis-extension loop).

## Inputs / outputs (the feature surface)

- **Input — the iterative-solve specification.** The operator-parameters `op` (the system
  operator `op.T`, the optional preconditioner-side `apply_BA`, the optional `op.orthog`
  orthogonalization closure, the optional `op.scalars` polynomial-recurrence closure), the seed
  iterate-bundle, and the stopping predicate (the convergence test). All construction-stratum;
  the operator/preconditioner are bound once outside the fold (the operator-capture-once law
  `fold_solve` Law 2). L0: the `CgSolver` / `GmresSolver` workspace + operator set
  (`iterative.cpp:361-372`, `:544-563`).
- **Output — the converged solve.** The terminal carry of the iterate trajectory: the converged
  iterate `s.x` plus the four-scalar KSP result surface (`converged`, `initial_res`, `final_res`,
  `final_it`; `iterative.hpp:52-55`). For the eigensolve consumer (via
  [`eigsolve-impl`](../L3/eigsolve-impl.md)) the terminal carry is the orthonormal Krylov basis
  `BV` + the recurrence coefficients (the Hessenberg/tridiagonal `H`/`T`). L0: the result
  extraction `ksp.cpp:296-310`.

## Why this is rough-in (the well-foundedness verdict)

Under the well-foundedness invariant `rank(u) ≤ min(deps)` (CLAUDE.md §Methodology-invariants
GRADED RESOLUTION LADDER), this column is **`rough-in`**, NOT firm:

- The three composed **blocking** constituents are `L3/krylov-step` (**firm**),
  `L3/fold_solve` (**partial-obstruction**), `L3/orthogonalize` (**partial-obstruction**) — read
  off each chapter's on-disk `## Status` / `firmness:` line this dispatch. So
  `rank(krylov-iteration) ≤ min(firm, partial-obstruction, partial-obstruction) =
  partial-obstruction (≈ rank 2.5)` — the column is at most as resolved as its least-resolved
  iteration-view, which is partial-obstruction.
- This is **faithful-or-finding, not a forced claim.** The iteration-rotation spine is *precisely*
  the surface where the body-lifts-loop-doesn't obstruction lives: the carry-threaded outer fold
  (`fold_solve`), the MGS `j`-loop (`orthogonalize`), and the outer Krylov sequential obstruction
  (`krylov-step`'s outer loop). A column composing those views honestly INHERITS the
  partial-obstruction — the iteration spine cannot be firm while its iteration-views carry
  witnessed sequential obstructions. The per-step bodies all lift (the composition is cleanly
  statable BY NAME), so the column is a real `rough-in` (it composes real on-disk firm/rankable
  substrate), not a roadmap_goal.
- **Promotion route:** `rough-in → firm` if/when the two partial-obstruction iteration-views
  promote (they will not — their obstructions are intrinsic: carry-threading and MGS numerical
  stability are non-removable). The honest standing state of the iteration spine is `rough-in`
  with the inherited sequential-obstruction recorded — the same body-lifts-loop-doesn't honesty
  the constituent L3 chapters carry. This is a *finding about the spine*: the iteration-rotation
  feature surface is constitutively partial-obstruction, because iteration IS the obstruction.

The roadmap_goal [`eigsolve-impl`](../L3/eigsolve-impl.md) / [`lanczos_step`](../L3/lanczos_step.md)
are `reference` (NOT blocking `depends-on`) — they are the constructive-eigensolve consumers that
fold this iteration spine (the coupling the planner noted), not constituents of it. Wiring them
`reference` keeps them from gating this column's rank (a rank-0 roadmap_goal blocking-dep would
force the column to rank 0, which would be the §2g over-edge — the real relationship is
"eigsolve-impl FOLDS this spine", a downstream consumer, not "this spine composes eigsolve-impl").

## Single-machine reading (DIRECTIVE-1)

The Krylov solve's `Mpi::GlobalSum` / `Mpi::Print` collectives inside the inner products
(`iterative.cpp` `linalg::Dot` over `comm`) are read **single-rank** — the iteration recurrence,
the orthogonalize stage, and the outer fold are identical at single rank; the parallelism is **by
composition** (the dot/allreduce inside HYPRE/MPI is the deferred MPI layer DIRECTIVE-1 keeps OUT).
No MPI-associated version is lifted here.

## Constituent down-links

| Stage | Constituent | Status | discharges | L0 site |
|---|---|---|---|---|
| per-step basis-extension body | [`krylov-step`](../L3/krylov-step.md) | firm (c010) | RE8 | `iterative.cpp:434-463` folded by `:427` |
| auxiliary orthogonalize stage | [`orthogonalize`](../L3/orthogonalize.md) | partial-obstruction (c112) | RE2 | `iterative.cpp:615-632` (GMRES Arnoldi) |
| outer fold over the step | [`fold_solve`](../L3/fold_solve.md) / [`iterate-while`](../L4/iterate-while.md) | partial-obstruction (c058) / firm | RE8 | `iterative.cpp:427` (CG) / `:563` (GMRES restart) |
| iterate combinator | [`iterate-while`](../L4/iterate-while.md) | firm | — | strawman §3.7 |
| Krylov-solve cap (consumer) | [`ksp_solve`](../L4/ksp_solve.md) | firm | — | `ksp.cpp:296-310` |
| constructive eigensolve consumer (reference) | [`eigsolve-impl`](../L3/eigsolve-impl.md) / [`lanczos_step`](../L3/lanczos_step.md) | roadmap_goal | — | — |

## Status

`rough-in` — the **first iteration-rotation infrastructure** feature-surface composition-root
(the 2nd member of the Infrastructure grouping after the GMG preconditioner; DIRECTIVE-2 item-4b,
the RE2/RE8 discharge). The GC-root marker `feature_root: seed` is preserved (root-role is
permanent/categorical, a separate axis from the resolution ladder). **Why rough-in (not firm):**
two of the three directly-owned **blocking** constituents are `partial-obstruction` on disk
(`L3/fold_solve`, `L3/orthogonalize`); `L3/krylov-step` is firm. The well-foundedness invariant
`rank(u) ≤ min(deps) = partial-obstruction` caps the column below firm — the honest verdict, since
the iteration-rotation spine is constitutively the surface where the body-lifts-loop-doesn't
sequential obstruction lives (carry-threading + MGS recurrence + outer Krylov fold). The per-step
bodies all lift, so the composition is cleanly statable BY NAME — a real rough-in column composing
real on-disk substrate, not a roadmap_goal. This chapter carries the *compositional* claim (the
Krylov iteration spine = this composition of these iteration-view pieces, GROUNDING RE2/RE8 by
name), not the constituents' per-op algebraic claims (those live in the linked chapters).
**DISCHARGES RE2** (`L3/orthogonalize` reachable via the `depends-on (composes)` edge) **and RE8**
(`L3/krylov-step`, `L3/fold_solve` reachable via `depends-on (composes)`) — a genuine
depends-on reachability flip (root→node liveness), NOT a reference-only-reachable artifact (see
the report's reference-edge-liveness scheme evidence). Evidence: `iterative.cpp:421-464` (CG outer
fold) + `:563-705` (GMRES restart + inner Arnoldi) realizing the composition, plus the L3
iteration-view down-links.
