---
kind: navigational-container (synthesis Part index)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order). The Synthesis section is an implementation
# VIEW that LINKS (reference-class) to the authoritative L4 / semantics /
# concepts defs — it adds no `depends-on` blocking edge and constrains no
# rank/liveness (scheme §4/§5).
edges:
  reference:
    - synthesis/types
    - synthesis/iteration
    - synthesis/data-algebra
    - synthesis/coordination
    - synthesis/drivers
---

# Synthesis — the synthesized-library implementation view

This Part renders the spec's surface **as though it were a real implementation library** — the synthesized codebase the layered spec describes — written in the **L4 pseudo-language** (Haskell `::` signatures + TypeScript `{ field: type }` records, fenced ` ```text `; the same convention as the L4 / L3 layers and the [semantic surface](../semantics/index.md)).

It is a **distinct chapter KIND**: the *implementation VIEW*, parallel to the [Feature surfaces](../feature/index.md) spine's *top-down entry-point VIEW*. Where the vocabulary Parts (L4→L0) climb from cited source to calculus combinators by *decomposing*, and the Feature spine *recomposes* the firm vocabulary into user-facing features, the Synthesis Part renders **the same firm vocabulary as concrete library code** — the form a reader who wants to *read the implementation* (like generated code) wants to consume.

## What this Part is — and is NOT

- **IS** the synthesized code form: concrete def bodies in the L4 pseudo-language, with per-def **code-doc** sections (explicit I/O sets, named shape contracts, the bunsen `# Arguments` / `# Returns` style).
- **IS NOT** a semantic restatement. Per the [semantic-consolidation directive](../methodology/semantic-consolidation.md) + the record-definition obligation, the authoritative **semantics / algebraic laws / record-field definitions** live ONCE — in the [L4 operator chapters](../L4/index.md), the [semantic surface](../semantics/index.md), and the [`concepts/`](../concepts/index.md) record-definition pages. Synthesis **LINKS to them** and renders the synthesized code form. A rendered def's correspondence to its L4 chapter body is *reviewable* (`lowering-verifier` may audit it); it does not own the law-claim.

The reader-entry duality: enter the Feature spine top-down ("what does the electrostatic driver *do*, what does it compose?"), the vocabulary spine bottom-up ("what is `fe_assemble`, where is it used?"), or **this Part as the implementation** ("what is the *code* that realizes the surface?").

## The 5-library partition

The library partition **mirrors the 3 L4 doc-groups** ([L4 overview](../L4/index.md)), bracketed by a foundational **`types`** library and a top **`drivers`** library:

| Library | Mirrors | Holds | Status |
|---|---|---|---|
| [`types`](./types.md) | (foundational bracket) | the genuinely **shared / cross-cutting** record/type defs (shared across ≥2 API groups): `IoData`, `SimState`, `OpParams` | navigational (rendered) |
| [`iteration`](./iteration.md) | [Iteration & step combinators](../L4/iteration-combinators-intro.md) | `chebyshev`, `iterate-while`, `iterate-while-with-prev`, `krylov-step` (+ the iteration-clustering step-state carriers) | stub (Wave 2) |
| [`data-algebra`](./data-algebra.md) | [Data-algebra combinators & named verbs](../L4/data-algebra-combinators-intro.md) | `assemble_frequency_operator`, `domain_energy_reduce`, `dot`, `eigenfreq_qfactor_reduce`, `eliminate_bc`, `fe_assemble`, `gram_reduce`, `inner_product`, `linear_combination`, `mk_matrix_free_operator`, `nrm2`, `sparameter_reduce`, `waveguide_mode_reduce` (+ `sharding-decompose-reduce` as a future-direction stub note) | stub (Wave 2) |
| [`coordination`](./coordination.md) | [Outer-driver caps & coordination combinators](../L4/outer-driver-combinators-intro.md) | `eigsolve`, `fold_solve`, `frequency_sweep`, `ksp_solve`, `preconditioning-framework`, `solve_family` (+ the coordination-clustering state carriers) | stub (Wave 2) |
| [`drivers`](./drivers.md) | (lifted from [Feature surfaces](../feature/index.md)) | the entry-point surfaces — 5 sim drivers + lifecycle ROOT + output products — composing the calculus libraries | stub (deferred) |

**Why this shape.** The 3 calculus libraries are the natural modular split of the L4 vocabulary (already grouped this way in the L4 SUMMARY). `types` brackets them at the bottom because a topological library order requires every shared type def to precede its consumers. `drivers` brackets them at the top because the entry-point surfaces *compose* the calculus libraries — they come last in topological order. The exact modularization is **a seed (5 libraries), refinable by use**.

### Type placement — cluster a type with its API group

Only types **genuinely shared across ≥2 API groups** live in the foundational `types` library. A type/record that **clusters with one** implementation-API group (e.g. `Krylov` / `StepOutputs` / `PrevCarry` ↔ `iteration`; `DofSet` / `WaveguideModeTable` ↔ `data-algebra`; `SolveResult` / `EigState` ↔ `coordination`; a per-driver config record ↔ its `drivers` column) is placed **immediately BEFORE that API group**, bundled with the type's **utility API** — its own intrinsic namespace (constructors / smart-constructors, field accessors, predicates, trivial projections; a Haskell-style `where` / module-local utility cluster). The type's **consumer methods are NOT moved with it** — the substantive operators that *consume* the type to do the algorithm stay in the API group proper, AFTER the type+utility block. (Topological order still governs overall: a type + its utility API precede their consumers.)

## Rendering conventions

These conventions govern every library chapter in this Part:

- **Topological def order.** Within a library, a def appears *after* everything it uses.
- **L4 pseudo-language.** Haskell `::` signatures, TS `{ field: type }` records, do-notation + lambda bodies, fenced ` ```text `. Reduction-rule math uses `$$ ... $$`. **The `$`-sigil pseudocode (`Tensor[$S]`, `LinOp[$S,$S]`, `$N`) MUST be inside a ` ```text ` fence**, never a 4-space-indented block (the KaTeX `$`-sigil-fence rule) — copy a landed `$`-sigil sibling such as `../L4/gram_reduce.md`.
- **Named shape groups.** Shape-generic ops use the named-shape-group form `Tensor[(S: ...)]` (binding) / `Tensor[$S]` (use) per the [semantic surface](../semantics/index.md) §1.2.1; reserve `Tensor[N]` for genuinely flat rank-1 dof-vectors.
- **`#extern NAME` for opaque kernels.** An opaque-library boundary kernel (the existing kernel-API nodes — libCEED element-quadrature, the SLEPc EPS eigsolve loop, triangular-solve / GS-SSOR relaxation) appears as **`#extern NAME`** in place of its implementation def, **after its type signature**. The from-our-primitives constructive realization (the kernel-impl node — `libceed-quadrature-kernel-impl`, `eigsolve-impl`, the multigrid-relaxation-smoother) is rendered inline where firm; the opaque loop itself is the `#extern`. Do NOT lift the opaque kernel into a fabricated def.
- **Deep-linked unchanged lower artifacts rendered INLINE.** Where an L4 form is identity-in-form to its L3 / L2 / L1 version (deep-linked *because unchanged* across the rotation), the unchanged artifact is rendered **inline** in the library (it IS the implementation) — not linked-away.
- **Haskell `where` clauses** define a def's private utility namespace (a library's internal helpers).
- **Code-doc per def.** Each def carries a docstring: explicit I/O sets, named shape contracts, `# Arguments` / `# Returns`.
- **Link, don't re-cite.** A rendered def LINKS to its authoritative `../L4/<op>.md` chapter (the law/semantic claim lives there); it does not re-cite L0 (the L4 chapter + the concept page own the citations). This Part adds `reference`-class navigational edges only — no `depends-on` blocking edges.

## Status

`navigational-container` (Part index). This page makes no resolution claim — it is the orientation + dep-map for the Synthesis implementation VIEW. The per-library chapters carry their own status (`types` rendered; `iteration` / `data-algebra` / `coordination` / `drivers` `stub` pending Wave-2 def rendering).
