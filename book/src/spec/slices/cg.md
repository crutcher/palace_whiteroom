# Slice: cg (reduced)

This slice is the cycle-001-era precursor to the firm CG row in the krylov-step chain. The L1/L2/L3/L4-v0.1-v0.4 forms have been lifted to firm entries; this stub points at them and retains the unique material below.

**Firm entries that supersede this slice's L0/L1/L2/L3/L4-v0.1-v0.4 content:**

- `book/src/L1/ksp_solve.md` (firm; cycle-007) — the variant-axis-collapsed L1 form. CG / GMRES / FGMRES share the same opaque `Solver[A]` type. Supersedes this slice's §"L1".
- `book/src/L1-L0/ksp-solve-mutation-rotation.md` §"Sub-pattern B — inner CG body" (rough-in; cycle-008) — the L1>L0 rewrite for CG. Cites `iterative.cpp:360-486`, `:369-374`, `:377-386`, `:418-419`, `:427-464`, `:443`, `:448-449`, `:484-485`. Supersedes this slice's §"L0".
- `book/src/L2/krylov-step.md` (firm; cycle-005) — the L2 primitive composition. CG instance cited. Supersedes this slice's §"L2".
- `book/src/L3/krylov-step.md` (firm; cycle-010 wave-1) — the L3 value-threaded form. Supersedes this slice's §"L3" and the cycle-116 retroactive rotation_claim section.
- `book/src/L3-L2/krylov-step-body-identity.md` (firm; cycle-009) — the L3>L2 identity-in-form theme.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` (firm; cycle-008) — the L4>L3 theme.
- `book/src/L4/krylov-step.md` (firm; cycle-006) Form A — supersedes this slice's §"L4" v0.1-v0.4 (the `CgState` / `cg_step` / `cg_solve` typing).
- `book/src/concepts/derived-view-hoisting.md` — supersedes this slice's §"L4 v0.4 derived-view hoisting (self-rotation)" rotation derivation (the residual-norm hoisting worked example).

**Unique material retained below** (the L4 v0.5 first-iteration-unrolling derivation): the canonical evidence for `concepts/first-iteration-unrolling.md`. The slice's `forget_beta_prev` projection making the v0.4-v0.5 equivalence formal, the `(first_step, steady_step)` signature derivation, and the closure-vs-state-field reasoning are load-bearing methodology evidence.

**Open questions still pending lift (from the now-stubbed §"Working Notes"):**

- The **initial-residual quirk** in the `!B && initial_guess` branch (`iterative.cpp:399-412`): Palace computes `initial_res = (b·b)^{1/4}` rather than `‖b‖₂` due to a `Norml2`-vs-`Dot` asymmetry between the unpreconditioned and preconditioned branches. This is a likely Palace bug; lift target is an annotation in `L1-L0/ksp-solve-mutation-rotation` Sub-pattern B or a `scaffolding/open-questions.md` entry flagging upstream confirmation needed.
- The **`CheckDot` partial-function guard** at `iterative.cpp:244-250` invoked at lines 396/412/444/461: the firm L1>L0 theme recognises CheckDot but does not enumerate per-call-site. Lift target is per-call-site `verified_against` rows.
- The **unpreconditioned-as-primary L4 modeling** choice (preconditioned-CG-as-variant via `forget_z`): inverts Palace's always-preconditioned source structure. Lift target is `concepts/state-stratification` or a presentation-choice note in `L4/krylov-step`.
- The **unit-test coverage gap**: no unit tests under `test/unit/` reference `CgSolver` or `PCG` directly. CG is exercised only via integration tests at `test/examples/`. Lift target is a `scaffolding/test-linkages/cg.md` entry noting the gap.

---

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
