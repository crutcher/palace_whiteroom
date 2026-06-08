---
layer: L1
operator: matrix_weighted_norm
rank: firm
edges:
  depends-on:
    - L1/dot
    - L1/apply_linop
  reference:
    - L1/bilinear_form
    - L1-L0/matrix-weighted-norm-mutation-rotation
---

# matrix_weighted_norm

Mutation-free operator-weighted vector norm: `α = ‖x‖_B = √(xᴴ B x)` for an SPD operator `B`. The energy-norm primitive at L1; the workhorse of M-orthonormal eigenvector normalisation in the generalised eigenvalue problem (`A x = λ B x`) and the natural metric in B-conjugate-gradient methods.

## Context

`matrix_weighted_norm` lifts the free-function templates `linalg::Norml2(comm, x, B, Bx)` (declared at `palace/linalg/operator.hpp:372-374`; specialized for `Vector` and `ComplexVector` at `palace/linalg/operator.cpp:599-619`) to a single pure-functional energy-norm operator. The two L0 specializations differ only in element-type plumbing — the complex specialization splits `B.Mult` into real/imaginary calls (since the L0 `B : Operator` is real-only by signature, even though the input vector may be complex) and adds the assertion that the resulting Hermitian self-bilinear is real to within `1e-9`. At L1 these collapse to one operator parameterised by element type, with the SPD precondition on `B` made an explicit applicability condition.

The L0 file layout — the matrix-weighted `linalg::` free-function block at the bottom of `operator.hpp` — is detailed in [`L0/linalg-operator-file`](../L0/linalg-operator-file.md) "linalg:: free functions". The workspace-internal-allocation pattern is not used here (caller supplies `Bx`); the related operator `Dot(comm, x, A, y)` uses Category 1 of [`L0/mutable-workspace-pattern`](../L0/mutable-workspace-pattern.md) (operator-composition workspace, holding the `A·x` intermediate between the apply and the reduction) — `matrix_weighted_norm`'s `Bx` is a *caller-owned* workspace, sliding it across the bilinear_form sibling boundary.

At L0, the caller-supplied workspace `Bx` is overwritten with `B · x` (it is a *destination* buffer, not just scratch), and the in-place destination for the return is the return register / a stack scalar. There is no destination buffer for the result. The L1 form drops both: the operator consumes `x` and `B`, produces a fresh scalar; the `Bx` workspace disappears. Workspace ownership and lifetime become an L1>L0 lowering concern (the `matrix-weighted-norm-mutation-rotation` theme, not yet authored).

The unweighted `nrm2` operator ([`nrm2`](./nrm2.md)) flags this operator as a sibling boundary in its Context section. Both operators share the structural shape `√(quadratic form of x)` but differ in the form: `nrm2` is `√⟨x, x⟩`; `matrix_weighted_norm` is `√⟨B·x, x⟩` (equivalently `√⟨x, B·x⟩` for Hermitian `B`). At L1 these are **distinct operators**, not variants of one operator — the algebraic laws differ (the unweighted norm is unconditionally a norm; the weighted form is a norm iff `B` is SPD, and degrades to a seminorm if `B` is SPSD).

## Signature

```
matrix_weighted_norm :: (x: Tensor[N], B: LinearOperator[N, N]) -> Scalar
matrix_weighted_norm(x, B) = √(xᴴ B x)
```

Shape contract (bunsen-style, named axes):

- `x` — `Tensor[N]` — read-only.
- `B` — `LinearOperator[N, N]` — read-only. **Square** (the codomain axis must equal the domain axis), because the form `xᴴ B x` requires `B·x` to live in the same space as `x`.
- result — `Scalar` — **always real-valued** (`real`), regardless of whether `x` and `B` are real or complex.
- The result is non-negative under the SPD applicability condition: `matrix_weighted_norm(x, B) ≥ 0`.

The "result is always real" rule mirrors `nrm2`'s collapse: for SPD `B`, the Hermitian sesquilinear form `xᴴ B x` is real (laws below). The L0 complex specialization asserts this directly (`palace/linalg/operator.cpp:616-617`: `MFEM_ASSERT(dot.real() > 0.0 && std::abs(dot.imag()) < 1.0e-9 * dot.real(), ...)`), then returns `std::sqrt(dot.real())` — confirming that the imaginary part is round-off only and the L1 statement "result is real" is a direct algebraic consequence of `B` being SPD.

## Semantics

Definitional: `matrix_weighted_norm(x, B) = √(xᴴ B x)` — the principal (non-negative) square root of the operator-induced Hermitian self-bilinear form.

For real element-type: `matrix_weighted_norm(x, B) = √(xᵀ B x) = √Σ_i x[i] · (B·x)[i]`.

For complex element-type: `matrix_weighted_norm(x, B) = √(xᴴ B x) = √Σ_i conj(x[i]) · (B·x)[i]`. The form `xᴴ B x` is real for Hermitian `B`; the L0 implementation's `MFEM_ASSERT` on the imaginary-part magnitude is a defensive round-off guard, not a semantic projection.

The form `xᴴ B x` is the *energy* (or *B-quadratic*) form of `x` with respect to `B`. When `B` is SPD it defines a true norm (the energy norm); when `B` is only SPSD (positive semi-definite, allowing zero eigenvalues) it defines only a seminorm; when `B` is indefinite the construct is **not a norm at all** and the square root is ill-defined for `x` such that `xᴴ B x < 0`. The L0 source treats SPD as the contract (the assertion `dot > 0.0` would fire for an indefinite `B` applied to a vector in its negative cone). The L1 form encodes SPD as an explicit applicability condition (see below).

The complex-input / real-operator structure (the L0 specialization signature `Norml2(comm, ComplexVector &x, Operator &B, ComplexVector &Bx)` — note `B` is real even though `x` is complex) reflects Palace's L0 convention that mass-like operators (the typical `B`) are real-valued operators applied componentwise to the real and imaginary parts of complex vectors. At L1 this distinction is absorbed by `apply_linop`'s element-type variant axis: the L1 operator just requires `B : LinearOperator[N, N]` with element type matching some inner-product compatibility rule, and the real-`B`-applied-to-complex-`x` case is admitted as a uniform treatment, not a distinct variant.

Reduction-tree non-associativity is **load-bearing** — inherited from the inner `dot(B·x, x)` via the same chain as `nrm2`. The outer `sqrt` is deterministic IEEE-754. Additionally, `apply_linop(B, x)` is itself subject to representation-aware non-associativity (per `apply_linop` Semantics — matrix-free representations of `B` introduce summation-order non-associativity). So `matrix_weighted_norm` accumulates non-associativity from **two** sources: the inner-product reduction and the operator-application's internal kernel.

The MPI collective is **not** in the L1 signature. The L0 `linalg::Norml2(comm, x, B, Bx)` folds an `MPI_Allreduce` inside the inner `Dot`; single-rank is in scope (per `CLAUDE.md` "Scope"). The L1>L0 lowering reintroduces the local-then-collective two-step and the bit-deterministic-reduction-order trade-offs already recorded for `dot` and `apply_linop`.

## Algebraic laws

The laws below hold **conditional on `B` being SPD**, for both real and complex element-types of `x`; absences are deliberate. The SPD precondition is what makes `matrix_weighted_norm` a norm rather than just a quadratic form. Where a weaker condition suffices (e.g. SPSD for non-negativity), it is noted.

1. **Non-negativity (SPSD sufficient)**: `matrix_weighted_norm(x, B) ≥ 0` for all `x` and any SPSD `B`. The full SPD condition is needed only for separation (law 2).
2. **Positive-definite (separation; SPD required)**: `matrix_weighted_norm(x, B) = 0` iff `x = 0` (in exact arithmetic), for SPD `B`. For SPSD `B` (positive semi-definite, possibly singular), the operator is a **seminorm**: `matrix_weighted_norm(x, B) = 0` for `x` in the null space of `B`, even when `x ≠ 0`.
3. **Positive homogeneity (absolute scalar)**: `matrix_weighted_norm(α·x, B) = |α|·matrix_weighted_norm(x, B)` for any scalar `α` (real or complex). Follows from `apply_linop`'s linearity in `x` (law 1) and `dot`'s conjugate-linearity in the first argument (law 7) — the conjugate-on-the-left cancels the linearity-on-the-right, leaving `|α|²` inside the square root, hence `|α|` outside.
4. **Triangle inequality (SPSD sufficient)**: `matrix_weighted_norm(x + y, B) ≤ matrix_weighted_norm(x, B) + matrix_weighted_norm(y, B)`. The inner-product structure inherited from `dot` plus SPSD `B` (so `xᴴ B x ≥ 0`) is sufficient — full SPD is not required for sub-additivity.
5. **Reverse triangle inequality**: `|matrix_weighted_norm(x, B) − matrix_weighted_norm(y, B)| ≤ matrix_weighted_norm(x − y, B)`. (Follows from law 4.)
6. **Cauchy–Schwarz in the B-inner-product**: for the bilinear form `⟨x, y⟩_B := xᴴ B y` (a separate L1 operator, queued as `bilinear_form`): `|⟨x, y⟩_B| ≤ matrix_weighted_norm(x, B) · matrix_weighted_norm(y, B)`, with equality iff `x` and `y` are linearly dependent modulo the null space of `B` (in exact arithmetic).
7. **Parallelogram identity (SPSD sufficient)**: `matrix_weighted_norm(x + y, B)² + matrix_weighted_norm(x − y, B)² = 2·matrix_weighted_norm(x, B)² + 2·matrix_weighted_norm(y, B)²`. Characterises norms induced by an inner product; for SPD `B` the B-inner-product `⟨x, y⟩_B` is a genuine inner product, but the identity itself is purely algebraic and holds for any semi-inner-product (SPSD `B` suffices — non-degeneracy is not required).
8. **Self-bilinear identity**: `matrix_weighted_norm(x, B)² = xᴴ B x`. The defining identity, restated. Used directly by the L0 source (the implementation factors as `B.Mult(x, Bx); dot = Dot(comm, Bx, x); return std::sqrt(dot)` — `palace/linalg/operator.cpp:602-606`).
9. **Identity-operator collapse**: `matrix_weighted_norm(x, I) = nrm2(x)` for the identity operator `I : V → V`. The two operators agree exactly on the identity weight; this is the algebraic statement that ties this entry to its sibling [`nrm2`](./nrm2.md).
10. **Diagonal-scaling structure**: for a diagonal SPD operator `D = diag(d_1, ..., d_N)` with `d_i > 0`, `matrix_weighted_norm(x, D) = √Σ_i d_i · |x[i]|²` — i.e. element-wise √d_i-weighted L2 norm. Note Palace's elementwise scaling family is the related-but-distinct operator class (`DiagonalOperator` at `palace/linalg/operator.cpp:480-585`), not directly used as the `B` in `Norml2(comm, x, B, Bx)` callsites identified in evidence.
11. **Phase invariance (complex)**: for complex `x` and any unit-modulus complex scalar `e^{iθ}`: `matrix_weighted_norm(e^{iθ}·x, B) = matrix_weighted_norm(x, B)`. (Special case of law 3 with `|α| = 1`.)
12. **Zero in argument**: `matrix_weighted_norm(0, B) = 0`. (Special case of law 2.)

Laws that explicitly **do not** hold:

- **B-linearity**: `matrix_weighted_norm(x, B₁ + B₂) ≠ matrix_weighted_norm(x, B₁) + matrix_weighted_norm(x, B₂)`. The square-root breaks operator-side additivity. What does hold (and is queued at the bilinear_form sibling) is the *squared* form `‖x‖²_{B₁+B₂} = ‖x‖²_{B₁} + ‖x‖²_{B₂}`, which follows from `apply_linop`'s operator-side linearity (law 5) and `dot`'s bilinearity. Not part of `matrix_weighted_norm` itself.
- **Vector-side linearity in x**: `matrix_weighted_norm(α·x + β·y, B) ≠ α·matrix_weighted_norm(x, B) + β·matrix_weighted_norm(y, B)` in general. `matrix_weighted_norm` is sub-additive (law 4), not additive. This is the defining feature that distinguishes a norm from a linear functional — same caveat as `nrm2`.
- **Norm contract for indefinite `B`**: if `B` is indefinite (has both positive and negative eigenvalues), the construct `xᴴ B x` can be negative, and `√(xᴴ B x)` is complex / undefined. Recorded as an absence: the L0 source's `MFEM_ASSERT(dot > 0.0)` *fails* for indefinite `B`; the L1 form requires SPD (or SPSD with seminorm caveat) as an applicability condition, not a soft guard.
- **Strict Cauchy–Schwarz in floating point**: law 6 can fail by ULP-level amounts due to the compound non-associativity (inner `dot` + inner `apply_linop`). Same caveat as `nrm2` plus an additional contribution from `apply_linop`.
- **Bit-determinism across operator representations of `B`**: same load-bearing caveat as `apply_linop` — a sparse-matrix realisation of `B` and a matrix-free realisation of the *same* SPD operator produce results that agree mathematically but may differ at the bit level.

## Applicability conditions

- **`B` must be square** (`LinearOperator[N, N]` with codomain axis = domain axis). The bilinear form `xᴴ B x` is otherwise dimensionally ill-formed. The L0 source enforces this implicitly via the workspace shape (`Bx` is sized `B.Height()` and dotted against `x` of length `N`).
- **`B` must be Hermitian (self-adjoint)** for the form `xᴴ B x` to be real-valued. The L0 implementation does **not** verify Hermiticity directly; instead the complex specialization asserts the imaginary part of the computed `xᴴ B x` is small relative to the real part (`palace/linalg/operator.cpp:616-617`), which is a numerical witness rather than a structural check.
- **`B` must be positive semi-definite (SPSD)** for the form `xᴴ B x` to be non-negative and the square root well-defined. The L0 implementation asserts `dot > 0.0` strictly (lines 604-605 for the real case, line 616 for the complex case) — i.e. it enforces **positive-definite** at run time, treating SPSD-but-zero cases as errors. This means the L0 contract is **SPD strict**, even though several of the algebraic laws above hold under the weaker SPSD condition.
- **`B` must be positive-definite (SPD)** for the operator to be a true norm (separation law 2). Without SPD, separation fails on the null space of `B` and the construct is a seminorm.

In practice across Palace's eigensolver corpus (the dense callsite cohort below), `B` is the mass matrix or a curl-curl mass-weighted operator — both SPD by construction. The applicability condition is satisfied uniformly.

## Composition note (informational; not L1 semantics)

The L0 implementation factors as `B.Mult(x, Bx); dot = Dot(comm, Bx, x); return std::sqrt(dot)` (`palace/linalg/operator.cpp:602-606`). At L1 this is the unfolded composition `√(dot(apply_linop(B, x), x))` — but **this composition is L1>L0 lowering-theme territory**, not the L1 semantics. The L1 operator is defined by the closed-form `√(xᴴ B x)`; the unfolding into three sub-operations belongs in the (not-yet-authored) `matrix-weighted-norm-mutation-rotation` L1>L0 theme. The L1 layer collapses the three-step unfold to a single semantic step, just as `nrm2` collapses `√(dot(x, x))` to a single step despite the L0 source making the two-step composition syntactically explicit.

## Dependencies

- [`dot`](./dot.md) — the inner reduction `xᴴ (B·x)`. Used in the **closed-form definition** of `matrix_weighted_norm` (law 8: `matrix_weighted_norm(x, B)² = xᴴ B x` is interpretable as `dot(B·x, x)` via dot's Hermitian-sesquilinear law). The L1 dependency is structural; it appears in the L1>L0 lowering as the second of the three composed primitives.
- [`apply_linop`](./apply_linop.md) — the operator-application primitive supplying `B · x`. Used in the closed-form via the `B·x` inside `xᴴ B x`. The L1 dependency is structural; it appears in the L1>L0 lowering as the first of the three composed primitives.

Not a leaf — two L1 dependencies. The factoring is parallel to `nrm2`'s factoring through `dot` (one dependency, one composition), but with the extra `apply_linop` step required to introduce the weight: an L2-style construct (energy norm) factored cleanly through L1 leaves.

The sibling operator [`bilinear_form`](./bilinear_form.md) depends on the same two L1 primitives but with a different composition `dot(apply_linop(A, x), y)` — the energy norm is the diagonal case `y = x` plus the outer square root, and the SPD applicability condition.

## Variant axes

`matrix_weighted_norm` has two orthogonal variant axes at L1:

- **element-type**: `real` | `complex`. At L0 these are template specializations of `linalg::Norml2<VecType>` (`VecType ∈ {Vector, ComplexVector}`, `palace/linalg/operator.cpp:599-619`). At L1 these **collapse to a single operator** with the same signature `(x: Tensor[N], B: LinearOperator[N, N]) → Scalar(real)`, because the result is real-valued regardless of input element type (the SPD precondition guarantees `xᴴ B x ∈ ℝ_{≥0}`) and all the algebraic laws hold uniformly. The complex specialization's per-component `B.Mult(x.Real(), Bx.Real()); B.Mult(x.Imag(), Bx.Imag())` plumbing (lines 613-614) reflects an L0 convention that `B` is real-valued even when `x` is complex; at L1 this is absorbed by `apply_linop`'s element-type variant axis.
- **output-arg vs return-value pattern**: at L0 the workspace `Bx` is a caller-supplied destination buffer; the L0 caller pre-allocates `Bx` and reuses it across calls (e.g. `palace/linalg/arpack.cpp:438` reuses `Bx` across each eigenvector). At L1 this distinction is erased — the operator returns a fresh scalar with no destination buffer. The `Bx`-as-workspace lifetime, allocation, and reuse become an L1>L0 lowering concern.

Collapsed (absorbed) axes:

- **parallel-wrapper**: the L0 `Norml2(comm, x, B, Bx)` takes an MPI communicator; single-rank is in scope per `CLAUDE.md` "Scope". At L1 the communicator is absorbed (the L1 reduction is one semantic step). The MPI collective reappears in the L1>L0 lowering, inherited from `dot`'s lowering.
- **operator-representation of `B`**: at L0 `B` may be any concrete subclass of `Operator` (real branch); per `apply_linop`'s variant absorption, this is collapsed at L1 to the opaque `LinearOperator[N, N]` type. Sparse-matrix / matrix-free / composition / multigrid representations of `B` are all admitted; the L1 contract sees only the linear-map interface.

The output-arg vs return-value axis is L1-level (the L1 form picks return-value uniformly); the operator-representation collapse follows `apply_linop`'s precedent. The L1 form treats the **complex-x-with-real-B** specialization as a uniform element-type rule (the per-component `B.Mult` on `x.Real()`/`x.Imag()` is L0 plumbing absorbed by `apply_linop`'s element-type variant axis), not a distinct L1 variant.

## L1 vs L0 distinction

- **L0**: free-function template `linalg::Norml2(MPI_Comm, x, B, Bx)` with two specializations (`Vector` and `ComplexVector`). Caller supplies the workspace `Bx`. Performs `B.Mult(x, Bx); dot = Dot(comm, Bx, x); return std::sqrt(dot)` with a `MFEM_ASSERT(dot > 0.0)` defensive guard. Complex specialization decomposes by real/imaginary parts because `B` is real. The reduction tree is pinned (Hypre + MPI). Single-rank is in scope; the `MPI_Allreduce` is inside the inner `Dot`.
- **L1**: pure functional energy-norm `α = matrix_weighted_norm(x, B)`. No workspace `Bx` in the signature. No MPI collective. No element-type-decomposition plumbing on the complex branch — collapsed to one operator parameterised by element type. The `MFEM_ASSERT` becomes the explicit SPD applicability condition. The composition `√(dot(apply_linop(B, x), x))` is the unfolding produced by the L1>L0 lowering theme (not yet authored); at L1 the operator is a single semantic step.

## Evidence

- `palace/linalg/operator.hpp:372-374` — `linalg::Norml2(comm, x, B, Bx)` template declaration with the comment `Calculate the vector norm with respect to an SPD matrix B.` (line 372). Direct evidence of the SPD precondition statement at L0.
- `palace/linalg/operator.hpp:377-384` — `linalg::Normalize(comm, x, B, Bx)` inline definition: calls `Norml2`, asserts `norm > 0.0`, then `x *= 1.0 / norm`. Confirms `Norml2`'s output is a positive real used as a divisor.
- `palace/linalg/operator.cpp:599-607` — real specialization body: `B.Mult(x, Bx); double dot = Dot(comm, Bx, x); MFEM_ASSERT(dot > 0.0, ...); return std::sqrt(dot);`. Direct evidence of the closed-form `√(xᴴ B x)` via the three-step composition.
- `palace/linalg/operator.cpp:609-619` — complex specialization body: split `B.Mult` into `Real()` / `Imag()` calls, compute `std::complex<double> dot = Dot(comm, Bx, x)`, assert `dot.real() > 0.0 && std::abs(dot.imag()) < 1.0e-9 * dot.real()`, return `std::sqrt(dot.real())`. Direct evidence of the SPD-implies-real Hermitian self-bilinear and the round-off-only imaginary-part guard.
- `palace/linalg/arpack.cpp:433-444` — `ArpackEigenvalueSolver::GetEigenvectorNorm`: dispatches to `linalg::Norml2(comm, x, *opB, Bx)` when `opB` is non-null, else falls back to plain `linalg::Norml2(comm, x)`. Direct callsite evidence of the SPD-weighted norm in the eigensolver M-orthonormalisation pipeline.
- `palace/linalg/arpack.cpp:470` — `xscale.get()[i] = 1.0 / GetEigenvectorNorm(x1, y1);` — the scaling factor for M-orthonormalisation derives from the weighted norm.
- `palace/linalg/slepc.cpp:470-481` — `SlepcEigenvalueSolver::GetEigenvectorNorm`: identical pattern (SLEPc backend).
- `palace/linalg/slepc.cpp:505` — analogous `xscale` computation in SLEPc.
- `palace/linalg/nleps.cpp:109-119` — `NonLinearEigenvalueSolver::GetEigenvectorNorm`: identical pattern (NLEPS backend). Three-backend consistency confirms the operator's role as the M-orthonormalisation norm primitive.
- `palace/linalg/nleps.cpp:146` — analogous `xscale` computation in NLEPS.
- `book/src/L0/linalg-operator-file.md:30-33` — the L0 chapter naming the `linalg::` free-function block, including the SPD-weighted `Norml2(comm, x, B, Bx)` and the (sibling) bilinear_form `Dot(comm, x, A, y)`.
- `book/src/L1/nrm2.md:13` — sibling-boundary statement: "The B-weighted overload `linalg::Norml2(comm, x, B, Bx)` at `palace/linalg/operator.cpp:600-619` is **not** part of this operator. ... It is a separate L1 operator candidate (forthcoming) that depends on both `dot` and the operator-application primitive `apply_linop`." Direct precedent / motivating reference.
- `book/src/L1/nrm2.md:100` — the same boundary statement reiterated in the Evidence section ("declaration of the B-weighted overload `Norml2(comm, x, B, Bx) → double`. Recorded here to mark the boundary").
- `book/src/L1/dot.md:43-49`, `book/src/L1/apply_linop.md:46-57` — algebraic-law dependencies (`dot`'s Hermitian-sesquilinear laws 7-9; `apply_linop`'s linearity law 1) that underwrite the closed-form `√(xᴴ B x)` derivation in this entry.
- `palace/drivers/eigensolver.cpp:205-213` — positive L0 home of the SPD premise: the source comment (`:206-207`) names `KM` as "the real SPD part of the mass matrix", `KM = GetInnerProductMatrix(0.0, 1.0, nullptr, M.get())` then `SetBMat(*KM)` — this is the `B` reaching `Norml2`'s `opB`, SPD by construction. Grounds the SPD applicability condition under which laws 4/6/7 (triangle, Cauchy–Schwarz, parallelogram) hold as inner-product-space theorems.
- `palace/models/spaceoperator.cpp:530-537` — SPD construction provenance: `GetInnerProductMatrix(0.0, 1.0, nullptr, M)` builds `BuildParSumOperator` with `1.0·M->Real()`, the real part of the FE mass matrix; the positive-coefficient mass form is SPD (strictly positive eigenvalues).
- `test/unit/test-domainpostoperator.cpp:75-93` — "DomainPostOperator - Electric Energy Units" positively covers the SPD-weighted radicand `⟨E, M_elec E⟩` + `½` scaling (the law-8 self-bilinear constituent) via `WithinRel` against the closed-form `½·ε₀·E₀²·V` (the `GetElectricFieldEnergy` body, `palace/models/domainpostoperator.cpp:219-231`: `M_elec->Mult(E.Real(),D); dot = LocalDot(E.Real(),D); return 0.5*dot`). It covers the radicand, not the outer `√` nor the named `Norml2(comm,x,B,Bx)` entry point.
