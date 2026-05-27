---
agent: harvester
invoked_at: 2026-05-27T160711Z
scope: L1 operator: ksp_solve
status: pending
inputs:
  - book/src/L0/kspsolver-base-class.md (cycle-006 L0 anchor)
  - book/src/concepts/solve-monad.md (cycle-002 concept page)
  - book/src/concepts/ksp_solve.md (early-cycle methodology concept page)
  - book/src/concepts/solver-as-operator.md (the type-rotation underwriting the L1 form)
  - book/src/L1/index.md (dep-map insertion point)
  - book/src/L1/apply_linop.md, axpy.md, dot.md, nrm2.md (firm-chapter precedent)
  - reference/palace/palace/linalg/ksp.hpp + ksp.cpp (BaseKspSolver class)
  - reference/palace/palace/linalg/iterative.hpp + iterative.cpp (IterativeSolver / CgSolver / GmresSolver / FgmresSolver)
  - reference/palace/palace/linalg/ksp.cpp:34-58 (KrylovSolver enum dispatch — implemented vs aborting)
  - reference/palace/palace/drivers/{electrostaticsolver,magnetostaticsolver,drivensolver}.cpp (call sites)
  - reference/palace/palace/linalg/divfree.cpp:175 (ksp->Mult call site inside DivFreeSolver)
  - sister-report: 2026-05-27T160550Z-harvester-iterate-while-family-L4 (codemap-pilot dispatch; no overlap with L1 work)
  - closes OQ: l1-ksp-solve-firm-up-anchor-ready (cycle-006)
status: integrated
integrated_at: 2026-05-27T17:17:02Z
integration_commit: 693f058
integration_notes: |
  Applied cycle-007 wave-1 per-report dispatch 2 of 6 at 17:30:00Z; finalized in batch cycle-007 at 17:17:02Z.
  Files created: book/src/L1/ksp_solve.md (first L1 op with structured opaque primary argument).
  Files edited: book/src/L1/index.md (Context bullet 6 added; Semantics motif 4 = Constructed-operator absorption added; Vocabulary cohort Firm 7→8; new ksp_solve dep-map row inserted after axpbypcz; Working Notes bullet added), book/src/SUMMARY.md (L1 Part insert after axpbypcz).
  3 OQs promoted: ksp-solve-concept-page-signature-update, ksp-solve-mutation-rotation-l1-l0-theme, l1-intro-refresh-after-constructed-operator-gate.
  Closes cycle-006 OQ l1-ksp-solve-firm-up-anchor-ready.
  L1 firm cohort: 7 → 8. Gate hits: 0.
---

# CYCLE: Formalize ksp_solve at L1

## Summary

Promote `ksp_solve` from speculative-concept-page-only status to a firm L1 operator chapter. The L0 anchor (`L0/kspsolver-base-class.md`, cycle-006) and concept-page anchor (`concepts/solve-monad.md`, cycle-002; plus the pre-existing methodology-era `concepts/ksp_solve.md`) are both in place, closing the OQ `l1-ksp-solve-firm-up-anchor-ready` from cycle-006. The L1 form rotates Palace's `BaseKspSolver<OperType>::Mult(b, y)` in-place pattern into a pure functional `ksp_solve :: (Solver[A], Vector[N]) -> SolveResult[N]`: the destination buffer drops out of the signature, scratch workspace (per-method `r`, `z`, `p`, Krylov basis `V`, Hessenberg `H`) disappears, the statistics counters (`ksp_mult`, `ksp_mult_it`) become driver-side concerns, and the convergence-warning side channel becomes a structured `SolveResult` field. Per-method enum dispatch (CG / GMRES / FGMRES, three of the six `KrylovSolver` enum cases) is variant-absorbed: the L1 signature exposes one operator whose internal Krylov method is bound at construction. The three unimplemented cases (MINRES / BICGSTAB / DEFAULT — `palace/linalg/ksp.cpp:53-57`) remain L1>L0 obstruction-theme territory per the unimplemented-Palace-stub policy and are **not** part of this firm operator's surface.

## Proposed changes

```edit:book/src/L1/ksp_solve.md
# ksp_solve

Mutation-lifted preconditioned Krylov solve: `(x, status) = ksp_solve(K, b)` where `K` is a construction-bound Krylov-solver value carrying its system operator, preconditioner, tolerances, and iteration budget. The constructed-operator gate at L1 — the bridge from BLAS-1 vocabulary (`axpy`, `dot`, `nrm2`, `apply_linop`) to the L2 `krylov-step` vocabulary; the canonical realisation of the *solver-as-operator* type rotation.

## Context

The L0 source-side form is Palace's `BaseKspSolver<OperType>::Mult(b, x)` method composed with its construction-bound iterative solver and preconditioner. See [`L0/kspsolver-base-class`](../L0/kspsolver-base-class.md) for the complete C++ surface: the templated class, three constructors (config-driven, IoData-driven, move-in), the composition-wiring step (`palace/linalg/ksp.cpp:272`), `SetOperators` with its multigrid-finest special case, the central `Mult(b, x)` method, the cumulative statistics counters, and the `BlockTimer` RAII wrapping. See [`L0/ksp-factory-file`](../L0/ksp-factory-file.md) for the enum-routed dispatch (`KrylovSolver::CG` / `GMRES` / `FGMRES` implemented; `MINRES` / `BICGSTAB` / `DEFAULT` aborting at `palace/linalg/ksp.cpp:53-57`). See [`L0/apply-linop-overload-set`](../L0/apply-linop-overload-set.md) for the underlying `Mult` overload family the iterative solvers dispatch into per step.

At L0, the `Mult(b, x)` method writes the solution through the in-place destination `x` (with `x` simultaneously serving as the initial-guess source when `IterativeSolver::initial_guess` is true — see `palace/linalg/iterative.cpp:377-386`). Cumulative statistics counters mutate (`ksp_mult++`, `ksp_mult_it += ksp->GetNumIterations()`, `palace/linalg/ksp.cpp:308-309`). Non-convergence emits an `Mpi::Warning` log line (`palace/linalg/ksp.cpp:303-306`) but does not abort. Internal workspace tensors (`CgSolver::{r, z, p}` at `palace/linalg/iterative.hpp:144`; `GmresSolver::{V, r, H, s, sn, cs}` at `palace/linalg/iterative.hpp:190-194`; `FgmresSolver::Z` at `palace/linalg/iterative.hpp:256`) are mutable members of the per-method solver class, allocated lazily on first `Mult` call.

The L1 form drops the destination-buffer mention, lifts the statistics counters into driver-side concerns (the counters are *outside* the algebraic relationship "solve `A·x = b` for `x`"), structures non-convergence as a `SolveResult` field rather than a logged side effect, and erases the per-method enum dispatch — at L1 the operator-bound solver `K` is opaque about whether it is CG, GMRES, or FGMRES under the hood. Internal workspace, the in-place overwrite of `x`, the `BlockTimer` RAII, and the per-method initial-guess threading are all L0 concerns; they reappear (where they have to) in the L1>L0 lowering theme, not in the L1 signature.

A cross-cutting prose treatment lives at [`concepts/ksp_solve`](../concepts/ksp_solve.md) — covering the constructed-operator pattern, why this is the canonical *constructed-operator absorption* example (see also [`concepts/constructed-operators`](../concepts/constructed-operators.md) and [`concepts/variant-absorption`](../concepts/variant-absorption.md)), and slice-level use in the divfree projection. The type-level rotation that makes `K` substitutable for an `apply_linop`-style primitive is treated at [`concepts/solver-as-operator`](../concepts/solver-as-operator.md). The L4-bound monadic coordination layer the L1 form anchors is at [`concepts/solve-monad`](../concepts/solve-monad.md). The L1 entry here is the firm operator definition; the concept pages are the narrative.

## Signature

```
ksp_solve :: (K: Solver[A: LinearOperator[N, N]], b: Tensor[N]) -> SolveResult[N]

SolveResult[N] = {
  x          : Tensor[N],   -- approximate solution to A · x = b
  converged  : Bool,        -- whether the convergence test was satisfied
  iterations : Int,         -- number of inner Krylov iterations consumed
  initial_res: Real,        -- initial residual norm (per the solver's residual proxy)
  final_res  : Real         -- final residual norm (per the solver's residual proxy)
}
```

Shape contract (bunsen-style, named axes):

- `K` — `Solver[A]` — an opaque construction-bound Krylov-solver value. `A` is the system operator, a `LinearOperator[N, N]` (square). `K` additionally binds an optional preconditioner `M⁻¹` (also a `LinearOperator[N, N]`), a relative tolerance `rel_tol`, an absolute tolerance `abs_tol`, an iteration cap `max_it`, and (for restarted methods) a restart dimension `max_dim`. Read-only at the L1 call site. *All* per-method choices (CG vs GMRES vs FGMRES, preconditioner side for GMRES, orthogonalisation method, initial-guess use) are bound inside `K` at construction; the per-call surface is variant-free.
- `b` — `Tensor[N]` — the right-hand side. Read-only. Must match the operator's axis `N`.
- result — `SolveResult[N]` — record containing the solution `x` (same axis `N`) and the four solver-statistics fields. The `iterations`, `initial_res`, `final_res` fields are the per-call analogues of Palace's `IterativeSolver::final_it`, `initial_res`, `final_res` (`palace/linalg/iterative.hpp:53-55`); `converged` is the per-call analogue of `GetConverged()` (`palace/linalg/iterative.hpp:98`).

The system operator `A` is square (`N → N`); rectangular systems require a different L1 primitive (least-squares solve), not in this operator's scope. The system operator and the preconditioner share the same axis `N` (preconditioner is an approximate inverse of `A`, hence same domain/codomain). The element type of `b`, `K`, and the result `x` must all match (all real or all complex), realised at L0 by the `OperType ∈ {Operator, ComplexOperator}` template parameter on `BaseKspSolver`.

`Solver[A]` is an *opaque type* at L1: it has a system-operator axis `N`, an element type (real or complex), and is guaranteed to satisfy the convergence-test semantics below. Its internal Krylov method (CG / GMRES / FGMRES) and its internal preconditioner representation are not part of the L1 signature; the L1 entry collapses across all L0 representations.

## Semantics

`ksp_solve(K, b)` returns a `SolveResult` whose `x` field is an approximate solution to `A · x = b`, where `A` is the system operator bound inside `K`. The approximation quality is governed by `K`'s convergence test: a solve terminates and reports `converged = True` when the residual proxy `res` (method-specific — see Variant axes) falls below `eps = max(rel_tol · initial_res, abs_tol)`. If the iteration cap `max_it` is reached first, the solve terminates and reports `converged = False`; the returned `x` is the best iterate found, **not** an undefined value. **Non-convergence is soft-failure** at the L1 level (matching the L0 `Mult` behaviour at `palace/linalg/ksp.cpp:301-307`, which logs a warning but returns the iterate); callers that require hard-failure on non-convergence must check `result.converged` themselves.

The result is determined by `(K, b)` modulo two load-bearing non-determinism sources detailed below (reduction-tree non-associativity inherited from `apply_linop` / `dot`, and per-method iteration-step floating-point ordering). Modulo those, the L1 form is referentially transparent: applying the same `K` to the same `b` returns the same `SolveResult`.

The L0 source overwrites the in-place destination buffer `x`, with `x` simultaneously serving as the initial-guess source when `IterativeSolver::initial_guess` is true (`palace/linalg/iterative.cpp:377-386` for CG; analogous in GMRES at `iterative.cpp:557-571`). The L1 form **drops the initial guess from the signature**: the construction-bound `K` carries the choice of initial-guess policy as part of its opaque state, and the L1 `ksp_solve(K, b)` reports the solution unconditional on whether a warm start was used. This is a deliberate axis collapse: the initial-guess policy is a tuning knob that does not change the algebraic relationship `A · x ≈ b`; it changes only the residual proxy used as the convergence-test denominator and the per-call iteration count. The L1>L0 lowering theme is where the initial-guess threading is reintroduced.

The cumulative statistics counters `ksp_mult` / `ksp_mult_it` from `BaseKspSolver` (`palace/linalg/ksp.cpp:308-309`) are not part of the L1 operator — they are a *driver-side accumulator* over many `ksp_solve` calls, computed as the running sum over the per-call `iterations` field. The L1 form returns the per-call count in `SolveResult.iterations`; reconstructing the L0 cumulative counters is `Σ_calls result.iterations`. The same is true of `ksp_mult` (number of solves): at L1 each `ksp_solve` call counts as one; the cumulative-call counter is driver-side. This separation keeps the L1 operator referentially transparent (no mutable per-solver-instance state visible to callers) while preserving the information the counters expose.

The convergence-warning `Mpi::Warning` log line at `palace/linalg/ksp.cpp:303-306` is a side effect at L0 — it emits to the MPI-aware logger. At L1 the warning is not part of the operator's semantics: the L1 `SolveResult.converged` field carries the same information in a structured form, and any caller-side warning emission is the caller's concern. This is the same pattern as the [`L1/dot`](./dot.md) treatment of MPI collectives: the L1 form is single-rank-scope per CLAUDE.md, and the logger / collective surfaces are L1>L0 lowering concerns.

Reduction-tree non-associativity is **load-bearing** in the CLAUDE.md sense, inherited transitively through the inner-loop primitives. Every Krylov iteration consumes `apply_linop` (matrix-vector products), `dot` (inner products for orthogonalisation coefficients and residual norms), and `axpy` / `axpby` (vector updates). Each of these has its own load-bearing reduction-tree pinning recorded in its L1 entry (see [`L1/apply_linop`](./apply_linop.md) "Algebraic laws", absence section; [`L1/dot`](./dot.md) "Semantics" paragraph 3; [`L1/nrm2`](./nrm2.md) likewise). The composite effect inside `ksp_solve` is that the per-call iteration count and the per-call final residual depend on the underlying reduction-tree at the bit level; the converged solution `x` itself differs by quantities bounded by the operator's condition number and the working precision. This is recorded here, not erased.

A second load-bearing non-determinism source is **per-method iteration-step ordering** for non-symmetric Krylov methods (GMRES / FGMRES): the orthogonalisation method (MGS vs CGS vs CGS2 — see `palace/linalg/iterative.hpp:184`) changes the per-step floating-point arithmetic. This is collapsed into `K`'s opaque state at L1 (the orthogonalisation method is bound at construction), but the choice affects the bit-level result. Algorithmic correctness is preserved across choices; bit-determinism is not.

Per-method variants (CG / GMRES / FGMRES) are **not** separate L1 operators (per the Variant axes section below). The L1 form collapses across all three; the L1>L0 lowering theme reintroduces the per-method body (see [`L2/krylov-step`](../L2/krylov-step.md), the upstream layer that exposes the per-iteration body as a distinct primitive).

## Algebraic laws

The laws below hold; absences are deliberate. All laws are **modulo the convergence tolerance**: equalities are in the limit of `rel_tol → 0`, `abs_tol → 0`, `max_it → ∞`, treating `K` as a function `b ↦ A⁻¹ · b` (its formal mathematical interpretation). Finite-tolerance behaviour is captured by the explicit caveats noted with each law.

1. **Linearity in `b`** (modulo tolerance and finite precision): `ksp_solve(K, α·b₁ + β·b₂).x ≈ α·ksp_solve(K, b₁).x + β·ksp_solve(K, b₂).x` for any scalars `α`, `β` and any vectors `b₁`, `b₂` in the codomain of `A`. This follows from the linearity of `A⁻¹` for any invertible linear operator `A`. The approximation is exact in the formal limit and approximate at any finite tolerance; the gap is bounded by the operator's condition number. The `iterations`, `initial_res`, `final_res`, `converged` fields are **not** linear (different RHSes generate different residual histories and may take different iteration counts).
2. **Zero RHS gives zero solution** (exact, not modulo tolerance): `ksp_solve(K, 0).x = 0`. The Krylov iteration with zero RHS and zero initial guess produces a zero iterate in one step; with a non-zero initial guess and zero RHS the solver converges to zero (assuming `A` is invertible). This law is special-cased in the L0 implementation by short-circuiting on `initial_res == 0` (`palace/linalg/iterative.cpp:418-419`).
3. **Operator inverse on the RHS** (modulo tolerance): `ksp_solve(K, apply_linop(A, x)).x ≈ x` for any `x` in the domain of `A`, where `A` is the system operator bound inside `K`. This is the defining property — `ksp_solve` is an approximation to the inverse of `A`. The approximation gap is bounded by `eps` (the convergence threshold).
4. **Idempotent re-solve** (modulo tolerance): `ksp_solve(K, b).x` applied to the *converged* result `x*` (i.e. re-solving `A · x = b` starting from `x*`) yields `x*` again in zero or near-zero iterations. Witnessed by Palace's initial-guess machinery: a warm start with the converged solution produces an initial residual at or below the convergence threshold (`palace/linalg/iterative.cpp:417-419`). At L1 the law captures that `ksp_solve` is the projection onto the converged-iterate fixed point of the Krylov iteration.
5. **Construction commutes with `SetOperators`** (composition law on `K` itself): the L0 `SetOperators(A, pc_op)` followed by `Mult(b, x)` is equivalent to constructing a fresh `K` with the new `A` and `pc_op` and calling `ksp_solve(K, b)`. This is the L0-witness that `K`'s system-operator and preconditioner-operator are part of its opaque state, not separate per-call arguments. At L1, mutating `K`'s system operator is **not** an exposed operation — `K` is a value, and "setting the operator" is "constructing a new `K`".

Laws that explicitly **do not** hold:

- **Bit-determinism across reduction-tree variants** — different orderings of the inner `dot` / `nrm2` reductions produce different per-call `iterations` and `final_res` values, and different bit-level `x`. Algorithmic correctness preserved; bit reproduction not. (Load-bearing per CLAUDE.md; inherited from `apply_linop`, `dot`, `nrm2`.)
- **Bit-determinism across orthogonalisation variants** (GMRES / FGMRES) — MGS vs CGS vs CGS2 produce different floating-point trajectories. Same caveat.
- **Bit-determinism across initial-guess variants** — warm-started vs cold-started solves take different per-call `iterations` and may converge to bit-different `x` (the orbit through Krylov subspaces differs). The mathematical solution is the same; the floating-point realisation differs.
- **Exact composition with `apply_linop`**: `apply_linop(A, ksp_solve(K, b).x) = b` does **not** hold exactly at finite tolerance — the equality is approximate within `eps`. The exact composition is recovered only in the formal limit. Algorithms that depend on exact composition (e.g. iterative-refinement schemes that assume the residual is zero after a solve) must guard.
- **Commutativity of nested `ksp_solve`s** — `ksp_solve(K₁, ksp_solve(K₂, b).x).x ≠ ksp_solve(K₂, ksp_solve(K₁, b).x).x` in general, since the underlying matrix product `A₁⁻¹ · A₂⁻¹` does not commute. Special case of operator-composition non-commutativity from [`L1/apply_linop`](./apply_linop.md).
- **Strict positive-iteration termination** — for `b ≈ 0` or warm starts at the converged solution, `result.iterations` may be `0` (the short-circuit at `palace/linalg/iterative.cpp:418-419`). Callers that assume `iterations ≥ 1` are wrong.

## Dependencies

At L1, `ksp_solve` depends on a single primitive plus three transitively-used BLAS-1 leaves:

- [`apply_linop`](./apply_linop.md) — the system-operator action `A · x` is the per-step matrix-vector product inside every Krylov method (CG at `palace/linalg/iterative.cpp:379, 443`; GMRES at `iterative.cpp:544-705`). The preconditioner application `M⁻¹ · r` is also an `apply_linop` call (via the [`solver-as-operator`](../concepts/solver-as-operator.md) type rotation: `Solver<OperType>` inherits from `OperType`, so a preconditioner is-an operator). Direct dependency.
- [`dot`](./dot.md), [`nrm2`](./nrm2.md), [`axpy`](./axpy.md) — transitively present in every Krylov iteration (orthogonalisation coefficients, residual norms, basis updates). Recorded as transitive rather than direct because they appear inside the per-method body the L1 `ksp_solve` opaquely wraps; the L2 `krylov-step` operator is the layer at which they become direct dependencies.

`ksp_solve` is the **gate from BLAS-1 to constructed-operator vocabulary** at L1 — it is the first L1 operator whose primary argument is itself a structured value (`Solver[A]`) rather than a raw tensor or scalar. The construction of `Solver[A]` from a system operator, preconditioner, and convergence-control parameters is the [`constructed-operator-factory`](../concepts/constructed-operator-factory.md) concept; the absorption of per-method variants into the opaque type is the [`variant-absorption`](../concepts/variant-absorption.md) concept; the L2 layer that unfolds the per-step body inside `Solver[A]` is [`L2/krylov-step`](../L2/krylov-step.md).

## Variant axes

`ksp_solve` has three orthogonal variant axes at L1; a fourth axis is collapsed and recorded as deliberate absorption.

- **element-type**: `real` | `complex`. The L0 source splits this into two parallel template instantiations — `KspSolver = BaseKspSolver<Operator>` and `ComplexKspSolver = BaseKspSolver<ComplexOperator>` at `palace/linalg/ksp.hpp:74-75`. At L1 these collapse to one operator parameterised by element type. Semantics are identical across element types — the linear-system relationship `A · x = b` is the same; only the field of the underlying scalar differs.
- **initial-guess-policy**: `cold-start` | `warm-start`. At L0 this is the `IterativeSolver::initial_guess` flag plus the requirement that `x` carry the initial-guess value on entry to `Mult` (`palace/linalg/iterative.cpp:377-386`). At L1 the policy is bound inside `K`'s opaque state and the per-call signature does not include an explicit initial guess. The choice affects `result.iterations` and `result.initial_res` but not the converged-solution algebraic property (law 3 above). Per-method initial-guess threading at L0 is an L1>L0 lowering concern.
- **convergence-failure-policy**: `soft-fail-with-flag` (the only variant Palace exposes). The L0 `BaseKspSolver::Mult` always returns the iterate and logs a warning on non-convergence (`palace/linalg/ksp.cpp:301-307`); there is no hard-fail mode. At L1 the policy is implicit in `SolveResult.converged` carrying a boolean rather than a sum-typed `Converged | TolFailed | DivergedNaN | …` (the L4 `solve-monad` lifts this to an `Outcome` sum type — see [`concepts/solve-monad`](../concepts/solve-monad.md) "Termination as a sum type"). At L1 a single boolean suffices because the L0 surface only distinguishes the two cases.

Collapsed (absorbed) axis:

- **krylov-method**: `CG` | `GMRES` | `FGMRES`. At L0 these are the three implemented arms of the `KrylovSolver` enum dispatch at `palace/linalg/ksp.cpp:34-58`, realised by separate `IterativeSolver` subclasses (`CgSolver`, `GmresSolver`, `FgmresSolver` at `palace/linalg/iterative.hpp:118-275`) with disjoint per-method workspace layouts (CG: `r, z, p`; GMRES: `V, r, H, s, sn, cs`; FGMRES adds `Z`). At L1 these **collapse to a single `Solver[A]` opaque type** — the L1 contract sees only the construction-bound solver and its convergence semantics; the per-method body is an L0 (and L2-`krylov-step`) concern that surfaces only in the L1>L0 lowering theme and in load-bearing numerical caveats (orthogonalisation-method bit-determinism for GMRES / FGMRES). This is the canonical *variant absorption* application for the constructed-operator vocabulary (per [`concepts/variant-absorption`](../concepts/variant-absorption.md) and [`concepts/constructed-operators`](../concepts/constructed-operators.md)).

Out of scope for this operator (deliberate exclusions):

- **MINRES / BICGSTAB / DEFAULT** — three enumerated `KrylovSolver` cases that route to `MFEM_ABORT` at `palace/linalg/ksp.cpp:53-57`. Per the CLAUDE.md "Unimplemented Palace stub policy", these are documented as L1>L0 obstruction themes ([`L1-L0/minres-iteration`](../L1-L0/minres-iteration.md), [`L1-L0/bicgstab-iteration`](../L1-L0/bicgstab-iteration.md)) and are **not** part of this firm L1 operator's surface. A Palace user attempting to construct `K` with `KrylovSolver::MINRES` aborts during factory construction (`ConfigureKrylovSolver` at `palace/linalg/ksp.cpp:34-58`), so no `K` of those methods ever reaches a `ksp_solve` call site.
- **Eigenvalue solves, nonlinear solves, least-squares solves** — different primitives, different signatures. Out of scope.

## Status

`firm` — signature is canonical (matches the in-place `BaseKspSolver<OperType>::Mult(b, x)` pattern with the L1 rotations applied — destination drops, statistics structured into the result, per-method dispatch absorbed), evidence is direct from the Palace source (the `BaseKspSolver` class plus the three implemented `IterativeSolver` subclasses plus use sites across the four solver-pipeline drivers), and the algebraic laws listed are standard properties of approximate-linear-inverse operators modulo the explicitly-recorded floating-point and finite-tolerance caveats. The MINRES / BICGSTAB / DEFAULT enum cases that abort at the factory are documented as out-of-scope obstructions, consistent with the unimplemented-Palace-stub policy in CLAUDE.md.

## L1 vs L0 distinction

- **L0**: `BaseKspSolver<OperType>` class with three constructors, owned `unique_ptr` to an `IterativeSolver<OperType>` (one of `CgSolver`, `GmresSolver`, `FgmresSolver`) and an optional `unique_ptr` to a `Solver<OperType>` preconditioner. `Mult(b, x)` method wraps `BlockTimer`, dispatches to `ksp->Mult(x, y)` (note: argument-name swap — the inner method's `x` is the RHS, `y` is the solution; see [`L0/kspsolver-base-class`](../L0/kspsolver-base-class.md) "The `Mult` method"), checks `ksp->GetConverged()`, logs an `Mpi::Warning` on non-convergence, and increments cumulative counters. Per-method body (CG / GMRES / FGMRES) implemented in `palace/linalg/iterative.cpp` with disjoint workspace layouts and per-method enum dispatch at the factory (`palace/linalg/ksp.cpp:34-58`). Three unimplemented enum cases (`MINRES` / `BICGSTAB` / `DEFAULT`) route to `MFEM_ABORT`.
- **L1**: pure functional solve. `result = ksp_solve(K, b)`. No destination buffer in the signature. Statistics structured into `SolveResult` fields rather than mutated counters. Convergence flag structured into `SolveResult.converged` rather than logged side effect. One operator parameterised by element type, with `krylov-method` axis collapsed into the opaque `Solver[A]` type. Initial-guess policy bound inside `K`; per-call signature is `(K, b) → SolveResult`. Algebraic laws (linearity, zero-RHS-zero-solution, operator inverse, idempotent re-solve) apply directly modulo convergence tolerance. Floating-point reduction-tree non-associativity (inherited from `apply_linop`, `dot`, `nrm2`) and orthogonalisation-method bit-determinism (GMRES / FGMRES) are recorded as explicit non-laws.

## Evidence

- `palace/linalg/ksp.hpp:29-72` — `BaseKspSolver<OperType>` class declaration (full surface: constructors, statistics accessors, tolerance forwarding, `SetOperators`, `Mult`).
- `palace/linalg/ksp.hpp:32-34` — `static_assert` restricting `OperType` to `Operator` or `ComplexOperator` (the element-type axis).
- `palace/linalg/ksp.hpp:71` — `Mult(const VecType &x, VecType &y) const` — the L0 central entry point (argument-name swap: `x` is the RHS, `y` is the solution).
- `palace/linalg/ksp.hpp:74-75` — `KspSolver` / `ComplexKspSolver` type aliases (the two L0 element-type instantiations).
- `palace/linalg/ksp.cpp:34-58` — `ConfigureKrylovSolver` switch on `KrylovSolver` enum: three implemented arms (`CG`, `GMRES`, `FGMRES`), three aborting arms (`MINRES`, `BICGSTAB`, `DEFAULT` — out of scope per stub policy).
- `palace/linalg/ksp.cpp:53-57` — the `MFEM_ABORT` fall-through for the three unimplemented enum cases. Direct evidence the L1 form's variant-axis collapse is across CG / GMRES / FGMRES only.
- `palace/linalg/ksp.cpp:265-274` — move-in constructor; load-bearing composition wiring at line 272 (`this->ksp->SetPreconditioner(*this->pc)`) — the moment the preconditioner is registered with the iterative solver.
- `palace/linalg/ksp.cpp:276-294` — `SetOperators` definition with the multigrid-finest special case at lines 283-288.
- `palace/linalg/ksp.cpp:296-310` — `Mult` definition (the central L0 entry point): `BlockTimer` wrap, `ksp->Mult(x, y)`, `GetConverged()` check + `Mpi::Warning` log, counter increments.
- `palace/linalg/ksp.cpp:308-309` — cumulative statistics counter mutations (`ksp_mult++`, `ksp_mult_it += ksp->GetNumIterations()`).
- `palace/linalg/ksp.cpp:301-307` — non-convergence soft-failure pattern: warning log, no abort, iterate returned regardless.
- `palace/linalg/ksp.cpp:312-313` — explicit template instantiations for `Operator` and `ComplexOperator` (the element-type axis).
- `palace/linalg/iterative.hpp:25-115` — `IterativeSolver<OperType>` base class: declares `A`, `B`, tolerance / iteration state, `converged`, `initial_res`, `final_res`, `final_it` (the four `SolveResult` fields' L0 origins), `GetConverged()` (line 98).
- `palace/linalg/iterative.hpp:118-150` — `CgSolver<OperType>` declaration with workspace `r, z, p` (line 144).
- `palace/linalg/iterative.hpp:154-217` — `GmresSolver<OperType>` declaration with workspace `V, r, H, s, sn, cs` (lines 190-194), `max_dim` restart parameter (line 180), `gs_orthog` orthogonalisation choice (line 184), `pc_side` preconditioner-side choice (line 187).
- `palace/linalg/iterative.hpp:221-275` — `FgmresSolver<OperType>` declaration extending `GmresSolver` with additional workspace `Z` (line 256), default-right preconditioning (line 265).
- `palace/linalg/iterative.cpp:361-486` — `CgSolver<OperType>::Mult` definition: full per-step CG body. Direct evidence of the per-method workspace allocation (`r.SetSize`, `z.SetSize`, `p.SetSize` at lines 369-371), the initial-guess threading (lines 377-386), the residual-proxy convergence test (line 417-419 short-circuit at zero residual), and the per-step `apply_linop` / `dot` / `axpy` use.
- `palace/linalg/iterative.cpp:544-705` — `GmresSolver<OperType>::Mult` definition: full per-step GMRES body with Arnoldi orthogonalisation, restart logic, and Hessenberg-update / Givens-rotation least-squares residual proxy.
- `palace/linalg/divfree.cpp:175` — `ksp->Mult(rhs, psi)` call site inside `DivFreeSolver<VecType>::Mult` — direct L0 evidence of the use pattern; the L2 form lifts this to `psi = ksp_solve(self.ksp, rhs)` (per [`spec/slices/divfree`](../spec/slices/divfree.md) §L2 step 3).
- `palace/drivers/electrostaticsolver.cpp:69` — `ksp.Mult(RHS, V[step])` call site inside the per-terminal loop. Direct L0 evidence of the driver-side use pattern.
- `palace/drivers/magnetostaticsolver.cpp:77` — `ksp.Mult(RHS, A[step])` call site (analogous).
- `palace/drivers/drivensolver.cpp:196` — `ksp.Mult(RHS, E)` call site (analogous, complex path).
- `book/src/L0/kspsolver-base-class.md` — cycle-006 L0 anchor chapter for `BaseKspSolver` (the direct source-of-truth for what L1 wraps).
- `book/src/L0/ksp-factory-file.md` — cycle-004 L0 anchor for the factory + the documented advertised-but-unimplemented pattern.
- `book/src/L0/apply-linop-overload-set.md` — L0 anchor for the `Mult` / `MultTranspose` / `AddMult` overload family the iterative solvers dispatch into.
- `book/src/concepts/ksp_solve.md` — pre-existing methodology-era concept page for the L1 `ksp_solve` primitive (predates the firm operator chapter; covers the constructed-operator-companion-to-`apply_linop` framing and the divfree slice use).
- `book/src/concepts/solve-monad.md` — L4-bound monadic coordination layer the L1 form anchors.
- `book/src/concepts/solver-as-operator.md` — the type-level rotation underwriting the L1 form's treatment of `K` as substitutable for an `apply_linop`-style primitive.
- `book/src/concepts/constructed-operators.md`, `concepts/variant-absorption.md`, `concepts/constructed-operator-factory.md` — the three methodology concepts the L1 entry's variant-axis collapse and opaque-type treatment rest on.
- `book/src/L2/krylov-step.md` — the upstream L2 layer that unfolds the per-method body the L1 `ksp_solve` opaquely wraps.
- `book/src/spec/slices/divfree.md` — the slice-corpus precedent for the L1 / L2 `ksp_solve` use pattern.
```

```edit:book/src/L1/index.md
[Replace the dep-map table to insert a new firm row for `ksp_solve`. The vocabulary cohort section also gets a new "Firm (8)" → grows by one, and `ksp_solve` is added to the firm list.]

# L1 — Mutation-lifted forms

Source operations re-expressed as pure functions: explicit input set, output set; in-place mutation and aliasing patterns either erased (workspace/scratch buffers) or made explicit (semantically-meaningful aliasing). The **mutation rotation** layer.

## Context

L1 is the closest pure-functional layer to the source. Structure follows the source loop; what changes is:

- **In-place vector updates → fresh-value updates.** `y.Add(α, x)` and `y.AXPBY(α, x, β)` (mutating member methods) become `y_new = axpy(α, x, y_old)` and `y_new = axpby(α, x, β, y_old)`. The L0 destination buffer disappears from the signature; the L1>L0 lowering reintroduces it.
- **Receiver-vs-argument asymmetry → first-class conjugation argument.** `ComplexVector::Dot` is a method on `*this`, making the receiver the linear argument and the call argument the conjugated one. At L1 the method-form / free-function-form distinction is erased: `dot` is sesquilinear in fixed argument order (first argument conjugated).
- **Operator-application mutation → pure operator-as-function.** `A.Mult(x, y)` (writes into `y`) → `y = A·x` (no destination buffer mention). Pattern recurs in `apply_BA`, residuals, and B-weighted norms.
- **Pinned reduction tree → reduction as a single semantic step.** L0 `dot` and `nrm2` are layered as `Hypre per-rank kernel + MPI_Allreduce`; L1 names the reduction as one step and records floating-point reduction-tree non-associativity as a **load-bearing** algebraic claim (per `CLAUDE.md` "Optimization tricks vs. base algebra"), not as separate operators.
- **Iterative loop mutating iterate in place → functional unfold** `state_{k+1} = step(state_k)`. Workspace `tmp` is omitted (the COW backend handles allocation).
- **Construction-bound solver state → opaque type at the L1 surface.** `BaseKspSolver<OperType>::Mult(b, x)` (writes into `x`, dispatches through owned `IterativeSolver` + `Solver` `unique_ptr`s, mutates statistics counters, logs convergence warnings) becomes `(x, status) = ksp_solve(K, b)` where `K : Solver[A]` is opaque about its internal Krylov method, per-method workspace, and preconditioner representation. Per-method enum dispatch (CG / GMRES / FGMRES) is variant-absorbed; cumulative counters lift to driver-side accumulation over per-call `SolveResult.iterations`.

## Semantics (overlay)

L1 vocabulary mirrors the source operations but with pure-functional binding. Four semantic motifs recur across the firm operators:

1. **Element-wise pure update** (`axpy`, `axpby`) — element-local, reduction-free, every output element depends on exactly one input element from each tensor argument. Algebraic laws are linear-combination facts; constant-folding branches at L0 (e.g., `axpy`'s `α == 1.0` fast path) are transparent performance tricks that disappear at L1.
2. **Mutation-free reduction** (`dot`, `nrm2`) — reduction over the length axis to a scalar. Reduction-tree non-associativity is load-bearing and recorded as an explicit non-law; the MPI collective is folded into the L1>L0 lowering, not the L1 signature.
3. **Subsumption-as-identity rather than dependency** — when one operator is a specialisation of another (`axpy(α, x, y) = axpby(α, x, 1, y)`), both stay in the L1 dep-map as siblings; the relationship is captured by an algebraic law in the subsuming operator, not by a dep-map edge.
4. **Constructed-operator absorption** (`ksp_solve`) — the L1 form takes a structured opaque `Solver[A]` argument whose per-method body (CG / GMRES / FGMRES), preconditioner, tolerances, and iteration cap are bound at construction; the L1 signature is variant-free. Result is structured (`SolveResult` carries `x` + four solve-statistics fields) rather than the L0 in-place destination + side-effect logger + mutating counters. The L2 `krylov-step` operator is where the per-method body unfolds.

Shape contracts are declared at boundaries (per the bunsen `contracts::unpack_shape_contract!` style). Single-rank is in scope per `CLAUDE.md`; MPI collectives appear only in lowering themes.

## Vocabulary cohort

**Firm (8)** — element-wise updates, BLAS-1 reductions, the opaque-operator gate, and the constructed-operator solve gate:

- [`axpy`](./axpy.md) — vector-scalar fused update; canonical BLAS-1 leaf.
- [`dot`](./dot.md) — Hermitian inner-product reduction (real / complex; `tdot` for unconjugated bilinear).
- [`nrm2`](./nrm2.md) — Euclidean norm; defined as `√dot(x, x)`.
- [`axpby`](./axpby.md) — fused two-scalar two-vector update; subsumes `axpy` and pure-scaling as algebraic identities.
- [`scal`](./scal.md) — pure vector-scalar multiply; the fourth BLAS-1 floor primitive (sibling-subsumed by `axpby` β=0).
- [`apply_linop`](./apply_linop.md) — pure linear-operator application `y = A·x`; opaque-operator gate to the L2 `krylov-step` vocabulary.
- [`axpbypcz`](./axpbypcz.md) — fused three-scalar three-vector update; subsumes `axpby` (γ=0) and `axpy` (β=1, γ=0).
- [`ksp_solve`](./ksp_solve.md) — pure preconditioned Krylov solve `(x, status) = ksp_solve(K, b)`; constructed-operator gate. The first L1 operator whose primary argument is itself a structured value (`Solver[A]`) rather than a raw tensor or scalar.

**Rough-in (obstruction)** — speculative L1 operators emitted by `L1>L0` obstruction themes (no Palace L0 anchor; harvester promotion gated on appearance of an anchor):

- `lanczos_step`, `three_term_recurrence_update`, `givens_apply_with_residual_min` — from [`minres-iteration`](../L1-L0/minres-iteration.md) theme.
- `bicgstab_step`, `omega_update`, `stabilisation_update` — from [`bicgstab-iteration`](../L1-L0/bicgstab-iteration.md) theme.

**Queued (open questions)** — small primitives that bottom-out remaining L0 patterns referenced by the firm cohort:

- `nrm2_B :: (x, B) → √(xᴴ B x)` — energy norm; depends on `dot` and `apply_linop`. Recorded as a boundary in `nrm2`'s entry; deferred to a separate harvest. Slug: `nrm2-B-weighted-energy-norm-harvest`.

## Operator dep-map

| Operator | Signature | Dependencies | Status |
|---|---|---|---|
| [`axpy`](./axpy.md) | `(α, x, y) → α·x + y` | (leaf) | `firm` |
| [`dot`](./dot.md) | `(x, y) → ⟨x, y⟩` (hermitian for complex) | (leaf) | `firm` |
| [`nrm2`](./nrm2.md) | `(x) → √⟨x,x⟩` | `dot` | `firm` |
| [`axpby`](./axpby.md) | `(α, x, β, y) → α·x + β·y` | (leaf; subsumes `axpy`) | `firm` |
| [`scal`](./scal.md) | `(α, x) → α·x` | (leaf; subsumed by `axpby` via β=0) | `firm` |
| [`apply_linop`](./apply_linop.md) | `(A: LinearOperator[M, N], x: Tensor[N]) → Tensor[M]` | (leaf; opaque operator) | `firm` |
| [`axpbypcz`](./axpbypcz.md) | `(α, x, β, y, γ, z) → α·x + β·y + γ·z` | (leaf; subsumes `axpby` and `axpy`) | `firm` |
| [`ksp_solve`](./ksp_solve.md) | `(K: Solver[A: LinearOperator[N, N]], b: Tensor[N]) → SolveResult[N]` | `apply_linop` (direct); `dot`, `nrm2`, `axpy` (transitive via per-method body) | `firm` |
| [`lanczos_step`](../L1-L0/minres-iteration.md) | `(A, B?, V_prev, V_curr) → (V_next, alpha, beta)` | `apply_linop`, `dot`, `axpy`, `nrm2` | `rough-in (obstruction, proposed-by: abstractor:2026-05-27T004641Z-abstractor-MINRES-L1-L0)` |
| [`three_term_recurrence_update`](../L1-L0/minres-iteration.md) | `(alpha_curr, beta_prev, beta_curr) → BandColumn3` | (leaf) | `rough-in (obstruction, proposed-by: abstractor:2026-05-27T004641Z-abstractor-MINRES-L1-L0)` |
| [`givens_apply_with_residual_min`](../L1-L0/minres-iteration.md) | `(qr_state, BandColumn3) → (qr_state', s_residual)` | `givens` | `rough-in (obstruction, proposed-by: abstractor:2026-05-27T004641Z-abstractor-MINRES-L1-L0)` |
| [`bicgstab_step`](../L1-L0/bicgstab-iteration.md) | `(A, M, r̂₀, state) → state'` (state ≡ `(x, r, p, v, ρ_prev, α_prev, ω_prev)`) | `axpy, axpby, dot, apply_linop` | `rough-in (obstruction, proposed-by: abstractor:2026-05-27T004641Z-abstractor-BiCGStab-L1-L0)` |
| [`omega_update`](../L1-L0/bicgstab-iteration.md) | `(t, r) → ⟨t,r⟩/⟨t,t⟩` | `dot` | `rough-in (obstruction, proposed-by: abstractor:2026-05-27T004641Z-abstractor-BiCGStab-L1-L0)` |
| [`stabilisation_update`](../L1-L0/bicgstab-iteration.md) | `(t, r, ẑ, h) → (x_new, r_new, ω)` | `omega_update, axpy` | `rough-in (obstruction, proposed-by: abstractor:2026-05-27T004641Z-abstractor-BiCGStab-L1-L0)` |

## Working Notes

- The dep-map records **L1-internal** dependencies only. Subsumption chains (`axpy ≺ axpby ≺ axpbypcz`) are stated as algebraic laws in the subsuming operator's entry, not as dep-map edges — both operators stay as siblings in the table.
- Aliasing-aware patterns where aliasing is semantically meaningful (not just buffer reuse) are first-class L1 content; transparent buffer reuse is an L1>L0 lowering concern.
- MPI single-rank scope (per `CLAUDE.md` "Scope") applies uniformly across L1 reductions: the L1 signature never includes a communicator; the L1>L0 lowering reintroduces `MPI_Allreduce` and records bit-deterministic-reduction-order trade-offs.
- Constant-folding fast paths at L0 (e.g., `axpy`'s `α == 1.0` branch, `dot`'s self-dot `&x == &y` branch) are classified as transparent performance tricks and erased at L1 — but only after the critic confirms they are algebraically equivalent to the unfolded form. Load-bearing numerical tricks (the pinned reduction tree) are preserved as explicit non-laws.
- The MINRES / BiCGStab rough-in operators above are emitted by **obstruction** L1>L0 themes — Palace has no L0 realisation (the `KrylovSolver::MINRES` and `KrylovSolver::BICGSTAB` enum cases route to `MFEM_ABORT` at `palace/linalg/ksp.cpp:53-57`). Harvester should not attempt promotion until either (a) Palace gains the implementation or (b) the L0 scope is widened to include vendored MFEM (see open question `bicgstab-mfem-reanchor-policy`).
- `ksp_solve` is the **first firm L1 operator whose primary argument is a structured opaque value** (`Solver[A]`) rather than a raw tensor or scalar. The construction of `Solver[A]` is the [`constructed-operator-factory`](../concepts/constructed-operator-factory.md) concept; the per-method axis collapse is [`variant-absorption`](../concepts/variant-absorption.md); the L0 anchor is [`L0/kspsolver-base-class`](../L0/kspsolver-base-class.md). The variant-axis collapse covers the **implemented** three (`CG`, `GMRES`, `FGMRES`) only; the three aborting enum cases (`MINRES`, `BICGSTAB`, `DEFAULT`) are out-of-scope per CLAUDE.md "Unimplemented Palace stub policy" and remain documented as L1>L0 obstruction themes.
```

```edit:book/src/SUMMARY.md
[Add chapter entry under the L1 Part. Insertion point: immediately after the `axpbypcz` row, before the `# L1 > L0 — Lowering` header. Exact diff:]

# L1 — Mutation-Lifted Forms
- [Overview](./L1/index.md)
- [axpy](./L1/axpy.md)
- [dot](./L1/dot.md)
- [nrm2](./L1/nrm2.md)
- [axpby](./L1/axpby.md)
- [scal](./L1/scal.md)
- [apply_linop](./L1/apply_linop.md)
- [axpbypcz](./L1/axpbypcz.md)
- [ksp_solve](./L1/ksp_solve.md)

[The L1 Part now contains 8 firm operators; the rest of SUMMARY.md is unchanged.]
```

## Operator content

The operator entry written above into `book/src/L1/ksp_solve.md` formalizes `ksp_solve` as the L1 mutation-rotation of Palace's `BaseKspSolver<OperType>::Mult(b, x)` method. Key formalization decisions:

- **Slug**: `ksp_solve` (matches existing concept-page slug `concepts/ksp_solve.md`, matches slice-corpus reference idiom `psi ← ksp_solve(self.ksp, rhs)`, lowercase underscore-separated like `apply_linop`).
- **Signature**: `(K: Solver[A: LinearOperator[N, N]], b: Tensor[N]) → SolveResult[N]` with `SolveResult = {x, converged, iterations, initial_res, final_res}`. The construction-bound `K` carries the system operator `A`, optional preconditioner, tolerances, iteration cap, restart-dim (for GMRES family), initial-guess policy, and per-method choice (CG / GMRES / FGMRES) — all opaque at the L1 surface.
- **Semantics** (3 paragraphs): (1) the `SolveResult` interpretation including soft-failure non-convergence; (2) the destination-buffer drop and the initial-guess axis collapse with rationale; (3) the load-bearing reduction-tree non-associativity inherited from inner-loop primitives plus the orthogonalisation-method bit-determinism for GMRES/FGMRES.
- **Algebraic laws** (5 holding; 6 explicit non-laws): linearity in `b` modulo tolerance; zero-RHS-zero-solution; operator inverse on RHS; idempotent re-solve; construction-commutes-with-`SetOperators`. Non-laws cover bit-determinism axes and the exactness-of-composition that holds only in the formal limit.
- **Dependencies**: direct on `apply_linop`; transitive on `dot`, `nrm2`, `axpy` via the per-method body. Gate to the L2 `krylov-step` vocabulary.
- **Variant axes**: 3 orthogonal exposed (element-type, initial-guess-policy, convergence-failure-policy) + 1 collapsed (krylov-method, with the implemented-only scope of CG/GMRES/FGMRES). MINRES / BICGSTAB / DEFAULT explicitly out of scope per the unimplemented-Palace-stub policy.
- **Status**: `firm` (no longer rough-in; both anchors now in place).
- **L1 vs L0 distinction**: explicit overlay table-form section paralleling the precedent in `apply_linop.md`.
- **Evidence**: full citation list of `palace/linalg/ksp.{hpp,cpp}` + `iterative.{hpp,cpp}` ranges + driver-side use sites + book-internal cross-references (the L0 anchor, the four concept pages, the L2 upstream, the slice-corpus precedent). Inline source-quoting is avoided per the dispatch #3 thinning convention; the L0 surface is delegated to `L0/kspsolver-base-class.md` and `L0/ksp-factory-file.md`.

## Supporting evidence

**L0 anchor (cycle-006)**: `book/src/L0/kspsolver-base-class.md` — particularly its "Notes for higher layers" section explicitly forecasting this L1 operator (it states: "`BaseKspSolver` is the natural anchor for the L1 `ksp_solve` operator (not yet authored ...); the L1 form drops the in-place destination `y`, the statistics counters, and the convergence-warning side-channel; the pure functional form returns the solution vector. Non-convergence in the L1 form would be modelled either as a sentinel return value or as a separate `convergence-status` output ..."). My formalization follows the second option (structured `SolveResult` field), consistent with how cycle-006 framed the cleanest L1 rotation.

**Concept-page anchor (cycle-002)**: `book/src/concepts/solve-monad.md` — establishes the L4 monadic coordination layer that the L1 `ksp_solve` underwrites. The L1 form is what `restart_cycle` / `inner_loop` decompose into below the monad; the L1 `ksp_solve` is the whole-solve primitive at the layer below the L4 monad-threading.

**Methodology concept (early-cycle)**: `book/src/concepts/ksp_solve.md` — the pre-existing concept page already describes the constructed-operator-companion-to-`apply_linop` framing. My L1 chapter explicitly cross-references this and is consistent with its claims; the L1 entry is now authoritative on every factual claim about the Palace surface.

**Slice corpus**: `book/src/spec/slices/divfree.md:165` — `psi ← ksp_solve(self.ksp, rhs)` is the slice-corpus precedent for the L1 call shape. My signature `(K, b) → SolveResult` matches with `SolveResult.x = psi`; the slice ignores the `(converged, iterations, ...)` fields (a slice-level abstraction the firm operator preserves).

**Palace source**: full citation list above; key load-bearing ranges are `palace/linalg/ksp.hpp:29-72` (class declaration), `palace/linalg/ksp.cpp:296-310` (`Mult` definition), `palace/linalg/ksp.cpp:34-58` (factory dispatch — implemented vs aborting arms), `palace/linalg/iterative.hpp:25-115` (`IterativeSolver` base with the four solve-statistics fields), `palace/linalg/iterative.cpp:361-486` (CG `Mult` body), `palace/linalg/iterative.cpp:544-705` (GMRES `Mult` body).

**Driver-side use**: `palace/drivers/electrostaticsolver.cpp:69`, `magnetostaticsolver.cpp:77`, `drivensolver.cpp:196`, and `palace/linalg/divfree.cpp:175` — four direct `ksp(.|->).Mult(RHS, x)` call sites across the solver pipelines, witnessing the use pattern.

**Tests**: No `test-ksp*.cpp` or `test-linalg*.cpp` unit-test surface exists in `reference/palace/test/unit/`; this is consistent with cycle-006's observation that the KSP solver is exercised at integration-test scale (driver pipelines), not at unit-test scale. The CG `Mult` body is exercised transitively via `test-rap.cpp` and `test-vector.cpp` only at the BLAS-1 primitives level. No test contradictions to my L1 claims.

## Open questions / caveats

- **Concept-page deconfliction (`concepts/ksp_solve.md` line 1-50 vs the L1 chapter)** — the early-cycle methodology concept page is consistent with my L1 chapter on every factual claim, but it predates the `SolveResult` structuring decision. The concept page says "returns x such that A · x ≈ b within ksp.tol" without naming the convergence-status / iteration-count outputs. A future invocation could update the concept-page signature to match the L1 chapter, or could leave the concept page as the narrative-level introduction with the L1 chapter as the authoritative definition (the precedent set by `concepts/nrm2.md` vs `L1/nrm2.md` per the cycle-002+ thinning sweep). My CYCLE.md proposes the L1 chapter as authoritative and does not touch the concept page. Slug for OQ: `ksp-solve-concept-page-signature-update`.
- **MINRES / BICGSTAB enum cases out of scope** — handled per CLAUDE.md "Unimplemented Palace stub policy" (the obstruction themes at `L1-L0/minres-iteration.md` and `L1-L0/bicgstab-iteration.md` document the stubs; my L1 operator's variant-axis collapse explicitly covers only the implemented CG/GMRES/FGMRES). No new OQ generated; this is the expected behaviour under the existing policy.
- **MFEM-vendored preconditioner reanchor (`bicgstab-mfem-reanchor-policy` open question, predates this dispatch)** — orthogonal to this dispatch's scope; not affected.
- **L1>L0 lowering theme for `ksp_solve`** — the firm L1 operator now exists; the L1>L0 lowering theme that maps `ksp_solve` to `BaseKspSolver::Mult(b, x)` + initial-guess threading + workspace allocation + statistics-counter mutation + convergence-warning logging is a natural next dispatch. Existing L1>L0 themes (`axpby-mutation-rotation`, `axpbypcz-mutation-rotation`, `apply-linop-mutation-rotation`) provide the precedent shape. Slug for OQ: `ksp-solve-mutation-rotation-l1-l0-theme`.
- **L2 layer connection** — the L2 `krylov-step` operator (cycle-006 firm) is the per-iteration body that the L1 `ksp_solve` opaquely wraps. The L1 chapter cross-references `L2/krylov-step` as the upstream layer that exposes the per-iteration body; a future L2>L1 lowering theme can make this connection explicit (lift L1 `ksp_solve` to an L2 `iterate_while(K.method, x_0)` form, or unfold an L1 `ksp_solve` call into an L2 sequence of `krylov-step`s). Not in this dispatch's scope; recorded as observation.
- **Layer intro refresh** — the L1 index intro section now has a four-motif structure (added "Constructed-operator absorption" as motif 4); the layer-intro-author may want to revisit the framing across `Context` / `Semantics (overlay)` paragraphs to integrate the constructed-operator motif more cleanly. Recorded per harvester role-spec convention as Open-question for the layer-intro-author. Slug for OQ: `l1-intro-refresh-after-constructed-operator-gate`.
- **Codemap-pilot note**: I did not invoke `mcp__palace-codemap__*` tools for this dispatch. The Palace KSP / iterative surface was already well-mapped by cycle-006's L0 chapter (with explicit `file:start-end` citations) and the directly-grep-able driver call sites were small enough to use `grep -n` + `Read` directly. The primary codemap pilot was on dispatch #1 (harvester `iterate_while`-family L4); this dispatch is consistent with not adding codemap-tool friction where the surface is already chapter-anchored.
- **Skill-uptake note: `classify-variant-axis`**: the skill's procedure (enumerate L0 dispatch axes; classify each as exposed-at-L1 vs collapsed-into-opaque-state; record absorbed axes with rationale) was followed procedurally though not explicitly invoked by name. The four-axis decomposition (element-type, initial-guess-policy, convergence-failure-policy as exposed; krylov-method as collapsed) plus the explicit out-of-scope listing of MINRES/BICGSTAB/DEFAULT matches the skill's expected output shape. Surfacing this note retroactively per the critic's telemetry-completeness check.
- **Skill-uptake note: `verify-citation-range`**: the skill's procedure (open each cited range, verify the cited content matches the claim, tighten over-reaches) was followed procedurally though not explicitly invoked by name across the ~25 cited file:start-end ranges. The critic identified one over-reach (`iterative.cpp:544-734` → should be `544-705`), which has been repaired in the cycle-007 repair pass. Procedural compliance was partial; explicit invocation would have caught the GMRES-Mult boundary slip during authoring.

## Append to scaffolding/open-questions.md

```yaml
---
slug: ksp-solve-concept-page-signature-update
opened_at: cycle-007
opened_by: harvester
status: open
---
```

The early-cycle methodology concept page `concepts/ksp_solve.md` documents `ksp_solve(ksp: KSP, b: Vector) → Vector` (a single solution-vector return). The cycle-007 firm L1 chapter `L1/ksp_solve.md` documents `ksp_solve(K, b) → SolveResult[N]` (a structured return carrying solution + four solve-statistics fields). Should the concept page be updated to match the L1 chapter's `SolveResult` signature, or is it intentional that the concept-page surface is the simpler narrative form?

Precedent from `concepts/nrm2.md` vs `L1/nrm2.md` (cycle-002+ thinning sweep) suggests the concept page should be updated to defer to the L1 chapter on factual claims while preserving the narrative framing. A future dispatch (likely under priority #11 retroactive-context-thinning or a follow-up concept-page sync) could update the concept-page signature line + add a "Solution-vs-result-record" note pointing at the L1 chapter's `SolveResult` definition. Not blocking. Source: `book/src/concepts/ksp_solve.md` vs `book/src/L1/ksp_solve.md` signature.

```yaml
---
slug: ksp-solve-mutation-rotation-l1-l0-theme
opened_at: cycle-007
opened_by: harvester
status: open
---
```

The firm L1 `ksp_solve` operator (cycle-007) now exists. The L1>L0 lowering theme that maps `ksp_solve(K, b) → SolveResult` to `BaseKspSolver::Mult(b, x)` + initial-guess threading + workspace allocation + statistics-counter mutation + convergence-warning `Mpi::Warning` logging is a natural next dispatch. Existing L1>L0 themes (`axpby-mutation-rotation`, `axpbypcz-mutation-rotation`, `apply-linop-mutation-rotation`) provide the precedent shape. Should this theme be queued for an `abstractor` or `lifter` dispatch in cycle-008 or later?

cycle-007 priority slate may or may not have this slot; cycle-008 cycle-planner can promote based on whether other L1>L0 work is already in progress. Not blocking. Source: `book/src/L1/ksp_solve.md` firm; no corresponding L1>L0 lowering theme yet.

```yaml
---
slug: l1-intro-refresh-after-constructed-operator-gate
opened_at: cycle-007
opened_by: harvester
status: open
---
```

The L1 layer-intro `Context` and `Semantics (overlay)` sections previously framed L1 as a BLAS-1-plus-opaque-operator surface. With cycle-007's `ksp_solve` adding the constructed-operator gate (the first L1 operator whose primary argument is a structured opaque value), the layer's semantic motif count grows from 3 to 4. The dep-map and motif list have been updated; should `layer-intro-author` revisit the broader framing in a follow-up dispatch (e.g. add a paragraph in `Context` calling out the constructed-operator absorption as the layer's transition point to upper-layer vocabulary)?

This is a polish-level concern; the current intro is correct and not misleading. cycle-008 or later can queue this if other layer-intro work is happening; otherwise the four-motif structure is self-explanatory. Source: `book/src/L1/index.md` updated to add "Constructed-operator absorption" as the fourth semantic motif.

## Closure note

This dispatch closes the OQ `l1-ksp-solve-firm-up-anchor-ready` from cycle-006 by emitting a firm L1 `ksp_solve` operator chapter with both anchors (concept-page + L0-anchor) in place, the dep-map row promoted to `firm`, and the SUMMARY chapter entry added.
