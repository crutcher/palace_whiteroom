---
verifies: ../REPORT.md
critiqued_at: 2026-06-01T141500Z
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
repaired_at: 2026-06-01T142000Z
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
follow_up_agent: null
---

# META: verification of L3>L2 theme `eigsolve-opaque-eigen-iteration`

## Critique

### Checks run

**citation-validity — pass.** `citecheck --scan` on the CYCLE.md reported 22 ok / 0 failing (all bounds + path-hygiene clean). I anchor-verified every load-bearing pinpoint via `citecheck --anchor` and confirmed the meaning-read with `read_range`: `slepc.cpp:694` (`EPSSolve`, anchor at 694), `arpack.cpp:318` (`naupd`, anchor at 318), `arpack.cpp:315` (`while`, anchor at 315), `arpack.cpp:323-326` (`ido`), `arpack.cpp:586` (`opProj`), `arpack.cpp:579-581` (`opInv`), `slepc.cpp:1847-1876` (`opInv` at 1858), `slepc.cpp:707` (`RescaleEigenvectors`), `slepc.cpp:711-716` (`gamma` at 715), `slepc.cpp:379-394` (`STPRECOND` at 384, `STSINVERT` at 388) — all `[ok]`. The `:313`→`:315` drift the abstractor caught is confirmed real and correctly handled: `citecheck 'arpack.cpp:313' --anchor 'while'` reports `[DRIFT +2]` with `suggested: arpack.cpp:315`; the report cites `:315-339` (loop) and `:318` (`naupd`) throughout, matching the firm L3 entry's own citations, and the §Open-questions process note (CYCLE.md #4) documents the catch (the `+2` matches the cycle-027 codemap brace-boundary drift pattern). I read the ARPACK RCI loop (`:313-335`) and the SLEPc `Solve` (`:687-709`) directly: the source confirms the callback-dispatcher claim verbatim — `while(true)`@315, `naupd`@318, `ApplyOp` dispatched only on `ido==1||ido==-1`@323-326, `break` on `ido==99`@331; and `EPSSolve(eps)`@694 is a single opaque library call. No `verified_against:` YAML block is emitted (the §Verified-against is plain prose, not a fenced YAML payload), so the round-trip sub-check no-ops.

**surface-or-evidence — pass.** The report both modifies surface (a `new:` theme file + 6 `edit:` blocks to existing artifacts) and carries rotation_claim evidence (the rewrite-shape table + L0 negative/positive anchors). It is not a pure rotation_claim with no surface, and not a pure retroactive backfill — it is a substantive new-theme + re-anchor proposal. Passes.

**rotation-quality — pass (substantive, not identity).** The asserted rotation is genuinely substantive on the loop: the L3 first-class opaque-library `sequential-obstruction` **marker** attached to the `eigen_iterate` role reference is **erased** at L2 to a plain role reference, shadowing to the two L2 non-laws ("Opening of the eigen-iteration fold at L2" + "Fold-merge / restart associativity"). This is state-hiding / coarser-substitution, not a rename or 1:1 mapping — it passes the rotation bar. The distinguishing fact vs the two sibling substantive themes is clearly narrated and source-grounded: for `ksp-solve-outer-driver` / `orthogonalize-variant-split` Palace **authors** the loop and L3 *renders* it as an explicit tail recursion (which L2 then erases), whereas for `eigsolve` Palace authors **no** recurrence — the ARPACK loop is an RCI callback dispatcher around the opaque `naupd` driver (`:315-339`) and SLEPc is a single opaque `EPSSolve` call (`:694`) — so L3 can only *mark* a library boundary and L2 erases the mark. The per-step body (`apply_linop ▷ ksp_solve ▷ scale_untransform [▷ project]`) is correctly held identity-in-form (witnessed at both ARPACK `ApplyOp` `:562-590` and SLEPc `__pc_apply_EPS` `:1847-1876` assembly sites), and explicitly scoped out as NOT the substantive content of this hop (it belongs to the L2>L1 body edge). The rewrite-shape table delimits the single non-identity line (the fold) from the identity lines (setup/body/extract modulo the `st0`→`st` rename) cleanly.

**variant-axis-coverage — pass.** The report addresses the variant axes explicitly (Applicability condition #4): the five-axis profile (three opened — spectral-transformation, problem-type, scaling; two collapsed — backend-orchestration, element-type). The load-bearing axis for this theme — **backend-orchestration** (`arpack-rci | slepc-st-shell`) — is handled correctly: both backend loops are opaque-library-owned, so the axis collapse at L2 is consistent with the obstruction-marker erasure on both arms (neither backend exposes a Palace-authored loop). No hidden branch. The non-interacting axes (spectral-transform / problem-type / scaling shape the body, not the loop) are scoped out with reasoning.

**cross-reference-integrity — pass.** All `[link]` targets resolve on disk: `L3/eigsolve.md`, `L2/eigsolve.md`, `L3-L2/ksp-solve-outer-driver.md`, `L3-L2/orthogonalize-variant-split.md`, `L2-L1/eigsolve-spectral-transform-composition.md`, `L3/apply_linop.md`, `L3/ksp_solve.md`, `L2/index.md`, and the four concept pages (`sequential-obstruction`, `solve-monad`, `solver-as-operator`, `constructed-operators`, `variant-absorption`) all exist. The `new:` target `L3-L2/eigsolve-opaque-eigen-iteration.md` is correctly absent (created by this report). The two `edit:L3-L2/index.md` blocks anchor onto the existing `orthogonalize-variant-split` row/bullet (present), and the `edit:SUMMARY.md` block anchors after the existing `orthogonalize-variant-split` SUMMARY line (line 56); the new slug pre-exists in neither index nor SUMMARY (no duplicate registration). Dual-registration is correct: own table row + §Vocabulary-cohort bullet in `L3-L2/index.md` + SUMMARY entry. The four `edit:L3/eigsolve.md` re-anchors target the four stale assertions accurately: frontmatter line 8, §Downward line 35, §Lowers-to line 199, §L3-vs-L2 line 210 — each currently asserts "no L3-L2 theme file / in-line annotation per cycle-012" and the new text flips it to cite the theme while keeping the body-identity in-line note accurate. The unedited line 37 ("Non-adjacent identity (in-line, no directory)") is NOT a stale contradiction: it concerns the transitive L3↔L1 (non-adjacent) identity and the `L3-L1/` directory question, concluding correctly that the L2↔L1 edge breaks transitivity — it is out of scope for this adjacent-edge flip and correctly left untouched. Build-readiness/firm-body-inside-fence: the `firm` theme body is fully enclosed in the `new:` fence (lines 48-501); the body uses 4-space indented code (not nested fences) for the L3/L2 pseudo-forms, so no nested-fence truncation hazard.

**edge-label-fidelity — pass.** Edge labels are uniformly forward high→low: 37× `L3>L2`, plus `L3→L2`/`L3 → L2` directional phrasing; LHS=L3, RHS=L2 consistently (§"L3 form (LHS)", §"L2 form (RHS)", §Verified-against "L3 evidence (the LHS)" / "L2 evidence (the RHS)"). The `L3↔L2` instances are legitimate bidirectional references in the body/loop-division discussion. No inverted-edge prose (no claim labeled L3>L2 that actually discusses L2>L1 — the L2>L1 body-edge content is explicitly partitioned into the §"L3>L2 vs L2>L1 distinction" section and attributed to the sibling theme).

**plan-kind-consistency — pass.** Declared kind is a `firm` L3>L2 theme. Content shape matches: both endpoints firm (L3/eigsolve cycle-024 partial-obstruction; L2/eigsolve cycle-023), substantive content structurally grounded and citation-backed at both layers + L0, no rough-in placeholders, no speculative L3 vocabulary introduced (§Speculative operators correctly "None"). The justification kind (`structural` dominant + secondary `obstruction` sub-kind `opaque-library-ownership`) matches the content and the CLAUDE.md obstruction sub-kind taxonomy.

**skill-uptake-survey — pass.** The citation-drift handling shape implies `verify-citation-range` / `citecheck`; the report references `citecheck --anchor` + on-disk `read_range` invocation in §Verified-against and the §Open-questions process note (#4) documenting the `[DRIFT +2]` catch. Telemetry present.

### Issues found

No blocking or warning issues found. The report is clean across all 8 checks. Minor observations (non-blocking, NOT repair candidates — surfaced for integrator/D3 awareness, all already self-flagged by the abstractor):

1. **Count deferred to D3 (correct, not a defect).** The report explicitly did NOT touch the consolidated §Working-Notes tally or the firm-15→16 / coverage-gap line (CYCLE.md §Open-questions #3), per the count-ownership partition — D3/layer-intro-author owns the tally this cycle. This is the correct partition behavior, noted here only so the integrator does not expect the count update in this report's proposed-changes.

2. **Concept-page distinction flagged out-of-scope (correct).** CYCLE.md §Open-questions #2 proposes that `concepts/sequential-obstruction.md` may want to note the opaque-library-rooted-marker vs Palace-authored-recurrence distinction, correctly deferred to a future layer-intro-author/cross-cutter pass (concept pages are out of abstractor write-scope). Not a defect in this report.

3. **OQ slug `l3-l2-substantive-erasure-scope-taxonomy`** is recommended for the meta-phase to name the now-complete three-corner taxonomy (CYCLE.md §Open-questions #1). Informational; the integrator-per-report promotes OQs.

## Repair

### Fixes attempted

No findings to repair. The critic returned all 8 checks `pass` with no warning/fail/unclear findings. There were no repair candidates.

Informational-no-defect (the critic's three "Issues found" entries are explicitly non-blocking, NOT repair candidates, and all already self-flagged by the abstractor — recorded here for accountability, no action taken):

- **Finding**: Count deferred to D3 — the report did not touch the §Working-Notes tally / firm-15→16 / coverage-gap line.
  - **Decision**: not-needed. Correct count-ownership partition behavior (D3/layer-intro-author owns the tally this cycle); not a defect. Touching the count here would be both out of partition and substantive authoring. No edit.

- **Finding**: Concept-page distinction (opaque-library-rooted-marker vs Palace-authored-recurrence) flagged out-of-scope for `concepts/sequential-obstruction.md`.
  - **Decision**: not-needed. Concept pages are out of abstractor write-scope AND out of repairer scope (the artifact is not a repairer target); correctly deferred to a future layer-intro-author/cross-cutter pass. No edit.

- **Finding**: OQ slug `l3-l2-substantive-erasure-scope-taxonomy` recommended for the meta-phase to name the three-corner taxonomy.
  - **Decision**: not-needed. Informational; the integrator-per-report promotes the report's Open questions. Not a repair candidate.

The `:313`→`:315` citation drift was already caught and corrected by the abstractor in-report (the report cites `arpack.cpp:315-339` / `:318` throughout, matching the firm L3 entry); the critic confirmed the `[DRIFT +2]` was real and correctly handled. No residual citation repair needed.

### Unrepairable findings

None.

## Suggested resolution

`ready`. Clean report, all 8 checks pass, zero repair candidates. Notes for the integrator:
- This report's proposed-changes deliberately omit the §Working-Notes count update — the firm-15→16 tally + coverage-gap line is D3/layer-intro-author's this cycle (count-ownership partition). Do not expect a count touch in this report.
- Promote the report's Open questions, including the recommended OQ slug `l3-l2-substantive-erasure-scope-taxonomy` (three-corner L3>L2 substantive-erasure taxonomy, for meta-phase naming) and the deferred `concepts/sequential-obstruction.md` opaque-marker-vs-authored-recurrence distinction note.
- The 6 `edit:` re-anchors on `L3/eigsolve.md` (frontmatter line 8, §Downward line 35, §Lowers-to line 199, §L3-vs-L2 line 210) + `L3-L2/index.md` (row + cohort bullet) + `SUMMARY.md` flip the prior "no L3-L2 theme file" assertions to cite the new `eigsolve-opaque-eigen-iteration.md`; line 37 (non-adjacent L3↔L1 identity) is correctly left untouched.
