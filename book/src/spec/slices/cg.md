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
  - `395-418` — initial scalars: `beta ← (z, r)`, `res ← √|beta|`; compute reference norm `initial_res` for the relative-tolerance test; check initial convergence. **Quirk**: at lines 407-411 (the `!B && initial_guess` branch), `initial_res = sqrt|Norml2(b)| = (b·b)^{1/4}`, NOT `‖b‖₂` — see Working Notes.
  - `244-250` — `CheckDot<T>(d, msg)`: partial-function guard; asserts `d` is finite and (for real `T`) non-negative; aborts with `msg` otherwise. Invoked at lines 396, 412, 444, 461 after each β-update.
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
- `ApplyB(B, r, z, ...)` — preconditioner application, `z ← B·r`. Wraps `B->Mult` inside a `BlockTimer` scope; asserts `B` is non-null. (palace/palace/linalg/iterative.cpp:389, 403, 454)
- `CheckDot<T>(d, msg)` — partial-function guard on inner products. (palace/palace/linalg/iterative.cpp:244-250, invoked at 396, 412, 444, 461)

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
    check_dot beta'                                // partial-function guard; aborts on non-finite
    -- (printed residual: ‖r‖_B = res', see effects discussion)
    continue with (x = x', r = r', z = z', p = p', beta = beta', beta_prev = beta, res = res', it = it')
```

Notes:

- The L3 calls to `A->Mult` and `B->Mult` write into pre-allocated output buffers (`z`, `r`). In L1 those are erased — the calls become pure `apply A p → tensor` and `apply B r → tensor`.
- The MFEM `Vector::Add(α, y)` mutates `x` in place; L1 names the resulting value `x'` and rebinds.
- `linalg::AXPBY(α, x, β, y)` mutates `y` in place; L1 makes the destination explicit as the result of the call.
- The `initial_guess` branch reuses `p` as scratch for computing `(Bb, b)`; L1 binds it to a local `p_tmp` since it is not the iteration's search direction.
- The `if it == 0` branch in the search-direction update is a bookkeeping convenience (avoid a divide-by-zero on `beta_prev`). It survives unchanged through L1–L2; at L4 it folds naturally into the first iteration's special-case via the `iterate_while` initial value.
- `check_dot` (Palace's `CheckDot`, [palace/linalg/iterative.cpp:244-250](../../../../reference/palace/linalg/iterative.cpp#L244-L250)) is a partial-function guard at each new inner-product site: it aborts execution if the result is non-finite or, on real SPD systems, negative (signalling loss of positive-definiteness). L1 surfaces it as a `check_dot β'` assertion; at L4 the guard maps to the precondition `β > 0` on `cg_step`'s call-site, not a runtime branch in the pure-functional form.
- **Initial-residual quirk in the no-preconditioner branch (`!B && initial_guess`).** Palace computes `beta_rhs = Norml2(b) = sqrt|(b,b)|` then sets `initial_res = sqrt|beta_rhs|`, yielding `initial_res = (b·b)^{1/4}` — not `‖b‖₂`. The preconditioned branch computes the correct `sqrt|(Bb, b)|`. L1 preserves Palace's source behavior; the L4 modeling and Working Notes flag this as a likely Palace bug (asymmetry with the `B` branch suggests the author intended `Dot(b,b)` not `Norml2(b)`).

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
  beta:      Scalar,        // (r, r); res = sqrt|beta| is a derived view, not stored
  beta_prev: Scalar,        // previous (r, r), 0 on iteration 0
  it:        Int,
  converged: Bool,
}

// `res = sqrt|beta|` is intentionally NOT in CgState — it is a pure function of
// beta. Storing it would duplicate the iteration's scalar state; instead the
// step exposes `residual_norm` as a step-output field, subject to §3.8
// demand-driven pruning.

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
  -- Palace quirk: in the !B branch, initial_res is sqrt|Norml2(b)| = (b·b)^{1/4}, not ‖b‖₂.
  -- See Working Notes; preserved here as a faithful L4 rendering of the source behavior.
  let init_res = if initial_guess then sqrt (sqrt (abs (dot b b))) else res0 in
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
  beta:      Scalar,        // (z, r); res = sqrt|beta| is derived, not stored
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

- v0.1 of this slice (against L4 v0.2) raised push-back signals about residual-norm logging requiring a Writer effect; **resolved by L4 v0.3's demand-driven pruning**. Updated v0.2 here. v0.3 (this revision) audits L0/L1 against source per Explorer cycle, surfacing two prior gaps (CheckDot partial-function guard; initial-residual quirk in `!B && initial_guess` branch).
- **Initial-residual quirk (likely Palace bug).** At [palace/linalg/iterative.cpp:399-412](../../../../reference/palace/linalg/iterative.cpp#L399-L412), when `initial_guess && !B`, Palace assigns `beta_rhs = linalg::Norml2(comm, b)` (already `sqrt|Dot(b,b)|`) then `initial_res = sqrt|beta_rhs|`. Net: `initial_res = (b·b)^{1/4}`. The preconditioned branch sets `beta_rhs = Dot(Bb, b)` (an inner product, NOT a norm), then `initial_res = sqrt|beta_rhs| = sqrt|(Bb,b)|`. The asymmetry — `Norml2` vs `Dot` — strongly suggests an intended `Dot(b, b)` in the unpreconditioned line that would yield `initial_res = ‖b‖₂` matching the energy-norm interpretation of the B-branch. L0/L1/L4 preserve the source behavior faithfully; consumers of the relative-tolerance test (`eps = max(rel_tol·initial_res, abs_tol)`) should be aware that the convergence threshold's scale differs from a pure ‖b‖ formulation in this branch.
- **`CheckDot` modeling.** Palace's `CheckDot` ([iterative.cpp:244-250](../../../../reference/palace/linalg/iterative.cpp#L244-L250)) asserts the dot-product result is finite and (for real systems) non-negative. It is invoked after every β-update at [iterative.cpp:396, 412, 444, 461](../../../../reference/palace/linalg/iterative.cpp#L396-L461). Modeled at L1 as `check_dot β'` partial-function guard; at L4 as a precondition on the SPD assumption (no runtime branch in the pure form).
- **Unit-test coverage.** Per Explorer cycle: no unit tests under `test/unit/` reference `CgSolver` or `PCG` directly (`test-orthog.cpp` is the closest topical sibling but exercises orthogonalization, not CG). CG is exercised only through integration tests under `test/examples/`. The L1–L4 forms remain unverified at the unit level; the L0→L1 rotation here rests on algebraic argument + source-citation, not `empirical_match`.
- **Open**: the L3 primitives invoked (`axpy`, `axpby`, `dot`, `apply_linop`, `norml2`) need `concepts/` entries. Highest priority: `axpy`, `dot`, `apply_linop`. To be written when the next slice (GMRES) is started or when this slice is re-pushed by the agent loop.
- **Open**: complex-valued case (`OperType = ComplexOperator`) is templated together with the real case in the Palace source. The L4 form does not distinguish them; `Scalar` and `Tensor[S]` are intended to admit both. Worth re-examining when a complex-valued slice (driven solver, eigenmode) is written.
- **Open**: MPI is out of scope per CLAUDE.md; `linalg::Dot(comm, ...)` is read as the local dot product. Single-machine assumption is preserved throughout.
- **Push-back to L3 (resolved at L4)**: the "first iteration takes `p = r`" (or `z`) branch survives all the way to L4 v0.4 as a step-internal `if`. Resolved in L4 v0.5 (see new section below) by unrolling the first iteration before `iterate_while` and threading `beta_prev` as a closure parameter rather than a state field. The pattern is documented as [first-iteration unrolling](../../concepts/first-iteration-unrolling.md) for reuse across future Krylov slices.
- **Push-back to L4 (potential, not pursued)**: `iterate_while`'s trajectory shape is `[{ residual_norm: Scalar }]` — a list of single-field records. Sugar like `iterate_while_scan` returning `[Scalar]` directly would be lighter, but it adds API surface for a minor convenience. Held pending evidence that the verbosity actually hurts readability.

## L4 v0.4 — derived-view hoisting (self-rotation)

**v0.4 vs. v0.3.** No semantic change. The v0.4 cycle is an L4→L4 *self-rotation* that names the state-hiding decision that produced the v0.3 schema, so the rationale is auditable rather than implicit. The schema, step bodies, equivalence note, and ownership analysis are unchanged from v0.3; only the commentary below is added.

A companion concept entry — [derived-view hoisting](../../concepts/derived-view-hoisting.md) — generalizes this rotation pattern for use by future slices that face the same state-vs-output design choice (GMRES residual tracking, LOBPCG eigenvalue traces, time-stepping diagnostics).

### The rotation, named

Per `book/src/concepts/rotation.md` criterion (a) *state hiding*: the scalar `res = sqrt|beta|` is hoisted from "hypothetical iteration-state field" to "step-output field, demand-pruned per L4 calculus §3.8".

A candidate v0.2-style schema would include `res: Scalar` in `CgState`/`PCgState` and require the step to maintain the invariant `s.res == sqrt|s.beta|` on every transition. v0.4 (= v0.3 schema, re-justified) eliminates the field:

```text
// Rejected v0.2-style schema (load-bearing field that defeats §3.8 pruning)
CgState = { x, r, p, beta, beta_prev, res, it, converged }
           with invariant res == sqrt|beta|

// Adopted v0.3/v0.4 schema
CgState = { x, r, p, beta, beta_prev, it, converged }
step returns { state: CgState, residual_norm: Scalar }
```

The rotation is observable in three places:

1. **State schema** — `CgState`/`PCgState` carry `beta` only; `res` is not a field.
2. **Step body** — `let res' = sqrt (abs beta')` is a step-local binding that flows into the step's *return record* (`residual_norm: res'`), not into the next state.
3. **Step output record** — `{ state, residual_norm }` separates iteration-threaded state from step-observable outputs. The split makes pruning targetable: `iterate_while`'s trajectory accumulates `residual_norm`s; consumers reading `.residual_history` cause materialization, consumers reading only `.final_state` cause pruning.

### What this rotation hides

A reader looking at `CgState<S>` v0.4 cannot tell — and **does not need to know** — whether downstream consumers will read the residual history. The state schema is the same in both cases. The decision "compute residual norms or not" is pushed entirely to §3.8 demand analysis at the call site.

Contrast: a state field `res` *forces* unconditional computation of the sqrt on every iteration (the iteration must produce a well-formed next state), defeating §3.8 pruning. The schema choice is load-bearing for the demand-driven-output property; v0.4 makes that load-bearing role explicit.

### General rule

If a candidate state field `f` satisfies `f == g(other_state_fields)` for a pure function `g`, hoist `f` to the step's return record as an output-extra. The L4 calculus' §3.8 demand-driven pruning then handles the "compute or skip" decision uniformly across all callers. The general pattern is documented as [derived-view hoisting](../../concepts/derived-view-hoisting.md).

### Equivalence to v0.3

The v0.4 form is **observably identical** to v0.3. The change is documentary: v0.3 had the right schema but did not name the rotation that produced it.

### Carry-through from v0.3

Unchanged at L4 v0.4: `cg_step`, `cg_init`, `cg_solve`, `pcg_step`, the equivalence note (`pcg_step opA Identity ≡ cg_step opA ∘ forget_z`), the ownership analysis, and the L3↔L4 correspondence. Only this section is added.

## L2→L3 — rotation claims (retroactive, cycle 116)

This section backfills explicit `rotation_claim` records for the L2→L3 edge of CG, against the on-disk L3 prose that has been present since cycle 1 (slice v0.1) and carried through v0.2–v0.4. The L3 prose was emitted without per-edge claims at the time; this cycle ratifies it under the current claim-emission discipline.

### Claim 1: outer-loop obstruction (negative L3)

The outer CG iteration does not lift to a single global tensor-field operation. Iteration `k`'s state `(x_k, r_k, p_k, β_k)` is a nonlinear function of iteration `k-1`'s state — through the search-direction recurrence, the residual update, and the α/β scalars — and no global-tensor-field rewrite of the k-indexed sequence exists short of changing the algorithm (e.g., to GMRES, which explicitly materializes the Krylov subspace). The obstruction is algorithmic sequentiality, not a missing representation.

This is a **negative L3 result** in the sense of [`sequential-obstruction`](../../concepts/sequential-obstruction.md): the L2→L3 rotation is recorded as `justification_kind: obstruction`, the obstruction class is `iteration-sequentiality`, and the outer loop survives into L4 as `iterate_while`. This is the expected outcome for Krylov methods at L3.

### Claim 2: step body lifts as identity

The per-step body — `apply A p'`, `apply B r'`, `axpy α p' s.x`, `axpy (-α) Ap s.r`, `axpby 1 s.z (β/β_prev) s.p`, `dot · ·`, and scalar arithmetic — composes primitives that are **already L3-native**. Each is a whole-tensor operation with no element loop exposed at L2:

- [`apply_linop`](../../concepts/apply_linop.md) is global by construction (the linear-operator interface hides any element loop or kernel structure inside `Op`).
- [`axpy`](../../concepts/axpy.md) and [`axpby`](../../concepts/axpy.md) denote whole-tensor `y ← α·x + y` / `y ← α·x + β·y` operations; the per-element index is implicit and globally quantified.
- [`dot`](../../concepts/dot.md) is a global reduction with no exposed element loop.
- Scalar arithmetic operates on rank-0 quantities and is trivially global.

The L2→L3 rotation on the step body is therefore the **identity in form**: no unfolding, no global lift, no schema change. The substantive content is the *recognition* that L2's primitive vocabulary is already L3-native, which is itself the L2→L3 rotation's natural conclusion when L2 was emitted in primitive-composition form.

Per [`rotation`](../../concepts/rotation.md) carry-through: all step-body primitives carry through unchanged from L2 to L3; the rotation work for the L2→L3 edge of CG is concentrated entirely in the obstruction claim above.

### Why the split is structural, not accidental

The inner-kernel-lifts / outer-iteration-does-not split is the canonical L3 outcome for iterative numerical methods. It is documented as [`sequential-obstruction`](../../concepts/sequential-obstruction.md) and is expected to recur across GMRES (with a different inner kernel but the same obstruction shape), LOBPCG, Chebyshev iteration, time-stepping, and operator-splitting schemes. CG is the first slice to make the split explicit; subsequent Krylov slices will cite the same pattern.

## L4 v0.5 — first-iteration unrolling (self-rotation)

**v0.5 vs. v0.4.** Refinement self-rotation prompted by the open push-back in Working Notes: the `if it == 0 then ... else axpby ...` branch inside `cg_step`/`pcg_step` is a step-local control choice that exists *only* because the first iteration lacks a `beta_prev`. By unrolling the first iteration explicitly before `iterate_while`, the branch is hoisted out of the per-step body; the steady-state step becomes branch-free.

This is an **L4 → L4 self-rotation** under `book/src/concepts/rotation.md` criterion (a) *state hiding*: the field `beta_prev: Scalar` and its iteration-zero special-case (`beta_prev = 0`, accompanied by a `0/0`-avoidance branch) are hidden from the steady-state schema. The v0.4 schema and step are preserved verbatim as an alternative form below — the rotation is documentary, not destructive — but the v0.5 form is the recommended L4 rendering going forward, and is the form that subsequent Krylov slices (GMRES, MINRES, BiCGStab) should pattern-match against when they hit the same first-iteration friction.

### The rotation, named

Under the current v0.4 form, every call to `cg_step` evaluates a branch on `s.it == 0` that is taken **exactly once** across the entire solve. The branch is load-bearing in v0.4 because `s.beta_prev = 0` on iteration 0, so the `else` arm's `s.beta / s.beta_prev` would divide by zero. The branch survives all the way from L1 (where it was marked *load-bearing* in §L2) into L4.

v0.5 separates the first step from the steady step:

```typescript
type CgState<S> = {
  x:         Tensor[S],
  r:         Tensor[S],
  p:         Tensor[S],
  beta:      Scalar,        // (r, r); always nonzero on entry to a steady step
  it:        Int,
  converged: Bool,
}
-- Note: `beta_prev` is gone. The steady step uses (s.beta / beta_prev) where
-- beta_prev is supplied as a closure-captured scalar from the prior step, not
-- a state field.

cg_first_step
  :: LinOp<S> -> Scalar -> CgState<S>
  -> { state: CgState<S>, residual_norm: Scalar }
cg_first_step opA eps s =
  -- Precondition: s.it == 0, so p ← r unconditionally.
  let p'    = s.r in
  let Ap    = apply opA p' in
  let alpha = s.beta / (dot Ap p') in
  let x'    = axpy alpha p' s.x in
  let r'    = axpy (negate alpha) Ap s.r in
  let beta' = dot r' r' in
  let res'  = sqrt (abs beta') in
  { state: { x: x', r: r', p: p',
             beta: beta',
             it: 1, converged: res' < eps },
    residual_norm: res' }

cg_steady_step
  :: LinOp<S> -> Scalar -> Scalar -> CgState<S>
  -> { state: CgState<S>, residual_norm: Scalar }
cg_steady_step opA eps beta_prev s =
  -- Precondition: s.it >= 1, beta_prev > 0. Branch-free.
  let p'    = axpby 1.0 s.r (s.beta / beta_prev) s.p in
  let Ap    = apply opA p' in
  let alpha = s.beta / (dot Ap p') in
  let x'    = axpy alpha p' s.x in
  let r'    = axpy (negate alpha) Ap s.r in
  let beta' = dot r' r' in
  let res'  = sqrt (abs beta') in
  { state: { x: x', r: r', p: p',
             beta: beta',
             it: s.it + 1, converged: res' < eps },
    residual_norm: res' }

cg_solve
  :: !CgConfig -> LinOp<S> -> Tensor[S] -> Tensor[S] -> Bool
  -> { final_state: CgState<S>, residual_history: [Scalar] }
cg_solve config opA b x_initial initial_guess =
  let { state: s0, initial_res } = cg_init opA b x_initial initial_guess in
  let eps = max (config.rel_tol * initial_res) config.abs_tol in
  if sqrt (abs s0.beta) < eps then
    { final_state: { ...s0, converged: True }, residual_history: [] }
  else
    let { state: s1, residual_norm: res1 } = cg_first_step opA eps s0 in
    if s1.converged || s1.it >= config.max_it then
      { final_state: s1, residual_history: [res1] }
    else
      let { final_state, trajectory } =
        iterate_while_with_prev s1 s0.beta
          (\(s, _) -> s.it < config.max_it && not s.converged)
          (\(s, beta_prev) ->
            let r = cg_steady_step opA eps beta_prev s in
            (r, s.beta)) in
      { final_state, residual_history: [res1] ++ trajectory.map(\t -> t.residual_norm) }
```

`iterate_while_with_prev` is `iterate_while` over the pair `(state, beta_prev)`, threading the prior step's `beta` as the next step's `beta_prev` without storing it in `CgState`. The L4 calculus admits this directly — it's a closure over the loop carry, not new machinery.

### What this rotation hides

- **The `beta_prev` state field is gone.** The steady-state schema is one scalar lighter. A reader of `CgState<S>` v0.5 sees only fields with a non-trivial role at *every* step.
- **The `if s.it == 0` branch is gone from the step body.** Both `cg_first_step` and `cg_steady_step` are straight-line: each named primitive fires exactly once per call, no per-iteration control choice.
- **The `0/0`-avoidance precondition is moved from a runtime branch to a static type/call-site obligation.** `cg_steady_step` is documented as requiring `beta_prev > 0`; this is automatically satisfied by construction (it is only ever called with `s.beta` from a strictly-preceding step, and `beta > 0` is the CheckDot precondition on SPD systems).

### Why this matters for downstream slices

The `if it == 0 then base_case else recurrence` pattern recurs across Krylov methods: GMRES's first Arnoldi step (no prior `v_{k-1}` to orthogonalize against — though MGS handles it naturally), LOBPCG's initial Rayleigh-Ritz setup (no prior eigenvalue estimate to subtract), Chebyshev iteration's first half-step (no `x_{k-1}`). The same rotation hoists all of them out of the steady step. Documented as a generalizable pattern in `book/src/concepts/first-iteration-unrolling.md`.

### Equivalence to v0.4

Observationally identical for any input `(opA, b, x_initial, initial_guess, config)`:

1. **Initial convergence.** Both forms test `sqrt|beta_0| < eps` before doing any work. v0.5 makes this an outer `if`; v0.4 folds it into the first call to `cg_step` via the `converged` field.
2. **First iteration.** v0.4's `cg_step` with `s.it == 0` executes `p' = s.r` (via the `if` branch). v0.5's `cg_first_step` executes `p' = s.r` directly. The remaining body is identical: same `Ap`, `alpha`, `x'`, `r'`, `beta'`, `res'`.
3. **Subsequent iterations.** v0.4's `cg_step` with `s.it >= 1` executes `p' = axpby 1 s.r (s.beta/s.beta_prev) s.p` (else branch). v0.5's `cg_steady_step` executes the same `axpby` with `beta_prev` supplied as a closure parameter rather than read from the state field. Same `Ap`, `alpha`, `x'`, `r'`, `beta'`, `res'`.
4. **`residual_history`.** v0.4 builds it from `iterate_while`'s trajectory; v0.5 prepends the first-step residual and concatenates the rest. Element-for-element identical.

The `forget_beta_prev : CgState_v04<S> → CgState_v05<S>` projection that drops `beta_prev` makes the equivalence formal: `cg_step` and the v0.5 split commute through this projection (modulo the closure-vs-field choice of where `beta_prev` lives).

### Variant: pcg under v0.5

The preconditioned variant rotates symmetrically. `pcg_first_step` uses `p' = s.z` (since `s.z = B·s.r = B·b` on iteration 0); `pcg_steady_step` is branch-free. The `forget_z : PCgState → CgState` equivalence from v0.3/v0.4 composes with `forget_beta_prev` to give the four-way equivalence between `pcg_*` Identity-instantiated and `cg_*` un-`z`'d.

### Carry-through from v0.4

Unchanged: the `residual_norm` output-extra and §3.8 pruning (v0.4 derived-view hoisting); the `LinOp<S>`/`CgConfig` shared types; the ownership analysis (the now-closure `beta_prev` remains an ephemeral intermediate, just localized to the loop driver rather than the state record); the L3↔L4 correspondence on the inner-kernel primitives. The L3-level *negative* obstruction (cycle 116 retroactive claim 1) is untouched — first-iteration unrolling rearranges the L4 form; it does not change the L2→L3 outer-loop verdict.

### What v0.5 does NOT do

v0.5 does not change the L0/L1/L2/L3 forms. Palace's source still has the `if it == 0` branch inside the loop (`palace/linalg/iterative.cpp:434-441`); L0 cites it; L1 surfaces it as a step-local conditional; L2 names it load-bearing. The v0.5 form is a *purely L4-level* rearrangement — a different rendering of the same algorithm in the calculus, chosen for branch-free steady-state legibility. This is consistent with the L4 calculus's role as *the layer at which algorithm presentation choices live*; v0.4 and v0.5 are both valid renderings, and the slice now exhibits both so downstream slices can pattern-match against either.

## L4 v0.5 — first-iteration unrolling (self-rotation, claim ratification)

**Status.** The L4 v0.5 form above (cycle 132) landed without an accompanying `rotation_claim`. This section, added cycle 137, backfills the per-edge claim under the meta-21 *self-rotation surface-or-evidence* discipline — the on-disk prose IS the surface; the claim ratifies it. `plan_kind: tightening`.

### Claim: state hiding (criterion (a) of `book/src/concepts/rotation.md`)

The `beta_prev: Scalar` field is hidden from the steady-state `CgState<S>` schema by hoisting it out of the iteration-threaded record and into the loop driver as a closure-captured scalar. Symmetrically, the iteration-zero special-case branch `if s.it == 0 then s.r else axpby ... s.p` — load-bearing only because `beta_prev = 0` on entry — is hoisted out of the per-step body into a separate `cg_first_step` call before `iterate_while_with_prev`.

The rotation is **L4 → L4**: no semantic change relative to v0.4; the `forget_beta_prev` projection makes the equivalence formal (see *Equivalence to v0.4* above). The work is documentary in the sense of preserving observable behavior, but **structural** in the sense of changing what the steady-state schema must carry — a strict reduction of state-record fields and step-body branches.

### Why this satisfies criterion (a) and not merely renaming

The renaming gate from the Synthesizer prompt asks: *could a reader replace the v0.5 steady-state primitive with a different algorithm and still satisfy the v0.4 contract?* The answer is yes in a meaningful sense: v0.5's `cg_steady_step` exposes a precondition (`beta_prev > 0`, `it >= 1`) that v0.4's `cg_step` does not — a downstream slice (e.g., MINRES, BiCGStab) reusing the *same skeleton* could substitute its own first-iteration setup and a structurally identical steady step, without needing to thread an iteration counter through the state for branch dispatch. v0.4's `cg_step` cannot be reused this way: the `if s.it == 0` branch ties the steady-state algorithm to its specific bootstrap.

In the language of `book/src/concepts/first-iteration-unrolling.md` (concept introduced cycle 132), v0.5 makes CG fit a *generalizable* pattern; v0.4 has the same algorithm mathematically but a less reusable presentation.

### Carry-through

Unchanged from v0.4: the `residual_norm` output-extra and §3.8 pruning (v0.4 derived-view hoisting); the `LinOp<S>`/`CgConfig` shared types; the ownership analysis (the now-closure `beta_prev` is an ephemeral intermediate localized to the loop driver); the L3↔L4 correspondence on inner-kernel primitives; the `pcg_*` ↔ `cg_*` equivalence via `forget_z`. The L2→L3 negative obstruction (cycle 116) is untouched — first-iteration unrolling rearranges the L4 form; it does not change the L2→L3 verdict.

### Why the claim is emitted now and not at cycle 132

Cycle 132 emitted the v0.5 prose as a refinement push but did not pair it with a `rotation_claim`. Under the meta-21 discipline (added after cycle 115's analogous omission), self-rotation cycles must include either the surface edit AND its claim, or retroactive-evidence quoting the on-disk prose. The v0.5 surface landed; this cycle (137) emits the missing claim against that surface. No further prose changes are made.
