---
agent: layer-intro-author
invoked_at: 2026-06-07T123000Z
scope: cycle-124 D5 — concepts/element-local-tensor record page + libceed-quadrature-kernel-impl promotion + L1/index substrate-cohort tally + semantics §1.2.3 element-local-axes
status: pending
integrated_at: 2026-06-07T112037Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-124 (batch-40 opener) D5. Applied clean. CREATED concepts/element-local-tensor.md FIRM (the shape-family record-definition home, closing D3's firm live-links + D4's rough-in bare-slug forward-refs) + promoted L1/libceed-quadrature-kernel-impl roadmap_goal->ROUGH-IN (realizes-kernel-api edges UNTOUCHED, DIRECTIVE-3 preserved) + new semantic 1.2.3 (USE+LINK) + SOLE-OWNED L1/index consolidated tally 43->45 firm + cohort header DRAINED. 1 OQ promoted (45->47 firm-flip follow-up). 2 ledger entries flagged resolved-by-landing for meta unify."
inputs:
  - reports/2026-06-07T112037Z-cycle-planner-c124/CYCLE.md (D5 entry + Overlap; D5 SOLE-OWNS the L1/index consolidated tally this wave)
  - reports/2026-06-07T112037Z-harvester-basis-apply-quad-contract/CYCLE.md (D3: basis_apply + quad_point_contract → firm; established [E,L]/[E,P,C]/[E,P,G] vocabulary; reference concepts/element-local-tensor)
  - reports/2026-06-07T112037Z-harvester-element-restrict-geom-factor/CYCLE.md (D4: element_restrict + geom_factor_build → rough-in; depends-on concepts/element-local-tensor shape home)
  - book/src/L1/libceed-quadrature-kernel-impl.md (the kernel-impl consumer to promote, roadmap_goal)
  - book/src/concepts/RefinementData.md (record-page format precedent)
  - book/src/semantics/index.md §1.2 (named shape groups — the semantic surface I own)
  - book/src/L1/index.md (the substrate-cohort tally I sole-own this wave)
  - L0 (codemap on-disk verified this dispatch): palace/fem/libceed/restriction.cpp:200-203, basis.cpp:25-37, integrator.cpp:393-398
---

# CYCLE: concepts/element-local-tensor record page + kernel-impl promotion + L1/index tally

## Summary

D5 lands the **data-shape home** for the libCEED element-local rank-tensor substrate cohort and
reconciles the cohort's graded-stack state:

1. **`concepts/element-local-tensor.md` — a new `record`-kind page** (rank `firm`) defining the
   `[E, L]` / `[E, P, C]` / `[E, P, G]` element-local rank-tensor **shape family**: the five named
   axes (element `E`, local-dofs-per-element `L`, quad-points `P`, value-components `C`,
   geometry-factor-components `G`), the construction-vs-run-time stratum of each, and the L0 home of
   the backing libCEED tensor layouts (`CeedElemRestrictionCreate` / `CeedBasisCreateTensorH1` /
   the `geom_data_size = 2 + space_dim*dim` build-QFunction output). The ≥2-consumer bar is fired
   (all 4 substrate ops + `libceed-quadrature-kernel-impl`). It defines the **data shape**; it does
   NOT restate the substrate ops' contraction algebra (that lives in `basis_apply` /
   `quad_point_contract` / `element_restrict` / `geom_factor_build`). It rests on positive libCEED
   layout source + the firm D3 ops, so it lands **firm** (the data-shape record analog of the
   firm-on-positive-structure escape — every axis is read directly off the libCEED `CeedElemRestriction`
   / `CeedBasis` construction args).

2. **`libceed-quadrature-kernel-impl` promoted `roadmap_goal` → `rough-in`** (NOT firm). Its 4
   `depends-on (composes)` constituents are now 2 firm (D3: `basis_apply`, `quad_point_contract`) +
   2 rough-in (D4: `element_restrict`, `geom_factor_build`). Per the §(h) well-foundedness cap
   `rank(impl) ≤ min over depends-on deps of rank(v)` = **rough-in** (the 2 rough-in D4 ops cap it).
   I note the coupling: it firms when `element_restrict` + `geom_factor_build` firm — which happens
   the moment THIS record page firms (D4's rough-in is capped on this shape home; my page lands firm,
   so the integrator's cross-report rank-propagation flips D4 firm, which un-caps the impl to firm).

3. **`semantics/index.md` §1.2.3 — a new sub-section** "Named axes of fixed meaning (the
   element-local family)" placing the `[E, L]` / `[E, P, C]` / `[E, P, G]` shapes in the surface's
   shape-semantics consolidation (§1.2), pointing at the record page as the authoritative axis-meaning
   home. USE+LINK: the surface states the *convention* (these are concrete named axes of fixed
   meaning, NOT congruence groups — the `Tensor[H, W, VY=3, VX=3]` precedent), the record page owns
   the axis *definitions*; the substrate ops keep only their own signatures.

4. **The L1/index substrate-cohort consolidated tally (I SOLE-OWN this wave).** The "Roadmap_goal
   (libCEED contraction substrate — 4)" cohort is now **fully drained**: all four ops left
   roadmap_goal this wave (2 firm via D3, 2 rough-in via D4). I rewrite the cohort header + the
   `libceed-quadrature-kernel-impl` roadmap_goal bullet (now rough-in) + the L1 firm grand-total bump
   (43 → **45**: +2 firm = D3's `basis_apply` + `quad_point_contract`; D4's two are rough-in, the
   kernel-impl is rough-in → not counted firm). D3/D4 emitted only their own rows + member bullets and
   deferred the cohort header + grand-total to me.

## Proposed changes

### (1) New record-definition page: `concepts/element-local-tensor.md`

```edit:book/src/concepts/element-local-tensor.md
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
```

### (2) Promote `libceed-quadrature-kernel-impl` roadmap_goal → rough-in

The promotion edits the frontmatter `rank:`, the leading comment, the `## Status` section, and the
`## Substrate L1 operators` section (the substrate is no longer all-roadmap_goal). The
`realizes-kernel-api` / `realizes-leaf` `reference` edges are UNCHANGED (DIRECTIVE-3 integrity).

```edit:book/src/L1/libceed-quadrature-kernel-impl.md
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
```

into:

```text
# Graded-stack scheme. This is a rough-in (rank 2) kernel-IMPL node (DIRECTIVE-3 item-2a):
# the constructive, in-our-tensor-algebra realization of the libCEED element-quadrature kernel
# that the firm `fe_assemble` fold (`K = Σ_i A(space, term_i)`) folds over opaquely as the leaf
# `A(space, term)`. Promoted roadmap_goal → rough-in (cycle-124 D5): its constructive constituents —
# the four element-local tensor-contraction substrate ops — became live L1 vocabulary this wave
# (`basis_apply` + `quad_point_contract` FIRM via c124 D3; `element_restrict` + `geom_factor_build`
# ROUGH-IN via c124 D4, capped on the `concepts/element-local-tensor` shape home, c124 D5). Per the
# well-foundedness cap `rank(impl) <= min over depends-on deps of rank(v)`: with two firm + two
# rough-in `composes` deps, min = rough-in, so this node CANNOT be firm — it lands rough-in. It firms
# when `element_restrict` + `geom_factor_build` firm, which happens the moment the
# `concepts/element-local-tensor` record page firms (their rough-in is capped on it, c124 D5 lands it
# firm). The `realizes-kernel-api` edge to the KEPT obstruction theme is `reference`-class
# (navigational/free — NOT depends-on; it does not block, does not constrain rank, does not carry
# liveness — it is a correspondence to be REVIEWED, audited by lowering-verifier). Pulled-by:
# `fe_assemble` (firm, the spine consumer whose opaque leaf this realizes) reaches the feature root
# via 7 feature-column inbound edges — so this node is reachable (not speculation-noise).
rank: rough-in
```

```edit:book/src/L1/libceed-quadrature-kernel-impl.md
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
```

into:

```text
## Status

`rough-in` (rank 2) — **kernel-impl** (the DIRECTIVE-3 role-label; this node is the constructive
realization, NOT the API surface). **Promoted roadmap_goal → rough-in (cycle-124 D5).** The operator
decomposition is well-understood and exhaustively anchored in the Palace libCEED source (see
*Evidence*), and its constructive constituents — the per-element / per-quadrature-point
tensor-contraction substrate — became **live L1 vocabulary this wave**: `basis_apply` +
`quad_point_contract` are now **firm** (c124 D3), and `element_restrict` + `geom_factor_build` are
**rough-in** (c124 D4), each resting on the `concepts/element-local-tensor` shape home (c124 D5). The
genuine vocabulary shift away from flat-vector BLAS (`Tensor[N]`) to the rank-structured element-local
tensors (`[E, L]` / `[E, P, C]` / `[E, P, G]`, `concepts/element-local-tensor`) is realized, so the
rank-0 disposition no longer holds.

**The rank is CAPPED at rough-in by well-foundedness** (CLAUDE.md §Methodology-invariants: an entry
is at most as resolved as its least-resolved dependency — the graded-stack `rank(u) ≤ rank(v)`
invariant): the four `depends-on
(composes)` substrate deps are 2 firm + 2 rough-in, so
`rank(impl) ≤ min over composes deps of rank(v) = rough-in`. This node **cannot be firm** while
`element_restrict` / `geom_factor_build` are rough-in — it lands rough-in. **Promotion route to firm:**
`element_restrict` + `geom_factor_build` firm the moment the `concepts/element-local-tensor` record
page firms (their rough-in is capped on that shape home, and c124 D5 lands it firm); once all four
substrate deps are firm, this node's `min(deps)` rises to firm and it promotes `rough-in → firm` on the
firm-on-positive-structure escape (its laws are syntactic-identity composition facts on the positively
read `AssembleCeedOperator` pipeline — no test gates them). **Blocking promotion condition:**
`element_restrict` + `geom_factor_build` must reach firm.
```

```edit:book/src/L1/libceed-quadrature-kernel-impl.md
## Substrate L1 operators (roadmap_goal, authored c122 D4; harvester promotion targets)

The four contraction-substrate operators are now rank-0 `roadmap_goal` chapters with
codemap-verified anchors (authored c122 D4), wired as this impl's `depends-on` substrate:

- [`element_restrict`](./element_restrict.md) — `G`/`Gᵀ`: the per-element gather/scatter
  `Tensor[(N: ...)] ↔ Tensor[(E, L)]`.
- [`basis_apply`](./basis_apply.md) — `B`/`Bᵀ`: the basis-eval contraction
  `Tensor[(E, L)] ↔ Tensor[(E, P, C)]`, keyed on the `EvalMode` the term's `𝒟` selects.
- [`quad_point_contract`](./quad_point_contract.md) — `D`: the pointwise per-quad-point
  `geom_data ⊙ ·` contraction (the embarrassingly-parallel lift).
- [`geom_factor_build`](./geom_factor_build.md) — the setup-stratum build-QFunction
  `(mesh-nodes, quad-weights) → geom_data`.

These four are the **shared tensor-contraction substrate** mined as a cohort (c122 D4) across the
element-local rank-structured tensor front; harvester promotes them `roadmap_goal → rough-in → firm`
when the element-local rank-tensor L1 vocabulary front lands, at which point this impl's
`depends-on` edges become firm-resting and the node itself can promote off `roadmap_goal`.
```

into:

```text
## Substrate L1 operators (c124 cohort: 2 firm + 2 rough-in)

The four contraction-substrate operators became live L1 vocabulary in the cycle-124 substrate-cohort
wave (D3 + D4 + D5), typed over the `concepts/element-local-tensor` shape family, wired as this impl's
`depends-on (composes)` substrate:

- [`element_restrict`](./element_restrict.md) — `G`/`Gᵀ`: the per-element gather/scatter
  `Tensor[(N: ...)] ↔ Tensor[(E, L)]`. **`rough-in`** (c124 D4; capped on the
  `concepts/element-local-tensor` shape home — firms when that record page firms).
- [`basis_apply`](./basis_apply.md) — `B`/`Bᵀ`: the basis-eval contraction
  `Tensor[(E, L)] ↔ Tensor[(E, P, C)]`, keyed on the `EvalMode` the term's `𝒟` selects. **`firm`**
  (c124 D3; firm-on-positive-structure).
- [`quad_point_contract`](./quad_point_contract.md) — `D`: the pointwise per-quad-point
  `geom_data ⊙ ·` contraction (the embarrassingly-parallel lift). **`firm`** (c124 D3;
  firm-on-positive-structure).
- [`geom_factor_build`](./geom_factor_build.md) — the setup-stratum build-QFunction
  `(mesh-nodes, quad-weights) → geom_data :: Tensor[(E, P, G)]`. **`rough-in`** (c124 D4; capped on
  the `concepts/element-local-tensor` shape home — firms when that record page firms).

The shared shape vocabulary these four are typed over is [`concepts/element-local-tensor`](../concepts/element-local-tensor.md)
(c124 D5, firm). With two firm + two rough-in substrate deps, this impl is capped at **rough-in** by
well-foundedness (`rank(impl) ≤ min(deps)`); it promotes `rough-in → firm` once `element_restrict` +
`geom_factor_build` firm (which happens when the `concepts/element-local-tensor` record page firms —
the rank-propagation flips them firm, lifting `min(deps)` to firm).
```

### (3) Semantic surface — new §1.2.3 (USE+LINK, not restate)

The element-local family is concrete named axes of fixed meaning (NOT congruence groups), so it lands
in §1.2 shape-semantics as a new sub-section §1.2.3 immediately after §1.2.2. It states the
*convention* and points at the record page for the *definitions* — it does NOT restate the per-axis
table (that lives on the record page) and does NOT restate the substrate ops' algebra.

```edit:book/src/semantics/index.md
This generalizes the rank-1 spelling `LinearOperator[M, N]` (where `M`, `N` are genuine flat dof-vector lengths) to the rank-agnostic case. At **L1/L0**, Palace operators act on flat dof-vectors and the concrete `LinearOperator[M, N]` / `Tensor[N]` rank-1 spelling is faithful — keep it there; the `LinOp[(R: ...), (D: ...)]` form is the L4/L3/L2 calculus rendering.

### 1.3 Terms
```

into:

```text
This generalizes the rank-1 spelling `LinearOperator[M, N]` (where `M`, `N` are genuine flat dof-vector lengths) to the rank-agnostic case. At **L1/L0**, Palace operators act on flat dof-vectors and the concrete `LinearOperator[M, N]` / `Tensor[N]` rank-1 spelling is faithful — keep it there; the `LinOp[(R: ...), (D: ...)]` form is the L4/L3/L2 calculus rendering.

#### 1.2.3 Named axes of fixed meaning (the element-local family)

Distinct from a **congruence shape group** (§1.2.1, `(S: ...)` / `$S` — a *name for an unknown-rank run* asserting two shapes agree) is a **concrete named axis of fixed meaning**: a single letter that denotes one specific, fixed quantity, the way `Tensor[H, W, VY=3, VX=3]` (§1.2) names a height, a width, and two pinned velocity axes. A concrete named axis is NOT rank-agnostic and is NOT a back-reference — it is one axis with a fixed semantic role.

The recurring concrete-named-axis family in this spec is the **element-local rank-tensor family** — the shape vocabulary of matrix-free FE operator application (the libCEED element-quadrature substrate). Its three shapes — `Tensor[(E, L)]`, `Tensor[(E, P, C)]`, `Tensor[(E, P, G)]` — are built from five fixed axes (`E` elements, `L` local-dofs-per-element, `P` quad-points, `C` value-components, `G` geometry-factor-components). The **authoritative definition home** for these axes (meaning, construction-vs-run-time stratum, the L0 libCEED layout each is read off) is the record page [`concepts/element-local-tensor`](../concepts/element-local-tensor.md) — this surface states only the *convention* (these are concrete named axes, not congruence groups), the record page owns the *definitions*, and the substrate operators (`basis_apply` / `quad_point_contract` / `element_restrict` / `geom_factor_build`) keep only their own signatures over the family. The flat global dof-axis `N` stays the genuine rank-1 `Tensor[(N: ...)]` (§1.2.1) and is NOT part of this family; the restriction `G` / `Gᵀ` is the boundary between the two.

### 1.3 Terms
```

### (4) L1/index consolidated substrate-cohort tally (D5 SOLE-OWNS this wave)

The "Roadmap_goal (libCEED contraction substrate — 4)" cohort is fully drained (all four left
roadmap_goal). I rewrite (a) the `libceed-quadrature-kernel-impl` roadmap_goal bullet → rough-in;
(b) the cohort header + close it out; (c) the firm grand-total bump (43 → 45). D3/D4's own member
bullets + table rows are applied by their reports; I own only the header + grand-total + the
kernel-impl bullet.

**(4a) the `libceed-quadrature-kernel-impl` bullet (line 99):**

```edit:book/src/L1/index.md
- **`libceed-quadrature-kernel-impl` is a `roadmap_goal` (kernel-impl)** *(cycle-121 D4)* — see [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md). The constructive, in-our-tensor-algebra realization of the per-term assembly leaf `A(space, term)` that [`fe_assemble`](./fe_assemble.md) folds over opaquely: the libCEED element-quadrature kernel as the contraction pipeline `A = Gᵀ B_𝒟ᵀ D(Q, geom) B_𝒟 G` (restriction-gather ▷ basis-eval ▷ pointwise geom×coeff×weight contraction ▷ basis-apply-transpose ▷ restriction-scatter). The DIRECTIVE-3 **kernel-impl** counterpart of the KEPT [`fe-assemble-libceed-boundary-obstruction`](../L1-L0/fe-assemble-libceed-boundary-obstruction.md) **kernel-api** surface, linked by a free `realizes-kernel-api` reference edge (NOT a `depends-on` — a reviewed correspondence, audited by `lowering-verifier`). **Rank-0 (roadmap_goal), NOT firm**, by the clean-gate: the per-element/per-quad-point tensor-contraction substrate (`element_restrict`/`basis_apply`/`quad_point_contract`/`geom_factor_build`) is a genuine vocabulary shift — our firm L1 algebra is flat-vector BLAS and does not carry the `[E, P, ...]` rank structure — so the honest disposition is a roadmap_goal carrying the constructive sketch + declaring the substrate it would rest on, NOT a firm claim. The obstruction theme STAYS the kernel-api surface (NOT downgraded). Promotes roadmap_goal→rough-in→firm once the substrate is mined (combinator-miner D6 of this cycle probes exactly this shared contraction core, shared with the D3 relaxation / D5 Krylov kernel-impls). Does NOT change the FE-assembly sub-spine firm count (still 4 firm).
```

into:

```text
- **`libceed-quadrature-kernel-impl` is now `rough-in` (kernel-impl)** *(cycle-121 D4 roadmap_goal → cycle-124 D5 rough-in)* — see [`libceed-quadrature-kernel-impl`](./libceed-quadrature-kernel-impl.md). The constructive, in-our-tensor-algebra realization of the per-term assembly leaf `A(space, term)` that [`fe_assemble`](./fe_assemble.md) folds over opaquely: the libCEED element-quadrature kernel as the contraction pipeline `A = Gᵀ B_𝒟ᵀ D(Q, geom) B_𝒟 G` (restriction-gather ▷ basis-eval ▷ pointwise geom×coeff×weight contraction ▷ basis-apply-transpose ▷ restriction-scatter). The DIRECTIVE-3 **kernel-impl** counterpart of the KEPT [`fe-assemble-libceed-boundary-obstruction`](../L1-L0/fe-assemble-libceed-boundary-obstruction.md) **kernel-api** surface, linked by a free `realizes-kernel-api` reference edge (NOT a `depends-on` — a reviewed correspondence, audited by `lowering-verifier`). **Promoted roadmap_goal → rough-in (cycle-124 D5):** the four substrate ops became live L1 vocabulary this wave (`basis_apply` + `quad_point_contract` FIRM c124 D3; `element_restrict` + `geom_factor_build` ROUGH-IN c124 D4), all typed over the firm [`concepts/element-local-tensor`](../concepts/element-local-tensor.md) shape family (c124 D5). The rank is **CAPPED at rough-in** by well-foundedness (`rank(impl) ≤ min over composes deps of rank(v)` = min(2 firm, 2 rough-in) = rough-in — it CANNOT be firm while two deps are rough-in); it promotes `rough-in → firm` once `element_restrict` + `geom_factor_build` firm (which happens when the `concepts/element-local-tensor` record page firms — the rank-propagation flips them firm, lifting `min(deps)`). The obstruction theme STAYS the kernel-api surface (NOT downgraded). Does NOT change the FE-assembly sub-spine firm count (still 4 firm).
```

**(4b) the substrate cohort header (line 101) — drained & closed:**

```edit:book/src/L1/index.md
**Roadmap_goal (libCEED contraction substrate — 4; opened cycle-122 D4)** — the four tensor-contraction substrate ops the `libceed-quadrature-kernel-impl` roadmap_goal (cycle-121 D4) declares as `depends-on` targets — the stages of the matrix-free FE operator-application pipeline `A = Gᵀ B_𝒟ᵀ D B_𝒟 G`. Authored as **rank-0 `roadmap_goal` chapters** (NOT firm/rough-in) by the clean-gate: each contracts over **rank-structured element-local / quad-point tensors** (`Tensor[(E, L)]` / `Tensor[(E, P, C)]`) that the firm flat-vector-BLAS L1 vocabulary (`Tensor[N]`) does **not** carry — a genuine vocabulary shift, not a re-expression in existing terms. Landing them roadmap_goal resolves 4 of the 6 `unresolved_depends_on_targets` to **LIVE links** with no false firm claim; the consumer `libceed-quadrature-kernel-impl` correctly STAYS roadmap_goal (well-foundedness: rank-0 ≤ rank-0). The decomposition is structurally exhaustive (read directly off `AssembleCeedOperator` + the build-QFunction); only the *existence of firm L1 substrate operators* is speculative. The four member bullets:
```

into:

```text
**libCEED contraction substrate (opened cycle-122 D4 roadmap_goal; DRAINED cycle-124 — 2 firm + 2 rough-in)** — the four tensor-contraction substrate ops that are the stages of the matrix-free FE operator-application pipeline `A = Gᵀ B_𝒟ᵀ D B_𝒟 G` (the `libceed-quadrature-kernel-impl` `depends-on (composes)` substrate). **The cycle-124 substrate-cohort wave (D3+D4+D5) firmed the element-local rank-tensor vocabulary shift** — the rank-structured element-local / quad-point tensors (`Tensor[(E, L)]` / `Tensor[(E, P, C)]` / `Tensor[(E, P, G)]`) the firm flat-vector-BLAS L1 (`Tensor[N]`) does not carry now have a firm data-shape home, [`concepts/element-local-tensor`](../concepts/element-local-tensor.md) (c124 D5). The four ops left roadmap_goal: `basis_apply` + `quad_point_contract` → **firm** (c124 D3, firm-on-positive-structure; the arithmetic basis-eval `B` and pointwise-diagonal `D` stages); `element_restrict` + `geom_factor_build` → **rough-in** (c124 D4; the gather/scatter `G` indexing + the geometry-factor build-pass, each `depends-on` the shape home and capped on its firmness — they firm when `concepts/element-local-tensor` firms, i.e. this cycle's record page). The consumer `libceed-quadrature-kernel-impl` promotes roadmap_goal → **rough-in** (capped by `min(deps)` = rough-in); it firms when the two D4 ops firm. The decomposition is structurally exhaustive (read directly off `AssembleCeedOperator` + the build-QFunction). This drains the cohort's 4 `unresolved_depends_on_targets`. The four member bullets (D3/D4 own their own; the maturity is read off each chapter's `## Status`):
```

**(4c) the firm grand-total bump (line 47, the §Vocabulary-cohort header).** D3 added 2 firm
(`basis_apply` + `quad_point_contract`); these are NOT main-cohort (they are the libCEED-substrate
sub-spine, like FE-assembly / FE-space / Mesh-construction). I introduce a "libCEED-substrate
sub-spine" sub-count and bump the grand total 43 → 45. The header sentence is amended at the
sub-spine enumeration:

```edit:book/src/L1/index.md
**Firm (33 main cohort; 43 firm grand total incl. the FE-assembly + FE-space + Mesh-construction sub-spines — cycle-117 wide wave landed three FE-construction firm operators: D3 `build_mesh` (new Mesh-construction sub-spine), D4 `fe_space_hierarchy` (FE-space sub-spine), D5 the de-Rham interpolator (FE-space sub-spine); the grand total is read off each chapter's on-disk `## Status`).**
```

into:

```text
**Firm (33 main cohort; 45 firm grand total incl. the FE-assembly + FE-space + Mesh-construction + libCEED-substrate sub-spines — cycle-124 substrate-cohort wave firmed two libCEED-substrate ops: D3 `basis_apply` + `quad_point_contract` (new libCEED-substrate sub-spine; the arithmetic `B` basis-eval + `D` pointwise-diagonal stages of the matrix-free FE operator-application pipeline, typed over the firm `concepts/element-local-tensor` shape family). The other two substrate ops (`element_restrict`, `geom_factor_build`) + the `libceed-quadrature-kernel-impl` consumer are rough-in this wave (capped on the shape home; firm-flip next cycle). The grand total is read off each chapter's on-disk `## Status`: 33 main + 4 FE-assembly + 5 FE-space + 1 Mesh-construction + 2 libCEED-substrate = 45.**
```

## Supporting evidence

- **L0 axis-layout citations, codemap on-disk verified this dispatch (`read_range`):**
  - `palace/fem/libceed/restriction.cpp:200-203` — `CeedElemRestrictionCreate(ceed, num_elem, P,
    fespace.GetVDim(), comp_stride, fespace.GetVDim()*fespace.GetNDofs(), …)` — confirmed the
    `(num_elem=E, P=L, vdim=C)` restriction layout args. CONFIRMED on-disk.
  - `palace/fem/libceed/basis.cpp:25-37` — `CeedBasisCreateTensorH1(ceed, dim, num_comp, P, Q,
    maps.Bt, maps.Gt, qX, qW, basis)` at `:35-37`, preceded by the `qW` weight-normalization loop
    `:25-33` — confirmed `num_comp=C`, libCEED `P`=nodes (spec `L`), libCEED `Q`=quad-points (spec
    `P`). CONFIRMED on-disk (the libCEED param-name inversion noted in the record page).
  - `palace/fem/libceed/integrator.cpp:393-398` — `CeedElemRestrictionGetNumComponents(geom_data_restr,
    &geom_data_size)` `:393-394`, `MFEM_VERIFY(geom_data_size == 2 + space_dim * dim, …)` `:395-396`,
    `CeedQFunctionAddOutput(build_qf, "geom_data", geom_data_size, CEED_EVAL_NONE)` `:397-398` —
    confirmed `G = 2 + space_dim*dim`. CONFIRMED on-disk.
- **Cohort context:** D3 (`basis_apply` + `quad_point_contract` firm; established the
  `[E,L]`/`[E,P,C]`/`[E,P,G]` vocabulary; references `concepts/element-local-tensor` by canonical slug)
  + D4 (`element_restrict` + `geom_factor_build` rough-in; `depends-on concepts/element-local-tensor`
  shape home). The record page's per-axis stratum + L0 bindings are consistent with both reports'
  signatures (verified the axis letters match: D3's `Tensor[(E, L)] → Tensor[(E, P, C)]`, D4's
  `Tensor[(N: ...)] ↔ Tensor[(E, L)]` and `→ Tensor[(E, P, G)]`).
- **Record-page format precedent:** `book/src/concepts/RefinementData.md` (c123) — the `kind: record`
  frontmatter + `cites-evidence depends-on` to L0 + `reference` to consumers + the
  "L0-source-wins-on-disagreement" footer.

## Open questions / caveats

- **D4's two rough-in ops firm-flip once this record page is verified-firm at integrate time
  (cross-report rank-propagation).** `element_restrict` + `geom_factor_build` are rough-in capped on
  `concepts/element-local-tensor`; this page lands firm, so by the §(h) well-foundedness rule their
  cap rises to firm and they promote `rough-in → firm`. Per the planner's note, the **integrator
  handles cross-report rank propagation** — I author the page firm and flag the coupling; I do NOT
  edit D4's two chapters (out of my dispatch's file scope, and D4 owns them). If the integrator does
  NOT auto-propagate, the clean follow-up is a same-cycle or c125 firm-flip of those two + a re-cap
  of `libceed-quadrature-kernel-impl` rough-in → firm (the impl's `min(deps)` rises to firm). Until
  then the rough-in state is correct and honest, NOT a failed promotion. **Consequence for the
  grand-total:** I bumped 43 → 45 (the 2 firm D3 ops only). When D4's two firm-flip + the impl
  firm-flips next, the grand total becomes 47 and the libCEED-substrate sub-spine count 2 → 4 — a c125
  tally follow-up (flagged, NOT done this wave since they are rough-in on-disk now).
- **`libceed-quadrature-kernel-impl` is rough-in, NOT firm — the §(h) cap, deliberate.** Even though
  D5's record page firms and D3's two ops are firm, the impl's two D4 `composes` deps are rough-in, so
  `min(deps) = rough-in` caps the impl at rough-in. This is the c123 krylov-iteration-column precedent
  (a composition-root over partial deps lands rough-in, not firm-on-positive-structure). The
  firm-on-positive-structure escape is orthogonal — it does NOT escape the well-foundedness cap. I
  recorded the blocking promotion condition (`element_restrict` + `geom_factor_build` must firm).
- **Semantic surface §1.2.3 is USE+LINK, not restate.** The new sub-section states the *convention*
  (concrete named axes vs congruence groups) and points at the record page for the per-axis
  *definitions*; it does NOT restate the axis table or the substrate ops' algebra. This is the
  semantic-consolidation discipline (the rule lives once on the surface; the record page owns the
  data-shape definitions; the op chapters keep only their own signatures). I verified the substrate
  ops (D3/D4) keep only their own signatures + a §1.2.1 link — no general-rule restatement to relocate
  this wave (D3/D4 already wrote thin "linked, not restated" pointers).
- **libCEED param-name inversion is a real naming hazard (flagged on the record page).** libCEED's
  `CeedBasisCreateTensorH1` names its nodes-per-element arg `P` and its quad-points arg `Q`, while the
  spec's element-local family uses `L` for local-dofs and `P` for quad-points. The record page's L0
  binding column states the inversion explicitly so a reader cross-checking the source is not misled.
  Not an error in D3/D4 (they use the spec letters consistently); a documentation note on the L0 home.
- **SUMMARY.md concepts-Part insertion (alpha position).** `concepts/element-local-tensor.md` inserts
  between `eigsolve` and `elementwise-product` (alpha). Proposed SUMMARY edit below.

```edit:book/src/SUMMARY.md
  - [eigsolve](./concepts/eigsolve.md)
  - [elementwise-product](./concepts/elementwise-product.md)
```

into:

```text
  - [eigsolve](./concepts/eigsolve.md)
  - [element-local-tensor — record definition](./concepts/element-local-tensor.md)
  - [elementwise-product](./concepts/elementwise-product.md)
```
