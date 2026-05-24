# Slice: gmres

Lifts Palace's restarted GMRES and FGMRES solvers into L0 cited regions and an L1 pure-functional dataflow form. Three orthogonal variant axes are absorbed at L1: `pc_side ∈ {LEFT, RIGHT}`, `gs_orthog ∈ {MGS, CGS, CGS2}`, and `max_dim` (restart dimension; default = `max_it` ⇒ non-restarted). The (fixed-vs-flexible-preconditioner) axis is absorbed by promoting the per-step preconditioned vector `z` to threaded basis state `Z[j]` in FGMRES — see [concept: constructed-operators](../../concepts/constructed-operators.md) and [concept: variant-absorption](../../concepts/variant-absorption.md).

## L0 — cited regions

**Class definitions.**
- L0.1 `GmresSolver` class declaration. `palace/linalg/iterative.hpp:152–217` (definition). Template over `OperType ∈ {Operator, ComplexOperator}`; configuration setters for `gs_orthog`, `pc_side`, `max_dim`; workspace fields `V`, `H`, `s`, `cs`, `sn`.
- L0.2 `FgmresSolver` class declaration. `palace/linalg/iterative.hpp:219–276` (definition). Inherits from `GmresSolver`; constructor forces `pc_side = RIGHT`; `SetPreconditionerSide` rejects `LEFT` via `MFEM_VERIFY`; adds basis storage `Z`.

**Scalar / kernel routines.**
- L0.3 `GeneratePlaneRotation(dx, dy) → (cs, sn)`. `palace/linalg/iterative.cpp:73–108` (definition). LAPACK-style scaled Givens generation; real and complex specialisations.
- L0.4 `ApplyPlaneRotation(dx, dy, cs, sn)`. `palace/linalg/iterative.cpp:227–241` (definition). In-place 2×2 unitary update.
- L0.5 `InitialResidual(pc_side, A, B, b, x, r, z, initial_guess)`. `palace/linalg/iterative.cpp:244–250 / 252–284` (definition). Branches on `(pc_side, initial_guess)`.
- L0.6 `ApplyBA(pc_side, A, B, x, y, z)`. `palace/linalg/iterative.cpp:286–305` (definition). The variant-absorbed operator action; `z` is the preconditioned input on the `RIGHT` branch.
- L0.7 `OrthogonalizeIteration(gs_orthog, V, w, Hj, j)`. `palace/linalg/iterative.cpp:307–326` (definition). One-shot dispatch on `gs_orthog`.

**Workspace allocation.**
- L0.8 `GmresSolver::Initialize / Update`. `palace/linalg/iterative.cpp:488–542` (definition). Lazy/incremental allocation of `V`, `H`, `s`, `cs`, `sn`.
- L0.9 `FgmresSolver::Initialize / Update`. `palace/linalg/iterative.cpp:707–731` (definition). Adds `Z` allocation.

**Main solve loops.**
- L0.10 `GmresSolver::Mult` body — outer restart loop + initial-residual / convergence-test setup. `palace/linalg/iterative.cpp:543–615` (definition).
- L0.11 `GmresSolver::Mult` body — inner Arnoldi / Givens loop. `palace/linalg/iterative.cpp:616–668` (definition).
- L0.12 `GmresSolver::Mult` body — back-solve and solution update (LEFT / RIGHT split). `palace/linalg/iterative.cpp:669–706` (definition).
- L0.13 `FgmresSolver::Mult`. `palace/linalg/iterative.cpp:733–875` (definition). Differs from `GmresSolver::Mult` only in: (a) initial residual into `Z[0]`; (b) `ApplyBA(RIGHT, …, Z[j])` threading the preconditioned input into the basis; (c) uniform solution reconstruction `x ← x + Σ s[k] · Z[k]` with no terminal `M`-apply.

**Top-level dispatch.**
- L0.14 `IterativeSolver` explicit-template-instantiation declarations. `palace/linalg/iterative.cpp:877–880` (declaration).
- L0.15 `ksp.cpp` configuration call sites. `palace/linalg/ksp.cpp:40–96` (call_site). Constructs `GmresSolver` or `FgmresSolver` and wires `linear.max_size`, `linear.pc_side`, `linear.gs_orthog`.

## L1 — pure-functional dataflow

### State schema

The L1 state is the bundle the inner solve loop transforms; ephemeral scratch (the lazily-sized buffers from L0.8 / L0.9) is not state.

```ts
// Sim state — the externally-visible quantities the solver evolves.
type SimState = {
  x: Vec;                   // current solution iterate
  it: int;                  // total inner iterations consumed
  converged: bool;
  final_res: real;          // last computed residual proxy β
  initial_res: real;        // β set on first restart cycle (rel-tol scale)
}

// Operator internal params — fixed across a single Mult call.
type OpParams = {
  A: LinOp; B: LinOp | null;
  pc_side: 'LEFT' | 'RIGHT';
  gs_orthog: 'MGS' | 'CGS' | 'CGS2';
  max_dim: int; max_it: int;
  rel_tol: real; abs_tol: real;
  initial_guess: bool;
  flexible: bool;           // true ⇒ FGMRES (B varies per step); forces pc_side = RIGHT
}

// Ephemeral per-cycle Krylov state — reborn at each restart.
type Krylov = {
  V: Vec[];                 // orthonormal basis, length j+2 at step j
  Z: Vec[] | null;          // preconditioned basis (FGMRES only)
  H: Matrix;                // upper-Hessenberg, columns Hj
  s: Vec; cs: Vec; sn: Vec; // RHS of LS problem and rotation registers
  j: int;                   // current Arnoldi index
  beta: real;               // current LS residual proxy
}
```

The `Krylov` bundle is *internal* to the solve; it is reset at every restart and discarded at return.

### Building-block operations

Each is a pure (or in-place-with-clear-output) function on the schema above. Per-element kernels are referenced by role; the L2 slice will substitute concrete primitives.

- `initial_residual(op, b, x) → (r0, x')` — produces the quantity whose norm GMRES is minimising. For `pc_side = LEFT`: `r0 = M·(b − A·x)`. For `pc_side = RIGHT`: `r0 = b − A·x` (true residual; `M` is deferred to the update step). Honours `initial_guess`: when false, sets `x' ← 0` and `r0 = (LEFT ? M·b : b)`. Cites L0.5.
- `apply_BA(op, v) → (w, z)` — the *constructed operator* that absorbs `pc_side`. For `LEFT`: `w = M·(A·v)`, `z` unused. For `RIGHT`: `z = M·v`, `w = A·z`. For no preconditioner: `w = A·v`. In FGMRES the returned `z` is the per-step preconditioned vector that gets *threaded into* the basis `Z`. Cites L0.6. See [concept: constructed-operators](../../concepts/constructed-operators.md).
- `orthogonalize(gs_orthog, V[0..j], w) → (w', h)` — single-dispatch orthogonalisation; returns the projected vector and the column of projection coefficients of length `j+1`. Cites L0.7. See [concept: orthogonalization](../../concepts/orthogonalization.md).
- `ls_update_column(K, j, h_new) → K'` — incremental least-squares update of the LS problem for `‖β·e₁ − H̄_j · y‖₂`. Replays previously-recorded rotations on the new column, generates one new rotation from the column tail, applies it to the column and to the RHS, advances `β ← |s[j+1]|`. Numerically realised by Givens-rotation kernels at L2 (cites L0.3, L0.4) — at L1 the role is incremental triangularisation of the LS system.
- `back_solve(K, j) → y` — solve the (now triangular) upper-left `(j+1)×(j+1)` block of `H` against `s[0..j]`, in place. Cites L0.12.
- `apply_correction(op, K, y, j, x) → x'` — produce the solution update. For GMRES with `pc_side ∈ {LEFT, none}`: `x' = x + Σ_{k=0..j} y[k]·V[k]`. For GMRES with `pc_side = RIGHT` (fixed `M`): `t = Σ y[k]·V[k]; x' = x + M·t` (terminal `M`-apply). For FGMRES: `x' = x + Σ y[k]·Z[k]` (no terminal apply — each `Z[k]` already carries its step-specific `M_k`). Cites L0.12, L0.13.

### Procedure

The outer/inner structure is identical for GMRES and FGMRES; the (fixed-vs-flexible) axis is absorbed by the choice of basis (`V` vs. `Z`) the correction step closes over, and by whether `apply_BA` threads its preconditioned output into the basis.

```
gmres_solve(op: OpParams, b: Vec, x0: Vec) -> SimState:
  state = { x: x0, it: 0, converged: false, final_res: ∞, initial_res: ⊥ }
  for restart in 0, 1, 2, ...:
    (r0, state.x) = initial_residual(op, b, state.x)
    β = ‖r0‖₂
    if restart == 0: state.initial_res = (op.initial_guess ? ‖b‖₂ (LEFT: ‖M·b‖₂) : β); ε = max(op.rel_tol · state.initial_res, op.abs_tol)
    if β < ε: state.converged = true; state.final_res = β; return state
    K = fresh_krylov(); K.V[0] = r0 / β; K.s[0] = β; K.j = 0; K.beta = β
    while true:
      (w, z) = apply_BA(op, K.V[K.j])
      if op.flexible: K.Z[K.j] = z
      (K.V[K.j+1], h_new) = orthogonalize(op.gs_orthog, K.V[0..K.j], w)
      h_new[K.j+1] = ‖K.V[K.j+1]‖₂; K.V[K.j+1] /= h_new[K.j+1]
      K = ls_update_column(K, K.j, h_new)         // incremental LS triangularisation
      state.it += 1
      if K.beta < ε or K.j+1 == op.max_dim or state.it == op.max_it: break
      K.j += 1
    y = back_solve(K, K.j)
    state.x = apply_correction(op, K, y, K.j, state.x)
    state.final_res = K.beta
    if K.beta < ε: state.converged = true; return state
    if state.it == op.max_it: return state
```

The procedure mentions each variant axis at exactly one dispatch site:
- `pc_side` — inspected only inside `initial_residual`, `apply_BA`, `apply_correction`. The main procedure does not branch on it.
- `gs_orthog` — inspected only inside `orthogonalize`.
- `max_dim` — appears only in the inner-break test; `max_dim = max_it` collapses the outer loop to one iteration (the non-restarted case).
- `flexible` — inspected only at the `K.Z[K.j] = z` capture and inside `apply_correction`'s basis selection. FGMRES configures this once at construction.

Variant absorption at all three levels per [concept: variant-absorption](../../concepts/variant-absorption.md): (a) the invariant (minimise `‖b − A·x‖` over a Krylov / preconditioned-Krylov subspace) is unified; (b) the procedure dispatches once per axis; (c) the primitive sequence (`apply_BA → orthogonalize → ls_update_column → back_solve → apply_correction`) is shape-stable across all parameter combinations.

## Open questions

- The `OrthogonalizeColumnMGS / CGS / CGS2` internals (MPI collective shape, CGS2 refinement semantics) belong to a separate `orthog` slice. The L1 contract here is that `orthogonalize` is the sole dispatch point.
- No dedicated GMRES/FGMRES unit test exists under `palace/test/`; coverage is via `models/modeeigensolver.cpp` and `ksp.cpp` consumers. A regression-test slice may be warranted.
- `GeneratePlaneRotation` complex specialisation has substantially more branches than the real one — numerical equivalence on real-cast-to-complex inputs is an L2 / numerics concern.
- `CheckDot` NaN/Inf gating semantics (referenced from the inner loop's residual checks) is cross-cutting across all iterative solvers and not pinned here.
