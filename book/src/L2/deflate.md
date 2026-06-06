# deflate

The L2 named-composition **oblique / Galerkin complementary projector** that removes the
deflation subspace `span(X)` (the already-converged invariant-pair basis) from a vector:
`deflate(X, v) = v − X·(coords-solve)`. It names the recurrent Palace NLEPS shape **extract
deflation coordinates `Xᴴ v` ▷ solve them against the (Schur-modified) Gram block ▷
back-project `X·(·)` and subtract**. The form Palace positively exhibits is the
**Schur-complement-modified** oblique projection of the SLEPc-NEP deflation scheme
(`palace/linalg/nleps.cpp:505-537`); the bare textbook Galerkin projector
`I − X(XᴴX)⁻¹Xᴴ` is its `S = I` degenerate case (literature-anchored, not positively sourced —
see § Status). It is built over the [`gram`](./gram.md) Gram-matrix constructor,
the [`lu_solve`](../L1/lu_solve.md) small-dense `k×k` solve, the
[`linear_combination`](./linear_combination.md) back-projection fold, and the
[`dot`](../L1/dot.md) coordinate-extraction kernel. It is **distinct** from
[`orthogonalize`](./orthogonalize.md) — see § Over-unification guard.

## Context

L2 is the fusion-rotation layer (`book/src/L2/index.md`): "Batched specialized BLAS calls are
written as compositions of base primitives… kernel fusion across multiple algebraic operations
is unfolded into composition." Palace's deflation projection is exactly such a batched
specialization — it is fused into a hand-written block of a double `for`-loop of `linalg::Dot`
(the Gram build, `palace/linalg/nleps.cpp:526-531`), three `Eigen::fullPivLu().solve` calls
(`palace/linalg/nleps.cpp:533-535`), a `MatVecMult` (`palace/linalg/nleps.cpp:535`), and an
`AXPY` (`palace/linalg/nleps.cpp:536`). L2 de-fuses that hand-written block into the canonical
`coords ▷ schur-solve ▷ back-project` composition, naming the constituents and stating the
projector laws at the composition level.

`deflate` is a **named composition**, the structural sibling of the firm
[`orthogonalize`](./orthogonalize.md) (the Gram-Schmidt `project ▷ subtract` composition) — but
the two are emphatically **not** the same combinator (§ Over-unification guard). Its
constituents are the firm L2 [`linear_combination`](./linear_combination.md) (the `X·coords`
back-projection is a length-`k` linear combination over the basis columns — the
`MatVecMult(X, ·)` at `palace/linalg/nleps.cpp:329-347`), the firm L1
[`lu_solve`](../L1/lu_solve.md) (the small-dense `k×k` factor-and-solve against the Gram /
Schur block, distinct from the iterative big-space [`ksp_solve`](../L1/ksp_solve.md)), the firm
L1 [`dot`](../L1/dot.md) (the coordinate extraction `Xᴴ v`), and the [`gram`](./gram.md)
constructor (`XᴴX`).

The composition is **value-producing and stateless** (like `orthogonalize`), not
iteration-structural: it folds a fixed-size deflation basis prefix into one projected vector,
with no convergence predicate and no monadic state threading. It therefore belongs with the
tensor algebra at L2, not with L4's `iterate_while`. (The *outer* deflation loop that grows `X`
by one column per converged eigenpair — `palace/linalg/nleps.cpp:606-619` — is the
iteration-structural part and lives in the NLEPS driver, not here.)

The closely-related L1 [`nleps_deflated_residual`](../L1/nleps_deflated_residual.md) shares
`deflate`'s `Xᴴ·` / `X·` constituents but computes a *residual* of an extended NEP operator (a
different thing): its over-unification guard (`book/src/L1/nleps_deflated_residual.md:109`)
records the same distinction from the *other* direction. Where this entry and that one name the
same source constituents, the cited line is authoritative.

## Signature

```text
deflate :: (op: DeflateOp, X: Basis[N, k], v: Tensor[(S: ...)]) -> Tensor[$S]

type DeflateOp = { dot: (Tensor[(S: ...)], Tensor[$S]) -> Scalar     -- inner-product hook
                 , block: GramBlock[k]                        -- the coordinate-solve block (below)
                 }

type GramBlock[k] = Schur { S: Matrix[k, k] }    -- NLEPS form (positively sourced):  coords solved against  −S⁻¹(XᴴX)  then  S⁻¹
                  | Galerkin                       -- bare Galerkin core (S = I, literature-anchored): coords solved against  XᴴX

deflate op X v = v − linear_combination (zip (coords-solve op X v) X)   -- = v − X·(coordinate solve)
```

Shape contract (bunsen-style; named axes; the vector shape group `S` follows the named-shape-group convention of [`l4_calculus`](../design/l4_calculus.md) §1.2.1; the deflation basis `Basis[N, k]` is a genuine 2-D `k`-column basis and the coordinate-solve `Matrix[k, k]` is genuinely 2-D — both KEEP their concrete axes):

- `op` — `DeflateOp` — the closed-over projection surface, bound once at solve setup. A record:
  - `op.dot : (Tensor[(S: ...)], Tensor[$S]) -> Scalar` — the inner-product hook (the canonical
    [`dot`](../L1/dot.md), conjugate-linear in the first argument, by default; a `B`-weighted
    hook for the SLEPc/ROM Galerkin variant). Identical hook axis to `orthogonalize`'s
    `op.dot` and `gram`'s `dot` (inherited).
  - `op.block : GramBlock[k]` — selects the coordinate-solve block: the NLEPS `Schur { S }`
    form actually in Palace (`S = λI − H`, the extended-operator linearization block,
    `palace/linalg/nleps.cpp:532`) or the bare `Galerkin` core (`S = I`, the
    literature-idealized Gram-only solve). This is the **central variant axis** (§ Variant
    axes); the Schur form is the positively-sourced one, the Galerkin core is its `S = I`
    degenerate case.
- `X` — `Basis[N, k]` — read-only; `k` columns each a length-`N` dof-vector (congruent to `S`), the converged
  invariant-pair / deflation basis. **Precondition: `X` full column rank** (so the Gram `XᴴX`
  is invertible). It is **NOT** assumed orthonormal — Palace stores raw normalized eigenvectors
  with no inter-column orthogonalization (`palace/linalg/nleps.cpp:606-619`,
  `book/src/L1/nleps_deflated_residual.md:60`); the non-orthonormality is exactly why the
  `(XᴴX)⁻¹` / Schur correction is load-bearing (§ Over-unification guard).
- `v` — `Tensor[(S: ...)]` — read-only; the vector to project against the deflation subspace.
- result — `Tensor[$S]` — the deflated vector `v − X·(coordinate solve)`, same shape group `S` as `v`.

The shape group `S` is uniform across `X`'s columns and `v`. The deflation-cardinality axis `k` is the
**variadic-in-`k`** axis — `k` grows by one per converged eigenpair
(`palace/linalg/nleps.cpp:614-619`), so `deflate` is parameterized by basis size, not a family
of fixed-`k` specializations. Element type is **complex** at the Palace site (`Eigen::MatrixXcd`
/ `ComplexVector`); the real case is absorbed by the `op.dot` hook (conjugation lives in `dot`).

The coordinate solve (the body of `coords-solve op X v`), with constituents pinned:

```text
coords-solve op X v =
  let c    = [ op.dot X[j] v | j <- 0..k-1 ]          -- = Xᴴ v   (deflation coordinates; k dots)
      G    = gram op.dot X                              -- = XᴴX    (the Gram matrix; entry (i,j) = X[i]ᴴ X[j])
  in case op.block of
       Galerkin    -> lu_solve G c                      -- (XᴴX)⁻¹ · (Xᴴ v)     [literature core, S = I]
       Schur { S } -> let SS = lu_solve S (scale (-1) G)  -- SS = −S⁻¹ (XᴴX)     (Schur complement; nleps.cpp:533)
                          c' = lu_solve SS c              -- SS⁻¹ · c             (nleps.cpp:534)
                      in lu_solve S c'                    -- S⁻¹ · c'             (nleps.cpp:535, inside MatVecMult arg)

deflate op X v = v − linear_combination (zip (coords-solve op X v) X)   -- v − X·(coordinate solve)
```

The empty-basis case (`k = 0`) is the identity: `deflate op [] v = v` for every `op.block`
(the `k == 0` early-return at `palace/linalg/nleps.cpp:515-518`).

## Semantics

`deflate(op, X, v)` projects `v` out of the deflation subspace `span(X)`. The pipeline has
three named stages, all read from the positive `deflated_solve` block
(`palace/linalg/nleps.cpp:505-537`):

1. **Coordinate extraction** — `c(j) = op.dot(X[j], v) = X[j]ᴴ v`, the `k` deflation
   coordinates of `v` against the basis columns. (`palace/linalg/nleps.cpp:519-523`, the
   `x2(j) = b2(j) − linalg::Dot(GetComm(), x1, X[j])` loop; the `b2 −` is the extended-block
   RHS, the `−⟨X[j],x1⟩` is the coordinate extraction.) The basis vector `X[j]` is the
   **conjugated** argument (§ Conjugation convention).
2. **Coordinate solve** — the coordinates are solved against the (Schur-modified) Gram block:
   - **Galerkin core** (`S = I`, literature): `lu_solve(XᴴX, c) = (XᴴX)⁻¹·(Xᴴ v)`.
   - **NLEPS Schur form** (positively sourced): `SS = −S⁻¹·(XᴴX)` (`palace/linalg/nleps.cpp:533`),
     then `SS⁻¹·c` (`:534`), then `S⁻¹·(·)` (`:535`) — three `lu_solve`s against `S = λI − H`
     and `SS`, the extended-block elimination the source documents at
     `palace/linalg/nleps.cpp:508-513` (the block linear system `[[T,U],[A,B]]` with Schur
     complement `SS = (B − A T⁻¹ U) = −XᴴX·S⁻¹`).
3. **Back-projection and subtraction** — `v − X·(coordinate solve)`, the length-`k`
   [`linear_combination`](./linear_combination.md) over the basis columns
   (`MatVecMult(X, ·)`, `palace/linalg/nleps.cpp:535`, `:329-347`) followed by the `AXPY(-1, …)`
   subtraction (`palace/linalg/nleps.cpp:536`).

In the **Galerkin core** the result is the standard oblique complementary projector
`(I − X(XᴴX)⁻¹Xᴴ) v` — a genuine projector onto `span(X)^⊥` *along* `span(X)`. The NLEPS Schur
form is the same shape with the Gram inverse `(XᴴX)⁻¹` replaced by the Schur-modified solve
`S⁻¹·(−S⁻¹(XᴴX))⁻¹` — the extended-operator block-elimination of the *nonlinear* eigenproblem,
where the `S = λI − H` linearization block couples the deflation coordinates. (See § Status for
why the Galerkin core is recorded as the literature degenerate case, not the firm form.)

Three semantic points are load-bearing and recorded rather than smoothed:

**(1) The Gram is solved, not transposed — the basis is non-orthonormal.** Were `X` orthonormal
(`XᴴX = I`), the coordinate solve would degenerate to the identity and `deflate` would collapse
to the orthogonal projector `I − XXᴴ` (= `orthogonalize`'s residual). It does **not**, because
`X` is the raw normalized-eigenvector basis (`palace/linalg/nleps.cpp:606-619`,
`book/src/L1/nleps_deflated_residual.md:60`). The `lu_solve` against `XᴴX` (or the Schur
`SS`) **is** the algorithm — its presence is exactly what distinguishes oblique deflation from
orthogonal Gram-Schmidt (§ Over-unification guard).

**(2) The conjugation is pinned at the combinator boundary.** The deflation coordinate is
`X[j]ᴴ v` — the **basis vector is the conjugated argument** — matching the L1/L2
arg-1-conjugated `dot` convention `⟨x, y⟩ = xᴴ y` (`book/src/L1/dot.md:43`). Palace writes
`linalg::Dot(GetComm(), x1, X[j])`; under its free-function order `linalg::Dot(comm, a, b) = bᴴ a`
the C++ arg-2 (`X[j]`) is conjugated, which is the L1 `dot`'s arg-1 once the call is re-ordered.
The Gram entry is `G(i,j) = X[i]ᴴ X[j]` (`palace/linalg/nleps.cpp:529`,
`linalg::Dot(GetComm(), X[i], X[j])`), consistent. Pinning the conjugation once here is the
simplification this combinator buys the NLEPS lowering (the cycle-020 census found
`:522, :529, :568` all load-bearing-conjugation-sensitive).

**(3) The big-space back-projection avoids a fresh temporary.** The source applies the
subtraction `x1 ← x1 − X·(…)` via `MatVecMult` into a temporary then `AXPY(-1, …, x1)`
(`palace/linalg/nleps.cpp:535-536`), in place on the destination `x1`. The L2 form is
out-of-place (`v − …`); the in-place destination is an L2>L1 transparent-performance concern,
not part of the L2 signature (the standard BLAS in-place / output-aliasing axis, matching
`linear_combination`).

## Algebraic laws

`deflate` is a **named composition** (a `coords ▷ solve ▷ back-project` pipeline parameterized
by `op.block` and `op.dot`), not a binary algebra. The laws below are stated at the composition
level — facts about the projected vector the composition produces — and the constituent L1/L2
laws (`dot` conjugate-linearity, `lu_solve` RHS-linearity, `linear_combination` linearity) are
inherited, not re-derived. "Exact" means exact arithmetic. Laws 1–4 hold for **both**
`op.block` variants (they are facts about a complementary projector along `span(X)`); laws
5–6 are the projector-specific identities that hold for the **Galerkin core** in exact
arithmetic (and are the design intent the Schur form realizes for the extended problem — see
the variant note).

1. **Empty-basis identity.** `deflate op [] v = v` for any `v` and any `op.block` (the `k = 0`
   path, `palace/linalg/nleps.cpp:515-518`). The deflation of nothing is the input.

2. **Linearity in `v`.** `deflate op X (α·v₁ + β·v₂) = α·deflate op X v₁ + β·deflate op X v₂`
   for scalars `α, β`. Holds because for fixed `op` and `X` the whole pipeline —
   coordinate extraction (`Xᴴ·`, linear in `v`), the coordinate solve (`lu_solve` against a
   fixed block, linear in its RHS — `book/src/L1/lu_solve.md:56`), the back-projection (`X·`,
   linear), and the subtraction — is a composition of linear maps. Conjugate-linearity in the
   complex case follows the inherited `op.dot` first-argument convention. In particular
   `deflate op X 0 = 0` (the `α = β = 0` case).

3. **Range-nulling on the basis (Galerkin core, exact).** `deflate op X X[i] = 0` for each
   `i ∈ [0, k)` (Galerkin `op.block`, exact). A basis column is entirely in `span(X)`, so its
   projection onto the complement is zero: `(I − X(XᴴX)⁻¹Xᴴ) X[i] = X[i] − X(XᴴX)⁻¹(XᴴX) e_i =
   X[i] − X e_i = 0`. This is the defining "project the deflation subspace out" contract — it is
   *why* the deflated solve cannot re-converge to an already-converged eigenvector. (For the
   NLEPS Schur form the corresponding statement is the extended-block annihilation; see the
   variant note.)

4. **Kernel / range characterization (Galerkin core, exact).** `ker(deflate op X) = span(X)`
   and `deflate op X v = v` iff `v ⊥ span(X)` under `op.dot` (i.e. `Xᴴ v = 0`). A vector already
   orthogonal to the deflation subspace passes through unchanged; a vector in the subspace is
   annihilated (law 3). The composition is the complementary projector `I − P` with
   `P = X(XᴴX)⁻¹Xᴴ` projecting onto `span(X)`.

5. **Idempotence (Galerkin core, exact).** `deflate op X (deflate op X v) = deflate op X v` —
   `deflate` is a genuine (idempotent) complementary projector, `(I − P)² = I − P`, because
   `P = X(XᴴX)⁻¹Xᴴ` satisfies `P² = P` (the `(XᴴX)⁻¹(XᴴX)` telescopes). Re-deflating an
   already-deflated vector is a no-op. (Holds exactly for the Galerkin core; the Schur form's
   idempotence is modulo the `S = λI − H` coupling, which is fixed per evaluation `λ`.)

6. **`op.dot`-hook invariance of shape and laws.** Substituting `op.dot` (canonical →
   `B`-weighted) leaves the composition's shape and laws 1–5 unchanged; only the inner-product
   realization differs and the orthogonality condition in law 4 reads `Xᴴ B v = 0`. The hook is
   a closure substitution, not a structural variant (inherited from `gram` / `inner_product` /
   `orthogonalize`).

Laws that explicitly **do NOT** hold:

- **Idempotence / projector structure at the bit level / for the Schur form across `λ`.** Laws
  3–5 are exact-arithmetic projector identities for the Galerkin core. In floating point they
  hold only up to roundoff (the `lu_solve` conditioning — `book/src/L1/lu_solve.md:63`). The
  NLEPS Schur form additionally carries the `S = λI − H` linearization block, which is
  re-formed per evaluation point `λ` (`palace/linalg/nleps.cpp:532, 562, 664`); it is a genuine
  complementary projector for the *extended* deflated operator at fixed `λ`, **not** the bare
  `span(X)` projector — recorded as the central variant (§ Variant axes), not as a law that
  holds uniformly.
- **Orthogonality of the projector (`deflate ≠ I − XXᴴ`).** `deflate` is **not** the orthogonal
  projector `I − XXᴴ`. That would require `XᴴX = I` (orthonormal `X`), which is false here
  (semantics point 1). The `(XᴴX)⁻¹` / Schur correction is load-bearing — erasing it silently
  assumes an orthonormal basis and changes the algorithm. This is the over-unification non-law
  (§ Over-unification guard).
- **Linearity / any structure in `X`.** `deflate(op, ·, v)` is **not** linear in the basis `X`
  (the Gram `XᴴX` and its inverse are nonlinear in `X` — inherited from `lu_solve`'s
  `A`-nonlinearity non-law, `book/src/L1/lu_solve.md:64`). Recorded so a basis-update does not
  attempt to distribute `deflate` over a column append (the incremental-Gram block law is
  `gram`'s, not a `deflate` linearity).
- **Column-order dependence (none, modulo conditioning).** Unlike MGS `orthogonalize` (whose
  result is column-order-dependent, `book/src/L2/orthogonalize.md:224`), `deflate`'s result is
  column-order-invariant in exact arithmetic — the Gram solve `(XᴴX)⁻¹` does not depend on
  column ordering (permuting `X`'s columns permutes `G`'s rows/columns symmetrically and the
  back-projection un-permutes). Bit-level reduction-tree and pivot noise are the only ordering
  sensitivity. (This is itself a *distinguisher* from MGS `orthogonalize`, recorded under the
  guard.)

## Over-unification guard: `deflate` vs `orthogonalize`

**They are RELATED but DISTINCT. Do NOT collapse them into one combinator.** Both project a
vector against a subspace `span(X)`, and there is a tempting identity
`orthogonalize = deflate` with `gram = I` (orthonormal basis). The cycle-021 combinator-miner
proposal flagged this collapse explicitly as an **over-unification to avoid**, and this entry
preserves the distinction. They differ along three load-bearing axes:

| Axis | [`orthogonalize`](./orthogonalize.md) (L2, firm) | `deflate` (this entry) |
|---|---|---|
| **Basis precondition** | `X` **orthonormal** (`⟨X[i],X[j]⟩ = δ_ij`); caller's contract (`book/src/L2/orthogonalize.md:74`). | `X` merely **full-rank** — the converged invariant-pair basis, NOT orthonormalized (`palace/linalg/nleps.cpp:606-619`, `book/src/L1/nleps_deflated_residual.md:60`). |
| **Algorithm** | Sequential / batched **rank-1 subtraction** `w ← w − ⟨w,X[j]⟩X[j]` (the `project ▷ subtract` `dot ▷ axpy` chain, `book/src/L2/orthogonalize.md:114-142`). **No Gram matrix, no solve.** | Build the explicit **Gram matrix** `XᴴX` (via [`gram`](./gram.md), `palace/linalg/nleps.cpp:526-531`) and **`lu_solve`** it (the Schur-modified solve, `palace/linalg/nleps.cpp:533-535`). **The solve is the algorithm.** |
| **Projection geometry** | **Orthogonal** projection `I − XXᴴ` (Gram is `I`, so `(XᴴX)⁻¹` drops out). | **Oblique / Galerkin** projection `I − X(XᴴX)⁻¹Xᴴ` (general non-orthonormal basis — the `(XᴴX)⁻¹` is present and load-bearing), Schur-modified in the NLEPS form. |
| **Specialization relation** | — | `orthogonalize` is `deflate` specialized to `gram = I` (orthonormal `X`) implemented by a *different, Gram-solve-free algorithm*. `deflate` is the general-basis parent. |

The decisive distinguisher is the **Gram-matrix `lu_solve`**. If a future pass tries to unify
them, the unification must **NOT** erase that `(XᴴX)⁻¹` / Schur correction — doing so would
silently assume the deflation basis is orthonormal (it is not), changing the algorithm and the
result (the §Algebraic-laws "orthogonality of the projector" non-law). They share *constituents*
(both extract coordinates via `dot`; both reconstruct via a `linear_combination`-shaped
`X·coords`), and `gram` is the shared Gram-matrix builder — but the **solve** step differs
fundamentally (sequential rank-1 subtraction vs Gram-`lu_solve`). The
[`same-layer-cross-cutter`](../../../scaffolding/priorities.md) may later record the
`orthogonalize = deflate|_{gram=I}` specialization *edge* as a cross-reference, but the two
entries stay distinct (precedent: the `inner_product` / `linear_combination` do-NOT-merge
boundary, `book/src/L2/index.md:22-26`; the `orthogonalize` Householder scope-out,
`book/src/L2/orthogonalize.md:301`). The L1 [`nleps_deflated_residual`](../L1/nleps_deflated_residual.md)
entry records the *same* over-unification guard from the other direction
(`book/src/L1/nleps_deflated_residual.md:109`).

## Dependencies

L2 dependencies (other L2 vocabulary or below):

- [`gram`](./gram.md) (L2, firm cycle-022) — the Gram-matrix constructor `XᴴX` (the all-pairs
  `inner_product` fold, `palace/linalg/nleps.cpp:526-531`). `deflate` consumes the Gram as the
  coefficient matrix of the coordinate solve.
- [`lu_solve`](../L1/lu_solve.md) (L1, firm cycle-022) — the small-dense `k×k`
  factor-and-solve against the Gram (Galerkin core) or the Schur block `S` and Schur-modified
  Gram `SS` (NLEPS form). The `Eigen::fullPivLu().solve` at `palace/linalg/nleps.cpp:533-535`.
  Distinct from the iterative big-space [`ksp_solve`](../L1/ksp_solve.md). The factorization
  kernel (full-pivot LU) is `lu_solve`'s contracted load-bearing axis, inherited.
- [`linear_combination`](./linear_combination.md) (L2, firm cycle-018) — the `X·coords`
  back-projection, a length-`k` linear combination over the basis columns (the
  `MatVecMult(X, ·)` at `palace/linalg/nleps.cpp:329-347`, called at `:535`). The final `v − …`
  subtraction is the `axpy`-shaped term of the same fold.
- [`dot`](../L1/dot.md) (L1, firm) — the coordinate extraction `c(j) = X[j]ᴴ v`
  (`palace/linalg/nleps.cpp:522`). The `op.dot` hook is a `dot` substitution. Arg-1-conjugated
  convention pinned (`book/src/L1/dot.md:43`).
- [`inner_product`](./inner_product.md) (L2, firm) — transitively, via [`gram`](./gram.md) (the
  Gram is the all-pairs lift of the scalar `inner_product` fold). Not a direct `deflate`
  dependency.

Related-but-distinct (do **NOT** merge):

- [`orthogonalize`](./orthogonalize.md) (L2, firm) — the orthonormal-basis specialization
  (`gram = I`) by a different algorithm. See § Over-unification guard.
- [`nleps_deflated_residual`](../L1/nleps_deflated_residual.md) (L1, firm cycle-022) — shares
  the `Xᴴ·` / `X·` constituents but computes an extended-NEP-operator *residual*, not a
  projection. The shared constituents are the unification surface; the operators stay distinct
  (`book/src/L1/nleps_deflated_residual.md:109`).

Consumers (the surfaces that fold or call this composition):

- The NLEPS deflated quasi-Newton solver (`QuasiNewtonSolver::Solve`) — the deflation
  projection inside `deflated_solve` (`palace/linalg/nleps.cpp:505-537`); the residual
  back-projection and the Jacobian deflation terms reuse the `X·(S⁻¹·)` back-projection half
  (`palace/linalg/nleps.cpp:563`, `:666-667` — the latter two are the back-projection without a
  fresh coordinate extraction, the carried-coordinate motif). The NLEPS L1>L0 lowering
  (forthcoming) narrates the fused block.

L2>L1 lowering theme (forthcoming; abstractor work, **not** authored here): an
`L2-L1/deflate-composition-lowering` theme will narrate how the named L2 composition lowers
into the fused `deflated_solve` block — the Gram double-loop, the three `fullPivLu().solve`
calls, the `MatVecMult` + `AXPY`. Plain-text forward-reference only — that chapter does not yet
exist.

## Variant axes

Following the [`classify-variant-axis`](../../../skills/classify-variant-axis/SKILL.md) output
contract (per-axis-value: absorption path, load-bearing primitive, state binding):

- **`op.block` ∈ {`Galerkin`, `Schur`}** (the **central, partly-constructive** axis): the
  coordinate-solve block.
  - `Schur { S = λI − H }`: the **positively-sourced** NLEPS form
    (`palace/linalg/nleps.cpp:532-535`). The coordinate solve is the extended-operator
    block-elimination: `SS = −S⁻¹(XᴴX)` (`:533`), `SS⁻¹·c` (`:534`), `S⁻¹·(·)` (`:535`).
    Load-bearing primitive: three [`lu_solve`](../L1/lu_solve.md)s against `S` and `SS`. State
    binding: `S` is re-formed per evaluation point `λ` (the `eig_opInv`/`lam`/`eig` scalar,
    `:532, :562, :664`); `H` is the carried Rayleigh block. This is the geometry of the
    *nonlinear*-eigenvalue extended problem (minimality index 1, Effenberger 2013), not the bare
    `span(X)` projector.
  - `Galerkin` (`S = I`): the **literature-anchored** bare oblique projector
    `I − X(XᴴX)⁻¹Xᴴ` — a single `lu_solve(XᴴX, c)`. This is the `S = I` degenerate case of the
    Schur form and the textbook Galerkin / Rayleigh-Ritz deflation projector. It is **not
    positively exhibited anywhere in Palace** (`search_text` for a bare `(XᴴX)⁻¹` Gram-only
    deflation solve across `palace/linalg/*.cpp` returns hits only inside the Schur-wrapped
    `nleps.cpp` block). Materialized from the deflation-scheme literature
    (`palace/linalg/nleps.cpp:357`); it is the higher-fan-out artifact (general
    eigensolver/preconditioner deflation uses plain oblique projection) but its firm status is
    gated (§ Status).
- **`op.dot` hook ∈ {`canonical ⟨·,·⟩`, `B-weighted`}**: parametric absorption (a closure
  substitution; the composition shape and laws are invariant — law 6). NLEPS uses the canonical
  Hermitian hook (`linalg::Dot`); the `B`-weighted hook is the Galerkin/Rayleigh-Ritz
  generalization (inherited from `gram` / `orthogonalize`). State binding: the weighted hook
  captures the weight operator in the closure.
- **element type ∈ {`real`, `complex`}**: absorbed by the `op.dot` / `linear_combination`
  dependencies (conjugation lives in `dot`). NLEPS is complex (`Eigen::MatrixXcd`); the real
  case is permitted-but-unwitnessed.
- **in-place vs out-of-place** (transparent perf, not a structural variant): Palace's
  `deflated_solve` mutates `x1` in place via `MatVecMult` + `AXPY(-1, …)`
  (`palace/linalg/nleps.cpp:535-536`); the pure L2 form is out-of-place. The standard BLAS
  in-place / output-aliasing axis, an L2>L1 fusion concern, matching `linear_combination`.

## Status

`partly-constructive` — the **structural decomposition is firm** and the **generic-Galerkin-core
sub-part is constructive** (literature-anchored, not positively sourced).

- **Firm part** (the Schur-form pipeline): the `coords ▷ schur-solve ▷ back-project`
  composition is read directly from a **positive** Palace source site — the `deflated_solve`
  lambda (`palace/linalg/nleps.cpp:505-537`), with the source's own block-elimination comment
  (`:508-513`) naming the Schur complement `SS = (B − A T⁻¹ U) = −XᴴX·S⁻¹` in its own words.
  Every constituent is read, not constructed: the coordinate extraction is a positive
  `linalg::Dot` loop (`:519-523`), the Gram build is a positive double-loop (`:526-531`), the
  Schur block is a positive `S = λI − H` (`:532`), the three solves are positive
  `fullPivLu().solve` calls (`:533-535`), the back-projection is a positive `MatVecMult` (`:535`,
  `:329-347`), the subtraction is a positive `AXPY` (`:536`). The dependencies are all firm
  vocabulary (`lu_solve`, `linear_combination`, `dot`; `inner_product` via `gram`). Laws 1–2
  and 6 are syntactic identities on this positive source (linearity of a fixed composition of
  linear maps; empty-basis branch).

- **Constructive sub-part** (the generic Galerkin core `I − X(XᴴX)⁻¹Xᴴ`): the bare oblique
  projector (the `op.block = Galerkin`, `S = I` case) and the projector-specific laws 3–5
  (range-nulling, kernel/range, idempotence) are stated for it. This sub-part is **NOT** read
  from a positive Palace site — Palace only exhibits the Schur-wrapped form. The Galerkin core
  is materialized from (i) the deflation-scheme literature (Effenberger 2013 robust successive
  eigenpair computation; Jarlebring–Koskela–Mele 2018 — `palace/linalg/nleps.cpp:354-362`),
  which defines the oblique-Galerkin deflation projector the Schur form specializes, and
  (ii) the **negative anchor** that no bare-Gram `(XᴴX)⁻¹` deflation solve appears anywhere in
  Palace (`search_text` for a Gram-only deflation projection across `palace/linalg/*.cpp`
  returns only the Schur-wrapped `nleps.cpp` block). The negative anchor is evidence **for** the
  Galerkin core being a faithful `S = I` reconstruction of the positively-sourced Schur form; it
  does NOT license asserting the Galerkin core as a positive Palace claim.

- **Promotion condition** (what makes the whole entry firm): a positive Palace source site that
  exhibits the bare Galerkin deflation projector `I − X(XᴴX)⁻¹Xᴴ` directly (e.g. a future
  linear-EVP deflation path, a preconditioner deflation, or a ROM Galerkin projection that uses
  the Gram inverse without the `S = λI − H` Schur wrapping). Until such a site is dissected, the
  Galerkin core stays constructive and the entry stays `partly-constructive`. Should the
  decision be made to scope `deflate` to the NLEPS Schur form only (dropping the Galerkin
  generalization), the entry would become `firm` on positive structure (the Schur pipeline) with
  the Galerkin core demoted to a literature note — a `same-layer-cross-cutter` scope call, not
  this dispatch's.

**Single-algorithm concentration** (noted, acceptable): all deflation-projection sites are in
`nleps.cpp` (one solver) — the same concentration accepted for the firm
`apply_nonlinear_pencil` / `nleps_deflated_residual`. The combinator's value is (a) pinning the
load-bearing conjugation once for the NLEPS lowering and (b) naming the oblique-projection shape
for anticipated reuse. The cross-algorithm fan-out is forecast, not yet observed; if a future
scan finds no second Gram-`lu_solve` site, the Galerkin-generalization scope is the
`same-layer-cross-cutter`'s call.

**Test-coverage caveat** (inherited, non-gating on the firm part): NLEPS has zero dedicated unit
tests (`search_text` for `QuasiNewton|nleps|fullPivLu|deflat` over `test/unit/**` returns no
deflation-projection coverage). Per CLAUDE.md status guidance the absent test does not gate the
syntactic-identity laws of the firm part (laws 1–2, 6 are operator-algebra facts). The gate on
the whole entry is the missing **positive Galerkin source site**, not the missing test.

## L2 vs L1 distinction

- **L0**: the fused `deflated_solve` block (`palace/linalg/nleps.cpp:505-537`) — the Gram
  double-loop, the `S = λI − H` build, the three `fullPivLu().solve` calls, the `MatVecMult`,
  the in-place `AXPY`. State threading via the destination `x1`; the `A2`/`H`/`X` captured by
  reference.
- **L2**: the *named composition* `deflate op X v → Tensor[$S]` — the `coords ▷ schur-solve ▷
  back-project` pipeline whose constituents (`dot`, `gram`, `lu_solve`, `linear_combination`)
  and projector laws are first-class. L2's role is to de-fuse the hand-written block into the
  canonical composition and surface the projector laws and the central `op.block`
  (Galerkin / Schur) variant, where at L0 they were a fused block of Eigen / `linalg` calls.

## Evidence

All ranges `read_range`-verified and `tools/citecheck/citecheck.py`-anchor-checked this
dispatch (paths relative to `reference/`):

- `palace/linalg/nleps.cpp:505-537` — the `deflated_solve` lambda: the complete positive
  deflation-projection block. `auto deflated_solve =` at `:505`; closing `};` at `:537`.
- `palace/linalg/nleps.cpp:508-513` — the source's own block-elimination comment: the `2×2`
  block system `[[T(σ),U(σ)],[A(σ),B(σ)]]` (`:509-510`), `x1 = T⁻¹ b1` (`:511`), and the
  decisive **Schur-complement** line `x2 = SS⁻¹(b2 − A x1)` where `SS = (B − A T⁻¹ U) = −XᴴX·S⁻¹`
  (`:512`), `x1 = x1 − X S x2` (`:513`). The positive evidence that the projector is
  Schur-modified, NOT the bare Gram.
- `palace/linalg/nleps.cpp:515-518` — `if (k == 0) { return; }` — the empty-deflation
  early-return (law 1, empty-basis identity).
- `palace/linalg/nleps.cpp:519-523` — coordinate extraction loop:
  `x2(j) = b2(j) − linalg::Dot(GetComm(), x1, X[j])` (`:522`) — the `b2 − Xᴴ x1` extended-block
  RHS (the `−⟨X[j],x1⟩` is the deflation coordinate `X[j]ᴴ x1`; semantics point 2).
- `palace/linalg/nleps.cpp:524-531` — the Gram build: `Eigen::MatrixXcd SS(k, k)` (`:524`),
  the double-loop `SS(i, j) = linalg::Dot(GetComm(), X[i], X[j])` (`:529`) = `X[i]ᴴ X[j]` = the
  `gram` constructor (the `XᴴX` Gram matrix).
- `palace/linalg/nleps.cpp:532` — `const Eigen::MatrixXcd S = eig_opInv * Identity(k,k) − H` —
  the `S = λI − H` extended-block linearization (the Schur block).
- `palace/linalg/nleps.cpp:533` — `SS = -S.fullPivLu().solve(SS)` — the Schur-modified Gram
  `SS = −S⁻¹(XᴴX)` (the multi-RHS `k×k` `lu_solve`; `book/src/L1/lu_solve.md:58`).
- `palace/linalg/nleps.cpp:534` — `x2 = SS.fullPivLu().solve(x2)` — the coordinate solve
  `SS⁻¹·c` (single-RHS `lu_solve`).
- `palace/linalg/nleps.cpp:535` — `const ComplexVector XSx2 = MatVecMult(X, S.fullPivLu().solve(x2))`
  — the back-projection `X·(S⁻¹·x2)`: the `lu_solve` (`S⁻¹`) composed with `linear_combination`
  (`MatVecMult(X, ·)`).
- `palace/linalg/nleps.cpp:536` — `linalg::AXPY(-1.0, XSx2, x1)` — the subtraction
  `x1 ← x1 − X·(…)` (semantics point 3; the in-place `axpy` term of the back-projection fold).
- `palace/linalg/nleps.cpp:329-347` — `ComplexVector MatVecMult(const std::vector<ComplexVector>&X, const Eigen::VectorXcd&y)`
  (`:329`): the `X·y` reconstruction (`z = 0; for j: AXPBYPCZ(…) into z`, closing `}` at `:347`)
  — a length-`k` `linear_combination` over the basis, with the complex real/imag split. The
  back-projection primitive at `:535`.
- `palace/linalg/nleps.cpp:562-563` — the residual-site reuse of the back-projection
  (`S = lam·I − H` at `:562`, `XSvv2 = MatVecMult(X, S.fullPivLu().solve(vv2))` at `:563`) — the
  `X·(S⁻¹·)` half on the residual rather than the solve (consumer relationship; see also
  `book/src/L1/nleps_deflated_residual.md`).
- `palace/linalg/nleps.cpp:664-667` — the Jacobian deflation terms: `S = eig·I − H` (`:664`),
  `Sv2 = S.fullPivLu().solve(v2)` (`:665`), `XSv2 = MatVecMult(X, Sv2)` (`:666`),
  `XSSv2 = MatVecMult(X, S.fullPivLu().solve(Sv2))` (`:667`, the nested `S⁻¹(S⁻¹·)`) — the
  back-projection half reused with carried coordinates (no fresh `dot`).
- `palace/linalg/nleps.cpp:606-619` — deflation-basis growth: each converged `v` normalized
  (`scale = linalg::Norml2`, `:610`), `X.resize(k + 1)` (`:614`), `X[k] = v` (`:615`),
  `H.conservativeResizeLike(...)`/`H.col(k)`/`H(k,k) = eig` (`:616-618`), `k++` (`:619`) —
  confirms `X` is the raw normalized-eigenvector basis (NOT orthonormalized → the `(XᴴX)⁻¹` /
  Schur solve is load-bearing; semantics point 1, the over-unification guard's basis-precondition
  row) and the variadic-in-`k` axis.
- `palace/linalg/nleps.cpp:354-362` — the deflation-scheme references (Jarlebring–Koskela–Mele
  2018 quasi-Newton at `:354`; Effenberger 2013 robust successive eigenpair computation at
  `:357`; SLEPc-NEP minimality index 1) — the literature anchor for the Schur form and the
  bare-Galerkin-core generalization (§ Status, constructive sub-part).
- `book/src/L1/lu_solve.md` (firm, cycle-022) — the small-dense `k×k` solve dependency
  (`:3` "small-dense"; RHS-linearity `:56`; multi-RHS column-wise `:58`; kernel-conditioning
  non-law `:63`; `A`-nonlinearity non-law `:64`). The `fullPivLu().solve` realization.
- `book/src/L2/linear_combination.md` (firm, cycle-018) — the `X·coords` back-projection fold
  (`MatVecMult` = length-`k` linear combination).
- `book/src/L2/inner_product.md` (firm) — the scalar fold `gram` lifts to a matrix (via `gram`).
- `book/src/L2/gram.md` (firm, cycle-022) — the Gram-matrix constructor `XᴴX` consumed as the
  coordinate-solve coefficient matrix.
- `book/src/L2/orthogonalize.md` (firm) — the over-unification target: orthonormal-basis
  precondition (`:74`), the `project ▷ subtract` Gram-solve-free algorithm (`:114-142`),
  MGS column-order non-commutativity (`:224`), Householder scope-out boundary (`:301`).
- `book/src/L1/dot.md:43` — the pinned `⟨x, y⟩ = xᴴ y` arg-1-conjugated convention (coordinate
  extraction; semantics point 2).
- `book/src/L1/nleps_deflated_residual.md` (firm, cycle-022) — the related-but-distinct L1
  residual sharing `deflate`'s constituents: the non-orthonormal-basis fact (`:60`), the
  over-unification guard from the other direction (`:109`).
- `book/src/L2/index.md:54-56` — the `gram` (firm) / `deflate` dep-map rows (this dispatch
  flips `deflate` to partly-constructive + a live link to `gram`).
- `reports/2026-05-29T051532Z-combinator-miner-deflate-gram/CYCLE.md` (integrated, commit
  `881f200`) — the proposing combinator report (the shape, the over-unification guard, the
  `project_oblique`-vs-Schur factoring OQ this dispatch decides).
