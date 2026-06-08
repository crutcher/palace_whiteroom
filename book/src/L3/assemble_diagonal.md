---
layer: L3
operator: assemble_diagonal
firmness: firm
edges:
  depends-on:
    - target: L2/assemble_diagonal
      kind: lowers-to
variant_axes:
  - element-type (real | complex; collapsed to a single parameterised operator)
  - operator-representation (sparse-CSR | matrix-free | parallel-wrapped | complex-wrapped; absorbed into the opaque LinearOperator type)
---

# assemble_diagonal

Whole-operator **operator-to-data** extraction at L3: `d = diag(A)`, the main diagonal of a square linear operator materialised as a vector. The diagonal-introspection primitive at L3 — the operator-to-data sibling of [`apply_linop`](./apply_linop.md) on the opaque-`LinearOperator` side of the L3 vocabulary, and the iteration-rotation rendering of the same diagonal-extraction map that L1 [`assemble_diagonal`](../L1/assemble_diagonal.md) provides. The gate to diagonally-scaled preconditioners (Jacobi, Chebyshev, block-Jacobi, polynomial) at the iteration-rotation layer.

## Context

L3 is the iteration-rotation layer: global tensor-field operations expressed as whole-tensor primitives with no element loop exposed at the layer's vocabulary, with sequential obstructions named explicitly per [`sequential-obstruction`](../concepts/sequential-obstruction.md). `assemble_diagonal` at L3 is the value-threaded form of the diagonal-extraction primitive — the same operator that L1 names as the "pure-functional operator-to-data extraction" (replacing the L0 `A.AssembleDiagonal(diag)` output-arg mutation idiom), read at L3 as one of the whole-operator field operations the layer composes. Its signature `(A: LinOp[(S: ...), $S]) -> Tensor[$S]` exposes no element loop — the per-row read of the operator's `(i, i)` entries is a single semantic step at L3 just as it is at L1.

Unlike the BLAS-1 cohort (`axpy`, `dot`, `nrm2`, `scal`), `assemble_diagonal` is **not** a vector-in / vector-out field operation: it consumes an opaque operator and produces operator-intrinsic data. It is the operator-to-data sibling of [`apply_linop`](./apply_linop.md) — the two share the opaque `LinearOperator` argument type and the L0 output-arg mutation idiom (`A.AssembleDiagonal(diag)` writes through `diag`, the same destination-buffer pattern as `apply_linop`'s `A.Mult(x, y)`), but they live on opposite sides of the operator/data divide. `assemble_diagonal` takes **no vector** and returns a property of `A` alone (per OQ `assemblediagonal-is-not-apply-linop-variant`, recorded at the L1 home).

The relationship to the adjacent layers:

- **Upward** to L4: there is **no standalone L4 entry** for `assemble_diagonal`. It is a leaf operator-introspection primitive carrying no monadic effect, no state-stratification typing, no novel calculus content at L4 — the same `CONFIRMED-NOT-NEEDED` disposition as `apply_linop` and the BLAS-1 cohort. At L4 it appears (where consumed) inside operator bodies as a let-binding feeding the diagonal-preconditioner-apply chain, not as first-class L4 vocabulary. Per CLAUDE.md §Methodology invariants "Layers are defined high→low", the absence of an L4 entry is a deliberate scoping verdict, not a gap.

- **Downward** to L2/L1: `assemble_diagonal` lowers to the **present adjacent L2 floor** [`assemble_diagonal`](../L2/assemble_diagonal.md) as **identity-in-form on the primitive's signature**, recorded as the in-line §"Downward to L2" note below (NOT a dedicated L3>L2 theme — the edge is a degenerate identity-in-named-terms lowering demoted to an in-line note per the 2026-06-01 vocabulary-shift redirect), and onward to L1 [`assemble_diagonal`](../L1/assemble_diagonal.md). The rotation is **identity-in-form on the primitive's signature** — L3 and L2 see `assemble_diagonal :: LinOp[(S: ...), $S] -> Tensor[$S]` and L1 sees its rank-1 realization `LinearOperator[N, N] -> Tensor[N]` (the concrete flat dof-vector length), with the same shape contract, the same six algebraic laws, the same non-law set (including the load-bearing exact-vs-approximate caveat), and the same variant-axis profile (one orthogonal element-type axis + one absorbed operator-representation axis). The L2 floor is the standalone (fork-independent) operator-to-data sibling of `apply_linop`. The transitive L3>L1 identity remains in-line, with no non-adjacent `L3-L1/` lowering directory created.

This L3 entry is the **layer-coherence anchor**: a reader navigating L3 (the iteration-rotation layer that composes whole-operator and whole-tensor primitives into smoother / solver bodies) can find `assemble_diagonal` here, in L3 vocabulary, without having to reach down to L1 to recover the signature. It enacts the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants): an **(A) identity-in-form** L3 backfill, structurally identical to the firm `apply_linop` opaque-operator-gate precedent, with the exact-vs-approximate caveat absorbed as a representation-aware L1>L0 non-law (`book/src/L3/index.md:46`).

## Signature

```text
assemble_diagonal :: LinOp[(S: ...), $S] -> Tensor[$S]
assemble_diagonal A = diag(A)
```

Shape contract (named shape groups / operator shapes per [`l4_calculus`](../semantics/index.md) §1.2.1–§1.2.2; the diagonal is intrinsic to a square operator, so domain and range are one shape group `S`; positional values; L3 has no `readonly` annotation and no monadic effect — the typing distinctions are deferred to the wrapper layers above):

- **`A`** — `LinOp[(S: ...), $S]`, an opaque **square** linear-operator type (domain group `S` equals range group `S`). Read-only at L3 (the L0 method is `const`; the L3 form never writes through `A`). The operator-representation axis (sparse-CSR, matrix-free, parallel-wrapped, complex-wrapped) is **absorbed at L3** into this opaque type; the L3 kernel does not branch on representation. The element type (real or complex) is parameterised; the L3 signature is uniform across the element-type axis.
- **result** — `Tensor[$S]`, the diagonal vector, congruent to the operator's (shared) square shape group `S`; `result[i]` is the `(i, i)` entry of `A`. A fresh value. No L0 destination buffer is mentioned at L3 (the destination-binding rotation is an L1>L0 concern, per the [`assemble-diagonal-mutation-rotation`](../L1-L0/assemble-diagonal-mutation-rotation.md) theme).

The **square requirement** (range group ≡ domain group) is intrinsic: a diagonal is only defined where the domain and range index sets coincide. This is the chief signature difference from the sibling `apply_linop`, which admits rectangular `R ≠ D`. Palace enforces the square precondition at the L0 source for the AMR path (`MFEM_VERIFY(&trial_fespace == &test_fespace, "Diagonal assembly is only available for square ParOperator!")`, `palace/linalg/rap.cpp:165-166` — predicate at :165, message string at :166) and the matrix-free path (`MFEM_VERIFY(diag.Size() == height, ...)`, `palace/fem/libceed/operator.cpp:120`) — both transitive through the L1 home.

`LinOp[(S: ...), $S]` is an **opaque type** at L3: its internal representation (sparse CSR / matrix-free / parallel-wrapped / complex-wrapped) is not part of the L3 signature; the L3 contract sees only "extract the diagonal of this square operator". The operator is guaranteed to expose a diagonal — the base `ComplexOperator::AssembleDiagonal` aborts (`palace/linalg/operator.cpp:25-28`), so the operator's L3 domain is the diagonal-capable subclasses (a precondition, not a variant — see Variant axes).

No L4 wrapper machinery is needed at L3: `assemble_diagonal` is a leaf operator-introspection field operation, not a step body, and the L4 monadic / typed-record / `readonly`-typing apparatus (which serves wrapper-bearing operators like `krylov_step`) does not apply to leaf primitives — the same discipline the L3 `apply_linop` and `scal` entries record.

## Semantics

`assemble_diagonal A` returns the vector of main-diagonal entries of `A`: `result[i] = Aᵢᵢ = eᵢᵀ A eᵢ` for `i ∈ [0, N)`, where `eᵢ` is the `i`-th standard basis vector. The result is determined entirely by `A` — the L3 form is pure functional (extracting the diagonal of the same `A` twice returns the same value), with no hidden state, no per-call side effects, no in-place mutation at the L3 surface. The L0 source sizes and overwrites the in-place destination buffer `diag`; that overwrite, the sizing, and the workspace are reintroduced only at the L1>L0 lowering.

The relationship `result[i] = eᵢᵀ A eᵢ` is the **mathematical** definition of the diagonal, **not** the implementation: Palace never forms `N` matrix-vector products. For a sparse representation it reads the stored diagonal directly (`HypreCSRMatrix::AssembleDiagonal` calls `hypre_CSRMatrixExtractDiagonal`, `palace/linalg/hypre.cpp:88`); for a matrix-free representation it accumulates element-local diagonal contributions via libCEED (`CeedOperatorLinearAssembleAddDiagonal`, `palace/fem/libceed/operator.cpp:139`). The `eᵢᵀ A eᵢ` form is the algebraic specification the implementations realise — it is what relates `assemble_diagonal` to the sibling `apply_linop` (the diagonal entries are the would-be results of probing `A` with basis vectors) **without** making `assemble_diagonal` a *use* of `apply_linop`. The two are L3 siblings on the opaque-operator side, not a dependency chain.

### Iteration-rotation marker

L3 is the iteration-rotation layer. **`assemble_diagonal` lifts as a whole-operator field operation at L3** — the primitive's signature has no element loop exposed at the layer, and the L1 form's `LinearOperator[N, N] -> Tensor[N]` signature is identity-in-form to the L3 form. The per-row read of the `(i, i)` entries is a single semantic step in the L3 calculus, not a loop.

There is **no sequential obstruction** for `assemble_diagonal`. Diagonal extraction is a per-row read of operator-intrinsic data: each `result[i]` depends on `A`'s `(i, i)` entry alone, with no cross-row recurrence and no carry threaded between rows. This is the structural distinction from the `partial-obstruction` L3 operators (`chebyshev`, `eigsolve`), whose bodies lift but whose loops do not: `assemble_diagonal` has no loop to obstruct — it is one of the layer's clean whole-operator field operations, embarrassingly parallel and GPU-friendly (a sparse-CSR realisation reads `N` stored diagonal entries independently; a matrix-free realisation accumulates element-local contributions, a reduction with no inter-row sequencing).

A subtle below-the-surface caveat: for **matrix-free high-order Nedelec (H(curl)) representations in 3D**, the element-local diagonal accumulation differs from the true assembled diagonal (face dofs shared across elements). This is a **load-bearing** numerical property (per the CLAUDE.md taxonomy) inherited unchanged from L1 — the approximate diagonal is what the consuming smoothers actually use, and the approximation is acceptable *because* the diagonal feeds an inexact preconditioner (a Jacobi/Chebyshev smoother tolerates an approximate diagonal scaling). The L3 form names this as a non-law (see Algebraic laws), not as an obstruction — the algebraic correctness of `assemble_diagonal` is unaffected; only the diagonal *value* changes across representations (not merely the bit pattern). Sourced from the Palace AMR convergent-diagonal note (`palace/linalg/rap.cpp:163-164`) and test-witnessed (`test/unit/test-libceed.cpp:367-376`, relaxing `rtol` to `1.0` for the high-order non-tensor-basis Nedelec case), both transitive through the L1 home.

## Algebraic laws

The six laws that hold at L1 (per `book/src/L1/assemble_diagonal.md` §"Algebraic laws") transport **unchanged** to L3, because the L3 form is value-thread-isomorphic to the L1 form. These are operator-introspection laws — they relate the diagonal of a *constructed* operator to the diagonals/entries of its parts, not laws of a vector update. The laws are reproduced here so the L3 reader does not have to reach to L1 for the listing.

1. **Linearity over operator scaling**: `assemble_diagonal (α·A) = α · assemble_diagonal A` for any scalar `α`. The diagonal of a scaled operator is the scaled diagonal (`(α·A)ᵢᵢ = α·Aᵢᵢ`).
2. **Linearity over operator sum**: `assemble_diagonal (A + B) = assemble_diagonal A + assemble_diagonal B` for square `A`, `B` sharing shape group `S` (`(A + B)ᵢᵢ = Aᵢᵢ + Bᵢᵢ`). Witnessed structurally by `ComplexWrapperOperator::AssembleDiagonal` (`palace/linalg/operator.cpp:85-96`), which assembles real and imaginary parts independently after `diag = 0.0`.
3. **Zero operator**: `assemble_diagonal 0_op = 0_$S` (the zero vector of shape group `S`). Special case of law 1 with `α = 0`.
4. **Identity operator**: `assemble_diagonal I = 𝟙_$S` (the all-ones vector of shape group `S`), since `Iᵢᵢ = 1` for all `i`.
5. **Diagonal-operator round-trip**: `assemble_diagonal (Diag(d)) = d` for the operator `Diag(d)` whose action is element-wise multiplication by `d`. Extracting the diagonal of a diagonal operator recovers its defining vector — the law that makes `assemble_diagonal` the left-inverse of diagonal-operator construction, and the round-trip the diagonal-preconditioner apply relies on (`Jacobi(A)·x = (1/diag(A)) ⊙ x`).
6. **Complex linearity (real/imag split)**: for a complex operator `A = Ar + i·Ai`, `assemble_diagonal A = assemble_diagonal Ar + i · assemble_diagonal Ai`. Witnessed by `ComplexWrapperOperator::AssembleDiagonal` (`palace/linalg/operator.cpp:85-96`) and `ComplexParOperator::AssembleDiagonal` (`palace/linalg/rap.cpp:467-479`). A specialisation of law 2 to the equivalent-real decomposition.

Laws that explicitly **do not** hold (inherited unchanged from L1):

- **Diagonal of a product**: `assemble_diagonal (A · B) ≠ assemble_diagonal A ⊙ assemble_diagonal B` in general — `(A·B)ᵢᵢ = Σ_k Aᵢₖ Bₖᵢ` is a full row·column contraction, not the product of the two `(i,i)` entries. Equality holds only when *both* operators are diagonal. Recorded as an absence because diagonal-of-product is a frequent false intuition; no Palace path assembles a product's diagonal this way.
- **Transpose invariance is non-distinguishing**: `assemble_diagonal Aᵀ = assemble_diagonal A` *does* hold (`(Aᵀ)ᵢᵢ = Aᵢᵢ`), but it is recorded as a non-distinguishing identity rather than a useful law — Palace exposes no transpose-mode axis on `AssembleDiagonal` (unlike `apply_linop`'s `Mult` / `MultTranspose`) precisely because the diagonal is transpose-invariant. For complex operators the Hermitian transpose conjugates the diagonal: `assemble_diagonal Aᴴ = conj(assemble_diagonal A)`. The **absence of a transpose-mode variant axis** is the chief variant-profile difference from the sibling `apply_linop` (three orthogonal axes), which carries a genuine three-valued transpose mode.
- **Exactness across representations** (load-bearing): a sparse-matrix realisation of `A` reads the **exact** stored diagonal, while a matrix-free high-order-Nedelec realisation of the *same* mathematical operator produces an **approximate** diagonal (face-dof sharing in 3D). Load-bearing per the CLAUDE.md taxonomy: the representation can change the diagonal *value* (not just its bit pattern). The six laws above hold for the exact diagonal; their matrix-free realisation may be approximate. This is the one case where the difference is semantic (a different value), not floating-point reduction-order noise. This is the "exact-vs-approximate caveat absorbed as a representation-aware L1>L0 non-law" (`book/src/L3/index.md:46`) — at L3 it is recorded against the absorbed operator-representation axis, surfaced concretely in the L1>L0 lowering.
- **Linearity strictness in floating point**: laws 1, 2, 6 are exact in ℝ / ℂ; in IEEE-754 the assembled diagonal sums round, so equality is approximate (and, for the matrix-free high-order case, *not even* approximate to round-off — the approximation is structural, per the previous non-law).

The law set and non-law set are **inherited unchanged** from L1; the L3 rendering introduces no new laws or non-laws. This is what makes the L3>L1 hop identity-in-form on the primitive's signature: not only does the signature transport unchanged, the entire algebraic profile transports unchanged.

## Dependencies

**Same-layer (L3)**: none. `assemble_diagonal` is a **leaf operator-introspection primitive** at L3 — a sibling of [`apply_linop`](./apply_linop.md) on the opaque-`LinearOperator` side of the L3 vocabulary (operator-to-data, where `apply_linop` is operator-and-vector-to-vector). Its sub-operations are the operator's internal diagonal extraction (Hypre CSR diagonal read, libCEED element-local diagonal accumulation, prolongation-transpose assembly) — all below the L3 layer's resolution and visible only in the L1>L0 lowering.

It is **not** factored through `apply_linop` despite the algebraic specification `result[i] = eᵢᵀ A eᵢ`: that specification is the mathematical definition, not the implementation (Palace forms no basis-vector probes), and treating it as a dependency would falsely imply `N` operator applies. The two are L3 siblings, not a chain.

**Consumers (L3)** (cross-reference, not reverse-dependencies) — the diagonal-preconditioner-apply fan-out that motivated the L1 harvest, transported to L3:

- **Jacobi smoother**: `dinv = assemble_diagonal A; dinv = reciprocal(dinv)` then `y = dinv ⊙ x`. The L0 chain `dinv.SetSize(op.Height()); op.AssembleDiagonal(dinv); dinv.Reciprocal();` is at `palace/linalg/jacobi.cpp:75-82`.
- **Chebyshev smoother** (both 4th-kind and 1st-kind): identical `op.AssembleDiagonal(dinv); dinv.Reciprocal();` setup (`palace/linalg/chebyshev.cpp:170-178`), feeding the diagonally-scaled polynomial smoother.
- Block-Jacobi / polynomial preconditioners reuse the same `assemble_diagonal` → `reciprocal` → element-wise-product chain.

The `reciprocal` and `elementwise_product` that complete the diagonal-preconditioner apply are themselves firm L3 entries.

**L1 anchor**: [`L1/assemble_diagonal`](../L1/assemble_diagonal.md) (firm) — authoritative on the Palace surface details (the abstract decls + concrete realisations across sparse/matrix-free/parallel/complex-wrapped representations, the consuming smoother call sites, the libCEED diagonal-assembly unit test), the square-precondition enforcement sites, the Dirichlet `DiagonalPolicy` BC post-step, and the complete L0 evidence list. This L3 entry does not duplicate those details; the L3>L1 rotation is identity-in-form on the primitive itself.

**Strawman reference**: `book/src/semantics/index.md` is the L4/L3 conventions source; this L3 entry follows the strawman's Haskell `::` signature notation. `assemble_diagonal` does not get its own L4 entry.

## Variant axes

`assemble_diagonal` has **one orthogonal variant axis at L3, plus one collapsed-and-absorbed axis** — the same framing as L1 (`book/src/L1/assemble_diagonal.md` §"Variant axes"), transported unchanged.

One orthogonal axis:

- **element-type** (`real` | `complex`) — collapsed to a single parameterised operator at L3. The L0 source splits this into two parallel hierarchies (real `Operator::AssembleDiagonal(Vector &diag)`, complex `ComplexOperator::AssembleDiagonal(ComplexVector &diag)`); at L3 these collapse to one operator parameterised by element type. The complex case assembles the real and imaginary diagonals separately (law 6); the per-element diagonal-extraction relationship is otherwise identical.

Collapsed (absorbed) axis:

- **operator-representation** (`sparse-CSR` | `matrix-free` | `parallel-wrapped` | `complex-wrapped`) — **absorbed** into the opaque `LinOp[(S: ...), $S]` type. The L0 concrete overrides (`HypreCSRMatrix`, `fem::libceed::Operator`, `ParOperator` / `ComplexParOperator`, `ComplexWrapperOperator`) collapse to a single L3 type; the L3 contract sees only "extract the diagonal of this square operator". This is the canonical application of [`variant-absorption`](../concepts/variant-absorption.md) — the same absorption the sibling `apply_linop` performs over its representation axis. The **load-bearing exact-vs-approximate caveat** (sparse exact; matrix-free high-order-Nedelec approximate) is the one place the absorbed axis surfaces semantically; it is recorded as a non-law and concretised in the L1>L0 lowering.

Non-axes (recorded for disambiguation, inherited from L1):

- **transpose-mode**: **not** an axis — the diagonal is transpose-invariant (see the non-law), so Palace exposes no `AssembleDiagonalTranspose`. This is the chief variant-profile contrast with the sibling `apply_linop`, which has a genuine three-valued transpose-mode axis. The operator-to-data primitive needs no transpose mode; the operator-and-vector-to-vector primitive does.
- **abs-vs-signed diagonal**: there is **no** absolute-value-diagonal variant. The absolute value appears only *inside* the `ParOperator` AMR assembly (`|P|ᵀ dₗ`, the entry-wise-absolute prolongation kept absolute to keep the assembled diagonal convergent on a non-conforming mesh) — it is the *prolongation* that is taken absolute, not the diagonal entries; the output diagonal retains its sign. The abs is an L0 assembly mechanic absorbed into the representation axis.
- **partial-domain (abort)**: the base `ComplexOperator::AssembleDiagonal` aborts (`palace/linalg/operator.cpp:25-28`). This is not a variant — it marks that the operator's L3 domain is the diagonal-capable subclasses (a precondition, not a variant). An operator that cannot expose a diagonal is outside `assemble_diagonal`'s domain.

The variant-axis profile (one orthogonal + one absorbed) matches the L1 entry exactly. **No new axes introduced by the L3 rendering; no axes merged or split; the orthogonal-vs-absorbed framing is preserved.**

## Lowers to

L3 `assemble_diagonal` lowers to the **present adjacent L2 floor** [`assemble_diagonal`](../L2/assemble_diagonal.md) as **identity-in-form on the primitive's signature**, recorded by the in-line §"Downward to L2 (in-line note)" below, and onward to L1 [`assemble_diagonal`](../L1/assemble_diagonal.md). L3 and L2 see `assemble_diagonal :: LinOp[(S: ...), $S] -> Tensor[$S]` and L1 its rank-1 realization `LinearOperator[N, N] -> Tensor[N]` (the concrete flat dof-vector length), with the same shape contract, the same six algebraic laws, the same non-law set (including the load-bearing exact-vs-approximate caveat), and the same variant-axis profile (one orthogonal + one absorbed). The L2 floor is the standalone (fork-independent) operator-to-data sibling of `apply_linop`, so the L3>L2 hop passes through the adjacent floor rather than skipping a layer to L1, per **Identity-lowerings still require both L levels**.

### Downward to L2 (in-line note)

The L3>L2 edge is a **degenerate identity-in-named-terms lowering** — the L3 whole-operator field
operation `assemble_diagonal :: LinOp[(S: ...), $S] -> Tensor[$S]` and the L2 floor are
value-thread-isomorphic on the body: same signature, same `assemble_diagonal A = diag(A)`
extraction (`result[i] = Aᵢᵢ`), same intrinsic-square (range group ≡ domain group) precondition, same opaque-`LinearOperator`
representation-axis absorption, same six laws + four non-laws. The vocabulary does not shift across
the edge, so per the 2026-06-01 vocabulary-shift redirect this is recorded **as this in-line note,
NOT as a dedicated L3>L2 theme**. There is **no wrapper** (it is a leaf field operation, not a kernel body inside an
`IterState`/outer-driver wrapper) and **no fold-parent** (it is the operator-to-data sibling of
`apply_linop`, belonging to no fold cohort), so there is no surface adjustment and no fold-level
rotation to carry — the edge is the pure identity. `assemble_diagonal` is **L3-native by signature
shape** (the per-row read of the `(i, i)` entries is a single semantic step at both layers; no
element loop is visible, no sequential obstruction — the iteration rotation is already complete at
the signature level), the same property `apply_linop` and the BLAS-1 cohort satisfy.

**Load-bearing non-law preserved through the edge (NOT erased).** The matrix-free
high-order-Nedelec (H(curl)) **approximate-diagonal** non-law carries across this edge unchanged: a
sparse-matrix realization of `A` reads the **exact** stored diagonal, while a matrix-free
high-order-Nedelec realization of the *same* mathematical operator produces an **approximate**
diagonal (face dofs shared across elements in 3D make the element-local summation differ from the
true assembled diagonal). Load-bearing per the CLAUDE.md taxonomy — the representation can change the
diagonal *value*, not merely its bit pattern. Because the L2 fusion content is degenerate there is no
de-fusion step in which the approximation could be lost; the non-law is preserved by reference, NOT
erased. Sourced from the Palace AMR convergent-diagonal note (`palace/linalg/rap.cpp:163-164`),
the matrix-free element-accumulation site (`palace/fem/libceed/operator.cpp:139`), and test-witnessed
(`test/unit/test-libceed.cpp:367-376`, relaxing `rtol` to `1.0` for the high-order 3D Nedelec
non-tensor-basis case) — all transitive through the L1 home. Concretized at the L1>L0
[`assemble-diagonal-mutation-rotation`](../L1-L0/assemble-diagonal-mutation-rotation.md) lowering.

The L3>L2 identity rotation is recorded by the §"Downward to L2 (in-line note)" above (a degenerate identity-in-named-terms edge recorded as an in-line note per the 2026-06-01 vocabulary-shift redirect); the transitive L3>L1 identity (L3>L2 ∘ L2>L1) is likewise annotated in-line, with no `book/src/L3-L1/` directory created. The substantive rotation in the chain is the L1>L0 [`assemble-diagonal-mutation-rotation`](../L1-L0/assemble-diagonal-mutation-rotation.md) theme — it lowers the L1 pure-functional form into Palace's output-arg-mutating L0 virtual `AssembleDiagonal(diag)` family (the destination sizing `diag.SetSize(height)`, the `diag = 0.0` zero-init, the sparse-CSR `hypre_CSRMatrixExtractDiagonal` read, the matrix-free `CeedOperatorLinearAssembleAddDiagonal` accumulation, the AMR `|P|ᵀ dₗ` absolute-value-prolongation assembly, and the Dirichlet `DiagonalPolicy` BC post-step). The L3>L1 hop is by contrast a layer-coherence rotation (each layer is coherent within itself), not an algebraic one.

**Practical reading**: an algorithm written at L3 that calls `assemble_diagonal` (e.g. the diagonal-preconditioner-apply setup of a Jacobi or Chebyshev smoother body) is reading the L1 entry's algebraic content (laws, non-laws, signature) one layer down; the L3 entry's role is to anchor the primitive in the L3 vocabulary inventory of whole-operator / whole-tensor field operations.

## Lifts from

`assemble_diagonal` has **no L4 entry** — leaf operator-introspection primitives are not first-class L4 vocabulary (leaf primitives carry no monadic effect, no state-stratification typing, no novel calculus content at L4). At L4 it appears (where consumed) inside larger composed entries as a let-binding feeding the diagonal-preconditioner-apply chain; the rotation from any such L4 mention to this L3 entry is the identity (the primitive's signature does not change between layers — only the surrounding wrapper does, and `assemble_diagonal` carries no wrapper at L4 or L3).

**This L3 entry exists for layer-coherence reasons** — a reader navigating L3 must find `assemble_diagonal` defined in L3 vocabulary, not have to reach down to L1 to recover the operator-to-data field-operation shape. The `apply_linop` L3 backfill (`book/src/L3/apply_linop.md`) is the structural precedent: identity-in-form rotation on the primitive's signature, opaque-operator-gate layer-coherence backfill, methodology invariant enacted. `assemble_diagonal` is the operator-to-data sibling of that precedent.

## Evidence

The L3 form is value-thread-isomorphic to the L1 form (identity-in-form on the primitive's signature); all L0 evidence is transitive through L1. Direct citations relevant to this L3 entry:

- `book/src/L1/assemble_diagonal.md` (firm) — the L1 entry whose signature, semantics, six algebraic laws, variant axes (one orthogonal + one absorbed), and complete L0 evidence chain are transported unchanged to L3. The laws and non-laws cited above are reproduced from the L1 entry's §"Algebraic laws".
- `book/src/L3/apply_linop.md` (firm) — the opaque-operator-gate L3 backfill precedent; `assemble_diagonal` is the operator-to-data sibling on the same opaque-`LinearOperator` side of the L3 vocabulary. The L3>L1 identity-in-form discipline, the no-L2-entry / no-theme-file rotation shape, and the variant-absorption framing are inherited from this sibling.
- `book/src/L3/index.md:12` — the L3 vocabulary inventory ("Whole-tensor field operations — primitives that act on whole tensors with no element loop exposed at the layer's vocabulary, L3-native by signature shape"); `assemble_diagonal` is the operator-to-data field operation this entry adds to the inventory.
- `book/src/L3/index.md:45-50` — line 46 classifies `assemble_diagonal` as **(A) identity-in-form L3 backfill** ("structurally identical to the firm `apply_linop` opaque-operator-gate precedent, with the exact-vs-approximate caveat absorbed as a representation-aware L1>L0 non-law").

**Transitive L0 evidence (via the L1 entry; not duplicated in detail)**:

- `palace/linalg/operator.cpp:25-28` — `ComplexOperator::AssembleDiagonal` base `MFEM_ABORT` (the partial-domain non-axis; the operator's L3 domain is the diagonal-capable subclasses).
- `palace/linalg/operator.cpp:85-96` — `ComplexWrapperOperator::AssembleDiagonal` (`diag = 0.0; Ar->AssembleDiagonal(diag.Real()); Ai->AssembleDiagonal(diag.Imag());`) — witnesses laws 2 and 6 (sum / complex real-imag-split linearity).
- `palace/linalg/hypre.cpp:85-89` — `HypreCSRMatrix::AssembleDiagonal` (`hypre_CSRMatrixExtractDiagonal` at :88) — the **exact** sparse-CSR diagonal read.
- `palace/fem/libceed/operator.cpp:120` — `MFEM_VERIFY(diag.Size() == height, ...)` (the square precondition, matrix-free path); `:139` — `CeedOperatorLinearAssembleAddDiagonal` (the matrix-free element-local accumulating assembly; the source of the high-order-Nedelec approximation).
- `palace/linalg/rap.cpp:165-166` — `MFEM_VERIFY(&trial_fespace == &test_fespace, "Diagonal assembly is only available for square ParOperator!")` (the square precondition, AMR path; predicate `&trial_fespace == &test_fespace` at :165, message string at :166); `:163-164` — the AMR `|P|ᵀ dₗ` convergent-diagonal note (the documented source of the approximate-diagonal caveat); `:467-479` — `ComplexParOperator::AssembleDiagonal` (complex parallel real-imag-split assembly; witnesses law 6).
- `palace/linalg/jacobi.cpp:75-82` — `JacobiSmoother::SetOperator`'s `op.AssembleDiagonal(dinv); dinv.Reciprocal();` (the diagonal-preconditioner-apply consumer chain).
- `palace/linalg/chebyshev.cpp:170-178` — `ChebyshevSmoother::SetOperator`'s identical `op.AssembleDiagonal(dinv); dinv.Reciprocal();` setup (second consumer code path).
- `test/unit/test-libceed.cpp:367-376` — the diagonal-assembly test relaxing `rtol` to `1.0` for high-order 3D Nedelec non-tensor-basis spaces (the test-witnessed load-bearing approximation). L0-equivalent semantic documentation per CLAUDE.md §"Tests as semantic supplement".

## L3 vs L4 distinction

- **L4**: no standalone `assemble_diagonal` entry. The primitive appears (where consumed) inside L4 operator entries as a let-binding within a do-block, carrying no monadic effect of its own. The surrounding wrapper (the do-block, the typed records, the `readonly` typing) is what makes the consuming entry L4-distinct — not the `assemble_diagonal` call itself.
- **L3**: standalone entry (this file). Positional value-threading: `assemble_diagonal A = diag(A)`. No monadic effect, no typed records, no `readonly` typing, no do-block. The primitive's signature is the L4 let-binding's RHS type, lifted out of any monadic context.

## L3 vs L1 distinction

- **L1**: pure-functional operator-to-data extraction; the mutation rotation has happened (the L0 destination buffer `diag` has been dropped from the signature, along with the sizing, the zero-init, the workspace, and the Dirichlet policy); the operator-representation axis has been absorbed (the opaque `LinearOperator` type). The L1 vocabulary mirrors the source `AssembleDiagonal(diag)` virtual with pure-functional binding.
- **L3**: whole-operator field operation; one of the operator-to-data primitives the iteration-rotation layer composes into smoother / preconditioner bodies (the diagonal-preconditioner-apply gate). **The primitive's signature is identity-in-form to L1** — no change in shape, no change in algebraic laws, no change in variant axes. The L3 entry exists for layer-coherence: a reader at L3 finds the primitive defined in L3 vocabulary without having to drop down to L1.

The two layers' entries are **value-thread-isomorphic** on the primitive itself, sharing signature, algebraic laws (six), non-laws (four, including the load-bearing exact-vs-approximate caveat), variant-axis profile (one orthogonal + one absorbed), and the cited L0 evidence (transitive). They differ in **layer interpretation**: L1 frames the primitive as the mutation-rotated form of the L0 `AssembleDiagonal` virtual; L3 frames it as one of the operator-to-data field operations the iteration-rotation layer enumerates as canonical vocabulary. The two framings are complementary — they read the same primitive from different layer roles — and the layer-coherence invariant (CLAUDE.md §Methodology invariants "Identity-lowerings still require both L levels") requires both entries to exist.
