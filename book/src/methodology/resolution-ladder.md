# Methodology — The graded resolution ladder & feature-root reachability

> **⟢ NON-AUTHORITATIVE — reader-facing mirror; a review point, not a source.**
>
> This chapter is a **reader-facing exposition** of the project's two-axis
> artifact-health model. It is **not** a directive source. The authoritative
> specification is `METHODOLOGY-GRADED-STACK.md` (the 2026-06-04 user directive) at
> the repo root, distilled operationally in `CLAUDE.md` §Methodology invariants.
>
> **If this chapter contradicts `METHODOLOGY-GRADED-STACK.md`, that document wins and
> this chapter is corrected.** A contradiction surfacing here is a *drift signal*, not
> a decision to adjudicate. Read this chapter to orient; read the spec to act.
>
> The **authoring convention** the agents and the two linters consume — the
> machine-readable `rank:` token, the typed-edge frontmatter grammar, and the
> migration mapping from the prior representations — is the separate normative page
> [Graded-stack scheme](./graded-stack-scheme.md). *That* page is the authoring spec;
> *this* page is the conceptual exposition of why the scheme has the shape it does.

The artifact has **two orthogonal, mechanically-checkable axes** that together define
its *health*:

1. **Resolution + well-foundedness** — how *resolved* each entry is, and the invariant
   that an entry can be no more resolved than its supports.
2. **Reachability / liveness** — whether each entry is *justified* by being reachable
   from a feature the artifact exists to serve.

Both run over **one** shared dependency graph (described last). They are orthogonal: an
entry can be fully firm yet garbage (firmly built, but nothing live depends on it), or
reachable yet unfinished (justified, but not yet resolved).

## Axis 1 — resolution + well-foundedness

### The graded ladder

Constructive resolution is a **total order** with a numeric rank:

```text
roadmap_goal = 0   <   stub = 1   <   rough-in = 2   <   firm = 3
```

- **`roadmap_goal` (0)** — a claim-free *intent* chapter (see below). The thinnest tier.
- **`stub` (1)** — a claim-free placeholder for a *real but undissected* referent
  (≥2 converging references, or a rough-in row already standing for it): a one-or-two
  line sketch + an "Implied by" provenance list + a "Refinement pending" note.
- **`rough-in` (2)** — the structural signature is anchored at L0, but the algebraic
  laws are stated-but-unconfirmed (or a constructive sub-part is gated).
- **`firm` (3)** — surface and laws fully anchored on positive source; the apparatus
  (Signature + Algebraic-laws + variant-axis coverage + Evidence) is complete.

Two qualifiers are **sub-ranks pinned just under firm (≈ 2.5)**: `partly-constructive`
(structure firm, one constructive sub-part materialized from negative anchors) and
`rough-in (test-coverage-bounded)` (structure firm, laws gated on a missing test). A
`firm` entry **cannot** rest on a 2.5 dep.

`obstruction` / `partial-obstruction` are **not** low-resolution — they are a *separate
kind*. A *firm* obstruction is a well-founded negative result (a Palace boundary or stub
exhaustively cited). The total order is over *constructive* resolution; `obstruction` is
its own rankable kind running alongside.

### The well-foundedness invariant

For every **`depends-on`** edge `u → v` (read: *`u` is well-founded on `v`*):

> `rank(u) ≤ rank(v)` — equivalently, **`rank(u) ≤ min over depends-on deps(u) of rank(v)`**.
>
> **An entry is at most as resolved as its least-resolved dependency.**

Read forward, this is the **promotion rule**: an entry promotes to rank *k* only once
*all* its `depends-on` dependencies are ≥ *k*. Consequences:

- `firm (3)` ⇒ every dependency is `firm`.
- `rough-in (2)` ⇒ dependencies ≥ `rough-in`.
- `stub (1)` ⇒ dependencies ≥ `stub`.
- `roadmap_goal (0)` ⇒ dependencies unconstrained — **roadmap_goals may stack on
  roadmap_goals**, as well as stubs, rough-ins, and firms.

This invariant **subsumes** two rules the project previously enforced by hand: "a
reduction is as firm as its least-firm folded primitive" (the `firm`/rank-3 case) and
the feature-column OWN-COMPOSITION promotion rule (Axis 2 below).

It is **orthogonal to, and compatible with, "layers are defined high → low."** Those are
two duals:

- **Definition flows *down*** — a layer is written in its own (or a higher layer's)
  vocabulary, never defined by reducing to the layer beneath it.
- **Well-foundedness / maturity flows *up*** — you cannot be firm until your supports
  are. Promotion propagates **upward** through the dependency DAG; the **frontier** is
  the rank-discontinuity surface where the resolved region meets the unbuilt region.

### Worked example — rank propagating upward (the cycles 088–095 cascade, completed)

The `matrix-weighted-norm` cascade is exactly a wave of rank propagating upward under
the invariant. The relevant fragment of the DAG (`depends-on` edges, leaf at the
bottom):

```text
   feature columns: capacitance, inductance, electrostatic,   energy-fields
                    magnetostatic   (depends-on gram_reduce)   (depends-on
                          |                                      domain_energy_reduce)
                          v                                          v
                    gram_reduce (L4)                        domain_energy_reduce (L4)
                       |        |                                    |
            depends-on |        | depends-on             depends-on  |
                       v        v                                    v
       bilinear-form (L1)   matrix-weighted-norm (L1) <--------------+
       ── off-diagonal      ── diagonal leaf
          leaf (firmed c095)    (firmed c091)
```

Before cycle-091, `matrix-weighted-norm` sat at `rough-in (test-coverage-bounded)`: its
structure was anchored, but its norm-axiom laws (triangle, Cauchy–Schwarz, parallelogram)
were gated on a missing direct test of the SPD-weighted `√`-entry-point. By the invariant,
**nothing above it could exceed `rough-in`** — so `gram_reduce` and `domain_energy_reduce`
were each capped at `rough-in`, and every feature column depending on them was capped at
`seed`. The cap was a *consequence* of the leaf's rank, not an independent decision at each
node.

The cap lifted in **two waves**, one per leaf — and the whole chain is now `firm`, so this
example is a completed rank-propagation *discharge*, not a standing block.

**Wave 1 (cycle-091) — the diagonal leaf.** Cycles 088–089 discharged both law-sides of
`matrix-weighted-norm` (the structure-side laws are inner-product-space theorems whose SPD premise
holds provably-by-construction at the usage sites; the floating-point sub-claims inherit additively
from the firm constituents `dot` and `apply_linop` through a deterministic IEEE-754 outer `√`). The
batch-28 meta-phase judged the lone remaining test gate **redundant**, and cycle-091 flipped
`matrix-weighted-norm` to **`firm` (rank 3)**. Rank then propagated up its branch:
`domain_energy_reduce` — which folds *only* `matrix-weighted-norm`, so all of its `depends-on` deps
were now firm — promoted to `firm` in the same wave, and through it the `energy-fields` feature column
reached **`rank: firm`**.

**Wave 2 (cycle-095) — the off-diagonal leaf.** `gram_reduce` could *not* promote in wave 1, because
it folds a **second** leaf: the *off-diagonal* `bilinear-form` primitive, still `rough-in` after c091.
By the invariant, `gram_reduce` was correctly held at `rough-in` (and the four columns over it at
`seed`-resolution) until that last support firmed — a faithful illustration of the invariant *holding
a node back while one support is still soft*. Cycle-095 (the `bilinear-form-firm-flip-and-cascade-wave`)
discharged it: D1 flipped `bilinear-form` to **`firm`** on the firm-on-positive-structure escape,
clearing `gram_reduce`'s sole residual gate, so D3 flipped `gram_reduce` to **`firm`** (both folded
leaves — diagonal `matrix-weighted-norm` from c091, off-diagonal `bilinear-form` from c095 — now firm).
With its own reduce verb firm, the rank wave continued upward: the four output-product / driver columns
over `gram_reduce` — `capacitance`, `inductance`, `electrostatic`, `magnetostatic` — each reached
**`rank: firm`** at cycle-095 under the OWN-COMPOSITION rule (their cross-linked sibling columns are
`reference`s, not blockers; see Axis 2 below).

The two waves together close the cascade: every node in this DAG fragment is now `firm`. Note the
two-axis separation the columns demonstrate — each promoted to `rank: firm` *resolution* while its
`feature_root: seed` root-set membership is unchanged (the `seed` marker is the permanent Axis-2 root
role, never a ladder rung). The promotion frontier — the rank-discontinuity surface — has moved past
this fragment entirely; it now lives wherever the next still-soft support sits.

### The `roadmap_goal` chapter (rank 0)

A `roadmap_goal` is a **real book chapter** — not an off-book roadmap node — so links to
it resolve natively and it is the authoritative location that **accretes the entry's
working context in place** as the entry climbs the ladder. It carries:

- `status: roadmap_goal` frontmatter (rank 0) + an unmissable banner;
- the **intent** — the L_n operator / theme / concept it will become;
- **pulled-by** provenance — ≥1 real inbound *blocking* consumer that justifies it (this
  is also its reachability requirement, Axis 2);
- the **declared dependencies** it will be well-founded on (which may themselves be
  roadmap_goals) — the linter reads these;
- the **accreting working context** — speculative sketch, gathered citations, gap notes,
  prior cross-cutter / abstractor observations;
- **no claims** — anything asserted is explicitly flagged speculative.

A `roadmap_goal` chapter is the **in-discipline replacement for the retired
`annotated-and-retained` slice**: it gives *intent* a legal, claim-free, refactorable home
on the ladder, governed by the invariant, so it climbs instead of freezing.

### `stub` vs `roadmap_goal`

Both are claim-free chapters, so the line is **not** "file vs no-file." Two things separate
them, both falling out of the invariant:

- **What the referent is.** A `stub` stands for a referent that is *real but undissected*.
  A `roadmap_goal` stands for an *intended* entry whose referent may itself be speculative.
- **What it may rest on.** `stub` ⇒ deps ≥ stub (grounded in at-least-placeholders).
  `roadmap_goal` ⇒ deps unconstrained (intent may rest on intent).

The `roadmap_goal → stub` promotion **is** the invariant firing: "all my supports are now
at least materialized, and my referent is confirmed real." Adjacent rungs, intentionally
similar in content; the load-bearing difference is what is allowed to rest on them, and
therefore what downstream claims can transitively rest on them.

## Axis 2 — reachability / liveness

### The feature surfaces are the root set

Think of a **garbage collector**. The FEATURE-SURFACE SPINE columns — the five simulation
drivers, the lifecycle spine-ROOT, the output products, and wave-port / boundary-mode — are
the **roots**: the entry points motivated users and downstream applications come to the
artifact *for*. **Reachability from the roots over `depends-on` edges defines liveness.** A
node on no root-to-leaf path is **garbage** — unjustified, *however firm it is*.

The `seed` marker is the **root-set membership marker** — it does **not** collapse into the
resolution ladder. A root's own composition-maturity is a *separate* property it carries
(the `seed → firm` flips of cycles 085 / 091 were maturity events on nodes whose root-role
never changed); its root-role is permanent and categorical.

### Reachability is justification

A vocabulary node exists *because* some feature surface transitively depends on it. This
**principled-izes** two things the project previously did by eye:

- **The detritus / orphan hunt is a mark-sweep from the root set.** "Is this read or
  referenced by anything live?" ≡ "is this reachable from a root?" Orphaned artifacts
  (kickoff-dead scaffolding, dead `priorities.md` active-heads) are precisely the
  *unreachable* nodes. The canonical worked instance was the **frozen Phase-1 slice corpus**
  — a detritus mass unreachable from any feature root, fully collected across cycles
  097/098/099 (the corpus went 9 → 0; `book/src/spec/` deleted), which is exactly the
  mark-sweep this axis formalizes.
- **The `roadmap_goal` proliferation guard *is* the reachability requirement.** A
  roadmap_goal is justified only if its pull-chain terminates at a feature root. No path to
  a root ⇒ speculation-noise ⇒ collected.

So **orphaned-intent GC and detritus GC are the same sweep**, run uniformly over built and
intended nodes.

Two refinements the typed-edge rollout (batch-33) made concrete:

- **Not every page is a DAG node.** Navigational containers (layer/group/feature index pages,
  group-intro pages, the concept dependency-map) carry `kind: navigational-container`, only
  `reference` edges, and no rank — they are *expected-unreachable*, never garbage. Likewise a
  narrative-concept page (a pointer to an L_n operator, a literature-background note) is a
  non-node: `reference`-only, no rank. Only **record-definition** concept pages and the
  operator/theme/feature chapters are DAG nodes. (The authoring contract is
  `graded-stack-scheme.md` §5/§6.)
- **A record consumed only inside an operator reaches the roots *through* that operator.** An
  internal record shape (a solver's `Krylov` / `SimState` / step-output carriers) is named in
  no feature-column signature; its live path is `column →(composes) op →(uses-record) record`,
  so the `uses-record` blocking edge belongs on the **op chapter**, not the column. Until that
  edge is typed, the record reads as (correctly) unreachable — a tracked baseline-exception, not
  a false alarm. This is the kind of edge the reachability GC can only honor once the linter
  actually traverses the edge form the producers write; making the GC *read* the typed edges and
  *typing* them are the same project (the batch-33 block-mapping-parser fix closed that gap, and
  reachability over the live tree jumped from the bare root set to its true transitive closure).

### The OWN-COMPOSITION rule falls out of the root marker

A feature column's edges to *vocabulary* are blocking `depends-on` edges (they constrain
its maturity); its edges to *sibling roots* are non-blocking `reference` edges (roots are
independently live and must not gate each other's rank). So the feature-column
OWN-COMPOSITION promotion rule — *a column promotes on its own firm constituents; the
sibling columns it cross-links are references, not blockers* — is **derived from "is the
target a root?"**, not a special edge type. (This is what broke the earlier
`eigenmode`↔`eigenfrequency-qfactor` mutual-blocking deadlock: each named the other as a
blocking constituent, when in fact the cross-link is a `reference` to a sibling root.)

### Where the graph stops

The root set is the feature surfaces **only**. Methodology / process pages (this chapter,
`graded-stack-scheme.md`, `goal-flow.md`, `book/src/design/`, and `concepts/` *meta* pages
*about* the construction) sit **outside** the subject DAG — they document the construction,
they are not nodes in it. (That is why this page carries no rank or edge frontmatter.)
Negative-result / obstruction nodes, by contrast, **are** on live paths — a
driver→assemble→solver path that hits "and here Palace forwards opaquely" runs *through* an
obstruction node, which is precisely why such negative results are load-bearing and must
live at reachable homes rather than be dropped.

Fan-out is reachability weight: the project's fan-out impact model
(`|concepts| × |downstream-reuse| × 1/cost`) approximates the count of root-to-leaf paths
through a node, so "dispatch highest-fan-out first" reads as "promote the most-reachable
frontier nodes first."

## The shared substrate — one typed dependency graph

Both axes run over **one** dependency graph whose edges are **typed**:

- **`depends-on`** — blocking. Carries **both** well-foundedness (constrains rank, Axis 1)
  **and** liveness (carries reachability, Axis 2). This is the bit both linters consume.
- **`reference`** — navigational "see-also". Constrains nothing and does **not** carry
  liveness (a mere mention must not keep dead vocabulary alive). **An edge to a *root* is a
  `reference`** — which is exactly where the OWN-COMPOSITION subtlety comes from.
- An optional **`kind:`** annotation on a `depends-on` edge (`folds` / `lowers-to` /
  `uses-record` / `cites-evidence` / …) is **documentation only; the linters ignore it.**

"Constrains rank" ≡ "carries liveness" ≡ "is a `depends-on` edge." The minimal binary
suffices because the analyses consume only the blocking bit, and the OWN-COMPOSITION
subtlety is handled by the orthogonal root marker, not a finer edge type.

Dep-maps — the per-chapter dependency sections and the `concepts/`-level dependency map —
are where edges are declared; each edge is marked `depends-on` or `reference` *deliberately*
(a default of `depends-on` is wrong: an edge to a root is `reference`). The exact authoring
grammar is the [Graded-stack scheme](./graded-stack-scheme.md).

### The two linters

Both live under `tools/` (purpose-built evaluation tooling) and read the same typed graph:

- **Rank linter** — graph-walks the `depends-on` edges and asserts
  `rank(u) ≤ min over depends-on deps of rank(v)` for every node. It reports rank
  violations (e.g. a `firm` entry resting on a `rough-in` dep) and, for free, emits the
  **promotion frontier** — the nodes all of whose deps are already ≥ their target rank.
- **Reachability GC** — marks outward from the feature-root node-set over `depends-on`
  edges; unmarked nodes are **garbage**. It reports detritus, unjustified vocabulary, and
  dead intent (roadmap_goals whose pull-chain no longer reaches a root).

**Artifact health** = *every node reachable from a root* **and** *the rank invariant holds*.
