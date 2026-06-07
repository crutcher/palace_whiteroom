---
rank: firm
kind: record
edges:
  depends-on:
    - target: palace/fem/libceed/restriction.cpp:200-203
      kind: cites-evidence            # CeedElemRestrictionCreate(ceed, num_elem=E, P=L /*nodes-per-element*/, vdim=C, comp_stride, vdim*ndofs, ...) — the [E,L] (and component C) restriction layout
    - target: palace/fem/libceed/basis.cpp:25-37
      kind: cites-evidence            # CeedBasisCreateTensorH1(ceed, dim, num_comp=C, P=L /*nodes*/, Q=P /*quad-points*/, Bt, Gt, qX, qW) — the basis layout binding L (nodes) ↔ P (quad-points) per component C
    - target: palace/fem/libceed/integrator.cpp:393-398
      kind: cites-evidence            # geom_data_size = 2 + space_dim*dim (MFEM_VERIFY :395) — the G axis; CeedQFunctionAddOutput("geom_data", geom_data_size, CEED_EVAL_NONE) :397-398
  reference:
    - L1/basis_apply
    - L1/quad_point_contract
    - L1/element_restrict
    - L1/geom_factor_build
    - L1/libceed-quadrature-kernel-impl
    - concepts/build-time-vs-run-time-stratification
---

# element-local-tensor

> **Kind: `record`.** This page defines the *data shape* of the **element-local rank-tensor family** —
> the `[E, L]` / `[E, P, C]` / `[E, P, G]` shapes the libCEED matrix-free FE operator-application
> substrate contracts over: the named axes, their meaning and construction-vs-run-time stratum, and
> the L0 home of the backing libCEED tensor layouts. The *behaviour* — how
> [`basis_apply`](../L1/basis_apply.md) contracts `[E, L] → [E, P, C]`, how
> [`quad_point_contract`](../L1/quad_point_contract.md) applies the pointwise `[E, P, C]` diagonal,
> how [`element_restrict`](../L1/element_restrict.md) gathers `[(N: ...)] ↔ [E, L]`, how
> [`geom_factor_build`](../L1/geom_factor_build.md) produces the `[E, P, G]` carrier — lives in those
> chapters; this page does NOT restate that contraction algebra. It defines only the *shape* those
> operators are typed over.

The **element-local rank-tensor family** is the shared data-shape vocabulary of the libCEED
element-quadrature contraction pipeline `A = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G` (the matrix-free FE
operator-application kernel — see [`libceed-quadrature-kernel-impl`](../L1/libceed-quadrature-kernel-impl.md)).
It is the **genuine vocabulary shift** away from the firm flat-vector-BLAS L1 (`Tensor[N]`, a rank-1
dof-vector): where flat L1 ops act on a single global axis, the element-local family carries the
**element axis `E`** and the per-element / per-quad-point structure that matrix-free FE assembly is
written over. Five named axes recur across the four substrate ops; this page is their definition home.
Multiple consumers (all four substrate ops + the kernel-impl that composes them) put it at the
≥2-consumer bar, so the shape family has a cross-cutting definition home here rather than being
re-declared per-chapter.

## One-line semantics

The element-local family names a small fixed set of **semantic axes** — `E` (mesh elements), `L`
(local dofs per element), `P` (quadrature points per element), `C` (value/derivative components), `G`
(geometry-data components) — and the three rank-structured tensors built from them (`[E, L]`,
`[E, P, C]`, `[E, P, G]`). These are **concrete named axes of fixed meaning**, not congruence shape
groups (`(S: ...)` / `$S`): each letter denotes one specific FE quantity, the way
`Tensor[H, W, VY=3, VX=3]` names concrete axes. The family carries no algebra of its own — it is the
shape over which the substrate ops' contractions are typed.

## Record definition — the named axes

The five axes, their meaning, and their construction-vs-run-time stratum (an axis is **build-stratum**
if its extent is fixed once per `(mesh, FE order)` and reused across every operator apply; it is
**run-stratum** if it indexes a per-apply field value):

| axis | name | meaning | stratum | L0 binding |
|---|---|---|---|---|
| `E` | element count | number of mesh elements (of a given geometry) the operator is assembled over. | build-time (fixed by the mesh; rebuilt on AMR refinement) | `num_elem` arg of `CeedElemRestrictionCreate` (`restriction.cpp:200-201`) |
| `L` | local dofs per element | dofs of the FE basis local to one element (`P_nodes`); `= dim`-product on a tensor-product element. | build-time (fixed by FE order + element geometry) | `elem_size`/`P` arg of `CeedElemRestrictionCreate` (`restriction.cpp:201`) = `num_nodes` `P` arg of `CeedBasisCreateTensorH1` (`basis.cpp:35`) |
| `P` | quadrature points per element | integration points per element (`Q`); set by the quadrature rule (FE order + over-integration). | build-time (fixed by the quadrature rule) | `num_qpts` `Q` arg of `CeedBasisCreateTensorH1` (`basis.cpp:35`) |
| `C` | value components | components of the basis-evaluated field at a quad point: `1` for scalar interp; `q_comp` (`= dim` for grad, `= dim`/`1` for curl/div) for derivatives. | run-time (a per-apply field-value axis) | `num_comp` arg of `CeedElemRestrictionCreate` / `CeedBasisCreateTensorH1` (`restriction.cpp:201`, `basis.cpp:35`), selected by the term's `EvalMode` |
| `G` | geometry-data components | per-quad-point precomputed geometry-metric storage; `G = 2 + space_dim*dim` (the metric `J⁻ᵀJ⁻¹\|J\|` / `\|J\|` × weight, coefficient pre-multiplied). | build-time (the setup-stratum factor — `geom_factor_build`) | `geom_data_size = 2 + space_dim*dim`, verified `MFEM_VERIFY` (`integrator.cpp:395`); `CeedQFunctionAddOutput("geom_data", geom_data_size, …)` (`integrator.cpp:397-398`) |

The three rank-structured tensors of the family (TS / shape-tuple form):

```text
Tensor[(E, L)]      -- per-element local-dof tensor: one local-dof vector per element
                    --   (the restricted / gathered field; the input to B and the output of Bᵀ)
Tensor[(E, P, C)]   -- per-quad-point value tensor: C components at each of P quad points, per element
                    --   (the basis-evaluated field; the operand of the pointwise D diagonal)
Tensor[(E, P, G)]   -- per-quad-point geometry-factor carrier: G metric components at each quad point
                    --   (geom_data; the setup-stratum factor D contracts against)
```

The **flat global axis `N`** is NOT part of this family: it stays a genuine rank-1 `Tensor[(N: ...)]`
dof-vector (the firm L1 `Tensor[N]` convention for Palace `Vector` — KEPT flat). `element_restrict`'s
`G` / `Gᵀ` is exactly the boundary between the flat `[(N: ...)]` global vocabulary and the
element-local `[E, L]` vocabulary this family defines (gather global → element-local; scatter-add
element-local → global). See the semantic surface [§1.2.3](../semantics/index.md) (named axes of fixed
meaning) for where this family sits in the shape-semantics convention, and §1.2 generally for the
distinction between a concrete named axis and a congruence shape group.

## Build-vs-run stratification

Per [`build-time-vs-run-time-stratification`](./build-time-vs-run-time-stratification.md): the axis
*extents* `E`, `L`, `P`, `G` are **build-stratum** — fixed once per `(mesh, FE order, quadrature
rule)` and reused across every operator apply (the restriction index map, the tabulated basis, and
`geom_data` are all built once). Only `C` indexes a **run-stratum** per-apply field value (and even
`C` is structurally fixed by the term's `EvalMode` — what varies per apply is the field *value* at
those `(e, p, c)` indices, not the shape). The `[E, P, G]` geometry carrier is wholly build-stratum
(`geom_factor_build` is a pure function of the mesh nodes + quad weights, cacheable and rebuilt only
on mesh change — e.g. AMR refinement). The `[E, P, C]` value tensor is the transient run-stratum
intermediate produced by `B` and consumed by `D` then `Bᵀ`.

## L0 source home — the libCEED tensor layouts

The family's backing layouts are the libCEED restriction + basis construction args (read single-rank
per CLAUDE.md §Scope — the multi-rank `ParMesh` shared-dof overlap is a deferred future direction):

- **`[E, L]` (and the component `C`)** — `CeedElemRestrictionCreate(ceed, num_elem /*=E*/, P
  /*=L, nodes-per-element*/, fespace.GetVDim() /*=C*/, comp_stride, vdim*ndofs, …)`
  (`palace/fem/libceed/restriction.cpp:200-203`). The restriction object maps the flat
  `vdim*ndofs`-length global vector into the `(E, L)`-shaped per-element local-dof tensor.
- **`L ↔ P` (basis layout) and `C`** — `CeedBasisCreateTensorH1(ceed, dim, num_comp /*=C*/, P
  /*=L, num_nodes*/, Q /*=P, num_qpts*/, maps.Bt, maps.Gt, qX, qW, …)`
  (`palace/fem/libceed/basis.cpp:25-37`). NOTE the libCEED parameter *names* invert the spec axis
  letters: libCEED's `P` argument is **nodes-per-element** (the spec's `L`) and libCEED's `Q` is
  **quad-points** (the spec's `P`). The spec uses `L` for local-dofs and `P` for quad-points
  consistently across the substrate chapters; this is the only naming hazard — the L0 binding is
  exact.
- **`G` (geometry-data components)** — `geom_data_size = 2 + space_dim*dim`, asserted by
  `MFEM_VERIFY(geom_data_size == 2 + space_dim * dim, …)` (`palace/fem/libceed/integrator.cpp:395`),
  and registered as the build-QFunction output `CeedQFunctionAddOutput(build_qf, "geom_data",
  geom_data_size, CEED_EVAL_NONE)` (`integrator.cpp:397-398`).

## Signatures / chapters that name this family

- [`basis_apply`](../L1/basis_apply.md) — **consumer** (firm, c124 D3): `B :: BasisMode → Basis →
  Tensor[(E, L)] → Tensor[(E, P, C)]` (and transpose `Bᵀ`). The basis-eval contraction between the
  `[E, L]` and `[E, P, C]` members.
- [`quad_point_contract`](../L1/quad_point_contract.md) — **consumer** (firm, c124 D3): `D ::
  GeomData → Tensor[(E, P, C)] → Tensor[(E, P, C')]`, `GeomData :: Tensor[(E, P, G)]`. The pointwise
  per-quad-point diagonal over `[E, P, C]` against the `[E, P, G]` carrier.
- [`element_restrict`](../L1/element_restrict.md) — **consumer** (rough-in, c124 D4): `G ::
  ElemRestriction → Tensor[(N: ...)] → Tensor[(E, L)]` (and transpose `Gᵀ`). The flat-`[(N: ...)]` ↔
  `[E, L]` gather/scatter boundary; `depends-on` THIS page for its `[E, L]` shape home.
- [`geom_factor_build`](../L1/geom_factor_build.md) — **consumer** (rough-in, c124 D4):
  `geom_factor_build :: MeshNodes → QuadWeights → Tensor[(E, P, G)]`. Produces the `[E, P, G]`
  carrier; `depends-on` THIS page for its carrier shape home.
- [`libceed-quadrature-kernel-impl`](../L1/libceed-quadrature-kernel-impl.md) — **consumer**
  (rough-in, c124 D5): composes all four substrate ops; the pipeline `A = Gᵀ B_𝒟ᵀ D B_𝒟 G` is typed
  over this family.

## See also

- [`libceed-quadrature-kernel-impl`](../L1/libceed-quadrature-kernel-impl.md) — the matrix-free FE
  operator-application kernel-impl whose five-stage pipeline is typed over this family; defines the
  *behaviour* (the contraction composition). This page defines only the *shape*.
- [`build-time-vs-run-time-stratification`](./build-time-vs-run-time-stratification.md) — the stratum
  pattern (most of this family's axis extents are build-stratum).
- [semantic surface §1.2.3](../semantics/index.md) — the named-axes-of-fixed-meaning convention;
  §1.2.1 for the distinction from congruence shape groups (`(S: ...)` / `$S`).

**If this page and a consumer chapter / the L0 source disagree on any factual claim about the shape
family, the L0 source (the libCEED `CeedElemRestriction` / `CeedBasis` / build-QFunction construction
args) wins and this page is corrected.**

## Status

`firm` — the shape family is read directly off the positive libCEED tensor-layout construction args:
`E`/`L`/`C` from `CeedElemRestrictionCreate` (`palace/fem/libceed/restriction.cpp:200-203`), `L`/`P`/`C`
from `CeedBasisCreateTensorH1` (`palace/fem/libceed/basis.cpp:25-37`), `G = 2 + space_dim*dim` from the
build-QFunction `geom_data` output + its `MFEM_VERIFY` (`palace/fem/libceed/integrator.cpp:393-398`).
There is no claim beyond the data shape (the contraction algebra lives in the four consumer chapters),
so the firm bar is the data-shape analog of the firm-on-positive-structure escape — every axis is a
syntactic read-off of a positive construction arg, no test gates a shape definition. All L0 citations
self-verified against on-disk source this dispatch via codemap `read_range`. The record-definition
obligation is met: this is the cross-cutting home for the element-local rank-tensor family, referenced
by ≥2 consumers (all 4 substrate ops + `libceed-quadrature-kernel-impl`).

Well-foundedness (rank): the page is a `record` DAG node at `rank: firm`; its only blocking edges are
`cites-evidence depends-on` to the libCEED layout source (rank-terminal ground truth), so the
`rank(u) ≤ rank(v)` invariant holds vacuously. The edges to the consumer chapters are `reference`
(navigational — a record page is named-by-use; it does not block on its consumers). This page firming
un-caps the two D4 rough-in consumers (`element_restrict`, `geom_factor_build`) — their rough-in is
capped on this shape home, and they promote `rough-in → firm` once it is firm (the integrator's
cross-report rank-propagation; flagged for the finalize pass).
