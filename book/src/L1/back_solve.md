# back_solve

Mutation-lifted small-dense triangular back-solve: `y = back_solve(R, s)`
returns the least-squares correction coefficients `y` solving the upper-triangular
system `R · y = s`, where `R` is the **Givens-rotated upper-triangular R-factor**
of the GMRES / FGMRES running-QR triangularisation and `s` is the rotated
right-hand side accumulated by that triangularisation. The **GMRES
restart-correction back-solve** — the terminal step of the running-QR
least-squares update, producing the coordinate vector `y` whose lift `V·y` / `Z·y`
is the iterate correction folded into the running solution at restart-cycle close.

## Context

The GMRES / FGMRES inner loop maintains a *running QR factorisation* of the
growing `(j+2)×(j+1)` upper-Hessenberg matrix `H̄_j` produced by Arnoldi: each
arriving Hessenberg column is reduced to upper-triangular form by replaying the
stored plane rotations and generating one new rotation, so that after `j+1`
columns the leading `(j+1)×(j+1)` block is an upper-triangular factor `R`, and the
rotated RHS `s` (initialised `s = β₀·e₁`) carries the least-squares residual in its
tail entry `s[j+1]`. That column-by-column triangularisation — the
`replay ▷ generate ▷ apply ▷ apply_rhs` stream — is the **L2 named composition**
[`incremental-least-squares`](../L2/incremental-least-squares.md) (firm cycle-026).
At restart-cycle close (convergence, restart boundary, or max-iterations) the
least-squares problem is finished by **back-solving** the triangular system
`R · y = s` for the coordinate vector `y`. That back-solve is this L1 leaf.

This leaf is the terminal **`back_solve`** projection named by the L2 entry's
signature (`L2/incremental-least-squares.md:81-83`); the concept page
[`concepts/givens`](../concepts/givens.md)
names it as the `back_solve` step "via `trsv`" (`:29`). (Note: the slug
`ls_update_column` at `L2/incremental-least-squares.md:412` and
`concepts/incremental-least-squares.md:14` names the DISTINCT per-column streaming
update step `ls_update_column(K, j, h_new) → K'`, not this terminal back-solve —
hence this leaf takes the artifact-native slug `back_solve`.) It is split out as its own
firm L1 primitive — rather than left as a sub-step inside the L2 composition —
because (i) each layer is coherent within itself and the back-solve is a
self-contained, reusable triangular-solve operation with its own laws, and (ii) it
is the concrete L0-anchored home for the back-solve the `trsv` L3-inventory gap was
searching for. The detailed lowering — how the abstract `R · y = s` back-solve
rewrites into the in-place `s[0..j]` overwrite at L0 — belongs to the forthcoming
L2>L1 `incremental-least-squares-composition-lowering` theme (cycle-027 dispatch 5,
authored concurrently), which forward-references this leaf as its landing target.

**Why this is NOT a general `trsv`.** The `trsv` L3-vocabulary-inventory gap
(`scaffolding/open-questions.md:24,:448`) is **blocked** — a general
sparse-triangular solve (`sparse_triangular_solve`, the Gauss-Seidel / ILU smoother
kernel) has *no positive L0 anchor* in the Palace tree (full-tree search returns
zero hits; it is likely an obstruction-theme target). `back_solve` is **not**
that operator. It is the **specific small-dense back-solve over the
Givens-rotated Hessenberg** that GMRES / FGMRES use to finish the restart-cycle
least-squares correction: the matrix `R` is a *dense, materialized*, small
`(j+1)×(j+1)` upper-triangular block (the running-QR R-factor, `j+1` ≤ the restart
dimension `max_dim`, typically tens), stored column-major in the flat `H` register;
the back-substitution is `O(j²)` dense scalar work, **independent of the field
dimension `N`** — exactly like its small-dense sibling
[`lu_solve`](./lu_solve.md), and unlike a sparse-triangular smoother kernel that
acts on the length-`N` field. Harvesting it as its own primitive gives the
back-solve a firm, positively-anchored L1 home without conflating it with the
unanchored general `trsv`. (The two are siblings on the "triangular solve" axis,
split by the dense-small-coordinate vs sparse-large-field representation/cost
distinction — the same split that separates `lu_solve` from `ksp_solve`.)

This leaf is the small-dense-triangular sibling of [`lu_solve`](./lu_solve.md)
(small-dense *full* LU/QR direct solve): both are coordinate-space dense direct
solves on a materialized `k×k` matrix (the L1 §Semantics motif-6 "Coordinate-space
dense direct algebra", `L1/index.md:25`), `O(k²)`–`O(k³)` scalar work independent
of `N`. `back_solve` is the *triangular* (back-substitution-only) case —
its coefficient matrix is already upper-triangular (the running-QR pre-rotated it),
so no factorisation is needed, only back-substitution. `lu_solve` is the
*general-dense* case (factor + solve). Neither is an [`apply_linop`](./apply_linop.md)
variant: both read the matrix entries (the back-substitution divides by `R`'s
diagonal and subtracts its super-diagonal entries), where `apply_linop` applies an
opaque action and never sees the entries.

## Signature

    back_solve
      :: (R: UpperTri[j+1, j+1], s: Tensor[j+1]) -> Tensor[j+1]

    back_solve(R, s) = the unique y with  R · y = s   (R upper-triangular, non-singular)

Shape contract (bunsen-style, named axes):

- `R` — `UpperTri[j+1, j+1]` — the **dense, materialized, square, upper-triangular**
  R-factor of the running-QR triangularisation. Read-only. The axis `j+1` is the
  small restart-cycle dimension (number of Arnoldi columns accumulated this restart
  cycle; `j+1` ≤ the restart dimension `max_dim`, single to low tens), **not** the
  large field dimension `N`. `R` is the leading `(j+1)×(j+1)` block of the
  Hessenberg register `H` after the running-QR stream has annihilated every
  sub-diagonal — every diagonal and super-diagonal entry present, sub-diagonal zero.
  Its uppertriangularity is load-bearing: it is what makes a *back-substitution*
  (rather than a full factor-and-solve) the right kernel, and it is established by
  the running-QR stream (the [`incremental-least-squares`](../L2/incremental-least-squares.md)
  L2 composition), not by this leaf.
- `s` — `Tensor[j+1]` — the right-hand side: the leading `j+1` entries of the
  rotated RHS accumulated by the running-QR stream (`s` started as `β₀·e₁`, each
  arriving column's rotation propagated to it; the tail entry `s[j+1]` — the
  least-squares residual — is **not** part of the back-solve's RHS). Read on entry.
  The element type is `ScalarType` (complex in the complex case, real otherwise),
  matching the `s` register declaration (`iterative.hpp:193`).
- result — `Tensor[j+1]` — the least-squares minimiser `y` of
  `‖β₀·e₁ − H̄_j · y‖₂`, the coordinate vector whose basis-lift `V·y` (GMRES) /
  `Z·y` (FGMRES) is the iterate correction. Same shape as `s`.

The matrix is **square and upper-triangular** (`(j+1)×(j+1)`). The empty-stream
case (`j = -1`, no columns accumulated this restart cycle) is the identity:
`back_solve` over an empty `R` yields `y = []` (the loop `for (int i = j;
i >= 0; …)` does not execute, `iterative.cpp:653`), and the downstream correction
`V·y` is the zero vector. The single-column case (`j = 0`) is one scalar division
`y[0] = s[0] / R[0][0]` (the inner subtract loop is empty).

The lift of `y` into the field-space correction (`V·y` / `Z·y`) is **not** part of
this leaf — it is a [`linear_combination`](../L2/linear_combination.md) of basis
vectors, performed by the caller (`x.Add(s[k], V[k])` `iterative.cpp:666` / `Z[k]`
`:843`). This leaf produces only the coordinate vector `y`; the basis choice
(`V` vs `Z`) is the consuming L2 composition's `op.basis_kind` axis, invisible here.

## Semantics

`back_solve(R, s)` returns the unique vector `y` satisfying `R · y = s` for
the upper-triangular non-singular `R`, computed by **back-substitution**: starting
from the last coordinate (largest index) and working backward, each `y[i]` is
solved from the already-computed `y[i+1..j]`. The standard QR least-squares solve:
because the running-QR stream has reduced the Hessenberg least-squares problem
`min_y ‖β₀·e₁ − H̄_j·y‖₂` to the triangular system `R · y = s` (with `R` the
upper-triangular R-factor and `s` the rotated RHS over the leading block), the
back-solved `y` is exactly the least-squares minimiser.

The L1 form is pure-functional: the same `(R, s)` yields the same `y`. The L0
source (`iterative.cpp:652-660` GMRES; `:831-840` FGMRES) overwrites the RHS buffer
`s[0..j]` in place with `y` — the destination *is* the RHS argument — and reads the
upper-triangular factor out of the flat column-major Hessenberg register `H` via a
stride pointer:

    // iterative.cpp:652  "Reconstruct the solution (for restart / convergence / max-it)"
    for (int i = j; i >= 0; i--) {                  // :653  back-substitution, descending i
      ScalarType *Hi = H.data() + i * (max_dim + 1);  // :655  Hi = column i of the column-major R-factor
      s[i] /= Hi[i];                                  // :656  divide by the diagonal R[i][i]
      for (int k = i - 1; k >= 0; k--)                // :657  for the super-diagonal entries above row i
        s[k] -= Hi[k] * s[i];                         // :659  subtract R[k][i] * y[i] from RHS[k]
    }                                                 // :660  leaving y = s[0..j]

The flat storage `Hi = H.data() + i*(max_dim+1)` (`:655`) is column `i` of the
column-major R-factor (stride `max_dim+1`); `Hi[i]` is the diagonal `R[i][i]`, and
`Hi[k]` (for `k < i`) is the entry `R[k][i]` *above* the diagonal in column `i` —
the super-diagonal entries the back-substitution eliminates. The in-place RHS
overwrite, the flat column-major storage stride, and the `Hi` pointer arithmetic are
L1>L0 lowering concerns (the forthcoming
`incremental-least-squares-composition-lowering` theme), not part of the L1
signature.

Two semantic points are load-bearing and recorded rather than smoothed:

**(1) `R` must be upper-triangular and non-singular; the result is the unique
exact-arithmetic least-squares minimiser.** The defining contract is
`R · back_solve(R, s) = s` for upper-triangular non-singular `R`. The
upper-triangularity is established by the running-QR stream (the
[`incremental-least-squares`](../L2/incremental-least-squares.md) composition has
annihilated every sub-diagonal); non-singularity holds unless Arnoldi breaks down
(a zero diagonal `R[i][i]` would divide-by-zero at `:656`, the lucky-breakdown /
exact-convergence case Palace handles upstream by the residual test exiting before
back-solve). The applicability condition is therefore: **`R` square,
upper-triangular, and (for the contracted semantics) non-singular.**

**(2) The back-substitution reduction order is load-bearing
finite-precision structure, not a transparent reorder.** The descending-`i` /
descending-`k` sweep (`iterative.cpp:653,:657`) pins a specific finite-precision
reduction path: each `y[i]` is formed from the diagonal division then the
super-diagonal corrections in a fixed order. This is the standard back-substitution
order; for the *exact-arithmetic* least-squares value it is irrelevant (law 1 holds
for any consistent ordering), but the *floating-point* result depends on it. Per the
CLAUDE.md numerical-trick taxonomy this is a **load-bearing numerical** detail (the
reduction order is part of the algorithm's finite-precision behaviour, jointly with
the running-QR rotation order that produced `R` and `s` — see the L2 entry's
rotation-stream non-associativity non-law, `L2/incremental-least-squares.md:278-285`).
It is **not** a transparent reorder: a different summation order would give a
bit-different `y`. The exact per-lowered-call reduction order is pinned by the
forthcoming L2>L1 theme. (The back-solve is *not* a reduction in the
`dot`/`nrm2` sense — there is no cross-rank `MPI_Allreduce`; the matrix `R` and the
vector `s` are redundant-on-all-ranks small coordinate data, so the back-solve is a
local dense computation with no collective, exactly like [`lu_solve`](./lu_solve.md).)

## Algebraic laws

The laws below hold; absences are deliberate. "Exact" means exact arithmetic.

1. **Solve inverts apply (the defining contract).** `R · back_solve(R, s) = s`
   for any `s`, and `back_solve(R, R · y) = y` for any `y`, **when `R` is
   upper-triangular and non-singular**. This is the defining property —
   `back_solve(R, ·) = R⁻¹` as a function on the leading block. The
   back-substitution at `iterative.cpp:656,:659` computes exactly this. The least-
   squares interpretation: `y` minimises `‖β₀·e₁ − H̄_j·y‖₂` because the running-QR
   stream reduced that problem to `R·y = s` (norm-preservation under the unitary
   rotation stream — the L2 entry's residual-exposure law,
   `L2/incremental-least-squares.md:225-232`).

2. **Linearity in the RHS.** `back_solve(R, α·s₁ + β·s₂) = α·back_solve(R, s₁)
   + β·back_solve(R, s₂)` for scalars `α, β`. Holds because for fixed
   upper-triangular non-singular `R`, `back_solve(R, ·) = R⁻¹` is a linear map.
   In particular `back_solve(R, 0) = 0` (the `α = β = 0` case).

3. **Compose-with-scale on the coefficient.** `back_solve(c·R, s) =
   (1/c)·back_solve(R, s)` for any nonzero scalar `c` (since `(cR)⁻¹ = c⁻¹R⁻¹`,
   and `c·R` is still upper-triangular). A true identity; not exploited in Palace (the
   R-factor is produced by the rotation stream, never explicitly scaled).

4. **Back-substitution correctness (descending recurrence).** The result satisfies
   the back-substitution recurrence `y[i] = (s[i] − Σ_{k>i} R[i][k]·y[k]) / R[i][i]`
   for `i = j, j−1, …, 0`. The Palace loop realises the *transposed-index* form (it
   sweeps column `i` and subtracts `R[k][i]·y[i]` from `s[k]` for `k < i`,
   `iterative.cpp:659`) — the column-oriented variant of row-oriented
   back-substitution, computing the same `y` (the super-diagonal corrections are
   applied eagerly as each `y[i]` is solved, rather than gathered per row). Both
   orderings yield the same exact-arithmetic `y` (they differ only in the
   finite-precision summation grouping — law-2's non-law below).

5. **Empty / single-column boundary.** The empty restart cycle (`j = -1`) yields
   `y = []` (the `for (int i = j; i >= 0; …)` loop body does not execute,
   `iterative.cpp:653`); the downstream correction `V·y` is the zero vector. The
   single column (`j = 0`) is one scalar division `y[0] = s[0] / R[0][0]`
   (`:656` with the inner `k` loop empty). Both are degenerate cases of law 1.

6. **Basis-lift independence.** The coordinate vector `y` this leaf produces is
   **independent of which basis the caller lifts it against** (`V` for GMRES /
   left-preconditioned, `Z` for FGMRES). The GMRES and FGMRES back-solve code is
   line-for-line identical (`iterative.cpp:652-660` ≡ `:831-840`); only the
   downstream `linear_combination` reconstruction reads a different basis
   (`x.Add(s[k], V[k])` `:666` vs `x.Add(s[k], Z[k])` `:843`). This leaf has no
   knowledge of the basis; the basis choice is the consuming L2 composition's
   `op.basis_kind` axis.

Laws that explicitly **do not** hold:

- **Reduction-order independence of the floating-point result.** The
  descending-`i` / column-oriented super-diagonal subtraction
  (`iterative.cpp:653-659`) pins a specific finite-precision reduction path; a
  different back-substitution ordering (row-oriented, or ascending) gives the same
  exact-arithmetic `y` (law 4) but a **bit-different** finite-precision `y`.
  Load-bearing per the CLAUDE.md numerical-trick taxonomy — recorded as a non-law so
  callers do not treat the summation order as a free choice. (Jointly with the
  running-QR rotation order that produced `R`/`s`, this pins the GMRES
  finite-precision solution path; see the L2 entry's rotation-stream
  non-associativity non-law, `L2/incremental-least-squares.md:278-285`.)
- **Linearity / any structure in the coefficient `R`.** `back_solve(·, s)` is
  **not** linear in `R` (`back_solve(R₁ + R₂, s) ≠ back_solve(R₁, s) +
  back_solve(R₂, s)` — matrix inversion is nonlinear). Recorded so the
  running-QR update code does not attempt to distribute a back-solve over an
  R-factor sum.
- **Definedness without non-singularity.** For singular upper-triangular `R` (a zero
  diagonal entry — the Arnoldi lucky-breakdown / exact-convergence case),
  `back_solve(R, s)` divides by zero at `iterative.cpp:656` and is undefined.
  Palace exits via the residual test (`converged = (beta < eps)`,
  `iterative.cpp:644`) before reaching the back-solve in that case. Recorded as an
  applicability boundary, not a law.
- **General-`trsv` membership.** This is **not** a general sparse-triangular solve
  (`trsv` / `sparse_triangular_solve`, the Gauss-Seidel / ILU smoother kernel acting
  on the length-`N` field). It is the *small-dense* back-solve over the running-QR
  R-factor (coordinate-space, dimension `j+1` ≤ `max_dim`, no collective). The
  general `trsv` has no positive L0 anchor (OQ `:448`); this leaf does not stand in
  for it. Recorded so the `trsv` L3-inventory gap is not falsely treated as closed by
  this firm entry (it is the GMRES-restart-correction back-solve, a sibling of the
  unanchored general `trsv`, not the general `trsv` itself).

## Dependencies

(leaf) — `back_solve` depends on no other L1 operator. It consumes a **dense
materialized upper-triangular matrix** `R` and a dense RHS `s`, both in small
coordinate space (dimension `j+1` ≤ `max_dim`), and produces a dense solution `y`;
the back-substitution (diagonal division + super-diagonal subtraction) is atomic at
L1 (the flat column-major storage stride, the `Hi` pointer arithmetic, and the
in-place RHS overwrite surface only in the L1>L0 lowering). In particular it is
**not** built on [`apply_linop`](./apply_linop.md) (which applies an *opaque*
operator and never reads its entries — the back-solve reads `R`'s diagonal and
super-diagonal entries) and is **not** built on [`ksp_solve`](./ksp_solve.md) (the
large-sparse iterative solve over the length-`N` field).

It is the small-dense-*triangular* sibling of [`lu_solve`](./lu_solve.md) (the
small-dense-*general* direct solve) on the "small-dense coordinate solve" axis, split
by the already-triangular (back-substitution-only) vs general (factor-and-solve)
distinction. Both are siblings of [`ksp_solve`](./ksp_solve.md) on the broader
"solve a linear system" axis, split by the dense-direct-coordinate vs
sparse-iterative-field representation/cost distinction (the L1 §Semantics motif-6,
`L1/index.md:25`).

`back_solve` is the per-restart-cycle back-solve atom that the L2
[`incremental-least-squares`](../L2/incremental-least-squares.md) named composition's
terminal `back_solve` projection depends on (the running-QR stream triangularises;
this leaf finishes the least-squares solve). The lift of its output `y` into the
field-space correction is a [`linear_combination`](../L2/linear_combination.md) of
basis vectors performed by the caller (`x.Add(s[k], V[k])` / `Z[k]`), not by this
leaf.

Concept references (cross-cutting; do not duplicate):

- [`concepts/givens`](../concepts/givens.md) —
  the narrative cross-cut naming the `back_solve` step (the `back_solve` "via `trsv`"
  at `:29`); the role: finish the running-QR least-squares solve by back-substitution.

## Variant axes

`back_solve` has the following variant axes at L1; all are absorbed (this leaf,
unlike its general-dense sibling `lu_solve`, has no contracted load-bearing kernel
axis — back-substitution is the only kernel for an already-triangular matrix).

- **element type** (absorbed): `complex` | `real`. The Palace GMRES/FGMRES registers
  are `ScalarType` (complex in the complex-arithmetic case, real otherwise) — `s`,
  `sn`, `H` are `ScalarType`; `cs` is always `RealType` (`iterative.hpp:193-194`).
  The back-substitution divides and subtracts `ScalarType` values uniformly
  (`iterative.cpp:656,:659`); the element type is fixed at solver instantiation, no
  per-call branching. Absorbed as a uniform element-type parameter.
- **basis the output is lifted against** (absorbed — NOT a structural axis of this
  leaf): `V` (GMRES / left-preconditioned) | `Z` (FGMRES / flexible-preconditioner).
  The back-solve code is line-for-line identical across the two
  (`iterative.cpp:652-660` ≡ `:831-840`); the basis is read only by the downstream
  `linear_combination` reconstruction (`:666` `V` vs `:843` `Z`), not by this leaf.
  This is the consuming L2 composition's `op.basis_kind` axis
  (`L2/incremental-least-squares.md:265-271` law 6); it is invisible at this leaf and
  recorded here only to make the no-structural-variant explicit (law 6).
- **restart dimension `j+1`** (parameterised, absorbed-as-form): the small coordinate
  dimension (number of accumulated Arnoldi columns this restart cycle), `j+1` ≤ the
  restart dimension `max_dim`. A size parameter, not a behavioural variant; the
  back-substitution is dimension-uniform.

There is **no** factorisation-kernel axis (unlike [`lu_solve`](./lu_solve.md)): `R`
is already upper-triangular (the running-QR pre-rotated it), so no
factorisation choice exists — back-substitution is the unique kernel. There is **no**
reduction-strategy axis on the summation order — the descending column-oriented sweep
is fixed and load-bearing (the reduction-order non-law), not a selectable strategy.

## Status

`firm` — the operator's structure is read directly from **positive** Palace source:
the in-place back-substitution loop `iterative.cpp:652-660` (GMRES, "Reconstruct the
solution") and its line-for-line identical FGMRES twin `:831-840`, both read in full;
the diagonal division `s[i] /= Hi[i]` (`:656` / `:835`), the super-diagonal
subtraction `s[k] -= Hi[k] * s[i]` (`:659` / `:838`), the column-major stride
`Hi = H.data() + i*(max_dim+1)` (`:655` / `:834`), and the descending sweep bounds
(`:653` / `:657`) are all positively anchored. The signature's shape (square
upper-triangular dense `(j+1)×(j+1)` R-factor, dense RHS `s`, dense solution `y`)
matches the leading block of the `ScalarType` Hessenberg register and the `s`
register (`iterative.hpp:193`); the algebraic laws are standard properties of the
inverse of a fixed non-singular upper-triangular matrix (solve-inverts-apply,
RHS-linearity, reciprocal-scaling, back-substitution-correctness) modulo the
explicitly-recorded reduction-order, `R`-nonlinearity, and singular-`R` non-laws.

This is the **firm-on-positive-structure** decision, exactly as for the small-dense
sibling [`lu_solve`](./lu_solve.md) and for [`apply_linop`](./apply_linop.md) /
[`apply_nonlinear_pencil`](./apply_nonlinear_pencil.md): every law is a **syntactic
identity on fully-specified positive source** (operator-algebra facts about `R⁻¹` on
the leading block), not a convergence fact. No dedicated GMRES/FGMRES running-QR
back-solve unit test exists in `reference/palace/test/unit/` (the GMRES path is
exercised only end-to-end — the same coverage situation as the parent L2
[`incremental-least-squares`](../L2/incremental-least-squares.md), firm cycle-026, and
its sibling `lu_solve`). Per the CLAUDE.md status-tier guidance, **a missing test does
not gate syntactic-identity laws** (the `apply_linop` / `lu_solve`
firm-on-positive-structure situation, not the `eigsolve`-convergence-semantics
situation): the laws do not depend on iteration or convergence behaviour, so the
absent test does not reduce law-confidence. Hence `firm`, not `rough-in
(test-coverage-bounded)`. The one load-bearing caveat (the back-substitution
reduction-order non-law) is carried as a recorded non-law with its numerical property
stated, not as a status reduction — the *value* the operator computes is
reduction-order-independent and fully specified.

Resolves OQ `ls-update-column-l1-leaf` (the back-solve now has a firm,
positively-anchored L1 home). It **relates to but does not close** the open `trsv`
L1-localization / L3-inventory gap (`scaffolding/open-questions.md:24,:448`): this
leaf is the GMRES-restart-correction back-solve, a *sibling* of the still-unanchored
general `trsv` (sparse-triangular smoother kernel), not the general `trsv` itself —
the `trsv` gap stays open (likely an obstruction-theme target, no positive L0 anchor).

## L1 vs L0 distinction

- **L0**: an in-place dense back-substitution overwriting the RHS buffer `s[0..j]`,
  reading the upper-triangular factor out of the flat column-major Hessenberg register
  `H` via a stride pointer. GMRES: `for (int i = j; i >= 0; i--) { Hi = H.data() +
  i*(max_dim+1); s[i] /= Hi[i]; for (int k = i-1; k >= 0; k--) s[k] -= Hi[k]*s[i]; }`
  (`iterative.cpp:653-660`) — the descending sweep, the diagonal division, the
  column-oriented super-diagonal subtraction, the result left in `s[0..j]`. FGMRES:
  line-for-line identical (`:832-840`). The flat column-major storage, the `Hi`
  pointer arithmetic, the in-place RHS-as-destination overwrite, and the `max_dim+1`
  stride are L0 mechanism.
- **L1**: pure-functional `y = back_solve(R, s)`. No destination buffer in the
  signature, no flat-storage stride, no `Hi` pointer arithmetic. One operator over a
  dense upper-triangular `R` and a dense RHS `s`, parameterised by the element-type
  axis (absorbed) and the restart-dimension size (absorbed). Solve-inverts-apply and
  RHS-linearity hold; `R`-nonlinearity, singular-`R`, and reduction-order are recorded
  as explicit non-laws. (The detailed lowering — how the abstract `R·y = s`
  back-solve rewrites into the in-place `s[0..j]` overwrite + column-major stride
  access at L0 — belongs to the forthcoming L2>L1
  `incremental-least-squares-composition-lowering` theme, cycle-027 dispatch 5.)

## Evidence

- `palace/linalg/iterative.cpp:652` — GMRES back-solve comment "Reconstruct the
  solution (for restart or due to convergence or maximum iterations)" — the
  restart-cycle terminal back-solve. **Self-verified via citecheck `--anchor
  'Reconstruct the solution'` (line 652).**
- `palace/linalg/iterative.cpp:653` — `for (int i = j; i >= 0; i--)` — the descending
  back-substitution sweep over the `j+1` accumulated columns; `i = -1` (empty cycle)
  skips the body (law 5). **Self-verified (`--anchor 'for (int i = j'`).**
- `palace/linalg/iterative.cpp:655` — `ScalarType *Hi = H.data() + i * (max_dim + 1);`
  — column `i` of the flat column-major R-factor (stride `max_dim+1`). Grounds the
  upper-triangular dense-materialized shape and the L0 flat storage. **Self-verified
  (`--anchor 'H.data() + i * (max_dim + 1)'`).**
- `palace/linalg/iterative.cpp:656` — `s[i] /= Hi[i];` — the diagonal division
  `y[i] = s[i]/R[i][i]` (law 1, law 4; the singular-`R` divide-by-zero boundary).
  **Self-verified (`--anchor 's[i] /= Hi[i]'`).**
- `palace/linalg/iterative.cpp:657` — `for (int k = i - 1; k >= 0; k--)` — the inner
  super-diagonal subtraction loop (empty for `i = 0`, the single-column case law 5).
  **Self-verified (`--anchor 'for (int k = i - 1'`).**
- `palace/linalg/iterative.cpp:659` — `s[k] -= Hi[k] * s[i];` — the column-oriented
  super-diagonal subtraction `s[k] -= R[k][i]·y[i]` (law 4 transposed-index form; the
  reduction-order non-law). **Self-verified (`--anchor 's[k] -= Hi[k] * s[i]'`).**
- `palace/linalg/iterative.cpp:666` — `x.Add(s[k], V[k]);` — the downstream
  `linear_combination` lift `x += Σ_k y[k]·V[k]` (GMRES `V` basis); NOT part of this
  leaf — recorded to ground law 6 (basis-lift independence). **Self-verified
  (`--anchor 'x.Add(s[k], V[k])'`).**
- `palace/linalg/iterative.cpp:831` — FGMRES back-solve comment "Reconstruct the
  solution" — the FGMRES restart-cycle terminal back-solve. **Self-verified
  (`--anchor 'Reconstruct the solution'`).**
- `palace/linalg/iterative.cpp:835` — FGMRES `s[i] /= Hi[i];` — the diagonal division,
  identical to GMRES `:656` (law 6: back-solve code line-for-line identical).
  **Self-verified (`--anchor 's[i] /= Hi[i]'`).**
- `palace/linalg/iterative.cpp:838` — FGMRES `s[k] -= Hi[k] * s[i];` — the
  super-diagonal subtraction, identical to GMRES `:659`. **Self-verified (`--anchor
  's[k] -= Hi[k] * s[i]'`).**
- `palace/linalg/iterative.cpp:843` — FGMRES `x.Add(s[k], Z[k]);` — the downstream
  lift against the flexible-preconditioner basis `Z` (FGMRES `Z` basis; the
  `op.basis_kind = Z` reconstruction); NOT part of this leaf — grounds law 6.
  **Self-verified (`--anchor 'x.Add(s[k], Z[k])'`).**
- `palace/linalg/iterative.cpp:612` — `s[0] = beta;` — the RHS initialisation
  `s = β₀·e₁` (the running-QR seed; the back-solve's RHS `s[0..j]` is the rotated
  descendant of this seed). **Self-verified (`--anchor 's[0] = beta'`).**
- `palace/linalg/iterative.cpp:642` — `beta = std::abs(s[j + 1]);` — the LS residual
  (the *tail* entry `s[j+1]`, NOT part of the back-solve RHS — the back-solve uses
  `s[0..j]`). **Self-verified (`--anchor 'beta = std::abs'`).**
- `palace/linalg/iterative.cpp:644` — `converged = (beta < eps);` — the convergence
  test that exits before the back-solve in the lucky-breakdown case (singular-`R`
  non-law boundary). **Self-verified (`--anchor 'converged = (beta < eps)'`).**
- `palace/linalg/iterative.cpp:631` — `Hj[j + 1] = linalg::Norml2(comm, w);` — the
  sub-diagonal `‖residual‖` entry the running-QR stream annihilates (context: the
  R-factor `back_solve` consumes is what remains after the stream zeroes every
  such sub-diagonal). **Self-verified (`--anchor 'Norml2'`).**
- `palace/linalg/iterative.hpp:193` — `mutable std::vector<ScalarType> s, sn;` — the
  RHS register `s` (and rotation register `sn`) element type `ScalarType` (complex in
  the complex case). Grounds the `s`/`R` element-type axis. **Self-verified
  (`--anchor 's, sn'` line 193).**
- `palace/linalg/iterative.hpp:194` — `mutable std::vector<RealType> cs;` — the cosine
  register `cs` always `RealType` (the element-type split underwriting the
  real/complex axis; not directly consumed by the back-solve but completes the
  register-type picture). **Self-verified (`--anchor 'cs'` line 194).**
- `book/src/L2/incremental-least-squares.md` — the firm L2 named composition (cycle-026);
  this leaf is its terminal `back_solve` projection (`:81-83`); the
  running-QR stream that produces the R-factor `R` and RHS `s` this leaf consumes;
  the rotation-stream non-associativity non-law (`:278-285`) that this leaf's
  reduction-order non-law composes with. (`:412` and
  `concepts/incremental-least-squares.md:14` bind the slug `ls_update_column` to the
  DISTINCT per-column streaming update step `ls_update_column(K,j,h_new)→K'`, not
  this terminal back-solve — hence this leaf is `back_solve`, not `ls_update_column`.)
- `book/src/concepts/givens.md` — the cross-cutting concept page;
  names the `back_solve` step "via `trsv`" (`:29`) — this leaf is that `back_solve`.
- `book/src/L1/lu_solve.md` — the firm small-dense-general direct-solve sibling
  (cycle-022); the structural template and the firm-on-positive-structure /
  no-dedicated-test precedent.
