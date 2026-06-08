---
rank: firm
kind: record
edges:
  depends-on:
    - target: palace/drivers/boundarymodesolver.cpp:272-340
      kind: cites-evidence
    - target: palace/models/modeeigensolver.cpp:516-519
      kind: cites-evidence
  reference:
    - L4/waveguide_mode_reduce
    - feature/waveguide-mode.L4
    - feature/waveguide-mode.L1
    - feature/boundary-mode.L4
    - concepts/config-record
---

# WaveguideModeTable

> **Kind: `record`.** This page defines the *data shape* of `WaveguideModeTable` — its row
> schema, the per-field types and meaning, the construction-vs-run-time stratum, and the L0
> readout source it mirrors. The *behaviour* — how [`waveguide_mode_reduce`](../L4/waveguide_mode_reduce.md)
> constructs it from the boundary-mode eigenpair family — lives in that operator chapter; this
> page does not restate that reduction algebra.

`WaveguideModeTable` is the **boundary-mode (2D waveguide-mode analysis) output product**: a
per-mode table characterizing each converged propagation mode. One row per converged mode, each
`{kn, n_eff, (Et, En, Bz)}` — the propagation constant `kn`, the effective index `n_eff = kn/ω`,
and the mode-field triple `(Et, En, Bz)` (the transverse H(curl) field `Et`, the longitudinal H1
field `En`, and, for propagating modes only, the longitudinal magnetic field
`Bz = curl(Et)/(iω)`). It is the physical product the user runs the boundary-mode solver to
obtain. It is **produced** by [`waveguide_mode_reduce`](../L4/waveguide_mode_reduce.md)
(`waveguide_mode_reduce :: EigResult -> Scalar -> WaveguideModeTable`) and named in the signatures
of the [`waveguide-mode.L4`](../feature/waveguide-mode.L4.md) and
[`waveguide-mode.L1`](../feature/waveguide-mode.L1.md) feature columns. Three distinct
signature-naming chapters (the standalone reduce-verb chapter + the two column levels) put it
above the ≥2-consumer bar, so it has a cross-cutting definition home here.

## One-line semantics

`WaveguideModeTable` is an immutable per-mode list — one row per converged waveguide mode, each
mixing complex propagation scalars (`kn`, `n_eff`) with rank-1 mode-field dof-vectors
(`Et`, `En`, `Bz`). It carries no algebra of its own; the reduce verb supplies all behaviour.

## Record definition

`WaveguideModeTable` is a list of per-mode rows. The TS brace form (each row immutable,
constructed by the per-mode reduce):

```text
WaveguideModeTable = [ WaveguideModeRow ]

WaveguideModeRow = {
  kn   : Complex,                          -- propagation constant
  n_eff: Complex,                          -- effective index = kn / ω
  Et   : Tensor[N_nd,   complex],          -- transverse H(curl) mode field (flat ND dof-vector)
  En   : Tensor[N_h1,   complex],          -- longitudinal H1 mode field    (flat H1 dof-vector)
  Bz   : Maybe (Tensor[N_curl, complex])   -- longitudinal B (propagating modes only)
}
```

| field | type | meaning | stratum | L0 source |
|---|---|---|---|---|
| `kn` | `Complex` | propagation constant — the shift-invert un-transform of the eigenvalue (`eig.GetPropagationConstant(i)`) | construction (readout) | `palace/drivers/boundarymodesolver.cpp:299` (un-transform), `:274` (reported) |
| `n_eff` | `Complex` | effective index `= kn / ω` | construction (readout) | `palace/drivers/boundarymodesolver.cpp:276` |
| `Et` | `Tensor[N_nd, complex]` | transverse H(curl) mode field — the VD-back-transform of the eigenvector, power-normalized so `|P| = 1` (genuine flat rank-1 dof-vector on the 2D-submesh ND space) | construction (readout) | `palace/drivers/boundarymodesolver.cpp:300` (`ApplyVDBackTransform`), `:304-307` (normalize) |
| `En` | `Tensor[N_h1, complex]` | longitudinal H1 mode field — the H1 component of the same VD-back-transform (flat rank-1 dof-vector on the 2D-submesh H1 space) | construction (readout) | `palace/drivers/boundarymodesolver.cpp:300` |
| `Bz` | `Maybe (Tensor[N_curl, complex])` | longitudinal magnetic field `Bz = curl(Et)/(iω)` — present (`Just`) only for propagating modes (`IsPropagating(kn)`), `Nothing` for evanescent | construction (readout) | `palace/drivers/boundarymodesolver.cpp:316-333` (formation), `palace/models/modeeigensolver.cpp:516-519` (`IsPropagating` predicate) |

The mode fields `Et` / `En` / `Bz` are **genuine flat rank-1 dof-vectors** on the 2D-submesh ND /
H1 / curl spaces — `Tensor[N]` is correct here per the semantic surface
[`semantics`](../semantics/index.md) §1.2.1 (NOT a named shape group); `kn` / `n_eff` are complex
scalars; `Bz` is `Maybe` (propagating modes only). The element-type is **pinned complex** —
waveguide modes are intrinsically complex (`kn` / `n_eff` / `(Et,En,Bz)` all complex).

## Stratum — construction-time (readout), immutable

`WaveguideModeTable` is **construction-stratum**: each row is materialized once by the per-mode
readout of the converged boundary-mode eigenpair family (after the single `eigsolve`), then read
as the final product. There is no per-iteration solve-time mutation — the reduction is a pure
`map`-then-collect over the eigenpair family with no inter-mode state (the readout loop carries no
accumulator). The whole table is the output of one reduction at a single operating frequency ω
(ω rides as a fixed scalar parameter, not a per-mode datum — the `n_eff` divisor + the `Bz` `1/ω`
scale). This is the [`build-time-vs-run-time-stratification`](./build-time-vs-run-time-stratification.md)
output-product side: the table is the constructed result, not run-time iteration scaffolding.

## L0 source home — the boundary-mode readout loops

The backing L0 surface is the boundary-mode driver's two per-mode readout loops
(`palace/drivers/boundarymodesolver.cpp:272-340`): the `kn` / `n_eff` print loop (`:272-278`) and
the field-readout + `Bz`-formation loop (`:292-335`). Palace materializes the rows imperatively
into per-mode `kn` / `(et, en)` / `Bz` values reported through `post_op.MeasureAndPrintAll(...)`
(`:314`); it does not name a single C++ struct for the whole table — `WaveguideModeTable` is the
lifted record of that scattered per-mode readout. The `IsPropagating` predicate that keys the
`Bz` `Maybe` is `ModeEigenSolver::IsPropagating(kn)` (`palace/models/modeeigensolver.cpp:516-519`:
`|kn.imag()| < 0.1·|kn.real()| ∧ |kn.real()| > 0`). The config-relevant `IoData` surface is
`iodata.solver.boundary_mode` (the operating frequency → ω, the boundary attributes → the
2D-submesh, the mode counts → the table rows) — cross-ref [`config-record`](./config-record.md).

## Signatures that name this record

The ≥2-consumer evidence for the standalone page (three signature consumers):

- [`waveguide_mode_reduce`](../L4/waveguide_mode_reduce.md) — the **producer** (L4 reduce verb):
  `waveguide_mode_reduce :: EigResult -> Scalar -> WaveguideModeTable`.
- [`waveguide-mode.L4`](../feature/waveguide-mode.L4.md) — the output-product composition root:
  `waveguide_mode :: BoundaryModeConfig -> WaveguideModeTable`
  (`book/src/feature/waveguide-mode.L4.md:30`).
- [`waveguide-mode.L1`](../feature/waveguide-mode.L1.md) — the L1 column:
  `waveguide_mode :: BoundaryModeConfig -> WaveguideModeTable`
  (`book/src/feature/waveguide-mode.L1.md:26`).

## See also

- [`waveguide_mode_reduce`](../L4/waveguide_mode_reduce.md) — the producer; defines HOW each row
  is constructed (eigenvalue un-transform → `kn`, `n_eff = kn/ω`, VD back-transform → `(Et, En)`,
  Poynting power-normalization, conditional curl `Bz`). This page defines only the *shape* of its
  output.
- [`waveguide-mode.L4`](../feature/waveguide-mode.L4.md) /
  [`waveguide-mode.L1`](../feature/waveguide-mode.L1.md) — the feature columns; define the
  *composition* that produces the table (reduce ∘ boundary-mode driver). This page does NOT
  restate that composition.
- [`boundary-mode.L4`](../feature/boundary-mode.L4.md) — the producing driver column (the 2D-submesh
  eigenpair family the reduction consumes).
- [`config-record`](./config-record.md) — the `iodata.solver.boundary_mode` surface (ω + boundary
  attributes + mode counts) the table's construction reads from.

**If this page and a consumer chapter / the L0 source disagree on any factual claim about the
record, the L0 source (`palace/drivers/boundarymodesolver.cpp` / `palace/models/modeeigensolver.cpp`)
wins and this page is corrected.**
