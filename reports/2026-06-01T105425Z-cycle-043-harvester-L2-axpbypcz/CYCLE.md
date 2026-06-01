---
agent: harvester
invoked_at: 2026-06-01T105425Z
scope: L2 operator: axpbypcz
status: pending
inputs:
  - book/src/L1/axpbypcz.md (firm; source-of-truth for laws, variant axes, L0 evidence)
  - book/src/L3/axpbypcz.md (firm; the L3 leaf this floor supports — cycle-011 backfill)
  - book/src/L2/linear_combination.md (firm cycle-018; the fold-PARENT — axpbypcz is its arity-3 member)
  - book/src/L2/scal.md (firm cycle-041 D3; the sibling fold-member floor template — arity-1 member)
  - book/src/L2/index.md (L2 Part overview + dep-map + §"Fold-cohort boundary")
  - reference/palace/palace/linalg/vector.{hpp,cpp} (L0 anchors, on-disk-verified 2026-06-01)
  - dispatch: cycle-043 D5; plan item l2-floor-under-l3-leaf-cohort; fork resolved (keep leaf-floor (b))
integrated_at: 2026-06-01T140000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-043 batch integration (cohort-completing L2-floor build); D5 L2 axpbypcz floor (firm; arity-3 fold-member, vector.cpp:745-772); applied clean; see reports/2026-06-01T140000Z-integrator-finalize-cycle-43/CYCLE.md + cycle-043 STAGING row."
---

# CYCLE: Formalize axpbypcz at L2

## Summary

Builds the L2 fusion-rotation **floor** entry for `axpbypcz` (`z ← α·x + β·y + γ·z`,
the arity-3 three-term combination) under the `l2-floor-under-l3-leaf-cohort` plan item
(the cycle-043 continuation of the 2026-05-31 `l2-floor-under-l3-blas1-cohort`
foundation-first directive). The firm L3 [`axpbypcz`](../L3/axpbypcz.md) (cycle-011
backfill) currently rests on the L1 leaf directly with no adjacent same-named L2 parent;
this dispatch supplies that parent per the **Identity-lowerings still require both L
levels** methodology invariant. The entry is a **thin identity-in-form floor**:
value-thread-isomorphic to the firm L1 [`axpbypcz`](../L1/axpbypcz.md), all twelve
algebraic laws + four non-laws inherited unchanged, two variant axes inherited unchanged.

**Fork resolution applied:** `axpbypcz` is the **arity-3 fold-MEMBER of
[`linear_combination`](./linear_combination.md)** (`axpbypcz(α,x,β,y,γ,z) =
linear_combination [(α,x),(β,y),(γ,z)]`), cited as a member but **NOT merged** (the
fold-cohort boundary in `L2/index.md` is load-bearing). This is the structural twin of
the cycle-041 `scal` floor (the arity-1 member); the batch-12-resolved leaf-floor reading
(b) is the realization. Per dispatch, **all fusion content is deferred to the fold's
§"Fusion note"** (the single-aligned-pass `add(α,x,β,y,z)` de-fusion + the `γ==0`
arity-collapse), and the **output-aliasing variant axis is the FOLD's, not leaf-specific**
— this floor carries only the two element-type/scalar-promotion axes.

## Proposed changes

```edit:book/src/L2/axpbypcz.md
[create — full firm chapter body, below in "Operator content"]
```

```edit:book/src/L2/index.md
[add ONE dep-map row for axpbypcz, placed immediately after the `scal` row (the other
linear_combination fold-member floor). DO NOT touch the consolidated firm running-count
tally / §Working-Notes count prose — D2 owns the L2/index tally this cycle per
COUNT-OWNERSHIP. Row text below in "Dep-map row".]
```

```edit:book/src/SUMMARY.md
[add chapter entry under the L2 Part, immediately after `- [scal](./L2/scal.md)` (line 58):
`- [axpbypcz](./L2/axpbypcz.md)`]
```

## Operator content

The full firm chapter body written into `book/src/L2/axpbypcz.md`:

```new:book/src/L2/axpbypcz.md
---
layer: L2
operator: axpbypcz
firmness: firm
lowers_to:
  - book/src/L1/axpbypcz.md (identity-in-form; no firm `L2-L1/axpbypcz-fusion` theme yet — the single-aligned-pass fusion is the arity-3 case of the `linear_combination` fold's fusion note; in-line below at "Lowers to")
lifts_from:
  - book/src/L1/axpbypcz.md (value-thread-isomorphic; same signature shape; whole-tensor fused leaf primitive, no kernel fusion to unfold beyond the arity-3 single-aligned pass / γ==0 arity-collapse)
fold_parent:
  - book/src/L2/linear_combination.md (arity-3 member of the term-axis fold; cited, NOT merged — fold-cohort boundary is load-bearing)
variant_axes:
  - element-type (real / complex)
  - scalar-promotion (real-(α,β,γ)-against-complex-(x,y,z) via concepts/scalar-promotion)
---

# axpbypcz

Fused three-scalar three-vector update as a base tensor-algebra primitive at L2 — the
**fusion-rotation** rendering of `z = α·x + β·y + γ·z`. Consumes three scalars
`(α, β, γ)` and three tensors `(x, y, z)` (the third being the *prior* value when used as
a fused update); produces a fresh tensor of the same length axis whose every element is
`α·x[i] + β·y[i] + γ·z[i]`. `axpbypcz` is the **arity-3 member of the firm
[`linear_combination`](./linear_combination.md) fold** (`scal`/`axpy`/`axpby`/`axpbypcz`
are its arity-1/2/2/3 specializations); this entry is the standalone leaf, cited as a
fold-specialization of `linear_combination` but **not merged into it** (the fold-cohort
boundary in `book/src/L2/index.md` §"Fold-cohort boundary" is load-bearing). Companion to
L1 [`axpbypcz`](../L1/axpbypcz.md) (the mutation-lifted form of the same primitive) and L3
[`axpbypcz`](../L3/axpbypcz.md) (the iteration-rotation rendering); the rotation L1 ↔ L2
is identity-in-form because `axpbypcz` is a fused leaf field operation whose L0 form is
already the unfolded composition (the single-aligned `add(α,x,β,y,z)` pass), with no
multi-operation kernel fusion to unfold beyond the arity-3 single pass.

## Context

L2 is the fusion-rotation layer (`book/src/L2/index.md`): "Kernel fusion across multiple
algebraic operations is unfolded into composition… Batched specialized BLAS calls are
written as compositions of base primitives." `axpbypcz` at L2 is the base fused
three-term linear-combination primitive in that vocabulary — a single field operation
parameterised by the scalar triple `(α, β, γ)` and acting pointwise over the length axis,
the arity-3 extension of the `axpy`/`axpby` BLAS-1 family.

**`axpbypcz` is the arity-3 member of the `linear_combination` fold, cited but not
merged.** The firm [`linear_combination`](./linear_combination.md) entry (cycle-018) is
the arity-family unification of the BLAS-1 scalar-weighted-sum cohort: its four
fixed-arity leaves (`scal`/`axpy`/`axpby`/`axpbypcz`) are the arity-1/2/2/3
specializations of one variadic `foldl` over a list of `(scalar, tensor)` terms, with
`axpbypcz(α, x, β, y, γ, z) = linear_combination [(α, x), (β, y), (γ, z)]` recorded as the
arity-3 specialization identity (`linear_combination.md` §Signature line 71,
§Algebraic-laws law 6). The fold **does not replace the leaves** — the `axpby-as-primitive`
decision ([`scaffolding/decisions/axpby-as-primitive.md`](../../../scaffolding/decisions/axpby-as-primitive.md))
keeps each leaf firm (fuse, don't decompose; the decision record explicitly invites the
`axpbypcz` harvester to mirror the fused-primitive choice), and the L2 index §"Fold-cohort
boundary" makes the do-NOT-merge boundary load-bearing. So `axpbypcz` has its own L2 floor
entry as a leaf, and that leaf is **also** the recognized arity-3 specialization of the
fold — the two relationships coexist by design, exactly as for the sibling `scal` floor
(the arity-1 member, cycle-041 D3).

This is a thin **floor presence** entry. It exists so the firm L3
[`axpbypcz`](../L3/axpbypcz.md) (cycle-011) rests on a present adjacent L2 parent, per the
methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md
§Methodology invariants, cycle-009 codification): each layer is coherent within itself,
and a reader at L2 must find `axpbypcz` defined in L2 vocabulary without reaching down to
L1 or up to L3. The foundation-first directive `l2-floor-under-l3-blas1-cohort`
(2026-05-31) names exactly this gap: the L3 BLAS-1 cohort
(`axpy`/`axpby`/`axpbypcz`/`dot`/`nrm2`/`scal`) was backfilled to L3 in cycle-011 without
the corresponding L2 floor entries being present, so the L3 cohort rested on the L1 leaves
directly. The cycle-041 wave floored `dot`/`nrm2`/`scal`; this dispatch floors
`axpbypcz`, the arity-3 fold-member sibling of the floored `scal`.

The arity axis (`scal`/`axpy`/`axpby`/`axpbypcz`) is the axis the **fold** unifies — it is
NOT a variant axis of this leaf; the leaf is the arity-3 fixed point. The
**output-aliasing** variant axis (in-place `z ← α·x + β·y + γ·z` vs fresh-output) is the
**fold's** variant axis (`linear_combination.md` §Variant-axes point 1), orthogonal to
arity and carried at the fold level — the `γ=1` accumulate-into sites
(`nleps.cpp:343-344`, `romoperator.cpp:188-189`) are the fold's aliasing case. This leaf
floor is uniformly pure / out-of-place; the in-place idiom is an L2>L1 (and onward L1>L0)
lowering concern.

## Signature

    axpbypcz :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]
    axpbypcz α x β y γ z = α·x + β·y + γ·z

Shape contract (bunsen-style, named axes; positional values, no monadic effect, no
destination buffer):

- **`α`** — first scalar coefficient (`real` or `complex`, matching the tensor element
  type per the element-type variant axis; or promoted from `real` to `complex` against
  complex tensors per the scalar-promotion sub-axis — all-or-none across the scalar
  triple).
- **`x`** — `Tensor[N]` — first input tensor; read-only at L2.
- **`β`** — second scalar coefficient.
- **`y`** — `Tensor[N]` — second input tensor; read-only at L2.
- **`γ`** — third scalar coefficient.
- **`z`** — `Tensor[N]` — third input tensor (the *prior* value, when used as a fused
  update); read-only at L2 (the L2 form is pure / out-of-place; the L0 in-place mutation
  is reintroduced only at the L1>L0 lowering).
- **result** — `Tensor[N]` — same axis `N` as `x`, `y`, `z`. Every output element equals
  `α·x[i] + β·y[i] + γ·z[i]`.

`x`, `y`, and `z` must share the same length axis `N` and the same element type. The
scalars `α`, `β`, `γ` share each other's type and the vector element type. When the
vectors are complex, real scalars are promoted to complex (all-or-none across the scalar
triple) per the [`scalar-promotion`](../concepts/scalar-promotion.md) typing rule. The
argument ordering `(α, x, β, y, γ, z)` interleaves scalars and tensors, matching both the
L1 signature and the upstream L0 Palace API surface
(`palace/linalg/vector.cpp:745-772`).

The L2 signature is **identical to the L1 signature** modulo notation; the rotation is
identity-in-form. As the arity-3 fold specialization, the same operator is
`linear_combination [(α, x), (β, y), (γ, z)]` (per `linear_combination.md` line 71) — but
the standalone leaf form is the canonical L2 rendering, with the fold view recorded as a
derived identity (the fold-specialization identity below), not as a decomposition.

## Semantics

`axpbypcz` at L2 is a single base tensor-algebra field operation: a value-threaded
transformation `(α, x, β, y, γ, z) -> w` where `w[i] = α·x[i] + β·y[i] + γ·z[i]` for every
element index `i ∈ [0, N)`. The operator is **element-local** (every output element
depends on exactly one element from each of `x`, `y`, `z` and the shared scalar triple),
**reduction-free** (no cross-element communication in the length axis), and **rank-local**
(no MPI collective at any layer; ranks own disjoint slices of `N` and apply the fused
combination independently — contrast `dot` / `nrm2`, which reduce over `N` and do carry an
MPI collective).

It is **pure / out-of-place** at L2: it consumes `(α, β, γ)` and the prior values of
`x, y, z` and produces a fresh tensor; no destination buffer appears in the signature. The
L0 in-place output-arg / receiver-mutating idiom (`z ← α·x + β·y + γ·z`) is an L2>L1 (and
onward L1>L0) lowering concern, captured by the **output-aliasing variant axis of the
fold-parent** [`linear_combination`](./linear_combination.md) (§Variant-axes point 1) —
not by this leaf's L2 algebra.

**Fused leaf, with no kernel fusion to unfold at L2.** L2 is the layer where kernel fusion
across multiple algebraic operations is unfolded into composition. `axpbypcz` is a fused
**leaf** in that vocabulary — the fusion question (single aligned `add(α,x,β,y,z)` pass vs
multi-call split) is the fold's, not the leaf's: **all fusion content is deferred to the
fold's §"Fusion note"** (`linear_combination.md` line 243), which records the single
aligned strided pass — the MFEM `add(α, x, β, y, z)` 5-arg in-place linear-combine
(`palace/linalg/vector.cpp:749-751` for the `AXPBYPCZ` `γ==0` fast-path) — as the
transparent-performance-trick implementation of the arity-3 fold's seed-and-accumulate.
The L2 leaf carries no separate fusion note; it inherits the fold's. The arity-3 case is
the fold over the three-term list `[(α,x),(β,y),(γ,z)]` collapsed to the single pass.

Special algebraic cases — `γ = 0` (recovers `axpby`), `β = 0, γ = 0` (recovers `axpy` with
coefficient `α`), `β = 1, γ = 0` (recovers `axpy`), `α = 0` (drops `x`, gives
`axpby(β, y, γ, z)`), all-zero (zero tensor) — are not separate operators at L2. They are
algebraic identities recorded in the laws below, inherited from L1. The L0 source has
exactly one specialisation branch inside the `AXPBYPCZ` family: the real-real path's
`γ == 0` constant-fold to MFEM's `add(α, x, β, y, z)` at `palace/linalg/vector.cpp:749-751`
— which is the **exact algebraic content of the fold's zero-coefficient term-drop law**
(`linear_combination.md` law 5: dropping the `γ·z` term collapses the arity-3 fold to the
arity-2 `axpby`). This is a transparent performance trick at L1 that has already been
erased; it does not reintroduce a leaf-level variant axis at L2.

## Algebraic laws

The twelve laws that hold at L1 (per `book/src/L1/axpbypcz.md` §Algebraic laws) hold
unchanged at L2. The rotation L2 ↔ L1 is identity-in-form on the operator's body and
signature, so the algebraic properties of the fused three-term linear combination
transport without modification. Absences are deliberate and inherited.

1. **Subsumption of `axpby`**: `axpbypcz(α, x, β, y, 0, z) = axpby(α, x, β, y)` for any
   `z`. The load-bearing identity from the L0 `γ == 0` branch
   (`palace/linalg/vector.cpp:749-751`); the arity-3 fold's zero-coefficient term-drop
   (`linear_combination.md` law 5).
2. **Subsumption of `axpy`**: `axpbypcz(α, x, 1, y, 0, z) = axpy(α, x, y)` for any `z`.
   Composition of law 1 (γ=0 → axpby) and axpby's β=1 → axpy law.
3. **Identity in `α`**: `axpbypcz(0, x, β, y, γ, z) = β·y + γ·z = axpby(β, y, γ, z)` for
   any `x`.
4. **Identity in `β`**: `axpbypcz(α, x, 0, y, γ, z) = α·x + γ·z = axpby(α, x, γ, z)` for
   any `y`.
5. **Identity in `γ`**: see law 1 (the γ=0 subsumption — recovers `axpby(α, x, β, y)`).
6. **All-zero identity**: `axpbypcz(0, x, 0, y, 0, z) = 0` (the zero tensor of axis `N`)
   for any `x`, `y`, `z`.
7. **Trilinearity in the scalar triple `(α, β, γ)`**: `axpbypcz(α, x, β, y, γ, z)` is
   linear separately in each of `α`, `β`, `γ` (with the others and all tensors held
   fixed). The arity-3 case of the fold's multilinearity (`linear_combination.md` law 3).
8. **Right distribution over tensor addition in `x`**:
   `axpbypcz(α, x₁ + x₂, β, y, γ, z) = axpbypcz(α, x₁, β, y, γ, z) + α·x₂`.
9. **Right distribution over tensor addition in `y`**:
   `axpbypcz(α, x, β, y₁ + y₂, γ, z) = axpbypcz(α, x, β, y₁, γ, z) + β·y₂`.
10. **Right distribution over tensor addition in `z`**:
    `axpbypcz(α, x, β, y, γ, z₁ + z₂) = axpbypcz(α, x, β, y, γ, z₁) + γ·z₂`.
11. **Scalar absorption**: `axpbypcz(α·κ, x, β, y, γ, z) = axpbypcz(α, κ·x, β, y, γ, z)`
    and symmetrically for the `β`/`y` and `γ`/`z` pairs — each scalar absorbs into its
    paired tensor. The arity-3 case of the fold's coefficient-scaling law
    (`linear_combination.md` law 4).
12. **Chained-`axpbypcz` collapse on shared `(x, y)`**:
    `axpbypcz(α₁, x, β₁, y, γ₁, axpbypcz(α₂, x, β₂, y, γ₂, z)) = axpbypcz(α₁ + γ₁·α₂, x, β₁ + γ₁·β₂, y, γ₁·γ₂, z)`.
    Two successive updates against the same `(x, y)` pair collapse to one. Generalises the
    axpby chained-collapse law; underwrites L2 fusion of consecutive coefficient-update
    lines sharing both an `x` and a `y` (GMRES/BiCGStab two-vector coefficient updates).

**Fold-specialization identity (the link to `linear_combination`, NOT a merge):**

- `axpbypcz(α, x, β, y, γ, z) = linear_combination [(α, x), (β, y), (γ, z)]` — `axpbypcz`
  is the arity-3 specialization of the firm
  [`linear_combination`](./linear_combination.md) fold (`linear_combination.md` §Signature
  line 71, §Algebraic-laws law 6). The fold's concatenation-homomorphism
  (`linear_combination.md` law 2) makes the four arities one fold: the arity-3 term list
  `[(α,x),(β,y),(γ,z)]` is the concatenation of an `axpby` 2-term list and a `scal` 1-term
  list, so `linear_combination [(α,x),(β,y),(γ,z)] = axpby(α,x,β,y) + scal(γ,z)`. The leaf
  laws above are the arity-3 shadow of the fold's laws (laws 7/11 here = the fold's
  multilinearity / coefficient-scaling at the 3-term list; laws 8–10 here = the fold's
  per-term distributivity; law 1 here = the fold's zero-coefficient term-drop at the
  third term). The leaf stays firm and standalone; the fold view is a derived identity,
  not a decomposition (do-NOT-merge per the fold-cohort boundary).

Laws that explicitly **do not** hold (inherited from L1):

- **Commutativity in the tensor arguments**: `axpbypcz(α, x, β, y, γ, z) ≠
  axpbypcz(β, y, α, x, γ, z)` in general unless `α = β` — the operator is symmetric in the
  inputs only because the linear combination is commutative mathematically; the signature
  distinguishes argument slots by which scalar pairs with which tensor. Three-way
  permutation of the `(α,x),(β,y),(γ,z)` pair-triples preserves the value algebraically,
  but the signature has fixed argument positions. (At the fold level this is the
  exact-arithmetic permutation law `linear_combination.md` law 7, with the fixed-position
  signature being the leaf's bounded-arity shadow.)
- **Associativity**: `axpbypcz` is six-ary (three scalar-tensor pairs); "associativity" is
  not well-typed.
- **Floating-point associativity of the summation**: `α·x + β·y + γ·z` computed in
  IEEE-754 may differ from any reordering at the bit level when the partial-sum magnitudes
  differ enough to lose precision in one ordering. Palace's L0 form pins the ordering in
  the `γ == 0` fast-path (MFEM's `add(α, x, β, y, z)` kernel,
  `palace/linalg/vector.cpp:749-751`) but the `γ ≠ 0` slow-path uses a two-call split
  (`AXPBY(α, x, γ, z); z.Add(β, y)`, `:755-756`) which computes the sum in a *different*
  order than the fused form would. The L2 algebra is order-agnostic for value, but
  bit-identical reproduction of L0 output requires matching the L0 branch's evaluation
  order, and the two L0 branches do not match each other. This is the leaf-level shadow of
  the fold's paired permutation non-law (`linear_combination.md` §Algebraic-laws,
  "Permutation-invariance under IEEE-754 (paired non-law)") — a **load-bearing numerical
  concern**, recorded, not erased.
- **Fusion identity with three separate `scal`+`add` passes**: `axpbypcz(α, x, β, y, γ, z)
  ≠ scal(α, x) + scal(β, y) + scal(γ, z)` in general at the bit level (the three-pass form
  rounds three times; the fused form rounds once or twice depending on the L0 branch),
  even though the values agree mathematically. The arity-3 case of the fold's "bit-level
  fusion identity against the multi-pass form" non-law (`linear_combination.md`
  §Algebraic-laws). The L0 form is fused for performance; the L2 algebra preserves the
  fused statement, with the fusion choice load-bearing for bit-reproduction and
  transparent for value.

## Dependencies

**Same-layer (L2)**: none as a constituent. `axpbypcz` is a fused leaf primitive at L2
just as it is at L1 — the fused three-term linear combination does not decompose into
other L2 primitives. The body is a single fused field operation; the sub-operations (three
scalar multiplications and two element-wise additions) are below the L2 layer's
resolution. (Decomposing it into `axpby` ▷ `axpy` or chained `axpby` calls is precisely the
choice the `axpby-as-primitive` decision declines — fuse, don't decompose.)

**Fold-parent (cited, NOT merged)**:

- [`linear_combination`](./linear_combination.md) (firm cycle-018) — the term-axis
  arity-family fold of which `axpbypcz` is the **arity-3 member**
  (`axpbypcz(α, x, β, y, γ, z) = linear_combination [(α, x), (β, y), (γ, z)]`). `axpbypcz`
  stays a firm standalone L2 leaf; `linear_combination` is the form the four leaves
  (`scal`/`axpy`/`axpby`/`axpbypcz`) fuse *up* into, not a replacement. The do-NOT-merge
  boundary (`book/src/L2/index.md` §"Fold-cohort boundary") is load-bearing — merging the
  leaf into the fold would erase the one-to-one leaf↔L0-symbol shape that the L1>L0
  mutation rotation relies on. **Fusion content (the single-aligned `add(α,x,β,y,z)` pass,
  the `γ==0` arity-collapse) is deferred to the fold's §"Fusion note"
  (`linear_combination.md` line 243); the output-aliasing in-place/out-of-place variant
  axis is the fold's (`linear_combination.md` §Variant-axes point 1, the `γ=1`
  accumulate-into sites), not this leaf's.**

**Cross-cutting concepts**:

- [`scalar-promotion`](../concepts/scalar-promotion.md) — the implicit-coercion typing
  rule for real `(α, β, γ)` against complex `(x, y, z)`. Internal promotion at L0 via the
  real-scalar-on-complex-vector specialisation `palace/linalg/vector.cpp:767-772`
  (delegating to the member form); collapsed at L1 / L2 / L3 into a single operator
  parameterised by the `real ⊑ complex` scalar lattice (all-or-none across the scalar
  triple).

**Sibling subsumption (not dependency)**:

- `axpby(α, x, β, y) ≡ axpbypcz(α, x, β, y, 0, z)` and
  `axpy(α, x, y) ≡ axpbypcz(α, x, 1, y, 0, z)` (for any `z` — the result is independent of
  `z` when `γ = 0`). All three (`axpy`, `axpby`, `axpbypcz`) stay in the L2 dep-map as
  sibling leaves; the subsumption chain `axpy ≺ axpby ≺ axpbypcz` is the bounded-arity
  shadow of the fold's concatenation law (`linear_combination.md` law 2), algebraic, not
  structural.
- `scal(γ, z) = axpbypcz(0, x, 0, y, γ, z)` for any `x`, `y` — the two-zero reduction. The
  firm L2 [`scal`](./scal.md) floor (cycle-041 D3) is the arity-1 sibling fold-member;
  this entry is its arity-3 counterpart.

**Lowering themes (forthcoming; D8 this cycle — plain-text forward-reference, files do not
yet exist)**: an `L2-L1/axpbypcz-fusion` (or sibling-named) theme will narrate how the L2
leaf lowers into the L1 leaf (identity-in-form; the only fusion content is the arity-3
single-aligned `add(α,x,β,y,z)` pass / `γ==0` arity-collapse, deferred to the fold's
fusion note), and the L3>L2 identity rotation for `axpbypcz` is the iteration-rotation
re-erasure narrated by the companion `axpbypcz-body-identity` theme. Forward-reference
only — those chapters do not yet exist; do not link.

## Variant axes

The two variant axes are inherited unchanged from L1. Both are absorbed at construction
time (the element-type axis through overload / template selection at L0; the
scalar-promotion sub-axis through the real-scalar-on-complex-vector specialisation);
neither appears in the L2 positional signature.

1. **element-type** (`real` | `complex`). The L0 source has separate template
   specialisations (real-real at `palace/linalg/vector.cpp:745-758`; complex-complex at
   `:760-765`; real-scalar-on-complex-vector at `:767-772`; member form on `ComplexVector`
   at `vector.hpp:133-136`). At L1 / L2 / L3 these collapse to one operator parameterised
   by element type — the per-element kernel is `α·x[i] + β·y[i] + γ·z[i]` in the
   appropriate field.
2. **scalar-promotion** (sub-axis on the complex element-type). See
   [`concepts/scalar-promotion`](../concepts/scalar-promotion.md) — real `(α, β, γ)`
   against complex `(x, y, z)` via the specialisation at `vector.cpp:767-772`, promoted to
   complex with zero imaginary part (all-or-none across the scalar triple). At L1 / L2 / L3
   this is one operator with the scalar triple typed through the `real ⊑ complex` lattice.

**NOT variant axes of this leaf:**

- **arity** (`scal`/`axpy`/`axpby`/`axpbypcz`) — this is the axis the **fold-parent**
  [`linear_combination`](./linear_combination.md) unifies; `axpbypcz` is the fixed arity-3
  point, not a remaining variant.
- **output-aliasing** (in-place vs out-of-place) — this is the **fold's** variant axis
  (`linear_combination.md` §Variant-axes point 1), orthogonal to arity; the `γ=1`
  accumulate-into sites (`palace/linalg/nleps.cpp:343-344`,
  `palace/models/romoperator.cpp:188-189`) are the fold's aliasing case. This leaf floor
  is uniformly pure / out-of-place; the in-place idiom is an L2>L1 (onward L1>L0) lowering
  concern.

**Internal control-flow axis at L0 (not an L2 variant axis)**: the real-real
specialisation's `γ == 0` branch (`vector.cpp:749-758`) is a transparent performance
specialisation — algebraically equivalent at L1 (the fold's zero-coefficient term-drop) —
and not visible at L2. Inherited from L1; the complex-complex and real-on-complex
specialisations do not have this branch (they uniformly delegate to the member form).

The variant-axis count matches the L1 and L3 entries exactly (two axes; element-type with
scalar-promotion as sub-axis). No new axes introduced by the L2 rendering; no axes merged
or split.

## Status

`firm` — signature is canonical (matches the three Palace `AXPBYPCZ` L0 entry points
exactly; identical to the L1 and L3 forms), and the twelve algebraic laws are standard
linear-combination facts extended from the `axpby` laws (axioms of a module over the
scalar field plus the trilinearity / chained-collapse rules). **Firm-on-positive-structure**:
the `axpbypcz` L0 surface is small, fully present, and positively cited
(`palace/linalg/vector.{hpp,cpp}` — three template specialisations + member decl), and
every law is a syntactic identity on that closure — the absence of a dedicated `AXPBYPCZ`
unit test does not gate firm (the syntactic-identity-laws-on-positive-source escape, the
`apply_linop` situation, not the `eigsolve`-convergence-semantics situation; the same
firm-without-dedicated-test bar the fold-parent `linear_combination` rests on — see its
§Status empirical-match caveat). This dispatch is the **L2 floor backfill** (cycle-043 D5)
under the `l2-floor-under-l3-leaf-cohort` plan item (continuation of the
`l2-floor-under-l3-blas1-cohort` foundation-first directive): the L2 form was previously
referenced only as the arity-3 leaf of `linear_combination` and inside `krylov-step` /
`chebyshev-iteration` dependency lists; it now has its own L2 entry per **Identity-lowerings
still require both L levels**, the arity-3 sibling of the cycle-041 `scal` floor. The
leaf-floor reading (b) — a standalone same-named leaf cited as fold-member, not merged — is
the batch-12-resolved realization (the `dot-l2-leaf-floor-vs-fold-only-design` fork
resolved to keep leaf-floor (b)).

## Lowers to

L2 `axpbypcz` lowers to L1 [`axpbypcz`](../L1/axpbypcz.md) via an **identity-in-form**
rotation: the signature
`Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` is
textually identical at both layers; the body is the same fused three-term linear-combination
field operation. There is no kernel fusion to unfold at the leaf level beyond the arity-3
single-aligned pass (deferred to the fold's §"Fusion note",
`linear_combination.md` line 243). No firm `L2-L1/axpbypcz-fusion` theme file yet exists
(the D8 dispatch this cycle authors the L2>L1 lowering themes for the floor cohort); this
entry captures the identity rotation in-line, following the L3/L2 `scal` floor precedent
for in-line identity-rotation annotation. The L0 in-place mutation is reintroduced at the
L1>L0 lowering ([`axpbypcz-mutation-rotation`](../L1-L0/axpbypcz-mutation-rotation.md)).

## Lifts from

L1 `axpbypcz` lifts to this L2 entry via the **value-thread-isomorphic** identity rotation:
the L1 form's signature has no kernel fusion exposed at the leaf level, no destination
buffer, no MPI collective — these are exactly the properties that make it L2-native by
construction as a base fused tensor-algebra primitive (and as the arity-3 member of the
`linear_combination` fold). The L2 entry exists for layer-coherence reasons — a reader
navigating L2 must find `axpbypcz` defined in L2 vocabulary as the base fused three-term
linear-combination primitive, not have to reach down to L1 to recover the field-operation
shape.

## Evidence

The L2 form is value-thread-isomorphic to the L1 form; all L0 evidence is sourced from the
firm L1 entry. Direct citations relevant to this L2 entry:

- `book/src/L1/axpbypcz.md` (firm) — the L1 form this L2 entry value-thread-mirrors. Body
  shape, signature, semantics (element-local, reduction-free, rank-local), the twelve
  algebraic laws, four non-laws, two variant axes (element-type + scalar-promotion
  sub-axis), and L0 evidence chain.
- `book/src/L3/axpbypcz.md` (cycle-011 firm) — the L3 consumer this floor entry supports;
  identical signature and laws, iteration-rotation framing.
- `book/src/L2/linear_combination.md` (cycle-018 firm) — the **fold-parent**. `axpbypcz`
  is its arity-3 specialization (`linear_combination.md` §Signature line 71:
  `axpbypcz(α, x, β, y, γ, z) = linear_combination [(α, x), (β, y), (γ, z)]`;
  §Algebraic-laws law 6 specialization identities). Cited as fold-parent, NOT merged
  (fold-cohort boundary load-bearing). Fusion content deferred to its §"Fusion note"
  (line 243); the output-aliasing variant axis is its §Variant-axes point 1 (line 220).
- `book/src/L2/scal.md` (cycle-041 D3 firm) — the sibling fold-member floor (arity-1
  member of `linear_combination`); the structural template this arity-3 floor follows.
- `book/src/L2/index.md` — L2 Part overview; §"Fold-cohort boundary" — the load-bearing
  do-NOT-merge note; the BLAS-1 cohort vocabulary inventory (`:17`) naming the
  `axpy`/`scal` family among the base primitive operations.
- `scaffolding/decisions/axpby-as-primitive.md` §"Knock-on effects" — the fused-leaf
  decision; governs the L1/L2 leaf-vs-decompose choice (keep leaves firm, fuse up into the
  fold, don't merge), with the explicit invitation for the `axpbypcz` harvester to mirror
  the fused-primitive choice.
- `book/src/concepts/scalar-promotion.md` — the typing rule for the scalar-promotion
  sub-axis (real `(α,β,γ)` against complex vectors).

**L0 evidence (canonical anchors, on-disk-verified 2026-06-01)**:

- `palace/linalg/vector.hpp:133-136` — `ComplexVector::AXPBYPCZ` member decl with comment
  `In-place addition (*this) = alpha * x + beta * y + gamma * (*this).`
- `palace/linalg/vector.hpp:313-316` — free-function template `AXPBYPCZ(ScalarType alpha,
  const VecType &x, ScalarType beta, const VecType &y, ScalarType gamma, VecType &z)`
  declared with comment `Addition z = alpha * x + beta * y + gamma * z.`
- `palace/linalg/vector.cpp:745-758` — `AXPBYPCZ(double, Vector, double, Vector, double,
  Vector)` real-real specialisation with the `γ == 0` branch: fast-path delegates to
  `add(alpha, x, beta, y, z)` (MFEM's 5-arg out-of-place form, `:749-751`); slow-path
  splits into `AXPBY(alpha, x, gamma, z); z.Add(beta, y)` (`:755-756`).
- `palace/linalg/vector.cpp:760-765` — `AXPBYPCZ(std::complex<double>, ComplexVector, …)`
  complex-complex specialisation: delegates to member `z.AXPBYPCZ(alpha, x, beta, y, gamma)`.
- `palace/linalg/vector.cpp:767-772` — `AXPBYPCZ(double, ComplexVector, …)`
  real-scalar-on-complex-vector specialisation: also delegates to the member form
  (implicit scalar promotion).

## L2 vs L1 distinction

- **L1**: mutation-lifted pure functional update. `z_new = axpbypcz(α, x, β, y, γ, z_old)`.
  Frames the operator as the pure-functional image of the L0 receiver-mutating member
  method / output-arg free-function idiom; emphasises the *mutation rotation* against the
  source (the destination-buffer drop and the `γ == 0` control-flow / fusion-branch
  erasure).
- **L2**: base fused tensor-algebra field operation. `w = axpbypcz(α, x, β, y, γ, z)`.
  Frames the operator as a fused leaf primitive in the fusion-rotation layer's base
  vocabulary — and as the **arity-3 member of the `linear_combination` fold** (cited, not
  merged); emphasises that the fusion question (single aligned pass vs split) is the
  fold's, deferred to its §"Fusion note", and that the output-aliasing axis is the fold's.
  The L2 form is **identical in body and signature to L1** — the framing differs (mutation
  rotation at L1 vs fusion rotation + fold-membership at L2), but no operational adjustment
  occurs.

The L2 ↔ L1 rotation is identity-in-form on the body and signature; the surface adjustment
is documentary. The methodology invariant **each layer is coherent within itself** is what
compels the L2 entry to exist as its own anchor — and the `l2-floor-under-l3-leaf-cohort`
plan item is what schedules it, so the firm L3 [`axpbypcz`](../L3/axpbypcz.md) rests on a
present adjacent L2 parent.
```

## Dep-map row

The single row to insert into `book/src/L2/index.md`'s operator dep-map table,
immediately after the `scal` row (its arity-1 fold-member sibling). **D2 owns the
consolidated firm running-count tally / §Working-Notes count prose this cycle — this
report appends ONLY the row below.**

```text
| [`axpbypcz`](./axpbypcz.md) | `axpbypcz :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` (`α,x,β,y,γ,z → α·x + β·y + γ·z`; fused three-scalar three-vector combination) | **Base fused three-term linear-combination leaf; arity-3 member of [`linear_combination`](./linear_combination.md) (cited, NOT merged — fold-cohort boundary load-bearing).** Leaf primitive (no L2 constituents; the three scalar-multiplies + two adds are below L2 resolution; no kernel fusion to unfold at the leaf — the single-aligned `add(α,x,β,y,z)` pass / `γ==0` arity-collapse is deferred to the fold's §"Fusion note"). Fold-parent: `linear_combination` (`axpbypcz(α,x,β,y,γ,z) = linear_combination [(α,x),(β,y),(γ,z)]`). The **output-aliasing** in-place/out-of-place variant is the fold's axis, NOT leaf-specific. Concepts: [`scalar-promotion`](../concepts/scalar-promotion.md) (element-type axis + real⊑complex sub-axis, all-or-none across the scalar triple). Sibling-subsumed: `axpby` (γ=0), `axpy` (β=1,γ=0), `scal` (α=0,β=0). L1 anchor via identity-in-form rotation (whole-tensor in/out at both layers; no leaf kernel fusion to unfold beyond the arity-3 single pass). | `firm` (harvested cycle-043 D5; L2 floor backfill under plan item `l2-floor-under-l3-leaf-cohort`; identity-lowering per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels** — floors the firm L3 [`axpbypcz`](../L3/axpbypcz.md), cycle-011; the arity-3 fold-member sibling of the cycle-041 [`scal`](./scal.md) floor; leaf-floor reading (b) per the batch-12-resolved `dot-l2-leaf-floor-vs-fold-only-design` fork; firm-on-positive-structure — syntactic-identity laws on the three fully-present `AXPBYPCZ` template specialisations `vector.cpp:745-772`) |
```

## SUMMARY.md entry

Insert under the L2 Part, immediately after `- [scal](./L2/scal.md)` (current line 58):

```text
- [axpbypcz](./L2/axpbypcz.md)
```

## Supporting evidence

- **Source-of-truth files** (read this invocation): firm L1 `book/src/L1/axpbypcz.md`
  (twelve laws, four non-laws, two variant axes, L0 evidence chain); firm L3
  `book/src/L3/axpbypcz.md` (cycle-011 identity-in-form backfill); firm L2 fold-parent
  `book/src/L2/linear_combination.md` (cycle-018; §Signature line 71 arity-3 specialization
  identity, §Algebraic-laws law 6, §Fusion-note line 243, §Variant-axes output-aliasing
  point 1 line 220); firm L2 sibling floor `book/src/L2/scal.md` (cycle-041 D3 — the
  structural template).
- **L0 anchors on-disk-verified 2026-06-01** (read directly from
  `reference/palace/palace/linalg/vector.{hpp,cpp}`; note the citation form
  `palace/linalg/vector.*` is the corpus-canonical relative path, the on-disk file is
  nested at `reference/palace/palace/linalg/`):
  - `vector.cpp:745-758` — real-real `AXPBYPCZ` with `γ==0` branch (fast-path `add` at 751;
    slow-path split at 755-756). ✓ verified on-disk.
  - `vector.cpp:760-765` — complex-complex specialisation (delegates to member). ✓
  - `vector.cpp:767-772` — real-on-complex promotion specialisation (delegates to member). ✓
  - `vector.hpp:133-136` — `ComplexVector::AXPBYPCZ` member decl, `(*this) = α·x + β·y +
    γ·(*this)` comment. ✓
  - `vector.hpp:313-316` — free-function template decl, `z = α·x + β·y + γ·z` comment. ✓
- **Fork resolution**: dispatch states the `dot-l2-leaf-floor-vs-fold-only-design` fork is
  resolved to keep leaf-floor (b); `axpbypcz` IS a fold-member. This entry realizes (b)
  exactly as the cycle-041 `scal`/`dot` floors do (standalone same-named leaf, cited as
  fold-member, NOT merged).
- **Count-ownership**: per dispatch, this report appends ONLY its own dep-map row + body +
  SUMMARY entry. The L2/index consolidated firm running-count tally + §Working-Notes count
  prose are D2's this cycle — NOT touched here.

## Open questions / caveats

- **`axpbypcz` L3 staleness → cycle-044 sweep (NOT here).** Per dispatch, the L3
  `axpbypcz` entry may carry stale cross-references / framing predating this L2 floor (it
  currently says the rotation "does not pass through L2 because `axpbypcz` is an L1 leaf,
  not an L2 composition" — `L3/axpbypcz.md:106,125`); now that an adjacent same-named L2
  floor exists, that prose wants a light refresh (the L3>L2 hop is identity-in-form to this
  floor, then this floor is identity-in-form to L1). Deferred to a cycle-044 sweep, not
  authored here. (This floor is correct as written — it lifts from / lowers to L1
  directly, identity-in-form, exactly as the `scal` floor does.)
- **L2>L1 + L3>L2 themes are D8's (this cycle).** This floor forward-references
  `L2-L1/axpbypcz-fusion` (or sibling-named) and the L3>L2 `axpbypcz-body-identity` theme
  as plain text only — those files do not yet exist; do not link. Slug naming for the
  L2>L1 edge should follow the cycle-042 `-leaf-identity` de-facto convention (the
  cycle-041 `-fold-specialization` outliers await meta-phase normalization per
  `L2/index.md:108`); flagged for D8 / the integrator.
- **Layer-intro refresh (not in scope).** The L2 `index.md` §Working-Notes cycle-041/042
  cohort-growth prose names the floored leaves; once D2 updates the count, a one-line
  mention of the `axpbypcz` arity-3 fold-member floor (completing the `scal`/`axpbypcz`
  fold-member-floor pair) would be apt — layer-intro-author's domain, noted not authored.
- **Empirical-match caveat inherited, does NOT reduce status.** As with the fold-parent
  `linear_combination` and the `scal` floor, there is no dedicated `AXPBYPCZ` unit test;
  firm rests on the syntactic-identity-laws-on-positive-source escape (three fully-present
  template specialisations). Recorded in §Status, consistent with the sibling floors.
