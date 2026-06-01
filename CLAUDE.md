# CLAUDE.md

Operational guide for Claude Code working in this repository. The project is a multi-agent pipeline that dissects AWS Labs **Palace** (C++ electromagnetic simulator) into a **layered, citation-grounded specification** organized as an incremental impedance-matching stack L4→L0.

This file replaces the original CLAUDE.md (slice-vertical era, cycles 1–172) after the **structural redirect of 2026-05-26**. The redirect is fully specified in `MIGRATION.md`; this CLAUDE.md is its operational distillation. The previous `BOOTSTRAP.md` is superseded and kept only as historical record.

## Repository status

- **Current flow**: 6-phase agent cycle (plan → dispatch → critique → repair → integrate → meta). See *Cycle structure* below and `MIGRATION.md` §2.
- **Artifact in progress**: layered specification under `book/src/L4/`–`book/src/L0/` + 4 lowering Parts. The Phase 1 slice corpus under `book/src/spec/slices/` is raw material for the layered artifact (not the deliverable) — slices reduce to stubs and eventually delete as their material is lifted into firm layered entries (user directive 2026-05-27, mid-cycle-009; see §Methodology invariants "Phase 1 corpus reduces as material is lifted").
- **First pilot cycle landed**: `pilot-1` (commit `a058f07`) — `axpy` at L1 via the new flow. See `log/pilot-1.md` and `reports/2026-05-26T223039Z-harvester-axpy-L1/`.
- **Decommissioned**: the Python orchestrator under `orchestrator/` (kept as historical reference). The 6 prompted roles (Planner/Explorer/Synthesizer/Critic + Meta-Critic + README Builder) are replaced by 13 Claude Code subagents under `.claude/agents/`.

## What this system is

A multi-agent pipeline that lifts traditional C/Fortran tensor-field simulators — which evolve fields by array iteration with in-place mutation — into a **citation-grounded, incrementally-layered series of representations**, where each layer re-expresses the layer below in a representation that has rotated one specific impedance, and the rotation is explicitly stated and verified.

**No port is produced.** The output is a layered specification; a separate downstream effort uses it to incrementally build burn components.

The methodology was developed in the user's **bunsen** project (see `reference/bunsen/crates/bunsen/src/kits/sims/` for the working Rust+burn realization at L3). Palace is a substantial test case.

## Extraction goal — what the spec is for

The artifact is an **incremental stack of representations** L4→L0:

- **L0** — cited Palace/MFEM source ranges. Ground truth.
- **L1** — *mutation rotation*. Source operations re-expressed as pure functions.
- **L2** — *fusion rotation*. L1 unfolded back into composition of base algebraic primitives, HPC tricks erased.
- **L3** — *iteration rotation*. Where possible, global tensor-field operations; otherwise record the obstruction.
- **L4** — small, formally-defined graph-evaluation calculus. **Vocabulary, not architecture.** High-order combinators + state monads + immutable tensors.

Between adjacent layers, **lowering layers** `L_{n+1}>L_n` describe the rewrite themes that take an L_{n+1} form into its L_n form. Lowerings are batched by themes (e.g. "in-place mutation under monad threading", "loop-recurrence → tensor-field op"), not point-wise edges.

**Each layer is its own mdBook Part** with multiple chapters: one for the Part overview (`index.md`), one per operator (for L_n) or theme (for L_{n+1}>L_n). The Part shape is load-bearing — it prevents per-layer content from accumulating into one giant file and preserves cross-referencing.

## Cycle structure: primary cycle (5 phases) + meta-phase every 3rd

There are **two cadences**:

- **Primary cycle (5 phases)**: plan → dispatch → critique → repair → integrate. Fires every cycle. The forward-frontier loop.
- **Meta-phase**: fires **every 3rd primary cycle** (user directive 2026-05-27, post-cycle-006 meta). Examines evidence aggregated across the **last 3 primary cycles** and adjusts methodology.

```
  Primary cycle (×3 between meta-phases):
    cycle-planner → N specialized agents → N critics → N repairers →
      integrator-per-report ×N → integrator-finalize
      (serial)        (scatter; parallel)     (scatter)    (scatter)
                                                                (serial; one-at-a-time)  (serial)

  Every 3rd primary cycle, after integrator-finalize:
    meta-phase (serial; aggregates evidence across the 3-cycle batch)
```

**Cycle counter** keeps incrementing across batches: cycles 007, 008, 009 form one meta-batch; meta-phase fires after 009; then 010, 011, 012 form the next batch; meta-phase after 012; and so on. The cycle counter does NOT reset at meta-batch boundaries.

**Phase 1 — plan**: `cycle-planner` reads roadmap, priorities, friction-ledger, open-questions, recent integrator batches, integrator-signals tail. Emits a dispatch plan with `(agent, scope, deps)` tuples and an overlap analysis. Does not mutate the artifact.

**Phase 2 — dispatch**: up to 12 specialized agents per plan (user directive 2026-05-27 — raised from 8 mid-cycle-006 after first split-integrator cycle (005) ran 6 wave-mates with no token-budget pressure), parallel where non-overlapping. Each writes a single `CYCLE.md` under `reports/<timestamp>-<agent>-<scope>/`. No artifact mutation in this phase.

**Phase 3 — critique**: `critic` agent runs on each report (parallel). Runs the 8-check checklist (citation-validity, surface-or-evidence, rotation-quality, variant-axis-coverage, cross-reference-integrity, edge-label-fidelity, plan-kind-consistency, skill-uptake-survey). Writes META.md critique section.

**Phase 4 — repair**: `repairer` agent runs on reports with warning/fail findings (parallel). Mechanical and surgical fixes only — not substantive authoring. Writes META.md repair section. Sets `overall_status`.

**Phase 5 — integrate** (split cycle-004 → cycle-005 boundary for context-bound per-dispatch budget):
- `integrator-per-report` runs **once per ready report, dispatched serially** (not parallel — artifact writes naturally serialize). Each per-report dispatch applies ONE report's proposed-changes, runs per-report safety-net gates, promotes that report's Open questions, and appends a row to a per-cycle staging log (`reports/<cycle-id>-integrator-staging/STAGING.md`). Does NOT rebuild book, does NOT commit.
- `integrator-finalize` runs **once at the end**. Reads the staging log, runs `cargo make book`, repairs build breakage, updates roadmap (when measurable), appends to `cycle-record.jsonl`, writes `log/cycle-N.md`, prepends to `log/README.md`, appends to `scaffolding/integrator-signals.md`, marks consumed reports' `integrated_at`, emits the batch CYCLE.md, runs single `git commit && git push origin main`.

Sole writers of `book/`, `scaffolding/roadmap.md`, `log/`, `scaffolding/cycle-record.jsonl`, `scaffolding/open-questions.md`, `scaffolding/integrator-signals.md` — partitioned per role spec (per-report writes artifact + open-questions + staging; finalize writes roadmap, cycle-record, log, integrator-signals, plus commit).

**Meta-phase (fires after every 3rd primary cycle)**: `meta-phase` examines evidence **aggregated across the last 3 primary cycles** + running history. Records escalating trends in `scaffolding/friction-ledger.md`. Proposes plans, judges them, decides `go` / `no-go` / `ask` per plan. Enacts `go` items directly: writes to `.claude/agents/`, `skills/`, `scaffolding/priorities.md`. Surfaces `ask` items to human. Separate commit from integrator-finalize. The aggregated-batch view is intentional — single-cycle noise washes out; persistent 2-of-3-cycle patterns surface as real friction.

## The 14 agents

Definitions live under `.claude/agents/`. Dispatch via `Agent(subagent_type=<name>, ...)`. Per-dispatch report file convention is `CYCLE.md` (renamed from `REPORT.md` cycle-004 to bypass the Claude Code subagent Write filter on `report|summary|findings|analysis` keywords).

**Pre-dispatch (1):**
- `cycle-planner` (opus) — serial dispatch planner.

**Specialized dispatch (8, all opus):**
- `layer-intro-author` — writes L_n / L_{n+1}>L_n Part overviews + dep-maps + `book/src/concepts/<slug>.md` pages (broadened cycle-003).
- `harvester` — formalizes one L_n operator per invocation.
- `abstractor` — sketches one L_{n+1}>L_n theme + speculative L_{n+1} operators.
- `lifter` — re-anchors a theme to firmed-up vocabulary.
- `lowering-verifier` — audits one theme against evidence.
- `combinator-miner` — finds one recurrent pattern, proposes a combinator.
- `same-layer-cross-cutter` — one unification/redundancy/contradiction observation.
- `cross-layer-cross-cutter` — one cross-layer coverage-gap/edge-mismatch observation.

**Post-dispatch validation (2):**
- `critic` — runs 8-check checklist per report; META.md critique section.
- `repairer` — attempts mechanical fixes per finding; META.md repair section + CYCLE.md in-place edits; sets `overall_status`.

**Application (2 — split cycle-004 → cycle-005):**
- `integrator-per-report` — applies ONE report; appends row to STAGING.md; dispatched serially once per ready report.
- `integrator-finalize` — runs ONCE at cycle-end; rebuild book + commit + push + cycle-end housekeeping (cycle-record, log, integrator-signals, roadmap, batch CYCLE.md).
- (RETIRED) `integrator` — single-pass version; kept as historical reference.

**Methodology (1):**
- `meta-phase` — examines cycle evidence; records trends; proposes / judges / decides; enacts methodology adjustments.

## Layout

```
book/src/                  # the mdBook artifact
  L4/                      # Part: graph-evaluation calculus
    index.md               (overview + dep-map)
    <operator>.md          (one chapter per operator)
  L4-L3/                   # Part: L4>L3 lowering
    index.md
    <theme>.md
  L3/, L3-L2/, ..., L0/    # one Part per layer + lowering layer
  spec/                    # Phase 1 corpus (slice-vertical, frozen)
  concepts/                # shared concept library (kept)
  design/                  # L4 calculus strawman (seeds L4 layer)
  meta-reviews/            # historical meta-review records (cycles 1–172)
.claude/agents/            # 13 agent definitions
reports/                   # per-invocation CYCLE.md + META.md channel
  <timestamp>-<agent>-<scope>/
    CYCLE.md
    META.md                (post-critique + repair)
    [supporting docs]
scaffolding/               # cumulative cross-cycle state (the workshop)
  roadmap.md               (relative-progress vs goals; integrator-maintained)
  priorities.md            (next-up list; meta-phase + cycle-planner co-edit)
  friction-ledger.md       (named friction patterns + recurrence; meta-phase-maintained)
  skill-candidates.md      (skill proposals; any-agent appendable)
  open-questions.md        (cross-cycle question ledger; any-agent appendable)
  cycle-record.jsonl       (per-cycle structured record; integrator + meta-phase append)
  problems-sensitivity.md  (problems/ filing-rate self-tuning; meta-phase-maintained)
  concept-dependency-map.md
  decisions/               (persistent-dual trade-off logs)
  test-linkages/           (source→test maps)
problems/                  # out-of-band concerns (any agent files; human reviews)
skills/                    # agent-invocable procedures (verbs; meta-phase promotes)
tools/                     # purpose-built evaluation tooling
log/                       # per-cycle human-readable summaries + README index
reference/                 # local clones of palace, bunsen, burn (gitignored)
orchestrator/              # decommissioned Python orchestrator (historical reference)
lessons.md                 # legacy cross-run lessons (historical; superseded by friction-ledger)
questions.md               # legacy question ledger (historical; superseded by open-questions)
MIGRATION.md               # full structural-redirect spec (Phase A artifact)
BOOTSTRAP.md               # original phased build spec (superseded; historical)
```

## Write-authority partition

| Agent | Writes to |
|---|---|
| cycle-planner | `reports/<id>/CYCLE.md` + `scaffolding/priorities.md` (**the plan** — co-owned with meta-phase; append fresh fan-out-ranked candidates + mark dispatched picks; does NOT do batch-level intake migration/compaction) |
| 8 specialized | `reports/<id>/CYCLE.md` + supporting docs in same dir only |
| critic | `reports/<id>/META.md` critique section |
| repairer | `reports/<id>/META.md` repair section + in-place edits to CYCLE.md / supporting docs |
| integrator-per-report | `book/` (per-report proposed-changes), `scaffolding/open-questions.md` (append-only), `reports/<cycle-id>-integrator-staging/STAGING.md` (append-only) |
| integrator-finalize | `book/` (build-repair only), `scaffolding/roadmap.md`, `scaffolding/cycle-record.jsonl`, `scaffolding/integrator-signals.md`, `log/`, `reports/<id>-integrator-finalize-cycle-N/CYCLE.md`, per-consumed-report `integrated_at` frontmatter touches |
| meta-phase | `.claude/agents/`, `skills/`, `scaffolding/priorities.md`, `scaffolding/friction-ledger.md`, `scaffolding/skill-candidates.md` (status updates), `scaffolding/problems-sensitivity.md`, `scaffolding/open-questions.md` (**unify only** — close/migrate/compact at meta-phase; see §Methodology invariants "Open-questions ledger is unified by the meta-phase"), channel-format specs |

**Any-agent-appendable** (append sections, never edit existing):
- `scaffolding/skill-candidates.md`
- `scaffolding/open-questions.md` (append-only between meta-phases; meta-phase has unify/edit authority — see partition note above)
- `scaffolding/decisions/`
- `scaffolding/test-linkages/`

## Methodology invariants

These are load-bearing — do not "improve" them away.

- **⟢ VOCABULARY-SHIFT REDIRECT (user directive 2026-06-01; full spec `METHODOLOGY-REDIRECT.md`).** The stack is a sequence of genuine **representational + component-vocabulary shifts**, NOT a rectangular projection. Each layer is complete/concise/correct **in itself**, and the **conciseness** constraint is the engine that drives **in-layer utility combinators/abstractions** (mined *inward* to simplify the layer; distinct from cross-layer themes). Each lowering is complete/concise/correct and is a **translation across vocabularies and semantic organizations — NOT a 1:1 named-term rename**; a degenerate identity-in-named-terms lowering is a **smell** (the vocabulary failed to shift — investigate; resolve as a thin in-line note or a combinator re-expression, NOT a mirrored entry + thin theme). **This SUPERSEDES:** the 2026-05-31 "uniform pull-up → rectangular" directive + its `foundation_solidity` / count-ownership / dual-registration rectangular-floor machinery (the "rectangular" success metric was the bug); "Identity-lowerings still require both L levels"; the leaf-vs-fold fork ratified (b) (→ now **fold/combinator-primary**: the combinator is the entry, leaves are specialization notes). The thin `-body-identity` L3>L2 / L2>L1 themes (cycles 041–048) and the base-form L2/L3 leaf floors are **refactored** (collapse leaves into in-layer combinators; propagate the combinator upward; demote thin themes to in-line notes) — refactor precedes new forward-frontier work. **Combinator-miner re-mandate:** replace-and-propagate, not mine-and-strand. **Solvers (all 5 pipelines + FE assembly) are pulled up as a LOW-PRIORITY test-load on the shared spine** — they advance a layer only when **cleanly describable** in existing shared vocabulary, NEVER at the cost of forcing the spine; what a solver can't cleanly say is a finding about the spine. The batch-14 "L4 substantially complete / strategic-pivot ASK" framing is **retired** — "complete" there meant *relative to the lifted inner-kernel cohort*, not the in-scope target; no pivot to the downstream burn effort yet. **The combinator-miner / harvester / abstractor / cycle-planner / layer-intro-author role-specs carry the matching bullets.**
- **The plan is the single ongoing work artifact; intake channels feed it, they don't hold work** (user directive 2026-05-28). `scaffolding/priorities.md` is **the plan**: the durable, fan-out-ranked component backlog, co-owned by `meta-phase` and `cycle-planner`. `scaffolding/open-questions.md`, `scaffolding/friction-ledger.md`, and `problems/` are **intake channels** — issues and friction are *reported* there, not parked. **Resolution = migration:** the meta-phase's standing every-batch pass (`.claude/agents/meta-phase.md` §Intake→plan migration) triages intake, **migrates actionable items into the plan** (ranked by fan-out), closes resolved/stale/duplicate to a compact index, and keeps genuinely-blocked items compacted with a trigger. `cycle-planner` examines the plan every primary cycle, dispatches **highest-fan-out work first**, and may append fresh plan candidates. `roadmap.md` is the coverage/goals map + the **fan-out impact model** (`|concepts| × |downstream-reuse| × 1/cost`) that ranks the plan — not itself a task list or a migration target. The *reason* for this structure: so the planning phase can prioritize the components with the most fan-out impact. An open question or friction pattern that lingers in its intake channel without a plan item means migration hasn't happened — that is the defect to catch, not unbounded ledger growth.
- **Citations are mandatory.** Every claim carries `(file, start_line, end_line)`. No citation, no claim. Citation format: plain text `relative/path/file.ext:start-end` (relative to `reference/`).
- **Roles do not share context.** Each subagent dispatch gets its own isolated context. The critic in particular must not see the producer's chain-of-thought.
- **Reports are append-only after integration.** After `integrated_at:` is set, CYCLE.md content is not edited. (Repairer may edit pre-integration; bounded by repair authority.)
- **Commit every cycle, pass or fail.** The integrator commits + pushes. Atomic operation: artifact + scaffolding + log + book output as one commit.
- **Push after every commit.** `git commit ... && git push origin main` chained. No commits sitting locally between turns.
- **Spec growth is monotonic and visible in `git log`.** Realized as CYCLE.md proposed-changes blocks parsed by the integrator.
- **If a step is ambiguous, stop and ask the human.** Don't improvise around the spec.
- **L4 strawman (`book/src/design/l4_calculus.md`) is in-management for L4 and L3 work** (user directive 2026-05-27, mid-cycle-006). The strawman is the authoritative reference for L4 calculus conventions: BNF grammar for types/terms/shapes, reduction-rule format ($$ ... $$ math display), `iterate_while` / pruning / monad semantics. L4 and L3 entries (`book/src/L4/<op>.md`, `book/src/L3/<op>.md`, `book/src/L4-L3/<theme>.md`, `book/src/L3-L2/<theme>.md`) cite and continue the strawman; they do not displace it. Cycle-006's first firm L4 entry (`book/src/L4/krylov-step.md`) and first firm L4>L3 theme (`book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`) are the precedent examples — read them when authoring new L4/L3 content.
- **L4 and L3 pseudo-language is Haskell + TypeScript notation in fenced code blocks** (user directive 2026-05-27, same as above). Signatures use Haskell `::` arrow form (`f :: A -> B -> C`); records use TypeScript brace form (`{ field: type }`); body shapes use Haskell-style do-notation (`do { let x = e; modify f; pure r }`) and lambda (`\s -> ...`). Fenced as ` ```text ... ``` ` (the strawman uses `text` as a generic non-highlighted fence). Reduction rules and small-step semantics use LaTeX math display (`$$ ... $$`). Do not transcribe L4/L3 forms into prose; do not invent new notation conventions. The strawman's notation is the canonical one because the calculus is language-agnostic-but-code-like and the mix has settled across v0.1–v0.3 iterations.
- **Primary-context reset is covered by the post-meta session restart; there is no separate `/compact` step** (user directive 2026-05-29, superseding the 2026-05-27 "Compactify primary context after every meta-phase" directive). The meta-phase routinely enacts role-spec changes, so the parent restarts the Claude Code session before the next cycle (per friction-ledger `new-agent-defs-need-session-restart`); a restart resets the primary conversation entirely, which subsumes what the old `/compact` step did. Do **not** emit `/compact` asks at meta-phase end — the restart is the reset mechanism. (Historical: the retired directive ran `/compact` at the end of each meta-phase to trim accumulated dispatch transcripts; it is removed because it is redundant with the restart.)
- **Meta-phase runs every 3rd primary cycle** (user directive 2026-05-27, post-cycle-006 meta). Primary cycles (plan → dispatch → critique → repair → integrate) fire continuously; meta-phase fires only after every 3rd primary cycle's integrator-finalize, aggregating evidence across the full 3-cycle batch. Rationale: single-cycle noise (a one-off critic warning, an isolated unrepairable finding) washes out in a 3-cycle window, so persistent patterns surface more cleanly and methodology adjustments are less reactive. The cycle counter does not reset at batch boundaries — cycles 007/008/009 form batch-1 with meta after 009; 010/011/012 form batch-2 with meta after 012; etc. The meta-phase report filename uses the cycle-id of the third (final) primary cycle in the batch (`reports/<timestamp>-meta-phase-cycle-<N>/CYCLE.md` where N = third cycle).
- **Layers are defined high→low; lifting notes go in working notes** (user directive 2026-05-27, mid-cycle-009). Higher-layer entries are defined **in terms of themselves** (their own layer's vocabulary, or higher-layer references), NOT in terms of lower-layer vocabulary. Lowering-layer themes (`L_{n+1}>L_n`) are defined as "**how the L_{n+1} form lowers into the L_n form**" — explicit direction; the LHS is L_{n+1}, the RHS is L_n, the prose narrates the rewrite. Notes about the *reverse* direction (how L_n lifts into L_{n+1}, what evidence supports the lift, what additional structure the lift requires) live in **working notes** (`scaffolding/`, per-report supporting docs, OQ ledger entries) — NOT in the formal chapter content. **The formal document structure stays high→low.** Cycle-008 wave-1 abstractor's `ksp-solve-mutation-rotation` (L1>L0) is the in-spirit precedent: the theme defines how L1 `ksp_solve` rewrites into L0 source patterns, not how L0 patterns lift to L1. Practical consequence: when authoring an L_n operator entry, the Semantics + Algebraic-laws + Signature live in L_n vocabulary (with references to L_{n+1} for upward context if useful); the L_n>L_{n-1} dispatch is what does the lowering work, narrated forward from L_n to L_{n-1}. If you find yourself defining an L_n operator's semantics in terms of L_{n-1} primitives, the description belongs in an L_n>L_{n-1} theme, not in the L_n entry.
- **Lower-level shared vocabulary takes priority** (user directive 2026-05-27, mid-cycle-009). When choosing between (a) expanding higher-layer vocabulary further and (b) populating lower-layer shared utility, **prefer (b)**. Reusable lower-level vocabulary makes other components cheaper and simpler to describe, enables unification of seemingly-distinct higher-layer patterns, and reduces duplication explosion in adjacent layers. Concretely as of post-batch-1: `book/src/L3/` is empty (placeholder only) despite the krylov-step lowering chain being fully firm via L4>L3>L2 with no interposed L3 row; per the **identity-lowerings still require both L levels** invariant below, the cycle-006 "no L3 row needed for krylov-step" verdict is SUPERSEDED — krylov-step should still get an L3 entry. Cycle-010+ planner should weight L3 / L2 / L1 firm operator additions above further L4 vocabulary expansion when both are eligible. Lower-layer rough-ins (e.g., the 1 firm L2 operator after 1 firm L4 chain promotes; the 0 firm L3 operators) signal that the lower vocabulary needs more weight in scheduling.
- **Uniform pull-up L0→L4; foundation-solidity is a ranking weight** (user directive 2026-05-31, post-cycle-040). The goal is a **uniform climb of the whole stack** — each layer advanced on **solid foundations below it**, NOT a single layer raced ahead of its support. This **restores the founding L0→L4 impedance-matching intent** and corrects the cycle-036-audit-driven "fill out L3 specifically" pressure, which grew L3 to 18 entries while only 5 had a same-named L2 parent and only 2 of 18 carried an L3>L2 rotation theme — a **middle-heavy stack standing on a missing floor**. **Soft weight, not a hard gate** (user decision 2026-05-31): foundation-solidity is a **strong fan-out ranking factor**, not a blocking precondition. Concretely:
  - An L_{n+1} entry's ranking value is **discounted** when its L_n parent and/or its L_{n+1}>L_n rotation theme are absent or non-firm; **completing a foundation gap** (an absent L_n parent under an existing L_{n+1} entry; an unwritten L_{n+1}>L_n rotation) is **rewarded** — it ranks at or above further same-layer width or higher-layer expansion when both are eligible.
  - The planner picks the **lowest incomplete layer first** when work is otherwise comparable in fan-out, so the frontier advances as a roughly level front rather than a spike.
  - **Exceptions are allowed with stated rationale** (it is a weight, not a gate) — a high-fan-out higher-layer item may still be picked over a low-value foundation backfill, but the planner must say why.
  - This **strengthens** "Lower-level shared vocabulary takes priority" (above) and tilts the standing tension between "Identity-lowerings still require both L levels" (below) and "Identity rotations across non-adjacent layers are annotated in-line" (further below) **toward present-floor coherence**. The concrete first instance is the **L2 floor under the L3 BLAS-1 / elementwise / smoother cohort**: 13 L3 entries (`dot`/`axpy`/`nrm2`/`scal`/`axpby`/`axpbypcz`, `assemble-diagonal`/`jacobi-smoother`/`divfree-projector`/`elementwise_product`/`reciprocal`/`normalize`, `chebyshev`) currently lift directly from L1 via the inline non-adjacent transitive-identity annotation, with **no L2 entry**. Under this directive, building those L2 floor entries (+ their L2>L1 identity themes) and the missing L3>L2 rotation themes is **high-fan-out foundation work, ranked above further L3 (B) substantive width**. The fan-out impact model (`scaffolding/roadmap.md` §Intermediate-tier `impact_score`) carries the matching `foundation_solidity` factor; `scaffolding/priorities.md` active head + High-fan-out backlog were reshaped to this directive (2026-05-31). This is a **ranking rebalance, not a pause** — foundation work and continued frontier work proceed together, the stack self-corrects toward rectangular cycle-by-cycle.
- **Identity-lowerings still require both L levels** (user directive 2026-05-27, mid-cycle-009). When the lower-layer form is identity-in-form to the upper-layer form — i.e., the operator's body at L_n is value-thread-isomorphic to its body at L_{n+1} and the rewrite is trivial — **the operator still gets its own entry at the lower layer.** Rationale: **each layer is coherent within itself.** A reader navigating L_n should not have to jump up to L_{n+1} to find the operator; the L_n entry exists, uses L_n vocabulary, and the L_{n+1}>L_n theme between them notes the identity. The cycle-006 audit's decision NOT to land `book/src/L3/krylov-step.md` on the rationale "L3 form is identity to L2 form" is now SUPERSEDED by this directive. Practical consequence: when a harvester or abstractor finds that a lower-layer form is identity-in-form, the work product is still an L_n entry (using L_n vocabulary) plus a thin L_{n+1}>L_n identity theme noting the no-op rewrite. Cycle-010+ harvester on `book/src/L3/krylov-step.md` is the precedent backfill; audit other L3 candidates (apply_linop, etc.) for the same pattern.
- **Phase 1 corpus reduces as material is lifted** (user directive 2026-05-27, mid-cycle-009; canonical-instance carve-out codified cycle-033 meta-phase). `book/src/spec/slices/` is the Phase 1 slice corpus (cycles 1–172 era; pre-structural-redirect). It is **raw material for the layered artifact**, not the deliverable. As a slice's material is successfully lifted into the layered artifact (L0/L1/L2/L3/L4 + lowering layers) and the lifted form becomes the authoritative representation, **the corresponding slice should be reduced** (compacted to a stub pointing at the firm layered entries it has been absorbed into) **and eventually removed** as the layered surface becomes fully authoritative. The corpus is allowed to shrink monotonically as the artifact grows; the slice form is not preserved as historical record once its content lives in the layered surface (the git history is the historical record). Audit pattern: cycle-010+ `same-layer-cross-cutter`-scoped dispatch on a `book/src/spec/slices/<slice>.md` entry — verify the slice's content is fully represented in firm layered entries, propose reduction to a stub or removal, surface any residual coverage gap that blocks reduction. The audit itself is per-cycle work, not a meta-phase enactment. **Canonical-instance carve-out (cycle-033 meta-phase codification of a pattern in implicit use since cycle-013):** the firm-layered-home check is *necessary but not sufficient* — a slice may have a firm layered home AND still be load-bearing as the **named canonical-witness instance** of downstream concept pages. A slice MAY be retained-by-design (status `annotated-and-retained`, NOT reduced-to-stub) when **(a)** it is named (by slug + filename) as the §Canonical-instance / "instance of" referent of **≥2 concept pages** in `book/src/concepts/`, AND **(b)** it carries unique L0 navigation (file:lines anchors) not covered elsewhere in the firm artifact. The bar is ≥2 concept-page references (a single concept-page reference is recoverable by re-anchoring the concept page); the carve-out does NOT license retaining slices that are only fully-lifted-AND-not-referenced. Precedents: `polynomial_recurrence_step` (cycle-013, retained-by-design as canonical instance for the chebyshev polynomial-recurrence concept), `sparse_triangular_solve` (cycle-031, retained-by-design as canonical instance for 3 concept pages even though `triangular-solve-obstruction` L1>L0 is firm at c029). The `phase-1-slice-reduction-audit` skill checklist carries the matching audit-side bullet (concept-page-grep before recommending reduction). Friction-ledger `negative-result-slice-canonical-instance-blocks-reduction`.

- **Theme/operator status `partly-constructive` is first-class** (cycle-012 meta-phase codification of a pattern recurring across cycles 010/011/012). Alongside `firm` / `rough-in` / `obstruction`, a theme or constructed operator may be **`partly-constructive`**: firm in its structural decomposition (the rewrite is recognized and exhaustively cited) but carrying a named, citation-backed caveat on one or more **constructive sub-parts** — a status value, a result field, an error condition materialized from negative anchors / literature rather than read from a positive Palace source site. A `partly-constructive` entry MUST state (i) exactly which sub-part is constructive, (ii) its negative-anchor citations, and (iii) an explicit **promotion condition** (what would make it fully firm: an upstream positive source site, a per-line lowering-verifier audit, or a literature-anchor upgrade). Do NOT mark such an entry `firm` (the constructive sub-part isn't) and do NOT downgrade the whole entry to `rough-in` (the structure IS firm). The **negative anchors** that justify a constructive sub-part (citations to where Palace does NOT positively exhibit the construct) are distinct from per-operator `obstruction`-theme negative anchors (which document an unimplemented stub): a per-status negative anchor is evidence FOR the constructed form being a faithful reconstruction; it does NOT license asserting a positive claim without a positive site. A `partly-constructive` status is a transient gate, not a permanent escape hatch — the promotion condition should eventually close. Precedent: `book/src/L1-L0/eigsolve-mutation-rotation.md` Sub-pattern B (`LinearSolveFailed`); audited cycle-012 (gated promotion to cycle-013). The lowering-verifier may UNBLOCK such a promotion (confirm the structure + identify the exact firming edits) without ENACTING it — the follow-up dispatch applies the edits then drops the caveat.

- **Two rough-in qualifiers are first-class: `rough-in (test-coverage-bounded)` and `partial-obstruction`** (cycle-021 meta-phase codification of two status tiers in live use since cycles 009/013). These sit alongside `stub` / `rough-in` / `partly-constructive` / `firm` / `obstruction` and name two recurring "structurally-anchored-but-not-promotable-yet" situations distinct from `partly-constructive`:
  - **`rough-in (test-coverage-bounded)`** — the operator's structural signature is well-anchored at L0 (input/output shape, variant axes, source-witnessed cases) but its **algebraic-law confidence is reduced pending dedicated test coverage OR expanded literature anchoring**. The entry stays `rough-in` (NOT firm) because the laws are stated-but-unconfirmed, not because the structure is unknown. Promotion route: a dedicated unit test exercising the operator at the exact entry point (which may be out of project write-scope when no `test-<area>.cpp` exists), OR a literature-anchor harvester/lowering-verifier pass that raises law-confidence to `ksp_solve`-equivalent. The qualifier is recorded in the `## Status` line with the gating reason. Distinct from `partly-constructive` (which is firm-structure + a *constructed* sub-part from negative anchors); here the structure is firm but the *laws* are test-gated. Precedents: `book/src/L1/eigsolve.md:167` (cycle-009), `book/src/L1/matrix-weighted-norm.md:110`. NOTE the firm-on-positive-structure escape: an entry whose laws are **syntactic identities on fully-specified positive source** (e.g. `apply_nonlinear_pencil` — every law is operator-algebra on a read closure) is `firm` even when the surrounding area has no test, because the missing test does not gate syntactic-identity laws (the `apply_linop` situation, not the `eigsolve`-convergence-semantics situation).
  - **`partial-obstruction`** — used at L3 (the iteration-rotation layer) for an operator whose **per-step body lifts cleanly to a global tensor-field expression but whose loop structure does NOT lift** (an inner recurrence and/or outer sweep is a witnessed `sequential-obstruction` with a cited non-removability reason). The status reflects the **loop structure, not the body**: the body is recorded as identity-in-form to the lower layer; the obstruction is the un-liftable iteration. Distinct from a whole-operator `obstruction` (which documents an unimplemented Palace stub) — here the operator IS implemented and its body IS lifted; only the loop resists the iteration rotation. Precedent: `book/src/L3/chebyshev.md` (cycle-013; inner `k`-recurrence + outer `pc_it` Richardson sweep both sequential per Phillips & Fischer 2022 §2). The cycle-021 `l3-eigsolve-linear-evp-has-no-krylov-step-kernel-analog` finding predicts the eventual L3 linear-EVP eigsolve will land `partial-obstruction` (or full sequential-obstruction) for the same reason (the eigen-iteration is opaque-library-owned).

- **Obstruction themes have two sub-kinds: `enum-only-stub` and `opaque-library-ownership`** (cycle-030 meta-phase codification of two distinct shapes in live use since cycles 004/029). Both wear `## Status: obstruction` (the umbrella category is unchanged), but the sub-kind is named inline (`## Status: obstruction (enum-only-stub)` vs. `## Status: obstruction (opaque-library-ownership)`) because the **routing decision the obstruction encodes is different**:
  - **`obstruction (enum-only-stub)`** — Palace ships an *internal* stub: a JSON / enum / aborting-branch configuration whose method body is `// TODO` / `MFEM_ABORT` / `MFEM_ASSERT(false)` / empty. The functionality is *named* in Palace's configuration surface but *not implemented*. Promotion route: a future Palace upstream change fills in the body. Precedent: `book/src/L1-L0/minres-iteration.md` + `bicgstab-iteration.md` (cycle-004).
  - **`obstruction (opaque-library-ownership)`** — the functionality IS available to Palace but ONLY through a *library boundary* (HYPRE relax-type enums, SLEPc EPS solver loop, external direct-solver wrappers). Palace itself never exposes the primitive as a standalone callable; it consumes the behavior opaquely via the library's own surface. Promotion route: NONE in the conventional sense — the theme stays obstruction unless Palace re-architects its consumption (highly unlikely). The theme's value is *documenting the boundary* + cataloguing the negative anchors so future producers don't waste cycles re-localizing. Precedent: `book/src/L1-L0/triangular-solve-obstruction.md` (cycle-029, the FIRST such; HYPRE relax-type sites + external direct-solver wrappers as negative anchors). The cycle-024 `eigsolve` L3 `partial-obstruction` is a sibling case at a different tier (loop-only opaque, body lifts).
  
  Practical consequence: when an abstractor authors a new obstruction theme, the sub-kind tag is mandatory in the `## Status` line (default to **enum-only-stub** when the Palace TODO / aborting branch is on a Palace-owned method body; default to **opaque-library-ownership** when the entire callable lives outside Palace). Cross-layer-cross-cutter consumers may treat the two sub-kinds differently (an enum-only-stub is "anticipated work the team might do upstream"; an opaque-library-ownership is "permanently library-owned, never re-promotable"). Friction-ledger `obstruction-sub-kind-opaque-library-vs-enum-only-stub`. Abstractor role-spec §Discipline carries the matching producer-side bullet. Skill `establish-negative-finding-exhaustiveness` is the companion procedure for establishing the negative anchors strongly enough to license either sub-kind's routing.

- **Integration may materialize implied components as stubs** (user directive 2026-05-28). The "one operator/theme per dispatch" discipline means producers reference siblings/children that *don't exist yet* via plain-text forward-references (per the `rough-in-rows-must-be-plain-text-when-anchor-missing` convention — a live link to a missing file is a hard `linkcheck2` build error). When **multiple passes converge on the same conclusion that a given slug should exist** — repeated forward-references, a rough-in dep-map row pointing at an unwritten chapter, recurring OQs naming the same target — leaving it as a perpetually-deferred plain-text reference is friction. **At integration, it is acceptable to create the additional slug/stub entry for the implied component, to be refined later.** A **`stub`** is the thinnest maturity tier — `stub` → `rough-in` → (`partly-constructive`) → `firm` — a *claim-free placeholder*: a real file (or dep-map row) with `status: stub` frontmatter, a one-or-two-line definition sketch, an **"Implied by"** provenance list (the reports / forward-refs / OQs that converged on it), and a "Refinement pending" note. Its purpose: cross-references resolve to a **live link**, the plan/OQ-ledger can point at a real home, and the next harvester/abstractor refines it in place. **Who/when:** `integrator-per-report` MAY create a stub for an implied not-yet-existing slug referenced by the report it is applying (instead of forcing the reference to plain-text); `integrator-finalize` MAY create a stub at build-repair time when a dead-link to a clearly-implied component surfaces (preferred over de-linking). **Bar:** the component is *clearly implied* (≥2 converging references, or a rough-in row already standing for it) — not merely speculative. Creating a stub is the **preferred** resolution for an implied-component forward-reference; plain-text-defer remains the fallback when the component is only speculative / might not materialize. **Critic handling:** a `stub` makes no claims, so the citation / surface / rotation / variant-axis checks no-op on it; the critic verifies only that the stub carries provenance and is wired into `SUMMARY.md`. Stubs are tracked for refinement in the plan (`priorities.md`) like any rough-in. Friction-ledger `rough-in-rows-must-be-plain-text-when-anchor-missing` + `rough-in-forward-reference-must-be-plain-text-not-live-link` (both amended by this directive: stub-creation is now the preferred path, plain-text the fallback).
- **Identity rotations across non-adjacent layers are annotated in-line, not via a dedicated lowering directory** (cycle-012 meta-phase decision; ~9+ in-line instances exceeded the revisit threshold of 6). Lowering directories are **per-adjacent-edge only** — `L4-L3/`, `L3-L2/`, `L2-L1/`, `L1-L0/`. When an operator's identity-in-form (per the "Identity-lowerings still require both L levels" invariant above) spans **non-adjacent** layers — e.g. its L3 body is value-thread-isomorphic to its L1 form because the intervening L2 absorption is also identity-like — that relationship is the **transitive consequence of the adjacent-edge themes** (L3>L2 identity ∘ L2>L1 identity ⟹ L3>L1 identity). Annotate it **in-line** in the L_n entry (the "Downward to L_{n-1}" prose + the dep-map), citing the existing adjacent-edge themes; do NOT create a `book/src/L3-L1/`, `L4-L2/`, etc. directory. Rationale: a non-adjacent lowering directory would break the adjacent-edge structural invariant and duplicate what the adjacent-edge chain already says; the in-line annotation is the natural home (each L_n is coherent within itself and notes its identity relationships in-line). Precedent: `book/src/L3/krylov-step.md` §"Upward"/"Downward" + dep-map; the whole BLAS-1 L3 cohort. Re-open ONLY if a genuine NON-identity rotation surfaces across non-adjacent layers that the adjacent themes don't compose to capture (none has). Friction-ledger `l3-l1-inline-identity-rotation-convention`.

## Process model: push-forward, push-back; the stack is a research artifact

**The stack is not the deliverable. It is a research artifact whose construction yields the understanding that *is* the deliverable.** Layers exist to expose friction. The valuable signal lives in the friction.

- **Push-forward, one slice / theme / operator at a time.** A layer's job ends as soon as the next layer can speak.
- **Push-back when friction surfaces.** While working at layer N+1, if a different framing of layer N would make N+1 dramatically easier, restructure layer N.
- **Move sideways** when progress on one slice is blocked. Use the sideways move to surface unification opportunities.
- **Explore alternative formulations when they exist; coalesce by use.** Persistent duals are permitted when they capture genuinely distinct aspects; not permitted when they cause duplication explosion in adjacent layers.
- **Accumulate a working surface with embedded problems.** Revise verdicts APPLY the diff (surface accumulates with friction embedded). Only `reject` blocks application.

## Optimization tricks vs. base algebra

A significant fraction of Palace's C++ exists because it was tuned for CPU + cache + SIMD. That cost model is not burn's, and most of the resulting code shape is counter to the goals of a pure GPU tensor implementation.

- **Transparent performance tricks** (fusion, tiling, packing, batching, memory layout, recomputation-vs-lookup) — algebraically equivalent to their unfolded form. The L1 form is the unfolded form; the trick gets a one-line note.
- **Load-bearing numerical tricks** (non-associative reduction orderings, fast-math, mixed-precision intermediates, deterministic-vs-atomic accumulation) — **part of the algorithm**. Preserve as explicit algebraic claims with the property they buy (determinism, condition-number, IEEE compliance) called out.

When in doubt, the critic flags as `unclear` and the human triages. Mis-classifying a load-bearing trick as transparent silently changes the algorithm.

## Tests as semantic supplement

Palace's unittests under `reference/palace/test/unit/` are **semantic documentation**, not just regression scaffolding. A test that constructs input, calls a function, and asserts on the resulting state is direct evidence of mutation pattern, algebraic semantics, and whether a trick is load-bearing.

- **Specialized agents** look for tests when localizing source. Cite tests alongside source ranges — tests are L0-equivalent.
- **Critic** consults tests when verifying claims. A test assertion contradicting a claim is `citation-does-not-support`.
- Test linkages tracked in `scaffolding/test-linkages/`.

## Scope

- **Target deployment is a single machine.** CPU → GPU via burn's device backends. MPI / multi-rank distribution is **out of scope** — flag once and skip. In MFEM, `Par*` types (`ParGridFunction`, `ParBilinearForm`, `HypreParVector`, …) are read as their single-rank equivalents.
- **Solvers in scope: all 5.** Electrostatic, magnetostatic, eigenmode, driven, transient.
- **Mesh / FE-space construction in scope.** MFEM-equivalent FE assembly is dissected alongside the solver pipelines.
- **Unimplemented Palace components are NOT direct implementation targets** (user directive 2026-05-27). When Palace ships a stub (enum-only / JSON-only / aborting-branch configuration, e.g., MINRES + BiCGStab at `palace/linalg/ksp.cpp:53-56`):
  - **Document the stub** as an L1>L0 obstruction theme with negative-anchor citations. This is documentation, not a lowering rule.
  - **Do not target the unimplemented functionality for filling in.** The goal is to match Palace's current feature set on top of the target L4 semantics — not to extend Palace.
  - **The literature-anchored L1 form may inform higher abstractions.** Collection and lifting of higher forms (L2 combinators, L4 primitives) may permit extensions into feature sets Palace hasn't implemented yet — this is permitted.
  - **Promote a speculative L1 operator to firm only when small AND when it simplifies the semantics of higher forms.** If `lanczos_step` makes `krylov-step` at L2 cleaner by factoring the symmetric-tridiagonal case from the asymmetric-Hessenberg case, that's a good promotion. If a promotion adds vocabulary without simplifying anything upstream, defer.
  - **Practical consequence**: cycle-004's `minres-iteration` and `bicgstab-iteration` themes stay as obstruction documentation. The 6 speculative rough-in operators are not promoted unless a cycle-005+ harvester-on-`krylov-step` finds that promoting one of them simplifies L2 semantics.

## Target system

**AWS Labs Palace** — <https://github.com/awslabs/palace>. C++ (~85% of tree), CMake ≥ 3.24, MFEM + libCEED + MPI + BLAS/LAPACK + optional CUDA/ROCm.

- Many symbols resolve into upstream libraries (MFEM, libCEED). Specialized agents cite Palace source, not vendored upstream. If a question requires upstream behavior, log as open question.
- Heavy C++ templates — read tightened regions; prefer narrow text-search before reading.
- **MCP-first localization** (cycle-012 meta-phase codification; pilot succeeded cycle-010, routine use cycles 011/012 with zero permission-denied). The `palace-codemap` MCP server is available and is the **preferred localization path** for the Palace C++ tree: localize via `mcp__palace-codemap__list_files` / `search_text` / `get_symbol_def` / `get_call_sites` / `list_dependencies` / `get_file_subtree`, then use `read_range` deliberately for the actual source (it is the only source-returning codemap tool). This is the better realization of "prefer narrow text-search before reading" for the heavy-template tree. The cycle-planner in particular should verify file paths / symbol locations via the codemap before citing them in dispatch scopes (it has repeatedly drifted on `linalg/*` paths — friction-ledger `cycle-planner-dispatch-prompt-framing-drift`). Vanilla `Grep`/`Read` remain available; agents apply judgment on which is faster for a given query. Friction-ledger `mcp-first-localization-codified` + `mcp-codemap-permission-denied-across-batch-1` (resolved).

## Reference repos (local clones, gitignored under `reference/`)

- `reference/palace/` — the C++ source being dissected.
- `reference/bunsen/` — the user's burn-overlay library. `reference/bunsen/crates/bunsen/src/kits/sims/` is the methodology reference (Conway, LBM).
- `reference/burn/` — the target tensor library.

## Bunsen methodology conventions (carried forward)

Visible in `reference/bunsen/crates/bunsen/src/kits/sims/`:

- **Pure tensor-in / tensor-out functions are the algebra.** State-bearing wrappers are *thin*.
- **Decompose into named algebraic pieces** in separate files.
- **Symbolic shape contracts at boundaries** — `[H, W, VY=3, VX=3]` with named axes.
- **Docstrings declare I/O sets explicitly** — `# Arguments` / `# Returns` blocks.
- **L1↔L2 equivalence tested concretely** when feasible.
- **Performance notes are inline `// Timing:` comments**, not abstractions.

## Problems channel — out-of-band concerns

`problems/` is the channel for any agent to raise concerns that exceed their own role's authority. **Relaxed bar (2026-05-26):**

- **(A) Out-of-role conflicts** — e.g., critic notices a producer-prompt-level pattern.
- **(B) Observed-but-not-in-focus drive-by observations** — phrasing pattern: "In reading the context for this work [...]; the following contradiction, duplication, miss-framing, etc in reference work was noticed."

Filing rate is self-tuned per `scaffolding/problems-sensitivity.md`; target ~1/15 cycles. Meta-phase recalibrates each cycle.

## Skills

Agent-invocable procedures under `skills/<name>/SKILL.md`. Any agent can propose via `scaffolding/skill-candidates.md`; meta-phase promotes with default-accept under low-bar policy. Promotion bar: pattern observed ≥2 cycles OR candidate sketch concrete enough to write as SKILL.md OR friction-ledger entry exists for the addressed pattern.

Current skills (under `skills/`; updated cycle-024 meta-phase):
- `classify-variant-axis`
- `verify-citation-range` (extended cycle-012 with an "Audit-report / inherited-citation sub-case"; cycle-021 with a "Sibling-slice / inherited-precedent re-anchor sub-case"; cycle-024 with the mechanical `tools/citecheck/` `--anchor`/`--scan` realization)
- `skill-selection`
- `verify-refinement-surface`
- `verify-rotation-citation`
- `propose-rotation`
- `find-tests-for-region`
- `plan-sideways-concept-emission`
- `cluster-friction-patterns`
- `survey-friction-window`
- `summary-md-surgical-insert` (cycle-005)
- `phase-1-slice-reduction-audit` (cycle-012; same-layer-cross-cutter slice-reduction audit with START+END boundary verification)
- `revert-dispatch-phase-book-mutation` (cycle-012; repairer safety-net for dispatch-phase artifact leaks)
- `partly-constructive-promotion-checklist` (cycle-015; the 4-point partly-constructive→firm promotion-record checklist)
- `proposed-changes-fence-encloses-full-body-guard` (cycle-021; critic build-readiness fence-parity guard — DETECTS the firm-body-outside-fence defect)
- `convert-nested-fences-to-indented-code-in-proposed-changes-block` (cycle-024; repairer REPAIR of the nested-`text`-fence truncation variant — counterpart to the detection guard)
- `upgrade-plain-text-ref-to-live-link-when-target-on-disk` (cycle-024; repairer/producer on-disk→live-link upgrade for references needlessly left plain-text)
- `embed-and-persist-subagent-dispatch` (pilot-1; retired-but-kept after the REPORT.md→CYCLE.md rename)

## Models

- **All agents** — `claude-opus-4-8` (user directive 2026-05-31: all models set to Opus 4.8). This subsumes the prior split (`cycle-planner` on `claude-haiku-4-5-20251001` "cheap routing"; all other agents on `claude-opus-4-7`). The cycle-planner haiku→opus escalation that the batch-10 meta-phase surfaced as an ASK (friction-ledger `cycle-planner-stale-priorities-line-recruitment`) is now enacted as part of this blanket upgrade.

## Escalation triggers

Surface to the human immediately rather than working around — these signal architectural problems, not content problems:

- Critic rejects three consecutive reports on the same scope (prompt bug, not content).
- A specialized agent's input exceeds reasonable token budgets on one region (scope too coarse — cycle-planner needs to subdivide).
- Open-questions ledger grows monotonically over 20 cycles with zero closures (generating questions faster than answering).
- Two specialized agents produce contradictory claims about the same source range across consecutive cycles (source itself may be ambiguous).
- Friction-ledger pattern reaches recurrence ≥5 with status not yet `addressed` (meta-phase isn't catching it).
- Custom `.claude/agents/<name>.md` definitions don't resolve via `Agent(subagent_type=<name>, ...)` (architectural — affects every dispatch).

## Inputs the human supplies

Before invoking the loop:
- Anthropic API access (env or harness credentials).
- `reference/` checkouts of palace + bunsen + burn (already in place).

If anything is missing or ambiguous, stop and ask.
