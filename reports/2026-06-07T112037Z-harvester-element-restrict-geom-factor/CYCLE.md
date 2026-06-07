---
agent: harvester
invoked_at: 2026-06-07T120000Z
scope: L1 operators element_restrict + geom_factor_build (cycle-124 D4; item-2 element-local-rank-tensor front, indexing/geometry half)
status: pending
integrated_at: 2026-06-07T112037Z
integration_commit: 331a5ed
integration_notes: "cycle-124 (batch-40 opener) D4. Applied clean. Promoted L1/element_restrict + L1/geom_factor_build roadmap_goal->ROUGH-IN (the honest one-rank climb; well-foundedness caps them at rough-in while the shape home concepts/element-local-tensor firms this same wave via a depends-on (shape-vocabulary) edge) + the stale-path fix + re-anchored build-QFunction citations. 1 OQ promoted (batch-37-era-stale-design-l4-calculus-path-drift-sweep). The 45->47 firm flip is the c125 follow-up."
inputs:
  - cycle-124 plan reports/2026-06-07T112037Z-cycle-planner-c124/CYCLE.md (D4 entry + Overlap + consolidated-tally partition: D5 owns the L1/index.md tally)
  - book/src/L1/element_restrict.md (existing roadmap_goal, c122-D4)
  - book/src/L1/geom_factor_build.md (existing roadmap_goal, c122-D4)
  - book/src/semantics/index.md §1.2.1 (named shape groups — the live semantic surface; substrate files cite the STALE design/l4_calculus.md path)
  - sibling cohort context: D3 (basis_apply + quad_point_contract), D5 (concepts/element-local-tensor record page + libceed-quadrature-kernel-impl promotion + L1/index consolidated tally)
  - L0 evidence (all on-disk citecheck-verified): palace/fem/libceed/restriction.cpp, palace/fem/bilinearform.cpp, palace/fem/libceed/integrator.{cpp,hpp}
---

# CYCLE: Formalize element_restrict + geom_factor_build at L1

## Summary

Two of the four libCEED contraction-substrate ops, promoted **roadmap_goal → rough-in** on the
element-local rank-tensor vocabulary the D3/D5 cohort establishes this wave. `element_restrict` is the
**G / Gᵀ** stage — the pure gather/scatter-add indexing backbone, `Tensor[(N: ...)] ↔ Tensor[(E, L)]`
(flat global true-dof axis `N` stays a genuine rank-1 `Tensor[(N: ...)]` per the L1/L0 flat-vector
convention; the element-local side `[E, L]` is the rank-structured axis). `geom_factor_build` is the
**build-QFunction** — the setup-stratum geometry-factor pass `(mesh-nodes, quad-weights) → geom_data ::
Tensor[(E, P, G)]` (Jacobian metric × quad-weight, material coefficient pre-multiplied).

Both were rank-0 roadmap_goals because the rank-structured element-local tensor (`[E, L]` / `[E, P, G]`)
was not carried by any firm L1 operator. This wave the cohort firms that shape-vocabulary home
(`concepts/element-local-tensor`, authored by D5 after D3+D4), so the honest promotion is to **rough-in**:
each op gains a `depends-on` edge to the shape-vocabulary record page, its exhaustively-anchored
structural decomposition stands, and its syntactic-identity operator-algebra laws are stated as rough-in
(promotable to firm once `concepts/element-local-tensor` firms — the firm-on-positive-structure escape
gated only by the to-be-firm shape vocabulary, not by missing tests). Per the honest clean-gate, this is
the maturity the evidence + the shared-wave record-page support sustains; firm follows the record page.

Semantic-surface fix folded in (both files): the stale `book/src/design/l4_calculus.md` §1.2.1
citation re-pointed to the live `book/src/semantics/index.md` §1.2.1 (named shape groups; USE+LINK, not
restated). Citation drift corrected: `restriction.cpp` `InitRestriction` END `:425 → :426`;
`integrator.cpp` build-QFunction anchors re-anchored (`attr :386→:387`, `q_w :387-388→:388`,
`MFEM_VERIFY :394→:395`, `geom_data` output `:396-398→:397-398`, function span
`:340-419 → :335-421`, consumer site `:423-465 → :423-427` + `:483-484`).

Consolidated-tally partition honored: I emit ONLY my two dep-map TABLE rows + my two
§Vocabulary-cohort member bullets; I DEFER the `L1/index.md` "Roadmap_goal … — 4" consolidated count
prose + any firm/rough-in tally bump to **D5** (the named owner this wave).

## Proposed changes

```edit:book/src/L1/element_restrict.md
---
layer: L1
operator: element_restrict
# Graded-stack: rough-in (rank 2). The G / Gᵀ stage of A = Gᵀ B_𝒟ᵀ D B_𝒟 G. Promoted roadmap_goal →
# rough-in (cycle-124 D4) on the element-local rank-tensor vocabulary the cohort firms this wave: the
# shape-vocabulary home concepts/element-local-tensor (D5) defines the rank-structured element-local
# tensor Tensor[(E, L)] this op contracts over, so the operator now RESTS on a (to-be-firm) shape home
# rather than introducing an unanchored shape. depends-on concepts/element-local-tensor (the [E, L]
# shape home) — rank invariant rank(u) <= min(deps): rough-in (2) <= the record page's rank; firm
# follows once concepts/element-local-tensor firms (the firm-on-positive-structure escape, gated only
# by the shape vocabulary, not by tests — laws are syntactic gather/scatter-add identities on positive
# source). The flat global axis N stays a genuine rank-1 Tensor[(N: ...)] (L1/L0 flat-vector
# convention). Reachable: pulled-by libceed-quadrature-kernel-impl, which reaches the feature root via
# the fe_assemble fold's feature-column inbound edges.
rank: rough-in
edges:
  depends-on:
    - target: concepts/element-local-tensor
      kind: shape-vocabulary   # the [E, L] element-local rank-tensor shape home this op's signature contracts over (D5; rank-constrained, GC-live)
  reference:
    - target: L1/libceed-quadrature-kernel-impl
      kind: pulled-by      # the consumer whose A = Gᵀ B_𝒟ᵀ D B_𝒟 G pipeline composes this G/Gᵀ stage (free; this node does not depend on its consumer)
    - target: concepts/tensor-field-lift   # Gᵀ scatter-add (assembly) is the element->global lift this substrate targets
---

# element_restrict

The **G / Gᵀ** stage of the libCEED element-quadrature contraction pipeline
`A = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G` (see [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md)):
the **element restriction** — a pure gather/scatter that maps the global true-dof vector to per-element
local-dof tensors (`G`, gather) and back by transpose scatter-add (`Gᵀ`, assembly). No arithmetic; it
is the indexing/permutation backbone of matrix-free FE operator application.

## Status

`rough-in` (rank 2). **Promoted roadmap_goal → rough-in (cycle-124 D4).** The Palace realization is
exhaustively anchored (see *Verified-against* — `CeedElemRestriction` construction and its index-map
builder), and the operator's signature now contracts over the **element-local rank-tensor**
`Tensor[(E, L)]` (element axis `E`, local-dofs-per-element axis `L`) whose **shape-vocabulary home is
`concepts/element-local-tensor`** — the record page the cohort authors this wave (D5). The rank-0
disposition was warranted only while that `[E, L]` shape had no definition home in firm L1 vocabulary;
with the home in place (as a `depends-on` shape-vocabulary edge), the op rests on a defined shape rather
than introducing an unanchored one, so the honest disposition rises to rough-in. Promotion route to
firm: once `concepts/element-local-tensor` firms, this promotes `rough-in → firm` on the
**firm-on-positive-structure escape** — every algebraic law below is a syntactic gather/scatter-add
operator-algebra identity on fully-specified positive source (the index map is read directly off
`InitRestriction`), so the absence of a dedicated restriction unit test does not gate firm; the only
remaining gate is the firmness of the `[E, L]` shape home. The flat global axis `N` stays a genuine
rank-1 `Tensor[(N: ...)]` dof-vector (the firm L1 `Tensor[N]` convention for Palace `Vector` — KEPT
flat) and is NOT part of the shape-vocabulary shift.

## L1 form (the constructive sketch)

For semantic/notation conventions (named shape groups, `Tensor[(S: ...)]` binding vs `Tensor[$S]`
use), see the governing surface `book/src/semantics/index.md` §1.2.1 — not restated here. The
`[E, L]` / `[E, P, G]` element-local rank-tensor shape family is defined at
`concepts/element-local-tensor` — linked, not restated.

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
convention for Palace `Vector` — KEPT flat). The element-local side `Tensor[(E, L)]` is the
rank-structured axis (the shape-vocabulary home `concepts/element-local-tensor`). On a tensor-product
element `L` itself factors as a per-dimension dof product, but that factoring is an interior detail of
`basis_apply` (the sum-factorization sub-axis), not of the restriction.

## Algebraic laws (rough-in — syntactic identities on positive source; firm on shape-home firmness)

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

These are the standard restriction/prolongation algebra — syntactic identities on the positively-read
Boolean index map. They are stated as rough-in (not yet firm) only because the `[E, L]` shape home
(`concepts/element-local-tensor`) is itself firming this wave; the laws themselves require no test
(firm-on-positive-structure).

## Applicability conditions

1. A standard FE basis with a tabulated `CeedElemRestriction` (the de-Rham family axis of
   [`weak_form_term`](./weak_form_term.md)); the lexicographic-vs-native ordering branch
   (`InitLexicoRestr` / `InitNativeRestr`) is an interior detail of the index-map construction.
2. Single-machine (per-`Ceed` device): the multi-rank shared-dof overlap (`ParMesh` assembly) is read
   single-rank per CLAUDE.md §Scope (DIRECTIVE-1 boundary) — the cross-rank scatter-add reconciliation
   is a deferred future direction, not lifted here.

## Verified-against

- `palace/fem/libceed/restriction.cpp:389-426` — `InitRestriction`: the element-restriction builder;
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
- `concepts/element-local-tensor` — the `[E, L]` element-local rank-tensor shape-vocabulary home this
  op's element-local side rests on (the `depends-on` shape edge).
- `concepts/tensor-field-lift` — `Gᵀ` (assembly) is the element→global lift this substrate targets.
```

```edit:book/src/L1/geom_factor_build.md
---
layer: L1
operator: geom_factor_build
# Graded-stack: rough-in (rank 2). The geometry-factor build-pass (build-QFunction) of the libCEED
# pipeline: (mesh-nodes, quad-weights) → geom_data. Promoted roadmap_goal → rough-in (cycle-124 D4) on
# the element-local rank-tensor vocabulary the cohort firms this wave: the shape-vocabulary home
# concepts/element-local-tensor (D5) defines the per-quad-point carrier Tensor[(E, P, G)] this op
# produces, so the op now RESTS on a (to-be-firm) shape home. depends-on concepts/element-local-tensor
# (the [E, P, G] geom-data carrier shape home) — rank invariant rank(u) <= min(deps): rough-in (2) <=
# the record page's rank; firm follows once concepts/element-local-tensor firms (firm-on-positive-
# structure escape — laws are syntactic setup-stratum-purity / pointwise identities on positive source).
# Setup-stratum (built once per mesh/order, reused across applies). Reachable via
# libceed-quadrature-kernel-impl (pulled-by) and quad_point_contract (which consumes geom_data).
rank: rough-in
edges:
  depends-on:
    - target: concepts/element-local-tensor
      kind: shape-vocabulary   # the [E, P, G] per-quad-point geom-data carrier shape home this op produces (D5; rank-constrained, GC-live)
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

`rough-in` (rank 2). **Promoted roadmap_goal → rough-in (cycle-124 D4).** The Palace realization is
exhaustively anchored (the `f_build_geom_factor_*` build-QFunction with its `attr`/`q_w`/`grad_x` inputs
and `geom_data` output — see *Verified-against*), and the operator produces the **quad-point-rank**
carrier `Tensor[(E, P, G)]` whose **shape-vocabulary home is `concepts/element-local-tensor`** — the
record page the cohort authors this wave (D5). The rank-0 disposition was warranted only while the
`[E, P, G]` carrier had no definition home in firm L1 vocabulary; with the home in place (as a
`depends-on` shape-vocabulary edge), the op rests on a defined shape, so the honest disposition rises to
rough-in. Promotion route to firm: once `concepts/element-local-tensor` firms, this promotes
`rough-in → firm` on the **firm-on-positive-structure escape** — every law below is a syntactic
setup-stratum-purity / pointwise-block-diagonality identity on fully-specified positive source (the
build-QFunction is read directly off `AssembleCeedGeometryData`), so the absence of a dedicated
build-QFunction unit test does not gate firm; the only remaining gate is the firmness of the `[E, P, G]`
shape home.

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

## Algebraic laws (rough-in — syntactic identities on positive source; firm on shape-home firmness)

- **Setup-stratum purity:** `geom_factor_build` is a pure function of `(mesh_nodes, quad_weights)` — no
  field/state dependence; its output is cacheable and reused across applies (the build/run-time split law).
- **Pointwise/element-local:** `geom_data[e, p]` depends only on the local mesh-node Jacobian and weight
  at `(e, p)` — block-diagonal in `(E, P)`, no inter-point/inter-element coupling.
- **`𝒟`-determined metric shape:** the geometry-metric form (`|J|` vs `J⁻ᵀ J⁻¹ |J|`) is fixed by the
  term's differential operator — a configuration of the build, not a run-time branch.
- **Affine-element constancy (special case):** on a straight-sided (affine) element `J` is constant over
  the element, so `geom_data` is constant in `p` — a degenerate case worth noting (the curved/high-order
  case is the general one).

These laws are syntactic facts on the positively-read build-QFunction. They are stated as rough-in (not
yet firm) only because the `[E, P, G]` shape home (`concepts/element-local-tensor`) is itself firming
this wave; the laws themselves require no test (firm-on-positive-structure).

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
- `book/src/L1/libceed-quadrature-kernel-impl.md` — the roadmap_goal consumer (pulled-by).

## Related

- [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md) — the roadmap_goal that
  consumes this op's `geom_data` output in its `D` stage.
- [`quad_point_contract`](./quad_point_contract.md) — the `D` stage that contracts against this op's
  `geom_data` (the run-time apply half of the build/apply split).
- `concepts/element-local-tensor` — the `[E, P, G]` quad-point-rank carrier shape-vocabulary home this
  op's output rests on (the `depends-on` shape edge).
- `concepts/build-time-vs-run-time-stratification` — the setup/run-time stratification this op anchors.
```

```edit:book/src/L1/index.md
- **`element_restrict` is a `rough-in`** *(cycle-122 D4 roadmap_goal → cycle-124 D4 rough-in)* — see [`element_restrict`](./element_restrict.md). The **G / Gᵀ** stage: the per-element gather (`G`, global true-dof → per-element local-dof `Tensor[(N: ...)] → Tensor[(E, L)]`) and its transpose scatter-add (`Gᵀ`, assembly). Pure gather/scatter, no arithmetic; `Gᵀ G` is the dof-multiplicity diagonal, `G Gᵀ ≠ I`. Promoted roadmap_goal → rough-in on the element-local rank-tensor vocabulary: `depends-on` `concepts/element-local-tensor` (the `[E, L]` shape home, D5 this wave); firm on the firm-on-positive-structure escape once that shape home firms. L0: `InitRestriction` (`palace/fem/libceed/restriction.cpp:389-426`), `CeedElemRestrictionCreate` (`:200`), `trial_restr`/`test_restr` (`palace/fem/bilinearform.cpp:64-70`).
```

```edit:book/src/L1/index.md
- **`geom_factor_build` is a `rough-in`** *(cycle-122 D4 roadmap_goal → cycle-124 D4 rough-in)* — see [`geom_factor_build`](./geom_factor_build.md). The geometry-factor **build-pass**: `(mesh-nodes, quad-weights) → geom_data :: Tensor[(E, P, G)]` (Jacobian metric × quad-weight, with the material coefficient pre-multiplied in). The **setup stratum** of the build/run-time split (`concepts/build-time-vs-run-time-stratification`) — built once per `(mesh, order)`, reused across applies. Promoted roadmap_goal → rough-in on the element-local rank-tensor vocabulary: `depends-on` `concepts/element-local-tensor` (the `[E, P, G]` carrier shape home, D5 this wave); firm on the firm-on-positive-structure escape once that shape home firms. L0: `AssembleCeedGeometryData` (`palace/fem/libceed/integrator.cpp:335-421`; QFunction dispatch `:348-384`, inputs `attr`/`q_w`/`grad_x` `:387`/`:388`/`:389-390`, output `geom_data` `:397-398`).
```

```edit:book/src/L1/index.md
| [`element_restrict`](./element_restrict.md) | `ElemRestriction → Tensor[(N: ...)] → Tensor[(E, L)]` (G, gather); transpose `Tensor[(E, L)] → Tensor[(N: ...)]` (Gᵀ, scatter-add/assembly) | `depends-on` (shape-vocabulary) `concepts/element-local-tensor` (the `[E, L]` element-local rank-tensor shape home, D5); `pulled-by` (reference) [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md) — the G/Gᵀ stage of its `A = Gᵀ B_𝒟ᵀ D B_𝒟 G` pipeline; references `concepts/tensor-field-lift` (Gᵀ assembly) | `rough-in` (promoted roadmap_goal → rough-in cycle-124 D4 on the element-local rank-tensor vocabulary; the per-element gather/scatter over the `[E, L]` element-rank tensor, now resting on the `concepts/element-local-tensor` shape home rather than introducing an unanchored shape; flat global axis `N` stays rank-1 `Tensor[(N: ...)]`; firm on the firm-on-positive-structure escape once the shape home firms; proposed-by: harvester:2026-06-07T112037Z-harvester-element-restrict-geom-factor) |
```

```edit:book/src/L1/index.md
| [`geom_factor_build`](./geom_factor_build.md) | `MeshNodes → QuadWeights → Tensor[(E, P, G)]` (geometry-factor build-pass: Jacobian metric × quad-weight, coefficient pre-multiplied) | `depends-on` (shape-vocabulary) `concepts/element-local-tensor` (the `[E, P, G]` quad-point-rank carrier shape home, D5); `pulled-by` (reference) [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md) — the build-QFunction whose geom_data its D stage consumes; references `concepts/build-time-vs-run-time-stratification` | `rough-in` (promoted roadmap_goal → rough-in cycle-124 D4 on the element-local rank-tensor vocabulary; the setup-stratum geometry-factor pass over the `[E, P, G]` quad-point-rank carrier, now resting on the `concepts/element-local-tensor` shape home; built once per `(mesh, order)`, reused across applies; firm on the firm-on-positive-structure escape once the shape home firms; proposed-by: harvester:2026-06-07T112037Z-harvester-element-restrict-geom-factor) |
```

## Operator content

### element_restrict (rough-in)

- **Signature:** `element_restrict :: ElemRestriction -> Tensor[(N: ...)] -> Tensor[(E, L)]` (G, gather);
  `element_restrict_t :: ElemRestriction -> Tensor[(E, L)] -> Tensor[(N: ...)]` (Gᵀ, scatter-add). `N` =
  flat global true-dof axis (rank-1 `Tensor[(N: ...)]`, KEPT flat); `E` = element count; `L` =
  local-dofs-per-element. The `[E, L]` shape home is `concepts/element-local-tensor`.
- **Semantics:** pure gather (`G`, Boolean selection through the local→global index map) / transpose
  scatter-add (`Gᵀ`, assembly summing element-local contributions into shared global slots). No
  arithmetic beyond the scatter accumulation.
- **Algebraic laws (rough-in):** transpose/adjoint pair `⟨Gx,y⟩=⟨x,Gᵀy⟩`; gather linear Boolean
  selection; `Gᵀ G` = dof-multiplicity diagonal (non-law: `≠ I`); `G Gᵀ ≠ I` (non-law). All syntactic
  on the positive index map.
- **Dependencies:** `depends-on concepts/element-local-tensor` (shape-vocabulary); `pulled-by`
  `libceed-quadrature-kernel-impl`; references `concepts/tensor-field-lift`.
- **Status:** `rough-in` (promoted from roadmap_goal). Firm on the firm-on-positive-structure escape once
  `concepts/element-local-tensor` firms.
- **Evidence:** `restriction.cpp:389-426` (`InitRestriction`, lexico `:113` / native `:207`), `:200`
  (`CeedElemRestrictionCreate`, oriented `:192`), `bilinearform.cpp:64-70` (`trial_restr`/`test_restr`).

### geom_factor_build (rough-in)

- **Signature:** `geom_factor_build :: MeshNodes -> QuadWeights -> Tensor[(E, P, G)]`. `E` = element
  count; `P` = quad-points/element; `G` = geom-data components (`= 2 + space_dim*dim`). The `[E, P, G]`
  carrier shape home is `concepts/element-local-tensor`.
- **Semantics:** setup-stratum build-QFunction; per `(e,p)` packs the `𝒟`-determined Jacobian metric ×
  quad-weight (coefficient `Q` pre-multiplied) into `geom_data`; built once per `(mesh, order)`, reused
  across applies.
- **Algebraic laws (rough-in):** setup-stratum purity (pure of `(mesh_nodes, quad_weights)`);
  pointwise/element-local block-diagonality in `(E, P)`; `𝒟`-determined metric shape; affine-element
  constancy (special case). All syntactic on the positive build-QFunction.
- **Dependencies:** `depends-on concepts/element-local-tensor` (shape-vocabulary); `pulled-by`
  `libceed-quadrature-kernel-impl`; references `concepts/build-time-vs-run-time-stratification`.
- **Status:** `rough-in` (promoted from roadmap_goal). Firm on the firm-on-positive-structure escape once
  `concepts/element-local-tensor` firms.
- **Evidence:** `integrator.cpp:335-421` (`AssembleCeedGeometryData`; switch `:348-384`; inputs
  `attr :387` / `q_w :388` / `grad_x :389-390`; output `geom_data :397-398`; size `MFEM_VERIFY :395`),
  `:423-427` + `:483-484` (`AssembleCeedOperator` consumer site), `integrator.hpp:14-23` (`EvalMode`).

## Supporting evidence

All anchors citecheck-verified on-disk (`--anchor` pass, 16/16 clean). Codemap+on-disk drift corrected:
- `restriction.cpp` `InitRestriction` END `:425 → :426` (the function's closing `}` is line 426 on-disk;
  the prior roadmap_goal entry cited `:425` — an END off-by-one, the FE-source close-brace drift class).
- `integrator.cpp` build-QFunction re-anchors (codemap and on-disk AGREE here, but the prior entry's
  numbers had drifted): function `AssembleCeedGeometryData` `:335-421` (prior `:340-419` truncated both
  ends); `attr :386 → :387`; `q_w :387-388 → :388`; `MFEM_VERIFY :394 → :395`; `geom_data` output
  `:396-398 → :397-398`; consumer site `AssembleCeedOperator` `:423-465 → :423-427` (signature) plus the
  actual `geom_data` field-set `:483-484` (the prior `:423-465` did not reach the `:483` threading site).

Semantic-surface fix (both files): `book/src/design/l4_calculus.md` §1.2.1 → `book/src/semantics/index.md`
§1.2.1 (the named-shape-groups surface moved batch-37; USE+LINK, not restated). Per the plan caveat, the
stale-path drift may exist in other batch-37-era files — flagged below for the meta-phase.

## Open questions / caveats

- **Consolidated tally deferred to D5.** Per the cycle-124 Overlap consolidated-tally partition, I did
  NOT touch the `L1/index.md` "Roadmap_goal (libCEED contraction substrate — 4)" header count (line 101)
  or the firm/grand-total tally. Both `element_restrict` and `geom_factor_build` left the roadmap_goal
  cohort for rough-in this wave (and D3's `basis_apply` + `quad_point_contract` likely too) — D5 must
  reconcile the "— 4" cohort header (now potentially "— 0" if all four promote) + any firm-count growth
  note. I emitted only my two member bullets + two table rows.
- **`concepts/element-local-tensor` is a forward-reference (D5 authors it this wave).** I reference it by
  the planner-stated canonical slug `concepts/element-local-tensor` as a plain-text inline-code span
  (NOT a live markdown link) in chapter prose, since the file does not yet exist at my authoring time —
  per the forward-reference-must-be-plain-text rule (a live link to a missing file is a hard
  `linkcheck2` error). The dep-map frontmatter `depends-on` edge target is the bare slug (linter reads
  the slug, not a link). Once D5 lands the page, a follow-up may upgrade the prose references to live
  links.
- **Maturity is rough-in, not firm — honest clean-gate.** The structural decomposition + syntactic laws
  qualify for the firm-on-positive-structure escape, but well-foundedness blocks firm: a rough-in op may
  rest on the to-be-firm `concepts/element-local-tensor` shape home, a firm op may not. Both promote
  `rough-in → firm` the moment D5's record page firms (no further evidence needed — the laws are already
  syntactic identities on positive source). If D5 lands the record page firm THIS wave, a same-cycle or
  next-cycle firm-flip of these two is the clean follow-up; the integrator should not read rough-in as a
  failed promotion (it is a one-rank honest climb from roadmap_goal).
- **Stale-semantic-path drift-check (meta-phase candidate).** The `design/l4_calculus.md` §1.2.1 →
  `semantics/index.md` §1.2.1 path move (batch-37) left stale citations in the libceed-substrate
  roadmap_goals; D3/D4/D5 fix the four substrate files on touch, but other batch-37-era files may carry
  the same stale path. Flagged for a meta-phase semantic-surface drift sweep.
