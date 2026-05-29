---
verifies: ./CYCLE.md
critiqued_at: 2026-05-29T04:04:10Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-29T04:20:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "L1>L0 theme sketch — assemble-diagonal-mutation-rotation"

## Critique

### Checks run

**citation-validity — warning.** I independently re-read every cited L0 range via
`palace-codemap read_range` against `reference/palace/` and verified line-exactness.
The large majority resolve exactly. **Confirmed-exact** (range + the report's
internal narrow attributions): `operator.hpp:21` (`using Operator = mfem::Operator;`),
`operator.hpp:50-51` (`// Diagonal assembly.` + abstract complex decl @51),
`operator.hpp:97` (`ComplexWrapperOperator::AssembleDiagonal` decl),
`operator.cpp:25-28` (base `MFEM_ABORT` @27), `operator.cpp:85-96`
(`ComplexWrapperOperator::AssembleDiagonal`; `diag = 0.0` @87, real @88-91, imag @92-95),
`hypre.cpp:85-89` (`SetSize(height)` @87, `hypre_CSRMatrixExtractDiagonal` @88),
`hypre.hpp:70`, `libceed/operator.cpp:116-143` (square `MFEM_VERIFY` @120, `diag = 0.0`
@121, `CeedOperatorLinearAssembleAddDiagonal` @139), `libceed/operator.hpp:56`,
`rap.cpp:154-193` (RAP-delegate @157-161, convergent comment @163-164, square verify
@165-166, `A->AssembleDiagonal(lx)` @168, DiagonalPolicy DIAG_ONE/DIAG_ZERO @180-191),
`rap.cpp:467-479` (`diag = 0.0` @470, real @471-474, imag @475-478), `rap.hpp:112`,
`rap.hpp:206`, `jacobi.cpp:79-80` (`SetSize` @77, `AssembleDiagonal` @79, `Reciprocal`
@80), `jacobi.hpp:15-16` (the "(approximate) diagonal construction for matrix-free
operators" comment, quoted verbatim and accurate), `chebyshev.cpp:177-178`,
`chebyshev.cpp:240-241`. The enclosing test range `test-libceed.cpp:343-376` is correct
and all the matched constructs (the `op_test->AssembleDiagonal` compare, the `rtol`
relaxation, the `ND_FECollection`/`GetOrder()>1`/`!UsesTensorBasis` guard) genuinely
exist. However four **narrow line attributions** are off (the surrounding ranges remain
in-range, so these are precision-of-attribution defects, not unsupported-claim defects) —
see Issues 1–4.

**surface-or-evidence — pass.** This is a refinement-shaped proposal that authors a NEW
surface (a fresh `L1-L0/assemble-diagonal-mutation-rotation.md` file with four rewrite
sub-patterns + a domain-boundary abort + a load-bearing non-law) AND carries
rotation/lowering evidence — it is not a pure rotation_claim. The load-bearing
approximate-matrix-free-diagonal non-law is the focus of the adversarial firm-vs-
partly-constructive question, and the `firm` (not `partly-constructive`) status holds:
the caveat is **positively anchored** in three real Palace sites — a positive comment at
`jacobi.hpp:15-16` ("(approximate) diagonal construction for matrix-free operators",
verified verbatim), a positive comment at `rap.cpp:163-164` (the convergent-diagonal
note, verified), and a positive test that exercises the property by relaxing its
tolerance for it at `test-libceed.cpp` (the `rtol = 1.0` branch, verified to exist). Per
the CLAUDE.md `partly-constructive` invariant, that status is reserved for a *constructive
sub-part* materialized from **negative anchors / literature** absent a positive Palace
site. Here the caveat is a load-bearing **non-law on an otherwise-exact rewrite** read
from positive sites, not a constructed sub-part — so `partly-constructive` does NOT apply
and `firm` is correct. I cross-checked the L1 anchor (`L1/assemble-diagonal.md` line 93):
the entry takes the identical posture (records the caveat as a non-law, not a status
reduction), so the theme's status reasoning is faithful to its anchor.

**rotation-quality — pass.** The rotation is genuine high→low (L1 pure form
`assemble_diagonal(A) -> diag` lowers into the L0 in-place `A.AssembleDiagonal(diag)`
out-parameter family). The L1 form is strictly more compact: it drops the destination
buffer, the sizing (`SetSize`), the zero-init (`diag = 0.0`), the workspace (AMR `lx`),
the absolute-value-prolongation assembly, the OpenMP region, and the Dirichlet
`DiagonalPolicy` step, and collapses four concrete representations into one opaque
`LinearOperator[N,N]`. This is state-hiding + representation-collapse, not a 1:1 rename.
The "operator-to-data materialization under out-parameter mutation" framing is correctly
distinguished from the in-place axpby family (which threads through vector operands) and
from `apply_linop` (operator-AND-vector-to-vector action vs operator-alone-to-data); the
distinction "no input vector; output is operator-intrinsic data" is precise and load-bearing.

**variant-axis-coverage — pass.** The orthogonal axis (element-type real/complex) is
covered: real path (sub-patterns A/B/C) and complex path (sub-pattern D, two witnesses:
`ComplexWrapperOperator` and `ComplexParOperator`). The operator-representation axis is
correctly stated as absorbed at L1 and surfaced here as four L0 sub-patterns (sparse-CSR /
matrix-free / parallel-AMR / complex-wrapped), exhaustively cited. The non-axes are
explicitly scoped out with justification: transpose-mode (diagonal is transpose-invariant,
no `AssembleDiagonalTranspose` exists), accumulate-mode (`AssembleDiagonal` always
materializes the full diagonal, no `AddMult`-style variant), abs-vs-signed (the abs is on
the prolongation, not the diagonal entries — output retains sign). All three non-axis
claims match the L1 entry's own non-laws (verified against `L1/assemble-diagonal.md`
lines 57, 87, 88). No hidden branches: the base-class abort is explicitly handled as
sub-pattern E (domain boundary, not a variant). The RAP-delegate fast path is noted and
flagged for lowering-verifier follow-up (OQ) rather than silently dropped.

**cross-reference-integrity — pass.** The L1 anchor `L1/assemble-diagonal.md` exists
(firm, cycle-019). The sibling `L1-L0/apply-linop-mutation-rotation.md` exists, and the
operator/data divide is correctly stated against it. The proposed new file
`L1-L0/assemble-diagonal-mutation-rotation.md` correctly does NOT yet exist (fresh-file
proposal, not a stub promotion). The forward-references `reciprocal` / `elementwise_product`
are kept plain-text (no live link) per the `rough-in-rows-must-be-plain-text-when-anchor-
missing` convention — correct, those L1 primitives are not authored. The upstream-MFEM
dependency is handled per scope: the theme cites the Palace alias
(`operator.hpp:21`) and the Palace concrete overrides, NOT MFEM internals, and logs the
dependency as an OQ. The in-file relative links (`./apply-linop-mutation-rotation.md`,
`../L1/assemble-diagonal.md`) resolve.

**edge-label-fidelity — pass.** The declared edge is L1>L0 throughout — frontmatter scope,
title, the "L1 form (LHS)" / "L0 form (RHS)" headings, and the prose all discuss exactly
the L1→L0 lowering. No edge-label/prose mismatch.

**plan-kind-consistency — pass.** Declared kind is a `firm` L1>L0 theme. The content
matches: four exhaustively-cited rewrite sub-patterns + a domain-boundary marker + a
positively-anchored load-bearing non-law, with per-sub-pattern justification kinds
(structural ×3, algebraic ×1, obstruction ×1). The proposed-changes are well-formed: a
new-file `edit:` block, a one-row dep-map append to `L1-L0/index.md` (anchor "after the
nrm2-mutation-rotation row (line 27)" — verified nrm2 is at index.md line 27), and a
SUMMARY.md chapter register (anchor "after the nrm2-mutation-rotation line (line 83)" —
verified nrm2 is at SUMMARY.md line 83). No rough-in placeholders in a firm entry.

**skill-uptake-survey — warning.** The report's shape (a fresh refinement-surface theme
asserting a rotation, carrying a load-bearing non-law, with citation ranges the report
claims to have "verified by direct read") implies several relevant skills exist —
`verify-rotation-citation`, `verify-refinement-surface`, `verify-citation-range` (whose
"inherited-citation sub-case" is directly on point given the `:172` inheritance below),
and `propose-rotation`. The report's prose asserts verification ("verified by direct
`read_range` during this dispatch") but does not reference invoking any named skill. Pure
telemetry surface, non-blocking — but the inherited mis-attribution (Issue 1) is exactly
the failure mode `verify-citation-range`'s inherited-citation sub-case is meant to catch,
so its non-invocation is worth flagging.

### Issues found

1. **`AbsMultTranspose` cited at `:172`, actually at `:174` (off by 2).** Location:
   CYCLE.md frontmatter input (line 14, "`AbsMultTranspose` :172"); sub-pattern C
   citations (line 209, "the absolute-value-prolongation transpose `hP->AbsMultTranspose
   (1.0, lx, 0.0, diag)` (line 172)"); verified-against note (line 514). Independent read
   of `rap.cpp:170-175`: line 172 = `if (const auto *hP = dynamic_cast<const
   mfem::HypreParMatrix *>(P))`, line 173 = `{`, line 174 = `hP->AbsMultTranspose(1.0, lx,
   0.0, diag);`. The `:172` attribution points at the `dynamic_cast` guard, not the call.
   Severity: **low-medium** — the enclosing range `rap.cpp:154-193` is correct and the
   construct genuinely exists, so the claim is supported; only the narrow line number is
   wrong. **Note (inherited):** this exact error is present in the L1 anchor
   `L1/assemble-diagonal.md` (line 111 also cites `AbsMultTranspose` "at line 172"); the
   theme inherited it rather than re-verifying. Fixing it here without fixing the L1 entry
   leaves the anchor inconsistent — worth surfacing to the integrator/repairer that the L1
   entry carries the same defect.

2. **`rtol = 1.0e-12` cited at `:363`, actually at `:360` (off by 3).** Location:
   CYCLE.md line 360-361 ("reproduces `mfem::SparseMatrix::GetDiag` to `rtol = 1.0e-12`
   in general (line 363)"); verified-against note line 538 ("rtol=1.0e-12 general (:363)").
   Independent read: `double rtol = 1.0e-12;` is at `test-libceed.cpp:360`; line 363 is
   `const auto &trial_fec = trial_fespace.GetFEColl();`. Severity: **low** — in-range of
   the cited block `343-376`; narrow attribution wrong.

3. **`rtol = 1.0` cited at `:372`, actually at `:371` (off by 1).** Location: CYCLE.md
   line 362 ("`rtol = 1.0` at line 372"); verified-against note line 538 ("rtol=1.0 at
   :372"). Independent read: `rtol = 1.0;` is at `test-libceed.cpp:371`; line 372 is the
   closing `}` of the relaxation branch. Severity: **low** — in-range; off by one.

4. **High-order-Nedelec condition range `:367-374` loosely bounds the construct.**
   Location: CYCLE.md frontmatter (line 19, ":367-374"), sub-pattern B / non-law section
   (line 360-362, "the `ND_FECollection` + `GetOrder() > 1` + `!UsesTensorBasis` condition,
   lines 367-374"), and the OQ. Independent read: the `if` guard spans lines 365-369, the
   `rtol = 1.0;` assignment is at 371, and line 374 is the **commented-out** `// REQUIRE
   (d_ref * d_ref > 0.0);` line (not part of the condition). The range `:367-374` starts in
   the middle of the trial-fec clause and ends on an unrelated commented line. Severity:
   **low** — the described construct exists within `343-376`; the sub-range is imprecise
   (it omits the start of the guard at 365-366 and overshoots into the commented REQUIRE).

5. **Index/SUMMARY anchor line numbers are correct at critique time but positional.**
   Location: CYCLE.md proposed-changes (lines 542, 548). The `L1-L0/index.md` "line 27"
   and `SUMMARY.md` "line 83" anchors both currently resolve to the nrm2-mutation-rotation
   row/line as claimed (verified). Severity: **informational** — not a defect now, but the
   anchors are line-number-positional; if another report integrates ahead of this one in
   the same cycle and shifts those files, the line numbers drift. The textual anchor ("after
   the nrm2-mutation-rotation row/line") is robust and should be the integrator's guide.

6. **Self-asserted "verified by direct read_range this cycle" does not exempt the inherited
   `:172`.** Location: CYCLE.md "Verified-against" (line 411-412) and "Supporting evidence"
   (line 566-567) both claim all ranges were verified by direct `read_range` this dispatch.
   The `:172` (Issue 1), `:363` (Issue 2), and `:372` (Issue 3) attributions contradict
   that claim — either the read was at range granularity (not line granularity) or the
   narrow attributions were copied from the L1 entry without per-line re-confirmation.
   Severity: **low-medium** — the verification-claim is overstated relative to the
   line-precision actually achieved; the underlying constructs are all present, so no claim
   is unsupported, but the "verified" framing should be read as range-verified, not
   line-verified.

## Repair

### Fixes attempted

- **Finding 1**: `AbsMultTranspose` cited `:172`, actually `:174` (off by 2).
  - **Decision**: repaired.
  - **Action**: re-read `rap.cpp:168-178` via `palace-codemap read_range` —
    `A->AssembleDiagonal(lx)` @168, the `dynamic_cast<const mfem::HypreParMatrix *>`
    guard @172, `hP->AbsMultTranspose(1.0, lx, 0.0, diag);` @174 confirmed.
    Corrected all four `:172` occurrences in CYCLE.md to `:174`:
    (a) frontmatter input list (line 14),
    (b) sub-pattern C citation inside the proposed-changes `edit:` block
    (`book/src/L1-L0/assemble-diagonal-mutation-rotation.md` §Sub-pattern C citations),
    (c) Summary-section "Verified-against" L0-evidence note (rap.cpp:154-193 note),
    (d) frontmatter "Status" `verified_against` YAML note for `rap.cpp:154-193`.
  - **Inherited-citation follow-up (note for integrator, NOT applied here)**: per the
    critic (Issue 1), this exact `:172` error is *inherited from the L1 anchor*
    `book/src/L1/assemble-diagonal.md` (its line ~111 cites `AbsMultTranspose` "at line
    172" with the same off-by-2). The repairer does NOT edit `book/`. The L1 entry
    should receive the identical `:172 → :174` correction in a future touch so the anchor
    and the theme stay consistent. **Routed as an OQ/follow-up** — see "Unrepairable
    findings" below. This is the failure mode `verify-citation-range`'s
    inherited-citation sub-case is meant to catch (the theme copied the anchor's narrow
    attribution rather than re-verifying it).

- **Finding 2**: `rtol = 1.0e-12` cited `:363`, actually `:360` (off by 3).
  - **Decision**: repaired.
  - **Action**: re-read `test/unit/test-libceed.cpp:358-376` — `double rtol = 1.0e-12;`
    @360; line 363 is `const auto &trial_fec = trial_fespace.GetFEColl();` (confirms the
    critic). Corrected `:363 → :360` in: the load-bearing-non-law section inside the
    proposed-changes `edit:` block (line 360 prose), the frontmatter input list (line 19),
    and the `verified_against` YAML note for `test-libceed.cpp:343-376`.

- **Finding 3**: `rtol = 1.0` cited `:372`, actually `:371` (off by 1).
  - **Decision**: repaired.
  - **Action**: re-read confirmed `rtol = 1.0;` @371; line 372 is the closing `}` of the
    relaxation branch. Corrected `:372 → :371` in the proposed-changes `edit:` block prose,
    the frontmatter input list, the Summary-prose test-relaxation reference, the
    "Verified-against" / "Supporting evidence" notes, and the `verified_against` YAML note.

- **Finding 4**: ND_FECollection condition range `:367-374` loosely bounds.
  - **Decision**: repaired.
  - **Action**: re-read confirmed the `if` guard spans `:365-369`
    (`if (trial_fespace.Dimension() == 3 && ...))`), the `rtol = 1.0;` assignment is @371,
    and `:374` is the **commented-out** `// REQUIRE(d_ref * d_ref > 0.0);` (not part of
    the condition). Tightened every `:367-374` reference to the precise pair
    "condition `:365-369`, assignment `:371`" (the prior range both started mid-guard at
    367 and overshot into the commented REQUIRE at 374). Updated: proposed-changes `edit:`
    block prose, Summary prose, frontmatter input list, "Verified-against" L0-evidence
    note, "Supporting evidence" note, and the `verified_against` YAML note.

- **Finding 5 [skill-uptake-survey]**: telemetry-only warning.
  - **Decision**: not-needed.
  - **Rationale**: pure telemetry surface, explicitly non-blocking per the critic. No
    artifact/report defect to fix. The substantive half of the critic's skill-uptake note
    (the non-invocation of `verify-citation-range`'s inherited-citation sub-case allowed
    the `:172` drift through) is *addressed in substance* by the Finding-1 repair + the
    inherited-L1 follow-up note; nothing further for the repairer to apply in this report.

### Unrepairable findings

- **Inherited `:172` defect in the L1 anchor `book/src/L1/assemble-diagonal.md`**
  (raised by critic Issue 1; surfaced by the Finding-1 repair).
  - **Why out of repair scope**: the repairer does not edit `book/`. This is an artifact
    edit to a *different, already-integrated* firm entry, not a fix to this report.
  - **Follow-up routing**: `follow_up_agent: null` — this does NOT block `ready` for THIS
    report (the report's own citations are now correct). It is routed to the integrator as
    an OQ/future-touch: when the L1 entry is next touched, apply the same
    `AbsMultTranspose :172 → :174` correction (`book/src/L1/assemble-diagonal.md`, the line
    near :111 citing "line 172"). Suggest the integrator-per-report append an OQ to
    `scaffolding/open-questions.md` recording this inherited-anchor drift so a future
    `lifter`/`lowering-verifier`/harvester touch on `L1/assemble-diagonal` closes it.

### Skill candidate observed

The four narrow-attribution drifts in this report all share one shape: a theme **inherited**
its anchor's narrow line attributions (the L1 entry's `:172`, and the test-relaxation
line numbers) without per-line re-verification against source — exactly the failure mode the
critic flagged under skill-uptake. The repair is mechanical and identical each time
(re-read the range, snap each narrow attribution to its true line). This is at least the
recurrence the `verify-citation-range` "Audit-report / inherited-citation sub-case" already
names; no new skill proposed (the existing skill covers it), but worth a note that
producers inheriting from a firm anchor should re-run that sub-case rather than trusting the
anchor's line numbers. Not appended to `skill-candidates.md` (existing skill already covers
the pattern); recorded here for the meta-phase's friction window.

## Suggested resolution

`overall_status: ready`. All four narrow-attribution citation drifts (the only
citation-validity defects) are mechanically corrected in CYCLE.md, including inside the
proposed-changes `edit:` block so the corrected line numbers land in the artifact at
integration. The `firm` status (adversarially re-checked by the critic and HOLDS — the
approximate-matrix-free non-law is positively anchored, not a `partly-constructive`
reconstruction) is unaffected. The `skill-uptake-survey` warning is telemetry-only.

Note for the integrator: the inherited `:172` defect in the *already-integrated* L1 anchor
`book/src/L1/assemble-diagonal.md` is NOT fixed by this repair (repairer does not touch
`book/`); the integrator should append an OQ so the same `:172 → :174` correction is applied
on the L1 entry's next touch. This does not block applying this report.
