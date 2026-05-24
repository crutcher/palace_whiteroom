# gemv_basis

**Primitive.** `gemv_basis(w, alpha, V[0..m-1], H[0..m-1]) → w'`

Batched coefficient–basis combination: given a stored basis `V[0..m-1]` (m vectors of length n) and a length-m coefficient vector `H`, update

```
w' = w + alpha · Σⱼ H[j] · V[j]
```

in one fused step. Equivalent to `w' = w + alpha · (V H)` viewing `V` as an n×m matrix and `H` as an m-vector — hence the name `gemv` (general matrix–vector) over a basis.

## Relation to axpy

`gemv_basis(w, α, V, H)` is the fused form of `m` sequential `axpy(w, α·H[j], V[j])` calls. The semantics are identical when the m axpys are independent of one another (no read–write dependency between iterations j and j+1 on `w`'s entries they share — and there is none, since each axpy is `w += scalar · V[j]` with all `V[j]` read-only). The fusion is transparent at L2: a slice may write the unfolded loop or the fused primitive interchangeably; the choice is an implementation detail (BLAS-2 packed call vs. loop of BLAS-1 axpys vs. hand-fused kernel).

Where the m updates are *not* independent — as in MGS, where each axpy mutates `w` and the next dot reads the mutated `w` — `gemv_basis` does NOT apply, and the unfolded axpy loop is the correct L2 form.

## Use sites

- **CGS / CGS2 orthogonalization** (`slices/orthog.md`): after the batched reduction yields the full coefficient vector `H[0..m-1]`, the basis correction `w − V H` is one `gemv_basis` call. The MGS variant cannot use `gemv_basis` for the reasons above.
- **GMRES basis combination** (anticipated): forming `x_m = x_0 + V_m y_m` after the small least-squares solve is the same primitive shape (with `alpha = +1`).
- **Projection / restriction operators on stored bases** (anticipated for eigensolver and FE slices).

## L2 status

`gemv_basis` is a derived L2 primitive: it is `dot`'s adjoint shape (dot reduces n→1 along a basis direction; gemv_basis expands 1→n along a basis direction with a coefficient vector). Both are batched forms of pointwise vector–scalar operations. Whether `gemv_basis` is realized as packed BLAS-2, as a manual loop of axpys, or as a fused custom kernel is an L3/L2-implementation choice and is transparent.

## Citations

- `palace/linalg/orthog.hpp:51-53` — the CGS post-reduction loop `for j: w.AXPY(-H[j], V[j])` is the unfolded form; this concept covers its L2 fusion.
