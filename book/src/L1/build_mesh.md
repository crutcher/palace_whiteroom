---
layer: L1
operator: build_mesh
harvested_by: harvester:2026-06-06T205239Z-harvester-build-mesh
cycle: cycle-117
# Graded-stack scheme. This firm L1 construction is a leaf at L1 (it consumes a `Config`/`IoData`
# surface and produces the `Mesh` typed value; no other L1 operator is invoked). It rests on its
# positive L0 ctor + build-referent source (cites-evidence, rank-terminal ground truth). The `Mesh`
# record is its produced output; `fe_space` (firm) consumes it (a consumed-by relation, NOT a dep of
# build_mesh). Well-foundedness rank(u) <= rank(v): this node firm (rank 3); the only edges are
# cites-evidence to rank-terminal L0 source. The L1>L0 mutation-rotation theme is named-not-authored
# (forthcoming), so no `lowers-to` edge is asserted yet (would point at a not-yet-firm node).
rank: firm
edges:
  depends-on:
    - target: palace/fem/mesh.hpp:44-115
      kind: cites-evidence        # the `class Mesh` wrapper (ctor chain :72-81, single-machine surface :84-96, libCEED attr map :96-115)
    - target: palace/main.cpp:286-301
      kind: cites-evidence        # the build referent: Load -> Preprocess -> Partition -> RefineMesh -> wrap
  reference:
    - L1/fe_space                  # the primary consumer of the constructed Mesh (fe_space takes `mesh: Mesh`)
    - feature/lifecycle.L1         # the composition root that forward-references `build_mesh :: Config -> Mesh`
---

# `build_mesh` — single-machine mesh construction

`build_mesh :: Config -> Mesh`

Construct the **discretised computational domain** `Mesh` — the geometric substrate every assembled-operator
pipeline stands on — from the input `Config`. The construction is the serial-stage pipeline
**load → preprocess → partition → a-priori-refine**: read the serial mesh from disk and perform all
serial-stage preparation (including the box/sphere **region refinement** of the serial mesh), apply
problem-type-specific preprocessing, partition (single-rank: the identity distribution, see *Scope*), then
apply the a-priori parallel **uniform** refinement requested by the config.
The result is the Palace `Mesh` wrapper — an `mfem::ParMesh` read single-rank, augmented with the libCEED
local-attribute mapping — consumed read-only thereafter by [`fe_space`](./fe_space.md) (which takes
`mesh: Mesh`) and, through it, by the whole assembled-operator front. `build_mesh` is the
[`lifecycle`](../feature/lifecycle.L1.md) composition root's stage (1).

## Context

L1 is the mutation-rotation layer: source operations re-expressed as pure functions. `build_mesh` is the
**domain-construction** view of that rotation — at L0 the mesh is loaded, preprocessed, partitioned, and
refined by a sequence of free functions that mutate (or consume-and-return) `unique_ptr` mesh handles
in place; the L1 form names the pure `config → mesh` pipeline and treats the constructed `Mesh` as an
immutable typed value.

At L0 the build referent is the mesh block of `main` (`palace/main.cpp:286-301`): a serial mesh is loaded
and serial-stage-prepared by `mesh::Load` (`palace/main.cpp:287`), the solver applies problem-type-specific
serial preprocessing via `solver->Preprocess` (`:288`), `mesh::Partition` partitions/distributes the prepared
serial mesh into a parallel mesh (`:290`), `mesh::RefineMesh` applies a-priori uniform refinement producing
the level-mesh sequence (`:291`), and each resulting `mfem::ParMesh` is wrapped into a Palace `Mesh`
(`:299`). The four `mesh::` stages are declared in `palace/utils/geodata.hpp:25-50`; their bodies live in
`palace/utils/geodata.cpp` (`Load` `:122`, `RefineMesh` `:421`).

This chapter is defined in L1 vocabulary (the typed `config → Mesh` construction pipeline). The forward
rewrite into the L0 free-function chain + the in-place `unique_ptr` mesh-handle mutation is the L1>L0
`build-mesh-construction-rotation` theme (named, NOT authored this cycle — see *Status*).

## Signature

    build_mesh :: Config -> Mesh

Shape contract (bunsen-style, named axes):

- `config` — `Config` — the `IoData` configuration surface (the same read-only record the
  [`lifecycle`](../feature/lifecycle.L1.md) root and every per-driver column consume; cross-referenced to
  [`config-record`](../concepts/config-record.md)). The mesh-relevant fields are `model.mesh` (the mesh
  file), `model.remove_curvature`, the region/box/sphere refinement config, and
  `model.refinement.uniform_ref_levels` (the a-priori refinement depth). Read-only.
- result — `Mesh` — the Palace mesh wrapper (see *Record definition*): a single-rank `mfem::ParMesh`
  augmented with the libCEED local-attribute mapping. The result carries the geometric axes the FE-space
  construction reads — `Dimension`, `SpaceDimension`, element count `GetNE`, boundary-element count
  `GetNBE` (`palace/fem/mesh.hpp:93-96`).

The `Mesh` is the load-bearing output: it is the very `mesh: Mesh` that [`fe_space`](./fe_space.md)
pairs with an `FECollection` to define the true-dof axis `N` that the whole vocabulary is indexed by.
(No `Tensor[...]` shape group appears in this signature — `build_mesh` consumes config and produces a
typed geometric object, not a tensor; the named-shape-group notation governs tensor-valued signatures, see
[semantics §1.2.1](../semantics/index.md).)

## Record definition

`Mesh` is the Palace wrapper for MFEM's `ParMesh` class, with extensions for Palace
(`palace/fem/mesh.hpp:44`). It is the produced output of `build_mesh` and the consumed input of
[`fe_space`](./fe_space.md). Single-consumer-judgment: `Mesh` is consumed by ≥2 chapters (every driver
column's mesh stage + `fe_space` + the deferred `fe_space_hierarchy`), so per the record-definition
obligation it warrants a shared `concepts/mesh.md` page — **flagged in Open questions**
(`record-Mesh-needs-definition-home`). This in-chapter section is the interim definition home until that
page lands (it is the chapter that *produces* the record).

| field | type | meaning | stratum |
|---|---|---|---|
| `mesh` | `unique_ptr<mfem::ParMesh>` (single-rank) | the underlying MFEM mesh object; can also point to a derived `mfem::ParSubMesh` (`palace/fem/mesh.hpp:47-49`) | construction-time (owns the loaded/partitioned/refined mesh) |
| `loc_attr` | `unordered_map<int,int>` | global (MFEM, 1-based) **domain** attribute → process-local contiguous (1-based) libCEED attribute (`palace/fem/mesh.hpp:51-58`) | construction-time (built by `Update`); single-rank = identity-flavoured remap (see *Scope*) |
| `loc_bdr_attr` | `unordered_map<int, unordered_map<int,int>>` | global **boundary** attribute → (neighbouring domain attr → local boundary attr) — discriminates boundary elements bordering more than one domain (`palace/fem/mesh.hpp:51-59`) | construction-time |
| `ceed_from_self` | `bool` | true after `RebuildCeedAttributes()` (`palace/fem/mesh.hpp:60`) | run-time flag |
| `geom_data` | `mutable ceed::CeedObjectMap<ceed::CeedGeomFactorData>` | cached libCEED geometry-factor quadrature data (`w·|J|`, `adj(J)^T/|J|`) per element-geometry/thread (`palace/fem/mesh.hpp:62-69`) | run-time (transparent cache, re-derivable on demand — a performance store, NOT lifted structure) |

The backing C++ struct is `class Mesh` (`palace/fem/mesh.hpp:44`). It is constructed by either the variadic
ctor that builds the `mfem::ParMesh` from forwarded args (`palace/fem/mesh.hpp:72-75`) or, the form `main`
uses, the `unique_ptr`-adopting ctor `Mesh(std::unique_ptr<T> &&mesh)` (`:76-81`) which runs
`EnsureNodes()` + `Update()` (`:79-80`) to finalize the geometry and build the attribute maps. The
single-machine read surface is `Get()` / `Dimension()` / `SpaceDimension()` / `GetNE()` / `GetNBE()`
(`palace/fem/mesh.hpp:84-96`); the libCEED attribute-map accessors are `GetCeedAttributes` /
`GetCeedBdrAttributes` (`:96-115`). The config-relevant `IoData` surface this record mirrors is
`model.mesh` + `model.refinement` (cross-ref [`config-record`](../concepts/config-record.md)).

## Algebraic laws

The laws are syntactic identities on the positive construction pipeline (no convergence / iteration
semantics — refinement *depth* is a fixed config field, not an adaptively-driven loop; the adaptive
estimate-mark-refine loop is the [`lifecycle`](../feature/lifecycle.L1.md) root's outer fold, NOT
`build_mesh`):

1. **Config determinism.** `build_mesh` is a pure function of `config` — the same config (same mesh file,
   same `remove_curvature`, same refinement settings) produces the same `Mesh` (the same geometry, the same
   `Dimension`/`SpaceDimension`/`GetNE`/`GetNBE`, the same attribute maps). The serial load + serial-stage
   prep is deterministic given the file (`palace/utils/geodata.cpp:122-143`).
2. **Pipeline staging (load ▷ preprocess ▷ partition ▷ refine).** The construction is the ordered
   composition of the four `mesh::` stages — `Load` then `Preprocess` then `Partition` then `RefineMesh`
   (`palace/main.cpp:287-291`) — each consuming the prior stage's mesh handle. The order is load-bearing
   (partition consumes a *prepared serial* mesh; refine consumes a *partitioned* mesh) and is NOT a
   commuting family.
3. **Zero-refinement identity.** With `uniform_ref_levels == 0`, `RefineMesh` produces the single
   partitioned mesh unchanged (`palace/utils/geodata.cpp:421-430`: the level-vector keeps its single entry;
   the refinement loop `for (l = 0; l < uniform_ref_levels; l++)` does not execute, `:448`). `RefineMesh`
   performs **parallel uniform refinement only** — box/sphere **region** refinement happens earlier, in the
   `Load`/serial-prep stage on the serial mesh (`palace/utils/geodata.hpp:25-31,45-46`; the in-body comment
   `palace/utils/geodata.cpp:423`), so the parallel refinement stage is the identity on the partitioned mesh
   independently of the region-refinement config.
4. **Refinement-level monotonicity (a-priori only).** With `uniform_ref_levels = k`, `RefineMesh` produces
   the ordered level-mesh sequence of increasing refinement (`palace/utils/geodata.hpp:47-49`: "stored in
   order of increased refinement"); the coarse mesh is the head, the finest the tail. This is *a-priori*
   refinement read from config — it is the geometric-multigrid level stack, NOT the adaptive AMR loop (the
   `lifecycle` root's fold owns that; see *Non-laws*).

**Non-laws (read-as-given / out-of-scope, do NOT constrain `build_mesh`):**

- **Partition / distribution semantics.** Single-rank (see *Scope*): `mesh::Partition` is read as the
  identity distribution; the multi-rank partition policy (`mfem::MeshPartitioner` vs byte-string broadcast,
  `palace/utils/geodata.cpp:131-143`) is out of scope. No L1 law constrains partition placement.
- **MFEM-opaque adaptive mesh refinement.** The adaptive (error-estimator-driven) refinement is NOT part of
  `build_mesh` — it is the `lifecycle` root's outer estimate-mark-refine fold (the per-element non-conformal
  AMR machinery, `mfem::Mesh::GeneralRefinement`, is MFEM-opaque). `build_mesh` performs only the
  **a-priori** (config-fixed uniform/region) refinement; the adaptive loop stays obstruction-documented at
  the lifecycle root, not forced into a firm claim here.
- **libCEED geometry-factor cache.** `geom_data` is a transparent performance store (re-derivable on
  demand); no L1 law constrains it (the `fe_space` libCEED-cache precedent,
  `book/src/L0/fespace-file.md:159-164`).

## Dependencies

(leaf at L1 — the construction takes a `Config`/`IoData` surface and produces a typed `Mesh` value; no
other L1 operator is invoked.) The result is consumed by [`fe_space`](./fe_space.md) (which pairs the
`Mesh` with an `FECollection`) and is stage (1) of the [`lifecycle`](../feature/lifecycle.L1.md)
composition root — those are consumed-by relations, NOT dependencies.

## Scope (single-machine — flag-once-skip)

Per CLAUDE.md §Scope (single-machine target; MPI / `Par*` out of scope):

- **`mesh::Partition` / distribution → single-rank.** The partition/distribute stage (`palace/main.cpp:290`,
  `palace/utils/geodata.hpp:33-36`) is read as the **identity distribution**: on a single rank the prepared
  serial mesh becomes the (single-rank) parallel mesh with no inter-process partitioning. The
  conformality-driven distribution-path branch (`use_mesh_partitioner`,
  `palace/utils/geodata.cpp:134,140-143`) and the `MeshPartitioner`-vs-byte-string-broadcast policy are
  multi-rank machinery — **flagged once and skipped**.
- **`mfem::ParMesh` / `loc_attr` / `loc_bdr_attr` per-process attribute remap → single-rank.** The wrapped
  `mfem::ParMesh` is read single-rank (the standing `par-types-single-rank-reading` rule); the
  global→process-local libCEED attribute remap (`palace/fem/mesh.hpp:51-59`) collapses to a single-process
  contiguous relabeling on one rank. The `Mesh` record carries these maps (above) but the L1 form does not
  define the multi-rank remap semantics.

These two are the **only** single-machine carve-outs; the load / serial-prep / a-priori-refine stages are
in scope and lifted here.

## Downward (to L0)

The L1>L0 rotation `build-mesh-construction-rotation` (named, NOT authored this cycle) will narrate how the
typed `config → Mesh` construction rewrites into the L0 free-function chain `mesh::Load` ▷
`solver->Preprocess` ▷ `mesh::Partition` ▷ `mesh::RefineMesh` ▷ `make_unique<Mesh>` (`palace/main.cpp:287-299`),
including the in-place `unique_ptr` mesh-handle mutation (the level-vector grown in place by `RefineMesh`,
`palace/utils/geodata.cpp:421-450`) and the construction-time `EnsureNodes()` + `Update()` finalization
(`palace/fem/mesh.hpp:79-80`). No `lowers-to` edge is asserted in this chapter's front-matter yet (it would
point at a not-yet-authored node); the theme is flagged in Open questions.

## Status

**firm (firm-on-positive-structure).** The construction is read directly from positive source: the `Mesh`
ctor chain (`palace/fem/mesh.hpp:72-81`), the single-machine read surface (`:84-96`), and the build referent
(`palace/main.cpp:286-301`) → the four `mesh::` stage declarations (`palace/utils/geodata.hpp:25-50`) +
bodies (`palace/utils/geodata.cpp:122`, `:421`). Every law is a syntactic identity on this positive
structure (construction determinism, pipeline staging, zero-refinement identity, a-priori
level-monotonicity) — there is no convergence/iteration semantics to test-gate (the a-priori refinement
*depth* is a fixed config field, not an adaptively-driven loop), so the absence of a dedicated
mesh-construction unit test does not gate firm (the `fe_space` cycle-064 / `fe_assemble` cycle-054 /
`apply_linop` no-dedicated-test precedent).

This is the **geometric substrate under all five solver pipelines** — the highest-fan-out entry of the
mesh-wrapper front (every driver column's mesh stage and the FE-space sub-spine, via `fe_space`'s
`mesh: Mesh` input, stand on it).

**Single-machine scope (flagged):** the partition/distribute stage and the `ParMesh`/`loc_attr` per-process
attribute remap are read as single-rank equivalents (see *Scope*); MFEM-opaque adaptive mesh refinement is
left to the `lifecycle` root's outer fold (obstruction-documented there), NOT forced to a firm claim here.

**`Mesh` record home:** an in-chapter `## Record definition` section is authored above (interim home); a
shared `concepts/mesh.md` page is flagged (`record-Mesh-needs-definition-home`) since `Mesh` has ≥2
consumers.

**Deferred follow-on (named, NOT authored this cycle):** the L1>L0
`build-mesh-construction-rotation` theme; the `concepts/mesh.md` record page; and (downstream) the
mesh-refinement / `fe_space_hierarchy` h-refinement coupling (the a-priori level sequence is the
geometric-multigrid stack `fe_space_hierarchy` consumes).

## Evidence

- `palace/fem/mesh.hpp:44-115` — the `class Mesh` wrapper: `class Mesh` (`:44`), the underlying
  `unique_ptr<mfem::ParMesh> mesh` (`:49`), the `loc_attr`/`loc_bdr_attr` libCEED attribute maps
  (`:51-59`), the variadic ctor (`:72-75`) and the `unique_ptr`-adopting ctor with `EnsureNodes()`+`Update()`
  (`:76-81`), the single-machine read surface `Get`/`Dimension`/`SpaceDimension`/`GetNE`/`GetNBE`
  (`:84-96`), and the libCEED attribute-map accessors (`:96-115`).
- `palace/main.cpp:286-301` — the build referent (the mesh block of `main`): `mesh::Load` (`:287`),
  `solver->Preprocess` (`:288`), `mesh::Partition` (`:290`), `mesh::RefineMesh` (`:291`), and the
  `make_unique<Mesh>(std::move(m))` wrap (`:299`). The driver-agnostic mesh-build scaffold the
  `lifecycle.L1` root cites (`book/src/feature/lifecycle.L1.md:44`).
- `palace/utils/geodata.hpp:25-50` — the four `mesh::` stage declarations + contracts: `Load`
  (load + serial-stage prep, `:25-31`), `Partition` (partition/distribute, `:33-36`), `RefineMesh`
  (parallel uniform a-priori refinement, ordered level meshes, `:45-50`).
- `palace/utils/geodata.cpp:122-143` — `Load` body: serial load + the conformality-driven
  distribution-path branch (`use_mesh_partitioner`, `:134,140-143` — multi-rank, out of scope).
- `palace/utils/geodata.cpp:421-450` — `RefineMesh` body: the single-mesh-in precondition (`:424-425`),
  `uniform_ref_levels` read (`:426`), the level-reserve (`:427-430`), and the a-priori refinement loop
  `for (l = 0; l < uniform_ref_levels; l++)` (`:448`) — the zero-refinement-identity + level-monotonicity
  law substrate.
- `book/src/feature/lifecycle.L1.md:37,44` — the composition root's forward-reference
  `build_mesh :: Config -> Mesh` (`:37`) + stage-(1) constituent narration (`:44`).
- `book/src/L1/fe_space.md:33,71-73` — `fe_space`'s `mesh: Mesh` input (the primary consumer of the
  constructed `Mesh`).
