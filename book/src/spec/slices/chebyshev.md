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
  - `lambda_max` — scalar, scaled spectral upper bound.
  - `lambda_min` — scalar, only for 1st-kind; from user `sf_min` or
    Phillips & Fischer (2022) eq. 2.24 default
    `1.69 / (order^{1.68} + 2.11*order + 1.98)`.
  - `order`, `pc_it`, `variant ∈ {4th-kind, 1st-kind}` — fixed.
- Ephemeral per `apply_linop` call: residual `r`, direction `d`
  (both length `A.height`); workspace.

### Setup (pure of `(A, sf_max[, sf_min], order, pc_it, variant)`)

1. `dinv := reciprocal(extract_diagonal(A))`.
2. `lambda_max := sf_max * spectrum_estimate(A, dinv)`, where
   `spectrum_estimate` returns the dominant eigenvalue magnitude of
   `D^{-1} A` via a Hermitian spectral-norm primitive (power
   iteration; SLEPc when configured). See
   `concepts/spectrum-estimate.md`.
3. If `variant = 1st-kind`: also set `lambda_min` (from `sf_min` or
   the default formula); precompute `theta := (lambda_max +
   lambda_min)/2`, `delta := (lambda_max - lambda_min)/2`.

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

## Concept references

- `concepts/apply-linop.md` — the apply interface.
- `concepts/axpy.md`, `concepts/elementwise-product.md` —
  primitives used by the inner recurrence.
- `concepts/extract-diagonal.md`, `concepts/reciprocal.md` — setup
  primitives.
- `concepts/spectrum-estimate.md` — dominant-eigenvalue estimate.
- `concepts/constructed-operators.md` — variant absorption route.
- `concepts/variant-absorption.md` — invariant/procedural/primitive
  axes.
