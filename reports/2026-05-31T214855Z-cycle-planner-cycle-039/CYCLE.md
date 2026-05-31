---
agent: cycle-planner
invoked_at: 2026-05-31T214855Z
scope: cycle-039 dispatch plan (THIRD/FINAL primary cycle of meta-batch-11; batch-11 meta-phase fires AFTER this cycle's integrator-finalize)
status: pending
---

# Cycle 039 dispatch plan

**Batch position:** THIRD and FINAL primary cycle of meta-batch-11 (cycles 037/038/039). The batch-11 meta-phase fires AFTER this cycle's `integrator-finalize`. **Process stakes:** `cycle-planner-stale-priorities-line-recruitment` is `escalating` (recurrence 6). c037 + c038 were BOTH clean opus-planner cycles (no stale picks; the orchestrator overrode nothing). A clean c039 closes the friction **3-of-3 across batch-11** for the batch-11 meta-phase to mark it structurally addressed by the haiku→opus escalation. This plan therefore runs the full `verify-dispatch-scope-not-already-discharged` four-step + step-5 (STOP-PROPOSING) + step-6 (audit-first framing) procedure on every dispatch, with **pasted inline command evidence** in §Deliverable-presence verification below.

## Goals selected this cycle

Discharge the three concrete carry-forwards the cycle-038 finalize handed off, all verified-open and all non-overlapping at the operational level:
1. **CLOSE the c036 (A) L3-backfill cohort 6-of-6** by landing the SOLE remaining (A) candidate, `normalize` at L3 (fused `nrm2 + scal`, identity-in-form). This shifts the L3 follow-frontier off the quick-backfill tier onto the (B) substantive cohort.
2. **ENACT** the floquet AddMult-aliasing re-anchor (OQ `floquet-corrector-addmult-aliasing-applicability-audit`, TRIGGER FIRED c038) — the c038 lowering-verifier UNBLOCKED + named the precise edits; this dispatch APPLIES them and widens the single `partially-supports` row to `supports`.
3. **FOLD** the fourth obstruction profile (`obstruction-carrying-by-reference`, instantiated by the c038 `divfree-projector` L3 landing) into the `L3/index.md` §Semantics-overlay sequential-obstruction taxonomy.

This is a fan-out-balanced batch-closing cycle: D1 closes a cohort end-to-end (Medium fan-out — completes the diagonal-preconditioner-apply + divfree chains at L3 and unblocks the (B)-tier follow-frontier); D2 firms a per-line citation surface on a firm L1>L0 theme (low/audit fan-out, but TRIGGER-FIRED carry-forward — discharging it clears an OPEN-OQ debt); D3 is a navigation/taxonomy hygiene fold (low fan-out, but discharges a co-scheduled layer-intro-author OQ + consolidates the c037/c038 parallel-blind firm-count tally to one correct state).

## Deliverable-presence verification

Mandatory pre-dispatch check (batch-10 meta-phase PASTE-INLINE-EVIDENCE strengthening). Literal command output per dispatch below. NONE of the three scopes is on the STOP-PROPOSING NEGATIVE LIST (`lu_solve`, `back_solve`, `ls-update-column`, 4 NLEPS atoms). All three are concrete c038-finalize carry-forwards, but each is verified by artifact-presence, not merely by the carry-forward claim.

### D1 — `normalize` L3 backfill — ALL FOUR CHECKS PASS → genuinely OPEN

**Check 1 (file existence — must be ABSENT):**
```
$ ls -la book/src/L3/normalize.md
ls: cannot access 'book/src/L3/normalize.md': No such file or directory
exit=2
```
L3 dir confirms `normalize.md` absent while the 17 sibling L3 chapters (incl. the c037/c038-landed `assemble-diagonal`/`jacobi-smoother`/`reciprocal`/`elementwise_product`/`divfree-projector`) are present.

**Check 2 (maturity — file absent, so no on-disk maturity to undercut; deps firm for live-linking):** L1 home + both L3 leaf deps firm on disk:
```
$ ls -la book/src/L1/normalize.md
-rw-rw-r-- ... 19789 May 29 17:34 book/src/L1/normalize.md     (firm L1 home)
$ ls -la book/src/L3/nrm2.md book/src/L3/scal.md
-rw-rw-r-- ... 20430 ... book/src/L3/nrm2.md                    (firm L3 leaf — live-link-eligible)
-rw-rw-r-- ... 24739 ... book/src/L3/scal.md                   (firm L3 leaf — live-link-eligible)
```

**Check 3 (OQ-ledger RESOLVED-grep — the only `normalize` closures are L1/L1>L0, NOT the L3 backfill):**
```
$ grep -in 'normalize.*RESOLVED\|normalize.*CLOSED\|normalize.*l3' scaffolding/open-questions.md
355: normalize-as-fused-l1-primitive ... resolved cycle-026   (L1, not L3)
364: normalize-mutation-rotation ... resolved cycle-027        (L1>L0, not L3)
392: normalize-mutation-rotation-lowering-verifier-audit ... RESOLVED c028  (L1>L0 verified_against, not L3)
406/407/412: normalize_B / verified-against-row stale ... RESOLVED c029/c030 (L1>L0, not L3)
880: l3-cohort-growth-audit-c036-verdict ... (A) list INCLUDES normalize as OPEN backfill
```
No `normalize` **L3** RESOLVED/CLOSED entry. The `l3-cohort-growth-audit-c036-verdict` tracker (lines 880/938) explicitly carries `normalize` as the SOLE remaining (A) backfill, "held to cycle-039 per the c037/c038 cohort routing."

**Check 4 (structural-block):** NONE. `normalize` is firm at L1, the L3 rotation is identity-in-form per the c036 D2 audit verdict, and both L3 leaf deps (`nrm2`/`scal`) are firm on disk for live-linking. No `rough-in (test-coverage-bounded)` / `partly-constructive` / `partial-obstruction` / `opaque-library` gate applies — this is a layer-coherence identity backfill (CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels**). **Step 6 (audit-first framing):** NOT needed — `normalize` is a fused BLAS-1 composition with a settled identity-in-form verdict from the c036 D2 audit, not an operator-to-data primitive or a cohort-boundary candidate. Reflexive harvest is correct.

### D2 — floquet AddMult-aliasing re-anchor ENACT — CHECKS CONFIRM OPEN WORK REMAINS

**Check 1 (theme file + Status):**
```
$ ls -la book/src/L1-L0/floquet-correction-mutation-rotation.md
-rw-rw-r-- ... 38821 May 31 14:33 ...   exit=0
$ grep -in '^## Status' book/src/L1-L0/floquet-correction-mutation-rotation.md
438:## Status
```
Theme firm on disk (the audit appended a `verified_against:` block c038; body firm).

**Check 2 (the single `partially-supports` row is STILL present — i.e. NOT yet widened; this is the work to enact):**
```
$ grep -c 'verified_against:' book/src/L1-L0/floquet-correction-mutation-rotation.md
1
$ grep -in 'partially.supports\|partially_supports' book/src/L1-L0/floquet-correction-mutation-rotation.md
552:    verdict: partially-supports
```
Exactly ONE `partially-supports` row (line 552) remains — the enact target. If this had already been widened to `supports` the dispatch would be a no-op; it has not.

**Check 3 (OQ still OPEN / TRIGGER-FIRED, not RESOLVED):**
```
$ grep -in 'floquet-corrector-addmult-aliasing' scaffolding/open-questions.md
899: ... opened cycle-036 D1 ... *Trigger:* a lowering-verifier dispatch ... (OPEN)
948: ... TRIGGER FIRED (cycle-038 D4); SHARPENED, NOT CLOSED ... precise carry-forward edits (OPEN)
```
OQ is OPEN with the trigger fired and the exact edits recorded — never RESOLVED/CLOSED.

**Check 4 (structural-block):** NONE. The c038 audit already localized and confirmed the true mechanism on-disk; this is a surgical citation re-anchor + a single-row verdict update, not a blocked promotion. **Step 6 (audit-first framing):** the audit already happened (c038 D4); this dispatch is the ENACT half. Routing `lowering-verifier` with explicit ENACT authority is the natural fit (the same agent class that authored the audit; the edits are within its `verified_against:`-row + citation-anchor authority).

**Pre-localized known-heavy anchors (embedded so the producer authors rather than re-localizing — `iterative.cpp` running region is on the dispatch-resilience watch-list):** I read the exact on-disk lines via codemap+disk:
- `palace/linalg/iterative.cpp:360` = `CgSolver<OperType>::Mult(const VecType &b, VecType &x)` signature; the `initial_guess == false` else-branch body is **`:383-386`** (`383:` `else {`, **`384:` `r = b;`**, **`385:` `x = 0.0;`**, `386:` `}`) — i.e. `b` is copied into workspace `r` BEFORE the aliased `x` is zeroed, which is the reads-`x`-once-then-writes-`y`-equivalent mechanism the AddMult fusion relies on. (The signals slug cited `:361`/`:384-385`; on-disk `Mult` is at `:360` and the two assignment lines are `:384`/`:385` — the producer cites the on-disk bounds.)
- `palace/linalg/floquetcorrection.cpp:61` = `pcg->SetInitialGuess(0);` (confirmed exactly on disk) — the gate establishing `initial_guess == false` for the inner CG.
- The thin-wrapper site to re-anchor AWAY from: `palace/linalg/ksp.cpp:297` (`BaseKspSolver<OperType>::Mult`, a delegating wrapper that does NOT itself exhibit the mechanism).

### D3 — layer-intro-author fourth-obstruction-profile fold — ALL CHECKS PASS → genuinely OPEN

**Check 1 (L3/index.md exists + the §Semantics-overlay taxonomy currently names only THREE shapes):**
```
$ ls -la book/src/L3/index.md            -> -rw-rw-r-- ... 38948 ... exit=0
$ grep -in 'Sequential obstructions' book/src/L3/index.md
15: - **Sequential obstructions** — ... Three firm shapes coexist at L3: (a) ksp_solve ... (b) chebyshev ... (c) eigsolve ...
```
Line 15 enumerates exactly three firm shapes (a)/(b)/(c) — the fourth (`obstruction-carrying-by-reference`) is NOT in the taxonomy.

**Check 2 (the fourth-profile fold is PENDING, not done — explicit pending marker on disk):**
```
$ grep -in 'fourth\|carrying-by-reference\|taxonomy.note' book/src/L3/index.md
58: - **Fourth-obstruction-profile taxonomy note pending** (cycle-038 D3 flag ...) ... A layer-intro-author follow-up dispatch should fold this fourth profile into the §Semantics-overlay taxonomy.
```
Line 58 is a §Working-Notes "pending" flag — the work is queued, not done. (`divfree-projector`'s row at line 36 + the §Working-Notes c038 bullet at line 57 describe the profile narratively, but the §Semantics-overlay TAXONOMY at line 15 does not yet name it.)

**Check 3 (OQ OPEN, not RESOLVED):**
```
$ grep -in 'fourth-obstruction-profile' scaffolding/open-questions.md
940: l3-index-fourth-obstruction-profile-obstruction-carrying-by-reference (opened cycle-038) ... layer-intro-author follow-up ... NOT enacted ... *Trigger:* next layer-intro-author L3-index touch. (OPEN)
```

**Check 4 (structural-block):** NONE — this is layer-intro-author authoring within its `book/src/L3/index.md` write authority; the trigger ("next layer-intro-author L3-index touch") fires this cycle. **Step 6:** N/A (taxonomy fold, not an operator harvest).

**ALL THREE DISPATCHES VERIFIED GENUINELY OPEN.** No reframe needed (D1 reflexive-harvest is correct for a settled-identity BLAS-1 composition; the c036 audit already classified it (A)). No STOP-PROPOSING-list collision.

## Dispatches

1. **agent:** `harvester`
   **scope:** L3 operator: `normalize` — the firm L1 `normalize` (`book/src/L1/normalize.md`, fused `nrm2 + scal` returning `(Scalar, Tensor[N])`) backfilled at L3 as an identity-in-form whole-tensor operator chapter (`book/src/L3/normalize.md`, NEW). This is the SIXTH and FINAL (A) firm identity-in-form L3 backfill of the c036 D2 audit verdict (`book/src/L3/index.md:46`), CLOSING the (A) cohort 6-of-6. Template the now-firm L3 identity-row precedents: `reciprocal`/`elementwise_product`/`assemble-diagonal` (c037/c038) and the original `apply_linop`/`krylov-step` identity-row form. Because `normalize` is a fused `nrm2 + scal`, its L3 dependencies reference **firm-on-disk** L3 `nrm2`/`scal` — those are **live-link-eligible** (`[nrm2](./nrm2.md)` / `[scal](./scal.md)`), per `upgrade-plain-text-ref-to-live-link-when-target-on-disk`. Append ONE dep-map row to `book/src/L3/index.md` (after the BLAS-1 cohort rows) + ONE `SUMMARY.md` L3-Part entry. Carry any L1-home non-laws/partiality (e.g. the `‖x‖ = 0` degenerate case) forward as inherited representation-aware non-laws, NOT a status reduction. **Per the c037/c038 §Working-Notes parallel-blind-count lesson:** do NOT author an absolute firm-count bullet in §Working-Notes — append only your dep-map row + (optionally) a relative "+1 this dispatch (normalize, 15th firm L3, closes the c036 (A) cohort 6-of-6)" note; the absolute tally reconciliation is D3's / finalize's job.
   **deps:** none.
   **rationale:** The c038-finalize-named cycle-039 opener + the integrator-signals cycle-038 §Suggested-next-dispatches top item. Closes `l3-cohort-growth-audit-c036-verdict` (A)-portion end-to-end (6/6), shifting the L3 follow-frontier to the (B) substantive cohort. Medium fan-out: completes the diagonal-preconditioner-apply + Krylov-normalize chains at L3. Verified OPEN (file absent; L1 home + both leaf deps firm).

2. **agent:** `lowering-verifier` (ENACT authority — this dispatch APPLIES the edits the c038 D4 audit identified; it is NOT a fresh audit)
   **scope:** ENACT the floquet AddMult-aliasing re-anchor in `book/src/L1-L0/floquet-correction-mutation-rotation.md` (OQ `floquet-corrector-addmult-aliasing-applicability-audit`, TRIGGER FIRED c038). Two coordinated edits: **(i)** in the theme body — Sub-pattern B / Applicability-condition-2 prose (the AddMult buffer-economy aliasing-tolerance mechanism) — RE-ANCHOR the citation from the thin delegating wrapper `palace/linalg/ksp.cpp:297` (`BaseKspSolver<OperType>::Mult`, which does NOT itself exhibit the mechanism) to the TRUE mechanism site: `palace/linalg/iterative.cpp:360` (`CgSolver<OperType>::Mult`) else-branch body `:383-386` (`r = b;` at `:384`, `x = 0.0;` at `:385` — `b` copied into workspace `r` before the aliased `x` is zeroed), and NAME the `initial_guess == false` precondition established by `palace/linalg/floquetcorrection.cpp:61` `pcg->SetInitialGuess(0)`. **(ii)** in the `verified_against:` block — update the single `partially-supports` row (currently at line 552) to `verdict: supports`, with the `note:` re-pointed to the `iterative.cpp:383-386` + `floquetcorrection.cpp:61` anchors (per the `verified-against-note-no-leading-quote-of-either-kind` channel-format rule — note value's first non-whitespace char must NOT be `'` or `"`). Theme stays firm; this widens one audit row from `partially-supports`→`supports` and corrects one citation. **Pre-localized anchors are embedded above in §Deliverable-presence D2 — read those exact lines, do not re-enter a localization loop on the `iterative.cpp` running region (it is on the dispatch-resilience known-heavy watch-list).**
   **deps:** none.
   **rationale:** integrator-signals cycle-038 §Suggested-next-dispatches item 2 + the cycle-038 finalize §Next-cycle-priorities "ENACT the floquet AddMult-aliasing carry-forward." TRIGGER FIRED, edits precisely specified, the `partially-supports` row still present (verified). Discharges an OPEN-OQ debt and completes the c038 UNBLOCK→ENACT pair. Low/audit fan-out but a concrete carry-forward.

3. **agent:** `layer-intro-author`
   **scope:** `book/src/L3/index.md` §Semantics-overlay taxonomy fold — add the **fourth obstruction profile** (`obstruction-carrying-by-reference`) to the sequential-obstruction enumeration at line 15 (currently names only three firm shapes (a) `ksp_solve` outer-loop-renders / (b) `chebyshev` numerical-stability `partial-obstruction` / (c) `eigsolve` opaque-library `partial-obstruction`). Add shape **(d)**: a constructed-operator gate that **carries** a `sequential-obstruction` it neither authors nor erases, via a nested inner gate — instantiated by `divfree-projector` (c038, its inner `ksp_solve`); the MIDDLE of the L3 obstruction-profile spectrum, distinct from the obstruction-authoring gates (`ksp_solve`/`eigsolve` own their loops) and the obstruction-free leaf gates (`jacobi-smoother`/`apply_linop`/`reciprocal`/`elementwise_product`/`dot`/`scal`); cite the `nested-constructed-operator-gate` fidelity rule. Clear the line-58 "Fourth-obstruction-profile taxonomy note pending" §Working-Notes flag once folded. **ALSO** (co-scheduled, since this dispatch is already in §Working-Notes): reconcile the §Working-Notes firm-count tally to the single correct post-D1 state — **15 firm + 2 partial-obstruction**, c036 (A) cohort **6-of-6 closed** (none remaining) — superseding the c037/c038 parallel-blind count bullets and incorporating D1's `normalize` landing; and apply the standing c037 `l3-index-semantics-overlay-constructed-operator-gate-sub-family` overlay-refresh + the c038 `l3-index-working-notes-firm-count-refresh-*` flags if cleanly co-foldable. Survey on-disk `## Status` lines for the absolute firm count rather than trusting any single prior prose bullet (per the layer-intro-author "survey firmness from on-disk `## Status`" discipline bullet).
   **deps:** **1** (D1) — so the §Working-Notes tally this dispatch writes reflects `normalize` having landed (15 firm, 6/6 (A) closed). The §Semantics-overlay (d)-profile fold itself does not depend on D1, but co-folding the count tally does; sequencing after D1 avoids re-introducing the parallel-blind-count divergence the c037/c038 finalize had to reconcile.
   **rationale:** integrator-signals cycle-038 §Suggested-next-dispatches item 3 + finalize §Next-cycle-priorities "fold the fourth obstruction profile." Discharges OQ `l3-index-fourth-obstruction-profile-obstruction-carrying-by-reference` + consolidates the lingering parallel-blind firm-count tally to one authoritative state. Low fan-out (navigation/taxonomy hygiene), but it is the natural batch-closing tidy of the L3 cohort the batch built.

## Overlap analysis

Three dispatches, three pairs:

- **D1 (`normalize` L3) × D2 (floquet L1>L0 re-anchor):** DISJOINT write surfaces. D1 writes a NEW `book/src/L3/normalize.md` + appends a dep-map row to `book/src/L3/index.md` + a `SUMMARY.md` L3 entry. D2 edits only `book/src/L1-L0/floquet-correction-mutation-rotation.md` (body prose + one `verified_against:` row). No shared file, no shared operator name. **PARALLEL.**

- **D1 (`normalize` L3) × D3 (L3/index.md taxonomy fold):** BOTH touch `book/src/L3/index.md`, but at OPERATIONALLY DISTINCT regions: D1 APPENDS one dep-map row to the operator table (after the BLAS-1 cohort) + (per the parallel-blind-count lesson) authors NO absolute-count bullet; D3 edits the §Semantics-overlay prose (line 15) + the §Working-Notes tally/pending-flag (lines 57-58). The dep-map-table-row-append vs prose-section-edit are non-overlapping per the "append distinct rows to the same table = NOT overlapping" rule. The ONE genuine coupling is the §Working-Notes absolute firm-count tally — exactly the c037/c038 parallel-blind-count pattern the finalize had to reconcile. To AVOID re-introducing that divergence (rather than relying on finalize to reconcile a third time), I make D3 the SOLE author of the absolute tally and **sequence D3 after D1** so it writes the correct post-`normalize` count (15 firm, 6/6 (A) closed). This is a forward-reference/count-ownership ordering, not a hard same-region conflict. **SEQUENTIAL (D3 after D1).**

- **D2 (floquet L1>L0) × D3 (L3/index.md):** DISJOINT write surfaces (`L1-L0/floquet-correction-mutation-rotation.md` vs `L3/index.md`). No shared file or operator name. **PARALLEL.**

## Sequencing schedule

- **Wave 1 (parallel):** D1 (`normalize` L3 harvest) + D2 (floquet AddMult-aliasing ENACT). Disjoint surfaces; no forward-references between them.
- **Wave 2 (after D1's report lands):** D3 (L3/index.md fourth-obstruction-profile fold + firm-count tally reconciliation). D3 is sequenced after D1 only so its §Working-Notes absolute firm-count reflects `normalize` (15 firm, c036 (A) cohort 6/6 closed) — making D3 the single tally author and avoiding the parallel-blind-count divergence seen c037/c038. D2 may complete in either wave relative to D3 (no coupling).

Per-cycle pipeline reminder: this is THREE specialized dispatches → 3 critics → repairers as needed → `integrator-per-report` ×3 (serial) → ONE `integrator-finalize` (rebuild book + commit + push + housekeeping). The waves above order the SPECIALIZED dispatches; `integrator-finalize` runs once at cycle end (it does NOT rebuild between waves). The §Working-Notes firm-count reconciliation is D3's job (with finalize as the safety-net single-reconciler if any residual divergence remains), NOT a per-wave rebuild.

## Open questions / caveats

- **Batch-closing process note (for the batch-11 meta-phase, fires after this finalize):** c037 + c038 were both clean opus-planner cycles; this c039 plan is verified-clean (all 3 dispatches genuinely open, pasted inline evidence, no STOP-PROPOSING collision, no reframe needed). If c039 lands clean, that is **3-of-3 across batch-11** and the batch-11 meta-phase should be positioned to mark `cycle-planner-stale-priorities-line-recruitment` (currently `escalating`, recurrence 6) as structurally addressed by the haiku→opus escalation — the held ASK `cycle-planner-haiku-opus-swap-recurrence-7-trigger-vs-defer-with-runway` is effectively answered (the swap already happened as part of the 2026-05-31 blanket Opus-4.8 upgrade; batch-11 is its confirmation window).
- **Parallel-blind firm-count pattern (recurrence c037/c038, low-severity, candidate methodology note):** the c038 integrator-signals flagged that ≥2 parallel L3-backfill dispatches each authoring a §Working-Notes absolute-count bullet self-report inconsistent counts (finalize reconciles once). This cycle has only ONE count-bearing L3 landing (D1 `normalize`) and I have explicitly assigned absolute-tally authorship to a SINGLE dispatch (D3, sequenced after D1) + instructed D1 to author only a relative "+1" note — so the pattern should NOT recur this cycle. **Surfaced for the batch-11 meta-phase as a candidate producer-side convention** (the c038 signals' proposed mitigation: "producers append only a dep-map row + relative '+1 this dispatch' note; the absolute tally is computed once by finalize/layer-intro-author"). The friction-ledger entry for this is not yet written (it is a 2-cycle soft datapoint); per the cadence note, I flag it here so the batch-11 meta-phase can decide whether to codify the convention rather than leaving it as a recurring finalize-reconciliation responsibility.
- **D2 routing judgment (`lowering-verifier` ENACT vs `abstractor`/`lifter`):** I routed `lowering-verifier` with explicit ENACT authority because the SAME agent class authored the c038 audit that identified these exact edits, and the work is within its `verified_against:`-row + citation-anchor surface (re-anchor one citation + widen one row `partially-supports`→`supports`). The scope explicitly states this dispatch ENACTS the widening (unlike the c038 audit which only routed it). If the orchestrator judges the body-prose citation re-anchor to be authoring-class beyond lowering-verifier authority, `lifter` (re-anchor to firmed-up evidence) is the clean alternative — but the edit is surgical (one citation swap + one verdict update, both already localized on-disk), so lowering-verifier ENACT is the tighter fit.
- **No `priorities.md` append needed this cycle.** All three dispatches discharge existing tracked items (the `l3-backfill-cohort-from-c036-audit` (A)-tail + two c038-opened OQs). On D1 landing, the `l3-cohort-growth-audit-c036-verdict` (A)-portion CLOSES 6/6 and the L3 follow-frontier becomes the (B) substantive cohort (`orthogonalize` third-partial-obstruction / `chebyshev-smoother`-subsumption-check / `apply_nonlinear_pencil`-fold) — already present in the Backlog Medium tier (`l3-substantive-cohort-from-c036-audit`); no re-rank required. I did NOT append candidates because the plan's active head + Backlog already hold the next-frontier work; the integrator-finalize will mark the (A)-tail item landed.
