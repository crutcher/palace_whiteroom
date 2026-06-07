---
status: stub
kind: navigational-container (synthesis library — drivers; body deferred to a later batch-44 cycle)
# Intro shell. No `rank:` — implementation VIEW, reference-class links only.
edges:
  reference:
    - feature/index
    - feature/lifecycle.L4
    - synthesis/types
    - synthesis/iteration
    - synthesis/data-algebra
    - synthesis/coordination
    - synthesis/index
---

# Library `drivers` — entry-point surfaces (lifted from the Feature spine)

> **Status: `stub`.** This is the library intro shell; the body is **deferred to a later batch-44 cycle**. Per the directive's LEAD-sequencing, `drivers` composes everything (the calculus libraries + the shared types) and therefore comes **last** in topological order — it is authored after the 3 calculus libraries' def bodies land.

The top bracket of the [Synthesis](./index.md) library partition: the synthesized rendering of the entry-point surfaces — the **5 simulation drivers** (electrostatic / magnetostatic / driven / transient / eigenmode), the **lifecycle ROOT** (`main` → `BaseSolver` dispatch), and the **output products** (capacitance / inductance / S-parameters / eigenfrequency+Q / energy-fields / waveguide-mode) — rendered as library code that **composes** the [`types`](./types.md), [`iteration`](./iteration.md), [`data-algebra`](./data-algebra.md), and [`coordination`](./coordination.md) libraries.

These are the same composition roots the [Feature surfaces](../feature/index.md) spine presents top-down; the `drivers` library is the **implementation rendering** of those entry points (the synthesized code that realizes them), parallel to the Feature spine's entry-point VIEW.

## What this library will hold (topological order — composes everything below it)

The expected contents (refine by use): the per-driver config records cluster **before** their driver def, bundled with the config's utility API ([type-placement rule](./index.md#type-placement--cluster-a-type-with-its-api-group)); then the per-driver composition def; then the output-product reductions; finally the lifecycle ROOT that dispatches on `IoData.problem.type`. Authoring is deferred so the def bodies compose the already-rendered calculus-library defs by name.

## Rendering conventions

Per the [Synthesis overview](./index.md#rendering-conventions): topological def order (this library is topologically last); per-driver config records placed before their driver, bundled with utility API; deep-linked-unchanged lower artifacts inline; Haskell `where` for private helpers; code-doc per def; link to the Feature columns + the composed calculus-library defs, do not re-cite L0.
