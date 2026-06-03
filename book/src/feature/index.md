# Feature surfaces — entry points

This Part is the **top-down composition-root spine** — a presentation of Palace's high-level **entry-point features** (what Palace is *written for*) that runs *parallel* to the bottom-up vocabulary spine (L4→L0 + lowerings). Where the vocabulary Parts climb from cited source (L0) to calculus combinators (L4) by *decomposing* operations into reusable algebra, the feature Parts run the other direction: each chapter is a **composition root** that *recomposes* the already-firm decomposed vocabulary back into the user-facing feature.

A feature chapter is **not** a new operator. It is a distinct *kind* of chapter:

- **inputs = config** — the simulation's configuration surface (the `iodata` / problem definition).
- **outputs = the physical product** — the thing the user ran Palace to get (a capacitance matrix, an inductance matrix, S-parameters, eigenfrequencies + Q, fields).
- **body = the composition of the already-firm vocabulary at that level** — the feature is expressed as a wiring of firm ops / combinators, in *that level's* vocabulary (high→low per-level coherence: the L4 chapter composes L4 combinators, the L1 chapter composes L1 operators, the L0 chapter is the cited driver source).
- **links DOWN to the constituent ops/combinators** — every composed piece is a live link to its firm chapter; the feature chapter carries the *compositional* claim (this feature = this composition of these firm pieces), not the per-op algebraic claims (those live in the linked chapters).

It **composes** the vocabulary; it does **not** replace it. Even as a feature decomposes into collections of internal vocabulary, the entry point itself remains a dedicated, navigable surface at each level — so a reader can enter top-down ("what does the electrostatic solver *do*, and what does it compose?") as well as bottom-up ("what is `fe_assemble`, and where is it used?").

## Why a parallel spine

The vocabulary spine answers *"what are the reusable pieces, and how do they lower?"* The feature spine answers *"what are the deliverable features, and how are they assembled from those pieces?"* The two are duals: the vocabulary spine is mined *inward* (decompose for reuse + conciseness); the feature spine is composed *outward* (recompose for the backend-lowering target). The L4 feature chapter in particular is the **outward backend-lowering entry point** — it presents a whole simulation as a single composition of L4 combinators, which is the form an external GPU-tensor / distributed backend wants to consume (the feature surface, not the unfolded driver loop).

## Feature × level matrix

The spine is seeded with the **electrostatic** exemplar — the simplest/cleanest entry point: a **fixed-operator** solve (assemble the stiffness operator `K` once, then a per-terminal-source RHS-varying map) producing a **capacitance matrix**. The composition root at every level is:

> **config → `fe_assemble` (assemble `K` once) → `solve_family` (fixed-operator per-source map) → energy-form reduction (`Xⱼᵀ K Xᵢ`) → physical-product-out.**

The **magnetostatic** column (cycle-072) is the second witness of this fixed-operator shape — structurally identical to electrostatic down to the `GetStiffnessMatrix()` / `SetOperators(*K,*K)`-outside-the-loop / `std::vector<Vector>`-collect shape, differing only in the absorbed family-index domain (surface-current vs terminal boundaries), the per-element field post-process (`B = ∇×A` vs `E = -∇V`), and the energy-form normalization (the inductance matrix is current-normalized `(Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)`; the capacitance matrix is voltage-formulated `Vⱼᵀ K Vᵢ`). The **lifecycle** column (cycle-072) is the top-level composition root — `main` → `BaseSolver` dispatch — that the per-feature columns hang under.

The within-column level ordering is **high→low** (L4 → L1 → L0), NOT alphabetized; the Feature Part does not use by-kind nesting yet (small-Part guard).

| Feature | L4 (combinator composition) | L1 (pure-function composition) | L0 (cited driver source) |
|---|---|---|---|
| [electrostatic](./electrostatic.L4.md) | [L4 root](./electrostatic.L4.md) | [L1 root](./electrostatic.L1.md) | [L0 surface](./electrostatic.L0.md) |
| [magnetostatic](./magnetostatic.L4.md) | [L4 root](./magnetostatic.L4.md) | [L1 root](./magnetostatic.L1.md) | [L0 surface](./magnetostatic.L0.md) |
| [driven](./driven.L4.md) | [L4 root](./driven.L4.md) | [L1 root](./driven.L1.md) | [L0 surface](./driven.L0.md) |
| [transient](./transient.L4.md) | [L4 root](./transient.L4.md) | [L1 root](./transient.L1.md) | [L0 surface](./transient.L0.md) |
| [eigenmode](./eigenmode.L4.md) | [L4 root](./eigenmode.L4.md) | [L1 root](./eigenmode.L1.md) | [L0 surface](./eigenmode.L0.md) |
| *output products* | | | |
| [capacitance](./capacitance.L4.md) | [L4 root](./capacitance.L4.md) | [L1 root](./capacitance.L1.md) | [L0 surface](./capacitance.L0.md) |
| [inductance](./inductance.L4.md) | [L4 root](./inductance.L4.md) | [L1 root](./inductance.L1.md) | [L0 surface](./inductance.L0.md) |
| *spine ROOT* | | | |
| [lifecycle](./lifecycle.L4.md) | [L4 root](./lifecycle.L4.md) | [L1 root](./lifecycle.L1.md) | [L0 surface](./lifecycle.L0.md) |

The **driven**, **transient**, and **eigenmode** driver columns (cycle-073) complete the 5-driver leaf-column set: with electrostatic + magnetostatic (the fixed-operator pair) these three add the **operator-VARYING** corner (driven — the per-ω rebuild + `SetOperators`-inside-the-loop [`frequency_sweep`](../L4/frequency_sweep.md) map), the **state-threaded sequential-fold** corner (transient — the [`fold_solve`](../L4/fold_solve.md) time-step march), and the **opaque-library black-box** corner (eigenmode — the SLEPc eigen-iteration). The driven column is the first whose three L4 composition stages all compose FIRM combinators (the assemble basis, the per-ω operand verb, and the operator-varying solve map are each firm).

The **output-product cohort** (cycle-074) adds the first two **output-product leaf columns** — [`capacitance`](./capacitance.L4.md) and [`inductance`](./inductance.L4.md). These are a distinct shape from the driver columns: a driver column produces a *solution family*; an output-product column *consumes* a driver's solution family and *reduces* it to the user-facing physical product. Both compose the single L4 [`gram_reduce`](../L4/gram_reduce.md) symmetric-Gram reduction combinator, differing ONLY in the normalization weight — capacitance is the **voltage `w = 1`** specialization (`Cᵢⱼ = Vⱼᵀ K Vᵢ`, over the [`electrostatic`](./electrostatic.L4.md) driver's family), inductance the **current-normalized `w = 1/(Iᵢ Iⱼ)`** specialization (`Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)`, over the [`magnetostatic`](./magnetostatic.L4.md) driver's family). Both stay `seed` (not promotable) because `gram_reduce` is itself `rough-in (test-coverage-bounded)`.

Still planned (per the FEATURE-SURFACE SPINE directive scope; not yet authored): the remaining output products (S-params / eigenfreq + Q / fields) and wave-port / boundary-mode (the 6th `ProblemType` branch, authored as a co-equal leaf driver column under the lifecycle ROOT). Each lands as a feature column when its constituent vocabulary is firm enough to compose cleanly (a feature that cannot yet be cleanly composed is a *finding about the spine*, surfaced as an open question — the same low-priority test-load discipline the solvers carry on the vocabulary spine).

## Chapter-kind status

`seed` — the electrostatic column is the first exemplar of the feature-surface kind, authored under the FEATURE-SURFACE SPINE user directive (2026-06-02) ahead of role-spec codification; the magnetostatic + lifecycle columns (cycle-072) are the second-wave instances confirming the kind scales (the batch-22 meta-phase codifies the kind into the role-specs + groups it under the forthcoming directive-3 by-kind grouping). The critic's surface-or-evidence check is adapted for this kind: a feature chapter's evidence is the L0 driver-source range + the constituent-op down-links, not a single decomposed op's source site; the rotation-quality + variant-axis-coverage checks no-op (a composition root introduces no new rotation or variant axis — it composes existing firm vocabulary).
