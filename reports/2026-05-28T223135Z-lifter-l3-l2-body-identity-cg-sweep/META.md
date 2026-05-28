---
verifies: ../REPORT.md
critiqued_at: 2026-05-28T224500Z
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
repaired_at: 2026-05-28T225200Z
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

# META: verification of "Re-anchor krylov-step-body-identity" (cg.md own-provenance sweep)

## Critique

### Checks run

**citation-validity — pass.** The report's central factual claim is that `cg.md:341-362` and the sub-range `:351-362` dangle because `cg.md` was reduced to a 165-line stub in the cycle-009/010 corpus reduction. Confirmed independently: `wc -l book/src/spec/slices/cg.md` = 165, and a full read of the stub shows it now carries only (i) the supersession header (lines 1-23, naming the firm entries that absorbed the slice's L0–L4 content, including `L3-L2/krylov-step-body-identity.md` at line 11) and (ii) the unique-retained L4 v0.5 first-iteration-unrolling material (lines 25-166). The verbatim Claim-2 text "*The L2→L3 rotation on the step body is therefore the identity in form…*" does NOT appear anywhere in the stub — grep over `identity in form` / `step body lifts` / `Claim 2` returns nothing. So all three cited ranges genuinely dangle; the demotion-to-parenthetical-provenance is the correct remedy. The three live co-citations the report deliberately leaves untouched also resolve: `arnoldi_step.md` is 302 lines (so `:178-213` and the sub-range `:185-188` are in-range, and the MGS sequential-obstruction content sits there per the read), and `gmres.md` is 671 lines (so `:459-471`, the `inner_loop` body, is in-range — confirmed `inner_loop` definitions at gmres.md:122/278/304). The demotion follows the cycle-013/014/015/016 lifted-evidence annotation convention; the precedent renderings at `L2/krylov-step.md:138,146` match the parenthetical "(Original pre-reduction slice ranges: …)" shape the report adopts.

**surface-or-evidence — pass.** This is a refinement-shaped proposal touching the surface of an existing firm theme, but the surface change is exclusively citation-provenance hygiene (three dangling `cg.md` ranges → in-document terminal home + parenthetical original-range note). The report is explicit and repeatedly so (Summary, Discipline notes "What changed", §Proposed-changes trailing notation block) that NO body-shape, signature, decomposition, justification-kind, or status change is made. This is the allowed retroactive-evidence / citation-backfill shape, not a pure unsubstantiated rotation_claim. The unchanged rotation content (the §"Rewrite shape" line-by-line identity table, the four applicability conditions, the empirical-match/structural justification) is the standing evidence. Pass.

**rotation-quality — pass (the asserted rotation is unchanged; verified not degraded).** The theme asserts an identity-in-form rotation on the kernel body plus two state-hiding/abstraction-by-role rotations at the wrapper (L3 `(op, K, s)` tuple → L2 unified `IterState` = state hiding; L3 tail-recursive `iterate_while_L3` → L2 outer-driver-by-role = abstraction-by-role). These are genuine rotations (state hiding / coarser substitution), not renaming-only, and they are untouched by this dispatch. The body identity-in-form is correctly NOT claimed as a "rotation" in the compaction sense — it is an identity edge, explicitly delimited from the two wrapper rotations that carry the actual compaction. No degradation introduced. Pass.

**variant-axis-coverage — pass.** The theme's §Applicability-conditions condition 4 ("the variant-axis profile is closed at six") and condition 1 (re-audit trigger for a new body shape) explicitly scope the six orthogonal axes (preconditioner-side, orthogonalization variant, polynomial-kind, first-iteration-unrolled, restart shape, in-place/out-of-place) and the MINRES/BiCGStab out-of-scope obstruction case. This dispatch touches none of that — the re-anchor is orthogonal to variant coverage. The pre-existing coverage is intact and the report does not perturb it. Pass.

**cross-reference-integrity — pass (the focus check; the "terminal home is this entry's own §Verified-against" reasoning is sound, NOT a self-referential dangle).** This is the load-bearing verification. The producer's claim is that the verbatim Claim-2 body-identity text *physically lives* at this theme's §Verified-against bullet 1, and that the rest of the chain already names this §section as the lifted-in terminal home. Both halves verified:
  - The verbatim quote physically resides at `book/src/L3-L2/krylov-step-body-identity.md:125` ("*The L2→L3 rotation on the step body is therefore the **identity in form**: no unfolding, no global lift, no schema change.*"). Read directly. So pointing the three intra-document sites at this bullet is pointing at the genuine physical home of the claim, NOT a relay to an empty/dead pointer.
  - `book/src/L3/krylov-step.md:188` reads: "`book/src/L3-L2/krylov-step-body-identity.md` §Verified-against (line 125; lifted from the original `cg.md:341-362` per the cycle-009 corpus reduction, preserved there with the verbatim Claim-2 quote at original slice line 360)". Confirmed — the L3 operator entry independently designates THIS §section as the terminal home.
  - `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:204` reads: "The CG half of this evidence (`cg.md:351-362`) has since been lifted into the firm theme [`L3-L2/krylov-step-body-identity`] §Verified-against per the cycle-009 corpus reduction; the historical slice ranges are retained here as the audit's provenance record". Confirmed — the upstream L4>L3 theme independently points HERE.
  This is the critical anti-circularity finding: the target is NOT self-referential in the defective sense. The defect being fixed was precisely that the §Verified-against bullet cited the *dead slice range* as a live source while the rest of the chain already treated that bullet as the lifted-in home; the re-anchor resolves the contradiction by declaring the bullet the terminal home (it physically holds the quote) and demoting the slice range to parenthetical provenance. A pointer from a §section to itself would be circular ONLY if the §section held no independent content — but it holds the verbatim quote, so it is a genuine terminal home, exactly the established claim-home semantics (cf. the cycle-015/016 precedents at OQ ledger lines 2813/2912). The producer's "terminal *methodological* claim, does not lower to an L0 Palace source" reasoning (Discipline notes; Open-questions lifting-note) is also sound — the body-identity observation is about primitive signature shapes, and the distinct CG *primitive-sequence* L0 home (`L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern B, `iterative.cpp:360-486`) is correctly identified and confirmed present in the cg.md stub at line 8. All `[link]`/slug references in the three proposed-changes `[new]` blocks resolve (the bullet self-reference, the upstream theme name, the L3 entry, the L2 precedent). Pass.

**edge-label-fidelity — pass.** The theme carries the L3>L2 edge label throughout; the report's prose discusses exactly the L3→L2 body-identity edge (and its identity twin, the L2→L3 cycle-002 lift). No edge-label mismatch. The Summary's repeated references to upstream `L4-L3` and the `L3` operator entry are correctly framed as *chain context* for locating the terminal home, not as the edge under modification. Pass.

**plan-kind-consistency — pass.** Declared as a lifter re-anchor (pure citation provenance sweep); content shape matches exactly — three `edit:` blocks, all swapping a dangling `cg.md` range for an in-document terminal-home reference plus parenthetical original-range note, with explicit "no body-shape / signature / decomposition change" framing. Status correctly held at `firm` (the dangling provenance never gated the firm status, only citation hygiene), with the report explicitly stating §"Speculative L3 operators" already reads "None" so nothing to firm there. This is textbook lifter scope, not mis-classified authoring. Pass.

**skill-uptake-survey — pass.** The report references `skills/verify-citation-range/SKILL.md` §"Producer self-verification before emitting citations" and explicitly applies its step-4 emit-time procedure (confirm new target is terminal, not a relocated dangle) in the Discipline-notes "Self-verify" bullet, citing the friction-ledger entry `producer-citation-drift-verify-not-self-invoked`. The skill whose shape the proposal implies is invoked and named. Pass (telemetry: clean uptake).

### Issues found

No blocking or warning issues. The three focus questions all resolve in the report's favor:

1. **(focus 1, cross-reference-integrity) — clean.** The "terminal home is this entry's own §Verified-against" reasoning is sound and NOT a self-referential dangle. The verbatim Claim-2 quote physically lives at `krylov-step-body-identity.md:125`; both `L3/krylov-step.md:188` and `L4-L3/krylov-step-typed-wrapper-dissolution.md:204` independently designate that §section as the lifted-in terminal home. The pointer terminates in genuine content, not a relay.

2. **(focus 2, citation-validity) — clean.** `cg.md` is a 165-line stub (verified `wc -l`); the verbatim claim and the cited line ranges (341/351/360) are absent from the stub, so `:341-362` / `:351-362` genuinely dangle. The demotion-to-parenthetical-provenance matches the cycle-013/014/015/016 convention and the live `L2/krylov-step.md:138,146` precedent renderings.

3. **(focus 3, scope) — clean.** The `gmres.md:459-471` co-pointer (and the `arnoldi_step.md:178-213` / `:185-188` co-citations) resolve in live slices (671 / 302 lines respectively) and are correctly left out of scope. The report acknowledges the gmres co-pointer explicitly (§Open-questions "Co-pointer note") and notes the parallel future sweep should `gmres.md` later be reduced — correct deferral, not a hidden omission.

Minor observation (non-blocking, NOT a defect — surfaced for integrator awareness only): the report's frontmatter `inputs:` lists `book/src/L2/krylov-step.md` §Evidence "lines 138/146 + line 9" as the precedent-convention anchor, but the L2 entry's annotation-convention prose lives at lines 138/146 within §Evidence (line 134); "line 9" appears to be a stale/imprecise pointer (the L2 entry's line 9 is not the convention anchor). This is in the report's own working-notes frontmatter, not in any proposed `book/` edit, so it does not affect the artifact and is not a citation-validity failure on the proposed changes themselves. Flagging only so the repairer/integrator is aware the "line 9" frontmatter reference is imprecise; the load-bearing precedent anchors (138, 146) are correct.

## Repair

### Fixes attempted

- **Finding**: frontmatter `inputs:` cites the L2 precedent-convention anchor as `book/src/L2/krylov-step.md` §Evidence "lines 138/146 + line 9" — the "line 9" reference is imprecise (the lifted-evidence annotation-convention prose lives at §Evidence lines 138/146; line 9 sits in §Context and carries a *different* lift note — the sequential-obstruction lift to the concept page + L3 entry, not the annotation-convention precedent being referenced).
  - **Decision**: repaired.
  - **Action**: confirmed against `book/src/L2/krylov-step.md` that lines 138/146 (within §Evidence, heading at line 134) carry the lifted-evidence annotation-convention rendering ("terminal firm home is …; the … rendering remains live …; (Original pre-reduction slice ranges: …)"), while line 9 (§Context) is an unrelated lift note. Removed the imprecise "+ line 9" / ",9" pointer at the two working-notes sites that carry it, leaving the two correct load-bearing anchors:
    - `reports/<id>/CYCLE.md` frontmatter `inputs:` (was "lines 138/146 + line 9" → "lines 138/146").
    - `reports/<id>/CYCLE.md` §Supporting evidence (was `…krylov-step.md:138,146,9` → `…krylov-step.md:138,146`).
  - **Rationale**: trivially surgical, mechanical citation re-anchor in the report's own working-notes (not artifact); the off-pointer was a single stale line number with a clearly-correct two-anchor replacement evident from the L2 file. No content authored.

The three proposed `book/` edits (the citation re-anchor at §Applicability-conditions cond. 3, §Justification-kind, and §Verified-against bullet 1 of `book/src/L3-L2/krylov-step-body-identity.md`) were verified clean by the critic and are untouched — within the repairer's read-only-on-artifact discipline, no artifact edit was applied.

### Unrepairable findings

None. The sole observation was a non-blocking working-notes imprecision, repaired in place.

## Suggested resolution

`ready`. All 8 critic checks pass; the single non-blocking frontmatter/supporting-evidence imprecision is repaired. The integrator may apply the three `book/src/L3-L2/krylov-step-body-identity.md` re-anchor edits as-is (dangling `cg.md` provenance ranges → in-document terminal firm home + parenthetical original-range note); status stays `firm`; closes OQ `l3-l2-body-identity-cg-md-citation-sweep` per the report's §Open-questions.
