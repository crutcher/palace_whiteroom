# Convention — output-argument vs receiver mutation

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
