---
agent: meta-phase
invoked_at: 2026-06-07T035336Z
scope: OUT-OF-BAND rescope-directive-enactment meta-phase (post-batch-38; answers the batch-38 plateau ASK)
status: pending
---

# REPORT: Out-of-band rescope meta-phase (2026-06-07 three-directive RE-SCOPE)

This is an **OUT-OF-BAND, directive-enactment meta-phase** — not a batch-aggregating one (the scheduled batch-38 meta already fired at `73b225e`). It enacts the user's 2026-06-07 three-directive RE-SCOPE, which answers the batch-38 (third-consecutive) plateau ASK and ENDS the plateau. Same pattern as the 2026-06-06 out-of-band meta-phase.

## The re-scope (as enacted)

The plateau was an artifact of three now-LIFTED postures. The vocabulary-shift redirect + graded-stack machinery (HOW vocabulary is expressed) is UNCHANGED; the re-scope governs WHAT is now the forward frontier.

- **DIRECTIVE 1 — MPI/sharding = DEFERRED future direction, NOT active work.** The MPI-associated version (`linalg/rap.{hpp,cpp}`, `utils/geodata.cpp` distribution, the MPI collectives) may be DESTRUCTIVE to the spine → do NOT lift now. Sharding-into-component-blocks is a recorded `roadmap_goal` future direction; the sharding-MATH-as-decomposition-abstraction is exploratory-only-if-non-destabilizing behind a hard gate. Single-machine-valid grounded consumers (geometric-multigrid, AMR) ARE in active scope.
- **DIRECTIVE 2 — the existing deferred IN-SCOPE work is LIFTED THROUGH** (LIFTS STOP-PROPOSING for the in-scope set). Build the grounded consumers and discharge RE1-RE10: the geometric-multigrid preconditioner (highest fan-out; discharges RE9/RE1/RE5/RE7), AMR, deflate/NLEPS (RE3), the L3 iteration-views (RE2/RE8), the axpy-arity-leaves (RE6). The RE set is now a discharge target, not a permanent floor.
- **DIRECTIVE 3 — spine-dependency opaque-library kernels get a CONSTRUCTIVE IMPL, preserving the kernel-API/impl distinction.** Revises "document obstructions, don't fill them" FOR spine-dependency opaque-library kernels (libCEED quadrature, triangular-solve/GS-SSOR relaxation, SLEPc eigsolve); the enum-only-stub carve-out (MINRES/BiCGStab) is preserved unchanged.

## Design decision (kernel-API/impl mechanics — sensible-default, refine-from-use)

The directive left the structural representation to me with a "make a sensible default, record it as decision-to-be-refined" instruction. **Decision:** EXTEND the existing black-box-kernel disposition rather than introduce a new top-level Part or new linter edge-semantics (minimal blast radius). A spine-dependency opaque-library kernel with a well-understood in-our-semantics impl gets TWO linked chapters:
- **(a) kernel-API surface** = the EXISTING obstruction theme, repositioned as "the API." Keeps `status: obstruction (opaque-library-ownership)` (it genuinely IS the opaque contract); `## Status` line gains the role-label `kernel-api`. Claim-free; KEPT (not downgraded/deleted).
- **(b) kernel-implementation** = a NEW constructive chapter at the appropriate L-layer (normal `rank`/`status`; role-label `kernel-impl`; ordinary `depends-on` edges to its from-our-primitives constituents).
- **The reviewable link** = a `realizes-kernel-api` edge (impl → API) of edge-class **`reference`** (navigational/free — the impl does NOT `depends-on` the opaque API; the relationship is a *correspondence to review*, not a build dependency, so it constrains neither rank nor liveness). The linters ignore the label via the existing optional-`kind:`-is-documentation mechanism → **NO new linter machinery required**. `lowering-verifier` audits the impl-realizes-API correspondence.

Rationale for the sensible-default over alternatives: a new chapter-Kind or new `kind:` edge-class would force a SUMMARY reorg + a linter change (a `tools/`-code ask) for a relationship the reviewer reads by following one link; the `reference`-class correspondence link captures "these two surfaces describe the same kernel, check they match" without adding rank/liveness machinery the relationship doesn't need. If use shows the distinction is hard to navigate (e.g. reviewers want a dedicated kernel-pair grouping), that is the refine-from-use signal.

## No ASK / no unreconcilable conflict

I checked the directives against the load-bearing invariants. **No conflict requiring an ASK:** DIRECTIVE 3 *revises* the obstruction policy for a precisely-bounded sub-kind (spine-dependency opaque-library kernels) while preserving the enum-only-stub carve-out verbatim, so `project_unimplemented_palace_components` is intact for what it actually governs; DIRECTIVE 2 *fires* the in-scope feature/consumer demand-gate while the redirect's no-forced-rectangular-VOCABULARY-pull-up still governs vocabulary picks (the two are about different things — features/consumers vs vocabulary floors); DIRECTIVE 1 *refines* "MPI out of scope, flag once" into a deferred-future-direction-with-a-gate without contradicting the single-machine scope. The graded-stack rank/reachability invariants are unchanged — the RE discharge happens by FAITHFUL inbound `depends-on` edges (a fired promotion condition is exactly a real consumer composing the node by name), which is the §2f GROUND disposition, not a forced edge.

## Plans proposed and judged → all GO (8 enactments, 0 no-go, 0 ask)

| # | kind | target | cascade | judgment |
|---|---|---|---|---|
| 1 | invariant + scope | CLAUDE.md §Scope (3 directives) + NEW §Methodology-invariant (kernel-API/impl) | Medium | GO |
| 2 | prompt edit ×6 | cycle-planner / harvester / abstractor / combinator-miner / lowering-verifier / layer-intro-author / meta-phase | Medium | GO |
| 3 | memory | 4 new + 2 updated + MEMORY.md pointers | Low | GO |
| 4 | priority update | priorities.md → CYCLE-121/batch-39 lift-through campaign (5 items) | Medium | GO |
| 5 | methodology mirror | goal-flow.md batch-39 arc + kernel-API/impl section + scope line | Low | GO |
| 6 | friction-ledger | NEW plateau-as-scope-boundary-not-project-boundary (recurrence-3, addressed) | Low | GO |
| 7 | OQ migration | banner migrating now-activated deferred families to the plan | Low | GO |
| 8 | session bookkeeping | cycle-121-resume-notes (SUPERSEDES batch-38 "no restart") + cycle-record append | Low | GO |

(7 role-spec edits counted under #2 — the 6 producers/planner/verifier plus meta-phase.)

## Trends recorded

- `plateau-as-scope-boundary-not-project-boundary` (NEW, friction-ledger) — recurrence-3 (meta-36/37/38), status `addressed` by the out-of-band re-scope. The lesson: a confirmed-three-times plateau is correctly surfaced as an ASK (the meta-phase did NOT manufacture a forced rectangular pull-up); the disciplined recognition of the clean-gate floor is what let the human re-scope deliberately.

## Decisions

### go (enacted this cycle)
All 8 plans above enacted. Files listed below.

### no-go (declined)
None.

### ask (surfaced to human)
None. The kernel-API/impl mechanics ambiguity was resolved with a sensible-default decision (recorded above as refine-from-use), per the directive's instruction.

## Enacted changes summary

- `CLAUDE.md` — §Scope rewritten (3 directives); NEW §Methodology-invariant "Kernel-API vs kernel-IMPLEMENTATION distinction".
- `.claude/agents/cycle-planner.md` — NEW 2026-06-07-RESCOPE banner (lift-through frontier; geometric-multigrid LEAD; STOP-PROPOSING lifted; MPI out).
- `.claude/agents/harvester.md` — NEW banner (kernel-API/impl + lift-through-deferred).
- `.claude/agents/abstractor.md` — NEW banner (kernel-API/impl supersedes obstruction-no-constructive-form for spine-dependency kernels; carve-out preserved).
- `.claude/agents/combinator-miner.md` — NEW banner (kernel-impl shared-substrate mining + lift-through).
- `.claude/agents/lowering-verifier.md` — NEW banner (audit impl-realizes-API correspondence + reference-class check).
- `.claude/agents/layer-intro-author.md` — NEW banner (kernel-API/impl chapter-kind mechanics + geometric-multigrid feature-surface column).
- `.claude/agents/meta-phase.md` — NEW §Standing-book-targets duty (kernel-API/impl integrity + lift-through RE-discharge tracking + DIRECTIVE-1 MPI-boundary guard).
- 4 NEW memories (`project_rescope_2026_06_07`, `project_sharding_mpi_deferred`, `project_lift_through_deferred_in_scope`, `project_kernel_api_impl_distinction`) + 2 updated (`project_blackbox_vs_accelerated_kernels`, `project_unimplemented_palace_components`) + MEMORY.md pointers.
- `scaffolding/priorities.md` — active head reshaped into the CYCLE-121/batch-39 lift-through campaign (5 fan-out-ranked items).
- `scaffolding/friction-ledger.md` — NEW plateau pattern.
- `scaffolding/open-questions.md` — banner migrating now-activated deferred families to the plan (OQ unification: closed 0 / migrated 6 family-cohorts / kept-deferred 1 = MPI/sharding).
- `book/src/methodology/goal-flow.md` — batch-39 re-scope arc + kernel-API/impl methodology section + scope line; `cargo make book` EXIT 0.
- `scaffolding/cycle-121-resume-notes.md` — SUPERSEDES the batch-38 "no restart" note; restart REQUIRED.
- `scaffolding/cycle-record.jsonl` — out-of-band rescope meta-phase record appended.

## Reshaped plan summary (CYCLE-121 / batch-39 — lift-through campaign)

1. **`geometric-multigrid-preconditioner`** (THE LEAD, HIGH — discharges RE1/RE5/RE7/RE9 by composing the level-stack + smoother + diagonal-preconditioner chains by name).
2. **`constructive-spine-kernels`** (PARALLEL HIGH — libCEED quadrature / triangular-solve+GS-SSOR relaxation / SLEPc eigsolve, each with the kernel-API/impl distinction).
3. **`amr-estimate-mark-refine`** (HIGH-MEDIUM — Palace-authored estimate→mark→refine + ZZ flux-recovery estimators, single-machine).
4. **`re-discharge-tail`** (MEDIUM — deflate/NLEPS RE3; the krylov-iteration feature column RE2/RE8; the axpy-arity-leaves RE6; consumer-gated on 1-2).
5. **`cheap-openers`** (LOW — RE10 interpolator-ground + waveguide-mode drift cleanup; carried from batch-38).

Items 1-3 are a wide wave sharing the mesh→fe_space→smoother→Krylov substrate (lift the shared cores once). MPI/sharding stays OUT of active scope (DIRECTIVE-1 standing gate).

## Decision counts

go: 8 · no-go: 0 · ask: 0. Ledger updates: 1. Skill promotions: 0. Skill retirements: 0. OQ unification: closed 0 / migrated 6 / kept-deferred 1.

## Restart note

**SESSION RESTART REQUIRED before cycle-121** (CLAUDE.md + 7 `.claude/agents/*` edits). `scaffolding/cycle-121-resume-notes.md` documents the restart-triggering edits and SUPERSEDES the batch-38 meta's stale "no restart" note. No `/compact` step (the restart resets primary context).

## Cycle-record append

The `kind: meta-phase-out-of-band-rescope` row appended to `scaffolding/cycle-record.jsonl` (cycle_id `cycle-120` as the off-schedule anchor; go=8, no-go=0, ask=0; session_restart_required=true).
