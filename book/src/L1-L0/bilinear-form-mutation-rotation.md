# bilinear-form-mutation-rotation

The mutation rotation for the operator-weighted (bilinear_form) inner product. Lowers the pure L1
form `bilinear_form(x, M, y) = xᴴ M y` ([`L1/bilinear_form`](../L1/bilinear_form.md)) into Palace's L0 `linalg::Dot(comm, x, A, y)` three-step composition
`ComplexVector Ax(A.Height()); A.Mult(x, Ax); return Dot(comm, Ax, y)`
(`palace/linalg/operator.cpp:621-639`). It is the **off-diagonal sibling** of
[`matrix-weighted-norm-mutation-rotation`](./matrix-weighted-norm-mutation-rotation.md): where the
weighted norm lowers the diagonal case `y = x` plus an outer `√` and an SPD precondition, this
theme lowers the general case `y ≠ x` with no precondition on `M`'s symmetry. The theme **reuses
two sibling sub-themes** rather than restating them: the leading `A.Mult(x, Ax)` is
[`apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md) Sub-pattern A; the inner
`Dot(comm, Ax, y)` is [`dot-mutation-rotation`](./dot-mutation-rotation.md) Sub-pattern A (the
`Mpi::GlobalSum ∘ LocalDot` two-step). What this theme adds is the bilinear_form machinery: the
**internally-allocated `Ax` workspace** (Category-4 synthetic — distinct from the caller-supplied
`Bx` of the sibling theme), the **element-type-of-`M` overload split** (real `A : Operator` with a
real/imaginary lane split on complex `x` vs complex `A : ComplexOperator` with a single direct
apply), and the **L1/L0 conjugation-handedness reconciliation** (the L1 convention names `x` as
the conjugated argument matching [`dot`](../L1/dot.md); Palace's L0 `Dot` conjugates its
second argument, so the L0 call shape `Dot(comm, Ax, y) = yᴴ A x` is the natural lowering of the
L1 form `xᴴ M y` with `x ↔ y` argument-order swap).

## Slug

`bilinear-form-mutation-rotation`

## L1 form (LHS)

The pure-functional matrix-weighted bilinear_form inner product consumes three read-only inputs
and produces a fresh scalar; nothing is mutated, and there is no workspace in the signature. The
LHS shape (the L1 operator; see [`L1/bilinear_form`](../L1/bilinear_form.md)):

    alpha = bilinear_form(x, M, y)    -- alpha = xᴴ M y, scalar
                                      -- (complex x, real M, complex y    -> complex)
                                      -- (complex x, complex M, complex y -> complex)
                                      -- (the real x / real M / real y case is not
                                      --  surfaced by Palace's L0 overload set;
                                      --  see L1/bilinear_form §Variant axes)

The L1 algebraic identity that anchors the lowering is
`bilinear_form(x, M, y) = dot(x, apply_linop(M, y))` — the matrix-weighted form unfolds into one
`apply_linop` + one `dot` (per [`L1/bilinear_form`](../L1/bilinear_form.md) §"Composition into
`apply_linop` + `dot`"). At L1 the operator is a single semantic step (the closed-form `xᴴ M y`);
the three-step unfolding is what this theme makes explicit. The element-type axis of `M`
(`real`/`complex`) is collapsed at L1 — see *Variant axes*. The MPI collective is **not** in the
L1 signature; the L1 reduction is one semantic step. The workspace `Ax` is **not** in the L1
signature; the operator returns a fresh scalar with no buffer parameter.

There is **no SPD precondition on `M`** at L1 (per [`L1/bilinear_form`](../L1/bilinear_form.md)
§Applicability conditions); the operator is well-defined for any linear `M`, including
non-Hermitian and indefinite weights. This is the **structural distinguisher** from
`matrix_weighted_norm`: the bilinear form has no positivity / Hermiticity / squareness gate, while
the weighted norm requires SPD (and the consumer-pattern outer `√` would otherwise be undefined).

## L0 form (RHS)

The L1 bilinear form lowers into the pair of free-function overloads `linalg::Dot(comm, x, A, y)`
declared at `palace/linalg/operator.hpp:386-394` and defined at
`palace/linalg/operator.cpp:621-639`. Both overloads compute the **same three-step composition**
(internal workspace allocation, leading operator-apply, inner reduction-and-return); they differ
only in the element-type plumbing of the leading apply.

### Sub-pattern A — real-operator overload (real `A`, complex `x`, complex `y`)

    // palace/linalg/operator.hpp:386-389  (decl + comment)
    // Compute the bilinear form inner product yᴴ A x for a real operator A and complex
    // vectors. Allocates workspace internally.
    std::complex<double> Dot(MPI_Comm comm, const ComplexVector &x, const Operator &A,
                             const ComplexVector &y);

    // palace/linalg/operator.cpp:621-629  (definition)
    std::complex<double> Dot(MPI_Comm comm, const ComplexVector &x, const Operator &A,
                             const ComplexVector &y)
    {
      ComplexVector Ax(A.Height());                        // :624  — workspace alloc (step 0)
      Ax.UseDevice(true);                                  // :625  — device-placement
      A.Mult(x.Real(), Ax.Real());                         // :626  — step 1a (real lane)
      A.Mult(x.Imag(), Ax.Imag());                         // :627  — step 1b (imag lane)
      return Dot(comm, Ax, y);                             // :628  — step 2 + return
    }

The three steps the L1 closed form hides, evaluated in order:

0. **`ComplexVector Ax(A.Height())`** (`:624`) — internally-allocated workspace, lifetime
   strictly scoped to the call. `Ax` is a `ComplexVector` of length `A.Height()`, holding the
   intermediate `A · x`. The `Ax.UseDevice(true)` line (`:625`) places the buffer on device when
   GPU is configured; this is a transparent infrastructure step (no algebraic content). This is
   the Category-4 ("synthetic workspace") instance of
   [`mutable-workspace-pattern`](../L0/mutable-workspace-pattern.md) per the L0 chapter
   classification — **distinct from the caller-supplied `Bx` of the sibling
   [`matrix-weighted-norm-mutation-rotation`](./matrix-weighted-norm-mutation-rotation.md)**. The
   choice of internal-vs-caller-supplied allocation is the only *structural* (not just
   compositional) difference between the two themes; see §"The internal workspace `Ax`" below.
1. **`A.Mult(x.Real(), Ax.Real()); A.Mult(x.Imag(), Ax.Imag())`** (`:626-627`) — the leading
   operator-apply, **split** because `A : Operator` is real-valued by signature while `x` is a
   `ComplexVector`. Palace applies the real `A` componentwise to the real and imaginary lanes of
   `x`, writing into the real and imaginary lanes of `Ax`. This is exactly
   [`apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md) Sub-pattern A
   (`A.Mult(x, y)`, destination-buffer pattern) applied **twice** (once per lane) —
   equivalently the `complex-from-real-lift` (`apply_linop` §Applicability condition 3) of a real
   `A` to a complex apply. At L1 this split is absorbed by `apply_linop`'s element-type variant
   axis: the L1 form is just `apply_linop(M, x)` with the element-type axis collapsed. **This is
   the same lane-split plumbing as Sub-pattern B of
   [`matrix-weighted-norm-mutation-rotation`](./matrix-weighted-norm-mutation-rotation.md)** — the
   two themes share the real-`B`/`A`-on-complex-`x` machinery exactly.
2. **`return Dot(comm, Ax, y)`** (`:628`) — the inner reduction. This is
   [`dot-mutation-rotation`](./dot-mutation-rotation.md) Sub-pattern A (free-function
   `linalg::Dot(comm, a, b)` = the `Mpi::GlobalSum ∘ LocalDot` two-step). This theme **inherits**
   that sub-theme — the local-then-collective two-step, the MPI collective (single-rank no-op,
   structurally present per CLAUDE.md "Scope"), and the reduction-tree non-associativity are all
   recorded there, not restated. The result is returned directly (no separate result buffer).

**Conjugation handedness — the core L1>L0 reconciliation.** Palace's `linalg::Dot(comm, Ax, y)`
computes `yᴴ Ax` (arg-2-conjugated convention — per
[`dot-mutation-rotation`](./dot-mutation-rotation.md) §"The conjugation asymmetry" and
[`L1/dot`](../L1/dot.md)`:43, 104-105`). Composing with step 1 (`Ax = A·x`):

    L0 result = Dot(comm, Ax, y) = yᴴ · Ax = yᴴ · (A·x) = yᴴ A x

This matches the L0 source comment at `palace/linalg/operator.hpp:386` (`yᴴ A x`) exactly. The L1
form is `bilinear_form(x, M, y) = xᴴ M y` (arg-1-conjugated, matching [`L1/dot`](../L1/dot.md)'s
L1 convention). The L1>L0 reconciliation is the **argument-position swap**:

    L1: bilinear_form(x, M, y) = xᴴ M y     -- conjugated arg named first
    L0: Dot(comm, x, A, y)     = yᴴ A x     -- conjugated arg named second

The two are the same closed-form value with `x ↔ y` swapped in the call. The L0 surface's choice
of which vector to name `x` and which to name `y` is the *call-order* convention; the L1 choice to
name the conjugated argument first is the *signature* convention. The reconciliation is mechanical
(an argument-position swap at the L1>L0 boundary) and **not** an algebraic rewrite — both forms
compute the same `yᴴ A x` value; only the parameter names differ. This is parallel to the
arg-1-vs-arg-2 conjugation reconciliation already documented in
[`dot-mutation-rotation`](./dot-mutation-rotation.md) for the unweighted case; the weighted form
inherits the convention from `dot` rather than introducing a new one.

Justification kind: **structural** — the syntactic expansion of one closed-form L1 step into the
L0 three-step (internal alloc → lane-split apply → inner Dot return); the destination for the
result is the return register, the destination for the intermediate `A·x` is the internal `Ax`.

Citations:

- `palace/linalg/operator.hpp:386-389` — real-`A` overload declaration + comment
  `// Compute the bilinear form inner product yᴴ A x for a real operator A and complex vectors.
   Allocates workspace internally.` (`:386-387`).
- `palace/linalg/operator.cpp:621-629` — real-`A` overload body: `ComplexVector Ax(A.Height())`
  (`:624`), `Ax.UseDevice(true)` (`:625`), `A.Mult(x.Real(), Ax.Real())` (`:626`),
  `A.Mult(x.Imag(), Ax.Imag())` (`:627`), `return Dot(comm, Ax, y)` (`:628`).
- [`apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md) Sub-pattern A — the
  inherited `A.Mult(x, y)` lowering applied twice for the real-on-complex lane split.
- [`dot-mutation-rotation`](./dot-mutation-rotation.md) Sub-pattern A — the inherited
  `Dot(comm, Ax, y)` lowering (the `Mpi::GlobalSum ∘ LocalDot` two-step + the arg-2-conjugated
  convention).

### Sub-pattern B — complex-operator overload (complex `A`, complex `x`, complex `y`)

    // palace/linalg/operator.hpp:391-394  (decl + comment)
    // Compute the bilinear form inner product yᴴ A x for a complex operator A and complex
    // vectors. Allocates workspace internally.
    std::complex<double> Dot(MPI_Comm comm, const ComplexVector &x, const ComplexOperator &A,
                             const ComplexVector &y);

    // palace/linalg/operator.cpp:631-638  (definition)
    std::complex<double> Dot(MPI_Comm comm, const ComplexVector &x, const ComplexOperator &A,
                             const ComplexVector &y)
    {
      ComplexVector Ax(A.Height());                        // :634  — workspace alloc (step 0)
      Ax.UseDevice(true);                                  // :635  — device-placement
      A.Mult(x, Ax);                                       // :636  — step 1 (direct complex apply)
      return Dot(comm, Ax, y);                             // :637  — step 2 + return
    }

Structurally identical to Sub-pattern A, with **one element-type difference**:

- **Step 1 is a single direct apply** (`:636`). The L0 `A : ComplexOperator` is complex-valued by
  signature, so `A.Mult(x, Ax)` applies it once to the whole complex vector — no lane split. This
  is still [`apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md) Sub-pattern A,
  applied once. At L1 this collapses with Sub-pattern A's two-call form into the same
  `apply_linop(M, x)` — the element-type-of-`M` axis is absorbed by `apply_linop`'s representation
  variant axis (per `apply_linop` §"Variant axes").

The workspace allocation (`:634`), the device placement (`:635`), the inner-`Dot` return
(`:637`), and the conjugation reconciliation (`Dot(comm, Ax, y) = yᴴ A x`, matching the L0
comment at `palace/linalg/operator.hpp:391`) are identical to Sub-pattern A. At L1 Sub-patterns A
and B **collapse to one operator** — both produce the same closed-form `xᴴ M y`, with the
element-type-of-`M` axis variant-absorbed into `apply_linop`.

Justification kind: **structural** (the three-step expansion + the element-type collapse onto
`apply_linop`'s representation axis).

Citations:

- `palace/linalg/operator.hpp:391-394` — complex-`A` overload declaration + comment
  `// Compute the bilinear form inner product yᴴ A x for a complex operator A and complex vectors.
   Allocates workspace internally.` (`:391-392`).
- `palace/linalg/operator.cpp:631-638` — complex-`A` overload body: `ComplexVector Ax(A.Height())`
  (`:634`), `Ax.UseDevice(true)` (`:635`), `A.Mult(x, Ax)` (`:636`), `return Dot(comm, Ax, y)`
  (`:637`).

### Sub-pattern C — call-sites: Poynting-power + boundary-cross-coupling (Hermitian-vs-non-Hermitian witnesses)

The two surfaced Palace call-sites for `linalg::Dot(comm, x, A, y)` both live in
`palace/models/boundarymodeoperator.cpp::ComputePoyntingPower` and span both M-symmetry-property
witnesses (per [`L1/bilinear_form`](../L1/bilinear_form.md) §"Variant axes"):

    // palace/models/boundarymodeoperator.cpp:85  — Hermitian-A witness
    std::complex<double> P = 0.5 * std::conj(kn) / omega * linalg::Dot(comm, et, *Bttr, et);

    // palace/models/boundarymodeoperator.cpp:90  — non-Hermitian-A witness
    P += std::complex<double>(0.0, 1.0) / (2.0 * omega) * linalg::Dot(comm, en, Atn, et);

The line `:85` is the **diagonal Hermitian-`A` case** `bilinear_form(et, Bttr, et) = etᴴ Bttr et`
— a real-valued energy-norm-squared (`Bttr` is a real symmetric MFEM `HypreParMatrix`; the form
hits law 8 of [`L1/bilinear_form`](../L1/bilinear_form.md) §"Algebraic laws"). This site is
**structurally** the same as a `matrix_weighted_norm` callsite (it computes `√(etᴴ Bttr et)`'s
square), but it is **call-coded** through the bilinear_form overload (not through `Norml2`),
because the caller (`ComputePoyntingPower`) wants the unrooted bilinear_form value to combine with
a `std::conj(kn) / omega` complex prefactor.

The line `:90` is the **off-diagonal non-Hermitian-`A` case**
`bilinear_form(en, Atn, et) = enᴴ Atn et` with `Atn = ComplexWrapperOperator(Atnr, Atni)` a
complex wrapper around a **non-symmetric** MFEM `HypreParMatrix`. This site is the direct witness
that law 7 (Hermitian symmetry — see [`L1/bilinear_form`](../L1/bilinear_form.md) §"Algebraic
laws") **does not** hold here: `linalg::Dot(comm, en, Atn, et) ≠ linalg::Dot(comm, et, Atn, en)`
in general. This is the structural reason a separate L1 operator
`bilinear_form` exists distinct from `matrix_weighted_norm` — the off-diagonal non-Hermitian case
is admitted.

Both callsites use the **complex-`A` overload** (Sub-pattern B): `Bttr` is wrapped to
`ComplexOperator` (`*Bttr` dereferences a `unique_ptr<ComplexOperator>`); `Atn` is constructed
inline as `ComplexWrapperOperator`. The real-`A` overload (Sub-pattern A) has no current
in-tree caller surfaced by the L1 entry — this is the **variant-axis-coverage gap** that gates
the L1 entry's `rough-in (test-coverage-bounded)` status; recorded here as a faithful reading of
the surface, not closed by this theme.

A second informational callsite is `palace/linalg/nleps.cpp:675` —
`linalg::Dot(GetComm(), w, w0)` in the Newton-denominator expression — but this is the
**unweighted** two-argument `linalg::Dot` (the `dot` lowering, not the bilinear_form lowering).
The L1 entry notes it as a witness that callers sometimes inline the L1>L0 unfolding manually
(computing `xᴴ M y` as `dot(x, apply_linop(M, y))` rather than calling the matrix-weighted
overload). This is **not** a Sub-pattern A or B callsite for this theme — it is a peer datum
confirming the L1>L0 unfolding identity.

Justification kind: **structural** — pure delegation to A/B at the call boundary, with witnesses
for both M-symmetry-property values (Hermitian / non-Hermitian).

Citations:

- `palace/models/boundarymodeoperator.cpp:75-93` — `BoundaryModeOperator::ComputePoyntingPower`
  function body. Line `:85` is the Hermitian-`A` callsite (`Bttr`); lines `:88-89` construct
  `Atn = ComplexWrapperOperator(Atnr, Atni)` and line `:90` is the non-Hermitian-`A` callsite.
- `palace/linalg/nleps.cpp:672-675` — Newton denominator: `delta_eig = -(linalg::Dot(GetComm(),
   u, w0) + u2_w0) / linalg::Dot(GetComm(), w, w0)` (`:674-675`). Unweighted `linalg::Dot`;
   informational only (does not exercise the bilinear_form overload).

## The internal workspace `Ax`

*The structural distinguisher from the weighted-norm sibling.*

The **single structural distinguisher** between this theme and
[`matrix-weighted-norm-mutation-rotation`](./matrix-weighted-norm-mutation-rotation.md) is the
**workspace-ownership boundary**:

- **`matrix_weighted_norm` (`Norml2`): workspace is CALLER-SUPPLIED.** The L0 signature
  `linalg::Norml2(comm, x, B, Bx)` takes `Bx` as a destination parameter; the eigensolver
  callsites pre-allocate it once outside a loop and reuse across all eigenvectors
  (`palace/linalg/arpack.cpp:470`, `slepc.cpp:505`, `nleps.cpp:146`). The reuse is a transparent
  performance trick (allocation hoisting); algebraically invisible.
- **`bilinear_form` (`Dot(...,A,...)`): workspace is INTERNALLY-ALLOCATED.** The L0 signature
  `linalg::Dot(comm, x, A, y)` does **not** take a workspace parameter; the body allocates
  `ComplexVector Ax(A.Height())` on entry (`palace/linalg/operator.cpp:624` / `:634`) and lets
  it fall out of scope on return. This is Category 4 ("synthetic workspace") of
  [`mutable-workspace-pattern`](../L0/mutable-workspace-pattern.md). **The caller does not see
  `Ax`; it has no name in the L0 signature.** Per-call allocation cost is paid every time.

The choice between caller-supplied and internally-allocated workspace is a Palace-level surface
design decision, not a structural property of the L1 form. At L1 both themes drop the workspace
entirely (`bilinear_form(x, M, y)` has no `Ax` parameter); the L0 surfaces *happen* to differ in
ownership because the dominant consumer of `Norml2` is an inner loop (M-orthonormalisation) where
allocation hoisting matters, while the dominant consumer of `Dot(...,A,...)` is a one-shot
Poynting-power computation where it doesn't. The L1>L0 lowering for this theme:

- **Re-introduces** an `A.Height()`-sized buffer `Ax` for `A·x`.
- **Writes it** via the inherited [`apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md)
  Sub-pattern A rotation (real-`A`: twice, lane-split; complex-`A`: once, direct).
- **Allocates it INTERNALLY** (lifetime scoped to the call), not as a caller-supplied parameter.
- **Reads it** via the inherited [`dot-mutation-rotation`](./dot-mutation-rotation.md)
  Sub-pattern A rotation (with arg-position swap from L1 `xᴴ M y` to L0 `yᴴ A x`).

If a future caller emerges that wants allocation-hoisted reuse (the Poynting-power loop over
boundary modes, perhaps, when expanded to a multi-mode sweep), the natural extension is a
caller-supplied-`Ax` overload — but **this would be a new L0 surface**, not a structural variant
of the L1 form. The L1 form is workspace-free; the workspace ownership is purely an L0 surface
choice. This is the same observation as `matrix-weighted-norm-mutation-rotation` §"The
caller-owned workspace `Bx`": the workspace boundary disappears at L1.

## Element-type-of-`M` overload split

*The variant-absorption boundary.*

The two L0 overloads (Sub-pattern A real-`A`, Sub-pattern B complex-`A`) differ only in:

- **Step 1 plumbing**: real-`A` runs `A.Mult` twice (`x.Real()→Ax.Real()`, `x.Imag()→Ax.Imag()`);
  complex-`A` runs `A.Mult(x, Ax)` once.
- **`A` parameter type**: `const Operator &A` vs `const ComplexOperator &A`.

Everything else — workspace allocation, device placement, inner `Dot` call, conjugation handedness,
return type (`std::complex<double>`), absence of MPI collective in the signature — is identical.

At L1 the element-type-of-`M` axis is **variant-absorbed** by `apply_linop`'s representation
variant axis (per [`L1/apply_linop`](../L1/apply_linop.md) §"Variant axes"); the L1 operator
`bilinear_form(x, M, y)` takes a single `LinearOperator[M, N]` parameter for `M`, and the
element type of `M` is collapsed alongside its representation (sparse / dense / matrix-free /
composition / multigrid). The L1>L0 lowering re-projects the element type onto the two L0
overloads; the dispatch is mechanical (a type check on `M`'s element type at the L1>L0 boundary).

This is the **same** element-type-absorption pattern as Sub-pattern A vs B of
[`matrix-weighted-norm-mutation-rotation`](./matrix-weighted-norm-mutation-rotation.md), with the
**same** `complex-from-real-lift` step ([`apply-linop`](../L1/apply_linop.md) §Applicability
condition 3) for the real-on-complex case.

## Reduction tree

*Load-bearing-numerical recording.*

The bilinear form accumulates non-associativity from **two** inherited sources (per
[`L1/bilinear_form`](../L1/bilinear_form.md) §Semantics):

1. **`apply_linop(M, x)`'s internal kernel** — a sparse-matrix realisation of `M` and a
   matrix-free realisation of the *same* operator produce bit-different `M·x` (the
   `apply-linop-mutation-rotation` representation axis). Pinned per the concrete `M` subclass.
2. **The inner `Dot(comm, Ax, y)` reduction** — the `dot-mutation-rotation` reduction-tree non-law
   (Hypre per-rank kernel + MPI tree-reduce). Pinned per the `dot` lowering.

There is **no outer `√`** here (unlike the weighted-norm sibling), so the bilinear form is one
reduction-non-associativity layer "shallower" than `matrix_weighted_norm`. Bit-identical
reproduction of a specific Palace `Dot(comm, x, A, y)` call requires matching **both** the
`A`-representation kernel tree and the inner `Dot` reduction tree — not merely the value. (Same
discipline as the weighted-norm sibling, minus the deterministic-`sqrt` final step.)

## Conjugation asymmetry

*The L1/L0 reconciliation.*

A core feature of this theme — and the key surface-form distinction from the weighted-norm sibling
— is that **the conjugation handedness is materially visible** in the bilinear_form lowering,
because the bilinear form's result is complex-valued and the imaginary part is not discarded.

In the weighted-norm sibling, the inner `Dot(comm, Bx, x)` result is a `std::complex<double>` but
the `MFEM_ASSERT` confirms its imaginary part is round-off and the return `std::sqrt(dot.real())`
**discards** it. The arg-1-vs-arg-2 conjugation re-order is re-order-invisible because the result
is a real projection. **In the bilinear form, there is no such projection** — the full complex
value of `Dot(comm, Ax, y) = yᴴ A x` is returned to the caller, and the L1 form `xᴴ M y` differs
from `yᴴ M x` by `conj`-and-`Mᴴ` (`xᴴ M y = conj(yᴴ Mᴴ x)`, which equals `conj(yᴴ M x)` only for
Hermitian `M`, and in general requires the `Mᴴ` adjoint).

This is why the L1 form picks the L1 `dot`-convention naming (arg-1 conjugated) — to give the
clean specialisation `bilinear_form(x, I, y) = dot(x, y)` ([`L1/bilinear_form`](../L1/bilinear_form.md)
law 6) — while the L0 form uses the arg-2-conjugated `Dot` convention (matching Palace's
two-argument `linalg::Dot`). The L1>L0 lowering is the argument-position swap:

    L1 form (arg-1 conjugated):   bilinear_form(x, M, y)         = xᴴ M y
    L0 call (arg-2 conjugated):   linalg::Dot(comm, y, M, x)     = xᴴ M y    -- swap x and y in the call!

…or, equivalently with the inherited dot identity `dot(a, b) = conj(dot(b, a))`:

    L1 form:                       bilinear_form(x, M, y)         = xᴴ M y
    L0 call (Palace's choice):     linalg::Dot(comm, x, M, y)     = yᴴ M x   = conj(xᴴ Mᴴ y)

The lowering rule: **when the L1 form is `bilinear_form(x, M, y)`, the L0 surface call is
`linalg::Dot(comm, y, M, x)`** (positions swapped; the *first* L0 argument is the *second* L1
argument). This matches the inherited handling of the same asymmetry in
[`dot-mutation-rotation`](./dot-mutation-rotation.md) §"The conjugation asymmetry" — the
bilinear_form theme inherits the convention reconciliation rather than introducing a new one.

Palace's own callsites are consistent with the L0 convention `Dot(comm, x, A, y) = yᴴ A x`:
`linalg::Dot(comm, et, Bttr, et)` at `boundarymodeoperator.cpp:85` returns `etᴴ Bttr et` (the
diagonal case — the swap is invisible because `x = y`); `linalg::Dot(comm, en, Atn, et)` at `:90`
returns `etᴴ Atn en` (per the L0 comment `yᴴ A x`), and the **caller knows this** (the prefactor
`std::complex<double>(0.0, 1.0) / (2.0 * omega)` is chosen for the `etᴴ Atn en` orientation, not
the `enᴴ Atn et` orientation; reading the Palace L0 comment as documentation of caller intent).

## Applicability conditions

The rewrite preserves semantics when:

1. **Read-only `x`, `M`, `y`.** `Dot(comm, x, A, y)` never writes any of its inputs; the `A.Mult`
   virtual is `const`. The only buffer mutation is the internal workspace `Ax` overwrite (the
   inherited `apply_linop` rotation, scoped to the call). The result is a returned scalar.
2. **`M` is a linear operator.** Nonlinear weights are not supported and not meaningful for
   `xᴴ M y` (see [`L1/bilinear_form`](../L1/bilinear_form.md) §Applicability conditions).
3. **Shape compatibility.** `M`'s codomain axis equals `x`'s length; `M`'s domain axis equals
   `y`'s length. **`M` need not be square** — unlike the weighted-norm sibling, the bilinear form
   admits rectangular `M`. (The L0 surface enforces `Ax.Size() == y.Size()` via the inherited
   inner `Dot` precondition — `Dot(comm, a, b)` requires `a.Size() == b.Size()`. So
   `A.Height() == y.Size()`, i.e. `M`'s codomain matches `y`. `M`'s domain matches `x` via the
   inherited `A.Mult(x, Ax)` precondition.)

   **NB**: the *Palace surfaced* callsites all happen to use square `M`
   (`Bttr : N×N`, `Atn : N×N`), so the rectangular case is not exercised; this is faithfully
   recorded as a variant-axis coverage gap, not an algebraic restriction.
4. **No SPD / Hermitian / positivity precondition on `M`.** The form `xᴴ M y` is well-defined for
   any linear `M`. The non-Hermitian witness `boundarymodeoperator.cpp:90` (`Atn`) is direct
   evidence that Palace exercises this. **This is the structural distinguisher from
   `matrix_weighted_norm`**, which requires SPD.
5. **Element-type compatibility.** The L0 surface fixes `x` and `y` as `ComplexVector`; the
   L1 entry's §Signature element-type table records this constraint. The real-`x` / real-`M` /
   real-`y` case is **not** surfaced (Palace does not provide an `xᵀ A y` overload); this is the
   L1 entry's variant-axis coverage gap, not closed by this theme.
6. **Single-rank reading of the collective.** The `MPI_Allreduce` inside the inner `Dot` is a
   local no-op under the single-machine target (CLAUDE.md "Scope"); structurally present, carrying
   the bit-determinism caveat. Inherited from [`dot-mutation-rotation`](./dot-mutation-rotation.md)
   applicability condition 4.
7. **Conjugation-asymmetry reconciliation via argument-position swap at the L1>L0 boundary.** See
   §"Conjugation asymmetry" above. The L1 form `bilinear_form(x, M, y) = xᴴ M y` lowers to the L0
   call `linalg::Dot(comm, y, M, x)`; or, equivalently, `linalg::Dot(comm, x, M, y) = yᴴ M x =
   conj(xᴴ Mᴴ y)` (which matches the L1 form for Hermitian `M` modulo an outer `conj`, and in
   general requires an additional adjoint). Palace's own callsites use the L0 convention
   `Dot(comm, x, M, y) = yᴴ M x` consistently.

## Justification kind

- **Sub-pattern A (real-`A` overload)** — `structural`. The three-step expansion `alloc → split
  Mult → Dot return`; result to the return register, `A·x` to the internal `Ax`; the lane split
  is the inherited `complex-from-real-lift`.
- **Sub-pattern B (complex-`A` overload)** — `structural`. The same three-step expansion with a
  single direct apply replacing the two-call lane split.
- **Sub-pattern C (call-sites)** — `structural`. Pure delegation to A/B at the call boundary,
  with witnesses for both M-symmetry-property values (Hermitian `Bttr`, non-Hermitian `Atn`).

The theme as a whole is `structural`, resting on:

- One **algebraic identity** ([`L1/bilinear_form`](../L1/bilinear_form.md) Composition note:
  `bilinear_form(x, M, y) = dot(x, apply_linop(M, y))`).
- Two **inherited sub-themes** (`apply-linop-mutation-rotation` Sub-pattern A, applied once or
  twice; `dot-mutation-rotation` Sub-pattern A).
- One **conjugation-asymmetry reconciliation** (argument-position swap, inherited from
  `dot-mutation-rotation` §"The conjugation asymmetry").
- One **transparent infrastructure step** (`Ax.UseDevice(true)` device placement, algebraically
  invisible).

**No load-bearing trick classification** is needed — unlike the weighted-norm sibling, there is
no `MFEM_ASSERT` SPD guard, no `std::sqrt`, and no real-projection discard of an imaginary part.
The bilinear form is the cleanest possible three-step composition: alloc, apply, reduce.

The non-syntactic ingredients — the `complex-from-real-lift` for the real-`A` overload, the
argument-position-swap reconciliation, the element-type-overload absorption onto `apply_linop` —
are all **positively anchored** in the inherited sub-themes and L1 entries (no negative-anchor
reconstruction, no literature inference, no speculative operator). Hence `firm` rather than
`partly-constructive`.

## Speculative L1 operators

**None.** This theme lowers the existing L1 [`bilinear_form`](../L1/bilinear_form.md) operator
(rough-in test-coverage-bounded) into existing firm L1 vocabulary — `apply_linop` for the `M·x`
(or `M·y`) step, `dot` for the inner reduction. It proposes no new L1 vocabulary. The sibling
**matrix_weighted_norm** `linalg::Norml2(comm, x, B, Bx)` shares the same two L1 primitives but
with the diagonal restriction `y = x` plus an outer `√` and an SPD applicability condition; it is
a **different operator** ([`L1/matrix_weighted_norm`](../L1/matrix_weighted_norm.md)) with its own
firm theme ([`matrix-weighted-norm-mutation-rotation`](./matrix-weighted-norm-mutation-rotation.md)).
The two themes share L0-file-block evidence (both live in `palace/linalg/operator.{hpp,cpp}`) and
inherited sub-themes (`apply-linop` Sub-pattern A + `dot` Sub-pattern A) but are kept separate
because the L1 operators are distinct (different signatures, different applicability conditions,
different consumer patterns) and the workspace-ownership boundary differs (caller-supplied `Bx`
vs internally-allocated `Ax`).

## Variant axes

`bilinear_form` has two orthogonal variant axes at the L1>L0 edge (per `classify-variant-axis`),
plus one collapsed onto an inherited sub-theme:

- **element-type of `M`**: `real` | `complex`. At L0 these are the two overloads
  (`Operator` weight, Sub-pattern A, `palace/linalg/operator.cpp:621-629`; `ComplexOperator`
  weight, Sub-pattern B, `palace/linalg/operator.cpp:631-638`). They differ in the leading-apply
  plumbing (real: lane split; complex: direct apply) but produce the same result type
  (`std::complex<double>`) and the same closed-form `xᴴ M y`. At L1 these **collapse to a single
  operator** — the element-type axis is absorbed by `apply_linop`'s representation variant axis.
- **M-symmetry-property**: `hermitian` | `non-symmetric`. This axis is **material at L1** because
  law 7 (Hermitian symmetry) of [`L1/bilinear_form`](../L1/bilinear_form.md) holds conditionally.
  At L0 it is **not** a variant axis — the same `linalg::Dot(comm, x, A, y)` overload handles
  both cases without dispatch. Palace exercises both witnesses in the same function:
  `boundarymodeoperator.cpp:85` (Hermitian `Bttr`), `:90` (non-Hermitian `Atn`). The lowering is
  uniform; the M-symmetry is **caller-side** knowledge that conditions which L1 laws are
  applicable, not a structural variant of the L0 surface.

Collapsed (absorbed) axes:

- **operator-representation of `M`**: at L0 `M` may be any concrete `Operator` or
  `ComplexOperator` subclass; per `apply_linop`'s variant absorption, this is collapsed at L1 to
  the opaque `LinearOperator[M, N]` type. Sparse-matrix / matrix-free / composition / multigrid
  representations are all admitted; the L1 contract sees only the linear-map interface.

Promotion-to-firm gates (upstream, not closed by this theme):

- **Real-`x` / real-`M` / real-`y` case**: not surfaced by Palace's L0 overload set; the L1 entry
  records this as the dominant variant-axis coverage gap. The eventual harvest of an `xᵀ A y`
  surface (or a tested confirmation that the absence is intentional) would close it.
- **Cauchy–Schwarz tight case at `y = x`**: unexercised by Palace; would be tested via either a
  dedicated unit test or an indirect call-site sweep through the weighted-norm consumer chain.

These gates are **upstream** L1-entry promotion conditions; they do not gate this theme's status
(per the `matrix-weighted-norm-mutation-rotation` precedent — a firm lowering theme over a
rough-in L1 entry is consistent).

## Evidence

L0 evidence ranges:

- `palace/linalg/operator.hpp:386-394` — both bilinear_form overload declarations + comments
  (`// Compute the bilinear form inner product yᴴ A x for a {real,complex} operator A and complex
   vectors. Allocates workspace internally.`).
- `palace/linalg/operator.cpp:621-629` — real-`A` overload body: `ComplexVector Ax(A.Height())`
  (`:624`), `Ax.UseDevice(true)` (`:625`), `A.Mult(x.Real(), Ax.Real())` (`:626`),
  `A.Mult(x.Imag(), Ax.Imag())` (`:627`), `return Dot(comm, Ax, y)` (`:628`).
- `palace/linalg/operator.cpp:631-638` — complex-`A` overload body: `ComplexVector Ax(A.Height())`
  (`:634`), `Ax.UseDevice(true)` (`:635`), `A.Mult(x, Ax)` (`:636`), `return Dot(comm, Ax, y)`
  (`:637`).
- `palace/models/boundarymodeoperator.cpp:75-93` — `ComputePoyntingPower` body. Line `:85`
  Hermitian-`A` callsite (`Bttr`); line `:90` non-Hermitian-`A` callsite (`Atn`).
- `palace/linalg/nleps.cpp:672-675` — Newton denominator using unweighted `linalg::Dot(GetComm(),
   w, w0)` (informational; not a bilinear_form callsite).

L1 / cross-theme anchors:

- [`L1/bilinear_form`](../L1/bilinear_form.md) — the L1 operator this theme lowers
  (rough-in test-coverage-bounded): closed form `xᴴ M y` (`:18-19`), composition note
  `bilinear_form(x, M, y) = dot(x, apply_linop(M, y))` (`:111-117`), conjugation convention
  (`:148-159`), algebraic laws 1-8 (`:181-220`), variant axes incl. M-symmetry-property
  (`:258-302`), applicability conditions (`:304-318`), test-coverage promotion gate (`:319-344`).
- [`L1/matrix_weighted_norm`](../L1/matrix_weighted_norm.md) — the sibling diagonal-restricted
  operator (rough-in test-coverage-bounded) for parallel-structure verification.
- [`L1-L0/matrix-weighted-norm-mutation-rotation`](./matrix-weighted-norm-mutation-rotation.md) —
  the firm paired sibling theme; followed as the structural precedent. Workspace boundary
  (`Bx` caller-supplied) explicitly contrasted; the L0 internal `Ax` boundary cited at
  `:194-196`. Sub-pattern A `B.Mult` lane-split lift inherited identically.
- [`L1-L0/apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md) — Sub-pattern A
  (bare `A.Mult(x, y)` forward apply into a destination buffer) inherited as step 1; the
  `complex-from-real-lift` for the real-`A` overload's real/imaginary split (§Applicability
  condition 3).
- [`L1-L0/dot-mutation-rotation`](./dot-mutation-rotation.md) — Sub-pattern A (`linalg::Dot(comm,
   Ax, y)` = `Mpi::GlobalSum ∘ LocalDot`) inherited as step 2; the arg-2-conjugated convention
  + the L1/L0 conjugation asymmetry reconciliation (§"The conjugation asymmetry") inherited
  directly (not restated).
- [`L1/apply_linop`](../L1/apply_linop.md)`:50` — laws 1 / 4 / 5 / 6 underwriting the `M·x` step
  across operator-representation axis.
- [`L1/dot`](../L1/dot.md)`:43, 104-105` — the arg-1-conjugated L1 convention + the documented
  L1/L0 conjugation asymmetry.

## Relationship to the matrix_weighted_norm sibling

The L1 operator [`bilinear_form`](../L1/bilinear_form.md) and its sibling
[`L1/matrix_weighted_norm`](../L1/matrix_weighted_norm.md) share L0-file-block evidence (both live
in `palace/linalg/operator.{hpp,cpp}`) and inherited sub-themes (`apply_linop` Sub-pattern A + `dot`
Sub-pattern A), but are distinct operators with their own firm themes
([`matrix-weighted-norm-mutation-rotation`](./matrix-weighted-norm-mutation-rotation.md)). The
single structural distinguisher is the workspace-ownership boundary (caller-supplied `Bx` vs
internally-allocated `Ax`); the bilinear form additionally admits the off-diagonal non-Hermitian
case the weighted norm excludes by its SPD precondition. The lowering's structural fidelity is
independent of the L1 leaf's own promotion gates: this theme lowers the L1 form into the L0 source
regardless of the L1 entry's test-coverage status — the same firm-theme-over-rough-in-leaf pattern
as [`matrix-weighted-norm-mutation-rotation`](./matrix-weighted-norm-mutation-rotation.md) and
[`eigsolve-mutation-rotation`](./eigsolve-mutation-rotation.md).

## Status

`firm` — the structural expansion of the L0 `Dot(comm, x, A, y)` three-step composition
`alloc → A.Mult → Dot return`, pinned by direct evidence (the two overload decls
`palace/linalg/operator.hpp:386-389` / `:391-394`, the two specialization bodies
`palace/linalg/operator.cpp:621-629` / `:631-638`, the two callsite witnesses
`palace/models/boundarymodeoperator.cpp:85` / `:90`). The non-syntactic ingredients
(`complex-from-real-lift`, the argument-position-swap conjugation reconciliation, the
element-type-overload absorption onto `apply_linop`) are positively anchored to the L0 source's
own `yᴴ A x` comments and the inherited sub-themes — no negative-anchor reconstruction.
