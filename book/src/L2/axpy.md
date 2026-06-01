---
layer: L2
operator: axpy
firmness: firm
lowers_to:
  - book/src/L1/axpy.md (identity-in-form; no firm `L2-L1/axpy-fusion` theme yet — the single-aligned-pass fusion is the arity-2 case of the `linear_combination` fold's fusion note; in-line below at "Lowers to". The L1>L0 in-place form is `axpby-mutation-rotation` sub-pattern A, the β=1 specialization.)
lifts_from:
  - book/src/L1/axpy.md (value-thread-isomorphic; same signature shape; whole-tensor leaf primitive, no kernel fusion to unfold beyond the arity-2 single-aligned pass)
fold_parent:
  - book/src/L2/linear_combination.md (arity-2 member of the term-axis fold, second coefficient fixed to 1; cited, NOT merged — fold-cohort boundary is load-bearing)
variant_axes:
  - element-type (real | complex)
  - scalar-promotion (real-α-against-complex-x via concepts/scalar-promotion)
---

# axpy

Vector-scalar fused linear update as a base tensor-algebra primitive at L2 — the
**fusion-rotation** rendering of `y_new = α·x + y_old`. Consumes a scalar `α` and two
tensors `x`, `y` of the same length axis; produces a fresh tensor whose every element is
`α` times the corresponding element of `x` plus the corresponding element of `y`. `axpy`
is the **arity-2 member of the firm [`linear_combination`](./linear_combination.md) fold**
(`scal`/`axpy`/`axpby`/`axpbypcz` are its arity-1/2/2/3 specializations; `axpy` is the
arity-2 case with the *second* coefficient fixed to 1); this entry is the standalone leaf,
cited as a fold-specialization of `linear_combination` but **not merged into it** (the
fold-cohort boundary in `book/src/L2/index.md` §"Fold-cohort boundary" is load-bearing).
Companion to L1 [`axpy`](../L1/axpy.md) (the mutation-lifted form of the same primitive)
and L3 [`axpy`](../L3/axpy.md) (the iteration-rotation rendering); the rotation L1 ↔ L2 is
identity-in-form because `axpy` is a leaf field operation with no multi-operation kernel
fusion to unfold beyond the single aligned `α·x + y` pass (the arity-2 case of the fold's
fusion note).

## Context

L2 is the fusion-rotation layer (`book/src/L2/index.md`): "Kernel fusion across multiple
algebraic operations is unfolded into composition… Batched specialized BLAS calls are
written as compositions of base primitives." The L2 vocabulary explicitly names `axpy`
among its base primitive operations (`book/src/L2/index.md:17` — "primitive operations
(axpy, dot, matvec, gemv, trsv, scal, nrm2, …)"). `axpy` at L2 is the base
scalar-vector-fused-update primitive in that vocabulary — a single field operation
parameterised by a scalar `α` and acting pointwise over the length axis, fusing one scaled
add into one aligned pass.

**`axpy` is the arity-2 member of the `linear_combination` fold, cited but not merged.**
The firm [`linear_combination`](./linear_combination.md) entry (cycle-018) is the
arity-family unification of the BLAS-1 scalar-weighted-sum cohort: its four fixed-arity
leaves (`scal`/`axpy`/`axpby`/`axpbypcz`) are the arity-1/2/2/3 specializations of one
variadic `foldl` over a list of `(scalar, tensor)` terms. `axpy` is the arity-2
specialization with the **second coefficient fixed to 1**:
`axpy(α, x, y) = linear_combination [(α, x), (1, y)]` (`linear_combination.md` §Signature
line 69, §Algebraic-laws law 6). The fixed-1 second coefficient is exactly what
distinguishes `axpy` from `axpby` (arity-2 with a *free* second coefficient) — the two
share the arity but differ on whether the `y`-term's scalar is pinned. The fold **does not
replace the leaves** — the `axpby-as-primitive` decision
([`scaffolding/decisions/axpby-as-primitive.md`](../../../scaffolding/decisions/axpby-as-primitive.md))
keeps each leaf firm (fuse, don't decompose), and the L2 index §"Fold-cohort boundary"
makes the do-NOT-merge boundary load-bearing. So `axpy` has its own L2 floor entry as a
leaf, and that leaf is **also** a recognized arity-2 specialization of the fold — the two
relationships coexist by design.

This is a thin **floor presence** entry. It exists so the firm L3 [`axpy`](../L3/axpy.md)
(cycle-011) rests on a present adjacent L2 parent, per the methodology invariant
**Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants,
cycle-009 codification): each layer is coherent within itself, and a reader at L2 must
find `axpy` defined in L2 vocabulary without reaching down to L1 or up to L3. The
foundation-first directive `l2-floor-under-l3-leaf-cohort` (2026-05-31) names exactly this
gap: the L3 BLAS-1 cohort (`axpy`/`axpby`/`axpbypcz`/`dot`/`nrm2`/`scal`) was backfilled to
L3 in cycle-011 without the corresponding L2 floor entries being present, so the L3 cohort
rests on the L1 leaves directly. The sibling arity-1 floor [`scal`](./scal.md) landed
cycle-041 D3 under this directive; this dispatch floors the arity-2 `axpy`, mirroring that
precedent.

A cross-cutting prose treatment lives at [`concepts/axpy`](../concepts/axpy.md) — covering
BLAS background (BLAS-1 `daxpy` / `zaxpy`), fusions (`α = 1` vector add, `α = -1` vector
subtract), and roll-up usage across slices (residual updates, Krylov basis corrections,
search-direction accumulation). The L2 entry here is the firm operator definition at the
fusion-rotation layer; the concept page is the narrative. The scalar-promotion sub-axis
(real `α` against complex `x, y`) is covered at
[`concepts/scalar-promotion`](../concepts/scalar-promotion.md).

## Signature

    axpy :: Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]
    axpy α x y = α·x + y

Shape contract (bunsen-style, named axes; positional values, no monadic effect, no
destination buffer):

- **`α`** — scalar (`real` or `complex`, matching the tensor element type per the
  element-type variant axis; or promoted from `real` to `complex` against complex `x, y`
  per the scalar-promotion sub-axis).
- **`x`** — `Tensor[N]` — the scaled input tensor with a single length axis `N`. Read-only
  at L2 (the L2 form is pure / out-of-place; the L0 in-place mutation is reintroduced only
  at the L1>L0 lowering). Enters scaled by `α`.
- **`y`** — `Tensor[N]` — the additive input tensor (the *prior* value), same axis `N`.
  Read-only at L2. Enters unscaled (its implicit coefficient is the fixed 1).
- **result** — `Tensor[N]` — same axis `N` as `x` and `y`. Every output element equals
  `α` times the corresponding element of `x` plus the corresponding element of `y`.

The L2 signature is **identical to the L1 signature** modulo notation; the rotation is
identity-in-form. As the arity-2 fold specialization, the same operator is
`linear_combination [(α, x), (1, y)]` (per `linear_combination.md` line 69) — but the
standalone leaf form is the canonical L2 rendering, with the fold view recorded as a
derived identity (the fold-specialization identity below), not as a decomposition. The
fixed-1 coefficient on the `y`-term is what distinguishes `axpy` from the free-second-coeff
`axpby` at the same arity.

## Semantics

`axpy` at L2 is a single base tensor-algebra field operation: a value-threaded
transformation `(α, x, y) -> r` where `r[i] = α · x[i] + y[i]` for every element index
`i ∈ [0, N)`. The operator is **element-local** (every output element depends on exactly
one input element from each of `x` and `y` plus the shared scalar `α`), **reduction-free**
(no cross-element communication), and **rank-local** (no MPI collective at any layer; ranks
own disjoint slices of `N` and apply the fused update independently — contrast `dot` /
`nrm2`, which reduce over `N` and do carry an MPI collective).

It is **pure / out-of-place** at L2: it consumes `α`, the prior `x`, and the prior `y` and
produces a fresh tensor; no destination buffer appears in the signature. The L0 in-place
receiver-mutating idiom (`y.Add(α, x)` / `y.AXPY(α, x)`, where the destination `y` aliases
the third argument) is an L2>L1 (and onward L1>L0) lowering concern, captured by the
output-aliasing direction of the lowering themes — not by the L2 algebra. (The
output-aliasing axis is the **fold's**, inherited; see Variant axes.)

**Leaf, with the single aligned-pass fusion note.** L2 is the layer where kernel fusion
across multiple algebraic operations is unfolded into composition. `axpy` is a **leaf** in
that vocabulary — there is no multi-operation fusion to unfold (it is a single fused scaled
add `α·x + y`, not a chained `α·x + β·y + γ·z` pass requiring de-composition into base
primitives). The one fusion note it carries is the **arity-2 case of the
`linear_combination` fold's fusion note**: the single aligned strided pass computing
`α·x[i] + y[i]` per element is the seed-and-accumulate fold collapsed to two terms (the
`foldl` over `[(α, x), (1, y)]` reduces to one scaled accumulate of `x` into `y` as the
running sum). This is the transparent-performance-trick implementation of the arity-2 fold;
L2 records it as one note (deferred to `linear_combination` §"Fusion note", which covers
the whole arity family's aligned-pass mechanics) and otherwise treats `axpy` as the base
primitive it is.

Special algebraic cases — `α = 0` (identity in the second argument, returns `y`), `α = 1`
(vector add, `x + y`), `α = -1` (vector subtract, `y − x`), `x = 0` (identity in the first
argument, returns `y`) — are not separate operators at L2. They are algebraic identities
recorded in the laws below, inherited from L1. The L0 source **does** carry one
constant-folding branch on the value of `α`: the real-real free function
`AXPY(double, Vector, Vector)` branches on `α == 1.0` to call `y += x` (MFEM
`operator+=`) rather than `y.Add(1.0, x)` (`palace/linalg/vector.cpp:702-712`, branch at
`:704`). This is a **transparent performance trick** (algebraically equivalent to the
unfolded form; classified at [`transparent-vs-load-bearing-tricks`](../L0/transparent-vs-load-bearing-tricks.md) per the L1 entry)
that has already been erased at L1; it does not reappear at L2.

## Algebraic laws

The six laws that hold at L1 (per `book/src/L1/axpy.md` §Algebraic laws) hold unchanged at
L2. The rotation L2 ↔ L1 is identity-in-form on the operator's body and signature, so the
algebraic properties of the affine vector update transport without modification. Absences
are deliberate and inherited.

1. **Identity in `α`**: `axpy(0, x, y) = y` for any `x`.
2. **Identity in `x`**: `axpy(α, 0, y) = y` for any `α`, where `0` is the zero tensor of
   axis `N`.
3. **Left distribution over tensor addition in `y`**:
   `axpy(α, x, y₁ + y₂) = axpy(α, x, y₁) + y₂`. Both sides equal `α·x + y₁ + y₂`.
4. **Scalar linearity in α (additive collapse)**:
   `axpy(α, x, axpy(β, x, y)) = axpy(α + β, x, y)` — two successive axpy's against the same
   `x` collapse to one with summed scalar.
5. **Scalar absorption**: `axpy(α·β, x, y) = axpy(α, β·x, y)` — the scalar absorbs into
   either side (the `α`-coefficient or the `x`-term).
6. **Vector linearity in x (additive expansion)**:
   `axpy(α, x₁ + x₂, y) = axpy(α, x₁, axpy(α, x₂, y))`. This law underwrites the L2
   unfolding of GMRES basis-correction sums into axpy chains (and is the arity-2 shadow of
   the `linear_combination` concatenation-homomorphism, law 2).

**Fold-specialization identity (the link to `linear_combination`, NOT a merge):**

- `axpy(α, x, y) = linear_combination [(α, x), (1, y)]` — `axpy` is the arity-2
  specialization of the firm [`linear_combination`](./linear_combination.md) fold, with the
  **second coefficient fixed to 1** (`linear_combination.md` §Signature line 69,
  §Algebraic-laws law 6). The fold's concatenation-homomorphism
  (`linear_combination.md` law 2) makes the four arities one fold; the leaf laws above are
  the arity-2 shadow of the fold's laws (law 3 here = `linear_combination.md` law 2
  concatenation specialized to splitting off the unit-coefficient `y`-term; law 4 here =
  `linear_combination.md` law 4 coefficient-scaling on the `x`-term; laws 5–6 here = the
  multilinearity / distributivity the fold generalizes). The leaf stays firm and
  standalone; the fold view is a derived identity, not a decomposition (do-NOT-merge per
  the fold-cohort boundary). The fixed-1 `y`-coefficient is the load-bearing difference from
  `axpby` (free second coefficient): erasing the leaf into the fold would lose the one-to-one
  `axpy` ↔ L0 `AXPY`-symbol shape the L1>L0 mutation rotation relies on.

Laws that explicitly **do not** hold (the first two inherited from L1; the IEEE-754
FP-summation non-law made explicit at L2):

- **Commutativity in the tensor arguments**: `axpy(α, x, y) ≠ axpy(α, y, x)`. The second
  argument `x` enters scaled by `α`; the third argument `y` enters unscaled (its
  coefficient is the fixed 1). Swapping them changes the value (unless `α = 1`).
- **Associativity as a binary algebra**: `axpy` is ternary; "associativity" is not even
  well-typed for it.
- **Floating-point associativity in the summation**: `α·x + y` in IEEE-754 may differ at
  the bit level from any reordering when the magnitudes of `α·x` and `y` differ enough to
  lose precision; and the fused single-pass form (`y.Add(α, x)`) may differ bit-for-bit
  from a two-pass `scal(α, x)` then `+ y`. The L2 form is order-agnostic algebraically;
  bit-identical reproduction of any L0 call requires matching that call's pinned summation
  order (pinned by MFEM's `Add` kernel / the `α == 1.0` fast path). Made explicit at L2
  (not among L1/axpy's two non-laws; added here under the load-bearing-numerical-trick
  methodology), recorded, not erased. (At the fold level, this is the arity-2 shadow of the
  `linear_combination` permutation non-law's summation-order load-bearing concern.)

## Dependencies

**Same-layer (L2)**: none as a constituent. `axpy` is a leaf primitive at L2 just as it is
at L1 — the fused scalar-vector update does not decompose into other L2 primitives. The
body is a single field operation; the sub-operations (scalar multiplication and per-element
addition) are below the L2 layer's resolution. (`axpy` does NOT depend on `scal` + a
tensor-add at L2: it is the *fused* primitive, kept whole per the `axpby-as-primitive`
fuse-don't-decompose decision; the de-fused two-pass form is the fold's seed-and-accumulate
realization, recorded as the fusion note, not as an L2 dependency.)

**Fold-parent (cited, NOT merged)**:

- [`linear_combination`](./linear_combination.md) (firm cycle-018) — the term-axis
  arity-family fold of which `axpy` is the **arity-2 member, second coefficient fixed to 1**
  (`axpy(α, x, y) = linear_combination [(α, x), (1, y)]`). `axpy` stays a firm standalone L2
  leaf; `linear_combination` is the form the four leaves (`scal`/`axpy`/`axpby`/`axpbypcz`)
  fuse *up* into, not a replacement. The do-NOT-merge boundary
  (`book/src/L2/index.md` §"Fold-cohort boundary") is load-bearing — merging the leaf into
  the fold would erase the one-to-one leaf↔L0-symbol shape that the L1>L0 mutation rotation
  relies on, and would lose the fixed-1 `y`-coefficient that distinguishes `axpy` from
  `axpby` at the same arity.

**Cross-cutting concepts**:

- [`scalar-promotion`](../concepts/scalar-promotion.md) — the implicit-coercion typing rule
  for real `α` against complex `x, y`. Collapsed at L1 / L2 / L3 into a single operator
  parameterised by the `real ⊑ complex` scalar lattice.
- [`axpy` (concept)](../concepts/axpy.md) — cross-cutting prose treatment; BLAS-1
  background (`daxpy` / `zaxpy`) and call-site role (residual update, Krylov basis
  correction, search-direction accumulation).

**Sibling subsumption (not dependency)**:

- `axpy(α, x, y) = axpby(α, x, 1, y)` — `axpy` is the `β = 1` specialization of `axpby`
  (per `book/src/L1/axpby.md` law 1). `axpy` stays in the L2 dep-map as a sibling leaf, not
  a sub-operation of `axpby` (per the harvester decision at
  `scaffolding/decisions/axpby-as-primitive.md` — fuse, keep both leaves firm).
- `scal(α, x) = axpy(α, x, 0)` — `scal` is the `y = 0` (degenerate additive-term)
  specialization of `axpy`. Likewise a sibling-leaf relationship, not a dependency.

**Lowering themes (forthcoming; D6 this cycle — plain-text forward-reference, files do not
yet exist)**: an `L2-L1/axpy-fusion` theme will narrate how the L2 leaf lowers into the L1
leaf (identity-in-form; the only fusion content is the arity-2 single-aligned pass), and
the L3>L2 identity rotation for `axpy` is the iteration-rotation re-erasure recorded in-line
at the L3 entry. The L1>L0 in-place mutation is already firm at
[`axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md) sub-pattern A (which covers
`axpy` as the β=1 specialization of `axpby`). Forward-reference only — the L2>L1 chapter
does not yet exist; do not link it.

## Variant axes

The two variant axes are inherited unchanged from L1. Both are absorbed at construction
time (the element-type axis through overload selection at L0; the scalar-promotion sub-axis
through the real-α-on-complex-vector forwarding overload); neither appears in the L2
positional signature.

1. **element-type** (`real` | `complex`). The L0 source has separate overloads: the
   real-real free function `AXPY(double, Vector, Vector)` at
   `palace/linalg/vector.cpp:702-712` (with the `α == 1.0` fast-path); the complex
   member-method `ComplexVector::AXPY` at `palace/linalg/vector.hpp:115-118` /
   `palace/linalg/vector.cpp:276-311`; and the free-function template
   `AXPY(ScalarType, const VecType &, VecType &)` at `palace/linalg/vector.hpp:305-307`. At
   L1 / L2 / L3 these collapse to one operator parameterised by element type — the
   semantics are identical (per-element fused scaled add in the appropriate field).
2. **scalar-promotion** (sub-axis on the complex element-type). See
   [`concepts/scalar-promotion`](../concepts/scalar-promotion.md) — real `α` against complex
   `x, y` via the real-α-on-complex-vector forwarding overload
   `AXPY(double, ComplexVector, ComplexVector)` at `palace/linalg/vector.cpp:714-718`
   (forwarding to `y.AXPY(alpha, x)` with the `double` `α` promoted to
   `std::complex<double>`). At L1 / L2 / L3 this is one operator with `α` typed through the
   `real ⊑ complex` scalar lattice.

**Output aliasing (the FOLD's axis, NOT a leaf-specific axis).** The in-place form
(`y ← α·x + y`, where the third argument `y` aliases the output buffer) is the case where
one term's tensor aliases the output. Per the fold-parent entry
([`linear_combination`](./linear_combination.md) §Variant axes, axis 1), **output aliasing
is the FOLD's variant axis — orthogonal to arity, not a per-leaf axis**: every arity ≥ 1
has both an aliasing form (the receiver-mutating / output-arg L0 idioms) and a fresh-output
form. At L2 the leaf is pure / out-of-place; aliasing is an L2>L1 lowering concern carried
by the fold's axis, NOT introduced as an `axpy`-leaf-specific variant axis. This entry
therefore lists only the two element-type axes; the aliasing axis is named here as the
fold's, by reference (recorded under OQ
`arity-family-leaf-floors-output-aliasing-axis-is-the-folds`).

The variant-axis count matches the L1 and L3 entries exactly (two axes; element-type with
scalar-promotion as sub-axis). No new axes introduced by the L2 rendering; no axes merged
or split. The output-aliasing axis is the fold's, carried by reference.

## Status

`firm` — signature is canonical (matches BLAS-1 `daxpy` / `zaxpy` and the Palace `AXPY`
free-function / `ComplexVector::AXPY` member surface exactly; identical to the L1 and L3
forms), and the six algebraic laws are standard affine-vector-update facts. **Firm-on-positive-structure**:
the `axpy` L0 surface is small, fully present, and positively cited
(`palace/linalg/vector.{hpp,cpp}` + inlined call sites), and every law is a syntactic
identity on that closure — the absence of a dedicated `axpy` unit test does not gate firm
(the syntactic-identity-laws-on-positive-source escape, the `apply_linop` situation, not
the `eigsolve`-convergence-semantics situation; the same escape ratified for the sibling
[`scal`](./scal.md) floor cycle-041 and for `linear_combination` cycle-018). This dispatch
is the **L2 floor backfill** (cycle-043 D3) under the foundation-first directive
`l2-floor-under-l3-leaf-cohort`: the L2 form was previously referenced only as the arity-2
leaf of `linear_combination` and inside `krylov-step` / `orthogonalize` /
`divfree-projector` / `chebyshev-iteration` dependency lists; it now has its own L2 entry
per **Identity-lowerings still require both L levels**. The leaf-vs-fold fork
(`dot-l2-leaf-floor-vs-fold-only-design`) is **resolved keep-(b)** (batch-12 meta-phase, per
the c042 cross-cutter audit) — this entry presupposes the (b) same-named-floor realization,
consistent with the landed `scal` / `dot` / `nrm2` cohort.

## Lowers to

L2 `axpy` lowers to L1 [`axpy`](../L1/axpy.md) via an **identity-in-form** rotation: the
signature `Scalar -> Tensor[N] -> Tensor[N] -> Tensor[N]` is textually identical at both
layers; the body is the same fused scalar-vector field operation. There is no
multi-operation kernel fusion to unfold beyond the arity-2 single-aligned pass (the arity-2
case of the `linear_combination` fold's fusion note). No firm `L2-L1/axpy-fusion` theme file
yet exists (the D6 dispatch this cycle authors the L2>L1 lowering themes for the BLAS-1
floor cohort); this entry captures the identity rotation in-line, following the L3 `axpy` /
L2 `scal` backfill precedents for in-line identity-rotation annotation. The L0 in-place
mutation is reintroduced at the firm L1>L0 lowering
[`axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md) sub-pattern A (which covers
`axpy` as the β=1 specialization of `axpby`).

## Lifts from

L1 `axpy` lifts to this L2 entry via the **value-thread-isomorphic** identity rotation: the
L1 form's signature has no kernel fusion exposed beyond the single aligned pass, no
destination buffer, no MPI collective — these are exactly the properties that make it
L2-native by construction as a base tensor-algebra primitive. The L2 entry exists for
layer-coherence reasons — a reader navigating L2 must find `axpy` defined in L2 vocabulary
as the base fused-update primitive (and as the arity-2 member of the `linear_combination`
fold), not have to reach down to L1 to recover the field-operation shape.

## Evidence

The L2 form is value-thread-isomorphic to the L1 form; all L0 evidence is sourced from the
firm L1 entry. Direct citations relevant to this L2 entry:

- `book/src/L1/axpy.md` (cycle-002 firm) — the L1 form this L2 entry value-thread-mirrors.
  Body shape, signature, semantics (element-local, reduction-free, rank-local), the six
  algebraic laws, two non-laws, variant axes (two: element-type, scalar-promotion sub-axis),
  and L0 evidence chain.
- `book/src/L1-L0/axpby-mutation-rotation.md` (firm) — the L1>L0 mutation rotation;
  sub-pattern A covers `axpy` (β=1 specialization of `axpby`) — the in-place
  `y.Add(α, x)` / `y.AXPY(α, x)` receiver-mutating idiom the L2 pure form abstracts over.
- `book/src/L3/axpy.md` (cycle-011 firm) — the L3 consumer this floor entry supports;
  identical signature and laws, iteration-rotation framing.
- `book/src/L2/linear_combination.md` (cycle-018 firm) — the fold-parent. `axpy` is its
  arity-2 specialization (`linear_combination.md` §Signature line 69:
  `axpy(α, x, y) = linear_combination [(α, x), (1, y)]`; §Algebraic-laws law 6
  specialization identities). Cited as fold-parent, NOT merged (fold-cohort boundary
  load-bearing).
- `book/src/L2/scal.md` (cycle-041 D3 firm) — the sibling arity-1 floor; the exact template
  this entry mirrors (floor-presence framing, fold-membership-cited-not-merged, in-line
  identity-rotation annotation, firm-on-positive-structure escape).
- `book/src/L2/index.md:17` — L2 vocabulary inventory naming `axpy` among the base
  primitive operations; §"Fold-cohort boundary" — the load-bearing do-NOT-merge note.
- `scaffolding/decisions/axpby-as-primitive.md` — the fused-leaf decision; governs the
  L1/L2 leaf-vs-decompose choice (keep leaves firm, fuse up into the fold, don't merge).
- `book/src/concepts/axpy.md` — pre-existing cross-cutting prose treatment; consistent with
  this L2 entry's framing.
- `book/src/concepts/scalar-promotion.md` — the typing rule for the scalar-promotion
  sub-axis.

**L0 evidence (canonical anchors, self-verified via codemap `read_range` + on-disk
`citecheck --anchor`, 2026-06-01)**:

- `palace/linalg/vector.cpp:702-712` — free function `AXPY(double, Vector, Vector)` (the
  real-real arity-2-coeff-1 leaf), with the `α == 1.0` fast-path branch at `:704`
  (`y += x` else `y.Add(alpha, x)`) — the transparent constant-folding trick erased at L1.
- `palace/linalg/vector.cpp:714-718` — `AXPY(double, ComplexVector, ComplexVector)`, the
  real-α-on-complex-vector forwarding overload (`y.AXPY(alpha, x)` with `double` `α`
  promoted) — the internal scalar-promotion site.
- `palace/linalg/vector.cpp:720-724` — the complex-α overload
  `AXPY(std::complex<double>, ComplexVector, ComplexVector)` forwarding to the
  member `ComplexVector::AXPY`.
- `palace/linalg/vector.cpp:276-311` — `ComplexVector::AXPY` definition and the element-wise
  `forall_switch` kernels (`YR[i] += ar·XR[i] − ai·XI[i]`).
- `palace/linalg/vector.hpp:115-118` — `ComplexVector::AXPY` and `Add` / `Subtract` aliases
  declared, comment `In-place addition (*this) += alpha * x.`
- `palace/linalg/vector.hpp:305-307` — free-function template
  `AXPY(ScalarType alpha, const VecType &x, VecType &y)` declared, comment
  `Addition y += alpha * x.`

## L2 vs L1 distinction

- **L1**: mutation-lifted pure functional update. `y_new = axpy(α, x, y_old)`. Frames the
  operator as the pure-functional image of the L0 receiver-mutating `Add` / `AXPY`
  member-method (and free-function) idiom; emphasises the *mutation rotation* against the
  source (the destination-buffer drop and the `α == 1.0` fast-path erasure).
- **L2**: base tensor-algebra field operation. `r = axpy(α, x, y)`. Frames the operator as
  a leaf primitive in the fusion-rotation layer's base vocabulary — and as the **arity-2
  member of the `linear_combination` fold** (cited, not merged; second coefficient fixed to
  1); emphasises that there is no multi-operation kernel fusion to unfold (the only fusion
  note is the arity-2 single-aligned pass). The L2 form is **identical in body and signature
  to L1** — the framing differs (mutation rotation at L1 vs fusion rotation + fold-membership
  at L2), but no operational adjustment occurs.

The L2 ↔ L1 rotation is identity-in-form on the body and signature; the surface adjustment
is documentary. The methodology invariant **each layer is coherent within itself** is what
compels the L2 entry to exist as its own anchor — and the foundation-first directive
`l2-floor-under-l3-leaf-cohort` is what schedules it, so the firm L3 [`axpy`](../L3/axpy.md)
rests on a present adjacent L2 parent.
