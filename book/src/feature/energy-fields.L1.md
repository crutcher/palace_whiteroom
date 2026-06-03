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
`(energyᵢ, pᵢ)` row (the domain-restricted energy form + the participation ratio). **Under the
OWN-COMPOSITION rule (USER DIRECTIVE 2026-06-03) a column promotes off `seed` when its OWN
directly-owned constituents are firm; this column STAYS `seed`** because its OWN reduce verb's L4 home
`domain_energy_reduce` is `rough-in` and its OWN folded domain energy form is the `matrix-weighted-norm`
`rough-in (test-coverage-bounded)` primitive (only the [`participation_ratio`](../L1/participation_ratio.md)
half is firm). These are OWN-constituent gates, NOT cross-linked-sibling blockers — the field-bearing
driver columns are SIBLING references (a driver-agnostic shared postprocess), not the gate. The
chapter carries the compositional claim only; per-op
algebraic claims live in the linked chapters. The defining structural fact carried from L4: a
rank-1 per-domain scalar table, NOT a `gram_reduce` family-PAIR grid (c074 D6). Evidence: the L0
energy-table ranges `postoperator.cpp:1021-1077` + the energy form `domainpostoperator.cpp:255-298`,
confirmed on-disk this dispatch, plus the constituent down-links.
