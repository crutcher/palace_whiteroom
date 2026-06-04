---
agent: layer-intro-author
invoked_at: 2026-06-04T22:35:00Z
scope: methodology/resolution-ladder.md worked-example repair (c095-cascade falsification)
status: integrated
integrated_at: 2026-06-05T001500Z
integration_commit: 2b8cb55b1fe4d011c4fd384b0b6f6459097804ba
integration_notes: |
  Applied clean (D2, cycle-096 batch-30 position 3/3). methodology/resolution-ladder.md worked-example repair (x3): the c094 FALSIFIED forward-prediction re-told as the COMPLETED c091/c095 two-wave cascade discharge (heading "cycles 088-095 cascade, completed"; DAG surfaces gram_reduce's second off-diagonal bilinear-form leaf). Non-authoritative methodology page; all typed-edge gates no-op. citecheck 7 ok / 0 failing. Build clean. Resolves the resolution-ladder.md half of OQ bilinear-form-firm-flip-stale-narration-in-meta-owned-methodology-pages (goal-flow.md half stays OPEN, meta-owned).
---

# CYCLE: resolution-ladder.md worked-example repair

## Summary

The worked example in `book/src/methodology/resolution-ladder.md` (§"Worked example — rank
propagating upward", lines 91–136) was authored c094 and its closing paragraph (lines 130–136)
predicted a *hypothetical hold-back*: `gram_reduce` "stays `rough-in`" because its off-diagonal
`bilinear-form` primitive "is still `rough-in`", and the four columns over it (`capacitance`,
`inductance`, `electrostatic`, `magnetostatic`) "correctly stay `seed`". The **c095 cascade
falsified this**: `bilinear-form` firmed (c095, D1), `gram_reduce` firmed (c095, D3), and all four
feature columns reached `rank: firm` (c095). A reader-facing methodology page now carries a wrong
prediction stated as present-tense fact.

This report re-tells the example as a **completed rank-propagation success** — the well-foundedness
invariant now demonstrated by a *discharge* (the two-leaf cascade that actually happened: `matrix-weighted-norm`
firmed c091, then `bilinear-form` firmed c095, propagating rank upward through `gram_reduce` /
`domain_energy_reduce` to all five output-product / driver columns), not a hypothetical block. The
§rank-ladder and §invariant prose are left intact; only the worked example changes (three edits:
the section heading, the DAG diagram to surface the second leaf, and the closing paragraph).

**Scope:** this resolves the `resolution-ladder.md` half of OQ
`bilinear-form-firm-flip-stale-narration-in-meta-owned-methodology-pages`. The `goal-flow.md:260-266`
half is meta-phase-owned and is **not** touched here (per the c096 planner partition).

## On-disk status verification (every cited node, read this dispatch)

Every node the repaired example asserts a status for was read from its authoritative `## Status`
line / frontmatter on disk this cycle (NOT from the cycle record, NOT from any index cell):

| Node | Layer/kind | On-disk status | Promoted | Source read |
|---|---|---|---|---|
| `matrix-weighted-norm` | L1 (diagonal leaf) | `firm` | c091 | `book/src/L1/matrix-weighted-norm.md:121-123` |
| `bilinear-form` | L1 (off-diagonal leaf) | `firm` | c095 | `book/src/L1/bilinear-form.md:329-331` |
| `domain_energy_reduce` | L4 reduce verb | `firm` | c091 | `book/src/L4/domain_energy_reduce.md:272-274` |
| `gram_reduce` | L4 reduce verb | `firm` | c095 | `book/src/L4/gram_reduce.md:229-238` |
| `energy-fields` | feature column | `feature_root: seed` / `rank: firm` | c091 | `book/src/feature/energy-fields.L4.md` (frontmatter + `:153`, `:185`) |
| `capacitance` | feature column | `feature_root: seed` / `rank: firm` | c095 | `book/src/feature/capacitance.L4.md` (frontmatter + `:66-68`) |
| `inductance` | feature column | `feature_root: seed` / `rank: firm` | c095 | `book/src/feature/inductance.L4.md` (frontmatter + `:69`) |
| `electrostatic` | feature column | `feature_root: seed` / `rank: firm` | c095 | `book/src/feature/electrostatic.L4.md` (frontmatter + `:77`) |
| `magnetostatic` | feature column | `feature_root: seed` / `rank: firm` | c095 | `book/src/feature/magnetostatic.L4.md` (frontmatter + `:77`) |

Two-axis confirmation: every column carries `feature_root: seed` (the permanent root-set marker, Axis 2)
**and** `rank: firm` (the resolution maturity, Axis 1) — which is exactly the two-axis separation the
page itself teaches (the `seed` marker does not collapse into the ladder). The repaired example states
the columns reached `firm` *resolution* while their `seed` root-role is unchanged — consistent with the
page's Axis-2 prose at lines 183–186.

Dependency structure verified from the firm chapters' Status/Evidence prose:
- `gram_reduce` folds **two** L1 leaves — the diagonal `matrix-weighted-norm` radicand (firm c091) and
  the off-diagonal `bilinear-form` (firm c095): `book/src/L4/gram_reduce.md:229-238`, corroborated at
  `book/src/feature/electrostatic.L4.md:49` ("the diagonal … is the firm `matrix-weighted-norm` radicand
  (firm c091), the off-diagonal … is the firm `bilinear-form` (firm c095)").
- `domain_energy_reduce` folds **only** `matrix-weighted-norm` (`book/src/L4/domain_energy_reduce.md:272-282`)
  — which is why it firmed in the c091 half, one wave ahead of `gram_reduce`.

The original DAG diagram showed both reduce verbs resting on a single `matrix-weighted-norm` leaf; that
is incomplete for `gram_reduce` (it also folds `bilinear-form`, the leaf whose c095 flip is the whole
point of the discharge). Edit 2 surfaces the second leaf so the completed two-leaf cascade is legible.

## Proposed changes

### Edit 1 — section heading (cascade now spans 088–095)

```edit:book/src/methodology/resolution-ladder.md
[old]: ### Worked example — rank propagating upward (the cycles 088–091 cascade)
[new]: ### Worked example — rank propagating upward (the cycles 088–095 cascade, completed)
```

### Edit 2 — DAG diagram: surface the second (off-diagonal) leaf

```edit:book/src/methodology/resolution-ladder.md
[old]: ```text
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
[new]: ```text
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
```

### Edit 3 — closing paragraphs: re-tell as a completed two-leaf discharge

```edit:book/src/methodology/resolution-ladder.md
[old]: Cycles 088–089 discharged both law-sides of the leaf (the structure-side laws are
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
[new]: The cap lifted in **two waves**, one per leaf — and the whole chain is now `firm`, so this
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
```

## Supporting evidence

- The §rank-ladder (lines 32–59) and §well-foundedness-invariant (lines 61–89) prose is unchanged —
  per the planner D2 scope ("Keep the §rank-ladder + §invariant prose intact; only the worked example
  changes").
- The repaired example continues to teach exactly the invariant the page asserts (`rank(u) ≤ min over
  depends-on deps`), but via a *discharge* the reader can verify against disk rather than a prediction
  that has since been falsified — which also makes it a stronger pedagogical example (it now shows BOTH
  the hold-back regime, Wave 2 before c095, AND the propagation regime, the c095 flip, in one chain).
- The two-axis `feature_root: seed` + `rank: firm` separation surfaced in the repaired example is the
  same separation the page already teaches at lines 183–186 ("the `seed → firm` flips … were maturity
  events on nodes whose root-role never changed") — the repair reinforces, does not contradict, the
  existing Axis-2 prose.
- The DAG edit corrects a *pre-existing* incompleteness (the original diagram hid `gram_reduce`'s second
  leaf), which is what made the original closing paragraph's `bilinear-form` reference appear out of
  nowhere. The corrected diagram makes the two-leaf structure — and thus the two-wave discharge —
  self-evident.

## Open questions / caveats

- **`goal-flow.md:260-266` is deliberately untouched** — it carries the SAME stale "stay rough-in /
  stay seed" cascade narration but is meta-phase-owned; the batch-30 meta-phase goal-flow refresh
  reconciles it (per the c096 planner partition + OQ
  `bilinear-form-firm-flip-stale-narration-in-meta-owned-methodology-pages`). This dispatch fixes ONLY
  the layer-intro-author-owned `resolution-ladder.md` half; the OQ should be marked partially-resolved
  (resolution-ladder half closed, goal-flow half open) at integration.
- This page is **reader-facing NON-AUTHORITATIVE methodology** (it carries the banner at lines 3–18).
  No `rank:`/`edges:` frontmatter is added — the page itself states methodology pages sit *outside* the
  subject DAG (lines 216–220), so no graded-stack typing applies. The repair is prose-only.
- No down-link / sibling edits: this is a methodology page, not a feature column or operator entry, so
  the index-cell-flip and whole-`feature/` sibling-status grep guards (which apply when *flipping a
  column's status*) do not bind here — the columns' statuses already flipped at c095; this repair only
  narrates that completed reality on a non-authoritative page.
