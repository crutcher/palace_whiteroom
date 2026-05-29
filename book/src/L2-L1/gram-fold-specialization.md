# gram-fold-specialization

The all-pairs lift of the BLAS-1 reduce-to-scalar conjugation rotation. Lowers the L2 all-pairs
fold [`gram`](../L2/gram.md) (`book/src/L2/gram.md`, firm cycle-022) into a **`k×k` grid of L1
per-cell leaves** — each cell a [`dot`](../L1/dot.md) (canonical Hermitian hook) or a
[`bilinear-form`](../L1/bilinear-form.md) (`xᴴ M y`, the B-weighted hook) — by **materializing
the all-pairs definition law as a double loop over the two basis index axes and dispatching each
cell on the hook's conjugation/weight exactly as the sibling scalar theme does**. Narrated
forward: the one L2 matrix-valued fold **re-fuses** downward into Palace's nested `for i { for j {
SS(i,j) = linalg::Dot(GetComm(), X[i], X[j]) } }` double-`Dot` loop
(`palace/linalg/nleps.cpp:525-531`), and this theme records (a) the **cell-dispatch** — each cell
is one inner-product leaf, inheriting the sibling theme's conjugation/element-type/weight keys;
(b) the **per-cell value-level conjugate-pair re-order** between the L1/L2 `xᴴ y` convention and
Palace's L0 `yᴴ x` form, applied independently to every cell; (c) the **symmetry-exploitation
transparent note** (Palace computes all `k²` cells; "upper-triangle + conjugate-mirror" is an
equivalent un-taken trick); and (d) the **per-cell pinned reduction tree** (the load-bearing
content the `gram` IEEE-754 non-law deferred here, `book/src/L2/gram.md` §"Algebraic laws").

This is the **matrix-valued sibling** of
[`inner-product-fold-specialization`](./inner-product-fold-specialization.md): that theme lowers
the reduce-to-`Scalar` fold `inner_product` to a single leaf; this one lowers `inner_product`'s
all-pairs lift `gram` to a `k×k` grid of those same leaves. Every dispatch decision is **inherited
pointwise** from the scalar theme (one cell = one `inner_product` lowering); the matrix-specific
content is the loop materialization, the symmetry note, and the per-cell tree. The two are not
merged: different L2 LHS (`inner_product : ... -> Scalar` vs `gram : ... -> Matrix[k,k]`),
different result rank, different consumer (`gram` feeds `deflate`'s Gram-solve; `inner_product`
feeds Krylov coefficients).

## Slug

`gram-fold-specialization`

## L2 form (LHS)

The L2 form is the all-pairs reduce-to-matrix fold over a `k`-column basis (`L2/gram` §Signature,
`book/src/L2/gram.md:42-50`), with an optional matrix weight carried in the `dot` hook:

```text
gram  :: (dot: (Tensor[N], Tensor[N]) -> Scalar, X: Basis[N, k])                  -> Matrix[k, k]
gram2 :: (dot,                                   X: Basis[N, k], Y: Basis[N, m]) -> Matrix[m, k]

gram  dot X   = Matrix (\i j -> dot X[j] X[i])   -- entry (i,j) = ⟨X[j], X[i]⟩ = X[j]ᴴ X[i]
gram2 dot X Y = Matrix (\i j -> dot Y[i] X[j])   -- entry (i,j) = ⟨Y[i], X[j]⟩ = Y[i]ᴴ X[j]
gram  dot X   = gram2 dot X X                    -- single-set ≡ cross-Gram of X with itself
```

The fold is **pure / out-of-place**: it consumes `dot` and `X` (and `Y`) and produces a fresh
dense `k×k` matrix; there is no destination buffer (NLEPS's `Eigen::MatrixXcd SS(k, k)` at
`palace/linalg/nleps.cpp:524` is the return value's L0 realization, a fresh small-dense matrix,
not a through-written argument). The pinned conjugation convention is **arg-1 conjugated**,
inherited unchanged from [`inner_product`](../L2/inner_product.md) (`L2/gram` §"Conjugation
convention", `book/src/L2/gram.md:73-85`):

$$ \text{gram}(\text{dot}, X)[i,j] = \text{inner\_product}(X[j], X[i]) = X[j]^{\mathsf H}\, X[i],
\qquad \text{column } j \text{ (the column index) is the conjugated operand.} $$

The shape precondition `X : Basis[N, k]` (the `k` columns share one length axis `N`; the two
index axes `k`, `m` may differ for `gram2`) is the aligned-pass precondition each per-cell L0
reduction kernel requires — the same `MFEM_ASSERT(x.Size() == y.Size())`
(`palace/linalg/vector.cpp:668`) the sibling scalar theme cites, applied per cell. The basis is
**not** required orthonormal — that is the entire point of building an explicit Gram for the
non-orthonormal-basis consumer `deflate` (`L2/gram` §Signature, `book/src/L2/gram.md:60-63`).

## L1 form (RHS)

The L1 form is a **`k×k` grid of per-cell leaves**, each cell one of the same three leaves the
sibling scalar theme dispatches over (the conjugation axis at [`dot`](../L1/dot.md), which
co-defines `dot`/`tdot`; the M-weighted member at [`bilinear-form`](../L1/bilinear-form.md)):

```text
dot           :: (x: Tensor[N], y: Tensor[N])                          -> Scalar
tdot          :: (x: Tensor[N], y: Tensor[N])                          -> Scalar   -- complex-only
bilinear_form :: (x: Tensor[M], M: LinearOperator[M, N], y: Tensor[N]) -> Scalar

-- the matrix is assembled cell-by-cell; each cell is one scalar leaf:
gram dot X  ⇒  Matrix (\i j -> leaf(X[i], X[j]))   -- leaf selected by the hook (table below)
```

There is no matrix-level L1 reduction primitive: `gram` adds no L0 kernel of its own (`L2/gram`
§Context, `book/src/L2/gram.md:15-25`). The matrix is **assembled** — `k²` independent scalar
leaf invocations written into a `Matrix[k,k]` — exactly Palace's `Eigen::MatrixXcd SS(k,k)`
filled by the `:525-531` double loop. At L1 the per-cell conjugation and weight are **fixed per
leaf** (`dot` Hermitian, `tdot` unconjugated, `bilinear_form` M-weighted), each mirroring Palace's
L0 reduction surface one-to-one — identical to the sibling scalar theme's RHS, just invoked `k²`
times. The leaves adopt the **same arg-1-conjugated convention** as the L2 fold
([`dot`](../L1/dot.md):43; [`bilinear-form`](../L1/bilinear-form.md):63), so the per-cell
LHS→RHS dispatch is convention-preserving at the representation level; the per-cell value-level
re-order against the Palace L0 source is §"The per-cell conjugate-pair re-order" below.

## The dispatch rewrite (L2 → L1)

The lowering reads the fold's hook + element-type, materializes the all-pairs definition law as a
double loop, and dispatches **each cell** to the matching L1 leaf. This is the **`gram` all-pairs
definition law** (`L2/gram` law 1, `book/src/L2/gram.md:117-122`) read as a lowering, composed
pointwise with the sibling scalar theme's three dispatch keys:

```text
gram dot X    with canonical Hermitian hook   ⇒  Matrix (\i j -> dot(X[i], X[j]))                    -- G = XᴴX
gram dot X    with B-weighted hook (inner_product_M) ⇒ Matrix (\i j -> bilinear_form(X[i], B, X[j])) -- G = XᴴBX
gram2 dot X Y with canonical Hermitian hook   ⇒  Matrix (\i j -> dot(Y[i], X[j]))                    -- cross G = YᴴX
```

The matrix lift is **two structural steps plus the inherited per-cell dispatch**:

1. **Double-loop materialization (the matrix-specific step).** The L2 form `Matrix (\i j -> dot
   X[j] X[i])` lowers to the nested `for i ∈ [0,k) { for j ∈ [0,k) { SS(i,j) = leaf(X[i], X[j]) }
   }` (`palace/linalg/nleps.cpp:525-531`). Each iteration is one scalar-leaf invocation; the loop
   nest is the cartesian product of the two basis index axes. The empty basis `k = 0` materializes
   as the `Matrix[0,0]` (the `if (k == 0) return;` early-return at
   `palace/linalg/nleps.cpp:515-518`, deflation skipped — `L2/gram` law 2). This step has **no
   analogue in the scalar sibling** (a single scalar has no index axes to range over).

2. **Per-cell dispatch (inherited pointwise from the sibling scalar theme).** Each cell `(i,j)` is
   exactly one [`inner-product-fold-specialization`](./inner-product-fold-specialization.md)
   instance on the operand pair `(X[i], X[j])`. The sibling theme's three orthogonal dispatch keys
   apply unchanged, per cell:
   - **Conjugation key** — the hook's per-element kernel. Canonical Hermitian `conj(x)·y` selects
     `dot`; unconjugated `x·y` selects `tdot`. NLEPS pins the Hermitian hook
     (`palace/linalg/nleps.cpp:529`, `linalg::Dot`), so every NLEPS Gram cell selects `dot`.
   - **Element-type key** — `real | complex`. NLEPS is complex (`Eigen::MatrixXcd SS`,
     `palace/linalg/nleps.cpp:524`); each cell lowers to the complex four-real-dot leaf
     (`palace/linalg/vector.cpp:674-685`). The real Gram would select the single Hypre pass
     (`palace/linalg/vector.cpp:665-672`) per cell. Inherited verbatim from the sibling theme's
     element-type key.
   - **Weight key** — `dot` hook ∈ {canonical, B-weighted}. The canonical hook gives `G = XᴴX`;
     the B-weighted hook (`inner_product_M`) gives `G = XᴴBX` via the `bilinear_form` leaf per
     cell (the mass-matrix / Rayleigh–Ritz overlap). The weight axis is the `gram` operator's
     variant axis 1 (`book/src/L2/gram.md:197-202`); NLEPS uses the canonical hook only.

The **selection is uniform across cells**: `gram`'s hook is a single field fixed for the whole
matrix, so all `k²` cells dispatch to the **same** leaf — the lowering selects the leaf once (from
the hook) and applies it `k²` times. This is the key structural simplification the matrix lift
buys over `k²` independent scalar lowerings: one dispatch decision, `k²` invocations.

### The cross-Gram member (a two-index-set degeneration, not a new dispatch key)

`gram2 dot X Y` materializes the `m×k` grid `Matrix (\i j -> leaf(Y[i], X[j]))` over two distinct
index sets (the off-diagonal block of the concatenation law, `L2/gram` law 5,
`book/src/L2/gram.md:153-156`). The dispatch is identical per cell — only the loop bounds and the
operand-source basis differ. NLEPS uses only the single-set form
(`palace/linalg/nleps.cpp:524-531`); the cross member is the general Rayleigh–Ritz overlap and the
block-law off-diagonal, lowered the same way.

## The per-cell conjugate-pair re-order (the core theme content)

This is the headline value-level reconciliation, inherited per cell from the sibling scalar theme
(`inner-product-fold-specialization` §"The conjugate-pair re-order") and pinned once at the
`gram` operator (`L2/gram` §"Conjugation convention (pinned via inner_product)",
`book/src/L2/gram.md:73-85`). The L1/L2 representation pins **arg-1 conjugated** (`xᴴ y`); the
Palace L0 surface pins **arg-2 conjugated** (`yᴴ x`). For the `dot` leaf they are complex
conjugates:

$$ x^{\mathsf H} y = \overline{\, y^{\mathsf H} x \,}. $$

**The matrix-specific shape of the re-order.** Palace's source writes the cell as
`SS(i, j) = linalg::Dot(GetComm(), X[i], X[j])` (`palace/linalg/nleps.cpp:529`), and the
free-function `linalg::Dot(comm, a, b)` conjugates **arg-2** (the deliberate L1 re-order recorded
at `inner_product.md:62-96` and verified against the `ComplexVector::Dot` body
`palace/linalg/vector.cpp:263-266`), so:

```text
Palace cell  SS(i,j) = linalg::Dot(comm, X[i], X[j]) = X[j]ᴴ X[i]   -- arg-2 (column j) conjugated
L2 cell      gram dot X [i,j]                        = X[j]ᴴ X[i]   -- arg-1 (column j) conjugated
```

i.e. **`SS(i,j)` already equals the L2 cell `inner_product(X[j], X[i]) = X[j]ᴴ X[i]`** — Palace's
choice to pass `X[i]` as the first (linear) operand and `X[j]` as the second (conjugated) operand
lands the conjugation on column `j`, which is precisely the L2 convention's conjugated operand.
So **the re-order is a no-op for the matrix as Palace writes it** (the operand order Palace chose
matches the L2 convention cell-for-cell). The re-order becomes load-bearing only if a downstream
implementation transposes the loop indices or swaps the operand positions: lowering `gram dot X
[i,j] = X[j]ᴴ X[i]` to a call `linalg::Dot(comm, a, b) = bᴴ a` requires `b = X[j]` (the conjugated
column), i.e. **`linalg::Dot(comm, X[i], X[j])`** — Palace's exact form — or equivalently
`conj(linalg::Dot(comm, X[j], X[i]))`.

**The Hermitian-symmetry interaction (matrix-specific).** Because the Gram is Hermitian for the
canonical hook (`G = Gᴴ`, `L2/gram` law 3, `book/src/L2/gram.md:130-135`), the cell `(j,i)` is the
conjugate of cell `(i,j)`: `G[j,i] = X[i]ᴴ X[j] = conj(X[j]ᴴ X[i]) = conj(G[i,j])`. The diagonal
`G[i,i] = X[i]ᴴ X[i]` is **convention-invariant** (real, `L2/gram` law 3 consequence); the
off-diagonal is the **conjugation-sensitive** part. So the re-order is observable per-cell exactly
where the scalar theme says: a downstream consumer that reads the **full complex value** of an
off-diagonal Gram cell sees the conjugate if the operand order is swapped. The
cross-layer-cross-cutter dot-callers census (`inner-product-fold-specialization` §"Caller-site
conjugation inventory") flags `nleps.cpp:529` as an **observable-unweighted** site precisely
because the Gram cells feed a complex LU solve (`palace/linalg/nleps.cpp:533-534`), not a real
projection — the full complex value is consumed, so the per-cell conjugation handedness is
load-bearing. This is the one place the re-order is genuine lowering work for `gram`, not a no-op.

## Symmetry-exploitation: a transparent perf-trick note (NOT a structural law)

Palace's `:525-531` double loop computes **all** `k²` cells — it does **not** exploit Hermitian
symmetry by computing only the lower (or upper) triangle and conjugate-reflecting the rest
(`L2/gram` §"Variant axes", `book/src/L2/gram.md:178-182,213-216`). The L1 RHS is the full
all-pairs grid. An equivalent **transparent performance trick** — "compute the upper triangle
(`k(k+1)/2` cells) + conjugate-mirror to fill the lower triangle" — would compute the same matrix
**modulo the per-cell IEEE non-law** (the mirrored cell is `conj` of the computed cell, which is
bit-exact under conjugation since conjugation is exact in IEEE-754; only the *choice* of which
cells to compute via `Dot` vs derive via `conj` differs, and `Dot(X[i],X[j])` vs
`conj(Dot(X[j],X[i]))` can differ at ULP level by the four-real-dot tree). Per CLAUDE.md
"Transparent performance tricks … algebraically equivalent to their unfolded form … the trick
gets a one-line note", this is recorded as a **one-line note on the lowering**, not a variant
axis: the L2 form is the full all-pairs fold; the triangle-mirror is an equivalent un-taken
materialization. (Palace's choice to compute all `k²` is the faithful one; a burn implementation
may mirror, accepting the ULP-level per-cell tree difference.)

## Per-cell summation-order recording

This is the **load-bearing-numerical content the `gram` entry defers to this theme** (`L2/gram`
§"Algebraic laws", the IEEE-754 per-cell reduction-tree non-law: "`gram` is order-agnostic for
value, but bit-identical reproduction of an L0 Gram requires matching each cell's pinned reduction
tree. Which tree a given lowered Gram pins is recorded by the L2>L1 lowering theme",
`book/src/L2/gram.md:166-176`). The L2 fold is order-agnostic for *value* per cell;
**bit-identical reproduction of an L0 Gram requires matching the pinned tree of every cell.** Each
cell's tree is exactly the sibling scalar theme's table entry for the selected leaf (read off the
verified `vector.cpp` bodies; single-rank scope — the per-rank kernel; the MPI tree-reduce
`Mpi::GlobalSum` is the second pinned layer in a multi-rank build, folded out per CLAUDE.md
scope):

| Gram instance | per-cell selected leaf | per-cell pinned reduction tree (from `inner-product-fold-specialization` §"Summation-order recording") |
|---|---|---|
| `gram dot X`, real, canonical hook | `dot(X[i], X[j])`, real | single Hypre `hypre_SeqVectorInnerProd` strided pass over `N` (`vector.cpp:665-672`), one per cell |
| `gram dot X`, complex, canonical hook (the NLEPS Gram) | `dot(X[i], X[j])`, complex | **four** real Hypre passes per cell (`xr·yr`, `xi·yi`, `xi·yr`, `xr·yi`), combined into `(Re,Im)` with `Im` cross-term sign `−` (`vector.cpp:674-685`) — `k²` independent four-real-dot trees |
| `gram dot X`, B-weighted hook | `bilinear_form(X[i], B, X[j])` | per cell a **two-stage** tree: the M-application reduction (`B`'s SpMV/quadrature tree, via the `Ax` workspace `operator.cpp:621-638`) **then** the four-real-dot reduction of `Dot(comm, B·X[i], X[j])` |

The matrix-level structure is **`k²` independent per-cell trees**: the Gram matrix as a whole has
no single pinned accumulation order (the cells are computed independently and written into
distinct `SS(i,j)` slots — there is no cross-cell accumulation), so the only pinned-tree content
is per-cell, inherited from the scalar theme. A downstream implementation reproducing a specific
Palace Gram bit-for-bit must pin each cell's tree (Hypre per-rank kernel + four-real-dot
combination for the complex NLEPS case), **and** respect the per-cell operand order (the re-order
§ above). The triangle-mirror trick (§ above) changes which cells get a `Dot` tree vs a `conj`,
so it is bit-distinguishable from the all-`k²` form even though value-equal.

## Applicability conditions

The dispatch lowering preserves the L2 Gram value when:

1. **Shared length axis per cell (the aligned-pass precondition).** Every column of `X` (and `Y`)
   shares one length axis `N`; each cell's leaf strides over that one axis (Palace's
   `MFEM_ASSERT(x.Size() == y.Size())`, `palace/linalg/vector.cpp:668`, per cell). For the
   B-weighted hook, additionally `B`'s codomain matches the conjugated-column axis and `B`'s
   domain matches the linear-column axis (`bilinear-form` §Applicability conditions).

2. **Hook fixed across the whole matrix.** `gram`'s `dot` hook is a single field; all `k²` cells
   dispatch to the same leaf (conjugation + weight selected once from the hook). Selecting the
   canonical Hermitian leaf vs the B-weighted leaf is value-bearing (different Gram: `XᴴX` vs
   `XᴴBX`) and not a free per-cell choice.

3. **Element-type conformance.** Element type is one shared `T ∈ {real, complex}` for the whole
   basis; the lowering dispatches every cell to the real Hypre kernel or the complex four-real-dot
   lift of the selected leaf. NLEPS is complex.

4. **Value-preservation vs bit-reproduction (the standard split, lifted per cell).** The grid of
   leaves computes the Gram's value (modulo the per-cell conjugate-pair re-order — condition 5).
   Bit-reproduction of a *specific* Palace Gram additionally requires (a) pinning **every cell's**
   reduction tree (the table in §"Per-cell summation-order recording"), (b) applying the per-cell
   operand order (Palace's `linalg::Dot(comm, X[i], X[j])`), and (c) computing all `k²` cells via
   `Dot` (not the triangle-mirror) if matching Palace's exact per-cell tree choice. The lowering
   is valid under **algorithmic-correctness** whenever 1–3 hold; under **bit-reproduction** only
   when the per-cell tree, operand order, and cell-coverage are matched (CLAUDE.md
   "load-bearing numerical tricks … non-associative reduction orderings … preserve as explicit
   algebraic claims").

5. **The per-cell conjugate-pair re-order is observable for full-complex Gram-cell consumers.** A
   Gram whose cells are consumed as a **real projection** (e.g. a real-symmetric Gram, or a Gram
   only used for its eigenvalues via a Hermitian solver) sees no re-order. A Gram whose
   **off-diagonal complex cells are consumed by value** — the NLEPS deflation Gram fed to the
   complex LU solve `SS.fullPivLu().solve(...)` (`palace/linalg/nleps.cpp:533-534`) — is the
   observable case (the cross-layer-cross-cutter census flags `nleps.cpp:529` observable-unweighted
   for exactly this reason). There the lowering must emit Palace's operand order
   `linalg::Dot(comm, X[i], X[j])` (or `conj(linalg::Dot(comm, X[j], X[i]))`) to land the
   conjugation on the right column.

## Justification kind

`algebraic` — the dispatch rule **is** the `gram` all-pairs definition law (`L2/gram` law 1) read
as a lowering, composed pointwise with the sibling scalar theme's already-firm conjugation /
element-type / weight dispatch (`inner-product-fold-specialization` §"The dispatch rewrite",
itself `algebraic`). The double-loop materialization is the cartesian-product structure of the
two basis index axes (the matrix-specific algebraic content); the per-cell conjugate-pair re-order
(`X[j]ᴴ X[i] = conj(X[i]ᴴ X[j])`) is a value-level algebraic identity verified directly against the
Palace `ComplexVector::Dot` body (`palace/linalg/vector.cpp:263-266`) and the cell-write
(`palace/linalg/nleps.cpp:529`). A **reduction-chain** flavour is present (each cell is a small-step
left-fold over `N`) and a **structural** flavour is present (the loop nest is shape-driven), but
the governing justification is the algebraic all-pairs-definition + inherited scalar dispatch, so
the theme is classified `algebraic` — consistent with its sibling. The symmetry-exploitation
triangle-mirror and the fused per-cell kernels are transparent-performance tricks; the per-cell
reduction-tree split is the load-bearing residue recorded in §"Per-cell summation-order recording".

## Speculative L1 operators

**None.** Both sides are existing vocabulary:

- LHS [`gram`](../L2/gram.md) is **firm** (cycle-022; all-pairs `inner_product` syntactic-identity
  laws on the positive Gram-build site `palace/linalg/nleps.cpp:524-531`).
- RHS leaves are the sibling scalar theme's leaves: [`dot`](../L1/dot.md) (firm; co-defines `dot`
  + `tdot`) and [`bilinear-form`](../L1/bilinear-form.md) (rough-in; the B-weighted hook member).

This theme proposes no new operators — it is the matrix-lift lowering edge between existing
vocabulary on both sides, built by lifting the sibling scalar theme's dispatch over the two basis
index axes.

Two evidentiary caveats carry over from the leaves / the LHS (neither is a status reduction on the
theme — the *dispatch structure* is firm):

- **`tdot` dispatch arm is type-API-surface-only.** Inherited from the sibling scalar theme:
  `ComplexVector::TransposeDot` has zero Palace call sites. NLEPS's Gram uses the Hermitian hook
  (`dot`), so the unconjugated-Gram arm (`gram` with the `tdot` hook → `XᵀX`) is structurally firm
  but behaviorally unexercised. The theme's behavioral weight is on the `dot` (Hermitian — the
  NLEPS deflation Gram) arm.

- **`bilinear-form` is rough-in at L1** (narrow variant-axis coverage). The B-weighted-hook Gram
  arm (`G = XᴴBX`) does not depend on its promotion: the arm's structure is firm (each cell is the
  composition `inner_product (apply_linop B X[i]) X[j]` lowering to `Dot(comm, B·X[i], X[j])`,
  directly verified at the scalar level). NLEPS uses the canonical hook only; the B-weighted Gram
  is the SLEPc/ROM Rayleigh–Ritz overlap, not exercised at the NLEPS site. The leaf's rough-in
  status lives at L1; it does not gate this theme.

## Verified-against

L0 evidence ranges (self-verified via `palace-codemap` read_range / search_text this invocation —
producer-citation-drift discipline, `verify-citation-range` producer-self-verification; paths
relative to `reference/`):

- `palace/linalg/nleps.cpp:524-531` — **the sole literal Gram-build site.** `Eigen::MatrixXcd
  SS(k, k);` (`:524`) then the nested loop `for (int i = 0; i < k; i++) { for (int j = 0; j < k;
  j++) { SS(i, j) = linalg::Dot(GetComm(), X[i], X[j]); } }` (`:525-531`, the cell body
  `SS(i, j) = linalg::Dot(GetComm(), X[i], X[j])` on `:529`). The double-loop materialization +
  the per-cell `dot`-leaf dispatch + the canonical Hermitian hook. **Self-verified via read_range
  (lines 504-537) + search_text (`linalg::Dot\(GetComm\(\), X` → exactly :529).**
- `palace/linalg/nleps.cpp:529` — the cell body, the only `linalg::Dot(GetComm(), X[i], X[j])`
  occurrence (search_text confirmed exactly one hit). The positive `XᴴX` build cell; per Palace's
  arg-2-conjugated `linalg::Dot`, `= X[j]ᴴ X[i] = inner_product(X[j], X[i])`. **Self-verified.**
- `palace/linalg/nleps.cpp:515-518` — the `k == 0` early-return (`if (k == 0) // no deflation
  { return; }`): the empty-basis identity (`gram dot [] = Matrix[0,0]`, `L2/gram` law 2) realized
  as the deflation skip. **Self-verified.**
- `palace/linalg/nleps.cpp:532-535` — the consumer (NOT a `gram` law): `const Eigen::MatrixXcd S =
  eig_opInv * Identity(k,k) - H` (`:532`), `SS = -S.fullPivLu().solve(SS)` (`:533`), `x2 =
  SS.fullPivLu().solve(x2)` (`:534`), back-projection `MatVecMult(X, S.fullPivLu().solve(x2))`
  (`:535`) — `deflate`'s complex LU solve consuming the full complex Gram value (the observable
  re-order witness). **Self-verified.**
- `palace/linalg/nleps.cpp:520-523` — the coordinate-extraction loop `x2(j) = b2(j) -
  linalg::Dot(GetComm(), x1, X[j])`: the `Xᴴ·` half (arg-1-conjugated convention applied to a
  vector rather than a basis column); flagged observable-unweighted at `:522` in the
  cross-layer-cross-cutter census. **Self-verified.**
- `palace/linalg/nleps.cpp:561-569` — `compute_residual`'s deflation: `MatVecMult(X,
  S.fullPivLu().solve(vv2))` (`:563`) + residual coords `rr2(j) = linalg::Dot(GetComm(), vv,
  X[j])` (`:568`). A second consumer of the Gram-solve (not a fresh Gram build). **Self-verified
  via read_range (lines 561-569).**
- `palace/linalg/nleps.cpp:614-619` — deflation-basis growth `X.resize(k+1); X[k] = v;
  H.conservativeResizeLike(...); H(k,k) = eig; k++`: the basis grows one column per converged
  eigenpair (the incremental-Gram rank-1 border, `L2/gram` law 6) — the Gram is rebuilt at the
  bordered `k+1` size on the next `deflated_solve`. **Self-verified.** (Range tightened from the
  enclosing `:613-619`; `:613` is `eigs[k] = eig;`, a related-but-distinct statement.)
- `palace/linalg/nleps.cpp:354-362` — the deflation-scheme literature anchors: Jarlebring/Koskela/
  Mele 2018 quasi-Newton (`:354-355`), SLEPc-NEP minimality index 1 (`:356`), Effenberger 2013
  successive eigenpair computation (`:357-358`). The standard-scheme anchor for the
  oblique-Galerkin deflation Gram. **Self-verified via read_range + search_text.**
- `palace/linalg/vector.cpp:263-266` — `ComplexVector::Dot` body `= x·conj(y) = yᴴ x` (arg-2
  conjugated): the per-cell conjugation kernel + the conjugate-pair re-order source. **Cited via
  the sibling scalar theme's verified evidence (read this invocation in
  `inner-product-fold-specialization.md:394-397`); inherited from the firm sibling.**
- `palace/linalg/vector.cpp:664-672` (real LocalDot single Hypre pass), `:674-685` (complex
  four-real-dot lift), `palace/linalg/operator.cpp:621-638` (weighted `Dot` two-stage) — the
  per-cell reduction trees. **Cited via the sibling scalar theme's verified evidence (the
  §"Summation-order recording" table); inherited from the firm sibling, not re-derived here.**

L2 / L1 anchors (read this invocation):

- `book/src/L2/gram.md` — the L2 all-pairs fold (LHS). Signature (`:42-50`), pinned conjugation
  convention (`:73-85`), all-pairs definition law 1 (`:117-122`), empty-basis law 2 (`:124-126`),
  Hermitian-symmetry law 3 (`:130-135`), concatenation/cross-Gram law 5 (`:153-156`),
  incremental-Gram law 6 (`:158-164`), the IEEE per-cell non-law + symmetry-exploitation note
  (`:166-182`), the variant axes (`:197-216`), the forward-reference to this theme (`:242-246`).
- `book/src/L2-L1/inner-product-fold-specialization.md` — the sibling scalar theme (firm). The
  per-cell dispatch keys (§"The dispatch rewrite", `:92-136`), the conjugate-pair re-order
  (§, `:158-220`), the summation-order table (§, `:222-251`), the caller-site conjugation
  inventory flagging `nleps.cpp:529` observable (`:301-329`). Every per-cell decision in this
  theme is one instance of that theme.
- `book/src/L1/dot.md` — the firm Hermitian / unconjugated per-cell leaf (RHS): `dot`/`tdot`
  (`:33-35`), the arg-1-conjugated convention (`:43`), the self-dot trick (`:49`).
- `book/src/L1/bilinear-form.md` — the rough-in B-weighted per-cell leaf (RHS): `xᴴ M y` (`:63`).
- `book/src/L2/inner_product.md` — the scalar parent (`L2/gram` lifts it): the pinned conjugation
  convention §"Conjugation convention (pinned)" (`:46-102`).

## Status

`firm` — the L2 LHS [`gram`](../L2/gram.md) is firm (cycle-022), the RHS leaves are existing
vocabulary (`dot`/`tdot` firm; `bilinear-form` rough-in but its B-weighted-hook dispatch arm is
firm), and the dispatch rule IS the `gram` all-pairs definition law (`L2/gram` law 1) read as a
lowering, composed pointwise with the **already-firm** sibling scalar theme
[`inner-product-fold-specialization`](./inner-product-fold-specialization.md). The matrix-specific
content — the double-loop materialization, the per-cell conjugate-pair re-order, the
symmetry-exploitation transparent note, and the per-cell pinned reduction tree — is read straight
off the **verified** positive Gram-build site (`palace/linalg/nleps.cpp:524-531`, cell body
`:529`) and the firm sibling theme's verified `vector.cpp` bodies. No literature inference, no
negative-anchor reconstruction, no speculative operator. This is the fifth chapter under the
`book/src/L2-L1/` Part (after `chebyshev-iteration-fusion`,
`linear-combination-fold-specialization`, `inner-product-fold-specialization`, and
`orthogonalize-composition-lowering`). A `lowering-verifier` audit confirming the per-cell
dispatch + the re-order + the per-cell summation-order table against the L0 source is the standard
follow-up, not a status reduction.

> **Coverage caveat (not a status reduction).** The literal `XᴴX` Gram-build appears at exactly
> **one** site in the whole Palace tree — `palace/linalg/nleps.cpp:524-531` (`search_text`
> `fullPivLu|Gram|deflat|SS\(` over `palace/**/*.cpp` returns the Gram cell + its solves only in
> `nleps.cpp`; the ROM path `palace/models/romoperator.cpp:757-765` does small-dense solves on a
> *reduced operator*, not an explicit `XᴴX` build, so it is not a `gram` instance — inherited from
> `L2/gram`'s coverage caveat). There is **no dedicated NLEPS/deflation unit test**. The firmness
> rests on (a) the dispatch being the `gram` all-pairs law composed with the firm sibling scalar
> theme's dispatch (both firm), and (b) the single build site being read directly. The
> single-algorithm concentration is recorded at the theme's granularity, not a firmness gate;
> promotion of the caveat to closed would follow a second Palace algorithm building an explicit
> Gram or a dedicated deflation unit test — neither blocks the firm status of the all-pairs-law +
> inherited-dispatch lowering.

## Open questions / caveats

- **Lifting note (reverse direction, working notes only — NOT in the high→low chapter body).**
  Lifting an L1 per-cell leaf grid *up* to the L2 `gram` fold is determinate: a `k×k` grid of
  `dot(X[i], X[j])` cells IS `gram dot X` with the canonical hook (the all-pairs definition law
  read in reverse), so the lift requires no additional structure beyond recognizing the cartesian
  index structure and naming the hook. The lift loses (a) the per-cell pinned reduction trees (the
  L2 fold is order-agnostic per cell), (b) the per-cell L0 arg-order/conjugation handedness (the
  L2 fold pins arg-1 per cell), and (c) the cell-coverage choice (all-`k²` vs triangle-mirror — the
  L2 fold has no materialization-order). So the lift is value-faithful but NOT bit-faithful, NOT
  handedness-faithful, and NOT materialization-faithful — re-lowering recovers the original Palace
  Gram only if the per-cell summation-order table, the per-cell operand order, AND the all-`k²`
  cell coverage are re-applied. This reverse-direction note lives here in working notes per the
  high→low layer-definition discipline; the formal chapter narrates only L2 → L1.

- **Per-cell tree independence is the matrix-specific structural fact.** Unlike a hypothetical
  matrix-level fused Gram kernel (e.g. a batched GEMM `XᴴX` that accumulates across cells in a
  shared tree), Palace's double-`Dot` loop computes `k²` **independent** trees with no cross-cell
  accumulation. A burn implementation using a single fused `XᴴX` matmul would pin a *different*
  (matrix-level) tree and would NOT bit-reproduce Palace's per-cell-`Dot` Gram even cell-for-cell.
  This is a genuine load-bearing-vs-transparent classification question for the downstream port: is
  the per-cell-`Dot` structure load-bearing (NLEPS depends on the exact Gram bits) or transparent
  (NLEPS only needs the Gram to LU-solve to within tolerance)? Surfaced as a new OQ
  (`gram-percell-dot-vs-fused-matmul-tree-loadbearing`) for a `lowering-verifier` /
  same-layer-cross-cutter follow-up — not resolvable from the source alone (needs the NLEPS
  convergence-sensitivity analysis). Not blocking: the value-level lowering is firm either way.

- **Carry-forward review from the sibling scalar theme
  (`inner-product-fold-specialization` §Open questions).** I reviewed the sibling's live
  follow-ups; none is small/in-scope to fold into *this* theme, and this theme consumes none of
  them as blockers:
  - its **lifting note** — mirrored here for the matrix lift above; no action needed on the scalar
    theme.
  - its **weighted-member two-stage reduction-tree** caveat — inherited verbatim by the B-weighted
    Gram arm's per-cell tree (the `bilinear_form` row of the per-cell table is two-stage). Tracked
    under the existing OQ `apply-linop-lowering-verifier-audit-cohort` exactly as the scalar theme
    records it; no new OQ needed for the Gram lift.
  - its **conjugate-pair re-order per-site audit** OQ — this theme adds one data point (the Gram
    cell `nleps.cpp:529` is observable-unweighted, already in the scalar theme's caller inventory);
    no separate audit needed.
  Recommend the integrator treat the sibling theme's follow-ups as unchanged — this Gram theme
  inherits them, does not add to them (except the per-cell-vs-fused-matmul OQ above, which is
  genuinely new to the matrix lift).

- **Plan / OQ bookkeeping (recommendation for the integrator).** This theme closes the `L2/gram`
  forward-reference (`book/src/L2/gram.md:242-246`, "L2>L1 lowering theme (forthcoming)") — the
  `gram` entry's §Dependencies and §"Algebraic laws" IEEE-non-law deferral now resolve to this
  chapter. Recommend the integrator (a) note in the `L2/gram` cross-reference that the forthcoming
  theme is now `gram-fold-specialization` (a layer-intro-author / lifter cross-reference refresh,
  NOT actioned here per dispatch-phase write discipline), and (b) surface the new OQ
  `gram-percell-dot-vs-fused-matmul-tree-loadbearing`. The L2-L1 `index.md` "two reduce-to-X fold
  siblings now both have matrix-and-scalar specialization themes" working-note refresh is
  layer-intro-author scope.

- **Coordination note for the integrator (shared-file overlap).** `book/src/L2-L1/index.md` and
  `book/src/SUMMARY.md` are shared with the parallel cycle-024 `deflate-composition-lowering` L2>L1
  abstractor. My proposed rows are **distinct and non-overlapping**: I append the
  `gram-fold-specialization` theme-list row + SUMMARY entry only. The `deflate` theme should append
  its own row. The two L2>L1 themes are siblings (both lower an NLEPS-deflation L2 operator) but
  distinct chapters — `gram` builds the matrix, `deflate` solves it; the rows do not collide.

```yaml
verified_against:
  - citation: palace/linalg/nleps.cpp:524-531
    verdict: supports
    audited_at: 2026-05-29T151441Z
    note: double-loop Gram-build materialization (SS decl :524 + nested loop :525-531); sole literal XHX build site (search_text)
  - citation: palace/linalg/nleps.cpp:529
    verdict: supports
    audited_at: 2026-05-29T151441Z
    note: cell body SS(i,j)=linalg::Dot(GetComm(),X[i],X[j]) = X[j]ᴴX[i]; conjugate-pair re-order is no-op for Palace's operand order (chain verified nleps:529 -> vector.cpp:265-266 -> dot.md:43)
  - citation: palace/linalg/nleps.cpp:515-518
    verdict: supports
    audited_at: 2026-05-29T151441Z
    note: k==0 early-return = empty-basis Matrix[0,0] (L2/gram law 2)
  - citation: palace/linalg/nleps.cpp:520-523
    verdict: supports
    audited_at: 2026-05-29T151441Z
    note: x2 coordinate loop (Xᴴ· half); :522 observable-unweighted
  - citation: palace/linalg/nleps.cpp:532-535
    verdict: supports
    audited_at: 2026-05-29T151441Z
    note: deflation complex LU solve (:533-534) consuming full Gram value -> off-diagonal re-order observable
  - citation: palace/linalg/nleps.cpp:561-569
    verdict: supports
    audited_at: 2026-05-29T151441Z
    note: compute_residual second Gram-solve consumer (:563 MatVecMult, :568 rr2 coords)
  - citation: palace/linalg/nleps.cpp:613-619
    verdict: partially-supports
    audited_at: 2026-05-29T151441Z
    note: enclosing range encloses all cited basis-growth constructs but :613 is eigs[k]=eig; tight range is :614-619 (off-by-one at low boundary, in-bounds, value-faithful)
  - citation: palace/linalg/nleps.cpp:354-362
    verdict: supports
    audited_at: 2026-05-29T151441Z
    note: Jarlebring/Koskela/Mele 2018 (:354-355), SLEPc-NEP minimality 1 (:356), Effenberger 2013 (:357-358)
  - citation: palace/linalg/vector.cpp:263-266
    verdict: supports
    audited_at: 2026-05-29T151441Z
    note: ComplexVector::Dot = x·conj(y) = yᴴx (arg-2 conjugated); the re-order source kernel
  - citation: palace/linalg/vector.cpp:665-672
    verdict: supports
    audited_at: 2026-05-29T151441Z
    note: real LocalDot single Hypre hypre_SeqVectorInnerProd pass (per-cell real tree)
  - citation: palace/linalg/vector.cpp:674-685
    verdict: supports
    audited_at: 2026-05-29T151441Z
    note: complex LocalDot four-real-dot lift; Re=xr·yr+xi·yi, Im=xi·yr−xr·yi (per-cell complex tree)
  - citation: palace/linalg/operator.cpp:621-638
    verdict: supports
    audited_at: 2026-05-29T151441Z
    note: weighted two-stage Dot (Ax workspace then Dot(comm,Ax,y)); both Operator and ComplexOperator overloads (bilinear_form per-cell tree)
  - citation: palace/linalg/vector.cpp:668
    verdict: does-not-support-at-cited-line-667
    audited_at: 2026-05-29T151441Z
    note: MFEM_ASSERT(x.Size()==y.Size()) is at :668, not the theme's previously-cited :667 (:667 is `static hypre::HypreVector X, Y;`); corrected to :668 in-theme; inherited carry-forward drift shared with inner_product.md + inner-product-fold-specialization.md
```
