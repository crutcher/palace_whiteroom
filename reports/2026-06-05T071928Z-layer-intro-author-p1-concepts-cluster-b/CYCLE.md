---
agent: layer-intro-author
invoked_at: 2026-06-05T071928Z
scope: P1 graded-stack typed-edge campaign — concepts/ cluster B (solver / iteration / calculus-typing vocabulary, 17 pages)
status: pending
integrated_at: 2026-06-05T085500Z
integration_commit: INTEGRATION_SHA_PLACEHOLDER
integration_notes: >
  Applied clean (cycle-103 D2, staging row 3 — P1 typed-edge campaign concepts cluster B).
  The ONE node of the 17-page set, config-record, typed rank: firm + 3 cites-evidence L0
  depends-on edges (iodata.hpp / configfile.hpp / labels.hpp) + 8 reference edges to feature
  roots; its 16 non-node siblings got NO frontmatter (the strict §5 zero-encoding — DIVERGES
  from D1/D3, routed for meta unify). overall_status: ready set by the repairer (accept-and-route
  on the lone skill-uptake-survey WARNING). Build green. step-5b rank_violations: 0 (config-record
  firm rests on cites-evidence L0 edges, vacuous). config-record is reachability-garbage until a
  consumer adds a uses-record edge (OQ config-record-reachability-gap, routed). The lone citecheck
  AMBIG (main.cpp:259) is a pre-existing body cite, not one of the 3 applied edge targets.
---

# CYCLE: P1 typed-edge pass — concepts/ cluster B

## Summary

Cycle-103 D2, first tranche of the graded-stack typed-edge campaign (P1). I audited
all 17 cluster-B concept pages and applied the node-vs-not-a-node classification from
the graded-stack scheme (`graded-stack-scheme.md` §2d/§5; `METHODOLOGY-GRADED-STACK.md`
§2d). The result is a clean split:

- **1 DAG node** — `concepts/config-record.md` is a **record-definition page**
  (defines a data shape that signatures rest on, scheme §5 record sub-case). It gets a
  `rank: firm` + `edges:` frontmatter block (the only proposed file edit in this report).
- **16 NON-nodes** — the other 16 are *meta / narrative-pointer / methodology layer-pattern*
  concept pages that sit **outside the subject DAG** (scheme §2d: "a concept page that is a
  *meta page about the construction* sits outside the subject DAG — no `rank:`/`edges:`,
  like this scheme page"). They get **no frontmatter** — typing them as nodes would be a
  scheme violation. The typing pass *visited and deliberately classified* each (table below);
  the determination is recorded here for the meta-phase node-status unification, not written
  to disk as frontmatter.

This matches the dispatch's explicit anticipation ("Resolve concept-page node-vs-not-a-node
inline ... record the convention you apply"). Cluster B is almost entirely
pattern/methodology vocabulary; only `config-record` is a record-definition node.

## Node-status convention applied (for meta-phase unification across D1/D3/D4/D5)

**The rule I applied, per scheme §2d/§5:**

1. A concept page that is a **narrative pointer** to an authoritative L_n operator entry
   (the L_n entry is the definition; the concept page forwards to it and explicitly says
   "if this page and the L_n entry disagree, the L_n entry wins") → **NOT a node**, no
   frontmatter. The page documents the construction; the DAG node is the L_n entry it points
   at. (e.g. `eigsolve`, `ksp_solve`.)
2. A concept page that is a **methodology / layer-pattern** page (names a *rotation pattern* /
   *stratification discipline* / *absorption route* — "methodology, not a tensor primitive",
   in the words several of these pages already use about themselves, cf. `rotation.md`) →
   **NOT a node**, no frontmatter. (e.g. `solve-monad`, `state-stratification`,
   `capability-typing`, `constructed-operators`, `solver-as-operator`, …)
3. A concept page that is a **record-definition** page (defines a *data shape* — fields,
   types, stratum, L0 backing struct — that ≥2 signatures rest on) → **IS a node**,
   `rank:` (the resolution of the shape; typically `firm` once the backing struct is cited)
   + `edges:`. (e.g. `config-record`.)

**Boundary calls I want meta-phase to confirm against D1/D3/D4/D5:**
- `counter-update` — defines a tiny L2 bookkeeping *primitive* (signature + state
  classification) with no `L2/counter-update.md` operator home; I classified it **NOT a node**
  (a pattern/primitive-naming page in the `solver-as-operator` / `constructed-operators` mold,
  whose algebra is exercised in the operator entry `L4/preconditioning-framework` that
  consumes it). It is a borderline case: if the unified convention decides "a concept page
  that is the *sole definition site* of a primitive a real node `depends-on` is itself a node",
  this flips to a `rank: firm` node. Flagged as OQ.
- `chebyshev-iteration` — a pre-redirect *background / literature* concept page (the math of
  Chebyshev iteration), no authoritative-L_n forward (the L_n homes
  `L1/chebyshev-smoother`, `L2/chebyshev-iteration`, `L3/chebyshev` reference IT as
  see-also background, not vice-versa). Classified **NOT a node** (background documentation,
  carries no claim the DAG rests on). Flagged as OQ alongside `counter-update`.

### Classification table (all 17)

| page | kind | node? | rationale |
|---|---|---|---|
| `eigsolve` | narrative-pointer (→ L1/L2/L3 eigsolve, L0 wrapper) | NO | explicitly "the L_n entry wins"; definition lives in the chain entries |
| `ksp_solve` | narrative-pointer (→ L2/L1 ksp_solve) | NO | the KSP primitive's algebra lives in the L_n entries |
| `solve-monad` | L4 layer-pattern (methodology) | NO | a state-monad coordination *pattern*, not a node |
| `solver-as-operator` | layer-pattern (methodology) | NO | a type-level rotation pattern |
| `convergence-test` | methodology pattern | NO | "this is a methodology pattern" (own prose) |
| `state-stratification` | L4 layer-pattern (methodology) | NO | the three-strata discipline; a pattern |
| `constructed-operators` | methodology | NO | "this concept is **methodology**, not a tensor primitive" (own prose) |
| `constructed-operator-factory` | layer-pattern (methodology) | NO | names the factory pattern; the L2 factory algebra lives elsewhere |
| `nested-constructed-operator-gate` | layer-pattern (methodology) | NO | a composition-of-gates structural-shape pattern |
| `capability-typing` | L4 layer-pattern (methodology) | NO | a phantom-brand discipline; a pattern |
| `build-time-vs-run-time-stratification` | layer-pattern (methodology) | NO | "a layer-pattern concept ... not a runtime primitive" (own prose) |
| `derived-view-hoisting` | L4 state-hiding rotation pattern (methodology) | NO | a design pattern for L4 step-output shape |
| `erasure-scope` | classifying-axis of substantive L3>L2 themes (methodology) | NO | a taxonomy axis, not a node |
| `config-record` | **record-definition** | **YES** | defines the `IoData` data shape ≥2 signatures rest on; `rank: firm` |
| `counter-update` | primitive-naming (no L_n home) | NO (borderline) | see boundary-call note above |
| `rotation` | methodology | NO | "this concept entry is **methodology**, not a tensor primitive" (own prose) |
| `chebyshev-iteration` | background / literature | NO | pre-redirect background page; no authoritative-L_n forward |

## Proposed changes

One file edit — the `config-record` node gets its `rank:` + `edges:` frontmatter.

Edge classification for `config-record` (the only node):
- **`depends-on` / `kind: cites-evidence`** → the raw L0 backing-struct source it rests on
  (`iodata.hpp` / `configfile.hpp` / `labels.hpp`). This follows the on-disk feature-column
  convention (e.g. `feature/lifecycle.L4.md` writes `cites-evidence` edges to raw
  `palace/...:lines` paths in its `edges:` block). The record's resolution rests on its
  backing struct being cited — `cites-evidence` is the documented `kind` for an L0 evidence
  dependency (scheme §4(c), migration of `l0_ground_truth:`).
- **`reference`** → `concepts/build-time-vs-run-time-stratification` (sibling concept the page
  cross-links) and the 6 driver/ROOT feature columns it serves (edges to feature *roots* are
  `reference`, never `depends-on`, scheme §3 — and these are downstream consumers the page
  *serves*, not deps it rests on). NB the feature columns are roots; a `reference` edge to a
  root carries no liveness (correct — config-record's liveness must come from a root's
  inbound `depends-on`, see the reachability OQ below).

```edit:book/src/concepts/config-record.md
[old]:
# config-record

Cross-cutting **record-definition** page for Palace's configuration record —
[new]:
---
rank: firm
edges:
  depends-on:
    - target: palace/utils/iodata.hpp:31-60
      kind: cites-evidence            # the IoData aggregate (backing struct)
    - target: palace/utils/configfile.hpp:57-1026
      kind: cites-evidence            # the config:: sub-record structs
    - target: palace/utils/labels.hpp:18-26
      kind: cites-evidence            # the ProblemType driver-selector enum
  reference:
    - concepts/build-time-vs-run-time-stratification
    - feature/lifecycle.L4
    - feature/electrostatic.L4
    - feature/magnetostatic.L4
    - feature/driven.L4
    - feature/transient.L4
    - feature/eigenmode.L4
    - feature/boundary-mode.L4
---

# config-record

Cross-cutting **record-definition** page for Palace's configuration record —
```

## Supporting evidence

- **Scheme references read:** `book/src/methodology/graded-stack-scheme.md` (full),
  `METHODOLOGY-GRADED-STACK.md` §2d/§3/§5/§8.
- **On-disk convention sampled:** `book/src/L2/eigsolve.md` (firm operator `edges:` block
  with `depends-on` + `reference` buckets), `book/src/L3/normalize.md` (firm composite),
  `book/src/feature/lifecycle.L4.md` + `book/src/feature/electrostatic.L4.md` (feature-column
  `edges:` blocks — the `{target:, kind:}` mapping form, raw-`palace/...:lines`
  `cites-evidence` targets, sibling-column `reference` edges). I follow the feature-column
  form for `config-record`'s `cites-evidence` edges.
- **`config-record` L0 citations** (already in the page body, re-confirmed against the page's
  own existing citations — not re-read against `reference/` source this pass, as I am not
  re-authoring the body; the citations are pre-existing and were authored under the
  record-definition obligation): `iodata.hpp:31-60`, `configfile.hpp:57` / `:156` / `:1026`,
  `labels.hpp:18-26`, `main.cpp:259`. The `edges:` `cites-evidence` ranges I emit
  (`iodata.hpp:31-60`, `configfile.hpp:57-1026`, `labels.hpp:18-26`) are span-bounds over the
  citations the body already makes; they are pointer edges, not new claims.
- **All book-node edge targets verified to exist on disk** (no dangling): the 6 feature L4
  columns + `lifecycle.L4` + `concepts/build-time-vs-run-time-stratification` all present
  (`ls` confirmed). The eigsolve-page targets were also spot-verified existing (informational —
  no edits to `eigsolve` since it is a non-node).
- **No L0 book chapter for `IoData`** exists (`ls L0/*iodata* L0/*config* L0/*labels*` empty),
  so the backing-struct dependency is a raw-source `cites-evidence` edge, exactly as the
  feature columns cite raw `palace/...` source — there is no `L0/<iodata>.md` slug to point at.

## Open questions / caveats

- **`config-record-reachability-gap` (HARD, for a feature-column author — NOT me).** Under the
  reachability GC, `config-record` is currently **unreachable garbage**: nothing `depends-on`
  it. The 6 driver feature columns + lifecycle ROOT only `reference`-link config-record (and a
  `reference` edge to/from a root carries no liveness). But a driver column *genuinely uses* the
  config record as its build-time input (`*Operator(iodata, mesh)`); the faithful edge is a
  **`depends-on` / `kind: uses-record`** from each consuming feature column → `concepts/config-record`.
  I cannot make that edit (feature columns are out of my page set; the typing of feature columns
  is another dispatch's scope). **Route to the feature-column typing dispatch:** add a
  `depends-on: { target: concepts/config-record, kind: uses-record }` edge to each of the 6
  driver columns + the lifecycle ROOT so the record-definition node is reachable. Until then the
  reachability GC will (correctly) flag `config-record` as unreachable — the gap is real and is a
  finding of this typing pass, not a defect in my classification.
- **`graded-stack-concept-node-status-convention` (for meta-phase unification).** I applied the
  three-rule convention above (narrative-pointer → non-node; methodology/layer-pattern →
  non-node; record-definition → node). The two borderline cases (`counter-update`,
  `chebyshev-iteration`) I resolved conservatively as **non-nodes**. D1/D3/D4/D5 are resolving
  the same question on disjoint page sets; meta-phase should unify the convention and reconcile
  any divergence — in particular the "sole-definition-site primitive page" sub-case
  (`counter-update`) which could legitimately flip to a node under a slightly different rule.
- **No `rank:` written for the 16 non-nodes — intentional.** Per scheme §2d and checklist
  item 4 ("a methodology / process / narrative-concept page carries **no** `rank:`/`edges:`"),
  the non-nodes get nothing on disk. If meta-phase later wants an explicit on-disk
  "deliberately-not-a-node" marker (e.g. a `dag_node: false` frontmatter or an HTML comment) to
  prove the typing pass *visited* each page, that is a scheme amendment to decide centrally —
  I did not invent one here (HARD-gate-new: only mark a node if it is one).
- **Build-safety.** The single edit prepends a YAML frontmatter block to a page that currently
  has none; mdBook + `linkcheck2` ignore frontmatter, and all `edges:` targets are either
  existing book chapters or raw-source `cites-evidence` strings (not link-checked). No link
  syntax is added to the body. Build-safe.
