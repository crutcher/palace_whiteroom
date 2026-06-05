---
kind: navigational-container (group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - L2/gram
    - L2/inner_product
    - L2/linear_combination
---

# L2 fold combinators

The variadic-reduction **fold combinators** — each a `foldl` skeleton with a distinct
homomorphism. These are the **family entries**: the once-standalone same-named BLAS-1
leaves are reduced specialization / consumer stubs that point *up* to these combinators
(grouped separately under *Fold-family specialization / consumer stubs*).

The two scalar/tensor folds share the fold skeleton but target **different codomains** —
merging them would erase the codomain distinction, so the **do-NOT-merge** boundary is
load-bearing and carried in both entries' dep-map rows:

- [`inner_product`](./inner_product.md) — folds the **length axis** to a `Scalar`
  (`foldl (+) zero (zipWith kernel x y)`); the conjugation / element-type / weight family
  of `dot` / `tdot` / `bilinear-form`.
- [`linear_combination`](./linear_combination.md) — folds the **term axis**, keeping
  `Tensor[N]` (`foldl (\acc (a,t) -> acc + a·t) zeros pairs`); the arity family of
  `scal` / `axpy` / `axpby` / `axpbypcz`.
- [`gram`](./gram.md) — the **all-pairs `inner_product` fold** → `Matrix[k,k]`; the
  matrix-valued lift of the scalar fold (Hermitian + PSD), consumed by `deflate`.

All three `firm`. Chapters are alphabetical.
