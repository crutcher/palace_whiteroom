# Convention — transparent vs load-bearing optimisation tricks

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
