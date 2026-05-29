---
agent: abstractor
invoked_at: 2026-05-29T175529Z
scope: L2>L1 theme sketch — incremental-least-squares-composition-lowering
status: pending
inputs:
  - book/src/L2/incremental-least-squares.md (firm L2 LHS, cycle-026)
  - book/src/L2-L1/orthogonalize-composition-lowering.md (firm sibling named-composition L2>L1 theme, cycle-019 precedent)
  - book/src/concepts/incremental-least-squares.md (ls_update_column L1 leaf contract)
  - book/src/concepts/plane-rotation-stream.md (replay-chain sequential character; L3 obstruction note)
  - book/src/concepts/givens.md / givens_generate.md / givens_apply.md (scalar kernel pair)
  - palace/linalg/iterative.cpp:73-118 (Givens generate real/complex), :227-241 (apply), :612 (s seed), :631 (Norml2 sub-diagonal), :634-644 (GMRES stream + beta read), :652-677 (GMRES back-solve + V/Z correction), :812-844 (FGMRES stream + back-solve + Z correction)
  - palace/linalg/iterative.hpp:193-194 (rotation-register element-type split)
---

# CYCLE: L2>L1 theme sketch — incremental-least-squares-composition-lowering

## Summary

The firm L2 named composition `incremental_least_squares` (the GMRES/FGMRES running-QR / Givens-rotation stream, firmed cycle-026) is the `replay ▷ generate ▷ apply ▷ apply_rhs` per-column pipeline with a terminal back-solve, exposing the LS residual norm `β = |s[j+1]|` as a unitary byproduct. This theme narrates forward (L2 → L1) how that composition **fans down** into its L1 leaves: the per-column running-QR sub-step sequence collapses into the single firm L1 leaf **`ls_update_column`** (dispatch-4, forward-referenced as plain text), whose own L0 in-place running-QR mechanics — the four scalar plane-rotation kernel calls per column at `iterative.cpp:634-642` — are the leaf's L1>L0 concern; the terminal back-solve fans into a small-dense triangular solve (the `trsv`-shaped back-substitution `iterative.cpp:652-660`) followed by the basis-reconstruction `correction_basis · y`. The theme records the **two faces** of the L1 RHS exactly as the sibling `orthogonalize-composition-lowering`: a fused face (the opaque `ls_update_column` leaf, one-to-one with Palace's per-column loop body) and a de-fused face (the four scalar Givens sub-steps spelled out). The **load-bearing content** is the disclosed replay-before-generate ordering (the running-QR's structural non-commutativity) and which finite-precision reduction path each lowered variant pins; the variant axes (`basis_kind ∈ {V,Z}` GMRES/FGMRES, `variant ∈ {real,complex}`) are both **parametric** — invariant on the stream shape, selecting only the back-solve reconstruction basis and the scalar kernel element-type. The justification is `algebraic` (the L2 entry's already-firm composition-level laws read as a lowering), matching the sibling. Both L1 RHS faces resolve to firm-or-forthcoming-firm vocabulary; no speculative operator is proposed.

## Proposed changes

```new:book/src/L2-L1/incremental-least-squares-composition-lowering.md
# incremental-least-squares-composition-lowering

The fan-down rotation for the GMRES / FGMRES running-QR / Givens-rotation stream. Lowers the
firm L2 named composition [`incremental-least-squares`](../L2/incremental-least-squares.md) — the
per-column `replay ▷ generate ▷ apply ▷ apply_rhs` pipeline with a terminal back-solve, threaded
across the Arnoldi iteration so the growing upper-Hessenberg least-squares problem
`min ‖β·e₁ − H̄·y‖₂` is triangularised incrementally and the residual norm `β = |s[j+1]|` falls out
as a free unitary byproduct — into its L1 leaves. Narrated forward (L2 → L1): the one named L2
composition **fans down** into the single firm L1 leaf `ls_update_column` (the per-column running-QR
update, opaque face) — equivalently, into the explicit scalar Givens sub-step sequence (de-fused
face) — plus a terminal back-solve = triangular solve ▷ basis reconstruction. This theme records
which finite-precision reduction path each lowered variant pins (the **load-bearing rotation-stream
non-associativity** the L2 entry deferred to "the forthcoming L2>L1 theme",
[`incremental-least-squares`](../L2/incremental-least-squares.md) §Algebraic-laws non-law /
§Dependencies) and the **replay-before-generate ordering** that is the running-QR's structural
invariant. Sibling to [`orthogonalize-composition-lowering`](./orthogonalize-composition-lowering.md)
(the other named-composition `project ▷ subtract` fan-down): each is a
one-L2-composition-fans-into-L1-vocabulary theme.

## Slug

`incremental-least-squares-composition-lowering`

## L2 form (LHS)

The L2 form is the named running-QR composition over the incremental factorisation state `st` and a
freshly-arrived Hessenberg column `h_new`, parameterised by the basis-kind and Givens-element-type
axes ([`incremental-least-squares`](../L2/incremental-least-squares.md) §Signature, §Semantics):

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
`op.variant`-shape-invariant in exact arithmetic (L2 entry laws 6, and the conjugation lives in the
scalar kernel).

## L1 form (RHS)

The L1 form has two co-extensive faces of the same value (as the sibling
[`orthogonalize-composition-lowering`](./orthogonalize-composition-lowering.md) §"L1 form (RHS)").
**Which face the lowering targets is a resolution choice, not a value choice** — they advance the
factorisation state identically.

### Face 1 — the opaque single-column leaf (the fused face)

The firm L1 leaf `ls_update_column` (dispatch-4, cycle-027, forward-reference; per the
[`concepts/incremental-least-squares`](../concepts/incremental-least-squares.md) contract), mirroring
Palace's per-column loop body one-to-one:

    ls_update_column :: (K: Krylov, j: Int, h_new: HessCol) -> Krylov'
      -- K' = K with: h_new triangularised into H[:,j]; one new rotation (cs[j], sn[j]) recorded;
      --              the RHS s advanced by that rotation; K'.beta = |s[j+1]| the LS residual.

At L1 the per-column running-QR sub-steps (replay / generate / apply / apply_rhs) and the
residual-exposure mechanism are **hidden inside the leaf** as a single "incremental triangularisation
with residual side-output" operation, exactly as the concept page's "What is *hidden* at L1" list
states ([`concepts/incremental-least-squares`](../concepts/incremental-least-squares.md):22-27). The
L2 record `{ state, beta }` is the same value as the L1 leaf's advanced `Krylov'` bundle (its `K'.beta`
is the L2 `beta`; its rotation registers + RHS + Hessenberg are the L2 `state`). The leaf's own
lowering onto the L0 in-place free functions — the four `*PlaneRotation` calls at
`iterative.cpp:634-642` writing `Hj`, `cs`, `sn`, `s` in place — is the **L1>L0** concern of the
forthcoming `ls_update_column-mutation-rotation` theme; **this theme stops at the L1 leaf and does not
re-derive that L0 in-place step** (the same boundary the sibling draws at the L1 `orthogonalize` leaf).

### Face 2 — the de-fused scalar Givens sub-step sequence (the spelled-out face)

The four per-column sub-steps spelled out in the firm scalar Givens kernel pair
([`concepts/givens_generate`](../concepts/givens_generate.md) /
[`concepts/givens_apply`](../concepts/givens_apply.md);
[`concepts/plane-rotation-stream`](../concepts/plane-rotation-stream.md) §Shape):

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
(`GeneratePlaneRotation` `iterative.cpp:73-118`, `ApplyPlaneRotation` `iterative.cpp:227-241`) are
**element-local, no reduction** — their L1>L0 realisation is the leaf-internal in-place 2-vector
update, deferred to the forthcoming `ls_update_column` L1>L0 theme; **this theme cites the kernel
pair, it does not re-derive the kernels' LAPACK-style scaling** (the load-bearing finite-precision
content lives in the kernel pages + the leaf's L1>L0 theme; this theme records only the per-variant
*orchestration* of the kernel calls — the §"Reduction-path recording" table).

### Terminal back-solve fan-down (both faces)

The restart-cycle terminal `back_solve` fans into two stages — a small-dense triangular solve then a
basis reconstruction — independent of which per-column face was used:

    back_solve st'  =  let y               = trsv_upper st'.H st'.s     -- back-substitution: H·y = s over leading (j+1)×(j+1) block
                           correction_basis = select st'.basis (op.basis_kind)
                       in { y, correction_basis }

    -- trsv_upper fans into the in-place back-substitution iterative.cpp:652-660 (GMRES) / :831-840 (FGMRES):
    --   for i = j..0:  s[i] /= H[i][i];  for k = i-1..0:  s[k] -= H[i][k]·s[i]   (leaves y = s[0..j])
    -- the reconstruction correction_basis · y = Σ_k y[k]·basis[k] fans into a linear_combination over V or Z

The triangular solve is a small-dense `trsv`-shaped op over the `(j+1)×(j+1)` upper-triangular block
(an L1 `trsv` leaf is the natural lowering target, forthcoming — forward-reference only). The
reconstruction `Σ_k y[k]·basis[k]` is the firm [`linear_combination`](../L2/linear_combination.md)
fold over the selected basis (the L0 `x.Add(s[k], V[k])` / `x.Add(s[k], Z[k])` accumulation loop,
`iterative.cpp:666` / `:843`); the `op.basis_kind` axis selects `V` vs `Z` and only this stage reads
the axis (L2 entry law 6).

## The fan-down rewrite (L2 → L1)

The lowering reads the per-column composition and emits the matching L1 form. **For Face 1** the
rewrite is the **identity-in-value** specialization onto the opaque leaf — the running-QR sub-steps
collapse into one `ls_update_column` call; `op.variant` and the registers flow straight through.
**For Face 2** the rewrite is the **fixed four-sub-step expansion** in scalar-kernel order — this is
the load-bearing content, because the sub-step *ordering* (replay-before-generate) is non-commutative
and the reduction path is pinned (§"Reduction-path recording"). There is **no per-variant sequence
selection** here (unlike the sibling's MGS/CGS/CGS2 axis): the sub-step sequence is **fixed and
identical** across both variant axes — `op.basis_kind` selects only the terminal reconstruction basis,
`op.variant` selects only the scalar kernel element-type. The L0 dispatch sites are the GMRES inner
loop `iterative.cpp:634-642` and the FGMRES inner loop `iterative.cpp:813-821` (line-for-line
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
scalar kernel element-type and `op.basis_kind` parameterises only the terminal back-solve basis.* This
is the L2 entry's residual-exposure + replay-ordering laws (laws 1, 2) read as a lowering — at the
value level it is one form; the variant axes are parametric substitutions, not structural variants.

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
§Algebraic-laws, the rotation-stream-non-associativity non-law `book/src/L2/incremental-least-squares.md:278-285`).
The incremental running-QR agrees with a from-scratch QR of the assembled `H̄_j` in exact arithmetic
(L2 entry law 1) but differs at the bit level — the rotation order and the LAPACK-style scaling pin a
specific finite-precision reduction path. Read off the verified `iterative.cpp` bodies (the scalar
2-vector kernel itself is the [`givens`](../concepts/givens.md) page; this table records the
**per-column orchestration** the lowering pins):

| lowered sub-step | L0 body (verified) | scalar-kernel fan | pinned reduction path |
|---|---|---|---|
| replay   | GMRES `iterative.cpp:634-636` / FGMRES `:813-815` (`for k=0..j-1: ApplyPlaneRotation(Hj[k], Hj[k+1], cs[k], sn[k])`) | `j` `givens_apply` calls, **strictly ordered `k = 0..j-1`** | each touches the new column before the next; **non-commutative chain** (law 2); the `plane-rotation-stream` §"Sequential character" `sequential-obstruction` candidate at L3 |
| generate | GMRES `iterative.cpp:638` / FGMRES `:817` (`GeneratePlaneRotation(Hj[j], Hj[j+1], cs[j], sn[j])`) | 1 `givens_generate` (real `:73-108` LAPACK-scaled / complex `:112-118`) | the LAPACK-style overflow/underflow scaling (`:101-108`) pins the rotation's finite-precision value |
| apply    | GMRES `iterative.cpp:639` / FGMRES `:818` (`ApplyPlaneRotation(Hj[j], Hj[j+1], cs[j], sn[j])`) | 1 `givens_apply` (`:227-241`); zeroes `Hj[j+1]` | element-local 2-vector FMA; `s̄n = conj(sn)` complex |
| apply_rhs | GMRES `iterative.cpp:640` / FGMRES `:819` (`ApplyPlaneRotation(s[j], s[j+1], cs[j], sn[j])`) | 1 `givens_apply` to the RHS pair | `β = |s[j+1]|` (`:642` / `:821`) — the residual exposure (law 1) |
| back-solve | GMRES `iterative.cpp:652-660` / FGMRES `:831-840` | `trsv`-shaped back-substitution over the `(j+1)×(j+1)` block | the inner `k`-recurrence (`s[k] -= Hi[k]·s[i]`, `:659`/`:838`) reads `s[i]` from the just-completed row — a sequential triangular-solve dependency |

The **replay sub-step is the bit-level non-commutative chain** (the left-to-right stored-rotation
composition does not commute — L2 entry law 2 / non-law sub-step commutativity); it is the
[`sequential-obstruction`](../concepts/sequential-obstruction.md) candidate flagged by
[`plane-rotation-stream`](../concepts/plane-rotation-stream.md) §"Sequential character" for the
eventual L3 iteration rotation. The reduction tree *within* each scalar kernel is element-local (a
single 2-vector FMA, no cross-element reduction), so unlike `dot`/`orthogonalize` there is **no MPI
collective** in the stream — the residue here is purely the **rotation ordering + LAPACK scaling**,
not a `GlobalSum` shape. (Single-rank scope folds nothing; the stream is rank-local already.)

## Empty / single-column boundary

The empty-stream case (`j = -1`, no columns) lowers to the identity for the terminal back-solve:
`back_solve` over an empty factor yields `y = []` and the zero correction (L2 entry law 5). The first
column (`j = 0`) lowers to the **skip-replay** form — the replay fold is empty (the `k < j` loop is
empty, `iterative.cpp:634-636`), so the lowered sequence is just `generate ▷ apply ▷ apply_rhs`; the
residual-exposure law still holds (`β = |s[1]|`). Both boundaries are the same in the opaque-leaf face
(`ls_update_column` at `j = 0` runs the no-replay body) and the de-fused face (the empty fold).

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
   (`:843`) — L2 entry law 6.

5. **Leaf-stops-at-L1; kernel L0 deferred.** The de-fused face's scalar kernels and the opaque leaf's
   in-place 2-vector updates are L1>L0 concerns of the forthcoming `ls_update_column` L1>L0 theme; the
   back-solve's in-place `trsv` and the `x.Add` reconstruction loop are likewise leaf-internal /
   `linear_combination` concerns. **This theme stops at the L1 leaves and does not re-derive the L0
   in-place mechanics** (the same boundary the sibling
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
and a **reduction-chain** flavour is present in the replay fold + the back-solve triangular recurrence
(each step reads the previous), but the governing justification is the algebraic residual-exposure +
replay-ordering laws, so the theme is classified `algebraic` — matching the sibling
[`orthogonalize-composition-lowering`](./orthogonalize-composition-lowering.md) `algebraic`
classification (both are L2-laws-read-as-lowering named-composition fan-downs). The per-variant
reduction path is the load-bearing-numerical residue recorded in §"Reduction-path recording"; the
scalar-kernel LAPACK scaling is delegated to the kernel pages + the forthcoming `ls_update_column`
L1>L0 theme.

## Speculative L1 operators

**None proposed by this theme.** The L1 RHS resolves to firm-or-forthcoming-firm vocabulary:

- Face 1 — the L1 leaf **`ls_update_column`** (cycle-027 dispatch-4, authored concurrently;
  **forward-reference as plain text** per the rough-in-forward-reference convention — integration lands
  dispatch-4 FIRST so the link resolves). The single-column running-QR update leaf; this theme is the
  fan-down it is the LHS-named-composition of.
- Face 2 — the scalar Givens kernel pair [`concepts/givens_generate`](../concepts/givens_generate.md) /
  [`concepts/givens_apply`](../concepts/givens_apply.md) (firm concept pages; element-local kernels).
- Terminal back-solve — a small-dense **`trsv`** L1 leaf (the `(j+1)×(j+1)` upper-triangular
  back-substitution) is the natural lowering target (**forward-reference / forthcoming** — does not yet
  exist on disk); the reconstruction stage is the firm
  [`linear_combination`](../L2/linear_combination.md) fold over the selected basis.

The LHS [`incremental-least-squares`](../L2/incremental-least-squares.md) is firm (cycle-026). This
theme proposes no new operators — it is the lowering edge between firm vocabulary (L2 LHS) and
firm-or-forthcoming-firm L1 leaves. **Householder is scoped out** (Palace's L0 has no Householder
path — L2 entry §Variant axes; CLAUDE.md unimplemented-component policy).

## Verified-against

L0 evidence ranges (self-verified via `tools/citecheck/citecheck.py --anchor` against on-disk
`reference/palace/` this invocation — producer-citation self-verification per
[`verify-citation-range`](../../../skills/verify-citation-range/SKILL.md) "Producer self-verification";
the codemap had a +1 brace drift on `iterative.hpp:193-194` in cycle-026 — **on-disk authoritative**,
re-confirmed here as `:193`/`:194` exact):

- `palace/linalg/iterative.cpp:73-108` — `GeneratePlaneRotation` (real): LAPACK-style scaled rotation
  generator (the generate sub-step's real kernel; scaling at `:101-108`). **Self-verified (`--anchor
  'GeneratePlaneRotation'`, line 73).**
- `palace/linalg/iterative.cpp:112-118` — `GeneratePlaneRotation` (complex): real `cs`, complex `sn`,
  in-comment unitarity contract "cs is real and cs² + |sn|² = 1" (`:118`). **Self-verified (`--anchor
  'GeneratePlaneRotation'` line 112; `--anchor 'cs is real'` line 118).**
- `palace/linalg/iterative.cpp:227-241` — `ApplyPlaneRotation` (real `:227` + complex `:235`): the
  in-place 2-vector update `(dx', dy') = (cs·dx + sn·dy, −s̄n·dx + cs·dy)`. The apply / apply_rhs /
  replay kernel. **Self-verified (`--anchor 'ApplyPlaneRotation'`, lines 227, 235).**
- `palace/linalg/iterative.cpp:612` — `s[0] = beta`: the RHS seed `s = β₀·e₁`. **Self-verified
  (`--anchor 's\[0\] = beta'`, regex).**
- `palace/linalg/iterative.cpp:631` — `Hj[j + 1] = linalg::Norml2(comm, w)`: the sub-diagonal entry of
  the arriving column `h_new[j+1]` (the orthogonalize coeffs occupy `0..j`). **Self-verified (`--anchor
  'Norml2'`).**
- `palace/linalg/iterative.cpp:634-636` — GMRES **replay**: `for (int k = 0; k < j; k++)
  ApplyPlaneRotation(Hj[k], Hj[k+1], cs[k], sn[k]);` (anchor on `:636`; law 2 ordering). **Self-verified
  (`--anchor 'ApplyPlaneRotation'`, line 636 within range).**
- `palace/linalg/iterative.cpp:638` — GMRES **generate**: `GeneratePlaneRotation(Hj[j], Hj[j+1], cs[j],
  sn[j]);`. **Self-verified (`--anchor 'GeneratePlaneRotation'`).**
- `palace/linalg/iterative.cpp:639` — GMRES **apply** (triangularise own column):
  `ApplyPlaneRotation(Hj[j], Hj[j+1], cs[j], sn[j]);`. **Self-verified (`--anchor 'ApplyPlaneRotation'`).**
- `palace/linalg/iterative.cpp:640` — GMRES **apply_rhs**: `ApplyPlaneRotation(s[j], s[j+1], cs[j],
  sn[j]);` — concentrates the residual in `s[j+1]`. **Self-verified (`--anchor 'ApplyPlaneRotation(s[j]'`
  regex, line 640).**
- `palace/linalg/iterative.cpp:642` — `beta = std::abs(s[j + 1]);` — the residual exposure (law 1).
  **Self-verified (`--anchor 'beta = std::abs'`).**
- `palace/linalg/iterative.cpp:644` — `converged = (beta < eps);` — convergence read with no explicit
  residual evaluation. **Self-verified (`--anchor 'converged = '`).**
- `palace/linalg/iterative.cpp:652-660` — GMRES **back-solve** ("Reconstruct the solution"): in-place
  back-substitution `s[i] /= Hi[i]` (`:656`) / `s[k] -= Hi[k]·s[i]` (`:659`) — the `trsv`-shaped solve
  (law 4). **Self-verified (`--anchor 'Reconstruct the solution'` line 652; `s[i] /= Hi[i]` line 656;
  `s[k] -= Hi[k] * s[i]` line 659 — all confirmed exact, no drift).**
- `palace/linalg/iterative.cpp:666` — GMRES correction (`op.basis_kind = V`, left/unpreconditioned):
  `x.Add(s[k], V[k]);` — the `linear_combination` reconstruction. **Self-verified (`--anchor 'x.Add(s[k],
  V[k])'` literal).**
- `palace/linalg/iterative.cpp:674-677` — GMRES correction (right-preconditioned): `r.Add(s[k], V[k])`
  (`:674`) then `ApplyB(B, r, V[0], ...); x += V[0]` (`:676-677`) — preconditioner post-applied to the
  `V`-correction; back-solve identical. **Self-verified (`--anchor 'r.Add(s[k], V[k])'` line 674;
  `'ApplyB'` line 676).**
- `palace/linalg/iterative.cpp:812-821` — FGMRES running-QR stream: replay `:813-815`, generate `:817`,
  apply `:818`, apply_rhs `:819`, `beta` `:821` — **line-for-line identical** to the GMRES stream (law
  6: `op.basis_kind`-invariant). **Self-verified (`--anchor 'GeneratePlaneRotation'` line 817 within
  range; full `--show` confirms the identical sub-step sequence).**
- `palace/linalg/iterative.cpp:831-844` — FGMRES back-solve + correction: back-substitution `:831-840`
  (identical to GMRES) then `x.Add(s[k], Z[k])` (`:843`) — the `op.basis_kind = Z` reconstruction.
  **Self-verified (`--anchor 'x.Add(s[k], Z[k])'` literal line 843).**
- `palace/linalg/iterative.hpp:193-194` — `GmresSolver` rotation-register declarations: `mutable
  std::vector<ScalarType> s, sn;` (`:193`) / `mutable std::vector<RealType> cs;` (`:194`) — the
  element-type split underwriting `op.variant`. **Self-verified (`--anchor 'ScalarType> s, sn'` line
  193; `--anchor 'RealType> cs'` line 194 — the c026 codemap +1 brace drift confirmed corrected;
  on-disk exact).**

L2 / L1 / concept / cross-theme anchors:

- `book/src/L2/incremental-least-squares.md` — the firm L2 named composition (LHS, cycle-026); its
  §Semantics four-sub-step pipeline, §Algebraic-laws laws 1/2/3/6, and the deferred
  rotation-stream-non-associativity non-law (`:278-285`) + §Dependencies forward-reference (`:334-340`)
  are this theme's dispatch rule and load-bearing residue.
- `book/src/L1/...ls_update_column...` — the forthcoming firm L1 leaf (Face 1 RHS; cycle-027 dispatch-4,
  **forward-reference plain text** — not yet on disk at dispatch time).
- `book/src/concepts/incremental-least-squares.md` — the `ls_update_column` L1 leaf contract + the
  "What is hidden at L1" list (`:22-27`); the cross-method reuse rationale.
- `book/src/concepts/plane-rotation-stream.md` — the stream §Shape (`:7-15`) + §"Sequential character"
  (`:21-23`, the replay-chain `sequential-obstruction` candidate at L3) + §"Variants the stream is
  invariant to" (`:25-33`, the parametric-axis invariance).
- `book/src/concepts/givens.md`, `givens_generate.md`, `givens_apply.md` — the scalar kernel pair + the
  replay-order contract.
- `book/src/L2/linear_combination.md` — the firm fold the terminal reconstruction `Σ_k y[k]·basis[k]`
  lowers into.
- `book/src/L2-L1/orthogonalize-composition-lowering.md` — the sibling firm L2>L1 named-composition
  theme (the structural template: two-face L1 RHS, dispatch-rule prose, collective/reduction-path
  recording table, justification `algebraic`).
- `book/src/L2/krylov-step.md`, `book/src/L2/ksp_solve.md` — the consumers that fold (krylov-step) /
  consume the byproduct + back-solve correction (ksp_solve §Semantics phase-3 `materialise_iterate`).

## Status

`rough-in` — the LHS L2 composition is firm (cycle-026) and the lowering structure is fully
recognized and exhaustively cited against self-verified L0 source (the four-sub-step fan-down, the
fixed replay-before-generate ordering, the terminal back-solve fan-down, the two parametric variant
axes, and the per-variant reduction-path table are all read straight off `iterative.cpp:634-642` /
`:652-677` / `:812-844` + the scalar kernels `:73-241`). The theme is held at `rough-in` rather than
`firm` for one reason: **the Face-1 L1 leaf `ls_update_column` is a concurrent dispatch-4 artifact and
is forward-referenced as plain text** (it is not yet on disk; per the rough-in-forward-reference
convention the row + link must be plain-text until the anchor exists). Once dispatch-4 lands the firm
`ls_update_column` leaf (integration order: dispatch-4 FIRST), this theme's Face-1 link resolves and
the theme is promotable to `firm` on the sibling
[`orthogonalize-composition-lowering`](./orthogonalize-composition-lowering.md) bar (the lowering rule
IS the L2 entry's already-firm laws 1/2/6 read as a fan-down; both RHS faces firm; no speculative
operator). The terminal back-solve's `trsv` L1 leaf is a forthcoming forward-reference (the `trsv`
shape is cited at `iterative.cpp:652-660` but no L1 `trsv` entry exists yet) — a secondary
promotion-gate, lower priority than the `ls_update_column` leaf. **Promotion condition:** (a) the firm
`ls_update_column` leaf is on disk (dispatch-4) so the Face-1 link resolves; optionally (b) the L1
`trsv` leaf lands so the back-solve fan-down's triangular-solve target is a live link rather than a
forthcoming forward-reference. A `lowering-verifier` audit attaching the `verified_against:` block
(confirming the four-sub-step fan-down + the reduction-path table against the L0 source, and the
clean leaf-stops-at-L1 / L1>L0-deferred boundary) is the standard follow-up.

## Open questions / caveats

- **`ls_update_column` leaf forward-reference (dispatch-4 ordering).** This theme's Face-1 RHS is the
  L1 leaf `ls_update_column`, authored concurrently as cycle-027 dispatch-4 and forward-referenced as
  plain text (not yet on disk). Integration MUST land dispatch-4 (the leaf) FIRST so this theme's
  Face-1 link resolves under `linkcheck2`; until then the dep-map row + the in-body Face-1 reference
  are plain text per the rough-in-forward-reference convention. This is the gating reason the theme is
  `rough-in` not `firm`.

- **`trsv` L1 leaf forthcoming (back-solve target).** The terminal back-solve fans into a small-dense
  `trsv`-shaped triangular solve (`iterative.cpp:652-660`); no L1 `trsv` entry exists on disk. This is
  a forward-reference, not a speculative operator (the L0 site is cited + self-verified). A future
  harvester landing an L1 `trsv` leaf would let the back-solve fan-down cite a live link; secondary
  promotion-gate.

- **L1>L0 boundary deferred to `ls_update_column` L1>L0 theme.** This theme stops at the L1 leaves and
  does NOT re-derive the L0 in-place running-QR mechanics (the four `*PlaneRotation` writes to `Hj` /
  `cs` / `sn` / `s`, the back-solve in-place over `s`, the `x.Add` reconstruction). Those are the
  concern of the forthcoming `ls_update_column-mutation-rotation` L1>L0 theme (the leaf's own
  lowering) — mirroring how the sibling defers the in-place `w.Add` to
  `orthogonalize-mutation-rotation`. The `lowering-verifier` audit should confirm this boundary is
  clean (no duplication of the L0 in-place step across the L2>L1 theme and the leaf's L1>L0 theme).

- **L3 sequential-obstruction forecast (replay chain).** The replay sub-step is a length-`j` ordered
  chain of 2-vector updates (`iterative.cpp:634-636`), each reading the previous — the
  [`plane-rotation-stream`](../concepts/plane-rotation-stream.md) §"Sequential character" flags it as a
  `sequential-obstruction` candidate for the eventual L3 iteration rotation (the back-solve's inner
  `k`-recurrence likewise). This is a forward note for a future L3 / L2>L1-vs-L3 lowering pass, NOT
  content of this L2>L1 theme; recorded so the L3 author finds it.

- **OQ `incremental-least-squares-composition-lowering-theme` — RESOLVED by this dispatch.** This
  dispatch authors the theme the firm L2 entry §Dependencies (`book/src/L2/incremental-least-squares.md:334-340`)
  and §Algebraic-laws non-law (`:285`) forward-referenced as "the forthcoming L2>L1 theme". The OQ is
  resolved (the theme is landed at `rough-in`, promotable to `firm` once dispatch-4's `ls_update_column`
  leaf lands). The companion `gmres-givens-stream-as-step-kernel-borderline` OQ was already resolved in
  the negative by the cycle-026 L2 harvest (distinct named composition, not a `krylov-step` axis) — no
  re-litigation here. *Meta-phase action:* migrate the theme OQ to Closed (answer-link
  `book/src/L2-L1/incremental-least-squares-composition-lowering.md`); note the `rough-in` status with
  the dispatch-4 leaf gate.
```

```edit:book/src/L2-L1/index.md
| [orthogonalize-composition-lowering](./orthogonalize-composition-lowering.md) | `L2/orthogonalize` (firm, cycle-019) | `L1/orthogonalize` (firm leaf) + `L1/dot` + `L1/axpy` (firm; `project`▷`subtract` de-fusion) | firm *(algebraic; MGS/CGS/CGS2 variant-dispatch = `[dot,axpy]` sequence selection; inner product cites `dot-mutation-rotation` Sub-pattern D; collective shape `m×1`/`1×m`/`2×m`)* |
| incremental-least-squares-composition-lowering *(rough-in; no anchor yet — gated on dispatch-4 `ls_update_column` leaf landing)* | `L2/incremental-least-squares` (firm, cycle-026) | `ls_update_column` *(forthcoming firm L1 leaf, cycle-027 dispatch-4; plain-text forward-ref)* + `concepts/givens_generate`/`givens_apply` (firm; de-fused 4-sub-step face) + `L2/linear_combination` (firm; back-solve reconstruction) + `trsv` *(forthcoming L1 leaf; back-solve target)* | rough-in *(algebraic; running-QR fan-down `replay▷generate▷apply▷apply_rhs`▷back-solve; FIXED sub-step sequence — replay-before-generate non-commutative load-bearing; two parametric axes `basis_kind∈{V,Z}` + `variant∈{real,complex}`; reduction-path = rotation-ordering + LAPACK scaling, NO MPI collective; proposed-by: abstractor:2026-05-29T175529Z)* |
```

Note for the integrator: the dep-map row above uses **plain-text** for the theme slug and the `ls_update_column` / `trsv` forward-refs (the rough-in-forward-reference convention — the `ls_update_column` L1 anchor does not exist on disk until dispatch-4 lands; `trsv` has no L1 entry). The theme's own chapter file (`incremental-least-squares-composition-lowering.md`) DOES exist on disk after this report applies, so the SUMMARY.md entry below is a live link. Once dispatch-4's `ls_update_column` leaf is on disk, a lifter/finalize may upgrade the dep-map row's theme slug to a live link `[incremental-least-squares-composition-lowering](./incremental-least-squares-composition-lowering.md)` and the `ls_update_column` forward-ref to a live link (skill `upgrade-plain-text-ref-to-live-link-when-target-on-disk`).

```edit:book/src/SUMMARY.md
- [orthogonalize-composition-lowering](./L2-L1/orthogonalize-composition-lowering.md)
- [incremental-least-squares-composition-lowering](./L2-L1/incremental-least-squares-composition-lowering.md)
```

The new SUMMARY entry inserts after the unique `orthogonalize-composition-lowering` line (SUMMARY.md:56), placing the new chapter adjacent to its sibling — the integrator's edit anchor is unambiguous (the `orthogonalize-composition-lowering` SUMMARY line is unique). The theme's own chapter file exists on disk after this report applies, so this live link resolves under `linkcheck2`.