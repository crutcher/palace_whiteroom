---
verifies: ../REPORT.md
critiqued_at: 2026-05-29T053000Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: warning
  skill-uptake-survey: warning
repaired_at: 2026-05-29T054500Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: repaired
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "Formalize ksp_solve at L2" (stub→firm outer-driver composition)

## Critique

### Checks run

**citation-validity — pass.** Every L0 anchor in the report was independently re-read via `palace-codemap read_range` against `reference/palace/`. All confirmed exactly:
- CG `Mult` def `iterative.cpp:361`; `eps = max(rel_tol·initial_res, abs_tol)` `:417`; pre-loop `converged = (res < eps)` `:418`; loop guard `for (; it < max_it && !converged; it++)` `:427`; operator-apply `A->Mult(p, z)` `:443`; **in-loop `converged = (res < eps)` `:463`**; result write `final_res = res; final_it = it;` `:484-485`.
- GMRES `Mult` def `iterative.cpp:544`; **restart loop `for (; it < max_it; restart++)` `:563`**; result write `final_res = beta; final_it = it;` `:703-704`.
- `iterative.hpp`: `ScalarType` element-type conditional `:25-32`; tolerance/`max_it` fields `:42-46`; result fields `converged`/`initial_res, final_res`/`final_it` `:52-55`; `GetConverged()` with `rel_tol > 0.0 || abs_tol > 0.0` gate `:98`; accessors `GetInitialRes`/`GetFinalRes`/`GetNumIterations` `:101-108`.
- `ksp.cpp`: `BaseKspSolver::Mult` def `:296`, `ksp->Mult(x, y)` `:300`, `GetConverged()`+`Mpi::Warning` `:301-306`, `ksp_mult++`/`ksp_mult_it += GetNumIterations()` `:308-309`; factory CG/GMRES/FGMRES arms with MINRES/BICGSTAB/DEFAULT `MFEM_ABORT` at `:53-56`; instantiations `:312-313`.

The two declared off-by-one **corrections vs. the firm L3 entry are both vindicated by source**: the L3 entry (`book/src/L3/ksp_solve.md`) cites the CG in-loop `converged` at `:464` (lines 74/88/185 of that entry) and the GMRES restart loop at `:564` (lines 94/102/157); direct source reads place them at `:463` and `:563` respectively. The report's `:463`/`:563` are correct. The report correctly declines to edit the append-only L3 entry and routes the drift to Open questions for a lowering-verifier/lifter pass. No claim in the entry lacks a pointer; pass.

**surface-or-evidence — pass.** This is a stub→firm surface promotion (the operator text is authored in full), not a pure retroactive-evidence backfill, so the surface-AND-evidence condition is the applicable one and is met: the kernel(`krylov-step`)/driver(`ksp_solve`) architecture, the signature `ksp_solve :: (K, b) -> SolveResult` with body `iterate_while (krylov-step op) s_init predicate`, and the non-identity coverage-gap framing (L2↔L1 un-collapse of the L1 opacity + L3↔L2 iteration-view erasure) are all grounded in cited Palace `Mult` bodies and the firm sibling entries. Pass.

**rotation-quality — pass (crux check, clear).** The entry stays in L2 vocabulary (kernel-fold composition, named-by-role wrap) and does NOT embed the L3>L2 lowering — `L3-L2/ksp-solve-outer-driver` is forward-referenced as plain text (confirmed missing on disk: that is correctly wave-2 dispatch #3's job). The firm body captures a genuine non-identity rotation against L1: the L1 form (`L1/ksp_solve`) collapses the entire method body — outer loop, restart, per-step kernel — into an opaque `Solver[A]` operator application; the L2 form opens that opacity into the explicit (`krylov-step` kernel) + (convergence-test/restart fold) composition, re-surfacing the L1-absorbed `krylov-method` axis as the L2 solver-method loop-shaping axis. This is state-hiding-un-erasure / opacity un-collapse, not a 1:1 rename. The §"L2 vs L1 distinction" and §"Lowers from" sections explicitly distinguish this from the identity `L3-L2/krylov-step-body-identity` kernel theme. Pass.

**variant-axis-coverage — pass.** Six loop-shaping axes are enumerated and each combination is addressed, not hidden: solver-method (CG single-fold vs GMRES/FGMRES restart-nested double fold, with the restart loop cited at `:563` and the per-method residual proxy cited at `:484`/`:703`), element-type (real/complex, `iterative.hpp:25-32` + instantiations `ksp.cpp:312-313`), preconditioner-side (left/right/split, absorbed into the kernel op-surface `op.T` per `apply_BA`), convergence-criterion (relative/absolute/combined via the `eps` threshold `:417`, including the degenerate both-zero-tol `GetConverged` corner `:98`), initial-guess-policy (cold/warm), convergence-failure-policy (soft-fail-with-flag — explicitly noted as the only Palace variant). The unimplemented MINRES/BICGSTAB arms are explicitly scoped out via the factory abort `:53-56`. The driver axes are correctly separated from `krylov-step`'s six body axes. No hidden branch; pass.

**cross-reference-integrity — pass (fence-guard check, clear; the cycle-019 defect is NOT present).** The full firm body is authored INSIDE the `edit:book/src/L2/ksp_solve.md` fence: the fence opens at CYCLE.md line 24 and closes at line 212, and every section — frontmatter (`---` 25/40), `# ksp_solve` (42), Signature (63), Semantics (99), Algebraic laws (117), Status (175), Lowers from (179), Lifts to (183), Evidence (197) — sits between those bounds, with Evidence the last section before the closing fence. The two inner ` ```text ` code blocks (Signature 65-75, body composition 79-89) are properly paired and nested; the already-integrated firm entries `book/src/L3/ksp_solve.md` (3 inner text blocks) and `book/src/L2/krylov-step.md` (2) confirm the integrator's fence parser handles nested ` ```text ` inside an `edit:` block correctly, so the nesting is established convention, not a risk. All `[link]` targets resolve: every same-layer (`krylov-step`, `orthogonalize`, `incremental-least-squares`), L1 (`apply_linop`/`axpy`/`axpby`/`axpbypcz`/`dot`/`nrm2`/`scal`/`ksp_solve`), L3 (`ksp_solve`), L3-L2 (`krylov-step-body-identity`), and concept (`convergence-test`/`solve-monad`/`solver-as-operator`/`derived-view-hoisting`/`variant-absorption`/`constructed-operators`/`apply_BA`/`first-iteration-unrolling`/`ksp_solve`) reference exists on disk. The only intentionally-unresolved reference (`L3-L2/ksp-solve-outer-driver`) is plain text, not a live link — correct per the rough-in-forward-reference convention. Pass.

**edge-label-fidelity — pass.** The `book/src/L2/index.md` dep-map edit flips the `ksp_solve` row from `stub` to `firm`; the prose in that row discusses exactly the L2↔L1 (un-collapse) and L3↔L2 (iteration-view erasure) relationships the entry carries, and the L0 anchors quoted in the row (CG `:361-486`, GMRES `:544-705`, base `:25-115`, driver wrap `:296-309`) match the entry's Evidence. Edge label matches prose; pass.

**plan-kind-consistency — warning.** The declared kind is a `firm` operator promotion and the body content is consistent with `firm` (no rough-in placeholders; Signature/Semantics/laws/Evidence all fully authored). Two of the three proposed-changes blocks are well-formed unambiguous replacements (the body fence; the L2/index dep-map row, which reproduces the full current row text verbatim as the replacement target). The **`edit:book/src/SUMMARY.md` block (lines 218-220) is under-specified as a replacement instruction**: it supplies only the new text `- [ksp_solve](./L2/ksp_solve.md)` but the current SUMMARY line is `- [ksp_solve (stub)](./L2/ksp_solve.md)` (verified at `book/src/SUMMARY.md:44`). An integrator that does a literal append rather than a de-stub replacement would produce a duplicate TOC entry / a stale `(stub)` line. The intent (de-stub the existing line) is clear from the Summary prose, but the edit block does not name the old line. Warning — flag for the integrator to treat as a replace-in-place of the line-44 `(stub)` entry, not an append.

**skill-uptake-survey — warning (telemetry only, non-blocking).** This stub→firm operator promotion with explicit citation re-verification and a declared rotation-quality claim is squarely the shape that `verify-citation-range` (extended cycle-012 with the inherited-citation sub-case — directly applicable here, since the report inherits and corrects the L3 entry's citation set), `verify-rotation-citation`, and `propose-rotation` exist to support. The report's Evidence/Supporting-evidence sections state citations were "self-verified against source via `palace-codemap` `read_range`" but do **not** name any skill invocation. Pure presence check; surfaced as telemetry, not a defect.

### Issues found

1. **SUMMARY de-stub edit is an under-specified replacement target** — `reports/2026-05-29T051532Z-harvester-l2-ksp-solve-firm/CYCLE.md:218-220` (`edit:book/src/SUMMARY.md` block). The block provides only the new line `- [ksp_solve](./L2/ksp_solve.md)`; the current SUMMARY line is `- [ksp_solve (stub)](./L2/ksp_solve.md)` (`book/src/SUMMARY.md:44`). As written, a literal-append integrator path would leave a stale `(stub)` line and/or duplicate the TOC entry. Severity: low-medium. Repair: have the integrator perform a replace-in-place of the existing line-44 `(stub)` entry (drop the `(stub)` suffix), not an append; or annotate the edit block to name the old line.

2. **L3-entry citation drift is correctly identified but only routed to OQ, not yet fixed** — confirmed by source: `book/src/L3/ksp_solve.md` cites CG in-loop `converged` at `:464` (lines 74/88/185) and GMRES restart at `:564` (lines 94/102/157); source truth is `:463`/`:563`. The report properly declines to edit the append-only L3 entry and files the OQ. Not a defect of THIS report (the L2 entry's own citations are correct) — recorded here as a corroborated cross-reference observation so the downstream lowering-verifier/lifter pass has independent confirmation that the corrections, not the L3 values, are right. Severity: informational (the L3 surrounding ranges `:361-486`/`:544-705` are correct; only the inner point-citations drift).

3. **L2 index Working Note staleness is out-of-scope but real** — the report's own Open-questions flags that `book/src/L2/index.md:73` Working Note still says "`L3/ksp_solve.md` not yet on disk" though the L3 entry landed cycle-020, and that the line-41 / line-72 prose stubs of the `ksp_solve` row are not refreshed by this dispatch's row-only edit. Confirmed present on disk. Correctly scoped out (index prose, not the operator row); noted for a layer-intro-author refresh. Severity: low, out-of-scope.

4. **`incremental-least-squares` referenced as plain text though it exists on disk** — `CYCLE.md:147` ("the queued `incremental-least-squares`") and the dep-map row treat it as a queued/plain-text sibling, but `book/src/L2/incremental-least-squares.md` exists. A live link would resolve. Not a defect (plain text is always safe and the entry may still be a stub), but a missed linking opportunity. Severity: cosmetic.

## Repair

### Fixes attempted

- **Finding**: [plan-kind-consistency, warning] The `edit:book/src/SUMMARY.md` block (CYCLE.md:218-220) supplies only the new line `- [ksp_solve](./L2/ksp_solve.md)` but the current SUMMARY line is `- [ksp_solve (stub)](./L2/ksp_solve.md)` (`book/src/SUMMARY.md:44`); a literal-append integrator path would leave a stale `(stub)` line and/or a duplicate TOC entry → `linkcheck2`/duplicate-link build error.
  - **Decision**: repaired
  - **Action**: Rewrote the `edit:book/src/SUMMARY.md` proposed-change block in `CYCLE.md` (proposed-changes, SUMMARY block) from a bare new-text supply into an explicit replace-in-place with named OLD/NEW lines:
    - `OLD: - [ksp_solve (stub)](./L2/ksp_solve.md)`
    - `NEW: - [ksp_solve](./L2/ksp_solve.md)`
    plus a `# REPLACE-IN-PLACE` directive comment noting that an append would create a duplicate TOC link. Verified the current `:44` text via Read before editing — it is exactly `- [ksp_solve (stub)](./L2/ksp_solve.md)`, so both OLD and NEW strings are unambiguous from context. This is a mechanical spec correction (de-stub OLD→NEW where both strings are obvious); no content authored.

- **Finding**: [skill-uptake-survey, warning] Telemetry only — the report does not name a `verify-citation-range` / `verify-rotation-citation` / `propose-rotation` skill invocation. Critic explicitly marked this non-blocking, pure presence check.
  - **Decision**: not-needed
  - **Rationale**: Telemetry-only presence check, explicitly non-blocking per the critic. Naming a retroactive skill invocation would be authoring after-the-fact provenance, not a mechanical fix — out of repair scope and not warranted (the citations were independently re-verified clean by the critic).

The other six checks were `pass` from the critic and required no repair (`not-needed`).

### Unrepairable findings

None. Both critic warnings are resolved (one repaired, one not-needed). The three non-defect observations the critic recorded are correctly out-of-scope / informational and route to the existing OQ-ledger entries the report already filed:
- L3-entry citation drift (`:463`/`:563`) — already filed as an OQ by the report; the L3 entry is append-only post-integration, so no edit here (out of repair authority + correct routing already in place; downstream lowering-verifier/lifter pass).
- L2 index Working Note staleness — out-of-scope (index prose, not the operator row); report already routed to a layer-intro-author refresh.
- `incremental-least-squares` plain-text-vs-live-link — cosmetic missed-linking opportunity, not a defect; plain text is always safe.

## Suggested resolution

`ready`. Integrator notes:
- Apply the SUMMARY block as a **replace-in-place** of the line-44 `(stub)` entry per the now-explicit OLD/NEW spec — do NOT append (the directive comment in the block flags the duplicate-link build error an append would cause).
- The L2/index dep-map row block reproduces the full current row verbatim as its replacement target (well-formed); the body fence is a clean new-file/full-body write.
- The report's three filed Open questions (L3 `:463`/`:563` citation drift; L2 index Working Note staleness; `incremental-least-squares` direct-cite tightening) should be promoted to the OQ-ledger for downstream lowering-verifier / lifter / layer-intro-author passes — none block this integration.
