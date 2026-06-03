---
agent: layer-intro-author
invoked_at: 2026-06-03T154000Z
scope: concepts/config-record.md — cross-cutting record-definition page (record-definition cohort #2(b))
status: pending
integrated_at: 2026-06-03T154500Z
integration_commit: 8e54d0f4a22185f0fa1aed38cb930fdb19f8aaea
integration_notes: "Applied clean (staging row 3/5). 1 record-definition concept page (config-record, the IoData config data shape) + 1 alpha-position index/SUMMARY entry (REUSED D1's `record` legend). >=2-consumer bar met by 5 driver columns + lifecycle ROOT. record-definition data-shape page (claim checks no-op); citecheck main.cpp AMBIG was a --scan basename-collision artifact (full paths resolve, critic passed). Build clean."
---

# CYCLE: concepts/config-record record-definition page

## Summary

Authors a NEW cross-cutting record-definition concept page
`book/src/concepts/config-record.md` (record-definition cohort #2(b), per user
directive 2 / the record-definition obligation). The page defines the **config
record schema** — Palace's `IoData` configuration tree — as a **data shape**: its
five top-level config sub-records (`ProblemData` / `ModelData` / `DomainData` /
`BoundaryData` / `SolverData`) + `Units`, each field's stratum, and the L0
backing surface (`palace/utils/iodata.hpp` class `IoData`, parsed from the JSON
config file). It is consumed across **≥2 feature columns** — every one of the 5
driver-leaf feature columns + the lifecycle spine-ROOT constructs its operator
graph from `iodata` (`LaplaceOperator laplace_op(iodata, mesh)` etc.) — clearing
the ≥2-consumer bar for a standalone cross-cutting page (rather than an in-chapter
`## Record definition` section).

The page is uniformly **readonly construction-stratum** (config is parsed once,
overrides defaults, then is read — never mutated — by the operator factories). It
cross-links `concepts/build-time-vs-run-time-stratification.md` (config-record
parsing is named there as a build-time primitive). Discipline: the page defines
the data shape; the operators/feature-columns define the behavior over it (no
operator algebra restated here).

Also: alpha-position row inserts into `concepts/index.md` `## Index` (reusing the
`record` Kind that the parallel D1 dispatch authors the legend line for — NOT
re-authored here) and `book/src/SUMMARY.md` concepts block.

## Proposed changes

### 1. New file: `book/src/concepts/config-record.md`

```edit:book/src/concepts/config-record.md
[old]:
[new]:
# config-record

Cross-cutting **record-definition** page for Palace's configuration record —
the `IoData` tree parsed from the JSON config file at startup. This page
defines the **data shape** (fields, types, meaning, stratum, L0 home); the
feature columns and operator factories that consume it define the *behavior*
over it. Authored under the record-definition obligation (a record named in
≥2 chapters' signatures gets a definition home in itself, not only by use).

## One-line semantics

The config record is the single immutable **construction-stratum** input to
every Palace solve: one object, parsed once from the user's JSON file, that
selects the driver (`problem.type`) and supplies the mesh, materials,
boundaries, sources, and solver parameters that every operator factory reads
to build its operator graph. It is **readonly after parse** — no run-time
field; the whole record is build-time scaffolding in the sense of
[`build-time-vs-run-time-stratification`](./build-time-vs-run-time-stratification.md).

## L0 home — the `IoData` backing surface

The backing struct is `class IoData` (`palace/utils/iodata.hpp:27-61`). It is
constructed once in `main` from the config filename:

- `IoData iodata(argv[1], false)` — `palace/main.cpp:231` (the construction
  site; the spine-ROOT lifecycle's config→… first stage).
- ctor `IoData(const char *filename, bool print)` — `palace/utils/iodata.hpp:54`
  parses the JSON file, overrides option defaults, and (later, via
  `NondimensionalizeInputs`, `palace/utils/iodata.hpp:60`) rescales SI values to
  normalized units. Parsing + nondimensionalization are the only writes; after
  that `iodata` is read-only to all consumers.

`IoData` is a flat aggregate of five `config::` sub-records plus a `Units`
helper. Each sub-record is a plain-old-data tree of fields with JSON-sourced
defaults (defined in `palace/utils/configfile.hpp`).

## Schema — top-level `IoData` fields

The TS brace form of the record (each field readonly, construction-stratum):

```text
IoData {
  problem    : config::ProblemData    // simulation type + output/verbosity
  model      : config::ModelData      // mesh file, length unit, refinement
  domains    : config::DomainData     // per-region material properties
  boundaries : config::BoundaryData   // boundary conditions + sources
  solver     : config::SolverData     // linear/eigen/driver solver parameters
  units      : Units                  // SI ↔ nondimensional scale converter
}
```

| field | type | meaning | stratum | L0 source |
|---|---|---|---|---|
| `problem`    | `config::ProblemData`  | simulation type (the driver selector), verbosity, output path/formats | readonly construction | `iodata.hpp:31`; struct `configfile.hpp:57` |
| `model`      | `config::ModelData`    | mesh file path, length unit `L0` / characteristic length `Lc`, mesh-preprocessing + refinement flags | readonly construction | `iodata.hpp:32`; struct `configfile.hpp:156` |
| `domains`    | `config::DomainData`   | per-region material properties (permittivity, permeability, conductivity, …) | readonly construction | `iodata.hpp:33` |
| `boundaries` | `config::BoundaryData` | boundary conditions (PEC/PMC/impedance/absorbing) + excitation sources (ports, current dipoles) | readonly construction | `iodata.hpp:34` |
| `solver`     | `config::SolverData`   | linear/eigen/time-domain solver parameters, device + libCEED backend selection | readonly construction | `iodata.hpp:35`; struct `configfile.hpp:1026` |
| `units`      | `Units`                | mesh scale + SI↔normalized converter (populated during nondimensionalization) | readonly construction (after `NondimensionalizeInputs`) | `iodata.hpp:38` |

### The driver selector — `problem.type`

`problem.type : ProblemType` is the field that routes the whole simulation. The
spine-ROOT lifecycle dispatches on it:

```text
switch (iodata.problem.type) { DRIVEN | EIGENMODE | ELECTROSTATIC
                             | MAGNETOSTATIC | TRANSIENT | BOUNDARYMODE }
```

`palace/main.cpp:259` (the 6-branch dispatch; the lambda constructing the
`BaseSolver` spans `main.cpp:257-281`). The enum is
`enum class ProblemType : char` (`palace/utils/labels.hpp:18-26`) with the six
values `DRIVEN`, `EIGENMODE`, `ELECTROSTATIC`, `MAGNETOSTATIC`, `TRANSIENT`,
`BOUNDARYMODE`. The default is `ProblemType::DRIVEN` (`configfile.hpp:57-61`).
This is the field that makes one `IoData` schema specialize into the
per-driver views below.

## Per-driver specializations — the readonly construction-stratum projection

There is **one** `IoData` type; the "per-driver config records"
(`ElectrostaticConfig` / `MagnetostaticConfig` / `EigenmodeConfig` /
`DrivenConfig` in the feature-column vocabulary) are **projections** of the
same `iodata` object — the subset of fields each driver's operator factory
reads. Each driver constructs its operator graph by passing the whole
read-only `iodata` (plus the mesh) to its model-operator factory:

| driver (`ProblemType`) | construction capture site | reads (projection) |
|---|---|---|
| `ELECTROSTATIC`  | `LaplaceOperator laplace_op(iodata, mesh)` — `palace/drivers/electrostaticsolver.cpp:29` | `model`, `domains` (permittivity), `boundaries` (Dirichlet terminals), `solver.linear` |
| `MAGNETOSTATIC`  | `CurlCurlOperator curlcurl_op(iodata, mesh)` — `palace/drivers/magnetostaticsolver.cpp:29` | `model`, `domains` (permeability), `boundaries` (current sources), `solver.linear` |
| `EIGENMODE`      | `SpaceOperator space_op(iodata, mesh)` — `palace/drivers/eigensolver.cpp:39` | `model`, `domains`, `boundaries`, `solver.eigenmode` |
| `DRIVEN`         | `SpaceOperator space_op(iodata, mesh)` — `palace/drivers/drivensolver.cpp:41` | `model`, `domains`, `boundaries` (ports), `solver.driven` |
| `TRANSIENT`      | `SpaceOperator space_op(iodata, mesh)` — `palace/drivers/transientsolver.cpp:32` | `model`, `domains`, `boundaries`, `solver.transient` |

The projection is read-only and build-time: the factory consumes the relevant
fields once to build its operator, then the run-time iteration never touches
`iodata` again. This is exactly the construction/run-time split named in
[`build-time-vs-run-time-stratification`](./build-time-vs-run-time-stratification.md)
— config-record parsing + the per-driver factory reads are build-time
primitives; nothing in the config record is a run-time field.

## Signatures that name this record

Every feature column and operator factory whose signature names the config
record (the ≥2-consumer evidence for the standalone page):

- the spine-ROOT lifecycle column — `IoData iodata(argv[1], false)`
  (`main.cpp:231`) and the `problem.type` dispatch (`main.cpp:259`).
- the 5 driver-leaf feature columns — each `*Operator(iodata, mesh)` capture
  site above.
- `BaseSolver` and every `*Solver` ctor take `iodata` (`main.cpp:262-280`).
- model-operator factory ctors (`LaplaceOperator`, `CurlCurlOperator`,
  `SpaceOperator`) — each forward-declares `class IoData`
  (e.g. `palace/models/laplaceoperator.hpp:19`,
  `palace/models/spaceoperator.hpp:27`).

## See also

- [`build-time-vs-run-time-stratification`](./build-time-vs-run-time-stratification.md)
  — config-record parsing is the canonical build-time primitive; this page
  supplies the data shape that primitive consumes.
- The feature columns under `book/src/feature/` (electrostatic / magnetostatic
  / driven / transient / eigenmode / boundary-mode + the lifecycle ROOT) —
  these define the *behavior* over the config record; this page defines only
  its *shape*. **If this page and a feature column / the L0 source disagree on
  any factual claim about a field, the L0 source (`iodata.hpp` /
  `configfile.hpp`) wins.**
```

### 2. `book/src/concepts/index.md` — alpha-position `## Index` row

Inserted between `complex-from-real-lift` (primitive) and
`constructed-operator-factory` (layer-pattern). The `record` Kind value's
legend line is authored by the parallel D1 dispatch — NOT re-authored here;
this row REUSES it.

```edit:book/src/concepts/index.md
[old]:| [complex-from-real-lift](./complex-from-real-lift.md) | primitive |
| [constructed-operator-factory](./constructed-operator-factory.md) | layer-pattern |
[new]:| [complex-from-real-lift](./complex-from-real-lift.md) | primitive |
| [config-record](./config-record.md) | record |
| [constructed-operator-factory](./constructed-operator-factory.md) | layer-pattern |
```

### 3. `book/src/SUMMARY.md` — alpha-position concepts-block entry

Inserted between `complex-from-real-lift` and `constructed-operator-factory`.

```edit:book/src/SUMMARY.md
[old]:  - [complex-from-real-lift](./concepts/complex-from-real-lift.md)
  - [constructed-operator-factory](./concepts/constructed-operator-factory.md)
[new]:  - [complex-from-real-lift](./concepts/complex-from-real-lift.md)
  - [config-record](./concepts/config-record.md)
  - [constructed-operator-factory](./concepts/constructed-operator-factory.md)
```

## Supporting evidence

All citation anchors verified on-disk with `tools/citecheck/citecheck.py --anchor`
(codemap localization confirmed against the on-disk file; two anchors corrected
for codemap+1 drift):

- `palace/main.cpp:231` — `IoData iodata(argv[1], false)` [ok].
- `palace/main.cpp:259` — `switch (iodata.problem.type)` [ok] (prompt cited :258
  for the dispatch; the actual `switch` line is :259 — the `// Initialize the
  problem driver.` comment + lambda start sit at 256–258).
- `palace/utils/iodata.hpp:27-61` — `class IoData` aggregate (anchor `class
  IoData` at :27 [ok]); members `problem` :31, `model` :32, `domains` :33,
  `boundaries` :34, `solver` :35, `units` :38 (all [ok]); ctor
  `IoData(const char *filename, bool print)` :54 (corrected from codemap :52,
  +2 drift); `NondimensionalizeInputs` :60 (corrected from codemap :57, +3
  drift).
- `palace/utils/labels.hpp:18-26` — `enum class ProblemType : char` with the 6
  values [ok].
- `palace/utils/configfile.hpp:57` — `struct ProblemData` (default
  `ProblemType::DRIVEN` at :61) [ok]; `:156` — `struct ModelData` [ok];
  `:1026` — `struct SolverData` [ok].
- per-driver capture sites: `electrostaticsolver.cpp:29` (`LaplaceOperator
  laplace_op`, prompt cited :28 — actual :29, +1), `magnetostaticsolver.cpp:29`
  (`CurlCurlOperator curlcurl_op`), `eigensolver.cpp:39` /
  `drivensolver.cpp:41` / `transientsolver.cpp:32` (`SpaceOperator space_op`)
  — all [ok].

Cross-page reference target verified present:
`book/src/concepts/build-time-vs-run-time-stratification.md` (line 14 already
names "config-record parsing" as a build-time primitive — the reciprocal
linkage now resolves).

Absence verified: `book/src/concepts/config-record.md` and
`book/src/concepts/iodata.md` do not exist (planner-confirmed; re-verified).

## Open questions / caveats

- **Page slug `config-record` vs `iodata`.** The page is named `config-record`
  (the vocabulary-level name the feature columns use) rather than `iodata` (the
  C++ type name). The L0 type `IoData` is documented as the backing surface
  inside the page. If a future dispatch wants the type-name slug `iodata` as a
  redirect/alias, that is a separate (speculative) decision — not created here
  to avoid a thin duplicate. Flagged for the OQ ledger.
- **`DomainData` / `BoundaryData` struct line anchors not pinned.** I cited
  `iodata.hpp:33`/`:34` for the member declarations and the `configfile.hpp`
  struct lines for `ProblemData`/`ModelData`/`SolverData`, but did not pin the
  `struct DomainData` / `struct BoundaryData` definition lines in
  `configfile.hpp` (the member-declaration cite is sufficient for a data-shape
  page; the per-field interiors of domains/boundaries are large and belong to
  the materials/boundary feature-column work, not this top-level schema page).
  A future record-definition page for `DomainData` or `BoundaryData`
  specifically (if either clears the ≥2-consumer bar on its own) would pin
  those — noted but not in this scope.
- **Per-driver `*Config` are projections, not distinct types.** The feature-
  column vocabulary names `ElectrostaticConfig` / `DrivenConfig` etc.; the L0
  reality is one `IoData` with a `problem.type` selector and per-driver field
  subsets. The page states this explicitly (no separate C++ type per driver).
  If a feature column treats its `*Config` as a nominally distinct record, that
  column should down-link here rather than re-defining — a drift signal to
  watch, not an error to fix in scope.
