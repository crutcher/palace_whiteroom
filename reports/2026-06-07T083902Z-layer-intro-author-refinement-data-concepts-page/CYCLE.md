---
agent: layer-intro-author
invoked_at: 2026-06-07T084500Z
scope: concepts/RefinementData.md record-definition page (cycle-123 D4)
status: pending
integrated_at: 2026-06-07T083902Z
integration_commit: e79fb8c
integration_notes: "Applied clean (D4, integrated FIRST so D1's forward link resolves). concepts/RefinementData.md firm record-definition page landed; consumers re-pointed (struct cite :97-154); SUMMARY concepts-list alpha insert. Closes OQ record-RefinementData-needs-concept-definition-home. cargo make book EXIT 0; rank_violations 0; both step-5b block-conditions PASS. Batch-39 BATCH-CLOSING finalize."
---

# CYCLE: concepts/RefinementData record-definition page

## Summary

Author `book/src/concepts/RefinementData.md` — the cross-cutting **record-definition** concepts
page for the AMR refinement config record `RefinementData` (the c122 `dorfler_mark` harvest flagged
`record-RefinementData-needs-concept-definition-home` at the ≥2-consumer bar). The page defines the
**data shape** (fields / types / meaning, the construction-vs-run-time stratum of each field, the L0
home of the backing C++ struct + the `refinement.*` IoData JSON surface) — NOT operator algebra. It
follows the `concepts/FiniteElementSpaceHierarchy.md` / `concepts/config-record.md` template.

Consumers at the ≥2 bar (the page is warranted): (1) [`dorfler_mark`](../L1/dorfler_mark.md) reads the
θ field (`update_fraction`); (2) the [`amr-estimate-mark-refine`](../L1-L0/amr-estimate-mark-refine.md)
theme names it as `RefineConfig` (currently an inline single-consumer §Record-definition); (3) the AMR
estimate→mark→refine outer fold at the [`lifecycle.L4`](../feature/lifecycle.L4.md) column (the loop
guard reads `refinement.tol`/`refinement.max_it`, the mark stage reads `refinement.update_fraction`).

Then re-point the consumers' inline mentions to the new page (back-links): `dorfler_mark`'s §Record
definition `RefinementData` paragraph and `amr-estimate-mark-refine`'s `RefineConfig` §Record-definition
bullet. Wire the page into `SUMMARY.md` at alpha position (between `rotation` and `scal`).

**L0 verification (this dispatch, via palace-codemap + on-disk reads):**
- `struct RefinementData` opens at `palace/utils/configfile.hpp:97` (`struct RefinementData` on `:97`,
  `{` on `:98`), closes at `:154` (the `};` after the two ctor declarations `:152-153`). The c122
  dispatches cited `~:96-125` / `:97-119`; the **exact** struct extent is **`:97-154`**. The public
  AMR fields are `:100-138`; the private box/sphere refinement lists + accessors are `:140-150`; the
  ctor declarations are `:152-153`.
- Field defaults (read off `configfile.hpp`): `tol = 1.0e-2` (`:101`), `max_it = 0` (`:104`),
  `max_size = 0` (`:108`), `nonconformal = true` (`:111`), `max_nc_levels = 1` (`:115`),
  `update_fraction = 0.7` (`:119`, with the Dörfler comment `:117-118`), `maximum_imbalance = 1.1`
  (`:123`), `save_adapt_iterations = true` (`:127`), `save_adapt_mesh = false` (`:130`),
  `uniform_ref_levels = 0` (`:133`), `ser_uniform_ref_levels = 0` (`:136`).
- IoData JSON surface: the keys are bound in `RefinementData::RefinementData(const json &refinement)`
  (`palace/utils/configfile.cpp:318-359`): `"Tol"` (`:321`), `"MaxIts"` (`:322`), `"MaxSize"` (`:323`),
  `"Nonconformal"` (`:324`), `"MaxNCLevels"` (`:325`), `"UpdateFraction"` (`:326`), `"MaximumImbalance"`
  (`:327`), `"SaveAdaptIterations"` (`:328`), `"SaveAdaptMesh"` (`:329`), `"UniformLevels"` (`:332`),
  `"SerialUniformLevels"` (`:333`). The record is parsed as `model["Refinement"]`
  (`refinement = ParseOptional<RefinementData>(model, "Refinement")`, `configfile.cpp:378`).

## Proposed changes

```edit:book/src/concepts/RefinementData.md
[new file]
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
```

```edit:book/src/L1/dorfler_mark.md
[old]: - **`θ : Real`** is a scalar, not a record — but its config home is the **`RefinementData`** struct
  (`palace/utils/configfile.hpp:97-119`), the `refinement.*` IoData surface. The field this verb reads
  is `update_fraction` (the Dörfler bulk fraction, default `0.7`, `:117-119`); sibling
  construction-time fields (`tol`/`max_it`/`max_size`/`max_nc_levels`/`nonconformal`) parameterize the
  enclosing AMR loop, not this verb. **Construction-time stratum** (read once, before the loop).
  `RefinementData` is used by ≥2 chapters (this verb, `flux_recovery_estimate`, the
  `amr-estimate-mark-refine` theme, the lifecycle feature column) — its full field-by-field definition
  is a cross-cutting concept home; the `amr-estimate-mark-refine` theme already defines it inline as a
  single-consumer record (§Record definition there). Flagged in Open questions
  (`record-RefinementData-needs-concept-definition-home`) so the cross-cutting page is dispatched; this
  verb references the θ ← `update_fraction` field only.
[new]: - **`θ : Real`** is a scalar, not a record — but its config home is the **`RefinementData`** struct
  (`palace/utils/configfile.hpp:97-154`), the `refinement.*` IoData surface. The field this verb reads
  is `update_fraction` (the Dörfler bulk fraction, default `0.7`, `:117-119`); sibling
  construction-time fields (`tol`/`max_it`/`max_size`/`max_nc_levels`/`nonconformal`) parameterize the
  enclosing AMR loop, not this verb. **Construction-time stratum** (read once, before the loop). The
  full field-by-field definition of `RefinementData` (used by ≥2 chapters — this verb, the
  `amr-estimate-mark-refine` theme, the lifecycle feature column) is its cross-cutting record-definition
  home [`concepts/RefinementData`](../concepts/RefinementData.md); this verb references the
  θ ← `update_fraction` field only.
```

```edit:book/src/L1-L0/amr-estimate-mark-refine.md
[old]: - **`RefineConfig`** — the (construction-time) refinement config record. The L0 home is the Palace
  `RefinementData` struct (`palace/utils/configfile.hpp:96-125`), the `refinement.*` IoData surface;
  the fields this step body reads are `fraction` (← `update_fraction`, the Dörfler bulk fraction θ,
  default 0.7, `:118-119`), with sibling construction-time fields `tol`/`max_it`/`max_size`/`max_nc_levels`
  also on the record. Construction-time stratum (read once before the loop), not run-time-threaded.
[new]: - **`RefineConfig`** — the (construction-time) refinement config record, an alias for the Palace
  `RefinementData` struct. Its full field-by-field definition home is
  [`concepts/RefinementData`](../concepts/RefinementData.md) (`palace/utils/configfile.hpp:97-154`,
  the `refinement.*` IoData surface). The fields this step body reads are `fraction`
  (← `update_fraction`, the Dörfler bulk fraction θ, default 0.7), with sibling construction-time
  fields `tol`/`max_it`/`max_size`/`max_nc_levels` also on the record. Construction-time stratum
  (read once before the loop), not run-time-threaded.
```

```edit:book/src/SUMMARY.md
[old]:   - [rotation — methodology concept](./concepts/rotation.md)
  - [scal](./concepts/scal.md)
[new]:   - [rotation — methodology concept](./concepts/rotation.md)
  - [RefinementData — record definition](./concepts/RefinementData.md)
  - [scal](./concepts/scal.md)
```

## Supporting evidence

- **L0 backing struct** `palace/utils/configfile.hpp:97-154` — `struct RefinementData`, verified via
  codemap `read_range` (`:90-160`, `:148-155`): opening `struct RefinementData` `:97`, public AMR
  fields `:100-138`, private region lists + accessors `:140-150`, ctor decls `:152-153`, `};` `:154`.
- **JSON binding** `palace/utils/configfile.cpp:318-359` — `RefinementData::RefinementData(const json
  &)`, verified via codemap `read_range` (`:318-340`) + `search_text`: each `field = refinement.value
  ("<Key>", field)` (`"Tol":321`, `"MaxIts":322`, `"MaxSize":323`, `"Nonconformal":324`,
  `"MaxNCLevels":325`, `"UpdateFraction":326`, `"MaximumImbalance":327`, `"SaveAdaptIterations":328`,
  `"SaveAdaptMesh":329`, `"UniformLevels":332`, `"SerialUniformLevels":333`). Parsed as
  `model["Refinement"]` (`configfile.cpp:378`); non-dimensionalized at `:1535`.
- **Consumers (the ≥2-consumer bar):** `book/src/L1/dorfler_mark.md` (θ ← `update_fraction`, §Record
  definition, signature `dorfler_mark :: Real -> Tensor[N] -> IndexSet[N]`);
  `book/src/L1-L0/amr-estimate-mark-refine.md` (`RefineConfig` §Record-definition bullet, step-body
  signature `amr_step :: Estimator -> RefineConfig -> AmrCarry -> AmrCarry`);
  `book/src/feature/lifecycle.L4.md:52` + `lifecycle.L0.md:41-42` (the estimate→mark→refine
  `fold_solve` reads `refinement.tol`/`max_it`/`update_fraction`/`max_nc_levels`).
- **Template precedent:** `book/src/concepts/FiniteElementSpaceHierarchy.md` (c121 record page),
  `book/src/concepts/config-record.md` (the enclosing config-record tree, of which `RefinementData` is
  the `model.refinement` sub-record).
- **Alpha position in SUMMARY:** between `rotation` (`:364`) and `scal` (`:365`) — `RefinementData`
  (capital R) files case-insensitively in the existing mixed-case ordering (cf. `Mesh` between
  `ksp_solve` and `negative-result-slice`; `FiniteElementSpaceHierarchy` between `finest-level-unwrap`
  and `first-iteration-unrolling`).

## Open questions / caveats

- **Shared-file coupling on `SUMMARY.md` (flagged for the integrator).** D1 (L1 AMR group-intro
  nesting, ~lines 245-246 / the L1-chapters block) and D2 (feature Part, the `# Feature surfaces`
  block ~line 54) also touch `SUMMARY.md` this cycle. My edit is the **concepts list** (the single
  `RefinementData` insertion between `:364`/`:365`) — a **disjoint region** from both. Per the c121/c122
  finalize precedent (multiple disjoint SUMMARY touches integrate clean via per-report on-disk
  re-read), this is parallel-safe; the integrator should apply each on-disk-re-read.
- **`amr-estimate-mark-refine`'s `AmrCarry` / `Estimator` / `IndexSet[E]` inline records are NOT
  migrated** — only `RefineConfig` (= `RefinementData`) crosses the ≥2-consumer bar this dispatch.
  `AmrCarry` is homed at `lifecycle.L4 §3`; `IndexSet[E]` is defined inline in both `dorfler_mark` and
  the theme (still single-cohort); `Estimator` has an OPEN harvester routing
  (`flux-projector-constructed-operator-gate-vs-absorbed`). None is in this page's scope (it defines
  `RefinementData` only); left as-is.
- **A-priori region-refinement sub-records (`BoxRefinementData` / `SphereRefinementData`) are named but
  not separately defined.** They are listed as the `box_list`/`sphere_list` field types (a-priori,
  out of the adaptive-loop scope). They are single-consumer (only `RefinementData` names them) and
  below the ≥2-consumer bar — no separate page warranted. If a second consumer surfaces, file
  `record-BoxRefinementData-needs-definition-home`; not flagged now (below bar).
- **`update_fraction` line-precise default citation kept as `:117-119`** in the re-pointed
  `dorfler_mark` text (the field + its Dörfler comment span `:117-119`; the bare default value is on
  `:119`). The struct-extent citation was corrected `:97-119` → `:97-154` (the c122 dispatches cited a
  truncated/approximate extent; the **exact** struct closes at `:154`). The `amr-estimate-mark-refine`
  citation was corrected `:96-125` → `:97-154` likewise.
- **OQ closure:** this dispatch closes `record-RefinementData-needs-concept-definition-home`.
