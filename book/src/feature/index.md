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

## Feature × level matrix (seed)

The spine is seeded with the **electrostatic** exemplar — the simplest/cleanest entry point: a **fixed-operator** solve (assemble the stiffness operator `K` once, then a per-terminal-source RHS-varying map) producing a **capacitance matrix**. The composition root at every level is:

> **config → `fe_assemble` (assemble `K` once) → `solve_family` (fixed-operator per-terminal map) → capacitance-matrix reduction (`Vⱼᵀ K Vᵢ`) → capacitance-out.**

| Feature | L4 (combinator composition) | L1 (pure-function composition) | L0 (cited driver source) |
|---|---|---|---|
| [electrostatic](./electrostatic.L4.md) | [L4 root](./electrostatic.L4.md) | [L1 root](./electrostatic.L1.md) | [L0 surface](./electrostatic.L0.md) |

Planned (per the FEATURE-SURFACE SPINE directive scope; not yet authored): the other 4 sim drivers (magnetostatic, eigenmode, driven, transient), the top-level lifecycle (`main` → `BaseSolver`), the output products (S-params / capacitance / inductance / eigenfreq + Q / fields), and wave-port / boundary-mode. Each lands as a feature column when its constituent vocabulary is firm enough to compose cleanly (a feature that cannot yet be cleanly composed is a *finding about the spine*, surfaced as an open question — the same low-priority test-load discipline the solvers carry on the vocabulary spine).

## Chapter-kind status

`seed (exemplar)` — the electrostatic column is the first exemplar of the feature-surface kind, authored under the FEATURE-SURFACE SPINE user directive (2026-06-02) ahead of role-spec codification (the batch-22 meta-phase codifies the kind into the role-specs + groups it under the forthcoming directive-3 by-kind grouping). The critic's surface-or-evidence check is adapted for this kind: a feature chapter's evidence is the L0 driver-source range + the constituent-op down-links, not a single decomposed op's source site.
