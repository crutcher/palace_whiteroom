# axpbypcz-leaf-identity

The L2>L1 lowering theme for the fused arity-3 three-term linear-combination leaf `axpbypcz`.
The rewrite is **identity-in-form on the leaf**: the L2 [`axpbypcz`](../L2/axpbypcz.md) leaf-floor
lowers to the firm L1 [`axpbypcz`](../L1/axpbypcz.md) primitive with the same six-argument
signature, the same fused three-term semantics, and the same twelve algebraic laws + four
non-laws — value-thread-isomorphic on the primitive. The L2 layer's fusion-rotation work (the
arity-3 single-aligned `add(α,x,β,y,z)` pass and the `γ==0` arity-collapse) is **not on this
leaf**; it is carried by the fold-parent
[`linear-combination-fold-specialization`](./linear-combination-fold-specialization.md) for the
whole arity family (`scal`/`axpy`/`axpby`/`axpbypcz`). This theme records the identity edge and
defers the fusion treatment to the fold-parent — the arity-3 analogue of
[`scal-leaf-identity`](./scal-leaf-identity.md) (the arity-1 row) and the sibling
shape of [`dot-leaf-identity`](./dot-leaf-identity.md).

## Slug

`axpbypcz-leaf-identity`

## Context

`axpbypcz` at L2 is the **leaf-floor** entry ([`L2/axpbypcz`](../L2/axpbypcz.md), harvested
cycle-043 wave-1 D5): the arity-3 member of the L2 fold-parent
[`linear_combination`](../L2/linear_combination.md), rendered as its own same-named L2 chapter so
the firm L3 [`axpbypcz`](../L3/axpbypcz.md) leaf rests on an adjacent same-named L2 parent (per
CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels**) rather than
skipping a layer to L1. This theme is the L2>L1 edge of that floor.

The edge is the **identity-in-form** case: the L2 `axpbypcz` leaf and the L1 `axpbypcz` leaf are
value-thread-isomorphic on the primitive. This is the L2>L1 analogue of the L3>L2
[`axpbypcz-body-identity`](../L3-L2/axpbypcz-body-identity.md) theme (the other thin edge of the
same leaf, co-authored this cycle), and the arity-3 sibling of the arity-1
[`scal-leaf-identity`](./scal-leaf-identity.md). It shares the
[`dot-leaf-identity`](./dot-leaf-identity.md) shape (identity-in-form on a single leaf with all
fusion deferred to a fold-parent), differing only in which fold-parent and which fusion content
defers.

**Why this edge is identity while its fold-parent sibling carries the fusion.** The L2 fusion
rotation for the linear-combination cohort — selecting the arity-3 single aligned strided pass
(MFEM's 5-arg `add(α, x, β, y, z)` at `palace/linalg/vector.cpp:749-751`) vs the two-call split
`AXPBY(α, x, γ, z); z.Add(β, y)` (`:755-756`), the `γ==0` arity-collapse to `axpby`, and the
pinned summation order — is **the fold-parent's job**. The firm
[`linear-combination-fold-specialization`](./linear-combination-fold-specialization.md) theme
carries all of it for the whole arity family (`scal`/`axpy`/`axpby`/`axpbypcz`) via its
arity-dispatch fusion-selection + pinned-summation-order content. The `axpbypcz` leaf is the
arity-3 member of that fold; restricting the fold-parent's fusion content to the arity-3 term list
`[(α,x),(β,y),(γ,z)]` leaves **no fusion structure unique to `axpbypcz`** beyond the fold's
arity-3 row. So the `axpbypcz` leaf's own L2>L1 edge — the rotation between the L2 `axpbypcz`
chapter and the L1 `axpbypcz` chapter — is the identity, with the fusion treatment deferred to the
fold-parent theme.

## L2 form (LHS)

The L2 form is the `axpbypcz` leaf-floor ([`L2/axpbypcz`](../L2/axpbypcz.md) §Signature, harvested
cycle-043 wave-1 D5) — the mutation-free fused three-term combination:

    axpbypcz :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]
    axpbypcz α x β y γ z = α·x + β·y + γ·z

with the per-element kernel `result[i] = α·x[i] + β·y[i] + γ·z[i]` inherited unchanged from the L1
leaf and the fold-parent. The L2 form is **pure / out-of-place** (no destination buffer; the
result is a fresh `Tensor[N]`; the `z` argument is the *prior* value when used as a fused update).
The L0 in-place receiver-mutating / output-arg idiom and the `γ==0` runtime control-flow branch are
NOT in the L2 signature — they reappear only at the L1>L0 lowering
([`axpbypcz-mutation-rotation`](../L1-L0/axpbypcz-mutation-rotation.md)).

`axpbypcz` is the **arity-3 member of the [`linear_combination`](../L2/linear_combination.md)
fold** (`axpbypcz(α, x, β, y, γ, z) = linear_combination [(α, x), (β, y), (γ, z)]`), cited as a
fold-specialization but NOT merged (the fold-cohort boundary in `book/src/L2/index.md` is
load-bearing). The **output-aliasing** in-place/out-of-place variant is the **fold's** axis
([`linear_combination`](../L2/linear_combination.md) §Variant axes, line 214), not leaf-specific;
this floor is uniformly pure.

## L1 form (RHS)

The L1 form is the firm `axpbypcz` leaf primitive ([`L1/axpbypcz`](../L1/axpbypcz.md) §Signature,
firm cycle-003) — identical in signature, semantics, and laws:

    axpbypcz :: (α: Scalar, x: Tensor[N], β: Scalar, y: Tensor[N], γ: Scalar, z: Tensor[N]) -> Tensor[N]
    axpbypcz(α, x, β, y, γ, z) = α·x + β·y + γ·z       -- same per-element kernel

The L1 leaf is the **mutation-rotation** rendering: it already erases the L0 destination buffer
(the in-place `z` overwrite drops to the L1>L0 lowering), erases the L0 `γ==0` control-flow branch
(a transparent performance specialisation, algebraically the law-1 subsumption of `axpby`), and
preserves the fused statement (the fusion has algebraic meaning — `axpbypcz(α,x,β,y,γ,z) = α·x +
β·y + γ·z` is a primitive statement of the linear combination, not a derived shorthand). The L1
entry is authoritative on every Palace-surface fact; the L2 form does not duplicate them.

## The rewrite (L2 → L1)

The rewrite is the **identity on the leaf**. Every L2 binding maps to the same L1 binding at the
same position:

    | L2 leaf (`L2/axpbypcz`)              | L1 leaf (`L1/axpbypcz`)             | Mapping  |
    |-------------------------------------|-------------------------------------|----------|
    | `axpbypcz :: (α,x,β,y,γ,z) -> T[N]` | `axpbypcz :: (α,x,β,y,γ,z) -> T[N]` | Identity. Same six-arg signature shape. |
    | `α·x + β·y + γ·z` (fused 3-term)    | `α·x + β·y + γ·z` (fused 3-term)    | Identity. Same per-element kernel; same fused statement. |
    | twelve algebraic laws               | twelve algebraic laws               | Identity. Inherited unchanged (module-action + trilinearity + chained-collapse). |
    | four non-laws (IEEE / fusion)       | four non-laws (IEEE / fusion)       | Identity. Same load-bearing summation-order / fusion non-laws preserved, not erased. |
    | two variant axes (element-type + scalar-promotion sub-axis) | two variant axes | Identity. Same axes; both absorbed at construction. |

There is **no L2 binding without an L1 partner and no L1 binding without an L2 partner**; the
mapping is total and bijective on the leaf. This is the identity-in-form property.

**The one note (fusion deferral).** The L2 layer's defining work is kernel-fusion de-fusion. For
the linear-combination cohort, that work is carried entirely by the fold-parent
[`linear-combination-fold-specialization`](./linear-combination-fold-specialization.md): the
arity-3 single-aligned strided pass (MFEM's 5-arg `add(α, x, β, y, z)`,
`palace/linalg/vector.cpp:749-751`), the `γ != 0` two-call split slow-path
(`AXPBY(α, x, γ, z); z.Add(β, y)`, `:755-756`), the `γ == 0` arity-collapse to `axpby` (the
fold's zero-coefficient term-drop), and the pinned summation order. The `axpbypcz` leaf is the
arity-3 member of that fold; **no fusion structure is unique to the leaf beyond the fold-parent's
arity-3 row**. So this theme's edge is the identity, and bit-reproduction / arity-collapse /
summation-order concerns are read off the fold-parent theme, not re-derived here. (The four
non-laws — IEEE summation-order non-associativity across the two L0 branches, and the
fusion-vs-three-pass bit-non-identity — ride the edge unchanged from L1: they are *recorded* at
the leaf as load-bearing numerical claims, and the *de-fusion mechanics* that make them live are
the fold-parent's.)

## Applicability conditions

The identity rewrite is valid when:

1. **The L2 `axpbypcz` is the leaf-floor realization** ([`L2/axpbypcz`](../L2/axpbypcz.md), the
   same-named arity-3 member of `linear_combination`) — NOT the fold-parent. This is the
   leaf-floor reading (b) (the batch-12-resolved `dot-l2-leaf-floor-vs-fold-only-design` fork,
   recommended KEEP-(b) by the cycle-042 cross-cutter audit). Under a hypothetical fold-only
   reading (a), this theme's LHS would not exist as a standalone L2 `axpbypcz` chapter, and the
   L2>L1 edge for `axpbypcz` would be subsumed into
   [`linear-combination-fold-specialization`](./linear-combination-fold-specialization.md)'s
   arity-3 dispatch row. This condition records the design presupposition explicitly.

2. **The leaf is value-thread-isomorphic across the edge.** The L2 `axpbypcz` leaf and the L1
   `axpbypcz` leaf share the six-arg signature, the per-element kernel, the twelve algebraic laws,
   the four non-laws, and the two variant axes. Confirmed by construction: `L2/axpbypcz` is
   authored as a thin floor entry whose laws are inherited unchanged from `L1/axpbypcz` (wave-1 D5
   §"Algebraic laws", §Signature).

3. **All fusion content is the fold-parent's.** No fusion structure unique to the `axpbypcz` leaf
   (beyond the fold-parent's arity-3 row — the single-aligned `add(α,x,β,y,z)` pass and the
   `γ==0` arity-collapse) exists; the leaf's edge is therefore the identity with a single
   deferring note. The output-aliasing in-place/out-of-place axis is likewise the fold's, not the
   leaf's.

If a future L2 `axpbypcz` variant introduced leaf-specific fusion not absorbed by the fold-parent,
the identity claim would need re-audit — none exists in the current surface.

## Justification kind

**`structural`** (dominant) with secondary **`empirical-match`**.

**Structural (dominant)**: the L2 `axpbypcz` leaf's signature shape
(`Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]`) is identical to
the L1 `axpbypcz` leaf's signature shape — a whole-tensor fused three-term combination with no
element loop exposed at either layer. The rotation between two value-thread-isomorphic leaves with
identical signatures is the identity by construction; the only L2-layer work (fusion de-fusion) is
carried by the fold-parent, leaving the leaf's own edge a no-op.

**Empirical-match (secondary)**: the L1 leaf is firm on direct Palace evidence
([`L1/axpbypcz`](../L1/axpbypcz.md) §Evidence — three template specialisations + member decl at
`palace/linalg/vector.{hpp,cpp}`), and the L2 leaf-floor was authored as value-thread-isomorphic to
it; the two forms agree on every law and every variant axis by independent transcription. The
identity is observational on the two existing firm/firming chapters, not derivational.

## Speculative L1 operators

**None.** Both endpoints are existing vocabulary: the L2 LHS is the `axpbypcz` leaf-floor (firming
cycle-043 wave-1 D5), the L1 RHS is the firm `axpbypcz` leaf (firm cycle-003). The fold-parent
[`linear_combination`](../L2/linear_combination.md) (firm cycle-018) and the sibling
[`linear-combination-fold-specialization`](./linear-combination-fold-specialization.md) (firm
cycle-018/019) are also existing vocabulary. This theme is the identity edge between existing
chapters; it proposes no new operators.

## Verified-against

L2 / L1 anchors (the two endpoints):

- `book/src/L2/axpbypcz.md` (firming cycle-043 wave-1 D5) — the L2 leaf-floor (LHS): the
  same-named arity-3 member of `linear_combination`, value-thread-isomorphic to the L1 leaf, laws
  inherited unchanged. (The chapter lands at this cycle's integration alongside this theme — wave-2
  serial sequencing applies D5 before this theme.)
- `book/src/L1/axpbypcz.md` (firm cycle-003) — the L1 leaf (RHS): signature (`:15-18`), the twelve
  algebraic laws (`:42-70`), the four non-laws (`:72-77`), the two variant axes (`:87-96`), the
  complete L0 evidence list (`:107-116`). Authoritative on every Palace-surface fact.
- `book/src/L2-L1/linear-combination-fold-specialization.md` (firm cycle-018/019) — the fold-parent
  theme this leaf's fusion content defers to (arity-dispatch fusion-selection + pinned summation
  order across `scal`/`axpy`/`axpby`/`axpbypcz`). The `axpbypcz` leaf is the arity-3 member of that
  fold's dispatch.
- `book/src/L2-L1/scal-leaf-identity.md` (firm cycle-041) — the arity-1 sibling row of the
  same fold; the structural template this arity-3 edge follows (degenerate single-term identity →
  arity-3 identity, same fold, same deferral pattern).
- `book/src/L2-L1/dot-leaf-identity.md` (firm cycle-041) — the sibling-shape precedent (identity-in-
  form on a single leaf with all fusion deferred to a fold-parent — there `inner-product-fold-
  specialization`, here `linear-combination-fold-specialization`).

L0 evidence (transitive through the firm L1 leaf / the fold-parent; self-verified via
`tools/citecheck/citecheck.py --anchor` this invocation; paths relative to `reference/palace/`):

- `palace/linalg/vector.cpp:745-758` — `AXPBYPCZ(double, Vector, …)` real-real specialisation with
  the `γ == 0` branch. **Self-verified (anchor `AXPBYPCZ` @746).** The fusion-selection content is
  the fold-parent's; the leaf's edge is identity so no new L0 claim is made here.
- `palace/linalg/vector.cpp:749-751` — the `γ == 0` fast-path MFEM 5-arg `add(α, x, β, y, z)` (the
  arity-3 single-aligned pass / the arity-collapse target). **Self-verified (anchor `add` @751).**
  Deferred to the fold-parent.
- `palace/linalg/vector.cpp:755-756` — the `γ != 0` slow-path two-call split
  `AXPBY(α, x, γ, z); z.Add(β, y)` (the cross-branch summation-order divergence underwriting the
  IEEE non-law). Deferred to the fold-parent; recorded as a leaf non-law.
- `palace/linalg/vector.hpp:313-316` — the free-function template `AXPBYPCZ` decl
  (`z = α·x + β·y + γ·z` comment). **Self-verified (anchor `AXPBYPCZ` @315).** Inherited
  transitively; the leaf's edge is identity so no new L0 claim is made here.

## Status

`firm` — the L2 LHS is the firm-this-cycle leaf-floor (D5 wave-1), the L1 RHS is the firm
`axpbypcz` leaf (cycle-003), and the rotation between two value-thread-isomorphic leaves with
identical six-arg signatures is the identity by construction (§"The rewrite (L2 → L1)" table is
total and bijective on the leaf). The only L2-layer work — kernel-fusion de-fusion (arity-3
single-aligned pass + `γ==0` arity-collapse) — is carried by the firm fold-parent
[`linear-combination-fold-specialization`](./linear-combination-fold-specialization.md) for the
whole arity family; no fusion structure is unique to the `axpbypcz` leaf. No speculative operator,
no negative-anchor reconstruction, no literature inference. The arity-3 sibling of the arity-1
`scal-leaf-identity`, slug `-leaf-identity` per the cycle-042 ratified convention.

> **Design-presupposition note (not a status reduction).** This theme presupposes the **leaf-floor
> (b)** realization of `L2/axpbypcz` (Applicability condition 1; the batch-12-resolved
> `dot-l2-leaf-floor-vs-fold-only-design` fork, recommended KEEP-(b) by the cycle-042 cross-cutter
> audit). Under the fold-only reading (a), this theme's LHS would not exist standalone and the edge
> would fold into `linear-combination-fold-specialization`'s arity-3 dispatch. The theme is
> self-coherent under the leaf-floor reading it is built on.

> **Non-law preservation note (not a status reduction).** The four `axpbypcz` non-laws — IEEE
> summation-order non-associativity (the two L0 real-real branches at `vector.cpp:749-751` vs
> `:755-756` sum in different orders) and the fusion-vs-three-pass bit-non-identity — are
> **preserved, not erased**, across this identity edge. They are recorded at the leaf as
> load-bearing numerical claims; the de-fusion mechanics that make them live are the fold-parent's
> (per `CLAUDE.md` §"Optimization tricks vs. base algebra").

## Open questions / caveats

- **Lifting note (reverse direction, working notes only — NOT in this high→low chapter body).**
  Lifting the L1 leaf *up* to the L2 floor leaf is the value-thread-isomorphic identity rotation:
  the L1 signature has no kernel fusion exposed at the leaf level and no destination buffer — exactly
  the properties that make it L2-native by construction as a fused base primitive (and as the
  arity-3 fold member). No additional structure is required for the lift. This reverse-direction note
  lives in working notes per the high→low layer-definition discipline; the formal chapter narrates
  only L2 → L1.

- **Non-adjacent L2>L0 chain (in-line, not a directory).** This theme's L2>L1 identity ∘ the L1>L0
  `axpbypcz-mutation-rotation` (firm cycle-022) compose to the full L2>L0 story; per the CLAUDE.md
  invariant "Identity rotations across non-adjacent layers are annotated in-line, not via a
  dedicated lowering directory," no `book/src/L2-L0/` directory — the adjacent-edge chain captures
  it.
