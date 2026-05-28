---
agent: harvester
invoked_at: 2026-05-28T143923Z
scope: L3 + L4 operator: chebyshev (identity backfill + monadic wrapper)
status: integrated
integrated_at: 2026-05-28T200000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-013 finalize. L3 chebyshev landed partial-obstruction (as authored); L4 chebyshev landed rough-in (repairer firm→rough-in downgrade — forM_/foldM un-anchored vs the firm iterate-while family). Both SUMMARY-registered. L4 firming condition = OQ chebyshev-l4-wrapper-iteration-vocabulary-reconcile, routed to combinator-miner. Non-adjacent L3↔L1 identity annotated in-line, no L3-L1/L3-L2 directory per cycle-012 convention."
inputs:
  - book/src/L1/chebyshev-smoother.md (cycle-012 firm; the L1 closed-form smoother action)
  - book/src/L2/chebyshev-iteration.md (cycle-012 firm; the L2 three-term recurrence)
  - book/src/spec/slices/chebyshev.md (cycle-001-era slice; §L3 tensor-field form + §L4 monadic form lifted here)
  - book/src/L3/krylov-step.md (identity-lowering backfill template: §Upward/§Downward + in-line non-adjacent identity)
  - book/src/L4/krylov-step.md (typed-wrapper precedent; Haskell :: + TS-record + $$ conventions)
  - book/src/design/l4_calculus.md (strawman §3.7 iterate_while, §3.8 demand-pruning, §2 ownership categories)
  - palace/linalg/chebyshev.cpp:191-220 (4th-kind Mult2; verified via codemap), :261-293 (1st-kind Mult2; verified via codemap)
  - palace/linalg/chebyshev.hpp:14-114 (both class decls + MultTranspose2 alias; verified via codemap)
---

# CYCLE: Formalize chebyshev at L3 and L4

## Summary

Cycle-012 landed `chebyshev-smoother` firm at L1 (the closed-form polynomial
smoother action) and `chebyshev-iteration` firm at L2 (the explicit three-term
recurrence unfolded into base algebra). The L3 and L4 rows are now eligible.
This dispatch formalizes **both**:

- **`book/src/L3/chebyshev.md`** (status `partial-obstruction`) — the
  iteration-rotation form. The per-step **body** lifts cleanly to global
  tensor-field expressions (`apply_linop`, `axpby`/`axpbypcz`, `scal`,
  `elementwise_product` are all whole-tensor by signature); the **loop
  structure** (the inner `k`-recurrence and the outer `pc_it` Richardson sweep)
  is recorded as a witnessed sequential obstruction with a cited
  non-removability reason (Phillips & Fischer 2022 §2: the recurrence form is
  chosen for numerical stability over explicit polynomial expansion). The body
  is **identity-in-form** to the L2 form (and, by transitive composition of the
  adjacent-edge identity themes, to the L1 form) — annotated **in-line** per the
  cycle-012 meta-phase non-adjacent-identity convention; **no `L3-L2/` or
  `L3-L1/` directory** is created by this dispatch.

- **`book/src/L4/chebyshev.md`** (status `firm`) — the graph-evaluation-calculus
  form. The constructed-operator `ChebOp` carries the variant-absorbed scalar
  generator; `apply` is a `Solve`-monad action whose two sequential obstructions
  surface as explicit `forM_` (outer `pc_it`) and `foldM` (inner `k`) binds;
  `initial_guess` is a per-call `Bool` (degenerate-case absorption, not a
  variant axis); `MultTranspose` is the L4-trivial `applyTranspose = apply`
  under operator symmetry.

Both entries are defined in their own layer's vocabulary. The two-kinds decision
follows the cycle-012 L1/L2 lead: 4th-kind and 1st-kind collapse to **one**
operator parameterised by `op.scalars`; the per-step body does not branch on
kind (variant absorption at level (c)).

Landing both rows unblocks the **full reduction of the Phase-1 slice**
`book/src/spec/slices/chebyshev.md` — its §L1/§L2/§L3/§L4 content is now
represented in firm layered entries (L1 cycle-012, L2 cycle-012, L3+L4 this
dispatch). See Open Questions for the slice-reduction follow-up.

## Proposed changes

```edit:book/src/L3/chebyshev.md
<NEW FILE — full content under "Operator content — L3/chebyshev.md" below>
```

```edit:book/src/L4/chebyshev.md
<NEW FILE — full content under "Operator content — L4/chebyshev.md" below>
```

```edit:book/src/L3/index.md
<append one dep-map row to the table at L3/index.md (after the `scal` row, line 28); plus one Working-Notes bullet. Exact insert text under "Index edits" below.>
```

```edit:book/src/L4/index.md
<append one dep-map row to the table at L4/index.md (after the `iterate-while-with-prev` row, line 51); plus add chebyshev to the "Firm at L4" vocabulary-cohort list and a Working-Notes mention. Exact insert text under "Index edits" below.>
```

```edit:book/src/SUMMARY.md
<add chapter entries under the L3 Part (`- [chebyshev](./L3/chebyshev.md)`) and the L4 Part (`- [chebyshev](./L4/chebyshev.md)`). Integrator wires the exact positions.>
```

---

## Operator content — L3/chebyshev.md

```markdown
---
layer: L3
operator: chebyshev
firmness: partial-obstruction
lowers_to:
  - book/src/L2/chebyshev-iteration.md (body identity-in-form; surface adjustments consolidate `(r, d, y, scalar_state)` carry into the L2 sweep; no L3-L2 theme file — in-line annotation)
lifts_from:
  - book/src/L4/chebyshev.md (typed-wrapper / Solve-monad dissolution; identity-in-form on the kernel body, substantive at the wrapper)
variant_axes:
  - polynomial-kind (Chebyshev-4th / Chebyshev-1st)
  - element-type (real / complex)
---

# chebyshev

Value-threaded fixed-degree polynomial-smoother step at L3 — the
**iteration-rotation** rendering of the Chebyshev smoother. The per-inner-step
**body** is a global tensor-field update `(r, d, y) -> (r', d', y')`; the
surrounding loop structure (the inner `k`-recurrence of degree `order` and the
outer `pc_it` Richardson sweep) is a witnessed **sequential obstruction** that
does **not** lift to a global tensor-field operation. Companion to L4
[`chebyshev`](../L4/chebyshev.md) (the `Solve`-monad wrapper around the same
body) and L2 [`chebyshev-iteration`](../L2/chebyshev-iteration.md) (the same
body as a primitive composition with the iteration view erased).

## Context

L3 is the iteration-rotation layer: where the L2 algebra admits a global
tensor-field form, L3 captures it; where no global form exists, the
**obstruction** is a first-class output (per
[`sequential-obstruction`](../concepts/sequential-obstruction.md)). `chebyshev`
at L3 is the canonical **partial-obstruction** case: the body lifts, the loop
does not.

Unlike L3 [`krylov-step`](./krylov-step.md), `chebyshev` is **not** a Krylov
method — it is **inner-product-free** (no `dot` / `nrm2` reduction appears in
the body; the coefficients are closed forms of the step index `k` and the
spectral bounds, computed without inspecting the iterate) and has **no
convergence test** (it applies a fixed-degree polynomial `pc_it` times; the loop
bounds are static, not predicate-driven). It is therefore defined here as its
own L3 operator in L3 vocabulary, not as a specialisation of `krylov-step`. The
two share the L3 whole-tensor field-operation vocabulary (`apply_linop`,
`axpby`, `axpbypcz`, `scal`, [`elementwise-product`](../concepts/elementwise-product.md))
but differ in their iteration structure: `krylov-step`'s outer loop is a
predicate-driven `iterate_while` fold; `chebyshev`'s loops are bounded
`forM_`/`foldM` ranges (rendered at L3 as tail recursions over static index
ranges).

The relationship to the adjacent layers:

- **Upward** to L4: [`chebyshev`](../L4/chebyshev.md) is the typed
  `Solve`-monad wrapper. The wrapper-dissolution (the `Solve (ChebSim E)`
  monad → explicit `(x, y)`-state threading; the `ChebOp` closure → positional
  operator-parameters value; the `Read`/`ReadWrite` capability typing on
  `ChebSim` → a documented mutation discipline; the `forM_`/`foldM` binds →
  tail recursions over static ranges) is **substantive at the wrapper**; the
  kernel body's primitive sequence is **value-thread-isomorphic** between the
  L4 form and this L3 form. The L4 `do`-block dissolves to a `let`-chain; the
  L4 `modifyY (\y -> y .+. dN)` dissolves to the explicit `let y' = y + dN`
  binding. No `book/src/L4-L3/` theme file is authored by this dispatch — the
  dissolution is value-thread-isomorphic on the body and the wrapper rewrite is
  the same shape the krylov-step typed-wrapper-dissolution theme catalogs
  (`book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`); a thin L4>L3
  chebyshev identity-theme is an Open Question follow-up if the
  lowering-verifier wants a dedicated audit anchor.
- **Downward** to L2: [`chebyshev-iteration`](../L2/chebyshev-iteration.md) is
  the same body as a base-algebra primitive composition with the iteration view
  erased (the outer driver referenced by role only). The L3>L2 rotation on the
  **body** is **identity-in-form**: the L3 tensor-field updates map line-for-line
  to the L2 `sweep` body's `axpy`/`axpby`/`scal`/`elementwise_product` calls
  (the L2 entry's §Semantics `sweep` is exactly this body with the field-algebra
  operators spelled as their L1-primitive names). The single surface adjustment
  is that L3 carries `(r, d, y, scalar_state)` as a positional recurrence tuple
  threaded by the explicit tail recursion, whereas L2 consolidates the same
  threading into its `for k in 1 .. order-1` loop with `op.scalars(k, st)`
  state. This is information-preserving. **No `book/src/L3-L2/` theme file is
  created** — the body identity-in-form annotation lives in-line here per the
  cycle-012 meta-phase non-adjacent-identity convention (precedent:
  `book/src/L3/krylov-step.md` §Downward).

**Non-adjacent identity (in-line, no directory).** Because the L3>L2 body
rotation is identity-in-form **and** the L2>L1 body rotation is identity-in-form
(the L2 [`chebyshev-iteration`](../L2/chebyshev-iteration.md) Law 1 establishes
the recurrence *is* the matrix-free evaluation of the L1 closed-form action
`p_order(D⁻¹ A)`, modulo floating-point reassociation; the L1↔L2 edge is a
resolution change, not a structural rewrite), the composition
(L3>L2 identity ∘ L2>L1 identity ⟹ L3>L1 identity) makes this L3 body
value-thread-isomorphic to the L1 [`chebyshev-smoother`](../L1/chebyshev-smoother.md)
action as well, at the body level. That non-adjacent relationship is the
**transitive consequence of the two adjacent-edge identities** and is annotated
**in-line** here (and in the dep-map), citing the existing adjacent entries; **no
`book/src/L3-L1/` directory is created** (per the cycle-012 meta-phase decision
`l3-l1-inline-identity-rotation-convention`, lowering directories are
per-adjacent-edge only). Note the caveat below: the L1↔L2 identity is on the
**body**; it does not erase the L3 loop-structure obstruction, which is a
property of the surrounding `forM_`/`foldM` ranges, not of the body.

A cross-cutting prose treatment lives at
[`concepts/chebyshev-iteration`](../concepts/chebyshev-iteration.md) (minimax
background, inner-product-free property, distinction from CG). This L3 entry is
the firm operator definition of the iteration-rotation form; the concept page is
the narrative.

## Signature

```text
chebyshev :: (op, x, y, initial_guess) -> y'
```

Shape contract (positional values; L3 has no `readonly` annotation and no
monadic effect):

- **`op`** — operator-parameters value. Closure-captured by the body via the
  convention that `op` is a positional argument never present in the return
  position. The body reads:
  - `op.A : LinearOperator[N, N]` — the captured SPD operator (residual
    `apply_linop op.A y` and direction-image `apply_linop op.A d`).
  - `op.dinv : Tensor[N]` — the inverse diagonal `1/diag(A)` (the `D⁻¹` action
    `elementwise_product op.dinv r`); real-valued even for complex `A`.
  - `op.order : Int` — the polynomial degree (`> 0`); the inner `k`-loop bound.
  - `op.pc_it : Int` — the outer Richardson-sweep count.
  - `op.scalars : (k, st) -> ((α₀ | (sd, sr)), st')` — the variant-bound scalar
    generator (4th-kind: stateless closed form in `(k, λ_max)`; 1st-kind:
    `ρ`-threaded recurrence). Variant absorption is a **documented invariant at
    L3** — the body does not branch on polynomial-kind; the dispatch is a single
    inlined closure call (`op.scalars`).
  - `op.scalar_init` — the initial scalar-recurrence state (`()` for 4th-kind;
    `{ ρ_prev = δ/θ }` for 1st-kind).
- **`x`** — `Tensor[N]` — the right-hand side (residual to smooth). Read-only.
- **`y`** — `Tensor[N]` — the input accumulator / current iterate. Read.
- **`initial_guess`** — `Bool` — whether `y` carries a meaningful initial guess.
  When `false`, the first sweep uses `r = x` with `y := 0` (degenerate-case
  absorption — the `y = 0` instance of the uniform `r = x − A·y`). A per-call
  argument, not a field of `op`.
- **result `y'`** — `Tensor[N]` — the post-smoothing accumulator
  (value-threaded; no aliasing with the input `y`). Same length axis `N`.

There is **no `outputs` record** in the signature: `chebyshev` is
inner-product-free and convergence-test-free, so no residual-norm / breakdown
readout is produced per step (contrast L3 [`krylov-step`](./krylov-step.md),
whose `(K', s', outputs)` carries a demand-prunable readout). The smoother's
only product is the accumulator `y'`.

L4 wrapper machinery absent at L3 (structural for the layer):

1. **No `Solve` monad.** The L4 `apply :: ChebOp E S -> Bool -> Solve (ChebSim
   E) ()` action dissolves into the explicit value-threaded `(op, x, y,
   initial_guess) -> y'` form. The L4 `modifyY (\y -> y .+. dN)` becomes the
   explicit `let y' = y + dN` binding; the L4 `readY`/`writeY` capability
   accessors become plain reads/returns of the positional `y`.
2. **No `Read`/`ReadWrite` capability typing.** The L4 `ChebSim E = { x:
   Read<Field E>, y: ReadWrite<Field E> }` mutation discipline (only `y` is
   written; `x` is read-only) demotes at L3 to a documented invariant verified
   by reading the body (`x` flows in, is never returned; `y` flows in and out).
3. **No closure-typed variant absorption.** The L4 distinct closure *types*
   (`ChebOp<E, Unit>` 4th-kind vs `ChebOp<E, { rho_prev: E }>` 1st-kind) collapse
   to one positional `op` value whose `op.scalars` / `op.scalar_init` carry the
   variant; the body's textual shape does not branch on kind.

## Semantics

`chebyshev` at L3 applies `op.pc_it` Richardson sweeps of a degree-`op.order`
matrix polynomial of `D⁻¹ A`, each sweep accumulating the polynomial action on
the current residual into `y`. The body of one sweep is value-threaded over the
recurrence carry `(r, d, y, st)`; the inner `k`-recurrence and the outer
`pc_it` loop are sequential (see Iteration-rotation marker).

### Tensor-field body (one inner step `k`)

Fix the inner-step body that runs once for each `k ∈ {1, …, order−1}`. With the
SPD operator `op.A`, the diagonal-inverse field `op.dinv`, and the three carried
fields `r, d, y : Tensor[N]`, the body is the simultaneous global update

$$
\begin{aligned}
y_{k+1} &= y_k + d_k, \\
r_{k+1} &= r_k - A\, d_k, \\
d_{k+1} &= \sigma_k^{\mathrm{d}}\, d_k + \sigma_k^{\mathrm{r}}\, \big(\text{dinv} \odot r_{k+1}\big),
\end{aligned}
$$

with scalar coefficients $(\sigma_k^{\mathrm{d}}, \sigma_k^{\mathrm{r}}) =
(\text{sd}_k, \text{sr}_k)$ from `op.scalars(k, st)`. Each line is a global
tensor-field expression built from L3-native whole-tensor primitives — `axpy`
(`y += d`), `apply_linop` + `axpby` (`r − A·d`), and the `axpbypcz`-shaped
direction update `d = sd·d + sr·(dinv ⊙ r)` realised as
`elementwise_product` then `axpby`. There is no per-element dependence *within* a
line; the body **lifts cleanly** to global field arithmetic.

The L2 element-fused kernels (`ApplyOrder0`, `ApplyOrderK`,
`palace/linalg/chebyshev.cpp:69-78, :114-123`) are a transparent performance
trick below L3's level of abstraction; the L3 body is the unfused tensor-field
composition (per [`chebyshev-iteration`](../L2/chebyshev-iteration.md) Law 3).

### Initial direction and final accumulate

The initial direction (`k = 0`)

$$d_0 = \alpha_0\, \big(\text{dinv} \odot r_0\big), \qquad r_0 = x - A\,y \;\;\text{(or } x \text{ with } y := 0 \text{ when } \texttt{initial\_guess} = \texttt{false on the first sweep})$$

is a single global field expression (`scal(α₀, elementwise_product(op.dinv,
r₀))`), and the final accumulate $y_{\text{order}} = y_{\text{order}-1} +
d_{\text{order}-1}$ is global (`axpy(1, d, y)`). The `initial_guess = false`
branch is the degenerate-case absorption (the `y = 0` instance of `r = x −
A·y`); it fires at most once per call (only on the first sweep), and is a
control-flow-boundary instance of
[`derived-view-hoisting`](../concepts/derived-view-hoisting.md).

### Value-threaded form (L3 rendering)

```text
chebyshev op x y initial_guess =
  let sweep s_first y =                                   -- one Richardson sweep
        let r0   = if s_first && not initial_guess
                     then x                               -- with y := 0 below
                     else axpby 1 x (-1) (apply_linop op.A y)   -- r = x − A·y
        let y0   = if s_first && not initial_guess then zero else y
        let (c0, st0) = op.scalars 0 op.scalar_init
        let d0   = scal c0.α₀ (elementwise_product op.dinv r0)  -- d = α₀·(dinv ⊙ r)
        let (rN, dN, _stN, yN) =
              kloop 1 (r0, d0, st0, y0)                   -- sequential inner recurrence
        in axpy 1 dN yN                                   -- final accumulate y += d
      kloop k (r, d, st, y) =                             -- tail recursion over k = 1 .. order-1
        if k >= op.order then (r, d, st, y)
        else let y'        = axpy 1 d y                   -- y += d
                 r'        = axpby 1 r (-1) (apply_linop op.A d)  -- r −= A·d
                 (c, st')  = op.scalars k st
                 t         = elementwise_product op.dinv r'
                 d'        = axpby c.sd d c.sr t          -- d = sd·d + sr·t
             in kloop (k+1) (r', d', st', y')
  in itloop 1 y                                           -- tail recursion over it = 1 .. pc_it
  where itloop it y = if it > op.pc_it then y
                      else itloop (it+1) (sweep (it == 1) y)
```

The two `if k >= op.order` / `if it > op.pc_it` tail recursions are the L3
rendering of the L4 `foldM`/`forM_` over static index ranges — the iteration
view that L3 makes load-bearing. The body inside `kloop` is the tensor-field
update above; every binding is a whole-tensor field operation.

The body is **stateless across calls** — `op` is closure-captured but never
mutated; `x` is read but never returned; `y` flows in, `y'` flows out as a fresh
value. The recurrence carry `(r, d, st, y)` is threaded positionally through the
inner tail recursion.

### Iteration-rotation marker

L3 is the iteration-rotation layer. `chebyshev`'s iteration view is the
relationship between successive recurrence carries `(r_k, d_k, y_k) -> (r_{k+1},
d_{k+1}, y_{k+1})` (inner) and successive sweep iterates `y -> sweep(y)` (outer).

- **The body lifts.** Each inner-step line is a global tensor-field expression
  (whole-tensor by signature shape). The initial direction and final accumulate
  lift. The 4th/1st-kind variant branch lifts trivially (the scalars are pure
  functions of `k`, and of `ρ_{k-1}` for 1st-kind — itself a length-1 scalar
  recurrence, `O(1)` per step, not part of the tensor-field state).
- **The inner `k`-loop does not lift** — `d_{k+1}` depends on `r_{k+1}`, which
  depends on `d_k`: the three-term recurrence is genuinely sequential in `k`. A
  *symbolic* global form `y_out = y_in + p_order(D⁻¹ A)·r₀` exists, but
  evaluating the polynomial matrix-free **re-derives** the same recurrence
  (Horner/Clenshaw); replacing it with an explicit monomial sum
  `Σ c_j (D⁻¹ A)^{j+1} r₀` is **numerically unstable** for the operative `order`
  range (Phillips & Fischer 2022 §2 motivates the recurrence form for exactly
  this reason). The sequentiality is **fundamental to the smoother's numerical
  behaviour**, not an implementation artifact. Recorded as a
  [`sequential-obstruction`](../concepts/sequential-obstruction.md).
- **The outer `pc_it`-loop does not lift** — each Richardson sweep consumes the
  previous sweep's accumulated `y`. The closed-form global statement
  `y_out = (I − p_order(D⁻¹ A)(I − A·))^{pc_it} y_in + (terms in x)` exists but
  evaluating it requires iterating the sweep; standard outer-iteration
  sequentiality.

This is the canonical **partial obstruction**: body lifts, loop does not (per
[`tensor-field-lift`](../concepts/tensor-field-lift.md)). It is **identity-in-form
to the L2 body** precisely because all sequentiality is in the surrounding loop
structure, not in the body — and the L2 entry records the same sequentiality as
non-laws (Step-reordering / `pc_it`-sweep non-commutativity).

## Algebraic laws

The laws below hold; absences are deliberate. They are the L2 laws restated in
L3 vocabulary (the body is identity-in-form), with the obstruction structure
made explicit at L3.

1. **Affine-in-(x, y) per sweep.** One sweep is the affine map `y ↦ y +
   p_order(D⁻¹ A)·(x − A·y)` = `(I − M A)·y + M·x` where `M = p_order(D⁻¹ A)`.
   Affine in `y`, affine in `x`; the polynomial action `M·(·)` is linear. This
   is the structural law underwriting the linear-preconditioner use (law 2).

2. **Linear preconditioner form (zero initial guess, single sweep).** With
   `initial_guess = false`, the first sweep sets `y = 0`, `r = x`, so the output
   is `y' = p_order(D⁻¹ A)·x` — a *linear* function of `x` (`apply_linop`-shaped).
   This is the form consumed when the smoother is the `B` preconditioner inside
   an outer Krylov method or a multigrid V-cycle correction.

3. **Transpose identity under symmetry.** For SPD `A`,
   `chebyshev_transpose(op, x, y, ig) = chebyshev(op, x, y, ig)`. Witnessed by
   the L0 `MultTranspose2 → Mult2` alias (`palace/linalg/chebyshev.hpp:72-75`).
   The conjugate-`dinv` transpose path in the complex source is dead code under
   symmetric wiring (see Variant axes / Open questions).

4. **Sweep idempotence on the zero-residual fixed point.** If `A·y = x` (zero
   residual), then `r = x − A·y = 0`, every direction `d = 0`, and `y' = y`. The
   exact solution is a fixed point. (Mathematical identity; in IEEE-754 the
   residual is computed, not assumed zero.)

5. **Variant-invariant body sequence.** The tensor-field body (the three-line
   inner update plus initial-direction / final-accumulate) is **identical**
   across 4th-kind and 1st-kind — only `op.scalars` branches. This is the (c)
   primitive-sequence axis of
   [`variant-absorption`](../concepts/variant-absorption.md): both polynomial
   families admit the same recurrence shape; 4th-kind via stateless closed form,
   1st-kind via the `ρ`-threaded scalar recurrence. The body does not branch on
   kind.

6. **Body identity-in-form across the L3↔L2↔L1 chain.** The L3 tensor-field
   body maps line-for-line to the L2 [`chebyshev-iteration`](../L2/chebyshev-iteration.md)
   `sweep` body and, transitively (L3>L2 identity ∘ L2>L1 identity), is
   value-thread-isomorphic to the L1 [`chebyshev-smoother`](../L1/chebyshev-smoother.md)
   closed-form action at the body level. **This is a body-level law, not a
   loop-level one** — the L3 loop-structure obstruction (laws below that do not
   hold) is not erased by the body identity.

Laws that explicitly **do not** hold:

- **Inner-loop lift to a single tensor-field op.** The map `(r_k, d_k, y_k) ↦
  (r_{k+1}, d_{k+1}, y_{k+1})` is genuinely sequential in `k`; the degree-`order`
  recurrence does not lift to one whole-tensor operation. **Sequential
  obstruction** — see Iteration-rotation marker.
- **Outer-loop lift to a single tensor-field op.** The `pc_it`-sweep composition
  does not lift; each sweep consumes the previous sweep's `y`. Standard
  outer-iteration sequentiality.
- **Step-reordering / associativity of the `k`-recurrence.** No reordering of the
  inner loop preserves the value (`d_{k+1}` reads `r_{k+1}` reads `d_k`).
  Inherited from L2.
- **Polynomial-expansion equivalence.** Replacing the recurrence with an explicit
  monomial sum is numerically unstable for the operative `order` range; the
  recurrence and the monomial sum are the same polynomial mathematically but
  **not** the same algorithm. The sequentiality is load-bearing (Phillips &
  Fischer 2022 §2). Inherited from L2.
- **Sweep idempotence in general.** Two calls compose into `2·pc_it` sweeps of
  error reduction, not `pc_it` — the smoother is a contraction (on the spectral
  window), not a projection. Inherited from L1.
- **Bit-determinism across operator representations / fusion choices.** A
  matrix-free vs assembled `A`, or a fused-FMA vs unfused direction update, give
  bit-different trajectories. Load-bearing per CLAUDE.md §"Optimization tricks".
  Inherited from L1/L2.
- **Linearity in `y` across the full `pc_it`-sweep action.** The full action with
  a non-zero initial guess is *affine*, not linear, in `y` (law 1's `M·x` offset).
  Only the `initial_guess = false`, single-input form (law 2) is linear in `x`.

## Dependencies

**Same-layer (L3)** — the body references the L3-native whole-tensor primitives
by their L1 names (L3-native by signature shape, each operating on whole tensors
with no element loop exposed):

- [`apply_linop`](./apply_linop.md) — the operator action `A·y` (residual) and
  `A·d` (direction-image).
- [`axpy`](./axpy.md), [`axpby`](./axpby.md) — residual / accumulate / direction
  updates.
- [`scal`](./scal.md) — initial-direction scaling.
- [`axpbypcz`](./axpbypcz.md) — the direction update `d = sd·d + sr·t` is in the
  linear-update family (here realised as `elementwise_product` then `axpby`; the
  three-input `axpbypcz` shape is the unfused canonical form).

`chebyshev` does **not** depend on the L3 reductions [`dot`](./dot.md) /
[`nrm2`](./nrm2.md) — it is inner-product-free. This is the structural
distinction from L3 [`krylov-step`](./krylov-step.md).

**Cross-cutting concepts:**

- [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the
  classification for both the inner `k`-loop and the outer `pc_it`-loop.
- [`tensor-field-lift`](../concepts/tensor-field-lift.md) — the
  body-lifts-but-loop-doesn't canonical partial case.
- [`elementwise-product`](../concepts/elementwise-product.md) — the `D⁻¹` action
  `dinv ⊙ r`.
- [`variant-absorption`](../concepts/variant-absorption.md) — the (c)
  primitive-sequence axis (law 5); at L3 a documented invariant (no `readonly`
  typing).
- [`derived-view-hoisting`](../concepts/derived-view-hoisting.md) — the
  control-flow-boundary instance for the `initial_guess` branch.
- [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md) — the
  initial-direction / final-accumulate loop-boundary unrolling.
- [`constructed-operators`](../concepts/constructed-operators.md) — the
  setup-bound `op` closure absorbing the variant axis.
- [`chebyshev-iteration`](../concepts/chebyshev-iteration.md) — narrative.

**Adjacent-layer siblings:**

- L2: [`chebyshev-iteration`](../L2/chebyshev-iteration.md) — the
  primitive-composition form this entry's body is identity-in-form to.
- L1: [`chebyshev-smoother`](../L1/chebyshev-smoother.md) — the closed-form
  action the body is value-thread-isomorphic to (transitively; in-line
  annotation, no `L3-L1/` directory).
- L4: [`chebyshev`](../L4/chebyshev.md) — the `Solve`-monad wrapper this entry
  lifts from.

## Variant axes

Two axes, both absorbed at construction (per
[`variant-absorption`](../concepts/variant-absorption.md)); neither appears in
the per-step body's positional signature:

1. **polynomial-kind** (`Chebyshev-4th | Chebyshev-1st`) — absorbed at level (c)
   into `op.scalars` / `op.scalar_init`. The L0 source splits this into two
   classes (`ChebyshevSmoother` 4th-kind, `palace/linalg/chebyshev.hpp:23`;
   `ChebyshevSmoother1stKind`, `:86`); they differ only in the scalar data
   captured at setup and the closed-form coefficient recurrence. At L3 they
   collapse to one operator; the body does not branch on kind (law 5).
2. **element-type** (`real | complex`) — the body is identical; only the
   underlying `apply_linop`, `axpby`, `scal`, `elementwise_product` dispatch on
   element type. `dinv` is real-valued even for complex `A`
   (`palace/linalg/chebyshev.hpp:37`). The complex transpose path uses the
   conjugate of `dinv` but is dead code under symmetric wiring (Open questions).

The **degree** (`op.order`) and **sweep-count** (`op.pc_it`) are construction
parameters carried in `op`, not variant axes — they parameterise one operator,
they do not select among operators. The **spectral-bound-estimation method**
(power iteration vs SLEPc) is a setup-side concern absorbed into the opaque
spectrum-estimate sub-action; it does not surface at the smoother-action
signature. There is **no first-iteration-unrolled-vs-branch-in-body axis** as a
*variant* (contrast `krylov-step` axis 4): the `initial_guess` branch is a
degenerate-case absorption controlled by a `Bool` argument, and the
initial-direction / final-accumulate boundary is a fixed loop-unrolling, not a
selectable form.

## Status

`partial-obstruction` — the per-inner-step body lifts cleanly to a global
tensor-field expression (every line is whole-tensor by signature shape; verified
against the L2 `sweep` body and the L0 `Mult2` bodies); the inner `k`-recurrence
and the outer `pc_it` Richardson sweep are **witnessed sequential obstructions**
with a cited non-removability reason (Phillips & Fischer 2022 §2: recurrence
form chosen for numerical stability). This is the canonical partial-obstruction
case (body lifts, loop does not), distinct from the firm-body / non-lifting-fold
shape of L3 [`krylov-step`](./krylov-step.md) in that `chebyshev`'s loops are
bounded static ranges (no convergence predicate, no inner-product reduction).
The body's algebraic laws are syntactic identities on the source (inherited from
the cycle-012 firm L1/L2 entries); the obstruction structure is explicit and
cited. **Caveat (not a status reduction)**: no dedicated unit test under
`reference/palace/test/unit/` — behaviour is exercised only through multigrid
integration (`gmg.cpp`, `distrelaxation.cpp`); same justification as the firm
L1/L2 entries (every body law is a syntactic identity on fully-specified C++
source). The `partial-obstruction` status reflects the **loop structure**, not
the body — it is the honest L3 verdict for a fixed-degree polynomial smoother and
does not impeach the firm L1/L2 rows.

## L3 vs L2 distinction

- **L3**: value-threaded positional form `(op, x, y, initial_guess) -> y'`. The
  iteration view is load-bearing — the inner `k`-recurrence and outer
  `pc_it`-sweep are rendered as explicit tail recursions over static ranges, and
  both sequential obstructions are named explicitly. The body lifts; the loops do
  not.
- **L2**: primitive-composition form `(op: ChebOp[N], x, y, initial_guess) -> y'`
  with the iteration view erased (`sweep` iterated `op.pc_it` times; the
  `for k in 1 .. order-1` loop referenced as a composition driver). The HPC
  element-fused kernels (`ApplyOrder0`, `ApplyOrderK`) de-fused into base
  composition.

The L3>L2 hop erases the explicit iteration view (the tail recursions collapse
to L2's loop-as-composition-driver) and leaves the body identity-in-form. No
`L3-L2/` theme file — the identity-in-form annotation lives in-line here (per the
cycle-012 meta-phase non-adjacent-identity convention; precedent
`book/src/L3/krylov-step.md`).

## L3 vs L4 distinction

- **L4**: typed `Solve`-monad wrapper. The `ChebOp<E, S>` closure carries the
  variant-typed scalar generator; `apply :: ChebOp E S -> Bool -> Solve (ChebSim
  E) ()` threads `(x, y)` through the `Solve (ChebSim E)` monad with `Read`/
  `ReadWrite` capability typing; the two sequential obstructions surface as
  `forM_` (outer) and `foldM` (inner) binds.
- **L3**: value-threaded positional form. The `Solve` monad has dissolved (`(x,
  y)` threaded explicitly; `modifyY` → explicit `let y' = ...`); the capability
  typing has demoted to a documented invariant; the closure-typed variant
  absorption has collapsed to one positional `op`; the `forM_`/`foldM` binds are
  tail recursions over static ranges. The kernel body's primitive sequence is
  value-thread-isomorphic to L4; only the wrapper differs.

## Evidence

- `palace/linalg/chebyshev.cpp:191-220` — 4th-kind `Mult2` body (verified via
  codemap): the `pc_it` outer sweep; `r = x − A·y` (via `ApplyOp(*A, y, r);
  AXPBY(1, x, -1, r)`) or `r = x; y = 0` on first sweep without initial guess;
  `ApplyOrder0(4/(3·λ_max), dinv, r, d)`; the `k`-loop with `y += d`,
  `ApplyOp(*A, d, r, -1.0)`, `sd = (2k−1)/(2k+3)`, `sr = (8k+4)/((2k+3)·λ_max)`,
  `ApplyOrderK(sd, sr, dinv, r, d)`; final `y += d`. The body whose three-line
  inner update this L3 entry lifts to tensor-field form.
- `palace/linalg/chebyshev.cpp:261-293` — 1st-kind `Mult2` body (verified via
  codemap): identical sweep scaffold; `ApplyOrder0(1/theta, dinv, r, d)`;
  `rhop = delta/theta`; the `k`-loop with `rho = 1/(2·theta/delta − rhop)`,
  `sd = rho·rhop`, `sr = 2·rho/delta`, `rhop = rho`; final `y += d`. The
  variant-invariant body sequence (law 5) is witnessed by the identical sweep
  scaffold across the two bodies.
- `palace/linalg/chebyshev.hpp:14-23` — `ChebyshevSmoother` (4th-kind) class doc
  + decl (verified via codemap): "Matrix-free diagonally-scaled Chebyshev
  smoothing … 4th-kind … Phillips and Fischer, arXiv:2210.03179v1 (2022)."
- `palace/linalg/chebyshev.hpp:72-75` — `MultTranspose2(x, y, r) { Mult2(x, y,
  r); }` (verified via codemap) — the symmetry alias witnessing law 3.
- `palace/linalg/chebyshev.hpp:80-114` — `ChebyshevSmoother1stKind` class doc +
  decl (verified via codemap): "standard 1st-kind Chebyshev polynomials … Adams
  et al., JCP (2003)"; `double theta, delta, sf_max, sf_min;`.
- `palace/linalg/chebyshev.hpp:37` — `VecType dinv; // … real-valued for now`
  (verified via codemap) — the element-type variant-axis note.
- `book/src/L2/chebyshev-iteration.md` (cycle-012 firm) — the L2
  primitive-composition form this entry's body is identity-in-form to; §Semantics
  `sweep` is exactly this body with the field-algebra operators spelled as their
  L1-primitive names. Laws 1/2/3 (L2) are the body-equivalence and fusion-
  transparency anchors; the L2 non-laws (step-reordering, `pc_it`-non-commutativity)
  are the L3 loop-structure obstructions.
- `book/src/L1/chebyshev-smoother.md` (cycle-012 firm) — the L1 closed-form
  action the body is value-thread-isomorphic to (transitively, in-line).
- `book/src/L3/krylov-step.md` (cycle-010 firm) — the template for the
  identity-lowering backfill (§Upward/§Downward in-line annotation) and the
  contrast operator (Krylov, predicate-driven loop, inner-product-bearing) vs
  this fixed-degree, inner-product-free, static-range smoother.
- `book/src/spec/slices/chebyshev.md:229-285` — the cycle-001-era §L3
  "tensor-field form (partial obstruction)" this entry promotes (the tensor-field
  body, the `k` and `pc_it` sequential obstructions, the what-lifts-vs-what-does-not
  table).
- `book/src/concepts/chebyshev-iteration.md` — narrative.
```

---

## Operator content — L4/chebyshev.md

```markdown
# chebyshev

Typed-wrapper fixed-degree polynomial-smoother operator at L4 — the Chebyshev
smoother as a constructed `ChebOp` whose `apply` is a `Solve`-monad action over
a capability-typed sim-state. The thin state-bearing wrapper around the pure
fixed-degree polynomial action; the two sequential obstructions (the outer
`pc_it` Richardson sweep, the inner `k`-recurrence) surface as explicit
`forM_` / `foldM` binds — they do not collapse. Companion to L3
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

`chebyshev` at L4 is **not** an instance of [`krylov-step`](./krylov-step.md).
The Krylov step kernel is folded by a predicate-driven `iterate_while` over a
trajectory of demand-prunable per-step extras; the Chebyshev smoother has **no
convergence predicate** (the loops are bounded static ranges `[1 .. pc_it]` and
`[1 .. order-1]`) and is **inner-product-free** (no `dot` / `nrm2` reduction; no
residual-norm trajectory). It is therefore the canonical L4 example of a
**fixed-degree** operator whose sequential obstructions are `forM_` (bounded
outer iteration) and `foldM` (bounded inner recurrence), not `iterate_while`.

The relationship to the lower layers:

- **L4 > L3** (substantive at the wrapper; identity-in-form on the body): the
  `Solve (ChebSim E)` monad dissolves to explicit `(x, y)`-state threading; the
  `ChebOp<E, S>` closure dissolves to a positional operator-parameters value;
  the `Read`/`ReadWrite` capability typing on `ChebSim` demotes to a documented
  mutation discipline; the `forM_`/`foldM` binds dissolve to tail recursions
  over static ranges. The kernel body's primitive sequence is value-thread-
  isomorphic to L3 [`chebyshev`](../L3/chebyshev.md). This is the same
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
ChebOp :: { A: LinOp[E], dinv: Tensor[E, N], order: Int, pc_it: Int
          , scalarInit: S
          , scalars: (Int, S) -> { α₀?: E, sd?: E, sr?: E, st: S } }

ChebSim :: { x: Read[Tensor[E, N]], y: ReadWrite[Tensor[E, N]] }

setup  :: LinOp[E] -> SetupParams -> Variant -> Solve s (ChebOp E S)
apply  :: ChebOp E S -> Bool -> Solve (ChebSim E) ()
```

Shape contract (bunsen-style; named records and axes):

- `ChebOp E S` — operator-internal configuration, captured once at setup;
  `readonly` per [`state-stratification`](../concepts/state-stratification.md).
  `S` is the scalar-recurrence state type, **statically determined by variant**:
  `Unit` for 4th-kind, `{ rho_prev: E }` for 1st-kind. The two variants are
  **distinct closure types** (`ChebOp E Unit` vs `ChebOp E { rho_prev: E }`),
  not a single union — there is no runtime variant tag at apply-time, only a
  closure dispatch through `scalars`. Fields:
  - `A: LinOp[E]` — the captured SPD operator (residual + direction-image).
  - `dinv: Tensor[E, N]` — `1/diag(A)` (the `D⁻¹` action); real-valued even for
    complex `A`.
  - `order: Int` — polynomial degree (`> 0`); the inner `foldM` range bound.
  - `pc_it: Int` — Richardson-sweep count; the outer `forM_` range bound.
  - `scalarInit: S` — the initial scalar-recurrence state at `k = 0`.
  - `scalars: (k: Int, st: S) -> { α₀?, sd?, sr?, st: S }` — the pure
    scalar-recurrence step (4th-kind: stateless closed form; 1st-kind:
    `ρ`-threaded). The kernel does not branch on variant — the variant axis is
    absorbed into the closure type per [`variant-absorption`](../concepts/variant-absorption.md)
    level (c).
- `ChebSim E` — the capability-typed sim-state record threaded by the `Solve`
  monad: `x: Read[Tensor[E, N]]` (the rhs; read-only) and `y: ReadWrite[Tensor[E,
  N]]` (the accumulator; the only field written). The `Read`/`ReadWrite` split
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
`D⁻¹ A`. The two sequential obstructions surface as explicit `forM_` (outer) and
`foldM` (inner) binds in the `Solve` monad; each step is a pure tensor-field
expression on the field algebra; the monad threads the sim-state accumulator `y`
and the fold threads the ephemeral `(r, d)` plus the scalar-state `st`.

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

- **Obstruction collapse.** The `forM_`/`foldM` binds do **not** reduce to a
  single tensor-field operation under the calculus's reduction rules — the inner
  `k`-recurrence and outer `pc_it`-sweep are genuinely sequential (inherited from
  the L3 partial-obstruction verdict). The `foldM` is not a `reduce`; the `forM_`
  is not a parallel map.
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
  scalar-recurrence stratum `S` threaded by `foldM`) is the worked example this
  entry instantiates.
- [`solve-monad`](../concepts/solve-monad.md) — the `Solve (ChebSim E)` monad
  threading sim-state through `forM_` and `foldM`; the capability-typed `Read`/
  `ReadWrite` accessors.
- [`constructed-operators`](../concepts/constructed-operators.md) — the `ChebOp`
  closure absorbing the variant axis at level (c).
- [`variant-absorption`](../concepts/variant-absorption.md) — the level-(c)
  absorption making the polynomial-kind axis structural via the distinct closure
  types `ChebOp E Unit` / `ChebOp E { rho_prev: E }`.
- [`derived-view-hoisting`](../concepts/derived-view-hoisting.md) — the
  control-flow-boundary instance for the `initial_guess` branch.
- [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the
  classification surfacing as `forM_` (outer) and `foldM` (inner) binds.
- [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md) — the
  initial-direction / final-accumulate loop-boundary unrolling.
- [`elementwise-product`](../concepts/elementwise-product.md) — the `D⁻¹` action
  `dinv ⊙ r` (`.*.`).
- [`chebyshev-iteration`](../concepts/chebyshev-iteration.md) — narrative.

Lower-layer rows (the evidence base):

- L2 [`chebyshev-iteration`](../L2/chebyshev-iteration.md) (cycle-012 firm) — the
  primitive composition this L4 wrapper's body is value-thread-isomorphic to;
  carries the L1 primitive-call enumeration, the fusion-transparency classification,
  the scalar recurrences, and the L0 source ranges.
- L1 [`chebyshev-smoother`](../L1/chebyshev-smoother.md) (cycle-012 firm) — the
  closed-form smoother action; carries the constructed-operator-gate framing.

Strawman reference: [`../design/l4_calculus.md`](../design/l4_calculus.md) §2
(ownership categories), §3.7 (the `iterate_while` family, contrasted here with
the bounded `forM_`/`foldM`), §3.8 (demand-pruning, noted as not-applicable —
no trajectory).

## Lowers to

L4 `chebyshev` lowers to L3 [`chebyshev`](../L3/chebyshev.md) via the
typed-wrapper dissolution (substantive at the wrapper; identity-in-form on the
body), then to L2 [`chebyshev-iteration`](../L2/chebyshev-iteration.md) (the body
identity-in-form, iteration view erased):

- **L4 > L3** (substantive at the wrapper): the `Solve (ChebSim E)` monad
  collapses to explicit `(x, y)`-state threading; the `ChebOp<E, S>` closure
  collapses to a positional operator-parameters value; the `Read`/`ReadWrite`
  capability typing demotes to a documented mutation discipline; the `forM_`/
  `foldM` binds become tail recursions over static ranges. The kernel body's
  primitive sequence is value-thread-isomorphic. Same shape as the krylov-step
  typed-wrapper dissolution (`book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`);
  no dedicated chebyshev L4>L3 theme authored by this dispatch (Open Question).
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

**Caveat (independent of the above; not the status driver)**: no dedicated unit
test (multigrid-integration coverage only) — same justification as the firm L1/L2
entries.

## L4 vs L3 distinction

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
  this entry's `forM_`/`foldM` binds inherit.
- `book/src/L4/krylov-step.md` (cycle-006 firm) — the typed-wrapper precedent
  (state-stratification records, `Solve` monad, `readonly` `OpParams`,
  effect-localisation discipline) this entry follows, and the contrast operator:
  `krylov-step` folds via predicate-driven `iterate_while` with a demand-pruned
  trajectory; `chebyshev` uses bounded `forM_`/`foldM` with no trajectory.
- `book/src/design/l4_calculus.md` §2 (ownership categories), §3.7 (`iterate_while`
  family, contrasted with the bounded `forM_`/`foldM`), §3.8 (demand-pruning,
  not-applicable for the no-trajectory smoother) — the strawman conventions this
  entry cites and continues.
- `palace/linalg/chebyshev.cpp:191-220, :261-293` (4th/1st-kind `Mult2`; verified
  via codemap) — the L0 behaviour the L4 typed wrapper re-types; cited transitively
  via the L1/L2 entries. The `forM_` outer loop is the `for (int it = 0; it <
  pc_it; it++)`; the `foldM` inner loop is the `for (int k = 1; k < order; k++)`.
- `palace/linalg/chebyshev.hpp:72-75` (`MultTranspose2 → Mult2`; verified via
  codemap) — the transpose-under-symmetry law witness (law 4).
- `book/src/spec/slices/chebyshev.md:287-439` — the cycle-001-era §L4 "calculus
  form" this entry promotes (the `ChebOp`/`ChebSim` types, the `apply` monadic
  action, the `setup` action, the sequential-obstruction-as-`forM_`/`foldM`
  treatment, the capability-typed sim-state, the initial-guess branch-vs-derived-view
  discussion).

No L0 Palace source range "is" the L4 `chebyshev`; the L4 form names a typed
shape, and all L0 evidence is transitive through the cycle-012 firm L1/L2 entries.
```

---

## Index edits

### `book/src/L3/index.md` — append one dep-map row (after the `scal` row, current line 28)

```markdown
| [`chebyshev`](./chebyshev.md) | `(op, x, y, initial_guess) -> y'` (value-threaded fixed-degree polynomial smoother; inner-product-free; no convergence test). | L3 whole-tensor field ops: `apply_linop`, `axpy`, `axpby`, `axpbypcz`, `scal`; concepts: `sequential-obstruction`, `tensor-field-lift`, `elementwise-product`, `variant-absorption`, `derived-view-hoisting`, `constructed-operators`. Does NOT depend on `dot`/`nrm2` (inner-product-free — the structural distinction from `krylov-step`). L4 lift via `book/src/L4/chebyshev.md` (typed-wrapper dissolution; identity-in-form on body, substantive at wrapper; no L4-L3 theme file — in-line). | L2 [`chebyshev-iteration`](../L2/chebyshev-iteration.md) (body identity-in-form; surface adjustment consolidates the `(r,d,y,st)` recurrence carry into the L2 sweep; no L3-L2 theme file — in-line annotation per cycle-012 non-adjacent-identity convention). | `partial-obstruction` (harvested cycle-013T143923Z; body lifts to global tensor-field expression, inner `k`-recurrence + outer `pc_it`-sweep are witnessed sequential obstructions per Phillips & Fischer 2022 §2; unblocks full reduction of `book/src/spec/slices/chebyshev.md`) |
```

### `book/src/L3/index.md` — append one Working-Notes bullet (after line 39)

```markdown
- **First firm L3 partial-obstruction landed cycle-013**: `chebyshev` (the fixed-degree polynomial smoother). Unlike the BLAS-1 cohort (clean identity-lowerings) and `krylov-step` (firm body, non-lifting predicate-driven fold), `chebyshev` is the canonical **partial-obstruction** case — the per-inner-step body lifts to a global tensor-field expression, but the inner `k`-recurrence (degree `order`) and the outer `pc_it` Richardson sweep are witnessed sequential obstructions with a cited non-removability reason (Phillips & Fischer 2022 §2: recurrence form chosen for numerical stability over explicit polynomial expansion). The body is identity-in-form to the cycle-012 firm L2 `chebyshev-iteration` and, transitively (L3>L2 ∘ L2>L1 identity), to the L1 `chebyshev-smoother` — annotated in-line, no `L3-L2/` or `L3-L1/` directory (cycle-012 meta-phase non-adjacent-identity convention). It is inner-product-free (no `dot`/`nrm2`) — the structural distinction from `krylov-step`. Landing this row + the L4 `chebyshev` row unblocks full reduction of the Phase-1 slice `book/src/spec/slices/chebyshev.md`.
```

### `book/src/L4/index.md` — append one dep-map row (after the `iterate-while-with-prev` row, current line 51)

```markdown
| [`chebyshev`](./chebyshev.md) | `setup :: LinOp[E] -> SetupParams -> Variant -> Solve s (ChebOp E S)`; `apply :: ChebOp E S -> Bool -> Solve (ChebSim E) ()`. Constructed-operator smoother; `ChebOp` `readonly` closure (variant absorbed via distinct closure types `S`); `ChebSim = { x: Read, y: ReadWrite }` capability-typed sim-state. | Concepts: `state-stratification`, `solve-monad`, `constructed-operators`, `variant-absorption`, `derived-view-hoisting`, `sequential-obstruction`, `first-iteration-unrolling`, `elementwise-product`. L4 rows: **iteration combinators UNRECONCILED** — the obstructions are rendered as bounded `forM_`/`foldM`, which are NOT anchored L4 rows and compete with the firm [`iterate-while`](./iterate-while.md) family (whose entry names Chebyshev as a consumer). Reconciliation is a combinator-miner/lifter follow-up (see entry §Status + OQ 6). | L3 [`chebyshev`](../L3/chebyshev.md) via typed-wrapper dissolution (substantive at wrapper; identity-in-form on body; no L4-L3 theme file — same shape as `krylov-step-typed-wrapper-dissolution`), then L2 [`chebyshev-iteration`](../L2/chebyshev-iteration.md). | `rough-in` (harvested cycle-013T143923Z; firm at the body re-type of the cycle-012 firm L1/L2 entries, but rough-in at the wrapper — repairer downgrade cycle-013: the `forM_`/`foldM` iteration combinators are un-anchored and unreconciled against the firm `iterate-while` family) |
```

### `book/src/L4/index.md` — add a "Rough-in at L4" vocabulary-cohort note (do NOT add to "Firm at L4"; do NOT bump the "Firm at L4 (3)" count)

> Repairer note (cycle-013): the original instruction placed `chebyshev` in the
> "Firm at L4" list and bumped "Firm at L4 (3)" → "(4)". Since the L4 entry was
> downgraded to `rough-in` (un-anchored `forM_`/`foldM` wrapper vocabulary; see
> entry §Status + OQ 6), it must NOT join the firm cohort and the "Firm at L4 (3)"
> count stays at 3. Integrator: add the bullet below as a NEW "Rough-in at L4"
> sub-cohort (or an inline rough-in note) rather than under "Firm at L4".

```markdown
- [`chebyshev`](./chebyshev.md) *(rough-in — firm at the body, rough-in at the wrapper)* — typed-wrapper fixed-degree polynomial smoother; the `ChebOp` constructed-operator closure absorbs the polynomial-kind variant via distinct closure types; `apply` is a `Solve (ChebSim E)` action over a capability-typed `ChebSim`. Inner-product-free and convergence-test-free (the fixed-degree contrast to `krylov-step`). The two sequential obstructions are currently rendered as bounded `forM_` (outer `pc_it`) / `foldM` (inner `k`) binds, but **those combinators are un-anchored at L4 and compete with the firm [`iterate-while`](./iterate-while.md) family** (whose entry names Chebyshev as a consumer); reconciling the wrapper iteration vocabulary is a combinator-miner/lifter follow-up before the entry firms (OQ 6).
```

### `book/src/SUMMARY.md`

Add `  - [chebyshev](./L3/chebyshev.md)` under the L3 Part and `  - [chebyshev](./L4/chebyshev.md)` under the L4 Part. Integrator wires the exact positions (alphabetical within each Part, or after the existing krylov-step / BLAS-1 cohort chapters).

---

## Supporting evidence

- **Source verification (codemap)**: read `palace/linalg/chebyshev.cpp:191-220`
  (4th-kind `Mult2`) and `:261-293` (1st-kind `Mult2`), and
  `palace/linalg/chebyshev.hpp:14-114` (both class decls + `MultTranspose2 →
  Mult2` alias at `:72-75`). All ranges confirm the cycle-012 L1/L2 transcriptions
  exactly (the `pc_it` outer loop, the `k` inner loop, the scalar closed forms,
  the symmetry alias, the `dinv real-valued for now` note at `:37`).
- **Two-kinds decision** follows the cycle-012 L1/L2 lead: 4th-kind and 1st-kind
  collapse to one operator parameterised by `op.scalars`; the body does not branch
  on kind (variant absorption level (c)). Not re-derived here — cited to
  `book/src/L1/chebyshev-smoother.md` §Variant axes and
  `book/src/L2/chebyshev-iteration.md` §Variant axes.
- **Identity-lowering backfill template**: `book/src/L3/krylov-step.md`
  §Upward/§Downward + dep-map (the in-line non-adjacent-identity annotation
  pattern). The chebyshev L3 entry is **not** a pure identity-lowering (it carries
  a partial obstruction at the loop structure) but uses the same in-line
  annotation discipline for the body identity-in-form.
- **L4 strawman conventions** (`book/src/design/l4_calculus.md`): §2 ownership
  categories, §3.7 `iterate_while` (contrasted with the bounded `forM_`/`foldM`),
  §3.8 demand-pruning (noted not-applicable). Haskell `::` + TS-record braces in
  `text` fences, `$$ ... $$` math display for the reduction shapes — per the
  `book/src/L4/krylov-step.md` precedent.
- **Slice content lifted**: `book/src/spec/slices/chebyshev.md` §L3 (lines
  229-285, the tensor-field-form partial obstruction) → L3 entry; §L4 (lines
  287-439, the `ChebOp`/`ChebSim` monadic form) → L4 entry.

## Open questions / caveats

1. **L4>L3 chebyshev theme file (not authored).** This dispatch annotates the
   L4>L3 wrapper-dissolution **in-line** in both entries (it is the same
   value-thread-isomorphic-body shape the `krylov-step-typed-wrapper-dissolution`
   theme catalogs). If the lowering-verifier wants a dedicated audit anchor for
   the chebyshev edge specifically (e.g., to confirm the `forM_`/`foldM`-to-tail-
   recursion dissolution is information-preserving and the `Read`/`ReadWrite`
   demotion is faithful), a thin `book/src/L4-L3/chebyshev-typed-wrapper-dissolution.md`
   could be added in a later cycle. Routed to the cycle-013+ planner / OQ ledger
   as a low-priority follow-up — not blocking, because the krylov-step theme
   establishes the wrapper-dissolution shape and the chebyshev body is
   identity-in-form on the same vocabulary.

2. **Phase-1 slice reduction unblocked.** With the L3 and L4 chebyshev rows
   landed, all four layered representations of the Chebyshev smoother are firm/
   partial-obstruction (L1 cycle-012, L2 cycle-012, L3+L4 this dispatch). The
   slice `book/src/spec/slices/chebyshev.md` is now fully represented in the
   layered artifact. Per the CLAUDE.md invariant **Phase 1 corpus reduces as
   material is lifted**, a follow-up `same-layer-cross-cutter`-scoped dispatch
   (using `skills/phase-1-slice-reduction-audit`) should verify START+END boundary
   coverage and reduce the slice to a stub pointing at the firm layered entries
   (L1/chebyshev-smoother, L2/chebyshev-iteration, L3/chebyshev, L4/chebyshev,
   concepts/chebyshev-iteration). One residual coverage check: the slice's §L4
   four-stratum worked example (sim / operator-internal / ephemeral /
   scalar-recurrence) and the control-flow-boundary derived-view example were
   flagged at the slice's reduction-status header (lines 13-14) as candidate
   extensions to `concepts/state-stratification.md` and
   `concepts/derived-view-hoisting.md`; the L4 entry references both but does not
   author the concept-page extensions (that is layer-intro-author's domain). Note
   in the slice-reduction audit so the concept extensions are not lost on
   reduction.

3. **`partial-obstruction` status precedent.** The L3 chebyshev entry is marked
   `partial-obstruction` (body lifts, loop does not). This is distinct from the
   cycle-012-codified `partly-constructive` status (firm structure + a
   negative-anchor-backed constructive sub-part). `partial-obstruction` is the
   honest L3 verdict for a fixed-degree smoother and is the status the slice's §L3
   header already used ("partial obstruction"). If the meta-phase wants
   `partial-obstruction` codified alongside `firm`/`rough-in`/`obstruction`/
   `partly-constructive` as a first-class L3 status value, that is a methodology
   note for the cycle-015 meta-phase — flagged here, not enacted. (It is already
   in use informally at the slice level and at `book/src/spec/slices/*` §L3
   sections; this is the first firm *layered* L3 entry to carry it.)

4. **Layer-intro refresh (note for layer-intro-author).** The L3 `index.md`
   intro (`book/src/L3/index.md:1-16`) and the L4 `index.md` vocabulary-cohort
   prose (`book/src/L4/index.md:30-43`) will want a refresh once these rows land:
   the L3 intro should mention that the layer now carries its first
   partial-obstruction operator (not just clean lifts + the krylov-step non-lift),
   and the L4 cohort prose should note the bounded-`forM_`/`foldM` iteration shape
   alongside the `iterate-while` family. Flagged per the harvester "do not update
   layer intros" discipline.

5. **Complex transpose dead code.** Inherited from the L1/L2 entries: the complex
   `Transpose=true` inner-kernel specialisations exist but are unreachable under
   the symmetric wiring (`MultTranspose2 → Mult2`). Documented at both layers as a
   variant-axis caveat, not re-investigated here. (Already an Open Question on the
   slice and L1 entry; not newly opened.)

6. **[REPAIRER-OPENED, cycle-013] L4 chebyshev wrapper iteration vocabulary
   un-anchored — combinator-miner / lifter follow-up.** The L4 entry renders its
   two sequential obstructions as `forM_` (outer `pc_it`) and `foldM` (inner `k`)
   binds. These combinators are **not anchored at L4** (no dep-map row, no concept
   page) and **compete with** the firm canonical iteration vocabulary
   [`iterate-while`](../L4/iterate-while.md) — whose own entry (`iterate-while.md:7`)
   declares itself the "canonical iteration primitive at L4" and **explicitly names
   Chebyshev as one of its consumers** — plus its `iterate-while-with-prev`
   companion (both cycle-007 firm). The strawman maps bounded loops to
   `iterate_while_pure` with a step-count predicate (`book/src/design/l4_calculus.md`
   §6). The repairer **downgraded the L4 entry from `firm` to `rough-in`** (firm at
   the body, rough-in at the wrapper) because reconciling the wrapper iteration
   vocabulary is substantive re-authoring (re-expressing the bounded `forM_`/`foldM`
   — including the `foldM` 3-tuple `(r, d, st)` accumulator with embedded `modifyY`
   effects — in terms of the `iterate-while` family requires re-deriving the
   monadic body shape, not a mechanical name swap), which exceeds repair authority.
   Follow-up dispatch (combinator-miner or lifter) should EITHER (i) re-express the
   bounded loops via `iterate_while_pure` / `iterate-while-with-prev` with
   step-count predicates (strawman-conformant; reuses canonical vocabulary), OR
   (ii) anchor `forM_`/`foldM` as their own firm L4 rows with a justification for a
   second iteration vocabulary alongside `iterate-while`. On reconciliation, the
   entry firms and the `iterate-while.md:7` "Chebyshev reduces to iterate_while"
   claim is satisfied or explicitly amended. The L3 entry's `forM_`/`foldM`
   references render as tail recursions over static ranges and are NOT the concern
   (L3 has no `iterate-while` row to compete with) — they should be re-touched only
   if the follow-up changes the L4 wrapper shape.
```

