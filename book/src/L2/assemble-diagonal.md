# assemble-diagonal

The **operator-to-data** diagonal-extraction primitive at the fusion-rotation layer:
the mutation-free `d = diag(A)`, the main diagonal of a square linear operator
materialised as a vector. This is the **L2 floor** under the firm L3
[`assemble-diagonal`](../L3/assemble-diagonal.md) — present so the L3 field operation
rests on an adjacent same-named L2 parent per the **Identity-lowerings still require
both L levels** invariant, rather than skipping a layer down to L1. It is a
**standalone operator-to-data primitive with NO fold-parent** (fork-independent): unlike
the cycle-041 BLAS-1 floors `dot` / `nrm2` / `scal` — which are leaf-of / consumer-of /
member-of the `inner_product` / `linear_combination` folds — `assemble_diagonal` belongs
to no fold cohort. It is **not** an [`apply_linop`](./krylov-step.md) variant either (the
operator/data divide is load-bearing — see § "Not an `apply_linop` variant").

## Context

L2 is the fusion-rotation layer (`book/src/L2/index.md`): "Kernel fusion across multiple
algebraic operations is unfolded into composition… Batched specialized BLAS calls are
written as compositions of base primitives." `assemble_diagonal` at L2 is the
diagonal-introspection primitive at that layer — a pure value-producing map from an
opaque square operator to its diagonal vector, with no control flow, no monadic state
threading, and no convergence predicate.

This entry is a **thin floor entry**, authored under the 2026-05-31 foundation-first
directive `l2-floor-under-l3-leaf-cohort` (extended this cycle from the BLAS-1 leaf
cohort to the operator-to-data primitive). Its purpose is floor *presence*: the firm L3
[`assemble-diagonal`](../L3/assemble-diagonal.md) (the iteration-rotation rendering, the
operator-to-data sibling of [`apply_linop`](../L3/apply_linop.md) consumed inside the
diagonal-preconditioner-apply chain of the Jacobi / Chebyshev smoother bodies) and the
firm L1 [`assemble-diagonal`](../L1/assemble-diagonal.md) (the mutation-rotation leaf)
sandwich a layer at which `assemble_diagonal` had no chapter. The L2 entry fills it so the
lowering chain L3 → L2 → L1 has a present chapter at every adjacent edge, and the L3 form
can lower to an adjacent L2 parent rather than non-adjacently to L1.

`assemble_diagonal` is **defined in L2 vocabulary** here (high→low discipline, CLAUDE.md
§Methodology invariants "Layers are defined high→low"): the signature, semantics, and
algebraic laws are stated at the L2 fusion-rotation resolution. Both adjacent rotations
are **degenerate identity-in-named-terms lowerings** (the vocabulary does not shift across
either edge), so per the 2026-06-01 vocabulary-shift redirect each is recorded as an
**in-line note rather than a dedicated theme**: how the L2 form lowers to L1 is the
§"Downward to L1" note below (demoted from the former `assemble-diagonal-leaf-identity`
L2>L1 theme cycle-050); how the L3 form lowers to L2 is the §"Downward to L2" in-line note
on the L3 [`assemble-diagonal`](../L3/assemble-diagonal.md) entry (demoted from the former
`assemble-diagonal-body-identity` L3>L2 theme cycle-050). This chapter does not define
`assemble_diagonal` in terms of L1 primitives or L0 mechanics.

The L1 entry [`L1/assemble-diagonal`](../L1/assemble-diagonal.md) is authoritative on every
factual claim about the Palace surface (the `AssembleDiagonal(diag)` virtual-method family
on the real `Operator` / complex `ComplexOperator` hierarchies, the concrete realisations
across sparse-CSR / matrix-free / parallel-wrapped / complex-wrapped representations, the
square-precondition enforcement sites, the Dirichlet `DiagonalPolicy` BC post-step, the
consuming smoother call sites, the libCEED diagonal-assembly unit test, and the complete L0
evidence list). This L2 entry adds **fusion-rotation framing** and does not duplicate those
Palace-surface details.

## Not an `apply_linop` variant

`assemble_diagonal` is the **operator-to-data sibling** of `apply_linop` on the
opaque-`LinearOperator` side of the L2 vocabulary, **not a variant of it** (OQ
`assemblediagonal-is-not-apply-linop-variant`, recorded at the L1 home). The two share the
opaque `LinearOperator` argument type and the L0 output-arg mutation idiom
(`A.AssembleDiagonal(diag)` writes through `diag`, the same destination-buffer pattern as
`apply_linop`'s `A.Mult(x, y)`), but they live on opposite sides of the operator/data
divide:

- `apply_linop :: (A: LinOp[(R: ...), (D: ...)], x: Tensor[$D]) -> Tensor[$R]` — takes a vector
  and returns the operator's *action* on it (admits rectangular `R ≠ D`).
- `assemble_diagonal :: (A: LinOp[(S: ...), $S]) -> Tensor[$S]` — takes **no vector** and
  returns operator-intrinsic *data* (intrinsically **square**, one shape group `S`).

There is no `x` to be linear in; the result is a property of `A` alone. Recording
`assemble_diagonal` as its own L2 floor — rather than folding it into `apply_linop`'s
variant axes — keeps that divide visible at the fusion-rotation layer, mirroring the L1 and
L3 entries' identical framing.

## No fold-parent (fork-independent)

`assemble_diagonal` belongs to **no L2 fold cohort**. This distinguishes it from the
cycle-041 BLAS-1 floor cohort, every member of which has a fold relationship to be disclaimed:
`dot` is the conjugation-axis *leaf-of* [`inner_product`](./inner_product.md), `nrm2` is a
*consumer-of* `inner_product`, `scal` is the arity-1 *member-of*
[`linear_combination`](./linear_combination.md). `assemble_diagonal` has no such parent —
it is a standalone operator-to-data primitive. There is no fold codomain to preserve, no
variadic / parametric generalization it specializes, and therefore no do-NOT-merge boundary
to police. The only sibling relationship is to `apply_linop` (operator/data divide, above),
which is a *sibling*, not a fold-parent.

## Signature

    assemble_diagonal :: LinOp[(S: ...), $S] -> Tensor[$S]
    assemble_diagonal A = diag(A)

Shape contract (named shape groups / operator shapes per [`l4_calculus`](../semantics/index.md) §1.2.1–§1.2.2; the diagonal is intrinsic to a square operator, so domain and range are one shape group `S`):

- **`A`** — `LinOp[(S: ...), $S]` — a **square** linear operator (domain group `S` equals
  range group `S`). Read-only (the L0 method is `const`; the L2 form never writes through
  `A`). The operator-representation axis (sparse-CSR / matrix-free / parallel-wrapped /
  complex-wrapped) is **absorbed at L2** into this opaque type — the L2 contract sees only
  "extract the diagonal of this square operator"; the L2 form does not branch on
  representation. The element type (real or complex) is parameterised.
- **result** — `Tensor[$S]` — the diagonal vector, congruent to the operator's (shared) square
  shape group `S`. Element `result[i]` is the `(i, i)` entry of `A`. A fresh
  value; no L0 destination buffer is mentioned at L2 (the destination-binding rotation is an
  L1>L0 concern).

The **square requirement** (range group ≡ domain group) is intrinsic: a diagonal is only defined where the
domain and range index sets coincide. This is the chief signature difference from the
sibling `apply_linop`, which admits rectangular `R ≠ D`. Palace enforces the square
precondition at the L0 source for the AMR path (`MFEM_VERIFY(&trial_fespace ==
&test_fespace, "Diagonal assembly is only available for square ParOperator!")`,
`palace/linalg/rap.cpp:165-166` — predicate at `:165`, message string at `:166`) and the
matrix-free path (`MFEM_VERIFY(diag.Size() == height, ...)`,
`palace/fem/libceed/operator.cpp:120`) — both transitive through the L1 home.

`LinOp[(S: ...), $S]` is an **opaque type** at L2: its internal representation is not part
of the L2 signature. The operator is guaranteed to expose a diagonal — the base
`ComplexOperator::AssembleDiagonal` aborts (`palace/linalg/operator.cpp:25-28`), so the
operator's L2 domain is the diagonal-capable subclasses (a precondition, not a variant — see
Variant axes).

The L2 signature is identical in shape to the L1
[`assemble-diagonal`](../L1/assemble-diagonal.md) signature; the rotation L2 → L1 is
identity-in-form on the primitive (the de-fusion the L2 layer un-does lives at the L0
representation's diagonal-extraction *implementation*, recorded by the §"Downward to L1"
in-line note below — a degenerate identity-in-named-terms edge, not a dedicated theme — not
in the signature).

## Semantics

`assemble_diagonal A` returns the vector of main-diagonal entries of `A`:
`result[i] = Aᵢᵢ = eᵢᵀ A eᵢ` for `i ∈ [0, N)`, where `eᵢ` is the `i`-th standard basis
vector. The result is determined entirely by `A` — the L2 form is **pure** (extracting the
diagonal of the same `A` twice returns the same value), with no hidden state, no per-call
side effects, no in-place mutation at the L2 surface. It consumes `A` and produces a fresh
`Tensor[$S]`; there is no destination buffer (the L0 in-place destination `diag`, its sizing
`diag.SetSize(height)`, and its `diag = 0.0` zero-init reappear only at the L1>L0 lowering).

The relationship `result[i] = eᵢᵀ A eᵢ` is the **mathematical** definition of the diagonal,
**not** the implementation: Palace never forms `N` matrix-vector products. The `eᵢᵀ A eᵢ`
form is the algebraic specification the L0 realisations satisfy — it is what relates
`assemble_diagonal` to the sibling `apply_linop` (the diagonal entries are the would-be
results of probing `A` with basis vectors) **without** making `assemble_diagonal` a *use* of
`apply_linop`. The two are L2 siblings on the opaque-operator side, not a dependency chain.

### Fusion note

The L2 fusion content for `assemble_diagonal` is **degenerate**: there is no kernel-fusion
across multiple algebraic operations to unfold at the operator-to-data boundary. The L0
"fusion" present in the diagonal-extraction realisations is the *representation-specific
diagonal-extraction mechanic*, which is below the L2 resolution and is an L0 concern surfaced
by the L1>L0 lowering, not an L2 composition to de-fuse:

- the **sparse-CSR** path reads the stored diagonal directly via a single Hypre kernel
  (`HypreCSRMatrix::AssembleDiagonal` calls `hypre_CSRMatrixExtractDiagonal`,
  `palace/linalg/hypre.cpp:88`) — the **exact** diagonal;
- the **matrix-free** path accumulates element-local diagonal contributions via libCEED
  (`CeedOperatorLinearAssembleAddDiagonal`, `palace/fem/libceed/operator.cpp:139`, under an
  OpenMP region, after `diag = 0.0`) — the **approximate** diagonal for the high-order
  Nedelec case (see the load-bearing non-law);
- the **AMR parallel** path assembles via the absolute-value prolongation transpose
  `|P|ᵀ dₗ` (`hP->AbsMultTranspose(1.0, lx, 0.0, diag)`, `palace/linalg/rap.cpp:174`, per the
  convergent-diagonal note at `:163-164`) then applies a Dirichlet `DiagonalPolicy` to BC
  true-dofs (`:184-190`);
- the **complex** paths assemble the real and imaginary diagonals separately
  (`ComplexWrapperOperator::AssembleDiagonal`, `palace/linalg/operator.cpp:85-96`;
  `ComplexParOperator::AssembleDiagonal`, `palace/linalg/rap.cpp:467-479`).

These are **representation-axis-absorbed L0 mechanics**, not an L2 fusion across operations.
Unlike `dot` (whose L2 fusion note de-fuses the Hypre strided-pass + MPI-collective
reduction kernels into the canonical reduction), `assemble_diagonal` has no multi-operation
kernel-fusion to unfold — the operator-to-data map is a single semantic step at L2. The L2
floor therefore records the fusion as this one note and **defers the de-fusion treatment to
the L1>L0 lowering** (which pins which diagonal-extraction mechanic each lowered call
selects, and is where the matrix-free element-accumulation order — the source of the
high-order-Nedelec approximation — becomes visible).

The Dirichlet-boundary diagonal policy (`DiagonalPolicy::DIAG_ONE` / `DIAG_ZERO`,
`palace/linalg/rap.cpp:184-190`) is **not** part of the bare `assemble_diagonal` operator at
L2: it is a BC-elimination post-step the `ParOperator` path applies after assembling the
interior diagonal. At L2 the operator `A` *is* the BC-eliminated operator, so its diagonal
already reflects the policy; the policy is an L1>L0 lowering concern, not an L2 parameter.

## Algebraic laws

The six laws below hold and are **inherited unchanged from the L1 leaf**
[`L1/assemble-diagonal`](../L1/assemble-diagonal.md) §"Algebraic laws"; the L2 form is
value-thread-isomorphic to the L1 form. Reproduced so the L2 reader does not have to reach
to L1. These are **operator-introspection laws** — they relate the diagonal of a
*constructed* operator to the diagonals/entries of its parts, not laws of a vector update.
Absences are deliberate.

1. **Linearity over operator scaling**: `assemble_diagonal (α·A) = α · assemble_diagonal A`
   for any scalar `α`. The diagonal of a scaled operator is the scaled diagonal
   (`(α·A)ᵢᵢ = α·Aᵢᵢ`).
2. **Linearity over operator sum**: `assemble_diagonal (A + B) = assemble_diagonal A +
   assemble_diagonal B` for square `A`, `B` sharing shape group `S` (`(A + B)ᵢᵢ = Aᵢᵢ + Bᵢᵢ`).
   Witnessed structurally by `ComplexWrapperOperator::AssembleDiagonal`
   (`palace/linalg/operator.cpp:85-96`), which assembles real and imaginary parts
   independently into `diag.Real()` / `diag.Imag()` after `diag = 0.0`.
3. **Zero operator**: `assemble_diagonal 0_op = 0_$S` (the zero vector of shape group `S`). Special
   case of law 1 with `α = 0`.
4. **Identity operator**: `assemble_diagonal I = 𝟙_$S` (the all-ones vector of shape group `S`),
   since `Iᵢᵢ = 1` for all `i`.
5. **Diagonal-operator round-trip**: `assemble_diagonal (Diag(d)) = d` for the operator
   `Diag(d)` whose action is element-wise multiplication by `d`. Extracting the diagonal of a
   diagonal operator recovers its defining vector — the law that makes `assemble_diagonal`
   the left-inverse of diagonal-operator construction, and the round-trip the
   diagonal-preconditioner apply relies on (`Jacobi(A)·x = (1/diag(A)) ⊙ x`).
6. **Complex linearity (real/imag split)**: for a complex operator `A = Ar + i·Ai`,
   `assemble_diagonal A = assemble_diagonal Ar + i · assemble_diagonal Ai`. Witnessed by
   `ComplexWrapperOperator::AssembleDiagonal` (`palace/linalg/operator.cpp:85-96`) and
   `ComplexParOperator::AssembleDiagonal` (`palace/linalg/rap.cpp:467-479`). A specialisation
   of law 2 to the equivalent-real `Ar + i·Ai` decomposition.

Laws that explicitly **do not** hold (inherited unchanged from L1):

- **Diagonal of a product**: `assemble_diagonal (A · B) ≠ assemble_diagonal A ⊙
  assemble_diagonal B` in general — `(A·B)ᵢᵢ = Σ_k Aᵢₖ Bₖᵢ` is a full row·column
  contraction, not the product of the two `(i,i)` entries. Equality holds only when *both*
  operators are diagonal. Recorded as an absence because diagonal-of-product is a frequent
  false intuition; no Palace path assembles a product's diagonal this way.
- **Transpose invariance is non-distinguishing**: `assemble_diagonal Aᵀ = assemble_diagonal
  A` *does* hold (`(Aᵀ)ᵢᵢ = Aᵢᵢ`), but it is recorded as a non-distinguishing identity
  rather than a useful law — Palace exposes no transpose-mode axis on `AssembleDiagonal`
  (unlike `apply_linop`'s `Mult` / `MultTranspose`) precisely because the diagonal is
  transpose-invariant. For complex operators the Hermitian transpose conjugates the diagonal:
  `assemble_diagonal Aᴴ = conj(assemble_diagonal A)`. The **absence of a transpose-mode
  variant axis** is the chief variant-profile difference from the sibling `apply_linop`.
- **Exactness across representations (LOAD-BEARING — preserved through the floor)**: a
  sparse-matrix realisation of `A` reads the **exact** stored diagonal, while a matrix-free
  high-order-Nedelec (H(curl)) realisation of the *same* mathematical operator produces an
  **approximate** diagonal (face dofs shared across elements in 3D make the element-local
  summation differ from the true assembled diagonal). Load-bearing per the CLAUDE.md taxonomy:
  the representation can change the diagonal *value* (not just its bit pattern). The six laws
  above hold for the exact diagonal; their matrix-free realisation may be approximate. This is
  the one case where the difference is semantic (a different value), not floating-point
  reduction-order noise. **The L2 fusion rotation does NOT erase this approximation** — it is
  recorded here as an explicit positively-anchored non-law (per the OQ caveat-lifetime note),
  exactly as at L1 and L3. The approximation is acceptable *because* the diagonal feeds an
  inexact preconditioner (a Jacobi / Chebyshev smoother tolerates an approximate diagonal
  scaling). Sourced from the Palace AMR convergent-diagonal note
  (`palace/linalg/rap.cpp:163-164`), the matrix-free element-accumulation site
  (`palace/fem/libceed/operator.cpp:139`), the Palace comment naming the matrix-free
  *approximate* diagonal at the consumer (`palace/linalg/jacobi.hpp:15-16`), and test-witnessed
  (`test/unit/test-libceed.cpp:367-376`, relaxing `rtol` to `1.0` for the high-order 3D
  Nedelec non-tensor-basis case). Recorded as a non-law, not a status reduction — the
  structure is exhaustively cited and the approximation is documented and test-witnessed, so
  the entry is `firm`, not `partly-constructive`.
- **Linearity strictness in floating point**: laws 1, 2, 6 are exact in ℝ / ℂ; in IEEE-754 the
  assembled diagonal sums round, so equality is approximate (and, for the matrix-free
  high-order case, *not even* approximate to round-off — the approximation is structural, per
  the previous non-law).

## Dependencies

- **Same-layer (L2):** none. `assemble_diagonal` is a **leaf operator-introspection
  primitive** at L2 — the operator-to-data sibling of `apply_linop` on the
  opaque-`LinearOperator` side of the L2 vocabulary. Its sub-operations (Hypre CSR diagonal
  read, libCEED element-local diagonal accumulation, prolongation-transpose assembly) are
  below the L2 layer's resolution and visible only in the L1>L0 lowering. It composes no other
  L2 operator.
- **No fold-parent (fork-independent):** `assemble_diagonal` belongs to no L2 fold cohort —
  unlike the cycle-041 BLAS-1 floors, it is neither leaf-of, consumer-of, nor member-of any
  fold (`inner_product` / `linear_combination`). There is no do-NOT-merge boundary to police.
- **Not factored through `apply_linop`:** despite the algebraic specification `result[i] =
  eᵢᵀ A eᵢ`, that is the mathematical definition, not the implementation (Palace forms no
  basis-vector probes); treating it as a dependency would falsely imply `N` operator applies.
  The two are L2 siblings, not a chain (see § "Not an `apply_linop` variant").
- **Consumers (L2)** (cross-reference, not reverse-dependencies) — the
  diagonal-preconditioner-apply fan-out that motivated the L1 harvest, transported to L2:
  the Jacobi smoother (`dinv = assemble_diagonal A; dinv = reciprocal(dinv)` then
  `y = dinv ⊙ x`; L0 chain `op.AssembleDiagonal(dinv); dinv.Reciprocal();` at
  `palace/linalg/jacobi.cpp:79`); the Chebyshev smoother, both 4th-kind and 1st-kind (identical
  `op.AssembleDiagonal(dinv); dinv.Reciprocal();` setup, `palace/linalg/chebyshev.cpp:177`);
  block-Jacobi / polynomial preconditioners reuse the same chain. The `reciprocal` and
  element-wise product that complete the diagonal-preconditioner apply are themselves L2
  primitive candidates (`reciprocal` / `elementwise_product` — referenced here as plain text;
  their L3 floors landed cycle-038, L2 floors not yet authored).
- **L1 anchor:** [`L1/assemble-diagonal`](../L1/assemble-diagonal.md) (firm) — authoritative
  on the Palace surface (the abstract decls + concrete realisations across
  sparse/matrix-free/parallel/complex-wrapped representations, the square-precondition
  enforcement sites, the Dirichlet `DiagonalPolicy` BC post-step, the consuming smoother call
  sites, the libCEED diagonal-assembly unit test, the complete L0 evidence list). The L2 entry
  does not duplicate those details.
- **L3 sibling this floor sits under:** [`L3/assemble-diagonal`](../L3/assemble-diagonal.md)
  (firm cycle-037) — the iteration-rotation rendering; the operator-to-data field operation
  whose adjacent L2 parent this entry supplies.

## Variant axes

`assemble_diagonal` has **one orthogonal variant axis at L2, plus one collapsed-and-absorbed
axis** — the same framing as L1 (`book/src/L1/assemble-diagonal.md` §"Variant axes") and L3,
transported unchanged.

One orthogonal axis:

- **element-type** (`real` | `complex`) — collapsed to a single parameterised operator at L2.
  The L0 source splits this into two parallel hierarchies (real
  `Operator::AssembleDiagonal(Vector &diag)`, complex
  `ComplexOperator::AssembleDiagonal(ComplexVector &diag)`); at L2 these collapse to one
  operator parameterised by element type. The complex case assembles the real and imaginary
  diagonals separately (law 6); the per-element diagonal-extraction relationship is otherwise
  identical.

Collapsed (absorbed) axis:

- **operator-representation** (`sparse-CSR` | `matrix-free` | `parallel-wrapped` |
  `complex-wrapped`) — **absorbed** into the opaque `LinOp[(S: ...), $S]` type. The L0
  concrete overrides (`HypreCSRMatrix`, `fem::libceed::Operator`, `ParOperator` /
  `ComplexParOperator`, `ComplexWrapperOperator`) collapse to a single L2 type; the L2 contract
  sees only "extract the diagonal of this square operator". This is the canonical application
  of [`variant-absorption`](../concepts/variant-absorption.md) — the same absorption the
  sibling `apply_linop` performs over its representation axis. The **load-bearing
  exact-vs-approximate caveat** (sparse exact; matrix-free high-order-Nedelec approximate) is
  the one place the absorbed axis surfaces semantically; it is recorded as a non-law (above)
  and concretised in the L1>L0 lowering.

Non-axes (recorded for disambiguation, inherited from L1):

- **transpose-mode**: **not** an axis — the diagonal is transpose-invariant (see the non-law),
  so Palace exposes no `AssembleDiagonalTranspose`. The chief variant-profile contrast with the
  sibling `apply_linop`, which has a genuine three-valued transpose-mode axis.
- **abs-vs-signed diagonal**: there is **no** absolute-value-diagonal variant. The absolute
  value appears only *inside* the `ParOperator` AMR assembly (`|P|ᵀ dₗ`, the entry-wise-absolute
  prolongation kept absolute to keep the assembled diagonal convergent on a non-conforming
  mesh, `palace/linalg/rap.cpp:174` per the note at `:163-164`) — it is the *prolongation* that
  is taken absolute, not the diagonal entries; the output diagonal retains its sign. The abs is
  an L0 assembly mechanic absorbed into the representation axis.
- **partial-domain (abort)**: the base `ComplexOperator::AssembleDiagonal` aborts
  (`palace/linalg/operator.cpp:25-28`). This is not a variant — it marks that the operator's
  L2 domain is the diagonal-capable subclasses (a precondition, not a variant).

The variant-axis profile (one orthogonal + one absorbed) matches the L1 and L3 entries
exactly. **No new axes introduced by the L2 rendering; no axes merged or split; the
orthogonal-vs-absorbed framing is preserved.**

## Status

`firm` — the L2 form is value-thread-isomorphic to the firm L1 leaf
[`L1/assemble-diagonal`](../L1/assemble-diagonal.md) (identity-in-form rotation on the
primitive); every algebraic law is a standard property of the matrix-diagonal map inherited
unchanged (operator-scaling / sum linearity, identity, zero, diagonal round-trip, complex
real/imag split), and every non-law is catalogued explicitly (diagonal-of-product,
non-distinguishing transpose invariance, the **load-bearing exact-vs-approximate
representation caveat preserved through the floor**, floating-point linearity strictness). The
variant-axis profile is one orthogonal (element-type) + one absorbed (operator-representation),
inherited unchanged from L1.

This is a **thin floor entry** authored under the 2026-05-31 foundation-first directive
`l2-floor-under-l3-leaf-cohort` (extended this cycle from the BLAS-1 leaf cohort to the
operator-to-data primitive): its purpose is floor *presence* so the firm L3
[`assemble-diagonal`](../L3/assemble-diagonal.md) field operation rests on an adjacent
same-named L2 parent (per CLAUDE.md §Methodology invariants **Identity-lowerings still require
both L levels**) rather than skipping a layer to L1. The fusion-rotation content is degenerate
(no multi-operation kernel-fusion to unfold at the operator-to-data boundary; the L0
representation's diagonal-extraction mechanics are absorbed into the representation axis and
deferred to the L1>L0 lowering); this floor records it as one deferring note.

The laws are syntactic identities on the matrix-diagonal map (operator-algebra on a read of
the operator's stored / accumulated diagonal) — so the entry is `firm`, not `rough-in`: the
missing dedicated unit test for the bare operator does not gate syntactic-identity laws (the
`apply_linop`-style firm-on-positive-structure situation, not the `eigsolve`-convergence-
semantics situation). The one caveat (matrix-free high-order-Nedelec approximate diagonal) is
recorded as a non-law, not a status reduction: the structure is exhaustively cited at the L1
home and the approximation is a documented, test-witnessed property of the matrix-free
representation, not an unresolved gap — so this entry is `firm`, exactly as the L1 entry is
(NOT `partly-constructive`).

## L2 vs L1 distinction

- **L1**: pure-functional operator-to-data extraction `d = assemble_diagonal(A)`.
  Mutation-rotation layer — the L0 destination buffer `diag` is dropped from the signature
  (along with the sizing, the zero-init, the workspace, and the Dirichlet policy); the
  operator-representation axis is absorbed (the opaque `LinearOperator` type). The L1
  vocabulary mirrors the source `AssembleDiagonal(diag)` virtual with pure-functional binding.
- **L2**: the same extraction `d = assemble_diagonal(A)` rendered as the fusion-rotation floor.
  The representation-specific diagonal-extraction mechanics (the sparse-CSR Hypre
  stored-diagonal read, the matrix-free libCEED element-local accumulation, the AMR `|P|ᵀ dₗ`
  prolongation-transpose assembly, the complex real/imag split) are recognized as
  representation-axis-absorbed L0 mechanics — there is no multi-operation kernel-fusion to
  de-fuse, so the fusion rotation is degenerate. The signature is identical to L1; the rotation
  L2 → L1 is identity-in-form on the primitive (what little the L2 layer un-does is at the
  representation implementation, captured by the L2>L1 lowering theme — not in the signature).

The two layers' entries are value-thread-isomorphic on the primitive itself, sharing
signature, algebraic laws (six), non-laws (four, including the load-bearing exact-vs-approximate
caveat), and variant-axis profile (one orthogonal + one absorbed). The L2 entry exists for
floor presence — so the L3 [`assemble-diagonal`](../L3/assemble-diagonal.md) field operation
has an adjacent L2 parent.

## Downward to L1 (in-line note)

The L2>L1 edge is a **degenerate identity-in-named-terms lowering** — the L2 floor and the L1
[`assemble-diagonal`](../L1/assemble-diagonal.md) leaf are value-thread-isomorphic on the leaf:
the L2 group-form signature `assemble_diagonal :: LinOp[(S: ...), $S] -> Tensor[$S]`
lowers to the L1 rank-1 realization `LinearOperator[N, N] -> Tensor[N]` (the concrete flat
dof-vector length), same
`assemble_diagonal A = diag(A)` extraction (`result[i] = Aᵢᵢ`), same intrinsic-square (range
group ≡ domain group) precondition, same opaque-`LinearOperator` representation-axis absorption, same six laws + four
non-laws. The vocabulary does not shift across the edge, so per the 2026-06-01 vocabulary-shift
redirect this is recorded **as this in-line note, NOT as a dedicated L2>L1 theme** (the former
`assemble-diagonal-leaf-identity.md` theme, demoted cycle-050).

There is **no fold-parent**: unlike the cycle-041 BLAS-1 floors (`dot` leaf-of `inner_product`,
`scal` member-of `linear_combination`), `assemble_diagonal` is the operator-to-data sibling of
`apply_linop`, belonging to no fold cohort, so there is nothing to defer fusion to. The L2 layer's
defining work — kernel-fusion de-fusion — is **degenerate** here: the operator-to-data boundary
carries no multi-operation kernel-fusion. The L0 "fusion" present in the diagonal-extraction
realizations is the *representation-specific diagonal-extraction mechanic* (the sparse-CSR
`hypre_CSRMatrixExtractDiagonal` read, `palace/linalg/hypre.cpp:88`; the matrix-free
`CeedOperatorLinearAssembleAddDiagonal` element-local accumulation, `palace/fem/libceed/operator.cpp:139`;
the AMR `|P|ᵀ dₗ` absolute-value-prolongation assembly, `palace/linalg/rap.cpp:174`; the complex
real/imag split, `palace/linalg/operator.cpp:85-96` / `palace/linalg/rap.cpp:467-479`) — all
representation-axis-absorbed L0 concerns surfaced by the L1>L0 lowering, not an L2 composition to
de-fuse. So the L2>L1 edge is the identity, with the representation-selection / zero-init /
element-accumulation-order treatment deferred to the L1>L0
[`assemble-diagonal-mutation-rotation`](../L1-L0/assemble-diagonal-mutation-rotation.md) theme.

**Load-bearing non-law preserved through the edge (NOT erased).** The matrix-free
high-order-Nedelec (H(curl)) **approximate-diagonal** non-law carries across this edge unchanged: a
sparse-matrix realization of `A` reads the **exact** stored diagonal, while a matrix-free
high-order-Nedelec realization of the *same* mathematical operator produces an **approximate**
diagonal (face dofs shared across elements in 3D). Load-bearing per the CLAUDE.md taxonomy — the
representation can change the diagonal *value*, not merely its bit pattern. Because the L2 fusion
content is degenerate there is no de-fusion step in which the approximation could be lost; the
non-law is preserved by reference, NOT erased. Sourced from the Palace AMR convergent-diagonal note
(`palace/linalg/rap.cpp:163-164`), the matrix-free element-accumulation site
(`palace/fem/libceed/operator.cpp:139`), the Palace comment naming the matrix-free *approximate*
diagonal at the consumer (`palace/linalg/jacobi.hpp:15-16`), and test-witnessed
(`test/unit/test-libceed.cpp:367-376`, relaxing `rtol` to `1.0` for the high-order 3D Nedelec
non-tensor-basis case) — all transitive through the L1 home.

## Evidence

The L2 form is value-thread-isomorphic to the L1 form (identity-in-form on the primitive's
signature); all L0 evidence is transitive through the firm L1 leaf. Direct citations relevant
to this L2 entry (paths relative to `reference/palace/`; L0 ranges self-verified via
`tools/citecheck/citecheck.py --anchor` this invocation):

- [`book/src/L1/assemble-diagonal.md`](../L1/assemble-diagonal.md) (firm) — authoritative on
  the Palace surface, the signature, the six algebraic laws (inherited unchanged at L2), the
  four non-laws (inherited unchanged, including the load-bearing exact-vs-approximate caveat),
  the variant axes (one orthogonal + one absorbed, inherited unchanged), and the complete L0
  evidence list.
- [`book/src/L3/assemble-diagonal.md`](../L3/assemble-diagonal.md) (firm cycle-037) — the L3
  consumer this floor goes under; the iteration-rotation rendering whose adjacent L2 parent
  this entry supplies; the operator-to-data sibling of [`L3/apply_linop`](../L3/apply_linop.md).
- [`book/src/L2/index.md`](./index.md) §"Identity-in-form BLAS-1 floors" — the floor cohort
  and the foundation-first directive `l2-floor-under-l3-leaf-cohort` this entry extends to the
  operator-to-data primitive.
- [`book/src/L2/dot.md`](./dot.md) (firm cycle-041) — the structural precedent: a thin
  identity-in-form L2 floor entry. (`dot` is leaf-of a fold; this entry is fork-independent —
  the differences are noted in § "No fold-parent".)
- `palace/linalg/operator.cpp:25-28` — `ComplexOperator::AssembleDiagonal` base
  `MFEM_ABORT("Base class ComplexOperator does not implement AssembleDiagonal!")` (the
  partial-domain non-axis; the operator's L2 domain is the diagonal-capable subclasses).
  **Self-verified (anchor `MFEM_ABORT` at :27).**
- `palace/linalg/operator.cpp:85-96` — `ComplexWrapperOperator::AssembleDiagonal`
  (`diag = 0.0; if (Ar) Ar->AssembleDiagonal(diag.Real()); if (Ai)
  Ai->AssembleDiagonal(diag.Imag());`) — witnesses laws 2 and 6 (sum / complex
  real-imag-split linearity) and the `diag = 0.0` zero-init. **Self-verified (anchor
  `ComplexWrapperOperator::AssembleDiagonal` at :85).**
- `palace/linalg/hypre.cpp:85-89` — `HypreCSRMatrix::AssembleDiagonal`
  (`hypre_CSRMatrixExtractDiagonal` at `:88`) — the **exact** sparse-CSR diagonal read.
  **Self-verified (anchor `hypre_CSRMatrixExtractDiagonal` at :88).**
- `palace/fem/libceed/operator.cpp:120` — `MFEM_VERIFY(diag.Size() == height, ...)` (the
  square precondition, matrix-free path); `:139` — `CeedOperatorLinearAssembleAddDiagonal`
  (the matrix-free element-local accumulating assembly; the source of the high-order-Nedelec
  approximation). **Self-verified (anchors `diag.Size() == height` at :120,
  `CeedOperatorLinearAssembleAddDiagonal` at :139).**
- `palace/linalg/rap.cpp:165-166` — `MFEM_VERIFY(&trial_fespace == &test_fespace, "Diagonal
  assembly is only available for square ParOperator!")` (the square precondition, AMR path;
  predicate at `:165`, message string at `:166`); `:163-164` — the AMR `|P|ᵀ dₗ`
  convergent-diagonal note (the documented source of the approximate-diagonal caveat); `:174` —
  `hP->AbsMultTranspose(1.0, lx, 0.0, diag)` (the abs-prolongation assembly); `:184-190` — the
  Dirichlet `DiagonalPolicy` `DIAG_ONE` / `DIAG_ZERO` BC post-step; `:467-479` —
  `ComplexParOperator::AssembleDiagonal` (complex parallel real-imag-split assembly; witnesses
  law 6). **Self-verified (anchors `trial_fespace == &test_fespace` at :165,
  `ComplexParOperator::AssembleDiagonal` at :467; convergent-diagonal note + `AbsMultTranspose`
  at :174 + BC policy on-disk-confirmed).**
- `palace/linalg/jacobi.cpp:75-82` — `JacobiSmoother::SetOperator`'s `op.AssembleDiagonal(dinv);
  dinv.Reciprocal();` (the diagonal-preconditioner-apply consumer chain; `AssembleDiagonal` at
  `:79`). **Self-verified (anchor `AssembleDiagonal` at :79).**
- `palace/linalg/jacobi.hpp:15-16` — the Palace comment naming the matrix-free **approximate**
  diagonal ("...allows for (approximate) diagonal construction for matrix-free operators.") —
  the load-bearing caveat at the consumer.
- `palace/linalg/chebyshev.cpp:170-178` — `ChebyshevSmoother::SetOperator`'s identical
  `op.AssembleDiagonal(dinv); dinv.Reciprocal();` setup (second consumer code path;
  `AssembleDiagonal` at `:177`). **Self-verified (anchor `AssembleDiagonal` at :177).**
- `test/unit/test-libceed.cpp:343-376` — the diagonal-assembly test: confirms `AssembleDiagonal`
  reproduces the assembled-matrix diagonal to `rtol = 1.0e-12` in general, relaxing `rtol` to
  `1.0` exactly for high-order 3D Nedelec non-tensor-basis spaces (`:367-376`) — the
  test-witnessed load-bearing approximation. L0-equivalent semantic documentation per CLAUDE.md
  §"Tests as semantic supplement". **Self-verified (anchor `rtol` at :371,:375).**
