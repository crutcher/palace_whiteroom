# Methodology — the graded-stack scheme (node-status + typed edges)

> **⟢ NORMATIVE authoring convention — but NON-AUTHORITATIVE relative to
> `METHODOLOGY-GRADED-STACK.md`.**
>
> This page is the **machine-readable scheme** the two graded-stack linters
> (`tools/` rank-check + reachability-GC) and all producers consume: it fixes the
> `rank:` token, the typed-edge block, the feature-root marker, and the migration
> mapping that makes the artifact-wide typing pass mechanical. It is the *authoring
> contract*; the **full spec** is `METHODOLOGY-GRADED-STACK.md` (2026-06-04 user
> directive). **If this page contradicts that doc, that doc wins and this page is
> corrected.** Same convention as `goal-flow.md`.
>
> This page **documents the construction**; it is not a node in the subject DAG
> (`METHODOLOGY-GRADED-STACK.md` §2d), so it carries **no `rank:`/`edges:` frontmatter
> itself**. The reader-facing exposition of *why* (the two axes, worked examples) lives
> in `resolution-ladder.md`; this page is the *how-to-write-it*.

The artifact is **one typed dependency graph** with two orthogonal, mechanically-checkable
axes (`METHODOLOGY-GRADED-STACK.md` §1–§3):

- **Axis 1 — resolution + well-foundedness.** Every node carries a resolution `rank`; for
  every blocking edge `u → v`, `rank(u) ≤ rank(v)` (a node is at most as resolved as its
  least-resolved dependency).
- **Axis 2 — reachability / liveness.** The feature-surface columns are the **root set**;
  a node reachable from a root over blocking edges is *live*, an unreachable node is
  *garbage*.

Both axes run over the same edge set. This page defines the four tokens that encode it:
the **`rank:`** token (§1), the **`edges:`** block (§2), the **`seed`** root marker (§3),
and the **migration mapping** + **node-status for un-fronted files** (§4–§5).

## 1. The `rank:` token and the maturity-vocabulary → ladder mapping

A node's resolution rank is a total order (`METHODOLOGY-GRADED-STACK.md` §1a):

```
roadmap_goal = 0   <   stub = 1   <   rough-in = 2   <   firm = 3
```

The on-disk maturity vocabulary (the values that appear today in `firmness:` / `status:`
frontmatter and in prose `## Status` lines) maps onto the ladder as follows. **The `rank:`
token is what the linters read; the prose maturity word is the human-facing label.** Every
producer writes the prose word it already writes AND the `rank:` it maps to.

| on-disk maturity value | `rank:` token | numeric rank | notes |
|---|---|---|---|
| `firm` | `firm` | 3 | a `firm` node's every `depends-on` dep must be `firm` (§2). |
| `partly-constructive` | `partly-constructive` | **2.5** | sub-rank pinned just under firm; `firm` **cannot** rest on it. First-class transient gate (unchanged semantics). |
| `rough-in (test-coverage-bounded)` | `rough-in-test-coverage-bounded` | **2.5** | sub-rank just under firm; `firm` cannot rest on it. First-class transient gate (unchanged semantics). |
| `rough-in` | `rough-in` | 2 | structural signature anchored; laws stated-but-unconfirmed. |
| `stub` | `stub` | 1 | claim-free placeholder; ≥2-converging-reference bar; deps must be ≥ `stub`. |
| `roadmap_goal` | `roadmap_goal` | 0 | the new thinnest tier (`METHODOLOGY-GRADED-STACK.md` §1d/1e); claim-free intent; deps **unconstrained**. |
| `obstruction` / `partial-obstruction` | `obstruction` *(+ `partial-obstruction` sub-kind)* | **separate kind** (rankable) | NOT a low rank — a *firm* obstruction is a well-founded negative result. See below. |
| `seed` | — *(NOT a ladder value)* | — | the feature-root marker (§3), a parallel axis; the column ALSO carries a separate composition-maturity rank. |

**Sub-rank rule (the 2.5 tier).** `partly-constructive` and `rough-in (test-coverage-bounded)`
are pinned at rank **2.5**: strictly above `rough-in` (2) and strictly below `firm` (3). The
load-bearing consequence the rank linter enforces: **`firm` (3) cannot rest on a 2.5 node** —
a firm entry depending on a `partly-constructive` or `rough-in (test-coverage-bounded)`
dependency is a rank violation, exactly as a firm entry depending on a `rough-in` dependency
is. (This is the mechanization of "a reduction is as firm as its least-firm folded
primitive.") A 2.5 node may itself rest on another 2.5 node or on `firm`.

**Obstruction is a separate axis, not a low rank** (`METHODOLOGY-GRADED-STACK.md` §1f). The
total order is over *constructive* resolution. An `obstruction` / `partial-obstruction` is a
*kind* (a documented negative / un-liftable-loop result) that is itself rankable for its
constructive content — a `firm` obstruction is a well-founded, exhaustively-cited negative
result and is a fully valid `depends-on` target on a live path (a driver→assemble→solver path
that terminates at "and here Palace forwards opaquely" is reachable, §3). The scheme records
the kind alongside the rank:

```yaml
rank: obstruction          # the kind
obstruction_kind: opaque-library-ownership   # or: enum-only-stub  (CLAUDE.md §obstruction sub-kinds)
obstruction_resolution: firm   # the constructive-resolution rank of the negative result itself
```

A `partial-obstruction` (the L3 "body lifts, loop does not" case) carries
`rank: partial-obstruction` with the same `obstruction_resolution` sub-field for the lifted
body. The rank linter treats an obstruction node as satisfying any *downstream* consumer's
requirement when its `obstruction_resolution` is `firm` (a firm negative result is a firm
support); the well-foundedness check on an obstruction node's OWN deps uses
`obstruction_resolution` as its rank.

## 2. The typed-edge block — `edges:`

Edges are declared in a single machine-readable **`edges:`** frontmatter block (this
supersedes the ad-hoc `depends_on:` list now in 10 files — §4). Every edge is typed by the
**minimal binary** (`METHODOLOGY-GRADED-STACK.md` §3): the linters consume only this bit.

```yaml
edges:
  depends-on:
    - L1/dot                       # blocking: constrains rank (§1) AND carries liveness (§3)
    - L1/apply_linop
  reference:
    - feature/eigenmode.L4         # navigational see-also: constrains NOTHING, carries NO liveness
    - concepts/solver-as-operator
```

- **`depends-on`** — **blocking.** Constrains rank (well-foundedness, §1) **and** carries
  liveness (reachability, §3). This is the bit both linters consume. `rank(u) ≤ rank(v)` is
  asserted for every `depends-on` edge `u → v`.
- **`reference`** — **navigational "see-also."** Constrains nothing; carries **no** liveness
  (a mere mention must not keep dead vocabulary alive). Used for sibling cross-links,
  concept-narrative pointers, and — load-bearing — **every edge whose target is a feature
  root** (§3).

> **"Constrains rank" ≡ "carries liveness" ≡ "is a `depends-on` edge."** The default is NOT
> `depends-on` — **classify each edge deliberately.** An edge to a feature-surface column
> (a root) is `reference`, never `depends-on` — this is precisely where the feature
> OWN-COMPOSITION promotion rule falls out (§3): a column's edges to *vocabulary* are
> blocking, its edges to *sibling roots* are references, so sibling roots never gate each
> other's rank.

**Optional `kind:` annotation — DOCUMENTATION ONLY.** A `depends-on` edge may carry a
free-text `kind` (`folds` / `lowers-to` / `uses-record` / `cites-evidence` / …). **The
linters ignore it.** It is human documentation; promote a `kind` to a real typed distinction
later only if an analysis ever needs it. Two equivalent surface forms are permitted (a
producer may write either):

```yaml
edges:
  depends-on:
    - target: L2/linear_combination
      kind: folds                  # documentation; linters read only `target` + the depends-on bucket
    - L1/apply_linop               # bare string form, kind omitted
```

The bare-string form and the `{target:, kind:}` mapping form are interchangeable; a linter
treats a bare string as `{target: <string>}` with no kind. **Targets are repo-relative slugs
without the `book/src/` prefix or the `.md` suffix** (`L1/dot`, `feature/eigenmode.L4`,
`concepts/config-record`, `L1-L0/ksp-solve-mutation-rotation`) — the linter resolves a slug
to `book/src/<slug>.md`.

## 3. The feature-root marker — `seed`

The FEATURE-SURFACE SPINE columns (the 5 drivers + boundary-mode, the lifecycle spine-ROOT,
the 5 output products) are the **root set** for the reachability GC
(`METHODOLOGY-GRADED-STACK.md` §2a). Root membership is marked by the **`seed`** token —
**a parallel axis, NOT a ladder rung.** A feature column therefore carries TWO independent
properties:

```yaml
kind: feature-surface
feature_root: seed       # root-set membership: permanent, categorical (NOT a rank)
rank: firm               # the column's OWN composition-maturity: a separate property that climbs
```

The historical `status: seed` on feature columns conflated these two. Under the scheme they
split: `feature_root: seed` is the *permanent* root marker (the `seed→firm` flips of cycles
085/091 were maturity events on `rank:`, on nodes whose root-role never changed); `rank:`
carries the column's composition-maturity, judged by the OWN-COMPOSITION rule (a column's
`depends-on` edges go to its *vocabulary* constituents; its edges to *sibling columns* are
`reference`, so siblings do not gate its rank — §2). A feature column whose own constituents
are all firm has `rank: firm` even while a sibling column it cross-links stays lower.

The reachability GC marks from every `feature_root: seed` node over `depends-on` edges;
unmarked nodes are garbage (the detritus / orphaned-intent sweep is one mark-sweep from this
root set, `METHODOLOGY-GRADED-STACK.md` §2b). A `roadmap_goal` is justified only if its
`pulled-by` provenance chains, over `depends-on` edges, to a root.

**The detritus set has two measurement subsets — distinguish them when projecting a
grounding pass's delta.** The linter reports garbage in two buckets:
`detritus_no_typed_edges_pre_p1_artifact` (**edge-untyped detritus** — dead-ends because their
`edges:` are not yet typed, i.e. frontmatter-less or legacy-only) and
`detritus_with_typed_edges_stronger_signal` (the **STRONGER subset** — nodes that DECLARE typed
`depends-on` deps yet are still unreachable: a real, examined off-spine node, not a typing gap).
Flipping an *edge-untyped* node reachable (e.g. grounding an op→theme edge whose theme carries no
frontmatter) drops the **edge-untyped** count, NOT STRONGER; only a *typed-but-unreachable* node
moving to reachable clears a STRONGER member. A grounding-pass projection that says "STRONGER −N"
for an edge-untyped flip conflates the two — the faithful result holds STRONGER and drops
edge-untyped. (c114 D2 surfaced this: grounding three frontmatter-less L1>L0 themes moved
reachable/edge-untyped but held STRONGER at 23.)

## 4. The migration mapping

*Where edges live going forward.*

Dependency information lives today in **three incompatible representations**. The scheme
unifies them into the single `edges:` frontmatter block (§2). The recommendation and the
per-representation migration:

**Recommendation: a single per-chapter `edges:` frontmatter block is the going-forward home
for edge types** — superseding the ad-hoc `depends_on:` list. Rationale: the prose
`## Dependencies` sections and the `L_n/index.md` dep-map *tables* are free text and are
**not machine-parseable** (an entry's "Dependencies" cell mixes slugs, prose qualifiers like
"(leaf; subsumed by `axpby` via β=0)", and parenthetical non-dependencies like "sibling to
`apply_linop`, NOT a dependency"); re-deriving typed edges from that prose for 357 files is
infeasible and error-prone. Frontmatter is the only representation a linter can consume
deterministically. The `edges:` block also subsumes the existing `lowers_to:` / `lifts_from:`
frontmatter (54 files) as typed edges (see (a)).

| current representation | count | migration to `edges:` |
|---|---|---|
| **(a)** `depends_on:` frontmatter (L1 entries) | 10 files | Each `depends_on:` slug becomes an `edges: depends-on:` entry. The co-resident `lowers_to:` / `lifts_from:` lists become `edges: depends-on:` entries with documentation `kind: lowers-to` / `kind: lifts-from` (the lowering edge IS a `depends-on` on both endpoints — §5). Mechanical, 1:1. |
| **(b)** prose `## Dependencies` + `L_n/index.md` dep-map tables | the bulk (NOT parseable) | NOT auto-migrated. The **authoritative** edge set moves to per-chapter `edges:` frontmatter; the prose dep-map table becomes a *derived human-readable view* (it may lag, like the index status cells). P1 reads each chapter's prose Dependencies cell, classifies each listed slug `depends-on` vs `reference` deliberately (the typing pass IS the audit), and writes the `edges:` block. The index table is regenerated/back-checked against the frontmatter, not parsed as the source. |
| **(c)** feature `composes:` / `l0_ground_truth:` frontmatter | 24 files (the 12 columns × levels with frontmatter) | `composes:` entries become `edges:` — a `composes:` target that is a *vocabulary op* → `depends-on`; a `composes:` target that is a *sibling feature column* → `reference` (the OWN-COMPOSITION rule, §3). `l0_ground_truth:` entries become `edges: depends-on:` with `kind: cites-evidence` (the L0 source the column rests on). The free-text maturity qualifiers in the `composes:` strings (e.g. "(firm — …)") are dropped from the edge (the dep's rank is read from the dep's own frontmatter, never restated on the edge — the index-cell-drift lesson). |

### Why per-chapter `edges:` frontmatter everywhere

The going-forward home is **option (a): per-chapter `edges:` frontmatter everywhere** — every
file that is a real DAG node gets a hand-classified `edges:` block. It is chosen over two
alternatives that materially set the typing cost:

- **(a) per-chapter `edges:` frontmatter everywhere** — *heavy but clean.* Every real DAG node
  (~250+ of the ~357 files) gets a hand-classified `edges:` block. Highest up-front cost;
  deterministic, complete, and the only option that covers themes + concepts (which appear in
  NO index table).
- **(b) parse the index dep-map tables** — *lighter but lossy.* The tables are inconsistent
  free text, and **themes, concepts, and feature columns are not rows in any layer dep-map
  table** — so this option structurally misses a large fraction of the DAG and cannot type the
  lowering edges at all.
- **(c) hybrid** — frontmatter for leaf entries + table-parse for the index aggregates. Splits
  the difference but creates two edge-of-truth surfaces that drift (the failure mode the
  index-status-cell drift already demonstrates).

Option (a) is the only one that (i) is deterministically parseable, (ii) covers
themes/concepts/feature-columns that no table holds, and (iii) avoids a second drifting
source-of-truth. The **(a)-incremental** rollout types the high-fan-out frontier + the feature
roots + their transitive `depends-on` closure first (the nodes the reachability GC and the
rank-validation actually need), letting the long tail of leaf entries acquire `edges:` lazily
as they are next touched — the linters treat un-typed frontmatter as a WARNING, not a hard
error, so an incrementally-typed artifact is runnable throughout.

## 5. Node-status for the un-fronted files

253 files carry no maturity frontmatter today: index pages, lowering themes, all L2/L3/L0
entries, all concept pages. How each acquires a `rank:`:

- **Operator entries with a prose `## Status` line but no frontmatter `rank:`** (the L2/L3/L0
  entries) — the **`## Status` line is authoritative** (the existing project rule: survey
  firmness from the on-disk `## Status`, never the index cell). P1 reads the prose `## Status`
  word, maps it via the §1 table, and writes the `rank:` frontmatter to match. Where a chapter
  has neither frontmatter nor a `## Status` line and lacks the firm apparatus, it is NOT
  labelled firm — its rank is prose-derived conservatively and the on-disk gap is flagged as an
  OQ (an upstream landing gap), not forced.

- **Lowering themes (`L*-L*/`)** — **resolved cleanly by the graded-stack §8 lowering-verifier
  rule.** A lowering theme is **at most as resolved as its endpoints**: the lowering edge is a
  `depends-on` on BOTH the L_{n+1} source entry and the L_n target entry. So a theme's `rank:`
  is `min(rank(L_{n+1} endpoint), rank(L_n endpoint))`, and the theme's `edges: depends-on:`
  lists both endpoints. The theme need not carry a free-standing rank judgment — its rank is
  derived from (and rank-checked against) its two endpoints. P1 writes the theme's `edges:`
  block (the two endpoints + any concept references) and a `rank:` consistent with the §1b
  invariant; the rank linter then validates `rank(theme) ≤ min(endpoints)` for free.
  - **Reachability ≠ well-foundedness for a lowering theme (clarification, batch-34).** The
    rule above makes a theme *well-founded* (rank ≤ min endpoints), but does **not** by itself
    make it *reachable*. A lowering theme is reachable **iff its UPPER-endpoint operator carries
    a `lowers-to` `depends-on` edge AT the theme** (so a reachable node `depends-on` it). The
    established convention is asymmetric: an **L1 op**'s `lowers_to:` points operator → its
    **L1-L0 theme** (so typing the L1 op rescues its theme automatically), but an **L2/L3 op**'s
    `lowers-to` points operator → the next **operator**, never at the theme — so the L2-L1 theme
    is only ever a `reference` target and stays off the `depends-on` spine. The bounded fix per
    affected theme is one edge: add `L2/<op> lowers-to L2-L1/<op>-theme` to the upper-endpoint op
    that already carries scheme frontmatter (mirroring the cycle-108 `L2/divfree_projector` edit).

- **Index pages + group-intro pages + the dependency-map page → `kind: navigational-container`
  (RATIFIED batch-33 meta-phase, post-cycle-105).** An `L_n/index.md`, a `*-intro` group page,
  `feature/index.md` + the three feature group pages, and `concepts/dependency-map.md` are all
  **navigational containers, NOT DAG nodes.** A container carries:
  - **NO `rank:`** — it makes no resolution claim and is not in the total order;
  - **`edges: reference:` ONLY** (its links point at the chapters it indexes; a `reference`
    edge constrains no rank and carries no liveness, so an index cannot keep dead vocabulary
    alive — exactly the property we need, since a container must not mark its members live);
  - **`kind: navigational-container`** — the explicit self-identification both linters key off
    (the reachability GC's `is_likely_outside_dag` treats any `kind: navigational-container`
    page as expected-unreachable, so it never reads as detritus). A free-text parenthetical
    sub-kind is permitted and ignored by the linter (`navigational-container (layer index)`,
    `… (group intro)`, `… (feature Part index)`, `… (concept dependency-map; derived view)`);
    the linter matches the **leading token** before the ` (`.

  This is the fully scheme-aligned reading of §4 ("an `L_n/index.md` is a navigational
  overview, not a DAG leaf node carrying claims; its dep-map table is a derived view") + §5.
  It closes the former carve-out OQ `graded-stack-index-and-concept-node-status` and the linter
  gaps `dependency-map-not-recognized-outside-dag-by-linter` /
  `linter-outside-dag-misses-group-intro-container-pages` (the batch-33 linter fix honors the
  `kind:` tag for exactly this set).

- **Concept pages (`concepts/`)** — two sub-cases. A concept page that is a *meta page about
  the construction* (narrative pointer to an L_n operator, e.g. `concepts/dot.md`,
  `concepts/solver-as-operator.md`) sits **outside the subject DAG** (`METHODOLOGY-GRADED-STACK.md`
  §2d). A concept page that is a **record-definition** page (e.g. `concepts/config-record.md`)
  defines a *data shape* that signatures rest on — it **is** a DAG node and its rank is the
  resolution of that shape (typically `firm` once its L0 backing struct is cited). The
  record-definition pages are the `record` Kind; the boundary needs the P1 author's judgment.

  **Non-node concept-page encoding — UNIFIED (RATIFIED batch-33 meta-phase, post-cycle-105):**
  a non-node (narrative-pointer / methodology / literature-background) concept page carries
  **NO `rank:`** and an **`edges: reference:`-only block** (its see-also links to the L_n home
  + sibling concepts, all `reference` since a non-node asserts no blocking dependency). This
  resolves the D1/D3/D5 (`reference`-only block) vs D2 (strict zero-frontmatter) divergence in
  favor of the **`reference`-only block** — the navigational see-also graph is then
  machine-readable for the reachability-GC author and uniform with the navigational-container
  convention above, at zero linter-invariance cost (a non-node contributes only `reference`
  edges → no rank/liveness claim either way). It closes OQs
  `concept-non-node-frontmatter-encoding-reference-only-vs-empty` /
  `graded-stack-concept-node-status-convention` / `graded-stack-concept-nonnode-edges-block-d1d3-vs-d2`.
  The c103 D2 cluster-B pages that were written strict-zero acquire a `reference`-only block as
  they are next touched (lazy convergence; the linter is invariant meanwhile). The two D2
  borderline calls reconcile: `counter-update` (sole-definition site of an L2 primitive a real
  node `depends-on`) **flips to a record/definition NODE** under the "sole-definition-site
  primitive is a node" reading; `chebyshev-iteration` (pre-redirect literature-background page
  with no authoritative L_n forward) stays a **non-node**.

## 6. Authoring checklist (the contract, condensed)

When you author or touch a DAG-node chapter:

1. Write the prose maturity word as today (`## Status` line / `firmness:`), AND the matching
   **`rank:`** frontmatter token (§1 table). For an obstruction, also write `obstruction_kind`
   + `obstruction_resolution`.
2. Write the **`edges:`** block (§2): every dependency classified `depends-on` (blocking) or
   `reference` (free); an edge to a feature root is `reference`; an `l0_ground_truth` /
   evidence citation is a `depends-on` with `kind: cites-evidence`; a lowering edge is a
   `depends-on` on both endpoints.
3. If the chapter is a feature column, carry **`feature_root: seed`** (permanent) separately
   from `rank:` (§3).
4. A **methodology / process** page carries **no** `rank:`/`edges:` (§2d, like this page). A
   **narrative-concept / non-node concept page** carries no `rank:` but **does** carry an
   `edges: reference:`-only block (the unified non-node encoding, §5). A **navigational
   container** (index / group-intro / dependency-map) carries no `rank:`, an `edges:
   reference:`-only block, AND `kind: navigational-container` (§5).
5. The rank invariant is a HARD gate for new work (`METHODOLOGY-GRADED-STACK.md` §5 step 4):
   do not promote a node above the rank of its least-resolved `depends-on` dependency.

---

*This page is the authoring contract; `resolution-ladder.md` is the reader-facing exposition;
`METHODOLOGY-GRADED-STACK.md` is the authoritative spec. The two linters under `tools/`
(rank-check, reachability-GC) consume the `rank:` token, the `edges:` block, and the
`feature_root: seed` marker defined here.*
