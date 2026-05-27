---
agent: layer-intro-author
invoked_at: 2026-05-27T025354Z
scope: L0 reference-notes bootstrap (bundle 1)
status: integrated
integrated_at: 2026-05-27T07:04:24Z
integration_commit: a16c32c76f7ed73c2ab1d381d440db2cd6b2e7f9
integration_notes: Applied. Bundle 1 of multi-cycle L0 buildout per priority #10. 6 chapters + L0/index.md re-framed as citations + reference notes. Folded the bicgstab :53-56 to :53-57 cross-reference fix from the resume-notes flag.
---

# REPORT: L0 reference-notes bootstrap — bundle 1

## Summary

User directive (priorities #10): the L0 layer is currently a 30-line stub. The prior slice-era stack carried over-robust L0 prose (line-level duplication); the current stack swung too far the other way ("look at the source"). This bundle bootstraps a **middle path**: short interpretation chapters that L1 entries can reference, anchored by representative citations rather than line-by-line transcription.

This report authors **6 starter L0 chapters** plus a refresh of `book/src/L0/index.md`, and registers the new chapters in `book/src/SUMMARY.md`.

Chapter set:

- **Conventions (4):** `output-arg-vs-receiver`, `mfem-vector-types`, `linalg-free-functions`, `transparent-vs-load-bearing-tricks`.
- **File overviews (2):** `linalg-vector-file` (`palace/linalg/vector.{hpp,cpp}`), `ksp-factory-file` (`palace/linalg/ksp.cpp`).

Each chapter follows the discipline: 2–4 paragraphs of interpretation, 3–6 representative citations, and (for the 4 conventions chapters) a `Referenced from:` backlink list pointing at L1 operator pages whose `Context` sections re-state the same convention. The backlink lists are the seam for the cycle-005 retroactive-thinning sweep (priority #11).

The L0 index refresh adds: (i) a one-paragraph reframing of the layer as "cited evidence + cross-cutting reference notes", (ii) a chapter index split into "Conventions" and "File overviews" cohorts (mirroring the Vocabulary-cohort pattern), (iii) a preserved "Citation format" rule.

## Proposed changes

```edit:book/src/L0/index.md
[old]: # L0 — Cited Palace source ranges

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
[new]: # L0 — Cited Palace source ranges + reference notes

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
```

```edit:book/src/L0/output-arg-vs-receiver.md
[old]:
[new]: # Convention — output-argument vs receiver mutation

A reference note for L1 entries. The Palace L0 surface has **two distinct in-place mutation idioms**; L1 lifts both to the same pure-functional form, but the lowering theme reintroduces the right one.

## The two idioms

**Output-argument mutation.** The mutated buffer appears as a non-const reference parameter, conventionally the *last* one. The function name is verb-like and the call reads "compute into the trailing buffer."

- `A.Mult(x, y)` — applies the operator to `x`, writes the result into `y` (`palace/linalg/operator.hpp:54` declaration for `ComplexOperator::Mult`; instances at `palace/linalg/iterative.cpp:379, 443`). The operator `A` is the receiver but is `const`; the *output* is the explicit argument.
- `add(α, x, β, y, z)` — MFEM 5-arg out-of-place additive combine; writes `z = α·x + β·y` (used at `palace/linalg/vector.cpp:751` as the `AXPBYPCZ` real-real `γ == 0` fast-path; also reused as `add(α, x, β, y, y)` at `palace/linalg/vector.cpp:729` for the `AXPBY` real-real path, where the output buffer aliases one of the inputs deliberately).

**Receiver mutation.** The mutated buffer is the implicit `*this`. The method name reads "mutate self" rather than "compute into something."

- `y.Add(α, x)` — `y += α·x`, mutating `y` (MFEM `Vector::Add`; aliased on `ComplexVector` at `palace/linalg/vector.hpp:117` as `Add(α, x) { AXPY(α, x); }`). Used at `palace/linalg/operator.cpp:458-466` inside `SumOperator::AddMult` to accumulate scaled operator outputs.
- `y.AXPY(α, x)` — equivalent to `Add` on `ComplexVector` (`palace/linalg/vector.hpp:116`). The method-form name explicitly matches the BLAS-1 symbol.
- `y += x` and `y -= x` — operator-overload form (`palace/linalg/vector.hpp:119-128`); also receiver mutation. Internally calls `AXPY(±1.0, x)`.
- `x *= s` — receiver-mutating scaling (`palace/linalg/vector.hpp:99`). MFEM provides the analogue on real `Vector`; Palace's overload handles `std::complex<double>` and branches on `s.imag() == 0.0` (`palace/linalg/vector.cpp:203-227`).
- `y.AXPBY(α, x, β)` and `y.AXPBYPCZ(α, x, β, y2, γ)` — fused receiver-mutating updates (`palace/linalg/vector.hpp:131, 134-136`).

## How L1 lifts both

The L1 form names the operator by its *algebraic action*, not its mutation idiom:

- `axpy(α, x, y) = α·x + y` — pure functional; no destination buffer in the signature. Lifts both `y.Add(α, x)` (receiver) and `linalg::AXPY(α, x, y)` (output-arg) to the same operator.
- `apply_linop(A, x) = A·x` — pure functional; no destination buffer. Lifts `A.Mult(x, y)` (output-arg).
- `scal(α, x) = α·x` — pure functional. Lifts `x *= s` (receiver).

The L1>L0 lowering theme is where the destination-buffer mention reappears and the receiver-vs-output-arg distinction reasserts itself. At L1 the distinction is erased; the algebraic laws apply uniformly.

## Why both idioms exist

Output-argument mutation is the dominant idiom when the operation is a *transformation* (`A·x` is conceptually "apply A to produce a new value"; the output buffer is a workspace concern, not the conceptual receiver). Receiver mutation is the dominant idiom when the operation is conceptually a *self-update* (`y += α·x` reads naturally as "increment `y`"). The split is a C++ ergonomic choice, not a semantic one. The L1 algebra has neither — every L1 operator is a function with explicit input and output sets.

## Referenced from

*Forward-declared; L1 pages will be thinned to reference this chapter in the cycle-006 retroactive-thinning sweep (priority #11).*

- [`L1/axpy`](../L1/axpy.md) — receiver `y.Add(α, x)` vs output-arg `linalg::AXPY(α, x, y)`.
- [`L1/axpby`](../L1/axpby.md) — receiver `y.AXPBY(α, x, β)` vs output-arg `linalg::AXPBY(α, x, β, y)`.
- [`L1/axpbypcz`](../L1/axpbypcz.md) — receiver `z.AXPBYPCZ(α, x, β, y, γ)` vs output-arg `linalg::AXPBYPCZ(α, x, β, y, γ, z)`.
- [`L1/scal`](../L1/scal.md) — receiver `x *= s` (no output-arg form in Palace).
- [`L1/apply_linop`](../L1/apply_linop.md) — output-arg `A.Mult(x, y)`.
```

```edit:book/src/L0/mfem-vector-types.md
[old]:
[new]: # Convention — MFEM vector types and the element-type axis

A reference note for L1 entries. Palace's vector surface has two element types (real, complex) and a parallel-wrapper axis (`Par*` types) that the current scope reads as a no-op.

## The two element types

`Vector` (real) is the MFEM type, re-exported at `palace/linalg/vector.hpp:20`:

```cpp
using Vector = mfem::Vector;
```

`ComplexVector` (complex) is a Palace class defined at `palace/linalg/vector.hpp:23-147`. Its internal representation is **two real `Vector`s** — one for the real part, one for the imaginary part — declared at `palace/linalg/vector.hpp:25-26`:

```cpp
private:
  Vector xr, xi;
```

This split representation has a consequence visible in nearly every `ComplexVector` method body: complex operations decompose into four real operations on the `(xr, xi)` pair (e.g. `ComplexVector::Dot` at `palace/linalg/vector.cpp:263-267` computes `(xr·yr + xi·yi)` for the real part and `(xi·yr − xr·yi)` for the imaginary part — four invocations of `mfem::Vector::operator*` (real-Dot) combined: `Real() * y.Real()`, `Imag() * y.Imag()`, `Imag() * y.Real()`, `Real() * y.Imag()`). The complex-shape kernel is not a single SIMD lane of complex arithmetic; it is a real-pair kernel with the cross-term algebra explicit.

`StaticVector<N>` (`palace/linalg/vector.hpp:177-194`) is a stack-allocated subclass of `Vector` with compile-time fixed size — used for small fixed-shape vectors like 3D Cartesian coordinates. It does not introduce a new element-type axis; it is a `Vector` with a stack-backed buffer.

## The element-type axis at L1

At L1 the element-type axis collapses to a single `Tensor[N]` (with element-type parameter `real | complex`). The Palace L0 surface has separate overloads / specialisations / class hierarchies for each element type:

- Real free-function: `template<> void AXPY(double, const Vector&, Vector&)` at `palace/linalg/vector.cpp:701-712`.
- Complex free-function: `template<> void AXPY(std::complex<double>, const ComplexVector&, ComplexVector&)` at `palace/linalg/vector.cpp:720-724`.
- Real-scalar-on-complex-vector overload: `template<> void AXPY(double, const ComplexVector&, ComplexVector&)` at `palace/linalg/vector.cpp:714-718` (implicit scalar promotion).

L1 names one `axpy` operator and absorbs the element-type axis into the type parameter; the scalar-promotion sub-axis is tracked under open question `scalar-promotion-typing-rule`.

## The `Par*` axis (single-rank reading)

Per `CLAUDE.md` "Scope", MPI / multi-rank distribution is out of scope; `Par*` types (`ParGridFunction`, `ParBilinearForm`, `HypreParVector`, `ParOperator`, …) are read as their single-rank equivalents. Palace's `ParOperator::Mult` at `palace/linalg/rap.cpp:195-234` wraps an inner operator with prolongation / restriction and Dirichlet-BC tdof masking; under the single-rank reading the prolongation and restriction collapse to identity, and the inner-operator-plus-BC-masking is what remains.

The element-type duality and the `Par*` axis are **orthogonal**: there is a `ParOperator` (real) and a `ComplexParOperator` (complex). The `LocalDot` vs `Dot` split at `palace/linalg/vector.hpp:242-253` likewise factors: `LocalDot` is the single-rank kernel, `Dot` adds `Mpi::GlobalSum` over the local result. L1 names the global form and the single-rank reading reduces the `MPI_Allreduce` to a no-op; the L1>L0 lowering reintroduces the local-then-collective two-step.

## Referenced from

*Forward-declared; L1 pages will be thinned to reference this chapter in the cycle-006 retroactive-thinning sweep (priority #11).*

- [`L1/axpy`](../L1/axpy.md), [`L1/axpby`](../L1/axpby.md), [`L1/axpbypcz`](../L1/axpbypcz.md), [`L1/scal`](../L1/scal.md) — element-type axis collapse.
- [`L1/dot`](../L1/dot.md), [`L1/nrm2`](../L1/nrm2.md) — element-type axis + `LocalDot` vs `Dot` (MPI collective) split.
- [`L1/apply_linop`](../L1/apply_linop.md) — `Operator` vs `ComplexOperator` hierarchy split; `ParOperator` wrapping.
```

```edit:book/src/L0/linalg-free-functions.md
[old]:
[new]: # Convention — `linalg::` free functions as template-dispatch wrappers

A reference note for L1 entries. Palace's `linalg::` namespace (declared inside `palace/linalg/vector.hpp:196` onward) exposes BLAS-1-shaped operations as **free-function templates** parameterised by vector type and scalar type. These wrappers are the call-site-friendly surface; underneath they dispatch into method-form or MFEM-form kernels.

## The wrapping pattern

A `linalg::` free function typically:

1. **Declares a template** parameterised by `VecType` (and sometimes `ScalarType`).
2. **Defines an inline body** for the common scaffold (e.g. local kernel + `MPI_Allreduce`), if the operation factors that way.
3. **Forward-declares specialisations** for each `(VecType, ScalarType)` combination, with definitions in `vector.cpp`.

Three representative shapes:

**Pure forward to method-form.** `linalg::AXPY` (`palace/linalg/vector.hpp:305-307`, definitions at `palace/linalg/vector.cpp:701-724`) is a free-function template with explicit specialisations for `(Vector, double)`, `(ComplexVector, std::complex<double>)`, and `(ComplexVector, double)`. The real-real specialisation has a constant-folding branch (`if (alpha == 1.0)`) and delegates to MFEM's `y += x` or `y.Add(α, x)`; the complex specialisations delegate to the method-form `y.AXPY(α, x)`.

**Composed scaffold.** `linalg::Dot` (`palace/linalg/vector.hpp:247-253`) is an inline template that composes `linalg::LocalDot` with `Mpi::GlobalSum`:

```cpp
template <typename VecType>
inline auto Dot(MPI_Comm comm, const VecType &x, const VecType &y)
{
  auto dot = LocalDot(x, y);
  Mpi::GlobalSum(1, &dot, comm);
  return dot;
}
```

The scaffold (local-then-collective) is shared across `VecType`; only `LocalDot` is specialised per element type (`palace/linalg/vector.hpp:242-244`; definitions at `palace/linalg/vector.cpp:665-685`).

**One-line composition.** `linalg::Norml2` (`palace/linalg/vector.hpp:255-260`) is a one-line composition `return std::sqrt(std::abs(Dot(comm, x, x)));` — the entire body. The element-type axis is absorbed by `Dot`; the outer `sqrt` and `abs` are scalar operations.

## Why the wrapping pattern matters

The free-function surface gives L1 a single algebraic name (e.g. `axpy(α, x, y)`) regardless of element type — the template-specialisation machinery handles the dispatch invisibly. L1 operator entries cite both the free-function declaration and the method-form definition because they are the same operator under two L0 spellings.

A few `linalg::` symbols are **not** wrappers but defined operations in their own right:

- `linalg::Normalize` (`palace/linalg/vector.hpp:262-270`) — composes `Norml2` and `*=` to return the original norm and rescale in place. A fused construct, not a wrapper.
- `linalg::LocalSum` / `linalg::Sum` / `linalg::Mean` / `linalg::NormalizePhase` (`palace/linalg/vector.hpp:272-303`) — reduction utilities; the `Sum` / `Mean` family follows the same `LocalSum` + `Mpi::GlobalSum` scaffold as `Dot`.
- `linalg::SetSubVector` / `linalg::SetRandom` (`palace/linalg/vector.hpp:220-240`) — mutation utilities; no method-form analogue.

Notable absence: **there is no `linalg::Scal` or `linalg::Scale` symbol.** Scaling is performed exclusively through the receiver-mutating `operator*=` method-form (per [`output-arg-vs-receiver`](./output-arg-vs-receiver.md) and [`L1/scal`](../L1/scal.md)). The L1 `scal` operator therefore has only the method-form anchor at L0.

## Referenced from

*Forward-declared; L1 pages will be thinned to reference this chapter in the cycle-006 retroactive-thinning sweep (priority #11).*

- [`L1/axpy`](../L1/axpy.md), [`L1/axpby`](../L1/axpby.md), [`L1/axpbypcz`](../L1/axpbypcz.md) — `linalg::AXPY` / `linalg::AXPBY` / `linalg::AXPBYPCZ` free-function-template wrappers over method-form.
- [`L1/dot`](../L1/dot.md) — `linalg::Dot` composing `LocalDot` + `Mpi::GlobalSum`; method-form `ComplexVector::Dot`.
- [`L1/nrm2`](../L1/nrm2.md) — `linalg::Norml2` as one-line composition `sqrt(abs(Dot(x, x)))`.
- [`L1/scal`](../L1/scal.md) — no free-function form (notable absence); `operator*=` only.
```

```edit:book/src/L0/transparent-vs-load-bearing-tricks.md
[old]:
[new]: # Convention — transparent vs load-bearing optimisation tricks

A reference note for L1 entries. Adapted from `CLAUDE.md` "Optimization tricks vs. base algebra". Operational L0 classification with worked examples from the BLAS-1 family that L1 references repeatedly.

A significant fraction of Palace's C++ exists because it was tuned for CPU + cache + SIMD. That cost model is not burn's, and most of the resulting code shape is counter to the goals of a pure GPU tensor implementation. L0 has two distinct categories of optimisation:

## Transparent performance tricks

Algebraically equivalent to their unfolded form; can be erased at L1 with a one-line note in the L1>L0 lowering. Worked examples:

- **Constant-folding fast paths.** `AXPY(double, Vector, Vector)` at `palace/linalg/vector.cpp:701-712` branches on `alpha == 1.0` and calls `y += x` instead of `y.Add(α, x)`. Both forms compute the same `y_new = α·x + y`; the branch saves one scalar-multiply per element. The L1 `axpy` operator names a single algebraic update; the `α == 1.0` branch disappears at L1 (recorded in [`L1/axpy`](../L1/axpy.md) "L1 vs L0 distinction").
- **Shape-specialisation branches.** `ComplexVector::operator*=` at `palace/linalg/vector.cpp:203-227` branches on `s.imag() == 0.0` and runs two real `operator*=` calls instead of the four-term complex fused kernel. Algebraically `(sr + 0i)·x = sr·x` exactly; the shape branch is a complex-arithmetic specialisation, not a value specialisation. Disappears at L1 (recorded in [`L1/scal`](../L1/scal.md)).
- **Self-aliasing fast paths.** `ComplexVector::Dot` at `palace/linalg/vector.cpp:266` returns imaginary part `0.0` directly when `&y == this`, because `xᴴ x` has zero imaginary part exactly in exact arithmetic. The L1 `dot` law 9 (Hermitian self-dot is real non-negative) subsumes this; the branch is transparent.
- **Out-of-place vs split-call fused updates.** `AXPBYPCZ(double, Vector, ...)` at `palace/linalg/vector.cpp:745-758` branches on `gamma == 0` to dispatch either MFEM's `add(α, x, β, y, z)` (one-call) or the split-call form `AXPBY(α, x, γ, z); z.Add(β, y)`. Both compute the same `z_new`; the split form recovers when `γ ≠ 0` requires the prior `z` to participate. Algebraically equivalent; the choice is a control-flow specialisation that disappears at L1.
- **Skipping zero-initialisation.** `SumOperator::Mult` at `palace/linalg/operator.cpp:428-441` zeros `y` then calls `AddMult` for the multi-operator path; the `AddMult` form skips the zero-init. The L1 composition `apply_linop` + `axpby` subsumes both; the fusion of "zero `y`, accumulate" into a single `Mult` call is transparent at L1 (recorded in [`L1/apply_linop`](../L1/apply_linop.md)).

## Load-bearing numerical tricks

**Part of the algorithm.** Preserve as explicit algebraic claims with the property they buy (determinism, condition-number, IEEE compliance) called out. Worked examples:

- **Reduction-tree non-associativity.** Floating-point summation is non-associative: `(a + b) + c ≠ a + (b + c)` at the bit level in IEEE-754. Palace's `linalg::Dot` (`palace/linalg/vector.hpp:247-253`) pins a specific reduction tree via the underlying Hypre kernel + `MPI_Allreduce` topology. A different reduction tree produces a different scalar at the bit level even though all are valid implementations of the L1 operator. Recorded as a load-bearing non-law at [`L1/dot`](../L1/dot.md) and propagated to [`L1/nrm2`](../L1/nrm2.md) (`nrm2(x) = √dot(x, x)` inherits `dot`'s reduction tree).
- **Defensive non-negativity guard.** `linalg::Norml2` at `palace/linalg/vector.hpp:255-260` is `return std::sqrt(std::abs(Dot(comm, x, x)));`. The outer `std::abs` is **not** a semantic projection — `dot(x, x)` is non-negative real in exact arithmetic for both real and complex (per `dot` laws 4 and 9). The `abs` defends against floating-point round-off pushing the sum slightly negative. At L1 this is recorded as a load-bearing implementation detail: the algebraic claim `dot(x, x) ≥ 0` subsumes the guard, but in IEEE-754 the guard is what makes the implementation robust.
- **Matrix-free element-summation order.** For matrix-free operator applies (MFEM partial-assembly, libCEED, Hypre SpMV) the per-element summation order is pinned by the underlying kernel. A different order gives a different bit-level output. Recorded as a load-bearing non-law at [`L1/apply_linop`](../L1/apply_linop.md).
- **`std::sqrt` itself is deterministic.** IEEE-754 correctly-rounded square root has a unique answer for any well-defined input. So `nrm2`'s non-determinism is entirely the inner `dot`'s; the outer `sqrt` adds no new non-determinism.

## Classification heuristic

A trick is **transparent** if and only if the L1 algebraic statement subsumes it without losing information. A trick is **load-bearing** if it pins a choice (reduction order, evaluation order, fused vs split rounding) that affects the bit-level output even when all variants are valid implementations of the same L1 operator.

When in doubt, the critic flags as `unclear` and the human triages. Mis-classifying a load-bearing trick as transparent silently changes the algorithm.

## Referenced from

*Forward-declared; L1 pages will be thinned to reference this chapter in the cycle-006 retroactive-thinning sweep (priority #11).*

- [`L1/axpy`](../L1/axpy.md) — `α == 1.0` fast path (transparent).
- [`L1/scal`](../L1/scal.md) — `s.imag() == 0.0` shape branch (transparent).
- [`L1/dot`](../L1/dot.md) — self-aliasing fast path (transparent); reduction-tree non-associativity (load-bearing).
- [`L1/nrm2`](../L1/nrm2.md) — `std::abs` defensive guard (load-bearing); inherited reduction-tree non-associativity (load-bearing).
- [`L1/axpby`](../L1/axpby.md) — fused vs split-pass rounding (load-bearing for bit-reproduction).
- [`L1/axpbypcz`](../L1/axpbypcz.md) — `γ == 0` control-flow branch (transparent); cross-branch summation-order divergence (load-bearing for bit-reproduction).
- [`L1/apply_linop`](../L1/apply_linop.md) — skipped zero-init in `AddMult` (transparent); matrix-free element-summation order (load-bearing).
```

```edit:book/src/L0/linalg-vector-file.md
[old]:
[new]: # File — `palace/linalg/vector.{hpp,cpp}`

A file-overview reference note for L1 entries. The home of Palace's vector surface. L1 entries cite into this file more than any other; this overview names the file's main regions so an L1 entry can refer to "the AXPBYPCZ family in `vector.cpp`" without re-citing every overload.

## At a glance

**Header (`palace/linalg/vector.hpp`).** Three main sections:

1. **The `Vector` type alias and the `ComplexVector` class** (lines 1–147). `using Vector = mfem::Vector;` at line 20 re-exports MFEM's real vector. `ComplexVector` is declared at lines 23–147 — a Palace class holding two real `Vector`s (lines 25–26) and exposing the in-place mutation surface: `operator*=` (line 99), `Conj` / `Abs` / `Reciprocal` (lines 102–108), `Dot` / `TransposeDot` / `operator*` (lines 110–113), `AXPY` / `Add` / `Subtract` / `operator+=` / `operator-=` (lines 115–128), and the fused updates `AXPBY` (line 131), `AXPBYPCZ` (lines 133–136). Also `StaticVector<N>` (lines 177–194) — stack-allocated `Vector` subclass with compile-time fixed size.

2. **The `linalg::` namespace** (lines 196 onward). Free-function templates parameterised by `VecType` (and sometimes `ScalarType`). The two main families:
   - **Reductions and norms** — `GlobalSize` / `GlobalSize2` (lines 200–215); `LocalDot` declarations (lines 242–244); `Dot` template scaffold (lines 247–253); `Norml2` one-liner (lines 255–260); `Normalize` fused `nrm2 + scal` (lines 262–270); `LocalSum` / `Sum` / `Mean` / `NormalizePhase` (lines 272–303).
   - **Element-wise mutations** — `SetSubVector` family (lines 220–231); `SetRandom` / `SetRandomReal` / `SetRandomSign` (lines 235–240); `AXPY` / `AXPBY` / `AXPBYPCZ` template declarations (lines 305–316); `Sqrt` (line 320); `Cross2` / `Cross3` (lines 322 onward).

3. **MFEM-pattern utilities** at the bottom of the header (small-vector cross products, etc., from line 322 onward).

**Source (`palace/linalg/vector.cpp`).** Contains the `ComplexVector` method definitions and the `linalg::` free-function template specialisations. The L1 BLAS-1 family is anchored here:

- `ComplexVector::operator*=` definition with the `s.imag() == 0.0` shape branch (lines 203–227).
- `ComplexVector::Dot` / `TransposeDot` definitions, with self-aliasing fast paths (lines 263–274).
- `linalg::LocalDot` real and complex definitions (lines 665–685).
- `linalg::LocalSum` definitions (lines 696–699).
- The `linalg::AXPY` family — three specialisations (lines 701–724), with the real-real `α == 1.0` constant-folding branch.
- The `linalg::AXPBY` family — three specialisations (lines 726–743), all delegating to MFEM's `add(α, x, β, y, y)` or to the `ComplexVector::AXPBY` member.
- The `linalg::AXPBYPCZ` family — three specialisations (lines 745–772), with the real-real `γ == 0` control-flow branch.

## The BLAS-1 fused-update family

`AXPY` → `AXPBY` → `AXPBYPCZ` form a generalisation chain: each adds one more scalar-vector pair. Palace exposes both member-form and free-function-form for each; the L1 operators `axpy`, `axpby`, `axpbypcz` lift this entire family. The subsumption chain `axpy ≺ axpby ≺ axpbypcz` is algebraic at L1 (each generalises the prior with one more pair) but **not** a dependency chain — all three are L1 leaves; see the decision record at `scaffolding/decisions/axpby-as-primitive.md`.

The only constant-folding branches in the family are `AXPY(double, …)`'s `α == 1.0` branch (line 704) and `AXPBYPCZ(double, …)`'s `γ == 0` branch (line 749). Neither `AXPBY` nor the complex specialisations of `AXPBYPCZ` constant-fold; they uniformly delegate (see [`transparent-vs-load-bearing-tricks`](./transparent-vs-load-bearing-tricks.md) for the classification).

## The reduction family

`Dot` / `TransposeDot` / `Norml2` / `Normalize` form a tight cluster. The base primitive is `LocalDot` (real and complex). `Dot` adds `Mpi::GlobalSum`; `Norml2` composes `sqrt(abs(Dot(x, x)))`; `Normalize` composes `Norml2` and `operator*=` to return the original norm and rescale in place. The single load-bearing line is `linalg::Norml2`'s body (header line 259) — one line of source that anchors an entire L1 norm operator.

## Referenced from

- [`L1/axpy`](../L1/axpy.md), [`L1/axpby`](../L1/axpby.md), [`L1/axpbypcz`](../L1/axpbypcz.md), [`L1/scal`](../L1/scal.md), [`L1/dot`](../L1/dot.md), [`L1/nrm2`](../L1/nrm2.md) — all six current L1 BLAS-1 / BLAS-1-extended operators anchor here.

## Evidence (representative)

- `palace/linalg/vector.hpp:20` — `using Vector = mfem::Vector;`.
- `palace/linalg/vector.hpp:23-147` — `ComplexVector` class declaration.
- `palace/linalg/vector.hpp:242-253` — `LocalDot` declarations + `Dot` template scaffold.
- `palace/linalg/vector.hpp:255-260` — `Norml2` one-liner.
- `palace/linalg/vector.hpp:262-270` — `Normalize` fused construct.
- `palace/linalg/vector.hpp:305-316` — `AXPY` / `AXPBY` / `AXPBYPCZ` free-function template declarations.
- `palace/linalg/vector.cpp:203-227` — `ComplexVector::operator*=` body with shape branch.
- `palace/linalg/vector.cpp:263-274` — `Dot` / `TransposeDot` bodies with self-aliasing fast paths.
- `palace/linalg/vector.cpp:701-724` — `AXPY` family specialisations.
- `palace/linalg/vector.cpp:726-743` — `AXPBY` family specialisations.
- `palace/linalg/vector.cpp:745-772` — `AXPBYPCZ` family specialisations.
```

```edit:book/src/L0/ksp-factory-file.md
[old]:
[new]: # File — `palace/linalg/ksp.cpp`

A file-overview reference note. The Krylov-solver factory: where Palace's enum-based solver-type selector dispatches into solver constructors. This file is the anchor for the **advertised-but-unimplemented pattern** that drives the cycle-004 obstruction themes for MINRES and BiCGStab.

## At a glance

The file is small (a few hundred lines) and has two main factory functions in an anonymous namespace plus a small public surface:

- **`ConfigureKrylovSolver<OperType>`** (lines 26–101). Switches on `linear.krylov_solver` (a `KrylovSolver` enum). The implemented cases construct a solver and configure it; the unimplemented cases abort.
- **`ConfigurePreconditionerSolver<OperType>`** (lines 125 onward). Switches on `linear.type` (a `LinearSolver` enum) and constructs the corresponding preconditioner (AMS, BOOMER_AMG, SUPERLU, STRUMPACK, MUMPS, JACOBI, …). Each unsupported build-time configuration aborts with a specific message.
- **Public entry point** that combines the two factories and assembles the final solver.

## The enum-routed dispatch in `ConfigureKrylovSolver`

The switch at lines 34–58 has six branches:

```cpp
switch (type)
{
  case KrylovSolver::CG:
    ksp = std::make_unique<CgSolver<OperType>>(comm, print);
    break;
  case KrylovSolver::GMRES:
    { /* GMRES + SetRestartDim */ }
    break;
  case KrylovSolver::FGMRES:
    { /* FGMRES + SetRestartDim */ }
    break;
  case KrylovSolver::MINRES:
  case KrylovSolver::BICGSTAB:
  case KrylovSolver::DEFAULT:
    MFEM_ABORT("Unexpected solver type for Krylov solver configuration!");
    break;
}
```

Three solver types are implemented (`CG`, `GMRES`, `FGMRES`); three trigger `MFEM_ABORT` (`MINRES`, `BICGSTAB`, `DEFAULT`). The fall-through on the three abort cases is deliberate — all three share the same abort message. After the switch, common configuration applies (lines 59–62): initial guess, relative tolerance, max iterations. GMRES-specific configuration follows (lines 64–95): preconditioner side, orthogonalisation method. A timer is enabled at line 98.

## The "advertised-but-unimplemented" pattern

`MINRES` and `BICGSTAB` are **enumerated solver types** — they appear in the `KrylovSolver` enum, the configuration parser accepts them as inputs, and the factory recognises them as valid switch arms — but the implementation aborts at runtime. This is the load-bearing observation behind two L1>L0 obstruction themes:

- [`L1-L0/minres-iteration`](../L1-L0/minres-iteration.md) — proposes the speculative L1 operators `lanczos_step`, `three_term_recurrence_update`, `givens_apply_with_residual_min`. Harvester promotion gated on Palace gaining the implementation (or scope widening to vendored MFEM; see open question `bicgstab-mfem-reanchor-policy`).
- [`L1-L0/bicgstab-iteration`](../L1-L0/bicgstab-iteration.md) — proposes speculative L1 operators `bicgstab_step`, `omega_update`, `stabilisation_update`. Same gating.

`DEFAULT` aborting alongside `MINRES` and `BICGSTAB` indicates that the configuration layer is expected to resolve `DEFAULT` to a concrete enum value before reaching the factory — the factory does not pick a default itself. This is a separate concern (configuration layering) and not part of the obstruction theme.

## The implemented branches

For the three implemented branches (`CG`, `GMRES`, `FGMRES`), the factory:

- Constructs the solver template-instantiated on `OperType` (which is `Operator` or `ComplexOperator` — the element-type axis from [`mfem-vector-types`](./mfem-vector-types.md)).
- For GMRES / FGMRES, calls `SetRestartDim(linear.max_size)` (lines 42, 49) — the restart parameter.
- For GMRES / FGMRES, downstream of the switch, configures preconditioner side (lines 73–86) and orthogonalisation method (lines 92–94).

The solver classes themselves (`CgSolver`, `GmresSolver`, `FgmresSolver`) live in `palace/linalg/iterative.{hpp,cpp}` and are the L2 / L1 anchors for [`spec/slices/cg`](../spec/slices/cg.md) and [`spec/slices/gmres`](../spec/slices/gmres.md).

## Referenced from

- [`L1-L0/minres-iteration`](../L1-L0/minres-iteration.md) — obstruction theme; cites `ksp.cpp:53-57` as the enum-routed-abort anchor.
- [`L1-L0/bicgstab-iteration`](../L1-L0/bicgstab-iteration.md) — obstruction theme; same anchor.
- [`L1/index`](../L1/index.md) "Working Notes" — references the abort pattern when discussing rough-in entries from obstruction themes.

## Evidence

- `palace/linalg/ksp.cpp:26-101` — `ConfigureKrylovSolver` factory.
- `palace/linalg/ksp.cpp:34-58` — the switch on `KrylovSolver` type.
- `palace/linalg/ksp.cpp:53-57` — the three-case fall-through to `MFEM_ABORT` for `MINRES` / `BICGSTAB` / `DEFAULT`.
- `palace/linalg/ksp.cpp:59-62` — common post-switch configuration (initial guess, tolerance, max iterations).
- `palace/linalg/ksp.cpp:64-95` — GMRES-specific configuration (preconditioner side, orthogonalisation).
```

```edit:book/src/SUMMARY.md
[old]:# L0 — Cited Palace Source
- [Overview](./L0/index.md)
[new]:# L0 — Cited Palace Source + Reference Notes
- [Overview](./L0/index.md)
- [Convention — output-arg vs receiver](./L0/output-arg-vs-receiver.md)
- [Convention — MFEM vector types](./L0/mfem-vector-types.md)
- [Convention — linalg:: free-function wrappers](./L0/linalg-free-functions.md)
- [Convention — transparent vs load-bearing tricks](./L0/transparent-vs-load-bearing-tricks.md)
- [File — palace/linalg/vector.{hpp,cpp}](./L0/linalg-vector-file.md)
- [File — palace/linalg/ksp.cpp](./L0/ksp-factory-file.md)
```

## Supporting evidence

**L1 operator pages whose `Context` sections re-state conventions covered by this bundle** (candidates for the cycle-005 retroactive-thinning sweep, priority #11):

- [`L1/axpy`](../../book/src/L1/axpy.md) `Context` — re-states the output-arg vs receiver mutation idiom (`y.Add` vs `y.AXPY` vs receiver `y`); re-states element-type axis. Thinning candidate: replace inline restatement with a one-line link to [`L0/output-arg-vs-receiver`](../../book/src/L0/output-arg-vs-receiver.md) and [`L0/mfem-vector-types`](../../book/src/L0/mfem-vector-types.md).
- [`L1/axpby`](../../book/src/L1/axpby.md) `Context` — same two conventions plus the `linalg::AXPBY` free-function-template wrapping pattern. Thinning candidate: link [`L0/linalg-free-functions`](../../book/src/L0/linalg-free-functions.md) instead of restating.
- [`L1/axpbypcz`](../../book/src/L1/axpbypcz.md) `Context` — same; plus the `γ == 0` transparent-trick classification belongs in [`L0/transparent-vs-load-bearing-tricks`](../../book/src/L0/transparent-vs-load-bearing-tricks.md).
- [`L1/scal`](../../book/src/L1/scal.md) `Context` — re-states the no-`linalg::Scal` notable-absence (now in [`L0/linalg-free-functions`](../../book/src/L0/linalg-free-functions.md)); re-states the `s.imag() == 0.0` shape branch classification (now in [`L0/transparent-vs-load-bearing-tricks`](../../book/src/L0/transparent-vs-load-bearing-tricks.md)).
- [`L1/dot`](../../book/src/L1/dot.md) `Context` — re-states the receiver-vs-argument asymmetry on the method form (now in [`L0/output-arg-vs-receiver`](../../book/src/L0/output-arg-vs-receiver.md) implicitly; method-form covered); re-states the `LocalDot` + `Mpi::GlobalSum` scaffold (now in [`L0/linalg-free-functions`](../../book/src/L0/linalg-free-functions.md)); re-states reduction-tree non-associativity load-bearing classification (now in [`L0/transparent-vs-load-bearing-tricks`](../../book/src/L0/transparent-vs-load-bearing-tricks.md)).
- [`L1/nrm2`](../../book/src/L1/nrm2.md) `Context` — re-states the `linalg::Norml2` one-line composition (now in [`L0/linalg-free-functions`](../../book/src/L0/linalg-free-functions.md) and [`L0/linalg-vector-file`](../../book/src/L0/linalg-vector-file.md)); re-states the `std::abs` defensive guard load-bearing classification (now in [`L0/transparent-vs-load-bearing-tricks`](../../book/src/L0/transparent-vs-load-bearing-tricks.md)).
- [`L1/apply_linop`](../../book/src/L1/apply_linop.md) `Context` — re-states the `A.Mult(x, y)` output-arg idiom (now in [`L0/output-arg-vs-receiver`](../../book/src/L0/output-arg-vs-receiver.md)); re-states the `Operator` vs `ComplexOperator` hierarchy split (now in [`L0/mfem-vector-types`](../../book/src/L0/mfem-vector-types.md)); re-states the matrix-free reduction-order load-bearing classification (now in [`L0/transparent-vs-load-bearing-tricks`](../../book/src/L0/transparent-vs-load-bearing-tricks.md)).

**Operators currently harvested at L1** (used to scope this bundle's backlinks):

- `axpy`, `dot`, `nrm2`, `axpby`, `scal`, `apply_linop`, `axpbypcz` — all firm; all have backlinks in at least three of the four conventions chapters.

**Cross-layer references this bundle establishes:**

- L1 → L0 conventions (7 L1 operator pages reference at least one of 4 convention chapters).
- L1-L0 (lowering) → L0 file overviews (`minres-iteration` and `bicgstab-iteration` reference `ksp-factory-file`).
- L0 file-overview `linalg-vector-file` ↔ L0 conventions (cross-links among reference notes).

## Open questions / caveats

- **Retroactive L1 thinning (priority #11) is a separate dispatch.** This bundle authors the L0 chapters and lays down the `Referenced from:` backlinks, but does **not** edit L1 entries — that crosses the layer-intro-author authority boundary (one layer per invocation; harvester or a dedicated thinner edits L1 operator entries). The supporting-evidence section above enumerates the specific `Context` paragraphs that should be replaced with one-line links in the follow-on sweep.
- **`mfem-vector-types` chapter does not cover MFEM types Palace re-exports beyond `Vector`** (e.g. `mfem::Operator` is re-exported at `operator.hpp:21`). Scope intentionally limited to vector types for this bundle; an operator-types convention chapter is a natural follow-on if L1 entries warrant it.
- **`transparent-vs-load-bearing-tricks` is sourced from `CLAUDE.md`**, which is the authoritative methodology document. If `CLAUDE.md` is revised, this chapter inherits the dependency — flagged as a maintenance link in the chapter body but no automated check exists.
- **`linalg-vector-file` overview cites representative ranges but is not exhaustive.** A reader searching for `LocalSum`, `Sqrt`, `Cross2/Cross3`, or `SetSubVector` will find pointers but not full coverage. The discipline (2–4 paragraphs + 3–6 citations) caps the per-chapter scope; expansion is a future-bundle decision.
- **`ksp-factory-file` overview stops short of `ConfigurePreconditionerSolver`.** That factory (lines 125 onward) is the anchor for a future L0 reference-note on the preconditioner-type enum and the build-time-conditional `MFEM_ABORT` pattern (SUPERLU / STRUMPACK / MUMPS gated on build flags). Flagged as a candidate bundle-2 chapter.
- **No new entries in `scaffolding/open-questions.md` are proposed** — the existing open questions (`scalar-promotion-typing-rule`, `bicgstab-mfem-reanchor-policy`, `nrm2-B-weighted-energy-norm-harvest`) suffice; this bundle does not surface new ones.
