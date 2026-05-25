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
