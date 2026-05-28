---
verifies: ../CYCLE.md
critiqued_at: 2026-05-28T20:05:00Z
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
repaired_at: 2026-05-28T20:30:00Z
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

# META: verification of "Audit chebyshev-lowering-themes (L1>L0 + L2>L1)"

## Critique

### Checks run

**citation-validity — warning.** I independently re-read the cited Palace ranges via `palace-codemap read_range` (no transcription from the report). Most anchors land as claimed and the report's core drift diagnoses are correct in direction: line 188 IS the closing `}` of 4th-kind `SetOperator` (so `:188-220` for `Mult2` does pull in a foreign brace); 4th-kind `SetOperator` close IS at line 188 (so `:169-186` undershoots, missing `this->width`@187 + close@188); 1st-kind `SetOperator` close IS at line 258 (so `:232-259` overshoots by one). The element kernels `:68-78` (ApplyOrder0) and `:112-123` (ApplyOrderK) land exact. BUT two of the report's own boundary claims are factually wrong (see Issues 1 and 2) — the proposed canonical `Mult2` start `:191` is the opening brace, not the signature (signature is line 190), and `chebyshev.hpp:43` is a comment line, not `mutable VecType d, r;` (that is line 44). The report asserts both as "exact."

**surface-or-evidence — pass.** Pure audit report. No surface (operator/theme text) mutation; the report routes citation-range refinements to a follow-up abstractor/lifter and explicitly leaves both `## Status` lines `firm`. This is retroactive evidence backfill (`verified_against` blocks) — allowed. Not refinement-shaped in the proposal sense.

**rotation-quality — pass.** The L2>L1 fusion-soundness verdict is justified, not hand-waved. The report grounds the per-degree three-term recurrence → closed-form polynomial-token collapse in the L2 entry's already-firm law 1, and I confirmed the load-bearing element kernels at source: `ApplyOrder0` is `D[i] = sr*DI[i]*R[i]`@77 and `ApplyOrderK` is `D[i] = sd*D[i] + sr*DI[i]*R[i]`@122 — exactly the FMA-shaped recurrence the L2 form makes explicit and L1 names as one polynomial step. The sequential-obstruction framing (forbidding monomial re-expansion / reorder) is correct. This is a genuine state-hiding / recurrence-compression rotation, not a 1:1 rename.

**variant-axis-coverage — pass.** The two orthogonal axes — polynomial kind (4th vs 1st) and element type (real vs complex `Operator`/`ComplexOperator`) — are both covered. The report verifies both `Mult2` bodies (4th `:191-220`, 1st `:261-293`), both `SetOperator` bodies, the `<Operator>`/`<ComplexOperator>` instantiations @295-299, and explicitly treats the complex transpose kernels (`:101-110`, `:150-159`) as dead-but-defined recognition rules. No hidden branch.

**cross-reference-integrity — warning.** The inherited-anchor carry-forward the report flags is real and correctly characterized: I confirmed `book/src/L1/chebyshev-smoother.md:245,247` and `book/src/L2/chebyshev-iteration.md:35,143,245,247` cite the element kernels as `:69-78`/`:114-123`, whose starts (`:69`/`:114`) are one line inside the signatures (`:68`/`:112`). Flagging that against the anchor entries (not these themes) is the right routing. However the report introduces a NEW cross-reference defect of its own at `chebyshev.hpp:43` (Issue 2). All named slugs and file paths resolve.

**edge-label-fidelity — pass.** Theme 1 carries L1>L0 and the prose narrates the L1-pure-action → L0-output-arg-mutation rewrite; Theme 2 carries L2>L1 and narrates the L2-explicit-recurrence → L1-fused-polynomial-token collapse. Both edge labels match their prose direction. The report's explicit "directionality (high→low) check: PASS" with quarantined reverse-direction lifting notes is corroborated.

**plan-kind-consistency — pass.** Declared shape is a lowering-verifier audit producing CONFIRMS / CONFIRMS-WITH-REFINEMENT verdicts with per-citation evidence, applicability conditions, and routed follow-up edits. Content matches: no new operator/theme authored, no status promotion, refinements routed out (lowering-verifier does not mutate `book/`). The `firm`-stays-`firm` decision and the "no partly-constructive caveat warranted" reasoning (syntactic identity on fully-specified source vs eigsolve negative-anchor reconstruction) are consistent with the audit kind.

**skill-uptake-survey — pass.** The report cites the relevant skill precedent (`audit-report-inherited-miscitation-lint` skill-candidate; `lifter-scope-content-correction-boundary`; `verify-citation-range`'s inherited-citation sub-case is the implicit procedure being run). Telemetry present; no blocking concern.

### Issues found

1. **`Mult2` canonical range `:191-220` starts at the opening brace, not the signature — report rationale misstates which line is the signature.** Location: CYCLE.md §Per-citation audit (Theme 1 first bullet, line ~51) and §Proposed changes R1/R4 (lines 167–168, 225). I read 186–192: line 189 = `template <typename OperType>`, line **190** = `void ChebyshevSmoother<OperType>::Mult2(...) const`, line **191** = `{`. The report repeatedly says "sig@191" / "signature@191" / "sig-to-close, matching the L1 anchor's `:191-220`." That is wrong: 191 is the brace; the signature is 190; a true signature-to-close range is `:190-220`, and template-to-close is `:189-220`. The proposed `:191-220` excludes the signature line entirely. The drift diagnosis (that `:188` is wrong because it grabs the prior function's close) is still correct; only the *replacement* range and its justification are off. Severity: medium — the correction lands a range that still omits the signature, and the stated rationale would mislead the repairer/integrator into believing 191 is the signature. (Note: the L1 anchor and dispatch prompt also use `:191`, so this may be an inherited convention; if `:191-220` is intentionally brace-to-close for consistency, the report should say so rather than mislabel 191 as the signature.)

2. **`chebyshev.hpp:43` is a comment, not `mutable VecType d, r;` — report confirms a stale citation as "exact."** Location: CYCLE.md §Per-citation audit (Theme 1, line 59–62) and §Supporting evidence (line 260), §Proposed-changes audit block (line 199–202). I read hpp 36–58: line **43** = `// Temporary vector for smoother application.`; line **44** = `mutable VecType d, r;`. The theme under audit (`chebyshev-smoother-mutation-rotation.md:75-76,103`) cites `hpp:43` for `mutable VecType d, r;` — that is an off-by-one miscitation, and the report verdicts it "supports / Exact" and copies `hpp:43` into the proposed `verified_against` block. Severity: medium — an actual citation defect in the audited theme was missed and then re-asserted as verified evidence; should be `:44` (or `:43-44` to include the explanatory comment). The same class as the inherited-anchor drift the report DID catch.

3. **Inherited-anchor element-kernel drift (correctly flagged) — confirm routing covers all instances.** Location: CYCLE.md §Open questions (line 267). The carry-forward against `book/src/L1/chebyshev-smoother.md` and `book/src/L2/chebyshev-iteration.md` (`:69-78`→`:68-78`, `:114-123`→`:112-123`) is real and verified. I found the L2 anchor carries the drifting ranges at FOUR sites (lines 35, 143, 245, 247), not the two §Evidence sites implied; a follow-up correction must sweep all occurrences, not just the Evidence block. Severity: low — the report's flag is directionally correct; this is a completeness note for whoever enacts the carry-forward.

4. **`hpp:50-76` collapse in the proposed audit block merges three distinct constructs into one range.** Location: CYCLE.md §Proposed-changes (lines 203–206). The per-citation audit verified `:50-58` (Mult), `:60-68` (MultTranspose), `:71` (Mult2 decl), `:73-76` (MultTranspose2 alias) separately and exactly, but the appended `verified_against` block compresses them to a single `chebyshev.hpp:50-76`. That envelope spans the gap and is coarser than what was verified; `:71` (the pure-virtual `Mult2` decl) is the load-bearing forwarding-target. Severity: low — cosmetic/over-coarsening, not a falsified claim, but reduces the precision the audit otherwise demonstrates.

## Repair

### Fixes attempted

- **Finding (Issue 1)**: `Mult2` canonical range `:191-220` starts at the opening brace, not the signature; report mislabels 191 as the signature (signature is line 190).
  - **Decision**: repaired
  - **Action**: Verified via `palace-codemap read_range palace/linalg/chebyshev.cpp 185 200` — line 189 = `template`, line **190** = `void ChebyshevSmoother<OperType>::Mult2(...)`, line **191** = `{`. Corrected CYCLE.md §Summary verdict, §Per-citation audit Theme-1 `Mult2` bullet (sig@191→@190, range `:191-220`→`:190-220`), §Per-citation audit Theme-2 `Mult2` bullet, §Proposed-changes R1 + R4 prose, and both `verified_against` YAML entries (`:191-220`→`:190-220`). The off-by-one in the L1/L2 *anchors*' own `:191` is routed to the carry-forward OQ (not editable from this report).

- **Finding (Issue 2)**: `chebyshev.hpp:43` is a comment; `mutable VecType d, r;` is line 44 — report verdicts the stale citation "exact."
  - **Decision**: repaired
  - **Action**: Verified via `read_range palace/linalg/chebyshev.hpp 40 48` — line **43** = `// Temporary vector for smoother application.`, line **44** = `mutable VecType d, r;`. Corrected CYCLE.md §Summary verdict, §Per-citation audit Theme-1 `hpp:43` bullet (verdict flipped from "supports/Exact" to "supports at :44 / off-by-one miscitation"), §Supporting-evidence hpp line, §Proposed-changes (added Refinement R1b `hpp:43`→`:44`) and the `verified_against` YAML entry (`hpp:43`→`hpp:44`). No wrong citation left marked verified.

- **Finding (Issue 3)**: inherited-anchor element-kernel drift correctly flagged, but the L2 anchor carries it at FOUR sites (lines 35, 143, 245, 247), not just the §Evidence block.
  - **Decision**: repaired (within report + OQ scope; the anchor entries themselves are out of this report's scope)
  - **Action**: Expanded CYCLE.md §Open-questions item 1 to enumerate ALL six sites (`book/src/L2/chebyshev-iteration.md` lines 35/143/245/247 + `book/src/L1/chebyshev-smoother.md` lines 245/247) plus the anchors' `Mult2 :191`→`:190` reconcile. Promoted to `scaffolding/open-questions.md` as slug `chebyshev-anchor-element-kernel-and-mult2-carry-forward-sweep`, naming all four L2 sites + both L1 sites. Did NOT edit the L2/L1 anchor entries (out of this report's scope — correctly routed to a follow-up abstractor/lifter).

- **Finding (Issue 4)**: `hpp:50-76` envelope over-coarsens four separately-verified constructs (`:50-58`, `:60-68`, `:71`, `:73-76`).
  - **Decision**: repaired (note recorded)
  - **Action**: Added a §Open-questions caveat noting the over-coarsening and that a follow-up may split the `verified_against` entry back into the four precise ranges. Left the YAML envelope in place (cosmetic; not a falsified claim) — the precise sub-ranges remain fully documented in the per-citation audit.

### Unrepairable findings

None. All four findings were mechanical citation-range / cross-reference corrections within repair authority. The verdicts themselves (L1>L0 CONFIRMS-WITH-REFINEMENT, L2>L1 CONFIRMS, fusion algebraically sound, no `partly-constructive` caveat) are unaffected and stand.

## Suggested resolution

`ready`. Integrator notes: this is a lowering-verifier audit (no `book/` mutation); the corrected `verified_against` blocks + range refinements (R1/R1b/R2/R3/R4) route to a follow-up abstractor/lifter on the two theme files. The carry-forward OQ (`chebyshev-anchor-element-kernel-and-mult2-carry-forward-sweep`) covers the L1/L2 anchor entries — a separate follow-up dispatch must sweep all six enumerated sites + the `Mult2 :191`→`:190` anchor reconcile. The `hpp:50-76` over-coarsening is a low-priority precision note, not a blocker.
