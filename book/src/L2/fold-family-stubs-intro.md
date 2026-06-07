---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L2/inner_product
    - L2/linear_combination
---

# L2 fold-family combinators (former specialization / consumer stubs — eliminated)

The once-standalone same-named BLAS-1 leaves have all been **eliminated into their fold
combinators** (the combinator is the entry; per the 2026-06-01 vocabulary-shift redirect the
residual same-named per-layer leaf-floors are the retired rectangular pattern).

The four `linear_combination` arity members (`scal`/`axpy`/`axpby`/`axpbypcz`) were
**eliminated cycle-124 (RE6)**, their unique L0 anchors folded into
[`linear_combination` §Arity specializations](./linear_combination.md#arity-specializations).

The two `inner_product` reduce-family stubs were **eliminated cycle-127 (RE-style)**, their
unique leaf-level facts folded into [`inner_product`](./inner_product.md):
- the `M = I` Hermitian/symmetric **specialization** `dot` (conjugation variant-axis + the
  `Dot`/`TransposeDot` kernels + self-dot fast path) → §"Specializations";
- the `√ ∘ abs ∘ inner_product` **consumer** `nrm2` at `y=x` (NOT a fold member — do-NOT-merge;
  the `std::abs` defensive guard preserved) → §"Consumer (NOT an instance)".

[`inner_product`](./inner_product.md) and [`linear_combination`](./linear_combination.md) are
now the sole family entries; the kept named L4 verbs `dot`/`nrm2` rise alongside the combinator
as the permitted dual.
