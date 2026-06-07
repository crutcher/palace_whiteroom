---
agent: harvester
invoked_at: 2026-06-07T071941Z
scope: L1 operators (cohort) — element_restrict, basis_apply, quad_point_contract, geom_factor_build
status: pending
inputs:
  - reports/2026-06-07T071941Z-cycle-planner-cycle-122/CYCLE.md (D4 row)
  - book/src/L1/libceed-quadrature-kernel-impl.md (the c121-D4 roadmap_goal that declares these 4 as unresolved depends-on targets)
  - book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md (kernel-api surface)
  - palace/fem/libceed/integrator.{cpp,hpp}, restriction.cpp, basis.cpp, bilinearform.cpp (codemap-verified)
  - book/src/design/l4_calculus.md §1.2.1 (named shape groups — governing semantic surface)
integrated_at: 2026-06-07T071941Z
integration_commit: 17cdafe9d9515c72045691b07420fbdfa25af81a
integration_notes: "cycle-122 D4. Applied clean. 4 libceed substrate ops (element_restrict/basis_apply/quad_point_contract/geom_factor_build) landed roadmap_goal; unresolved_depends_on_targets 6→2. 0 gate hits. See reports/cycle-122-integrator-staging/STAGING.md."
---

# CYCLE: Formalize the 4 libCEED contraction-substrate ops at L1 (cohort)

## Summary

The c121-D4 `libceed-quadrature-kernel-impl` roadmap_goal realizes the per-term FE-assembly leaf
`A(space, term)` as the five-stage libCEED contraction pipeline `A = Gᵀ B_𝒟ᵀ D B_𝒟 G`, and declares
**four `depends-on` targets that have no file** — `element_restrict` (G), `basis_apply` (B),
`quad_point_contract` (D), `geom_factor_build` (the geometry-factor build-pass). They are 4 of the 6
`unresolved_depends_on_targets` the graded-stack linter reports. This dispatch authors all four as
**rank-0 `roadmap_goal` chapters**: the HONEST clean-gate disposition (the planner flagged this, and
the upstream node's §Status already establishes it). Our firm L1 algebra is flat-vector BLAS-1/2 over
`Tensor[N]`; the libCEED kernel contracts over **rank-structured element-local tensors**
(`Tensor[(E, L)]` / `Tensor[(E, P, C)]` over an element axis `E` and a quad-point axis `P`) that **no
firm L1 operator carries**. Realizing them is a genuine **vocabulary shift**, not a re-expression in
existing terms — a firm/rough-in claim would assert the rank-structured substrate exists in our
vocabulary when it does not. Landing them `roadmap_goal` resolves the 4 unresolved targets to **LIVE
links** (the linker warning clears) with **no false firm claim**; the consumer
`libceed-quadrature-kernel-impl` correctly STAYS `roadmap_goal` (well-foundedness: rank-0 ≤ rank-0,
vacuously satisfied — it cannot exceed its least-resolved dep). This is the intended grounded-future
state, not a defect. None of the four is cleanly expressible in existing firm vocabulary, so none is
forced firm.

The decomposition itself is **structurally exhaustive and read directly off Palace source** (not
reconstructed from negative anchors): the four stages are the explicit field roles in Palace's
`AssembleCeedOperator` master assembler + the `f_build_geom_factor_*` build-QFunction. What is
speculative is only the *existence of firm L1 substrate operators* — hence rank-0, carrying the
constructive sketch + named shape groups + the cited Palace evidence.

## Proposed changes

```new:book/src/L1/element_restrict.md
---
layer: L1
operator: element_restrict
# Graded-stack: roadmap_goal (rank 0). One of the four libCEED contraction-substrate ops the
# `libceed-quadrature-kernel-impl` roadmap_goal (c121-D4) declares as depends-on targets. It is the
# G / Gᵀ stage of A = Gᵀ B_𝒟ᵀ D B_𝒟 G. Rank-0 because it operates on RANK-STRUCTURED element-local
# tensors (Tensor[(E, L)]) that our firm flat-vector-BLAS L1 vocabulary (Tensor[N]) does not carry —
# a genuine vocabulary shift, not a re-expression. A roadmap_goal may rest on anything (rank invariant
# rank(u) <= rank(v) is vacuous at rank 0). Reachable: pulled-by libceed-quadrature-kernel-impl, which
# reaches the feature root via the fe_assemble fold's 7 feature-column inbound edges.
rank: roadmap_goal
edges:
  reference:
    - target: L1/libceed-quadrature-kernel-impl
      kind: pulled-by      # the roadmap_goal consumer whose A = Gᵀ B_𝒟ᵀ D B_𝒟 G pipeline composes this G/Gᵀ stage (free; this node does not depend on its consumer)
    - target: concepts/tensor-field-lift   # Gᵀ scatter-add (assembly) is the element->global lift this substrate targets
---

# element_restrict

The **G / Gᵀ** stage of the libCEED element-quadrature contraction pipeline
`A = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G` (see [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md)):
the **element restriction** — a pure gather/scatter that maps the global true-dof vector to per-element
local-dof tensors (`G`, gather) and back by transpose scatter-add (`Gᵀ`, assembly). No arithmetic; it
is the indexing/permutation backbone of matrix-free FE operator application.

## Status

`roadmap_goal` (rank 0). **The clean-gate call is ROADMAP_GOAL, not firm/rough-in.** The Palace
realization is exhaustively anchored (see *Verified-against* — `CeedElemRestriction` construction and
its index-map builder), but the operator's signature contracts over a **rank-structured element-local
tensor** `Tensor[(E, L)]` (element axis `E`, local-dofs-per-element axis `L`) that **no firm L1
operator carries**: our firm L1 algebra is flat-vector BLAS-1/2 over `Tensor[N]` (the
`space.GetTrueVSize()` true-dof axis). Introducing the `[E, L]` element-rank structure is a genuine
**vocabulary shift**, so the honest disposition is rank-0 — it carries the constructive sketch and the
named shape groups, with NO claim that the rank-structured substrate exists in firm L1 vocabulary.
Promotion route: once the element-rank tensor substrate is firm L1 vocabulary, this promotes
`roadmap_goal → rough-in → firm` on the usual gates, and the consumer
`libceed-quadrature-kernel-impl`'s `depends-on` edge to it becomes firm-resting.

## L1 form (the constructive sketch)

For semantic/notation conventions (named shape groups, `Tensor[(S: ...)]` binding vs `Tensor[$S]`
use), see the governing surface `book/src/design/l4_calculus.md` §1.2.1 — not restated here.

    element_restrict :: ElemRestriction -> Tensor[(N: ...)] -> Tensor[(E, L)]
        -- G   (gather):  global true-dof vector -> per-element local-dof tensor
    element_restrict_t :: ElemRestriction -> Tensor[(E, L)] -> Tensor[(N: ...)]
        -- Gᵀ  (scatter-add / assembly): per-element local-dof tensor -> global true-dof vector
        --   N = space true-dof axis (flat, the firm Tensor[N] dof-vector — KEPT flat per L1/L0 convention)
        --   E = element count;  L = local dofs per element

`G` is a pure **gather**: it reads each element's local dofs from the shared global vector through the
element's local-dof → global-dof index map (built once per `(space, element-geometry)` pair). `Gᵀ` is
the **transpose scatter-add**: it sums each element-local contribution into its global slot — the
*assembly* operation (shared dofs at element boundaries receive a sum). The two are exact transposes:
`Gᵀ` is the adjoint of `G` under the standard inner products (no arithmetic beyond the scatter-add
accumulation).

The flat global axis `N` stays a genuine rank-1 `Tensor[(N: ...)]` dof-vector (the firm L1 `Tensor[N]`
convention for Palace `Vector` — KEPT flat). The element-local side `Tensor[(E, L)]` is the new
rank-structured axis this op introduces (the vocabulary shift). On a tensor-product element `L`
itself factors as a per-dimension dof product, but that factoring is an interior detail of `basis_apply`
(the sum-factorization sub-axis), not of the restriction.

## Algebraic laws (sketch — to be confirmed at promotion)

- **Transpose/adjoint pair:** `⟨G x, y⟩_{(E,L)} = ⟨x, Gᵀ y⟩_N` — `element_restrict_t` is the exact
  adjoint of `element_restrict` (the gather and the scatter-add are transposes of the same Boolean
  index map).
- **Gather is linear and a Boolean selection:** `G` carries no arithmetic; each output entry equals
  exactly one input entry (a 0/1 selection matrix), so `G (a·x + b·y) = a·(G x) + b·(G y)`.
- **`Gᵀ G` is the dof-multiplicity diagonal:** `Gᵀ G` acts on the global vector as multiplication by
  each true-dof's element-incidence count (the number of elements sharing that dof) — NOT the identity
  (shared dofs are counted with multiplicity). This is the standard FE assembly-multiplicity relation.
- **`G Gᵀ` is NOT the identity** on the element-local side (it averages-then-redistributes across the
  shared-dof equivalence classes) — stated as a non-law to forestall the false `G Gᵀ = I` assumption.

These are the standard restriction/prolongation algebra; they are sketched (not asserted firm) pending
the firm element-rank substrate.

## Applicability conditions

1. A standard FE basis with a tabulated `CeedElemRestriction` (the de-Rham family axis of
   [`weak_form_term`](./weak_form_term.md)); the lexicographic-vs-native ordering branch
   (`InitLexicoRestr` / `InitNativeRestr`) is an interior detail of the index-map construction.
2. Single-machine (per-`Ceed` device): the multi-rank shared-dof overlap (`ParMesh` assembly) is read
   single-rank per CLAUDE.md §Scope (DIRECTIVE-1 boundary) — the cross-rank scatter-add reconciliation
   is a deferred future direction, not lifted here.

## Verified-against

- `palace/fem/libceed/restriction.cpp:389-425` — `InitRestriction`: the element-restriction builder;
  dispatches lexicographic (`InitLexicoRestr`, `:113`) vs native (`InitNativeRestr`, `:207`) ordering
  for the local-dof → global-dof index map.
- `palace/fem/libceed/restriction.cpp:200` — `CeedElemRestrictionCreate(...)` — the libCEED restriction
  object built from the index map (the `G` realization; oriented variant `CeedElemRestrictionCreateOriented`
  at `:192`/`:372` for sign-carrying H(curl)/H(div) dofs).
- `palace/fem/bilinearform.cpp:64-70` — `trial_restr`/`test_restr` (`:64`/`:66`): the `G` operands the
  assembler receives (`GetCeedElemRestriction`); the per-element gather inputs to the leaf kernel.
- `book/src/L1/libceed-quadrature-kernel-impl.md` — the roadmap_goal consumer whose pipeline
  `A = Gᵀ B_𝒟ᵀ D B_𝒟 G` composes this `G`/`Gᵀ` stage (pulled-by).

## Related

- [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md) — the roadmap_goal that
  composes this stage (the `G`/`Gᵀ` ends of the pipeline).
- [`basis_apply`](./basis_apply.md) — the `B`/`Bᵀ` stage applied AFTER `G` (and before `Gᵀ`).
- `concepts/tensor-field-lift` — `Gᵀ` (assembly) is the element→global lift this substrate targets.
```

```new:book/src/L1/basis_apply.md
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
```

```new:book/src/L1/quad_point_contract.md
---
layer: L1
operator: quad_point_contract
# Graded-stack: roadmap_goal (rank 0). The D stage of A = Gᵀ B_𝒟ᵀ D B_𝒟 G — the pointwise per-quad-point
# contraction geom_data ⊙ (basis-evaluated trial). Rank-0: it operates on the quad-point-rank tensor
# Tensor[(E, P, C)] our firm flat-vector-BLAS L1 (Tensor[N]) does not carry. This is the
# embarrassingly-parallel diagonal of the pipeline (the per-quad-point lift). Reachable via
# libceed-quadrature-kernel-impl (pulled-by).
rank: roadmap_goal
edges:
  reference:
    - target: L1/libceed-quadrature-kernel-impl
      kind: pulled-by      # the roadmap_goal consumer whose pipeline composes this pointwise D stage (free)
    - target: L1/geom_factor_build   # produces the geom_data this op contracts against (the setup-stratum factor)
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

`roadmap_goal` (rank 0). **Clean-gate: ROADMAP_GOAL, not firm/rough-in.** The Palace realization is
exhaustively anchored (the apply-QFunction field wiring + the `f_apply_*` pointwise kernels — see
*Verified-against*), but the operator acts on the **quad-point-rank** tensor `Tensor[(E, P, C)]` (element
axis `E`, quad-point axis `P`, component axis `C`) that the firm flat-vector-BLAS L1 (`Tensor[N]`) does
not carry — a genuine **vocabulary shift** — so the honest disposition is rank-0. Note: the *pointwise*
elementwise-product structure (`⊙`) IS firm L1 vocabulary (`elementwise_product`), but it is firm only
over flat `Tensor[N]`; lifting it to the `[E, P, C]`-shaped diagonal is the substrate gap that keeps this
rank-0. Promotion route: firm when the quad-point-rank substrate (and the geom_data carrier) is firm L1
vocabulary.

## L1 form (the constructive sketch)

Semantic/notation conventions (named shape groups, the elementwise lift) live on
`book/src/design/l4_calculus.md` §1.2.1 — linked, not restated.

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

## Algebraic laws (sketch — to be confirmed at promotion)

- **Pointwise (no coupling across quadrature points):** `D` is block-diagonal in `(E, P)` — the output at
  `(e, p)` depends only on the input at `(e, p)` and `geom_data[e, p]`. The embarrassingly-parallel law.
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

- `palace/fem/libceed/integrator.cpp:451-512` — the apply-QFunction + operator-field wiring:
  `geom_data` input field (`:483-485`), optional `q_w` quad-weight (`:486-490`), active trial inputs /
  test outputs (`AddOperatorActiveInputFields` `:492`, `AddOperatorActiveOutputFields` `:493`) — the
  `B G` (input) / `Bᵀ Gᵀ` (output) field chains around the pointwise `D`.
- `palace/fem/libceed/integrator.cpp:215-308` — `QuadratureDataAssembly` (`:220`) + the `f_apply_*`
  pointwise apply-QFunctions selected by active-field component sizes — the `D` per-quad-point kernels.
- `palace/fem/libceed/integrator.cpp:423-465` — `AssembleCeedOperator` master assembler: the
  `geom_data` / `q_w` inputs that feed the pointwise contraction.
- `book/src/L1/libceed-quadrature-kernel-impl.md` — the roadmap_goal consumer (pulled-by).

## Related

- [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md) — composes this `D` stage.
- [`geom_factor_build`](./geom_factor_build.md) — the setup-stratum pass that produces the `geom_data`
  this op contracts against.
- [`basis_apply`](./basis_apply.md) — the `B`/`Bᵀ` stages on either side of `D`.
- `concepts/tensor-field-lift` — the per-quad-point lift this op realizes.
- [`elementwise_product`](./elementwise_product.md) — the firm flat-`Tensor[N]` pointwise multiply this
  op generalizes to the `[E, P, C]`-rank diagonal (the substrate gap that keeps it rank-0).
```

```new:book/src/L1/geom_factor_build.md
---
layer: L1
operator: geom_factor_build
# Graded-stack: roadmap_goal (rank 0). The geometry-factor build-pass (build-QFunction) of the libCEED
# pipeline: (mesh-nodes, quad-weights) → geom_data. Rank-0: it produces the per-quad-point geom_data
# carrier Tensor[(E, P, G)] — a setup-stratum rank-structured tensor our firm flat-vector-BLAS L1
# (Tensor[N]) does not carry. Setup-stratum (built once per mesh/order, reused across applies).
# Reachable via libceed-quadrature-kernel-impl (pulled-by) and quad_point_contract (which consumes geom_data).
rank: roadmap_goal
edges:
  reference:
    - target: L1/libceed-quadrature-kernel-impl
      kind: pulled-by      # the roadmap_goal consumer whose pipeline's D stage consumes this op's geom_data output (free)
    - target: concepts/build-time-vs-run-time-stratification   # this is the setup-stratum (build-once) factor of the build/apply split
---

# geom_factor_build

The **geometry-factor build-pass** (libCEED build-QFunction) of the contraction pipeline
`A = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G` (see [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md)):
precompute, per quadrature point, the `geom_data` that the `D` stage ([`quad_point_contract`](./quad_point_contract.md))
contracts against — the Jacobian-derived geometry metric times the quadrature weight. This is the
**setup-stratum** factor: built once per `(mesh, order)`, reused across every operator apply.

## Status

`roadmap_goal` (rank 0). **Clean-gate: ROADMAP_GOAL, not firm/rough-in.** The Palace realization is
exhaustively anchored (the `f_build_geom_factor_*` build-QFunction with its `attr`/`q_w`/`grad_x` inputs
and `geom_data` output — see *Verified-against*), but the operator produces the **quad-point-rank**
carrier `Tensor[(E, P, G)]` that the firm flat-vector-BLAS L1 (`Tensor[N]`) does not carry — a genuine
**vocabulary shift** — so the honest disposition is rank-0. Promotion route: firm when the quad-point-rank
geom_data carrier is firm L1 vocabulary.

## L1 form (the constructive sketch)

Semantic/notation conventions (named shape groups, the build/run-time stratification) live on
`book/src/design/l4_calculus.md` §1.2.1 + `concepts/build-time-vs-run-time-stratification` — linked, not
restated.

    geom_factor_build :: MeshNodes -> QuadWeights -> Tensor[(E, P, G)]
        -- per (e, p): geom_data[e,p] = f(J(mesh_nodes)[e,p], w[e,p])
        --   E = element count;  P = quadrature points per element;
        --   G = geom-data components (= 2 + space_dim*dim, the per-point metric storage)
        --   MeshNodes :: the high-order mesh-node coordinate field (the geometry dofs)
        --   QuadWeights :: the reference-element quadrature weights

The build-QFunction computes, per quadrature point `(e, p)`: the **Jacobian** `J` of the geometric map
(from the mesh-node gradient `grad_x`, evaluated by basis-eval mode `CEED_EVAL_GRAD`), the **quadrature
weight** `w` (`CEED_EVAL_WEIGHT`), and the **attribute** `attr` (material-region tag, `CEED_EVAL_INTERP`),
and packs the metric-times-weight into `geom_data` (`CEED_EVAL_NONE` output — a stored per-point tensor).
The geometry-metric form depends on the term's `𝒟`: `|J|·w` for mass (`Identity`), `J⁻ᵀ J⁻¹ |J|·w` for
grad-grad (`Gradient`/`Curl`/`Div`). Palace pre-multiplies the material **coefficient** `Q` into this
same `geom_data` (via the `attr`-keyed coefficient lookup), so the run-time `D` apply is a single
pointwise multiply.

This is the **setup stratum** of the build/run-time split (`concepts/build-time-vs-run-time-stratification`):
`geom_data` is computed once per `(mesh, order)` and reused across all operator applies — the geometry is
fixed, only the trial field varies per apply. (When the mesh moves — e.g. AMR refinement — `geom_data` is
rebuilt; that is a setup-stratum invalidation, not a run-time cost.)

## Algebraic laws (sketch — to be confirmed at promotion)

- **Setup-stratum purity:** `geom_factor_build` is a pure function of `(mesh_nodes, quad_weights)` — no
  field/state dependence; its output is cacheable and reused across applies (the build/run-time split law).
- **Pointwise/element-local:** `geom_data[e, p]` depends only on the local mesh-node Jacobian and weight
  at `(e, p)` — block-diagonal in `(E, P)`, no inter-point/inter-element coupling.
- **`𝒟`-determined metric shape:** the geometry-metric form (`|J|` vs `J⁻ᵀ J⁻¹ |J|`) is fixed by the
  term's differential operator — a configuration of the build, not a run-time branch.
- **Affine-element constancy (special case):** on a straight-sided (affine) element `J` is constant over
  the element, so `geom_data` is constant in `p` — a degenerate case worth noting (the curved/high-order
  case is the general one).

## Applicability conditions

1. A high-order mesh with a tabulated mesh `CeedBasis` for the geometry map (the `mesh_basis` / `mesh_restr`
   inputs); the `grad_x` Jacobian and `q_w` weight are evaluated by libCEED.
2. The geom-data storage size `2 + space_dim*dim` must match the geom-data restriction (the
   `MFEM_VERIFY(geom_data_size == 2 + space_dim*dim)` contract).
3. Single-machine (per-`Ceed` device).

## Verified-against

- `palace/fem/libceed/integrator.cpp:340-419` — the build-QFunction `f_build_geom_factor_*`: the
  `(dim, space_dim)`-keyed QFunction dispatch (`f_build_geom_factor_22`/`33`/`21`/`31`/`32`, `:352-377`),
  the inputs `attr` (`CEED_EVAL_INTERP`, `:386`), `q_w` (`CEED_EVAL_WEIGHT`, `:387-388`), `grad_x`
  (Jacobian, `CEED_EVAL_GRAD`, `:389-390`), and the `geom_data` output (`CEED_EVAL_NONE`, `:396-398`,
  size `2 + space_dim*dim` verified at `:394`).
- `palace/fem/libceed/integrator.cpp:423-465` — `AssembleCeedOperator`: the `geom_data` /
  `geom_data_restr` inputs the master assembler threads into the apply-QFunction (the build output's
  consumer site).
- `palace/fem/libceed/integrator.hpp:14-23` — `EvalMode` (`Weight`/`Grad`/`Interp`): the build inputs'
  evaluation modes.
- `book/src/L1/libceed-quadrature-kernel-impl.md` — the roadmap_goal consumer (pulled-by).

## Related

- [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md) — the roadmap_goal that
  consumes this op's `geom_data` output in its `D` stage.
- [`quad_point_contract`](./quad_point_contract.md) — the `D` stage that contracts against this op's
  `geom_data` (the run-time apply half of the build/apply split).
- `concepts/build-time-vs-run-time-stratification` — the setup/run-time stratification this op anchors.
```

```edit:book/src/L1/index.md
- **`libceed-quadrature-kernel-impl` is a `roadmap_goal` (kernel-impl)** *(cycle-121 D4)* — see [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md). The constructive, in-our-tensor-algebra realization of the per-term assembly leaf `A(space, term)` that [`fe_assemble`](./fe_assemble.md) folds over opaquely: the libCEED element-quadrature kernel as the contraction pipeline `A = Gᵀ B_𝒟ᵀ D(Q, geom) B_𝒟 G` (restriction-gather ▷ basis-eval ▷ pointwise geom×coeff×weight contraction ▷ basis-apply-transpose ▷ restriction-scatter). The DIRECTIVE-3 **kernel-impl** counterpart of the KEPT [`fe-assemble-libceed-boundary-obstruction`](../L1-L0/fe-assemble-libceed-boundary-obstruction.md) **kernel-api** surface, linked by a free `realizes-kernel-api` reference edge (NOT a `depends-on` — a reviewed correspondence, audited by `lowering-verifier`). **Rank-0 (roadmap_goal), NOT firm**, by the clean-gate: the per-element/per-quad-point tensor-contraction substrate (`element_restrict`/`basis_apply`/`quad_point_contract`/`geom_factor_build`) is a genuine vocabulary shift — our firm L1 algebra is flat-vector BLAS and does not carry the `[E, P, ...]` rank structure — so the honest disposition is a roadmap_goal carrying the constructive sketch + declaring the substrate it would rest on, NOT a firm claim. The obstruction theme STAYS the kernel-api surface (NOT downgraded). Promotes roadmap_goal→rough-in→firm once the substrate is mined (combinator-miner D6 of this cycle probes exactly this shared contraction core, shared with the D3 relaxation / D5 Krylov kernel-impls). Does NOT change the FE-assembly sub-spine firm count (still 4 firm).

**Roadmap_goal (libCEED contraction substrate — 4; opened cycle-122 D4)** — the four tensor-contraction substrate ops the `libceed-quadrature-kernel-impl` roadmap_goal (cycle-121 D4) declares as `depends-on` targets — the stages of the matrix-free FE operator-application pipeline `A = Gᵀ B_𝒟ᵀ D B_𝒟 G`. Authored as **rank-0 `roadmap_goal` chapters** (NOT firm/rough-in) by the clean-gate: each contracts over **rank-structured element-local / quad-point tensors** (`Tensor[(E, L)]` / `Tensor[(E, P, C)]`) that the firm flat-vector-BLAS L1 vocabulary (`Tensor[N]`) does **not** carry — a genuine vocabulary shift, not a re-expression in existing terms. Landing them roadmap_goal resolves 4 of the 6 `unresolved_depends_on_targets` to **LIVE links** with no false firm claim; the consumer `libceed-quadrature-kernel-impl` correctly STAYS roadmap_goal (well-foundedness: rank-0 ≤ rank-0). The decomposition is structurally exhaustive (read directly off `AssembleCeedOperator` + the build-QFunction); only the *existence of firm L1 substrate operators* is speculative. The four member bullets:

- **`element_restrict` is a `roadmap_goal`** *(cycle-122 D4)* — see [`element_restrict`](./element_restrict.md). The **G / Gᵀ** stage: the per-element gather (`G`, global true-dof → per-element local-dof `Tensor[(N: ...)] → Tensor[(E, L)]`) and its transpose scatter-add (`Gᵀ`, assembly). Pure gather/scatter, no arithmetic; `Gᵀ G` is the dof-multiplicity diagonal, `G Gᵀ ≠ I`. L0: `InitRestriction`/`CeedElemRestrictionCreate` (`palace/fem/libceed/restriction.cpp:389-425,:200`), `trial_restr`/`test_restr` (`palace/fem/bilinearform.cpp:64-70`).
- **`basis_apply` is a `roadmap_goal`** *(cycle-122 D4)* — see [`basis_apply`](./basis_apply.md). The **B / Bᵀ** stage: basis evaluation contracting per-element dofs to quad-point values `Tensor[(E, L)] → Tensor[(E, P, C)]`, keyed on the `EvalMode` (`Interp`/`Grad`/`Curl`/`Div`) the term's `𝒟` selects. Sum-factorization is a **transparent trick** (one-line note — resolves OQ `libceed-quadrature-kernel-impl-sum-factorization-classification`). L0: `AddQFunctionActiveInputs` (`palace/fem/libceed/integrator.cpp:25-65`), `EvalMode` (`palace/fem/libceed/integrator.hpp:14-23`), `InitBasis`/`InitTensorBasis` (`palace/fem/libceed/basis.cpp:169-180,:15-35`).
- **`quad_point_contract` is a `roadmap_goal`** *(cycle-122 D4)* — see [`quad_point_contract`](./quad_point_contract.md). The **D** stage: the pointwise per-quad-point contraction `geom_data ⊙ ·` over `Tensor[(E, P, C)]` — the embarrassingly-parallel diagonal (the per-quad-point lift `concepts/tensor-field-lift`). The flat-`Tensor[N]` pointwise multiply is firm (`elementwise_product`); lifting it to the `[E, P, C]` diagonal is the substrate gap. L0: the apply-QFunction wiring (`palace/fem/libceed/integrator.cpp:451-512`), the `f_apply_*` kernels (`:215-308`).
- **`geom_factor_build` is a `roadmap_goal`** *(cycle-122 D4)* — see [`geom_factor_build`](./geom_factor_build.md). The geometry-factor **build-pass**: `(mesh-nodes, quad-weights) → geom_data :: Tensor[(E, P, G)]` (Jacobian metric × quad-weight, with the material coefficient pre-multiplied in). The **setup stratum** of the build/run-time split (`concepts/build-time-vs-run-time-stratification`) — built once per `(mesh, order)`, reused across applies. L0: `f_build_geom_factor_*` (`palace/fem/libceed/integrator.cpp:340-419`; inputs `attr`/`q_w`/`grad_x` `:386-390`, output `geom_data` `:396-398`).
```

```edit:book/src/L1/index.md
| [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md) | `(space, term=(Q, 𝒟)) → LinearOperator[(N: ...)]` (i.e. the per-term assembly leaf `A(space, term) = Gᵀ B_𝒟ᵀ D(Q, geom) B_𝒟 G` — the libCEED element-quadrature kernel as a tensor-contraction pipeline) | composes the speculative tensor-contraction substrate `element_restrict` (G) / `basis_apply` (B) / `quad_point_contract` (D) / `geom_factor_build` (rough-in roadmap-deps; NOT firm yet); `realizes-kernel-api` (reference) → [`fe-assemble-libceed-boundary-obstruction`](../L1-L0/fe-assemble-libceed-boundary-obstruction.md); `realizes-leaf` (reference) the opaque `A(space, ·)` leaf of firm [`fe_assemble`](./fe_assemble.md) | `roadmap_goal` (**kernel-impl**; DIRECTIVE-3 item-2a constructive realization of the libCEED element-quadrature kernel; rank-0 because the per-element/per-quad-point tensor-contraction substrate is a genuine vocabulary shift NOT yet firm L1 vocabulary — flat-vector BLAS does not carry the `[E, P, ...]` rank structure; the obstruction theme is KEPT as the kernel-api surface, NOT downgraded; `realizes-kernel-api` is a free reference edge, NOT depends-on; promotes roadmap_goal→rough-in→firm once the substrate is mined — combinator-miner D6 probes exactly this shared contraction core; proposed-by: abstractor:2026-06-07T054924Z-abstractor-libceed-quadrature-kernel-impl) |
| [`element_restrict`](./element_restrict.md) | `ElemRestriction → Tensor[(N: ...)] → Tensor[(E, L)]` (G, gather); transpose `Tensor[(E, L)] → Tensor[(N: ...)]` (Gᵀ, scatter-add/assembly) | `pulled-by` (reference) [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md) — the G/Gᵀ stage of its `A = Gᵀ B_𝒟ᵀ D B_𝒟 G` pipeline; references `concepts/tensor-field-lift` (Gᵀ assembly) | `roadmap_goal` (rank-0 libCEED contraction substrate; the per-element gather/scatter over the `[E, L]` element-rank tensor our firm flat-vector-BLAS L1 does not carry — a genuine vocabulary shift, NOT a forced firm claim; resolves 1 of 6 `unresolved_depends_on_targets`; proposed-by: harvester:2026-06-07T071941Z-harvester-libceed-substrate-ops) |
| [`basis_apply`](./basis_apply.md) | `BasisMode → Basis → Tensor[(E, L)] → Tensor[(E, P, C)]` (B, basis-eval); transpose `Tensor[(E, P, C)] → Tensor[(E, L)]` (Bᵀ) | `pulled-by` (reference) [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md) — the B/Bᵀ stage; references [`weak_form_term`](./weak_form_term.md) (𝒟 selects the EvalMode) | `roadmap_goal` (rank-0 libCEED contraction substrate; basis-eval keyed on the EvalMode the term's `𝒟` selects, over the `[E, P, C]` quad-point-rank tensor not in firm L1; sum-factorization a transparent trick; resolves 1 of 6 `unresolved_depends_on_targets`; proposed-by: harvester:2026-06-07T071941Z-harvester-libceed-substrate-ops) |
| [`quad_point_contract`](./quad_point_contract.md) | `GeomData → Tensor[(E, P, C)] → Tensor[(E, P, C')]` (D, pointwise per-quad-point `geom_data ⊙ ·`) | `pulled-by` (reference) [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md) — the D stage (embarrassingly-parallel diagonal); references [`geom_factor_build`](./geom_factor_build.md) (produces geom_data) + `concepts/tensor-field-lift` | `roadmap_goal` (rank-0 libCEED contraction substrate; the per-quad-point pointwise contraction over the `[E, P, C]` quad-point-rank tensor; the flat-`Tensor[N]` `elementwise_product` is firm but the `[E,P,C]` diagonal lift is the substrate gap; resolves 1 of 6 `unresolved_depends_on_targets`; proposed-by: harvester:2026-06-07T071941Z-harvester-libceed-substrate-ops) |
| [`geom_factor_build`](./geom_factor_build.md) | `MeshNodes → QuadWeights → Tensor[(E, P, G)]` (geometry-factor build-pass: Jacobian metric × quad-weight, coefficient pre-multiplied) | `pulled-by` (reference) [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md) — the build-QFunction whose geom_data its D stage consumes; references `concepts/build-time-vs-run-time-stratification` | `roadmap_goal` (rank-0 libCEED contraction substrate; the setup-stratum geometry-factor pass over the `[E, P, G]` quad-point-rank carrier not in firm L1; built once per `(mesh, order)`, reused across applies; resolves 1 of 6 `unresolved_depends_on_targets`; proposed-by: harvester:2026-06-07T071941Z-harvester-libceed-substrate-ops) |
```

```edit:book/src/SUMMARY.md
  - [libceed-quadrature-kernel-impl](./L1/libceed-quadrature-kernel-impl.md)
  - [element_restrict](./L1/element_restrict.md)
  - [basis_apply](./L1/basis_apply.md)
  - [quad_point_contract](./L1/quad_point_contract.md)
  - [geom_factor_build](./L1/geom_factor_build.md)
```

## Operator content

The four chapters are authored in full inside the proposed-changes fences above. Each is a rank-0
`roadmap_goal` carrying: a one-line role, `## Status` (the clean-gate ROADMAP_GOAL justification), the
`## L1 form` constructive sketch (Haskell-style signatures + named shape groups; USE+LINK to the
semantic surface, no restated general rule), sketched `## Algebraic laws` (marked "to be confirmed at
promotion" — NOT asserted firm), `## Applicability conditions`, codemap-verified `## Verified-against`,
and `## Related`. The named shape groups are load-bearing here: `Tensor[(N: ...)]` for the flat global
dof axis (KEPT flat per the L1/L0 `Tensor[N]` convention), and the new rank-structured
`Tensor[(E, L)]` / `Tensor[(E, P, C)]` / `Tensor[(E, P, G)]` element/quad-point axes that ARE the
vocabulary shift keeping these rank-0.

## Supporting evidence

Citations are relative to `reference/` following the established project convention used by the
sibling firm chapters (source files under the doubled `reference/palace/palace/...` on-disk tree are
cited as `palace/fem/...`; test files under `reference/palace/test/...` are cited as
`palace/test/...`). All anchors below were verified this cycle via `palace-codemap` read_range +
`tools/citecheck/citecheck.py --anchor` against the on-disk file (the doubled-`palace/palace/` path):

- `element_restrict` — `restriction.cpp:389` `InitRestriction` [ok]; `:200` `CeedElemRestrictionCreate`
  [ok]; `bilinearform.cpp:64` `trial_restr` [ok].
- `basis_apply` — `palace/fem/libceed/integrator.cpp:25` `AddQFunctionActiveInputs` [ok];
  `palace/fem/libceed/integrator.hpp:15` `EvalMode` (in range 14-23) [ok]; `basis.cpp:169` `InitBasis`
  [ok]; `:15` `InitTensorBasis` [ok]; `:35` `CeedBasisCreateTensorH1` [ok].
- `quad_point_contract` — `palace/fem/libceed/integrator.cpp:492` `AddOperatorActiveInputFields` (in
  range 451-512) [ok]; `:423` `AssembleCeedOperator` [ok]; `:220` `QuadratureDataAssembly` (in range
  215-308) [ok].
- `geom_factor_build` — `palace/fem/libceed/integrator.cpp:340-419` `f_build_geom_factor_*` (anchors at
  :352-377) [ok]; `:390` `grad_x` (in range 386-390) [ok]; `:423` `AssembleCeedOperator` [ok].
- `TestCeedOperatorFullAssemble` `palace/test/unit/test-libceed.cpp:284` [ok] — the empirical anchor
  (assembled matrix matches MFEM reference to 1e-12) cited by the consumer's D6 audit; referenced
  indirectly via the consumer, not load-bearing for these rank-0 substrate sketches.

Motivating reports: the c121-D4 abstractor (`2026-06-07T054924Z-abstractor-libceed-quadrature-kernel-impl`,
which authored the consumer roadmap_goal and named these 4 targets) and the c122 planner D4 row.

## Open questions / caveats

- **`libceed-quadrature-kernel-impl` STAYS `roadmap_goal` after this dispatch** — this is the CORRECT
  grounded-future state, not a missed promotion. Its 4 `depends-on` edges now resolve to LIVE rank-0
  roadmap_goal nodes (the `unresolved_depends_on_targets` count drops 6→2, the remaining 2 being the
  D1/D2 AMR verbs). Well-foundedness holds vacuously (rank-0 ≤ rank-0). The OQ
  `libceed-quadrature-kernel-impl-roadmap-goal-vs-rough-in-disposition` resolves: STAYS roadmap_goal
  (the substrate is roadmap_goal, so the consumer cannot exceed it). The consumer's `depends-on` edge
  labels currently say "rough-in; no anchor yet" in its frontmatter NOTE comment — that comment is now
  stale (the targets exist as roadmap_goal). I did NOT edit the consumer file (it is D6's audit target
  this cycle, marked SEQUENTIAL in the overlap analysis — same-file region touch). **Flag for the
  integrator / D6:** the consumer's frontmatter `depends-on` NOTE comment (lines 27-40) and the
  "Speculative L1 operators (rough-in; harvester promotion targets)" section (lines 166-177) should be
  re-anchored to "roadmap_goal (authored c122 D4)" — a navigational text refresh, deferred to avoid the
  same-file collision the planner flagged.
- **OQ `libceed-quadrature-kernel-impl-sum-factorization-classification` RESOLVED** — sum-factorization
  is a **transparent performance trick** (the L1 form is the dense per-element basis contraction;
  sum-factorization changes the contraction ORDER not the RESULT). Recorded as a one-line note in
  `basis_apply` §"L1 form" + a non-law "sum-factorization invariance".
- **The four substrate ops are sketched-not-firm by design.** Their algebraic laws are stated as
  "sketch — to be confirmed at promotion" (the standard restriction/basis/pointwise-contraction
  algebra), NOT asserted firm. A firm flip requires the **element-rank / quad-point-rank tensor
  substrate** to become firm L1 vocabulary — the genuine vocabulary shift. This is the consumer-gated
  promotion route the combinator-miner shared-substrate probe (c121 D6) targets; flag for the batch-39
  meta whether to schedule a dedicated "element-local rank-structured tensor" L1 vocabulary front
  (which would simultaneously firm all four + the consumer).
- **`GeomData` / `BasisMode` / `ElemRestriction` are signature-named types without a full definition
  home.** `BasisMode` is the `EvalMode` enum (`{Interp, Grad, Curl, Div}`, cited
  `palace/fem/libceed/integrator.hpp:14-23`)
  — adequately pinned in-line. `GeomData` is the `Tensor[(E, P, G)]` carrier (defined inline in
  `geom_factor_build`). `ElemRestriction` / `Basis` are the opaque libCEED handles (`CeedElemRestriction`
  / `CeedBasis`) — used opaquely, not records to define. Since these substrate ops are themselves rank-0
  roadmap_goal (the rank structure is the open vocabulary), a full `## Record definition` section would
  over-commit; the inline pinning is appropriate at rank-0. If/when the cohort firms, the rank-structured
  tensor carrier likely wants a `concepts/element-local-tensor.md` definition home — flag
  `record-element-local-tensor-needs-definition-home-at-firming` (deferred, gated on the firm flip).
- **Single-machine boundary (DIRECTIVE-1):** the cross-rank shared-dof scatter-add reconciliation in
  `element_restrict`'s `Gᵀ` (ParMesh assembly overlap) is read single-rank and noted as a deferred
  future direction, NOT lifted — consistent with the consumer's applicability condition 3.
- **Index registration:** I authored my own dep-map table rows (4) + my own §Vocabulary-cohort bullet
  block (the new "Roadmap_goal (libCEED contraction substrate — 4)" subsection) + the 4 SUMMARY
  entries. There is **no consolidated running-count tally** for this new group (it is a fresh rank-0
  group, distinct from the FE-assembly firm count which is explicitly unchanged at 4), so no tally to
  defer. The FE-assembly sub-spine firm-count prose is untouched (these are roadmap_goal, not firm).
