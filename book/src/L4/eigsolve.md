---
layer: L4
operator: eigsolve
firmness: firm
consumes:
  - book/src/L4/index.md (solve_loop / restart_cycle / Outcome — the firm c047 outer-driver vocabulary rows)
  - book/src/concepts/solve-monad.md (Solve = StateT SimState Identity; §Shape, §"Termination as a sum type" — the Outcome pattern this cap EXTENDS)
lowers_to:
  - book/src/L3/eigsolve.md (the partial-obstruction iteration-rotation view; in-line marker-erasure rotation, NO dedicated L4-L3 theme — the loop is opaque-library-owned, marked-not-rendered at both layers)
variant_axes:
  - eig-outcome-classification (Done Converged / Done (PartialConverged k) / Done MaxIterReached / Done LinearSolveFailed — the richer 4-arm sum; the PartialConverged arm has NO ksp_solve analog)
  - problem-type (linear EPS / quadratic PEP / nonlinear NEP — selects the operand-assembly the inner ksp_solve inverts; absorbed into OpParams)
  - spectral-transformation (none / shift-invert / shift-invert-precond — selects which operator op.inv inverts; absorbed into OpParams)
  - backend-orchestration (arpack-rci / slepc-st-shell — both opaque-library-owned loops; absorbed; the load-bearing fact for the obstruction marker)
  - element-type (complex only — Palace's EigenvalueSolver surface is complex-only; inherited from L1/L2/L3)
---

# eigsolve

The L4 **outer-driver cap** for the generalized eigenproblem: the `Solve`-monadic coordination that drives the eigen-iteration to convergence and classifies its richer termination once at the iteration boundary. Unlike its sibling cap [`ksp_solve`](./ksp_solve.md) (a clean `Solve`-monadic fold of a Palace-authored convergence-test loop), `eigsolve` at L4 is a **role-naming `Outcome`-wrapper over an opaque-library obstruction marker**: the eigen-iteration is entirely inside SLEPc `EPSSolve` / ARPACK `naupd` RCI, so the cap **names the iteration by role and marks the obstruction** — it does **not** render a Palace-authored loop, because Palace authors none. This is the L4 echo of the [`L3/eigsolve`](../L3/eigsolve.md) `partial-obstruction` status: the per-step body lifts (an `apply_shift_invert` whole-tensor composition); the eigen-iteration loop does not.

## Context

L4's job is to write algorithms in a graph-evaluation calculus that makes lifetimes, dispatch sites, and effect placement structural. `eigsolve` at L4 is the typed coordination shape that the `solve-monad` concept ([`solve-monad`](../concepts/solve-monad.md)) sketches in prose and that the `L4/index` dep-map anchors as the three firm outer-driver vocabulary rows (`solve_loop` / `restart_cycle` / `Outcome`). This chapter is the per-operator cap that *consumes* those rows — but it consumes them under the **opaque-library constraint**, which makes it shaped differently from the `ksp_solve` cap.

The load-bearing structural fact, carried forward from L3: **`eigsolve` has a lifting per-step body and a non-lifting loop, and the loop's non-lift is because Palace authors no loop.** Two consequences at the cap level:

- The **body** — the per-step shift-invert spectral-transform application `apply_shift_invert = apply_linop(op.operand) ▷ ksp_solve(op.inv) ▷ scale_untransform [▷ project]` — is a clean whole-tensor composition; it is identity-in-form across the L3↔L2 edge (per [`L3/eigsolve`](../L3/eigsolve.md) §"Lowers to" and the firm [`L2/eigsolve`](../L2/eigsolve.md) `apply_shift_invert` body). At L4 the body is what an *imagined* Palace-authored `iterate_while` fold would step.
- The **loop** — the Krylov-Schur restart, Arnoldi/Lanczos basis extension, Rayleigh-Ritz extraction, convergence test — is entirely **opaque-library-owned**, a witnessed [`sequential-obstruction`](../concepts/sequential-obstruction.md) rooted in opaque-library-ownership. There is **no Palace-authored eigen-step kernel / eigen-iteration driver pair** analogous to `(krylov-step, ksp_solve)`. So the cap **cannot** render the loop as `solve_loop` recursing a Palace `restart_cycle`; it names the fold by role (`eigen_iterate`) and marks the obstruction.

The relationship to the inner kernel is therefore **NOT** the clean driver-to-kernel pairing the `ksp_solve` cap has. There is no Palace-authored eigen-step body for the cap to fold; the body it *would* fold (`apply_shift_invert`) is handed to the library as an `ApplyOp` / `__pc_apply_EPS` callback, and the library owns the surrounding iteration. The cap's `solve_loop` analog is therefore a **single opaque library step** (`do { o <- eigen_iterate op inp; pure () }`), not a tail-recursion over Palace-authored cycles. This is stated explicitly because it is the central honest fact of the entry.

The cap is defined **in L4 vocabulary** (high→low discipline): its semantics, signature, and laws are stated in terms of the `Solve` monad, the `solve-monad` outer-driver surface, and the opaque-library obstruction — NOT in terms of L3 value-threading primitives. There is **no separate L4>L3 dissolution theme** for `eigsolve` (planner decision; the in-line convention for an opaque-library / no-removable-recurrence case — parallel to `chebyshev`'s in-line-by-design L4>L3). The rotation is a *marker-erasure*: the L4 cap marks the eigen-iteration obstruction; the L3 [`L3/eigsolve`](../L3/eigsolve.md) marks the same obstruction; the "rotation" between them is the erasure of the `Solve`/`EigOutcome` wrapper, recorded in-line in §"Lowers to".

`eigsolve` at L4 is a **methodology-level cap**, not a Palace-source artefact — there is no L0 source range that "is" the L4 `eigsolve`. The Palace evidence sits at L3 / L2 / L1 / L0 (the per-backend `Solve()` bodies, the `ApplyOp` / `__pc_apply_EPS` callbacks, the `EigenvalueSolver` base); L4 cites the L3 parent and the L1 collapse as its evidence base, plus the `solve-monad` concept for the outer-driver pattern and the strawman for the monad / loop / pruning conventions.

## Signature

The L4 cap signature is the `solve-monad` outer-driver shape, specialised to the opaque-library eigen-iteration and the richer termination sum. The entry point and its single opaque driver layer:

```text
-- entry point: run the outer driver over the initial SimState
eigsolve :: OpParams -> Inputs -> EigState
eigsolve op inp = execState (solve_loop op inp) (initial_eig_state inp)

-- outer driver: the eigen-iteration is OPAQUE — one library step, classified once
-- (NOT a tail-recursion of a Palace-authored restart_cycle; Palace authors no loop)
solve_loop :: OpParams -> Inputs -> Solve ()
solve_loop op inp = do
  o <- eigen_iterate op inp        -- OPAQUE library fold (SLEPc EPSSolve / ARPACK naupd RCI)
  classify_into_state o            -- fold the EigOutcome into EigState once at the boundary

-- the opaque eigen-iteration, named by ROLE only (a sequential-obstruction marker,
-- NOT a renderable Palace loop): folds the per-step apply_shift_invert body library-internally
eigen_iterate :: OpParams -> Inputs -> Solve EigOutcome

-- the per-step body the library folds (handed in as an ApplyOp / __pc_apply_EPS callback);
-- whole-tensor, LIFTS — identity-in-form to the firm L2/L3 apply_shift_invert composition
apply_shift_invert :: OpParams -> Tensor[(S: ...)] -> Tensor[$S]

-- the RICHER termination sum (the eigsolve-specific extension of the canonical Outcome)
data EigStatus = Converged | PartialConverged Int | MaxIterReached | LinearSolveFailed
data EigOutcome = Continue | Done EigStatus
```

Shape contract (bunsen-style; named records and axes; the operator-domain shape group `S` follows the named-shape-group convention of [`l4_calculus`](../semantics/index.md) §1.2.1 — `complex` is an element type, not an axis; the eigenvalue/error lists `Tensor[K, ...]` are genuine length-K; the same three strata per [`state-stratification`](../concepts/state-stratification.md) the `ksp_solve` cap uses, with `EigState` the eigsolve-specific persistent stratum):

- `OpParams` — operator-internal configuration, captured once at solve construction; `readonly` per [`state-stratification`](../concepts/state-stratification.md). Closes over the bound problem operators (`op.K`, `op.M`, optional `op.C` / `op.A2` per problem-type), the inner solver `op.inv` (the construction-bound [`ksp_solve`](./ksp_solve.md) inverting the shifted operator `(K − σM)`), the shift `σ` and spectral-transform mode (STSINVERT / STPRECOND), the optional divergence-free projector `op.projector`, the Higham scaling factors, the requested mode count `K_max`, tolerance, and iteration cap. The cap's driver does **not** branch on any `OpParams` field (problem-type, spectral-transformation, backend-orchestration are all absorbed per [`variant-absorption`](../concepts/variant-absorption.md) `readonly` typing); the body it hands to the library reads `op.operand` / `op.inv` only.
- `Inputs` — the per-solve inputs that seed `initial_eig_state` (the optional initial-subspace seed `control.initial_space`; when absent, the library generates its own by internal RNG). Read-only.
- `EigState` — externally-visible state that persists across the entire solve call. Per [`state-stratification`](../concepts/state-stratification.md), the eigsolve-specific persistent stratum: contains `pairs: [(λ: Complex, x: Tensor[(S: ...), complex])]` (the converged eigenpairs, the eigenvector `x` congruent to the operator domain shape group `S`, in original-problem coordinates — un-scaled), `converged: Int`, `requested: Int`, `error: Tensor[K, real]` (a genuine length-K list of per-pair errors), and the `EigStatus` terminal. Threaded by `Solve a = StateT EigState Identity a`; the cap's net effect is the `EigState` transition from `initial_eig_state inp` to the terminal state, extracted by `execState`. (This is the L4 typing of the firm L1 `EigResult` record, [`L1/eigsolve`](../L1/eigsolve.md) §Signature.)
- `eigen_iterate` — the **opaque-library eigen-iteration**, named by role only. It is **not** a Palace-authored loop and **not** renderable as a `solve_loop` tail-recursion of a Palace `restart_cycle` — it is a single library call (`EPSSolve`) or an RCI callback-dispatch loop (`naupd`) whose body is a callback dispatcher, not an algorithm. Recorded as a witnessed [`sequential-obstruction`](../concepts/sequential-obstruction.md) rooted in opaque-library-ownership. This is the structural contrast with the `ksp_solve` cap's `restart_cycle` (which IS Palace-authored).
- `apply_shift_invert` — the per-step body the library folds internally (handed in as the `ApplyOp` / `__pc_apply_EPS` callback). Whole-tensor by signature shape — `apply_linop(op.operand)` then inner `ksp_solve(op.inv)` then `scale_untransform` then optional `apply_linop(op.projector)`. It **lifts** (identity-in-form to the firm [`L2/eigsolve`](../L2/eigsolve.md) / [`L3/eigsolve`](../L3/eigsolve.md) body). It is a *plain function* the cap hands to the library, not a monadic effect — its only `EigState`-touching consequence is mediated through the library's basis management, which is opaque.
- `EigOutcome = Continue | Done EigStatus` — the **richer termination sum**, the eigsolve-specific extension of the canonical [`Outcome`](./index.md) (`Continue | Done Bool`). Where `ksp_solve`'s `Outcome` carries a soft-fail `Bool`, `eigsolve`'s `EigOutcome` carries the 4-arm `EigStatus`: `Converged` (all `K_max` pairs converged), `PartialConverged k` (`0 < k < K_max` — the partial-success arm with **no `ksp_solve` analog**, per [`L1/eigsolve`](../L1/eigsolve.md):78), `MaxIterReached` (`k = 0` at max-iter), `LinearSolveFailed` (the L1-constructive inner-solve-failure arm, per [`L1/eigsolve`](../L1/eigsolve.md):54). Classified **once** at the iteration boundary (post-`EPSSolve` / post-`naupd`), folded uniformly into `EigState.status`.
- `Solve a = StateT EigState Identity a` — the state monad ([`solve-monad`](../concepts/solve-monad.md)), here over `EigState`. The cap's effect domain is exactly `EigState`; the entry point discharges it via `execState`.

The shape contract makes three things structural at the cap level:

1. **Termination is a single typed decision site over a richer sum.** The four termination reasons are named arms of `EigStatus` and classified once at the iteration boundary, replacing the L1/L3 form's count-vs-request comparison the caller performs. The partial-success arm `PartialConverged k` is first-class — the load-bearing distinction from `ksp_solve`'s `Done Bool` (which has no partial-success notion: a linear solve either reaches a single solution or does not).
2. **The eigen-iteration is a marked obstruction, not a rendered fold.** The `Solve ()` typing and the `eigen_iterate :: ... -> Solve EigOutcome` role-signature make the opaque-library ownership structural: there is no Palace `restart_cycle` body inside the cap, only the role-named library call and the once-at-boundary classification. The body `apply_shift_invert` is structurally a `let`-bound plain function (the callback), not a monadic step.
3. **The per-step body lifts; the loop does not.** `apply_shift_invert` is whole-tensor (the body-half of the partial obstruction); `eigen_iterate` is the opaque-library loop-half. The cap states both at the coordination layer — the body is the firm L2/L3 composition, the loop is the marked obstruction.

## Semantics

`eigsolve` at L4 is the complete generalized-eigenproblem solve expressed as a `Solve`-monadic outer driver over an **opaque-library** eigen-iteration. The cap assembles the `solve-monad` vocabulary under the opaque-library constraint:

`solve_loop op inp` is the **outer driver** — but unlike the `ksp_solve` cap (where `solve_loop` tail-recurses a Palace-authored `restart_cycle` until an `Outcome` says stop), here `solve_loop` is a **single opaque library step followed by one classification**: `do { o <- eigen_iterate op inp; classify_into_state o }`. There is no tail recursion at the cap level because there is no Palace-authored per-cycle body to recurse — the entire restart / basis-extension / convergence structure is inside `eigen_iterate`. The cap names the iteration; it does not drive it step-by-step.

`eigen_iterate op inp` is the **opaque-library eigen-iteration**, named by role only and marked as a [`sequential-obstruction`](../concepts/sequential-obstruction.md):

- **SLEPc**: the entire iteration is one opaque call `EPSSolve(eps)` (`palace/linalg/slepc.cpp:694`, inside `SlepcEPSSolverBase::Solve`, `:687-709`). Palace supplies only the PC-shell callback (`__pc_apply_EPS`) and the A0/A1 shell matvecs; SLEPc's `STSINVERT` machinery composes them. There is no Palace loop at all.
- **ARPACK**: the iteration is a reverse-communication-interface (RCI) loop — Palace's `while(true)` (`palace/linalg/arpack.cpp:315-339`) calls the opaque ARPACK driver `naupd` (`palace/linalg/arpack.cpp:318`) and dispatches the per-step body callback `ApplyOp` only on the reverse-communication tag `ido == 1 || ido == -1`, breaking on `ido == 99`. The loop body is a callback dispatcher, not an algorithm — all eigen-iteration logic is inside `naupd`.

The per-step body the library folds is `apply_shift_invert` — the whole-tensor composition `apply_linop(op.operand) ▷ ksp_solve(op.inv) ▷ scale_untransform [▷ project]` (witnessed `opM->Mult(x1, z1); opInv->Mult(z1, y1); y1 *= gamma` at `palace/linalg/arpack.cpp:579-581`; the SLEPc `__pc_apply_EPS` realization at `palace/linalg/slepc.cpp:1847-1876`). This **lifts** (identity-in-form to the firm L2/L3 body); the cap hands it to the library as a callback and the library owns the surrounding fold.

`EigOutcome` classification happens once, at the iteration boundary (post-`EPSGetConverged` / post-`neupd`), against the converged-pair count: `Converged` when `K_max` pairs converged, `PartialConverged k` when `0 < k < K_max`, `MaxIterReached` when `k = 0`, `LinearSolveFailed` for the L1-constructive inner-solve-failure case. The `EigStatus` folds uniformly into `EigState.status`. This is the eigsolve specialisation of the `solve-monad` §"Termination as a sum type" classify-once / fold-uniformly law — extended from a `Bool` to a 4-arm sum.

The cap's **net effect** is the `EigState` transition discharged by `execState`: `eigsolve op inp` projects the terminal `EigState` (whose `.pairs` hold the `K = converged` eigenpairs in original-problem coordinates, whose `.converged` / `.requested` / `.error` / `.status` are the readout fields) out of the `solve_loop op inp` action run from `initial_eig_state inp`. The eigenpair extraction (un-transform `λ = l * gamma` per `palace/linalg/slepc.cpp:711-716`, normalize, residual, count→status) is the firm L1 readout, lifted to the `EigState` terminal. The cumulative inner-solver statistics counters are driver-side accumulators above the cap (the same treatment as the `ksp_solve` cap), not part of the `Solve` effect.

The result is determined by `(op, inp)` modulo the four load-bearing non-determinism sources the firm L1 entry catalogs (reduction-tree non-associativity in the inner BLAS-1 ops, per-backend floating-point ordering, inner-`ksp_solve` non-determinism propagated to the outer eigensolve, library-internal RNG for initial-space generation). The cap inherits these through the lifting `apply_shift_invert` body (whose inner `ksp_solve` is itself non-deterministic) and through the opaque library loop (whose basis management and RNG are library-internal).

### No demand-pruning interaction at the cap level

The `ksp_solve` cap carries a demand-pruning interaction (the per-step residual trajectory prunes when no consumer reads it). For `eigsolve` there is **no Palace-visible per-step observation point** — the eigen-iteration consumes the transformed vector and produces no per-step Palace readout (the only Palace observation is post-loop, at `EPSGetConverged` / `RescaleEigenvectors`, per [`L3/eigsolve`](../L3/eigsolve.md) §"Algebraic laws"). So the demand-pruning law statable at the `ksp_solve` cap is **not statable here** — the trajectory is library-internal and never surfaces to a Palace demand site. This absence is itself a consequence of the opaque-library ownership.

## Algebraic laws

`eigsolve` is a **monadic outer driver over an opaque-library obstruction**, not an algebra. The laws below are (a) the cap's coordination identities (the `execState`/`StateT` discharge fusion) and the `EigOutcome` classify-once law, and (b) the body-composition + fold-terminal laws inherited from the firm L1/L2/L3 entries. Absences are catalogued explicitly — and the central absence (the loop does not lift / does not render) is the load-bearing non-law that drives the cap's role-naming shape.

1. **`execState`/`StateT` discharge fusion** (the cap's defining identity). `eigsolve op inp = execState (solve_loop op inp) (initial_eig_state inp)` — the cap *is* the `execState`-discharge of the `solve_loop` action. The threaded `EigState` is projected and the `()` value discarded. **Consequence**: the cap's observable result is exactly the terminal `EigState` (the `EigResult`-shaped readout); there is no residual monadic structure. This makes the cap a *pure function* `(op, inp) -> EigState` despite the internal `StateT` threading (modulo the inherited non-determinism sources). Identical in form to the `ksp_solve` cap's law 1, over `EigState` rather than `SimState`.

2. **`apply_shift_invert` body-composition identity** (exact; the load-bearing body law, lifted from [`L2/eigsolve`](../L2/eigsolve.md) law 1 / [`L3/eigsolve`](../L3/eigsolve.md) law 1). The per-step body the cap hands to the library factors exactly as `apply_shift_invert(op, v) = scale_untransform(ksp_solve(op.inv, apply_linop(op.operand, v)))` (optional projector tail). This is a syntactic identity read from `ArpackEPSSolver::ApplyOp` (`palace/linalg/arpack.cpp:579-581`) and the SLEPc `__pc_apply_EPS` realization (`palace/linalg/slepc.cpp:1847-1876`). **Consequence**: the body is the firm L2/L3 composition, expressed at L4 as the callback the cap supplies. It is whole-tensor (it lifts); this is the body-half of the partial obstruction at the cap layer.

3. **`EigOutcome` classify-once / fold-uniformly** (the sum-type coordination law, the eigsolve **extension** of the canonical `Outcome` law from [`solve-monad`](../concepts/solve-monad.md) §"Termination as a sum type"). The four termination reasons are classified at exactly one site (the iteration boundary), and the `EigStatus` folds uniformly into `EigState.status`. **Consequence**: there is no termination-reason information lost or duplicated across the coordination layer — the multi-reason classification (including the partial-success arm) is a single total function `(converged, requested) -> EigStatus`. This is the law that **extends** the `ksp_solve` cap's `Outcome` law: `ksp_solve` classifies into `Done Bool`; `eigsolve` classifies into `Done EigStatus` with a first-class `PartialConverged k` arm (`0 < k < requested`) that the `Bool` sum cannot express (per [`L1/eigsolve`](../L1/eigsolve.md):78). The richer sum is registered as the `EigOutcome` L4 row (a clean addition, not an override of `Outcome`).

4. **Eigenvalue defining equation at the cap terminal** (modulo tolerance; the load-bearing terminal law, lifted from [`L1/eigsolve`](../L1/eigsolve.md) law 1 and [`L3/eigsolve`](../L3/eigsolve.md) law 3). For each converged pair `(λᵢ, xᵢ)` in `(eigsolve op inp).pairs`, the relevant eigenvalue equation holds approximately — linear: `apply_linop(op.K, xᵢ) ≈ λᵢ · apply_linop(op.M, xᵢ)`; quadratic / nonlinear per [`L1/eigsolve`](../L1/eigsolve.md) §Semantics. Exact in the limit `tol → 0`, `max_it → ∞`. The returned `λᵢ` are in original-problem coordinates (the un-transform `l * gamma` performed at the L0 accessor, `palace/linalg/slepc.cpp:711-716`), regardless of spectral-transformation mode.

5. **Eigenvector normalisation at the cap terminal** (exact). Each `xᵢ` in `(eigsolve op inp).pairs` satisfies `‖xᵢ‖₂ = 1` (`op.B = Nothing`) or `xᵢᴴ B xᵢ = 1` (`op.B = Just B`), enforced by the library `RescaleEigenvectors` step ([`L1/eigsolve`](../L1/eigsolve.md) law 2). A post-condition on the `EigState` terminal, not a property of the (opaque) iteration.

Laws that explicitly **do not** hold:

- **Eigen-iteration loop lift / render** (the load-bearing non-law — the reason the cap is a role-wrapper, not a fold). The eigen-iteration fold does **not** lift to a tensor-field op, **and does not render as a Palace-authored `solve_loop`/`restart_cycle` tail-recursion**, because Palace authors no loop — it is inside `EPSSolve` (`palace/linalg/slepc.cpp:694`) / `naupd` (`palace/linalg/arpack.cpp:318`). This is the **opaque-library [`sequential-obstruction`](../concepts/sequential-obstruction.md)** — the loop-half of the partial obstruction, carried up from [`L3/eigsolve`](../L3/eigsolve.md). The cap names the obstruction; the `Solve` monad does not remove it. (Contrast the `ksp_solve` cap, whose `solve_loop` IS a tail-recursion of a Palace `restart_cycle` and degenerates to `iterate_while_pure`; `eigsolve` cannot make that move.)
- **Per-step body observability / demand-pruning** (stated above, §"No demand-pruning"). No Palace-visible per-step observation point; the trajectory is library-internal. The demand-pruning law statable at the `ksp_solve` cap is not statable here.
- **Outer-cycle fold-merge / restart associativity.** The library Krylov-Schur restart re-seeds the basis; iterating two restart cycles is not iterating one double-length cycle. The cap cannot assert restart-associativity because the restart is library-internal (strengthened from the `ksp_solve` cap non-law, where Palace authors the restart — here Palace authors none at all). Inherited from [`L3/eigsolve`](../L3/eigsolve.md).
- **Determinism of `K_max` truncation.** Increasing the requested mode count rebuilds the (library-internal) Krylov basis differently; the first `K` returned pairs are not preserved. The cap cannot assert otherwise (library-owned basis). Inherited from [`L1/eigsolve`](../L1/eigsolve.md).
- **Eigenvalue ordering.** The returned eigenvalues are in the library's internal convergence order; any sort is a downstream concern. Inherited from [`L1/eigsolve`](../L1/eigsolve.md) / [`L3/eigsolve`](../L3/eigsolve.md).
- **Bit-determinism across backend-orchestration / reduction-tree / initial-space variants.** Inherited transitively through `apply_shift_invert`'s inner `ksp_solve` and the library RNG; the two backends fold the same body at different floating-point orderings. Load-bearing per CLAUDE.md §"Optimization tricks vs. base algebra". The `Solve` monad's `EigState` threading does not introduce a determinising identity.
- **`LinearSolveFailed` positive observability.** The `LinearSolveFailed` arm is L1-constructive (introduced to make the inner-solve coupling visible; no positive L0 site — the inner `opInv->Mult` is `void` and unqueried, per [`L1/eigsolve`](../L1/eigsolve.md):54). At the cap it remains constructive: a future `eigsolve-mutation-rotation` L1>L0 materialisation plumbs `ksp->GetConverged()` / SLEPc `EPSConvergedReason`. The cap carries it as a first-class `EigStatus` arm but does not assert current L0 instantiations produce it.

## Dependencies

L4 outer-driver vocabulary (the firm c047 rows this cap consumes — `book/src/L4/index.md` §Vocabulary-cohort "`solve-monad` outer-driver vocabulary"):

- `solve_loop` — the outer driver the cap's entry point runs (`execState (solve_loop op inp) …`). Here specialised to a single opaque library step + classification (no Palace tail-recursion).
- `restart_cycle` — consumed by *role contrast only*: the cap names where a Palace `restart_cycle` would sit (`eigen_iterate`) and marks that Palace authors none. The `ksp_solve` cap consumes `restart_cycle` substantively; the `eigsolve` cap consumes it as the absent-analog reference.
- `Outcome` — the canonical 3-arm termination sum the cap **extends** to `EigOutcome` (the 4-arm `Continue | Done EigStatus`). The cap consumes the `Outcome` *pattern* (classify-once / fold-uniformly) and specialises the sum.

L4 row dependencies:

- `EigOutcome` — the richer termination sum the cap produces and classifies (the eigsolve-specific extension of `Outcome`; registered as this cap's own L4 dep-map row).
- [`ksp_solve`](./ksp_solve.md) — the sibling cap, and the **inner solver** `op.inv` the per-step body `apply_shift_invert` invokes (the construction-bound `ksp_solve` inverting the shifted operator). The cap composes two layers of solver-as-operator: the eigsolve cap drives an opaque library iteration whose per-step body itself folds a `ksp_solve`.
- [`iterate-while`](./iterate-while.md) — referenced by *role contrast only*: the combinator an *imagined* Palace-authored eigen-iteration loop would use (per `book/src/semantics/index.md`). Since the loop is library-owned, the cap does **not** consume `iterate-while` substantively — it marks the obstruction instead.

L4 concept references:

- [`solve-monad`](../concepts/solve-monad.md) — the `Solve a = StateT EigState Identity a` outer-driver pattern; §"Termination as a sum type" (the `Outcome` classify-once law this cap extends to `EigOutcome`).
- [`state-stratification`](../concepts/state-stratification.md) — the three-stratum (`EigState` / `OpParams` / library-internal-ephemeral) typing; the eigen-iteration's ephemeral basis is library-owned (not even a Palace `let`-bound bundle).
- [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the opaque-library eigen-iteration obstruction the cap marks at the coordination layer (the load-bearing concept for this entry).
- [`tensor-field-lift`](../concepts/tensor-field-lift.md) — the body-lifts-but-loop-doesn't partial case.
- [`variant-absorption`](../concepts/variant-absorption.md) — the problem-type / spectral-transformation / backend-orchestration absorption into `op` (`readonly` typing); none of the cap's axes shape the driver body.
- [`constructed-operators`](../concepts/constructed-operators.md) — the shifted operator `(K − σM)` the inner solve inverts is a constructed operator; the spectral-transform binding is its construction.
- [`solver-as-operator`](../concepts/solver-as-operator.md) — the inner `ksp_solve` consumed as an operator (the shift-invert action).
- [`convergence-test`](../concepts/convergence-test.md) — the stopping-predicate surface the `EigOutcome` classification reads (here library-internal — the threshold relationship is delegated to SLEPc/ARPACK, per [`L1/eigsolve`](../L1/eigsolve.md) §"Algebraic laws").

**Strawman reference**: `book/src/semantics/index.md` §3.3–3.4 (monad / state-effect laws), §3.7 (`iterate_while` small-step — the loop the eigen-iteration would fold *if* Palace authored it; it does not), §3.8 (demand-pruning — not statable here, no per-step observation point) are the conventions source for this cap's laws.

## Lowers to

L4 `eigsolve` lowers to L3 [`eigsolve`](../L3/eigsolve.md) (`partial-obstruction`, cycle-024) via an **in-line marker-erasure rotation — NOT a dedicated `L4-L3/eigsolve-*` theme** (planner decision this cycle; the in-line convention for an opaque-library / no-removable-recurrence case, parallel to `chebyshev`'s in-line-by-design L4>L3). The rotation is recorded here in-line per the high→low discipline:

- **The `Solve`/`EigState` monad dissolves** to explicit positional value-threading (the L3 per-step body is already in explicit positional form; [`L3/eigsolve`](../L3/eigsolve.md) §"Value-threaded form").
- **The `EigOutcome` sum dissolves** to the L3 fold-terminal readout (the `count→EigStatus` structural map at extraction; [`L3/eigsolve`](../L3/eigsolve.md) §Semantics phase 3).
- **The `eigen_iterate` obstruction marker is preserved, not rendered** — this is the *marker-erasure* (the cap's `Solve`-wrapped role-naming collapses to the L3 `eigen_iterate` named-by-role obstruction marker; both layers mark the same opaque-library `sequential-obstruction`, so the "rotation" between them is the erasure of the monadic wrapper, not a loop-rendering). The body `apply_shift_invert` is identity-in-form across the hop (it lifts at both layers).

Because the rotation is a marker-erasure over an opaque-library obstruction (no Palace loop to render, no removable recurrence), a dedicated L4>L3 theme would carry no rewrite content beyond the wrapper-erasure already stated — hence the in-line treatment. The firm L3 image is [`L3/eigsolve`](../L3/eigsolve.md), whose own §"Lowers to" carries the further L3>L2 hop ([`L3-L2/eigsolve-opaque-eigen-iteration`](../L3-L2/eigsolve-opaque-eigen-iteration.md), firm — the opaque-library erasure-scope root).

## Variant axes

Five axes; the load-bearing one (eig-outcome-classification) is coordination-shaping, the rest are absorbed into `OpParams`:

1. **eig-outcome-classification** (`Done Converged | Done (PartialConverged k) | Done MaxIterReached | Done LinearSolveFailed`) — the load-bearing cap axis: the 4-arm `EigStatus` sum into which the cap classifies the post-iteration count. The **`PartialConverged k` arm (`0 < k < requested`) has no `ksp_solve` analog** — it is the eigsolve-specific extension of the canonical `Outcome` ([`L1/eigsolve`](../L1/eigsolve.md):78 — the substantive partial-success-arm anchor; [`L3/eigsolve`](../L3/eigsolve.md):166, the `solve-monad` dependency bullet, supports only the general "richer than soft-fail" theme). `LinearSolveFailed` is L1-constructive ([`L1/eigsolve`](../L1/eigsolve.md):54). Registered as the `EigOutcome` L4 row — a clean addition extending the `Outcome` pattern, not an override.
2. **problem-type** (`linear | quadratic | nonlinear`) — selects the operand-assembly the inner `ksp_solve` inverts (linear `(K − σM)`; quadratic PEP block `(L₀ − σL₁)`; nonlinear NEP per-`λ` operator). Absorbed into `OpParams`; the cap driver does not branch.
3. **spectral-transformation** (`none | shift-invert | shift-invert-precond`) — selects which operator `op.inv` inverts and what `op.operand` feeds the body. Absorbed into `OpParams`.
4. **backend-orchestration** (`arpack-rci | slepc-st-shell`) — the same body assembled two ways, **both loops opaque-library-owned** (the load-bearing fact for the obstruction marker). Absorbed into `OpParams`; collapsed to the single role-named `eigen_iterate`.
5. **element-type** (`complex only`) — Palace's `EigenvalueSolver` surface is complex-only (inherited from L1/L2/L3). No real-element variant.

These differ from the `ksp_solve` cap's axes in two structural ways: (a) the outcome axis is a **4-arm** sum (vs `ksp_solve`'s 2-arm `Done Bool`), with the partial-success arm load-bearing; (b) there is **no restart-shape axis** that selects a Palace per-cycle verb — the restart is library-internal, so backend-orchestration (which is absorbed, not coordination-shaping) takes its structural place.

## Status

`firm` — the `Solve`-monadic outer-driver cap `eigsolve op inp = execState (solve_loop op inp) initial_eig_state` is the canonical top-of-stack coordination shape for the generalized eigenproblem, consuming the firm c047 `solve-monad` vocabulary under the **opaque-library constraint**. The cap is honestly a **role-naming `EigOutcome`-wrapper over an obstruction marker**, not a clean `iterate_while` fold: the eigen-iteration is opaque-library-owned (SLEPc `EPSSolve` `palace/linalg/slepc.cpp:694`; ARPACK `naupd` RCI `palace/linalg/arpack.cpp:318`), so the cap names the iteration by role (`eigen_iterate`) and marks the [`sequential-obstruction`](../concepts/sequential-obstruction.md) — it does not render a Palace loop because Palace authors none. This is the L4 echo of the [`L3/eigsolve`](../L3/eigsolve.md) `partial-obstruction` status (the cap is firm *as a cap*; the obstruction it carries is the same one L3 carries — the cap's firmness is in its coordination apparatus and the body/loop split, not in a claim that the loop lifts).

The algebraic content is the cap's coordination identities (the `execState`/`StateT` discharge fusion, the `EigOutcome` classify-once law extending the canonical `Outcome`) plus the body-composition + fold-terminal laws (the `apply_shift_invert` body identity, the eigenvalue defining equation, the normalisation post-condition) inherited from the firm L1/L2/L3 entries, with the opaque-library eigen-iteration recorded as the load-bearing non-lift / non-render. The **load-bearing eigsolve-specific addition** is the richer `EigOutcome` sum with a first-class `PartialConverged k` arm (no `ksp_solve` analog), registered as the cap's own L4 dep-map row. The variant-axis profile is closed at five axes (one coordination-shaping — the 4-arm outcome; four absorbed).

The pattern is well-attested: the `partial-obstruction` L3 parent ([`L3/eigsolve`](../L3/eigsolve.md); L0 bodies ARPACK `ApplyOp` `palace/linalg/arpack.cpp:562-590`, SLEPc `__pc_apply_EPS` `palace/linalg/slepc.cpp:1847-1876`; opaque loops `EPSSolve` `:694` / `naupd` `:318`), the firm L2 named composition ([`L2/eigsolve`](../L2/eigsolve.md)), the firm L1 collapse ([`L1/eigsolve`](../L1/eigsolve.md)), the `solve-monad` concept, and the strawman conventions. This dispatch (cycle-048 R3) is the **L4 driver-half cap** consuming the cycle-047 outer-driver vocabulary anchor; it closes the `eigsolve` half of OQ `l4-ksp-solve-eigsolve-caps-gated-on-solve-monad-outer-driver-vocabulary` and re-anchors the seven stale "no L4 cap" assertions in [`L3/eigsolve`](../L3/eigsolve.md) (§Upward sites). There is **no dedicated L4>L3 dissolution theme** (the rotation is an in-line marker-erasure over the opaque-library obstruction); the relationship is recorded in-line in §"Lowers to".

## L4 vs L3 distinction

- **L3**: value-threaded iteration-rotation view (`partial-obstruction`). The per-step body `apply_shift_invert` is rendered as a whole-tensor value-threaded expression (lifts); the eigen-iteration loop is rendered as an **explicit obstruction marker** — `eigen_iterate` named by role with a cited opaque-library `sequential-obstruction` (the loop does not lift, and cannot even be rendered as a tail recursion because Palace authors no loop). No `Solve` monad, no `EigOutcome` sum (the soft-fail is the L1 `EigStatus` flag), no `readonly` typing.
- **L4**: `Solve`-monadic outer-driver cap `eigsolve op inp = execState (solve_loop op inp) initial_eig_state`. The coordination is typed — `solve_loop` threads `EigState` through the `Solve = StateT EigState Identity` monad; the eigen-iteration is a role-named `Solve EigOutcome` obstruction marker (NOT a Palace `restart_cycle` tail-recursion); termination is the richer `EigOutcome` sum classified once; `OpParams` is `readonly`. The L4>L3 marker-erasure (in-line) erases the monad and the sum-type wrapper, recovering the L3 explicit obstruction-marked form.

## Evidence

`eigsolve` at L4 is a methodology-level cap; Palace's C++ source does not realise the L4 form. The L0 evidence is transitive through the `partial-obstruction` L3 parent and the firm L2/L1 entries; the cap-level coordination apparatus is evidenced by the `solve-monad` concept and the strawman, and the opaque-library obstruction is evidenced by the SLEPc `EPSSolve` / ARPACK `naupd` call sites. Citations self-verified against source this dispatch (codemap `read_range` against on-disk).

- `book/src/L3/eigsolve.md` (cycle-024, `partial-obstruction`) — the L3 parent this cap lowers to (in-line marker-erasure). Its §Semantics names the body-lifts / loop-doesn't split; its §"Iteration-rotation marker" cites the opaque-library `sequential-obstruction`; its `EigStatus`-via-count readout is the L3 image of the cap's `EigOutcome` classification. The marker-erasure target.
- `book/src/L2/eigsolve.md` (cycle-023 firm) — the named `apply_shift_invert` composition the cap's body law restates; the L2↔L1 non-identity edge.
- `book/src/L1/eigsolve.md` (cycle-022 firm) — the opaque collapse; the `EigStatus` sum (`:51`), the partial-success arm (`:78` — the distinguishing feature with no `ksp_solve` analog), the `LinearSolveFailed` L1-constructive arm (`:54`), the `EigResult` readout (`:32-49`) the cap's `EigState` terminal lifts, the five fixed-point laws the cap restates as terminal laws.
- `book/src/L4/ksp_solve.md` (cycle-048 R2, D1 wave-1 — same-cycle sibling) — the sibling clean-fold cap; the structural contrast (Palace-authored `restart_cycle` fold vs this cap's opaque-library obstruction marker); the shared `solve-monad` vocabulary + the `Outcome` pattern this cap's `EigOutcome` extends. (Same-cycle co-land; cross-ref live at finalize.)
- `book/src/L4/krylov-step.md` (cycle-006 firm) — the L4 chapter altitude/structure precedent.
- `book/src/concepts/solve-monad.md:1-68` — the outer-driver pattern: §Shape (`:5-17`), §"Termination as a sum type" (`:58-68`, the `Outcome` classify-once / fold-uniformly law this cap extends to `EigOutcome`).
- `book/src/concepts/sequential-obstruction.md` — the opaque-library eigen-iteration obstruction the cap marks (the load-bearing concept).
- `book/src/semantics/index.md` — L4 strawman; §3.3–3.4 (monad / state-effect laws), §3.7 (`iterate_while` — the loop the eigen-iteration would fold *if* Palace authored it; library-owned, so the cap marks the obstruction instead).
- L0 anchors (transitive via the L3 parent; codemap-verified this dispatch against on-disk):
  - `palace/linalg/slepc.cpp:694` — `EPSSolve(eps)`, the entire SLEPc eigen-iteration as one opaque library call (inside `SlepcEPSSolverBase::Solve`, `:687-709`). The decisive negative anchor: no Palace loop at all.
  - `palace/linalg/slepc.cpp:711-716` — `SlepcEPSSolverBase::GetEigenvalue`: `EPSGetEigenvalue(eps, i, &l, nullptr)` then `return l * gamma` — the eigenvalue un-transform at the extraction boundary (the cap's original-problem-coordinate readout).
  - `palace/linalg/slepc.cpp:1847-1876` — `__pc_apply_EPS`: the SLEPc per-step body that LIFTS (`ctx->opInv->Mult(ctx->x1, ctx->y1)` inner solve + un-scale + optional projector tail).
  - `palace/linalg/arpack.cpp:318` — `naupd(...)`, the opaque ARPACK RCI driver (inside the `while(true)` loop `:315-339`); the per-step body callback `ApplyOp` is dispatched only on `ido == 1 || ido == -1`, breaking on `ido == 99`. The decisive negative anchor: Palace's loop body is a callback dispatcher, not an algorithm.
  - `palace/linalg/arpack.cpp:562-590` — `ArpackEPSSolver::ApplyOp`: the ARPACK per-step body that LIFTS (shift-invert branch `opM->Mult(x1, z1); opInv->Mult(z1, y1); y1 *= gamma` at `:579-581`; optional projector tail `opProj->Mult(y1)` at `:586`).
- Cap-half OQ closure: OQ `l4-ksp-solve-eigsolve-caps-gated-on-solve-monad-outer-driver-vocabulary` (`eigsolve` half) + the seven `L3/eigsolve` §Upward floor-landing re-anchors.
