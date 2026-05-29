---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T040458Z
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
repaired_at: 2026-05-29T041530Z
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

# META: verification of "Re-anchor gmres-inner-loop-iterate-while-migration" (lifter gmres §L4 v0.6→v0.7 self-rotation + theme firming)

## Critique

### Checks run

**citation-validity — warning.** I independently verified the load-bearing citations against source.
- **Palace L0 (codemap `read_range`):** `iterative.cpp:614-650` is the GMRES inner Arnoldi loop; the body (`ApplyBA → OrthogonalizeIteration → Norml2 → ApplyPlaneRotation`-chain at 627-640), the residual proxy (`beta = std::abs(s[j+1]); CheckDot; converged = (beta<eps)` at 642-644), the three-way break (`if (converged || j+1==max_dim || it+1==max_it) { it++; break; }` at 645-648), and the per-iteration print (617-621) all match the report's characterization exactly. `iterative.hpp:53-55` (the four mutable result scalars), `:155` (`class GmresSolver`, plain GMRES), `:222` (`class FgmresSolver : public GmresSolver`), `:256` (`mutable std::vector<VecType> Z` — FGMRES-only), and `:263-266` (the FgmresSolver ctor pinning `pc_side = PreconditionerSide::RIGHT`) are all accurate. The `flexible=false` / `Z`-is-FGMRES-only argument is correct against source.
- **The slice re-anchor (the crux):** I read the current `book/src/spec/slices/gmres.md` (671 lines) directly. Every re-anchored GMRES line-ref is correct: v0.6 `inner_loop` at `:594-606` (line 594 = the `inner_loop ::` signature), `check_stop` at `:587-592`, the `StopReason` sum type at `:551-554`, earliest-retained v0.2 form at `:122-133`, variant axes at `:172-176` and `:248-252`, the v0.6 surface table at `:645-654` with the cited rows verified per-line (`apply_BA`/`pc_side` at 648, `orthogonalize`/`gs_orthog` at 649, `apply_correction`/`flexible` at 650, `check_stop`/`max_it,max_dim` at 652), the `K.Z with` capture site at `:597`, the `K.j+1==op.max_dim` guard at `:591`, and `restart_cycle` at `:613-631`. The drift the report diagnoses is real: the old theme §Context cites `gmres.md:459-470 … :1067-1078`, and `:1067-1078` is well out of the 671-line slice — confirming the slice was reduced and the re-anchor is necessary and correct. The Edit-10 append anchor (the "witness approach generalises" bullet at slice `:671`) matches verbatim and is the slice's final content.
- **The warning** is a single class of drift the sweep MISSED: the report re-emits `cg.md:215-219` (the CG `iterate_while s0' (\s -> s.it < config.max_it && not s.converged) (\s -> cg_step opA eps s)` precedent) in three places — Edit 2's `[new]` (retained verbatim from `[old]`), the slice §L4 v0.7 append prose (block line 219), and the append §Citations (block line 284). The current `cg.md` is only **166 lines** (also reduced; its retained unique material is the L4 **v0.5** first-iteration-unrolling derivation, per its stub-header), so `cg.md:215-219` is out of range. The CG v0.4 `iterate_while` precedent was lifted to `book/src/L4/krylov-step.md` Form A. The report's entire thesis is "the gmres slice was reduced, so its line-refs drifted — sweep them"; the identical reduction happened to `cg.md`, but the report applied the sweep only to `gmres.md` refs. (Mitigating: the same stale `cg.md:215-219` already exists in the firm `iterate-while.md:229` and the pre-edit theme §Context, so the report partly inherits an upstream-stale ref — but it actively re-emits it in NEW content, the v0.7 append, which is squarely inside the report's own declared stale-citation sweep scope.)

**surface-or-evidence — pass.** This is a refinement-shaped proposal that modifies surface (the theme's prose/status + an appended slice §L4 v0.7 section) AND carries rotation evidence. The witness-into-carry hoist is faithful: the v0.6 predicate reads `op`/`conv`/`s.it` (outside the carry); the firm `iterate-while.md` §Signature (point 1, line 57; `cont: α -> Bool` contract, line 50: "The predicate is a pure function; it cannot read SimState … the slice folds `it` into its `α` carry") MANDATES folding non-carry termination state into the carry. The `stop_reason :: Maybe StopReason` carry field + `\K -> isNothing K.stop_reason` predicate + `check_stop_into_carry` writer + `fromJust K_final.stop_reason` post-loop extract is the textbook application of that discipline. The iteration-for-iteration equivalence argument holds: `check_stop_into_carry` computes exactly v0.6's `check_stop` (`:587-592`), the loop stops on the same condition, and the `j`-advance fires on the same `Nothing` arm.

**rotation-quality (CRUX) — pass.** This is a lifter self-rotation: lowering STRUCTURE stays, vocabulary firms. I confirmed the body primitive sequence survives textually unchanged — v0.6 slice body (`:596-601`: `apply_BA → orthogonalize → ls_update_column → modify it → carry-update`) is character-for-character the same as the v0.7 LHS body (theme block lines 81-86 and slice-append lines 251-256), modulo the named rotation (the added `check_stop_into_carry` write + the `j`-advance restructure, which IS the rotation, not noise). The rotation is genuinely more abstract/equational: the hand-rolled `case check_stop … of { Just -> pure; Nothing -> inner_loop … }` tail recursion is replaced by a direct invocation of the firm `iterate_while` combinator, making the predicate-on-carry-only discipline structural rather than implicit (`α -> Bool` literally) and exposing the §3.8 trajectory-pruning law — this is state-hiding / vocabulary-reuse compression, not a 1:1 rename. The parallel to `krylov-step-typed-wrapper-dissolution` is sound (same wrapper-dissolution shape; the GMRES additions — `stop_reason` carry threading + extras-record + trajectory pruning — are correctly scoped as the delta over the krylov-step theme). The "two distinct v0.7s" disambiguation is sound: the migration v0.7 touches only `inner_loop` + adds the `stop_reason` field; the classifier-compaction v0.7 (anticipated by the slice v0.6 OQ at `:669`, splitting `classify` to drop dead `total_it`) is on the orthogonal `restart_cycle`-classifier axis. I verified the slice v0.6 OQ at `:669` does name the classifier-compaction route, and the two read disjoint surfaces (`check_stop_into_carry` vs `classify_post`), so they compose without conflict as claimed.

**variant-axis-coverage — pass.** The four GMRES variant axes (`pc_side`, `gs_orthog`, `flexible`, `max_dim`) are each addressed and shown to pass through the L4>L3 rotation at body-primitive level (Edit 5). The fgmres sibling is correctly HELD (OQ 2): it carries TWO additional variant-axis collapses (`pc_side=RIGHT` pinned at the ctor `iterative.hpp:263-266`, `flexible=true`) plus the per-iteration `Z[j]` workspace — these are genuinely orthogonal axes that warrant a separate dispatch, not hidden branches. The plain-GMRES `flexible=false` clarification (Edit 5 note) is L0-correct: `GmresSolver` (`:155`) does not declare `Z`; `Z` is the FGMRES-only member (`:256`), so the `if op.flexible then … else K` carry-update takes its `else K` no-op branch in plain GMRES. No hidden combination.

**cross-reference-integrity — pass.** All `[link]` targets resolve: `L4-L3/fgmres-inner-loop-iterate-while-migration.md`, `L4-L3/krylov-step-typed-wrapper-dissolution.md`, `L4/iterate-while.md`, `L3/krylov-step.md`, `concepts/derived-view-hoisting.md` all exist on disk. The dep-map status touch is correctly flagged-not-improvised: `L4/index.md:44` (theme row) and `:53` (`iterate-while` "Lowers to" cell) both currently carry `*(rough-in; landed cycle-008 wave-2)*` annotations — I verified both — and the report routes the `rough-in→firm` sync to the integrator/`layer-intro-author` rather than emitting it as a proposed-change (correct authority partition; the report notes a firm theme with a rough-in dep-map annotation would be a drift the critic flags). The structural-home OQ (slice §L4 vs a standalone `L4/gmres.md` operator) is surfaced as OQ 1 for the planner, not improvised into the artifact — the most-conservative placement (slice §L4 append + theme LHS, no new `L4/gmres.md` file) is the right lifter-scope call.

**edge-label-fidelity — pass.** The theme's edge is L4>L3; the LHS stays L4 (the v0.7 `iterate_while` invocation), the RHS stays L3 (the value-threaded dissolution), and the prose narrates the rewrite forward L4→L3. The self-rotation is correctly framed as L4→L4 (no layer advancement), consistent with the slice's v0.2–v0.6 self-rotation sections. No inversion; high→low direction preserved.

**plan-kind-consistency — pass.** The 10 proposed-changes blocks are well-formed and match a `theme` firming + slice self-rotation append shape: Edits 1-9 are surgical `[old]`/`[new]` prose/status edits to the theme (I verified every `[old]` anchor matches the on-disk theme verbatim — lines 3, 11, 15, 19, 114-121, 125, 176, 192, 196-202), Edit 10 is the slice §L4 v0.7 append (correct append idiom — `[new]` re-quotes the `[old]` final bullet then appends). The status flip `rough-in → firm` is content-justified (the upstream rotation is now authored). The one remaining rough-in element (`check_stop_into_carry`) is correctly left unpromoted with the firm-theme-with-rough-in-helper precedent cited (krylov-step-typed-wrapper-dissolution firm while `iterate_while` was rough-in). No rough-in placeholders masquerading as firm.

**skill-uptake-survey — warning (non-blocking, telemetry only).** The report's shape implies several relevant skills exist (`verify-citation-range` for the slice/Palace line-ref sweep — the report's central activity; `verify-rotation-citation` / `verify-refinement-surface` for the self-rotation; `propose-rotation`). The §Discipline notes describe the verification work in prose ("verified by direct read this dispatch", "verified each surface-table row") but do not name any skill invocation. Pure presence check; surfaces telemetry, does not block. Given the report IS a citation-re-anchor sweep, an explicit `verify-citation-range` invocation (which carries an "Audit-report / inherited-citation sub-case" section as of cycle-012) would likely have caught the `cg.md:215-219` blind spot below.

### Issues found

1. **`cg.md:215-219` is out of range (stale CG-precedent citation re-emitted in new content).** Severity: **warning** (citation-validity). The current `book/src/spec/slices/cg.md` is 166 lines; its retained unique material is the L4 v0.5 first-iteration-unrolling derivation, and the v0.1–v0.4 forms (including the v0.4 `iterate_while` rendering) were lifted to `book/src/L4/krylov-step.md` Form A. The report cites `cg.md:215-219` for the CG `iterate_while` precedent in three locations: Edit 2 `[new]` (`book/src/spec/slices/gmres.md` §Context, retained from `[old]`), the slice §L4 v0.7 append prose (CYCLE.md Edit 10 block, the "It is the GMRES analogue of CG's v0.4 … (`cg.md:215-219`)" sentence), and the append §Citations ("The CG precedent rendering … `cg.md:215-219`"). This is the exact class of slice-reduction drift the report exists to catch — applied to `gmres.md` refs but not to the `cg.md` ref in the same paragraphs. Re-anchor target: the firm `L4/krylov-step.md` Form A (or `L4/iterate-while.md:229`, though that firm row carries the same stale ref — a pre-existing drift outside this report's scope). Note the stale ref pre-exists in `iterate-while.md:229` and the un-edited theme §Context, so it is partly inherited — but the v0.7 append is NEW content authored this dispatch.

2. **`iterative.cpp:615` is off-by-one for the loop header.** Severity: **informational** (citation-validity). The GMRES inner loop `for (;; j++, it++)` is at line **614**; line 615 is the opening `{`. The report cites `:615` for the loop header in §Supporting evidence (CYCLE.md line 317) and the slice-append §Citations (block line 285). This is NOT a unique-to-this-report error: the firm `iterate-while.md:232` already cites `iterative.cpp:615` for the same GMRES loop, so the report is consistent with an established (if technically off-by-one) convention. Body content is correctly characterized. Flagging for completeness, not as a defect requiring repair.

3. **`gmres.md:537` is a loose supporting anchor for the flexible capture site.** Severity: **informational** (citation-validity). Edit 5 cites "the prose at `gmres.md:537`" for the `flexible` in-loop variant read. Line 537 is a v0.5-section *Open questions* musing ("Whether the `op.flexible` read inside `inner_loop` … admits a similar consolidation"), which is topically supportive and in-range but is OQ prose rather than a definitional statement. The load-bearing anchor for the same claim — the actual capture-site code `K1 = if op.flexible then K{ Z = K.Z with (K.j, z) } else K` at `:597` — is cited correctly alongside it, so the claim is well-supported. Minor anchor-quality note only.

4. **Skill invocation not surfaced for the citation-sweep.** Severity: **informational** (skill-uptake-survey). The report's core activity is a citation re-anchor sweep, for which `verify-citation-range` (with its cycle-012 inherited-citation sub-case) is the matching skill; no invocation is referenced. Telemetry only; relates to why finding 1 was missed.

## Repair

### Fixes attempted

- **Finding 1 — `cg.md:215-219` out of range (CG `iterate_while` precedent re-emitted in NEW content).** [citation-validity, warning]
  - **Decision**: repaired.
  - **Action**: re-anchored all three re-emissions of the stale `cg.md:215-219` ref in `reports/2026-05-29T034441Z-lifter-gmres-l4-self-rotation/CYCLE.md`. The CG v0.4 `iterate_while s0' (\s -> ...) (\s -> cg_step ...)` precedent was lifted to the firm L4 entry `book/src/L4/krylov-step.md` §Semantics (Form A — explicitly labeled "CG v0.4-shape" at `L4/krylov-step.md:22`, dataflow rendered at `:54`) when the cg slice was reduced (the current `cg.md` is 166 lines and retains only the unique L4 v0.5 first-iteration-unrolling material, which uses `iterate_while_with_prev`). The three fixes:
    1. **Edit 2 `[new]`** (`gmres.md` §Context, CYCLE.md ~line 127): rewrote the "CG slice already renders … at `cg.md:215-219`" clause to point at the lifted firm home `L4/krylov-step` §Semantics Form A, noting the cg slice was reduced and retains only the v0.5 `iterate_while_with_prev` material.
    2. **Edit 10 slice-append prose** (CYCLE.md ~line 219, the "GMRES analogue of CG's v0.4 … (`cg.md:215-219`)" sentence): replaced the dead `cg.md:215-219` ref with a live `[L4/krylov-step](../../L4/krylov-step.md)` §Semantics Form A link (correct relative path from `book/src/spec/slices/`).
    3. **Edit 10 §Citations** (CYCLE.md ~line 284, "The CG precedent rendering … `cg.md:215-219`"): re-anchored to `L4/krylov-step` §Semantics Form A and pointed the residual cg-slice material at the in-range `cg.md:86-108` (`cg_solve` + the `iterate_while_with_prev` driver, verified against the current 166-line file).
  - **Note**: the surviving `cg.md:215-219` at CYCLE.md line 126 is inside Edit 2's `[old]` anchor block — that is the verbatim on-disk theme §Context text the integrator must match, so it is intentionally left unchanged (changing it would break the integrator's `[old]` anchor). Only the `[new]` content the integrator writes is corrected. The same stale ref pre-exists in the firm artifact (`iterate-while.md:229` and the un-edited theme §Context); those are out of this report's scope (artifact, not the report) and were not touched.

- **Finding 2 — `iterative.cpp:615` off-by-one (loop header at 614).** [citation-validity, informational]
  - **Decision**: not-needed.
  - **Rationale**: the critic flagged this as informational and consistent with the established convention in the firm `iterate-while.md:232`, which cites the same `iterative.cpp:615` for the same GMRES loop. Body content is correctly characterized. Re-anchoring to `:614` here would create a *divergence* from the established artifact convention; leaving it matches the precedent. No fix applied.

- **Finding 3 — `gmres.md:537` loose-but-in-range supporting anchor.** [citation-validity, informational]
  - **Decision**: not-needed.
  - **Rationale**: the critic confirms `:537` is topically supportive and in-range (v0.5 OQ prose), and the load-bearing capture-site anchor `gmres.md:597` is cited correctly alongside it, so the claim is well-supported. Anchor-quality note only; no defect to repair.

- **Finding 4 — skill invocation not surfaced.** [skill-uptake-survey, informational]
  - **Decision**: not-needed.
  - **Rationale**: telemetry-only presence check; not a content defect. Not repairer-actionable on the report (would require the producer to re-run; the substantive blind-spot it relates to — finding 1 — is now repaired).

### Unrepairable findings

None. The one substantive warning (finding 1) was mechanically repairable: the stale CG-precedent ref had a single, unambiguous, source-verified current home (`L4/krylov-step.md` §Semantics Form A, which the cg slice stub-header at `cg.md:13` explicitly names as the supersessor of the cg slice's L4 v0.1–v0.4 content). The re-anchor is a pure repoint — no substantive authoring.

## Suggested resolution

`ready`. Notes for the integrator:

- The `cg.md:215-219` re-anchor is applied to the report (the three `[new]`/append-prose locations). The integrator applies the report's proposed-changes as usual; the re-anchored CG-precedent links resolve to the live firm `L4/krylov-step.md` (verified on disk).
- **Dep-map status touch still pending (CYCLE.md Open question 3, not a repair item):** the `rough-in → firm` flip means `L4/index.md:44` (theme row) and `:53` (`iterate-while` "Lowers to" cell) carry stale `*(rough-in; landed cycle-008 wave-2)*` annotations. The report correctly routes this to the integrator / `layer-intro-author` rather than emitting it as a proposed-change (dep-map wording is `layer-intro-author` territory). The integrator should sync both cells to `*(firm; cycle-020 wave-1 lifter)*` at finalize — a firm theme with a rough-in dep-map annotation would be a cross-reference-integrity drift.
- **Pre-existing stale `cg.md:215-219` in the artifact** (`iterate-while.md:229`, and the theme §Context being edited) is the same slice-reduction drift class, outside this report's repair scope (it is artifact, not report). Worth a planner/lifter follow-up to sweep the firm `iterate-while.md` ref onto the same `L4/krylov-step` Form A home — flagging, not enacting.
