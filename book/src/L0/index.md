# L0 — Cited Palace source ranges + reference notes

Ground truth and its short interpretation overlay. L0 is **citations** that anchor higher layers to concrete code, **plus** a small set of cross-cutting reference notes that explain what L1 entries are actually referring to when they cite L0.

## Context

L0 is the evidence floor. Every claim higher in the stack carries an L0 citation as its anchor. Historically (slice-era), L0 also accumulated line-level prose duplication of source — too robust. The current organisation keeps L0 lean: **citations remain the primary content**, with a small companion set of reference-note chapters that capture cross-cutting Palace / MFEM idioms once, so L1 operator entries can point at them rather than re-state them inline.

The reference notes are not source paraphrases. They name conventions (output-arg vs receiver mutation, MFEM-vector type duality, free-function vs method-form symbols, transparent vs load-bearing optimisation tricks) and give file-level overviews of the two anchor files L1 references repeatedly (`linalg/vector.{hpp,cpp}`, `linalg/ksp.cpp`). Each chapter is 2–4 paragraphs of interpretation plus representative citations; no line-by-line transcription.

## Reference-note cohort

**Conventions** — cross-cutting Palace / MFEM idioms referenced by L1 entries:

- [`output-arg-vs-receiver`](./output-arg-vs-receiver.md) — `A.Mult(x, y)` writes `y` vs receiver-mutating `y.Add(α, x)` / `y *= s`; how L1 lifts both into pure-functional form.
- [`mfem-vector-types`](./mfem-vector-types.md) — `Vector` / `ComplexVector` duality (element-type axis); single-rank reading of `Par*` types per `CLAUDE.md` "Scope".
- [`linalg-free-functions`](./linalg-free-functions.md) — `linalg::AXPY` / `linalg::Dot` / `linalg::Norml2` as template-dispatch wrappers over the method-form surface; the wrapping pattern Palace uses across `vector.hpp`.
- [`transparent-vs-load-bearing-tricks`](./transparent-vs-load-bearing-tricks.md) — Operational L0 classification (lifted from `CLAUDE.md`): `α == 1.0` branch in `AXPY` is transparent; reduction-tree non-associativity is load-bearing. Worked examples from the BLAS-1 family.

**File overviews** — anchor files L1 references repeatedly:

- [`linalg-vector-file`](./linalg-vector-file.md) — `palace/linalg/vector.{hpp,cpp}` at a glance. The home of `ComplexVector`, the `AXPY/AXPBY/AXPBYPCZ` family, `Dot`/`TransposeDot`/`LocalDot`, `Norml2`, `Normalize`.
- [`ksp-factory-file`](./ksp-factory-file.md) — `palace/linalg/ksp.cpp` Krylov-solver factory. Enum-routed dispatch: CG / GMRES / FGMRES implemented; MINRES / BICGSTAB / DEFAULT abort. Anchor for the "advertised-but-unimplemented" pattern that drives the MINRES / BiCGStab obstruction themes.

## Source organization

The target repository is `reference/palace/` (gitignored, local clone of <https://github.com/awslabs/palace>). Major regions:

- `palace/linalg/` — Krylov solvers (CG, GMRES, BICGSTAB), preconditioners, smoothers, orthogonalization
- `palace/fem/` — Finite-element discretization (assembly, integration, basis evaluation)
- `palace/models/` — Solver pipelines (electrostatic, magnetostatic, eigenmode, driven, transient)
- `palace/utils/` — IO, configuration, mesh handling
- `palace/main/` — Entry points per solver
- `palace/test/unit/` — Topic-keyed unittests (often the most authoritative semantic statement; see `scaffolding/test-linkages/`)

## Citation format

Plain text `relative/path/file.ext:start-end` (relative to `reference/`), e.g., `palace/linalg/cg.cpp:42-67`. Editors with line-aware navigation resolve against local clones. No markdown links in citations — grep/IDE workflow is the navigation.

## Working Notes

- L0 cited-evidence pointers also live in the L1>L0 lowering theme entries (per-theme `evidence:` field).
- Negative-result citations (regions explicitly out of scope: MPI, `Par*` types) get noted in `scaffolding/decisions/` rather than the lowering themes.
- The reference-note cohort is **discipline-bound**: 2–4 paragraphs of interpretation + 3–6 representative citations per chapter; no line-by-line source duplication. When a reference note would need to grow past that, split it into a new chapter rather than expand the existing one.
- L1 operator `Context` sections that re-state any of the conventions chapters above are candidates for the cycle-005 retroactive-thinning sweep (priority #11) — the convention chapters' `Referenced from:` backlinks identify them.
