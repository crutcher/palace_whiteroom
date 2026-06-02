---
verifies: ../REPORT.md
critiqued_at: 2026-06-02T013500Z
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
repaired_at: 2026-06-02T015200Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: unrepairable
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: needs-revision
follow_up_agent: lifter
---

# META: verification of cycle-055 D7 consolidated-count owner (L4/L4-L3/L1 index tallies + frontier narrative)

## Critique

### Checks run

**citation-validity — pass.** D7 is primarily an arithmetic + narrative-reconciliation report; its load-bearing "claims" are the COUNTS, which I verified directly against on-disk reality (see Issues for the per-count audit). The few L0 source citations carried into the L1 FE-sub-spine narrative (the `eliminate_*` evidence) were checked mechanically: `python3 tools/citecheck/citecheck.py --scan CYCLE.md --quiet` returns `9 ok, 0 failing`. I anchored the load-bearing pinpoints: `palace/linalg/rap.cpp:69-73 --anchor 'Mult'` resolves (anchor at 69,72), `palace/models/laplaceoperator.cpp:216-217 --anchor 'SetEssentialTrueDofs'` resolves (anchor at 217), `rap.cpp:36-47`, `rap.cpp:141-143`, `laplaceoperator.cpp:252`, `drivensolver.cpp:176-180` all in-bounds. The `:216-217` anchor confirmation independently validates D7's claim that the sibling `fe_assemble.md:147` `215-217` citation is stale drift (the construction is at :216, the `SetEssentialTrueDofs` call at :217). Note: the report's `verified_against` frontmatter sub-check is N/A (D7 emits no such block). No quoted-scalar YAML round-trip concern.

**surface-or-evidence — pass.** Not a refinement-of-an-existing-operator report in the usual sense; D7 modifies index narrative + count surface and carries the evidence (the on-disk-status reads + the D1–D6 report frontmatter cross-references) inline in §Supporting evidence. Every count edit is paired with its on-disk justification. No bare rotation_claim.

**rotation-quality — pass (not applicable).** D7 asserts no algebraic/structural rotation; it is a count/narrative reconciliation. The one rotation-adjacent statement (the L4-L3 tally prose noting `solve-family-map-dissolution` is "substantive, not identity-in-named-terms") is a relayed characterization of D2's theme, not a rotation claim D7 originates. Marked pass as inapplicable to the count-owner report kind.

**variant-axis-coverage — pass.** No new operator/theme with variant axes is authored here. The FE-sub-spine narrative correctly relays the `eliminate_essential_bc` diagonal-policy axis (`DIAG_ONE`/`DIAG_ZERO`) and the `solve_family` fixed-operator-vs-per-element axis (2-of-5 pipelines, driven superset explicitly scoped out as batch-17-gated) — both scoped, neither a hidden branch.

**cross-reference-integrity — pass (with a flagged dependency-ordering note, see Issues #4).** I verified every count against on-disk reality and every `old`-anchor resolves to a real on-disk narrative region: L4 edit#1 anchor `**Firm at L4 (6 + 4 outer-driver)**` (L4/index.md:32), edit#2 anchor `**Rough-in at L4 (0)**` (:47), edit#3 anchor `**Queued at L4 (0 — substantially complete)**` (:56); L1 edit anchors `**Rough-in (FE-assembly sub-spine — THREAD-OPENER cycle-053)**` (:70) and `**Firm (26)**` (:31) — all present and unique on disk. The L4-L3 edit#2 anchor (D2's seeded bullet) does NOT pre-exist on disk by design (it is seeded by D2 this cycle); D7's `[old]` text matches D2's proposed bullet text verbatim (D2 report line 241), so the anchor resolves IF D2 is applied before D7. This is a build-readiness check, not a firm-body-inside-fence concern (no `firm` chapter body is authored here — these are index edits). Fence enumeration: 12 fence lines = 6 balanced `edit:` blocks, no nested fences, even parity.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is mis-attached. The L4-L3 tally prose discusses the L4>L3 edge (`solve_family` → L3 family-sweep) and the stratified composition (4-shell hop) correctly; the L1 narrative discusses L1 operators + their L1>L0 anchors with correct direction.

**plan-kind-consistency — pass.** The report declares itself a consolidated-count / narrative-reconciliation dispatch (layer-intro-author kind). Content matches: it touches only index tallies, cohort headers, and frontier prose, deferring all operator/theme authoring to D1–D6. No mis-classification.

**skill-uptake-survey — warning.** D7 performs exactly the work the `proposed-changes-fence-encloses-full-body-guard` is adjacent to (fence-bearing index edits) and an on-disk status-survey that the `verify-citation-range` skill's count-audit posture covers, but references no skill invocation. More pointedly: D7's core method here — "survey the consolidated count from the on-disk `## Status`, not the cycle record / planner projection" — is a recurring, crystallize-able procedure (it caught the 6→3 L4-L3 planner-projection error and the prose/table firmness divergence precisely BECAUSE it read on-disk). No `count-owner-survey-from-on-disk-status` skill exists. This is telemetry, not blocking; see the skill-candidate note appended below.

### Issues found

**Issue #1 — L4-L3 firm count: PLANNER PROJECTION WAS WRONG; D7's on-disk correction (3→4) is verified correct. (informational / no defect in D7.)** The dispatch projected "6→7 firm". I counted the on-disk `L4-L3/index.md` theme-list table: exactly 3 firm rows (`iterate-while-dissolution`, `iterate-while-with-prev-dissolution`, `ksp-solve-driver-dissolution`) and 3 rough-in (`krylov-step-typed-wrapper-dissolution`, `gmres-inner-loop-iterate-while-migration`, `fgmres-inner-loop-iterate-while-migration`). D7's correction to 3→4 (with D2's `solve-family-map-dissolution` landing firm) is on-disk-truthful. No defect — this is D7 doing its job correctly. Severity: none (positive verification).

**Issue #2 — L4/index.md prose↔L4-L3/index.md table firmness divergence is REAL and load-bearing. (warning; D7 correctly surfaced as OQ; needs integrator/finalize follow-up, NOT a D7 fix.)** Verified: `L4/index.md:52-53` labels both `gmres-inner-loop-iterate-while-migration` AND `fgmres-inner-loop-iterate-while-migration` as *(firm; ...)* in the L4 Part-overview prose, while the authoritative `L4-L3/index.md:16-17` table carries BOTH as `rough-in`. D7 computed its tally from the table (per count-owner discipline) and flagged the mismatch as new OQ `l4-l3-fgmres-firmness-prose-vs-table-divergence`. This is a genuine cross-surface consistency defect in the EXISTING artifact (not introduced by D7); it warrants a lifter/cross-layer-cross-cutter reconciliation pass and a finalize-logged OQ. Location: report §"Open questions / caveats" first bullet; underlying defect at `book/src/L4/index.md:52-53` vs `book/src/L4-L3/index.md:16-17`. Severity: warning (correctly handled by D7; flagged for downstream).

**Issue #3 — fe_assemble.md citation residual: the DRIFT is real but D7 OVER-COUNTS the occurrences. (low severity; in a flagged-out-of-scope OQ note, not in D7's count edits.)** D7's OQ `fe-assemble-laplaceoperator-citation-drift-215-vs-216` states the stale `laplaceoperator.cpp:215-217` appears "in 2 places (§laws ~line 147, §Evidence ~line 257)". On-disk, `book/src/L1/fe_assemble.md` carries the `215-217` string in only ONE place (line 147); the §Evidence reference at line 253 cites the broader `184-223` (correct, in-bounds). So the drift itself is real (citecheck confirms the construction/`SetEssentialTrueDofs` sites are at :216/:217, not :215), but it is a single-site residual, not two. This mischaracterization sits inside an OQ note that D7 explicitly scopes OUT of its own count-owner work (for a future lifter), so it does not affect any applied edit. Location: report §"Open questions / caveats" fourth bullet. Severity: low (cosmetic over-count in a deferred-OQ note; the residual flag itself is valid and useful).

**Issue #4 — L4-L3 edit#2 has a hard cross-dispatch application-ordering dependency (D2-before-D7). (informational; D7 documented it and provided a fallback.)** The edit#2 `[old]` anchor is D2's `solve-family-map-dissolution` §Vocabulary-cohort bullet, which does not exist on disk pre-cycle (D2 seeds it this cycle). D7's `[old]` matches D2's proposed-bullet text verbatim, so the anchor resolves ONLY if the integrator applies D2 before D7. D7 is wave-3 (applied after D1–D6), so ordering should hold, and D7 explicitly documented the fallback ("integrate this as an append to the `## Vocabulary-cohort` section" if the exact-text anchor fails). This is a correctly-handled coordination risk, not a defect — but the integrator-per-report should be aware the edit#2 anchor is on D2-seeded text, and D2's section header is `## Vocabulary-cohort` (with hyphen), matching D7's prose reference. Location: report §"Proposed changes" #2 preamble. Severity: informational.

**Issue #5 — L1 firm arithmetic verified correct; the "26 main + 3 FE = 29 grand total" decomposition is on-disk-accurate. (informational / positive verification.)** On disk: 27 L1 files carry `## Status` → ``firm`` (counting fe_assemble); the `**Firm (26)**` header (L1/index.md:31) enumerates exactly 26 main-cohort bullets, and `fe_assemble` lives in its own FE-sub-spine subsection (NOT among the 26). So 26 main + `fe_assemble` = 27 firm pre-cycle, matching D7. The +2 (`eliminate_rhs` D3, `eliminate_essential_bc` D4) is conditional on those two files landing firm; both reports carry `firmness: firm` (verified). D7's choice to annotate "29 grand total" rather than renumber the "26" header is sound (renumbering would mis-describe the enumerated bullet list and would touch producer-owned bullets, outside the count-owner partition). The L4-firm-UNCHANGED-at-6 claim is likewise verified: `solve_family.md` does not yet exist on disk (D1 creates it this cycle at `rough-in (test-coverage-bounded)`, per D1 frontmatter), so L4 firm chapters stay 6 and the "Rough-in at L4 (0)→(1)" flip is correct. Severity: none (positive verification).

**Issue #6 — stale L4-frontier prose flip ("substantially complete / near-exhausted" → "active solver-test-load frontier") is correct and coherent. (informational / positive verification.)** The retirement is mandated by the 2026-06-01 VOCABULARY-SHIFT REDIRECT (CLAUDE.md: the batch-14 "substantially complete / strategic-pivot" framing is retired; solvers are a test-load that advances a layer when cleanly describable). D7's reword correctly preserves the still-valid sub-claim (13-of-18 BLAS-1/elementwise/smoother L3 ops remain no-L4-by-design) while retiring only the over-broad inference that the whole L4 frontier is exhausted. `solve_family` as the "first solver-driven L4 combinator" is consistent with D1's framing. Coherent with the redirect. Severity: none.

**Collision-discipline verdict (positive):** All of D7's `old` anchors target COUNT/NARRATIVE regions (cohort headers at L4:32/47/56, L1:31/70, and D2's seeded cohort bullet at L4-L3) — NONE target a D1–D6 producer's dep-map row, §Vocabulary-cohort own-bullet, or SUMMARY entry. This honors the count-owner partition exactly as described in §Supporting evidence. No collision.

## Repair

### Fixes attempted

- **Finding (Issue #2 — fgmres/gmres prose↔table firmness divergence)**
  - **Decision**: unrepairable
  - **Investigation**: The repair instruction directed me to reconcile `L4/index.md:52-53` prose to the
    L4-L3 table — UNLESS the theme files' own `## Status` lines are authoritatively `firm`, in which case
    reconcile the other direction. I verified the on-disk truth on three independent surfaces:
    1. `book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md:196-198` — `## Status` = ``firm`` (cycle-020 wave-1 lifter re-anchor, fully justified).
    2. `book/src/L4-L3/fgmres-inner-loop-iterate-while-migration.md:191-195` — `## Status` = ``firm`` (cycle-021 wave-1 lifter re-anchor, closes the 5-batch carry-forward).
    3. `log/cycle-020.md:24` ("`gmres-inner-loop` PROMOTED rough-in→firm … L4>L3 firm 1→2") and `log/cycle-021.md:14`
       ("`fgmres-inner-loop` PROMOTED rough-in→firm … L4>L3 firm 2→3") — both firmings landed and are recorded.
    The authoritative truth is **both themes are firm** (since c020/c021). Therefore the `L4/index.md:52-53`
    PROSE (which labels both `(firm)`) is **already correct** — no prose edit is warranted. The defect is the
    **stale `L4-L3/index.md` table rows 16-17**, which were never updated from their original cycle-008/011
    `rough-in` status when c020/c021 firmed the themes (row 16 even still carries the c008 boilerplate "this
    dispatch creates the anchor file").
  - **Rationale (why unrepairable)**: Fixing the true defect is beyond repair authority on three counts:
    (a) The correct fix is to update the stale `L4-L3/index.md` **table** rows — that is an artifact mutation
        (`book/`), outside the repairer's write partition (repairer edits CYCLE.md / supporting docs only).
    (b) The true firm count pre-cycle is **5**, not 3 (`iterate-while-dissolution`,
        `iterate-while-with-prev-dissolution`, `ksp-solve-driver-dissolution`, `gmres-inner-loop`,
        `fgmres-inner-loop`). With D2's `solve-family-map-dissolution` the on-disk-truthful tally is **5→6**,
        NOT the report's **3→4**. The planner's "6→7" projection was therefore essentially correct (counted
        from the firm prose/theme-file surface). D7's entire edit#2 consolidated tally rests on the stale-table
        premise and is wrong; recomputing the count surface is the count-owner's substantive job, not a
        mechanical repairer fix.
    (c) The critic verified "3→4 correct against on-disk reality" by consulting ONLY the stale table, not the
        theme files' `## Status` or the cycle log. The repairer may not override the critic's `checks:` values,
        but the deeper on-disk truth I was explicitly instructed to verify contradicts the repair-instruction
        premise that the table is authoritative — so I defer rather than encode either a known-wrong count or
        a check override.

- **Finding (Issue #3 — fe_assemble citation-residual OQ over-counts: should say 1 place not 2)**
  - **Decision**: not-needed (the critic's correction would introduce an error)
  - **Investigation**: `grep -n "215-217" book/src/L1/fe_assemble.md` returns **two** matches:
    - `fe_assemble.md:147` — the §laws ref `palace/models/laplaceoperator.cpp:215-217`.
    - `fe_assemble.md:257` — the §Evidence ref ``(`:215-217`, the separable `eliminate_essential_bc` post-comp)``.
    Line 253 separately cites the broader correct `184-223` (as the critic noted), but the stale `215-217`
    string ALSO appears at line 257. D7's OQ note ("appears in 2 places: §laws ~line 147, §Evidence ~line 257")
    is therefore **on-disk-accurate on the count of 2**; the critic's Issue #3 ("only 1 place, at 147") missed
    the line-257 occurrence. Applying the critic's "2 → 1" correction would make D7's note false.
  - **Action**: none. Left D7's "2 places" note intact (it is correct). This sits in a deferred OQ note that D7
    explicitly scopes OUT of count-owner work, so it affects no applied edit either way.

- **Finding (Issue #4 — edit#2 D2-before-D7 application-ordering dependency)**
  - **Decision**: not-needed
  - **Rationale**: D7 documented the dependency and provided a fallback ("integrate as an append to the
    `## Vocabulary-cohort` section" if the exact-text anchor fails). The wave order (D2 wave-2, D7 wave-3)
    honors it. Informational per the critic; no fix.

### Unrepairable findings

- **Issue #2 / cross-reference-integrity — L4-L3 consolidated tally is computed from a stale table; the true
  firm count is 5→6, not 3→4.** Routed to **lifter**. The lifter pass should:
  1. Reconcile the stale `book/src/L4-L3/index.md` table rows 16-17 (`gmres-inner-loop` /
     `fgmres-inner-loop`) from `rough-in` to ``firm`` to match the themes' authoritative `## Status` and the
     c020/c021 cycle logs (the `L4/index.md:52-53` prose is already correct and should NOT be touched).
  2. Re-author D7's edit#2 consolidated tally to the on-disk-truthful **5 firm → 6 firm** (4 prior firm is
     wrong; the prior firm set is the 5 named above).
  3. Close/repoint OQ `l4-l3-fgmres-firmness-prose-vs-table-divergence` — the divergence is resolved by fixing
     the table (the prose was right all along), not by a future prose-vs-table audit that assumed the table.

### Suggested resolution

`needs-revision` — do NOT apply edit#2's "3→4 firm" tally; it under-counts because it was computed from a stale
`L4-L3/index.md` table that never reflected the cycle-020/021 firming of `gmres-inner-loop` and
`fgmres-inner-loop`. The other two index targets in this report are sound and independently applicable:
- **Edit #1 (`L4/index.md`** — L4 firm UNCHANGED at 6, rough-in 0→1, active-frontier reword): verified correct,
  applicable as-is.
- **Edit #3 (`L1/index.md`** — FE sub-spine Rough-in→Firm, grand-total 27→29): verified correct, applicable as-is.
- **Edit #2 (`L4-L3/index.md` tally)**: needs the lifter's 5→6 recomputation + the stale-table-row fix before
  it can land truthfully.

The integrator may apply edits #1 and #3 and stage edit #2 for the follow-up lifter, or hold the whole report
for the lifter re-dispatch — integrator's call. D7 did its job correctly given its inputs; the failure is an
upstream stale-table surface the count-owner read in good faith (and even flagged as an OQ), compounded by the
critic verifying the arithmetic against that same stale surface.
