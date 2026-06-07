---
layer: L1
operator: basis_apply
# Graded-stack: roadmap_goal (rank 0). The B / Bᵀ stage of A = Gᵀ B_𝒟ᵀ D B_𝒟 G. Rank-0: it contracts
# the element-local-dof tensor Tensor[(E, L)] against the tabulated basis to produce quad-point values
# Tensor[(E, P, C)] — the [E, P, C] rank structure is the vocabulary shift our firm flat-vector-BLAS
# L1 (Tensor[N]) does not carry. Reachable via libceed-quadrature-kernel-impl (pulled-by).
rank: roadmap_goal
edges:
  reference:
    - target: L1/libceed-quadrature-kernel-impl
      kind: pulled-by      # the roadmap_goal consumer whose pipeline composes this B/Bᵀ basis-eval stage (free)
    - target: L1/weak_form_term   # the term's differential-operator 𝒟 selects the EvalMode (Interp/Grad/Curl/Div) this op applies
---

# basis_apply

The **B / Bᵀ** stage of the libCEED contraction pipeline
`A = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G` (see [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md)):
**basis evaluation** — contract the per-element local-dof tensor against the tabulated basis (and its
derivatives) to produce field values (or derivatives) at quadrature points (`B`), and its transpose
contracting quad-point data back to element dofs (`Bᵀ`). The basis-eval *mode* (`interp` / `grad` /
`curl` / `div`) is selected by the term's differential operator `𝒟`.

## Status

`roadmap_goal` (rank 0). **Clean-gate: ROADMAP_GOAL, not firm/rough-in.** The Palace realization is
exhaustively anchored (the `CeedBasis` construction + the `EvalMode`-keyed field dispatch — see
*Verified-against*), but the operator contracts the element-local tensor `Tensor[(E, L)]` to the
**quad-point-valued** tensor `Tensor[(E, P, C)]` (element axis `E`, quad-point axis `P`, value-component
axis `C`). The `[E, P, C]` rank structure is exactly the vocabulary our firm flat-vector-BLAS L1
(`Tensor[N]`) does not carry — a genuine **vocabulary shift** — so the honest disposition is rank-0,
carrying the constructive sketch + named shape groups with no firm claim. Promotion route: firm when the
quad-point-rank tensor substrate is firm L1 vocabulary.

## L1 form (the constructive sketch)

Semantic/notation conventions (named shape groups, basis-eval modes) live on the governing surface
`book/src/design/l4_calculus.md` §1.2.1 — linked, not restated.

    basis_apply :: BasisMode -> Basis -> Tensor[(E, L)] -> Tensor[(E, P, C)]
        -- B:  per-element local-dofs -> values (or derivatives) at quadrature points
    basis_apply_t :: BasisMode -> Basis -> Tensor[(E, P, C)] -> Tensor[(E, L)]
        -- Bᵀ: quad-point data -> per-element local-dofs (the transpose contraction)
        --   E = element count;  L = local dofs per element;
        --   P = quadrature points per element;  C = value components (1 for scalar interp; q_comp for grad/curl/div)
        -- BasisMode in { Interp, Grad, Curl, Div }  (selected by the term's 𝒟; see EvalMode)

`B` is a **per-element contraction** of the local-dof vector against the tabulated basis matrix (`interp`:
basis values at quad points) or the tabulated basis-derivative matrix (`grad`/`curl`/`div`). The mode is
chosen by the term's differential operator `𝒟 ∈ {Identity, Gradient, Curl, Divergence}`
([`weak_form_term`](./weak_form_term.md)), which Palace encodes as the `EvalMode`
(`Interp`/`Grad`/`Curl`/`Div`) wired into the QFunction active-input fields. `Bᵀ` is the exact transpose
(the basis matrix is applied on the left in `B`, on the right in `Bᵀ`).

**Sum-factorization is a transparent performance trick.** On a tensor-product element the basis matrix
factors into a sequence of 1-D contractions (`CeedBasisCreateTensorH1`), reducing the per-element cost
from `O(P·L)` to `O(d·P^{1/d}·L)`. This is *algebraically equivalent* to the dense per-element basis
contraction — it changes the contraction order, not the result. Per CLAUDE.md §Optimization-tricks it
is a **transparent trick**: the L1 form is the un-factorized dense contraction; sum-factorization is a
one-line note, not a separate algebraic claim. (This resolves the OQ
`libceed-quadrature-kernel-impl-sum-factorization-classification`: transparent, one-line note.)

## Algebraic laws (sketch — to be confirmed at promotion)

- **Transpose pair:** `⟨B x, q⟩_{(E,P,C)} = ⟨x, Bᵀ q⟩_{(E,L)}` — `basis_apply_t` is the exact adjoint of
  `basis_apply` for a fixed mode/basis.
- **Linearity (per element):** `B` is a per-element linear contraction — `B (a·x + b·y) = a·(B x) + b·(B y)`.
- **Element-diagonal (no inter-element coupling):** `B` acts independently per element (block-diagonal in
  `E`) — all inter-element coupling lives in `element_restrict`'s `Gᵀ`, not here.
- **Sum-factorization invariance:** the sum-factorized and dense contractions produce identical results
  (the transparent-trick equivalence) — a stated equivalence, not a distinct algorithm.

## Applicability conditions

1. A standard FE basis with a tabulated `CeedBasis` (nodal Lagrange / Nédélec / Raviart-Thomas / L2),
   built by `InitBasis` — the de-Rham family axis of [`weak_form_term`](./weak_form_term.md). The
   `CeedBasisCreateH1`/`Hcurl`/`Hdiv` selectors realize the family-keyed basis-eval modes.
2. The term's `𝒟` is one of `{Identity, Gradient, Curl, Divergence}` — these select the `EvalMode`
   (`Interp`/`Grad`/`Curl`/`Div`). Non-de-Rham / non-polynomial integrands are out of scope.

## Verified-against

- `palace/fem/libceed/integrator.cpp:25-65` — `AddQFunctionActiveInputs`: the `EvalMode`-keyed
  active-input field dispatch (`CEED_EVAL_INTERP`/`GRAD`/`DIV`/`CURL`) — the per-mode basis-eval
  selection that realizes `B`.
- `palace/fem/libceed/integrator.hpp:14-23` — `enum EvalMode { Weight, None, Interp, Grad, Div, Curl }`
  — the basis-eval modes the term's `𝒟` selects.
- `palace/fem/libceed/basis.cpp:169-180` — `InitBasis`: the `CeedBasis` builder; dispatches the
  tensor-product (`InitTensorBasis`, `:15`) vs non-tensor path.
- `palace/fem/libceed/basis.cpp:15-35` — `InitTensorBasis` + `CeedBasisCreateTensorH1` (`:35`): the
  **sum-factorized** tensor-product basis (the transparent-trick efficiency win).
- `palace/fem/libceed/basis.cpp:67-81` — `CeedBasisCreateHdiv` (`:67`) / `CeedBasisCreateHcurl` (`:74`) /
  `CeedBasisCreateH1` (`:81`): the de-Rham family basis-eval selectors.
- `palace/fem/bilinearform.cpp:64-70` — `trial_basis`/`test_basis` (`:68`/`:69`): the `B` operands the
  assembler receives (`GetCeedBasis`).
- `book/src/L1/libceed-quadrature-kernel-impl.md` — the roadmap_goal consumer (pulled-by).

## Related

- [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md) — composes this `B`/`Bᵀ` stage.
- [`element_restrict`](./element_restrict.md) — the `G` stage applied BEFORE `B` (and `Gᵀ` after `Bᵀ`).
- [`quad_point_contract`](./quad_point_contract.md) — the `D` stage applied between `B` and `Bᵀ`.
- [`weak_form_term`](./weak_form_term.md) — `(Q, 𝒟)`; `𝒟` selects this op's `BasisMode`.
