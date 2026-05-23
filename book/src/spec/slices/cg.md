# CG — Preconditioned Conjugate Gradient

## Context

Palace's CG (`CgSolver<OperType>::Mult`) is a textbook **preconditioned** conjugate gradient solver for symmetric positive-definite (SPD) operators. It is templated over `OperType ∈ {Operator, ComplexOperator}` (real and complex SPD systems) and always preconditioned — when no preconditioner `B` is supplied, the code substitutes the identity inline.

CG is the first slice to exercise the L4 calculus end-to-end: it has an iterative outer loop with a convergence predicate, multiple state fields, preconditioner application as an internal operator, and monitoring outputs (printed residual norms). The four ownership categories in L4 — operator instances, operator internal params, sim/iteration state, ephemeral — should all be visible and distinct.

**Modeling choice (L4 only).** Palace's source structures CG as always-preconditioned with identity as the default. The L4 form here inverts that: **unpreconditioned CG is the primary algorithm** (cleaner mathematical exposition; smaller state), and **preconditioned CG is presented as a variant** that adds a preconditioned-residual field and uses it in place of the raw residual at the relevant points. The two algorithms are equivalent when `B = Identity`; the variant collapses to the primary in that case. This restructure does not change the L0–L3 layers, which describe the Palace source faithfully — only the L4 modeling.

This slice is in **v0.2** form against L4 calculus v0.3. The previous v0.1's open friction around residual-norm logging is **resolved by L4 v0.3's demand-driven pruning** (§3.8 of the calculus): `cg_step` exposes `residual_norm` as a regular record output; consumers that read it cause it to be computed; consumers that don't read it cause it to be pruned. No Writer effect, no phase-config flags, no monadic effects channel needed.

## L0

Cited source ranges, relative to `reference/`:

- `palace/palace/linalg/iterative.hpp:117-150` — `CgSolver<OperType>` class declaration. Inherits from `IterativeSolver<OperType>`; declares the workspace vectors `r, z, p` as `mutable VecType` (used for in-place updates inside `Mult`).
- `palace/palace/linalg/iterative.cpp:360-486` — `CgSolver<OperType>::Mult(const VecType &b, VecType &x) const`. The full preconditioned-CG body, including:
  - `360-374` — setup: scalar workspace, size assertions, `r/z/p.SetSize(...)`, device flags.
  - `376-394` — initialization: if `initial_guess`, compute `r ← b − A·x`; otherwise `r ← b, x ← 0`. Then apply preconditioner `z ← B·r` (or `z ← r` if `B` is null).
  - `395-418` — initial scalars: `beta ← (z, r)`, `res ← √|beta|`; compute reference norm `initial_res` for the relative-tolerance test; check initial convergence.
  - `421-464` — main loop:
    - `434-441` — search direction `p`: first iteration `p ← z`; subsequent `p ← z + (beta/beta_prev)·p`.
    - `443-446` — `z ← A·p`; `denom ← (z, p)`; `alpha ← beta / denom`.
    - `448-449` — `x ← x + α·p`; `r ← r − α·z`.
    - `451-462` — new preconditioned residual: `z ← B·r`; `beta ← (z, r)`; `res ← √|beta|`; convergence check.
  - `465-486` — finalization: print summary, store `final_res`, `final_it`.

Linear-algebra primitives invoked (defined in `palace/palace/linalg/` but treated as concepts here):

- `A->Mult(in, out)` — operator application: writes `out ← A · in`. (palace/palace/linalg/iterative.cpp:379, 443)
- `linalg::AXPBY(α, x, β, y)` — `y ← α·x + β·y` (note: in-place into `y`). (palace/palace/linalg/iterative.cpp:380, 440)
- `linalg::Dot(comm, u, v)` — `(u, v)`, MPI-reduced. (palace/palace/linalg/iterative.cpp:395, 444, 460)
- `linalg::Norml2(comm, v)` — `‖v‖₂`. (palace/palace/linalg/iterative.cpp:408)
- `x.Add(α, y)` (MFEM Vector method) — `x ← x + α·y`. (palace/palace/linalg/iterative.cpp:448, 449)
- `ApplyB(B, r, z, ...)` — preconditioner application, `z ← B·r`. (palace/palace/linalg/iterative.cpp:389, 403, 454)

## L1

Mutation lifted. Workspace `r, z, p` is mutated heavily in the source; here it is rewritten as a chain of pure assignments. The MPI-conditioned `linalg::Dot` and the parallel comm are out of scope (see CLAUDE.md *Scope*); we read `linalg::Dot(comm, u, v)` as the local dot product, and similarly for `Norml2`.

Convention: variable names ending with `'` denote the next-iteration value (the "primed" form). The original is shadowed at the binding point.

```text
// Setup
let r₀, x₀ =
  if initial_guess then
    let r₀ = b - apply A x_in                    // A->Mult(x, r); AXPBY(1, b, -1, r)
    (r₀, x_in)
  else
    (b, 0)                                       // r = b; x = 0

let z₀ = apply B r₀                              // ApplyB(B, r, z); or z = r if !B
let beta₀ = dot z₀ r₀

let initial_res =
  if initial_guess then
    let p_tmp = apply B b                        // tmp use of p as Bb workspace
    sqrt |dot p_tmp b|                           // or Norml2(b) if !B
  else
    sqrt |beta₀|

let eps = max(rel_tol · initial_res, abs_tol)
let converged₀ = (sqrt |beta₀|) < eps

// Iteration
iterate from (x = x₀, r = r₀, z = z₀, p = ⊥, beta = beta₀, beta_prev = 0, res = sqrt |beta₀|, it = 0):
  while it < max_it && !converged:
    let p' = if it == 0 then z else axpby 1.0 z (beta/beta_prev) p
    let z'_pre = apply A p'                      // A->Mult(p, z)
    let denom = dot z'_pre p'
    let alpha = beta / denom
    let x' = x + alpha · p'                      // x.Add(alpha, p)
    let r' = r - alpha · z'_pre                  // r.Add(-alpha, z)
    let z' = apply B r'                          // ApplyB(B, r, z); or z = r if !B
    let beta' = dot z' r'
    let res' = sqrt |beta'|
    let converged' = res' < eps
    let it' = it + 1
    -- (printed residual: ‖r‖_B = res', see effects discussion)
    continue with (x = x', r = r', z = z', p = p', beta = beta', beta_prev = beta, res = res', it = it')
```

Notes:

- The L3 calls to `A->Mult` and `B->Mult` write into pre-allocated output buffers (`z`, `r`). In L1 those are erased — the calls become pure `apply A p → tensor` and `apply B r → tensor`.
- The MFEM `Vector::Add(α, y)` mutates `x` in place; L1 names the resulting value `x'` and rebinds.
- `linalg::AXPBY(α, x, β, y)` mutates `y` in place; L1 makes the destination explicit as the result of the call.
- The `initial_guess` branch reuses `p` as scratch for computing `(Bb, b)`; L1 binds it to a local `p_tmp` since it is not the iteration's search direction.
- The `if it == 0` branch in the search-direction update is a bookkeeping convenience (avoid a divide-by-zero on `beta_prev`). It survives unchanged through L1–L2; at L4 it folds naturally into the first iteration's special-case via the `iterate_while` initial value.

## L2

Fusion unfolded and operations named as their algebraic counterparts. Each L3 primitive (`apply A`, `apply B`, `axpy`, `axpby`, `dot`) is treated as one operation in the algebra; the L2 form is their pure composition.

The CG algorithm in L2 form, as a step from one iteration's state to the next:

```text
step(s) =
  let p'    = if s.it == 0 then s.z
              else            axpby 1.0 s.z (s.beta / s.beta_prev) s.p
  let z'_A  = apply A p'
  let alpha = s.beta / dot z'_A p'
  let x'    = axpy   alpha p'   s.x
  let r'    = axpy (-alpha) z'_A s.r
  let z'    = apply B r'
  let beta' = dot z' r'
  let res'  = sqrt |beta'|
  in (x', r', z', p', beta', s.beta, res', s.it + 1)
```

**No HPC fusion tricks needed unfolding** — the Palace source already composes named primitives (`AXPBY`, `Dot`, `Add`, `A->Mult`); the `bgk_collision_with_spherical_reflection`-style coupled-operation fusion seen in LBM does not occur in this CG implementation. The L1→L2 rotation here is essentially trivial: name the L1 operations as their L3 algebraic counterparts, which they already were.

The only optimization-level note is `Vector::Add(α, y)` — this is an axpy with implicit accumulator into the left operand. L2 makes the dataflow explicit: `x' = axpy α p x` (read: `x' = x + α·p`), which matches the C++ semantics by spelling out the implicit destination.

The early-iteration branch `if s.it == 0 then s.z else axpby ... ` is **not** an optimization trick; it is a *load-bearing* control choice that avoids an undefined `0/0` on iteration 0. It must survive into L4 (see CLAUDE.md *Optimization tricks vs. base algebra*).

## L3

CG is an inherently **sequential** algorithm at the outer-loop level: iteration `k` depends on iteration `k−1` through the residual, search direction, and scalar accumulators. There is no global-tensor-field rewrite of the entire CG iteration. **This is a negative L3 result for the outer loop**, and it is correct — the obstruction is genuine algorithmic sequentiality, not a missing transformation.

Specifically: any attempt to express CG as a single global tensor-field operation would either:

1. Require materializing the full Krylov subspace `{r₀, A·r₀, A²·r₀, …}` and inverting a Hessenberg-style relation — which is exactly what GMRES does, and would change the algorithm.
2. Or fold the iteration into a single tensor op of unbounded depth — which is not a tensor op in any useful sense.

The **per-step** body, however, *is* a composition of L3 primitives — each of `apply A`, `apply B`, `axpy`, `dot`, `axpby`, scalar arithmetic — is a whole-tensor operation with no element loop. L3 for CG is therefore:

- **Inner step body**: positive L3 result — pure tensor-algebra composition (already given in §L2 above).
- **Outer iteration**: negative L3 result, **obstruction = genuine algorithmic sequentiality**. The L2→L3 rotation does not apply to the loop itself; the iteration survives into L4 as `iterate_while`.

This is a *normal* and expected outcome for Krylov methods. The same will hold for GMRES, LOBPCG, time-stepping, etc.: the inner kernel lifts to L3; the iteration does not.

## L4

Against L4 calculus **v0.3**. **Unpreconditioned CG is presented as the primary algorithm**; preconditioned CG is a variant. The two collapse equivalently when `B = Identity`. All algorithms are **pure functions** over records — no `Sim`, no monadic state machinery; optional outputs (residual norms) are exposed as record fields and pruned per §3.8 when not consumed.

### Shared types

```typescript
type LinOp<S>  = Op[Tensor[S] → Tensor[S]]     // operator with closed-over internals

type CgConfig = !{
  rel_tol: Scalar,
  abs_tol: Scalar,
  max_it:  Int,
}
```

### Primary: unpreconditioned CG

```typescript
type CgState<S> = {
  x:         Tensor[S],     // current iterate
  r:         Tensor[S],     // current residual: r = b - A·x
  p:         Tensor[S],     // search direction
  beta:      Scalar,        // (r, r)
  beta_prev: Scalar,        // previous (r, r), 0 on iteration 0
  it:        Int,
  converged: Bool,
}

cg_step
  :: LinOp<S> -> Scalar -> CgState<S>
  -> { state: CgState<S>, residual_norm: Scalar }
cg_step opA eps s =
  let p'    = if s.it == 0 then s.r
                           else axpby 1.0 s.r (s.beta / s.beta_prev) s.p in
  let Ap    = apply opA p' in
  let alpha = s.beta / (dot Ap p') in
  let x'    = axpy alpha p' s.x in
  let r'    = axpy (negate alpha) Ap s.r in
  let beta' = dot r' r' in
  let res'  = sqrt (abs beta') in
  { state: { x: x', r: r', p: p',
             beta: beta', beta_prev: s.beta,
             it: s.it + 1, converged: res' < eps },
    residual_norm: res' }

cg_init
  :: LinOp<S> -> Tensor[S] -> Tensor[S] -> Bool
  -> { state: CgState<S>, initial_res: Scalar }
cg_init opA b x_initial initial_guess =
  let { r0, x0 } =
    if initial_guess
      then { r0: axpby 1.0 b (negate 1.0) (apply opA x_initial), x0: x_initial }
      else { r0: b, x0: zeros_like b } in
  let beta0 = dot r0 r0 in
  let res0  = sqrt (abs beta0) in
  let init_res = if initial_guess then sqrt (abs (dot b b)) else res0 in
  { state: { x: x0, r: r0, p: zeros_like b,
             beta: beta0, beta_prev: 0,
             it: 0, converged: False },
    initial_res }

cg_solve
  :: !CgConfig -> LinOp<S> -> Tensor[S] -> Tensor[S] -> Bool
  -> { final_state: CgState<S>, residual_history: [Scalar] }
cg_solve config opA b x_initial initial_guess =
  let { state: s0, initial_res } = cg_init opA b x_initial initial_guess in
  let eps = max (config.rel_tol * initial_res) config.abs_tol in
  let s0' = { ...s0, converged: sqrt (abs s0.beta) < eps } in
  let { final_state, trajectory }
        = iterate_while s0'
            (\s -> s.it < config.max_it && not s.converged)
            (\s -> cg_step opA eps s) in
  { final_state, residual_history: trajectory.map(\t -> t.residual_norm) }
```

Read: `cg_solve` returns both the converged iterate and the per-iteration residual history. **If the caller reads `.final_state` only, the residual history is pruned** — `cg_step`'s `residual_norm` output is eliminated and the iteration runs without computing per-step residuals. **If the caller reads `.residual_history`** (for plotting, monitoring, regression-checks), the residuals are materialized. Same algorithm; consumer demand decides what's computed.

### Variant: preconditioned CG

Preconditioned CG threads an additional state field — the preconditioned residual `z = B·r` — and uses it in place of `r` for the search-direction update and the inner product. When `B = Identity` the variant collapses to the primary form (because `z = r` becomes a trivial identity).

```typescript
type PCgState<S> = {
  x:         Tensor[S],
  r:         Tensor[S],
  z:         Tensor[S],     // preconditioned residual: z = B·r
  p:         Tensor[S],
  beta:      Scalar,        // (z, r)
  beta_prev: Scalar,
  it:        Int,
  converged: Bool,
}

pcg_step
  :: LinOp<S> -> LinOp<S> -> Scalar -> PCgState<S>
  -> { state: PCgState<S>, residual_norm: Scalar }
pcg_step opA opB eps s =
  let p'    = if s.it == 0 then s.z
                           else axpby 1.0 s.z (s.beta / s.beta_prev) s.p in
  let Ap    = apply opA p' in
  let alpha = s.beta / (dot Ap p') in
  let x'    = axpy alpha p' s.x in
  let r'    = axpy (negate alpha) Ap s.r in
  let z'    = apply opB r' in
  let beta' = dot z' r' in
  let res'  = sqrt (abs beta') in
  { state: { x: x', r: r', z: z', p: p',
             beta: beta', beta_prev: s.beta,
             it: s.it + 1, converged: res' < eps },
    residual_norm: res' }
```

`pcg_init` and `pcg_solve` mirror the unpreconditioned versions with the added `z` field and the use of `opB`. Omitted for brevity; the parallel is mechanical.

**Equivalence note.** `pcg_step opA Identity eps s` (where `Identity : LinOp<S>` returns its argument unchanged) is **observably equal** to `cg_step opA eps s'` where `s'` is `s` with the `z` field projected out (and `beta` reinterpreted as `(r, r)` instead of `(z, r)`, which coincide when `z = r`). Formally: define `forget_z : PCgState<S> → CgState<S>` as the projection that drops `z`; then `pcg_step opA Identity eps ≡ cg_step opA eps ∘ forget_z` modulo the `z` field's no-op write-back. This makes the preconditioned variant a true refinement of the primary.

### Ownership analysis

- `opA`, `opB`: `LinOp<S>` operator instances, constructed by the caller. **Operator instances.**
- `config`: `!CgConfig`, closed-over configuration. **Operator-equivalent internal parameter** at the solve level.
- `s : CgState<S>` / `s : PCgState<S>`: the iteration's threaded state, plumbed through `iterate_while`'s accumulator. Linear (one current state per step).
- `p'`, `Ap`, `alpha`, `x'`, `r'`, `z'`, `beta'`, `res'`: bindings inside the step. **Ephemeral intermediates.**
- `residual_norm`: a per-step **output extra** — exposed in the step's return record, collected by `iterate_while`'s trajectory, pruned (via §3.8) when downstream doesn't consume it.

### L3 ↔ L4 correspondence

The step-level correspondence is mechanical (β, let, spread, δ-rules). Notable points:

1. Palace's in-place updates `x.Add(α, p)` and `r.Add(-α, z)` correspond to `x' = axpy α p s.x` and `r' = axpy (negate α) Ap s.r`. The mutation rotation L0→L1 erases the destination; L4 binds the next-iterate name into the next state record via record-spread.
2. Palace's `linalg::AXPBY(1.0, z, beta/beta_prev, p)` corresponds directly to the `axpby` call; symbols match; mutation erased.
3. Palace's `for (; it < max_it && !converged; it++)` corresponds to `iterate_while ... (\s -> s.it < config.max_it && not s.converged) (\s -> cg_step ...)`. The loop counter folds into the state.
4. The `initial_guess` branching is preserved; it propagates through `cg_init` and is gone for the iteration.
5. The "first iteration takes `p = r`" (unprec) / "`p = z`" (prec) branch is preserved inside the step. It is **load-bearing** (avoids `0/0` on iteration 0); flagged at §L2.
6. **Palace's `print_opts.iterations`-conditional residual logging** corresponds to L4's `residual_history` consumption. Palace gates printing by a runtime flag; L4 gates *computation* by consumer demand. The mapping is: if the caller chains `cg_solve(...).residual_history` into a printer, residual norms are computed and printed; if the caller takes only `.final_state`, they aren't. The flag-gating disappears.
7. The unpreconditioned-as-primary modeling does not correspond to any Palace source structure — Palace always preconditions. The L4 modeling is a cleaner mathematical exposition; the correspondence between L3 and L4 maps Palace's "preconditioned with identity fallback" onto L4's `pcg_step opA Identity ≡ cg_step opA ∘ forget_z` equivalence.

## Working Notes

- v0.1 of this slice (against L4 v0.2) raised push-back signals about residual-norm logging requiring a Writer effect; **resolved by L4 v0.3's demand-driven pruning**. Updated v0.2 here.
- **Open**: the L3 primitives invoked (`axpy`, `axpby`, `dot`, `apply_linop`, `norml2`) need `concepts/` entries. Highest priority: `axpy`, `dot`, `apply_linop`. To be written when the next slice (GMRES) is started or when this slice is re-pushed by the agent loop.
- **Open**: complex-valued case (`OperType = ComplexOperator`) is templated together with the real case in the Palace source. The L4 form does not distinguish them; `Scalar` and `Tensor[S]` are intended to admit both. Worth re-examining when a complex-valued slice (driven solver, eigenmode) is written.
- **Open**: MPI is out of scope per CLAUDE.md; `linalg::Dot(comm, ...)` is read as the local dot product. Single-machine assumption is preserved throughout.
- **Push-back to L3 (still open)**: the "first iteration takes `p = r`" (or `z`) branch survives all the way to L4 as a step-internal `if`. Could it be hoisted out by unrolling the first iteration before `iterate_while`? That is an L4 readability transformation that doesn't change semantics. Not pursued here — could be done in a later iteration if the special-case clutter becomes a friction point across multiple Krylov slices.
- **Push-back to L4 (potential, not pursued)**: `iterate_while`'s trajectory shape is `[{ residual_norm: Scalar }]` — a list of single-field records. Sugar like `iterate_while_scan` returning `[Scalar]` directly would be lighter, but it adds API surface for a minor convenience. Held pending evidence that the verbosity actually hurts readability.
