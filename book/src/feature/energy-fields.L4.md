---
kind: feature-surface
feature: energy-fields
level: L4
feature_root: seed
rank: firm
edges:
  depends-on:
    - target: L4/domain_energy_reduce
      kind: folds
    - target: L1/participation_ratio
      kind: folds
    - target: L1/matrix-weighted-norm
      kind: folds
    - target: palace/models/postoperator.cpp:1021-1077
      kind: cites-evidence
    - target: palace/models/domainpostoperator.cpp:255-298
      kind: cites-evidence
    - target: concepts/config-record
      kind: uses-record               # input signature: energy_fields :: PostprocessConfig -> Field -> [DomainData]; PostprocessConfig = the energy-postprocess domain set IoData.domains.postpro.energy (config::DomainPostData, configfile.hpp:283-295), a sub-record of the IoData config umbrella
  reference:
    - feature/electrostatic.L4
---

# energy-fields — L4 composition-root (output product)

The **domain field-energy table** output product, presented at L4 as a single composition of L4
vocabulary — the **outward backend-lowering entry point** for "what the field-energy postprocess
computes." This chapter is an **output-product leaf feature column** (a composition root): inputs =
config (the energy-postprocess domain set); output = the physical product (the per-domain electric
+ magnetic field-energy table with participation ratios); body = the composition of the
`domain_energy_reduce` per-domain energy-table reduction over a
field-bearing driver column's solution field. It does **not** introduce new per-op algebra; it
wires existing L4 vocabulary into the user-facing output product and links DOWN to each composed
piece.

The domain energy table is the **output-product half** of every field-bearing driver: any driver
that produces a field grid function (`V`/`E` → electric energy, `A`/`B` → magnetic energy) feeds
the SAME per-domain energy reduction as its post-processing readout. Unlike the
[capacitance](./capacitance.L4.md) / [inductance](./inductance.L4.md) products (which reduce a
*solution family* to a rank-2 symmetric-Gram matrix via [`gram_reduce`](../L4/gram_reduce.md)) and
unlike [sparameters](./sparameters.L4.md) (a rank-2 port-projection), this product reduces a
*single solution field* to a **rank-1 per-domain scalar table** — the per-domain-table sibling of
the per-mode-table [eigenfrequency-qfactor](./eigenfrequency-qfactor.L4.md). This column is the
feature-surface view of that distinct reduction.

## The composition

At L4 the domain energy table is the composition (Haskell-style; the strawman
`book/src/semantics/index.md` notation):

    -- inputs = config (the energy-postprocess domain set); output = the domain energy table (the physical product)
    energy_fields :: PostprocessConfig -> Field -> [DomainData]
    energy_fields cfg field =
      let doms     = energy_domains cfg                        -- the configured domain-attribute set {idx → M_idx}
          e_total  = field_energy field                        -- the whole-domain energy ½⟨field, M field⟩  (the denominator)
      in  domain_energy_reduce doms field e_total              -- per domain: (energy_i = ½⟨field, M_i field⟩, p_i = energy_i / e_total)

One composed reduction stage, fed by a field-bearing driver column's solution field:

1. **A field-bearing driver column supplies the solution field** — e.g.
   [`electrostatic.L4`](./electrostatic.L4.md) (the potential `V` → `E`), or any driver that
   yields a field grid function (`magnetostatic` `A` → `B`; the `eigenmode`/`driven`/`transient`
   per-step fields). This output-product column **consumes** the field; it does not re-derive the
   solve (the driver column owns the solve, this column owns the reduction — the output-product /
   driver split the FEATURE-SURFACE SPINE encodes). The energy table is driver-agnostic: it is the
   SAME per-domain reduction regardless of which driver produced the field, which is why it is a
   standalone output-product column rather than a per-driver stage-3. L0: the field is whichever of
   `V`/`E`/`A`/`B` the solver populated (`postoperator.cpp:1032, 1057`).

2. **The per-domain energy-table reduction** — [`domain_energy_reduce`](../L4/domain_energy_reduce.md)
   (**firm**). The L4 per-domain energy-table reduction combinator
   `domain_energy_reduce doms field e_total` maps each configured domain attribute `idx` to its
   `DomainData` row: the **per-domain energy** `energyᵢ = ½⟨field, M_idx field⟩` (the
   domain-restricted SPD energy form — the [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)
   squared radicand `⟨x, B x⟩` with `B = M_idx` the operator restricted to one domain attribute),
   and the **participation ratio** `pᵢ = energyᵢ / e_total` (the firm
   [`participation_ratio`](../L1/participation_ratio.md) with the per-domain energy numerator over
   the whole-domain total). This is a pure per-domain `map`-then-collect over the configured domain
   set — no inter-domain state, no `Solve` effect (a post-processing readout, like the eigenmode
   `(f,Q)` readout). The reduction runs **twice** — once for the electric field, once for the
   magnetic field — producing two tables (`domain_E_field_energy_i`, `domain_H_field_energy_i`),
   the field-kind being the load-bearing variant axis. L0: the per-domain electric loop
   `postoperator.cpp:1036-1042`, the per-domain magnetic loop `:1061-1066`; the energy form
   `domainpostoperator.cpp:255-275` (electric) / `:277-298` (magnetic).

The whole-domain totals `e_total` (`GetElectricFieldEnergy` / `GetMagneticFieldEnergy`,
`postoperator.cpp:1033, 1058`) are the un-restricted energy form (the same
[`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)-squared over the full operator), supplied
as the denominator — they are the field's total energy, NOT part of the per-domain map.

## Record definition

`Measurement::DomainData` — the per-domain energy-table result row (the output product's element
type).

| field | type | meaning |
|---|---|---|
| `idx` | `int` | the domain attribute index (the `M_i` map key — which configured domain this row reports) |
| `energy` | `double` | the per-domain field energy `energyᵢ = ½⟨field, M_idx field⟩` (real-valued; electric `½⟨E,M_iE⟩` or magnetic `½⟨B,M_iB⟩` depending on which table) |
| `participation_ratio` | `double` | the dimensionless per-domain participation `pᵢ = energyᵢ / e_total` (zeroed when the numerator energy is `0`) |

- **Stratum.** All three fields are **run-time / measurement** stratum (computed per readout from the
  solved field), NOT construction-time config. `idx` mirrors the construction-time domain-attribute
  configuration but the row itself is materialized during the energy measurement.
- **L0 source home.** The backing C++ struct is `Measurement::DomainData`
  (`palace/models/postoperatorcsv.hpp:74-79`): `{ int idx; double energy; double participation_ratio; }`.
  It is emitted in `MeasureDomainFieldEnergy` (`postoperator.cpp:1040-1041` electric,
  `:1065-1066` magnetic) into the measurement-cache vectors `domain_E_field_energy_i` /
  `domain_H_field_energy_i`.
- **Signatures that name it.** `energy_fields :: PostprocessConfig -> Field -> [DomainData]` (this
  column, L4/L1); the reduction verb `domain_energy_reduce` result
  element. Currently a single-consumer record (this column); if the CSV-writer (`postoperatorcsv`)
  becomes a 2nd consumer it promotes to a `concepts/` record-definition page.

## Inputs / outputs (the feature surface)

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
- **Output — the physical product.** Two per-domain `[DomainData]` tables — `domain_E_field_energy_i`
  (electric) and `domain_H_field_energy_i` (magnetic) — each row carrying the per-domain energy and
  participation ratio, plus the whole-domain totals `domain_E_field_energy_all` /
  `domain_H_field_energy_all`. This IS what the user runs to inspect where field energy concentrates.
  L0 home: the cache vectors set at `postoperator.cpp:1040-1041, 1065-1066`; the totals `:1034, 1059`.

## Why this is a distinct output-product column (rank-1 per-domain table, not Gram)

The energy table is the **per-domain-table sibling** of the
[eigenfrequency-qfactor](./eigenfrequency-qfactor.L4.md) per-mode table — both are rank-1
scalar-table reductions, distinct from the rank-2 Gram ([capacitance](./capacitance.L4.md) /
[inductance](./inductance.L4.md)) and rank-2 port-projection ([sparameters](./sparameters.L4.md))
products:

- The upstream is a **single solution field**, not a solution family — there is no family-PAIR
  `xⱼᵀ K xᵢ` bilinear, no `symmetric_from_upper` (the load-bearing distinction from `gram_reduce`;
  the do-NOT-over-unify guard).
- The reduction is [`domain_energy_reduce`](../L4/domain_energy_reduce.md) (**firm**), a **per-domain scalar
  map** folding two scalar projections per domain: the domain-restricted energy form
  (`matrix-weighted-norm`-squared, **firm**) and the participation ratio (firm
  [`participation_ratio`](../L1/participation_ratio.md)).
- The reduction is driver-agnostic — the SAME per-domain energy table reduces any field-bearing
  driver's field, which is why it is its own output-product column rather than a per-driver
  stage-3.

The whole output product therefore lowers cleanly outward to the L4 backend surface:
`energy_fields = domain_energy_reduce (doms, e_total) ∘ driver_field` — a one-reduction tail on a
field-bearing driver column. Under the **OWN-COMPOSITION rule** a column promotes off `seed` when
its OWN directly-owned constituents are firm; this column is **firm** because its OWN composition is
all-firm: its OWN reduce verb [`domain_energy_reduce`](../L4/domain_energy_reduce.md), its OWN folded
domain-restricted energy form [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md), and the
[`participation_ratio`](../L1/participation_ratio.md) half — all three directly-owned constituents
firm. The field-bearing driver columns are SIBLING references, NOT blockers — energy-fields is
driver-agnostic (a shared postprocess all field-bearing drivers point at).

## Constituent down-links

| Stage | L4 constituent | Status | L0 site |
|---|---|---|---|
| producing field (any field-bearing driver) | [`electrostatic.L4`](./electrostatic.L4.md) / [`magnetostatic.L4`](./magnetostatic.L4.md) / … | firm | `postoperator.cpp:1032, 1057` |
| per-domain energy-table reduction | [`domain_energy_reduce`](../L4/domain_energy_reduce.md) | firm | `postoperator.cpp:1036-1042, 1061-1066` |
| per-domain energy form (folded) | [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)-squared (domain-restricted `M_i`) | firm | `domainpostoperator.cpp:255-275, 277-298` |
| participation ratio (folded) | [`participation_ratio`](../L1/participation_ratio.md) | firm | `postoperator.cpp:1039, 1064` |

## Promotion basis

An output-product **leaf feature column**: the rank-1 **per-domain**-table sibling of the rank-1
per-mode-table [eigenfrequency-qfactor](./eigenfrequency-qfactor.L4.md) and the rank-2
Gram/port-projection products [capacitance](./capacitance.L4.md) / [inductance](./inductance.L4.md) /
[sparameters](./sparameters.L4.md). Under the OWN-COMPOSITION rule (a column is firm when its OWN
composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT
blockers), this column is firm: its OWN reduce verb `domain_energy_reduce`, its OWN folded
domain-restricted energy form `matrix-weighted-norm`, and the `participation_ratio` half are all
firm. The field-bearing driver columns are SIBLING references (a driver-agnostic shared
postprocess), NOT blockers. This chapter carries the *compositional* claim (the domain energy table
= the per-domain energy reduction over a field-bearing driver's field), NOT the constituents' per-op
algebraic claims (those live in the linked chapters). The defining structural fact: a rank-1
per-domain scalar table, NOT a `gram_reduce` family-PAIR grid (do-NOT-over-unify). Evidence:
`MeasureDomainFieldEnergy` (`postoperator.cpp:1021-1077`) + the energy form
(`domainpostoperator.cpp:255-298`), plus the constituent down-links.
