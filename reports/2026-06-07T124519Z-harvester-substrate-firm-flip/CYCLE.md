---
agent: harvester
invoked_at: 2026-06-07T124519Z
scope: L1 firm-flip cohort — element_restrict + geom_factor_build + libceed-quadrature-kernel-impl (rough-in → firm); SOLE-OWN L1/index.md tally 45 → 47
status: integrated
integrated_at: 2026-06-07T124519Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-125 D1 (batch-40 MIDDLE). Applied clean by integrator-per-report (staging row 1); no gate hits. L1 firm 45→47 (element_restrict + geom_factor_build rough-in→firm, sole blocking dep concepts/element-local-tensor firm on disk c124 D5); libceed-quadrature-kernel-impl rough-in→firm (4 depends-on(composes) substrate deps now firm); realizes-kernel-api edge stays reference-class, the kernel-api obstruction surface untouched. CLOSED OQ libceed-substrate-rough-in-to-firm-flip-and-45-to-47-tally-followup. rank_violations 0. Build EXIT 0, no finalize build-repair."
inputs:
  - reports/2026-06-07T124519Z-cycle-planner-c125/CYCLE.md (D1 entry)
  - book/src/concepts/element-local-tensor.md (firm on disk, c124 D5, commit db5ea4d) — the shape-vocabulary home whose firming lifts the well-foundedness cap
  - book/src/L1/basis_apply.md + book/src/L1/quad_point_contract.md (firm on disk, c124 D3) — the other two kernel-impl composes-deps
  - OQ libceed-substrate-rough-in-to-firm-flip-and-45-to-47-tally-followup (closes)
---

# CYCLE: Firm-flip the libCEED contraction substrate — element_restrict + geom_factor_build + libceed-quadrature-kernel-impl (45 → 47)

## Summary

Three L1 nodes were capped below firm in the c124 substrate-cohort wave only because their
shape-vocabulary home `concepts/element-local-tensor` was firming in the same wave. That record page
is now `firm` on disk (c124 D5, commit `db5ea4d`), so the well-foundedness cap lifts and all three
flip `rough-in → firm` via the **firm-on-positive-structure escape**:

1. **`element_restrict`** (the `G`/`Gᵀ` gather/scatter-add stage) — its sole blocking edge
   `depends-on (shape-vocabulary)` → `concepts/element-local-tensor` now rests on a firm dep
   (`rank(u) ≤ min(deps)`: rough-in→firm warranted). Its laws are syntactic gather/scatter-add
   operator-algebra identities on the positively-read Boolean index map (`InitRestriction`); no test
   gates them.
2. **`geom_factor_build`** (the setup-stratum geometry-factor build-pass) — same: its
   `depends-on (shape-vocabulary)` → `concepts/element-local-tensor` now rests on a firm dep. Laws are
   syntactic setup-stratum-purity / pointwise-block-diagonality identities on the positively-read
   build-QFunction (`AssembleCeedGeometryData`).
3. **`libceed-quadrature-kernel-impl`** (the kernel-IMPL node) — capped at `min(deps)` over its four
   `depends-on (composes)` substrate deps. Two were already firm (`basis_apply` +
   `quad_point_contract`, c124 D3); the other two (`element_restrict` + `geom_factor_build`) firm in
   THIS report. So `min(deps)` rises firm → `rank(impl) ≤ min(deps) = firm`. Its laws are
   syntactic-identity composition facts on the positively-read `AssembleCeedOperator` pipeline. The
   `realizes-kernel-api` edge stays `reference`-class (the firm-flip is on the kernel-IMPL node, NOT
   the kept kernel-api obstruction surface).

This **completes the libCEED-substrate sub-spine** (4 firm + kernel-impl firm; sub-spine count 2→4
firm), **fires the kernel-impl** (the constructive realization of the libCEED element-quadrature
kernel is now firm vocabulary the c125 D2 L2 contraction-chain combinator rests on), and reconciles
the **drifted L1/index.md tally to 47** (33 main + 4 FE-assembly + 5 FE-space + 1 Mesh-construction +
4 libCEED-substrate). The index narrative carried multi-era count-history (both `45` and `43`); this
reconcile drains the stale prose to a single clean current count of **47**. Closes OQ
`libceed-substrate-rough-in-to-firm-flip-and-45-to-47-tally-followup`.

## Precondition verification (on-disk, this dispatch)

- `concepts/element-local-tensor.md` reads `rank: firm` on disk (frontmatter `:2`, `## Status` `:153`)
  — the cap-lifting dep is firm. ✓
- `basis_apply.md` reads `rank: firm`; `quad_point_contract.md` reads `rank: firm` (the other two
  kernel-impl `composes`-deps) — so post-flip all four kernel-impl composes-deps are firm,
  `min(deps) = firm`. ✓
- **firm-on-positive-structure escape genuinely applies** to each (laws are syntactic identities on
  positive source, no test gates them — re-checked the cited L0 anchors hold via `citecheck --anchor`
  on-disk this dispatch):
  - `element_restrict`: `InitRestriction` (`palace/fem/libceed/restriction.cpp:389-426`,
    anchor `InitRestriction` at `:389` ✓), `CeedElemRestrictionCreate` (`:200` ✓),
    `trial_restr`/`test_restr` (`palace/fem/bilinearform.cpp:64-70`, anchor `trial_restr` at `:64` ✓).
  - `geom_factor_build`: `AssembleCeedGeometryData` (`palace/fem/libceed/integrator.cpp:335-421`,
    anchor at `:335` ✓), `geom_data_size` verify (`:395`, anchor `geom_data_size` ✓).
  - `libceed-quadrature-kernel-impl`: `AssembleCeedOperator` (`palace/fem/libceed/integrator.cpp:423-445`,
    anchor at `:423`, the 5-input signature `:423-427` read on-disk this dispatch ✓),
    `BilinearFormIntegrator::Assemble` pure-virtual leaf contract (`palace/fem/integrator.hpp:58-61`,
    anchor `Assemble` at `:58` ✓).

No node is firmed whose laws need a test it does not have: every law in all three is a syntactic
identity / composition fact on fully-specified positive source.

## Proposed changes

### 1. element_restrict.md — rank: rough-in → firm

```edit:book/src/L1/element_restrict.md
---
layer: L1
operator: element_restrict
# Graded-stack: firm (rank 3). The G / Gᵀ stage of A = Gᵀ B_𝒟ᵀ D B_𝒟 G. Promoted roadmap_goal →
# rough-in (cycle-124 D4) → firm (cycle-125 D1) on the element-local rank-tensor vocabulary: the
# shape-vocabulary home concepts/element-local-tensor (firm c124 D5, commit db5ea4d) defines the
# rank-structured element-local tensor Tensor[(E, L)] this op contracts over, so the op RESTS on a
# firm shape home. depends-on concepts/element-local-tensor (the [E, L] shape home) — rank invariant
# rank(u) <= min(deps): the dep is now firm, so the firm-flip is warranted (the firm-on-positive-
# structure escape, gated only by the shape vocabulary, not by tests — laws are syntactic gather/
# scatter-add identities on positive source). The flat global axis N stays a genuine rank-1
# Tensor[(N: ...)] (L1/L0 flat-vector convention). Reachable: pulled-by libceed-quadrature-kernel-impl,
# which reaches the feature root via the fe_assemble fold's feature-column inbound edges.
rank: firm
edges:
  depends-on:
    - target: concepts/element-local-tensor
      kind: shape-vocabulary   # the [E, L] element-local rank-tensor shape home this op's signature contracts over (firm c124 D5; rank-constrained, GC-live)
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

`firm` (rank 3). **Promoted roadmap_goal → rough-in (cycle-124 D4) → firm (cycle-125 D1).** The Palace
realization is exhaustively anchored (see *Verified-against* — `CeedElemRestriction` construction and
its index-map builder), and the operator's signature contracts over the **element-local rank-tensor**
`Tensor[(E, L)]` (element axis `E`, local-dofs-per-element axis `L`) whose **shape-vocabulary home is
`concepts/element-local-tensor`** — now **firm on disk** (c124 D5, commit `db5ea4d`). With that home
firm (as a `depends-on` shape-vocabulary edge), the op rests on a firm shape and the well-foundedness
cap lifts: `rank(u) ≤ min(deps)` no longer bounds this op below firm. The promotion is on the
**firm-on-positive-structure escape** — every algebraic law below is a syntactic gather/scatter-add
operator-algebra identity on fully-specified positive source (the index map is read directly off
`InitRestriction`), so the absence of a dedicated restriction unit test does not gate firm; the only
gate was the firmness of the `[E, L]` shape home, now discharged. The flat global axis `N` stays a
genuine rank-1 `Tensor[(N: ...)]` dof-vector (the firm L1 `Tensor[N]` convention for Palace `Vector` —
KEPT flat) and is NOT part of the shape-vocabulary shift.

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

## Algebraic laws (firm — syntactic identities on positive source)

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
Boolean index map. They require no test (firm-on-positive-structure); the only gate was the firmness of
the `[E, L]` shape home (`concepts/element-local-tensor`), now firm on disk (c124 D5).

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
- `book/src/L1/libceed-quadrature-kernel-impl.md` — the firm kernel-impl consumer whose pipeline
  `A = Gᵀ B_𝒟ᵀ D B_𝒟 G` composes this `G`/`Gᵀ` stage (pulled-by).

## Related

- [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md) — the firm kernel-impl that
  composes this stage (the `G`/`Gᵀ` ends of the pipeline).
- [`basis_apply`](./basis_apply.md) — the `B`/`Bᵀ` stage applied AFTER `G` (and before `Gᵀ`).
- `concepts/element-local-tensor` — the `[E, L]` element-local rank-tensor shape-vocabulary home this
  op's element-local side rests on (the `depends-on` shape edge).
- `concepts/tensor-field-lift` — `Gᵀ` (assembly) is the element→global lift this substrate targets.
```

### 2. geom_factor_build.md — rank: rough-in → firm

```edit:book/src/L1/geom_factor_build.md
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
```

### 3. libceed-quadrature-kernel-impl.md — rank: rough-in → firm

Frontmatter `rank:` + the leading scheme comment + the two §Status paragraphs that conclude
"rough-in" / "CANNOT be firm" + the §"Substrate L1 operators" header and its closing paragraph are
re-anchored to the firm verdict (the within-file end-to-end self-consistency re-anchor mandated when
flipping the operator's own §Status). The `realizes-kernel-api` / `realizes-leaf` reference edges are
UNCHANGED (the flip is on the kernel-IMPL node; the kernel-api obstruction surface is untouched).

```edit:book/src/L1/libceed-quadrature-kernel-impl.md
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
    verdict: empirical-anchor-confirmed-deferred
    audited_at: 2026-06-07T093000Z
    note: TestCeedOperatorFullAssemble exists (:284); :298 asserts mat_diff MaxNorm < 1.0e-12 * max(mat_ref MaxNorm, 1.0) — assembled libCEED matrix matches MFEM reference to 1e-12. The empirical-match target for the FIRMING audit (the lowering-verifier re-audit owed now that the impl is firm — c125 D1). Path is palace/test/... single-palace under reference/, NOT doubled.
```
```

## L1/index.md tally reconciliation (SOLE-OWNED — 45 → 47)

Four edits to `book/src/L1/index.md`: (1) the §"Firm" header paragraph (`:47`) — drain ALL stale
`43`/`45` count-history to a single clean current grand total of **47**, mark the two flipped ops +
the kernel-impl firm, set libCEED-substrate = **4**; (2) the kernel-impl FE-assembly-section bullet
(`:99`) — rough-in → firm; (3) the libCEED-substrate sub-spine header + the two flipped-op bullets
(`:101`, `:103`, `:106`) — 2 firm + 2 rough-in → 4 firm; (4) the AMR-cohort cross-reference (`:134`)
— 43-member → 47-member; plus the kernel-impl + element_restrict + geom_factor_build dep-map table
rows (`:187`, `:188`, `:191`) — Status → firm.

### 4a. §"Firm" header paragraph (drain multi-era count-drift to a single clean 47)

```edit:book/src/L1/index.md
**Firm (33 main cohort; 47 firm grand total incl. the FE-assembly + FE-space + Mesh-construction + libCEED-substrate sub-spines — the libCEED-substrate sub-spine is now COMPLETE at 4 firm: the cycle-124 substrate-cohort wave firmed `basis_apply` + `quad_point_contract` (D3, the arithmetic `B` basis-eval + `D` pointwise-diagonal stages) and the cycle-125 D1 firm-flip firmed `element_restrict` + `geom_factor_build` (the `G`/`Gᵀ` gather/scatter + the geometry-factor build-pass) the moment their shape home `concepts/element-local-tensor` firmed (c124 D5); the `libceed-quadrature-kernel-impl` consumer firmed alongside (its `min(deps)` rose firm). All four substrate ops are typed over the firm `concepts/element-local-tensor` shape family. The grand total is read off each chapter's on-disk `## Status`: 33 main + 4 FE-assembly + 5 FE-space + 1 Mesh-construction + 4 libCEED-substrate = 47.** The 33 main-cohort firm operators are listed below; the FE-assembly sub-spine adds **4** more firm (`fe_assemble` c054 + `weak_form_term` c061 + `eliminate_essential_bc` + `eliminate_rhs` both c055 — see the §"Firm (FE-assembly sub-spine)" subsection), the FE-space sub-spine adds **5** more firm (`fe_space` c064 + `fe_collection` c065 + `essential_dofs` c066 + `fe_space_hierarchy` c117 + the de-Rham interpolator c117 — see the §"Firm (FE-space sub-spine)" subsection), the **Mesh-construction sub-spine** adds **1** more firm (`build_mesh` c117 — the `(config) → Mesh` mesh-wrapper, single-machine scope), and the **libCEED-substrate sub-spine** adds **4** more firm (`basis_apply` + `quad_point_contract` c124 D3 + `element_restrict` + `geom_factor_build` c125 D1 — see the §"libCEED contraction substrate" subsection), bringing the L1 firm grand total to **47**. **Count discipline: the grand total is computed by reading each linked chapter's on-disk `## Status` line, not the index cells — 33 main + 4 FE-assembly + 5 FE-space + 1 Mesh-construction + 4 libCEED-substrate = 47.** (Growth log, most-recent first: cycle-125 D1 firmed the libCEED-substrate sub-spine to 4 — `element_restrict` + `geom_factor_build` rough-in→firm on the firm-on-positive-structure escape once `concepts/element-local-tensor` firmed, + the `libceed-quadrature-kernel-impl` kernel-impl consumer rough-in→firm as its `min(deps)` rose, 45→47; cycle-124 D3 firmed the libCEED-substrate sub-spine's first two members `basis_apply` + `quad_point_contract`, 43→45; cycle-117 wide wave added `build_mesh` D3 + `fe_space_hierarchy` D4 + the de-Rham interpolator D5 to 43; cycle-104 D3 added the 33rd main-cohort firm member `set_subvector_zero`, the `s=0.0` index-set vector-zeroing essential/port-BC cleanup atom — the diagonal 0/1 projector `Z_idx = I − P_idx`, vector-side sibling of `eliminate_essential_bc`, promoted firm on the firm-on-positive-structure escape; cycle-095 D1 added the 32nd main-cohort firm member `bilinear-form`, the matrix-weighted inner-product reduction `xᴴ M y` — promoted rough-in→firm by the `bilinear-form-firm-flip-and-cascade-wave` on the firm-on-positive-structure escape, firmability discharged by the cycle-092 `lowering-verifier` probe; cycle-091 D1 promoted `matrix-weighted-norm` rough-in (test-coverage-bounded)→firm by the batch-29 LEAD firm-flip-and-cascade wave; cycle-080 D2 added `eigenvalue-untransform`, the eigenvalue→ω un-transform scalar map `√μ`/`λ/i`; cycle-077 D5 added `port_projection`, the port-mode linear-functional projection `⟨s, E⟩`; cycle-077 D4 added `participation_ratio`, the energy-participation-ratio scalar-quotient primitive; cycle-066 D1 added the FE-space sub-spine's `essential_dofs`, the boundary-attribute→essential-true-dof-set constructor.) All firm rows are now on-table; there is no off-table firm operator. The 33 main-cohort firm operators are element-wise updates, BLAS-1 reductions, the matrix-weighted inner-product reduction (`bilinear-form`, c095 — `xᴴ M y` for arbitrary linear `M`, the matrix-weighted generalisation of `dot`), the fused-normalise primitive, the energy-participation-ratio scalar-quotient primitive (`participation_ratio`, c077), the eigenvalue→ω un-transform scalar map (`eigenvalue-untransform`, c080 — the `√μ`/`λ/i` per-mode un-transform keyed on EVP-degree, the second per-mode scalar building block of `eigenfreq_qfactor_reduce`), the port-mode linear-functional projection (`port_projection`, c077), the opaque-operator gate, the constructed-operator solve gate, the eigenmode-solve gate, the polynomial-smoother gate, the divergence-free projector gate, the nonlinear-pencil interior atom, the NEP deflated-residual extension, the small-dense direct-solve gate, the NEP deflated-solve extension, the NEP quasi-Newton Jacobian action, the NEP quasi-Newton eigenvalue-correction step, the GMRES/FGMRES restart-correction back-solve, the GMRES/FGMRES per-column running-QR leaf, the diagonal-preconditioner-apply Jacobi smoother, the elementwise multiplicative-inverse primitive, the elementwise (Hadamard) pointwise-product primitive, the floquet-periodicity B-field correction gate, the driven per-ω system-operator assembly (`assemble_frequency_operator`, c062), the SPD operator-weighted energy norm (`matrix-weighted-norm`, c091 — `‖x‖_B = √(xᴴ B x)`), and the index-set vector-zeroing essential/port-BC cleanup atom (`set_subvector_zero`, c104 — the `s=0.0` specialization of `linalg::SetSubVector`, the diagonal 0/1 projector `Z_idx = I − P_idx`, vector-side sibling of `eliminate_essential_bc` and the primitive `eliminate_rhs`/`divfree-projector` use at their essential-dof pin / RHS-clean steps):
```

### 4b. kernel-impl bullet in the FE-assembly section (rough-in → firm)

```edit:book/src/L1/index.md
- **`libceed-quadrature-kernel-impl` is now `firm` (kernel-impl)** *(cycle-121 D4 roadmap_goal → cycle-124 D5 rough-in → cycle-125 D1 firm)* — see [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md). The constructive, in-our-tensor-algebra realization of the per-term assembly leaf `A(space, term)` that [`fe_assemble`](./fe_assemble.md) folds over opaquely: the libCEED element-quadrature kernel as the contraction pipeline `A = Gᵀ B_𝒟ᵀ D(Q, geom) B_𝒟 G` (restriction-gather ▷ basis-eval ▷ pointwise geom×coeff×weight contraction ▷ basis-apply-transpose ▷ restriction-scatter). The DIRECTIVE-3 **kernel-impl** counterpart of the KEPT [`fe-assemble-libceed-boundary-obstruction`](../L1-L0/fe-assemble-libceed-boundary-obstruction.md) **kernel-api** surface, linked by a free `realizes-kernel-api` reference edge (NOT a `depends-on` — a reviewed correspondence, audited by `lowering-verifier`). **Promoted roadmap_goal → rough-in (cycle-124 D5) → firm (cycle-125 D1):** all four substrate ops are now firm L1 vocabulary (`basis_apply` + `quad_point_contract` FIRM c124 D3; `element_restrict` + `geom_factor_build` FIRM c125 D1, the moment their shape home `concepts/element-local-tensor` firmed c124 D5), all typed over the firm [`concepts/element-local-tensor`](../concepts/element-local-tensor.md) shape family. With all four `composes` deps firm, `rank(impl) ≤ min(deps) = firm`, so this node promotes firm on the firm-on-positive-structure escape (its laws are syntactic-identity composition facts on the positively read `AssembleCeedOperator` pipeline — no test gates them). The obstruction theme STAYS the kernel-api surface (NOT downgraded; the firm-flip is on the kernel-IMPL node ONLY). Does NOT change the FE-assembly sub-spine firm count (still 4 firm; the kernel-impl is counted in the libCEED-substrate sub-spine, not FE-assembly).
```

### 4c. libCEED contraction substrate sub-spine header + the two flipped-op bullets

```edit:book/src/L1/index.md
**libCEED contraction substrate (opened cycle-122 D4 roadmap_goal; COMPLETE cycle-125 — 4 firm)** — the four tensor-contraction substrate ops that are the stages of the matrix-free FE operator-application pipeline `A = Gᵀ B_𝒟ᵀ D B_𝒟 G` (the `libceed-quadrature-kernel-impl` `depends-on (composes)` substrate). **The cycle-124 substrate-cohort wave (D3+D4+D5) firmed the element-local rank-tensor vocabulary shift** — the rank-structured element-local / quad-point tensors (`Tensor[(E, L)]` / `Tensor[(E, P, C)]` / `Tensor[(E, P, G)]`) the firm flat-vector-BLAS L1 (`Tensor[N]`) does not carry now have a firm data-shape home, [`concepts/element-local-tensor`](../concepts/element-local-tensor.md) (c124 D5) — and the **cycle-125 D1 firm-flip** completed the sub-spine. The four ops are now ALL firm: `basis_apply` + `quad_point_contract` → **firm** (c124 D3, firm-on-positive-structure; the arithmetic basis-eval `B` and pointwise-diagonal `D` stages); `element_restrict` + `geom_factor_build` → **firm** (c125 D1; the gather/scatter `G` indexing + the geometry-factor build-pass — each `depends-on` the shape home and was capped on its firmness, promoted rough-in→firm the moment `concepts/element-local-tensor` firmed, on the firm-on-positive-structure escape). The consumer `libceed-quadrature-kernel-impl` is now **firm** (its `min(deps)` rose to firm with all four substrate ops firm). The decomposition is structurally exhaustive (read directly off `AssembleCeedOperator` + the build-QFunction). The four member bullets (the maturity is read off each chapter's `## Status`):

- **`element_restrict` is now FIRM** *(cycle-122 D4 roadmap_goal → cycle-124 D4 rough-in → cycle-125 D1 firm)* — see [`element_restrict`](./element_restrict.md). The **G / Gᵀ** stage: the per-element gather (`G`, global true-dof → per-element local-dof `Tensor[(N: ...)] → Tensor[(E, L)]`) and its transpose scatter-add (`Gᵀ`, assembly). Pure gather/scatter, no arithmetic; `Gᵀ G` is the dof-multiplicity diagonal, `G Gᵀ ≠ I`. **Promoted rough-in → firm** on the element-local rank-tensor vocabulary: `depends-on` `concepts/element-local-tensor` (the `[E, L]` shape home) is now firm on disk (c124 D5), so the well-foundedness cap lifts and the op firms on the firm-on-positive-structure escape (laws are syntactic gather/scatter-add identities on positive source). L0: `InitRestriction` (`palace/fem/libceed/restriction.cpp:389-426`), `CeedElemRestrictionCreate` (`:200`), `trial_restr`/`test_restr` (`palace/fem/bilinearform.cpp:64-70`).
- **`basis_apply` is now FIRM** *(cycle-124 D3)* — see [`basis_apply`](./basis_apply.md). The **B / Bᵀ** stage: basis evaluation contracting per-element dofs to quad-point values `Tensor[(E, L)] → Tensor[(E, P, C)]`, keyed on the `EvalMode` (`Interp`/`Grad`/`Curl`/`Div`) the term's `𝒟` selects. **Promoted roadmap_goal → firm**: the element-local rank-tensor is now firm L1 vocabulary (`concepts/element-local-tensor`, cycle-124 D5), and the laws are firm-on-positive-structure syntactic identities (adjoint basis-eval pairing, per-element linearity, block-diagonality in `E`) read off the libCEED operator-construction code — no-dedicated-test caveat non-gating per the `weak_form_term`/`fe_assemble` precedent. Sum-factorization is a **transparent trick** (one-line note — resolves OQ `libceed-quadrature-kernel-impl-sum-factorization-classification`). L0: `AddQFunctionActiveInputs` (`palace/fem/libceed/integrator.cpp:25-65`), `EvalMode` (`palace/fem/libceed/integrator.hpp:14-23`), `InitBasis`/`InitTensorBasis` (`palace/fem/libceed/basis.cpp:169-180,:15-35`).
- **`quad_point_contract` is now FIRM** *(cycle-124 D3)* — see [`quad_point_contract`](./quad_point_contract.md). The **D** stage: the pointwise per-quad-point contraction `geom_data ⊙ ·` over `Tensor[(E, P, C)]` — the embarrassingly-parallel diagonal (the per-quad-point lift `concepts/tensor-field-lift`). **Promoted roadmap_goal → firm**: the element-local rank-tensor is now firm L1 vocabulary (`concepts/element-local-tensor`, cycle-124 D5), closing the substrate gap (the flat-`Tensor[N]` `elementwise_product` lifts to the `[E, P, C]` diagonal); the laws are firm-on-positive-structure syntactic identities (pointwise-no-coupling block-diagonal in `(E, P)`, linearity-in-field, self-adjoint-when-symmetric). L0: the apply-QFunction wiring (`palace/fem/libceed/integrator.cpp:451-495`; `geom_data` `:457-458`, `q_w` `:462`, active in/out `:492`/`:493`), the `f_apply_*` kernels (`:215-308`, `f_apply_22` `:260`).
- **`geom_factor_build` is now FIRM** *(cycle-122 D4 roadmap_goal → cycle-124 D4 rough-in → cycle-125 D1 firm)* — see [`geom_factor_build`](./geom_factor_build.md). The geometry-factor **build-pass**: `(mesh-nodes, quad-weights) → geom_data :: Tensor[(E, P, G)]` (Jacobian metric × quad-weight, with the material coefficient pre-multiplied in). The **setup stratum** of the build/run-time split (`concepts/build-time-vs-run-time-stratification`) — built once per `(mesh, order)`, reused across applies. **Promoted rough-in → firm** on the element-local rank-tensor vocabulary: `depends-on` `concepts/element-local-tensor` (the `[E, P, G]` carrier shape home) is now firm on disk (c124 D5), so the well-foundedness cap lifts and the op firms on the firm-on-positive-structure escape (laws are syntactic setup-stratum-purity / pointwise identities on positive source). L0: `AssembleCeedGeometryData` (`palace/fem/libceed/integrator.cpp:335-421`; QFunction dispatch `:348-384`, inputs `attr`/`q_w`/`grad_x` `:387`/`:388`/`:389-390`, output `geom_data` `:397-398`).
```

### 4d. AMR-cohort cross-reference (43-member → 47-member)

```edit:book/src/L1/index.md
**Firm (AMR estimate/mark vocabulary) — DIRECTIVE-2 (2026-06-07):** the AMR estimate→mark→refine grounded consumer (the `amr-estimate-mark-refine` L1>L0 theme's verbs). This cohort carries no consolidated running count (its members are AMR-vocabulary-group, distinct from the 47-member L1 firm grand total spanning the main + FE-assembly + FE-space + Mesh-construction + libCEED-substrate sub-spines).
```

### 4e. dep-map table rows — kernel-impl + element_restrict + geom_factor_build → firm

```edit:book/src/L1/index.md
| [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md) | `(space, term=(Q, 𝒟)) → LinearOperator[(N: ...)]` (i.e. the per-term assembly leaf `A(space, term) = Gᵀ B_𝒟ᵀ D(Q, geom) B_𝒟 G` — the libCEED element-quadrature kernel as a tensor-contraction pipeline) | composes the firm tensor-contraction substrate `element_restrict` (G) / `basis_apply` (B) / `quad_point_contract` (D) / `geom_factor_build` (all firm — 2 c124 D3, 2 c125 D1); `realizes-kernel-api` (reference) → [`fe-assemble-libceed-boundary-obstruction`](../L1-L0/fe-assemble-libceed-boundary-obstruction.md); `realizes-leaf` (reference) the opaque `A(space, ·)` leaf of firm [`fe_assemble`](./fe_assemble.md) | `firm` (**kernel-impl**; DIRECTIVE-3 item-2a constructive realization of the libCEED element-quadrature kernel; promoted roadmap_goal→rough-in (c124 D5)→firm (c125 D1) once all four `composes` substrate deps firmed — `rank(impl) ≤ min(deps) = firm`, on the firm-on-positive-structure escape (laws syntactic-identity composition facts on the positively read `AssembleCeedOperator` pipeline); the obstruction theme is KEPT as the kernel-api surface, NOT downgraded; `realizes-kernel-api` is a free reference edge, NOT depends-on; proposed-by: abstractor:2026-06-07T054924Z-abstractor-libceed-quadrature-kernel-impl) |
```

```edit:book/src/L1/index.md
| [`element_restrict`](./element_restrict.md) | `ElemRestriction → Tensor[(N: ...)] → Tensor[(E, L)]` (G, gather); transpose `Tensor[(E, L)] → Tensor[(N: ...)]` (Gᵀ, scatter-add/assembly) | `depends-on` (shape-vocabulary) `concepts/element-local-tensor` (the `[E, L]` element-local rank-tensor shape home, firm c124 D5); `pulled-by` (reference) [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md) — the G/Gᵀ stage of its `A = Gᵀ B_𝒟ᵀ D B_𝒟 G` pipeline; references `concepts/tensor-field-lift` (Gᵀ assembly) | `firm` (promoted roadmap_goal → rough-in cycle-124 D4 → firm cycle-125 D1 on the element-local rank-tensor vocabulary; the per-element gather/scatter over the `[E, L]` element-rank tensor, resting on the now-firm `concepts/element-local-tensor` shape home; flat global axis `N` stays rank-1 `Tensor[(N: ...)]`; firmed on the firm-on-positive-structure escape the moment the shape home firmed — laws are syntactic gather/scatter-add identities on positive source; proposed-by: harvester:2026-06-07T112037Z-harvester-element-restrict-geom-factor, firm-flip harvester:2026-06-07T124519Z-harvester-substrate-firm-flip) |
```

```edit:book/src/L1/index.md
| [`geom_factor_build`](./geom_factor_build.md) | `MeshNodes → QuadWeights → Tensor[(E, P, G)]` (geometry-factor build-pass: Jacobian metric × quad-weight, coefficient pre-multiplied) | `depends-on` (shape-vocabulary) `concepts/element-local-tensor` (the `[E, P, G]` quad-point-rank carrier shape home, firm c124 D5); `pulled-by` (reference) [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md) — the build-QFunction whose geom_data its D stage consumes; references `concepts/build-time-vs-run-time-stratification` | `firm` (promoted roadmap_goal → rough-in cycle-124 D4 → firm cycle-125 D1 on the element-local rank-tensor vocabulary; the setup-stratum geometry-factor pass over the `[E, P, G]` quad-point-rank carrier, resting on the now-firm `concepts/element-local-tensor` shape home; built once per `(mesh, order)`, reused across applies; firmed on the firm-on-positive-structure escape the moment the shape home firmed — laws are syntactic setup-stratum-purity / pointwise identities on positive source; proposed-by: harvester:2026-06-07T112037Z-harvester-element-restrict-geom-factor, firm-flip harvester:2026-06-07T124519Z-harvester-substrate-firm-flip) |
```

## Supporting evidence

- `concepts/element-local-tensor.md:2,153` — `rank: firm` + `## Status` firm (the cap-lifting dep,
  c124 D5, commit `db5ea4d`). On-disk this dispatch.
- `book/src/L1/basis_apply.md` / `quad_point_contract.md` — `rank: firm` (the other two kernel-impl
  composes-deps, c124 D3). On-disk this dispatch (`grep rank:`).
- L0 anchors re-confirmed via `tools/citecheck/citecheck.py --anchor` on-disk this dispatch:
  `restriction.cpp:389` (`InitRestriction`), `:200` (`CeedElemRestrictionCreate`),
  `palace/fem/bilinearform.cpp:64` (`trial_restr`), `palace/fem/libceed/integrator.cpp:335`
  (`AssembleCeedGeometryData`), `palace/fem/libceed/integrator.cpp:395` (`geom_data_size`),
  `palace/fem/libceed/integrator.cpp:423` (`AssembleCeedOperator`), `palace/fem/integrator.hpp:58`
  (`Assemble`) — all `[ok]`.
  `AssembleCeedOperator` 5-input signature `palace/fem/libceed/integrator.cpp:423-427` +
  `InitRestriction` `palace/fem/libceed/restriction.cpp:389` read via codemap
  `read_range` (END-line guard for the cited ranges).
- Planner D1 deliverable-presence: all three targets `rough-in` on disk pre-flip (OPEN); the
  shape-home `firm` on disk (flip warranted); OQ open.

## Open questions / caveats

- **No new OQ.** This dispatch CLOSES OQ
  `libceed-substrate-rough-in-to-firm-flip-and-45-to-47-tally-followup` (the firm-flip + tally
  reconcile it routed to c125).
- **lowering-verifier re-audit owed (non-blocking, flagged not dispatched).** The kernel-impl's
  `realizes-kernel-api` correspondence audit (c124 D2) was a STRUCTURAL audit with empirical-match
  DEFERRED (the impl was then rough-in/roadmap_goal). Now that the impl is firm, the empirical-match
  target `test-libceed.cpp:284` (`TestCeedOperatorFullAssemble`, 1e-12 vs MFEM reference) is the
  re-audit anchor. The `verified_against` block records this; per the planner's standing-gate note no
  lowering-verifier dispatch is needed THIS cycle (the firm-flip changes only rank, and the c124 D2
  audit confirmed the correspondence FAITHFUL). Flagged for a future lowering-verifier pass as the
  impl is now firm.
- **D2 (c125, the L2 contraction-chain combinator) now rests on firm substrate.** This report firms
  the four substrate ops + the kernel-impl D2 composes; sequenced after D1 per the plan so D2's L2
  rank rests on firm deps (§(h) well-foundedness).
