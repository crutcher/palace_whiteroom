---
verifies: ../REPORT.md
critiqued_at: 2026-06-02T073000Z
critic_version: 1
repaired_at: 2026-06-02T074500Z
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
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
---

# META: verification of "L3 index — spectrum prose-sync (shape (f) `fold_solve`)"

## Critique

### Checks run

**citation-validity — pass.** Every load-bearing claim in the proposed `[new]` prose is backed and was cross-checked against source. (a) The stale/current divergence is real: `book/src/L3/index.md:15` spectrum prose reads "Five non-trivial-obstruction shapes then coexist" and "(b), (c), and (e) are the three `partial-obstruction` operators" (confirmed verbatim on read) — STALE; the authoritative count-tally bullet at `:64` already reads "17 firm + 4 `partial-obstruction` … `fold_solve` c059" and already carries the full shape-(f) characterization in its final two sentences ("`fold_solve` (c059) adds a SIXTH non-trivial obstruction shape (f)…") — ALREADY CURRENT. (b) The c057-meta count-owner guard is respected: the report's single `[old]`/`[new]` edit targets only `:15`; the `:64` tally is NOT in the edit block and is not otherwise touched. (c) Shape (f) is characterized from the linked chapter, not from index cells — `fold_solve.md:4` frontmatter `firmness: partial-obstruction`, `:150-156` `## Status` confirmed `partial-obstruction`; the combined obstruction (carry-threading `sequential-obstruction` + opaque per-step leaf), the Palace-authored renderable sweep (`transientsolver.cpp:77`), the in-place `sol` carry root (`timeoperator.cpp:410`), and the no-L2-composition opaque-leaf contrast against chebyshev/eigsolve all match `fold_solve.md:18`, `:24-27`, `:32`, `:152`. The L0 anchors cited in the report's Supporting-evidence (transientsolver.cpp:77, timeoperator.cpp:410) appear verbatim in the chapter; the report cites the chapter as the proximate source (correct discipline). No `verified_against:` YAML block in this report — that sub-check is N/A.

**surface-or-evidence — pass.** Not a refinement of an operator/theme surface; this is a pure index-overlay prose-sync propagating already-landed content (the `:64` tally's shape-(f) characterization) into the `:15` spectrum prose so the two loci read consistently. No new claim is introduced (report §Open-questions confirms this). Inapplicable in the rotation-claim sense; no fail condition triggered.

**rotation-quality — pass (not applicable).** No algebraic/structural rotation is asserted — this is an index-prose hygiene touch, not a layer-edge rewrite. The shape-(f) description it propagates correctly characterizes the existing `fold_solve` L3 obstruction, but the report itself proposes no rotation.

**variant-axis-coverage — pass (not applicable).** No operator variant axes are in scope for an index spectrum-prose edit. (The `fold_solve` chapter's own variant axes — schedule-source, per-step-operator, carry-shape, element-type — are covered in `fold_solve.md:9-13`/`:148`; the spectrum prose appropriately summarizes the obstruction shape without re-enumerating them.)

**cross-reference-integrity — pass.** The `[new]` prose adds one new live link `[`fold_solve`](./fold_solve.md)` — the target exists on disk and is the firm `partial-obstruction` chapter. All other links in the edited line are carried unchanged from the `[old]` text (chebyshev, eigsolve, divfree-projector, orthogonalize, ksp_solve, nested-constructed-operator-gate). The `[old]` anchor matches `:15` exactly: `grep -c "Five non-trivial-obstruction shapes then coexist"` = 1 (unique single-locus anchor). No firm-body-inside-fence concern (this is an `edit:` prose touch, not a chapter body).

**edge-label-fidelity — pass (not applicable).** No L_{n+1}→L_n edge label is carried by this index-prose edit.

**plan-kind-consistency — pass.** Declared shape is a surgical single-locus prose-sync (layer-intro-author index touch); content matches — one `edit:` block, three in-bullet sub-edits all within the single `:15` line ("Five/three" → "Six/four" + appended shape-(f) clause + extended distinction sentence). No placeholders, no mis-classification.

**skill-uptake-survey — pass.** No skill invocation is strictly implied by a single-locus index prose-sync. `summary-md-surgical-insert` is for SUMMARY.md, not applicable; the count-owner discipline is followed in-spirit per the c057-meta guard (cited in the report). Telemetry-only; non-blocking.

### Issues found

No blocking or warning issues. Observations only:

1. **(informational, not a defect)** The `:64` tally's final sentence already enumerates shape (f) with the same distinguishing facts the `[new]` prose adds (Palace-authored renderable sweep; opaque leaf with no L2 composition; carry-threading root). The report's `[new]` prose is consistent with — and a faithful expansion of — that already-landed characterization. The two loci now agree on six profile shapes and four `partial-obstruction` operators. This is the intended outcome of the sync, not duplication friction (the `:15` prose is the per-shape spectrum narration; `:64` is the count tally + one-sentence shape-(f) summary).

2. **(out-of-scope, correctly noted by the report)** The §Working-Notes bullets at `:60`/`:62`/`:63` carry stale per-cycle count snapshots and shape-count narratives ("four obstruction profile … shape (d)" at `:62`; "four non-trivial obstruction shapes (a)/(b)/(c)/(d)" at `:63`) — but these are explicitly marked SUPERSEDED landing-narrative snapshots, not the live spectrum, and the report correctly scopes them out (§Open-questions/caveats). No edit warranted; flagging only as a standing compaction candidate for a future meta-phase, consistent with the already-resolved OQ `l3-index-working-notes-stale-snapshot-compaction-candidate` referenced at `:64`.

3. **(verified clean)** The c057-meta count-owner guard is satisfied: the authoritative `:64` tally is untouched; the prose at `:15` is synced TO match it (not vice-versa), and shape (f) is sourced from `fold_solve.md` (status confirmed `partial-obstruction` at `:4`/`:150-156`), not from index dep-map cells.

## Repair

### Fixes attempted

No findings to repair. The critic returned all 8 checks `pass` with three informational observations only:
- Obs. 1 (`:64` tally already characterizes shape (f)) — intended outcome of the sync, not a defect.
- Obs. 2 (`:60`/`:62`/`:63` stale Working-Notes snapshots) — correctly scoped out by the report as SUPERSEDED landing-narrative snapshots; standing compaction candidate already filed as OQ `l3-index-working-notes-stale-snapshot-compaction-candidate`. Out of repair scope; no edit warranted.
- Obs. 3 (count-owner guard satisfied) — verified clean.

None of the three observations names a warning/fail finding or an edit target. Nothing to apply.

### Unrepairable findings

None.

## Suggested resolution

`ready`. Clean, surgical single-locus prose-sync at `book/src/L3/index.md:15` — one `edit:` block bringing the spectrum narration into agreement with the already-current `:64` count tally (six profile shapes, four `partial-obstruction` operators, shape (f) `fold_solve`). The `:64` count-owner tally is untouched; the c057-meta anti-drift guard is respected. Integrator may apply the single `[old]`/`[new]` edit as-is. The `:60`/`:62`/`:63` Working-Notes stale snapshots remain a future-meta-phase compaction candidate (already tracked), not a blocker.
