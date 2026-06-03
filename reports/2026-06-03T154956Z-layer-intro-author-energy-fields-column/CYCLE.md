---
agent: layer-intro-author
invoked_at: 2026-06-03T154956Z
scope: energy-fields output-product feature column (5th-of-5) + shared feature/index + SUMMARY cohort-owner for energy-fields + boundary-mode
status: pending
integrated_at: 2026-06-03T160000Z
integration_commit: dcfb41e
integration_notes: |
  Applied cycle-078 (batch-24 position 3/3, THIRD/FINAL). The FINAL output-product feature
  column energy-fields (output-product cohort 4->5, status seed, alpha-within-kind between
  eigenfrequency-qfactor and inductance) + COHORT-OWNER of the shared feature/index.md matrix
  + SUMMARY.md rows for BOTH new columns this cycle (energy-fields + boundary-mode). The minted
  domain_energy_reduce L4 verb is referenced as plain-text code-spans only (verb file NOT
  authored -- follow-up OQ domain_energy_reduce-l4-verb-needs-authoring); CRITICAL build check
  confirmed ZERO live link to the non-existent book/src/L4/domain_energy_reduce.md. energy-fields
  is driver-AGNOSTIC (breaks the 1:1 output-product<->driver convention -- OQ for the meta-phase).
  Consistency touch applied to the "one reduction verb each" prose. NO firm-count change (seed
  column). cargo make book exit 0, linkcheck2 clean, zero build-repair. Build-relevant: yes.
---

# CYCLE: energy-fields output-product feature column (+ shared-surface cohort owner)

## Summary

Authors the NEW **energy-fields** output-product feature column — the 5th-of-5 output-product
column, status `seed` — at all three levels (`book/src/feature/energy-fields.{L4,L1,L0}.md`),
landing in the **output-product** by-kind grouping at the alpha-within-kind position (between
`eigenfrequency-qfactor` and `inductance`).

The physical product is the **domain field-energy table**: per-domain electric + magnetic field
energies and per-domain participation ratios (`energy_i / energy_all`). The reduction composes
the **firm** L1 [`participation_ratio`](../../book/src/L1/participation_ratio.md) (the
`energy_i/E_total` ratio, firmed c077 D4) over the per-domain SPD energy-form
`Eᵢ = ½⟨field, M_i field⟩` (the rough-in
[`matrix-weighted-norm`](../../book/src/L1/matrix-weighted-norm.md)-squared radicand restricted
to one domain attribute).

**Author judgment (L4 verb):** I mint a **thin per-column reduction verb**
`domain_energy_reduce` (`rough-in`) rather than inlining. Rationale: this names a *genuinely
distinct reduction shape* — a per-domain **scalar TABLE** (per domain: restrict-energy +
participation-ratio), the rank-1 per-entry-table sibling of `eigenfreq_qfactor_reduce` (which is
per-MODE) and structurally NOT a `gram_reduce` family-PAIR grid. The verb does NOT add vocabulary
without simplifying: it factors the per-domain restriction + ratio into one fold that composes the
firm `participation_ratio` building block, exactly as the cohort's other reduce-verbs factor their
folds (verb-per-column symmetry the redirect permits when the verb names a real shift). It is NOT
a `gram_reduce` weight specialization (no family-PAIR bilinear) — the c074 D6 do-NOT-over-unify
guard is honored.

The column stays `seed` because a composed constituent (the per-domain energy-form, via
`matrix-weighted-norm` rough-in, and the freshly-minted `domain_energy_reduce` verb) is not firm —
a feature column may promote past `seed` only once ALL composed constituents are firm.

**Record-definition obligation:** the column references `Measurement::DomainData`
(`{ int idx; double energy; double participation_ratio; }`,
`palace/models/postoperatorcsv.hpp:74-79`). Author judgment: it is the per-domain result carrier
used by THIS column's measurement only (both the E-field and H-field loops emit it, but both loops
are inside the single `MeasureDomainFieldEnergy` this column maps) — currently a **single-consumer**
record. I give it an in-chapter `## Record definition` section in `energy-fields.L4.md` (the
single-consumer home), and ALSO flag `record-DomainData-needs-definition-home` in
`scaffolding/open-questions.md` so a future cross-cutter can confirm whether the CSV-writer
(`postoperatorcsv`) or another postprocess chapter becomes a 2nd consumer (→ promote to a
`concepts/` page).

**Cohort-owner (parallel-blind-shared-index guard, c074/c075 precedent):** I SOLE-own the shared
`feature/index.md` matrix + the `book/src/SUMMARY.md` `# Feature surfaces` block for BOTH new
columns this cycle — adding the energy-fields rows (output-product grouping, alpha) AND the
boundary-mode rows (driver-leaf grouping, alpha-FIRST before `driven`). D2 (boundary-mode) DEFERS
its index/SUMMARY rows to me. I also update the `feature/index.md` line-54 "Still planned" prose
and add my OWN energy-fields bullet to the `feature/output-product.md` group-intro. I do NOT author
the boundary-mode group-intro bullet (driver-leaf.md) — that is D2's own (1)+(2), not the
count-owner's (3).

## Supporting evidence

**L0 ground-truth, self-verified on-disk this dispatch via palace-codemap `read_range`:**
- `palace/models/postoperator.cpp:1021` — `PostOperator<solver_t>::MeasureDomainFieldEnergy()` def
  (confirmed `search_text`).
- `palace/models/postoperator.cpp:1022-1079` — the body: E-field per-domain loop
  (`:1036-1042`, with `GetElectricFieldEnergy` total at `:1033`, per-domain
  `GetDomainElectricFieldEnergy` at `:1038` + `participation_ratio = energy_i/energy` at `:1039`,
  `Measurement::DomainData{idx, energy_i, participation_ratio}` emit at `:1040-1041`), and the
  H-field per-domain loop (`:1061-1066`, total `GetMagneticFieldEnergy` at `:1058`, per-domain
  `GetDomainMagneticFieldEnergy` at `:1063`, ratio `:1064`, emit `:1065-1066`). Verified the
  E-only / H-only `else` branches emit zero-DomainData (`:1044-1053`, `:1069-1078`).
- `palace/models/domainpostoperator.cpp:255-275` — `DomainPostOperator::GetDomainElectricFieldEnergy`
  (confirmed `search_text` def at `:255`): the SPD energy form `0.5 * dot` where
  `dot = LocalDot(E.Real(), M_i·E.Real())` (+ imag part), i.e. `½⟨E, M_i E⟩` over one domain
  attribute. The magnetic sibling `GetDomainMagneticFieldEnergy` is `:277-298`, same `½⟨B, M_i B⟩`
  shape.
- `palace/models/postoperatorcsv.hpp:74-79` — `Measurement::DomainData` struct
  `{ int idx; double energy; double participation_ratio; }` (read on-disk this dispatch).

**Composed constituents:**
- FIRM: `book/src/L1/participation_ratio.md` (`firmness: firm`, c077 D4) — the `energy_i/E_total`
  ratio that the per-domain reduce folds; §"Downward to L0" explicitly names the
  `energy-fields-output-product-column` as the home for the domain energy-readout vocabulary.
- ROUGH-IN: `book/src/L1/matrix-weighted-norm.md` (`rough-in (test-coverage-bounded)`,
  confirmed `## Status` on-disk this dispatch) — the `√(xᴴ B x)` whose squared radicand
  `⟨x, B x⟩` is the per-domain energy form (here weighted by the domain-restricted operator `M_i`).
- NEW rough-in verb: `book/src/L4/domain_energy_reduce.md` (minted this cycle, NOT authored here —
  flagged as a forward-reference rough-in; the L4 chapter's down-link uses plain-text per the
  rough-in-rows-must-be-plain-text convention since the anchor file does not yet exist).

**Sibling exemplars mirrored (structure):** `book/src/feature/eigenfrequency-qfactor.{L4,L1,L0}.md`
(the rank-1 scalar-table output-product, closest structural sibling — per-entry-table, not Gram),
`book/src/feature/inductance.L4.md` (the output-product column shape + cross-link convention).

## Proposed changes

### New file 1 of 3 — the L4 composition root

```new:book/src/feature/energy-fields.L4.md
---
kind: feature-surface
feature: energy-fields
level: L4
status: seed
composes:
  - book/src/feature/electrostatic.L4.md (seed — a producing driver column: supplies the field family the energy table reduces; any field-bearing driver feeds it)
  - book/src/L4/domain_energy_reduce.md (rough-in — the per-domain energy-table reduction verb, minted cycle-078)
  - book/src/L1/participation_ratio.md (firm — the energy_i/E_total per-domain ratio the reduction folds)
  - book/src/L1/matrix-weighted-norm.md (rough-in (test-coverage-bounded) — the ½⟨field,M_i field⟩ per-domain energy form, squared radicand restricted to one domain attribute)
l0_ground_truth:
  - palace/models/postoperator.cpp:1021-1077 (PostOperator::MeasureDomainFieldEnergy — the per-domain energy + participation table)
  - palace/models/domainpostoperator.cpp:255-298 (GetDomainElectricFieldEnergy / GetDomainMagneticFieldEnergy — the ½⟨field,M_i field⟩ energy form)
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
`book/src/design/l4_calculus.md` notation):

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

2. **The per-domain energy-table reduction** — `domain_energy_reduce`
   (**rough-in**, minted cycle-078). The L4 per-domain energy-table reduction combinator
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
  element. Currently a single-consumer record (this column); flagged for cross-cutter re-check
  (OQ `record-DomainData-needs-definition-home`) in case the CSV-writer (`postoperatorcsv`) is
  authored as a 2nd consumer (→ promote to a `concepts/` record-definition page).

## Inputs / outputs (the feature surface)

- **Input — config (the energy-postprocess domain set) + a solution field.** `PostprocessConfig`:
  the configured domain-attribute set that defines which domains get their own energy row (→ the
  `M_i` domain-restricted operators, the reduction's index domain), inherited from the simulation
  config. The **field** is supplied by the producing driver column (`V`/`E` for electric energy,
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
  the c074 D6 do-NOT-over-unify guard, honored).
- The reduction is `domain_energy_reduce`, a **per-domain scalar
  map** folding two scalar projections per domain: the domain-restricted energy form
  (`matrix-weighted-norm`-squared, rough-in) and the participation ratio (firm
  [`participation_ratio`](../L1/participation_ratio.md)).
- The reduction is driver-agnostic — the SAME per-domain energy table reduces any field-bearing
  driver's field, which is why it is its own output-product column rather than a per-driver
  stage-3.

The whole output product therefore lowers cleanly outward to the L4 backend surface:
`energy_fields = domain_energy_reduce (doms, e_total) ∘ driver_field` — a one-reduction tail on a
field-bearing driver column. The column is `seed` (not promoted past it) because
`domain_energy_reduce` is `rough-in` (newly minted) and its
domain-restricted energy form is the [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)
`rough-in (test-coverage-bounded)` primitive — a feature column may promote past `seed` only once
ALL its composed constituents are firm (the firm [`participation_ratio`](../L1/participation_ratio.md)
half is necessary but not sufficient).

## Constituent down-links

| Stage | L4 constituent | Status | L0 site |
|---|---|---|---|
| producing field (any field-bearing driver) | [`electrostatic.L4`](./electrostatic.L4.md) / [`magnetostatic.L4`](./magnetostatic.L4.md) / … | seed | `postoperator.cpp:1032, 1057` |
| per-domain energy-table reduction | domain_energy_reduce *(rough-in; no anchor yet)* | rough-in | `postoperator.cpp:1036-1042, 1061-1066` |
| per-domain energy form (folded) | [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)-squared (domain-restricted `M_i`) | rough-in (test-coverage-bounded) | `domainpostoperator.cpp:255-275, 277-298` |
| participation ratio (folded) | [`participation_ratio`](../L1/participation_ratio.md) | firm | `postoperator.cpp:1039, 1064` |

## Status

`seed` — an output-product **leaf feature column** authored under the FEATURE-SURFACE SPINE
directive (2026-06-02), the rank-1 **per-domain**-table sibling of the rank-1 per-mode-table
[eigenfrequency-qfactor](./eigenfrequency-qfactor.L4.md) and the rank-2 Gram/port-projection
products [capacitance](./capacitance.L4.md) / [inductance](./inductance.L4.md) /
[sparameters](./sparameters.L4.md). The composition is sound: a field-bearing driver column
supplies the solution field; the `domain_energy_reduce` reduction
maps each configured domain to its `(energyᵢ, pᵢ)` row, folding the domain-restricted energy form
([`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)-squared) and the firm
[`participation_ratio`](../L1/participation_ratio.md). The column stays `seed` because
`domain_energy_reduce` is `rough-in` (newly minted) and its domain-restricted energy form is the
`matrix-weighted-norm` `rough-in (test-coverage-bounded)` primitive — a feature column may promote
past `seed` only once ALL composed constituents are firm. This chapter carries the *compositional*
claim (the domain energy table = the per-domain energy reduction over a field-bearing driver's
field), NOT the constituents' per-op algebraic claims (those live in the linked chapters). The
defining structural fact: a rank-1 per-domain scalar table, NOT a `gram_reduce` family-PAIR grid
(c074 D6 do-NOT-over-unify, honored). Evidence: `MeasureDomainFieldEnergy`
(`postoperator.cpp:1021-1077`) + the energy form (`domainpostoperator.cpp:255-298`), all anchors
confirmed on-disk via palace-codemap `read_range`/`search_text` this dispatch, plus the
constituent down-links.
```

### New file 2 of 3 — the L1 composition root

```new:book/src/feature/energy-fields.L1.md
---
kind: feature-surface
feature: energy-fields
level: L1
status: seed
composes:
  - book/src/feature/electrostatic.L1.md (seed — a producing driver column: supplies the solution field the energy table reduces)
  - book/src/L1/participation_ratio.md (firm — the energy_i/E_total per-domain ratio)
  - book/src/L1/matrix-weighted-norm.md (rough-in (test-coverage-bounded) — the ½⟨field,M_i field⟩ per-domain energy form)
l0_ground_truth:
  - palace/models/postoperator.cpp:1021-1077 (PostOperator::MeasureDomainFieldEnergy — the per-domain energy + participation table)
  - palace/models/domainpostoperator.cpp:255-298 (GetDomainElectricFieldEnergy / GetDomainMagneticFieldEnergy — the ½⟨field,M_i field⟩ energy form)
---

# energy-fields — L1 composition-root (output product)

The **domain field-energy table** output product, presented at L1 as a pure-function composition
of L1 operations. This is the **pure-function feature surface** of the output-product sub-kind:
the same composition root as the [L4 chapter](./energy-fields.L4.md), but expressed in L1
vocabulary (an explicit per-domain pure readout, no L4 combinator naming) — the form a reader
navigating L1 sees when asking "what whole product does this per-domain energy readout add up to?"

At L1 the energy table is a pure function `(config, field) → [DomainData]`: it consumes a solution
field produced by a field-bearing driver column (the [`electrostatic.L1`](./electrostatic.L1.md)
potential, or any field-bearing driver), computes the whole-domain total energy, then maps each
configured domain to its per-domain energy + participation row (the **mutation already lifted** —
the L0 in-place `measurement_cache.domain_E_field_energy_i.emplace_back(...)` accumulation is
lifted to a value-returning per-domain map per the L1>L0 mutation rotation).

## The composition

    -- inputs = config + a solution field; output = the per-domain energy table (the physical product)
    energy_fields :: PostprocessConfig -> Field -> [DomainData]
    energy_fields cfg field =
      let doms    = energy_domains cfg                              -- the configured domain-attribute set {idx → M_idx}
          e_total = matrix_weighted_norm_sq field full_operator     -- the whole-domain energy ½⟨field, M field⟩ (the denominator)
      in  [ let energy_i = matrix_weighted_norm_sq field (M doms idx)   -- ½⟨field, M_idx field⟩ (domain-restricted)
                p_i      = if energy_i > 0 then participation_ratio energy_i e_total else 0   -- energy_i / e_total
            in  DomainData { idx, energy: energy_i, participation_ratio: p_i }                -- per-domain row
          | idx <- domain_indices doms ]                                                      -- map over configured domains (no inter-domain state)

1. **A field-bearing driver column supplies the solution field** —
   [`electrostatic.L1`](./electrostatic.L1.md) (**seed**, the potential `V` → `E`), or any driver
   yielding a field grid function. This output-product column **consumes** the field; it does not
   re-derive the solve. The reduction is driver-agnostic (the SAME per-domain readout regardless of
   producer). L0: the field selection `auto &field = V ? *V : *E` (`postoperator.cpp:1032`) for the
   electric energy, `A ? *A : *B` (`:1057`) for the magnetic.

2. **The per-domain pure readout → the energy table** — a pure list comprehension over the
   configured domain-attribute set, mapping each domain to its `DomainData` row:
   - the per-domain energy `energyᵢ = ½⟨field, M_idx field⟩`, the domain-restricted SPD energy form
     (the [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) squared radicand `⟨x, B x⟩` with
     `B = M_idx`). L0: `GetDomainElectricFieldEnergy` returns `0.5 * dot` where
     `dot = LocalDot(E.Real(), M_i·E.Real())` + imag (`domainpostoperator.cpp:255-275`); the
     magnetic sibling `:277-298`.
   - the participation ratio `pᵢ = energyᵢ / e_total` (the firm
     [`participation_ratio`](../L1/participation_ratio.md), zeroed when `energyᵢ = 0`). L0:
     `participation_ratio = std::abs(energy_i) > 0.0 ? energy_i / energy : 0.0`
     (`postoperator.cpp:1039` electric, `:1064` magnetic).
   This stage is a pure per-domain map — no inter-domain state, no solve-iteration. At L4 this exact
   per-domain reduction is named the `domain_energy_reduce`
   combinator (the reduce-to-per-domain-scalar-table member of the L4 algebra-of-folds); L1 sees the
   unfolded per-domain comprehension. The readout runs twice (electric + magnetic), the field-kind
   the load-bearing variant axis.

## Record definition

The per-domain row is `Measurement::DomainData`
(`{ idx: int, energy: double, participation_ratio: double }`,
`palace/models/postoperatorcsv.hpp:74-79`). The full fielded schema — field types, meaning,
construction-vs-run-time stratum, L0 source home, and the signatures that name it — is in the
[L4 chapter's `## Record definition`](./energy-fields.L4.md#record-definition) (the single home;
not duplicated here per the data-shape-defined-once discipline).

## Inputs / outputs (the feature surface)

- **Input — config + a solution field.** `PostprocessConfig` (the configured domain-attribute set →
  the `M_i` domain-restricted operators, the reduction's index domain) + the **field** supplied by
  the producing driver column (`V`/`E` electric, `A`/`B` magnetic). All read-only.
- **Output — the physical product.** Two per-domain `[DomainData]` tables (electric + magnetic),
  each row carrying the per-domain energy `energyᵢ` and participation ratio `pᵢ`, plus the
  whole-domain totals. L0: the cache vectors set at `postoperator.cpp:1040-1041, 1065-1066`; the
  totals `:1034, 1059`.

## L1 vs L4

The L1 and L4 composition roots express the **same output product**; they differ in vocabulary:
- **L1** (this chapter): the reduction is an explicit per-domain pure list comprehension — the
  domain-restricted energy form + the participation quotient, written out per domain.
- **L4** ([`energy-fields.L4`](./energy-fields.L4.md)): the whole per-domain reduction is the
  `domain_energy_reduce` combinator (the per-domain map + energy
  form + participation closure made *structural*). The L4 form is the one the outward backend
  consumes; the L1 form is the pure-function decomposition the L4 combinator names.

The defining structural fact at both levels: a **rank-1 per-domain scalar-ratio table**, NOT a
rank-2 family-PAIR Gram grid — distinct from the capacitance / inductance output products (c074 D6
do-NOT-over-unify), and the per-domain sibling of the per-mode
[eigenfrequency-qfactor](./eigenfrequency-qfactor.L1.md) table. The L1→L0 direction (how the
per-domain readout lowers to the in-place `emplace_back(DomainData{...})` cache accumulation) is the
per-operator L1>L0 mutation-rotation of the readout; this composition root records only the L1
composition (high→low discipline).

## Constituent down-links

| Stage | L1 constituent | Status | L0 site |
|---|---|---|---|
| producing field (field-bearing driver) | [`electrostatic.L1`](./electrostatic.L1.md) (driver feature column) | seed | `postoperator.cpp:1032, 1057` |
| per-domain energy form | [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)-squared (domain-restricted `M_i`) | rough-in (test-coverage-bounded) | `domainpostoperator.cpp:255-275, 277-298` |
| participation ratio | [`participation_ratio`](../L1/participation_ratio.md) | firm | `postoperator.cpp:1039, 1064` |

## Status

`seed` — the L1 pure-function composition root for the domain field-energy table output product
(the output-product **leaf feature column**), authored under the FEATURE-SURFACE SPINE directive
(2026-06-02), the L1 counterpart of the [energy-fields.L4](./energy-fields.L4.md) composition root.
It consumes a field-bearing driver column's solution field, then maps each configured domain to its
`(energyᵢ, pᵢ)` row (the domain-restricted energy form + the participation ratio). The reduction's
L4 home `domain_energy_reduce` is `rough-in` and its domain energy
form is the `matrix-weighted-norm` `rough-in (test-coverage-bounded)` primitive (only the
[`participation_ratio`](../L1/participation_ratio.md) half is firm) — consistent with the column
being `seed`, not a firm composition. The chapter carries the compositional claim only; per-op
algebraic claims live in the linked chapters. The defining structural fact carried from L4: a
rank-1 per-domain scalar table, NOT a `gram_reduce` family-PAIR grid (c074 D6). Evidence: the L0
energy-table ranges `postoperator.cpp:1021-1077` + the energy form `domainpostoperator.cpp:255-298`,
confirmed on-disk this dispatch, plus the constituent down-links.
```

### New file 3 of 3 — the L0 ground-truth surface

```new:book/src/feature/energy-fields.L0.md
---
kind: feature-surface
feature: energy-fields
level: L0
status: seed
l0_ground_truth:
  - palace/models/postoperator.cpp:1021-1077 (PostOperator::MeasureDomainFieldEnergy — the per-domain energy + participation table)
  - palace/models/domainpostoperator.cpp:255-298 (GetDomainElectricFieldEnergy / GetDomainMagneticFieldEnergy — the ½⟨field,M_i field⟩ energy form)
lifts_to:
  - book/src/feature/energy-fields.L1.md (the L1 pure-function composition root)
---

# energy-fields — L0 ground-truth surface

The **domain field-energy table** output product at L0: the cited Palace source that realizes the
per-domain energy reduction composition root, with the per-stage source ranges that the L1 / L4
feature chapters lift. This is the ground-truth surface — every claim is a `(file:start-end)`
citation into `palace/models/postoperator.cpp` (the per-domain table) and
`palace/models/domainpostoperator.cpp` (the energy form).

The domain energy reduction lives in `PostOperator<solver_t>::MeasureDomainFieldEnergy()`
(`palace/models/postoperator.cpp:1021`, body `:1022-1079`): a per-domain map over the configured
domain-attribute set `dom_post_op.M_i`, run once for the electric field and once for the magnetic
field. It is the **output-product** readout that any field-bearing driver feeds — driver-agnostic,
reducing a single solution field (not a solution family) to a rank-1 per-domain table.

## The composition, in source

The energy reduction is a pure per-domain map over the configured domains — no inter-domain state.
The source stages, in order:

1. **Setup (clear + reserve the per-domain caches).** `domain_E_field_energy_i.clear()` /
   `domain_H_field_energy_i.clear()` (`:1023-1024`), reserved to `dom_post_op.M_i.size()`
   (`:1028-1029`). `dom_post_op.M_i` is the configured domain-attribute → restricted-operator map
   (the reduction's index domain).

2. **The electric-energy per-domain map** (guarded `if constexpr (HasEGridFunction<solver_t>())`,
   `:1030`). The field is `auto &field = V ? *V : *E` (`:1032`, use `V` if present else `E`); the
   whole-domain total is `auto energy = dom_post_op.GetElectricFieldEnergy(field)` (`:1033`), cached
   as `domain_E_field_energy_all` (`:1034`). The per-domain loop
   `for (const auto &[idx, data] : dom_post_op.M_i)` (`:1036`) computes per domain:
   `auto energy_i = dom_post_op.GetDomainElectricFieldEnergy(idx, field)` (`:1038`, the
   domain-restricted energy form), `auto participation_ratio = std::abs(energy_i) > 0.0 ? energy_i /
   energy : 0.0` (`:1039`, the participation quotient with the zero-numerator guard), and emits
   `Measurement::DomainData{idx, energy_i, participation_ratio}` (`:1040-1041`) into the cache. The
   E-only `else` (no E grid function) emits zero `DomainData` rows (`:1044-1053`).

3. **The magnetic-energy per-domain map** (guarded `if (HasBGridFunction<solver_t>())`, `:1055`).
   Structurally identical with `A`/`B` for `V`/`E`: `auto &field = A ? *A : *B` (`:1057`),
   `auto energy = dom_post_op.GetMagneticFieldEnergy(field)` (`:1058`) → `domain_H_field_energy_all`
   (`:1059`), and the per-domain loop (`:1061-1066`) computing
   `energy_i = GetDomainMagneticFieldEnergy(idx, field)` (`:1063`), the participation ratio (`:1064`,
   note the guard tests the *total* `energy` here, the source's own form), and the
   `DomainData{idx, energy_i, participation_ratio}` emit (`:1065-1066`). The H-only `else` emits
   zero rows (`:1069-1078`).

4. **The per-domain energy form (`½⟨field, M_i field⟩`).** `DomainPostOperator::
   GetDomainElectricFieldEnergy(int idx, const GridFunction &E)`
   (`palace/models/domainpostoperator.cpp:255`) restricts to one domain attribute: it looks up
   `M_i.find(idx)` (`:259`), applies the restricted operator `it->second.first->Mult(E.Real(), D)`
   (`:265`), forms `double dot = linalg::LocalDot(E.Real(), D)` (`:266`), adds the imaginary part if
   present (`:267-271`), globally sums (`:272`), and returns `0.5 * dot` (`:273`) — the
   `½⟨E, M_idx E⟩` SPD energy form (the [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)
   squared radicand restricted to one domain). The magnetic sibling
   `GetDomainMagneticFieldEnergy(int idx, const GridFunction &B)` (`:277`) is identical with `B`/`H`,
   returning `0.5 * dot` (`:296`).

## Inputs / outputs (the feature surface, in source)

- **Input — config + a solution field.** The configured domain-attribute map `dom_post_op.M_i`
  (`postoperator.cpp:1029, 1036`, the reduction's index domain); the field `V ? *V : *E`
  (`:1032`) / `A ? *A : *B` (`:1057`) supplied by the producing driver column.
- **Output — the physical product.** The per-domain caches
  `measurement_cache.domain_E_field_energy_i` / `domain_H_field_energy_i` (each a
  `std::vector<Measurement::DomainData>`, set `:1040-1041, 1065-1066`), plus the whole-domain totals
  `domain_E_field_energy_all` / `domain_H_field_energy_all` (`:1034, 1059`) — the rank-1 per-domain
  energy + participation table.

## Lifts to

This L0 surface lifts to the L1 pure-function composition root
[`energy-fields.L1`](./energy-fields.L1.md) (the in-place `emplace_back(DomainData{...})` cache
accumulation → value-returning per-domain `(energyᵢ, pᵢ)` evaluations) and the L4 combinator
composition root [`energy-fields.L4`](./energy-fields.L4.md) (the per-domain `for` loop + the energy
form + the participation quotient → the `domain_energy_reduce`
per-domain energy-table reduction combinator, folding the
[`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)-squared energy form and the firm
[`participation_ratio`](../L1/participation_ratio.md)). The per-operator L1>L0 mutation-rotation of
the readout carries the per-write lifts; this feature surface records the output-product *site map*
(which source range realizes which reduction stage).

## Status

`seed` — the L0 ground-truth surface for the domain field-energy table output product (the
output-product **leaf feature column**), authored under the FEATURE-SURFACE SPINE directive
(2026-06-02), mirroring the [eigenfrequency-qfactor.L0](./eigenfrequency-qfactor.L0.md) /
[capacitance.L0](./capacitance.L0.md) output-product exemplars. Every stage is a cited range into
`palace/models/postoperator.cpp` (the per-domain table) + `palace/models/domainpostoperator.cpp`
(the energy form), confirmed on-disk via palace-codemap `read_range`/`search_text` this dispatch
(the def `postoperator.cpp:1021`, the electric map `:1030-1053`, the magnetic map `:1055-1078`, the
`DomainData` emits `:1040-1041, 1065-1066`; the energy form `domainpostoperator.cpp:255-275`
electric / `:277-298` magnetic, both returning `0.5 * dot`; the `Measurement::DomainData` struct
`postoperatorcsv.hpp:74-79`). The load-bearing structural fact at L0: a pure per-domain map (the
loops carry no inter-domain accumulator), reducing a single solution field to its per-domain
`(energy, participation)` rows — a rank-1 per-domain table, NOT a family-PAIR Gram grid (c074 D6
do-NOT-over-unify). The chapter's evidence IS the source range + the per-stage site map to the
constituent reduction (the adapted surface-or-evidence form for the feature-surface kind).
```

### Edit 1 — `feature/index.md` matrix: add BOTH new rows (cohort-owner)

```edit:book/src/feature/index.md
[old]: | **[Driver-leaf columns](./driver-leaf.md)** | | | |
| [driven](./driven.L4.md) | [L4 root](./driven.L4.md) | [L1 root](./driven.L1.md) | [L0 surface](./driven.L0.md) |
[new]: | **[Driver-leaf columns](./driver-leaf.md)** | | | |
| [boundary-mode](./boundary-mode.L4.md) | [L4 root](./boundary-mode.L4.md) | [L1 root](./boundary-mode.L1.md) | [L0 surface](./boundary-mode.L0.md) |
| [driven](./driven.L4.md) | [L4 root](./driven.L4.md) | [L1 root](./driven.L1.md) | [L0 surface](./driven.L0.md) |
```

```edit:book/src/feature/index.md
[old]: | [eigenfrequency-qfactor](./eigenfrequency-qfactor.L4.md) | [L4 root](./eigenfrequency-qfactor.L4.md) | [L1 root](./eigenfrequency-qfactor.L1.md) | [L0 surface](./eigenfrequency-qfactor.L0.md) |
| [inductance](./inductance.L4.md) | [L4 root](./inductance.L4.md) | [L1 root](./inductance.L1.md) | [L0 surface](./inductance.L0.md) |
[new]: | [eigenfrequency-qfactor](./eigenfrequency-qfactor.L4.md) | [L4 root](./eigenfrequency-qfactor.L4.md) | [L1 root](./eigenfrequency-qfactor.L1.md) | [L0 surface](./eigenfrequency-qfactor.L0.md) |
| [energy-fields](./energy-fields.L4.md) | [L4 root](./energy-fields.L4.md) | [L1 root](./energy-fields.L1.md) | [L0 surface](./energy-fields.L0.md) |
| [inductance](./inductance.L4.md) | [L4 root](./inductance.L4.md) | [L1 root](./inductance.L1.md) | [L0 surface](./inductance.L0.md) |
```

### Edit 2 — `feature/index.md` output-product cohort prose: add the energy-fields reduction-shape bullet (cohort-owner)

```edit:book/src/feature/index.md
[old]: - **Per-mode scalar-table (rank-1)** — cycle-075: [`eigenfrequency-qfactor`](./eigenfrequency-qfactor.L4.md), over the [`eigenmode`](./eigenmode.L4.md) driver's converged-mode family. It composes the new `eigenfreq_qfactor_reduce` reduction (mined c075 D3, `rough-in`) — a per-mode `(f, Q)` map (`f = Re ω` un-transformed; `Q = ω/κ`), the reduce-to-scalar-TABLE member, structurally distinct from both the rank-2 family-PAIR Gram and the rank-2 port-projection.

All three output-product columns stay `seed` (not promotable) because each composed reduction verb is itself `rough-in` (a feature column may promote past `seed` only once ALL its composed constituents are firm).
[new]: - **Per-mode scalar-table (rank-1)** — cycle-075: [`eigenfrequency-qfactor`](./eigenfrequency-qfactor.L4.md), over the [`eigenmode`](./eigenmode.L4.md) driver's converged-mode family. It composes the new `eigenfreq_qfactor_reduce` reduction (mined c075 D3, `rough-in`) — a per-mode `(f, Q)` map (`f = Re ω` un-transformed; `Q = ω/κ`), the reduce-to-scalar-TABLE member, structurally distinct from both the rank-2 family-PAIR Gram and the rank-2 port-projection.
- **Per-domain scalar-table (rank-1)** — cycle-078: [`energy-fields`](./energy-fields.L4.md), over a *single solution field* (not a family) from any field-bearing driver. It composes the new `domain_energy_reduce` reduction (minted c078, `rough-in`) — a per-domain `(energyᵢ, pᵢ)` map folding the domain-restricted SPD energy form `½⟨field, M_i field⟩` ([`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)-squared, rough-in) and the **firm** [`participation_ratio`](../L1/participation_ratio.md). It is the **per-domain** sibling of the per-mode `eigenfreq_qfactor_reduce` table (both reduce-to-scalar-TABLE, rank-1) — NOT a `gram_reduce` family-PAIR grid (the c074 D6 do-NOT-over-unify guard, honored).

All five output-product columns stay `seed` (not promotable) because each composed reduction verb is itself `rough-in` (a feature column may promote past `seed` only once ALL its composed constituents are firm).
```

### Edit 3 — `feature/index.md` line-54 "Still planned" prose (cohort-owner: both now authored)

```edit:book/src/feature/index.md
[old]: Still planned (per the FEATURE-SURFACE SPINE directive scope; not yet authored): the remaining output product (energy/field measurements) and wave-port / boundary-mode (the 6th `ProblemType` branch, authored as a co-equal leaf driver column under the lifecycle ROOT). Each lands as a feature column when its constituent vocabulary is firm enough to compose cleanly (a feature that cannot yet be cleanly composed is a *finding about the spine*, surfaced as an open question — the same low-priority test-load discipline the solvers carry on the vocabulary spine).
[new]: The FEATURE-SURFACE SPINE directive scope is now fully authored: cycle-078 lands the last output product ([`energy-fields`](./energy-fields.L4.md), the per-domain energy table) and the 6th-`ProblemType` wave-port / [`boundary-mode`](./boundary-mode.L4.md) driver column (a co-equal leaf driver column under the lifecycle ROOT). Every column lands `seed` and promotes only when its constituent vocabulary is firm enough to compose cleanly (a feature that cannot yet be cleanly composed is a *finding about the spine*, surfaced as an open question — the same low-priority test-load discipline the solvers carry on the vocabulary spine).
```

### Edit 4 — `feature/output-product.md` group-intro: add the energy-fields bullet (my OWN bullet, alpha) + convert the line-12 "planned" prose

```edit:book/src/feature/output-product.md
[old]: - [`eigenfrequency-qfactor`](./eigenfrequency-qfactor.L4.md) — **per-mode scalar-table (rank-1)**, the [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) per-mode `(f, Q)` map, over the [`eigenmode`](./eigenmode.L4.md) driver's converged-mode family. Levels: [L4](./eigenfrequency-qfactor.L4.md) · [L1](./eigenfrequency-qfactor.L1.md) · [L0](./eigenfrequency-qfactor.L0.md).
[new]: - [`eigenfrequency-qfactor`](./eigenfrequency-qfactor.L4.md) — **per-mode scalar-table (rank-1)**, the [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) per-mode `(f, Q)` map, over the [`eigenmode`](./eigenmode.L4.md) driver's converged-mode family. Levels: [L4](./eigenfrequency-qfactor.L4.md) · [L1](./eigenfrequency-qfactor.L1.md) · [L0](./eigenfrequency-qfactor.L0.md).
- [`energy-fields`](./energy-fields.L4.md) — **per-domain scalar-table (rank-1)**, the `domain_energy_reduce` per-domain `(energyᵢ, pᵢ)` map (minted c078, `rough-in`), folding the domain-restricted SPD energy form `½⟨field, M_i field⟩` ([`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)-squared) and the **firm** [`participation_ratio`](../L1/participation_ratio.md), over a *single solution field* from any field-bearing driver (not a solution family). The per-domain sibling of the per-mode `eigenfrequency-qfactor` table. Levels: [L4](./energy-fields.L4.md) · [L1](./energy-fields.L1.md) · [L0](./energy-fields.L0.md).
```

```edit:book/src/feature/output-product.md
[old]: Columns are alpha-ordered within this grouping. The within-column level ordering is **high→low** (L4 → L1 → L0), the deliberate FEATURE-SURFACE exception to alpha-within-cohort ordering. A further output product — energy/field measurements — is planned and lands here when its constituent vocabulary is firm. All columns stay `seed` because each composed reduction verb is itself `rough-in` (a feature column may promote past `seed` only once all its composed constituents are firm).
[new]: Columns are alpha-ordered within this grouping. The within-column level ordering is **high→low** (L4 → L1 → L0), the deliberate FEATURE-SURFACE exception to alpha-within-cohort ordering. With [`energy-fields`](./energy-fields.L4.md) (cycle-078) the output-product cohort is complete (5 columns). All columns stay `seed` because each composed reduction verb is itself `rough-in` (a feature column may promote past `seed` only once all its composed constituents are firm).
```

### Edit 5 — `book/src/SUMMARY.md` `# Feature surfaces` block: add BOTH new columns' 3-level nested entries (cohort-owner)

Boundary-mode in driver-leaf grouping, alpha-FIRST (before `driven`); energy-fields in output-product grouping, alpha (between `eigenfrequency-qfactor` and `inductance`). Within-column high→low L4→L1→L0 preserved.

```edit:book/src/SUMMARY.md
[old]: - [Driver-leaf columns](./feature/driver-leaf.md)
  - [driven — L4 composition-root](./feature/driven.L4.md)
[new]: - [Driver-leaf columns](./feature/driver-leaf.md)
  - [boundary-mode — L4 composition-root](./feature/boundary-mode.L4.md)
  - [boundary-mode — L1 composition-root](./feature/boundary-mode.L1.md)
  - [boundary-mode — L0 ground-truth surface](./feature/boundary-mode.L0.md)
  - [driven — L4 composition-root](./feature/driven.L4.md)
```

```edit:book/src/SUMMARY.md
[old]:   - [eigenfrequency-qfactor — L0 ground-truth surface](./feature/eigenfrequency-qfactor.L0.md)
  - [inductance — L4 composition-root](./feature/inductance.L4.md)
[new]:   - [eigenfrequency-qfactor — L0 ground-truth surface](./feature/eigenfrequency-qfactor.L0.md)
  - [energy-fields — L4 composition-root](./feature/energy-fields.L4.md)
  - [energy-fields — L1 composition-root](./feature/energy-fields.L1.md)
  - [energy-fields — L0 ground-truth surface](./feature/energy-fields.L0.md)
  - [inductance — L4 composition-root](./feature/inductance.L4.md)
```

### Append to `scaffolding/open-questions.md`

```append:scaffolding/open-questions.md

## OQ (cycle-078 D1, energy-fields output-product column)

- **`record-DomainData-needs-definition-home`** — `Measurement::DomainData`
  (`{ int idx; double energy; double participation_ratio; }`,
  `palace/models/postoperatorcsv.hpp:74-79`) is currently defined in-chapter as a single-consumer
  record (the `## Record definition` section of `book/src/feature/energy-fields.L4.md`), since the
  energy-fields output-product column is its only firm-artifact consumer this cycle. BUT the struct
  lives in `postoperatorcsv.hpp` (the CSV-writer surface) and is also consumed by the CSV
  measurement-output path (`postoperatorcsv` writes the per-domain energy table from these rows).
  If/when a `postoperatorcsv` output-surface chapter (or a `lifecycle` postprocess-output stage) is
  authored as a 2nd consumer, `DomainData` clears the ≥2-consumer bar → promote it to a
  cross-cutting `book/src/concepts/DomainData.md` record-definition page (move the schema there;
  the energy-fields chapter then links to it). Flag for a cross-cutter / record-definition
  dispatch. (record-definition obligation, user directive-2 2026-06-03.)

- **`domain_energy_reduce-l4-verb-needs-authoring`** — the energy-fields column composes a newly
  minted L4 reduction verb `domain_energy_reduce` (`rough-in`, no anchor file yet — referenced
  plain-text per the rough-in-no-anchor convention). It is the per-DOMAIN scalar-table sibling of
  `eigenfreq_qfactor_reduce` (per-MODE): a per-domain `(energyᵢ, pᵢ)` map folding the
  domain-restricted energy form (`matrix-weighted-norm`-squared, rough-in) and the firm
  `participation_ratio`. A harvester/combinator-miner dispatch should author
  `book/src/L4/domain_energy_reduce.md` (rough-in → its gates: a firm domain-restricted energy-form
  L1 primitive, and the `matrix-weighted-norm` test-coverage gate). It joins the L4 reduce-family
  (now 4 reduce-shapes: `gram_reduce`, `sparameter_reduce`, `eigenfreq_qfactor_reduce`,
  `domain_energy_reduce`). NOTE: confirm with a combinator-miner that the per-domain restriction +
  ratio genuinely warrants a distinct verb vs. a `participation_ratio`-fold inlined into the column
  (this dispatch's author-judgment was: distinct verb, for the rank-1-table cohort symmetry + the
  named per-domain-restriction shift — but a 2nd witness or a miner pass should confirm it does not
  collapse into an existing reduce-shape).

- **`energy-fields-driver-agnostic-not-per-driver-stage3`** — the domain energy table is a
  driver-AGNOSTIC output product (the SAME `MeasureDomainFieldEnergy` reduces any field-bearing
  driver's solution field, unlike capacitance/inductance/sparameters/eigenfrequency-qfactor which
  each reduce ONE specific driver's family). This breaks the output-product↔driver-column
  stage-3 cross-linking convention's 1:1 assumption (there is no single producing driver to
  reciprocal-link). The column links to `electrostatic`/`magnetostatic`/… generically rather than
  to one driver's stage-3. Flag whether the cross-link convention needs an "N-driver output
  product" amendment (the reciprocal up-link from each field-bearing driver's stage-3 to
  energy-fields), or whether energy-fields is correctly treated as a shared postprocess all drivers
  point at. (Observation routed as OQ, not an in-column edit to the driver columns — the read-only
  down-link discipline.)
```

## Open questions / caveats

1. **L4 reduction-verb judgment (mint vs. inline).** I minted `domain_energy_reduce` (rough-in) for
   the rank-1-table cohort symmetry + because it names a genuine per-domain-restriction reduction
   shape composing the firm `participation_ratio`. This is author-judgment under the redirect's
   "do not mint a verb that adds no simplification" rule; a combinator-miner 2nd-witness pass should
   confirm it does not collapse into `eigenfreq_qfactor_reduce` (the per-mode sibling) — they share
   the rank-1-table shape but differ in index domain (mode vs. domain) and folded projections
   (`(f,Q)` un-transform+κ vs. domain-restricted-energy+participation). OQ
   `domain_energy_reduce-l4-verb-needs-authoring` filed.

2. **`DomainData` record home (single vs. cross-cutting).** Author-judgment: single-consumer →
   in-chapter `## Record definition` (energy-fields.L4). But the struct lives in the CSV-writer
   header and IS consumed by the CSV output path; if that path is ever a firm chapter, promote to a
   `concepts/` page. OQ `record-DomainData-needs-definition-home` filed (record-definition
   obligation directive-2).

3. **Driver-agnostic output product.** energy-fields breaks the 1:1 output-product↔driver
   cross-link convention (no single producing driver). OQ
   `energy-fields-driver-agnostic-not-per-driver-stage3` filed for the convention amendment. I did
   NOT add reciprocal up-links into the driver columns (would be a constituent-algebra edit + there
   is no single driver) — routed as OQ per the read-only-down-link discipline.

4. **Cohort-owner scope honored.** I own (3) the shared `feature/index.md` matrix + cohort prose +
   "Still planned" line + `SUMMARY.md` block for BOTH columns, and my OWN (1)+(2) for energy-fields
   (the index row is in the matrix edit; my output-product.md group-intro bullet is Edit 4). I did
   NOT author D2's boundary-mode driver-leaf.md group-intro bullet or the boundary-mode 3 chapter
   files — those are D2's own (1)+(2) and column authoring. D2 DEFERS only its index/SUMMARY rows to
   me (done in Edits 1 + 5). The driver-leaf.md line-19 "A 6th co-equal leaf driver column … is
   planned" prose is left for D2 to convert (it is D2's column's group-intro bullet, not the
   count-owner's surface).

5. **No consolidated firm-tally on this surface.** The feature Part uses a status-token matrix, not
   a firm/rough-in count tally; there is no layer-index consolidated count to own here (the
   cohort-owner duty on the feature surface is the shared matrix + SUMMARY block, which I own).

## Citation self-verification

All L0 citations self-verified on-disk this dispatch via palace-codemap `read_range` + `search_text`
against `reference/palace/`:
- `postoperator.cpp:1021` `MeasureDomainFieldEnergy` def (search_text exact match).
- `postoperator.cpp:1022-1079` body read (the `clear`/`reserve` `:1023-1029`, the
  `HasEGridFunction` guard `:1030`, field `V?*V:*E` `:1032`, total `:1033`, `_all=` `:1034`,
  electric per-domain loop `:1036` with `GetDomainElectricFieldEnergy` `:1038` + ratio `:1039` +
  `DomainData` emit `:1040-1041`, the E-only else `:1044-1053`, the `HasBGridFunction` guard
  `:1055`, field `A?*A:*B` `:1057`, total `:1058`, `_all=` `:1059`, the magnetic loop `:1061` with
  `GetDomainMagneticFieldEnergy` `:1063` + ratio `:1064` + emit `:1065-1066`, the H-only else
  `:1069-1078`). NOTE: the prompt's line hints (def `:1021` matched; loop hint `:1029-1075`, ratio
  hint `:1038`) and the codemap `read_range` indexing were each +1 high on the electric block on the
  leading-comment boundary; the exact on-disk numbers above (loops `:1036`/`:1061`, ratios
  `:1039`/`:1064`, emits `:1040-1041`/`:1065-1066`) are read directly on-disk and are what the
  chapters use (the known codemap +1 drift on a comment+brace boundary — on-disk wins).
- `domainpostoperator.cpp:255` `GetDomainElectricFieldEnergy` def (search_text exact match), body
  `:255-275` returning `0.5 * dot` (`:273`); magnetic sibling `:277-298` returning `0.5*dot`
  (`:296`).
- `postoperatorcsv.hpp:74-79` `Measurement::DomainData` struct
  `{ int idx; double energy; double participation_ratio; }` (read on-disk).
