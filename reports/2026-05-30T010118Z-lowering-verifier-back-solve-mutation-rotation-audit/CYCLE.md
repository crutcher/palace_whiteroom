---
agent: lowering-verifier
invoked_at: 2026-05-30T010118Z
scope: L1>L0 theme audit — back-solve-mutation-rotation (cycle-029 firm landing)
status: integrated
integrated_at: 2026-05-30T050000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: Applied clean as report-2 of cycle-030; appended 22-row `verified_against:` block (21 supports + 1 partially-supports — narrative-only F1 routed to c031); theme stays firm. INDEPENDENT diff confirmation of GMRES `:653-660` ≡ FGMRES `:832-839` byte-identical. See `reports/cycle-030-integrator-staging/STAGING.md` row 2 + `log/cycle-30.md` HEADLINE 2.
inputs:
  - book/src/L1-L0/back-solve-mutation-rotation.md (firm L1>L0 theme, c029 dispatch-1)
  - book/src/L1/back_solve.md (firm L1 leaf, c028 audited)
  - reports/2026-05-29T205945Z-abstractor-back-solve-mutation-rotation/CYCLE.md (c029 abstractor context)
  - reference/palace/palace/linalg/iterative.cpp (GMRES :652-660 + FGMRES :831-840 + boundaries)
  - reference/palace/palace/linalg/iterative.hpp (registers :192-194, FGMRES class :222-256)
  - tools/citecheck/citecheck.py (--anchor source of truth)
---

# CYCLE: Audit back-solve-mutation-rotation

## Summary

`partially-supports` — **substantively-confirms with one factual-error finding and three minor anchor-imprecisions to repair.**

Every cited L0 anchor in `book/src/L1-L0/back-solve-mutation-rotation.md` (22
L0 anchors total: 13 in `iterative.cpp` body/boundary, 5 in `iterative.hpp`,
plus 4 internal cross-anchors to the L1 leaf) is **zero-drift on-disk** per
`tools/citecheck/citecheck.py --anchor` (independently re-confirmed this
invocation, not transcribed from the c029 abstractor's `--scan` run). The
core rotation — the four-element rewrite (descending outer sweep, column-major
stride pointer, diagonal division, column-oriented super-diagonal subtraction)
plus the in-place RHS-as-destination overwrite — is positively anchored
and accurately transcribed; the GMRES `:653-660` and FGMRES `:832-839` blocks
are independently confirmed byte-for-byte identical via `diff` (no character
differences beyond absolute line numbers). The L1 leaf's algebraic laws (1, 4,
5, 6) all hold against the cited source. Applicability conditions 1-6 are
complete and verifiable. Justification kind `structural` is correct. No new
L1 vocabulary is proposed, no operator promotion is gated, no `partly-constructive`
caveat is needed — the firm status is justified by the firm-on-positive-structure
rationale.

**Audit finding (factual error in theme prose, NOT a citation drift): the
theme's Sub-pattern B narrative incorrectly attributes the GMRES↔FGMRES line-
shift to brace-style ("GMRES places `{` at the end of the `for` line; FGMRES
places `{` on the next line"). Direct `diff` of the two ranges shows they are
byte-for-byte identical (both methods place `{` on its own line); the line
numbers differ only because the methods have different preceding code in their
respective `for(;;)` bodies. The L1 leaf at `:225-226` says "line-for-line
identical" — that is the correct phrasing. There is no `+1 line-shift from
brace placement`. The cited LINE NUMBERS (:653/:655/:656/:657/:659 vs
:832/:834/:835/:836/:838) are all correct as anchors, but the explanatory
narrative for WHY they shift is wrong. Mark verdict `partially-supports`
on the FGMRES sub-pattern citations and propose narrative repair below.**

**Three minor anchor-precision repairs** (1-line off-by-one in L1-leaf cross-
references, NOT L0 drift): the theme's `[`L1/back_solve`](../L1/back_solve.md)`
back-anchor list at lines 686-694 cites `:78` (signature), `:218-221` (law 5),
and `:466-540` (verified_against block). Citecheck flags: `back_solve` name is
on `:77` with the `::` arrow on `:78` (signature range `:77-78`); law 5 bullet
header is on `:217` (body `:217-221`); `verified_against:` keyword is on `:467`
(fence at `:466`, block `:466-540`). All three are 1-line-tight; tighten to
`:77-78`, `:217-221`, `:467` for precision.

The theme as a whole is **substantively firm** and the firm landing is
correct — the proposed `verified_against:` block emits in full; the narrative
repair to Sub-pattern B is a follow-up (lifter / abstractor reread, not a
status reduction).

## Per-citation audit

### Sub-pattern A — GMRES canonical back-substitution (:652-660)

- **Citation**: `palace/linalg/iterative.cpp:652`
  - **Theme claim**: comment `"Reconstruct the solution (for restart or due to convergence or maximum iterations)."` naming the block's role.
  - **Found**: `// Reconstruct the solution (for restart or due to convergence or maximum iterations).` at :652 (citecheck `--anchor 'Reconstruct the solution'` → 652 zero-drift).
  - **Verdict**: `supports`.

- **Citation**: `palace/linalg/iterative.cpp:653`
  - **Theme claim**: `for (int i = j; i >= 0; i--)` — descending outer sweep; `j = -1` empty-cycle skips the body (law 5 boundary).
  - **Found**: `for (int i = j; i >= 0; i--)` at :653 zero-drift. The descending direction is correct; the `i >= 0` termination paired with initial `i = j` correctly bounds to `s[0..j]` per applicability-condition 3.
  - **Verdict**: `supports`.

- **Citation**: `palace/linalg/iterative.cpp:655`
  - **Theme claim**: `ScalarType *Hi = H.data() + i * (max_dim + 1);` — column-major stride pointer, column `i` of the dense upper-triangular R-factor.
  - **Found**: `ScalarType *Hi = H.data() + i * (max_dim + 1);` at :655 zero-drift. The stride formula `max_dim+1` is the allocated slab size (allocation detail, not active dimension); the theme correctly classifies this as a transparent-allocation trick.
  - **Verdict**: `supports`.

- **Citation**: `palace/linalg/iterative.cpp:656`
  - **Theme claim**: `s[i] /= Hi[i];` — diagonal division `y[i] = s[i] / R[i][i]` (in-place RHS overwrite kernel, law-1/law-4 boundary, singular-`R` divide-by-zero non-law).
  - **Found**: `s[i] /= Hi[i];` at :656 zero-drift. Compound `/=` operator confirms in-place RHS overwrite.
  - **Verdict**: `supports`.

- **Citation**: `palace/linalg/iterative.cpp:657`
  - **Theme claim**: `for (int k = i - 1; k >= 0; k--)` — inner super-diagonal scan; `i = 0` empty (law 5 single-column boundary).
  - **Found**: `for (int k = i - 1; k >= 0; k--)` at :657 zero-drift. Descending inner scan over rows above the diagonal; `i = 0` gives `k = -1` initial which violates `k >= 0` → loop skips, matches the single-column boundary claim.
  - **Verdict**: `supports`.

- **Citation**: `palace/linalg/iterative.cpp:659`
  - **Theme claim**: `s[k] -= Hi[k] * s[i];` — column-oriented super-diagonal subtraction `s[k] -= R[k][i] * y[i]`; reduction-order non-law.
  - **Found**: `s[k] -= Hi[k] * s[i];` at :659 zero-drift. The `s[i]` factor is the just-written `y[i]` (from :656); the `s[k]` accumulator is read-modify-write (compound `-=`); the descending sweep ensures correctness (each `s[k]` finalised at outer iteration `i = k`).
  - **Verdict**: `supports`.

### Sub-pattern B — FGMRES twin (:831-840)

- **Citation**: `palace/linalg/iterative.cpp:831`
  - **Theme claim**: comment `"Reconstruct the solution (for restart or due to convergence or maximum iterations)."` — FGMRES copy of the role-naming comment.
  - **Found**: `// Reconstruct the solution (for restart or due to convergence or maximum iterations).` at :831 zero-drift; byte-for-byte identical to :652.
  - **Verdict**: `supports`.

- **Citation**: `palace/linalg/iterative.cpp:832`
  - **Theme claim**: `for (int i = j; i >= 0; i--)` — FGMRES outer descending sweep, noted as "+1 line-shift vs GMRES :653 from brace-on-own-line style".
  - **Found**: `for (int i = j; i >= 0; i--)` at :832 zero-drift. **However, the explanatory narrative is wrong** — see below.
  - **Verdict**: `partially-supports`. The cited line and content are correct; the explanatory narrative ("brace placement / line shift; GMRES places `{` at the end of the `for` line; FGMRES places `{` on the next line") in §"Sub-pattern B" lines 219-229 is factually incorrect — both methods place `{` on its own line (GMRES :654 = FGMRES :833 = `    {` indented identically), and the two back-solve bodies are byte-for-byte identical (`diff` confirms zero character differences). The line numbers differ only because of unrelated preceding code in the two methods' `for(;;)` bodies.

- **Citation**: `palace/linalg/iterative.cpp:834`
  - **Theme claim**: `ScalarType *Hi = H.data() + i * (max_dim + 1);` — FGMRES column-major stride pointer, same formula as :655.
  - **Found**: At :834 zero-drift, byte-for-byte identical to :655. Same column-major stride, same allocation detail.
  - **Verdict**: `supports` (same as A:655; the FGMRES twin is correctly transcribed).

- **Citation**: `palace/linalg/iterative.cpp:835`
  - **Theme claim**: `s[i] /= Hi[i];` — FGMRES diagonal division, identical to :656.
  - **Found**: At :835 zero-drift, byte-for-byte identical to :656.
  - **Verdict**: `supports`.

- **Citation**: `palace/linalg/iterative.cpp:836`
  - **Theme claim**: `for (int k = i - 1; k >= 0; k--)` — FGMRES inner scan, identical to :657.
  - **Found**: At :836 zero-drift, byte-for-byte identical to :657.
  - **Verdict**: `supports`.

- **Citation**: `palace/linalg/iterative.cpp:838`
  - **Theme claim**: `s[k] -= Hi[k] * s[i];` — FGMRES column-oriented subtraction, identical to :659.
  - **Found**: At :838 zero-drift, byte-for-byte identical to :659.
  - **Verdict**: `supports`.

### Sub-pattern C — downstream basis-lift boundary markers

- **Citation**: `palace/linalg/iterative.cpp:666`
  - **Theme claim**: `x.Add(s[k], V[k]);` — GMRES `V`-basis lift (LEFT-preconditioning branch). NOT part of the leaf; boundary marker for law-6 basis-lift independence.
  - **Found**: `x.Add(s[k], V[k]);` at :666 zero-drift. Per the surrounding context (:662-668), this is the LEFT branch; the RIGHT branch at :669-678 also reads `s[k]` (at :674 `r.Add(s[k], V[k])`), confirming both branches consume the post-back-solve `s[0..j]` — basis-invariance holds across LEFT/RIGHT as the theme claims.
  - **Verdict**: `supports`.

- **Citation**: `palace/linalg/iterative.cpp:843`
  - **Theme claim**: `x.Add(s[k], Z[k]);` — FGMRES `Z`-basis lift. NOT part of the leaf; second boundary instance grounding basis-lift independence.
  - **Found**: `x.Add(s[k], Z[k]);` at :843 zero-drift. The basis-lift V/Z split is downstream and external to the back-solve body.
  - **Verdict**: `supports`.

### Boundary / context citations

- **Citation**: `palace/linalg/iterative.cpp:612`
  - **Theme claim**: `s[0] = beta;` — RHS seed for the running-QR stream; the back-solve's RHS `s[0..j]` is its rotated descendant.
  - **Found**: `s[0] = beta;` at :612 zero-drift.
  - **Verdict**: `supports`.

- **Citation**: `palace/linalg/iterative.cpp:631`
  - **Theme claim**: `Hj[j + 1] = linalg::Norml2(comm, w);` — the sub-diagonal entry the running-QR stream annihilates; context for upper-triangularity precondition.
  - **Found**: `Hj[j + 1] = linalg::Norml2(comm, w);` at :631 zero-drift. The sole MPI-collective in the upstream pipeline; the back-solve itself has no `MPI_Allreduce` (verified by grep on :650-660 / :830-840 — zero `MPI`/`comm` references).
  - **Verdict**: `supports`.

- **Citation**: `palace/linalg/iterative.cpp:644`
  - **Theme claim**: `converged = (beta < eps);` — the convergence test that exits before the back-solve in the lucky-breakdown / singular-`R` case (applicability boundary).
  - **Found**: `converged = (beta < eps);` at :644 zero-drift. Control-flow traced: the outer-`for(;;)` exit at :645-648 break on `converged`, and the NEXT iteration's seed (`s[0] = beta` at :612) would otherwise overwrite `s[0]`; instead the back-solve at :652-660 runs once on the just-finished restart cycle. The applicability-condition-2 claim ("Palace exits via the convergence test before the back-solve in the lucky-breakdown case") is correctly grounded.
  - **Verdict**: `supports`.

### Register declarations (iterative.hpp)

- **Citation**: `palace/linalg/iterative.hpp:192`
  - **Theme claim**: `mutable std::vector<ScalarType> H;` — the flat register storing the column-major R-factor.
  - **Found**: `mutable std::vector<ScalarType> H;` at :192 zero-drift.
  - **Verdict**: `supports`.

- **Citation**: `palace/linalg/iterative.hpp:193`
  - **Theme claim**: `mutable std::vector<ScalarType> s, sn;` — the RHS / Givens-sine register `s` of element type `ScalarType`.
  - **Found**: `mutable std::vector<ScalarType> s, sn;` at :193 zero-drift.
  - **Verdict**: `supports`.

- **Citation**: `palace/linalg/iterative.hpp:222`
  - **Theme claim**: `class FgmresSolver : public GmresSolver<OperType>` — FGMRES inherits from GMRES.
  - **Found**: `class FgmresSolver : public GmresSolver<OperType>` at :222 zero-drift.
  - **Verdict**: `supports`.

- **Citation**: `palace/linalg/iterative.hpp:250`
  - **Theme claim**: `using GmresSolver<OperType>::H;` — FGMRES inherits the Hessenberg register.
  - **Found**: `using GmresSolver<OperType>::H;` at :250 zero-drift. Grounds Sub-pattern B's identical-`H`-and-`s`-access claim.
  - **Verdict**: `supports`.

- **Citation**: `palace/linalg/iterative.hpp:256`
  - **Theme claim**: `mutable std::vector<VecType> Z;` — FGMRES-specific right-preconditioned-basis register, NOT read by this leaf.
  - **Found**: `mutable std::vector<VecType> Z;` at :256 zero-drift.
  - **Verdict**: `supports`.

### Internal cross-references to L1 leaf

- **Citation**: `book/src/L1/back_solve.md:78` (signature anchor)
  - **Theme claim**: signature `back_solve :: (UpperTri[j+1,j+1], Tensor[j+1]) -> Tensor[j+1]`.
  - **Found**: `back_solve` name at :77, `:: (R: UpperTri[j+1, j+1], s: Tensor[j+1]) -> Tensor[j+1]` at :78. The signature spans :77-78; the theme cites only :78, which is the type-arrow line, NOT the operator name line.
  - **Verdict**: `partially-supports`. Tighten to `:77-78` for precision.

- **Citation**: `book/src/L1/back_solve.md:187-195` (law 1)
  - **Theme claim**: "the defining contract `R · back_solve(R, s) = s` (law 1)".
  - **Found**: Law 1 "Solve inverts apply (the defining contract)." at :187, body extends through :195.
  - **Verdict**: `supports`.

- **Citation**: `book/src/L1/back_solve.md:207-215` (law 4)
  - **Theme claim**: "the back-substitution recurrence (law 4)".
  - **Found**: Law 4 "Back-substitution correctness (descending recurrence)." at :207, body through :215.
  - **Verdict**: `supports`.

- **Citation**: `book/src/L1/back_solve.md:218-221` (law 5)
  - **Theme claim**: "the empty-stream / single-column boundary (law 5)".
  - **Found**: Law 5 "Empty / single-column boundary." header at :217; body :217-221 (so the full law is :217-221).
  - **Verdict**: `partially-supports`. The cited body lines (:218-221) are within law 5 but exclude the header :217. Tighten to `:217-221` for precision.

- **Citation**: `book/src/L1/back_solve.md:223-230` (law 6)
  - **Theme claim**: "basis-lift independence (law 6)".
  - **Found**: Law 6 "Basis-lift independence." at :223, body through :230. **The L1 leaf at :225-226 explicitly says "the GMRES and FGMRES back-solve code is line-for-line identical (`iterative.cpp:652-660` ≡ `:831-840`)"** — this is the precedent prose for the theme's Sub-pattern B narrative and directly contradicts the theme's "+1 line-shift from brace placement" claim.
  - **Verdict**: `supports` (the cross-reference is accurate; the contradiction surfaces inside the theme itself, not in this cross-reference).

- **Citation**: `book/src/L1/back_solve.md:234-243` (reduction-order non-law)
  - **Theme claim**: "the reduction-order non-law".
  - **Found**: "Reduction-order independence of the floating-point result." at :234, body through :243. Cites `L2/incremental-least-squares.md:278-285` for composition with rotation-stream non-associativity — the same composition the theme claims.
  - **Verdict**: `supports`.

- **Citation**: `book/src/L1/back_solve.md:249-254` (singular-`R` applicability boundary)
  - **Theme claim**: "the singular-`R` applicability boundary".
  - **Found**: "Definedness without non-singularity." at :249, body through :254. Cites `iterative.cpp:644` for the exit path — matches the theme's claim.
  - **Verdict**: `supports`.

- **Citation**: `book/src/L1/back_solve.md:330-369` (firm-on-positive-structure status)
  - **Theme claim**: "the firm-on-positive-structure status".
  - **Found**: `## Status` at :330, full rationale through :369. `firm` status with the firm-on-positive-structure rationale matches.
  - **Verdict**: `supports`.

- **Citation**: `book/src/L1/back_solve.md:371-390` (L1 vs L0 distinction)
  - **Theme claim**: "the L1 vs L0 distinction section".
  - **Found**: `## L1 vs L0 distinction` at :371, body through :390.
  - **Verdict**: `supports`.

- **Citation**: `book/src/L1/back_solve.md:466-540` (cycle-028 `verified_against:` block)
  - **Theme claim**: "the cycle-028 `verified_against:` block".
  - **Found**: ` ```yaml ` fence at :466, `verified_against:` keyword at :467, closing ` ``` ` fence at :540. Range :466-540 is correct as the full fenced block.
  - **Verdict**: `supports`.

### Cross-theme / concept anchors

- **Citation**: `book/src/concepts/givens.md:29` ("back_solve via `trsv`" anchor)
  - **Theme claim**: "names the back_solve step 'via `trsv`'".
  - **Found**: `back_solve` keyword anchor at :29 zero-drift.
  - **Verdict**: `supports`.

## Applicability conditions

Each of the theme's six applicability conditions (lines 444-486):

- **Condition 1** ("No observer of the prior `s` value after the call"):
  - **Verifiable**: yes, by control-flow trace. Sole consumers of `s[0..j]` post-back-solve are `:664-666` (LEFT), `:672-675` (RIGHT, into `r`), and `:841-843` (FGMRES) — all consume `s` AS `y` (the back-solve output). No site reads the pre-back-solve RHS values after the back-solve. Found in source.
  - **Found counter-example?**: No.

- **Condition 2** ("`R` square, upper-triangular, non-singular"):
  - **Verifiable**: yes, established by upstream L2 `incremental-least-squares` running-QR stream (annihilates each sub-diagonal via `:631` + plane rotations :634-639); non-singularity guarded by `:644` convergence-exit before the next seed.
  - **Found counter-example?**: No. The lucky-breakdown / exact-convergence path correctly exits before back-solve.

- **Condition 3** ("Tail entry `s[j+1]` (the LS residual) is NOT touched"):
  - **Verifiable**: yes, loop bound `i >= 0` paired with initial `i = j` ensures `s[j+1]` is never touched. `s[j+1]` was consumed at :642 (`beta = std::abs(s[j+1])`) prior to the back-solve.
  - **Found counter-example?**: No.

- **Condition 4** ("Hessenberg register `H` is redundant-on-all-ranks"):
  - **Verifiable**: yes, single-machine target per CLAUDE.md "Scope" makes this automatic; inherited from upstream running-QR stream maintaining `H` identically on every rank.
  - **Found counter-example?**: No. Zero MPI calls in the back-solve range (grep-verified).

- **Condition 5** ("Element type `ScalarType` matches across `R` (in `H`) and `s`"):
  - **Verifiable**: yes, both `H` (:192) and `s` (:193) declared `std::vector<ScalarType>`; bound at solver template instantiation.
  - **Found counter-example?**: No.

- **Condition 6** ("Restart dimension `j+1` is the *active* upper-triangular block, not the allocated `max_dim+1`"):
  - **Verifiable**: yes, outer loop bound walks active columns (`i = j ↓ 0`); stride formula walks allocation. Unused columns `> j` are not read.
  - **Found counter-example?**: No.

All six applicability conditions are complete and verifiable from cited evidence.

## Algebraic laws (per L1 leaf, applied to L0 lowering)

The theme inherits the L1 leaf's six laws and one applicability boundary; the audit checks each against the L0 source:

- **Law 1** (`R · back_solve(R, s) = s`): the lowered code at :656/:659 computes the unique `y` satisfying `R · y = s` by descending back-substitution. **Holds on operators** in exact arithmetic; the L0 source realises it via `s[i] /= Hi[i]` + the descending `s[k] -= Hi[k] * s[i]` recurrence.

- **Law 2** (linearity in RHS): inherited from law-1 unique-inverse structure; not exploited in Palace. **Holds on operators** trivially.

- **Law 3** (compose-with-scale on coefficient): inherited from `(c·R)⁻¹ = c⁻¹·R⁻¹`; not exploited in Palace. **Holds on operators** trivially.

- **Law 4** (back-substitution descending recurrence): the L0 source realises the **column-oriented variant** (eager-subtract `R[k][i]·y[i]` into `s[k]` at outer iteration `i`, not gathered per-row) at :659. Both column-oriented and row-oriented variants compute the same exact-arithmetic `y`. **Holds on operators** in exact arithmetic; the variant choice pins the finite-precision reduction order (recorded as non-law).

- **Law 5** (empty / single-column boundary): empty cycle `j = -1` → outer loop body skips (`:653` condition fails immediately). Single column `j = 0` → outer runs once, inner `k = -1 < 0` skips (`:657` condition fails immediately), reducing to `s[0] /= Hi[0]`. **Holds on operators** in source.

- **Law 6** (basis-lift independence): the back-solve body :653-660 / :832-839 produces `y` in `s[0..j]` with NO read of any basis register (`V` or `Z`); the basis is consumed only by the downstream linear-combination lift at :666 (`V`) / :674 (`V` through `r`) / :843 (`Z`). The two body ranges are **byte-for-byte identical** (verified by `diff` modulo line numbers; this is the L1 leaf's "line-for-line identical" claim — see Finding A below for the theme's contradicting narrative). **Holds on operators** unambiguously.

- **Non-law: reduction-order independence of floating-point result** — pinned by descending column-oriented variant. **Correctly recorded as non-law** in the theme §"Reduction order".

- **Non-law: linearity / structure in `R`** — matrix inversion is nonlinear. **Correctly recorded as non-law** in L1 leaf :244-248.

- **Non-law: definedness without non-singularity** — singular `R` divides by zero at :656. **Correctly recorded as applicability boundary** in L1 leaf :249-254 and theme applicability-condition-2.

All laws hold on the cited L0 operators.

## Findings (named)

### Finding A — Sub-pattern B "+1 line-shift from brace placement" narrative is factually wrong (LOW severity, narrative-only)

**Location**: `book/src/L1-L0/back-solve-mutation-rotation.md:219-229` (the bullet "Brace placement / line shift").

**Theme claim**: "GMRES (Sub-pattern A) places `{` at the end of the `for` line (one statement on the line); FGMRES (Sub-pattern B) places `{` on the next line. This shifts every body line by +1: GMRES :653/:655/:656/:657/:659 ↔ FGMRES :832/:834/:835/:836/:838."

**Found**: Direct read of both ranges shows:
- GMRES :653 `for (int i = j; i >= 0; i--)` → :654 `    {` (own line) → :655 `Hi = ...`.
- FGMRES :832 `for (int i = j; i >= 0; i--)` → :833 `    {` (own line) → :834 `Hi = ...`.

`diff <(cat lines 653-660) <(cat lines 832-839)` returns **zero character differences**. Both methods place `{` on its own line, identically indented. The two back-solve bodies are byte-for-byte identical.

The cited LINE NUMBERS (:653/:655/:656/:657/:659 vs :832/:834/:835/:836/:838) are correct as anchors and the relative intra-block offsets are identical in both blocks (+2/+1/+1/+2 from line-1). The line numbers differ by +179 globally because the methods have different preceding code in their `for(;;)` bodies (Arnoldi orthogonalisation differs, FGMRES has the extra `Z[k] = ApplyB(...)` step at :806, etc.), NOT because of brace style.

**Severity**: low. The error is in the explanatory narrative, not in the cited evidence. The citations are correct; only the explanation for why the lines differ is wrong. The L1 leaf at :225-226 has the correct phrasing: "line-for-line identical". The theme should adopt the same phrasing.

**Repair**: rewrite §"Sub-pattern B" lines 219-229 to: "GMRES and FGMRES back-solve bodies are **line-for-line identical** (byte-for-byte identical text; verified by `diff` modulo absolute line numbers). The GMRES :652-660 and FGMRES :831-840 ranges contain the same comment, the same outer loop, the same own-line `{`, the same stride pointer, the same diagonal division, the same inner loop, and the same column-oriented subtraction. The differing absolute line numbers are an artefact of unrelated preceding code in each method's `for(;;)` body, NOT a brace-style shift. The basis the consumer reads (V vs Z) is the sole content difference, and it lives outside the body."

This repair restores consistency with the L1 leaf and removes the false brace-placement claim. The repair does NOT change the verdict, the firm status, or the law-6 grounding (which is in fact STRONGER under the byte-identical reading than under a brace-shifted reading).

### Finding B — Three minor 1-line off-by-one imprecisions in L1-leaf cross-references (LOW severity, anchor-precision)

**Location**: `book/src/L1-L0/back-solve-mutation-rotation.md:686-694` (L1 cross-anchor bullet list).

The theme cites three L1-leaf anchors at lines that are off-by-one from the most-precise anchor:
- `:78` → tighten to `:77-78` (signature spans both: `back_solve` name on :77, `::`-arrow on :78).
- `:218-221` → tighten to `:217-221` (law 5 header "5. Empty / single-column boundary." at :217; body :218-221).
- `:466-540` → confirm as `:466-540` (correct as the full fenced block; `verified_against:` keyword is at :467 inside the :466 fence).

**Severity**: low. The cited ranges land in the correct semantic region in all three cases; tightening is a precision improvement, not a correctness fix.

**Repair**: bulk-edit the L1 cross-anchor list to use `:77-78`, `:217-221`, `:466-540` (the third was already correct as a range; only the first two need tightening).

### Finding C — every L0 citation is zero-drift on-disk; no anchor repairs needed in the L0 evidence ranges (CONFIRMATION)

**Location**: all 22 L0 anchors in `book/src/L1-L0/back-solve-mutation-rotation.md` (lines 605-682, the "Verified-against" section).

Each citation independently re-verified via `tools/citecheck/citecheck.py --anchor` against on-disk `reference/palace/` this invocation:

```
palace/linalg/iterative.cpp:652  ('Reconstruct the solution')         → 652 OK
palace/linalg/iterative.cpp:653  ('for (int i = j')                    → 653 OK
palace/linalg/iterative.cpp:655  ('H.data() + i * (max_dim + 1)')      → 655 OK
palace/linalg/iterative.cpp:656  ('s[i] /= Hi[i]')                     → 656 OK
palace/linalg/iterative.cpp:657  ('for (int k = i - 1')                → 657 OK
palace/linalg/iterative.cpp:659  ('s[k] -= Hi[k] * s[i]')              → 659 OK
palace/linalg/iterative.cpp:666  ('x.Add(s[k], V[k])')                 → 666 OK
palace/linalg/iterative.cpp:831  ('Reconstruct the solution')         → 831 OK
palace/linalg/iterative.cpp:832  ('for (int i = j')                    → 832 OK
palace/linalg/iterative.cpp:834  ('H.data() + i * (max_dim + 1)')      → 834 OK
palace/linalg/iterative.cpp:835  ('s[i] /= Hi[i]')                     → 835 OK
palace/linalg/iterative.cpp:836  ('for (int k = i - 1')                → 836 OK
palace/linalg/iterative.cpp:838  ('s[k] -= Hi[k] * s[i]')              → 838 OK
palace/linalg/iterative.cpp:843  ('x.Add(s[k], Z[k])')                 → 843 OK
palace/linalg/iterative.cpp:612  ('s[0] = beta')                       → 612 OK
palace/linalg/iterative.cpp:631  ('Norml2(comm, w)')                   → 631 OK
palace/linalg/iterative.cpp:644  ('converged = (beta < eps)')          → 644 OK
palace/linalg/iterative.hpp:192  ('std::vector<ScalarType> H')         → 192 OK
palace/linalg/iterative.hpp:193  ('s, sn')                             → 193 OK
palace/linalg/iterative.hpp:222  ('class FgmresSolver')                → 222 OK
palace/linalg/iterative.hpp:250  ('GmresSolver<OperType>::H')          → 250 OK
palace/linalg/iterative.hpp:256  ('std::vector<VecType> Z')            → 256 OK
```

22/22 L0 citations zero-drift. **The codemap-`read_range` +1 brace-boundary drift hazard flagged in the role spec is NOT present here** — the citecheck-against-on-disk pass agrees with every cited line. The c029 abstractor's `--scan 33/33 anchor zero-drift` claim is independently confirmed.

## Proposed changes

Append the mechanically-fenced `verified_against:` block to the theme file. Note: emitted as a fenced YAML code block per the channel-format requirement (downstream `cross-layer-cross-cutter` parses by fence). One audit row per cited range; the FGMRES Sub-pattern B body anchors carry the `partially-supports` verdict per Finding A with the note pointing at the narrative-repair follow-up (Finding A is narrative-only — the citations themselves are correct, the explanation for the line offset is wrong).

```edit:book/src/L1-L0/back-solve-mutation-rotation.md
[append at end of file]

    verified_against:
      - citation: palace/linalg/iterative.cpp:652
        verdict: supports
        audited_at: 2026-05-30T010118Z
        note: GMRES "Reconstruct the solution" comment; citecheck --anchor zero-drift on-disk.
      - citation: palace/linalg/iterative.cpp:653
        verdict: supports
        audited_at: 2026-05-30T010118Z
        note: GMRES outer descending sweep `for (int i = j; i >= 0; i--)`; empty-cycle (j=-1) skip grounds law 5; zero-drift.
      - citation: palace/linalg/iterative.cpp:655
        verdict: supports
        audited_at: 2026-05-30T010118Z
        note: GMRES column-major stride pointer `Hi = H.data() + i*(max_dim+1)`; transparent allocation trick; zero-drift.
      - citation: palace/linalg/iterative.cpp:656
        verdict: supports
        audited_at: 2026-05-30T010118Z
        note: GMRES diagonal division `s[i] /= Hi[i]` (in-place RHS overwrite, laws 1+4, singular-R divide-by-zero boundary); zero-drift.
      - citation: palace/linalg/iterative.cpp:657
        verdict: supports
        audited_at: 2026-05-30T010118Z
        note: GMRES inner super-diagonal scan `for (int k = i-1; k >= 0; k--)` (empty for i=0, law 5 single-column boundary); zero-drift.
      - citation: palace/linalg/iterative.cpp:659
        verdict: supports
        audited_at: 2026-05-30T010118Z
        note: GMRES column-oriented subtraction `s[k] -= Hi[k] * s[i]` (law-4 transposed-index variant; pins reduction-order non-law); zero-drift.
      - citation: palace/linalg/iterative.cpp:666
        verdict: supports
        audited_at: 2026-05-30T010118Z
        note: GMRES downstream V-basis lift `x.Add(s[k], V[k])` (LEFT branch; RIGHT branch :674 also reads s[k] via r-register; grounds law-6 basis-invariance; NOT part of leaf); zero-drift.
      - citation: palace/linalg/iterative.cpp:831
        verdict: supports
        audited_at: 2026-05-30T010118Z
        note: FGMRES "Reconstruct the solution" comment; byte-for-byte identical to :652; zero-drift.
      - citation: palace/linalg/iterative.cpp:832
        verdict: partially-supports
        audited_at: 2026-05-30T010118Z
        note: FGMRES outer descending sweep `for (int i = j; i >= 0; i--)` zero-drift; but the theme narrative claiming a "+1 line-shift from brace placement" is FACTUALLY WRONG (both GMRES and FGMRES place `{` on its own line; diff of :653-660 vs :832-839 is byte-for-byte zero) — repair follow-up noted; the L1 leaf at :225-226 has the correct "line-for-line identical" phrasing.
      - citation: palace/linalg/iterative.cpp:834
        verdict: supports
        audited_at: 2026-05-30T010118Z
        note: FGMRES column-major stride pointer; byte-for-byte identical to :655; zero-drift.
      - citation: palace/linalg/iterative.cpp:835
        verdict: supports
        audited_at: 2026-05-30T010118Z
        note: FGMRES diagonal division; byte-for-byte identical to :656; zero-drift.
      - citation: palace/linalg/iterative.cpp:836
        verdict: supports
        audited_at: 2026-05-30T010118Z
        note: FGMRES inner super-diagonal scan; byte-for-byte identical to :657; zero-drift.
      - citation: palace/linalg/iterative.cpp:838
        verdict: supports
        audited_at: 2026-05-30T010118Z
        note: FGMRES column-oriented subtraction; byte-for-byte identical to :659; zero-drift.
      - citation: palace/linalg/iterative.cpp:843
        verdict: supports
        audited_at: 2026-05-30T010118Z
        note: FGMRES downstream Z-basis lift `x.Add(s[k], Z[k])` (second boundary instance grounding law-6 V/Z basis split; NOT part of leaf); zero-drift.
      - citation: palace/linalg/iterative.cpp:612
        verdict: supports
        audited_at: 2026-05-30T010118Z
        note: RHS seed `s[0] = beta` (s = beta_0 e_1); back-solve RHS s[0..j] is its Givens-rotated descendant; zero-drift.
      - citation: palace/linalg/iterative.cpp:631
        verdict: supports
        audited_at: 2026-05-30T010118Z
        note: 'sub-diagonal `Hj[j+1] = Norml2(comm, w)` the running-QR stream annihilates (sole MPI-collective in upstream; back-solve itself has zero MPI calls — grep-verified on :650-660 / :830-840); zero-drift.'
      - citation: palace/linalg/iterative.cpp:644
        verdict: supports
        audited_at: 2026-05-30T010118Z
        note: convergence test `converged = (beta < eps)`; control-flow traced (outer :645-648 break before next-restart-cycle seed :612), so lucky-breakdown singular-R back-solve is unreachable; applicability-condition-2 complete; zero-drift.
      - citation: palace/linalg/iterative.hpp:192
        verdict: supports
        audited_at: 2026-05-30T010118Z
        note: flat column-major Hessenberg register `mutable std::vector<ScalarType> H`; zero-drift.
      - citation: palace/linalg/iterative.hpp:193
        verdict: supports
        audited_at: 2026-05-30T010118Z
        note: RHS / Givens-sine register `mutable std::vector<ScalarType> s, sn`; grounds element-type axis with H :192; zero-drift.
      - citation: palace/linalg/iterative.hpp:222
        verdict: supports
        audited_at: 2026-05-30T010118Z
        note: FgmresSolver inherits from GmresSolver — grounds Sub-pattern B identical-register-access claim; zero-drift.
      - citation: palace/linalg/iterative.hpp:250
        verdict: supports
        audited_at: 2026-05-30T010118Z
        note: FGMRES `using GmresSolver<OperType>::H;` — inherited Hessenberg register confirms FGMRES back-solve reads the same H slab as GMRES; zero-drift.
      - citation: palace/linalg/iterative.hpp:256
        verdict: supports
        audited_at: 2026-05-30T010118Z
        note: FGMRES-specific `mutable std::vector<VecType> Z;` right-preconditioned-basis register; NOT read by the back-solve body (basis-lift independence boundary); zero-drift.

NOTE TO INTEGRATOR: the `verified_against:` payload above is rendered as a 4-space-indented code block (per skill `convert-nested-fences-to-indented-code-in-proposed-changes-block`, option (b)) so it does not toggle the enclosing `edit:` fence. When materialised in the target chapter file, the integrator should re-fence the payload as a top-level ` ```yaml … ``` ` block (channel-format requirement: downstream `cross-layer-cross-cutter` parses the chapter file by fence). The payload content is the entire 4-space-indented YAML block above, with the leading 4 spaces stripped per line.
```

(The proposed-changes block above uses 4-space-indented code rather than a nested ` ```yaml ` fence to avoid mis-toggling the outer ` ```edit:… ` fence under CommonMark — per skill `convert-nested-fences-to-indented-code-in-proposed-changes-block`. The downstream `cross-layer-cross-cutter` parses the chapter file by fence; the integrator re-fences the payload as a top-level ` ```yaml … ``` ` in the landed chapter. The audit is `partially-supports` overall due to Finding A; the citations themselves are all `supports` or `partially-supports` zero-drift on-disk.)

### Follow-up: narrative repair for Sub-pattern B (lifter / abstractor reread, NOT this audit)

The factually-wrong "+1 line-shift from brace placement" narrative at theme
lines 219-229 should be repaired by a lifter or abstractor follow-up to match
the L1 leaf's correct "line-for-line identical" phrasing. The text repair
proposed in Finding A above can be applied verbatim. This is a narrative-prose
repair, not a citation-evidence repair — the audit per-citation verdicts
above stand on their own; the prose repair is downstream housekeeping.

Open question to file (cycle-030 OQ ledger):
`back-solve-mutation-rotation-subpattern-b-narrative-repair` — Sub-pattern B
narrative attributes the GMRES↔FGMRES line offset to brace style, but both
methods place `{` on its own line and the bodies are byte-for-byte identical;
the L1 leaf at :225-226 has correct phrasing. Schedule a lifter or
small-scope abstractor reread to apply the proposed text in Finding A. Low
fan-out (cosmetic / consistency); ties to the basis-lift independence
grounding.

### Follow-up: anchor-precision repair for three L1 cross-references (mechanical lift / repairer)

The three off-by-one anchor imprecisions in §Verified-against L1 cross-anchor
list (Finding B) — `:78` → `:77-78`, `:218-221` → `:217-221`, `:466-540`
correct-as-is — are bulk-editable in one pass. Mechanical; appropriate for a
repairer or lifter pass during a future cycle.

## Supporting evidence

Files consulted (all read this invocation):

- `book/src/L1-L0/back-solve-mutation-rotation.md` (the audited theme, full read).
- `book/src/L1/back_solve.md` (the firm L1 leaf, full read; cycle-028 audited).
- `reports/2026-05-29T205945Z-abstractor-back-solve-mutation-rotation/CYCLE.md` (cycle-029 dispatch-1 abstractor report; full read for context).
- `reference/palace/palace/linalg/iterative.cpp:603-680` (GMRES outer loop + back-solve + downstream basis-lift, full read via citecheck `--show`).
- `reference/palace/palace/linalg/iterative.cpp:828-846` (FGMRES back-solve + downstream basis-lift, full read).
- `reference/palace/palace/linalg/iterative.hpp:192-256` (registers + FGMRES class declaration, individual line-anchor reads).
- `tools/citecheck/citecheck.py` (used 27 times in this invocation, all `--anchor` checks against on-disk).
- `diff` on `iterative.cpp:653-660` vs `:832-839` body text (zero character differences confirmed).
- `grep -n -i 'mpi\|allreduce\|comm'` on `iterative.cpp:650-660 / :830-840` (zero matches confirmed for the no-MPI claim).

## Open questions / caveats

1. **Sub-pattern B narrative repair** (Finding A): the "+1 line-shift from brace placement" claim is factually wrong. Filed as OQ `back-solve-mutation-rotation-subpattern-b-narrative-repair` for cycle-030+ lifter/abstractor follow-up. The repair text is in Finding A; it is a 10-line prose substitution. The audit per-citation verdicts stand independently; the prose fix is downstream housekeeping that strengthens (rather than weakens) the law-6 grounding.

2. **L1-leaf cross-anchor precision** (Finding B): three 1-line off-by-one anchor imprecisions in the §Verified-against L1 cross-reference list. Bulk-editable; appropriate for a repairer or lifter pass. Low priority.

3. **No drift detected in the L0 evidence ranges** — the codemap +1 brace-boundary hazard the role spec flagged does NOT manifest here. Every cited L0 line is on-disk where the theme says it is, per `citecheck --anchor`. The c029 abstractor's `--scan 33/33 zero-drift` claim is independently re-confirmed.

4. **No status reduction needed.** The theme's `firm` status is correct: every law of the L1 leaf is operator-algebra on the cited positive source, no convergence-semantics dependency, no negative-anchor reconstruction. The firm-on-positive-structure rationale (matching the `lu-solve-mutation-rotation` sibling and the `apply_linop` precedent) is sound. The narrative error in Finding A is in the explanatory prose, NOT in the citations or the algebraic claims.

5. **No new sibling-slice / inherited-precedent re-anchor sub-case triggered** — the audit did not inherit citations from a sibling-theme without independent verification. The theme's references to `lu-solve-mutation-rotation` and `matrix-weighted-norm-mutation-rotation` are pattern/precedent references (not citation inheritance); no cross-theme re-anchoring is needed.

6. **`apply_linop` / `lu_solve` firm-on-positive-structure precedent confirmed** — the audit confirms this theme follows the same pattern: laws are syntactic identities on fully-specified positive source, no test dependency, no constructive sub-part needing negative-anchor backing. The `firm` (not `rough-in (test-coverage-bounded)`, not `partly-constructive`) status is correct per the CLAUDE.md "Two rough-in qualifiers" invariant's firm-on-positive-structure escape.
