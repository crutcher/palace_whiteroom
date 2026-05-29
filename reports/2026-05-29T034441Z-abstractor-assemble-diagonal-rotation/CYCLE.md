---
agent: abstractor
invoked_at: 2026-05-29T03:50:30Z
scope: L1>L0 theme sketch — assemble-diagonal-mutation-rotation
status: integrated
integrated_at: 2026-05-29T06:05:00Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-020 finalize (staging row #4). assemble-diagonal-mutation-rotation NEW firm L1>L0 file (Write, not a stub promotion; operator-to-data diagonal extraction; 4 L0 sub-patterns). Landed firm NOT partly-constructive — the matrix-free high-order-Nedelec approximate-diagonal caveat is a POSITIVELY-ANCHORED load-bearing non-law (jacobi.hpp:15-16 + rap.cpp:163-164 + test-libceed rtol=1.0), not a negative-anchor reconstruction. New SUMMARY chapter line after scal; new L1-L0/index dep-map row after dot / before minres-bicgstab obstruction rows. reciprocal/elementwise_product forward-refs correctly plain-text (speculative-tier). Post-repair 4 narrow-line drifts (AbsMultTranspose :172→:174 + 3 more) already fixed before apply; enclosing ranges correct. Resolves theme-authoring OQ assemble-diagonal-mutation-rotation (:110; meta-phase migrates). L1>L0 themes contribute to 12→15. retroactive-budget 0; clean build."
inputs:
  - book/src/L1/assemble-diagonal.md (firm L1 entry, landed cycle-019; operator-to-data primitive)
  - palace/linalg/operator.hpp:21 (using Operator = mfem::Operator alias)
  - palace/linalg/operator.hpp:51 (virtual ComplexOperator::AssembleDiagonal decl)
  - palace/linalg/operator.cpp:25-28 (base ComplexOperator abort)
  - palace/linalg/operator.cpp:85-96 (ComplexWrapperOperator::AssembleDiagonal, diag = 0.0 + real/imag split)
  - palace/linalg/hypre.cpp:85-89 (HypreCSRMatrix exact sparse-CSR diagonal read)
  - palace/fem/libceed/operator.cpp:116-143 (matrix-free element-local accumulation; square verify :120; diag=0.0 :121; CeedOperatorLinearAssembleAddDiagonal :139)
  - palace/linalg/rap.cpp:154-193 (ParOperator AMR |P|ᵀ dₗ path; square verify :165; convergent-diagonal comment :163-164; AbsMultTranspose :174; DiagonalPolicy :180-191)
  - palace/linalg/rap.cpp:467-479 (ComplexParOperator real/imag split)
  - palace/linalg/jacobi.cpp:79-80 (consuming chain: op.AssembleDiagonal(dinv); dinv.Reciprocal();)
  - palace/linalg/jacobi.hpp:15-16 (approximate-matrix-free non-law comment)
  - palace/linalg/chebyshev.cpp:177-178, 240-241 (Chebyshev consuming chains)
  - test/unit/test-libceed.cpp:343-376 (diagonal-assembly test; rtol=1.0e-12 general :360; rtol=1.0 high-order-Nedelec relaxation, condition :365-369, assignment :371)
---

# CYCLE: L1>L0 theme sketch — assemble-diagonal-mutation-rotation

## Summary

The firm L1 entry `book/src/L1/assemble-diagonal.md` (landed cycle-019) lifts the
`AssembleDiagonal(diag)` virtual-method family on the real `Operator` / complex
`ComplexOperator` hierarchies to a single pure-functional **operator-to-data**
primitive `assemble_diagonal(A) = diag(A) :: LinearOperator[N,N] -> Tensor[N]`. The
cycle-019 harvester forward-referenced this exact lowering theme as a follow-up; no stub
home exists yet. This theme is a fresh file. It narrates **high→low** how the pure L1 form
`assemble_diagonal(A) -> diag` lowers into Palace's L0 `A.AssembleDiagonal(diag)`
out-parameter mutation pattern — an "operator-to-data materialisation under out-parameter
mutation" rotation. It belongs to the in-place-mutation theme family
(`apply-linop-mutation-rotation` is the closest sibling — both mutate a destination buffer
through a virtual method on the operator object) but is distinguished by **no input
vector**: where `apply_linop` mutates `y` from `(A, x)`, `assemble_diagonal` mutates `diag`
from `A` alone, and the output is operator-*intrinsic* data, not the operator's action.

The rewrite decomposes into four representation sub-patterns (sparse-CSR exact read;
matrix-free element-local accumulation; parallel AMR absolute-value-prolongation transpose
with a Dirichlet `DiagonalPolicy` post-step; complex real/imag split) plus the
partial-domain abort, all of which collapse to the single opaque-`LinearOperator` L1 form.
The theme carries one **load-bearing non-law caveat verbatim from the L1 entry**: for
matrix-free high-order Nedelec (H(curl)) operators in 3D the assembled diagonal is
**approximate** (face-dof sharing), cited `palace/linalg/jacobi.hpp:15-16` + the
convergent-diagonal comment `palace/linalg/rap.cpp:163-164` + the test relaxation
`test/unit/test-libceed.cpp:365-371` (condition :365-369, `rtol = 1.0` assignment :371).
The real-path `AssembleDiagonal` resolves into
vendored MFEM through the alias `using Operator = mfem::Operator`
(`palace/linalg/operator.hpp:21`); the theme cites the Palace call sites and the alias, NOT
MFEM internals, and logs the upstream dependency as an OQ.

Status is **firm**: the structural decomposition is recognised and exhaustively cited
across all four representations + the abort + the two consuming smoother families, and the
approximate-diagonal caveat is a **positively-anchored** non-law (a Palace comment that
names it + a test that relaxes its tolerance for it), not a reconstruction from negative
anchors — so this is NOT `partly-constructive`.

## Proposed changes

```edit:book/src/L1-L0/assemble-diagonal-mutation-rotation.md
# assemble-diagonal-mutation-rotation

The mutation rotation for linear-operator diagonal extraction. Lowers the
pure L1 form `assemble_diagonal(A) = diag(A)` into Palace's in-place L0
virtual `AssembleDiagonal(diag)` family on the `Operator` /
`ComplexOperator` class hierarchies. Companion to
[`apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md): both
lower an L1 pure-functional form into an L0 in-place mutation through a
virtual method on the operator object — but where `apply_linop` mutates the
output buffer `y` from `(A, x)` (an operator *action*), `assemble_diagonal`
mutates the output buffer `diag` from `A` **alone** (operator-intrinsic
*data*). There is no input vector and no transpose-mode / accumulate-mode
axis (the diagonal is transpose-invariant; see the L1 entry's non-laws);
the only orthogonal L1 axis is element-type (real / complex), and the
operator-representation axis is absorbed at L1 and surfaces here as four L0
sub-patterns.

## Slug

`assemble-diagonal-mutation-rotation`

## L1 form (LHS)

The pure-functional operator-to-data diagonal extraction
([`L1/assemble-diagonal`](../L1/assemble-diagonal.md)):

    diag = assemble_diagonal(A)            -- diag[i] = Aᵢᵢ, A square N×N

`A` is an opaque square `LinearOperator[N, N]`; the result is a fresh
`Tensor[N]`. No input vector, no destination buffer in the L1 signature, no
sizing, no zero-init, no workspace, no Dirichlet policy. There is **no
transpose variant** (the diagonal is transpose-invariant) and **no
accumulate variant** (`AssembleDiagonal` always materialises the full
diagonal; the only accumulation is the internal element-local one of the
matrix-free path, an L0 mechanic). The single orthogonal L1 axis is the
element type — real vs complex — recoverable as the two parallel
hierarchies below.

## L0 form (RHS)

Four representation sub-patterns of the same rewrite, distinguished by the
operator-representation axis absorbed at L1, plus a partial-domain abort.
All sub-patterns share the same mutation-rotation shape: the L1 output
value binds to the L0 destination argument `diag`, the operator becomes the
receiver of the method call, and there is **no input argument** (contrast
`apply_linop`, whose `x` becomes the method's first argument). The
destination `diag` is sized (`SetSize(height)`) and/or zero-initialised
(`diag = 0.0`) by the L0 method before it is written; the operator `A` is
read-only (the method is `const`).

### Sub-pattern A — exact sparse-CSR diagonal read (`HypreCSRMatrix`)

    A.AssembleDiagonal(diag);              // real path: HypreCSRMatrix::AssembleDiagonal
    // body: diag.SetSize(height); hypre_CSRMatrixExtractDiagonal(mat, diag.Write(), 0);

The textbook exact diagonal read. The destination `diag` is sized to
`height`, then the stored `(i,i)` entries are extracted verbatim from the
CSR structure. This is the **exact** representation: the assembled diagonal
equals the true mathematical diagonal (modulo IEEE round-off of the stored
values, which were themselves assembled — no additional approximation at
extraction time).

Justification kind: **structural** — re-bind the L1 output value into the
L0 destination buffer; the operator-representation axis collapse (sparse
CSR) is absorbed at L1. The sizing (`SetSize(height)`) is an L0 buffer
mechanic the L1 form drops.

Citations:
- `palace/linalg/operator.hpp:21` — `using Operator = mfem::Operator;` —
  the real-operator alias inheriting the abstract
  `mfem::Operator::AssembleDiagonal(Vector &diag) const` virtual from MFEM
  (resolves into vendored MFEM; see Open questions / OQ).
- `palace/linalg/hypre.hpp:70` — `HypreCSRMatrix::AssembleDiagonal` override
  declaration.
- `palace/linalg/hypre.cpp:85-89` — the body:
  `diag.SetSize(height); hypre_CSRMatrixExtractDiagonal(mat, diag.Write(), 0);`
  — the exact sparse-CSR read; witnesses the destination sizing.

### Sub-pattern B — matrix-free element-local accumulation (libCEED)

    A.AssembleDiagonal(diag);              // real path: fem::libceed::Operator::AssembleDiagonal
    // body: MFEM_VERIFY(diag.Size() == height, ...);  // square precondition
    //       diag = 0.0;                                // zero-init
    //       (OpenMP) CeedOperatorLinearAssembleAddDiagonal(op[id], v[id], ...);

The matrix-free path. The destination `diag` is checked against the square
size, zero-initialised, then accumulated element-by-element via libCEED's
`CeedOperatorLinearAssembleAddDiagonal` under an OpenMP-parallel region. The
zero-init + element accumulation is the assembly mechanic; for an
exactly-assembled operator the accumulated result equals the true diagonal,
but for the **high-order Nedelec (H(curl)) representation in 3D the
accumulation is approximate** (see the load-bearing non-law below).

Justification kind: **structural** — re-bind the L1 output value into the L0
destination buffer; the matrix-free representation is absorbed at L1. The
`diag = 0.0` zero-init and the element-local accumulation order are L0
mechanics; for the exact case they are transparent, but the accumulation
order is the **source of the load-bearing approximation** for the
high-order-Nedelec case (the one case where the accumulation order changes
the *value*, not just the bit pattern).

Citations:
- `palace/fem/libceed/operator.hpp:56` — libCEED operator
  `AssembleDiagonal` override declaration.
- `palace/fem/libceed/operator.cpp:116-143` — the body:
  `MFEM_VERIFY(diag.Size() == height, ...)` (square precondition, line 120),
  `diag = 0.0` (line 121), and the OpenMP-parallel
  `CeedOperatorLinearAssembleAddDiagonal(op[id], v[id], ...)` (line 139) —
  the matrix-free element-local accumulating assembly.

### Sub-pattern C — parallel AMR absolute-value-prolongation transpose (`ParOperator`)

    A.AssembleDiagonal(diag);              // real path: ParOperator::AssembleDiagonal
    // if (RAP) { RAP->AssembleDiagonal(diag); return; }              // delegate to assembled RAP
    // MFEM_VERIFY(&trial_fespace == &test_fespace, "... square ...");  // square precondition
    // A->AssembleDiagonal(lx);                                        // local diagonal
    // hP->AbsMultTranspose(1.0, lx, 0.0, diag);                       // |P|ᵀ dₗ
    // // then Dirichlet DiagonalPolicy on dbc_tdof_list

The parallel wrapper path. When an explicit RAP product is available it
delegates (sub-pattern A or B on the inner operator); otherwise, on an AMR
mesh, it assembles a **convergent** diagonal as `|P|ᵀ dₗ`, where `|P|` is
the entry-wise-absolute conforming prolongation operator and `dₗ` is the
local-vector diagonal. The absolute value is taken on the *prolongation*
(to keep the assembled diagonal convergent on a non-conforming mesh), not
on the diagonal entries — the output retains its sign (this is the
`abs-vs-signed` non-axis from the L1 entry). A Dirichlet-boundary
`DiagonalPolicy` post-step then sets BC true-dofs to `1.0` (`DIAG_ONE`) or
`0.0` (`DIAG_ZERO`).

Justification kind: **structural** — re-bind the L1 output value into the L0
destination buffer; the parallel-wrapped representation is absorbed at L1.
The `|P|ᵀ dₗ` absolute-value-prolongation assembly and the
`DiagonalPolicy` BC post-step are L0 mechanics. The BC policy is **not** a
parameter of the bare `assemble_diagonal` operator: at L1 the operator `A`
*is* the BC-eliminated operator, so its diagonal already reflects the
policy; the policy step is reintroduced here, in the lowering, not in the L1
signature.

Citations:
- `palace/linalg/rap.hpp:112` — `ParOperator::AssembleDiagonal` override
  declaration.
- `palace/linalg/rap.cpp:154-193` — the body: the RAP-delegate fast path
  (lines 157-161), the convergent-diagonal comment (lines 163-164), the
  square precondition `MFEM_VERIFY(&trial_fespace == &test_fespace, "...
  square ParOperator!")` (lines 165-166), the local-diagonal assembly
  `A->AssembleDiagonal(lx)` (line 168), the absolute-value-prolongation
  transpose `hP->AbsMultTranspose(1.0, lx, 0.0, diag)` (line 174), and the
  Dirichlet `DiagonalPolicy` BC post-step `DIAG_ONE` / `DIAG_ZERO`
  (lines 180-191).

### Sub-pattern D — complex real/imag split (`ComplexWrapperOperator`, `ComplexParOperator`)

    A.AssembleDiagonal(diag);              // complex path: ComplexVector &diag
    // body: diag = 0.0;
    //       if (Ar) Ar->AssembleDiagonal(diag.Real());
    //       if (Ai) Ai->AssembleDiagonal(diag.Imag());

The complex path. The destination `ComplexVector diag` is zero-initialised,
then the real and imaginary diagonals are assembled **independently** into
`diag.Real()` and `diag.Imag()` by delegating to the real-path
`AssembleDiagonal` (sub-pattern A / B / C) of each part. This witnesses the
L1 entry's law 2 (linearity over operator sum) and law 6 (complex real/imag
split): `diag(Ar + i·Ai) = diag(Ar) + i·diag(Ai)`.

Justification kind: **algebraic** — the rewrite is recognised by
`A.AssembleDiagonal(diag)` on a complex operator ⇒
`diag = assemble_diagonal(Ar) + i·assemble_diagonal(Ai)`, the complex
real/imag-split linearity of the L1 entry. The `diag = 0.0` zero-init and
the two delegated real-path assemblies are L0 mechanics; the two parts
reduce to sub-patterns A/B/C on `Ar`, `Ai`.

Citations:
- `palace/linalg/operator.hpp:50-51` — `// Diagonal assembly.` /
  `virtual void AssembleDiagonal(ComplexVector &diag) const;` — the abstract
  complex-operator diagonal-assembly declaration.
- `palace/linalg/operator.hpp:97` — `ComplexWrapperOperator::AssembleDiagonal`
  override declaration.
- `palace/linalg/operator.cpp:85-96` — `ComplexWrapperOperator::AssembleDiagonal`:
  `diag = 0.0` (line 87); `if (Ar) Ar->AssembleDiagonal(diag.Real())`
  (lines 88-91); `if (Ai) Ai->AssembleDiagonal(diag.Imag())`
  (lines 92-95) — the complex real/imag split + zero-init.
- `palace/linalg/rap.hpp:206` — `ComplexParOperator::AssembleDiagonal`
  override declaration.
- `palace/linalg/rap.cpp:467-479` — `ComplexParOperator::AssembleDiagonal`:
  `diag = 0.0` (line 470); real part into `diag.Real()` (lines 471-474);
  imag part into `diag.Imag()` (lines 475-478) — second witness of the
  complex split.

### Sub-pattern E (non-rewrite) — partial-domain abort (base `ComplexOperator`)

    A.AssembleDiagonal(diag);              // base ComplexOperator: MFEM_ABORT
    // body: MFEM_ABORT("Base class ComplexOperator does not implement AssembleDiagonal!");

The base `ComplexOperator::AssembleDiagonal` aborts. This is **not** a
rewrite sub-pattern — it marks the boundary of the L1 operator's *domain*:
`assemble_diagonal`'s L1 domain is the diagonal-capable subclasses (A–D
above), not every `LinearOperator`. An operator that cannot expose a
diagonal is a precondition violation, not a variant; the abort is the L0
realisation of "outside the domain of `assemble_diagonal`".

Justification kind: **obstruction (domain-boundary)** — the abort is
recorded as the L0 partial-domain marker; it does not lower any L1 form. The
L1 entry's "partial-domain (abort)" non-axis is its source.

Citations:
- `palace/linalg/operator.cpp:25-28` — `ComplexOperator::AssembleDiagonal`
  base definition:
  `MFEM_ABORT("Base class ComplexOperator does not implement AssembleDiagonal!")`.

## Consuming chain (downstream context)

The diagonal-preconditioner-apply chain that motivated harvesting the L1
operator and this theme: every consumer follows
`op.AssembleDiagonal(dinv); dinv.Reciprocal();` and then an element-wise
product in its `Mult`. At L1 this is
`dinv = reciprocal(assemble_diagonal(A)); y = dinv ⊙ x`. The `reciprocal`
(`mfem::Vector::Reciprocal`) and the element-wise product are themselves
forthcoming L1-primitive candidates (`reciprocal` / `elementwise_product`
entries — referenced here as plain text, not yet authored; the lowering of
those steps is out of scope for this theme).

Consuming call sites (cross-reference, not part of this rewrite):
- `palace/linalg/jacobi.cpp:79-80` — `JacobiSmoother::SetOperator`:
  `op.AssembleDiagonal(dinv); dinv.Reciprocal();` (after
  `dinv.SetSize(op.Height())` at line 77).
- `palace/linalg/chebyshev.cpp:177-178` — `ChebyshevSmoother::SetOperator`:
  `op.AssembleDiagonal(dinv); dinv.Reciprocal();`.
- `palace/linalg/chebyshev.cpp:240-241` — `ChebyshevSmoother1stKind::SetOperator`:
  the identical setup (second consumer code path).

## Applicability conditions

For all four rewrite sub-patterns (A–D) the rewrite preserves semantics
when:

1. **Operator is square** (`M = N`). A diagonal is only defined where domain
   and codomain index sets coincide. Palace enforces this at the AMR path
   (`MFEM_VERIFY(&trial_fespace == &test_fespace, "... square ParOperator!")`,
   `palace/linalg/rap.cpp:165-166`) and the libCEED path
   (`MFEM_VERIFY(diag.Size() == height, ...)`, `palace/fem/libceed/operator.cpp:120`).
   This is the chief precondition difference from `apply_linop`, which admits
   rectangular `M ≠ N`.

2. **Operator is diagonal-capable** (in `assemble_diagonal`'s L1 domain).
   The base `ComplexOperator::AssembleDiagonal` aborts
   (`palace/linalg/operator.cpp:25-28`); an operator that does not override
   it is a precondition violation (sub-pattern E), not a representable input.

3. **No observer of the prior `diag` value after the call.** `diag` is an
   overwrite destination (sized via `SetSize` for sub-pattern A; zeroed via
   `diag = 0.0` for B, D before accumulation). The prior contents are
   destroyed, not consumed. There is no accumulate-mode variant (contrast
   `apply_linop`'s `AddMult` family): `AssembleDiagonal` always materialises
   the full diagonal.

4. **Element type matches.** Either all real (`Vector`, `Operator`) or all
   complex (`ComplexVector`, `ComplexOperator`). The complex case (sub-pattern
   D) assembles the real and imaginary diagonals separately; the per-element
   diagonal-extraction relationship is otherwise identical to the real case.

5. **Operator `A` is read-only** (the L0 method is `const`). Workspace
   mutation (e.g. the AMR path's local vector `lx` via
   `trial_fespace.GetLVector<Vector>()`) is private to the call and not
   observable from outside; it does not affect the L1 view.

6. **Exact-vs-approximate awareness** (the load-bearing non-law; see below).
   For sub-pattern B with a high-order Nedelec representation in 3D, the
   rewrite preserves the *intended* semantics (an approximate diagonal scaling
   for an inexact preconditioner) but **not** an exact-diagonal equality. A
   downstream consumer that requires the exact diagonal is outside this
   theme's applicability for that representation.

## Load-bearing non-law — matrix-free high-order-Nedelec approximate diagonal

Carried verbatim from the L1 entry as a **load-bearing** numerical property
(per the CLAUDE.md optimization-tricks-vs-base-algebra taxonomy): for a
matrix-free high-order Nedelec (H(curl)) operator in 3D, the assembled
diagonal (sub-pattern B's element-local accumulation) is **approximate** —
face dofs shared across elements make the element-local-summation diagonal
differ from the true assembled diagonal. This changes the diagonal *value*
(not merely its bit pattern), so it is a semantic approximation, not
floating-point reduction-order noise.

It is acceptable *because* the diagonal feeds an inexact preconditioner: a
Jacobi / Chebyshev smoother tolerates an approximate diagonal scaling. The
approximation is **positively anchored**:

- `palace/linalg/jacobi.hpp:15-16` — Palace comment:
  `// Simple Jacobi smoother using the diagonal vector from
  OperType::AssembleDiagonal(), which allows for (approximate) diagonal
  construction for matrix-free operators.` — names the matrix-free
  approximate diagonal at the consumer.
- `palace/linalg/rap.cpp:163-164` — the AMR `|P|ᵀ dₗ` convergent-diagonal
  comment naming the convergent (approximate-but-convergent) assembly.
- `test/unit/test-libceed.cpp:343-376` — the diagonal-assembly test confirms
  `AssembleDiagonal` reproduces `mfem::SparseMatrix::GetDiag` to
  `rtol = 1.0e-12` in general (line 360), but **relaxes the tolerance to
  `rtol = 1.0` exactly for high-order 3D Nedelec non-tensor-basis spaces**
  (the `ND_FECollection` + `GetOrder() > 1` + `!UsesTensorBasis` condition,
  lines 365-371; `rtol = 1.0` at line 371). This is the test-witnessed
  load-bearing approximation; L0-equivalent semantic documentation per
  CLAUDE.md "Tests as semantic supplement".

This caveat is **positively anchored** (a Palace comment that names the
approximation + a test that relaxes its tolerance for it) — it is NOT a
reconstruction from negative anchors — so this theme is `firm`, not
`partly-constructive`.

## Justification kind

- **Sub-pattern A** (sparse-CSR exact read) — `structural`. Re-bind L1 output
  value into L0 destination buffer; sparse representation absorbed at L1.
- **Sub-pattern B** (matrix-free accumulation) — `structural`. Same re-bind;
  matrix-free representation absorbed at L1. The element-local accumulation
  order is the source of the high-order-Nedelec approximation (load-bearing
  non-law).
- **Sub-pattern C** (parallel AMR `|P|ᵀ dₗ`) — `structural`. Same re-bind;
  parallel-wrapped representation absorbed at L1. The abs-prolongation and
  DiagonalPolicy are L0 mechanics.
- **Sub-pattern D** (complex real/imag split) — `algebraic`.
  `A.AssembleDiagonal(diag)` on a complex operator ⇒
  `assemble_diagonal(Ar) + i·assemble_diagonal(Ai)` (L1 laws 2, 6).
- **Sub-pattern E** (abort) — `obstruction (domain-boundary)`. Marks the L0
  partial-domain boundary; lowers no L1 form.

The theme as a whole is `structural` (the operator-to-data materialisation
re-bind) with one algebraic sub-rule (complex split) and one
domain-boundary marker. A `lowering-verifier` audit in a later cycle should
confirm the four rewrite sub-patterns exhaust the diagonal-capable subclasses
in the L0 corpus and that the abs-prolongation / zero-init / element-local
accumulation readings are consistent across the realisations.

## Speculative L1 operators

None.

`assemble_diagonal` is the firm L1 form (cycle-019); the four rewrite
sub-patterns decompose into existing firm L1 vocabulary only (the single
`assemble_diagonal` operator, parameterised by element type; the complex
split reduces to two real-path applications). No rough-in L1 operator is
needed for this theme. The consuming chain references `reciprocal` and
`elementwise_product` (forthcoming L1-primitive candidates) — these are
plain-text forward-references, not speculative operators emitted by this
theme; they belong to the diagonal-preconditioner-apply chain, not to the
`assemble_diagonal` lowering itself.

## Verified-against

L0 evidence ranges (verified by direct read during this cycle via
palace-codemap `read_range`):

- `palace/linalg/operator.hpp:21` — `using Operator = mfem::Operator;`
  (real alias; inherits abstract `AssembleDiagonal` from MFEM).
- `palace/linalg/operator.hpp:50-51` — abstract `ComplexOperator::AssembleDiagonal`
  decl.
- `palace/linalg/operator.hpp:97` — `ComplexWrapperOperator::AssembleDiagonal`
  override decl.
- `palace/linalg/operator.cpp:25-28` — base `ComplexOperator::AssembleDiagonal`
  abort (sub-pattern E).
- `palace/linalg/operator.cpp:85-96` — `ComplexWrapperOperator::AssembleDiagonal`
  (sub-pattern D; `diag = 0.0` at :87, real/imag at :88-95).
- `palace/linalg/hypre.hpp:70` — `HypreCSRMatrix::AssembleDiagonal` decl.
- `palace/linalg/hypre.cpp:85-89` — `HypreCSRMatrix::AssembleDiagonal` body
  (sub-pattern A; exact CSR read).
- `palace/fem/libceed/operator.hpp:56` — libCEED operator
  `AssembleDiagonal` decl.
- `palace/fem/libceed/operator.cpp:116-143` — libCEED
  `AssembleDiagonal` body (sub-pattern B; square verify :120, `diag = 0.0`
  :121, `CeedOperatorLinearAssembleAddDiagonal` :139).
- `palace/linalg/rap.hpp:112` — `ParOperator::AssembleDiagonal` decl.
- `palace/linalg/rap.cpp:154-193` — `ParOperator::AssembleDiagonal` body
  (sub-pattern C; convergent comment :163-164, square verify :165-166,
  `AbsMultTranspose` :174, DiagonalPolicy :180-191).
- `palace/linalg/rap.hpp:206` — `ComplexParOperator::AssembleDiagonal` decl.
- `palace/linalg/rap.cpp:467-479` — `ComplexParOperator::AssembleDiagonal`
  body (sub-pattern D; `diag = 0.0` :470, real/imag :471-478).
- `palace/linalg/jacobi.cpp:79-80` — consuming chain
  `op.AssembleDiagonal(dinv); dinv.Reciprocal();`.
- `palace/linalg/jacobi.hpp:15-16` — approximate-matrix-free non-law comment.
- `palace/linalg/chebyshev.cpp:177-178` — `ChebyshevSmoother` consuming chain.
- `palace/linalg/chebyshev.cpp:240-241` — `ChebyshevSmoother1stKind` consuming
  chain.
- `test/unit/test-libceed.cpp:343-376` — diagonal-assembly test;
  `rtol = 1.0` high-order-Nedelec relaxation (condition :365-369, assignment :371).

L1 anchor:

- `book/src/L1/assemble-diagonal.md` — the firm L1 operator (cycle-019) that
  all four sub-patterns lower from.

Sibling lowering theme:

- `book/src/L1-L0/apply-linop-mutation-rotation.md` — the operator/data
  divide is stated against it (`apply_linop` is operator-and-vector-to-vector
  in-place mutation; `assemble_diagonal` is operator-to-data in-place
  mutation with no input vector).

Coverage note: this theme cites the **complete** set of concrete
`AssembleDiagonal` realisations in the Palace tree (`HypreCSRMatrix`,
`fem::libceed::Operator`, `ParOperator`, `ComplexParOperator`,
`ComplexWrapperOperator`) plus the base-class abort — diagonal assembly is a
narrower virtual family than `Mult` (not every operator overrides it; only
the diagonal-capable subclasses do), so the corpus is small and the cited
set is exhaustive rather than illustrative. A `lowering-verifier` audit
should confirm no further override exists.

## Status

`firm` — the operator-to-data materialisation rewrite is recognised and
exhaustively cited across all four representation sub-patterns (sparse-CSR
exact / matrix-free accumulation / parallel AMR abs-prolongation / complex
split) + the partial-domain abort + the two consuming smoother families. The
structural decomposition matches the firm L1 `assemble-diagonal` entry; the
L0 evidence ranges have been verified by direct read this cycle. The one
caveat — the matrix-free high-order-Nedelec approximate diagonal — is a
**positively-anchored load-bearing non-law** (a Palace comment that names it
+ a test that relaxes its tolerance for it), carried verbatim from the L1
entry, NOT a reconstruction from negative anchors: this theme is therefore
`firm`, not `partly-constructive`. The only residual is the upstream-MFEM
resolution of the real-path `mfem::Operator::AssembleDiagonal` virtual
(logged as an OQ), which does not affect the rewrite recognition (the alias
is the Palace L0 anchor).

verified_against:
  - citation: palace/linalg/operator.hpp:21
    verdict: supports
    audited_at: 2026-05-29T03:50:30Z
    note: using Operator = mfem::Operator; real-operator alias, inherits abstract AssembleDiagonal from MFEM.
  - citation: palace/linalg/operator.hpp:50-51
    verdict: supports
    audited_at: 2026-05-29T03:50:30Z
    note: "// Diagonal assembly." + virtual void AssembleDiagonal(ComplexVector &diag) const; abstract complex decl.
  - citation: palace/linalg/operator.cpp:25-28
    verdict: supports
    audited_at: 2026-05-29T03:50:30Z
    note: ComplexOperator::AssembleDiagonal base MFEM_ABORT; partial-domain boundary (sub-pattern E).
  - citation: palace/linalg/operator.cpp:85-96
    verdict: supports
    audited_at: 2026-05-29T03:50:30Z
    note: ComplexWrapperOperator::AssembleDiagonal; diag = 0.0 at :87, Ar->AssembleDiagonal(diag.Real()) :88-91, Ai->AssembleDiagonal(diag.Imag()) :92-95 (sub-pattern D; laws 2/6).
  - citation: palace/linalg/hypre.cpp:85-89
    verdict: supports
    audited_at: 2026-05-29T03:50:30Z
    note: HypreCSRMatrix::AssembleDiagonal; diag.SetSize(height) :87, hypre_CSRMatrixExtractDiagonal(mat, diag.Write(), 0) :88 (sub-pattern A; exact sparse read).
  - citation: palace/fem/libceed/operator.cpp:116-143
    verdict: supports
    audited_at: 2026-05-29T03:50:30Z
    note: fem::libceed::Operator::AssembleDiagonal; MFEM_VERIFY(diag.Size() == height) :120, diag = 0.0 :121, CeedOperatorLinearAssembleAddDiagonal :139 (sub-pattern B; matrix-free accumulation).
  - citation: palace/linalg/rap.cpp:154-193
    verdict: supports
    audited_at: 2026-05-29T03:50:30Z
    note: ParOperator::AssembleDiagonal; RAP-delegate :157-161, convergent comment :163-164, MFEM_VERIFY square :165-166, A->AssembleDiagonal(lx) :168, hP->AbsMultTranspose(1.0, lx, 0.0, diag) :174, DiagonalPolicy DIAG_ONE/DIAG_ZERO :180-191 (sub-pattern C).
  - citation: palace/linalg/rap.cpp:467-479
    verdict: supports
    audited_at: 2026-05-29T03:50:30Z
    note: ComplexParOperator::AssembleDiagonal; diag = 0.0 :470, RAPr->AssembleDiagonal(diag.Real()) :471-474, RAPi->AssembleDiagonal(diag.Imag()) :475-478 (sub-pattern D; second witness).
  - citation: palace/linalg/jacobi.cpp:79-80
    verdict: supports
    audited_at: 2026-05-29T03:50:30Z
    note: JacobiSmoother::SetOperator; op.AssembleDiagonal(dinv) :79, dinv.Reciprocal() :80 (consuming chain).
  - citation: palace/linalg/jacobi.hpp:15-16
    verdict: supports
    audited_at: 2026-05-29T03:50:30Z
    note: comment naming (approximate) diagonal construction for matrix-free operators (load-bearing non-law positive anchor).
  - citation: palace/linalg/chebyshev.cpp:177-178
    verdict: supports
    audited_at: 2026-05-29T03:50:30Z
    note: ChebyshevSmoother::SetOperator; op.AssembleDiagonal(dinv) :177, dinv.Reciprocal() :178.
  - citation: palace/linalg/chebyshev.cpp:240-241
    verdict: supports
    audited_at: 2026-05-29T03:50:30Z
    note: ChebyshevSmoother1stKind::SetOperator; identical op.AssembleDiagonal(dinv) :240, dinv.Reciprocal() :241.
  - citation: test/unit/test-libceed.cpp:343-376
    verdict: supports
    audited_at: 2026-05-29T03:50:30Z
    note: diagonal-assembly test; mat_ref->GetDiag/op_test->AssembleDiagonal compare; rtol=1.0e-12 general (:360), rtol=1.0 for high-order 3D Nedelec non-tensor-basis (condition :365-369, assignment :371). Test-witnessed load-bearing approximation.
```

```edit:book/src/L1-L0/index.md
[append one row to the Theme-list table, after the nrm2-mutation-rotation row (line 27):]

| [assemble-diagonal-mutation-rotation](./assemble-diagonal-mutation-rotation.md) | `L1/assemble-diagonal` (firm) | `palace/linalg/operator.{hpp,cpp}`, `hypre.{hpp,cpp}`, `rap.{hpp,cpp}`, `fem/libceed/operator.{hpp,cpp}` | firm *(structural; 4 representation sub-patterns + abort; load-bearing approximate-matrix-free non-law, positively anchored)* |
```

```edit:book/src/SUMMARY.md
[add chapter entry under the L1 > L0 Part, after the nrm2-mutation-rotation line (line 83):]

- [assemble-diagonal-mutation-rotation](./L1-L0/assemble-diagonal-mutation-rotation.md)
```

## Speculative operators proposed

None. The theme decomposes entirely into existing firm L1 vocabulary (the
single `assemble_diagonal` operator, parameterised by element type; the
complex sub-pattern reduces to two real-path applications). The consuming
chain's `reciprocal` / `elementwise_product` are plain-text forward-references
to forthcoming L1 primitives — they belong to the diagonal-preconditioner-apply
chain, NOT to this `assemble_diagonal` lowering, and are not emitted as
speculative operators by this theme. (Harvester picks them up when the
diagonal-preconditioner-apply L1 operators are localized.)

## Supporting evidence

All ranges below were verified by direct `read_range` against
`reference/palace/` during this dispatch:

- `palace/linalg/operator.hpp:21` — `using Operator = mfem::Operator;` (real alias).
- `palace/linalg/operator.hpp:50-51` — abstract complex `AssembleDiagonal` decl.
- `palace/linalg/operator.hpp:97` — `ComplexWrapperOperator::AssembleDiagonal` decl.
- `palace/linalg/operator.cpp:25-28` — base abort (sub-pattern E).
- `palace/linalg/operator.cpp:85-96` — `ComplexWrapperOperator::AssembleDiagonal` (sub-pattern D).
- `palace/linalg/hypre.hpp:70` — `HypreCSRMatrix::AssembleDiagonal` decl.
- `palace/linalg/hypre.cpp:85-89` — exact CSR read (sub-pattern A).
- `palace/fem/libceed/operator.hpp:56` — libCEED `AssembleDiagonal` decl.
- `palace/fem/libceed/operator.cpp:116-143` — matrix-free accumulation (sub-pattern B; square :120, zero-init :121, CeedOperatorLinearAssembleAddDiagonal :139).
- `palace/linalg/rap.hpp:112` / `palace/linalg/rap.hpp:206` — Par / ComplexPar decls.
- `palace/linalg/rap.cpp:154-193` — AMR `|P|ᵀ dₗ` path (sub-pattern C).
- `palace/linalg/rap.cpp:467-479` — complex parallel split (sub-pattern D).
- `palace/linalg/jacobi.cpp:79-80` + `palace/linalg/jacobi.hpp:15-16` — consumer + non-law comment.
- `palace/linalg/chebyshev.cpp:177-178` + `palace/linalg/chebyshev.cpp:240-241` — Chebyshev consumers.
- `test/unit/test-libceed.cpp:343-376` — test (rtol relaxation: condition :365-369, assignment :371).

## Open questions

- **OQ (upstream-MFEM): real-path `AssembleDiagonal` resolves into vendored
  MFEM.** The real-operator path's `AssembleDiagonal(Vector &diag) const` is
  inherited from `mfem::Operator` via the alias `using Operator =
  mfem::Operator;` (`palace/linalg/operator.hpp:21`). For the abstract real
  base, the diagonal-extraction body lives in MFEM (`mfem::Operator` /
  `mfem::SparseMatrix::GetDiag` etc.), not in the Palace tree. Per CLAUDE.md
  scope ("Specialized agents cite Palace source, not vendored upstream"), this
  theme cites only the Palace alias + the Palace concrete overrides
  (`HypreCSRMatrix`, libCEED, `ParOperator`); the abstract real-base MFEM
  behaviour is logged here as an upstream dependency. This OQ shares the same
  shape as the `apply_linop` real-base-Mult upstream-MFEM dependency. Suggest
  appending to `scaffolding/open-questions.md` (integrator-per-report) as a
  cross-reference to the existing `apply_linop` MFEM-dependency OQ rather than
  a fresh entry, if one exists.

- **Forward-references stay plain-text.** The consuming-chain `reciprocal` and
  `elementwise_product` L1 primitives are not yet authored; they are referenced
  as plain text in the theme (no live link), per the
  `rough-in-rows-must-be-plain-text-when-anchor-missing` convention. They are
  not part of this theme's rewrite; no dep-map row is emitted for them here.

- **Lowering-verifier follow-up.** A later `lowering-verifier` audit should
  confirm (a) the four rewrite sub-patterns exhaust the diagonal-capable
  subclasses in the L0 corpus (the cited set is believed exhaustive — diagonal
  assembly is a narrow virtual family — but this was not exhaustively
  cross-checked against every operator subclass this dispatch); (b) the
  abs-prolongation / zero-init / element-local-accumulation readings are
  consistent across the realisations; (c) whether the `RAP`-delegate fast path
  in `ParOperator::AssembleDiagonal` (lines 157-161) warrants its own
  sub-pattern note or is adequately covered as "delegates to A/B".

- **Caveat lifetime.** The approximate-matrix-free non-law is positively
  anchored and load-bearing; it should be preserved through any future L1>L2
  lift of `assemble_diagonal` (the L2 fusion-rotation must not erase the
  approximation, since it is part of the algorithm for the matrix-free
  high-order-Nedelec case). Noted for the eventual L2 abstractor.
