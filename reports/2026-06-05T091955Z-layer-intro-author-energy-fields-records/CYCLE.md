---
agent: layer-intro-author
invoked_at: 2026-06-05T091955Z
scope: energy-fields output-product column — config-record uses-record edge (closes OQ energy-fields-config-and-domaindata-records-need-concept-pages)
status: integrated
integrated_at: 2026-06-05T100000Z
integration_commit: 7417836
integration_notes: |
  Applied clean (cycle-105 D1, batch-33 position 3/3, BATCH-CLOSING). FOLD decision — no new concept page. Added the 12th-and-final `depends-on (kind: uses-record)` edge from `feature/energy-fields.L4` → `concepts/config-record` (PostprocessConfig is a read-only IoData sub-record projection) + reciprocal `reference` back-ref + a §Per-driver-specializations paragraph in config-record.md. ALL 12 config-input feature columns now carry the edge. Closes OQ `energy-fields-config-and-domaindata-records-need-concept-pages`. The output `Measurement::DomainData` record stays homed in-chapter under the single-consumer bar (OQ `record-DomainData-needs-definition-home` unchanged/orthogonal). Build EXIT 0; rank firm≤firm holds; citecheck energy-fields.L4 14 ok / config-record 31 ok.
---

# CYCLE: energy-fields config-record edge (FOLD decision)

## Summary

Cycle-105 D1 closes the last unlinked output-product feature column. In c104 the
`energy-fields` column was the ONE output-product column NOT given a
`uses-record → config-record` edge, because its signature
`energy_fields :: PostprocessConfig -> Field -> [DomainData]` names two records with no
concept page yet (OQ `energy-fields-config-and-domaindata-records-need-concept-pages`,
framed as "decide config-record-fold vs own page").

**DECISION: FOLD — no new pages.** On inspecting the L0 backing, neither named record
warrants its own concept page:

1. **`PostprocessConfig`** (the INPUT config in the signature) is the feature-column
   vocabulary name for the **energy-postprocess domain-attribute set**, whose L0 backing
   is the config sub-tree `config::DomainPostData` (`palace/utils/configfile.hpp:283-295`,
   holding `std::map<int, DomainEnergyData> energy` at `:290`, each
   `DomainEnergyData` carrying its per-index `attributes` list `:263-270`). This sub-record
   hangs off the `IoData` config tree: it is `config::DomainData.postpro : DomainPostData`
   (`configfile.hpp:322`), i.e. `IoData.domains.postpro.energy`. It is therefore a
   **sub-record of the `IoData` umbrella** that `concepts/config-record.md` already defines
   (that page's schema table already lists `domains : config::DomainData` at line 81). So
   the clean resolution is identical to the other 11 columns: edge to
   `concepts/config-record` (the umbrella IoData config home), and note the postprocess
   sub-records as covered. It is NOT a distinct data shape — it is a readonly
   construction-stratum projection of the config tree, exactly the per-driver-projection
   model `config-record.md` already documents.

2. **`DomainData`** (the OUTPUT `[DomainData]` element type) is **NOT a config record at
   all** — it is `Measurement::DomainData` (`palace/models/postoperatorcsv.hpp:74-79`:
   `{ int idx; double energy; double participation_ratio; }`), the per-domain energy
   **result row**, run-time / measurement stratum. It already has an in-chapter
   `## Record definition` section in `energy-fields.L4.md` (lines 90-113) and is a
   single-consumer record (this column only), correctly homed in-chapter per the
   ≥2-consumer bar. (The pre-existing OQ `record-DomainData-needs-definition-home` already
   tracks promoting it to a `concepts/` page ONLY IF the CSV-writer is authored as a 2nd
   consumer — unchanged by this dispatch.) Note the name collision: there are TWO unrelated
   `DomainData` structs — `config::DomainData` (config domains, `configfile.hpp:313-326`)
   and `Measurement::DomainData` (the energy result row); the signature's `[DomainData]` is
   the latter.

So `energy-fields` gets the same `uses-record → config-record` edge as its 4 sibling
output-product columns (capacitance / inductance / sparameters / eigenfrequency-qfactor),
matching the c104 convention exactly. No new files; no SUMMARY changes; both edge targets
already exist on disk, so the new edge resolves to a live target (build-safe).

## Proposed changes

### 1. `energy-fields.L4.md` — add the `uses-record → config-record` edge

The edge goes in the `depends-on` block (matching the sibling output-product columns, which
all place `uses-record` as a `depends-on` edge with a `kind: uses-record` comment naming the
input-signature record + "(the IoData surface)"). It is placed AFTER the existing
`cites-evidence` edges, mirroring sparameters/capacitance/eigenfrequency-qfactor.

```edit:book/src/feature/energy-fields.L4.md
[old]:
    - target: palace/models/postoperator.cpp:1021-1077
      kind: cites-evidence
    - target: palace/models/domainpostoperator.cpp:255-298
      kind: cites-evidence
  reference:
    - feature/electrostatic.L4
[new]:
    - target: palace/models/postoperator.cpp:1021-1077
      kind: cites-evidence
    - target: palace/models/domainpostoperator.cpp:255-298
      kind: cites-evidence
    - target: concepts/config-record
      kind: uses-record               # input signature: energy_fields :: PostprocessConfig -> Field -> [DomainData]; PostprocessConfig = the energy-postprocess domain set IoData.domains.postpro.energy (config::DomainPostData, configfile.hpp:283-295), a sub-record of the IoData config umbrella
  reference:
    - feature/electrostatic.L4
```

Add a one-line prose note in the `## Record definition` section's Inputs bullet so the prose
points at the umbrella page (matching the data-shape-home discipline — the column names the
record, the concept page defines it). The existing text already cites the L0 config home; this
adds the cross-link to the umbrella record-definition page:

```edit:book/src/feature/energy-fields.L4.md
[old]:
- **Input — config (the energy-postprocess domain set) + a solution field.** `PostprocessConfig`:
  the configured domain-attribute set that defines which domains get their own energy row (→ the
  `M_i` domain-restricted operators, the reduction's index domain), inherited from the simulation
  config. The **field** is supplied by the producing driver column (`V`/`E` for electric energy,
  `A`/`B` for magnetic). All `readonly` to this reduction. L0 home: the domain map `dom_post_op.M_i`
  (`postoperator.cpp:1028-1029`), the field selection `V ? *V : *E` (`:1032`) / `A ? *A : *B`
  (`:1057`).
[new]:
- **Input — config (the energy-postprocess domain set) + a solution field.** `PostprocessConfig`:
  the configured domain-attribute set that defines which domains get their own energy row (→ the
  `M_i` domain-restricted operators, the reduction's index domain), inherited from the simulation
  config. `PostprocessConfig` is **not a distinct data shape** — it is the energy-postprocess
  sub-record of the [`config-record`](../concepts/config-record.md) `IoData` umbrella
  (`IoData.domains.postpro.energy`, backed by `config::DomainPostData`,
  `palace/utils/configfile.hpp:283-295`, holding `std::map<int, DomainEnergyData> energy` at
  `:290`); see that page for the data-shape definition (this column defines only the *behaviour*
  over it). The **field** is supplied by the producing driver column (`V`/`E` for electric energy,
  `A`/`B` for magnetic). All `readonly` to this reduction. L0 home: the domain map `dom_post_op.M_i`
  (`postoperator.cpp:1028-1029`), the field selection `V ? *V : *E` (`:1032`) / `A ? *A : *B`
  (`:1057`).
```

### 2. `concepts/config-record.md` — add the reciprocal back-ref + note the postprocess sub-records

(a) Add `feature/energy-fields.L4` to the `reference:` edge list so the back-ref reciprocates
(matching the 11 existing feature-column back-refs). Alpha-placed among the feature references;
the existing list is ordered lifecycle → drivers → output-products, so it goes after
`feature/eigenfrequency-qfactor.L4` (the last output-product entry):

```edit:book/src/concepts/config-record.md
[old]:
    - feature/capacitance.L4
    - feature/inductance.L4
    - feature/sparameters.L4
    - feature/eigenfrequency-qfactor.L4
---
[new]:
    - feature/capacitance.L4
    - feature/inductance.L4
    - feature/sparameters.L4
    - feature/eigenfrequency-qfactor.L4
    - feature/energy-fields.L4
---
```

(b) Extend the `## Per-driver specializations` section's note to record that the
energy-postprocess config (`PostprocessConfig` in the feature vocabulary) is a sub-record
projection of the same `IoData` tree — so the umbrella page documents that it covers the
postprocess sub-records, not only the per-driver factory projections. This is added as a short
paragraph after the per-driver projection table's trailing paragraph:

```edit:book/src/concepts/config-record.md
[old]:
The projection is read-only and build-time: the factory consumes the relevant
fields once to build its operator, then the run-time iteration never touches
`iodata` again. This is exactly the construction/run-time split named in
[`build-time-vs-run-time-stratification`](./build-time-vs-run-time-stratification.md)
— config-record parsing + the per-driver factory reads are build-time
primitives; nothing in the config record is a run-time field.
[new]:
The projection is read-only and build-time: the factory consumes the relevant
fields once to build its operator, then the run-time iteration never touches
`iodata` again. This is exactly the construction/run-time split named in
[`build-time-vs-run-time-stratification`](./build-time-vs-run-time-stratification.md)
— config-record parsing + the per-driver factory reads are build-time
primitives; nothing in the config record is a run-time field.

The **postprocess sub-records are projections of the same `IoData` tree**, not
separate config records. The output-product feature columns (capacitance /
inductance / sparameters / eigenfrequency-qfactor / energy-fields) name a config
input in their signatures — e.g. the `energy-fields` column's `PostprocessConfig`
is the **energy-postprocess domain-attribute set** `IoData.domains.postpro.energy`
(backed by `config::DomainPostData`, `palace/utils/configfile.hpp:283-295`, a
`std::map<int, DomainEnergyData> energy` at `:290`, each `DomainEnergyData`
`:263-270` carrying its per-index `attributes` list). These are readonly
construction-stratum sub-records of `domains.postpro` (`config::DomainData.postpro`,
`configfile.hpp:322`), the same `IoData` umbrella this page defines — so an
output-product column's `uses-record` edge resolves here, to the umbrella, rather
than to a per-postprocess-record page. (NOTE the name collision: the config-side
`config::DomainData` — `configfile.hpp:313-326`, the domains record this page's
schema lists — is unrelated to the run-time `Measurement::DomainData` result row
`postoperatorcsv.hpp:74-79` that the `energy-fields` column's output `[DomainData]`
names; the latter is a measurement-stratum result row, homed in-chapter, not here.)
```

## Supporting evidence

- **Consumer column:** `book/src/feature/energy-fields.L4.md` — signature
  `energy_fields :: PostprocessConfig -> Field -> [DomainData]` (line 51, 109); the in-chapter
  `## Record definition` for the OUTPUT `Measurement::DomainData` result row (lines 90-113).
- **Umbrella record page:** `book/src/concepts/config-record.md` — the `IoData` config tree;
  schema already lists `domains : config::DomainData` (line 81); 11 sibling feature columns
  already in its `reference:` back-ref list (lines 14-23).
- **Sibling convention (matched exactly):** `sparameters.L4.md:17-18`, `capacitance.L4.md:13-14`,
  `eigenfrequency-qfactor.L4.md:15-16` — each carries
  `depends-on: target: concepts/config-record / kind: uses-record` with an input-signature
  comment + "(the IoData surface)".
- **L0 backing (all confirmed on-disk via palace-codemap `read_range` this dispatch):**
  - `config::DomainPostData` — `palace/utils/configfile.hpp:283-295` (the `energy` map at `:290`).
  - `config::DomainEnergyData` — `palace/utils/configfile.hpp:263-270` (per-index `attributes`).
  - `config::DomainData.postpro : DomainPostData` — `palace/utils/configfile.hpp:322` (the
    `IoData.domains.postpro` chain); the struct `configfile.hpp:313-326`.
  - `Measurement::DomainData` (the result row, NOT config) —
    `palace/models/postoperatorcsv.hpp:74-79`: `{ int idx; double energy; double participation_ratio; }`.

## Build-safety / wiring

- **No new files; no SUMMARY changes.** FOLD means the only new edge target is
  `concepts/config-record`, which already exists and is wired into `SUMMARY.md:304`. The
  reciprocal back-ref target `feature/energy-fields.L4` exists (`SUMMARY.md:41`). No dangling
  edge; HARD-gate-new satisfied vacuously (no new node).
- **`linkcheck2`-safe:** the one new prose markdown link added to `energy-fields.L4.md`
  (`../concepts/config-record.md`) resolves to an existing file; the reciprocal frontmatter
  `reference:` slug (`feature/energy-fields.L4`) resolves to an existing file. Frontmatter
  `edges:` slugs are not link-checked by `linkcheck2` but both resolve under the graded-stack
  slug convention (`book/src/<slug>.md`).
- **Graded-stack typing:** the new edge is correctly typed `depends-on` with documentation
  `kind: uses-record` — a record-definition page IS a DAG node (graded-stack-scheme §5), so a
  `uses-record` edge to it is a genuine blocking `depends-on` (the column's signature rests on
  the record's data shape), consistent with the 4 sibling output-product columns. `config-record`
  is `rank: firm`, and `energy-fields.L4` is `rank: firm`, so `rank(u=energy-fields) ≤ rank(v=config-record)`
  (3 ≤ 3) — the well-foundedness invariant holds, no rank violation introduced. The reciprocal
  `reference:` edge from `config-record` constrains nothing (navigational), correct for a
  record page named-by-use.

## Open questions / caveats

- The pre-existing OQ `record-DomainData-needs-definition-home` (in `energy-fields.L4.md:112`)
  is **unchanged** by this dispatch and correctly remains open: it tracks promoting the
  OUTPUT `Measurement::DomainData` result row to a `concepts/` page ONLY IF the CSV-writer
  (`postoperatorcsv`) is later authored as a 2nd consumer. This is orthogonal to the config-input
  FOLD decision here (it is a measurement-stratum result record, not a config record).
- OQ `energy-fields-config-and-domaindata-records-need-concept-pages` (from c104) is **closed by
  this dispatch**: decision recorded FOLD; `PostprocessConfig` is a sub-record of the
  `config-record` umbrella (no own page), and the output `DomainData` is the already-homed
  in-chapter result row (no own page). Integrator should mark it resolved in the OQ ledger.
- Name-collision flag (no action needed, documented in the config-record edit): `config::DomainData`
  (config domains) vs `Measurement::DomainData` (energy result row) are two unrelated structs
  sharing a name. The signature `[DomainData]` is the measurement result row; `PostprocessConfig`
  routes through `config::DomainData.postpro` but is NOT itself the `config::DomainData` struct.
  The config-record edit notes this collision so a future reader does not conflate them.
