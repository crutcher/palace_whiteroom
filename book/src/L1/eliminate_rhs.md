---
layer: L1
operator: eliminate_rhs
firmness: firm
edges:
  depends-on:
    - L1/apply_linop
    - L1/axpy
    - target: L1-L0/fe-operator-assemble-mutation-rotation
      kind: lowers-to
variant_axes:
  - diagonal-policy
  - bc-data-homogeneity
---

# eliminate_rhs

Mutation-free **inhomogeneous-Dirichlet-data lift into the RHS**: given an assembled linear
operator `K`, the essential (Dirichlet) boundary values `x_bc`, and a right-hand-side vector `b`,
produce the adjusted RHS `b' = b − K·x_bc` with the essential rows of `b'` pinned to the boundary
data (or zero, by diagonal policy). The pure-functional lift of Palace's
`ParOperator::EliminateRHS` (`reference/palace/palace/linalg/rap.cpp:56-82`). A **separable
post-composition** on the assembled operator — it composes AFTER [`fe_assemble`](./fe_assemble.md),
not as part of the assembly fold.

## Context

`eliminate_rhs` is the second half of the standard conforming-FE essential-BC treatment. After the
global operator `K` is assembled by [`fe_assemble`](./fe_assemble.md) and its essential dofs are
pinned by `eliminate_essential_bc` (the L0 `ParOperator::SetEssentialTrueDofs`,
`reference/palace/palace/models/laplaceoperator.cpp:215-217`), an **inhomogeneous** Dirichlet
condition (boundary value `≠ 0`) still contributes a known forcing to the interior equations. That
forcing is the operator applied to the boundary-data extension, `K·x_bc`, and `eliminate_rhs`
subtracts it from the RHS so the reduced system solves for the interior unknowns alone.

The electrostatic witness is `LaplaceOperator::GetExcitationVector`
(`reference/palace/palace/models/laplaceoperator.cpp:225-252`): a unit Dirichlet value is projected
onto the terminal boundary (`ProjectBdrCoefficient`, `:238`), restricted to true dofs into `X`
(`:247`), then `PtAP_K->EliminateRHS(X, RHS)` (`:252`) produces the excitation RHS. This is the L1
`eliminate_rhs(K, x_bc, b)` call with `b = 0` and `x_bc = X`.

`eliminate_rhs` is defined here in **L1 vocabulary** — the operator action `K·x_bc` is an
[`apply_linop`](./apply_linop.md), and the RHS subtraction is an [`axpy`](./axpy.md). The L0
imperative details (the local/true-dof scatter-gather around the operator apply, the in-place
`b.Add`, the diagonal-policy row-pin) are L0 concerns reintroduced by the
[`fe-operator-assemble-mutation-rotation`](../L1-L0/fe-operator-assemble-mutation-rotation.md)
L1>L0 lowering theme (the `eliminate_rhs` leg is folded there — see its §"The `eliminate_rhs` leg
(folded here)"; see *Downward to L0*).

## Signature

```text
eliminate_rhs :: (K: LinearOperator[N, N], x_bc: Tensor[N], b: Tensor[N], policy: DiagonalPolicy)
              -> Tensor[N]

eliminate_rhs(K, x_bc, b, policy) =
  let b'   = axpy(-1, apply_linop(K, restrict_essential(x_bc)), b)   -- b − K·x_bc
      pin  = case policy of DIAG_ONE -> x_bc ; DIAG_ZERO -> 0
  in  set_essential(b', pin)                                         -- BC rows ← pin
```

Shape contract (bunsen-style, named axes):

- `K` — `LinearOperator[N, N]` — the assembled (square) global operator; `N` is the global true-dof
  count `space.GetTrueVSize()` (`reference/palace/palace/fem/fespace.hpp:96`), the axis the
  finite-element space [`fe_space`](./fe_space.md) constructs and defines (the same `N` the essential
  `dbc_tdof_list` indexes). The **unconstrained** operator action is applied (`A->Mult`, the local
  matrix before essential-row elimination — `reference/palace/palace/linalg/rap.cpp:69`). Read-only.
- `x_bc` — `Tensor[N]` — the essential boundary data: a true-dof vector that is the prescribed
  Dirichlet value on essential dofs and arbitrary (masked out) on interior dofs. Only the essential
  entries are read (`SetSubVector(tx, dbc_tdof_list, x)` extracts them onto a zeroed true-dof
  vector, `reference/palace/palace/linalg/rap.cpp:62-64`). Read-only.
- `b` — `Tensor[N]` — the right-hand-side vector to adjust. Read-only at L1 (the L0 form mutates `b`
  in place via `b.Add`; the L1 form returns a fresh value).
- `policy` — `DiagonalPolicy` — `DIAG_ONE` | `DIAG_ZERO`: whether the essential rows of the result
  carry the boundary data (`DIAG_ONE`, paired with a unit operator-diagonal on those rows) or zero
  (`DIAG_ZERO`). The L0 `MFEM_VERIFY` (`reference/palace/palace/linalg/rap.cpp:38-41`) restricts the
  policy to exactly these two.
- result — `Tensor[N]` — the adjusted RHS `b' = (b − K·x_bc)` with essential rows pinned per policy.

`restrict_essential(x_bc)` and `set_essential(·, pin)` are the essential-dof gather/scatter (L0
`linalg::SetSubVector` over `dbc_tdof_list`, `reference/palace/palace/linalg/rap.cpp:64,76,80`); they
are masking projections onto the essential-dof subspace, not separate L1 spine operators (see
*Dependencies*).

## Semantics

`eliminate_rhs(K, x_bc, b, policy)` performs the **inhomogeneous-Dirichlet RHS lift** in three
algebraic steps:

1. **Boundary-data extension and operator apply.** The essential boundary values are extended to a
   full field (the essential entries of `x_bc`, the rest zeroed) and the unconstrained operator is
   applied: `y = K · Eₑ(x_bc)`, where `Eₑ` is the essential-dof masking extension. At L0 this is the
   prolongation `P·tx → lx`, the local apply `A->Mult(lx, ly)`, and the restriction
   `RestrictionMatrixMult(ly, ty)` (`reference/palace/palace/linalg/rap.cpp:65,69,72`); the
   composite local→apply→restrict round-trip is the true-dof operator action `K·x_bc`. At L1 it is
   one [`apply_linop`](./apply_linop.md) (the prolongation/restriction round-trip is the assembled
   operator's own galerkin structure, absorbed into `K` — see *Variant axes*).

2. **RHS subtraction.** `b' = b − y` — one [`axpy`](./axpy.md) with `α = −1`
   (`b.Add(-1.0, ty)`, `reference/palace/palace/linalg/rap.cpp:73`).

3. **Essential-row pin.** The essential rows of `b'` are overwritten with the boundary data
   (`DIAG_ONE`: `set_essential(b', x_bc)`, `reference/palace/palace/linalg/rap.cpp:76`) or zero
   (`DIAG_ZERO`: `set_essential(b', 0)`, `:80`). This makes the pinned system consistent: the
   essential equations become `1·xᵢ = (x_bc)ᵢ` (DIAG_ONE) or `1·xᵢ = 0` (DIAG_ZERO), matching the
   essential-row diagonal that `eliminate_essential_bc` installed on `K`.

The operator is **pure at L1**: the L0 source mutates `b` in place (`b.Add`) and threads scratch
through pooled local/true vectors (`GetLVector` / `GetTVector`,
`reference/palace/palace/linalg/rap.cpp:59-62,71`); the L1 form returns a fresh value. Those
mutations and the workspace pooling are L0 concerns reintroduced by the L1>L0 lowering theme.

## Algebraic laws

Write `Eₑ` for the essential-dof masking extension (`restrict_essential`), `Pₑ` for the
essential-row pin-projection (`set_essential(·, ·)` overwrites the essential rows), and `Iₑ̄` for the
complementary interior identity, so that on interior dofs the result equals `b − K·x_bc` and on
essential dofs it equals the pin. The laws hold treating `K` as an opaque
[`apply_linop`](./apply_linop.md) operator and the masks as fixed projections.

1. **Additive linearity in the RHS** (homogeneous BC fixed): for fixed `x_bc` and `policy`, on the
   interior dofs `eliminate_rhs(K, x_bc, b₁ + b₂) = eliminate_rhs(K, x_bc, b₁) + (b₂ on interior)`;
   more precisely the interior block is affine in `b` with unit gradient —
   `Iₑ̄ · eliminate_rhs(K, x_bc, b) = Iₑ̄·b − Iₑ̄·K·Eₑ(x_bc)`. The essential block is constant in `b`
   (overwritten by the pin), so the full map is **not** linear in `b` (the pin breaks it); it is
   affine on the interior block. (L0: the interior rows receive only `b.Add(-1.0, ty)`,
   `reference/palace/palace/linalg/rap.cpp:73`, untouched by the subsequent `SetSubVector` which
   writes essential rows only.)

2. **Linearity in the boundary data** (interior block; `b` and `policy` fixed): the forcing
   correction is linear in `x_bc` — `eliminate_rhs(K, α·x_bc, b)` differs from
   `eliminate_rhs(K, x_bc, b)` on the interior by `−(α−1)·K·Eₑ(x_bc)`. The correction term
   `−K·Eₑ(x_bc)` is `apply_linop` ∘ `Eₑ` applied to `x_bc`, both linear, so the interior correction
   is linear in `x_bc`. (The essential block under `DIAG_ONE` is `Pₑ(x_bc) = α·(x_bc on essential)`,
   also linear; under `DIAG_ZERO` it is constant zero.)

3. **Homogeneous-BC identity** (interior block): when `x_bc = 0` on essential dofs,
   `K·Eₑ(0) = 0`, so `eliminate_rhs(K, 0, b) = b` on the interior and `= 0`/`b`-pinned on essential
   (DIAG_ZERO/DIAG_ONE both pin to 0). The RHS lift is a **no-op on the interior for homogeneous
   Dirichlet data** — the whole operator collapses to the essential-row pin. This is the
   `bc-data-homogeneity` variant axis (see *Variant axes*).

4. **Separable post-composition with `fe_assemble`** (the load-bearing framing law): `eliminate_rhs`
   composes with the assembly fold as `eliminate_rhs(fe_assemble(space, terms), x_bc, b, policy)` —
   it consumes the *already-assembled* operator `K` and is independent of HOW `K` was assembled. It
   is **not** distributive over the assembly fold (`eliminate_rhs(K₁ + K₂, ...)` is NOT
   `eliminate_rhs(K₁, ...) + eliminate_rhs(K₂, ...)` — the pin would be applied twice and the `b`
   carried twice). The correct statement is that `eliminate_rhs` is a post-composition on the
   assembled-operator value, valid for any `K`; it sits **after** the `fe_assemble` fold in the
   pipeline, not inside it. (This is the sibling-side statement of `fe_assemble` law-list item
   "BC-elimination is NOT part of the fold", `book/src/L1/fe_assemble.md:145-150`.)

Laws that explicitly **do not** hold:

- **Not linear in `b` as a whole map**: the essential-row pin (`Pₑ`) overwrites rather than adds,
  so the full `b ↦ eliminate_rhs(K, x_bc, b)` is affine-on-interior + constant-on-essential, not
  linear. Linearity is recovered only on the interior block (law 1).
- **Not idempotent**: applying `eliminate_rhs` twice subtracts `K·x_bc` twice on the interior
  (`b'' = b' − K·x_bc = b − 2·K·x_bc` on interior), so `eliminate_rhs ∘ eliminate_rhs ≠
  eliminate_rhs` for inhomogeneous data. It is a one-shot RHS preparation, not a projector.
- **No SPD / invertibility precondition on `K`**: `eliminate_rhs` applies `K` opaquely; it carries
  no symmetry or definiteness requirement (the witness diffusion `K` is SPD only after BC
  elimination, but `eliminate_rhs` does not rely on that).

## Dependencies

`eliminate_rhs` is defined over two firm L1 spine operators plus an essential-dof masking projection:

- [`apply_linop`](./apply_linop.md) (direct) — the unconstrained operator action `K·x_bc`
  (`A->Mult(lx, ly)`, `reference/palace/palace/linalg/rap.cpp:69`). The prolongation/restriction
  round-trip wrapping the local apply (`:65,72`) is the assembled operator's galerkin true-dof
  action, absorbed into `K` at L1 (see *Variant axes*).
- [`axpy`](./axpy.md) (direct) — the RHS subtraction `b ← b − K·x_bc` with `α = −1`
  (`b.Add(-1.0, ty)`, `reference/palace/palace/linalg/rap.cpp:73`).
- `set_subvector` / essential-dof mask (concept, NOT a spine operator) — the gather
  `restrict_essential(x_bc)` (`reference/palace/palace/linalg/rap.cpp:64`) and the scatter/pin
  `set_essential(b', pin)` (`:76,80`), both `linalg::SetSubVector` over the essential-dof index list
  `dbc_tdof_list`. These are masking projections onto the essential-dof subspace: the gather (`:64`,
  writes `x`) and the `DIAG_ONE` pin (`:76`, writes the boundary data) are the **general**
  `set_subvector` write-mask, of which the `DIAG_ZERO` arm (`:80`, writes zero) is exactly the
  zeroing special case `set_subvector_zero` that [`divfree_projector`](./divfree_projector.md)
  §Dependencies names (`concepts/set_subvector_zero.md`). Reused here as the essential-dof pin, they
  do not introduce a new spine operator.

It depends on no FE-assembly vocabulary — `K` enters as an opaque assembled `LinearOperator[N, N]`,
which is why `eliminate_rhs` is a **separable post-composition** that does not need `fe_assemble`'s
term-list machinery.

## Variant axes

- **diagonal-policy**: `DIAG_ONE` (essential rows pinned to the boundary data `x_bc`, paired with a
  unit operator-diagonal) | `DIAG_ZERO` (essential rows pinned to zero). The L0 branch
  (`reference/palace/palace/linalg/rap.cpp:74-81`) selects by the operator's stored `diag_policy`;
  the `MFEM_VERIFY` at `:38-41` restricts the policy to exactly these two values. The interior block
  (`b − K·x_bc`) is identical across both; the policy affects only the essential-row pin value.
- **bc-data-homogeneity**: `homogeneous` (`x_bc = 0` on essential dofs — the interior correction
  `K·x_bc = 0` vanishes, per law 3; the operator collapses to the essential-row pin) | `inhomogeneous`
  (`x_bc ≠ 0` — the full `b − K·x_bc` lift fires). The electrostatic witness
  (`reference/palace/palace/models/laplaceoperator.cpp:238`) is inhomogeneous (unit terminal value).
- **operator-true-dof-representation** (absorbed): the L0 source applies `K` via a
  prolongation→local-apply→restriction round-trip (`reference/palace/palace/linalg/rap.cpp:65,69,72`)
  because the assembled `ParOperator` stores a *local* matrix `A` and the galerkin `Pᵀ A P` action is
  realized on the fly. At L1 the operator `K` is the true-dof operator and `apply_linop(K, x_bc)` is
  its action directly; the round-trip is the L0 realization of one `apply_linop`, absorbed (not a
  distinct algebraic step).

## Vocabulary closure

`eliminate_rhs`'s definition, signature, and all four algebraic laws are stated entirely in
**existing firm-spine vocabulary** — [`apply_linop`](./apply_linop.md) for the operator action
`K·x_bc`, [`axpy`](./axpy.md) for the RHS subtraction `b − K·x_bc`, and the already-named
`set_subvector` essential-dof masking projection (shared with
[`divfree_projector`](./divfree_projector.md)) for the gather/pin. The body needs **no vocabulary the
spine lacks**: the L0 prolongation/restriction round-trip is the assembled operator's own true-dof
action (absorbed into `apply_linop`), and the diagonal-policy branch is a parameter on the
essential-row pin, not a new primitive. Source line-by-line: `SetSubVector` gather `:64` →
prolongation `:65` → `A->Mult` (apply_linop) `:69` → restriction `:72` → `b.Add(-1.0, ·)` (axpy)
`:73` → diagonal-policy pin `:74-81`.

The only sub-step that is not a named spine operator is the essential-dof mask (`SetSubVector` over
`dbc_tdof_list`). This is NOT a spine gap — it is the general `set_subvector` write-mask, whose
zeroing special case `divfree_projector` names and uses as `set_subvector_zero`
(`concepts/set_subvector_zero.md`): the `DIAG_ZERO` pin arm is exactly that zeroing case, while the
gather and the `DIAG_ONE` pin are its general (boundary-data-writing) form. Reusing it as the
essential-dof pin introduces no new vocabulary.

This is the **firm-on-positive-structure** situation: every law is a syntactic identity on the
fully-specified positive source body (`reference/palace/palace/linalg/rap.cpp:56-82`), so the absence
of a dedicated `eliminate_rhs` unit test does not gate them.

## L1 vs L0 distinction

- **L0**: imperative in-place RHS mutation with pooled scratch. Gather essential values onto a zeroed
  pooled true-dof vector (`tx`, `reference/palace/palace/linalg/rap.cpp:62-64`), prolong to a pooled
  local vector (`lx`, `:65`), apply the local matrix into a pooled local output (`ly`, `:69`),
  restrict to a pooled true-dof vector (`ty`, `:71-72`), mutate `b` in place by `b.Add(-1.0, ty)`
  (`:73`), then overwrite `b`'s essential rows in place by `SetSubVector` (`:76` or `:80`). State is
  threaded through five pooled MFEM vectors and the mutated `b`.
- **L1**: pure functional post-composition. `b' = eliminate_rhs(K, x_bc, b, policy)`. No pooled
  scratch, no in-place `b` mutation; the operator action is one `apply_linop`, the subtraction one
  `axpy`, the pin one `set_subvector` scatter. The L0 prolongation/restriction round-trip, the
  vector pooling (`GetLVector`/`GetTVector`), and the in-place `Add` are all L1>L0 lowering concerns.

## Evidence

- `reference/palace/palace/linalg/rap.cpp:56-82` — `ParOperator::EliminateRHS`: the full L0 body.
  Essential gather `linalg::SetSubVector(tx, dbc_tdof_list, x)` (`:64`); prolongation
  `GetProlongationMatrix()->Mult(tx, lx)` (`:65`); **unconstrained operator apply** `A->Mult(lx, ly)`
  (`:69`, the `apply_linop`); restriction `RestrictionMatrixMult(ly, ty)` (`:72`); **RHS subtraction**
  `b.Add(-1.0, ty)` (`:73`, the `axpy` with `α = −1`); diagonal-policy essential-row pin
  `SetSubVector(b, dbc_tdof_list, x | 0.0)` (`:74-81`).
- `reference/palace/palace/linalg/rap.cpp:38-41` — the `MFEM_VERIFY` restricting the diagonal policy
  to `DIAG_ONE` | `DIAG_ZERO` (the `diagonal-policy` variant axis is exactly two-valued).
- `reference/palace/palace/linalg/rap.hpp:97-99` — the `EliminateRHS` declaration + doc-comment
  ("Eliminate essential true dofs from the RHS vector b, using the essential boundary condition
  values in x") — confirms the (x_bc, b) argument roles.
- `reference/palace/palace/models/laplaceoperator.cpp:225-252` — `LaplaceOperator::GetExcitationVector`:
  the electrostatic witness call site. Unit Dirichlet projection (`ProjectBdrCoefficient(one, ...)`,
  `:238`), restriction to true dofs `x.ParallelProject(X)` (`:247`), then
  `PtAP_K->EliminateRHS(X, RHS)` (`:252`) — the `eliminate_rhs(K, x_bc=X, b=0)` inhomogeneous lift.
- `book/src/L1/fe_assemble.md:145-150` — the sibling firm `fe_assemble` law-list statement that
  BC-elimination (`eliminate_essential_bc` + `eliminate_rhs`) is a **separable post-composition**,
  NOT part of the assembly fold — the upstream side of `eliminate_rhs` law 4.
- `book/src/L1/apply_linop.md` — the operator-action dependency (`K·x_bc`).
- `book/src/L1/axpy.md` — the RHS-subtraction dependency (`b − K·x_bc`).
- `book/src/L1/divfree_projector.md` — the `set_subvector` essential-dof-mask concept reuse precedent.

## Downward to L0

The lowering is **folded into**
[`fe-operator-assemble-mutation-rotation`](../L1-L0/fe-operator-assemble-mutation-rotation.md) — the
firm L1>L0 theme that lowers the whole FE-operator construction surface (the `fe_assemble` fold +
both separable BC-elimination legs). The `eliminate_rhs` leg is its own named sub-section there,
§"The `eliminate_rhs` leg (folded here)", which narrates how this L1 post-composition lowers into
Palace's in-place RHS-mutation protocol: gather essential values onto pooled scratch
(`rap.cpp:62-63`) → prolong (`:64`) → apply local matrix (`A->Mult`, `:69`) → restrict (`:72`) →
in-place `b.Add(-1.0, ·)` (`:73`) → in-place essential-row `SetSubVector` pin (`:76`/`:80`), with the
prolongation/restriction round-trip realizing the single `apply_linop`. It shares that theme with the
operator-side leg `eliminate_essential_bc` — both BC-treatment post-compositions lower in one theme
on the shared `GetExcitationVector`/`GetStiffnessMatrix` witness. There is **no** dedicated
`eliminate-rhs-mutation-rotation` sibling theme — a degenerate split would be an anti-mirror smell.
