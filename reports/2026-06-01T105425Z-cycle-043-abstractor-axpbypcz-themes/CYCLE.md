---
agent: abstractor
invoked_at: 2026-06-01T105425Z
scope: two adjacent thin-identity lowering themes for axpbypcz — L2>L1 axpbypcz-leaf-identity + L3>L2 axpbypcz-body-identity
status: pending
inputs:
  - reports/2026-06-01T105425Z-cycle-043-harvester-L2-axpbypcz/CYCLE.md (wave-1 D5; the co-landing L2 floor — source-of-truth for the L2 axpbypcz form)
  - book/src/L1/axpbypcz.md (firm; the L1 leaf — RHS of the L2>L1 edge)
  - book/src/L3/axpbypcz.md (cycle-011 firm; the L3 leaf — LHS of the L3>L2 edge)
  - book/src/L2/linear_combination.md (firm cycle-018; the fold-parent — §Fusion note line 243, §Variant axes line 214)
  - book/src/L1-L0/axpbypcz-mutation-rotation.md (firm cycle-022; the onward L1>L0 edge)
  - book/src/L2-L1/dot-leaf-identity.md (cycle-041; the L2>L1 leaf-identity precedent)
  - book/src/L3-L2/scal-body-identity.md (cycle-041 D6; the L3>L2 body-identity arity-1 fold-member precedent)
  - book/src/L3-L2/krylov-step-body-identity.md:97 (firm; names axpbypcz L3-native by signature shape)
  - dispatch: cycle-043 D8 (wave-2); slugs -leaf-identity / -body-identity ratified
integrated_at: 2026-06-01T140000Z
integration_commit: 3f9a7d0
integration_notes: "cycle-043 batch integration (cohort-completing L2-floor build); D8 axpbypcz theme pair (L2>L1 axpbypcz-leaf-identity + L3>L2 axpbypcz-body-identity); cross-report rename repair applied; clean; see reports/2026-06-01T140000Z-integrator-finalize-cycle-43/CYCLE.md + cycle-043 STAGING row."
---

# CYCLE: axpbypcz adjacent thin-identity lowering themes (L2>L1 + L3>L2)

## Summary

`axpbypcz` (`z ← α·x + β·y + γ·z`, the fused arity-3 three-term linear combination) is firm
at L1 ([`axpbypcz`](../../book/src/L1/axpbypcz.md)) and L3
([`axpbypcz`](../../book/src/L3/axpbypcz.md)), and gets its L2 floor this cycle (wave-1 D5,
co-landing [`L2/axpbypcz`](../../book/src/L2/axpbypcz.md)). It is the **arity-3 member of the
[`linear_combination`](../../book/src/L2/linear_combination.md) fold**, the direct arity-sibling
of the arity-1 [`scal`](../../book/src/L2/scal.md) floor (cycle-041 D3). This D8 dispatch authors
the **two adjacent thin identity-in-form lowering themes** that close the `axpbypcz` floor's
downward edges:

- **L2>L1** — `axpbypcz-leaf-identity`: the L2 leaf-floor lowers to the firm L1 leaf
  value-thread-isomorphic on the primitive (identical six-arg signature, twelve laws, four
  non-laws, two variant axes). The L2-layer fusion work — the arity-3 single-aligned
  `add(α,x,β,y,z)` pass + the `γ==0` arity-collapse — is **deferred to the fold-parent**
  [`linear-combination-fold-specialization`](../../book/src/L2-L1/linear-combination-fold-specialization.md),
  exactly as `dot-leaf-identity` defers to `inner-product-fold-specialization`. The leaf's own
  edge is the identity.
- **L3>L2** — `axpbypcz-body-identity`: the L3 whole-tensor field operation lowers to the L2
  floor leaf identity-in-form on the body, **no wrapper to rotate** (`axpbypcz` is a leaf, not a
  step body — no `(op, K, s)`→`IterState` consolidation, no outer-loop dissolution). The
  leaf-primitive counterpart of `krylov-step-body-identity`, mirroring `scal-body-identity` as
  the arity-3 fold-member analogue.

Both are `firm` identity-in-form edges between firm/firming endpoints, narrated high→low. No
speculative operators. The slugs use the ratified `-leaf-identity` / `-body-identity` convention
(the cycle-042 uniform convention; `axpbypcz` IS a fold-member like `scal`, but the dispatch
ratifies `-leaf-identity` rather than the cycle-041 `scal`/`nrm2` `-fold-specialization` outliers
— the fold-membership / fusion-deferral is recorded in the body, not the slug).

## Proposed changes

### Theme 1 — L2>L1 `axpbypcz-leaf-identity`

```new:book/src/L2-L1/axpbypcz-leaf-identity.md
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
[`scal-fold-specialization`](./scal-fold-specialization.md) (the arity-1 row) and the sibling
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
[`scal-fold-specialization`](./scal-fold-specialization.md). It shares the
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
- `book/src/L2-L1/scal-fold-specialization.md` (firm cycle-041 D6) — the arity-1 sibling row of the
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
`scal-fold-specialization`, slug `-leaf-identity` per the cycle-042 ratified convention.

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
```

### Theme 2 — L3>L2 `axpbypcz-body-identity`

```new:book/src/L3-L2/axpbypcz-body-identity.md
# axpbypcz-body-identity

The L3>L2 lowering theme for the fused arity-3 BLAS-1-extended leaf `axpbypcz`. The rewrite is
**identity-in-form on the body** with **no wrapper rotation** — `axpbypcz` is a leaf whole-tensor
field operation, not a step body, so the L3 whole-tensor form lowers into the L2 floor form by the
identity on the primitive itself. There is no `(op, K, s)`→`IterState` consolidation and no
outer-loop dissolution to perform (the two surface adjustments that the sibling
[`krylov-step-body-identity`](./krylov-step-body-identity.md) carries at its wrapper); `axpbypcz`
has no wrapper. The body IS the identity. This is the leaf-primitive analogue of the `krylov-step`
body-identity theme and the arity-3 fold-member sibling of [`scal-body-identity`](./scal-body-identity.md)
(the arity-1 member of the same `linear_combination` fold).

## Slug

`axpbypcz-body-identity`

## Context

The `axpbypcz` lowering relationships span three adjacent layers, all identity-in-form because
`axpbypcz` is a fused BLAS-1-extended leaf with no iteration view and a single fused field
operation:

- **L3 form** ([`L3/axpbypcz`](../L3/axpbypcz.md), firm cycle-011) — the whole-tensor field
  operation `axpbypcz :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Scalar -> Tensor[N] ->
  Tensor[N]`, the iteration-rotation rendering. Carries **no iteration view** (leaf primitive, not
  a step body) and **no sequential obstruction** (every element independent under the per-element
  fused combination). The LHS of this theme.
- **L3>L2 form — this theme.** Identity-in-form on the body, no wrapper rotation.
- **L2 form** ([`L2/axpbypcz`](../L2/axpbypcz.md), firming cycle-043 wave-1 D5) — the
  fusion-rotation floor leaf, the base fused three-term linear-combination primitive and the
  arity-3 member of the [`linear_combination`](../L2/linear_combination.md) fold. The RHS of this
  theme.
- **L2>L1 form** ([`L2-L1/axpbypcz-leaf-identity`](../L2-L1/axpbypcz-leaf-identity.md), this cycle
  D8) — the onward edge into the L1 leaf; also identity-in-form (all fusion deferred to the fold's
  arity-3 row).

This theme is the **leaf-primitive counterpart** of the firm
[`krylov-step-body-identity`](./krylov-step-body-identity.md) (cycle-007/009), and the direct
arity-3 sibling of [`scal-body-identity`](./scal-body-identity.md) (the arity-1 fold member,
cycle-041 D6). The `krylov-step` theme establishes the pattern "identity-in-form on the kernel
**body**, with surface adjustments at the **wrapper**"; its point-3 applicability condition names
the seven L1 primitives — including **`axpbypcz`** — as L3-native by signature shape: "each operates
on whole-tensor inputs with no element-loop exposed at L2. This is what makes the L3>L2 rotation
identity-in-form rather than requiring a decomposition step (each L1 primitive is *also* L3-native
because its signature has no per-element loop visible)" (`krylov-step-body-identity.md:97`). This
theme is the standalone-leaf realization of that classification for `axpbypcz`: the body is the
identity, **and there is no wrapper at all** — `axpbypcz` is not a step body, so the two wrapper
adjustments the `krylov-step` theme carries (the `(op, K, s)`→`IterState` consolidation and the
outer-loop-to-driver-by-role dissolution) have no analog here.

## L3 form (LHS)

The L3 whole-tensor form ([`L3/axpbypcz`](../L3/axpbypcz.md) §Signature):

    axpbypcz :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]
    axpbypcz α x β y γ z = α·x + β·y + γ·z

Pure / out-of-place; positional values, no monadic effect, no destination buffer. `α, β, γ`
scalars (`real` or `complex`, or `real` promoted against complex tensors); `x, y, z : Tensor[N]`
sharing one length axis, read-only at L3 (`z` is the *prior* value when used as a fused update);
result `Tensor[N]` of the same axis with `result[i] = α·x[i] + β·y[i] + γ·z[i]` for every
`i ∈ [0, N)`. The operator carries **no iteration view** (it is a leaf field operation, not a step
body) and **no sequential obstruction** (every element is independent of every other under the
per-element fused combination — embarrassingly parallel, fully GPU-friendly). No L4 wrapper
machinery applies (the L4 candidate for `axpbypcz` is CONFIRMED-NOT-NEEDED per the cycle-010 cohort
audit — leaf primitives appear inside L4 operator bodies as let-bindings, e.g. inside
`krylov-step`'s three-vector slice update, not as first-class L4 typed-wrapper anchors).

## L2 form (RHS)

The L2 floor form ([`L2/axpbypcz`](../L2/axpbypcz.md) §Signature):

    axpbypcz :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]
    axpbypcz α x β y γ z = α·x + β·y + γ·z

The base fused three-term linear-combination leaf in the fusion-rotation vocabulary — **and** the
arity-3 member of the [`linear_combination`](../L2/linear_combination.md) fold
(`axpbypcz(α, x, β, y, γ, z) = linear_combination [(α, x), (β, y), (γ, z)]`, cited NOT merged). The
signature is **textually identical to the L3 form** modulo notation; the body is the same single
fused whole-tensor field operation. The twelve algebraic laws + four non-laws hold unchanged across
the edge (L3 §Algebraic laws ≡ L2 §Algebraic laws — both inherit the L1 leaf's twelve laws and four
non-laws). The only fusion note the L2 floor carries is the arity-3 single-aligned `add(α,x,β,y,z)`
pass / `γ==0` arity-collapse (the arity-3 case of the fold's fusion note); at L3 even that note is
absent (L3 exposes no element loop at all). The output-aliasing in-place/out-of-place variant is the
fold's axis, not the leaf's; this floor is uniformly pure.

## Rewrite shape

The rewrite is the **identity on the leaf primitive's body**, with **no wrapper adjustment**:

    axpbypcz α x β y γ z   (L3 whole-tensor field op)   ⇒   axpbypcz α x β y γ z   (L2 floor leaf)

The body maps trivially — one binding, one primitive, same position, same dataflow:

| L3 form | L2 form | Mapping |
|---|---|---|
| `axpbypcz α x β y γ z = α·x + β·y + γ·z` (whole-tensor field operation; no iteration view) | `axpbypcz α x β y γ z = α·x + β·y + γ·z` (base fused three-term floor leaf; arity-3 fold member) | Identity. Same six-arg signature, same single fused field operation. The only framing difference is documentary: L3 frames `axpbypcz` as a whole-tensor field operation in the iteration-rotation vocabulary; L2 frames the same operator as a base fusion-rotation primitive (and as the arity-3 fold member). No operational adjustment occurs. |

**There is no wrapper to rotate.** The sibling `krylov-step-body-identity` carries two surface
adjustments at the wrapper around its kernel body: (1) the L3 `(op, K, s)` positional tuple
consolidates into the L2 unified `IterState` record (state-hiding), and (2) the L3 tail-recursive
outer loop `iterate_while_L3` collapses to the L2 outer-driver-by-role reference
(abstraction-by-role). **Neither has an analog for `axpbypcz`**: `axpbypcz` is a single fused leaf
field operation, not a step body with an `(op, K, s)` carrier and an outer loop. There is no
`IterState` (no state record — `axpbypcz` is a pure positional function), and there is no outer
driver (no loop folds `axpbypcz` calls at the operator itself; `axpbypcz` is *called by* step
bodies like `krylov-step`'s `krylov_update` three-vector slice patterns — Chebyshev, BiCGStab — but
those loops belong to the step body, not to `axpbypcz`). The mapping is total and bijective on a
single binding — the degenerate maximal case of the identity-in-form property.

## Applicability conditions

The identity-in-form rotation is valid (unconditionally, for the firm `axpbypcz` endpoints) when:

1. **`axpbypcz` is treated as a leaf primitive, not decomposed.** `axpbypcz` does not decompose into
   other L3 or L2 primitives — the fused three-term linear combination is a single field operation;
   its sub-operations (three scalar multiplies, two element-wise additions) are below both layers'
   resolution. The `axpby-as-primitive` decision
   ([`scaffolding/decisions/axpby-as-primitive.md`](../../../scaffolding/decisions/axpby-as-primitive.md))
   keeps the BLAS-1 leaves firm (fuse, don't decompose; the decision record explicitly invites the
   `axpbypcz` harvester to mirror the fused-primitive choice). Decomposing it into chained `axpby`
   calls is precisely the choice the decision declines.

2. **The signature is whole-tensor at both layers** —
   `Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` with no
   per-element loop exposed at L2 and no iteration view at L3. This is exactly the
   `krylov-step-body-identity` point-3 condition specialized to the standalone `axpbypcz` leaf:
   `axpbypcz`'s signature has no per-element loop visible (it is named at line 97 among the seven
   L3-native primitives), so it is L3-native by construction and the rotation is identity-in-form
   rather than a decomposition.

3. **No iteration view, no sequential obstruction.** `axpbypcz` is element-local, reduction-free,
   rank-local; every element is independent. There is no outer loop, no carry trajectory, no
   recurrence — so there is nothing for the L3 iteration rotation to have rotated and nothing for the
   L3>L2 lowering to dissolve. The fused statement is preserved (the fusion has algebraic meaning),
   and the `γ==0` arity-collapse / single-aligned-pass fusion content is the fold-parent's concern at
   the L2>L1 edge, not an L3>L2 obstruction.

## Justification kind

`structural` (dominant) with secondary `empirical-match`.

**Structural (dominant)**: the leaf's signature shape
`Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]` is whole-tensor by
construction at both layers — no element loop is exposed at L2, no iteration view at L3. The L3
vocabulary at this scope demands whole-tensor field operations with no element loop exposed;
`axpbypcz` satisfies this *at L2 already*, so the rotation is the identity. This is a structural
argument about the leaf's signature, and it is the same structural argument the
`krylov-step-body-identity` theme makes as its secondary justification for each primitive in the
kernel body (point-3 condition, naming `axpbypcz` explicitly at line 97) — here promoted to dominant
because there is no kernel body wrapping the leaf, only the leaf itself.

**Empirical-match (secondary)**: the cross-layer-cross-cutter identity-in-form audit
(`reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md`
§"(2) the BLAS-1 cohort") classified the `axpbypcz` L3↔L1 rotation as identity-in-form by inspection
of the firm L3>L2 and L4>L3 themes; the firm `krylov-step-body-identity` names `axpbypcz` L3-native
at line 97. This theme's L3>L2 edge is the standalone-leaf realization of that audited
classification, now that the L2 floor entry exists (cycle-043 wave-1 D5) for the rotation to target.
The empirical evidence is observational about the firm artifact's existing classification of
`axpbypcz`; the structural signature argument is why it holds.

## Speculative L3 operators

**None.** This theme is the identity rotation between firm endpoints: the L3 LHS
([`L3/axpbypcz`](../L3/axpbypcz.md)) is firm (cycle-011), and the L2 RHS
([`L2/axpbypcz`](../L2/axpbypcz.md)) is firming (cycle-043 wave-1 D5). No new L3 vocabulary is
introduced. `axpbypcz` does not get its own L4 typed-wrapper anchor (leaf primitives appear inside
L4 operator bodies as let-bindings — the cycle-010 cohort audit "L4 candidate CONFIRMED-NOT-NEEDED"
verdict for the BLAS-1 cohort), so there is no upstream L4>L3 theme for `axpbypcz` either; the L3
form is L3-native by signature and this theme closes its downward edge to the L2 floor.

## Verified-against

L3 / L2 anchors (firm both sides):

- `book/src/L3/axpbypcz.md` (cycle-011 firm) — the L3 whole-tensor form (LHS). Signature,
  semantics (element-local, reduction-free, rank-local, no iteration view, no sequential
  obstruction), twelve algebraic laws, four non-laws, the leaf-not-step-body §"Iteration-rotation
  marker", two variant axes.
- `book/src/L2/axpbypcz.md` (firming cycle-043 wave-1 D5 floor) — the L2 floor form (RHS). Identical
  signature and twelve laws; the base fused three-term linear-combination leaf framing + the arity-3
  fold-membership identity (`axpbypcz(α,x,β,y,γ,z) = linear_combination [(α,x),(β,y),(γ,z)]`).
- `book/src/L3-L2/krylov-step-body-identity.md:97` (cycle-007/009 firm) — the mirror precedent
  classifying `axpbypcz` (among the seven L1 primitives) as L3-native by signature shape at its
  point-3 applicability condition. The structural justification this theme promotes to dominant.
- `book/src/L3-L2/scal-body-identity.md` (cycle-041 D6 firm) — the arity-1 fold-member sibling of the
  same `linear_combination` fold; the structural template this arity-3 edge follows.

Cross-layer audit (the empirical-match anchor):

- `reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md`
  §"(2) the BLAS-1 cohort" — the HIGH CONFIDENCE classification of the `axpbypcz` rotation as
  identity-in-form, the dispatch rationale for the cycle-011 L3 `axpbypcz` backfill and (now) this
  L3>L2 edge.

Onward edges (cross-reference, not this theme's content):

- `book/src/L2-L1/axpbypcz-leaf-identity.md` (this cycle D8) — the onward L2>L1 edge into the L1
  leaf; also identity-in-form (all fusion deferred to the fold's arity-3 row). Co-dispatched this
  cycle.
- `book/src/L1/axpbypcz.md` (cycle-003 firm) + `book/src/L1-L0/axpbypcz-mutation-rotation.md` (firm
  cycle-022) — the L1 leaf and its in-place L0 mutation rotation (4 sub-patterns + the
  mixed-justification `γ==0` algebraic sub-rule), reached via the onward edge.

Transitive L0 evidence (inherited from the firm L1 leaf; not re-localized — identity-in-form edge,
L0 evidence transitive through L1; paths relative to `reference/palace/`):

- `palace/linalg/vector.cpp:745-758` — real-real `AXPBYPCZ` specialisation with the `γ==0` branch
  (`add(α,x,β,y,z)` fast-path at `:751`; `AXPBY(α,x,γ,z); z.Add(β,y)` slow-path at `:755-756`).
- `palace/linalg/vector.hpp:313-316` — the free-function template `AXPBYPCZ` decl
  (`z = α·x + β·y + γ·z`).

## Status

`firm` — identity-in-form L3>L2 edge between firm endpoints. The L3 LHS
([`L3/axpbypcz`](../L3/axpbypcz.md)) is firm (cycle-011); the L2 RHS
([`L2/axpbypcz`](../L2/axpbypcz.md)) is firming this cycle (wave-1 D5). The body is the identity
rotation on a single fused leaf field operation; **there is no wrapper to rotate** (no
`(op, K, s)`→`IterState` consolidation, no outer-loop dissolution — `axpbypcz` is a leaf, not a step
body). The structural justification (whole-tensor six-arg signature, no element loop, no iteration
view) is the `krylov-step-body-identity` point-3 condition specialized to the standalone leaf
(naming `axpbypcz` at line 97) and promoted to dominant; the empirical-match anchor is the firm
cross-layer audit + the `krylov-step-body-identity:97` L3-native classification. No speculative
operator, no negative-anchor reconstruction, no sequential obstruction. The arity-3 fold-member
counterpart of `scal-body-identity` (arity-1), both leaf members of the `linear_combination` fold.

A standing design fork (`dot-l2-leaf-floor-vs-fold-only-design`; batch-12-resolved, recommended
KEEP-(b) by the cycle-042 cross-cutter audit) is whether the BLAS-1 / linear-combination leaf cohort
should be realized as standalone same-named floors (the **(b)** realization this theme is built on)
or absorbed into the `linear_combination` fold (the **(a) fold-only** reading). Under the fold-only
reading, the L2 RHS this theme targets would re-point from a standalone `axpbypcz` floor to the
fold's arity-3 row. The theme is stated against the (b) realization, consistent with the firm L2
floor entry D5 lands this cycle.

## Open questions / caveats

- **Lifting note (reverse direction, working notes only — NOT in this high→low chapter body).**
  Lifting the L2 floor leaf *up* to the L3 whole-tensor form is the value-thread-isomorphic identity
  rotation: the L2 signature has no element loop exposed, which is exactly what makes it L3-native by
  construction. No additional structure is required for the lift. This reverse-direction note lives
  here in working notes per the high→low layer-definition discipline; the formal chapter narrates
  only L3 → L2.

- **Non-adjacent L3>L1 identity is in-line, not a directory.** The transitive L3>L1 identity (this
  theme's L3>L2 identity ∘ the L2>L1 `axpbypcz-leaf-identity` identity) is annotated in-line at the
  `axpbypcz` entries per the CLAUDE.md invariant "Identity rotations across non-adjacent layers are
  annotated in-line, not via a dedicated lowering directory" — no `book/src/L3-L1/` directory. This
  theme + the co-dispatched `axpbypcz-leaf-identity` compose to capture it.

- **L3 `axpbypcz` staleness (cycle-044 sweep, NOT here).** The firm L3 `axpbypcz` entry currently
  says the L3→L1 rotation "does not pass through L2 because `axpbypcz` is an L1 leaf, not an L2
  composition" (`L3/axpbypcz.md:106,125`), predating both the L2 floor (D5) and this L3>L2 edge. Now
  that an adjacent same-named L2 floor exists, that prose wants a light refresh (the L3>L2 hop is
  identity-in-form to this floor, then this floor is identity-in-form to L1). Deferred to a cycle-044
  sweep, flagged in the D5 OQ as well; not authored here (this theme is correct as written — it
  lowers the L3 leaf to the L2 floor identity-in-form, exactly as `scal-body-identity` does).
```

### L2/index.md dep-map row (L2>L1 theme registration)

The L2>L1 theme list lives in `book/src/L2-L1/index.md`. Append ONE row to the theme-list table,
immediately after the `scal-fold-specialization` row (line 15 — the arity-1 fold-member sibling).
**COUNT-OWNERSHIP: this report appends ONLY this row; D2 owns the consolidated firm running-count
tally / §Vocabulary-cohort / §Working-Notes count prose.**

```edit:book/src/L2-L1/index.md
[INSERT (1) — theme-list table row — immediately after line 15 (the `scal-fold-specialization`
row), before the `inner-product-fold-specialization` row (line 16). New row:]

| [axpbypcz-leaf-identity](./axpbypcz-leaf-identity.md) | `L2/axpbypcz` (firm, cycle-043 D5 leaf-floor) | `L1/axpbypcz` (firm leaf, cycle-003) | firm *(structural; identity-in-form on the fused arity-3 three-term linear-combination leaf — value-thread-isomorphic six-arg signature + twelve laws + four non-laws + two variant axes; the **arity-3 fold-member analogue** of `scal-fold-specialization` (arity-1) — all L2-layer fusion (the single-aligned `add(α,x,β,y,z)` pass + the `γ==0` arity-collapse + pinned summation order) deferred to the fold-parent `linear-combination-fold-specialization`; output-aliasing axis is the fold's; four IEEE/fusion non-laws preserved-through-the-edge NOT erased; slug `-leaf-identity` per the cycle-042 ratified convention; leaf-floor reading (b) per the batch-12-resolved `dot-l2-leaf-floor-vs-fold-only-design` fork, recommended KEEP-(b) by the cycle-042 cross-cutter audit)* |

[INSERT (2) — §Vocabulary-cohort bullet (D8's OWN per-theme cohort entry; NOT the consolidated
running-count tally / sub-cohort-header count prose, which is D2's) — into the §"Vocabulary cohort"
fold-parented BLAS-1-floor sub-list, immediately after the `scal-fold-specialization` bullet (line
46), matching the sibling bullet format:]

- `axpbypcz-leaf-identity` — the L2 `axpbypcz` leaf-floor lowers to the L1 `axpbypcz` leaf identity-in-form on the fused arity-3 three-term primitive; the **arity-3 fold-member analogue** of `scal-fold-specialization` (arity-1) — all L2-layer fusion (the single-aligned `add(α,x,β,y,z)` pass + the `γ==0` arity-collapse + pinned summation order) deferred to the fold-parent `linear-combination-fold-specialization`; output-aliasing axis is the fold's; four IEEE/fusion non-laws preserved-through-the-edge NOT erased. Slug `-leaf-identity` per the cycle-042 ratified convention; leaf-floor reading (b) per the batch-12-resolved `dot-l2-leaf-floor-vs-fold-only-design` fork.
```

### L3/index.md dep-map row — N/A (L3>L2 theme list lives in L3-L2/index.md)

The L3>L2 theme list lives in `book/src/L3-L2/index.md` (NOT `book/src/L3/index.md`). Append ONE
row to the theme-list table, immediately after the `scal-body-identity` row (line 17 — the arity-1
fold-member sibling). **COUNT-OWNERSHIP: this report appends ONLY this row; D2 owns the consolidated
firm running-count tally / §Vocabulary-cohort / §Working-Notes count prose.**

```edit:book/src/L3-L2/index.md
[INSERT (1) — theme-list table row — immediately after line 17 (the `scal-body-identity` row),
before the `assemble-diagonal-body-identity` row (line 18). New row:]

| [`axpbypcz-body-identity`](./axpbypcz-body-identity.md) | L3 [`axpbypcz`](../L3/axpbypcz.md) §Signature — the whole-tensor fused three-term field operation `axpbypcz :: Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Scalar -> Tensor[N] -> Tensor[N]`; leaf primitive, **no iteration view, no sequential obstruction** (per-element fused combination, embarrassingly parallel). | L2 [`axpbypcz`](../L2/axpbypcz.md) §Signature — the base fused three-term linear-combination floor leaf (arity-3 member of `linear_combination`, cited NOT merged); identical six-arg signature. | `structural` (whole-tensor six-arg signature, no element loop, no iteration view — `krylov-step-body-identity` point-3 condition specialized to the standalone leaf, which names `axpbypcz` L3-native at `:97`) + secondary `empirical-match` (firm cross-layer identity-in-form audit + `krylov-step-body-identity:97` L3-native classification) | `firm` (cycle-043 D8 abstractor; identity-in-form on the body, **no wrapper to rotate** — the arity-3 fold-member counterpart of the arity-1 `scal-body-identity`, both leaf members of the `linear_combination` fold) |

[INSERT (2) — §Vocabulary-cohort bullet (D8's OWN per-theme cohort entry; NOT the consolidated
`firm 5 → 10` running-count tally / coverage-gap progress prose, which is D2's) — into the
§"Vocabulary cohort" *Identity-in-form BLAS-1-leaf body edges (cycle-041; FOLD-PARENTED ...)*
sub-list, immediately after the `scal-body-identity` bullet (line 35), matching the sibling bullet
format:]

- `axpbypcz-body-identity` — the L3 whole-tensor `axpbypcz` fused three-term field operation lowers to the L2 base fused-three-term floor leaf (arity-3 fold member); the body IS the identity, there is no wrapper to rotate — the arity-3 fold-member counterpart of the arity-1 `scal-body-identity`.
```

### SUMMARY.md registrations

Two chapter entries, under the respective Parts. **The integrator applies these.**

```edit:book/src/SUMMARY.md
[(1) under the L3 > L2 Part, immediately after `- [scal-body-identity](./L3-L2/scal-body-identity.md)`
(line 46), insert:]
- [axpbypcz-body-identity](./L3-L2/axpbypcz-body-identity.md)

[(2) under the L2 > L1 Part, immediately after `- [scal-fold-specialization](./L2-L1/scal-fold-specialization.md)`
(line 78), insert:]
- [axpbypcz-leaf-identity](./L2-L1/axpbypcz-leaf-identity.md)
```

## Speculative operators proposed

**None.** Both themes are identity edges between firm/firming endpoints:

- L2>L1 `axpbypcz-leaf-identity`: LHS = `L2/axpbypcz` (firming cycle-043 wave-1 D5), RHS =
  `L1/axpbypcz` (firm cycle-003). Fold-parent `linear_combination` (firm cycle-018) and
  `linear-combination-fold-specialization` (firm cycle-018/019) are existing vocabulary.
- L3>L2 `axpbypcz-body-identity`: LHS = `L3/axpbypcz` (firm cycle-011), RHS = `L2/axpbypcz`
  (firming cycle-043 wave-1 D5). No L4 anchor (CONFIRMED-NOT-NEEDED per cycle-010 cohort audit).

No new L1/L2/L3 operators are introduced. Harvester has nothing to promote from these themes.

## Supporting evidence

- **Source-of-truth files** (read this invocation): wave-1 D5
  `reports/2026-06-01T105425Z-cycle-043-harvester-L2-axpbypcz/CYCLE.md` (the co-landing L2 floor —
  the authoritative L2 `axpbypcz` form, §Signature / §Algebraic-laws / §Variant-axes / §Status);
  firm L1 `book/src/L1/axpbypcz.md` (twelve laws, four non-laws, two variant axes, L0 evidence
  chain); firm L3 `book/src/L3/axpbypcz.md` (cycle-011 identity-in-form backfill); firm L1>L0
  `book/src/L1-L0/axpbypcz-mutation-rotation.md` (cycle-022; the onward edge — 4 sub-patterns + the
  `γ==0` mixed-justification sub-rule).
- **Precedent themes** (mirrored): `book/src/L2-L1/dot-leaf-identity.md` (the L2>L1 leaf-identity
  shape — identity-in-form leaf with fusion deferred to a fold-parent); `book/src/L3-L2/scal-body-identity.md`
  (the L3>L2 body-identity arity-1 fold-member shape — direct sibling); `book/src/L2-L1/scal-fold-specialization.md`
  (the arity-1 L2>L1 row of the same fold); `book/src/L3-L2/krylov-step-body-identity.md:97` (names
  `axpbypcz` L3-native by signature shape — verified this invocation).
- **L0 anchors self-verified 2026-06-01** via `tools/citecheck/citecheck.py --anchor` (read directly
  from `reference/palace/palace/linalg/vector.{hpp,cpp}`):
  - `vector.cpp:745-758` — real-real `AXPBYPCZ` (anchor `AXPBYPCZ` @746). ✓
  - `vector.cpp:749-751` — `γ==0` fast-path `add(α,x,β,y,z)` (anchor `add` @751). ✓
  - `vector.hpp:313-316` — free-function template decl (anchor `AXPBYPCZ` @315). ✓
- **Fold-parent section anchors verified**: `book/src/L2/linear_combination.md` §Variant axes @214,
  §Fusion note @243 (grep-confirmed this invocation).
- **Count-ownership**: per dispatch, this report appends ONLY its two theme bodies + two dep-map
  rows (one in `L2-L1/index.md`, one in `L3-L2/index.md`) + two SUMMARY registrations. The
  consolidated firm running-count tallies, §Vocabulary-cohort lists, and §Working-Notes cohort-growth
  prose in both index files are D2's this cycle — NOT touched here.

## Open questions / caveats

- **Slug convention (ratified `-leaf-identity` / `-body-identity`).** Per dispatch, the slugs use
  the cycle-042 uniform `-leaf-identity` (L2>L1) / `-body-identity` (L3>L2) convention. Note
  `axpbypcz` IS a fold-member (like `scal`, whose cycle-041 L2>L1 edge used the `-fold-specialization`
  slug — one of the two cycle-041 outliers the cycle-042 cross-cutter flagged for meta-phase
  normalization, `L2/index.md:64`). The dispatch ratifies `-leaf-identity` for `axpbypcz` (aligning
  with the cycle-042 cohort, NOT the cycle-041 `scal`/`nrm2` outliers); the fold-membership and
  fusion-deferral are recorded in the body text, not the slug. This is consistent — `dot-leaf-identity`
  is also a fold-member edge (member of `inner_product`) that used `-leaf-identity`. Surfaced for the
  integrator / any later meta-phase slug-normalization pass.

- **D2 count-ownership boundary.** Both index files (`L2-L1/index.md`, `L3-L2/index.md`) carry
  consolidated firm running-counts and §Vocabulary-cohort / §Working-Notes cohort-growth prose that
  this cycle's D2 owns. This report's two `edit:` blocks insert ONLY the two new theme-list rows
  (one per index), positioned right after the respective arity-1 `scal` sibling rows. D2 will
  reconcile the L2>L1 firm count (currently "15 firm + 1 partly-constructive" per
  `L2-L1/index.md:63`) and the L3>L2 firm count (currently "firm 5 → 10" per `L3-L2/index.md:48`),
  the §Vocabulary-cohort bullets, and the `l3-l2-rotation-theme-coverage-gap` progress line
  (currently "10-of-18") to include these two themes. Flagged for the integrator's serial sequencing:
  apply D5 (the L2 floor) and these two themes before D2's count consolidation.

- **L3 `axpbypcz` staleness refresh (cycle-044, shared with D5).** Both the D5 floor and this D8
  L3>L2 theme surface that `L3/axpbypcz.md:106,125` carries stale "does not pass through L2" prose
  predating the L2 floor. A light cycle-044 sweep should refresh it (the L3>L2 hop is now
  identity-in-form to the floor). Not authored here — the floor and themes are correct as written;
  the L3 entry's framing is the only stale surface. Deferred.

- **Onward `L2-L1/axpbypcz-leaf-identity` cross-reference in the co-landing L2 floor.** The wave-1 D5
  L2 floor forward-references the L2>L1 lowering theme as plain text "an `L2-L1/axpbypcz-fusion`
  (or sibling-named) theme" (D5 §"Lowering themes" + §Open-questions). With this theme now named
  `axpbypcz-leaf-identity` (NOT `-fusion`), the integrator may optionally upgrade that D5 plain-text
  forward-reference to a live link to `./axpbypcz-leaf-identity.md` once both land (per skill
  `upgrade-plain-text-ref-to-live-link-when-target-on-disk`). Noted, not enacted (cross-report edit
  to D5's content is outside this dispatch's authority).
