---
agent: harvester
invoked_at: 2026-05-30T15:30:00Z
scope: L1 operator: elementwise_product
status: applied
integrated_at: 2026-05-30T18:00:00Z
integration_commit: PLACEHOLDER_SHA
integration_notes: |
  Cycle-033 D3; landed firm L1 leaf book/src/L1/elementwise_product.md (the Hadamard
  pointwise-product primitive a ⊙ b; the diagonal-operator-action primitive at L1 —
  law 9: apply_linop(DiagonalOperator(d), x) = elementwise_product(d, x); two variant
  axes: element-type {Real,Complex} × conjugation sub-axis on complex; canonical L0
  site BaseDiagonalOperator::Mult at palace/linalg/operator.cpp:486,:504-505 +
  MultHermitianTranspose conjugate variant at :564-565). L1 Firm count 24->25;
  cohort bullet + dep-map row + SUMMARY entry inserted after reciprocal (post-D2
  anchor). firm-on-positive-structure per the apply_linop / lu_solve / back_solve /
  ls_update_column / jacobi-smoother no-dedicated-test precedent. 3 OQs filed:
  elementwise-product-l1-l0-mutation-rotation-theme (abstractor candidate c034+
  possibly composite with reciprocal-mutation-rotation),
  elementwise-product-apply-linop-diagonal-operator-round-trip-law-9-cross-reference
  (informational cross-reference for future assemble-diagonal editing pass),
  elementwise-product-conjugation-variant-axis-vs-distinct-primitive-decision-record
  (durable methodology-decision record; may seed a future skill). Closes the other
  half of the c032 routed reciprocal-and-elementwise-product-l1-primitives
  stub-or-harvest decision. Completes the diagonal-preconditioner-apply
  assemble_diagonal -> reciprocal -> elementwise_product chain that
  assemble-diagonal:73 + jacobi-smoother:289-297 previously forward-referenced.
inputs:
  - cycle-033 plan D3 dispatch (lower-shared-vocabulary; forward-referenced from `jacobi-smoother` cycle-032 + `assemble-diagonal` cycle-019 + `chebyshev-smoother` cycle-012)
  - `palace/linalg/operator.cpp:478-507,545-568` — `BaseDiagonalOperator::Mult` real + complex + `MultHermitianTranspose` conjugate variant (canonical operator-class site)
  - `palace/linalg/operator.hpp:256-289` — `BaseDiagonalOperator` class definition (operator-action-as-elementwise-multiply)
  - `palace/linalg/jacobi.cpp:30-39,41-69` — local `Apply` helper (consumer/witness; duplicates the canonical kernel inline)
  - `book/src/concepts/elementwise-product.md` — pre-existing cross-cutting concept page
  - sibling L1 entries `scal.md`, `axpy.md`, `assemble-diagonal.md`, `jacobi-smoother.md` (house style)
---

# CYCLE: Formalize elementwise_product at L1

## Summary

Lands the first firm L1 entry for `elementwise_product` (Hadamard pointwise product `(a, b) → a ⊙ b`, `result[i] = a[i] · b[i]`) — a lower-shared-vocabulary primitive forward-referenced by **three** firm L1 chapters (`jacobi-smoother` cycle-032, `assemble-diagonal` cycle-019, `chebyshev-smoother` cycle-012) and the **L2** [`chebyshev-iteration`](../L2/chebyshev-iteration.md) lift. The canonical L0 site is `palace/linalg/operator.cpp:478-507` (`BaseDiagonalOperator<Operator>::Mult` real and `<ComplexOperator>::Mult` complex) — the operator-class formal realization of "apply a diagonal operator as elementwise multiply against its defining vector". The conjugate-transpose variant (`MultHermitianTranspose`, `:545-568`, complex-only) supplies a first-class **conjugation variant axis** on the complex element-type: `Mult = a ⊙ b` vs. `MultHermitianTranspose = ā ⊙ b`. The Jacobi `Apply` helper (`palace/linalg/jacobi.cpp:30-69`) is a line-for-line consumer duplicate cited as second-witness.

Status lands `firm` per the **firm-on-positive-structure** precedent (`apply_linop` / `lu_solve` / `back_solve` / `ls_update_column` / `jacobi-smoother`): every law is a syntactic identity on fully-specified positive source, so the absent dedicated `test-elementwise-product` test does not gate firm. The variant-axis treatment carries one conjugation axis (real | complex × straight | conjugate-RHS) absorbed cleanly without bifurcating the primitive — confirms the OQ-posed judgement.

This is **D3 in cycle-033**'s lower-shared-vocabulary cohort, parallel with D2 (`reciprocal`); the consuming `jacobi-smoother` apply factors as the composition `dinv_ω ⊙ x` where `dinv_ω = ω · reciprocal(assemble_diagonal(op))`. With this cycle's two additions, the `assemble_diagonal → reciprocal → elementwise_product` chain that `assemble-diagonal:73` and `jacobi-smoother:289-297` flagged as "forthcoming, plain text" is fully realised in firm L1 vocabulary.

## Proposed changes

```new:book/src/L1/elementwise_product.md
# elementwise_product

Pure elementwise (Hadamard) pointwise product `result = a ⊙ b`, defined by `result[i] = a[i] · b[i]` for `i ∈ [0, N)`. The diagonal-operator-action primitive at L1, and the per-call kernel of the diagonally-scaled-preconditioner cohort (`jacobi-smoother`, `chebyshev-smoother`, block-Jacobi).

## Context

`elementwise_product` lifts Palace's elementwise pointwise-multiply kernel from the diagonal-operator method form (the canonical site: `BaseDiagonalOperator<OperType>::Mult` writing `y[i] = d[i] · x[i]` at `palace/linalg/operator.cpp:478-487` real and `:489-507` complex, plus the conjugate-transpose variant at `:545-568`) and from one inline consumer duplicate (`palace/linalg/jacobi.cpp:30-39` real, `:41-69` complex) to a single pure-functional binary operator. The L0 surface mutates the output destination buffer (`Y[i] = D[i] * X[i]` in the real case; six fused multiply-adds across `(YR, YI)` in the complex case); the L1 form drops the destination-buffer mention — the operator consumes the prior values of `a` and `b` and produces a fresh result vector.

There is no free-function `linalg::ElementwiseProduct` / `linalg::Hadamard` symbol in Palace — the operation surfaces exclusively as **the action of a `BaseDiagonalOperator` against a vector** (the canonical site) and as **inline consumer-local duplicates** of the same kernel (`jacobi.cpp`). The conceptual decoupling at L1 — `elementwise_product(a, b)` as a free binary operator independent of either operand being the "diagonal of an operator" — is the L1 abstraction over an L0 surface that has only the operator-method form. The cycle-019 [`assemble-diagonal`](./assemble-diagonal.md) entry §Dependencies:73 named the `assemble_diagonal → reciprocal → elementwise_product` chain as "forthcoming, plain text"; this entry closes the chain.

A cross-cutting prose treatment already lives at [`elementwise-product`](../concepts/elementwise-product.md) — covering background (Hadamard / pointwise product), role at L2 (the diagonal-operator apply), and the Palace mapping. The L1 entry here is the firm operator definition; the concept page is the narrative.

## Signature

    elementwise_product :: (a: Tensor[N], b: Tensor[N]) -> Tensor[N]
    elementwise_product(a, b) = a ⊙ b

Shape contract (bunsen-style, named axes):

- `a` — `Tensor[N]` — read-only.
- `b` — `Tensor[N]` — read-only.
- result — `Tensor[N]` — same axis `N` as inputs.

`a` and `b` must share the same length axis `N` and the same element type (both real or both complex). The conjugate variant (complex element-type only) takes one operand to its conjugate before multiplying:

    elementwise_product_conj :: (a: ComplexTensor[N], b: ComplexTensor[N]) -> ComplexTensor[N]
    elementwise_product_conj(a, b) = ā ⊙ b

— modeled here as the same operator with a **conjugation variant axis** (see Variant axes below) rather than as a separate primitive.

## Semantics

Element-wise: `result[i] = a[i] · b[i]` for `i ∈ [0, N)`. Reduction-free and element-local — every output element depends on exactly one input element from each of `a` and `b`. No cross-element communication, no dependence on iteration order, no MPI collective at any layer (elementwise multiplication is rank-local; ranks own disjoint slices of `N`).

The operator is pure at L1: the prior `a`, the prior `b`, and the new `result` are distinct values. The L0 source overwrites the in-place destination buffer; the L1>L0 lowering theme is where that overwrite is reintroduced (forthcoming `elementwise-product-mutation-rotation`, plain-text forward-reference). At L1 the relationship is purely algebraic.

In the **complex** element-type, the per-element multiply is the standard complex multiplication `(a_R + i·a_I)(b_R + i·b_I) = (a_R·b_R − a_I·b_I) + i·(a_I·b_R + a_R·b_I)` — exactly the six fused multiply-adds in `reference/palace/palace/linalg/operator.cpp:498-507`. In the **conjugate variant** (`MultHermitianTranspose`), the multiply is `(a_R − i·a_I)(b_R + i·b_I) = (a_R·b_R + a_I·b_I) + i·(−a_I·b_R + a_R·b_I)` — exactly `reference/palace/palace/linalg/operator.cpp:561-568`. The two forms differ only in the sign of two cross-terms; algebraically the conjugate variant is `ā ⊙ b`.

Special algebraic cases — `a = 1` (the all-ones vector — identity in `a`), `a = 0` (zero in `a`), `a = -1` (negation), `a = b` (squaring each element) — are not separate operators at L1; they are algebraic identities recorded in the laws below. The L0 source has **no** constant-folding branches on `a` or `b` — the canonical and consumer kernels are uniform per-element multiplies (`forall_switch` over `N` with the multiply lambda). The conjugation variant in the complex case is a structural axis (which kernel template instantiation `Mult` vs. `MultHermitianTranspose`), not a value branch on `imag(a) == 0`.

`elementwise_product` and `scal` are tightly related but distinct: `scal(α, x) = elementwise_product(broadcast(α, N), x)` — i.e. `scal` is the special case of `elementwise_product` when the first operand is a length-`N` broadcast of a single scalar. They stay as **sibling leaf primitives** at L1; `scal` is not factored as a dependency of `elementwise_product` (the L0 surfaces are distinct — `scal` is `Vector::operator*=(α)` on a scalar argument; `elementwise_product` is `BaseDiagonalOperator::Mult` over two equally-shaped vectors) and `elementwise_product` is not factored as a dependency of `scal`. The broadcast relationship is the **inverse** of `axpby`'s subsumption of `scal` — `elementwise_product` strictly generalises `scal`'s scalar-multiplication action to a vector-multiplication action.

## Algebraic laws

The laws below hold; absences are deliberate.

1. **Commutativity**: `elementwise_product(a, b) = elementwise_product(b, a)`. Inherited from element-wise scalar commutativity in the underlying field (`ℝ` or `ℂ`). The complex *non-conjugate* form is genuinely commutative; the **conjugate variant** is **not** (see non-laws below).
2. **Associativity**: `elementwise_product(a, elementwise_product(b, c)) = elementwise_product(elementwise_product(a, b), c)`. Inherited from per-element associativity.
3. **Identity (all-ones)**: `elementwise_product(𝟙, x) = x` where `𝟙` is the all-ones vector of axis `N`. The neutral element of pointwise multiplication.
4. **Absorption (all-zeros)**: `elementwise_product(𝟘, x) = 𝟘` for any `x`, where `𝟘` is the zero vector of axis `N`. Element-wise: `0 · x[i] = 0`.
5. **Distributivity over vector addition**: `elementwise_product(a, b + c) = elementwise_product(a, b) + elementwise_product(a, c)`. Linearity in the second argument. By commutativity (law 1), also `elementwise_product(a + b, c) = elementwise_product(a, c) + elementwise_product(b, c)` (linearity in the first argument).
6. **Scalar absorption (compatibility with `scal`)**: `elementwise_product(scal(α, a), b) = scal(α, elementwise_product(a, b)) = elementwise_product(a, scal(α, b))` for any scalar `α`. The scalar passes freely between either operand and the outside.
7. **Subsumption of `scal` (broadcast specialisation)**: `scal(α, x) = elementwise_product(broadcast(α, N), x)`, where `broadcast(α, N)` is the all-`α` vector of length `N`. The relationship is stated as an algebraic identity, not a dep-map edge — both operators stay as siblings.
8. **Negation**: `elementwise_product(−𝟙, x) = −x`. (Special case of laws 3 + 5 + 6 with `α = -1`.)
9. **Diagonal-operator action (operator/data identity)**: for any vector `d ∈ Tensor[N]`, `apply_linop(DiagonalOperator(d), x) = elementwise_product(d, x)`. This is the **defining identity** of the operator-class realization at the canonical L0 site (`BaseDiagonalOperator<Operator>::Mult` writing `Y[i] = D[i] * X[i]`, `reference/palace/palace/linalg/operator.cpp:486`). The diagonal-operator constructor wraps a vector into a `LinearOperator`; applying that operator IS the elementwise product against the wrapped vector. This law makes `elementwise_product` the operator/data sibling of [`apply_linop`](./apply_linop.md) on the diagonal-operator slice: where `assemble-diagonal` extracts the diagonal *out of* an opaque operator, `elementwise_product` realizes the action of the diagonal-operator *constructed from* a vector. It is the law that closes the `assemble_diagonal → reciprocal → elementwise_product → DiagonalOperator-apply` round-trip for diagonal preconditioners.
10. **Conjugation involution (conjugate variant only, complex element-type)**: `elementwise_product_conj(a, elementwise_product_conj(b, c)) = elementwise_product(elementwise_product(ā, b̄), c) = elementwise_product(¯(a ⊙ b), c)` — applying the conjugate variant twice conjugates the combined left operand. Equivalent: `elementwise_product_conj(elementwise_product_conj(a, b), c) ≠ elementwise_product(a, elementwise_product_conj(b, c))` in general — the conjugation is left-applied per call.

Laws that explicitly **do not** hold:

- **Idempotence**: `elementwise_product(a, a) ≠ a` in general — the result is the elementwise square `a ⊙ a`, which equals `a` only when each `a[i] ∈ {0, 1}` (more broadly when `a[i]² = a[i]`, i.e. `a[i](a[i] − 1) = 0` per element). For complex `a`, the corresponding fixed points are `{0, 1}` (the same idempotent scalars).
- **Inverse (multiplicative)**: there is no general two-sided inverse — `elementwise_product(a, b) = 𝟙` has the solution `b[i] = 1 / a[i]` only when **every** `a[i] ≠ 0`. The partial inverse is realized by composing with `reciprocal` (the sibling L1 primitive being authored in the same cycle): `elementwise_product(a, reciprocal(a)) = 𝟙` when `a` has no zero entries. This is the algebraic shape of the `assemble_diagonal → reciprocal → elementwise_product` preconditioner chain.
- **Commutativity of the conjugate variant**: `elementwise_product_conj(a, b) = ā ⊙ b ≠ b̄ ⊙ a = elementwise_product_conj(b, a)` in general — the conjugation always applies to the **first** argument, breaking the argument symmetry of the straight variant. The two are equal only when `a` and `b` are both real, or when one of them is real and `imag(other) = 0`.
- **Distributivity over inner products**: not applicable at L1 — `elementwise_product` produces a vector, not a scalar; the natural composition with `dot` is `dot(a, elementwise_product(b, c)) = dot(elementwise_product(a, b), c) = dot(elementwise_product(ā, ·), ...)` depending on conjugation convention. These are L2 fold facts, not L1 laws.
- **Bit-level equivalence under reduction reordering**: `elementwise_product` itself is reduction-free, so this non-law is *vacuous* for the primitive — there is no reduction tree to reorder. The non-law surfaces only when `elementwise_product` is consumed by a reduction (`dot(d, elementwise_product(a, b))` inherits `dot`'s reduction-tree non-associativity); the elementwise multiply itself is bit-deterministic per element.

## Dependencies

None at L1. `elementwise_product` is a **leaf primitive** at L1 — the diagonal-operator-action / Hadamard-product floor of the elementwise vocabulary, sibling to [`scal`](./scal.md) (scalar broadcast specialisation), [`axpy`](./axpy.md) / [`axpby`](./axpby.md) / [`axpbypcz`](./axpbypcz.md) (linear-combination cohort), and [`reciprocal`](./reciprocal.md) (the elementwise-inverse sibling co-authored this cycle as D2 — see plain-text fallback below if the live link doesn't resolve at integration time). Its sub-operation is the per-element scalar multiplication of two operand vectors, at the L1 layer's resolution.

Sibling subsumption (not dependency):

- `scal(α, x) = elementwise_product(broadcast(α, N), x)` — `elementwise_product` strictly generalises `scal` (broadcast specialisation); both stay in the L1 dep-map as siblings.
- `apply_linop(DiagonalOperator(d), x) = elementwise_product(d, x)` — law 9; `elementwise_product` is the realization of the diagonal-operator action. Both stay as siblings: `apply_linop` is opaque-operator-and-vector-to-vector; `elementwise_product` is vector-and-vector-to-vector with no operator argument.
- `reciprocal(a)` (co-authored D2) — composes with `elementwise_product` to form the `assemble_diagonal → reciprocal → elementwise_product` diagonal-preconditioner chain (`jacobi-smoother`, `chebyshev-smoother`, block-Jacobi).

Downstream consumers at L1 (cross-reference, not reverse-dependencies):

- [`jacobi-smoother`](./jacobi-smoother.md) — the apply body is one elementwise product: `y = dinv_ω ⊙ x`, realised by the local `Apply` helper at `palace/linalg/jacobi.cpp:30-39` (real) and `:41-69` (complex). The smoother's defining lightness is *one elementwise product, no `apply_linop` call*.
- [`chebyshev-smoother`](./chebyshev-smoother.md) — the diagonally-scaled polynomial sweep uses `dinv ⊙ r` per inner step (cycle-012 firm; `palace/linalg/chebyshev.cpp:177-178,240-241` setup), then `DiagonalOperator(dinv)` realised through the same `BaseDiagonalOperator<Operator>::Mult` canonical site.
- [`assemble-diagonal`](./assemble-diagonal.md) — closes the `assemble_diagonal → reciprocal → elementwise_product` chain (cycle-019 §Dependencies:73 forward-reference).
- L2 [`chebyshev-iteration`](../L2/chebyshev-iteration.md) — Concepts cross-reference §:189 cites `elementwise-product` as "the diagonal-operator apply primitive at L2".

## Variant axes

`elementwise_product` has two orthogonal variant axes at L1:

- **element-type**: `real` | `complex`. The L0 source separates these into the two parallel template specialisations — real `BaseDiagonalOperator<Operator>::Mult` at `palace/linalg/operator.cpp:478-487` (per-element single multiply `Y[i] = D[i] * X[i]`) and complex `BaseDiagonalOperator<ComplexOperator>::Mult` at `palace/linalg/operator.cpp:489-507` (per-element six-multiply-add complex product). At L1 these collapse to one operator parameterised by element type — the per-element semantics is "multiplication in the underlying field"; the field is `ℝ` or `ℂ`.

- **conjugation** (sub-axis on the complex element-type): `straight (a ⊙ b)` | `conjugate-first-operand (ā ⊙ b)`. The L0 source materialises the straight form as `Mult` (`reference/palace/palace/linalg/operator.cpp:489-507`) and the conjugate form as `MultHermitianTranspose` (`reference/palace/palace/linalg/operator.cpp:545-568`, complex-only, three sign flips on the cross-terms). At L1 this is a structural variant axis (which call form), not a value branch — both forms are exhaustively defined per element. The real element-type does **not** carry this axis (real conjugation is identity); the L0 real `MultTranspose` aliases to `Mult` per `reference/palace/palace/linalg/operator.hpp:279`. The conjugate variant breaks commutativity (non-law above) and changes the conjugation-involution law (law 10), but preserves associativity (in the bilinear sense `elementwise_product(ā, b ⊙ c)`), the all-ones identity (with the convention `𝟙̄ = 𝟙`), the all-zeros absorption, and distributivity over addition. *Variant-axis decision rationale*: kept as one axis with two values rather than as two distinct primitives (`elementwise_product` vs. `complex_elementwise_multiply_conj`) because the conjugation differs only in three sign flips on cross-terms — the operator's identity is "elementwise multiplication" in both cases, parameterised by which operand (if any) is conjugated. This is justified on the operator's own terms: the eight non-conjugation-sensitive laws (commutativity in the straight form, associativity, all-ones identity, all-zeros absorption, distributivity, scalar absorption, broadcast subsumption of `scal`, negation) are **identical** between straight and conjugate variants — the conjugation only modifies the commutativity (broken) and adds the involution law (law 10). Splitting into two primitives would duplicate eight laws verbatim for negligible gain. (Note: this is a *different* convention than `dot` / `tdot`, where on-disk `book/src/L1/dot.md:16-20,:94` treats them as **two distinct operators co-housed in one chapter** — they share only the reduction skeleton and their algebraic laws genuinely differ (e.g. `dot` is positive semi-definite at `y = x`, `tdot` is not). For `elementwise_product` the algebraic-law overlap is much larger and the variant is a true sub-axis, hence the different modeling choice.)

Non-axes (recorded for disambiguation):

- **constant-folding on `a` or `b`**: not an axis — the L0 source has no constant-folding branches (unlike `axpy`'s `α == 1.0` fast path or `scal`'s `imag(s) == 0.0` complex-shape specialisation). The canonical and consumer per-element kernels are uniform multiplies (`forall_switch` over `N`). Constant-folding cases (`a = 𝟙`, `a = 𝟘`) are absorbed into the algebraic laws above.
- **operator-action vs. free binary**: not an axis at L1 — the canonical L0 site is the operator-action form (`DiagonalOperator::Mult`), and Palace has no free-binary `linalg::ElementwiseProduct` symbol; but the L1 abstraction lifts the kernel out of the operator-action wrapper into a free binary primitive on two equally-shaped vectors. The operator-action form is **recovered** algebraically by law 9 (`apply_linop(DiagonalOperator(d), x) = elementwise_product(d, x)`); the recovery is an algebraic identity, not a variant.
- **dead-code conjugate path**: `palace/linalg/jacobi.cpp:61-69` (the `Transpose = true` complex `Apply` template instantiation inside `jacobi.cpp`) is **unreferenced** in Palace because `JacobiSmoother::MultTranspose` aliases to `MultHermitianTranspose` which aliases through to `Mult` for the real-`dinv` smoother. It is recorded as a dead-code caveat in [`jacobi-smoother`](./jacobi-smoother.md). The canonical `BaseDiagonalOperator<ComplexOperator>::MultHermitianTranspose` at `reference/palace/palace/linalg/operator.cpp:545-568` IS live (called whenever a diagonal operator's Hermitian-transpose action is needed) — so the conjugation axis is not dead at the canonical site even though one specific consumer's copy of it is.

## Status

`firm` — signature is canonical (matches the `BaseDiagonalOperator::Mult` operator-action form, the `MultHermitianTranspose` conjugate variant on the complex side, and the inline `Apply` helper consumer duplicate at `jacobi.cpp`, with one element-type axis and a sub-axis for conjugation on the complex side), evidence is direct from the canonical operator-class site plus consumer-duplicate cross-witness, and the ten algebraic laws listed are standard properties of pointwise multiplication (commutative ring under elementwise multiply, distributive over elementwise addition) plus the conjugation-involution rule on the complex-side variant.

**Firm-on-positive-structure** — every law is a syntactic identity on fully-specified positive source (per-element multiplies in `forall_switch` lambdas at `reference/palace/palace/linalg/operator.cpp:486` + `reference/palace/palace/linalg/operator.cpp:498-507` + `reference/palace/palace/linalg/operator.cpp:561-568` and `reference/palace/palace/linalg/jacobi.cpp:38` + `reference/palace/palace/linalg/jacobi.cpp:52-60` + `reference/palace/palace/linalg/jacobi.cpp:62-68`); the absent dedicated `test-elementwise-product` test does not gate firm. Precedent: the `apply_linop` / `lu_solve` / `back_solve` / `ls_update_column` / `jacobi-smoother` (cycle-032, same chain) decisions.

The L1>L0 mutation-rotation theme — `elementwise-product-mutation-rotation` — is forthcoming (plain-text forward-reference; not yet authored). The dominant rewrite pattern is the same destination-binding rule as `dot-mutation-rotation` and `assemble-diagonal-mutation-rotation`: an output-arg `y = a ⊙ b` at L1 lowers to a `forall_switch` per-element kernel writing `Y[i] = A[i] * B[i]` at L0 with the destination buffer reintroduced.

## L1 vs L0 distinction

- **L0**: an operator-class method (the canonical `BaseDiagonalOperator<OperType>::Mult` writing `Y[i] = D[i] * X[i]` through the output vector argument, with the implicit "the operator IS its diagonal vector" wrapping) plus inline consumer duplicates (the `Apply` helper at `jacobi.cpp:30-69` writing `Y[i] = DI[i] * X[i]` for the smoother's `dinv ⊙ x` per-call action). The complex case carries six fused multiply-adds per element across `(YR, YI, DR, DI, XR, XI)`; the conjugate variant flips three signs. No free-function `linalg::ElementwiseProduct` exists.

- **L1**: pure functional binary operator. `result = elementwise_product(a, b)`. No destination buffer in the signature, no operator wrapping, no output sizing, no workspace. One operator parameterised by element type with a conjugation sub-axis on the complex side. Algebraic laws (commutativity, associativity, identity, absorption, distributivity, scalar absorption, broadcast-subsumption-of-`scal`, diagonal-operator-action identity, conjugation involution) apply directly. The L0 in-place mutation, the operator-class wrapping at the canonical site, the consumer-local inline duplication of the kernel at `jacobi.cpp`, and the `forall_switch` device dispatch are all L1>L0 lowering concerns.

## Evidence

- `reference/palace/palace/linalg/operator.hpp:256-289` — `BaseDiagonalOperator<OperType>` class definition (`class BaseDiagonalOperator` at `:257`, the `Mult` / `MultTranspose` / `AddMult` / `AddMultTranspose` overrides at `:277-286`), with the type aliases `using DiagonalOperator = BaseDiagonalOperator<Operator>` at `:290` and `using ComplexDiagonalOperator = BaseDiagonalOperator<ComplexOperator>` at `:291`. The operator-class wrapping that makes `apply_linop(DiagonalOperator(d), x)` the **defining identity** site for law 9.
- `reference/palace/palace/linalg/operator.cpp:478-487` — `BaseDiagonalOperator<Operator>::Mult` real, the **canonical** elementwise-multiply site: `mfem::forall_switch(use_dev, N, [=] MFEM_HOST_DEVICE(int i) { Y[i] = D[i] * X[i]; });` at `:486`. Single multiply per element. Direct evidence of laws 1 (commutativity is symmetric in `D` and `X`), 9 (the operator-action identity), and the `forall_switch` device-uniform kernel.
- `reference/palace/palace/linalg/operator.cpp:489-507` — `BaseDiagonalOperator<ComplexOperator>::Mult` complex, the **canonical complex straight-multiply** site: six fused multiply-adds per element `YR[i] = DR[i] * XR[i] − DI[i] * XI[i]; YI[i] = DI[i] * XR[i] + DR[i] * XI[i]` at `:504-505`. Standard complex multiplication realised as four real multiplies + two real subtract/adds. Direct evidence of the complex element-type variant and the per-element complex semantics.
- `reference/palace/palace/linalg/operator.cpp:545-568` — `DiagonalOperatorHelper<BaseDiagonalOperator<ComplexOperator>, ComplexOperator>::MultHermitianTranspose`, the **canonical conjugate-variant** site: `YR[i] = DR[i] * XR[i] + DI[i] * XI[i]; YI[i] = −DI[i] * XR[i] + DR[i] * XI[i]` at `:564-565`. Three sign flips (on `DI*XI` cross-term + on both `DI*XR` cross-terms) realise the conjugation `d̄ ⊙ x` algebraically. Direct evidence of the conjugation sub-axis on the complex side.
- `reference/palace/palace/linalg/jacobi.cpp:30-39` — `Apply<Transpose=false>` real helper, the **consumer-duplicate** site for the Jacobi smoother: `mfem::forall_switch(use_dev, N, [=] MFEM_HOST_DEVICE(int i) { Y[i] = DI[i] * X[i]; });` at `:38`. Line-for-line identical to `reference/palace/palace/linalg/operator.cpp:486` (modulo variable rename `D` → `DI`). Cross-witness for the canonical real form.
- `reference/palace/palace/linalg/jacobi.cpp:41-69` — `Apply` complex helper, the **consumer-duplicate** complex site: forward branch `YR[i] = DIR[i] * XR[i] − DII[i] * XI[i]; YI[i] = DII[i] * XR[i] + DIR[i] * XI[i]` at `:57-58` (matches `reference/palace/palace/linalg/operator.cpp:504-505` canonical); transpose branch `YR[i] = DIR[i] * XR[i] + DII[i] * XI[i]; YI[i] = −DII[i] * XR[i] + DIR[i] * XI[i]` at `:66-67` (matches `reference/palace/palace/linalg/operator.cpp:564-565` canonical conjugate variant). Cross-witness for both complex variants. The forward branch is live (called by `JacobiSmoother::Mult`); the transpose branch is dead code under the `MultTranspose → MultHermitianTranspose → Mult` aliasing for real `dinv`, recorded as the dead-code caveat in [`jacobi-smoother`](./jacobi-smoother.md).
- `reference/palace/palace/linalg/jacobi.cpp:74-93` — `JacobiSmoother<OperType>::SetOperator` setup chain: `op.AssembleDiagonal(dinv)` at `:79` (the `assemble-diagonal` step), `dinv.Reciprocal()` at `:80` (the `reciprocal` step — D2 sibling this cycle), and `dinv *= omega` at `:92` (the damping `scal` step). Confirms the `assemble_diagonal → reciprocal → elementwise_product` chain reaches `elementwise_product` last in `Mult`.
- `reference/palace/palace/linalg/chebyshev.cpp:177-178` — `ChebyshevSmoother::SetOperator`: `op.AssembleDiagonal(dinv); dinv.Reciprocal();` setup feeding the `dinv ⊙ r` step inside the polynomial sweep — second downstream consumer of the chain.
- `reference/palace/palace/linalg/chebyshev.cpp:240-241` — `ChebyshevSmoother1stKind::SetOperator`: identical `op.AssembleDiagonal(dinv); dinv.Reciprocal();` setup — third consumer code path of the chain.
- `book/src/L1/jacobi-smoother.md` — the cycle-032 firm L1 entry; the §Dependencies prose at `:289-297` flagged `elementwise_product` (and `reciprocal`) as plain-text forward-references; this entry closes that reference.
- `book/src/L1/assemble-diagonal.md` — the cycle-019 firm L1 entry; the §Dependencies prose at `:73` flagged `elementwise_product` (and `reciprocal`) as "forthcoming L1-primitive candidates, plain text"; this entry closes that reference.
- `book/src/L1/scal.md` — sibling leaf primitive; the broadcast-specialisation relationship `scal(α, x) = elementwise_product(broadcast(α, N), x)` is stated as algebraic law 7 above, not as a dep-map edge.
- `book/src/L1/apply_linop.md` — sibling primitive; the operator-action identity `apply_linop(DiagonalOperator(d), x) = elementwise_product(d, x)` is stated as algebraic law 9 above (the diagonal-operator-action realization rule).
- `book/src/L2/chebyshev-iteration.md:189` — Concepts cross-reference citing `elementwise-product` as "the diagonal-operator apply primitive at L2"; confirms the L1>L2 lift direction (`elementwise_product` is the L1 primitive that the L2 chebyshev-iteration's `dinv ⊙ r` step realises).
- `book/src/concepts/elementwise-product.md` — pre-existing cross-cutting prose treatment; consistent with this L1 entry (background, Palace mapping, L2 role).
- No dedicated `test-elementwise-product` exists in `reference/palace/test/unit/` (search confirms); the operator is exercised indirectly through the diagonal-preconditioner consumer chain (Jacobi/Chebyshev smoothers in `test-libceed.cpp` diagonal-assembly + multigrid integration). Per the `firm-on-positive-structure` precedent, the absent dedicated test does not gate firm — every law is a syntactic identity on the positive multiply lambdas cited above.
```

```edit:book/src/L1/index.md
[NOTE TO INTEGRATOR: this edit-block assumes D2 (`reciprocal`) has already been applied — D2 integrates FIRST in the cycle-033 dispatch ordering. After D2, the §Vocabulary-cohort heading reads `**Firm (24)**`, a new `[reciprocal](./reciprocal.md)` bullet appears immediately after `[jacobi-smoother]`, a new `reciprocal` dep-map row appears after the `[jacobi-smoother]` row, and a new `- [reciprocal](./L1/reciprocal.md)` line appears in SUMMARY after the `jacobi-smoother` line. D3 anchors its inserts on these *post-D2* on-disk lines (i.e. inserts go AFTER the `reciprocal` lines, not after the `jacobi-smoother` lines). If D2 has NOT landed first for some reason, the integrator should reconcile by anchoring on the most stable nearby unique line that still represents "the last L1 vocabulary entry after `jacobi-smoother`" and adjust the count header from its on-disk value upward by one.]

(a) Bump the §Vocabulary-cohort count header:

<<<OLD
**Firm (24)** —
=== NEW
**Firm (25)** —
>>>

(b) Append the `elementwise_product` cohort bullet AFTER the `reciprocal` bullet (which D2 inserted after `jacobi-smoother`). Anchor on D2's `reciprocal`-bullet leading substring (stable across D2's exact prose-to-bullet realization — the bullet starts with the same one-line description from D2's CYCLE.md line 165):

<<<OLD
- [`reciprocal`](./reciprocal.md) — pure-functional elementwise multiplicative-inverse `result[i] = 1/x[i]`.
=== NEW
- [`reciprocal`](./reciprocal.md) — pure-functional elementwise multiplicative-inverse `result[i] = 1/x[i]`.
- [`elementwise_product`](./elementwise_product.md) — pure-functional **Hadamard pointwise product** `result = a ⊙ b`, `result[i] = a[i] · b[i]`; the diagonal-operator-action primitive at L1 (law 9: `apply_linop(DiagonalOperator(d), x) = elementwise_product(d, x)`) and the per-call kernel of the diagonally-scaled-preconditioner cohort (`jacobi-smoother`, `chebyshev-smoother`). Strictly generalises `scal` via broadcast specialisation (`scal(α, x) = elementwise_product(broadcast(α, N), x)`); composes with `reciprocal` (D2 sibling this cycle) to close the `assemble_diagonal → reciprocal → elementwise_product` diagonal-preconditioner chain that `assemble-diagonal` §Dependencies named "forthcoming, plain text". Canonical L0 site is the operator-class `BaseDiagonalOperator<OperType>::Mult` (real `palace/linalg/operator.cpp:486`; complex `:504-505` six-fused-multiply-add) plus the **conjugate variant** `MultHermitianTranspose` (`:564-565` complex-only, three sign flips realising `ā ⊙ b`); the `jacobi.cpp` `Apply` helper (`:30-69`) is a line-for-line consumer duplicate. Two variant axes: element-type (real | complex) × conjugation (straight | conjugate-first-operand, complex-only). Firm-on-positive-structure (the `apply_linop` / `lu_solve` / `back_solve` / `ls_update_column` / `jacobi-smoother` no-dedicated-test precedent): every law is a syntactic identity on positive source. Closes the §Dependencies forward-references in `assemble-diagonal:73` and `jacobi-smoother:289-297`.
>>>

(c) Append the `elementwise_product` dep-map row AFTER the `reciprocal` row (which D2 inserted after the `jacobi-smoother` row per D2's CYCLE.md line 169):

<<<OLD
| [`reciprocal`](./reciprocal.md) | `(x: Tensor[N]) → Tensor[N]` (i.e. elementwise `1/x[i]`) | (leaf; elementwise BLAS-1-shape primitive; partial at `x[i] = 0`) | `firm`
=== NEW
| [`reciprocal`](./reciprocal.md) | `(x: Tensor[N]) → Tensor[N]` (i.e. elementwise `1/x[i]`) | (leaf; elementwise BLAS-1-shape primitive; partial at `x[i] = 0`) | `firm`
| [`elementwise_product`](./elementwise_product.md) | `(a: Tensor[N], b: Tensor[N]) → Tensor[N]` (i.e. `a ⊙ b`; complex conjugation sub-axis: `ā ⊙ b`) | (leaf; sibling to `scal` via broadcast subsumption `scal(α, x) = elementwise_product(broadcast(α, N), x)`; sibling to `apply_linop` via the diagonal-operator-action identity `apply_linop(DiagonalOperator(d), x) = elementwise_product(d, x)`; composes with `reciprocal` co-authored D2) | `firm` (Hadamard pointwise-product primitive; diagonal-operator-action realization; L0: `palace/linalg/operator.cpp:478-507` canonical real+complex straight + `:545-568` complex conjugate variant + `palace/linalg/jacobi.cpp:30-69` consumer-duplicate; harvested cycle-033; firm-on-positive-structure, no-dedicated-test caveat non-gating per `apply_linop` / `jacobi-smoother` precedent; closes the `assemble-diagonal:73` + `jacobi-smoother:289-297` forward-references)
>>>

(Note: the row's match anchors on the leading prefix only — the truncated `firm` cell preserves the dep-map's `| firm (...) |` cell content as D2 lands it; the integrator should treat the OLD as a prefix-anchor and append the NEW row as a fresh line below, not as an in-line replacement.)
```

```edit:book/src/SUMMARY.md
<<<OLD
- [reciprocal](./L1/reciprocal.md)
=== NEW
- [reciprocal](./L1/reciprocal.md)
- [elementwise_product](./L1/elementwise_product.md)
>>>
```

## Operator content

(The full chapter body is authored in the `new:book/src/L1/elementwise_product.md` proposed-changes block above. Key elements:)

- **Slug + one-line**: `elementwise_product` — pure elementwise (Hadamard) pointwise product `(a, b) → a ⊙ b`, `result[i] = a[i] · b[i]`. Diagonal-operator-action primitive at L1.
- **Signature**: `elementwise_product :: (a: Tensor[N], b: Tensor[N]) -> Tensor[N]`, defined as `a ⊙ b`. Shape contracts on `(a, b, result)` all sharing axis `N` and element type. Conjugate variant `elementwise_product_conj` (complex-only) modeled as a conjugation sub-axis.
- **Semantics**: element-local, reduction-free, no MPI collective, no destination-buffer mention. Complex multiplication is the standard six-FMA per element; conjugate variant flips three signs on cross-terms.
- **Algebraic laws** (10 — all syntactic identities on positive source):
  1. Commutativity (straight only).
  2. Associativity.
  3. Identity in all-ones.
  4. Absorption in all-zeros.
  5. Distributivity over vector addition.
  6. Scalar absorption (compatibility with `scal`).
  7. Broadcast subsumption of `scal`.
  8. Negation.
  9. **Diagonal-operator-action identity** — the defining identity at the canonical L0 site: `apply_linop(DiagonalOperator(d), x) = elementwise_product(d, x)`.
  10. Conjugation involution (conjugate variant, complex only).
- **Non-laws explicitly recorded**: idempotence, full multiplicative inverse, commutativity-of-conjugate-variant, distributivity-over-inner-products (out-of-type), bit-level reordering (vacuous — reduction-free).
- **Variant axes**: element-type (real | complex), conjugation sub-axis (straight | conjugate-first-operand, complex-only). Two non-axes recorded (no constant-folding, no operator-action-vs-free-binary at L1; dead-code conjugate `jacobi.cpp:61-69` caveat).
- **Dependencies**: none at L1 (leaf primitive). Sibling subsumption relations stated as algebraic laws to `scal` (law 7), `apply_linop` (law 9), `reciprocal` (D2 sibling). Downstream consumers cited at L1 (`jacobi-smoother`, `chebyshev-smoother`, `assemble-diagonal`) and L2 (`chebyshev-iteration`).
- **Status**: `firm` — firm-on-positive-structure (`apply_linop` / `lu_solve` / `back_solve` / `ls_update_column` / `jacobi-smoother` no-dedicated-test precedent). L1>L0 mutation-rotation theme forthcoming (plain-text forward-reference).
- **Evidence**: every cited line verified via `tools/citecheck/citecheck.py --anchor` against the on-disk file.

## Supporting evidence

Verified-against-source citation manifest (all confirmed via `tools/citecheck/citecheck.py --anchor`):

| Citation | Anchor | Verification |
|---|---|---|
| `reference/palace/palace/linalg/operator.cpp:478-487` | `Y[i] = D[i] * X[i]` | ok @ :486 |
| `reference/palace/palace/linalg/operator.cpp:489-507` | `YR[i] = DR[i] * XR[i] - DI[i] * XI[i]` | ok @ :504 |
| `reference/palace/palace/linalg/operator.cpp:545-568` | `YR[i] = DR[i] * XR[i] + DI[i] * XI[i]` | ok @ :564 |
| `reference/palace/palace/linalg/operator.hpp:256-289` | `class BaseDiagonalOperator` | ok @ :257 |
| `reference/palace/palace/linalg/jacobi.cpp:30-39` | `Y[i] = DI[i] * X[i]` | ok @ :38 |
| `reference/palace/palace/linalg/jacobi.cpp:41-69` | `YR[i] = DIR[i] * XR[i] - DII[i] * XI[i]` | ok @ :57 |

Sibling chapter citations cross-checked from on-disk reads (line numbers confirmed against current files):

- `book/src/L1/assemble-diagonal.md:73` — §Dependencies forward-reference to `reciprocal` / `elementwise_product` (this entry closes it).
- `book/src/L1/jacobi-smoother.md:289-297` — §Dependencies forward-reference to `elementwise_product` (this entry closes it).
- `book/src/L2/chebyshev-iteration.md:189` — Concepts cross-reference to `concepts/elementwise-product.md`.
- `book/src/concepts/elementwise-product.md` — pre-existing cross-cutting prose page (consistent with this L1 entry).

Cross-references to firm sibling primitives:

- `book/src/L1/scal.md` — broadcast-subsumption law 7.
- `book/src/L1/apply_linop.md` — diagonal-operator-action identity law 9.
- `book/src/L1/axpy.md` / `axpby.md` / `axpbypcz.md` — linear-combination cohort siblings.

## Open questions / caveats

1. **L1>L0 mutation-rotation theme not yet authored.** This entry forward-references `elementwise-product-mutation-rotation` (plain-text). The theme is mechanical (destination-binding `y = a ⊙ b` → output-arg `forall_switch` per-element kernel writing `Y[i] = A[i] * B[i]`), close in shape to the existing `dot-mutation-rotation` and `assemble-diagonal-mutation-rotation`. Recommend cycle-planner queues this as a low-cost L1>L0 follow-up to materialize the chain end-to-end.

2. **Single primitive with conjugation variant axis vs. two primitives — verdict.** The dispatch posed the question whether the complex conjugate-multiply (`MultHermitianTranspose`, `ā ⊙ b`) warrants a separate L1 primitive (`complex_elementwise_multiply` or `elementwise_product_conj`). The judgement landed in this entry is **one primitive with a conjugation sub-axis on the complex element-type**, justified on the operator's own terms (not by precedent): (a) the L0 kernels differ only in three sign flips on cross-terms — the per-element operation's *identity* is "elementwise multiplication", parameterised by which operand is conjugated; (b) the law catalog absorbs the variant cleanly — the eight non-conjugation-sensitive laws (commutativity-of-straight-form, associativity, all-ones identity, all-zeros absorption, distributivity, scalar absorption, broadcast subsumption of `scal`, negation) are **identical** between straight and conjugate variants; the conjugation-specific facts surface as one law (law 10, involution) plus one non-law (broken commutativity in the conjugate variant). Splitting into two primitives would duplicate those eight laws verbatim for negligible gain. *Note on precedent*: this convention differs from the on-disk `book/src/L1/dot.md:16-20,:94` model, where `dot` and `tdot` are **two distinct co-housed operators** sharing only the reduction skeleton (their laws genuinely diverge — `dot` is positive semi-definite at `y = x`, `tdot` is not). For `elementwise_product` the law overlap is much larger, so the sub-axis modeling is appropriate; `dot`/`tdot` is **not** the precedent for it. Confidence: high.

3. **D2 (`reciprocal`) live-link resolution.** This entry treats `reciprocal` as a live link `[`reciprocal`](./reciprocal.md)` because D2 is authoring it in parallel this cycle. If D2 lands first at integration time, the link resolves; if not, the integrator's per-report serial dispatch ordering applies — when this entry is applied before D2's, `mdbook-linkcheck2` will hard-fail. **Mitigation**: the integrator should apply both reports in the same finalize cycle (cycle-033) so both files land before the build runs. If only one lands per the per-report-dispatch ordering, the integrator may need to (a) downgrade the `[`reciprocal`](./reciprocal.md)` references in this entry to plain `` `reciprocal` `` inline code, or (b) create a `stub` for `reciprocal` per the **Integration may materialize implied components as stubs** invariant. The four references to `reciprocal` in this entry are: §Context (twice), §Dependencies, §Algebraic-laws (non-law of multiplicative inverse). Recommendation: apply both reports (D2 + D3) in the same finalize pass — same-cycle batch ordering is the natural solution.

4. **Forthcoming downstream consumers.** The `assemble_diagonal → reciprocal → elementwise_product` chain closes the diagonal-preconditioner-apply pattern for **Jacobi** and **Chebyshev**. Roadmap §Intermediate names block-Jacobi and polynomial preconditioners as reusing the chain. When those land, they will each compose two `elementwise_product` calls per inner step (one for the inverse-diagonal scaling, one for the polynomial-update fused multiply); the in-block-Jacobi variant axis (real-block / complex-block / block-size) is orthogonal to the elementwise-product semantics. Cross-reference recorded; no proposed-change to this entry.

5. **Concepts page does not need extension.** `book/src/concepts/elementwise-product.md` already covers the background, contract, role in higher layers, and Palace mapping. Its summary that "Palace's Jacobi/Chebyshev smoothers use the precomputed-diagonal reciprocal pattern" is consistent with this firm L1 entry. No edits proposed.

6. **Layer intro refresh — minimal.** The L1 vocabulary cohort line `## Vocabulary cohort` currently reads `**Firm (23)** — element-wise updates...`. With this entry (+`reciprocal` from D2 in parallel) the count becomes 24 + 1 = 25 firm operators. The cohort prose mentions "the diagonal-preconditioner-apply Jacobi smoother" in the long list; the §Vocabulary-cohort prose plus the §Working-Notes line on the chain may want a layer-intro-author refresh to mention `elementwise_product` and `reciprocal` as the closing-the-chain primitives. Not blocking — this entry's §Context and the consumer chapters' existing forward-references already carry the load. Flag for next layer-intro-author pass; not surfaced as a hard open question.

7. **Confidence note on law 9 (diagonal-operator-action identity).** Law 9 — `apply_linop(DiagonalOperator(d), x) = elementwise_product(d, x)` — is the *defining identity* of the canonical L0 site, so it is unconditionally firm. But it composes nicely with `assemble-diagonal`'s law set to close a round-trip: `apply_linop(DiagonalOperator(assemble_diagonal(A)), x) = elementwise_product(assemble_diagonal(A), x)` — i.e. "build the diagonal-operator-from-diagonal, apply it, get the elementwise product against the diagonal". This round-trip would be the natural law to record in a future `assemble-diagonal` refresh as a cross-operator identity. Not blocking; flagged for the next `assemble-diagonal` editing pass.
