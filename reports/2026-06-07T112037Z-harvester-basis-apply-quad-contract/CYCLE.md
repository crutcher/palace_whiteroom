---
agent: harvester
invoked_at: 2026-06-07T113000Z
scope: L1 operators basis_apply + quad_point_contract (the two arithmetic libceed substrate ops; element-local rank-tensor vocabulary shift)
status: pending
integrated_at: 2026-06-07T112037Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-124 (batch-40 opener) D3. Applied clean. Promoted L1/basis_apply + L1/quad_point_contract roadmap_goal->FIRM (firm-on-positive-structure escape) + reference edge to concepts/element-local-tensor + stale design/l4_calculus.md ->semantics/index.md path fix + repaired EvalMode/apply-QFunction pinpoints. L1/index in-place flips only (consolidated tally deferred to D5). Part of the libCEED-substrate firm-flip (43->45)."
inputs:
  - reports/2026-06-07T112037Z-cycle-planner-c124/CYCLE.md (D3 entry + Overlap + consolidated-tally partition: D5 owns L1/index tally)
  - book/src/L1/basis_apply.md (roadmap_goal, to firm)
  - book/src/L1/quad_point_contract.md (roadmap_goal, to firm)
  - book/src/L1/libceed-quadrature-kernel-impl.md (the kernel-impl consumer; exhaustive verified_against block)
  - book/src/semantics/index.md §1.2.1 / §1.2.2 (named shape groups — USE+LINK, the live surface; replaces stale design/l4_calculus.md path)
  - concepts/element-local-tensor (canonical slug; D5 authors this wave — the [E,L]/[E,P,C]/[E,P,G] record page)
  - reference/palace/palace/fem/libceed/{integrator.cpp,integrator.hpp,basis.cpp} + fem/bilinearform.cpp (codemap on-disk verified)
---

# CYCLE: Formalize basis_apply + quad_point_contract at L1 (the arithmetic libceed substrate)

## Summary

D3 firms the **two arithmetic libceed substrate operators** that carry the genuine element-local
rank-tensor vocabulary shift: `basis_apply` (the `B`/`Bᵀ` basis-evaluation contraction
`Tensor[(E, L)] ↔ Tensor[(E, P, C)]`) and `quad_point_contract` (the `D` pointwise per-quad-point
contraction over `Tensor[(E, P, C)]`). Both were rank-0 `roadmap_goal` chapters (authored c122 D4)
with exhaustively-anchored Palace realizations but a deferred maturity, pending the element-local
rank-tensor becoming firm L1 vocabulary. **That substrate becomes firm L1 vocabulary THIS wave** —
D5 authors the `concepts/element-local-tensor` record page defining the `[E, L]` / `[E, P, C]` /
`[E, P, G]` shape family as a first-class L1 data shape, and both operators' laws are **syntactic
identities on fully-specified positive source** (transpose adjointness, per-element linearity,
block-diagonality, pointwise-no-coupling) read directly off the libCEED operator-construction code.
So both promote `roadmap_goal → firm` on the **firm-on-positive-structure escape** (no dedicated
unit test gates a syntactic-identity law — the `apply_linop` / `weak_form_term` / `fe_assemble`
precedent). The shape vocabulary established: `Tensor[(E, L)]` (per-element local-dof tensor),
`Tensor[(E, P, C)]` (per-quad-point value/derivative tensor), `Tensor[(E, P, G)]` (the
geometry-factor carrier) — all referencing the canonical `concepts/element-local-tensor` record
page; the contraction algebra (adjoint basis-eval, pointwise diagonal). Sum-factorization is
confirmed a **transparent performance trick** (one-line note; the L1 form is the un-factorized dense
contraction). Both chapters' stale `book/src/design/l4_calculus.md` §1.2.1 citation is fixed to the
live `book/src/semantics/index.md` §1.2.1. The `quad_point_contract` apply-QFunction citations
(`geom_data` input, `q_w`) are re-anchored from the drifted `:483-485`/`:486-490` to the on-disk
`:457-458`/`:462`. **I emit ONLY my own two dep-map rows + cohort bullets (flipped roadmap_goal →
firm); I DEFER the L1/index consolidated firm-count tally to D5** (the wave's tally owner).

## Proposed changes

```edit:book/src/L1/basis_apply.md
---
layer: L1
operator: basis_apply
# Graded-stack: firm (rank 3). The B / Bᵀ stage of A = Gᵀ B_𝒟ᵀ D B_𝒟 G. It contracts the
# element-local-dof tensor Tensor[(E, L)] against the tabulated basis to produce quad-point values
# Tensor[(E, P, C)] — the element-local rank-tensor vocabulary now firm L1 (concepts/element-local-tensor,
# D5 this wave). Firm-on-positive-structure: the laws are syntactic identities (adjoint pairing,
# per-element linearity, block-diagonality) on exhaustively-anchored positive libCEED source.
# Reachable via libceed-quadrature-kernel-impl (pulled-by).
rank: firm
edges:
  reference:
    - target: L1/libceed-quadrature-kernel-impl
      kind: pulled-by      # the kernel-impl consumer whose pipeline composes this B/Bᵀ basis-eval stage (free)
    - target: L1/weak_form_term   # the term's differential-operator 𝒟 selects the EvalMode (Interp/Grad/Curl/Div) this op applies
    - target: concepts/element-local-tensor   # the [E,L]/[E,P,C] element-local rank-tensor shape family this op maps between (the firm L1 data shape, D5 this wave)
---

# basis_apply

The **B / Bᵀ** stage of the libCEED contraction pipeline
`A = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G` (see [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md)):
**basis evaluation** — contract the per-element local-dof tensor against the tabulated basis (and its
derivatives) to produce field values (or derivatives) at quadrature points (`B`), and its transpose
contracting quad-point data back to element dofs (`Bᵀ`). The basis-eval *mode* (`interp` / `grad` /
`curl` / `div`) is selected by the term's differential operator `𝒟`.

## Status

`firm` (rank 3). **Clean-gate: PROMOTE (roadmap_goal → firm).** The operator contracts the
element-local tensor `Tensor[(E, L)]` to the **quad-point-valued** tensor `Tensor[(E, P, C)]`
(element axis `E`, local-dofs-per-element axis `L`, quad-point axis `P`, value-component axis `C`) —
the element-local rank structure the firm flat-vector-BLAS L1 (`Tensor[N]`) does not carry. That
rank-tensor is now **firm L1 vocabulary**: the `[E, L]` / `[E, P, C]` shape family has a
record-definition home at [`concepts/element-local-tensor`](../concepts/element-local-tensor.md)
(this wave), so the vocabulary shift that kept this chapter rank-0 is closed. The promotion uses the
**firm-on-positive-structure escape**: the algebraic laws below are **syntactic identities on
fully-specified positive source** (the adjoint pairing is the basis-matrix transpose read off the
`B`-on-the-left / `Bᵀ`-on-the-right construction; per-element linearity and block-diagonality are the
structure of a per-element matrix contraction) — not test-gated convergence semantics — so the
absence of a dedicated `test-basis.cpp` does not gate firm (the `apply_nonlinear_pencil` cycle-021 /
`weak_form_term` cycle-061 / `fe_assemble` no-dedicated-test precedent). The Palace realization is
exhaustively anchored (the `CeedBasis` construction + the `EvalMode`-keyed field dispatch — see
*Verified-against*).

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
one-line note, not a separate algebraic claim. (This resolves the OQ
`libceed-quadrature-kernel-impl-sum-factorization-classification`: transparent, one-line note.)

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

## Verified-against

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
```

```edit:book/src/L1/quad_point_contract.md
---
layer: L1
operator: quad_point_contract
# Graded-stack: firm (rank 3). The D stage of A = Gᵀ B_𝒟ᵀ D B_𝒟 G — the pointwise per-quad-point
# contraction geom_data ⊙ (basis-evaluated trial) over Tensor[(E, P, C)]. The element-local
# rank-tensor is now firm L1 vocabulary (concepts/element-local-tensor, D5 this wave). Firm-on-positive-
# structure: the laws are syntactic identities (pointwise no-coupling, linearity-in-field, self-adjoint-
# when-symmetric) on exhaustively-anchored positive libCEED source. This is the embarrassingly-parallel
# diagonal of the pipeline (the per-quad-point lift). Reachable via libceed-quadrature-kernel-impl (pulled-by).
rank: firm
edges:
  reference:
    - target: L1/libceed-quadrature-kernel-impl
      kind: pulled-by      # the kernel-impl consumer whose pipeline composes this pointwise D stage (free)
    - target: L1/geom_factor_build   # produces the geom_data this op contracts against (the setup-stratum factor)
    - target: concepts/element-local-tensor   # the [E,P,C]/[E,P,G] quad-point rank-tensor this op operates on (the firm L1 data shape, D5 this wave)
    - target: concepts/tensor-field-lift   # the per-quad-point pointwise contraction IS the diagonal lift this concept describes
---

# quad_point_contract

The **D** stage of the libCEED contraction pipeline
`A = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G` (see [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md)):
the **pointwise per-quadrature-point contraction** — apply, *independently at each quadrature point*, the
precomputed `geom_data` (the product of material coefficient `Q`, geometry factor, and quadrature weight)
to the basis-evaluated trial field. This is the **embarrassingly-parallel diagonal** of the pipeline — the
per-quad-point lift that is the natural GPU-tensor form.

## Status

`firm` (rank 3). **Clean-gate: PROMOTE (roadmap_goal → firm).** The operator acts on the
**quad-point-rank** tensor `Tensor[(E, P, C)]` (element axis `E`, quad-point axis `P`, component axis
`C`) and contracts against the geometry-factor carrier `Tensor[(E, P, G)]` — the element-local rank
structure the firm flat-vector-BLAS L1 (`Tensor[N]`) does not carry. That rank-tensor is now **firm L1
vocabulary**: the `[E, P, C]` / `[E, P, G]` shape family has a record-definition home at
[`concepts/element-local-tensor`](../concepts/element-local-tensor.md) (this wave), so the substrate gap
that kept this chapter rank-0 — the *pointwise* elementwise-product structure (`⊙`) was firm only over
flat `Tensor[N]` ([`elementwise_product`](./elementwise_product.md)); lifting it to the `[E, P, C]`-shaped
diagonal needed the rank-tensor vocabulary — is closed. The promotion uses the **firm-on-positive-
structure escape**: the algebraic laws below are **syntactic identities on fully-specified positive
source** (pointwise-no-coupling is the per-`(e,p)` independence of the apply-QFunction; linearity-in-field
and self-adjoint-when-symmetric are the structure of a pointwise multiply by a fixed factor) — not
test-gated convergence semantics — so the absence of a dedicated test does not gate firm (the
`apply_nonlinear_pencil` / `weak_form_term` / `fe_assemble` no-dedicated-test precedent). The Palace
realization is exhaustively anchored (the apply-QFunction field wiring + the `f_apply_*` pointwise kernels
— see *Verified-against*).

## L1 form

Semantic/notation conventions (named shape groups, the `(E, P, C)` / `(E, P, G)` element-local rank
structure, the elementwise lift) live on [`book/src/semantics/index.md`](../semantics/index.md) §1.2.1 +
the record page [`concepts/element-local-tensor`](../concepts/element-local-tensor.md) — linked, not
restated.

    quad_point_contract :: GeomData -> Tensor[(E, P, C)] -> Tensor[(E, P, C')]
        -- D: pointwise, per (e, p): out[e,p,·] = geom_data[e,p] ⊙ in[e,p,·]
        --   E = element count;  P = quadrature points per element;
        --   C = trial value/derivative components;  C' = test components (often = C)
        --   GeomData :: Tensor[(E, P, G)]   the per-quad-point precomputed factor (G = geom-data components)

At each quadrature point `(e, p)` the contraction applies the precomputed `geom_data[e,p]` — which has
**pre-multiplied** the three pointwise factors (the material coefficient `Q` = `ε`/`μ⁻¹`/…, the
Jacobian-derived geometry metric `J⁻ᵀ J⁻¹ |J|` for grad-grad / `|J|` for mass, and the quadrature weight
`w`) into one factor by the separate build pass ([`geom_factor_build`](./geom_factor_build.md)). The
run-time apply is therefore a single pointwise multiply `geom_data ⊙ (basis-evaluated trial)` — no
inter-point coupling. In Palace this is the `f_apply_*` family (`f_apply_22`/`f_apply_33`/…), the
per-`(dim, space_dim)` pointwise apply-QFunctions selected by the active-field component sizes.

This is the **diagonal** of the pipeline: `B G` evaluates the trial field at quad points, `D` weights it
pointwise, `Bᵀ Gᵀ` contracts the weighted field back to the global operator. The pointwise structure is
exactly the per-quad-point lift `concepts/tensor-field-lift` describes — the embarrassingly-parallel,
GPU-natural stage.

## Algebraic laws

- **Pointwise (no coupling across quadrature points):** `D` is block-diagonal in `(E, P)` — the output at
  `(e, p)` depends only on the input at `(e, p)` and `geom_data[e, p]`. (Syntactic identity: the
  apply-QFunction is invoked per-quadrature-point with no cross-point term.) The embarrassingly-parallel law.
- **Linearity in the field:** for fixed `geom_data`, `D(a·u + b·v) = a·D(u) + b·D(v)` — `D` is the
  pointwise elementwise-product lift of `geom_data`, which is linear in its field argument.
- **Self-adjoint when `geom_data` is symmetric/diagonal:** for the mass/grad-grad metrics (symmetric
  positive `geom_data` blocks) the pointwise contraction is self-adjoint — `D = Dᵀ` — which underwrites
  the symmetry of `A = Gᵀ Bᵀ D B G` for self-adjoint terms.
- **Composition with the basis-eval:** `D` consumes `B`'s output shape `Tensor[(E, P, C)]` and emits the
  shape `Bᵀ` consumes — the pipeline shape-congruence law.

## Applicability conditions

1. The pointwise factors are pre-multiplied into `geom_data` by [`geom_factor_build`](./geom_factor_build.md)
   (the setup/run-time stratification): this op is the *run-time apply* half; the build half is separate.
2. The term's `𝒟` fixes the `geom_data` block shape (the `2 + space_dim*dim` geometry-data size) — mass
   (`|J|`) vs grad-grad (`J⁻ᵀ J⁻¹ |J|`).
3. Single-machine (per-`Ceed` device); the pointwise apply has no cross-rank coupling (the diagonal is
   element-local).

## Verified-against

- `palace/fem/libceed/integrator.cpp:451-495` — the apply-QFunction + operator-field wiring:
  `geom_data` input field (`:457-458`), optional `q_w` quad-weight (`:462`, `CEED_EVAL_WEIGHT`), active
  trial inputs / test outputs (`AddOperatorActiveInputFields` `:492`, `AddOperatorActiveOutputFields`
  `:493`) — the `B G` (input) / `Bᵀ Gᵀ` (output) field chains around the pointwise `D`.
- `palace/fem/libceed/integrator.cpp:215-308` — `QuadratureDataAssembly` (`:220`) + the `f_apply_*`
  pointwise apply-QFunctions selected by active-field component sizes (`f_apply_22` `:260`) — the `D`
  per-quad-point kernels.
- `palace/fem/libceed/integrator.cpp:423-445` — `AssembleCeedOperator` master assembler (`:423`): the
  `geom_data` / `q_w` inputs that feed the pointwise contraction.
- `book/src/concepts/element-local-tensor.md` — the `(E, P, C)` / `(E, P, G)` quad-point rank-tensor
  shape family this op operates on (the firm L1 data shape).
- `book/src/L1/libceed-quadrature-kernel-impl.md` — the kernel-impl consumer (pulled-by).

## Related

- [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md) — composes this `D` stage.
- [`geom_factor_build`](./geom_factor_build.md) — the setup-stratum pass that produces the `geom_data`
  this op contracts against.
- [`basis_apply`](./basis_apply.md) — the `B`/`Bᵀ` stages on either side of `D`.
- `concepts/tensor-field-lift` — the per-quad-point lift this op realizes.
- [`concepts/element-local-tensor`](../concepts/element-local-tensor.md) — the `[E, P, C]` / `[E, P, G]`
  element-local rank-tensor shape family (the firm L1 data shape this op operates on).
- [`elementwise_product`](./elementwise_product.md) — the firm flat-`Tensor[N]` pointwise multiply this
  op lifts to the `[E, P, C]`-rank diagonal (now firm L1 vocabulary via the element-local rank-tensor).
```

```edit:book/src/L1/index.md
- **`basis_apply` is a `roadmap_goal`** *(cycle-122 D4)* — see [`basis_apply`](./basis_apply.md). The **B / Bᵀ** stage: basis evaluation contracting per-element dofs to quad-point values `Tensor[(E, L)] → Tensor[(E, P, C)]`, keyed on the `EvalMode` (`Interp`/`Grad`/`Curl`/`Div`) the term's `𝒟` selects. Sum-factorization is a **transparent trick** (one-line note — resolves OQ `libceed-quadrature-kernel-impl-sum-factorization-classification`). L0: `AddQFunctionActiveInputs` (`palace/fem/libceed/integrator.cpp:25-65`), `EvalMode` (`palace/fem/libceed/integrator.hpp:14-23`), `InitBasis`/`InitTensorBasis` (`palace/fem/libceed/basis.cpp:169-180,:15-35`).
- **`basis_apply` is now FIRM** *(cycle-124 D3)* — see [`basis_apply`](./basis_apply.md). The **B / Bᵀ** stage: basis evaluation contracting per-element dofs to quad-point values `Tensor[(E, L)] → Tensor[(E, P, C)]`, keyed on the `EvalMode` (`Interp`/`Grad`/`Curl`/`Div`) the term's `𝒟` selects. **Promoted roadmap_goal → firm**: the element-local rank-tensor is now firm L1 vocabulary (`concepts/element-local-tensor`, cycle-124 D5), and the laws are firm-on-positive-structure syntactic identities (adjoint basis-eval pairing, per-element linearity, block-diagonality in `E`) read off the libCEED operator-construction code — no-dedicated-test caveat non-gating per the `weak_form_term`/`fe_assemble` precedent. Sum-factorization is a **transparent trick** (one-line note — resolves OQ `libceed-quadrature-kernel-impl-sum-factorization-classification`). L0: `AddQFunctionActiveInputs` (`palace/fem/libceed/integrator.cpp:25-65`), `EvalMode` (`palace/fem/libceed/integrator.hpp:14-23`), `InitBasis`/`InitTensorBasis` (`palace/fem/libceed/basis.cpp:169-180,:15-35`).
- **`quad_point_contract` is a `roadmap_goal`** *(cycle-122 D4)* — see [`quad_point_contract`](./quad_point_contract.md). The **D** stage: the pointwise per-quad-point contraction `geom_data ⊙ ·` over `Tensor[(E, P, C)]` — the embarrassingly-parallel diagonal (the per-quad-point lift `concepts/tensor-field-lift`). The flat-`Tensor[N]` pointwise multiply is firm (`elementwise_product`); lifting it to the `[E, P, C]` diagonal is the substrate gap. L0: the apply-QFunction wiring (`palace/fem/libceed/integrator.cpp:451-512`), the `f_apply_*` kernels (`:215-308`).
- **`quad_point_contract` is now FIRM** *(cycle-124 D3)* — see [`quad_point_contract`](./quad_point_contract.md). The **D** stage: the pointwise per-quad-point contraction `geom_data ⊙ ·` over `Tensor[(E, P, C)]` — the embarrassingly-parallel diagonal (the per-quad-point lift `concepts/tensor-field-lift`). **Promoted roadmap_goal → firm**: the element-local rank-tensor is now firm L1 vocabulary (`concepts/element-local-tensor`, cycle-124 D5), closing the substrate gap (the flat-`Tensor[N]` `elementwise_product` lifts to the `[E, P, C]` diagonal); the laws are firm-on-positive-structure syntactic identities (pointwise-no-coupling block-diagonal in `(E, P)`, linearity-in-field, self-adjoint-when-symmetric). L0: the apply-QFunction wiring (`palace/fem/libceed/integrator.cpp:451-495`; `geom_data` `:457-458`, `q_w` `:462`, active in/out `:492`/`:493`), the `f_apply_*` kernels (`:215-308`, `f_apply_22` `:260`).
```

```edit:book/src/L1/index.md
| [`basis_apply`](./basis_apply.md) | `BasisMode → Basis → Tensor[(E, L)] → Tensor[(E, P, C)]` (B, basis-eval); transpose `Tensor[(E, P, C)] → Tensor[(E, L)]` (Bᵀ) | `pulled-by` (reference) [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md) — the B/Bᵀ stage; references [`weak_form_term`](./weak_form_term.md) (𝒟 selects the EvalMode) | `roadmap_goal` (rank-0 libCEED contraction substrate; basis-eval keyed on the EvalMode the term's `𝒟` selects, over the `[E, P, C]` quad-point-rank tensor not in firm L1; sum-factorization a transparent trick; resolves 1 of 6 `unresolved_depends_on_targets`; proposed-by: harvester:2026-06-07T071941Z-harvester-libceed-substrate-ops) |
| [`basis_apply`](./basis_apply.md) | `BasisMode → Basis → Tensor[(E, L)] → Tensor[(E, P, C)]` (B, basis-eval); transpose `Tensor[(E, P, C)] → Tensor[(E, L)]` (Bᵀ) | `pulled-by` (reference) [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md) — the B/Bᵀ stage; references [`weak_form_term`](./weak_form_term.md) (𝒟 selects the EvalMode) + `concepts/element-local-tensor` (the `[E, L]`/`[E, P, C]` shape family) | `firm` (the element-local rank-tensor `[E, L]`↔`[E, P, C]` is now firm L1 vocabulary via `concepts/element-local-tensor`, cycle-124 D5; firm-on-positive-structure — laws are syntactic identities: adjoint basis-eval pairing `⟨Bx,q⟩=⟨x,Bᵀq⟩`, per-element linearity, block-diagonality in `E`; sum-factorization a transparent trick; no-dedicated-test non-gating per `weak_form_term`/`fe_assemble`; promoted roadmap_goal→firm cycle-124 D3) |
| [`quad_point_contract`](./quad_point_contract.md) | `GeomData → Tensor[(E, P, C)] → Tensor[(E, P, C')]` (D, pointwise per-quad-point `geom_data ⊙ ·`) | `pulled-by` (reference) [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md) — the D stage (embarrassingly-parallel diagonal); references [`geom_factor_build`](./geom_factor_build.md) (produces geom_data) + `concepts/tensor-field-lift` | `roadmap_goal` (rank-0 libCEED contraction substrate; the per-quad-point pointwise contraction over the `[E, P, C]` quad-point-rank tensor; the flat-`Tensor[N]` `elementwise_product` is firm but the `[E,P,C]` diagonal lift is the substrate gap; resolves 1 of 6 `unresolved_depends_on_targets`; proposed-by: harvester:2026-06-07T071941Z-harvester-libceed-substrate-ops) |
| [`quad_point_contract`](./quad_point_contract.md) | `GeomData → Tensor[(E, P, C)] → Tensor[(E, P, C')]` (D, pointwise per-quad-point `geom_data ⊙ ·`) | `pulled-by` (reference) [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md) — the D stage (embarrassingly-parallel diagonal); references [`geom_factor_build`](./geom_factor_build.md) (produces geom_data) + `concepts/element-local-tensor` (the `[E, P, C]`/`[E, P, G]` shape family) + `concepts/tensor-field-lift` | `firm` (the `[E, P, C]`/`[E, P, G]` quad-point rank-tensor is now firm L1 vocabulary via `concepts/element-local-tensor`, cycle-124 D5, closing the `elementwise_product` flat→diagonal substrate gap; firm-on-positive-structure — laws are syntactic identities: pointwise-no-coupling block-diagonal in `(E, P)`, linearity-in-field, self-adjoint-when-symmetric; no-dedicated-test non-gating; promoted roadmap_goal→firm cycle-124 D3) |
```

## Operator content

(The two firm chapter bodies are the full content of the proposed-changes blocks above — `## Status`,
`## L1 form`, `## Algebraic laws`, `## Applicability conditions`, `## Verified-against`, `## Related`
for each, all inside the fence.)

**basis_apply** — `firm`. Signature `basis_apply :: BasisMode -> Basis -> Tensor[(E, L)] ->
Tensor[(E, P, C)]` + transpose. Laws: transpose-adjointness, per-element linearity, element-diagonal
(block-diagonal in `E`), sum-factorization-invariance. Shape vocabulary: `Tensor[(E, L)]` ↔
`Tensor[(E, P, C)]` (element-local rank-tensor, `concepts/element-local-tensor`). Evidence:
`integrator.cpp:25-65` (EvalMode dispatch), `integrator.hpp:14-23` (EvalMode enum), `basis.cpp:15-35`
(sum-factorized tensor basis), `:67-81` (de-Rham family selectors), `:169-180` (InitBasis),
`bilinearform.cpp:64-70` (trial/test_basis operands).

**quad_point_contract** — `firm`. Signature `quad_point_contract :: GeomData -> Tensor[(E, P, C)] ->
Tensor[(E, P, C')]`, `GeomData :: Tensor[(E, P, G)]`. Laws: pointwise-no-coupling (block-diagonal in
`(E, P)`), linearity-in-field, self-adjoint-when-symmetric, composition-with-basis-eval. Shape
vocabulary: `Tensor[(E, P, C)]` operated on, `Tensor[(E, P, G)]` geom-factor carrier
(`concepts/element-local-tensor`). Evidence: `integrator.cpp:451-495` (apply-QFunction wiring;
geom_data `:457-458`, q_w `:462`, active in/out `:492`/`:493`), `:215-308` (QuadratureDataAssembly +
f_apply_*; f_apply_22 `:260`), `:423-445` (AssembleCeedOperator).

## Supporting evidence

All citations codemap-verified on-disk this dispatch (`mcp__palace-codemap__read_range`):

- `palace/fem/libceed/integrator.cpp:25` — `AddQFunctionActiveInputs` signature; `:41` `CEED_EVAL_INTERP`,
  `:49` `CEED_EVAL_GRAD`, `:57` `CEED_EVAL_DIV`, `:65` `CEED_EVAL_CURL` — EvalMode-keyed dispatch (AddInput call lines). CONFIRMED.
- `palace/fem/libceed/integrator.hpp:14-23` — `enum EvalMode` (`Weight = 1<<0` at `:17`, … `Curl = 1<<5`
  at `:22`; enum body `:15-23`). CONFIRMED.
- `palace/fem/libceed/basis.cpp:15` — `InitTensorBasis`; `CeedBasisCreateTensorH1` at `:35`. CONFIRMED.
- `palace/fem/libceed/basis.cpp:67` — `CeedBasisCreateHdiv`; `:74` Hcurl branch; `:81` `CeedBasisCreateH1`.
  CONFIRMED (the read started at :67 showing `CeedBasisCreateHdiv`).
- `palace/fem/libceed/basis.cpp:169` — `InitBasis`; tensor dispatch to `InitTensorBasis` at `:176-180`.
  CONFIRMED.
- `palace/fem/bilinearform.cpp:64` `trial_restr`, `:66` `test_restr`, `:68` `trial_basis`, `:69`
  `test_basis`, `:75` `integ->Assemble`, `:77` `AddSubOperator`. CONFIRMED.
- `palace/fem/libceed/integrator.cpp:457-458` — `geom_data` input field (`CeedQFunctionAddInput(apply_qf,
  "geom_data", …)`); `:462` `q_w` `CEED_EVAL_WEIGHT`; `:492` `AddOperatorActiveInputFields`; `:493`
  `AddOperatorActiveOutputFields`. CONFIRMED (re-anchored from the drifted `:483-485`/`:486-490`).
- `palace/fem/libceed/integrator.cpp:220` — `QuadratureDataAssembly`; `:260` `f_apply_22`. CONFIRMED.
- `palace/fem/libceed/integrator.cpp:423` — `AssembleCeedOperator`. CONFIRMED.

Cross-references: the kernel-impl consumer `book/src/L1/libceed-quadrature-kernel-impl.md` already
carries an exhaustive verified_against block (the c122 D4 + c123 audit) confirming the same anchors;
`weak_form_term` (firm) supplies the `𝒟`→EvalMode axis; `concepts/element-local-tensor` (D5 this wave)
is the record-definition home for the `[E, L]`/`[E, P, C]`/`[E, P, G]` shape family.

## Open questions / caveats

- **`concepts/element-local-tensor` is a co-wave forward-reference (D5).** Both firm chapters reference
  `concepts/element-local-tensor` by the **canonical slug stated in the planner's D3+D5 scope** — the page
  is authored by D5 THIS wave. D5 lands in WAVE-2 (after D3); per the planner's forward-reference-slug
  coordination, the slug is canonical (not a guess). The links are written as live markdown links
  (`../concepts/element-local-tensor.md`); if the integrator applies D3 before D5's file exists, the
  `linkcheck2` build would error — but the two-wave sequencing + single-finalize (book rebuilt once, after
  both waves) makes the file present at build time. Flagged so the integrator orders D5's concepts-page
  creation before the finalize build (it does, by the wave schedule).
- **Maturity call: firm, on the firm-on-positive-structure escape.** Both ops' laws are syntactic
  identities on exhaustively-anchored positive libCEED source, and the element-local rank-tensor becomes
  firm L1 vocabulary this wave (D5). This is the planner's honest-clean-gate "land at the maturity the
  evidence + the D5 record-page support justify." If the critic judges the rank-tensor shape family NOT
  firm until D5's page is verified-firm at integrate time, the honest fallback is `rough-in
  (test-coverage-bounded)` for both (structure firm, the shape-family-firmness gated on D5) — but the
  firm call stands given D5 is a committed co-wave deliverable and the laws need no test.
- **Consolidated tally DEFERRED to D5** (per the planner's parallel-blind-shared-index partition). I emit
  ONLY my two dep-map rows (flipped firm) + my two cohort bullets (flipped firm); the `L1/index.md`
  substrate-cohort consolidated firm-count tally + growth-log is D5's (the wave's tally owner). The cohort
  bullet header "**Roadmap_goal (libCEED contraction substrate — 4 …)**" count is part of the consolidated
  tally → D5 adjusts it (2 of the 4 now firm); I do NOT touch that header line.
- **`element_restrict` + `geom_factor_build` (D4) are the other two substrate ops** flipping this wave;
  the `libceed-quadrature-kernel-impl` consumer's promotion off roadmap_goal (its `depends-on` edges
  becoming firm-resting once all 4 substrate ops firm) is D5's call, not mine.
- **No SUMMARY.md change needed.** Both chapters are already registered in `SUMMARY.md` (roadmap_goal
  lines, present since c122 D4); the maturity flip is in-place, no new SUMMARY line, distinct slugs — per
  the planner's overlap note "D3/D4 flip in-place, no new lines."
