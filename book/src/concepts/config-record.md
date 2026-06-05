---
rank: firm
edges:
  depends-on:
    - target: palace/utils/iodata.hpp:31-60
      kind: cites-evidence            # the IoData aggregate (backing struct)
    - target: palace/utils/configfile.hpp:57-1026
      kind: cites-evidence            # the config:: sub-record structs
    - target: palace/utils/labels.hpp:18-26
      kind: cites-evidence            # the ProblemType driver-selector enum
  reference:
    - concepts/build-time-vs-run-time-stratification
    - feature/lifecycle.L4
    - feature/electrostatic.L4
    - feature/magnetostatic.L4
    - feature/driven.L4
    - feature/transient.L4
    - feature/eigenmode.L4
    - feature/boundary-mode.L4
    - feature/capacitance.L4
    - feature/inductance.L4
    - feature/sparameters.L4
    - feature/eigenfrequency-qfactor.L4
    - feature/energy-fields.L4
---

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
`BaseSolver` spans `palace/main.cpp:257-281`). The enum is
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

The **postprocess sub-records are projections of the same `IoData` tree**, not
separate config records. The output-product feature columns (capacitance /
inductance / sparameters / eigenfrequency-qfactor / energy-fields) name a config
input in their signatures — e.g. the `energy-fields` column's `PostprocessConfig`
is the **energy-postprocess domain-attribute set** `IoData.domains.postpro.energy`
(backed by `config::DomainPostData`, `palace/utils/configfile.hpp:283-295`, a
`std::map<int, DomainEnergyData> energy` at `:290`, each `DomainEnergyData`
`:263-270` carrying its per-index `attributes` list). These are readonly
construction-stratum sub-records of `domains.postpro` (`config::DomainData.postpro`,
`configfile.hpp:322`), the same `IoData` umbrella this page defines — so an
output-product column's `uses-record` edge resolves here, to the umbrella, rather
than to a per-postprocess-record page. (NOTE the name collision: the config-side
`config::DomainData` — `configfile.hpp:313-326`, the domains record this page's
schema lists — is unrelated to the run-time `Measurement::DomainData` result row
`postoperatorcsv.hpp:74-79` that the `energy-fields` column's output `[DomainData]`
names; the latter is a measurement-stratum result row, homed in-chapter, not here.)

## Signatures that name this record

Every feature column and operator factory whose signature names the config
record (the ≥2-consumer evidence for the standalone page):

- the spine-ROOT lifecycle column — `IoData iodata(argv[1], false)`
  (`palace/main.cpp:231`) and the `problem.type` dispatch (`palace/main.cpp:259`).
- the 5 driver-leaf feature columns — each `*Operator(iodata, mesh)` capture
  site above.
- `BaseSolver` and every `*Solver` ctor take `iodata` (`palace/main.cpp:262-280`).
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
