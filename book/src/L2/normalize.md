---
layer: L2
operator: normalize
firmness: firm
lowers_to:
  - book/src/L1/normalize.md (identity-in-form on the operator's signature — degenerate identity-in-named-terms, recorded as an in-line §"Downward to L1" note rather than a dedicated theme — see Lowers-to)
lifts_from:
  - book/src/L3/normalize.md (identity-in-form; L3 is the iteration-rotation view of the same fused composite — see Lifts-from)
consumes:
  - book/src/L2/nrm2.md (β = nrm2(x); the norm constituent — a CONSUMER-of inner_product, NOT a fold member)
  - book/src/L2/scal.md (û = scal(1/β, x); the rescale constituent — arity-1 member-of linear_combination, cited NOT merged)
variant_axes:
  - element-type (real / complex; collapsed to a single parameterised operator — norm output always real)
---

# normalize

Fused vector **normalize** rendered at L2 (the fusion-rotation layer): `normalize(x) = (β, x/β)` where `β = ‖x‖₂`. Consumes a tensor `x`; produces the pair `(β, û)` of its Euclidean norm `β` and its unit vector `û = x/β`, computing the norm once and reusing it as the rescale divisor. The fused `nrm2 + scal(1/nrm2, ·)` composite whose **returned norm** is load-bearing (Arnoldi Hessenberg sub-diagonal, spectral-radius eigenvalue estimate, NEP deflation companion-vector scale). Written at L2 as the named composition over the two firm same-layer floors [`nrm2`](./nrm2.md) and [`scal`](./scal.md) — with no genuine kernel fusion to un-fold (Palace's `linalg::Normalize` is already the one-line norm-then-rescale composition). Identity-in-form lowering to L1 [`normalize`](../L1/normalize.md); the entry exists primarily as a **layer-coherence floor** — present so the firm L3 [`normalize`](../L3/normalize.md) rests on an adjacent same-named L2 parent.

## Context

L2 is the **fusion-rotation** layer: each operation is written as a composition of base tensor / operator / quadrature primitives, with cache-blocked loops, SIMD intrinsics, packed formats, and batched specialized BLAS calls **unfolded back into the base algebras** (per [`L2/index`](./index.md) §Context). For `normalize` there is **no fusion trick to unfold** — Palace's `linalg::Normalize` (`palace/linalg/vector.hpp:262-270`) is a short free-function template whose body is already the base-algebra composition: `auto norm = Norml2(comm, x); MFEM_ASSERT(norm > 0.0, ...); x *= 1.0 / norm; return norm;`. The norm reduction (`Norml2`) and the rescale (`*= 1.0/norm`) are already two separate passes; there is no fused single-pass kernel (no blocked / SIMD / batched fusion of norm-and-rescale) to decompose. The L2 rendering therefore adds no buffer-side decomposition over the L1 form; it adds the **fusion-rotation framing** — naming `normalize` as the `nrm2 ∘ scal` *composition* in L2 vocabulary over the firm same-layer floors — and preserves the reduction-tree non-associativity (inherited from `nrm2`) as an explicit numerical claim.

This entry is a **thin layer-coherence floor** per the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, codified cycle-009 meta-phase). The L2 form is value-thread-isomorphic to the L1 form — the rotation L2→L1 is identity-in-form on the operator's signature; only the surrounding layer's framing differs (fusion-rotation view at L2 vs. mutation-rotation view at L1). The floor exists under the 2026-05-31 foundation-first directive (`l2-floor-under-l3-leaf-cohort`): the firm L3 [`normalize`](../L3/normalize.md) (cycle-039) must rest on a *present* adjacent L2 parent, not skip a layer down to L1. It is the **last genuine missing floor** of that directive's leaf cohort — the L3 entry's §"Downward to L1" + §"Lowers to" recorded "no interposed L2 entry" (`book/src/L3/normalize.md:27,131`); this floor supersedes that note (see §Open-questions in this report — the staleness is routed to the c044 sweep, not corrected here).

The L1 entry [`L1/normalize`](../L1/normalize.md) (firm cycle-027) is **authoritative on every factual claim about the Palace surface** — the `linalg::Normalize` free-function template, the three consumer shapes, the returned-norm load-bearing analysis, the `normalize_B` rough-in note, and the complete L0 evidence list. This L2 entry does not duplicate that material; it states the laws (which hold uniformly across L1 / L2 / L3 because the body is identity-in-form across the chain) and cites the L1 entry as the anchor.

### Fused composite over two floors, NOT a fold member (load-bearing)

`normalize` is a **fused composite** — it is to the firm L2 [`nrm2`](./nrm2.md) / [`scal`](./scal.md) floors what `axpy` is to `scal`/vector-add: a recognised composition that Palace ships as one symbol. The fusion is named because the **returned norm** is load-bearing — many call sites consume `β` *after* the rescale (a bare `scal(1/nrm2(x), x)` would discard it):

    normalize(x) = (nrm2(x), scal(1/nrm2(x), x))        -- the fused norm-then-rescale pairing

It is **fork-INDEPENDENT on fold-membership**, exactly like its norm constituent `nrm2`. Recall the L2 fold cohort (two reductions sharing a `foldl` skeleton — [`inner_product`](./inner_product.md) folds the length axis to a `Scalar`, [`linear_combination`](./linear_combination.md) folds the term axis to `Tensor[N]`; per [`L2/index`](./index.md) §"Fold cohorts"). `normalize` is **a member of neither**:

- It is not a length-axis reduction (it returns a `Tensor[N]` alongside the scalar — the unit vector — so its codomain is not `Scalar`).
- It is not a term-axis scalar-weighted-sum (the rescale `scal(1/β, x)` is a single-term scaling, but the *fused composite* with the norm output is not a `linear_combination` instance).

So `normalize` carries **NO fold-parent**. Its constituents have the fold relationships ([`nrm2`](./nrm2.md) is a *consumer-of* `inner_product`; [`scal`](./scal.md) is the *arity-1 member-of* `linear_combination`), but `normalize` itself, as a composite, is design-final on the **batch-12 leaf-vs-fold fork** (`dot-l2-leaf-floor-vs-fold-only-design`; [`L2/index`](./index.md) §Working-Notes): that fork can only ever re-anchor a *fold-parented leaf* into its fold-parent, and `normalize` has no fold-parent to fold into. Whatever the meta-phase decides about the `dot`/`scal`/`nrm2` leaf-floor realisation, this composite's floor stands unchanged — it cites its two constituent floors as *consumed* same-layer dependencies, never as a fold of which `normalize` is a member. This is the same fork-invariance the cycle-042 standalone-floor cohort (`reciprocal`/`elementwise_product`/`assemble-diagonal`/`jacobi-smoother`/`divfree-projector`) carries — `normalize` is in that design-final camp by virtue of being a composite-with-no-fold-parent, not a fold leaf.

The B-weighted sibling `normalize_B` (rescale by the energy norm `√(xᴴ B x)` for SPD `B`) is **not** part of this operator. Palace ships a fused B-weighted `Normalize(comm, x, B, Bx)` at `palace/linalg/operator.hpp:377-384` but it is **defined-but-uncalled** (zero 4-arg callsites), and its norm constituent [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) is `rough-in (test-coverage-bounded)`. Per the L1 entry's boundary documentation (`book/src/L1/normalize.md:83-95`), `normalize_B` is an L1 **rough-in note**, not a firm operator and not an L2 floor candidate. At L2 the same boundary holds: this entry is the unweighted Euclidean normalize.

## Signature

    normalize :: Tensor[N] -> (Scalar, Tensor[N])
    normalize x = (β, x/β)   where  β = nrm2 x,  β > 0

The L2 signature is identical to the L1 and L3 signatures; only the surrounding layer's framing differs.

Shape contract (bunsen-style, named axes; positional values, no monadic effect, no destination buffer):

- **`x`** — `Tensor[N]` — read-only whole-tensor argument (the *prior* value). Element type real or complex.
- **result.0** — `Scalar` — the norm `β = ‖x‖₂`. **Always real-valued and positive** (`β > 0`), regardless of `x`'s element type (inherited from [`nrm2`](./nrm2.md)'s real-valued-output collapse). The load-bearing returned scalar.
- **result.1** — `Tensor[N]` — the unit vector `û = x/β`, same axis `N` and same element type as `x`. Has unit norm: `nrm2(û) = 1` (in exact arithmetic).

**Precondition (partiality).** `normalize(x)` is defined only where `β > 0`, i.e. `x ≠ 0`. The L0 source asserts this directly (`MFEM_ASSERT(norm > 0.0, "Zero vector norm in normalization!")` at `palace/linalg/vector.hpp:267`). At L2 the operator is **partial** — undefined on the zero vector. This is the one applicability condition distinguishing it from the (total) `nrm2` and `scal` floors it composes; it is **not** a variant axis, a precondition on the input domain uniform across element types.

No element loop is exposed at L2 — the norm reduction over `i ∈ [0, N)` is the `nrm2` consumer's single semantic step, and the rescale is element-local; the fusion rotation erases any inner SIMD/blocked loop. This signature-shape property (no per-element loop visible) is what makes `normalize` a clean L2 composition over its two floors, exactly as it makes the seven BLAS-1 leaves L2-native / L3-native (per `book/src/L3-L2/krylov-step-body-identity.md:97`).

## Semantics

Fusion-rotation composition with defining identity: `normalize(x) = (nrm2(x), scal(1/nrm2(x), x))` — the norm is computed once, returned as `result.0`, and reused as the rescale divisor producing `result.1`. The fusion is the **single-evaluation pairing**, not a new arithmetic; both components are expressed over the firm L2 floors. At L2 the rendering names this composition explicitly; it does **not** un-fold a fused kernel (there is none — the L0 form already separates the norm pass from the rescale pass).

The norm sub-step `β = nrm2(x)` is the length-axis reduction `√ ∘ abs ∘ inner_product` at `y = x` (inherited from [`nrm2`](./nrm2.md) §Semantics — a *consumer* of the `inner_product` fold, with the `std::abs` defensive guard preserved as a load-bearing claim at the `nrm2` floor). The rescale sub-step `û = scal(1/β, x)` is **element-local** (every output element depends on one input element and the shared scalar `1/β`), **reduction-free**, and **rank-local** (inherited from [`scal`](./scal.md) §Semantics). Composed: `normalize` carries exactly one reduction (the norm) and one element-local map (the rescale), with no cross-element coupling beyond the norm reduction.

**Reduction-tree non-associativity is load-bearing**, inherited unchanged from the inner `nrm2` (hence from `dot` / `inner_product`). The rescale `scal(1/β, ·)` is element-local and adds no reduction; the square root and `abs` are deterministic IEEE-754 scalar operations. So `normalize`'s entire non-determinism is the norm fold's, and it is recorded as a non-law (see §Algebraic laws). The MPI collective is **not** in the L2 signature — single-rank is in scope per CLAUDE.md §Scope; the local-then-collective two-step reappears only in the L1>L0 lowering (at the `nrm2`/`inner_product`/`dot` leaf).

The reciprocal-then-multiply at L0 (`1.0 / norm` then `x *= …`, rather than a per-element divide) is the L0 form; at L2 it is the algebraic `x/β`, and any reciprocal-vs-divide bit-difference is an L1>L0 transparent-trick note (recorded as a non-law below), not an L2 sub-operator.

The **returned norm is the load-bearing output** — three consumer shapes recur (the reason the fusion is named rather than discarded):

- The norm is captured separately and the unit vector is the working result (GMRES Arnoldi: `β` becomes the Hessenberg sub-diagonal `H[j+1,j]`, the unit `w` extends the Krylov basis — `palace/linalg/iterative.cpp:631-632`).
- The norm is the working result and the unit vector carries the next iteration (spectral-radius power iteration: `l = Normalize(comm, u)` is the dominant-eigenvalue estimate, `u` is renormalised for the next `A·u` — `palace/linalg/operator.cpp:673`, convergence test at `:676`).
- The norm rescales a *companion* quantity as well as `x` (NEP deflation: the scale rescales both the basis vector `v` and its coordinate companion `v2 / scale` — `palace/linalg/nleps.cpp:610-611,617`).

The operator is **pure / out-of-place** at L2: it consumes the prior `x` and produces a fresh `(β, û)` pair with no destination buffer in the signature. The L0 receiver-mutating idiom (`x *= 1.0/norm`, the norm returned by value) is an L2>L1 (and onward L1>L0) lowering concern, captured by the lowering themes — not by the L2 algebra.

## Algebraic laws

The six laws that hold at L1 (per `book/src/L1/normalize.md` §"Algebraic laws") hold **unchanged** at L2, because the L2 form is value-thread-isomorphic to the L1 form. Inheritance is total: every L1 law holds at L2 with the same statement, and every L1 non-law remains a non-law at L2. They are reproduced here so the L2 reader does not have to reach to L1 for the listing. They hold for `x ≠ 0` (the operator's domain); the partiality is recorded once (above) and not re-stated per law. Write `normalize(x) = (β, û)` with `β = nrm2(x)` and `û = x/β`.

1. **Unit output**: `nrm2(û) = 1` (in exact arithmetic). The defining property — the second result has unit norm.
2. **Norm recovery**: `β = nrm2(x)`. The first result is exactly the input's norm; the projection `fst ∘ normalize = nrm2`.
3. **Reconstruction**: `scal(β, û) = x`, i.e. `β · (x/β) = x`. The pair `(β, û)` losslessly reconstructs `x` (the inverse of the [`scal`](./scal.md) law-8 round-trip with `α = 1/β`). This is why `normalize` is information-preserving where a bare unit-vector projection would not be.
4. **Positive homogeneity collapse (scale invariance of the unit vector)**: for any scalar `α ≠ 0`, `snd(normalize(scal(α, x))) = scal(α/|α|, û)`. For real positive `α`: `snd(normalize(scal(α, x))) = û` (the unit vector is invariant under positive rescaling of the input). For complex `α`: the unit vector picks up the phase `α/|α|`. Correspondingly `fst(normalize(scal(α, x))) = |α|·β` (positive homogeneity inherited from [`nrm2`](./nrm2.md) law 3).
5. **Idempotence of the unit vector (up to the trivial norm)**: `normalize(û) = (1, û)`. Normalising an already-unit vector returns norm `1` and the same vector. Equivalently `snd ∘ normalize ∘ snd ∘ normalize = snd ∘ normalize` (the unit-vector projection is idempotent) and `fst(normalize(snd(normalize(x)))) = 1`.
6. **Factorisation (the defining decomposition)**: `normalize(x) = (nrm2(x), scal(1/nrm2(x), x))`. This is the L2 statement of the fusion — both components in terms of the firm L2 [`nrm2`](./nrm2.md) and [`scal`](./scal.md) floors. It is the law a consumer or lowering theme rewrites against, and the structural justification for the `consumes` frontmatter (two same-layer dependencies, no fold-membership).

Laws that explicitly **do not** hold (inherited unchanged from L1):

- **Totality**: `normalize` is undefined at `x = 0` (`β = 0`, division by zero; the L0 `MFEM_ASSERT(norm > 0.0)` fires). Unlike `nrm2(0) = 0` and `scal(α, 0) = 0` (both total), the fused operator is **partial**. This is the single semantic addition of the fusion over its constituents, recorded as a precondition rather than a law that fails.
- **Additivity / linearity**: `normalize(x + y) ≠ (β_x + β_y, û_x + û_y)` in any form — the norm is sublinear (triangle inequality, from [`nrm2`](./nrm2.md) law 4) and the unit vector is a nonlinear (projective) function of the input. The operator is **not** linear in `x`; it is positively-homogeneous-of-degree-zero in the unit-vector component (law 4) and degree-one in the norm component.
- **Bit-level fusion equivalence**: the L0 reciprocal-then-multiply (`x *= 1.0/norm`) and an idealised per-element divide (`x[i] /= norm`) may differ at the bit level in IEEE-754. The reciprocal form is Palace's actual L0 (`vector.hpp:268`); pinning it is an L1>L0 transparent-trick note, not an L2 law — the algebraic value `x/β` is the same.
- **Bit-determinism across reduction trees**: the norm sub-step inherits `nrm2`'s load-bearing reduction-tree non-associativity — different reduction orders produce different bit-level `β` (hence different `û`). The mathematical laws above hold; their floating-point realisations are exact modulo summation-order noise.

The law set and non-law set are **inherited unchanged** from L1; the L2 rendering introduces no new laws or non-laws. This is what makes the L2>L1 hop identity-in-form on the operator's signature — not only the signature but the entire algebraic profile transports unchanged.

## Dependencies

**Consumes (L2, same-layer floors — `normalize` is a fused composite, NOT a leaf, NOT a fold member)**:

- [`nrm2`](./nrm2.md) (firm cycle-041 D2) — the norm reduction `β = √⟨x, x⟩` (result.0, and the rescale divisor). A *consumer-of* `inner_product` (`√ ∘ abs ∘ inner_product` at `y=x`), not a fold member; supplies the reduction-tree non-associativity `normalize` inherits and the `std::abs` load-bearing guard (recorded at the `nrm2` floor).
- [`scal`](./scal.md) (firm cycle-041 D3) — the rescale `û = scal(1/β, x)` (result.1). The arity-1 *member-of* `linear_combination` (cited NOT merged), element-local / reduction-free / rank-local; its law-8 round-trip (`scal(α⁻¹, scal(α, x)) = x`) is what makes `normalize` reconstruction-exact (law 3).

The factorisation `normalize(x) = (nrm2(x), scal(1/nrm2(x), x))` (law 6) is the complete L2-internal decomposition; these two floors are the **only** L2 dependencies. The reciprocal `1/β` is a scalar operation below the L2 layer's resolution (a deterministic IEEE-754 primitive on the single scalar the norm produces).

**Fold-relationship (fork-INDEPENDENT — load-bearing)**: `normalize` has **NO fold-parent**. It is neither a member/leaf of [`inner_product`](./inner_product.md) (its codomain is not `Scalar` — it returns the unit `Tensor[N]` alongside the norm) nor of [`linear_combination`](./linear_combination.md) (the fused norm-then-rescale composite is not a term-axis scalar-weighted-sum). Its *constituents* carry fold relationships, but the composite is design-final on the batch-12 leaf-vs-fold fork (`dot-l2-leaf-floor-vs-fold-only-design`, [`L2/index`](./index.md) §Working-Notes) — that fork can only re-anchor a fold-parented *leaf*, and `normalize` is a composite with no fold to fold into. This puts `normalize` in the same fork-invariant camp as the cycle-042 standalone-floor cohort (a different basis — composite-with-no-fold-parent rather than standalone-leaf-with-no-fold-parent — but the same design-final conclusion).

**Sibling / subsumption relationships (not dependencies)**:

- Bare `scal(1/nrm2(x), x)` (norm discarded) is the projection `snd ∘ normalize`. When a consumer needs only the unit vector and not the norm, the `scal ∘ nrm2` spelling is equivalent; `normalize` is preferred when the norm is consumed downstream (the load-bearing case that justifies naming the fusion). This is exactly the open question the [`scal`](./scal.md) §Dependencies "Sibling subsumption" note flagged (`book/src/L2/scal.md:223-228`) — `Normalize(x) = scal(1/nrm2(x), x)` paired with the returned norm; this entry closes it (the fused composite gets its own L2 floor).
- The B-weighted sibling `normalize_B` (rescale by `√(xᴴ B x)`) is an L1-entry **rough-in note**, NOT a firm operator and NOT an L2 candidate — the fused B-Normalize (`palace/linalg/operator.hpp:377-384`) is defined-but-uncalled and its norm constituent [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) is `rough-in (test-coverage-bounded)`. Tracked as plain text here, not a live link, since no L2 `normalize_B` chapter exists.

**Consumers (L2)** (cross-reference, not reverse-dependencies):

- [`krylov-step`](./krylov-step.md) — GMRES Arnoldi basis-normalisation `H[j+1,j] = nrm2(w); w ← scal(1/H[j+1,j], w)` (the inline two-output form of `normalize`; `palace/linalg/iterative.cpp:631-632`). The returned norm becomes the Hessenberg sub-diagonal.
- Spectral-radius power iteration — `l = Normalize(comm, u)` returns the dominant-eigenvalue estimate, `u` is renormalised for the next `A·u` (`palace/linalg/operator.cpp:673`, convergence test at `:676`).
- NEP deflation-basis growth — inline unweighted normalise rescaling both the basis vector and its coordinate companion (`palace/linalg/nleps.cpp:610-611,617`).
- Gram-Schmidt output-normalisation in [`orthogonalize`](./orthogonalize.md) — the `nrm2`/`scal` normalize step after orthogonalisation (FGMRES, ROM basis-extension).

**L1 anchor**: [`L1/normalize`](../L1/normalize.md) (firm cycle-027) — authoritative on the Palace surface details (the `linalg::Normalize` free-function template, the three consumer shapes, the returned-norm load-bearing analysis, the `normalize_B` rough-in note, the complete L0 evidence list). This L2 entry does not duplicate those details; the L2>L1 rotation is identity-in-form on the operator itself.

## Variant axes

Inherited unchanged from L1 at **one** axis:

- **element-type** (`real` | `complex`) — collapsed to a single parameterised operator at L2. The `linalg::Normalize` template is `VecType`-generic (real `mfem::Vector`, complex `ComplexVector`); the inner [`nrm2`](./nrm2.md) returns a real scalar in both cases (the norm output is **always real**), and the rescale [`scal`](./scal.md) dispatches to the matching element type (including the `imag(s)==0.0` real-into-complex promotion at the `scal` floor). At L2 these collapse to one operator parameterised by element type; the norm output is real-valued in all variants, the unit vector matches the input element type.

No other variant axes at L2 — `normalize` introduces none beyond its constituents', which both collapse to the single element-type axis. There is no constant-folding axis (the rescale scalar `1/β` is a runtime value, never `0`/`1`/`-1` by construction since `β > 0`); no reduction-order variant beyond `nrm2`'s inherited (load-bearing, non-axis) one. The only non-trivial semantic property relative to the floors is the **partiality** at `x = 0`, which is uniform across element types and recorded as a precondition, not an axis.

The variant-axis count matches the L1 and L3 entries exactly (one orthogonal axis: element-type). No new axes introduced by the L2 rendering; no axes merged or split.

## Status

`firm` — L2 form is value-thread-isomorphic to the L1 form (identity-in-form rotation); the fusion rotation is a **no-op on the buffer side** for this composite (no HPC/SIMD/batched kernel fuses the norm and rescale into one pass — `linalg::Normalize` is already the one-line norm-then-rescale composition, with the norm reduction and rescale already separate passes); algebraic laws (the six: unit output, norm recovery, reconstruction, positive-homogeneity collapse, unit-vector idempotence, factorisation) inherited unchanged from L1, and the non-law set (partiality / no-totality, nonlinearity, IEEE-754 bit-level fusion + reduction-tree caveats) likewise; variant-axis profile inherited unchanged at one axis (element-type).

**Firm-on-positive-structure** (the `apply_nonlinear_pencil` / `lu_solve` precedent, mirrored from the firm L1 and L3 entries): the signature matches `linalg::Normalize` exactly; the body is a read closure (`vector.hpp:262-270`), not a literature reconstruction; the six laws are syntactic identities on that positive source plus the inherited firm `nrm2` / `scal` algebra (themselves firm). The absence of a dedicated `test-normalize` does not gate the laws — they are operator-algebra identities, not convergence claims (the `apply_linop` / `reciprocal` firm-on-positive-structure situation, not the `eigsolve`-convergence-semantics situation; `normalize`'s laws carry no literature-inferred semantics). The one semantic addition over the floors — partiality at `x = 0` — is positively anchored by the L0 `MFEM_ASSERT(norm > 0.0)` at `vector.hpp:267`, recorded as a consumer-enforced precondition, not a status reduction.

The genuinely-L2 content beyond identity is **fusion-naming** (`normalize` as the `nrm2 ∘ scal` composition over its two firm same-layer floors, fork-INDEPENDENT on fold-membership — NO fold-parent, design-final on the batch-12 leaf-vs-fold fork) and the preservation of the inherited reduction-tree non-associativity as an explicit numerical claim. The B-weighted sibling `normalize_B` is **not** part of this firm claim (it is an L1-entry rough-in note, L1-promotion-gated via `matrix-weighted-norm`).

This dispatch is the **L2 floor backfill** (cycle-043 D9) under the foundation-first directive `l2-floor-under-l3-leaf-cohort`: the L2 form was previously referenced only as the fused `nrm2 + scal` construct inside [`scal`](./scal.md) §Dependencies (`book/src/L2/scal.md:223-228`) and the `orthogonalize` output-normalisation step; it now has its own L2 entry per **Identity-lowerings still require both L levels** — flooring the firm L3 [`normalize`](../L3/normalize.md) (cycle-039). It is the **last genuine missing floor** of the directive's leaf cohort.

## Downward to L1

L2 `normalize` lowers to L1 [`normalize`](../L1/normalize.md) as **identity-in-form on the operator's signature** — a **degenerate identity-in-named-terms lowering** with no vocabulary shift across the edge, recorded here as an **in-line note** rather than a dedicated `L2-L1/` theme chapter (the `normalize-leaf-identity` theme was demoted to this note under the 2026-06-01 VOCABULARY-SHIFT REDIRECT, cycle-050; CLAUDE.md §Methodology invariants ⟢). Both L1 and L2 see `normalize :: Tensor[N] -> (Scalar, Tensor[N])` with the same shape contract, the same six algebraic laws, the same non-law set (partiality at `x ≠ 0`, nonlinearity, IEEE-754 caveats), the same law-6 factorisation `normalize(x) = (nrm2(x), scal(1/nrm2(x), x))`, and the same single-orthogonal-axis variant profile (element-type). The fusion rotation L2→L1 is a **no-op on the buffer side** — there is no fused kernel to unfold (the norm and rescale are already separate passes at L0) and no destination buffer at L2 (the result is a returned pair); the two same-layer constituent floors (`nrm2` + `scal`) are cited unchanged across the edge, and `normalize` carries no fold-parent to defer fusion to (its codomain `(Scalar, Tensor[N])` is neither reduce-to-`Scalar` nor reduce-to-`Tensor[N]`). The operator is value-thread-isomorphic across the edge; only the surrounding layer's framing differs (fusion-rotation view at L2 vs. mutation-rotation view at L1).

The substantive rotation in the chain is the firm L1>L0 [`normalize-mutation-rotation`](../L1-L0/normalize-mutation-rotation.md) (cycle-027) — it lowers the L1 pure-functional `(β, û) = normalize(x)` into Palace's L0 in-place receiver-mutating `linalg::Normalize(comm, x)` (computing `norm = Norml2(comm, x)`, asserting `norm > 0`, rescaling `x *= 1.0/norm` in place, returning `norm` by value), composing the [`nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) no-buffer reduction with the [`scal-mutation-rotation`](../L1-L0/scal-mutation-rotation.md) sub-pattern A in-place rescale plus the returned-scalar binding. None of that is L2 content; the L2 form sees a single fused composition over its two floors — which is exactly why the L2>L1 edge needs no dedicated theme chapter.

## Lifts from

L2 `normalize` lifts from / to L3 [`normalize`](../L3/normalize.md) (firm cycle-039) as **identity-in-form**. L3 is the iteration-rotation layer; its `normalize` is the same fused whole-tensor composite with the iteration view of the *surrounding* consuming context (the Arnoldi basis-normalisation / power-iteration / deflation-basis-growth bodies) carried by the surrounding step kernel, not by `normalize` itself (its iteration view is degenerate — a fused leaf composite, not a step body). The L3>L2 rotation on the operator itself is identity-in-form; the firm L3 entry's §"Downward to L1" + §"Lowers to" (`book/src/L3/normalize.md:27,131`) currently record "no interposed L2 entry" — **this floor supersedes that note** (the staleness is routed to the c044 sweep; see this report's §Open-questions, not corrected here per one-operator-per-dispatch discipline).

`normalize` has **no L4 entry** — fused leaf composites are not first-class L4 vocabulary (the same `CONFIRMED-NOT-NEEDED` verdict the cycle-010 cross-layer audit reached for the BLAS-1 cohort, `apply_linop`, and `assemble-diagonal`: they carry no monadic effect, no state-stratification typing, no novel calculus content at L4). At L4 it appears (where consumed) inside larger composed entries as a let-binding feeding the Arnoldi / power-iteration / deflation chains; the rotation from any such L4 mention to this floor is the identity.

The L2 entry exists for **layer-coherence reasons** — a reader navigating L2 must find `normalize` defined in L2 vocabulary as the fused `nrm2 ∘ scal` composition over its two firm same-layer floors, not have to reach down to L1 to recover the field-operation shape, nor up to L3 to recover the composite framing.

## Evidence

The L2 form is value-thread-isomorphic to the L1 form (identity-in-form on the operator's signature); all L0 evidence is transitive through L1. Direct citations relevant to this L2 entry:

- `book/src/L1/normalize.md` (firm cycle-027 — firm-on-positive-structure) — the L1 form this L2 entry value-thread-mirrors: signature, semantics (the fused `nrm2 + scal` composite, the returned-norm load-bearing analysis), the six algebraic laws (inherited unchanged at L2), the single variant axis (element-type, inherited unchanged at L2), the partiality precondition (`x ≠ 0`), the `normalize_B` rough-in note, and the complete L0 evidence chain.
- `book/src/L3/normalize.md` (firm cycle-039) — the L3 consumer this floor sits under; identity-in-form framing and frontmatter conventions mirrored. Its §27/§131 "no interposed L2 entry" notes are superseded by this floor (routed to c044 sweep).
- `book/src/L2/nrm2.md` (firm cycle-041 D2) — the norm constituent floor (`β = nrm2(x)`); a consumer-of `inner_product`, supplying the reduction-tree non-associativity and the `std::abs` guard `normalize` inherits.
- `book/src/L2/scal.md` (firm cycle-041 D3) — the rescale constituent floor (`û = scal(1/β, x)`); the arity-1 member-of `linear_combination` whose law-8 round-trip makes `normalize` reconstruction-exact (law 3). Its §Dependencies sibling-subsumption note (`book/src/L2/scal.md:223-228`) flagged `Normalize(x) = scal(1/nrm2(x), x)` paired with the returned norm as an open question; this entry closes it.
- `book/src/L1-L0/normalize-mutation-rotation.md` (firm cycle-027) — the substantive L1>L0 rotation in the chain, which reintroduces the L0 in-place rescale, the returned-by-value norm, the reciprocal-then-multiply trick, and the MPI collective that this L2 entry abstracts away.
- `book/src/L2/index.md` §"Fold cohorts" + §"Working Notes" (the `dot-l2-leaf-floor-vs-fold-only-design` fork note) — the structural justification for the fork-INDEPENDENT (no-fold-parent, design-final) framing.

**L0 evidence (canonical anchors, self-verified on-disk via `tools/citecheck/citecheck.py --anchor`, 2026-06-01)**:

- `palace/linalg/vector.hpp:262-270` — `linalg::Normalize` template: `auto norm = Norml2(comm, x); MFEM_ASSERT(norm > 0.0, "Zero vector norm in normalization!"); x *= 1.0 / norm; return norm;`. The positive source site — `normalize` verbatim, returning the norm; comment line 262, template line 263, def line 264, body 266-269. The norm-then-rescale separation (line 266 reduction, line 268 rescale) is what makes the L2 fusion rotation a no-op (no fused single pass to unfold). **Self-verified** (`--anchor 'Normalize'` → 262/264; `--anchor 'MFEM_ASSERT'` → 267 the partiality precondition; `--anchor '1.0 / norm'` → 268 the rescale; `--anchor 'return norm'` → 269 the returned norm).
- `palace/linalg/vector.hpp:256-260` — `linalg::Norml2` template; body line 259 `return std::sqrt(std::abs(Dot(comm, x, x)));`. The norm constituent's source; the one-line unfolded `√ ∘ abs ∘ inner_product` composition the `nrm2` floor consumes. **Self-verified** (body `std::sqrt`/`std::abs`/`Dot` on line 259; comment line 255, template line 256, signature line 257).
- `palace/linalg/iterative.cpp:631-632` — GMRES Arnoldi: `Hj[j + 1] = linalg::Norml2(comm, w); w *= 1.0 / Hj[j + 1];` — the inline two-output form of `normalize`, the returned norm stored as the Hessenberg sub-diagonal AND used to normalise. **Self-verified** (`--anchor 'Hj[j + 1] = linalg::Norml2'` → 631; `--anchor '1.0 / Hj'` → 632).
- `palace/linalg/operator.cpp:673` — `l = Normalize(comm, u);` — power-iteration: the returned norm `l` IS the dominant-eigenvalue estimate (consumed by the convergence test at `:676`). **Self-verified** (`--anchor 'l = Normalize'` → 673; `--anchor 'res = std::abs(l - l0)'` → 676).
- `palace/linalg/nleps.cpp:610-611` — NEP deflation-basis growth: `const auto scale = linalg::Norml2(GetComm(), v); v *= 1.0 / scale;` — inline unweighted normalise; the returned norm `scale` reused at `:617` (`H.col(k).head(k) = v2 / scale;`) to rescale the coordinate companion. **Self-verified** (`--anchor 'Norml2(GetComm(), v)'` → 610; `--anchor 'v2 / scale'` → 617).
- *Negative anchor*: no dedicated `test-normalize` under `reference/palace/test/unit/`. Per the firm-on-positive-structure precedent (`apply_linop`, `reciprocal`, `elementwise_product`, the BLAS-1 floors), the firm judgement does not require a dedicated test — every law is a syntactic identity on the positive `linalg::Normalize` source closure plus the inherited firm `nrm2` / `scal` algebra. Behaviour is exercised indirectly through the integration coverage of the Arnoldi (`palace/linalg/iterative.cpp:631-632`), power-iteration (`palace/linalg/operator.cpp:673`), and deflation (`palace/linalg/nleps.cpp:610-611`) consumer sites, plus the by-hand `normalize` shape in `palace/test/unit/test-orthog.cpp:193,208` (real path, norm asserted then rescaled).

## L2 vs L1 distinction

- **L1**: mutation-lifted pure functional update. `(β, û) = normalize(x)`. Frames the operator as the pure-functional image of the L0 receiver-mutating `linalg::Normalize(comm, x)` free-function idiom; emphasises the *mutation rotation* against the source (the in-place rescale drop, the returned-by-value norm made first-class, the MPI collective folded into the lowering, the reciprocal-vs-divide trick).
- **L2**: fusion-rotation composition. `(β, û) = normalize(x)` written as `nrm2 ∘ scal` over the firm same-layer floors. Frames the operator as a fused composite in the fusion-rotation layer's base vocabulary — fork-INDEPENDENT on fold-membership (NO fold-parent); emphasises that there is **no kernel fusion to unfold** (the L0 form already separates the norm pass from the rescale pass — the only L2-genuine content is naming the composition), and that the reduction-tree non-associativity inherited from `nrm2` is preserved as an explicit numerical claim. The signature is identical to L1; the rotation on the operator is identity-in-form.

The two layers' entries are **value-thread-isomorphic** on the operator itself. The L2 entry exists for layer-coherence — so the firm L3 [`normalize`](../L3/normalize.md) rests on a present adjacent L2 parent — per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels** and the 2026-05-31 `l2-floor-under-l3-leaf-cohort` directive.
