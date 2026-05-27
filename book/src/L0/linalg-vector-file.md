# File — `palace/linalg/vector.{hpp,cpp}`

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
