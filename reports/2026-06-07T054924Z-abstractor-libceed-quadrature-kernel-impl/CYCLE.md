---
agent: abstractor
invoked_at: 2026-06-07T060000Z
scope: L1 kernel-impl chapter — libceed-quadrature-kernel-impl (DIRECTIVE-3 item-2a; constructive realization of the libCEED element-quadrature kernel as tensor contractions, kernel-API/impl-linked to the kept fe-assemble-libceed-boundary-obstruction)
status: pending
inputs:
  - book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md (the KEPT kernel-api obstruction theme — role-labeled this cycle)
  - book/src/L1/fe_assemble.md (the firm fold whose opaque leaf A(space, term) this impl realizes)
  - palace/fem/libceed/integrator.cpp:215-512 (AssembleCeedOperator + apply/build QFunction structure — the libCEED operator decomposition source of truth)
  - palace/fem/libceed/integrator.cpp:340-419 (f_build_geom_factor_* geom-factor + quad-weight build QFunction)
  - palace/fem/libceed/integrator.hpp:14-23 (EvalMode enum — Weight/Interp/Grad/Div/Curl basis-eval modes)
  - palace/fem/integrator.hpp:58-61 (BilinearFormIntegrator::Assemble pure-virtual leaf-kernel contract)
  - reference: project_kernel_api_impl_distinction, project_lift_through_deferred_in_scope, project_blackbox_vs_accelerated_kernels
integrated_at: 2026-06-07T054924Z
integration_commit: ae2e2f4
integration_notes: "Applied clean. L1/libceed-quadrature-kernel-impl roadmap_goal (DIRECTIVE-3 dual-surface); grounded-future [GARBAGE*] awaiting c122 substrate harvest."
---

# CYCLE: L1 kernel-impl — libceed-quadrature-kernel-impl

## Summary

The firm `fe_assemble` fold (`K = Σ_i A(space, term_i)`) quantifies **opaquely** over the
per-term assembly leaf `A(space, term)`, whose interior — the libCEED element-local quadrature
kernel — is documented as an `obstruction (opaque-library-ownership)` boundary by the existing
`fe-assemble-libceed-boundary-obstruction` theme. DIRECTIVE-3 instructs that this spine-dependency
opaque-library kernel — which has a **well-understood implementation in terms of our existing
tensor-algebra semantics** — now gets a constructive **kernel-impl** node alongside the kept
kernel-api obstruction, linked by a `realizes-kernel-api` `reference`-class edge.

The constructive content is the standard libCEED operator decomposition, which the Palace source
exposes directly: the element operator is `A = Gᵀ Bᵀ D B G`, a five-stage pipeline of
**(1) element-restriction gather** `G` (global-dof → per-element-dof), **(2) basis evaluation** `B`
(per-element-dof → per-quadrature-point values/derivatives via interp/grad/curl/div), **(3) a
pointwise quadrature-point contraction** `D` (the per-point apply-QFunction: geometry-factor ×
coefficient × quadrature-weight, all pre-baked into `geom_data` by the build-QFunction), then
**(4) basis-apply-transpose** `Bᵀ` (contract the weighted quad-point values back to element dofs)
and **(5) restriction-scatter-transpose** `Gᵀ` (assemble element contributions into the global
vector). This is a genuine **vocabulary shift**: the flat-vector BLAS algebra of our firm L1 ops
does NOT carry the rank-structured per-element / per-quad-point tensors this kernel contracts over,
so the impl introduces a **new tensor-contraction substrate** (rough-in operators: `element_restrict`,
`basis_apply`, `quad_point_contract`, `geom_factor_build`).

Because that substrate is **not yet composable from already-firm primitives** (our firm L1
vocabulary is flat-vector; the per-element rank structure is genuinely new), I land this as a
**`roadmap_goal` (rank-0)** chapter per my role-spec clean-gate: it carries the full constructive
sketch + the `realizes-kernel-api` link + the four speculative tensor-contraction operators as
rough-in placeholders for harvester promotion, with NO firm claim that the substrate exists. The
existing obstruction theme is **kept and NOT downgraded**; it gains the `kernel-api` role-label
inline in its `## Status` line (a separate D-row note for the integrator). This is the matrix-free
GPU-tensor target form (`project_l4_is_backend_lowering_target`): the contraction pipeline is exactly
what burn's batched tensor ops express natively.

## Proposed changes

```new:book/src/L1/libceed-quadrature-kernel-impl.md
---
layer: L1
operator: libceed-quadrature-kernel-impl
# Graded-stack scheme. This is a roadmap_goal (rank 0) kernel-IMPL node (DIRECTIVE-3 item-2a):
# the constructive, in-our-tensor-algebra realization of the libCEED element-quadrature kernel
# that the firm `fe_assemble` fold (`K = Σ_i A(space, term_i)`) folds over opaquely as the leaf
# `A(space, term)`. It is rank-0 (roadmap_goal) because its constructive constituents — the
# per-element / per-quad-point tensor-contraction substrate — are NOT yet firm L1 vocabulary
# (our firm L1 ops are flat-vector BLAS; the rank-structured element-local tensors are a genuine
# vocabulary shift). A roadmap_goal may rest on anything, incl. other roadmap_goals (the rank
# invariant `rank(u) <= rank(v)` is vacuously satisfied since rank(u)=0). The `realizes-kernel-api`
# edge to the KEPT obstruction theme is `reference`-class (navigational/free — NOT depends-on; it
# does not block, does not constrain rank, does not carry liveness — it is a correspondence to be
# REVIEWED, audited by lowering-verifier). Pulled-by: `fe_assemble` (firm, the spine consumer whose
# opaque leaf this realizes) reaches the feature root via 7 feature-column inbound edges — so this
# roadmap_goal is reachable (not speculation-noise).
rank: roadmap_goal
edges:
  reference:
    - target: L1-L0/fe-assemble-libceed-boundary-obstruction
      kind: realizes-kernel-api    # the kernel-api obstruction surface this impl realizes (free, navigational; the reviewed correspondence — NOT depends-on)
    - target: L1/fe_assemble
      kind: realizes-leaf          # the firm fold whose opaque per-term leaf A(space, term) THIS is the constructive interior of (free; fe_assemble does NOT depend on the impl — it folds over A opaquely)
    - target: L1/weak_form_term    # the (coefficient, differential-operator) pair whose differential-operator selects the basis-eval mode B and whose coefficient enters the pointwise contraction D
    - target: concepts/tensor-field-lift   # the contraction pipeline is the matrix-free GPU-tensor target form (backend-lowering)
  depends-on:
    # NOTE (clean-gate): these are the speculative tensor-contraction substrate operators this
    # impl WOULD rest on. They do NOT exist as firm L1 vocabulary yet (rough-in roadmap-deps).
    # Because THIS node is rank-0 (roadmap_goal), these may themselves be rank-0 and the rank
    # invariant holds. Listed as the declared-future deps the graded stack tracks; harvester
    # promotes them when the substrate is mined (combinator-miner D6 of this cycle probes exactly
    # this shared contraction substrate).
    - target: L1/element_restrict        # G — global-dof → per-element-dof gather (rough-in; no anchor yet)
      kind: composes
    - target: L1/basis_apply             # B — per-element-dof → per-quad-point eval (interp/grad/curl/div) (rough-in; no anchor yet)
      kind: composes
    - target: L1/quad_point_contract     # D — pointwise geom×coeff×weight contraction at quad points (rough-in; no anchor yet)
      kind: composes
    - target: L1/geom_factor_build       # the build-QFunction: Jacobian × quad-weight → geom_data (rough-in; no anchor yet)
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

`roadmap_goal` (rank 0) — **kernel-impl** (the DIRECTIVE-3 role-label; this node is the
constructive realization, NOT the API surface). The clean-gate call is **ROADMAP_GOAL, not firm**:
the operator decomposition is well-understood and exhaustively anchored in the Palace libCEED source
(see *Evidence*), but its constructive constituents — the per-element / per-quadrature-point
tensor-contraction substrate (`element_restrict`, `basis_apply`, `quad_point_contract`,
`geom_factor_build`) — are **not yet firm L1 vocabulary**. Our firm L1 algebra is **flat-vector
BLAS-1/2** (`apply_linop`, `axpy`, `dot` over `Tensor[N]`); the libCEED kernel contracts over
**rank-structured element-local tensors** (`[E, P, ...]` over elements `E` and quadrature points
`P`) that no firm L1 operator carries. Realizing the kernel is therefore a genuine **vocabulary
shift**, not a re-expression in existing terms — so the honest disposition is a rank-0 roadmap_goal
that carries the constructive sketch + declares the substrate it would rest on, with NO claim that
the substrate exists. Promotion route: harvester mines the four substrate operators (the
combinator-miner shared-substrate probe of this same cycle targets exactly this contraction core);
once they are firm, this node promotes `roadmap_goal → rough-in → firm` on the usual gates and its
`depends-on` edges become firm-resting.

**The `realizes-kernel-api` link is `reference`-class (free, navigational).** This impl does **not**
`depends-on` the opaque API; the relationship is a *correspondence to be reviewed*, not a build
dependency, so it must not constrain rank or carry liveness (CLAUDE.md DIRECTIVE-3). The linters
ignore the `realizes-kernel-api` label via the optional-`kind:`-is-documentation mechanism — no new
linter edge-semantics. Likewise the `realizes-leaf` edge to `fe_assemble` is `reference`-class:
`fe_assemble` stays firm and folds over `A` **opaquely**; it does not depend on this impl (the fold's
firmness is independent of how the leaf is computed — see the obstruction theme's §"`fe_assemble`
stays FIRM").

## L1 form (the constructive realization)

The kernel realizes the per-term leaf `A(space, term)` — one weak-form term's element-local→global
linear-operator contribution — as the standard **libCEED operator decomposition**, a five-stage
contraction pipeline. Writing `term = (Q, 𝒟)` (a [`weak_form_term`](./weak_form_term.md): coefficient
`Q`, differential-operator `𝒟 ∈ {Identity, Gradient, Curl, Divergence}`):

    A(space, (Q, 𝒟)) = Gᵀ ∘ B_𝒟ᵀ ∘ D(Q, geom) ∘ B_𝒟 ∘ G
        -- A(space, term) :: LinearOperator[(N: ...)]   (N = space true-dof axis)
        -- as a tensor-contraction pipeline over an element axis E and a quad-point axis P

Stage-by-stage (each stage is a speculative rough-in substrate operator):

- **G — element restriction (gather).** `element_restrict :: Tensor[(N: ...)] -> Tensor[(E, L)]`
  scatters the global true-dof vector into per-element local-dof tensors (`E` = element count,
  `L` = local dofs per element). The libCEED `CeedElemRestriction` (`trial_restr`/`test_restr`,
  built by Palace at `bilinearform.cpp:64-66`; the index map `restriction.cpp`). Pure
  gather/scatter — no arithmetic; `Gᵀ` is the transpose scatter-add (assembly).

- **B — basis evaluation.** `basis_apply :: BasisMode -> Tensor[(E, L)] -> Tensor[(E, P, C)]`
  contracts the per-element dofs against the tabulated basis (and its derivatives) to produce values
  at quadrature points: `interp` (values), `grad`/`curl`/`div` (derivatives), selected by the
  `EvalMode` the term's `𝒟` determines (`palace/fem/libceed/integrator.hpp:14-23` —
  `Weight/Interp/Grad/Div/Curl`). The libCEED `CeedBasis` (`trial_basis`/`test_basis`,
  `bilinearform.cpp:68-69`). On a tensor-product element this `B` itself factors into a sum-factorized
  sequence of 1-D contractions (the matrix-free efficiency win) — a sub-axis the impl notes but does
  not need at L1.

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
  `concepts/tensor-field-lift` describes, and the natural GPU-tensor form.

- **geom_factor_build — the build-QFunction.** `geom_factor_build :: MeshNodes -> QuadWeights ->
  GeomData` precomputes `geom_data` per quadrature point from the mesh-node Jacobian (`grad_x`,
  `CEED_EVAL_GRAD`) and the quadrature weight (`q_w`, `CEED_EVAL_WEIGHT`):
  `f_build_geom_factor_*` (`palace/fem/libceed/integrator.cpp:340-419`; inputs `attr`/`q_w`/`grad_x` at `:386-390`,
  output `geom_data` at `:397`). This is the **setup-stratum** factor (built once per mesh/order,
  reused across applies) — a build-time-vs-run-time stratification
  (`concepts/build-time-vs-run-time-stratification`).

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
explicit field roles in the Palace libCEED operator-construction code. What is **speculative** is
only the *existence of firm L1 substrate operators* for the contraction stages — hence rank-0
roadmap_goal, not firm.

## Speculative L1 operators (rough-in; harvester promotion targets)

- `element_restrict` — `G`/`Gᵀ`: the per-element gather/scatter `Tensor[(N: ...)] ↔ Tensor[(E, L)]`.
- `basis_apply` — `B`/`Bᵀ`: the basis-eval contraction `Tensor[(E, L)] ↔ Tensor[(E, P, C)]`, keyed on
  the `EvalMode` the term's `𝒟` selects.
- `quad_point_contract` — `D`: the pointwise per-quad-point `geom_data ⊙ ·` contraction (the
  embarrassingly-parallel lift).
- `geom_factor_build` — the setup-stratum build-QFunction `(mesh-nodes, quad-weights) → geom_data`.

These four are the **shared tensor-contraction substrate** the combinator-miner shared-substrate
probe (D6 of this cycle) is designed to mine ONCE across the relaxation (D3) / contraction (D4=this)
/ Krylov (D5) kernel-impls; harvester promotes them when the substrate is firm.

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
```

### Obstruction-theme role-label edit (kept as kernel-api; NOT downgraded)

The existing obstruction theme stays `status: obstruction (opaque-library-ownership)` and is KEPT
in full. The ONLY change is the **opening sentence of its `## Status` section**, which gains the
`kernel-api` role-label. This is a precise one-sentence find/replace; everything from "The entire
callable that produces the element-local quadrature contribution lives **outside Palace**…" onward
is UNCHANGED.

```edit:book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md
REPLACE the opening sentence of the `## Status` section. The current text is:

    `obstruction (opaque-library-ownership)` — the mandatory sub-kind tag (per CLAUDE.md
    §Methodology-invariants "Obstruction themes have two sub-kinds"). The entire callable that

Replace it with (leaving "The entire callable that …" and the rest of the section intact):

    `obstruction (opaque-library-ownership)` — **kernel-api** (the DIRECTIVE-3 role-label: this
    node IS the opaque kernel-API CONTRACT the spine calls; the from-our-tensor-algebra realization
    is the separate **kernel-impl** node
    [`libceed-quadrature-kernel-impl`](../L1/libceed-quadrature-kernel-impl.md), linked back here by
    a `realizes-kernel-api` `reference`-class edge — free, navigational, NOT a `depends-on`; a
    reviewer reads both and checks they match, `lowering-verifier` audits the correspondence). The
    role-label does NOT change the obstruction disposition; this remains the mandatory sub-kind tag
    (per CLAUDE.md §Methodology-invariants "Obstruction themes have two sub-kinds"). The entire
    callable that
```

(Optionally the integrator may also append a `## Related` cross-link in the obstruction theme back
to the new kernel-impl node, symmetric to the impl's back-link; the `## Status` role-label edit
above is the load-bearing change.)

### SUMMARY.md registration

```edit:book/src/SUMMARY.md
Under the `- [FE-assembly sub-spine](./L1/fe-assembly-intro.md)` Part, insert the new chapter in
alphabetical position (after `fe_assemble`, before `weak_form_term`):

- [FE-assembly sub-spine](./L1/fe-assembly-intro.md)
  - [eliminate_essential_bc](./L1/eliminate_essential_bc.md)
  - [eliminate_rhs](./L1/eliminate_rhs.md)
  - [fe_assemble](./L1/fe_assemble.md)
  - [libceed-quadrature-kernel-impl](./L1/libceed-quadrature-kernel-impl.md)
  - [weak_form_term](./L1/weak_form_term.md)
```

### L1 index dep-map row (my own table row — index dual-registration partition)

```edit:book/src/L1/index.md
Insert in alphabetical position within the **FE-assembly sub-spine** dep-map grouping (after the
`fe_assemble` row, before the `weak_form_term` row):

| [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md) | `(space, term=(Q, 𝒟)) → LinearOperator[(N: ...)]` (i.e. the per-term assembly leaf `A(space, term) = Gᵀ B_𝒟ᵀ D(Q, geom) B_𝒟 G` — the libCEED element-quadrature kernel as a tensor-contraction pipeline) | composes the speculative tensor-contraction substrate `element_restrict` (G) / `basis_apply` (B) / `quad_point_contract` (D) / `geom_factor_build` (rough-in roadmap-deps; NOT firm yet); `realizes-kernel-api` (reference) → [`fe-assemble-libceed-boundary-obstruction`](../L1-L0/fe-assemble-libceed-boundary-obstruction.md); `realizes-leaf` (reference) the opaque `A(space, ·)` leaf of firm [`fe_assemble`](./fe_assemble.md) | `roadmap_goal` (**kernel-impl**; DIRECTIVE-3 item-2a constructive realization of the libCEED element-quadrature kernel; rank-0 because the per-element/per-quad-point tensor-contraction substrate is a genuine vocabulary shift NOT yet firm L1 vocabulary — flat-vector BLAS does not carry the `[E, P, ...]` rank structure; the obstruction theme is KEPT as the kernel-api surface, NOT downgraded; `realizes-kernel-api` is a free reference edge, NOT depends-on; promotes roadmap_goal→rough-in→firm once the substrate is mined — combinator-miner D6 probes exactly this shared contraction core; proposed-by: abstractor:2026-06-07T054924Z-abstractor-libceed-quadrature-kernel-impl) |
```

### L1 index FE-assembly §Vocabulary-cohort bullet (my own cohort bullet — partition)

```edit:book/src/L1/index.md
Append to the **FE-assembly sub-spine** §Vocabulary-cohort bullet list (after the four firm member
bullets — the `eliminate_rhs` bullet). This is MY own-cohort bullet (registered by me per the index
dual-registration partition); the consolidated firm-count TALLY is NOT touched — this node is
`roadmap_goal`, not firm, so the FE-assembly sub-spine firm count stays 4:

- **`libceed-quadrature-kernel-impl` is a `roadmap_goal` (kernel-impl)** *(cycle-121 D4)* — see [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md). The constructive, in-our-tensor-algebra realization of the per-term assembly leaf `A(space, term)` that [`fe_assemble`](./fe_assemble.md) folds over opaquely: the libCEED element-quadrature kernel as the contraction pipeline `A = Gᵀ B_𝒟ᵀ D(Q, geom) B_𝒟 G` (restriction-gather ▷ basis-eval ▷ pointwise geom×coeff×weight contraction ▷ basis-apply-transpose ▷ restriction-scatter). The DIRECTIVE-3 **kernel-impl** counterpart of the KEPT [`fe-assemble-libceed-boundary-obstruction`](../L1-L0/fe-assemble-libceed-boundary-obstruction.md) **kernel-api** surface, linked by a free `realizes-kernel-api` reference edge (NOT a `depends-on` — a reviewed correspondence, audited by `lowering-verifier`). **Rank-0 (roadmap_goal), NOT firm**, by the clean-gate: the per-element/per-quad-point tensor-contraction substrate (`element_restrict`/`basis_apply`/`quad_point_contract`/`geom_factor_build`) is a genuine vocabulary shift — our firm L1 algebra is flat-vector BLAS and does not carry the `[E, P, ...]` rank structure — so the honest disposition is a roadmap_goal carrying the constructive sketch + declaring the substrate it would rest on, NOT a firm claim. The obstruction theme STAYS the kernel-api surface (NOT downgraded). Promotes roadmap_goal→rough-in→firm once the substrate is mined (combinator-miner D6 of this cycle probes exactly this shared contraction core, shared with the D3 relaxation / D5 Krylov kernel-impls). Does NOT change the FE-assembly sub-spine firm count (still 4 firm).
```

## Speculative operators proposed

Four rough-in tensor-contraction substrate operators (harvester promotion targets; the
combinator-miner D6 shared-substrate probe of this cycle targets exactly this contraction core,
shared with the D3 relaxation / D5 Krylov kernel-impls):

- **`element_restrict`** — `BasisMode-free; sig (best guess) :: Tensor[(N: ...)] -> ElemRestriction -> Tensor[(E, L)]` (and its transpose `Gᵀ :: Tensor[(E, L)] -> Tensor[(N: ...)]`, scatter-add). The pure gather/scatter between the global true-dof vector and per-element local-dof tensors — no arithmetic. L0 referent: `CeedElemRestriction` (`palace/fem/libceed/restriction.cpp`; built `bilinearform.cpp:64-66`). The `Gᵀ` scatter-add IS the conforming-FE assembly step.
- **`basis_apply`** — `sig (best guess) :: EvalMode -> Tensor[(E, L)] -> Basis -> Tensor[(E, P, C)]` (and transpose). Contracts per-element dofs against the tabulated basis (and derivatives) to quad-point values, keyed on the `EvalMode` (`Interp`/`Grad`/`Curl`/`Div`) the term's `𝒟` selects. On a tensor-product element it sub-factors into sum-factorized 1-D contractions. L0: `CeedBasis` (`palace/fem/bilinearform.cpp:68-69`; modes `palace/fem/libceed/integrator.hpp:14-23`).
- **`quad_point_contract`** — `sig (best guess) :: Tensor[(E, P, C)] -> GeomData -> Tensor[(E, P, C)]`. The pointwise per-quadrature-point apply: `geom_data ⊙ (basis-evaluated trial)`, where `geom_data` has pre-baked geometry-factor × coefficient × quad-weight. The embarrassingly-parallel diagonal (the `concepts/tensor-field-lift` per-point lift; the natural GPU-tensor form). L0: `f_apply_*` (`palace/fem/libceed/integrator.cpp:215-308`, `:451-512`).
- **`geom_factor_build`** — `sig (best guess) :: MeshNodes -> QuadWeights -> Coefficient -> GeomData`. The setup-stratum build-QFunction: precompute `geom_data` per quad point from the mesh-node Jacobian (`grad_x`) × quad weight (`q_w`) (× coefficient, when pre-baked). A build-time-vs-run-time stratification factor (`concepts/build-time-vs-run-time-stratification`). L0: `f_build_geom_factor_*` (`palace/fem/libceed/integrator.cpp:340-419`).

## Supporting evidence

All citations self-verified via `citecheck --anchor` and direct codemap `read_range` this cycle:

- `palace/fem/libceed/integrator.cpp:423-445` — `AssembleCeedOperator` master assembler signature (the `Gᵀ Bᵀ D B G` wiring inputs: `trial_restr`/`test_restr`/`trial_basis`/`test_basis`/`geom_data`/`geom_data_restr`). citecheck `--anchor 'AssembleCeedOperator'` zero-drift (line 423).
- `palace/fem/libceed/integrator.cpp:451-512` — apply-QFunction + operator-field wiring; `q_w` quad-weight input at 462 (citecheck zero-drift); `AddOperatorActiveInputFields`/`AddOperatorActiveOutputFields` at 492/493 (direct read confirmed — the `B G` input + `Bᵀ Gᵀ` output field chains).
- `palace/fem/libceed/integrator.cpp:340-419` — build-QFunction `f_build_geom_factor_*`: `q_w` (`CEED_EVAL_WEIGHT`) at 388 (citecheck zero-drift), `grad_x` (`CEED_EVAL_GRAD`) at 390, `geom_data` output at 397.
- `palace/fem/libceed/integrator.cpp:215-308` — `QuadratureDataAssembly` + `f_apply_*` pointwise kernels (direct read confirmed).
- `palace/fem/libceed/integrator.hpp:15-23` — `enum EvalMode { Weight, None, Interp, Grad, Div, Curl }` (citecheck `--anchor 'EvalMode'` zero-drift line 15; `--anchor 'Weight'` line 17).
- `palace/fem/integrator.hpp:58-61` — `BilinearFormIntegrator::Assemble` pure-virtual leaf-kernel contract (citecheck `--anchor 'Assemble'` line 58).
- `palace/fem/bilinearform.cpp:64-70` — Palace-supplied `G`/`B` operands (restriction + basis inputs).
- `book/src/L1/fe_assemble.md` — the firm fold whose opaque leaf this realizes (stays firm; folds over `A` opaquely).
- `book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md` — the KEPT kernel-api obstruction surface.

## Open questions / caveats

- **`realizes-leaf` is a NEW reference-edge label.** I introduced `realizes-leaf` (impl → `fe_assemble`) alongside the directive-mandated `realizes-kernel-api` to express "this is the constructive interior of the fold's opaque leaf." It is `reference`-class (free; the linters ignore the optional `kind:`), so it adds no machinery — but it is a label not in prior use. If the meta-phase / lowering-verifier prefers to fold this into a plain `reference` (no `kind:`) or reuse `realizes-kernel-api` semantics, that is a free relabel. Flagged for the c122 lowering-verifier audit dispatch.
- **roadmap_goal vs rough-in disposition.** I chose `roadmap_goal` (rank-0) over `rough-in` (rank-2) because the constructive constituents are NOT confirmed-real-but-undissected (the `stub`/`rough-in` bar) — they are *intended/speculative* substrate that does not yet exist in any form in our L1 vocabulary. Per the `stub` vs `roadmap_goal` line (METHODOLOGY-GRADED-STACK §1e), an intended/speculative referent that may rest on anything is `roadmap_goal`. If the combinator-miner D6 probe THIS cycle surfaces a firm-composable substrate, the c122 planner should re-evaluate whether this node can promote straight to `rough-in`.
- **Pulled-by reachability.** The node is pulled-by `fe_assemble` (firm; reachable via 7 feature-column inbound edges), so it is NOT speculation-noise (the reachability guard is satisfied). But the `realizes-kernel-api`/`realizes-leaf` edges are `reference`-class (free, do NOT carry liveness), and the `depends-on` edges point at not-yet-existing substrate. Confirm with the c122 linter run that the node reads reachable (it should, via the inbound side once a consumer references it; if it reads detritus, the grounding is the `realizes-leaf` correspondence + the substrate-mining pull — ground, don't remove, per `feedback_gc_ground_dont_remove_future_deps`).
- **Faithfulness audit (lowering-verifier, c122).** The impl-realizes-API correspondence — that `A = Gᵀ Bᵀ D B G` faithfully matches what the opaque libCEED kernel computes — is the reviewable claim DIRECTIVE-3 wants checked. The strongest empirical anchor is `test/unit/test-libceed.cpp` `TestCeedOperatorFullAssemble` (assembled matrix matches MFEM reference to 1e-12), cited in `fe_assemble.md` as future `empirical-match` evidence for `A`'s faithfulness — a natural anchor for the c122 lowering-verifier impl-realizes-API audit.
- **Sum-factorization sub-axis.** The `B` basis-apply factors into sum-factorized 1-D contractions on tensor-product elements (the matrix-free efficiency win). I noted this as a sub-axis but did not lift it — it is a transparent performance trick (algebraically equal to the dense `B` contraction), so per CLAUDE.md §Optimization-tricks it is a one-line note, not separate vocabulary. Confirm this classification holds (it is transparent, not load-bearing) when `basis_apply` is harvested.
