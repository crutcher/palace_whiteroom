---
agent: layer-intro-author
invoked_at: 2026-06-07T230500Z
scope: synthesis-section-shell — # Synthesis Part shell + SUMMARY wiring + 5 per-library intros + the types library body
status: integrated
integrated_at: 2026-06-07T230000Z
integration_commit: 5828a07
integration_notes: |
  Applied cycle-136 (batch-44 LEAD/OPENER). Created the `# Synthesis` Part — index + types BODY (IoData/OpParams/SimState) + 4 stub library shells (iteration/data-algebra/coordination/drivers) + SUMMARY wiring immediately before `# Feature surfaces`. All 6 navigational-containers (reference-class edges only). Build EXIT 0; rank_violations=0. Finalize normalized the cross-chapter status-token convention (filled VIEW chapters carry no `status:` field; drivers stays `status: stub`).
---

# CYCLE: # Synthesis Part shell + the `types` library

## Summary

Batch-44 LEAD opener (user directive 2026-06-07, CLAUDE.md §"The SYNTHESIS section"). Lays the structural foundation for the new top-level `# Synthesis` Part — the spec's L4 surface rendered as a synthesized implementation library in the L4 pseudo-language. This dispatch delivers the directive's LEAD-sequencing steps (a)+(b):

- **(a)** `book/src/synthesis/index.md` (the Part overview), the SUMMARY.md wiring (the `# Synthesis` Part placed **immediately before `# Feature surfaces`**), and the 5 per-library chapter intro shells (`types` → `iteration` → `data-algebra` → `coordination` → `drivers`).
- **(b)** the foundational **`types`** library BODY — holding ONLY the genuinely **shared / cross-cutting** type defs (shared across ≥2 API groups): `IoData` (config record), `SimState`, `OpParams`. Each is rendered in the L4 pseudo-language (TS brace form) with a code-doc block and a back-link to its authoritative `concepts/<record>.md` home (semantic-consolidation: define once; render the synthesized form + link, do NOT restate field semantics). Types that cluster with a single API group are deliberately NOT here — they are placed before their group in Wave 2 (per the type-placement rule).

The 3 calculus libraries (`iteration` / `data-algebra` / `coordination`) and the `drivers` library are seeded as `stub` shells; Wave 2 (abstractor/harvester) renders their per-operator def bodies into the shells this dispatch creates. The `drivers` library is deferred to a later batch-44 cycle (it composes everything, comes last).

**Graded-stack discipline:** every Synthesis chapter is an implementation-VIEW that LINKS (reference-class) to the authoritative L4/semantics/concepts defs — it manufactures NO `depends-on` blocking edge (it adds no new rank/liveness constraint on any firm node). The Part index + per-library intros are `navigational-container` (no `rank:`, `reference`-edges only). The `types` library body is a navigational-container too — it RENDERS shared record forms but the authoritative defs (with their `depends-on` evidence edges) live in `concepts/`; the synthesized rendering carries `reference` edges to those homes (it does not re-cite L0 — the concept page owns the citation).

## Proposed changes

### 1. NEW FILE — `book/src/synthesis/index.md` (Part overview)

```edit:book/src/synthesis/index.md
[old]:
[new]:
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
```

### 2. NEW FILE — `book/src/synthesis/types.md` (the `types` library — BODY)

```edit:book/src/synthesis/types.md
[old]:
[new]:
---
kind: navigational-container (synthesis library — types)
# Navigational container, not a DAG node: no `rank:`. This library RENDERS the
# synthesized form of shared record types; the authoritative defs (with their
# L0 `depends-on` evidence edges) live in the linked `concepts/<record>.md`
# pages. The rendering carries `reference` edges to those homes — it re-cites
# nothing (the concept page owns the citation) and constrains no rank/liveness.
edges:
  reference:
    - concepts/config-record
    - concepts/sim-state
    - concepts/op-params
    - synthesis/index
---

# Library `types` — shared cross-cutting type defs

The foundational bracket of the [Synthesis](./index.md) library partition: the **genuinely shared / cross-cutting** record/type defs — the types referenced across **≥2** of the implementation-API groups (`iteration` / `data-algebra` / `coordination` / `drivers`). They are rendered here, ahead of all the groups that use them, so the overall library order stays topological (a type precedes its consumers).

This is a rendered library chapter (the implementation VIEW), **not** a record-definition page. Each type's authoritative field schema — fields, types, meaning, construction-vs-run-time stratum, L0 source home — lives ONCE in its [`concepts/`](../concepts/index.md) record-definition page (semantic-consolidation: define once). This chapter renders the **synthesized type-def form** in the L4 pseudo-language with a code-doc block, and **links** to the authoritative home. It does not restate field semantics and does not re-cite L0.

> **Type placement (the rule that scopes this library).** Only types shared across **≥2** API groups live here. A type that **clusters with one** API group (e.g. `Krylov` / `StepOutputs` / `PrevCarry` ↔ `iteration`; `DofSet` / `WaveguideModeTable` ↔ `data-algebra`; `SolveResult` / `EigState` ↔ `coordination`; a per-driver config record ↔ its `drivers` column) is placed **immediately before that API group**, bundled with the type's utility API — see the [Synthesis overview](./index.md#type-placement--cluster-a-type-with-its-api-group). This library holds only the cross-cutting remainder.

The three cross-cutting types, in topological order (`IoData` first — it is the construction-time input every solve reads; `OpParams` and `SimState` are the construction-time-readonly and run-time-evolved strata both the iteration kernel and the coordination caps thread):

## `IoData` — the parsed configuration record

Shared across **every** `drivers` column and the `coordination` caps (every solve reads it). The single immutable **construction-stratum** input — one object, parsed once from the user's JSON config, that selects the driver (`problem.type`) and supplies mesh / materials / boundaries / solver knobs. Authoritative field schema: [`config-record`](../concepts/config-record.md).

```text
-- The aggregate parsed once at startup; readonly across the whole solve.
-- Authoritative schema + field strata + L0 home: concepts/config-record.md
-- The five sub-record type names below are the synthesized (clean-room) renderings
-- of the authoritative `config::*Data` types (config-record.md:69-73):
--   ProblemConfig ≡ config::ProblemData,  ModelConfig ≡ config::ModelData,
--   DomainConfig  ≡ config::DomainData,   BoundaryConfig ≡ config::BoundaryData,
--   SolverConfig  ≡ config::SolverData.
IoData = {
  problem    : ProblemConfig,     -- driver selector (problem.type) + solver-pipeline knobs
  model      : ModelConfig,       -- mesh file + refinement + material assignment
  domains    : DomainConfig,      -- per-domain materials + postprocessing energy regions
  boundaries : BoundaryConfig,    -- BC surfaces (PEC/PMC/impedance/lumped-port/wave-port/…)
  solver     : SolverConfig       -- linear/eigen/driven/transient solver settings + tolerances
}

-- # Arguments / # Returns (utility API — construction-stratum only)
-- parseConfig :: FilePath -> IoData          -- parse the JSON config tree once
-- problemType :: IoData -> ProblemType       -- the driver-dispatch selector (a trivial projection)
```

## `OpParams` — operator-internal parameters (construction-time, readonly)

Shared across `iteration` (the `krylov-step` kernel reads it through closed-over surfaces) and `coordination` (`ksp_solve` / `solve_family` / `fold_solve` capture it once at solve construction). The readonly variant-selector + constructed-operator-surface closure, fixed across the whole `Mult` call. Authoritative field schema: [`op-params`](../concepts/op-params.md).

```text
-- readonly; captured once at solve construction, never re-inspected per step.
-- Authoritative schema + field strata + L0 home: concepts/op-params.md
OpParams = {
  -- constructed-operator surfaces (the kernel touches OpParams ONLY through these)
  T          : ConstructedOp,        -- the apply surface (preconditioned operator)
  orthog?    : OrthogSurface,        -- GMRES/Arnoldi only; absent (no-op) for CG
  scalars?   : ScalarSurface,        -- Chebyshev polynomial-recurrence scalars; absent otherwise
  eps        : Convergence,          -- the stopping-predicate surface

  -- variant selectors (closed over by the surfaces above; not read by the kernel body)
  pc_side    : PreconditionerSide,
  gs_orthog  : Orthogonalization,
  flexible   : Bool,
  poly_kind? : PolynomialKind,
  restart    : RestartMode,

  -- termination knobs (close into eps)
  max_dim    : Int,
  max_it     : Int,
  rel_tol    : Scalar,
  abs_tol    : Scalar
}
```

## `SimState` — sim-state stratum (run-time-evolved)

Shared across `iteration` (the `krylov-step` kernel's monadic effect *is* the `SimState` transition) and `coordination` (the `Solve = StateT SimState Identity` caps thread it; `solve_family` collects it). The externally-visible quantities a Krylov-shaped solve evolves and reports; **uniform across all slices** (CG / GMRES / FGMRES / Chebyshev share this exact five-field shape). Authoritative field schema: [`sim-state`](../concepts/sim-state.md).

```text
-- the value threaded by `Solve a = StateT SimState Identity a`; every field run-time.
-- the iterate `x` is named with shape group S (semantics/index.md §1.2.1), not a rank-1 axis.
-- Authoritative schema + field strata + L0 home: concepts/sim-state.md
SimState = {
  x           : Tensor[(S: ...)],   -- the current iterate (the solve's primary product)
  it          : Int,                -- iteration count
  converged   : Bool,               -- convergence flag
  final_res   : Scalar,             -- final (absolute) residual, possibly an estimate
  initial_res : Scalar              -- initial (absolute) residual, captured at solve entry
}
```

The `Solve` monad (`Solve a = StateT SimState Identity a`) that threads `SimState` is the coordination surface — its rendered form lives in the [`coordination`](./coordination.md) library; here we render only the state type the two groups share.

## Status

`navigational-container` (rendered library chapter). Holds the rendered synthesized form of the three cross-cutting shared types (`IoData`, `OpParams`, `SimState`); the authoritative field schemas live in the linked `concepts/` record-definition pages. Single-group-clustering types are deliberately absent (placed before their API group in Wave 2 per the type-placement rule).
```

### 3. NEW FILE — `book/src/synthesis/iteration.md` (intro shell — Wave 2 fills the bodies)

```edit:book/src/synthesis/iteration.md
[old]:
[new]:
---
status: stub
kind: navigational-container (synthesis library — iteration; def bodies pending Wave-2 rendering)
# Intro shell. No `rank:` — implementation VIEW, reference-class links only.
edges:
  reference:
    - L4/iteration-combinators-intro
    - L4/chebyshev
    - L4/iterate-while
    - L4/iterate-while-with-prev
    - L4/krylov-step
    - synthesis/types
    - synthesis/index
---

# Library `iteration` — iteration & step combinators

> **Status: `stub`.** This is the library intro shell. The per-operator synthesized def bodies are rendered into this chapter in Wave 2 (abstractor). The shell establishes the operator list, the topological order, and the rendering conventions so the def-rendering dispatch can fill it.

The synthesized rendering of the L4 [Iteration & step combinators](../L4/iteration-combinators-intro.md) doc-group: the value-threaded loop combinators and the step kernels that drive Palace's iterative algorithms. Implementation VIEW — links to the authoritative L4 chapters for laws/semantics, renders the synthesized code form here.

## Operators this library holds (topological order)

A def appears after everything it uses. The expected order (refine by use):

1. [`iterate-while`](../L4/iterate-while.md) — value-threaded tail-recursive loop with demand-pruned trajectory; the canonical iteration primitive (everything below uses it).
2. [`iterate-while-with-prev`](../L4/iterate-while-with-prev.md) — carry-bootstrapped variant threading a `PrevCarry` closure; degenerates to `iterate-while` when `β = ()`.
3. [`krylov-step`](../L4/krylov-step.md) — the typed-wrapper Krylov step kernel; Form A consumes `iterate-while`, Form B consumes `iterate-while-with-prev`.
4. [`chebyshev`](../L4/chebyshev.md) — the fixed-degree polynomial smoother; both bounded loops are `iterate-while` folds with step-count predicates.

## Clustering types (placed BEFORE the group in Wave 2)

Per the [type-placement rule](./index.md#type-placement--cluster-a-type-with-its-api-group), the iteration-clustering state carriers — [`Krylov`](../concepts/krylov.md) (the ephemeral per-restart workspace), [`StepOutputs`](../concepts/step-outputs.md), [`PrevCarry`](../concepts/prev-carry.md) — are rendered **immediately before** the operator group, bundled with their utility API (constructors / accessors / predicates). Their consumer methods stay in the group AFTER the type+utility block. The cross-cutting `SimState` / `OpParams` are shared and live in [`types`](./types.md), not here.

## Rendering conventions

Per the [Synthesis overview](./index.md#rendering-conventions): topological def order; `#extern NAME` after the type signature for any opaque-kernel boundary; deep-linked-unchanged lower artifacts rendered inline; Haskell `where` for private helpers; code-doc per def; `$`-sigil pseudocode inside ` ```text ` fences (KaTeX rule); link to `../L4/<op>.md`, do not re-cite L0.
```

### 4. NEW FILE — `book/src/synthesis/data-algebra.md` (intro shell — Wave 2 fills the bodies)

```edit:book/src/synthesis/data-algebra.md
[old]:
[new]:
---
status: stub
kind: navigational-container (synthesis library — data-algebra; def bodies pending Wave-2 rendering)
# Intro shell. No `rank:` — implementation VIEW, reference-class links only.
edges:
  reference:
    - L4/data-algebra-combinators-intro
    - L4/linear_combination
    - L4/inner_product
    - L4/dot
    - L4/nrm2
    - L4/fe_assemble
    - L4/mk_matrix_free_operator
    - L4/eliminate_bc
    - L4/assemble_frequency_operator
    - L4/gram_reduce
    - L4/domain_energy_reduce
    - L4/eigenfreq_qfactor_reduce
    - L4/sparameter_reduce
    - L4/waveguide_mode_reduce
    - L4/sharding-decompose-reduce
    - synthesis/types
    - synthesis/index
---

# Library `data-algebra` — data-algebra combinators & named verbs

> **Status: `stub`.** This is the library intro shell. The per-operator synthesized def bodies are rendered into this chapter in Wave 2 (abstractor). The shell establishes the operator list, the topological order, and the rendering conventions so the def-rendering dispatch can fill it.

The synthesized rendering of the L4 [Data-algebra combinators & named verbs](../L4/data-algebra-combinators-intro.md) doc-group: the pure value-producing combinators (folds + reductions) and the kept named verbs the backend wants. Implementation VIEW — links to the authoritative L4 chapters for laws/semantics, renders the synthesized code form here.

## Operators this library holds (topological order)

A def appears after everything it uses. The expected order (refine by use) — the general folds first, then their named-verb specializations / consumers, then the reductions and the assemble verbs that compose them:

- [`linear_combination`](../L4/linear_combination.md) — the scalar-weighted-tensor-sum fold (the four arity leaves `scal`/`axpy`/`axpby`/`axpbypcz` are specialization notes tied below).
- [`inner_product`](../L4/inner_product.md) — the reduce-to-scalar inner-product combinator.
- [`dot`](../L4/dot.md) — the Hermitian/symmetric inner-product verb (specialization of `inner_product` at `M=I`).
- [`nrm2`](../L4/nrm2.md) — the Euclidean-norm verb (`√∘abs∘inner_product`; a CONSUMER, not a fold member).
- [`gram_reduce`](../L4/gram_reduce.md) — the operator-weighted symmetric-Gram reduce-to-matrix.
- [`mk_matrix_free_operator`](../L4/mk_matrix_free_operator.md) — the matrix-free operator constructor (libCEED quadrature leaf renders `#extern`; the matrix-free impl `libceed-quadrature-kernel-impl` renders inline where firm).
- [`fe_assemble`](../L4/fe_assemble.md) — the assemble-fold combinator (the opaque per-term `assemble_term` libCEED leaf renders `#extern`).
- [`eliminate_bc`](../L4/eliminate_bc.md) — the post-assembly BC-application verb-pair (the RHS side is one `linear_combination`).
- [`assemble_frequency_operator`](../L4/assemble_frequency_operator.md) — the per-ω system-operator assembly verb (operator-operand specialization of `linear_combination`).
- [`domain_energy_reduce`](../L4/domain_energy_reduce.md) — the per-domain energy-table reduction.
- [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) — the per-mode (f, Q) scalar-table reduction.
- [`sparameter_reduce`](../L4/sparameter_reduce.md) — the driven S-parameter reduction.
- [`waveguide_mode_reduce`](../L4/waveguide_mode_reduce.md) — the boundary-mode waveguide-mode-table reduction.
- [`sharding-decompose-reduce`](../L4/sharding-decompose-reduce.md) — **rank-0 `roadmap_goal`**: render as a **future-direction stub note** (a claim-free placeholder, NOT a firm def), preserving the DIRECTIVE-1 boundary (MPI mechanism cited-not-lifted).

## Clustering types (placed BEFORE the group in Wave 2)

Per the [type-placement rule](./index.md#type-placement--cluster-a-type-with-its-api-group): the data-algebra-clustering types — [`DofSet`](../concepts/dofset.md) (consumed by `eliminate_bc`), [`WaveguideModeTable`](../concepts/WaveguideModeTable.md) (produced by `waveguide_mode_reduce`) — are rendered immediately before the relevant operators, bundled with their utility API. Cross-cutting types live in [`types`](./types.md).

## Rendering conventions

Per the [Synthesis overview](./index.md#rendering-conventions): topological def order; `#extern NAME` after the type signature for opaque kernels (libCEED quadrature in `fe_assemble` / `mk_matrix_free_operator`); deep-linked-unchanged lower artifacts inline; Haskell `where` for private helpers; code-doc per def; `$`-sigil pseudocode inside ` ```text ` fences; named shape groups for shape-generic ops; link to `../L4/<op>.md`, do not re-cite L0.
```

### 5. NEW FILE — `book/src/synthesis/coordination.md` (intro shell — Wave 2 fills the bodies)

```edit:book/src/synthesis/coordination.md
[old]:
[new]:
---
status: stub
kind: navigational-container (synthesis library — coordination; def bodies pending Wave-2 rendering)
# Intro shell. No `rank:` — implementation VIEW, reference-class links only.
edges:
  reference:
    - L4/outer-driver-combinators-intro
    - L4/preconditioning-framework
    - L4/ksp_solve
    - L4/eigsolve
    - L4/solve_family
    - L4/fold_solve
    - L4/frequency_sweep
    - synthesis/types
    - synthesis/index
---

# Library `coordination` — outer-driver caps & coordination combinators

> **Status: `stub`.** This is the library intro shell. The per-operator synthesized def bodies are rendered into this chapter in Wave 2 (harvester). The shell establishes the operator list, the topological order, and the rendering conventions so the def-rendering dispatch can fill it.

The synthesized rendering of the L4 [Outer-driver caps & coordination combinators](../L4/outer-driver-combinators-intro.md) doc-group: the `Solve`-monadic outer-driver caps and the map/fold coordination combinators that drive the iteration kernels to convergence and over RHS / schedule / frequency families. Implementation VIEW — links to the authoritative L4 chapters for laws/semantics, renders the synthesized code form here.

## Operators this library holds (topological order)

A def appears after everything it uses. The expected order (refine by use) — the construction/binding framework first, then the caps, then the combinators that map/fold over them:

- [`preconditioning-framework`](../L4/preconditioning-framework.md) — the `buildKspSolver` / `setOperators` construction-and-binding framework (the non-iteration construction surface the caps run against).
- [`ksp_solve`](../L4/ksp_solve.md) — the `Solve`-monadic outer-driver cap for preconditioned Krylov solves (folds `krylov-step` from the [`iteration`](./iteration.md) library).
- [`eigsolve`](../L4/eigsolve.md) — the `Solve`-monadic eigenproblem cap; the SLEPc EPS eigsolve loop renders **`#extern`** at the kernel-API boundary, the constructive `eigsolve-impl` (Lanczos/Arnoldi/Krylov-Schur in `lanczos_step`/`krylov-step` vocabulary) renders inline where firm.
- [`solve_family`](../L4/solve_family.md) — the fixed-operator map-over-RHS-family combinator.
- [`fold_solve`](../L4/fold_solve.md) — the state-threaded fold-over-schedule combinator.
- [`frequency_sweep`](../L4/frequency_sweep.md) — the per-ω operator-VARYING sweep combinator (rebuilds the operator inside the map via `assemble_frequency_operator`).

## Clustering types (placed BEFORE the group in Wave 2)

Per the [type-placement rule](./index.md#type-placement--cluster-a-type-with-its-api-group): the coordination-clustering state carriers — the per-solver state carriers `EigState` / `SimState`-family caps and [`SolveResult`](../concepts/solve-result.md) — are rendered immediately before the group, bundled with their utility API; consumer methods stay in the group. The cross-cutting `SimState` / `OpParams` / `IoData` live in [`types`](./types.md). The `Solve = StateT SimState Identity` monad (the `solve-monad` outer-driver vocabulary) is rendered here as the coordination surface.

## Rendering conventions

Per the [Synthesis overview](./index.md#rendering-conventions): topological def order; `#extern NAME` after the type signature for the SLEPc EPS loop in `eigsolve`; deep-linked-unchanged lower artifacts inline; Haskell `where` for private helpers; code-doc per def; `$`-sigil pseudocode inside ` ```text ` fences; link to `../L4/<op>.md`, do not re-cite L0.
```

### 6. NEW FILE — `book/src/synthesis/drivers.md` (intro shell — body DEFERRED to a later batch-44 cycle)

```edit:book/src/synthesis/drivers.md
[old]:
[new]:
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
```

### 7. EDIT — `book/src/SUMMARY.md` (wire the `# Synthesis` Part immediately before `# Feature surfaces`)

```edit:book/src/SUMMARY.md
[old]:
[Introduction](./introduction.md)
# Methodology
- [Overview](./methodology/overview.md)
- [Goal & Flow](./methodology/goal-flow.md)
- [Resolution ladder & reachability](./methodology/resolution-ladder.md)
- [Graded-stack scheme (node-status + typed edges)](./methodology/graded-stack-scheme.md)
- [Semantic consolidation (active-management semantic surface)](./methodology/semantic-consolidation.md)
# Feature surfaces — entry points
[new]:
[Introduction](./introduction.md)
# Methodology
- [Overview](./methodology/overview.md)
- [Goal & Flow](./methodology/goal-flow.md)
- [Resolution ladder & reachability](./methodology/resolution-ladder.md)
- [Graded-stack scheme (node-status + typed edges)](./methodology/graded-stack-scheme.md)
- [Semantic consolidation (active-management semantic surface)](./methodology/semantic-consolidation.md)
# Synthesis — synthesized-library implementation view
- [Overview](./synthesis/index.md)
- [Library — types (shared cross-cutting type defs)](./synthesis/types.md)
- [Library — iteration (iteration & step combinators)](./synthesis/iteration.md)
- [Library — data-algebra (data-algebra combinators & named verbs)](./synthesis/data-algebra.md)
- [Library — coordination (outer-driver caps & coordination combinators)](./synthesis/coordination.md)
- [Library — drivers (entry-point surfaces)](./synthesis/drivers.md)
# Feature surfaces — entry points
```

## Supporting evidence

- **Directive source:** CLAUDE.md §"The SYNTHESIS section — the synthesized-library implementation view (user directive 2026-06-07)" — the 5-library partition (`types` → `iteration` / `data-algebra` / `coordination` → `drivers`), the type-placement rule, `#extern NAME`-after-type-sig, deep-link-inline, topological order, Haskell `where`, implementation-VIEW-links-not-restates, ownership (layer-intro-author authors the Part shell + per-library intros + `types` + `drivers`). Memory `project_synthesis_section_directive`.
- **L4 doc-group → library mapping** confirmed on disk `book/src/SUMMARY.md:65-91` and `book/src/L4/index.md`: `iteration` ← Iteration & step combinators (4 ops); `data-algebra` ← Data-algebra combinators & named verbs (14 ops, incl. the rank-0 `sharding-decompose-reduce`); `coordination` ← Outer-driver caps & coordination combinators (6 ops).
- **Shared cross-cutting types (≥2 API groups → `types` library):**
  - `IoData` ([`config-record`](book/src/concepts/config-record.md)) — `reference`-listed by every `feature/*.L4` column (drivers) + read by coordination caps.
  - `OpParams` ([`op-params`](book/src/concepts/op-params.md):84-85) — read by `iteration` (krylov-step) AND `coordination` (ksp_solve/solve_family/fold_solve); the page's "Used by" list names `L4/krylov-step` + the `solve-monad` surface, and the Status line states the record is "referenced by ≥2 consumers" (`op-params.md:97`).
  - `SimState` ([`sim-state`](book/src/concepts/sim-state.md):66-71) — "Used by" lists `L4/krylov-step` (iteration) + `solve-monad`/`convergence-test` (coordination); uniform across slices.
- **Single-group-clustering types (NOT in `types` — placed before their API group in Wave 2):** `Krylov`/`StepOutputs`/`PrevCarry` ↔ iteration; `DofSet`/`WaveguideModeTable` ↔ data-algebra; `SolveResult` ↔ coordination. Confirmed present under `book/src/concepts/`.
- **Navigational-container frontmatter form** copied from the landed `book/src/L4/index.md:1-11` + `book/src/feature/index.md:1-11` (`kind: navigational-container`, `edges: reference:`-only, NO `rank:`) per the graded-stack scheme §5/§6 — the two graded-stack linters key off these tags.
- **`$`-sigil-fence rule** (memory `project_katex_dollar_sigil_fence_requirement`): the `Tensor[(S: ...)]` / `Tensor[$S]` renderings in `types.md` (`SimState.x`) are inside ` ```text ` fences, copying the landed `concepts/sim-state.md:33-41` form.

## Open questions / caveats

- **`EigState` has no `concepts/` record-definition home yet.** The `coordination` library intro names `EigState` as a coordination-clustering state carrier (per the directive's coordination type-placement example, and `coordination`'s D4 scope). There is NO `book/src/concepts/EigState.md` (the `concepts/` ls shows `sim-state`, `op-params`, `krylov`, `solve-result`, `step-outputs`, `prev-carry`, `dofset`, `WaveguideModeTable`, `config-record` — no `EigState`). Flag: `record-EigState-needs-definition-home` — if `EigState` is named in the rendered `eigsolve`/eigenmode coordination def signatures (≥2 consumers → page; 1 consumer → in-chapter section), a record-definition home must be dispatched. Wave-2 D4 (harvester, coordination) should either confirm `EigState` collapses to `SimState` for the eigen cap (then no new home) or flag the home. Not blocking this shell.
- **Type-placement boundary is a per-type Wave-2 judgment.** I placed only the three unambiguous ≥2-group types (`IoData`/`OpParams`/`SimState`) in `types`. `SolveResult` is `reference`-listed primarily by coordination (likely single-group → cluster), but if a `drivers` output-product also names it directly it would cross the ≥2-group bar and migrate to `types`. I left it clustering with `coordination`; the Wave-2 D4 harvester should flag if a second API-group consumer surfaces (semantic-consolidation: define once — migrate, don't duplicate).
- **`drivers` library body deferred (multi-cycle arc).** Per the directive's LEAD-sequencing (d), `drivers` composes everything and is authored last. This shell seeds it as `stub`; a later batch-44 cycle authors the body (after the 3 calculus library def bodies land). The per-driver config records cluster before their driver column with the config's utility API.
- **Role-specs not yet carrying the Synthesis discipline.** The `layer-intro-author` / `abstractor` / `harvester` / `lowering-verifier` role-specs do not yet encode the Synthesis chapter-KIND mechanics (the batch-44 meta-phase codifies them). This shell + the dispatch scopes carry the load-bearing bullets from CLAUDE.md §SYNTHESIS in-line. Flag for the batch-44 meta: codify the Synthesis chapter-KIND mechanics (type-placement, `#extern`, deep-link-inline, implementation-VIEW-links-not-restates) into the role-specs.
- **Synthesis adds NO `depends-on` edges.** Every Synthesis chapter is reference-reachable navigational (implementation VIEW); it links reference-class to the authoritative L4/semantics/concepts defs and constrains no firm node's rank/liveness. This is the property the D5 maintenance-floor cross-cutter is asked to confirm for the post-apply tree (the `#extern` callouts in D2/D3/D4 must not mis-type a `depends-on` edge to the opaque kernels).
