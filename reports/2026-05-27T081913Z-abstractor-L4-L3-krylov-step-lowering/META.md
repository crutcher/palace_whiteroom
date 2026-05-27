---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T09:15:00Z
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
repaired_at: 2026-05-27T08:36:15Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: repaired
overall_status: ready
follow_up_agent: null
---

# META: verification of REPORT — L4>L3 theme sketch — krylov-step typed-wrapper dissolution

## Critique

### Checks run

**citation-validity (pass).** All cited spec/concept ranges resolve and the cited content supports the claims made. Spot-verified: `cg.md:341-362` contains the L2→L3 rotation claims; Claim 2 at `:351-360` states verbatim "The L2→L3 rotation on the step body is therefore the **identity in form**" — matches the report's audit verdict. `arnoldi_step.md:178-213` contains the partial-lift story with the MGS sequential obstruction at `:205-211` — matches the report's localisation of the obstruction below the `krylov-step` body. `first-iteration-unrolling.md:21-37` contains the Form B `first_step` / `steady_step` signatures and the PrevCarry-as-closure-parameter framing — matches the report's claim verbatim. `solve-monad.md:53-54` matches the `inner_loop` / `restart_cycle` / `modify SimState.it` discipline. `state-stratification.md:1-45` matches. `concepts/counter-update.md` exists and supports the "counter update is L3-native" claim. Minor inconsistency: report uses both `cg.md:351-362` (RHS §) and `cg.md:352-362` (audit §) for the same content; the harvester upstream uses `:352-362` consistently. Both ranges enclose Claim 2; not a citation error, just a range-boundary drift.

**surface-or-evidence (pass).** The report is a new-theme proposal (creates `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`) — substantive surface, not pure rotation-claim. The proposal cites both the L_{n+1} source (the just-landed L4 `krylov-step` harvester output at `book/src/L4/krylov-step.md` + the harvester CYCLE.md) and the L_n sink (the cycle-005 firm `book/src/L2/krylov-step.md`). Per the report-under-review's intermediate-cycle context, the forward reference to the not-yet-integrated L4 entry is acceptable per the special-check note. The rewrite shape (four-part LHS→RHS) is the surface.

**rotation-quality (pass).** The four-part wrapper-dissolution rewrite — (a) `StateT SimState` → explicit s arg, (b) typed records → positional tuples, (c) `readonly` typing → documented invariant, (d) Form-A/B → carry-threading — is a genuine rotation: it removes structural machinery at L_{n+1} (typed records + monadic effect + typing constraint + presentation variant) without altering the body's dataflow. The four pieces are internally consistent: the LHS signatures match the harvester output's Form A and Form B signatures verbatim; the RHS positional shapes are the standard de-monadised forms; the `modify (\s -> s {it = s.it + 1})` → `s' = s {it = s.it + 1}` reduction is the textbook StateT-Identity desugaring (correctly identified as `reduction-chain` in the Justification kind section). The report correctly frames the rotation direction: L4 (more typed/wrapped) lowers to L3 (less typed, value-threaded) — this is dissolution, which is a valid lowering-direction rotation under the methodology's "rotation is between forms across layers" framing (not the "L_{n+1} should be more abstract" criterion, which applies in the lifting direction).

**variant-axis-coverage (pass).** The variant-axis inventory is inherited unchanged from L2 (six axes), and the report explicitly handles the axis most relevant to this lowering (Form A vs Form B, axis #4) via both LHS and RHS treatment plus the carry-threading collapse. Other axes are explicitly scoped out (orthog-variant obstruction noted as belonging below the `krylov-step` body inside `op.orthog`, not introduced by this theme; in-place vs out-of-place noted as below-L4-level). The "What this lowering does NOT cover" subsection is the explicit scope-out. No hidden branches.

**cross-reference-integrity (pass).** All concept-page references resolve: `state-stratification.md`, `solve-monad.md`, `first-iteration-unrolling.md`, `derived-view-hoisting.md`, `convergence-test.md`, `sequential-obstruction.md`, `counter-update.md` all exist under `book/src/concepts/`. The L2 entry `book/src/L2/krylov-step.md` exists. The L4 entry `book/src/L4/krylov-step.md` is forward-referenced and will land in the same cycle (per special-check guidance, acceptable). The proposed file naming convention `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` matches the L4-L3 directory's existing chapter convention (currently only `index.md` exists; this is the first theme entry). Open-question slug `krylov-step-l3-identity-in-form-audit` resolves at line 974 of `scaffolding/open-questions.md`.

**edge-label-fidelity (pass).** The proposal carries the L4→L3 edge label consistently throughout (title, slug `krylov-step-typed-wrapper-dissolution`, §"L4 form (LHS)" / §"L3 form (RHS)", proposed file location `book/src/L4-L3/`). All prose discusses that edge. Where the report mentions the orthogonal L3>L2 edge or the L2>L3 cycle-002 assertion, it labels them explicitly and distinguishes them from this dispatch's L4>L3 scope. No edge-label-prose mismatch.

**plan-kind-consistency (pass).** Declared status is `rough-in` (in the proposed theme file's Status section); declared scope is "L4>L3 theme sketch — krylov-step typed-wrapper dissolution" (frontmatter). The content shape matches: a new theme with LHS/RHS/applicability/justification/audit + two speculative L4 operators marked `rough-in`. The audit-verdict embedded inside the theme is a secondary audit task that the planner explicitly queued for this dispatch (per planner caveat 2) — acceptable cohabitation with the primary theme-sketch task. No misclassification.

**skill-uptake-survey (warning).** The report performs a substantive rotation proposal (the wrapper-dissolution rewrite) and a citation-grounded audit (the cycle-002 identity-in-form re-verification). Multiple existing skills are relevant: `skills/propose-rotation/`, `skills/verify-rotation-citation/`, `skills/verify-citation-range/`. None are invoked or referenced by the report. This is a pure-presence telemetry signal, not a blocking finding — the report's work appears to follow rotation-proposal discipline by hand without naming the skill. Surfaces as warning so the meta-phase can decide whether the skill-discovery channel is functioning for abstractor invocations.

### Issues found

1. **Audit-verdict wording inconsistency** (severity: low). The report uses three different terms for the audit disposition: "confirmed-and-refined" (§"Audit of cycle-002 identity-in-form claim", §"Open question disposition"), "closed-with-refinement" (§"Open questions / caveats" item 1), and "Audit refinement on the original assertion" (heading inside the audit section). The planner-special-check asks the resolution be "confirmed-with-refinement" (not flatly "confirmed"). The report's "confirmed-and-refined" satisfies the not-flat criterion but is a third unique phrasing. Recommend unifying on one phrase across all four occurrences for cleaner integrator handling. Location: lines ~226-230, ~291 of CYCLE.md.

2. **Citation range drift on cg.md** (severity: low). The report cites `cg.md:351-362` in §"L3 form (RHS)" (line 110 of CYCLE.md, "MGS carries sequential-obstruction (inherited from arnoldi_step.md:194-213, not introduced by this lowering)" — wait, this cite is actually arnoldi_step.md; let me re-locate). Re-located: `cg.md:351-362` appears in §"Applicability conditions" condition 3 ("per `cg.md:351-362`, `arnoldi_step.md:185-188`"); `cg.md:352-362` appears in the §"Context" subsection of the theme content ("per the combinator-miner cycle-002 assertion (`cg.md:341-362`, `arnoldi_step.md:178-213`)"); the audit section also varies. Different range-boundaries for the same evidence. Recommend canonicalising to `cg.md:351-362` (the range that fully contains Claim 2 — Claim 2 begins at line 351 not 352). Location: CYCLE.md lines 65, 110, 154, 167, 219 (various ranges).

3. **`iterate_while_L3` rendering loses trajectory accumulation** (severity: low–medium). The "What the L3 form for `iterate_while` looks like" subsection (lines 203-208 of CYCLE.md) renders the L3 lowering of `iterate_while` as `step (carry, sim) -> (carry', sim', readout, continue)` returning a single readout when continue=false. But the L4 `iterate_while` signature given earlier in the same report (lines 176-185) is `Step -> carry -> Solve Trajectory` with `Trajectory = [readout]` — i.e., the L4 form accumulates readouts across iterations subject to demand-pruning. The L3 tail-recursive form should also accumulate (or expose a demand-pruning-equivalent), not return only the final iteration's readout. The rendered L3 form drops the trajectory aspect, which is an actual semantic change in the rotation rather than a wrapper dissolution. Either the L3 rendering needs the trajectory accumulator pass-through, or the rotation discussion needs to acknowledge "demand-pruning collapses to single-readout when no consumer reads the trajectory" as an additional reduction step. As written the rotation is locally inconsistent. Location: CYCLE.md lines 199-210.

4. **L4-vs-L3 abstraction-direction prose** (severity: low). The methodology's rotation-quality criterion as stated in the critic checklist favours L_{n+1} being "strictly more compact / more abstract / more equational than the L_n form". The report's L4 form (typed records, monad, readonly typing, Form A/B distinction) is more typed and more abstract than the L3 value-threaded form, which is consistent with the lowering direction (L4 = more abstract, L3 = less abstract). The report's framing as "dissolution" is accurate. No fix needed, but the report could note explicitly that this dissolution is the lowering direction's correct rotation shape (preempting any reader who reads the checklist criterion and sees the L4 form as "more elaborate"). Location: CYCLE.md §"Justification kind" (lines 161-167).

5. **No skill invocation** (severity: telemetry-only). The relevant skills `propose-rotation`, `verify-rotation-citation`, `verify-citation-range` exist and apply directly to this dispatch's work. None are named or invoked by the report. Surface to meta-phase / scaffolding/skill-candidates.md if a pattern across cycle-006 reports. Not blocking; the work was done correctly by hand. Location: report-wide.

6. **Note on integration-order caveat (item 2)** (severity: informational, no action). The report's caveat 2 correctly flags the L4 dep-map dependency on `L4/krylov-step` landing before this report's rough-in `iterate_while` rows; this is routed to the integrator-per-report ordering. Critic confirms: per cycle-planner CYCLE.md §"Sequencing schedule", wave-1 contains the L4 harvester dispatch and wave-2 is this report — the dispatch ordering is correct. The flag in the report is a defensive note for the integrator-per-report serial-ordering, not an actual problem. Mentioned here so the repairer can disposition cleanly.

## Repair

### Fixes attempted

1. **Finding**: Audit-verdict wording inconsistency (three phrasings: "confirmed-and-refined", "closed-with-refinement", "Audit refinement on the original assertion").
   - **Decision**: repaired
   - **Action**: Canonicalized to "confirmed-with-refinement" (the phrasing requested by the planner-special-check) across all four occurrences in CYCLE.md:
     - Line 226: heading "Audit refinement on the original assertion" → "Audit verdict — confirmed-with-refinement"
     - Line 230: "confirmed-and-refined" → "confirmed-with-refinement"
     - Line 291 (caveat 1): two occurrences ("confirmed at L3>L2..." + "closed-with-refinement") consolidated to single "confirmed-with-refinement" phrasing
     - Line 295 (caveat 3): "closed-with-refinement" → "marked confirmed-with-refinement" (cross-reference to caveat 1)

2. **Finding**: `cg.md` citation range drift (`:351-362` vs `:352-362`).
   - **Decision**: repaired
   - **Action**: Verified against source by reading `book/src/spec/slices/cg.md:340-365`. Claim 2 begins at line 351 with `### Claim 2: step body lifts as identity`; the "identity in form" verbatim text is at line 360; the range that fully contains Claim 2 (header included) is `:351-362`. The lone `:352-362` occurrence at CYCLE.md line 214 (inside the paraphrased open-question text) was canonicalized to `:351-362` with a parenthetical note acknowledging the open-questions ledger's `:352-362` framing for traceability. Other `:351-362` and `:341-362` and `:341-349` ranges in CYCLE.md were left intact: each refers to the appropriate sub-range (Claim 2 body alone, both claims combined, or Claim 1 alone, respectively).

3. **Finding**: `iterate_while_L3` rendering drops trajectory accumulation (locally inconsistent rotation).
   - **Decision**: unrepairable
   - **Rationale**: Resolution requires either (a) re-rendering the L3 form with explicit `trajectory` accumulator threading, or (b) authoring an explicit demand-pruning step that justifies the collapse to a single readout. Both are substantive rotation decisions — choosing the L3 semantics of a (still rough-in) L4 loop combinator — which exceeds repair authority (mechanical fixes only; not substantive content authoring). The abstractor's role spec emits rough-in; substantive rotation gaps belong to harvester or lowering-verifier scope. **Action taken in lieu**: appended a new Open question / caveat (item 8) to CYCLE.md surfacing the inconsistency explicitly, deferring to cycle-007's lowering-verifier follow-up (already named in §Status) or to the cycle-007 harvester on the L4 loop-combinator family (caveat 4). Noted that the primary content of this dispatch — the four-part wrapper-dissolution theme for `krylov-step` itself — is unaffected; this is a sub-issue on the speculative L4 loop combinator's L3 shape, not on the `krylov-step` body's rotation.

4. **Finding**: L4-vs-L3 abstraction-direction prose could be made explicit to preempt reader confusion.
   - **Decision**: repaired
   - **Action**: Added a one-paragraph "Abstraction-direction note" at the top of §"Justification kind" in CYCLE.md (CYCLE.md ~line 163), explaining that L4 is the higher-abstraction layer (typed records, monad, readonly typing, Form A/B), L3 is the lower-abstraction layer (positional values, documented invariants), and the rotation direction L4 → L3 is the correct lowering direction under the methodology's rotation-quality criterion. Frames the L4 elaboration as *abstraction* (typing buys mechanical-checkability) rather than accidental complexity.

5. **Finding**: No skill invocation (telemetry only).
   - **Decision**: repaired
   - **Action**: Added a "Skills applicable to this dispatch" subsection to §"Supporting evidence" in CYCLE.md, naming the three relevant skills (`propose-rotation`, `verify-rotation-citation`, `verify-citation-range`) and acknowledging they were followed by hand without explicit invocation. Provides the skill-uptake telemetry signal the critic flagged as warning.

6. **Finding**: Integration-order caveat (item 2) — informational, no action requested.
   - **Decision**: not-needed
   - **Rationale**: Pure informational signal. The dispatch ordering is already correct per the cycle-planner's wave-1/wave-2 sequencing schedule (harvester before abstractor), and the integrator-per-report serial-dispatch discipline naturally honors the staging order. No action required; left as-is in CYCLE.md caveat 2.

### Unrepairable findings

- **Finding 3 (`iterate_while_L3` trajectory accumulation)**: deferred to cycle-007. The new CYCLE.md caveat 8 surfaces the inconsistency for the cycle-007 lowering-verifier dispatch (already named in §Status) or the cycle-007 harvester on the L4 loop-combinator family (named in caveat 4). Follow-up routing: `lowering-verifier` (preferred — already named in §Status as the cycle-007 follow-up) or `harvester` (secondary path, would resolve as part of formalising `iterate_while`'s firm L4 signature).

## Suggested resolution

`ready` for integration. The primary content — the four-part L4>L3 wrapper-dissolution theme for `krylov-step`, the audit confirming-with-refinement of the cycle-002 identity-in-form claim, the two rough-in L4 loop-combinator operators, and the no-L3-row disposition — is internally consistent and applies cleanly.

**Notes for the integrator**:

- The cycle-005 open question `krylov-step-l3-identity-in-form-audit` should be marked **confirmed-with-refinement** (not closed; per the methodology a refined assertion typically stays in the ledger with the refinement annotated). The wording is now canonical across CYCLE.md.
- A new caveat 8 has been added to CYCLE.md noting the `iterate_while_L3` rendering's trajectory-accumulation gap. This is a deferred substantive issue routed to cycle-007 (lowering-verifier or harvester). It does **not** block integration of the L4>L3 `krylov-step` theme itself, and it does **not** require an open-question filing (it sits inside the rough-in `iterate_while` L4 operator's scope, which the harvester will formalise).
- The wave-1 harvester report (`reports/2026-05-27T080944Z-harvester-krylov-step-L4/`) must integrate before this report so the L4 dep-map has the firm `krylov-step` row when this report's `iterate_while` rough-in rows are appended (per CYCLE.md caveat 2, already correctly sequenced by the cycle-planner).
