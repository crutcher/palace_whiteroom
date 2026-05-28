---
agent: harvester
invoked_at: 2026-05-28T034154Z
scope: L1 operator: chebyshev-smoother; L2 operator: chebyshev-iteration
status: integrated
integrated_at: 2026-05-28T072500Z
integration_commit: 5964cb4
integration_notes: "Applied cycle-012 (report 2 of 8). Firm L1 chebyshev-smoother + firm L2 chebyshev-iteration created (RATIFIED KEEP-FIRM by integrator) + L1/index.md (Firm 9->10) + L2/index.md dep-map row + 2 SUMMARY entries. Closes cycle-011 OQ l1-l2-chebyshev-smoother-and-iteration-firm-row-promotion. 4 new OQs. L2 firm cohort 1->2 (first L2 growth since cycle-005; priority #17). 0 gate hits. Build exit 0, pages rendered."
inputs:
  - book/src/spec/slices/chebyshev.md (cycle-011 partially-reduced slice; L1/L2/L3/L4 content)
  - palace/linalg/chebyshev.cpp (VERIFIED L0 source; ChebyshevSmoother + ChebyshevSmoother1stKind)
  - palace/linalg/chebyshev.hpp (VERIFIED L0 source; class decls)
  - palace/linalg/gmg.cpp:53-59 (consumer: multigrid V-cycle smoother)
  - palace/linalg/distrelaxation.cpp:21-35 (consumer: distributive relaxation)
  - cycle-011 OQ l1-l2-chebyshev-smoother-and-iteration-firm-row-promotion
  - book/src/concepts/chebyshev-iteration.md (high-level prose)
  - book/src/L1/apply_linop.md, book/src/L1/index.md (L1 vocabulary + entry conventions)
  - book/src/L2/krylov-step.md, book/src/L2/index.md (L2 vocabulary + entry conventions)
---

# CYCLE: Formalize chebyshev-smoother at L1 + chebyshev-iteration at L2

## Summary

This dispatch promotes the cycle-001-era `chebyshev.md` slice into two firm
layered rows per cycle-011 OQ
`l1-l2-chebyshev-smoother-and-iteration-firm-row-promotion`. **`L1/chebyshev-smoother`**
is the mutation-lifted smoother primitive: a pure-functional preconditioner
action `(op, x, y, initial_guess) → y'` that applies a degree-`order`
diagonally-scaled Chebyshev polynomial of the operator as a Richardson-sweep
smoother, where `op` is a constructed-operator closure carrying the variant
(4th-kind / 1st-kind) and the spectral-bound-derived coefficient generator.
**`L2/chebyshev-iteration`** unfolds that L1 closed-form polynomial action into
its base-algebra composition: the explicit degree-`order` three-term
polynomial recurrence (`d ← sd·d + sr·(dinv ⊙ r)`, `r ← r − A·d`, `y ← y + d`)
built from the L1 leaf primitives `apply_linop`, `axpby`/`axpbypcz`,
`scal`, and the elementwise diagonal action. Both variants share an identical
primitive *sequence* at L2; only the scalar generator `(α₀, sd_k, sr_k)`
branches — the (c) primitive-sequence axis of `variant-absorption`. The L0
evidence is direct from `palace/linalg/chebyshev.cpp` (both `Mult2` bodies and
both `SetOperator` setups). No dedicated unit test exists (only multigrid
integration coverage), so the operators land **firm on structural signature
and algebraic-law grounds** (every law is a closed-form identity readable
straight off the source recurrence) with the test-coverage gap recorded as a
caveat rather than a status reduction — both forms are direct transcriptions
of fully-specified source code, not literature-inferred. One slice error is
flagged for correction (the slice's `rho_0 = delta/(2*theta)` contradicts the
source `rhop = delta/theta`).

## Proposed changes

```edit:book/src/L1/chebyshev-smoother.md
[create — full content in "Operator content — L1" below]
```

```edit:book/src/L2/chebyshev-iteration.md
[create — full content in "Operator content — L2" below]
```

```edit:book/src/L1/index.md
[add row to Operator dep-map table + Vocabulary-cohort line; diffs below]
```

```edit:book/src/L2/index.md
[add row to Operator dep-map table; diff below]
```

```edit:book/src/SUMMARY.md
[add two chapter entries under the L1 and L2 Parts; diffs below]
```

---

## Operator content — L1 (`book/src/L1/chebyshev-smoother.md`)

```markdown
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

> **Firm-promotion-with-precedent-deviation — integrator to ratify.** This firm
> decision deviates from the nearest two constructed-operator-gate precedents
> (`ksp_solve`, `eigsolve`), at least one of which (`eigsolve`) landed rough-in
> pending dedicated test coverage. The deviation rationale is the
> source-transcription distinction above: every chebyshev law is a syntactic
> identity on fully-specified C++ source (verified exact by the critic), whereas
> `eigsolve`'s rough-in was driven by *literature-inferred convergence
> semantics* that the source alone does not pin down. Chebyshev is additionally
> a bounded fixed-degree polynomial action with closed-form coefficients and
> live integration coverage (`gmg.cpp`, `distrelaxation.cpp`), not a composite
> solve-to-convergence with constructed sum-type status. The integrator should
> ratify firm against the constructed-operator-gate firm-bar, or downgrade to
> rough-in if the precedent is judged to bind; the decision should not be
> settled silently inside the harvest.

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
```

---

## Operator content — L2 (`book/src/L2/chebyshev-iteration.md`)

```markdown
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
action `y + p_order(D⁻¹ A)·(x − A·y)` as one closed-form smoother step. L2 is the
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
shape — the same kernel-plus-driver shape the L2 [`krylov-step`](./krylov-step.md)
catalogs as one of its five pattern instances (`krylov-step.md:7`, citing
`chebyshev.md:354-362`). `chebyshev-iteration` is the concrete L2 entry that the
`krylov-step` variant-axis (3) (polynomial-kind, `op.scalars`) points at.

The HPC element-fused kernels in the L0 source — `ApplyOrder0` (one elementwise
pass computing `d = sr · dinv · r`) and `ApplyOrderK` (one elementwise pass
computing `d = sd · d + sr · dinv · r`, `palace/linalg/chebyshev.cpp:69-78,
:114-123`) — are **transparent fusions** at L2: they compute the same value as
the unfused `scal` + elementwise-product + `axpby` chain modulo standard
floating-point rules for the same operand order. L2 unfolds them into the base
composition and records the fusion as a one-line note.

A cross-cutting prose treatment lives at
[`concepts/chebyshev-iteration`](../concepts/chebyshev-iteration.md). The L2 entry
here is the firm operator definition.

## Signature

```text
chebyshev_iteration
  :: (op: ChebOp[N], x: Tensor[N], y: Tensor[N], initial_guess: Bool)
     -> Tensor[N]
```

Shape contract (bunsen-style; named axes) — identical boundary to L1, with the
internal scalar generator made explicit:

- `op` — `ChebOp[N]` — the constructed smoother. Carries `op.A :
  LinearOperator[N, N]`, `op.dinv : Tensor[N]`, `op.order : Int`, `op.pc_it :
  Int`, and the scalar generator `op.scalars`:
  - **4th-kind**: `scalars(k) = { α₀ = 4/(3·λ_max), sd_k = (2k−1)/(2k+3), sr_k =
    (8k+4)/((2k+3)·λ_max) }` — closed form in `k` and `λ_max`; stateless.
  - **1st-kind**: a `ρ`-threaded recurrence with `ρ₀ = δ/θ` (= `delta/theta`),
    `α₀ = 1/θ`, and for `k ≥ 1`: `ρ_k = 1/(2θ/δ − ρ_{k−1})`, `sd_k = ρ_k·ρ_{k−1}`,
    `sr_k = 2·ρ_k/δ` — threads a scalar state `ρ` across `k`.
- `x`, `y`, `initial_guess` — as in L1.
- result — `Tensor[N]` — the post-sweep accumulator.

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
block that `krylov-step`'s polynomial-method instances factor into.

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
   `palace/linalg/chebyshev.cpp:114-123`) equals the base composition `axpby(sd,
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
- L2 sibling: [`krylov-step`](./krylov-step.md) — `chebyshev-iteration` is the
  concrete L2 entry behind `krylov-step`'s polynomial-method variant-axis (3);
  its `op.scalars` closure is `krylov-step`'s `op.scalars?` field.

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
bodies (`palace/linalg/chebyshev.cpp:191-220, :261-293`), with the
element-fused `ApplyOrder0` / `ApplyOrderK` kernels unfolded into base algebra
and the fusion classified as transparent. The scalar recurrences are exact
closed forms from the source (4th-kind `:215-217`; 1st-kind `:286-288`). Every
algebraic law is a syntactic identity on the source. **Caveat (not a status
reduction)**: no dedicated unit test (multigrid-integration coverage only) —
same justification as the L1 entry.

> **Firm-promotion-with-precedent-deviation — integrator to ratify.** Inherits
> the L1 entry's firm-without-dedicated-test deviation note: ratify firm against
> the constructed-operator-gate firm-bar (source-transcription confidence +
> integration coverage + closed-form fixed-degree action), or downgrade to
> rough-in in lockstep with L1 if the `eigsolve` precedent is judged to bind.

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

- `palace/linalg/chebyshev.cpp:69-78` — `ApplyOrder0` (real): one elementwise
  pass `D[i] = sr · DI[i] · R[i]` (= `scal(sr, elementwise_product(dinv, r))`).
- `palace/linalg/chebyshev.cpp:114-123` — `ApplyOrderK` (real): one elementwise
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
  final `y += d`. (The slice §L2 line 160 `delta/(2·theta)` is in error vs. this
  source `delta/theta`.)
- `palace/linalg/chebyshev.cpp:215-217` — 4th-kind `sd` / `sr` closed forms.
- `palace/linalg/chebyshev.cpp:286-288` — 1st-kind `rho` / `sd` / `sr` recurrence.
- `book/src/L2/krylov-step.md:7` — catalogs `chebyshev.md:354-362` as one of the
  five polynomial-recurrence pattern instances `krylov-step` factors.
- `book/src/spec/slices/chebyshev.md:122-228` — the cycle-001-era L2 slice
  content this entry promotes.
```

---

## index + SUMMARY diffs

### `book/src/L1/index.md` — dep-map row (append after the `bilinear-form` row, before the obstruction rough-ins)

```text
| [`chebyshev-smoother`](./chebyshev-smoother.md) | `(op: ChebSmoother[N], x: Tensor[N], y: Tensor[N], initial_guess: Bool) → Tensor[N]` | `apply_linop` (direct); `spectrum_estimate` (setup-only, opaque) | `firm` (constructed-operator gate; L0: `palace/linalg/chebyshev.cpp`; harvested cycle-012; test-coverage caveat) |
```

### `book/src/L1/index.md` — Vocabulary-cohort "Firm" count + line

Bump "**Firm (8)**" → "**Firm (9)**" and append a bullet:

```text
- [`chebyshev-smoother`](./chebyshev-smoother.md) — pure-functional
  diagonally-scaled Chebyshev polynomial smoother `y' =
  chebyshev_smoother(op, x, y, initial_guess)`; the third constructed-operator
  gate at L1 (after `ksp_solve` and `eigsolve`), and the first that is a
  fixed-degree polynomial *action* rather than a solve-to-convergence. Variant
  (4th-/1st-kind) absorbed into the closure's `scalars` generator.
```

(Working-note bullet recommended for the index, optional for integrator: note
the firm-on-structural-grounds-despite-no-test rationale and the constructed-
operator-gate-but-not-a-solve distinction from `ksp_solve`/`eigsolve`.)

### `book/src/L2/index.md` — dep-map row (append after the `krylov-step` row)

```text
| [`chebyshev-iteration`](./chebyshev-iteration.md) | `(op: ChebOp[N], x: Tensor[N], y: Tensor[N], initial_guess: Bool) → Tensor[N]` | L1: `apply_linop`, `axpy`, `axpby`, `scal`. Concepts: `elementwise-product`, `variant-absorption`, `sequential-obstruction`, `first-iteration-unrolling`. L1 sibling: `chebyshev-smoother`. L2 sibling: `krylov-step`. | `firm` (harvested cycle-012; the concrete L2 entry behind `krylov-step` variant-axis 3; test-coverage caveat) |
```

### `book/src/SUMMARY.md` — chapter entries

Under `# L2 — Algebraic Decompositions`, after the `krylov-step` line:

```text
- [chebyshev-iteration](./L2/chebyshev-iteration.md)
```

Under `# L1 — Mutation-Lifted Forms`, after the `bilinear-form` line:

```text
- [chebyshev-smoother](./L1/chebyshev-smoother.md)
```

---

## Supporting evidence

- **Source path VERIFIED via MCP** (`list_files` + `search_text`): the actual
  Chebyshev source is `palace/linalg/chebyshev.cpp` / `.hpp` (the planner's
  guess was correct, now confirmed — not assumed). Two classes:
  `ChebyshevSmoother<OperType>` (4th-kind) and
  `ChebyshevSmoother1stKind<OperType>` (1st-kind), each a `Solver<OperType>`.
- **3-term recurrence located**: 4th-kind `Mult2` at
  `palace/linalg/chebyshev.cpp:191-220`, 1st-kind at `:261-293`. The
  `d / r / y` recurrence is in both; the element-fused kernels `ApplyOrder0` /
  `ApplyOrderK` are at `:69-78, :81-110` (real/complex order-0) and
  `:114-123, :126-159` (real/complex order-k).
- **Eigenvalue bound located**: `GetLambdaMax` at `:13-27` →
  `linalg::SpectralNorm(comm, DinvA, hermitian)` (power iteration /
  SLEPc-backed spectral norm of `D⁻¹ A`); the real overload (`:18`) passes
  literal `true`, the complex overload (`:27`) passes `A.IsReal()`. 1st-kind
  `sf_min` default
  (Phillips & Fischer eq. 2.24) at `:251-253`.
- **Degree-k loop located**: `for (int k = 1; k < order; k++)` at `:209` (4th)
  and `:283` (1st).
- **No unit test**: `search_text` for `chebyshev` over `reference/palace/test`
  and `find -iname '*cheby*'` both empty — confirms the slice's "No direct unit
  test under test/unit/" note. Behaviour exercised through multigrid
  (`gmg.cpp:52-59`) and distributive-relaxation (`distrelaxation.cpp:21-36`)
  integration only.
- **Consumers VERIFIED**: `gmg.cpp:52-59` and `distrelaxation.cpp:21-36` both
  branch on `cheby_4th_kind` to construct the matching class. The
  `distrelaxation` path calls `B_G->SetInitialGuess(false)` (`:36`), the L1
  law-2 (linear-preconditioner) use site.

## Open questions / caveats

1. **Slice §L2 `rho_0` error.** `book/src/spec/slices/chebyshev.md:160` states
   the 1st-kind initial `rho_0 = delta / (2*theta)`. The L0 source is
   `rhop = delta / theta` (`palace/linalg/chebyshev.cpp:282`) — **no factor of
   2**. Likewise the slice's `alpha_0 = 1/theta` matches the source (`:281`), so
   the discrepancy is isolated to the `rho_0` initialiser. The firm L1/L2 entries
   use the source value (`δ/θ`). **Recommend**: when the slice is further reduced
   (this dispatch unblocks that reduction per the OQ), correct or drop the
   erroneous line. Filed for the integrator to note in the slice-reduction OQ
   residual; not in scope to edit the slice here (one-operator discipline +
   slice is not this dispatch's authority).

2. **`spectrum_estimate` / `SpectralNorm` L1 rough-in.** The setup-side
   `spectrum_estimate(A, dinv)` is cited as an opaque L1 dependency but has no
   firm L1 entry. It is the power-iteration (`linalg::SpectralNorm`) sibling
   tracked under the cycle-008 OQ
   `matrix-weighted-norm-and-bilinear-form-l1-rough-ins` residual cohort. A
   future harvester on `spectrum_estimate` would let `chebyshev-smoother`'s
   setup dependency point at a concrete entry rather than naming it opaque.

3. **L3 + L4 Chebyshev rows not in scope.** The slice carries firm L3
   (partial-obstruction) and L4 (calculus) Chebyshev content
   (`chebyshev.md:229-440`). Per the **identity-lowerings still require both L
   levels** invariant and the **lower-layer shared vocabulary takes priority**
   directive, `L3/chebyshev-iteration` and `L4/chebyshev-smoother` are eligible
   future harvester targets (the L4 form is already drafted in the slice with
   `ChebOp<E, S>` typing and `foldM`/`forM_` monadic shape). Recommend a
   cycle-012+ OQ to schedule them; the slice cannot fully reduce until L3/L4 are
   also lifted. Out of scope for this 2-operator dispatch.

4. **Dead complex transpose kernels.** The conjugate-`dinv` transpose
   specialisations (`palace/linalg/chebyshev.cpp:101-110, :150-159`) are
   unreachable under the symmetric wiring (`MultTranspose2 → Mult2`). Recorded as
   a non-law caveat in the L1 entry (law 3); flagged in the slice's Open
   questions already. No action needed unless an asymmetric variant appears.

5. **L1>L0 + L2>L1 lowering themes not authored.** This dispatch firms the L1
   and L2 *operator* rows; the forward lowering themes
   (`L1-L0/chebyshev-smoother-mutation-rotation` — the `Mult2` output-arg /
   workspace mutation rotation; `L2-L1/chebyshev-iteration-fusion` — the
   `ApplyOrder0`/`ApplyOrderK` element-fusion theme) are abstractor work, not in
   scope here. Noted for the planner. The L1 entry references the (forthcoming)
   L1>L0 theme in prose without linking a non-existent file.

6. **Layer-intro refresh.** `book/src/L1/index.md` "Vocabulary cohort" prose
   describes a "Firm (8)" cohort and motifs; adding `chebyshev-smoother` as the
   ninth firm operator (and the third constructed-operator gate, first
   polynomial-*action* gate) may warrant a motif-prose touch by the
   layer-intro-author beyond the mechanical row+count bump proposed here.
   `book/src/L2/index.md` Working Notes similarly may want a note that
   `chebyshev-iteration` is the second firm L2 operator and the concrete entry
   behind `krylov-step` variant-axis 3. Flagged for layer-intro-author; not
   done here (not harvester authority).
```

