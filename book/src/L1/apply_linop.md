# apply_linop

Mutation-lifted linear-operator application: `y = A · x` for an abstract linear operator `A`. The opaque-operator primitive at L1; the unit of operator-cost accounting for iterative solvers and the gate to the L2 `krylov-step` vocabulary.

## Context

`apply_linop` lifts the entire `Mult` / `MultTranspose` / `MultHermitianTranspose` / `AddMult` virtual-method family on the parallel `Operator` (real) / `ComplexOperator` (complex) base classes, across all concrete subclasses (`SumOperator`, `BaseProductOperator`, `BaseDiagonalOperator`, `BaseMultigridOperator`, `ComplexWrapperOperator`, `ParOperator`, `ComplexParOperator`, all preconditioners, all FE assembly closures, all Jacobian-action operators), to a single pure-functional operator-application primitive `y = A·x` over an opaque `LinearOperator[M, N]` type. The full overload set, sub-axes (transpose mode, accumulate mode, element type), and concrete-subclass roster are detailed in [`L0/apply-linop-overload-set`](../L0/apply-linop-overload-set.md). The output-arg mutation idiom (`A.Mult(x, y)` writes through `y`) is named in [`L0/output-arg-vs-receiver`](../L0/output-arg-vs-receiver.md). The element-type axis (`Operator` vs `ComplexOperator`, plus the `Par*` parallel-wrapper axis read as single-rank per CLAUDE.md Scope) is named in [`L0/mfem-vector-types`](../L0/mfem-vector-types.md). The `Mult → AddMult` fused-zero-init dispatch in `SumOperator` and the matrix-free element-summation-order load-bearing case are classified in [`L0/transparent-vs-load-bearing-tricks`](../L0/transparent-vs-load-bearing-tricks.md).

At L0, the in-place destination `y` is overwritten; the operator `A` is read-only (the methods are `const`); workspace tensors are private to the operator's representation (e.g. `BaseProductOperator::z`, `palace/linalg/operator.hpp:192`). The L1 form drops the destination-buffer mention: the operator consumes `A` and `x`, produces a fresh output. Workspace, in-place overwrite, and the choice of representation (sparse / dense / matrix-free / composition / multigrid) are all L0 concerns; they reappear in the L1>L0 lowering theme, not in the L1 signature.

A cross-cutting prose treatment lives at [`concepts/apply_linop`](../concepts/apply_linop.md) — covering background (BLAS-2 generalisation), constructed-operator chains, and slice-level use across CG / GMRES / divfree. The L1 entry here is the firm operator definition; the concept page is the narrative.

## Signature

```
apply_linop :: (A: LinearOperator[M, N], x: Tensor[N]) -> Tensor[M]
apply_linop(A, x) = A · x
```

Shape contract (bunsen-style, named axes):

- `A` — `LinearOperator[M, N]` — a linear map from a domain space of axis `N` to a codomain space of axis `M`. Read-only.
- `x` — `Tensor[N]` — the input vector. Read-only. Must match the operator's domain axis.
- result — `Tensor[M]` — the output vector. Same axis `M` as the operator's codomain.

The axes `M` and `N` are independent in general — `A` may be rectangular. For square operators (the common case in iterative solvers: `A` is square in CG and GMRES, both squares of dimension `M = N`), the codomain and domain coincide. For prolongation/restriction operators (e.g. `trial_fespace.GetProlongationMatrix()` at `palace/linalg/rap.cpp:212`) and discrete differential operators (`Grad`: H1 → Nedelec; `WeakDiv`: Nedelec → H1), `M ≠ N` is genuine.

The element type of `A`, `x`, and the result must all match (all real or all complex). Palace exposes this as the `Operator` (real) vs `ComplexOperator` (complex) hierarchy split — see Variant axes.

`LinearOperator[M, N]` is an *opaque type* at L1: it has a domain axis `N`, a codomain axis `M`, and is guaranteed linear (see Algebraic laws). Its internal representation (sparse / dense / matrix-free / composition) is not part of the L1 signature; the L1 entry collapses across all L0 representations.

## Semantics

`apply_linop(A, x)` returns the image of `x` under the linear map `A`. The result is determined entirely by `A` and `x`; the L1 form is pure functional — applying the same `A` to the same `x` returns the same value. The L0 source overwrites the in-place destination buffer `y`; the L1>L0 lowering theme is where that overwrite is reintroduced (and where workspace ownership of intermediate buffers like `BaseProductOperator::z` becomes explicit).

Linearity is the defining property: `apply_linop(A, α·x + β·y) = α·apply_linop(A, x) + β·apply_linop(A, y)`. This is what makes `A` a *linear* operator rather than a general function; nonlinear actions (e.g. Jacobian evaluation at a moving point, semi-discrete time-step operators with state-dependent matrices) are not `apply_linop` — they go through a different L1 primitive when one is introduced.

Reduction-tree non-associativity is **load-bearing** in the CLAUDE.md sense for matrix-free operators that involve quadrature summation: different summation orders over element contributions produce different bit-level results. Palace's L0 implementation pins specific orderings via the underlying kernels (MFEM partial-assembly, libCEED, Hypre SpMV); a different ordering gives a different output at the bit level even though all are valid implementations of the L1 operator. For exactly-representable element-local applies followed by gather/assembly via a deterministic mapping (e.g. an assembled sparse matrix in a fixed CSR ordering), no such concern arises — the result is bit-deterministic given the ordering. This load-bearing distinction is recorded here, not erased.

Variant transpose modes (`Mult`, `MultTranspose`, `MultHermitianTranspose`) are **not** separate operators at L1. They are recoverable from the L1 operator by replacing `A` with the appropriate algebraic transform: `apply_linop(Aᵀ, x)`, `apply_linop(Aᴴ, x)`. The L0 source has dedicated virtual methods because the operator's internal representation may permit a more efficient transpose path than constructing an explicit transposed operator (e.g. swapping prolongation and restriction roles in `ParOperator::MultTranspose`, `palace/linalg/rap.cpp:236-275`); this is an L0 representation-aware specialisation, recorded in the L1>L0 lowering, not in the L1 signature.

Constructed operators (`A · B`, `M⁻¹ · A`, `Gᵀ M G`, etc.) are not a separate L1 operator either — they are values of type `LinearOperator[M, N]` formed by other operator-level constructors (operator composition, sum, scaling). The fact that `apply_linop(A · B, x)` may internally compose two `Mult` calls (e.g. `BaseProductOperator::Mult` at `palace/linalg/operator.hpp:202-206` calls `B.Mult(x, z); A.Mult(z, y)`) is an L0 implementation detail; at L1 the composition is preserved as an algebraic identity (see law 4 below). See [`concepts/constructed-operators`](../concepts/constructed-operators.md) for the narrative.

The accumulating form `AddMult` (`y ← y + a · A · x`) is not a separate L1 operator either — it is algebraically `axpby(a, apply_linop(A, x), 1, y)`, a composition of two L1 primitives. The L0 source provides `AddMult` as a fused method for two reasons: (i) it permits skipping the zero-initialisation of `y` (a transparent performance trick at L1), and (ii) for matrix-free operators it permits accumulating element contributions directly into `y` without a separate temporary (also transparent algebraically, but load-bearing for memory traffic). Both are L1>L0 lowering concerns.

## Algebraic laws

The laws below hold; absences are deliberate.

1. **Linearity in `x`**: `apply_linop(A, α·x + β·y) = α·apply_linop(A, x) + β·apply_linop(A, y)` for any scalars `α`, `β` and any vectors `x`, `y` in the domain of `A`. This is the defining property — it is what distinguishes `apply_linop` from a general (nonlinear) function-application primitive.
2. **Zero-vector annihilation**: `apply_linop(A, 0) = 0` (where the left `0` is the zero vector of axis `N` and the right `0` is the zero vector of axis `M`). Follows from law 1 with `α = β = 0`.
3. **Identity operator**: `apply_linop(I, x) = x` for the identity operator `I : V → V` (where `V` is some space with axis `N`; in this case `M = N`). The identity-operator construct is exposed in the L0 surface implicitly (any operator that returns the trivial implementation `y = x`); at L1 this is a named algebraic identity.
4. **Composition (operator product)**: `apply_linop(A · B, x) = apply_linop(A, apply_linop(B, x))` where `A · B` is the operator-composition construct (an operator with domain matching `B`'s domain and codomain matching `A`'s codomain, requiring `B`'s codomain axis to equal `A`'s domain axis). Witnessed in the L0 source by `BaseProductOperator::Mult` at `palace/linalg/operator.hpp:202-206`: `B.Mult(x, z); A.Mult(z, y)` — the two-step apply is the L0 unfolding of the L1 composition identity. This law is what enables constructed-operator chains like `apply_BA = A · M⁻¹` to be unfolded into a sequence of single-operator applies at L2.
5. **Sum operator distributes over addition (operator-side linearity)**: `apply_linop(A + B, x) = apply_linop(A, x) + apply_linop(B, x)` where `A + B` is the operator-sum construct (both `A` and `B` share the same domain and codomain axes). Witnessed by `SumOperator::Mult` at `palace/linalg/operator.cpp:428-441` plus `SumOperator::AddMult` at `palace/linalg/operator.cpp:458-466` (the accumulating loop `y.Add(a*c, z)` over each operator's contribution).
6. **Scaled operator (operator-side scalar absorption)**: `apply_linop(α·A, x) = α·apply_linop(A, x)` for any scalar `α`. Witnessed by `SumOperator::Mult` at `palace/linalg/operator.cpp:430-437` (single-operator fast path applying `y *= c` after `Mult` when the coefficient is non-unit). At L1 this is the algebraic statement; the L0 implementation realises it by composing `Mult` with a scalar-times-vector update.
7. **Zero operator**: `apply_linop(0, x) = 0` for the zero operator `0 : V → W`. Special case of law 6 with `α = 0`.

Laws that explicitly **do not** hold:

- **Commutativity of operator composition**: `apply_linop(A · B, x) ≠ apply_linop(B · A, x)` in general. Operator product is non-commutative (it is matrix multiplication in the assembled-operator case); only in special structured cases (e.g. simultaneously diagonalisable operators) does the equality hold. Recorded as an absence because callers must not assume it.
- **Self-inverse / involutivity**: `apply_linop(A, apply_linop(A, x)) ≠ x` in general. Only true for involutive `A` (e.g. reflections, where `A² = I`). Most operators in Palace's solver corpus are not involutive.
- **Bit-determinism across operator representations**: a sparse-matrix realisation of `A` and a matrix-free realisation of the *same* mathematical operator produce results that agree mathematically but may differ at the bit level (different summation orders in the assembly / quadrature stage). Load-bearing per the CLAUDE.md taxonomy: the choice of representation can change the bit-level output even though the algorithmic correctness is preserved. The mathematical laws above hold; their floating-point realisations are exact modulo summation-order noise inherited from the underlying kernel.
- **Floating-point linearity strictness**: law 1 is the mathematical identity in ℝ / ℂ. In IEEE-754 the equality is approximate (the two sides round differently); the difference is bounded by the operator's condition number and the working precision. Algorithms that depend on exact linearity (e.g. some recurrence-residual update schemes that recompute the residual to check the recurrence) must guard.

## Dependencies

None at L1. `apply_linop` is a leaf primitive at L1 — alongside `axpy`, `axpby`, `dot`, and `nrm2`, it is one of the foundational L1 operators. Its sub-operations are the operator's internal evaluation (element-local kernels, SpMV inner loops, multigrid V-cycles, etc.) — all below the L1 layer's resolution and visible only in the L1>L0 lowering.

`apply_linop` is the operator-application primitive that the L2 `krylov-step` will depend on (forthcoming). At L2, the operator-application count is the standard cost metric for iterative solvers; each L2 step (CG inner iteration, GMRES Arnoldi step, MGS orthogonalisation pass) is characterised by its number of `apply_linop` calls. The L2 vocabulary names these as opaque primitives rather than unfolding them into per-element loops — see [`concepts/apply_linop`](../concepts/apply_linop.md) "Role in the L2 vocabulary".

The accumulating form `AddMult(A, x, a, y) → y + a · A · x` is **not** a separate L1 operator (per the Semantics section): it is the L1 composition `axpby(a, apply_linop(A, x), 1, y)` — a sibling-leaf composition, not a dependency. The L0 source provides `AddMult` as a fused method for performance; the L1>L0 lowering reintroduces the fusion as a transparent performance trick.

## Variant axes

`apply_linop` has three orthogonal variant axes at L1; a fourth axis is collapsed and recorded as deliberate absorption.

- **element-type**: `real` | `complex`. The L0 source splits this into two parallel class hierarchies — `Operator` (real, base `mfem::Operator::Mult`) and `ComplexOperator` (complex, `palace/linalg/operator.hpp:24-68`). At L1 these collapse to one operator parameterised by element type. The semantics are identical across element types — the per-operator linear-map relationship is the same; only the field of the underlying scalar differs.
- **transpose-mode**: `forward` | `transpose` | `hermitian-transpose`. The L0 source exposes three dedicated virtual methods (`Mult`, `MultTranspose`, `MultHermitianTranspose`, `operator.hpp:54-58`) because the operator's internal representation may permit more efficient transpose paths than constructing an explicit transposed operator. At L1 these are **not** separate operators — they are recoverable via `apply_linop(Aᵀ, x)` and `apply_linop(Aᴴ, x)` from the algebraic transforms `Aᵀ` and `Aᴴ` of the operator. The L1>L0 lowering reintroduces the dedicated virtual methods as a representation-aware specialisation; at L1 there is one operator. (For real operators the hermitian-transpose collapses to the transpose; `MultHermitianTranspose` is meaningful only on `ComplexOperator`.)
- **accumulate-mode**: `overwrite` | `accumulate`. The L0 source exposes `Mult` (overwriting) and `AddMult` (accumulating; `operator.hpp:60-67`) as separate virtual methods. At L1 these are **not** separate operators — the accumulating form is the composition `axpby(a, apply_linop(A, x), 1, y)`. The L1>L0 lowering theme reintroduces the fusion as a transparent performance trick (skipping zero-initialisation; for matrix-free operators, fusing element-contribution accumulation directly into `y`).

Collapsed (absorbed) axis:

- **operator-representation**: `sparse-matrix` | `dense-matrix` | `matrix-free` | `composition` | `multigrid` | `block` | `wrapped` | ... At L0 these are concrete subclasses of the `Operator` / `ComplexOperator` interface (`SumOperator`, `BaseProductOperator`, `BaseDiagonalOperator`, `BaseMultigridOperator`, `ComplexWrapperOperator`, `ParOperator`, `ComplexParOperator`, all preconditioners, all FE assembly closures, ...). At L1 these **collapse to a single `LinearOperator` opaque type** — the L1 contract sees only the linear-map interface and the domain/codomain axes; the internal representation is an L0 concern that surfaces only in the L1>L0 lowering theme (and in load-bearing numerical caveats like reduction-tree non-associativity for matrix-free representations). This is the canonical *variant absorption* application (per [`concepts/variant-absorption`](../concepts/variant-absorption.md)).

## Status

`firm` — signature is canonical (matches the abstract `Mult` virtual on both the real and complex operator hierarchies, parameterised by element type), evidence is direct from the Palace source (abstract decls + concrete realisations + use sites in iterative solvers), and the algebraic laws listed are standard properties of linear maps modulo the explicitly-recorded floating-point caveats.

## L1 vs L0 distinction

- **L0**: a family of virtual `Mult(x, y) const` methods (and their transpose / accumulating variants) on a deep class hierarchy. Writes through the output argument `y`. Internal workspace tensors are members of the concrete operator subclass (e.g. `BaseProductOperator::z`, `palace/linalg/operator.hpp:192`; `SumOperator::z`, `operator.hpp:120`). Reduction order is pinned by the underlying kernel (MFEM partial-assembly / libCEED / Hypre SpMV). Transpose and accumulating modes are separate virtual methods for representation-aware specialisation. The `ParOperator::Mult` path applies prolongation, calls the inner operator, then applies restriction, with optional Dirichlet-BC tdof masking around the call (`palace/linalg/rap.cpp:195-234`).
- **L1**: pure functional application. `y = apply_linop(A, x)`. No destination buffer in the signature. No workspace ownership. One operator parameterised by element type; transpose-mode is recoverable via `Aᵀ`, `Aᴴ`; accumulating-mode is the composition with `axpby`. Operator representation (sparse / dense / matrix-free / composition / multigrid / parallel / wrapped) is collapsed to a single opaque `LinearOperator` type. Algebraic laws (linearity, composition, sum, scaling) apply directly. Floating-point evaluation-order non-associativity is recorded as an explicit non-law, classified as load-bearing for bit-reproduction but not for algorithmic correctness.

## Evidence

- `palace/linalg/operator.hpp:21` — `using Operator = mfem::Operator;` — the real-operator type alias inheriting the abstract `mfem::Operator::Mult(const Vector &x, Vector &y) const` virtual.
- `palace/linalg/operator.hpp:24-68` — `ComplexOperator` abstract class: declares pure virtual `Mult` (line 54), plus `MultTranspose` (56), `MultHermitianTranspose` (58), and the accumulating forms `AddMult` / `AddMultTranspose` / `AddMultHermitianTranspose` (60-67).
- `palace/linalg/operator.hpp:36-39` — `Height()` / `Width()` accessors confirming the operator has domain (`Width`) and codomain (`Height`) axes that may differ (rectangular operators).
- `palace/linalg/operator.hpp:116-136` — `SumOperator` declaration: `Mult`, `MultTranspose`, `AddMult`, `AddMultTranspose` all overridden; coefficient list `std::vector<std::pair<const Operator *, double>> ops`.
- `palace/linalg/operator.hpp:178-229` — `BaseProductOperator` template: the operator-composition construct. `Mult` definition at `operator.hpp:202-206` shows the two-step `B.Mult(x, z); A.Mult(z, y)` — direct witness of algebraic law 4 (composition).
- `palace/linalg/operator.hpp:298-367` — `BaseMultigridOperator` template: dispatches `Mult` / `MultTranspose` / `AddMult` / `AddMultTranspose` to the finest-level operator. Confirms that even multigrid hierarchies expose the same single `Mult` interface at L0.
- `palace/linalg/operator.cpp:428-441` — `SumOperator::Mult` definition: single-operator fast path with optional scaling (witnesses law 6); multi-operator path zeros `y` then calls `AddMult` (witnesses the L0 dispatch `Mult → AddMult` reuse pattern).
- `palace/linalg/operator.cpp:458-466` — `SumOperator::AddMult` definition: loop over operators, applying each into workspace `z` and accumulating with `y.Add(a * c, z)`. Witnesses laws 5 (sum) and 6 (scaling) in the assembled L0 form.
- `palace/linalg/rap.cpp:195-234` — `ParOperator::Mult` definition: parallel-wrapper apply with prolongation, inner-operator call (`A->Mult(lx, ly)` at line 220), restriction, and Dirichlet-BC tdof masking. Witnesses that even with parallel wrapping the abstract interface is preserved (the single-rank reading per CLAUDE.md Scope reduces this to inner-operator-plus-BC-masking).
- `palace/linalg/rap.cpp:481-517` — `ComplexParOperator::Mult` definition: complex analogue of the above.
- `palace/linalg/iterative.cpp:379, 443` — CG using `A->Mult(x, r)` for residual computation and `A->Mult(p, z)` for the inner-loop matrix-vector product. Direct evidence `apply_linop` is the per-step primitive in CG.
- `palace/linalg/iterative.cpp:544-734` — GMRES `Mult` body using `A->Mult` for Arnoldi-step matrix-vector products. Confirms `apply_linop` is the per-step primitive in GMRES.
- `book/src/concepts/apply_linop.md` — cross-cutting prose treatment (predates this L1 firm-up; covers BLAS-2 generalisation, constructed-operator chains, and slice-level use across CG / GMRES / divfree).
- `book/src/concepts/constructed-operators.md` — narrative for the operator-composition construct underwriting algebraic law 4.
- `book/src/concepts/variant-absorption.md` — narrative for the operator-representation axis collapse.
