---
verifies: ../REPORT.md
critiqued_at: 2026-05-28T22:30:00Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-28T23:05:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of L1>L0 theme — divfree-projector-mutation-rotation

## Critique

### Checks run

**citation-validity — warning.** I independently verified every cited range
against `reference/palace/` source (Read on the actual files, not inherited from
the report). The **headline / load-bearing citations are all exact and the
report's self-reported corrections are correct**:

- Sub-pattern A apply: `divfree.cpp:155` (sig), `:156` (open brace), `:187`
  (close brace) — the "corrected from `:155-186`" claim is **right**; the L1
  entry's `:155-186` genuinely undershoots the close brace by one (independently
  confirmed: source close brace is `:187`, `template class DivFreeSolver<Vector>;`
  at `:189`).
- The four step ranges are **all exact**: step 1 `:159-168` (complex Re/Im
  `:162-163`, real `:167`), step 2 `:170-174` (`SetSubVector` at `:173`), step 3
  `:175` (`ksp->Mult(rhs, psi)`), step 4 `:177-186` (complex `:180-181`, real
  `:185` with `1.0`).
- The CG-tol corrections are **exact and verified**: `SetRelTol(tol)` is at
  `:141` (the report's correction), `:140` is `SetInitialGuess(false)`,
  `SetAbsTol(epsilon())` is at `:142` (confirmed). The report's OQ
  `divfree-l1-entry-apply-close-and-reltol-line-drift` is **well-founded**: I
  confirmed the firm L1 entry `book/src/L1/divfree-projector.md` does cite the
  apply as `:155-186` (lines 14/122/237/301) and rel-tol at `:140` (line 179).
- The load-bearing sign sub-note is **rock-solid**: `integrator.hpp:217`
  (`a(u, v) = -(Q u, grad v)` comment) exact; `MixedVectorWeakDivergenceIntegrator`
  class `:218-226` exact; `mixedvecgrad.cpp:202` `PopulateCoefficientContext(...,
  -1.0)` exact; sibling-contrast `:142` (no `-1.0`) exact; `:23` and `:148`
  Assemble-body openings exact.
- hpp: `:55` (`mutable VecType psi, rhs;`), `:63-66` (`Mult(VecType&)` decl +
  doc), `:68-72` (`Mult(const VecType&, VecType&) { y=x; Mult(y); }`), `:28-31`
  (class doc `Gᵀ M x = 0`) — **all exact**.
- `vector.hpp:221` (`SetSubVector(..., double s)` scalar-fill), `operator.hpp:133`
  (`AddMult(..., a = 1.0)`), `eigensolver.cpp:262` (`divfree->Mult(v0)`),
  `arpack.cpp:586` (`opProj->Mult(y1)`), `test-libceed.cpp:905-916` (MFEM
  cross-validation) — **all exact**.

The warning is for a **systematic off-by-one-to-two drift in the parenthetical
`@:NN` sub-line pin-points inside Sub-pattern C's Citations block** (lines
261-287 of CYCLE.md). The *outer block ranges* there (`:51-81`, `:84-110`,
`:111-116`, `:120-146`, `:148-151`) are correct or near-correct and enclose the
cited elements, but the inline `@:NN` element annotations drift below the true
source lines. See Issues found for the enumerated list. This is the same drift
class as batch-3's producer-citation-drift friction; it is in low-stakes
construction-site scaffolding (not the load-bearing apply or sign), so warning
rather than fail.

**surface-or-evidence — pass.** This is a NEW theme proposal (a fresh
`book/src/L1-L0/divfree-projector-mutation-rotation.md` entry), not a refinement
of an existing theme. It modifies surface (the new theme file + index.md row +
SUMMARY.md row) and carries L0 rotation evidence for every sub-pattern. The
check's refinement-vs-backfill axis is satisfied by the surface-modifying branch.

**rotation-quality — pass.** The theme asserts a structural mutation rotation
(L1 pure out-of-place `y' = divfree_project(P, y)` ⟸ L0 in-place
`DivFreeSolver::Mult(VecType &y)` with output-arg mutation, scratch-member
threading, construction-bound closure-field reads). The L1 form is strictly more
compact / more abstract: it hides the `psi`/`rhs` scratch ownership, the
destination-arg mutation, the `VecType` template dispatch, and the
construction-bound closure into a single value-producing action over an opaque
`P`. This is genuine state-hiding + threaded-state compression, not a 1:1
rename. The 4 sub-patterns each name a distinct erasure (dest-arg, scratch,
closure, element-type). Pass.

**variant-axis-coverage — pass.** Two orthogonal variant axes are present and
both are covered, not hidden: (i) in-place vs out-of-place entry — sub-pattern A
(`Mult(y)`) and sub-pattern B (`Mult(x, y)` = copy-then-apply) both authored;
(ii) real vs complex element type — sub-pattern D (`VecType ∈ {Vector,
ComplexVector}`, the `if constexpr` Re/Im split, instantiations `:189-190`)
explicitly covered. The empty-boundary synthetic-pin branch (`:51-81`) and the
GMG-depth>1 vs BoomerAMG-depth-1 preconditioner branch (`:124-132` vs `:120-122`)
are both surfaced in sub-pattern C. Single-machine MPI scope-out is flagged
(Applicability condition 7). No hidden branches found.

**cross-reference-integrity — warning.** All theme/operator/concept slug links
resolve: the L1-L0 sibling links (`apply-linop-`, `chebyshev-smoother-`,
`ksp-solve-`, `eigsolve-mutation-rotation.md`) exist; the L1 anchors
(`divfree-projector.md`, `apply_linop.md`, `axpy.md`, `ksp_solve.md`) exist; the
concepts (`set_subvector_zero.md`, `constructed-operator-factory.md`) exist; the
proposed index.md row anchors on the existing line-24 chebyshev row and the
SUMMARY.md L1-L0 section exists. The warning is one **dangling section-anchor
reference**: the theme cites `[L1/divfree-projector](../L1/divfree-projector.md)
§Variant axes` (CYCLE.md lines 320-321), but the L1 entry has **no `## Variant
axes` heading** — it only has an inline "see Variant axes" pointer at its line
43 (itself dangling). This is an **inherited** dangling pointer (the L1 entry has
the same defect), not introduced by this report, but the theme propagates it. See
Issues found.

**edge-label-fidelity — pass.** The theme is labelled L1>L0 throughout
(slug, frontmatter scope, index.md row, "Narrated forward: the L1 pure
out-of-place projection dissolves into the L0 ... mutation idiom"). The LHS is
consistently the L1 `divfree_project` form, the RHS is consistently the L0
`DivFreeSolver` source; the prose narrates exactly the L1→L0 lowering direction.
The reverse-direction lifting note is correctly quarantined to "Open questions /
caveats" working notes per the high→low invariant. No edge mismatch.

**plan-kind-consistency — pass.** Declared status `firm`. The firm claim is
justified under the project's firmness bar: every sub-pattern reads from a
positive Palace source site (all independently re-verified above), the L1 anchor
is firm (promoted cycle-015 per OQ `divfree-projector-partly-constructive-to-firm-enactment`),
and the single load-bearing algebraic sub-note (the `WeakDiv = -Gᵀ` sign) is
**positively anchored** (`integrator.hpp:217` + `mixedvecgrad.cpp:202`, with the
non-negated sibling `:142` as contrast) — exactly the promotion condition that
the cycle-013 `partly-constructive` adjudication required, now satisfied. The
report correctly distinguishes this from the `eigsolve-mutation-rotation`
`partly-constructive` case (negative-anchor reconstruction) and explicitly states
"No partly-constructive caveat applies." No rough-in placeholders in a firm
entry. Content shape matches declared kind.

**skill-uptake-survey — pass.** Pure presence check; non-blocking. The report's
shape (an abstractor authoring an L1>L0 theme with heavy citation verification)
implies `verify-citation-range` and `verify-rotation-citation` as relevant. The
report references `palace-codemap` `read_range` / `search_text` / `get_symbol_def`
invocation throughout (frontmatter "codemap-verified this cycle", Verified-against
header, Supporting evidence §) — the localization-skill uptake is documented.
`verify-citation-range` is not named by slug, but the procedure (per-range
read-back with brace/line confirmation) is visibly exercised. Telemetry: codemap
uptake strong; named-skill-by-slug uptake weak but the equivalent procedure ran.

### Issues found

1. **[low — citation-validity] Sub-pattern C MPI-pin sub-line drift.** CYCLE.md
   §"Sub-pattern C ... Citations" (lines 264-267): the empty-boundary pin
   annotations are each off by 1-2 from source. Report says `GetComm()@:62`,
   `Mpi::GlobalSum@:63`, `Mpi::Size/Rank@:65-66`, `Mpi::GlobalMin@:67`,
   `tdof_list[0] = 0@:77`. Source is `GetComm()` `:63`, `Mpi::GlobalSum` `:64`,
   `Mpi::Size/Rank` `:67-68`, `Mpi::GlobalMin` `:69`, `tdof_list[0] = 0` `:78`.
   The outer block range `:51-81` correctly encloses all of these.

2. **[low — citation-validity] Sub-pattern C M-assembly sub-line drift.**
   CYCLE.md lines 270-271: report says `epsilon_func@:84-85`, `BilinearForm
   m@:89`, `DiffusionIntegrator@:90`, `bdr_tdof_list_M =
   ...GetEssentialTrueDofs()@:103`. Source is `epsilon_func` `:86-87`,
   `BilinearForm m` `:90`, `DiffusionIntegrator` `:91`, `bdr_tdof_list_M = ...`
   `:104`. (`DIAG_ONE@:100-101` and `M = std::move(M_mg)@:108` are correct.) The
   outer block range `:84-110` encloses them.

3. **[low — citation-validity] Sub-pattern C WeakDiv sub-line drift.** CYCLE.md
   lines 272-275: report says comment`@:112`, `BilinearForm weakdiv@:113`,
   `MixedVectorWeakDivergenceIntegrator@:114`, `WeakDiv =
   make_unique<ParOperator>@:115-116`. Source is comment `:111`, `BilinearForm
   weakdiv` `:112`, `MixedVectorWeakDivergenceIntegrator` `:113`, `WeakDiv = ...`
   `:114-115`. Also the outer block range is cited `:111-116` but the WeakDiv
   block opens at `:110` (the `{`); `:111-116` still encloses the integrator.

4. **[low — cross-reference-integrity] Dangling `§Variant axes` section
   reference.** CYCLE.md §"Sub-pattern D" (lines 320-321) cites
   `[L1/divfree-projector](../L1/divfree-projector.md) §Variant axes`, but the L1
   entry has no `## Variant axes` heading (its headers are Context / Signature /
   Semantics / Algebraic laws / Dependencies / Status / Evidence). The L1 entry
   itself has an inline dangling "see Variant axes" at its line 43. This is an
   inherited dangling pointer; the theme propagates it. Candidate: either re-point
   to the L1 entry's actual §Signature/§Semantics block that describes the
   complex block-diagonal action, or fold into the existing L1-entry-drift OQ /
   surface to a harvester pass on the L1 entry.

5. **[informational — not a defect] L1-entry drift correctly handled.** The
   report's headline OQ `divfree-l1-entry-apply-close-and-reltol-line-drift` is
   accurate (independently confirmed against `book/src/L1/divfree-projector.md`).
   The abstractor correctly cited the *corrected* ranges in this theme, did NOT
   edit the firm L1 entry (out of abstractor authority), and filed an OQ. This is
   the desired behavior under batch-3's producer-citation-drift friction — noted
   here as positive telemetry for the integrator, not a problem to repair.

### Note for the repairer

Issues 1-3 are mechanical sub-line corrections within already-correct enclosing
ranges; the load-bearing apply/sign/tol citations are all exact, so these do not
threaten the `firm` status — they are surface-citation hygiene. Issue 4 is a
single section-anchor re-point (or an OQ fold-in). None of the four issues
touches a load-bearing claim. The `firm` status premise (positive site per step
+ positively-anchored sign + firm L1 anchor) is independently verified sound.

---

## Repair

### Fixes attempted

- **Finding (Issue 1, citation-validity)**: Sub-pattern C empty-boundary-pin
  parenthetical `@:NN` sub-line drift (CYCLE.md Sub-pattern C Citations block).
  - **Decision**: repaired.
  - **Action**: CYCLE.md §"Sub-pattern C ... Citations", the `:51-81` bullet.
    Re-pinned the inline element annotations to the true source lines, verified
    via codemap `read_range` on `palace/linalg/divfree.cpp:51-81`: `GetComm()`
    `@:62`→`@:63`, `Mpi::GlobalSum` `@:63`→`@:64`, `Mpi::Size/Rank`
    `@:65-66`→`@:67-68`, `Mpi::GlobalMin` `@:67`→`@:69`, `tdof_list[0] = 0`
    `@:77`→`@:78`; the MPI-selection summary range `:62-67,:71`→`:63-69,:73`.
    The outer block range `:51-81` was already correct and still encloses every
    cited element.

- **Finding (Issue 2, citation-validity)**: Sub-pattern C M-assembly
  parenthetical `@:NN` sub-line drift (CYCLE.md, `:84-110` bullet).
  - **Decision**: repaired.
  - **Action**: CYCLE.md §"Sub-pattern C ... Citations", the `:84-110` bullet.
    Re-pinned (verified via `read_range` on `:84-116`): `epsilon_func`
    `@:84-85`→`@:86-87`, `BilinearForm m` `@:89`→`@:90`, `DiffusionIntegrator`
    `@:90`→`@:91`, `bdr_tdof_list_M = ...GetEssentialTrueDofs()` `@:103`→`@:104`.
    `DIAG_ONE@:100-101` and `M = std::move(M_mg)@:108` were already correct and
    left unchanged. Outer range `:84-110` already correct.

- **Finding (Issue 3, citation-validity)**: Sub-pattern C WeakDiv-assembly
  parenthetical `@:NN` sub-line drift (CYCLE.md, `:111-116` bullet).
  - **Decision**: repaired.
  - **Action**: CYCLE.md §"Sub-pattern C ... Citations", the `:111-116` bullet.
    Re-pinned (verified via `read_range`): comment `@:112`→`@:111`,
    `BilinearForm weakdiv(...)` `@:113`→`@:112`,
    `MixedVectorWeakDivergenceIntegrator` `@:114`→`@:113`,
    `WeakDiv = std::make_unique<ParOperator>(...)` `@:115-116`→`@:114-115`.
    Outer range `:111-116` still encloses the integrator.

- **Finding (Issue 4, cross-reference-integrity)**: Dangling `§Variant axes`
  section-anchor reference (CYCLE.md Sub-pattern D, the `[L1/divfree-projector]
  §Variant axes` pointer).
  - **Decision**: repaired (in the theme; inherited L1-entry defect deferred —
    see below).
  - **Action**: CYCLE.md §"Sub-pattern D", the closing parenthetical. Re-pointed
    the theme's reference from the non-existent `§Variant axes` heading to the L1
    entry's actual `§Signature` block (the `y` element-type note,
    `book/src/L1/divfree-projector.md:92-94`, which describes the
    `Vector`/`ComplexVector` complex action). The block-diagonal characterization
    `P·(u + iv) = (P·u) + i(P·v)` is the abstractor's own one-line summary,
    supported by the L1 Signature element-type note; only the dangling anchor was
    corrected to a real one (trivial cross-reference fix, no content authored).
    Verified the L1 entry headings (`## Context / Signature / Semantics /
    Algebraic laws / Dependencies / Status / Evidence`) — confirmed no
    `## Variant axes` heading exists, and the L1 entry carries its own inline
    dangling "(see Variant axes)" pointer at its line 43.

### Unrepairable findings

None block the report. One inherited defect is deferred (not the repairer's to
fix here):

- **Inherited dangling `(see Variant axes)` pointer inside the firm L1 entry**
  (`book/src/L1/divfree-projector.md:43`). This is a defect in the artifact (the
  L1 operator entry), not in this theme report. Modifying `book/` directly is out
  of repairer authority, and the L1 entry is a firm, already-integrated artifact.
  The theme's *propagation* of the dangling anchor has been repaired above
  (re-pointed to a real L1 section). The L1-entry-internal dangling pointer should
  be cleaned up by the same harvester/repairer pass that closes the existing OQ
  `divfree-l1-entry-apply-close-and-reltol-line-drift` (both are firm-L1-entry
  citation/anchor hygiene on the same file). Recommend the integrator note this
  L1-entry anchor defect on that OQ when promoting it (it is the natural co-located
  fix). Not blocking: the theme no longer carries the dangling anchor.

## Suggested resolution

`ready`. All four critic-flagged issues are repaired in-place (3 mechanical
sub-line re-pins within already-correct enclosing ranges, verified against
`reference/palace/` via codemap `read_range`; 1 trivial cross-reference re-point
to a real L1 section). No load-bearing claim was touched — the headline apply /
sign / tol citations were independently confirmed exact by the critic and were not
modified. The `firm` status premise stands.

Integrator notes:
- The producer-filed OQ `divfree-l1-entry-apply-close-and-reltol-line-drift`
  (CYCLE.md §"Open questions" item 1) is preserved untouched — it is the
  downstream harvester/repairer follow-up on the firm L1 entry. When promoting
  that OQ, fold in the L1-entry-internal `(see Variant axes)` dangling-anchor
  cleanup (line 43) noted under Unrepairable findings — same file, same
  citation-hygiene pass.
- OQs 2 (`divfree-mult-doc-irrotational-vs-divfree-stale`, carried) and 3
  (closure-nesting structural shape, new/informational) are unaffected by this
  repair.
