# L2 fold-family specialization / consumer stubs

The once-standalone same-named BLAS-1 leaves, **reduced to thin specialization / consumer
stubs** under their fold combinators (cycle-052 vocabulary-shift-redirect refactor —
the combinator is the entry, these are pointers up to it). Each stub **defers** all
semantics / laws / fusion-rotation framing to its combinator and keeps only its unique
L0 anchors + its one variant-axis row. The files are kept on disk (reduce-to-stub, not
delete) so every inbound link stays live.

Specialization-stubs of [`linear_combination`](./linear_combination.md) (fixed arity;
output-aliasing is the **fold's** axis, carried by reference):

- [`scal`](./scal.md) — arity-1 (`scal(α,x) = linear_combination [(α,x)]`).
- [`axpy`](./axpy.md) — arity-2, second coefficient fixed to 1.
- [`axpby`](./axpby.md) — arity-2, general second coefficient.
- [`axpbypcz`](./axpbypcz.md) — arity-3 (the maximal fixed-arity L0 symbol).

Specialization / consumer stubs of [`inner_product`](./inner_product.md) (do-NOT-merge —
codomain / fold distinction load-bearing, §"Fold-cohort boundary"):

- [`dot`](./dot.md) — the `M = I` Hermitian/symmetric **specialization** (the conjugation
  variant-axis — `dot` Hermitian vs `tdot` unconjugated — is the value-bearing leaf fact).
- [`nrm2`](./nrm2.md) — the `√ ∘ abs ∘ inner_product` **consumer** at `y=x` (NOT a fold
  member); the `std::abs` defensive guard preserved as an explicit numerical claim.

All six `firm` (specialization / consumer stubs). Chapters are alphabetical.
