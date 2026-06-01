---
layer: L2
operator: nrm2
firmness: firm
lowers_to:
  - book/src/L1/nrm2.md (identity-in-form on the primitive's signature; the L2>L1 rotation is a degenerate identity-in-named-terms lowering recorded in-line at §"Lowers to" / §"Downward to L1" — no theme file per the 2026-06-01 vocabulary-shift redirect)
lifts_from:
  - book/src/L3/nrm2.md (identity-in-form; L3 is the iteration-rotation view of the same reduction — see Lifts-from)
consumes:
  - book/src/L2/inner_product.md (nrm2 = √ ∘ inner_product at y=x — CONSUMER, not a fold member; do-NOT-merge per L2 §"Fold-cohort boundary")
variant_axes:
  - element-type (real / complex; collapsed to single operator at L2 — result is always real)
---

# nrm2

Euclidean-norm reduction rendered at L2 (the fusion-rotation layer): `α = ‖x‖₂ = √⟨x, x⟩`. The canonical BLAS-1 norm primitive written as the algebraic composition `√ ∘ abs ∘ inner_product` over the length axis, with HPC/SIMD optimization tricks unfolded (here: none to unfold — Palace's `linalg::Norml2` is already the one-line unfolded form). Identity-in-form lowering to L1 [`nrm2`](../L1/nrm2.md); the fusion-rotation work that L2 nominally performs (unfold fused kernels into base-algebra composition) is a **no-op on the buffer side** for this leaf, so the entry exists primarily as a **layer-coherence floor** — present so the firm L3 [`nrm2`](../L3/nrm2.md) rests on an adjacent L2 parent.

## Context

L2 is the **fusion-rotation** layer: each operation is written as a composition of base tensor / operator / quadrature primitives, with cache-blocked loops, SIMD intrinsics, packed formats, and batched specialized BLAS calls **unfolded back into the base algebras** (per [`L2/index`](./index.md) §Context). For `nrm2` there is **no fusion trick to unfold** — Palace's `linalg::Norml2` is a one-line free-function template whose body `std::sqrt(std::abs(Dot(comm, x, x)))` is *already* the base-algebra composition. The L2 rendering therefore adds no decomposition over the L1 form; it adds the **fusion-rotation framing** — naming `nrm2` as the `√ ∘ abs ∘ inner_product` composition in L2 vocabulary — and preserves the one load-bearing numerical trick (the `std::abs` guard) as an explicit algebraic claim.

This entry is a **layer-coherence floor** per the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, codified cycle-009 meta-phase). The L2 form is value-thread-isomorphic to the L1 form — the rotation L2→L1 is identity-in-form on the primitive's signature; only the surrounding layer's framing differs (fusion-rotation view at L2 vs. mutation-rotation view at L1). The floor exists under the 2026-05-31 foundation-first directive (`l2-floor-under-l3-leaf-cohort`): the firm L3 [`nrm2`](../L3/nrm2.md) (cycle-011) must rest on a *present* adjacent L2 parent, not skip a layer.

The L1 entry [`L1/nrm2`](../L1/nrm2.md) (firm cycle-003) is **authoritative on every factual claim about the Palace surface** — in particular: Palace's `linalg::Norml2` computes the naive `√⟨x, x⟩` via `Dot`, **not** the BLAS scaled-summation algorithm (the [`concepts/nrm2`](../concepts/nrm2.md) page's claim to the contrary is a correction-pending item noted at `book/src/L1/nrm2.md:11`). This L2 entry does not duplicate the L0 evidence list or the algebraic-law derivations; it states the laws (which hold uniformly across L1 / L2 / L3 because the body is identity-in-form across the chain) and cites the L1 entry as the anchor.

### Consumer of `inner_product`, NOT a fold member (load-bearing)

The L2 fold-cohort comprises two reductions sharing a `foldl` skeleton: [`inner_product`](./inner_product.md) folds the **length axis** to a `Scalar`, and [`linear_combination`](./linear_combination.md) folds the **term axis**, keeping `Tensor[N]` (per [`L2/index`](./index.md) §"Fold cohorts"). **`nrm2` is a CONSUMER of `inner_product`, not an instance of it:**

    nrm2(x) = √ (abs (inner_product(x, x)))        -- √ ∘ abs ∘ inner_product at y = x

`nrm2` post-composes the scalar square-root (and the defensive `abs`) onto the `inner_product` fold at the diagonal `y = x`; it does not itself fold. Merging `nrm2` into `inner_product` would be a category error — `inner_product` is the length-axis homomorphism producing `dot(x, x)`; `nrm2` is the scalar map `α ↦ √|α|` applied to that fold's output. The do-NOT-merge boundary is carried in the [`inner_product`](./inner_product.md) dep-map row ("Consumer (NOT an instance): `nrm2` / `matrix-weighted-norm` = `√ ∘ inner_product` at `y=x`") and in [`L2/index`](./index.md) §"Fold-cohort boundary". This entry honors that boundary: it lists `inner_product` under `consumes`, never under "this operator IS a member of the fold".

The B-weighted overload `linalg::Norml2(comm, x, B, Bx) = √(xᴴ B x)` (`palace/linalg/operator.cpp:600-619`, declared `palace/linalg/operator.hpp:372-374`) is **not** part of this operator (per the L1 entry's boundary documentation at `book/src/L1/nrm2.md:13`). It is the operator-weighted energy norm — a separate L2 candidate consuming the M-weighted member of `inner_product` (`inner_product_M(x, M, x) = xᴴ M x`) rather than the plain fold — tracked as rough-in [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) at L1. At L2 the same boundary holds: `nrm2` is the unweighted Euclidean reduction.

## Signature

    nrm2 :: Tensor[N] -> Scalar
    nrm2(x) = √⟨x, x⟩ = √ (abs (inner_product(x, x)))

The L2 signature is identical to the L1 and L3 signatures; only the surrounding layer's framing differs.

Shape contract (bunsen-style, named axis; no element loop exposed at L2 — the fusion rotation erases any inner SIMD/blocked loop):

- **`x`** — `Tensor[N]` — read-only whole-tensor argument.
- **result** — `Scalar` — **always real-valued** (`real`), regardless of whether `x` is real or complex.
- The result is non-negative: `nrm2(x) ≥ 0`.

The "result is always real" rule is load-bearing — it is what makes the element-type axis collapse to a single L2 operator (in contrast to `dot` / `inner_product`, where the result element-type tracks the input). It follows from the fact that `inner_product(x, x) = dot(x, x)` is a non-negative real scalar for both real (L1 dot law 4) and complex (L1 dot law 9) inputs.

No element loop is exposed at L2 — the reduction over `i ∈ [0, N)` is the `inner_product` fold's single semantic step, and the post-composed `abs` and `√` are scalar operations on its output. This is what makes `nrm2` a clean L2 composition by signature shape (the seven BLAS-1 primitives including `nrm2` are L2-native / L3-native because their signatures have no per-element loop visible, per `book/src/L3-L2/krylov-step-body-identity.md:97`).

## Semantics

Fusion-rotation composition with defining identity: `nrm2(x) = √ (abs (inner_product(x, x)))`, the principal (non-negative) square root of the (defensively sign-stripped) Hermitian self-inner-product. At L2 the reduction is the `inner_product` fold over the length axis; `nrm2` post-composes two scalar maps onto it.

For real element-type: `nrm2(x) = √Σ_i x[i]²`.

For complex element-type: `nrm2(x) = √Σ_i |x[i]|² = √Σ_i (re(x[i])² + im(x[i])²)`. The Hermitian self-inner-product `inner_product(x, x) = Σ_i conj(x[i])·x[i] = Σ_i |x[i]|²` is real and non-negative element-wise. Inherited unchanged from [`L1/nrm2`](../L1/nrm2.md) §Semantics.

**The `std::abs` defensive guard is preserved as an explicit load-bearing numerical claim** (L2 discipline: load-bearing numerical tricks survive the fusion rotation as explicit algebraic claims, per [`L2/index`](./index.md) §Semantics). It is a no-op in exact arithmetic (the self-inner-product is non-negative real, so `abs` of it equals it) but **load-bearing in floating point**, where it strips a sign that round-off in the reduction could have flipped negative on a numerically-zero vector, buying **domain-safety for `√` (no NaN)**. The full classification (load-bearing-defensive, property-it-buys = non-negativity invariant for the square root) lives at [`L1-L0/nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) §"The `std::abs` defensive guard — classification". At L2 it is named as a preserved scalar guard composed onto the fold output; at L1 it is recognized as a floating-point implementation detail that disappears (the algebraic claim that `inner_product(x, x)` is non-negative real subsumes it). Both treatments are consistent: the guard *implements* the non-negativity claim under floating point.

Reduction-tree non-associativity is **load-bearing** — inherited unchanged from the `inner_product` fold (and through it from `dot`). The square root and `abs` are deterministic IEEE-754 scalar operations (correctly rounded), so `nrm2`'s non-determinism is entirely the fold's. Recorded as a non-law (see §Algebraic laws).

The MPI collective is **not** in the L2 signature — single-rank is in scope per CLAUDE.md §Scope. The reduction at L2 is a single fold step; the local-then-collective two-step reappears only in the L1>L0 lowering (at the `inner_product` / `dot` leaf, per [`L1-L0/nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) §"L0 form (RHS)").

## Algebraic laws

The L2 algebraic laws are **inherited unchanged from L1** because the L2 form is value-thread-isomorphic to the L1 form. Inheritance is total: every L1 law for `nrm2` holds at L2 with the same statement, and every L1 non-law remains a non-law at L2. The laws are reproduced here so the L2 reader does not have to reach to L1 for the listing.

The laws below hold for both real and complex element-types of `x`; absences are deliberate.

1. **Non-negativity**: `nrm2(x) ≥ 0` for all `x`.
2. **Positive-definite (separation)**: `nrm2(x) = 0` iff `x = 0` (in exact arithmetic). The "iff" direction follows from `dot` law 4 / 9.
3. **Positive homogeneity (absolute scalar)**: `nrm2(α·x) = |α|·nrm2(x)` for any scalar `α` (real or complex). The absolute value is necessary on both sign and complex phase; the norm strips both.
4. **Triangle inequality**: `nrm2(x + y) ≤ nrm2(x) + nrm2(y)`.
5. **Reverse triangle inequality**: `|nrm2(x) − nrm2(y)| ≤ nrm2(x − y)`. (Follows from law 4.)
6. **Cauchy–Schwarz** (relating `nrm2` to `inner_product`): `|inner_product(x, y)| ≤ nrm2(x) · nrm2(y)`, with equality iff `x` and `y` are linearly dependent (in exact arithmetic).
7. **Parallelogram identity**: `nrm2(x + y)² + nrm2(x − y)² = 2·nrm2(x)² + 2·nrm2(y)²`. (Characterizes norms induced by an inner product; holds here because `nrm2` is defined as `√⟨·,·⟩`.)
8. **Self-inner-product identity**: `nrm2(x)² = inner_product(x, x)` (real and complex) — the defining identity, restated. This is the structural link that makes `nrm2` a *consumer* of the `inner_product` fold; CG-style algorithms reuse `inner_product(r, r)` instead of recomputing `nrm2(r)²`.
9. **Zero in argument**: `nrm2(0) = 0`. (Special case of law 2.)
10. **Phase invariance (complex)**: for complex `x` and any unit-modulus complex scalar `e^{iθ}`: `nrm2(e^{iθ}·x) = nrm2(x)`. (Special case of law 3 with `|α| = 1`.)

Laws that explicitly **do not** hold (inherited unchanged from L1):

- **Linearity in `x`**: `nrm2(α·x + β·y) ≠ α·nrm2(x) + β·nrm2(y)` in general. `nrm2` is sub-additive (law 4), not additive. This is the defining feature that distinguishes a norm from a linear functional.
- **Strictness of Cauchy–Schwarz in floating point**: law 6 can fail by ULP-level amounts due to summation ordering inside the `inner_product` fold (same load-bearing caveat as the fold). Algorithms that depend on the strict inequality (e.g. orthogonality-loss detection in MGS reorthogonalization) must guard.
- **Bit-determinism across reduction trees**: same load-bearing caveat as the `inner_product` fold — different reduction orders produce different bit-level `nrm2` values. The mathematical laws above hold; their floating-point realizations are exact modulo summation-order noise.
- **`abs`-erasability**: the `std::abs` guard is NOT erasable in floating point without introducing a NaN failure mode on numerically-zero vectors — it is a no-op in exact arithmetic only. (See §Semantics; full classification at the L1>L0 theme.)
- **Multiplicativity over the cross-element kernel**: `nrm2(x ⊙ y) ≠ nrm2(x) · nrm2(y)` in general — not applicable; `nrm2` is a reduction-consumer, not a binary algebra on vectors.

## Dependencies

**Consumes (L2, NOT a parent fold)**: [`inner_product`](./inner_product.md) (firm cycle-019) — `nrm2(x) = √ (abs (inner_product(x, x)))`, the post-composition of two scalar maps (`abs`, `√`) onto the length-axis fold at `y = x`. This is a **consumer** relationship, not membership: `nrm2` is explicitly NOT a member of the fold cohort (do-NOT-merge boundary per [`L2/index`](./index.md) §"Fold-cohort boundary"; the [`inner_product`](./inner_product.md) dep-map row names `nrm2` as a consumer, not an instance). The `inner_product` fold is the **only** L2 dependency; the outer `abs` and `√` are scalar operations below the L2 layer's resolution (deterministic IEEE-754 primitives operating on the single scalar the fold produces).

The fact that `nrm2` factors so cleanly through `inner_product` is exactly the kind of compositional structure the L2 layer is meant to expose at the fusion-rotation level; the L0 form makes the composition syntactically explicit (one line of source at `palace/linalg/vector.hpp:259`), and the L2 form names it as the defining identity (algebraic law 8) with `nrm2` as a downstream consumer of the fold.

**Consumers (L2)**: [`krylov-step`](./krylov-step.md) — the per-step body consumes `nrm2` for the residual-norm readout (CG, MINRES convergence test) and the Arnoldi sub-diagonal scalar (GMRES basis-vector normalization, `H[j+1,j] = nrm2(w)`); the [`krylov-step`](./krylov-step.md) dep-map row lists `nrm2` among its L1 primitives, here rendered at the L2 floor.

**Cross-cutting concepts**: [`nrm2`](../concepts/nrm2.md) — the cross-cutting concept page with BLAS-1 heritage framing (its scaled-summation stability claim is incorrect per the L1 correction-pending note at `book/src/L1/nrm2.md:11`; the L1 entry is authoritative). [`dot`](../concepts/dot.md) — referenced transitively through the `inner_product` fold the defining identity consumes.

**L1 anchor**: [`L1/nrm2`](../L1/nrm2.md) (firm cycle-003) — authoritative on the Palace surface details, the one-line `linalg::Norml2` template definition, the relationship to the B-weighted overload (separately tracked), and the complete L0 evidence list. This L2 entry does not duplicate those details; the L2>L1 rotation is identity-in-form on the primitive itself.

## Variant axes

Inherited unchanged from L1 at **one** axis:

1. **element-type** (`real` | `complex`) — at L0 these are template specializations of `linalg::Norml2<VecType>` (`VecType ∈ {Vector, ComplexVector}`). At L1 / L2 / L3 these **collapse to a single operator** with the same signature `Tensor[N] -> Scalar(real)`, because the result is real-valued regardless of input element type (the Hermitian self-inner-product is real per `dot` law 4 / 9), and the defining identity `nrm2(x) = √ (abs (inner_product(x, x)))` is shared across element types; the element-type dispatch is entirely absorbed by the `inner_product` fold (and through it by `dot`).

This is a stronger collapse than `inner_product`'s element-type axis: `inner_product` retains an element-type-tracking return scalar (real `dot` → real, complex `dot` → complex); `nrm2` does not, because the post-composed `abs` projects the complex self-inner-product `{re, 0.0}` onto its real magnitude before `√`.

No other variant axes at L2:

- **B-weighting**: not a variant of `nrm2` — it is a distinct operator (the operator-weighted energy norm `‖x‖_B = √(xᴴ B x)`) consuming the M-weighted member of `inner_product` (`inner_product_M(x, M, x)`) rather than the plain fold. Tracked as [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) at L1 (rough-in cycle-010 wave-1). The L0 surface uses the same overloaded name `linalg::Norml2`, but the algebraic structure differs (requires an external `B`-application primitive, requires an SPD precondition on `B`, the workspace `Bx` is a load-bearing buffer at L0).
- **Stability variants**: BLAS-style scaled-summation `nrm2` (which avoids overflow/underflow at the cost of extra arithmetic) is **not present** in Palace's `linalg::Norml2` — Palace uses the naive `√⟨x, x⟩` form. Not a variant axis of the L2 operator.

## Status

`firm` — L2 form is value-thread-isomorphic to the L1 form (identity-in-form rotation); the fusion rotation is a no-op for this leaf (no HPC/SIMD trick to unfold — `linalg::Norml2` is already the one-line unfolded composition); algebraic laws inherited unchanged from L1; variant-axis profile inherited unchanged at one axis. The one genuinely-L2 content beyond identity is the fusion-rotation framing (`nrm2` as `√ ∘ abs ∘ inner_product` consumer of the fold, do-NOT-merge boundary honored) and the preservation of the `std::abs` load-bearing numerical guard as an explicit algebraic claim. The entry exists as a **layer-coherence floor** per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels** (cycle-009 codification) under the 2026-05-31 foundation-first directive `l2-floor-under-l3-leaf-cohort`: it gives the firm L3 [`nrm2`](../L3/nrm2.md) (cycle-011) a present adjacent L2 parent. Harvested cycle-041 wave-1 (D2) as part of the L2-floor-under-L3-BLAS1-cohort backfill.

## Lowers to

L2 `nrm2` lowers to L1 [`nrm2`](../L1/nrm2.md) as **identity-in-form on the primitive's signature**. The fusion rotation L2→L1 is a no-op on the buffer side (there is no destination buffer for `nrm2` — the result is a returned scalar; per [`L1-L0/nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) the "mutation rotation" is essentially nothing on the buffer side, and the fusion rotation likewise has no fused kernel to unfold). The L2>L1 rotation is a degenerate identity-in-named-terms lowering, recorded in-line in §"Downward to L1" below rather than as a thin theme file (per the 2026-06-01 vocabulary-shift redirect). The L1>L0 lowering — Palace's `linalg::Norml2` template at `palace/linalg/vector.hpp:255-260` expanding into the four-stage `Dot → MPI_Allreduce → std::abs → std::sqrt` chain — lives at [`L1-L0/nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md). None of that is L2 content; the L2 form sees a single-step fold consumed by two scalar maps.

### Downward to L1 (consumer identity-in-form; no theme file)

L2 `nrm2` re-fuses downward onto the single L1 leaf [`nrm2`](../L1/nrm2.md) (firm cycle-003) as **identity-in-form on the primitive's signature** — value-thread-isomorphic, with **no dispatch** (one L1 leaf — there is no L1 family to dispatch into, contrast the `dot`/`tdot` inner-product cohort), **no decomposition** (the L2 fusion rotation is a no-op — `linalg::Norml2` is already the one-line unfolded composition), and **no destination-buffer concern** (the result is a returned scalar). What the hop does is two surface adjustments, both value-preserving:

1. **The `inner_product` fold at `y = x` re-fuses to the `dot` leaf at the diagonal.** L2 names the inner reduction as the length-axis `inner_product` fold (firm cycle-019); at L1 the same diagonal self-inner-product is the `dot(x, x)` leaf (the defining identity `nrm2(x) = √dot(x, x)`, L1 algebraic law 8, `book/src/L1/nrm2.md:53`). This is the **consumer's** view of the edge [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md) §"The diagonal degeneration (`y = x`)" lowers for the fold itself — that theme names `nrm2` precisely as the consumer entry point (`√ ∘ inner_product` at `y = x`, with the outer `√` a post-step "downstream of this lowering, not a dispatch within it"). The inner `inner_product(x, x) → dot(x, x)` re-fusion is inherited from the inner-product theme; the `nrm2`-specific content is the outer `√ ∘ abs` post-step. **`nrm2` is a CONSUMER of `inner_product`, not a fold member** (do-NOT-merge per [`L2/inner_product`](./inner_product.md) §"Consumer (NOT an instance)" and §"Consumer of `inner_product`, NOT a fold member" above); the namesake "fold" is the one `nrm2` *consumes* at `y = x`, not one it instantiates.
2. **The two scalar post-steps change framing, not value.** At L2 the `abs` guard is **preserved as an explicit load-bearing numerical claim** and the `√` is the principal non-negative real square root composed onto the fold output. At L1 both drop **below the layer's resolution**: the `abs` guard **disappears**, subsumed by the L1 algebraic claim that `dot(x, x)` is non-negative real (so `abs` of it equals it exactly in exact arithmetic), and the `√` is a deterministic IEEE-754 scalar primitive on the leaf's output ([`L1/nrm2`](../L1/nrm2.md) §Dependencies, `:66`). Both treatments are consistent — the guard *implements* the non-negativity claim under floating point; it is a no-op in exact arithmetic and is **NOT erasable in floating point** without introducing a NaN failure mode on numerically-zero vectors. The full load-bearing-defensive classification (property bought = domain-safety / non-negativity invariant for `√`, no NaN) lives at [`L1-L0/nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) §"The `std::abs` defensive guard — classification", where the guard re-materializes as stage 3 of the four-stage `Dot → MPI_Allreduce → std::abs → std::sqrt` chain.

The mapping is total and trivial on the kernel content: the single L2 `nrm2` form maps to the single L1 `nrm2` leaf, same signature, same value, same defining identity (law 8). The element-type axis is collapsed identically at both layers (one operator, always-real result — the post-composed `abs` projects the complex self-inner-product onto its real magnitude before `√`). This is the **identity-in-form** property; the rotation is at the framing (preserved-`abs` fusion-rotation view at L2 → absorbed-`abs` mutation-rotation view at L1), not on the primitive.

L0 anchor (transitive through L1; verified on-disk this dispatch via `citecheck --anchor Norml2`): `palace/linalg/vector.hpp:255-260` — `linalg::Norml2` template; body line 259 is `return std::sqrt(std::abs(Dot(comm, x, x)));`. The one-line unfolded composition that makes the L2>L1 fusion rotation a no-op. (Path relative to `reference/palace/`; full L0 evidence at [`L1/nrm2`](../L1/nrm2.md) §Evidence.)

## Lifts from

L2 `nrm2` lifts from / to L3 [`nrm2`](../L3/nrm2.md) (firm cycle-011) as **identity-in-form**. L3 is the iteration-rotation layer; its `nrm2` is the same whole-tensor reduction with the iteration view of the *surrounding* consuming context (the [`krylov-step`](./krylov-step.md) body's residual-norm readout / Arnoldi sub-diagonal) rendered explicitly. The L3>L2 rotation on the primitive itself is identity-in-form, recorded in-line at the L3 entry's §"Downward to L2" note (no theme file per the 2026-06-01 vocabulary-shift redirect; structurally justified by [`L3-L2/krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md) §"Applicability conditions" point 3, which names `nrm2` among the seven primitives that are L2-native / L3-native because each signature has no per-element loop visible). `nrm2` has **no L4 entry** — leaf primitives are not first-class L4 vocabulary (per the cycle-010 audit verdict); at L4 it appears inside larger composed entries (e.g. `book/src/L4/krylov-step.md` §Semantics, `outputs.residual_norm`) as a let-binding consuming the L3-native primitive surface.

## Evidence

The L2 form is value-thread-isomorphic to the L1 form (identity-in-form on the primitive's signature); all L0 evidence is transitive through L1. Direct citations relevant to this L2 entry:

- [`book/src/L1/nrm2.md`](../L1/nrm2.md) (firm cycle-003) — authoritative on Palace surface, signature, algebraic laws (inherited unchanged at L2), variant axes (inherited unchanged at L2), the defining identity `nrm2(x) = √dot(x, x)`, the B-weighted-overload boundary, and the complete L0 evidence list.
- [`book/src/L1-L0/nrm2-mutation-rotation.md`](../L1-L0/nrm2-mutation-rotation.md) (firm) — the four-stage L0 chain `Dot → MPI_Allreduce → std::abs → std::sqrt` and the full `std::abs` defensive-guard classification (load-bearing-defensive; property bought = non-negativity invariant for the square root). The L2 entry preserves the guard as an explicit algebraic claim and cites this theme for the classification.
- [`book/src/L2/inner_product.md`](./inner_product.md) (firm cycle-019) — the fold `nrm2` consumes (`√ ∘ abs ∘ inner_product` at `y=x`); the do-NOT-merge boundary (`nrm2` is a consumer, not a member) is carried in this entry's dep-map row.
- [`book/src/L2/index.md`](./index.md) §"Fold-cohort boundary" + line 17 (L2 vocabulary inventory names `nrm2`) — the structural justification for the consumer-not-member framing and the L2-vocabulary home.
- [`book/src/L3/nrm2.md`](../L3/nrm2.md) (firm cycle-011) — the L3 consumer this floor sits under; frontmatter conventions and identity-in-form framing mirrored.
- [`book/src/L3-L2/krylov-step-body-identity.md`](../L3-L2/krylov-step-body-identity.md) §"Applicability conditions" point 3 (`:97`) — the load-bearing statement that the seven L1 primitives (including `nrm2`) are L2-native / L3-native by signature shape. The structural justification for the identity-in-form rotations on both adjacent edges.
- `palace/linalg/vector.hpp:255-260` — `linalg::Norml2` template definition: full body (line 259) is `return std::sqrt(std::abs(Dot(comm, x, x)));`. The single load-bearing line; the one-line unfolded composition that makes the L2 fusion rotation a no-op. (Path relative to `reference/palace/`; verified on-disk via `citecheck --anchor Norml2`.)
- `palace/linalg/vector.hpp:262-270` — `linalg::Normalize` template, which uses `Norml2` then asserts `norm > 0.0` and scales `x *= 1.0 / norm`. Confirms `nrm2` returns a positive real used as a divisor. (Path relative to `reference/palace/`; verified on-disk via `citecheck --anchor Normalize`.)
- [`book/src/concepts/nrm2.md`](../concepts/nrm2.md) — the cross-cutting concept page; BLAS-1 heritage framing. (Note: the concept page's stability claim ("Palace uses scaled summation") is incorrect per the L1 correction-pending note at `book/src/L1/nrm2.md:11`; the L1 entry is authoritative.)

## L2 vs L1 distinction

- **L1**: pure functional reduction `α = nrm2(x)`. Mutation-rotation layer — the L0 destination buffer is erased from the signature (there is none — the result is a returned scalar); the MPI collective is folded into the L1>L0 lowering; the `std::abs` guard disappears (subsumed by the algebraic non-negativity claim). The defining identity `nrm2(x) = √dot(x, x)` is stated as algebraic law 8.
- **L2**: fusion-rotation composition `α = nrm2(x)` written as `√ ∘ abs ∘ inner_product` at `y = x`. Fusion-rotation layer — HPC/SIMD tricks unfolded (none here; the L0 form is already unfolded), the `std::abs` load-bearing numerical guard **preserved as an explicit algebraic claim** (not erased as at L1), and `nrm2` framed as a **consumer of the `inner_product` fold** (do-NOT-merge: not a fold member). The signature is identical to L1; the rotation on the primitive is identity-in-form.

The two layers' entries are **value-thread-isomorphic** on the primitive itself. The L2 entry exists for layer-coherence — so the firm L3 [`nrm2`](../L3/nrm2.md) rests on a present adjacent L2 parent — per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels** and the 2026-05-31 `l2-floor-under-l3-leaf-cohort` directive.
