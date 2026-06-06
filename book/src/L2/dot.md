# dot

> **Specialization-stub (reduced cycle-052 D3, vocabulary-shift-redirect refactor pass).**
> `dot` at L2 is the **`M = I` Hermitian/symmetric specialization** of the fold combinator
> [`inner_product`](./inner_product.md) (firm cycle-050) — the combinator IS the L2 entry for
> the reduce-to-scalar inner-product family; `dot` is a **specialization note** under it
> (per CLAUDE.md §Methodology invariants ⟢ — the combinator is the entry, members are
> specialization notes). This chapter is reduced to the leaf-level facts the combinator does
> not carry: the conjugation variant-axis (`dot` Hermitian-conjugated vs `tdot` unconjugated
> — value-bearing for complex vectors) and `dot`'s unique L0 anchors. Semantics, algebraic
> laws, fusion-rotation framing, and the do-NOT-merge boundary are **deferred** to the
> combinator [`inner_product`](./inner_product.md) §"Specializations" — not re-derived here.

The conjugation-axis specialization of the L2 [`inner_product`](./inner_product.md) combinator:
the mutation-free reduce-to-scalar reduction `α = ⟨x, y⟩` at the Hermitian (complex) /
symmetric (real) kernel value with `M = I`, co-defined with its unconjugated co-variant
`tdot`. Recovered from the combinator at fixed axis-values:

    dot(x, y)  = inner_product x y          -- Hermitian (complex) / symmetric (real)
    tdot(x, y) = inner_product x y          -- with the unconjugated kernel (complex-only)

**Do NOT merge into `inner_product`** — the codomain/fold distinction is load-bearing
(`book/src/L2/index.md` §"Fold-cohort boundary"): `inner_product` is the variadic fold over
the conjugation/element-type/weight family; `dot` is the named leaf at the single plain
conjugation value (`M = I`). The named-specialization presence lets the L3 [`dot`](../L3/dot.md)
lower to an adjacent same-named L2 parent. All semantics, laws, and fusion content are the
combinator's — see [`inner_product`](./inner_product.md) §"Specializations".

## Signature

    dot   :: (x: Tensor[(S: ...)], y: Tensor[$S]) -> Scalar
    tdot  :: (x: Tensor[(S: ...)], y: Tensor[$S]) -> Scalar     -- complex-only variant

Two operators in one chapter because they share the entire reduction skeleton (sum over the
shape group `S`) and differ only by the per-element kernel. The signature is the combinator's,
read at the plain (`M = I`) conjugation value (named shape groups per
[`l4_calculus`](../design/l4_calculus.md) §1.2.1 — both operands congruent over one shape
group `S` of arbitrary unknown rank, NOT rank-1). Full shape contract:
[`inner_product`](./inner_product.md) §Signature.

## Conjugation variant-axis (the leaf-level fact, value-bearing for complex vectors)

`dot` is **conjugate-linear in arg-1, linear in arg-2** (`⟨x, y⟩ = xᴴ y`). The conjugation
convention is **value-bearing for complex vectors** and is the one fact this specialization
carries beyond the combinator. The per-element kernel by element-type:

| element type | operator | per-element kernel | form |
|---|---|---|---|
| `real`    | `dot`  | `x[idx] · y[idx]`        | bilinear symmetric (conjugation a no-op) |
| `complex` | `dot`  | `conj(x[idx]) · y[idx]`  | Hermitian sesquilinear (arg-1 conjugated) |
| `complex` | `tdot` | `x[idx] · y[idx]`        | unconjugated bilinear |

The two are distinct operators because the algebraic laws differ: `dot` is PSD-at-diagonal
(`dot(x, x) ≥ 0`, confirmed by the in-source `&x==&y` imag=`0.0` elision at
`palace/linalg/vector.cpp:266`); `tdot` is the indefinite form (`tdot(x, x) = 0` does not imply
`x = 0`, e.g. `x = (1, i)`). The full conjugation-convention reconciliation (Palace's L0
surface pins the **opposite** operand — `linalg::Dot(comm, x, y) = yᴴ x = conj(xᴴ y)`) and the
weight-presence axis (`M = I` here; the M-weighted member is the separate
[`bilinear-form`](../L1/bilinear-form.md)) live at the combinator §"Specializations" and the
genuine L2>L1 [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md)
theme — not re-derived here.

> **Member-level caveat (inherited; not a status reduction).** `tdot` (`ComplexVector::TransposeDot`)
> has zero Palace call sites (declaration `palace/linalg/vector.hpp:112` + definition
> `palace/linalg/vector.cpp:269` only). The reduction structure is firm and the Hermitian arm is
> behaviorally exercised; only `tdot`'s behavioral weight is API-only. See
> [`inner_product`](./inner_product.md) §"tdot".

## Status

`firm` — specialization-stub. `dot` at L2 is the `M = I` Hermitian/symmetric specialization of
the firm L2 [`inner_product`](./inner_product.md) combinator (firm cycle-050); semantics,
algebraic laws, fusion-rotation framing, and the do-NOT-merge boundary are inherited from the
combinator unchanged. This chapter retains only the conjugation variant-axis (the value-bearing
leaf-level fact) and `dot`'s unique L0 anchors. Originally harvested cycle-041 wave-1 as a thin
L2 floor under the L3 leaf cohort; re-expressed through the combinator and reduced to a
specialization-stub cycle-052 D3 (vocabulary-shift-redirect refactor pass). The named-leaf
presence is retained so the firm L3 [`dot`](../L3/dot.md) lowers to an adjacent same-named L2
parent (CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels**).

## Evidence

`dot`'s unique L0 anchors (RETAINED — the conjugation variant-axis and self-dot evidence the
combinator does not carry; paths relative to `reference/palace/`; self-verified via
`tools/citecheck/citecheck.py --anchor` this invocation). All other L0 evidence is the
combinator's / the firm L1 leaf's:

- [`book/src/L2/inner_product.md`](./inner_product.md) (firm cycle-050) — the combinator this
  leaf specializes; §"Specializations" (the conjugation/element-type/weight recovery), §"Fusion
  note", §Signature. All deferred semantics/laws/fusion content lives here.
- [`book/src/L1/dot.md`](../L1/dot.md) (firm cycle-002) — authoritative on the Palace surface,
  the receiver-vs-argument conjugation asymmetry, the self-dot fast path, and the complete L0
  evidence list.
- [`book/src/L3/dot.md`](../L3/dot.md) (firm cycle-011) — the L3 specialization this floor sits
  under.
- `palace/linalg/vector.hpp:110-113` — `ComplexVector::Dot` decl, comment `// Vector dot
  product (yᴴ x) or indefinite dot product (yᵀ x) for complex vectors.`; `TransposeDot`
  alongside. **Self-verified (anchor `Dot` at :111-113).**
- `palace/linalg/vector.cpp:263-267` — `ComplexVector::Dot` body = `x·conj(y) = yᴴ x`, with the
  `&y==this` imag=`0.0` self-dot fast path at `:266` (the PSD-at-diagonal confirmation).
  **Self-verified (anchor `Dot` at :263; `0.0` at :266).**
- `palace/linalg/vector.cpp:269-274` — `ComplexVector::TransposeDot` body: unconjugated
  bilinear, negated imaginary cross-term — the `tdot` kernel. **Self-verified (anchor
  `TransposeDot` at :269).**
- `test/unit/test-vector.cpp:206-207` — real-vector dot via `operator*`: `double dot = vec1 *
  vec2; CHECK_THAT(dot, WithinRel(32.0));` (`1·4+2·5+3·6=32`). Direct value-asserting test.
  **Self-verified (anchor `WithinRel` at :207).**
- [`book/src/concepts/dot.md`](../concepts/dot.md) — the cross-cutting concept page; BLAS-1
  heritage framing.
