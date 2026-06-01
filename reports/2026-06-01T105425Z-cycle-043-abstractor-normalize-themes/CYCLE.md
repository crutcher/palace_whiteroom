---
agent: abstractor
invoked_at: 2026-06-01T105425Z
scope: two adjacent thin-identity lowering themes for `normalize` — L2>L1 (`normalize-leaf-identity`) + L3>L2 (`normalize-body-identity`)
status: pending
inputs:
  - reports/2026-06-01T105425Z-cycle-043-harvester-L2-normalize/CYCLE.md (wave-1 D9 — co-landing L2 `normalize` floor; source of truth for the L2 `nrm2 ∘ scal` composite framing + thin-floor reasoning + fork-INDEPENDENT no-fold-parent determination)
  - book/src/L1/normalize.md (firm cycle-027 — the L1 RHS of the L2>L1 edge; signature, six laws, partiality, normalize_B rough-in note, full L0 evidence chain)
  - book/src/L3/normalize.md (firm cycle-039 — the L3 LHS of the L3>L2 edge; iteration-rotation rendering, §27/§131 "no interposed L2 entry" notes that go stale once the D9 floor lands)
  - book/src/L1-L0/normalize-mutation-rotation.md (firm cycle-027 — the substantive rotation in the chain, abstracted away by both identity edges)
  - book/src/L2-L1/reciprocal-leaf-identity.md + book/src/L3-L2/reciprocal-body-identity.md (firm cycle-042 D10 — the fork-INDEPENDENT thin-identity sibling precedents; structure inherited)
  - book/src/L3-L2/krylov-step-body-identity.md (firm cycle-007/009 — point-3 L3-native-by-signature classification + body-vs-wrapper division)
  - L0: palace/linalg/vector.hpp:262-270 (linalg::Normalize), :267 (MFEM_ASSERT partiality), :268 (rescale), :269 (return norm) — all self-verified via citecheck --anchor 2026-06-01
integrated_at: 2026-06-01T140000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-043 batch integration (cohort-completing L2-floor build); D10 normalize theme pair (L2>L1 normalize-leaf-identity + L3>L2 normalize-body-identity); cross-report rename repair (3 classes) applied; clean; see reports/2026-06-01T140000Z-integrator-finalize-cycle-43/CYCLE.md + cycle-043 STAGING row."
---

# CYCLE: two adjacent thin-identity lowering themes for `normalize` — L2>L1 + L3>L2

## Summary

This dispatch authors the **two adjacent thin identity-in-form lowering themes** that flank the co-landing L2 `normalize` floor (wave-1 D9): `book/src/L2-L1/normalize-leaf-identity.md` (the L2>L1 edge, into the firm L1 [`normalize`](../L1/normalize.md)) and `book/src/L3-L2/normalize-body-identity.md` (the L3>L2 edge, from the firm L3 [`normalize`](../L3/normalize.md)). Both edges are **identity-in-form**: the L2 form is value-thread-isomorphic to L1, and L3 to L2 — same signature `Tensor[N] -> (Scalar, Tensor[N])`, same six algebraic laws, same partiality non-law at `x = 0`, same single element-type variant axis. The genuinely-load-bearing framing both themes carry is that `normalize` is a **fused composite — `nrm2 ∘ scal` — that is fork-INDEPENDENT (carries NO fold-parent)**. This makes it a *new sub-shape* relative to the prior thin-identity cohorts: it is **not a leaf** (it has genuine same-layer constituents `nrm2` + `scal`, cited as `consumes`), but it is **also not a fold member** (its codomain `(Scalar, Tensor[N])` is neither reduce-to-`Scalar` nor reduce-to-`Tensor[N]`), so it sits in the same design-final camp as the cycle-042 standalone-floor cohort (`reciprocal`/`elementwise_product`/`assemble-diagonal`/`jacobi-smoother`/`divfree-projector`) — distinct basis (composite-with-no-fold-parent vs standalone-leaf/gate-with-no-fold-parent), same conclusion (unaffected by the `dot-l2-leaf-floor-vs-fold-only-design` fork). Both edges are thin because **there is no genuine kernel fusion to unfold**: Palace's `linalg::Normalize` (`vector.hpp:262-270`) is already the one-line norm-then-rescale composition with the norm reduction (line 266) and rescale (line 268) as separate passes — there is no fused single-pass kernel to de-fuse. The slug convention `-leaf-identity` (L2>L1) / `-body-identity` (L3>L2) is the ratified pattern, matching the cycle-042 `reciprocal`/`elementwise_product` sibling pair. The partiality non-law at `x = 0` (the `MFEM_ASSERT(norm > 0.0)`, the one semantic addition the fusion carries over its total `nrm2`/`scal` constituents) transports unchanged through both edges.

## Proposed changes

```new:book/src/L2-L1/normalize-leaf-identity.md
# normalize-leaf-identity

The L2>L1 lowering theme for the fused vector-normalisation composite `normalize`. The rewrite is
**identity-in-form on the operator's signature**: the L2 [`normalize`](../L2/normalize.md) floor lowers
to the L1 [`normalize`](../L1/normalize.md) operator with the same signature
`Tensor[N] -> (Scalar, Tensor[N])`, the same fused `(β, x/β)` semantics, the same six algebraic laws,
the same partiality non-law at `x = 0`, and the same single variant axis (element-type) —
value-thread-isomorphic on the operator. Unlike the cycle-041 fold-parented BLAS-1-leaf edges
([`dot-leaf-identity`](./dot-leaf-identity.md), [`scal-fold-specialization`](./scal-fold-specialization.md),
[`nrm2-fold-specialization`](./nrm2-fold-specialization.md)), and unlike the cycle-042 standalone-*leaf*
edges ([`reciprocal-leaf-identity`](./reciprocal-leaf-identity.md),
[`elementwise-product-leaf-identity`](./elementwise-product-leaf-identity.md)), `normalize` is a **fused
composite** — it is **not a leaf** (it has genuine same-layer constituents `nrm2` + `scal`, cited as
`consumes`) but is **also not a fold member** (codomain `(Scalar, Tensor[N])` — neither reduce-to-`Scalar`
nor reduce-to-`Tensor[N]`), so it carries **NO fold-parent**. There is therefore no fusion to defer
(contrast `dot-leaf-identity`) *and* no genuine kernel fusion to unfold: Palace's `linalg::Normalize`
already separates the norm pass from the rescale pass. This theme records the identity edge; it is the
L2>L1 analogue of the L3>L2 [`normalize-body-identity`](../L3-L2/normalize-body-identity.md) (the other
thin edge of the same composite).

## Slug

`normalize-leaf-identity`

## Context

`normalize` at L2 is the **floor** entry (`book/src/L2/normalize.md`, harvested cycle-043 D9): the fused
vector-normalisation composite `normalize(x) = (β, x/β)` where `β = ‖x‖₂`, rendered as its own same-named
L2 chapter so the firm L3 [`normalize`](../L3/normalize.md) (cycle-039) rests on an adjacent same-named L2
parent (per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels**) rather
than skipping a layer to L1. It is the **last genuine missing floor** of the `l2-floor-under-l3-leaf-cohort`
directive. This theme is the L2>L1 edge of that floor.

The edge is the **identity-in-form** case: the L2 `normalize` floor and the L1 `normalize` operator are
value-thread-isomorphic on the operator. This is the L2>L1 analogue of the L3>L2
[`normalize-body-identity`](../L3-L2/normalize-body-identity.md) theme (the other thin edge of the same
composite).

**Why this edge is identity AND has no fusion to unfold (the distinction from the prior cohorts).** Three
structurally-distinct prior cohorts inform this edge, and `normalize` differs from all of them:

- The cycle-041 **fold-parented** BLAS-1-leaf edges (`dot-leaf-identity`, `scal-fold-specialization`,
  `nrm2-fold-specialization`) are identity-in-form *because* all their L2-layer fusion content is carried
  by a fold-parent (`inner-product-fold-specialization` / `linear-combination-fold-specialization`).
  `normalize` has **no fold-parent at all**, so there is nothing to defer to.
- The cycle-042 **standalone-leaf / -gate** edges (`reciprocal-leaf-identity`,
  `elementwise-product-leaf-identity`, `jacobi-smoother-leaf-identity`, `assemble-diagonal-leaf-identity`)
  are identity-in-form because each is a *single* leaf / gate field operation with no multi-operation
  kernel fusion. `normalize` is **not a leaf** — it is a fused *composite* with two genuine same-layer
  constituents (`nrm2` for the norm, `scal` for the rescale). So it differs from the standalone-leaf cohort
  on the leaf-vs-composite axis (it has same-layer `consumes` dependencies), while sharing their
  fork-independence (no fold-parent).
- The cycle-042 `divfree-projector-leaf-identity` standalone-*gate* edge is the closest prior shape (a
  composite-of-floors with no fold-parent), but it carries **exactly one genuine fusion rotation** at its
  L2>L1 edge (the step-4 `apply_linop(P.Grad,ψ) ▷ axpy` RE-FUSES into the L1 fused `Grad->AddMult`).
  `normalize` carries **zero** genuine fusion rotations at this edge: Palace's `linalg::Normalize`
  (`palace/linalg/vector.hpp:262-270`) is **already** the one-line composition
  `norm = Norml2(comm, x); x *= 1.0/norm; return norm` — the norm reduction (`:266`) and the rescale
  (`:268`) are already two separate passes; there is no fused single-pass (blocked / SIMD / batched)
  norm-and-rescale kernel to de-fuse. The L2 floor adds the fusion-*naming* (`normalize` framed as the
  `nrm2 ∘ scal` composition), not a fusion *un-folding*.

So `normalize` is a **fused composite with no fold-parent**: it cites its two constituent floors as
*consumed* same-layer dependencies, but the composite itself is neither a fold member nor decomposed by
the L2>L1 edge — the factorisation `normalize(x) = (nrm2(x), scal(1/nrm2(x), x))` (law 6) is the same at
L1 and L2, so the edge is the pure identity on the operator, with the constituent-floor citations carried
unchanged across the edge.

## L2 form (LHS)

The L2 form is the `normalize` floor (`book/src/L2/normalize.md` §Signature, harvested cycle-043 D9) — the
mutation-free fused norm-then-rescale composite, parameterised by element type:

    normalize :: Tensor[N] -> (Scalar, Tensor[N])
    normalize x = (β, x/β)   where  β = nrm2 x,  β > 0

written at L2 as the named composition over the two firm same-layer floors [`nrm2`](../L2/nrm2.md) and
[`scal`](../L2/scal.md):

    normalize x = (nrm2 x, scal (1 / nrm2 x) x)        -- law 6, the fused norm-then-rescale pairing

The L2 form is **pure / out-of-place** (no destination buffer; the result is a fresh `(Scalar, Tensor[N])`
pair). It is **partial**: defined only where `β > 0`, i.e. `x ≠ 0` (the L0 `MFEM_ASSERT(norm > 0.0)`,
`palace/linalg/vector.hpp:267`, lifts as a precondition on the input — `L2/normalize` §Signature). The
returned norm `β` is **load-bearing** (Arnoldi Hessenberg sub-diagonal, power-iteration eigenvalue
estimate, NEP deflation companion-scale — the reason the fusion is named rather than discarded as a bare
`scal(1/nrm2(x), x)`). The L0 receiver-mutating idiom (`x *= 1.0/norm`, the norm returned by value), the
reciprocal-then-multiply trick, and the MPI collective folded inside `Norml2` are NOT in the L2 signature —
they reappear only at the substantive L1>L0 rotation
([`normalize-mutation-rotation`](../L1-L0/normalize-mutation-rotation.md)).

## L1 form (RHS)

The L1 form is the firm `normalize` operator (`book/src/L1/normalize.md` §Signature, firm cycle-027) —
identical in signature, semantics, the six algebraic laws, the partiality precondition, and the single
variant axis:

    normalize :: (x: Tensor[N]) -> (Scalar, Tensor[N])
    normalize(x) = (β, x/β)   where  β = nrm2(x),  β > 0      -- same fused composite, same law 6

The L1 operator is the **mutation-rotation** rendering: it already erases the L0 receiver-self-overwrite
(`x *= 1.0/norm`), folds the reciprocal-vs-divide transparent trick and the MPI collective into the L1>L0
lowering, makes the returned norm a first-class result component, and records the partiality as a
precondition. The L1 entry is authoritative on every Palace-surface fact (the `linalg::Normalize`
free-function template, the three load-bearing consumer shapes, the returned-norm analysis, the
`normalize_B` rough-in note, the complete L0 evidence list); the L2 form does not duplicate them.

## The rewrite (L2 → L1)

The rewrite is the **identity on the operator**. Every L2 binding maps to the same L1 binding at the same
position:

    | L2 floor (`L2/normalize`)                       | L1 operator (`L1/normalize`)                    | Mapping  |
    |-------------------------------------------------|-------------------------------------------------|----------|
    | `normalize :: Tensor[N] -> (Scalar, Tensor[N])` | `normalize :: Tensor[N] -> (Scalar, Tensor[N])` | Identity. Same signature shape. |
    | `normalize x = (nrm2 x, scal (1/nrm2 x) x)`     | `normalize(x) = (nrm2(x), scal(1/nrm2(x), x))`  | Identity. Same fused norm-then-rescale composite; same law-6 factorisation over the same two constituents. |
    | partial: `x ≠ 0` precondition                   | partial: `x ≠ 0` precondition                   | Identity. Same partiality (the `MFEM_ASSERT(norm > 0.0)`), recorded once on the input. |
    | algebraic laws 1–6                              | algebraic laws 1–6                              | Identity. Inherited unchanged (unit output, norm recovery, reconstruction, positive-homogeneity collapse, unit-vector idempotence, factorisation). |
    | non-laws (no totality, nonlinearity, IEEE-754)  | non-laws (no totality, nonlinearity, IEEE-754)  | Identity. The partiality, the nonlinearity, the reciprocal-vs-divide bit-difference, and the load-bearing reduction-tree non-associativity (inherited from `nrm2`) all transport unchanged. |
    | single variant axis: element-type               | single variant axis: element-type               | Identity. Real/complex collapsed to one parameterised operator; norm output always real, unit vector tracks input element type. |
    | consumes: `nrm2` + `scal` (NO fold-parent)      | depends-on: `nrm2` + `scal` (fused composite)   | Identity. The two same-layer constituents are cited unchanged across the edge; the composite has no fold-parent at either layer. |

There is **no L2 binding without an L1 partner and no L1 binding without an L2 partner**; the mapping is
total and bijective on the operator. This is the identity-in-form property.

**The constituent-floor citations carry across the edge, NOT a fusion to defer.** Unlike `dot-leaf-identity`
(whose L2-layer fusion content IS deferred to the fold-parent `inner-product-fold-specialization`),
`normalize` has no fold-parent — and unlike `divfree-projector-leaf-identity` (which carries one genuine
step-4 `AddMult` re-fusion at this edge), `normalize` has **no genuine kernel fusion to unfold**. The L2
floor's two `consumes` floors (`nrm2` for the norm, `scal` for the rescale) are the *same* two constituents
the L1 operator depends on; they are cited unchanged on both sides of the edge. The L2>L1 edge performs no
de-fusion and no fold-deferral — it is the pure identity, with the constituent-floor structure preserved.

## Applicability conditions

The identity rewrite is valid when:

1. **`normalize` is treated as a fused composite over its two firm same-layer floors, NOT decomposed and
   NOT folded.** `normalize` has exactly two L2-internal constituents — [`nrm2`](../L2/nrm2.md) (the norm,
   a *consumer-of* `inner_product`) and [`scal`](../L2/scal.md) (the rescale, the arity-1 *member-of*
   `linear_combination`) — composed by law 6. It has **no fold-parent** (its codomain `(Scalar, Tensor[N])`
   is neither reduce-to-`Scalar` nor reduce-to-`Tensor[N]`), so — like the cycle-042 standalone-floor cohort
   but unlike the cycle-041 fold-parented leaves — there is **no design-fork presupposition** here. The
   `dot-l2-leaf-floor-vs-fold-only-design` fork does not touch this composite (see §Status).

2. **The operator is value-thread-isomorphic across the edge.** The L2 `normalize` floor and the L1
   `normalize` operator share the signature, the law-6 factorisation, the partiality precondition, the six
   algebraic laws, the non-law set, and the single element-type variant axis. Confirmed by construction:
   `L2/normalize` (D9) is authored as a thin floor entry whose laws are inherited unchanged from
   `L1/normalize` (D9 §"Algebraic laws", §Signature).

3. **No genuine kernel fusion to unfold, and no fold-level fusion to defer.** Palace's `linalg::Normalize`
   (`palace/linalg/vector.hpp:262-270`) is already the one-line norm-then-rescale composition — the norm
   reduction (`:266`) and the rescale (`:268`) are already separate passes; there is no fused single-pass
   kernel to de-fuse at this edge. The only L2-genuine content is the fusion-*naming* (the `nrm2 ∘ scal`
   composition), already recorded at the floor. Neither a fold-parent deferral (contrast `dot-leaf-identity`)
   nor a step-4 re-fusion (contrast `divfree-projector-leaf-identity`) applies.

If a future L2 `normalize` variant introduced a genuinely-fused single-pass norm-and-rescale kernel (e.g.
a blocked / SIMD batched normalise), the identity claim would need re-audit — none exists in the current
surface.

## Justification kind

**`structural`** (dominant) with secondary **`empirical-match`**.

**Structural (dominant)**: the L2 `normalize` floor's signature shape
(`Tensor[N] -> (Scalar, Tensor[N])`) is identical to the L1 `normalize` operator's signature shape — a
whole-tensor fused composite with no element loop exposed at either layer (the norm reduction is the
`nrm2` consumer's single semantic step; the rescale is element-local). The rotation between two
value-thread-isomorphic forms with identical signatures and identical law-6 factorisations is the identity
by construction; there is no fold-parent fusion content to defer and no genuine kernel fusion to unfold, so
the composite's own edge is a no-op with the constituent-floor citations preserved.

**Empirical-match (secondary)**: the L1 operator is firm on direct Palace evidence (`L1/normalize`
§Evidence: the `linalg::Normalize` template `palace/linalg/vector.hpp:262-270`, the three consumer sites
`palace/linalg/iterative.cpp:631-632` / `palace/linalg/operator.cpp:673,676` / `palace/linalg/nleps.cpp:610-611,617`), and the L2 floor was authored
(D9) as value-thread-isomorphic to it; the two forms agree on every law, the non-law set, and the single
variant axis by independent transcription. The identity is observational on the two firm/firming chapters,
not derivational.

## Speculative L1 operators

**None.** Both endpoints are existing vocabulary: the L2 LHS is the `normalize` floor (firming cycle-043
D9), the L1 RHS is the firm `normalize` operator (firm cycle-027). This theme is the identity edge between
existing chapters; it proposes no new operators. The B-weighted sibling `normalize_B` (energy-norm
normalisation `(β_B, x/β_B)` with `β_B = √(xᴴ B x)`) is recorded at both floor entries as a **rough-in
note**, NOT a speculative operator of this theme — Palace's fused B-Normalize
(`palace/linalg/operator.hpp:377-384`) is defined-but-uncalled and its norm constituent
[`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) is `rough-in (test-coverage-bounded)`; the identity
edge maps the unweighted Euclidean `normalize` regardless (plain text here, not a live link, since no L2
`normalize_B` chapter exists).

## Verified-against

L2 / L1 anchors (the two endpoints):

- `book/src/L2/normalize.md` (firming cycle-043 D9) — the L2 floor (LHS): the fused `nrm2 ∘ scal`
  composite, value-thread-isomorphic to the L1 operator, six laws + single element-type axis inherited
  unchanged, **fork-INDEPENDENT, NO fold-parent**, thin floor (no genuine fusion to unfold). (The chapter
  lands at this cycle's integration alongside this theme — wave-2 serial sequencing applies D9 before this
  theme.)
- `book/src/L1/normalize.md` (firm cycle-027) — the L1 operator (RHS): signature, the law-6 factorisation,
  the partiality precondition (`x ≠ 0`), the six algebraic laws, the non-law set, the three load-bearing
  consumer shapes, the `normalize_B` rough-in note, the complete L0 evidence list. Authoritative on every
  Palace-surface fact.
- `book/src/L3-L2/normalize-body-identity.md` (firm cycle-043 D10) — the sibling L3>L2 edge of the same
  composite (the other thin edge); co-dispatched this cycle.
- `book/src/L2/nrm2.md` + `book/src/L2/scal.md` (firm cycle-041 D2/D3) — the two same-layer constituent
  floors cited unchanged across the edge (`nrm2` the norm, `scal` the rescale); the law-6 factorisation
  `normalize(x) = (nrm2(x), scal(1/nrm2(x), x))` is the complete L2 decomposition.
- this L2>L1 identity edge composes with the firm L1>L0
  `book/src/L1-L0/normalize-mutation-rotation.md` (firm cycle-027) — the **substantive** rotation in the
  chain, which reintroduces the L0 in-place receiver rescale (`x *= 1.0/norm`), the returned-by-value norm,
  the reciprocal-then-multiply trick, the `MFEM_ASSERT(norm > 0.0)` partiality guard, and the MPI collective
  this identity edge abstracts away (it composes `nrm2-mutation-rotation` + `scal-mutation-rotation`
  sub-pattern A + the returned-scalar binding).

L0 evidence (transitive through the firm L1 operator; self-verified via `tools/citecheck/citecheck.py
--anchor` this invocation, all `[ok]`; paths relative to `reference/palace/`):

- `palace/linalg/vector.hpp:262-270` — `linalg::Normalize` template:
  `auto norm = Norml2(comm, x); MFEM_ASSERT(norm > 0.0, ...); x *= 1.0 / norm; return norm;`. The positive
  source site — `normalize` verbatim, returning the norm; the norm reduction (`:266`) and the rescale
  (`:268`) are already separate passes (what makes this edge carry no genuine fusion to unfold).
  **Self-verified (anchor `Normalize` @262/264).** Inherited transitively; the operator's edge is identity
  so no new L0 claim is made here.
- `palace/linalg/vector.hpp:267` — `MFEM_ASSERT(norm > 0.0, "Zero vector norm in normalization!")` — the
  partiality witness (`x ≠ 0`), the one semantic addition the fusion carries over its total constituents.
  **Self-verified (anchor `MFEM_ASSERT` @267).**
- `palace/linalg/vector.hpp:268` — `x *= 1.0 / norm;` — the in-place rescale (the reciprocal-then-multiply
  L0 form; the algebraic `x/β` at L1/L2). **Self-verified (anchor `1.0 / norm` @268).**
- `palace/linalg/vector.hpp:269` — `return norm;` — the returned norm (load-bearing `result.0`).
  **Self-verified (anchor `return norm` @269).**

## Status

`firm` — the L2 LHS is the firm-this-cycle floor (D9), the L1 RHS is the firm `normalize` operator
(cycle-027), and the rotation between two value-thread-isomorphic forms with identical signatures and
identical law-6 factorisations is the identity by construction (§"The rewrite (L2 → L1)" table is total and
bijective on the operator). `normalize` is a **fused composite with NO fold-parent** — there is no
fold-level fusion content to defer (contrast `dot-leaf-identity`) and no genuine kernel fusion to unfold at
this edge (contrast `divfree-projector-leaf-identity`'s one step-4 re-fusion); the two same-layer
constituent floors (`nrm2` + `scal`) are cited unchanged across the edge. The partiality non-law at `x = 0`
(the `MFEM_ASSERT(norm > 0.0)`, `vector.hpp:267`) transports unchanged. No speculative operator, no
negative-anchor reconstruction, no literature inference.

> **Design-final on the leaf-vs-fold fork (NOT a presupposition, unlike the cycle-041 BLAS-1-floor themes).**
> The batch-12 meta-phase fork `dot-l2-leaf-floor-vs-fold-only-design` concerns whether the L2 BLAS-1
> *fold-member* leaves (`dot`, `scal`) are same-named floors or are absorbed into their fold-parents.
> **`normalize` has no fold-parent** (a fused composite whose codomain is neither reduce-to-`Scalar` nor
> reduce-to-`Tensor[N]`), so neither the (a) fold-only nor the (b) same-named-floor reading re-anchors it —
> its L2 floor can only ever be a standalone same-named composite citing its two constituents. This theme is
> therefore *design-final*, not presuppositional: unlike `dot-leaf-identity` (whose §Status carries a
> design-presupposition note), this theme's identity claim does not depend on the fork's outcome — exactly
> like the cycle-042 standalone-floor cohort, on a *different basis* (composite-with-no-fold-parent rather
> than standalone-leaf-with-no-fold-parent). Note its *constituents* `nrm2` (consumer-of `inner_product`)
> and `scal` (arity-1 member-of `linear_combination`) do carry fold relationships and DO ride the fork at
> their own floors; `normalize` cites them as consumed dependencies, never as a fold of which it is a
> member, so whatever the fork decides about `dot`/`scal`/`nrm2`, this composite's edge stands unchanged.
```

```new:book/src/L3-L2/normalize-body-identity.md
# normalize-body-identity

The L3>L2 lowering theme for the fused vector-normalisation composite `normalize`. The rewrite is
**identity-in-form on the body** with **no wrapper rotation** — `normalize` is a fused whole-tensor
composite, not a step body, so the L3 [`normalize`](../L3/normalize.md) whole-tensor form lowers into the
L2 [`normalize`](../L2/normalize.md) floor form by the identity on the composite itself. There is no
`(op, K, s)`→`IterState` consolidation and no outer-loop dissolution to perform (the two surface adjustments
the sibling [`krylov-step-body-identity`](./krylov-step-body-identity.md) carries at its wrapper);
`normalize` has no wrapper. The body IS the identity. This is the **fused-composite** analogue of the
leaf-primitive [`reciprocal-body-identity`](./reciprocal-body-identity.md) and
[`scal-body-identity`](./scal-body-identity.md), and — like those, and unlike the fold-member BLAS-1 leaves
— **fold-parent-free**: there is no fold-parent at L2 for the composite's fusion content to belong to. The
one structural difference from the standalone-leaf siblings is that `normalize` carries genuine same-layer
L2 dependencies (`nrm2` + `scal`, cited as `consumes`) — it is a *composite*, not a leaf — but the body
edge is identity nonetheless because the law-6 factorisation `normalize(x) = (nrm2(x), scal(1/nrm2(x), x))`
is the same at L3 and L2.

## Slug

`normalize-body-identity`

## Context

The `normalize` lowering relationships span three adjacent layers, all identity-in-form because `normalize`
is a fused whole-tensor composite with no iteration view and no genuine kernel fusion:

- **L3 form** ([`L3/normalize`](../L3/normalize.md), firm cycle-039) — the whole-tensor fused composite
  `normalize :: Tensor[N] -> (Scalar, Tensor[N])`, the iteration-rotation rendering. Carries **no iteration
  view** (fused leaf composite, not a step body) and **no sequential obstruction** (the norm sub-step is
  the parallel `nrm2` reduction, the rescale sub-step is the embarrassingly-parallel `scal`). Partial at
  `x = 0`. The LHS of this theme.
- **L3>L2 form — this theme.** Identity-in-form on the body, no wrapper rotation.
- **L2 form** ([`L2/normalize`](../L2/normalize.md), firm cycle-043 D9) — the fusion-rotation floor: the
  fused `nrm2 ∘ scal` composite. **No fold-parent** (a fused composite whose codomain `(Scalar, Tensor[N])`
  is neither reduce-to-`Scalar` nor reduce-to-`Tensor[N]`), with two genuine same-layer constituent floors
  cited as `consumes`. The RHS of this theme.
- **L2>L1 form** ([`L2-L1/normalize-leaf-identity`](../L2-L1/normalize-leaf-identity.md), firm cycle-043
  D10) — the onward edge into the L1 operator; also identity-in-form.

This theme is the **fused-composite counterpart** of the firm
[`krylov-step-body-identity`](./krylov-step-body-identity.md) (cycle-007/009), and a direct sibling of
[`reciprocal-body-identity`](./reciprocal-body-identity.md) and
[`scal-body-identity`](./scal-body-identity.md) (cycle-041/042). The `krylov-step` theme establishes the
pattern "identity-in-form on the kernel **body**, with surface adjustments at the **wrapper**"; its point-3
applicability condition (`krylov-step-body-identity.md:97`) names the seven BLAS-1 primitives as L3-native
by signature shape: "each operates on whole-tensor inputs with no element-loop exposed at L2. This is what
makes the L3>L2 rotation identity-in-form rather than requiring a decomposition step." `normalize` is the
**fused-composite** realization of the same classification: its signature
`Tensor[N] -> (Scalar, Tensor[N])` exposes no per-element loop (the norm reduction is the `nrm2` consumer's
single semantic step; the rescale is element-local), so it is L3-native by the identical signature criterion
— the body is the identity, **and there is no wrapper at all** — `normalize` is not a step body, so the two
wrapper adjustments the `krylov-step` theme carries have no analog here. The one difference from the
standalone-*leaf* siblings (`reciprocal-body-identity`, `scal-body-identity`): `normalize` is a *composite*
with two genuine same-layer constituents (`nrm2` + `scal`), not a single leaf — but a composite with no
fold-parent, so the fork-independence is preserved and the body edge is still the identity.

The firm L3 entry (`book/src/L3/normalize.md:27,131` §"Downward"/"Lowers to") currently records its lowering
as direct L3>L1 identity-in-form ("no interposed L2 entry and no `L3-L2`/`L3-L1` theme file") via the
non-adjacent in-line convention, because no L2 `normalize` chapter existed. With the L2 `normalize` floor now
present (D9), this theme supplies the **adjacent-edge** L3>L2 rotation the L3 entry's §"Lowers to" had to
skip — so the L3 composite lowers to an adjacent same-named L2 parent (per CLAUDE.md §Methodology invariants
**Identity-lowerings still require both L levels**) rather than non-adjacently to L1. (The L3 entry's
§27/§131 notes go stale once the D9 floor + this theme land; the re-anchor is a downstream-consistency touch
routed to the c044 sweep — see §Open questions.)

## L3 form (LHS)

The L3 whole-tensor form ([`L3/normalize`](../L3/normalize.md) §Signature, firm cycle-039):

    normalize :: Tensor[N] -> (Scalar, Tensor[N])
    normalize x = (β, x/β)   where  β = nrm2 x,  β > 0

Pure / out-of-place; positional values, no monadic effect, no destination buffer. `x : Tensor[N]` a single
length axis, read-only at L3; result `(β, û)` with `β = nrm2(x)` the norm (always real, positive) and
`û = scal(1/β, x)` the unit vector (same axis, same element type). The defining factorisation is law 6:
`normalize(x) = (nrm2(x), scal(1/nrm2(x), x))`. Partial at `x = 0` (the precondition `x ≠ 0`, recorded
once). The operator carries **no iteration view** (fused leaf composite, not a step body) and **no
sequential obstruction** (the norm sub-step is the parallel `nrm2` reduction — clean at L3; the rescale
sub-step is the embarrassingly-parallel element-local `scal`). No L4 wrapper machinery applies (fused leaf
composites appear inside L4 operator bodies as let-bindings, not first-class L4 typed-wrapper anchors — the
cross-layer "L4 candidate CONFIRMED-NOT-NEEDED" verdict for the BLAS-1 / operator-to-data cohort).

## L2 form (RHS)

The L2 floor form ([`L2/normalize`](../L2/normalize.md) §Signature, firm cycle-043 D9):

    normalize :: Tensor[N] -> (Scalar, Tensor[N])
    normalize x = (nrm2 x, scal (1 / nrm2 x) x)        -- law 6, the fused norm-then-rescale composite

The fused vector-normalisation composite in the fusion-rotation vocabulary — a **fused composite with NO
fold-parent** (codomain `(Scalar, Tensor[N])` is neither reduce-to-`Scalar` nor reduce-to-`Tensor[N]`),
citing the two firm same-layer floors [`nrm2`](../L2/nrm2.md) (the norm, a consumer-of `inner_product`) and
[`scal`](../L2/scal.md) (the rescale, the arity-1 member-of `linear_combination`) as `consumes`. The
signature is **textually identical to the L3 form** modulo notation; the law-6 factorisation is the same
fused composition. The six algebraic laws hold unchanged across the edge (L3 §Algebraic laws ≡ L2 §Algebraic
laws — both inherit the L1 operator's six laws). There is **no fold-level fusion note** to carry (no
fold-parent) and **no genuine kernel fusion to unfold** (Palace's `linalg::Normalize` already separates the
norm pass from the rescale pass — the L2-genuine content is fusion-*naming*, not de-fusion); at L3 even the
reciprocal-vs-divide bit-difference drops below the whole-tensor resolution.

## The rewrite (L3 → L2)

The rewrite is the **identity on the fused composite's body**, with **no wrapper adjustment**:

    normalize x   (L3 whole-tensor fused composite)   ⇒   normalize x   (L2 fusion-rotation floor)

The body maps trivially — the same fused composition, same position, same dataflow, over the same two
constituents:

    | L3 form (`L3/normalize`)                          | L2 form (`L2/normalize`)                          | Mapping  |
    |---------------------------------------------------|---------------------------------------------------|----------|
    | `normalize x = (nrm2 x, scal (1/nrm2 x) x)` (whole-tensor fused composite; no iteration view) | `normalize x = (nrm2 x, scal (1/nrm2 x) x)` (fusion-rotation floor; NO fold-parent) | Identity. Same signature, same law-6 fused composition over the same two constituents (`nrm2` + `scal`). The only framing difference is documentary: L3 frames `normalize` as a whole-tensor fused composite in the iteration-rotation vocabulary; L2 frames the same operator as a fused `nrm2 ∘ scal` composition in the fusion-rotation vocabulary. No operational adjustment. |
    | partial: `x ≠ 0`                                  | partial: `x ≠ 0`                                  | Identity. Same partiality precondition (the `MFEM_ASSERT(norm > 0.0)`). |
    | algebraic laws 1–6                                | algebraic laws 1–6                                | Identity. Inherited unchanged across the chain. |
    | element-type variant axis                         | element-type variant axis                         | Identity. Real/complex collapsed; norm output always real, unit vector tracks input. |
    | consumes: `nrm2` + `scal` (NO fold-parent)        | consumes: `nrm2` + `scal` (NO fold-parent)        | Identity. The two same-layer constituents are cited unchanged across the edge; the composite has no fold-parent at either layer. |
    | no iteration view, no obstruction                 | no fold-parent, no genuine fusion                 | Identity. Nothing to rotate (composite, no loop) and nothing to de-fuse (no fold, no genuine kernel fusion — `linalg::Normalize` already separates the norm pass from the rescale pass). |

The mapping is total and bijective on the fused composite's body — the same single law-6 factorisation at
both layers, with the two constituent-floor citations preserved. This is the identity-in-form property.

**There is no wrapper to rotate.** The sibling `krylov-step-body-identity` carries two surface adjustments
at the wrapper around its kernel body — the L3 `(op, K, s)` positional tuple consolidating into the L2
`IterState` record, and the L3 tail-recursive outer loop collapsing to the L2 outer-driver-by-role
reference. **Neither has an analog for `normalize`**: it is a single fused field-operation composite, not a
step body with an `(op, K, s)` carrier and an outer loop. This is the shape of
[`reciprocal-body-identity`](./reciprocal-body-identity.md) / [`scal-body-identity`](./scal-body-identity.md):
the body IS the identity, there is no wrapper, and there is no fold-parent to defer to — the one difference
being that `normalize` is a *composite* (two genuine same-layer constituents) rather than a single leaf, so
the constituent-floor citations (`nrm2` + `scal`) are carried across the edge unchanged.

## Applicability conditions

The identity-in-form rotation is valid (unconditionally, for the firm `normalize` endpoints) when:

1. **`normalize` is treated as a fused composite over its two firm constituents, not decomposed further and
   not folded.** `normalize` decomposes into exactly its two L2/L3 constituents (`nrm2` + `scal`) by law 6;
   the constituents themselves are firm same-layer floors below `normalize`. It has **no fold-parent** (a
   fused composite, not a member of `inner_product` or `linear_combination`; D9 establishes this), so —
   unlike the fold-member BLAS-1 body-identity themes (`dot-body-identity` Applicability condition 2,
   `scal-body-identity` §Status) — there is **no leaf-floor-vs-fold-only design presupposition** for this
   theme's RHS (see §Status).

2. **The signature is whole-tensor at both layers** — `Tensor[N] -> (Scalar, Tensor[N])` with no
   per-element loop exposed at L2 and no iteration view at L3 (the norm reduction is the `nrm2` consumer's
   single semantic step; the rescale is element-local). This is the `krylov-step-body-identity` point-3
   condition applied to the fused `normalize` composite: its signature has no per-element loop visible, so
   it is L3-native by construction and the rotation is identity-in-form rather than a decomposition.

3. **No iteration view, no sequential obstruction, no fold-level fusion, no genuine kernel fusion.**
   `normalize` carries exactly one reduction (the parallel `nrm2` norm) and one element-local map (the
   `scal` rescale); every element of the rescale is independent and the reduction is parallel in exact
   arithmetic. There is no outer loop, no carry trajectory, no recurrence — nothing for the L3 iteration
   rotation to have rotated and nothing for the L3>L2 lowering to dissolve. There is also no fold-parent and
   no genuine multi-operation kernel fusion (Palace's `linalg::Normalize` already separates the norm pass
   from the rescale pass — the only "fusion" is the *naming* of the composition, which is the same at L3 and
   L2). The load-bearing reduction-tree non-associativity (inherited from `nrm2`) is an L0 floating-point
   choice recorded as a non-law, not an L3 obstruction.

## Justification kind

`structural` (dominant) with secondary `empirical-match`.

**Structural (dominant)**: the composite's signature shape `Tensor[N] -> (Scalar, Tensor[N])` is
whole-tensor by construction at both layers — no element loop is exposed at L2, no iteration view at L3. The
L3 vocabulary at this scope demands whole-tensor field operations with no element loop exposed; `normalize`
satisfies this *at L2 already* (its norm reduction is a single `nrm2`-consumer step, its rescale is
element-local `scal`), so the rotation is the identity. This is the same structural argument
`reciprocal-body-identity` / `scal-body-identity` make (and `krylov-step-body-identity` point-3 makes for
each primitive in the kernel body), here applied to a fused composite — and the law-6 factorisation is the
same at both layers, so the constituent-floor citations carry across the edge unchanged.

**Empirical-match (secondary)**: the L3 composite (firm cycle-039) and the L2 floor (firm cycle-043 D9) were
authored independently as value-thread-isomorphic to the same firm L1 operator (cycle-027), and they agree
on every law, the single variant axis (element-type), the non-law set, and the partiality precondition by
independent transcription. The cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit
(`book/src/L3/index.md:44`) classified `normalize` ("fused `nrm2 + scal`") as an **(A) identity-in-form**
backfill candidate; this theme's L3>L2 edge is the fused-composite realization of that audited
classification, now that the L2 floor entry exists for the rotation to target.

## Speculative L2 operators

**None.** This theme is the identity rotation between firm endpoints: the L3 LHS
([`L3/normalize`](../L3/normalize.md)) is firm (cycle-039), and the L2 RHS
([`L2/normalize`](../L2/normalize.md)) is firm (cycle-043 D9). No new L2 vocabulary is introduced. The two
constituent floors (`nrm2`, `scal`) already exist (firm cycle-041 D2/D3). `normalize` does not get its own
L4 typed-wrapper anchor (fused leaf composites appear inside L4 operator bodies as let-bindings — the
cross-layer "L4 candidate CONFIRMED-NOT-NEEDED" verdict for the BLAS-1 / operator-to-data cohort), so there
is no upstream L4>L3 theme for `normalize` either; the L3 form is L3-native by signature and this theme
closes its downward edge to the L2 floor. The B-weighted sibling `normalize_B` is an L1-entry rough-in note
(defined-but-uncalled fused B-Normalize + `matrix-weighted-norm` test-coverage bound), NOT an L2/L3 candidate
— plain text here, not a live link, since no L2/L3 `normalize_B` chapter exists.

## Verified-against

L3 / L2 anchors (firm both sides):

- `book/src/L3/normalize.md` (firm cycle-039) — the L3 whole-tensor form (LHS). Signature (:33-34),
  semantics (one reduction + one element-local map, no iteration view, no sequential obstruction), six
  algebraic laws (:70-75), the single element-type variant axis (:113-117), the §"Lowers to" currently
  recording direct L3>L1 identity via the non-adjacent convention (:131) — this theme supplies the
  now-present adjacent L3>L2 edge (downstream-consistency touch on the L3 entry flagged in §Open questions).
- `book/src/L2/normalize.md` (firm cycle-043 D9) — the L2 floor form (RHS). Identical signature and six
  laws; the fused `nrm2 ∘ scal` composite framing + the **fork-INDEPENDENT, NO fold-parent** /
  design-final determination + the thin-floor (no genuine fusion to unfold) reasoning. (Lands at this
  cycle's integration alongside this theme.)
- `book/src/L2/nrm2.md` + `book/src/L2/scal.md` (firm cycle-041 D2/D3) — the two same-layer constituent
  floors cited unchanged across the edge (`nrm2` the norm consumer-of `inner_product`, `scal` the rescale
  arity-1 member-of `linear_combination`).
- `book/src/L3-L2/reciprocal-body-identity.md` + `book/src/L3-L2/scal-body-identity.md` (firm cycle-042/041)
  — the direct sibling shapes: fold-free `-body-identity` edges, "no wrapper to rotate, the body IS the
  identity". The structure of this theme is inherited from them; the one difference is that `normalize` is a
  *composite* (two same-layer constituents) rather than a single leaf.
- `book/src/L3-L2/krylov-step-body-identity.md:97` (firm cycle-007/009) — §"Applicability conditions"
  point 3: the L3-native-by-signature-shape classification (no per-element loop visible) that is the
  structural justification for this identity edge. **Self-verified (anchor `L3-native` @97 — confirmed by
  the firm `dot-body-identity` / `scal-body-identity` / `reciprocal-body-identity` themes that cite the same
  line).**

L0 evidence (transitive through the firm L1 operator; self-verified via `tools/citecheck/citecheck.py
--anchor` this invocation, all `[ok]`; paths relative to `reference/palace/`):

- `palace/linalg/vector.hpp:262-270` — `linalg::Normalize` template
  (`auto norm = Norml2(comm, x); MFEM_ASSERT(norm > 0.0, ...); x *= 1.0/norm; return norm;`); the norm
  reduction (`:266`) and rescale (`:268`) are already separate passes (what makes this edge carry no
  genuine fusion to unfold). **Self-verified (anchor `Normalize` @262/264).** Inherited transitively; the
  body's edge is identity, no new L0 claim.
- `palace/linalg/vector.hpp:267` — `MFEM_ASSERT(norm > 0.0, ...)` — the partiality witness (`x ≠ 0`).
  **Self-verified (anchor `MFEM_ASSERT` @267).**
- `palace/linalg/vector.hpp:269` — `return norm;` — the load-bearing returned norm (`result.0`).
  **Self-verified (anchor `return norm` @269).**

## Status

`firm` — identity-in-form L3>L2 edge between firm endpoints. The L3 LHS
([`L3/normalize`](../L3/normalize.md)) is firm (cycle-039); the L2 RHS
([`L2/normalize`](../L2/normalize.md)) is firm (cycle-043 D9). The body is the identity rotation on a single
fused composite (the same law-6 factorisation `normalize(x) = (nrm2(x), scal(1/nrm2(x), x))` at both layers,
with the two constituent-floor citations preserved); **there is no wrapper to rotate** (no
`(op, K, s)`→`IterState` consolidation, no outer-loop dissolution — `normalize` is a fused composite, not a
step body) and **no fold-parent to defer fusion to** (codomain `(Scalar, Tensor[N])` is neither
reduce-to-`Scalar` nor reduce-to-`Tensor[N]`), and **no genuine kernel fusion to unfold** (`linalg::Normalize`
already separates the norm pass from the rescale pass). The structural justification (whole-tensor signature,
no element loop, no iteration view) is the `krylov-step-body-identity` point-3 condition applied to the fused
composite; the empirical-match anchor is the firm L1/L2/L3 value-thread-isomorphic chain + the cycle-036
cross-layer (A) identity-in-form classification. The partiality non-law at `x = 0` (`vector.hpp:267`)
transports unchanged. No speculative operator, no negative-anchor reconstruction, no sequential obstruction.
The fused-composite counterpart of `krylov-step-body-identity`, a direct sibling of `reciprocal-body-identity`
/ `scal-body-identity`, additionally fold-free.

> **Design-final on the leaf-vs-fold fork (NOT a presupposition).** The batch-12 meta-phase fork
> `dot-l2-leaf-floor-vs-fold-only-design` concerns the L2 *fold-member* BLAS-1 leaves. `normalize` has **no
> fold-parent** (a fused composite whose codomain is neither reduce-to-`Scalar` nor reduce-to-`Tensor[N]`),
> so its L2 RHS can only ever be a same-named standalone composite citing its two constituents — neither the
> (a) fold-only nor the (b) same-named-floor reading re-anchors it. Unlike `dot-body-identity` /
> `scal-body-identity` (whose §Status carries a design-presupposition note), this theme's RHS is
> design-final; the identity claim does not depend on the fork's outcome — exactly like the cycle-042
> standalone-floor cohort, on a different basis (composite-with-no-fold-parent rather than
> standalone-leaf-with-no-fold-parent). The *constituents* `nrm2` / `scal` do ride the fork at their own
> floors; `normalize` cites them as consumed dependencies, never as a fold of which it is a member, so this
> composite's edge stands unchanged regardless.

## Open questions / caveats

- **Lifting note (reverse direction, working notes only — NOT in this high→low chapter body).** Lifting the
  L2 floor composite *up* to the L3 whole-tensor form is the value-thread-isomorphic identity rotation: the
  L2 signature has no element loop exposed (the norm is a single `nrm2`-consumer reduction, the rescale is
  element-local `scal`), which is exactly what makes it L3-native by construction. No additional structure
  is required for the lift. This reverse-direction note lives here in working notes per the high→low
  layer-definition discipline; the formal chapter narrates only L3 → L2.

- **L3 `normalize` §27/§131 "no interposed L2 entry" goes STALE once the D9 floor + this theme land
  (downstream-consistency touch, route to c044 sweep — NOT corrected here).** The firm L3 entry
  `book/src/L3/normalize.md` records at line 27 ("**Downward** to L1 … with **no interposed L2 entry and no
  `L3-L2`/`L3-L1` theme file**") and line 131 ("The L2 layer hosts no standalone `normalize` entry … the
  L3>L1 hop is therefore direct") that there is no L2 `normalize`. The D9 floor + this theme supersede those
  notes — once landed, the L3 entry's downward rotation should re-anchor to a **direct L3>L2** hop onto the
  new floor (and this `normalize-body-identity` theme), not a layer-skipping L3>L1 hop (and the L3
  frontmatter `lowers_to: book/src/L1/normalize.md (… no L3-L2/L3-L1 theme)` likewise). Per
  one-operator/theme-per-dispatch discipline this is **NOT corrected in this dispatch**; routed to the c044
  sweep (the same OQ the D9 report flagged).

- **Non-adjacent L3>L1 identity is in-line, not a directory.** The transitive L3>L1 identity (this theme's
  L3>L2 identity ∘ the L2>L1 `normalize-leaf-identity` identity) is annotated in-line at the `normalize`
  entries per the CLAUDE.md invariant "Identity rotations across non-adjacent layers are annotated in-line,
  not via a dedicated lowering directory" — no `book/src/L3-L1/` directory. This theme + the co-dispatched
  `normalize-leaf-identity` compose to capture it.
```

```edit:book/src/SUMMARY.md
- [reciprocal-leaf-identity](./L2-L1/reciprocal-leaf-identity.md)
- [normalize-leaf-identity](./L2-L1/normalize-leaf-identity.md)
```

```edit:book/src/SUMMARY.md
- [elementwise_product-body-identity](./L3-L2/elementwise_product-body-identity.md)
- [normalize-body-identity](./L3-L2/normalize-body-identity.md)
```

```edit:book/src/L2-L1/index.md
| [reciprocal-leaf-identity](./reciprocal-leaf-identity.md) | `L2/reciprocal` (firm, cycle-042 D2 floor) | `L1/reciprocal` (firm cycle-033 leaf) | firm *(structural; identity-in-form on the elementwise multiplicative-inverse leaf — value-thread-isomorphic signature + eight laws + single element-type axis; **fold-parent-FREE** — a nonlinear self-map, NOT a member of `inner_product`/`linear_combination`, so NO fusion to defer (contrast `dot-leaf-identity`); only the transparent `s = 1/|z|²` complex-intermediate note; **design-final on the leaf-vs-fold fork — no fold-parent to re-anchor into**)* |
| [normalize-leaf-identity](./normalize-leaf-identity.md) | `L2/normalize` (firm, cycle-043 D9 floor) | `L1/normalize` (firm cycle-027 operator) | firm *(structural; identity-in-form on the operator's signature — value-thread-isomorphic signature + six laws + partiality non-law at `x=0` + single element-type axis; **fused composite — NOT a leaf** (genuine same-layer `consumes`: `nrm2` + `scal`, cited unchanged across the edge) but **fork-INDEPENDENT, NO fold-parent** (codomain `(Scalar, Tensor[N])` — neither reduce-to-`Scalar` nor reduce-to-`Tensor[N]`), so NO fusion to defer (contrast `dot-leaf-identity`) AND **no genuine kernel fusion to unfold** (Palace's `linalg::Normalize` already separates the norm pass from the rescale pass — contrast the one step-4 `AddMult` re-fusion `divfree-projector-leaf-identity` carries); **design-final on the leaf-vs-fold fork**, on the composite-with-no-fold-parent basis; substantive rotation deferred to L1>L0 `normalize-mutation-rotation`)* |
```

```edit:book/src/L3-L2/index.md
| [`elementwise_product-body-identity`](./elementwise_product-body-identity.md) | L3 [`elementwise_product`](../L3/elementwise_product.md) §Signature — the whole-tensor binary field operation `elementwise_product :: (Tensor[N], Tensor[N]) -> Tensor[N]` (Hadamard `a ⊙ b`); leaf primitive, **no iteration view, no sequential obstruction**. | L2 [`elementwise_product`](../L2/elementwise_product.md) §Signature — the base Hadamard-binary-multiply floor leaf; **fork-INDEPENDENT, NO fold-parent**; identical signature + ten laws + two variant axes (element-type + conjugation sub-axis). | `structural` (whole-tensor binary signature, no element loop, no iteration view — `krylov-step-body-identity` point-3 specialized to the standalone fork-independent leaf) + secondary `empirical-match` (firm L1/L2/L3 value-thread-isomorphic chain + cycle-036 (A) identity-in-form classification) | `firm` (cycle-042 D10 abstractor; identity-in-form on the body, **no wrapper to rotate AND no fold-parent to defer to** — direct sibling of `scal-body-identity`/`reciprocal-body-identity`; **design-final on the leaf-vs-fold fork**) |
| [`normalize-body-identity`](./normalize-body-identity.md) | L3 [`normalize`](../L3/normalize.md) §Signature — the whole-tensor fused composite `normalize :: Tensor[N] -> (Scalar, Tensor[N])` (`(β, x/β)` where `β = nrm2 x`; partial at `x=0`); fused leaf composite, **no iteration view, no sequential obstruction**. | L2 [`normalize`](../L2/normalize.md) §Signature — the fusion-rotation floor: the fused `nrm2 ∘ scal` composite; **fork-INDEPENDENT, NO fold-parent** (codomain `(Scalar, Tensor[N])`), with two genuine same-layer `consumes` floors (`nrm2` + `scal`); identical signature + six laws + partiality + element-type axis. | `structural` (whole-tensor composite signature, no element loop, no iteration view — `krylov-step-body-identity` point-3 specialized to the fused composite; the norm sub-step is a single `nrm2`-consumer reduction, the rescale is element-local `scal`) + secondary `empirical-match` (firm L1/L2/L3 value-thread-isomorphic chain + cycle-036 D2 (A) "fused `nrm2 + scal`" identity-in-form classification, `L3/index.md:44`) | `firm` (cycle-043 D10 abstractor; identity-in-form on the body, **no wrapper to rotate AND no fold-parent to defer to AND no genuine kernel fusion to unfold** — fused-composite counterpart of `krylov-step-body-identity`, direct sibling of `reciprocal-body-identity`/`scal-body-identity` but a *composite* not a leaf; **design-final on the leaf-vs-fold fork**, on the composite-with-no-fold-parent basis) |
```

```edit:book/src/L2-L1/index.md
- `elementwise-product-leaf-identity` — the L2 `elementwise_product` floor lowers to the L1 leaf identity-in-form (ten laws + element-type / conjugation axes); **fork-INDEPENDENT, NO fold-parent** (a binary field op; the inverse-subsumption generalisation of `scal`), so NO fusion to defer — the L0 `forall_switch` per-element multiply is already unfolded.
- `normalize-leaf-identity` — the L2 `normalize` floor lowers to the L1 `normalize` operator identity-in-form on the signature; a **fused composite — NOT a leaf** (genuine same-layer `consumes`: `nrm2` + `scal`, cited unchanged) but **fork-INDEPENDENT, NO fold-parent** (codomain `(Scalar, Tensor[N])` — neither reduce-to-`Scalar` nor reduce-to-`Tensor[N]`), so NO fusion to defer (contrast `dot-leaf-identity`) AND **no genuine kernel fusion to unfold** (Palace's `linalg::Normalize` already separates the norm pass from the rescale pass — contrast the one step-4 `AddMult` re-fusion `divfree-projector-leaf-identity` carries); design-final on the leaf-vs-fold fork (composite-with-no-fold-parent basis); substantive rotation deferred to L1>L0 `normalize-mutation-rotation`.
```

```edit:book/src/L3-L2/index.md
- `elementwise_product-body-identity` — the L3 whole-tensor `elementwise_product` Hadamard binary field op lowers to the L2 standalone floor leaf (fork-INDEPENDENT, NO fold-parent); identity-in-form on the body (ten laws + element-type / conjugation axes); no wrapper and no fold-parent to defer to.
- `normalize-body-identity` — the L3 whole-tensor fused `normalize` composite lowers to the L2 same-named fusion-rotation floor (the fused `nrm2 ∘ scal` composite, **fork-INDEPENDENT, NO fold-parent**); identity-in-form on the body (six laws + partiality at `x=0` + element-type axis), no wrapper to rotate, no fold-parent to defer to, and no genuine kernel fusion to unfold; a *composite* (two same-layer `consumes` floors `nrm2` + `scal`) not a single leaf — the fused-composite counterpart of the standalone-leaf siblings.
```

## Speculative operators proposed

**None** (both themes). Both are identity edges between **already-firm / firming-this-cycle** endpoints:

- `normalize-leaf-identity` (L2>L1): LHS = `L2/normalize` floor (firming cycle-043 D9), RHS = `L1/normalize` operator (firm cycle-027). No new L1 vocabulary.
- `normalize-body-identity` (L3>L2): LHS = `L3/normalize` (firm cycle-039), RHS = `L2/normalize` floor (firming cycle-043 D9). No new L2 vocabulary.

The two same-layer constituents (`nrm2`, `scal`) already exist firm at both layers (cycle-041 D2/D3). The B-weighted sibling `normalize_B` is an L1-entry rough-in note (defined-but-uncalled fused B-Normalize at `palace/linalg/operator.hpp:377-384` + `matrix-weighted-norm` test-coverage bound), NOT a speculative operator of either theme.

## Supporting evidence

- **L0 source of truth** — `palace/linalg/vector.hpp:262-270` (`linalg::Normalize`). All four load-bearing anchors self-verified on-disk via `tools/citecheck/citecheck.py --anchor` 2026-06-01, all `[ok]`: `Normalize` → 262/264; `MFEM_ASSERT` → 267 (partiality); `1.0 / norm` → 268 (rescale); `return norm` → 269 (returned norm). The norm reduction (`:266`) and rescale (`:268`) are already two separate passes — the structural fact that makes both edges carry **no genuine kernel fusion to unfold**.
- **Firm endpoints** — `book/src/L1/normalize.md` (firm cycle-027), `book/src/L2/normalize.md` (firming cycle-043 D9, co-landing this cycle), `book/src/L3/normalize.md` (firm cycle-039). The two constituent floors `book/src/L2/nrm2.md` + `book/src/L2/scal.md` (firm cycle-041 D2/D3).
- **Sibling-precedent themes** (structure inherited) — `book/src/L2-L1/reciprocal-leaf-identity.md` + `book/src/L3-L2/reciprocal-body-identity.md` (firm cycle-042 D10; the fork-INDEPENDENT thin-identity sibling pair, slug convention `-leaf-identity`/`-body-identity` ratified), `book/src/L3-L2/scal-body-identity.md` (firm cycle-041; the fold-free body-identity shape), `book/src/L3-L2/krylov-step-body-identity.md:97` (firm cycle-007/009; point-3 L3-native-by-signature classification + body-vs-wrapper division), `book/src/L2-L1/divfree-projector-leaf-identity.md` (firm cycle-042 D6; the closest prior composite-of-floors shape, which DOES carry one genuine step-4 `AddMult` re-fusion — the contrast that makes `normalize`'s zero-fusion-to-unfold determination load-bearing).
- **The substantive rotation in the chain** — `book/src/L1-L0/normalize-mutation-rotation.md` (firm cycle-027): the L1>L0 edge that reintroduces everything both identity edges abstract away (in-place rescale, returned-by-value norm, reciprocal-then-multiply trick, `MFEM_ASSERT` partiality guard, MPI collective).

## Open questions / caveats

- **The `normalize` new sub-shape: fused-composite-with-no-fold-parent.** `normalize` is the first thin-identity entry that is **a composite (genuine same-layer `consumes`) AND fork-INDEPENDENT (no fold-parent)** simultaneously. The cycle-041 cohort is fold-parented leaves; the cycle-042 cohort is standalone leaves/gates with no constituents (or, for `divfree-projector`, a composite-gate that DOES carry one genuine fusion at its L2>L1 edge). `normalize` is the clean case: a composite with two constituents, no fold-parent, and **zero** genuine fusion to unfold (because Palace already ships the unfused two-pass form). Both themes name this sub-shape explicitly and place it in the design-final camp on the composite-with-no-fold-parent basis. A future same-layer-cross-cutter or meta-phase pass may want to record this as a named third thin-identity sub-shape alongside "fold-parented leaf" and "standalone leaf/gate" — flagged, not enacted here.

- **L3 entry §27/§131 + frontmatter `lowers_to` staleness → c044 sweep.** As the D9 report flagged, the firm L3 `normalize` entry's "no interposed L2 entry / no L3-L2 theme" notes (`book/src/L3/normalize.md:27,131`) and its frontmatter `lowers_to` go stale once the D9 floor + this `normalize-body-identity` theme land. The re-anchor (direct L3>L2 hop onto the new floor + this theme) is a **downstream-consistency touch**, NOT corrected in this dispatch per one-theme-per-dispatch discipline; routed to the c044 sweep. (Same OQ the D9 report routes there — this dispatch confirms the L3>L2 theme it should re-anchor to now exists.)

- **Slug-naming-normalization (`-leaf-identity` vs `-body-identity`).** The L2>L1 theme uses `normalize-leaf-identity` and the L3>L2 theme `normalize-body-identity` — the ratified convention (per the dispatch prompt; matching the cycle-042 `reciprocal`/`elementwise_product` sibling pairs). Note `normalize` is a *composite*, not literally a "leaf"/"body" — the slug suffix `-leaf-identity`/`-body-identity` is the cohort-uniform convention name for "thin identity-in-form edge", not a claim that `normalize` is a leaf. The D9 report's §Open-questions anticipated either `normalize-composite-identity` or `normalize-leaf-identity`; the ratified `-leaf-identity`/`-body-identity` is used here for cohort uniformity. If the meta-phase normalization pass (the cycle-041 `-fold-specialization` outlier-normalization OQ, `book/src/L2/index.md:108` / `L2-L1/index.md` §Working-Notes) revisits suffixes, `normalize`'s pair travels with the cohort.

- **Count-ownership deferred to D2.** Per the dispatch directive, this report appends ONLY its two theme rows (L2-L1/index + L3-L2/index dep-maps), two SUMMARY registrations, and two chapter bodies. It does **NOT** touch the consolidated firm-count tallies in either index's §"Cohort growth" / §"Working Notes" (the L2-L1 "firm 10 → 15" tally and the L3-L2 "firm 5 → 10 / `l3-l2-rotation-theme-coverage-gap` 10-of-18" tally) — **D2 owns those this cycle** per the `parallel-blind-shared-index-count-divergence` convention. With these two themes, the L2-L1 cohort gains +1 firm and the L3-L2 cohort gains +1 firm; the owner reconciles the absolute counts post-cohort.
