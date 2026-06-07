---
rank: firm
kind: record
edges:
  depends-on:
    - target: palace/utils/configfile.hpp:97-154
      kind: cites-evidence            # struct RefinementData: public AMR fields :100-138 (tol :101, max_it :104, max_size :108, nonconformal :111, max_nc_levels :115, update_fraction :119, maximum_imbalance :123, save_adapt_iterations :127, save_adapt_mesh :130, uniform_ref_levels :133, ser_uniform_ref_levels :136), private box/sphere lists + accessors :140-150, ctors :152-153
    - target: palace/utils/configfile.cpp:318-359
      kind: cites-evidence            # RefinementData(const json &) JSON->field binding: "Tol":321 "MaxIts":322 "MaxSize":323 "Nonconformal":324 "MaxNCLevels":325 "UpdateFraction":326 "MaximumImbalance":327 "SaveAdaptIterations":328 "SaveAdaptMesh":329 "UniformLevels":332 "SerialUniformLevels":333
  reference:
    - L1/dorfler_mark
    - L1-L0/amr-estimate-mark-refine
    - feature/lifecycle.L4
    - concepts/config-record
    - concepts/build-time-vs-run-time-stratification
---

# RefinementData

> **Kind: `record`.** This page defines the *data shape* of `RefinementData` — its fields, their
> types and meaning, the construction-vs-run-time stratum of each, and the L0 source home (the
> backing C++ struct + the `Refinement` JSON surface) the record mirrors. The *behaviour* — how
> [`dorfler_mark`](../L1/dorfler_mark.md) uses the θ field, how the AMR
> [estimate→mark→refine fold](../L1-L0/amr-estimate-mark-refine.md) reads the loop bounds — lives in
> those chapters; this page does not restate that algebra.

`RefinementData` is the Palace **adaptive-mesh-refinement (AMR) configuration record** — the
construction-time settings sub-record that parameterizes the estimate→mark→refine loop (Dörfler bulk
fraction, convergence tolerance, iteration / DOF / nonconformity caps) plus the a-priori
(non-adaptive) uniform-refinement levels. It is a sub-record of the [config-record](./config-record.md)
tree (the `model.refinement` field, parsed from `config["Model"]["Refinement"]`). The
[`amr-estimate-mark-refine`](../L1-L0/amr-estimate-mark-refine.md) theme refers to it by the name
`RefineConfig` (an inline single-consumer alias); this page is its definition home. Multiple consumers
([`dorfler_mark`](../L1/dorfler_mark.md) θ-field + the AMR loop at
[`lifecycle.L4`](../feature/lifecycle.L4.md) + the estimate-mark-refine theme) put it at the
≥2-consumer bar, so it has a cross-cutting definition home here rather than only an in-chapter section.

## One-line semantics

`RefinementData` is an immutable **construction-stratum** bag of AMR scalars: the Dörfler bulk
fraction `update_fraction` (θ), the convergence tolerance `tol`, the iteration / DOF-size /
nonconformity caps that bound the loop, and the a-priori uniform-refinement level counts. It carries
no algebra of its own — it is read once at startup and consumed read-only by the AMR loop and the
marking verb.

## Record definition

`RefinementData` is the backing C++ `struct RefinementData` (`palace/utils/configfile.hpp:97-154`).
The TS brace form (all fields construction-time scalars; defaults as shipped):

```text
RefinementData = {
  -- adaptive (estimate→mark→refine) controls
  tol                    : Real,   -- AMR convergence tolerance (non-dimensional); default 1.0e-2
  max_it                 : Int,    -- max adaptation iterations; default 0 (0 ⇒ AMR disabled)
  max_size               : Int,    -- DOF cap: no refinement once #DOFs exceeds this; default 0 (no cap)
  nonconformal           : Bool,   -- perform nonconformal (hanging-node) adaptation; default true
  max_nc_levels          : Int,    -- max nonconformity difference between adjacent elements; default 1
  update_fraction        : Real,   -- the Dörfler bulk fraction θ ∈ (0,1]; default 0.7
  maximum_imbalance      : Real,   -- multi-rank load-rebalance trigger ratio; default 1.1 [out of scope]
  save_adapt_iterations  : Bool,   -- write each adaptation iteration as a postprocess subfolder; default true
  save_adapt_mesh        : Bool,   -- write a (serial) mesh after each AMR modification; default false
  -- a-priori (non-adaptive) uniform refinement
  uniform_ref_levels     : Int,    -- parallel uniform refinement levels; default 0 [Par* single-rank]
  ser_uniform_ref_levels : Int,    -- serial uniform refinement levels; default 0
  -- region-refinement lists (a-priori box/sphere; private, accessor-fronted)
  box_list               : [BoxRefinementData],     -- per-box refinement regions (a-priori)
  sphere_list            : [SphereRefinementData]   -- per-sphere refinement regions (a-priori)
}
```

| field | type | meaning | stratum | L0 source |
|---|---|---|---|---|
| `tol` | `Real` | AMR convergence tolerance: the loop runs while the indicator norm `err >= tol`. Non-dimensional. | construction-time | `configfile.hpp:101` (← `"Tol"`, `configfile.cpp:321`) |
| `max_it` | `Int` | maximum adaptation iterations; **`0` disables AMR** (the loop never enters — the single initial `Solve`). | construction-time | `configfile.hpp:104` (← `"MaxIts"`, `configfile.cpp:322`) |
| `max_size` | `Int` | DOF cap: once a refinement would exceed this #DOFs, no further refinement is allowed. `0` ⇒ no cap. | construction-time | `configfile.hpp:108` (← `"MaxSize"`, `configfile.cpp:323`) |
| `nonconformal` | `Bool` | whether to perform nonconformal (hanging-node) adaptation. | construction-time | `configfile.hpp:111` (← `"Nonconformal"`, `configfile.cpp:324`) |
| `max_nc_levels` | `Int` | max nonconformity-refinement-level difference between two adjacent elements; `0` ⇒ unconstrained. Passed to `GeneralRefinement`. | construction-time | `configfile.hpp:115` (← `"MaxNCLevels"`, `configfile.cpp:325`) |
| `update_fraction` | `Real` | **the Dörfler bulk fraction θ** ∈ `(0,1]` — the marked set is the minimum set covering `update_fraction` of the total error. Read by [`dorfler_mark`](../L1/dorfler_mark.md) as its θ argument. | construction-time | `configfile.hpp:119` (← `"UpdateFraction"`, `configfile.cpp:326`) |
| `maximum_imbalance` | `Real` | max element-count ratio across processors before rebalancing. **Out of scope** (multi-rank; read single-rank, rebalancing is a no-op). | construction-time | `configfile.hpp:123` (← `"MaximumImbalance"`, `configfile.cpp:327`) |
| `save_adapt_iterations` | `Bool` | write each adaptation iteration's results as a postprocessing subfolder. (I/O concern.) | construction-time | `configfile.hpp:127` (← `"SaveAdaptIterations"`, `configfile.cpp:328`) |
| `save_adapt_mesh` | `Bool` | write a serial mesh to file after each AMR mesh modification. (I/O concern.) | construction-time | `configfile.hpp:130` (← `"SaveAdaptMesh"`, `configfile.cpp:329`) |
| `uniform_ref_levels` | `Int` | a-priori **parallel** uniform mesh-refinement levels (applied before the solve, not adaptive). `Par*` — read single-rank. | construction-time | `configfile.hpp:133` (← `"UniformLevels"`, `configfile.cpp:332`) |
| `ser_uniform_ref_levels` | `Int` | a-priori **serial** uniform mesh-refinement levels (applied before the solve, not adaptive). | construction-time | `configfile.hpp:136` (← `"SerialUniformLevels"`, `configfile.cpp:333`) |
| `box_list` / `sphere_list` | `[BoxRefinementData]` / `[SphereRefinementData]` | a-priori region-refinement specs (refine elements inside named boxes / spheres). Private; fronted by `GetBox`/`GetBoxes`/`GetSphere`/`GetSpheres` accessors. Out of the adaptive-loop scope. | construction-time | `configfile.hpp:140-150` (parsed `configfile.cpp:334-357`) |

Every field is **construction-time**: the record is parsed once at startup from the JSON config and
consumed read-only thereafter (it is not threaded through the AMR carry — the carry is
[`AmrCarry`](../L1-L0/amr-estimate-mark-refine.md) `{ mesh, indicators, ntdof, err }`, a distinct
run-time value). The [`build-time-vs-run-time-stratification`](./build-time-vs-run-time-stratification.md)
split is trivial here: the whole record is build-time.

## L0 source home — `struct RefinementData` + the `Refinement` JSON surface

The backing C++ struct is `struct RefinementData` (`palace/utils/configfile.hpp:97-154`): the public
AMR fields (`:100-138`), the private box/sphere region-refinement lists + their accessors
(`:140-150`), and the two ctor declarations (`:152-153`). It is parsed from the JSON `Refinement`
object by `RefinementData::RefinementData(const json &refinement)`
(`palace/utils/configfile.cpp:318-359`) — each public scalar field is bound by a
`field = refinement.value("<JsonKey>", field)` line (`:321-333`), so the **`refinement.*` IoData
surface** is exactly the `"Tol"` / `"MaxIts"` / `"MaxSize"` / `"Nonconformal"` / `"MaxNCLevels"` /
`"UpdateFraction"` / `"MaximumImbalance"` / `"SaveAdaptIterations"` / `"SaveAdaptMesh"` /
`"UniformLevels"` / `"SerialUniformLevels"` key set. The record is reached as `model.refinement`
within the [config-record](./config-record.md) tree (`refinement = ParseOptional<RefinementData>(model,
"Refinement")`, `configfile.cpp:378`); a non-dimensionalization pass `Nondimensionalize(units, data)`
(`configfile.cpp:1535`) scales the dimensioned a-priori box/sphere region bounds — `tol`,
`update_fraction`, and the integer caps are non-dimensional and untouched.

**Single-machine carve-outs (flagged once, per CLAUDE.md §Scope).** `maximum_imbalance`,
`uniform_ref_levels` (the `Par*` parallel uniform levels), and the multi-rank rebalancing trigger are
**out of scope** — read single-rank, the rebalance is a no-op and `uniform_ref_levels` reduces to the
serial uniform refinement. They are recorded here as struct fields for fidelity but the record does
not define the multi-rank rebalancing semantics.

## Signatures / chapters that name this record

- [`dorfler_mark`](../L1/dorfler_mark.md) — **consumer** (the θ field): `dorfler_mark`'s θ argument is
  `RefinementData.update_fraction` (the Dörfler bulk fraction, default 0.7); the mark-stage caller
  binds `θ = refinement.update_fraction` (`palace/drivers/basesolver.cpp:223-224`).
- [`amr-estimate-mark-refine`](../L1-L0/amr-estimate-mark-refine.md) — **consumer** (names it
  `RefineConfig` in the step-body signature `amr_step :: Estimator -> RefineConfig -> AmrCarry ->
  AmrCarry`; reads `cfg.fraction ← update_fraction`).
- [`lifecycle.L4`](../feature/lifecycle.L4.md) §3 — **consumer** (the estimate→mark→refine outer
  [`fold_solve`](../L4/fold_solve.md)): the loop guard reads `refinement.tol` / `refinement.max_it`,
  the mark stage reads `refinement.update_fraction`, the refine stage reads `refinement.max_nc_levels`
  (`fine_mesh.GeneralRefinement(marked, -1, refinement.max_nc_levels)`,
  `palace/drivers/basesolver.cpp:239`).

## See also

- [`dorfler_mark`](../L1/dorfler_mark.md) — the marking verb that reads the θ (`update_fraction`)
  field; defines the *behaviour* (the bulk-marking criterion). This page defines only the *shape* of
  its config input.
- [`amr-estimate-mark-refine`](../L1-L0/amr-estimate-mark-refine.md) — the L1>L0 AMR lowering theme;
  names this record `RefineConfig` and reads the loop bounds. This page is its definition home.
- [config-record](./config-record.md) — the enclosing config tree; `RefinementData` is its
  `model.refinement` sub-record.
- [`build-time-vs-run-time-stratification`](./build-time-vs-run-time-stratification.md) — the
  stratum pattern (this record is wholly build-time).

**If this page and a consumer chapter / the L0 source disagree on any factual claim about the record,
the L0 source (`palace/utils/configfile.hpp` / `configfile.cpp`) wins and this page is corrected.**

## Status

`firm` — the data shape is read directly from the positive `struct RefinementData`
(`palace/utils/configfile.hpp:97-154`): the public AMR fields with their defaults (`tol :101`,
`max_it :104`, `max_size :108`, `nonconformal :111`, `max_nc_levels :115`, `update_fraction :119`,
`maximum_imbalance :123`, `save_adapt_iterations :127`, `save_adapt_mesh :130`, `uniform_ref_levels
:133`, `ser_uniform_ref_levels :136`), the private region-refinement lists + accessors (`:140-150`),
and the ctor declarations (`:152-153`). The JSON `Refinement` surface + the field bindings are read off
`RefinementData::RefinementData(const json &)` (`palace/utils/configfile.cpp:318-359`,
`field = refinement.value("<Key>", field)` per field `:321-333`). Every field is construction-time
(parsed once at startup, read-only thereafter). All L0 citations self-verified against on-disk source
this dispatch via codemap `read_range`. The record-definition obligation is met: this is the
cross-cutting home for `RefinementData`, referenced by ≥2 consumers (`L1/dorfler_mark` θ-field + the
AMR loop at `lifecycle.L4` + the `amr-estimate-mark-refine` theme).

Well-foundedness (rank): the page is a `record` DAG node at `rank: firm`; its only blocking edges are
`cites-evidence depends-on` to the L0 `struct RefinementData` extent + JSON-ctor range (rank-terminal
ground truth), so the `rank(u) ≤ rank(v)` invariant holds vacuously. The edges to the consumer
chapters are `reference` (navigational — a record page is named-by-use, it does not block on its
consumers).
