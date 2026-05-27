# CLAUDE.md

Operational guide for Claude Code working in this repository. The project is a multi-agent pipeline that dissects AWS Labs **Palace** (C++ electromagnetic simulator) into a **layered, citation-grounded specification** organized as an incremental impedance-matching stack L4→L0.

This file replaces the original CLAUDE.md (slice-vertical era, cycles 1–172) after the **structural redirect of 2026-05-26**. The redirect is fully specified in `MIGRATION.md`; this CLAUDE.md is its operational distillation. The previous `BOOTSTRAP.md` is superseded and kept only as historical record.

## Repository status

- **Current flow**: 6-phase agent cycle (plan → dispatch → critique → repair → integrate → meta). See *Cycle structure* below and `MIGRATION.md` §2.
- **Artifact in progress**: layered specification under `book/src/L4/`–`book/src/L0/` + 4 lowering Parts. The Phase 1 slice corpus under `book/src/spec/slices/` is preserved as raw material for combinator extraction (not the deliverable).
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

## Cycle structure: plan → dispatch → critique → repair → integrate → meta

Each R&D cycle has 6 phases:

```
  cycle-planner → N specialized agents → N critics → N repairers → integrator → meta-phase
    (serial)        (scatter; parallel)     (scatter)    (scatter)    (serial)    (serial)
```

**Phase 1 — plan**: `cycle-planner` reads roadmap, priorities, friction-ledger, open-questions, recent integrator batches. Emits a dispatch plan with `(agent, scope, deps)` tuples and an overlap analysis. Does not mutate the artifact.

**Phase 2 — dispatch**: 1–6 specialized agents per plan, parallel where non-overlapping. Each writes a single `CYCLE.md` under `reports/<timestamp>-<agent>-<scope>/`. No artifact mutation in this phase.

**Phase 3 — critique**: `critic` agent runs on each report (parallel). Runs the 8-check checklist (citation-validity, surface-or-evidence, rotation-quality, variant-axis-coverage, cross-reference-integrity, edge-label-fidelity, plan-kind-consistency, skill-uptake-survey). Writes META.md critique section.

**Phase 4 — repair**: `repairer` agent runs on reports with warning/fail findings (parallel). Mechanical and surgical fixes only — not substantive authoring. Writes META.md repair section. Sets `overall_status`.

**Phase 5 — integrate**: `integrator` reads all reports + METAs. Applies `ready` reports, defers `needs-revision`, marks `reject`. Runs safety-net gates. Rebuilds book, repairs link-check / format breakage, commits + pushes. Emits batch report. Sole writer of `book/`, `scaffolding/roadmap.md`, `log/`, `scaffolding/cycle-record.jsonl`, `scaffolding/open-questions.md`.

**Phase 6 — meta**: `meta-phase` examines cycle evidence + running history. Records escalating trends in `scaffolding/friction-ledger.md`. Proposes plans, judges them, decides `go` / `no-go` / `ask` per plan. Enacts `go` items directly: writes to `.claude/agents/`, `skills/`, `scaffolding/priorities.md`. Surfaces `ask` items to human. Separate commit from integrator.

## The 13 agents

Definitions live under `.claude/agents/`. Dispatch via `Agent(subagent_type=<name>, ...)`. If custom agent definitions don't resolve in the current Claude Code session, use the embed-and-persist pattern from `skills/embed-and-persist-subagent-dispatch/`.

**Pre-dispatch (1):**
- `cycle-planner` (haiku) — serial dispatch planner.

**Specialized dispatch (8, all opus):**
- `layer-intro-author` — writes L_n / L_{n+1}>L_n Part overviews + dep-maps.
- `harvester` — formalizes one L_n operator per invocation.
- `abstractor` — sketches one L_{n+1}>L_n theme + speculative L_{n+1} operators.
- `lifter` — re-anchors a theme to firmed-up vocabulary.
- `lowering-verifier` — audits one theme against evidence.
- `combinator-miner` — finds one recurrent pattern, proposes a combinator.
- `same-layer-cross-cutter` — one unification/redundancy/contradiction observation.
- `cross-layer-cross-cutter` — one cross-layer coverage-gap/edge-mismatch observation.

**Post-dispatch validation (2):**
- `critic` — runs 8-check checklist per report; META.md critique section.
- `repairer` — attempts mechanical fixes per finding; META.md repair section + REPORT in-place edits; sets `overall_status`.

**Application (1):**
- `integrator` — applies ready reports; safety-net gates; rebuild book; commit + push.

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
| cycle-planner, 8 specialized | `reports/<id>/CYCLE.md` + supporting docs in same dir only |
| critic | `reports/<id>/META.md` critique section |
| repairer | `reports/<id>/META.md` repair section + in-place edits to CYCLE.md / supporting docs |
| integrator | `book/`, `scaffolding/roadmap.md`, `scaffolding/cycle-record.jsonl`, `scaffolding/open-questions.md`, `log/` |
| meta-phase | `.claude/agents/`, `skills/`, `scaffolding/priorities.md`, `scaffolding/friction-ledger.md`, `scaffolding/skill-candidates.md` (status updates), `scaffolding/problems-sensitivity.md`, channel-format specs |

**Any-agent-appendable** (append sections, never edit existing):
- `scaffolding/skill-candidates.md`
- `scaffolding/open-questions.md`
- `scaffolding/decisions/`
- `scaffolding/test-linkages/`

## Methodology invariants

These are load-bearing — do not "improve" them away.

- **Citations are mandatory.** Every claim carries `(file, start_line, end_line)`. No citation, no claim. Citation format: plain text `relative/path/file.ext:start-end` (relative to `reference/`).
- **Roles do not share context.** Each subagent dispatch gets its own isolated context. The critic in particular must not see the producer's chain-of-thought.
- **Reports are append-only after integration.** After `integrated_at:` is set, CYCLE.md content is not edited. (Repairer may edit pre-integration; bounded by repair authority.)
- **Commit every cycle, pass or fail.** The integrator commits + pushes. Atomic operation: artifact + scaffolding + log + book output as one commit.
- **Push after every commit.** `git commit ... && git push origin main` chained. No commits sitting locally between turns.
- **Spec growth is monotonic and visible in `git log`.** Realized as CYCLE.md proposed-changes blocks parsed by the integrator.
- **If a step is ambiguous, stop and ask the human.** Don't improvise around the spec.

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

## Target system

**AWS Labs Palace** — <https://github.com/awslabs/palace>. C++ (~85% of tree), CMake ≥ 3.24, MFEM + libCEED + MPI + BLAS/LAPACK + optional CUDA/ROCm.

- Many symbols resolve into upstream libraries (MFEM, libCEED). Specialized agents cite Palace source, not vendored upstream. If a question requires upstream behavior, log as open question.
- Heavy C++ templates — read tightened regions; prefer narrow text-search before reading.

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

Current skills (post-pilot-1):
- `classify-variant-axis`
- `verify-citation-range`
- `skill-selection`
- `verify-refinement-surface`
- `plan-sideways-concept-emission`
- `embed-and-persist-subagent-dispatch` (pilot-1)

## Models

- `cycle-planner` — `claude-haiku-4-5-20251001` (cheap routing).
- All other agents — `claude-opus-4-7`.

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
