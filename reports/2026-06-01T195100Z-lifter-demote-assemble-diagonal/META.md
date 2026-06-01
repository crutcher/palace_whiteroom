---
verifies: ../REPORT.md
critiqued_at: 2026-06-01T200918Z
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
repaired_at: 2026-06-01T201530Z
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
overall_status: ready
follow_up_agent: null
---

# META: verification of "Demote `assemble-diagonal` degenerate theme pair to in-line notes"

## Critique

### Checks run

**citation-validity — pass.** Ran `tools/citecheck/citecheck.py --scan` on the report (27 ok / 2 "failing") and `--anchor` on the six load-bearing pinpoints. The two scan flags are NOT defects: `operator.cpp:139` is `[AMBIG]` only because the report writes it as a bare basename in one prose sentence (Discipline note line 289), while every *citation* occurrence is full-pathed (`palace/fem/libceed/operator.cpp:139`); `reciprocal.md:25` is likewise a bare-basename prose mention, full-pathed where load-bearing. All six load-bearing anchors resolve in-range on-disk: `rap.cpp:163-164` (`convergent` @163), `test-libceed.cpp:367-376` (`rtol` @371,375), `palace/fem/libceed/operator.cpp:139` (`CeedOperatorLinearAssembleAddDiagonal` @139), `hypre.cpp:88` (`hypre_CSRMatrixExtractDiagonal` @88), `jacobi.hpp:15-16` (`approximate` @16), `rap.cpp:174` (`AbsMultTranspose` @174). The report carries no `verified_against:` YAML block, so that sub-check is not applicable. Every claim in the in-line notes is an inherited transitive citation through the firm L1 home (the edge is identity, so no new L0 claim is made) and each carries its pointer.

**surface-or-evidence — pass.** This is a refactor-pass demotion under the 2026-06-01 vocabulary-shift redirect, not a refinement proposal. It modifies surface (deletes two theme files; rewrites §Context / §"Lowers to" / §"Downward" prose on `L3/assemble-diagonal.md` and `L2/assemble-diagonal.md`) and is grounded in the cited degeneracy evidence (the two deleted themes' own §"The rewrite" tables, "total and bijective on the body", every row `Identity`). No fresh rotation_claim is asserted without surface; the surface is the demotion itself. Pass.

**rotation-quality — pass (by design: the deleted edges are confirmed degenerate, which is the demotion's premise).** I independently read both deleted theme files. `assemble-diagonal-body-identity.md` §"The rewrite (L3 → L2)" (lines 96-104) maps all seven rows `Identity` and states "total and bijective on the body". `assemble-diagonal-leaf-identity.md` §"The rewrite (L2 → L1)" (lines 102-108) maps all five rows `Identity` and states "total and bijective on the leaf". Both are genuine identity-in-named-terms lowerings (same signature `assemble_diagonal :: LinearOperator[N, N] -> Tensor[N]`, same six laws, same four non-laws, same variant profile across the edge) — i.e. the vocabulary genuinely failed to shift, which is exactly the §1d smell the redirect prescribes demoting. D3 did NOT delete a substantive theme: neither carried a non-trivial rewrite, a state-hiding, a coarser substitution, or a re-fusion step (unlike e.g. `divfree-projector-leaf-identity`'s `AddMult` re-fusion, explicitly contrasted). The demotion is the correct redirect-prescribed resolution.

**variant-axis-coverage — pass.** The operator's variant profile (one orthogonal element-type axis + one absorbed operator-representation axis) is preserved verbatim in both in-line notes and was already covered in the surviving L3/L2 operator entries. No variant combination is hidden by the demotion; the demotion touches lowering-edge prose only, not the variant inventory.

**cross-reference-integrity — warning.** Build-readiness is sound on the assemble-diagonal scope: both deleted slugs' inbound references are accounted for — the two SUMMARY rows (located on-disk at `SUMMARY.md:55,101`) removed, the two dangling live-link index rows (`L3-L2/index.md:21`, `L2-L1/index.md:22`) removed (anchors confirmed byte-exact), and the two plain-text inbound mentions (`L3/reciprocal.md:150`, `L2-L1/normalize-leaf-identity.md:47`) re-anchored (anchors confirmed byte-exact). Fence parity is clean (28 markers, 14 balanced blocks; 2 `delete:` + 12 `edit:`; no nested-`text`-fence). The in-line note bodies are correctly authored INSIDE their `edit:` `[new]` fences (no firm-body-outside-fence defect). The **warning** is the cross-dispatch coordination collision flagged in §Issues: D3's edit #6b re-anchors a line inside `L2-L1/normalize-leaf-identity.md`, a file that the sibling D6 (`reports/2026-06-01T195100Z-lifter-demote-normalize/CYCLE.md` lines 8, 48) DELETES this same cycle. Build stays green either way (the file vanishes entirely), but D3's edit anchor will not exist if D6 applies first.

**edge-label-fidelity — pass.** Both in-line notes' edge labels are exact: the §"Downward to L2" note on the L3 entry discusses the L3>L2 edge; the §"Downward to L1" note on the L2 entry discusses the L2>L1 edge. The prose narrates each rewrite forward (L3→L2, L2→L1), consistent with the high→low discipline. No label/prose mismatch.

**plan-kind-consistency — pass.** Declared as a lifter demotion (re-anchor degenerate theme pair to in-line notes). The content matches: deletions + in-line-note adds + re-anchors + dangling-row removal, with consolidated tallies correctly DEFERRED to D7 (only the two build-breaking live-link rows removed, not the count prose). The scope discipline ("standalone operator-to-data leaf, NO fold-parent — operator entries not slated for fold-collapse, no held chapter touched") is consistent with a clean demotion.

**skill-uptake-survey — pass.** The report invokes `tools/citecheck/citecheck.py --anchor` for L0 verification (Discipline note + Supporting evidence) and references the cycle-021 fence-parity / cycle-012 lowering-directory conventions. The shape (demotion + fence-bearing proposed-changes) implies the `proposed-changes-fence-encloses-full-body-guard` discipline, which the report respects in practice. Telemetry only; non-blocking.

### Issues found

1. **[warning — cross-reference-integrity, cross-dispatch coordination] Edit #6b targets a file the sibling D6 dispatch deletes this same cycle.** Proposed-changes §6 (CYCLE.md:266-275) edits `book/src/L2-L1/normalize-leaf-identity.md:47` (re-anchoring its cohort enumeration off the `assemble-diagonal-leaf-identity` slug). But the sibling normalize demotion `reports/2026-06-01T195100Z-lifter-demote-normalize/CYCLE.md` (frontmatter line 8, proposed-change line 48) DELETES `book/src/L2-L1/normalize-leaf-identity.md` outright. The two dispatches collide on one file. Consequence is benign for the build (the file is removed entirely, so no dangling reference remains regardless of ordering) but D3's edit #6b is either a wasted edit (D3 applies first, then D6 deletes) or an unresolvable anchor (D6 applies first, file gone). D3's own §Discipline notes (CYCLE.md:313-319) and §Open-questions treat `normalize-leaf-identity.md` as a surviving live file and do NOT acknowledge that D6 deletes it — D3 only flagged the slug as a re-anchor target, missing that the *whole file* is going away. Surface for integrator sequencing: edit #6b is droppable. Severity: low (no build hazard; pure redundant/conflicting work). The other re-anchor (#6a, `L3/reciprocal.md:150`) targets a surviving file and is correct.

2. **[informational — no severity, scope-correct] §1d-smell judgment independently confirmed; load-bearing non-law preserved.** Not a defect — recorded for the repairer/integrator. The matrix-free high-order-Nedelec approximate-diagonal non-law is reproduced verbatim in BOTH in-line notes (L3 note CYCLE.md:99-111; L2 note CYCLE.md:202-214) with its full citation set (`rap.cpp:163-164` + `operator.cpp:139` + `hypre.cpp:88` + `test-libceed.cpp:367-376`, plus the L2 note adds `jacobi.hpp:15-16`). All anchors verified on-disk in-range. The deleted themes carried exactly this non-law (`assemble-diagonal-body-identity.md:114-127`, `assemble-diagonal-leaf-identity.md:125-139`); nothing load-bearing was lost in the demotion. The "preserved by reference, NOT erased" framing is faithful to the source.

3. **[informational — no severity] Minor heading-level inconsistency between the two in-line notes.** The L3 note is authored as `### Downward to L2 (in-line note)` (h3, CYCLE.md:82) while the L2 note is `## Downward to L1 (in-line note)` (h2, CYCLE.md:176). Cross-references between them and from re-anchored prose use the bare §"Downward to L2" / §"Downward to L1" form, so resolution is unaffected. Cosmetic; not a build or fidelity issue. Noted only for completeness.

4. **[informational — no severity, scan artifact] Two `citecheck --scan` flags are bare-basename prose mentions, not citation defects.** `operator.cpp:139` (`[AMBIG]`) and `reciprocal.md:25` (`[AMBIG]`) trip the scanner because they appear once each as un-pathed basenames in prose (Discipline notes), while their load-bearing citation occurrences are correctly full-pathed. No correction needed; flagged so the repairer does not chase a false off-by-one.

## Repair

### Fixes attempted

- **Finding**: [warning — cross-reference-integrity] Edit #6b re-anchors `book/src/L2-L1/normalize-leaf-identity.md:47`, but the sibling D6 dispatch (`reports/2026-06-01T195100Z-lifter-demote-normalize/`) DELETES that whole file this same cycle — making #6b a wasted edit (if D3 applies first) or an unresolvable anchor (if D6 applies first).
  - **Decision**: repaired
  - **Action**: Dropped edit #6b from CYCLE.md §6 proposed-changes (`reports/.../CYCLE.md` §"6. Re-anchor the two plain-text inbound slug mentions"). Removed the `edit:book/src/L2-L1/normalize-leaf-identity.md` block and its lead-in; replaced with a "(Dropped — was edit #6b)" note explaining the inbound mention is moot because D6 deletes the file. Also propagated the change to: the frontmatter `inputs:` list (the `normalize-leaf-identity.md` re-anchor line → repairer NOTE), the §Summary clause (e) ("two plain-text inbound slug mentions" → "the surviving plain-text inbound slug mention (`L3/reciprocal.md:150`)" + dropped-#6b note), and the §Discipline-notes scope-fence bullet (clarified the `:47` re-anchor is dropped). Edit #6a (`L3/reciprocal.md:150`, a surviving file) is KEPT — correct and unchanged.
  - Verified independently that D6 deletes the file (D6 CYCLE.md frontmatter line 8 `(DELETE)` + delete-block line 48 `delete:book/src/L2-L1/normalize-leaf-identity.md`).
  - Verified dropping #6b leaves no dangling reference to the deleted assemble-diagonal slugs: `grep -rln` of both deleted slugs across `book/src/` resolves to (a) `SUMMARY.md` (handled by edit #4), (b) `L3/assemble-diagonal.md` (edit #2), (c) `L3/reciprocal.md` (edit #6a), (d) the two self-files (deleted by edit #1), (e) the two index live-link rows at `L3-L2/index.md:21` / `L2-L1/index.md:22` (removed by edit #5), (f) the index prose-bullet/cohort-log mentions (`:49`/`:64`/`:78` — build-safe plain text, explicitly DEFERRED to D7 per D3's Discipline notes, out of D3 scope), and (g) `normalize-leaf-identity.md:47` (moot — D6 deletes the whole file). No build-breaking or dangling live-link reference remains.
  - Fence parity re-verified post-edit: 14 openers (2 `delete:` + 12 `edit:`) / 14 bare closers / 28 markers, all balanced (the critic's prose "12 edit" was an off-by-one in the critique narration; the pre-repair report had 13 edit blocks, dropping #6b yields 12 — balance is clean either way).

The other three issues the critic raised are informational (no severity): issue #2 (load-bearing non-law preserved — confirmation, not a defect), issue #3 (cosmetic h2/h3 heading-level inconsistency between the two in-line notes — resolution unaffected since references use the bare §-title form; not repaired, below repair bar and explicitly cosmetic), issue #4 (citecheck scan bare-basename artifacts — explicitly no correction needed). None require a fix.

### Unrepairable findings

None. The single warning was mechanically droppable (delete a dead proposed-changes block + propagate the count/scope prose), entirely within repair authority.

## Suggested resolution

`ready`. Notes for the integrator:

- D3 (this report) and D6 (`demote-normalize`) both touch `book/src/L2-L1/normalize-leaf-identity.md` this cycle; with edit #6b dropped, D3 no longer touches that file at all — D6 is now its sole writer (D6 deletes it). No cross-dispatch sequencing constraint remains between D3 and D6 on that file.
- D3's index-file count/cohort-prose reconciliation (`L3-L2/index.md` firm 17→16, `L2-L1/index.md` "five"→"four" standalone-floor cohort framing, etc.) is correctly DEFERRED to the wave-2 count-owner D7 — see D3 §Discipline notes + §Open-questions. D3 removed only the two build-breaking live-link rows; D7 owns the tallies. The integrator should ensure D7's worklist enumerates the assemble-diagonal demotion's count impact (D3's §Open-questions flags this explicitly).
- SUMMARY.md edits #4 leave a blank line in place of each removed theme row; mdBook tolerates this (integrator may collapse at apply time per D3's note).
