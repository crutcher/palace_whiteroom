---
agent: layer-intro-author
invoked_at: 2026-06-03T143647Z
scope: Feature-Part by-kind reorg wave (PURE STRUCTURAL)
status: pending
integrated_at: 2026-06-03T153000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: |
  cycle-076 (batch-24 position 1/3, LEAD). Applied clean as D1 by integrator-per-report;
  finalized + committed by integrator-finalize. PURE-STRUCTURAL Feature-Part by-kind reorg:
  created book/src/feature/{spine-root,driver-leaf,output-product}.md group-intro pages,
  nested SUMMARY.md # Feature surfaces block into 3 by-kind groupings (spine-ROOT first /
  driver-leaf 5 alpha-within-kind / output-product 4 alpha-within-kind), re-sorted
  feature/index.md matrix with bold group-header rows, replaced the stale small-Part-guard
  prose line. within-column high->low exception preserved. ZERO count/status/citation/
  column-body changes (column-body-edit-scope gate = 0). cargo make book exit 0, linkcheck2
  clean, zero build-repair. Closes OQ feature-part-by-kind-nesting-output-product-cohort-grouping.
---

# CYCLE: Feature-surfaces Part by-kind reorg wave

## Summary

One-time PURE-STRUCTURAL reorg (cycle-071 layer-Part pattern) of the flat 10-column
`# Feature surfaces — entry points` Part into **3 by-kind sub-chapter groupings**, each
headed by a new group-intro page:

- **spine-ROOT (lifecycle)** — 1 column (lifecycle), nested FIRST (the spine reads top-down).
- **driver-leaf** — 5 columns, alpha-within-kind: driven, eigenmode, electrostatic, magnetostatic, transient.
- **output-product** — 4 columns, alpha-within-kind: capacitance, eigenfrequency-qfactor, inductance, sparameters.

**ZERO count/status/citation/body changes.** Deliverables: (1) 3 new group-intro pages
(`feature/spine-root.md`, `feature/driver-leaf.md`, `feature/output-product.md`); (2) SUMMARY.md
nested into the 3 groupings; (3) `feature/index.md` matrix re-sorted to the 3-grouping structure +
the stale "does not use by-kind nesting yet" line updated + the 3 group-intro pages wired into
the narrative. **Within each column the 3 level rows STAY high→low (L4 → L1 → L0)** — the deliberate
FEATURE-SURFACE exception is preserved everywhere; only the COLUMN order changes (alpha-within-kind),
never the level-row order.

**Grouping order choice:** spine-ROOT / driver-leaf / output-product (the spine reads top-down:
ROOT → drivers it dispatches → products those drivers feed). This matches the active-head listing
and CLAUDE.md §Extraction-goal ("the spine-ROOT grouping nests first"). I did NOT use plain alpha
order across the 3 group names, by design and per directive.

## Proposed changes

### 1. New file: `book/src/feature/spine-root.md`

Full content authored as `reports/2026-06-03T143647Z-layer-intro-author-feature-part-reorg-wave/spine-root.md`
(co-located in this report dir). Integrator: copy that file's content verbatim to
`book/src/feature/spine-root.md`.

### 2. New file: `book/src/feature/driver-leaf.md`

Full content authored as `reports/2026-06-03T143647Z-layer-intro-author-feature-part-reorg-wave/driver-leaf.md`.
Integrator: copy verbatim to `book/src/feature/driver-leaf.md`.

### 3. New file: `book/src/feature/output-product.md`

Full content authored as `reports/2026-06-03T143647Z-layer-intro-author-feature-part-reorg-wave/output-product.md`.
Integrator: copy verbatim to `book/src/feature/output-product.md`.

### 4. SUMMARY.md — nest the flat Feature Part into 3 groupings

```edit:book/src/SUMMARY.md
[old]:
# Feature surfaces — entry points
- [Overview](./feature/index.md)
- [electrostatic — L4 composition-root](./feature/electrostatic.L4.md)
- [electrostatic — L1 composition-root](./feature/electrostatic.L1.md)
- [electrostatic — L0 ground-truth surface](./feature/electrostatic.L0.md)
- [magnetostatic — L4 composition-root](./feature/magnetostatic.L4.md)
- [magnetostatic — L1 composition-root](./feature/magnetostatic.L1.md)
- [magnetostatic — L0 ground-truth surface](./feature/magnetostatic.L0.md)
- [driven — L4 composition-root](./feature/driven.L4.md)
- [driven — L1 composition-root](./feature/driven.L1.md)
- [driven — L0 ground-truth surface](./feature/driven.L0.md)
- [transient — L4 composition-root](./feature/transient.L4.md)
- [transient — L1 composition-root](./feature/transient.L1.md)
- [transient — L0 ground-truth surface](./feature/transient.L0.md)
- [eigenmode — L4 composition-root](./feature/eigenmode.L4.md)
- [eigenmode — L1 composition-root](./feature/eigenmode.L1.md)
- [eigenmode — L0 ground-truth surface](./feature/eigenmode.L0.md)
- [capacitance — L4 composition-root](./feature/capacitance.L4.md)
- [capacitance — L1 composition-root](./feature/capacitance.L1.md)
- [capacitance — L0 ground-truth surface](./feature/capacitance.L0.md)
- [eigenfrequency-qfactor — L4 composition-root](./feature/eigenfrequency-qfactor.L4.md)
- [eigenfrequency-qfactor — L1 composition-root](./feature/eigenfrequency-qfactor.L1.md)
- [eigenfrequency-qfactor — L0 ground-truth surface](./feature/eigenfrequency-qfactor.L0.md)
- [inductance — L4 composition-root](./feature/inductance.L4.md)
- [inductance — L1 composition-root](./feature/inductance.L1.md)
- [inductance — L0 ground-truth surface](./feature/inductance.L0.md)
- [sparameters — L4 composition-root](./feature/sparameters.L4.md)
- [sparameters — L1 composition-root](./feature/sparameters.L1.md)
- [sparameters — L0 ground-truth surface](./feature/sparameters.L0.md)
- [lifecycle — L4 composition-root](./feature/lifecycle.L4.md)
- [lifecycle — L1 composition-root](./feature/lifecycle.L1.md)
- [lifecycle — L0 ground-truth surface](./feature/lifecycle.L0.md)
[new]:
# Feature surfaces — entry points
- [Overview](./feature/index.md)
- [Spine ROOT (lifecycle)](./feature/spine-root.md)
  - [lifecycle — L4 composition-root](./feature/lifecycle.L4.md)
  - [lifecycle — L1 composition-root](./feature/lifecycle.L1.md)
  - [lifecycle — L0 ground-truth surface](./feature/lifecycle.L0.md)
- [Driver-leaf columns](./feature/driver-leaf.md)
  - [driven — L4 composition-root](./feature/driven.L4.md)
  - [driven — L1 composition-root](./feature/driven.L1.md)
  - [driven — L0 ground-truth surface](./feature/driven.L0.md)
  - [eigenmode — L4 composition-root](./feature/eigenmode.L4.md)
  - [eigenmode — L1 composition-root](./feature/eigenmode.L1.md)
  - [eigenmode — L0 ground-truth surface](./feature/eigenmode.L0.md)
  - [electrostatic — L4 composition-root](./feature/electrostatic.L4.md)
  - [electrostatic — L1 composition-root](./feature/electrostatic.L1.md)
  - [electrostatic — L0 ground-truth surface](./feature/electrostatic.L0.md)
  - [magnetostatic — L4 composition-root](./feature/magnetostatic.L4.md)
  - [magnetostatic — L1 composition-root](./feature/magnetostatic.L1.md)
  - [magnetostatic — L0 ground-truth surface](./feature/magnetostatic.L0.md)
  - [transient — L4 composition-root](./feature/transient.L4.md)
  - [transient — L1 composition-root](./feature/transient.L1.md)
  - [transient — L0 ground-truth surface](./feature/transient.L0.md)
- [Output-product columns](./feature/output-product.md)
  - [capacitance — L4 composition-root](./feature/capacitance.L4.md)
  - [capacitance — L1 composition-root](./feature/capacitance.L1.md)
  - [capacitance — L0 ground-truth surface](./feature/capacitance.L0.md)
  - [eigenfrequency-qfactor — L4 composition-root](./feature/eigenfrequency-qfactor.L4.md)
  - [eigenfrequency-qfactor — L1 composition-root](./feature/eigenfrequency-qfactor.L1.md)
  - [eigenfrequency-qfactor — L0 ground-truth surface](./feature/eigenfrequency-qfactor.L0.md)
  - [inductance — L4 composition-root](./feature/inductance.L4.md)
  - [inductance — L1 composition-root](./feature/inductance.L1.md)
  - [inductance — L0 ground-truth surface](./feature/inductance.L0.md)
  - [sparameters — L4 composition-root](./feature/sparameters.L4.md)
  - [sparameters — L1 composition-root](./feature/sparameters.L1.md)
  - [sparameters — L0 ground-truth surface](./feature/sparameters.L0.md)
```

### 5. feature/index.md — update the by-kind-nesting prose line

```edit:book/src/feature/index.md
[old]:
The within-column level ordering is **high→low** (L4 → L1 → L0), NOT alphabetized; the Feature Part does not use by-kind nesting yet (small-Part guard).
[new]:
The Feature Part is nested by kind into **three sub-chapter groupings** (directive-1 codification, batch-23 meta-phase) — [Spine ROOT (lifecycle)](./spine-root.md), [Driver-leaf columns](./driver-leaf.md), and [Output-product columns](./output-product.md) — each with its own group-intro page; the spine-ROOT grouping nests first (the spine reads top-down: ROOT → drivers it dispatches → products those drivers feed). Columns sort **alpha-within-each-kind** in the matrix below and in `SUMMARY.md`. The deliberate FEATURE-SURFACE exception is preserved: the within-column level ordering stays **high→low** (L4 → L1 → L0), NOT alphabetized.
```

### 6. feature/index.md — re-sort the matrix into the 3 groupings (alpha-within-kind)

```edit:book/src/feature/index.md
[old]:
| Feature | L4 (combinator composition) | L1 (pure-function composition) | L0 (cited driver source) |
|---|---|---|---|
| [electrostatic](./electrostatic.L4.md) | [L4 root](./electrostatic.L4.md) | [L1 root](./electrostatic.L1.md) | [L0 surface](./electrostatic.L0.md) |
| [magnetostatic](./magnetostatic.L4.md) | [L4 root](./magnetostatic.L4.md) | [L1 root](./magnetostatic.L1.md) | [L0 surface](./magnetostatic.L0.md) |
| [driven](./driven.L4.md) | [L4 root](./driven.L4.md) | [L1 root](./driven.L1.md) | [L0 surface](./driven.L0.md) |
| [transient](./transient.L4.md) | [L4 root](./transient.L4.md) | [L1 root](./transient.L1.md) | [L0 surface](./transient.L0.md) |
| [eigenmode](./eigenmode.L4.md) | [L4 root](./eigenmode.L4.md) | [L1 root](./eigenmode.L1.md) | [L0 surface](./eigenmode.L0.md) |
| *output products* | | | |
| [capacitance](./capacitance.L4.md) | [L4 root](./capacitance.L4.md) | [L1 root](./capacitance.L1.md) | [L0 surface](./capacitance.L0.md) |
| [eigenfrequency-qfactor](./eigenfrequency-qfactor.L4.md) | [L4 root](./eigenfrequency-qfactor.L4.md) | [L1 root](./eigenfrequency-qfactor.L1.md) | [L0 surface](./eigenfrequency-qfactor.L0.md) |
| [inductance](./inductance.L4.md) | [L4 root](./inductance.L4.md) | [L1 root](./inductance.L1.md) | [L0 surface](./inductance.L0.md) |
| [sparameters](./sparameters.L4.md) | [L4 root](./sparameters.L4.md) | [L1 root](./sparameters.L1.md) | [L0 surface](./sparameters.L0.md) |
| *spine ROOT* | | | |
| [lifecycle](./lifecycle.L4.md) | [L4 root](./lifecycle.L4.md) | [L1 root](./lifecycle.L1.md) | [L0 surface](./lifecycle.L0.md) |
[new]:
| Feature | L4 (combinator composition) | L1 (pure-function composition) | L0 (cited driver source) |
|---|---|---|---|
| **[Spine ROOT (lifecycle)](./spine-root.md)** | | | |
| [lifecycle](./lifecycle.L4.md) | [L4 root](./lifecycle.L4.md) | [L1 root](./lifecycle.L1.md) | [L0 surface](./lifecycle.L0.md) |
| **[Driver-leaf columns](./driver-leaf.md)** | | | |
| [driven](./driven.L4.md) | [L4 root](./driven.L4.md) | [L1 root](./driven.L1.md) | [L0 surface](./driven.L0.md) |
| [eigenmode](./eigenmode.L4.md) | [L4 root](./eigenmode.L4.md) | [L1 root](./eigenmode.L1.md) | [L0 surface](./eigenmode.L0.md) |
| [electrostatic](./electrostatic.L4.md) | [L4 root](./electrostatic.L4.md) | [L1 root](./electrostatic.L1.md) | [L0 surface](./electrostatic.L0.md) |
| [magnetostatic](./magnetostatic.L4.md) | [L4 root](./magnetostatic.L4.md) | [L1 root](./magnetostatic.L1.md) | [L0 surface](./magnetostatic.L0.md) |
| [transient](./transient.L4.md) | [L4 root](./transient.L4.md) | [L1 root](./transient.L1.md) | [L0 surface](./transient.L0.md) |
| **[Output-product columns](./output-product.md)** | | | |
| [capacitance](./capacitance.L4.md) | [L4 root](./capacitance.L4.md) | [L1 root](./capacitance.L1.md) | [L0 surface](./capacitance.L0.md) |
| [eigenfrequency-qfactor](./eigenfrequency-qfactor.L4.md) | [L4 root](./eigenfrequency-qfactor.L4.md) | [L1 root](./eigenfrequency-qfactor.L1.md) | [L0 surface](./eigenfrequency-qfactor.L0.md) |
| [inductance](./inductance.L4.md) | [L4 root](./inductance.L4.md) | [L1 root](./inductance.L1.md) | [L0 surface](./inductance.L0.md) |
| [sparameters](./sparameters.L4.md) | [L4 root](./sparameters.L4.md) | [L1 root](./sparameters.L1.md) | [L0 surface](./sparameters.L0.md) |
```

## Supporting evidence

- Flat Feature Part as of cycle-075: `book/src/SUMMARY.md:7-38` (Overview + 30 flat column-level entries, 10 columns × 3 levels).
- 10 columns confirmed on disk (`ls book/src/feature/`): capacitance, driven, eigenfrequency-qfactor, eigenmode, electrostatic, inductance, lifecycle, magnetostatic, sparameters, transient — 30 `.{L4,L1,L0}.md` files + index.md.
- The 3 group-intro slugs (`spine-root.md`, `driver-leaf.md`, `output-product.md`) verified ABSENT on disk before authoring.
- Group-intro convention mirrored from `book/src/L4/iteration-combinators-intro.md` (group-orientation prose + bulleted member list + alpha/ordering note).
- Spine framing + sub-kind taxonomy from `book/src/feature/index.md` and CLAUDE.md §Extraction-goal "FEATURE-SURFACE SPINE" (leaf feature column vs meta-feature/spine-ROOT sub-kinds; high→low within-column exception; spine-ROOT nests first).
- ZERO `## Status` lines touched; ZERO citations touched; ZERO column-chapter bodies touched. Lifecycle column confirmed `status: seed` (`feature/lifecycle.L4.md:5`) — unchanged.

## Open questions / caveats

- The matrix uses bold group-header rows (`**[Spine ROOT (lifecycle)](./spine-root.md)**`) in place of the prior `*output products*` / `*spine ROOT*` italic sub-headers — this keeps the single-table form (consistent with the prior matrix) while making the 3 groupings explicit and linking each to its group-intro. An alternative would be three separate tables; I kept one table to minimize structural churn in a pure-structural reorg.
- A 6th driver-leaf column (wave-port / boundary-mode) and a further output product (energy/field measurements) are noted as planned in both index.md narrative and the relevant group-intro pages; when each lands it inserts in alpha position within its kind grouping (not flat-appended) — recorded as routing guidance, no action this cycle.
