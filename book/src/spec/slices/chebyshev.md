# Slice: chebyshev (reduced — §L1/§L2/§L3 absorbed; §L4 retained)

> **Reduction status (cycle-014+):** the §L1, §Consumers, §Open-questions, §L2, and
> §L3 content of this cycle-001-era slice is **fully absorbed** by the firm/landed
> chebyshev layered cohort and is reduced here to pointers. The §L4 "calculus form"
> below is **RETAINED verbatim** — see the retain-rationale note immediately above it.
>
> **Fully-absorbed sections (now pointers):**
> - **§L1** → `book/src/L1/chebyshev-smoother.md` (firm, cycle-012). Re-cites the
>   `palace/linalg/chebyshev.{cpp,hpp}` ranges independently.
> - **§Consumers / §Open-questions** → `L1/chebyshev-smoother.md` Evidence
>   (`gmg.cpp:52-59`, `distrelaxation.cpp:21-36`) + `L1-L0/chebyshev-smoother-mutation-rotation.md`
>   (consumer sites, dead-code complex-transpose recognition rules).
> - **§L2** → `book/src/L2/chebyshev-iteration.md` (firm, cycle-012) — §Semantics
>   `sweep` IS the §L2 primitive composition; `L2-L1/chebyshev-iteration-fusion.md`
>   (firm, cycle-013) is the upward fusion.
> - **§L3** → `book/src/L3/chebyshev.md` (partial-obstruction, cycle-013) — the
>   tensor-field body lifts; the inner `k`-recurrence + outer `pc_it` sweep are
>   witnessed sequential obstructions.
> - Concept worked-examples lifted: `concepts/state-stratification.md` §"fourth
>   stratum" and `concepts/derived-view-hoisting.md` §"Chebyshev initial-guess branch".
>
> **§L4 RETAINED (not yet removable):**
> - The §L4 `ChebOp<E,S>` / `apply`-as-`Solve`-monad form is transcribed into
>   `book/src/L4/chebyshev.md`, but that entry is `rough-in` (its `forM_`/`foldM`
>   wrapper vocabulary is queued for a cycle-015 `iterate-while` re-anchor), AND the
>   firm `book/src/L2/krylov-step.md` cites this slice's §L4 line ranges
>   (`:354-362`, `:330-353`, `:355-362`, `:308-323`, `:421-436`) as canonical
>   pattern-instance evidence. Full §L4 removal is gated on (a) re-pointing those
>   `krylov-step` citations onto the `L4/chebyshev.md` anchors and (b) the L4 entry
>   firming. OQ `chebyshev-slice-l4-full-removal`.
>
> _(§L4 START anchor `## L4 — calculus form` is a unique heading; the retained span is
>  text-anchored, stable under upstream edits.)_

> **§L4 retain rationale (cycle-014):** retained verbatim because the firm
> `book/src/L2/krylov-step.md` (a distinct operator) cites the line ranges below
> (`:354-362` innerStep, `:330-353` apply, `:355-362` op.scalars, `:308-323`
> ChebOp<E,S>, `:421-436` initial-guess derived-view) and the absorbing
> `book/src/L4/chebyshev.md` is `rough-in`. Remove after the krylov-step citation
> re-point + L4 firming (OQ `chebyshev-slice-l4-full-removal`).

## L4 — calculus form

Against the [L4 calculus](../../design/l4_calculus.md), the Chebyshev smoother is a `Solver<OperType>` constructed once at setup time and then invoked as a pure `apply_linop` action inside an outer [solve monad](../../concepts/solve-monad.md) (the multigrid V-cycle or distributive-relaxation iteration). The L3 sequential obstructions in `k` and `pc_it` survive into L4 as explicit monadic `forM_` binds; they do not collapse.

### State stratification

Per [`state-stratification`](../../concepts/state-stratification.md), the L4 form distinguishes three kinds of state:

- **Sim state** (caller-owned, threaded by the outer solve monad): `x` (rhs), `y` (accumulator / iterate).
- **Operator internal params** (captured at `setup`, immutable across `apply` calls): `A`, `dinv`, `order`, `pc_it`, and the variant-specific scalars (`lam_max` for 4th-kind, `theta`/`delta` for 1st-kind). These live inside the constructed-operator closure ([`constructed-operators`](../../concepts/constructed-operators.md)).
- **Ephemeral intermediates** (allocated per `apply_linop` call, discarded on return): `r`, `d`, `t`, `Ay`, `Ad` — pure field-algebra values, not threaded across calls.
- **Scalar-recurrence state** (per-call ephemeral, but threaded across `k`-iterations within a single `apply` call): `rho_prev` for the 1st-kind variant. Lives inside the `ScalarState` type carried by the inner `foldM`. It is distinct from the operator-internal stratum (the closure does not retain `rho_prev` across `apply` calls — each call starts the recurrence from `rho_0`) and distinct from ordinary ephemerals (it is genuinely threaded, not a transient temporary). For 4th-kind, `ScalarState = ()`.

```ts
// Operator internal params (immutable post-setup); S is the scalar-state type,
// statically determined by variant (Unit for 4th-kind, { rho_prev: E } for 1st-kind).
type ChebOp<E, S> = {
  A: LinOp<E>;                                // SPD operator, by reference
  dinv: Field<E>;                             // 1 / diag(A)
  order: int;
  pc_it: int;
  scalarInit: S;                              // initial ScalarState at k=0
  scalars: (k: int, st: S) =>                 // pure scalar-recurrence step;
    { a0?: E; sd?: E; sr?: E; st: S };        // returns step output + next state
};

// Sim-state capabilities consumed by apply_linop
//   x: read-only field (rhs)
//   y: read-write field (the accumulator the outer solve monad threads)
type ChebSim<E> = { x: Read<Field<E>>; y: ReadWrite<Field<E>> };
```

The scalar-state stratum is encoded in the `S` parameter: `Kind4 :: ChebOp<E, Unit>`, `Kind1 :: ChebOp<E, { rho_prev: E }>`. The two variants have **distinct closure types**, not a single union — there is no runtime variant tag at apply-time, only a closure dispatch through `scalars`. This is the L4 surface of constructed-operator [variant absorption](../../concepts/variant-absorption.md) at level (c).

The `S` type parameter makes the scalar-recurrence stratum visible at the type level: 4th-kind instantiates `ChebOp<E, Unit>` and 1st-kind instantiates `ChebOp<E, { rho_prev: E }>`, with no runtime discriminator at apply-time — the variant axis is absorbed into the closure type per [`constructed-operators`](../../concepts/constructed-operators.md). The `Read`/`ReadWrite` capability split on `ChebSim` records the L4 mutation discipline (only `y` is written; `x` is read-only) at the type-surface, matching the [`solve-monad`](../../concepts/solve-monad.md) convention.

### Apply as a monadic action

The outer `pc_it` loop and the inner `k` loop are sequential by L3 obstruction; in L4 they become explicit `forM_` binds in the `Solve` monad. Each step is a pure tensor-field expression on the field algebra; the monad threads the ephemeral `r`, `d` buffers and the scalar-state `rho_prev`.

```haskell
apply :: ChebOp E S -> Bool -> Solve (ChebSim E) ()
apply op initial_guess = do
  x <- readX
  forM_ [1 .. op.pc_it] $ \it -> do
    -- 1. residual
    r0 <- if it == 1 && not initial_guess
            then do { writeY zero; pure x }   -- r0 = x; y := 0
            else do
              y  <- readY
              ay <- applyLinop op.A y
              pure (x .-. ay)                 -- r = x - A y

    -- 2. initial direction d_0 = alpha_0 * dinv .* r
    let (c0, st0) = op.scalars 0 op.scalarInit
    let d0 = c0.a0 .* (op.dinv .*. r0)

    -- 3. inner k-recurrence (sequential obstruction in k)
    --    fold threads (r, d, scalar_state); modifyY accumulates y += d each step
    (_rN, dN, _stN) <-
      foldM (innerStep op) (r0, d0, st0) [1 .. op.order - 1]

    -- 4. final accumulation
    modifyY (\y -> y .+. dN)
  where
    innerStep op (r, d, st) k = do
      modifyY (\y -> y .+. d)                 -- y += d
      ad <- applyLinop op.A d
      let r'       = r .-. ad                 -- r -= A d
      let (c, st') = op.scalars k st
      let t        = op.dinv .*. r'
      let d'       = c.sd .* d .+. c.sr .* t
      pure (r', d', st')
```

At L4 the field expressions `(x .-. ay)`, `(c.sd .* d .+. c.sr .* t)`, etc. are pure values — the `r`, `d`, `t`, `ay`, `ad` bindings are immutable let-bindings to field-algebra results, not in-place buffers. The L2/runtime implementation is free to realize them via in-place `axpy`/`scal` on aliased storage; that is the standard transparent optimization handled at L2 and does not surface at L4.

The monadic signature is `Bool -> Solve (ChebSim E) ()` — the sim-state capability record `ChebSim E = { x: Read<Field E>, y: ReadWrite<Field E> }` is the monad's environment, not an argument. `readX`, `readY`, `writeY`, `modifyY` are the capability-mediated accessors. The `initial_guess` flag is a **per-call argument** to `apply`, threaded by the outer V-cycle on each invocation; it is **not** a field of `ChebOp` (operator-internal state is invariant across calls).

`modifyY` is the sim-state mutator the outer monad exposes; `applyLinop`, `(.*.)`  (elementwise product), `(.+.)`, `(.-.)`, `(.*)` are the field-algebra primitives carried over from L2/L3.

### Setup as a separate monadic action

Setup is itself a `Solve`-monad action (it issues a `spectrum_estimate` sub-solve), but its product is an **immutable operator closure**, not new sim-state. The closure embeds the variant choice ([`constructed-operators`](../../concepts/constructed-operators.md)):

```haskell
setup :: LinOp E -> SetupParams -> Variant -> Solve s (ChebOp E)
setup A p variant = do
  let dinv = recip (extractDiagonal A)
  lam_max <- (p.sf_max *) <$> spectrumEstimate A dinv
  case variant of
    Kind4 -> pure ChebOp
      { A, dinv, order = p.order, pc_it = p.pc_it
      , scalars = scalars4 lam_max }
    Kind1 -> do
      let sf_min_eff = if p.sf_min > 0 then p.sf_min
                       else 1.69 / (p.order**1.68 + 2.11*p.order + 1.98)
      let lam_min = sf_min_eff * lam_max
      let theta   = (lam_max + lam_min) / 2
      let delta   = (lam_max - lam_min) / 2
      pure ChebOp
        { A, dinv, order = p.order, pc_it = p.pc_it
        , scalars = scalars1 theta delta }
```

Here `scalars4` and `scalars1` are pure scalar-recurrence functions; they close over the persisted spectral bounds and produce the per-`k` `(alpha_0, sd_k, sr_k)` tuple. The variant axis is fully absorbed into the closure — `apply` does not branch on variant. This is the L4 realization of (c)-level [variant absorption](../../concepts/variant-absorption.md).

### Sequential obstructions at L4

- The `forM_ [1 .. pc_it]` outer bind is the L4 surface of the Richardson-sweep sequentiality recorded at L3.
- The `foldM (innerStep op)` is the L4 surface of the three-term-recurrence sequentiality in `k`. The accumulator threads `(r, d, scalar_state)`; each `innerStep` consumes the previous tuple. This is the canonical L4 shape for a [sequential-obstruction](../../concepts/sequential-obstruction.md) that lifted only at the body level — `foldM` over a finite range, body is pure field arithmetic.
- The 1st-kind `rho_k` scalar update rides inside `ScalarState` and is threaded by the same `foldM`; it is `O(1)` work per step and does not introduce additional state-monad complexity.

### Pure-action discipline

The `apply` action does **not** mutate `op` (the operator closure). All mutation lives in the sim-state slice — and even there, only `y` is mutated; `x` is read-only. The ephemeral fields `r`, `d`, `t`, `ay`, `ad` are L4-pure values (immutable let-bindings to field-algebra expressions, not mutated in-place); whether the L2/runtime implementation realizes them via in-place `axpy`/`scal` on aliased storage is the standard transparent optimization handled at L2.

The `MultTranspose` alias under the symmetry assumption is L4-trivial: `applyTranspose op = apply op` for SPD `A`.

### What carries through from L3

- The body's tensor-field expressions ([`tensor-field-lift`](../../concepts/tensor-field-lift.md)) carry through verbatim as field-algebra expressions.
- Both sequential obstructions are made explicit as monadic binds; nothing pretends to be parallel.
- Variant absorption stays at level (c): one `apply` body, scalar-generator selected at setup. (Strictly two closure *types* — one per variant — but a single procedural shape.)

### Capability-typed sim state

The `ChebSim<E> = { x: Read<Field<E>>; y: ReadWrite<Field<E>> }` shape encodes the L4 mutation discipline at the type surface: `apply` may **read** `x` (but not write it) and **read/write** `y`. This is the [`solve-monad`](../../concepts/solve-monad.md) capability-typing convention adapted for a smoother: the outer multigrid V-cycle constructs the `ChebSim` capability record by handing the per-level `(rhs, correction)` field pair to the smoother and trusting that the `Read`/`ReadWrite` split prevents the smoother from clobbering rhs. The L2/runtime is free to alias buffers if it can prove the `Read` discipline holds (typically: `rhs` is the level's accumulated residual and is distinct storage from `correction`). At L4 the read-only / read-write split is enforced by the capability types, not by runtime convention.

### Initial-guess shape: branch vs. derived view

The `apply` body opens with a conditional on `initial_guess`:

```haskell
r0 <- if it == 1 && not initial_guess
        then do { writeY zero; pure x }
        else do
          y  <- readY
          ay <- applyLinop op.A y
          pure (x .-. ay)
```

This branch is a **degenerate-case absorption**, not a residual variant axis. The `initial_guess = false` path is the algebraic specialization of the `true` path under `y_in = 0` (which makes `A y_in = 0` and `r = x - A y_in = x`); writing `y := 0` is the precondition that *establishes* `y_in = 0` so subsequent sweeps (`it >= 2`) follow the uniform `r = x - A y` path. The branch fires at most once per `apply` call (only when `it == 1 && not initial_guess`), and only on the residual-computation step — the rest of the per-sweep procedure is uniform.

This is the [`derived-view-hoisting`](../../concepts/derived-view-hoisting.md) pattern applied at the *control-flow* boundary rather than the state-shape boundary: a single Boolean parameter `initial_guess: Bool` at the `apply` signature replaces what would otherwise be a constructed-operator variant axis (`ChebOpWithGuess` vs. `ChebOpNoGuess`) carrying a `hasInitialGuess: Bool` field. The branch is fully absorbed at level (a) — the invariant `r = x - A y_post_zeroing` unifies both cases — and at level (b)/(c) the residual axis is the single Boolean argument, with the procedural divergence confined to the one residual step.

The alternative — promoting `initial_guess` to a constructed-operator variant — would inflate the closure-type lattice to four (`Kind4 × {guess, no-guess}` and `Kind1 × {guess, no-guess}`) for no structural benefit: the polynomial-recurrence machinery is genuinely insensitive to `initial_guess`, which only affects the first residual computation. Keeping `initial_guess` as a `Bool` argument preserves the [`variant-absorption`](../../concepts/variant-absorption.md) discipline by *not* over-absorbing — a per-call flag and a constructed-operator variant are different categorical objects, and the former is correct here.

### Concept references added at L4

- [`solve-monad`](../../concepts/solve-monad.md) — the outer monad threading sim state through `forM_` and `foldM`.
- [`state-stratification`](../../concepts/state-stratification.md) — the three-way split of sim / operator-internal / ephemeral state.
- [`constructed-operators`](../../concepts/constructed-operators.md) — the closure that absorbs the variant axis at L4.
