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
