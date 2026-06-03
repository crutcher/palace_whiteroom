---
agent: layer-intro-author
invoked_at: 2026-06-03T02:02:07Z
scope: concepts/index.md API/dep-map table — 2-row membership reconciliation
status: pending
integrated_at: 2026-06-03T024500Z
integration_commit: PLACEHOLDER_SHA_CYCLE_072_FINALIZE
integration_notes: |
  Applied clean cycle-072 (D3; staging row 3/3). Edited concepts/index.md (+2 rows in alpha position: black-box-vs-accelerated-kernels [methodology], nested-constructed-operator-gate [layer-pattern]) -> 44 content rows == SUMMARY '# Concepts' 44. CLOSED the inbound OQ concepts-index-table-vs-summary-membership-drift-two-missing-rows in-line in open-questions.md (the c071 D6 hand-maintained-derived-surface drift). Disjoint from D1/D2 (no file contention). Both target pages verified on disk + SUMMARY-registered. cargo make book exit 0; links resolve; linkcheck2 clean. retroactive-budget global 0; no gate hits.
---

# CYCLE: concepts/index.md 2-row reconciliation

## Summary

The `book/src/concepts/index.md` `## Index` table (columns `| Concept | Kind |`) was missing 2 rows for concept pages that exist on disk AND are listed in `book/src/SUMMARY.md`'s `# Concepts` block — a pre-existing membership drift surfaced by the cycle-071 D6 reorg (OQ `concepts-index-table-vs-summary-membership-drift-two-missing-rows`). This report proposes adding the 2 missing rows, each in correct global-alpha position (the table is globally alpha-sorted by Concept slug, not grouped by kind):

- `black-box-vs-accelerated-kernels` → kind `methodology`; inserts between `axpy` and `build-time-vs-run-time-stratification`.
- `nested-constructed-operator-gate` → kind `layer-pattern`; inserts between `negative-result-slice` and `nrm2`.

After both insertions the table has **44 content rows** (was 42), matching the **44** content entries in the SUMMARY `# Concepts` block (the c071 D6 critic established SUMMARY has 44 content entries). **44 ⟷ 44 confirmed.**

## Proposed changes

```edit:book/src/concepts/index.md
[old]: | [axpy](./axpy.md) | primitive |
| [build-time-vs-run-time-stratification](./build-time-vs-run-time-stratification.md) | layer-pattern |
[new]: | [axpy](./axpy.md) | primitive |
| [black-box-vs-accelerated-kernels](./black-box-vs-accelerated-kernels.md) | methodology |
| [build-time-vs-run-time-stratification](./build-time-vs-run-time-stratification.md) | layer-pattern |
```

```edit:book/src/concepts/index.md
[old]: | [negative-result-slice](./negative-result-slice.md) | methodology |
| [nrm2](./nrm2.md) | primitive |
[new]: | [negative-result-slice](./negative-result-slice.md) | methodology |
| [nested-constructed-operator-gate](./nested-constructed-operator-gate.md) | layer-pattern |
| [nrm2](./nrm2.md) | primitive |
```

## Supporting evidence

**Row content cited from disk:**

- `black-box-vs-accelerated-kernels` — kind `methodology`. The page self-declares as classification vocabulary, not an operator: "Cross-cutting **classification-vocabulary** concept page" (`black-box-vs-accelerated-kernels.md:3`) — this `:3` anchor is the load-bearing kind justification (resolves mechanically). Reinforced by "This is methodology vocabulary, not an operator: it has no signature or algebraic laws of its own" (`book/src/concepts/black-box-vs-accelerated-kernels.md:6-7`) — note: the quoted phrase `methodology vocabulary` spans the line 6/7 wrap on disk (`methodology` ends line 6, `vocabulary` begins line 7), so a mechanical `--anchor` reports `[NOANC]`; the range is correct and the quote is faithful when reflowed. Matches the index `methodology` kind definition ("concepts about the dissection process itself"). Page exists on disk (`book/src/concepts/black-box-vs-accelerated-kernels.md`).
- `nested-constructed-operator-gate` — kind `layer-pattern`. The page self-declares: "A **layer-pattern** concept naming the structural shape in which a [`constructed-operator`] gate's closure carries one or more further constructed-operator gates as sub-fields" (`book/src/concepts/nested-constructed-operator-gate.md:1-5`). Its central claim is a cross-layer lowering-fidelity rule ("how L1/L2/L3/L4 work" → `layer-pattern` per the index kind definition; `nested-constructed-operator-gate.md:37-60`). Page exists on disk (`book/src/concepts/nested-constructed-operator-gate.md`).

**Alpha positions verified against current table (`book/src/concepts/index.md:64-105`):** <!-- full-path-qualified (repairer): bare `index.md` is AMBIG across 17 files -->



- `black-box-…`: `axpy` (`a-x`) < `black-` (`b-l`) < `build-` (`b-u`) ⇒ inserts at line 66/67 boundary. ✓
- `nested-…`: `negative-` (`ne-g`) < `nested-` (`ne-s`) < `nrm2` (`n-r`) ⇒ inserts at line 89/90 boundary. ✓

**Count reconciliation:** current table = 42 content rows (`book/src/concepts/index.md:64-105`, 42 `| [...] |` rows). +2 = 44. SUMMARY `# Concepts` block = 44 content entries (c071 D6 critic). **44 ⟷ 44.**

**Sibling kin precedent for kind assignment:** `constructed-operators` (methodology), `constructed-operator-factory` (layer-pattern), and `solver-as-operator` (layer-pattern) are already in the table — `nested-constructed-operator-gate` is the composition counterpart of `constructed-operator-factory` (`nested-constructed-operator-gate.md:6-9`) and correctly shares its `layer-pattern` kind.

## Open questions / caveats

None. The two `[old]` anchors are 2-line verbatim slices of the on-disk table (lines 66–67 and 89–90); each insertion preserves the existing rows and adds exactly one row in alpha position. The OQ `concepts-index-table-vs-summary-membership-drift-two-missing-rows` is closed by this fix.
