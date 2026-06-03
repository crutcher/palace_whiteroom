---
verifies: ../CYCLE.md
critiqued_at: 2026-06-03T00:54:20Z
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
adapted-checks:
  chapter-preservation: pass
  alpha-sort-correctness: pass
  directive-guards-honored: pass
  pre-existing-drift-scoping: warning
  old-anchor-fidelity: pass
repaired_at: 2026-06-03T01:08:00Z
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
  pre-existing-drift-scoping: repaired
overall_status: ready
follow_up_agent: null
---

# META: verification of directive-3 reorg — Concepts + small Parts (D6)

## Critique

This is a directive-3 STRUCTURAL-REORG dispatch: pure `SUMMARY.md` re-sort, no new operator/theme claims, no new group-intro pages. The 8 standard critic checks (citation-validity, surface-or-evidence, rotation-quality, variant-axis-coverage, cross-reference-integrity, edge-label-fidelity, plan-kind-consistency, skill-uptake-survey) **no-op on this report shape** — there are no source claims, no rotations, no surface modifications, no variant axes, no edge labels. cross-reference-integrity is the only standard check with traction (do the re-ordered links resolve?) and it passes: every `[new]` link basename maps to an on-disk `concepts/*.md` file, and the set is unchanged from `[old]`. The substantive verification is the adapted structural checklist below.

### Adapted checks run

**chapter-preservation (load-bearing) — pass.** Mechanically verified the `[new]` Concepts block is a pure re-ordering of `[old]`: 46 link rows in each (2 navigation header rows `Index`/`Dependency map` + 44 content concept rows), zero duplicates in either, and the slug-set is **identical** (`set(old) == set(new)`, empty symmetric difference). No concept dropped, none added, none renamed. The four other owned Parts (`# Methodology`, `# Feature surfaces — entry points`, `# Design Artifacts`, `# Meta-Reviews`) do not appear in the proposed-changes `edit:` block at all, so they are provably untouched by this diff. Confirmed on disk that those Parts retain their current content (SUMMARY lines 4–11, 277–303). Pass.

**alpha-sort-correctness — pass.** The 44 content slugs in `[new]` are C-locale lexicographically sorted by **file slug** (`content == sorted(content)`, confirmed; collation edge cases hold: `givens` < `givens_apply` < `givens_generate`, `scal` < `scalar-promotion`). The two navigation rows are correctly kept above the sorted content (landing + dep-map view, not concept entries). Consistency with `concepts/index.md`: the index table's 42 data rows are themselves sorted (by display-name AND by slug — they coincide), and the SUMMARY slug-order is consistent with it. The four `— methodology concept` display-name rows (`black-box-...`, `constructed-operators`, `rotation`, `variant-absorption`) sort into correct slug positions, so the slug-key choice does not create a display-order anomaly. Pass.

**directive-guards-honored — pass.** Each guard verified:
- `# Meta-Reviews` KEPT chronological — not in the edit block (untouched); on-disk rows 282–303 are 23 dated records with monotonic-non-decreasing cycle-range starts (1, 4, 7, …, 104, 116), matching the report's evidence. No forced alpha. Pass.
- `# Methodology` (2 chapters) and `# Design Artifacts` (2 chapters) — small-Part guard honored; not in the edit block, un-nested, landing-chapter-first order preserved. Pass.
- **`# Feature surfaces — entry points` left AS-IS (load-bearing standing-OQ guard)** — confirmed the Part is NOT in the proposed-changes edit block; on-disk SUMMARY lines 7–11 retain the within-column high→low level ordering `electrostatic.L4 → .L1 → .L0`, NOT alphabetized (alpha would force `.L0 → .L1 → .L4`). The standing batch-22-meta OQ ordering is untouched. This guard is honored. Pass.

**old-anchor-fidelity — pass.** The Concepts `[old]` block (report lines 28–74) matches disk verbatim — SUMMARY.md lines 229–275, line-for-line including the navigation header rows and the exact chronological-by-extraction order. No drift in the anchor.

**pre-existing-drift-scoping — warning.** The report correctly identifies that a SUMMARY-vs-`concepts/index.md`-table membership drift exists, correctly establishes it as **pre-existing** (the reorg is set-preserving, so it neither created nor widened the drift — confirmed by `set(old)==set(new)`), and correctly scopes the *fix* out of a reorder-only dispatch (route to a follow-up reconciliation, do not block). That scoping decision is sound and should NOT block integration. **However, the report's characterization of the drift is incomplete and partly garbled**, which is a content-accuracy defect in the flagged finding (see Issues). The drift is wider than reported: **two** SUMMARY slugs are absent from the index table, not one.

### Issues found

1. **Under-reported drift extent (CYCLE.md §Open questions, line 135; §Supporting evidence, line 128) — warning, do-not-block.** The report flags only `nested-constructed-operator-gate` as present in SUMMARY but missing from the `concepts/index.md` table. Mechanical diff shows **two** slugs in this state: `nested-constructed-operator-gate` AND `black-box-vs-accelerated-kernels`. Both files exist on disk (`book/src/concepts/{nested-constructed-operator-gate,black-box-vs-accelerated-kernels}.md`); both are in SUMMARY (44 content slugs); the index table has only 42 rows, missing exactly these two. The report's "41 entries vs 42 rows" framing implies the index table is a *superset* of SUMMARY (table has more), but the truth is the reverse — SUMMARY (44) is a strict superset of the table (42). The follow-up reconciliation dispatch the report requests should add **both** missing rows, not just `nested-constructed-operator-gate`. This is a finding-accuracy issue, not a reorg-correctness issue: the reorg itself is clean.

2. **Entry-count mis-statement (CYCLE.md §Summary line 14, §Supporting evidence line 127, repeated throughout) — warning, cosmetic.** The report repeatedly states the Concepts Part holds **"41 concept entries"**. The actual content-entry count is **44** (excluding the 2 navigation rows `Index`/`Dependency map`). The slug-set preservation is nonetheless correct (44→44, verified), so the off-by-3 count does not affect the reorg's correctness — it is a reporting error in the count, not in the diff. The `[new]` block is complete and faithful regardless of the stated cardinality.

3. **Garbled evidence sentence (CYCLE.md §Supporting evidence, line 128) — note.** The parenthetical "two SUMMARY-block entries (`nested-constructed-operator-gate`, `eigsolve`/`erasure-scope` were already in the SUMMARY but the `concepts/index.md` table omits `nested-constructed-operator-gate`, `dependency-map`, `eigsolve`-vs-table" is syntactically broken (unclosed paren, conflated examples) and factually loose: `eigsolve` and `erasure-scope` ARE in the index table (verified), so they are not part of the drift. Only `nested-constructed-operator-gate` and `black-box-vs-accelerated-kernels` are the genuine table-omissions. This sentence should be rewritten in the repair pass to state the drift accurately, or deleted in favor of the cleaner §Open-questions formulation (itself needing the one-slug→two-slug correction from Issue 1).

### Verdict (concise)

- **Concepts preservation + alpha:** PASS. Pure set-preserving re-ordering (44 content slugs + 2 nav rows, identical slug-set old/new, no dup/drop/rename), correctly C-locale slug-sorted, consistent with the already-sorted index table. `[old]` matches disk verbatim.
- **Feature-ordering guard honored?** YES. `# Feature surfaces` is not in the edit block; the `electrostatic.L4 → .L1 → .L0` within-column high→low ordering is untouched (NOT alphabetized). The other three small/dated Parts (`Meta-Reviews` chronological, `Methodology`, `Design Artifacts`) are likewise untouched. All directive guards honored.
- **Pre-existing drift correctly scoped?** Scoping YES (pre-existing, set-preserving reorg neither created nor widened it, correctly routed to follow-up, correctly not blocking). Characterization NO — the report under-counts the drift (2 missing index rows, not 1: also `black-box-vs-accelerated-kernels`), mis-states the entry count as 41 (actual 44), and carries a garbled evidence sentence. These are finding-accuracy warnings on an otherwise-correct reorg; they inform the requested follow-up reconciliation but do not block application of the re-sort.

## Repair

### Fixes attempted

The three finding-accuracy warnings are mechanical text corrections to the report's drift characterization (counts, slug names, direction of containment, a garbled sentence). They do NOT touch the proposed-changes `edit:` block (the re-sort itself is correct and untouched), do not author substantive content, and do not mutate the artifact. All three are in repair scope.

- **Finding 1 (Under-reported drift extent — pre-existing-drift-scoping warning, do-not-block).** The report named only `nested-constructed-operator-gate` as in-SUMMARY-but-absent-from-index-table; the truth is TWO slugs (`nested-constructed-operator-gate` AND `black-box-vs-accelerated-kernels`), and SUMMARY (44) is a strict superset of the table (42), not the reverse.
  - **Decision**: repaired.
  - **Action**: corrected the §Open-questions drift entry (CYCLE.md §Open questions) to state the correct direction (SUMMARY 44 ⊃ index-table 42), name BOTH missing slugs with their on-disk paths, note that `eigsolve`/`erasure-scope` are NOT part of the drift, and route the reconciliation to the batch-22 meta-phase OR a cycle-072 hygiene dispatch (add both rows, confirm 1:1). Also corrected the §Supporting-evidence note (see Finding 3).

- **Finding 2 (Entry-count mis-statement — warning, cosmetic).** Report says "41 concept entries"; actual is 44 content entries (46 rows incl. 2 nav).
  - **Decision**: repaired.
  - **Action**: corrected the count 41→44 (content) / 46 (total) at all three sites: CYCLE.md §Summary (Concepts bullet + "pure reordering of the same … links" line) and §Supporting-evidence (Concepts-block line). Slug-set preservation was already correctly verified, so only the stated cardinality changed.

- **Finding 3 (Garbled evidence sentence — note).** The §Supporting-evidence parenthetical was syntactically broken (unclosed paren, conflated examples) and factually loose (implicated `eigsolve`/`erasure-scope`, which are PRESENT in the table).
  - **Decision**: repaired.
  - **Action**: rewrote the §Supporting-evidence note (CYCLE.md §Supporting evidence) into a clean statement of the drift: SUMMARY (44) strict superset of table (42), the two genuine omissions named, explicit note that `eigsolve`/`erasure-scope` are in the table, cross-reference to the §Open-questions routing.

### Unrepairable findings

None. All three findings were finding-accuracy text corrections within repair authority. Per task scope, the actual index-table reconciliation (adding the 2 missing rows to `concepts/index.md`) is deliberately NOT performed in this reorder-only dispatch — it is routed as a follow-up via the corrected Open question, not deferred as an unrepairable repair-phase finding.

## Suggested resolution

`overall_status: ready`. The reorg re-sort is correct and clean (critic-confirmed: set-preserving, C-locale sorted, Feature-ordering + Meta-Reviews + small-Part guards all honored, `[old]` matches disk verbatim) and applies as-is. The finding-accuracy warnings on the drift characterization are now corrected in CYCLE.md, so the routed follow-up is accurate.

Note for the integrator: do NOT reconcile `concepts/index.md` as part of applying this report — that is explicitly out of scope. The corrected §Open question routes the 2-missing-row reconciliation to the batch-22 meta-phase or a cycle-072 hygiene dispatch; promote it accordingly.
