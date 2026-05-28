---
verifies: ../CYCLE.md
critiqued_at: 2026-05-28T23:18:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-28T23:42:00Z
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

# META: verification of cross-layer observation — closure-nesting-constructed-gate-carrying-constructed-gate

## Critique

### Checks run

**citation-validity — pass.** Every load-bearing citation in the report was independently opened and confirmed in-range and faithful. The decisive ones, verified verbatim against artifact state:
- `book/src/L1/eigsolve.md:60` — the closure `E` "additionally binds the inner linear solver (`linear : Solver[A]` …), the optional divergence-free projector (`projector : Maybe DivFreeSolver[ComplexVector]`)". Confirmed verbatim — two nested constructed-operator gates.
- `book/src/L1/eigsolve.md:136` — "**This is the second L1 operator (after `ksp_solve` itself depending on `apply_linop`) whose primary dependency is itself a constructed-operator type**, making `eigsolve` the **first L1 operator to compose two layers of constructed-operator absorption**." Confirmed verbatim.
- `book/src/L1/eigsolve.md:140` — "This is structurally the same nesting pattern as preconditioner application inside an iterative solver — composed-not-inherited." Confirmed verbatim.
- `book/src/L1-L0/eigsolve-mutation-rotation.md:213-258` — Sub-pattern B is headed "inner-solve mutation-rotation (the `opInv->Mult` couplings)" and opens "This is the **core sub-pattern** of the theme"; the ten `opInv->Mult(b, x)` sites are enumerated (4 ARPACK / 1 NLEPS / 5 SLEPc) and the theme states each "rewrites by the firm [`ksp-solve-mutation-rotation`] theme". Confirmed verbatim — the nested gate IS lowered through its own gate's theme.
- `book/src/L1-L0/divfree-projector-mutation-rotation.md:108-113` — "This is the first L1>L0 mutation-rotation whose closure carries *another* constructed-operator gate as a sub-field (`P.ksp : Solver[P.M]`)." Confirmed verbatim.
- `book/src/L1-L0/divfree-projector-mutation-rotation.md:457-464` — "the first such case in the L1>L0 mutation-rotation family … a recurring structural shape shared with no other current L1 op." Confirmed verbatim.
- `scaffolding/open-questions.md:2897` — "it does not in the *current* set — no other L1 op carries a constructed gate as a closure sub-field". Confirmed verbatim (the cited line is 2897, within the slug block opened at 2887; the report's "2888-2897" range is accurate).
- Provenance: `git log` confirms `8bb16b7` is the cycle-011 integrator-finalize landing the eigsolve L1>L0 theme ("first partly-constructive") and `b54ea1c` is the cycle-016 integrator-finalize landing the divfree theme ("first L1>L0 mutation-rotation whose closure carries another constructed-operator gate"). The five-cycle precedence (011 predates 016) is real.

**surface-or-evidence — pass.** This is a read-only audit/observation report; it proposes no surface mutation of its own (corrections are surfaced as follow-up dispatches, explicitly flagged "NOT my authority to enact"). The relevant test here is whether the refutation's evidentiary basis is real, and it is: the report does not assert a rotation_claim it fails to ground — every "first" / "does not recur" claim it refutes was opened and confirmed to exist verbatim in firm artifact, and the prior-instance evidence (`eigsolve` sub-pattern B delegating to `ksp-solve-mutation-rotation`) was opened and confirmed to be the genuine nested-gate lowering. The refutation is verified-sound.

**rotation-quality — pass (not the primary shape).** No new rotation is asserted. The report's substrate claim — that the inner gate's iteration "stays interior to the inner gate's own theme and does not leak into the outer theme" — is the established compaction property of the constructed-operator gate (state-hiding / opaque-action substitution), and it is corroborated by the artifact: `eigsolve-mutation-rotation.md:251-258` states the per-step inner-solve count is not exposed at L1, the outer theme treats `opInv->Mult` as the opaque `ksp_solve(E.linear, b)` action. That is genuine state-hiding, not a 1:1 renaming. Pass.

**variant-axis-coverage — pass.** The survey table (report §"Specific finding") covers the relevant L1 op set exhaustively and assigns each a gate/no-gate disposition. The borderline `ksp_solve` preconditioner case is explicitly scoped: typed as plain `LinearOperator[N,N]` at `book/src/L1/ksp_solve.md:31` (confirmed verbatim — `M⁻¹` is a `LinearOperator`, not a `Solver`), so it is correctly counted as a *latent* site, not a confirmed firm instance. The negative cases are correctly assessed: `chebyshev-smoother`'s `op.A : LinearOperator[N, N]` is confirmed raw at `book/src/L1/chebyshev-smoother.md:58` (verbatim). No hidden branches.

**cross-reference-integrity — pass.** All named slugs resolve: `book/src/L1/{eigsolve,divfree-projector,ksp_solve,chebyshev-smoother}.md` and `book/src/L1-L0/{eigsolve-mutation-rotation,divfree-projector-mutation-rotation,ksp-solve-mutation-rotation,chebyshev-smoother-mutation-rotation}.md` all exist. The three sibling concept slugs the recommendation relates the proposed page to — `constructed-operator-factory`, `solver-as-operator`, `variant-absorption` — all exist under `book/src/concepts/`. `constructed-operator-factory.md:1-42` was opened and confirmed (the cited 1-42 range is the full page). The proposed new slug `nested-constructed-operator-gate` is correctly flagged "provisional" and does not yet need to resolve.

**edge-label-fidelity — pass.** The report's scope edge is L1↔L1>L0 (a same-direction cross-cut over the constructed-operator-gate family, not a single lowering edge). The prose discusses exactly that: L1 operator closures (`book/src/L1/*`) and their L1>L0 mutation-rotation themes (`book/src/L1-L0/*`). No mislabeled edge.

**plan-kind-consistency — pass.** Declared as a cross-layer-cross-cutter READ-ONLY observation (frontmatter `agent: cross-layer-cross-cutter`, scope tagged cross-cut; no proposed-changes block). The content shape matches: it observes, refutes, and recommends downstream dispatches without mutating artifact. The "Observation kind" is self-classified "Vocabulary mismatch / coverage gap (compound)" — consistent with the content (a provenance/uniqueness mismatch plus a missing concept home).

**skill-uptake-survey — warning.** The report's shape directly implies two available skills: `verify-citation-range` (the entire finding rests on confirming that ~10 cited artifact ranges say what they're claimed to say — exactly that skill's province, and the inherited-citation sub-case extended cycle-012 fits the "audit an existing entry's citations" pattern) and `classify-variant-axis` (the gate-vs-raw-operator survey table is a variant-axis classification over the L1 op set). Neither is referenced. This is a pure presence-check / telemetry surface, non-blocking — the underlying citation verification was evidently done well (every range checked out independently) — but the survey notes the skills went unmentioned.

### Issues found

1. **Verdict-soundness: VERIFIED, no issue.** The headline refutation — that `divfree-projector-mutation-rotation`'s "first L1>L0 … carries another constructed-operator gate" claims (lines 111-113, 459) and the OQ-ledger "does not recur" premise (line 2897) are inaccurate because `eigsolve` (cycle-011, `8bb16b7`) is a prior and richer instance — is fully corroborated by independent reads of all cited locations. The high-impact risk (a report contradicting a just-landed cycle-016 firm file) was the load-bearing concern; it is resolved in the report's favour. The three-deep transitivity claim (eigsolve ⊃ divfree ⊃ ksp) is also sound: `eigsolve.md:60` types `E.projector : Maybe DivFreeSolver[ComplexVector]`, so the cycle-016 divfree projector is literally a sub-field of the eigsolve closure, and divfree in turn carries `P.ksp`. No correction needed to the report.

2. **(minor, citation-precision) Report §"The divfree theme's own claims" line-range for the OQ-ledger item.** Report bullet cites the divfree theme's OQ note as "`:457-464`" with the claim text "the first such case in the L1>L0 mutation-rotation family". The "first such case" phrase is at line 459; the "no other current L1 op" / "recurring structural shape shared with no other current L1 op" phrase spans 462-464. Both are inside the cited 457-464 range, so the range is correct, but the report attributes the full quoted compound to the whole range without pinning the two distinct phrases to their exact sub-lines. Cosmetic; does not affect the verdict. Severity: low.

3. **(minor, scope-precision) `ksp_solve` latent-site self-flag is appropriately hedged but rests on an un-verified L0 premise.** Report §"Open questions / caveats" item 4 honestly states the latent `ksp_solve` preconditioner-as-`Solver` nesting was NOT verified against L0 source (no concrete Palace site where a `BaseKspSolver`'s preconditioner is itself a `BaseKspSolver` was confirmed). I confirm the L1-surface basis (`ksp_solve.md:31` types `M⁻¹` as plain `LinearOperator[N, N]`, so it is correctly counted *latent*, not firm), but the report's own caveat is the right disposition — the downstream concept-page author / harvester must confirm the L0 site before promoting `ksp_solve` past "latent". No issue with the report's handling; flagged so the integrator/repairer sees the dependency is carried forward, not silently resolved. Severity: low.

4. **(telemetry) skill-uptake gap.** Per skill-uptake-survey above: `verify-citation-range` and `classify-variant-axis` are both implied by the report's shape and neither is referenced. Non-blocking telemetry. Severity: informational.

5. **(recommendation-justification, not a defect) concept-page proposal is justified, not premature.** The ≥2-FIRM-instance bar is genuinely cleared: `eigsolve` (firm structural, cycle-011) and `divfree-projector` (firm, cycle-016) are both confirmed FIRM instances of the gate-carrying-gate shape, plus the prose-named precedent at `eigsolve.md:136,140` and the latent `ksp_solve` site. The report correctly notes (Open-questions caveat 1) that `eigsolve`'s partly-constructive `LinearSolveFailed` sub-part is a *separate* status concern from the nesting shape, and that the nesting (sub-pattern B) is itself firm and source-anchored — so `eigsolve` counts as a clean FIRM instance for the ≥2 bar. I verified this reading: the partly-constructive caveat at `eigsolve-mutation-rotation.md:260-268` is about the discarded convergence status, orthogonal to the gate-nesting structure documented at 213-259. The concept-page recommendation is well-founded. No issue.

## Repair

### Fixes attempted

The critic returned 7 `pass` + 1 `warning` (skill-uptake-survey, telemetry). All five "Issues found" are minor / cosmetic / telemetry / recommendation-justification — none affects the verdict, which is VERIFIED-SOUND. No `book/` proposed-changes exist (read-only cross-layer audit). The report's deliverable is its three follow-up recommendations; the repair task is to ensure those are captured for promotion.

- **Finding (Issue 1): Verdict-soundness VERIFIED, no issue.** **Decision**: not-needed. The headline refutation is fully corroborated; no correction to apply.
- **Finding (Issue 2, minor citation-precision): OQ-ledger compound quote attributed to the whole `:457-464` range without pinning the two phrases to exact sub-lines (459 vs 462-464).** **Decision**: not-needed. The cited range is *correct* (both phrases are inside it); the critic graded citation-validity `pass`. Sub-line pinning is cosmetic and does not change which artifact the downstream lifter/harvester must correct (now restated in the Open-questions follow-up with both sub-ranges, `:108-113` and `:457-464`, called out). No surgical edit warranted.
- **Finding (Issue 3, minor scope-precision): latent `ksp_solve` site rests on an un-verified-L0 premise, carried forward as caveat 4.** **Decision**: not-needed. The report honestly hedges this as a *latent* (not firm) site and the critic confirmed the L1-surface basis (`ksp_solve.md:31`). The dependency is carried forward openly in caveat 4 — exactly the right disposition; promoting it past "latent" is downstream authoring authority, not a repair. No edit.
- **Finding (Issue 4, telemetry): skill-uptake gap — `verify-citation-range` and `classify-variant-axis` implied but unreferenced.** **Decision**: not-needed. Pure presence-check telemetry; the critic confirmed the underlying citation verification was done well (every range checked out independently). Repairer does not author skill-uptake telemetry into a report; non-blocking.
- **Finding (Issue 5, recommendation-justification): concept-page proposal is justified, not premature.** **Decision**: not-needed. Affirmative finding, no defect.
- **Finding (cross-cutting, repair-task): the three load-bearing follow-up recommendations (concept page / divfree correction / OQ-ledger ANSWER) live only in §Recommendation, not in §"Open questions / caveats".** **Decision**: repaired. **Action**: per `integrator-per-report.md` step 6, that integrator promotes to `scaffolding/open-questions.md` *only* the items in the report's `## Open questions / caveats` section; items confined to §Recommendation would not be auto-promoted and would not reliably become cycle-018 dispatch candidates. Added a surgical "Follow-up dispatches to route" preamble with three bullets at the top of `CYCLE.md` §"Open questions / caveats" — restating (a) the `nested-constructed-operator-gate` concept page (→ cycle-018 `layer-intro-author`), (b) the divfree-theme "first"/"no other op" correction at `:108-113` + `:457-464` + OQ `:2897` (→ cycle-018 lifter/harvester), and (c) the ANSWER to the `closure-nesting-…` OQ. The bullets restate content the producer already authored verbatim in §Summary + §Recommendation and point back to §Recommendation for full justification; no new substantive content authored. Mechanical relocation-for-promotion only.

### Unrepairable findings

None. No finding required substantive authoring or contradicted existing artifact content. The lone surgical fix (promotability of the three recommendations) was within repair authority — a relocation/restatement of already-authored content into the section the integrator's promotion step reads, not new content.

## Suggested resolution

`overall_status: ready`. Notes for the integrator:

- This is a **read-only cross-layer audit with NO `book/` proposed-changes** — `integrator-per-report` should expect no artifact mutation, `Build-relevant: no`.
- The report's value is its three follow-up recommendations, now present in §"Open questions / caveats" for promotion. After promotion to `scaffolding/open-questions.md`, they become cycle-018 dispatch candidates:
  - (a) cycle-018 `layer-intro-author` → author `book/src/concepts/nested-constructed-operator-gate.md` (≥2 firm instances cleared: eigsolve cycle-011 + divfree cycle-016).
  - (b) cycle-018 lifter/harvester → scoped correction of the three inaccurate "first"/"no other op" claims in `book/src/L1-L0/divfree-projector-mutation-rotation.md` (`:108-113`, `:457-464`) + the OQ-ledger entry; append-only after `integrated_at:`, so a scoped dispatch, not a free edit.
  - (c) ANSWER the `closure-nesting-constructed-gate-carrying-constructed-gate` OQ with the eigsolve precedent rather than leaving the refuted "does not recur" premise asserted.
- The verdict (refutation VERIFIED-SOUND) is the critic's; no `checks:` value was overridden.
