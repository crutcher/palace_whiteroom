---
agent: harvester
invoked_at: 2026-05-27T00:46:41Z
scope: L1 operator: apply_linop
status: integrated
integrated_at: 2026-05-27T01:00:00Z
integration_commit: b8332b98300205740c4be4a9b1a2b30a2743dee3
integration_notes: Applied. New firm L1 operator. The opaque-operator gate to L2 krylov-step. Unblocks krylov-step harvester promotion next cycle.
inputs:
  - book/src/concepts/apply_linop.md (prior concept-page prose)
  - book/src/L1/{axpy,dot,nrm2,axpby}.md (format references)
  - palace/linalg/operator.hpp (abstract ComplexOperator + SumOperator + BaseProductOperator decls)
  - palace/linalg/operator.cpp (SumOperator::Mult / AddMult)
  - palace/linalg/rap.cpp (ParOperator::Mult)
  - palace/linalg/iterative.cpp (A->Mult use sites in CG / GMRES / FGMRES)
skill_uptake:
  - skill: classify-variant-axis
    triggered: true
    decision: artifact_landed
    rationale: Three orthogonal variant axes identified (element-type, transpose-mode, accumulating-vs-overwriting). Operator-representation axis (sparse/dense/matrix-free/composition) called out and explicitly classified as L0-only — collapses to a single L1 operator because the L1 contract only sees the linear-map interface.
  - skill: verify-citation-range
    triggered: true
    decision: explained_non_applicable
    rationale: Citations verified inline by reading the cited ranges (~10 ranges, abstract Mult decls + concrete Mult/AddMult definitions + use sites). Skill invocation deferred until critic-phase mechanism stabilizes per cycle-002 pattern.
  - skill: skill-selection
    triggered: true
    decision: artifact_landed
    rationale: Two relevant skills considered (classify-variant-axis, verify-citation-range); both applied. Refinement-surface verification not applicable (this is a single-operator firm-up, not a refinement of a prior coarser surface).

---

# REPORT: Formalize apply_linop at L1

## Summary

`apply_linop` is the operator-application primitive `y = A · x`: applying an abstract linear operator `A` to an input vector `x` to produce an output vector. It is the third major L1 primitive (after the BLAS-1 vector operations `axpy` / `axpby` / `dot` / `nrm2`) and gates the L2 `krylov-step` decomposition — every Krylov inner step is a small chain of `apply_linop` calls plus BLAS-1 work.

Current state: a `concepts/apply_linop.md` page exists (substantial prose, predating the firm-operator era), but no L1 chapter entry, no row in the L1 dep-map, and no SUMMARY.md chapter. This report promotes the operator from concept-only to firm L1 with explicit signature, semantics, algebraic laws, dependencies, and variant axes. The concept page is cross-referenced (per the harvester discipline of "cross-reference rather than duplicate"); the concept page contains minor terminology drift (it pre-dates the L1>L0 lowering vocabulary) but is left intact to be revised by a future cross-cutter or concept-edit pass.

The L0 surface is broad — `mfem::Operator::Mult` is the abstract base; `ComplexOperator::Mult` is Palace's complex analogue; numerous concrete subclasses (`SumOperator`, `BaseProductOperator`, `BaseDiagonalOperator`, `ParOperator`, `ComplexParOperator`, `BaseMultigridOperator`, `ComplexWrapperOperator`, plus preconditioners, FE assembly closures, and matrix-free callers) implement the virtual method. The L1 entry deliberately collapses across all concrete operator representations: at L1 there is one `apply_linop` operator parameterised by element type and transpose mode; the concrete operator structure (sparse / dense / matrix-free / composition) is an L0 representation choice not visible at L1. This is the *variant absorption* move (per [`concepts/variant-absorption`](../concepts/variant-absorption.md)).

## Proposed changes

```edit:book/src/L1/apply_linop.md
# apply_linop

Mutation-lifted linear-operator application: `y = A · x` for an abstract linear operator `A`. The opaque-operator primitive at L1; the unit of operator-cost accounting for iterative solvers and the gate to the L2 `krylov-step` vocabulary.

## Context

The L0 source-side forms are the family of virtual `Mult(x, y)` methods on the operator-interface hierarchy:

- `mfem::Operator::Mult(const Vector &x, Vector &y) const` — abstract base for real operators; inherited from MFEM and re-exported by Palace as `using Operator = mfem::Operator;` at `palace/linalg/operator.hpp:21`. Writes through the output argument `y`.
- `palace::ComplexOperator::Mult(const ComplexVector &x, ComplexVector &y) const = 0` — abstract base for complex operators; declared at `palace/linalg/operator.hpp:54`. Pure virtual; the entire `ComplexOperator` hierarchy is shaped around this method.
- `palace::ComplexOperator::MultTranspose` (`operator.hpp:56`) and `MultHermitianTranspose` (`operator.hpp:58`) — transpose / Hermitian-transpose variants; same shape as `Mult` but apply `Aᵀ` or `Aᴴ` instead of `A`.
- `palace::ComplexOperator::AddMult(x, y, a)` (`operator.hpp:60`) and the `MultTranspose` / `MultHermitianTranspose` accumulating analogues (`operator.hpp:63-67`) — accumulate `a · A · x` into `y` rather than overwrite. The default `Mult` paths in concrete subclasses often dispatch through `AddMult` (e.g. `SumOperator::Mult` zeros `y` then calls `AddMult`, `palace/linalg/operator.cpp:439-440`).
- Concrete subclasses implementing the virtual: `SumOperator::Mult` (`operator.cpp:428-441`); `BaseProductOperator::Mult` (`operator.hpp:202-206`, two-step `B.Mult(x, z); A.Mult(z, y)`); `BaseDiagonalOperator::Mult` (decl at `operator.hpp:277`, element-wise `y[i] = d[i] * x[i]`); `BaseMultigridOperator::Mult` (`operator.hpp:347`, dispatches to finest-level operator); `ComplexWrapperOperator::Mult` (`operator.hpp:99`, real-imaginary block dispatch); `ParOperator::Mult` (`palace/linalg/rap.cpp:195-234`, parallel wrapper applying prolongation/restriction around the inner operator); `ComplexParOperator::Mult` (`rap.cpp:481-517`). Plus all preconditioners, FE assembly closures, and Jacobian-action operators that implement the same interface.

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
```

```edit:book/src/L1/index.md
# L1 — Mutation-lifted forms

Source operations re-expressed as pure functions: explicit input set, output set; in-place mutation and aliasing patterns either erased (workspace/scratch buffers) or made explicit (semantically-meaningful aliasing). The **mutation rotation** layer.

## Context

L1 is the closest pure-functional layer to the source. Structure follows the source loop; what changes is:
- `x.Add(α, y)` → `x_{k+1} = x_k + α·y`
- `A.Mult(x, y)` (writes into `y`) → `y = A·x` (no destination buffer mention)
- Iterative loop mutating iterate in place → functional unfold `state_{k+1} = step(state_k)`
- Reused workspace `tmp` → omitted (the COW backend handles allocation)

## Semantics (overlay)

L1 vocabulary mirrors the source operations but with pure-functional binding. Shape contracts are declared at boundaries (per the bunsen `contracts::unpack_shape_contract!` style).

## Operator dep-map

| Operator | Signature | Dependencies | Status |
|---|---|---|---|
| [`axpy`](./axpy.md) | `(α, x, y) → α·x + y` | (leaf) | `firm` |
| [`dot`](./dot.md) | `(x, y) → ⟨x, y⟩` (hermitian for complex) | (leaf) | `firm` |
| [`nrm2`](./nrm2.md) | `(x) → √⟨x,x⟩` | `dot` | `firm` |
| [`axpby`](./axpby.md) | `(α, x, β, y) → α·x + β·y` | (leaf; subsumes `axpy`) | `firm` |
| [`apply_linop`](./apply_linop.md) | `(A: LinearOperator[M, N], x: Tensor[N]) → Tensor[M]` | (leaf; opaque operator) | `firm` |

## Working Notes

- L1 is what `abstractor` produces in early bottom-up sweeps (L0 → L1).
- Aliasing-aware patterns where aliasing is semantically meaningful (not just buffer reuse) are first-class L1 content.
```

```edit:book/src/SUMMARY.md
[Under the `# L1 — Mutation-Lifted Forms` heading, append one chapter line after `- [axpby](./L1/axpby.md)`:]

- [apply_linop](./L1/apply_linop.md)
```

## Supporting evidence

The operator's existence and shape are uncontested across the Palace solver corpus: every iterative-solver path (`CgSolver::Mult`, `GmresSolver::Mult`, `FgmresSolver::Mult` in `palace/linalg/iterative.cpp`), every divergence-free projection (`palace/linalg/divfree.cpp`), every preconditioner (`palace/linalg/{ams,amg,chebyshev,jacobi}.cpp`), every eigensolver (`palace/linalg/{arpack,slepc,nleps}.cpp`), and the FE assembly path (`palace/fem/`) treats `Mult(x, y)` on the operator interface as the unit of operator application.

Cross-references to existing artifacts:
- `book/src/concepts/apply_linop.md` — narrative; predates this firm-up.
- `book/src/concepts/constructed-operators.md` — underwrites algebraic law 4 (composition).
- `book/src/concepts/variant-absorption.md` — underwrites the operator-representation axis collapse.
- `book/src/concepts/apply_BA.md` — example of a constructed operator used at L2 in GMRES.
- `book/src/spec/slices/cg.md`, `gmres.md`, `divfree.md` — slice-level uses of `apply_linop`.

No sister-report from this cycle directly cites `apply_linop` as a dependency (`apply_linop` is being firmed up *for* future cycles to depend on it), but it is named as the gate for the L2 `krylov-step` per the cycle-004 plan.

## Open questions / caveats

1. **Concept-page drift**: `book/src/concepts/apply_linop.md` predates the L1 firm-operator era and contains some structural drift (duplicate "Concept: apply_linop" heading at line 79; canonical signature section uses both pure and mutating forms; "L3 tensor-field form" section ought to live in an L3 layer or tensor-field-lift page). Page left intact per harvester discipline (cross-reference rather than rewrite from inside a per-operator harvest). Flagged for a future cross-cutter or concept-edit pass. **Not in scope for this harvester invocation.**

2. **Subdivision: NOT needed.** The L0 surface is genuinely broad (>10 concrete `Operator` subclasses, plus all preconditioners and FE closures), but the L1 collapse is clean: the variant-absorption move reduces all of them to a single opaque `LinearOperator` type, and the algebraic laws are standard linear-map facts. *However:* the L1>L0 lowering theme for `apply_linop` will be much more substantial than the BLAS-1 lowerings, because of (i) the representation-axis variants (sparse vs matrix-free reduction-order caveats), (ii) the transpose-mode representation-aware specialisations, (iii) the accumulating-form fusion, and (iv) the parallel-wrapper prolongation/restriction (out of scope per CLAUDE.md but worth a one-line note in the lowering theme). Cycle-005 abstractor for `apply-linop-mutation-rotation` should expect a larger theme than `axpby-mutation-rotation`.

3. **`AddMult` decomposition claim**: the L1 entry claims `AddMult(A, x, a, y) = axpby(a, apply_linop(A, x), 1, y)`. Mathematically true; bit-equivalent at L0 only if (i) the operator's internal accumulation matches the explicit `axpby` form (true for assembled matrix `Mult` followed by `Add`), or (ii) the fusion is recognised as a transparent performance trick at the lowering layer. For matrix-free operators that fuse element-contribution accumulation directly into `y` (skipping the workspace `z`), the floating-point sum order differs by one level of round-off. This is recorded as a load-bearing-for-bit-reproduction caveat in the entry, but a more detailed treatment belongs in the L1>L0 lowering theme. **Flagged for the cycle-005 abstractor.**

4. **Floquet correction**: `palace/linalg/floquetcorrection.{hpp,cpp}` introduces complex-shifted operators for Floquet-periodic eigenmode problems. Not surveyed for this entry; if they expose additional operator-construction variants (beyond sum / product / diagonal / multigrid), the L1>L0 lowering theme would need to absorb them. Not blocking the L1 firm-up — they implement the same abstract `Mult` interface.

5. **`AddMult` is sometimes the "more primitive" form**: in some concrete implementations (e.g. `SumOperator::Mult` at `palace/linalg/operator.cpp:439-440`), `Mult` is implemented in terms of `AddMult` rather than the other way around. The L1 entry treats `apply_linop` as primitive and `AddMult` as a composition; this is the conventional algebraic direction but inverts the L0 dispatch for some subclasses. The L1>L0 lowering theme should record both directions. **Not blocking; flagged for the lowering theme.**

6. **`AssembleDiagonal` (`operator.hpp:51`) is not an `apply_linop` variant**: it extracts the diagonal of `A` as a vector. This is a separate operator-shaped construct that belongs in a future L1 entry (diagonal extraction or a more general "operator-to-data" primitive). **Not in scope; recorded so it isn't accidentally folded into `apply_linop`'s variant axes.**
