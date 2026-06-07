---
layer: L1
operator: geom_factor_build
# Graded-stack: firm (rank 3). The geometry-factor build-pass (build-QFunction) of the libCEED
# pipeline: (mesh-nodes, quad-weights) → geom_data. Promoted roadmap_goal → rough-in (cycle-124 D4) →
# firm (cycle-125 D1) on the element-local rank-tensor vocabulary: the shape-vocabulary home
# concepts/element-local-tensor (firm c124 D5, commit db5ea4d) defines the per-quad-point carrier
# Tensor[(E, P, G)] this op produces, so the op RESTS on a firm shape home. depends-on
# concepts/element-local-tensor (the [E, P, G] geom-data carrier shape home) — rank invariant
# rank(u) <= min(deps): the dep is now firm, so the firm-flip is warranted (firm-on-positive-structure
# escape — laws are syntactic setup-stratum-purity / pointwise identities on positive source).
# Setup-stratum (built once per mesh/order, reused across applies). Reachable via
# libceed-quadrature-kernel-impl (pulled-by) and quad_point_contract (which consumes geom_data).
rank: firm
edges:
  depends-on:
    - target: concepts/element-local-tensor
      kind: shape-vocabulary   # the [E, P, G] per-quad-point geom-data carrier shape home this op produces (firm c124 D5; rank-constrained, GC-live)
  reference:
    - target: L1/libceed-quadrature-kernel-impl
      kind: pulled-by      # the consumer whose pipeline's D stage consumes this op's geom_data output (free)
    - target: concepts/build-time-vs-run-time-stratification   # this is the setup-stratum (build-once) factor of the build/apply split
---

# geom_factor_build

The **geometry-factor build-pass** (libCEED build-QFunction) of the contraction pipeline
`A = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G` (see [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md)):
precompute, per quadrature point, the `geom_data` that the `D` stage ([`quad_point_contract`](./quad_point_contract.md))
contracts against — the Jacobian-derived geometry metric times the quadrature weight. This is the
**setup-stratum** factor: built once per `(mesh, order)`, reused across every operator apply.

## Status

`firm` (rank 3). **Promoted roadmap_goal → rough-in (cycle-124 D4) → firm (cycle-125 D1).** The Palace
realization is exhaustively anchored (the `f_build_geom_factor_*` build-QFunction with its `attr`/`q_w`/`grad_x` inputs
and `geom_data` output — see *Verified-against*), and the operator produces the **quad-point-rank**
carrier `Tensor[(E, P, G)]` whose **shape-vocabulary home is `concepts/element-local-tensor`** — now
**firm on disk** (c124 D5, commit `db5ea4d`). With that home firm (as a `depends-on` shape-vocabulary
edge), the op rests on a firm shape and the well-foundedness cap lifts: `rank(u) ≤ min(deps)` no longer
bounds this op below firm. The promotion is on the **firm-on-positive-structure escape** — every law
below is a syntactic setup-stratum-purity / pointwise-block-diagonality identity on fully-specified
positive source (the build-QFunction is read directly off `AssembleCeedGeometryData`), so the absence
of a dedicated build-QFunction unit test does not gate firm; the only gate was the firmness of the
`[E, P, G]` shape home, now discharged.

## L1 form (the constructive sketch)

Semantic/notation conventions (named shape groups, the build/run-time stratification) live on
`book/src/semantics/index.md` §1.2.1 + `concepts/build-time-vs-run-time-stratification` — linked, not
restated. The `[E, P, G]` quad-point-rank carrier shape is defined at `concepts/element-local-tensor`
— linked, not restated.

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

## Algebraic laws (firm — syntactic identities on positive source)

- **Setup-stratum purity:** `geom_factor_build` is a pure function of `(mesh_nodes, quad_weights)` — no
  field/state dependence; its output is cacheable and reused across applies (the build/run-time split law).
- **Pointwise/element-local:** `geom_data[e, p]` depends only on the local mesh-node Jacobian and weight
  at `(e, p)` — block-diagonal in `(E, P)`, no inter-point/inter-element coupling.
- **`𝒟`-determined metric shape:** the geometry-metric form (`|J|` vs `J⁻ᵀ J⁻¹ |J|`) is fixed by the
  term's differential operator — a configuration of the build, not a run-time branch.
- **Affine-element constancy (special case):** on a straight-sided (affine) element `J` is constant over
  the element, so `geom_data` is constant in `p` — a degenerate case worth noting (the curved/high-order
  case is the general one).

These laws are syntactic facts on the positively-read build-QFunction. They require no test
(firm-on-positive-structure); the only gate was the firmness of the `[E, P, G]` shape home
(`concepts/element-local-tensor`), now firm on disk (c124 D5).

## Applicability conditions

1. A high-order mesh with a tabulated mesh `CeedBasis` for the geometry map (the `mesh_basis` / `mesh_restr`
   inputs); the `grad_x` Jacobian and `q_w` weight are evaluated by libCEED.
2. The geom-data storage size `2 + space_dim*dim` must match the geom-data restriction (the
   `MFEM_VERIFY(geom_data_size == 2 + space_dim*dim)` contract).
3. Single-machine (per-`Ceed` device).

## Verified-against

- `palace/fem/libceed/integrator.cpp:335-421` — `AssembleCeedGeometryData`: the build-QFunction
  `f_build_geom_factor_*` assembly: the `(dim, space_dim)`-keyed QFunction dispatch
  (`f_build_geom_factor_22`/`33`/`21`/`31`/`32`, the `switch (10 * space_dim + dim)` block `:348-384`),
  the inputs `attr` (`CEED_EVAL_INTERP`, `:387`), `q_w` (`CEED_EVAL_WEIGHT`, `:388`), `grad_x`
  (Jacobian, `CEED_EVAL_GRAD`, `:389-390`), and the `geom_data` output (`CEED_EVAL_NONE`, `:397-398`,
  size `2 + space_dim*dim` verified at `:395`).
- `palace/fem/libceed/integrator.cpp:423-427` — `AssembleCeedOperator`: the `geom_data` /
  `geom_data_restr` parameters the master assembler receives, threaded into the apply-QFunction at the
  `geom_data` field-set `:483-484` (the build output's consumer site).
- `palace/fem/libceed/integrator.hpp:14-23` — `EvalMode` (`Weight`/`Grad`/`Interp`): the build inputs'
  evaluation modes.
- `book/src/L1/libceed-quadrature-kernel-impl.md` — the firm kernel-impl consumer (pulled-by).

## Related

- [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md) — the firm kernel-impl that
  consumes this op's `geom_data` output in its `D` stage.
- [`quad_point_contract`](./quad_point_contract.md) — the `D` stage that contracts against this op's
  `geom_data` (the run-time apply half of the build/apply split).
- `concepts/element-local-tensor` — the `[E, P, G]` quad-point-rank carrier shape-vocabulary home this
  op's output rests on (the `depends-on` shape edge).
- `concepts/build-time-vs-run-time-stratification` — the setup/run-time stratification this op anchors.
