# Slice: gmres (reduced)

This slice is the historical precursor to the cycle-005/006/007/008/009/010 krylov-step chain. The L1/L2/L3/L4-v0.1 forms below have been lifted to firm entries; this stub points at them and retains the unique material (the L4 v0.1→v0.6 self-rotation history) below.

**Firm entries that supersede this slice's L0/L1/L2/L3/L4-v0.1 content:**

- `book/src/L1/ksp_solve.md` (firm; cycle-007) — the variant-axis-collapsed L1 form. CG / GMRES / FGMRES all share the same `ksp_solve(K, b) -> SolveResult` signature; the per-method body is internal to `K`'s opaque type. This supersedes this slice's §"L1 — pure-functional dataflow".
- `book/src/L1-L0/ksp-solve-mutation-rotation.md` (rough-in; cycle-008) — the mutation rotation theme. Sub-patterns A (outer `BaseKspSolver::Mult`) / B (CG body) / C (GMRES body) / D (FGMRES body) cover the L1>L0 rewrite. This supersedes this slice's §"L0 — cited regions" line-range citations.
- `book/src/L2/krylov-step.md` (firm; cycle-005) — the L2 primitive composition. Five primitive groups (apply, optional auxiliary, iterate-update, scalar-update, output-readout); GMRES instance cited. This supersedes this slice's §"L2 — primitive composition".
- `book/src/L3/krylov-step.md` (firm; cycle-010 wave-1) — the L3 value-threaded form with the sequential-obstruction recorded. This supersedes this slice's §"L3 — global tensor-field form" (the LS-update / back-solve sequential obstructions on small-dense state).
- `book/src/L3-L2/krylov-step-body-identity.md` (firm; cycle-009) — the L3>L2 identity-in-form theme.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` (firm; cycle-008) — the L4>L3 typed-wrapper-dissolution theme.
- `book/src/L4/krylov-step.md` (firm; cycle-006) — the L4 typed wrapper Form A / Form B. This supersedes this slice's §"L4" v0.1 (the `SimState` / `OpParams` / `Krylov` typing, `solve_loop` / `restart_cycle` / `inner_loop` monadic structure, `Convergence` value).
- `book/src/L1-L0/minres-iteration.md` + `book/src/L1-L0/bicgstab-iteration.md` (firm; cycle-004) — the obstruction themes covering the unimplemented Krylov methods.

**Unique material retained below**: the L4 v0.2 → v0.3 → v0.4 → v0.5 → v0.6 self-rotation progression. This documents the canonical derivation of `build_convergence` / `classify_outcome` / `check_stop` / `StopReason`-witness extraction. These are load-bearing methodology evidence for `concepts/derived-view-hoisting.md` and a candidate `concepts/witness-typed-dispatch.md` (per v0.6 §"Open questions" — promotion criterion is "second instance lands"). Pending lift to those concepts, the v0.2-v0.6 sections are retained verbatim.

**Open questions still pending lift (from the now-stubbed §"L1 Open questions"):**
- The L0.11a drift-warning compare (10% threshold at `iterative.cpp:592-600`) is not yet cited in firm entries. This is an observability hook on the LS-proxy-vs-true-residual numerical drift.
- The `givens_generate` / `givens_apply` L2 primitive vocabulary exists as firm concept pages (`book/src/concepts/givens_generate.md` and `book/src/concepts/givens_apply.md`) but is NOT promoted as firm L1 operators (the firm L2 `krylov-step` stays at the five-group level and elides Givens-rotation primitives at the operator level). Promotion criterion: simplifies higher forms — likely yes for the GMRES `ls_update_column` decomposition.

---

## L4 v0.2 — convergence-criterion absorption tightening

The L4 v0.1 form above introduced `build_convergence` as a third constructed-operator surface alongside `initial_residual`, `apply_BA`, `apply_correction`. This is a self-rotation (L4→L4): the form does not advance a layer, it tightens the v0.1 form by closing two gaps that the original prose left implicit.

### Gap 1 — `derive_ir` is unspecified in v0.1

The v0.1 `restart_cycle` body contains:

```haskell
put s{ x = x', initial_res = (if isUnset s.initial_res then derive_ir op b β else s.initial_res) }
```

but `derive_ir` is never defined. The intended value is precisely the `ε0` computed inside `build_convergence` — the initial-residual scale that drives the relative-tolerance test. v0.1 leaks this duplication: the same dispatch (`initial_guess`? · `pc_side == LEFT`?) is performed twice, once by `derive_ir` (to populate `SimState.initial_res`) and once by `build_convergence` (to compute `ε0`).

The tightening: `build_convergence` returns both `ε` and `ε0`, and `derive_ir` is deleted. The `Convergence` value becomes the single dispatch surface for the residual policy.

```haskell
data Convergence = Convergence
  { epsilon         :: real
  , initial_residual :: real           -- ε0 ; written to SimState.initial_res on first cycle
  , satisfied       :: real -> Bool
  }

build_convergence :: OpParams -> Vec -> real -> real -> Convergence
build_convergence op b β prior_initial_res =
  let ε0 = if isUnset prior_initial_res
             then if op.initial_guess
                     then (if op.pc_side == LEFT then nrm2 (op.M · b) else nrm2 b)
                     else β
             else prior_initial_res
      ε  = max (op.rel_tol * ε0) op.abs_tol
  in Convergence { epsilon = ε, initial_residual = ε0, satisfied = \β' -> β' < ε }
```

The `restart_cycle` body simplifies:

```haskell
restart_cycle op b = do
  s <- get
  let (r0, x') = initial_residual op b s.x
      β        = nrm2 r0
      conv     = build_convergence op b β s.initial_res
  put s{ x = x', initial_res = conv.initial_residual }
  -- ... rest unchanged
```

The `isUnset` check moves entirely into `build_convergence`; the outer code unconditionally writes `conv.initial_residual` because on subsequent cycles `build_convergence` returns the prior value unchanged. This is the v0.1 form's `derive_ir` gap closed.

### Gap 2 — `restart_cycle` re-inspects `op.max_it`

The v0.1 `restart_cycle` post-correction body contains:

```haskell
pure $ if conv.satisfied K.beta    then Done True
       else if s'.it == op.max_it  then Done False
       else                             Continue
```

The `s'.it == op.max_it` check is a second decision surface that reads `op.max_it` directly from `OpParams` — outside the constructed-operator helpers. By the variant-absorption discipline at L4 ([concept: variant-absorption](../../concepts/variant-absorption.md) levels (b) and (c)), the main `solve_loop` / `restart_cycle` / `inner_loop` should not branch on `OpParams` fields outside the named operator surfaces.

The fix: extend the constructed-operator surface to include a *budget* helper that classifies the inner-loop outcome. The `inner_loop` returns the `Krylov` value; `classify_outcome` is the pure function that maps `(Krylov, SimState.it)` to an `Outcome`. It is the L4 home for the inner-loop's three-way termination decision.

```haskell
data Outcome = Continue | Done Bool

classify_outcome :: OpParams -> Convergence -> Krylov -> int -> Outcome
classify_outcome op conv K total_it
  | conv.satisfied K.beta = Done True       -- LS residual proxy below ε
  | total_it == op.max_it = Done False      -- exhausted iteration budget
  | otherwise              = Continue        -- hit max_dim per-cycle, restart
```

The `restart_cycle` post-correction tail collapses to:

```haskell
  s' <- get
  pure (classify_outcome op conv K s'.it)
```

This moves the only remaining `op.max_it` re-inspection into `classify_outcome`, where it is co-located with the convergence check and the `max_dim` check. `restart_cycle` now reads only `op.max_it`/`op.max_dim` via the helpers; it never inspects variant axes directly.

Symmetrically, the `inner_loop` body's stop condition

```haskell
if conv.satisfied K3.beta || K3.j + 1 == op.max_dim || s.it == op.max_it
```

factors through a `should_stop_inner` predicate of the same shape:

```haskell
should_stop_inner :: OpParams -> Convergence -> Krylov -> int -> Bool
should_stop_inner op conv K total_it =
  conv.satisfied K.beta || K.j + 1 == op.max_dim || total_it == op.max_it
```

The `inner_loop` then reads:

```haskell
inner_loop op conv K = do
  let (w, z)      = apply_BA op K.j K.V[K.j]
      K1          = if op.flexible then K{ Z = K.Z `with` (K.j, z) } else K
      (v_next, h) = orthogonalize op (K1.V[0..K1.j]) w
      K2          = K1{ V = K1.V `with` (K1.j+1, v_next) }
      K3          = ls_update_column K2 h
  modify (\s -> s{ it = s.it + 1 })
  s <- get
  if should_stop_inner op conv K3 s.it
    then pure K3
    else inner_loop op conv K3{ j = K3.j + 1 }
```

The `op.flexible` read inside `inner_loop` remains — it gates the `Z` capture, which is the load-bearing FGMRES variant point. v0.1's design absorbed `flexible` into the `apply_BA` return (the `z` value); v0.2 retains the v0.1 capture-site convention rather than relocating it. The single `if op.flexible then ... else K` is the one acceptable variant-axis read in the main inner loop because the alternative (always allocating a `Z` slot and threading `⊥`) wastes memory in the non-flexible case.

### v0.2 constructed-operator surface

After the tightening, the variant-absorption invariant at L4 is realised by a closed set of operator helpers, each named once with its variant-axis dependency made explicit:

| helper                | reads                                                         | role                                                |
|-----------------------|---------------------------------------------------------------|-----------------------------------------------------|
| `initial_residual`    | `pc_side`, `initial_guess`                                   | residual at restart entry                            |
| `apply_BA`            | `pc_side`, (`Mk` if flexible)                                | constructed Krylov operator                          |
| `orthogonalize`       | `gs_orthog`                                                  | MGS/CGS/CGS2 dispatch                                |
| `apply_correction`    | `pc_side`, `flexible`                                        | basis selection + terminal M-apply                   |
| `build_convergence`   | `pc_side`, `initial_guess`, `rel_tol`, `abs_tol`             | ε computation + initial-residual scale               |
| `should_stop_inner`   | `max_dim`, `max_it`                                          | inner-loop termination predicate                     |
| `classify_outcome`    | `max_it`                                                     | restart-cycle outcome classifier                     |

`solve_loop`, `restart_cycle`, and `inner_loop` read `op.flexible` (one site, in `inner_loop`, for the Z-capture gate) and otherwise touch `OpParams` only by passing it to a helper. Levels (a) the unified invariant, (b) once-per-axis procedural dispatch, and (c) shape-stable primitive sequence are all preserved per [concept: variant-absorption](../../concepts/variant-absorption.md).

### Citations

- The `derive_ir` gap is the unspecified-function in v0.1's `restart_cycle` (this slice, §L4 above, the line `initial_res = (if isUnset s.initial_res then derive_ir op b β else s.initial_res)`).
- The `op.max_it` re-inspection is the v0.1 `restart_cycle` line `else if s'.it == op.max_it then Done False`.
- The constructed-operator pattern is documented at [concept: constructed-operators](../../concepts/constructed-operators.md).
- The variant-absorption levels (a/b/c) are documented at [concept: variant-absorption](../../concepts/variant-absorption.md).

## Context

# GMRES (Generalized Minimal Residual)



Palace's preconditioned GMRES solver for general (non-symmetric, possibly indefinite or complex) linear systems `A x = b`. Implemented in `palace/linalg/iterative.{hpp,cpp}` as `GmresSolver<OperType>` (with `FgmresSolver<OperType>` as a related slice — flexible preconditioning — not covered here). Selected by `KspSolver` when the operator is not SPD or the preconditioner is non-stationary.

## Background

The canonical formulation is *restarted preconditioned GMRES(m)* (Saad 2003 §6.5, Algorithm 6.11; Saad & Schultz 1986). The method minimizes `‖b − A x‖` (or `‖M^{-1}(b − A x)‖` under left preconditioning) over the affine subspace `x_0 + K_m(B, r_0)` where `B = M^{-1}A` (left) or `A M^{-1}` (right) and `m` is the restart dimension. Each restart cycle builds an orthonormal basis of `K_m` via Arnoldi, factorizes the resulting `(m+1) × m` upper-Hessenberg matrix incrementally via Givens rotations into upper triangular `R`, and reads off the residual norm from the last component of the transformed RHS without forming the iterate.

Variant axes the slice exposes (per [variant-absorption](../../concepts/variant-absorption.md)):
- **Preconditioning side**: left (`B = M^{-1}A`, residual is `M^{-1}r`) vs right (`B = A M^{-1}`, residual is `r`, iterate update applies `M^{-1}` to the basis combination).
- **Orthogonalization variant**: classical Gram-Schmidt (CGS), modified Gram-Schmidt (MGS), CGS with one reorthogonalization step (CGS2). Palace's `OrthogonalizationType` enum selects.
- **Restart dimension `m`**: configurable; on restart, the residual is recomputed and the basis is rebuilt.
- **Initial-guess handling**: `use_zero_initial_guess` short-circuits the initial matvec.

Deviations from textbook GMRES:
- Givens rotations are constructed with the [givens](../../concepts/givens.md) primitive (Palace defers to a scaled form that handles complex coefficients without underflow); see `GeneratePlaneRotation` and `ApplyPlaneRotation` in source.
- Convergence testing uses the *implicit* residual norm `|γ_{k+1}|` from the transformed RHS rather than recomputing `‖b − A x_k‖` (textbook standard, called out here because it interacts with right-preconditioning's residual semantics).

## L0 — cited source facts

All citations against `reference/palace`.

### L0.1 State carried across iterations of a restart cycle

Within one restart cycle of dimension up to `m`, `GmresSolver::Mult` maintains: current iterate `x`; residual `r`; basis vectors `V = [v_0, v_1, …, v_k]` (each a Vector, stored as a `std::vector<Vector>` or fixed Krylov array); upper-Hessenberg matrix `H ∈ C^{(m+1)×m}` (column-by-column populated); Givens rotation coefficients `(c_j, s_j)` for `j = 0..k`; transformed RHS vector `γ ∈ C^{m+1}` with `γ_0 = ‖r_0‖`, all later entries zero initially. The residual norm at step `k` is `|γ_{k+1}|`.

Citation: [palace/linalg/iterative.cpp:GmresSolver::Mult](../../../../reference/palace/linalg/iterative.cpp).

### L0.2 Initialization (per restart cycle)

Compute residual `r ← b − A x` (or `r ← b` if zero initial guess on first cycle). Apply preconditioner under left-precond: `r ← M^{-1} r`. Compute `β ← ‖r‖`; set `v_0 ← r / β`; set `γ_0 ← β`. The initial-cycle norm `β` on the first restart establishes the relative-tolerance baseline.

Citation: [palace/linalg/iterative.cpp:GmresSolver::Mult — restart initialization](../../../../reference/palace/linalg/iterative.cpp).

### L0.3 Per-Arnoldi-step body

At step `k` (0-indexed) of a restart cycle:
1. Apply `B = M^{-1}A` (left) or `A M^{-1}` (right) to `v_k` to obtain `w`.
2. Orthogonalize `w` against `V[0..k]` using the selected variant (CGS / MGS / CGS2), producing the column `H[0..k, k]` and the orthogonalized `w`.
3. Compute `H[k+1, k] ← ‖w‖`; if non-zero, set `v_{k+1} ← w / H[k+1, k]`.
4. Apply existing Givens rotations `(c_j, s_j)` for `j = 0..k-1` to the new Hessenberg column `H[:, k]` in place.
5. Generate a new Givens rotation `(c_k, s_k)` that zeros `H[k+1, k]` after applying it; apply it to `H[k:k+2, k]` and to `γ[k:k+2]`.
6. The current implicit residual norm is `|γ_{k+1}|`; convergence test against tolerance.

Citation: [palace/linalg/iterative.cpp:GmresSolver::Mult — Arnoldi loop body](../../../../reference/palace/linalg/iterative.cpp).

### L0.4 Solution reconstruction (at convergence or restart boundary)

When the loop exits at step `k_*`, solve the upper-triangular system `R y = γ[0..k_*]` via back-substitution, where `R` is the `(k_*+1) × (k_*+1)` upper block of the transformed `H`. Form the iterate update `x ← x + V[0..k_*] · y` (a `gemv` against the stored basis). Under right preconditioning, the update is `x ← x + M^{-1} (V[0..k_*] · y)`.

Citation: [palace/linalg/iterative.cpp:GmresSolver::Mult — solution reconstruction](../../../../reference/palace/linalg/iterative.cpp).

### L0.5 Restart

If the loop reaches the restart dimension `m` without converging, the iterate is updated as in L0.4, the basis and Hessenberg are discarded, and a new cycle begins from L0.2 using the updated `x` as the new initial iterate. The relative-tolerance baseline is *not* re-established.

Citation: [palace/linalg/iterative.cpp:GmresSolver::Mult — restart branch](../../../../reference/palace/linalg/iterative.cpp).

### L0.6 Orthogonalization variant dispatch

The `Orthogonalize` helper accepts the `OrthogonalizationType` enum and dispatches: MGS performs `k+1` sequential dot+axpy steps; CGS performs a batched dot block then a batched axpy block; CGS2 performs CGS twice (a one-step reorthogonalization). All variants produce the same column `H[0..k, k]` and orthogonalized `w` up to roundoff but differ in numerical stability and parallel-communication pattern.

Citation: [palace/linalg/iterative.cpp:Orthogonalize](../../../../reference/palace/linalg/iterative.cpp).

## L1 — coordinate-free statement

**State** (per [state-stratification](../../concepts/state-stratification.md)):
- Simulation state: `x` (iterate; externally visible).
- Operator-internal: `A`, `M`, and a *bound operator* `B` constructed at solve start (see below) — `B` internalizes the preconditioning-side choice so the Krylov procedure does not re-inspect that variant. Per [constructed-operators](../../concepts/constructed-operators.md).
- Ephemeral per restart cycle: a Krylov subspace `K_k = span(v_0, …, v_k)` represented by an orthonormal basis, an upper-Hessenberg coefficient `H` of `B`'s action on `K_k`, and the running [incremental-least-squares](../../concepts/incremental-least-squares.md) factorization of `H̄` (the `(k+1)×k` augmented matrix) into upper-triangular `R` with transformed RHS `γ`, sufficient to read off `‖γ_{k+1}‖` as the implicit residual norm.

**Invariant.** Let `B` be the bound preconditioned operator and `r_0` the preconditioned initial residual. At step `k` of a restart cycle, the iterate `x` minimizes `‖r_0 − B (x − x_0)‖` over `x_0 + K_k(B, r_0)`. Equivalently, the implicit residual norm tracked at L1 equals the true norm of `B`-projected residual for the current step.

**Procedure** (one restart cycle, coordinate-free):

1. **Bind** the preconditioned operator `B` once at the start of the solve from `(A, M, precond_side)`, producing a uniform `apply` interface. The per-step procedure does not re-inspect `precond_side`.
2. **Initialize** the cycle: form the preconditioned residual `r_0`, set `β = ‖r_0‖`, install `v_0 = r_0 / β` as the first basis vector and `γ_0 = β` as the initial transformed-RHS entry.
3. **Iterate** `k = 0, 1, …` until convergence or `k = m`:
   a. **Extend the Krylov basis**: apply `B` to `v_k` and orthogonalize against `K_{k-1}` (under the selected orthogonalization policy, bound at solve start), yielding the new basis vector `v_{k+1}` and the new Hessenberg column `H[:, k]`.
   b. **Update the running QR**: extend the incremental-least-squares factorization by one column; this absorbs `H[:, k]` into `R` and updates `γ`. The implicit residual norm `|γ_{k+1}|` becomes available.
   c. **Convergence test**: terminate if `|γ_{k+1}| ≤ tol`.
4. **Reconstruct the iterate**: solve `R y = γ[0..k]` and form `x ← x + (post-precond combination of) V · y`. The post-preconditioning step is encoded by `B`'s output convention (right-preconditioning applies `M^{-1}` to `V · y`; left applies identity).
5. **Restart** if not converged: discard `K, H, R, γ` and return to step 2 with the updated `x` as new initial iterate.

**Variant axes** and their absorption levels:
- `precond_side` (left/right): absorbed at level (a)+(b)+(c) via the [constructed operator](../../concepts/constructed-operators.md) `B`. Both prose, procedure, and primitive sequence are uniform.
- `orthogonalization_type` (CGS/MGS/CGS2): absorbed at level (a)+(b) via a bound orthogonalization policy. The per-step primitive sequence at L2 *will* differ (CGS uses a batched dot+axpy block, MGS uses sequential dot+axpy) — residual axis disclosed at L2.
- `restart_dim m`: parametric; mentioned once as the cycle bound.
- `use_zero_initial_guess`: parametric; binds the initial-residual computation.

## Open questions

- The orthogonalization variant has a residual L2 axis (primitive sequence differs); the L1 statement claims absorption at (a)+(b) only. Document the L2 divergence clearly when L2 lands.
- Right-preconditioning's `x ← x + M^{-1}(V · y)` requires an extra preconditioner apply at reconstruction time; whether `B`'s `apply` semantics absorb this or it is a separate `finalize` operation is a design choice. Current form treats it as a post-step of reconstruction.
- Whether `B` (constructed operator) is also the right abstraction for FGMRES — where the preconditioner changes per step — is a sideways question for the FGMRES slice.

## L4 v0.3 — single-cycle inner-loop predicate consolidation

The v0.2 form named `should_stop_inner` and `classify_outcome` as two separate predicates over `OpParams × Convergence × Krylov × int`. Read carefully, they share their entire decision basis — the three termination conditions `(conv.satisfied K.beta, K.j + 1 == op.max_dim, total_it == op.max_it)` — and differ only in how they encode the result: `should_stop_inner` collapses all three to `Bool`, `classify_outcome` distinguishes the convergence case from the budget-exhausted case from the restart case. This is a tightening of the v0.2 surface: the two helpers are two projections of one classifier, and naming them separately obscures that the inner-loop stop decision and the restart-cycle outcome decision are *the same decision*, made once per inner step.

v0.3 consolidates by having `inner_loop` return `(Krylov, Outcome)` directly, where `Outcome` is computed by a single `classify_outcome` call at the inner-loop stop point. The outer `restart_cycle` reads the `Outcome` rather than re-classifying. This eliminates the redundant `s' <- get` + `classify_outcome` call in `restart_cycle` and removes the duplicate three-way condition from the surface.

### Consolidated form

```haskell
-- One classifier, used at the inner-loop stop point.
classify_outcome :: OpParams -> Convergence -> Krylov -> int -> Outcome
classify_outcome op conv K total_it
  | conv.satisfied K.beta       = Done True       -- LS residual proxy below ε
  | total_it == op.max_it       = Done False      -- exhausted iteration budget
  | K.j + 1 == op.max_dim       = Continue        -- hit max_dim per-cycle, restart
  | otherwise                   = error "inner_loop stopped without a stop condition"

-- inner_loop returns the final Krylov and the Outcome that caused the stop.
inner_loop :: OpParams -> Convergence -> Krylov -> Solve (Krylov, Outcome)
inner_loop op conv K = do
  let (w, z)      = apply_BA op K.j K.V[K.j]
      K1          = if op.flexible then K{ Z = K.Z `with` (K.j, z) } else K
      (v_next, h) = orthogonalize op (K1.V[0..K1.j]) w
      K2          = K1{ V = K1.V `with` (K1.j+1, v_next) }
      K3          = ls_update_column K2 h
  modify (\s -> s{ it = s.it + 1 })
  s <- get
  case classify_outcome op conv K3 s.it of
    Continue | K3.j + 1 < op.max_dim ->            -- not yet at restart boundary
      inner_loop op conv K3{ j = K3.j + 1 }
    out -> pure (K3, out)

-- restart_cycle reads the Outcome from inner_loop; no re-classification.
restart_cycle :: OpParams -> Vec -> Solve Outcome
restart_cycle op b = do
  s <- get
  let (r0, x') = initial_residual op b s.x
      β        = nrm2 r0
      conv     = build_convergence op b β s.initial_res
  put s{ x = x', initial_res = conv.initial_residual }
  if conv.satisfied β
    then do modify (\s -> s{ converged = True, final_res = β }) ; pure (Done True)
    else do
      let K0 = fresh_krylov op β r0
      (K, outcome) <- inner_loop op conv K0
      let y = back_solve K
      modify (\s -> s{ x = apply_correction op K y s.x, final_res = K.beta
                     , converged = case outcome of { Done True -> True ; _ -> False } })
      pure outcome
```

The `should_stop_inner` helper is deleted. The `Outcome` type carries both "the inner loop should stop" (any `Done _` or boundary-`Continue`) and "the restart cycle should/shouldn't continue" — these are the same decision viewed from two sides of the inner-loop return.

### Why v0.2 was load-bearing-redundant

In v0.2, both `should_stop_inner` and `classify_outcome` read the same three conditions in the same order. The only difference was:

- `should_stop_inner`: `Bool` — "do I stop *now*?"
- `classify_outcome`: `Outcome` — "if I stopped, what happens next?"

But the inner loop already knew it had stopped (by virtue of returning), so the `classify_outcome` re-read in `restart_cycle` was reading the *same Krylov* and *same SimState.it* that triggered the `should_stop_inner` true-branch. The two helpers were a `Bool`-then-tag pattern that collapses cleanly to a single tag with a "don't stop yet" arm.

The consolidation preserves variant absorption at L4 — the only `OpParams` reads in `classify_outcome` are `op.max_it` and `op.max_dim`, the same two fields v0.2 read across both helpers. Levels (a/b/c) per [variant-absorption](../../concepts/variant-absorption.md) are preserved: (a) the invariant is unchanged; (b) the main loop dispatches once on the budget axes (inside `classify_outcome`); (c) the primitive sequence in the inner-step body is unchanged.

### v0.3 constructed-operator surface

| helper                | reads                                                         | role                                                |
|-----------------------|---------------------------------------------------------------|-----------------------------------------------------|
| `initial_residual`    | `pc_side`, `initial_guess`                                   | residual at restart entry                            |
| `apply_BA`            | `pc_side`, (`Mk` if flexible)                                | constructed Krylov operator                          |
| `orthogonalize`       | `gs_orthog`                                                  | MGS/CGS/CGS2 dispatch                                |
| `apply_correction`    | `pc_side`, `flexible`                                        | basis selection + terminal M-apply                   |
| `build_convergence`   | `pc_side`, `initial_guess`, `rel_tol`, `abs_tol`             | ε computation + initial-residual scale               |
| `classify_outcome`    | `max_it`, `max_dim`                                          | unified stop classifier (inner-loop AND restart)     |

One fewer row than v0.2. The `should_stop_inner` / `classify_outcome` pair becomes a single classifier with three arms (`Done True`, `Done False`, `Continue`) that doubles as the inner-loop stop predicate (any non-default arm) and the restart-cycle outcome (the arm itself).

### Citations

- The v0.2 redundancy: this slice, §L4 v0.2 — the two helpers `should_stop_inner` and `classify_outcome` read the same three conditions in the same order, with results differing only in encoding (`Bool` vs three-arm `Outcome`).
- The single-classifier pattern is a standard application of [variant-absorption](../../concepts/variant-absorption.md) level (b): when two dispatch surfaces share the same axis-reads, they are one surface.

### Open questions (L4 v0.3-specific)

- Whether the `Continue | K3.j + 1 < op.max_dim` guard in `inner_loop` should itself be folded into `classify_outcome` (returning a four-arm tag `{Done True, Done False, RestartContinue, InnerContinue}`) is a stylistic choice; the current form keeps the inner-loop / outer-loop boundary visible at the call-site. The four-arm form would push level (b) absorption one step further at the cost of a more granular tag set.

## L4 v0.4 — restart-pivot extraction (single residual-policy locus)

The v0.3 form consolidated `should_stop_inner` and `classify_outcome` into one classifier; the constructed-operator surface narrowed from seven helpers to six. This v0.4 tightening (also L4→L4, no layer advancement) closes one residual asymmetry the v0.3 surface still carries: **the convergence test fires at two structurally-distinct sites** — once on the freshly-computed initial residual `β` inside `restart_cycle` (the pre-loop short-circuit), and once on the LS proxy `K.beta` inside `classify_outcome` (the inner-loop / restart classification). v0.3 splits the residual policy across these two sites: the pre-loop site reads `conv.satisfied β` and writes `(converged = True, final_res = β)`; the post-correction site reads the inner-loop's returned `Outcome` and writes `(converged = (outcome == Done True), final_res = K.beta)`. The classifier is unified but the *application* of the classifier is not — `restart_cycle` still contains two separate SimState-write paths gated on the same `Convergence` value.

v0.4 extracts the SimState write into a single `commit_outcome` helper that takes the final residual proxy and the `Outcome`, leaving `restart_cycle` with one residual-policy decision-and-commit point per cycle iteration. The pre-loop short-circuit becomes `classify_outcome` called against a degenerate `Krylov` (where `K.beta = β` and `K.j = -1` so the `max_dim` arm cannot fire).

### Degenerate-Krylov classifier call

```haskell
-- A pre-Krylov classifier call: K.beta = β (the entry residual), K.j = -1
-- (so the K.j + 1 == max_dim arm cannot fire on a never-built basis).
classify_entry :: OpParams -> Convergence -> real -> int -> Outcome
classify_entry op conv β total_it
  | conv.satisfied β       = Done True
  | total_it == op.max_it  = Done False
  | otherwise              = Continue
```

This is the same three-arm shape as `classify_outcome` with the `max_dim` arm structurally absent — and `classify_entry` is in fact `classify_outcome` evaluated at the pre-cycle position. We name it separately only because the input shape differs (a scalar β rather than a `Krylov`); the body is one arm shorter.

### `commit_outcome` — the single SimState-write site

```haskell
commit_outcome :: real -> Outcome -> Solve ()
commit_outcome final_β outcome = modify $ \s -> s
  { final_res = final_β
  , converged = case outcome of { Done True -> True ; _ -> False }
  }
```

`commit_outcome` is the only place in the L4 form that writes `converged` and `final_res`. Both the pre-loop short-circuit and the post-correction commit route through it.

### v0.4 `restart_cycle`

```haskell
restart_cycle :: OpParams -> Vec -> Solve Outcome
restart_cycle op b = do
  s <- get
  let (r0, x') = initial_residual op b s.x
      β        = nrm2 r0
      conv     = build_convergence op b β s.initial_res
  put s{ x = x', initial_res = conv.initial_residual }
  s0 <- get
  case classify_entry op conv β s0.it of
    Done flag -> do commit_outcome β (Done flag) ; pure (Done flag)
    Continue  -> do
      let K0 = fresh_krylov op β r0
      (K, outcome) <- inner_loop op conv K0
      let y = back_solve K
      modify (\s -> s{ x = apply_correction op K y s.x })
      commit_outcome K.beta outcome
      pure outcome
```

The two SimState-write paths fuse: the only writes to `converged` / `final_res` happen via `commit_outcome`. The iterate update `x = apply_correction ...` is a separate concern (iterate evolution, not residual policy) and stays in `restart_cycle`.

### v0.4 constructed-operator surface

| helper                | reads                                                         | role                                                |
|-----------------------|---------------------------------------------------------------|-----------------------------------------------------|
| `initial_residual`    | `pc_side`, `initial_guess`                                   | residual at restart entry                            |
| `apply_BA`            | `pc_side`, (`Mk` if flexible)                                | constructed Krylov operator                          |
| `orthogonalize`       | `gs_orthog`                                                  | MGS/CGS/CGS2 dispatch                                |
| `apply_correction`    | `pc_side`, `flexible`                                        | basis selection + terminal M-apply                   |
| `build_convergence`   | `pc_side`, `initial_guess`, `rel_tol`, `abs_tol`             | ε + initial-residual scale                           |
| `classify_outcome`    | `max_it`, `max_dim`                                          | inner / post-correction stop classifier              |
| `classify_entry`      | `max_it`                                                     | pre-Krylov entry classifier (degenerate variant)     |
| `commit_outcome`      | —                                                            | single SimState write site for `converged`/`final_res` |

The surface grew by two rows but each row reads strictly *fewer* `OpParams` fields than v0.3's `classify_outcome` did across its two use-sites. `commit_outcome` reads no `OpParams` at all — it is a pure SimState writer, the most absorbed possible form.

### Why v0.3 was tight-but-not-tightest

v0.3's `classify_outcome` *value* was used uniformly, but v0.3's `restart_cycle` body still contained two separate `modify` blocks writing the same two SimState fields with the same `Convergence`-derived semantics — one inside the pre-loop short-circuit `if conv.satisfied β then ...`, one in the post-correction tail. From the [variant-absorption](../../concepts/variant-absorption.md) perspective, the residual-policy axis was absorbed at the *decision* layer (one classifier) but not at the *commit* layer (two write sites). v0.4 closes the commit-layer gap.

This is also a [derived-view-hoisting](../../concepts/derived-view-hoisting.md) move at the SimState level: `(converged, final_res)` is a derived view of `(outcome, final_β)`, and v0.3 computed that view twice in two locations. v0.4 hoists the view-computation into `commit_outcome`, called from two sites with the same arguments. The two call-sites remain (they observe distinct residuals — entry-β vs. K.beta) but the policy is centralized.

### Citations

- The v0.3 dual-write redundancy: this slice, §L4 v0.3 — the `if conv.satisfied β then ... pure (Done True)` block and the subsequent `modify (\s -> s{ ..., converged = case outcome of { Done True -> True ; _ -> False } })` both write `converged` and `final_res` from `Convergence`-derived semantics.
- The degenerate-classifier pattern (one helper with an arm structurally absent at one call-site) is a standard application of [variant-absorption](../../concepts/variant-absorption.md) where the unifying invariant covers both call positions but the input shape differs.
- The single-commit-site pattern is a [derived-view-hoisting](../../concepts/derived-view-hoisting.md) application at the monadic-write layer: the derived fields `(converged, final_res)` collapse to one write site.

### Open questions (L4 v0.4-specific)

- Whether `classify_entry` and `classify_outcome` should be unified into a single function taking a sum-typed argument (`PreKrylov real | PostKrylov Krylov`) is a stylistic question; the current split keeps the call-site shape obvious. The cost of the split is the duplicated `max_it`-arm; the cost of the union would be a more granular tag type. The split form is preferred for now because the `K.j = -1` sentinel in a unified form is uglier than the explicit two-function form.

## L4 v0.5 — unified classifier with positional sum

The v0.4 form extracted `commit_outcome` as the single SimState-write site for residual policy and introduced `classify_entry` as a degenerate variant of `classify_outcome` (the `max_dim` arm structurally absent). The v0.4 open question asked whether the two classifiers should be unified into one function taking a sum-typed argument (`PreKrylov real | PostKrylov Krylov`). v0.5 resolves that question affirmatively: the two classifiers share the same `(max_it, max_dim, conv)` decision basis and differ only in *which residual is read* and *whether `K.j + 1 == max_dim` is even askable*. A single classifier dispatching on the call-position tag closes the last residual asymmetry on the residual-policy axis.

This is again an L4→L4 self-rotation (no layer advancement). The motivation is twofold: (i) the [variant-absorption](../../concepts/variant-absorption.md) level (b) discipline ("the procedure dispatches once per axis") is currently satisfied per-call-site but not globally — `restart_cycle` calls two structurally-distinct classifiers; (ii) the [derived-view-hoisting](../../concepts/derived-view-hoisting.md) move v0.4 made at the *commit* layer has a symmetric move available at the *classify* layer.

### Unified classifier

```haskell
-- The position of the classifier call within a restart cycle.
-- PreKrylov carries the entry residual β; the max_dim arm is unreachable
-- because no basis exists. PostKrylov carries the post-inner-loop Krylov;
-- all three arms are reachable.
data Position = PreKrylov real | PostKrylov Krylov

classify :: OpParams -> Convergence -> Position -> int -> Outcome
classify op conv pos total_it = case pos of
  PreKrylov β ->
    if conv.satisfied β       then Done True
    else if total_it == op.max_it then Done False
    else                            Continue
  PostKrylov K ->
    if conv.satisfied K.beta  then Done True
    else if total_it == op.max_it then Done False
    else if K.j + 1 == op.max_dim then Continue   -- restart
    else                                error "PostKrylov classify on a non-stopped Krylov"
```

The `error` arm guards the invariant that `classify` at the `PostKrylov` position is only called after `inner_loop` has returned — i.e., the inner-step stop condition fired. This makes the `PostKrylov` arm total over its legitimate inputs.

The `inner_loop` body retains its in-line stop check (using `classify` at `PostKrylov`) and returns `(Krylov, Outcome)` as in v0.3 / v0.4:

```haskell
inner_loop :: OpParams -> Convergence -> Krylov -> Solve (Krylov, Outcome)
inner_loop op conv K = do
  let (w, z)      = apply_BA op K.j K.V[K.j]
      K1          = if op.flexible then K{ Z = K.Z `with` (K.j, z) } else K
      (v_next, h) = orthogonalize op (K1.V[0..K1.j]) w
      K2          = K1{ V = K1.V `with` (K1.j+1, v_next) }
      K3          = ls_update_column K2 h
  modify (\s -> s{ it = s.it + 1 })
  s <- get
  case classify op conv (PostKrylov K3) s.it of
    Continue | K3.j + 1 < op.max_dim ->
      inner_loop op conv K3{ j = K3.j + 1 }
    out -> pure (K3, out)
```

### v0.5 `restart_cycle`

```haskell
restart_cycle :: OpParams -> Vec -> Solve Outcome
restart_cycle op b = do
  s <- get
  let (r0, x') = initial_residual op b s.x
      β        = nrm2 r0
      conv     = build_convergence op b β s.initial_res
  put s{ x = x', initial_res = conv.initial_residual }
  s0 <- get
  case classify op conv (PreKrylov β) s0.it of
    Done flag -> do commit_outcome β (Done flag) ; pure (Done flag)
    Continue  -> do
      let K0 = fresh_krylov op β r0
      (K, outcome) <- inner_loop op conv K0
      let y = back_solve K
      modify (\s -> s{ x = apply_correction op K y s.x })
      commit_outcome K.beta outcome
      pure outcome
```

The `classify_entry` / `classify_outcome` pair is deleted; both call-sites route through `classify` with a `Position`-tagged argument.

### v0.5 constructed-operator surface

| helper                | reads                                                         | role                                                |
|-----------------------|---------------------------------------------------------------|-----------------------------------------------------|
| `initial_residual`    | `pc_side`, `initial_guess`                                   | residual at restart entry                            |
| `apply_BA`            | `pc_side`, (`Mk` if flexible)                                | constructed Krylov operator                          |
| `orthogonalize`       | `gs_orthog`                                                  | MGS/CGS/CGS2 dispatch                                |
| `apply_correction`    | `pc_side`, `flexible`                                        | basis selection + terminal M-apply                   |
| `build_convergence`   | `pc_side`, `initial_guess`, `rel_tol`, `abs_tol`             | ε + initial-residual scale                           |
| `classify`            | `max_it`, `max_dim` (PostKrylov only)                        | unified stop classifier (entry AND post-correction)  |
| `commit_outcome`      | —                                                            | single SimState write site for `converged`/`final_res` |

One fewer row than v0.4. The decision-basis-read for the residual policy is concentrated in exactly two helpers — `build_convergence` for the ε / initial-residual computation, `classify` for the stop / restart / continue decision — and the write is concentrated in `commit_outcome`. The remaining `OpParams` reads in the main loop body are `op.flexible` (once, in `inner_loop`, gating the `Z` capture) and the helpers themselves.

### Why the union form is the tightest viable

v0.4's split (two classifiers) preserved the call-site shape obviously: each call site read the residual it had naturally available (β at entry, K.beta post-correction). The cost was a duplicated `max_it` arm and the unstated invariant that `classify_entry`'s `max_dim` arm could not be relevant. v0.5 makes the call-position tag explicit (`PreKrylov` / `PostKrylov`), and pays back two things:

1. **Single dispatch surface.** The [variant-absorption](../../concepts/variant-absorption.md) level (b) requirement — "the procedure mentions the variant parameter at most once" — is now met for the *stop-decision axis* globally, not just per-call-site. There is one function name to read when asking "what makes the solve stop?".
2. **Total over legitimate inputs.** The `PostKrylov`-with-no-stop-condition path is an explicit `error`, surfacing the invariant that `classify` at that position is only called after `inner_loop` returns. v0.4 left this invariant implicit (it was a property of `restart_cycle`'s control flow, not of any helper's signature).

The stylistic cost is one new tag type (`Position`) and a four-arm case (counting the `error`). Compared to v0.4's two function names with duplicated arms, the tag-and-case form is the more compact and verifiable surface.

### Citations

- The v0.4 open question: this slice, §L4 v0.4 *Open questions* — "Whether `classify_entry` and `classify_outcome` should be unified into a single function taking a sum-typed argument (`PreKrylov real | PostKrylov Krylov`) is a stylistic question; ... the explicit two-function form ... is preferred for now because the `K.j = -1` sentinel in a unified form is uglier than the explicit two-function form."
- The resolution: a `Position` sum type replaces the sentinel — there is no `K.j = -1` ugliness because `PreKrylov` does not carry a `Krylov` at all. This was the load-bearing aesthetic objection in v0.4 and v0.5 closes it cleanly.
- The unified-classifier pattern is [variant-absorption](../../concepts/variant-absorption.md) level (b) applied globally across call sites, and [derived-view-hoisting](../../concepts/derived-view-hoisting.md) applied at the classify layer (symmetric with v0.4's commit-layer hoist).

### Open questions (L4 v0.5-specific)

- The `error "PostKrylov classify on a non-stopped Krylov"` arm encodes an invariant that could alternatively be expressed by refining the `PostKrylov` constructor to carry a witness of the stop condition (e.g., `PostKrylov Krylov StoppedAt` where `StoppedAt ∈ {Conv, MaxIt, MaxDim}`). The witness form would push the dispatch into the `inner_loop` body (where the stop condition is determined) and reduce `classify`'s `PostKrylov` arm to a pure pattern-match on the witness. This is a further [derived-view-hoisting](../../concepts/derived-view-hoisting.md) move — the witness is a derived view of the (Krylov, total_it, conv) state at the stop point — and could be pursued in a v0.6 tightening if a downstream slice motivates it. Not pursued here because the current form's `error` arm is informative enough.
- Whether the `op.flexible` read inside `inner_loop` (the one remaining variant-axis read in the main loop body) admits a similar consolidation — e.g., by always allocating a `Z` slot in `Krylov` and threading `⊥` in the non-flexible case, then moving the `op.flexible` read into `apply_BA` itself — is a separate question on a different axis. The current form preserves the v0.1 convention of capture-at-call-site for performance reasons (no `Z` allocation when not needed); a memory-vs-uniformity tradeoff that belongs to a memory-layout slice.

## L4 v0.6 — stop-witness extraction (eliminating the `error` arm)

The v0.5 form unified `classify_entry` / `classify_outcome` into a single `classify` function dispatching on a `Position` sum type, and concentrated the residual-policy write at `commit_outcome`. The v0.5 *Open questions* surfaced one residual asymmetry: the `PostKrylov` arm of `classify` contains an `error "PostKrylov classify on a non-stopped Krylov"` fallthrough that encodes a control-flow invariant (the `PostKrylov` arm is only reached after `inner_loop` returned because its stop check fired) as a partial pattern rather than a typed witness.

This v0.6 tightening (L4→L4 self-rotation, no layer advancement) eliminates the `error` arm by carrying the stop reason as a sum-typed witness on the `PostKrylov` constructor itself. The witness is computed at the *one* site where the stop condition is actually known — inside `inner_loop`, at the moment the loop decides to return — and `classify` becomes a total pattern match on the witness.

This is the [derived-view-hoisting](../../concepts/derived-view-hoisting.md) move v0.5 explicitly deferred: the witness is a derived view of `(K.beta, K.j, total_it, conv, op.max_dim, op.max_it)` at the stop point, and v0.5 recomputed it at the `classify` call site after `inner_loop` had already determined it. v0.6 hoists the computation to the determining site.

### Stop-witness as a sum type

```haskell
-- The reason the inner_loop stopped, witnessed at the stop site.
data StopReason
  = StoppedConverged    -- conv.satisfied K.beta fired
  | StoppedMaxIt        -- total_it == op.max_it fired
  | StoppedMaxDim       -- K.j + 1 == op.max_dim fired (restart)

-- The classifier position. PreKrylov carries the entry residual β;
-- PostKrylov carries the post-inner-loop Krylov AND the witness of why
-- inner_loop stopped. PostKrylov is no longer constructible without a witness.
data Position = PreKrylov real | PostKrylov Krylov StopReason
```

The `Position` type's `PostKrylov` constructor now requires a `StopReason` field. There is no longer a way to construct a `PostKrylov` value without committing to which stop condition fired — so the `classify` `PostKrylov` arm cannot encounter a non-stopped Krylov.

### Unified classifier becomes total

```haskell
classify :: OpParams -> Convergence -> Position -> int -> Outcome
classify op conv pos total_it = case pos of
  PreKrylov β ->
    if conv.satisfied β            then Done True
    else if total_it == op.max_it  then Done False
    else                                Continue
  PostKrylov _ StoppedConverged  -> Done True
  PostKrylov _ StoppedMaxIt      -> Done False
  PostKrylov _ StoppedMaxDim     -> Continue
```

The `PostKrylov` arms are now three pure pattern matches on the witness, each total over its constructor. The `op.max_it` / `op.max_dim` reads that v0.5 performed inside the `PostKrylov` body are gone from `classify`: they happened earlier, inside `inner_loop`, at the site that produced the `StopReason`. The `PreKrylov` arm is unchanged from v0.5.

Note the `Krylov` payload of `PostKrylov` is now unused in the `classify` body (the witness alone determines the outcome). It remains on the constructor because `restart_cycle` consumes it for `back_solve` and `apply_correction` after the `classify` call. An alternative shape would split the post-classification handoff so `classify` takes only the witness; the current form keeps the `Krylov` and witness paired in transit, which matches their actual lifetime as a single returned value from `inner_loop`.

### `inner_loop` produces the witness

```haskell
-- The stop check now produces a StopReason at the site where the condition
-- is determined, eliminating the recomputation in classify.
check_stop :: OpParams -> Convergence -> Krylov -> int -> Maybe StopReason
check_stop op conv K total_it
  | conv.satisfied K.beta        = Just StoppedConverged
  | total_it == op.max_it        = Just StoppedMaxIt
  | K.j + 1 == op.max_dim        = Just StoppedMaxDim
  | otherwise                    = Nothing

inner_loop :: OpParams -> Convergence -> Krylov -> Solve (Krylov, StopReason)
inner_loop op conv K = do
  let (w, z)      = apply_BA op K.j K.V[K.j]
      K1          = if op.flexible then K{ Z = K.Z `with` (K.j, z) } else K
      (v_next, h) = orthogonalize op (K1.V[0..K1.j]) w
      K2          = K1{ V = K1.V `with` (K1.j+1, v_next) }
      K3          = ls_update_column K2 h
  modify (\s -> s{ it = s.it + 1 })
  s <- get
  case check_stop op conv K3 s.it of
    Just reason -> pure (K3, reason)
    Nothing     -> inner_loop op conv K3{ j = K3.j + 1 }
```

`inner_loop` now returns `(Krylov, StopReason)` rather than `(Krylov, Outcome)`. The `Outcome` is derived from the `StopReason` at the `classify` site; the `StopReason` is the more primitive notion (it names *what fired*; the `Outcome` names *what the outer loop should do*). Separating them lets `classify` be the sole `Outcome`-producing site.

### v0.6 `restart_cycle`

```haskell
restart_cycle :: OpParams -> Vec -> Solve Outcome
restart_cycle op b = do
  s <- get
  let (r0, x') = initial_residual op b s.x
      β        = nrm2 r0
      conv     = build_convergence op b β s.initial_res
  put s{ x = x', initial_res = conv.initial_residual }
  s0 <- get
  case classify op conv (PreKrylov β) s0.it of
    Done flag -> do commit_outcome β (Done flag) ; pure (Done flag)
    Continue  -> do
      let K0 = fresh_krylov op β r0
      (K, reason) <- inner_loop op conv K0
      let y       = back_solve K
          outcome = classify op conv (PostKrylov K reason) (error "total_it unused")
      modify (\s -> s{ x = apply_correction op K y s.x })
      commit_outcome K.beta outcome
      pure outcome
```

The `total_it` parameter to `classify` is dead in the `PostKrylov` arms after the witness hoist — `classify` reaches its decision from `(pos, conv)` alone in the `PostKrylov` case. The `error "total_it unused"` in the call site marks this; a cleaner v0.7 would split the classifier signature so the `PostKrylov` form doesn't take `total_it` at all. We retain the current form because eliminating the unused parameter is a separate concern (signature compaction) from the witness extraction this section addresses; see Open questions.

### Why v0.5 was tight-but-leaky

v0.5's `classify` had a four-arm `PostKrylov` body — three productive arms plus the `error` fallthrough. The fallthrough encoded a control-flow invariant: "the `PostKrylov` position is only reached after `inner_loop` stopped because some condition fired". v0.5 made this invariant visible (the `error` message names it) but not type-enforced. A reader inspecting `classify` in isolation could not see *why* the fallthrough is unreachable — they had to read `inner_loop` and verify its return is gated on at least one stop condition firing.

v0.6 makes the invariant type-enforced: `PostKrylov` is constructible only with a `StopReason`, and `StopReason` is produced only by `check_stop` returning `Just`, and `check_stop` returns `Just` only when one of the three stop conditions fires. The chain from "PostKrylov is constructed" to "a stop condition fired" is now a sequence of typed constructors rather than a comment-load-bearing control-flow assumption.

This is [derived-view-hoisting](../../concepts/derived-view-hoisting.md) at the *witness layer*: the stop reason is a derived view of the (Krylov, total_it, conv, OpParams) state at the stop point, and v0.5 forced `classify` to re-derive it. v0.6 hoists the derivation to `check_stop`, the single site where the derivation is determinative.

### v0.6 constructed-operator surface

| helper                | reads                                                         | role                                                |
|-----------------------|---------------------------------------------------------------|-----------------------------------------------------|
| `initial_residual`    | `pc_side`, `initial_guess`                                   | residual at restart entry                            |
| `apply_BA`            | `pc_side`, (`Mk` if flexible)                                | constructed Krylov operator                          |
| `orthogonalize`       | `gs_orthog`                                                  | MGS/CGS/CGS2 dispatch                                |
| `apply_correction`    | `pc_side`, `flexible`                                        | basis selection + terminal M-apply                   |
| `build_convergence`   | `pc_side`, `initial_guess`, `rel_tol`, `abs_tol`             | ε + initial-residual scale                           |
| `check_stop`          | `max_it`, `max_dim`                                          | stop-witness producer (one site, total over inputs)  |
| `classify`            | (PreKrylov only: `max_it`)                                   | Outcome from Position + Convergence (total)          |
| `commit_outcome`      | —                                                            | single SimState write site for `converged`/`final_res` |

The surface grew by one row (`check_stop`) but every row is now total over its declared input domain. There is no `error` arm anywhere in the L4 form. The `PostKrylov` arm of `classify` reads zero `OpParams` fields — the witness has already absorbed the dispatch.

Variant absorption per [variant-absorption](../../concepts/variant-absorption.md) is preserved at all three levels: (a) the invariant is unchanged; (b) the budget axes `max_it` / `max_dim` are now read at exactly one site (`check_stop`) rather than at one site in `classify` plus zero elsewhere — strictly tighter; (c) the primitive sequence is unchanged.

### Citations

- The v0.5 `error` arm: this slice, §L4 v0.5 — the `classify` definition contains `| else → error "PostKrylov classify on a non-stopped Krylov"` as the `PostKrylov` fallthrough.
- The v0.5 open question naming the witness route: this slice, §L4 v0.5 *Open questions* — "the `error` arm encodes an invariant that could alternatively be expressed by refining the `PostKrylov` constructor to carry a witness of the stop condition (e.g., `PostKrylov Krylov StoppedAt` where `StoppedAt ∈ {Conv, MaxIt, MaxDim}`)". This is the v0.6 form, with `StopReason` replacing the open-question's `StoppedAt`.
- The witness-extraction pattern is [derived-view-hoisting](../../concepts/derived-view-hoisting.md) applied at the constructor layer: the derived view (the stop reason) is materialised at the construction site rather than recomputed at the consumption site.
- The `check_stop` / `classify` separation realises [variant-absorption](../../concepts/variant-absorption.md) level (b) at strictly-tighter granularity than v0.5: budget-axis reads collapse from "once at the `inner_loop` body's case, once at the `classify` PostKrylov body" (v0.5) to "once at `check_stop`, never at `classify`'s PostKrylov" (v0.6).

### Open questions (L4 v0.6-specific)

- The `total_it` parameter to `classify` is dead in the `PostKrylov` case after the witness hoist; the v0.6 `restart_cycle` call site marks this with `error "total_it unused"`. A v0.7 would split `classify` into two functions (`classify_entry :: OpParams → Convergence → real → int → Outcome` and `classify_post :: Convergence → StopReason → Outcome`) to remove the dead parameter. This re-introduces two function names, which v0.5 deliberately consolidated — but the v0.7 split is on a different axis (signature compaction, not residual-policy unification), so it would not regress v0.5's level-(b) achievement. Not pursued here because the current `error "total_it unused"` is a minor blemish.
- Whether `check_stop` should return `Maybe StopReason` or `Either Krylov StopReason` (i.e., return the still-running Krylov in the Nothing case) is a stylistic question; the current form keeps `inner_loop`'s recursion structure obvious (the `Nothing` branch recurses, the `Just` branch returns) and is preferred.
- The witness approach generalises: any classifier whose dispatch tag is determined upstream of the classification site can be migrated to carry the tag as a constructor field. This is a candidate methodology concept ("witness-typed dispatch") that may warrant extraction if it recurs in other slices (Chebyshev's convergence-by-eigenvalue-band, GMG's coarse-grid-direct-solve trigger). Deferred until a second instance lands.
