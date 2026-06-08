# incremental-least-squares-composition-lowering

The fan-down rotation for the GMRES / FGMRES running-QR / Givens-rotation stream. Lowers the
firm L2 named composition [`incremental_least_squares`](../L2/incremental_least_squares.md) — the
per-column `replay ▷ generate ▷ apply ▷ apply_rhs` pipeline with a terminal back-solve, threaded
across the Arnoldi iteration so the growing upper-Hessenberg least-squares problem
`min ‖β·e₁ − H̄·y‖₂` is triangularised incrementally and the residual norm `β = |s[j+1]|` falls out
as a free unitary byproduct — into its L1 leaves. Narrated forward (L2 → L1): the one named L2
composition **fans down** into the single L1 column-streaming leaf `ls_update_column` (the per-column
running-QR update, opaque face) — equivalently, into the explicit scalar Givens sub-step sequence
(de-fused face) — plus a terminal back-solve = small-dense triangular solve
([`back_solve`](../L1/back_solve.md)) ▷ basis reconstruction
([`linear_combination`](../L2/linear_combination.md)). This theme records which finite-precision
reduction path each lowered variant pins (the **load-bearing rotation-stream non-associativity** the
L2 entry deferred to "the forthcoming L2>L1 theme",
[`incremental_least_squares`](../L2/incremental_least_squares.md) §Algebraic-laws non-law
(`:278-285`) / §Dependencies) and the **replay-before-generate ordering** that is the running-QR's
structural invariant. Sibling to
[`orthogonalize-composition-lowering`](./orthogonalize-composition-lowering.md) (the other
named-composition `project ▷ subtract` fan-down): each is a
one-L2-composition-fans-into-L1-vocabulary theme.

## Slug

`incremental-least-squares-composition-lowering`

## L2 form (LHS)

The L2 form is the named running-QR composition over the incremental factorisation state `st` and a
freshly-arrived Hessenberg column `h_new`, parameterised by the basis-kind and Givens-element-type
axes ([`incremental_least_squares`](../L2/incremental_least_squares.md) §Signature, §Semantics):

    incremental_least_squares :: (op: LsqOp, st: LsqState, h_new: HessCol) -> { state: LsqState', beta: RealScalar }

    incremental_least_squares op st h_new =
      let h1       = replay    op.variant st.cs st.sn st.H.ncols h_new   -- apply stored rotations 0..j-1 to the new column
      let (cs_j, sn_j) = generate op.variant h1[j] h1[j+1]               -- rotation annihilating the sub-diagonal
      let h2       = apply     op.variant cs_j sn_j h1                   -- triangularise: h2[j+1] := 0
      let s'       = apply_rhs op.variant cs_j sn_j st.s                 -- propagate to RHS: s'[j+1] carries the residual
      let st'      = { H = st.H ⊕ h2, cs = st.cs ++ [cs_j], sn = st.sn ++ [sn_j], s = s' }
      in { state = st', beta = |s'[j+1]| }

with the restart-cycle terminal back-solve as a separate projection:

    back_solve :: LsqState' -> { y: Coords[j+1], correction_basis: Basis[N, j+1] }

where `op.variant : GivensKind ∈ {real, complex}` selects the scalar kernel pair (inspected once at
instantiation) and `op.basis_kind : BasisKind ∈ {V, Z}` selects which basis the back-solve
reconstructs the correction against (GMRES `V` / FGMRES `Z`). The composition is value-producing and
**incremental-stateful** (it threads the rotation registers `(cs, sn)`, the rotated RHS `s`, and the
Hessenberg `H` across columns) but **not iteration-structural** — there is no convergence predicate
inside it; it produces one updated triangular factor + one new residual norm per column (L2 entry
§Context). At L2 the **four-sub-step sequence and the replay-before-generate ordering** are the
load-bearing structure made visible (L2 entry §"L2 vs L1 distinction"); the residual exposure
`β = |s[j+1]|` is the side-output the [`ksp_solve`](../L2/ksp_solve.md) convergence predicate consumes
(L2 entry law 1). The value the composition computes is `op.basis_kind`-invariant and
`op.variant`-shape-invariant in exact arithmetic (L2 entry law 6; the conjugation lives in the
scalar kernel).

## L1 form (RHS)

The L1 form has two co-extensive faces of the same value (as the sibling
[`orthogonalize-composition-lowering`](./orthogonalize-composition-lowering.md) §"L1 form (RHS)").
**Which face the lowering targets is a resolution choice, not a value choice** — they advance the
factorisation state identically.

### Face 1 — the opaque single-column leaf (the fused face)

The L1 column-streaming leaf [`ls_update_column`](../L1/ls_update_column.md) (the per-column running-QR update; per the
[`concepts/incremental_least_squares`](../concepts/incremental_least_squares.md) contract `:14`),
mirroring Palace's per-column loop body one-to-one:

    ls_update_column :: (K: Krylov, j: Int, h_new: HessCol) -> Krylov'
      -- K' = K with: h_new triangularised into H[:,j]; one new rotation (cs[j], sn[j]) recorded;
      --              the RHS s advanced by that rotation; K'.beta = |s[j+1]| the LS residual.

At L1 the per-column running-QR sub-steps (replay / generate / apply / apply_rhs) and the
residual-exposure mechanism are **hidden inside the leaf** as a single "incremental triangularisation
with residual side-output" operation, exactly as the concept page's "What is *hidden* at L1" list
states ([`concepts/incremental_least_squares`](../concepts/incremental_least_squares.md):22-27). The
L2 record `{ state, beta }` is the same value as the L1 leaf's advanced `Krylov'` bundle (its
`K'.beta` is the L2 `beta`; its rotation registers + RHS + Hessenberg are the L2 `state`). The leaf's
own lowering onto the L0 in-place free functions — the four `*PlaneRotation` calls at
`iterative.cpp:634-642` writing `Hj`, `cs`, `sn`, `s` in place — is the **L1>L0** concern of the firm
[`ls_update_column-mutation-rotation`](../L1-L0/ls-update-column-mutation-rotation.md) theme;
**this theme stops at the L1 leaf and does not re-derive that L0 in-place step** (the
same boundary the sibling draws at the L1 `orthogonalize` leaf). The
[`ls_update_column`](../L1/ls_update_column.md) column-streaming leaf is **firm**
(`book/src/L1/ls_update_column.md`, firm-on-positive-structure per the running-QR loop body
`iterative.cpp:634-640` / `:813-819`); the co-extensive **Face 2** below carries the same value via the
de-fused scalar Givens kernel pair, so either face resolves the L1 RHS of this fan-down.

### Face 2 — the de-fused scalar Givens sub-step sequence (the spelled-out face)

The four per-column sub-steps spelled out in the firm scalar Givens kernel pair
([`concepts/givens_generate`](../concepts/givens_generate.md) /
[`concepts/givens_apply`](../concepts/givens_apply.md);
[`concepts/plane-rotation-stream`](../concepts/plane-rotation-stream.md) §Shape `:5-15`):

    givens_generate :: (variant: GivensKind, dx: Scalar, dy: Scalar) -> (cs: RealScalar, sn: Scalar)
      -- (cs, sn) annihilating dy against dx; cs always real, sn ScalarType; cs² + |sn|² = 1
    givens_apply    :: (variant: GivensKind, cs: RealScalar, sn: Scalar, dx: Scalar, dy: Scalar) -> (dx', dy')
      -- (dx', dy') = (cs·dx + sn·dy, −s̄n·dx + cs·dy);  s̄n = conj(sn) in the complex case

    -- replay   fans into j applications of givens_apply to the new column (entries 0..j of h_new)
    -- generate fans into 1 application of givens_generate (the (h_new[j], h_new[j+1]) pair)
    -- apply    fans into 1 application of givens_apply to the column's own pair (zeroes h_new[j+1])
    -- apply_rhs fans into 1 application of givens_apply to the RHS pair (s[j], s[j+1])

Face 2 is the de-fusion of Face 1's leaf body into the explicit scalar-kernel sequence — exactly what
the L2 composition surfaces as first-class structure. The scalar kernels' own L0 surfaces
(`GeneratePlaneRotation` `iterative.cpp:73-109`, `ApplyPlaneRotation` `iterative.cpp:227-241`) are
**element-local, no reduction** — their L1>L0 realisation is the leaf-internal in-place 2-vector
update, deferred to the firm `ls_update_column` L1>L0 theme; **this theme cites the kernel
pair, it does not re-derive the kernels' LAPACK-style scaling** (the load-bearing finite-precision
content lives in the kernel pages + the leaf's L1>L0 theme; this theme records only the per-variant
*orchestration* of the kernel calls — the §"Reduction-path recording" table).

### Terminal back-solve fan-down (both faces)

The restart-cycle terminal `back_solve` fans into two stages — a small-dense triangular solve then a
basis reconstruction — independent of which per-column face was used:

    back_solve st'  =  let y               = back_solve_leaf st'.R st'.s   -- R · y = s over the leading (j+1)×(j+1) block
                           correction_basis = select st'.basis (op.basis_kind)
                       in { y, correction_basis }

    -- back_solve_leaf IS the firm L1 leaf `back_solve` (the small-dense triangular back-solve y = back_solve(R, s)):
    --   the in-place back-substitution iterative.cpp:652-660 (GMRES) / :831-840 (FGMRES):
    --   for i = j..0:  s[i] /= R[i][i];  for k = i-1..0:  s[k] -= R[i][k]·s[i]   (leaves y = s[0..j])
    -- the reconstruction correction_basis · y = Σ_k y[k]·basis[k] fans into a linear_combination over V or Z

The triangular solve **IS** the firm L1 leaf [`back_solve`](../L1/back_solve.md): the
small-dense back-substitution `y = back_solve(R, s)` over the materialised `(j+1)×(j+1)`
upper-triangular running-QR R-factor `R` (the leading block of the Hessenberg register, after the
stream has annihilated every sub-diagonal) and the rotated RHS `s`. Its body is the in-place
`s[0..j]` overwrite at `iterative.cpp:652-660` (GMRES) / `:831-840` (FGMRES); that in-place L0
mechanism is the leaf's own L1>L0 concern, not re-derived here. The reconstruction
`Σ_k y[k]·basis[k]` is the firm [`linear_combination`](../L2/linear_combination.md) fold over the
selected basis (the L0 `x.Add(s[k], V[k])` / `x.Add(s[k], Z[k])` accumulation loop,
`iterative.cpp:666` / `:843`); the `op.basis_kind` axis selects `V` vs `Z` and only this stage reads
the axis (L2 entry law 6).

**The terminal leaf is `back_solve`, NOT a general `trsv`.** The back-solve target is the
**specific** small-dense restart-correction back-solve
[`back_solve`](../L1/back_solve.md), which `book/src/L1/back_solve.md:44-61` deliberately argues is
**not** a general `trsv` (a general sparse-triangular solve `sparse_triangular_solve` — the
Gauss-Seidel / ILU smoother kernel acting on the length-`N` field — has *no positive L0 anchor* and
remains the **blocked** `trsv` L3-inventory item, `scaffolding/open-questions.md:24`). This theme's
back-solve fan-down targets `back_solve` (the coordinate-space dense back-substitution, dimension
`j+1` ≤ `max_dim`, no collective); the general `trsv` is a distinct, separately-blocked operator and
is **not** claimed to exist by this theme. (`back_solve` is the small-dense-*triangular* sibling of
the firm [`lu_solve`](../L1/lu_solve.md), the small-dense-*general* direct solve.)

## The fan-down rewrite (L2 → L1)

The lowering reads the per-column composition and emits the matching L1 form. **For Face 1** the
rewrite is the **identity-in-value** specialization onto the opaque leaf — the running-QR sub-steps
collapse into one `ls_update_column` call; `op.variant` and the registers flow straight through.
**For Face 2** the rewrite is the **fixed four-sub-step expansion** in scalar-kernel order — this is
the load-bearing content, because the sub-step *ordering* (replay-before-generate) is non-commutative
and the reduction path is pinned (§"Reduction-path recording"). There is **no per-variant sequence
selection** here (unlike the sibling's MGS/CGS/CGS2 axis): the sub-step sequence is **fixed and
identical** across both variant axes — `op.basis_kind` selects only the terminal reconstruction
basis, `op.variant` selects only the scalar kernel element-type. The L0 dispatch sites are the GMRES
inner loop `iterative.cpp:634-642` and the FGMRES inner loop `iterative.cpp:813-821` (line-for-line
identical — L2 entry law 6).

    incremental_least_squares op st h_new                       -- Face 1 (opaque leaf)
      =  ls_update_column (krylov_of op st) (st.H.ncols) h_new  -- sub-steps collapse; { state, beta } = (K'.regs, K'.beta)

    incremental_least_squares op st h_new                       -- Face 2 (de-fused), j = st.H.ncols, FIXED sequence
      =  let h1  = foldl (\h k -> givens_apply op.variant st.cs[k] st.sn[k] h[k] h[k+1])  -- REPLAY: j applies, ordered 0..j-1
                          h_new [0 .. j-1]                                                --   each touches the new column
         let (cs_j, sn_j) = givens_generate op.variant h1[j] h1[j+1]                      -- GENERATE: 1 (AFTER replay — law 2)
         let h2  = givens_apply op.variant cs_j sn_j h1[j] h1[j+1]                        -- APPLY: 1 (h2[j+1] := 0)
         let s'  = givens_apply op.variant cs_j sn_j st.s[j] st.s[j+1]                    -- APPLY_RHS: 1 (s'[j+1] = residual)
         in { state = advance st h2 cs_j sn_j s', beta = |s'[j+1]| }

The **dispatch rule** is: *emit the fixed `replay(×j) ▷ generate ▷ apply ▷ apply_rhs` scalar-kernel
sequence (the de-fused face) or the single opaque `ls_update_column` leaf (the fused face); the
replay-before-generate ordering is mandatory and non-commutative; `op.variant` parameterises the
scalar kernel element-type and `op.basis_kind` parameterises only the terminal back-solve basis.*
This is the L2 entry's residual-exposure + replay-ordering laws (laws 1, 2) read as a lowering — at
the value level it is one form; the variant axes are parametric substitutions, not structural
variants.

### Why the sequence is fixed (no MGS/CGS-style axis)

Unlike the sibling [`orthogonalize-composition-lowering`](./orthogonalize-composition-lowering.md)
(whose `gs_orthog` axis fans into three genuinely-distinct `[dot, axpy]` loop structures), the
running-QR stream has **exactly one sub-step ordering** — `iterative.cpp:632-642` is the only
plane-rotation path Palace's GMRES/FGMRES use; there is no Householder / two-sided alternative (L2
entry §Variant axes; Householder scoped out per CLAUDE.md unimplemented-component policy). The two
variant axes here are both **parametric absorption**: they substitute the scalar kernel
(`op.variant`) or the reconstruction basis (`op.basis_kind`) without changing the sub-step sequence,
its ordering, or its reduction shape. The single load-bearing residue is the **finite-precision
reduction path** pinned by the fixed sequence (§"Reduction-path recording"), not a selectable
collective shape.

## Reduction-path recording — load-bearing-numerical residue

This is the **load-bearing residue the L2 entry deferred to "the forthcoming L2>L1 theme"** (L2 entry
§Algebraic-laws, the rotation-stream-non-associativity non-law
`book/src/L2/incremental_least_squares.md:278-285`). The incremental running-QR agrees with a
from-scratch QR of the assembled `H̄_j` in exact arithmetic (L2 entry law 1) but differs at the bit
level — the rotation order and the LAPACK-style scaling pin a specific finite-precision reduction
path. Read off the verified `iterative.cpp` bodies (the scalar 2-vector kernel itself is the
[`givens`](../concepts/givens.md) page; this table records the **per-column orchestration** the
lowering pins):

| lowered sub-step | L0 body (verified) | scalar-kernel fan | pinned reduction path |
|---|---|---|---|
| replay   | GMRES `iterative.cpp:634-636` / FGMRES `:813-815` (`for k=0..j-1: ApplyPlaneRotation(Hj[k], Hj[k+1], cs[k], sn[k])`) | `j` `givens_apply` calls, **strictly ordered `k = 0..j-1`** | each touches the new column before the next; **non-commutative chain** (law 2); the `plane-rotation-stream` §"Sequential character" `sequential-obstruction` candidate at L3 |
| generate | GMRES `iterative.cpp:638` / FGMRES `:817` (`GeneratePlaneRotation(Hj[j], Hj[j+1], cs[j], sn[j])`) | 1 `givens_generate` (real `:73-108` LAPACK-scaled / complex `:112-118`) | the LAPACK-style overflow/underflow scaling (`:101-108`) pins the rotation's finite-precision value |
| apply    | GMRES `iterative.cpp:639` / FGMRES `:818` (`ApplyPlaneRotation(Hj[j], Hj[j+1], cs[j], sn[j])`) | 1 `givens_apply` (`:227-241`); zeroes `Hj[j+1]` | element-local 2-vector FMA; `s̄n = conj(sn)` complex |
| apply_rhs | GMRES `iterative.cpp:640` / FGMRES `:819` (`ApplyPlaneRotation(s[j], s[j+1], cs[j], sn[j])`) | 1 `givens_apply` to the RHS pair | `β = |s[j+1]|` (`:642` / `:821`) — the residual exposure (law 1) |
| back-solve | GMRES `iterative.cpp:652-660` / FGMRES `:831-840` | the firm L1 [`back_solve`](../L1/back_solve.md) leaf (small-dense back-substitution over the `(j+1)×(j+1)` block) | the inner `k`-recurrence (`s[k] -= Hi[k]·s[i]`, `:659`/`:838`) reads `s[i]` from the just-completed row — a sequential triangular-solve dependency (the back-solve's own reduction-order non-law, `back_solve.md` §Algebraic-laws) |

The **replay sub-step is the bit-level non-commutative chain** (the left-to-right stored-rotation
composition does not commute — L2 entry law 2 / non-law sub-step commutativity); it is the
[`sequential-obstruction`](../concepts/sequential-obstruction.md) candidate flagged by
[`plane-rotation-stream`](../concepts/plane-rotation-stream.md) §"Sequential character" (`:21-23`) for
the eventual L3 iteration rotation. The reduction tree *within* each scalar kernel is element-local (a
single 2-vector FMA, no cross-element reduction), so unlike `dot`/`orthogonalize` there is **no MPI
collective** in the stream — the residue here is purely the **rotation ordering + LAPACK scaling**,
not a `GlobalSum` shape. (Single-rank scope folds nothing; the stream is rank-local already. The
terminal `back_solve` is likewise local dense work with no collective — `back_solve.md` §Semantics.)

## Empty / single-column boundary

The empty-stream case (`j = -1`, no columns) lowers to the identity for the terminal back-solve:
`back_solve` over an empty factor yields `y = []` and the zero correction (L2 entry law 5;
`back_solve.md` §Algebraic-laws law 5). The first column (`j = 0`) lowers to the **skip-replay** form
— the replay fold is empty (the `k < j` loop is empty, `iterative.cpp:634-636`), so the lowered
sequence is just `generate ▷ apply ▷ apply_rhs`; the residual-exposure law still holds (`β = |s[1]|`).
Both boundaries are the same in the opaque-leaf face (`ls_update_column` at `j = 0` runs the no-replay
body) and the de-fused face (the empty fold); the terminal `back_solve` at `j = 0` is one scalar
division `y[0] = s[0] / R[0][0]` (`back_solve.md:109-110`).

## Applicability conditions

The fan-down preserves the L2 value when:

1. **Replay-before-generate ordering is mandatory.** The stored rotations `0..j-1` MUST be applied to
   the new column before the new rotation `j` is generated (`iterative.cpp:634-638`: the replay loop
   precedes `GeneratePlaneRotation`). Generating from an un-replayed column annihilates against the
   wrong diagonal and produces a non-triangular factor (L2 entry law 2). The lowering is **not**
   order-invariant in this sub-step — this is the running-QR's structural invariant, inherited from
   the [`givens`](../concepts/givens.md) §Contract replay-order rule.

2. **Unitary kernels, exact residual exposure.** Each scalar rotation is unitary
   (`cs² + |sn|² = 1`, `iterative.cpp:118`), so the full stream `Qⱼ` is unitary and
   `β = |s[j+1]| = min_y ‖β₀·e₁ − H̄_j·y‖₂` exactly (L2 entry laws 1, 3). The lowering preserves this
   under the **algorithmic-correctness** reading unconditionally; **bit-reproduction** of a specific
   Palace call additionally requires matching the fixed sub-step ordering + LAPACK scaling
   (§"Reduction-path recording"; the standard load-bearing-vs-transparent classification, CLAUDE.md
   §Optimization tricks — the running-QR exists precisely to make the residual cheap, a load-bearing
   numerical trick).

3. **`op.variant` is a scalar-kernel substitution.** Real (`cs`, `sn` real) ↔ complex (`cs` real,
   `sn` `ScalarType`, `s̄n = conj(sn)` in `apply`) substitutes only the element-local kernel; the
   sub-step sequence, ordering, and the register layout `(s, sn : ScalarType; cs : RealType)` are
   invariant (`iterative.hpp:193-194`; L2 entry §Variant axes). No per-column branching.

4. **`op.basis_kind` reads only the terminal reconstruction.** `V` (GMRES) ↔ `Z` (FGMRES) leaves the
   stream, the registers, the residual byproduct, and the back-solved `y` identical (the GMRES/FGMRES
   stream code is line-for-line identical, `iterative.cpp:634-642` ≡ `:813-821`); only
   `correction_basis · y` reads `V` (`:666`, right-precond post-applies `B`: `:674-677`) vs `Z`
   (`:843`) — L2 entry law 6. The terminal [`back_solve`](../L1/back_solve.md) leaf is itself
   basis-lift-independent (`back_solve.md` §Algebraic-laws law 6) — it produces only the coordinate
   vector `y`; the basis is read by the downstream `linear_combination` reconstruction only.

5. **Leaf-stops-at-L1; kernel L0 deferred.** The de-fused face's scalar kernels and the opaque leaf's
   in-place 2-vector updates are L1>L0 concerns of the firm `ls_update_column` L1>L0 theme; the
   terminal back-solve's in-place `s[0..j]` overwrite is the firm [`back_solve`](../L1/back_solve.md)
   leaf's own L1>L0 concern (`back_solve.md` §"L1 vs L0 distinction"), and the `x.Add` reconstruction
   loop is a [`linear_combination`](../L2/linear_combination.md) concern. **This theme stops at the L1
   leaves and does not re-derive the L0 in-place mechanics** (the same boundary the sibling
   [`orthogonalize-composition-lowering`](./orthogonalize-composition-lowering.md) draws at its L1
   leaves).

## Justification kind

`algebraic` — the fan-down rule **is** the L2 entry's already-firm composition-level laws read as a
lowering: law 1 (residual exposure by unitarity — `β = |s[j+1]|` is the apply_rhs byproduct), law 2
(replay-before-generate ordering — the mandatory non-commutative sub-step sequence), and law 6
(`op.basis_kind`/`op.variant` parametric invariance — the variant axes select kernel + reconstruction
basis, not structure) together pin the entire rewrite. The Face-1 lowering (onto the opaque
`ls_update_column` leaf) is the **identity-in-value** specialization of the named composition onto the
single-column L1 leaf (L2 entry §"L2 vs L1 distinction"). A **structural** flavour is present (the
Face-2 de-fusion is the syntactic expansion of the four-sub-step pipeline into scalar-kernel calls)
and a **reduction-chain** flavour is present in the replay fold + the terminal back-solve triangular
recurrence (each step reads the previous), but the governing justification is the algebraic
residual-exposure + replay-ordering laws, so the theme is classified `algebraic` — matching the
sibling [`orthogonalize-composition-lowering`](./orthogonalize-composition-lowering.md) `algebraic`
classification (both are L2-laws-read-as-lowering named-composition fan-downs). The per-variant
reduction path is the load-bearing-numerical residue recorded in §"Reduction-path recording"; the
scalar-kernel LAPACK scaling is delegated to the kernel pages + the firm `ls_update_column`
L1>L0 theme; the back-solve's reduction-order non-law is delegated to the firm
[`back_solve`](../L1/back_solve.md) leaf.

## Speculative L1 operators

**None proposed by this theme.** The L1 RHS resolves to firm vocabulary:

- Face 1 — the L1 column-streaming leaf **[`ls_update_column`](../L1/ls_update_column.md)**
  (the single-column running-QR update `(K, j, h_new) → K'`; **firm**,
  firm-on-positive-structure). The co-extensive firm **Face 2** carries the de-fused value, so either
  face resolves the L1 RHS.
- Face 2 — the scalar Givens kernel pair [`concepts/givens_generate`](../concepts/givens_generate.md)
  / [`concepts/givens_apply`](../concepts/givens_apply.md) (firm concept pages; element-local
  kernels).
- Terminal back-solve — the firm L1 leaf [`back_solve`](../L1/back_solve.md) (the
  small-dense `(j+1)×(j+1)` upper-triangular back-substitution `y = back_solve(R, s)`); the
  reconstruction stage is the firm [`linear_combination`](../L2/linear_combination.md) fold over the
  selected basis.

The LHS [`incremental_least_squares`](../L2/incremental_least_squares.md) is firm. This
theme proposes no new operators — it is the lowering edge between firm vocabulary (L2 LHS) and
firm L1 leaves (Face 2 + `back_solve` + `linear_combination`), with the opaque Face-1 leaf a
plain-text forward-reference. **Householder is scoped out** (Palace's L0 has no Householder path — L2
entry §Variant axes; CLAUDE.md unimplemented-component policy). **The general `trsv` is NOT the
back-solve target** — it is a distinct, separately-**blocked** L3-inventory operator
(`sparse_triangular_solve`, no positive L0 anchor, `scaffolding/open-questions.md:24`); this theme's terminal
solve is the specific `back_solve` leaf.

## Evidence

L0 evidence ranges (paths relative to `reference/`):

- `palace/linalg/iterative.cpp:73-108` — `GeneratePlaneRotation` (real): LAPACK-style scaled rotation
  generator (the generate sub-step's real kernel; scaling at `:101-108`).
- `palace/linalg/iterative.cpp:112-118` — `GeneratePlaneRotation` (complex): real `cs`, complex `sn`,
  in-comment unitarity contract "cs is real and cs² + |sn|² = 1" (`:118`).
- `palace/linalg/iterative.cpp:227-241` — `ApplyPlaneRotation` (real `:227` + complex `:235`): the
  in-place 2-vector update `(dx', dy') = (cs·dx + sn·dy, −s̄n·dx + cs·dy)`. The apply / apply_rhs /
  replay kernel.
- `palace/linalg/iterative.cpp:612` — `s[0] = beta`: the RHS seed `s = β₀·e₁`.
- `palace/linalg/iterative.cpp:631` — `Hj[j + 1] = linalg::Norml2(comm, w)`: the sub-diagonal entry of
  the arriving column `h_new[j+1]` (the orthogonalize coeffs occupy `0..j`).
- `palace/linalg/iterative.cpp:634-636` — GMRES **replay**: `for (int k = 0; k < j; k++)
  ApplyPlaneRotation(Hj[k], Hj[k+1], cs[k], sn[k]);` (anchor on `:636`; law 2 ordering).
- `palace/linalg/iterative.cpp:638` — GMRES **generate**: `GeneratePlaneRotation(Hj[j], Hj[j+1], cs[j],
  sn[j]);`.
- `palace/linalg/iterative.cpp:639` — GMRES **apply** (triangularise own column):
  `ApplyPlaneRotation(Hj[j], Hj[j+1], cs[j], sn[j]);`.
- `palace/linalg/iterative.cpp:640` — GMRES **apply_rhs**: `ApplyPlaneRotation(s[j], s[j+1], cs[j],
  sn[j]);` — concentrates the residual in `s[j+1]`.
- `palace/linalg/iterative.cpp:642` — `beta = std::abs(s[j + 1]);` — the residual exposure (law 1).
- `palace/linalg/iterative.cpp:644` — `converged = (beta < eps);` — convergence read with no explicit
  residual evaluation.
- `palace/linalg/iterative.cpp:652-660` — GMRES **back-solve** ("Reconstruct the solution"): in-place
  back-substitution `s[i] /= Hi[i]` (`:656`) / `s[k] -= Hi[k] * s[i]` (`:659`) — the firm
  [`back_solve`](../L1/back_solve.md) leaf body (law 4).
- `palace/linalg/iterative.cpp:666` — GMRES correction (`op.basis_kind = V`, left/unpreconditioned):
  `x.Add(s[k], V[k]);` — the `linear_combination` reconstruction.
- `palace/linalg/iterative.cpp:674-677` — GMRES correction (right-preconditioned): `r.Add(s[k], V[k])`
  (`:674`) then `ApplyB(B, r, V[0], ...); x += V[0]` (`:676-677`) — preconditioner post-applied to the
  `V`-correction; back-solve identical.
- `palace/linalg/iterative.cpp:812-821` — FGMRES running-QR stream: replay `:813-815`, generate `:817`,
  apply `:818`, apply_rhs `:819`, `beta` `:821` — **line-for-line identical** to the GMRES stream (law
  6: `op.basis_kind`-invariant).
- `palace/linalg/iterative.cpp:831-840` — FGMRES back-solve (identical to GMRES `:652-660`); then
  `x.Add(s[k], Z[k])` (`:843`) the `op.basis_kind = Z` reconstruction.
- `palace/linalg/iterative.hpp:193-194` — `GmresSolver` rotation-register declarations: `mutable
  std::vector<ScalarType> s, sn;` (`:193`) / `mutable std::vector<RealType> cs;` (`:194`) — the
  element-type split underwriting `op.variant`.

L2 / L1 / concept / cross-theme anchors:

- `book/src/L2/incremental_least_squares.md` — the firm L2 named composition (LHS); its
  §Semantics four-sub-step pipeline, §Algebraic-laws laws 1/2/3/6, the `back_solve` terminal-projection
  signature (`:81-83`), and the deferred rotation-stream-non-associativity non-law (`:278-285`) +
  §Dependencies forward-reference (`:334-340`) are this theme's dispatch rule and load-bearing residue.
- `book/src/L1/back_solve.md` — the **firm** L1 leaf (Face / terminal back-solve target);
  the small-dense triangular back-solve `y = back_solve(R, s)`, its §"Why this is NOT a general `trsv`"
  argument (`:44-61`), its basis-lift-independence law (§Algebraic-laws law 6), and its reduction-order
  non-law. This theme's terminal-back-solve fan-down lowers onto this leaf.
- `book/src/concepts/incremental_least_squares.md` — the `ls_update_column` L1 column-streaming-leaf
  contract (`:14`) + the "What is hidden at L1" list (`:22-27`); the cross-method reuse rationale.
- `book/src/concepts/plane-rotation-stream.md` — the stream §Shape (`:5-15`) + §"Sequential character"
  (`:21-23`, the replay-chain `sequential-obstruction` candidate at L3) + §"Variants the stream is
  invariant to" (`:25-33`, the parametric-axis invariance).
- `book/src/concepts/givens.md`, `givens_generate.md`, `givens_apply.md` — the scalar kernel pair + the
  replay-order contract.
- `book/src/L2/linear_combination.md` — the firm fold the terminal reconstruction `Σ_k y[k]·basis[k]`
  lowers into.
- `book/src/L2-L1/orthogonalize-composition-lowering.md` — the sibling firm L2>L1 named-composition
  theme (the structural template: two-face L1 RHS, dispatch-rule prose, reduction-path recording table,
  justification `algebraic`).
- `book/src/L2/krylov_step.md`, `book/src/L2/ksp_solve.md` — the consumers that fold (krylov_step) /
  consume the byproduct + back-solve correction (ksp_solve §Semantics phase-3 `materialise_iterate`).

## Status

`firm` — the LHS L2 composition is firm; the lowering structure is fully recognized and
exhaustively cited against L0 source (the four-sub-step fan-down, the fixed
replay-before-generate ordering, the terminal back-solve fan-down, the two parametric variant axes,
and the per-variant reduction-path table are all read straight off `iterative.cpp:634-642` /
`:652-677` / `:812-844` + the scalar kernels `:73-241`); and the L1 RHS resolves to **firm**
vocabulary on the value-carrying faces: the de-fused **Face 2** is the firm scalar Givens kernel pair
([`givens_generate`](../concepts/givens_generate.md) / [`givens_apply`](../concepts/givens_apply.md)),
the terminal triangular solve **is the firm L1 [`back_solve`](../L1/back_solve.md) leaf**,
and the reconstruction is the firm [`linear_combination`](../L2/linear_combination.md) fold. The opaque
Face-1 [`ls_update_column`](../L1/ls_update_column.md) column-streaming leaf (firm) and the de-fused
Face-2 are co-extensive presentations of the same value. The general `trsv` is a distinct,
separately-blocked L3-inventory operator (`scaffolding/open-questions.md:24`), NOT this theme's
back-solve target.

## Open questions / caveats

- **General `trsv` remains BLOCKED.** The terminal-back-solve target is the
  specific `back_solve` leaf, NOT the general `trsv` / `sparse_triangular_solve` (the Gauss-Seidel /
  ILU smoother kernel on the length-`N` field, no positive L0 anchor, `scaffolding/open-questions.md:24,:537`).
  The `trsv` L3-inventory gap stays open (likely obstruction-theme target).

- **L1>L0 boundary deferred.** This theme stops at the L1 leaves and does NOT re-derive the L0 in-place
  running-QR mechanics (the four `*PlaneRotation` writes to `Hj`/`cs`/`sn`/`s`) or the back-solve
  in-place `s[0..j]` overwrite (the firm `back_solve` leaf's own L1>L0 concern) or the `x.Add`
  reconstruction (a `linear_combination` concern). The per-column in-place step is the firm
  [`ls_update_column-mutation-rotation`](../L1-L0/ls-update-column-mutation-rotation.md) L1>L0 theme.

- **L3 sequential-obstruction forecast (replay chain + back-solve recurrence).** The replay sub-step is
  a length-`j` ordered chain of 2-vector updates (`iterative.cpp:634-636`), each reading the previous —
  the [`plane-rotation-stream`](../concepts/plane-rotation-stream.md) §"Sequential character" (`:21-23`)
  flags it as a `sequential-obstruction` candidate for the eventual L3 iteration rotation (the
  back-solve's inner `k`-recurrence likewise — `back_solve.md` reduction-order non-law).
