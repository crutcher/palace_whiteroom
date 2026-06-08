# elementwise_product

Pure elementwise (Hadamard) pointwise product `result = a ⊙ b`, defined by `result[i] = a[i] · b[i]` for `i ∈ [0, N)`. The diagonal-operator-action primitive at L1, and the per-call kernel of the diagonally-scaled-preconditioner cohort (`jacobi-smoother`, `chebyshev-smoother`, block-Jacobi).

## Context

`elementwise_product` lifts Palace's elementwise pointwise-multiply kernel from the diagonal-operator method form (the canonical site: `BaseDiagonalOperator<OperType>::Mult` writing `y[i] = d[i] · x[i]` at `palace/linalg/operator.cpp:478-487` real and `:489-507` complex, plus the conjugate-transpose variant at `:545-568`) and from one inline consumer duplicate (`palace/linalg/jacobi.cpp:30-39` real, `:41-69` complex) to a single pure-functional binary operator. The L0 surface mutates the output destination buffer (`Y[i] = D[i] * X[i]` in the real case; six fused multiply-adds across `(YR, YI)` in the complex case); the L1 form drops the destination-buffer mention — the operator consumes the prior values of `a` and `b` and produces a fresh result vector.

There is no free-function `linalg::ElementwiseProduct` / `linalg::Hadamard` symbol in Palace — the operation surfaces exclusively as **the action of a `BaseDiagonalOperator` against a vector** (the canonical site) and as **inline consumer-local duplicates** of the same kernel (`jacobi.cpp`). The conceptual decoupling at L1 — `elementwise_product(a, b)` as a free binary operator independent of either operand being the "diagonal of an operator" — is the L1 abstraction over an L0 surface that has only the operator-method form. It is the final step of the `assemble_diagonal → reciprocal → elementwise_product` chain that [`assemble-diagonal`](./assemble-diagonal.md) names.

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

The operator is pure at L1: the prior `a`, the prior `b`, and the new `result` are distinct values. The L0 source overwrites the in-place destination buffer; the `elementwise-product-mutation-rotation` L1>L0 lowering theme is where that overwrite is reintroduced. At L1 the relationship is purely algebraic.

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

None at L1. `elementwise_product` is a **leaf primitive** at L1 — the diagonal-operator-action / Hadamard-product floor of the elementwise vocabulary, sibling to [`scal`](./scal.md) (scalar broadcast specialisation), [`axpy`](./axpy.md) / [`axpby`](./axpby.md) / [`axpbypcz`](./axpbypcz.md) (linear-combination cohort), and [`reciprocal`](./reciprocal.md) (the elementwise-inverse sibling). Its sub-operation is the per-element scalar multiplication of two operand vectors, at the L1 layer's resolution.

Sibling subsumption (not dependency):

- `scal(α, x) = elementwise_product(broadcast(α, N), x)` — `elementwise_product` strictly generalises `scal` (broadcast specialisation); both stay in the L1 dep-map as siblings.
- `apply_linop(DiagonalOperator(d), x) = elementwise_product(d, x)` — law 9; `elementwise_product` is the realization of the diagonal-operator action. Both stay as siblings: `apply_linop` is opaque-operator-and-vector-to-vector; `elementwise_product` is vector-and-vector-to-vector with no operator argument.
- `reciprocal(a)` — composes with `elementwise_product` to form the `assemble_diagonal → reciprocal → elementwise_product` diagonal-preconditioner chain (`jacobi-smoother`, `chebyshev-smoother`, block-Jacobi).

Downstream consumers at L1 (cross-reference, not reverse-dependencies):

- [`jacobi-smoother`](./jacobi-smoother.md) — the apply body is one elementwise product: `y = dinv_ω ⊙ x`, realised by the local `Apply` helper at `palace/linalg/jacobi.cpp:30-39` (real) and `:41-69` (complex). The smoother's defining lightness is *one elementwise product, no `apply_linop` call*.
- [`chebyshev-smoother`](./chebyshev-smoother.md) — the diagonally-scaled polynomial sweep uses `dinv ⊙ r` per inner step (`palace/linalg/chebyshev.cpp:177-178,240-241` setup), then `DiagonalOperator(dinv)` realised through the same `BaseDiagonalOperator<Operator>::Mult` canonical site.
- [`assemble-diagonal`](./assemble-diagonal.md) — the `assemble_diagonal → reciprocal → elementwise_product` chain head.
- L2 [`chebyshev-iteration`](../L2/chebyshev-iteration.md) — Concepts cross-reference §:189 cites `elementwise-product` as "the diagonal-operator apply primitive at L2".

## Variant axes

`elementwise_product` has two orthogonal variant axes at L1:

- **element-type**: `real` | `complex`. The L0 source separates these into the two parallel template specialisations — real `BaseDiagonalOperator<Operator>::Mult` at `palace/linalg/operator.cpp:478-487` (per-element single multiply `Y[i] = D[i] * X[i]`) and complex `BaseDiagonalOperator<ComplexOperator>::Mult` at `palace/linalg/operator.cpp:489-507` (per-element six-multiply-add complex product). At L1 these collapse to one operator parameterised by element type — the per-element semantics is "multiplication in the underlying field"; the field is `ℝ` or `ℂ`.

- **conjugation** (sub-axis on the complex element-type): `straight (a ⊙ b)` | `conjugate-first-operand (ā ⊙ b)`. The L0 source materialises the straight form as `Mult` (`reference/palace/palace/linalg/operator.cpp:489-507`) and the conjugate form as `MultHermitianTranspose` (`reference/palace/palace/linalg/operator.cpp:545-568`, complex-only, three sign flips on the cross-terms). At L1 this is a structural variant axis (which call form), not a value branch — both forms are exhaustively defined per element. The real element-type does **not** carry this axis (real conjugation is identity); the L0 real `MultTranspose` aliases to `Mult` per `reference/palace/palace/linalg/operator.hpp:279`. The conjugate variant breaks commutativity (non-law above) and changes the conjugation-involution law (law 10), but preserves associativity (in the bilinear sense `elementwise_product(ā, b ⊙ c)`), the all-ones identity (with the convention `𝟙̄ = 𝟙`), the all-zeros absorption, and distributivity over addition. *Variant-axis decision rationale*: kept as one axis with two values rather than as two distinct primitives (`elementwise_product` vs. `complex_elementwise_multiply_conj`) because the conjugation differs only in three sign flips on cross-terms — the operator's identity is "elementwise multiplication" in both cases, parameterised by which operand (if any) is conjugated. This is justified on the operator's own terms: the eight non-conjugation-sensitive laws (commutativity in the straight form, associativity, all-ones identity, all-zeros absorption, distributivity, scalar absorption, broadcast subsumption of `scal`, negation) are **identical** between straight and conjugate variants — the conjugation only modifies the commutativity (broken) and adds the involution law (law 10). Splitting into two primitives would duplicate eight laws verbatim for negligible gain. (Note: this is a *different* convention than `dot` / `tdot`, where on-disk `book/src/L1/dot.md:16-20,:94` treats them as **two distinct operators co-housed in one chapter** — they share only the reduction skeleton and their algebraic laws genuinely differ (e.g. `dot` is positive semi-definite at `y = x`, `tdot` is not). For `elementwise_product` the algebraic-law overlap is much larger and the variant is a true sub-axis, hence the different modeling choice.)

Non-axes (recorded for disambiguation):

- **constant-folding on `a` or `b`**: not an axis — the L0 source has no constant-folding branches (unlike `axpy`'s `α == 1.0` fast path or `scal`'s `imag(s) == 0.0` complex-shape specialisation). The canonical and consumer per-element kernels are uniform multiplies (`forall_switch` over `N`). Constant-folding cases (`a = 𝟙`, `a = 𝟘`) are absorbed into the algebraic laws above.
- **operator-action vs. free binary**: not an axis at L1 — the canonical L0 site is the operator-action form (`DiagonalOperator::Mult`), and Palace has no free-binary `linalg::ElementwiseProduct` symbol; but the L1 abstraction lifts the kernel out of the operator-action wrapper into a free binary primitive on two equally-shaped vectors. The operator-action form is **recovered** algebraically by law 9 (`apply_linop(DiagonalOperator(d), x) = elementwise_product(d, x)`); the recovery is an algebraic identity, not a variant.
- **dead-code conjugate path**: `palace/linalg/jacobi.cpp:61-69` (the `Transpose = true` complex `Apply` template instantiation inside `jacobi.cpp`) is **unreferenced** in Palace because `JacobiSmoother::MultTranspose` aliases to `MultHermitianTranspose` which aliases through to `Mult` for the real-`dinv` smoother. It is recorded as a dead-code caveat in [`jacobi-smoother`](./jacobi-smoother.md). The canonical `BaseDiagonalOperator<ComplexOperator>::MultHermitianTranspose` at `reference/palace/palace/linalg/operator.cpp:545-568` IS live (called whenever a diagonal operator's Hermitian-transpose action is needed) — so the conjugation axis is not dead at the canonical site even though one specific consumer's copy of it is.

## Downward to L0

The `elementwise-product-mutation-rotation` L1>L0 mutation-rotation theme reintroduces the destination buffer. The dominant rewrite pattern is the same destination-binding rule as `dot-mutation-rotation` and `assemble-diagonal-mutation-rotation`: an output-arg `y = a ⊙ b` at L1 lowers to a `forall_switch` per-element kernel writing `Y[i] = A[i] * B[i]` at L0 with the destination buffer reintroduced. Every law is a syntactic identity on the positive per-element multiply lambdas (firm-on-positive-structure; the absent dedicated `test-elementwise-product` test does not gate firm).

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
- `reference/palace/palace/linalg/jacobi.cpp:74-93` — `JacobiSmoother<OperType>::SetOperator` setup chain: `op.AssembleDiagonal(dinv)` at `:79` (the `assemble-diagonal` step), `dinv.Reciprocal()` at `:80` (the `reciprocal` step), and `dinv *= omega` at `:92` (the damping `scal` step). Confirms the `assemble_diagonal → reciprocal → elementwise_product` chain reaches `elementwise_product` last in `Mult`.
- `reference/palace/palace/linalg/chebyshev.cpp:177-178` — `ChebyshevSmoother::SetOperator`: `op.AssembleDiagonal(dinv); dinv.Reciprocal();` setup feeding the `dinv ⊙ r` step inside the polynomial sweep — second downstream consumer of the chain.
- `reference/palace/palace/linalg/chebyshev.cpp:240-241` — `ChebyshevSmoother1stKind::SetOperator`: identical `op.AssembleDiagonal(dinv); dinv.Reciprocal();` setup — third consumer code path of the chain.
- `book/src/L1/jacobi-smoother.md` — firm L1 entry; its §Dependencies names `elementwise_product` (and `reciprocal`) as the chain constituents this entry defines.
- `book/src/L1/assemble-diagonal.md` — firm L1 entry; the head of the `assemble_diagonal → reciprocal → elementwise_product` chain.
- `book/src/L1/scal.md` — sibling leaf primitive; the broadcast-specialisation relationship `scal(α, x) = elementwise_product(broadcast(α, N), x)` is stated as algebraic law 7 above, not as a dep-map edge.
- `book/src/L1/apply_linop.md` — sibling primitive; the operator-action identity `apply_linop(DiagonalOperator(d), x) = elementwise_product(d, x)` is stated as algebraic law 9 above (the diagonal-operator-action realization rule).
- `book/src/L2/chebyshev-iteration.md:189` — Concepts cross-reference citing `elementwise-product` as "the diagonal-operator apply primitive at L2"; confirms the L1>L2 lift direction (`elementwise_product` is the L1 primitive that the L2 chebyshev-iteration's `dinv ⊙ r` step realises).
- `book/src/concepts/elementwise-product.md` — pre-existing cross-cutting prose treatment; consistent with this L1 entry (background, Palace mapping, L2 role).
- No dedicated `test-elementwise-product` exists in `reference/palace/test/unit/` (search confirms); the operator is exercised indirectly through the diagonal-preconditioner consumer chain (Jacobi/Chebyshev smoothers in `test-libceed.cpp` diagonal-assembly + multigrid integration). Per the `firm-on-positive-structure` precedent, the absent dedicated test does not gate firm — every law is a syntactic identity on the positive multiply lambdas cited above.

## Status

`firm` — canonical operator-action signature with direct source evidence; the algebraic laws are standard properties of pointwise multiplication.
