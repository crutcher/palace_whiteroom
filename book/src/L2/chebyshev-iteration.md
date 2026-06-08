# chebyshev-iteration

The base-algebra unfolding of the L1 [`chebyshev-smoother`](../L1/chebyshev-smoother.md):
the closed-form polynomial action `p_order(D⁻¹ A)·r` written explicitly as a
degree-`order` **three-term polynomial recurrence** composed of L1 leaf
primitives (`apply_linop`, `axpby`/`axpbypcz`, `scal`, elementwise diagonal
action), threaded by the variant-dependent scalar generator. The fusion-rotation
form: the matrix-free polynomial is de-fused into its constituent
direction/residual/accumulator updates with the HPC element-fused kernels
(`ApplyOrder0`, `ApplyOrderK`) unfolded back into base algebra.

## Context

At L1, [`chebyshev-smoother`](../L1/chebyshev-smoother.md) names the polynomial
action `y + p_order(D⁻¹ A)·(x − A·y)` as one closed-form smoother step. This step
is a **specialization of the L2 step-kernel combinator
[`correction_step`](./correction_step.md)** `y + B·(x − A·y)` with the
preconditioner slot `B = p_order(D⁻¹ A)` (the order-`order` correction polynomial
in `D⁻¹ A`): `correction_step` names the residual-correction skeleton, and
`chebyshev-iteration` fills `B` with the polynomial and unfolds its internal
three-term recurrence (Palace spells the contract verbatim — `chebyshev.cpp:193`
4th-kind, `:264` 1st-kind: "Apply smoother: y = y + p(A) (x - A y)"). L2 is the
layer where that polynomial is unfolded: the order-`order` Chebyshev correction
polynomial is realised as a parameterised three-term recurrence

    d_0     = α₀ · (dinv ⊙ r)                            -- initial direction
    for k = 1 .. order-1:
      y     = y + d                                      -- accumulate
      r     = r − A·d                                    -- residual update
      d     = sd_k · d + sr_k · (dinv ⊙ r)               -- direction recurrence
    y       = y + d                                      -- final accumulate

where `(α₀, sd_k, sr_k)` come from the variant scalar generator and `dinv ⊙ r`
is the elementwise diagonal action. This is the canonical **polynomial-recurrence**
shape — the same kernel-plus-driver shape the L2 [`krylov_step`](./krylov_step.md)
catalogs as one of its five pattern instances (`krylov_step.md:7`, citing
`book/src/L4/chebyshev.md` §Semantics `innerStep`). `chebyshev-iteration` is the concrete L2 entry that the
`krylov_step` variant-axis (3) (polynomial-kind, `op.scalars`) points at.

The HPC element-fused kernels in the L0 source — `ApplyOrder0` (one elementwise
pass computing `d = sr · dinv · r`) and `ApplyOrderK` (one elementwise pass
computing `d = sd · d + sr · dinv · r`, `palace/linalg/chebyshev.cpp:68-78,
:112-123`) — are **transparent fusions** at L2: they compute the same value as
the unfused `scal` + elementwise-product + `axpby` chain modulo standard
floating-point rules for the same operand order. L2 unfolds them into the base
composition and records the fusion as a one-line note.

A cross-cutting prose treatment lives at
[`concepts/chebyshev-iteration`](../concepts/chebyshev-iteration.md). The L2 entry
here is the firm operator definition.

## Signature

```text
chebyshev_iteration
  :: (op: ChebOp[S], x: Tensor[(S: ...)], y: Tensor[$S], initial_guess: Bool)
     -> Tensor[$S]
```

Shape contract (bunsen-style; named axes; the field shape group `S` and the
square operator form `LinOp[(S: ...), $S]` follow the named-shape-group
convention of [`l4_calculus`](../semantics/index.md) §1.2.1–§1.2.2) —
identical boundary to L1, with the internal scalar generator made explicit:

- `op` — `ChebOp[S]` — the constructed smoother. Carries `op.A :
  LinOp[(S: ...), $S]` (square, on the field shape group `S`), `op.dinv :
  Tensor[$S]`, `op.order : Int`, `op.pc_it :
  Int`, and the scalar generator `op.scalars`:
  - **4th-kind**: `scalars(k) = { α₀ = 4/(3·λ_max), sd_k = (2k−1)/(2k+3), sr_k =
    (8k+4)/((2k+3)·λ_max) }` — closed form in `k` and `λ_max`; stateless.
  - **1st-kind**: a `ρ`-threaded recurrence with `ρ₀ = δ/θ` (= `delta/theta`),
    `α₀ = 1/θ`, and for `k ≥ 1`: `ρ_k = 1/(2θ/δ − ρ_{k−1})`, `sd_k = ρ_k·ρ_{k−1}`,
    `sr_k = 2·ρ_k/δ` — threads a scalar state `ρ` across `k`.
- `x`, `y`, `initial_guess` — as in L1.
- result — `Tensor[$S]` — the post-sweep accumulator.

The L2 form differs from L1 only in **resolution**: L1 sees one closed-form
polynomial action; L2 sees the explicit `order`-step recurrence built from named
base primitives. The boundary contract is unchanged.

## Semantics

`chebyshev_iteration` realises the L1 polynomial action as a composition of base
algebra. One outer Richardson sweep (`palace/linalg/chebyshev.cpp:194-219` for
4th-kind; `:264-292` for 1st-kind) unfolds to:

```text
sweep(op, x, y, first):
  -- 1. residual: r = x − A·y   (or r = x, y = 0 on first sweep without guess)
  r = if first && not initial_guess
        then x                  -- with y := 0 (degenerate absorption)
        else axpby(1, x, -1, apply_linop(op.A, y))    -- r = x − A·y

  -- 2. initial direction:  d = α₀ · (dinv ⊙ r)
  (α₀, st) = op.scalars(0, op.scalar_init)
  d        = scal(α₀, elementwise_product(op.dinv, r))

  -- 3. inner recurrence  k = 1 .. order-1
  for k in 1 .. op.order - 1:
    y         = axpy(1, d, y)                          -- y += d
    r         = axpby(1, r, -1, apply_linop(op.A, d))  -- r -= A·d
    (sd, sr, st) = op.scalars(k, st)
    t         = elementwise_product(op.dinv, r)        -- dinv ⊙ r
    d         = axpby(sd, d, sr, t)                    -- d = sd·d + sr·t

  -- 4. final accumulate
  y = axpy(1, d, y)
  in y
```

The full action is `sweep` iterated `op.pc_it` times. Each line is a composition
of L1 leaf primitives:

- **Operator apply** — exactly one `apply_linop(op.A, ·)` per residual update and
  one per direction-image; the operator-apply count per step is structural (the
  standard Krylov/smoother cost metric).
- **Residual / accumulate / direction updates** — `axpy` / `axpby`. The L0 source
  realises `r = x − A·y` as `ApplyOp(*A, y, r); AXPBY(1, x, -1, r)` (an
  `apply_linop` then an `axpby`), and `r −= A·d` as the accumulating
  `ApplyOp(*A, d, r, -1.0)` (= `apply_linop` then `axpby(1, r, -1, A·d)`).
- **Elementwise diagonal action** — `elementwise_product(op.dinv, r)` realises
  the `D⁻¹` action `dinv ⊙ r`. Fused with the `scal`/`axpby` into one elementwise
  pass at L0 (`ApplyOrder0`, `ApplyOrderK`); de-fused into the base composition
  at L2.
- **Scalar generator** — `op.scalars(k, st)` produces `(α₀ | (sd, sr))` and the
  next scalar state. 4th-kind is stateless closed form; 1st-kind threads `ρ`.

This is the **polynomial-recurrence** primitive composition — the L2 building
block that `krylov_step`'s polynomial-method instances factor into.

## Algebraic laws

The laws below hold; absences are deliberate.

1. **Equivalence to the L1 closed-form action.** `chebyshev_iteration(op, x, y,
   ig)` computes the same value as `chebyshev_smoother(op, x, y, ig)` modulo
   floating-point reassociation — the explicit recurrence *is* the matrix-free
   evaluation of `p_order(D⁻¹ A)`. This is the L1↔L2 fusion-rotation identity:
   the recurrence and the closed-form action are the same algebra at different
   resolution. (Bit-exactness against any *other* polynomial evaluation scheme
   does not hold — see non-laws.)

2. **Variant-invariant primitive sequence.** The primitive *sequence* in `sweep`
   is identical across 4th-kind and 1st-kind — only `op.scalars` branches. This
   is the (c) primitive-sequence axis of
   [`variant-absorption`](../concepts/variant-absorption.md): both polynomial
   families admit the same `(α₀, sd_k, sr_k)`-parameterised recurrence shape;
   4th-kind via stateless closed form, 1st-kind via the `ρ`-threaded scalar
   recurrence. The `sweep` body does not branch on kind.

3. **Fusion transparency of the elementwise kernels.** `ApplyOrderK(sd, sr,
   dinv, r, d)` (one elementwise pass `d ← sd·d + sr·dinv·r`,
   `palace/linalg/chebyshev.cpp:112-123`) equals the base composition `axpby(sd,
   d, sr, elementwise_product(dinv, r))` for the same operand order. The fusion
   is a transparent performance trick (one kernel pass vs. three); L2 unfolds it.
   Same for `ApplyOrder0` (`d ← sr·dinv·r`) = `scal(sr,
   elementwise_product(dinv, r))`.

4. **Final-accumulate idempotence of the trailing `axpy`.** The closing
   `y = axpy(1, d, y)` (step 4) is the same `y += d` primitive as the loop's
   leading accumulate (step 3 head); the recurrence is written so the
   accumulation of `d_{order-1}` happens after the loop rather than at the loop
   head of a non-existent `k = order` iteration — a loop-boundary unrolling, not
   a distinct operation.

Laws that explicitly **do not** hold:

- **Polynomial-expansion equivalence.** Replacing the three-term recurrence with
  an explicit monomial sum `Σ c_j (D⁻¹ A)^{j+1} r` is **numerically unstable**
  for the operative `order` range — the recurrence form is chosen specifically
  for stability (Phillips & Fischer 2022 §2). The recurrence and the monomial sum
  are the same polynomial mathematically but **not** the same algorithm; the
  sequentiality is load-bearing. (This is the L3 sequential-obstruction's root.)

- **Step-reordering / associativity of the `k`-recurrence.** `d_{k+1}` depends on
  `r_{k+1}`, which depends on `d_k` — the recurrence is genuinely sequential in
  `k`. No reordering of the inner loop preserves the value. (L3 records this as a
  sequential obstruction.)

- **Bit-determinism across fusion choices.** A fused FMA `d ← sd·d + sr·dinv·r`
  (one rounding per element via FMA) is **not** bit-identical to the unfused
  two-rounding `scal` + `elementwise_product` + `axpby` chain. Treating the
  fusion as transparent (law 3) assumes no bit-exact-reproducibility promise
  against the unfused chain — the standard Palace smoother assumption (Phillips &
  Fischer §3). Load-bearing for bit reproduction, transparent for algorithmic
  correctness.

- **`pc_it`-sweep commutativity with the residual recompute.** Each sweep
  recomputes `r = x − A·y` from the post-previous-sweep `y`; sweeps do not commute
  with a cached residual. Standard outer-iteration sequentiality.

## Dependencies

- L1: [`apply_linop`](../L1/apply_linop.md) — operator action (residual,
  direction-image); [`axpy`](../L1/axpy.md), [`axpby`](../L1/axpby.md) —
  residual / accumulate / direction updates; [`scal`](../L1/scal.md) — initial
  direction scaling.
- Concepts: [`elementwise-product`](../concepts/elementwise-product.md) — the
  `D⁻¹` action `dinv ⊙ r`; [`variant-absorption`](../concepts/variant-absorption.md)
  — the (c) primitive-sequence axis (law 2);
  [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the
  `k`-recurrence and `pc_it`-sweep sequentiality (non-laws);
  [`chebyshev-iteration`](../concepts/chebyshev-iteration.md) — narrative;
  [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md) — the
  initial-direction / final-accumulate loop-boundary unrolling (law 4, the
  degenerate-residual branch).
- L1 sibling: [`chebyshev-smoother`](../L1/chebyshev-smoother.md) — the
  closed-form L1 action this entry unfolds (law 1).
- L2 sibling: [`krylov_step`](./krylov_step.md) — `chebyshev-iteration` is the
  concrete L2 entry behind `krylov_step`'s polynomial-method variant-axis (3);
  its `op.scalars` closure is `krylov_step`'s `op.scalars?` field.

## Variant axes

Same two axes as L1 ([`chebyshev-smoother`](../L1/chebyshev-smoother.md)):
**polynomial-kind** (`4th-kind` | `1st-kind`) absorbed into `op.scalars`, and
**element-type** (`real` | `complex`) dispatched at the primitive level (`axpy`,
`axpby`, `scal`, `elementwise_product`, `apply_linop` honour the operand element
type; `dinv` is real-valued). At L2 the polynomial-kind axis is concretely the
two `op.scalars` recurrences (4th-kind closed form vs. 1st-kind `ρ`-threaded),
sharing one primitive sequence (law 2).

## Status

`firm` — the primitive composition is a direct transcription of both `Mult2`
bodies (`palace/linalg/chebyshev.cpp:190-220, :261-293`), with the
element-fused `ApplyOrder0` / `ApplyOrderK` kernels unfolded into base algebra
and the fusion classified as transparent. The scalar recurrences are exact
closed forms from the source (4th-kind `:215-217`; 1st-kind `:286-288`). Every
algebraic law is a syntactic identity on the source. The absence of a dedicated
unit test (multigrid-integration coverage only) does not gate the
syntactic-identity laws — same justification as the L1 entry.

## L2 vs L1 distinction

- **L1**: one closed-form polynomial action `y + p_order(D⁻¹ A)·(x − A·y)` per
  sweep; the recurrence body is below L1 resolution; only `apply_linop` and the
  opaque setup `spectrum_estimate` are L1 dependencies.
- **L2**: the explicit `order`-step three-term recurrence built from named L1
  leaf primitives (`apply_linop`, `axpby`, `scal`, `elementwise_product`); the
  HPC element-fused kernels de-fused into base composition; the scalar generator
  made explicit as `op.scalars(k, st)`. The polynomial-kind variant is the
  concrete `op.scalars` recurrence; the primitive sequence is variant-invariant.

## Evidence

- `palace/linalg/chebyshev.cpp:68-78` — `ApplyOrder0` (real): one elementwise
  pass `D[i] = sr · DI[i] · R[i]` (= `scal(sr, elementwise_product(dinv, r))`).
- `palace/linalg/chebyshev.cpp:112-123` — `ApplyOrderK` (real): one elementwise
  pass `D[i] = sd · D[i] + sr · DI[i] · R[i]` (= `axpby(sd, d, sr,
  elementwise_product(dinv, r))`). Law 3 fusion witness.
- `palace/linalg/chebyshev.cpp:49-66` — `ApplyOp` accumulating overload
  (`A.AddMult(x, y, a)`) used for `r −= A·d` (the `a = -1.0` form,
  `:212, :283`).
- `palace/linalg/chebyshev.cpp:194-219` — 4th-kind sweep body: residual,
  `ApplyOrder0(4/(3·λ_max), …)`, the `k`-loop (`y += d`; `ApplyOp(*A, d, r,
  -1.0)`; `sd = (2k−1)/(2k+3)`; `sr = (8k+4)/((2k+3)·λ_max)`;
  `ApplyOrderK(sd, sr, …)`), final `y += d`.
- `palace/linalg/chebyshev.cpp:264-292` — 1st-kind sweep body: residual,
  `ApplyOrder0(1/theta, …)`, `rhop = delta/theta`, the `k`-loop (`rho =
  1/(2·theta/delta − rhop)`; `sd = rho·rhop`; `sr = 2·rho/delta`; `rhop = rho`),
  final `y += d`.
- `palace/linalg/chebyshev.cpp:215-217` — 4th-kind `sd` / `sr` closed forms.
- `palace/linalg/chebyshev.cpp:286-288` — 1st-kind `rho` / `sd` / `sr` recurrence.
- `book/src/L2/krylov_step.md:7` — catalogs `book/src/L4/chebyshev.md`
  §Semantics `innerStep` as one of the five polynomial-recurrence pattern
  instances `krylov_step` factors.
