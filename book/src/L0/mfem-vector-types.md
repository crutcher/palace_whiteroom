# Convention — MFEM vector types and the element-type axis

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

- [`L1/axpy`](../L1/axpy.md), [`L1/axpby`](../L1/axpby.md), [`L1/axpbypcz`](../L1/axpbypcz.md), [`L1/scal`](../L1/scal.md) — element-type axis collapse.
- [`L1/dot`](../L1/dot.md), [`L1/nrm2`](../L1/nrm2.md) — element-type axis + `LocalDot` vs `Dot` (MPI collective) split.
- [`L1/apply_linop`](../L1/apply_linop.md) — `Operator` vs `ComplexOperator` hierarchy split; `ParOperator` wrapping.
