---
layer: L3
operator: ksp_solve
firmness: firm
lowers_to:
  - book/src/L2/ksp_solve.md (substantive outer-driver consolidation; NOT identity-in-form)
lifts_from:
  - book/src/L1/ksp_solve.md (the opaque solver-as-operator collapse; this L3 entry is the iteration-rotation un-collapse of the L1 body's outer loop)
variant_axes:
  - krylov-method (CG single-loop / GMRES restart-nested / FGMRES restart-nested — selects loop nesting, not body)
  - element-type (real / complex)
  - initial-guess-policy (cold-start / warm-start — sets the residual-proxy denominator and the entry-iterate)
  - convergence-failure-policy (soft-fail-with-flag; the only Palace variant)
  - restart-shape (non-restarted / restarted-fixed-dim / restarted-adaptive — the outer-of-two loop for GMRES/FGMRES)
---

# ksp_solve

Value-threaded **outer-driver solve loop** for preconditioned Krylov solvers at L3 — the **iteration-rotation** rendering of the fold that drives [`krylov_step`](./krylov_step.md) to convergence. Consumes a closure-captured solver-parameters value `op`, an initial iterate-bundle / simulator-state pair, and produces the converged simulator-state plus the four-field solve result. This is the L3 *driver* that complements the L3 *kernel* [`krylov_step`](./krylov_step.md): the kernel is the foldable body (identity-in-form across the chain); `ksp_solve` is the **non-lifting fold over it** — the canonical instance of the outer-loop `sequential-obstruction` that `krylov_step` defers to its surrounding loop.

## Context

L3 is the iteration-rotation layer: global tensor-field operations expressed as `state' = f(state, params)`, with sequential obstructions named explicitly per [`sequential-obstruction`](../concepts/sequential-obstruction.md). `ksp_solve` at L3 is the value-threaded form of the per-solve outer loop — the tail-recursive `iterate_while_L3` fold that repeatedly applies `krylov_step`, tests convergence, and on exit extracts the four-field result. Where [`krylov_step`](./krylov_step.md) renders a *single* per-step transition `(op, K, s) -> (K', s', outputs)`, `ksp_solve` renders the *whole trajectory* `(op, K_0, s_0) -> (s_final, result)` — the fold over that transition.

The two L3 entries are complementary halves of one algorithm:

- [`krylov_step`](./krylov_step.md) — the **kernel**. Its body is L3-native (every primitive is whole-tensor by signature shape) and value-thread-isomorphic to L4/L2 across the chain. It carries no obstruction in its body.
- `ksp_solve` (this entry) — the **driver**. The fold over `krylov_step` does **not** lift to a closed-form whole-tensor operation because each step reads scalars (`α`, `β`, `ρ`, `ω`, `θ`) produced by the previous step, and the scalar dependence is not closed-form in the carry. This is the **outer-loop `sequential-obstruction`** that `krylov_step` §"Iteration-rotation marker" explicitly attributes to "the surrounding `iterate_while_L3` tail-recursion, not the `krylov_step` body itself". `ksp_solve` is that surrounding tail-recursion, made a first-class L3 entry.

This entry is the layer-coherence anchor for the *driver*: a reader at L3 can find the solve loop here, in L3 vocabulary, without reaching up to the L1 collapse ([`L1/ksp_solve`](../L1/ksp_solve.md), which makes the solver opaque) or down to L2. It is the enactment of **Identity-lowerings still require both L levels** *for the driver half* — except that here the L3>L2 rotation is **not** identity-in-form (see §"Iteration-rotation marker" and §"Lowers to"); the L3 entry records the genuine rotation, and the obstruction is part of the deliverable per [`L3/index`](./index.md) §Context.

### Relationship to the L1 collapse

[`L1/ksp_solve`](../L1/ksp_solve.md) collapses the entire method body — outer loop and all — into an **opaque** `ksp_solve :: (K: Solver[A], b) -> SolveResult`. That collapse is the *solver-as-operator* type rotation: at L1 the solve is one indivisible operator application, with the loop invisible. **This L3 entry is the un-collapse of that loop's iteration view.** The L1 form treats `K` as a black box that maps `b ↦ A⁻¹·b`; the L3 form opens the box and shows the loop. The element-type, initial-guess-policy, convergence-failure-policy, and krylov-method axes that L1 absorbs into the opaque `Solver[A]` are re-exposed here only insofar as they shape the *loop* (number of nested loops, the residual-proxy denominator, the result-extraction); the per-step body remains absorbed in `krylov_step`. The L1 algebraic laws (linearity in `b`, zero-RHS-zero-solution, operator-inverse, idempotent re-solve) are properties of the *fixed point* the L3 fold converges to; they are restated at L3 as trajectory-terminal properties (see §"Algebraic laws").

## Signature

```text
ksp_solve :: (op, K_0, s_0) -> (s_final, result)
```

where the fold is the L3 tail recursion over [`krylov_step`](./krylov_step.md):

```text
ksp_solve op K_0 s_0 =
  let s_init                = init_convergence op K_0 s_0     -- residual proxy + eps + converged_0
  let (K_n, s_n, outputs_n) = iterate_while_L3                -- the outer-driver fold
                                (krylov_step op)              --   body: the L3 kernel
                                (K_0, s_init)                 --   seed carry
                                (\s -> not s.converged && s.it < op.max_it)  -- predicate
  let s_final               = fold_iterate op K_n s_n         -- final iterate materialised into s.x
  let result                = extract_result s_final outputs_n -- the four-field readout
  in (s_final, result)
```

Shape contract (positional values; L3 has no `readonly` annotation and no monadic effect):

- **`op`** — solver-parameters value, closure-captured (first positional argument, never in the return position; the value flows in, never out). Carries the system operator `op.T : LinearOperator[N, N]` (or constructed `apply_BA` per the preconditioner-side variant), the optional preconditioner, the convergence-control scalars `op.rel_tol`, `op.abs_tol`, `op.max_it`, and (for restarted methods) `op.max_dim`. The same `op` value is threaded into every `krylov_step` invocation inside the fold. Variant absorption is a **documented invariant at L3**: the loop does not branch on a *body-shaping* field of `op` (those are absorbed in `krylov_step`); it branches only on the *loop-shaping* fields (`max_it`, `max_dim`, the krylov-method nesting). The L4 `readonly` typing that forbids re-inspection demotes to a documented invariant, verified by inspection.
- **`K_0`** — initial iterate-bundle value (the `K` of [`krylov_step`](./krylov_step.md)). Born at solve entry; for restarted methods, re-born at each restart-cycle boundary. The internal structure is slice-specific (CG: `{ r, z, p, β, α }`; GMRES: `{ V, H, s, cs, sn, β, j }`); this chapter names its positional role, not its fields.
- **`s_0`** — initial simulator-state value (the `s` of [`krylov_step`](./krylov_step.md)). Carries the persistent fields: `s.it: Int` (iteration counter, seeded at 0), `s.converged: Bool`, `s.x: Tensor[N]` (the externally-visible iterate, carrying the initial guess on entry when the warm-start policy is selected), and the scalar bookkeeping `s.initial_res: Real`, `s.final_res: Real`. The L4 `Solve = StateT SimState Identity` monad has dissolved; `s_0` flows in positionally, `s_final` flows out positionally.
- **result `(s_final, result)`** — a positional pair carrying the converged simulator-state `s_final` (value-threaded; `s_final.x` holds the approximate solution) and the four-field readout `result`. The `result` record is the L3 rendering of the L1 `SolveResult` minus `x` (which lives in `s_final.x`):

```text
result : {
  converged  : Bool,    -- s_final.converged; the L1 SolveResult.converged
  iterations : Int,     -- s_final.it;        the L1 SolveResult.iterations
  initial_res: Real,    -- s_final.initial_res
  final_res  : Real     -- s_final.final_res
}
```

These four fields are the L3 value-threaded analogues of the L0 `IterativeSolver` result-extraction surface `converged` / `initial_res` / `final_res` / `final_it` (`reference/palace/palace/linalg/iterative.hpp:52-55`; `GetConverged` at `:98`, accessors `GetInitialRes`/`GetFinalRes`/`GetNumIterations` at `:101-108`). At L0 they are mutable members written on solve exit (`final_res = res; final_it = it;` for CG at `reference/palace/palace/linalg/iterative.cpp:484-485`; `final_res = beta; final_it = it;` for GMRES at `:703-704`); at L3 they are positional projections of `s_final`.

The fold's predicate `\s -> not s.converged && s.it < op.max_it` is the **convergence test** (per [`convergence-test`](../concepts/convergence-test.md)). It is the L3 rendering of the L0 loop-guard `it < max_it && !converged` (`reference/palace/palace/linalg/iterative.cpp:427`) with the per-step convergence flag `converged = (res < eps)` (`:463`) folded into `s.converged` by the kernel's `outputs.residual_norm` readout. The threshold `eps = max(rel_tol·initial_res, abs_tol)` is established once at `init_convergence` (`reference/palace/palace/linalg/iterative.cpp:417-418`) and closure-captured.

Three pieces of L4 wrapper machinery are absent at L3 (inherited from the kernel's dissolution, applied to the driver):

1. **No `Solve` monad.** The L4 outer driver's `do`-block / `StateT` threading dissolves into the explicit `iterate_while_L3` tail recursion plus positional `(K, s)` threading; the convergence-flag `modify` becomes the predicate's read of `s.converged`. The L4 cap is [`L4/ksp_solve`](../L4/ksp_solve.md); this entry is its substantive (non-identity-in-form) L3 image.
2. **No `readonly` typing.** `op`'s loop-shaping fields (`max_it`, `max_dim`) are read but never written; the L1 "K is read-only at the call site" survives as the convention that `op` never appears in the return position.
3. **No L1 opacity.** The L1 form's opaque `Solver[A]` is *opened* at L3 — the loop and its body are visible. The element-type / krylov-method axes that L1 absorbs into opacity re-surface as loop-shaping variant axes (see §"Variant axes"), but only at the loop granularity; the body stays in `krylov_step`.

## Semantics

`ksp_solve` at L3 is the complete preconditioned-Krylov solve, expressed as a value-threaded fold `(op, K_0, s_0) -> (s_final, result)`. The body has four phases, in dataflow order:

1. **Convergence-test initialisation** (`init_convergence`). Establish the residual proxy and the threshold `eps = max(op.rel_tol · s.initial_res, op.abs_tol)`, and seed `s.converged` by the pre-loop test `res < eps`. The L0 anchor is `reference/palace/palace/linalg/iterative.cpp:417-418` (CG): the `eps` formula and the pre-loop `converged = (res < eps)` short-circuit (which makes a warm-started already-converged solve take zero iterations — the basis of the L1 idempotent-re-solve law). The residual-proxy denominator depends on the initial-guess policy: cold-start uses `‖b‖_B`-style proxy, warm-start uses the initial-residual proxy (`reference/palace/palace/linalg/iterative.cpp:395-415`).

2. **The outer-driver fold** (`iterate_while_L3 (krylov_step op) (K_0, s_init) predicate`). This is the L3 iteration rotation proper — the tail-recursive form of the L0 `for (; it < max_it && !converged; it++)` loop (`reference/palace/palace/linalg/iterative.cpp:427`). Each fold step is exactly one [`krylov_step`](./krylov_step.md) invocation; the kernel increments `s.it`, updates the iterate-bundle, and emits `outputs.residual_norm`; the predicate reads `s.converged` (set from `outputs.residual_norm < eps`, the L0 `converged = (res < eps)` at `:463`). The fold is published as a tail recursion per [`krylov_step`](./krylov_step.md) §Strawman-reference and the strawman `book/src/semantics/index.md` §3.7 `iterate_while` conventions.

3. **Final-iterate materialisation** (`fold_iterate`). For non-restarted methods (CG, Chebyshev) the running iterate `s.x` is updated in-bundle each step, so `fold_iterate` is identity (the final `s_n.x` is already correct). For restarted methods (GMRES, FGMRES) the externally-visible iterate is folded in *once per restart cycle* from the basis correction `K.V · K.y`; `fold_iterate` materialises the last partial restart-cycle's correction into `s.x`. The placement "iterate folded at restart boundaries, not per step" is inherited from [`krylov_step`](./krylov_step.md) §Semantics counter-increment discussion and `solve-monad` §"Worked example — GMRES".

4. **Result extraction** (`extract_result`). Project the four `result` fields from `s_final` plus the terminal `outputs`. The L0 anchor is the result-write tail of each method's `Mult`: `final_res = res; final_it = it;` (CG, `reference/palace/palace/linalg/iterative.cpp:484-485`); `final_res = beta; final_it = it;` (GMRES, `:703-704`). `converged` is `s_final.converged`; the L0 `GetConverged()` additionally gates on `rel_tol > 0 || abs_tol > 0` (`reference/palace/palace/linalg/iterative.hpp:98`) — that gate is a loop-shaping convention preserved at L3 as part of `extract_result`.

The **restart nesting** is a loop-shaping variant, not a body variant. CG is a single fold (`reference/palace/palace/linalg/iterative.cpp:427`). GMRES/FGMRES are a **double-nested** fold: the outer restart loop `for (; it < max_it; restart++)` (`reference/palace/palace/linalg/iterative.cpp:563`) wraps the inner Arnoldi-iteration fold. At L3 each fold dissolves independently into a tail recursion; the restart loop is the outer `iterate_while_L3` whose body re-seeds `K` (a fresh basis) and whose predicate is `it < max_it` (the inner fold owns the convergence flag). This is the same structure `krylov_step` §"Algebraic laws" (associativity non-law) cites as "slice-level restart logic is structured as an *outer* loop around the `krylov_step`-folding inner loop".

The **driver does not branch on the per-step body**: the kernel is `krylov_step op`, invoked uniformly; the krylov-method axis selects the *nesting* (single vs restart-nested) and the result-extraction proxy (`final_res = res` for CG's `√|β|` proxy; `final_res = beta` for GMRES's LS-residual proxy), not the kernel's body. This is what lets `ksp_solve` name the *role* (outer-driver fold) while `krylov_step` supplies the per-step shape.

The **statistics counters are driver-side accumulators above this operator**, exactly as at L1. The L0 `BaseKspSolver::Mult` (`reference/palace/palace/linalg/ksp.cpp:296-310`) wraps the per-method `ksp->Mult(x, y)` and increments cumulative counters `ksp_mult++` / `ksp_mult_it += GetNumIterations()` (`:308-309`); the non-convergence `Mpi::Warning` (`:303-306`) is a logged side effect. At L3 `ksp_solve` is the per-method `ksp->Mult` (the per-solve loop); the `BaseKspSolver::Mult` cumulative wrapper is *above* this operator — `result.iterations` is the per-call count, and the L0 cumulative `ksp_mult_it` is `Σ_calls result.iterations`. The warning is the caller's concern (the structured `result.converged` carries the same information). This separation keeps `ksp_solve` referentially transparent at the per-solve granularity.

### Iteration-rotation marker

L3 is the iteration-rotation layer, and `ksp_solve` **is** the iteration rotation for the Krylov-solve family: the L0 `for`-loop (`reference/palace/palace/linalg/iterative.cpp:427` for CG; `:563` for GMRES restart) re-expressed as a value-threaded tail recursion. **The fold does not lift to a closed-form whole-tensor operation.** The trajectory of carries `(K_0, s_0), (K_1, s_1), …, (K_n, s_n)` is intrinsically sequential because each `krylov_step` reads scalars produced by the previous step (`α = β / dot(Ap, p)` etc.), and these scalars are not closed-form in the carry. This is the **outer-loop `sequential-obstruction`** documented at the firm [`sequential-obstruction`](../concepts/sequential-obstruction.md) concept page and named by [`krylov_step`](./krylov_step.md) §"Iteration-rotation marker" as "a property of the surrounding `iterate_while_L3` tail-recursion, not of the `krylov_step` body itself". **`ksp_solve` is that surrounding tail-recursion.** Recording the obstruction is the deliverable here, per [`L3/index`](./index.md) §Context ("negative L3 results are part of the deliverable").

The obstruction is the *complement* of the kernel's lift: `krylov_step`'s body lifts as a whole-tensor operation (all primitives are L3-native); the fold over it does not. The pair `(krylov_step lifts, ksp_solve does not)` is the precise L3 statement of "the Krylov method's per-step work is GPU-parallel but its iteration is sequential" — the single most important fact about porting iterative solvers to a tensor backend.

## Algebraic laws

`ksp_solve` is a **fold**, not an algebra. The laws below are trajectory-terminal properties (laws about the fixed point the fold converges to) plus structural invariants; the L1 algebraic laws restate here as terminal properties because the L1 opaque operator *is* this fold's converged result.

1. **Terminal operator-inverse** (modulo tolerance; the load-bearing terminal law, inherited from [`L1/ksp_solve`](../L1/ksp_solve.md) law 3). For `op` whose system operator is `A`, `ksp_solve op K_0 s_0` with `s_0.x` seeded for RHS `b` produces `s_final.x ≈ A⁻¹·b`, exact in the limit `op.rel_tol, op.abs_tol → 0`, `op.max_it → ∞`. The fold converges to the fixed point of the Krylov iteration, which is the solution. The four `result` fields are the *finite-tolerance witnesses* of how close the terminal carry got: `result.final_res` bounds the gap, `result.converged` reports whether `eps` was met, `result.iterations` is the trajectory length.

2. **Zero-RHS / converged-warm-start short-circuit** (exact). When the pre-loop test `res < eps` holds (zero RHS, or warm start at the converged solution), the fold runs **zero** iterations: `result.iterations = 0` and `s_final.x = s_0.x`. This is the L0 short-circuit `converged = (res < eps)` before the loop (`reference/palace/palace/linalg/iterative.cpp:418`) combined with the loop guard `!converged` (`:427`). It is the L3 statement of the L1 idempotent-re-solve law (law 4) and the zero-RHS-zero-solution law (law 2): a fold whose predicate is false at the seed is identity on the iterate. **Consequence**: callers that assume `result.iterations ≥ 1` are wrong.

3. **Per-call referential transparency** (modulo the two load-bearing non-determinism sources). `ksp_solve op K_0 s_0` is a pure function of `(op, K_0, s_0)` — no mutable per-solver-instance state escapes (the L0 cumulative counters live in the `BaseKspSolver::Mult` wrapper *above* this operator, not inside the fold). The same inputs produce the same `(s_final, result)` modulo (a) reduction-tree non-associativity inherited transitively through `krylov_step`'s `dot`/`nrm2`/`apply_linop`, and (b) orthogonalisation-variant floating-point ordering (GMRES/FGMRES). This is the L3 rendering of the L1 "referentially transparent modulo two non-determinism sources" statement.

4. **Trajectory-length determinism within a fixed reduction tree**. For a fixed reduction-tree ordering and a fixed orthogonalisation variant, `result.iterations` is a deterministic function of `(op, K_0, s_0)` — the fold runs exactly until the predicate flips. This is a structural invariant of the tail recursion, not an algebraic identity; it is what makes the demand-pruning law (below) sound.

Laws that explicitly **do not** hold:

- **Lift of the fold to a single tensor-field op**. The trajectory `(K_0, s_0), …, (K_n, s_n)` does **not** lift to a closed-form whole-tensor operation in `n` steps — the **outer-loop `sequential-obstruction`** (§"Iteration-rotation marker"). The body is L3-native; the fold over the body is not. This is the load-bearing *non*-law and the reason `ksp_solve` is a distinct L3 entry from `krylov_step` rather than a corollary of it.
- **Fold-merge / associativity**. `ksp_solve op K_0 (state after a partial ksp_solve)` is **not** the same as a single `ksp_solve op K_0 s_0` with a combined predicate, for restarted methods — the restart re-seeds the basis `K` (discards the Krylov subspace), so the trajectory through two `max_dim`-bounded restart cycles is not the trajectory through one `2·max_dim`-bounded cycle. Inherited from [`krylov_step`](./krylov_step.md) §"Algebraic laws" (associativity non-law); this is why GMRES restart is an *outer* fold around the inner fold, not a flattened single fold.
- **Linearity of the result fields in `b`**. `result.iterations` / `result.initial_res` / `result.final_res` are **not** linear in the RHS — different RHSes generate different residual histories and take different trajectory lengths. Only the *terminal solution* `s_final.x` is linear in `b` (modulo tolerance, L1 law 1); the trajectory metadata is not. Inherited from [`L1/ksp_solve`](../L1/ksp_solve.md) law 1's explicit caveat.
- **Exact composition with `apply_linop`**. `apply_linop op.T (ksp_solve op K_0 s_0).s_final.x ≈ b` holds only within `eps`, not exactly, at finite tolerance — inherited from [`L1/ksp_solve`](../L1/ksp_solve.md). Iterative-refinement schemes that assume a zero residual after a solve must guard.
- **Bit-determinism across reduction-tree / orthogonalisation / initial-guess variants**. Inherited from [`L1/ksp_solve`](../L1/ksp_solve.md) (non-laws) and transitively from [`krylov_step`](./krylov_step.md). The fold's trajectory length and terminal `result.final_res` depend on the inner reduction tree, the orthogonalisation variant (GMRES/FGMRES), and the initial-guess policy at the bit level; the mathematical solution is the same, the floating-point realisation differs. Load-bearing per CLAUDE.md §"Optimization tricks vs. base algebra".
- **Commutativity of nested solves**. `ksp_solve op_1 _ (ksp_solve op_2 _ _).s_final` ≠ the swapped composition, since `A_1⁻¹ · A_2⁻¹` does not commute. Inherited from [`L1/ksp_solve`](../L1/ksp_solve.md).

### Inherited demand-pruning (Law 1 of `krylov_step`, lifted to the fold)

The fold's `result` fields are demand-pruned per [`derived-view-hoisting`](../concepts/derived-view-hoisting.md): if no consumer reads `result.iterations` / `result.initial_res` / `result.final_res`, the fold need not materialise the per-step `outputs.residual_norm` beyond what the convergence predicate requires. The convergence predicate *does* require the residual norm (it is the predicate's input), so `result.final_res` is never fully pruned — but the *per-step trajectory* of residual norms (used only for printing) is prunable, which is exactly the §3.8 trajectory-accumulator pruning that the L4>L3 theme `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` §"What the L3 form for `iterate_while` looks like" cites. Witnessed by the consumer surface: the four-scalar result is consumed at `reference/palace/palace/linalg/iterative.hpp:52-55` and the sole `palace/` caller of cumulative stats is `reference/palace/palace/linalg/ksp.cpp:296-310` — per-iteration trajectory consumption is absent in `palace/`, so the trajectory accumulator prunes.

## Dependencies

**Same-layer (L3)**:

- [`krylov_step`](./krylov_step.md) — the per-step kernel this operator folds. **Direct, load-bearing dependency**: `ksp_solve`'s body is `iterate_while_L3 (krylov_step op) …`. The kernel supplies the body; `ksp_solve` supplies the fold. This is the canonical L3 kernel/driver pair.
- The L3-native whole-tensor primitives appear only *transitively* through `krylov_step` ([`apply_linop`](./apply_linop.md), [`axpy`](./linear_combination.md#arity-specializations), [`axpby`](./linear_combination.md#arity-specializations), [`axpbypcz`](./linear_combination.md#arity-specializations), [`dot`](./inner_product.md#specializations), [`nrm2`](./inner_product.md#consumer-nrm2-and-matrix-weighted-norm), [`scal`](./linear_combination.md#arity-specializations)) — the driver does not call them directly; the kernel does.

**Cross-cutting concepts** (consumed unchanged across the chain):

- [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the iteration-rotation marker for **this** operator (the outer loop); `ksp_solve` is the canonical fold that carries it.
- [`convergence-test`](../concepts/convergence-test.md) — the stopping-predicate surface that drives the fold (the `\s -> not s.converged && s.it < op.max_it` predicate).
- [`solve-monad`](../concepts/solve-monad.md) — the L4 outer-driver surface; at L3 dissolved to the explicit `iterate_while_L3` tail recursion + positional `(K, s)` threading. The firm L4 cap that *consumes* this surface is [`L4/ksp_solve`](../L4/ksp_solve.md) (the `solve_loop` / `restart_cycle` / `Outcome` assembly this fold lowers from).
- [`solver-as-operator`](../concepts/solver-as-operator.md) — the consumer-side framing; the L1 collapse this entry un-collapses.
- [`derived-view-hoisting`](../concepts/derived-view-hoisting.md) — the demand-pruning algebra governing the `result`-field / trajectory-accumulator materialisation.
- [`state-stratification`](../concepts/state-stratification.md) — the three-stratum partition (`op` / `K` / `s`) the fold threads.
- [`variant-absorption`](../concepts/variant-absorption.md) — the body-variant absorption (in `krylov_step`); the driver's loop-shaping axes are *not* absorbed (they shape the fold).
- [`constructed-operators`](../concepts/constructed-operators.md) — the preconditioner-side absorption into `op.T`.

**Strawman reference**: `book/src/semantics/index.md` §3.7 is the conventions source for the `iterate_while` shape this operator renders as a tail recursion; the L3 rendering is published in [`krylov_step`](./krylov_step.md) §Strawman-reference and `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` §"What the L3 form for `iterate_while` looks like".

No L4 monadic vocabulary appears in the L3 signature (no `Solve`, no `modify`, no `do`-block); no L1 opacity appears (the loop is open). That is the discipline of the layer.

## Variant axes

Five axes, all **loop-shaping** (they shape the fold, not the per-step body — body axes live in [`krylov_step`](./krylov_step.md)):

1. **krylov-method** (`CG | GMRES | FGMRES`) — selects the **loop nesting**: CG is a single `iterate_while_L3` fold (`reference/palace/palace/linalg/iterative.cpp:427`); GMRES/FGMRES are a restart-nested double fold (outer restart loop `:563` wrapping the inner Arnoldi fold). Also selects the result-extraction residual proxy (`final_res = res` √|β| proxy for CG `:484`; `final_res = beta` LS-residual proxy for GMRES `:703`). The per-step body stays uniform (`krylov_step op`); only the nesting and the proxy differ. Absorbed into opacity at L1; re-exposed here at loop granularity.
2. **element-type** (`real | complex`) — the L0 `OperType ∈ {Operator, ComplexOperator}` template parameter (`reference/palace/palace/linalg/iterative.hpp:30-33`; instantiations `reference/palace/palace/linalg/ksp.cpp:312-313`). The fold structure is identical across element types; only the scalar field differs. Collapsed to one operator at L3 (parameterised by element type), as at L1.
3. **initial-guess-policy** (`cold-start | warm-start`) — sets the entry iterate (`s_0.x = 0` cold vs `s_0.x =` warm value) and the residual-proxy denominator in `init_convergence` (`reference/palace/palace/linalg/iterative.cpp:376-415` for CG). Affects `result.iterations` and `result.initial_res`, not the converged-solution algebraic property. Loop-shaping (it shapes the seed and the predicate denominator), not body-shaping.
4. **convergence-failure-policy** (`soft-fail-with-flag`) — the only Palace variant: the fold always returns the terminal iterate and reports `result.converged` (`reference/palace/palace/linalg/ksp.cpp:301-307` returns the iterate regardless; no hard-fail). At L3 the policy is implicit in `result.converged` being a `Bool` rather than a sum type (the L4 cap [`L4/ksp_solve`](../L4/ksp_solve.md) lifts it to an `Outcome` sum per [`solve-monad`](../concepts/solve-monad.md), where `Done False` is a first-class arm).
5. **restart-shape** (`non-restarted | restarted-fixed-dim | restarted-adaptive`) — for non-restarted methods (CG) the axis collapses to a single value (one fold); for GMRES/FGMRES it selects the outer restart loop's re-seed cadence (`max_dim`-bounded inner cycles, outer loop `reference/palace/palace/linalg/iterative.cpp:563`). This is the *outer* of the two loops; it is loop-shaping by definition.

These five are **distinct from** `krylov_step`'s six body-variant axes (preconditioner-present, orthogonalisation-variant, polynomial-kind, first-iteration-unrolled, restart-shape-on-the-body, in-place-buffer). The only shared axis is **restart-shape**: at the body level (`krylov_step`) the kernel is restart-*agnostic*; at the driver level (`ksp_solve`) restart-shape selects the outer loop. The two appearances are complementary, not duplicated — the kernel ignores restart, the driver owns it.

## Lowers to

L3 `ksp_solve` lowers to L2 [`ksp_solve`](../L2/ksp_solve.md) (the L2 outer-driver framing) via the firm L3>L2 theme [`ksp-solve-outer-driver`](../L3-L2/ksp-solve-outer-driver.md). **This rotation is NOT identity-in-form.** The L3 explicit tail-recursive `iterate_while_L3` fold consolidates into the L2 "outer-driver-by-role" reference — the same surface adjustment named for the kernel at [`krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md) ("L3 tail-recursive outer loop collapses to L2's outer-driver-by-role reference"), but for `ksp_solve` the loop *is* the operator, so the consolidation is the *whole* rotation, not a surface adjustment around an identity body.

The L3>L2 hop here is the *complement* of the krylov_step hop: `krylov_step` lowers body-identity (the kernel body maps line-for-line); `ksp_solve` lowers the loop *erasure* (L3 makes the fold explicit, L2 erases the iteration view to an outer-driver-by-role reference). The pair is the L3>L2 statement of "L2 erases the iteration view per `book/src/L2/index.md`".

## Lifts from

L3 `ksp_solve` lifts from L1 [`ksp_solve`](../L1/ksp_solve.md): the L1 form collapses the entire solve — loop and body — into the opaque `(K, b) -> SolveResult` solver-as-operator. **This L3 entry is the iteration-rotation un-collapse of that loop.** The lift is *not* identity: L1 opacity is opened at L3 (the fold and its predicate become visible); the L1 `SolveResult.x` becomes `s_final.x`; the L1 three structured fields become the `result` record; the L1 absorbed krylov-method / element-type / initial-guess axes re-surface as L3 loop-shaping axes. The L1 algebraic laws (linearity in `b`, operator-inverse, idempotent re-solve) become L3 *trajectory-terminal* laws — properties of the fixed point this fold converges to. The per-step body that the L1 collapse hides surfaces at L3 in the *companion* [`krylov_step`](./krylov_step.md) entry, not here; `ksp_solve` is the driver, `krylov_step` is the kernel.

This entry is the layer-coherence backfill for the driver half. The L1 collapse is the right L1 representation (a solve *is* one operator application at the BLAS-1-to-constructed-operator gate); the L3 un-collapse is the right L3 representation (L3 is the iteration-rotation layer, and the solve *is* an iteration). Each layer is coherent within itself.

## Evidence

The L3 fold structure is directly read from the Palace per-method `Mult` bodies; the four-field result and convergence predicate are read from the `IterativeSolver` base; the obstruction is inherited from the firm `krylov_step` entry.

- `reference/palace/palace/linalg/iterative.cpp:361-486` — `CgSolver<OperType>::Mult` — the canonical single-loop outer driver. Setup + pre-loop convergence test (`:417-418`); the outer-driver `for` loop `for (; it < max_it && !converged; it++)` (`:427`); the per-step body folding `krylov_step` (`:434-464`, with the in-loop convergence test `converged = (res < eps)` at `:463`); result extraction `final_res = res; final_it = it;` (`:484-485`).
- `reference/palace/palace/linalg/iterative.cpp:544-705` — `GmresSolver<OperType>::Mult` — the restart-nested double-loop outer driver. The outer restart loop `for (; it < max_it; restart++)` (`:563`); result extraction `final_res = beta; final_it = it;` (`:703-704`).
- `reference/palace/palace/linalg/iterative.hpp:25-115` — `IterativeSolver<OperType>` base class. The element-type axis (`OperType` template, `:30-33`); the four result fields `converged` / `initial_res` / `final_res` / `final_it` (`:52-55`); `GetConverged()` with its `rel_tol > 0 || abs_tol > 0` gate (`:98`); accessors `GetInitialRes` / `GetFinalRes` / `GetNumIterations` (`:101-108`); the tolerance / `max_it` loop-control fields (`:42-46`).
- `reference/palace/palace/linalg/ksp.cpp:296-310` — `BaseKspSolver<OperType>::Mult` — the cumulative-statistics wrapper *above* this operator: `ksp->Mult(x, y)` (the per-method fold this L3 entry renders), the `GetConverged()` check + `Mpi::Warning` (`:301-306`), the counter increments `ksp_mult++` / `ksp_mult_it += GetNumIterations()` (`:308-309`). Evidence that the cumulative counters are driver-side, above the per-solve fold.
- `reference/palace/palace/linalg/ksp.cpp:312-313` — explicit template instantiations for `Operator` and `ComplexOperator` (the element-type axis).
- `book/src/L3/krylov_step.md` (firm) — the L3 kernel half this operator folds. §"Iteration-rotation marker" attributes the outer-loop `sequential-obstruction` to "the surrounding `iterate_while_L3` tail-recursion, not the `krylov_step` body itself" — this `ksp_solve` entry IS that surrounding tail-recursion. §"Algebraic laws" (associativity non-law) cites the restart-as-outer-loop structure.
- `book/src/L2/krylov_step.md` (firm) — §Context: "krylov_step lives at L2, not L3 or L4. L3 is the iteration-rotation layer; the *outer* iteration of every Krylov method carries a `sequential-obstruction` at L3 … Putting `krylov_step` at L3 would conflate 'kernel exists' with 'kernel lifts'." Direct evidence that the L3 home for the *outer iteration* is a distinct entry — this one.
- `book/src/L1/ksp_solve.md` (firm) — the L1 collapse this entry un-collapses. §Semantics (the opaque solver, soft-fail, statistics-as-driver-side), §"Algebraic laws" (the five laws that become trajectory-terminal here), §"Variant axes" (the krylov-method axis absorbed into opacity, re-exposed here at loop granularity).
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` (firm) — §"What the L3 form for `iterate_while` looks like" publishes the L3 tail-recursion rendering of the outer loop with the §3.8 demand-pruning rule cited; the conventions source for this entry's fold rendering.
- `book/src/L2/ksp_solve.md` (firm) — the L2 outer-driver anchor this entry lowers to (rotation substantive).
- `book/src/L3-L2/ksp-solve-outer-driver.md` (firm) — the L3>L2 theme narrating the fold→outer-driver-by-role consolidation.
- `book/src/concepts/sequential-obstruction.md` (firm) — the canonical write-up of the outer-loop obstruction this operator carries.
- `book/src/concepts/convergence-test.md`, `book/src/concepts/solve-monad.md`, `book/src/concepts/solver-as-operator.md`, `book/src/concepts/derived-view-hoisting.md` — cross-cutting concept anchors (predicate surface, L4 driver, consumer framing, demand-pruning).
- `book/src/semantics/index.md` §3.7 — the `iterate_while` conventions source the L3 tail-recursion renders.

## L3 vs L1 distinction

- **L1**: opaque solver-as-operator. `ksp_solve :: (K: Solver[A], b) -> SolveResult`. The loop is invisible — a solve is one indivisible operator application. Krylov-method / element-type / initial-guess axes absorbed into the opaque `Solver[A]`. Algebraic laws are fixed-point properties (linearity in `b`, operator-inverse, idempotent re-solve) stated directly on the operator.
- **L3**: value-threaded outer-driver fold. `ksp_solve :: (op, K_0, s_0) -> (s_final, result)`. The loop is open — `iterate_while_L3 (krylov_step op) …`. The body is the companion [`krylov_step`](./krylov_step.md) kernel. The L1 absorbed axes re-surface as loop-shaping axes (nesting, residual proxy, seed). The L1 fixed-point laws become trajectory-terminal laws. The fold carries the **outer-loop `sequential-obstruction`** — the iteration does not lift, even though the body does.

## L3 vs L2 distinction

- **L3**: value-threaded explicit fold `(op, K_0, s_0) -> (s_final, result)`. The iteration view is load-bearing — the outer tail-recursive loop is rendered explicitly, and the outer-loop `sequential-obstruction` is named.
- **L2**: outer-driver framing with the iteration view erased — the loop is referenced by *role* only (the restart / convergence-test wrap of [`krylov_step`](../L2/krylov_step.md)). The L3>L2 hop erases the explicit fold to the role reference; this is a **substantive** rotation (the loop *is* the operator), not an identity — the complement of the kernel's body-identity hop.
