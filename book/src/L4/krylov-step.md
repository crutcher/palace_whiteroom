# krylov-step

Typed-wrapper step kernel for iterative Krylov-shaped solvers, expressed in the L4 state-stratification idiom. The body of the `solve-monad`'s `iterate_while`-style inner driver — `krylov-step` is what gets folded; the monadic coordination is around it, not inside it. Companion to the L2 entry [`krylov-step`](../L2/krylov-step.md), which names the underlying primitive composition.

## Context

L4's job is to write algorithms in a graph-evaluation calculus that makes lifetimes, dispatch sites, and effect placement structural. `krylov-step` at L4 is the typed shape that the L4 concepts `solve-monad`, `state-stratification`, and `first-iteration-unrolling` already reference in prose without a dep-map anchor (per the cycle-005 cross-cutter report, `solve-monad.md:13-17` writes an implicit step-fold via `solve_loop`'s `restart_cycle` recursion, `state-stratification.md:11` references step-local ephemeral state, `first-iteration-unrolling.md:21-23` already names `first_step` and `steady_step` signatures). This chapter is the missing anchor.

The relationship to L2 `krylov-step` is **typed-wrapper-to-primitive-composition**:

- L2 names the algebraic composition: at most five primitive groups (apply, optional auxiliary, iterate-update, scalar-update, output-readout) per step.
- L4 names the typed wrapper: the same kernel, re-typed against the three-stratum state record, with the consumed-by surfaces (`iterate_while`, `solve-monad`, `convergence-test`) and the optional first-iteration unrolling rendered at the calculus level.

The L4>L2 lowering is **not identity-in-form**: L4 carries the `SimState` / `OpParams` / `Krylov` typing and the optional `(first_step, steady_step)` split, both of which collapse to value-threading on the way down. The intermediate L3 lowering is plausibly identity-in-form on the kernel body itself (per the combinator-miner cycle-002 assertion, now firm in [`L3-L2/krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md) §Verified-against and co-anchored by the live `arnoldi_step.md:185-188`; the original CG evidence at `cg.md:352-362` was lifted into that firm theme per the cycle-009 corpus reduction), with the L4>L3 transition carrying the substantive rotation; this is the rotation that the cycle-006 wave-2 abstractor dispatch is auditing. If the abstractor finds non-identity rotation at L3, an L3 `krylov-step` row will follow in cycle-007.

`krylov-step` at L4 is a **methodology-level concept**, not a Palace-source artefact — there is no L0 source range that "is" the L4 `krylov-step`. The Palace evidence sits at L2 (and at the slice corpus); L4 cites the L2 entry as its evidence base.

## Signature

The L4 signature is the typed-wrapper shape. Two surface forms, depending on whether `first-iteration-unrolling` is applied:

**Form A — branch-in-body** (default; CG v0.4-shape):

```text
krylov-step :: OpParams -> Krylov -> (SimState -> Solve { sim: SimState', krylov: Krylov', outputs: StepOutputs })
```

**Form B — first-iteration-unrolled** (CG v0.5-shape; opt-in per first-iteration-unrolling rotation):

```text
first_step  :: OpParams -> Krylov -> (SimState -> Solve { sim: SimState', krylov: Krylov', carry: PrevCarry, outputs: StepOutputs })
steady_step :: OpParams -> Krylov -> (PrevCarry -> SimState -> Solve { sim: SimState', krylov: Krylov', carry: PrevCarry', outputs: StepOutputs })
```

Shape contract (bunsen-style; named records and axes):

- `OpParams` — operator-internal configuration, captured once at solve construction; `readonly` per [`state-stratification`](../concepts/state-stratification.md). Closes over the variant selectors (`pc_side`, `gs_orthog`, `flexible`, polynomial-kind, restart-mode) and the constructed-operator surfaces. The kernel body does not branch on `OpParams` fields — variant absorption is structural per the `readonly` typing (see [`variant-absorption`](../concepts/variant-absorption.md) level (b)/(c)). Fields are slice-specific; the kernel sees them only through the closed-over surfaces `op.T`, `op.orthog?`, `op.scalars?`, `op.eps`.
- `Krylov` — solve-local ephemeral bundle; born at restart entry, discarded at restart exit or solve return. Per `state-stratification`, `Krylov` is **not** part of `SimState` — its lifetime is strictly within a single restart cycle. Mixed-stratum: contains both `Tensor[N]`-typed iterate-bundle fields (`V`, `Z`, basis-columns) and small-dense scalar-stratum fields (`H`, `s`, `cs`, `sn`, `β`). Threaded through the kernel as a plain value (not as a monadic effect — its lifetime defeats encoding-as-state).
- `SimState` — externally-visible state that persists across the entire solve call. Per `state-stratification`, contains `x: Tensor[N]`, `it: Int`, `converged: Bool`, `final_res: Scalar`, `initial_res: Scalar`. Threaded by the `Solve a = StateT SimState Identity a` monad (see [`solve-monad`](../concepts/solve-monad.md)); the monadic effect of `krylov-step` is the `SimState` transition.
- `PrevCarry` (Form B only) — the closure-threaded recurrence carry that the first-iteration-unrolling rotation moves out of the steady-state schema. For CG: `β_prev`. For GMRES: `H_{k,k-1}` (less acute; GMRES does not commonly adopt Form B). Per [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md), `PrevCarry` is a *closure parameter of the loop driver*, not a *state field of the iteration*.
- result `{ sim: SimState', krylov: Krylov', outputs: StepOutputs }` (Form A) or `+carry` (Form B): a record carrying (a) the next `SimState` value (returned through the monadic state transition, not by structural projection — written as a record field here only for the L4 narrative; the actual monadic discharge is via `modify`), (b) the next `Krylov` ephemeral bundle (plain value), (c) the demand-prunable `StepOutputs` record (residual norm, LS residual, breakdown tokens — see L2 entry for slice-specific contents), and (d) for Form B, the new `PrevCarry` value to thread to the next step.
- `Solve` — the state monad over `SimState`, defined at [`solve-monad`](../concepts/solve-monad.md) as `Solve a = StateT SimState Identity a`. The `Solve { ... }` return wraps a `modify`-shaped action that performs the `SimState` transition; the other record fields (`krylov`, `outputs`, `carry`) are returned as the monadic action's value.

The shape contract makes three things structural that are merely conventional at L2:

1. **The `OpParams` `readonly` annotation forbids the kernel from re-inspecting variant selectors.** Variant absorption becomes a typing invariant rather than a discipline. This is the load-bearing typing distinction between L4 and L2.
2. **The `Krylov` ephemeral bundle is threaded as a plain value, not as a monad effect.** Its lifetime (born at restart, discarded at restart-or-return) defeats encoding as monadic state — `SimState` would otherwise need to either grow `Krylov` (mis-typing the lifetime) or carry an `Option<Krylov>` (mis-typing the always-present-within-restart invariant). The split-out is mechanical from `state-stratification`.
3. **The `Solve` monad's effect domain is exactly `SimState`.** Operator applications, dense recurrences, and `Krylov`-bundle updates are all pure on their inputs and live outside the monad — the rule of thumb from `solve-monad.md` is "if the action reads or writes `SimState`, it's in the monad; otherwise it's a pure function call inside a `let` or `pure` block". `krylov-step` honours this rule: typically one `modify` per step (incrementing `SimState.it`, or — at the restart boundary — folding the correction into `SimState.x`), with everything else in `let`-bindings on `Krylov` and `OpParams`.

The two `OpParams` and `Krylov` records are **slice-specific** (CG's `Krylov` is `{ r, p, z?, α, β }`; GMRES's is the full `{ V, Z?, H, s, cs, sn, β, j }` bundle); this chapter does not enumerate their fields, only their stratification. Each consuming slice instantiates the records and writes `krylov-step` over its instantiation. The L4 calculus names the **role and the typing**; the slice supplies the record schema.

## Semantics

`krylov-step` at L4 is a single pass of the iterative method's per-step kernel, expressed against the typed state-stratified record and embedded in the `Solve` monad. The L4 dataflow shape (Form A) is:

```text
krylov-step op K = \s -> do
  -- Operator apply on Krylov's iterate-side input (no SimState read; no monad effect)
  let w         = apply_linop op.T K.<input_field>

  -- Optional auxiliary stage (absorbed; one branch, statically selected by op)
  let K_aux     = optionally apply op.orthog (K.V_prefix, w)        -- GMRES / Arnoldi
                  or       apply op.scalars (K.k, K.scalar_state)   -- Chebyshev
                  or       K                                        -- CG (no-op)

  -- Krylov-bundle update (pure on K; the iterate-stratum and scalar-stratum
  -- update primitives are L1 calls — axpy, axpby, axpbypcz, dot, nrm2, scal —
  -- staged in the dataflow-forced order specified by the L2 entry)
  let K'        = krylov_update K_aux op w                          -- pure; see L2/krylov-step.md §Semantics

  -- Derived view of the post-step bundle (demand-pruned per derived-view-hoisting)
  let outputs   = derived_views K' op                               -- typically residual_norm; for GMRES ls_residual; for breakdown-guarding kernels a breakdown_token

  -- The sole monadic effect: increment the iteration counter in SimState
  modify (\s -> s { it = s.it + 1 })

  pure { krylov: K', outputs }
```

The body composes the same five primitive groups as the L2 entry, in the same dataflow-forced order. What the L4 typing adds is **placement discipline**: every primitive call sits in a pure `let`-binding on `Krylov`-bundle fields; the only `modify` is the `SimState.it` increment; the `SimState.x` is **not** touched per step (it is updated by the outer `restart_cycle` after `back_solve` produces the correction — see `concepts/solve-monad.md` §"Worked example — GMRES"). This placement is exactly the L4 calculus's effect-localisation discipline: the monad's effect domain is `SimState`; the kernel touches `SimState` exactly where it must (the counter), nowhere else.

Form B (first-iteration-unrolled) splits the body into two named functions per [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md) §"The rotation". `first_step` produces the initial `PrevCarry` from a base-case computation; `steady_step` consumes `PrevCarry` (the prior iteration's recurrence variable, e.g., `β_prev`) as a closure argument rather than reading it from `Krylov`. The `Krylov` schema in Form B is one slot lighter (no `β_prev` field); the branch-free `steady_step` is the body folded by `iterate_while_with_prev`. Both forms are valid L4 renderings of the same L2 `krylov-step`; the choice is the `first-iteration-unrolled` variant axis (inherited unchanged from L2). The CG instantiation of Form B is worked below; the abstract `(first_step, steady_step)` rotation it specialises lives in [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md) §"The rotation" and is not restated here.

### Worked example — CG Form B (v0.5 first-iteration-unrolling)

This is the canonical CG instantiation of Form B: the `Krylov` bundle is `CgState<S>`, the `PrevCarry` is `β_prev`, and the rotation drops `β_prev` from the steady-state schema by threading it as a closure argument of the loop driver. It is the worked datum that grounds Form B and the `first-iteration-unrolling` concept; the abstract `(first_step, steady_step)` signatures it specialises are in [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md) §"The rotation" (not restated here).

The v0.5 `CgState<S>` schema is one scalar lighter than the Form-A (v0.4) schema — `beta_prev` is gone:

    type CgState<S> = {
      x:         Tensor[S],
      r:         Tensor[S],
      p:         Tensor[S],
      beta:      Scalar,        // (r, r); always nonzero on entry to a steady step
      it:        Int,
      converged: Bool,
    }
    -- `beta_prev` is gone. The steady step uses (s.beta / beta_prev) where
    -- beta_prev is supplied as a closure-captured scalar from the prior step,
    -- not a state field.

The first iteration is unrolled (precondition `s.it == 0`, so `p ← r` unconditionally — the Form-A `if it == 0` branch is hoisted out); the steady step is branch-free (precondition `s.it >= 1, beta_prev > 0`):

    cg_first_step
      :: LinOp<S> -> Scalar -> CgState<S>
      -> { state: CgState<S>, residual_norm: Scalar }
    cg_first_step opA eps s =
      let p'    = s.r in                         -- s.it == 0 ⇒ p ← r
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

The driver runs the first step, then folds `cg_steady_step` with `iterate_while_with_prev` — `iterate_while` over the pair `(state, beta_prev)`, threading the prior step's `beta` as the next step's `beta_prev` without storing it in `CgState`. This is a closure over the loop carry, not new calculus machinery:

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

**What this CG rotation hides.** (a) The `beta_prev` state field is gone — the steady-state schema is one scalar lighter, and a reader of `CgState<S>` sees only fields with a non-trivial role at *every* step. (b) The `if s.it == 0` branch is gone from the step body — both `cg_first_step` and `cg_steady_step` are straight-line, each named primitive firing exactly once per call. (c) The `0/0`-avoidance precondition moves from a runtime branch to a static call-site obligation: `cg_steady_step` requires `beta_prev > 0`, automatically satisfied by construction (only ever called with `s.beta` from a strictly-preceding step, and `beta > 0` is the `CheckDot` precondition on SPD systems).

**Equivalence to Form A (v0.4↔v0.5).** The two CG forms are observationally identical for any input `(opA, b, x_initial, initial_guess, config)`: (1) both test `sqrt|beta_0| < eps` before any work — v0.5 as an outer `if`, v0.4 folded into the first `cg_step` via the `converged` field; (2) the first iteration runs `p' = s.r` in both (v0.4 via the `if` branch, v0.5 directly), with identical remaining body; (3) subsequent iterations run the same `axpby` (v0.4 reading `s.beta_prev` from state, v0.5 receiving `beta_prev` as a closure parameter), with identical `Ap`, `alpha`, `x'`, `r'`, `beta'`, `res'`; (4) `residual_history` is element-for-element identical. The projection `forget_beta_prev : CgState_v04<S> → CgState_v05<S>` that drops `beta_prev` makes the equivalence formal — `cg_step` and the v0.5 split commute through it (modulo the closure-vs-field choice of where `beta_prev` lives). This is the CG witness of the L4 non-law catalogued in §"Algebraic laws" (form-equivalence-under-monad-laws): Form A and Form B are trajectory-identical but NOT related by a monad-law β-reduction — the rotation drops a `Krylov` field and threads a closure argument.

**Variant: pcg under v0.5.** The preconditioned variant rotates symmetrically. `pcg_first_step` uses `p' = s.z` (since `s.z = B·s.r = B·b` on iteration 0); `pcg_steady_step` is branch-free. The `forget_z : PCgState → CgState` equivalence composes with `forget_beta_prev` to give the four-way equivalence between `pcg_*` Identity-instantiated and `cg_*` un-`z`'d.

**L0 ground.** Both CG forms render the *same* Palace CG body — the v0.5 unrolling is a purely L4-level rearrangement and does not change the L0/L1/L2/L3 forms (Palace's source keeps the `if (!it)` branch inside the loop). The terminal L0 home is [`ksp-solve-mutation-rotation`](../L1-L0/ksp-solve-mutation-rotation.md) §"Sub-pattern B — inner CG body" (`CgSolver<OperType>::Mult`, `palace/linalg/iterative.cpp:360-486`): the per-step for-loop at `iterative.cpp:427-464` carries the Form-A first-iteration branch `if (!it) { p = z; } else { AXPBY(1.0, z, beta/beta_prev, p); }` (`iterative.cpp:434-441`) that v0.5 hoists out, the operator apply `A->Mult(p, z)` (`iterative.cpp:443`), the `alpha`/`x.Add`/`r.Add` updates (`iterative.cpp:446-449`), the `beta_prev = beta` carry that v0.5 moves into the closure (`iterative.cpp:451`), and the `beta`/`res` readout (`iterative.cpp:460-462`).

Three placements are made structural by the L4 typing that are merely conventional at L2:

- **Convergence-predicate evaluation is `Krylov`-local, not `SimState`-local.** The convergence test surface ([`convergence-test`](../concepts/convergence-test.md)) reads the freshly-computed residual proxy `K'.β` (or for Chebyshev, the trivially-converging post-fixed-order signal); it does not read `SimState.x`. The `Convergence` value is constructed once per restart cycle and consumed inside the inner loop as a plain closure; `krylov-step` does not need to know about it (the wrapper `iterate_while` does). This is one of the three surfaces — alongside `apply_BA` and `apply_correction` — through which variant axes would leak into the loop body if not absorbed.
- **Breakdown signals propagate through `outputs`, not `SimState`.** Palace's `CheckDot` partial-function guard (`iterative.cpp:244-250`, cited transitively via the L2 entry) becomes, at L4, a `BreakdownTag`-valued slot in the `StepOutputs` record. The outer driver (`iterate_while`'s predicate, or `solve_loop`'s `Outcome` classifier) inspects `outputs.breakdown_token` and decides whether to stop, restart, or signal failure. The kernel itself does not branch — this preserves the dataflow purity of the body and routes the partiality to the wrapper.
- **The iterate field `SimState.x` is updated at restart-cycle boundaries, not per step.** This is the GMRES pattern from `concepts/solve-monad.md` §"Worked example": `restart_cycle` builds a fresh `Krylov`, folds `inner_loop` over `krylov-step`, then folds the correction `K.V · K.y` into `SimState.x` via `modify` exactly once. For non-restarted Krylov methods (CG, Chebyshev) the same shape collapses: the "restart cycle" is the entire solve, and `SimState.x` is written once at solve exit. `krylov-step` is uniformly a step-kernel that does not touch the iterate field; the iterate update is the restart-boundary operation.

The kernel is **stateless across calls** in the same sense as L2: no in-step mutation escapes; the `Krylov'` bundle is a fresh record; the `SimState'` is produced by `modify` (not by destructive update on the same cell — `StateT`'s state is a value). This is what makes `krylov-step` foldable by `iterate_while`-style combinators at L4 — the body has no hidden side channels beyond the explicit `SimState`-monad effect.

## Algebraic laws

The L4 laws are the same three that hold at L2, sharpened by the typing where the typing tightens them. Absences are catalogued explicitly to prevent decoration drift.

1. **Output-extras distributivity over trajectory** (the load-bearing law; inherited from [`derived-view-hoisting`](../concepts/derived-view-hoisting.md)). For any `StepOutputs`-typed field `f` such that `f = g(krylov')` for a pure function `g` of the post-step `Krylov` bundle, the trajectory observation `(iterate_while (krylov-step op) K₀ cond).trajectory.map(.outputs.f)` is equal to `(iterate_while (krylov-step op) K₀ cond).trajectory.map(.krylov).map(g)`. **Consequence**: if no downstream consumer reads `.outputs.f`, the kernel is free to skip the `g` computation — the trajectory's `krylov` projection is unchanged. This is the demand-pruning law underwriting the residual-norm hoisting documented in the firm [`derived-view-hoisting`](../concepts/derived-view-hoisting.md) §"Worked example: CG residual norm" (lines 14-19; the original CG evidence at `cg.md:325-339` was lifted into that concept page per the cycle-009 corpus reduction, which the reduced slice's stub header names as the supersessor) and the LS-residual proxy at `gmres.md:471-489`. At L4 the law is statable directly because `Krylov` and `StepOutputs` are typed separately and the `g` derivation is visible as a pure binding; at L2 the same law holds but requires extracting the derivation from the kernel-body description.

2. **Primitive-count invariance under reformulation**. The number of `apply_linop` calls per step is a structural invariant of the slice's variant-axis profile — Form A and Form B of the kernel have the same per-step `apply_linop` count (the `first_step` / `steady_step` split moves the branch, not the apply). Any reformulation that changes the count is a *different algorithm*. (CG: 1 per step. GMRES inner Arnoldi: 1 per step. Chebyshev inner k-loop: 1 per k. Arnoldi step: 1.) The L4 form preserves the count by the same dataflow argument as L2 — there is no L4 calculus rewrite that introduces or elides an `apply_linop`. Inherited from the L2 entry.

3. **State-stratum independence under the typed split**. At L4 the three strata (sim, op, ephemeral) are *typed* records with no cross-stratum aliasing. The kernel's `Krylov`-bundle update touches only `Krylov` fields; the sole `SimState` write is the counter increment via `modify`; `OpParams` is `readonly` and untouched. Consequence (sharpened from L2): a reordering of the iterate-stratum-update primitives among themselves (subject to dataflow constraints) does not affect the scalar-stratum-update primitives, **and** the `SimState`-counter increment commutes with any pure `Krylov`-bundle binding (the `modify` can be hoisted to the start or end of the kernel without changing observed semantics, as long as the `SimState.it` value is not read inside the body — which it is not per the typing). The L4 typing makes the cross-stratum non-aliasing structural; at L2 it is a discipline.

Laws that explicitly **do not** hold:

- **Commutativity of the primitive sequence**. Inherited from L2. The five primitive groups (apply, auxiliary, iterate-update, scalar-update, output-readout) cannot be reordered without changing the value. Dataflow on the `Krylov`-bundle is rigid: `apply_linop` produces `w`, `axpy(α, ·, w)` reads it, `dot(w, ·)` reads it. The L4 typing does not relax this — `Krylov`-bundle fields participate in the same dataflow chains as their L2-form counterparts.
- **Associativity / fold-merge**. Inherited from L2. `iterate_while (krylov-step op) (iterate_while (krylov-step op) K₀ p₁) p₂` is **not** equal to `iterate_while (krylov-step op) K₀ (p₁ ‖ p₂)` for arbitrary predicates. The inner fold's `outputs` are not visible to the outer fold; convergence predicates that depend on monotonic-loss properties do not generally compose. This is why slice-level restart logic (`gmres.md:435-454`) is structured as an *outer* loop around the `krylov-step`-folding inner loop, not as a flattened single fold. At L4 the non-associativity is preserved exactly — the `Solve` monad's `SimState` threading does not introduce a fold-merge identity.
- **Identity element**. Inherited from L2. There is no `K_id` such that `krylov-step op K_id = pure { krylov: K_id, outputs: ... }` in general. `α = 0` in CG is breakdown, not identity. The L4 typing does not introduce one — `StateT`'s identity element is `pure ()`, not `pure { krylov, outputs }`.
- **Step composition into a bigger step**. Inherited from L2. Two successive `krylov-step` invocations do not simplify to a single `krylov-step` with combined parameters — the second step reads scalars produced by the first. The L4 `Solve` monad does not change this; monadic `>>=` is sequential composition, not fusion.
- **Linearity in any single argument**. Inherited from L2. `krylov-step op (α·K₁ + β·K₂) ≠ α · krylov-step op K₁ + β · krylov-step op K₂` because the scalar-stratum update involves divisions and the convergence flag involves a comparison. Built from linear primitives, but their composition with `dot` and scalar arithmetic destroys linearity.
- **Bit-determinism across orthogonalization variants**. Inherited from L2. Switching `gs_orthog` from MGS to CGS to CGS2 produces mathematically-equivalent but bit-distinct trajectories. Load-bearing per CLAUDE.md §"Optimization tricks vs. base algebra".
- **Form-equivalence-under-monad-laws**. Form A and Form B (first-iteration-unrolled) produce iteration-for-iteration-identical trajectories per `concepts/first-iteration-unrolling.md` §"What is preserved", but they are **not** related by an L4-calculus rewrite using only the monad laws (the rotation is a structural rewrite that drops a `Krylov` field and threads a closure argument; it is not a β-reduction or a `>>=`-associativity step). The `(first_step, steady_step)` pair is a different `krylov-step` shape, not a syntactic variant of Form A. Promoted from the `first-iteration-unrolling` rotation discussion to a non-law of `krylov-step` at L4 to forestall the misreading.

## Dependencies

L4 concept references (per the cycle-006 caveat 1, these are concept-page links — see Open Questions for the L4-row-vs-concept dependency question):

- [`state-stratification`](../concepts/state-stratification.md) — the three-stratum (`SimState` / `OpParams` / `Krylov`) typing.
- [`solve-monad`](../concepts/solve-monad.md) — the `Solve a = StateT SimState Identity a` outer driver that consumes `krylov-step` as its fold body.
- [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md) — the rotation supplying Form B's `(first_step, steady_step)` split.
- [`derived-view-hoisting`](../concepts/derived-view-hoisting.md) — the demand-pruning algebra underwriting Law 1.
- [`convergence-test`](../concepts/convergence-test.md) — the stopping-predicate surface consumed by the outer `iterate_while`-style driver (not by the kernel itself, but referenced for the placement discipline).
- [`variant-absorption`](../concepts/variant-absorption.md) — the absorption discipline making the six variant axes structural via the `OpParams` `readonly` typing.
- [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the L3-edge classification recording why the L3>L2 step lowering is plausibly identity-in-form (per the combinator-miner cycle-002 assertion).

L2 dependencies (the underlying primitive-composition row):

- [`krylov-step`](../L2/krylov-step.md) at L2 — the firm primitive-composition row that L4 `krylov-step` lowers to. The L2 entry carries the L1 primitive-call enumeration, the L2-composition surfaces (`apply_BA`, `orthogonalization`), the cited slice corpus evidence (cg.md, gmres.md, chebyshev.md, arnoldi_step.md, polynomial_recurrence_step.md), and the L0 source ranges (`iterative.cpp:244-250` for `CheckDot`; the test corpus at `test/unit/test-orthog.cpp:80-170, :234-280`).

## Lowers to

L4 `krylov-step` lowers to L2 `krylov-step` via the L4>L3>L2 chain:

- **L4 > L3** (substantive rotation): typed-wrapper-with-state-monad → value-threaded form. The `Solve a = StateT SimState Identity a` threading collapses to a `SimState` value passed explicitly between calls; the `Krylov` bundle, already a plain value, is unchanged; the `OpParams` `readonly` typing collapses to an "the variant selectors are not read in the body" invariant that is documented but no longer typed. The first-iteration-unrolling Form-A-vs-Form-B distinction (if Form B is in use) similarly collapses to value-threading of `PrevCarry`. **Cycle-006 wave-2 abstractor dispatch** is authoring this theme at `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` (per `reports/2026-05-27T081913Z-abstractor-L4-L3-krylov-step-lowering/CYCLE.md`; updated by repairer from the original placeholder `krylov-step-state-thread.md`).
- **L3 > L2** (plausibly identity-in-form on the kernel body): per the combinator-miner cycle-002 assertion (now firm in [`L3-L2/krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md) §Verified-against, co-anchored by the live `arnoldi_step.md:185-188`; the original CG evidence at `cg.md:352-362` was lifted into that firm theme per the cycle-009 corpus reduction), the L3 kernel body and the L2 kernel body are isomorphic — the L3 form is the value-threaded body with the outer loop's `sequential-obstruction` made explicit at L3, but the body itself does not change. The cycle-006 abstractor's audit landed the firm L3>L2 body-identity theme (the firm L3 `krylov-step` row was subsequently promoted cycle-010 per the identity-lowerings-still-require-both-L-levels directive).

## Variant axes

Inherited unchanged from the L2 entry. All six axes are absorbed at construction (per [`variant-absorption`](../concepts/variant-absorption.md)), encoded in `OpParams`'s `readonly` fields and the constructed-operator surfaces (`op.T`, `op.orthog?`, `op.scalars?`); none appears in the per-step kernel signature. The six:

1. **preconditioner present/absent** — absorbed at level (c) into `op.T` (the constructed `apply_BA`).
2. **orthogonalization variant** (`gs_orthog ∈ {MGS, CGS, CGS2}`) — absorbed at level (b) into `op.orthog`.
3. **polynomial-kind** (`Chebyshev-4th | Chebyshev-1st`) — absorbed at level (c) into `op.scalars`.
4. **first-iteration-unrolled vs. branch-in-body** — selected at the L4 form level (Form A vs Form B). The two forms produce trajectory-identical iterates; the choice is a presentation rotation per `first-iteration-unrolling`.
5. **restart shape** (`non-restarted | restarted-fixed-dim | restarted-adaptive`) — restart logic lives in the outer `solve_loop`, not in the kernel; the kernel is restart-agnostic. The `Krylov`-bundle's "born at restart, discarded at restart" lifecycle is what the typing enforces.
6. **in-place vs. out-of-place buffer use** — transparent performance-equivalent per CLAUDE.md §"Optimization tricks". The L4 form is uniformly out-of-place (a fresh `Krylov'` is returned); in-place specialisation reappears in the L2>L1 lowering.

The L4 typing makes axes (1), (2), (3), and (5) **structurally absorbed**: the `OpParams` `readonly` annotation forbids the kernel from re-inspecting their selectors. Axis (4) is a presentation choice between Form A and Form B; axis (6) is a transparent rotation below L4's level of abstraction.

The variant-axis count of six matches the L2 entry exactly. No new axes are introduced by the L4 typing; no axes are merged or split.

## Status

`firm` — typed-wrapper signature is the canonical fold-body shape for the `solve-monad`'s inner driver; algebraic laws are inherited from the L2 entry (with state-stratum independence sharpened by the typing) and reduced to one non-trivial property (the demand-pruning law) plus two structural invariants; non-laws are catalogued explicitly, including the form-equivalence non-law for Form A vs Form B; variant-axis profile is closed at six, inherited unchanged from L2. The pattern is well-attested at the L4 level across four slices' explicit L4 sections (CG L4 Form A `cg_step` and L4-v0.5 Form B `cg_first_step`/`cg_steady_step` — lifted into the firm `book/src/L2/krylov-step.md` §Evidence registry, line 138, per the cycle-009 corpus reduction, with the CG-concrete Form B v0.5 bodies now worked inline in §Semantics §"Worked example — CG Form B"; gmres.md:459-471; arnoldi_step.md:285-298), and the slot is the consumed-by surface for the L4 concepts `solve-monad`, `state-stratification`, and `first-iteration-unrolling`, which previously referenced "step" without a vocabulary anchor.

## L4 vs L2 distinction

- **L2**: names the *primitive composition* — at most five primitive groups (apply, optional auxiliary, iterate-update, scalar-update, output-readout) in a dataflow-forced sequence. The L2 form is the algebraic decomposition into L1 primitives plus L2-composition surfaces (`apply_BA`, `orthogonalization`); state threading is by explicit value semantics; no monadic structure; variant absorption is a discipline.
- **L4**: names the *typed wrapper* — the same composition, re-typed against the three-stratum state record, with the `Solve` monad threading `SimState`, the `Krylov` bundle threaded as a plain ephemeral value, and `OpParams` `readonly`. Variant absorption becomes structural (typing-enforced rather than discipline-enforced). The optional `(first_step, steady_step)` split per `first-iteration-unrolling` is named at the calculus level.

The two layers' entries share variant-axis count, primitive-call count, and the cited slice corpus. They differ in **typing and effect placement**. The L4>L2 lowering (via the cycle-006 wave-2 abstractor theme) erases the typing and the monadic effect, recovering the L2 form.

## Evidence

- `book/src/L2/krylov-step.md` (cycle-005 firm) — the L2 row whose primitive composition this L4 entry wraps. All L1 primitive calls, L2-composition surfaces (`apply_BA`, `orthogonalization`), pattern-instance citations (five slices), L0 source ranges (`iterative.cpp:244-250` for `CheckDot`; the test corpus at `test/unit/test-orthog.cpp:80-170, :234-280`), and cycle-004 obstruction-theme guidance (MINRES, BiCGStab) are cited there and inherited by reference.
- `book/src/concepts/solve-monad.md:1-69` — the L4 outer-driver pattern; `solve_loop`, `restart_cycle`, `inner_loop`, `Outcome` classifier all named here. The worked-example GMRES section (`:47-68`) shows `krylov-step` consumed exactly as this entry describes.
- `book/src/concepts/state-stratification.md:1-45` — the three-stratum typing; the GMRES worked example (`:37-45`) shows `OpParams` / `SimState` / `Krylov` instantiated for restarted GMRES, with the same `readonly` and ephemeral-bundle treatment this entry adopts.
- `book/src/concepts/first-iteration-unrolling.md:21-37` — the `(first_step, steady_step)` signatures (Form B) named here; this entry adopts them verbatim.
- `book/src/concepts/derived-view-hoisting.md:14-19` — the demand-pruning property underwriting Law 1; the CG residual-norm worked example is the canonical evidence.
- `book/src/concepts/convergence-test.md:7-26` — the `Convergence` value and its `build_convergence(op, b, β, prior_initial_res) -> Convergence` constructor; placement discipline (convergence-test lives in the outer driver, not the kernel) cited from here.
- Four explicit L4 slice sections in the corpus (cited transitively via the L2 entry, not re-anchored here):
  - CG L4 `cg_step` (Form A) — lifted into firm `book/src/L2/krylov-step.md` §Evidence (line 138, the narrative registry carrying the CG L4 Form A step-body instance) per the cycle-009 corpus reduction; the firm `book/src/L4/krylov-step.md` Form A typing (this entry) is the L4 supersessor named in the reduced slice's stub header. (Original pre-reduction range: `cg.md:172-188`.)
  - CG L4 v0.5 `cg_first_step` / `cg_steady_step` split (Form B) — worked inline in this chapter's §Semantics §"Worked example — CG Form B (v0.5 first-iteration-unrolling)"; the canonical CG instantiation of the abstract rotation in `concepts/first-iteration-unrolling.md`, also registered in firm `book/src/L2/krylov-step.md` §Evidence (line 138). The L0 ground is the same CG body as Form A: [`ksp-solve-mutation-rotation`](../L1-L0/ksp-solve-mutation-rotation.md) §"Sub-pattern B" (`palace/linalg/iterative.cpp:360-486`; per-step for-loop `:427-464`; first-iteration branch `:434-441`). (This material was previously retained live in the reduced slice at `book/src/spec/slices/cg.md:27-141`, absorbed here in cycle-099 so the slice is clear-to-delete; original pre-reduction range was `cg.md:393-425`.)
  - `book/src/spec/slices/gmres.md:459-471` — GMRES L4 `inner_loop` body (Form A; Arnoldi-step + LS-update + counter-increment + convergence-test).
  - `book/src/spec/slices/arnoldi_step.md:285-298` — L4 `arnoldiStep` monadic form (Form A).
- Cross-cutter motivating report: `reports/2026-05-27T025354Z-cross-layer-cross-cutter-krylov-step-placement/CYCLE.md` — the dual-placement recommendation this entry implements.

No L0 Palace source ranges are cited directly. The `krylov-step` at L4 is a methodology-level naming of a typed shape; Palace's C++ source does not realise the L4 form. All L0 evidence is transitive through the L2 entry.
