# normalize-leaf-identity

The L2>L1 lowering theme for the fused vector-normalisation composite `normalize`. The rewrite is
**identity-in-form on the operator's signature**: the L2 [`normalize`](../L2/normalize.md) floor lowers
to the L1 [`normalize`](../L1/normalize.md) operator with the same signature
`Tensor[N] -> (Scalar, Tensor[N])`, the same fused `(β, x/β)` semantics, the same six algebraic laws,
the same partiality non-law at `x = 0`, and the same single variant axis (element-type) —
value-thread-isomorphic on the operator. Unlike the cycle-041 fold-parented BLAS-1-leaf edges
([`dot-leaf-identity`](./dot-leaf-identity.md), [`scal-leaf-identity`](./scal-leaf-identity.md),
[`nrm2-leaf-identity`](./nrm2-leaf-identity.md)), and unlike the cycle-042 standalone-*leaf*
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

- The cycle-041 **fold-parented** BLAS-1-leaf edges (`dot-leaf-identity`, `scal-leaf-identity`,
  `nrm2-leaf-identity`) are identity-in-form *because* all their L2-layer fusion content is carried
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
