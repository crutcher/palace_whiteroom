# chebyshev-smoother

Mutation-lifted Chebyshev polynomial smoother: a pure-functional preconditioner
action `y' = chebyshev_smoother(op, x, y, initial_guess)` that applies a
degree-`order` diagonally-scaled Chebyshev polynomial of an SPD operator as a
Richardson-sweep smoother. The constructed-operator gate for polynomial
smoothing at L1; the per-level smoother consumed by geometric multigrid and
distributive-relaxation preconditioners.

## Context

`chebyshev_smoother` lifts the `ChebyshevSmoother<OperType>::Mult2` /
`ChebyshevSmoother1stKind<OperType>::Mult2` member-method family
(`palace/linalg/chebyshev.cpp:191-220, :261-293`) — which writes into the
accumulator argument `y`, threads a mutable residual workspace `r` and a
mutable direction workspace `d`, and reads the construction-bound spectral
bounds — to a single pure-functional smoother action over an opaque
constructed-operator closure. The two L0 classes (`ChebyshevSmoother` 4th-kind,
`ChebyshevSmoother1stKind` 1st-kind) collapse to one L1 operator whose variant
is carried by the closure, not by a runtime tag (see Variant axes). The
output-arg mutation idiom (`Mult2(x, y, r)` writes through `y` and scribbles
`r`, `d`) is an L0 concern reintroduced in the forthcoming L1>L0 lowering theme,
not in the L1 signature.

`chebyshev_smoother` is a **constructed-operator gate** at L1, in the same
family as [`ksp_solve`](./ksp_solve.md) and [`eigsolve`](./eigsolve.md): its
primary argument `op` is a structured opaque value built once at solver setup
(the `SetOperator` step, `palace/linalg/chebyshev.cpp:170-189, :233-259`),
carrying the captured operator `A`, the inverse diagonal `dinv`, the
fixed `order` / `pc_it`, and the variant-specific spectral scalars. Unlike
`ksp_solve`, the smoother is not a *solve to convergence* — it is a fixed
`pc_it`-sweep application of a fixed-degree polynomial, with no convergence
test. The closed-form coefficient generation is the defining L1 semantic; the
*unfolding* of that polynomial into its base-algebra three-term recurrence is
L2 detail (see [`L2/chebyshev-iteration`](../L2/chebyshev-iteration.md)).

A cross-cutting prose treatment lives at
[`concepts/chebyshev-iteration`](../concepts/chebyshev-iteration.md) — covering
the minimax-error background, the inner-product-free property, and the
distinction from CG. The L1 entry here is the firm operator definition; the
concept page is the narrative.

## Signature

```text
chebyshev_smoother
  :: (op: ChebSmoother[N], x: Tensor[N], y: Tensor[N], initial_guess: Bool)
     -> Tensor[N]

chebyshev_smoother(op, x, y, initial_guess) = y + p_order(D⁻¹ A)·(x − A·y)
                                              [repeated op.pc_it times]
```

Shape contract (bunsen-style; named axes):

- `op` — `ChebSmoother[N]` — the constructed smoother closure. Bound at setup;
  immutable across calls. Carries:
  - `op.A : LinearOperator[N, N]` — the captured SPD system operator. Read-only.
  - `op.dinv : Tensor[N]` — the inverse diagonal `1 / diag(A)`. Real-valued
    (even for a complex `A`, per the source `// real-valued for now`,
    `palace/linalg/chebyshev.hpp:37`).
  - `op.order : Int` — the polynomial degree (`> 0`; enforced by
    `MFEM_VERIFY`, `palace/linalg/chebyshev.cpp:166, :229`).
  - `op.pc_it : Int` — the number of outer Richardson sweeps.
  - `op.scalars : (k: Int, S) -> ((α₀ | (sd, sr)), S')` — the variant-bound
    pure scalar-coefficient closure (4th-kind closes over `lambda_max`;
    1st-kind closes over `theta`, `delta` and threads a scalar `rho`).
- `x` — `Tensor[N]` — the right-hand side (residual to smooth). Read-only.
- `y` — `Tensor[N]` — the input accumulator / current iterate. Read.
- `initial_guess` — `Bool` — whether `y` carries a meaningful initial guess.
  When `false`, the first sweep uses `r = x`, `y = 0` (degenerate-case
  absorption; see Algebraic laws law 5). A per-call argument, **not** a closure
  field — operator-internal state is invariant across calls
  (`palace/linalg/chebyshev.cpp:196, :266` read `this->initial_guess`, which is
  set per-consumer via `SetInitialGuess`, e.g.
  `palace/linalg/distrelaxation.cpp:36`).
- result — `Tensor[N]` — the post-smoothing accumulator (the L0 `y` after
  `Mult2` returns). Same length axis `N`.

`ChebSmoother[N]` is an *opaque constructed type* at L1: the variant
(4th-kind / 1st-kind) is absorbed into `op.scalars`; the L1 contract sees only
the smoother-action interface. Setup — the construction of `ChebSmoother[N]`
from `(A, sf_max[, sf_min], order, pc_it, variant)` — is itself a pure function
of those inputs modulo the opaque `spectrum_estimate(A, dinv)` sub-action that
estimates `lambda_max` (see Dependencies); it is described as a separate setup
action, mirroring the L0 `SetOperator` / `Mult2` split.

## Semantics

`chebyshev_smoother(op, x, y, initial_guess)` returns the accumulator after
`op.pc_it` Richardson sweeps, each sweep applying the degree-`order` polynomial
`p_order(D⁻¹ A)` to the current residual and accumulating the result into `y`:

    y_out = y + p_order(D⁻¹ A)·(x − A·y)     (one sweep; repeated pc_it times)

where `D⁻¹ = diag(op.dinv)` and `p_order` is the order-`order` Chebyshev
residual-correction polynomial determined by `op.scalars`. The result is a pure
function of `(op, x, y, initial_guess)`; the same inputs return the same value.
The L0 source overwrites `y` in place and scribbles the workspaces `r`, `d`; the
L1 form drops those — the smoother consumes `x`, `y` and produces a fresh
accumulator value.

The polynomial is **never materialised as an explicit operator** — it is applied
matrix-free via a fixed-degree recurrence whose closed-form coefficients
`op.scalars` generates. At L1 the recurrence body is below the layer's
resolution: L1 names the *action* `y + p_order(D⁻¹ A)·r` as one closed-form
smoother step. The base-algebra unfolding of that polynomial action (the
explicit `(α₀, sd_k, sr_k)`-parameterised three-term recurrence) is the L2 form
[`chebyshev-iteration`](../L2/chebyshev-iteration.md).

The smoother is **inner-product-free**: unlike a Krylov method, no `dot` / `nrm2`
reduction appears in the action — the coefficients are fixed closed forms of the
step index `k` and the spectral bounds, computed without inspecting the iterate
(`palace/linalg/chebyshev.cpp:215-217, :286-288`). This is the property that
makes Chebyshev attractive as a communication-light multigrid smoother
(see [`concepts/chebyshev-iteration`](../concepts/chebyshev-iteration.md)).

`MultTranspose` aliases `Mult` under the operator-symmetry assumption
(`palace/linalg/chebyshev.cpp` — `MultTranspose2` forwards to `Mult2`,
`palace/linalg/chebyshev.hpp:72-75`): for the SPD `A` the smoother is its own
transpose. At L1 this is the algebraic identity `chebyshev_smoother_transpose(op,
…) = chebyshev_smoother(op, …)`.

## Algebraic laws

The laws below hold; absences are deliberate.

1. **Affine-in-(x, y) action per sweep.** A single sweep is the affine map
   `y ↦ y + p_order(D⁻¹ A)·(x − A·y)`. Fixing `x` and writing
   `M = p_order(D⁻¹ A)`, one sweep is `y ↦ (I − M A)·y + M·x` — affine in `y`,
   affine in `x`. The polynomial action `M·(·)` is itself linear (a polynomial
   in the linear operator `D⁻¹ A`). This is the structural law that makes the
   smoother a valid linear-preconditioner action when `initial_guess = false`
   and `pc_it = 1` (see law 5).

2. **Linear preconditioner form (zero initial guess, single sweep).** With
   `initial_guess = false`, the first sweep sets `y = 0`, `r = x`, so the output
   is purely `y_out = p_order(D⁻¹ A)·x` — a *linear* function of `x`
   (`apply_linop`-shaped). This is the form consumed when the smoother is used
   as the `B` preconditioner inside an outer Krylov method or a multigrid
   V-cycle correction (`palace/linalg/distrelaxation.cpp:36`,
   `B_G->SetInitialGuess(false)`). The polynomial `p_order` is the
   minimax residual-reduction polynomial over the spectral window
   (4th-kind: `[0, lambda_max]`; 1st-kind: `[lambda_min, lambda_max]`); see
   [`concepts/chebyshev-iteration`](../concepts/chebyshev-iteration.md).

3. **Transpose identity under symmetry.** For SPD `A`,
   `chebyshev_smoother_transpose(op, x, y, ig) = chebyshev_smoother(op, x, y, ig)`.
   Witnessed by `MultTranspose2 → Mult2` aliasing
   (`palace/linalg/chebyshev.hpp:72-75`). The conjugate-`dinv` transpose kernels
   exist in the complex source (`palace/linalg/chebyshev.cpp:101-110, :150-159`)
   but are dead code under the current symmetric wiring — see Open questions.

4. **Sweep idempotence on the zero-residual fixed point.** If `y` already
   satisfies `A·y = x` (zero residual), then `r = x − A·y = 0`, every direction
   `d = 0`, and `y_out = y`. The exact solution is a fixed point of the sweep.
   (Mathematical identity; in IEEE-754 the residual is computed, not assumed
   zero, so floating-point noise applies.)

5. **Initial-guess degenerate-case absorption.** The `initial_guess = false`
   path is the algebraic specialisation of the `true` path under `y = 0`: setting
   `y := 0` makes `A·y = 0` and `r = x − A·y = x`, so the explicit
   `r = x; y = 0` branch (`palace/linalg/chebyshev.cpp:201-205, :271-275`) is the
   `y = 0` instance of the uniform residual `r = x − A·y`. The branch fires at
   most once per call (only on `it == 0 && !initial_guess`); sweeps `it ≥ 1`
   always take the uniform `r = x − A·y` path. This is the
   [`derived-view-hoisting`](../concepts/derived-view-hoisting.md) pattern at the
   control-flow boundary — a single `Bool` argument replaces a
   constructed-operator variant axis.

Laws that explicitly **do not** hold:

- **Sweep idempotence in general.** `chebyshev_smoother(op, x, ·, ig)` applied
  twice is **not** equal to applied once unless `pc_it` already absorbs the
  repetition: each sweep further reduces the residual, so two calls compose into
  `2·pc_it` sweeps of error reduction, not `pc_it`. The smoother is a contraction
  (on the relevant spectral window), not a projection.

- **Bit-determinism across operator representations.** Inherited from
  [`apply_linop`](./apply_linop.md): a matrix-free vs. assembled `A` give
  bit-different residuals `r = x − A·y`. Load-bearing per CLAUDE.md.

- **Linearity in `y` across the full `pc_it`-sweep action.** The full action
  with a non-zero initial guess is *affine*, not linear, in `y` (law 1's `M·x`
  term is the affine offset). Only the `initial_guess = false`, single-input
  form (law 2) is linear in `x`.

- **Spectral-bound monotone-correctness.** A smaller `lambda_max` estimate than
  the true spectral radius does **not** preserve the smoothing property — the
  minimax polynomial is calibrated to the window, and an underestimate breaks
  the contraction. The `sf_max` safety factor (`palace/linalg/chebyshev.cpp:180,
  :247`) scales the *estimate* up; correctness depends on `lambda_max` bounding
  the spectrum, which is an algorithmic precondition, not a law of the operator.

## Dependencies

`chebyshev_smoother` depends (at L1) on:

- [`apply_linop`](./apply_linop.md) — the operator action `A·y` (residual) and
  `A·d` (direction image), and the polynomial's matrix-free realisation.
- `spectrum_estimate` (setup only) — the dominant-eigenvalue estimate of
  `D⁻¹ A`, via a Hermitian spectral-norm primitive (power iteration; SLEPc when
  configured). At L0 this is `GetLambdaMax(comm, A, dinv)` →
  `linalg::SpectralNorm(comm, DinvA, hermitian)` where the **real** overload
  passes literal `true` (`palace/linalg/chebyshev.cpp:18`) and the **complex**
  overload passes `A.IsReal()` (`:27`); for the in-scope SPD-real wiring this is
  Hermitian (`palace/linalg/chebyshev.cpp:13-27`).
  Opaque at L1 — it is a setup sub-action producing the scalar `lambda_max`, not
  part of the per-call smoother action. A firm `spectrum_estimate` (the
  `SpectralNorm` power-iteration sibling) is an open L1 candidate
  (`scaffolding/open-questions.md`, the `matrix-weighted-norm-and-bilinear-form`
  residual cohort).

The polynomial-recurrence internals (`scal`, `axpby`, the elementwise diagonal
action) are **L2** detail — they appear when the closed-form polynomial action
is unfolded into base algebra at
[`chebyshev-iteration`](../L2/chebyshev-iteration.md). At L1 the action is one
closed-form step; only `apply_linop` and the opaque `spectrum_estimate` are L1
dependencies.

## Variant axes

`chebyshev_smoother` has two orthogonal variant axes at L1; both are absorbed
into the constructed-operator closure (level (c) of
[`variant-absorption`](../concepts/variant-absorption.md)).

- **polynomial-kind**: `4th-kind` | `1st-kind`. The L0 source splits this into
  two classes (`ChebyshevSmoother` 4th-kind, `palace/linalg/chebyshev.cpp:161`;
  `ChebyshevSmoother1stKind`, `:223`). They differ only in (a) the spectral
  data captured at setup (4th-kind: `lambda_max` alone; 1st-kind:
  `theta = (λ_max+λ_min)/2`, `delta = (λ_max−λ_min)/2`), and (b) the closed-form
  coefficient recurrence inside `op.scalars`. At L1 these collapse to one
  operator parameterised by the `op.scalars` closure; the per-call action does
  not branch on kind. This is the constructed-operator absorption — the variant
  is the closure's identity, not a runtime field.

- **element-type**: `real` | `complex`. The L0 source instantiates both
  (`template class ChebyshevSmoother<Operator>;` and `<ComplexOperator>`,
  `palace/linalg/chebyshev.cpp:295-299`). The smoother action is identical; only
  the underlying `apply_linop` and the elementwise diagonal scaling dispatch on
  element type. `dinv` is real-valued even for complex `A`
  (`palace/linalg/chebyshev.hpp:37`); the complex transpose path uses the
  conjugate of `dinv` but is dead code under symmetric wiring (Open questions).

The **spectral-bound-estimation method** (power iteration vs. SLEPc) is a
*setup-side* axis absorbed into the opaque `spectrum_estimate` sub-action; it
does not surface at the smoother-action signature. The **degree** (`order`) and
**sweep-count** (`pc_it`) are construction parameters carried in `op`, not
variant axes — they parameterise one operator, they do not select among
operators.

## Status

`firm` — the signature is a direct transcription of the `Mult2` member-method
family on both `ChebyshevSmoother` and `ChebyshevSmoother1stKind`, parameterised
by polynomial-kind and element-type; the algebraic laws are closed-form
identities readable straight off the source recurrence (no
literature-inference). The constructed-operator gate framing matches the firm
[`ksp_solve`](./ksp_solve.md) precedent. **Caveat (not a status reduction)**:
there is no dedicated unit test under `reference/palace/test/unit/` — behaviour
is exercised only through multigrid integration (`gmg.cpp`,
`distrelaxation.cpp`). Because every L1 law is a syntactic identity on
fully-specified source code rather than a literature-inferred property, the
absence of a dedicated test does not reduce confidence to rough-in (contrast
[`eigsolve`](./eigsolve.md), where literature-anchored convergence semantics
*did* warrant rough-in pending coverage).

> **Firm-promotion ratified (cycle-012 integrator).** The
> firm-without-dedicated-test decision was surfaced for integrator ratification
> and is ratified **keep-firm**. The decision deviates from the `eigsolve`
> constructed-operator-gate precedent (which landed rough-in), but the deviation
> is justified: every chebyshev law is a syntactic identity on fully-specified
> C++ source (verified exact by the critic), whereas `eigsolve`'s rough-in was
> driven by *literature-inferred convergence semantics* the source alone does
> not pin down. Chebyshev is additionally a bounded fixed-degree polynomial
> action with closed-form coefficients and live integration coverage
> (`gmg.cpp`, `distrelaxation.cpp`), not a composite solve-to-convergence with
> constructed sum-type status — so the `eigsolve` precedent does not bind.

## L1 vs L0 distinction

- **L0**: two template classes (`ChebyshevSmoother<OperType>`,
  `ChebyshevSmoother1stKind<OperType>`) deriving `Solver<OperType>`. `Mult2(x, y,
  r)` writes through `y`, scribbles the passed workspace `r` and the member
  workspace `d` (`palace/linalg/chebyshev.hpp:42, :105`), reads the
  construction-bound `lambda_max` / `theta` / `delta`, and reads
  `this->initial_guess`. `SetOperator` captures `A`, assembles and reciprocates
  the diagonal into `dinv`, and computes the spectral bounds via
  `GetLambdaMax → linalg::SpectralNorm`. `Mult` forwards to `Mult2` with a
  resized member workspace `r`; `MultTranspose2` aliases `Mult2`.
- **L1**: one pure-functional smoother action `y' = chebyshev_smoother(op, x, y,
  initial_guess)` over an opaque constructed closure `op` carrying `(A, dinv,
  order, pc_it, scalars)`. No destination buffer, no workspace ownership in the
  signature. Polynomial-kind and element-type collapsed into the closure; the
  spectral-bound estimation is a setup sub-action. The closed-form polynomial
  action is named as one step; its base-algebra unfolding is the L2 form.

## Evidence

- `palace/linalg/chebyshev.hpp:14-23` — `ChebyshevSmoother` class doc + decl:
  "Matrix-free diagonally-scaled Chebyshev smoothing … Chebyshev polynomials of
  the 4th-kind … Phillips and Fischer, arXiv:2210.03179v1 (2022)."
- `palace/linalg/chebyshev.hpp:30-43` — 4th-kind member layout: `const int
  pc_it, order;`, `const OperType *A;`, `VecType dinv;`, `double lambda_max,
  sf_max;`, `mutable VecType d, r;`.
- `palace/linalg/chebyshev.hpp:47-75` — 4th-kind ctor signature `(comm,
  smooth_it, poly_order, sf_max)`; `Mult` resizes member `r` and forwards to
  `Mult2`; `MultTranspose2(x, y, r) { Mult2(x, y, r); }` (symmetry alias).
- `palace/linalg/chebyshev.hpp:80-114` — `ChebyshevSmoother1stKind` doc + decl
  (Adams et al. 2003); 1st-kind member `double theta, delta, sf_max, sf_min;`;
  ctor `(comm, smooth_it, poly_order, sf_max, sf_min)`.
- `palace/linalg/chebyshev.cpp:13-27` — `GetLambdaMax` (real + complex
  overloads): builds `DinvA = Dinv·A` and returns `linalg::SpectralNorm(comm,
  DinvA, hermitian)` — the **real** overload (`:18`) passes literal `true`; the
  **complex** overload (`:27`) passes `A.IsReal()`. The opaque
  `spectrum_estimate` setup sub-action.
- `palace/linalg/chebyshev.cpp:161-189` — 4th-kind ctor + `SetOperator`:
  `op.AssembleDiagonal(dinv); dinv.Reciprocal();` then `lambda_max = sf_max *
  GetLambdaMax(...)`, with `MFEM_VERIFY(lambda_max > 0.0, …)`.
- `palace/linalg/chebyshev.cpp:191-220` — 4th-kind `Mult2` body: the `pc_it`
  outer sweep; `r = x − A·y` (via `ApplyOp(*A, y, r); AXPBY(1, x, -1, r)`) or
  `r = x; y = 0` on first sweep without initial guess; `ApplyOrder0(4/(3·λ_max),
  dinv, r, d)`; the `k`-loop with `sd = (2k−1)/(2k+3)`, `sr =
  (8k+4)/((2k+3)·λ_max)`; final `y += d`.
- `palace/linalg/chebyshev.cpp:233-259` — 1st-kind `SetOperator`: `sf_min`
  default `1.69 / (order^1.68 + 2.11·order + 1.98)` when non-positive (Phillips &
  Fischer 2022, eq. 2.24); `theta = 0.5·(λ_max+λ_min)`, `delta =
  0.5·(λ_max−λ_min)`.
- `palace/linalg/chebyshev.cpp:261-293` — 1st-kind `Mult2` body: identical sweep
  scaffold; `ApplyOrder0(1/theta, dinv, r, d)`; `rhop = delta/theta` (NOTE: the
  slice §L2 line 160 claims `delta/(2·theta)` — the **source is `delta/theta`**);
  the `k`-loop with `rho = 1/(2·theta/delta − rhop)`, `sd = rho·rhop`, `sr =
  2·rho/delta`, `rhop = rho`.
- `palace/linalg/chebyshev.cpp:295-299` — element-type instantiations
  (`<Operator>` and `<ComplexOperator>` for both kinds).
- `palace/linalg/gmg.cpp:52-59` — consumer: geometric-multigrid per-level
  smoother constructs `ChebyshevSmoother` (4th) or `ChebyshevSmoother1stKind`
  (1st) per `cheby_4th_kind`.
- `palace/linalg/distrelaxation.cpp:21-36` — consumer: distributive-relaxation
  smoother constructs the same; `B_G->SetInitialGuess(false)` (law 2 use site).
- `book/src/spec/slices/chebyshev.md:34-116` — the cycle-001-era L1 slice
  content this entry promotes (with the `rho_0` correction noted above).
- `book/src/concepts/chebyshev-iteration.md` — cross-cutting prose treatment.
