---
layer: L1
operator: libceed-quadrature-kernel-impl
# Graded-stack scheme. This is a firm (rank 3) kernel-IMPL node (DIRECTIVE-3 item-2a):
# the constructive, in-our-tensor-algebra realization of the libCEED element-quadrature kernel
# that the firm `fe_assemble` fold (`K = Σ_i A(space, term_i)`) folds over opaquely as the leaf
# `A(space, term)`. Promoted roadmap_goal → rough-in (cycle-124 D5) → firm (cycle-125 D1): its
# constructive constituents — the four element-local tensor-contraction substrate ops — are now ALL
# firm L1 vocabulary (`basis_apply` + `quad_point_contract` FIRM c124 D3; `element_restrict` +
# `geom_factor_build` FIRM c125 D1, the moment their `concepts/element-local-tensor` shape home firmed,
# c124 D5). Per the well-foundedness cap `rank(impl) <= min over depends-on deps of rank(v)`: with all
# four `composes` deps firm, min = firm, so this node promotes firm on the firm-on-positive-structure
# escape (its laws are syntactic-identity composition facts on the positively-read `AssembleCeedOperator`
# pipeline — no test gates them). The `realizes-kernel-api` edge to the KEPT obstruction theme stays
# `reference`-class (navigational/free — NOT depends-on; it does not block, does not constrain rank,
# does not carry liveness — it is a correspondence to be REVIEWED, audited by lowering-verifier).
# Pulled-by: `fe_assemble` (firm, the spine consumer whose opaque leaf this realizes) reaches the
# feature root via 7 feature-column inbound edges — so this node is reachable (not speculation-noise).
rank: firm
edges:
  reference:
    - target: L1-L0/fe-assemble-libceed-boundary-obstruction
      kind: realizes-kernel-api    # the kernel-api obstruction surface this impl realizes (free, navigational; the reviewed correspondence — NOT depends-on)
    - target: L1/fe_assemble
      kind: realizes-leaf          # the firm fold whose opaque per-term leaf A(space, term) THIS is the constructive interior of (free; fe_assemble does NOT depend on the impl — it folds over A opaquely)
    - target: L1/weak_form_term    # the (coefficient, differential-operator) pair whose differential-operator selects the basis-eval mode B and whose coefficient enters the pointwise contraction D
    - target: concepts/tensor-field-lift   # the contraction pipeline is the matrix-free GPU-tensor target form (backend-lowering)
  depends-on:
    # The tensor-contraction substrate operators this impl rests on — all four now FIRM L1 vocabulary
    # (basis_apply + quad_point_contract firm c124 D3; element_restrict + geom_factor_build firm c125 D1),
    # typed over the firm concepts/element-local-tensor shape family (c124 D5). With all four firm,
    # rank(impl) <= min(deps) = firm, so this node is firm.
    - target: L1/element_restrict        # G — global-dof → per-element-dof gather (firm c125 D1)
      kind: composes
    - target: L1/basis_apply             # B — per-element-dof → per-quad-point eval (interp/grad/curl/div) (firm c124 D3)
      kind: composes
    - target: L1/quad_point_contract     # D — pointwise geom×coeff×weight contraction at quad points (firm c124 D3)
      kind: composes
    - target: L1/geom_factor_build       # the build-QFunction: Jacobian × quad-weight → geom_data (firm c125 D1)
      kind: composes
---

# libceed-quadrature-kernel-impl

The constructive, in-our-tensor-algebra realization of the **libCEED element-local quadrature
kernel** — the per-term assembly leaf `A(space, term)` that the firm
[`fe_assemble`](./fe_assemble.md) fold `K = Σ_i A(space, term_i)` quantifies over **opaquely**, and
whose library boundary is documented (claim-free) by the
[`fe-assemble-libceed-boundary-obstruction`](../L1-L0/fe-assemble-libceed-boundary-obstruction.md)
theme. This chapter is the **kernel-impl** counterpart of that **kernel-api** surface, per the
DIRECTIVE-3 kernel-API/impl distinction (CLAUDE.md §Methodology-invariants "Kernel-API vs
kernel-IMPLEMENTATION distinction"): the obstruction theme stays the opaque-boundary CONTRACT (what
the spine calls); THIS node is the from-our-firm-primitives version (how it would be realized as
tensor contractions). A reviewer reads both and checks they match; `lowering-verifier` audits the
correspondence.

## Status

`firm` (rank 3) — **kernel-impl** (the DIRECTIVE-3 role-label; this node is the constructive
realization, NOT the API surface). **Promoted roadmap_goal → rough-in (cycle-124 D5) → firm
(cycle-125 D1).** The operator decomposition is well-understood and exhaustively anchored in the Palace
libCEED source (see *Evidence*), and its constructive constituents — the per-element /
per-quadrature-point tensor-contraction substrate — are now **all firm L1 vocabulary**: `basis_apply` +
`quad_point_contract` firmed c124 D3, and `element_restrict` + `geom_factor_build` firmed c125 D1 (the
moment their `concepts/element-local-tensor` shape home firmed, c124 D5). The genuine vocabulary shift
away from flat-vector BLAS (`Tensor[N]`) to the rank-structured element-local tensors (`[E, L]` /
`[E, P, C]` / `[E, P, G]`, `concepts/element-local-tensor`) is realized and firm.

**The rank rises to firm by well-foundedness** (CLAUDE.md §Methodology-invariants: an entry is at most
as resolved as its least-resolved dependency — the graded-stack `rank(u) ≤ rank(v)` invariant): the
four `depends-on (composes)` substrate deps are now all firm, so
`rank(impl) ≤ min over composes deps of rank(v) = firm`. The cap that held this node at rough-in
(`element_restrict` / `geom_factor_build` rough-in, c124 D4) lifted the moment those two firmed (c125
D1) — which in turn happened the moment their `concepts/element-local-tensor` shape home firmed (c124
D5). The promotion is on the **firm-on-positive-structure escape**: the laws are syntactic-identity
composition facts on the positively read `AssembleCeedOperator` pipeline (no test gates them — the
`AssembleCeedOperator` master assembler wires restriction → basis → QFunction → basis → restriction,
read directly).

**The `realizes-kernel-api` link is `reference`-class (free, navigational).** This impl does **not**
`depends-on` the opaque API; the relationship is a *correspondence to be reviewed*, not a build
dependency, so it must not constrain rank or carry liveness (CLAUDE.md DIRECTIVE-3). The linters
ignore the `realizes-kernel-api` label via the optional-`kind:`-is-documentation mechanism — no new
linter edge-semantics. Likewise the `realizes-leaf` edge to `fe_assemble` is `reference`-class:
`fe_assemble` stays firm and folds over `A` **opaquely**; it does not depend on this impl (the fold's
firmness is independent of how the leaf is computed — see the obstruction theme's §"`fe_assemble`
stays FIRM"). The firm-flip is on this kernel-IMPL node ONLY; the kernel-api obstruction surface is
untouched (it KEEPS `obstruction (opaque-library-ownership)`).

## L1 form (the constructive realization)

The kernel realizes the per-term leaf `A(space, term)` — one weak-form term's element-local→global
linear-operator contribution — as the standard **libCEED operator decomposition**, a five-stage
contraction pipeline. Writing `term = (Q, 𝒟)` (a [`weak_form_term`](./weak_form_term.md): coefficient
`Q`, differential-operator `𝒟 ∈ {Identity, Gradient, Curl, Divergence}`):

    A(space, (Q, 𝒟)) = Gᵀ ∘ B_𝒟ᵀ ∘ D(Q, geom) ∘ B_𝒟 ∘ G
        -- A(space, term) :: LinearOperator[(N: ...)]   (N = space true-dof axis)
        -- as a tensor-contraction pipeline over an element axis E and a quad-point axis P

Stage-by-stage (each stage is a firm substrate operator):

- **G — element restriction (gather).** `element_restrict :: Tensor[(N: ...)] -> Tensor[(E, L)]`
  scatters the global true-dof vector into per-element local-dof tensors (`E` = element count,
  `L` = local dofs per element). The libCEED `CeedElemRestriction` (`trial_restr`/`test_restr`,
  built by Palace at `bilinearform.cpp:64-66`; the index map `restriction.cpp`). Pure
  gather/scatter — no arithmetic; `Gᵀ` is the transpose scatter-add (assembly). **Firm** (c125 D1).

- **B — basis evaluation.** `basis_apply :: BasisMode -> Tensor[(E, L)] -> Tensor[(E, P, C)]`
  contracts the per-element dofs against the tabulated basis (and its derivatives) to produce values
  at quadrature points: `interp` (values), `grad`/`curl`/`div` (derivatives), selected by the
  `EvalMode` the term's `𝒟` determines (`palace/fem/libceed/integrator.hpp:14-23` —
  `Weight/Interp/Grad/Div/Curl`). The libCEED `CeedBasis` (`trial_basis`/`test_basis`,
  `bilinearform.cpp:68-69`). On a tensor-product element this `B` itself factors into a sum-factorized
  sequence of 1-D contractions (the matrix-free efficiency win) — a sub-axis the impl notes but does
  not need at L1. **Firm** (c124 D3).

- **D — pointwise quadrature contraction.** `quad_point_contract :: Tensor[(E, P, C)] -> GeomData ->
  Tensor[(E, P, C)]` applies, **independently at each quadrature point**, the product of three
  factors: the **coefficient** `Q` (the material property — `ε`, `μ⁻¹`, …), the **geometry factor**
  (the Jacobian-derived metric `J⁻ᵀ J⁻¹ |J|` for grad-grad / `|J|` for mass), and the **quadrature
  weight** `w`. In Palace these three are **pre-multiplied into `geom_data`** by a separate build
  pass (see `geom_factor_build` below), so the run-time apply-QFunction `f_apply_*` is a single
  pointwise `geom_data ⊙ (basis-evaluated trial)` (`palace/fem/libceed/integrator.cpp:451-512`, the
  apply-QFunction field wiring; `f_apply_22`/`f_apply_33`/… the per-(dim,space_dim) pointwise
  kernels). This is the
  **embarrassingly-parallel diagonal** of the pipeline — exactly the per-quad-point lift
  `concepts/tensor-field-lift` describes, and the natural GPU-tensor form. **Firm** (c124 D3).

- **geom_factor_build — the build-QFunction.** `geom_factor_build :: MeshNodes -> QuadWeights ->
  GeomData` precomputes `geom_data` per quadrature point from the mesh-node Jacobian (`grad_x`,
  `CEED_EVAL_GRAD`) and the quadrature weight (`q_w`, `CEED_EVAL_WEIGHT`):
  `f_build_geom_factor_*` (`palace/fem/libceed/integrator.cpp:340-419`; inputs `attr`/`q_w`/`grad_x` at `:386-390`,
  output `geom_data` at `:397`). This is the **setup-stratum** factor (built once per mesh/order,
  reused across applies) — a build-time-vs-run-time stratification
  (`concepts/build-time-vs-run-time-stratification`). **Firm** (c125 D1).

The composite `A` is then `Gᵀ B_𝒟ᵀ D B_𝒟 G`, and `fe_assemble`'s fold sums these per-term:
`K = Σ_i A(space, term_i)` (the firm fold; `AddSubOperator` at `bilinearform.cpp:77`). The two
representation variants the obstruction theme catalogues map cleanly onto this pipeline: **partial
assembly (matrix-free)** keeps `A` as the un-materialized operator (apply the pipeline on demand);
**full assembly** materializes `A` by applying the pipeline to the identity columns and extracting
COO triples (`CeedOperatorAssembleCOO`, `palace/fem/libceed/operator.cpp:483`) — a derived materialization of
the same contraction, not a different algorithm.

## Applicability conditions

The constructive realization is faithful when:

1. The element basis is a **standard FE basis** (nodal Lagrange / Nédélec / Raviart-Thomas /
   discontinuous-L2) with a tabulated `CeedBasis` — true for all in-scope Palace pipelines
   (`weak_form_term`'s de-Rham family axis). GSLIB point-interpolation is a *different* facility
   (`obstruction (opaque-library-ownership)`, see [`interpolator`](./interpolator.md)) and is NOT
   realized by this kernel.
2. The term's differential operator `𝒟` is one of `{Identity, Gradient, Curl, Divergence}` (the
   firm `weak_form_term` axis) — these select the `B` basis-eval mode (`Interp`/`Grad`/`Curl`/`Div`)
   and the `D` geometry-factor shape. Non-de-Rham / non-polynomial integrands are out of scope.
3. Single-machine (per-`Ceed` device) — parallelism is by composition; the multi-rank
   element-restriction overlap (`ParMesh` shared-dof assembly) is read single-rank per CLAUDE.md
   §Scope (DIRECTIVE-1 boundary).

## Justification kind

**structural** — the decomposition `A = Gᵀ Bᵀ D B G` is the canonical libCEED operator structure and
is read directly off the Palace `AssembleCeedOperator` master assembler (the operator-field wiring
that connects restriction → basis → QFunction → basis → restriction) plus the build-QFunction
geometry-factor pass. The five stages are not reconstructed from negative anchors; they are the
explicit field roles in the Palace libCEED operator-construction code. The four firm substrate
operators realize the contraction stages, so this node is firm (the firm-on-positive-structure escape
on a fully-firm substrate).

## Substrate L1 operators (c124/c125 cohort: 4 firm)

The four contraction-substrate operators are all live, firm L1 vocabulary (D3 firmed two, c125 D1
firmed the other two), typed over the firm `concepts/element-local-tensor` shape family, wired as this
impl's `depends-on (composes)` substrate:

- [`element_restrict`](./element_restrict.md) — `G`/`Gᵀ`: the per-element gather/scatter
  `Tensor[(N: ...)] ↔ Tensor[(E, L)]`. **`firm`** (c125 D1; firm-on-positive-structure once its
  `concepts/element-local-tensor` shape home firmed).
- [`basis_apply`](./basis_apply.md) — `B`/`Bᵀ`: the basis-eval contraction
  `Tensor[(E, L)] ↔ Tensor[(E, P, C)]`, keyed on the `EvalMode` the term's `𝒟` selects. **`firm`**
  (c124 D3; firm-on-positive-structure).
- [`quad_point_contract`](./quad_point_contract.md) — `D`: the pointwise per-quad-point
  `geom_data ⊙ ·` contraction (the embarrassingly-parallel lift). **`firm`** (c124 D3;
  firm-on-positive-structure).
- [`geom_factor_build`](./geom_factor_build.md) — the setup-stratum build-QFunction
  `(mesh-nodes, quad-weights) → geom_data :: Tensor[(E, P, G)]`. **`firm`** (c125 D1;
  firm-on-positive-structure once its `concepts/element-local-tensor` shape home firmed).

The shared shape vocabulary these four are typed over is [`concepts/element-local-tensor`](../concepts/element-local-tensor.md)
(c124 D5, firm). With all four substrate deps firm, this impl is firm by well-foundedness
(`rank(impl) ≤ min(deps) = firm`), on the firm-on-positive-structure escape.

## Verified-against

- `palace/fem/libceed/integrator.cpp:423-445` — `AssembleCeedOperator` master assembler signature
  (`trial_restr`/`test_restr`/`trial_basis`/`test_basis`/`geom_data`/`geom_data_restr`) — the five
  inputs that wire the `Gᵀ Bᵀ D B G` pipeline.
- `palace/fem/libceed/integrator.cpp:451-512` — the apply-QFunction + operator-field wiring:
  `geom_data` input, optional `q_w` quad-weight (`:459-462`), active trial inputs / test outputs
  (`AddOperatorActiveInputFields` `:492`, `AddOperatorActiveOutputFields` `:493`) — the
  `B G` (input) and `Bᵀ Gᵀ` (output) field chains around the pointwise `D`.
- `palace/fem/libceed/integrator.cpp:340-419` — the build-QFunction `f_build_geom_factor_*`: geometry
  factor from `grad_x` (Jacobian, `CEED_EVAL_GRAD` `:390`) × quad weight (`q_w`, `CEED_EVAL_WEIGHT`
  `:388`) → `geom_data` (`:397`) — the `geom_factor_build` setup-stratum stage.
- `palace/fem/libceed/integrator.cpp:215-308` — `QuadratureDataAssembly` + the `f_apply_*` pointwise
  apply-QFunctions selected by active-field sizes — the `D` per-quad-point contraction kernels.
- `palace/fem/libceed/integrator.hpp:14-23` — `enum EvalMode { Weight, None, Interp, Grad, Div,
  Curl }` — the `B` basis-eval modes the term's `𝒟` selects.
- `palace/fem/integrator.hpp:58-61` — `BilinearFormIntegrator::Assemble` pure-virtual leaf-kernel
  contract (the boundary the obstruction theme documents; the dispatch this impl realizes).
- `palace/fem/bilinearform.cpp:64-70` — Palace-supplied restriction/basis inputs (`trial_restr`
  `:64`, `test_restr` `:66`, `trial_basis` `:68`, `test_basis` `:69`) — the `G`/`B` operands.
- `book/src/L1/fe_assemble.md` — the firm fold whose opaque leaf `A(space, term)` this realizes.
- `book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md` — the KEPT kernel-api obstruction
  surface this `realizes-kernel-api`.

## Related

- [`fe-assemble-libceed-boundary-obstruction`](../L1-L0/fe-assemble-libceed-boundary-obstruction.md)
  — the **kernel-api** surface (kept, NOT downgraded); this node is its **kernel-impl** counterpart
  via the `realizes-kernel-api` `reference` edge.
- [`fe_assemble`](./fe_assemble.md) — the firm fold; `A(space, term)` is the opaque leaf it folds.
- [`weak_form_term`](./weak_form_term.md) — `(Q, 𝒟)`; `𝒟` selects `B`, `Q` enters `D`.
- [`interpolator`](./interpolator.md) — the de-Rham discrete grid-transfer operator (a DIFFERENT FE
  facility; its GSLIB point-interp sibling is a separate obstruction, not realized here).
- `concepts/tensor-field-lift`, `concepts/build-time-vs-run-time-stratification` — the per-quad-point
  lift + the setup/run-time stratification the pipeline uses.

```yaml
verified_against:
  - citation: book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md
    verdict: realizes-kernel-api-faithful
    audited_at: 2026-06-07T093000Z
    note: STRUCTURAL correspondence audit (c124 D2). The five-stage A = Gᵀ B_𝒟ᵀ D B_𝒟 G pipeline maps 1:1 onto the kernel-api leaf contract (palace/fem/integrator.hpp:58-61 Assemble pure-virtual; restriction/basis/geom_data field roles). realizes-kernel-api edge confirmed reference-class (NOT depends-on); API stays obstruction(opaque-library-ownership), undowngraded; fe_assemble stays firm. The c125 D1 firm-flip changes only this impl node's RANK (to firm), not the correspondence — re-audit owed by lowering-verifier as the impl firms (empirical-match target test-libceed.cpp:284 below).
  - citation: reference/palace/palace/fem/libceed/integrator.cpp:423-445
    verdict: supports
    audited_at: 2026-06-07T093000Z
    note: AssembleCeedOperator master assembler signature with trial_restr/test_restr/trial_basis/test_basis/geom_data/geom_data_restr inputs (:423-427) — the five inputs wiring Gᵀ Bᵀ D B G; on-disk awk read, exact. Re-confirmed via codemap read_range :423-427 this dispatch (c125 D1).
  - citation: reference/palace/palace/fem/integrator.hpp:58-61
    verdict: supports
    audited_at: 2026-06-07T093000Z
    note: BilinearFormIntegrator::Assemble pure-virtual leaf-kernel contract (= 0) — the SHARED anchor on which the impl-realizes-api correspondence pivots (the impl's A(space,term) IS the constructive interior of this opaque dispatch); exact. Re-confirmed via citecheck --anchor Assemble this dispatch (c125 D1).
  - citation: reference/palace/palace/fem/libceed/integrator.cpp:340-419
    verdict: supports
    audited_at: 2026-06-07T093000Z
    note: build-QFunction f_build_geom_factor_* — attr CEED_EVAL_INTERP (:387), q_w CEED_EVAL_WEIGHT (:388), grad_x CEED_EVAL_GRAD (:389-390), geom_data output + 2+space_dim*dim verify (:395-397); the geom_factor_build stage; exact.
  - citation: reference/palace/palace/fem/libceed/integrator.cpp:451-512
    verdict: supports
    audited_at: 2026-06-07T093000Z
    note: apply-QFunction/operator-field wiring — geom_data input (:457-458), q_w CEED_EVAL_WEIGHT (:462), AddOperatorActiveInputFields (:492) / AddOperatorActiveOutputFields (:493); the B G input / Bᵀ Gᵀ output chains around the pointwise D; in-range.
  - citation: reference/palace/palace/fem/libceed/integrator.hpp:14-23
    verdict: supports
    audited_at: 2026-06-07T093000Z
    note: enum EvalMode { Weight None Interp Grad Div Curl } (:15-23) — the B basis-eval modes the term's 𝒟 selects; exact.
  - citation: reference/palace/palace/fem/bilinearform.cpp:64-70
    verdict: supports
    audited_at: 2026-06-07T093000Z
    note: Palace-supplied restriction/basis inputs trial_restr :64 test_restr :66 trial_basis :68 test_basis :69; leaf call integ->Assemble :75; fold AddSubOperator :77; exact (the G/B operands + the firm fold L0 home).
  - citation: reference/palace/test/unit/test-libceed.cpp:284
    verdict: empirical-match
    audited_at: 2026-06-07T134107Z
    note: FIRMING empirical-match re-audit (c126 D2; owed since c124 now the impl is firm c125 D1). TestCeedOperatorFullAssemble (:284) asserts mat_diff MaxNorm < 1.0e-12 * max(mat_ref MaxNorm, 1.0) at :298 — the libCEED-assembled matrix (mat_test, from a_test.PartialAssemble then FullAssemble) matches the MFEM-assembled reference (mat_ref) to 1e-12. Empirical evidence that the constructive A = Gᵀ B_𝒟ᵀ D B_𝒟 G impl realizes the opaque kernel-api faithfully. citecheck --anchor TestCeedOperatorFullAssemble [ok] :284; --anchor MaxNorm [ok] :298. Upgrades the c124 empirical-anchor-confirmed-deferred row.
  - citation: reference/palace/test/unit/test-libceed.cpp:328-377
    verdict: empirical-match
    audited_at: 2026-06-07T134107Z
    note: TestCeedOperator harness — mat_ref built MFEM-side (a_ref.Assemble/SpMat :332-334); op_test built libCEED matrix-free (a_test.PartialAssemble :338, the un-materialized ceed::Operator the impl's partial-assembly variant describes), mat_test materialized via a_test.FullAssemble :342. TWO matches asserted — apply-level TestCeedOperatorMult(op_test, op_ref) :339 (Mult/MultTranspose y_test*y_test < 1e-12 :280, directly exercises the A x contraction the impl realizes) AND assembled-matrix-level TestCeedOperatorFullAssemble :343. Covers BOTH representation variants (partial matrix-free + full materialized). citecheck --anchor TestCeedOperatorMult [ok] :339.
```
