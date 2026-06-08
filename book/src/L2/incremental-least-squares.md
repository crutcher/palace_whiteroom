# incremental-least-squares

The L2 first-class composition naming the GMRES / FGMRES **running-QR /
Givens-rotation stream**: the incremental triangularisation of the growing
upper-Hessenberg least-squares problem `min ‖β·e₁ − H̄·y‖₂`, threaded across the
Arnoldi iteration so that each newly-orthogonalised Hessenberg column is reduced
to upper-triangular form by replaying the stored plane rotations and generating
one new rotation — with the least-squares residual norm `β = |s[j+1]|` exposed as
a **free byproduct** of the rotation applied to the right-hand side, never
computed by an explicit residual evaluation. At the close of a restart cycle the
triangular system is back-solved for the coordinate vector `y`, and the
externally-visible iterate correction is `V·y` (GMRES) / `Z·y` (FGMRES). This is
the second **named-composition** motif (sibling to
[`orthogonalize`](./orthogonalize.md)), the composition GMRES / FGMRES fold into
their per-restart-cycle correction machinery and the one
[`ksp_solve`](./ksp_solve.md) §Semantics `materialise_iterate` consumes to fold the
last partial restart cycle's correction into the running iterate `s.x`.

## Context

At L1 this is a single opaque operation (`ls_update_column`, per the
[`concepts/incremental-least-squares`](../concepts/incremental-least-squares.md)
contract): a `Krylov` bundle carrying the rotation registers `(cs, sn)`, the RHS
`s`, and the LS-residual proxy `β` advances by one column. L2 is the
fusion-rotation layer (`book/src/L2/index.md`): "Batched specialized BLAS calls
are written as compositions of base primitives… kernel fusion across multiple
algebraic operations is unfolded into composition." The running-QR is exactly such
a specialization — Palace does not materialise `H̄`, factor it, and solve; it fuses
the QR factorisation *into the column-arrival loop* and reads the residual off the
rotated RHS. L2 de-fuses that into the canonical composition
`replay-rotations ▷ generate-rotation ▷ apply-to-rhs ▷ back-solve`, **keeping the
replay-then-generate ordering as the disclosed load-bearing structure** because it
is the entire reason the residual-norm estimate is exact and cheap (the running-QR
is a load-bearing numerical trick per `CLAUDE.md` §Optimization tricks, not a
transparent fusion).

This entry is a **named composition**, the structural sibling of the firm
[`orthogonalize`](./orthogonalize.md) (the Gram-Schmidt `project ▷ subtract`
composition) and the firm [`linear_combination`](./linear_combination.md)
(the BLAS-1 arity-family fold): name the composition, list its variant axes, state
the laws that hold *at the composition level*, do not re-derive the laws of the
constituent L1 primitives.

**Relation to `krylov-step` (the borderline, resolved).** This composition is **not**
a [`krylov-step`](./krylov-step.md) instance. `krylov-step` is the iterative-method
step kernel that builds and orthogonalises a new length-`N` basis vector;
`incremental-least-squares` operates on the **small-dense** `(j+2)×(j+1)` Hessenberg
matrix and the length-`(j+2)` RHS — its work is `O(j)` scalar rotations per step,
independent of the field dimension `N`. It is *folded by* the GMRES step (the
column produced by `orthogonalize` + the `Norml2` sub-diagonal is the input column
`H̄[:,j]`), but it is a distinct composition consumed within the step, not a step
variant. The decision closes the `gmres-givens-stream-as-step-kernel-borderline` OQ:
the Givens-stream is a separate named composition, not a `krylov-step` axis.

The composition is **value-producing and incremental-stateful** (it threads the
rotation registers `(cs, sn)` and the rotated RHS `s` across columns), but it is
**not iteration-structural** in the L4 `iterate_while` sense — there is no
convergence predicate inside it; it produces one updated triangular factor + one
new residual norm per column, and the convergence test reads `β` from the result.
The *outer* Arnoldi loop that calls it column-by-column is the iteration-structural
part, which lives in [`krylov-step`](./krylov-step.md) + L4's driver, not here. The
LS residual exposure `β = |s[j+1]|` is the side-output that the
[`ksp_solve`](./ksp_solve.md) convergence predicate consumes.

A cross-cutting prose treatment lives at
[`concepts/incremental-least-squares`](../concepts/incremental-least-squares.md);
the scalar Givens kernel pair is at [`concepts/givens`](../concepts/givens.md)
(generate + apply), with [`concepts/givens_generate`](../concepts/givens_generate.md)
and [`concepts/givens_apply`](../concepts/givens_apply.md) the per-kernel pages.
Where this entry and the concept pages disagree, the L0 source ranges cited in
§Evidence are authoritative.

## Signature

    incremental_least_squares :: (op: LsqOp, st: LsqState, h_new: HessCol) -> { state: LsqState', beta: RealScalar }

with the restart-cycle back-solve as a terminal projection:

    back_solve :: LsqState' -> { y: Coords[j+1], correction_basis: Basis[N, j+1] }

Shape contract (bunsen-style; named axes):

- `op` — `LsqOp` — the closed-over least-squares-update surface, bound once at
  solve setup. A record:
  - `op.variant : GivensKind ∈ {real, complex}` — selects the real vs complex
    Givens kernel pair (the rotation registers `cs` are always real; `sn` and the
    RHS `s` are `ScalarType`, i.e. complex in the complex case — the L0 register
    declaration `iterative.hpp:193-194`). Inspected once at instantiation, never
    re-branched per column.
  - `op.basis_kind : BasisKind ∈ {V, Z}` — selects which basis the back-solve
    reconstructs the correction against: the Arnoldi basis `V` (GMRES, and the
    left-preconditioned / unpreconditioned GMRES path) or the flexible
    preconditioned basis `Z` (FGMRES, and the right-preconditioned GMRES path,
    which post-applies the preconditioner to the `V`-correction). This is the
    composition's only structural axis.
- `st` — `LsqState` — the incremental factorisation state threaded across columns.
  A record:
  - `st.H : UpperHess[j+2, j+1]` — the column-major Hessenberg factor accumulated so
    far (the leading `j+1` columns, each of length up to `j+2`); columns
    `0..j-1` already triangularised.
  - `st.cs : RealScalar[j]`, `st.sn : ScalarType[j]` — the stored plane-rotation
    registers for columns `0..j-1` (the `(cosine, sine)` pairs; `cs` real, `sn`
    `ScalarType`), append-only and indexed by step.
  - `st.s : ScalarType[j+2]` — the rotated right-hand side, initialised `s[0] = β₀`
    (the initial residual norm), zero elsewhere; entry `s[j+1]` carries the running
    LS residual.
- `h_new` — `HessCol` ≡ `ScalarType[j+2]` — read-then-consumed; the freshly-arrived
  Hessenberg column: entries `0..j` are the Arnoldi coefficients
  `⟨w, V[k]⟩` (the [`orthogonalize`](./orthogonalize.md) `coeffs`) and entry `j+1`
  is the sub-diagonal `‖w‖` (`Norml2` of the orthogonal residual).
- result — `{ state: LsqState', beta: RealScalar }`:
  - `state : LsqState'` — `st` advanced: `h_new` triangularised into `H[:,j]` (its
    sub-diagonal annihilated), one new rotation `(cs[j], sn[j])` recorded, the RHS
    `s` advanced by that rotation.
  - `beta : RealScalar` — `|state.s[j+1]|`, the LS residual norm at step `j`, exposed
    as a free side-output (no explicit residual evaluation). This is the
    [`ksp_solve`](./ksp_solve.md) convergence predicate's input.

The restart-cycle terminal `back_solve` consumes the final `LsqState'` (over the
`j+1` accumulated columns) and produces:

- `y : Coords[j+1]` — the least-squares minimiser of `‖β·e₁ − H̄·y‖₂`, obtained by
  back-substitution against the triangularised `H` (`H` is now upper-triangular in
  its leading `(j+1)×(j+1)` block; the back-substitution overwrites `s[0..j]` with
  `y`).
- `correction_basis : Basis[N, j+1]` — `op.basis_kind` selects `V` or `Z`; the
  externally-visible iterate correction is `correction_basis · y = Σ_k y[k]·basis[k]`.

The empty-stream case (`j = -1`, no columns yet) is the identity: `back_solve` over
an empty factorisation yields `y = []` and the zero correction. The first column
(`j = 0`) skips the replay sub-step (no prior rotations) and runs only
generate + apply.

## Semantics

`incremental_least_squares` maintains a running QR factorisation of the
upper-Hessenberg matrix `H̄_j` produced column-by-column by Arnoldi, so that the
least-squares problem `min_y ‖β·e₁ − H̄_j·y‖₂` is solved incrementally rather than
re-factorised at every step. The canonical L2 composition per arriving column is:

    incremental_least_squares op st h_new =
      let h1 = replay op.variant st.cs st.sn st.H.ncols h_new   -- apply stored rotations 0..j-1 to the new column
      let (cs_j, sn_j) = generate op.variant h1[j] h1[j+1]      -- rotation annihilating the sub-diagonal
      let h2 = apply op.variant cs_j sn_j h1                    -- triangularise: h2[j+1] := 0
      let s' = apply_rhs op.variant cs_j sn_j st.s              -- propagate to the RHS: s'[j+1] carries the residual
      let st' = { H = st.H ⊕ h2, cs = st.cs ++ [cs_j], sn = st.sn ++ [sn_j], s = s' }
      in { state = st', beta = |s'[j+1]| }

The four sub-steps, in order:

1. **Replay** (`replay`). For `k = 0..j-1`, apply the stored plane rotation
   `(cs[k], sn[k])` to the pair `(h_new[k], h_new[k+1])`. This brings the new column
   into the frame established by the prior columns' triangularisation. Source:
   the GMRES loop `for (int k = 0; k < j; k++) ApplyPlaneRotation(Hj[k], Hj[k+1],
   cs[k], sn[k]);` (`iterative.cpp:634-636`). **The replay-before-generate ordering
   is load-bearing** (see Algebraic laws law 2): a stored rotation `k` must touch the
   new column before the new rotation `j` is generated, or the factorisation is wrong.

2. **Generate** (`generate`). Compute the new rotation `(cs[j], sn[j])` that
   annihilates the sub-diagonal entry `h_new[j+1]` against the diagonal `h_new[j]`:
   `GeneratePlaneRotation(Hj[j], Hj[j+1], cs[j], sn[j])` (`iterative.cpp:638`). The
   real kernel returns `cs = |dx|/r`, `sn = dy/copysign(r,dx)` with LAPACK-style
   overflow/underflow scaling (`iterative.cpp:73-108`); the complex kernel returns
   real `cs` with `cs² + |sn|² = 1` (`iterative.cpp:112-118`).

3. **Apply** (`apply`). Apply the new rotation to its own pair, zeroing the
   sub-diagonal: `ApplyPlaneRotation(Hj[j], Hj[j+1], cs[j], sn[j])`
   (`iterative.cpp:639`). After this, column `j` is upper-triangular: `Hj[j+1] = 0`.
   The 2-vector update is `(dx', dy') = (cs·dx + sn·dy, −s̄n·dx + cs·dy)`
   (`iterative.cpp:227-241`; `s̄n = conj(sn)` in the complex case).

4. **Apply-to-RHS** (`apply_rhs`). Apply the *same* new rotation to the RHS pair
   `(s[j], s[j+1])`: `ApplyPlaneRotation(s[j], s[j+1], cs[j], sn[j])`
   (`iterative.cpp:640`). Because `s` started as `β·e₁` and each rotation is unitary,
   `|s[j+1]|` after this step is exactly the residual norm of the LS problem over the
   `j+1` columns: `β = std::abs(s[j+1])` (`iterative.cpp:642`). The convergence test
   `converged = (beta < eps)` (`iterative.cpp:644`) reads it with **no explicit
   residual evaluation** — this exposure is the entire point of the running-QR.

At restart-cycle close (convergence, restart boundary, or max-iterations), the
terminal **back-solve** reconstructs the solution correction. The triangular system
`H·y = s` (with `H` now upper-triangular in its leading block) is back-substituted
in place over `s[0..j]`:

    for (int i = j; i >= 0; i--) {                 -- iterative.cpp:652-660 (GMRES) / :831-840 (FGMRES)
      s[i] /= H[i][i];                             -- iterative.cpp:656 / :835
      for (int k = i-1; k >= 0; k--)
        s[k] -= H[i][k] * s[i];                    -- iterative.cpp:659 / :838
    }

leaving `y = s[0..j]`. The externally-visible iterate correction is then
`Σ_k y[k]·basis[k]`, with the basis selected by `op.basis_kind`:

- **GMRES, unpreconditioned / left-preconditioned** (`op.basis_kind = V`):
  `x += Σ_k s[k]·V[k]` (`iterative.cpp:666`, the `!B || pc_side == LEFT` branch).
- **GMRES, right-preconditioned**: form the `V`-correction `r = Σ_k s[k]·V[k]`
  (`iterative.cpp:674`), then post-apply the preconditioner `B·r` and add
  (`ApplyB(B, r, V[0]); x += V[0]`, `iterative.cpp:676-677`). The back-solve is
  identical; only the correction post-processing differs.
- **FGMRES** (`op.basis_kind = Z`): `x += Σ_k s[k]·Z[k]` (`iterative.cpp:843`),
  against the flexible-preconditioner basis `Z` (each `Z[k]` is the
  per-iteration-preconditioned vector). The running-QR stream is **identical** to
  GMRES's (`iterative.cpp:812-821` matches `:632-642` line-for-line); the only
  difference is the back-solve reconstructs against `Z` rather than `V`. This is the
  `op.basis_kind` axis.

The L0 register storage confirms the element-type split: `H`, `s`, `sn` are
`ScalarType` (complex in the complex case) and `cs` is always `RealType`
(`iterative.hpp:193-194`), matching the complex Givens kernel's "cs is real" contract
(`iterative.cpp:118`).

## Algebraic laws

`incremental_least_squares` is a **named composition** (a per-column
`replay ▷ generate ▷ apply ▷ apply_rhs` pipeline, with a terminal back-solve), not a
binary algebra. The laws are stated at the **composition level** — facts about the
factorisation state and the residual byproduct — and the scalar Givens kernels' own
properties (unitarity, the `cs² + |sn|² = 1` identity) are inherited, not re-derived.
"Exact" means exact arithmetic.

1. **Residual exposure (the defining contract).** After the per-column update,
   `beta = |st'.s[j+1]| = min_y ‖β₀·e₁ − H̄_j·y‖₂` exactly — the LS residual norm of
   the problem over the `j+1` accumulated columns equals the magnitude of the rotated
   RHS tail. This holds because every rotation is unitary, so applying the rotation
   stream to `β₀·e₁` preserves the 2-norm and concentrates the un-annihilatable
   component in entry `j+1`. This is what lets the convergence test read `β` without
   an explicit residual evaluation (`iterative.cpp:642-644`). It is the composition's
   load-bearing reason to exist.

2. **Replay-before-generate ordering (load-bearing, non-commutative).** The stored
   rotations `0..j-1` must be applied to the new column *before* the new rotation `j`
   is generated and applied (`iterative.cpp:634-639`: the replay loop precedes
   `GeneratePlaneRotation`). The composition is **not** order-invariant in this
   sub-step: generating rotation `j` from an un-replayed column would annihilate
   against the wrong diagonal and produce a non-triangular factor. This is the
   running-QR's structural invariant, the same one the
   [`concepts/givens`](../concepts/givens.md) §Contract states ("a previously-stored
   rotation `k` must be applied to a new column before any newly-generated rotation
   `j > k` touches it").

3. **Norm preservation (unitarity).** Each plane rotation is unitary
   (`cs² + |sn|² = 1`, `iterative.cpp:112-118`), so the full rotation stream `Qⱼ` is
   unitary and `‖β₀·e₁‖₂ = ‖Qⱼ·(β₀·e₁)‖₂ = ‖s‖₂` is preserved column-to-column
   (exact). The residual decomposition `β₀² = ‖s[0..j]‖² + |s[j+1]|²` is the
   composition-level form of the concept page's invariant
   `‖R·y − s‖² + |s[j+1]|² = ‖H̄·y − β·e₁‖²`.

4. **Back-solve correctness.** After triangularisation the leading `(j+1)×(j+1)` block
   of `H` is upper-triangular and non-singular (Arnoldi breakdown excepted), so the
   back-substitution (`iterative.cpp:652-660`) yields the unique `y` minimising
   `‖β₀·e₁ − H̄_j·y‖₂` — the standard QR least-squares solve. The minimiser is
   independent of `op.basis_kind`; only the reconstruction `correction_basis · y`
   differs.

5. **Empty / single-column boundary.** The empty stream (`j = -1`) yields `y = []`
   and the zero correction (back-solve over an empty factor is the identity). The
   first column (`j = 0`) skips the replay sub-step (the `k < j` loop is empty,
   `iterative.cpp:634-636`) and runs only generate + apply + apply_rhs; the residual
   exposure law still holds.

6. **`op.basis_kind` invariance of the factorisation.** Substituting `op.basis_kind`
   (`V` ↔ `Z`) leaves the running-QR stream and laws 1–5 unchanged — the factorisation,
   the rotation registers, the residual byproduct, and the back-solved `y` are
   identical; only the terminal `correction_basis · y` reconstruction reads a
   different basis (`iterative.cpp:666` `V` vs `:843` `Z`). The GMRES and FGMRES
   stream code is line-for-line identical (`:632-642` ≡ `:812-821`). The axis is a
   reconstruction-target substitution, not a structural variant of the LS update.

Laws that explicitly **do NOT** hold:

- **Sub-step commutativity (replay vs generate).** Law 2 — replay and generate do
  **not** commute. This is the algebraic shadow of the running-QR's column-arrival
  ordering and is load-bearing (not a transparent reorder).
- **Rotation-stream associativity / re-factorisation equivalence at the bit level.**
  The incremental running-QR and a from-scratch QR of the assembled `H̄_j` agree in
  exact arithmetic (law 1) but differ at the bit level — the rotation order and the
  LAPACK-style scaling (`iterative.cpp:101-108`) pin a specific finite-precision
  reduction path. This is a **load-bearing numerical trick** (the cheap incremental
  residual estimate is the property bought), preserved as an explicit claim per
  `CLAUDE.md` §Optimization tricks — not erased as a transparent fusion. The exact
  per-lowered-call reduction order is pinned by the forthcoming L2>L1 theme.
- **Convergence-test fold-merge with the kernel.** The residual byproduct `β` is read
  by the [`ksp_solve`](./ksp_solve.md) convergence predicate, but the predicate is
  **not** fusible into this composition — `incremental_least_squares` produces one `β`
  per column and the fold/restart logic lives in `ksp_solve` (the outer driver). The
  composition is the kernel's LS-update half, not the loop.
- **`krylov-step` membership.** This is **not** a [`krylov-step`](./krylov-step.md)
  variant (the borderline OQ, resolved): it works on the `(j+2)×(j+1)` small-dense
  Hessenberg, not the length-`N` field; it is folded *by* the step, not a step axis.

## Dependencies

L2 dependencies (other L2 vocabulary or below):

- L1 leaf it lifts: the `ls_update_column` operation per
  [`concepts/incremental-least-squares`](../concepts/incremental-least-squares.md)
  (the single-column running-QR update; the L1 leaf is forthcoming — this entry is
  the form it is *named as* at L2).
- Scalar kernels the composition's sub-steps compose: the Givens generate/apply pair
  ([`concepts/givens`](../concepts/givens.md), with
  [`givens_generate`](../concepts/givens_generate.md) /
  [`givens_apply`](../concepts/givens_apply.md)) — element-local, no reduction. The
  back-solve sub-step is a small-dense triangular solve (`trsv`-shaped over the
  `(j+1)×(j+1)` block; an L1 `trsv` leaf is the natural lowering target, forthcoming).
- Producer of the input column `h_new`: [`orthogonalize`](./orthogonalize.md) (the
  `coeffs` are the column's `0..j` Arnoldi entries) followed by the caller's `Norml2`
  sub-diagonal (`iterative.cpp:631`). `orthogonalize` and `incremental-least-squares`
  are siblings folded by the same GMRES step: orthogonalize produces the column,
  incremental-least-squares triangularises it.

Concept references (cross-cutting; do not duplicate):

- [`concepts/incremental-least-squares`](../concepts/incremental-least-squares.md) —
  the narrative cross-cut (the role: incremental triangularisation with residual as a
  free byproduct; reuse across GMRES / FGMRES / MINRES / LSQR / LSMR).
- [`concepts/givens`](../concepts/givens.md) — the scalar kernel pair and the
  replay-order contract.

Consumers (the L2/L4 surfaces that fold or call this composition):

- [`krylov-step`](./krylov-step.md) — folds this composition inside the GMRES /
  FGMRES step (the column produced by `orthogonalize` + `Norml2` is fed in; the
  byproduct `β` is the step's residual-norm output). Named by `krylov-step`'s
  §"L2 vs L1 distinction" as a future L2 candidate; this entry is that candidate.
- [`ksp_solve`](./ksp_solve.md) — §Semantics phase-3 `materialise_iterate` folds the
  last partial restart cycle's correction `V·y` / `Z·y` (this composition's back-solve
  output) into the running iterate `s.x` for GMRES/FGMRES; the byproduct `β` is the
  driver's convergence-predicate input.

L2>L1 lowering theme (`L2-L1/incremental-least-squares-composition-lowering`, not yet
authored): narrates how the named L2 composition lowers into the L1 `ls_update_column`
leaf — the per-column replay/generate/apply sub-step sequence, the back-solve `trsv`, and
which L0 finite-precision reduction order each lowered variant pins (the load-bearing
content of the rotation-stream non-associativity non-law).

## Variant axes

Following the [`classify-variant-axis`](../../../skills/classify-variant-axis/SKILL.md)
output contract (per-axis-value: absorption path, load-bearing primitive, state
binding):

- `op.basis_kind` ∈ {`V`, `Z`}: **parametric absorption** (a reconstruction-target
  substitution; the running-QR stream and laws 1–5 are invariant — algebraic-laws
  law 6). The only structural axis.
  - `V`: GMRES Arnoldi basis (unpreconditioned / left-preconditioned; the
    right-preconditioned path post-applies `B` to the `V`-correction). Back-solve
    reconstruction `x += Σ_k s[k]·V[k]` (`iterative.cpp:666`); right-precond variant
    `r = Σ_k s[k]·V[k]; x += B·r` (`iterative.cpp:674-677`).
  - `Z`: FGMRES flexible-preconditioner basis. Back-solve reconstruction
    `x += Σ_k s[k]·Z[k]` (`iterative.cpp:843`). Stream code identical to `V`.
  - State binding: both share the rotation registers `(cs, sn)`, the RHS `s`, and the
    Hessenberg `H`; the basis (`V` or `Z`) is the solver's per-restart workspace,
    bound at the back-solve reconstruction only.

- `op.variant` (Givens kernel) ∈ {`real`, `complex`}: **parametric absorption** (the
  element-type axis; the composition shape and laws are invariant; the conjugation
  lives in the scalar kernel). Real: `cs`, `sn` real; complex: `cs` real, `sn`
  `ScalarType` complex with `s̄n = conj(sn)` in `apply` (`iterative.cpp:227-241`). The
  L0 register declaration pins this: `H`, `s`, `sn` are `ScalarType`, `cs` is
  `RealType` (`iterative.hpp:193-194`).
  - State binding: the register element types are fixed at solver instantiation; no
    per-column branching.

There is **no** Givens-variant axis on the reduction-ordering — the
replay-then-generate sequence is fixed and load-bearing (algebraic-laws law 2), not a
selectable strategy. (Householder / two-sided reductions are scoped out: Palace's L0
GMRES uses exactly the plane-rotation stream, `iterative.cpp:632-642`; no Householder
path exists, so it is out of scope per the unimplemented-component policy.)

## Status

`firm` — a `replay ▷ generate ▷ apply ▷ apply_rhs` pipeline over the firm scalar Givens
kernel pair with a terminal back-solve, read in full in both the GMRES
(`iterative.cpp:632-680`) and FGMRES (`:812-844`) arms. Every algebraic law is a
composition-level fact or a standard running-QR invariant; firm-on-positive-structure
(syntactic / unitarity identities on fully-read positive source, no dedicated unit test
required). The variant axes are closed at two parametric axes (`op.basis_kind` `V`/`Z` +
`op.variant` real/complex). The `gmres-givens-stream-as-step-kernel-borderline` OQ is
resolved in the negative: a distinct named composition, not a `krylov-step` axis.

## L2 vs L1 distinction

- **L1**: the single opaque leaf `ls_update_column(K, j, h_new) → K'` (per
  [`concepts/incremental-least-squares`](../concepts/incremental-least-squares.md)),
  advancing the `Krylov` bundle by one column — the running-QR sub-steps and the
  residual-exposure mechanism are hidden as a single "incremental triangularisation
  with residual side-output" leaf.
- **L2**: the *named composition*
  `incremental_least_squares op st h_new → { state, beta }` (+ terminal `back_solve`)
  — the `replay ▷ generate ▷ apply ▷ apply_rhs` pipeline whose **sub-step sequence and
  replay-before-generate ordering are the load-bearing structure made visible**. L2's
  role is not to add a primitive but to name the canonical composition and surface its
  composition-level laws: the residual-exposure-by-unitarity contract, the
  replay-ordering non-commutativity, the norm-preservation decomposition, and the
  back-solve become first-class L2 content, where at L1 they were a leaf and a side
  effect. This is the surface `krylov-step` folds and `ksp_solve` consumes.

## Evidence

- `palace/linalg/iterative.cpp:73-108` — `GeneratePlaneRotation` (real): the
  LAPACK-style scaled rotation generator (`cs = |dx|/d`, `sn = dy/copysign(d,dx)`,
  with overflow/underflow scaling at `:101-108`). The `generate` sub-step's real
  kernel.
- `palace/linalg/iterative.cpp:112-118` — `GeneratePlaneRotation` (complex): real
  `cs`, complex `sn`, with the in-comment contract "cs is real and cs² + |sn|² = 1"
  (`:118`). The complex `generate` kernel + the unitarity identity underwriting laws
  1/3.
- `palace/linalg/iterative.cpp:227-241` — `ApplyPlaneRotation` (real `:227` + complex
  `:235`): the in-place 2-vector update `(dx', dy') = (cs·dx + sn·dy, −s̄n·dx + cs·dy)`
  (`s̄n = conj(sn)` complex). The `apply` / `apply_rhs` sub-step kernel.
- `palace/linalg/iterative.cpp:612` — `s[0] = beta`: the RHS initialisation `s = β₀·e₁`
  for the GMRES restart cycle (the running-QR's right-hand side seed).
- `palace/linalg/iterative.cpp:631` — `Hj[j + 1] = linalg::Norml2(comm, w)`: the
  sub-diagonal `‖residual‖` entry of the arriving column `h_new[j+1]` (the
  `orthogonalize` coeffs occupy `0..j`).
- `palace/linalg/iterative.cpp:634-636` — GMRES **replay** sub-step:
  `for (int k = 0; k < j; k++) ApplyPlaneRotation(Hj[k], Hj[k+1], cs[k], sn[k]);` —
  the stored-rotation replay on the new column (law 2 ordering).
- `palace/linalg/iterative.cpp:638` — GMRES **generate**:
  `GeneratePlaneRotation(Hj[j], Hj[j+1], cs[j], sn[j]);` — the new rotation.
- `palace/linalg/iterative.cpp:639` — GMRES **apply** (triangularise own column):
  `ApplyPlaneRotation(Hj[j], Hj[j+1], cs[j], sn[j]);`.
- `palace/linalg/iterative.cpp:640` — GMRES **apply_rhs**:
  `ApplyPlaneRotation(s[j], s[j+1], cs[j], sn[j]);` — propagates the new rotation to
  the RHS, concentrating the residual in `s[j+1]`.
- `palace/linalg/iterative.cpp:642` — `beta = std::abs(s[j + 1]);` — the residual
  exposure (law 1: the free byproduct).
- `palace/linalg/iterative.cpp:644` — `converged = (beta < eps);` — the convergence
  test reads `β` with no explicit residual evaluation.
- `palace/linalg/iterative.cpp:652-660` — GMRES **back-solve** ("Reconstruct the
  solution"): the in-place back-substitution `s[i] /= H[i][i]` (`:656`) /
  `s[k] -= H[i][k]·s[i]` (`:659`) yielding `y = s[0..j]` (law 4).
- `palace/linalg/iterative.cpp:666` — GMRES correction (left/unpreconditioned):
  `x.Add(s[k], V[k]);` — `x += Σ_k y[k]·V[k]` (the `op.basis_kind = V` reconstruction).
 
- `palace/linalg/iterative.cpp:674-677` — GMRES correction (right-preconditioned):
  `r.Add(s[k], V[k])` (`:674`) then `ApplyB(B, r, V[0]); x += V[0]` (`:676-677`) — the
  preconditioner post-applied to the `V`-correction; back-solve identical.
- `palace/linalg/iterative.cpp:812-821` — FGMRES running-QR stream: replay `:813-815`,
  generate `:817`, apply `:818`, apply_rhs `:819`, `beta` `:821` — **line-for-line
  identical** to the GMRES stream (law 6: `op.basis_kind`-invariant).
- `palace/linalg/iterative.cpp:831-844` — FGMRES back-solve + correction:
  back-substitution `:831-840` (identical to GMRES) then `x.Add(s[k], Z[k])` (`:843`) —
  the `op.basis_kind = Z` reconstruction against the flexible-preconditioner basis.
 
- `palace/linalg/iterative.hpp:193-194` — `GmresSolver` rotation-register declarations:
  `mutable std::vector<ScalarType> s, sn;` (`:193`) / `mutable std::vector<RealType>
  cs;` (`:194`) — the element-type split (`s`, `sn` `ScalarType`; `cs` always
  `RealType`) underwriting the `op.variant` real/complex axis.
- `book/src/concepts/incremental-least-squares.md` — the cross-cutting concept page
  (the role: incremental triangularisation with residual byproduct; the L1
  `ls_update_column` contract; cross-method reuse).
- `book/src/concepts/givens.md` — the scalar kernel pair + the replay-order contract
  (`:25`, `:33-34` Palace mapping); `book/src/concepts/givens_generate.md` /
  `book/src/concepts/givens_apply.md` per-kernel pages.
- `book/src/L2/orthogonalize.md` — the sibling firm L2 named composition (the
  structural template; produces the input column `h_new[0..j]`).
- `book/src/L2/krylov-step.md` — the consumer folding this composition; §"L2 vs L1
  distinction" (`:132`) forecasts this exact entry.
- `book/src/L2/ksp_solve.md` — the outer-driver consumer; §Semantics phase-3
  `materialise_iterate` (`:63`, `:83`) folds this composition's restart-cycle
  correction `K.V · K.y`.
