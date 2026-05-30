---
agent: lowering-verifier
invoked_at: 2026-05-30T010118Z
scope: L1>L0 theme audit — bilinear-form-mutation-rotation
status: integrated
integrated_at: 2026-05-30T050000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: Applied clean as report-3 of cycle-030; appended 19-row `verified_against:` block (all supports, fully-supported); theme stays firm. Repairer fixed (a) bare-basename `operator.cpp:613-614` AMBIG → full path, (b) two leading-single-quote `note:` values that broke `yaml.safe_load` (the c030 refinement of the c028 leading-DOUBLE-quote hazard — recurrence-2 of channel-format friction). See `reports/cycle-030-integrator-staging/STAGING.md` row 3 + `log/cycle-30.md` HEADLINE 2.
inputs:
  - book/src/L1-L0/bilinear-form-mutation-rotation.md (the firm theme under audit, landed cycle-029 dispatch-2)
  - book/src/L1/bilinear-form.md (the L1 operator, rough-in test-coverage-bounded)
  - book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md (the firm sibling — workspace-ownership cross-check)
  - book/src/L1-L0/apply-linop-mutation-rotation.md (inherited Sub-pattern A + complex-from-real-lift)
  - book/src/L1-L0/dot-mutation-rotation.md (inherited Sub-pattern A + conjugation-asymmetry reconciliation)
  - book/src/L1/dot.md (arg-1-conjugated L1 convention anchor)
  - reference/palace/palace/linalg/operator.hpp:386-394 (the two bilinear-form Dot decls)
  - reference/palace/palace/linalg/operator.cpp:621-639 (the two Dot specializations)
  - reference/palace/palace/models/boundarymodeoperator.cpp:75-93 (the Hermitian Bttr + non-Hermitian Atn callsites)
  - reference/palace/palace/linalg/nleps.cpp:672-675 (the informational Newton denominator)
  - reports/2026-05-29T205945Z-abstractor-bilinear-form-mutation-rotation/CYCLE.md (precedent abstractor report)
  - tools/citecheck/citecheck.py (mechanical citation source-of-truth)
---

# CYCLE: Audit bilinear-form-mutation-rotation

## Summary

Audits the firm L1>L0 theme `bilinear-form-mutation-rotation` (landed cycle-029 dispatch-2,
integration commit `e44896d`). The theme lowers the L1 operator `bilinear_form(x, M, y) = xᴴ M y`
(rough-in test-coverage-bounded) into Palace's two `linalg::Dot(comm, x, A, y)` free-function
overloads at `palace/linalg/operator.cpp:621-629` (real-A) / `:631-638` (complex-A) plus the two
callsite witnesses at `palace/models/boundarymodeoperator.cpp:85` (Hermitian Bttr) / `:90`
(non-Hermitian Atn).

**Top-level verdict: fully-supported.** Every cited Palace L0 range exhibits exactly the form
claimed (mechanically `citecheck --anchor`-confirmed on-disk, plus semantic eyeball verification);
the conjugation-asymmetry reconciliation (L1 arg-1-conjugated `xᴴ M y` vs L0 arg-2-conjugated
`Dot=yᴴAx`) is internally consistent and correctly anchored to the inherited
`dot-mutation-rotation` reconciliation; the workspace-ownership distinction (internally-allocated
`Ax` vs the sibling's caller-supplied `Bx`) is exact and cross-attested in both sibling themes;
the inherited apply-linop Sub-pattern A + dot Sub-pattern A boundaries hold; the c029 repairer's
two corrections (the misquoted composition identity `dot(apply_linop(M,y),x)` -> upstream-canonical
`dot(x, apply_linop(M,y))` AND the Atn-construction span `:88-90` -> `:88-89`) are correctly
landed in the on-disk firm theme. Law-confidence is justified: structural-only justifications
rest on inherited firm sub-themes (no new algebraic-law assertions over the bilinear form that
would require its own test coverage). 19/19 anchors clean; one nit (a minor doc-prose
duplicate-citation framing) recorded under §"Open questions / caveats" as non-blocking.

The audit emits the standard `verified_against:` YAML block as a proposed-changes append for
the integrator to add to the theme.

## Per-citation audit

### L0 Palace source citations

- **Citation**: `palace/linalg/operator.hpp:386-394` (both bilinear-form overload decls + comments)
  - **Theme claim**: "Both overloads' comments document the form as `yᴴ A x` (the L0 convention).
    Allocates workspace internally."
  - **Found** (lines 386-394 on-disk): identical to theme transcription. `:386-387` is the real-A
    overload comment "Compute the bilinear form inner product yᴴ A x for a real operator A and
    complex vectors. Allocates workspace internally."; `:388-389` is the real-A decl
    `std::complex<double> Dot(MPI_Comm comm, const ComplexVector &x, const Operator &A,
    const ComplexVector &y);`. `:391-392` is the complex-A overload comment (same text, swapping
    "real" -> "complex"); `:393-394` is the complex-A decl
    `std::complex<double> Dot(MPI_Comm comm, const ComplexVector &x, const ComplexOperator &A,
    const ComplexVector &y);`. `citecheck --anchor 'Compute the bilinear form'` lands at lines
    `[386, 391]` both within `386-394`.
  - **Verdict**: supports
  - **Notes**: the comment text "yᴴ A x" is the load-bearing positive anchor for the conjugation
    reconciliation — Palace itself documents the arg-2-conjugated convention, making it not a
    theme reconstruction but a direct read of the L0 surface. Verified.

- **Citation**: `palace/linalg/operator.cpp:621-629` (real-A overload body)
  - **Theme claim**: Three-step composition `ComplexVector Ax(A.Height())` (`:624`),
    `Ax.UseDevice(true)` (`:625`), `A.Mult(x.Real(), Ax.Real())` (`:626`), `A.Mult(x.Imag(),
    Ax.Imag())` (`:627`), `return Dot(comm, Ax, y)` (`:628`).
  - **Found** (lines 621-629 on-disk): exact match. Line 621 is the function header
    `std::complex<double> Dot(MPI_Comm comm, const ComplexVector &x, const Operator &A,`,
    line 622 the continuation `const ComplexVector &y)`, line 623 the opening brace `{`, line 624
    `  ComplexVector Ax(A.Height());`, line 625 `  Ax.UseDevice(true);`, line 626
    `  A.Mult(x.Real(), Ax.Real());`, line 627 `  A.Mult(x.Imag(), Ax.Imag());`, line 628
    `  return Dot(comm, Ax, y);`, line 629 `}`. `citecheck --anchor 'ComplexVector Ax'` lands at
    `[624]`; `--anchor 'A.Mult(x.Real()'` lands at `[626]`. All claimed pinpoints exact.
  - **Verdict**: supports
  - **Notes**: This is the real-A overload whose lane split applies `A` to the real and imaginary
    components of `x` separately — exactly the same shape as Sub-pattern B of the
    matrix-weighted-norm sibling theme (`:613-614`). Theme correctly inherits via
    `apply-linop` Sub-pattern A + complex-from-real-lift (apply-linop applicability condition 3,
    on-disk `:225`).

- **Citation**: `palace/linalg/operator.cpp:631-638` (complex-A overload body)
  - **Theme claim**: Three-step composition `ComplexVector Ax(A.Height())` (`:634`),
    `Ax.UseDevice(true)` (`:635`), `A.Mult(x, Ax)` (`:636`), `return Dot(comm, Ax, y)` (`:637`).
  - **Found** (lines 631-638 on-disk): exact match. Line 631 the function header
    `std::complex<double> Dot(MPI_Comm comm, const ComplexVector &x, const ComplexOperator &A,`,
    line 632 the continuation, line 633 the brace, line 634 `  ComplexVector Ax(A.Height());`,
    line 635 `  Ax.UseDevice(true);`, line 636 `  A.Mult(x, Ax);`, line 637
    `  return Dot(comm, Ax, y);`, line 638 `}`. `citecheck --anchor 'A.Mult(x, Ax)'` lands at
    `[636]`. All claimed pinpoints exact.
  - **Verdict**: supports
  - **Notes**: the structural-distinguisher from Sub-pattern A — a single direct apply
    (`A.Mult(x, Ax)`) instead of the two-lane split — confirms the element-type variant axis
    "real `A` lane-splits, complex `A` direct-applies" is exactly two-line code-different. Theme
    classification correct.

- **Citation**: `palace/models/boundarymodeoperator.cpp:75-93` (`ComputePoyntingPower` body)
  with sub-citations `:85` (Hermitian Bttr callsite), `:88-89` (Atn construction),
  `:90` (non-Hermitian Atn callsite)
  - **Theme claim**: Line `:85` is the Hermitian-A callsite
    `std::complex<double> P = 0.5 * std::conj(kn) / omega * linalg::Dot(comm, et, *Bttr, et);`;
    lines `:88-89` construct `Atn = ComplexWrapperOperator(Atnr, Atni)`; line `:90` is the
    non-Hermitian-A callsite `P += std::complex<double>(0.0, 1.0) / (2.0 * omega) *
    linalg::Dot(comm, en, Atn, et);`.
  - **Found** (lines 75-93 on-disk): exact match. Line 85 is verbatim the Hermitian Bttr
    callsite as quoted. Line 88 is `    ComplexWrapperOperator Atn(const_cast<mfem::HypreParMatrix
    *>(Atnr.get()),`, line 89 `                               const_cast<mfem::HypreParMatrix
    *>(Atni.get()));`. Line 90 is verbatim the non-Hermitian Atn callsite as quoted.
    `citecheck --anchor 'linalg::Dot'` lands at `[85]` for the `:85` citation and `[90]` for the
    `:90` citation (both single-line). `--anchor 'ComplexWrapperOperator'` lands at `[88]` within
    `88-89`. The c029 repairer's correction `:88-90` -> `:88-89` for the Atn-construction span is
    correctly landed: the construction spans exactly two source lines (`88-89`); line 90 is the
    USE of `Atn`, not its construction.
  - **Verdict**: supports
  - **Notes**: The two callsites are exactly the two M-symmetry-property axis witnesses the
    theme claims — `Bttr` is a real symmetric MFEM `HypreParMatrix` (wrapped as
    `unique_ptr<ComplexOperator>` per the `*Bttr` dereference; the Sub-pattern B complex-A
    overload is dispatched), and `Atn` is a complex wrapper around a non-symmetric Hypre
    matrix (constructed inline as `ComplexWrapperOperator`; same Sub-pattern B dispatch). The
    theme's claim that BOTH callsites use the complex-A overload is correct: `*Bttr` is a
    `ComplexOperator&` per the `unique_ptr<ComplexOperator>` member declaration, and `Atn` is a
    direct `ComplexWrapperOperator` (which inherits from `ComplexOperator`). The real-A
    Sub-pattern A overload genuinely has no in-tree witness — the theme honestly records this as
    a variant-axis-coverage gap, not a closure.

- **Citation**: `palace/linalg/nleps.cpp:672-675` (informational Newton denominator)
  - **Theme claim**: `delta_eig = -(linalg::Dot(GetComm(), u, w0) + u2_w0) / linalg::Dot(GetComm(),
    w, w0)`; this is the UNWEIGHTED two-argument `linalg::Dot` (the `dot` lowering, NOT the
    bilinear-form lowering); informational only.
  - **Found** (lines 672-675 on-disk): exact match. Line 672 the comment
    `// Undamped Newton step for the eigenvalue; the line search damps it.`; line 673
    `const std::complex<double> u2_w0 = std::complex<double>(w2.adjoint() * u2);`; line 674
    `const std::complex<double> delta_eig =`; line 675
    `    -(linalg::Dot(GetComm(), u, w0) + u2_w0) / linalg::Dot(GetComm(), w, w0);`. `citecheck
    --anchor 'linalg::Dot(GetComm(), w, w0)'` lands at `[675]` within `672-675`.
  - **Verdict**: supports
  - **Notes**: theme correctly classifies this as "NOT a bilinear-form callsite". Both `Dot`
    calls on line 675 take only `(comm, x, y)` argument signatures — three arguments, the
    unweighted `dot` lowering. The theme's claim that the Newton denominator inlines the
    unfolding manually (treating the weight separately via `apply_linop` then composing with
    unweighted `dot`) is consistent with the surrounding context (the `w2.adjoint() * u2` on
    line 673 is an MFEM dense `eigen`-style operation; the construction of `w` and `w0` happens
    upstream via separate `opJ->AddMult` / `A->AddMult` calls at lines 668-669). The
    classification as informational-only (NOT a Sub-pattern A or B witness) is correct.

### L1 / cross-theme anchors

- **Citation**: [`L1/bilinear-form`](../L1/bilinear-form.md) `:18-19`, `:111-117`, `:148-159`,
  `:181-220`, `:258-302`, `:304-318`, `:319-344` (the L1 operator the theme lowers)
  - **Theme claim**: closed form `xᴴ M y` (`:18-19`), composition note (`:111-117`),
    conjugation convention (`:148-159`), algebraic laws 1-8 (`:181-220`), variant axes incl.
    M-symmetry-property (`:258-302`), applicability conditions (`:304-318`), test-coverage
    promotion gate (`:319-344`).
  - **Found** (read on-disk): `:18-19` -> "Mutation-free matrix-weighted inner-product reduction:
    `α = xᴴ M y`" — exact. `:111-117` -> the "Composition into `apply_linop` + `dot`
    (informational)" block stating `bilinear_form(x, M, y) = dot(x, apply_linop(M, y))` —
    exact, AND confirms the c029 repairer's correction of the previously-misquoted form. The
    other ranges checked via citecheck bounds (all OK). Per the structural-redirect convention,
    spot-reading the load-bearing one (`:111-117` for the composition identity) is sufficient:
    the corrected identity is on-disk in the upstream L1 entry, and the theme correctly cites
    it without rewording.
  - **Verdict**: supports
  - **Notes**: this is the upstream rough-in L1 entry; the theme correctly notes the
    "rough-in (test-coverage-bounded)" status of its LHS and the firm-over-rough-in precedent
    (matrix-weighted-norm / eigsolve). Status independence holds.

- **Citation**: [`L1/matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (sibling
  diagonal-restricted operator)
  - **Theme claim**: parallel-structure verification.
  - **Found**: confirmed by reading sibling theme — both L1 entries have parallel-structure
    headings (Signature, Semantics, Algebraic laws, Variant axes, Applicability conditions,
    Status). Sibling is firm-over-rough-in (precedent), bilinear-form is firm-over-rough-in
    (this theme); parallel.
  - **Verdict**: supports

- **Citation**: [`L1-L0/matrix-weighted-norm-mutation-rotation`](./matrix-weighted-norm-mutation-rotation.md)
  `:194-196` (the firm paired sibling — workspace-ownership boundary cross-attestation)
  - **Theme claim**: "Workspace boundary (`Bx` caller-supplied) explicitly contrasted; the L0
    internal `Ax` boundary cited at `:194-196`."
  - **Found** (lines 194-196 on-disk): "- **It is caller-owned, not internally allocated.**
    Contrast the sibling bilinear-form `linalg::Dot(comm, x, A, y)`
    (`palace/linalg/operator.hpp:386-389`, `palace/linalg/operator.cpp:621-639`), which allocates
    its workspace `Ax` internally (`ComplexVector Ax(A.Height())`). `Norml2` instead requires the
    caller to pass `Bx` so it can be **reused across calls** without per-call allocation..." —
    exact cross-attestation. The sibling explicitly defers the `Ax` internal allocation to this
    theme; this theme explicitly contrasts the `Bx` caller-supplied to its `Ax` internal. The
    workspace-ownership distinction is bidirectionally documented.
  - **Verdict**: supports
  - **Notes**: cross-attestation confirmed in both directions; no contradiction.

- **Citation**: [`L1-L0/apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md)
  Sub-pattern A + complex-from-real-lift (applicability condition 3 at on-disk `:218-225`)
  - **Theme claim**: "Sub-pattern A (bare `A.Mult(x, y)` forward apply into a destination buffer)
    inherited as step 1; the `complex-from-real-lift` for the real-`A` overload's real/imaginary
    split (§Applicability condition 3)."
  - **Found**: Sub-pattern A header at apply-linop line 43 ("bare forward apply `Mult`");
    complex-from-real-lift named at line 225 ("The lifting is the `complex-from-real-lift`
    concept, not part of this theme."). Both inherited references verified on-disk.
  - **Verdict**: supports

- **Citation**: [`L1-L0/dot-mutation-rotation`](./dot-mutation-rotation.md) Sub-pattern A + §"The
  conjugation asymmetry"
  - **Theme claim**: "Sub-pattern A (`linalg::Dot(comm, Ax, y)` = `Mpi::GlobalSum ∘ LocalDot`)
    inherited as step 2; the arg-2-conjugated convention + the L1/L0 conjugation asymmetry
    reconciliation (§"The conjugation asymmetry") inherited directly (not restated)."
  - **Found**: Sub-pattern A header at dot-mutation-rotation line 44 ("free-function template
    `linalg::Dot(comm, x, y)` (the canonical form)"); §"The conjugation asymmetry" header at
    line 189 ("the core theme content"). Both inherited references verified on-disk.
  - **Verdict**: supports

- **Citation**: [`L1/apply_linop`](../L1/apply_linop.md)`:50` — laws 1/4/5/6
  - **Verdict**: supports (in-bounds per citecheck; the apply_linop laws underwrite the M·x step
    across operator-representation axis; this is a standard parallel-structure cite).

- **Citation**: [`L1/dot`](../L1/dot.md)`:43, 104-105` — arg-1-conjugated L1 convention +
  documented L1/L0 conjugation asymmetry
  - **Theme claim**: arg-1-conjugated L1 convention + documented L1/L0 conjugation asymmetry.
  - **Found** (read on-disk): `:43` -> "Conjugation convention (complex `dot`): conjugate-linear
    in the **first** argument, linear in the second." — exact anchor for the arg-1-conjugated
    L1 convention. `:104-105` -> the "L1 vs L0 distinction" block stating L0's free-function /
    method-form receiver-vs-argument asymmetry; the L1 form erases it ("first argument is by
    convention the conjugated one"). Both citations exact and load-bearing for the theme's
    inherited conjugation reconciliation.
  - **Verdict**: supports

## Applicability conditions

The theme states 7 applicability conditions; each walked below.

- **Condition 1: Read-only `x`, `M`, `y`.** "`Dot(comm, x, A, y)` never writes any of its
  inputs; the `A.Mult` virtual is `const`. The only buffer mutation is the internal workspace
  `Ax` overwrite."
  - **Verifiable**: directly from L0 source `:621-638` — neither overload writes to `x`, `A`,
    or `y` (no `const_cast`, no method calls on them other than the `const A.Mult` virtual and
    the `Real()/Imag()` const accessors). The Ax-overwrite-only claim is exactly the body.
  - **Found counter-example?**: No.

- **Condition 2: `M` is a linear operator.**
  - **Verifiable**: L0 type-system — the parameter is `const Operator &A` or
    `const ComplexOperator &A`; both are the abstract linear-operator types Palace uses
    throughout. There is no nonlinear-operator type in Palace's `linalg/` namespace.
  - **Found counter-example?**: No.

- **Condition 3: Shape compatibility, `M` need not be square.**
  - **Verifiable**: the theme correctly derives this from the inherited preconditions —
    `A.Mult(x, Ax)` requires `A.Width() == x.Size()`; the inner `Dot(comm, Ax, y)` requires
    `Ax.Size() == y.Size()`, i.e. `A.Height() == y.Size()`. So `M`'s codomain matches `y` and
    `M`'s domain matches `x`; nothing forces `Height == Width`. The Palace surfaced callsites
    happen to use square M, but the L0 surface does not REQUIRE squareness.
  - **Found counter-example?**: No. (NB: the theme correctly records the Palace callsite cohort
    is square-M-only as a variant-axis coverage gap, not an algebraic restriction.)

- **Condition 4: No SPD / Hermitian / positivity precondition on `M`.**
  - **Verifiable**: the L0 body has NO `MFEM_ASSERT` of any kind (contrast `Norml2`'s
    `MFEM_ASSERT(dot > 0.0)` at `palace/linalg/operator.cpp:604-605`). The non-Hermitian witness
    `boundarymodeoperator.cpp:90` (`Atn` non-symmetric) executes successfully without firing any
    assertion. Direct evidence the lowering admits non-SPD/non-Hermitian M.
  - **Found counter-example?**: No.

- **Condition 5: Element-type compatibility.** The L0 surface fixes `x`/`y` as `ComplexVector`.
  - **Verifiable**: both overload decls at `:388-389` and `:393-394` show `const ComplexVector &x`
    / `const ComplexVector &y`. No `Vector` (real) overload exists. The theme correctly notes
    the real-x/real-M/real-y case is NOT surfaced.
  - **Found counter-example?**: No.

- **Condition 6: Single-rank reading of the collective.** Inherited from dot-mutation-rotation
  applicability condition 4.
  - **Verifiable**: structurally inherited via the inner `Dot(comm, Ax, y)` call which routes
    through `linalg::Dot(comm, a, b)` and its internal `Mpi::GlobalSum`. Single-rank reading is
    a no-op per CLAUDE.md "Scope".
  - **Found counter-example?**: N/A (this is the CLAUDE.md project-wide convention).

- **Condition 7: Conjugation-asymmetry reconciliation via argument-position swap.**
  - **Verifiable**: directly from L0 source — `Dot(comm, x, A, y)` body computes `Ax = A·x`
    then returns `Dot(comm, Ax, y)`; by the inherited dot arg-2-conjugated convention
    (`L1/dot.md:43, 104-105`; `dot-mutation-rotation` §189), `Dot(comm, Ax, y) = yᴴ Ax = yᴴ A x`,
    which matches the L0 source comments at `:386, :391` exactly. To recover the L1 form
    `bilinear_form(x, M, y) = xᴴ M y` from a single L0 call, the swap is mandatory:
    `linalg::Dot(comm, y, M, x)` would compute `xᴴ M y` directly. Theme's two equivalent
    formulations (direct swap; or call-as-is + outer conj-and-adjoint for non-Hermitian M) are
    both algebraically valid; the swap is the cleaner of the two. The Palace callsites at
    `:85` (`et,Bttr,et` — swap-invariant because x=y) and `:90` (`en,Atn,et` — knowing the
    `yᴴ A x` convention via the `(0.0, 1.0)/(2.0*omega)` prefactor orientation) are both
    consistent with the L0 reading; this is read off the callsite intent, not asserted.
  - **Found counter-example?**: No.

## Algebraic laws (if cited)

The theme does NOT introduce new algebraic laws over the bilinear form; it inherits them from
[`L1/bilinear-form`](../L1/bilinear-form.md) §"Algebraic laws" (laws 1-8) and from the two
sub-themes (`apply_linop` §laws, `dot` §laws). The theme's role is structural lowering, not
algebraic-law statement.

The ONE algebraic identity load-bearing for the lowering — the composition unfolding
`bilinear_form(x, M, y) = dot(x, apply_linop(M, y))` — is correctly cited to the upstream L1
entry `:111-117` (the on-disk corrected form per the c029 repairer). I confirmed the upstream
identity matches: `:111-117` of L1/bilinear-form.md reads "the natural unfolding
`bilinear_form(x, M, y) = dot(x, apply_linop(M, y))`" — exact agreement with the theme's
reference. The c029 repair removed an earlier misquote `dot(apply_linop(M, y), x)` and replaced
it with the L1-canonical `dot(x, apply_linop(M, y))`; on-disk both the theme and the upstream
L1 entry agree.

- **Law (composition identity)**: `bilinear_form(x, M, y) = dot(x, apply_linop(M, y))`.
- **Holds on operators?**: Yes — at L1, by direct substitution: `dot(x, apply_linop(M, y)) =
  xᴴ (M y) = xᴴ M y = bilinear_form(x, M, y)`. The identity holds for any linear `M`; it does
  NOT require `M` to be Hermitian or square. Confirmed.

The L0 surface realizes a SWAPPED form of this unfolding: `Ax = M·x; return Dot(comm, Ax, y) =
yᴴ A x = conj(xᴴ Mᴴ y)`. For Hermitian `M`, this equals `conj(xᴴ M y) = conj(bilinear_form(x,
M, y))`. For non-Hermitian `M`, the L0 call returns `yᴴ A x` directly (not `xᴴ M y`); Palace's
callsites at `:85` (`x=y`, swap-invariant) and `:90` (caller selects prefactor for the `etᴴ Atn
en` orientation) both consume the L0 value with full knowledge of the arg-2-conjugated
convention. **The lowering rule** (theme's §"Conjugation asymmetry"): to lower an L1 form
`bilinear_form(x, M, y) = xᴴ M y` into L0, call `linalg::Dot(comm, y, M, x)` (positions
swapped). This is mechanically the conjugation-reconciliation inherited from
`dot-mutation-rotation`; the theme correctly does not introduce a new reconciliation.

## Proposed changes

```edit:book/src/L1-L0/bilinear-form-mutation-rotation.md
[append at end of file]

~~~yaml
verified_against:
  - citation: palace/linalg/operator.hpp:386-394
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: both bilinear-form Dot overload decls + comments yᴴ A x; citecheck --anchor 'Compute the bilinear form' lands at [386, 391] within range; on-disk lines 386-394 verbatim-match the theme transcription
  - citation: palace/linalg/operator.hpp:386-389
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: real-A overload decl + comment; on-disk :386-387 comment + :388-389 decl exact; provides the load-bearing positive anchor 'yᴴ A x' for the conjugation reconciliation (not a theme reconstruction)
  - citation: palace/linalg/operator.hpp:391-394
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: complex-A overload decl + comment; on-disk :391-392 comment + :393-394 decl exact; same positive anchor for arg-2-conjugated convention
  - citation: palace/linalg/operator.cpp:621-629
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: real-A Dot body; ComplexVector Ax(:624)/UseDevice(:625)/Mult lane split(:626-627)/return Dot(:628) all citecheck --anchor OK; lane-split exactly parallels matrix-weighted-norm Sub-pattern B (palace/linalg/operator.cpp:613-614)
  - citation: palace/linalg/operator.cpp:631-638
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: complex-A Dot body; ComplexVector Ax(:634)/UseDevice(:635)/direct Mult(:636)/return Dot(:637) all exact; the single-direct-apply form (vs Sub-pattern A's lane split) is the only element-type difference
  - citation: palace/models/boundarymodeoperator.cpp:75-93
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: ComputePoyntingPower body; on-disk matches theme; both Bttr(:85) Hermitian-A and Atn(:90) non-Hermitian-A callsites within range; both dispatch via complex-A Sub-pattern B overload
  - citation: palace/models/boundarymodeoperator.cpp:85
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: Hermitian Bttr callsite; on-disk verbatim '0.5 * std::conj(kn) / omega * linalg::Dot(comm, et, *Bttr, et)'; the diagonal (x=y) case so the L1/L0 arg-swap is invisible
  - citation: palace/models/boundarymodeoperator.cpp:88-89
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: Atn ComplexWrapperOperator construction; cycle-029 repairer correction :88-90 to :88-89 confirmed on-disk (construction spans exactly two lines; line 90 is the USE not construction); --anchor 'ComplexWrapperOperator' lands at [88] within :88-89
  - citation: palace/models/boundarymodeoperator.cpp:90
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: non-Hermitian Atn callsite; on-disk verbatim 'P += std::complex<double>(0.0, 1.0) / (2.0 * omega) * linalg::Dot(comm, en, Atn, et)'; the caller-selected prefactor orientation confirms the arg-2-conjugated reading via the etᴴ Atn en intent
  - citation: palace/linalg/nleps.cpp:672-675
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: informational Newton denominator; both linalg::Dot calls on :675 are the unweighted 3-arg form (comm,x,y), NOT bilinear-form 4-arg; correctly classified as a peer datum (manually-inlined L1>L0 unfolding) not a Sub-pattern A/B callsite; NOT affected by cycle-025 nleps +1 codemap drift (anchor at :675 verified on-disk)
  - citation: book/src/L1/bilinear-form.md:111-117
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: composition identity bilinear_form(x, M, y) = dot(x, apply_linop(M, y)); cycle-029 repairer correction landed on-disk (previous misquote dot(apply_linop(M,y), x) replaced with upstream-canonical dot(x, apply_linop(M,y))); theme cites the corrected form
  - citation: book/src/L1/dot.md:43
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: arg-1-conjugated L1 convention 'conjugate-linear in the first argument'; the load-bearing inherited convention that motivates the L1 form xᴴ M y and gives the clean bilinear_form(x, I, y) = dot(x, y) specialisation
  - citation: book/src/L1/dot.md:104-105
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: L1 vs L0 distinction recording the receiver-vs-argument arg-2-conjugated L0 convention; theme inherits the reconciliation rather than restating
  - citation: book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md:194-196
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: workspace-ownership boundary cross-attestation; sibling explicitly cites this theme as the internal-Ax counterpart, this theme explicitly contrasts the caller-supplied Bx; bidirectional documentation, no contradiction
  - citation: book/src/L1-L0/apply-linop-mutation-rotation.md:225
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: complex-from-real-lift concept (applicability condition 3 zone :218-225); the named inherited mechanism for the real-A overload's lane split; theme correctly cites
  - citation: book/src/L1-L0/dot-mutation-rotation.md:44
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: Sub-pattern A free-function 'linalg::Dot(comm, x, y) canonical form'; the inherited inner-Dot reduction lowering
  - citation: book/src/L1-L0/dot-mutation-rotation.md:189
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: section header "The conjugation asymmetry" — the core theme content; the inherited reconciliation the bilinear-form theme refers to rather than restating
  - citation: book/src/L1/apply_linop.md:50
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: laws 1/4/5/6 underwriting the M·x apply step across operator-representation axis (cited for parallel-structure with the sibling theme; in-bounds per citecheck)
  - citation: book/src/L1/bilinear-form.md:18-19
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: opening tagline — Mutation-free matrix-weighted inner-product reduction α = xᴴ M y; the L1 closed form the theme lowers
~~~

```

The block above appends a `verified_against:` YAML fence to the on-disk theme file. The
audit found NO contradictions and NO drift; no additional proposed edits beyond the YAML
metadata block.

## Supporting evidence

### Citecheck `--anchor` runs (mechanical no-drift confirmation)

All 19 citations bounds-clean via `citecheck --scan book/src/L1-L0/bilinear-form-mutation-rotation.md
--quiet` (exit 0, "19 ok, 0 failing").

Per-anchor (the load-bearing pinpoints):

- `palace/linalg/operator.hpp:386-394 --anchor 'Compute the bilinear form'` -> OK at `[386, 391]`
- `palace/linalg/operator.hpp:386-389 --anchor 'real operator'` -> OK at `[386]`
- `palace/linalg/operator.hpp:391-394 --anchor 'complex operator'` -> OK at `[391]`
- `palace/linalg/operator.cpp:621-629 --anchor 'ComplexVector Ax'` -> OK at `[624]`
- `palace/linalg/operator.cpp:621-629 --anchor 'A.Mult(x.Real()'` -> OK at `[626]`
- `palace/linalg/operator.cpp:631-638 --anchor 'A.Mult(x, Ax)'` -> OK at `[636]`
- `palace/models/boundarymodeoperator.cpp:85 --anchor 'linalg::Dot'` -> OK at `[85]`
- `palace/models/boundarymodeoperator.cpp:90 --anchor 'linalg::Dot'` -> OK at `[90]`
- `palace/models/boundarymodeoperator.cpp:88-89 --anchor 'ComplexWrapperOperator'` -> OK at `[88]`
- `palace/linalg/nleps.cpp:672-675 --anchor 'linalg::Dot(GetComm(), w, w0)'` -> OK at `[675]`
- `book/src/L1/dot.md:43 --anchor 'conjug'` -> OK at `[43]`
- `book/src/L1/dot.md:104-105 --anchor 'conjug'` -> OK at `[104, 105]`

### On-disk reads (semantic verification)

- `reference/palace/palace/linalg/operator.hpp:380-403` (the bilinear-form decl block) — read,
  matches theme verbatim.
- `reference/palace/palace/linalg/operator.cpp:595-644` (both Norml2 + both bilinear-form Dot
  specializations) — read, matches theme verbatim; the parallel between matrix-weighted-norm
  Sub-pattern B lane-split (`:613-614`) and bilinear-form Sub-pattern A lane-split (`:626-627`)
  is mechanically identical.
- `reference/palace/palace/models/boundarymodeoperator.cpp:70-95` (ComputePoyntingPower body) —
  read, matches theme verbatim; the c029 `:88-90` -> `:88-89` correction lands precisely
  (construction spans :88-89, callsite USE is :90).
- `reference/palace/palace/linalg/nleps.cpp:668-682` (Newton denominator context) — read,
  confirms both Dot calls on :675 are 3-arg unweighted, not 4-arg bilinear-form.
- `book/src/L1/dot.md:40-50` (conjugation convention) — read, confirms arg-1-conjugated L1
  convention.
- `book/src/L1/dot.md:100-112` (L1 vs L0 distinction) — read, confirms L0 method-form
  receiver-vs-argument asymmetry inherited.
- `book/src/L1/bilinear-form.md:110-120` (composition identity) — read, confirms upstream
  on-disk correctly carries the c029-corrected `dot(x, apply_linop(M, y))` form.
- `book/src/L1-L0/apply-linop-mutation-rotation.md:218-225` (complex-from-real-lift) — read,
  confirms the named inherited mechanism.
- `book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md:186-218` (workspace-ownership
  contrast) — read, confirms bidirectional cross-attestation.

### codemap drift note (per the loaded discipline)

Per the cycle-025 friction-ledger entry `codemap-read-range-plus-one-drift-on-brace-boundary`,
codemap `read_range` can drift +1 on certain multi-line-comment + opening-brace boundaries
(observed batches 5/6/7 on `nleps.cpp:810`-ish region). For this audit I used citecheck
`--anchor` (on-disk) as the source of truth and avoided codemap `read_range` for the
load-bearing pinpoints. The cycle-025 drift on `nleps.cpp` is confirmed NOT to affect
`operator.hpp`, `operator.cpp`, `boundarymodeoperator.cpp`, OR the `nleps.cpp:672-675` Newton
denominator zone (anchors land exactly on asserted lines per citecheck).

## Open questions / caveats

1. **Doc-prose duplicate citation in §"Citations" lists.** The theme's per-sub-pattern
   "Citations:" sections (lines 140-152, 190-197 of on-disk theme) restate `palace/linalg/operator.cpp:621-629`
   and `:631-638` as bare-citation entries that mostly repeat what the inline `(`:624`)` `(`:625`)`
   `(`:626`)` etc. pinpoints already say in the prose two paragraphs up. This is a stylistic
   non-issue (the structural-precedent matrix-weighted-norm sibling does the same — its
   citations at `:99-101, :156-158` are similarly bare-cite-after-prose-cite); flagged here
   only for completeness. **NOT a blocker.** Doc-prose hygiene, not citation drift.

2. **Sub-pattern A real-A overload has no in-tree caller.** Theme honestly records this
   (§"Sub-pattern C — call-sites"). The `boundarymodeoperator.cpp:85, :90` callsites both
   dispatch to the complex-A Sub-pattern B overload (`*Bttr` via `unique_ptr<ComplexOperator>`,
   `Atn` via `ComplexWrapperOperator`). The real-A overload is reachable from the L0 surface
   (declared, defined) but unwitnessed by in-tree callers. This is consistent with the L1
   entry's `rough-in (test-coverage-bounded)` status and is the L1-side variant-axis-coverage
   gap that gates upstream promotion. This audit does NOT close that gate; it remains open per
   the OQ ledger entries the c029 abstractor noted.

3. **The c029 abstractor's Open question #1 (callout-box at the top of the L1 entry stating
   the L1/L0 conjugation asymmetry).** Verified the c029 abstractor's recommendation but did
   not act on it — that's a future downstream polish edit, not in this audit's scope. Recording
   here for traceability: if a future cycle wants to add a one-line callout at the top of
   `book/src/L1/bilinear-form.md` reading "L1 uses arg-1 conjugation (`xᴴ M y`); L0 uses arg-2
   conjugation (`yᴴ A x`); the lowering swaps argument positions" it would be a useful
   reading-aid. NOT a citation-drift or audit-finding issue.

4. **The c029 abstractor's Open question #2 (the L2 "weighted-inner-product reduction"
   combinator lifting note).** Working-notes-only per the high->low discipline; properly
   parked. Not in this audit's scope.

5. **No direction-of-definition violation.** The theme narrates L1 -> L0 (forward / high->low)
   throughout: §"L1 form (LHS)" then §"L0 form (RHS)", with each Sub-pattern A/B/C reading from
   L1 closed form into L0 three-step expansion. The "Conjugation asymmetry — the L1/L0
   reconciliation" §correctly reads as "L1 says X; L0 says Y; the rewrite from L1 into L0
   is..."; the §"The internal workspace `Ax`" §correctly reads as "L1 has no workspace; the
   lowering re-introduces it". No reverse-direction (L0 lifting up to L1) prose in formal
   theme content. PASS.

6. **Promotion status.** The theme is already `firm` (landed c029 dispatch-2). This audit
   confirms-without-change: no status downgrade, no promotion-blocking finding. The
   `verified_against:` block this audit emits is the standard sibling-theme-convention
   metadata appendage, not a status change.
