---
agent: harvester
invoked_at: 2026-06-01T051607Z
scope: L2 operator: scal
status: pending
integrated_at: 2026-06-01T062913Z
integration_commit: c1f7ea3c651e65ed212aa8500c7c8572aaa2ec92
integration_notes: "Applied clean (staging row D3). book/src/L2/scal.md created firm (arity-1 member of linear_combination, cited-NOT-merged). vector.cpp:207-211 pinpoint kept UNCHANGED. fold_parent frontmatter field kept AS AUTHORED (meta-phase convention signal). SUMMARY + L2/index dep-map row. L2 firm 9->12 (cohort 3-of-13)."
inputs:
  - book/src/L1/scal.md (firm; authoritative L1 surface + L0 evidence)
  - book/src/L1-L0/scal-mutation-rotation.md (firm; L0 mutation rotation)
  - book/src/L3/scal.md (firm; the L3 consumer this floor entry supports)
  - book/src/L2/linear_combination.md (firm; the arity fold-parent — cited, NOT merged)
  - book/src/L2/index.md §"Fold-cohort boundary" (load-bearing do-NOT-merge boundary)
  - palace/linalg/vector.hpp:98-99,262-270 ; vector.cpp:203-227 (canonical L0 anchors, self-verified)
  - dispatch: cycle-041 D3, foundation-first directive l2-floor-under-l3-blas1-cohort (2026-05-31)
---

# CYCLE: Formalize scal at L2

## Summary

`scal` (vector-scalar multiplication `y = α·x`) is firm at L1 (cycle-004) and at L3
(cycle-011), but the **adjacent L2 floor entry is missing** — the L3 `scal` consumer
currently rests on no present L2 parent, and the L2 surface only mentions `scal` as
the arity-1 leaf the firm `linear_combination` fold (cycle-018) fuses up from. This
dispatch lands the **thin identity-in-form L2 floor entry** `book/src/L2/scal.md`
under the 2026-05-31 foundation-first directive (`l2-floor-under-l3-blas1-cohort`),
floored for layer-coherence per the methodology invariant **Identity-lowerings still
require both L levels**. The entry defines `scal` in **L2 (fusion-rotation) vocabulary**
as a leaf scalar-vector field operation, and frames it as the **arity-1 member of the
firm `linear_combination` fold** — citing `linear_combination` as the fold-parent
**without merging** (the fold-cohort boundary at `book/src/L2/index.md` §"Fold-cohort
boundary" is load-bearing). The L2 body is identity-in-form to L1 (no fusion to unfold
beyond the single-aligned-pass note inherited from the fold-parent's fusion note); the
substantive L2>L1 / L3>L2 rotations are narrated by the D6 themes this cycle, referenced
in plain text (those theme files do not yet exist). Status: `firm` (identity-in-form
floor; firm-on-positive-structure — every law is a syntactic identity on the small,
fully-present `operator*=` surface).

## Proposed changes

```new:book/src/L2/scal.md
---
layer: L2
operator: scal
firmness: firm
lowers_to:
  - book/src/L1/scal.md (identity-in-form; no firm `L2-L1/scal-fusion` theme yet — the single-aligned-pass fusion is the degenerate arity-1 case of the `linear_combination` fold's fusion note; in-line below at "Lowers to")
lifts_from:
  - book/src/L1/scal.md (value-thread-isomorphic; same signature shape; whole-tensor leaf primitive, no kernel fusion to unfold beyond the arity-1 single-pass)
fold_parent:
  - book/src/L2/linear_combination.md (arity-1 member of the term-axis fold; cited, NOT merged — fold-cohort boundary is load-bearing)
variant_axes:
  - element-type (real / complex)
  - scalar-promotion (real-α-against-complex-x via concepts/scalar-promotion)
---

# scal

Vector-scalar multiplication as a base tensor-algebra primitive at L2 — the
**fusion-rotation** rendering of `y = α·x`. Consumes a scalar `α` and a tensor `x`;
produces a fresh tensor of the same length axis whose every element is `α` times the
corresponding input element. `scal` is the **arity-1 member of the firm
[`linear_combination`](./linear_combination.md) fold** (`scal`/`axpy`/`axpby`/`axpbypcz`
are its arity-1/2/2/3 specializations); this entry is the standalone leaf, cited as a
fold-specialization of `linear_combination` but **not merged into it** (the fold-cohort
boundary in `book/src/L2/index.md` §"Fold-cohort boundary" is load-bearing). Companion
to L1 [`scal`](../L1/scal.md) (the mutation-lifted form of the same primitive) and L3
[`scal`](../L3/scal.md) (the iteration-rotation rendering); the rotation L1 ↔ L2 is
identity-in-form because `scal` is a leaf field operation with no kernel fusion to
unfold beyond the degenerate arity-1 single-aligned pass.

## Context

L2 is the fusion-rotation layer (`book/src/L2/index.md`): "Kernel fusion across multiple
algebraic operations is unfolded into composition… Batched specialized BLAS calls are
written as compositions of base primitives." The L2 vocabulary explicitly names `scal`
among its base primitive operations (`book/src/L2/index.md:17` — "primitive operations
(axpy, dot, matvec, gemv, trsv, scal, nrm2, …)"). `scal` at L2 is the base
scalar-vector-multiply primitive in that vocabulary — a single field operation
parameterised by a scalar `α` and acting pointwise over the length axis.

**`scal` is the arity-1 member of the `linear_combination` fold, cited but not merged.**
The firm [`linear_combination`](./linear_combination.md) entry (cycle-018) is the
arity-family unification of the BLAS-1 scalar-weighted-sum cohort: its four fixed-arity
leaves (`scal`/`axpy`/`axpby`/`axpbypcz`) are the arity-1/2/2/3 specializations of one
variadic `foldl` over a list of `(scalar, tensor)` terms, with
`scal(α, x) = linear_combination [(α, x)]` recorded as the arity-1 specialization
identity (`linear_combination.md` §Signature line 68, §Algebraic-laws law 6). The fold
**does not replace the leaves** — the `axpby-as-primitive` decision
([`scaffolding/decisions/axpby-as-primitive.md`](../../../scaffolding/decisions/axpby-as-primitive.md))
keeps each leaf firm (fuse, don't decompose), and the L2 index §"Fold-cohort boundary"
makes the do-NOT-merge boundary load-bearing. So `scal` has its own L2 floor entry as a
leaf, and that leaf is **also** a recognized arity-1 specialization of the fold — the
two relationships coexist by design.

This is a thin **floor presence** entry. It exists so the firm L3 [`scal`](../L3/scal.md)
(cycle-011) rests on a present adjacent L2 parent, per the methodology invariant
**Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants,
cycle-009 codification): each layer is coherent within itself, and a reader at L2 must
find `scal` defined in L2 vocabulary without reaching down to L1 or up to L3. The
foundation-first directive `l2-floor-under-l3-blas1-cohort` (2026-05-31) names exactly
this gap: the L3 BLAS-1 cohort (`axpy`/`axpby`/`axpbypcz`/`dot`/`nrm2`/`scal`) was
backfilled to L3 in cycle-011 without the corresponding L2 floor entries being present,
so the L3 cohort rests on the L1 leaves directly. This dispatch floors `scal`; the
sibling BLAS-1 floor entries are co-dispatched this cycle.

A cross-cutting prose treatment lives at [`concepts/scal`](../concepts/scal.md) —
covering BLAS background (BLAS-1 `dscal` / `zscal`) and call-site role (basis
normalisation, search-direction rescaling). The scalar-promotion sub-axis (real `α`
against complex `x`) is covered at [`concepts/scalar-promotion`](../concepts/scalar-promotion.md).
The L2 entry here is the firm operator definition at the fusion-rotation layer; the
concept pages are the narrative and the typing rule.

## Signature

```text
scal :: Scalar -> Tensor[N] -> Tensor[N]
scal α x = α·x
```

Shape contract (bunsen-style, named axes; positional values, no monadic effect, no
destination buffer):

- **`α`** — scalar (`real` or `complex`, matching the tensor element type per the
  element-type variant axis; or promoted from `real` to `complex` against complex `x`
  per the scalar-promotion sub-axis).
- **`x`** — `Tensor[N]` — the input tensor with a single length axis `N`. Read-only at
  L2 (the L2 form is pure / out-of-place; the L0 in-place mutation is reintroduced only
  at the L1>L0 lowering).
- **result** — `Tensor[N]` — same axis `N` as `x`. Every output element equals `α`
  times the corresponding input element.

The L2 signature is **identical to the L1 signature** modulo notation; the rotation is
identity-in-form. As the arity-1 fold specialization, the same operator is
`linear_combination [(α, x)]` (per `linear_combination.md` line 68) — but the standalone
leaf form is the canonical L2 rendering, with the fold view recorded as a derived
identity (law 4 below), not as a decomposition.

## Semantics

`scal` at L2 is a single base tensor-algebra field operation: a value-threaded
transformation `(α, x) -> y` where `y[i] = α · x[i]` for every element index
`i ∈ [0, N)`. The operator is **element-local** (every output element depends on exactly
one input element and the shared scalar `α`), **reduction-free** (no cross-element
communication), and **rank-local** (no MPI collective at any layer; ranks own disjoint
slices of `N` and apply the scalar multiplication independently — contrast `dot` /
`nrm2`, which reduce over `N` and do carry an MPI collective).

It is **pure / out-of-place** at L2: it consumes `α` and the prior value of `x` and
produces a fresh tensor; no destination buffer appears in the signature. The L0 in-place
receiver-mutating idiom (`x *= α`) is an L2>L1 (and onward L1>L0) lowering concern,
captured by the output-aliasing direction of the lowering themes — not by the L2 algebra.

**Leaf, with no kernel fusion to unfold.** L2 is the layer where kernel fusion across
multiple algebraic operations is unfolded into composition. `scal` is a **leaf** in that
vocabulary — there is no multi-operation fusion to unfold (it is a single scalar-vector
multiply, not a fused `α·x + β·y` pass). The one fusion note it carries is the
**degenerate arity-1 case of the `linear_combination` fold's fusion note**: the single
aligned strided pass computing `α·x[i]` per element is the seed-and-accumulate fold
collapsed to one term (the `foldl` over a singleton `[(α, x)]` reduces to one scaled
accumulate into a zero seed). This is the transparent-performance-trick implementation
of the arity-1 fold; L2 records it as one note and otherwise treats `scal` as the base
primitive it is.

Special algebraic cases — `α = 0` (zero-fill, discards `x`), `α = 1` (identity),
`α = -1` (negation), `α⁻¹` (inverse for non-zero `α`) — are not separate operators at
L2. They are algebraic identities recorded in the laws below, inherited from L1. The L0
source has no constant-folding branches on the value of `α` (the `s.imag() == 0.0`
branch in `ComplexVector::operator*=` at `palace/linalg/vector.cpp:207-211` is a
complex-scalar-*shape* specialisation, not a scalar-*value* specialisation, and
disappears at L1 per the transparent-vs-load-bearing-tricks discipline).

## Algebraic laws

The nine laws that hold at L1 (per `book/src/L1/scal.md` §Algebraic laws) hold unchanged
at L2. The rotation L2 ↔ L1 is identity-in-form on the operator's body and signature, so
the algebraic properties of vector-scalar multiplication (axioms of a module over the
scalar field, plus the field-commutativity inherited rule) transport without
modification. Absences are deliberate and inherited.

1. **Identity in `α`**: `scal(1, x) = x`. The neutral element of scalar multiplication.
2. **Absorption in `α`**: `scal(0, x) = 0` (the zero tensor of axis `N`), for any `x`.
3. **Absorption in `x`**: `scal(α, 0) = 0`, for any `α`.
4. **Composition (scalar fusion)**: `scal(α, scal(β, x)) = scal(α·β, x)`. Two successive
   scalings collapse to one with the scalar product. The action of scalars on tensors is
   multiplicative.
5. **Distributivity over scalar addition**: `scal(α + β, x) = scal(α, x) + scal(β, x)`,
   where `+` on the right is element-wise tensor addition. Linearity in the scalar
   argument.
6. **Distributivity over tensor addition**: `scal(α, x + y) = scal(α, x) + scal(α, y)`.
   Linearity in the tensor argument.
7. **Negation**: `scal(-1, x) = -x`. (Special case of laws 1 + 5.)
8. **Inverse (for non-zero scalar)**: `scal(α⁻¹, scal(α, x)) = x` for `α ≠ 0`. (Special
   case of law 4 with `β = α⁻¹` and law 1.) This is the rule that makes `Normalize`
   invertible up to the recovered `α = 1/nrm2(x)`.
9. **Commutativity of scalars (field-inherited)**: `scal(α·β, x) = scal(β·α, x)`.
   Inherited from the underlying field (`ℝ` or `ℂ`).

**Fold-specialization identity (the link to `linear_combination`, NOT a merge):**

- `scal(α, x) = linear_combination [(α, x)]` — `scal` is the arity-1 specialization of
  the firm [`linear_combination`](./linear_combination.md) fold (`linear_combination.md`
  §Signature line 68, §Algebraic-laws law 6). The fold's concatenation-homomorphism
  (`linear_combination.md` law 2) makes the four arities one fold; the leaf laws above
  are the arity-1 shadow of the fold's laws (law 4 here = `linear_combination.md` law 4
  coefficient-scaling at singleton; laws 5–6 here = the multilinearity / distributivity
  the fold generalizes). The leaf stays firm and standalone; the fold view is a derived
  identity, not a decomposition (do-NOT-merge per the fold-cohort boundary).

Laws that explicitly **do not** hold:

- **Idempotence**: `scal(α, scal(α, x)) ≠ scal(α, x)` in general — the result is
  `scal(α², x)`, which equals `scal(α, x)` only when `α² = α`, i.e. `α ∈ {0, 1}` (or
  `α(α−1) = 0` more broadly).
- **Commutativity in argument positions**: `α` and `x` live in distinct types (scalar
  vs tensor). "Commutativity" is not well-typed for the operator's argument list.
- **Distributivity over tensor products**: not applicable at L2 — there is no
  inner-tensor multiplication in the scalar-vector-multiply leaf's vocabulary (`dot`
  reduces to a scalar; the element-wise Hadamard product is the separate
  `elementwise_product` primitive, of which `scal` is the broadcast-scalar special case).
  The closest applicable rule is law 6, distributivity over tensor **addition**.
- **Bit-level equivalence under fusion**: `scal(α, scal(β, x))` (law 4 LHS) and
  `scal(α·β, x)` (law 4 RHS) are algebraically equal but may differ at the bit level in
  IEEE-754 because the two-pass form rounds twice (once per element-multiply) and the
  fused form rounds once. Transparent-trick consideration inherited from L1; not
  load-bearing in CLAUDE.md's sense for the algorithms Palace runs, but worth recording
  for solvers that depend on bit-determinism across fusion choices. (At the fold level,
  this is the arity-1 shadow of the `linear_combination` permutation non-law's
  summation-order load-bearing concern.)

## Dependencies

**Same-layer (L2)**: none as a constituent. `scal` is a leaf primitive at L2 just as it
is at L1 — vector-scalar multiplication does not decompose into other L2 primitives. The
body is a single field operation; the sub-operations (scalar multiplication and
per-element application) are below the L2 layer's resolution.

**Fold-parent (cited, NOT merged)**:

- [`linear_combination`](./linear_combination.md) (firm cycle-018) — the term-axis
  arity-family fold of which `scal` is the **arity-1 member**
  (`scal(α, x) = linear_combination [(α, x)]`). `scal` stays a firm standalone L2 leaf;
  `linear_combination` is the form the four leaves (`scal`/`axpy`/`axpby`/`axpbypcz`)
  fuse *up* into, not a replacement. The do-NOT-merge boundary
  (`book/src/L2/index.md` §"Fold-cohort boundary") is load-bearing — merging the leaf
  into the fold would erase the one-to-one leaf↔L0-symbol shape that the L1>L0 mutation
  rotation relies on.

**Cross-cutting concepts**:

- [`scalar-promotion`](../concepts/scalar-promotion.md) — the implicit-coercion typing
  rule for real `α` against complex `x`. Internal promotion at L0 via the
  `s.imag() == 0.0` branch in `ComplexVector::operator*=`; collapsed at L1 / L2 / L3
  into a single operator parameterised by the `real ⊑ complex` scalar lattice.
- [`scal` (concept)](../concepts/scal.md) — cross-cutting prose treatment; BLAS-1
  background and call-site role (basis normalisation, search-direction rescaling).

**Sibling subsumption (not dependency)**:

- `scal(α, x) = axpby(α, x, 0, y) = axpby(0, y, α, x)` for any `y`, per `axpby` laws 2
  and 3 at `book/src/L1/axpby.md`. `scal` stays in the L2 dep-map as a sibling leaf, not
  a sub-operation of `axpby` (per the harvester decision at
  `scaffolding/decisions/axpby-as-primitive.md`).
- `Normalize(x) = scal(1 / nrm2(x), x)` paired with the returned norm. The free-function
  `linalg::Normalize` at `palace/linalg/vector.hpp:262-270` is a fused `nrm2 + scal`
  construct; at L2 it factors as the composition `scal(1/nrm2(x), x)`. Whether to harvest
  a fused `normalize` L2 primitive is an open question inherited from L1 (the firm L3
  [`normalize`](../L3/normalize.md), cycle-039, is the iteration-rotation rendering of
  that fused composite).

**Lowering themes (forthcoming; D6 this cycle — plain-text forward-reference, files do
not yet exist)**: an `L2-L1/scal-fusion` theme will narrate how the L2 leaf lowers into
the L1 leaf (identity-in-form; the only fusion content is the degenerate arity-1
single-aligned pass), and the L3>L2 identity rotation for `scal` is the iteration-rotation
re-erasure recorded in-line at the L3 entry. Forward-reference only — those chapters do
not yet exist; do not link.

## Variant axes

The two variant axes are inherited unchanged from L1. Both are absorbed at construction
time (the element-type axis through overload selection at L0; the scalar-promotion
sub-axis through the internal `s.imag() == 0.0` branch); neither appears in the L2
positional signature.

1. **element-type** (`real` | `complex`). The L0 source has separate overloads
   (`mfem::Vector::operator*=(double)` from MFEM for real; `ComplexVector::operator*=(std::complex<double>)`
   at `palace/linalg/vector.cpp:203-227` for complex). At L1 / L2 / L3 these collapse to
   one operator parameterised by element type — the semantics are identical (per-element
   scalar multiplication in the appropriate field).
2. **scalar-promotion** (sub-axis on the complex element-type). See
   [`concepts/scalar-promotion`](../concepts/scalar-promotion.md) — real `α` against
   complex `x` via the internal `s.imag() == 0.0` branch at `vector.cpp:207-211`.
   Value-based (not overload-based) promotion: the L0 caller passes
   `std::complex<double>` with zero imaginary part, and Palace recognises the special
   case to dispatch to two real `operator*=` calls. At L1 / L2 / L3 this is one operator
   with `α` typed through the `real ⊑ complex` scalar lattice.

No other variant axes — `scal` is unconditionally pure, element-local, reduction-free,
and rank-local across all variants. Unlike `axpy` (which has the real-path `α == 1.0`
constant-folding specialisation at L0) and like `axpby` (which has no constant-folding),
`scal` has no L0 constant-folding branches on the value of `α`; the branch in
`ComplexVector::operator*=` is a complex-scalar-shape branch (`imag == 0`), not a
scalar-value branch.

The variant-axis count matches the L1 and L3 entries exactly (two axes; element-type
with scalar-promotion as sub-axis). No new axes introduced by the L2 rendering; no axes
merged or split.

## Status

`firm` — signature is canonical (matches BLAS-1 `dscal` / `zscal` and the Palace
`operator*=` surface exactly; identical to the L1 and L3 forms), and the nine algebraic
laws are standard scalar-vector-multiplication facts (axioms of a module over the scalar
field, plus the field-commutativity inherited rule). **Firm-on-positive-structure**: the
`scal` L0 surface is small, fully present, and positively cited
(`palace/linalg/vector.{hpp,cpp}` + inlined call sites), and every law is a syntactic
identity on that closure — the absence of a dedicated `scal` unit test does not gate firm
(the syntactic-identity-laws-on-positive-source escape, the `apply_linop` situation, not
the `eigsolve`-convergence-semantics situation). This dispatch is the **L2 floor
backfill** (cycle-041 D3) under the foundation-first directive
`l2-floor-under-l3-blas1-cohort`: the L2 form was previously referenced only as the
arity-1 leaf of `linear_combination` and inside `krylov-step` / `chebyshev-iteration`
dependency lists; it now has its own L2 entry per **Identity-lowerings still require both
L levels**.

## Lowers to

L2 `scal` lowers to L1 [`scal`](../L1/scal.md) via an **identity-in-form** rotation: the
signature `Scalar -> Tensor[N] -> Tensor[N]` is textually identical at both layers; the
body is the same scalar-vector field operation. There is no kernel fusion to unfold
beyond the degenerate arity-1 single-aligned pass (the arity-1 case of the
`linear_combination` fold's fusion note). No firm `L2-L1/scal-fusion` theme file yet
exists (the D6 dispatch this cycle authors the L2>L1 lowering themes for the BLAS-1 floor
cohort); this entry captures the identity rotation in-line, following the L3 `scal`
backfill precedent for in-line identity-rotation annotation. The L0 in-place mutation is
reintroduced at the L1>L0 lowering ([`scal-mutation-rotation`](../L1-L0/scal-mutation-rotation.md),
firm).

## Lifts from

L1 `scal` lifts to this L2 entry via the **value-thread-isomorphic** identity rotation:
the L1 form's signature has no kernel fusion exposed, no destination buffer, no MPI
collective — these are exactly the properties that make it L2-native by construction as a
base tensor-algebra primitive. The L2 entry exists for layer-coherence reasons — a reader
navigating L2 must find `scal` defined in L2 vocabulary as the base scalar-vector-multiply
primitive (and as the arity-1 member of the `linear_combination` fold), not have to reach
down to L1 to recover the field-operation shape.

## Evidence

The L2 form is value-thread-isomorphic to the L1 form; all L0 evidence is sourced from
the firm L1 entry. Direct citations relevant to this L2 entry:

- `book/src/L1/scal.md` (cycle-004 firm) — the L1 form this L2 entry value-thread-mirrors.
  Body shape, signature, semantics (element-local, reduction-free, rank-local), the nine
  algebraic laws, variant axes (two: element-type, scalar-promotion sub-axis), and L0
  evidence chain.
- `book/src/L1-L0/scal-mutation-rotation.md` (firm) — the L1>L0 mutation rotation; the
  in-place `x *= α` receiver-mutating idiom the L2 pure form abstracts over.
- `book/src/L3/scal.md` (cycle-011 firm) — the L3 consumer this floor entry supports;
  identical signature and laws, iteration-rotation framing.
- `book/src/L2/linear_combination.md` (cycle-018 firm) — the fold-parent. `scal` is its
  arity-1 specialization (`linear_combination.md` §Signature line 68:
  `scal(α, x) = linear_combination [(α, x)]`; §Algebraic-laws law 6 specialization
  identities). Cited as fold-parent, NOT merged (fold-cohort boundary load-bearing).
- `book/src/L2/index.md:17` — L2 vocabulary inventory naming `scal` among the base
  primitive operations; §"Fold-cohort boundary" — the load-bearing do-NOT-merge note.
- `scaffolding/decisions/axpby-as-primitive.md` — the fused-leaf decision; governs the
  L1/L2 leaf-vs-decompose choice (keep leaves firm, fuse up into the fold, don't merge).
- `book/src/concepts/scal.md` — pre-existing cross-cutting prose treatment; consistent
  with this L2 entry's framing.
- `book/src/concepts/scalar-promotion.md` — the typing rule for the scalar-promotion
  sub-axis (`vector.cpp:207-211` anchor).

**L0 evidence (canonical anchors, self-verified via codemap `read_range` + on-disk
`citecheck --anchor`, 2026-06-01)**:

- `palace/linalg/vector.hpp:98-99` — `ComplexVector::operator*=(std::complex<double> s)`
  declaration with comment `Scale all entries by s.`
- `palace/linalg/vector.cpp:203-227` — `ComplexVector::operator*=` definition; lines
  207-211 branch `if (si == 0.0)` to two real `operator*=` calls
  (`Real() *= sr; Imag() *= sr;`); lines 212-225 run the general complex-scalar
  `forall_switch` kernel computing `XR[i] = sr·XR[i] − si·XI[i]; XI[i] = si·XR[i] + sr·XI[i]`.
- `palace/linalg/vector.hpp:262-270` — `linalg::Normalize` template
  (`auto norm = Norml2(comm, x); … x *= 1.0 / norm; return norm;`) — the fused
  `nrm2 + scal` construct factoring at L2 as `scal(1/nrm2(x), x)`.

## L2 vs L1 distinction

- **L1**: mutation-lifted pure functional update. `x_new = scal(α, x_old)`. Frames the
  operator as the pure-functional image of the L0 receiver-mutating `*=` member-method
  idiom; emphasises the *mutation rotation* against the source (the destination-buffer
  drop and the real-imag-shape branch erasure).
- **L2**: base tensor-algebra field operation. `y = scal(α, x)`. Frames the operator as
  a leaf primitive in the fusion-rotation layer's base vocabulary — and as the **arity-1
  member of the `linear_combination` fold** (cited, not merged); emphasises that there is
  no kernel fusion to unfold (the only fusion note is the degenerate arity-1 single-pass).
  The L2 form is **identical in body and signature to L1** — the framing differs (mutation
  rotation at L1 vs fusion rotation + fold-membership at L2), but no operational adjustment
  occurs.

The L2 ↔ L1 rotation is identity-in-form on the body and signature; the surface
adjustment is documentary. The methodology invariant **each layer is coherent within
itself** is what compels the L2 entry to exist as its own anchor — and the
foundation-first directive `l2-floor-under-l3-blas1-cohort` is what schedules it, so the
firm L3 [`scal`](../L3/scal.md) rests on a present adjacent L2 parent.
```

```edit:book/src/L2/index.md
| [`linear_combination`](./linear_combination.md) | `[(Scalar, Tensor[N])] -> Tensor[N]` (≡ `foldl (\acc (a,t) -> acc + a·t) zeros pairs`) | **Fold cohort — reduce-to-`Tensor[N]`, folds the term axis.** L1 fixed-arity specializations: `scal` (arity 1), `axpy` (arity 2, coeff 1 fixed), `axpby` (arity 2), `axpbypcz` (arity 3). Concepts: `scalar-promotion` (element-type axis, concept-page-level sibling of this arity-axis unification; inherited with its open upstream dependency — OQ `scalar-promotion-typing-rule`, not yet committed). **Sibling fold (do NOT merge):** `inner_product` (reduce-to-`Scalar`; different codomain/homomorphism). | `firm` (harvested cycle-018; promoted from rough-in proposed-by combinator-miner:2026-05-28T223022Z; constructive prong (b) of OQ blas1-variadic-linear-combination-fold-unification) |
| [`scal`](./scal.md) | `scal :: Scalar -> Tensor[N] -> Tensor[N]` (`α, x → α·x`) | **Base scalar-vector-multiply leaf; arity-1 member of [`linear_combination`](./linear_combination.md) (cited, NOT merged — fold-cohort boundary load-bearing).** Leaf primitive (no L2 constituents; sub-operations below L2 resolution). Fold-parent: `linear_combination` (`scal(α,x) = linear_combination [(α,x)]`). Concepts: [`scalar-promotion`](../concepts/scalar-promotion.md) (element-type axis + real⊑complex sub-axis), [`scal`](../concepts/scal.md) (cross-cut prose). Sibling-subsumed by `axpby` (β=0). L1 anchor via identity-in-form rotation (whole-tensor in/out at both layers; no kernel fusion to unfold beyond the degenerate arity-1 single-pass). | `firm` (harvested cycle-041 D3; L2 floor backfill under foundation-first directive `l2-floor-under-l3-blas1-cohort`; identity-lowering per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels** — floors the firm L3 [`scal`](../L3/scal.md), cycle-011; firm-on-positive-structure — syntactic-identity laws on the small fully-present `operator*=` surface) |
```

**Insertion note for integrator**: the `linear_combination` row above is the *anchor*
(unchanged) — insert the new `scal` row **immediately after** it. Do **NOT** touch the
L2/index consolidated firm-count tally (the "raised the firm cohort N→M" running totals
in §"Working Notes" / §"Vocabulary cohort") — **D7 owns the L2/index tally this cycle**
(count-ownership partition). This dispatch appends only the `scal` dep-map row + the
SUMMARY registration below.

```edit:book/src/SUMMARY.md
- [linear_combination](./L2/linear_combination.md)
- [scal](./L2/scal.md)
- [inner_product](./L2/inner_product.md)
```

## Operator content

The full firm chapter body is authored inside the `new:book/src/L2/scal.md` fenced
block above (§Context through §"L2 vs L1 distinction", `## Status: firm`). Key points:

- **Slug + one-line**: `scal` — vector-scalar multiplication `y = α·x` as the L2
  fusion-rotation base scalar-vector-multiply primitive; the arity-1 member of the firm
  `linear_combination` fold.
- **Signature**: `scal :: Scalar -> Tensor[N] -> Tensor[N]` (`scal α x = α·x`); pure /
  out-of-place; shape contract with named axis `N`, element-type + scalar-promotion
  variant axes absorbed at construction.
- **Semantics**: single base tensor-algebra field operation; element-local,
  reduction-free, rank-local; leaf with **no kernel fusion to unfold** beyond the
  degenerate arity-1 single-aligned pass (the arity-1 case of the `linear_combination`
  fold's fusion note).
- **Algebraic laws**: the nine L1 laws transport unchanged (identity-in-form);
  fold-specialization identity `scal(α, x) = linear_combination [(α, x)]` links to the
  fold-parent (cited, NOT merged); four non-laws (idempotence, argument-commutativity,
  tensor-product distributivity, bit-level fusion equivalence) inherited.
- **Dependencies**: none as a constituent (leaf); fold-parent `linear_combination`
  (cited, not merged); concepts `scalar-promotion` + `scal`.
- **Status**: `firm` — firm-on-positive-structure (syntactic-identity laws on the small
  fully-present `operator*=` surface; missing dedicated test does not gate firm).
- **Evidence**: firm L1/L3/L2-fold-parent entries + the self-verified canonical L0
  anchors (`vector.hpp:98-99,262-270`, `vector.cpp:203-227`).

## Supporting evidence

**Source-of-truth artifact entries (read this invocation, not re-derived):**

- `book/src/L1/scal.md` (firm cycle-004) — authoritative L1 surface; nine algebraic
  laws, two variant axes, L0 evidence chain. The L2 entry value-thread-mirrors this.
- `book/src/L1-L0/scal-mutation-rotation.md` (firm) — the L1>L0 mutation rotation; the
  in-place `x *= α` idiom the L2 pure form abstracts over. Confirms no free-function
  `linalg::Scal`/`Scale` symbol and no scalar-value constant-folding.
- `book/src/L3/scal.md` (firm cycle-011) — the L3 consumer; frontmatter conventions
  (`layer`/`operator`/`firmness`/`lowers_to`/`lifts_from`/`variant_axes`) mirrored,
  extended with a `fold_parent` field for the `linear_combination` membership.
- `book/src/L2/linear_combination.md` (firm cycle-018) — the fold-parent. Line 68
  (`scal(α, x) = linear_combination [(α, x)]`) and law 6 (specialization identities) are
  the load-bearing arity-1-membership anchors. Cited, NOT merged.
- `book/src/L2/index.md` §"Fold-cohort boundary" (`:22-26`, `:75`) — the load-bearing
  do-NOT-merge boundary between the leaves and the fold; line 17 names `scal` in the L2
  base-primitive vocabulary.

**L0 anchors — self-verified 2026-06-01 (citecheck `--anchor`, all `[ok]`):**

- `palace/linalg/vector.hpp:98-99` — `operator*=` decl (anchor `operator*=` at :99). `[ok]`
- `palace/linalg/vector.hpp:262-270` — `Normalize` template (anchor `Normalize` at :262,:264). `[ok]`
- `palace/linalg/vector.cpp:203-227` — `ComplexVector::operator*=` definition (anchor at :203). `[ok]`
- `palace/linalg/vector.cpp:207-211` — `si == 0.0` promotion branch (anchor at :207). `[ok]`
- Read-confirmed the `:203-227` body directly: `:207-211` two-real-call branch,
  `:212-225` general complex `forall_switch` kernel.

All L0 citations in this report are inherited verbatim from the firm L1 entry and
re-verified against on-disk source this invocation — no new L0 localization was required
(the L2 entry is identity-in-form; L0 evidence is transitive through L1).

## Count-ownership note (mandatory, per dispatch)

This dispatch appends **only** its own `book/src/L2/scal.md` chapter, its own L2/index
dep-map **row** (after the `linear_combination` anchor row), and the SUMMARY registration.
It does **NOT** write the L2/index consolidated firm-count tally (the "firm cohort N→M"
running totals in §"Vocabulary cohort" / §"Working Notes") — **D7 owns the L2/index tally
this cycle**. The integrator should apply the row + SUMMARY insert and leave the tally to
D7's landing.

## Open questions / caveats

- **L2 BLAS-1 floor cohort completeness (this cycle's co-dispatch).** `scal` is one of
  the L2 floor entries co-dispatched this cycle under `l2-floor-under-l3-blas1-cohort`.
  The L3 BLAS-1 cohort (`axpy`/`axpby`/`axpbypcz`/`dot`/`nrm2`/`scal`) was backfilled to
  L3 in cycle-011 with no corresponding L2 floor entries; the sibling L2 floor entries
  (`axpy`/`axpby`/`axpbypcz`/`dot`/`nrm2`) should land in the same cohort to fully floor
  the L3 cohort. Not in this dispatch's scope (one operator per invocation). Surfaced for
  the planner to confirm the cohort closes.

- **`L2-L1/scal-fusion` + `L3-L2/scal` themes are forward-referenced plain-text (D6 this
  cycle).** This entry references the forthcoming D6 L2>L1 lowering theme for `scal` in
  plain text (no live link — the theme file does not yet exist). When D6 lands the
  `L2-L1/scal-fusion` theme, a future pass should upgrade the plain-text reference in
  `book/src/L2/scal.md` §"Lowers to" and §Dependencies to a live link
  (skill `upgrade-plain-text-ref-to-live-link-when-target-on-disk`). The `scal` L2>L1
  lowering is identity-in-form (the only fusion content is the degenerate arity-1
  single-aligned pass), so the theme is thin.

- **`fold_parent` frontmatter field is new.** The L3 `scal` frontmatter does not carry a
  `fold_parent` field; I added one to the L2 entry to record the `linear_combination`
  arity-1 membership in machine-readable form (the fold-cohort boundary is load-bearing
  and worth surfacing in frontmatter, not just prose). If the layer-intro-author prefers
  the membership stay prose-only (consistent with how L1 records it), the field can be
  dropped without affecting the body. Flagged as a low-stakes convention choice, not a
  blocker.

- **Normalize-as-fused-L2-primitive (inherited OQ).** Whether to harvest a fused
  `normalize` L2 primitive (the `nrm2 + scal` `linalg::Normalize` construct) is an open
  question inherited from L1 (`normalize-as-fused-l1-primitive` / the
  `normalize-l1-primitive-harvest` plan item). The firm L3 [`normalize`](../L3/normalize.md)
  (cycle-039) is the iteration-rotation rendering of that fused composite; an L2 floor for
  it may be wanted symmetrically with this `scal` floor. Out of scope here; noted for the
  planner.

- **L2/index intro refresh (layer-intro-author's domain).** The L2 index §"Vocabulary
  cohort" / §"Working Notes" will want a note that the BLAS-1 base-primitive floor
  (`scal` + siblings) is now landing as standalone L2 entries (distinct from their
  `linear_combination` fold-membership). That is the layer-intro-author's edit, not this
  harvester's — flagged per role discipline (harvester does not update layer intros). The
  consolidated firm-count tally is D7's this cycle (count-ownership).
