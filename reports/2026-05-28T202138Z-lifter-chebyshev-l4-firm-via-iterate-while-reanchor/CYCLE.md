---
agent: lifter
invoked_at: 2026-05-28T20:21:38Z
scope: L4>L3 theme re-anchor — chebyshev (L4 entry firm-via-iterate-while re-anchor)
status: integrated
integrated_at: 2026-05-29T0030Z
integration_commit: 1af0c3d
integration_notes: "Applied cycle-015 (per-report position 2). L4/chebyshev rough-in->firm ENACTED — apply body re-anchored forM_/foldM -> nested iterate_while_pure folds with step-count predicates, reusing the canonical iterate-while family. L4 firm 3->4, rough-in cohort -> 0. OQs chebyshev-l4-firm-via-iterate-while-reanchor + chebyshev-l4-inner-loop-presentation-carry-st-vs-with-prev closed. All 19 proposed-change blocks applied clean; book build clean. (Three residual forM_/foldM prose mentions outside re-anchor blocks routed to cycle-016 OQ l4-chebyshev-residual-formm-foldm-prose-cleanup.)"
inputs:
  - book/src/L4/chebyshev.md (rough-in; the re-anchor target)
  - book/src/L4/index.md (dep-map row + cohort counts)
  - book/src/L4/iterate-while.md (the canonical firm family being re-anchored onto)
  - book/src/L4/krylov-step.md (firm house-style precedent)
  - book/src/design/l4_calculus.md:376-385,418 (strawman §6.5 step 5 — fixed-count → iterate_while_pure + step-count predicate)
  - reports/2026-05-28T193256Z-combinator-miner-chebyshev-l4-wrapper-iteration-vocabulary-reconcile/CYCLE.md (route (i) + concrete re-anchor sketch)
---

# CYCLE: Re-anchor chebyshev (L4) — `forM_`/`foldM` → `iterate_while_pure` + step-count predicate; flip rough-in → firm

## Summary

`book/src/L4/chebyshev.md` was `rough-in` for exactly one reason: its `apply`
body rendered the two sequential obstructions (outer `pc_it` Richardson sweep,
inner `k`-degree recurrence) as **un-anchored** `forM_` / `foldM` binds, which
have no L4 dep-map row, no concept page, and compete with the firm canonical
[`iterate-while`](../../book/src/L4/iterate-while.md) family (whose own entry,
`iterate-while.md:7`, names **Chebyshev** as a consumer of the canonical
iteration primitive). The cycle-014 combinator-miner decided **route (i):
REUSE the `iterate-while` family** — both bounded loops are
`iterate_while_pure` with a **step-count predicate** (`s.it <= bound`), the loop
counter folded into the carry; the fixed-count-vs-convergence distinction lives
in the *predicate*, not the combinator (strawman §6.5 step 5,
`book/src/design/l4_calculus.md:418`; `run_lbm` precedent `:376-385`). This is a
**pure re-anchoring pass**: I re-express the `apply` body (and the prose that
names `forM_`/`foldM`) using `iterate_while_pure`, leaving the entry's
structure, semantics, signature, and chebyshev math untouched, then flip the
status `rough-in` → `firm` and the L4 index dep-map cell (`rough-in` → `firm`,
L4 firm cohort **3 → 4**). The un-anchored-vocabulary blocker — the sole reason
for `rough-in` — is resolved.

## Proposed changes

### Change 1 — re-anchor the `apply` body (§Semantics)

The two un-anchored binds become two `iterate_while_pure` folds with step-count
predicates and the counter folded into the carry. The `y` accumulator stays a
`Solve (ChebSim E)` effect threaded orthogonally to the value-carry (the
no-extras / empty-trajectory case per `iterate-while.md:98`, exactly the
strawman `run_lbm` shape). The inner loop's `(r, d, st)` tuple plus its counter
`k` becomes the inner carry record (OQ resolution below).

```edit:book/src/L4/chebyshev.md
[old]:
```text
apply :: ChebOp E S -> Bool -> Solve (ChebSim E) ()
apply op initial_guess = do
  x <- readX
  forM_ [1 .. op.pc_it] $ \it -> do
    -- 1. residual r0 = x − A·y   (or r0 = x; y := 0 on first sweep w/o guess)
    r0 <- if it == 1 && not initial_guess
            then do { writeY zero; pure x }
            else do { y <- readY; ay <- applyLinop op.A y; pure (x .-. ay) }

    -- 2. initial direction d0 = α₀ · (dinv ⊙ r0)
    let { α₀: c0, st: st0 } = op.scalars 0 op.scalarInit
    let d0 = c0 .* (op.dinv .*. r0)

    -- 3. inner k-recurrence (sequential obstruction in k)
    (rN, dN, stN) <- foldM (innerStep op) (r0, d0, st0) [1 .. op.order - 1]

    -- 4. final accumulation
    modifyY (\y -> y .+. dN)
  where
    innerStep op (r, d, st) k = do
      modifyY (\y -> y .+. d)                    -- y += d
      ad <- applyLinop op.A d
      let r' = r .-. ad                          -- r −= A·d
      let { sd, sr, st: st' } = op.scalars k st
      let t  = op.dinv .*. r'                     -- dinv ⊙ r'
      let d' = sd .* d .+. sr .* t                -- d = sd·d + sr·t
      pure (r', d', st')
```

The field expressions `(x .-. ay)`, `(sd .* d .+. sr .* t)`, etc. are pure
values — the `r`, `d`, `t`, `ay`, `ad` bindings are immutable `let`-bindings to
field-algebra results, not in-place buffers. The L2/runtime is free to realise
them via in-place `axpy`/`scal` on aliased storage; that is the standard
transparent optimization handled below L4 and does not surface here.

What the L4 typing adds is **placement discipline**: every field-algebra call
sits in a pure `let`-binding; the only monadic effects are the `writeY`
(degenerate-case `y := 0`) and the `modifyY` accumulator updates; `x` is read
once via `readX` and never written. The `Solve` monad's effect domain is exactly
`ChebSim`.
[new]:
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
```

### Change 2 — re-anchor the §Semantics intro paragraph (the `forM_`/`foldM` description)

```edit:book/src/L4/chebyshev.md
[old]:
`chebyshev` at L4 is the constructed-operator smoother whose `apply` action
applies `op.pc_it` Richardson sweeps of a degree-`op.order` matrix polynomial of
`D⁻¹ A`. The two sequential obstructions surface as explicit `forM_` (outer) and
`foldM` (inner) binds in the `Solve` monad; each step is a pure tensor-field
expression on the field algebra; the monad threads the sim-state accumulator `y`
and the fold threads the ephemeral `(r, d)` plus the scalar-state `st`.
[new]:
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
```

### Change 3 — re-anchor the §"Sequential obstructions at L4" bullets

```edit:book/src/L4/chebyshev.md
[old]:
- The `forM_ [1 .. op.pc_it]` outer bind is the L4 surface of the Richardson-sweep
  sequentiality (each sweep consumes the previous sweep's accumulated `y`).
- The `foldM (innerStep op) (r0, d0, st0) [1 .. op.order - 1]` is the L4 surface
  of the three-term-recurrence sequentiality in `k`. The accumulator threads
  `(r, d, scalar_state)`; each `innerStep` consumes the previous tuple. This is
  the canonical L4 shape for a [`sequential-obstruction`](../concepts/sequential-obstruction.md)
  that lifted only at the body level — `foldM` over a finite range, body pure
  field arithmetic.
- The 1st-kind `ρ_k` scalar update rides inside the `S = { rho_prev: E }` fold
  state; `O(1)` work per step, no additional state-monad complexity.

Both obstructions are made explicit as bounded monadic binds; nothing pretends to
be parallel. They are inherited from the L3 [`chebyshev`](../L3/chebyshev.md)
partial-obstruction verdict.
[new]:
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
```

### Change 4 — re-anchor the §"L4 > L3" relationship bullet (the §Context block)

```edit:book/src/L4/chebyshev.md
[old]:
- **L4 > L3** (substantive at the wrapper; identity-in-form on the body): the
  `Solve (ChebSim E)` monad dissolves to explicit `(x, y)`-state threading; the
  `ChebOp<E, S>` closure dissolves to a positional operator-parameters value;
  the `Read`/`ReadWrite` capability typing on `ChebSim` demotes to a documented
  mutation discipline; the `forM_`/`foldM` binds dissolve to tail recursions
  over static ranges. The kernel body's primitive sequence is value-thread-
  isomorphic to L3 [`chebyshev`](../L3/chebyshev.md). This is the same
  wrapper-dissolution shape that
[new]:
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
```

### Change 5 — re-anchor the §"Pure-action discipline" law 3 effect-domain mention

The §"Solve monad's effect domain" sentence in Signature shape-contract point 3
already names `writeY`/`modifyY` and is correct as-is; no `forM_`/`foldM`
reference there. Law 3 in §Algebraic laws is likewise vocabulary-clean. The
**non-law** that names the binds (§Algebraic laws → "Obstruction collapse") needs
the vocabulary update:

```edit:book/src/L4/chebyshev.md
[old]:
- **Obstruction collapse.** The `forM_`/`foldM` binds do **not** reduce to a
  single tensor-field operation under the calculus's reduction rules — the inner
  `k`-recurrence and outer `pc_it`-sweep are genuinely sequential (inherited from
  the L3 partial-obstruction verdict). The `foldM` is not a `reduce`; the `forM_`
  is not a parallel map.
[new]:
- **Obstruction collapse.** The two `iterate_while_pure` folds do **not** reduce
  to a single tensor-field operation under the calculus's reduction rules — the
  inner `k`-recurrence and outer `pc_it`-sweep are genuinely sequential
  (inherited from the L3 partial-obstruction verdict). Neither fold is a `reduce`
  or a parallel map; the step-count predicate does not change this (it bounds the
  iteration, it does not parallelise it — the carry-threaded recurrence forces
  sequentiality, per `iterate-while.md:155` step-composition non-law).
```

### Change 6 — re-anchor the §Dependencies `solve-monad` concept reference + strawman reference

```edit:book/src/L4/chebyshev.md
[old]:
- [`solve-monad`](../concepts/solve-monad.md) — the `Solve (ChebSim E)` monad
  threading sim-state through `forM_` and `foldM`; the capability-typed `Read`/
  `ReadWrite` accessors.
[new]:
- [`solve-monad`](../concepts/solve-monad.md) — the `Solve (ChebSim E)` monad
  threading sim-state (the `y` accumulator) orthogonally to the two
  `iterate_while_pure` value-carries; the capability-typed `Read`/`ReadWrite`
  accessors.
```

```edit:book/src/L4/chebyshev.md
[old]:
Strawman reference: [`../design/l4_calculus.md`](../design/l4_calculus.md) §2
(ownership categories), §3.7 (the `iterate_while` family, contrasted here with
the bounded `forM_`/`foldM`), §3.8 (demand-pruning, noted as not-applicable —
no trajectory).
[new]:
Strawman reference: [`../design/l4_calculus.md`](../design/l4_calculus.md) §2
(ownership categories), §3.7 (the `iterate_while` family — the bounded
`pc_it`/`k` loops are its `iterate_while_pure` sugar with a step-count
predicate), §6.5 step 5 (`l4_calculus.md:418` — the fixed-count bounded loop →
`iterate_while_pure` + step-count-predicate precedent, witnessed by the
`run_lbm` example `:382-385`), §3.8 (demand-pruning, noted as not-applicable —
the trajectory is uniformly empty).
```

### Change 7 — add the L4-row dependency to §Dependencies

The entry now consumes a firm L4 row (`iterate-while`); the §Dependencies block
currently lists only concept references and L1/L2 evidence rows. Add the L4-row
dependency (mirroring `krylov-step.md`'s "L4 row dependencies" structure):

```edit:book/src/L4/chebyshev.md
[old]:
Lower-layer rows (the evidence base):

- L2 [`chebyshev-iteration`](../L2/chebyshev-iteration.md) (cycle-012 firm) — the
  primitive composition this L4 wrapper's body is value-thread-isomorphic to;
  carries the L1 primitive-call enumeration, the fusion-transparency classification,
  the scalar recurrences, and the L0 source ranges.
- L1 [`chebyshev-smoother`](../L1/chebyshev-smoother.md) (cycle-012 firm) — the
  closed-form smoother action; carries the constructed-operator-gate framing.
[new]:
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
```

### Change 8 — re-anchor the §"Lowers to" L4>L3 bullet

```edit:book/src/L4/chebyshev.md
[old]:
- **L4 > L3** (substantive at the wrapper): the `Solve (ChebSim E)` monad
  collapses to explicit `(x, y)`-state threading; the `ChebOp<E, S>` closure
  collapses to a positional operator-parameters value; the `Read`/`ReadWrite`
  capability typing demotes to a documented mutation discipline; the `forM_`/
  `foldM` binds become tail recursions over static ranges. The kernel body's
  primitive sequence is value-thread-isomorphic. Same shape as the krylov-step
  typed-wrapper dissolution (`book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`);
  no dedicated chebyshev L4>L3 theme authored by this dispatch (Open Question).
[new]:
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
```

### Change 9 — re-anchor the §"L4 vs L3 distinction" bullets

```edit:book/src/L4/chebyshev.md
[old]:
- **L4**: typed `Solve`-monad wrapper. `ChebOp<E, S>` `readonly` closure;
  `apply :: ChebOp E S -> Bool -> Solve (ChebSim E) ()` threads the
  capability-typed `ChebSim` (`x: Read`, `y: ReadWrite`); the two obstructions
  are `forM_` (outer) / `foldM` (inner) binds; variant absorption is structural
  via distinct closure types.
- **L3**: value-threaded positional form `(op, x, y, initial_guess) -> y'`. The
  `Solve` monad has dissolved (`(x, y)` threaded explicitly; `modifyY` →
  explicit `let y' = ...`); the capability typing has demoted to a documented
  invariant; the closure types have collapsed to one positional `op`; the
  `forM_`/`foldM` are tail recursions over static ranges. The kernel body's
  primitive sequence is value-thread-isomorphic to L4.
[new]:
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
```

### Change 10 — re-anchor §"chebyshev is NOT an instance of krylov-step" (§Context)

This paragraph contrasts the smoother against `krylov-step` and currently asserts
the obstructions are `forM_`/`foldM` "not `iterate_while`". After route (i) the
obstructions ARE `iterate_while` (specifically `iterate_while_pure`); the
contrast that survives is the **predicate shape** (step-count vs. convergence),
not the combinator. Re-anchor:

```edit:book/src/L4/chebyshev.md
[old]:
`chebyshev` at L4 is **not** an instance of [`krylov-step`](./krylov-step.md).
The Krylov step kernel is folded by a predicate-driven `iterate_while` over a
trajectory of demand-prunable per-step extras; the Chebyshev smoother has **no
convergence predicate** (the loops are bounded static ranges `[1 .. pc_it]` and
`[1 .. order-1]`) and is **inner-product-free** (no `dot` / `nrm2` reduction; no
residual-norm trajectory). It is therefore the canonical L4 example of a
**fixed-degree** operator whose sequential obstructions are `forM_` (bounded
outer iteration) and `foldM` (bounded inner recurrence), not `iterate_while`.
[new]:
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
```

### Change 11 — re-anchor the §Status block (flip rough-in → firm; remove the wrapper caveat)

The wrapper caveat IS the status driver and is now resolved; the resolution-path
note becomes a closed historical note. The independent no-dedicated-unit-test
caveat stays (it never drove the status — it matches the firm L1/L2 entries).

```edit:book/src/L4/chebyshev.md
[old]:
## Status

`rough-in` — **firm at the body, rough-in at the wrapper.** The body re-typing is
a clean re-type of the cycle-012 firm L1/L2 entries against the L4
state-stratification idiom: the `ChebOp` closure absorbs the variant at level (c)
via distinct closure types; `initial_guess` is the degenerate-case-absorption
`Bool`; the capability typing makes the mutation discipline structural; every
body algebraic law is the L1/L2 body law sharpened by the typing, and the
body-level non-laws (obstruction non-collapse, polynomial-expansion
non-equivalence) are inherited. The L4 form is methodology-level — Palace's C++
realises the behaviour, not the typed wrapper; the L0 evidence is transitive
through the L1/L2 entries.

**Wrapper caveat (the reason this is `rough-in`, not `firm`)** — repairer
downgrade, cycle-013. The two sequential obstructions are rendered here as
`forM_` (outer `pc_it`) and `foldM` (inner `k`) binds, but **these iteration
combinators are not anchored at L4**: they have no L4 dep-map row and no concept
page, and they compete with the firm canonical iteration vocabulary
[`iterate-while`](./iterate-while.md) (whose own entry, `iterate-while.md:7`,
declares itself the "canonical iteration primitive at L4" and explicitly names
**Chebyshev** as one of its consumers) and its `iterate-while-with-prev`
companion (cycle-007 firm). The strawman maps bounded loops to
`iterate_while_pure` with a step-count predicate
(`book/src/design/l4_calculus.md` §6). The `forM_`/`foldM` rendering is a
faithful verbatim promotion of the cycle-001-era pre-redirect slice §L4
(`book/src/spec/slices/chebyshev.md:289, 325, 396-397`), but the promotion did
**not reconcile** the slice's combinators against the now-firm `iterate-while`
family. Until the wrapper's iteration combinators are reconciled — either by
re-expressing the bounded loops via `iterate_while_pure`/`iterate-while-with-prev`
with step-count predicates (strawman-conformant, reuses canonical vocabulary), or
by anchoring `forM_`/`foldM` as their own firm L4 rows — the entry over-claims at
`firm`. **Escalated to a combinator-miner / lifter follow-up** (see Open Question
6). The body is firm; the wrapper-iteration vocabulary is the open part.

**Resolution path (cycle-014 combinator-miner; enactment scheduled cycle-015).**
The reconcile has a decided route: the cycle-014 combinator-miner
(`reports/2026-05-28T193256Z-combinator-miner-chebyshev-l4-wrapper-iteration-vocabulary-reconcile/`)
selected route (i) — **REUSE the `iterate-while` family, do NOT firm a new
combinator.** The two un-anchored binds re-anchor onto the canonical firm
vocabulary: `forM_` (outer `pc_it` sweep) and `foldM` (inner `k`-recurrence)
both become [`iterate_while_pure`](./iterate-while.md) with a **step-count
predicate** (`s.it <= bound`), the loop counter folded into the carry — the
"fixed-count vs. convergence-gated" distinction lives in the **predicate**, not
the combinator (strawman §6.5 step 5, `book/src/design/l4_calculus.md:418`; the
`run_lbm` bounded-loop precedent `:382-385`). The inner `st`/`rho_prev`
recurrence-carry may alternatively use
[`iterate-while-with-prev`](./iterate-while-with-prev.md) (see OQ
`chebyshev-l4-inner-loop-presentation-carry-st-vs-with-prev`). A **cycle-015
lifter/abstractor** enacts the body re-anchor of §Signature/§Semantics + the
`L4/index.md` dep-map row rewrite, **then flips this Status `rough-in`→`firm`**
(L4 firm 3→4). The concrete re-anchored `apply` body sketch is staged in the
combinator-miner CYCLE.md §"Proposed combinator". Tracking OQ:
`chebyshev-l4-firm-via-iterate-while-reanchor`. (This note does not itself flip
the status — enactment is the cycle-015 follow-up's work.)

**Caveat (independent of the above; not the status driver)**: no dedicated unit
test (multigrid-integration coverage only) — same justification as the firm L1/L2
entries.
[new]:
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
```

### Change 12 — add the inner-loop-presentation resolution to §Variant axes

The combinator-miner flagged a variant axis (inner-loop presentation). The OQ is
resolved to the plain carry-`st` form; record the decision in §Variant axes
(where the combinator-miner located the axis) so the entry is self-contained.

```edit:book/src/L4/chebyshev.md
[old]:
`order` and `pc_it` are construction parameters, not variant axes. There is no
first-iteration-unrolled-vs-branch-in-body axis (the `initial_guess` branch is a
`Bool` argument; the initial-direction / final-accumulate unrolling is fixed).
The spectral-bound-estimation method is a setup-side concern in `setup`'s
`spectrumEstimate` sub-action.
[new]:
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
```

### Change 13 — re-anchor the §Evidence krylov-step contrast bullet

```edit:book/src/L4/chebyshev.md
[old]:
- `book/src/L4/krylov-step.md` (cycle-006 firm) — the typed-wrapper precedent
  (state-stratification records, `Solve` monad, `readonly` `OpParams`,
  effect-localisation discipline) this entry follows, and the contrast operator:
  `krylov-step` folds via predicate-driven `iterate_while` with a demand-pruned
  trajectory; `chebyshev` uses bounded `forM_`/`foldM` with no trajectory.
[new]:
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
```

### Change 14 — re-anchor the §Evidence strawman + slice + L0 bullets

```edit:book/src/L4/chebyshev.md
[old]:
- `book/src/design/l4_calculus.md` §2 (ownership categories), §3.7 (`iterate_while`
  family, contrasted with the bounded `forM_`/`foldM`), §3.8 (demand-pruning,
  not-applicable for the no-trajectory smoother) — the strawman conventions this
  entry cites and continues.
- `palace/linalg/chebyshev.cpp:191-220, :261-293` (4th/1st-kind `Mult2`; verified
  via codemap) — the L0 behaviour the L4 typed wrapper re-types; cited transitively
  via the L1/L2 entries. The `forM_` outer loop is the `for (int it = 0; it <
  pc_it; it++)`; the `foldM` inner loop is the `for (int k = 1; k < order; k++)`.
[new]:
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
```

### Change 15 — re-anchor the §Evidence slice-corpus bullet

```edit:book/src/L4/chebyshev.md
[old]:
- `book/src/spec/slices/chebyshev.md:287-439` — the cycle-001-era §L4 "calculus
  form" this entry promotes (the `ChebOp`/`ChebSim` types, the `apply` monadic
  action, the `setup` action, the sequential-obstruction-as-`forM_`/`foldM`
  treatment, the capability-typed sim-state, the initial-guess branch-vs-derived-view
  discussion).
[new]:
- `book/src/spec/slices/chebyshev.md:287-439` — the cycle-001-era §L4 "calculus
  form" this entry promotes (the `ChebOp`/`ChebSim` types, the `apply` monadic
  action, the `setup` action, the capability-typed sim-state, the initial-guess
  branch-vs-derived-view discussion). The slice's `forM_`/`foldM` rendering of
  the two obstructions is **superseded** here by the `iterate_while_pure` +
  step-count-predicate re-anchor (cycle-014 combinator-miner route (i), enacted
  cycle-015) — the slice predates the firm `iterate-while` family (cycle-007).
```

### Change 16 — update the §Lowers-to top sentence (`forM_`/`foldM` not named there, but verify clean)

The §"Lowers to" intro sentence and the L3>L2 bullet do not name `forM_`/`foldM`
(checked: only the L4>L3 bullet, handled in Change 8). The §"Sequential
obstructions at L4" header block, the §Signature `ChebOp` field docs ("the inner
`foldM` range bound", "the outer `forM_` range bound") DO name the binds —
re-anchor those two field annotations:

```edit:book/src/L4/chebyshev.md
[old]:
  - `order: Int` — polynomial degree (`> 0`); the inner `foldM` range bound.
  - `pc_it: Int` — Richardson-sweep count; the outer `forM_` range bound.
[new]:
  - `order: Int` — polynomial degree (`> 0`); the inner `iterate_while_pure`
    step-count-predicate bound (`c.k <= order - 1`).
  - `pc_it: Int` — Richardson-sweep count; the outer `iterate_while_pure`
    step-count-predicate bound (`s.it <= pc_it`).
```

### Change 17 — re-anchor the §Context lede paragraph (top-of-file summary)

```edit:book/src/L4/chebyshev.md
[old]:
Typed-wrapper fixed-degree polynomial-smoother operator at L4 — the Chebyshev
smoother as a constructed `ChebOp` whose `apply` is a `Solve`-monad action over
a capability-typed sim-state. The thin state-bearing wrapper around the pure
fixed-degree polynomial action; the two sequential obstructions (the outer
`pc_it` Richardson sweep, the inner `k`-recurrence) surface as explicit
`forM_` / `foldM` binds — they do not collapse. Companion to L3
[`chebyshev`](../L3/chebyshev.md) (the value-threaded form of the same body)
and L2 [`chebyshev-iteration`](../L2/chebyshev-iteration.md) (the primitive
composition with the iteration view erased).
[new]:
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
```

### Change 18 — L4 index dep-map: flip status + rewrite Dependencies cell

```edit:book/src/L4/index.md
[old]:
| [`chebyshev`](./chebyshev.md) | `setup :: LinOp[E] -> SetupParams -> Variant -> Solve s (ChebOp E S)`; `apply :: ChebOp E S -> Bool -> Solve (ChebSim E) ()`. Constructed-operator smoother; `ChebOp` `readonly` closure (variant absorbed via distinct closure types `S`); `ChebSim = { x: Read, y: ReadWrite }` capability-typed sim-state. | Concepts: `state-stratification`, `solve-monad`, `constructed-operators`, `variant-absorption`, `derived-view-hoisting`, `sequential-obstruction`, `first-iteration-unrolling`, `elementwise-product`. L4 rows: **iteration combinators UNRECONCILED** — the obstructions are rendered as bounded `forM_`/`foldM`, which are NOT anchored L4 rows and compete with the firm [`iterate-while`](./iterate-while.md) family (whose entry names Chebyshev as a consumer). Reconciliation is a combinator-miner/lifter follow-up (see entry §Status + OQ 6). | L3 [`chebyshev`](../L3/chebyshev.md) via typed-wrapper dissolution (substantive at wrapper; identity-in-form on body; no L4-L3 theme file — same shape as `krylov-step-typed-wrapper-dissolution`), then L2 [`chebyshev-iteration`](../L2/chebyshev-iteration.md). | `rough-in` (harvested cycle-013T143923Z; firm at the body re-type of the cycle-012 firm L1/L2 entries, but rough-in at the wrapper — repairer downgrade cycle-013: the `forM_`/`foldM` iteration combinators are un-anchored and unreconciled against the firm `iterate-while` family) |
[new]:
| [`chebyshev`](./chebyshev.md) | `setup :: LinOp[E] -> SetupParams -> Variant -> Solve s (ChebOp E S)`; `apply :: ChebOp E S -> Bool -> Solve (ChebSim E) ()`. Constructed-operator smoother; `ChebOp` `readonly` closure (variant absorbed via distinct closure types `S`); `ChebSim = { x: Read, y: ReadWrite }` capability-typed sim-state. | Concepts: `state-stratification`, `solve-monad`, `constructed-operators`, `variant-absorption`, `derived-view-hoisting`, `sequential-obstruction`, `first-iteration-unrolling`, `elementwise-product`. L4 rows: [`iterate-while`](./iterate-while.md) — both bounded loops are its `iterate_while_pure` sugar with a **step-count predicate** (`s.it <= op.pc_it` outer, `c.k <= op.order - 1` inner; counter folded into the carry), per strawman §6.5 step 5 (`l4_calculus.md:418`); the inner `st`/`rho_prev` recurrence-carry may alternatively use [`iterate-while-with-prev`](./iterate-while-with-prev.md) (entry adopts the plain carry-`st` form; see entry §Variant axes). | L3 [`chebyshev`](../L3/chebyshev.md) via typed-wrapper dissolution (substantive at wrapper; identity-in-form on body; no L4-L3 theme file — same shape as `krylov-step-typed-wrapper-dissolution`), then L2 [`chebyshev-iteration`](../L2/chebyshev-iteration.md). | `firm` (harvested cycle-013T143923Z; re-anchored cycle-015T202138Z lifter — the `forM_`/`foldM` obstructions re-expressed as `iterate_while_pure` folds with step-count predicates per cycle-014 combinator-miner route (i), reusing the firm `iterate-while` family; wrapper-vocabulary blocker closed) |
```

### Change 19 — L4 index: move chebyshev from the "Rough-in (1)" cohort into "Firm (3→4)"

```edit:book/src/L4/index.md
[old]:
**Firm at L4 (3)** — the typed-wrapper Krylov step kernel plus the two value-threading loop combinators that drive it:

- [`krylov-step`](./krylov-step.md) — typed-wrapper Krylov step kernel against the three-stratum state record; Form A consumes `iterate-while`, Form B consumes `iterate-while-with-prev`. The L4 calculus's first firm step-body shape.
- [`iterate-while`](./iterate-while.md) — value-threaded tail-recursive loop with demand-pruned trajectory of per-step extras; canonical iteration primitive at L4 (every iterative algorithm reduces to one or more folds). Inherits small-step semantics from the strawman §3.7.
- [`iterate-while-with-prev`](./iterate-while-with-prev.md) — carry-bootstrapped variant of `iterate-while` that threads a `PrevCarry` closure parameter for the previous-iteration recurrence variable. The driver for [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md)'s unrolled form; degenerates to `iterate-while` when `β = ()`.

**Rough-in at L4 (1)** — typed shapes that are firm at the body but carry an open wrapper-vocabulary reconciliation:

- [`chebyshev`](./chebyshev.md) *(rough-in — firm at the body, rough-in at the wrapper)* — typed-wrapper fixed-degree polynomial smoother; the `ChebOp` constructed-operator closure absorbs the polynomial-kind variant via distinct closure types; `apply` is a `Solve (ChebSim E)` action over a capability-typed `ChebSim`. Inner-product-free and convergence-test-free (the fixed-degree contrast to `krylov-step`). The two sequential obstructions are currently rendered as bounded `forM_` (outer `pc_it`) / `foldM` (inner `k`) binds, but **those combinators are un-anchored at L4 and compete with the firm [`iterate-while`](./iterate-while.md) family** (whose entry names Chebyshev as a consumer); reconciling the wrapper iteration vocabulary is a combinator-miner/lifter follow-up before the entry firms (OQ 6).
[new]:
**Firm at L4 (4)** — the typed-wrapper Krylov step kernel, the two value-threading loop combinators that drive it, and the fixed-degree polynomial smoother:

- [`krylov-step`](./krylov-step.md) — typed-wrapper Krylov step kernel against the three-stratum state record; Form A consumes `iterate-while`, Form B consumes `iterate-while-with-prev`. The L4 calculus's first firm step-body shape.
- [`iterate-while`](./iterate-while.md) — value-threaded tail-recursive loop with demand-pruned trajectory of per-step extras; canonical iteration primitive at L4 (every iterative algorithm reduces to one or more folds). Inherits small-step semantics from the strawman §3.7.
- [`iterate-while-with-prev`](./iterate-while-with-prev.md) — carry-bootstrapped variant of `iterate-while` that threads a `PrevCarry` closure parameter for the previous-iteration recurrence variable. The driver for [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md)'s unrolled form; degenerates to `iterate-while` when `β = ()`.
- [`chebyshev`](./chebyshev.md) — typed-wrapper fixed-degree polynomial smoother; the `ChebOp` constructed-operator closure absorbs the polynomial-kind variant via distinct closure types; `apply` is a `Solve (ChebSim E)` action over a capability-typed `ChebSim`. Inner-product-free and convergence-test-free (the fixed-degree contrast to `krylov-step`): both bounded obstructions (outer `pc_it`, inner `k`) are `iterate_while_pure` folds with **step-count predicates** (the counter folded into the carry), reusing the firm [`iterate-while`](./iterate-while.md) family rather than a separate iteration vocabulary (cycle-014 combinator-miner route (i); re-anchored cycle-015). The fixed-count-vs-convergence distinction lives in the predicate, not the combinator.

**Rough-in at L4 (0)** — none currently.
```

## Discipline notes

This is a **pure structural re-anchoring pass** (lifter discipline). The entry's
narrative, signature (`setup` / `apply` arrow shapes), semantics, algebraic laws,
variant axes, and the chebyshev math are all untouched. The ONLY change is the
**iteration vocabulary**: the two un-anchored `forM_` (outer `pc_it`) / `foldM`
(inner `k`) binds are re-expressed as nested `iterate_while_pure` folds with
step-count predicates (the loop counter folded into the carry), reusing the firm
canonical [`iterate-while`](./iterate-while.md) family. Direction stays
high→low throughout (LHS L4 form lowering toward L3); I did not invert the
rewrite.

**Why this is a lift, not authorship.** The cycle-014 combinator-miner
(`reports/2026-05-28T193256Z-combinator-miner-…/CYCLE.md`) made the substantive
content decision (route (i): REUSE; the concrete `apply`-body sketch is staged in
its §"Proposed combinator", lines 125-162). My pass mechanically applies that
sketch, adjusting only the surface to (a) the entry's existing prose conventions
and (b) the precise Solve-threaded-vs-pure rendering (see below). No
re-derivation of the carry-record design, predicate formulation, or effect
interleaving — those are the combinator-miner's.

**One rendering refinement over the combinator-miner sketch (notation-precision,
not content).** The combinator-miner sketch wrote `iterate_while_pure` while the
step body contained `modifyY` (a `Solve (ChebSim E)` effect). Strictly,
`iterate_while_pure :: α -> (α -> Bool) -> (α -> α) -> α` (`iterate-while.md:22`)
is the *no-Solve-threading* sugar. The reconciliation, already stated in
`iterate-while.md:90,98`, is that the Solve-threaded form is "equivalent to the
pure form modulo the `Sim` effect being orthogonal to the value-threading," and
`iterate_while_pure` is "idiomatic" for the **no-extras / empty-trajectory** case
— which is exactly the smoother (`y` is the orthogonal `ChebSim` effect; the
value-carry has no per-step readouts). So I preserved the combinator-miner's
`iterate_while_pure` framing verbatim (the value-carry IS the pure-shaped slot;
the trajectory IS uniformly empty) and added a clarifying sentence pinning it to
the `iterate-while.md:98` no-extras case + the strawman `run_lbm` shape
(`l4_calculus.md:382-385`), which is the identical pattern (a `Solve`-free pure
fold in that example, but the same empty-trajectory carry-threading shape). This
is a notation-precision note, NOT a content change — the combinator-miner's
chosen combinator stands.

**Inner-loop-presentation OQ — RESOLVED (not carried forward).** The
combinator-miner flagged a presentation axis (OQ
`chebyshev-l4-inner-loop-presentation-carry-st-vs-with-prev`): the inner loop's
`st`/`rho_prev` recurrence variable can either ride in the `iterate_while_pure`
carry (`{ r, d, st, k }`) or be threaded as the `iterate-while-with-prev` closure
`prev` parameter. The combinator-miner *recommended* the plain carry-`st` form
(its OQ 1) on the ground that 4th-kind's `st = ()` makes the carry-`st` form the
degenerate no-prev case, unifying both polynomial kinds without a bootstrap step.
The re-anchor sketch the combinator-miner staged uses the carry-`st` form. I
adopt that resolution: the entry now uses `iterate_while_pure` with `st` in the
carry, and §Variant axes (Change 12) + §Status (Change 11) record the decision
and close the OQ. This is within lifter discipline because the combinator-miner
both staged the carry-`st` sketch AND recommended it as default — I am enacting
the staged resolution, not making a fresh content choice. (Open Question 1 below
records the residual same-layer-cross-cutter watch-item the combinator-miner
attached, which is NOT a blocker on this entry's firm status.)

**Prose-correction note (bounded, evidenced, recorded).** Change 10 corrects a
claim that was *made backward* by the re-anchor: the §Context paragraph asserted
the obstructions are "`forM_`/`foldM`, **not** `iterate_while`." After route (i)
that is false — they ARE `iterate_while` (specifically `iterate_while_pure`); the
surviving contrast with `krylov-step` is the **predicate shape** (step-count vs.
convergence), which is precisely what `iterate-while.md` §Variant axes
(`:201-207`) and the combinator-miner report (lines 176-179) identify as the
distinguishing axis. The correction is directly supported by `iterate-while.md:7`
(names Chebyshev as a consumer) + `:90,98` (Solve-threaded ≡ pure modulo
orthogonal effect) and is bounded (it rewrites a now-false contrast sentence; it
does not re-architect the entry's decomposition or signature). Recorded here per
the lifter `lifter-scope-content-correction-boundary` friction-ledger discipline.

## Supporting evidence

- `reports/2026-05-28T193256Z-combinator-miner-chebyshev-l4-wrapper-iteration-vocabulary-reconcile/CYCLE.md`
  — the cycle-014 route (i) decision + the staged `apply`-body sketch (lines
  125-162) this pass mechanically applies; OQ 1 (inner-loop presentation, resolved
  here) at lines 257-265.
- `book/src/L4/iterate-while.md:7` — canonical-primitive claim naming Chebyshev as
  a consumer (the constraint route (i) satisfies); `:22` the `iterate_while_pure`
  signature; `:57,102,165` predicate-discipline (counter folded into carry) +
  bounded-totality discharge; `:90,98` Solve-threaded ≡ pure modulo orthogonal
  effect + no-extras idiom; `:155` step-composition non-law; `:193-195`
  `iterate_while_pure_L3` lowering image; `:201-207` predicate-shape variant axis.
- `book/src/design/l4_calculus.md:418` — strawman §6.5 step 5: fixed-count bounded
  loop → `iterate_while_pure` with step-count predicate (the decisive precedent);
  `:376-385` the `run_lbm` worked example (live call shape).
- `book/src/L4/krylov-step.md` (cycle-006 firm) — house-style precedent for the
  §Status / §Dependencies / §"L4 vs L_n distinction" structure; the convergence-
  predicate contrast operator.
- `book/src/L4/chebyshev.md` (cycle-013 rough-in) — the re-anchor target; §Status
  (lines 387-444) carried the wrapper caveat + the cycle-014 resolution-path note;
  §Semantics (lines 124-221) the body re-anchored here.
- `book/src/L4/index.md:32-56` — the Firm/Rough-in cohort lists + the dep-map row.

## Open questions / caveats

1. **Same-layer-cross-cutter watch-item (NOT a blocker on firm status)** — the
   combinator-miner's OQ 1 attached a follow-up: a same-layer-cross-cutter MAY
   later want to unify this entry's inner `st`-carry with the CG `beta_prev`-carry
   under one shared "recurrence-variable-threading" note (the with-prev form
   mirrors CG's treatment). This entry's chosen form (plain `iterate_while_pure`
   carry-`st`) is firm regardless; the unification, if pursued, is a sideways
   concept emission, not a change to this entry. Carrying forward as a watch-item
   only (the inner-loop *presentation* OQ for THIS entry is resolved — see
   Discipline notes).

2. **"step-count-predicate" concept page (combinator-miner OQ 2 — watch-item)** —
   the combinator-miner flagged that if a third fixed-count consumer surfaces
   (transient fixed-step time-loop, arnoldi fixed-restart-dimension loop) a
   one-paragraph `concepts/` note "fixed-count bounded iteration is
   `iterate_while_pure` + step-count predicate" might be worth a
   layer-intro-author sideways emission. Today only 2 firm consumers (Chebyshev +
   LBM); not proposed, carried forward as a watch-item. Not a blocker.

3. **No dedicated chebyshev L4>L3 identity theme** (pre-existing OQ, unchanged) —
   the L4>L3 dissolution is the same shape as
   `krylov-step-typed-wrapper-dissolution`; this dispatch did not author a
   standalone `book/src/L4-L3/chebyshev-typed-wrapper-dissolution.md`. With both
   loops now `iterate_while_pure`, the L4>L3 image is cleaner (the loops lower to
   `iterate_while_pure_L3` per `iterate-while.md:193-195`, matching the L3
   `itloop`/`kloop` the cycle-013 L3 entry already renders). A lowering-verifier
   follow-up may want the standalone audit anchor; not a blocker on this entry's
   firm status. Out of this pure-re-anchor dispatch's scope.

4. **`forM_`/`foldM` as desugaring sugar (combinator-miner OQ 3 — deferred,
   unchanged)** — a future cycle could admit `forM_`/`foldM` as *surface sugar
   that desugars to `iterate_while_pure`* via a strawman §-addition (a desugaring
   rule). That is a strawman edit, not an L4 row, and not this dispatch's call.
   Route (i) keeps the calculus closed without it.

5. **`l3-chebyshev-downward-prose-iterate-while-refresh` (cross-layer follow-up;
   added cycle-015 by repairer — NOT a blocker)** — once this re-anchor lands,
   `book/src/L3/chebyshev.md:236-238` carries stale upward-pointing prose: it
   describes the L3 `itloop`/`kloop` tail recursions as "the L3 rendering of the
   L4 `foldM`/`forM_`", but the L4 `chebyshev` entry no longer uses
   `foldM`/`forM_` (both obstructions are now `iterate_while_pure` folds with
   step-count predicates, lowering to `iterate_while_pure_L3` per
   `iterate-while.md:193-195`). This is harmless to the firm flip (it is a
   downward-pointing cross-reference in a *different file* that this pure-re-anchor
   dispatch correctly scoped out — only `L4/chebyshev.md` + `L4/index.md`), but
   the L3 entry's upward reference should be refreshed to name
   `iterate_while_pure`/`iterate_while_pure_L3` instead of `foldM`/`forM_`. Route
   to a follow-up cross-layer touch (lifter on `L3/chebyshev` or a
   cross-layer-cross-cutter sweep). Surgical one-line prose refresh; no L3
   semantics change. Source: cycle-015 critic Issue 2 (out-of-scope observation),
   promoted by repairer.
