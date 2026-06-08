---
kind: navigational-container (feature group intro)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the chapters it
# indexes (carry no liveness, constrain no rank — scheme §4/§5, OQ resolved D5).
edges:
  reference:
    - feature/capacitance.L4
    - feature/capacitance.L1
    - feature/capacitance.L0
    - feature/eigenfrequency-qfactor.L4
    - feature/eigenfrequency-qfactor.L1
    - feature/eigenfrequency-qfactor.L0
    - feature/energy-fields.L4
    - feature/energy-fields.L1
    - feature/energy-fields.L0
    - feature/inductance.L4
    - feature/inductance.L1
    - feature/inductance.L0
    - feature/sparameters.L4
    - feature/sparameters.L1
    - feature/sparameters.L0
    - feature/waveguide-mode.L4
    - feature/waveguide-mode.L1
    - feature/waveguide-mode.L0
---

# Feature surfaces — output-product columns

The **output-product** grouping holds the family-reduction feature columns — the **leaf feature column** sub-kind whose stage-(2) constituents are *vocabulary ops* (the L4 reduction verbs). An output-product column is a distinct shape from a driver column: a driver column *produces* a solution family; an output-product column *consumes* a driver's solution family and *reduces* it to the user-facing physical product. Each column down-links to its reduction verb and cross-links to its producing driver column (the reduction's authoritative home is the verb chapter + this column; the driver column's stage-3 is a thin up-pointer).

The cohort spans **three reduction shapes** (the rank-1 per-element scalar-table shape carries two verbs — `eigenfreq_qfactor_reduce` per-mode + `domain_energy_reduce` per-domain; the rank-2 Gram and rank-2 port-projection shapes one verb each) — a small algebra of family-reductions:

- [`capacitance`](./capacitance.L4.md) — **energy symmetric-Gram (rank-2, family-PAIR)**, the **voltage `w = 1`** specialization of [`gram_reduce`](../L4/gram_reduce.md) (`Cᵢⱼ = Vⱼᵀ K Vᵢ`), over the [`electrostatic`](./electrostatic.L4.md) driver's family. Levels: [L4](./capacitance.L4.md) · [L1](./capacitance.L1.md) · [L0](./capacitance.L0.md).
- [`eigenfrequency-qfactor`](./eigenfrequency-qfactor.L4.md) — **per-mode scalar-table (rank-1)**, the [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) per-mode `(f, Q)` map, over the [`eigenmode`](./eigenmode.L4.md) driver's converged-mode family. Levels: [L4](./eigenfrequency-qfactor.L4.md) · [L1](./eigenfrequency-qfactor.L1.md) · [L0](./eigenfrequency-qfactor.L0.md).
- [`energy-fields`](./energy-fields.L4.md) — **per-domain scalar-table (rank-1)**, the `domain_energy_reduce` per-domain `(energyᵢ, pᵢ)` map, folding the domain-restricted SPD energy form `½⟨field, M_i field⟩` (the **firm** [`matrix_weighted_norm`](../L1/matrix_weighted_norm.md)-squared) and the **firm** [`participation_ratio`](../L1/participation_ratio.md), over a *single solution field* from any field-bearing driver (not a solution family). The per-domain sibling of the per-mode `eigenfrequency-qfactor` table. **The column is `firm`** (own composition all-firm). Levels: [L4](./energy-fields.L4.md) · [L1](./energy-fields.L1.md) · [L0](./energy-fields.L0.md).
- [`inductance`](./inductance.L4.md) — **energy symmetric-Gram (rank-2, family-PAIR)**, the **current-normalized `w = 1/(Iᵢ Iⱼ)`** specialization of [`gram_reduce`](../L4/gram_reduce.md) (`Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)`), over the [`magnetostatic`](./magnetostatic.L4.md) driver's family. Levels: [L4](./inductance.L4.md) · [L1](./inductance.L1.md) · [L0](./inductance.L0.md).
- [`sparameters`](./sparameters.L4.md) — **port-projection (rank-2 matrix, a LINEAR projection — NOT a Gram)**, the [`sparameter_reduce`](../L4/sparameter_reduce.md) reduction, over the [`driven`](./driven.L4.md) driver's per-ω family. Levels: [L4](./sparameters.L4.md) · [L1](./sparameters.L1.md) · [L0](./sparameters.L0.md).
- [`waveguide-mode`](./waveguide-mode.L4.md) — **per-mode mode-table (carrying mode-FIELDS)**, the [`waveguide_mode_reduce`](../L4/waveguide_mode_reduce.md) reduction (**firm**), over the [`boundary-mode`](./boundary-mode.L4.md) driver's converged eigenpair family — a per-mode map to `{kn, n_eff, (Et, En, Bz)}`. The propagation-mode member of the reduce-verb algebra: a reduce-to-mode-TABLE carrying mode-FIELDS (not only scalars), distinct from the scalar-only per-element tables and the rank-2 Gram / port-projection products. It homes the boundary-mode driver's stage-(3) readout. **The column is `firm`** (own reduce verb firm; own composition all-firm — retaining its permanent `feature_root: seed` GC-root marker). Levels: [L4](./waveguide-mode.L4.md) · [L1](./waveguide-mode.L1.md) · [L0](./waveguide-mode.L0.md).

Columns are alpha-ordered within this grouping. The within-column level ordering is **high→low** (L4 → L1 → L0), the deliberate FEATURE-SURFACE exception to alpha-within-cohort ordering. The cohort holds **6 columns**, **all `firm`** under the OWN-COMPOSITION rule (a column promotes off `seed`/`rough-in` when its OWN reduce verb + directly-owned constituents are firm; cross-linked sibling driver columns are references, NOT blockers): [`eigenfrequency-qfactor`](./eigenfrequency-qfactor.L4.md) (own verb firm), [`sparameters`](./sparameters.L4.md) (own verb firm), [`energy-fields`](./energy-fields.L4.md) (own verb firm), [`capacitance`](./capacitance.L4.md) + [`inductance`](./inductance.L4.md) (own verb [`gram_reduce`](../L4/gram_reduce.md) firm), and [`waveguide-mode`](./waveguide-mode.L4.md) (own verb [`waveguide_mode_reduce`](../L4/waveguide_mode_reduce.md) firm — the boundary-mode driver's readout product). Every column retains its permanent `feature_root: seed` GC-root marker (the reachability root flag, NOT a maturity rung).
