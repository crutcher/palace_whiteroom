---
agent: layer-intro-author
invoked_at: 2026-06-05T09:00:00Z
scope: graded-stack typed-edge campaign P1 — add depends-on (kind: uses-record) edges from GC-root feature columns to the record-concept pages
status: pending
integrated_at: 2026-06-05T093000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-104 D2, applied clean (staging row 4/4, FINAL). 12 depends-on (kind: uses-record) edges (11 feature columns -> concepts/config-record + transient.L4 -> concepts/op-params) + 4 reciprocal reference back-refs in config-record.md. config-record + op-params become root-reachable (2 of 8 graded-stack records rescued; other 6 await WAVE-3 op-chapter edges). energy-fields.L4 deliberately NOT linked (no PostprocessConfig/DomainData concept pages, 0 danglers). Opened HIGH OQ solve-record-reachability-needs-op-chapter-uses-record-edges + MEDIUM OQ energy-fields-config-and-domaindata-records-need-concept-pages. NOTE: the linter's hand-rolled parse_frontmatter does not parse block-mapping edges, so the reachability rescue is correct on disk but does not show in the GC (pre-existing uniform parser gap, routed to meta/tools). rank_violations held 0; build EXIT 0."
---

# CYCLE: feature-column → record `uses-record` reachability edges

## Summary

Cycle-104 D2 (graded-stack typed-edge campaign P1, WAVE 2). The c103/c104 typing turned the
record-concept pages into typed firm DAG nodes, but they are **unreachable garbage** under the
reachability GC: the feature columns (the `feature_root: seed` root set) only `reference`-link
records (actually they don't link them at all yet), and `reference` edges carry no liveness. The
fix (per the c103 finding): add a **blocking `depends-on (kind: uses-record)` edge** from each
consuming feature column → the record pages it **genuinely names in its signature/composition**.

**Applying the precision constraint literally** ("only add the edge where the column genuinely uses
the record — a record named in the column's input/output/state signature; do NOT over-link"), I
surveyed every feature column's signature + composition body. The records each column **actually
names**:

- **`config-record`** — named in the **input signature of ALL 7 columns**. The lifecycle ROOT:
  `lifecycle :: Config -> Product` (`feature/lifecycle.L4.md:35`), with the input described as
  "`Config` (the `IoData` surface)" (`:52`). Each of the 6 driver columns names a per-driver config
  record specialization in its input signature — `ElectrostaticConfig` (`electrostatic.L4.md:34`),
  `MagnetostaticConfig` (`magnetostatic.L4.md:34`), `DrivenConfig` (`driven.L4.md:55`),
  `TransientConfig` (`transient.L4.md:32`), `EigenmodeConfig` (`eigenmode.L4.md:30`),
  `BoundaryModeConfig` (`boundary-mode.L4.md:32`) — each explicitly narrated as "the `IoData`
  surface / the config surface" (the data shape that `concepts/config-record` defines; `iodata` is
  named the config surface in every column's Input bullet). The per-driver `*Config` names are
  *specializations* of the `IoData`/`Config` shape `config-record` homes — exactly the consumer-set
  `config-record.md`'s OWN `reference` edges already enumerate (it back-references all 6 drivers +
  lifecycle). So the reciprocal blocking edge is precise on all 7.

- **`op-params`** — named in the **composition body of `transient.L4`**: `op : OpParams`
  (`feature/transient.L4.md:38`, the captured ODE-operator type annotation in the `let`-composition).
  This is the one driver column that surfaces `OpParams` in its OWN composition (the others capture
  the operator stratum inside the composed `ksp_solve`/`solve_family`/`fold_solve` ops, not in the
  column body). So `transient.L4 → concepts/op-params` is a precise, non-over-linked `uses-record`
  edge.

**Edges added (8 total):**

| column | `uses-record` → | basis (named-in-signature) |
|---|---|---|
| `feature/lifecycle.L4` | `concepts/config-record` | `lifecycle :: Config -> Product` (:35, :52) |
| `feature/electrostatic.L4` | `concepts/config-record` | `electrostatic :: ElectrostaticConfig -> …` (:34, :53) |
| `feature/magnetostatic.L4` | `concepts/config-record` | `magnetostatic :: MagnetostaticConfig -> …` (:34, :53) |
| `feature/driven.L4` | `concepts/config-record` | `driven :: DrivenConfig -> …` (:55) |
| `feature/transient.L4` | `concepts/config-record` | `transient :: TransientConfig -> …` (:32, :53) |
| `feature/transient.L4` | `concepts/op-params` | `op : OpParams` in composition body (:38) |
| `feature/eigenmode.L4` | `concepts/config-record` | `eigenmode :: EigenmodeConfig -> …` (:30, :50) |
| `feature/boundary-mode.L4` | `concepts/config-record` | `boundary_mode :: BoundaryModeConfig -> …` (:32) |

## Rank well-foundedness (each edge `depends-on u → v` requires `rank(u) ≤ rank(v)`)

| edge `u → v` | rank(u) | rank(v) | `rank(u) ≤ rank(v)` |
|---|---|---|---|
| lifecycle.L4 → config-record | firm (3) | firm (3) | ✓ 3 ≤ 3 |
| electrostatic.L4 → config-record | firm (3) | firm (3) | ✓ |
| magnetostatic.L4 → config-record | firm (3) | firm (3) | ✓ |
| driven.L4 → config-record | firm (3) | firm (3) | ✓ |
| transient.L4 → config-record | firm (3) | firm (3) | ✓ |
| transient.L4 → op-params | firm (3) | firm (3) | ✓ |
| eigenmode.L4 → config-record | firm (3) | firm (3) | ✓ |
| **boundary-mode.L4 → config-record** | **rough-in (2)** | firm (3) | ✓ **2 ≤ 3** |

All 8 edges are well-founded. Note `boundary-mode.L4` is `rank: rough-in` (2), not firm — a
rough-in consumer depending on a firm record is well-founded (the consumer is at most as resolved
as its dep; `2 ≤ 3` holds). Column ranks confirmed on-disk (`lifecycle/electrostatic/magnetostatic/
driven/transient/eigenmode` all `rank: firm`; `boundary-mode` `rank: rough-in`). The two record
targets are `rank: firm` per D1's report (`config-record` was c103-typed firm on-disk; `op-params`
is D1-typed `rank: firm`, applied serially before this dispatch).

## Reachability outcome (records now reachable from the root set)

The reachability GC marks from the `feature_root: seed` columns over `depends-on` edges (the linter
consumes only the `depends-on` bit; the `kind: uses-record` annotation is documentation it ignores —
scheme §2).

**Reachable after these edges (2 of 8 target records):**

- ✅ **`config-record`** — now `depends-on`-reachable from 11 columns: the 7 driver/lifecycle columns
  + (repairer addendum, cycle-104) the 4 output-product columns naming a `*Config` record
  (`capacitance`/`inductance`/`sparameters`/`eigenfrequency-qfactor`). The 5th output-product column
  `energy-fields.L4` names `PostprocessConfig` (no concept page yet) and is flagged-not-linked — see
  the `energy-fields-config-and-domaindata-records-need-concept-pages` OQ. (config-record was already
  reachable via the 7; the addendum applies the precision rule evenly across the full 12-column root
  set rather than expanding reachability.)
- ✅ **`op-params`** — now `depends-on`-reachable from `transient.L4` (root → op-params).

**NOT yet reachable from the column roots (6 of 8 — see Open questions; OUT of this dispatch's
precise scope):**

- ❌ `sim-state`, `krylov`, `step-outputs`, `prev-carry`, `solve-result` — and `op-params` on the
  non-transient columns — are **NOT named in any feature-column signature**. They are the internal
  record shapes of the L4 solve OPERATORS (`ksp_solve :: OpParams -> Inputs -> SimState`
  (`L4/ksp_solve.md:39`); `krylov-step :: OpParams -> Krylov -> (SimState -> Solve { sim, krylov,
  outputs })` (`L4/krylov-step.md:25,31-32`); `solve_family :: OpParams -> [Inputs] -> [SimState]`
  (`L4/solve_family.md:40`); `fold_solve :: OpParams -> TimeState -> [Time] -> TimeState`
  (`L4/fold_solve.md:41`, `op : OpParams` at `:61,69`)). The columns reach these ops via their
  EXISTING `depends-on (kind: composes)` edges (`→ L4/ksp_solve`, `→ L4/solve_family`,
  `→ L4/fold_solve`, etc.), so the **correct reachability path is `column → op → record`** — the
  `uses-record` edge belongs on the OP chapter, NOT the column. Adding a `column → sim-state`
  (etc.) edge would be exactly the over-linking the directive forbids (no column names these
  records in its own signature).

- ❌ `dofset` — `DofSet[N]` is named by `L4/eliminate_bc` (`:8,26,36`) and `L1/essential_dofs`, NOT
  by any feature column (zero hits for `DofSet`/`dofset`/`essential`/`eliminate` across all
  `feature/*.md`). Its reachability path is `column → (depends-on composes) fe_assemble →
  eliminate_bc → dofset` — again an OP-chapter `uses-record` edge, not a column edge.

**So this dispatch makes 2 of the 8 records root-reachable; the other 6 require the L4 solve/BC
OP chapters to carry their own `uses-record` edges.** Those op chapters (`ksp_solve`,
`krylov-step`, `solve_family`, `fold_solve`, `eliminate_bc`) still carry the OLD
`consumes:`/`lowers_to:` frontmatter and have NOT been migrated to typed `edges:` — typing them is
a distinct P1 frontmatter-migration task (op-chapter edges), explicitly outside this dispatch's
feature-column scope. I route it as a precise OQ below so the campaign closes the gap rather than
leaving the records garbage; doing it HERE would mean either (a) over-linking the columns with
records they don't name (the forbidden anti-pattern) or (b) editing op chapters out of this
dispatch's scope. The principled move is the precise column edges + the routed OQ.

## Proposed changes

Each block inserts ONE `uses-record` `depends-on` entry into a column's existing `depends-on:`
list, immediately after its last `cites-evidence` entry and before the `reference:` key. Pure
insertions; no body change.

```edit:book/src/feature/lifecycle.L4.md
[old]:
    - target: palace/drivers/basesolver.cpp:153-276
      kind: cites-evidence
  reference:
[new]:
    - target: palace/drivers/basesolver.cpp:153-276
      kind: cites-evidence
    - target: concepts/config-record
      kind: uses-record               # input signature: lifecycle :: Config -> Product (the IoData surface)
  reference:
```

```edit:book/src/feature/electrostatic.L4.md
[old]:
    - target: palace/drivers/electrostaticsolver.cpp:21-98
      kind: cites-evidence
  reference:
[new]:
    - target: palace/drivers/electrostaticsolver.cpp:21-98
      kind: cites-evidence
    - target: concepts/config-record
      kind: uses-record               # input signature: electrostatic :: ElectrostaticConfig -> CapacitanceMatrix (the IoData surface)
  reference:
```

```edit:book/src/feature/magnetostatic.L4.md
[old]:
    - target: palace/drivers/magnetostaticsolver.cpp:22-108
      kind: cites-evidence
  reference:
[new]:
    - target: palace/drivers/magnetostaticsolver.cpp:22-108
      kind: cites-evidence
    - target: concepts/config-record
      kind: uses-record               # input signature: magnetostatic :: MagnetostaticConfig -> InductanceMatrix (the IoData surface)
  reference:
```

```edit:book/src/feature/driven.L4.md
[old]:
    - target: palace/drivers/drivensolver.cpp:77-229
      kind: cites-evidence
  reference:
[new]:
    - target: palace/drivers/drivensolver.cpp:77-229
      kind: cites-evidence
    - target: concepts/config-record
      kind: uses-record               # input signature: driven :: DrivenConfig -> FrequencyResponse (the IoData surface)
  reference:
```

```edit:book/src/feature/transient.L4.md
[old]:
    - target: palace/models/timeoperator.cpp:407-413
      kind: cites-evidence
  reference:
[new]:
    - target: palace/models/timeoperator.cpp:407-413
      kind: cites-evidence
    - target: concepts/config-record
      kind: uses-record               # input signature: transient :: TransientConfig -> FieldTrajectory (the IoData surface)
    - target: concepts/op-params
      kind: uses-record               # composition body: op : OpParams (the captured ODE operator, feature/transient.L4.md:38)
  reference:
```

```edit:book/src/feature/eigenmode.L4.md
[old]:
    - target: palace/drivers/eigensolver.cpp:32-477
      kind: cites-evidence
  reference:
[new]:
    - target: palace/drivers/eigensolver.cpp:32-477
      kind: cites-evidence
    - target: concepts/config-record
      kind: uses-record               # input signature: eigenmode :: EigenmodeConfig -> EigenmodeResult (the IoData surface)
  reference:
```

```edit:book/src/feature/boundary-mode.L4.md
[old]:
    - target: palace/main.cpp:276-278
      kind: cites-evidence
  reference:
[new]:
    - target: palace/main.cpp:276-278
      kind: cites-evidence
    - target: concepts/config-record
      kind: uses-record               # input signature: boundary_mode :: BoundaryModeConfig -> BoundaryModeResult (the IoData surface)
  reference:
```

### Repairer addendum (cycle-104 repair) — output-product columns naming a `*Config` record

The four output-product feature columns that NAME a config-record specialization in their input
signature get the analogous `uses-record → concepts/config-record` edge, applying the same precision
rule evenly across the 12-column root set (the critic's variant-axis + surface-or-evidence warning).
Each is `rank: firm`; `config-record` is `rank: firm` → `3 ≤ 3` well-founded. The fifth output-product
column (`energy-fields.L4`) names `PostprocessConfig` (and a `DomainData` result), neither of which has
a `concepts/` record page on-disk — so per the no-dangling-edge rule it is NOT linked here; it is
flagged as a record-page-needed follow-up (see Open questions).

```edit:book/src/feature/capacitance.L4.md
[old]:
    - target: palace/drivers/electrostaticsolver.cpp:100-140
      kind: cites-evidence
  reference:
[new]:
    - target: palace/drivers/electrostaticsolver.cpp:100-140
      kind: cites-evidence
    - target: concepts/config-record
      kind: uses-record               # input signature: capacitance :: ElectrostaticConfig -> CapacitanceMatrix (the IoData surface)
  reference:
```

```edit:book/src/feature/inductance.L4.md
[old]:
    - target: palace/drivers/magnetostaticsolver.cpp:110-152
      kind: cites-evidence
  reference:
[new]:
    - target: palace/drivers/magnetostaticsolver.cpp:110-152
      kind: cites-evidence
    - target: concepts/config-record
      kind: uses-record               # input signature: inductance :: MagnetostaticConfig -> InductanceMatrix (the IoData surface)
  reference:
```

```edit:book/src/feature/sparameters.L4.md
[old]:
    - target: palace/models/waveportoperator.cpp:780-793
      kind: cites-evidence
  reference:
[new]:
    - target: palace/models/waveportoperator.cpp:780-793
      kind: cites-evidence
    - target: concepts/config-record
      kind: uses-record               # input signature: sparameters :: DrivenConfig -> ScatteringMatrix (the IoData surface)
  reference:
```

```edit:book/src/feature/eigenfrequency-qfactor.L4.md
[old]:
    - target: palace/models/postoperator.cpp:1171-1203
      kind: cites-evidence
  reference:
[new]:
    - target: palace/models/postoperator.cpp:1171-1203
      kind: cites-evidence
    - target: concepts/config-record
      kind: uses-record               # input signature: eigenfrequency_qfactor :: EigenmodeConfig -> [(Scalar, Scalar)] (the IoData surface)
  reference:
```

The reciprocal half — `concepts/config-record.md`'s `reference:` back-list — should also gain the four
output-product columns so the navigational pairing is complete (it currently lists only the 7
driver/lifecycle columns):

```edit:book/src/concepts/config-record.md
[old]:
    - feature/eigenmode.L4
    - feature/boundary-mode.L4
[new]:
    - feature/eigenmode.L4
    - feature/boundary-mode.L4
    - feature/capacitance.L4
    - feature/inductance.L4
    - feature/sparameters.L4
    - feature/eigenfrequency-qfactor.L4
```

## Supporting evidence

- **Column signatures naming a config record (the precise `uses-record` basis):**
  `feature/lifecycle.L4.md:35` (`lifecycle :: Config -> Product`) + `:52` ("`Config` (the `IoData`
  surface)"); `feature/electrostatic.L4.md:34` + `:53` ("`ElectrostaticConfig`"… "`iodata` is the
  config surface"); `feature/magnetostatic.L4.md:34` + `:53`; `feature/driven.L4.md:55`;
  `feature/transient.L4.md:32` + `:53`; `feature/eigenmode.L4.md:30` + `:50`;
  `feature/boundary-mode.L4.md:32`.
- **`transient.L4 → op-params` basis:** `feature/transient.L4.md:38`
  (`op = time_operator (k,c,m) (dJdt cfg)  -- the captured ODE operator (readonly; op : OpParams)`).
- **The reciprocal already-present half:** `concepts/config-record.md` frontmatter `reference:`
  already lists `feature/lifecycle.L4` + all 6 driver columns — so these `uses-record` `depends-on`
  edges are the *blocking-direction* completion of an existing navigational pairing (the column
  USES the record; the record back-references its consumers). The record does not block on its
  consumers (it is named-by-use); the columns block on the record shape they rest on.
- **Records the columns do NOT name (why no column edge):** zero hits for
  `SimState`/`Krylov`/`StepOutputs`/`PrevCarry`/`solve-result`/`DofSet` in any `feature/*.L4.md`
  signature or composition (only `feature/transient.L4.md:38` surfaces `OpParams`). The L4 solve ops name them:
  `L4/ksp_solve.md:39`, `L4/krylov-step.md:25,31-32`, `L4/solve_family.md:40,58,60`,
  `L4/fold_solve.md:41,61,69`; `L4/eliminate_bc.md:8,26,36` names `DofSet[N]`.
- **Edge targets all exist on-disk:** `concepts/config-record.md` ✓, `concepts/op-params.md` ✓
  (the 8 record pages all present). No dangling edges.
- **Linter semantics confirmed** (`tools/graded-stack-lint/graded_stack_lint.py`): reachability GC
  marks from `feature_root: seed` nodes over `depends-on` edges (lines 15-17, 441-446); consumes
  ONLY the blocking bit (line 20); `kind:` annotation is ignored documentation (scheme §2). The
  feature columns are confirmed roots (they carry `feature_root: seed` + `kind: feature-surface`).

## Open questions / caveats

- **`solve-record-reachability-needs-op-chapter-uses-record-edges` (HIGH for the campaign; routes
  the remaining 6 records out of garbage).** Five solve-internal records (`sim-state`, `krylov`,
  `step-outputs`, `prev-carry`, `solve-result`) + `op-params` (on the non-transient columns) + the
  BC record `dofset` are NOT named in any feature-column signature, so per the no-over-linking
  precision rule they get **no column edge** from this dispatch and remain reachability-GC garbage
  until the L4 solve/BC OP chapters that DO name them carry typed `uses-record` `depends-on` edges:
  - `L4/ksp_solve` → `op-params`, `sim-state` (`:39`).
  - `L4/krylov-step` → `op-params`, `krylov`, `sim-state`, `step-outputs`, `prev-carry`,
    `solve-result` (`:25,31-32`). (`krylov-step` has NO frontmatter at all today — needs an
    `edges:` block from scratch.)
  - `L4/solve_family` → `op-params`, `sim-state` (`:40,58,60`).
  - `L4/fold_solve` → `op-params` (`:41,61,69`).
  - `L4/eliminate_bc` → `dofset` (`:8,26,36`); and the `fe_assemble`→`eliminate_bc` reach.

  These op chapters still carry the pre-scheme `consumes:`/`lowers_to:` frontmatter — typing them is
  a distinct P1 frontmatter-migration sub-task (the op-chapter half of the `uses-record` wiring),
  separate from this feature-column dispatch. **Recommend a WAVE-3 dispatch** (harvester or
  layer-intro-author over the L4 solve-op chapters) to migrate their frontmatter to typed `edges:`
  AND add the `uses-record` edges above — at which point all 8 records become reachable
  (`column →(composes) op →(uses-record) record`). Flagging rather than doing here because (a) the
  columns genuinely do not name these records (a column edge would over-link, the directive's
  forbidden anti-pattern) and (b) the op chapters are out of this dispatch's scope.

- **`energy-fields-config-and-domaindata-records-need-concept-pages` (medium; repairer-routed,
  cycle-104 repair).** The fifth output-product column `energy-fields.L4` names `PostprocessConfig`
  in its input signature (`feature/energy-fields.L4.md:51`, `:117`) and `DomainData` as its result
  element. Neither has a `concepts/` record-definition page on-disk (`config-record.md` is the only
  config page; there is no `concepts/postprocess-config.md`), so per the no-dangling-edge rule the
  repairer did NOT add a `uses-record` edge from `energy-fields.L4` to a missing target — that would
  be a `linkcheck2`/reachability dangler. `PostprocessConfig` is plausibly a specialization of the
  same `IoData`/`config-record` shape (like the per-driver `*Config` records), but the repairer does
  not author that determination — wiring `energy-fields → config-record` requires a content judgment
  (is `PostprocessConfig` the same record shape, or a distinct post-processing config record needing
  its own page?) that exceeds mechanical repair authority. `DomainData` already carries the OQ
  `record-DomainData-needs-definition-home` (energy-fields.L4 §Record-definition). **Routes to:** a
  layer-intro-author pass to (a) decide whether `PostprocessConfig` folds into `config-record` or
  gets its own `concepts/postprocess-config.md` page, then (b) add the analogous `uses-record` edge
  from `energy-fields.L4`. Until then `energy-fields.L4` is the one output-product column without a
  config-record edge — flagged-not-linked, deliberately.

- **`feature-record-mention-via-l0-not-signature` (low; no action).** Three driver L0 columns
  (`electrostatic.L0`, `magnetostatic.L0`, `driven.L0`) mention "Krylov" in PROSE (the L0
  ground-truth narration of the iterative solve), and `transient.L0`/`transient.L4` mention
  `OpParams`. These are not *signature* uses — the L0 columns describe the C++ solver call site, not
  an L4 record-typed signature. I did NOT add `uses-record` edges from the L0 columns (the L4
  record concept pages define an L4 data shape; the L0 column's Krylov mention is a prose pointer to
  the solver family, not a typed signature dependency). Consistent with the precision rule. The L1
  columns are the natural place a future pass might surface record-shaped signatures if the L1
  feature surfaces ever name the L1 record forms — none do today.

- **Build-safety.** All 8 edge targets are `concepts/<slug>` repo-relative slugs resolving to
  existing `book/src/concepts/*.md` files; the edges live in YAML frontmatter (not mdBook link
  syntax), so `linkcheck2` is not involved and the inserts cannot break the build. Pure frontmatter
  insertions, no body or `SUMMARY.md` change.

- **Linter-noise caveat (acknowledged from the dispatch prompt).** `is_likely_outside_dag` +
  uses-record-kind recognition are meta-phase/tools-owned; the finalize linter may still show
  residual noise after these edges. My scope is the EDGES (the `depends-on` blocking bit the GC
  consumes), not the linter tuning — the 2 newly-reachable records (`config-record`, `op-params`)
  will mark live from the roots regardless of `kind:`-annotation handling.
