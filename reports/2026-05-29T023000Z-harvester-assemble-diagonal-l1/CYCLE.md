---
agent: harvester
invoked_at: 2026-05-29T023000Z
scope: L1 operator: assemble-diagonal
status: integrated
integrated_at: 2026-05-29T08:10:00Z
integration_commit: efb8a0b
integration_notes: "cycle-019 finalize. assemble-diagonal PROMOTED stub→firm (operator-to-data (A: LinearOperator[N,N]) -> Tensor[N]; 6 laws + 4 non-laws; element-type live axis + operator-representation absorbed axis; the fifth L1 motif). L1/index Firm 11→12 + cohort bullet + dep-map row; SUMMARY de-stub. L1 firm 11→12. reciprocal/elementwise_product + assemble-diagonal-mutation-rotation L1>L0 forward-refs correctly plain-text singletons. retroactive-budget 0; clean build."
inputs:
  - book/src/L1/assemble-diagonal.md (stub, materialized 2026-05-28)
  - book/src/L1/apply_linop.md (firm; the "this is NOT an apply_linop variant" contrast)
  - book/src/L1/scal.md, book/src/L1/nrm2.md (L1 entry models)
  - book/src/L1/index.md (dep-map + cohort prose)
  - OQ assemblediagonal-is-not-apply-linop-variant
  - plan Backlog Medium diagonal-extraction-l1; roadmap §Intermediate "Diagonal-preconditioner apply"
  - palace-codemap localization of AssembleDiagonal (decls, defns, call sites, test)
---

# CYCLE: Formalize assemble-diagonal at L1

## Summary
Promotes the L1 `assemble-diagonal` stub (materialized 2026-05-28) to a **firm** L1 operator. `assemble_diagonal` is the **operator-to-data** primitive `assemble_diagonal(A) -> Tensor[N]` — it extracts the main diagonal of a square linear operator into a vector. It is harvested as a primitive *distinct* from `apply_linop`: `apply_linop` is `(Operator, Tensor) -> Tensor` (the *action* of the operator on a vector); `assemble_diagonal` is `Operator -> Tensor` (operator *introspection / materialization* — no input vector, the result is determined by `A` alone). This distinction is the substance of OQ `assemblediagonal-is-not-apply-linop-variant`, and the entry makes it explicit. The signature is canonical (matches the `AssembleDiagonal(diag)` virtual across the Palace real/complex operator hierarchies and every concrete leaf), evidence is direct from `palace/linalg/{operator,rap,hypre}.{hpp,cpp}` + `palace/fem/libceed/operator.cpp` + the `test-libceed.cpp` diagonal-assembly test, and the operator carries one load-bearing numerical caveat (the diagonal is **approximate** for matrix-free high-order Nedelec spaces — a non-law, sourced from both the Palace AMR comment and the test's relaxed tolerance). The fan-out justification (Jacobi / Chebyshev / block-Jacobi / polynomial preconditioners all reuse it) is witnessed directly: `jacobi.cpp:79` and `chebyshev.cpp:177,240` all call `op.AssembleDiagonal(dinv); dinv.Reciprocal();`.

## Proposed changes

```edit:book/src/L1/assemble-diagonal.md
[full-rewrite — stub → firm; see "Operator content" below for the file body]
```

```edit:book/src/L1/index.md
[1) cohort count "Firm (11)" → "Firm (12)"; 2) add a firm-cohort bullet for assemble-diagonal; 3) add a dep-map row. See "Wiring edits" below for exact strings.]
```

```edit:book/src/SUMMARY.md
[drop the "(stub)" label on the existing L1 chapter line so it reads as a firm chapter:
 `- [assemble-diagonal](./L1/assemble-diagonal.md)`  (was `- [assemble-diagonal (stub)](./L1/assemble-diagonal.md)`)]
```

## Operator content

The body to write into `book/src/L1/assemble-diagonal.md`:

---

# assemble-diagonal

Mutation-lifted **operator-to-data** extraction: `d = diag(A)`, the main diagonal of a square linear operator materialised as a vector. The diagonal-introspection primitive at L1 — distinct from [`apply_linop`](./apply_linop.md) (which applies the operator to a vector); `assemble_diagonal` consumes only the operator and produces operator-derived data. The gate to diagonally-scaled preconditioners (Jacobi, Chebyshev, block-Jacobi, polynomial).

## Context

`assemble_diagonal` lifts the `AssembleDiagonal(diag)` virtual-method family on the parallel `Operator` (real) / `ComplexOperator` (complex) base classes — across every concrete subclass that overrides it (`HypreCSRMatrix`, `ParOperator`, `ComplexParOperator`, `ComplexWrapperOperator`, the libCEED matrix-free `fem::libceed::Operator`) — to a single pure-functional primitive `d = diag(A)` over an opaque square `LinearOperator[N, N]`. The output-arg mutation idiom (`A.AssembleDiagonal(diag)` writes through `diag`, sizing it via `diag.SetSize(height)` / `diag = 0.0`) is the same destination-buffer pattern named in [`L0/output-arg-vs-receiver`](../L0/output-arg-vs-receiver.md) for `apply_linop`. The element-type axis (`Operator` vs `ComplexOperator`) is the same hierarchy split named in [`L0/mfem-vector-types`](../L0/mfem-vector-types.md).

**This is not an `apply_linop` variant** (OQ `assemblediagonal-is-not-apply-linop-variant`): `apply_linop` has signature `(A: LinearOperator[M, N], x: Tensor[N]) -> Tensor[M]` — it takes a vector and returns the operator's *action* on it. `assemble_diagonal` has signature `(A: LinearOperator[N, N]) -> Tensor[N]` — it takes **no vector** and returns operator-intrinsic *data*. There is no `x` to be linear in; the result is a property of `A` alone. The two share the opaque `LinearOperator` argument type and the L0 output-arg mutation idiom, but they live on opposite sides of the operator/data divide (the action of `A` versus the contents of `A`). Recording `assemble_diagonal` as its own L1 entry — rather than folding it into `apply_linop`'s variant axes — keeps that divide visible.

At L0, the in-place destination `diag` is sized and overwritten; the operator `A` is read-only (the method is `const`). For the matrix-free libCEED path the diagonal is accumulated element-by-element (`CeedOperatorLinearAssembleAddDiagonal`), and for the `ParOperator` AMR path it is assembled via the absolute-value prolongation transpose `|P|ᵀ dₗ` then has its Dirichlet true-dofs set per a `DiagonalPolicy`. The L1 form drops the destination buffer, the sizing, the workspace, and the BC-policy step: the operator consumes `A`, produces a fresh `Tensor[N]`. Workspace, in-place overwrite, the choice of representation, the absolute-value-prolongation assembly, and the Dirichlet-BC diagonal policy are all L0 concerns; they reappear in the (forthcoming) L1>L0 `assemble-diagonal-mutation-rotation` lowering theme, not in the L1 signature.

## Signature

```text
assemble_diagonal :: (A: LinearOperator[N, N]) -> Tensor[N]
assemble_diagonal(A) = diag(A)
```

Shape contract (bunsen-style, named axes):

- `A` — `LinearOperator[N, N]` — a **square** linear operator (domain axis `N` equals codomain axis `N`). Read-only.
- result — `Tensor[N]` — the diagonal vector, length `N` matching the operator's (shared) domain/codomain axis. Element `result[i]` is the `(i, i)` entry of `A`.

The square requirement (`M = N`) is intrinsic: a diagonal is only defined where the domain and codomain index sets coincide. Palace enforces this at the L0 source for the AMR path (`MFEM_VERIFY(&trial_fespace == &test_fespace, "Diagonal assembly is only available for square ParOperator!")`, `palace/linalg/rap.cpp:165`) and for the libCEED path (`MFEM_VERIFY(diag.Size() == height, ...)`, `palace/fem/libceed/operator.cpp:120`). This is the chief signature difference from `apply_linop`, which admits rectangular `M ≠ N`.

The element type of `A` and the result match (both real or both complex). Palace exposes this as the `Operator` (real) vs `ComplexOperator` (complex) hierarchy split — see Variant axes.

`LinearOperator[N, N]` is an *opaque type* at L1: it has a domain/codomain axis `N`, is guaranteed linear, and is guaranteed to expose a diagonal (see "Partial-domain" caveat under Variant axes — the base `ComplexOperator::AssembleDiagonal` aborts; only diagonal-capable subclasses are in the operator's domain). Its internal representation (sparse CSR / matrix-free / parallel-wrapped / complex-wrapped) is not part of the L1 signature; the L1 entry collapses across all L0 representations.

## Semantics

`assemble_diagonal(A)` returns the vector of main-diagonal entries of `A`: `result[i] = Aᵢᵢ = eᵢᵀ A eᵢ` for `i ∈ [0, N)`, where `eᵢ` is the `i`-th standard basis vector. The result is determined entirely by `A`; the L1 form is pure functional — extracting the diagonal of the same `A` twice returns the same value. The L0 source sizes and overwrites the in-place destination buffer `diag`; the L1>L0 lowering theme is where that overwrite, the sizing, and the workspace are reintroduced.

The relationship `result[i] = eᵢᵀ A eᵢ` is the *mathematical* definition of the diagonal, **not** the implementation: Palace never forms `N` matrix-vector products. For a sparse representation it reads the stored diagonal directly (`HypreCSRMatrix::AssembleDiagonal` calls `hypre_CSRMatrixExtractDiagonal`, `palace/linalg/hypre.cpp:88`); for a matrix-free representation it accumulates element-local diagonal contributions via libCEED (`CeedOperatorLinearAssembleAddDiagonal`, `palace/fem/libceed/operator.cpp:139`). The `eᵢᵀ A eᵢ` form is the algebraic specification the implementations realise — it is what relates `assemble_diagonal` to `apply_linop` (the diagonal entries are the would-be results of probing `A` with basis vectors) without making `assemble_diagonal` a *use* of `apply_linop`.

The diagonal is **exact** for an explicitly-assembled (sparse / Hypre CSR) representation — the stored `(i,i)` entries are read verbatim. The diagonal is **approximate** for a matrix-free high-order Nedelec (H(curl)) representation in 3D, where face dofs shared across elements make the element-local-summation diagonal differ from the true assembled diagonal. This is a **load-bearing** numerical property (per the CLAUDE.md taxonomy): the approximate diagonal is what the consuming smoothers actually use, and the approximation is acceptable *because* the diagonal feeds an inexact preconditioner (a Jacobi/Chebyshev smoother tolerates an approximate diagonal scaling). The approximation is sourced from the Palace comment at `palace/linalg/rap.cpp:163-164` (the AMR `|P|ᵀ dₗ` convergent-diagonal note) and witnessed by the test, which relaxes its tolerance to `rtol = 1.0` exactly for the high-order non-tensor-basis Nedelec case (`test/unit/test-libceed.cpp:367-376`). Recorded here as a non-law, not erased.

The accumulating element-local form `CeedOperatorLinearAssembleAddDiagonal` (matrix-free) and the `diag = 0.0` zero-initialisation that precedes it are L0 assembly mechanics; at L1 the result is the assembled diagonal value, and the zero-init / element-accumulation are L1>L0 lowering concerns (transparent for an exactly-assembled representation; the source of the approximation for the matrix-free high-order-Nedelec representation — the one case where the accumulation order is load-bearing).

The Dirichlet-boundary diagonal policy (`DiagonalPolicy::DIAG_ONE` sets BC true-dofs to `1.0`; `DIAG_ZERO` sets them to `0.0`, `palace/linalg/rap.cpp:180-191`) is **not** part of the bare `assemble_diagonal` operator: it is a BC-elimination post-step the `ParOperator` path applies after assembling the interior diagonal. At L1 this is an operator-construction concern (the operator `A` *is* the BC-eliminated operator, so its diagonal already reflects the policy) reintroduced in the L1>L0 lowering, not a parameter of `assemble_diagonal`.

## Algebraic laws

The laws below hold; absences are deliberate. (Note: these are operator-introspection laws — they relate the diagonal of a *constructed* operator to the diagonals/entries of its parts, not laws of a vector update.)

1. **Linearity over operator scaling**: `assemble_diagonal(α·A) = α·assemble_diagonal(A)` for any scalar `α`. The diagonal of a scaled operator is the scaled diagonal (each `(i,i)` entry scales). Follows from `(α·A)ᵢᵢ = α·Aᵢᵢ`.
2. **Linearity over operator sum**: `assemble_diagonal(A + B) = assemble_diagonal(A) + assemble_diagonal(B)` for square `A`, `B` sharing axis `N`. The diagonal of a sum is the sum of diagonals (`(A + B)ᵢᵢ = Aᵢᵢ + Bᵢᵢ`). Witnessed structurally by the additive complex-wrapper assembly `ComplexWrapperOperator::AssembleDiagonal` (`palace/linalg/operator.cpp:85-96`), which assembles the real and imaginary parts independently into `diag.Real()` / `diag.Imag()` after `diag = 0.0` — the diagonal of `Ar + i·Ai` is `diag(Ar) + i·diag(Ai)`.
3. **Zero operator**: `assemble_diagonal(0) = 0` (the zero vector of axis `N`). Special case of law 1 with `α = 0`. Realised at L0 by the `diag = 0.0` initialisation that an operator with no diagonal contribution leaves untouched.
4. **Identity operator**: `assemble_diagonal(I) = 𝟙` (the all-ones vector of axis `N`), since `Iᵢᵢ = 1` for all `i`. The algebraic statement of the identity operator's diagonal.
5. **Diagonal operator round-trip**: `assemble_diagonal(Diag(d)) = d` for the operator `Diag(d)` whose action is element-wise multiplication by `d` (`Diag(d)·x = d ⊙ x`). Extracting the diagonal of a diagonal operator recovers its defining vector. This is the law that makes `assemble_diagonal` the left-inverse of diagonal-operator construction — and the round-trip the diagonal-preconditioner-apply intermediate relies on (`Jacobi(A)·x = (1/diag(A)) ⊙ x`).
6. **Complex linearity (real/imag split)**: for a complex operator `A = Ar + i·Ai`, `assemble_diagonal(A) = assemble_diagonal(Ar) + i·assemble_diagonal(Ai)`. Witnessed by `ComplexWrapperOperator::AssembleDiagonal` (`palace/linalg/operator.cpp:85-96`) and `ComplexParOperator::AssembleDiagonal` (`palace/linalg/rap.cpp:467-479`), both of which assemble the real and imaginary diagonals into `diag.Real()` / `diag.Imag()` separately. A specialisation of law 2 to the equivalent-real `Ar + i·Ai` decomposition.

Laws that explicitly **do not** hold:

- **Diagonal of a product**: `assemble_diagonal(A · B) ≠ assemble_diagonal(A) ⊙ assemble_diagonal(B)` in general. The `(i,i)` entry of `A·B` is `Σ_k Aᵢₖ Bₖᵢ` — a full row·column contraction, not the product of the two `(i,i)` entries. Recorded as an absence because the diagonal-of-product is a frequent false intuition; only for *both* operators diagonal does the equality hold (then both sides equal the element-wise product). No Palace path assembles a product's diagonal this way.
- **Transpose invariance is not informative**: `assemble_diagonal(Aᵀ) = assemble_diagonal(A)` *does* hold (the diagonal is fixed under transpose, `(Aᵀ)ᵢᵢ = Aᵢᵢ`), but it is recorded as a non-distinguishing identity rather than a useful law — Palace exposes no transpose-mode axis on `AssembleDiagonal` (unlike `apply_linop`'s `Mult` / `MultTranspose`), precisely because the diagonal is transpose-invariant and a transpose variant would be redundant. For complex operators the Hermitian transpose conjugates the diagonal: `assemble_diagonal(Aᴴ) = conj(assemble_diagonal(A))`.
- **Exactness across representations**: a sparse-matrix realisation of `A` reads the exact stored diagonal, while a matrix-free high-order-Nedelec realisation of the *same* mathematical operator produces an *approximate* diagonal (face-dof sharing in 3D). Load-bearing per the CLAUDE.md taxonomy: the representation can change the diagonal value (not just its bit pattern) for the high-order-Nedelec case. The laws above hold for the exact diagonal; their matrix-free realisation may be approximate. This is the one case where the difference is semantic (a different value), not merely floating-point reduction-order noise.
- **Linearity strictness in floating point**: laws 1, 2, 6 are exact in ℝ / ℂ; in IEEE-754 the assembled diagonal sums round, so equality is approximate (and, for the matrix-free high-order case, *not even* approximate to round-off — the approximation is structural, per the previous non-law).

## Dependencies

None at L1. `assemble_diagonal` is a **leaf primitive** at L1 — a sibling of `apply_linop` on the opaque-`LinearOperator` side of the vocabulary (operator-to-data, where `apply_linop` is operator-and-vector-to-vector). Its sub-operations are the operator's internal diagonal extraction (Hypre CSR diagonal read, libCEED element-local diagonal accumulation, prolongation-transpose assembly) — all below the L1 layer's resolution and visible only in the L1>L0 lowering.

It is **not** factored through `apply_linop` despite the algebraic specification `result[i] = eᵢᵀ A eᵢ`: that specification is the mathematical definition, not the implementation (Palace forms no basis-vector probes), and treating it as a dependency would falsely imply `N` operator applies. The two are siblings, not a chain.

Downstream consumers at L1 (cross-reference, not reverse-dependencies) — the fan-out that motivated harvesting this operator:

- **Jacobi smoother**: `dinv = assemble_diagonal(A); dinv = reciprocal(dinv)` then `y = dinv ⊙ x` (`palace/linalg/jacobi.cpp:79-80`). The diagonal-preconditioner-apply intermediate is `assemble_diagonal` + element-wise `reciprocal` + element-wise product.
- **Chebyshev smoother** (both 4th-kind and 1st-kind): identical `op.AssembleDiagonal(dinv); dinv.Reciprocal();` setup (`palace/linalg/chebyshev.cpp:177-178` and `chebyshev.cpp:240-241`), feeding the diagonally-scaled polynomial smoother.
- Block-Jacobi / polynomial preconditioners (roadmap §Intermediate "Diagonal-preconditioner apply") reuse the same `assemble_diagonal` → `reciprocal` → element-wise-product chain.

The `reciprocal` (`mfem::Vector::Reciprocal`) and element-wise product that complete the diagonal-preconditioner apply are themselves L1-primitive candidates (forthcoming `reciprocal` / `elementwise_product` entries — referenced here as plain text, not yet authored).

## Variant axes

`assemble_diagonal` has one orthogonal variant axis at L1; a second axis is collapsed and recorded as deliberate absorption.

- **element-type**: `real` | `complex`. The L0 source splits this into the two parallel hierarchies — real `Operator::AssembleDiagonal(Vector &diag)` (the MFEM `mfem::Operator::AssembleDiagonal` virtual, inherited via the `using Operator = mfem::Operator` alias at `palace/linalg/operator.hpp:21`) and complex `ComplexOperator::AssembleDiagonal(ComplexVector &diag)` (`palace/linalg/operator.hpp:51`). At L1 these collapse to one operator parameterised by element type. The complex case assembles the real and imaginary diagonals separately (law 6); the per-element diagonal-extraction relationship is otherwise identical.

Collapsed (absorbed) axis:

- **operator-representation**: `sparse-CSR` | `matrix-free` | `parallel-wrapped` | `complex-wrapped`. At L0 these are concrete overrides of the `AssembleDiagonal` virtual (`HypreCSRMatrix`, `fem::libceed::Operator`, `ParOperator` / `ComplexParOperator`, `ComplexWrapperOperator`). At L1 these **collapse to a single `LinearOperator` opaque type** — the L1 contract sees only "extract the diagonal of this square operator"; the internal representation is an L0 concern that surfaces only in the L1>L0 lowering (and in the load-bearing exact-vs-approximate caveat for the matrix-free high-order-Nedelec representation). This is the same *variant absorption* application (per [`concepts/variant-absorption`](../concepts/variant-absorption.md)) that `apply_linop` performs over its representation axis.

Non-axes (recorded for disambiguation):

- **abs-vs-signed diagonal**: there is **no** absolute-value-diagonal variant of `assemble_diagonal`. The absolute value appears only *inside* the `ParOperator` AMR assembly (`|P|ᵀ dₗ`, where `|P|` is the entry-wise-absolute prolongation, `palace/linalg/rap.cpp:163-176`) — it is the *prolongation* that is taken absolute (to keep the assembled diagonal convergent on a non-conforming mesh), not the diagonal entries. The output diagonal retains its sign. So abs-vs-signed is not a variant axis of the operator; the abs is an L0 assembly mechanic absorbed into the representation axis.
- **transpose-mode**: not an axis — the diagonal is transpose-invariant (see the non-law), so Palace exposes no `AssembleDiagonalTranspose`. Contrast `apply_linop`, which has a genuine three-valued transpose-mode axis.
- **partial-domain (abort)**: the base `ComplexOperator::AssembleDiagonal` aborts (`MFEM_ABORT("Base class ComplexOperator does not implement AssembleDiagonal!")`, `palace/linalg/operator.cpp:25-28`). This is not a variant — it marks that the operator's L1 domain is the diagonal-capable subclasses, not every `LinearOperator`. An operator that cannot expose a diagonal is outside `assemble_diagonal`'s domain (a precondition, not a variant).

## Status

`firm` — signature is canonical (matches the `AssembleDiagonal(diag)` virtual on both the real and complex operator hierarchies, parameterised by element type, with the square `N×N` precondition the source enforces), evidence is direct from the Palace source (abstract decls + concrete realisations across sparse/matrix-free/parallel/complex-wrapped representations + the consuming smoother call sites + the libCEED diagonal-assembly unit test), and the algebraic laws listed are standard properties of the matrix-diagonal map modulo the explicitly-recorded load-bearing exact-vs-approximate caveat. The one caveat (matrix-free high-order-Nedelec approximate diagonal) is recorded as a non-law, not a status reduction: the structure is exhaustively cited and the approximation is a documented, test-witnessed property of the matrix-free representation, not an unresolved gap.

## L1 vs L0 distinction

- **L0**: a family of virtual `AssembleDiagonal(diag) const` methods on the operator hierarchy. Writes through the output argument `diag`, sizing it (`diag.SetSize(height)`) and/or zero-initialising it (`diag = 0.0`) first. Sparse path reads the stored CSR diagonal (`hypre_CSRMatrixExtractDiagonal`); matrix-free path accumulates element-local diagonal contributions (`CeedOperatorLinearAssembleAddDiagonal`) under an OpenMP region; the `ParOperator` AMR path assembles via the absolute-value prolongation transpose `|P|ᵀ dₗ` then applies a Dirichlet `DiagonalPolicy` to BC true-dofs; the complex paths assemble real/imag parts separately. The base `ComplexOperator` method aborts.
- **L1**: pure functional extraction. `d = assemble_diagonal(A)`. No destination buffer in the signature, no sizing, no zero-init, no workspace, no Dirichlet policy parameter. One operator parameterised by element type; representation (sparse / matrix-free / parallel / complex-wrapped) collapsed to a single opaque `LinearOperator[N, N]`. Algebraic laws (operator-scaling/sum linearity, identity, diagonal round-trip) apply directly. The exact-vs-approximate distinction (sparse exact; matrix-free high-order-Nedelec approximate) is recorded as an explicit non-law, classified as load-bearing for the value (not merely the bit pattern). The absolute-value prolongation, the zero-init, the element accumulation, and the Dirichlet policy are all L1>L0 lowering concerns.

## Evidence

- `palace/linalg/operator.hpp:21` — `using Operator = mfem::Operator;` — the real-operator alias inheriting the abstract `mfem::Operator::AssembleDiagonal(Vector &diag) const` virtual (resolves into upstream MFEM; see Open questions).
- `palace/linalg/operator.hpp:50-51` — `// Diagonal assembly.` / `virtual void AssembleDiagonal(ComplexVector &diag) const;` — the abstract complex-operator diagonal-assembly declaration.
- `palace/linalg/operator.hpp:97` — `void AssembleDiagonal(ComplexVector &diag) const override;` — `ComplexWrapperOperator` override declaration.
- `palace/linalg/operator.cpp:25-28` — `ComplexOperator::AssembleDiagonal` base definition: `MFEM_ABORT("Base class ComplexOperator does not implement AssembleDiagonal!")` — the partial-domain non-axis (the operator's L1 domain is the diagonal-capable subclasses).
- `palace/linalg/operator.cpp:85-96` — `ComplexWrapperOperator::AssembleDiagonal`: `diag = 0.0; if (Ar) Ar->AssembleDiagonal(diag.Real()); if (Ai) Ai->AssembleDiagonal(diag.Imag());` — witnesses laws 2 and 6 (sum / complex real-imag-split linearity) and the `diag = 0.0` zero-init.
- `palace/linalg/hypre.cpp:85-89` — `HypreCSRMatrix::AssembleDiagonal`: `diag.SetSize(height); hypre_CSRMatrixExtractDiagonal(mat, diag.Write(), 0);` — the **exact** sparse-CSR diagonal read; witnesses the destination sizing and the representation axis.
- `palace/linalg/hypre.hpp:70` — `void AssembleDiagonal(Vector &diag) const override;` — `HypreCSRMatrix` override declaration.
- `palace/fem/libceed/operator.cpp:116-143` — `fem::libceed::Operator::AssembleDiagonal`: `MFEM_VERIFY(diag.Size() == height, ...)` (square precondition, line 120), `diag = 0.0` (line 121), and the OpenMP-parallel `CeedOperatorLinearAssembleAddDiagonal(op[id], v[id], ...)` (line 139) — the **matrix-free** element-local accumulating assembly (the source of the high-order-Nedelec approximation).
- `palace/fem/libceed/operator.hpp:56` — `void AssembleDiagonal(Vector &diag) const override;` — libCEED operator override declaration.
- `palace/linalg/rap.cpp:154-193` — `ParOperator::AssembleDiagonal`: square-only `MFEM_VERIFY(&trial_fespace == &test_fespace, ...)` (line 165), the AMR `|P|ᵀ dₗ` absolute-value-prolongation assembly with the convergent-diagonal comment (lines 163-176, `hP->AbsMultTranspose(1.0, lx, 0.0, diag)` at line 172), and the Dirichlet `DiagonalPolicy` BC post-step `DIAG_ONE` / `DIAG_ZERO` (lines 180-191). Witnesses the square precondition, the abs-prolongation non-axis, and the BC-policy L0-only step.
- `palace/linalg/rap.cpp:467-479` — `ComplexParOperator::AssembleDiagonal`: `diag = 0.0; if (RAPr) RAPr->AssembleDiagonal(diag.Real()); if (RAPi) RAPi->AssembleDiagonal(diag.Imag());` — complex parallel real-imag-split assembly (witnesses law 6).
- `palace/linalg/rap.hpp:112` / `palace/linalg/rap.hpp:206` — `ParOperator` / `ComplexParOperator` `AssembleDiagonal` override declarations.
- `palace/linalg/jacobi.cpp:75-82` — `JacobiSmoother::SetOperator`: `dinv.SetSize(op.Height()); op.AssembleDiagonal(dinv); dinv.Reciprocal();` — direct evidence of the **diagonal-preconditioner-apply** chain (`assemble_diagonal` → `reciprocal` → element-wise product in `Mult`).
- `palace/linalg/jacobi.hpp:15-16` — `// Simple Jacobi smoother using the diagonal vector from OperType::AssembleDiagonal(), which allows for (approximate) diagonal construction for matrix-free operators.` — the Palace comment naming the matrix-free **approximate** diagonal (load-bearing caveat).
- `palace/linalg/chebyshev.cpp:170-178` — `ChebyshevSmoother::SetOperator`: `op.AssembleDiagonal(dinv); dinv.Reciprocal();` feeding the diagonally-scaled Chebyshev smoother.
- `palace/linalg/chebyshev.cpp:233-241` — `ChebyshevSmoother1stKind::SetOperator`: the identical `op.AssembleDiagonal(dinv); dinv.Reciprocal();` setup (second consumer code path).
- `test/unit/test-libceed.cpp:343-376` — diagonal-assembly test: `mat_ref->GetDiag(d_ref); op_test->AssembleDiagonal(d_test); d_test *= scaling; d_test -= d_ref;` then `REQUIRE(d_test * d_test < rtol * std::max(d_ref * d_ref, 1.0))`. Confirms `AssembleDiagonal` reproduces the **assembled-matrix** diagonal (`mfem::SparseMatrix::GetDiag`) to `rtol = 1.0e-12` in general, but relaxes to `rtol = 1.0` exactly for **high-order 3D Nedelec non-tensor-basis** spaces (lines 367-374) — the test-witnessed load-bearing approximation. L0-equivalent semantic documentation per CLAUDE.md "Tests as semantic supplement".
- `book/src/L1/apply_linop.md` — the sibling firm L1 operator; the operator/data divide (`apply_linop` is operator-and-vector-to-vector; `assemble_diagonal` is operator-to-data) is stated against it.

---

## Wiring edits (book/src/L1/index.md)

1. **Cohort count** — change `**Firm (11)**` → `**Firm (12)**` (line 29).

2. **Cohort bullet** — append after the `divfree-projector` firm bullet (after line 41):

```
- [`assemble-diagonal`](./assemble-diagonal.md) — pure-functional operator-to-data diagonal extraction `d = assemble_diagonal(A)`; the diagonal-introspection primitive at L1, sibling to [`apply_linop`](./apply_linop.md) on the opaque-operator side (operator-to-data, where `apply_linop` is operator-and-vector-to-vector). Explicitly **not** an `apply_linop` variant (it consumes no vector; the result is a property of `A` alone — resolves OQ `assemblediagonal-is-not-apply-linop-variant`). The gate to diagonally-scaled preconditioners: Jacobi / Chebyshev / block-Jacobi / polynomial smoothers all reuse the `assemble_diagonal` → `reciprocal` → element-wise-product chain. Firm despite a single (libCEED diagonal-assembly) test, on the strength of exhaustive structural citation across all five concrete representations; carries one load-bearing non-law (matrix-free high-order-Nedelec diagonals are *approximate*, test-witnessed at the relaxed `rtol = 1.0`).
```

3. **Dep-map row** — append a row to the operator dep-map table (after the `divfree-projector` row, line 75):

```
| [`assemble-diagonal`](./assemble-diagonal.md) | `(A: LinearOperator[N, N]) → Tensor[N]` (i.e. `diag(A)`) | (leaf; opaque square operator; sibling to `apply_linop`, NOT a dependency) | `firm` (operator-to-data gate; L0: `palace/linalg/{operator,rap,hypre}.cpp` + `palace/fem/libceed/operator.cpp`; harvested cycle-019; matrix-free high-order-Nedelec approximate-diagonal load-bearing non-law) |
```

## Supporting evidence

- All citations self-verified against source via `palace-codemap` `read_range` at emit time (cycle-015 producer self-verification; `verify-citation-range` skill). Verified line-exact: `operator.hpp:21,50-51,97`; `operator.cpp:25-28,85-96`; `hypre.cpp:85-89`; `hypre.hpp:70`; `libceed/operator.cpp:116-143` (square check line 120, zero-init 121, AddDiagonal 139); `libceed/operator.hpp:56`; `rap.cpp:154-193` (square check 165, abs-prolongation comment 163-164, `AbsMultTranspose` 172, DiagonalPolicy 180-191), `rap.cpp:467-479`; `rap.hpp:112,206`; `jacobi.cpp:75-82`; `jacobi.hpp:15-16`; `chebyshev.cpp:170-178,233-241`; `test-libceed.cpp:343-376`.
- The "NOT an apply_linop variant" framing is anchored against the firm `apply_linop` entry's signature `(A: LinearOperator[M, N], x: Tensor[N]) → Tensor[M]` (`book/src/L1/apply_linop.md:16`).
- Fan-out (Jacobi / Chebyshev consumers) witnessed directly at the three smoother call sites — this is the `diagonal-extraction-l1` Backlog item's reuse claim, confirmed in source.

## Open questions

- **`assemble-diagonal-mutation-rotation` L1>L0 lowering theme (NEW, abstractor)** — the L1>L0 lowering for `assemble_diagonal` is not yet authored. It must narrate forward from L1 `d = assemble_diagonal(A)` to the L0 `A.AssembleDiagonal(diag)` output-arg mutation, and absorb: (i) the destination sizing / `diag = 0.0` zero-init; (ii) the representation split (Hypre CSR exact read vs libCEED element-local accumulation vs `ParOperator` abs-prolongation-transpose); (iii) the Dirichlet `DiagonalPolicy` BC post-step; (iv) the matrix-free high-order-Nedelec approximation as a load-bearing assembly-order property. Recommend filing as a Backlog item paired with the existing `diagonal-extraction-l1`.
- **Upstream MFEM `mfem::Operator::AssembleDiagonal` (real path)** — the real-operator `AssembleDiagonal` resolves into vendored MFEM via `using Operator = mfem::Operator` (`palace/linalg/operator.hpp:21`); Palace overrides it only on its own subclasses (`HypreCSRMatrix`, `ParOperator`, libCEED `Operator`). Per CLAUDE.md "Many symbols resolve into upstream libraries", the L1 entry cites the Palace *call sites* and overrides, not the MFEM base virtual. Log as an upstream-behavior dependency: the exact semantics of `mfem::Operator::AssembleDiagonal` for any Palace operator that does *not* override it (and inherits the MFEM default) is out-of-scope evidence. No such un-overridden real-operator path is surfaced in the consuming smoothers (they all call into overriding subclasses), so this does not block the firm status — but a future cross-layer pass should confirm no real-operator consumer relies on the MFEM default behaviour.
- **`reciprocal` / `elementwise_product` L1 primitives (forthcoming)** — the diagonal-preconditioner apply completes via `mfem::Vector::Reciprocal` (`dinv.Reciprocal()`) and an element-wise product (`Apply(dinv, x, y)` in `jacobi.cpp:104`). These are referenced as plain text in the entry (not yet authored). Harvesting them would let the Jacobi/Chebyshev preconditioner-apply be expressed as a clean L1 composition `y = elementwise_product(reciprocal(assemble_diagonal(A)), x)`. Candidate Backlog items.
- **OQ `assemblediagonal-is-not-apply-linop-variant` — resolve / close** — this harvest is the deliberate resolution: `assemble_diagonal` lands as its own firm L1 entry with the operator/data divide stated explicitly. The OQ should be closed (migrated out of the open-questions ledger) by the integrator / meta-phase, with this entry as the resolution anchor.
- **Layer-intro refresh (layer-intro-author)** — the L1 `index.md` "Semantics (overlay)" section enumerates four recurring semantic motifs; `assemble_diagonal` introduces a fifth — **operator-to-data introspection** (an operator-argument primitive that returns operator-intrinsic data rather than the operator's action). The intro's motif list could note this fifth motif. Flagged here per harvester scope (intro edits are layer-intro-author's job).
