---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L3/inner_product
    - L3/linear_combination
---

# BLAS-1 vocabulary (L3)

The closed BLAS-1 cohort at L3: whole-tensor linear-update and reduction primitives, all element-local or parallel-clean over the shape group `S` (arbitrary, unknown rank; see [`l4_calculus`](../semantics/index.md) §1.2.1) — the **obstruction-free end** of the L3 obstruction-profile spectrum (`index.md` §Semantics).

Two L3 **combinators** carry the cohort's settled vocabulary, and the BLAS-1 leaves speak through them as list-length / kernel-value specializations:

- [`linear_combination`](./linear_combination.md) — the whole-tensor variadic scalar-weighted-tensor-sum fold `[(Scalar, Tensor[(S: ...)])] -> Tensor[$S]`. The four arity members `scal` (arity-1), `axpy` (arity-2, trailing coeff 1), `axpby` (arity-2), `axpbypcz` (arity-3) are its specializations — **eliminated cycle-124 (RE6)**, their unique L0 anchors folded into [§Arity specializations](./linear_combination.md#arity-specializations).
- [`inner_product`](./inner_product.md) — the whole-tensor reduce-to-scalar inner product `Tensor[(S: ...)] -> Tensor[$S] -> Scalar`. `dot` is its Hermitian/symmetric [§Specialization](./inner_product.md#specializations-the-members-as-notes-under-the-combinator); `nrm2` is the `√ ∘ abs ∘ inner_product` [**consumer**](./inner_product.md#consumer-not-an-instance-nrm2--matrix-weighted-norm) at `y=x` (NOT a fold member — the do-NOT-merge boundary). Both standalone leaf chapters were **eliminated cycle-127 (RE-style)**, their unique leaf facts folded into the combinator.

All carry **no sequential obstruction** — finite static term-list folds (`linear_combination`) and parallel-clean length-axis reductions (`inner_product`); the pinned L0 summation tree is a deferred non-law, not an obstruction. The substantive rotation in each chain is the L2>L1 fold-specialization theme (`linear-combination-fold-specialization` / `inner-product-fold-specialization`); the L3>L2 edge is the degenerate identity-in-named-terms in-line §"Downward to L2" note on each combinator.

See `index.md` §"Operator dep-map → BLAS-1 vocabulary" for the per-operator signatures, dependencies, and status.
