# gram

The matrix-valued lift of the firm L2 reduce-to-scalar fold
[`inner_product`](./inner_product.md): `gram` is the **all-pairs `inner_product`** over a
`k`-column basis `X`, materializing the `k×k` Gram matrix `G = XᴴX` whose entry
`G[i,j] = inner_product(X[j], X[i]) = X[j]ᴴ X[i]`. Where `inner_product` collapses two tensors
to one scalar over the length axis, `gram` evaluates that scalar over every pair of basis
columns, collapsing the length axis once per `(i,j)` cell and keeping the two `k`-sized basis
index axes. The fusion-rotation form: Palace fuses the Gram build into a double `for`-loop of
`linalg::Dot` calls (`palace/linalg/nleps.cpp:524-531`); L2 unfolds that fused double-loop into
the named all-pairs fold over `inner_product`.

## Context

At L2 — the fusion-rotation layer (`book/src/L2/index.md`: "Batched specialized BLAS calls are
written as compositions of base primitives… Kernel fusion across multiple algebraic operations
is unfolded into composition") — `gram` is a **composition**, not a new floor primitive. It
adds no L0 reduction kernel of its own: each of its `k²` entries is one
[`inner_product`](./inner_product.md) (whose own L1 leaf [`dot`](../L1/dot.md) carries the
reduction kernel). Palace literally fuses the Gram into the double `for`-loop at
`palace/linalg/nleps.cpp:525-531`; de-fusing that double-loop into the canonical all-pairs fold
is the L2 rotation. The all-pairs lift sits alongside its scalar parent
[`inner_product`](./inner_product.md) and is consumed by the sibling oblique-projection
combinator `deflate` (rough-in; the Gram matrix `gram` builds is exactly what `deflate`
LU-solves — `book/src/L2/index.md:55`).

`gram` is **value-producing and stateless** — a pure fold from a basis to a matrix, with no
control-flow, no monadic state threading, and no convergence predicate. It therefore belongs
with the tensor algebra at L2, not with L4's `iterate_while`. (The *outer* deflation loop that
grows `X` by one column per converged eigenpair — `palace/linalg/nleps.cpp:613-619` — is the
iteration-structural part, and that lives in the NLEPS driver, not here. This is the same
stateless-at-L2 / iteration-outside argument the sibling named composition
[`orthogonalize`](./orthogonalize.md):40-44 makes.)

This entry is defined in **L2 vocabulary** (the `inner_product` fold, the `dot` hook,
matrix/basis axes); how the L2 all-pairs fold lowers onto Palace's `nleps.cpp` double-`Dot`
loop (and which reduction tree each entry pins) is L2>L1 lowering work, narrated forward from
L2 to L1 in [`L2-L1/gram-fold-specialization`](../L2-L1/gram-fold-specialization.md) (firm) — not authored here.

## Signature

```text
gram :: (dot: (Tensor[(S: ...)], Tensor[$S]) -> Scalar, X: Basis[N, k]) -> Matrix[k, k]
gram dot X = Matrix (\i j -> dot X[j] X[i])      -- entry (i,j) = ⟨X[j], X[i]⟩ = X[j]ᴴ X[i]

-- cross-Gram (two-set) member:
gram2 :: (dot, X: Basis[N, k], Y: Basis[N, m]) -> Matrix[m, k]
gram2 dot X Y = Matrix (\i j -> dot Y[i] X[j])   -- entry (i,j) = ⟨Y[i], X[j]⟩ = Y[i]ᴴ X[j]
gram dot X = gram2 dot X X                        -- single-set ≡ cross-Gram of X with itself
```

Shape contract (bunsen-style; named shape groups per
[`l4_calculus`](../semantics/index.md) §1.2.1):

- `dot` — `(Tensor[(S: ...)], Tensor[$S]) -> Scalar` — the inner-product hook (shape-generic
  over a congruent shape group `S` — the hook reduces whole congruent
  tensors), the **same hook axis**
  the sibling [`orthogonalize`](./orthogonalize.md) carries (`orthogonalize.md`:67-71, the
  `op.dot` field). The canonical Hermitian [`inner_product`](./inner_product.md) /
  [`dot`](../L1/dot.md) (conjugate-linear in arg-1) by default; the SLEPc/ROM paths may
  substitute a `B`-weighted hook (`inner_product_M`), giving the weighted Gram `XᴴBX`. NLEPS
  uses the canonical Hermitian hook (`linalg::Dot`, `palace/linalg/nleps.cpp:529`).
- `X` — `Basis[N, k]` — read-only; `k` columns each of length axis `N` (the converged
  invariant-pair basis in NLEPS; in general any `k`-vector set). The basis is **not** required
  orthonormal — that is the entire point of building and consuming an explicit Gram (contrast
  `orthogonalize`'s orthonormal-basis precondition, `orthogonalize.md`:73-76).
- `Y` (cross-Gram member) — `Basis[N, m]` — read-only; `m` columns sharing the length axis `N`
  with `X`. The two index axes `k`, `m` may differ.
- result — `Matrix[k, k]` (single-set) or `Matrix[m, k]` (cross) — element type per the `dot`
  hook (`real` / `complex`, conjugation living in the hook exactly as for `inner_product`); the
  empty basis `k = 0` gives the `Matrix[0, 0]` (the `k == 0` early-return guard in NLEPS,
  `palace/linalg/nleps.cpp:515-518`).
- `X`, `Y` and the hook's two operands share one length axis `N` and one element type
  `T ∈ {real, complex}`.

**Conjugation convention (pinned via `inner_product`).** The entry `gram dot X` `[i,j]` is
`inner_product(X[j], X[i]) = X[j]ᴴ X[i]` — **column `j` (the column index) is the conjugated
operand**, inherited unchanged from [`inner_product`](./inner_product.md)'s arg-1-conjugated
convention (`inner_product.md`:48-51) and the L1 [`dot`](../L1/dot.md):43 pinned
`⟨x, y⟩ = xᴴ y`. Palace's source writes `SS(i, j) = linalg::Dot(GetComm(), X[i], X[j])`
(`palace/linalg/nleps.cpp:529`), and the free-function `linalg::Dot(comm, a, b) = bᴴ a`
conjugates **arg-2** (the deliberate L1 re-order recorded at `inner_product.md`:62-96), so
`linalg::Dot(GetComm(), X[i], X[j]) = X[j]ᴴ X[i]` — i.e. Palace's `SS(i,j)` equals
`inner_product(X[j], X[i])` in the representation convention, with column `j` conjugated. Pinning
this once at `gram` (rather than re-deriving the `yᴴx`-vs-`xᴴy` reconciliation per Gram cell) is
the simplification this lift buys; the diagonal `G[i,i] = X[i]ᴴ X[i]` is convention-invariant
(real), the off-diagonal is the convention-sensitive part (`nleps.cpp:529` observable).

## Semantics

`gram dot X` reduces a `k`-column basis to a `k×k` matrix: cell `(i,j)` is the inner product of
column `j` (conjugated) with column `i`, `G[i,j] = inner_product(X[j], X[i]) = X[j]ᴴ X[i]`. It
is the **outer cartesian lift** of [`inner_product`](./inner_product.md) over two copies of the
basis index set — every law and degeneration of `gram` is a pointwise consequence of the scalar
fold applied to a pair of columns. The cross-Gram member `gram2 dot X Y` does the same over two
*distinct* index sets, `G[i,j] = Y[i]ᴴ X[j]`; the single-set form is the diagonal-block special
case `gram dot X = gram2 dot X X`.

It is **pure** at L2: it consumes `dot` and `X` (and `Y`) and produces a fresh dense `k×k`
matrix; there is no destination buffer (NLEPS's `Eigen::MatrixXcd SS(k, k)` at
`palace/linalg/nleps.cpp:524` is the return value's L0 realization, a fresh small-dense matrix
redundant on all ranks, not a through-written argument). Each cell carries the same MPI
collective `inner_product` does (`LocalDot ∘ Mpi::GlobalSum`); the collective is not in the L2
signature (single-rank scope, ranks read as their single-rank equivalents), exactly as for
`inner_product`.

The result is a **dense `k×k` matrix on a small index axis** (`k` = number of converged
eigenpairs, grown incrementally; `palace/linalg/nleps.cpp:613-619`), distinct from the big
length axis `N` that the columns live on and that each cell collapses. `gram` is the bridge
between the big-space basis `X : Basis[N, k]` and the small-space coordinate algebra
(`Matrix[k, k]`) that its consumer `deflate` LU-solves.

## Algebraic laws

The laws below hold; every one is a **syntactic identity on the firm `inner_product` fold**
(`book/src/L2/inner_product.md` §"Algebraic laws"), lifted pointwise over the basis index axes.
Absences are deliberate.

**Defining lift law (this is what makes `gram` the all-pairs lift):**

1. **All-pairs definition.** `gram dot X` `[i,j] = inner_product(X[j], X[i])` for all
   `i, j ∈ [0, k)`. Directly the double-loop body `SS(i, j) = linalg::Dot(GetComm(), X[i], X[j])`
   (`palace/linalg/nleps.cpp:529`), read through the pinned conjugation convention. Every other
   law is a consequence of this one composed with an `inner_product` law.

2. **Empty-basis identity.** `gram dot [] = Matrix[0, 0]` (the empty `k = 0` Gram) — the
   pointwise lift of `inner_product`'s empty-axis seed, and the `k == 0` early-return in NLEPS
   (`palace/linalg/nleps.cpp:515-518`, where deflation is skipped because there is no subspace).

**Hermitian / definiteness (lifted from `inner_product` laws 4–5):**

3. **Hermitian symmetry.** `gram dot X = (gram dot X)ᴴ` (the matrix equals its conjugate
   transpose) when `dot` is the Hermitian inner product: cell `(i,j)` is `X[j]ᴴ X[i]` and cell
   `(j,i)` is `X[i]ᴴ X[j] = conj(X[j]ᴴ X[i])` by `inner_product`'s Hermitian symmetry
   (`inner_product.md` law 4). For a real `dot` this is plain symmetry `G = Gᵀ`. Consequence:
   the **diagonal is real** (`G[i,i] = X[i]ᴴ X[i] ∈ ℝ`, `inner_product` law 5), which is the
   convention-invariant part; the off-diagonal is the conjugation-sensitive part.

4. **Positive semi-definiteness.** `gram dot X ⪰ 0` (every eigenvalue `≥ 0`), and **positive
   definite iff `X` has full column rank** — the matrix lift of `inner_product`'s
   PSD-at-diagonal law 5 **via sesquilinearity (law 3)**: for any coordinate vector `v`,
   sesquilinearity (`inner_product` law 3) collapses the quadratic form into a single diagonal
   inner product, `vᴴ G v = inner_product(Xv, Xv)`, and diagonal-PSD (`inner_product` law 5) gives
   `inner_product(Xv, Xv) ≥ 0`, with equality iff `Xv = 0`, i.e. iff `v` is a column-rank-deficiency
   direction. (Law 5 alone gives only the per-entry diagonal non-negativity `G[i,i] ≥ 0`; the full
   quadratic-form PSD needs law 3 to assemble the off-diagonal cross-terms into `inner_product(Xv, Xv)`.)
   This is exactly the property that makes `gram`'s consumer `deflate` well-posed: the Gram is
   invertible (the `fullPivLu().solve` at `palace/linalg/nleps.cpp:534` is well-defined) precisely
   when the deflation basis is full-rank, which the NLEPS invariant-pair basis is by construction
   (each converged eigenvector is appended only after normalization,
   `palace/linalg/nleps.cpp:613-619`).

**Block / incremental laws (lifted from `inner_product`'s length-concatenation homomorphism):**

5. **Concatenation block law.** `gram dot (X ++ Y)` is the `2×2` block matrix
   `[[gram dot X, gram2 dot Y X], [gram2 dot X Y, gram dot Y]]` (the off-diagonal blocks are the
   cross-Grams). This is the basis-index-axis analogue of `inner_product`'s split-additivity:
   appending columns extends the Gram by bordering blocks.

6. **Incremental-Gram (rank-1 border) law.** The single-column special case of law 5:
   `gram dot (X ++ [x])` borders `gram dot X` with one new row/column —
   `[[gram dot X, c], [cᴴ, x ᴴ x]]` where `c[j] = inner_product(x, X[j]) = X[j]ᴴ x` is the new
   coordinate column. This is exactly how NLEPS grows the deflation state as eigenpairs converge
   (`palace/linalg/nleps.cpp:613-619` resizes `X` to `k+1` and extends `H`; the Gram `SS` is
   rebuilt at the bordered size on the next `deflated_solve`). It certifies `gram` is a genuine
   fold over basis columns (variadic-in-`k`), not a coincidental cluster.

Laws that explicitly **do not** hold:

- **Associativity of the per-cell reduction-tree under IEEE-754 (inherited load-bearing
  non-law).** Each cell is one `inner_product`, whose combining `(+)` is floating-point
  non-associative (`inner_product.md` §"Algebraic laws", the load-bearing non-law). Different
  summation orders give different bit-level cells. Palace pins a specific tree per cell (the
  Hypre per-rank kernel + MPI tree-reduce of each `linalg::Dot`). Per CLAUDE.md "load-bearing
  numerical tricks… non-associative reduction orderings… preserve as explicit algebraic claims",
  this is recorded, not erased: **`gram` is order-agnostic for value, but bit-identical
  reproduction of an L0 Gram requires matching each cell's pinned reduction tree.** Which tree a
  given lowered Gram pins is recorded by the L2>L1 lowering theme [`gram-fold-specialization`](../L2-L1/gram-fold-specialization.md) (firm).

- **Symmetry-exploitation is a transparent perf trick, NOT a structural law.** Palace's
  `:525-531` double-loop computes **all** `k²` cells without exploiting Hermitian symmetry (it
  does not compute only the lower triangle and conjugate-reflect). The L2 form is the full
  all-pairs fold; "compute upper triangle + conjugate-mirror" is a one-line transparent note for
  the lowering (it computes the same matrix modulo the IEEE per-cell non-law), not an axis.

- **PSD strictness in floating point.** `gram dot X ⪰ 0` holds mathematically but can fail by
  ULP-level amounts (a near-rank-deficient basis can produce a Gram with a tiny negative
  eigenvalue under finite-precision summation). Inherited from `inner_product`'s Cauchy–Schwarz
  finite-precision non-law; consumers that LU-solve the Gram (`deflate`) rely on the basis being
  comfortably full-rank, not marginally so.

- **No fold-merge with `linear_combination`.** `gram` reduces (per cell) the **length axis** to a
  scalar and assembles a `Matrix[k,k]`; `linear_combination` reduces the **term axis** keeping
  `Tensor[N]`. They share no bridge identity (inherited from the `inner_product` /
  `linear_combination` do-NOT-merge boundary, `inner_product.md` §"Sibling fold").

## Variant axes

1. **`dot` hook** ∈ {`canonical Hermitian ⟨·,·⟩`, `B-weighted`} — the same hook axis the sibling
   [`orthogonalize`](./orthogonalize.md) carries (`orthogonalize.md`:67-71). The canonical
   Hermitian hook gives `G = XᴴX`; the `B`-weighted hook (`inner_product_M`) gives the weighted
   Gram `G = XᴴBX` (the mass-matrix / SPD-weighted overlap used by Rayleigh-Ritz / Galerkin
   projection). NLEPS uses the canonical hook (`linalg::Dot`, `palace/linalg/nleps.cpp:529`).
   Orthogonal to the others; conjugation lives entirely in the hook. **The `B`-weighted member
   has two concrete Palace witnesses** — the electrostatic capacitance and magnetostatic
   inductance energy reductions, each an all-pairs weighted Gram `G[i,j] = Xⱼᴴ K Xᵢ` over a
   small per-terminal field-solution set `X` with `K` an **assembled FE mass matrix** (the
   SPD instance of the `B`-weight): the capacitance build
   `C(i,j) = linalg::Dot(V[j], M_elec·V[i]) = V[j]ᴴ M_elec V[i]`
   (`palace/drivers/electrostaticsolver.cpp:111-137`, `M_elec` = ε-weighted
   `VectorFEMassIntegrator`, `palace/models/domainpostoperator.cpp:30-41`), and the inductance
   build `M(i,j) = A[j]ᴴ M_mag A[i]` (`palace/drivers/magnetostaticsolver.cpp:110-152`,
   `M_mag` = μ⁻¹-weighted mass integrator, `palace/models/domainpostoperator.cpp:43-66`). Both
   are the **single-set `gram dot X`** form (axis 2) and **exploit Hermitian symmetry in the
   lowering** (compute the upper triangle `j = i+1..`, copy the lower —
   `electrostaticsolver.cpp:131-137`, `magnetostaticsolver.cpp:144-150`; the transparent
   perf-trick non-axis below, here actually taken, unlike NLEPS's full-`k²` build at
   `nleps.cpp:525-531`). The energy-formulation post-Gram cell scaling (`/Vᵢ²` with `Vᵢ≡1`;
   `/(IᵢIⱼ)`) and the `Cm`/`Mm` capacitance/inductance sign-remix + final in-place invert are
   **downstream consumers** of this weighted Gram, not part of the fold (the consumer-vs-
   constituent split, as for `deflate`).

2. **Single-set vs cross-Gram** — `gram dot X` (the `k×k` `XᴴX`) vs `gram2 dot X Y` (the `m×k`
   `YᴴX`). NLEPS uses only the single-set form (the deflation Gram is `XᴴX`,
   `palace/linalg/nleps.cpp:524-531`); the cross member is the block-law's off-diagonal and the
   general Rayleigh-Ritz overlap. The single-set form is the diagonal-block special case.

3. **Element-type** ∈ {`real`, `complex`} — absorbed by the `dot` hook (conjugation and the
   real-vs-complex kernel live in `inner_product`/`dot`), exactly as for `inner_product`. NLEPS
   is complex (`Eigen::MatrixXcd SS`, `palace/linalg/nleps.cpp:524`).

**Symmetry-exploitation (`:525-531` computes all `k²` cells) is NOT a variant axis** — it is the
transparent perf-trick non-law above. **Basis cardinality `k`** is NOT a variant axis either —
it is the natural fold parameter (`gram` is variadic-in-`k`; the incremental-Gram law 6 certifies
the fold over columns), not a family of fixed-`k` specializations.

## Dependencies

- **Constituent fold (the scalar this lifts to a matrix):** [`inner_product`](./inner_product.md)
  (firm) — `gram dot X [i,j] = inner_product(X[j], X[i])`. Every `gram` law is a pointwise lift
  of an `inner_product` law. `gram` does not replace `inner_product`; it is the all-pairs lift of
  it.
- **L1 entry kernel:** [`dot`](../L1/dot.md) (firm; the canonical Hermitian hook) — the per-cell
  reduction kernel, with the arg-1-conjugated `⟨x,y⟩ = xᴴ y` convention `gram` inherits
  (`dot.md`:43). The `B`-weighted hook is the M-weighted [`inner_product`](./inner_product.md)
  member (`bilinear-form` leaf).
- **Sibling (constituent-shared, do NOT merge):** [`orthogonalize`](./orthogonalize.md) (firm) —
  shares the `dot` hook axis and the "project a vector against a subspace `span(X)`" target, but
  `orthogonalize` is the **orthonormal-basis** Gram-Schmidt with **no Gram matrix and no solve**
  (sequential rank-1 subtraction, orthogonal projection `I − XXᴴ`), whereas `gram` is the
  explicit `XᴴX` build that the **non-orthonormal-basis** oblique projector `deflate` LU-solves.
  `orthogonalize`'s Gram is the implicit identity (`gram = I`); `gram` is needed exactly when the
  basis is **not** orthonormal. See the `deflate` rough-in's over-unification guard
  (`book/src/L2/index.md:55`).
- **Consumer (NOT a constituent):** `deflate` (rough-in; `book/src/L2/index.md:55`) — the oblique
  /Galerkin complementary projector `I − X(XᴴX)⁻¹Xᴴ` LU-solves the Gram `gram` builds (the
  `fullPivLu().solve(SS)` chain at `palace/linalg/nleps.cpp:533-535`). `deflate`'s promotion to
  firm additionally needs the small-dense `lu_solve` primitive (OQ
  `deflate-needs-small-dense-lu-solve-primitive`), which is `deflate`'s dependency, not `gram`'s —
  `gram` builds the matrix; `deflate` solves it.
- **L2>L1 lowering theme** [`gram-fold-specialization`](../L2-L1/gram-fold-specialization.md) (firm): how the L2
  all-pairs fold lowers onto Palace's `nleps.cpp:524-531` double-`linalg::Dot` loop (the dispatch
  of each cell to the Hermitian/weighted `dot` leaf; the symmetry-exploitation transparent note;
  which reduction tree each cell pins — the load-bearing content of the IEEE non-law).

## Status

`firm` — the all-pairs lift of the firm L2 fold [`inner_product`](./inner_product.md):
every algebraic law is a syntactic identity on the `inner_product` fold (firm-on-positive-structure
on the literal Gram-build site `palace/linalg/nleps.cpp:524-531`).

> **Coverage caveat.** The literal unweighted `XᴴX` Gram-build appears at exactly **one** site in
> the Palace tree — `palace/linalg/nleps.cpp:524-531` (the ROM path
> `palace/models/romoperator.cpp:757-765` does small-dense solves on a *reduced operator* `Ar`, not
> an explicit `XᴴX`, so it is not a `gram` instance) — and there is **no dedicated NLEPS/deflation
> unit test**. Firmness rests on the laws being `inner_product`-identities (anchored by the
> real-member value test `test/unit/test-vector.cpp:206-207` and the SPD-realness assertion
> `palace/linalg/operator.cpp:615-616`) plus the single build site read directly. The **`B`-weighted
> `XᴴKX`** member has two concrete witnesses (the capacitance/inductance energy reductions, variant-axis
> 1 above).

## Evidence

Paths relative to `reference/`.

- `palace/linalg/nleps.cpp:524-531` — **the sole literal Gram-build site.** `Eigen::MatrixXcd
  SS(k, k);` (`:524`) then the double-loop `for i { for j { SS(i, j) = linalg::Dot(GetComm(),
  X[i], X[j]); } }` (`:525-531`, the cell body `SS(i,j) = linalg::Dot(GetComm(), X[i], X[j])` on
  `:529`). The `k×k` deflation Gram `XᴴX`; cell `SS(i,j) = X[j]ᴴ X[i] = inner_product(X[j],
  X[i])`.
- `palace/linalg/nleps.cpp:532-535` — the consumer (NOT a `gram` law): Schur-modify `S = eig_opInv
  ·I − H` (`:532`), `SS = -S.fullPivLu().solve(SS)` (`:533`), coord solve `x2 =
  SS.fullPivLu().solve(x2)` (`:534`), back-projection `XSx2 = MatVecMult(X, S.fullPivLu().
  solve(x2))` (`:535`) — `deflate`'s use of the Gram `gram` builds.
- `palace/linalg/nleps.cpp:504-537` — `deflated_solve` lambda enclosing the Gram build, with the
  block-system comment `SS = (B − A T⁻¹U) = −X*X S⁻¹` (`:512-513`).
- `palace/linalg/nleps.cpp:515-518` — the `k == 0` early-return (no deflation subspace): the
  empty-basis identity (law 2) realized as the deflation skip.
- `palace/linalg/nleps.cpp:520-523` — the coordinate-extraction loop `x2(j) = b2(j) −
  linalg::Dot(GetComm(), x1, X[j])`: the `Xᴴ·` half consumed alongside the Gram (the
  arg-1-conjugated convention applied to a vector rather than a basis column).
- `palace/linalg/nleps.cpp:561-569` — `compute_residual`'s deflation: `XSvv2 = MatVecMult(X,
  S.fullPivLu().solve(vv2))` (`:563`) + residual coords `rr2(j) = linalg::Dot(GetComm(), vv,
  X[j])` (`:568`). A second consumer of the Gram-solve (not a fresh Gram build).
- `palace/linalg/nleps.cpp:660-668` — the Jacobian deflation terms: `S = eig·I − H` (`:664`),
  `Sv2 = S.fullPivLu().solve(v2)` (`:665`), `XSv2 = MatVecMult(X, Sv2)` (`:666`), `XSSv2 =
  MatVecMult(X, S.fullPivLu().solve(Sv2))` (`:667`). A third Gram-solve consumer.
- `palace/linalg/nleps.cpp:329-347` — `MatVecMult(X, y)`: the `X·coords` reconstruction (a
  length-`k` `linear_combination` over the basis, `z = 0; for j: AXPBYPCZ(...) into z`); the
  `deflate` consumer's back-projection half.
- `palace/linalg/nleps.cpp:613-619` — deflation-basis growth `X.resize(k+1); X[k] = v;
  H.conservativeResizeLike(...); H(k,k) = eig; k++`: the incremental-Gram (rank-1 border) law 6
  realized — the basis grows one column per converged eigenpair, and `X` is the **raw normalized
  invariant-pair basis (NOT orthonormalized)** → Gram inversion required → the explicit `gram`
  build is load-bearing.
- `palace/linalg/nleps.cpp:354-362` — the deflation-scheme literature anchors (Effenberger 2013
  successive eigenpair computation; Jarlebring/Koskela/Mele 2018 quasi-Newton; SLEPc-NEP
  minimality index 1) — the standard-scheme anchor for the oblique-Galerkin deflation Gram.
 
- `palace/linalg/nleps.cpp:542` — `deflated_solve(c, c2, w0, w2)`: a live call site of the lambda
  enclosing the Gram build.
- `palace/models/romoperator.cpp:757-765` — the ROM small-dense solves `RHSr =
  Ar.ldlt().solve(RHSr)` / `Ar.selfadjointView<...>().ldlt().solve(...)` /
  `Ar.fullPivHouseholderQr().solve(...)`: a *non-instance* — small-dense solve on a reduced
  operator `Ar`, NOT an explicit `XᴴX` Gram build (the coverage caveat's "no second Gram-build
  site" evidence).
- `palace/drivers/electrostaticsolver.cpp:111-137` — **first `B`-weighted `gram` witness
  (capacitance).** The double-loop `C(i,j) = linalg::Dot(V[j], D_gf)` with `D_gf = M_elec·V[i]`
  pinned once per outer `i` (`:118`), inner sweep `:124-130`, symmetry copy `:131-137`. Cell
  `C(i,j) = V[j]ᴴ M_elec V[i] = inner_product_M(V[j], M_elec, V[i])` — the single-set weighted
  Gram. Palace's own comment names the shape: `// (Vⱼᵀ K Vᵢ)` (`:122`).
- `palace/drivers/magnetostaticsolver.cpp:110-152` — **second `B`-weighted `gram` witness
  (inductance).** Structurally identical: `M(i,j) = linalg::Dot(A[j], H_gf)/(Iᵢ Iⱼ)` with
  `H_gf = M_mag·A[i]` (`:129`), inner sweep `:135-141`, symmetry copy `:144-150`. Cell
  `M(i,j) = A[j]ᴴ M_mag A[i]` (pre-`/(IᵢIⱼ)`) `= inner_product_M(A[j], M_mag, A[i])`. Palace
  comment `// (Aⱼᵀ K Aᵢ)` (`:134`).
- `palace/models/domainpostoperator.cpp:30-66` — the weight matrices' construction: `M_elec`
  = `BilinearForm + VectorFEMassIntegrator(ε)` `PartialAssemble()` (`:38-39`); `M_mag` =
  μ⁻¹-weighted mass integrator `PartialAssemble()` (`:53-64`). Establishes `K` is an assembled
  SPD FE mass matrix — the concrete `B`-weight.
- Artifact cross-references: `book/src/L2/inner_product.md` (the firm
  scalar fold `gram` lifts; the pinned arg-1-conjugated convention §"Conjugation convention
  (pinned)" `:46-102`; the Algebraic-laws §`:184-265`; the sibling-fold do-NOT-merge boundary
  §`:364-388`), `book/src/L1/dot.md:43` (the pinned `⟨x,y⟩ = xᴴ y` convention),
  `book/src/L2/orthogonalize.md:40-44,67-71,73-76` (the stateless-L2-placement argument, the
  `op.dot` hook axis, the orthonormal-basis precondition — the over-unification-guard sibling),
  `book/src/L2/index.md:50,54,55` (the firm `inner_product` row, the `gram` row, the
  `deflate` consumer row).
