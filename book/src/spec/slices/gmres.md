# Slice: gmres

Lifts Palace's restarted GMRES and FGMRES solvers into L0 cited regions and an L1 pure-functional dataflow form. Three orthogonal variant axes are absorbed at L1: `pc_side ∈ {LEFT, RIGHT}`, `gs_orthog ∈ {MGS, CGS, CGS2}`, and `max_dim` (restart dimension; default = `max_it` ⇒ non-restarted). The (fixed-vs-flexible-preconditioner) axis is absorbed by promoting the per-step preconditioned vector `z` to threaded basis state `Z[j]` in FGMRES — see [concept: constructed-operators](../../concepts/constructed-operators.md) and [concept: variant-absorption](../../concepts/variant-absorption.md).

## L0 — cited regions

**Class definitions.**
- L0.1 `GmresSolver` class declaration. [`palace/linalg/iterative.hpp:155-217`](../../../../reference/palace/linalg/iterative.hpp#L155-L217) (definition; lines 152–154 are the doc-comment header, audit-tolerable extent). Template over `OperType ∈ {Operator, ComplexOperator}`; configuration setters for `gs_orthog`, `pc_side`, `max_dim`; workspace fields `V`, `H`, `s`, `cs`, `sn`.
- L0.2 `FgmresSolver` class declaration. [`palace/linalg/iterative.hpp:222-275`](../../../../reference/palace/linalg/iterative.hpp#L222-L275) (definition; lines 219–221 are the class-doc header, audit-tolerable extent). Inherits from `GmresSolver`; constructor forces `pc_side = RIGHT`; `SetPreconditionerSide` rejects `LEFT` via `MFEM_VERIFY`; adds basis storage `Z`. Note: the inherited workspace field `r` (declared in `GmresSolver` at iterative.hpp:194) is structurally dead in FGMRES — `FgmresSolver::Mult` never calls `r.SetSize` and uses `Z[0]` for the initial residual and `V[0]` as the unused LEFT-scratch parameter to `InitialResidual`.

**Scalar / kernel routines.**
- L0.3a `GeneratePlaneRotation` (real specialisation). [`palace/linalg/iterative.cpp:73-109`](../../../../reference/palace/linalg/iterative.cpp#L73-L109) (definition). LAPACK-style scaled Givens generation, real path.
- L0.3b `GeneratePlaneRotation` (complex specialisation). [`palace/linalg/iterative.cpp:112-224`](../../../../reference/palace/linalg/iterative.cpp#L112-L224) (definition). The complex path has substantially more branches than the real path (handling `dx = 0`, `|dx| ≥ |dy|` vs. `|dy| > |dx|` scaling); see the L2 open question.
- L0.4 `ApplyPlaneRotation(dx, dy, cs, sn)`. [`palace/linalg/iterative.cpp:227-241`](../../../../reference/palace/linalg/iterative.cpp#L227-L241) (definition; spans the real specialisation 227–232 and the complex specialisation 235–241, with the inter-function blank lines at 233–234). In-place 2×2 unitary update.
- L0.5a `ApplyB(B, x, y)` helper. [`palace/linalg/iterative.cpp:244-250`](../../../../reference/palace/linalg/iterative.cpp#L244-L250) (definition). Single LEFT-side preconditioner apply primitive used by `InitialResidual` and by the GMRES correction step.
- L0.5 `InitialResidual(pc_side, A, B, b, x, r, z, initial_guess)`. [`palace/linalg/iterative.cpp:253-285`](../../../../reference/palace/linalg/iterative.cpp#L253-L285) (definition). Branches on `(pc_side, initial_guess)`; calls `ApplyB` on the LEFT branch.
- L0.6 `ApplyBA(pc_side, A, B, x, y, z)`. [`palace/linalg/iterative.cpp:288-305`](../../../../reference/palace/linalg/iterative.cpp#L288-L305) (definition). The variant-absorbed operator action; `z` is the preconditioned input on the `RIGHT` branch (live for FGMRES, scratch-overwritten for fixed-`M` GMRES).

**Workspace allocation.**
- L0.8a `GmresSolver::Initialize`. [`palace/linalg/iterative.cpp:489-516`](../../../../reference/palace/linalg/iterative.cpp#L489-L516) (definition). Lazy allocation of `V`, `H`, `s`, `cs`, `sn` at `init_size = 5`.
- L0.8b `GmresSolver::Update`. [`palace/linalg/iterative.cpp:519-541`](../../../../reference/palace/linalg/iterative.cpp#L519-L541) (definition). Incremental growth (`add_size = 10`) of the same workspace.
- L0.9a `FgmresSolver::Initialize`. [`palace/linalg/iterative.cpp:708-718`](../../../../reference/palace/linalg/iterative.cpp#L708-L718) (definition). Adds `Z` allocation on top of `GmresSolver::Initialize`.
- L0.9b `FgmresSolver::Update`. [`palace/linalg/iterative.cpp:721-731`](../../../../reference/palace/linalg/iterative.cpp#L721-L731) (definition). Adds `Z` incremental growth.

**Main solve loops.**
- L0.10 `GmresSolver::Mult` body — outer restart loop + initial-residual / convergence-test setup. [`palace/linalg/iterative.cpp:544-611`](../../../../reference/palace/linalg/iterative.cpp#L544-L611) (definition). Ends at the V[0]/s reset line, strictly before the inner-loop `int j = 0;` initialisation.
- L0.11 `GmresSolver::Mult` body — inner Arnoldi / Givens loop. [`palace/linalg/iterative.cpp:613-648`](../../../../reference/palace/linalg/iterative.cpp#L613-L648) (definition). The `int j = 0;` init at 613 and the `for (;; j++, it++) {` header at 614 frame the loop body 615–647, with the closing brace at 648.
- L0.11a `GmresSolver::Mult` body — restart-cycle drift-warning compare (`|beta − true_beta| > 0.1·true_beta` ⇒ optional warning). [`palace/linalg/iterative.cpp:592-600`](../../../../reference/palace/linalg/iterative.cpp#L592-L600) (definition). The 10% threshold comparison is at line 592. Observability only; does NOT alter dataflow.
- L0.12 `GmresSolver::Mult` body — back-solve (651–659), solution update with LEFT/RIGHT split (660–678), and the post-correction convergence check (679–682). [`palace/linalg/iterative.cpp:651-682`](../../../../reference/palace/linalg/iterative.cpp#L651-L682) (definition). The RIGHT branch reuses `r` and `V[0]` as scratch for the `M·t` accumulator + apply.
- L0.13 `FgmresSolver::Mult`. [`palace/linalg/iterative.cpp:734-871`](../../../../reference/palace/linalg/iterative.cpp#L734-L871) (definition). Differs from `GmresSolver::Mult` only in: (a) initial residual into `Z[0]` (the `V[0]` argument to `InitialResidual` at lines 754–755 is the unused LEFT-scratch parameter on a RIGHT-side call); (b) `ApplyBA(RIGHT, …, Z[j])` threading the preconditioned input into the basis; (c) uniform solution reconstruction `x ← x + Σ s[k] · Z[k]` (lines 833–846) with no terminal `M`-apply.

**Top-level dispatch.**
- L0.14 `GmresSolver` / `FgmresSolver` explicit-template-instantiation declarations. [`palace/linalg/iterative.cpp:877-880`](../../../../reference/palace/linalg/iterative.cpp#L877-L880) (declaration). The `{Gmres,Fgmres}Solver<{Operator,ComplexOperator}>` instantiations.
- L0.15 `ksp.cpp` configuration call sites. [`palace/linalg/ksp.cpp:39-96`](../../../../reference/palace/linalg/ksp.cpp#L39-L96) (call_site). The `case KrylovSolver::GMRES:` branch starts at line 39; constructs `GmresSolver` or `FgmresSolver` and wires `linear.max_size`, `linear.pc_side`, `linear.gs_orthog`.

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

**Storage-vs-value note.** L0.8 / L0.9 allocate `V`, `H`, `s`, `cs`, `sn` (and `Z` for FGMRES) incrementally (`init_size = 5`, `add_size = 10`) and **reuse** the buffers across restart cycles — only the logical values are zeroed at restart (`s ← 0`, `V[0] ← 0`). The L1 `fresh_krylov()` is a dataflow fiction: the *values* are fresh at every restart, the *storage* is reused. This distinction is invisible at L1 and is the correct level of abstraction for the dataflow rotation; it surfaces again at L2/L3 as a memory-layout concern.

### Building-block operations

Each is a pure (or in-place-with-clear-output) function on the schema above. Per-element kernels are referenced by role; the L2 slice will substitute concrete primitives.

- `initial_residual(op, b, x) → (r0, x')` — produces the quantity whose norm GMRES is minimising. For `pc_side = LEFT`: `r0 = M·(b − A·x)` (one `ApplyB` call, L0.5a). For `pc_side = RIGHT`: `r0 = b − A·x` (true residual; `M` is deferred to the update step). Honours `initial_guess`: when false, sets `x' ← 0` and `r0 = (LEFT ? M·b : b)`. Cites L0.5, L0.5a.
- `apply_BA(op, v) → (w, z)` — the *constructed operator* that absorbs `pc_side`. For `LEFT`: `w = M·(A·v)`, `z` unused. For `RIGHT`: `z = M·v`, `w = A·z`. For no preconditioner: `w = A·v`. In FGMRES the returned `z` is the per-step preconditioned vector that gets *threaded into* the basis `Z`. Cites L0.6. See [concept: constructed-operators](../../concepts/constructed-operators.md).
- `orthogonalize(gs_orthog, V[0..j], w) → (w', h)` — single-dispatch orthogonalisation; returns the projected vector and the column of projection coefficients of length `j+1`. Cites L0.7. See [concept: orthogonalization](../../concepts/orthogonalization.md).
- `ls_update_column(K, j, h_new) → K'` — incremental least-squares update of the LS problem for `‖β·e₁ − H̄_j · y‖₂`. Replays previously-recorded rotations on the new column, generates one new rotation from the column tail, applies it to the column and to the RHS, advances `β ← |s[j+1]|`. Numerically realised by Givens-rotation kernels at L2 (cites L0.3, L0.4) — at L1 the role is incremental triangularisation of the LS system.
- `back_solve(K, j) → y` — solve the (now triangular) upper-left `(j+1)×(j+1)` block of `H` against `s[0..j]`, in place. Cites L0.12.
- `apply_correction(op, K, y, j, x) → x'` — produce the solution update. For GMRES with `pc_side ∈ {LEFT, none}`: `x' = x + Σ_{k=0..j} y[k]·V[k]`. For GMRES with `pc_side = RIGHT` (fixed `M`): `t = Σ y[k]·V[k]; x' = x + M·t` (terminal `M`-apply). For FGMRES: `x' = x + Σ y[k]·Z[k]` (no terminal apply — each `Z[k]` already carries its step-specific `M_k`). Cites L0.12, L0.13. The pure-functional form abstracts a buffer detail visible at L0: the RIGHT branch physically realises `t` and `M·t` in the scratch slots `r` and `V[0]`, both of which are clobbered — safe because the basis is discarded at restart/return. The L2 form will re-expose this as a `scratch_buffer` mutation pattern; the L1 contract is purely functional.

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
- No dedicated GMRES/FGMRES unit test exists under `palace/test/`; the `palace/test/**/*iterative*` glob returns empty. Coverage is via `models/modeeigensolver.cpp` and `ksp.cpp` consumers. A regression-test slice may be warranted.
- `GeneratePlaneRotation` complex specialisation has substantially more branches than the real one — numerical equivalence on real-cast-to-complex inputs is an L2 / numerics concern.
- `CheckDot` NaN/Inf gating semantics (referenced from the inner loop's residual checks) is cross-cutting across all iterative solvers and not pinned here.
- The recurrence-vs-direct residual drift check at restart (`|beta − true_beta| > 0.1·true_beta` ⇒ warning; L0.11a, `iterative.cpp:595–605`) is an observability hook on a known numerical drift between the LS-proxy residual `|s[j+1]|` and the explicit `‖b − A·x‖`. The 10% threshold is currently an unmotivated constant. Deferred to a numerics slice.
- The L1 dataflow form treats `Krylov` as fresh-per-restart; the L0 storage is physically reused (init_size=5, add_size=10 incremental allocation, zeroed-not-freed at restart per L0.8/L0.9). A memory-layout slice could pin the storage-reuse contract without affecting L1.

## L2 — primitive composition

The L1 building blocks unfold into the named tensor/scalar primitives below. The procedure shape is unchanged from L1; each L1 operation is realised as a fixed sequence of L2 primitives. Variant axes (`pc_side`, `gs_orthog`, `flexible`) remain absorbed: dispatch sites collapse to primitive-sequence choices, not control-flow re-inspection.

### Primitive vocabulary

- `axpy(α, x, y) → y'`: `y' = α·x + y`. See [concept: axpy](../../concepts/axpy.md).
- `dot(x, y) → r`: Euclidean / Hermitian inner product. See [concept: dot](../../concepts/dot.md).
- `nrm2(x) → ‖x‖₂`: realised as `sqrt(dot(x, x).real)`. See [concept: nrm2](../../concepts/nrm2.md).
- `scal(α, x) → x'`: `x' = α·x` (in-place rescale).
- `apply_linop(L, x, y) → y`: `y ← L·x`. The single primitive through which `A`, `M`, and `BA`-composites act. See [concept: apply_linop](../../concepts/apply_linop.md).
- `givens_generate(a, b) → (c, s)`: produce a 2×2 unitary `[[c, s*]; [−s, c]]` such that `c·a + s*·b = r ≥ 0`, `−s·a + c·b = 0`. Cites L0.3.
- `givens_apply((c, s), (a, b)) → (a', b')`: in-place 2×2 unitary update; `a' = c·a + s*·b`, `b' = −s·a + c·b`. Cites L0.4.

### L1 → L2 unfoldings

**`initial_residual(op, b, x)`.** Unfolds into one `apply_linop` (and one conditional `apply_linop` for `M`):
```
if not op.initial_guess: x ← 0; r ← b
else: apply_linop(op.A, x, Ax); r ← b; axpy(-1, Ax, r)        // r = b − A·x
if op.pc_side == LEFT: apply_linop(op.M, r, Mr); r ← Mr        // r = M·(b − A·x)
return (r, x)
```
The `pc_side == RIGHT` branch leaves `r` as the true residual.

**`apply_BA(op, v)`.** Unfolds into one or two `apply_linop` calls:
```
if op.pc_side == RIGHT:                    // FGMRES always lands here
  apply_linop(op.M, v, z); apply_linop(op.A, z, w)             // z = M·v; w = A·z
elif op.pc_side == LEFT:
  apply_linop(op.A, v, Av); apply_linop(op.M, Av, w); z = ⊥    // w = M·A·v
else: apply_linop(op.A, v, w); z = ⊥                           // w = A·v
return (w, z)
```

**`orthogonalize(gs_orthog, V[0..j], w)`.** Unfolds into a `dot`/`axpy` sequence whose shape is fixed by `gs_orthog` but whose primitives are uniform — `dot` to project, `axpy` to subtract. See [concept: orthogonalization](../../concepts/orthogonalization.md) for the per-variant `dot`/`axpy` count. At this layer:
```
for k in 0..=j:
  h[k] = dot(V[k], w)                       // (CGS / MGS / CGS2 differ in batching & repeats)
  axpy(-h[k], V[k], w)
h[j+1] = nrm2(w); scal(1/h[j+1], w)
return (w, h)
```
MGS performs `dot`+`axpy` in sequence per `k`; CGS batches all `dot`s then all `axpy`s; CGS2 repeats once. The L2 primitive set is the same; the L3 form (orthog slice) will pin the batching.

**`ls_update_column(K, j, h_new)`.** This is the load-bearing L1→L2 unfolding — the incremental-LS role is realised by stored Givens rotations plus one new rotation:
```
// (1) Replay stored rotations on the new column h_new[0..j+1].
for k in 0..j:
  (h_new[k], h_new[k+1]) = givens_apply((K.cs[k], K.sn[k]), (h_new[k], h_new[k+1]))
// (2) Generate a new rotation to zero h_new[j+1] against h_new[j].
(K.cs[j], K.sn[j]) = givens_generate(h_new[j], h_new[j+1])
// (3) Apply the new rotation to the column tail and to the RHS s.
(h_new[j], h_new[j+1]) = givens_apply((K.cs[j], K.sn[j]), (h_new[j], h_new[j+1]))   // h_new[j+1] = 0
(K.s[j], K.s[j+1])     = givens_apply((K.cs[j], K.sn[j]), (K.s[j], 0))              // s[j+1] = −sn[j]·s[j]
K.H[:, j] = h_new
K.beta = |K.s[j+1]|
return K
```
The LS-residual proxy `K.beta` updates in O(1) per step; no explicit LS solve runs inside the inner loop.

**`back_solve(K, j)`.** Standard back-substitution against the now-triangular `K.H[0..=j, 0..=j]`:
```
y[j] = K.s[j] / K.H[j, j]
for k in (j-1)..0:
  y[k] = K.s[k]
  for i in (k+1)..=j: y[k] -= K.H[k, i] · y[i]
  y[k] /= K.H[k, k]
return y
```
No per-element primitive substitution; this is a small dense O(j²) kernel on the LS state, not on field state.

**`apply_correction(op, K, y, j, x)`.** Unfolds into `axpy`s, with one optional terminal `apply_linop`:
```
if op.flexible:                              // FGMRES
  for k in 0..=j: axpy(y[k], K.Z[k], x)      // x += Σ y[k]·Z[k]
elif op.pc_side == RIGHT:                    // fixed-M GMRES, right
  t ← 0; for k in 0..=j: axpy(y[k], K.V[k], t)
  apply_linop(op.M, t, Mt); axpy(1, Mt, x)   // x += M·(Σ y[k]·V[k])
else:                                        // LEFT or no-preconditioner
  for k in 0..=j: axpy(y[k], K.V[k], x)      // x += Σ y[k]·V[k]
return x
```

### Primitive-sequence summary (per inner iteration)

With the unfoldings above, a single inner Arnoldi step is the fixed shape:

```
apply_BA          : 1× apply_linop  (no-pc) | 2× apply_linop  (LEFT or RIGHT)
orthogonalize     : (j+1)× dot, (j+1)× axpy, 1× nrm2, 1× scal     // MGS/CGS baseline
ls_update_column  : (j+1)× givens_apply, 1× givens_generate
// state.it += 1; convergence test on K.beta
```

This primitive sequence is shape-invariant across all variant axes (orthogonalisation differs only in `dot`/`axpy` ordering, not count of primitives; `pc_side` differs only in the `apply_linop` count inside `apply_BA`; `flexible` differs only in whether `z` is stored). Variant absorption is preserved at L2.

### Citations

- `givens_generate`, `givens_apply` ↔ L0.3, L0.4.
- The replay-then-generate-then-apply sequence inside `ls_update_column` ↔ L0.11 inner loop body (`palace/linalg/iterative.cpp:616–668`), which interleaves Arnoldi orthogonalisation, stored-rotation replay on the new column, new-rotation generation, and RHS update.
- The `apply_correction` three-way unfolding ↔ L0.12 (GMRES back-solve + LEFT/RIGHT split) and L0.13 (FGMRES uniform `Z`-based update).

### Open questions (L2-specific)

- The per-variant `dot`/`axpy` ordering for `orthogonalize` (MGS sequential vs. CGS batched vs. CGS2 repeat-once) is deferred to the `orthog` slice; the L2 primitive set is fixed here but the L3 global-tensor form will distinguish.
- The complex specialisation of `givens_generate` (L0.3) has additional branches for `dx = 0`, `|dx| ≥ |dy|` vs. `|dy| > |dx|` scaling; these are L2 numerical details, not new primitives.

## L3 — global tensor-field form

The L2 primitive composition lifts cleanly to global tensor-field operations for the field-level state (`x`, `b`, `V[k]`, `Z[k]`) — these are the per-DoF vectors over the mesh on which `A`, `M` act. The LS-side state (`H`, `s`, `cs`, `sn`, `y`) is small dense (size O(j) ≤ O(max_dim)) and is **not** field state; it does not lift. The inner Arnoldi step has one genuine sequential obstruction (incremental LS triangularisation), which is recorded as a first-class L3 result.

### What lifts to a global form

The field-side primitives identified at L2 each have a canonical global form:

- `axpy(α, x, y)`, `scal(α, x)`, `dot(x, y)`, `nrm2(x)` — pointwise / reduction over the global DoF index set. See [concept: tensor-field-lift](../../concepts/tensor-field-lift.md) for the L2→L3 lift template for the support-operator family.
- `apply_linop(L, x, y)` — `y = L · x` as a global linear map over the DoF field. `A` is an assembled (or matrix-free) operator on the field; `M` is the preconditioner as a field-to-field linear map. No per-element loop survives at L3.

With these lifts, the L2 sub-procedures rewrite as global statements:

**`initial_residual` (global).**
```
r0 = (initial_guess ? b − A·x : b);  x0 = (initial_guess ? x : 0)
r  = (pc_side == LEFT ? M · r0 : r0)
```

**`apply_BA` (global).**
```
pc_side == RIGHT:    z = M · v;   w = A · z
pc_side == LEFT:     w = M · A · v;   z = ⊥
pc_side == NONE:     w = A · v;       z = ⊥
```
The constructed operator at the field level is the composition `M ∘ A` (LEFT) or `A ∘ M` (RIGHT), with the FGMRES per-step `M_k` realised by re-evaluating `M·v` and threading `z` into `Z[k]`.

**`orthogonalize` (global, CGS shape).**
```
h[0..j] = Vᴴ_{0..j} · w           // batched projection: a single (j+1)×n × n vector product
w       = w − V_{0..j} · h[0..j]   // batched subtraction: a single n × (j+1) × (j+1) update
h[j+1]  = ‖w‖₂
w       = w / h[j+1]
```
This is the CGS / CGS2 form; the global tensor view treats `V_{0..j}` as an `n × (j+1)` tall-skinny matrix and the projection as a single tall-skinny-matrix transpose-times-vector reduction. MGS does not have a single-shot global form (its sequential `dot`+`axpy` per `k` is its defining characteristic) — this is an internal-to-`orthogonalize` obstruction routed to the `orthog` slice; the L1 dispatch site is unchanged.

**`apply_correction` (global).**
```
flexible:               x = x + Z_{0..j} · y     // tall-skinny × small dense: a single n×(j+1) × (j+1) product
pc_side == RIGHT:       t = V_{0..j} · y;  x = x + M · t
other:                  x = x + V_{0..j} · y
```
The `Σ_k y[k] · V[k]` accumulator collapses to one tall-skinny gemv at the field level.

### Obstruction: incremental LS triangularisation

**Claim (L3 obstruction).** `ls_update_column` does **not** lift to a global tensor-field operation, and this is structural rather than an artifact of presentation.

Reasoning. The inner Arnoldi loop maintains, after step `j`, a QR factorisation of `H̄_j` whose `R` factor is stored implicitly via the rotation registers `(cs, sn)` and the accumulated RHS `s`. Step `j+1` must:

1. Replay rotations `0..j` on the new column in order — rotation `k+1` operates on the output of rotation `k`. This is a sequential reduction over `k` with no associativity (the rotation matrices do not commute), so it does not collapse to a parallel reduction.
2. Read the resulting `(h[j], h[j+1])` pair to generate rotation `j` — a data dependency from the replay output to the generator.
3. Apply rotation `j` to the column tail and to the RHS `s` — uses the just-generated rotation.

The loop-carried dependency is on a small dense O(j) state (the rotation registers and the RHS), not on field state. No global field operation hides this; at the field level the inner step is a *scalar* recurrence over the rotation index. The LS state is not a tensor field in the L3 sense (no DoF index set), so there is no global form to lift into.

This is a classical *sequential algorithm* obstruction in the sense of [concept: sequential-obstruction](../../concepts/sequential-obstruction.md): the recurrence is on dense state of size O(j) where `j ≤ max_dim` is typically O(10²)–O(10³). The obstruction is benign — the per-step cost is O(j) FLOPS on a buffer that fits in cache, and the field-side work (one `apply_linop`, one batched orthogonalisation) dominates. There is nothing to vectorise; there is no field-level form. The L1 form of `ls_update_column` (incremental LS) is the L3 form, unchanged.

Alternative formulations considered: batched re-triangularisation of the full `H̄_j` from scratch each step (replaces an O(j) recurrence with an O(j²) blocked operation) — strictly worse cost and gains no parallelism in the regime where `j` is small enough to live in cache. Not pursued.

### `back_solve` (also not field state)

The terminal `back_solve(K, j)` operates on the same small dense `(j+1)×(j+1)` triangular state. The serial back-substitution is the textbook sequential triangular solve. As with `ls_update_column`, this is not field state and not a tensor-field operation; the L1 form is the L3 form. We mark it as a deferred-once, end-of-cycle scalar operation (no per-iteration cost in the inner loop) — see [concept: sequential-obstruction](../../concepts/sequential-obstruction.md) for the small-dense-state class.

### L3 inner-step shape

With the lifts and obstructions resolved, a single inner Arnoldi step at L3 is:

```
1. w = (pc_side-determined composition of A, M, optionally storing z into Z[j])    // global apply_linop chain
2. (h[0..j], w) = batched_project_and_subtract(V_{0..j}, w)                          // global CGS form
   h[j+1] = ‖w‖₂;  w = w / h[j+1]                                                    // global nrm2 + scal
3. ls_update_column(K, j, h)                                                          // sequential recurrence on O(j) dense state — does NOT lift
```

The field-side work (step 1, step 2) is fully global / tensor-field; the LS-side work (step 3) is an explicitly-recorded sequential obstruction on small dense state. Variant absorption is preserved: `pc_side` selects the global operator composition in step 1; `gs_orthog` selects the global form in step 2 (CGS / CGS2 are global; MGS is itself sequential and routed to `orthog`); `flexible` selects whether `z` is captured in step 1. The procedure shape is unchanged from L2.

### Citations

- The field-side lifts of `axpy` / `dot` / `nrm2` / `scal` / `apply_linop` follow the standard support-operator template — see [concept: tensor-field-lift](../../concepts/tensor-field-lift.md).
- The sequential-obstruction classification follows [concept: sequential-obstruction](../../concepts/sequential-obstruction.md); GMRES's `ls_update_column` and `back_solve` are recorded as the small-dense-state subcase.
- L0 backing for the sequential structure: `palace/linalg/iterative.cpp:616–668` (inner loop, the rotation replay / generate / apply sequence) and `palace/linalg/iterative.cpp:669–706` (back-solve).

### Open questions (L3-specific)

- The L3 form of `orthogonalize` for `gs_orthog == MGS` is itself a sequential obstruction (per-`k` `dot`+`axpy` chain). This is internal to the `orthog` slice and is the natural place to record that obstruction; the GMRES slice's L1 dispatch contract is unaffected.
- The CGS2 form (one CGS sweep, then a second corrective sweep) is two global batched operations in sequence; the second sweep's coefficients depend on the first sweep's output, so it does not collapse further. Also routed to `orthog`.
- Whether the FGMRES `Z[k]` storage admits a streaming / out-of-core form at the field level (avoiding `O(max_dim · n)` memory) is a memory-layout concern below L3 and is not pursued here.

## L4 — calculus form

The L3 form distinguished field-side state (`x`, `b`, `V[k]`, `Z[k]`) from small-dense LS-side state (`H`, `s`, `cs`, `sn`, `y`), and recorded `ls_update_column` / `back_solve` as sequential obstructions on dense O(j) state. L4 makes that distinction structural: sim state, operator internal params, and ephemeral per-cycle Krylov state are typed separately, and the inner solve threads the Krylov bundle monadically. The form is code-like-but-not-runnable; it pins the calculus contract the implementation must respect.

See [concept: state-stratification](../../concepts/state-stratification.md) and [concept: solve-monad](../../concepts/solve-monad.md) for the cross-cutting forms. The constructed-operator helpers (`initial_residual`, `apply_BA`, `apply_correction`) are the operator-internal surface through which variant absorption is preserved at L4 — they are the *only* sites that read `op.pc_side`, `op.gs_orthog`, `op.flexible`.

### Convergence-criterion absorption

The convergence test the inner loop fires on (`K.beta < ε` with `ε = max(rel_tol·initial_res, abs_tol)`) is the third constructed-operator surface at L4. The main `solve_loop` / `restart_cycle` / `inner_loop` never reads `op.rel_tol`, `op.abs_tol`, or `s.initial_res` directly; instead a `Convergence` value is built once per restart cycle and applied as a pure predicate. This pulls the residual-policy decisions (relative vs. absolute, initial-residual scaling, LEFT-side `M·b` rescaling for `initial_guess = false`) out of the main control flow and into a single dispatch surface — symmetric with how `apply_BA` absorbs `pc_side`.

```haskell
data Convergence = Convergence { epsilon :: real, satisfied :: real -> Bool }

build_convergence :: OpParams -> Vec -> real -> real -> Convergence
build_convergence op b β prior_initial_res =
  let ε0 = if isUnset prior_initial_res
             then if op.initial_guess
                     then (if op.pc_side == LEFT then nrm2 (op.M · b) else nrm2 b)
                     else β
             else prior_initial_res
      ε  = max (op.rel_tol * ε0) op.abs_tol
  in Convergence { epsilon = ε, satisfied = \β' -> β' < ε }
```

The inner loop and the post-correction test below take a `Convergence` value and call `.satisfied` — they do not re-derive `ε`.

### State stratification

```ts
// SimState — externally-visible, persists across the Mult call.
type SimState = {
  readonly x: Vec;            // current iterate (field)
  readonly it: int;           // total inner iterations consumed
  readonly converged: bool;
  readonly final_res: real;   // last computed residual proxy β
  readonly initial_res: real; // β set on first restart cycle (rel-tol scale)
}

// OpParams — fixed across a single Mult call. Includes the constructed operator.
type OpParams = {
  readonly A: LinOp;
  readonly M: LinOp | null;          // fixed preconditioner; null for FGMRES
  readonly Mk: (step: int) => LinOp; // per-step preconditioner; only used when flexible
  readonly pc_side: 'LEFT' | 'RIGHT' | 'NONE';
  readonly gs_orthog: 'MGS' | 'CGS' | 'CGS2';
  readonly max_dim: int;
  readonly max_it: int;
  readonly rel_tol: real;
  readonly abs_tol: real;
  readonly initial_guess: bool;
  readonly flexible: bool;            // true ⇒ FGMRES; forces pc_side = RIGHT
}

// Krylov — ephemeral, reborn at each restart, discarded at return.
// Field-side: V, Z. LS-side: H, s, cs, sn — small dense, NOT field state.
type Krylov = {
  V: Vec[];                  // orthonormal field basis, length j+2 at step j
  Z: Vec[] | null;           // preconditioned field basis (FGMRES only)
  H: Dense;                  // upper-Hessenberg, small dense (max_dim+1)×max_dim
  s: DenseVec;               // LS RHS, length max_dim+1
  cs: DenseVec; sn: DenseVec; // rotation registers, length max_dim
  j: int;                    // current Arnoldi index
  beta: real;                // current LS residual proxy = |s[j+1]|
}
```

The `readonly` markers on `SimState` and `OpParams` are load-bearing: the solve produces a new `SimState` value rather than mutating in place; `OpParams` is captured once and never re-read for variant dispatch outside the constructed-operator helpers `initial_residual`, `apply_BA`, `apply_correction`. `Krylov` is mutable internally but does not escape the solve.

### Constructed-operator interface

Variant absorption per [concept: variant-absorption](../../concepts/variant-absorption.md) is realised at L4 as a small set of operator-internal helpers that close over `OpParams`. The main solve never inspects `pc_side`, `gs_orthog`, or `flexible`.

```
initial_residual : OpParams → Vec → Vec → (Vec, Vec)         -- (r, x') ; honours initial_guess and pc_side
apply_BA         : OpParams → int → Vec → (Vec, Vec | ⊥)     -- (w, z) ; step index lets Mk vary in FGMRES
orthogonalize    : OpParams → Vec[] → Vec → (Vec, DenseVec)  -- (v_next_unit, h_col)
ls_update_column : Krylov → DenseVec → Krylov                -- pure on small-dense state
back_solve       : Krylov → DenseVec                          -- pure on small-dense state
apply_correction : OpParams → Krylov → DenseVec → Vec → Vec  -- closes over the right basis (V or Z)
```

### Monadic coordination

The solve coordinates `SimState` evolution and `Krylov` lifecycle via a state monad over `SimState`; `Krylov` is born at restart, threaded through the inner step as a plain value, and discarded at restart or return — it does not appear in `SimState`. See [concept: solve-monad](../../concepts/solve-monad.md).

A single `Outcome` value records why the inner loop stopped; the outer loop folds it into `SimState` uniformly. There is no separate `StopTag` / `hit_limit_converged` plumbing.

```haskell
-- The Solve monad threads SimState; Krylov lives within a single restart_cycle.
type Solve a = StateT SimState Identity a

-- Why the inner loop stopped. `Continue` ⇒ another restart cycle is warranted;
-- `Done` ⇒ outer loop terminates. The boolean inside `Done` is the converged flag.
data Outcome = Continue | Done Bool

gmres_solve :: OpParams -> Vec -> Vec -> SimState
gmres_solve op b x0 = execState (solve_loop op b) (SimState x0 0 False ∞ ⊥)

solve_loop :: OpParams -> Vec -> Solve ()
solve_loop op b = do
  outcome <- restart_cycle op b
  case outcome of { Done _ -> pure () ; Continue -> solve_loop op b }

-- One restart cycle: build a fresh Krylov, run the inner loop, fold the correction
-- back into SimState.x. The returned Outcome subsumes converged / max_it / max_dim.
restart_cycle :: OpParams -> Vec -> Solve Outcome
restart_cycle op b = do
  s <- get
  let (r0, x') = initial_residual op b s.x
      β        = nrm2 r0
      conv     = build_convergence op b β s.initial_res
  put s{ x = x', initial_res = (if isUnset s.initial_res then derive_ir op b β else s.initial_res) }
  if conv.satisfied β
    then do modify (\s -> s{ converged = True, final_res = β }) ; pure (Done True)
    else do
      let K0 = fresh_krylov op β r0          -- V[0] = r0/β, s[0] = β, j=0, Z if flexible
      K <- inner_loop op conv K0
      let y = back_solve K
      modify (\s -> s{ x = apply_correction op K y s.x, final_res = K.beta })
      s' <- get
      pure $ if conv.satisfied K.beta    then Done True
             else if s'.it == op.max_it  then Done False
             else                             Continue   -- hit max_dim ⇒ restart

-- Inner Arnoldi loop: pure on Krylov, increments SimState.it via the monad.
-- Stops on the first of: LS residual < ε, basis full (j+1 == max_dim), or total
-- iteration budget exhausted. The reason is recoverable from (K.beta, K.j, s.it).
inner_loop :: OpParams -> Convergence -> Krylov -> Solve Krylov
inner_loop op conv K = do
  let (w, z)      = apply_BA op K.j K.V[K.j]
      K1          = if op.flexible then K{ Z = K.Z `with` (K.j, z) } else K
      (v_next, h) = orthogonalize op (K1.V[0..K1.j]) w
      K2          = K1{ V = K1.V `with` (K1.j+1, v_next) }
      K3          = ls_update_column K2 h
  modify (\s -> s{ it = s.it + 1 })
  s <- get
  if conv.satisfied K3.beta || K3.j + 1 == op.max_dim || s.it == op.max_it
    then pure K3
    else inner_loop op conv K3{ j = K3.j + 1 }
```

The `do`-blocks mark the points where `SimState` is read or written; everywhere else the code is pure on `OpParams` and `Krylov`. The inner loop's only `SimState` interaction is the `it`-counter increment — the iterate `x` is updated exactly once per restart cycle, after `back_solve`. This is the structural realisation of the L1 / L2 / L3 claim that the inner loop does not touch field state on `x` until correction time.

The three termination paths (converged on the LS proxy, exhausted total iterations, hit per-cycle basis dimension) are resolved from `(K.beta, K.j, SimState.it)` at the outer-loop level — the inner loop returns a single `Krylov` value and the outer loop classifies. The `Outcome` type collapses the previously-articulated `StopTag` × `final_res` × `ε` decision table into one constructor.

### Sequential-obstruction placement

The small-dense recurrences identified at L3 — `ls_update_column` and `back_solve` — appear in the calculus as pure functions on `Krylov` (which is small-dense on the LS side). They are NOT lifted to a tensor-field operation; the L4 form simply types them as `Krylov → Krylov` and `Krylov → DenseVec` respectively. The calculus reflects the obstruction by *not* hiding it: there is no monadic effect, no field-level operator, no parallel reduction; the sequential nature is visible as a plain functional recurrence on small-dense state. See [concept: sequential-obstruction](../../concepts/sequential-obstruction.md).

### FGMRES variant

FGMRES is the same `gmres_solve` with `op.flexible = true`, `op.pc_side = RIGHT`, and `op.Mk` supplying the per-step preconditioner. The `apply_BA` constructed operator threads `z = Mk(j) · v` into `K.Z[j]`; `apply_correction` closes over `K.Z` instead of `K.V`. No control flow in `solve_loop` / `restart_cycle` / `inner_loop` is conditioned on `flexible` — the variant is fully absorbed in the constructed-operator helpers, preserving the variant-absorption invariant at L4.

### Citations

- The `SimState` / `OpParams` / `Krylov` split mirrors the L1 state schema (this slice, §L1) and the L0 class layout (L0.1, L0.2, L0.8, L0.9).
- The monadic outer/inner structure mirrors L0.10–L0.13 (`GmresSolver::Mult` and `FgmresSolver::Mult` bodies).
- The constructed-operator interface is the L4 realisation of the L1 building-block contract; see also [concept: constructed-operators](../../concepts/constructed-operators.md).
- The sequential-obstruction typing of `ls_update_column` / `back_solve` follows the L3 obstruction record (this slice, §L3).

### Open questions (L4-specific)

- The `orthogonalize` return contract: the form above has it return `(v_next, h)` where `h` already includes the `h[j+1] = ‖w_proj‖₂` entry and `v_next` is the post-normalisation unit vector. This matches the L1 building-block contract. An alternative — returning the normaliser separately — is equivalent in content and not pursued here.
- The `Mk : int → LinOp` field models FGMRES's per-step preconditioner abstractly; in the implementation `M` is mutated externally between calls to `apply_BA`. Whether the L4 calculus draft prefers explicit step indexing or a side-effecting `M` will need to align with the cross-slice [L4 calculus draft](../../design/l4_calculus.md) — currently the explicit-indexing form is more faithful to the mathematical FGMRES contract.

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
