---
layer: L1
operator: bilinear-form
firmness: firm
rank: firm
edges:
  depends-on:
    - L1/dot
    - L1/apply_linop
    - L1/matrix-weighted-norm
  reference:
    - L1-L0/bilinear-form-mutation-rotation
variant_axes:
  - precision-mode
  - output-arg-pattern
  - M-symmetry-property
  - parallel-wrapper
---

# bilinear-form

Mutation-free matrix-weighted inner-product reduction: `α = xᴴ M y` for a
vector `x`, a linear operator `M`, and a vector `y`. The matrix-weighted
generalisation of [`dot`](./dot.md) at L1; the operator-as-metric primitive
that underlies energy products, Poynting-power boundary integrals, and Newton
denominators in nonlinear eigenvalue methods.

## Context

`bilinear-form` lifts Palace's `linalg::Dot(comm, x, A, y)` free-function
overload pair (declared at `palace/linalg/operator.hpp:386-394`, defined at
`palace/linalg/operator.cpp:621-639`) to a single pure-functional
matrix-weighted reduction operator. The L0 declaration set names two overloads
that differ only in the element-type of the weight operator `A` (`Operator`
for real-valued operators against complex vectors; `ComplexOperator` for
complex-valued operators against complex vectors); both compute the same L1
semantic object. The element-type split at L0 is variant absorption at L1 —
see *Variant axes*.

The L0 implementations allocate a workspace `ComplexVector Ax(A.Height())`
internally, write `A · x` into it, and return `dot(Ax, y)` (using L1
vocabulary; the L0 call is `Dot(comm, Ax, y)`). The internal-workspace
allocation is the Category 4 ("synthetic workspace") instance of
[`mutable-workspace-pattern`](../L0/mutable-workspace-pattern.md) per the L0
chapter classification. At L1 the workspace disappears (pure functional
threading); the L1>L0 lowering theme reintroduces it.

`bilinear-form` is **firm** (promoted from `rough-in` cycle-095, the
bilinear-form-firm-flip-and-cascade-wave; firmability DISCHARGED by the
cycle-092 `lowering-verifier` probe — see *Status* below). The structural
signature is well-anchored at L0 and the algebraic laws are inherited cleanly
from the firm L1 dependencies `dot`, `apply_linop`, and `matrix-weighted-norm`;
the formerly-cited narrow-variant-axis-coverage gate was judged REDUNDANT under
the firm-on-positive-structure escape (the two surfaced use sites are the only
matrix-weighted `Dot` call sites in the tree, and the one unexercised shape —
real-`M`-real-`y` `xᵀ M y` — is not surfaced by Palace at all). *(An earlier
draft listed a second gating reason — an alleged L0 comment-vs-implementation
conjugation disagreement — that was based on a misreading of the L0 free-function
`linalg::LocalDot` convention. The L0 source is self-consistent: see Status and
the `bilinear-form-conjugation-convention-anchor` OQ for the verification.)*

A cross-cutting prose treatment is not yet authored at `concepts/`; if/when
the operator's use pattern becomes thick enough, a concept page following the
[`dot`](../concepts/dot.md) precedent would be appropriate.

## Signature

```
bilinear_form :: (x: Tensor[M], M: LinearOperator[M, N], y: Tensor[N]) -> Scalar
bilinear_form(x, M, y) = xᴴ M y
```

Shape contract (bunsen-style, named axes):

- `x` — `Tensor[M]` — read-only. Axis `M` matches the codomain of `M`.
- `M` — `LinearOperator[M, N]` — read-only. The matrix-weight; a linear map
  from a domain space of axis `N` to a codomain space of axis `M`. (Slight
  notational overload: the type parameter `M` and the operator name `M` are
  not the same `M` — the codomain axis is named `M` after Palace's
  `Operator::Height()`; the operator value is named `M` after the standard
  mathematical notation for a matrix-weight.)
- `y` — `Tensor[N]` — read-only. Axis `N` matches the domain of `M`.
- result — `Scalar` — element type follows the rule below.

Element-type rule:

| `x` element type | `M` element type | `y` element type | result |
|---|---|---|---|
| `complex` | `real`    | `complex` | `complex` |
| `complex` | `complex` | `complex` | `complex` |

The real-`x` / real-`M` / real-`y` case is **not surfaced by Palace** through
the matrix-weighted `linalg::Dot` overload set — only the complex-vector
overloads exist (the real-vector counterpart would be `xᵀ M y` and is not
named in Palace's free-function namespace; see *Variant axes* and *Open
questions*).

`LinearOperator[M, N]` is the opaque-operator type from
[`apply_linop`](./apply_linop.md); its internal representation
(sparse/dense/matrix-free/composition/multigrid/wrapped/parallel) is
collapsed at L1 to the linear-map interface plus the domain/codomain axes.

## Semantics

`bilinear_form(x, M, y)` returns the matrix-weighted inner product `xᴴ M y`
— the conjugate-linear-in-`x`, linear-in-`y`, linear-in-`M` reduction to a
scalar. The L1 form is pure functional: same `x`, same `M`, same `y`, same
return value.

**Specialisation to `dot`**: when `M` is the identity operator `I` (axis
`N = M`), `bilinear_form(x, I, y) = xᴴ I y = xᴴ y = dot(x, y)`. This is
the algebraic statement that `dot` is the special case `M = I` of
`bilinear-form`. In the dep-map, both `dot` and `bilinear-form` are siblings
at L1; the specialisation is captured by this algebraic identity (per the L1
overlay invariant "Subsumption-as-identity rather than dependency"), not by a
dep-map edge from `bilinear-form` to `dot`.

**Composition into `apply_linop` + `dot` (informational)**: as an L1>L0
lowering preview only, the natural unfolding `bilinear_form(x, M, y) =
dot(x, apply_linop(M, y))` recasts the reduction as "apply `M` to `y`, take
`dot` with `x`". This unfolding is **not** the L1 definition of the operator
— the L1 definition is the closed-form `xᴴ M y` — but it is the natural
shape of the L1>L0 lowering and is recorded here so that callers can see the
relationship without scrolling to a lowering theme.

The Palace L0 implementation realises an equivalent unfolding with a swapped
argument order that matches the L0 free-function's **second-argument-conjugation**
convention. Concretely: L0 computes `Ax = A · x` into a workspace, then calls
`linalg::Dot(comm, Ax, y)`. Because the free-function `linalg::Dot` conjugates
its **second** argument (per `palace/linalg/vector.cpp:674-685` and as
documented at `book/src/L1/dot.md:43, 104-105`), `linalg::Dot(comm, Ax, y) =
yᴴ · Ax = yᴴ A x`, which matches the L0 source comment at
`palace/linalg/operator.hpp:386` ("Compute the bilinear form inner product
yᴴ A x"). The L0 source is self-consistent.

The L1>L0 lowering between the closed-form `xᴴ M y` (L1) and `linalg::Dot(comm,
A·x, y) = yᴴ A x` (L0) is **conjugation-asymmetric**: at L1 the conjugated
argument is named first (matching `dot`'s L1 convention); at L0 the conjugated
argument is the second-position call argument. The two are related by the
identity `xᴴ M y = conj(yᴴ Mᴴ x)` — for a Hermitian `M` (law 7), `xᴴ M y =
conj(yᴴ M x)`. The L1>L0 lowering theme will name this asymmetry explicitly;
mechanically, the L1 form `bilinear_form(x, M, y) = xᴴ M y` lowers either to
`linalg::Dot(comm, apply_linop(M, y), x)` (which gives `xᴴ M y` directly, using
the L0 free-function's second-argument-conjugation) or, equivalently with an
argument swap, to `conj(linalg::Dot(comm, apply_linop(M, x), y))` (which gives
`conj(yᴴ M x) = xᴴ Mᴴ y`; matches when `M` is Hermitian, but in general
requires an outer `conj` to recover `xᴴ M y`). The shape Palace itself uses is
the latter (`Ax = A·x`, then `Dot(comm, Ax, y)` → `yᴴ A x = conj(xᴴ Mᴴ y) =
conj(...)`, which for a Hermitian `M` collapses to `conj(xᴴ M y)`; the
non-Hermitian witness `Atn` shows Palace genuinely computes `yᴴ A x` and not
`xᴴ A y`). The L1 convention's choice to name `x` first is a free choice; the
lowering reconciliation is mechanical.

**Conjugation convention**: the L1 signature names `x` (the first vector
argument) as the conjugated argument and `y` (the second vector argument) as
the linear argument, matching the conjugation convention of [`dot`](./dot.md)
(conjugate-linear in first, linear in second). This is the convention chosen
**by the L1 specification** to give a clean `dot(x, y) = bilinear_form(x, I,
y)` specialisation. The Palace L0 free-function form uses second-argument-
conjugation (as documented at `book/src/L1/dot.md:43, 104-105` for the
sister operator); the L1>L0 lowering theme reconciles the two conventions
mechanically (see the composition note above). **There is no L0 ambiguity:**
the comment `yᴴ A x` at `palace/linalg/operator.hpp:386` and the
implementation at `palace/linalg/operator.cpp:621-639` both express the
same form `yᴴ A x`.

**Reduction-tree non-associativity is load-bearing** in the same CLAUDE.md
sense as [`dot`](./dot.md): the underlying scalar accumulation is the same
non-associative IEEE-754 floating-point summation, and the matrix-weight
application adds a second non-associative step (the operator's internal
quadrature / SpMV reduction). Both contribute to bit-level non-reproducibility
under reduction-order changes; mathematical laws hold exactly, floating-point
realisations are approximate. Inherits this property from its two
dependencies.

**The MPI collective is not in the L1 signature** (single-rank scope per
CLAUDE.md). The L0 `linalg::Dot(comm, x, A, y)` takes an `MPI_Comm` and
internally combines the per-rank kernel with `Mpi::GlobalSum`; at L1 the
collective is folded into the L1>L0 lowering theme.

## Algebraic laws

The laws below hold; absences are deliberate. Laws are stated for the L1
convention `bilinear_form(x, M, y) = xᴴ M y` (conjugate-linear in `x`, linear
in `y`, linear in `M`).

**Linearity laws (complex element-type, general `M`):**

1. **Conjugate-linearity in `x`**: `bilinear_form(α·x₁ + x₂, M, y) =
   conj(α)·bilinear_form(x₁, M, y) + bilinear_form(x₂, M, y)`. Inherited
   from `dot`'s conjugate-linearity in the first argument.
2. **Linearity in `y`**: `bilinear_form(x, M, α·y₁ + y₂) =
   α·bilinear_form(x, M, y₁) + bilinear_form(x, M, y₂)`. Inherited from
   `dot`'s linearity in the second argument and `apply_linop`'s linearity.
3. **Linearity in `M` (operator-side bilinearity)**: `bilinear_form(x, α·M₁
   + M₂, y) = α·bilinear_form(x, M₁, y) + bilinear_form(x, M₂, y)`. Follows
   from `apply_linop`'s operator-side linearity (laws 5 and 6 of
   `apply_linop`).
4. **Zero-vector annihilation (either vector)**: `bilinear_form(0, M, y) =
   bilinear_form(x, M, 0) = 0`. Follows from laws 1 and 2 with the
   zero-scalar coefficients.
5. **Zero-operator annihilation**: `bilinear_form(x, 0, y) = 0` where `0`
   is the zero operator. Follows from law 3 with `α = 0` and `M₂ = 0`.
6. **Identity-weight specialisation**: `bilinear_form(x, I, y) = dot(x, y)`
   for `I : V → V` the identity on a space with axis `N = M`. This is the
   *defining* relationship between `bilinear-form` and `dot` — the operator
   is named "bilinear-form" precisely because it is the matrix-weighted
   generalisation of `dot`.

**Symmetry laws (depend on `M`-symmetry — see Variant axes):**

7. **Hermitian-`M` Hermitian symmetry**: when `M` is Hermitian (i.e.
   `Mᴴ = M`), `bilinear_form(x, M, y) = conj(bilinear_form(y, M, x))`.
   This is the matrix-weighted analogue of `dot`'s Hermitian symmetry.
   Recorded as a conditional law because Palace's surfaced use sites
   exercise both Hermitian-`M` (the boundary mass matrix `Bttr` in
   `palace/models/boundarymodeoperator.cpp:85`) and non-Hermitian-`M`
   (the inhomogeneous boundary coupling `Atn` in
   `palace/models/boundarymodeoperator.cpp:90` — a complex wrapper around
   a non-symmetric MFEM HypreParMatrix).
8. **Hermitian-`M` positive semi-definite at `y = x` (and `M` is SPD)**:
   when `M` is symmetric positive-definite, `bilinear_form(x, M, x) ∈ ℝ`
   and `bilinear_form(x, M, x) ≥ 0`, with equality iff `x = 0` (in exact
   arithmetic). This is the energy-norm-squared identity:
   `nrm2_M(x)² = bilinear_form(x, M, x)`, anchoring the future
   `nrm2_B`-weighted operator (cycle-008 OQ `nrm2-B-weighted-energy-norm-
   harvest`; sibling-dispatch #5 in cycle-010 wave-1).

**Laws that explicitly do not hold:**

- **General-`M` symmetry**: `bilinear_form(x, M, y) ≠ bilinear_form(y, M, x)`
  for non-symmetric `M`. The Poynting-power use site at
  `palace/models/boundarymodeoperator.cpp:90` is a direct witness:
  `linalg::Dot(comm, en, Atn, et)` with `Atn` non-symmetric returns a
  different value than `linalg::Dot(comm, et, Atn, en)` would.
- **Cauchy–Schwarz strictness in floating point**:
  `|bilinear_form(x, M, y)|² ≤ bilinear_form(x, M, x) · bilinear_form(y, M, y)`
  holds mathematically when `M` is SPD, but can fail by ULP-level amounts due
  to summation-ordering noise (inherited from `dot`'s floating-point caveat
  plus `apply_linop`'s reduction-tree non-associativity for matrix-free
  representations).
- **Associativity of the underlying reductions in floating point**: inherited
  from both `dot` and `apply_linop`. Different summation orders give
  different bit-level results.

## Dependencies

- [`apply_linop`](./apply_linop.md) — for the `M · y` application step (or
  `M · x`, depending on which unfolding the L1>L0 lowering chooses).
- [`dot`](./dot.md) — for the final `xᴴ (...)` reduction step.

Both dependencies are L1-internal (sister leaf operators at L1). The natural
L1>L0 lowering decomposes `bilinear_form(x, M, y)` into one `apply_linop`
call followed by one `dot` call; the workspace-internal-allocation pattern at
L0 (Category 4 of [`mutable-workspace-pattern`](../L0/mutable-workspace-pattern.md))
is the operator-applied intermediate `Ax`.

Future `nrm2_B`-weighted operator (cycle-010 wave-1 sibling dispatch #5,
addressing cycle-008 OQ `nrm2-B-weighted-energy-norm-harvest` and the
sibling OQ `matrix-weighted-norm-and-bilinear-form-l1-rough-ins` — BOTH
halves of which are now resolved: the `matrix-weighted-norm` half promoted to
`firm` at cycle-091, and the `bilinear-form` half promoted to `firm` at
cycle-095 (this dispatch, the firm-flip-and-cascade wave)) will likely
depend on `bilinear-form` via `nrm2_B(x, B) = √bilinear_form(x, B, x)` when
`B` is SPD (law 8). That is the L1 statement of the energy norm.

## Variant axes

`bilinear-form` has four orthogonal variant axes at L1:

- **precision-mode**: the working precision of the underlying reductions.
  Inherited from `dot` and `apply_linop`. Palace exposes one precision
  (`double` for real, `std::complex<double>` for complex) through the
  current L0 surface; the axis is recorded because precision-mode is the
  canonical first variant axis at L1 across the BLAS-1 cohort.
- **output-arg-pattern**: at L0, `linalg::Dot(comm, x, A, y)` returns its
  result by value (return register / scalar). There is no "output-arg" form
  in Palace's matrix-weighted surface — unlike `apply_linop` (which has both
  `Mult` and `AddMult` accumulating variants), `bilinear-form` has only the
  return-by-value form. The axis is recorded for parallel-structure with
  other L1 operators; at L1 the only realised mode is `return`.
- **M-symmetry-property**: `hermitian` | `non-symmetric`. This axis is
  **material** at L1 because law 7 (Hermitian symmetry) and law 8 (positive
  semi-definiteness at `y = x`) hold conditionally on `M`'s symmetry
  properties. Downstream callers either know `M` is Hermitian (Poynting
  boundary mass `Bttr` at `palace/models/boundarymodeoperator.cpp:85`, which
  is symmetric by construction) or do not (the cross-coupling `Atn` at
  line 90, the Newton-step linear-operator weight in
  `palace/linalg/nleps.cpp:675`). The L1 entry does not branch by
  M-symmetry; the algebraic laws guard the symmetric cases conditionally.
- **parallel-wrapper**: at L0, the underlying operator may or may not be
  parallel-wrapped (`ParOperator` / `ComplexParOperator`); the matrix-weighted
  `linalg::Dot` takes a `Vector` and dispatches through whatever `Operator`
  reference it gets. Per CLAUDE.md single-rank scope, parallel-wrapped types
  are read as their single-rank equivalents at L1. The axis is recorded so
  that L1>L0 lowering correctly classifies the workspace allocation and
  collective-reduction step.

Collapsed (absorbed) axes:

- **element-type of `M`**: `real` | `complex`. At L0 these are separate
  overloads (`Operator` weight at `palace/linalg/operator.hpp:388-389`;
  `ComplexOperator` weight at `palace/linalg/operator.hpp:393-394`). At L1
  these collapse to one operator parameterised by element type. The real-`M`
  overload's implementation splits `x` into real/imaginary parts and applies
  `A` to each separately (`palace/linalg/operator.cpp:625-628`); the
  complex-`M` overload applies `A` to `x` directly (`palace/linalg/operator.cpp:635`).
  This is an L1>L0 lowering concern, not an L1 variant axis.
- **operator-representation of `M`**: absorbed into the opaque
  `LinearOperator` type from [`apply_linop`](./apply_linop.md). See that
  operator's *Variant axes* §"Collapsed".

## Applicability conditions

- `M` must be a linear operator. (Nonlinear weights are not supported and not
  meaningful for `xᴴ M y`.)
- `M`'s codomain axis must match `x`'s length axis (`M`).
- `M`'s domain axis must match `y`'s length axis (`N`).
- **No SPD requirement on `M`.** The operator is well-defined for any linear
  `M`. Algebraic laws 7 (Hermitian symmetry) and 8 (positive semi-definiteness
  at `y = x`) hold *conditionally* on `M`'s symmetry properties; the operator
  itself does not require them. This distinguishes `bilinear-form` from the
  forthcoming `nrm2_B`-weighted energy-norm operator (sibling dispatch #5),
  which requires `B` SPD because the square-root step demands a non-negative
  real argument.
- The element types of `x`, `M`, and `y` must be compatible per the table in
  *Signature*.

## Status

`firm` (promoted from `rough-in (lower-layer-shared-vocabulary,
cycle-010-wave-1)` at **cycle-095**, the `bilinear-form-firm-flip-and-cascade-wave`,
on the **firm-on-positive-structure escape** — DISCHARGE established by the
cycle-092 `lowering-verifier` probe, `verified_against:` block below). The
structural signature is anchored at L0 (`palace/linalg/operator.hpp:385-394`,
`palace/linalg/operator.cpp:621-639`), and the laws are inherited cleanly from
the firm L1 dependencies `dot` (`book/src/L1/dot.md:100`), `apply_linop`
(`book/src/L1/apply_linop.md:87`), and `matrix-weighted-norm`
(`book/src/L1/matrix-weighted-norm.md:110`, firm c091).

**Firmability DISCHARGED (cycle-092 dischargeability probe; `verified_against:`
block below) and ENACTED (cycle-095, this dispatch).** A scoped
`lowering-verifier` probe (the c088/c089 `matrix-weighted-norm` pattern) judged
that the **firm-on-positive-structure escape** (CLAUDE.md §Methodology
invariants, the `rough-in (test-coverage-bounded)` bullet) APPLIES to this
operator; cycle-095 enacts the flip:

1. **Laws 1-6 (`:182-201`) are syntactic read-offs over firm constituents.**
   They are pure linearity / annihilation / identity-specialisation —
   `bilinear_form(x, M, y) = dot(x, apply_linop(M, y))` is a syntactic
   composition of the firm `dot` (`book/src/L1/dot.md:100` firm) and firm
   `apply_linop` (`book/src/L1/apply_linop.md:87` firm) laws, with **NO
   inner-product-norm theorem content**. This is materially cleaner than
   `matrix-weighted-norm` was (whose gating laws WERE norm-axiom theorems
   — triangle / Cauchy–Schwarz / parallelogram — needing two probes c088+c089);
   `bilinear-form` has none. The escape promotes laws that are
   syntactic-identity content on fully-specified positive source even with no
   surrounding test (the `apply_linop` / `solve_family` c086 /
   `eigenfreq_qfactor_reduce` c082 / `sparameter_reduce` c083 /
   `matrix-weighted-norm` c091 precedents).
2. **Laws 7-8 (`:205-220`) are M-symmetry-CONDITIONAL with both witnesses
   on-disk.** Law 7 (Hermitian symmetry under `Mᴴ = M`) and law 8 (PSD at
   `y = x` for SPD `M`) are premise-guarded conditional identities; both
   branches are positively witnessed — Hermitian `Bttr`
   (`palace/models/boundarymodeoperator.cpp:85`, a `y = x` form) and
   non-Hermitian `Atn` (`palace/models/boundarymodeoperator.cpp:90`). Law 8's
   sole positivity content is the SPD-diagonal `xᴴ B x ≥ 0`, which the firm
   `matrix-weighted-norm` sibling (c091) already discharged via its
   structure-side probe c088 — it is inherited, not an independent gate.
3. **The narrow-variant-axis-coverage gate is REDUNDANT under the escape.**
   The two surfaced use sites are the only matrix-weighted `Dot` call sites in
   the whole tree (`grep` confirms exactly 2: `boundarymodeoperator.cpp:85`/`:90`),
   and no `test/unit/*` exercises the 4-arg overload (the direct-test route is
   genuinely absent — the same situation as `matrix-weighted-norm`'s gate (a),
   which the batch-28 meta-phase judged REDUNDANT). The one shape the coverage
   gate names — real-`M`-real-`y` `xᵀ M y` — is **not surfaced by Palace at
   all** (`:85-89`); a test of it cannot exist and would only confirm a
   hypothetical extension. Cauchy–Schwarz at `y = x` is a floating-point
   strictness **non-law** (`:229-234`) already inherited from `dot` +
   `apply_linop`; a test would only re-confirm an already-anchored property.

**The flip is ENACTED in cycle-095** (the `bilinear-form-firm-flip-and-cascade-wave`):
the c092 probe was the gate-TEST (per the c088/c089 discipline — the probe
establishes firmability, the flip is a separate gated wave), and cycle-095 lands
the firm flip together with the coupled `gram_reduce` firm re-judgment (D3), the
4-column (capacitance/inductance/electrostatic/magnetostatic) unblock (D4), and
the whole-book cross-reference re-anchor (D2). What the probe established and this
dispatch enacts: the verb IS firm via the escape; nothing structural blocks it;
the residual coverage gate is redundant.

*(Repair note — cycle-010 critic pass: an earlier draft listed a second
gating reason (an alleged L0 comment-vs-implementation conjugation
disagreement). That claim was based on a misreading of the L0 free-function
`linalg::LocalDot` convention. Verified at `palace/linalg/vector.cpp:674-685`
that the free-function conjugates the second argument, yielding `yᴴ x`;
this is already documented at `book/src/L1/dot.md:43, 104-105`. The L0
source `linalg::Dot(comm, A·x, y) = yᴴ A x` matches the L0 comment at
`palace/linalg/operator.hpp:386`. The false gating reason was removed; the
single remaining gating reason (narrow variant-axis coverage) was then judged
REDUNDANT under the firm-on-positive-structure escape (cycle-092 probe), and
the verb was promoted to firm at cycle-095.)*

## L1 vs L0 distinction

- **L0**: two free-function overloads `linalg::Dot(comm, x, A, y)` with
  `Operator` or `ComplexOperator` weight type. Each allocates a workspace
  `ComplexVector Ax(A.Height())` internally (Category 4 synthetic workspace
  per [`mutable-workspace-pattern`](../L0/mutable-workspace-pattern.md)),
  applies `A` to `x` (splitting into real/imaginary parts for the real-`A`
  overload), then calls the free-function `linalg::Dot(comm, Ax, y)` which
  combines the per-rank kernel with `Mpi::GlobalSum`. Element-type of `M`
  is a dispatched axis; element-type of `x` and `y` is fixed at
  `ComplexVector` for both overloads. **Conjugation handedness**: the L0
  free-function `linalg::Dot` conjugates its **second** argument (per
  `palace/linalg/vector.cpp:674-685`; see also `book/src/L1/dot.md:43,
  104-105` for the documented L0/L1 conjugation asymmetry), so
  `linalg::Dot(comm, A·x, y) = yᴴ A x`, matching the L0 comment at
  `palace/linalg/operator.hpp:386`.
- **L1**: pure functional reduction `α = bilinear_form(x, M, y) = xᴴ M y`.
  No MPI collective in the signature. No workspace allocation in the
  signature. Element-type of `M` is variant-absorbed (one L1 operator
  parameterised by element type). Operator-representation of `M` is
  variant-absorbed into the opaque `LinearOperator` type. **Conjugation
  handedness**: fixed by the L1 specification to match
  [`dot`](./dot.md)'s L1 convention (conjugate-linear in the first vector
  argument). The L1>L0 lowering theme inherits the L0/L1 conjugation
  asymmetry documented in `dot.md` — Palace's L0 free-function form
  conjugates the second argument, so the lowering inserts either an
  argument-position swap or an outer `conj` depending on which L1>L0
  composition shape is chosen (see *Semantics* §"Composition into
  `apply_linop` + `dot`" for the explicit identities).

## Evidence

- `palace/linalg/operator.hpp:385-394` — two `linalg::Dot` overload
  declarations for the matrix-weighted bilinear-form inner product (real-`A`
  weight at line 388-389, complex-`A` weight at line 393-394). Comment at
  line 386 documents the intended form as `yᴴ A x` for both overloads.
- `palace/linalg/operator.cpp:621-629` — real-`A` overload implementation:
  splits `x` into `Real()` / `Imag()` parts, applies `A` to each part, returns
  `linalg::Dot(comm, Ax, y)`.
- `palace/linalg/operator.cpp:631-639` — complex-`A` overload implementation:
  applies `A` to `x` directly via `A.Mult(x, Ax)`, returns `linalg::Dot(comm,
  Ax, y)`. Combined with the free-function `linalg::LocalDot` body at
  `palace/linalg/vector.cpp:674-685` (which conjugates the **second**
  argument, returning `yᴴ x`), the L0 implementation returns
  `linalg::Dot(comm, Ax, y) = yᴴ · Ax = yᴴ A x`, **matching** the L0 comment
  at `palace/linalg/operator.hpp:386`. The L0/L1 conjugation asymmetry that
  this composition relies on is documented at `book/src/L1/dot.md:43,
  104-105`.
- `palace/models/boundarymodeoperator.cpp:85` — Hermitian-`M` use site:
  `linalg::Dot(comm, et, *Bttr, et)` computing the Poynting-power
  contribution from the boundary mass matrix `Bttr` (a symmetric MFEM
  HypreParMatrix). Argument structure: `bilinear_form(et, Bttr, et)`
  evaluates the energy-norm-squared of the transverse field `et` against
  the mass-matrix weight (a special case of law 8 anchoring the Cauchy–
  Schwarz tight case).
- `palace/models/boundarymodeoperator.cpp:90` — non-Hermitian-`M` use site:
  `linalg::Dot(comm, en, Atn, et)` computing the cross-coupling
  contribution from the inhomogeneous boundary operator `Atn` (a
  `ComplexWrapperOperator` around a non-symmetric MFEM `HypreParMatrix`).
  Witness for the asymmetric-`M` case where law 7 (Hermitian symmetry)
  does not hold.
- `palace/linalg/nleps.cpp:675` — Newton denominator use site:
  `linalg::Dot(GetComm(), w, w0)` is the unweighted form; the surrounding
  context computes weighted variants by composing `apply_linop` with `dot`
  rather than calling the matrix-weighted `Dot` overload directly. Witness
  that callers sometimes inline the L1>L0 unfolding manually.
- `book/src/L0/linalg-operator-file.md` §"linalg:: free functions" (lines
  30-35) and §"Why this file pair matters" (line 73) — L0 chapter naming
  the matrix-weighted `Dot` overloads as the natural L0 anchor for an L1
  matrix-weighted bilinear-form operator. The L0 chapter and this entry both
  use the slug `bilinear-form` (the cycle-026 naming sweep repointed the
  former candidate slug `dot_bilinear` to `bilinear-form` throughout). No slug
  discrepancy remains.
- `book/src/L1/dot.md` — the firm dependency for the final inner-product
  step; defines the conjugation convention this entry inherits.
- `book/src/L1/apply_linop.md` — the firm dependency for the matrix-weight
  application step; defines the opaque-operator type.
- `book/src/L1/index.md` — dep-map this entry adds a row to.
- `scaffolding/open-questions.md` §`matrix-weighted-norm-and-bilinear-form-
  l1-rough-ins` (cycle-008, layer-intro-author) — the cycle-008 OQ that
  motivates this harvest.
- `scaffolding/priorities.md` #17 `lower-layer-shared-vocabulary-priority`
  (cycle-009 meta-phase) — the priority that schedules this dispatch.

```yaml
verified_against:
  - citation: palace/linalg/operator.cpp:621-639
    verdict: supports
    audited_at: 2026-06-04T065200Z
    note: both matrix-weighted Dot overload bodies (real-A split real/imag + Dot(comm,Ax,y); complex-A direct A.Mult + Dot(comm,Ax,y)) confirmed verbatim on disk; the closed-form xᴴ M y = dot(x, apply_linop(M, y)) is a syntactic composition of firm dot + firm apply_linop
  - citation: palace/linalg/operator.hpp:385-394
    verdict: supports
    audited_at: 2026-06-04T065200Z
    note: two decls + the yᴴ A x comment (line 386) confirmed verbatim; matches the impl, no comment-vs-impl conjugation ambiguity
  - citation: palace/models/boundarymodeoperator.cpp:85
    verdict: supports
    audited_at: 2026-06-04T065200Z
    note: Hermitian-M y=x witness Dot(comm, et, *Bttr, et) confirmed on disk; anchors law 7 Hermitian branch + law 8 PSD-at-y=x diagonal case
  - citation: palace/models/boundarymodeoperator.cpp:90
    verdict: supports
    audited_at: 2026-06-04T065200Z
    note: non-Hermitian-M witness Dot(comm, en, Atn, et) with Atn a ComplexWrapperOperator over a non-symmetric HypreParMatrix confirmed on disk; anchors law 7 non-Hermitian branch (the general-M-asymmetry non-law)
  - citation: book/src/L1/dot.md:65-66
    verdict: supports
    audited_at: 2026-06-04T065200Z
    note: dot firm Hermitian-symmetry (law 6) + conjugate-linearity-left (law 7) are the inherited sources for bilinear-form laws 1 and 7; dot Status firm confirmed at dot.md:100
  - citation: book/src/L1/apply_linop.md:50-55
    verdict: supports
    audited_at: 2026-06-04T065200Z
    note: apply_linop firm linearity (law 1) + operator-side linearity (laws 5,6) are the inherited sources for bilinear-form laws 2 and 3; apply_linop Status firm confirmed at apply_linop.md:87
  - citation: book/src/L1/matrix-weighted-norm.md:108-115
    verdict: supports
    audited_at: 2026-06-04T065200Z
    note: matrix-weighted-norm firm c091 is the SPD diagonal sibling bilinear_form(x,B,x); its discharge of the same 4-arg-overload no-test gate (a) as REDUNDANT under the firm-on-positive-structure escape is the directly-applicable prior for law 8 PSD content
  - citation: book/src/L1/bilinear-form.md:182-201
    verdict: supports
    audited_at: 2026-06-04T065200Z
    note: laws 1-6 are pure linearity/annihilation/identity-specialisation - syntactic read-offs over firm dot + apply_linop with NO norm-axiom theorem content; the firm-on-positive-structure escape applies directly
  - citation: book/src/L1/bilinear-form.md:205-220
    verdict: partially-supports
    audited_at: 2026-06-04T065200Z
    note: laws 7,8 are M-symmetry-CONDITIONAL with both witnesses on-disk (Bttr Hermitian, Atn non-Hermitian); law 8 positivity content is the SPD diagonal already discharged by the firm matrix-weighted-norm sibling - conditional, not an independent gate
```
