---
rank: firm
kind: record
edges:
  depends-on:
    - target: palace/fem/mesh.hpp:44-115
      kind: cites-evidence
  reference:
    - L1/build_mesh
    - L1/fe_space
    - L1/fe_space_hierarchy
    - feature/lifecycle.L1
    - concepts/config-record
    - concepts/build-time-vs-run-time-stratification
---

# Mesh

> **Kind: `record`.** This page defines the *data shape* of `Mesh` — its fields, their
> types and meaning, the construction-vs-run-time stratum of each, and the L0 source home
> the backing C++ struct mirrors. The *behaviour* — how [`build_mesh`](../L1/build_mesh.md)
> constructs it and how [`fe_space`](../L1/fe_space.md) / [`fe_space_hierarchy`](../L1/fe_space_hierarchy.md)
> consume it — lives in those operator chapters; this page does not restate that algebra.

`Mesh` is the Palace **wrapper for the discretised computational domain** — the geometric
substrate every assembled-operator pipeline stands on. It owns a single-rank `mfem::ParMesh`
(read single-rank per the standing `par-types-single-rank-reading` rule; MPI/`Par*`/partitioning
out of scope) augmented with the libCEED local-attribute mapping needed to assemble libCEED
operators over the mesh. It is **produced** by [`build_mesh`](../L1/build_mesh.md)
(`build_mesh :: Config -> Mesh`) and **consumed** by [`fe_space`](../L1/fe_space.md)
(`mesh: Mesh` input), [`fe_space_hierarchy`](../L1/fe_space_hierarchy.md) (`[Mesh]` element
type), and the [`lifecycle`](../feature/lifecycle.L1.md) composition root's stage-(1). Four
distinct consumers put it above the ≥2-consumer bar, so it has a cross-cutting definition home
here rather than only an in-chapter section in its producing chapter.

## One-line semantics

`Mesh` is an immutable typed geometric value — a single-rank `mfem::ParMesh` plus the libCEED
attribute maps — over which the FE-space construction reads the geometric axes (`Dimension`,
`SpaceDimension`, element count `GetNE`, boundary-element count `GetNBE`). It carries no algebra
of its own; the constructor and the FE-space ops supply all behaviour.

## Record definition

`Mesh` is the backing C++ `class Mesh` (`palace/fem/mesh.hpp:44`). The TS brace form (the value
is immutable once constructed; per-field strata below):

```text
Mesh = {
  mesh          : unique_ptr<mfem::ParMesh>,   -- the underlying MFEM mesh (single-rank)
  loc_attr      : Map<int, int>,               -- global domain attr -> local libCEED attr
  loc_bdr_attr  : Map<int, Map<int, int>>,     -- global bdr attr -> (neighbour domain attr -> local bdr attr)
  ceed_from_self: bool,                         -- true after RebuildCeedAttributes()
  geom_data     : CeedObjectMap<CeedGeomFactorData>  -- cached libCEED geometry factors (transparent)
}
```

| field | type | meaning | stratum | L0 source |
|---|---|---|---|---|
| `mesh` | `unique_ptr<mfem::ParMesh>` (single-rank) | the underlying MFEM mesh object; can also point to a derived `mfem::ParSubMesh` (boundary-mode submesh extraction) | construction-time (owns the loaded/partitioned/refined mesh) | `palace/fem/mesh.hpp:47-49` |
| `loc_attr` | `unordered_map<int,int>` | global (MFEM, 1-based) **domain** attribute → process-local contiguous (1-based) libCEED attribute | construction-time (built by `Update()`; single-rank = identity-flavoured remap) | `palace/fem/mesh.hpp:51-58` |
| `loc_bdr_attr` | `unordered_map<int, unordered_map<int,int>>` | global **boundary** attribute → (neighbouring domain attr → local boundary attr) — discriminates boundary elements bordering more than one domain | construction-time | `palace/fem/mesh.hpp:51-59` |
| `ceed_from_self` | `bool` | true after `RebuildCeedAttributes()` | run-time flag | `palace/fem/mesh.hpp:60` |
| `geom_data` | `mutable ceed::CeedObjectMap<ceed::CeedGeomFactorData>` | cached libCEED geometry-factor quadrature data (`w·|J|`, `adj(J)^T/|J|`) per element-geometry/thread | run-time (transparent cache, re-derivable on demand — a performance store, NOT lifted structure) | `palace/fem/mesh.hpp:62-69` |

The single-machine **read surface** (read-as-given accessors, NOT operations): `Get()` /
`Dimension()` / `SpaceDimension()` / `GetNE()` / `GetNBE()` (`palace/fem/mesh.hpp:84-96`); the
libCEED attribute-map accessors `GetCeedAttributes` / `GetCeedBdrAttributes`
(`palace/fem/mesh.hpp:96-115`). These expose the geometric axes the FE-space construction reads
(`fe_space`'s `mesh: Mesh` input pairs `Dimension`/`SpaceDimension`/`GetNE`/`GetNBE` with an
`FECollection` to define the true-dof axis `N`).

## Stratum — construction-time, immutable-once-built

`Mesh` is **construction-stratum**: it is built once at the start of every solver pipeline (the
lifecycle stage-(1) mesh block) and consumed read-only thereafter — there is no per-iteration
solve-time mutation of the geometric value (the adaptive estimate-mark-refine loop produces a
*new* `Mesh` per AMR iterate at the lifecycle root, it does not mutate an existing one). The
construction-vs-run-time split per field (above) is the
[`build-time-vs-run-time-stratification`](./build-time-vs-run-time-stratification.md) pattern:
`mesh` / `loc_attr` / `loc_bdr_attr` are built-at-construction scaffolding; `geom_data` is a
run-time transparent cache (a performance store, re-derivable, NOT lifted structure — the
`fe_space` libCEED-cache precedent).

Concretely in Palace: the `unique_ptr`-adopting ctor `Mesh(std::unique_ptr<T> &&mesh)`
(`palace/fem/mesh.hpp:76-81`) runs `EnsureNodes()` (`:79`, geometry finalization) + `Update()`
(`:80`, builds the `loc_attr` / `loc_bdr_attr` libCEED maps) at construction; the variadic ctor
(`:72-75`) builds the `mfem::ParMesh` from forwarded args then delegates to the adopting ctor.
The construction finalization (`EnsureNodes()` + `Update()`) is the L1>L0
[`build-mesh-construction-rotation`](../L1-L0/build-mesh-construction-rotation.md) theme's Piece-3.

## L0 source home — the `class Mesh` wrapper

The backing C++ struct is `class Mesh` (`palace/fem/mesh.hpp:44`). Its construction lifecycle
across the L0 surface (the mesh block of `main`, `palace/main.cpp:286-301`): `mesh::Load` →
`solver->Preprocess` → `mesh::Partition` (read single-rank) → `mesh::RefineMesh` →
`make_unique<Mesh>(std::move(m))` (the adopting ctor). The config-relevant `IoData` surface this
record mirrors is `model.mesh` (the mesh file) + `model.refinement` (the a-priori refinement
config), part of `config::ModelData` — cross-ref [`config-record`](./config-record.md)
(`model : config::ModelData`, `iodata.hpp:32`, struct `configfile.hpp:156`).

**Single-machine carve-outs (flagged once).** The `mfem::ParMesh` is read single-rank; the
global→process-local libCEED attribute remap (`loc_attr` / `loc_bdr_attr`) collapses to a
single-process contiguous relabeling on one rank. The `mesh::Partition` distribution stage is
the identity distribution; the multi-rank partition policy is out of scope. This record carries
the maps but does not define the multi-rank remap semantics (per CLAUDE.md §Scope).

## Signatures that name this record

The ≥2-consumer evidence for the standalone page (four consumers):

- [`build_mesh`](../L1/build_mesh.md) — the **producer**: `build_mesh :: Config -> Mesh`
  (`book/src/L1/build_mesh.md:27,62`).
- [`fe_space`](../L1/fe_space.md) — the primary consumer; its `mesh: Mesh` parameter
  (`fe_space :: (mesh: Mesh, collection: FECollection) -> FiniteElementSpace[N]`,
  `book/src/L1/fe_space.md:33,68,72`).
- [`fe_space_hierarchy`](../L1/fe_space_hierarchy.md) — the `[Mesh]` coarse-to-fine input list
  element type (`fe_space_hierarchy :: [Mesh] -> [FECollection] -> Config ->
  FiniteElementSpaceHierarchy`, `book/src/L1/fe_space_hierarchy.md:33,89-93`).
- [`lifecycle.L1`](../feature/lifecycle.L1.md) — the composition root's stage-(1) build_mesh
  output threaded through the whole pipeline + the AMR fold (`book/src/feature/lifecycle.L1.md:39,44`).

## See also

- [`build_mesh`](../L1/build_mesh.md) — the producer; defines HOW the mesh is constructed
  (load → preprocess → partition → a-priori-refine). This page defines only the *shape* of its
  output.
- [`build-mesh-construction-rotation`](../L1-L0/build-mesh-construction-rotation.md) — the L1>L0
  theme; the construction finalization (`EnsureNodes()` + `Update()` building this record's
  attribute maps) is its Piece-3.
- [`fe_space`](../L1/fe_space.md) / [`fe_space_hierarchy`](../L1/fe_space_hierarchy.md) — the
  consumers; define the *behaviour over* the mesh (pairing it with an `FECollection` to build the
  space). This page does NOT restate that algebra.
- [`config-record`](./config-record.md) — the `IoData` surface (`model.mesh` + `model.refinement`)
  this record's construction reads from.
- [`build-time-vs-run-time-stratification`](./build-time-vs-run-time-stratification.md) — the
  per-field construction-vs-run-time split (`mesh`/`loc_attr`/`loc_bdr_attr` build-time;
  `geom_data` run-time cache).

**If this page and a consumer chapter / the L0 source disagree on any factual claim about the
record, the L0 source (`palace/fem/mesh.hpp`) wins and this page is corrected.**
