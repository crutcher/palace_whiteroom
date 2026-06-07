---
agent: layer-intro-author
invoked_at: 2026-06-07T054924Z
scope: FiniteElementSpaceHierarchy record concepts-page promotion + multigrid→fe_space_hierarchy RE9-edge VERIFY (cycle-121 D2, dep D1)
status: pending
integrated_at: 2026-06-07T054924Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean. concepts/FiniteElementSpaceHierarchy.md firm + fe_space_hierarchy Record-def trim (>=2-consumer promotion)."
---

# CYCLE: `FiniteElementSpaceHierarchy` record concepts-page promotion (RE9 grounding)

## Summary

Two-part dispatch (cycle-121 D2, Wave-2, dep D1):

**Part 1 — `multigrid → fe_space_hierarchy` GROUND edge (RE9 discharge): VERIFY, do NOT
duplicate.** D1's GMG column (`reports/.../layer-intro-author-geometric-multigrid-preconditioner/CYCLE.md`)
**already authors the faithful `depends-on (composes)` edge** to `L1/fe_space_hierarchy` on
**both** GMG levels (`GMG.L4` frontmatter `depends-on: target: L1/fe_space_hierarchy / kind:
composes # GetProlongationOperators() ... (GROUNDS RE9)`; same on `GMG.L1`). I verified the
edge is (a) faithful — the GMG preconditioner genuinely consumes `GetProlongationOperators()`
(and `GetDiscreteInterpolators()`) by name at the construction site `ksp.cpp:221,228`, and the
V-cycle restricts (`Pᵀ`) / prolongs (`P`) over `P[l]` (`RealMultTranspose(*P[l-1], …)` `gmg.cpp:191` / `RealMult(*P[l-1], …)` `gmg.cpp:199`); (b) well-founded —
`rank(GMG)=rough-in (2) ≤ rank(fe_space_hierarchy)=firm (3)`; and (c) RE9-grounding — it makes
the currently-detritus `L1/fe_space_hierarchy` node **reachable from the GC-root GMG column**.
**No edit from me on Part 1** (duplicating D1's edge would be a double-author). I flag the
shared-edge coordination for the integrator below.

**Part 2 — `FiniteElementSpaceHierarchy` record concepts-page promotion (the ≥2-consumer bar,
`record-FiniteElementSpaceHierarchy-promote-watch` NOW FIRING).** Judgment: **the bar IS met
→ promote.** The record now has **two** referencing chapters: (1) `L1/fe_space_hierarchy` (the
**producer** + current sole in-chapter §Record-definition home), and (2) the **GMG
preconditioner column** (D1, landing this cycle), which consumes the record by name
(`GetProlongationOperators()` / `GetDiscreteInterpolators()` / the V-cycle `P[l]` transfers).
The bar is "≥2 **consumers**" (NOT "≥2 *firm* consumers") — same ≥2-consumer bar as the
`concepts/mesh.md` precedent, which counts its producer `build_mesh` among the ≥2 — so the
D1-rough-in consumer counts (a record page is a `reference` target, named-by-use; it does not
block on consumer maturity). I therefore promote `FiniteElementSpaceHierarchy` from the
in-chapter `L1/fe_space_hierarchy.md:120-141` §Record-definition → a `concepts/FiniteElementSpaceHierarchy.md`
record page (the data shape — fields / types / meaning / construction-vs-run-time stratum / L0
backing struct), trim the in-chapter section to a back-link (the "a record lives ONCE"
discipline — the in-chapter §Record-definition becomes a pointer), and update the
"sole … producer/consumer" prose now that a 2nd consumer exists.

Deliverables:
1. `book/src/concepts/FiniteElementSpaceHierarchy.md` (new) — the record-definition page.
2. `book/src/L1/fe_space_hierarchy.md` — trim the in-chapter §Record-definition to a back-link;
   fix the "single-consumer / sole harvested … producer/consumer" prose; add a `reference` edge
   to the new concepts page.
3. `book/src/SUMMARY.md` — wire the new page into the Concepts Part in alpha position.

## Proposed changes

### 1. New record-definition concepts page

```new-file:book/src/concepts/FiniteElementSpaceHierarchy.md
---
rank: firm
kind: record
edges:
  depends-on:
    - target: palace/fem/fespace.hpp:200-286
      kind: cites-evidence            # class FiniteElementSpaceHierarchy: fespaces (:203), mutable lazy P (:204) + BuildProlongationAtLevel (:206), seed ctor (:210-213), AddLevel = push_back + nullptr slot (:217-221), accessors GetNumLevels/GetFESpaceAtLevel/GetFinestFESpace/GetProlongationAtLevel/GetProlongationOperators/GetDiscreteInterpolators (:215-285)
  reference:
    - L1/fe_space_hierarchy
    - L1/fe_space
    - feature/geometric-multigrid-preconditioner.L4
    - feature/geometric-multigrid-preconditioner.L1
    - concepts/mesh
    - concepts/build-time-vs-run-time-stratification
---

# FiniteElementSpaceHierarchy

> **Kind: `record`.** This page defines the *data shape* of `FiniteElementSpaceHierarchy` —
> its fields, their types and meaning, the construction-vs-run-time stratum of each, and the
> L0 source home the backing C++ class mirrors. The *behaviour* — how
> [`fe_space_hierarchy`](../L1/fe_space_hierarchy.md) constructs it (the `AddLevel`-fold) and
> how the [geometric-multigrid preconditioner](../feature/geometric-multigrid-preconditioner.L4.md)
> consumes its prolongation level-stack — lives in those chapters; this page does not restate
> that algebra.

`FiniteElementSpaceHierarchy` is the Palace **coarse-to-fine stack of typed finite-element
spaces** — the geometric/p-multigrid level hierarchy the multigrid preconditioner relaxes
over. It is **produced** by [`fe_space_hierarchy`](../L1/fe_space_hierarchy.md)
(`fe_space_hierarchy :: [Mesh] -> [FECollection] -> Config -> FiniteElementSpaceHierarchy`,
the `AddLevel`-fold) and **consumed** by the
[geometric-multigrid preconditioner](../feature/geometric-multigrid-preconditioner.L4.md) — the
V-cycle's inter-level transfers are exactly this record's per-level prolongation operators
`P[l]` (`GetProlongationOperators()` / `GetDiscreteInterpolators()` passed to the
`GeometricMultigridSolver` constructor, `palace/linalg/ksp.cpp:221,228`). Two distinct
consumers (producer + GMG column) put it at the ≥2-consumer bar, so it has a cross-cutting
definition home here rather than only an in-chapter section in its producing chapter.

## One-line semantics

`FiniteElementSpaceHierarchy` is an immutable coarse-to-fine **list of [`fe_space`](../L1/fe_space.md)
values** (`fespaces[0]` coarsest, `fespaces.back()` finest) plus a **lazily-materialized
per-level prolongation operator stack** `P[l]` (each lifting level `l → l+1`). It carries no
algebra of its own: the [`fe_space_hierarchy`](../L1/fe_space_hierarchy.md) fold builds it, the
multigrid V-cycle reads its prolongations, and the accessors below are read-as-given.

## Record definition

`FiniteElementSpaceHierarchy` is the backing C++ `class FiniteElementSpaceHierarchy`
(`palace/fem/fespace.hpp:200`). The TS brace form (immutable level stack once built;
per-field strata below):

```text
FiniteElementSpaceHierarchy = {
  fespaces : [FiniteElementSpace],   -- coarse-to-fine level stack; [0] coarsest, back() finest
  P        : [Operator?]             -- per-level prolongation operators P[l] : level l -> l+1
                                     --   (mutable; lazily built; nullptr until first request)
}
```

| field | type | meaning | stratum | L0 source |
|---|---|---|---|---|
| `fespaces` | `[FiniteElementSpace]` | the coarse-to-fine level stack; `fespaces[0]` the coarsest, `fespaces.back()` the finest. Each element is one [`fe_space`](../L1/fe_space.md) value. | construction-time (built by the `AddLevel`-fold; thereafter read-only) | `palace/fem/fespace.hpp:203` |
| `P` | `[Operator?]` (`mutable`) | per-level **prolongation** operators (`P[l]` lifts level `l → l+1`); **lazily** materialized on first `GetProlongationAtLevel(l)` via `BuildProlongationAtLevel` — `nullptr` until then. The V-cycle's `restrict = Pᵀ`, `prolong = P` over exactly these. | run-time (lazy; populated on demand during the multigrid solve, NOT at construction) | `palace/fem/fespace.hpp:204,206` |

The single-machine **read surface** (read-as-given accessors, NOT operations): `GetNumLevels`
(`fespace.hpp:215`), `GetFESpaceAtLevel` (`:223-234`), `GetFinestFESpace` (`:236-247`),
`GetProlongationAtLevel` / `GetProlongationOperators` (`:249-267`),
`GetDiscreteInterpolatorAtLevel` / `GetDiscreteInterpolators` (`:269-285`). The
`GetProlongationOperators()` accessor returns the `GetNumLevels()-1`-length `P[l]` list (one
per inter-level transfer) and is the exact value the multigrid preconditioner consumes by name.

## Stratum — construction-time stack, run-time-lazy prolongations

The two fields split across the stratum boundary (the
[`build-time-vs-run-time-stratification`](./build-time-vs-run-time-stratification.md) pattern):

- **`fespaces` is construction-stratum.** The level stack is built once by the
  [`fe_space_hierarchy`](../L1/fe_space_hierarchy.md) `AddLevel`-fold (the coarse seed
  `make_unique<FiniteElementSpace>` + the h-/p-refinement `AddLevel` loops) at the start of the
  solve and consumed read-only thereafter; `AddLevel` is strict `push_back` + a `nullptr`
  prolongation slot (`fespace.hpp:217-221`).
- **`P` is run-time-lazy.** Each prolongation slot is `nullptr` after the fold; the operator is
  materialized **on demand** the first time `GetProlongationAtLevel(l)` is called
  (`P[l] ? *P[l] : BuildProlongationAtLevel(l)`, `fespace.hpp:249-255`) — i.e. during the
  multigrid solve, not at construction. The `mutable` keyword on `P` (`fespace.hpp:204`) marks
  it as written-during-`const`-access, the run-time-lazy-cache stratum (the `Mesh.geom_data`
  precedent on [`concepts/mesh`](./mesh.md)). This is read-as-given here, NOT a lifted L1
  operation: the prolongation-build machinery (`BuildProlongationAtLevel`) is sibling-pull-gated
  per the [`fe_space`](../L1/fe_space.md) / [`fe_space_hierarchy`](../L1/fe_space_hierarchy.md)
  deferred-sibling lists.

## L0 source home — the `class FiniteElementSpaceHierarchy`

The backing C++ class is `class FiniteElementSpaceHierarchy` (`palace/fem/fespace.hpp:200-286`):
the protected level vector `fespaces` (`:203`); the `mutable` lazy prolongation vector `P`
(`:204`) + the protected `BuildProlongationAtLevel` (`:206`); the single-arg seed ctor
(`:210-213`, delegating to `AddLevel`); `AddLevel` = `push_back` + `nullptr` slot (`:217-221`);
and the read surface (`:215-285`). The hierarchy value flows from the
[`fe_space_hierarchy`](../L1/fe_space_hierarchy.md) fold
(`ConstructFiniteElementSpaceHierarchy`, `palace/fem/multigrid.hpp:78-126`, `return fespaces`
`:125`) into the Krylov-solver setup, where `GetProlongationOperators()` (and, when an
auxiliary space is present, `GetDiscreteInterpolators()`) are passed to the
`GeometricMultigridSolver` constructor (`palace/linalg/ksp.cpp:221,228`).

**Single-machine carve-outs (flagged once).** Each `FiniteElementSpace` in the stack wraps an
`mfem::ParFiniteElementSpace` (read single-rank per the standing `par-types-single-rank-reading`
rule); the prolongation operators `P[l]` are the single-rank inter-level transfer operators.
Mesh partitioning / multi-rank distribution is out of scope (per CLAUDE.md §Scope). This record
carries the level stack but does not define the multi-rank transfer semantics.

## Signatures that name this record

The ≥2-consumer evidence for the standalone page (the `record-FiniteElementSpaceHierarchy-promote-watch`
firing — producer + GMG column):

- [`fe_space_hierarchy`](../L1/fe_space_hierarchy.md) — the **producer**:
  `fe_space_hierarchy :: [Mesh] -> [FECollection] -> Config -> FiniteElementSpaceHierarchy`
  (`book/src/L1/fe_space_hierarchy.md:35,87`).
- [geometric-multigrid preconditioner](../feature/geometric-multigrid-preconditioner.L4.md) —
  the **consumer**: the V-cycle composes the record's `GetProlongationOperators()` level-stack
  by name (the `depends-on (composes)` edge `GMG.L4 → L1/fe_space_hierarchy`, GROUNDING RE9;
  `book/src/feature/geometric-multigrid-preconditioner.L4.md`); the L1 surface
  ([`geometric-multigrid-preconditioner.L1`](../feature/geometric-multigrid-preconditioner.L1.md))
  renders the same `restrict = apply_transpose (P[l])` / `prolong = apply (P[l])` transfers.

**Further (non-blocking) fan-out** — the same `GeometricMultigridSolver` (hence the same
hierarchy-prolongation consumption) is also constructed by the firm
[`divfree-projector`](../L1/divfree-projector.md) (`palace/linalg/divfree.cpp:128`), the
H(curl) mass-matrix solver (`palace/linalg/hcurl.cpp:101`), and the AMR flux-recovery error
estimator (`palace/linalg/errorestimator.cpp:86`). These are additional driver-agnostic
consumers of the hierarchy via the GMG infrastructure column; they corroborate the record's
cross-cutting status but are mediated through the GMG column (the consumer named above), so the
≥2 bar is met by producer + GMG column alone.

## See also

- [`fe_space_hierarchy`](../L1/fe_space_hierarchy.md) — the producer; defines HOW the hierarchy
  is constructed (the `AddLevel`-fold over per-level [`fe_space`](../L1/fe_space.md)
  constructions). This page defines only the *shape* of its output.
- [geometric-multigrid preconditioner](../feature/geometric-multigrid-preconditioner.L4.md) —
  the consumer; defines the *behaviour over* the prolongation stack (the V-cycle
  restrict/recurse/prolong). This page does NOT restate that algebra.
- [`fe_space`](../L1/fe_space.md) — the element type of `fespaces` (each level is one
  `FiniteElementSpace`).
- [`mesh`](./mesh.md) — the analogous FE-construction record (the `[Mesh]` element of the
  hierarchy's input), same record-definition-page pattern.
- [`build-time-vs-run-time-stratification`](./build-time-vs-run-time-stratification.md) — the
  per-field split (`fespaces` construction-time; `P` run-time-lazy).

**If this page and a consumer chapter / the L0 source disagree on any factual claim about the
record, the L0 source (`palace/fem/fespace.hpp`) wins and this page is corrected.**

## Status

`firm` — the data shape is read directly from the positive `class FiniteElementSpaceHierarchy`
(`palace/fem/fespace.hpp:200-286`): the level vector `fespaces` (`:203`), the `mutable` lazy
prolongation vector `P` (`:204`) + `BuildProlongationAtLevel` (`:206`), the seed ctor
(`:210-213`), `AddLevel` = `push_back` + `nullptr` slot (`:217-221`), and the read surface
`GetNumLevels`/`GetFESpaceAtLevel`/`GetFinestFESpace`/`GetProlongationAtLevel`/`GetProlongationOperators`/`GetDiscreteInterpolators`
(`:215-285`). The construction-vs-run-time stratum per field is read off the `mutable`-marking
+ the lazy `BuildProlongationAtLevel` materialization. The record-definition obligation is met:
this is the cross-cutting home for `FiniteElementSpaceHierarchy`, referenced by ≥2 consumers
(`L1/fe_space_hierarchy` producer + the geometric-multigrid-preconditioner column). All L0
citations self-verified against on-disk source this dispatch via codemap `read_range`.

Well-foundedness (rank): the page is a `record` DAG node at `rank: firm`; its only blocking
edge is `cites-evidence depends-on` to the L0 `class FiniteElementSpaceHierarchy` range
(rank-terminal ground truth), so the `rank(u) ≤ rank(v)` invariant holds vacuously. The edges
to the producer/consumer chapters are `reference` (navigational — a record page is named-by-use,
it does not block on its consumers; the GMG consumer being rough-in does not gate this firm
record page).
```

### 2. Trim the in-chapter §Record-definition to a back-link + fix the sole-consumer prose

The "a record lives ONCE" discipline: now that `FiniteElementSpaceHierarchy` has a
cross-cutting concepts page, the in-chapter §Record-definition becomes a pointer (keeping only
the producer-local note that the fold builds the level stack). The "single-consumer / sole
harvested L1 producer/consumer" claim is now stale (the GMG column is the 2nd consumer) and is
corrected. A `reference` edge to the new concepts page is added to the frontmatter.

```edit:book/src/L1/fe_space_hierarchy.md
[old]:  reference:
    - L1/build_mesh                # the [Mesh] input element type — the `Mesh` record home (D3 this cycle); navigational, NOT a depends-on
---
[new]:  reference:
    - L1/build_mesh                # the [Mesh] input element type — the `Mesh` record home (D3 this cycle); navigational, NOT a depends-on
    - concepts/FiniteElementSpaceHierarchy   # the output record's cross-cutting definition home (promoted c121; producer + GMG-column consumers ≥2)
---
```

```edit:book/src/L1/fe_space_hierarchy.md
[old]:## Record definition: `FiniteElementSpaceHierarchy`

The output record is defined here (single-consumer: `fe_space_hierarchy` is the
sole harvested L1 producer/consumer of this type; its downstream
geometric-multigrid solver consumers are not yet L1-harvested). The backing C++
class is `palace::FiniteElementSpaceHierarchy` (`palace/fem/fespace.hpp:200-286`).

| field | type | meaning | stratum |
|---|---|---|---|
| `fespaces` | `[FiniteElementSpace]` | the coarse-to-fine level stack; `fespaces[0]` the coarsest, `fespaces.back()` the finest. Each is one [`fe_space`](./fe_space.md) value. (`fespace.hpp:203`) | construction-time (built by the fold; thereafter read-only) |
| `P` | `[Operator?]` | per-level **prolongation** operators (`P[l]` lifts level `l` → `l+1`); `mutable`, **lazily** materialized on first `GetProlongationAtLevel(l)` via `BuildProlongationAtLevel` (`fespace.hpp:204,206,249-255`) — `nullptr` until then. | run-time (lazy; populated on demand during the multigrid solve, not at construction) |

Accessors (read-as-given, NOT L1 operations): `GetNumLevels`
(`fespace.hpp:215`), `GetFESpaceAtLevel` (`:223-234`), `GetFinestFESpace`
(`:236-247`), `GetProlongationAtLevel` / `GetProlongationOperators`
(`:249-267`), `GetDiscreteInterpolatorAtLevel` / `GetDiscreteInterpolators`
(`:269-285`). The prolongation/interpolator machinery is **sibling-pull-gated**:
the `BuildProlongationAtLevel` (multigrid transfer) and discrete-interpolator
construction are read-as-given properties of the record here, not L1 operations
(the deferred `BuildDiscreteInterpolator` / `BuildProlongationAtLevel` siblings,
named in the `fe_space` deferred-sibling list).
[new]:## Record definition: `FiniteElementSpaceHierarchy`

The output record `FiniteElementSpaceHierarchy` now has a cross-cutting
definition home at [`concepts/FiniteElementSpaceHierarchy`](../concepts/FiniteElementSpaceHierarchy.md)
— its field schema (`fespaces` construction-time level stack; `P` run-time-lazy
prolongations), per-field construction-vs-run-time strata, the read surface, and
the L0 backing `class FiniteElementSpaceHierarchy` (`palace/fem/fespace.hpp:200-286`)
are defined there. It was promoted to a standalone page (c121) once the
≥2-consumer bar was met: this chapter is the **producer** (the `AddLevel`-fold),
and the [geometric-multigrid preconditioner](../feature/geometric-multigrid-preconditioner.L4.md)
is the **consumer** (its V-cycle composes the record's `GetProlongationOperators()`
level-stack by name).

Producer-local note: the fold's output value IS this record — the coarse-seed
`make_unique<FiniteElementSpace>` populates `fespaces[0]`, each `AddLevel`
`push_back`es one more level (`fespace.hpp:217-221`, strict append + a `nullptr`
prolongation slot), and the prolongation operators `P[l]` are left `nullptr` by the
fold (lazily built later during the multigrid solve, NOT here). The
prolongation/discrete-interpolator machinery is read-as-given (sibling-pull-gated
per the [`fe_space`](./fe_space.md) deferred-sibling list); see the concepts page
for the field-level detail.
[new]:
```

```edit:book/src/L1/fe_space_hierarchy.md
[old]:- result — `FiniteElementSpaceHierarchy` — the coarse-to-fine level stack; see
  *Record definition*. `GetNumLevels()` is the produced level count;
  `GetFinestFESpace()` is the finest [`fe_space`](./fe_space.md)
  (`FiniteElementSpace[N]`, `N` its true-dof count).
[new]:- result — `FiniteElementSpaceHierarchy` — the coarse-to-fine level stack; the
  field schema + strata are defined at
  [`concepts/FiniteElementSpaceHierarchy`](../concepts/FiniteElementSpaceHierarchy.md).
  `GetNumLevels()` is the produced level count; `GetFinestFESpace()` is the finest
  [`fe_space`](./fe_space.md) (`FiniteElementSpace[N]`, `N` its true-dof count).
```

### 3. Wire the new concepts page into SUMMARY.md (alpha position)

Alphabetically (case-insensitive), `finite…` sorts after `finest-level-unwrap` and before
`first-iteration-unrolling` (`fine` < `fini` < `firs`).

```edit:book/src/SUMMARY.md
[old]:  - [finest-level-unwrap](./concepts/finest-level-unwrap.md)
  - [first-iteration-unrolling](./concepts/first-iteration-unrolling.md)
[new]:  - [finest-level-unwrap](./concepts/finest-level-unwrap.md)
  - [FiniteElementSpaceHierarchy — record definition](./concepts/FiniteElementSpaceHierarchy.md)
  - [first-iteration-unrolling](./concepts/first-iteration-unrolling.md)
```

## Supporting evidence

### Part 1 — RE9 edge VERIFY (no edit; D1 authored it)

- D1's `book/src/feature/geometric-multigrid-preconditioner.L4.md` frontmatter `depends-on`
  block carries `- target: L1/fe_space_hierarchy / kind: composes` annotated
  `# GetProlongationOperators() — the level-stack P[l] prolongation GMG restricts/prolongs over
  (GROUNDS RE9)`. The `.L1.md` frontmatter carries the same edge. **This IS the RE9-grounding
  edge.** I do not duplicate it.
- Faithfulness confirmed on disk (palace-codemap `read_range`):
  - `palace/linalg/ksp.cpp:207-234` — `GeometricMultigridSolver` is constructed with
    `fespaces.GetProlongationOperators()` (`:221`, `:228`) and, when `linear.mg_smooth_aux`,
    `fespaces.GetDiscreteInterpolators(*aux_fespaces)` (`:219`). The GMG genuinely consumes the
    hierarchy record's prolongation/interpolator stack by name.
  - `palace/fem/fespace.hpp:257-267` — `GetProlongationOperators()` returns the
    `GetNumLevels()-1`-length `P[l]` list (the per-inter-level transfer operators).
- Well-foundedness: `rank(GMG)=rough-in (2) ≤ rank(fe_space_hierarchy)=firm (3)` — the
  `depends-on` edge satisfies `rank(u) ≤ rank(v)`.
- Reachability/RE9: the edge makes `L1/fe_space_hierarchy` (listed detritus in the c120
  linter baseline) reachable from the GC-root GMG column. **RE9 grounded.** (Authoritative
  confirmation is the c122 linter re-run on the landed tree, per the plan's RE-re-check note.)

### Part 2 — ≥2-consumer judgment + record citations (self-verified, codemap `read_range`)

- `palace/fem/fespace.hpp:200-286` — `class FiniteElementSpaceHierarchy`: class line `:200`;
  `std::vector<std::unique_ptr<FiniteElementSpace>> fespaces` `:203`; `mutable
  std::vector<std::unique_ptr<Operator>> P` `:204`; `BuildProlongationAtLevel` decl `:206`;
  single-arg seed ctor delegating to `AddLevel` `:210-213`; `AddLevel` = `push_back` + `nullptr`
  slot `:217-221`; `GetNumLevels` `:215`; `GetFESpaceAtLevel` `:223-234`; `GetFinestFESpace`
  `:236-247`; `GetProlongationAtLevel` `:249-255` (lazy `P[l] ? *P[l] : BuildProlongationAtLevel(l)`);
  `GetProlongationOperators` `:257-267`; `GetDiscreteInterpolatorAtLevel`/`GetDiscreteInterpolators`
  `:269-285`; class close `};` `:286`. **Range END `:286` confirmed by direct on-disk read** (the
  `};` is the class-closing brace; `:286` is exact, not ±1 — the close-brace off-by-one check).
- The in-chapter §Record-definition I am trimming (`L1/fe_space_hierarchy.md:120-141`) cites the
  same `fespace.hpp:200-286` range and the same field schema; my concepts page is a faithful
  promotion of it (no new claims), with the stratum prose expanded per the `mesh.md` /
  `sim-state.md` record-page template.

### Consumer-count judgment (the ≥2 bar)

| consumer | role | names the record |
|---|---|---|
| `L1/fe_space_hierarchy` | producer | `fe_space_hierarchy :: ... -> FiniteElementSpaceHierarchy` (`:35,87`) |
| GMG preconditioner column (D1, rough-in, landing c121) | consumer | `GetProlongationOperators()` / `GetDiscreteInterpolators()` / V-cycle `P[l]` (`ksp.cpp:221,228`) |

Two referencing chapters → bar met. The bar is "≥2 consumers" (NOT "≥2 firm consumers"); the
`mesh.md` precedent counts its producer `build_mesh` in the ≥2 and is promoted with the same
producer-+-consumers shape. The GMG column being rough-in does not block promotion (a record
page is a `reference` target, named-by-use). The watch `record-FiniteElementSpaceHierarchy-promote-watch`
(anchored at `fe_space_hierarchy.md:120-123`) has fired → promote.

### On-disk `## Status` lines surveyed (NOT index cells)

- `L1/fe_space_hierarchy.md` `## Status`: **firm (firm-on-positive-structure)** (c117) — the
  producer; the record it produces is firm.
- The GMG column (D1) lands `rank: rough-in` (D1's report `## Status`: rough-in, held by the
  smoother leg's well-foundedness gate). This is the 2nd consumer.

## Open questions / caveats

- **[INTEGRATOR — D1↔D2 shared-edge coordination, Part 1.]** D1 and D2 are sequenced D1→D2 with
  the overlap noted as "D2 reads D1's column and appends the inbound `depends-on` edge." On
  inspection, **D1 already authored the `GMG → L1/fe_space_hierarchy` `depends-on (composes)`
  edge on both GMG levels** (it is part of the column's composition). So D2 does **NOT** add or
  duplicate that edge — duplicating it would double-register the edge. D2's contribution to
  Part 1 is a **VERIFY-only** (faithfulness + well-foundedness + RE9-grounding confirmed above).
  The integrator should apply D1's edge as-is (it is in D1's proposed-changes) and apply only
  D2's Part-2 promotion edits. No edit collision between D1 and D2 on `fe_space_hierarchy.md`:
  D1 does not edit `L1/fe_space_hierarchy.md` (it only adds an outbound edge in the *GMG*
  frontmatter); D2 edits `L1/fe_space_hierarchy.md` (the §Record-definition trim + the
  `reference` edge + the result-line back-link). Disjoint.
- **D1 forward-references `concepts/FiniteElementSpaceHierarchy` indirectly.** D1's column links
  to `L1/fe_space_hierarchy` (the producer), not to the new concepts page — that is correct (the
  column consumes the *operator*; the operator's output record's definition home is the concepts
  page). No D1 edit is needed to point at the new page; the concepts page back-links to the GMG
  column (in its `reference` edges + "Signatures that name this record") so the wiring is
  navigable from both directions.
- **`record-MultigridConfig-needs-definition-home` (D1's flag, NOT my scope).** D1 flagged
  `MultigridConfig` as a single-consumer record (its column) needing an in-chapter
  §Record-definition or a future concepts page if a 2nd consumer surfaces. That is a separate
  record from `FiniteElementSpaceHierarchy`; not actioned here. Left to the record-definition
  dispatcher / a future cycle (it is currently single-consumer, below the standalone-page bar).
- **c122 RE9 confirmation.** The authoritative RE9-discharge confirmation is the c122 linter
  re-run with `--show-inbound` on `L1/fe_space_hierarchy` (it should show the inbound
  `depends-on` from the GMG column, and the node should drop off the detritus list). This
  dispatch grounds RE9 by VERIFYING D1's edge + ensuring the record's definition home is live;
  the measurement is c122's per the plan's RE-re-check standing duty.
- **SUMMARY alpha-position assumption.** I placed the new concepts page between
  `finest-level-unwrap` and `first-iteration-unrolling`. The Concepts Part is case-insensitive
  alpha-sorted on disk; `FiniteElementSpaceHierarchy` (mixed-case slug, matching the `Mesh —
  record definition` / `DofSet — record definition` capitalized-record convention) sorts on its
  lowercased form `finite…`. If the integrator finds a different sort key in use, the row is a
  cheap re-position (single line).
