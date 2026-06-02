---
agent: harvester
invoked_at: 2026-06-02T010700Z
scope: L1 operator: eliminate_rhs
status: integrated
integrated_at: 2026-06-02T034000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "D3 cycle-055. Applied clean — new book/src/L1/eliminate_rhs.md (firm L1, b'=b−K·x_bc, essential rows pinned per diagonal policy; firm-on-positive-structure, separable post-composition after fe_assemble) + L1/index :74 bullet rough-in→firm + dep-map row + SUMMARY. L1 firm 27→28 (with D4 → 29). Repairer pre-applied :248→:247 witness-drift + orphan-fence fixes."
inputs:
  - dispatch D3 cycle-055 (batch-17, VOCABULARY-SHIFT REDIRECT 2026-06-01)
  - rough-in bullet book/src/L1/index.md:74 (eliminate_rhs, no anchor yet)
  - L0 anchors (pre-supplied): reference/palace/palace/linalg/rap.cpp:56-82 (ParOperator::EliminateRHS); reference/palace/palace/models/laplaceoperator.cpp:252 (call site)
  - sibling firm entry book/src/L1/fe_assemble.md (cycle-054; separable-post-composition framing)
  - cycle-053 D3 judgment (body is apply_linop+axpy, firm-spine vocabulary)
---

# CYCLE: Formalize eliminate_rhs at L1

## Summary

`eliminate_rhs` is the inhomogeneous-Dirichlet-data lift into the RHS: given an assembled
linear operator `K`, the essential-dof boundary values, and a RHS vector `b`, it adjusts
`b ← b − K·x_bc` (then pins the essential rows of `b` to the BC values or zero by diagonal
policy). It is currently a `rough-in (no anchor yet)` plain-text bullet at
`book/src/L1/index.md:74`. The L0 body (`ParOperator::EliminateRHS`,
`reference/palace/palace/linalg/rap.cpp:56-82`) lifts **cleanly** in firm-spine vocabulary:
one `apply_linop` (`A->Mult`, `:69`) composed with one `axpy` (`b.Add(-1.0, ty)`, `:73`),
bracketed by essential-dof scatter/gather (`SetSubVector` + prolongation/restriction). It is a
**separable post-composition** on the assembled operator — it composes AFTER `fe_assemble`, is
NOT part of the assembly fold. **Clean-gate call: PROMOTE — clean.** This report lands
`book/src/L1/eliminate_rhs.md` as `firm`, flips the index bullet + dep-map row to firm, registers
the SUMMARY chapter, and forward-references a (not-yet-authored) L1>L0 lowering theme in plain text.

## Proposed changes

```new:book/src/L1/eliminate_rhs.md
---
layer: L1
operator: eliminate_rhs
firmness: firm
lowers_to:
  - L1-L0/eliminate-rhs-mutation-rotation
lifts_from: []
depends_on:
  - apply_linop
  - axpy
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
`eliminate-rhs-mutation-rotation` L1>L0 lowering theme (forthcoming; see *Downward to L0*).

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
  count. The **unconstrained** operator action is applied (`A->Mult`, the local matrix before
  essential-row elimination — `reference/palace/palace/linalg/rap.cpp:69`). Read-only.
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
  zeroing special case `set_subvector_zero` that [`divfree-projector`](./divfree-projector.md)
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

## Status

`firm`. **Clean-gate call: PROMOTE — clean.** The operator's definition, signature, and all four
algebraic laws are stated entirely in **existing firm-spine vocabulary** —
[`apply_linop`](./apply_linop.md) for the operator action `K·x_bc`, [`axpy`](./axpy.md) for the RHS
subtraction `b − K·x_bc`, and the already-named `set_subvector` essential-dof masking projection
(shared with [`divfree-projector`](./divfree-projector.md)) for the gather/pin. The body needs **no
vocabulary the spine lacks**: the L0 prolongation/restriction round-trip is the assembled operator's
own true-dof action (absorbed into `apply_linop`), and the diagonal-policy branch is a parameter on
the essential-row pin, not a new primitive.

This is the **firm-on-positive-structure** situation (the `apply_linop` / BLAS-1-leaf /
`fe_assemble` no-dedicated-test precedent): every law is a syntactic identity on the fully-specified
positive source body (`reference/palace/palace/linalg/rap.cpp:56-82`), so the absence of a dedicated
`eliminate_rhs` unit test does not gate them. The cycle-053 D3 judgment (the body is
`apply_linop`+`axpy`, firm-spine vocabulary) is confirmed against source line-by-line:
`SetSubVector` gather `:64` → prolongation `:65` → `A->Mult` (apply_linop) `:69` → restriction `:72`
→ `b.Add(-1.0, ·)` (axpy) `:73` → diagonal-policy pin `:74-81`.

**Clean-gate honesty note**: the only sub-step that is not a named spine operator is the essential-dof
mask (`SetSubVector` over `dbc_tdof_list`). This is NOT a spine gap — it is the general
`set_subvector` write-mask, whose zeroing special case `divfree-projector` already names and uses as
`set_subvector_zero` (`concepts/set_subvector_zero.md`): the `DIAG_ZERO` pin arm is exactly that
zeroing case, while the gather and the `DIAG_ONE` pin are its general (boundary-data-writing) form.
Reusing it as the essential-dof pin introduces no new vocabulary. The clean-gate is met.

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
- `book/src/L1/divfree-projector.md` — the `set_subvector` essential-dof-mask concept reuse precedent.

## Downward to L0

The lowering is the (forthcoming) `eliminate-rhs-mutation-rotation` L1>L0 theme — NOT yet authored
(no `book/src/L1-L0/eliminate-rhs-mutation-rotation.md` exists; referenced here in plain text per the
missing-anchor convention). It will narrate how this L1 post-composition lowers into Palace's
in-place RHS-mutation protocol: gather essential values onto pooled scratch → prolong → apply local
matrix → restrict → in-place `b.Add(-1.0, ·)` → in-place essential-row `SetSubVector` pin, with the
prolongation/restriction round-trip realizing the single `apply_linop`. It is a **sibling theme** to
the `eliminate-essential-bc-mutation-rotation` lowering (the operator-side BC pin) — both lower the
separable BC-treatment post-compositions that `fe-operator-assemble-mutation-rotation` references but
does not contain.
```

```edit:book/src/L1/index.md
- `eliminate_rhs` *(rough-in; no anchor yet)* — lift inhomogeneous Dirichlet data into the RHS (L0: `ParOperator::EliminateRHS`, `palace/linalg/rap.cpp:56-82`) (proposed-by: abstractor:2026-06-01T235200Z-abstractor-fe-assembly-thread-opener).
```
↓ replace with ↓
```
- **`eliminate_rhs` is now FIRM** (cycle-055) — see [`eliminate_rhs`](./eliminate_rhs.md). Lift inhomogeneous Dirichlet data into the RHS as the separable post-composition `b' = b − K·x_bc` (essential rows pinned per diagonal policy); clean-gate PROMOTE (the body is `apply_linop`(`A->Mult`, `palace/linalg/rap.cpp:69`) + `axpy`(`b.Add(-1.0,·)`, `:73`) + the `set_subvector` essential-dof pin (`:64,76,80`) — entirely firm-spine vocabulary, no spine gap). **Separable post-composition**, NOT part of the `fe_assemble` fold — it consumes the already-assembled `K` (witness `laplaceoperator.cpp:252`). Laws: interior-block linearity in `b` and in `x_bc`, homogeneous-BC interior identity, separable-post-composition-with-`fe_assemble`; non-laws: not linear-in-`b`-as-a-whole (the pin overwrites), not idempotent. L1>L0 lowering `eliminate-rhs-mutation-rotation` forthcoming (plain text — theme not yet authored).
```

(Dep-map table — append a new row after the `floquet-correction` row at `book/src/L1/index.md:111`:)
```
| [`eliminate_rhs`](./eliminate_rhs.md) | `(K: LinearOperator[N, N], x_bc: Tensor[N], b: Tensor[N], policy: DiagonalPolicy) → Tensor[N]` (i.e. `b − K·x_bc`, essential rows pinned per policy) | `apply_linop` (direct, `K·x_bc`), `axpy` (direct, `b − K·x_bc`); `set_subvector` (concept, essential-dof gather/pin — shared with `divfree-projector`, NOT a spine dep) | `firm` (FE essential-BC RHS-lift; separable post-composition on the assembled operator, NOT part of the `fe_assemble` fold; L0: `palace/linalg/rap.cpp:56-82` + witness `palace/models/laplaceoperator.cpp:225-252`; harvested cycle-055; firm-on-positive-structure, no-dedicated-test caveat non-gating per `fe_assemble`/`apply_linop` precedent; diagonal-policy + bc-data-homogeneity variant axes; interior-block-only linearity, not-idempotent non-laws) |
```

```edit:book/src/SUMMARY.md
- [floquet-correction](./L1/floquet-correction.md)
```
↓ replace with (append the new chapter after floquet-correction under the L1 Part) ↓
```
- [floquet-correction](./L1/floquet-correction.md)
- [eliminate_rhs](./L1/eliminate_rhs.md)
```

## Operator content

(Authored in full inside the `new:book/src/L1/eliminate_rhs.md` block above. Summary of the firm apparatus:)

- **Slug + one-line**: `eliminate_rhs` — inhomogeneous-Dirichlet-data lift into the RHS, `b' = b − K·x_bc`, essential rows pinned per diagonal policy; a separable post-composition on the assembled operator.
- **Signature**: `eliminate_rhs :: (K: LinearOperator[N, N], x_bc: Tensor[N], b: Tensor[N], policy: DiagonalPolicy) -> Tensor[N]`, defined as `set_essential(axpy(-1, apply_linop(K, restrict_essential(x_bc)), b), pin)`.
- **Semantics**: three steps — operator apply `K·x_bc` (`apply_linop`), RHS subtraction `b − K·x_bc` (`axpy`, α = −1), essential-row pin (`set_subvector`).
- **Algebraic laws**: (1) interior-block linearity in `b`; (2) interior-block linearity in `x_bc`; (3) homogeneous-BC interior identity; (4) separable post-composition with `fe_assemble`. Non-laws: not linear-in-`b`-as-a-whole (pin overwrites), not idempotent, no SPD precondition.
- **Dependencies**: `apply_linop` (direct), `axpy` (direct), `set_subvector` (concept, NOT a spine dep).
- **Status**: `firm` — clean-gate PROMOTE.
- **Evidence**: `reference/palace/palace/linalg/rap.cpp:56-82` (body), `:38-41` (policy verify), `rap.hpp:97-99` (decl), `laplaceoperator.cpp:225-252` (witness call site).

## Supporting evidence

- **L0 body verified on-disk line-by-line** (codemap `read_range` drifted +2 vs on-disk on the comment/brace boundary — the documented `codemap-read-range-plus-one-drift-on-brace-boundary` friction; citecheck/on-disk truth used for all emitted line numbers):
  - `:64` `linalg::SetSubVector(tx, dbc_tdof_list, x)` — essential gather
  - `:65` `GetProlongationMatrix()->Mult(tx, lx)` — prolongation
  - `:69` `A->Mult(lx, ly)` — unconstrained apply (**`apply_linop`**)
  - `:72` `RestrictionMatrixMult(ly, ty)` — restriction
  - `:73` `b.Add(-1.0, ty)` — RHS subtraction (**`axpy`**, α = −1)
  - `:74-81` diagonal-policy `SetSubVector` essential-row pin
- citecheck pass: `rap.cpp:54-82 --anchor EliminateRHS` ok; `rap.cpp:60-66 --anchor SetSubVector` ok; `laplaceoperator.cpp:225-252 --anchor GetExcitationVector` ok; `laplaceoperator.cpp:252 --anchor EliminateRHS` ok.
- Sibling firm `book/src/L1/fe_assemble.md:145-150` independently names the separable-post-composition framing (the upstream side of law 4).
- cycle-053 D3 judgment (body is `apply_linop`+`axpy`) confirmed against source.

## Index-registration partition (per role-spec)

- (1) **Dep-map table row** — authored above (mine; appended after the `floquet-correction` row).
- (2) **§Vocabulary-cohort bullet** — authored above (mine; the FE-assembly sub-spine bullet flipped rough-in → firm at `index.md:74`).
- (3) **Consolidated cohort-header count** (the FE-cohort subsection-header tally at `book/src/L1/index.md:70`, D7-owned this cycle) — **DEFERRED to D7**. I did NOT touch the `:70` header.
- SUMMARY.md chapter registration — authored above (mine).

## Open questions / caveats

- **L1>L0 lowering theme `eliminate-rhs-mutation-rotation` is not yet authored** — forward-referenced
  in plain text per the missing-anchor convention. A follow-on abstractor pass should author it as a
  sibling to the `eliminate-essential-bc-mutation-rotation` theme (both lower the separable BC-treatment
  post-compositions that `fe-operator-assemble-mutation-rotation` references). When that theme lands,
  the plain-text refs in `eliminate_rhs.md` §Downward and the index bullet upgrade to live links.
- **`eliminate_essential_bc` sibling is still rough-in** (`book/src/L1/index.md:73`, no anchor yet) —
  the operator-side BC pin (`ParOperator::SetEssentialTrueDofs`, `laplaceoperator.cpp:215-217`). It
  is the natural co-dispatch sibling to `eliminate_rhs` (the two halves of essential-BC treatment).
  Not in this dispatch's scope (D3 = `eliminate_rhs` only); flagged for a future harvester pass.
- **`set_subvector` essential-dof mask is referenced as a concept, not a firm L1 operator** — it is
  shared with `divfree-projector` (boundary-zeroing). If a future pass wants it as a first-class
  concept page, `book/src/concepts/set-subvector.md` would be the home; not required for this firm land
  (it does not gate any `eliminate_rhs` law). Surfaced, not actioned.
- **Layer intro refresh**: the L1 index §FE-assembly sub-spine prose may want a one-line note that the
  two BC-treatment post-compositions (`eliminate_rhs` firm; `eliminate_essential_bc` still rough-in)
  are separable from the `fe_assemble` fold. Flagged for layer-intro-author (not my write-scope).
