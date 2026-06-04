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

### Worked example — rank propagating upward (the cycles 088–091 cascade)

The `matrix-weighted-norm` cascade is exactly a wave of rank propagating upward under
the invariant. The relevant fragment of the DAG (`depends-on` edges, leaf at the
bottom):

```text
   feature columns: capacitance, inductance, electrostatic,   energy-fields
                    magnetostatic   (depends-on gram_reduce)   (depends-on
                          |                                      domain_energy_reduce)
                          v                                          v
                    gram_reduce (L4)                        domain_energy_reduce (L4)
                          |                                          |
                          +--------------- depends-on ---------------+
                                            |
                                            v
                            matrix-weighted-norm (L1)  ── the leaf that firmed
```

Before cycle-091, `matrix-weighted-norm` sat at `rough-in (test-coverage-bounded)`: its
structure was anchored, but its norm-axiom laws (triangle, Cauchy–Schwarz, parallelogram)
were gated on a missing direct test of the SPD-weighted `√`-entry-point. By the invariant,
**nothing above it could exceed `rough-in`** — so `gram_reduce` and `domain_energy_reduce`
were each capped at `rough-in`, and every feature column depending on them was capped at
`seed`. The cap was a *consequence* of the leaf's rank, not an independent decision at each
node.

Cycles 088–089 discharged both law-sides of the leaf (the structure-side laws are
inner-product-space theorems whose SPD premise holds provably-by-construction at the usage
sites; the floating-point sub-claims inherit additively from the firm constituents `dot`
and `apply_linop` through a deterministic IEEE-754 outer `√`). The batch-28 meta-phase then
judged the lone remaining test gate **redundant**, and cycle-091 flipped
`matrix-weighted-norm` to **`firm` (rank 3)**.

Once the leaf firmed, the cap lifted and rank **propagated upward**:
`domain_energy_reduce` — all of whose `depends-on` deps were now firm — promoted to `firm`
in the same cascade wave, and through it the `energy-fields` feature column promoted to
`firm`.

The cascade is also an honest illustration of the invariant **holding things back where a
support is still soft**: `gram_reduce` did **not** promote, because it folds the
*off-diagonal* `bilinear-form` primitive, which is still `rough-in`. So `gram_reduce` stays
`rough-in`, and the four columns over it — `capacitance`, `inductance`, `electrostatic`,
`magnetostatic` — correctly stay `seed`. The next leaf to firm (`bilinear-form`, probe
discharged cycle-092) is the convergent blocker whose flip will let that rank wave continue
upward to those four columns. The promotion frontier *is* this rank-discontinuity surface.

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
  (frozen Phase-1 slices, kickoff-dead scaffolding, dead `priorities.md` active-heads) are
  precisely the *unreachable* nodes.
- **The `roadmap_goal` proliferation guard *is* the reachability requirement.** A
  roadmap_goal is justified only if its pull-chain terminates at a feature root. No path to
  a root ⇒ speculation-noise ⇒ collected.

So **orphaned-intent GC and detritus GC are the same sweep**, run uniformly over built and
intended nodes.

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
