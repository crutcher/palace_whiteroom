---
layer: L2
operator: elementwise_product
firmness: firm
lowers_to:
  - book/src/L1/elementwise_product.md (identity-in-form on the primitive's signature; degenerate identity-in-named-terms edge — recorded in-line below at "Lowers to" per the 2026-06-01 vocabulary-shift redirect, no dedicated L2>L1 theme; leaf binary field operation, no multi-operation kernel fusion to unfold; substantive rotation deferred to the L1>L0 `reciprocal-elementwise-product-mutation-rotation` sub-pattern B)
lifts_from:
  - book/src/L1/elementwise_product.md (value-thread-isomorphic; same signature shape; whole-tensor leaf binary field operation, no kernel fusion to unfold)
fold_parent:
  - (none) — `elementwise_product` is a standalone binary field operation, NOT a member/leaf of either L2 fold cohort (`inner_product` reduces to `Scalar`; `linear_combination` folds the term axis). Fork-INDEPENDENT.
variant_axes:
  - element-type (real / complex; collapsed to a single parameterised operator)
  - conjugation (sub-axis on the complex element-type: straight `a ⊙ b` | conjugate-first-operand `ā ⊙ b`)
---

# elementwise_product

Whole-tensor **Hadamard (elementwise) binary product** as a base tensor-algebra
primitive at L2 — the **fusion-rotation** rendering of `result = a ⊙ b`, defined by
`result[idx] = a[idx] · b[idx]` for every multi-index `idx` of `S`. Consumes two congruent tensors `a` and
`b`; produces a fresh tensor of the same shape whose every element is the per-element
product of the corresponding input elements. `elementwise_product` is a **standalone
binary field operation** at L2 — the diagonal-operator-apply primitive and the per-call
kernel of the diagonally-scaled-preconditioner cohort (`jacobi-smoother`, Chebyshev
smoother, block-Jacobi). It is **fork-INDEPENDENT — it has NO fold-parent**: unlike the
cycle-041 BLAS-1 floor leaves (`dot` leaf-of [`inner_product`](./inner_product.md), `scal`
member-of [`linear_combination`](./linear_combination.md)), the Hadamard binary product is
not a member or leaf of either L2 fold cohort. Companion to L1
[`elementwise_product`](../L1/elementwise_product.md) (the mutation-lifted form of the same
primitive) and L3 [`elementwise_product`](../L3/elementwise_product.md) (the
iteration-rotation rendering, cycle-038); the rotation L1 ↔ L2 is identity-in-form because
`elementwise_product` is a leaf binary field operation with no multi-operation kernel
fusion to unfold.

## Context

L2 is the fusion-rotation layer (`book/src/L2/index.md`): "Kernel fusion across multiple
algebraic operations is unfolded into composition… Batched specialized BLAS calls are
written as compositions of base primitives." `elementwise_product` at L2 is the base
Hadamard-binary-multiply primitive in that vocabulary — a single binary field operation
acting pointwise over the shared shape group `S` (arbitrary, unknown rank). It is the L2 rendering of the same
operation the concept page [`elementwise-product`](../concepts/elementwise-product.md)
names "the diagonal-operator apply primitive at L2": applying a diagonal operator `D` to a
vector `x` is `elementwise_product(diag(D), x)`.

**`elementwise_product` is fork-INDEPENDENT — it has NO fold-parent.** This is the
structural difference from the cycle-041 BLAS-1 floor cohort and the load-bearing reason it
is *not* on the batch-12 meta-phase leaf-vs-fold design fork. The two L2 fold cohorts
(`book/src/L2/index.md` §"Fold cohorts") are:

- [`inner_product`](./inner_product.md) — folds the **length axis** to a `Scalar`
  (`foldl (+) zero (zipWith kernel x y)`); the `dot` / `tdot` / `bilinear-form` family.
- [`linear_combination`](./linear_combination.md) — folds the **term axis**, keeping
  `Tensor[$S]` (`foldl (\acc (a,t) -> acc + a·t) zeros pairs`); the
  `scal` / `axpy` / `axpby` / `axpbypcz` arity family.

`elementwise_product` is **neither**: it is a binary field operation
`(Tensor[(S: ...)], Tensor[$S]) -> Tensor[$S]` that consumes two congruent operands and produces a
congruent result, with no fold skeleton (no reduction to a scalar, no variadic term list
to accumulate). It does not fuse *up* into either cohort, and neither cohort subsumes it.
The closest relationship is the **inverse** subsumption with `scal`:
`scal(α, x) = elementwise_product(broadcast(α, S), x)` — `elementwise_product` strictly
*generalises* `scal`'s scalar-multiplication action to a vector-multiplication action (the
broadcast specialisation; see Algebraic laws law 7). That is a sibling-subsumption identity,
not a fold membership. So `elementwise_product` stands alone as a standalone L2 leaf — there
is no `do-NOT-merge` fold boundary to police for this entry, because there is no fold to
merge it into.

This is a thin **floor presence** entry. It exists so the firm L3
[`elementwise_product`](../L3/elementwise_product.md) (cycle-038) rests on a present
adjacent L2 parent, per the methodology invariant **Identity-lowerings still require both L
levels** (CLAUDE.md §Methodology invariants, cycle-009 codification): each layer is coherent
within itself, and a reader at L2 must find `elementwise_product` defined in L2 vocabulary
without reaching down to L1 or up to L3. The foundation-first directive
`l2-floor-under-l3-leaf-cohort` (2026-05-31) names exactly this gap: the L3 cohort was
backfilled to L3 in cycle-011/038 without the corresponding L2 floor entries being present,
so the L3 leaves rested on the L1 leaves directly. This dispatch floors
`elementwise_product` as the **standalone (fork-independent) member** of that floor batch.

A cross-cutting prose treatment lives at
[`elementwise-product`](../concepts/elementwise-product.md) — covering Hadamard /
pointwise-product background, the diagonal-operator-apply role, and the Palace mapping
(`mfem::Vector` component-wise operators; the Jacobi / Chebyshev precomputed-diagonal
reciprocal pattern). The L2 entry here is the firm operator definition at the
fusion-rotation layer; the concept page is the narrative.

## Signature

    elementwise_product :: (a: Tensor[(S: ...)], b: Tensor[$S]) -> Tensor[$S]
    elementwise_product(a, b) = a ⊙ b

Shape contract (bunsen-style; named shape groups per [`l4_calculus`](../semantics/index.md)
§1.2.1; positional values, no monadic effect, no destination buffer):

- **`a`** — `Tensor[(S: ...)]` — read-only at L2 (the L2 form is pure / out-of-place; the L0
  in-place mutation is reintroduced only at the L1>L0 lowering). Its whole shape is the group
  `S` (arbitrary, unknown rank).
- **`b`** — `Tensor[$S]` — read-only, congruent to `a` (same shape group `S`) and sharing its element type.
- **result** — `Tensor[$S]` — congruent to the inputs; `result[idx]` is the per-element
  product `a[idx] · b[idx]`. A fresh value (no L0 destination buffer mentioned at L2).

`a` and `b` must be congruent (same shape group `S`) and share the same element type (both real or
both complex). The element-type axis (real or complex) is parameterised; the L2 signature
is uniform across it. The **conjugate variant** (complex element-type only) takes one
operand to its conjugate before multiplying:

    elementwise_product_conj :: (a: ComplexTensor[(S: ...)], b: ComplexTensor[$S]) -> ComplexTensor[$S]
    elementwise_product_conj(a, b) = ā ⊙ b

— modeled here, as at L1 and L3, as the same operator with a **conjugation variant axis**
(see Variant axes) rather than as a separate primitive.

The L2 signature is **congruent to the L1 signature** modulo notation (L1 spells the flat dof-vector as `Tensor[N]`; L2 states the rank-generic congruence as the group `S`); the rotation is
identity-in-form. `elementwise_product` is a leaf binary field operation, not a fold
member: there is no `[(Scalar, Tensor[$S])]` term-list argument (contrast
`linear_combination`) and no reduction to a `Scalar` (contrast `inner_product`). The
operator-action recovery `apply_linop(DiagonalOperator(d), x) = elementwise_product(d, x)`
(law 9) is a derived identity, not a decomposition.

## Semantics

`elementwise_product` at L2 is a single base tensor-algebra binary field operation: a
value-threaded transformation `(a, b) -> result` where `result[idx] = a[idx] · b[idx]` for every
multi-index `idx` of `S`. The operator is **element-local** (every output element depends
on exactly one input element from each of `a` and `b`), **reduction-free** (no cross-element
communication — the structural opposite of `dot` / `inner_product`, which reduce over `S`),
and **rank-local** (no MPI collective at any layer; ranks own disjoint slices of `S` and
apply the multiplication independently — contrast `dot` / `nrm2`, which reduce over `N` and
do carry an MPI collective).

It is **pure / out-of-place** at L2: it consumes the prior values of `a` and `b` and
produces a fresh tensor; no destination buffer appears in the signature. The L0 in-place
output-mutating idiom (`Y[i] = D[i] · X[i]` writing through the output vector argument of
`BaseDiagonalOperator::Mult`) is an L2>L1 (and onward L1>L0) lowering concern, captured by
the output-aliasing direction of the lowering themes — not by the L2 algebra.

**Leaf, with no kernel fusion to unfold.** L2 is the layer where kernel fusion across
multiple algebraic operations is unfolded into composition. `elementwise_product` is a
**leaf** in that vocabulary — there is no multi-operation fusion to unfold (it is a single
per-element binary multiply, not a fused `α·x + β·y` linear-combination pass or a fused
`reduce ∘ map` reduction). The L0 source materialises it as one uniform
`mfem::forall_switch` strided pass over `N` applying the multiply lambda per element
(real `Y[i] = D[i] * X[i]`; complex six fused multiply-adds; conjugate variant two
sign-flips) — which **is already** the unfolded single-pass form. There is no fusion note
to carry beyond that observation: unlike `dot` (which defers a family of fused reduction
kernels to the `inner_product` fold-parent) and unlike `scal` (which carries the degenerate
arity-1 case of the `linear_combination` fold's fusion note), `elementwise_product` has no
fold-parent and so no fold-level fusion content to defer. The single per-element multiply
pass is the base primitive's own implementation, recorded as this one note.

Special algebraic cases — `a = 𝟙` (the all-ones vector — identity in `a`), `a = 𝟘`
(zero in `a`), `a = −𝟙` (negation), `a = b` (squaring each element) — are not separate
operators at L2. They are algebraic identities recorded in the laws below, inherited from
L1. The L0 source has **no** constant-folding branches on the value of `a` or `b` — the
canonical and consumer kernels are uniform per-element multiplies (`forall_switch` over
`N` with the multiply lambda); the conjugation variant is a structural axis (which kernel
template instantiation `Mult` vs. `MultHermitianTranspose`), not a value branch on
`imag(a) == 0`.

In the **complex** element-type, the per-element multiply is the standard complex
multiplication `(a_R + i·a_I)(b_R + i·b_I) = (a_R·b_R − a_I·b_I) + i·(a_I·b_R + a_R·b_I)` —
the six fused multiply-adds at the canonical complex site. In the **conjugate variant**
(`MultHermitianTranspose`), the multiply is
`(a_R − i·a_I)(b_R + i·b_I) = (a_R·b_R + a_I·b_I) + i·(−a_I·b_R + a_R·b_I)` — two sign flips
on the cross-terms; algebraically `ā ⊙ b`. The two forms differ only in the sign of two
cross-terms; the element-local, reduction-free, rank-local character is identical across
both.

## Algebraic laws

The ten laws that hold at L1 (per `book/src/L1/elementwise_product.md` §"Algebraic laws")
and unchanged at L3 hold unchanged at L2. The rotation L2 ↔ L1 is identity-in-form on the
operator's body and signature, so the algebraic properties of pointwise multiplication
(commutative ring under elementwise multiply, distributive over elementwise addition) plus
the conjugation-involution rule on the complex-side variant transport without modification.
Absences are deliberate and inherited. The laws are reproduced so the L2 reader does not
have to reach to L1.

1. **Commutativity**: `elementwise_product(a, b) = elementwise_product(b, a)`. Inherited
   from element-wise scalar commutativity in the underlying field (`ℝ` or `ℂ`). The complex
   *non-conjugate* form is genuinely commutative; the **conjugate variant** is **not** (see
   non-laws).
2. **Associativity**:
   `elementwise_product(a, elementwise_product(b, c)) = elementwise_product(elementwise_product(a, b), c)`.
   Inherited from per-element associativity.
3. **Identity (all-ones)**: `elementwise_product(𝟙, x) = x` where `𝟙` is the all-ones
   tensor of shape group `S`. The neutral element of pointwise multiplication.
4. **Absorption (all-zeros)**: `elementwise_product(𝟘, x) = 𝟘` for any `x`, where `𝟘` is
   the zero tensor of shape group `S`. Element-wise `0 · x[idx] = 0`.
5. **Distributivity over vector addition**:
   `elementwise_product(a, b + c) = elementwise_product(a, b) + elementwise_product(a, c)`.
   Linearity in the second argument; by commutativity (law 1) also in the first.
6. **Scalar absorption (compatibility with `scal`)**:
   `elementwise_product(scal(α, a), b) = scal(α, elementwise_product(a, b)) = elementwise_product(a, scal(α, b))`
   for any scalar `α`. The scalar passes freely between either operand and the outside.
7. **Subsumption of `scal` (broadcast specialisation; the inverse-fork relationship)**:
   `scal(α, x) = elementwise_product(broadcast(α, S), x)`, where `broadcast(α, S)` is the
   all-`α` tensor of shape group `S`. Stated as an algebraic identity, not a dep-map edge or a
   fold-membership — `elementwise_product` strictly *generalises* `scal`, the inverse of
   `scal`'s membership in `linear_combination`. Both stay as L2 siblings.
8. **Negation**: `elementwise_product(−𝟙, x) = −x`. (Special case of laws 3 + 5 + 6 with
   `α = −1`.)
9. **Diagonal-operator action (operator/data identity)**: for any tensor
   `d ∈ Tensor[(S: ...)]`, `apply_linop(DiagonalOperator(d), x) = elementwise_product(d, x)`. The
   **defining identity** of the operator-class realization — applying the diagonal-operator
   wrapped from `d` IS the elementwise product against `d`. This makes `elementwise_product`
   the operator/data sibling of the L1 [`apply_linop`](../L1/apply_linop.md) on the
   diagonal-operator slice, and closes the
   `assemble_diagonal → reciprocal → elementwise_product → DiagonalOperator-apply` round-trip
   the diagonal preconditioners rely on (`Jacobi(A)·x = (1/diag(A)) ⊙ x`).
10. **Conjugation involution (conjugate variant only, complex element-type)**:
    `elementwise_product_conj(a, elementwise_product_conj(b, c)) = elementwise_product(elementwise_product(ā, b̄), c) = elementwise_product(¯(a ⊙ b), c)`
    — applying the conjugate variant twice conjugates the combined left operand. The
    conjugation is left-applied per call.

Laws that explicitly **do not** hold (inherited unchanged from L1):

- **Idempotence**: `elementwise_product(a, a) ≠ a` in general — the result is the
  elementwise square `a ⊙ a`, equal to `a` only when each `a[idx]² = a[idx]` (i.e.
  `a[idx] ∈ {0, 1}` per position, the same idempotent scalars in `ℝ` and `ℂ`).
- **Inverse (multiplicative)**: there is no general two-sided inverse —
  `elementwise_product(a, b) = 𝟙` has the solution `b[idx] = 1 / a[idx]` only when **every**
  `a[idx] ≠ 0`. The partial inverse is realised by composing with `reciprocal` (the
  elementwise-inverse sibling, firm L1/L3):
  `elementwise_product(a, reciprocal(a)) = 𝟙` when `a` has no zero entries. This is the
  algebraic shape of the `assemble_diagonal → reciprocal → elementwise_product`
  preconditioner chain.
- **Commutativity of the conjugate variant**:
  `elementwise_product_conj(a, b) = ā ⊙ b ≠ b̄ ⊙ a = elementwise_product_conj(b, a)` in
  general — the conjugation always applies to the **first** argument, breaking the argument
  symmetry of the straight variant. Equal only when both operands are real (or one is real).
- **Distributivity over inner products**: not applicable at L2 — `elementwise_product`
  produces a tensor, not a scalar; the natural composition with `dot`
  (`dot(a, elementwise_product(b, c))`) is a consumer fact (an `inner_product` fold over the
  Hadamard product), not a law of this primitive.
- **Bit-level equivalence under reduction reordering**: `elementwise_product` is
  reduction-free, so this non-law is *vacuous* for the primitive — there is no reduction tree
  to reorder; the per-element multiply is bit-deterministic. It surfaces only when
  `elementwise_product` is consumed by a reduction (`dot(d, elementwise_product(a, b))`
  inherits `dot`'s reduction-tree non-associativity). This is the **opposite** of the
  reduction leaves `dot` / `nrm2`, which carry the IEEE-754 reduction-tree non-law as a
  load-bearing concern of their own.

The law set and non-law set are **inherited unchanged** from L1; the L2 rendering introduces
no new laws or non-laws. This is what makes the L2 ↔ L1 rotation identity-in-form on the
primitive's signature: not only does the signature transport unchanged, the entire algebraic
profile transports unchanged.

## Dependencies

**Same-layer (L2)**: none as a constituent. `elementwise_product` is a **leaf binary field
operation** at L2 just as it is at L1 — the Hadamard-product floor of the elementwise
vocabulary. The body is a single field operation; its sub-operation (the per-element scalar
multiplication of two operand vectors) is below the L2 layer's resolution and visible only
in the L1>L0 lowering.

**Fold-parent**: **none (fork-INDEPENDENT).** `elementwise_product` is **not** a member or
leaf of either L2 fold cohort. It is not the term-axis fold `linear_combination` (which
keeps `Tensor[$S]` but accumulates a `[(Scalar, Tensor[$S])]` term list — a different shape),
and it is not the length-axis fold `inner_product` (which reduces to a `Scalar`). There is
no `do-NOT-merge` fold boundary for this entry because there is no fold to merge it into.
This distinguishes it from the cycle-041 BLAS-1 floors (`dot` = conjugation-leaf of
`inner_product`; `scal` = arity-1 member of `linear_combination`) — and is the load-bearing
reason `elementwise_product` is **not** on the batch-12 meta-phase leaf-vs-fold design fork.

**Sibling subsumption (not dependency)**:

- `scal(α, x) = elementwise_product(broadcast(α, S), x)` — `elementwise_product` strictly
  generalises [`scal`](./linear_combination.md#arity-specializations) (broadcast specialisation; law 7), the **inverse** of
  `scal`'s membership in the `linear_combination` fold. The L0 surfaces are distinct (`scal`
  is `Vector::operator*=(α)` on a scalar; `elementwise_product` is
  `BaseDiagonalOperator::Mult` over two vectors); both stay as L2 siblings, not a dependency
  chain.
- `apply_linop(DiagonalOperator(d), x) = elementwise_product(d, x)` — law 9;
  `elementwise_product` is the realisation of the diagonal-operator action, the operator/data
  sibling of [`apply_linop`](../L1/apply_linop.md). Both stay as siblings: `apply_linop` is
  opaque-operator-and-vector-to-vector; `elementwise_product` is vector-and-vector-to-vector
  with no operator argument.
- `reciprocal` (the elementwise self-map; firm L1/L3) composes with `elementwise_product` to
  form the `assemble_diagonal → reciprocal → elementwise_product` diagonal-preconditioner
  apply chain.

**Consumers (L2)** (cross-reference, not reverse-dependencies) — the
diagonal-preconditioner-apply fan-out:

- [`chebyshev-iteration`](./chebyshev-iteration.md) (firm cycle-012) — its dep-map row
  already cites the `elementwise-product` concept; the diagonally-scaled polynomial sweep
  uses `dinv ⊙ r` per inner step, realised through the same `BaseDiagonalOperator::Mult`
  canonical site. The concept page (`book/src/concepts/elementwise-product.md:17`) names this
  the `dinv ⊙ r` "cheapest possible preconditioning step".
- The Jacobi / block-Jacobi smoother apply (`y = dinv ⊙ x`) — *one* `elementwise_product`,
  the thinnest preconditioner gate (witnessed at L1/L3 `jacobi-smoother`; the L2 smoother
  bodies consume `elementwise_product` as the apply kernel).

**Cross-cutting concepts**:

- [`elementwise-product`](../concepts/elementwise-product.md) — the cross-cutting prose
  treatment (Hadamard / pointwise-product background, the diagonal-operator-apply role at L2,
  the Palace mapping).

**Lowering themes**: both adjacent edges of `elementwise_product` are **degenerate
identity-in-named-terms** rotations recorded **in-line** (no dedicated theme files), per the
2026-06-01 vocabulary-shift redirect (a degenerate identity-in-named-terms lowering is a smell
resolved as a thin in-line note). The L2>L1 edge is recorded in-line at §"Lowers to" below (the L2
leaf lowers into the L1 leaf identity-in-form; no multi-operation kernel fusion to unfold — only the
single per-element `forall_switch` multiply pass, already the unfolded single-pass form); the L3>L2
edge is recorded in-line at the L3 entry's §"Lowers to". The substantive rotation in the chain is the
L1>L0 [`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md)
(sub-pattern B). (The former thin `L2-L1/elementwise-product-leaf-identity` + `L3-L2/elementwise-product-body-identity`
themes were demoted to these in-line notes cycle-050 D4.)

**L1 anchor**: [`L1/elementwise_product`](../L1/elementwise_product.md) (firm;
cycle-019/032/036 chain) — authoritative on the Palace surface details (the canonical
`BaseDiagonalOperator<OperType>::Mult` operator-action site, the `MultHermitianTranspose`
conjugate variant, the `jacobi.cpp` inline consumer duplicate, the absence of any
free-function `linalg::ElementwiseProduct` symbol), the ten algebraic laws, and the complete
L0 evidence list. This L2 entry does not duplicate those details; the L2>L1 rotation is
identity-in-form on the primitive.

## Variant axes

`elementwise_product` has **two variant axes at L2** — the same framing as L1 and L3
(`book/src/L1/elementwise_product.md` §"Variant axes"), transported unchanged: one orthogonal
element-type axis plus one conjugation sub-axis on the complex side. Both are absorbed at
construction time (the element-type axis through template specialisation at L0; the
conjugation axis through which method-template instantiation `Mult` vs.
`MultHermitianTranspose` is called); neither appears in the L2 positional signature.

1. **element-type** (`real` | `complex`) — collapsed to a single parameterised operator at
   L2. The L0 source splits this into two parallel template specialisations (real
   `BaseDiagonalOperator<Operator>::Mult`, per-element single multiply `Y[i] = D[i] * X[i]`;
   complex `BaseDiagonalOperator<ComplexOperator>::Mult`, per-element six-multiply-add complex
   product). At L2 these collapse to one operator parameterised by element type — the
   per-element semantics is "multiplication in the underlying field"; the field is `ℝ` or `ℂ`.

2. **conjugation** (sub-axis on the complex element-type): `straight (a ⊙ b)` |
   `conjugate-first-operand (ā ⊙ b)`. The L0 source materialises the straight form as `Mult`
   and the conjugate form as `MultHermitianTranspose` (complex-only, two sign flips on the
   cross-terms). At L2 this is a structural variant axis (which call form), not a value branch
   — both forms are exhaustively defined per element. The real element-type does **not** carry
   this axis (real conjugation is identity; the L0 real `BaseDiagonalOperator::MultTranspose`
   aliases to `Mult` — `void MultTranspose(const VecType &x, VecType &y) const override { Mult(x, y); }`
   at `reference/palace/palace/linalg/operator.hpp:279`). The conjugate variant breaks
   commutativity (non-law) and changes the conjugation-involution law (law 10), but preserves
   associativity (in the bilinear sense), the all-ones identity, the all-zeros absorption, and
   distributivity over addition.

Non-axes (recorded for disambiguation, inherited from L1):

- **constant-folding on `a` or `b`**: **not** an axis — the L0 source has no constant-folding
  branches (unlike `axpy`'s `α == 1.0` fast path). The canonical and consumer per-element
  kernels are uniform multiplies (`forall_switch` over `N`). Constant-folding cases
  (`a = 𝟙`, `a = 𝟘`) are absorbed into the algebraic laws.
- **operator-action vs. free binary**: **not** an axis at L2 — the canonical L0 site is the
  operator-action form (`DiagonalOperator::Mult`), and Palace has no free-binary
  `linalg::ElementwiseProduct` symbol; but the L1/L2/L3 abstraction lifts the kernel out of
  the operator-action wrapper into a free binary primitive on two equally-shaped vectors. The
  operator-action form is **recovered** algebraically by law 9, not as a variant.

The variant-axis profile (one orthogonal element-type axis + one conjugation sub-axis)
matches the L1 and L3 entries exactly. **No new axes introduced by the L2 rendering; no axes
merged or split.**

## Status

`firm` — signature is canonical (matches the `BaseDiagonalOperator::Mult` operator-action
form, the `MultHermitianTranspose` conjugate variant on the complex side, and the inline
`Apply` consumer duplicate at `jacobi.cpp`, with one element-type axis and a conjugation
sub-axis on the complex side; identical to the L1 and L3 forms), and the ten algebraic laws
are standard pointwise-multiplication facts (commutative ring under elementwise multiply,
distributive over elementwise addition) plus the conjugation-involution rule on the
complex-side variant. **Firm-on-positive-structure**: the L2 form is value-thread-isomorphic
to the firm L1 leaf, and every law is a syntactic identity on fully-specified positive source
(per-element multiply lambdas in `forall_switch` at the canonical `BaseDiagonalOperator::Mult`
site + the `jacobi.cpp` consumer duplicate); the absent dedicated `test-elementwise-product`
does not gate firm (the syntactic-identity-laws-on-positive-source escape, the `apply_linop`
situation, not the `eigsolve`-convergence-semantics situation). There is **no caveat** to
record — the Hadamard product is exact per element across all representations.

This dispatch is the **L2 floor backfill** (cycle-042 D3) under the foundation-first directive
`l2-floor-under-l3-leaf-cohort`: the L2 form was previously referenced only inside
`chebyshev-iteration`'s dependency list and as the `dinv ⊙ r` step of the smoother bodies; it
now has its own L2 entry per **Identity-lowerings still require both L levels**.
**Fork-INDEPENDENT — standalone elementwise binary, NO fold-parent**: this entry is
design-final regardless of the batch-12 meta-phase leaf-vs-fold adjudication (that fork is
about the BLAS-1 floors' relationship to the *fold* parents `inner_product` /
`linear_combination`; `elementwise_product` has no fold-parent and is not on that fork).

## Lowers to

L2 `elementwise_product` lowers to L1 [`elementwise_product`](../L1/elementwise_product.md)
via a **degenerate identity-in-named-terms** rotation, recorded **in-line** (no dedicated theme) per
the 2026-06-01 vocabulary-shift redirect: the signature is congruent at both layers (L2 `(Tensor[(S: ...)], Tensor[$S]) -> Tensor[$S]`; L1 the flat dof-vector spelling `(Tensor[N], Tensor[N]) -> Tensor[N]`), and the mapping is the total bijective identity on the leaf —
every L2 binding (the `a ⊙ b` body, the ten algebraic laws, both variant axes: element-type +
conjugation sub-axis) maps to the same L1 binding at the same position. There is no multi-operation
kernel fusion to unfold — `elementwise_product` is a leaf binary field operation with **no fold-parent**
(fork-INDEPENDENT; the inverse-subsumption generalisation of `scal`, not a fold member), and the L0
`forall_switch` per-element multiply is already the unfolded single-pass form (contrast `dot`, which
de-fuses a family of fused reduction kernels into the canonical reduction). Because the vocabulary does
not shift across this edge, it is a thin in-line note, not a mirrored theme. (Demoted from the former
`L2-L1/elementwise-product-leaf-identity.md` theme, cycle-050 D4.) The **substantive** rotation in the
chain is the L1>L0
[`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md)
(sub-pattern B) — it reintroduces the L0 in-place destination buffer (the real single-multiply
`Y[i] = A[i] * B[i]`, the complex six-multiply-add, the conjugate two-sign-flip variant, and
the device dispatch).

## Lifts from

L1 `elementwise_product` lifts to this L2 entry via the **value-thread-isomorphic** identity
rotation: the L1 form's signature has no kernel fusion exposed, no destination buffer, no MPI
collective — these are exactly the properties that make it L2-native by construction as a base
tensor-algebra binary primitive. The L2 entry exists for layer-coherence reasons — a reader
navigating L2 must find `elementwise_product` defined in L2 vocabulary as the base
Hadamard-binary-multiply primitive (and as the diagonal-operator apply primitive, law 9), not
have to reach down to L1 to recover the field-operation shape. The cycle-041 `dot` / `nrm2` /
`scal` L2 floor backfills are the structural precedents — identity-in-form rotation on the
primitive's signature, leaf layer-coherence backfill, foundation-first directive enacted — with
the one difference that `elementwise_product` is **fork-independent** (no fold-parent), so it
carries no fold-membership identity (whereas `scal` carries the arity-1 `linear_combination`
membership and `dot` the conjugation-leaf `inner_product` membership).

## Evidence

The L2 form is value-thread-isomorphic to the L1 form (identity-in-form on the primitive's
signature); all L0 evidence is sourced from the firm L1 entry. Direct citations relevant to
this L2 entry (paths relative to `reference/palace/`; L0 ranges self-verified via
`tools/citecheck/citecheck.py --anchor` this invocation, 2026-06-01):

- `book/src/L1/elementwise_product.md` (firm; cycle-019/032/036 chain) — the L1 form this L2
  entry value-thread-mirrors. Body shape, signature, semantics (element-local, reduction-free,
  rank-local), the ten algebraic laws, variant axes (two: element-type + conjugation sub-axis
  on the complex side), and the complete L0 evidence chain. The laws and non-laws above are
  reproduced from `book/src/L1/elementwise_product.md:43` §"Algebraic laws"; the `scal`
  broadcast-subsumption from `book/src/L1/elementwise_product.md:41`; the
  firm-on-positive-structure rationale from `book/src/L1/elementwise_product.md:99`.
- `book/src/L3/elementwise_product.md` (firm cycle-038) — the L3 consumer this floor entry
  supports; identical signature and laws, iteration-rotation framing. The L3>L2 hop is the
  identity rotation recorded in-line there (the L3 entry's "Lowers to" prose notes the
  no-interposed-L2-entry situation this dispatch now closes).
- `book/src/L2/index.md` — the L2 Part overview; §"Fold cohorts" defines the two fold cohorts
  `elementwise_product` is **not** a member of (`inner_product` reduce-to-`Scalar`,
  `linear_combination` reduce-to-`Tensor[$S]`); §"Identity-in-form BLAS-1 floors" / the
  cycle-041 floor-cohort note is the precedent framing this standalone floor extends.
- `book/src/L2/linear_combination.md` §Arity specializations (the arity-1 `scal` readout, folded in cycle-124 RE6) — the floor-cohort template; `scal` is the
  broadcast-scalar special case `scal(α, x) = elementwise_product(broadcast(α, S), x)` (law 7,
  the inverse-fork relationship). `book/src/L2/dot.md` (firm cycle-041) — the thin
  identity-in-form floor template (leaf, laws inherited unchanged from the L1 leaf, fusion note
  deferred).
- `book/src/L2/chebyshev-iteration.md` (firm cycle-012) — the L2 consumer; its dep-map row
  cites the `elementwise-product` concept for the `dinv ⊙ r` diagonal-operator apply step.
- `book/src/concepts/elementwise-product.md` — pre-existing cross-cutting prose treatment;
  consistent with this L2 entry's framing (`:17` names the L2 diagonal-operator-apply role and
  the `dinv ⊙ r` cheapest-preconditioning-step; `:19` notes the trivial lift to L3).

**L0 evidence (canonical anchors, self-verified via on-disk `citecheck --anchor`,
2026-06-01)**:

- `palace/linalg/operator.cpp:478-487` — `BaseDiagonalOperator<Operator>::Mult` real, the
  **canonical** elementwise-multiply site:
  `mfem::forall_switch(use_dev, N, [=] MFEM_HOST_DEVICE(int i) { Y[i] = D[i] * X[i]; });` at
  `:486` (single multiply per element). Direct witness of laws 1 (symmetric in `D` and `X`), 9
  (the operator-action identity), and the `forall_switch` device-uniform single-pass kernel
  (the "already-unfolded leaf, no fusion to undo" observation).
- `palace/linalg/operator.cpp:489-507` — `BaseDiagonalOperator<ComplexOperator>::Mult` complex,
  the **canonical complex straight-multiply** site: six fused multiply-adds per element
  `YR[i] = DR[i] * XR[i] − DI[i] * XI[i]; YI[i] = DI[i] * XR[i] + DR[i] * XI[i]` at `:504-505`.
  Witness of the complex element-type variant and the per-element complex semantics.
- `palace/linalg/operator.cpp:545-568` —
  `DiagonalOperatorHelper<BaseDiagonalOperator<ComplexOperator>, ComplexOperator>::MultHermitianTranspose`,
  the **canonical conjugate-variant** site:
  `YR[i] = DR[i] * XR[i] + DI[i] * XI[i]; YI[i] = −DI[i] * XR[i] + DR[i] * XI[i]` at `:564-565`
  (two sign flips realising `d̄ ⊙ x`). Witness of the conjugation sub-axis on the complex side.
- `palace/linalg/operator.hpp:279` — the real
  `BaseDiagonalOperator<Operator>::MultTranspose` alias to `Mult`
  (`void MultTranspose(const VecType &x, VecType &y) const override { Mult(x, y); }`); confirms
  the real element-type does not carry the conjugation axis.
- No dedicated `test-elementwise-product` exists in `reference/palace/test/unit/` (search
  confirms, transitive through L1); the operator is exercised indirectly through the
  diagonal-preconditioner consumer chain. Per the `firm-on-positive-structure` precedent, the
  absent dedicated test does not gate firm.

## L2 vs L1 distinction

- **L1**: mutation-lifted pure functional binary operator. `result = elementwise_product(a, b)`.
  Frames the operator as the pure-functional image of the L0 `BaseDiagonalOperator::Mult`
  output-arg-mutating idiom; emphasises the *mutation rotation* against the source (the
  destination-buffer drop, the operator-class unwrapping, the consumer-local inline-duplication
  erasure at `jacobi.cpp`).
- **L2**: base tensor-algebra binary field operation. `result = elementwise_product(a, b)`.
  Frames the operator as a **standalone (fork-independent) leaf primitive** in the
  fusion-rotation layer's base vocabulary — NOT a member of either fold cohort; emphasises that
  there is no multi-operation kernel fusion to unfold (the L0 `forall_switch` per-element
  multiply is already the unfolded single-pass form). The L2 form is **identical in body and
  signature to L1** — the framing differs (mutation rotation at L1 vs fusion rotation +
  fork-independence at L2), but no operational adjustment occurs.

The L2 ↔ L1 rotation is identity-in-form on the body and signature; the surface adjustment is
documentary. The methodology invariant **each layer is coherent within itself** is what compels
the L2 entry to exist as its own anchor — and the foundation-first directive
`l2-floor-under-l3-leaf-cohort` is what schedules it, so the firm L3
[`elementwise_product`](../L3/elementwise_product.md) rests on a present adjacent L2 parent.
