# chebyshev-iteration-fusion

The fusion rotation for the Chebyshev polynomial smoother. Lowers the L2 explicit
`order`-step three-term recurrence [`chebyshev-iteration`](../L2/chebyshev-iteration.md)
into the L1 closed-form polynomial action [`chebyshev-smoother`](../L1/chebyshev-smoother.md):
the per-degree direction / residual / accumulator updates **fuse** into a single
closed-form matrix-free polynomial-action call `y + p_order(D⁻¹ A)·(x − A·y)`
whose coefficients the variant scalar generator produces. Narrated forward: the L2
recurrence collapses (fuses) upward into one named polynomial step at L1.

## Slug

`chebyshev-iteration-fusion`

## L2 form (LHS)

The L2 form is the explicit degree-`order` three-term polynomial recurrence,
built from named L1 leaf primitives, threaded by the variant scalar generator
(`palace/linalg/chebyshev.cpp:188-220` 4th-kind, `:261-293` 1st-kind; the L2
unfolding in [`chebyshev-iteration`](../L2/chebyshev-iteration.md) §Semantics):

```text
sweep(op, x, y, first):
  r = if first && not initial_guess
        then x                                       -- with y := 0
        else axpby(1, x, -1, apply_linop(op.A, y))   -- r = x − A·y
  (α₀, st) = op.scalars(0, op.scalar_init)
  d        = scal(α₀, elementwise_product(op.dinv, r))   -- d = α₀·(dinv ⊙ r)
  for k in 1 .. op.order - 1:
    y           = axpy(1, d, y)                          -- y += d
    r           = axpby(1, r, -1, apply_linop(op.A, d))  -- r −= A·d
    (sd, sr, st) = op.scalars(k, st)
    t           = elementwise_product(op.dinv, r)        -- dinv ⊙ r
    d           = axpby(sd, d, sr, t)                    -- d = sd·d + sr·t
  y = axpy(1, d, y)                                      -- final accumulate
  in y
```

The full L2 action is `sweep` iterated `op.pc_it` times. Each line is a
composition of L1 leaf primitives: one `apply_linop` per residual update and per
direction-image; `axpy` / `axpby` for residual / accumulate / direction updates;
`scal` for the initial direction; `elementwise_product` for the `D⁻¹` action; and
the scalar generator `op.scalars(k, st)` producing `(α₀ | (sd, sr))` and the next
scalar state (4th-kind stateless closed form; 1st-kind `ρ`-threaded).

## L1 form (RHS)

The L1 form names the same polynomial as **one closed-form action** — the
matrix-free evaluation of `p_order(D⁻¹ A)`, applied without exposing the
per-degree recurrence body ([`chebyshev-smoother`](../L1/chebyshev-smoother.md)):

    y_new = chebyshev_smoother(op, x, y_old, initial_guess)
          = y_old + p_order(D⁻¹ A)·(x − A·y_old)        -- repeated op.pc_it times

At L1 the order-`order` recurrence is **below the layer's resolution**: L1 sees a
single closed-form smoother step `y + p_order(D⁻¹ A)·r`, where `p_order` is the
Chebyshev residual-correction polynomial determined by `op.scalars`. The L2
`sweep` body — the `α₀`/`sd_k`/`sr_k`-parameterised direction/residual/accumulate
updates — is fused away into the opaque polynomial action.

## The fusion (L2 → L1)

The lowering is a **resolution collapse**, not an algebraic transformation of the
value: the L2 recurrence *is* the matrix-free evaluation of the L1 polynomial, so
the two compute the same value (modulo floating-point reassociation —
[`chebyshev-iteration`](../L2/chebyshev-iteration.md) law 1). The fusion folds
two distinct structures upward:

1. **Per-degree-step fusion (the primary fusion).** The L2 `order`-step loop —
   each degree `k` performing an `apply_linop` + `axpby` (residual) + a
   `scal`/`axpby` over an `elementwise_product` (direction) + an `axpy`
   (accumulate) — collapses into the single L1 token `p_order(D⁻¹ A)·(·)`. The
   `order` distinct iterations and their ~4 primitive calls each become one
   closed-form polynomial-action name. **This is the fusion**: the explicit
   recurrence's per-degree work is fused into one polynomial-action call whose
   degree and coefficients are closure fields, exactly as the L1 entry's
   §Semantics states ("never materialised as an explicit operator … applied
   matrix-free via a fixed-degree recurrence whose closed-form coefficients
   `op.scalars` generates").
2. **Element-kernel fusion (the secondary, transparent fusion).** Within each L2
   step, the `scal` / `elementwise_product` / `axpby` chain over `dinv` is
   *already* realised in the L0 source as the single element-fused kernels
   `ApplyOrder0` (`d ← sr·dinv·r`) and `ApplyOrderK` (`d ← sd·d + sr·dinv·r`,
   `palace/linalg/chebyshev.cpp:68-78, :112-123`). The L2 entry de-fuses these
   into the base composition and records them as transparent (L2 law 3); the L1
   form re-absorbs them — they are part of the opaque polynomial action. At
   L2>L1 these are *inside* the fused polynomial token, so they need no separate
   treatment here beyond the note that L1 does not see them.

The two scalar generators (4th-kind stateless closed form; 1st-kind `ρ`-threaded)
both fuse into the same `op.scalars` closure field — the **polynomial-kind variant
axis** is absorbed identically at L1 and L2 (it is the closure's identity, not a
runtime branch; L2 law 2 — the primitive *sequence* is variant-invariant).

## Applicability conditions

The fusion preserves the L1 value when:

1. **No bit-exactness promise across fusion choices.** The L2→L1 fusion treats
   the recurrence and the closed-form action as the same algebra at different
   resolution; a fused-FMA element kernel is NOT bit-identical to the unfused
   `scal` + `elementwise_product` + `axpby` chain (L2 non-law). The fusion is
   transparent for *algorithmic correctness* and load-bearing for *bit
   reproduction* (Phillips & Fischer 2022 §3; the standard Palace smoother
   assumption). The lowering is valid under the algorithmic-correctness reading.
2. **Sequentiality is preserved inside the fused token.** The L2 `k`-recurrence
   is genuinely sequential (`d_{k+1}` depends on `r_{k+1}` depends on `d_k`; L2
   non-law) and the monomial-sum expansion is numerically unstable for the
   operative `order` range. The L1 polynomial token does NOT license reordering
   or monomial re-expansion — it names *this* recurrence's value, computed by
   *this* stable three-term scheme. (This sequential obstruction is what blocks
   an L3 global-tensor-field form;
   [`concepts/sequential-obstruction`](../concepts/sequential-obstruction.md).)
3. **`pc_it`-sweep sequentiality.** Each L2 sweep recomputes `r = x − A·y` from
   the post-previous-sweep `y`; sweeps do not commute with a cached residual. The
   L1 form preserves this by repeating the polynomial action `pc_it` times over
   the recomputed residual (L1 §Signature "repeated op.pc_it times").
4. **Variant + element-type conformance.** Polynomial-kind (4th / 1st) is the
   `op.scalars` closure identity at both layers; element-type (real / complex) is
   dispatched at the primitive level at L2 and inside the opaque action at L1.
   The fusion holds for all four combinations (the primitive sequence is
   variant-invariant — L2 law 2).

## Justification kind

`algebraic` — the core identity is "the explicit three-term recurrence *is* the
matrix-free evaluation of `p_order(D⁻¹ A)`" (L2 law 1: `chebyshev_iteration(op,
x, y, ig) = chebyshev_smoother(op, x, y, ig)` modulo floating-point
reassociation). The fusion is the algebraic fact that the polynomial action and
its three-term realisation are the same value at different resolution. A
**reduction-chain** flavour is present in the per-step structure (the `order`-step
small-step recurrence reduces to one closed-form action), but the governing
justification is the algebraic recurrence↔polynomial identity, so the theme is
classified `algebraic`. The element-kernel sub-fusion (point 2 of §The fusion) is
a transparent-performance-trick fusion (L2 law 3) nested inside.

## Speculative L1 operators

None. Both anchors are firm
([`L1/chebyshev-smoother`](../L1/chebyshev-smoother.md),
[`L2/chebyshev-iteration`](../L2/chebyshev-iteration.md), both cycle-012
ratified). The L1 leaf primitives the L2 form composes
([`apply_linop`](../L1/apply_linop.md), [`axpy`](../L1/axpy.md),
[`axpby`](../L1/axpby.md), [`scal`](../L1/scal.md)) and the
[`elementwise-product`](../concepts/elementwise-product.md) concept are all
already-firm vocabulary; this theme proposes no new operators.

## Verified-against

L0 evidence ranges (verified via `palace-codemap` read_range this cycle):

- `palace/linalg/chebyshev.cpp:188-220` — 4th-kind `Mult2`: the `order`-step
  recurrence (`ApplyOrder0`, the `k`-loop with `sd`/`sr` closed forms,
  `ApplyOrderK`, the `y += d` accumulates) that L2 makes explicit and L1 fuses.
- `palace/linalg/chebyshev.cpp:261-293` — 1st-kind `Mult2`: same scaffold, the
  `ρ`-threaded scalars.
- `palace/linalg/chebyshev.cpp:68-78` — `ApplyOrder0` (real overload; the
  element-fused initial-direction kernel `d ← sr·dinv·r`; secondary fusion).
- `palace/linalg/chebyshev.cpp:112-123` — `ApplyOrderK` (real overload; the
  element-fused direction-recurrence kernel `d ← sd·d + sr·dinv·r`; secondary
  fusion).

L1 / L2 anchors:

- `book/src/L1/chebyshev-smoother.md` — the firm L1 closed-form action (RHS).
- `book/src/L2/chebyshev-iteration.md` — the firm L2 explicit recurrence (LHS);
  its law 1 is this theme's core identity.

## Status

`firm` — the L2→L1 fusion is the L2 entry's already-firm law 1 (the recurrence
*is* the polynomial action), read as a lowering. Both anchors are firm
(cycle-012 ratified); the fusion is a syntactic resolution-collapse with no
literature inference and no negative-anchor reconstruction. The per-step and
element-kernel structure both read straight off the source. This is the first
chapter under the `book/src/L2-L1/` Part; a `lowering-verifier` audit confirming
the fusion against the L0 source (both kinds) is the standard follow-up, not a
status reduction.

## Open questions / caveats

- **L3 sequential obstruction (downward context, not this theme's concern).** The
  L2 `k`-recurrence and `pc_it`-sweep sequentiality block a global-tensor-field
  L3 form — recorded in [`L2/chebyshev-iteration`](../L2/chebyshev-iteration.md)
  non-laws and [`concepts/sequential-obstruction`](../concepts/sequential-obstruction.md).
  The cycle-013 wave-1 harvester's L3 chebyshev row treats this; this L2>L1
  theme does not depend on it.
- **Lifting note (reverse direction, working notes only).** Lifting an L1
  polynomial-action token *up* to the L2 explicit recurrence requires knowing the
  `op.scalars` generator (which closed-form / `ρ`-threaded family) and the
  `order` — both are closure fields, so the lift is determinate given the
  closure. This reverse-direction note lives here in working notes, not in the
  formal high→low chapter.
- **Bit-reproduction caveat.** The fusion is transparent only under the
  algorithmic-correctness reading; bit-exact reproduction against any other
  polynomial-evaluation scheme does not hold (L2 non-law). Not a status
  reduction — it is the standard load-bearing-vs-transparent classification, and
  Palace itself uses the fused kernels.
