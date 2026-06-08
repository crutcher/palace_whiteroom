# File — `palace/fem/fespace.{hpp,cpp}`

A reference note for the **FE-space wrapper + space-hierarchy** file — the input substrate every
solver's assembly consumes. Per the `FiniteElementSpace` class header comment
(`palace/fem/fespace.hpp:18-20`): *"Wrapper for MFEM's ParFiniteElementSpace class, with extensions
for Palace."* The file holds two classes in `namespace palace` (`fespace.hpp:15`): the
`FiniteElementSpace` wrapper (`fespace.hpp:21-194`) and the `FiniteElementSpaceHierarchy` collection
(`fespace.hpp:200-286`, header comment `fespace.hpp:196-198`: *"A collection of FiniteElementSpace
objects constructed on the same mesh with the ability to construct the prolongation operators between
them as needed."*).

It is **in scope** under the mesh / FE-space-construction directive (`CLAUDE.md` §Scope). Per the
single-rank reading rule ([`par-types-single-rank-reading`](./par-types-single-rank-reading.md)), the
wrapped `mfem::ParFiniteElementSpace` (`fespace.hpp:24`) is read as a serial `FiniteElementSpace`; the
libCEED objects (`Ceed`, `CeedBasis`, `CeedElemRestriction`) and the MPI communicator accessor
(`GetComm`, `fespace.hpp:186`) are read single-rank / single-`Ceed`.

**Framing — this file wraps MFEM dof structure; it does not redefine it.** dof/vdof numbering,
byNODES/byVDIM ordering, element-to-dof tables, conformity, and the prolongation/restriction matrices
are **MFEM's** (`mfem::ParFiniteElementSpace`); Palace surfaces them through thin forwarding
accessors that all `return Get().X()` (`fespace.hpp:93-103`). What this file *adds* on top of MFEM —
and what this chapter anchors — is (i) the **libCEED operator-construction substrate** (per-`Ceed`,
per-geometry lazy basis / element-restriction caches) and (ii) the **inter-space / inter-level
transfer operators** (discrete gradient/curl/divergence interpolators; hierarchy prolongation). The
MFEM dof internals are read as-is per the single-rank rule and not re-anchored here.

## At a glance

*The wrapper class, the hierarchy, and the MFEM-forwarding surface.*

- **`FiniteElementSpace`** (`fespace.hpp:21-194`) — wraps a `mfem::ParFiniteElementSpace fespace`
  (`fespace.hpp:24`) plus a non-owned `Mesh &mesh` (`fespace.hpp:27`). Holds the Palace-specific
  libCEED caches: `ceed::CeedObjectMap<CeedBasis> basis` and three
  `CeedObjectMap<CeedElemRestriction> restr, interp_restr, interp_range_restr`
  (`fespace.hpp:30-32`); mutable workspace `ComplexVector tx, lx, ly` (`fespace.hpp:35`); and the
  lazy discrete-interpolator state `const FiniteElementSpace *aux_fespace` + `unique_ptr<Operator> G`
  (`fespace.hpp:37-39`). The variadic constructor (`fespace.hpp:67-75`) forwards its arguments
  straight into the `mfem::ParFiniteElementSpace` constructor (`&mesh.Get(), forward<T>(args)...`),
  then `ResetCeedObjects()` + marks `tx/lx/ly` device-resident.
- **MFEM-forwarding accessor surface** (`fespace.hpp:77-103`) — thin `return Get().X()` forwarders:
  `Get()` (the underlying `mfem::ParFiniteElementSpace`), `GetFEColl`, `GetMesh`/`GetParMesh`,
  `GetVDim`/`GetVSize`/`GlobalVSize`/`GetTrueVSize`/`GlobalTrueVSize` (dof counts),
  `Dimension`/`SpaceDimension`/`GetMaxElementOrder`, and crucially
  **`GetProlongationMatrix`/`GetRestrictionMatrix`** (`fespace.hpp:102-103`) — the L-vector ↔
  true-dof transfer matrices, **owned by MFEM**, forwarded verbatim. This is the surface that
  [`linalg-rap-file`](./linalg-rap-file.md)'s `ParOperator` uses for its prolongate-apply-restrict
  sandwich.
- **libCEED basis / element-restriction accessors** (`fespace.hpp:114-149`) —
  `GetCeedBasis(ceed, geom)`, `GetCeedElemRestriction(ceed, geom, indices)`, plus the two
  interpolation-specialized variants `GetInterpCeedElemRestriction` /
  `GetInterpRangeCeedElemRestriction`, and the static builders `BuildCeedBasis` /
  `BuildCeedElemRestriction`. These are the objects [`fem-libceed-operator-file`](./fem-libceed-operator-file.md)'s
  `CeedOperatorCoarsen` pulls via `GetCeedGeomFactorData` / `GetCeedElemRestriction` / `GetCeedBasis`.
- **Discrete-interpolator accessor** (`fespace.hpp:106-112`) — `GetDiscreteInterpolator(aux_fespace)`
  returns the gradient/curl/divergence operator interpolating from an auxiliary to the primal space,
  lazily building it via `BuildDiscreteInterpolator` (`fespace.hpp:63`, body `fespace.cpp:173-238`)
  and caching against `aux_fespace`.
- **`FiniteElementSpaceHierarchy`** (`fespace.hpp:200-286`) — owns
  `vector<unique_ptr<FiniteElementSpace>> fespaces` + a parallel `mutable
  vector<unique_ptr<Operator>> P` of inter-level prolongations (`fespace.hpp:203-204`). `AddLevel`
  (`fespace.hpp:216-220`) pushes a space + a null prolongation slot; `GetFESpaceAtLevel` /
  `GetFinestFESpace` index the stack (`fespace.hpp:222-246`); `GetProlongationAtLevel`
  (`fespace.hpp:248-254`) lazily builds via `BuildProlongationAtLevel` (`fespace.hpp:205`, body
  `fespace.cpp:240-261`); `GetProlongationOperators` (`fespace.hpp:256-266`) collects the full chain.
  `GetDiscreteInterpolators` (`fespace.hpp:274-285`) collects per-level interpolators (level 0 is
  null — *"No discrete interpolator for coarsest level"*, `fespace.cpp` analogue at `fespace.hpp:280`).

## libCEED basis / restriction caches — lazy, per-`Ceed`, per-geometry

`GetCeedBasis` (`fespace.cpp:15-26`) is a two-level lazy cache: it looks up the `Ceed` context in
`basis` (`MFEM_ASSERT` the context is known, `fespace.cpp:17`), then the `mfem::Geometry::Type` in that
context's map, returning the cached `CeedBasis` or `emplace`-ing a freshly-built one via the static
`BuildCeedBasis` (`fespace.cpp:25`). `GetCeedElemRestriction` (`fespace.cpp:28-41`) follows the
identical pattern against the `restr` map.

The two interpolation-specialized restrictions branch on element type:

- `GetInterpCeedElemRestriction` (`fespace.cpp:44-65`) — for tensor-product, non-VECTOR-range
  elements (`HasUniqueInterpRestriction`, `fespace.hpp:40-48`, requires **native, not lexicographic**
  ordering, `fespace.hpp:42-43` comment), uses a separate `interp_restr` cache built with
  `is_interp=true` (`fespace.cpp:62`). Otherwise it falls through to the plain
  `GetCeedElemRestriction` (guard `fespace.cpp:49`, fall-through `fespace.cpp:51`).
- `GetInterpRangeCeedElemRestriction` (`fespace.cpp:67-88`) — for 3-D spaces whose FE collection has
  a non-identity `DofTransformation` for the geometry (`HasUniqueInterpRangeRestriction`,
  `fespace.hpp:50-61`), uses `interp_range_restr` built with `is_interp=true, is_interp_range=true`
  (`fespace.cpp:83`). The comment (`fespace.hpp:51-52`) is the load-bearing reason: *"The range
  restriction for interpolation operators needs to use a special DofTransformation (not equal to the
  transpose of the domain restriction)."* Otherwise it falls through to `GetInterpCeedElemRestriction`.

The static builders are where the MFEM↔libCEED bridge happens. `BuildCeedBasis`
(`fespace.cpp:134-159`) selects the quadrature rule via `fem::DefaultIntegrationOrder::Get(T)`
(`fespace.cpp:147`) against the **nodal** FE for the geometry (`fespace.cpp:139-145`), then calls
`ceed::InitBasis(*fe, ir, vdim, ceed, &val)` (`fespace.cpp:158`). `BuildCeedElemRestriction`
(`fespace.cpp:162-171`) computes `use_bdr` (whether the element geometry's dimension is below the
mesh dimension — a **boundary** restriction, `fespace.cpp:166`) and calls
`ceed::InitRestriction(...)` (`fespace.cpp:167`). The actual basis / restriction construction lives in
`fem/libceed/basis.hpp` / `restriction.hpp` (forward-referenced; not yet anchored).

`ResetCeedObjects` (`fespace.cpp:90-132`) is the teardown/re-init: it destroys every cached
`CeedBasis` / `CeedElemRestriction` across all four maps via `PalaceCeedCall(...Destroy(&val))`
(`fespace.cpp:92-119`), clears the maps (`fespace.cpp:121-124`), then re-seeds one empty
per-geometry map for each registered `Ceed` context (`fespace.cpp:125-131`). The destructor
(`fespace.hpp:76`) and `Update()` (`fespace.hpp:141`) both route through it. The cache lifecycle is
transparent performance machinery ([`transparent-vs-load-bearing-tricks`](./transparent-vs-load-bearing-tricks.md)):
the basis / restriction objects are functions of (space, geometry, `Ceed`) and re-derivable on
demand.

## `BuildDiscreteInterpolator` — gradient / curl / divergence interpolator dispatch

`BuildDiscreteInterpolator` (`fespace.cpp:173-238`) constructs the discrete differential operator
interpolating from an auxiliary space to the primal space, **always partially assembled**
(`fespace.cpp:175-176` comment). It first resolves orientation: `forward` holds when the primal
space's map type equals the auxiliary space's *derivative* map type
(`GetMapType(dim) == aux->GetDerivMapType(dim)`, `fespace.cpp:178-179`), with a `swap` guard that
`MFEM_VERIFY`s the spaces were passed in the intended `deriv(aux) -> primal` order
(`fespace.cpp:180-185`). It then dispatches on the `(aux_map_type, primal_map_type)` pair, building a
[`DiscreteLinearOperator`](./fem-bilinearform-file.md) with the matching MFEM interpolator and wrapping
its `PartialAssemble()` in a [`ParOperator`](./linalg-rap-file.md):

- **VALUE → H_CURL** (`fespace.cpp:191-198`): discrete **gradient** (`GradientInterpolator`).
- **H_CURL → H_DIV** (`fespace.cpp:199-206`): discrete **curl** in 3-D (`CurlInterpolator`).
- **H_CURL → INTEGRAL** (`fespace.cpp:207-220`): discrete **curl** in 2-D (scalar curl, H(curl) → L2).
  This branch uses **MFEM's native assembly** (`interp.Assemble()` + `interp.Finalize()` +
  `LoseMat()`), not libCEED partial assembly — the comment (`fespace.cpp:213-214`) states *"libCEED
  does not support partial assembly for this operator type."* This is a **load-bearing variant**, not a
  transparent trick: the 2-D scalar-curl interpolator is assembled differently from the other three.
- **H_DIV → INTEGRAL** (`fespace.cpp:221-228`): discrete **divergence** (`DivergenceInterpolator`).
- anything else: `MFEM_ABORT` *"Unsupported trial/test FE spaces..."* (`fespace.cpp:230-233`).

The constructed `G` is cached and returned (`fespace.cpp:238`).

## `BuildProlongationAtLevel` — inter-level multigrid prolongation

`BuildProlongationAtLevel(l)` (`fespace.cpp:240-261`) builds the prolongation from hierarchy level `l`
to `l+1`, **always partially assembled** (`fespace.cpp:242` comment), branching on whether the two
levels share a mesh:

- **Different meshes** (`fespace.cpp:245-251`): an `mfem::TransferOperator` (the h-refinement / mesh
  transfer) wrapped in a `ParOperator`.
- **Same mesh** (p-refinement, `fespace.cpp:252-258`): a `DiscreteLinearOperator` with an
  `IdentityInterpolator` (`fespace.cpp:255`), `PartialAssemble`d and wrapped in a `ParOperator`.

This is the per-level construction that supplies the multigrid prolongation stack consumed by
`GeometricMultigridSolver` ([`preconditioner-classes-overview`](./preconditioner-classes-overview.md)).
It is the **input-side** counterpart to [`fem-libceed-operator-file`](./fem-libceed-operator-file.md)'s
`CeedOperatorCoarsen` (which builds the coarse *operators*); this builds the inter-level *transfer
operators*.

## Notes for higher layers

- **This file is the FE-space input substrate; assembly consumes it.** `BilinearForm` /
  `DiscreteLinearOperator` ([`fem-bilinearform-file`](./fem-bilinearform-file.md)) take a
  `FiniteElementSpace &` and pull its `GetCeedBasis` / `GetCeedElemRestriction` /
  `GetInterp*CeedElemRestriction` to build libCEED sub-operators. At L1, the FE-space is the typed
  *domain/range* object of the FE-assembly map; this chapter anchors that object.
- **The dof structure is MFEM's; the lift reads it as given.** dof/vdof numbering, byNODES/byVDIM
  ordering, element-to-dof tables, conformity, and the prolongation/restriction matrices forward to
  `mfem::ParFiniteElementSpace` (`fespace.hpp:93-103`). Higher layers treat the FE-space as an opaque
  index structure with a known true-dof ↔ L-vector transfer (`GetProlongationMatrix`); the internal
  numbering is out of scope per the single-rank / MFEM-as-given reading.
- **The four basis/restriction caches collapse to one "FE-space → libCEED-data" map at L1.** The
  plain / interp / interp-range restriction split (`fespace.cpp:44-88`) is a load-bearing distinction
  *only* for the interpolation path (tensor native-ordering; 3-D special `DofTransformation`); for a
  plain `BilinearForm` it is the bare `restr`. At L1 the basis + restriction are derived data of
  (space, geometry); the lazy-cache lifecycle (`ResetCeedObjects`) is a transparent performance
  annotation.
- **`BuildDiscreteInterpolator`'s 4-way dispatch is the discrete-de-Rham interpolator family.** The
  gradient / curl(3-D) / curl(2-D) / divergence cases (`fespace.cpp:191-228`) are the discrete
  differential operators of the FE de-Rham complex (H1 →∇ H(curl) →∇× H(div) →∇· L2). At L2 these lift
  as a single "discrete exterior-derivative interpolator" parameterized by the (domain, range) space
  pair; the 2-D-scalar-curl native-assembly branch is the one load-bearing variant.
- **`BuildProlongationAtLevel` is the input-side multigrid transfer; coarsening is the operator
  side.** The h/p-refinement prolongation built here (`fespace.cpp:245-258`) is paired with
  [`fem-libceed-operator-file`](./fem-libceed-operator-file.md)'s `CeedOperatorCoarsen`: together they
  are the prolongation `P` and coarse operator `RAP` of the geometric-multigrid V-cycle algebra.

## Referenced from

*Forward-declared. L1 work on the FE-assembly operator (the FE-space as typed domain/range, the
discrete-interpolator family, the multigrid transfer stack), queued as FE-space material reaches the
frontier, will reference this chapter.*

- [`L0/fem-bilinearform-file`](./fem-bilinearform-file.md) — the assembly entry-point file whose
  `BilinearForm` / `DiscreteLinearOperator` take a `FiniteElementSpace &` and pull its libCEED basis /
  restriction objects; this chapter is its input substrate.
- [`L0/fem-libceed-operator-file`](./fem-libceed-operator-file.md) — the libCEED backend whose
  `CeedOperatorCoarsen` reuses this file's `GetCeedBasis` / `GetCeedElemRestriction`; the
  operator-side counterpart to this file's transfer-operator side.
- [`L0/linalg-rap-file`](./linalg-rap-file.md) — the `ParOperator` wrapper this file uses for every
  constructed interpolator / prolongation, and which uses this file's `GetProlongationMatrix` /
  `GetRestrictionMatrix` for its prolongate-apply-restrict sandwich.
- [`L0/par-types-single-rank-reading`](./par-types-single-rank-reading.md) — the
  `mfem::ParFiniteElementSpace` / `ParMesh` / `GetComm` single-rank reading rule applied throughout.
- [`L0/transparent-vs-load-bearing-tricks`](./transparent-vs-load-bearing-tricks.md) — the lazy
  basis/restriction cache lifecycle (transparent) vs the 2-D-scalar-curl native-assembly branch and
  the interp-range special-`DofTransformation` (load-bearing) classification.
- [`L0/preconditioner-classes-overview`](./preconditioner-classes-overview.md) — the
  `GeometricMultigridSolver` consuming the `FiniteElementSpaceHierarchy` prolongation stack.

## Evidence (representative)

- `palace/fem/fespace.hpp:1-291` — the header file (291 lines; `FiniteElementSpace` +
  `FiniteElementSpaceHierarchy`).
- `palace/fem/fespace.hpp:15` — `namespace palace` open.
- `palace/fem/fespace.hpp:18-20` — `FiniteElementSpace` doc comment (*"Wrapper for MFEM's
  ParFiniteElementSpace class, with extensions for Palace."*).
- `palace/fem/fespace.hpp:21-194` — `class FiniteElementSpace` body.
- `palace/fem/fespace.hpp:24,27` — `mfem::ParFiniteElementSpace fespace;` (wrapped MFEM space) +
  `Mesh &mesh;` (non-owned).
- `palace/fem/fespace.hpp:30-32` — the four libCEED caches: `CeedObjectMap<CeedBasis> basis;` +
  `CeedObjectMap<CeedElemRestriction> restr, interp_restr, interp_range_restr;`.
- `palace/fem/fespace.hpp:35` — `mutable ComplexVector tx, lx, ly;` (operator-apply workspace).
- `palace/fem/fespace.hpp:37-39` — `mutable const FiniteElementSpace *aux_fespace;` +
  `mutable std::unique_ptr<Operator> G;` (lazy discrete-interpolator state).
- `palace/fem/fespace.hpp:40-48` — `HasUniqueInterpRestriction` (tensor-product, native-ordering,
  non-VECTOR-range predicate).
- `palace/fem/fespace.hpp:50-61` — `HasUniqueInterpRangeRestriction` (3-D, non-identity
  `DofTransformation` predicate; comment 51-52 the load-bearing reason).
- `palace/fem/fespace.hpp:63` — `const Operator &BuildDiscreteInterpolator() const;` decl.
- `palace/fem/fespace.hpp:67-75` — variadic constructor: forwards `args...` into
  `mfem::ParFiniteElementSpace`, then `ResetCeedObjects()` + device-marks `tx/lx/ly`.
- `palace/fem/fespace.hpp:76` — `virtual ~FiniteElementSpace() { ResetCeedObjects(); }`.
- `palace/fem/fespace.hpp:77-101` — MFEM-forwarding accessors (`Get`, conversions, `GetFEColl`,
  `GetMesh`/`GetParMesh`, dof-count getters, `Dimension`/`SpaceDimension`/`GetMaxElementOrder`).
- `palace/fem/fespace.hpp:93-96` — `GetVDim`/`GetVSize`/`GlobalVSize`/`GetTrueVSize` — each
  `return Get().X()` (MFEM-owned dof counts).
- `palace/fem/fespace.hpp:102-103` — `GetProlongationMatrix` / `GetRestrictionMatrix` — each
  `return Get().GetProlongationMatrix()` / `Get().GetRestrictionMatrix()` (MFEM-owned transfer
  matrices).
- `palace/fem/fespace.hpp:106-112` — `GetDiscreteInterpolator(aux_fespace_)` (lazy-build + cache-on
  `aux_fespace`).
- `palace/fem/fespace.hpp:114` — `CeedBasis GetCeedBasis(Ceed ceed, mfem::Geometry::Type geom) const;`.
- `palace/fem/fespace.hpp:118-135` — `GetCeedElemRestriction` + `GetInterpCeedElemRestriction` +
  `GetInterpRangeCeedElemRestriction` decls (with comments on the interp / interp-range fallbacks).
- `palace/fem/fespace.hpp:137-149` — `ResetCeedObjects` + `Update()` + static `BuildCeedBasis` /
  `BuildCeedElemRestriction` decls.
- `palace/fem/fespace.hpp:151-184` — `GetTVector` / `GetLVector` / `GetLVector2` templated workspace
  accessors (`ComplexVector` vs `.Real()` on the element-type axis).
- `palace/fem/fespace.hpp:186` — `MPI_Comm GetComm() const { return fespace.GetComm(); }`.
- `palace/fem/fespace.hpp:196-198` — `FiniteElementSpaceHierarchy` doc comment.
- `palace/fem/fespace.hpp:200-286` — `class FiniteElementSpaceHierarchy` body.
- `palace/fem/fespace.hpp:203-204` — `std::vector<std::unique_ptr<FiniteElementSpace>> fespaces;` +
  `mutable std::vector<std::unique_ptr<Operator>> P;`.
- `palace/fem/fespace.hpp:205` — `const Operator &BuildProlongationAtLevel(std::size_t l) const;` decl.
- `palace/fem/fespace.hpp:216-220` — `AddLevel` (push space + null prolongation slot).
- `palace/fem/fespace.hpp:222-246` — `GetFESpaceAtLevel` / `GetFinestFESpace` (bounds-checked index).
- `palace/fem/fespace.hpp:248-254` — `GetProlongationAtLevel` (lazy via `BuildProlongationAtLevel`).
- `palace/fem/fespace.hpp:256-266` — `GetProlongationOperators` (collect chain, levels 0..N-2).
- `palace/fem/fespace.hpp:268-285` — `GetDiscreteInterpolatorAtLevel` + `GetDiscreteInterpolators`
  (level-0 null, *"No discrete interpolator for coarsest level"*).
- `palace/fem/fespace.cpp:1-264` — the source file (264 lines).
- `palace/fem/fespace.cpp:12` — `namespace palace` open.
- `palace/fem/fespace.cpp:15-26` — `GetCeedBasis` (two-level lazy cache; `emplace(BuildCeedBasis)` at 25).
- `palace/fem/fespace.cpp:28-41` — `GetCeedElemRestriction` (same lazy-cache pattern on `restr`).
- `palace/fem/fespace.cpp:44-65` — `GetInterpCeedElemRestriction` (`HasUniqueInterpRestriction` guard
  49, fall-through 51, `interp_restr` cache, `BuildCeedElemRestriction(..., true, false)` at 62).
- `palace/fem/fespace.cpp:67-88` — `GetInterpRangeCeedElemRestriction`
  (`HasUniqueInterpRangeRestriction` guard 71, fall-through 73, `interp_range_restr` cache,
  `BuildCeedElemRestriction(..., true, true)` at 83).
- `palace/fem/fespace.cpp:90-132` — `ResetCeedObjects` (destroy 92-119, clear 121-124, re-seed
  per-`Ceed` empty maps 125-131).
- `palace/fem/fespace.cpp:134-159` — `BuildCeedBasis` (static): nodal-FE integration-rule selection
  (139-148) + `ceed::InitBasis(*fe, ir, vdim, ceed, &val)` (158).
- `palace/fem/fespace.cpp:162-171` — `BuildCeedElemRestriction` (static): `use_bdr` boundary check
  (166) + `ceed::InitRestriction(...)` (167).
- `palace/fem/fespace.cpp:173-238` — `BuildDiscreteInterpolator`: orientation resolve (178-188), 4-way
  `(aux_map, primal_map)` dispatch — gradient (191-198), 3-D curl (199-206), 2-D scalar curl via MFEM
  native assembly (207-220, comment 213-214), divergence (221-228), `MFEM_ABORT` else (230-233).
- `palace/fem/fespace.cpp:240-261` — `FiniteElementSpaceHierarchy::BuildProlongationAtLevel`:
  bounds-verify (242-244), different-mesh `TransferOperator` path (245-251), same-mesh
  `IdentityInterpolator` p-refinement path (252-258).
- `test/unit/test-libceed.cpp:12` — `#include "fem/fespace.hpp"` (the FE-space wrapper is exercised by
  the libCEED test).
- `test/unit/test-libceed.cpp:1169-1199` — H1 / H(curl) / H(div) **prolongation** SECTIONs:
  `FiniteElementSpace` coarse+fine pairs, `DiscreteLinearOperator` with `IdentityInterpolator`,
  asserted against `mfem::PRefinementTransferOperator` — exercises the same p-refinement prolongation
  primitive `BuildProlongationAtLevel`'s same-mesh branch (`fespace.cpp:252-258`) constructs.
- `test/unit/test-libceed.cpp:1202-1222` — discrete **gradient** (H1→H(curl)) and **curl**
  (H(curl)→H(div)) SECTIONs through `FiniteElementSpace` + `DiscreteLinearOperator`, asserted against
  `mfem::DiscreteLinearOperator` — the same interpolator-family primitives `BuildDiscreteInterpolator`
  dispatches (`fespace.cpp:191-206`).
- `test/unit/test-boundarymodeoperator.cpp:75-92` — `FiniteElementSpace nd_fespace` / `h1_fespace`
  constructed directly, `Get().GetEssentialTrueDofs` / `GetTrueVSize` exercised — the
  wrapper's MFEM-forwarding accessor surface (`fespace.hpp:93-103`).
