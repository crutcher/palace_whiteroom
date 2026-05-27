# Convention — `linalg::` free functions as template-dispatch wrappers

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

- [`L1/axpy`](../L1/axpy.md), [`L1/axpby`](../L1/axpby.md), [`L1/axpbypcz`](../L1/axpbypcz.md) — `linalg::AXPY` / `linalg::AXPBY` / `linalg::AXPBYPCZ` free-function-template wrappers over method-form.
- [`L1/dot`](../L1/dot.md) — `linalg::Dot` composing `LocalDot` + `Mpi::GlobalSum`; method-form `ComplexVector::Dot`.
- [`L1/nrm2`](../L1/nrm2.md) — `linalg::Norml2` as one-line composition `sqrt(abs(Dot(x, x)))`.
- [`L1/scal`](../L1/scal.md) — no free-function form (notable absence); `operator*=` only.
