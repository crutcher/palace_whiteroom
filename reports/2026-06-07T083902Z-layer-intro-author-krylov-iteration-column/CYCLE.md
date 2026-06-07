---
agent: layer-intro-author
invoked_at: 2026-06-07T083902Z
scope: D2 cycle-123 — the L3-iteration-view feature column (Krylov-iteration infrastructure column; DIRECTIVE-2 item-4b; discharges RE2/RE8)
status: pending
integrated_at: 2026-06-07T083902Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean (D2). krylov-iteration.{L4,L1} infrastructure feature column landed (feature_root: seed, rank: rough-in); blocking depends-on edges DISCHARGE RE2 (L3/orthogonalize) + RE8 (L3/krylov-step, L3/fold_solve) via a GENUINE depends-on reachability flip (confirmed on landed tree; eigsolve-impl + lanczos_step correctly stayed detritus). Landed rough-in PRECISELY to keep rank(u) <= min deps over its partial-obstruction L3 deps. Promoted OQ krylov-iteration-rough-in-vs-firm-over-partial-obstruction-iteration-views (a batch-39 meta headline) + optional eigsolve-impl-reference-uplink. cargo make book EXIT 0; rank_violations 0; both step-5b block-conditions PASS. Batch-39 BATCH-CLOSING finalize."
---

# CYCLE: feature/krylov-iteration — the L3 iteration-rotation spine (infrastructure column)

## Summary

Authors a new **infrastructure / shared-substrate feature-surface column** —
`feature/krylov-iteration.{L4,L1}` (canonical slug kept; no cleaner name surfaced) — the
2nd member of the Infrastructure grouping alongside the GMG preconditioner. It is the
**iteration-rotation spine**: a composition root that explains the Krylov / Arnoldi
basis-extension iteration as a coherent surface and COMPOSES the L3 iteration-view
vocabulary BY NAME via faithful `depends-on (composes)` edges to
[`L3/krylov-step`](../../book/src/L3/krylov-step.md) (firm),
[`L3/fold_solve`](../../book/src/L3/fold_solve.md) (partial-obstruction),
[`L3/orthogonalize`](../../book/src/L3/orthogonalize.md) (partial-obstruction), and a
`reference` to the roadmap_goal [`L3/eigsolve-impl`](../../book/src/L3/eigsolve-impl.md) /
[`L3/lanczos_step`](../../book/src/L3/lanczos_step.md).

**RE2/RE8 discharge — REAL, not a reference-edge stranding.** Per the planner's note, the
`depends-on (composes)` edges from this `feature_root` column to the three L3 iteration-views
are the EXACT discharge trigger RE2 (`L3/orthogonalize`) and RE8 (`L3/fold_solve`,
`L3/krylov-step`) name. Because a feature ROOT carries liveness through its OWN-COMPOSITION
`depends-on` edges (root→node), the three views become **reachable** under the reachability
GC — RE2 and RE8 discharge by composition-by-name, exactly as the GMG column discharged
RE9/RE1/RE5/RE7. I wired them as **blocking `depends-on (composes)`**, NOT `reference`, so the
discharge is genuine.

**Column rank: `rough-in` (NOT firm) — faithful-or-finding.** The well-foundedness invariant
`rank(u) ≤ min(deps)` caps the column at its least-resolved BLOCKING constituent. Two of the
three composed iteration-views are **`partial-obstruction`** on disk (`fold_solve`,
`orthogonalize`); `krylov-step` is firm. So `rank(krylov-iteration) ≤ min(firm,
partial-obstruction, partial-obstruction) = partial-obstruction ≈ 2.5`, i.e. NOT firm. This
is the honest verdict: the iteration-rotation spine is precisely the surface where the
body-lifts-loop-doesn't obstruction lives (the MGS `j`-loop, the carry-threaded time-sweep,
the outer Krylov fold), so a column composing those views faithfully inherits the
partial-obstruction. I land it `rough-in` with the obstruction-inheritance recorded — the
clean-gate "land a roadmap_goal/finding rather than a forced firm claim" applied (it composes
real on-disk firm/rankable substrate, so it is a real rough-in column, not a roadmap_goal).

## Reference-edge-liveness scheme evidence (for the batch-39 meta — REQUIRED per the planner)

Per the planner's OQ and the c123 plan §Open-questions: this column's landing is **intentional
evidence-gathering** for the batch-39-meta reference-edge-liveness scheme adjudication.

- **The faithful RE2/RE8 discharge route IS a root→node `depends-on (composes)` chain.** The
  column is a `feature_root: seed`; its `depends-on (composes)` edges to `L3/krylov-step` /
  `L3/fold_solve` / `L3/orthogonalize` make those three nodes reachable from a GC root. This
  IS the discharge. Under the *current* depends-on-traversing GC, a `feature_root` node's
  OUTBOUND `depends-on` edges propagate liveness to their targets (the same mechanism by which
  the GMG column's `depends-on (composes)` edges grounded RE9/RE1/RE5/RE7). So unlike the GMG
  `L3/chebyshev` / `L2/jacobi-smoother` case — which the GMG column reaches via `reference`
  (sibling-view) edges and which therefore STAY reference-only-reachable / STRONGER — this
  column reaches its three L3 views via **blocking `depends-on`**, so they should flip to
  **reachable**. **Net: the RE2/RE8 discharge is NOT a reference-only-reachable artifact; it is
  a genuine depends-on reachability flip.** This is the distinguishing data point for the meta:
  a faithful feature-column discharge via `depends-on (composes)` flips the discharged views
  `reachable` (RE2/RE8 leave STRONGER), whereas the c122 kernel-impl/combinator-specialization
  cohort reaches its targets via `reference`/`folds`/`realizes-kernel-api` and stays
  reference-only-reachable. The two cohorts are mechanically distinct.
- **Per-node attribution after this lands (predicted; the integrator/meta confirm on the
  rebuilt tree):** `L3/krylov-step`, `L3/fold_solve`, `L3/orthogonalize` should move OUT of
  STRONGER (RE2/RE8 discharged). The roadmap_goal `L3/eigsolve-impl` / `L3/lanczos_step` are
  reached only by `reference` here (NOT by this column's `depends-on`), so they do NOT gain
  liveness from this column — their liveness still rests on their own `pulled-by` provenance
  to the eigenmode root (unchanged). So this column adds **3 nodes flipping reachable via
  depends-on** to the evidence corpus, and does NOT add to the reference-only-reachable
  corpus. That is the clean second data class the planner wanted: a depends-on RE-discharge
  (reachable-flip) distinct from the c122 reference-only-reachable kernel-impl/combinator class.

## Proposed changes

### 1. New file — `feature/krylov-iteration.L4.md`

```edit:book/src/feature/krylov-iteration.L4.md
[old]:
[new]:
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
```

### 2. New file — `feature/krylov-iteration.L1.md`

```edit:book/src/feature/krylov-iteration.L1.md
[old]:
[new]:
---
kind: feature-surface
feature: krylov-iteration
level: L1
feature_root: seed
rank: rough-in
edges:
  depends-on:
    - target: L1/orthogonalize
      kind: composes                  # the pure orthogonalize leaf the iteration's auxiliary stage applies (firm); the L1 image of the L3 orthogonalize view
    - target: L1/apply_linop
      kind: composes                  # the whole-tensor operator-apply A·v per step (firm)
    - target: L1/axpy
      kind: composes                  # the iterate update x += α p / r -= α z (firm)
    - target: L1/axpby
      kind: composes                  # the direction update p ← z + (β/β_prev) p (firm)
    - target: L1/dot
      kind: composes                  # the recurrence inner products (Ap,p) / (Br,r) (firm)
    - target: L1/nrm2
      kind: composes                  # the residual / Hessenberg-subdiagonal norm (firm)
    - target: L1/scal
      kind: composes                  # the basis-column normalization v ← w/β (firm)
    - target: palace/linalg/iterative.cpp:421-464
      kind: cites-evidence            # CgSolver::Mult pure-function-rendered per-step body + outer fold
    - target: palace/linalg/iterative.cpp:563-705
      kind: cites-evidence            # GmresSolver::Mult restart + inner Arnoldi/orthogonalize
  reference:
    - feature/krylov-iteration.L4
    - L3/krylov-step
    - L3/fold_solve
    - L3/orthogonalize
    - concepts/sequential-obstruction
---

# Krylov-iteration spine — L1 composition-root

The **Krylov iteration spine** presented at L1 as the pure-function rendering of the per-step
basis-extension body and the outer fold — the mutation-rotated form of `CgSolver::Mult` /
`GmresSolver::Mult` (`palace/linalg/iterative.cpp:361-464`, `:544-705`), where the in-place
vector mutations (`x.Add(alpha, p)`, `r.Add(-alpha, z)`, `w.Add(-H[j], V[j])`) are re-expressed
as pure tensor-in / tensor-out functions threaded through the iteration. This is the
infrastructure / shared-substrate column at L1; it composes the firm L1 BLAS-1 + orthogonalize
vocabulary into the per-step iterate update and links DOWN to each piece. The L4 surface
([`krylov-iteration.L4`](./krylov-iteration.L4.md)) carries the full iteration-rotation
composition narrative (the three L3 iteration-views it composes, the RE2/RE8 discharge); this L1
surface is the pure-function shape the L4 combinator composition lowers onto.

## The pure per-step body

The per-step Krylov body is a **pure function** over flat dof-vectors (`Vector` is rank-1, so
the L1 shape group is the flat `Tensor[N]` per the named-shape-group convention; KEEP `Tensor[N]`
at L1). For CG (`iterative.cpp:434-463`), one step is:

    -- per-step CG body (pure form; the in-place x.Add / r.Add re-expressed as pure axpy):
    cg_step :: (op, K) -> K'
    cg_step op K =
      let p'    = if K.first then K.z else axpby K.z (K.beta / K.beta_prev) K.p  -- direction update (L1/axpby)
          z'    = apply_linop op.A p'                                             -- A·p           (L1/apply_linop)
          denom = dot z' p'                                                       -- (Ap, p)        (L1/dot)
          alpha = K.beta / denom
          x'    = axpy alpha p' K.x                                              -- x += α p       (L1/axpy)
          r'    = axpy (negate alpha) z' K.r                                     -- r -= α z       (L1/axpy)
          z''   = apply_B op.B r'                                                -- preconditioner apply
          beta' = dot z'' r'                                                     -- (Br, r)        (L1/dot)
      in  K { x = x', r = r', p = p', z = z'', beta = beta', beta_prev = K.beta }

For GMRES the per-step body additionally runs the [`orthogonalize`](../L1/orthogonalize.md) leaf
against the stored basis prefix (`iterative.cpp:615-632`) and normalizes via
[`nrm2`](../L1/nrm2.md) + [`scal`](../L1/scal.md). The body **lifts** — every primitive is a pure
whole-vector L1 op; the sequentiality is in the *outer fold over the body* (the carry-threading),
not the body itself. This is the L1 pure-function image of the firm [`krylov-step`](../L3/krylov-step.md)
iteration-view (the L3>L2>L1 body identity-in-form chain).

## The outer fold

The outer fold is a tail recursion threading the iterate-bundle carry `K` over the iteration —
the L1 image of the L3 [`fold_solve`](../L3/fold_solve.md) outer-driver. Each step's input `K` is
the prior step's output `K'`: the read-after-write that is the carry-threading
[`sequential-obstruction`](../concepts/sequential-obstruction.md). L0: the CG outer loop
`for (; it < max_it && !converged; it++)` (`iterative.cpp:427`); the GMRES restart loop
(`:563`) folding the inner Arnoldi loop (`:615`).

## Constituent down-links

| Stage | Constituent | Status | L0 site |
|---|---|---|---|
| direction / iterate update | [`axpy`](../L1/axpy.md) / [`axpby`](../L1/axpby.md) | firm | `iterative.cpp:440,448,449` |
| operator apply | [`apply_linop`](../L1/apply_linop.md) | firm | `iterative.cpp:443` (`A->Mult(p, z)`) |
| recurrence inner products | [`dot`](../L1/dot.md) | firm | `iterative.cpp:444,461` (`linalg::Dot`) |
| residual / subdiagonal norm | [`nrm2`](../L1/nrm2.md) | firm | `iterative.cpp:462` / GMRES `:630` |
| basis-column normalize | [`scal`](../L1/scal.md) | firm | GMRES `:631` |
| auxiliary orthogonalize | [`orthogonalize`](../L1/orthogonalize.md) | firm | `iterative.cpp:629` (`OrthogonalizeIteration`) |

## Status

`rough-in` — the L1 pure-function surface of the Krylov iteration spine (the 2nd Infrastructure
column at L1, after the GMG preconditioner). The L1 constituents are all firm BLAS-1 +
orthogonalize leaves, but the column inherits the L4 surface's `rough-in` rank: the
*iteration-rotation* claim it composes (the [`krylov-iteration.L4`](./krylov-iteration.L4.md)
view) rests on the L3 iteration-views, two of which are `partial-obstruction`. The L1 per-step
bodies lift cleanly; the obstruction is in the outer fold over the body (carry-threading), which
this column records via the L3 `fold_solve` reference. This chapter carries the *compositional*
claim (the iteration spine's per-step body = this pure composition of these firm L1 leaves), not
the constituents' per-op algebra. Evidence: `iterative.cpp:421-464` (CG) + `:563-705` (GMRES)
mutation-rotated to the pure per-step body + outer fold.
```

### 3. `feature/index.md` — add the column to the Infrastructure matrix grouping

```edit:book/src/feature/index.md
[old]:
| **[Infrastructure / shared-substrate columns](./infrastructure.md)** | | | |
| [geometric-multigrid-preconditioner](./geometric-multigrid-preconditioner.L4.md) (firm) | [L4 root](./geometric-multigrid-preconditioner.L4.md) | [L1 root](./geometric-multigrid-preconditioner.L1.md) | — |
[new]:
| **[Infrastructure / shared-substrate columns](./infrastructure.md)** | | | |
| [geometric-multigrid-preconditioner](./geometric-multigrid-preconditioner.L4.md) (firm) | [L4 root](./geometric-multigrid-preconditioner.L4.md) | [L1 root](./geometric-multigrid-preconditioner.L1.md) | — |
| [krylov-iteration](./krylov-iteration.L4.md) (rough-in) | [L4 root](./krylov-iteration.L4.md) | [L1 root](./krylov-iteration.L1.md) | — |
```

### 4. `feature/infrastructure.md` — add the column to the member list + the reference edges

```edit:book/src/feature/infrastructure.md
[old]:
edges:
  reference:
    - feature/geometric-multigrid-preconditioner.L4
    - feature/geometric-multigrid-preconditioner.L1
[new]:
edges:
  reference:
    - feature/geometric-multigrid-preconditioner.L4
    - feature/geometric-multigrid-preconditioner.L1
    - feature/krylov-iteration.L4
    - feature/krylov-iteration.L1
```

```edit:book/src/feature/infrastructure.md
[old]:
Current member:

- [**geometric-multigrid preconditioner**](./geometric-multigrid-preconditioner.L4.md) — the
  V-cycle preconditioner every multi-level Krylov solve (and the firm
  [`divfree-projector`](../L1/divfree-projector.md)) hangs under; the DIRECTIVE-2 grounded
  consumer-(1) that GROUNDS RE9/RE1/RE5/RE7 by composing the prolongation level-stack +
  smoother leg + diagonal-preconditioner chains by name. (rough-in.)
[new]:
Current members (alpha-within-this-kind):

- [**geometric-multigrid preconditioner**](./geometric-multigrid-preconditioner.L4.md) — the
  V-cycle preconditioner every multi-level Krylov solve (and the firm
  [`divfree-projector`](../L1/divfree-projector.md)) hangs under; the DIRECTIVE-2 grounded
  consumer-(1) that GROUNDS RE9/RE1/RE5/RE7 by composing the prolongation level-stack +
  smoother leg + diagonal-preconditioner chains by name. (firm.)
- [**krylov-iteration**](./krylov-iteration.L4.md) — the Krylov / Arnoldi **iteration spine**
  every iterative solve hangs under; the iteration-rotation parallel of the GMG column. The
  DIRECTIVE-2 item-4b grounded consumer that DISCHARGES RE2 (`L3/orthogonalize`) and RE8
  (`L3/krylov-step`, `L3/fold_solve`) by composing the L3 iteration-rotation form BY NAME via
  blocking `depends-on (composes)` edges (a genuine depends-on reachability flip). (rough-in —
  capped at partial-obstruction by its `fold_solve` / `orthogonalize` iteration-views, the
  body-lifts-loop-doesn't honesty; coupled to the roadmap_goal
  [`eigsolve-impl`](../L3/eigsolve-impl.md) constructive eigensolve consumer.)
```

### 5. `SUMMARY.md` — nest the column under the Infrastructure grouping (high→low within-column order)

```edit:book/src/SUMMARY.md
[old]:
- [Infrastructure / shared-substrate columns](./feature/infrastructure.md)
  - [geometric-multigrid-preconditioner — L4 composition-root](./feature/geometric-multigrid-preconditioner.L4.md)
  - [geometric-multigrid-preconditioner — L1 composition-root](./feature/geometric-multigrid-preconditioner.L1.md)
[new]:
- [Infrastructure / shared-substrate columns](./feature/infrastructure.md)
  - [geometric-multigrid-preconditioner — L4 composition-root](./feature/geometric-multigrid-preconditioner.L4.md)
  - [geometric-multigrid-preconditioner — L1 composition-root](./feature/geometric-multigrid-preconditioner.L1.md)
  - [krylov-iteration — L4 composition-root](./feature/krylov-iteration.L4.md)
  - [krylov-iteration — L1 composition-root](./feature/krylov-iteration.L1.md)
```

## Supporting evidence

- **Constituent on-disk `## Status` (read this dispatch, NOT the cycle record):**
  - `book/src/L3/krylov-step.md` — `firmness: firm` (frontmatter) + `## Status: firm` (:166-168).
  - `book/src/L3/fold_solve.md` — `firmness: partial-obstruction` (frontmatter) + `## Status:
    partial-obstruction` (:150-156).
  - `book/src/L3/orthogonalize.md` — `rank: partial-obstruction` (frontmatter) + `## Status:
    partial-obstruction` (:478-502).
  - `book/src/L3/eigsolve-impl.md` — `status: roadmap_goal` / `rank: roadmap_goal` (reference,
    not blocking).
  - `book/src/L3/lanczos_step.md` — `status: roadmap_goal` / `rank: roadmap_goal` (reference,
    not blocking).
- **Precedent (the Infrastructure / shared-substrate sub-kind):**
  `book/src/feature/infrastructure.md` (the group intro) + `book/src/feature/geometric-
  multigrid-preconditioner.{L4,L1}.md` (the GMG composition-root — the
  `feature_root: seed` + `rank` + `depends-on (composes)` + `reference` edge-block shape, the
  within-column high→low ordering, the RE-grounding-by-name pattern).
- **L0 anchors (self-verified via `palace-codemap` `read_range` this dispatch):**
  - `palace/linalg/iterative.cpp:361-372` — `CgSolver::Mult` workspace + operator-set head.
  - `palace/linalg/iterative.cpp:427` — `for (; it < max_it && !converged; it++)` — the CG
    outer fold over the per-step body (the `iterate_while`-folding-`krylov-step` consumer site).
  - `palace/linalg/iterative.cpp:434-463` — the CG per-step body (`AXPBY` direction update :440,
    `A->Mult(p,z)` :443, `Dot` :444, `x.Add`/`r.Add` :448-449, preconditioner `ApplyB` :454,
    `Dot` :461, `res` :462) — the per-step body the fold folds.
  - `palace/linalg/iterative.cpp:544-563` — `GmresSolver::Mult` head + the outer restart loop
    `for (; it < max_it; restart++)` (:563).
  - `palace/linalg/iterative.cpp:615` — the GMRES inner Arnoldi loop `for (;; j++, it++)` (the
    basis-extension + orthogonalize loop the restart loop folds).
- **The RE2/RE8 baseline-exception text** (planner CYCLE.md §RE-recheck rows RE2/RE8): both name
  "the L3-iteration-view feature column composing the iteration-rotation form by name" as the
  exact discharge trigger — this column is that trigger.
- **Semantic surface USE+LINK:** the L4 chapter's calculus notation cites
  [`semantics/index`](../semantics/index.md) (§3.7 `iterate_while`, the named-shape-group
  convention) rather than restating the general rules; the per-op shape facts stay in the linked
  constituent chapters.

## Open questions / caveats

- **Column rank is `rough-in`, deliberately — the iteration spine is constitutively
  partial-obstruction.** Unlike the GMG column (which firmed once its smoother constituent
  firmed), this column's two `partial-obstruction` iteration-views (`fold_solve`,
  `orthogonalize`) will NOT promote — their obstructions (carry-threading; MGS numerical
  stability) are intrinsic and non-removable. So the column is a *permanent* `rough-in` unless
  the methodology decides a composition-root may be `firm` over partial-obstruction constituents
  (the GMG column took the position that documented-sequential-obstructions inherited from a firm
  constituent do NOT gate the compositional firm claim — but there the blocking constituent was
  *firm*; here two are partial-obstruction). **FLAGGING for the batch-39 meta:** is a
  feature-column composing partial-obstruction iteration-views `rough-in` (well-foundedness
  `rank ≤ min(deps)`, my verdict) or `firm` (the GMG firm-on-positive-structure +
  documented-sequential-obstruction discipline, extended to partial-obstruction blocking deps)?
  I took the conservative well-foundedness reading (`rough-in`); the GMG precedent is the
  counter-argument. OQ `krylov-iteration-rough-in-vs-firm-over-partial-obstruction-iteration-views`.
- **reference-edge-liveness scheme evidence (the planner's required statement — see the report
  §Reference-edge-liveness scheme evidence above).** This column's RE2/RE8 discharge is a
  **`depends-on (composes)` root→node reachability flip** (the three L3 views should move OUT of
  STRONGER), NOT a reference-only-reachable artifact — mechanically distinct from the c122
  kernel-impl/combinator reference-only-reachable cohort. The integrator/meta should confirm on
  the rebuilt tree (re-run `graded_stack_lint.py --book-src book/src --json` and check
  `L3/krylov-step` / `L3/fold_solve` / `L3/orthogonalize` left STRONGER). If the GC does NOT flip
  them reachable, that is itself the headline scheme finding (a feature-root's outbound
  `depends-on` is not being traversed — a GC bug, not a modelling artifact).
- **The roadmap_goal coupling is wired `reference`, not `depends-on`.**
  [`eigsolve-impl`](../L3/eigsolve-impl.md) FOLDS this iteration spine (it is the downstream
  constructive-eigensolve consumer, per its own `depends-on (folds) → L3/krylov-step` +
  `L3/lanczos_step`); this column does NOT compose `eigsolve-impl`. So the coupling is a
  `reference` see-also (the drift-guard), not a blocking edge — forcing a `depends-on` here would
  be the §2g over-edge (and would pin the column to rank-0 roadmap_goal, which is wrong). The
  faithful direction is `eigsolve-impl →(folds)→ krylov-step ←(composes)← krylov-iteration`: both
  consume `krylov-step`, they are siblings over it, not a chain. NOTE for the c121 eigsolve-impl
  author / a future lifter: `eigsolve-impl` could add a `reference` see-also UP to this column
  (the iteration-rotation spine it folds) for symmetry — I did NOT edit `eigsolve-impl` (down-links
  are read-only; routed as this OQ). OQ `eigsolve-impl-reference-uplink-to-krylov-iteration-column`.
- **No L0 column file.** Like the GMG column, this infrastructure column has no
  `feature/krylov-iteration.L0.md` (the matrix L0 cell is `—`) — the L0 ground-truth is the
  cited driver source in the L4/L1 chapters' `cites-evidence` edges (`iterative.cpp`), not a
  separate L0 surface. The GMG column set this precedent (its matrix L0 cell is also `—`).
- **Slug confirmed:** `feature/krylov-iteration.{L4,L1}` (the planner's canonical working slug;
  no cleaner name surfaced — "krylov-iteration" reads cleanly as the iteration spine). Stated for
  the integrator.
```

I've authored the column. Here is my summary.

## Summary

**D2 complete — authored the new infrastructure feature column `feature/krylov-iteration.{L4,L1}`** (canonical slug kept; no cleaner name surfaced), the 2nd member of the Infrastructure / shared-substrate grouping alongside the GMG preconditioner. It is the **iteration-rotation spine** — the parallel of how GMG composes the smoother vocabulary, this column composes the L3 iteration-view vocabulary.

**RE2/RE8 DISCHARGE — real, via blocking `depends-on (composes)`.** I wired faithful `depends-on (composes)` edges from this `feature_root: seed` column to `L3/krylov-step` (firm), `L3/fold_solve` (partial-obstruction), and `L3/orthogonalize` (partial-obstruction). Per the planner's directive these are **blocking depends-on, not reference**, so the discharge is genuine: RE2 (`L3/orthogonalize`) and RE8 (`L3/krylov-step` + `L3/fold_solve`) are the exact baseline-exceptions whose discharge trigger is "a feature column composing the L3 iteration-rotation form by name."

**Column lands `rough-in`, NOT firm — faithful-or-finding.** Well-foundedness `rank(u) ≤ min(deps)` caps it at its least-resolved blocking constituent: two of the three iteration-views are `partial-obstruction` on disk (read from each chapter's `## Status` line, not the cycle record). This is the honest verdict — the iteration-rotation spine is *constitutively* the surface where the body-lifts-loop-doesn't obstruction lives (carry-threading + MGS recurrence + outer Krylov fold). The per-step bodies all lift, so it's a real rough-in composing real substrate, not a roadmap_goal.

**Reference-edge-liveness scheme evidence (for the batch-39 meta):** I stated explicitly that this discharge is a **`depends-on` root→node reachability FLIP** (the three views should leave STRONGER) — mechanically *distinct* from the c122 kernel-impl/combinator reference-only-reachable cohort. This is the clean second data class the planner wanted: a depends-on RE-discharge (reachable-flip), not a reference-only-reachable artifact. The roadmap_goal `eigsolve-impl`/`lanczos_step` are wired `reference` (the eigensolve FOLDS this spine — it's a downstream sibling over `krylov-step`, not a constituent; a `depends-on` there would be a §2g over-edge pinning the column to rank-0).

**Files (proposed-changes, NOT written to `book/`):** 2 new column files (`.L4`, `.L1`), plus edits to `feature/index.md` (matrix row), `feature/infrastructure.md` (member list + reference edges), and `SUMMARY.md` (nested grouping, high→low within-column).

**Key OQ flagged for the meta:** `krylov-iteration-rough-in-vs-firm-over-partial-obstruction-iteration-views` — whether a composition-root over partial-obstruction blocking deps is `rough-in` (my well-foundedness reading) or `firm` (the GMG firm-on-positive-structure precedent extended). The GMG case differs because its blocking constituent was *firm*; here two are partial-obstruction.

Report written to `/home/crutcher/git/palace_whiteroom/reports/2026-06-07T083902Z-layer-intro-author-krylov-iteration-column/CYCLE.md`.

