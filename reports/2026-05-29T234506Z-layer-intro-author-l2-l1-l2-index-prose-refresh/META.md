---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T235500Z
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
repaired_at: 2026-05-29T235800Z
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

# META: L2-L1 + L2 index prose refresh — critic verification

## Critique

### Checks run

**citation-validity** — pass. Mechanical `tools/citecheck/citecheck.py --scan` reports `6 ok, 0 failing (6 citations checked)`. Spot-checked the four load-bearing pinpoints with `--anchor`: `book/src/L2-L1/index.md:11-20` resolves the `incremental-least-squares-composition-lowering` row at line 20 (in-range); `book/src/L2/index.md:50-61` resolves the `incremental-least-squares` token at lines 57-58 (in-range); `book/src/L2/incremental-least-squares.md:376-378` resolves the `firm` status token at line 378 (in-range); `book/src/L2-L1/incremental-least-squares-composition-lowering.md:414-416` resolves the `firm` status token at line 416 (in-range). All citations are accurate and in-range.

**surface-or-evidence** — pass. This is a pure-prose refresh of two Part-overview navigational sections after upstream firm landings (cycle-026 L2/incremental-least-squares + cycle-028 L2>L1/incremental-least-squares-composition-lowering); both the surface (the index prose) and the evidence (the on-disk dep-map rows and status lines those new firm landings already wrote) are present. The load-bearing requirement — that the refreshed prose counts match the on-disk dep-maps — was independently verified: `grep -c "^| \[" book/src/L2-L1/index.md` returns 8 (matches "7 firm + 1 partly-constructive" claim — status-cell count: 7 firm, 1 partly-constructive, exact match); `grep -c "^| \[\`" book/src/L2/index.md` returns 10 (matches "9 firm + 1 partly-constructive" claim — status-cell count: 9 firm, 1 partly-constructive, exact match). Every count claim in the proposed prose is dep-map-anchored.

**rotation-quality** — pass (not applicable to navigational-prose-refresh report shape). The report does not assert a new algebraic / structural / reduction rotation; it refreshes Part-overview navigational prose to mirror dep-map state that prior firm landings already wrote. The Vocabulary-cohort subsection enumerates existing firm + partly-constructive entries; the named-compositions motif extension reflects already-firm L2 entries (`ksp_solve` cycle-021, `eigsolve` cycle-023). No new rotation claimed, so the check is inapplicable.

**variant-axis-coverage** — pass. The Vocabulary-cohort subsection follows the role-spec template by splitting on firmness state (Firm vs Partly-constructive); the L2 cohort retains both halves because `deflate` remains partly-constructive (per role-spec "the split is only useful when both states coexist"); the L2-L1 cohort is split similarly (7 firm + 1 partly-constructive `deflate-composition-lowering`); the L2 "Queued at L2 (stub)" subsection is correctly removed (now empty after `incremental-least-squares` promotion, per role-spec "Skip the subsection when the layer has only firm entries... or only rough-ins"). No hidden axes; the split mirrors the dep-map maturity distribution exactly.

**cross-reference-integrity** — pass. SUMMARY.md references both `L2/index.md` (line 39) and `L2-L1/index.md` (line 52) — both Part overviews stay wired. The named-compositions motif extension in Change 2 (adding `ksp_solve` as third and `eigsolve` as fourth) is supported by downstream chapter prose: `L2/ksp_solve.md:24` frames itself as "the named composition that wraps krylov-step"; `L2/eigsolve.md:23` explicitly says "`eigsolve` at L2 is the **named-composition** motif (per [`L2/index`](./index.md) §"Named compositions"), another named composition alongside [`orthogonalize`] and [`ksp_solve`]". Build-readiness fence-parity guard: 10 fence lines = 5 balanced `edit:`/close pairs (Changes 1, 2, 3a, 3b, 4 — Change 3 is split into two edits as the report explicitly states), no nested fences, no `firm`-claimed body sits outside a fence. `L1/back_solve.md` exists on-disk (firm cycle-027 leaf the cohort-entry cites); `L1/ls_update_column.md` does NOT exist but is correctly carried as a plain-text forward-reference within the dep-map descriptor (consistent with the existing on-disk row at `L2-L1/index.md:20` — the report does not promote it to a live link). No dead links, no missing slugs, no inconsistent counts.

**edge-label-fidelity** — pass (not applicable to navigational-prose-refresh report shape). The report does not author or edit any edge-labeled lowering theme content; it edits index prose that mentions L2 / L2-L1 / L2↔L1 / L3 in passing as navigational scaffolding (e.g., "the L2 named composition lowers into L1 leaves"). All edge directions in the prose match the natural high→low convention.

**plan-kind-consistency** — pass. Status declared `pending` (frontmatter `status: pending`), scope declared `L2-L1 + L2 Part-overview prose refresh`. Verified: every edit block is additive prose or subsection-shape modification — no dep-map row, no status line, no chapter-body content edited. The four (effectively five-block) edits target: (1) L2-L1 add Vocabulary-cohort subsection + Cohort-growth-log bullet; (2) L2 named-compositions motif paragraph refresh; (3a) L2 remove now-empty "Queued at L2 (stub)" subsection; (3b) L2 add two stale-by-omission firm entries to Vocabulary-cohort "Firm at L2" list; (4) L2 Working-Notes bullet refresh. The "no structural edits" framing matches the actual diff shape exactly. layer-intro-author scope shape (Part-overview prose) is correctly self-described.

**skill-uptake-survey** — pass. The report's discipline section explicitly invokes the role-spec rules driving the edits: the cohort-split threshold rule (`≥3 firm + a queued / partly-constructive entry`), the role-spec template for split-by-firmness Vocabulary-cohort subsections, the "Skip the subsection when the layer has only firm entries... or only rough-ins" rule for removing the empty Queued subsection, and the survey-from-on-disk-`## Status` discipline (rather than trusting the dispatcher's count). No skill-invocation gap on the producer side. The producer also self-verified the dispatcher's stated count rather than trusting it — a defensible discipline application even when the dispatcher count happens to be correct.

### Issues found

**No defects found.** This is a clean low-fan-out navigational hygiene report: the bar is count-accuracy + no accidental structural mutation, and both hold:

- L2-L1 dep-map count claim (8 = 7 firm + 1 partly-constructive) matches the on-disk row count + status-cell count exactly.
- L2 dep-map count claim (10 = 9 firm + 1 partly-constructive) matches the on-disk row count + status-cell count exactly.
- L2/incremental-least-squares and L2-L1/incremental-least-squares-composition-lowering both confirmed `firm` on-disk via `## Status` line scan.
- The "Firm at L2" sub-list staleness diagnosis (omits `incremental-least-squares` AND `eigsolve`) verified on-disk — current list (lines 32-38) has exactly 7 entries: krylov-step, chebyshev-iteration, linear_combination, inner_product, orthogonalize, ksp_solve, gram. Both missing entries the report adds (`incremental-least-squares` cycle-026 firm, `eigsolve` cycle-023 firm) are firm in the dep-map.
- The "Queued at L2 (stub)" subsection at line 44-46 is verified to contain only `incremental-least-squares` (now firm) — removal is correct.
- The named-compositions motif extension to 4 exemplars (orthogonalize, incremental-least-squares, ksp_solve, eigsolve) is downstream-anchored — `L2/eigsolve.md:23` explicitly establishes the 4-way framing already.
- Proposed-changes fence parity holds (10 fences = 5 balanced pairs, no nested fences).
- No structural mutation: every edit is additive prose or subsection shape; no dep-map row, status line, or chapter content edited.

**Two minor observations** (not defects; not blocking; worth noting for repairer awareness if relevant):

1. Line 82 of `book/src/L2/index.md` (the "Batch-6 cohort growth" Working-Notes bullet) says "three landings raised the firm cohort **6→8**" — a historical description of what batch-6 did, not a current count claim. The current firm cohort at L2 is 9 (post c021 ksp_solve + c026 incremental-least-squares), not 8. The report does NOT touch this bullet (Change 4 targets a different bullet at lines 78-79). The line is historically accurate as a what-batch-6-did description, so it is NOT a defect — but if a future refresh wants to add a "cycle-021/026 cohort growth" note for symmetry with the batch-6 bullet, lines 80 (ksp_solve note) and the absence of an incremental-least-squares note would be the natural targets. Flagging only because the scope adjacent.

2. Open question 3 (`ksp_solve` placement in named-compositions motif) and the report's framing choice — adding `ksp_solve` as "third" and `eigsolve` as "fourth" named composition rather than carving a separate "outer-driver compositions" sub-motif — is self-flagged by the producer as a framing choice with an alternative. The downstream chapter prose at `L2/eigsolve.md:23` explicitly endorses the inline 4-way framing ("alongside [`orthogonalize`] and [`ksp_solve`]"), so the choice is well-grounded. Not a defect; just confirming the producer's self-flag is benign.

The report is mechanically clean and ready for repairer no-op pass-through.

## Repair

### Fixes attempted

No findings required repair. The critic verdict was 8/8 pass with no warning/fail findings; all repair entries are `not-needed`.

- **Finding**: citation-validity pass (6/6 citations resolve in-range via mechanical `--anchor`/`--scan`).
  - **Decision**: not-needed.
- **Finding**: surface-or-evidence pass (count claims independently verified — L2-L1 = 8 rows = 7 firm + 1 partly-constructive; L2 = 10 rows = 9 firm + 1 partly-constructive).
  - **Decision**: not-needed.
- **Finding**: rotation-quality pass (not applicable — navigational-prose-refresh; no new rotation asserted).
  - **Decision**: not-needed.
- **Finding**: variant-axis-coverage pass (firmness-state split applied per role-spec template; empty "Queued at L2 (stub)" subsection removal correct per "skip when only firm" rule).
  - **Decision**: not-needed.
- **Finding**: cross-reference-integrity pass (SUMMARY.md wiring intact; named-compositions 4-way framing downstream-anchored at `L2/eigsolve.md:23`; fence parity 10 = 5 balanced pairs).
  - **Decision**: not-needed.
- **Finding**: edge-label-fidelity pass (not applicable — no edge-labeled lowering content authored).
  - **Decision**: not-needed.
- **Finding**: plan-kind-consistency pass (every edit is additive prose or subsection-shape modification; no structural mutation).
  - **Decision**: not-needed.
- **Finding**: skill-uptake-survey pass (cohort-split threshold rule, split-by-firmness template, skip-when-only-firm rule, on-disk `## Status` survey discipline all invoked).
  - **Decision**: not-needed.

### Unrepairable findings

None. The two non-blocking observations the critic surfaced (the historical "6→8" line at `L2/index.md:82` and the producer's framing choice for `ksp_solve`/`eigsolve` placement in the named-compositions motif) are explicitly NOT defects per the critic's own framing — the first is historically accurate as a what-batch-6-did description and out of this report's scope; the second is downstream-anchored at `L2/eigsolve.md:23` and constitutes a well-grounded producer choice. Neither requires repair authority.

## Suggested resolution

`ready` — the report is mechanically clean and may be applied as-is by `integrator-per-report`. Notes for the integrator:

- All 5 proposed-changes edit blocks are pure navigational-prose refreshes of two Part-overview indexes (`book/src/L2/index.md`, `book/src/L2-L1/index.md`) — no dep-map rows, status lines, or chapter bodies edited.
- The "Queued at L2 (stub)" subsection removal (Change 3a) is correct now that `incremental-least-squares` is firm — the subsection would otherwise be left empty.
- The named-compositions motif extension to 4 exemplars in Change 2 is already endorsed by downstream chapter prose (`L2/eigsolve.md:23` uses the inline 4-way framing).
- Fence parity confirmed by critic (10 fences = 5 balanced pairs, no nested fences) — no `proposed-changes-fence-encloses-full-body-guard` concern.
- Open question 3 (the `ksp_solve` placement framing alternative) is producer-self-flagged and may be carried forward as an OQ if the integrator considers it worth ledgering; the chosen framing is already wired downstream so deferring is also fine.
