---
agent: combinator-miner
invoked_at: 2026-05-29T051532Z
scope: Pattern proposal — deflation-subspace projection (deflate / gram) in SLEPc-NEP
status: integrated
integrated_at: 2026-05-29T06:14:03Z
integration_commit: 881f200
integration_notes: "cycle-021 finalize (staging row #6). 2 rough-in L2 dep-map rows appended to L2/index.md after the now-firm ksp_solve row :53 — gram (all-pairs inner_product fold → Matrix[k,k]) + deflate (oblique projector I−X(XᴴX)⁻¹Xᴴ over gram+lu_solve+linear_combination+dot, with the do-NOT-merge orthogonalize=deflate|_gram=I over-unification guard). BOTH plain-text/inline-code forward-refs (gram.md/deflate.md absent on disk; no live link → no linkcheck2 break); NO stub created (clearly-implied bar NOT met — single-algorithm concentration, all 5 sites in nleps.cpp). Proposal-only; mutates no chapter files. Load-bearing firm-promotion BLOCKER = a NEW lu_solve L1 dense-solve primitive (HIGH fan-out; OQ deflate-needs-small-dense-lu-solve-primitive). L1/L2 boundary CLEAN against sibling harvester-nleps-l1 (this owns the L2 combinator; sibling owns the L1 pencil-apply). retroactive-budget 0; clean build."
---

# CYCLE: Combinator candidate — deflate / gram (deflation-subspace oblique projection)

## Summary

Palace's SLEPc-NEP quasi-Newton solver (`palace/linalg/nleps.cpp`) repeatedly projects a
vector onto / extracts coordinates against a **deflation subspace** spanned by the already-
converged invariant-pair basis `X = [X[0], …, X[k-1]]`. The recurrent shape is: form the
**deflation coordinates** `c[j] = ⟨X[j], v⟩` (`= X[j]ᴴ v`, arg-1-conjugated per the L1/L2
`dot` convention; Palace writes it `linalg::Dot(comm, v, X[j])` = `X[j]ᴴ v` under its
arg-2-conjugating free-function order), build the **Gram matrix** `SS[i,j] = ⟨X[j], X[i]⟩`
(`= X[j]ᴴ X[i]`), and reconstruct the projected component via a small-dense **LU solve**
against that Gram matrix followed by a `linear_combination` back into the big space
(`X · (S⁻¹ c)` via `MatVecMult`). This is an **oblique / Galerkin projection** against a
**non-orthonormal** basis — the Gram inversion is exactly what distinguishes it from
Gram-Schmidt, where the basis is orthonormal and the projection is the trivial `Vᴴ` map with
no inverse.

I propose **two related combinators**, `gram` (build `Xᴴ X`) and `deflate` (project against
the deflation subspace via a Gram-LU solve), at **L2** — both are *compositions* over the
firm L1 `dot` / firm L2 `inner_product` fold plus a new small-dense `lu_solve` primitive and
the firm L2 `linear_combination` fold (`MatVecMult` = `X · y` is exactly a length-`k`
`linear_combination`). The pattern recurs ≥3× within `nleps.cpp` and is forecast to fan out
to future eigensolver / preconditioner deflation variants. The over-unification guard against
`orthogonalize` (the L2 Gram-Schmidt named-composition) holds firmly: **deflation builds and
LU-solves an explicit Gram matrix (oblique projection, non-orthonormal basis); Gram-Schmidt
does sequential rank-1 subtraction with no Gram-matrix solve (orthogonal projection,
orthonormal basis).** Do NOT collapse them.

## Pattern instances

All within `palace/linalg/nleps.cpp` (the deflated quasi-Newton, deflation scheme = SLEPc-NEP
with minimality index 1; `:354-362` cite the Effenberger 2013 / Jarlebring 2018 references).
Five concrete deflation-projection sites split across the two combinator candidates:

**`gram` (build `SS = Xᴴ X`) — 1 build site, but its product feeds 3 distinct projections:**
- Instance G1: `nleps.cpp:526-531` — the double-loop `SS(i,j) = linalg::Dot(GetComm(), X[i], X[j])`
  (`= X[j]ᴴ X[i]`), the full `k×k` deflation Gram matrix. (The only literal Gram-build site,
  but it is the load-bearing constructor the projection depends on.)

**`deflate` (project v out of / extract coords against `span(X)` via Gram-LU) — 3 sites:**
- Instance D1: `nleps.cpp:520-535` — `deflated_solve`'s deflation correction: coords
  `x2(j) = b2(j) − ⟨X[j], x1⟩` (`:522`), then the Gram build (`:526-531`), Schur-modify
  `SS = −S.fullPivLu().solve(SS)` (`:533`), coord solve `x2 = SS.fullPivLu().solve(x2)`
  (`:534`), and the back-projection `x1 ← x1 − X·(S⁻¹ x2)` via `MatVecMult` + `AXPY`
  (`:535-536`). The complete deflation projection in one block.
- Instance D2: `nleps.cpp:561-569` — `compute_residual`'s residual deflation coords
  `rr2(j) = ⟨X[j], vv⟩` (`:568`) plus the back-projection `XSvv2 = MatVecMult(X, S⁻¹ vv2)`
  added into the residual (`:563-565`). Same `X[j]ᴴ·` coordinate extraction + `X·(S⁻¹·)`
  reconstruction, here on the residual rather than the solve.
- Instance D3: `nleps.cpp:664,:666,:667` — the Jacobian apply's deflation terms
  `XSv2 = MatVecMult(X, S⁻¹ v2)` and `XSSv2 = MatVecMult(X, S⁻¹ (S⁻¹ v2))` (the
  `T'(l)XS v2 − T(l)XS² v2` deflation contribution to the directional derivative `w`). The
  back-projection half of the same combinator (no fresh coordinate `dot` here — the coords
  `v2` are carried state — but the `X · (S-applied coords)` reconstruction is the identical
  motif).

**Supporting (the back-projection primitive shared by D1/D2/D3):** `MatVecMult(X, y)` at
`nleps.cpp:329-347` is a length-`k` `linear_combination` `Σ_j y[j]·X[j]` over the basis
(its body is two `AXPBYPCZ` calls realizing the complex-arithmetic split). Called at
`:535, :563, :666, :667, :788` (`get_call_sites MatVecMult` = 5 sites). This is the
`X·coords` half; `dot(X[j], ·)` is the `Xᴴ·coords` half.

(The `:675` complex Newton-ratio `Dot` sites flagged observable by the cycle-020 census are
**not** deflation-projection instances — they are the eigenvalue-correction scalar ratio
`−(w0ᴴu + u2_w0)/(w0ᴴw)`. Correctly excluded from this candidate; they belong to the NLEPS
Newton-step lowering, dispatch #7.)

## Proposed combinator

Two related combinators. The instance-counting modes (below) argue for proposing **both** as
a small coupled pair — `gram` is the constructor `deflate` consumes — rather than one
monolithic operator, because `gram` is independently reusable (any Galerkin/Rayleigh-Ritz
projection builds a Gram/mass matrix) while `deflate` is the specific oblique-projection
assembly.

### Combinator A — `gram`

- **Slug**: `gram`
- **Layer**: **L2**. Rationale: `gram` is a *composition* — it is the length-axis
  `inner_product` fold (firm L2, `book/src/L2/inner_product.md`) applied over the
  **cartesian product of two basis index sets**, materializing a `k×k` matrix of scalars. It
  is not a new floor primitive (it adds no reduction kernel below `dot`); it is the
  "all-pairs `inner_product`" matrix builder. That is squarely the L2 fusion-rotation role
  (Palace fuses it into a double `for`-loop of `linalg::Dot`; L2 unfolds it into the named
  all-pairs-fold composition). Not L1: it has no atomic L0 kernel of its own (the kernel is
  `dot`'s); not L3: it is value-producing and stateless, not iteration-structural.
- **Signature sketch** (harvester to firm up):
  ```text
  gram :: (dot: (Tensor[N], Tensor[N]) -> Scalar, X: Basis[N, k]) -> Matrix[k, k]
  -- gram dot X = Matrix (\i j -> dot X[j] X[i])   -- entry (i,j) = ⟨X[j], X[i]⟩ = X[j]ᴴ X[i]
  -- the dot hook defaults to the canonical Hermitian dot; the B-weighted hook gives Xᴴ B X
  ```
- **Algebraic intuition**: the result is **Hermitian** (`gram dot X = (gram dot X)ᴴ`) when
  `dot` is the Hermitian inner product — so its diagonal is real (this is the cycle-020
  census's "diagonal-only consumption would be invisible; the off-diagonal entries are the
  convention-sensitive ones" caveat). It is **positive semi-definite**, and positive definite
  iff `X` has full column rank. Identity element: `gram dot [] = Matrix[0,0]` (empty basis).
  Block law: `gram dot (X ++ Y)` is the 2×2 block matrix `[[Gxx, Gxy], [Gyx, Gyy]]` — the
  incremental-Gram update law (appending one column to `X` extends `SS` by one bordered
  row/column), which is exactly how `nleps.cpp:616` grows `H`/the deflation state as
  eigenpairs converge.
- **Variant axes**:
  - `dot` hook ∈ {`canonical Hermitian ⟨·,·⟩`, `B-weighted`} — identical hook axis to the L2
    `orthogonalize` (its row carries the same `dot`-hook axis). NLEPS uses the canonical
    Hermitian hook (`linalg::Dot`).
  - element-type ∈ {`real`, `complex`} — absorbed by the `dot` hook (conjugation lives in
    `dot`), exactly as for `inner_product`. NLEPS is complex (`Eigen::MatrixXcd`).
  - symmetry-exploitation (transparent perf trick, **not** a structural variant): Palace's
    `:526-531` double-loop computes **all** `k²` entries without exploiting Hermitian symmetry
    (it does not compute only the lower triangle and conjugate-reflect). The L2 form is the
    full all-pairs fold; "compute upper triangle + conjugate-mirror" is a one-line transparent
    note for the lowering, not an axis.

### Combinator B — `deflate`

- **Slug**: `deflate`
- **Layer**: **L2** (composition over `gram` + `lu_solve` + `linear_combination` + `dot`).
  Rationale below; the level decision is the crux of this proposal.
- **Signature sketch** (harvester to firm up; the `nleps` form is the Effenberger oblique
  Galerkin projection with an explicit Schur/`S = λI − H` modification, so the cleanest
  decomposition exposes the inner Gram-solve as the reusable core and the `S`-modification as
  the NLEPS specialization):
  ```text
  -- the reusable oblique-projection core (project v onto span(X) along span(X)):
  project_oblique :: (dot, X: Basis[N, k], v: Tensor[N]) -> Tensor[N]
  -- project_oblique dot X v = X · ( gram dot X  `lu_solve`  coords dot X v )
  --   where coords dot X v = [ dot X[j] v | j <- 0..k-1 ]   -- = Xᴴ v
  --   residual form: deflate dot X v = v − project_oblique dot X v   -- = (I − X (XᴴX)⁻¹ Xᴴ) v

  -- the NLEPS-specialized form actually in the source (Schur-modified Gram):
  deflated_correct :: (dot, X, S: Matrix[k,k], v1: Tensor[N], v2: Vec[k]) -> (Tensor[N], Vec[k])
  -- coords:   x2 = v2 − coords dot X v1          (:522)
  --           SS = − S `lu_solve` (gram dot X)   (:533)   -- Schur complement = −XᴴX S⁻¹
  --           x2 = SS `lu_solve` x2              (:534)
  -- back-proj: x1 = v1 − X · (S `lu_solve` x2)   (:535-536)
  ```
- **Algebraic intuition**:
  - `project_oblique` is **idempotent** (`P² = P` where `P = X (XᴴX)⁻¹ Xᴴ`) — it is a genuine
    projector. `deflate = I − P` is the complementary projector (`(I−P)² = I−P`).
  - When `X` is **orthonormal** (`gram dot X = I`), the Gram-solve degenerates to identity and
    `deflate` collapses to `orthogonalize`'s `(I − X Xᴴ) v` (CGS form). **This is the precise
    boundary statement**: `orthogonalize` is `deflate` specialized to `gram = I`. They are NOT
    the same combinator — `deflate` is the general-basis parent, `orthogonalize` the
    orthonormal-basis specialization with a different *algorithm* (sequential subtraction, no
    Gram-solve) and a different *precondition* (orthonormal vs full-rank). See the
    over-unification guard.
  - Range/kernel laws: `range(P) = span(X)`, `ker(deflate) = span(X)`,
    `deflate dot X v = v` iff `v ⊥ span(X)` (under `dot`).
  - Identity element: `deflate dot [] v = v` (empty basis — the `k == 0` early-return at
    `nleps.cpp:515-518`).
- **Variant axes**:
  - **plain oblique projection** vs **Schur-modified (NLEPS)**: the bare `project_oblique`
    (Gram-LU-solve) vs the `nleps` form with the `S = λI − H` linearization modification
    (`SS = −S⁻¹ (XᴴX)`, an extra LU solve at `:533` reflecting the *nonlinear*-eigenvalue
    extended-operator block structure). The Schur modification is NLEPS-specific; the harvester
    should decide whether to factor it out (so `deflate` = the reusable core and the
    `S`-modification is an NLEPS-lowering note) or keep it as a variant axis. I lean toward
    factoring: the reusable `project_oblique` is the higher-fan-out artifact.
  - `dot` hook ∈ {canonical, B-weighted} — inherited from `gram`.
  - in-place vs out-of-place: `nleps`'s `deflated_solve` mutates `x1` in place
    (`AXPY(-1.0, XSx2, x1)`, `:536`); the pure L2 form is out-of-place. This is the standard
    BLAS in-place/output-aliasing axis (a lowering fusion concern, not a structural variant),
    matching the convention noted for `linear_combination`.
  - element-type ∈ {real, complex} — absorbed by `dot`/`linear_combination`.

### Conjugation convention (pinned at the combinator boundary)

The deflation coordinates use `X[j]ᴴ v` (**arg-1-conjugated**, the linear/operator argument
is the basis vector `X[j]`), matching the L1/L2 `inner_product`/`dot` pinned convention
`⟨x, y⟩ = xᴴ y` (`book/src/L1/dot.md:43`; `book/src/L2/inner_product.md` row,
`book/src/L2/index.md:50`). Palace's source writes `linalg::Dot(GetComm(), v, X[j])`, and the
free-function `linalg::Dot(comm, a, b) = bᴴ a` (arg-2-conjugated, wave-1 verified) — so
`linalg::Dot(comm, v, X[j]) = X[j]ᴴ v`, i.e. the **deflation coordinate is the inner product
with the basis vector conjugated**. At the combinator boundary this is pinned **once**:
`coords dot X v = [ dot X[j] v ]` with the canonical `dot` (`X[j]` first/conjugated). The
Gram entry is `gram[i,j] = dot X[j] X[i] = X[j]ᴴ X[i]` (`nleps.cpp:529`), consistent. This is
the cycle-020 census's load-bearing-conjugation finding (`:522, :529, :568` all observable):
pinning it once at `deflate`/`gram` rather than re-deriving the `yᴴx`-vs-`xᴴy` reconciliation
per site is exactly the simplification this combinator buys the NLEPS lowering.

## Over-unification guard: `deflate` vs `orthogonalize`

**They are RELATED but DISTINCT. Do NOT collapse.** Both project a vector against a subspace
`span(X)`, but along three load-bearing axes:

| Axis | `orthogonalize` (L2, firm) | `deflate` (this candidate) |
|---|---|---|
| **Basis precondition** | `X` **orthonormal** (`⟨X[i],X[j]⟩ = δ_ij`); caller's contract, `orthog.hpp:22-23`, `book/src/L2/orthogonalize.md:74-76`. | `X` merely **full-rank** (the converged invariant-pair basis; not orthonormalized — `nleps.cpp:616` stores raw normalized eigenvectors, no inter-column orthogonalization). |
| **Algorithm** | Sequential / batched **rank-1 subtraction** `w ← w − ⟨w,X[j]⟩X[j]` (`orthog.hpp:38-89`, the `w.Add(-H[j], V[j])` loop). **No Gram matrix, no solve.** | Build explicit **Gram matrix** `XᴴX` (`:526-531`) and **LU-solve** it (`fullPivLu().solve`, `:533-534`). The solve is the algorithm. |
| **Projection geometry** | **Orthogonal** projection `I − X Xᴴ` (Gram is `I`, so `(XᴴX)⁻¹` drops out). | **Oblique / Galerkin** projection `I − X(XᴴX)⁻¹Xᴴ` (general non-orthonormal basis — the `(XᴴX)⁻¹` is present and load-bearing). |
| **Specialization relation** | — | `orthogonalize` = `deflate` at `gram = I`. `deflate` is the **parent**; `orthogonalize` is the orthonormal specialization implemented by a *different (Gram-solve-free) algorithm*. |

The decisive distinguisher is the **Gram-matrix LU solve**. If a future pass tries to unify
them, the unification must NOT erase that `(XᴴX)⁻¹` — doing so would silently assume the
deflation basis is orthonormal (it is not), changing the algorithm and the result. They share
a *constituent* (both build coordinates via `dot`; both reconstruct via a `linear_combination`
`X·coords`), and `gram` is the shared Gram-matrix builder, but the **project** step differs
fundamentally (sequential subtraction vs Gram-solve). Precedent for keeping algorithm-distinct
same-target operators separate: the `inner_product` / `linear_combination` do-NOT-merge
boundary (`book/src/L2/index.md:69`) and the `orthogonalize` entry's own "Householder is
scoped out" boundary (different state-threading → different combinator). The `same-layer-
cross-cutter` may later record the `orthogonalize = deflate|_{gram=I}` specialization edge as
a cross-reference, but the two entries stay distinct.

## Instance-counting: both modes

**Same-shape mode (default):** the `Xᴴ·` coordinate-extraction + `X·(solve(coords))`
reconstruction shape recurs **≥3×** in `nleps.cpp` (D1 `:520-535`, D2 `:561-569`, D3
`:664,:666,:667`), with the Gram build (G1 `:526-531`) feeding the solve. Clears the ≥3 soft bar
**within a single file** — but only one algorithm, so this alone is a within-NLEPS pattern
(fan-out argument below carries the cross-algorithm case).

**Parametric / variadic-family mode:** I checked. `deflate`/`gram` are **not** an
arity/element-type/conjugation/weight *family* in the BLAS-1 sense (there is no cohort of
fixed-arity siblings folding to a variadic parent — `MatVecMult`/`X·coords` IS already a
variadic `linear_combination` over the `k`-column basis, and that fold is the firm L2
`linear_combination`, not a new family). The relevant parametric axis here is the **basis-
cardinality `k`** (the deflation subspace grows by one column per converged eigenpair,
`nleps.cpp:613-619`), which makes `gram`/`deflate` *naturally variadic over `k`* — a single
combinator parameterized by basis size, not a family of fixed-`k` specializations. So family-
mode **confirms** the single-combinator (variadic-in-`k`) framing rather than splitting it:
`gram :: Basis[N,k] -> Matrix[k,k]` and `deflate :: (Basis[N,k], Tensor[N]) -> Tensor[N]` are
already the variadic-in-`k` parents; there are no fixed-`k` siblings to unify. The
incremental-Gram block law (`gram (X ++ [x])` borders `gram X`) is the fold/parametric law
that certifies the variadic-in-`k` form is a genuine fold over basis columns, not a
coincidental cluster.

## Level decision (the requested judgment): **L2**, not L1

`deflate` and `gram` are **L2 compositions**, not L1 primitives. Argument:

1. **No atomic L0 kernel.** L1 leaves are floor primitives with a single L0 reduction/BLAS
   kernel (`dot`, `axpy`, `nrm2`). `gram` decomposes into `k²` `dot`s; `deflate` decomposes
   into `k` `dot`s + a Gram build + an LU solve + a `k`-term `linear_combination`. They are
   *built from* L1/L2 vocabulary — the L2 fusion-rotation signature ("batched specialized
   calls written as compositions of base primitives", `book/src/L2/index.md:11`). Palace
   literally fuses the Gram into a double `for`-loop of `linalg::Dot` (`:526-531`); unfolding
   that fusion into the all-pairs-fold composition is the L2 rotation.
2. **Structural sibling of the firm L2 cohort.** `gram`/`deflate` sit alongside
   `inner_product` (all-pairs `gram` is the matrix-valued lift of the scalar `inner_product`
   fold), `linear_combination` (the `X·coords` reconstruction *is* a `linear_combination`),
   and `orthogonalize` (the named-composition sibling `deflate` specializes from). Placing
   them at L2 lets them reuse all three firm L2 entries as dependencies.
3. **One genuinely-new sub-primitive is needed: a small-dense `lu_solve`.** The `fullPivLu().
   solve` (`:533, :534, :535` and the `S⁻¹` solves at `:563, :665, :667`) is a **dense
   factor-and-solve on the `k×k` redundant-on-all-ranks coordinate matrices** — distinct from
   the firm `ksp_solve` (which is the *iterative* big-space solve). This is a candidate **L1**
   leaf (`lu_solve :: (Matrix[k,k], Vec[k]) -> Vec[k]`, a dense LAPACK/`trsv`-family
   primitive — note `concepts/trsv.md` already exists as the triangular-solve concept). I do
   **not** propose `lu_solve` here (one pattern per invocation), but flag it as the dependency
   `deflate` will need; it is the only piece not already firm. (Open question below.)
4. **Not L3.** `gram`/`deflate` are value-producing and stateless (like `orthogonalize`, per
   `book/src/L2/orthogonalize.md:42-44`); the *outer* deflation loop that grows `X` across
   converged eigenpairs is the iteration-structural part and lives in the NLEPS driver
   (dispatch #7 / L4 `iterate_while`), not here.

## Proposed changes

Two **rough-in** dep-map rows appended to the L2 dep-map. Per the forward-reference
convention, the future-chapter names are **inline-code spans / plain text, NOT live links**
(`book/src/L2/deflate.md` and `book/src/L2/gram.md` do not yet exist; the harvester authors
them). This report does **not** create those chapter files.

```edit:book/src/L2/index.md
[append two rows to the "## Operator dep-map" table, after the `ksp_solve` stub row (`:53`)]
| `gram` *(rough-in; no anchor yet)* | `(dot: (Tensor[N], Tensor[N]) -> Scalar, X: Basis[N, k]) -> Matrix[k, k]` (≡ all-pairs `inner_product`: entry `(i,j) = ⟨X[j], X[i]⟩ = X[j]ᴴ X[i]`, arg-1-conjugated) | **All-pairs `inner_product` fold → `Matrix[k,k]`.** Constituent: L2 `inner_product` (firm; the scalar fold this lifts to a matrix). L1: `dot` (the entry kernel; `dot` hook ∈ {canonical, B-weighted} inherited from `inner_product`/`orthogonalize`). Hermitian + PSD (PD iff `X` full-rank); diagonal real (off-diagonal is the conjugation-sensitive part — cycle-020 census). Incremental-Gram block law: `gram (X ++ [x])` borders `gram X`. Consumer: `deflate` (below). | `rough-in` (proposed-by combinator-miner:2026-05-29T051532Z; pattern `nleps.cpp:526-531`; OQ nleps-deflation-subspace-projection-combinator-deflate-gram) |
| `deflate` *(rough-in; no anchor yet)* | `(dot, X: Basis[N, k], v: Tensor[N]) -> Tensor[N]` (≡ `v − X·((XᴴX)⁻¹·(Xᴴ v))`, the oblique/Galerkin complementary projector `I − X(XᴴX)⁻¹Xᴴ`) | **Named composition — oblique-projection assembly.** Constituents: `gram` (above; builds `XᴴX`), `lu_solve` (the small-dense `k×k` Gram solve — NOT yet vocabulary; candidate L1 leaf, OQ below), L2 `linear_combination` (the `X·coords` reconstruction = length-`k` lin-comb over the basis), L1 `dot` (coordinate extraction `Xᴴv`). Idempotent complementary projector; identity at `k=0`. **Over-unification guard (do NOT merge with `orthogonalize`):** `orthogonalize` = `deflate` at `gram = I` (orthonormal basis, sequential subtraction, no Gram-solve); `deflate` is the general non-orthonormal-basis parent with a Gram-matrix LU solve (oblique vs orthogonal projection). Variant axes: plain vs Schur-modified-NLEPS (`S = λI − H`), `dot` hook, in-place/out-of-place. | `rough-in` (proposed-by combinator-miner:2026-05-29T051532Z; pattern `nleps.cpp:520-535`, `:561-569`, `:663-668`; feeds NLEPS lowering dispatch #7; OQ nleps-deflation-subspace-projection-combinator-deflate-gram) |
```

The harvester (later pass) creates `book/src/L2/gram.md` and `book/src/L2/deflate.md`,
firms the signatures/laws, decides the `project_oblique`-vs-Schur-modified factoring, and at
*that* point switches these dep-map cells to live links. Until then they stay plain-text.

A companion plan candidate (for `cycle-planner`/`meta-phase` to migrate, not enacted here):
the small-dense `lu_solve` L1 leaf — see Open questions.

## Supporting evidence

All ranges `read_range`-verified this invocation (paths relative to `reference/`):

- `palace/linalg/nleps.cpp:504-537` — `deflated_solve` lambda: block-system comment
  (`:509-514` `x1 = x1 − X S x2`, `SS = (B − A T⁻¹U) = −X*X S⁻¹`); `k==0` early-return
  (`:515-518`); coordinate extraction `x2(j) = b2(j) − linalg::Dot(GetComm(), x1, X[j])`
  (`:520-523`); Gram build `SS(i,j) = linalg::Dot(GetComm(), X[i], X[j])` (`:526-531`);
  Schur-modify `SS = −S.fullPivLu().solve(SS)` (`:533`); coord solve
  `x2 = SS.fullPivLu().solve(x2)` (`:534`); back-projection
  `XSx2 = MatVecMult(X, S.fullPivLu().solve(x2)); linalg::AXPY(-1.0, XSx2, x1)` (`:535-536`).
- `palace/linalg/nleps.cpp:547-578` — `compute_residual` lambda: deflated-residual comment
  (`:547-549` `rr2 = X* vv`); back-projection `XSvv2 = MatVecMult(X, S.fullPivLu().solve(vv2))`
  added into `rr` (`:563-565`); residual coords `rr2(j) = linalg::Dot(GetComm(), vv, X[j])`
  (`:566-569`).
- `palace/linalg/nleps.cpp:660-668` — Jacobian deflation terms: `S = eig·I − H` (`:664`),
  `XSv2 = MatVecMult(X, S.solve(v2))` (`:666`), `XSSv2 = MatVecMult(X, S.solve(Sv2))` (`:667`).
- `palace/linalg/nleps.cpp:329-347` — `MatVecMult(X, y)`: the `X·y` reconstruction
  (`z = 0; for j: AXPBYPCZ(...) into z` — a length-`k` `linear_combination` over the basis,
  with the complex real/imag split). `get_call_sites MatVecMult` → `:535, :563, :666, :667,
  :788` (5 sites).
- `palace/linalg/nleps.cpp:606-619` — deflation-basis growth: `X.resize(k+1); X[k] = v;
  H.conservativeResizeLike(...); H.col(k).head(k) = v2/scale; H(k,k) = eig; k++` — confirms
  `X` is the raw normalized-eigenvector invariant-pair basis (NOT orthonormalized → Gram
  inversion required → oblique projection; the over-unification guard's basis-precondition row).
- `palace/linalg/nleps.cpp:354-362` — the deflation-scheme references (Effenberger 2013
  successive eigenpair computation; Jarlebring 2018 quasi-Newton; SLEPc-NEP minimality index 1)
  — the literature anchor for the oblique-Galerkin deflation form.
- `palace/linalg/orthog.hpp:19-89` — the over-unification target: `OrthogonalizeColumnMGS`
  (`:41-54`, `H[j] = dot_op(w,V[j]); GlobalSum; w.Add(-H[j],V[j])` per-`j` — sequential rank-1
  subtraction, **no Gram matrix, no solve**) and `OrthogonalizeColumnCGS` (`:57-89`); header
  `:19-23` "orthogonalizing a vector against a number of basis vectors using modified or
  classical Gram-Schmidt … Assumes that the input vectors are normalized". The
  no-Gram-solve / orthonormal-basis distinction from `deflate`.
- `book/src/L2/inner_product.md` + `book/src/L2/index.md:50` — the firm L2 `inner_product`
  scalar fold `gram` lifts to a matrix; the pinned arg-1-conjugated convention.
- `book/src/L2/linear_combination.md` + `book/src/L2/index.md:49` — the firm L2
  `linear_combination` the `X·coords` reconstruction (`MatVecMult`) instantiates.
- `book/src/L2/orthogonalize.md:42-44,74-76,326-341` — the L2 named-composition sibling: its
  stateless/value-producing L2-placement argument (reused here), its orthonormal-basis
  precondition, and its firm status (the bar `deflate` aims at).
- `book/src/L1/dot.md:43` — the pinned `⟨x,y⟩ = xᴴ y` arg-1-conjugated convention.
- `reports/2026-05-29T034441Z-cross-layer-cross-cutter-dot-callers/CYCLE.md` (integrated,
  commit `14cc0bd`) — the dot-callers census that flagged `:522,:529,:568` observable and
  proposed this combinator (its "Follow-up candidates → combinator-miner" bullet, `:198-202`).

## Open questions / caveats

- **OQ (new, dependency — for cycle-planner/meta-phase migration):**
  `deflate-needs-small-dense-lu-solve-primitive`. `deflate` depends on a small-dense `k×k`
  factor-and-solve (`Eigen::fullPivLu().solve`, `nleps.cpp:533,534,535,563,665,667`) that is
  **not yet vocabulary**. It is distinct from the iterative big-space `ksp_solve` and from the
  triangular `concepts/trsv.md`: it is a dense LU on the redundant-on-all-ranks coordinate
  matrices. Candidate **L1** leaf `lu_solve :: (Matrix[k,k], Vec[k]) -> Vec[k]` (or
  `dense_solve`). A future harvester/combinator-miner pass should localize all `fullPivLu`/
  `solve` sites across `palace/linalg/` (`densematrix.cpp` is a likely sibling source) and
  decide its layer. Blocks `deflate`'s promotion to firm but not the rough-in.

- **OQ (new, factoring decision — for harvester):**
  `deflate-project-oblique-core-vs-nleps-schur-modification`. Should the firm `deflate` be the
  reusable bare oblique projector `I − X(XᴴX)⁻¹Xᴴ` (with NLEPS's `S = λI − H` Schur
  modification as a lowering-specific note in the NLEPS L1>L0 theme), or should the `S`-modified
  form be a variant axis of `deflate`? I lean toward the bare core as the higher-fan-out
  artifact (eigensolver/preconditioner deflation generally uses plain oblique projection; the
  `S`-modification is the nonlinear-eigenvalue extended-operator specialization). Harvester
  decides at formalization.

- **Caveat (instances concentrate in one algorithm):** all five deflation-projection sites are
  in `nleps.cpp` (one solver). The same-shape bar (≥3) is met **within** that file, and the
  parametric-in-`k` framing + literature anchor (Effenberger oblique Galerkin deflation is a
  standard scheme) carry the "stateable combinator" case. But the *cross-algorithm* fan-out is
  currently **forecast, not observed**: I did NOT find a second Palace algorithm that builds-
  and-LU-solves a deflation Gram matrix (the linear SLEPc/ARPACK eigensolvers, `divfree.cpp`,
  and the ROM path use Gram-Schmidt `orthog.hpp`, not Gram-LU oblique projection — search of
  `fullPivLu|Gram|deflat` across `palace/linalg/*.cpp` returned hits only in `nleps.cpp`). The
  combinator's value is therefore (a) pinning the load-bearing conjugation once for the NLEPS
  lowering (dispatch #7), and (b) the *anticipated* reuse if/when other deflation/Galerkin-
  projection variants are dissected. If a future scan finds no second Gram-LU site, the
  harvester may keep `deflate` NLEPS-scoped rather than fully general — flag for the level/
  scope review.

- **Caveat (`gram` vs `deflate` as two rows):** I propose two coupled rough-in rows rather
  than one. If `same-layer-cross-cutter` later judges `gram` too thin to stand alone (it is a
  one-line all-pairs lift of `inner_product`), it could be folded as an internal stage of
  `deflate` (the way `orthogonalize`'s `project`/`subtract` stages are not separate entries).
  I keep them separate because `gram` is independently reusable (any Rayleigh-Ritz / Galerkin
  / mass-matrix projection builds a Gram matrix) and the Hermitian-PSD laws are cleanly `gram`'s
  own. The unification call is `same-layer-cross-cutter`'s, not mine.

- **Direction-of-definition: clean.** This is a read-only L0-evidence scan producing an L2
  combinator proposal (high→low respected: `deflate`/`gram` defined in L2 vocabulary —
  `inner_product`, `linear_combination`, a candidate `lu_solve` — not in L0 terms). No `book/`
  mutation; the proposed-changes block is two rough-in dep-map rows for the integrator, per
  the dispatch-phase write-guard.
