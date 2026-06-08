---
layer: L3
operator: chebyshev
firmness: partial-obstruction
lowers_to:
  - book/src/L2/chebyshev-iteration.md (body identity-in-form in-line; substantive nested-loop erasure via book/src/L3-L2/chebyshev-nested-recurrence.md)
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

Unlike L3 [`krylov_step`](./krylov_step.md), `chebyshev` is **not** a Krylov
method — it is **inner-product-free** (no `dot` / `nrm2` reduction appears in
the body; the coefficients are closed forms of the step index `k` and the
spectral bounds, computed without inspecting the iterate) and has **no
convergence test** (it applies a fixed-degree polynomial `pc_it` times; the loop
bounds are static, not predicate-driven). It is therefore defined here as its
own L3 operator in L3 vocabulary, not as a specialisation of `krylov_step`. The
two share the L3 whole-tensor field-operation vocabulary (`apply_linop`,
`axpby`, `axpbypcz`, `scal`, [`elementwise-product`](../concepts/elementwise-product.md))
but differ in their iteration structure: `krylov_step`'s outer loop is a
convergence-predicate-driven `iterate_while` fold; `chebyshev`'s loops are two
nested **step-count-predicate** `iterate_while_pure` folds (outer `pc_it`
Richardson sweep `s.it <= op.pc_it`, inner `k`-recurrence `c.k <= op.order - 1`),
rendered at L3 as the `iterate_while_pure_L3` tail recursions over those static
ranges.

The relationship to the adjacent layers:

- **Upward** to L4: [`chebyshev`](../L4/chebyshev.md) is the typed
  `Solve`-monad wrapper. The wrapper-dissolution (the `Solve (ChebSim E)`
  monad → explicit `(x, y)`-state threading; the `ChebOp` closure → positional
  operator-parameters value; the `Read`/`ReadWrite` capability typing on
  `ChebSim` → a documented mutation discipline; the two nested
  `iterate_while_pure` folds → `iterate_while_pure_L3` tail recursions over their
  step-count predicates) is **substantive at the wrapper**; the
  kernel body's primitive sequence is **value-thread-isomorphic** between the
  L4 form and this L3 form. The L4 `do`-block dissolves to a `let`-chain; the
  L4 `modifyY (\y -> y .+. dN)` dissolves to the explicit `let y' = y + dN`
  binding. There is no `book/src/L4-L3/` theme file — the
  dissolution is value-thread-isomorphic on the body and the wrapper rewrite is
  the same shape the krylov_step typed-wrapper-dissolution theme catalogs
  (`book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`).
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
  state. This is information-preserving. The **body identity-in-form** annotation
  lives in-line here per the non-adjacent-identity convention
  (precedent: `book/src/L3/krylov_step.md` §Downward); the **substantive
  nested-loop erasure** (the two `iterate_while_pure_L3` tail recursions dissolving
  into the L2 loop-as-driver + role reference, with the inner-`k` + outer-`pc_it`
  `sequential-obstruction`s erased to the L2 non-laws) is the dedicated L3>L2 theme
  [`chebyshev-nested-recurrence`](../L3-L2/chebyshev-nested-recurrence.md) — the loop surface exceeds the identity-only convention, the same
  body-identity-in-line / loop-erasure-as-theme division `ksp_solve` makes
  (`krylov-step-body-identity` + `ksp-solve-outer-driver`).

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
`book/src/L3-L1/` directory is created** (per the non-adjacent-identity convention
`l3-l1-inline-identity-rotation-convention`, lowering directories are
per-adjacent-edge only). Note the caveat below: the L1↔L2 identity is on the
**body**; it does not erase the L3 loop-structure obstruction, which is a
property of the surrounding two nested `iterate_while_pure` folds (the
`iterate_while_pure_L3` tail recursions over the `pc_it`/`k` step-count
predicates), not of the body.

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
monadic effect; the field shape group `S` and the square operator form
`LinOp[(S: ...), $S]` follow the named-shape-group convention of
[`l4_calculus`](../semantics/index.md) §1.2.1–§1.2.2):

- **`op`** — operator-parameters value. Closure-captured by the body via the
  convention that `op` is a positional argument never present in the return
  position. The body reads:
  - `op.A : LinOp[(S: ...), $S]` — the captured SPD operator (square, on
    the field shape group `S`; residual `apply_linop op.A y` and direction-image
    `apply_linop op.A d`).
  - `op.dinv : Tensor[$S]` — the inverse diagonal `1/diag(A)` (the `D⁻¹` action
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
- **`x`** — `Tensor[(S: ...)]` — the right-hand side (residual to smooth). Read-only.
- **`y`** — `Tensor[$S]` — the input accumulator / current iterate. Read.
- **`initial_guess`** — `Bool` — whether `y` carries a meaningful initial guess.
  When `false`, the first sweep uses `r = x` with `y := 0` (degenerate-case
  absorption — the `y = 0` instance of the uniform `r = x − A·y`). A per-call
  argument, not a field of `op`.
- **result `y'`** — `Tensor[$S]` — the post-smoothing accumulator
  (value-threaded; no aliasing with the input `y`). Same shape group `S`.

There is **no `outputs` record** in the signature: `chebyshev` is
inner-product-free and convergence-test-free, so no residual-norm / breakdown
readout is produced per step (contrast L3 [`krylov_step`](./krylov_step.md),
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
fields `r, d, y : Tensor[$S]`, the body is the simultaneous global update

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
rendering of the L4 [`chebyshev`](../L4/chebyshev.md)'s two nested
[`iterate_while_pure`](../L4/iterate_while.md) folds over **step-count
predicates** (`c.k <= op.order - 1` inner, `s.it <= op.pc_it` outer) — the
`iterate_while_pure_L3` tail-recursion lowering image of those bounded folds (per
L4 `chebyshev` §"L4 > L3"), the iteration view that L3 makes load-bearing. The
body inside `kloop` is the tensor-field update above; every binding is a
whole-tensor field operation.

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
- [`axpy`](./linear_combination.md#arity-specializations), [`axpby`](./linear_combination.md#arity-specializations) — residual / accumulate / direction
  updates.
- [`scal`](./linear_combination.md#arity-specializations) — initial-direction scaling.
- [`axpbypcz`](./linear_combination.md#arity-specializations) — the direction update `d = sd·d + sr·t` is in the
  linear-update family (here realised as `elementwise_product` then `axpby`; the
  three-input `axpbypcz` shape is the unfused canonical form).

`chebyshev` does **not** depend on the L3 reductions [`dot`](./inner_product.md#specializations) /
[`nrm2`](./inner_product.md#consumer-nrm2-and-matrix-weighted-norm) — it is inner-product-free. This is the structural
distinction from L3 [`krylov_step`](./krylov_step.md).

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
*variant* (contrast `krylov_step` axis 4): the `initial_guess` branch is a
degenerate-case absorption controlled by a `Bool` argument, and the
initial-direction / final-accumulate boundary is a fixed loop-unrolling, not a
selectable form.

## Status

`partial-obstruction` — the per-inner-step body lifts cleanly to a global
tensor-field expression (every line is whole-tensor by signature shape; matches
the L2 `sweep` body and the L0 `Mult2` bodies); the inner `k`-recurrence
and the outer `pc_it` Richardson sweep are **witnessed sequential obstructions**
with a cited non-removability reason (Phillips & Fischer 2022 §2: recurrence
form chosen for numerical stability). The status reflects the **loop structure**,
not the body. The body's algebraic laws are syntactic identities on the source
(inherited from the firm L1/L2 entries). No dedicated unit test under
`reference/palace/test/unit/` — behaviour is exercised only through multigrid
integration (`gmg.cpp`, `distrelaxation.cpp`); the body laws are syntactic
identities on fully-specified C++ source, so the missing test does not gate.

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
to L2's loop-as-composition-driver) and leaves the body identity-in-form. The
**body** identity-in-form annotation lives in-line here (per the
non-adjacent-identity convention; precedent
`book/src/L3/krylov_step.md`); the **substantive loop erasure** is the dedicated
L3>L2 theme [`chebyshev-nested-recurrence`](../L3-L2/chebyshev-nested-recurrence.md).

## L3 vs L4 distinction

- **L4**: typed `Solve`-monad wrapper. The `ChebOp<E, S>` closure carries the
  variant-typed scalar generator; `apply :: ChebOp E S -> Bool -> Solve (ChebSim
  E) ()` threads `(x, y)` through the `Solve (ChebSim E)` monad with `Read`/
  `ReadWrite` capability typing; the two sequential obstructions surface as two
  nested `iterate_while_pure` folds with step-count predicates (`iterate_while_pure`
  outer `pc_it` sweep, `iterate_while_pure` inner `k`-recurrence).
- **L3**: value-threaded positional form. The `Solve` monad has dissolved (`(x,
  y)` threaded explicitly; `modifyY` → explicit `let y' = ...`); the capability
  typing has demoted to a documented invariant; the closure-typed variant
  absorption has collapsed to one positional `op`; the two nested
  `iterate_while_pure` folds are the `iterate_while_pure_L3` tail recursions over
  their step-count predicates. The kernel body's primitive sequence is
  value-thread-isomorphic to L4; only the wrapper differs.

## Evidence

- `palace/linalg/chebyshev.cpp:191-220` — 4th-kind `Mult2` body: the `pc_it` outer sweep; `r = x − A·y` (via `ApplyOp(*A, y, r);
  AXPBY(1, x, -1, r)`) or `r = x; y = 0` on first sweep without initial guess;
  `ApplyOrder0(4/(3·λ_max), dinv, r, d)`; the `k`-loop with `y += d`,
  `ApplyOp(*A, d, r, -1.0)`, `sd = (2k−1)/(2k+3)`, `sr = (8k+4)/((2k+3)·λ_max)`,
  `ApplyOrderK(sd, sr, dinv, r, d)`; final `y += d`. The body whose three-line
  inner update this L3 entry lifts to tensor-field form.
- `palace/linalg/chebyshev.cpp:261-293` — 1st-kind `Mult2` body: identical sweep scaffold; `ApplyOrder0(1/theta, dinv, r, d)`;
  `rhop = delta/theta`; the `k`-loop with `rho = 1/(2·theta/delta − rhop)`,
  `sd = rho·rhop`, `sr = 2·rho/delta`, `rhop = rho`; final `y += d`. The
  variant-invariant body sequence (law 5) is witnessed by the identical sweep
  scaffold across the two bodies.
- `palace/linalg/chebyshev.hpp:14-23` — `ChebyshevSmoother` (4th-kind) class doc
  + decl: "Matrix-free diagonally-scaled Chebyshev
  smoothing … 4th-kind … Phillips and Fischer, arXiv:2210.03179v1 (2022)."
- `palace/linalg/chebyshev.hpp:72-75` — `MultTranspose2(x, y, r) { Mult2(x, y,
  r); }` — the symmetry alias witnessing law 3.
- `palace/linalg/chebyshev.hpp:80-114` — `ChebyshevSmoother1stKind` class doc +
  decl: "standard 1st-kind Chebyshev polynomials … Adams
  et al., JCP (2003)"; `double theta, delta, sf_max, sf_min;`.
- `palace/linalg/chebyshev.hpp:37` — `VecType dinv; // … real-valued for now` — the element-type variant-axis note.
- `book/src/L2/chebyshev-iteration.md` (firm) — the L2
  primitive-composition form this entry's body is identity-in-form to; §Semantics
  `sweep` is exactly this body with the field-algebra operators spelled as their
  L1-primitive names. Laws 1/2/3 (L2) are the body-equivalence and fusion-
  transparency anchors; the L2 non-laws (step-reordering, `pc_it`-non-commutativity)
  are the L3 loop-structure obstructions.
- `book/src/L1/chebyshev-smoother.md` (firm) — the L1 closed-form
  action the body is value-thread-isomorphic to (transitively, in-line).
- `book/src/L3/krylov_step.md` (firm) — the template for the
  identity-lowering backfill (§Upward/§Downward in-line annotation) and the
  contrast operator (Krylov, predicate-driven loop, inner-product-bearing) vs
  this fixed-degree, inner-product-free, static-range smoother.
- `book/src/concepts/chebyshev-iteration.md` — narrative.
