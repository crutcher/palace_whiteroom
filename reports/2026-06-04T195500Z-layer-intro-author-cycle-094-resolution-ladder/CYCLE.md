---
agent: layer-intro-author
invoked_at: 2026-06-04T195500Z
scope: P3 — book methodology page book/src/methodology/resolution-ladder.md (reader-facing mirror of the graded-stack two-axis health model)
status: pending
integrated_at: 2026-06-04T211500Z
integration_commit: PLACEHOLDER_SHA_CYCLE_094
integration_notes: "Applied clean (D3, cycle-094 batch-30 position 1/3). Created book/src/methodology/resolution-ladder.md (P3, the reader-facing NON-AUTHORITATIVE two-axis mirror) + SUMMARY row inserted BETWEEN Goal & Flow and Graded-stack scheme (named final order). Forward-link ./graded-stack-scheme.md resolves under linkcheck2. Outside the subject DAG per §2d. retroactive-budget 0; build exit 0; no build-repair. 2 OQs promoted."
---

# CYCLE: methodology/resolution-ladder.md (the graded-stack reader-facing mirror)

## Summary

Authors the **new** reader-facing methodology chapter `book/src/methodology/resolution-ladder.md` — the
NON-AUTHORITATIVE mirror of the two-axis artifact-health model defined in
`METHODOLOGY-GRADED-STACK.md` (user directive 2026-06-04), per its §9 instructions.

The page covers both axes:
- **Axis 1 — resolution + well-foundedness:** the graded ladder `roadmap_goal=0 < stub=1 < rough-in=2 < firm=3`
  (sub-ranks 2.5; obstruction a separate rankable kind) + the well-foundedness invariant
  `rank(u) ≤ min over depends-on deps of rank(v)`, with the **matrix-weighted-norm → gram_reduce /
  domain_energy_reduce → feature-columns cascade of cycles 088–091** as the worked example of rank
  propagating UPWARD through the DAG once a leaf firms.
- The `roadmap_goal` chapter (rank 0, a real book chapter) + the `stub` vs `roadmap_goal` line (§1e).
- **Axis 2 — reachability / liveness:** the feature-surface-spine columns as the GC root set; reachability
  over `depends-on` edges = liveness; unreachable = garbage; the detritus hunt is a mark-sweep from the
  roots, and orphaned-intent GC + detritus GC are one sweep.
- **Shared substrate:** one typed dependency graph (`depends-on` blocking vs `reference` free; edge-to-a-root
  is `reference`; optional linter-ignored `kind:`) + the two `tools/` linters (rank check + reachability GC).

The page is a methodology mirror **outside** the subject DAG (§2d), so it carries NO rank/edge frontmatter.
It states the non-authoritative-mirror convention up front (same pattern as `goal-flow.md`) and
forward-references the **authoritative** scheme page D1 authors this cycle by its exact canonical slug
`book/src/methodology/graded-stack-scheme.md`. Wired into `SUMMARY.md` under `# Methodology` AFTER
`goal-flow.md` (ordering: overview → goal-flow → resolution-ladder [this] → graded-stack-scheme [D1]).

Per the planner's overlap analysis, **D1 owns the SUMMARY insert-position discipline for both new
methodology rows this cycle**; this report inserts only its own `resolution-ladder.md` row at the named
position (overview → goal-flow → resolution-ladder → graded-stack-scheme). If the integrator stages D1's
row first, the two appends compose; if a mild ordering conflict surfaces it is the cheap per-report SUMMARY
merge the planner anticipated.

## Proposed changes

### 1. New file `book/src/methodology/resolution-ladder.md`

```edit:book/src/methodology/resolution-ladder.md
[old]:
[new]:
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
```
```

### 2. Wire into `book/src/SUMMARY.md` under `# Methodology` (after `goal-flow.md`)

```edit:book/src/SUMMARY.md
[old]:
# Methodology
- [Overview](./methodology/overview.md)
- [Goal & Flow](./methodology/goal-flow.md)
[new]:
# Methodology
- [Overview](./methodology/overview.md)
- [Goal & Flow](./methodology/goal-flow.md)
- [Resolution ladder & reachability](./methodology/resolution-ladder.md)
```

> **Integrator note on SUMMARY ordering (per planner overlap analysis D1↔D3).** D1 owns
> the SUMMARY insert-position discipline for both new methodology rows this cycle; the
> intended `# Methodology` ordering is `overview → goal-flow → resolution-ladder` (this
> report) `→ graded-stack-scheme` (D1). This report's edit appends the
> `resolution-ladder` row immediately after `goal-flow`. When D1's `graded-stack-scheme`
> row is staged, it lands *after* this one. If both reports' old/new anchors collide on
> the same two-line `# Methodology` block, apply this report's edit first (it appends one
> row) then D1's (it appends its row after) — the result is the four-row ordering above.

## Supporting evidence

- **Authoritative spec:** `METHODOLOGY-GRADED-STACK.md` in full — §1 (Axis 1: ladder + the
  `rank(u) ≤ min(deps)` invariant + `roadmap_goal` + `stub` vs `roadmap_goal`), §2 (Axis 2:
  root set + reachability + OWN-COMPOSITION-from-root-marker + graph boundary §2d + fan-out
  §2e), §3 (typed-edge substrate / minimal binary), §4 (the two linters), §9 (the
  reader-facing-mirror instruction this page executes). The page mirrors these and states
  the spec wins on conflict.
- **Reader-facing-tone + non-authoritative-mirror precedent:** `book/src/methodology/goal-flow.md`
  (the `⟢ NON-AUTHORITATIVE` banner, the "source wins / contradiction = drift signal"
  framing, the GOAL/FLOW exposition register). This page reuses that banner shape verbatim
  in spirit, retargeted to `METHODOLOGY-GRADED-STACK.md`.
- **Worked-example artifacts (status lines read on-disk per role-spec, not from the cycle
  record):**
  - `book/src/L1/matrix-weighted-norm.md` `## Status`: **`firm`** — "promoted from
    `rough-in (test-coverage-bounded)` by the batch-28 meta-phase GO … enacted cycle-091";
    both norm-axiom law-sides discharged (structure-side cycle-088, FP-side cycle-089), the
    lone test gate judged redundant. This is the leaf that firmed.
  - `book/src/L4/domain_energy_reduce.md` `## Status`: **`firm`** — "promoted from
    `rough-in` by the cycle-091 batch-29 firm-flip-and-cascade wave … coupled to the
    `matrix-weighted-norm` firm flip." The upward-propagation cascade-yield.
  - `book/src/feature/energy-fields.L1.md` frontmatter `status: firm` (and `.L4.md`
    `status: firm`) — the feature column that promoted through `domain_energy_reduce`.
  - `book/src/L4/gram_reduce.md` `## Status`: **`rough-in (test-coverage-bounded)`** — did
    NOT promote, because it folds the off-diagonal `bilinear-form` primitive, still
    `rough-in`. The honest "invariant holds things back" half of the worked example.
  - `book/src/L1/bilinear-form.md` `## Status`: **`rough-in`** — the next convergent leaf
    (probe discharged cycle-092 per `goal-flow.md`); its eventual firm flip continues the
    rank wave to `capacitance`/`inductance`/`electrostatic`/`magnetostatic`.
  - `book/src/feature/electrostatic.L4.md` / `capacitance.L4.md` frontmatter
    `status: seed` — correctly held at `seed` on the genuine own-constituent `gram_reduce`
    gate (verifying the invariant-holds-things-back narrative, not a sibling blocker).
- **Forward-ref slug coordination (c048 convention, named in both D1 and D3 scopes):** the
  page forward-references D1's authoritative scheme page by the exact canonical slug
  `book/src/methodology/graded-stack-scheme.md` — relative link `./graded-stack-scheme.md`.
  Per the integrator-finalize note, this link resolves once D1's page is staged in the same
  cycle; if D1's page is not yet on disk at per-report integration time, `linkcheck2` would
  flag the link as a missing anchor — the integrator wires D3's forward-link to D1's scheme
  page once **both** are staged (the planner's wave-2 finalize note). Both pages land this
  cycle, so the link is live at finalize.

## Open questions / caveats

- **OQ-intake for the batch-30 meta-phase — `goal-flow.md` GOAL/FLOW additions (deferred
  by scope, NOT authored here).** `METHODOLOGY-GRADED-STACK.md` §9 + §8 specify that the
  GOAL section of `goal-flow.md` should gain "two checkable health invariants
  (well-foundedness + reachability)" and the FLOW section should gain the typing+audit
  campaign + the `roadmap_goal` tier; §9 also notes this resolves the open
  `goal-flow-mwn-firm-flip-cascade-refresh-stale-rough-in-refs` OQ. `goal-flow.md` is
  **meta-phase-owned** (the seed transferred ownership), so this report does NOT touch it.
  Flagging for the batch-30 meta-phase to fold into its goal-flow refresh.
- **`## Roadmap goals — unbuilt frontier` SUMMARY grouping is NOT added this cycle (per
  scope).** No `roadmap_goal` chapters exist on disk yet — that grouping (and the unmissable
  per-chapter banner) lands when P2 mints the first `roadmap_goal` chapter (the
  graded-stack §6 migration surfacing e.g. the un-authored `orthogonalize-mutation-rotation`
  L1>L0 theme). The page's prose describes the grouping/banner convention so readers
  understand it before any such chapter exists, but the SUMMARY wiring is deferred.
- **Forward-link liveness depends on D1 landing this cycle.** The page's
  `./graded-stack-scheme.md` link is live only because D1 authors that page in the same
  cycle. If D1 slips, the integrator should either (a) stage D1's page anyway as part of
  this cycle, or (b) defang the single forward-link to plain text per the
  `rough-in-rows-must-be-plain-text-when-anchor-missing` convention until the scheme page
  lands. Flagged so the per-report integrator is not surprised by a transient missing
  anchor.
- **The worked example's DAG fragment is a hand-drawn illustration, not a linter-emitted
  graph.** The `depends-on` edges shown (columns → reduce verbs → matrix-weighted-norm) are
  faithful to the on-disk `## Status` chains and the goal-flow cascade narrative, but the
  artifact's edges are not yet machine-typed (that is the P1 campaign). Once P1 types the
  edges and the rank linter runs, the illustration should be cross-checked against the
  linter's actual emitted frontier; if they diverge, the linter (mechanical truth) wins and
  this page's diagram is corrected. Noting so a future refresh re-verifies the diagram
  against the live graph rather than against this prose.
