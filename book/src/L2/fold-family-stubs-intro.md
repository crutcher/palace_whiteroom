---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L2/dot
    - L2/nrm2
---

# L2 fold-family specialization / consumer stubs

The once-standalone same-named BLAS-1 leaves, **reduced to thin specialization / consumer
stubs** under their fold combinators (cycle-052 vocabulary-shift-redirect refactor —
the combinator is the entry, these are pointers up to it). Each stub **defers** all
semantics / laws / fusion-rotation framing to its combinator and keeps only its unique
L0 anchors + its one variant-axis row.

The four `linear_combination` arity members (`scal`/`axpy`/`axpby`/`axpbypcz`) were
**eliminated cycle-124 (RE6)**, their unique L0 anchors folded into
[`linear_combination` §Arity specializations](./linear_combination.md#arity-specializations) —
the combinator is now the sole family entry.

Specialization / consumer stubs of [`inner_product`](./inner_product.md) (do-NOT-merge —
codomain / fold distinction load-bearing, §"Fold-cohort boundary"):

- [`dot`](./dot.md) — the `M = I` Hermitian/symmetric **specialization** (the conjugation
  variant-axis — `dot` Hermitian vs `tdot` unconjugated — is the value-bearing leaf fact).
- [`nrm2`](./nrm2.md) — the `√ ∘ abs ∘ inner_product` **consumer** at `y=x` (NOT a fold
  member); the `std::abs` defensive guard preserved as an explicit numerical claim.

Both `firm` (specialization / consumer stubs). Chapters are alphabetical.
