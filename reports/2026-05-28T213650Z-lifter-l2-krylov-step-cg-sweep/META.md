---
verifies: ../REPORT.md
critiqued_at: 2026-05-28T223500Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-28T230000Z
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

# META: verification of "Re-anchor book/src/L2/krylov-step.md cg.md dangling-pointer sweep"

## Critique

### Checks run

**citation-validity — warning.** Every re-anchor target the 12 edits emit was verified against source this critique. The central prose-correction is L0-confirmed: `reference/palace/palace/linalg/iterative.cpp:21-32` is the two `CheckDot` overloads (real at :22, complex at :28, the `isfinite && >= 0.0` guard), called for CG at :396/:410/:445/:461 — confirmed via codemap `read_range` + `search_text`. `iterative.cpp:243-250` is the `ApplyB` preconditioner helper (`BlockTimer ...; B->Mult(x, y);`), NOT CheckDot — so the file's pre-edit `iterative.cpp:244-250` CheckDot citation is genuinely a drifted mislabel, and the `:21-32` correction is sound. The CG inner-loop ranges are exact: `A->Mult(p, z)` at :443, `denom = Dot(comm, z, p)` at :444, `CheckDot(denom)` at :445, `x.Add`/`r.Add` axpy at :448-449 (all four line numbers in edit line 77 match source verbatim), preconditioner branch + second `Dot`/`CheckDot` at :460-461, first-iteration branch `if (!it) { p = z; } else { AXPBY(...beta/beta_prev...); }` at :434-441, initial-guess threading at :377-386. Live retained slice ranges all confirmed against the 165-line stub: `cg.md:27-141` (v0.5 section), `:86-106` (`cg_solve` def), `:120-133` (§Equivalence-to-v0.4 → `forget_beta_prev` at :129 → §Variant pcg), `:39-106` (v0.5 typescript + driver). The warning is for one **incomplete-sweep** defect (see Issues #1): the same drifted `iterative.cpp:244-250` CheckDot mislabel survives uncorrected at L2 line 171, even though the report establishes and L0-verifies that `:244-250` is ApplyB.

**surface-or-evidence — pass.** This is a pure citation-refinement sweep (corpus-reduction re-anchoring), not a refinement-shaped surface change. The report is explicit (Discipline notes line 107): no structural / decomposition / signature / status edits — the five-primitive-group decomposition, six variant axes, three algebraic laws, and `firm` status are unchanged. The one prose-correction is a bounded drifted-citation fix, not a rotation claim. The framing is retroactive-evidence / citation-backfill, which is allowed. No rotation_claim is asserted, so the no-surface-without-claim gate does not apply.

**rotation-quality — pass (not applicable to a citation-sweep).** No algebraic / structural / reduction rotation is asserted in this dispatch. The L2 entry's existing rotation content (the demand-pruning law, state-stratum independence) is untouched. The retained references to the v0.4↔v0.5 self-rotation (`forget_beta_prev`) are pointers to existing established rotations in the slice, not new claims. Nothing to score.

**variant-axis-coverage — pass.** The six variant axes are not modified — the edits re-anchor the citations that witness axes 1 (preconditioner present/absent, line 116) and 4 (first-iteration-unrolled vs branch-in-body, line 119) without changing the axis enumeration or collapsing any combination. The preconditioner branch re-anchor correctly points at the L0 `if (B) { ApplyB(...) } else { z = r; }` site inside `:427-464` plus the variant-collapse home `L1/ksp_solve.md` Variant axes (confirmed at L1/ksp_solve.md:85) and the L1>L0 reintroduction in Sub-pattern B. No hidden branch introduced.

**cross-reference-integrity — pass.** This was the CRITICAL-focus check. Every re-anchor destination is a verified TERMINAL firm home, not a relocated dangle (the cycle-015 L3-sweep failure mode is avoided). Confirmed real and content-bearing: `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern B (lines 159-295; CG inner body `iterative.cpp:360-486`, per-step loop `:427-464`, initial-guess `:377-386`, CheckDot recognition note at :251-265 citing `iterative.cpp:21-32`); `concepts/sequential-obstruction.md`, `concepts/derived-view-hoisting.md` (§"Worked example: CG residual norm" at line 14), `concepts/first-iteration-unrolling.md` — all exist; `L1/ksp_solve.md` Variant axes (line 85); `L1/chebyshev-smoother.md:260` (multigrid-integration coverage note confirmed); `arnoldi_step.md:194-213` (in 302-line file); `chebyshev.md` §"Initial-guess shape: branch vs derived view" (line 274) and §Semantics `innerStep`. The terminal-home convention is independently corroborated by `book/src/L3/krylov-step.md` §Evidence lines 196/204, which terminate the SAME CG dangling cohort at `L2/krylov-step.md:138`/`:146` (i.e., L2 is the terminus from L3's perspective) — so L2's own outbound pointers correctly resolve one layer further down to L0 + concept pages + live retained-slice material. No re-anchor points at another dangling pointer. All `[link]` markdown references in the new prose resolve.

**edge-label-fidelity — pass.** The dispatch carries an L2>L1 / corpus-reduction-sweep label (frontmatter line 4); the edits operate on the L2 `krylov-step` entry and re-anchor its outbound evidence downward to L0/L1/concept homes. The narrative direction stays high→low (LHS = L2 `krylov-step`; cited evidence is the L0/firm-layered substrate it composes from), consistent with the report's Discipline note (line 107). No edge-label/prose mismatch.

**plan-kind-consistency — pass.** Declared shape is a citation-refinement sweep (status `pending`, scope "citation sweep"). Content matches: 12 mechanical re-anchors + 1 recorded bounded prose-correction, no structural authoring. The retained-`firm`-status claim is consistent — the entry was firm before and stays firm; this is not a rough-in or firm-up. The two flagged-for-future live citations (`cg.md:27-141` / `:86-106`) are correctly framed as live-retained-not-dangling (Open questions caveat line 135), matching the sweep kind.

**skill-uptake-survey — pass.** The report references `verify-citation-range` "Producer self-verification before emitting citations" (skill section confirmed at SKILL.md:36) and records the bounded prose-correction per friction-ledger `lifter-scope-content-correction-boundary` (entry confirmed at friction-ledger.md:1006) and `producer-citation-drift-verify-not-self-invoked` (line 1134). The self-verification block (report lines 111-119) is substantive and accurate — each terminal target was independently re-derived this critique and matched. Skill-uptake is well-surfaced.

### Issues found

**Issue #1 — incomplete sweep: drifted `iterative.cpp:244-250` CheckDot mislabel survives at L2 line 171 (citation-validity, severity: moderate).** `book/src/L2/krylov-step.md` line 171 (§Evidence "L0 / source-side tests") reads:
> `- reference/palace/palace/linalg/iterative.cpp:244-250` — `CheckDot` partial-function guard.

This is the SAME drifted citation the report corrects at line 67 (`CheckDot` cited as `:244-250`) — the report itself L0-verifies (Discipline notes line 109) that `:244-250` is the `ApplyB` helper, not `CheckDot`, and re-anchors every other CheckDot occurrence to `:21-32`. But the standalone line-171 instance is not in the report's 12 edits. The report's site table (CYCLE.md line 41) and its line-172 edit handle the adjacent `cg.md:288`→`:21-32` test-coverage row, yet leave line 171's `iterative.cpp:244-250` CheckDot mislabel uncorrected. After this dispatch applies, the L2 file would still carry one self-inconsistent citation: line 67 says CheckDot is at `:21-32`, line 171 says CheckDot is at `:244-250`. Candidate fix: add a 13th edit re-anchoring line 171's `iterative.cpp:244-250` → `iterative.cpp:21-32` (consistent with the report's own established correction and the firm L1>L0 / L3 anchors).

**Issue #2 — line 171/172 are adjacent; the report's line-172 edit narrowly misses the line-171 sibling (citation-validity, severity: minor, sub-issue of #1).** The report's §Evidence line-172 edit rewrites the test-coverage prose and folds in the `cg.md:288`→`:21-32` re-anchor, but the immediately-preceding bullet (line 171) carrying the standalone drifted CheckDot citation was apparently not enumerated in the dangling-pointer scan (it cites `iterative.cpp:244-250`, not a `cg.md:NNN` range, so it would not have matched a `cg.md:`-pattern sweep — but it IS the exact drift the report's prose-correction targets elsewhere). Recording as a sibling of #1 so the repairer treats the §Evidence "L0 / source-side tests" block (lines 168-172) as a unit when closing the CheckDot-drift consistency gap.

**Note (not an issue) — scope-statement self-correction is sound.** The report's Open-questions caveat (line 134) correctly notes the dispatch framing said the `cg.md` slice "was removed" when it was reduced-to-stub (the `chebyshev.md` slice was the removed one). The dangling-pointer symptom and re-anchor targets are identical either way; the correction is for-the-record and needs no action. No issue.

**Note (not an issue) — bounded prose-correction is in-bounds.** The CheckDot `:244-250`→`:21-32` correction satisfies all three `lifter-scope-content-correction-boundary` gates: (i) directly L0-supported (independently re-confirmed this critique), (ii) bounded (fixes a drifted citation pointing at the wrong helper; does not touch decomposition / signature / laws / status), (iii) recorded explicitly (Discipline notes line 109). Not over-reach into abstractor authoring authority.

## Repair

### Fixes attempted

- **Finding (Issue #1, citation-validity, moderate)**: the same drifted `iterative.cpp:244-250` `CheckDot` mislabel survives uncorrected at `book/src/L2/krylov-step.md` line 171 (§Evidence "L0 / source-side tests"), even though the report corrects this exact drift at line 67 and re-anchors the adjacent `cg.md:288` test-coverage row at line 172. Post-apply the file would self-contradict: line 67 says CheckDot is `:21-32`, line 171 says `:244-250`. The line-171 instance was missed because it cites `iterative.cpp:`, not a `cg.md:NNN` range, so a `cg.md:`-pattern dangling-pointer scan would skip it.
  - **Decision**: repaired.
  - **Action**: Added a 13th proposed-changes edit block to `reports/2026-05-28T213650Z-lifter-l2-krylov-step-cg-sweep/CYCLE.md` (§Proposed changes, immediately after the prior §Evidence "L0/source-side tests" edit). The edit re-anchors line 171's `reference/palace/palace/linalg/iterative.cpp:244-250` → `iterative.cpp:21-32` and folds in the same ApplyB-drift note the report applies at line 67. The new edit's `[old]` block matches the on-disk line-171 text verbatim (`- reference/palace/palace/linalg/iterative.cpp:244-250` — `CheckDot` partial-function guard.). Also updated the CYCLE.md Summary ("12 sites" → "13 sites", repair-added) and appended a 13th site-table row for internal consistency.
  - **L0 re-verification (codemap `read_range` on `reference/palace/linalg/iterative.cpp`)**: `:21-32` IS the two `CheckDot` overloads (`inline void CheckDot(T dot, ...)` at :22, the `std::complex` overload at :28, the `MFEM_ASSERT(std::isfinite(dot) && dot >= 0.0, ...)` guard). `:243-250` (containing `:244-250`) IS the `ApplyB` preconditioner helper (`BlockTimer bt(Timer::KSP_PRECONDITIONER, ...); B->Mult(x, y);`), NOT `CheckDot`. The critic's confirmation holds; the re-anchor is sound and consistent with the report's own established correction + the firm L1>L0 / L3 anchors.

- **Finding (Issue #2, citation-validity, minor; sub-issue of #1)**: line 171/172 are adjacent; the report's line-172 edit narrowly missed the line-171 sibling carrying the standalone drifted citation.
  - **Decision**: repaired (closed by the same 13th edit as Issue #1 — the §Evidence "L0 / source-side tests" block, lines 168-172, is now treated as a unit; both line-171 and line-172 CheckDot citations resolve to `iterative.cpp:21-32`).

### Unrepairable findings

None. The two retained live `cg.md:27-141` / `:86-106` citations the critic flagged are correctly framed by the report as live-retained-not-dangling (Open questions caveat, CYCLE.md line 135) with an explicit future re-point flagged for the eventual slice-removal audit — these are left as-is per the dispatch instruction (the slice is still live; not actionable now).

## Suggested resolution

`ready`. The single warning (citation-validity, moderate Issue #1 + its minor sibling #2) was a mechanical incomplete-sweep defect — a surviving copy of the exact CheckDot drift the report already corrects elsewhere — and is closed by the repair-added 13th edit, which is surgical (re-anchor one citation to a target the report itself L0-established this dispatch) and introduces no new content decision. The post-apply L2 file is now self-consistent: every `CheckDot` citation resolves to `iterative.cpp:21-32`. Integrator note: apply all 13 proposed-changes edits; the 13th targets line 171's standalone `iterative.cpp:244-250` bullet.
