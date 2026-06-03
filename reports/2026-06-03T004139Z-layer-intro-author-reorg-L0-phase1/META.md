---
verifies: ../CYCLE.md
critiqued_at: 2026-06-03T010500Z
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
repaired_at: 2026-06-03T011500Z
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

# META: verification of "L0 + Phase-1-corpus directive-3 structural reorg" (D5)

## Critique

This is a directive-3 STRUCTURAL-REORG dispatch (pure `book/src/SUMMARY.md` `# L0` + `# Phase 1 corpus` regroup + index re-sort + 3 new group-intro pages). No new operator/theme claims, no surface edits to existing chapters, no rotations. The standard citation/surface/rotation/variant/edge checks therefore no-op (marked `pass`, not-applicable to a reorg report); the adapted structural checklist (chapter-preservation, alpha-sort, small-Part guard, group-intro soundness, `[old]`-anchor fidelity) is the load-bearing surface and is reported below.

### Checks run

- **citation-validity** — not applicable to a structural reorg; no algebraic claims are asserted. The report's evidentiary claims (cohort split, chapter counts) are structural assertions verified directly against disk in the adapted checks below. `pass`.
- **surface-or-evidence** — not applicable; no existing operator/theme surface is modified (titles preserved verbatim, only re-ordered + nested). `pass`.
- **rotation-quality** — not applicable; no rotation asserted. `pass`.
- **variant-axis-coverage** — not applicable. `pass`.
- **cross-reference-integrity** — verified. All 22 L0 chapter slugs + 9 Phase-1 slice slugs in the `[new]` block resolve to files on disk (`book/src/L0/*.md`, `book/src/spec/slices/*.md`). The 3 new `create:` intros (`conventions-intro.md`, `file-overviews-intro.md`, `overload-sets-and-classes-intro.md`) are absent on disk (correct for `create:`) and are wired into SUMMARY as the parent of each grouping. Each intro's only internal link is `./index.md`, which resolves to `book/src/L0/index.md`. `spec/index.md` (the retained Phase-1 group index) resolves. No dead links introduced. `pass`.
- **edge-label-fidelity** — not applicable (no lowering edge). `pass`.
- **plan-kind-consistency** — content shape matches a reorg dispatch: SUMMARY edit block + 3 group-intro creates + scoping rationale. No mis-classification. `pass`.
- **skill-uptake-survey** — `summary-md-surgical-insert` is the nearest relevant skill but applies to insertions, not a whole-block regroup; non-blocking. `pass`.

### Adapted structural checks

1. **Chapter-preservation (load-bearing) — PASS.** Set-diff of `[old]` vs `[new]` slugs (excluding the 3 new intros) is empty: 33 path slugs in each, identical sets, no duplicates in `[new]`. Every `[old]` chapter appears exactly once in `[new]`; no drop, no rename, no re-path. On-disk reconciliation: `book/src/L0/` holds 23 `.md` (22 chapters + `index.md`) — all 22 chapters present in both blocks. `book/src/spec/slices/` holds exactly 9 `.md`; all 9 present and retained. **Count reconciliation: the dispatch directive's "planner awk said 10" is wrong; on-disk is 9.** The report's "9 slices" is correct and matches disk verbatim — no missing/phantom 10th slice. No build-time dead link from a dropped chapter.

2. **Alpha-sort correctness — PASS (by slug, the report's stated key).** The report states "alpha-sorted **by slug**." Checked against the slug (filename) key, all four lists are clean: Conventions (6), File overviews (11), Overload-sets & classes (5), Phase-1 flat (9) all pass `sort -c` on their path filenames. NOTE for the integrator: by *visible title* the File-overviews and Overload-sets groups are NOT title-sorted (e.g. `fespace` title sorts after `libceed` but its slug `fespace-file` sorts before; `Overload set —` precedes the `Class —` titles though `apply-linop` slug leads). This is internally consistent with the declared slug-key and a defensible realization of the alpha directive, but it diverges from a title-key reading — flagged as an observation, not a defect, since the report is self-consistent and the directive memory note ("sort the list-of-API/dep-map sections ALPHABETICALLY") does not pin the key. If the meta-phase one-time-reorg settles on title-key sorting across the 6 parallel dispatches, these two groups would re-order.

3. **Small-Part guard — PASS.** The 3 L0 source-area cohorts are 6 / 11 / 5 members, each ≥2, so nesting (vs. flat) is warranted. The cohorts match `book/src/L0/index.md` §Reference-note cohort 1:1: Conventions (index lines 15–20, 6 bullets), File overviews (lines 24–33, 11 bullets), Overload sets and class interfaces (lines 37–41, 5 bullets) — same membership as the SUMMARY nesting. Phase-1 left flat (correct — raw-material reference list, not a vocabulary layer, per the dispatch directive).

4. **New group-intro pages — PASS.** All 3 are sound 1-screen orientations condensing the matching `index.md` cohort paragraph; each links back to `./index.md` §Reference-note cohort (resolves), no dead links, no over-claiming. All 3 wired into SUMMARY as grouping parents and absent on disk (correct `create:` state). Phase-1 paths target the correct on-disk `spec/` locations (`./spec/slices/*.md` + the retained `./spec/index.md` group index) — the report correctly did NOT relocate slices into `L0/` and correctly left `spec/index.md` as the group's own index rather than authoring a 4th intro.

5. **`[old]` anchor fidelity — PASS.** The report's `[old]` block (CYCLE.md lines 48–82) matches on-disk `book/src/SUMMARY.md` lines 194–228 verbatim, line-for-line, including the original non-alpha order. The dispatch-phase note (an initial direct SUMMARY edit was applied then reverted) is confirmed true: on-disk SUMMARY is the un-reorganized original, so `integrator-per-report` will find the `[old]` anchor intact. No leftover `book/` mutation from D5.

### Issues found

No blocking issues. One observation for integrator/meta-phase awareness:

- **Sort-key ambiguity (observation, severity: low)** — CYCLE.md §Proposed-changes, File-overviews and Overload-sets groups. Lists are slug-key alpha-sorted (clean) but not visible-title alpha-sorted. Self-consistent with the report's declared "by slug" key; surfaced only so the meta-phase can confirm slug-key vs title-key is uniform across the 6 parallel directive-3 reorg dispatches (D1–D6). Not a defect in this report.

- **`spec/index.md` slice-status table ordering (observation, severity: low)** — CYCLE.md OQ. The 9 slice sub-entries are re-sorted in SUMMARY, but the report notes (correctly, as an out-of-scope caveat) it did not touch the `spec/index.md` slice-status table's internal row order or the `L0/index.md` cohort bullet ordering. Both are flagged-not-bundled in the report's Open-questions; consistent with the D5 scoping. No action required of this dispatch.

## Repair

### Fixes attempted

The critic returned all 8 checks `pass` (each not-applicable to a pure structural reorg and verified via the adapted structural checklist: chapter-preservation, alpha-sort-by-slug, small-Part guard, group-intro soundness, `[old]`-anchor fidelity — all PASS). No warning/fail finding was raised. The only two items are explicitly-flagged low-severity **observations**, not defects:

- **Finding**: Sort-key ambiguity (low) — File-overviews / Overload-sets groups sorted by file SLUG, not visible TITLE.
  - **Decision**: not-needed.
  - **Rationale**: The slug-key sort is internally consistent and clean (`sort -c` passes all four lists), and a defensible realization of the alpha directive (the directive memory note does not pin slug-vs-title key). The critic surfaced this solely so the **meta-phase** can confirm slug-key vs title-key uniformity across the 6 parallel directive-3 reorg dispatches (D1–D6) — a cross-dispatch methodology call above repair authority, not a per-report fix. Left as the standing OQ note for the meta-phase. Mutating the sort key here would be a unilateral content/methodology decision, out of scope.

- **Finding**: `spec/index.md` slice-status table ordering (low) — internal row order of the slice-status table and `L0/index.md` cohort bullets not re-sorted.
  - **Decision**: not-needed.
  - **Rationale**: Correctly scoped out by D5 (the dispatch was a SUMMARY regroup, not an index-body re-sort) and already flagged-not-bundled in the report's Open-questions. No defect; consistent with the dispatch scope.

### Unrepairable findings

None. No finding requires substantive authoring or contradicts artifact content; nothing deferred to a follow-up agent.

## Suggested resolution

`ready`. The reorg is clean per the critic's adapted structural checklist (no dropped chapters — 33 slugs preserved set-diff-empty; counts reconciled — 9 Phase-1 slices, 22 L0 chapters; alpha-sort clean by slug; cohorts match `L0/index.md`; 3 new intros sound and wired; `[old]` anchors verbatim with the dispatch-phase SUMMARY edit confirmed reverted). No `book/` or proposed-changes mutation performed by this repair pass. Integrator note: the sort-key observation is a standing OQ item for the meta-phase to settle uniformly across D1–D6 — do not act on it per-report.
