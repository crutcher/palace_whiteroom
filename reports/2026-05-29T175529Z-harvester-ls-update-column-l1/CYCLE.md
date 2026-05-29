---
agent: harvester
invoked_at: 2026-05-29T175529Z
scope: L1 operator: back_solve (harvested under dispatch-scope name `ls_update_column`; renamed to artifact-native `back_solve` at repair — `ls_update_column` collides with the L2 column-streaming step)
status: integrated
integrated_at: 2026-05-29T21:15:00Z
integration_commit: 8f14978
integration_notes: "cycle-027 finalize. NEW firm L1 leaf back_solve (the GMRES/FGMRES restart-correction back-solve y = back_solve(R, s) over the small-dense Givens-rotated upper-triangular R-factor; terminal back_solve projection of the firm L2 incremental-least-squares; small-dense-triangular sibling of lu_solve on the coordinate-space dense-direct-solve axis [motif 6], explicitly NOT a general trsv and NOT an apply_linop variant; firm-on-positive-structure iterative.cpp:652-660 GMRES + line-for-line-identical FGMRES :831-840; one load-bearing non-law [descending column-oriented back-substitution reduction order]). L1 firm 20→21. RENAMED IN REPAIR from ls_update_column to back_solve to resolve a slug collision — the ls_update_column slug stays reserved for the distinct still-un-harvested column-streaming step. Resolves OQ ls-update-column-l1-leaf; the trsv L3-inventory gap stays OPEN. Finalize bumped L1/index.md:31 Firm (20)→(21) + motif enumeration as measurable housekeeping (harvester correctly deferred the count-prose bump). SUMMARY-registered + link-clean; retroactive-budget 0; clean build."
inputs:
  - book/src/L2/incremental-least-squares.md (firm L2 named composition, cycle-026 — the back-solve is its terminal `back_solve` projection)
  - book/src/concepts/givens.md (the cross-cutting concept page; names the `back_solve` "via `trsv`" connection at :29)
  - book/src/concepts/incremental-least-squares.md (the cross-cutting concept page; names the DISTINCT column-streaming `ls_update_column(K,j,h_new)→K'` step at :14 — not this back-solve leaf)
  - book/src/L1/lu_solve.md (firm sibling — the small-dense direct-solve L1 leaf; structural template)
  - palace/linalg/iterative.cpp:652-660 (GMRES back-solve) / :831-840 (FGMRES back-solve) — the L0 source, self-verified on-disk via citecheck
  - palace/linalg/iterative.hpp:193-194 (rotation-register declarations — element-type split)
  - scaffolding/open-questions.md (OQ ls-update-column-l1-leaf to resolve; the trsv L3-inventory gap at :24/:448)
  - cycle-027 dispatch 5 (L2>L1 incremental-least-squares-composition-lowering theme — forward-references this leaf as its landing target)
---

# CYCLE: Formalize back_solve at L1

## Summary

This dispatch firms the L1 leaf **`back_solve`** — the atomic
back-substitution step that solves the small upper-triangular system `R · y = s`
produced by the GMRES / FGMRES running-QR triangularisation of the
upper-Hessenberg least-squares problem, producing the least-squares correction
coefficients `y` (overwriting `s[0..j]` in place). It is the terminal
**`back_solve`** projection of the firm L2 named composition
[`incremental-least-squares`](../../book/src/L2/incremental-least-squares.md)
(firmed cycle-026): the running-QR stream triangularises the Hessenberg
column-by-column, and at restart-cycle close this leaf back-solves the resulting
triangular factor for the coordinate vector `y`. Its existence is named (as a
plain-text forward-reference) by the L2 entry's §Dependencies ("an L1 `trsv` leaf
is the natural lowering target, forthcoming", `L2/incremental-least-squares.md:308`)
and by the L2 signature's terminal **`back_solve`** projection
(`L2/incremental-least-squares.md:81-83`), and by the concept page
[`concepts/givens`](../../book/src/concepts/givens.md)
(the `back_solve` "via `trsv`" at `:29`). The L0 source is the in-place
back-substitution loop `iterative.cpp:652-660` (GMRES, "Reconstruct the
solution") and its line-for-line identical FGMRES twin `:831-840`. This is the
**concrete L1 home** for the back-solve the long-blocked `trsv` L3-inventory gap
was searching for — but it is harvested as its **own** firm primitive, the GMRES
restart-correction back-solve over the Givens-rotated Hessenberg, **distinct from
a general `trsv`** (which has no positive L0 anchor and is likely an
obstruction-theme target, per OQ `:448`). Firm-on-positive-structure (a read
closure over the `iterative.cpp` loop). Resolves OQ `ls-update-column-l1-leaf`;
relates to (does not close) the open `trsv` L1-localization gap. L1 firm count
goes 20→21.

## Proposed changes

```new:book/src/L1/back_solve.md
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
```

```edit:book/src/L1/index.md
| [`nleps_eigenvalue_correction`](./nleps_eigenvalue_correction.md) | `(resid: ExtendedVec[N, k], jac_action: Tensor[N], proj_dir: ExtendedVec[N, k]) → { δλ: Complex, z: Tensor[N], z2: Vec[k] }` (projected scalar Newton step `δλ = −⟨[w0;w2],[u;u2]⟩ / ⟨[w0;w2],w⟩`; coupled vector-step RHS `z = −δλ·w − u`, `z2 = −u2`) | [`dot`](./dot.md) (the three projected inner products); [`axpby`](./axpby.md) (big-space RHS), [`scal`](./scal.md) (coordinate RHS) | `firm` (NEP eigenvalue-correction interior atom; L0: `palace/linalg/nleps.cpp:672-677` positive site + `:587,:657,:542-545,:682,:691,:708` consumer/producer sites; harvested cycle-024; scalar Newton half of the coupled `(λ, v)` step; consumes residual + Jacobian-action, feeds `nleps_deflated_solve`; `eigsolve`-inherited no-dedicated-test caveat non-gating) |
| [`back_solve`](./back_solve.md) | `(R: UpperTri[j+1, j+1], s: Tensor[j+1]) → Tensor[j+1]` (i.e. `R⁻¹s` — the GMRES/FGMRES restart-correction back-solve `R·y = s` over the running-QR R-factor) | (leaf; dense materialized upper-triangular matrix; small-dense-triangular sibling of `lu_solve` and `ksp_solve` on the solve-a-system axis, NOT a dependency, NOT an `apply_linop` variant, NOT a general `trsv`) | `firm` (GMRES restart-correction back-solve; L0: `palace/linalg/iterative.cpp:652-660` GMRES + `:831-840` FGMRES; harvested cycle-027; terminal `back_solve` of L2 `incremental-least-squares`; firm-on-positive-structure, no-dedicated-test caveat non-gating; reduction-order load-bearing non-law) |
```

(Dep-map row appended after the `nleps_eigenvalue_correction` row — the last firm row before the rough-in obstruction rows. The `nleps_eigenvalue_correction` row is reproduced verbatim as the unique anchor.)

```edit:book/src/L1/index.md
- [`nleps_eigenvalue_correction`](./nleps_eigenvalue_correction.md) — pure-functional **quasi-Newton eigenvalue-correction step** of the nonlinear eigenvalue problem `{ δλ, z, z2 } = nleps_eigenvalue_correction(resid, jac_action, proj_dir)`; the scalar half of the coupled `(λ, v)` Newton step. Given the committed extended residual `[u; u2]`, the Jacobian action `w = J·v`, and a (deflated) projection direction `[w0; w2]`, it computes the undamped projected one-dimensional Newton ratio `δλ = −⟨[w0;w2], [u;u2]⟩ / ⟨[w0;w2], w⟩` and assembles the coupled vector-step RHS `[z; z2] = [−δλ·w − u; −u2]` that [`nleps_deflated_solve`](./nleps_deflated_solve.md) inverts. The **scalar coupling** between the residual and the Jacobian — the eigenvalue moves by a rank-one projected ratio while the eigenvector moves by the deflated linear solve of the assembled RHS; the Armijo line search damps the combined `(δλ, du)` step. Consumes [`nleps_deflated_residual`](./nleps_deflated_residual.md) (residual) + [`nleps_jacobian_action`](./nleps_jacobian_action.md) (Jacobian action), feeds [`nleps_deflated_solve`](./nleps_deflated_solve.md) (RHS). Factors entirely through firm BLAS-1 leaves ([`dot`](./dot.md) for the three projected inner products, [`axpby`](./axpby.md) for the big-space RHS, [`scal`](./scal.md) for the coordinate RHS). Firm on exhaustive positive structural citation of the sole eigenvalue-correction block (`palace/linalg/nleps.cpp:672-677`); the conjugated operand in all three inner products is the projection direction, the Jacobian action has no coordinate part (lower block-row `[Xᴴ, 0]` is `λ`-independent), and the well-definedness-when-`⟨[w0;w2],w⟩=0` / undamped-`δλ` / `λ`-nonlinearity facts are recorded as non-laws (not test-gated identities). The `eigsolve`-inherited no-dedicated-test caveat is non-gating. The fifth (and final deferred) NEP-interior atom at L1 — closing the per-step quasi-Newton chain `residual → jacobian-action → eigenvalue-correction → deflated-solve → line-search`.
- [`back_solve`](./back_solve.md) — pure-functional **GMRES / FGMRES restart-correction back-solve** `y = back_solve(R, s)`; solves the small-dense upper-triangular system `R · y = s` over the **Givens-rotated R-factor** of the running-QR triangularisation, producing the least-squares correction coordinate vector `y` (whose basis-lift `V·y` / `Z·y` is the iterate correction folded at restart-cycle close). The terminal **`back_solve`** projection of the firm L2 named composition [`incremental-least-squares`](../L2/incremental-least-squares.md) (the running-QR stream triangularises; this leaf finishes the LS solve). The **small-dense-triangular** sibling of [`lu_solve`](./lu_solve.md) (small-dense *general* direct solve) on the coordinate-space dense-direct-solve axis (motif 6), split by the already-triangular back-substitution-only vs general factor-and-solve distinction; and of [`ksp_solve`](./ksp_solve.md) on the broader solve-a-system axis (dense-direct-coordinate vs sparse-iterative-field). Explicitly **NOT** a general `trsv` (the unanchored sparse-triangular smoother kernel; OQ `trsv` stays open) and **NOT** an [`apply_linop`](./apply_linop.md) variant (it reads `R`'s diagonal/super-diagonal entries). Firm-on-positive-structure: the back-solve loop is read in full in both the GMRES (`palace/linalg/iterative.cpp:652-660`) and the line-for-line identical FGMRES (`:831-840`) arms; every law is a syntactic identity on positive source (back-substitution / `R⁻¹` operator-algebra facts), so the absent dedicated running-QR test does not gate them (the `lu_solve` / `apply_linop` precedent). One load-bearing non-law: the descending column-oriented back-substitution reduction order pins a finite-precision path (composes with the L2 running-QR rotation-stream non-associativity). Resolves OQ `ls-update-column-l1-leaf`. The concrete L1 home for the back-solve the long-blocked `trsv` L3-inventory gap was searching for — harvested as its own GMRES-restart-correction primitive, a sibling (not the realisation) of the general `trsv`.
```

(Cohort bullet appended after the `nleps_eigenvalue_correction` bullet — the last entry in the `**Firm (20)**` list. **NOTE for layer-intro-author / finalize: the `**Firm (20)**` header count must increment 20→21 — this dispatch deliberately does NOT edit the count motif per its scope; only the dep-map row + cohort bullet are emitted here.** The `nleps_eigenvalue_correction` bullet is reproduced verbatim as the unique anchor.)

```edit:book/src/SUMMARY.md
- [nleps_eigenvalue_correction](./L1/nleps_eigenvalue_correction.md)
- [back_solve](./L1/back_solve.md)
```

(SUMMARY chapter entry appended under the L1 Part, after `nleps_eigenvalue_correction` (SUMMARY.md:84) and before the `# L1 > L0 — Lowering` Part header (SUMMARY.md:86). The integrator wires this.)

## Operator content

The full firm operator body is authored inside the `new:book/src/L1/back_solve.md`
proposed-changes block above. Summary of its shape:

- **Slug + one-line**: `back_solve` — the GMRES/FGMRES restart-correction
  back-solve `y = back_solve(R, s)` over the running-QR upper-triangular R-factor.
- **Signature** (Haskell `::` form, bunsen shape contract):
  `back_solve :: (R: UpperTri[j+1, j+1], s: Tensor[j+1]) -> Tensor[j+1]`,
  `back_solve(R, s) = the unique y with R·y = s`. Named axes pinned: `R`
  dense-materialized square upper-triangular `(j+1)×(j+1)` (small coordinate
  dimension, NOT field dimension `N`); `s` rotated RHS leading block; result the LS
  minimiser `y`.
- **Semantics**: back-substitution finishing the running-QR least-squares solve;
  the L0 in-place `s[0..j]` overwrite via column-major stride pointer; two
  load-bearing points (upper-triangular + non-singular contract; descending
  column-oriented reduction order as load-bearing finite-precision structure).
- **Algebraic laws** (only those that hold): solve-inverts-apply (defining),
  RHS-linearity, reciprocal coefficient-scaling, back-substitution correctness,
  empty/single-column boundary, basis-lift independence. Non-laws stated explicitly:
  reduction-order independence (does NOT hold — load-bearing), coefficient linearity
  (does NOT hold), definedness without non-singularity (boundary), general-`trsv`
  membership (does NOT hold — it is NOT the general `trsv`).
- **Dependencies**: (leaf). Small-dense-triangular sibling of `lu_solve`; sibling of
  `ksp_solve` on the solve-a-system axis. NOT `apply_linop`, NOT `ksp_solve`, NOT a
  general `trsv`. The terminal `back_solve` atom the L2 `incremental-least-squares`
  composition depends on; its output `y` is lifted by `linear_combination`.
- **Status**: `firm` (firm-on-positive-structure; no-dedicated-test caveat
  non-gating, the `lu_solve`/`apply_linop` precedent).
- **Evidence**: GMRES back-solve `iterative.cpp:652-660` + FGMRES `:831-840` (every
  load-bearing line self-verified via citecheck `--anchor` against on-disk
  `reference/palace/`), the register element-type split `iterative.hpp:193-194`, and
  the parent L2 + concept cross-references.

## Supporting evidence

- **L0 source (self-verified via `tools/citecheck/citecheck.py --batch` against
  on-disk `reference/palace/`)**: all 15 load-bearing pinpoint citations confirmed
  on-disk (`612, 631, 642, 644, 652, 653, 655, 656, 657, 659, 666, 831, 835, 838, 843`
  in `iterative.cpp`; `193, 194` in `iterative.hpp`), 0 failing. The GMRES back-solve
  is `iterative.cpp:652-660`: comment `:652`, descending sweep `:653`, column stride
  `Hi = H.data() + i*(max_dim+1)` `:655`, diagonal division `s[i] /= Hi[i]` `:656`,
  inner loop `:657`, super-diagonal subtraction `s[k] -= Hi[k]*s[i]` `:659`. The
  FGMRES twin is `:831-840` (comment `:831`, division `:835`, subtraction `:838`) —
  line-for-line identical (law 6). Note: cycle-026 dispatch-2 found a +1 codemap
  brace-boundary drift in this exact region; this dispatch read via the codemap then
  re-confirmed every citation on-disk — the codemap and on-disk agreed for the
  back-solve interior lines (`:656`/`:659`), and the `// Reconstruct` comment is at
  `:652` (GMRES) / `:831` (FGMRES) as confirmed on-disk.
- **Parent L2 entry** `book/src/L2/incremental-least-squares.md` (firm cycle-026):
  this leaf is its terminal `back_solve` projection (signature `:81-83`); the
  running-QR stream that triangularises the
  R-factor `R` this leaf consumes; the rotation-stream non-associativity non-law
  (`:278-285`) that this leaf's reduction-order non-law composes with. (The `:412`
  slug `ls_update_column(K,j,h_new)→K'` and `concepts/incremental-least-squares.md:14`
  name the DISTINCT per-column streaming update step, not this terminal back-solve.)
- **Concept page** `book/src/concepts/givens.md`: names the
  `back_solve` step "via `trsv`" (`:29`); this leaf is that `back_solve` (harvested as
  its own primitive, distinct from the general `trsv`).
- **Sibling template** `book/src/L1/lu_solve.md` (firm cycle-022): the small-dense
  direct-solve structural template and the firm-on-positive-structure /
  no-dedicated-test precedent the Status section leans on.

## Open questions / caveats

- **OQ `ls-update-column-l1-leaf` — RESOLVED by this firm entry.** The back-solve now
  has a firm, positively-anchored L1 home. The L2 entry's plain-text forward-references
  (`L2/incremental-least-squares.md:308` "an L1 `trsv` leaf is the natural lowering
  target, forthcoming"; `:412` "the L1 leaf `ls_update_column`") now resolve to a real
  file. *Action for meta-phase:* migrate the OQ to the Closed index with answer-link
  `book/src/L1/back_solve.md`. (If no discrete `ls-update-column-l1-leaf` entry
  exists in the ledger yet — it is referenced in the dispatch but not found as a
  standalone entry — record it as resolved-on-arrival.)
- **`trsv` L1-localization / L3-inventory gap — RELATED, NOT closed.** This leaf is
  the *GMRES-restart-correction* back-solve, a **sibling** of the still-unanchored
  general `trsv` (the sparse-triangular Gauss-Seidel / ILU smoother kernel acting on
  the length-`N` field), **not** the general `trsv` itself. The `trsv` gap
  (`scaffolding/open-questions.md:24,:448`) stays open — a general
  sparse-triangular solve has no positive L0 anchor (likely an obstruction-theme
  target). Recorded explicitly as a non-law ("general-`trsv` membership") so the `trsv`
  gap is not falsely treated as closed by this firm entry. *Note for cycle-planner:*
  the `trsv` L3-inventory item remains BLOCKED at L1-localization; `back_solve`
  does **not** discharge it.
- **L1 firm count 20→21 (NOT edited here).** The `book/src/L1/index.md` §"Vocabulary
  cohort" `**Firm (20)**` header count must increment to `**Firm (21)**` with this
  landing. Per dispatch scope this report deliberately does **NOT** edit the count
  motif — only the dep-map row + the cohort prose bullet are emitted. *Flag for
  layer-intro-author / integrator-finalize:* bump the `**Firm (20)**` → `**Firm (21)**`
  header (and the §"Vocabulary cohort" lead sentence enumerating the firm motifs, if it
  individually lists the 21st). This is the same count-motif-handoff convention the
  prior NEP-cohort harvests used.
- **L2>L1 lowering theme (cycle-027 dispatch 5, concurrent) — this is its landing
  target.** The forthcoming `L2-L1/incremental-least-squares-composition-lowering`
  theme forward-references this leaf for the back-solve sub-step. It will narrate how
  the abstract `R·y = s` back-solve lowers into the in-place `s[0..j]` overwrite +
  column-major stride access at L0 (`iterative.cpp:652-660`), and which finite-precision
  reduction order the lowered call pins (the load-bearing reduction-order non-law). No
  cross-edit needed here — the forward-reference resolves once both land.
- **L1>L0 dedicated mutation-rotation theme (not authored, not this dispatch).** The
  per-leaf L1>L0 lowering of `back_solve` itself (the in-place RHS overwrite +
  flat column-major Hessenberg stride) is covered by the L2>L1 composition-lowering
  theme's back-solve sub-step rather than a standalone `back-solve-mutation-rotation`
  theme — flagged for the abstractor/planner if a standalone leaf-level L1>L0 theme is
  later wanted (low priority; the composition-lowering theme subsumes it).
- **`concepts/givens.md:29` says "via `trsv`".** That concept page describes the
  `back_solve` as "via `trsv`" (`concepts/incremental-least-squares.md` does NOT
  mention `trsv` — it frames the residual as a free byproduct with no explicit `y`
  solve, `:9`/`:14`) — now
  that the back-solve has its own firm L1 leaf (`back_solve`), distinct from the
  general `trsv`, that prose reference could be tightened to name `back_solve`
  (the specific GMRES-restart-correction back-solve) rather than the unanchored general
  `trsv`. Concept-page edits are out of harvester scope. *Trigger:* a future
  lifter / layer-intro-author / concept-page re-cite dispatch; low fan-out, mechanical
  prose tightening. (Pairs with the existing `givens-concept-page-gmres-md-to-iterative-cpp-recite`
  plan candidate touching the same `givens.md` region.)
