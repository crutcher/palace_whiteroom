---
layer: L2
operator: axpby
firmness: firm
lowers_to:
  - book/src/L1/axpby.md (identity-in-form; whole-tensor in/out at both layers; no kernel fusion to unfold beyond the arity-2 single-aligned pass, which is the fold's fusion note — no firm `L2-L1/axpby-fusion` theme yet, D7 this cycle authors it; in-line below at "Lowers to")
lifts_from:
  - book/src/L1/axpby.md (value-thread-isomorphic; same fused-primitive signature shape; whole-tensor leaf, the fused `α·x + β·y` pass is preserved as a primitive statement of the linear combination, not unfolded)
fold_parent:
  - book/src/L2/linear_combination.md (arity-2 member of the term-axis fold; cited, NOT merged — fold-cohort boundary is load-bearing)
variant_axes:
  - element-type (real / complex)
  - scalar-promotion (real-(α,β)-against-complex-vectors via concepts/scalar-promotion)
---

# axpby

Fused two-scalar two-vector update as a base tensor-algebra primitive at L2 — the
**fusion-rotation** rendering of `y = α·x + β·y`. Consumes two scalars `α, β` and two
tensors `x, y` of one shared length axis `N`; produces a fresh tensor whose every element
is `α·x[i] + β·y[i]`. `axpby` is the **arity-2 member of the firm
[`linear_combination`](./linear_combination.md) fold** (`scal`/`axpy`/`axpby`/`axpbypcz`
are its arity-1/2/2/3 specializations); this entry is the standalone leaf, cited as a
fold-specialization of `linear_combination` but **not merged into it** (the fold-cohort
boundary in `book/src/L2/index.md` §"Fold-cohort boundary" is load-bearing). Companion to
L1 [`axpby`](../L1/axpby.md) (the mutation-lifted form of the same primitive) and L3
[`axpby`](../L3/axpby.md) (the iteration-rotation rendering); the rotation L1 ↔ L2 is
identity-in-form because `axpby` is a leaf field operation whose single fused
`α·x + β·y` pass is the arity-2 case of the fold's fusion note, with no further
multi-operation kernel fusion to unfold.

## Context

L2 is the fusion-rotation layer (`book/src/L2/index.md`): "Kernel fusion across multiple
algebraic operations is unfolded into composition… Batched specialized BLAS calls are
written as compositions of base primitives." The L2 vocabulary names `axpy` (and by the
arity family `axpby`) among its base primitive operations (`book/src/L2/index.md:17` —
"primitive operations (axpy, dot, matvec, gemv, trsv, scal, nrm2, …)"). `axpby` at L2 is
the base fused two-scalar two-vector linear-combination primitive in that vocabulary — a
single field operation parameterised by two scalars `α, β` and acting pointwise over the
length axis `N` to compute `α·x + β·y`.

**`axpby` is the arity-2 member of the `linear_combination` fold, cited but not merged.**
The firm [`linear_combination`](./linear_combination.md) entry (cycle-018) is the
arity-family unification of the BLAS-1 scalar-weighted-sum cohort: its four fixed-arity
leaves (`scal`/`axpy`/`axpby`/`axpbypcz`) are the arity-1/2/2/3 specializations of one
variadic `foldl` over a list of `(scalar, tensor)` terms, with
`axpby(α, x, β, y) = linear_combination [(α, x), (β, y)]` recorded as the arity-2
specialization identity (`linear_combination.md` §Signature line 70, §Algebraic-laws
law 6). The fold **does not replace the leaves** — the `axpby-as-primitive` decision
([`scaffolding/decisions/axpby-as-primitive.md`](../../../scaffolding/decisions/axpby-as-primitive.md))
keeps each leaf firm (fuse, don't decompose), and the L2 index §"Fold-cohort boundary"
makes the do-NOT-merge boundary load-bearing — merging the leaf into the fold would erase
the one-to-one leaf↔L0-symbol shape (`axpby` ↔ `linalg::AXPBY` /
`ComplexVector::AXPBY`) that the L1>L0 mutation rotation relies on. So `axpby` has its own
L2 floor entry as a leaf, and that leaf is **also** the recognized arity-2 specialization
of the fold — the two relationships coexist by design.

This is a thin **floor presence** entry. It exists so the firm L3 [`axpby`](../L3/axpby.md)
(cycle-011) rests on a present adjacent L2 parent, per the methodology invariant
**Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants,
cycle-009 codification): each layer is coherent within itself, and a reader at L2 must
find `axpby` defined in L2 vocabulary as the base fused-linear-combination primitive
without reaching down to L1 or up to L3. The foundation-first directive
`l2-floor-under-l3-leaf-cohort` (2026-05-31) names exactly this gap: the L3 BLAS-1 cohort
(`axpy`/`axpby`/`axpbypcz`/`dot`/`nrm2`/`scal`) was backfilled to L3 in cycle-011 without
the corresponding L2 floor entries being present. This dispatch floors `axpby`; the
sibling BLAS-1 floor entries `scal` (cycle-041 D3) and `axpy` (co-dispatched this cycle,
D3) are the same-named leaf-floor pattern this entry mirrors.

A cross-cutting prose treatment for `axpby` specifically does not yet exist (the existing
[`concepts/axpy`](../concepts/axpy.md) covers `axpy` only); if an `axpby` concept page is
authored, it should cross-reference this entry. The scalar-promotion sub-axis (real
`(α, β)` against complex vectors) is covered at
[`concepts/scalar-promotion`](../concepts/scalar-promotion.md). The L2 entry here is the
firm operator definition at the fusion-rotation layer; the concept page (when authored)
and the typing rule are the narrative.

## Signature

```text
axpby :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]
axpby α x β y = α·x + β·y
```

Shape contract (bunsen-style, named axes; positional values, no monadic effect, no
destination buffer):

- **`α`** — scalar (`real` or `complex`, matching the vector element type per the
  element-type variant axis; or promoted from `real` to `complex` against complex
  vectors per the scalar-promotion sub-axis; promoted all-or-none with `β`).
- **`x`** — `Tensor[N]` — first input tensor with a single length axis `N`. Read-only at
  L2 (the L2 form is pure / out-of-place; the L0 in-place mutation is reintroduced only
  at the L1>L0 lowering).
- **`β`** — scalar (same type as `α`; the scalar pair shares one type and the vector
  element type).
- **`y`** — `Tensor[N]` — second input tensor (the *prior* value when `axpby` is used as
  a fused update); read-only at L2.
- **result** — `Tensor[N]` — same axis `N` as `x` and `y`. Every output element equals
  `α·x[i] + β·y[i]`.

`x` and `y` must share the same length axis `N` and the same element type (both real or
both complex). The L2 signature is **identical to the L1 signature** modulo notation; the
rotation is identity-in-form. As the arity-2 fold specialization, the same operator is
`linear_combination [(α, x), (β, y)]` (per `linear_combination.md` line 70) — but the
standalone leaf form is the canonical L2 rendering, with the fold view recorded as a
derived identity (the fold-specialization identity below), not as a decomposition.

## Semantics

`axpby` at L2 is a single base tensor-algebra field operation: a value-threaded
transformation `(α, x, β, y) -> r` where `r[i] = α·x[i] + β·y[i]` for every element index
`i ∈ [0, N)`. The operator is **element-local** (every output element depends on exactly
one input element from each of `x` and `y` plus the two shared scalars),
**reduction-free** (no cross-element communication), and **rank-local** (no MPI
collective at any layer; ranks own disjoint slices of `N` and apply the fused update
independently — contrast `dot` / `nrm2`, which reduce over `N` and do carry an MPI
collective).

It is **pure / out-of-place** at L2: it consumes `α`, the prior value of `x`, `β`, and
the prior value of `y`, and produces a fresh tensor; no destination buffer appears in the
signature. The L0 in-place idioms (the receiver-mutating `ComplexVector::AXPBY(α, x, β)`
writing through `*this`, and the output-arg `linalg::AXPBY(α, x, β, y)` writing through
`y`) are an L2>L1 (and onward L1>L0) lowering concern — captured by the output-aliasing
variant axis **of the fold** (`linear_combination.md` §Variant-axes axis 1), not by this
leaf's L2 algebra.

**Leaf, with the fused pass as the fold's arity-2 fusion note.** L2 is the layer where
kernel fusion across multiple algebraic operations is unfolded into composition. `axpby`
is a **leaf** in that vocabulary — the single fused `α·x + β·y` pass is **not** unfolded
into a two-pass `scal(β, y)` then `axpy(α, x, ·)` chain, because the fusion preserves
the algebraic statement `α·x + β·y` as a primitive linear combination (the
`axpby-as-primitive` decision; the fused form rounds once where the two-pass form rounds
twice — see the non-laws). The one fusion note `axpby` carries is the **arity-2 case of
the `linear_combination` fold's fusion note**: the single aligned strided pass computing
`α·x[i] + β·y[i]` per element — realized at L0 by MFEM's `add(α, x, β, y, y)` 5-arg
in-place linear-combine (`palace/linalg/vector.cpp:726-730`, the real-real path) — is the
fold's seed-and-accumulate collapsed to two terms. **Fusion content is deferred to the
fold-parent's §"Fusion note"** (`linear_combination.md` §"Fusion note"); this leaf entry
records only that the arity-2 single-aligned pass is the fusion realization and otherwise
treats `axpby` as the base fused-linear-combination primitive it is.

Special algebraic cases — `α = 0` (pure scaling of `y`), `β = 0` (pure scaling of `x`,
discards `y`), `α = 1, β = 1` (vector add), `β = 1` (recovers `axpy`),
`α = -1, β = 1` (vector subtract) — are not separate operators at L2. They are algebraic
identities recorded in the laws below, inherited from L1. The L0 source has **no**
constant-folding branches inside the `AXPBY` family on the values of `α` or `β` (unlike
`axpy`'s real-path `α == 1.0` fast-path) — the L0 surface uniformly delegates
(`vector.cpp:726-730` real-real → `add`; `:732-737` complex-complex and `:739-743`
real-scalar-on-complex → the member form) without inspecting scalar values, per
`book/src/L1/axpby.md` §Semantics.

## Algebraic laws

The nine laws that hold at L1 (per `book/src/L1/axpby.md` §Algebraic laws) hold unchanged
at L2. The rotation L2 ↔ L1 is identity-in-form on the operator's body and signature, so
the algebraic properties of the fused linear combination transport without modification.
Absences are deliberate and inherited.

1. **Subsumption of `axpy`**: `axpby(α, x, 1, y) = axpy(α, x, y) = α·x + y`. The
   load-bearing identity from `scaffolding/decisions/axpby-as-primitive.md`: `axpy` is the
   β=1 specialisation of `axpby`, not a dependency. Both stay firm L2 floor leaves as
   siblings.
2. **Identity in `α`**: `axpby(0, x, β, y) = β·y` for any `x`. (Equals `scal(β, y)` per
   the L2 [`scal`](./scal.md) leaf — `axpby` at `α=0` is the arity-1 specialization in
   the `y` term.)
3. **Identity in `β`**: `axpby(α, x, 0, y) = α·x` for any `y`. (Equals `scal(α, x)`.)
4. **Identities in both**: `axpby(0, x, 0, y) = 0` (the zero tensor of axis `N`).
5. **Bilinearity in the scalar pair `(α, β)`**: `axpby(α, x, β, y)` is linear separately
   in each of `α` and `β` (with the other scalar and both tensors held fixed). Inherited
   from L1 Law 5; the arity-2 instance of `linear_combination.md` law 3 (multilinearity
   in the scalar list).
6. **Right distribution over tensor addition in `x`**:
   `axpby(α, x₁ + x₂, β, y) = axpby(α, x₁, β, y) + axpby(α, x₂, 0, y) = α·x₁ + α·x₂ + β·y`
   (the `axpby(α, x₂, 0, y)` term is `α·x₂` per law 3; the `+` is element-wise tensor
   addition).
7. **Right distribution over tensor addition in `y`**:
   `axpby(α, x, β, y₁ + y₂) = axpby(α, x, β, y₁) + β·y₂ = α·x + β·y₁ + β·y₂`.
8. **Scalar absorption**:
   `axpby(α·γ, x, β, y) = axpby(α, γ·x, β, y) = axpby(α, x, β·γ, γ⁻¹·y)` (the latter only
   for invertible scalar `γ`) — the scalars absorb into their paired tensor. The arity-2
   instance of `linear_combination.md` law 4 (coefficient-scaling).
9. **Chained-`axpby` collapse on shared `x`**:
   `axpby(α₁, x, β₁, axpby(α₂, x, β₂, y)) = axpby(α₁ + β₁·α₂, x, β₁·β₂, y)`. Two
   successive `axpby` updates against the same `x` collapse to one with scalars
   `(α₁ + β₁·α₂, β₁·β₂)`. Generalises law 4 of `axpy` (the β₁ = β₂ = 1 case) and
   underwrites the L2 fusion of consecutive coefficient-update lines in Krylov solvers.

**Fold-specialization identity (the link to `linear_combination`, NOT a merge):**

- `axpby(α, x, β, y) = linear_combination [(α, x), (β, y)]` — `axpby` is the arity-2
  specialization of the firm [`linear_combination`](./linear_combination.md) fold
  (`linear_combination.md` §Signature line 70, §Algebraic-laws law 6). The fold's
  concatenation-homomorphism (`linear_combination.md` law 2) makes the four arities one
  fold: `axpby`'s 2-term list is `scal`'s 1-term list concatenated with another `scal`
  1-term list, so the leaf laws above are the arity-2 shadow of the fold's laws (law 5
  here = `linear_combination.md` law 3 multilinearity at length 2; law 8 here =
  `linear_combination.md` law 4 coefficient-scaling; laws 6–7 here = the
  distribution the fold's concatenation-homomorphism generalizes). The leaf stays firm
  and standalone; the fold view is a derived identity, not a decomposition (do-NOT-merge
  per the fold-cohort boundary).

Laws that explicitly **do not** hold (inherited from L1):

- **Commutativity in the tensor arguments**: `axpby(α, x, β, y) ≠ axpby(β, y, α, x)` in
  general unless `α = β` — the operator is symmetric in the inputs only because
  `α·x + β·y = β·y + α·x` mathematically, and the signature distinguishes argument slots
  by which scalar pairs with which tensor. Swapping both scalar-tensor pairs
  simultaneously preserves the value; swapping tensors without swapping scalars does not.
- **Associativity**: `axpby` is quaternary; "associativity" is not well-typed for the
  operator's argument list.
- **Floating-point associativity of the summation**: `α·x + β·y` computed in IEEE-754
  may differ from any reordering at the bit level when the magnitudes of `α·x` and `β·y`
  differ enough to lose precision in one ordering. The L2 algebra is order-agnostic for
  value; bit-identical reproduction of L0 output requires matching the L0 evaluation
  order pinned by MFEM's `add(α, x, β, y, y)` kernel (`vector.cpp:726-730`). This is the
  arity-2 shadow of the `linear_combination` permutation non-law's summation-order
  load-bearing concern (`linear_combination.md` §Algebraic-laws, paired permutation
  non-law). Recorded here, not erased.
- **Fusion identity with `scal + axpy`**: `axpby(α, x, β, y) ≠ scal(β, axpy(α/β, x, y))`
  in general at the bit level (the two-pass form rounds twice; the fused form rounds
  once) even though the values agree mathematically. The L0 form is fused for a reason;
  the L2 algebra preserves the fused statement. The fusion choice is load-bearing for
  bit-reproduction, transparent for value — the arity-2 instance of the fold's
  "bit-level fusion identity against the multi-pass form" non-law
  (`linear_combination.md` §Algebraic-laws).

## Dependencies

**Same-layer (L2)**: none as a constituent. `axpby` is a leaf primitive at L2 just as it
is at L1 — the fused two-scalar two-vector update does not decompose into other L2
primitives (the harvester decision `scaffolding/decisions/axpby-as-primitive.md` is
explicit: fuse, don't decompose). The body is a single fused field operation; the
sub-operations (two scalar multiplications and one element-wise add) are below the L2
layer's resolution.

**Fold-parent (cited, NOT merged)**:

- [`linear_combination`](./linear_combination.md) (firm cycle-018) — the term-axis
  arity-family fold of which `axpby` is the **arity-2 member**
  (`axpby(α, x, β, y) = linear_combination [(α, x), (β, y)]`). `axpby` stays a firm
  standalone L2 leaf; `linear_combination` is the form the four leaves
  (`scal`/`axpy`/`axpby`/`axpbypcz`) fuse *up* into, not a replacement. The do-NOT-merge
  boundary (`book/src/L2/index.md` §"Fold-cohort boundary") is load-bearing — merging the
  leaf into the fold would erase the one-to-one leaf↔L0-symbol shape that the L1>L0
  mutation rotation relies on. **All fusion content and the output-aliasing variant axis
  are the fold's**, deferred to `linear_combination.md` §"Fusion note" / §"Variant axes"
  — this leaf entry does not re-author them.

**Cross-cutting concepts**:

- [`scalar-promotion`](../concepts/scalar-promotion.md) — the implicit-coercion typing
  rule for real `(α, β)` against complex `x, y` (promote all-or-none across the scalar
  pair). Internal promotion at L0 via the real-scalar-on-complex-vector overload at
  `palace/linalg/vector.cpp:739-743`; collapsed at L1 / L2 / L3 into a single operator
  parameterised by the `real ⊑ complex` scalar lattice.

**Sibling subsumption (not dependency)**:

- `axpy(α, x, y) ≡ axpby(α, x, 1, y)` (law 1) — `axpy` is the β=1 specialisation;
  `scal(α, x) ≡ axpby(α, x, 0, y)` for any `y` (law 3) and `scal(β, y) ≡ axpby(0, x, β, y)`
  for any `x` (law 2). The L1/L2/L3 `axpy`, `scal`, and `axpby` leaves all stay in the
  dep-map as siblings, not sub-operations of one another (per the harvester decision at
  `scaffolding/decisions/axpby-as-primitive.md`).
- `axpbypcz(α, x, β, y, γ, z) ≡ axpby(α, x, β, axpby(γ/β, z, 1, y))` and (at L0) the
  `γ == 0` branch of real-real `AXPBYPCZ` collapses to `add(α, x, β, y, z)` — the in-source
  arity-collapse confirming `axpbypcz` ≻ `axpby` in the subsumption chain
  (`linear_combination.md` law 5; the L1 `axpbypcz` entry). `axpby` stays a sibling leaf.

**Lowering themes (forthcoming; D7 this cycle — plain-text forward-reference, files do
not yet exist)**: an `L2-L1/axpby-fusion` theme will narrate how the L2 leaf lowers into
the L1 leaf (identity-in-form; the only fusion content is the arity-2 single-aligned
`add(α, x, β, y, y)` pass — itself the arity-2 case of the fold's fusion note), and an
`L3-L2/axpby-body-identity` theme will narrate the L3 ↔ L2 identity rotation. Forward-
reference only — those chapters do not yet exist; do not link.

## Variant axes

The two variant axes are inherited unchanged from L1. Both are absorbed at construction
time (the element-type axis through overload selection at L0; the scalar-promotion
sub-axis through the real-scalar-on-complex-vector overload); neither appears in the L2
positional signature.

1. **element-type** (`real` | `complex`). The L0 source has separate template
   specialisations: real-real at `palace/linalg/vector.cpp:726-730` (delegating to MFEM's
   `add(α, x, β, y, y)`); complex-complex at `:732-737` (delegating to the member form);
   and the member declaration `ComplexVector::AXPBY` at `palace/linalg/vector.hpp:130-131`.
   At L1 / L2 / L3 these collapse to one operator parameterised by element type — the
   semantics are identical (the per-element kernel is `α·x[i] + β·y[i]` in the
   appropriate field).
2. **scalar-promotion** (sub-axis on the complex element-type). See
   [`concepts/scalar-promotion`](../concepts/scalar-promotion.md) — real `(α, β)` against
   complex `x, y` via the real-scalar-on-complex-vector overload at
   `palace/linalg/vector.cpp:739-743` (which delegates to the member form, implicitly
   promoting the real scalars to complex with zero imaginary part, all-or-none across the
   scalar pair). At L1 / L2 / L3 this is one operator with `(α, β)` typed through the
   `real ⊑ complex` scalar lattice.

**The output-aliasing axis is the FOLD's, not this leaf's.** The in-place forms
(`y ← α·x + β·y`, where the `y` term aliases the output buffer) are captured by the
output-aliasing variant axis of [`linear_combination`](./linear_combination.md)
(§"Variant axes" axis 1) — orthogonal to arity, applying uniformly to every arity ≥ 1.
At L2 this leaf is pure / out-of-place; aliasing is an L2>L1 lowering concern recorded by
the fold, not a leaf-specific axis.

No other variant axes — `axpby` is unconditionally pure, element-local, reduction-free,
and rank-local across all variants. Unlike `axpy` (which has the real-path `α == 1.0`
constant-folding specialisation at L0), `axpby` has **no** L0 constant-folding branches
on the values of `α` or `β` — the AXPBY surface uniformly delegates without inspecting
scalar values. The variant-axis count matches the L1 and L3 entries exactly (two axes;
element-type with scalar-promotion as sub-axis). No new axes introduced by the L2
rendering; no axes merged or split.

## Status

`firm` — signature is canonical (matches the three Palace L0 entry points exactly —
real-real `AXPBY`, complex-complex `AXPBY`, and the `ComplexVector::AXPBY` member; the
free-function template decl at `palace/linalg/vector.hpp:309-311`; identical to the L1 and
L3 forms), and the nine algebraic laws are standard fused-linear-combination facts
(bilinearity, distribution, scalar absorption, the chained-collapse law, the
specialization subsumptions). **Firm-on-positive-structure**: the `AXPBY` L0 surface is
small, fully present, and positively cited (`palace/linalg/vector.{hpp,cpp}` + the inlined
call sites in the fold-parent's evidence), and every law is a syntactic identity on that
closure — the absence of a dedicated `axpby` unit test does not gate firm (the
syntactic-identity-laws-on-positive-source escape, the `apply_linop` situation, not the
`eigsolve`-convergence-semantics situation; the fold-parent `linear_combination.md`
carries the matching empirical-match caveat for the BLAS-1 free-function family). This
dispatch is the **L2 floor backfill** (cycle-043 D4) under the foundation-first directive
`l2-floor-under-l3-leaf-cohort`, resolving the leaf-vs-fold design fork in favor of the
leaf-floor reading (b) (`book/src/L2/index.md` §Working-Notes,
`dot-l2-leaf-floor-vs-fold-only-design`; the c042 cross-cutter audit's recommendation):
the L2 form was previously referenced only as the arity-2 leaf of `linear_combination`
and inside `krylov-step` / `chebyshev-iteration` dependency lists; it now has its own L2
entry per **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology
invariants), so the firm L3 [`axpby`](../L3/axpby.md) (cycle-011) rests on a present
adjacent L2 parent. Mirrors the cycle-041 D3 [`scal`](./scal.md) sibling floor.

## Lowers to

L2 `axpby` lowers to L1 [`axpby`](../L1/axpby.md) via the **identity-in-form rotation on
the primitive's signature shape**. The two surfaces are value-thread-isomorphic
(whole-tensor in / whole-tensor out at both layers); the body is the same fused
two-scalar two-vector field operation. There is no multi-operation kernel fusion to
unfold beyond the arity-2 single-aligned `add(α, x, β, y, y)` pass (`vector.cpp:726-730`,
real-real path), which is itself the arity-2 case of the `linear_combination` fold's
fusion note — deferred to the fold-parent, not re-authored here. No firm
`L2-L1/axpby-fusion` theme file yet exists (the D7 dispatch this cycle authors the L2>L1
lowering themes for the BLAS-1 floor cohort); this entry captures the identity rotation
in-line, following the cycle-041 `scal` floor precedent for in-line identity-rotation
annotation. The L0 in-place mutation is reintroduced at the L1>L0 lowering
([`axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md), firm).

## Lifts from

L1 `axpby` lifts to this L2 entry via the **value-thread-isomorphic** identity rotation:
the L1 form's signature has no kernel fusion exposed beyond the single fused pass, no
destination buffer, no MPI collective — exactly the properties that make it L2-native by
construction as a base fused-linear-combination primitive. The L2 entry exists for
layer-coherence reasons — a reader navigating L2 must find `axpby` defined in L2
vocabulary as the base fused two-scalar two-vector primitive (and as the arity-2 member
of the `linear_combination` fold), not have to reach down to L1 to recover the
field-operation shape.

## Evidence

The L2 form is value-thread-isomorphic to the L1 form; all L0 evidence is sourced from
the firm L1 entry. Direct citations relevant to this L2 entry:

- `book/src/L1/axpby.md` (cycle-003 firm) — the L1 form this L2 entry value-thread-mirrors.
  Body shape, signature, semantics (element-local, reduction-free, rank-local), the nine
  algebraic laws, four non-laws, two variant axes (element-type + scalar-promotion
  sub-axis), and the L0 evidence chain.
- `book/src/L3/axpby.md` (cycle-011 firm) — the L3 consumer this floor entry supports;
  identical signature and laws, iteration-rotation framing (leaf primitive, no iteration
  view of its own — the iteration view applies to consuming compositions like
  `krylov-step`).
- `book/src/L2/linear_combination.md` (cycle-018 firm) — the fold-parent. `axpby` is its
  arity-2 specialization (`linear_combination.md` §Signature line 70:
  `axpby(α, x, β, y) = linear_combination [(α, x), (β, y)]`; §Algebraic-laws law 6
  specialization identities; §"Fusion note" carries the arity-2 single-aligned-pass fusion
  content; §"Variant axes" axis 1 carries the output-aliasing axis). Cited as fold-parent,
  NOT merged (fold-cohort boundary load-bearing).
- `book/src/L2/scal.md` (cycle-041 D3 firm) — the sibling BLAS-1 floor entry this entry's
  structure mirrors (same identity-in-form leaf-floor pattern, same fold-membership-cited-
  not-merged framing).
- `book/src/L2/index.md:17` — L2 vocabulary inventory naming `axpy` among the base
  primitive operations; §"Fold-cohort boundary" — the load-bearing do-NOT-merge note;
  §Working-Notes — the leaf-vs-fold design fork (`dot-l2-leaf-floor-vs-fold-only-design`,
  resolved (b)).
- `book/src/L1-L0/axpby-mutation-rotation.md` (firm, cycle-002) — the L1>L0 mutation
  rotation; the in-place receiver-mutating / output-arg idioms the L2 pure form abstracts
  over.
- `scaffolding/decisions/axpby-as-primitive.md` (cycle-003) — the fused-leaf decision;
  governs the L1/L2 leaf-vs-decompose choice (keep leaves firm, fuse don't decompose,
  don't merge into the fold).
- `book/src/concepts/scalar-promotion.md` — the typing rule for the scalar-promotion
  sub-axis (`real ⊑ complex` lattice; `vector.cpp:739-743` promotion site).

**L0 evidence (canonical anchors; self-verified via `citecheck --anchor` + on-disk read,
2026-06-01)**:

- `palace/linalg/vector.hpp:130-131` — `ComplexVector::AXPBY` member declaration with
  comment `In-place addition (*this) = alpha * x + beta * (*this).` (the receiver-mutating
  member form).
- `palace/linalg/vector.hpp:309-311` — free-function template
  `AXPBY(ScalarType alpha, const VecType &x, ScalarType beta, VecType &y)` declared with
  comment `Addition y = alpha * x + beta * y.` (the bounded-arity surface the fold
  unifies).
- `palace/linalg/vector.cpp:726-730` — real-real specialisation
  `AXPBY(double, Vector, double, Vector)`: delegates to MFEM's `add(alpha, x, beta, y, y)`
  (the 5-arg single aligned in-place linear-combine; the arity-2 fusion-note witness).
- `palace/linalg/vector.cpp:732-737` — complex-complex specialisation
  `AXPBY(std::complex<double>, ComplexVector, std::complex<double>, ComplexVector)`:
  delegates to the member form `y.AXPBY(alpha, x, beta)`.
- `palace/linalg/vector.cpp:739-743` — real-scalar-on-complex-vector specialisation
  `AXPBY(double, ComplexVector, double, ComplexVector)`: also delegates to the member form
  (implicit scalar promotion; the scalar-promotion sub-axis L0 anchor).

## L2 vs L1 distinction

- **L1**: mutation-lifted pure functional update. `r = axpby(α, x, β, y)`. Frames the
  operator as the pure-functional image of the L0 receiver-mutating / output-arg `AXPBY`
  idioms; emphasises the *mutation rotation* against the source (the destination-buffer
  drop and the real-imag-shape branch erasure).
- **L2**: base tensor-algebra field operation. `r = axpby(α, x, β, y) = α·x + β·y`.
  Frames the operator as a leaf primitive in the fusion-rotation layer's base vocabulary
  — and as the **arity-2 member of the `linear_combination` fold** (cited, not merged);
  emphasises that the only fusion note is the arity-2 single-aligned pass (deferred to the
  fold). The L2 form is **identical in body and signature to L1** — the framing differs
  (mutation rotation at L1 vs fusion rotation + fold-membership at L2), but no operational
  adjustment occurs.

The L2 ↔ L1 rotation is identity-in-form on the body and signature; the surface
adjustment is documentary. The methodology invariant **each layer is coherent within
itself** is what compels the L2 entry to exist as its own anchor — and the
foundation-first directive `l2-floor-under-l3-leaf-cohort` is what schedules it, so the
firm L3 [`axpby`](../L3/axpby.md) rests on a present adjacent L2 parent.
