---
agent: layer-intro-author
invoked_at: 2026-06-05T223620Z
scope: type concepts/counter-update.md as a graded-stack NODE (rank + typed edges); resolve OQ concepts-counter-update-needs-node-rank-and-depends-on-edges
status: pending
integrated_at: 2026-06-05T230500Z
integration_commit: fd5fabd175ffc45a4e75dbf9907b4a53a42093e5
integration_notes: "Applied clean (staging row D2, cycle-108 batch-34 position 3/3). Typed concepts/counter-update.md as a firm NODE (rank: firm, kind: primitive, depends-on: [], reference: [state-stratification, preconditioning-framework, krylov-step]); body prose unchanged. The state-stratification depends-on candidate down-typed to reference per well-foundedness (non-node). untyped 61→60. Honestly NOT forced reachable (reference-only edges, no consumer depends-on it — the expected critic-reproduced outcome; no depends-on manufactured to chase reachability). detritus +1 (typed-but-unreached node). cargo make book EXIT 0; no finalize build-repair. Resolved OQ concepts-counter-update-needs-node-rank-and-depends-on-edges. All per-report safety-net gates PASS/N/A (rank gate vacuous on depends-on: []); global retroactive-budget 0."
---

# CYCLE: concepts/counter-update node typing

## Summary

Type `book/src/concepts/counter-update.md` as a graded-stack **DAG node** (the single
c107-D2 deferral; batch-33 §5 ratified it a NODE, unlike the 15 sibling strict-zero pages
typed `reference`-only non-nodes). I assign **`rank: firm`** + an `edges:` block. The content
supports `firm` (fully-specified `## L2 form`, a settled syntactic-identity definition, ≥2 real
on-disk consumers); the laws are the syntactic-identity case (an in-place integer increment),
so the firm-on-positive-structure reading applies.

**One deliberate departure from the OQ's recommended resolution:** the planner/OQ suggested a
`depends-on (kind: classifies) → concepts/state-stratification` edge. I verified that this edge
is **already classified `ref` (navigational) in the derived dependency-map view**
(`concepts/dependency-map.md:131` — `counter-update -.->|ref| state-stratification`), and that
`state-stratification` is itself encoded as a **non-node** (no `rank:`; a `reference`-only block,
`book/src/concepts/state-stratification.md:1-8`). The page's own §See-also calls the relationship
*justificatory* ("the classification that **justifies** separating counter-update"), not a
constructive dependency. So the honest typing is **`reference`, NOT `depends-on`** — resting a
`firm` node's blocking foundation on a no-rank non-node would be exactly the well-foundedness
murk the scheme avoids. `counter-update` therefore carries an **empty `depends-on:`** (its L2
definition is self-contained syntactic identity; it rests on no cited L0 struct, so I invent no
`cites-evidence` edge) and `reference` edges to its classification basis + its three on-disk
use-sites. Well-foundedness holds trivially (no blocking deps to violate).

## Proposed changes

Prepend a YAML frontmatter block to `book/src/concepts/counter-update.md` (the body prose is
unchanged — frontmatter + minimal typing only, no semantics rewrite). The current first line is
the H1 `# counter-update`; the new block goes above it.

```edit:book/src/concepts/counter-update.md
[old]: # counter-update

A small bookkeeping primitive denoting in-place increment of an integer counter held inside a solver-state bundle.
[new]: ---
rank: firm
kind: primitive
edges:
  depends-on: []
  reference:
    - concepts/state-stratification
    - L4/preconditioning-framework
    - L3/krylov-step
---
# counter-update

A small bookkeeping primitive denoting in-place increment of an integer counter held inside a solver-state bundle.
```

### Edge-classification justification (per §2 deliberate typing)

| edge | type | why |
|---|---|---|
| `concepts/state-stratification` | `reference` | The classification that *justifies* the counter/iterate split (page §State-classification + §See-also). Already wired `ref` in `dependency-map.md:131`. Target is a non-node (no `rank:`), so it cannot be a blocking `depends-on` target anyway. |
| `L4/preconditioning-framework` | `reference` | Use-site: `solve` threads `counters.mult` via `modifyCounters` (`L4/preconditioning-framework.md:201`; named in the page §Used-by). A use-site is an inbound reference *to* counter-update; encoded here as the reciprocal navigational see-also. |
| `L3/krylov-step` | `reference` | Use-site: the L3 `let s' = s { it = s.it + 1 }` counter-update line (`L3/krylov-step.md:64`). |

`depends-on: []` — empty. `counter-update` is a self-contained L2 syntactic-identity primitive
(`c ← c + δ`); it cites no L0 backing struct, so I add no `cites-evidence` `depends-on` (inventing
one would be a fabricated citation). The fourth on-disk mention,
`L1-L0/ksp-solve-mutation-rotation.md:130`, is an additional use-site link but I keep the
`reference` set to the three primary consumers to avoid over-wiring; it is harmless to add if the
integrator prefers completeness.

## Supporting evidence

**Rank judgment — `firm`:**
- `## L2 form` is fully specified (`counter-update.md:5-12`): `counter_update(c: &mut int, δ: int): c ← c + δ` with explicit `&mut` in-place mutation semantics. Not a sketch.
- Classification basis present (`counter-update.md:14-16`): the observability/diagnostic stratum of `state-stratification`, carriable in a `Writer`-like effect.
- ≥2 real consumers on-disk (the node-status bar): `L4/preconditioning-framework` (firm), `L3/krylov-step`, `L1-L0/ksp-solve-mutation-rotation` — confirmed by grep.
- Laws are syntactic identities on a fully-specified positive form (an integer increment) — the firm-on-positive-structure / syntactic-identity reading (CLAUDE.md §`rough-in (test-coverage-bounded)` "firm-on-positive-structure escape"). No surrounding test gates a syntactic-identity law, so `firm` is honest, not inflated.

**Well-foundedness:** `depends-on: []` ⇒ trivially well-founded (no blocking edge to check). `rank: firm` rests on nothing below it.

**Edge-target resolution (all resolve on-disk):**
- `book/src/concepts/state-stratification.md` ✓
- `book/src/L4/preconditioning-framework.md` ✓
- `book/src/L3/krylov-step.md` ✓

**Linter before / after** (`python3 tools/graded-stack-lint/graded_stack_lint.py`; AFTER measured
by temporarily applying the proposed frontmatter, linting, then reverting — no book write persisted
in this dispatch phase):

```
                         BEFORE        AFTER
typed nodes:               294    →      295
untyped (WARNING):          61    →       60      (counter-update leaves the untyped set)
RANK VIOLATIONS:          none    →     none      (held — invariant satisfied)
reachable from roots:       95    →       95      (held — counter-update NOT reachable)
detritus nodes:            163    →      164      (counter-update joins detritus: typed-but-unreached)
unresolved depends-on:       0    →        0      (all 3 reference targets resolve on-disk)
RESULT line:  0 rank violation(s), 164 detritus node(s), 60 untyped (warning).
```

**Reachability — honestly NO.** After typing, `counter-update` is reported `[garbage?]
concepts/counter-update` (typed DAG node, unreachable from any feature root). This is correct and
NOT forced: a node becomes reachable only when a *reachable* node carries a typed `depends-on`
edge **to** it. No node `depends-on` counter-update today (its inbound mentions are `reference`
use-sites, which carry no liveness by design, §2), and its consumers `preconditioning-framework`
+ `state-stratification` are themselves currently `[GARBAGE*]`/`[garbage?]` detritus in the
pre-P1 graph. I did not invent a `depends-on` to manufacture reachability — that would violate the
"note honestly, don't force" instruction and the §3 liveness semantics. counter-update will become
live when the broader P1 typing pass connects its firm consumer (`preconditioning-framework`) up to
a feature root and that consumer's edge to the counter-update concept is (if ever) re-typed
`depends-on` — but on current evidence the consumer's reference to the *concept* is navigational,
so counter-update may legitimately remain a reachable-only-via-reference concept page. The detritus
count rising 163→164 is the expected pre-P1 edge-untypedness artifact the linter itself annotates,
not new garbage.

## Open questions / caveats

- **OQ `concepts-counter-update-needs-node-rank-and-depends-on-edges` (cycle-107 D2) — RESOLVED by this dispatch.** counter-update is now a typed NODE: `rank: firm` + an `edges:` block. The OQ's recommended `depends-on → state-stratification` was **down-typed to `reference`** on verification (the edge is already `ref` in `dependency-map.md`, and `state-stratification` is a non-node — a `firm` node cannot take a blocking `depends-on` on a no-rank node). The OQ noted "no DAG node carries a typed `depends-on: concepts/counter-update` edge today, so the deferral introduces no live rank-violation" — that remains true after this typing (counter-update's own `depends-on` is empty, and nothing depends-on it), confirmed: `rank_violations` held 0, `reachable` held 95, unresolved targets 0.
- **`kind: primitive` is documentation only** (the linter ignores `kind:`); I chose `primitive` over `record` because counter-update defines a *verb* (in-place increment), not a data shape — it is not a record-definition concept page. If a future pass prefers no `kind:` on non-record concept nodes, dropping it is invariant-neutral.
- **state-stratification is a non-node today** (no `rank:`, `reference`-only block). It is referenced by ≥3 firm nodes (`sim-state`, `preconditioning-framework`, now `counter-update`) and arguably should itself be promoted to a rank-bearing node in a future pass so that classification edges to it can become blocking where genuinely constructive. Out of scope here (one page per invocation); flagging for the P1 frontier. No new OQ filed — this is a known consequence of the c103/c107 non-node-encoding of taxonomy concept pages, not a new defect.
- Did NOT touch `concepts/dependency-map.md`, `concepts/index.md`, or `SUMMARY.md` — the existing `ref` edge in the derived dependency-map view is now consistent with the authoritative `reference` edge I added (no drift introduced).
