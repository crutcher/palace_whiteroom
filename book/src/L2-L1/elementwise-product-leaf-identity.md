# elementwise-product-leaf-identity

The L2>L1 lowering theme for the Hadamard binary product leaf `elementwise_product`. The rewrite is
**identity-in-form on the leaf**: the L2 [`elementwise_product`](../L2/elementwise_product.md) floor
lowers to the L1 [`elementwise_product`](../L1/elementwise_product.md) primitive with the same
signature `(Tensor[N], Tensor[N]) -> Tensor[N]`, the same per-element `result[i] = a[i]·b[i]`
semantics, the same ten algebraic laws, and the same two variant axes (element-type + conjugation
sub-axis on the complex side) — value-thread-isomorphic on the primitive. Like
[`reciprocal-leaf-identity`](./reciprocal-leaf-identity.md) and unlike the cycle-041 fold-member
BLAS-1 floor edges, `elementwise_product` is **fork-INDEPENDENT — it has NO fold-parent**: it is a
binary `(Tensor[N], Tensor[N]) -> Tensor[N]` field operation, neither the length-axis fold
`inner_product` (reduce-to-`Scalar`) nor the term-axis fold `linear_combination`
(reduce-to-`Tensor[N]`). So there is no fusion to defer (the L0 `forall_switch` per-element multiply is
already the unfolded single-pass form). This theme records the identity edge; it is the L2>L1 analogue
of the L3>L2 [`elementwise_product-body-identity`](../L3-L2/elementwise_product-body-identity.md) (the
other thin edge of the same leaf).

## Slug

`elementwise-product-leaf-identity`

## Context

`elementwise_product` at L2 is the **floor** entry (`book/src/L2/elementwise_product.md`, harvested
cycle-042 D3): the standalone Hadamard binary field operation, the diagonal-operator-apply primitive,
rendered as its own same-named L2 chapter so the firm L3
[`elementwise_product`](../L3/elementwise_product.md) (cycle-038) leaf rests on an adjacent same-named
L2 parent (per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels**)
rather than skipping a layer to L1. This theme is the L2>L1 edge of that floor.

The edge is the **identity-in-form** case: the L2 `elementwise_product` floor and the L1
`elementwise_product` leaf are value-thread-isomorphic on the primitive. This is the L2>L1 analogue of
the L3>L2 [`elementwise_product-body-identity`](../L3-L2/elementwise_product-body-identity.md) theme
(the other thin edge of the same leaf).

**Why this edge is identity AND fork-independent (the distinction from `dot-leaf-identity`).** The
cycle-041 `dot-leaf-identity` is identity-in-form *because* all its L2-layer fusion content is carried
by the fold-parent `inner-product-fold-specialization` — the leaf's own edge is left a no-op with a
deferring note. `elementwise_product` has **no fold-parent at all** (the D3 report establishes this
exhaustively: it is a binary field operation consuming two full-length operands and producing a
full-length result, with no fold skeleton — no reduction to a scalar, no variadic term list to
accumulate). The closest relationship is the *inverse* subsumption with `scal`
(`scal(α, x) = elementwise_product(broadcast(α, N), x)`; D3 law 7) — `elementwise_product` strictly
*generalises* `scal`, which is a sibling-subsumption identity, **not** a fold membership. So there is
nothing to defer to — and nothing to defer: `elementwise_product` is a leaf binary field operation
with **no multi-operation kernel fusion to unfold** (the L0 `forall_switch` per-element multiply —
real single-multiply `Y[i] = D[i]*X[i]`, complex six-multiply-add, conjugate two-sign-flip variant —
is already the unfolded single-pass form). The leaf's edge is therefore the pure identity with no
fusion-deferral note.

## L2 form (LHS)

The L2 form is the `elementwise_product` floor (`book/src/L2/elementwise_product.md` §Signature,
harvested cycle-042 D3) — the mutation-free Hadamard binary product, parameterised by element type:

    elementwise_product :: (a: Tensor[N], b: Tensor[N]) -> Tensor[N]
    elementwise_product(a, b) = a ⊙ b               -- result[i] = a[i] · b[i]

with the conjugate variant (complex element-type only) as a sub-axis (NOT a separate primitive):

    elementwise_product_conj :: (a: ComplexTensor[N], b: ComplexTensor[N]) -> ComplexTensor[N]
    elementwise_product_conj(a, b) = ā ⊙ b

The L2 form is **pure / out-of-place** (no destination buffer; the result is a fresh tensor with the
same axis `N` and element type as the operands). `a` and `b` must share the length axis and the element
type. The in-place output-arg mutation idiom (`Y[i] = D[i]·X[i]` writing through the `y` output
argument of `BaseDiagonalOperator::Mult`), the operator-class wrapping, the consumer-local inline
duplicate (`jacobi.cpp` `Apply`), and the `forall_switch` host/device dispatch are NOT in the L2
signature — they reappear only at the substantive L1>L0 rotation
([`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md)
sub-pattern B).

## L1 form (RHS)

The L1 form is the firm `elementwise_product` leaf primitive (`book/src/L1/elementwise_product.md`
§Signature, firm cycle-019/032/036) — identical in signature, semantics, laws, and variant axes:

    elementwise_product :: (a: Tensor[N], b: Tensor[N]) -> Tensor[N]
    elementwise_product(a, b) = a ⊙ b               -- same per-element kernel; same conjugation sub-axis

The L1 leaf is the **mutation-rotation** rendering: it already erases the L0 output-arg destination
mutation (the L1 form takes `a, b` as values and returns a fresh result), unwraps the operator-class
(the `BaseDiagonalOperator` wrapping; the operator-action form is recovered as L1 law 9
`apply_linop(DiagonalOperator(d), x) = elementwise_product(d, x)`), erases the consumer-local
inline-duplication (`jacobi.cpp` `Apply`), and folds the `forall_switch` dispatch into the L1>L0
lowering. The L1 entry is authoritative on every Palace-surface fact (the canonical
`BaseDiagonalOperator::Mult` site, the `MultHermitianTranspose` conjugate variant, the `jacobi.cpp`
inline consumer duplicate, the absence of any free-function `linalg::ElementwiseProduct` symbol, the
ten algebraic laws, the complete L0 evidence list); the L2 form does not duplicate them.

## The rewrite (L2 → L1)

The rewrite is the **identity on the leaf**. Every L2 binding maps to the same L1 binding at the same
position:

    | L2 floor (`L2/elementwise_product`)            | L1 leaf (`L1/elementwise_product`)             | Mapping  |
    |------------------------------------------------|------------------------------------------------|----------|
    | `elementwise_product :: (a, b) -> Tensor[N]`   | `elementwise_product :: (a, b) -> Tensor[N]`   | Identity. Same binary signature shape. |
    | `elementwise_product(a, b) = a ⊙ b`            | `elementwise_product(a, b) = a ⊙ b`            | Identity. Same per-element multiply `result[i] = a[i]·b[i]`. |
    | conjugate variant `elementwise_product_conj`   | conjugate variant `elementwise_product_conj`   | Identity. Same `ā ⊙ b` complex-side sub-axis. |
    | algebraic laws 1–10                            | algebraic laws 1–10                            | Identity. Inherited unchanged (commutativity, associativity, all-ones identity, all-zeros absorption, distributivity, scalar absorption, broadcast-subsumption-of-`scal`, negation, diagonal-operator-action identity, conjugation involution). |
    | two variant axes: element-type + conjugation   | two variant axes: element-type + conjugation   | Identity. Real/complex collapsed; conjugation sub-axis on the complex side. |

There is **no L2 binding without an L1 partner and no L1 binding without an L2 partner**; the mapping
is total and bijective on the leaf. This is the identity-in-form property.

**No fusion-deferral note (the fork-independence consequence).** Unlike `dot-leaf-identity`, this
theme has no fold-parent to defer fusion to — and no fusion to defer. The L0 `forall_switch`
per-element multiply pass (canonical `BaseDiagonalOperator::Mult` real `Y[i] = D[i]*X[i]`, complex
six-multiply-add, conjugate `MultHermitianTranspose` two-sign-flip) is already the unfolded single-pass
form. The L2>L1 edge therefore carries no de-fusion treatment; the substantive content (destination
buffer, operator-class unwrapping, consumer-duplicate erasure, device dispatch) is reintroduced only at
the L1>L0 rotation (sub-pattern B).

## Applicability conditions

The identity rewrite is valid when:

1. **`elementwise_product` is treated as a standalone binary leaf, not decomposed.**
   `elementwise_product` does not decompose into other L2 primitives — the Hadamard binary multiply is
   a single field operation; its sub-operation (per-element scalar multiplication of two operand
   vectors) is below the L2 layer's resolution. It has **no fold-parent** (fork-INDEPENDENT; the D3
   report establishes this: a binary `(Tensor[N], Tensor[N]) -> Tensor[N]` field op, neither
   reduce-to-`Scalar` nor a variadic term-fold), so — unlike `dot-leaf-identity` (Applicability
   condition 1, which presupposes the leaf-floor-vs-fold-only design fork) — there is **no
   design-fork presupposition** here. The leaf-vs-fold fork does not touch this fork-independent leaf
   (see §Status).

2. **The leaf is value-thread-isomorphic across the edge.** The L2 `elementwise_product` floor and the
   L1 `elementwise_product` leaf share the binary signature, the per-element multiply, the ten
   algebraic laws, and the two variant axes (element-type + conjugation sub-axis). Confirmed by
   construction: `L2/elementwise_product` is authored as a thin floor entry whose laws are inherited
   unchanged from `L1/elementwise_product` (D3 §"Algebraic laws", §Signature).

3. **No fold-level fusion to defer; the per-element pass is already unfolded.** No multi-operation
   kernel fusion is unique to (or present on) the `elementwise_product` leaf; the L0 `forall_switch`
   per-element multiply is the unfolded single-pass form (contrast `dot-leaf-identity`, whose fusion
   content IS the fold-parent's). The leaf's edge is therefore the identity with no fusion-deferral
   note.

## Justification kind

**`structural`** (dominant) with secondary **`empirical-match`**.

**Structural (dominant)**: the L2 `elementwise_product` floor's signature shape
(`(a: Tensor[N], b: Tensor[N]) -> Tensor[N]`) is identical to the L1 leaf's signature shape — a
whole-tensor binary field operation with no element loop exposed at either layer. The rotation between
two value-thread-isomorphic leaves with identical signatures is the identity by construction; there is
no fold-parent fusion content to defer and no leaf-unique fusion, so the leaf's own edge is a no-op.

**Empirical-match (secondary)**: the L1 leaf is firm on direct Palace evidence
(`L1/elementwise_product` §Evidence: the canonical `BaseDiagonalOperator::Mult` real
`palace/linalg/operator.cpp:478-487` / complex `:489-507` sites, the conjugate `MultHermitianTranspose`
`:545-568`, the `jacobi.cpp` consumer duplicate), and the L2 floor was authored (D3) as
value-thread-isomorphic to it; the two forms agree on every law and both variant axes by independent
transcription. The identity is observational on the two firm/firming chapters, not derivational.

## Speculative L1 operators

**None.** Both endpoints are existing vocabulary: the L2 LHS is the `elementwise_product` floor
(firming cycle-042 D3), the L1 RHS is the firm `elementwise_product` leaf (firm cycle-019/032/036
chain). This theme is the identity edge between existing chapters; it proposes no new operators.

One evidentiary caveat carries over unchanged from the leaves (NOT a status reduction — the identity
structure is firm):

- **Conjugate-variant consumer duplicate is dead code (recognition rule).** The consumer-local
  `Apply<Transpose=true>` complex kernel (`palace/linalg/jacobi.cpp:61-69`) is unreachable under
  Palace's symmetric `MultTranspose → Mult` wiring (`jacobi.hpp:43`); the canonical
  `MultHermitianTranspose` (`palace/linalg/operator.cpp:545-568`) is live. The conjugation variant axis
  IS live at the canonical site; the identity edge maps it identity-in-form regardless of the
  consumer-duplicate dead branch (per `reciprocal-elementwise-product-mutation-rotation` §Status
  caveats). Not a status reduction.

## Verified-against

L2 / L1 anchors (the two endpoints):

- `book/src/L2/elementwise_product.md` (firming cycle-042 D3) — the L2 floor (LHS): the standalone
  Hadamard binary field operation, value-thread-isomorphic to the L1 leaf, ten laws + two variant axes
  inherited unchanged, fold-parent NONE (fork-INDEPENDENT). (The chapter lands at this cycle's
  integration alongside this theme — wave-2 serial sequencing applies D3 before this theme.)
- `book/src/L1/elementwise_product.md` (firm cycle-019/032/036) — the L1 leaf (RHS): the binary
  signature, the per-element kernel, the conjugation sub-axis (§Variant axes), the ten algebraic laws
  (the diagonal-operator-action law 9, the `scal` broadcast-subsumption law 7), the complete L0
  evidence list. Authoritative on every Palace-surface fact.
- `book/src/L3-L2/elementwise_product-body-identity.md` (firm cycle-042 D10) — the sibling L3>L2 edge
  of the same leaf (the other thin edge); co-dispatched this cycle.
- this L2>L1 leaf-identity edge composes with the firm L1>L0
  `book/src/L1-L0/reciprocal-elementwise-product-mutation-rotation.md` (firm) — the **substantive**
  rotation in the chain (sub-pattern B), which reintroduces the L0 output-arg destination mutation, the
  operator-class wrapping, the consumer-duplicate kernel, the conjugation kernel-template choice, and
  the device dispatch this identity edge abstracts away.

L0 evidence (transitive through the firm L1 leaf; self-verified via `tools/citecheck/citecheck.py
--anchor` this invocation, all `[ok]`; paths relative to `reference/palace/`):

- `palace/linalg/operator.cpp:478-487` — real canonical `BaseDiagonalOperator<Operator>::Mult`, the
  per-element body `Y[i] = D[i] * X[i]` at `:486`. **Self-verified (anchor `Mult` @479; `Y[i] = D[i] *
  X[i]` @486).** Inherited transitively; the leaf's edge is identity so no new L0 claim is made here.
- `palace/linalg/operator.cpp:545-568` — complex conjugate-variant canonical
  `DiagonalOperatorHelper<…>::MultHermitianTranspose`, the two-sign-flip kernel realising `d̄ ⊙ x`.
  **Self-verified (anchor `MultHermitianTranspose` @548).** Witnesses the conjugation sub-axis.

## Status

`firm` — the L2 LHS is the firm-this-cycle floor (D3), the L1 RHS is the firm `elementwise_product`
leaf (cycle-019/032/036), and the rotation between two value-thread-isomorphic leaves with identical
binary signatures is the identity by construction (§"The rewrite (L2 → L1)" table is total and
bijective on the leaf). `elementwise_product` is a **standalone binary field operation — fork-INDEPENDENT,
NO fold-parent** — there is no fold-level fusion content to defer (contrast `dot-leaf-identity`) and no
leaf-unique fusion; the L0 `forall_switch` per-element multiply is already the unfolded single-pass
form. No speculative operator, no negative-anchor reconstruction, no literature inference.

> **Design-final on the leaf-vs-fold fork (NOT a presupposition, unlike the BLAS-1-floor themes).**
> The batch-12 meta-phase fork `dot-l2-leaf-floor-vs-fold-only-design` concerns whether the L2 BLAS-1
> *fold-member* leaves (`dot`, `scal`) are same-named floors or are absorbed into their fold-parents.
> **`elementwise_product` has no fold-parent** (it is the inverse-subsumption *generalisation* of
> `scal`, not a fold member), so neither the (a) fold-only nor the (b) same-named-floor reading
> re-anchors it — its L2 floor can only ever be a standalone same-named leaf. This theme is therefore
> *design-final*, not presuppositional: unlike `dot-leaf-identity` (whose §Status carries a
> design-presupposition note), this theme's identity claim does not depend on the fork's outcome.
