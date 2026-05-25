# Slice: chebyshev

Chebyshev polynomial smoother applying `p_k(D^{-1} A)` to damp
high-frequency error on an SPD operator with extracted diagonal
preconditioner `D = diag(A)`. Used as the per-level smoother in
geometric multigrid and distributive-relaxation preconditioners.

Two polynomial variants are exposed, selected at construction:

- **4th-kind** (Phillips & Fischer 2022): requires only `lambda_max`.
- **1st-kind** (Adams-style): requires the spectral window
  `[lambda_min, lambda_max]`.

The variants share an outer Richardson-like residual/accumulator
scaffold and differ only in the scalar recurrence that builds the
polynomial. Variant absorption is via **constructed-operator**: the
caller chooses 4th- vs. 1st-kind at construction, and the resulting
smoother exposes a uniform `apply_linop` interface; the per-iteration
procedure does not re-inspect the variant.

## L1

### State

- Captured at `setup` (immutable through `apply_linop` calls):
  - `A` — SPD operator (by reference).
  - `dinv` — vector of `1 / diag(A)`, length `A.height`.
  - Variant-specific persisted scalars (set in `setup`, used in `apply`):
    - **4th-kind**: `lambda_max` — scaled spectral upper bound.
    - **1st-kind**: `theta := (lambda_max + lambda_min)/2`,
      `delta := (lambda_max - lambda_min)/2`. The bounds
      `lambda_max`, `lambda_min` themselves are transient setup
      values and do not persist past `setup`.
  - `order`, `pc_it` — fixed. `variant` is encoded by the
    constructed-operator class identity, not stored as a runtime
    field.
- Ephemeral per `apply_linop` call: residual `r`, direction `d`
  (both length `A.height`); workspace.

### Setup (pure of `(A, sf_max[, sf_min], order, pc_it, variant)`)

1. `dinv := reciprocal(extract_diagonal(A))`.
2. `lambda_max := sf_max * spectrum_estimate(A, dinv)`, where
   `spectrum_estimate` returns the dominant eigenvalue magnitude of
   `D^{-1} A` via a Hermitian spectral-norm primitive (power
   iteration; SLEPc when configured). See
   `concepts/spectrum-estimate.md`.
3. If `variant = 1st-kind`: derive `sf_min` (from user input or
   the Phillips & Fischer (2022) eq. 2.24 default
   `1.69 / (order^{1.68} + 2.11*order + 1.98)` when the user
   supplies a non-positive value); set
   `lambda_min := sf_min * lambda_max`; persist
   `theta := (lambda_max + lambda_min)/2`,
   `delta := (lambda_max - lambda_min)/2`. `lambda_max` and
   `lambda_min` are discarded after this step.

### Apply (`apply_linop`: given rhs `x`, accumulator `y`, optional `initial_guess`)

Repeat `pc_it` times the Richardson-like sweep:

1. Compute residual: `r := x - A*y` (or `r := x`, `y := 0` on the
   first iteration when `initial_guess = false`).
2. Apply the order-`order` polynomial of `D^{-1} A` to `r`,
   accumulating into `y`. The polynomial is a degree-`order`
   parameterized recurrence:
   - **Initial direction** (`k = 0`):
     `d := alpha_0 * dinv .* r` for a variant-dependent scalar `alpha_0`.
   - **Inner steps** (`k = 1 .. order - 1`):
     `y := y + d`
     `r := r - A*d`
     `d := sd_k * d + sr_k * dinv .* r`
     with variant-dependent scalars `(sd_k, sr_k)`.
   - **Final update**: `y := y + d`.

The polynomial coefficients `(alpha_0, sd_k, sr_k)` are determined
by `variant` and the spectral bounds; their concrete recurrences are
L2 detail (the closed-form `k`-indexed coefficients for 4th-kind and
the three-term Chebyshev recurrence centered at `theta` with
half-width `delta` for 1st-kind).

`MultTranspose` aliases `Mult` under the symmetry assumption.

### Operator-kind support

Real (`Operator`) and complex (`ComplexOperator`) instantiations
share the L1 procedure; the complex case uses `conj(dinv)` in the
transpose path.

## Consumers

- `gmg.cpp` (geometric multigrid): per-level relaxation.
- `distrelaxation.cpp` (distributive relaxation): smoother.

The smoother is a leaf in the preconditioner stack: it consumes `A`
(plus its diagonal) and produces a `Solver<OperType>` exposing
`apply_linop`.

## Open questions

- No direct unit test under `test/unit/`; behavior exercised through
  multigrid integration only.
- `spectrum_estimate` has a build-flag-dependent backend (power
  iteration vs. SLEPc); L2 unfold will need to acknowledge both.
- MPI involvement is confined to `spectrum_estimate` (parallel norms
  inside power iteration); the polynomial recurrence itself is
  local.
- The complex `Transpose=true` template specializations of the
  inner kernels exist but are unreachable: `MultTranspose` forwards
  to `Mult` under the symmetry assumption, so the transpose-conjugate
  paths are dead code under current wiring. Flagged for future
  cleanup or for use by an asymmetric variant.

## Concept references

- `concepts/apply_linop.md` — the apply interface.
- `concepts/axpy.md`, `concepts/elementwise-product.md` —
  primitives used by the inner recurrence.
- `concepts/extract-diagonal.md`, `concepts/reciprocal.md` — setup
  primitives.
- `concepts/spectrum-estimate.md` — dominant-eigenvalue estimate.
- `concepts/constructed-operators.md` — variant absorption route.
- `concepts/variant-absorption.md` — invariant/procedural/primitive
  axes.

## L2 — primitive composition

The L1 Apply procedure unfolds into a sequence of named base primitives. Variant absorption is preserved: 4th-kind and 1st-kind share the same primitive shape; only the closed-form scalars `(alpha_0, sd_k, sr_k)` differ.

### Setup primitives

```
setup(A, sf_max, sf_min, order, pc_it, variant):
  d_diag   = extract_diagonal(A)                  # vector, length A.height
  dinv     = reciprocal(d_diag)                   # vector, in-place ok
  lam_max  = sf_max * spectrum_estimate(A, dinv)  # scalar
  if variant == 1st-kind:
    sf_min_eff = sf_min if sf_min > 0
                  else 1.69 / (order^1.68 + 2.11*order + 1.98)
    lam_min  = sf_min_eff * lam_max
    theta    = (lam_max + lam_min) / 2
    delta    = (lam_max - lam_min) / 2
    persist: dinv, theta, delta, order, pc_it
  else:  # 4th-kind
    persist: dinv, lam_max, order, pc_it
```

Spectrum estimate is itself a sub-procedure (power iteration or SLEPc); see `concepts/spectrum-estimate.md`. It is opaque at this layer.

### Apply primitives

Let `op` denote the constructed smoother carrying `(A, dinv, order, pc_it, scalars)`. The variant-dependent scalar generator is

```
scalars(op, k):
  if op.variant == 4th-kind:
    # Phillips & Fischer 2022, eq. 2.12 (4th-kind Chebyshev coeffs)
    alpha_0 = 4/3 / op.lam_max
    sd_k    = (2k - 1) / (2k + 3)
    sr_k    = (8k + 4) / ((2k + 3) * op.lam_max)
  else:  # 1st-kind, three-term Chebyshev recurrence centered at theta
    alpha_0 = 1 / op.theta
    # rho_k tracked across k: rho_0 = delta / (2*theta), then
    #   rho_k = 1 / (2*theta/delta - rho_{k-1}) for k >= 1
    sd_k    = rho_k * rho_{k-1}              # = rho_k * rho_prev
    sr_k    = 2 * rho_k / op.delta
```

The per-call apply procedure:

```
apply_linop(op, x, y, initial_guess):
  for it in 1 .. op.pc_it:
    # 1. residual r = x - A y  (or r = x if !initial_guess on first sweep)
    if it == 1 and not initial_guess:
      r ← copy(x)
      zero(y)
    else:
      r ← copy(x)
      Ay ← apply_linop(op.A, y)
      axpy(-1, Ay, r)                         # r ← r - A y

    # 2. initial direction:  d = alpha_0 * dinv .* r
    a0 = scalars(op, 0).alpha_0
    d  ← elementwise_product(dinv, r)
    scal(a0, d)

    # 3. inner recurrence k = 1 .. order - 1
    for k in 1 .. op.order - 1:
      axpy(1, d, y)                           # y ← y + d
      Ad ← apply_linop(op.A, d)
      axpy(-1, Ad, r)                         # r ← r - A d
      (sd, sr) = scalars(op, k)
      # d ← sd * d + sr * (dinv .* r)
      t ← elementwise_product(dinv, r)
      scal(sd, d)
      axpy(sr, t, d)

    # 4. final accumulation
    axpy(1, d, y)                             # y ← y + d
```

### Primitive inventory

| Primitive            | Role in Apply                                  |
|----------------------|------------------------------------------------|
| `copy`               | `r ← x` at sweep start                         |
| `zero`               | `y ← 0` when no initial guess                  |
| `apply_linop(A, ·)`  | residual `Ay` and direction-image `Ad`         |
| `axpy(α, v, w)`      | residual update, direction accumulation, `y` accumulate |
| `elementwise_product`| `D⁻¹` action: `dinv .* r`                      |
| `scal(α, v)`         | scalar rescale of direction                    |

The `d ← sd·d + sr·(dinv .* r)` update is canonically `scal` + `elementwise_product` + `axpy`. Whether an implementation fuses these into one kernel pass (single elementwise loop over `d`, `dinv`, `r`) is transparent at L2 — the fused kernel computes the same value modulo standard floating-point rules for the same operand order.

### Variant absorption at L2

The primitive *sequence* in `apply_linop` is identical across variants. Only the scalar-generator `scalars(op, k)` branches on variant. This is the (c) primitive-sequence axis of variant absorption per `concepts/variant-absorption.md`, achieved here because both polynomial families admit a uniform `(alpha_0, sd_k, sr_k)` recurrence parameterization — 4th-kind via closed-form, 1st-kind via a `rho_k` scalar carried across `k`.

### Operator-kind support at L2

Real vs. complex differs only at the primitive level: `axpy`, `scal`, `elementwise_product` dispatch on the operand element type; `apply_linop(A, ·)` honors the operator's element type. The transpose path, under the symmetry assumption, aliases to `Mult`; the conjugate of `dinv` mentioned in L1 is dead code at current wiring and would only become live for an asymmetric variant.

### Numerical-claim preservation

- The `axpy(-1, Ad, r)` step computes `r - Ad` in the standard left-to-right reduction; non-associative summation order matches the source.
- The `elementwise_product(dinv, r)` then `axpy(sr, t, d)` route materializes a temporary `t`. A fused kernel `d ← sd·d + sr·dinv·r` is bit-identical for IEEE-754 only if the fused FMA pattern matches the unfused two-rounding pattern; treating fusion as transparent assumes the implementation does not promise bit-exact reproducibility against the unfused chain. This is the standard Palace assumption for smoothers (see Phillips & Fischer §3) and is preserved as a transparent optimization here.

### Open questions deferred to L3

- Whether the per-sweep loop body admits a global tensor-field form. The residual update `r ← r - A·d` and direction update `d ← sd·d + sr·dinv·r` are point-local once `A·d` is computed; the recurrence in `k` is sequential by construction (each iterate depends on the previous direction), so L3 will likely be a **partial obstruction**: the body is a tensor-field expression, but the `k`-recurrence is not global. Documented for the L2→L3 rotation.

## L3 — tensor-field form (partial obstruction)

The L2 procedure is a `pc_it`-times outer Richardson sweep wrapping a degree-`order` polynomial recurrence in `k`. Both the outer `pc_it` loop and the inner `k` loop are sequential by construction. We lift the **body** to a global tensor-field expression and record the **loop structure** as an obstruction.

### Tensor-field body (per inner step `k`)

Fix the inner-step body that runs once for each `k ∈ {1, …, order-1}`. With $A \in \mathbb{R}^{n \times n}$ SPD, $D^{-1} = \operatorname{diag}(\text{dinv}) \in \mathbb{R}^{n \times n}$, and the three carried fields $r_k, d_k, y_k \in \mathbb{R}^n$, the body is the simultaneous global update

$$
\begin{aligned}
y_{k+1} &= y_k + d_k, \\
r_{k+1} &= r_k - A\, d_k, \\
d_{k+1} &= \sigma_k^{\mathrm{d}}\, d_k + \sigma_k^{\mathrm{r}}\, D^{-1} r_{k+1},
\end{aligned}
$$

with scalar coefficients $(\sigma_k^{\mathrm{d}}, \sigma_k^{\mathrm{r}}) = (\text{sd}_k, \text{sr}_k)$ from the L2 `scalars(op, k)` generator. Each line is a fully global field expression — `axpy`, `apply_linop(A, ·)`, and `elementwise_product(dinv, ·)` are all defined as global tensor-field operations (see [`apply_linop`](../../concepts/apply_linop.md), [`axpy`](../../concepts/axpy.md), [`elementwise-product`](../../concepts/elementwise-product.md)). There is no per-element dependence within a line; the body **lifts cleanly**.

Similarly, the L2 *initial-direction* step
$$d_0 = \alpha_0\, D^{-1} r_0, \qquad r_0 = x - A y_{\mathrm{in}} \;\text{ (or } x \text{ when no initial guess)}$$
is a single global field expression, and the *final accumulation* $y_{\text{order}} = y_{\text{order}-1} + d_{\text{order}-1}$ is global.

### Sequential obstruction in `k`

The map $(r_k, d_k, y_k) \mapsto (r_{k+1}, d_{k+1}, y_{k+1})$ is genuinely sequential: $d_{k+1}$ depends on $r_{k+1}$, which depends on $d_k$. The order-`order` polynomial $p_{\text{order}}(D^{-1} A)$ admits a closed-form coefficient expansion, so a *symbolic* global form

$$y_{\mathrm{out}} = y_{\mathrm{in}} + p_{\text{order}}(D^{-1} A)\, r_0$$

exists; but evaluating the polynomial as a matrix-free action on $r_0$ in practice **re-derives** the same three-term recurrence (Horner / Clenshaw form). Replacing the recurrence with an explicit sum of monomials $\sum_{j=0}^{\text{order}-1} c_j (D^{-1} A)^{j+1} r_0$ is numerically unstable for the operative `order` range (Phillips & Fischer 2022 §2 motivates the recurrence form specifically for this reason). The sequentiality is **fundamental to the smoother's numerical behavior**, not an artifact of the implementation.

This is a [sequential obstruction](../../concepts/sequential-obstruction.md) at L3 in the inner `k` loop. See also [`tensor-field-lift`](../../concepts/tensor-field-lift.md) — the body lifts, the recurrence does not.

### Sequential obstruction in `pc_it`

The outer `for it in 1 .. pc_it` loop is also sequential — each Richardson sweep consumes the previous sweep's accumulated `y`. The composition $y_{\text{out}} = (I - p_{\text{order}}(D^{-1} A) (I - A \cdot))^{\text{pc\_it}} y_{\text{in}} + (\text{terms in } x)$ is the closed-form global statement, but evaluating it requires iterating the sweep — again, no parallelism in `it` is exposed. Standard outer-iteration sequentiality.

### What lifts vs. what does not

| Element                                         | L3 status                                          |
|-------------------------------------------------|----------------------------------------------------|
| Single inner-step body (the three assignments)  | Lifts to a global tensor-field expression.         |
| Initial direction $d_0 = \alpha_0 D^{-1} r_0$  | Lifts.                                             |
| Final accumulation $y \mathrel{+}= d$           | Lifts.                                             |
| Inner loop `k = 1 .. order-1`                  | **Obstructed** — sequential three-term recurrence. |
| Outer loop `it = 1 .. pc_it`                   | **Obstructed** — Richardson sweep sequentiality.   |
| Variant branching (4th- vs. 1st-kind)           | Lifts trivially — scalars are pure functions of $k$ (and of $\rho_{k-1}$ for 1st-kind, itself sequential in $k$ but $O(1)$ work per step). |

The L3 form is therefore a **partial obstruction**: the body is expressed as global field arithmetic, and the loop structure is recorded as a witnessed sequential obstruction with a cited reason for non-removability (Phillips & Fischer 2022 §2 — recurrence form chosen for numerical stability over explicit polynomial expansion).

### Scalar-recurrence side note (1st-kind)

The 1st-kind variant carries a scalar $\rho_k$ across `k` via $\rho_k = 1/(2\theta/\delta - \rho_{k-1})$. This is a scalar (length-1) sequential update — trivially "sequential" but $O(1)$ memory and arithmetic, and not part of the tensor-field state. It rides alongside the field recurrence as a coefficient generator; it does not affect the tensor-field lift status of the body.

### Concept references added at L3

- [`sequential-obstruction`](../../concepts/sequential-obstruction.md) — the classification used for both the `k` and `pc_it` loops.
- [`tensor-field-lift`](../../concepts/tensor-field-lift.md) — body-lifts-but-loop-doesn't is the canonical partial case.
