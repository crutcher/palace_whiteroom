# nrm2-body-identity

The L3>L2 lowering theme for the BLAS-1 Euclidean-norm reduction. Lowers the L3 `nrm2`
whole-tensor norm (`book/src/L3/nrm2.md`, firm cycle-011) into the L2 `nrm2` fusion form
(`book/src/L2/nrm2.md`, firm cycle-041). The rewrite is **identity-in-form on the kernel** —
the L3 whole-tensor reduction and the L2 fusion-rotation composition are value-thread-isomorphic
on the primitive's signature; there is no element loop at either layer (the reduction over the
length axis `N` is a single semantic step at both L3 and L2), and the `√ ∘ abs ∘ inner_product`
consumer framing is shared verbatim. This theme is the BLAS-1-leaf analogue of
[`krylov-step-body-identity`](./krylov-step-body-identity.md), whose §"Applicability conditions"
point 3 names `nrm2` among the seven L1 primitives that are **L3-native / L2-native by signature
shape** (no per-element loop visible). Narrated forward: the L3 whole-tensor norm **dissolves**
into the L2 fusion composition with no decomposition and no wrapper rotation — `nrm2` is a leaf
reduction, so unlike `krylov-step` there is no surrounding `(op, K, s)` consolidation or
outer-loop collapse; the identity is total.

## Slug

`nrm2-body-identity`

## Context

`nrm2` is one of the seven L1 primitives that the cycle-002 combinator-miner argument (preserved
verbatim in [`krylov-step-body-identity`](./krylov-step-body-identity.md) §"Verified-against"
bullet 1) and the cycle-006 audit established as **L3-native / L2-native by signature shape**:
each operates on whole-tensor inputs with no element loop exposed at L2, which is what makes the
L3>L2 rotation identity-in-form rather than requiring a decomposition step
([`krylov-step-body-identity`](./krylov-step-body-identity.md) §"Applicability conditions"
point 3, `:97`: "The seven L1 primitives used (`apply_linop`, `axpy`, `axpby`, `axpbypcz`,
`dot`, `nrm2`, `scal`) ... each operates on whole-tensor inputs with no element-loop exposed at
L2 ... each L1 primitive is *also* L3-native because its signature has no per-element loop
visible"). Where `krylov-step-body-identity` ratifies that classification for the *composite*
kernel body (the five-primitive-group let-chain) with two wrapper-level surface adjustments,
this theme ratifies it for the *single leaf* `nrm2` — and the leaf case is strictly simpler:
there is no surrounding wrapper to rotate (no `(op, K, s)` tuple to consolidate, no outer
tail-recursive loop to collapse), so the identity is total on both the kernel and its (absent)
wrapper.

The L3 `nrm2` (firm cycle-011) and the L2 `nrm2` floor (firm cycle-041, wave-1 D2) are both
**layer-coherence entries** per the methodology invariant **Identity-lowerings still require
both L levels** (CLAUDE.md §Methodology invariants, codified cycle-009): each layer is coherent
within itself, so the reduction is defined in L3 vocabulary at L3 and L2 vocabulary at L2, and
this theme is the adjacent-edge identity rotation between them. The L2 floor exists under the
2026-05-31 `l2-floor-under-l3-blas1-cohort` foundation-first directive so the firm L3 anchor
rests on a present adjacent L2 parent; this theme completes that adjacent edge.

## L3 form (LHS)

The L3 form is the whole-tensor Euclidean-norm reduction (`L3/nrm2` §Signature / §Semantics),
rendered as an L3 field operation:

    nrm2 :: Tensor[N] -> Scalar
    nrm2 x = √dot(x, x)                          -- whole-tensor reduction; √ ∘ dot at the diagonal

The signature `Tensor[N] -> Scalar` exposes no element loop — the reduction over `i ∈ [0, N)`
is a single semantic step in the L3 iteration-rotation calculus (`L3/nrm2` §"Iteration-rotation
marker"). There is **no sequential obstruction**: the reduction over independent length-axis
indices is a parallel operation in exact arithmetic; the load-bearing pinned reduction tree at
L0 is a floating-point implementation choice (a recorded non-law), not an algebraic obstruction
at L3. At L3 `nrm2` is **consumed inside** larger forms in two roles — the convergence-test
readout `outputs.residual_norm` and the Arnoldi sub-diagonal `H[j+1,j] = nrm2(w)` (`L3/nrm2`
§"Iteration-rotation marker" points 1-2) — but those iteration views belong to the surrounding
`krylov-step` body / outer convergence-test consumer, not to the `nrm2` leaf itself, which has
no iteration view of its own. The defining identity `nrm2(x) = √dot(x, x)` (L1 law 8, inherited
unchanged at L3) is the structural link to the inner-product surface.

## L2 form (RHS)

The L2 form is the fusion-rotation composition (`L2/nrm2` §Signature / §Semantics), the same
reduction written as `√ ∘ abs ∘ inner_product` at the diagonal `y = x`:

    nrm2 :: Tensor[N] -> Scalar
    nrm2 x = √ (abs (inner_product x x))        -- √ ∘ abs ∘ inner_product at y = x; consumer, NOT a fold member

The L2 form's inner reduction is the firm `inner_product` fold (cycle-019) over the length
axis; `nrm2` post-composes the scalar `abs` and `√` onto the fold output at `y = x` as a
**consumer**, NOT a fold member (do-NOT-merge per [`L2/inner_product`](../L2/inner_product.md)
§"Consumer (NOT an instance)"). The `std::abs` defensive guard is **preserved at L2 as an explicit
load-bearing numerical claim** (the fusion-rotation discipline keeps load-bearing numerical
tricks as algebraic claims); the signature is identical to the L3 form. The only textual
difference from the L3 form is the **inner-reduction name**: L3 writes the defining identity
through `dot(x, x)` (the L3 same-layer leaf, `L3/nrm2` §Dependencies), while L2 writes it
through the `inner_product` fold at the diagonal — these denote the same self-inner-product
value (`dot(x, x) = inner_product(x, x)` at `y = x`; the inner-product fold's diagonal
degeneration, [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md)
§"The diagonal degeneration (`y = x`)").

## The rewrite (L3 → L2)

The rewrite is the **identity on the leaf** — the L3 whole-tensor norm and the L2 fusion
composition are value-thread-isomorphic, with **no wrapper rotation** (the leaf case, simpler
than `krylov-step`):

    nrm2 x  =  √dot(x, x)                        -- L3 whole-tensor reduction (LHS)
            =  √ (abs (inner_product x x))       -- L2 fusion composition (RHS)

The mapping is total and trivial:

| L3 element | L2 element | Mapping |
|---|---|---|
| `nrm2 :: Tensor[N] -> Scalar` | `nrm2 :: Tensor[N] -> Scalar` | Identity. Same signature; no element loop exposed at either layer (`nrm2` is L3-native / L2-native by signature shape per [`krylov-step-body-identity`](./krylov-step-body-identity.md) point 3). |
| `√dot(x, x)` (defining identity through the L3 `dot` leaf) | `√ (abs (inner_product x x))` (defining identity through the L2 `inner_product` fold at `y = x`) | Identity on value. The inner self-inner-product is the same value (`dot(x, x) = inner_product(x, x)` at the diagonal); the L2 form names it as the `inner_product` fold (the L2 inner-product surface) where L3 names it as the `dot` same-layer leaf. The outer `√` is shared; the `abs` is implicit in the L3 form (subsumed by the non-negativity claim) and **preserved-as-explicit** at L2 (load-bearing numerical claim). |
| consumed-inside roles: `outputs.residual_norm`, Arnoldi `H[j+1,j] = nrm2(w)` | consumed by [`krylov-step`](../L2/krylov-step.md) (residual-norm readout + Arnoldi sub-diagonal) | Identity. The surrounding consumer is the same `krylov-step` body at both layers; the consumer's iteration view is wrapper content, not `nrm2` content. **No wrapper rotation on the `nrm2` leaf itself.** |

There is **no surface adjustment** of the kind `krylov-step-body-identity` carries (no
`(op, K, s)` → `IterState` consolidation, no outer-loop collapse) because `nrm2` is a leaf
reduction with no surrounding wrapper of its own — the iteration view is entirely the
*consuming* context's, and that context's rotation is `krylov-step`'s, not `nrm2`'s. The only
textual difference between the L3 and L2 forms is the inner-reduction name (`dot` leaf at L3 vs
`inner_product` fold at L2), which denotes the same diagonal self-inner-product value. This is
the **identity-in-form** property: every L3 element maps to an L2 element at the same position
with the same value, and the leaf carries no wrapper to rotate.

## Applicability conditions

The rewrite is valid when (all hold for the firm L3 form by construction):

1. **`nrm2` is L3-native / L2-native by signature shape.** The signature `Tensor[N] -> Scalar`
   exposes no per-element loop at either layer; the reduction over the length axis is a single
   semantic step at both L3 and L2. This is the condition
   [`krylov-step-body-identity`](./krylov-step-body-identity.md) §"Applicability conditions"
   point 3 (`:97`) names for the whole seven-primitive cohort including `nrm2`; it is what makes
   the rotation identity-in-form rather than requiring a decomposition. Currently satisfied.

2. **The inner self-inner-product denotes the same value at both layers.** The L3 form's
   `dot(x, x)` and the L2 form's `inner_product(x, x)` at the diagonal `y = x` are the same
   Hermitian self-inner-product `Σ_i |x[i]|²` (real, non-negative — L1 dot laws 4 / 9). The L2
   inner-product surface is the *fold* (firm cycle-019); the L3 surface is the *leaf* `dot`
   (firm). Both denote the diagonal degeneration of the same reduction; the L2>L1 sibling theme
   [`nrm2-leaf-identity`](../L2-L1/nrm2-leaf-identity.md) lowers the L2 form the rest
   of the way to the L1 `dot(x, x)` leaf. Currently satisfied.

3. **The `√ ∘ abs` post-step is shared (modulo the abs-preserved/abs-absorbed framing).** The
   outer `√` is identical at both layers (principal non-negative real square root, deterministic
   IEEE-754); the `abs` guard is implicit at L3 (subsumed by the non-negativity claim — `L3/nrm2`
   inherits the L1 treatment) and **preserved as an explicit load-bearing claim** at L2. Both
   treatments are consistent (the guard implements the non-negativity invariant under floating
   point); the framing difference does not change the value. Currently satisfied.

4. **No surrounding wrapper to rotate.** `nrm2` is a leaf reduction; unlike `krylov-step` it has
   no `(op, K, s)` tuple, no outer tail-recursive loop, no `IterState` record. The iteration view
   belongs entirely to the consuming `krylov-step` body / outer convergence-test, whose rotation
   is captured by [`krylov-step-body-identity`](./krylov-step-body-identity.md) /
   [`ksp-solve-outer-driver`](./ksp-solve-outer-driver.md), not by this theme. The leaf identity
   is total. Currently satisfied.

## Justification kind

**`structural`** (dominant) with secondary **`empirical-match`**.

**Structural (dominant)**: each L1/L2/L3 form of `nrm2` has the signature shape
`Tensor[N] -> Scalar` — a whole-tensor reduction with no element loop exposed at L2 or L3. The
L3 vocabulary at this scope demands whole-tensor operations with no element loop; `nrm2`
satisfies this requirement *at L2*, so the rotation is the identity. This is a structural
argument about the `nrm2` signature shape — the same structural argument
[`krylov-step-body-identity`](./krylov-step-body-identity.md) §"Justification kind" gives as its
secondary justification for the whole cohort, applied here to the single leaf.

**Empirical-match (secondary)**: the cycle-002 combinator-miner claim — that L2's primitive
vocabulary (including `nrm2`) is already L3-native by inspection of the slice corpus's L2 and L3
prose — is the original empirical evidence, re-confirmed by the cycle-006 audit and ratified at
[`krylov-step-body-identity`](./krylov-step-body-identity.md) §"Verified-against" bullet 1 (the
terminal firm home of the cycle-002 Claim 2). The L2>L3 lift of `nrm2` is the identity rotation;
therefore the L3>L2 lowering — running the same edge in the opposite direction — is also the
identity rotation. For the *leaf* `nrm2` the empirical-match is even cleaner than for the
composite body: there is no wrapper whose rotation the empirical observation must exclude, so the
observation is total.

**Abstraction-direction note**: L3 is the higher-abstraction layer for this edge (it has the
iteration rotation already done by the L4>L3 hop and speaks about whole-tensor field operations);
L2 is the lower-abstraction layer (it speaks about the primitive composition — here the
`√ ∘ abs ∘ inner_product` fusion form). The rotation direction is L3 → L2: the L3 whole-tensor
norm lowers to the L2 fusion composition by re-naming the inner reduction from the `dot` leaf to
the `inner_product` fold at the diagonal and surfacing the `abs` guard as an explicit
load-bearing claim. There is no wrapper rotation (the leaf has no wrapper); the rotation is the
identity on the leaf. This matches the methodology's lowering direction.

## Speculative L2 operators

**None.** This theme is the identity rotation; no new L2 vocabulary is introduced. The L3 form
referenced in the LHS is the firm [`L3/nrm2`](../L3/nrm2.md) (cycle-011); the L2 form referenced
in the RHS is the firm [`L2/nrm2`](../L2/nrm2.md) (cycle-041, wave-1 D2). Both endpoints exist in
the artifact; the theme ratifies their identity-in-form relationship. The B-weighted overload
(the operator-weighted energy norm, [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)
rough-in at L1) is a separate operator consuming the M-weighted member of `inner_product`, not a
variant of this `nrm2`; named here only to mark the boundary.

## Verified-against

L3 / L2 anchors:

- [`book/src/L3/nrm2.md`](../L3/nrm2.md) (firm cycle-011) — the L3 LHS: whole-tensor reduction
  `√dot(x, x)`, the no-sequential-obstruction iteration-rotation marker, the two consumed-inside
  roles (residual-norm readout + Arnoldi sub-diagonal), the always-real element-type collapse,
  the L1-inherited algebraic laws.
- [`book/src/L2/nrm2.md`](../L2/nrm2.md) (firm cycle-041, wave-1 D2) — the L2 RHS: the
  fusion-rotation form `√ ∘ abs ∘ inner_product` at `y = x`, the consumer-not-fold-member
  boundary, the preserved `std::abs` load-bearing claim.
- [`book/src/L3-L2/krylov-step-body-identity.md`](./krylov-step-body-identity.md)
  §"Applicability conditions" point 3 (`:97`) — the load-bearing statement that the seven L1
  primitives (including `nrm2`) are L3-native / L2-native by signature shape (no per-element
  loop visible). The structural justification this theme applies to the single leaf.
- [`book/src/L2-L1/inner-product-fold-specialization.md`](../L2-L1/inner-product-fold-specialization.md)
  §"The diagonal degeneration (`y = x`)" — the inner-product fold's diagonal degeneration, where
  `dot(x, x) = inner_product(x, x)`; the basis for the inner-reduction-name equivalence in
  §"The rewrite" condition 2.
- [`book/src/L2-L1/nrm2-leaf-identity.md`](../L2-L1/nrm2-leaf-identity.md) (this
  cycle, sibling D5 theme) — the adjacent L2>L1 hop that lowers the L2 `nrm2` form the rest of
  the way to the L1 `nrm2` leaf; together the two D5 themes complete the `nrm2` adjacent-edge
  chain below the firm L3 anchor.

L0 anchor (transitive through L1; verified on-disk this invocation):

- `palace/linalg/vector.hpp:255-260` — `linalg::Norml2` template; body line 259 is
  `return std::sqrt(std::abs(Dot(comm, x, x)));`. The single load-bearing line; the one-line
  unfolded composition that makes both the L3>L2 and the L2>L1 rotations identity-in-form. (Path
  relative to `reference/palace/`; full L0 evidence at [`L1/nrm2`](../L1/nrm2.md) §Evidence.)

## Status

`firm` — the L3 LHS is firm (cycle-011), the L2 RHS is firm (cycle-041, wave-1 D2), and the
rotation is identity-in-form on the leaf: one L3 whole-tensor norm, one L2 fusion composition,
same signature, same value, same defining identity (`nrm2(x) = √dot(x, x)`, L1 law 8 inherited
unchanged). No decomposition (the reduction is a single semantic step at both layers — `nrm2` is
L3-native / L2-native by signature shape), no wrapper rotation (the leaf has no surrounding
`(op, K, s)` tuple or outer loop — strictly simpler than `krylov-step-body-identity`), no
speculative operator, no constructive sub-part (every claim is positively anchored on
fully-specified source). The only textual difference between the L3 and L2 forms is the
inner-reduction name (`dot` leaf at L3 vs `inner_product` fold at L2 at the diagonal), which
denotes the same value. This is the BLAS-1-leaf analogue of
[`krylov-step-body-identity`](./krylov-step-body-identity.md), under the 2026-05-31
`l2-floor-under-l3-blas1-cohort` foundation-first directive: it completes the adjacent edge
below the firm L3 [`nrm2`](../L3/nrm2.md) anchor. A `lowering-verifier` audit attaching a
`verified_against:` block confirming the identity-in-form rotation is the standard follow-up,
not a status reduction.

## L3>L2 vs L2>L1 distinction (the two D5 nrm2 themes)

The two `nrm2` themes landed this cycle (D5) divide the adjacent-edge chain below the firm L3
anchor cleanly, both identity-in-form:

- **L3>L2 (this theme; `nrm2-body-identity`)**: the L3 whole-tensor norm dissolves into the L2
  fusion composition. Identity on the leaf; the only textual change is the inner-reduction name
  (`dot` leaf → `inner_product` fold at the diagonal) and the surfacing of the `abs` guard as an
  explicit L2 claim. No wrapper rotation.
- **L2>L1 (`nrm2-leaf-identity`)**: the L2 fusion composition re-fuses onto the single L1
  `nrm2` leaf. Identity on the primitive's signature; the only change is the resolution drop of
  the `√`/`abs` scalar post-steps (named L2 fusion steps → below-L1-resolution IEEE-754
  primitives) and the absorption of the preserved `abs` guard into the L1 non-negativity claim.

Together they constitute the full L3>L1 lowering chain for `nrm2`, identity-in-form at every hop
(both are no-ops on the buffer side — there is no destination buffer; the result is a returned
scalar). The L1>L0 expansion into the four-stage `Dot → MPI_Allreduce → std::abs → std::sqrt`
chain is the separate firm [`nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) theme,
where the `abs` guard re-materializes as stage 3 and the MPI collective re-appears.
