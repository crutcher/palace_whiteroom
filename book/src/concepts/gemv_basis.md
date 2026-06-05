---
edges:
  reference:
    - concepts/orthogonalization   # primary use-site (CGS/CGS2 basis correction)
    - L2/linear_combination        # the variadic scalar-weighted-vector-sum fold this is the
                                    # batched-coefficient specialization of (the fold home)
    - L1/orthogonalize             # the L0-anchored consumer: the CGS basis-correction loop
                                    # `for j: w.Add(-H[j], V[j])` (orthog.hpp:71-74) lives inside it.
---

# gemv_basis

**Primitive (concept-only).** `gemv_basis(w, alpha, V[0..m-1], H[0..m-1]) → w'`

Batched coefficient–basis combination: given a stored basis `V[0..m-1]` (m vectors of length n) and a length-m coefficient vector `H`, update

```
w' = w + alpha · Σⱼ H[j] · V[j]
```

in one fused step. Equivalent to `w' = w + alpha · (V H)` viewing `V` as an n×m matrix and `H` as an m-vector — hence the name `gemv` (general matrix–vector) over a basis.

## Disposition: concept-only — no standalone L0 callable

`gemv_basis` has **no standalone callable in Palace** and gets **no L1 operator**. Its only L0
referent is the **inline** CGS basis-correction loop `for j: w.Add(-H[j], V[j])`
(`palace/linalg/orthog.hpp:71-74`) inside `OrthogonalizeColumnCGS` — Palace writes the unfolded
loop of `axpy`, never a fused BLAS-2 `gemv`. That inline loop is already covered by the firm L1
operator [`orthogonalize`](../L1/orthogonalize.md) (which lifts the whole CGS/MGS/CGS2 family).
The *batched-coefficient fold shape* `w + α·Σⱼ H[j]·V[j]` is a specialization of the L2 variadic
scalar-weighted-vector-sum fold [`linear_combination`](../L2/linear_combination.md) (the
expand-1→n adjoint of `dot`'s reduce-n→1). So this page stays a **concept** documenting the
fold-shape; it is a non-node pointer to its fold home (`linear_combination`) and its L0-anchored
consumer (`orthogonalize`), not a book operator.

## Relation to axpy

`gemv_basis(w, α, V, H)` is the fused form of `m` sequential `axpy(w, α·H[j], V[j])` calls. The semantics are identical when the m axpys are independent of one another (no read–write dependency between iterations j and j+1 on `w`'s entries they share — and there is none, since each axpy is `w += scalar · V[j]` with all `V[j]` read-only). The fusion is transparent at L2: a slice may write the unfolded loop or the fused primitive interchangeably; the choice is an implementation detail (BLAS-2 packed call vs. loop of BLAS-1 axpys vs. hand-fused kernel).

Where the m updates are *not* independent — as in MGS, where each axpy mutates `w` and the next dot reads the mutated `w` — `gemv_basis` does NOT apply, and the unfolded axpy loop is the correct L2 form.

## Use sites

- **CGS / CGS2 orthogonalization** ([`orthogonalization`](./orthogonalization.md), lifted by firm L1 [`orthogonalize`](../L1/orthogonalize.md)): after the batched reduction yields the full coefficient vector `H[0..m-1]`, the basis correction `w − V H` is the unfolded loop `for j: w.Add(-H[j], V[j])` (`palace/linalg/orthog.hpp:71-74`). The MGS variant cannot use the batched form for the reasons above.
- **GMRES basis combination**: forming `x_m = x_0 + V_m y_m` after the back-solve is the same fold shape (with `alpha = +1`) — the downstream `linear_combination` lift in [`back_solve`](../L1/back_solve.md) (`x.Add(s[k], V[k])`, `iterative.cpp:666`).
- **Projection / restriction operators on stored bases** (anticipated for eigensolver and FE slices).

## L2 status

`gemv_basis` is a derived fold shape: it is `dot`'s adjoint (dot reduces n→1 along a basis direction; gemv_basis expands 1→n along a basis direction with a coefficient vector). Both are batched forms of pointwise vector–scalar operations. As such it is a coefficient-batched specialization of the L2 [`linear_combination`](../L2/linear_combination.md) fold — NOT a separate book operator. Whether it is realized as packed BLAS-2, a manual loop of axpys, or a fused custom kernel is an L3/L2-implementation choice and is transparent.

## Citations

- `palace/linalg/orthog.hpp:71-74` — the CGS post-reduction loop `for j: w.Add(-H[j], V[j])` is the unfolded form (the only L0 referent — an inline loop, not a standalone callable); this concept covers its fold shape, and the firm L1 [`orthogonalize`](../L1/orthogonalize.md) lifts the loop.
