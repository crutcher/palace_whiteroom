# chebyshev

Typed-wrapper fixed-degree polynomial-smoother operator at L4 — the Chebyshev
smoother as a constructed `ChebOp` whose `apply` is a `Solve`-monad action over
a capability-typed sim-state. The thin state-bearing wrapper around the pure
fixed-degree polynomial action; the two sequential obstructions (the outer
`pc_it` Richardson sweep, the inner `k`-recurrence) surface as nested
[`iterate_while_pure`](./iterate-while.md) folds with **step-count predicates** —
they do not collapse. Companion to L3
[`chebyshev`](../L3/chebyshev.md) (the value-threaded form of the same body)
and L2 [`chebyshev-iteration`](../L2/chebyshev-iteration.md) (the primitive
composition with the iteration view erased).

## Context

L4's job is to write algorithms in a graph-evaluation calculus that makes
lifetimes, dispatch sites, and effect placement structural (per
[`../design/l4_calculus.md`](../design/l4_calculus.md) §0). `chebyshev` at L4 is
the typed shape of the Chebyshev smoother: a `Solver<OperType>` constructed once
at setup (the `ChebOp` closure absorbing the variant) and then invoked as a pure
`apply` action inside an outer solve monad (the multigrid V-cycle or
distributive-relaxation iteration).

`chebyshev` at L4 is **not** an instance of [`krylov-step`](./krylov-step.md),
even though both consume the [`iterate-while`](./iterate-while.md) family. The
Krylov step kernel is folded by a **convergence-predicate-driven** `iterate_while`
over a trajectory of demand-prunable per-step extras; the Chebyshev smoother is
folded by a **step-count-predicate** `iterate_while_pure` (the loops are bounded
static ranges `[1 .. pc_it]` and `[1 .. order-1]`, the bound folded into the
carry counter) and is **inner-product-free** (no `dot` / `nrm2` reduction; no
residual-norm trajectory — the trajectory is uniformly empty). It is therefore
the canonical L4 example of a **fixed-degree** operator whose sequential
obstructions are `iterate_while_pure` folds with step-count predicates — the
predicate shape, not the combinator, is what distinguishes the smoother from
the convergence-gated Krylov step (per [`iterate-while`](./iterate-while.md)
§Variant axes).

The relationship to the lower layers:

- **L4 > L3** (substantive at the wrapper; identity-in-form on the body): the
  `Solve (ChebSim E)` monad dissolves to explicit `(x, y)`-state threading; the
  `ChebOp<E, S>` closure dissolves to a positional operator-parameters value;
  the `Read`/`ReadWrite` capability typing on `ChebSim` demotes to a documented
  mutation discipline; the two `iterate_while_pure` folds dissolve to the L3
  `iterate_while_pure_L3` tail recursions over the step-count predicate
  (`iterate-while.md:193-195`), matching the L3 `itloop`/`kloop` shape. The
  kernel body's primitive sequence is value-thread-isomorphic to L3
  [`chebyshev`](../L3/chebyshev.md). This is the same
  wrapper-dissolution shape that
  [`krylov-step-typed-wrapper-dissolution`](../L4-L3/krylov-step-typed-wrapper-dissolution.md)
  catalogs for the Krylov kernel; a dedicated L4>L3 chebyshev identity-theme is
  an Open Question follow-up if the lowering-verifier wants a standalone audit
  anchor.
- **L3 > L2**: the L3 explicit-iteration form lowers to the L2 primitive
  composition with the iteration view erased (the body identity-in-form).

`chebyshev` at L4 is a **methodology-level typed shape** — Palace's C++ source
realises the *behaviour* (the `Mult2` member-method family) but not the L4
typed-wrapper form; the L0 evidence sits at the cycle-012 firm L1/L2 entries and
the slice corpus, which L4 cites as its evidence base.

## Signature

The L4 signature is the typed-wrapper shape. Setup constructs the `ChebOp`
closure; `apply` is the `Solve`-monad action.

```text
ChebOp :: { A: LinOp[E], dinv: Tensor[E, (V: ...)], order: Int, pc_it: Int
          , scalarInit: S
          , scalars: (Int, S) -> { α₀?: E, sd?: E, sr?: E, st: S } }

ChebSim :: { x: Read[Tensor[E, $V]], y: ReadWrite[Tensor[E, $V]] }

setup  :: LinOp[E] -> SetupParams -> Variant -> Solve s (ChebOp E S)
apply  :: ChebOp E S -> Bool -> Solve (ChebSim E) ()
```

Shape contract (bunsen-style; named records and axes; the field shape group `V`
follows the named-shape-group convention of
[`l4_calculus`](../design/l4_calculus.md) §1.2.1 — named `V` here to avoid
colliding with the scalar-recurrence state type parameter `S`; `E` is the element
type, not an axis):

- `ChebOp E S` — operator-internal configuration, captured once at setup;
  `readonly` per [`state-stratification`](../concepts/state-stratification.md).
  `S` is the scalar-recurrence state type, **statically determined by variant**:
  `Unit` for 4th-kind, `{ rho_prev: E }` for 1st-kind. The two variants are
  **distinct closure types** (`ChebOp E Unit` vs `ChebOp E { rho_prev: E }`),
  not a single union — there is no runtime variant tag at apply-time, only a
  closure dispatch through `scalars`. Fields:
  - `A: LinOp[E]` — the captured SPD operator (residual + direction-image).
  - `dinv: Tensor[E, $V]` — `1/diag(A)` (the `D⁻¹` action), congruent to the
    field shape group `V`; real-valued even for complex `A`.
  - `order: Int` — polynomial degree (`> 0`); the inner `iterate_while_pure`
    step-count-predicate bound (`c.k <= order - 1`).
  - `pc_it: Int` — Richardson-sweep count; the outer `iterate_while_pure`
    step-count-predicate bound (`s.it <= pc_it`).
  - `scalarInit: S` — the initial scalar-recurrence state at `k = 0`.
  - `scalars: (k: Int, st: S) -> { α₀?, sd?, sr?, st: S }` — the pure
    scalar-recurrence step (4th-kind: stateless closed form; 1st-kind:
    `ρ`-threaded). The kernel does not branch on variant — the variant axis is
    absorbed into the closure type per [`variant-absorption`](../concepts/variant-absorption.md)
    level (c).
- `ChebSim E` — the capability-typed sim-state record threaded by the `Solve`
  monad: `x: Read[Tensor[E, $V]]` (the rhs; read-only) and `y: ReadWrite[Tensor[E,
  V]]` (the accumulator; the only field written), both congruent to the field
  shape group `V`. The `Read`/`ReadWrite` split
  encodes the L4 mutation discipline at the type surface (per
  [`solve-monad`](../concepts/solve-monad.md)): `apply` may read `x` but not
  write it, and read/write `y`.
- `Solve (ChebSim E)` — the state monad over `ChebSim E`. `apply` returns
  `Solve (ChebSim E) ()` — its only product is the sim-state transition (the
  accumulated `y`); there is no result-value record (contrast `krylov-step`'s
  `Solve { sim, krylov, outputs }`, because the smoother is inner-product-free
  and convergence-test-free, producing no per-step readout).
- `Variant` — `Kind4 | Kind1`, consumed only by `setup` to select the scalar
  generator and instantiate the closure type `S`. Not present at apply-time.
- `initial_guess: Bool` — the per-call argument to `apply` (threaded by the
  outer V-cycle on each invocation). **Not** a field of `ChebOp` —
  operator-internal state is invariant across calls. The
  degenerate-case-absorption flag (see Semantics / Initial-guess shape).

The shape contract makes three things structural that are conventional at L3:

1. **The `ChebOp` `readonly` typing forbids `apply` from re-inspecting the
   variant.** Variant absorption is a typing invariant (the `S` type parameter
   selects the closure shape), not a discipline. The two variants have distinct
   closure types — no apply-time discriminator.
2. **The `Read`/`ReadWrite` capability split on `ChebSim` is type-enforced.**
   The smoother cannot clobber the rhs `x`; only `y` is mutable. The L2/runtime
   may alias buffers if it can prove the `Read` discipline holds; at L4 the split
   is enforced by capability types, not runtime convention.
3. **The `Solve` monad's effect domain is exactly `ChebSim`.** Operator
   applications, dense scalar recurrences, and ephemeral field bindings (`r`,
   `d`, `t`) are pure on their inputs and live outside the monad in `let`-
   bindings; the only monadic effects are the `writeY`/`modifyY` accumulator
   updates.

## Semantics

`chebyshev` at L4 is the constructed-operator smoother whose `apply` action
applies `op.pc_it` Richardson sweeps of a degree-`op.order` matrix polynomial of
`D⁻¹ A`. The two sequential obstructions surface as two nested
[`iterate_while_pure`](./iterate-while.md) folds with **step-count predicates**
(the bounded loop counters folded into the carry, per strawman §6.5 step 5):
the outer `pc_it` sweep and the inner `k`-degree recurrence. Each step is a pure
tensor-field expression on the field algebra; the `Solve` monad threads the
sim-state accumulator `y` (the orthogonal effect; the trajectory is uniformly
empty) and the inner fold's value-carry threads the ephemeral `(r, d)` plus the
scalar-state `st` plus the counter `k`.

```text
apply :: ChebOp E S -> Bool -> Solve (ChebSim E) ()
apply op initial_guess = do
  x <- readX
  -- outer pc_it Richardson sweep: bounded iteration via iterate_while_pure
  -- with a step-count predicate; the sweep counter `it` is folded into the
  -- carry (the only carry field — the y accumulator is the orthogonal Solve
  -- effect, not a value-carry field). Trajectory is uniformly empty.
  _ <- iterate_while_pure
         { it: 1 }                              -- carry: bounded sweep counter
         (\s -> s.it <= op.pc_it)               -- step-count predicate (NOT convergence)
         (\s -> do { sweep op initial_guess s.it; pure { it: s.it + 1 } })
  pure ()
  where
    -- one Richardson sweep; the y accumulator is the Solve-monad effect
    sweep op initial_guess it = do
      -- 1. residual r0 = x − A·y   (or r0 = x; y := 0 on first sweep w/o guess)
      r0 <- if it == 1 && not initial_guess
              then do { writeY zero; pure x }
              else do { y <- readY; ay <- applyLinop op.A y; pure (x .-. ay) }

      -- 2. initial direction d0 = α₀ · (dinv ⊙ r0)
      let { α₀: c0, st: st0 } = op.scalars 0 op.scalarInit
      let d0 = c0 .* (op.dinv .*. r0)

      -- 3. inner k-recurrence (sequential obstruction in k): bounded iteration
      -- via iterate_while_pure with a step-count predicate; the recurrence
      -- tuple (r, d, st) plus the counter `k` is the value-threaded carry.
      cN <- iterate_while_pure
              { r: r0, d: d0, st: st0, k: 1 }    -- carry: recurrence tuple + counter
              (\c -> c.k <= op.order - 1)         -- step-count predicate
              (\c -> do
                 modifyY (\y -> y .+. c.d)         -- y += d   (Solve effect)
                 ad <- applyLinop op.A c.d
                 let r' = c.r .-. ad               -- r −= A·d
                 let { sd, sr, st: st' } = op.scalars c.k c.st
                 let t  = op.dinv .*. r'           -- dinv ⊙ r'
                 let d' = sd .* c.d .+. sr .* t    -- d = sd·d + sr·t
                 pure { r: r', d: d', st: st', k: c.k + 1 })

      -- 4. final accumulation
      modifyY (\y -> y .+. cN.d)
```

Both `iterate_while_pure` folds are the **no-extras / empty-trajectory** case
(`iterate-while.md:98`): the value-carry threads the loop and the `y`
accumulator is the orthogonal `Solve (ChebSim E)` effect — the same shape as the
strawman `run_lbm` bounded loop (`book/src/design/l4_calculus.md:382-385`). The
step-count predicates (`s.it <= op.pc_it`, `c.k <= op.order - 1`) fold the loop
bounds into the carry exactly as the `iterate-while.md:57,102` predicate
discipline requires; both folds are total by construction (the counter strictly
increments, so the predicate becomes false in `bound` steps — the
bounded-`max_it`-folded-into-carry totality discharge of `iterate-while.md:165`).
The field expressions `(x .-. ay)`, `(sd .* d .+. sr .* t)`, etc. are pure
values — the `r`, `d`, `t`, `ay`, `ad` bindings are immutable `let`-bindings to
field-algebra results, not in-place buffers. The L2/runtime is free to realise
them via in-place `axpy`/`scal` on aliased storage; that is the standard
transparent optimization handled below L4 and does not surface here.

What the L4 typing adds is **placement discipline**: every field-algebra call
sits in a pure `let`-binding; the only monadic effects are the `writeY`
(degenerate-case `y := 0`) and the `modifyY` accumulator updates; `x` is read
once via `readX` and never written. The `Solve` monad's effect domain is exactly
`ChebSim`. The bounded iteration is the [`iterate-while`](./iterate-while.md)
family's `iterate_while_pure` with a step-count predicate (the loop counter
folded into the carry), per strawman §6.5 step 5
([`../design/l4_calculus.md`](../design/l4_calculus.md):418) — the calculus's
canonical fixed-count bounded-loop form, not a second iteration vocabulary.

### Setup as a separate monadic action

Setup is itself a `Solve` action (it issues a spectrum-estimate sub-solve), but
its product is an **immutable operator closure**, not new sim-state. The closure
embeds the variant choice (per
[`constructed-operators`](../concepts/constructed-operators.md)):

```text
setup :: LinOp E -> SetupParams -> Variant -> Solve s (ChebOp E S)
setup A p variant = do
  let dinv = recip (extractDiagonal A)
  lam_max <- (p.sf_max *) <$> spectrumEstimate A dinv
  case variant of
    Kind4 -> pure { A, dinv, order: p.order, pc_it: p.pc_it
                  , scalarInit: (), scalars: scalars4 lam_max }
    Kind1 -> do
      let sf_min_eff = if p.sf_min > 0 then p.sf_min
                       else 1.69 / (p.order ** 1.68 + 2.11 * p.order + 1.98)
      let lam_min = sf_min_eff * lam_max
      let theta   = (lam_max + lam_min) / 2
      let delta   = (lam_max - lam_min) / 2
      pure { A, dinv, order: p.order, pc_it: p.pc_it
           , scalarInit: { rho_prev: delta / theta }
           , scalars: scalars1 theta delta }
```

`scalars4` and `scalars1` are pure scalar-recurrence functions closing over the
persisted spectral bounds. The variant axis is fully absorbed into the closure —
`apply` does not branch on variant. This is the L4 realisation of (c)-level
[`variant-absorption`](../concepts/variant-absorption.md).

### Sequential obstructions at L4

- The outer `iterate_while_pure { it: 1 } (\s -> s.it <= op.pc_it) …` fold is the
  L4 surface of the Richardson-sweep sequentiality (each sweep consumes the
  previous sweep's accumulated `y`). The carry holds only the bounded sweep
  counter `it`; the cross-step linkage is the `y` accumulator, threaded by the
  `Solve` monad orthogonally to the value-carry (the Solve-threaded-body
  discipline of `iterate-while.md:59`).
- The inner `iterate_while_pure { r, d, st, k: 1 } (\c -> c.k <= op.order - 1) …`
  fold is the L4 surface of the three-term-recurrence sequentiality in `k`. The
  value-carry threads `(r, d, scalar_state)` plus the counter `k`; each step
  consumes the previous carry. This is the canonical L4 shape for a
  [`sequential-obstruction`](../concepts/sequential-obstruction.md) that lifted
  only at the body level — a bounded `iterate_while_pure` over a step-count
  predicate, body pure field arithmetic.
- The 1st-kind `ρ_k` scalar update rides inside the carry's `st` field
  (`S = { rho_prev: E }`); `O(1)` work per step, no additional state-monad
  complexity.

Both obstructions are made explicit as bounded `iterate_while_pure` folds with
step-count predicates; the bound is folded into the carry counter, and the
predicate — not the combinator — encodes the fixed-count (vs. convergence-gated)
nature (the distinction `krylov-step` resolves the other way, with a convergence
predicate; see [`iterate-while`](./iterate-while.md) §Variant axes). Nothing
pretends to be parallel. They are inherited from the L3
[`chebyshev`](../L3/chebyshev.md) partial-obstruction verdict.

### Initial-guess shape: branch vs derived view

The `apply` body opens with a conditional on `initial_guess`. This branch is a
**degenerate-case absorption**, not a residual variant axis: the
`initial_guess = false` path is the algebraic specialisation of the `true` path
under `y_in = 0` (which makes `A·y_in = 0` and `r = x − A·y_in = x`); writing
`y := 0` establishes `y_in = 0` so subsequent sweeps (`it ≥ 2`) follow the
uniform `r = x − A·y` path. The branch fires at most once per `apply` call (only
`it == 1 && not initial_guess`). This is the
[`derived-view-hoisting`](../concepts/derived-view-hoisting.md) pattern at the
*control-flow* boundary: a single `Bool` parameter `initial_guess` replaces what
would otherwise be a constructed-operator variant axis (`ChebOpWithGuess` vs
`ChebOpNoGuess`). Promoting `initial_guess` to a closure variant would inflate
the closure-type lattice to four (`Kind4 × {guess, no-guess}`, `Kind1 × {guess,
no-guess}`) for no structural benefit — keeping it a per-call `Bool` preserves
the [`variant-absorption`](../concepts/variant-absorption.md) discipline by *not*
over-absorbing.

### Transpose under symmetry

`MultTranspose` is L4-trivial under operator symmetry: `applyTranspose op =
apply op` for SPD `A`. Witnessed by the L0 `MultTranspose2 → Mult2` alias
(`palace/linalg/chebyshev.hpp:72-75`, cited via the L1/L2 entries).

## Algebraic laws

The L4 laws are the L1/L2 body laws sharpened by the typing where the typing
tightens them. Absences are catalogued explicitly.

1. **Affine-in-(x, y) per sweep / linear preconditioner form.** One sweep is the
   affine map `y ↦ y + p_order(D⁻¹ A)·(x − A·y)`. With `initial_guess = false`
   and `pc_it = 1`, the output is `y' = p_order(D⁻¹ A)·x` — a linear function of
   `x`. At L4 the capability typing (`x: Read`, `y: ReadWrite`) makes the
   linear-preconditioner-action shape structural: the consumer hands `apply` a
   `ChebSim` with a fresh zero `y` and reads back the polynomial action. Inherited
   from L1 [`chebyshev-smoother`](../L1/chebyshev-smoother.md) laws 1-2.

2. **Variant-invariant kernel structure.** The `apply` body's primitive sequence
   is identical across 4th-kind and 1st-kind — only `op.scalars` and the closure
   type `S` differ. At L4 this is structural via the `readonly` `ChebOp` typing
   and the distinct-closure-type absorption (no apply-time discriminator).
   Inherited from L2 [`chebyshev-iteration`](../L2/chebyshev-iteration.md) law 2.

3. **Pure-action discipline (no operator mutation; localised sim effect).**
   `apply` does not mutate `op` (the closure is `readonly`); all sim mutation is
   the `y` accumulator (the `Read`/`ReadWrite` typing forbids writing `x`); the
   ephemeral `r`, `d`, `t`, `ay`, `ad` are L4-pure `let`-bindings. The `Solve`
   monad's effect domain is exactly `ChebSim`, and within it only `y` is written.
   This is the L4 effect-localisation discipline made structural by the
   capability typing.

4. **Transpose identity under symmetry.** `applyTranspose op = apply op` for SPD
   `A` (law witness `palace/linalg/chebyshev.hpp:72-75`).

5. **Sweep idempotence on the zero-residual fixed point.** If `A·y = x`, then
   `r = 0`, every `d = 0`, and `apply` leaves `y` unchanged. (Mathematical
   identity; IEEE-754 caveat as L1.)

Laws that explicitly **do not** hold:

- **Obstruction collapse.** The two `iterate_while_pure` folds do **not** reduce
  to a single tensor-field operation under the calculus's reduction rules — the
  inner `k`-recurrence and outer `pc_it`-sweep are genuinely sequential
  (inherited from the L3 partial-obstruction verdict). Neither fold is a `reduce`
  or a parallel map; the step-count predicate does not change this (it bounds the
  iteration, it does not parallelise it — the carry-threaded recurrence forces
  sequentiality, per `iterate-while.md:155` step-composition non-law).
- **Polynomial-expansion equivalence.** Replacing the recurrence with an explicit
  monomial sum is numerically unstable for the operative `order` range; same
  polynomial mathematically, **not** the same algorithm. Load-bearing
  sequentiality (Phillips & Fischer 2022 §2). Inherited from L2.
- **Sweep idempotence in general.** Two `apply` calls compose into `2·pc_it`
  sweeps of error reduction, not `pc_it` — a contraction, not a projection.
  Inherited from L1.
- **Bit-determinism across operator representations / fusion choices.** Inherited
  from L1/L2; load-bearing per CLAUDE.md §"Optimization tricks".
- **Linearity in `y` across the full `pc_it`-sweep action.** Affine, not linear,
  in `y` with a non-zero initial guess (the `M·x` offset). Only the
  `initial_guess = false` single-sweep form (law 1) is linear in `x`.
- **Demand-pruning of a trajectory.** Unlike `krylov-step` (whose `iterate_while`
  trajectory of per-step extras is demand-pruned per §3.8), `chebyshev` produces
  **no** per-step readout to prune — it is inner-product-free and
  convergence-test-free, so there is no `StepOutputs` trajectory and no
  demand-pruning law to state. The `apply` action's only observable is the
  accumulated `y`.

## Dependencies

L4 concept references:

- [`state-stratification`](../concepts/state-stratification.md) — the three-stratum
  split: `ChebSim` (sim; threaded by `Solve`), `ChebOp` (operator-internal;
  `readonly`), and the ephemeral fold-bundle `(r, d, st)` (born per `apply` call,
  discarded on return). The slice's four-way refinement (adding the
  scalar-recurrence stratum `S` threaded through the inner `iterate_while_pure`
  carry) is the worked example this entry instantiates.
- [`solve-monad`](../concepts/solve-monad.md) — the `Solve (ChebSim E)` monad
  threading sim-state (the `y` accumulator) orthogonally to the two
  `iterate_while_pure` value-carries; the capability-typed `Read`/`ReadWrite`
  accessors.
- [`constructed-operators`](../concepts/constructed-operators.md) — the `ChebOp`
  closure absorbing the variant axis at level (c).
- [`variant-absorption`](../concepts/variant-absorption.md) — the level-(c)
  absorption making the polynomial-kind axis structural via the distinct closure
  types `ChebOp E Unit` / `ChebOp E { rho_prev: E }`.
- [`derived-view-hoisting`](../concepts/derived-view-hoisting.md) — the
  control-flow-boundary instance for the `initial_guess` branch.
- [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the
  classification surfacing as the two nested `iterate_while_pure` folds (outer
  `pc_it` sweep, inner `k`-recurrence) with step-count predicates.
- [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md) — the
  initial-direction / final-accumulate loop-boundary unrolling.
- [`elementwise-product`](../concepts/elementwise-product.md) — the `D⁻¹` action
  `dinv ⊙ r` (`.*.`).
- [`chebyshev-iteration`](../concepts/chebyshev-iteration.md) — narrative.

L4 row dependencies (the iteration vocabulary this entry consumes):

- [`iterate-while`](./iterate-while.md) at L4 — the canonical iteration
  primitive; both bounded loops are its `iterate_while_pure` sugar with a
  **step-count predicate** (`s.it <= op.pc_it`, `c.k <= op.order - 1`), the loop
  counter folded into the carry. The fixed-count (vs. convergence-gated)
  distinction lives in the predicate, not the combinator (route (i),
  combinator-miner cycle-014; strawman §6.5 step 5). The inner `st`/`rho_prev`
  recurrence-carry may alternatively use
  [`iterate-while-with-prev`](./iterate-while-with-prev.md) (see §Variant axes);
  this entry adopts the plain `iterate_while_pure` carry-`st` form (4th-kind's
  `st = ()` degenerate case unifies both kinds without a bootstrap step).

Lower-layer rows (the evidence base):

- L2 [`chebyshev-iteration`](../L2/chebyshev-iteration.md) (cycle-012 firm) — the
  primitive composition this L4 wrapper's body is value-thread-isomorphic to;
  carries the L1 primitive-call enumeration, the fusion-transparency classification,
  the scalar recurrences, and the L0 source ranges.
- L1 [`chebyshev-smoother`](../L1/chebyshev-smoother.md) (cycle-012 firm) — the
  closed-form smoother action; carries the constructed-operator-gate framing.

Strawman reference: [`../design/l4_calculus.md`](../design/l4_calculus.md) §2
(ownership categories), §3.7 (the `iterate_while` family — the bounded
`pc_it`/`k` loops are its `iterate_while_pure` sugar with a step-count
predicate), §6.5 step 5 (`l4_calculus.md:418` — the fixed-count bounded loop →
`iterate_while_pure` + step-count-predicate precedent, witnessed by the
`run_lbm` example `:382-385`), §3.8 (demand-pruning, noted as not-applicable —
the trajectory is uniformly empty).

## Lowers to

L4 `chebyshev` lowers to L3 [`chebyshev`](../L3/chebyshev.md) via the
typed-wrapper dissolution (substantive at the wrapper; identity-in-form on the
body), then to L2 [`chebyshev-iteration`](../L2/chebyshev-iteration.md) (the body
identity-in-form, iteration view erased):

- **L4 > L3** (substantive at the wrapper): the `Solve (ChebSim E)` monad
  collapses to explicit `(x, y)`-state threading; the `ChebOp<E, S>` closure
  collapses to a positional operator-parameters value; the `Read`/`ReadWrite`
  capability typing demotes to a documented mutation discipline; the two
  `iterate_while_pure` folds become the L3 `iterate_while_pure_L3` tail
  recursions over their step-count predicates (`iterate-while.md:193-195`),
  matching the L3 `itloop`/`kloop`. The kernel body's primitive sequence is
  value-thread-isomorphic. Same shape as the krylov-step typed-wrapper
  dissolution (`book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`); no
  dedicated chebyshev L4>L3 theme authored by this dispatch (Open Question).
- **L3 > L2** (identity-in-form on the body): the explicit iteration view erases;
  the body maps line-for-line. In-line annotation, no `L3-L2/` theme file.

## Variant axes

Two axes, both absorbed at construction; neither appears in the per-step kernel
signature:

1. **polynomial-kind** (`Kind4 | Kind1`) — absorbed at level (c) into the
   `ChebOp`'s `scalars` / `scalarInit` and the closure type `S` (`Unit` vs
   `{ rho_prev: E }`). Structural via the distinct closure types — no apply-time
   discriminator.
2. **element-type** (`real | complex`) — the kernel body is identical; only the
   field-algebra primitives (`applyLinop`, `.*.`, `.+.`, `.-.`, `.*`) dispatch on
   element type. `dinv` is real-valued even for complex `A`. The complex transpose
   path uses `conj(dinv)` but is dead code under symmetric wiring (Open questions).

`order` and `pc_it` are construction parameters, not variant axes. There is no
first-iteration-unrolled-vs-branch-in-body axis (the `initial_guess` branch is a
`Bool` argument; the initial-direction / final-accumulate unrolling is fixed).
The spectral-bound-estimation method is a setup-side concern in `setup`'s
`spectrumEstimate` sub-action.

There is one **presentation** axis at the inner `k`-recurrence fold, decided
here (not a residual variant axis): the scalar-recurrence state `st`
(`rho_prev` for 1st-kind) may either ride in the `iterate_while_pure` carry
(`{ r, d, st, k }`, this entry's form) **or** be threaded as the closure `prev`
parameter of [`iterate-while-with-prev`](./iterate-while-with-prev.md)
(schema-narrowed carry `{ r, d, k }`, mirroring the CG `beta_prev` treatment).
Both are firm-vocabulary-valid. **This entry adopts the plain `iterate_while_pure`
carry-`st` form**: the 4th-kind's `st = ()` makes it the degenerate no-prev case,
so the carry-`st` form unifies both polynomial kinds without a bootstrap step,
whereas the with-prev form would require a bootstrap `first_step` that the
4th-kind does not need. (Decided cycle-015, resolving combinator-miner OQ
`chebyshev-l4-inner-loop-presentation-carry-st-vs-with-prev`. If a
same-layer-cross-cutter later wants to unify the `st`-carry with the CG
`beta_prev`-carry under one recurrence-variable-threading note, that is a
separate sideways emission, not a change to this entry's chosen form.)

## Status

`firm` — re-anchored cycle-015 (lifter
`reports/2026-05-28T202138Z-lifter-chebyshev-l4-firm-via-iterate-while-reanchor/`).
The body re-typing is a clean re-type of the cycle-012 firm L1/L2 entries against
the L4 state-stratification idiom: the `ChebOp` closure absorbs the variant at
level (c) via distinct closure types; `initial_guess` is the
degenerate-case-absorption `Bool`; the capability typing makes the mutation
discipline structural; every body algebraic law is the L1/L2 body law sharpened
by the typing, and the body-level non-laws (obstruction non-collapse,
polynomial-expansion non-equivalence) are inherited. The two sequential
obstructions are now rendered as nested
[`iterate_while_pure`](./iterate-while.md) folds with **step-count predicates**
(`s.it <= op.pc_it`, `c.k <= op.order - 1`), the loop counter folded into the
carry — reusing the canonical firm `iterate-while` family per the cycle-014
combinator-miner route (i), strawman §6.5 step 5
(`book/src/design/l4_calculus.md:418`; `run_lbm` precedent `:382-385`). The L4
form is methodology-level — Palace's C++ realises the behaviour, not the typed
wrapper; the L0 evidence is transitive through the L1/L2 entries.

**Wrapper-iteration-vocabulary reconcile (the former `rough-in` driver) — closed
cycle-015.** The cycle-013 repairer downgraded this entry `firm`→`rough-in`
because the two sequential obstructions were rendered as un-anchored `forM_`
(outer `pc_it`) / `foldM` (inner `k`) binds, which had no L4 dep-map row, no
concept page, and competed with the firm canonical
[`iterate-while`](./iterate-while.md) family (whose entry, `iterate-while.md:7`,
names **Chebyshev** as a consumer). The cycle-014 combinator-miner
(`reports/2026-05-28T193256Z-combinator-miner-chebyshev-l4-wrapper-iteration-vocabulary-reconcile/`)
decided **route (i): REUSE the `iterate-while` family** — both bounded loops are
`iterate_while_pure` with a step-count predicate, the fixed-count
(vs. convergence-gated) distinction living in the predicate, not the combinator.
This cycle-015 lifter pass enacts that re-anchor (§Semantics body + the prose
naming `forM_`/`foldM` throughout) and the `L4/index.md` dep-map row rewrite,
closing OQ `chebyshev-l4-firm-via-iterate-while-reanchor`. The inner-loop
presentation question (`iterate_while_pure` carry-`st` vs.
`iterate-while-with-prev` closure-`prev`) is **resolved to the plain
carry-`st` form** — see §Variant axes — closing OQ
`chebyshev-l4-inner-loop-presentation-carry-st-vs-with-prev`.

**Caveat (independent of the above; never the status driver)**: no dedicated unit
test (multigrid-integration coverage only) — same justification as the firm L1/L2
entries.

## L4 vs L3 distinction

- **L4**: typed `Solve`-monad wrapper. `ChebOp<E, S>` `readonly` closure;
  `apply :: ChebOp E S -> Bool -> Solve (ChebSim E) ()` threads the
  capability-typed `ChebSim` (`x: Read`, `y: ReadWrite`); the two obstructions
  are nested `iterate_while_pure` folds with step-count predicates (outer
  `pc_it` / inner `k`); variant absorption is structural via distinct closure
  types.
- **L3**: value-threaded positional form `(op, x, y, initial_guess) -> y'`. The
  `Solve` monad has dissolved (`(x, y)` threaded explicitly; `modifyY` →
  explicit `let y' = ...`); the capability typing has demoted to a documented
  invariant; the closure types have collapsed to one positional `op`; the two
  `iterate_while_pure` folds become `iterate_while_pure_L3` tail recursions over
  their step-count predicates. The kernel body's primitive sequence is
  value-thread-isomorphic to L4.

## Evidence

- `book/src/L2/chebyshev-iteration.md` (cycle-012 firm) — the L2 primitive
  composition this L4 wrapper's body is value-thread-isomorphic to; the L1
  primitive-call enumeration, fusion-transparency classification, scalar
  recurrences (4th-kind closed form; 1st-kind `ρ`-threaded), and L0 source ranges
  are cited there and inherited.
- `book/src/L1/chebyshev-smoother.md` (cycle-012 firm) — the L1 closed-form
  smoother action; the constructed-operator-gate framing, the affine/linear laws,
  the transpose-under-symmetry law, and the `initial_guess` degenerate-case
  absorption are anchored there.
- `book/src/L3/chebyshev.md` (this cycle) — the value-threaded L3 form this L4
  entry lifts from; the partial-obstruction verdict (body lifts, loops do not)
  this entry's two `iterate_while_pure` folds inherit.
- `book/src/L4/krylov-step.md` (cycle-006 firm) — the typed-wrapper precedent
  (state-stratification records, `Solve` monad, `readonly` `OpParams`,
  effect-localisation discipline) this entry follows, and the contrast operator:
  `krylov-step` folds via a **convergence**-predicate `iterate_while` with a
  demand-pruned trajectory; `chebyshev` folds via a **step-count**-predicate
  `iterate_while_pure` with a uniformly-empty trajectory. Both consume the
  [`iterate-while`](./iterate-while.md) family; the predicate shape is the
  distinction.
- `book/src/L4/iterate-while.md` (cycle-007 firm) — the canonical iteration
  primitive this entry's two bounded loops consume via `iterate_while_pure` with
  a step-count predicate; `iterate-while.md:7` names Chebyshev as a consumer,
  `:57,102,165` give the counter-folded-into-carry predicate discipline +
  bounded totality discharge, `:193-195` the `iterate_while_pure_L3` lowering
  image.
- `book/src/design/l4_calculus.md` §2 (ownership categories), §3.7 (`iterate_while`
  family — the bounded `pc_it`/`k` loops are its `iterate_while_pure` sugar with
  a step-count predicate), §6.5 step 5 (`:418` — the fixed-count → step-count-
  predicate precedent; `run_lbm` witness `:382-385`), §3.8 (demand-pruning,
  not-applicable for the uniformly-empty-trajectory smoother) — the strawman
  conventions this entry cites and continues.
- `palace/linalg/chebyshev.cpp:191-220, :261-293` (4th/1st-kind `Mult2`; verified
  via codemap) — the L0 behaviour the L4 typed wrapper re-types; cited transitively
  via the L1/L2 entries. The outer `iterate_while_pure` is the L4 surface of
  `for (int it = 0; it < pc_it; it++)` (`:191`); the inner `iterate_while_pure`
  is the L4 surface of `for (int k = 1; k < order; k++)` (`:200`).
- `palace/linalg/chebyshev.hpp:72-75` (`MultTranspose2 → Mult2`; verified via
  codemap) — the transpose-under-symmetry law witness (law 4).
- Provenance: the cycle-001-era §L4 "calculus form" this entry promotes (the
  `ChebOp`/`ChebSim` types, the `apply` monadic action, the `setup` action, the
  capability-typed sim-state, the initial-guess branch-vs-derived-view discussion)
  was lifted from the cycle-001-era Phase-1 chebyshev §L4 (439-line form), reduced
  cycle-015 once its material became authoritative here and deleted cycle-099
  (graded-stack P2; git history is the record). The former §L4's `forM_`/`foldM` rendering of
  the two obstructions is **superseded** here by the `iterate_while_pure` +
  step-count-predicate re-anchor (cycle-014 combinator-miner route (i), enacted
  cycle-015) — the slice predates the firm `iterate-while` family (cycle-007).

No L0 Palace source range "is" the L4 `chebyshev`; the L4 form names a typed
shape, and all L0 evidence is transitive through the cycle-012 firm L1/L2 entries.
