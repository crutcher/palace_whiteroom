---
verifies: ../CYCLE.md
critiqued_at: 2026-05-28T201500Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-28T203000Z
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

# META: verification of "Combinator candidate — fixed-count bounded iteration is `iterate_while_pure` with a step-count predicate (no new combinator)"

## Critique

### Checks run

- **citation-validity — warning.** Most citations verified exact: `L4/chebyshev.md:137` (`forM_`), `:148` (`foldM`), Status caveat at 400-419; `l4_calculus.md:418` (the §6.5 step-5 strawman precedent, verbatim as quoted) + `:382-385` (`run_lbm` `iterate_while_pure … (\s -> s.step < maxSteps)` call shape); `iterate-while.md:7` canonical-primitive claim naming Chebyshev; `chebyshev.cpp:191`/`:200` (outer `for it`/inner `for k`, both static-bound, no convergence test — codemap-confirmed). **One wrong citation, used twice:** `L3/chebyshev.md:309,318` (Instance 4 line 89-93 and Supporting evidence line 238) is cited as the `itloop`/`kloop` tail recursions, but 309/318 are §6 body-identity-law *prose*; the actual `kloop` is at 221-230 and `itloop` at 231-233. ~90-line drift.
- **surface-or-evidence — pass.** Not a surface-mutating refinement: the report explicitly does NOT mutate `book/` and stages a follow-up edit. It is a route-decision/observation with a concrete sketch, properly scoped as combinator-miner output; no rotation_claim-without-surface problem applies.
- **rotation-quality — pass.** The `forM_`/`foldM` → `iterate_while_pure`-with-step-count-predicate mapping is sound and IS a compaction: it collapses two un-anchored ad-hoc iteration vocabularies into one canonical firm primitive whose only differentiator (step-count vs convergence) lives in the predicate, not the combinator. Verified against `iterate-while.md:50,57,102` (predicate folds counter into carry; `cg.md:217` `s.it < config.max_it`) and the §6.5-step-5 precedent. More-abstract / fewer-rows = a genuine rotation, not renaming.
- **variant-axis-coverage — pass.** The two real axes are covered: (i) predicate shape (step-count vs convergence) — the load-bearing argument; (ii) inner-loop presentation (`iterate_while_pure` carry-`st` vs `iterate-while-with-prev` closure-`prev`) — explicitly deferred to the firming follow-up as OQ 1 with a stated default (carry-`st`, since 4th-kind `st=()` is the degenerate no-prev case). The with-prev consumer claim is confirmed against `iterate-while-with-prev.md:7` (names Chebyshev `x_{k-1}`). No hidden branch.
- **cross-reference-integrity — warning.** All `[link]` targets resolve (`iterate-while.md`, `iterate-while-with-prev.md`, `L3/chebyshev.md`, `L4/index.md`); the dep-map row (`index.md:56`) carries the exact "iteration combinators UNRECONCILED" text the staged edit replaces, and the cohort headings (`index.md:32` "Firm at L4 (3)", `:38` "Rough-in at L4 (1)") confirm the 3→4 count. Only defect is the slug-internal line anchors 309/318 above (the named loops exist, the line pointers don't).
- **edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried as the proposal's primary claim; the work is intra-L4 re-anchoring. The incidental L4>L3 / L3↔L2↔L1 references (Instance 4, the L3 `iterate_while_pure_L3` shape at `iterate-while.md:193-195`) are described in the correct direction and match `L3/chebyshev.md` §6.
- **plan-kind-consistency — pass.** A combinator-miner returning a REUSE/negative result (do NOT firm a new row) is in-role and well-precedented; the content shape (pattern instances, route recommendation, no new operator file) matches. The level decision (no new L4 row) has correct provenance: routed from the cycle-013 harvester META (`follow_up_agent: combinator-miner`, "Unrepairable findings" → combinator-miner, "Suggested resolution" naming strawman §6 + `iterate-while.md:7`), all verified.
- **skill-uptake-survey — warning.** The report's shape (citation-range assertions across L0 + several L4/L3 artifact files, plus a rotation/reuse claim) maps to `verify-citation-range`, `verify-rotation-citation`, and `propose-rotation`; none is referenced as invoked. Non-blocking telemetry — and the one missed-anchor citation (309/318) is exactly the class `verify-citation-range` would have caught.

### Issues found

1. **Wrong line anchors for the L3 Chebyshev loops (citation-validity, cross-reference-integrity, medium).** `CYCLE.md` §"Pattern instances" Instance 4 (lines 88-93: "`L3/chebyshev.md:318` `itloop` and `:309` `kloop`") and §"Supporting evidence" (line 238: "`book/src/L3/chebyshev.md:309,318` — the L3 `kloop`/`itloop` tail recursions") both point at §6 body-identity-law prose. The real definitions are `kloop` at `L3/chebyshev.md:221-230` and `itloop` at `:231-233`. The named loops exist and the claim about them is correct; only the line pointers are wrong (consistent ~90-line drift). Candidate for repair: re-point both citations to 221-233.

2. **Skill-invocation telemetry absent (skill-uptake-survey, low/non-blocking).** No reference to `verify-citation-range` / `verify-rotation-citation` despite a citation-heavy, rotation-asserting report. Surfaced as telemetry; the missed anchor in issue 1 is the concrete cost.

3. **Watch-item, not a defect (informational).** OQ 1 (inner-loop carry-`st` vs `iterate-while-with-prev` closure-`prev`) is correctly left open and well-framed; the default recommendation (carry-`st`, 4th-kind `st=()` degenerate) is defensible. The claim that re-anchoring firms `L4/chebyshev` rough-in→firm (L4 firm 3→4) is contingent on a cycle-015 follow-up applying the body re-anchor + dep-map rewrite — correctly stated as staged, not applied. No over-claim: the report firms nothing itself.

## Repair

### Fixes attempted

- **Finding**: Wrong line anchors for the L3 Chebyshev loops — `L3/chebyshev.md:309,318` (cited twice, Instance 4 + Supporting evidence) point at §6 body-identity prose, not the `kloop`/`itloop` definitions (~90-line drift).
  - **Decision**: repaired
  - **Action**: Verified via `Read` of `book/src/L3/chebyshev.md:215-244` — `kloop` is defined at `:223-230` (call site `:221`), `itloop` at `:231-233`; `:309`/`:318` are §6 body-identity-law prose. Corrected both citations in CYCLE.md: §"Pattern instances" Instance 4 → "`L3/chebyshev.md:231-233` `itloop` and `:221-230` `kloop`"; §"Supporting evidence" → "`book/src/L3/chebyshev.md:221-233` — the L3 `kloop` (`:221-230`) / `itloop` (`:231-233`) tail recursions". The L0 `chebyshev.cpp:191`/`:200` codemap-confirmed citations left untouched.

- **Finding**: Skill-invocation telemetry absent (`verify-citation-range` / `verify-rotation-citation` not referenced).
  - **Decision**: not-needed
  - **Rationale**: Non-blocking telemetry only (critic marked it `warning`, not a content defect). The concrete cost it flagged (the missed L3 anchor) is repaired above; no further action within repair authority.

- **Finding**: REUSE-iterate-while route + `iterate_while_pure` step-count-predicate re-anchor sketch + staged L4-firm-3→4 proposal.
  - **Decision**: not-needed (sound as-authored)
  - **Rationale**: Critic confirmed the route against `iterate-while.md:7` + strawman `l4_calculus.md:418`; `rotation-quality` and `variant-axis-coverage` both `pass`. The proposed-changes block is correctly staged-not-applied (`L4/index.md` dep-map row rewrite + Status `rough-in`→`firm`) for a cycle-015 lifter/abstractor to enact. Left intact as a PROPOSAL; nothing firmed this cycle.

### Unrepairable findings

None. The sole repair-class defect (wrong L3 loop anchors) was mechanical and is fixed. The body re-anchor / firming is substantive authoring deliberately deferred by the report itself to a cycle-015 follow-up — not a repair-authority item and not a blocker.

## Suggested resolution

`ready` for the integrator. Notes:
- This report mutates no `book/` surface; the integrator should NOT apply the staged `L4/index.md` edit block this cycle — it is explicitly marked for cycle-015 enactment.
- Two OQs were promoted to `scaffolding/open-questions.md` (the deferred inner-loop-presentation choice `chebyshev-l4-inner-loop-presentation-carry-st-vs-with-prev`, and the firming follow-up `chebyshev-l4-firm-via-iterate-while-reanchor`). Cycle-015 planner should pick up the firming OQ → lifter/abstractor to flip `L4/chebyshev` rough-in→firm (L4 firm 3→4).
