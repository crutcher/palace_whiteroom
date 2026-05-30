---
agent: layer-intro-author
invoked_at: 2026-05-30T05:01:00Z
scope: concepts/eigsolve.md cross-cutting concept page
status: no-op-stale-scope
integrated_at: 2026-05-30T051734Z
integration_commit: PLACEHOLDER_SHA
integration_notes: noop-stale-scope (cycle-031 D6b) — concepts/eigsolve.md page firm-landed c025, refined c026; OQ-ledger marker concepts-eigsolve-page-still-absent already RESOLVED c025; cycle-031 D6 re-route recruited from stale priorities.md:37 (six cycles out of date). Orchestrator retired stale line + filed shared OQ cycle-planner-pre-dispatch-existence-check-of-target-artifact. No book changes; CYCLE.md disposition recorded for traceability; routed as batch-9 meta-phase agenda item.
---

# CYCLE: concepts/eigsolve.md — STALE-TARGET DEFERRAL (page already firm cycle-025)

## Summary

**Defer; the authoring target does not exist.** The cycle-031 D6 re-route was itself stale: `book/src/concepts/eigsolve.md` is **already on disk**, is **already wired into `book/src/SUMMARY.md`** (at `:198` under the concepts section), and the OQ this dispatch was framed against (`concepts-eigsolve-page-still-absent`) is **already marked `resolved cycle-025`** in `scaffolding/open-questions.md:341`. The originating plan item `eigsolve-l2-l1-and-concept` is also marked **`FULLY discharged (both halves landed c025)`** at the same OQ-ledger line.

No proposed-changes are emitted — there is nothing to author. This CYCLE.md is the no-op disposition for D6 plus the audit confirmation that the existing on-disk page matches the dispatch's specification.

The dispatch prompt's premise ("the concept page is the missing reader-facing synthesis", "concepts/eigsolve.md is currently ABSENT") is **stale**. Reading the OQ ledger BEFORE authoring — per the role-spec discipline "Survey chapter firmness from the on-disk `## Status`, NOT the cycle record" generalized to "verify the artifact target exists/is-absent on disk before treating the dispatch's premise as ground truth" — caught this in one read.

## Audit confirmation — what is actually on disk

The page `book/src/concepts/eigsolve.md` (created cycle-025; refined cycle-026 D7 lifter for live-link upgrade of the chain-entry "concepts/eigsolve does not yet exist" prose) was read in full (202 lines) and audited against the dispatch's three success-criteria items:

1. **Reads as cross-cutting synthesis** (not operator-entry duplication):
   - Opening paragraph establishes the *navigational/conceptual home* framing and the explicit "if this page and any L_n entry disagree on a factual claim, the L_n entry wins" rule (`book/src/concepts/eigsolve.md:1-14`) — verbatim the discipline from the role-spec `concepts/` page bullet.
   - One-line semantics + the four-way sum-typed `EigStatus` are summarized; the algebraic laws are NOT re-stated (forwarded to L1 entry) (`:16-26`).
   - The `EigSolver[problem]` opaque type, the shift-invert composition seam (`apply_linop ▷ ksp_solve`), and the opaque-library-ownership L3 verdict are the three main sections — exactly the "cross-cutting synthesis" structure the dispatch asked for (`:28-129`).

2. **Threads the layer stack** (the dispatch's explicit ask: "how it threads the layer stack (L1 operator → L2 spectral-transform composition → L3 partial-obstruction with the opaque eigen-iteration)"):
   - L1 chain link: `:6` ("`L1/eigsolve` (firm)").
   - L2 chain link: `:7` ("`L2/eigsolve` (firm)").
   - L3 chain link: `:8` ("`L3/eigsolve` (partial-obstruction)").
   - L0 surface: `:8-9` ("`L0/eigensolver-wrapper`").
   - Section §"The shift-invert spectral-transform composition seam" `:64-99` explicitly narrates the L2/L3 per-step body opening — the dispatch's specified content.
   - Section §"Opaque-library ownership — why L3 is a partial-obstruction" `:101-129` carries the explicit L3 verdict justification — the dispatch's specified content.

3. **Cross-links to all firm entries** (live links, per role-spec discipline "live links — all targets are on disk"):
   - L1/L2/L3 main chain: `:6-8` + repeated throughout + summarized in §"See also" `:183-202`.
   - L2>L1 theme: `:150` (`L1-L0/eigsolve-mutation-rotation` — note: the dispatch lists `L2-L1/eigsolve-spectral-transform-composition` as one of the firm targets; that L2>L1 theme is also live-linked from the page at `:97-98` via the L2 entry forward — confirmed by reading `L2/eigsolve.md:155` cited in the page).
   - L1>L0 themes: `:150-153` (`eigsolve-mutation-rotation`, `eigsolve-convergence-reason-mapping`).
   - NEP-interior cohort atoms: `:143-149` (the 5 L1 atoms `apply_nonlinear_pencil`, `nleps_jacobian_action`, `nleps_eigenvalue_correction`, `nleps_deflated_residual`, `nleps_deflated_solve` — all firm per their on-disk statuses).
   - Concept cross-links: `:32-33` (`solver-as-operator`, `ksp_solve`), `:125` (`sequential-obstruction`), `:98` (`constructed-operators`), `:200-202` (`solve-monad`).

4. **L0 citation hygiene** (per role-spec discipline "Verify any L0 citations with `tools/citecheck/ --scan`"):
   - `python3 tools/citecheck/citecheck.py --scan book/src/concepts/eigsolve.md --quiet` → **`12 ok, 0 failing (12 citations checked).`** All 12 pinpoint `palace/...` citations resolve clean.

5. **On-disk firmness of the chain entries** (per role-spec discipline "Survey chapter firmness from the on-disk `## Status`"):
   - `book/src/L1/eigsolve.md:165` → `## Status` block reads `firm` (cycle-022; the test-coverage-bounded qualifier was retired cycle-022). Concept page asserts `(firm)` at `:6` ✓.
   - `book/src/L2/eigsolve.md:153` → `## Status` block reads `firm` (cycle-023). Concept page asserts `(firm)` at `:7` ✓.
   - `book/src/L3/eigsolve.md:189` → `## Status` block reads `partial-obstruction`. Concept page asserts `(partial-obstruction)` at `:8` ✓.
   - All three chain links use live-link `[...](../L_n/eigsolve.md)` form (targets all on disk) — per role-spec convention ✓.

6. **SUMMARY.md registration** (per role-spec discipline "Register the new page in `book/src/SUMMARY.md`"):
   - `book/src/SUMMARY.md:198` carries `- [eigsolve](./concepts/eigsolve.md)` under the concepts section — placement is alphabetically-late among siblings (after `nested-constructed-operator-gate` at `:197`), consistent with prior c025 landings of similar-tier concept pages. No additional surgical insert needed.

## Proposed changes

**None.** The dispatch target is already on disk, fully meets the dispatch's three structural asks, passes citecheck clean, and is already wired into `SUMMARY.md`. There is no defensible additional edit at the layer-intro-author authority that would not duplicate / replace existing material the c025 dispatch already landed and the c026 lifter already refined.

## Supporting evidence

- `scaffolding/open-questions.md:323` — original migration of `concepts-eigsolve-page-still-absent` from `:323` "informational" cluster → plan item `eigsolve-l2-l1-and-concept` (cycle-025 active-head #2/#3).
- `scaffolding/open-questions.md:341` — resolution log entry: "`concepts-eigsolve-page-still-absent` — resolved cycle-025 — `book/src/concepts/eigsolve.md` created (cross-cutting nav home; introduces `EigSolver[problem]`); the migrated-to-plan `:323` clause + the `eigsolve-l2-l1-and-concept` plan item FULLY discharged (both halves landed c025)."
- `scaffolding/open-questions.md:343` — cycle-026 D7 lifter follow-up: `concepts-eigsolve-chain-entries-live-link-upgrade-followup` — resolved cycle-026 — the three chain entries' stale "`concepts/eigsolve` does not yet exist" prose upgraded to live links.
- `book/src/concepts/eigsolve.md` (202 lines, on disk; created c025, refined c026).
- `book/src/SUMMARY.md:198` (registration on disk).
- `python3 tools/citecheck/citecheck.py --scan book/src/concepts/eigsolve.md --quiet` → `12 ok, 0 failing`.
- On-disk `## Status` lines: L1:165 `firm`, L2:153 `firm`, L3:189 `partial-obstruction` — match concept page assertions verbatim.

## Open questions / caveats

- **OQ `concepts-eigsolve-page-still-absent` was already addressed cycle-025**, not by this dispatch. The cycle-031 plan's framing of D6 as the "last authoring gap in the eigsolve cohort" was inherited from the dispatch prompt; reading the OQ ledger before plan-emission would have caught it. **Recommend** routing this finding to the cycle-031 finalize integrator as a no-op deferral row in the staging log, and to the cycle-031 meta-phase consideration for a friction-ledger entry under the **stale-target dispatch** pattern (already a known shape: cycle-031 D6 originally targeted `nleps` which was also stale/already-firm; this is the *second* stale re-route in the same cycle's D6 slot, which raises the bar from "incidental" to "pattern this cycle"). Candidate friction-ledger slug: `cycle-planner-dispatch-target-staleness-not-caught-pre-emission` — the localization pre-pass per priorities §dispatch-resilience path (a) (the cycle-planner pre-localize-known-heavy-regions bullet — commit `f582a66`) does not catch *artifact* target-staleness (it catches *source* region drift); a sibling check on dispatch-time presence/absence of the artifact target (`ls book/src/concepts/<slug>.md`) would have caught both D6 re-routes pre-emission. NOT raising a `problems/` file — meta-phase route is sufficient.
- No factual disagreement found between the on-disk concept page and the on-disk L1/L2/L3 entries. The audit above is also a fresh-eyes sanity pass on the c025 page; no defects surfaced.

## Disposition

`overall_status: deferred (stale-target)` — the authoring target exists firm-and-clean. This CYCLE.md serves as the audit-confirmation record + the stale-dispatch friction signal for cycle-031 meta-phase consumption.
