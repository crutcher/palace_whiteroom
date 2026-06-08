---
layer: L1
operator: basis_apply
# The B / Bᵀ stage of A = Gᵀ B_𝒟ᵀ D B_𝒟 G: contracts the element-local-dof tensor
# Tensor[(E, L)] against the tabulated basis to produce quad-point values Tensor[(E, P, C)].
# Firm-on-positive-structure: the laws are syntactic identities (adjoint pairing,
# per-element linearity, block-diagonality) on exhaustively-anchored positive libCEED source.
rank: firm
edges:
  reference:
    - target: L1/libceed-quadrature-kernel-impl
      kind: pulled-by      # the kernel-impl consumer whose pipeline composes this B/Bᵀ basis-eval stage (free)
    - target: L1/weak_form_term   # the term's differential-operator 𝒟 selects the EvalMode (Interp/Grad/Curl/Div) this op applies
    - target: concepts/element-local-tensor   # the [E,L]/[E,P,C] element-local rank-tensor shape family this op maps between (the firm L1 data shape)
---

# basis_apply

The **B / Bᵀ** stage of the libCEED contraction pipeline
`A = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G` (see [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md)):
**basis evaluation** — contract the per-element local-dof tensor against the tabulated basis (and its
derivatives) to produce field values (or derivatives) at quadrature points (`B`), and its transpose
contracting quad-point data back to element dofs (`Bᵀ`). The basis-eval *mode* (`interp` / `grad` /
`curl` / `div`) is selected by the term's differential operator `𝒟`.

## L1 form

Semantic/notation conventions (named shape groups, the `(E, L)` / `(E, P, C)` element-local rank
structure) live on the governing surface [`book/src/semantics/index.md`](../semantics/index.md)
§1.2.1 + the record page [`concepts/element-local-tensor`](../concepts/element-local-tensor.md) —
linked, not restated.

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
one-line note, not a separate algebraic claim.

## Algebraic laws

- **Transpose pair (adjointness):** `⟨B x, q⟩_{(E,P,C)} = ⟨x, Bᵀ q⟩_{(E,L)}` — `basis_apply_t` is the
  exact adjoint of `basis_apply` for a fixed mode/basis. (Syntactic identity: `Bᵀ` IS the transpose of
  the tabulated basis matrix `B` applies — the same `maps.Bt`/`maps.Gt` data applied on the opposite
  side; the assembler wires `trial_basis` on the input chain and `test_basis` on the output chain.)
- **Linearity (per element):** `B` is a per-element linear contraction —
  `B (a·x + b·y) = a·(B x) + b·(B y)`. (Matrix contraction is linear in its operand.)
- **Element-diagonal (no inter-element coupling):** `B` acts independently per element (block-diagonal in
  `E`) — all inter-element coupling lives in `element_restrict`'s `Gᵀ`, not here. (The QFunction is
  applied element-by-element over the restricted local-dof tensor; the basis matrix is shared across
  elements but applied without cross-element terms.)
- **Sum-factorization invariance:** the sum-factorized and dense contractions produce identical results
  (the transparent-trick equivalence) — a stated equivalence, not a distinct algorithm.

## Applicability conditions

1. A standard FE basis with a tabulated `CeedBasis` (nodal Lagrange / Nédélec / Raviart-Thomas / L2),
   built by `InitBasis` — the de-Rham family axis of [`weak_form_term`](./weak_form_term.md). The
   `CeedBasisCreateH1`/`Hcurl`/`Hdiv` selectors realize the family-keyed basis-eval modes.
2. The term's `𝒟` is one of `{Identity, Gradient, Curl, Divergence}` — these select the `EvalMode`
   (`Interp`/`Grad`/`Curl`/`Div`). Non-de-Rham / non-polynomial integrands are out of scope.

## Evidence

- `palace/fem/libceed/integrator.cpp:25-65` — `AddQFunctionActiveInputs`: the `EvalMode`-keyed
  active-input field dispatch (`CEED_EVAL_INTERP` `:41`, `GRAD` `:49`, `DIV` `:57`, `CURL` `:65`) — the
  per-mode basis-eval selection that realizes `B`.
- `palace/fem/libceed/integrator.hpp:14-23` — `enum EvalMode { Weight, None, Interp, Grad, Div, Curl }`
  (enum body `:15-23`) — the basis-eval modes the term's `𝒟` selects.
- `palace/fem/libceed/basis.cpp:169-180` — `InitBasis`: the `CeedBasis` builder; dispatches the
  tensor-product (`InitTensorBasis`, `:176-180`) vs non-tensor path.
- `palace/fem/libceed/basis.cpp:15-35` — `InitTensorBasis` + `CeedBasisCreateTensorH1` (`:35`): the
  **sum-factorized** tensor-product basis (the transparent-trick efficiency win).
- `palace/fem/libceed/basis.cpp:67-81` — `CeedBasisCreateHdiv` (`:67`) / `CeedBasisCreateHcurl` (`:74`) /
  `CeedBasisCreateH1` (`:81`): the de-Rham family basis-eval selectors.
- `palace/fem/bilinearform.cpp:64-70` — `trial_basis`/`test_basis` (`:68`/`:69`): the `B` operands the
  assembler receives (`GetCeedBasis`); the leaf `Assemble` call `:75`.
- `book/src/concepts/element-local-tensor.md` — the `(E, L)` / `(E, P, C)` rank-tensor shape family
  this op maps between (the firm L1 data shape).
- `book/src/L1/libceed-quadrature-kernel-impl.md` — the kernel-impl consumer (pulled-by).

## Related

- [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md) — composes this `B`/`Bᵀ` stage.
- [`element_restrict`](./element_restrict.md) — the `G` stage applied BEFORE `B` (and `Gᵀ` after `Bᵀ`).
- [`quad_point_contract`](./quad_point_contract.md) — the `D` stage applied between `B` and `Bᵀ`.
- [`weak_form_term`](./weak_form_term.md) — `(Q, 𝒟)`; `𝒟` selects this op's `BasisMode`.
- [`concepts/element-local-tensor`](../concepts/element-local-tensor.md) — the `[E, L]` / `[E, P, C]`
  element-local rank-tensor shape family (the firm L1 data shape this op operates on).
