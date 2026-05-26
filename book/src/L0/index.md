# L0 — Cited Palace source ranges

Ground truth. The Palace C++ source, cited by `(file, start_line, end_line)`. No abstraction — this is what is.

## Context

L0 is not authored as prose in the book. It is **citations** that anchor L1 (and through the lowering chain, L2 / L3 / L4) to concrete code. Every claim higher in the stack carries an L0 citation as its evidence floor.

## Source organization

The target repository is `reference/palace/` (gitignored, local clone of <https://github.com/awslabs/palace>). Major regions:

- `palace/linalg/` — Krylov solvers (CG, GMRES, BICGSTAB), preconditioners, smoothers, orthogonalization
- `palace/fem/` — Finite-element discretization (assembly, integration, basis evaluation)
- `palace/models/` — Solver pipelines (electrostatic, magnetostatic, eigenmode, driven, transient)
- `palace/utils/` — IO, configuration, mesh handling
- `palace/main/` — Entry points per solver
- `palace/test/unit/` — Topic-keyed unittests (often the most authoritative semantic statement; see `scaffolding/test-linkages/`)

## Citation format

Plain text `relative/path/file.ext:start-end` (relative to `reference/`), e.g., `palace/linalg/cg.cpp:42-67`. Editors with line-aware navigation resolve against local clones. No markdown links — grep/IDE workflow is the navigation.

## Working Notes

- L0 cited-evidence pointers also live in the L1>L0 lowering theme entries (per-theme `evidence:` field).
- Negative-result citations (regions explicitly out of scope: MPI, `Par*` types) get noted in `scaffolding/decisions/` rather than the lowering themes.
