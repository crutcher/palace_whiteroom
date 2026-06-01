---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T071500Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-01T072000Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: lifter
---

# META: verification of "Formalize assemble-diagonal at L2" (L2 assemble-diagonal floor)

## Critique

### Checks run

**citation-validity — pass.** `citecheck --scan` over the whole report returned 25 ok / 0 failing (bounds + path-hygiene clean). I then `--anchor`-verified every load-bearing pinpoint: `operator.cpp:85-96` (`ComplexWrapperOperator::AssembleDiagonal` @85), `operator.cpp:25-28` (`MFEM_ABORT` @27), `rap.cpp:163-164` (`convergent` @163 — the comment "a convergent diagonal is assembled with |P|ᵀ dₗ"), `rap.cpp:174` (`AbsMultTranspose` @174), `rap.cpp:165-166` (`test_fespace` @165, square precondition), `rap.cpp:467-479` (`ComplexParOperator::AssembleDiagonal` @467), `hypre.cpp:88` (`hypre_CSRMatrixExtractDiagonal`), `libceed/operator.cpp:120` (`diag.Size() == height`) and `:139` (`CeedOperatorLinearAssembleAddDiagonal`), `jacobi.cpp:79` and `chebyshev.cpp:177` (`AssembleDiagonal` consumer chain), and `test-libceed.cpp:367-376` (`rtol` @371,375). All resolve in-range with the cited tokens present. The `eᵢᵀ A eᵢ` mathematical-spec framing is correctly flagged in-prose as the *definition not the implementation* (Palace forms no basis-vector probes), so it carries no false positive-source obligation. No `verified_against:` block is present (harvester report), so that sub-check is N/A. Specifically focus-item (1) is satisfied: all four named anchors support their claims and the +1-drift guard is clear.

**surface-or-evidence — pass.** This is a `new:` operator entry (floor creation), not a refinement of existing operator/theme text, so the refinement-surface rule applies only loosely. The entry creates new L2 surface (signature, semantics, six laws, four non-laws, variant axes) and is positively anchored throughout; it does not assert an unsupported rotation_claim. The "value-thread-isomorphic to L1" framing is an identity-in-form claim backed by the inherited-law disclosure, not a bare rotation assertion.

**rotation-quality — pass (degenerate-rotation, correctly framed).** The report does NOT claim a compaction/abstraction rotation at the L2→L1 edge — it explicitly declares the fusion content **degenerate** (no multi-operation kernel-fusion to unfold at the operator-to-data boundary; the representation-specific diagonal-extraction mechanics are L0 concerns absorbed into the representation axis and deferred to L1>L0). This is the honest call: an identity-in-form floor is not a rotation, and the report frames it as such rather than manufacturing a fake one. Per the "Identity-lowerings still require both L levels" invariant, the floor is justified by *presence* (the L3 form rests on an adjacent L2 parent), not by a rotation claim — so the no-rotation framing is correct, not a defect. Focus-item (3): the NO-fold-parent / sibling-of-`apply_linop` / operator-to-data-divide framing is consistent across intro, §"Not an apply_linop variant", §"No fold-parent", and the dep-map; the operator/data divide (no `x` to be linear in; square `M=N`; result is a property of `A` alone) is a sound, well-argued basis for fork-independence.

**variant-axis-coverage — pass.** The report enumerates one orthogonal axis (element-type real|complex, collapsed to a parameterised operator) + one absorbed axis (operator-representation: sparse-CSR | matrix-free | parallel-wrapped | complex-wrapped, absorbed into the opaque `LinearOperator[N,N]`), and three explicit non-axes (transpose-mode — diagonal is transpose-invariant; abs-vs-signed — the abs is on the *prolongation* not the diagonal; partial-domain abort — a precondition, not a variant). Each is cited. No hidden branch. Focus-item (2): the load-bearing exact-vs-approximate caveat is correctly placed as the one point where the absorbed representation axis surfaces *semantically*, and is preserved as a non-law rather than swept into the absorption.

**cross-reference-integrity — pass.** All `[link]` targets resolve on disk: `L1/assemble-diagonal.md`, `L3/assemble-diagonal.md`, `L3/apply_linop.md`, `L2/dot.md`, `L2/index.md`, `L2/inner_product.md`, `L2/linear_combination.md`, `L2/krylov-step.md`, `concepts/variant-absorption.md`. The `edit:book/src/L2/index.md` row matches the established table-row format (verified against the existing `dot` row at index.md:62). The `edit:book/src/SUMMARY.md` insert lands in a populated L2 section (siblings present at SUMMARY.md:49-62). Build-readiness fence guard: the firm body is fully ENCLOSED inside the `new:` fence (lines 22–470) with `## Status` at line 354 inside the fence; fence enumeration shows even parity (6 markers / 3 balanced blocks: 22–470 new, 472–475 index edit, 477–479 SUMMARY edit) with no nested-fence truncation. No firm-body-outside-fence defect.

**edge-label-fidelity — pass.** The report's edge claims (L2→L1 identity-in-form on the primitive; L3→L2 body-identity narrated by the separate theme; L1>L0 defers the de-fusion) are each discussed in prose that matches the named edge. No mismatched edge label. The high→low discipline is respected: `assemble_diagonal` is defined in L2 vocabulary, with the two adjacent rotations narrated as belonging to the separate lowering themes, and the chapter does not define the operator in terms of L1 primitives or L0 mechanics. Focus-item (5) satisfied.

**plan-kind-consistency — pass.** Declared kind is `firm`, and the content matches: complete signature, semantics, six fully-stated laws, four non-laws, variant-axis profile, evidence list — no rough-in placeholders, no TODO sentinels. Focus-item (2) adjudication: the `firm`-not-`partly-constructive` call is correct. The matrix-free high-order-Nedelec approximate-diagonal caveat is recorded as a **positively-anchored non-law** (sourced to `rap.cpp:163-164` convergent-diagonal comment + `libceed/operator.cpp:139` element-accumulation + `jacobi.hpp:15-16` "(approximate) diagonal construction for matrix-free operators" consumer comment — I confirmed that exact comment text on disk + test-witnessed `test-libceed.cpp:367-376` relaxing `rtol` to 1.0 for the 3D order>1 non-tensor-basis Nedelec case). A `partly-constructive` status would require a *constructed* sub-part materialized from negative anchors lacking a positive source site; here every claim has a positive source site and the approximation is a documented, test-witnessed property — so the non-law (not a status reduction) is the right vehicle, and `firm` is correct, consistent with the L1 and L3 entries.

**skill-uptake-survey — pass.** The report's shape (a firm floor harvest with heavy citation) implies `verify-citation-range` / the `citecheck` mechanical realization; the report explicitly records "all L0 anchors self-verified via `tools/citecheck/citecheck.py --anchor` this invocation" (frontmatter + §Evidence + §Supporting evidence). The fence-encloses-body guard concern is also pre-empted ("full firm chapter body is authored inside the proposed-changes block"). Skill uptake is surfaced. Non-blocking telemetry check.

### Issues found

No defects in THIS report. Two non-defect observations, both already self-flagged by the report and recorded here for the repairer/integrator trail:

1. **Cross-report follow-up (NOT a defect in this report): L1-entry citation drift.** `book/src/L1/assemble-diagonal.md:111` cites `hP->AbsMultTranspose(1.0, lx, 0.0, diag)` "at line 172"; the on-disk call is at `rap.cpp:174` (I confirmed line 172 is the `if (const auto *hP = dynamic_cast<...>(P))` guard). This is a drift in a **different file** (the L1 entry), out of this dispatch's one-operator-per-invocation scope. THIS report cites `:174` correctly throughout. Per the dispatch framing, this is a cross-report follow-up for a future lifter/repairer pass on the L1 entry, not a defect to repair here. The report already filed it as a §Open-questions caveat (CYCLE.md §Open questions, 3rd bullet) — no action needed on this report.

2. **Directive-scope normalization (non-blocking, meta-phase domain).** The report extends the `l2-floor-under-l3-blas1-cohort` directive from the BLAS-1 leaf cohort to the operator-to-data primitive `assemble_diagonal` (which is not BLAS-1). The extension is well-justified (same identity-in-form floor shape, same "firm L3 leaf rests on adjacent L2 parent" rationale), but the directive name and the L2/index "Identity-in-form BLAS-1 floors" cohort heading no longer cleanly cover the new member. The report surfaces this for the batch-12 meta-phase / layer-intro-author (rename to cohort-neutral, e.g. `l2-floor-under-l3-leaf-cohort`, or a new sub-bullet). Correctly scoped out of this dispatch (the report adds only its dep-map row + SUMMARY entry, not an intro rewrite). Not a citation/surface/rotation/variant defect — surfaced for completeness.

3. **Count-ownership (focus-item 4) — clean.** The report explicitly disclaims the L2/index running-count tally ("D11 owns the L2/index running-count tally — I do NOT touch it"; "I added only my dep-map row + SUMMARY entry, not an intro rewrite"). The `edit:book/src/L2/index.md` block adds only the single `assemble-diagonal` dep-map row and does not mutate the firm-count line. No count-divergence risk from this report.

## Repair

### Fixes attempted

The critic returned all 8 checks **pass** with **no defects in this report's own content**. There is nothing repairable in THIS report — all `repairs:` entries are `not-needed`. The three items in the critic's "Issues found" section are non-defect observations (all already self-flagged by the producer); I triaged each below.

- **Finding (critic obs. 1)**: L1-entry citation drift — `book/src/L1/assemble-diagonal.md:111` cites `AbsMultTranspose` "at line 172"; on-disk call is `rap.cpp:174` (line 172 is the `dynamic_cast` guard).
  - **Decision**: not-needed (in this report) → **deferred as follow-up**.
  - **Rationale**: The drift is in a **different file** (the firm L1 entry), out of this dispatch's one-operator-per-invocation scope. THIS report cites `rap.cpp:174` correctly throughout (citecheck `--anchor`-confirmed by the critic). Editing the L1 entry's citation is a cross-file artifact touch I do NOT have authority to make from this report (repairer does not modify `book/` directly; cross-report edits are out of scope). The producer already filed it as a §Open-questions caveat. Routed to a future lifter/repairer pass on the L1 entry.

- **Finding (critic obs. 2)**: Directive-scope normalization — the report extends `l2-floor-under-l3-blas1-cohort` from the BLAS-1 leaf cohort to the non-BLAS-1 operator-to-data primitive `assemble_diagonal`; the directive name + the L2/index "Identity-in-form BLAS-1 floors" cohort heading no longer cleanly cover the new member.
  - **Decision**: not-needed → **deferred to meta-phase / layer-intro-author**.
  - **Rationale**: A directive-rename / cohort-heading rewrite is a methodology-level concern explicitly out of repair scope ("Methodology-level concerns the critic flagged for meta-phase attention"). The report correctly scopes this out (it adds only its dep-map row + SUMMARY entry, not an intro rewrite). Surfaced for the batch-12 meta-phase.

- **Finding (dispatch-directed check, not in critic's list)**: The firm `book/src/L3/assemble-diagonal.md` asserts **"no interposed L2 entry exists"** in its frontmatter (`lowers_to` row, L3:6), §Downward prose (L3:28), and §Lowers-to (L3:128-130) — e.g. "no interposed L2 entry and no `L3-L2`/`L3-L1` theme file"; "The L2 layer hosts no standalone `assemble_diagonal` entry". This report **creates** exactly that L2 entry, so those three assertions in the L3 entry go stale once this floor lands.
  - **Decision**: not-needed (in this report) → **deferred as follow-up (lifter)**.
  - **Rationale**: This is a **contradiction between the report and existing firm artifact content** — explicitly out of repair scope. Reconciling it requires substantively rewriting the L3 entry's §Lowers-to / §Downward prose and dep-map row to narrate the now-present L2 parent (the L3>L1 hop becomes L3>L2>L1, mirroring how the rest of the L2-floor-under-L3 cohort entries read). That is substantive authoring in a **different firm file**, not a mechanical/surgical fix, and not trivially within my authority. It is the same class of follow-up the dispatch noted "D7's themes already flag stale L3 §Lowers-to". Routed to a lifter touch on the L3 entry, to run after this floor integrates.

### Unrepairable findings

None of the three items is a *defect in this report*. All three are **cross-file / methodology follow-ups** that do not block applying this report's own (clean, complete, fully-cited) L2 floor:

1. **L1 citation drift** (`book/src/L1/assemble-diagonal.md:111`, "line 172" → `rap.cpp:174`) → lifter/repairer pass on the L1 entry.
2. **Directive-scope / cohort-heading normalization** (`l2-floor-under-l3-blas1-cohort` no longer covers a non-BLAS-1 member) → batch-12 meta-phase / layer-intro-author.
3. **Stale "no interposed L2 entry" assertions** in `book/src/L3/assemble-diagonal.md` (frontmatter L3:6, §Downward L3:28, §Lowers-to L3:128-130) → lifter touch on the L3 entry, post-integration.

## Suggested resolution

**`overall_status: ready`.** This report's own content is defect-free (8/8 pass) and applies cleanly — the L2 `assemble-diagonal` floor is complete, fully cited, and correctly framed as an identity-in-form floor. None of the three follow-ups blocks integration of THIS report.

`follow_up_agent: lifter` names the **post-integration** reconciliation of the L3 entry's now-stale "no interposed L2 entry" prose (item 3, the highest-leverage of the three — it's a direct contradiction created by landing this floor). The integrator should land this report, then schedule the lifter touch on `book/src/L3/assemble-diagonal.md` (reconcile §Lowers-to L3:128-130, §Downward L3:28, and the `lowers_to` frontmatter row L3:6 to reflect the now-present L2 parent — the L3>L1 hop is now L3>L2>L1). The L1 citation-drift fix (item 1) can ride the same lifter/repairer sweep. Item 2 (directive rename) is meta-phase domain. None blocks the commit.
