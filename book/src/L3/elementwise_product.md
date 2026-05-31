---
layer: L3
operator: elementwise_product
firmness: firm
lowers_to:
  - book/src/L1/elementwise_product.md (identity-in-form on the primitive's signature; no L3-L2/L3-L1 theme — see Lowers-to)
lifts_from:
  - (none) — `elementwise_product` is a leaf binary field operation; no L4 entry exists (leaf primitives don't get L4 rows per the cycle-010 audit verdict; the Hadamard sibling of the BLAS-1 / `scal` leaf cohort, which is likewise L4-row-free)
variant_axes:
  - element-type (real | complex; collapsed to a single parameterised operator)
  - conjugation (sub-axis on the complex element-type: straight `a ⊙ b` | conjugate-first-operand `ā ⊙ b`)
---

# elementwise_product

Whole-tensor **Hadamard (elementwise) binary product** at L3: `result = a ⊙ b`, defined by `result[i] = a[i] · b[i]` for `i ∈ [0, N)`. The diagonal-operator-action field operation at the iteration-rotation layer — the per-call kernel of the diagonally-scaled-preconditioner cohort (`jacobi-smoother`, `chebyshev`, block-Jacobi) and the iteration-rotation rendering of the same Hadamard map that L1 [`elementwise_product`](../L1/elementwise_product.md) provides. A leaf field operation: two equally-shaped tensors in, one fresh tensor out, no element loop exposed at the layer's vocabulary.

## Context

L3 is the iteration-rotation layer: global tensor-field operations expressed as whole-tensor primitives with no element loop exposed at the layer's vocabulary, with sequential obstructions named explicitly per [`sequential-obstruction`](../concepts/sequential-obstruction.md). `elementwise_product` at L3 is the whole-tensor form of the Hadamard binary product — the same operator that L1 names as the "pure-functional binary operator" (replacing the L0 `Y[i] = D[i] · X[i]` output-arg-mutating `BaseDiagonalOperator::Mult` idiom), read at L3 as one of the whole-tensor field operations the layer composes into smoother / preconditioner bodies. Its signature `(a: Tensor[N], b: Tensor[N]) -> Tensor[N]` exposes no element loop — the per-element binary multiply is a single semantic step at L3 just as it is at L1.

`elementwise_product` is the **binary** field operation of the elementwise cohort, the vector-vector multiplication generalisation of the scalar-vector [`scal`](./scal.md) (`scal(α, x) = elementwise_product(broadcast(α, N), x)` — broadcast specialisation; see Algebraic laws). It is also the realisation of the **diagonal-operator action**: `apply_linop(DiagonalOperator(d), x) = elementwise_product(d, x)` (law 9), making it the operator-action sibling of the L3 [`apply_linop`](./apply_linop.md) on the diagonal-operator slice, and the apply kernel that the L3 [`jacobi-smoother`](./jacobi-smoother.md) gate (`y = op.dinv ⊙ x`) is *one call to*.

The relationship to the adjacent layers:

- **Upward** to L4: there is **no standalone L4 entry** for `elementwise_product`. It is a leaf binary field operation carrying no monadic effect, no state-stratification typing, no novel calculus content at L4 — the same `CONFIRMED-NOT-NEEDED` verdict the cycle-010 cross-layer audit reached for `apply_linop`, `assemble_diagonal`, and the BLAS-1 / `scal` cohort. At L4 it appears (where consumed) inside operator bodies as a let-binding feeding the diagonal-preconditioner-apply chain (e.g. the `dinv ⊙ x` step inside the smoother bodies), not as first-class L4 vocabulary. Per CLAUDE.md §Methodology invariants "Layers are defined high→low", the absence of an L4 entry is a deliberate scoping verdict, not a gap.

- **Downward** to L1: `elementwise_product` lowers to L1 [`elementwise_product`](../L1/elementwise_product.md) directly, with **no interposed L2 entry and no `L3-L2`/`L3-L1` theme file**. The rotation is **identity-in-form on the primitive's signature** — both L1 and L3 see `elementwise_product :: (Tensor[N], Tensor[N]) -> Tensor[N]` with the same shape contract, the same ten algebraic laws, the same non-law set (idempotence, multiplicative inverse, conjugate-variant commutativity), and the same variant-axis profile (one orthogonal element-type axis + one conjugation sub-axis on the complex side). The L2 layer hosts no standalone `elementwise_product` entry (it is referenced from L2 compositions — the `dinv ⊙ r` step of `chebyshev-iteration` — but does not get a standalone L2 entry when the rotation carries no algebraic novelty); the L3>L1 hop is therefore direct, mirroring the `apply_linop` / `assemble_diagonal` / `scal` L3>L1 discipline. The identity-in-form annotation lives in-line here, per the cycle-012 non-adjacent-identity convention (precedent: `apply_linop`, `assemble-diagonal`, `dot`, `scal`, `krylov-step`); no non-adjacent lowering directory is created. The substantive rotation in the chain is the L1>L0 [`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md) (sub-pattern B), which lowers the L1 pure-functional `y = a ⊙ b` into Palace's `forall_switch` per-element output-arg kernel `Y[i] = A[i] * B[i]`.

This L3 entry is the **layer-coherence anchor**: a reader navigating L3 (the iteration-rotation layer that composes whole-tensor primitives into smoother / solver bodies) can find `elementwise_product` here, in L3 vocabulary, without having to reach down to L1 to recover the field-operation shape. The backfill is the cycle-038 enactment of the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, cycle-009 meta-phase codification), on the cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit's **(A) identity-in-form** verdict (`book/src/L3/index.md:41`): "`elementwise_product` (Hadamard binary)" listed among the six (A) firm backfill candidates, four of which (`reciprocal`, `elementwise_product`, `normalize`, `divfree-projector`) remained after the cycle-037 `assemble-diagonal` + `jacobi-smoother` landings (`book/src/L3/index.md:53`).

A cross-cutting prose treatment lives at [`elementwise-product`](../concepts/elementwise-product.md) — covering Hadamard / pointwise-product background, the diagonal-operator-apply role, and the Palace mapping. The L3 entry here is the firm operator definition at the iteration-rotation layer; the concept page is the narrative.

## Signature

    elementwise_product :: (a: Tensor[N], b: Tensor[N]) -> Tensor[N]
    elementwise_product(a, b) = a ⊙ b

Shape contract (bunsen-style, named axes; positional values, no monadic effect, no destination buffer — the typing distinctions are deferred to the wrapper layers above):

- **`a`** — `Tensor[N]` — read-only at L3 (the L3 form is pure; the L0 in-place mutation is reintroduced only at the L1>L0 lowering).
- **`b`** — `Tensor[N]` — read-only, sharing the length axis `N` and element type with `a`.
- **result** — `Tensor[N]` — same axis `N` as the inputs; `result[i]` is the per-element product `a[i] · b[i]`. A fresh value (no L0 destination buffer mentioned at L3).

`a` and `b` must share the same length axis `N` and the same element type (both real or both complex). The element-type axis (real or complex) is parameterised; the L3 signature is uniform across it. The **conjugate variant** (complex element-type only) takes one operand to its conjugate before multiplying:

    elementwise_product_conj :: (a: ComplexTensor[N], b: ComplexTensor[N]) -> ComplexTensor[N]
    elementwise_product_conj(a, b) = ā ⊙ b

— modeled here, as at L1, as the same operator with a **conjugation variant axis** (see Variant axes) rather than as a separate primitive.

The L3 signature is **identical to the L1 signature** modulo notation; the rotation is identity-in-form. No L4 wrapper machinery is needed at L3: `elementwise_product` is a leaf binary field operation, not a step body, and the L4 monadic / typed-record / `readonly`-typing apparatus (which serves wrapper-bearing operators like `krylov-step`) does not apply to leaf primitives — the same discipline the L3 `scal` / `apply_linop` / `assemble-diagonal` entries record.

## Semantics

`elementwise_product(a, b)` at L3 is a single whole-tensor field operation: a value-threaded transformation `(a, b) -> result` where `result[i] = a[i] · b[i]` for every element index `i ∈ [0, N)`. The operator is **element-local** (every output element depends on exactly one input element from each of `a` and `b`), **reduction-free** (no cross-element communication), and **rank-local** (no MPI collective at any layer; ranks own disjoint slices of `N` and apply the multiplication independently).

At L3 the operator carries **no iteration view** — it is not a step body; the iteration-rotation layer composes whole-tensor primitives like `elementwise_product` into step bodies (e.g. the `dinv ⊙ x` apply inside the [`jacobi-smoother`](./jacobi-smoother.md) gate, or the `dinv ⊙ r` step inside the [`chebyshev`](./chebyshev.md) polynomial sweep). The whole-tensor field-operation framing is what the L3 index (`book/src/L3/index.md:12`) calls a "whole-tensor field operation" — the L3 vocabulary's primitive shape, with no element-loop exposed.

The operator is **pure at L3**: the prior `a`, the prior `b`, and the result are distinct values; the L0 source overwrites the in-place destination buffer (`Y[i] = D[i] · X[i]` real; six fused multiply-adds across `(YR, YI)` complex) via the L1>L0 lowering ([`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md) sub-pattern B). At L3 the relationship is purely algebraic.

In the **complex** element-type, the per-element multiply is the standard complex multiplication `(a_R + i·a_I)(b_R + i·b_I) = (a_R·b_R − a_I·b_I) + i·(a_I·b_R + a_R·b_I)` — exactly the six fused multiply-adds at the canonical complex site. In the **conjugate variant** (`MultHermitianTranspose`), the multiply is `(a_R − i·a_I)(b_R + i·b_I) = (a_R·b_R + a_I·b_I) + i·(−a_I·b_R + a_R·b_I)` — two sign flips on the cross-terms; algebraically `ā ⊙ b`. The two forms differ only in the sign of two cross-terms; the element-local, reduction-free, rank-local character is identical across both.

The body has **no structural sub-composition** — `elementwise_product` is a leaf primitive, so the L3 form does not decompose into other L3 primitives. The five primitive groups that a wrapper-bearing operator like `krylov-step` has (operator-apply, optional auxiliary, iterate-and-scalar update, output readout, counter increment) have no analog here: the body is one whole-tensor field operation.

Special algebraic cases — `a = 𝟙` (the all-ones vector — identity in `a`), `a = 𝟘` (zero in `a`), `a = −𝟙` (negation), `a = b` (squaring each element) — are not separate operators at L3. They are algebraic identities recorded in the laws below, inherited from L1. The L0 source has **no** constant-folding branches on the value of `a` or `b` — the canonical and consumer kernels are uniform per-element multiplies (`forall_switch` over `N` with the multiply lambda); the conjugation variant is a structural axis (which kernel template instantiation `Mult` vs. `MultHermitianTranspose`), not a value branch on `imag(a) == 0`.

### Iteration-rotation marker

L3 is the iteration-rotation layer, and `elementwise_product`'s iteration view is **degenerate**: it is a leaf binary field operation, not a step body, so the operator carries no iteration view of its own. It composes into step bodies (e.g. the Jacobi-smoother apply `y = dinv ⊙ x`, the Chebyshev inner `dinv ⊙ r`) where the surrounding step kernel carries the iteration view; the `elementwise_product` call site itself is a single whole-tensor field operation per step.

There is **no sequential obstruction** in `elementwise_product` — every output element is independent of every other element under the per-element multiplication; the operator is embarrassingly parallel and fully GPU-friendly (`forall_switch` over `N`, one multiply per element, no cross-element carry). This is the **sharpest-contrast** clean field operation against the L3 `partial-obstruction` operators ([`chebyshev`](./chebyshev.md), [`eigsolve`](./eigsolve.md)), whose bodies lift but whose loops do not: `elementwise_product` has no loop to obstruct. It is the apply kernel that gives the L3 `jacobi-smoother` its defining lightness — the thinnest constructed-operator gate is "one `elementwise_product`, no obstruction".

## Algebraic laws

The ten laws that hold at L1 (per `book/src/L1/elementwise_product.md:43` §"Algebraic laws") transport **unchanged** to L3, because the L3 form is value-thread-isomorphic to the L1 form. The rotation L3 → L1 is identity-in-form on the operator's body and signature, so the algebraic properties of pointwise multiplication (commutative ring under elementwise multiply, distributive over elementwise addition) plus the conjugation-involution rule on the complex-side variant transport without modification. Absences are deliberate and inherited. The laws are reproduced here so the L3 reader does not have to reach to L1 for the listing.

1. **Commutativity**: `elementwise_product(a, b) = elementwise_product(b, a)`. Inherited from element-wise scalar commutativity in the underlying field (`ℝ` or `ℂ`). The complex *non-conjugate* form is genuinely commutative; the **conjugate variant** is **not** (see non-laws).
2. **Associativity**: `elementwise_product(a, elementwise_product(b, c)) = elementwise_product(elementwise_product(a, b), c)`. Inherited from per-element associativity.
3. **Identity (all-ones)**: `elementwise_product(𝟙, x) = x` where `𝟙` is the all-ones vector of axis `N`. The neutral element of pointwise multiplication.
4. **Absorption (all-zeros)**: `elementwise_product(𝟘, x) = 𝟘` for any `x`, where `𝟘` is the zero vector of axis `N`. Element-wise `0 · x[i] = 0`.
5. **Distributivity over vector addition**: `elementwise_product(a, b + c) = elementwise_product(a, b) + elementwise_product(a, c)`. Linearity in the second argument; by commutativity (law 1) also in the first.
6. **Scalar absorption (compatibility with `scal`)**: `elementwise_product(scal(α, a), b) = scal(α, elementwise_product(a, b)) = elementwise_product(a, scal(α, b))` for any scalar `α`. The scalar passes freely between either operand and the outside.
7. **Subsumption of `scal` (broadcast specialisation)**: `scal(α, x) = elementwise_product(broadcast(α, N), x)`, where `broadcast(α, N)` is the all-`α` vector of length `N`. Stated as an algebraic identity, not a dep-map edge — both operators stay as L3 siblings (see Dependencies).
8. **Negation**: `elementwise_product(−𝟙, x) = −x`. (Special case of laws 3 + 5 + 6 with `α = −1`.)
9. **Diagonal-operator action (operator/data identity)**: for any vector `d ∈ Tensor[N]`, `apply_linop(DiagonalOperator(d), x) = elementwise_product(d, x)`. The **defining identity** of the operator-class realization — applying the diagonal-operator wrapped from `d` IS the elementwise product against `d`. This makes `elementwise_product` the operator/data sibling of the L3 [`apply_linop`](./apply_linop.md) on the diagonal-operator slice, and closes the `assemble_diagonal → reciprocal → elementwise_product → DiagonalOperator-apply` round-trip the diagonal preconditioners rely on (`Jacobi(A)·x = (1/diag(A)) ⊙ x`).
10. **Conjugation involution (conjugate variant only, complex element-type)**: `elementwise_product_conj(a, elementwise_product_conj(b, c)) = elementwise_product(elementwise_product(ā, b̄), c) = elementwise_product(¯(a ⊙ b), c)` — applying the conjugate variant twice conjugates the combined left operand. The conjugation is left-applied per call.

Laws that explicitly **do not** hold (inherited unchanged from L1):

- **Idempotence**: `elementwise_product(a, a) ≠ a` in general — the result is the elementwise square `a ⊙ a`, equal to `a` only when each `a[i]² = a[i]` (i.e. `a[i] ∈ {0, 1}` per element, the same idempotent scalars in `ℝ` and `ℂ`).
- **Inverse (multiplicative)**: there is no general two-sided inverse — `elementwise_product(a, b) = 𝟙` has the solution `b[i] = 1 / a[i]` only when **every** `a[i] ≠ 0`. The partial inverse is realised by composing with [`reciprocal`](./reciprocal.md) (the elementwise-inverse sibling): `elementwise_product(a, reciprocal(a)) = 𝟙` when `a` has no zero entries. This is the algebraic shape of the `assemble_diagonal → reciprocal → elementwise_product` preconditioner chain.
- **Commutativity of the conjugate variant**: `elementwise_product_conj(a, b) = ā ⊙ b ≠ b̄ ⊙ a = elementwise_product_conj(b, a)` in general — the conjugation always applies to the **first** argument, breaking the argument symmetry of the straight variant. Equal only when both operands are real (or one is real).
- **Distributivity over inner products**: not applicable at L3 — `elementwise_product` produces a tensor, not a scalar; the natural composition with `dot` (`dot(a, elementwise_product(b, c))`) is an L2 fold fact, not an L3 law of this primitive.
- **Bit-level equivalence under reduction reordering**: `elementwise_product` is reduction-free, so this non-law is *vacuous* for the primitive — there is no reduction tree to reorder; the per-element multiply is bit-deterministic. It surfaces only when `elementwise_product` is consumed by a reduction (`dot(d, elementwise_product(a, b))` inherits `dot`'s reduction-tree non-associativity).

The law set and non-law set are **inherited unchanged** from L1; the L3 rendering introduces no new laws or non-laws. This is what makes the L3>L1 hop identity-in-form on the primitive's signature: not only does the signature transport unchanged, the entire algebraic profile transports unchanged.

## Dependencies

**Same-layer (L3)**: none. `elementwise_product` is a **leaf binary field operation** at L3 just as it is at L1 — the Hadamard-product floor of the elementwise vocabulary. Its sub-operation is the per-element scalar multiplication of two operand vectors, below the L3 layer's resolution and visible only in the L1>L0 lowering.

**Sibling subsumption (not dependency)**:

- `scal(α, x) = elementwise_product(broadcast(α, N), x)` — `elementwise_product` strictly generalises [`scal`](./scal.md) (broadcast specialisation; law 7); both stay in the L3 dep-map as siblings, not a dependency chain. The L0 surfaces are distinct (`scal` is `Vector::operator*=(α)` on a scalar; `elementwise_product` is `BaseDiagonalOperator::Mult` over two vectors).
- `apply_linop(DiagonalOperator(d), x) = elementwise_product(d, x)` — law 9; `elementwise_product` is the realisation of the diagonal-operator action, the operator/data sibling of [`apply_linop`](./apply_linop.md). Both stay as L3 siblings: `apply_linop` is opaque-operator-and-vector-to-vector; `elementwise_product` is vector-and-vector-to-vector with no operator argument.
- [`reciprocal`](./reciprocal.md) (the elementwise self-map) composes with `elementwise_product` to form the `assemble_diagonal → reciprocal → elementwise_product` diagonal-preconditioner apply chain.

**Consumers (L3)** (cross-reference, not reverse-dependencies) — the diagonal-preconditioner-apply fan-out, transported to L3:

- [`jacobi-smoother`](./jacobi-smoother.md) (cycle-037 firm) — the apply body is **one** `elementwise_product`: `y = op.dinv ⊙ x = (ω·D⁻¹) ⊙ x`. The thinnest constructed-operator gate is *one call to this operator* (`book/src/L3/index.md:33`); `elementwise_product` is the kernel that gives that gate its defining lightness.
- [`chebyshev`](./chebyshev.md) (cycle-013 `partial-obstruction`) — the diagonally-scaled polynomial sweep uses `dinv ⊙ r` per inner step, realised through the same `BaseDiagonalOperator::Mult` canonical site.
- L2 [`chebyshev-iteration`](../L2/chebyshev-iteration.md) cites `elementwise-product` as "the diagonal-operator apply primitive at L2" — the L1>L2 lift direction; the L3 entry is the iteration-rotation rendering of that same primitive.

**L1 anchor**: [`L1/elementwise_product`](../L1/elementwise_product.md) (firm; cycle-019/032/036 chain) — authoritative on the Palace surface details (the canonical `BaseDiagonalOperator<OperType>::Mult` operator-action site, the `MultHermitianTranspose` conjugate variant, the `jacobi.cpp` inline consumer duplicate, the absence of any free-function `linalg::ElementwiseProduct` symbol), the ten algebraic laws, and the complete L0 evidence list. This L3 entry does not duplicate those details; the L3>L1 rotation is identity-in-form on the primitive itself.

**Cross-cutting concepts**:

- [`elementwise-product`](../concepts/elementwise-product.md) — the cross-cutting prose treatment (Hadamard / pointwise-product background, diagonal-operator-apply role, Palace mapping).
- [`variant-absorption`](../concepts/variant-absorption.md) — the framing for the element-type axis absorption at L3.

**Strawman reference**: `book/src/design/l4_calculus.md` is the L4/L3 conventions source; this L3 entry follows the strawman's Haskell `::` signature notation. `elementwise_product` does not get its own L4 entry (per the leaf-primitive / `CONFIRMED-NOT-NEEDED` verdict the cycle-010 audit reached for the BLAS-1 / `scal` / `apply_linop` cohort) — at L4 it appears inside operator bodies as a let-binding, not as first-class vocabulary.

## Variant axes

`elementwise_product` has **two variant axes at L3** — the same framing as L1 (`book/src/L1/elementwise_product.md` §"Variant axes"), transported unchanged: one orthogonal element-type axis plus one conjugation sub-axis on the complex side.

1. **element-type** (`real` | `complex`) — collapsed to a single parameterised operator at L3. The L0 source splits this into two parallel template specialisations (real `BaseDiagonalOperator<Operator>::Mult`, per-element single multiply `Y[i] = D[i] * X[i]`; complex `BaseDiagonalOperator<ComplexOperator>::Mult`, per-element six-multiply-add complex product). At L3 these collapse to one operator parameterised by element type — the per-element semantics is "multiplication in the underlying field"; the field is `ℝ` or `ℂ`. This is the canonical application of [`variant-absorption`](../concepts/variant-absorption.md).

2. **conjugation** (sub-axis on the complex element-type): `straight (a ⊙ b)` | `conjugate-first-operand (ā ⊙ b)`. The L0 source materialises the straight form as `Mult` and the conjugate form as `MultHermitianTranspose` (complex-only, two sign flips on the cross-terms). At L3 this is a structural variant axis (which call form), not a value branch — both forms are exhaustively defined per element. The real element-type does **not** carry this axis (real conjugation is identity; the L0 real `BaseDiagonalOperator::MultTranspose` aliases to `Mult` — `void MultTranspose(const VecType &x, VecType &y) const override { Mult(x, y); }` at `reference/palace/palace/linalg/operator.hpp:279`). The conjugate variant breaks commutativity (non-law) and changes the conjugation-involution law (law 10), but preserves associativity (in the bilinear sense), the all-ones identity, the all-zeros absorption, and distributivity over addition.

Non-axes (recorded for disambiguation, inherited from L1):

- **constant-folding on `a` or `b`**: **not** an axis — the L0 source has no constant-folding branches (unlike `axpy`'s `α == 1.0` fast path). The canonical and consumer per-element kernels are uniform multiplies (`forall_switch` over `N`). Constant-folding cases (`a = 𝟙`, `a = 𝟘`) are absorbed into the algebraic laws.
- **operator-action vs. free binary**: **not** an axis at L3 — the canonical L0 site is the operator-action form (`DiagonalOperator::Mult`), and Palace has no free-binary `linalg::ElementwiseProduct` symbol; but the L1/L3 abstraction lifts the kernel out of the operator-action wrapper into a free binary primitive on two equally-shaped vectors. The operator-action form is **recovered** algebraically by law 9, not as a variant.

The variant-axis profile (one orthogonal element-type axis + one conjugation sub-axis) matches the L1 entry exactly. **No new axes introduced by the L3 rendering; no axes merged or split; the orthogonal-plus-sub-axis framing is preserved.**

## Status

`firm` — value-threaded positional signature is the canonical iteration-rotation form for the Hadamard binary product (matching the `BaseDiagonalOperator::Mult` operator-action form, the `MultHermitianTranspose` conjugate variant on the complex side, and the inline `Apply` consumer duplicate at `jacobi.cpp`, with one element-type axis and a conjugation sub-axis on the complex side); algebraic laws are the same ten that hold at L1 (commutativity, associativity, all-ones identity, all-zeros absorption, distributivity, scalar absorption, broadcast-subsumption-of-`scal`, negation, diagonal-operator-action identity, conjugation involution); non-laws are catalogued explicitly (idempotence, multiplicative inverse, conjugate-variant commutativity, reduction-reordering vacuity); variant-axis profile is one orthogonal element-type axis + one conjugation sub-axis, inherited unchanged from L1.

**Firm-on-positive-structure** — the rotation is value-thread-isomorphic on a firm L1 home, and every law is a syntactic identity on fully-specified positive source (per-element multiply lambdas in `forall_switch` at the canonical `BaseDiagonalOperator::Mult` site + the `jacobi.cpp` consumer duplicate). The absent dedicated `test-elementwise-product` does not gate firm — the missing test does not gate syntactic-identity laws (the `apply_linop` / `assemble-diagonal` / `scal` firm-on-positive-structure situation, not the `eigsolve`-convergence-semantics situation). There is **no caveat** to record (unlike `assemble-diagonal`'s load-bearing exact-vs-approximate non-law) — the Hadamard product is exact per element across all representations.

The pattern is well-attested via the chain: L1 firm-up (the Hadamard binary primitive harvested with full L0 evidence: the canonical operator-action site, the conjugate variant, the consumer duplicate, the absent free-function symbol); cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit (`book/src/L3/index.md:40-45`) classified `elementwise_product` as an **(A) identity-in-form** backfill ("Hadamard binary", `book/src/L3/index.md:41`); cycle-037 landed the first two of the six (A) backfills (`assemble-diagonal`, `jacobi-smoother`), leaving `reciprocal`, `elementwise_product`, `normalize`, `divfree-projector` (`book/src/L3/index.md:53`). This dispatch (cycle-038) is the **layer-coherence backfill** for `elementwise_product` — the L3 form was previously implicit in the diagonal-preconditioner-apply chain consumed by the smoother bodies (the `dinv ⊙ x` of `jacobi-smoother`, the `dinv ⊙ r` of `chebyshev`); it now has its own L3 entry per the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, cycle-009 meta-phase codification).

## Lowers to

L3 `elementwise_product` lowers to L1 [`elementwise_product`](../L1/elementwise_product.md) as **identity-in-form on the primitive's signature** — **no interposed L2 entry, no `L3-L2`/`L3-L1` theme file**. Both L1 and L3 see `elementwise_product :: (Tensor[N], Tensor[N]) -> Tensor[N]` with the same shape contract, the same ten algebraic laws, the same non-law set, and the same variant-axis profile (one orthogonal element-type axis + one conjugation sub-axis). The L2 layer does not host an `elementwise_product` entry (mirroring the `apply_linop` / `assemble_diagonal` L2 verdict — primitives are referenced from L2 compositions like `chebyshev-iteration`'s `dinv ⊙ r` step but do not get standalone L2 entries when the rotation carries no algebraic novelty); the L3>L1 hop is therefore direct.

No `book/src/L3-L1/` directory exists in the artifact; per the cycle-010 `krylov-step`, cycle-011 BLAS-1 / `apply_linop`, and cycle-037 `assemble-diagonal` / `jacobi-smoother` precedents this entry captures the identity rotation **in-line** (per the cycle-012 meta-phase non-adjacent-identity convention — lowering directories are per-adjacent-edge only). The **substantive** rotation in the chain is the L1>L0 [`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md) (sub-pattern B) — it lowers the L1 pure-functional `y = a ⊙ b` into Palace's `forall_switch` per-element output-arg kernel (the destination buffer reintroduced, the real single-multiply `Y[i] = A[i] * B[i]` / the complex six-multiply-add / the conjugate two-sign-flip variant, the device dispatch). The L3>L1 hop is by contrast a layer-coherence rotation (each layer is coherent within itself), not an algebraic one.

**Practical reading**: an algorithm written at L3 that calls `elementwise_product` (e.g. the diagonal-preconditioner apply of a Jacobi or Chebyshev smoother body) is reading the L1 entry's algebraic content (laws, non-laws, signature) one layer down; the L3 entry's role is to anchor the primitive in the L3 vocabulary inventory of whole-tensor field operations.

## Lifts from

`elementwise_product` has **no L4 entry** — leaf binary field operations are not first-class L4 vocabulary (the same `CONFIRMED-NOT-NEEDED` verdict the cycle-010 cross-layer audit reached for `apply_linop`, `assemble_diagonal`, and the BLAS-1 / `scal` cohort: leaf primitives carry no monadic effect, no state-stratification typing, no novel calculus content at L4). At L4 it appears (where consumed) inside larger composed entries as a let-binding feeding the diagonal-preconditioner-apply chain; the rotation from any such L4 mention to this L3 entry is the identity (the primitive's signature does not change between layers — only the surrounding wrapper does, and `elementwise_product` carries no wrapper at L4 or L3).

**This L3 entry exists for layer-coherence reasons** — a reader navigating L3 must find `elementwise_product` defined in L3 vocabulary, not have to reach down to L1 to recover the Hadamard-binary field-operation shape. The cycle-011 `scal` L3 backfill (`book/src/L3/scal.md`) and the cycle-037 `jacobi-smoother` / `assemble-diagonal` L3 backfills are the structural precedents: identity-in-form rotation on the primitive's signature, leaf / constructed-operator-gate layer-coherence backfill, methodology invariant enacted. `elementwise_product` is the binary-Hadamard sibling of `scal` (its broadcast-generalisation) and the apply kernel of `jacobi-smoother`; this dispatch closes its L3 entry.

## Evidence

The L3 form is value-thread-isomorphic to the L1 form (identity-in-form on the primitive's signature); all L0 evidence is transitive through L1. Direct citations relevant to this L3 entry:

- `book/src/L1/elementwise_product.md` (firm) — the L1 entry whose signature, semantics, ten algebraic laws, variant axes (one orthogonal element-type axis + one conjugation sub-axis), and complete L0 evidence chain are transported unchanged to L3. The laws and non-laws cited above are reproduced from the L1 entry's §"Algebraic laws" (`book/src/L1/elementwise_product.md:43`); the `scal` broadcast-subsumption relationship from `book/src/L1/elementwise_product.md:41`; the firm-on-positive-structure rationale from `book/src/L1/elementwise_product.md:99`.
- `book/src/L3/scal.md` (cycle-011 firm) — the leaf-field-operation L3 backfill precedent; `elementwise_product` is the binary-Hadamard generalisation of `scal` (broadcast specialisation, law 7). The L3>L1 identity-in-form discipline, the no-L2-entry / no-theme-file rotation shape, and the variant-absorption framing are inherited from this sibling.
- `book/src/L3/apply_linop.md` (cycle-011 firm) — the opaque-operator-gate L3 backfill precedent; `elementwise_product` is the operator-action realisation `apply_linop(DiagonalOperator(d), x) = elementwise_product(d, x)` (law 9), the operator/data sibling on the diagonal-operator slice.
- `book/src/L3/jacobi-smoother.md` (cycle-037 firm) — the consumer whose apply body is *one* `elementwise_product` (`y = op.dinv ⊙ x`); the thinnest constructed-operator gate. The freshest L3 identity-row template precedent (along with `assemble-diagonal`).
- `book/src/L3/assemble-diagonal.md` (cycle-037 firm) — the freshest L3 identity-in-form template precedent; the operator-to-data sibling that opens the `assemble_diagonal → reciprocal → elementwise_product` diagonal-preconditioner chain `elementwise_product` closes.
- `book/src/L3/index.md:12` — the L3 vocabulary inventory ("Whole-tensor field operations — primitives that act on whole tensors with no element loop exposed at the layer's vocabulary, L3-native by signature shape"); `elementwise_product` is the Hadamard binary field operation this entry adds to the inventory.
- `book/src/L3/index.md:41` — the cycle-036 D2 cross-layer-cross-cutter L3-cohort-growth audit; lists `elementwise_product` ("Hadamard binary") among the six **(A) identity-in-form L3 backfill candidates**. `book/src/L3/index.md:53` — the cycle-037 status note recording that four of the six (A) backfills remain (`reciprocal`, `elementwise_product`, `normalize`, `divfree-projector`) after the `assemble-diagonal` + `jacobi-smoother` landings. This entry is the enactment of that verdict for `elementwise_product`.
- `book/src/L3-L2/krylov-step-body-identity.md:97` (cycle-009 firm) — the firm theme naming the L1 primitives as L3-native by signature shape ("each L1 primitive is *also* L3-native because its signature has no per-element loop visible"); the classification rationale this identity-in-form backfill relies on.

**Transitive L0 evidence (via the L1 entry; load-bearing citations re-verified on-disk for this dispatch, not duplicated in detail)**:

- `reference/palace/palace/linalg/operator.cpp:478-487` — `BaseDiagonalOperator<Operator>::Mult` real, the **canonical** elementwise-multiply site: `Y[i] = D[i] * X[i]` (single multiply per element) at `:486`. Direct witness of laws 1 (symmetric in `D` and `X`), 9 (operator-action identity), and the `forall_switch` device-uniform kernel.
- `reference/palace/palace/linalg/operator.cpp:489-507` — `BaseDiagonalOperator<ComplexOperator>::Mult` complex, the **canonical complex straight-multiply** site: six fused multiply-adds per element at `:504-505`. Witness of the complex element-type variant.
- `reference/palace/palace/linalg/operator.cpp:545-568` — `DiagonalOperatorHelper<…>::MultHermitianTranspose`, the **canonical conjugate-variant** site: two sign flips at `:564-565` realising `d̄ ⊙ x`. Witness of the conjugation sub-axis on the complex side.
- `reference/palace/palace/linalg/jacobi.cpp:30-39` — `Apply<Transpose=false>` real consumer-duplicate site: `Y[i] = DI[i] * X[i]` at `:38`, line-for-line identical to `reference/palace/palace/linalg/operator.cpp:486` (modulo rename `D` → `DI`). Cross-witness for the canonical real form; the kernel the L3 `jacobi-smoother` apply is one call to.
- `reference/palace/palace/linalg/jacobi.cpp:74-93` — `JacobiSmoother::SetOperator` setup chain (`op.AssembleDiagonal(dinv)`, `dinv.Reciprocal()`, `dinv *= omega`); confirms the `assemble_diagonal → reciprocal → elementwise_product` chain reaches `elementwise_product` last in `Mult`.
- No dedicated `test-elementwise-product` exists in `reference/palace/test/unit/` (search confirms, transitive through L1); the operator is exercised indirectly through the diagonal-preconditioner consumer chain. Per the `firm-on-positive-structure` precedent, the absent dedicated test does not gate firm.

## L3 vs L4 distinction

- **L4**: no standalone `elementwise_product` entry. The primitive appears (where consumed) inside L4 operator entries as a let-binding within a do-block (e.g. the `dinv ⊙ x` step of a smoother body), carrying no monadic effect of its own. The surrounding wrapper (the do-block, the typed records, the `readonly` typing) is what makes the consuming entry L4-distinct — not the `elementwise_product` call itself.
- **L3**: standalone entry (this file). Positional value-threading: `elementwise_product(a, b) = a ⊙ b`. No monadic effect, no typed records, no `readonly` typing, no do-block. The primitive's signature is the L4 let-binding's RHS type, lifted out of any monadic context.

## L3 vs L1 distinction

- **L1**: pure-functional binary operator; the mutation rotation has happened (the L0 destination buffer has been dropped from the signature, along with the operator-class wrapping at the canonical site and the consumer-local inline duplication at `jacobi.cpp`); the element-type axis carries the conjugation sub-axis on the complex side. The L1 vocabulary frames the operator as the *mutation-rotation* image of the L0 `BaseDiagonalOperator::Mult` output-arg-mutating idiom.
- **L3**: whole-tensor field operation; one of the binary field operations the iteration-rotation layer composes into smoother / preconditioner bodies (the diagonal-operator apply, the `jacobi-smoother` apply kernel, the `chebyshev` inner `dinv ⊙ r`). **The primitive's signature is identity-in-form to L1** — no change in shape, no change in algebraic laws, no change in variant axes. The L3 entry exists for layer-coherence: a reader at L3 finds the primitive defined in L3 vocabulary without having to drop down to L1.

The two layers' entries are **value-thread-isomorphic** on the primitive itself, sharing signature, algebraic laws (ten), non-laws (idempotence, multiplicative inverse, conjugate-variant commutativity, reduction-reordering vacuity), variant-axis profile (one orthogonal + one sub-axis), and the cited L0 evidence (transitive). They differ in **layer interpretation**: L1 frames the primitive as the mutation-rotated form of the L0 `BaseDiagonalOperator::Mult` operator-action idiom; L3 frames it as one of the whole-tensor field operations the iteration-rotation layer enumerates as canonical vocabulary. The two framings are complementary — they read the same primitive from different layer roles — and the layer-coherence invariant (CLAUDE.md §Methodology invariants "Identity-lowerings still require both L levels") requires both entries to exist.
