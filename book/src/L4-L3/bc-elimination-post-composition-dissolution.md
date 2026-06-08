---
layer: L4-L3
theme: bc-elimination-post-composition-dissolution
firmness: firm
justification_kind: structural
# Graded-stack scheme: lowering theme. This theme dissolves the L4 eliminate_bc
# verb-pair DIRECTLY to its two L1 sources (no interposed L3/eliminate_bc entry —
# warranted on-disk at :105,:114-121). rank = min(endpoints); both endpoints firm
# (rank 3) and the L4 source is firm, so the theme is firm. rank(theme) <= min holds.
rank: firm
edges:
  depends-on:
    - target: L4/eliminate_bc
      kind: lifts-from            # the L4 source verb-pair this theme lowers (the LHS)
    - target: L1/eliminate_essential_bc
      kind: lowers-to             # operator-side: deferred-config-then-apply (:35)
    - target: L1/eliminate_rhs
      kind: lowers-to             # RHS-side: in-place pooled-scratch loop (:59-61)
    - target: L1-L0/fe-operator-assemble-mutation-rotation
      kind: lowers-to             # the operator-pin L1>L0 half this L4>L3 half composes with
  reference:
    - L4/eliminate_bc
    - L1/essential_dofs           # the DofSet[N] consumed as a given operand (:99-101; own construction theme)
    - L4-L3/fe-assemble-fold-dissolution   # the assemble-fold sibling theme
---

# bc-elimination-post-composition-dissolution

The L4>L3 dissolution of the [`eliminate_bc`](../L4/eliminate_bc.md) post-assembly BC-application
verb-pair into Palace's imperative BC staging. **Substantive** (not identity-in-form): the two pure
post-compositions collapse to a **deferred-config-then-apply** operator pin and an **in-place pooled-
scratch** RHS-mutation loop.

## Context

A lowering theme rewrites an L4 form of shape A into an L3 form of shape B. The
[`eliminate_bc`](../L4/eliminate_bc.md) L4 surface is the pure post-assembly Dirichlet-BC verb-pair
`(eliminate_essential_bc, eliminate_rhs)` over the `readonly` `(DofSet[N], DiagPolicy)` BC stratum;
this theme narrates how it lowers (L4→L3 direction, per high→low discipline) into the L3 imperative
staging Palace actually writes.

This is the **post-composition sibling** of the [`fe-assemble-fold-dissolution`](./fe-assemble-fold-dissolution.md)
theme: where `fe-assemble-fold-dissolution` lowers the assemble FOLD that builds `K`, this theme lowers
the BC verb-pair that post-composes on the assembled `K` (the operator pin) and the `(K, b)` pair (the
RHS lift). The two themes together cover the assemble + BC-application halves of the FE-operator
construction surface.

## LHS (L4) → RHS (L3)

### Operator-side: `eliminate_essential_bc` → deferred-config-then-apply

The L4 pure post-composition `K' = eliminate_essential_bc K dofs policy` (zero essential rows/cols, set
the eliminated diagonal per policy; the linear free-block projection `K ↦ P_F K P_F` under DIAG_ZERO)
dissolves to the L3 **two-step on a mutable `ParOperator` wrapper**:

1. **Record** the `(dofs, policy)` BC stratum on the wrapper — `SetEssentialTrueDofs(tdof_list, policy)`
   stores `dbc_tdof_list` + `diag_policy` (`palace/linalg/rap.cpp:36-47`, the `:45-46` writes; guards
   `policy ∈ {DIAG_ONE, DIAG_ZERO}` `:39-41` and squareness `:42-43`). The L4 `readonly` BC stratum
   captured once dissolves to this deferred mutation of the wrapper's `dbc_tdof_list`/`diag_policy`
   members.
2. **Apply** at parallel-assemble time — `RAP->EliminateBC(dbc_tdof_list, diag_policy)`
   (`palace/linalg/rap.cpp:139-148`, the call at `:143` guarded square `:141`) mutates the assembled
   `HypreParMatrix` **in place** (zero rows/cols + set diagonal per policy). The L4 fresh-value-returning
   post-composition dissolves to this destructive matrix mutation; the rectangular case is a hard L0
   reject (`:145-148`).

Substantive: the pure value-returning post-composition → a deferred-config record + an in-place matrix
mutation, the `readonly` BC stratum → mutable wrapper state, the squareness precondition → an
`MFEM_VERIFY` guard + a rectangular-reject branch. The operator-pin L1→L0 half is carried by the
[`fe-operator-assemble-mutation-rotation`](../L1-L0/fe-operator-assemble-mutation-rotation.md) theme
(which narrates the FE-assembly build-up-then-assemble protocol + the separable BC-elimination
post-compositions).

### RHS-side: `eliminate_rhs` → in-place pooled-scratch loop

The L4 pure post-composition `b' = eliminate_rhs K x_bc b policy` (`b − K·x_bc` then pin the essential
rows; one `apply_linop` + one `linear_combination` + one essential-row scatter) dissolves to the L3
**in-place RHS mutation with pooled scratch** (`palace/linalg/rap.cpp:56-83`):

- gather essential values onto a zeroed pooled true-dof vector `tx` (`SetSubVector(tx, dbc_tdof_list,
  x)`, `:62-64`) → prolong to a pooled local vector `lx` (`:65`) → apply the local matrix into a pooled
  local output `ly` (`A->Mult(lx, ly)`, `:69`, the `apply_linop`) → restrict to a pooled true-dof
  vector `ty` (`:71-72`);
- mutate `b` **in place** by `b.Add(-1.0, ty)` (`:73`, the `linear_combination [(1,b),(-1,y)]` / axpy
  with `α = −1`);
- overwrite `b`'s essential rows **in place** by `SetSubVector` (`:74-81`, the diagonal-policy pin —
  `x` for DIAG_ONE `:76`, `0.0` for DIAG_ZERO `:80`).

Substantive: the pure value-returning post-composition → an in-place `b` mutation threaded through five
pooled MFEM vectors, the single logical `apply_linop` → the prolongation→local-apply→restriction
round-trip (the assembled operator's galerkin true-dof action realized on the fly), the
`linear_combination` → the in-place `b.Add`, the essential-row pin → an in-place `SetSubVector`. The
RHS-side L1→L0 half is folded into the firm
[`fe-operator-assemble-mutation-rotation`](../L1-L0/fe-operator-assemble-mutation-rotation.md) theme
(§"The `eliminate_rhs` leg (folded here)") — there is no separate `eliminate-rhs-mutation-rotation`
theme (disposition FOLD); see `L1/eliminate_rhs.md` §"Downward to L0".

## What does NOT change in the rotation

The **separable post-composition position** survives the rotation unchanged — both verbs still consume
the *already-assembled* operator value and run AFTER the assemble fold, never inside it (the L4 cap's
law 8; the L3 staging is likewise applied after assembly, at parallel-assemble time for the operator
pin, at excitation-vector-build time for the RHS lift). The **free/essential block structure** survives
(the operator pin still touches only essential rows/cols; the RHS lift still affects the interior block
by `b − K·x_bc` and the essential block by the pin). The **diagonal-policy semantics** survive
(DIAG_ONE solve-side, DIAG_ZERO energy-block; identical row/col-zeroing). The verbs carry **NO
`sequential-obstruction`** — they are one-shot post-compositions, not iterations (the contrast with
`fold_solve`'s carry-threaded sweep).

## What this lowering does NOT cover

- **The assemble fold that builds `K`** — that is the [`fe-assemble-fold-dissolution`](./fe-assemble-fold-dissolution.md)
  theme. This theme lowers only the BC post-compositions ON the assembled `K`.
- **The `DofSet[N]` construction** — the boundary-attribute → essential-true-dof-set build is the firm
  L1 [`essential_dofs`](../L1/essential_dofs.md), lowered by its own
  `essential-dofs-construction-rotation` L1>L0 theme. This theme consumes `DofSet[N]` as a given operand.
- **The libCEED/MFEM kernel interiors** — the `EliminateBC` HYPRE matrix mutation and the prolongation/
  restriction MFEM operators are library-owned (out of scope per CLAUDE.md §Target-system — "cite
  Palace source, not vendored upstream"); the theme records Palace's CALLs, not the library bodies.
- **The L3>L2 hop.** There is **no standalone `L3/eliminate_bc` entry warranted** — the BC verb-pair
  carries no `sequential-obstruction` (one-shot post-compositions; nothing to iterate-rotate), so its
  L3 image is the imperative staging described above, homed here. This matches the
  `solve-family-map-dissolution` / `fe-assemble-fold-dissolution` NO-ENTRY pattern: a standalone L3
  chapter would mirror this theme's RHS (the §1d anti-mirror smell). This L4>L3 theme is the
  **authoritative downward home** for the BC-application post-composition pair.

## L3-entry-vs-dissolution-home verdict

**WARRANT-FIRST: DISSOLUTION-HOME (no interposed `L3/eliminate_bc` entry).** The decision criterion (per
the `fold_solve` L3-ENTRY vs `solve_family` / `fe_assemble` NO-ENTRY precedents): does the
L3 image carry a `sequential-obstruction` or `partial-obstruction` warranting a standing iteration-
rotation chapter? **No** — the BC verb-pair lowers to two one-shot imperative stagings (a deferred-
config-then-apply operator mutation + an in-place pooled-scratch RHS mutation), neither an iteration.
There is no loop to rotate, no carry to thread, no obstruction to render. A standalone `L3/eliminate_bc`
would be a degenerate identity-in-named-terms restatement of this theme's RHS — the vocabulary-shift-
redirect anti-mirror smell. This theme is the authoritative L3-form home.

## Evidence

- `palace/linalg/rap.cpp:36-47` — `SetEssentialTrueDofs` (the operator-side deferred-config record;
  `:45-46` writes, `:39-43` guards).
- `palace/linalg/rap.cpp:139-148` — the `EliminateBC` in-place apply (`:143` call, `:141` square guard,
  `:145-148` rectangular reject).
- `palace/linalg/rap.cpp:56-83` — `EliminateRHS` (the RHS-side in-place pooled-scratch loop: gather
  `:64`, prolong `:65`, apply `:69`, restrict `:72`, in-place `b.Add(-1.0,·)` `:73`, in-place pin
  `:74-81`).
- `book/src/L4/eliminate_bc.md` — the LHS L4 verb-pair (the eight laws this theme's RHS realizes; the
  in-line §"Lowers to" rotation direction).
- `book/src/L1/eliminate_essential_bc.md` / `book/src/L1/eliminate_rhs.md` — the firm L1 sources; their
  §"L1 vs L0 distinction" + §"Downward to L0" prose is the L1→L0 half this theme's L4→L3 half composes
  with.
- `book/src/L1-L0/fe-operator-assemble-mutation-rotation.md` — the operator-side L1>L0 theme (the
  build-up-then-assemble protocol + the separable BC-elimination post-compositions).
