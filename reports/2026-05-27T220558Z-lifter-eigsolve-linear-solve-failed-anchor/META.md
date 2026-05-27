---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T22:30:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-27T22:42:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: pass-after-repair
follow_up_agent: null
---

# META: verification of lifter-eigsolve-linear-solve-failed-anchor

## Critique

### Checks run

**citation-validity: pass.** Every load-bearing citation in the report was verified against source:

- `palace/linalg/ksp.cpp:297-310` — confirmed: `BaseKspSolver<OperType>::Mult(const VecType &x, VecType &y) const` body opens at line 297, returns `void`, executes `ksp->Mult(x, y)` at line 300, then `if (!ksp->GetConverged())` at line 301 dispatches an `Mpi::Warning` at lines 303-306 with format string "Linear solver did not converge, norm(Ax-b)/norm(b) = ...". No error return, no exception, no flag set on the solver — exactly as the report claims.
- `palace/linalg/arpack.cpp:574, 580, 761, 778` — confirmed all four `opInv->Mult` call sites. Lines 573-574 (non-shift-invert linear EPS), 579-580 (shift-invert linear EPS), 761 (quadratic PEP non-shift-invert branch), 778 (quadratic PEP shift-invert branch). None query `ksp->GetConverged()` after the call — the lines immediately following are either scaling (`y1 *= 1.0 / gamma;`), projection (`opProj->Mult(y1)`), or the subsequent `Get(py, ...)` host-pointer write-back.
- `palace/linalg/nleps.cpp:514` — confirmed: `opInv->Mult(b1, x1)` is the first statement of the `deflated_solve` lambda body (lines 505-537); the lines immediately following dispatch the deflation math (`x2.conservativeResize`, dot products against the deflation basis, the Schur-complement linear algebra). No `ksp->GetConverged()` query.
- `palace/linalg/slepc.cpp:1858, 1965, 1978, 2076, 2159` — confirmed all five SLEPc shell-matrix callback sites via direct grep on `opInv->Mult` in slepc.cpp (the grep returns exactly these five lines and no others). Spot-read of lines 1850-1880, 1960-1985, 2070-2090, 2155-2170 confirms each call is immediately followed by scaling/projection, no `GetConverged` query. The only `EPSGetConverged` / `PEPGetConverged` / `NEPGetConverged` / `SVDGetConverged` calls in the file (lines 276, 310, 695, 1178, 1525) are all on the outer `eps` / `pep` / `nep` / `svd` PETSc object after `EPSSolve` / etc., not on the inner `opInv` Krylov solver.
- `palace/linalg/slepc.cpp:687-709` — confirmed: `SlepcEPSSolverBase::Solve()` body. `EPSSolve(eps)` at 694, `EPSGetConverged(eps, &num_conv)` at 695, then `EPSConvergedReasonView` print at 699 (print-only, no status capture). No reference to the inner `opInv` solver's status.
- OQ ledger citations — `scaffolding/open-questions.md:1342-1351` covers the yaml fence-to-fence block for `eigsolve-l1-operator-rough-in-candidate` (verified at lines 1342-1351); `scaffolding/open-questions.md:1470-1479` covers the cycle-009 `eigsolve-linear-solve-failed-status-anchor` block (verified — yaml at 1470-1477, prose at 1479; line 1478 is empty between yaml close and prose). The cited ranges are accurate.

The five-call-site claim is exactly right (4 ARPACK + 1 NLEPS + 5 SLEPc = 10 total in the report's prose; but the SLEPc 5 are the shell-matrix callback distinct sites and the report's "five eigensolver-side opInv->Mult call sites" phrasing is loose in §Summary — see cross-reference-integrity below). All cited line numbers resolve.

**surface-or-evidence: pass.** This is a refinement-shaped proposal (modifies the existing `book/src/L1/eigsolve.md` chapter) and meets the surface-AND-rotation_claim bar via a different route: the proposal is **pure evidence backfill** — it surfaces the existing rough-in caveat into additional reader touchpoints (§Signature, §Status, §Algebraic-laws §3, §"Laws that explicitly do not hold") and adds two new negative-anchor citations (`ksp.cpp:297-310` and the 5 SLEPc shell-matrix call sites) that were not in the chapter's evidence list. The chapter's semantic content is unchanged (no new variant axes, no new laws, no changed signature, no changed status); the four prose edits replace rough-in caveats with resolved-with-annotation prose pointing at the negative anchors. Retroactive evidence backfill is explicitly allowed under the surface-or-evidence check.

**rotation-quality: pass — not the primary check axis for this dispatch.** This is a re-anchor / annotation lift, not a structural rotation; there is no L_{n+1}→L_n rewrite being proposed (the future `eigsolve-mutation-rotation` L1>L0 theme is queued but deferred to a separate dispatch). The L1 form is unchanged. What the dispatch does propose is a **classification annotation** ("the `LinearSolveFailed` variant is constructed by the L1 form, not L0-derived") — this is a categorisation of an existing structural distinction (the four-way `EigStatus` vs the three L0-anchored cases), and it is consistent with the cycle-009 harvester's prose intent. No 1:1 renaming; no spurious rotation claim made. Pass.

**variant-axis-coverage: pass.** The chapter's existing variant axes (problem-type, spectrum-target, spectral-transformation, scaling; plus the three collapsed axes orchestration-pattern / SLEPc-internal-method / SLEPc-problem-type) are unchanged. The dispatch explicitly does not introduce a new variant axis around `LinearSolveFailed` (the `EigStatus` sum-type is part of the result-record type, not a `EigSolver`-construction-time variant). The status-block annotation correctly scopes the `EigStatus` four-way as a sum-type completeness claim, not a variant axis. The three sibling cycle-009 OQs (`eigsolve-scaling-coordinate-convention`, `eigsolve-initial-space-axis-placement`, `eigsolve-iteration-count-result-field`) remain open and are explicitly noted as out of scope per "one theme per invocation" — the discipline is observed.

**cross-reference-integrity: warning.** Three coherence issues across the six proposed edits, none blocking:

1. **Edit 1's `[old]:` block is non-contiguous.** The report's edit shows:
   ```
   [old]:
   EigStatus = Converged | PartialConverged | MaxIterReached | LinearSolveFailed
   ```
   Shape contract (bunsen-style, named axes):
   ```
   But in the source file (lines 44-47), this is not a contiguous text block: line 44 is `EigStatus = ...`, line 45 is the closing ` ``` ` fence, line 46 is blank, line 47 begins `Shape contract...`. The `[old]:` text as shown skips lines 45-46. Two readings are possible: (a) the report intended `[old]:` to mean "find this text starting here, replace with this text starting here, leave everything between intact" (which is not how the rest of the report's `[old]:`/`[new]:` blocks read in Edits 2/3/4/5/6 — those are contiguous-block replacements); (b) the report intended Edit 1 as a contiguous replacement of lines 44-47 but the displayed `[old]:` and `[new]:` blocks elide the intermediate ` ``` ` and blank line. Either reading leaves the integrator-per-report needing to disambiguate. The simpler integrator-side fix: spell out the contiguous block explicitly (include the ` ``` ` fence + blank line between the two anchor lines in both `[old]:` and `[new]:`). This is a mechanical clarity issue, not a semantic one.

2. **"Five eigensolver-side opInv->Mult call sites" — phrasing slip.** The §Summary at line 19 says "five eigensolver-side `opInv->Mult` call sites" (matching the prose in Edits 1, 2, 5 and the OQ append in Edit 6); but the actual count is **10** distinct call sites (4 ARPACK + 1 NLEPS + 5 SLEPc). The dispatch's own enumerations (e.g., Edit 1's prose body, Edit 2's prose body, Edit 5's evidence rows, Edit 6's prose) all list `arpack.cpp:574, 580, 761, 778` (4) + `nleps.cpp:514` (1) + `slepc.cpp:1858, 1965, 1978, 2076, 2159` (5) = 10. The "five" phrasing in the §Summary likely conflates "five categories" (ARPACK linear, ARPACK quadratic, NLEPS, SLEPc EPS, SLEPc PEP/NEP) or counts only the SLEPc subset. The semantic content is correct everywhere (all 10 sites are enumerated correctly in each edit body); only the §Summary's prose count is off. A repairer fix is to change "five eigensolver-side `opInv->Mult` call sites" → "ten eigensolver-side `opInv->Mult` call sites across the three orchestrations" (or "nine call sites in ARPACK+NLEPS+SLEPc shell-matrix callbacks" if NLEPS is excluded from the count). Three of the four edits themselves use phrasings that suggest "all five eigensolver-side `opInv->Mult` call sites" — Edit 6's resolution narrative also says "all five". This phrasing would land in `book/src/L1/eigsolve.md` if applied verbatim.

3. **Edit 6's OQ-status-flip ambiguity.** The dispatch notes that the yaml `status: open` line in the original OQ entry is *not* part of proposed-changes, on the grounds that the OQ ledger has a "do not edit original entries" convention. But the verified state of the OQ ledger at lines 1342-1351 (the predecessor OQ `eigsolve-l1-operator-rough-in-candidate`) shows `status: partially-answered` with `partial_answer_at: cycle-009` and `partial_answer_in: reports/...` — clearly the ledger **does** permit status-and-partial-answer updates to the yaml block of existing entries (the precedent is in the ledger itself). The dispatch's claim that yaml updates are "a meta-phase concern" is over-cautious. This is a process-policy disagreement, not a content error; flagging for repairer/integrator awareness. The integrator-per-report could choose to mark the OQ `partially-answered` (with `partial_answer_at: cycle-010` / `partial_answer_in: reports/...`) by analogy with the precedent, rather than leaving the resolution prose appended after the open yaml.

All `[link]` references in the proposed edits resolve: `palace/linalg/ksp.cpp:297-310`, the 10 source line citations, the cycle-008 OQ slug, the cycle-009 OQ slug, the future `eigsolve-mutation-rotation` theme slug (queued, not yet existing — correctly marked as a forward reference per CLAUDE.md "Accumulate surface with embedded friction"), and the §Signature / §Algebraic-laws §3 / §"Laws that explicitly do not hold" / §Status section anchors in the existing chapter (all confirmed present in the verified read of `book/src/L1/eigsolve.md`).

**edge-label-fidelity: pass.** The dispatch carries no L_{n+1}→L_n edge label (it is an annotation lift on a single L1 entry, not a lowering theme). The status-block annotation in Edit 4 explicitly marks `LinearSolveFailed` as "constructively introduced by the L1 form" — this is the correct L-level framing (the construction happens at L1; the L0 surface has only the three observable variants). The proposed Algebraic-laws §3 edit (Edit 2) and the "Laws that explicitly do not hold" edit (Edit 3) both preserve the existing chapter's L0-vs-L1 distinction prose. The eventual L1>L0 theme is correctly named in all four edits (`eigsolve-mutation-rotation`) and the direction (L1 form lowers into L0 form) matches the CLAUDE.md "layers are defined high→low" invariant.

**plan-kind-consistency: pass.** The dispatch is correctly classified as a `lifter` dispatch (re-anchor of an existing rough-in chapter against new evidence; preserves operator semantics, lifts the resolution into the chapter surface). The proposed-changes block contains four prose edits + one evidence-section append + one OQ append — appropriately mechanical/decisional scope for a lifter. No new operator definitions, no new themes, no new laws — discipline observed. The §Discipline notes section explicitly grounds the dispatch in the lifter role-spec ("preserve the theme's narrative; firm up the vocabulary").

**skill-uptake-survey: pass with new pattern flagged.** The dispatch identifies a **negative-anchor citation pattern for L1-constructive cases** (citing L0 lines that demonstrate the *absence* of a behaviour) and surfaces it as analogous to (but distinct from) the obstruction-theme negative-anchor pattern at `book/src/L1-L0/minres-iteration.md` / `book/src/L1-L0/bicgstab-iteration.md`. Verification: those two obstruction themes do use `verdict: negative-anchor` in their evidence rows (confirmed by grep). The pattern proposed by this dispatch is distinguishable on three axes — granularity (per-status-variant vs per-operator), purpose (justify a sum-type variant as L1-constructive vs justify an entire L1-L0 theme as obstruction), and rhetorical shape (demonstrate `void` return / missing query vs demonstrate stub-default / `MFEM_ABORT`). The §Open-questions-and-caveats item 4 flags this for meta-phase consideration if the pattern recurs (e.g., on the sibling `eigsolve-iteration-count-result-field` OQ). The flagging is appropriate — not over-eager skill-promotion, just telemetry. No skill-candidate append to `scaffolding/skill-candidates.md` is needed at this point; recurrence on a second case would justify promotion. Pass (telemetry only).

### Issues found

**Issue 1 (Edit 1, low-medium severity)** — non-contiguous `[old]:` block. Edit 1's `[old]:` and `[new]:` skip the closing ` ``` ` fence and the blank line between lines 44 and 47 of the source file. The integrator-per-report will need to spell out the contiguous block (or treat `[old]:` as a regex / multi-anchor match). Mechanical fix: rewrite Edit 1's `[old]:` to include the ` ``` ` fence + blank line; rewrite Edit 1's `[new]:` correspondingly so the callout block lands between them. Located at `CYCLE.md` Edit 1, lines 29-43.

**Issue 2 (§Summary + Edits 1/2/5/6 prose, low severity)** — incorrect call-site count in prose. The §Summary at line 19 and the prose body of Edits 1, 2, and 6 use the phrasing "five eigensolver-side `opInv->Mult` call sites" while the enumerated list in all edits totals **ten** distinct sites (4 ARPACK + 1 NLEPS + 5 SLEPc shell-matrix). The enumerations themselves are correct (and verified against source); only the summary count is off. If applied verbatim, the misleading count would land in `book/src/L1/eigsolve.md`. Mechanical fix: replace "five" with "ten" (or with "across the three orchestrations" if a categorical count is intended). Located at `CYCLE.md` §Summary (line 19, line 21), Edit 1 body (line 39), Edit 2 body (line 48), Edit 5 evidence rows (lines 71-74 — these enumerate correctly, only the summary-style "five" needs adjustment if it appears here; it does not, the evidence rows are clean), Edit 6 OQ-append prose (line 85).

**Issue 3 (Edit 6, low severity)** — OQ yaml-status-flip is more permissible than the dispatch claims. The cycle-009 precedent at lines 1342-1351 of the OQ ledger shows status updates to existing yaml blocks (`status: open` → `status: partially-answered` with `partial_answer_at` and `partial_answer_in` fields added). The dispatch's claim that yaml updates are exclusively a meta-phase concern is over-cautious; the integrator-per-report could reasonably flip the status to `partially-answered` (or fully `resolved`) by analogy. This is a process-policy disagreement, not a content error; the integrator-per-report can decide. Located at `CYCLE.md` Edit 6 prose (lines 88-89) and the §Open-questions-and-caveats §1 (line 115).

**Issue 4 (informational, no severity)** — the §"Laws that explicitly do not hold" edit (Edit 3) introduces the phrasing "**L1-coordinated** termination cases (including the L1-constructive `LinearSolveFailed`)" vs "**L0-observable** termination cases". This is a useful new distinction (and consistent with the dispatch's intent), but the phrase "L1-coordinated" is not used elsewhere in the chapter or in the existing L1 corpus. If the integrator-per-report applies the edit verbatim, the new phrase will be a one-off in the L1 vocabulary. Not a blocker — flagging as terminology drift telemetry. Located at `CYCLE.md` Edit 3 body (line 55).

**Issue 5 (informational, no severity)** — Edit 5's first row update (the existing "cycle-008 OQ `eigsolve-l1-operator-rough-in-candidate`" parenthetical) changes "the dispatch target" to "the cycle-009 harvester dispatch target". This is a clarifying edit but slightly misleading: the cycle-008 OQ was actually the *cycle-009 harvester's* dispatch target (the OQ is dated `opened_at: cycle-008`, `partial_answer_at: cycle-009`). The new phrasing is correct. The new evidence rows (the cycle-009 OQ, `ksp.cpp:297-310`, the 4 ARPACK + 1 NLEPS + 5 SLEPc enumerations) are all correctly cited. No fix needed; flagging for completeness.

## Repair

### Fixes attempted

**Finding 1: cross-reference-integrity — Edit 1's `[old]:` block is non-contiguous (skips closing ``` fence and blank line at source lines 45-46).**
- Decision: **repaired**.
- Action: Rewrote Edit 1 in CYCLE.md to use the `[insert-after: <anchor>]` / `[content]:` pattern (the same pattern already in use at Edit 6) rather than `[old]:`/`[new]:`. The anchor is the closing ` ``` ` fence at source line 45 (the line immediately following the unique `EigStatus = Converged | PartialConverged | MaxIterReached | LinearSolveFailed` line); the new callout block is inserted after that anchor, displacing the existing blank line and the "Shape contract" paragraph. This avoids embedding the triple-backtick fence inside an `[old]:`/`[new]:` block (which is what caused the mechanical-clarity issue) and matches the established insert-after pattern in this report and in prior reports (`reports/2026-05-27T004641Z-abstractor-BiCGStab-L1-L0/CYCLE.md`, `reports/2026-05-27T001116Z-harvester-nrm2-L1/CYCLE.md`, etc.). A clarifying preamble was added to Edit 1 explaining the choice and citing the cycle-010 critic's flag.

**Finding 2: cross-reference-integrity — "five" vs "ten" call-site count discrepancy in §Summary and Edits 1/2/6 prose.**
- Decision: **repaired**.
- Action: Mechanical search-replace of "five eigensolver-side `opInv->Mult` call sites" → "ten eigensolver-side `opInv->Mult` call sites (4 ARPACK + 1 NLEPS + 5 SLEPc shell-matrix)" across the four affected loci in CYCLE.md:
  - §Summary (line 19, "any of the five eigensolver call sites" → "any of the ten eigensolver call sites (4 ARPACK + 1 NLEPS + 5 SLEPc shell-matrix)").
  - §Summary (line 21, "any of the five `opInv->Mult` eigensolver call sites" → "any of the ten `opInv->Mult` eigensolver call sites").
  - Edit 1 callout (rewritten as part of Finding 1; the new callout uses "ten inner `opInv->Mult(...)` call sites").
  - Edit 2 `[new]:` block ("five eigensolver-side" → "ten eigensolver-side (4 ARPACK + 1 NLEPS + 5 SLEPc shell-matrix)").
  - Edit 6 `[content]:` block (Resolved-narrative; "all five eigensolver-side" → "all ten eigensolver-side (4 ARPACK + 1 NLEPS + 5 SLEPc shell-matrix)").
  - Three additional internal-prose loci that were not part of the critic's enumerated list but contain the same content error and would propagate confusion if unrepaired: §Supporting-evidence (line 121, "confirmed five eigensolver-side" → "confirmed ten eigensolver-side ..."); §Open-questions-and-caveats §3 (line 130, "at the five call sites" → "at the ten call sites"); §Open-questions-and-caveats §4 (line 132, "the five eigensolver-side call sites" → "the ten eigensolver-side call sites").
- The unrelated "five edits surface the resolution into the chapter" at §Discipline-notes line 103 was deliberately NOT changed — that "five" correctly counts the number of edits to `book/src/L1/eigsolve.md` (Edits 1-5), which remains 5 even after the new Edit 7 was added (Edit 7 hits `scaffolding/open-questions.md`, not the chapter).

**Finding 3: cross-reference-integrity — OQ yaml-status-flip framed as "meta-phase only", over-cautious vs. cycle-009 precedent.**
- Decision: **repaired**.
- Action: Added a new **Edit 7** to CYCLE.md proposing a `[old]:`/`[new]:` yaml-block update on the `eigsolve-linear-solve-failed-status-anchor` OQ — flipping `status: open` to `status: partially-answered` with `partial_answer_at: cycle-010` and `partial_answer_in: reports/2026-05-27T220558Z-lifter-eigsolve-linear-solve-failed-anchor/`. The repair note cites the cycle-009 precedent at `scaffolding/open-questions.md:1342-1351` (the predecessor OQ `eigsolve-l1-operator-rough-in-candidate` uses exactly this pattern: `status: partially-answered` + `partial_answer_at: cycle-009` + `partial_answer_in: reports/...`). The status is `partially-answered` (not fully `resolved`) because the materialising L1>L0 theme (`eigsolve-mutation-rotation`) is still deferred to a cycle-010+ abstractor — analogous to how cycle-009 closed the harvester-rough-in part of the predecessor OQ while leaving firm-promotion follow-ups partially-answered. Also updated the explanatory prose between Edit 6 and §Discipline-notes (which previously claimed "yaml-status update is a meta-phase concern") and the §Open-questions / caveats §1 bullet (which previously claimed the yaml flip was intentionally NOT part of proposed-changes), to reflect the new proposed-changes scope and retain an audit trail of the cycle-010 critic/repairer adjustment.

**Finding 4 (informational, no severity) — "L1-coordinated" phrase one-off in Edit 3.**
- Decision: **not-needed**.
- Rationale: Critic flagged as terminology drift telemetry, not a defect. The phrase "L1-coordinated termination cases" is the natural complement to "L0-observable termination cases" introduced in the same edit; both phrases land in a single bullet to mark a deliberate distinction, and rewriting either would be substantive content authoring (out of repairer scope). The phrase is consistent with the cycle-006/007/008 L4-monadic-coordination vocabulary in `book/src/L4/`. If the term proves orphaned across the L1 corpus over cycle-011+ work, a same-layer-cross-cutter dispatch can audit. No mechanical fix.

**Finding 5 (informational, no severity) — Edit 5 row-1 wording adjustment ("the cycle-009 harvester dispatch target").**
- Decision: **not-needed**.
- Rationale: Critic notes the new phrasing is correct and the citation is accurate. Not a defect.

### Unrepairable findings

None. All cross-reference-integrity warnings were within mechanical repair scope (anchor-pattern rewrite, mechanical search-replace, and a yaml-block update with explicit prior-art precedent in the same ledger file).

## Suggested resolution

`overall_status: pass-after-repair`. The integrator-per-report can apply CYCLE.md's seven proposed edits (Edits 1-5 → `book/src/L1/eigsolve.md`; Edit 6 → `scaffolding/open-questions.md` append; Edit 7 → `scaffolding/open-questions.md` yaml-block update). The Edit 1 reframe to insert-after pattern should be smoother for the per-report integrator than the prior non-contiguous [old]/[new] block. The Edit 7 yaml flip mirrors the cycle-009 precedent for predecessor-OQ resolution and is unambiguously traceable to this report. Notes for integrator:
- Edit 1's anchor is the closing ` ``` ` fence on source line 45 (the line right after the unique `EigStatus = ...` line at line 44). Integrator should match the fence by anchoring on the unique preceding line if the bare ` ``` ` is ambiguous in the source file.
- The Edits 6 and 7 both modify `scaffolding/open-questions.md` — Edit 6 appends prose after the OQ's existing prose body; Edit 7 updates the yaml block. Both can be applied in either order (they touch non-overlapping line ranges); applying Edit 7 first is recommended so a downstream sweep that reads only the yaml block sees the updated status before encountering the appended prose.
