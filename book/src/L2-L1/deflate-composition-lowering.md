# deflate-composition-lowering

The composition-fan-down rotation for the oblique / Galerkin deflation projector. Lowers the L2
named composition [`deflate`](../L2/deflate.md) — the `coords ▷ (schur-)solve ▷ back-project`
pipeline parameterised by `op.block ∈ {Galerkin, Schur}` and the inner-product hook `op.dot` —
into its L1 form by **mapping each composition stage onto the L1/L2 leaf that realises it** in
Palace's fused `deflated_solve` block (`palace/linalg/nleps.cpp:505-537`). Narrated forward: the
one named L2 composition **fans down** into a fixed small-step sequence of leaf calls — a `dot`
coordinate-extraction fold, a [`gram`](../L2/gram.md) Gram build, one-or-three
[`lu_solve`](../L1/lu_solve.md) small-dense solves (the `op.block` variant axis), a
[`linear_combination`](../L2/linear_combination.md) back-projection, and a final `axpy`
subtraction. This theme **inherits `deflate`'s `partly-constructive` status**: the **Schur-form**
fan-down is read from a positive source block, but the **Galerkin-core** fan-down (the single
bare-Gram `lu_solve(XᴴX, c)`) is **constructive** — Palace never positively exhibits a bare-Gram
deflation solve (§ Status). Sibling to the parallel-cycle
[`gram-fold-specialization`](./gram-fold-specialization.md) (the Gram-build fold this theme consumes
whole), and to
[`orthogonalize-composition-lowering`](./orthogonalize-composition-lowering.md) (the
**related-but-distinct** Gram-Schmidt projector — the over-unification guard the L2 entry pins,
`book/src/L2/deflate.md:248-276`, carries into the lowering: the decisive distinguisher is *this*
theme's `lu_solve` stage, absent from `orthogonalize`'s fan-down).

## Slug

`deflate-composition-lowering`

## Status

`partly-constructive` — the **structural fan-down is firm** (each L2 composition stage maps onto a
positively-sourced L1/L2 leaf call in the `deflated_solve` block) and the **Galerkin-core
sub-part of the solve stage is constructive** (literature-anchored, not positively sourced),
inherited verbatim from the L2 [`deflate`](../L2/deflate.md) entry (`book/src/L2/deflate.md:362-415`).

- **Firm part** (the Schur-form fan-down). Every stage of the rewrite is read directly from the
  **positive** `deflated_solve` block (`palace/linalg/nleps.cpp:505-537`): the coordinate
  extraction is the positive `linalg::Dot` loop (`palace/linalg/nleps.cpp:519-523`), the Gram
  build is the positive double-loop (`palace/linalg/nleps.cpp:524-531`), the Schur block is the
  positive `S = λI − H` (`palace/linalg/nleps.cpp:532`), the three solves are positive
  `fullPivLu().solve` calls (`palace/linalg/nleps.cpp:533-535`), the back-projection is the
  positive `MatVecMult` (`palace/linalg/nleps.cpp:535`, defined `:329-347`), and the subtraction is
  the positive in-place `AXPY` (`palace/linalg/nleps.cpp:536`). All target leaves are firm L1/L2
  vocabulary: [`dot`](../L1/dot.md), [`gram`](../L2/gram.md), [`lu_solve`](../L1/lu_solve.md),
  [`linear_combination`](../L2/linear_combination.md). The stage-to-leaf map is a syntactic
  reduction-chain on positive source.

- **Constructive sub-part** (the **Galerkin-core solve fan-down**: `op.block = Galerkin`, `S = I`).
  When the central `op.block` variant takes its `Galerkin` value, the L2 coordinate-solve stage
  `lu_solve(XᴴX, c) = (XᴴX)⁻¹·(Xᴴ v)` lowers to a **single** L1 `lu_solve` against the bare Gram
  `G = XᴴX`. This single-bare-Gram-solve fan-down is **NOT** read from a positive Palace site —
  Palace only exhibits the *Schur-wrapped* three-solve form (`palace/linalg/nleps.cpp:533-535`).
  It is materialised from (i) the deflation-scheme literature (Jarlebring–Koskela–Mele 2018;
  Effenberger 2013, `palace/linalg/nleps.cpp:354-362`), which defines the oblique-Galerkin
  projector the Schur form specialises, and (ii) the **negative anchor** that no bare-Gram
  `(XᴴX)⁻¹` deflation solve appears anywhere in Palace (`search_text` for a Gram-only deflation
  projection across `palace/linalg/*.cpp` returns only the Schur-wrapped `nleps.cpp` block; the L2
  entry records the same anchor, `book/src/L2/deflate.md:343-348, 386-391`). The negative anchor is
  evidence **for** the Galerkin-core fan-down being a faithful `S = I` reduction of the
  positively-sourced Schur fan-down; it does NOT license asserting the bare-Gram solve as a
  positive Palace lowering.

- **Promotion condition** (what makes this theme firm — identical to the L2 entry's, NOT closed
  here): a positive Palace source site exhibiting the bare Galerkin deflation solve
  `lu_solve(XᴴX, c)` directly (a future linear-EVP deflation path, a preconditioner deflation, or a
  ROM Galerkin projection using the Gram inverse without the `S = λI − H` Schur wrapping). Until
  such a site is dissected, the Galerkin-core fan-down stays constructive and this theme stays
  `partly-constructive`. Should `deflate` be scoped to the NLEPS Schur form only (a
  `same-layer-cross-cutter` call, not this dispatch's), this theme would become `firm` on positive
  structure with the Galerkin-core fan-down demoted to a literature note. **This theme does not make
  that call and does not close the gate.**

The promotion condition closes the *whole-theme* gate; the firm Schur-form fan-down is already firm
and not blocked by it (per the CLAUDE.md `partly-constructive` invariant: the structural
decomposition IS firm; only the constructive sub-part carries the open gate).

## L2 form (LHS)

The L2 form is the named `coords ▷ (schur-)solve ▷ back-project` composition over a basis prefix
`X` and a vector `v`, parameterised by the coordinate-solve block and the inner-product hook
([`deflate`](../L2/deflate.md) §Signature, `book/src/L2/deflate.md:55-66`):

```text
deflate :: (op: DeflateOp, X: Basis[N, k], v: Tensor[N]) -> Tensor[N]

type DeflateOp = { dot: (Tensor[N], Tensor[N]) -> Scalar     -- inner-product hook
                 , block: GramBlock[k] }                      -- coordinate-solve block

type GramBlock[k] = Schur { S: Matrix[k, k] }    -- coords solved against −S⁻¹(XᴴX) then S⁻¹
                  | Galerkin                       -- coords solved against XᴴX (S = I)

deflate op X v = v − linear_combination (zip (coords-solve op X v) X)   -- = v − X·(coordinate solve)

coords-solve op X v =
  let c = [ op.dot X[j] v | j <- 0..k-1 ]            -- = Xᴴ v   (deflation coordinates; k dots)
      G = gram op.dot X                                -- = XᴴX    (the Gram matrix)
  in case op.block of
       Galerkin    -> lu_solve G c                     -- (XᴴX)⁻¹·(Xᴴ v)     [Galerkin core, S = I]
       Schur { S } -> let SS = lu_solve S (scale (-1) G)  -- SS = −S⁻¹(XᴴX)   (Schur complement)
                          c' = lu_solve SS c              -- SS⁻¹·c
                      in lu_solve S c'                    -- S⁻¹·c'
```

The composition is value-producing and stateless: a fixed-size deflation-basis prefix folds into
one projected vector, with no convergence predicate and no monadic state threading
([`deflate`](../L2/deflate.md) §Context, `book/src/L2/deflate.md:40-45`). At L2 the **`op.block`
variant** (Galerkin single-solve vs Schur triple-solve) is the central axis made visible
([`deflate`](../L2/deflate.md) §Variant axes, `book/src/L2/deflate.md:330-348`); this theme records
which L1 `lu_solve` sequence each variant pins. The shape precondition is `X` **full column rank**
(so `XᴴX` is invertible) and **NOT** orthonormal — the raw normalized-eigenvector basis
(`palace/linalg/nleps.cpp:606-619`).

## L1 form (RHS)

The L1 form is the fan-down of the L2 composition stages onto leaf calls, in the order the source
block performs them (`palace/linalg/nleps.cpp:505-537`). Each stage names the firm leaf it lowers
to. The element type is **complex** at the Palace site (`Eigen::MatrixXcd` / `ComplexVector`); the
conjugation lives in the `dot` / `gram` leaves (§ Conjugation, below).

### Stage 0 — empty-basis short-circuit (`k = 0`)

The `k == 0` early-return (`palace/linalg/nleps.cpp:515-518`) lowers `deflate op [] v = v` to the
identity — no leaf call at all. This is the L2 empty-basis law 1
([`deflate`](../L2/deflate.md):183-184) realised as a source branch.

### Stage 1 — coordinate extraction (`c = Xᴴ v`)

The L2 `[ op.dot X[j] v | j <- 0..k-1 ]` fold lowers to a `k`-iteration loop of the firm L1
[`dot`](../L1/dot.md) leaf:

```text
for j in 0..k-1:
  c[j] = dot(X[j], v)          -- = X[j]ᴴ v   (arg-1-conjugated; book/src/L1/dot.md:43)
```

Source: the loop `x2(j) = b2(j) − linalg::Dot(GetComm(), x1, X[j])` (`palace/linalg/nleps.cpp:519-523`,
the decisive line `:522`). The `b2 −` term is the extended-block RHS (the NLEPS-specific shift);
the `−linalg::Dot(GetComm(), x1, X[j])` is the deflation coordinate `X[j]ᴴ x1`. Palace's
free-function `linalg::Dot(comm, a, b) = bᴴ a` conjugates its arg-2 (`X[j]`); under the L1 `dot`
arg-1-conjugated convention this re-orders to `dot(X[j], v)` (`book/src/L1/dot.md:43`). The
**conjugation is pinned once here** — the simplification the combinator buys the lowering
([`deflate`](../L2/deflate.md) semantics point 2, `:154-162`).

### Stage 2 — Gram build (`G = XᴴX`)

The L2 `gram op.dot X` lowers to the firm L2 [`gram`](../L2/gram.md) all-pairs `inner_product`/`dot`
fold — **consumed whole, not re-derived here**. Its own L2>L1 fan-down (the `k²` `dot` double-loop,
Hermitian-symmetry trick, single vs all-pairs) is the parallel-cycle
[`gram-fold-specialization`](./gram-fold-specialization.md) theme's content; this theme cites it and
does not duplicate it.

```text
G = gram(op.dot, X)            -- entry (i,j) = dot(X[i], X[j]) = X[i]ᴴ X[j]
```

Source: the double-loop `SS(i, j) = linalg::Dot(GetComm(), X[i], X[j])`
(`palace/linalg/nleps.cpp:524-531`, the assignment at `:529`); the `Eigen::MatrixXcd SS(k, k)`
materialisation at `:524`. (Palace names the Gram buffer `SS` and overwrites it in place at `:533`
with the Schur-modified form — see Stage 3; the L2 `gram` value is the buffer's *initial* content.)

### Stage 3 — coordinate solve (the `op.block` variant axis)

This is the **fan-out point** — the one L2 `coords-solve` stage lowers to **different L1 `lu_solve`
sequences** per `op.block`. The fan-down is the load-bearing content of this theme.

**Schur variant (positively sourced; firm).** Three [`lu_solve`](../L1/lu_solve.md) calls against the
extended-block linearization `S = λI − H` and the Schur-modified Gram `SS`:

```text
S  = scale(eig_opInv) Identity(k) − H            -- the Schur block (palace/linalg/nleps.cpp:532)
SS = lu_solve(S, scale(-1) G)                     -- multi-RHS k×k: SS = −S⁻¹·(XᴴX)   (:533)
c' = lu_solve(SS, c)                              -- single-RHS:    c' = SS⁻¹·c        (:534)
y  = lu_solve(S, c')                              -- single-RHS:    y  = S⁻¹·c'        (:535, inside MatVecMult arg)
```

Source (all positive): `S = eig_opInv * Eigen::MatrixXcd::Identity(k, k) − H`
(`palace/linalg/nleps.cpp:532`); `SS = -S.fullPivLu().solve(SS)` (`:533`, the multi-RHS `k×k`
solve — `lu_solve`'s column-wise multi-RHS form, `book/src/L1/lu_solve.md:58`);
`x2 = SS.fullPivLu().solve(x2)` (`:534`); the `S.fullPivLu().solve(x2)` inside the `MatVecMult` arg
(`:535`). The factorization kernel is full-pivot LU — `lu_solve`'s load-bearing numerical-kernel
axis, inherited (`book/src/L1/lu_solve.md:47, 63`). The nested `lu_solve(S, lu_solve(SS, ·))` shape
is `lu_solve` law 5's witnessed compositional form (`book/src/L1/lu_solve.md:59`).

**Galerkin variant (constructive; § Status).** A **single** [`lu_solve`](../L1/lu_solve.md) against
the bare Gram:

```text
y = lu_solve(G, c)                                -- y = (XᴴX)⁻¹·(Xᴴ v)   [S = I; NOT positively sourced]
```

This single-solve fan-down is the **constructive sub-part** — it is the `S = I` reduction of the
Schur triple-solve (`SS = −I⁻¹·G = −G`, `SS⁻¹·c = −G⁻¹·c`, `S⁻¹·(·) = (·)`, composing to
`−(−G⁻¹·c) = G⁻¹·c` — the bare-Gram solve), materialised from literature + the negative anchor
(no bare-Gram deflation solve in Palace, `book/src/L2/deflate.md:343-348`). It is **not** read from
a positive site (§ Status).

### Stage 4 — back-projection (`X·y`)

The L2 `linear_combination (zip y X)` lowers to the firm L2
[`linear_combination`](../L2/linear_combination.md) over the basis columns — at L0 the `MatVecMult`
primitive:

```text
Xy = linear_combination(zip(y, X))     -- = X·y = Σ_j y[j]·X[j]   (length-k linear combination)
```

Source: `const ComplexVector XSx2 = MatVecMult(X, S.fullPivLu().solve(x2))`
(`palace/linalg/nleps.cpp:535`); `MatVecMult` is defined at `:329-347` (the `z = 0; for j:
AXPBYPCZ(…)` fold with the complex real/imag split). At `:535` the inner `S.fullPivLu().solve(x2)`
is Stage-3's last solve `y`, so the source **fuses** Stage 3's final `S⁻¹·` with Stage 4's `X·` into
one expression — the L2 form un-fuses them into a `lu_solve` ▷ `linear_combination` composition.

### Stage 5 — subtraction (`v − X·y`)

The L2 `v − …` lowers to the firm `axpy` term (`y = −1·Xy + v`), in place on the destination:

```text
v ← axpy(-1, Xy, v)            -- v ← v − X·y
```

Source: `linalg::AXPY(-1.0, XSx2, x1)` (`palace/linalg/nleps.cpp:536`), in place on `x1`. The
**in-place destination** (`x1` is both the input `v` and the output) is an L2>L1 transparent-perf
concern (the standard BLAS in-place / output-aliasing axis), not part of the L2 signature
([`deflate`](../L2/deflate.md) semantics point 3, `:164-169`). The L2 form is out-of-place
(`v − …`); the in-place buffer is the fan-down detail.

## Applicability conditions

- **`X` full column rank** (so `XᴴX` / `S` / `SS` are invertible — the `lu_solve` invertibility
  precondition, `book/src/L1/lu_solve.md:45`). Palace's `X` is the converged invariant-pair basis,
  full-rank by construction (distinct eigenvectors, `palace/linalg/nleps.cpp:606-619`).
- **`X` NOT assumed orthonormal** — the raw normalized-eigenvector basis. This is exactly why the
  `lu_solve` (Stage 3) is load-bearing and the projector is oblique, not orthogonal
  ([`deflate`](../L2/deflate.md) semantics point 1, `:146-152`; the over-unification guard,
  `:248-276`). Were `X` orthonormal the fan-down would collapse to `orthogonalize`'s Gram-solve-free
  `[dot, axpy]` chain (`book/src/L2-L1/orthogonalize-composition-lowering.md`) — but it is not, so
  Stage 3 stays.
- **`op.block = Schur` for the firm fan-down**; `op.block = Galerkin` invokes the constructive
  single-solve fan-down (§ Status). The hook `op.dot` (canonical Hermitian / `B`-weighted) is a
  closure substitution into the `dot` / `gram` leaves — invariant to the fan-down structure
  ([`deflate`](../L2/deflate.md) law 6, `:214-218`).
- **Element type complex** at the Palace site; the real case is absorbed by the `dot` /
  `linear_combination` leaves (conjugation lives in `dot`).

## Justification kind

**reduction-chain** (primary) — the L2 composition stages map onto a fixed small-step sequence of
L1/L2 leaf calls in the positive `deflated_solve` block, in source order (Stage 0 short-circuit →
Stage 1 `dot`-fold → Stage 2 `gram` → Stage 3 `lu_solve` sequence → Stage 4 `linear_combination` →
Stage 5 `axpy`). The Schur sub-part is **algebraic/structural** on positive source (each stage is a
read leaf call); the Galerkin sub-part is **constructive** on negative anchors + literature
(§ Status). The fusion the source performs (Stage 3's final `S⁻¹·` folded into Stage 4's `X·` at
`:535`) is a transparent-performance un-fusion the L2 form makes explicit.

## Conjugation convention (pinned)

The deflation coordinate is `X[j]ᴴ v` — the **basis vector is the conjugated argument** — matching
the L1/L2 arg-1-conjugated `dot` convention `⟨x, y⟩ = xᴴ y` (`book/src/L1/dot.md:43`). Palace writes
`linalg::Dot(GetComm(), x1, X[j])`; under its free-function order `linalg::Dot(comm, a, b) = bᴴ a`
the C++ arg-2 (`X[j]`) is conjugated, which is the L1 `dot`'s arg-1 once re-ordered. The Gram entry
is `G(i,j) = X[i]ᴴ X[j]` (`palace/linalg/nleps.cpp:529`), consistent. Pinning the conjugation once
at the fan-down boundary is the simplification this lowering buys the NLEPS dissection
([`deflate`](../L2/deflate.md):154-162).

## Over-unification guard (inherited)

The L2 entry's `deflate` vs `orthogonalize` guard (`book/src/L2/deflate.md:248-276`) carries into
the lowering: the decisive distinguisher between the two compositions' fan-downs is **Stage 3, the
`lu_solve`**. `orthogonalize`'s fan-down
([`orthogonalize-composition-lowering`](./orthogonalize-composition-lowering.md)) is a
Gram-solve-free `[dot, axpy]` sequence (sequential rank-1 subtraction over an orthonormal basis);
`deflate`'s fan-down inserts the Gram build (Stage 2) and the `lu_solve` (Stage 3) precisely because
`X` is non-orthonormal. A future unification of the two themes must **NOT** erase Stage 3 — doing so
silently assumes `XᴴX = I` and changes the algorithm ([`deflate`](../L2/deflate.md):230-234, the
orthogonality non-law). They share Stages 1, 4, 5 (the `dot` extraction, the `X·` back-projection,
the `axpy` subtraction); they differ at Stages 2–3.

## Verified-against

All ranges `read_range`-verified via the `palace-codemap` MCP this dispatch (paths relative to
`reference/`):

- `palace/linalg/nleps.cpp:505-537` — the positive `deflated_solve` block; the complete fan-down
  target. `auto deflated_solve =` at `:505`; closing `};` at `:537`.
- `palace/linalg/nleps.cpp:508-513` — the source's own block-elimination comment naming the Schur
  complement `SS = (B − A T⁻¹ U) = − XᴴX·S⁻¹` (`:512`) and `x1 = x1 − X S x2` (`:513`) — the
  positive evidence the projector is Schur-modified, not bare Gram.
- `palace/linalg/nleps.cpp:515-518` — `if (k == 0) { return; }` — Stage 0 empty-basis short-circuit.
- `palace/linalg/nleps.cpp:519-523` — Stage 1 coordinate-extraction loop;
  `x2(j) = b2(j) − linalg::Dot(GetComm(), x1, X[j])` at `:522`.
- `palace/linalg/nleps.cpp:524-531` — Stage 2 Gram build; `Eigen::MatrixXcd SS(k, k)` at `:524`,
  `SS(i, j) = linalg::Dot(GetComm(), X[i], X[j])` at `:529`.
- `palace/linalg/nleps.cpp:532` — Stage 3 Schur block `S = eig_opInv * Identity(k,k) − H`.
- `palace/linalg/nleps.cpp:533` — Stage 3 multi-RHS `SS = -S.fullPivLu().solve(SS)` = `−S⁻¹(XᴴX)`.
- `palace/linalg/nleps.cpp:534` — Stage 3 single-RHS `x2 = SS.fullPivLu().solve(x2)` = `SS⁻¹·c`.
- `palace/linalg/nleps.cpp:535` — Stage 3+4 fused `XSx2 = MatVecMult(X, S.fullPivLu().solve(x2))` =
  `X·(S⁻¹·c')`.
- `palace/linalg/nleps.cpp:536` — Stage 5 `linalg::AXPY(-1.0, XSx2, x1)` = `x1 ← x1 − X·(…)`.
- `palace/linalg/nleps.cpp:329-347` — `MatVecMult(const std::vector<ComplexVector>&X, const Eigen::VectorXcd&y)`
  (`:329`), the back-projection primitive (`z = 0; for j: AXPBYPCZ(…)`, closing `}` at `:347`).
- `palace/linalg/nleps.cpp:354-362` — the deflation-scheme literature anchors: Jarlebring–Koskela–Mele
  2018 (`:354`), Effenberger 2013 (`:357`), SLEPc-NEP minimality index 1 (`:356`) — the literature
  anchor for the Galerkin-core constructive fan-down (§ Status).
- `palace/linalg/nleps.cpp:606-619` — deflation-basis growth (`X.resize(k+1)` at `:614`, `X[k] = v`
  at `:615`, `k++` at `:619`) — confirms `X` is the raw normalized-eigenvector basis (NOT
  orthonormalized), the non-orthonormal precondition.
- `palace/linalg/nleps.cpp:562-563` — the residual-site reuse of the back-projection
  (`S = lam·I − H` at `:562`, `XSvv2 = MatVecMult(X, S.fullPivLu().solve(vv2))` at `:563`) — Stages
  3+4 reused on the residual (consumer relationship; see `book/src/L1/nleps_deflated_residual.md`).
- `palace/linalg/nleps.cpp:664-667` — the Jacobian deflation terms (`S = eig·I − H` at `:664`,
  `Sv2 = S.fullPivLu().solve(v2)` at `:665`, `XSv2 = MatVecMult(X, Sv2)` at `:666`,
  `XSSv2 = MatVecMult(X, S.fullPivLu().solve(Sv2))` at `:667`) — Stages 3+4 reused with carried
  coordinates (no fresh Stage-1 `dot`).
- `book/src/L2/deflate.md` (partly-constructive, this cycle) — the LHS L2 composition: signature
  (`:55-66`), coordinate-solve body (`:96-109`), semantics points 1–3 (`:146-169`), laws (`:171-246`),
  over-unification guard (`:248-276`), variant axes (`:326-360`), Status (`:362-415`).
- `book/src/L1/lu_solve.md` (firm, cycle-022) — Stage 3 leaf: invertibility precondition (`:45`),
  full-pivot kernel (`:47, :63`), RHS-linearity (`:56`), multi-RHS column-wise (`:58`),
  solve-composition (`:59`).
- `book/src/L1/dot.md:43` — Stage 1 leaf: the arg-1-conjugated `⟨x,y⟩ = xᴴ y` convention.
- `book/src/L2/gram.md` (firm, cycle-022) — Stage 2 leaf: the `XᴴX` builder (consumed whole; its own
  fan-down is `gram-fold-specialization`).
- `book/src/L2/linear_combination.md` (firm, cycle-018) — Stage 4 leaf: the `X·y` back-projection
  fold (`MatVecMult` = length-`k` linear combination).
- `book/src/L2-L1/orthogonalize-composition-lowering.md` (firm, cycle-019) — the related-but-distinct
  Gram-Schmidt projector fan-down (over-unification guard, inherited).
- `book/src/L1/nleps_deflated_residual.md` (firm, cycle-022) — the consumer reusing Stages 3+4 on a
  residual (`:60` non-orthonormal-basis fact; `:109` over-unification guard from the other direction).

## Working notes (reverse-direction lifting; NOT chapter content)

- **Lift L1→L2 (how the source block lifts to the named composition).** The source's fused Stage
  3+4 expression (`:535`) is the first thing the lift must un-fuse: recognising `MatVecMult(X,
  S.fullPivLu().solve(x2))` as `linear_combination ∘ lu_solve` rather than a monolithic op is the
  load-bearing lift step. The `SS` buffer name aliasing (Gram, then Schur-modified Gram) at
  `:524`→`:533` is the second: the lift must track that `SS` holds *two distinct L2 values* across
  the in-place overwrite. Both are working-notes observations about the reverse direction; the
  formal chapter narrates only forward (high→low).
- **Galerkin-core promotion watch.** The promotion gate (positive bare-Gram-solve site) is the SAME
  gate as the L2 entry's — this theme does not introduce a second gate. When a future linear-EVP /
  preconditioner / ROM-Galerkin deflation site is dissected and exhibits `lu_solve(XᴴX, c)`
  positively, BOTH the L2 entry and this theme promote together (a lowering-verifier UNBLOCK +
  follow-up ENACT, per the partly-constructive promotion checklist). Recorded as OQ below.

```yaml
verified_against:
  - citation: palace/linalg/nleps.cpp:505-537
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: firm Schur-form fan-down; every Stage 0-5 anchor zero-drift (citecheck --anchor)
  - citation: palace/linalg/nleps.cpp:508-513
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: source block-elimination comment; :512 Schur complement, :513 back-projection
  - citation: palace/linalg/nleps.cpp:515-518
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: Stage 0 k==0 short-circuit
  - citation: palace/linalg/nleps.cpp:519-523
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: Stage 1 dot-fold; decisive :522 zero-drift
  - citation: palace/linalg/nleps.cpp:524-531
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: Stage 2 Gram build; :524 materialization, :529 assignment zero-drift; SS buffer-aliasing confirmed
  - citation: palace/linalg/nleps.cpp:532
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: Stage 3 Schur block S = eig_opInv*I - H
  - citation: palace/linalg/nleps.cpp:533
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: Stage 3 multi-RHS solve SS = -S^-1(XHX) (lu_solve law 4)
  - citation: palace/linalg/nleps.cpp:534
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: Stage 3 single-RHS solve c' = SS^-1 c
  - citation: palace/linalg/nleps.cpp:535
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: Stage 3+4 fused MatVecMult(X, S^-1 c'); L2 un-fuse faithful
  - citation: palace/linalg/nleps.cpp:536
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: Stage 5 in-place AXPY(-1, XSx2, x1)
  - citation: palace/linalg/nleps.cpp:329-347
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: MatVecMult back-projection primitive (:329 sig, :347 close)
  - citation: palace/linalg/nleps.cpp:354-362
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: literature anchors (Jarlebring-Koskela-Mele 2018 :354, SLEPc-NEP minimality :356, Effenberger 2013 :357)
  - citation: palace/linalg/nleps.cpp:606-619
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: non-orthonormal precondition; only Norml2-normalization at :610-611, no orthonormalization
  - citation: palace/linalg/nleps.cpp:562-563
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: residual-site reuse of Stages 3+4 (still Schur-wrapped)
  - citation: palace/linalg/nleps.cpp:664-667
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: Jacobian reuse of Stages 3+4 with carried coordinates (still Schur-wrapped)
  - citation: book/src/L2/deflate.md:343-348
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: negative anchor (no bare-Gram solve in Palace) re-confirmed complete by exhaustive *.cpp dense-solve search
  - citation: book/src/L1/dot.md:43
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: arg-1-conjugated dot convention pinned at Stage 1
  - citation: book/src/L1/lu_solve.md:58
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: multi-RHS column-wise law 4 (witnessed :533)
  - citation: book/src/L1/lu_solve.md:59
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: solve-composition law 5 (witnessed nested :533-534)
gate_verdict:
  shared_gate: bare-Galerkin-core-positive-source-site
  status: stays-gated-correctly
  audited_at: 2026-05-29T15:19:15Z
  finding: >-
    Exhaustive codemap search of every dense .solve()/.inverse()/LU/LDLT/QR/Cholesky
    site in palace/*.cpp found NO unwrapped bare-Gram (XHX)^-1 deflation solve. The
    one near-candidate romoperator.cpp:757-765 solves against Ar = V^H A V (ROM-projected
    system operator pencil, per romoperator.cpp:74 + :729-734), NOT a Gram matrix.
    Negative anchor correct AND complete; NLEPS-scoped is acceptable; partly-constructive
    correctly held across all 3 shared references.
```
