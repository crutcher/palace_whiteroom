---
layer: L3
operator: nrm2
firmness: firm
lowers_to:
  - book/src/L1/nrm2.md (identity-in-form on the primitive's signature; no L3-L1 theme — see Lowers-to)
lifts_from:
  - book/src/L4/nrm2.md (firm cycle-069 D2 — the L4 Euclidean-norm verb `nrm2(r)`; the kept named abstraction risen to L4 as a named CONSUMER verb of the `inner_product` combinator at the diagonal `y = x` (`√ ∘ abs ∘ inner_product`), NOT a fold member — the do-NOT-merge guard; `concepts/black-box-vs-accelerated-kernels.md` §2; identity-in-form on the body — value-thread-isomorphic, no dedicated L4>L3 theme, the in-line-marker route)
variant_axes:
  - element-type (real / complex; collapsed to single operator at L3 — result is always real)
---

# nrm2

> **Consumer-stub (reduced cycle-052 D3, vocabulary-shift-redirect refactor pass).**
> `nrm2` at L3 is a **CONSUMER** of the inner-product fold (`nrm2(x) = √dot(x, x)`, or through
> the L2 [`inner_product`](../L2/inner_product.md) combinator at the diagonal: `√ ∘ abs ∘
> inner_product` at `y = x`) — it is **NOT a fold member** (the do-NOT-merge carve-out): it
> post-composes the scalar `√` (and the defensive `abs`) onto the fold's output, it does not
> itself fold. Semantics, algebraic laws, and the no-sequential-obstruction verdict are deferred
> to the firm L1 leaf [`L1/nrm2`](../L1/nrm2.md) / the combinator; this stub retains the
> consuming-context framing (residual-norm readout, Arnoldi sub-diagonal), the load-bearing
> `std::abs` guard note, and the kept in-line §"Downward to L2" consumer note.

Whole-tensor Euclidean-norm reduction at L3: `α = ‖x‖₂ = √⟨x, x⟩`. The canonical BLAS-1 norm
primitive rendered as an L3 field operation; the workhorse of residual-norm convergence tests,
basis-vector normalization, and Arnoldi sub-diagonal coefficients at the iteration-rotation layer.
Identity-in-form lowering to L1 [`nrm2`](../L1/nrm2.md); the rotation work is at the surrounding
wrapper (the `krylov-step` body or the outer convergence-test consumer), not on the primitive.

## Signature

    nrm2 :: Tensor[N] -> Scalar
    nrm2(x) = √⟨x, x⟩ = √dot(x, x)

Result is **always real-valued** and non-negative (`nrm2(x) ≥ 0`), regardless of `x`'s element
type. Identical to the L1 signature; full shape contract + algebraic-law listing at the firm L1
leaf [`L1/nrm2`](../L1/nrm2.md).

## Consuming context (the leaf-level fact — RETAINED)

`nrm2` is a leaf reduction at L3 with **no iteration view of its own**; the iteration view is what
the surrounding form provides. It is **consumed inside** larger L3 forms in two distinct roles:

1. **Convergence-test readout in `outputs`** — per `book/src/L3/krylov-step.md` §Semantics, the
   per-step body's `derived_views K' op` projection produces `outputs.residual_norm = sqrt(abs K'.β)`
   (CG, inferred via the recurrence) or `outputs.residual_norm = nrm2(K'.r)` (recompute-from-residual
   variants). The surrounding `iterate_while_L3` outer loop reads `outputs.residual_norm` against the
   convergence predicate.
2. **Arnoldi sub-diagonal coefficient** — `H[j+1, j] = nrm2(w)` after orthogonalization (per
   `palace/linalg/iterative.cpp:631, 810`, the Arnoldi loop's basis-vector normalization). Consumed
   inside the `op.orthog` closure.

There is **no sequential obstruction** for `nrm2` — the reduction over independent length-axis
indices is parallel in exact arithmetic; the load-bearing pinned reduction tree at L0 is a
floating-point implementation choice (a recorded non-law), not an algebraic obstruction at L3.

## The `std::abs` defensive guard (load-bearing leaf-level fact)

The defining identity is `nrm2(x) = √dot(x, x)`; the L0 source is the one-line composition
`std::sqrt(std::abs(Dot(comm, x, x)))` (`palace/linalg/vector.hpp:255-260`). The `std::abs` outer
guard is a **load-bearing defensive non-negativity check** against floating-point round-off pushing
the sum slightly negative on a numerically-zero vector (buying domain-safety for `√`, no NaN). It is
implicit at L3 (subsumed by the non-negativity claim) and preserved as an explicit algebraic claim
at L2; the full classification lives at
[`L1-L0/nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) §"The `std::abs` defensive
guard — classification". The B-weighted overload `linalg::Norml2(comm, x, B, Bx)` is **not** part of
this operator (tracked as rough-in [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) at L1).

## Status

`firm` — consumer-stub. `nrm2` at L3 is a CONSUMER of the inner-product fold (`√dot(x, x)`; through
the L2 [`inner_product`](../L2/inner_product.md) combinator at the diagonal), **not a fold member**
(the do-NOT-merge carve-out). The L3 form is value-thread-isomorphic to the firm L1 leaf
[`L1/nrm2`](../L1/nrm2.md); semantics, algebraic laws, and variant axes are inherited from L1
unchanged. This chapter retains only the consuming-context framing, the `std::abs` guard note, and
the consumer-identity §"Downward to L2" note. The entry exists as a **layer-coherence anchor** per
CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels** (cycle-009
codification). Harvested cycle-011 wave-1 (BLAS-1 reduction cohort backfill); reduced to a
consumer-stub cycle-052 D3 (vocabulary-shift-redirect refactor pass).

## Lowers to

L3 `nrm2` lowers to L1 [`nrm2`](../L1/nrm2.md) as **identity-in-form on the primitive's signature**.
There is no L3-L1 lowering theme (precedent: cycle-010 `L3/krylov-step.md` records its
identity-in-form lowering in-line). The rotation work lives in the surrounding wrapper at the
consuming `krylov-step` body or outer convergence-test consumer, captured by
[`book/src/L3-L2/krylov-step-body-identity.md`](../L3-L2/krylov-step-body-identity.md)
§"Applicability conditions" point 3 (which names `nrm2` among the seven primitives that are
"L3-native because [each primitive's] signature has no per-element loop visible"). The L1>L0
lowering lives at the L1 entry — Palace's `linalg::Norml2` at `palace/linalg/vector.hpp:255-260`
expands into `std::sqrt(std::abs(Dot(comm, x, x)))`, the `Dot` carrying the MPI_Allreduce. None of
this is L3 content.

### Downward to L2 (consumer identity-in-form; no theme file)

L3 `nrm2` lowers to L2 [`nrm2`](../L2/nrm2.md) as **identity-in-form on the primitive's signature**.
There is no dedicated L3>L2 theme file: the rotation is a degenerate identity-in-named-terms
lowering (the only textual delta is the inner-reduction NAME), so under the 2026-06-01
vocabulary-shift redirect it is recorded here in-line.

- **`nrm2` is a CONSUMER of `inner_product`, not a fold member.** At L2 the defining identity is
  written through the `inner_product` fold at the diagonal — `nrm2 x = √ (abs (inner_product x x))`,
  the `√ ∘ abs ∘ inner_product` composition at `y = x`. `nrm2` post-composes two scalar maps (`abs`,
  then `√`) onto the fold's scalar output; it does NOT itself fold and is NOT a member of the fold
  cohort. Merging `nrm2` into `inner_product` would be a category error (the do-NOT-merge boundary,
  carried in the [`inner_product`](../L2/inner_product.md) §"Consumer (NOT an instance)" and
  [`L2/index`](../L2/index.md) §"Fold-cohort boundary"). The L2 entry lists `inner_product` under
  `consumes`, never as a fold the operator instantiates.
- **The only textual change L3 → L2 is the inner-reduction name.** L3 writes the defining identity
  through the same-layer `dot(x, x)` leaf; L2 writes it through the `inner_product(x, x)` fold at the
  diagonal `y = x`. These denote the same Hermitian self-inner-product value (`dot(x, x) =
  inner_product(x, x)` at `y = x` — the inner-product fold's diagonal degeneration,
  [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md) §"The diagonal
  degeneration (`y = x`)"). The signature `Tensor[N] -> Scalar` is identical at both layers; no
  element loop is exposed at either, so the rotation is identity-in-form with **no wrapper to
  rotate** (`nrm2` is a leaf reduction). `nrm2` is L3-native / L2-native by signature shape per
  [`krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md) §"Applicability conditions"
  point 3 (`:97`).
- **The `std::abs` defensive guard is preserved as an explicit load-bearing numerical claim at L2**
  (it is implicit at L3, subsumed by the non-negativity claim). The guard is a no-op in exact
  arithmetic but load-bearing in floating point — it strips a sign that round-off in the reduction
  could have flipped negative on a numerically-zero vector, buying domain-safety for `√` (no NaN).
  Both framings are consistent; the full classification lives at
  [`L1-L0/nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) §"The `std::abs` defensive
  guard — classification".

L0 anchor (transitive through L1; verified on-disk this dispatch via `citecheck --anchor Norml2`):
`palace/linalg/vector.hpp:255-260` — `linalg::Norml2` template; body line 259 is
`return std::sqrt(std::abs(Dot(comm, x, x)));`. The one-line unfolded composition that makes the
L3>L2 rotation identity-in-form. (Path relative to `reference/palace/`; full L0 evidence at
[`L1/nrm2`](../L1/nrm2.md) §Evidence.)

## Lifts from

L3 `nrm2` lifts to the firm L4 [`nrm2`](../L4/nrm2.md) (firm cycle-069 D2) by **identity-in-form
on the body** — the L4 form is the calculus-level named verb re-expressing the diagonal consume of
the [`inner_product`](../L4/inner_product.md) combinator under the `√ ∘ abs` scalar map; it is
value-thread-isomorphic to this L3 consumer-stub (the same `Tensor[N] -> Scalar` `√(abs(inner_product
x x))` skeleton), so there is **no dedicated L4>L3 theme** (the in-line-marker route — no monadic
wrapper / `Solve` monad / convergence predicate to dissolve; the `abs` defensive guard is preserved
as an explicit scalar-map detail at L4). `nrm2` is one of the **kept named abstractions** that rise
to L4 as named verbs *alongside* the general combinator (the permitted dual per
[`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md) §2 — the
literature-standard unit a Krylov / eigen solver description spells residual `nrm2(r)` / the Arnoldi
sub-diagonal `H[j+1,j] = nrm2(w)`), but as a **CONSUMER** of `inner_product`, NOT a fold member (the
do-NOT-merge over-unification guard — split-additivity is lost under `√`). At L4 `nrm2` also still
appears *inside* larger composed entries (e.g. `book/src/L4/krylov-step.md` §Semantics body —
`outputs.residual_norm`) as a let-binding consuming the primitive surface.

> **Superseded.** This entry formerly recorded `nrm2` as having **no L4 entry** — "leaf primitives
> are not first-class L4 vocabulary (per the cycle-010 audit verdict); at L4 `nrm2` appears only
> inside larger composed entries as a let-binding." That blanket "no-L4-by-design" reading was
> **superseded cycle-069 D2** when `nrm2` rose to a firm L4 named verb. Under the 2026-06-01
> VOCABULARY-SHIFT REDIRECT (L4 is the outward backend-lowering target) the per-case disposition of
> [`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md) §2 governs:
> the `inner_product` combinator rises regardless, and the **kept named abstractions `dot` / `nrm2`
> rise alongside it as named verbs** (`nrm2` as a CONSUMER of the combinator, not a member; distinct
> from the *pure accelerated kernels* `scal` / `axpy` / `axpby` / `axpbypcz`, which correctly stay
> low). The cycle-010 verdict was right for accelerated-kernel leaves; `nrm2` is a kept named
> abstraction, not such a leaf.

## Evidence

`nrm2`'s deferred-to homes + retained leaf-level anchors. All semantics/laws evidence is the firm L1
leaf's / the combinator's:

- [`book/src/L1/nrm2.md`](../L1/nrm2.md) (firm cycle-003) — authoritative on Palace surface,
  signature, algebraic laws, variant axes, the defining identity `nrm2(x) = √dot(x, x)`, the
  B-weighted-overload boundary, and the complete L0 evidence list (`palace/linalg/vector.hpp:255-260`,
  `palace/linalg/vector.hpp:262-270`, `palace/linalg/operator.hpp:372-374`, `palace/linalg/operator.cpp:600-619`, etc.).
- [`book/src/L3/dot.md`](./dot.md) (firm cycle-011) — the L3 dependency anchor; the defining
  identity `nrm2(x) = √dot(x, x)` is L3-internal.
- [`book/src/L2/nrm2.md`](../L2/nrm2.md) (firm cycle-041) — the adjacent L2 consumer-stub this lowers
  to; the consumer-not-member framing mirrored.
- [`book/src/L1-L0/nrm2-mutation-rotation.md`](../L1-L0/nrm2-mutation-rotation.md) (firm) — the
  four-stage L0 chain and the full `std::abs` defensive-guard classification (the RETAINED guard's
  home).
- [`book/src/L3/krylov-step.md`](./krylov-step.md) §Semantics + [`book/src/L3-L2/krylov-step-body-identity.md`](../L3-L2/krylov-step-body-identity.md) §"Applicability conditions" point 3 — the consuming context + the structural justification (`nrm2` L3-native by signature shape).
- `palace/linalg/iterative.cpp:408, 568, 578, 582, 631, 756, 762, 810` — CG and GMRES using
  `linalg::Norml2` for the initial RHS norm, true residual norm, and Arnoldi sub-diagonal
  coefficients. Direct evidence `nrm2` is the convergence-test / Arnoldi primitive, inherited
  transitively. (Paths relative to `reference/palace/`.)
- `test/unit/test-vector.cpp:209-211` — direct test: `double norm1 = vec1.Norml2();
  CHECK_THAT(norm1, WithinRel(std::sqrt(14.0)));` for `vec1 = (1, 2, 3)`. L0-equivalent semantic
  documentation, inherited transitively. (Path relative to `reference/palace/`.)
- [`book/src/concepts/nrm2.md`](../concepts/nrm2.md) — the cross-cutting concept page; BLAS-1
  heritage framing. (Note: its scaled-summation stability claim is incorrect per the L1
  correction-pending note at `book/src/L1/nrm2.md:11`; the L1 entry is authoritative.)
