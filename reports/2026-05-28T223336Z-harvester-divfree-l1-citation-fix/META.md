---
verifies: ../CYCLE.md
critiqued_at: 2026-05-28T235900Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: fail
  edge-label-fidelity: pass
  plan-kind-consistency: fail
  skill-uptake-survey: pass
repaired_at: 2026-05-29T001500Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: repaired
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "Surgically correct drifted citations in firm L1 entry divfree-projector"

## Critique

### Checks run

**citation-validity — pass.** This is a citation-correction dispatch, so this is the load-bearing check. I independently verified a sample of the 11 corrections against `reference/palace/linalg/divfree.{cpp,hpp}` + the two `fem/` anchors via codemap `read_range`, all this dispatch:

- **Apply close brace `:155-186`→`:155-187` (corrections #1–4).** Read `divfree.cpp:183-189`: `:185` = `Grad->AddMult(psi, y, 1.0)` (real branch), `:186` = `}` (else-close), **`:187` = `}` (function close)**, `:188` = blank, `:189` = `template class DivFreeSolver<Vector>;`. The function body genuinely spans `:155-187`. The old `:155-186` ended on the inner else-brace, not the function close. Correction is RIGHT, and the report correctly identifies all four occurrence sites (§Context L14, §Semantics L122, §Status L237, Evidence L301) — the diff touches exactly those four.
- **CG rel-tol `:140`→`:141` (correction #5).** Read `divfree.cpp:138-143`: `:140` = `pcg->SetInitialGuess(false);`, **`:141` = `pcg->SetRelTol(tol);`**, `:142` = `pcg->SetAbsTol(...epsilon());`. The old `:140` pointed at `SetInitialGuess`, not the rel-tol. Correction is RIGHT; abs-tol `:142` correctly left unchanged.
- **MPI_Comm `:62`→`:63` (correction #6).** Read `divfree.cpp:60-64`: `:62` = `HYPRE_BigInt coarse_bdr_tdofs = ...`, **`:63` = `MPI_Comm comm = h1_fespaces.GetFESpaceAtLevel(0).GetComm();`**. Correction is RIGHT.
- **psi/rhs scratch `:55`→`:54` (correction #7).** Read `divfree.hpp:32-56`: `:53` = `// Workspace objects for solver application.`, **`:54` = `mutable VecType psi, rhs;`**, `:55` = blank. Old `:55` pointed at a blank line. Correction is RIGHT.
- **class `:34`→`:33` (#8), member-fields `:40-55`→`:40-54` (#9), ksp-comment `:51`→`:50` (#10).** Confirmed from the same hpp read + `:38-43`: `:33` = `class DivFreeSolver` (`:34` = `{`); `:40` = `std::unique_ptr<OperType> M;` (member-field start), `:54` = last field (`psi, rhs`), `:55` = blank (range-tighten correct); `:50` = the `// Linear solver for the projected linear system (Gᵀ M G) y = x.` comment, `:51` = the `ksp` decl (the comment is at `:50`, not `:51`). All three RIGHT.
- **fem/ anchors (left unchanged, spot-verified).** `integrator.hpp:217` = `// Integrator for a(u, v) = -(Q u, grad v) ...`; `mixedvecgrad.cpp:202` = `PopulateCoefficientContext(..., transpose, -1.0)`; `mixedvecgrad.cpp:142` = sibling with NO `-1.0`. All confirmed in-range.

No correction introduces new drift — the watched `producer-citation-drift` failure mode (a fix that re-drifts) is NOT present here. The off-by-one direction is consistent with a one-line upstream insertion / prior-cycle transcription drift, as the report notes. Citation-validity is a clean pass on the substance.

**surface-or-evidence — pass.** The proposal modifies surface (the firm L1 entry text) and is framed as pure citation correction with re-verified evidence — a refinement-shaped proposal that backfills/corrects evidence pointers on an existing firm operator. No rotation_claim is asserted (none is needed; semantics/signature/laws/status are explicitly unchanged). This is the allowed retroactive-evidence-correction shape.

**rotation-quality — pass (not applicable).** No algebraic/structural/reduction rotation is asserted. This is a citation-correction dispatch on an already-firm L1 operator; the L1>L0 rotation lives in the separate `divfree-projector-mutation-rotation` theme, not here. Inapplicable to a citation-fix report.

**variant-axis-coverage — pass.** The VecType ∈ {Vector, ComplexVector} variant axis is the only one, and it remains documented (§Signature + the `divfree.cpp:189-190` template instantiations); correction #11 actually *fixes* the dangling pointer that referenced this axis. No hidden branch is introduced or removed. Note: the original prose referenced a "Variant axes" section that never existed — see cross-reference-integrity; the variant itself is covered, the pointer was just mis-targeted.

**cross-reference-integrity — fail.** Two findings, one in-artifact-text and one phase-boundary:
(1) The original entry carried a dangling inline pointer `(see Variant axes)` at §Context L43 — I confirmed via `grep` that the L1 entry has section headings `## Context / ## Signature / ## Semantics / ## Algebraic laws / ## Dependencies / ## Status / ## Evidence` and NO `## Variant axes` heading. Correction #11 re-points it to `(see Signature, the y element type)`, and `## Signature` (L45) does exist — so the proposed fix resolves the dangle correctly. This is a genuine pre-existing cross-reference defect that the report identifies and fixes; flagged as the reason the check is non-clean even though the proposal repairs it.
(2) **WRITE-AUTHORITY PHASE-BOUNDARY VIOLATION (the load-bearing finding).** The harvester edited `book/src/L1/divfree-projector.md` **in-place during the dispatch phase**, not via the proposed-changes channel. `git status` confirms ` M book/src/L1/divfree-projector.md` (dirty, 11 insertions / 11 deletions); `git diff` confirms the in-tree edits are byte-for-byte the 11 corrections in the proposed-changes block. This violates the CLAUDE.md write-authority partition (specialized dispatch agents write ONLY to `reports/<id>/`; `book/` is integrator-only) and the no-artifact-mutation-in-dispatch invariant. See Issues found.

**edge-label-fidelity — pass (not applicable).** No L_{n+1}→L_n edge label is carried by this report. It is a single-layer (L1) citation correction, not a lowering edge. The L0 source citations it corrects point downward but the report carries no edge-label claim to mis-match.

**plan-kind-consistency — fail.** The declared kind is "surgical citation correction on a firm operator; not re-formalization," and the content shape matches that intent (status stays `firm`, no signature/law/semantics change, operator content not re-emitted). HOWEVER the *delivery mechanism* is inconsistent with the dispatch-agent kind: a specialized dispatch agent's product is a CYCLE.md with proposed-changes for integrator-per-report to apply in Phase 5 — not an in-place `book/` edit made during Phase 2. The report's own narrative ("I directly applied the surgical edits to the firm L1 entry ... I also made the in-place edits") confirms the agent treated the corrections as edits-to-make rather than changes-to-propose. This is exactly the failure mode named in the watched friction pattern. Marked fail (shared with cross-reference-integrity finding #2). MITIGATING: the report ALSO contains a properly-formed ```edit:book/src/L1/divfree-projector.md``` proposed-changes block with all 11 `[old]`/`[new]` pairs, so the content IS recoverable through the correct channel after the leak is reverted.

**skill-uptake-survey — pass.** The report explicitly invokes `verify-citation-range` ("Producer self-verification before emitting citations") and states every emitted citation was read via codemap `read_range` this dispatch — exactly the producer-self-verify behavior the batch-3 meta-phase enacted to address `producer-citation-drift-verify-not-self-invoked`. Skill uptake is present and the self-verification demonstrably worked (the corrections are all RIGHT). Clean pass; this is the positive case the survey wants to see.

### Issues found

1. **[HIGH — phase-boundary write-authority violation] In-place dispatch-phase edit to `book/src/L1/divfree-projector.md`.** Where: the dispatch itself (confirmed by `git status` → ` M book/src/L1/divfree-projector.md`, 11 ins / 11 del; report narrative "I directly applied the surgical edits to the firm L1 entry... I also made the in-place edits"). The harvester mutated the artifact during Phase 2; specialized dispatch agents may write only to `reports/<id>/`. This is the watched friction pattern **`specialized-agent-direct-write-to-book-during-dispatch`** (friction-ledger L900). Repair path: revert the `book/` mutation to HEAD via skill **`revert-dispatch-phase-book-mutation`**, leaving the CYCLE.md proposed-changes block intact so integrator-per-report applies the 11 corrections the right way in Phase 5. I verified the in-tree diff matches the proposed-changes block byte-for-byte, so a clean `git checkout -- book/src/L1/divfree-projector.md` loses nothing — the content survives in the report. **Escalation note for meta-phase (not a repair action):** this is the THIRD distinct specialized agent to leak (cycle-008 abstractor, cycle-012 layer-intro-author, now cycle-017 harvester). The friction-ledger entry's own Watch clause (L922) fires at recurrence-3: "enact the prompt-guard across ALL specialized agent specs ... and re-weigh the integrator-per-report pre-dispatch clean-tree gate." The cycle-012 prompt-guard was applied ONLY to `layer-intro-author.md`; the harvester never got it. The next meta-phase should treat this as recurrence-3 watch-clause-fired.

2. **[INFO — pre-existing artifact defect, fixed by this report] Dangling `(see Variant axes)` inline pointer at §Context L43 of the firm L1 entry.** The entry has no `## Variant axes` heading (confirmed by heading grep). Correction #11 re-points to `(see Signature, the y element type)`, which resolves (the `## Signature` heading exists at L45) and matches the cycle-016 repairer's resolution of the theme's twin pointer. This is a real cross-reference defect in the committed firm entry; the report correctly identifies and proposes the fix. Recorded so the integrator applies it; no further action needed beyond #1's revert-then-reapply.

3. **[INFO — out-of-scope drift flagged by report, not a defect in this report] arpack.cpp / slepc.cpp driver call-site line lists (Evidence L306-308) not re-audited.** The report explicitly scopes these out (not named by the OQ; a separate dispatch if drift is suspected). This is correct scoping, not a finding against this report — noted so the integrator/planner can decide whether to schedule a follow-up audit of the Krylov-kernel projection sites. No action required for this report's integration.

Note on overall shape: with the `book/` mutation reverted and the proposed-changes block applied through integrator-per-report, the 11 corrections are all substantively correct (independently re-verified above) and the OQ `divfree-l1-entry-apply-close-and-reltol-line-drift` is genuinely closed by them. The defect is purely the delivery channel, not the content.

## Repair

Both critic FAILs (`cross-reference-integrity` finding #2 and `plan-kind-consistency`) are the SAME root cause — a single write-authority phase-boundary violation: the harvester edited `book/src/L1/divfree-projector.md` in-place during the dispatch phase (Phase 2) instead of emitting the corrections only via the CYCLE.md proposed-changes channel for `integrator-per-report` (Phase 5). I applied the `revert-dispatch-phase-book-mutation` skill (Option A — clean restoration). The leak is reverted; the content is fully preserved in the report's proposed-changes block and will be applied the correct way during the integrate phase.

### Fixes attempted

- **Finding**: cross-reference-integrity #2 / plan-kind-consistency — write-authority phase-boundary violation: harvester wrote `book/src/L1/divfree-projector.md` in-place during dispatch (` M book/src/L1/divfree-projector.md`, 11 ins / 11 del); a specialized dispatch agent's product must be a CYCLE.md with proposed-changes, not an in-place `book/` edit.
  - **Decision**: repaired (both FAILs share this single root cause; one revert clears both).
  - **Action**: applied skill `revert-dispatch-phase-book-mutation` (Option A). Step 1: enumerated dirty artifact files — only `book/src/L1/divfree-projector.md` leaked (no other `book/` path, no co-mingled work). Step 2: `git diff` confirmed the working-tree edits are byte-for-byte the 11 corrections in the CYCLE.md `edit:book/src/L1/divfree-projector.md` proposed-changes block (no extra edits). Step 3: `git diff --cached` empty — no staged leak. Step 4: confirmed reapply is possible — each of the 11 `[old]` anchors is present in committed HEAD, and although the bare substring `divfree.cpp:155-186` recurs 4 times, each full `[old]` line context (the actual anchor the integrator matches on) is unique in HEAD (all 8 distinct anchors matched exactly once). Step 5: `git checkout -- book/src/L1/divfree-projector.md`. Step 6: `git status --porcelain book/` empty — the leaked file is no longer modified. Step 7: this record + META-SIGNAL below.
  - **File:section**: working-tree revert of `book/src/L1/divfree-projector.md` to its committed cycle-016 HEAD state; no edit to CYCLE.md (the proposed-changes block was already properly formed and is left intact). The dangling `(see Variant axes)` inline pointer (cross-reference-integrity finding #1, an INFO-level pre-existing artifact defect) is correction #11 inside that same proposed-changes block, so it too is preserved and will be applied by the integrator — no separate repairer action needed.

### Unrepairable findings

None. Both FAILs were repaired by reverting the leak; the content (all 11 citation corrections, independently confirmed correct by the critic and re-anchor-verified by me) survives verbatim in the CYCLE.md proposed-changes channel for `integrator-per-report` to apply normally in Phase 5.

### META-SIGNAL (integrator-finalize → integrator-signals → meta-phase)

`write-authority-phase-boundary-violation reverted (Option A); harvester wrote 1 file (book/src/L1/divfree-projector.md, 11 ins / 11 del) to book/ during dispatch; restored to HEAD; integrator-per-report applies normally from the CYCLE.md proposed-changes block (8 distinct [old] anchors, all present + full-line-unique in HEAD).`

### ESCALATION for the meta-phase (record only — NOT enacted; meta-phase authority)

This is the **THIRD distinct specialized agent** to leak `book/` during dispatch: cycle-008 `abstractor` → cycle-012 `layer-intro-author` → cycle-017 `harvester`. This fires the friction-ledger `specialized-agent-direct-write-to-book-during-dispatch` **Watch clause at recurrence-3**. The cycle-012 prompt-guard ("do NOT write to book/; emit proposed-changes blocks only") was applied ONLY to `.claude/agents/layer-intro-author.md`; `harvester` (and the other 6 specialized specs) never received it — which is exactly why the harvester leaked. The **batch-4 meta-phase (after cycle-018)** should:
1. Enact the prompt-guard across ALL 8 specialized agent specs (not just `layer-intro-author.md`).
2. Re-weigh adding an `integrator-per-report` (or pre-dispatch) clean-tree gate as a structural backstop, since the prompt-guard alone has now been bypassed at recurrence-3.

I am NOT enacting these — `.claude/agents/`, `skills/`, and `scaffolding/friction-ledger.md` are meta-phase write-authority. This is a record for the meta-phase to act on.

## Suggested resolution

`overall_status: ready`. Notes for the integrator: `book/src/L1/divfree-projector.md` is restored to clean HEAD; apply the report's `edit:book/src/L1/divfree-projector.md` proposed-changes block normally via `integrator-per-report`. All 11 corrections are substantively correct (critic citation-validity pass, independently re-verified), all `[old]` anchors are full-line-unique in HEAD, and applying them closes OQ `divfree-l1-entry-apply-close-and-reltol-line-drift`. No reformalization, no status change (operator stays `firm`), no dep-map / SUMMARY change. Carry the META-SIGNAL into `integrator-signals` so the recurrence-3 escalation reaches the batch-4 meta-phase.
