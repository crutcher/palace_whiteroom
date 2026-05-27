---
agent: harvester
invoked_at: 2026-05-27T215427Z
scope: L1 operator: bilinear-form (rough-in)
status: integrated
integrated_at: 2026-05-27T230802Z
integration_commit: 30119eb
integration_notes: Applied via integrator-per-report pass 4 of cycle-010 (wave-2 sibling to pass 3 matrix-weighted-norm). **First cycle-010 citation-validity FAIL repaired cleanly** — the original draft mis-read L0 conjugation convention; repairer applied 9 coordinated in-place edits correcting the analysis; false OQ `bilinear-form-conjugation-convention-anchor` closed `resolved-by-correction` in-CYCLE (NOT propagated to ledger). 3 new OQs promoted (`bilinear-form-real-vector-coverage-gap`, `bilinear-form-slug-name-coordination`, `bilinear-form-variant-axis-test-coverage`). Closes priority #17 second target. L1 cohort post-cycle-010: 8 firm + 3 rough-in (now including bilinear-form). **Landed with 8-field frontmatter** per the cycle-010 wave-1 L3 precedent — diverges from sibling matrix-weighted-norm (no frontmatter) and existing L1 cohort convention; future-normalization candidate forwarded to cycle-012 meta-phase batch.
inputs:
  - scaffolding/open-questions.md §matrix-weighted-norm-and-bilinear-form-l1-rough-ins (cycle-008, layer-intro-author)
  - scaffolding/priorities.md #17 lower-layer-shared-vocabulary-priority
  - book/src/L1/dot.md (firm dependency; M = I special case)
  - book/src/L1/apply_linop.md (firm dependency)
  - book/src/L0/linalg-operator-file.md §"linalg:: free functions"
  - palace/linalg/operator.hpp:385-394 (declarations)
  - palace/linalg/operator.cpp:621-639 (definitions)
  - palace/models/boundarymodeoperator.cpp:85-90 (use site: Poynting power)
  - palace/linalg/nleps.cpp:675 (use site: Newton step denominator)
---

# CYCLE: Formalize bilinear-form at L1 (rough-in)

## Summary

Rough-in a new L1 operator `bilinear-form` — the matrix-weighted inner product
`xᴴ M y`. This generalises the existing firm L1 `dot` operator (which is the
M = I special case) by inserting a linear-operator weight between the two
vectors. The Palace L0 anchor is the `linalg::Dot(comm, x, A, y)` free-function
overload pair declared at `palace/linalg/operator.hpp:386-394` and defined at
`palace/linalg/operator.cpp:621-639`. Both overloads (real-`A` and complex-`A`)
compute the same L1 semantic object; the element-type split at L0 is variant
absorption at L1. The operator lands as **rough-in** rather than firm for one
reason recorded in *Open questions*: Palace's two surfaced use sites
(Poynting-power boundary integral, NLEPS Newton denominator) are too narrow to
exhaust the variant-axis coverage that a firm entry needs.

*(Repair note — cycle-010 critic pass: an earlier draft flagged a second
gating reason, an alleged L0-comment vs L0-implementation disagreement on
conjugation handedness. That claim was based on a misreading of the
free-function `linalg::LocalDot` convention; the L0 free-function conjugates
the **second** argument (yielding `yᴴ x`), already documented at
`book/src/L1/dot.md:43, 104-105` as the L0-vs-L1 conjugation asymmetry. So
`linalg::Dot(comm, Ax, y) = yᴴ · Ax = yᴴ A x`, matching the L0 source comment
at `palace/linalg/operator.hpp:386`. No L0 disagreement exists; the gating
reason has been removed.)*

The rough-in carries the candidate signature in L1 vocabulary, the closed-form
semantic statement `xᴴ M y` (with the conjugation convention chosen to match
the dispatch directive and the natural specialisation `bilinear_form(x, I, y)
= dot(x, y)`), three solid algebraic laws (linearity in the linear argument,
bilinearity in the weight, zero-vector annihilation), and the four variant
axes (precision-mode, output-arg-pattern, M-symmetry-property,
parallel-wrapper). Composition-into-`apply_linop`-and-`dot` is recorded as an
**informational note** only — that unfolding is L1>L0 lowering territory, not
L1 definitional content.

## Proposed changes

```edit:book/src/L1/bilinear-form.md
---
layer: L1
operator: bilinear-form
firmness: rough-in
lowers_to: []
lifts_from: []
depends_on:
  - L1/apply_linop
  - L1/dot
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

`bilinear-form` is a **rough-in** rather than firm — see *Status* and *Open
questions* below. The structural signature is well-anchored, but narrow
variant-axis coverage in Palace's two surfaced use sites (Poynting-power
boundary integral; NLEPS Newton denominator) holds the entry below
firm-promotion threshold. *(An earlier draft listed a second gating reason
— an alleged L0 comment-vs-implementation conjugation disagreement — that
was based on a misreading of the L0 free-function `linalg::LocalDot`
convention. The L0 source is self-consistent: see Status and the
`bilinear-form-conjugation-convention-anchor` OQ for the verification.)*

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
sibling OQ `matrix-weighted-norm-and-bilinear-form-l1-rough-ins`) will likely
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

`rough-in (lower-layer-shared-vocabulary, cycle-010-wave-1)` — the structural
signature is anchored at L0 (`palace/linalg/operator.hpp:386-394`,
`palace/linalg/operator.cpp:621-639`), and the laws are inherited cleanly
from the firm L1 dependencies `dot` and `apply_linop`. Promotion to **firm**
is gated on resolving the one open question below:

1. Narrow variant-axis coverage from Palace's two surfaced use sites
   (Poynting-power and NLEPS Newton denominator) — neither exercises the
   real-`M`-real-`y` shape that the dispatch description names as the
   simplest case, and both happen to be complex-`x`-complex-`y`. The
   M-symmetry-property axis has two witnesses (one Hermitian, one not) but
   Cauchy–Schwarz at `y = x` is unexercised.

*(Repair note — cycle-010 critic pass: an earlier draft listed a second
gating reason (an alleged L0 comment-vs-implementation conjugation
disagreement). That claim was based on a misreading of the L0 free-function
`linalg::LocalDot` convention. Verified at `palace/linalg/vector.cpp:674-685`
that the free-function conjugates the second argument, yielding `yᴴ x`;
this is already documented at `book/src/L1/dot.md:43, 104-105`. The L0
source `linalg::Dot(comm, A·x, y) = yᴴ A x` matches the L0 comment at
`palace/linalg/operator.hpp:386`. The false gating reason has been removed;
the integrator may consider whether the remaining single gating reason
holds firm-promotion below firm or whether the rough-in is now
firm-promotion-eligible.)*

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
  matrix-weighted bilinear-form operator. The L0 chapter uses the candidate
  slug `dot_bilinear`; this entry uses the dispatch-supplied slug
  `bilinear-form` (matching the OQ candidate phrasing). The slug
  discrepancy is noted in *Open questions* below.
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
```

```edit:book/src/L1/index.md
[insert into the operator dep-map table — a new row positioned after the
`ksp_solve` firm row and before the `eigsolve` rough-in row, and a parallel
entry under the *Vocabulary cohort* §"Rough-in" subsection. Both insertions
are append-only relative to existing entries.]

Add row to the dep-map table:

| [`bilinear-form`](./bilinear-form.md) | `(x: Tensor[M], M: LinearOperator[M, N], y: Tensor[N]) → Scalar` (i.e. `xᴴ M y`) | `apply_linop` (direct), `dot` (direct) | `rough-in (lower-layer-shared-vocabulary, harvested-by: harvester:2026-05-27T215427Z-harvester-bilinear-form-l1)` |

Add to the *Vocabulary cohort* §"Rough-in" listing (a new subsection or
adjacent to the existing `eigsolve` rough-in entry; whichever cycle-010
sibling-dispatch coordination preserves):

- [`bilinear-form`](./bilinear-form.md) — matrix-weighted inner product
  `xᴴ M y`; the matrix-weighted generalisation of `dot` (M = I special
  case). Rough-in status motivated by narrow variant-axis coverage in
  Palace's two surfaced use sites (Poynting-power boundary integral;
  NLEPS Newton denominator).
```

```edit:book/src/SUMMARY.md
[add a chapter entry under the L_1 Part, positioned alphabetically (after
`axpy` / before `dot` — or in dep-map order, after `apply_linop` and before
`dot`; integrator chooses):

- [bilinear-form](./L1/bilinear-form.md)
]
```

## Operator content

The actual operator entry is the body of the `edit:book/src/L1/bilinear-form.md`
block above (the full chapter content as written).

## Supporting evidence

- **OQ source**: `scaffolding/open-questions.md` lines 1359-1366
  (`matrix-weighted-norm-and-bilinear-form-l1-rough-ins`, cycle-008,
  layer-intro-author). The OQ names `L1/dot_bilinear` as a candidate slug;
  this dispatch uses `bilinear-form` per the dispatch instructions.
- **Priority source**: `scaffolding/priorities.md` #17
  `lower-layer-shared-vocabulary-priority` (cycle-009 meta-phase).
- **L0 anchor (declarations)**: `palace/linalg/operator.hpp:386-394` —
  documented as `yᴴ A x`.
- **L0 anchor (implementations)**: `palace/linalg/operator.cpp:621-639` —
  real-`A` overload (lines 621-629) and complex-`A` overload (lines
  631-639), both computing `Dot(comm, Ax, y)` after applying `A` to `x`.
- **L0 file overview**: `book/src/L0/linalg-operator-file.md` §"linalg::
  free functions" (lines 30-35) and §"Why this file pair matters" (line 73).
- **Use sites**:
  - `palace/models/boundarymodeoperator.cpp:85` — Poynting power
    contribution from boundary mass matrix `Bttr` (Hermitian-`M` case).
  - `palace/models/boundarymodeoperator.cpp:90` — Poynting power cross-
    coupling contribution from inhomogeneous `Atn` (non-Hermitian-`M`
    case).
  - `palace/linalg/nleps.cpp:675` — NLEPS Newton denominator (the
    surrounding context uses the unweighted `linalg::Dot` overload;
    listed for inhomogeneous-anchor proximity rather than as a direct
    L0 anchor for the matrix-weighted form).
- **L1 dependencies**:
  - `book/src/L1/dot.md` — the M = I special case; defines the conjugation
    convention.
  - `book/src/L1/apply_linop.md` — the operator-application primitive.
- **Sibling dispatches** (cycle-010 wave-1):
  - #3 `matrix-weighted-norm` (likely slug `nrm2_B` or similar) —
    sibling operator addressing the same OQ.
  - #5 `nrm2_B-weighted` — depends on `bilinear-form` via
    `nrm2_B(x, B) = √bilinear_form(x, B, x)` for SPD `B`.

## Open questions / caveats

```yaml
---
slug: bilinear-form-conjugation-convention-anchor
opened_at: cycle-010
opened_by: harvester:2026-05-27T215427Z-harvester-bilinear-form-l1
status: resolved-by-correction
resolved_at: cycle-010 (critic + repairer pass)
resolved_by: critic:2026-05-27T223000Z (verification at vector.cpp:674-685) + repairer (in-place correction)
---
```

**Resolved-by-correction.** An earlier draft of this OQ flagged an
alleged disagreement between the L0 source comment (`yᴴ A x`, at
`palace/linalg/operator.hpp:386`) and the L0 implementation, claiming
the implementation returned `xᴴ Aᴴ y` by applying the L1 first-argument-
conjugation convention to the free-function `linalg::Dot(comm, Ax, y)`
call. **That claim was wrong.** Verification at
`palace/linalg/vector.cpp:674-685` shows the free-function `LocalDot(x, y)`
body assembles its imaginary part as `Im(x)·Re(y) - Re(x)·Im(y)`, which is
the imaginary part of `yᴴ x` (not `xᴴ y`). So the L0 free-function
`linalg::Dot(comm, Ax, y)` conjugates its **second** argument and returns
`yᴴ · Ax = yᴴ A x`, matching the L0 source comment exactly. **There is
no L0 disagreement.**

The L0/L1 conjugation asymmetry — L0 free-function conjugates the second
argument, L1 specification conjugates the first — is already documented
in the L1 `dot` chapter at `book/src/L1/dot.md:43` and reiterated at
`book/src/L1/dot.md:104-105`. The L1>L0 lowering theme for
`bilinear-form` inherits this asymmetry from `dot` without needing a
fresh OQ.

The three-way ambiguity (options a/b/c) the earlier draft listed is
spurious — option (c) (the L0 author using second-argument conjugation)
is in fact the correct reading, and is already canonicalised in `dot.md`.

**No new OQ ledger entry needed.** The L1>L0 lowering composition note
in *Semantics* §"Composition into `apply_linop` + `dot`" now explicitly
references the L0/L1 conjugation asymmetry and names the two equivalent
L0 unfolding shapes (argument-swap vs outer-`conj`). The mechanical
reconciliation is the L1>L0 theme's job, not an open research question.

```yaml
---
slug: bilinear-form-real-vector-coverage-gap
opened_at: cycle-010
opened_by: harvester:2026-05-27T215427Z-harvester-bilinear-form-l1
status: open
---
```

Palace's `linalg::Dot(comm, x, A, y)` matrix-weighted overload set is
**complex-vector only** — both overloads take `ComplexVector` arguments;
there is no `Dot(comm, Vector, Operator, Vector)` overload for real
vectors. The L1 entry's variant-axis table records this as "the real-`x`
/ real-`M` / real-`y` case is not surfaced by Palace".

**Question**: should the L1 `bilinear-form` operator (a) restrict to
complex-only at L1 (matching the Palace surface), (b) cover both real
and complex at L1 with the real-only case marked "L1-only; no L0
anchor", or (c) treat the real case as an implicit composition
`dot(x, apply_linop(M, y))` recovered from existing L1 operators?

**Recommendation pending firm-promotion**: option (c) — the real case
falls out of existing L1 vocabulary without needing a separate operator.
The L1 `bilinear-form` operator covers the matrix-weighted reduction
where Palace surfaces it as a distinct L0 free-function (the complex
case), and the real case is recovered by composition. This keeps the
L1 cohort minimal and matches the L1 invariant "subsumption-as-identity
rather than dependency".

```yaml
---
slug: bilinear-form-slug-name-coordination
opened_at: cycle-010
opened_by: harvester:2026-05-27T215427Z-harvester-bilinear-form-l1
status: open
---
```

The cycle-008 OQ that motivates this harvest names `L1/dot_bilinear` as
the candidate slug. The L0 file-overview chapter (`linalg-operator-file.md`,
lines 73 and 88) names `L1/dot_bilinear` as the expected lift target. The
cycle-010 dispatch directive uses the slug `bilinear-form` (matching the
mathematical form name rather than the BLAS-1 family naming). This rough-in
uses `bilinear-form` per the dispatch directive.

**Question**: keep `bilinear-form` (mathematical-form naming, matches the
sibling-operator `matrix-weighted-norm` dispatched in cycle-010 wave-1 #3),
or rename to `dot_bilinear` (BLAS-family naming, matches the cycle-008 OQ
and L0 chapter expectations)?

**Recommendation pending firm-promotion**: keep `bilinear-form`. Reasons:
(a) `dot_bilinear` is misleading because `dot` already returns a
sesquilinear (Hermitian) form on complex input — `bilinear` modifying
`dot` would suggest the unconjugated bilinear-form variant `tdot`, not
the matrix-weighted generalisation; (b) the sibling-operator naming
(`matrix-weighted-norm` for `nrm2_B`, `bilinear-form` for this operator)
gives the L1 cohort a coherent mathematical-form vocabulary; (c) the
specialisation law `bilinear_form(x, I, y) = dot(x, y)` is more
readable than `dot_bilinear(x, I, y) = dot(x, y)`.

**Follow-up**: the integrator should update the L0 chapter
(`book/src/L0/linalg-operator-file.md`) to point at the chosen L1 slug
after the cycle-010 wave-1 batch settles. That edit is **not** part of
this dispatch's authority (the L0 chapter is owned by
layer-intro-author).

```yaml
---
slug: bilinear-form-variant-axis-test-coverage
opened_at: cycle-010
opened_by: harvester:2026-05-27T215427Z-harvester-bilinear-form-l1
status: open
---
```

Promotion of `bilinear-form` from `rough-in` to `firm` is gated on
**variant-axis test coverage**. The currently-anchored variant-axis cells:

| axis | values | direct evidence |
|---|---|---|
| precision-mode | `double` only | inherited from `dot` + `apply_linop` |
| output-arg-pattern | `return` only | the only L0 form |
| M-symmetry-property | `hermitian` (Bttr) | `boundarymodeoperator.cpp:85` |
| M-symmetry-property | `non-symmetric` (Atn) | `boundarymodeoperator.cpp:90` |
| parallel-wrapper | both | per `apply_linop`'s coverage |
| element-type | complex-`x` / complex-`y` only | both overloads use ComplexVector |
| `M` element-type | `real` (Operator) | `operator.hpp:388-389` |
| `M` element-type | `complex` (ComplexOperator) | `operator.hpp:393-394` |

**Unexercised**: real-`x` / real-`y` cases (per the prior OQ);
Cauchy–Schwarz-tight case at `y = x` with non-SPD `M` (only the SPD
case has surfaced); algebraic law 8 (positive semi-definiteness)
direct numerical witness.

**Resolution path**: either expanded direct test coverage of
`linalg::Dot(comm, x, A, y)` under `palace/test/unit/`, or
literature-anchored evidence at firm-equivalent confidence (e.g.
Higham 2008 §10 inner-product accuracy bounds).

### Caveat on `book/src/L1/index.md` row positioning

The proposed dep-map edit adds a row for `bilinear-form`. The integrator
must coordinate with the sibling cycle-010 wave-1 dispatches (#3
`matrix-weighted-norm` and #5 `nrm2_B-weighted`) so that the dep-map
table receives **distinct** rows for each new operator. The
*Vocabulary cohort* listing's "Rough-in" section currently contains
the cycle-009 `eigsolve` test-coverage-bounded entry; the three new
rough-ins (`matrix-weighted-norm`, `bilinear-form`, `nrm2_B-weighted`)
could either join that listing under a new "Rough-in (lower-layer-
shared-vocabulary)" subsection or be appended to the existing one.

### Caveat on L1 intro refresh

The L1 intro's *Vocabulary cohort* §"Queued (open questions)" line
(`book/src/L1/index.md:51`) names the future `nrm2_B`-weighted operator
but does NOT name `bilinear-form` — the cycle-008 OQ that motivates
both was filed against `nrm2` only, and the `bilinear-form` candidate
was added retroactively to the same OQ. The intro should be refreshed
to name both. **That refresh is the layer-intro-author's domain**;
this dispatch only adds the dep-map row. Logging here per the
harvester role spec "What you DO NOT do" §"Update layer intros".
