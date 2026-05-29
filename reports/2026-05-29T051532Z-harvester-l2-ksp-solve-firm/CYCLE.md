---
agent: harvester
invoked_at: 2026-05-29T051532Z
scope: L2 operator: ksp_solve
status: integrated
integrated_at: 2026-05-29T06:14:03Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-021 finalize (staging row #4). ksp_solve L2 operator PROMOTED stub→firm (full firm body landed — the outer-driver named-composition wrapping the firm L2 krylov-step kernel in a convergence-test/restart iterate_while fold; full body verified present, cycle-019 fence-truncation defect avoided). Establishes the NON-identity L2↔L1 (un-collapse) + L2↔L3 (iteration-view un-erasure) relationships; RESOLVES the maturity-gradient inversion below the firm cycle-020 L3 entry. dep-map :53 stub→firm; SUMMARY :44 in-place de-stub (replace, not append). Ordering: landed BEFORE the L3>L2 ksp-solve-outer-driver theme (#5) which depends on this firm L2 entry. L3-entry citation drift (:464→:463, :564→:563) routed to OQ (L3 append-only; new L2 entry uses corrected values). L2 firm 5→6. retroactive-budget 0; clean build. NOTE finalize moved ksp_solve from the L2/index Queued/stub cohort bullet to the Firm-at-L2 bullet (cohort-list consistency-repair to match this row)."
inputs:
  - book/src/L3/ksp_solve.md (firm L3 outer-driver fold, cycle-020 wave-1)
  - book/src/L2/ksp_solve.md (the stub being promoted)
  - book/src/L2/krylov-step.md (the L2 kernel sibling; ksp_solve is the driver)
  - book/src/L1/ksp_solve.md (firm; the opaque solver-as-operator collapse this L2 entry un-collapses)
  - book/src/concepts/ksp_solve.md (the methodology-era concept page)
  - book/src/L2/index.md (dep-map; stub row → firm row)
  - plan item ksp-solve-l2-promotion-non-identity-substantive-gap
  - OQ ksp-solve-l2-promotion-non-identity-substantive-gap
---

# CYCLE: Formalize ksp_solve at L2

## Summary
Promotes `book/src/L2/ksp_solve.md` from `stub` to `firm`. `ksp_solve` at L2 is the **outer-driver composition** for preconditioned Krylov solvers — the convergence-test / restart fold that wraps the [`krylov-step`](./krylov-step.md) kernel into a complete solve. It is the L2 *driver* complementing the L2 *kernel* `krylov-step`: the kernel names the per-step primitive composition (`carry -> {carry', readout}`), `ksp_solve` names the composition that folds that kernel under a convergence predicate to produce a converged solution plus the four-field result record. This entry resolves a **maturity-gradient inversion** (cycle-020 landed a firm L3 `ksp_solve` above an L2 stub) and closes a **substantive, non-identity** L2 coverage gap: every one of the five Palace solver pipelines wraps a `ksp_solve`, and the L2↔L1 relationship is genuinely non-identity (L1 collapses the entire method body — loop included — into one opaque operator application; L2 opens the wrap into the explicit kernel-fold composition while still erasing the L3 iteration-rotation view to an outer-driver-by-role surface). The L3>L2 lowering theme (`L3-L2/ksp-solve-outer-driver`) is forward-referenced as plain-text (cycle-021 wave-2 dispatch #3 authors it); this entry records only the L2-native composition, in L2 vocabulary.

## Proposed changes

```edit:book/src/L2/ksp_solve.md
---
layer: L2
operator: ksp_solve
firmness: firm
lifts_to:
  - book/src/L3/ksp_solve.md (the L3 iteration-rotation un-erasure: L2's outer-driver-by-role wrap becomes the explicit iterate_while_L3 fold; theme L3-L2/ksp-solve-outer-driver pending — NOT identity-in-form)
lowers_from:
  - book/src/L1/ksp_solve.md (the opaque solver-as-operator collapse; this L2 entry opens that collapse into the kernel-fold composition while keeping the iteration view erased)
variant_axes:
  - solver-method (CG single-fold / GMRES restart-nested-fold / FGMRES restart-nested-fold — selects the fold nesting + the result-residual proxy, not the kernel body)
  - element-type (real / complex)
  - preconditioner-side (left / right / split — absorbed into the constructed op.T the kernel folds; loop-shaping only via the residual proxy)
  - convergence-criterion (relative / absolute / combined — the eps = max(rel_tol·initial_res, abs_tol) threshold parameterizing the predicate)
  - initial-guess-policy (cold-start / warm-start — sets the entry iterate and the residual-proxy denominator)
  - convergence-failure-policy (soft-fail-with-flag — the only Palace variant)
---

# ksp_solve

The L2 **outer-driver composition** for preconditioned Krylov solvers: the convergence-test / restart fold that wraps the [`krylov-step`](./krylov-step.md) kernel into a complete solve. Consumes the construction-bound solver surface and a right-hand side; produces the converged solution plus the four-field solve-result record. This is the L2 *driver* that complements the L2 *kernel* [`krylov-step`](./krylov-step.md): the kernel names the per-step primitive composition (`(op, s) -> {state', outputs}`), `ksp_solve` names the composition that **folds** that kernel under a convergence predicate. The pair `(krylov-step = kernel, ksp_solve = driver)` is the L2 statement of the kernel-plus-driver shape that recurs across every Krylov-shaped slice in the corpus.

## Context

L2 is the fusion-rotation layer: each operation is written as a composition of base algebraic primitives, with HPC/SIMD tricks unfolded back into the base algebras. `ksp_solve` at L2 is the named composition that wraps [`krylov-step`](./krylov-step.md) — the *kernel* — into a *complete solve* by composing it with a convergence-test wrap and (for restarted methods) a restart wrap. Where [`krylov-step`](./krylov-step.md) is the recurring per-step kernel (one operator-apply, the optional orthogonalize/scalar-generator stage, the iterate-stratum update, the scalar-stratum update, the demand-pruned output readout), `ksp_solve` is the surrounding driver composition: it threads the kernel's state across steps, tests convergence after each step, re-seeds the basis at restart boundaries, and projects out the four-field result on exit.

The two L2 entries are complementary halves of one composition:

- [`krylov-step`](./krylov-step.md) — the **kernel**. Names the per-step L1-primitive composition. Foldable by construction (`iterate_while (krylov-step op) s₀ predicate` is a well-defined fold). Carries six *body*-variant axes, all absorbed at construction.
- `ksp_solve` (this entry) — the **driver**. Names the composition that wraps the kernel into a solve: the convergence-test fold plus the optional restart fold. Carries six *loop-shaping* variant axes (solver-method, element-type, preconditioner-side, convergence-criterion, initial-guess-policy, convergence-failure-policy) that shape the *fold*, not the kernel body.

This entry is the L2-coherence anchor for the *driver*: a reader at L2 can find the complete-solve composition here, in L2 vocabulary, without reaching up to the L3 iteration-rotation view ([`L3/ksp_solve`](../L3/ksp_solve.md), which renders the fold as an explicit tail recursion and names its `sequential-obstruction`) or down to the L1 collapse ([`L1/ksp_solve`](../L1/ksp_solve.md), which makes the solve one opaque operator application). It is the enactment of **Identity-lowerings still require both L levels** *for the driver half* — except that here both the L2↔L1 and L3↔L2 rotations are **non-identity** (see §"Lifts to" / §"Lowers from"); each is a genuine composition rotation, not a no-op.

### Relationship to the L1 collapse

[`L1/ksp_solve`](../L1/ksp_solve.md) collapses the entire method body — outer loop, restart logic, per-step kernel, all of it — into an **opaque** `ksp_solve :: (K: Solver[A], b) -> SolveResult`. That collapse is the *solver-as-operator* type rotation (per [`solver-as-operator`](../concepts/solver-as-operator.md)): at L1 a solve is one indivisible operator application, with `K` a black box that maps `b ↦ A⁻¹·b`. **This L2 entry opens that black box into the kernel-fold composition.** The L1 opaque `Solver[A]` becomes the explicit pairing of (a) the [`krylov-step`](./krylov-step.md) kernel parameterized by the construction-bound operator surface, and (b) the convergence-test/restart driver that folds it. The L1 absorbed `krylov-method` axis re-surfaces at L2 as the **solver-method** loop-shaping axis (selecting fold nesting and result proxy); the L1 absorbed preconditioner-side re-surfaces as a loop-shaping residual-proxy effect (the kernel-side absorption lives in [`krylov-step`](./krylov-step.md) / [`apply_BA`](../concepts/apply_BA.md)). The L1 algebraic laws (linearity in `b`, zero-RHS-zero-solution, operator-inverse, idempotent re-solve) are properties of the *fixed point* this fold converges to; they restate at L2 as fold-terminal properties (see §"Algebraic laws").

The L2↔L1 rotation is **non-identity**: it is the *un-collapse* of the L1 opacity into a composition. This is distinct from the identity [`L3-L2/krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md) kernel theme (where the L3 kernel body maps line-for-line into the L2 kernel body); the *driver* has no such identity — the wrap *is* the operator at L2, so opening the L1 opacity into the kernel-fold composition is the whole content of the rotation.

## Signature

```text
ksp_solve :: (K: Solver[A: LinearOperator[N, N]], b: Tensor[N]) -> SolveResult[N]

SolveResult[N] = {
  x          : Tensor[N],   -- approximate solution to A · x = b
  converged  : Bool,        -- whether the convergence test was satisfied
  iterations : Int,         -- number of inner Krylov iterations consumed
  initial_res: Real,        -- initial residual norm (per the solver's residual proxy)
  final_res  : Real         -- final residual norm (per the solver's residual proxy)
}
```

The body is the L2 driver composition — the convergence-test fold of the [`krylov-step`](./krylov-step.md) kernel:

```text
ksp_solve K b =
  let (op, s_0)     = setup K b                          -- bind kernel op-surface; seed state (iterate, eps, counters)
  let s_init        = init_convergence op s_0            -- residual proxy + eps + pre-loop converged flag
  let s_n           = iterate_while                       -- the outer-driver fold over the kernel
                        (\s -> (krylov-step op s).state)  --   body: the L2 kernel (state projection)
                        s_init                            --   seed
                        (\s -> not s.converged && s.it < op.max_it)  -- convergence predicate
  let s_final       = materialise_iterate op s_n          -- fold restart-cycle correction into s.x (identity for CG)
  in extract_result s_final                               -- the four-field SolveResult readout
```

Shape contract (bunsen-style; named axes — `SolveResult` matches the firm [`L1/ksp_solve`](../L1/ksp_solve.md) result so the L2↔L1 rotation is on the *body*, not the boundary type):

- **`K`** — `Solver[A]` — the construction-bound Krylov-solver value, identical in surface to the [`L1/ksp_solve`](../L1/ksp_solve.md) `K`: it binds the system operator `A : LinearOperator[N, N]` (or the constructed `apply_BA` per the preconditioner-side axis), an optional preconditioner `M⁻¹`, the convergence-control scalars `rel_tol` / `abs_tol` / `max_it`, and (for restarted methods) the restart dimension `max_dim`. Read-only at the call site. **At L2 the L1 opacity is opened**: `K` is destructured by `setup` into the kernel op-surface `op` (which [`krylov-step`](./krylov-step.md) consumes per-step) plus the loop-shaping fields (`max_it`, `max_dim`, the solver-method nesting) the driver fold reads. The kernel's six body-variant axes are absorbed into `op` at construction (per [`variant-absorption`](../concepts/variant-absorption.md)); the driver's six loop-shaping axes shape the fold (see §"Variant axes").
- **`b`** — `Tensor[N]` — the right-hand side. Read-only. Must match the operator's axis `N`. Seeds the initial residual `r_0 = b - A·x_0` inside `setup` / `init_convergence`.
- **result** — `SolveResult[N]` — the four-field solve-result record plus the solution `x`. The solution `x` is the converged iterate; the four statistics fields are the L2 readout of the convergence-test state, projected by `extract_result` from the terminal fold carry. These are the L2 composition's exposure of the [`krylov-step`](./krylov-step.md) kernel's `outputs.residual_norm` readout (demand-pruned per [`derived-view-hoisting`](../concepts/derived-view-hoisting.md)): `converged`/`iterations`/`initial_res`/`final_res` are pure functions of the fold's terminal carry. The L0 origins are the `IterativeSolver` result members `converged` / `initial_res` / `final_res` / `final_it` (`reference/palace/palace/linalg/iterative.hpp:52-55`), exposed through `GetConverged` (`:98`, with its `rel_tol > 0 || abs_tol > 0` gate) and `GetInitialRes` / `GetFinalRes` / `GetNumIterations` (`:101-108`); they are written on solve exit as `final_res = res; final_it = it;` (CG, `reference/palace/palace/linalg/iterative.cpp:484-485`) and `final_res = beta; final_it = it;` (GMRES, `:703-704`).

The fold's predicate `\s -> not s.converged && s.it < op.max_it` is the **convergence test** (per [`convergence-test`](../concepts/convergence-test.md)). It is the L2 rendering of the L0 loop guard `for (; it < max_it && !converged; it++)` (`reference/palace/palace/linalg/iterative.cpp:427`) composed with the per-step convergence flag `converged = (res < eps)` (`:463`, the in-loop test) that the [`krylov-step`](./krylov-step.md) kernel folds into `s.converged` via its `outputs.residual_norm` readout. The threshold `eps = max(rel_tol · initial_res, abs_tol)` is established once by `init_convergence` (`reference/palace/palace/linalg/iterative.cpp:417`) and closed over; the pre-loop `converged = (res < eps)` (`:418`) is the zero-iteration short-circuit (see §"Algebraic laws" law 2).

## Semantics

`ksp_solve` at L2 is the complete preconditioned-Krylov solve, expressed as a composition over the [`krylov-step`](./krylov-step.md) kernel. The composition has four phases, in dataflow order:

1. **Setup + convergence-test initialisation** (`setup` ▷ `init_convergence`). Destructure `K` into the kernel op-surface `op` and the loop-shaping fields; seed the iteration state (initial iterate `s.x`, residual `r_0`, counters `s.it = 0`). Establish the residual proxy and the threshold `eps = max(op.rel_tol · s.initial_res, op.abs_tol)` (`reference/palace/palace/linalg/iterative.cpp:417`), and seed `s.converged` by the pre-loop test `res < eps` (`:418`). The residual-proxy denominator depends on the initial-guess policy (cold-start uses the `‖b‖`-style proxy; warm-start uses the initial-residual proxy). A warm start at the already-converged solution short-circuits the fold to zero iterations — the basis of the idempotent re-solve law (§"Algebraic laws" law 4).

2. **The outer-driver fold** (`iterate_while (krylov-step op) s_init predicate`). This is the L2 composition proper — the kernel folded under the convergence predicate. Each fold step is exactly one [`krylov-step`](./krylov-step.md) invocation; the kernel increments `s.it`, updates the iterate/scalar strata, and emits `outputs.residual_norm`; the predicate reads `s.converged` (set from `outputs.residual_norm < eps`, the L0 `converged = (res < eps)` at `:463`). The fold is the L2 surface of the L0 `for (; it < max_it && !converged; it++)` loop (`reference/palace/palace/linalg/iterative.cpp:427`). **At L2 the fold is named by role — the convergence-test wrap of the kernel — not rendered as an explicit tail recursion**; the explicit-recursion iteration-rotation view, and the `sequential-obstruction` it carries, are the [`L3/ksp_solve`](../L3/ksp_solve.md) concern. L2 erases the iteration view to the role reference per [`L2/index`](./index.md) §Context.

3. **Final-iterate materialisation** (`materialise_iterate`). For non-restarted methods (CG, Chebyshev) the running iterate `s.x` is updated in-kernel each step, so `materialise_iterate` is identity (the terminal `s_n.x` is already correct). For restarted methods (GMRES, FGMRES) the externally-visible iterate is folded in once per restart cycle from the basis correction `K.V · K.y`; `materialise_iterate` folds the last partial restart-cycle's correction into `s.x`. This "iterate folded at restart boundaries, not per step" placement is the same the [`krylov-step`](./krylov-step.md) §Semantics restart discussion and [`solve-monad`](../concepts/solve-monad.md) §"Worked example — GMRES" describe.

4. **Result extraction** (`extract_result`). Project the four `SolveResult` statistics fields plus the solution `x` from the terminal fold carry. The L0 anchor is the result-write tail of each method's `Mult`: `final_res = res; final_it = it;` (CG, `reference/palace/palace/linalg/iterative.cpp:484-485`); `final_res = beta; final_it = it;` (GMRES, `:703-704`). `converged` is the terminal `s.converged`; the L0 `GetConverged()` additionally gates on `rel_tol > 0 || abs_tol > 0` (`reference/palace/palace/linalg/iterative.hpp:98`) — that gate is preserved in `extract_result`.

The **restart nesting** is a loop-shaping variant, not a kernel variant. CG is a single fold (`reference/palace/palace/linalg/iterative.cpp:427`). GMRES/FGMRES are a **double-nested** composition: the outer restart fold `for (; it < max_it; restart++)` (`reference/palace/palace/linalg/iterative.cpp:563`) wraps the inner Arnoldi-iteration fold. At L2 each fold is a named-by-role wrap; the restart fold re-seeds `K` (a fresh basis) per cycle and its predicate is `it < max_it` (the inner fold owns the convergence flag). This is the same structure [`krylov-step`](./krylov-step.md) §"Algebraic laws" (associativity non-law) cites: "slice-level restart logic is structured as an *outer* loop around the `krylov-step`-folding inner loop". The kernel is restart-*agnostic*; the driver owns restart.

The **driver does not branch on the kernel body**: the fold body is `krylov-step op`, invoked uniformly; the solver-method axis selects the fold *nesting* (single vs restart-nested) and the result-extraction residual proxy (`final_res = res`, the √|β| proxy for CG `:484`; `final_res = beta`, the LS-residual proxy for GMRES `:703`), not the kernel's body. This is what lets `ksp_solve` name the composition role (outer-driver wrap of the kernel) while [`krylov-step`](./krylov-step.md) supplies the per-step shape.

The **statistics counters are driver-side accumulators above this operator**, exactly as at L1. The L0 `BaseKspSolver<OperType>::Mult` (`reference/palace/palace/linalg/ksp.cpp:296-309`) wraps the per-method `ksp->Mult(x, y)` (`:300`) and increments cumulative counters `ksp_mult++` / `ksp_mult_it += GetNumIterations()` (`:308-309`); the non-convergence `Mpi::Warning` (`:301-306`) is a logged side effect. At L2 `ksp_solve` is the per-method solve composition (the per-solve fold); the `BaseKspSolver::Mult` cumulative wrapper sits *above* it — `result.iterations` is the per-call count, and the L0 cumulative `ksp_mult_it` is `Σ_calls result.iterations`. The warning is the caller's concern (the structured `result.converged` carries the same information). This keeps `ksp_solve` referentially transparent at the per-solve granularity.

## Algebraic laws

`ksp_solve` is a **driver composition** (a convergence-test fold of a kernel), not a binary algebra. The laws below are fold-terminal properties (laws about the fixed point the fold converges to) plus structural invariants; the L1 algebraic laws restate here as terminal properties because the L1 opaque operator *is* this composition's converged result.

1. **Terminal operator-inverse** (modulo tolerance; the load-bearing terminal law, inherited from [`L1/ksp_solve`](../L1/ksp_solve.md) law 3). For `K` whose system operator is `A`, `ksp_solve K b` produces `result.x ≈ A⁻¹·b`, exact in the limit `rel_tol, abs_tol → 0`, `max_it → ∞`. The fold converges to the fixed point of the Krylov iteration, which is the solution. The four statistics fields are the *finite-tolerance witnesses* of how close the terminal carry got: `result.final_res` bounds the gap, `result.converged` reports whether `eps` was met, `result.iterations` is the fold length. The approximation gap is bounded by `eps`.

2. **Zero-RHS / converged-warm-start short-circuit** (exact). When the pre-loop test `res < eps` holds (zero RHS, or warm start at the converged solution), the fold runs **zero** iterations: `result.iterations = 0` and `result.x = x_0`. This is the L0 short-circuit `converged = (res < eps)` before the loop (`reference/palace/palace/linalg/iterative.cpp:418`) combined with the loop guard `!converged` (`:427`). It is the L2 statement of the L1 idempotent-re-solve law (law 4) and the zero-RHS-zero-solution law (law 2): a fold whose predicate is false at the seed is identity on the iterate. **Consequence**: callers that assume `result.iterations ≥ 1` are wrong.

3. **Linearity of the terminal solution in `b`** (modulo tolerance). `ksp_solve K (α·b₁ + β·b₂).x ≈ α·(ksp_solve K b₁).x + β·(ksp_solve K b₂).x`, following the linearity of `A⁻¹`. Inherited from [`L1/ksp_solve`](../L1/ksp_solve.md) law 1. Only the *terminal solution* `x` is linear; the statistics fields (`iterations`, `initial_res`, `final_res`) are **not** linear in `b` — different RHSes generate different residual histories and take different fold lengths.

4. **Per-call referential transparency** (modulo the two load-bearing non-determinism sources). `ksp_solve K b` is a pure function of `(K, b)` — no mutable per-solver-instance state escapes (the L0 cumulative counters live in the `BaseKspSolver::Mult` wrapper *above* this operator, not inside the fold). The same inputs produce the same `SolveResult` modulo (a) reduction-tree non-associativity inherited transitively through the kernel's `dot` / `nrm2` / `apply_linop`, and (b) orthogonalisation-variant floating-point ordering (GMRES/FGMRES). The L2 rendering of the L1 "referentially transparent modulo two non-determinism sources" statement.

Laws that explicitly **do not** hold:

- **Fold-merge / associativity**. `ksp_solve` over a state resumed from a partial solve is **not** the same as a single `ksp_solve` with a combined predicate, for restarted methods — the restart re-seeds the basis `K` (discards the Krylov subspace), so the trajectory through two `max_dim`-bounded restart cycles is not the trajectory through one `2·max_dim`-bounded cycle. Inherited from [`krylov-step`](./krylov-step.md) §"Algebraic laws" (associativity non-law); this is why GMRES restart is an *outer* fold around the inner fold, not a flattened single fold.
- **Linearity of the statistics fields in `b`**. `result.iterations` / `result.initial_res` / `result.final_res` are **not** linear in `b` — different RHSes generate different residual histories and take different fold lengths. Only `result.x` is linear (law 3). Inherited from [`L1/ksp_solve`](../L1/ksp_solve.md) law 1's caveat.
- **Exact composition with `apply_linop`**. `apply_linop A (ksp_solve K b).x = b` holds only within `eps`, not exactly, at finite tolerance — inherited from [`L1/ksp_solve`](../L1/ksp_solve.md). Iterative-refinement schemes that assume a zero residual after a solve must guard.
- **Commutativity of nested solves**. `ksp_solve K₁ (ksp_solve K₂ b).x` ≠ the swapped composition, since `A₁⁻¹ · A₂⁻¹` does not commute. Inherited from [`L1/ksp_solve`](../L1/ksp_solve.md).
- **Bit-determinism across reduction-tree / orthogonalisation / initial-guess variants**. The fold's length and terminal `result.final_res` depend on the inner reduction tree, the orthogonalisation variant (GMRES/FGMRES), and the initial-guess policy at the bit level; the mathematical solution is the same, the floating-point realisation differs. Load-bearing per CLAUDE.md §"Optimization tricks vs. base algebra"; inherited from [`L1/ksp_solve`](../L1/ksp_solve.md) and transitively from [`krylov-step`](./krylov-step.md).
- **Identity / lift of the fold to a single tensor-field op at L2**. `ksp_solve` is not an algebra with an identity element, and the fold over the kernel does not collapse to a closed-form composition — the kernel is intrinsically sequential at the step boundary (the second step reads scalars produced by the first, per [`krylov-step`](./krylov-step.md) §"Algebraic laws" step-composition non-law). At L2 this surfaces only as the non-mergeability of the fold; the *iteration-rotation* statement of it (the outer-loop `sequential-obstruction`) is the [`L3/ksp_solve`](../L3/ksp_solve.md) concern, where the iteration view is load-bearing.

### Inherited demand-pruning (Law 1 of `krylov-step`, lifted to the fold)

The fold's `SolveResult` statistics fields are demand-pruned per [`derived-view-hoisting`](../concepts/derived-view-hoisting.md): if no consumer reads `result.iterations` / `result.initial_res` / `result.final_res`, the composition need not materialise the kernel's per-step `outputs.residual_norm` beyond what the convergence predicate requires. The predicate *does* require the residual norm (it is the predicate's input), so `result.final_res` is never fully pruned — but the *per-step trajectory* of residual norms (used only for printing, the L0 `print_opts.iterations` branch at `reference/palace/palace/linalg/iterative.cpp:465`) is prunable. This is the [`krylov-step`](./krylov-step.md) Law 1 (output-extras distributivity over the trajectory), lifted from the kernel to the driver. Witnessed by the consumer surface: the four-scalar result is consumed at `reference/palace/palace/linalg/iterative.hpp:52-55` and the sole `palace/` cumulative-stats caller is `reference/palace/palace/linalg/ksp.cpp:296-309` — per-iteration trajectory consumption is absent in `palace/`, so the trajectory accumulator prunes.

## Dependencies

**Same-layer (L2)**:

- [`krylov-step`](./krylov-step.md) — the per-step kernel this operator folds. **Direct, load-bearing dependency**: `ksp_solve`'s body is the convergence-test fold of `krylov-step op`. The kernel supplies the body; `ksp_solve` supplies the driver composition. This is the canonical L2 kernel/driver pair (mirroring the L2-kernel/L4-driver pair `(krylov-step, iterate_while)`).
- L2 named compositions appear only *transitively* through the kernel: [`orthogonalize`](./orthogonalize.md) (the `op.orthog` surface, present for GMRES/FGMRES) and the queued `incremental-least-squares` (the GMRES running-QR / Givens stream that produces the restart-cycle correction `K.y`) are folded by `krylov-step`, not called directly by the driver.
- The L1 primitives ([`apply_linop`](../L1/apply_linop.md), [`axpy`](../L1/axpy.md), [`axpby`](../L1/axpby.md), [`axpbypcz`](../L1/axpbypcz.md), [`dot`](../L1/dot.md), [`nrm2`](../L1/nrm2.md), [`scal`](../L1/scal.md)) appear only *transitively* through `krylov-step`; the driver does not call them directly.

**Cross-cutting concepts** (consumed unchanged):

- [`convergence-test`](../concepts/convergence-test.md) — the stopping-predicate surface that drives the fold (the `\s -> not s.converged && s.it < op.max_it` predicate).
- [`solver-as-operator`](../concepts/solver-as-operator.md) — the consumer-side framing; the L1 collapse this entry opens.
- [`solve-monad`](../concepts/solve-monad.md) — the L4 outer-driver surface; at L4 the convergence-test fold is the `Solve` monad's `iterate_while`, at L2 it is this named-by-role composition.
- [`derived-view-hoisting`](../concepts/derived-view-hoisting.md) — the demand-pruning algebra governing the statistics-field / trajectory-accumulator materialisation.
- [`variant-absorption`](../concepts/variant-absorption.md) — the kernel-body-variant absorption (in `krylov-step`); the driver's loop-shaping axes are *not* absorbed (they shape the fold).
- [`constructed-operators`](../concepts/constructed-operators.md) / [`apply_BA`](../concepts/apply_BA.md) — the preconditioner-side absorption into the kernel op-surface `op.T`.
- [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md) — the kernel-side first-step variant (in `krylov-step`); the driver is unrolling-agnostic.

A cross-cutting prose treatment of the constructed-operator framing lives at [`concepts/ksp_solve`](../concepts/ksp_solve.md). No L3 or L4 vocabulary appears in the L2 signature — no explicit `iterate_while_L3` tail recursion, no `Solve` monad, no L1 opacity (the kernel and the fold are visible at L2). That is the discipline of the layer.

## Variant axes

Six axes, all **loop-shaping** (they shape the driver fold, not the per-step kernel body — kernel body axes live in [`krylov-step`](./krylov-step.md)):

1. **solver-method** (`CG | GMRES | FGMRES`) — selects the **fold nesting**: CG is a single convergence-test fold (`reference/palace/palace/linalg/iterative.cpp:427`); GMRES/FGMRES are a restart-nested double fold (outer restart fold `:563` wrapping the inner Arnoldi fold). Also selects the result-extraction residual proxy (`final_res = res` √|β| proxy for CG `:484`; `final_res = beta` LS-residual proxy for GMRES `:703`). The kernel body stays uniform (`krylov-step op`); only the nesting and the proxy differ. Absorbed into opacity at L1; re-exposed here at composition granularity. The three implemented arms are the `KrylovSolver` factory cases `reference/palace/palace/linalg/ksp.cpp:34-58`; MINRES/BICGSTAB/DEFAULT abort at the factory (`:53-56`) and are out of scope per the unimplemented-Palace-stub policy.
2. **element-type** (`real | complex`) — the L0 `OperType ∈ {Operator, ComplexOperator}` template parameter on `IterativeSolver` (`reference/palace/palace/linalg/iterative.hpp:25-32`; `BaseKspSolver` instantiations `reference/palace/palace/linalg/ksp.cpp:312-313`). The fold structure is identical across element types; only the scalar field differs. Collapsed to one operator parameterised by element type, as at L1.
3. **preconditioner-side** (`left | right | split`) — for restarted methods, the side on which `M⁻¹` is applied; absorbed into the kernel op-surface `op.T` as a constructed `apply_BA` (per [`apply_BA`](../concepts/apply_BA.md) / [`constructed-operators`](../concepts/constructed-operators.md)). Loop-shaping only via the residual proxy the side selects (preconditioned vs unpreconditioned residual); the per-step application itself is kernel-side. CG uses split/symmetric preconditioning; GMRES/FGMRES select the side at construction.
4. **convergence-criterion** (`relative | absolute | combined`) — the `eps = max(rel_tol · initial_res, abs_tol)` threshold (`reference/palace/palace/linalg/iterative.cpp:417`) parameterising the fold predicate. `rel_tol = 0` gives a pure absolute criterion, `abs_tol = 0` a pure relative criterion, both nonzero the combined criterion (the default). The L0 `GetConverged()` gate `rel_tol > 0 || abs_tol > 0` (`reference/palace/palace/linalg/iterative.hpp:98`) means a solve with both tolerances zero reports `converged = False` regardless of residual — a degenerate corner preserved in `extract_result`. Loop-shaping (it shapes the predicate), not kernel-shaping.
5. **initial-guess-policy** (`cold-start | warm-start`) — sets the entry iterate (`x_0 = 0` cold vs `x_0 =` warm value) and the residual-proxy denominator in `init_convergence`. Affects `result.iterations` and `result.initial_res`, not the converged-solution algebraic property (law 1). Loop-shaping (it shapes the seed and the predicate denominator), not kernel-shaping.
6. **convergence-failure-policy** (`soft-fail-with-flag`) — the only Palace variant: the fold always returns the terminal iterate and reports `result.converged` (`reference/palace/palace/linalg/ksp.cpp:301-307` returns the iterate regardless; no hard-fail). At L2 the policy is implicit in `result.converged` being a `Bool` rather than a sum type (the L4 [`solve-monad`](../concepts/solve-monad.md) lifts it to an `Outcome` sum).

These six are **distinct from** [`krylov-step`](./krylov-step.md)'s six body-variant axes (preconditioner-present, orthogonalisation-variant, polynomial-kind, first-iteration-unrolled, restart-shape-on-the-body, in-place-buffer). The shared concerns are **restart** and **preconditioner**: at the body level (`krylov-step`) the kernel is restart-*agnostic* and the preconditioner application is per-step; at the driver level (`ksp_solve`) the solver-method axis owns the restart fold and the preconditioner-side axis shapes the residual proxy. The two appearances are complementary, not duplicated — the kernel does the per-step work, the driver owns the loop shape.

## Status

`firm` — the convergence-test fold of the [`krylov-step`](./krylov-step.md) kernel is the canonical L2 form for the preconditioned-Krylov outer-driver composition; the four-field result extraction, convergence predicate, restart nesting, and statistics-as-driver-side separation are all directly evidenced in the Palace per-method `Mult` bodies and the `IterativeSolver` base; the algebraic content is fold-terminal laws (operator-inverse, zero-RHS short-circuit, terminal-solution linearity, per-call referential transparency) inherited from the L1 fixed-point laws plus the inherited demand-pruning; the variant-axis profile is closed at six loop-shaping axes, complementary to `krylov-step`'s six body axes. The pattern is well-attested: the L0 driver bodies (CG `reference/palace/palace/linalg/iterative.cpp:361-486`; GMRES `:544-705`), the L1 collapse (firm [`L1/ksp_solve`](../L1/ksp_solve.md)), the L2 kernel half (firm [`krylov-step`](./krylov-step.md)), and the L3 iteration-rotation view (firm [`L3/ksp_solve`](../L3/ksp_solve.md)). This dispatch (cycle-021 wave-1) is the **driver-half L2 backfill** resolving the maturity-gradient inversion (firm L3 above an L2 stub) and closing the `ksp-solve-l2-promotion-non-identity-substantive-gap` plan item / OQ; it enacts **Identity-lowerings still require both L levels** + **Lower-level shared vocabulary takes priority** (CLAUDE.md §Methodology invariants). Both the L2↔L1 and L3↔L2 rotations are **non-identity** (see §"Lowers from" / §"Lifts to"), unlike the identity [`krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md) kernel theme.

## Lowers from

L2 `ksp_solve` lowers from L1 [`ksp_solve`](../L1/ksp_solve.md): the L1 form collapses the entire solve — loop, restart, kernel — into the opaque `(K, b) -> SolveResult` solver-as-operator. **This L2 entry opens that collapse into the kernel-fold composition.** The rotation is *not* identity: L1 opacity is opened at L2 (the [`krylov-step`](./krylov-step.md) kernel and the convergence-test fold that wraps it become visible); the L1 absorbed `krylov-method` axis re-surfaces as the L2 solver-method loop-shaping axis; the L1 absorbed preconditioner side re-surfaces as the residual-proxy effect of the preconditioner-side axis. The `SolveResult` boundary type is unchanged (so the rotation is on the body, not the boundary); the L1 fixed-point algebraic laws restate as L2 fold-terminal laws. The per-step kernel that the L1 collapse hides surfaces at L2 in the *companion* [`krylov-step`](./krylov-step.md) entry, not here; `ksp_solve` is the driver, `krylov-step` is the kernel. The reverse direction (how the L1 collapse re-absorbs the L2 composition) and the firming evidence for the open are working-notes / OQ-ledger concerns, not chapter content, per the high→low discipline.

## Lifts to

L2 `ksp_solve` lifts to L3 [`ksp_solve`](../L3/ksp_solve.md): the L2 outer-driver-by-role composition becomes, at L3, the **explicit `iterate_while_L3` tail-recursive fold** with its **outer-loop `sequential-obstruction`** named. **This rotation is NOT identity-in-form.** L2 erases the iteration view (the fold is named by role — the convergence-test wrap of the kernel); L3 un-erases it (the fold is rendered as an explicit value-threaded tail recursion, and the obstruction "the iteration does not lift to a closed-form whole-tensor operation" is made first-class). This is the *complement* of the kernel hop: [`krylov-step`](./krylov-step.md) lowers body-identity (the kernel body maps line-for-line, per [`L3-L2/krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md)); `ksp_solve` lowers the loop *erasure* (L3 makes the fold explicit, L2 erases it to the role reference). The L3>L2 theme that narrates this fold→outer-driver-by-role consolidation forward (`L3-L2/ksp-solve-outer-driver`) is **pending** (cycle-021 wave-2 dispatch #3 authors it, now that this L2 entry is firm). This entry records only the rotation direction (L2 role-reference ⟷ L3 explicit fold) in-line per the high→low discipline; it does not author the theme.

## L2 vs L1 distinction

- **L1**: opaque solver-as-operator. `ksp_solve :: (K: Solver[A], b) -> SolveResult`. The loop *and* the kernel are invisible — a solve is one indivisible operator application. Krylov-method / element-type / initial-guess axes absorbed into the opaque `Solver[A]`. Algebraic laws are fixed-point properties stated directly on the operator.
- **L2**: outer-driver composition over the kernel. `ksp_solve :: (K, b) -> SolveResult` with body = convergence-test fold of [`krylov-step`](./krylov-step.md). The opacity is opened — the kernel and the fold are visible — but the *iteration view* stays erased (the fold is named by role, not rendered as explicit recursion). The L1 absorbed axes re-surface as loop-shaping axes. The L1 fixed-point laws become fold-terminal laws.

## L2 vs L3 distinction

- **L2**: outer-driver composition with the iteration view **erased** — the fold is referenced by *role* (the convergence-test / restart wrap of [`krylov-step`](./krylov-step.md)). No explicit recursion; no `sequential-obstruction` named at this layer.
- **L3**: value-threaded explicit fold `(op, K_0, s_0) -> (s_final, result)`. The iteration view is **load-bearing** — the outer tail-recursive loop is rendered explicitly, and the outer-loop `sequential-obstruction` is named. The L2>L3 lift un-erases the iteration view; the L3>L2 lowering re-erases it. Substantive (non-identity), the complement of the kernel's body-identity hop.

## Evidence

The L2 driver composition is read directly from the Palace per-method `Mult` bodies; the four-field result and convergence predicate are read from the `IterativeSolver` base; the kernel half is the firm [`krylov-step`](./krylov-step.md) entry. Citations self-verified against source this dispatch (CG in-loop `converged` at `:463` and GMRES restart loop at `:563` corrected from the L3 entry's `:464` / `:564`).

- `reference/palace/palace/linalg/iterative.cpp:361-486` — `CgSolver<OperType>::Mult` (def starts `:361`) — the canonical single-fold outer driver. Setup + pre-loop convergence test: `eps = max(rel_tol·initial_res, abs_tol)` (`:417`), `converged = (res < eps)` pre-loop short-circuit (`:418`); the outer-driver loop guard `for (; it < max_it && !converged; it++)` (`:427`); the per-step body folding `krylov-step` (the operator-apply `A->Mult(p, z)` at `:443`, the in-loop convergence test `converged = (res < eps)` at `:463`); result extraction `final_res = res; final_it = it;` (`:484-485`).
- `reference/palace/palace/linalg/iterative.cpp:544-705` — `GmresSolver<OperType>::Mult` (def starts `:544`) — the restart-nested double-fold outer driver. The outer restart loop `for (; it < max_it; restart++)` (`:563`); result extraction `final_res = beta; final_it = it;` (`:703-704`).
- `reference/palace/palace/linalg/iterative.hpp:25-115` — `IterativeSolver<OperType>` base class. The element-type axis (`OperType` template + `ScalarType` conditional, `:25-32`); the tolerance / `max_it` loop-control fields (`:42-46`); the four result fields `converged` / `initial_res` / `final_res` / `final_it` (`:52-55`); `GetConverged()` with its `rel_tol > 0 || abs_tol > 0` gate (`:98`); accessors `GetInitialRes` / `GetFinalRes` / `GetNumIterations` (`:101-108`).
- `reference/palace/palace/linalg/ksp.cpp:296-309` — `BaseKspSolver<OperType>::Mult` — the cumulative-statistics wrapper *above* this operator: `ksp->Mult(x, y)` (`:300`, the per-method fold this L2 entry composes), the `GetConverged()` check + `Mpi::Warning` (`:301-306`), the counter increments `ksp_mult++` / `ksp_mult_it += GetNumIterations()` (`:308-309`). Evidence that the cumulative counters are driver-side, above the per-solve composition.
- `reference/palace/palace/linalg/ksp.cpp:34-58` — `ConfigureKrylovSolver` factory switch on the `KrylovSolver` enum: implemented arms CG / GMRES / FGMRES; MINRES / BICGSTAB / DEFAULT abort at `:53-56` (the solver-method axis is closed at three implemented arms). The `MFEM_ABORT` at `:56`.
- `reference/palace/palace/linalg/ksp.cpp:312-313` — explicit `BaseKspSolver` template instantiations for `Operator` and `ComplexOperator` (the element-type axis).
- `book/src/L2/krylov-step.md` (cycle-005 firm) — the L2 kernel half this operator folds. §Context establishes the kernel-plus-driver shape; §"Algebraic laws" (associativity / step-composition non-laws) cite the restart-as-outer-loop structure and the intrinsic step-boundary sequentiality this driver's fold is built over.
- `book/src/L1/ksp_solve.md` (firm) — the L1 collapse this entry opens. §Semantics (the opaque solver, soft-fail, statistics-as-driver-side), §"Algebraic laws" (the five laws that become fold-terminal here), §"Variant axes" (the krylov-method axis absorbed into opacity, re-exposed here at composition granularity).
- `book/src/L3/ksp_solve.md` (cycle-020 firm) — the L3 iteration-rotation view this entry lifts to. §"Iteration-rotation marker" names the outer-loop `sequential-obstruction`; §"Lowers to" records the L3>L2 rotation as substantive (non-identity), the same rotation this entry's §"Lifts to" records from the L2 side.
- `book/src/concepts/ksp_solve.md` — the methodology-era concept page (constructed-operator-companion-to-`apply_linop` framing; the divfree slice use). Cross-referenced, not duplicated.
- `book/src/concepts/convergence-test.md`, `book/src/concepts/solve-monad.md`, `book/src/concepts/solver-as-operator.md`, `book/src/concepts/derived-view-hoisting.md`, `book/src/concepts/variant-absorption.md`, `book/src/concepts/constructed-operators.md`, `book/src/concepts/apply_BA.md` — cross-cutting concept anchors (predicate surface, L4 driver, consumer framing, demand-pruning, body-variant absorption, preconditioner-side absorption).
```

```edit:book/src/L2/index.md
| [`ksp_solve`](./ksp_solve.md) | `(K: Solver[A], b: Tensor[N]) → SolveResult[N]` (body ≡ convergence-test `iterate_while` fold of `krylov-step op`) | **Outer-driver composition** above L1 `ksp_solve`. Wraps the [`krylov-step`](./krylov-step.md) kernel in the convergence-test / restart fold. **Direct L2 dep:** `krylov-step` (the folded kernel). L1 primitives + L2 named compositions (`orthogonalize`, `incremental-least-squares`) appear only *transitively* through `krylov-step`. Concepts: `convergence-test`, `solver-as-operator`, `solve-monad`, `derived-view-hoisting`, `variant-absorption`, `constructed-operators`, `apply_BA`. Establishes the **non-identity** L2↔L1 relationship (un-collapse of the L1 opacity) and the **non-identity** L3↔L2 relationship (L2 erases the iteration view, L3 un-erases it — theme `L3-L2/ksp-solve-outer-driver` pending). L0 anchors: CG `iterative.cpp:361-486`, GMRES `:544-705`, base `iterative.hpp:25-115`, driver wrap `ksp.cpp:296-309`. | `firm` (harvested cycle-021 wave-1; promoted from stub; closes plan item / OQ `ksp-solve-l2-promotion-non-identity-substantive-gap`; resolves the maturity-gradient inversion of the firm cycle-020 L3 entry above an L2 stub) |
```

```edit:book/src/SUMMARY.md
# REPLACE-IN-PLACE (de-stub the existing line-44 entry; NOT an append — an append would create a duplicate TOC link → build error)
OLD: - [ksp_solve (stub)](./L2/ksp_solve.md)
NEW: - [ksp_solve](./L2/ksp_solve.md)
```

## Operator content

The full firm body is inside the `edit:book/src/L2/ksp_solve.md` fence above. Key points:

- **Slug + one-line**: `ksp_solve` at L2 — the outer-driver composition that wraps the `krylov-step` kernel in a convergence-test / restart fold to produce a complete solve.
- **Signature**: `ksp_solve :: (K: Solver[A: LinearOperator[N, N]], b: Tensor[N]) -> SolveResult[N]`, body = `iterate_while (krylov-step op) s_init predicate`. `SolveResult` boundary type identical to the firm L1 entry (the rotation is on the body, not the boundary).
- **Semantics**: four-phase composition (setup+init_convergence ▷ outer-driver fold ▷ materialise_iterate ▷ extract_result), iteration view erased to a named-by-role wrap (the L3 concern is the explicit recursion + obstruction).
- **Algebraic laws**: four fold-terminal/structural laws that hold (terminal operator-inverse, zero-RHS short-circuit, terminal-solution linearity, per-call referential transparency) + inherited demand-pruning; six explicit non-laws (fold-merge/associativity, statistics-field linearity, exact apply_linop composition, nested-solve commutativity, bit-determinism across variants, identity/fold-lift).
- **Dependencies**: direct L2 dep on `krylov-step` (the folded kernel); L1 primitives + L2 named compositions transitive through the kernel; seven cross-cutting concepts.
- **Status**: `firm`.
- **Variant axes**: six loop-shaping (solver-method, element-type, preconditioner-side, convergence-criterion, initial-guess-policy, convergence-failure-policy), complementary to `krylov-step`'s six body axes.

## Supporting evidence

All L0 citations self-verified against `reference/palace/` source via `palace-codemap` `read_range` this dispatch:

- CG `Mult` def at `iterative.cpp:361`; `eps`/pre-loop `converged` at `:417-418`; loop guard `:427`; operator-apply `A->Mult(p,z)` at `:443`; in-loop `converged = (res < eps)` at **`:463`**; result write `final_res = res; final_it = it;` at `:484-485`.
- GMRES `Mult` def at `iterative.cpp:544`; restart loop `for (; it < max_it; restart++)` at **`:563`**; result write `final_res = beta; final_it = it;` at `:703-704`.
- `IterativeSolver` base: template + `ScalarType` element-type conditional `iterative.hpp:25-32`; tolerance/max_it `:42-46`; result fields `:52-55`; `GetConverged()` gate `:98`; accessors `:101-108`.
- `BaseKspSolver::Mult` wrapper `ksp.cpp:296-309` (`ksp->Mult` at `:300`, warning `:301-306`, counters `:308-309`); factory `:34-58` with MINRES/BICGSTAB/DEFAULT abort at `:53-56`; instantiations `:312-313`.

**Citation corrections vs. the L3 entry's starting set** (the L3 entry cited these, off-by-one from source): in-loop `converged` is at `:463` (L3 said `:464`); GMRES restart loop is at `:563` (L3 said `:564`). The L3 entry is append-only post-integration so I do not edit it; I flag the drift in Open questions for a future lifter/lowering-verifier pass.

## Open questions

- **L3 entry citation drift (`:463` / `:563`)**: `book/src/L3/ksp_solve.md` cites the CG in-loop `converged = (res < eps)` at `:464` (source `:463`) and the GMRES restart loop at `:564` (source `:563`) — each off-by-one. The L3 entry is firm + integrated (append-only), so this dispatch does not touch it; recommend a lowering-verifier or lifter pass correct the two anchors. Low severity (the surrounding ranges `:361-486` / `:544-705` are correct; only the inner point-citations drift).
- **L2 index Working Note staleness**: `book/src/L2/index.md` Working Note (last bullet, "L3 driver/kernel complementarity") says "`L3/ksp_solve.md` not yet on disk" and asks for a forward-reference to be added once it lands — but the L3 entry *did* land cycle-020. This dispatch's dep-map row edit makes the L2 entry firm but does not rewrite that Working Note (out of one-operator scope; it is index prose, not the operator row). Recommend the layer-intro-author refresh the L2 index Working Note to (a) drop the "not yet on disk" clause, (b) note the L2 `ksp_solve` is now firm, and (c) point the complementarity note at the now-firm `L3/ksp_solve.md`.
- **`L3-L2/ksp-solve-outer-driver` theme is the gated dependent**: this firm L2 entry unblocks cycle-021 wave-2 dispatch #3 (the abstractor/lifter authoring the L3>L2 theme narrating the fold→outer-driver-by-role consolidation forward). The theme is forward-referenced plain-text in this entry's §"Lifts to" and the dep-map row; it is NOT authored here (one-operator-per-dispatch + lowering-author-is-abstractor discipline).
- **`materialise_iterate` for restarted methods**: the §Semantics phase-3 `materialise_iterate` (folding the last partial restart-cycle's basis correction `K.V · K.y` into `s.x`) leans on the GMRES restart-correction mechanics that live in the queued `incremental-least-squares` L2 stub. When that stub firms, the restart-correction reference here may want tightening to cite it directly (currently it cites `krylov-step` §Semantics + `solve-monad` §"Worked example — GMRES"). Not blocking; noted for the `incremental-least-squares` harvester.
