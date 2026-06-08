---
layer: L1
operator: nrm2
rank: firm
edges:
  depends-on:
    - L1/dot
    - kind: lowers-to        # the L1>L0 mutation-rotation theme
      target: L1-L0/nrm2-mutation-rotation
---

# nrm2

Mutation-free vector Euclidean-norm reduction: `α = ‖x‖₂ = √⟨x, x⟩`. The canonical BLAS-1 norm primitive at L1; the workhorse of residual-norm convergence tests, basis-vector normalisation, and Arnoldi sub-diagonal coefficients.

## Context

`nrm2` lifts the one-line free-function template `linalg::Norml2(comm, x) = std::sqrt(std::abs(Dot(comm, x, x)))` (and the MFEM method-form `Vector::Norml2()` on real vectors, plus the thin caller-side wrapper `ErrorIndicator::Norml2(comm)` at `palace/fem/errorindicator.hpp:43`) to a single pure-functional Euclidean-norm reduction. The L0 file layout — `Norml2`'s one-line body and the surrounding reduction family — is detailed in [`L0/linalg-vector-file`](../L0/linalg-vector-file.md) "The reduction family". The composition shape (one-line `sqrt(abs(Dot(...)))`) is named in [`L0/linalg-free-functions`](../L0/linalg-free-functions.md) "One-line composition". The element-type axis (real / complex, with both collapsed to a real-valued result) is named in [`L0/mfem-vector-types`](../L0/mfem-vector-types.md). The outer `std::abs` defensive non-negativity guard is classified as a load-bearing implementation detail in [`L0/transparent-vs-load-bearing-tricks`](../L0/transparent-vs-load-bearing-tricks.md).

At L0, the in-place destination for `nrm2` is the return register / a stack scalar; there is no destination buffer to write through. The L1 form is identical algebraically — the operator is naturally pure. What the mutation rotation does here is essentially nothing on the buffer side; the L1 entry exists to record the algebraic identity `nrm2(x) = √dot(x, x)`, the element-type unification (one operator at L1; two specialisations at L0), and the load-bearing numerical caveat (the reduction-tree non-associativity that propagates from `dot` is the same one).

A cross-cutting prose treatment lives at [`concepts/nrm2`](../concepts/nrm2.md). The L1 entry here is the firm operator definition; the concept page is the narrative. Note: the concept page claims Palace uses "scaled summation (BLAS `nrm2` algorithm) to avoid overflow/underflow". This is **not** what `linalg::Norml2` actually does — it computes the naive `√⟨x, x⟩` via `Dot`. Palace inherits any over/underflow risk; if the underlying BLAS / Hypre kernel internally scales, that is an L1>L0 lowering observation, not a Palace-level guarantee. The L1 entry is authoritative; the concept page should be corrected by a future invocation.

The B-weighted overload `linalg::Norml2(comm, x, B, Bx)` at `palace/linalg/operator.cpp:600-619` (declared at `operator.hpp:372-374`) is **not** part of this operator. It computes `√(xᴴ B x)` for an SPD operator `B`, requires a workspace `Bx`, and is algebraically a different construct (operator-weighted norm, a.k.a. energy norm). It is a separate L1 operator candidate (forthcoming) that depends on both `dot` and the operator-application primitive `apply_linop`.

## Signature

```
nrm2 :: (x: Tensor[N]) -> Scalar
nrm2(x) = √⟨x, x⟩
```

Shape contract (bunsen-style, named axes):

- `x` — `Tensor[N]` — read-only.
- result — `Scalar` — **always real-valued** (`real`), regardless of whether `x` is real or complex.
- The result is non-negative: `nrm2(x) ≥ 0`.

The "result is always real" rule is load-bearing — it is what makes the element-type axis collapse to a single L1 operator (in contrast to `dot`, where the result element-type tracks the input). It follows from the fact that `dot(x, x)` is a non-negative real scalar for both real (law 4 of L1 dot) and complex (law 9 of L1 dot) inputs.

## Semantics

Definitional: `nrm2(x) = √dot(x, x)`. This is the principal (non-negative) square root of the Hermitian self-inner-product.

For real element-type: `nrm2(x) = √Σ_i x[i]²`.

For complex element-type: `nrm2(x) = √Σ_i |x[i]|² = √Σ_i (re(x[i])² + im(x[i])²)`. The Hermitian self-dot `dot(x, x)` for complex `x` is `Σ_i conj(x[i])·x[i] = Σ_i |x[i]|²`, which is real and non-negative element-wise — so the L0 implementation's outer `std::abs(...)` before `std::sqrt` is a defensive guard against floating-point round-off pushing the sum slightly negative, **not** a semantic projection. Algebraically `nrm2(x) = √dot(x, x)` for both element types.

Reduction-tree non-associativity is **load-bearing** — inherited unchanged from `dot`. The square root itself is a deterministic IEEE-754 operation (correctly rounded), so `nrm2`'s non-determinism is entirely the `dot`'s.

The MPI collective is **not** in the L1 signature. The `linalg::Norml2(comm, x)` form folds a `MPI_Allreduce` inside the inner `dot`; single-rank is in scope (per `CLAUDE.md` "Scope"), so the L1 reduction is a single semantic step. The L1>L0 lowering reintroduces the local-then-collective two-step (and inherits the bit-deterministic-reduction-order trade-offs already recorded for `dot`).

## Algebraic laws

The laws below hold for both real and complex element-types of `x`; absences are deliberate.

1. **Non-negativity**: `nrm2(x) ≥ 0` for all `x`.
2. **Positive-definite (separation)**: `nrm2(x) = 0` iff `x = 0` (in exact arithmetic). The "iff" direction follows from `dot` law 4 / 9.
3. **Positive homogeneity (absolute scalar)**: `nrm2(α·x) = |α|·nrm2(x)` for any scalar `α` (real or complex). Note the `|α|` — the absolute value is necessary on both sign and complex phase; the norm strips both.
4. **Triangle inequality**: `nrm2(x + y) ≤ nrm2(x) + nrm2(y)`.
5. **Reverse triangle inequality**: `|nrm2(x) − nrm2(y)| ≤ nrm2(x − y)`. (Follows from law 4.)
6. **Cauchy–Schwarz** (relating `nrm2` to `dot`): `|dot(x, y)| ≤ nrm2(x) · nrm2(y)`, with equality iff `x` and `y` are linearly dependent (in exact arithmetic).
7. **Parallelogram identity**: `nrm2(x + y)² + nrm2(x − y)² = 2·nrm2(x)² + 2·nrm2(y)²`. (Characterises norms induced by an inner product; holds here because `nrm2` is defined as `√⟨·,·⟩`.)
8. **Self-dot identity**: `nrm2(x)² = dot(x, x)` (real and complex) — the defining identity, restated. Used directly by Palace at `palace/linalg/vector.hpp:259` and indirectly anywhere CG-style algorithms reuse `dot(r, r)` instead of recomputing `nrm2(r)²`.
9. **Zero in argument**: `nrm2(0) = 0`. (Special case of law 2.)
10. **Phase invariance (complex)**: for complex `x` and any unit-modulus complex scalar `e^{iθ}`: `nrm2(e^{iθ}·x) = nrm2(x)`. (Special case of law 3 with `|α| = 1`.)

Laws that explicitly **do not** hold:

- **Linearity in `x`**: `nrm2(α·x + β·y) ≠ α·nrm2(x) + β·nrm2(y)` in general. `nrm2` is sub-additive (law 4), not additive. This is the defining feature that distinguishes a norm from a linear functional.
- **Strictness of Cauchy–Schwarz in floating point**: law 6 can fail by ULP-level amounts due to summation ordering inside `dot` (same load-bearing caveat as the `dot` operator). Algorithms that depend on the strict inequality (e.g. orthogonality-loss detection in MGS reorthogonalisation) must guard.
- **Bit-determinism across reduction trees**: same load-bearing caveat as `dot` — different reduction orders produce different bit-level `nrm2` values. The mathematical laws above hold; their floating-point realisations are exact modulo summation-order noise.
- **Multiplicativity over the cross-element kernel**: `nrm2(x ⊙ y) ≠ nrm2(x) · nrm2(y)` in general (where `⊙` is the hypothetical element-wise product). Not applicable — `nrm2` is a reduction, not a binary algebra on vectors.

## Dependencies

- [`dot`](./dot.md) (firm) — `nrm2(x) = √dot(x, x)`. The dependency is direct and complete: the L0 source defines `Norml2` as a one-line composition `std::sqrt(std::abs(Dot(comm, x, x)))`. At L1 this is the **only** L1 operator that `nrm2` depends on; the outer `sqrt` and `abs` are scalar operations below the L1 layer's resolution (deterministic IEEE-754 primitives).

Not a leaf — but only one level removed. The fact that `nrm2` factors so cleanly through `dot` is exactly the kind of compositional structure the L1 layer is meant to expose; the L0 form makes the composition syntactically explicit (one line of source), and the L1 form names it as the defining identity (algebraic law 8).

## Variant axes

`nrm2` has one orthogonal variant axis at L1:

- **element-type**: `real` | `complex`. At L0 these are template specialisations of `linalg::Norml2<VecType>` (`VecType ∈ {Vector, ComplexVector}`). At L1 these **collapse to a single operator** with the same signature `(x: Tensor[N]) → Scalar(real)`, because:
  - The result is real-valued regardless of input element type (the Hermitian self-dot is real).
  - The defining identity `nrm2(x) = √dot(x, x)` is shared across element types; the element-type dispatch is entirely absorbed by `dot`.
  - All ten algebraic laws hold uniformly across both element types.

  This is a stronger collapse than `dot`'s element-type axis: `dot` retains an element-type-tracking return scalar (real `dot` → real, complex `dot` → complex); `nrm2` does not.

No other variant axes at L1:

- **B-weighting**: not a variant of `nrm2` — it is a distinct operator (operator-weighted norm, `‖x‖_B = √(xᴴ B x)`) with its own L1 entry forthcoming. The L0 surface uses the same overloaded name `linalg::Norml2`, but the algebraic structure differs (requires an external `B`-application primitive, requires an SPD precondition on `B`, the workspace `Bx` is a load-bearing buffer at L0 even though it's pure at L1).
- **Stability variants**: BLAS-style scaled-summation `nrm2` (which avoids overflow/underflow at the cost of extra arithmetic) is **not present** in Palace's `linalg::Norml2` — Palace uses the naive `√⟨x,x⟩` form. If scaling matters for a specific algorithm, that is a caller-side concern (no Palace use site is known to scale before calling `Norml2`); not a variant axis of the L1 operator.

## L1 vs L0 distinction

- **L0**: free-function `linalg::Norml2(MPI_Comm, x)` (does `Dot` + `MPI_Allreduce` + `std::abs` + `std::sqrt`), method-form `Vector::Norml2()` (real, no MPI), or wrapper `ErrorIndicator::Norml2(comm)`. The B-weighted overload `Norml2(comm, x, B, Bx)` is a separately-named operator at L0 sharing the same symbol via overloading. The `std::abs` outer guard is present to defend against round-off-induced sub-zero `dot(x,x)` values.
- **L1**: pure functional reduction `α = nrm2(x)`. No MPI collective in the signature, no method-form / wrapper / overload distinction. The B-weighted overload is **factored out** as a separate L1 operator (forthcoming). The defining identity `nrm2(x) = √dot(x, x)` is stated as algebraic law 8; the `std::abs` defensive guard is recognised as a floating-point implementation detail and disappears at L1 (the algebraic claim that `dot(x, x)` is non-negative real subsumes it).

## Evidence

- `palace/linalg/vector.hpp:255-260` — `linalg::Norml2` template definition: full body is `return std::sqrt(std::abs(Dot(comm, x, x)));`. The single load-bearing line.
- `palace/linalg/vector.hpp:262-270` — `linalg::Normalize` template, which uses `Norml2` then scales `x *= 1.0 / norm` and asserts `norm > 0.0`. Confirms `nrm2` returns a positive real used as a divisor.
- `palace/linalg/operator.hpp:372-374` — declaration of the B-weighted overload `Norml2(comm, x, B, Bx) → double`. Recorded here to mark the boundary; not part of this operator's definition.
- `palace/linalg/operator.cpp:600-619` — definitions of the B-weighted overload for both `Vector` and `ComplexVector`. The complex case asserts `dot.real() > 0.0 && std::abs(dot.imag()) < 1.0e-9 * dot.real()` then returns `std::sqrt(dot.real())` — confirming that `xᴴ B x` is expected to be real for SPD `B`. Recorded as boundary evidence.
- `palace/fem/errorindicator.hpp:43` — `ErrorIndicator::Norml2(comm) const { return linalg::Norml2(comm, local); }` — a transparent wrapper.
- `palace/linalg/iterative.cpp:408, 568, 578, 582, 631, 756, 762, 810` — CG and GMRES iterative solvers using `linalg::Norml2` for: initial right-hand-side norm `β = ‖b‖` (l.408, 578, 582, 762), true residual norm `‖r‖` (l.568, 756), and Arnoldi sub-diagonal coefficients `H[j+1,j] = ‖w‖` (l.631, 810). Direct evidence `nrm2` is the convergence-test and Arnoldi-orthogonalisation primitive.
- `palace/linalg/arpack.cpp:438, 442, 471, 609, 826` — ARPACK Arnoldi residual norm computations: B-weighted form at l.438 (separate operator), plain form at l.442; residual relative norm at l.471; final residual norms at l.609 and l.826.
- `palace/linalg/nleps.cpp:114, 118, 147, 610, 820` — nonlinear-EVP residual norms; B-weighted at l.114; plain at l.118; relative residual at l.147 (`GetResidualNorm(...) / linalg::Norml2(comm, x1)`); scale-extraction for normalisation at l.610; final residual norm at l.820.
- `palace/linalg/slepc.cpp:475, 479, 507, 834, 976, 1329, 1776` — SLEPc Arnoldi residual norms (B-weighted and plain), confirming `nrm2` is the primary residual-norm primitive across all three eigensolver backends (ARPACK, SLEPc, NLEPS).
- `test/unit/test-vector.cpp:209-211` — direct test: `double norm1 = vec1.Norml2(); CHECK_THAT(norm1, WithinRel(std::sqrt(14.0)));` for `vec1 = (1, 2, 3)`. Confirms `nrm2((1,2,3)) = √14` and confirms the return type is `double` (real) for real inputs. L0-equivalent semantic documentation per CLAUDE.md "Tests as semantic supplement".
- Firm `dot` entry at `book/src/L1/dot.md` — provides laws 4 and 9 (Hermitian self-dot is non-negative real) on which `nrm2`'s real-valued result and positivity depend.
