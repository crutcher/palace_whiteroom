# MIGRATION.md

Working plan for migrating from the current loop (Python orchestrator + slice-vertical artifact) to the new shape (Claude-subagent coordination + L4→L0 layered artifact with themed lowering passes). **Draft — iterate.**

## 1. What we're leaving

### Agent flow

- Python orchestrator under `orchestrator/` invoking the Anthropic SDK directly.
- 6 prompted roles (Planner, Explorer, Synthesizer, Critic per-cycle; Meta-Critic + README Builder meta-cycle).
- 4 push kinds (forward, back, sideways, refinement) + orchestrator-driven escalate.
- Integration-plan architecture with channels: slice_writes, concept_writes, section_appends, file_edits, slice_index_updates, dependency_map_edges, lessons, log_synthesis, rotation_claims, skill_uptake.
- Integrator phase pipeline: SIDEWAYS auto-rewrite, same-cycle create+edit merge, H1→H2 normalization, append-by-slug fallback, retroactive-budget hard gate (per-slice ≥3, global ≥4 → retry-once with addendum then escalate), refinement surface-or-evidence gate, forward-edge claims-require-surface, plan_kind misclassification capture, bookkeeping vs substantive failure classification.
- 5 skills under `skills/`: classify-variant-axis, verify-citation-range, skill-selection, verify-refinement-surface, plan-sideways-concept-emission.
- 15 numbered Critic checks + structured `skill_uptake` field.
- 25 meta-reviews of accumulated methodology, immutable under `book/src/meta-reviews/`.
- problems/ channel with self-tuning sensitivity (1–5 scale, currently 3 under relaxed bar).
- log/ per-cycle and per-meta files + README index.
- episodic.jsonl structured per-cycle record.

### Artifact

- ~10 active **slices** at varying layer depths under `book/src/spec/slices/`, each owning its own L0/L1/L2/L3/L4 progression.
- ~28 concepts under `book/src/concepts/`, plus a dep-map and an index.
- L4 calculus strawman under `book/src/design/l4_calculus.md` (v0.3).
- Each slice carries citations to Palace source as L0; each layer transition has explicit rotation_claims with file:line evidence.

## 2. What we're going to

### Artifact (new structure)

- **Layered L4→L0**, not slice-vertical. **Each layer and each lowering layer is its own mdBook Part** with multiple chapters. Nine Parts total:
  ```
  book/src/L4/             - L4 layer: simulation framework + utility combinators
    index.md               (Part overview chapter — orientation, semantics, dep-map)
    <operator>.md          (one chapter per operator)
  book/src/L4-L3/          - L4>L3 lowering, batched by themes
    index.md               (Part overview)
    <theme>.md             (one chapter per theme)
  book/src/L3/             - L3 layer
  book/src/L3-L2/          - L3>L2 lowering
  book/src/L2/             - L2 layer
  book/src/L2-L1/          - L2>L1 lowering
  book/src/L1/             - L1 layer
  book/src/L1-L0/          - L1>L0 lowering
  book/src/L0/             - L0: cited Palace source ranges (the lowered output)
  ```
- **The Part/Chapter shape is load-bearing.** A single index.md per layer accumulates context unboundedly — the Part lets per-operator and per-theme chapters carry their own context, with cross-references between chapters. As a layer's `index.md` exceeds ~200 lines, the semantics overlay and dep-map split into dedicated chapters (`semantics.md`, `dep-map.md`) under the same Part.
- Each **L_n** layer Part: `index.md` (overview) + one chapter per operator. The layer-intro-author writes the index; harvester writes operator chapters.
- Each **L_{n+1}>L_n** lowering layer Part: `index.md` (overview) + one chapter per theme. The layer-intro-author writes the index; abstractor writes theme chapters; lifter refactors them; lowering-verifier audits them.
- **Roughed-in entries** at higher layers permitted as draft options before downstream use; unified/rewritten/formalized/pruned as semantics firm up.
- L4 is a **compiler-frontend target**: high-order combinators, state monads, immutable tensors. Lowering substitutes combinators in (and they disappear from the lowered code), inlines, optimizes.
- **No 1:1 L0↔L4 correspondence** — the relationship is the lowering relation, not point-wise rotation. Citations remain evidence (cited ranges support a lowering claim), but a single L4 combinator may produce many L0 fragments and a single L0 fragment may be the lowered residue of multiple L4 combinator applications.
- The slice corpus (cg, gmres, orthog, ...) becomes **raw material** to mine for shared combinators at each layer — not finalized vertical specs.

### Agent flow (new)

- **Pure Claude Code subagent machinery**: invoke subagents via the `Agent` tool with `subagent_type` parameter, or custom `.claude/agents/<name>.md` definitions.
- **No Python orchestrator process**. The main Claude session coordinates: dispatches subagents for layer work, applies their output to disk, manages git commits/pushes.
- **Local tools allowed**. MCP codemap server (Rust, tree-sitter) stays as a tool subagents can call. Other purpose-built tools under `tools/` continue to apply.
- **Skills**: built-in Skill machinery (the existing SKILL.md format is Claude-Code-compatible already). Subagents invoke skills directly.
- **Per-subagent context isolation** preserves the "no shared context between roles" invariant the orchestrator's role separation provided.

### Agent role philosophy

**Many small focused agents, not a few large generalist ones.** Each agent has a narrow remit and produces a small integratable change per invocation. The goal is incremental evolution that migrates slowly through the stack — finer-grained change cadence than the current 12-cycle meta windows.

Tradeoff: more agents to define and maintain, more coordination overhead from the main session. Payoff: each invocation lands a small reviewable change, parallel-dispatch possibilities increase, and refinement (per the L_{n+1}-rough-in → formalize → re-lift pattern from Section 2 above) maps naturally to dedicated agents per pipeline stage.

### Cycle structure: plan → dispatch → critique → repair → integrate → meta

An R&D cycle has six phases. Serial-scatter-scatter-scatter-serial-serial:

```
  ┌──────────────┐   ┌────────────────────┐   ┌────────────────────┐   ┌────────────────────┐   ┌────────────┐   ┌────────────┐
  │ cycle-planner│ ► │ N sub-agents        │ ► │ N critics           │ ► │ N repairers         │ ► │ integrator │ ► │ meta-phase │
  │   (serial)   │   │ (scatter; writes    │   │ (scatter; runs      │   │ (scatter; reads     │   │  (serial)  │   │  (serial)  │
  │              │   │  CYCLE.md)         │   │  checkers; finds    │   │  META; attempts     │   │ apply +    │   │ examine,   │
  │              │   │                     │   │  problems; writes   │   │  in-place fixes;    │   │ rebuild +  │   │ record,    │
  │              │   │                     │   │  META.md critique   │   │  updates REPORT     │   │ book-fix + │   │ propose,   │
  │              │   │                     │   │  section)           │   │  + META repair      │   │ commit +   │   │ judge,     │
  │              │   │                     │   │                     │   │  section)           │   │ push       │   │ decide     │
  └──────────────┘   └────────────────────┘   └────────────────────┘   └────────────────────┘   └────────────┘   └────────────┘
```

The critic pass is sub-divided into two stages — **critique** (find problems) and **repair** (try to fix the found problems in place). Both run scatter/gather, one invocation per report. The split decouples *detection* (cheap, parallel, exhaustive) from *fix-attempt* (more expensive, narrower in authority, may need multiple checker findings as input).

#### Pre-dispatch: serial planning

A single **cycle-planner** invocation runs first. Inputs:

- **R&D goals** — `scaffolding/roadmap.md` (coarse map of what's in scope) + the L4→L0 layer stack's gaps and partial states.
- **Recent task-firing rates** — counts of recent reports by agent type (read `reports/` index). Used to balance the dispatch and prevent any one agent from dominating.
- **Priority list** — a curated short list of next-up items. Lives at `scaffolding/priorities.md` (new — accumulates from open-questions in prior reports, user direction, and meta-review findings).

Output: a **dispatch plan** (itself written as a report under `reports/<timestamp>-cycle-planner-<id>/CYCLE.md`). The plan contains:

- A list of `(agent, scope, deps)` tuples — N R&D passes for this cycle.
- An **overlap analysis** establishing that the dispatched chunks are non-overlapping (directly OR through immediate dependencies). Two reports overlap if they propose changes to the same file region, OR if one's proposed-change depends on a not-yet-formalized operator the other proposes.
- A **sequencing schedule** — which dispatches can run in parallel; which must be sequential (because one depends on another's report).

#### Dispatch: sub-agents producing reports

Per the plan, the main session invokes the chosen sub-agents:

- Parallel where the plan permits (`Agent` tool calls in a single message).
- Sequential where the plan requires it (one agent's report feeds another's input).

Each sub-agent writes its CYCLE.md (and any supporting docs) to its own `reports/<timestamp>-<agent>-<scope>/` subdirectory. **No artifact mutation.** Reports accumulate.

#### Critique: scatter/gather problem-finding, one critic per report

For each report written during dispatch, a **critic agent** runs in parallel. The critic reads the CYCLE.md (and any supporting docs in the same directory) and runs a checklist of cross-check / critique tasks — the things we want enforced as true. Output: a co-located **`META.md`** in the same report directory containing the **critique section** with per-check pass/warning/fail and a list of concrete problems.

```
reports/
  2026-05-26T143012Z-abstractor-L1-L0-fusion/
    CYCLE.md                       (the sub-agent's proposed changes)
    META.md                         (the critic + repair results)
    evidence-cg-cycle-128.md
    proposed-lowering-draft.md
```

The critic is **distinct from the integrator** and does **no artifact mutation** and **no fix-attempts**. Critique is purely analytic: "what is wrong with this report?" The repair agent (next phase) handles fix-attempts; the integrator handles application. Separating concerns avoids the orchestrator's old pattern where validation and application were intertwined in `_apply_integration_plan`.

The critic's checklist is the new home for the methodology's accumulated correctness rules — most of the 15 Critic checks generalize as per-report checks:

- Citation validity (citation-does-not-support, verify-citation-range skill)
- Surface-or-evidence (refinement reports have either surface edits or retroactive evidence)
- Rotation quality (state hiding / coarser substitution / threaded-state compression)
- Variant-axis classification coverage (classify-variant-axis skill output present when applicable)
- Cross-reference integrity (links to other concepts/slices/reports resolve)
- Edge-label fidelity (rotation_claim's edge matches the prose layer being discussed)
- Plan-kind consistency (declared plan_kind matches the report's proposed-change content)
- Skill-uptake survey (skills-selection skill output present for the report's content shape)

Scatter pattern: one critic invocation per report, run in parallel across all reports written this cycle. The critic appends to META.md (creating it if absent). It does **not** set `overall_status` — that's the repair agent's call after the fix-attempt pass.

#### Repair: scatter/gather fix-attempts, one repairer per report

For each report with a non-empty critique (any check at `warning` or `fail`), a **repairer agent** runs in parallel. The repairer reads CYCLE.md + the critique section of META.md, and for each found problem decides whether it is repairable in-place.

**Repair authority is bounded.** The repairer is for mechanical, surgical, and small-scope fixes — not substantive content authorship. Examples of what's in scope:

- Missing citation that the source range trivially supports (the original agent forgot to copy the line range).
- Citation line range off by a small offset (a few lines slip).
- Forgotten dep-map entry where the new operator is clearly named in the prose.
- Missing append-by-slug hint where the slug is obvious from context.
- H1→H2 normalization when a section reuses the page heading.
- A `concept_writes` proposal for an existing concept slug (auto-rewrite to `section_appends`).
- Trivial cross-reference fix (broken `[link]` to a renamed file).
- Edge-label fix where the rotation_claim names L_{n+1}→L_n but the prose is L_n→L_{n-1}.

Examples of what's **out of scope** for the repairer (left as `unrepairable` for the next cycle's planner to route):

- Missing surface for a refinement claim (substantive authoring required).
- Missing rotation-quality argument.
- Missing variant-axis classification when the axes themselves aren't clearly enumerable from the prose.
- Contradictions between the report and existing artifact content (the repairer doesn't decide which side wins).
- Methodology-level concerns the critic flagged that need meta-phase attention.

For each problem, the repairer either:

1. **Repaired** — applies the fix in-place to CYCLE.md (or its supporting docs in the same directory), and records the repair attempt + new status in META.md's `repair` section.
2. **Unrepairable** — leaves the problem as found, records the reason in META.md's `repair` section, and (when applicable) names a `follow_up_agent` to dispatch in a future cycle.

After the repair pass, the repairer sets `overall_status`:

- `ready` — all critique findings either passed originally or were repaired.
- `needs-revision` — at least one finding is `unrepairable` and the report can't go in as-is; `follow_up_agent` names who should re-do or extend.
- `reject` — the report is structurally wrong in a way that's not worth revising (rare).

##### META.md format (critique + repair sections)

```markdown
---
verifies: ../CYCLE.md                     # always present; relative path
critiqued_at: 2026-05-26T14:32:08Z
critic_version: 1                          # which version of the checklist
repaired_at: 2026-05-26T14:35:12Z          # null if no repair pass ran
repairer_version: 1
checks:                                    # per-check status from critique
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: warning
  cross-reference-integrity: fail
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repairs:                                   # per-finding fix-attempt outcomes
  cross-reference-integrity: repaired
  variant-axis-coverage: repaired
  skill-uptake-survey: unrepairable
overall_status: needs-revision             # set by repairer: ready | needs-revision | reject
follow_up_agent: harvester                 # named by repairer when needs-revision
---

# META: <verification of REPORT title>

## Critique

### Checks run

[per-check detail — what was checked, what was found, why pass/warning/fail; one short paragraph per check]

### Issues found

[concrete issues — what, where in the report, severity]

## Repair

### Fixes attempted

[per-finding: what was attempted, what was changed (file:line in the report or supporting doc), outcome (repaired / unrepairable + reason)]

### Unrepairable findings

[the residue — what couldn't be fixed and why. The integrator reads this to know what the deferral covers; the next cycle's planner reads it to route follow-ups.]

## Suggested resolution

[if `needs-revision`: what action the follow_up_agent should take.
 if `reject`: why this report should not be applied at all.
 if `ready`: optional notes for the integrator (e.g., "apply after report X" if there's a soft dependency)]

## Cross-references

[other reports this verification depends on or relates to]
```

##### Why split critique from repair

- **Different authority profiles.** The critic can be aggressive about flagging things; the repairer's bar for *fixing* is much tighter. Conflating them risks either under-flagging (so repair gates the critique) or over-fixing (so the critic-as-fixer makes substantive content changes).
- **Different prompts.** Critic prompt is a long checklist (the methodology's 15 checks); repair prompt is a fix-attempt skill set (mechanical edits, no authorship). Easier to evolve separately.
- **Different parallelism characteristics.** All reports run their critique; only reports *with findings* run repair. The repair-fanout is data-dependent.
- **Cleaner audit trail.** META.md shows both what was wrong AND what was fixed AND what couldn't be — distinct from the integrator's downstream apply/defer/reject decision.

##### Integrator's relationship to META.md

The integrator reads each report's co-located META.md before deciding:

- `overall_status: ready` → apply the (possibly-repaired) report's proposed changes.
- `overall_status: needs-revision` → defer; the integrator records the deferral in its batch report; the next cycle's planner picks up the named `follow_up_agent` to fix.
- `overall_status: reject` → do not apply; mark the report `rejected` with the META's reason in the integration commit.

The integrator's own gates (the orchestrator's carried-over surface-or-evidence, retroactive-budget, etc.) remain as a final safety net — anything caught there is a critic-checklist gap to surface for the next meta-phase.

#### Integrate: serial application + rebuild + commit/push

A single **integrator** invocation runs after verification. It:

- Discovers all reports written this cycle (and any unintegrated reports from prior cycles).
- Reads each report's co-located META.md for the verifier's overall_status.
- For `ready` reports: parses proposed-changes, applies them.
- For `needs-revision` reports: defers, records the follow-up routing.
- For `reject` reports: marks rejected, does not apply.
- Resolves remaining conflicts (in principle minimal because the cycle-planner enforces non-overlap and the verifiers catch most issues, but the integrator's gates remain as the final safety net).
- **Rebuilds the book** (`cargo make book`).
- **Repairs build failures** (most commonly: broken cross-references from new content) — small surgical fixes; broader issues are surfaced as meta-phase input.
- **Commits and pushes** the applied changes + book rebuild output as a single atomic operation. One commit per cycle is the norm; multiple smaller commits when the cycle's work is bundle-distinct.
- Marks each consumed report with `integrated_at: …` / `integration_commit: …` frontmatter.
- Emits its own batch report under `reports/<timestamp>-integrator-cycle-<n>/CYCLE.md` describing what landed, what deferred, what rejected, what build-repair was needed.

#### Meta-phase: serial methodology examination

A single **meta-phase** invocation runs last. It examines the cycle's evidence — conflict signals from the cycle-planner, problems and open-questions from sub-agent REPORTs, warnings/failures from verifier METAs, deferrals/rejections from the integrator batch report — and aligns them against project goals (roadmap, priority list).

Process — strict ordering, decisions only after analysis:

1. **Examine evidence.** Parse this cycle's reports + METAs + integrator batch. Read prior meta-phase reports to establish baseline.
2. **Record escalating trends.** Compare this cycle's signals against the running history. A recurrence count incrementing on the same pattern is the primary signal. (Replaces the old loop's "recurrence #N" tracking from meta-reviews.)
3. **Propose plans.** Draft methodology adjustments: agent-prompt edits, skill additions, channel-shape changes, tooling adjustments, priority-list updates.
4. **Judge plans.** Filter — drop speculative or under-evidenced ones, sharpen unclear ones, prioritize the actionable ones.
5. **Decide per plan**: `go` / `no-go` / `ask`.

##### Decision semantics

- **go** — enact the change directly. Meta-phase has authority over the methodology surface: edits agent prompts (`.claude/agents/<name>.md`), edits skills (`skills/*/SKILL.md`), edits channel-shape conventions (CYCLE.md format spec, META.md checklist), updates the priority list (`scaffolding/priorities.md`). The change ships in the meta-phase's own commit at end of phase.
- **no-go** — explicit decision NOT to enact, with recorded reason. Distinct from ignoring the signal: a `no-go` says "we considered this and decided against." Future cycles see the `no-go` in the meta-phase report history.
- **ask** — escalate to human. For (a) tooling adjustments that require code changes (orchestrator helpers if any survive, MCP server, build infrastructure); (b) high-cascade methodology changes that exceed meta-phase authority (introducing new agent roles, restructuring the layer stack, changing the cycle structure itself); (c) anything where the evidence is real but the right action is genuinely uncertain.

##### Meta-phase write authority

Meta-phase writes to:

- `.claude/agents/<name>.md` (agent definitions = task prompts).
- `skills/<name>/SKILL.md` (skill content).
- `scaffolding/priorities.md` (priority list updates).
- The CYCLE.md and META.md format specs (channel-shape changes; these live as embedded specs in this MIGRATION.md or graduate to a `docs/report-format.md`).

Meta-phase does NOT write to:

- `book/`, `scaffolding/roadmap.md`, or anything else the integrator owns.
- Code (`orchestrator/`, `mcp/codemap/`, `tools/`) — tooling adjustments are `ask`-decisions.

##### Output

A meta-phase report under `reports/<timestamp>-meta-phase-cycle-<n>/CYCLE.md`:

- Evidence examined (sources, count of signals per type).
- Escalating trends recorded (named patterns, recurrence counts, comparison against prior meta-phase observations).
- Plans proposed (with one-line per plan).
- Per-plan judgment (drop / sharpen / keep).
- Per-kept-plan decision (go / no-go / ask) with reason.
- Enacted changes summary (what was written to `.claude/agents/`, `skills/`, `scaffolding/priorities.md`).
- Open `ask` items surfaced for the human.

The meta-phase commits its enacted changes in a separate commit from the integrator's artifact commit, so the methodology-change history is distinct from the artifact-change history.

#### Why this shape

- **Serial planning** ensures overlap is reasoned about up front; we don't discover conflicts at integration time.
- **Parallel dispatch** is the leverage point for sub-agent authoring — N agents can work simultaneously on disjoint chunks.
- **Parallel critique** is the leverage point for correctness detection — N critics run independent checklists per report. Detection is exhaustive and parallel.
- **Parallel repair** is the leverage point for low-cost fixes — most reports need at most a few mechanical touch-ups; running them per-report in parallel keeps cycle latency bounded. Repair is decoupled from application: an unrepairable finding flags the report for revision but doesn't block reports that did repair cleanly.
- **Serial integration** preserves atomicity: one commit per cycle for the artifact, with a clean cause-chain through the consumed reports. Book rebuild + repair fold in here so the published artifact stays self-consistent.
- **Serial meta-phase** keeps methodology adjustments deliberate: examine → record → propose → judge → decide, in that order. Meta-phase authority is scoped (prompts, skills, channels, priorities) so its mutations don't mix with artifact mutations from the integrator.

The cycle granularity is tunable — the cycle-planner can dispatch 1 agent (an effectively serial cycle) or N agents (highly parallel) based on what the priority list and overlap analysis admit. Meta-phase runs every cycle; most cycles will produce minimal meta output (nothing escalating, nothing to enact) — that's the steady state.

### Friction capture and trend tracking

The old loop captured friction in many overlapping channels (`episodic.jsonl` `friction_observed`/`push_back_signals`, `lessons.md`, `problems/`, meta-review records, Working Notes, `bookkeeping_incomplete`, `plan_kind_misclassification`). Two design goals went **under-realized**:

1. **Cross-cycle pattern integration**. Recurrence counts (`recurrence #N`) lived inside meta-review records — every meta-review had to re-derive them by re-reading prior records. No standing ledger.
2. **Friction → action**. Friction was recorded but the path from "we observed X 6 times" to "we did Y about it" was meta-review-only, which fired every 12 cycles. Most observed friction never reached action.

The new flow consolidates into **two running ledgers** under `scaffolding/`:

- **`scaffolding/friction-ledger.md`** — running list of NAMED friction patterns. One section per pattern with: slug, first-observed cycle, last-observed cycle, recurrence count, status (`new` / `recurring` / `escalating` / `addressed` / `resolved`), short description, and pointers to evidence (report IDs, commit shas). **Meta-phase appends and updates** this every cycle. **Cycle-planner reads** it as a primary priority input — recurring-but-unaddressed patterns get scheduling priority.

- **`scaffolding/cycle-record.jsonl`** (replaces `episodic.jsonl`) — per-cycle structured row appended by **integrator** (post-batch) and **meta-phase** (post-decisions). Fields: cycle-id, timestamp, dispatch counts by agent type, critic finding counts by check, repair outcome counts (repaired/unrepairable), integration counts (ready/deferred/rejected), meta-phase decision counts (go/no-go/ask), token usage. This is the structured record analog of the old `episodic.jsonl`; trend computation runs on it.

Friction signal flow per cycle:

```
sub-agents      → CYCLE.md "Open questions / caveats"
critic          → META.md critique section
repairer        → META.md repair section (unrepairable findings = friction)
integrator      → batch CYCLE.md (gate-hits, deferrals, rejections)
                       ↓
            meta-phase reads all of the above
                       ↓
       friction-ledger.md updated  +  cycle-record.jsonl appended
```

The **aggregation step** is what closes the loop. Without meta-phase synthesizing scattered signals into a single named-pattern ledger, friction signals decay into individual report bodies that nobody re-reads.

#### Replacing the old loop's friction artifacts

- **`lessons.md` (old)** — append-only Critic-authored narrative. Migrate content into `friction-ledger.md` as initial named patterns. Going forward, the friction-ledger replaces it (named patterns + recurrence counts are sharper than prose).
- **`questions.md` (old)** — open/closed question ledger. Replace with **`scaffolding/open-questions.md`** — appendable by any agent surfacing a question, closed by integrator or meta-phase when resolved. Per-report CYCLE.md "Open questions / caveats" sections **feed into** this ledger (the integrator promotes them on landing).
- **`episodic.jsonl` (old)** — replaced by `cycle-record.jsonl` (same shape, new fields).
- **`problems/` (kept)** — out-of-band concerns channel with self-tuning sensitivity. The sensitivity calibration becomes a meta-phase responsibility (it already was, just under the old name).

### Skill development and formation

The old loop **under-formed skills**: 5 skills across 170+ cycles and 25 meta-reviews. The mechanism limited skill formation by design:

1. Per-cycle agents observed procedural patterns but could only describe them in `lessons.md` (prose) or `Working Notes` (per-slice).
2. Only Meta-Critic could promote → SKILL.md, and only at meta-review cadence (12 cycles).
3. The +60% skill-priority directive (meta-19) was a prompt-engineering patch trying to overcome the structural under-bias.

The new flow addresses this in **three structural ways**:

1. **Open skill-candidate channel.** `scaffolding/skill-candidates.md` is **appendable by any agent** that notices a procedural pattern worth crystallizing. Sub-agents, critic, repairer, integrator — all can propose. One section per candidate: slug, proposer (agent + cycle), motivating observation (one paragraph), sketch of procedure (one paragraph), status (`proposed` / `evaluating` / `promoted` / `deferred` / `rejected`). Meta-phase reads this each cycle as the **primary skill-promotion signal**.

2. **Skill-invocation telemetry.** When an agent invokes a skill, the CYCLE.md may carry a `skill_uptake` field (same idea as the old `skill_uptake_summary`): which skill, did it help (`applied` / `inapplicable` / `fell-short`), what was the gap. Meta-phase aggregates this in `cycle-record.jsonl`. Skills with high `fell-short` counts get refined; skills with high `inapplicable-but-invoked` counts get scope-tightened in their prompt.

3. **Per-cycle meta-phase consideration.** No 12-cycle wait. Meta-phase considers `skill-candidates.md` every cycle and promotes when the bar is met. The bar should be intentionally **low**:
   - Default-accept procedural patterns observed ≥2 cycles unless there's a specific reason against.
   - The cost of a too-eager promotion is a few unused SKILL.md files; the cost of under-promotion is missed pattern capture across many cycles.
   - This matches the user-confirmed default: "Small-scope speculative skills are default-accepted."

Skill lifecycle:

```
proposed (any agent appends to skill-candidates.md)
    ↓ (meta-phase: pattern observed ≥2× or candidate sketch is concrete)
promoted (meta-phase writes skills/<slug>/SKILL.md; candidate status = "promoted")
    ↓ (agents invoke; uptake telemetry accumulates in cycle-record.jsonl)
refined (meta-phase edits SKILL.md when telemetry surfaces gaps)
    ↓ OR
retired (meta-phase moves to skills/_retired/<slug>/ with retirement reason)
```

**Retirement matters.** The old loop never retired anything; if a skill became irrelevant it just stayed. The new flow explicitly retires (with reason) so the active set stays focused.

### Scaffolding layout

Scaffolding is the agent-side workshop — cumulative state that lives between cycles. The new layout:

```
scaffolding/
  README.md                 # index (one-liner per file/dir)
  roadmap.md                # relative-progress vs roadmap (integrator-maintained)
  priorities.md             # short next-up list (meta-phase + cycle-planner co-edit)
  friction-ledger.md        # named friction patterns + recurrence (meta-phase-maintained; new)
  skill-candidates.md       # appendable skill proposals (any-agent appendable; new)
  open-questions.md         # open question ledger (replaces questions.md; any-appendable)
  cycle-record.jsonl        # per-cycle structured record (replaces episodic.jsonl)
  decisions/                # persistent-dual trade-offs (sub-agent appendable)
    <topic>.md
  test-linkages/            # source→test maps (sub-agent appendable)
    README.md
    <topic>.md
  problems-sensitivity.md   # self-tuning sensitivity calibration (meta-phase-maintained)
```

Read/write matrix:

| Agent | Reads | Writes |
|---|---|---|
| cycle-planner | roadmap, priorities, friction-ledger, open-questions, cycle-record (tail), integrator batch reports (last N cycles) | — |
| 8 specialized | decisions/, test-linkages/ (per scope), open-questions (relevant) | (only their own report dir; may append to skill-candidates.md, open-questions.md, decisions/, test-linkages/) |
| critic | (the report it's critiquing) | META.md critique section; **may append to** skill-candidates.md if pattern observed |
| repairer | CYCLE.md, META.md critique | META.md repair section + CYCLE.md in-place fixes; **may append to** skill-candidates.md |
| integrator | reports + METAs | book/, roadmap.md, cycle-record.jsonl (append), open-questions.md (close-on-landing), log/ |
| meta-phase | scaffolding/ (all), reports/ (this cycle's + tail), prior meta-phase reports | priorities, friction-ledger, skill-candidates (refine status), cycle-record.jsonl (append decisions), problems-sensitivity, `.claude/agents/`, `skills/` |

**The "any-agent-appendable" docs** (`skill-candidates.md`, `open-questions.md`, `decisions/`, `test-linkages/`) are exceptions to strict report-channel discipline. They're cumulative state, not per-cycle artifacts. Discipline: agents **append a section**, never edit existing sections. Promotion / refinement / retirement is meta-phase or integrator work.

### Validation gates: current → new home

The Python orchestrator's `_apply_integration_plan` carries ~12 validation gates accumulated over 25 meta-reviews. Each gate's authority partitions cleanly into critique vs repair vs integrator-safety-net:

| Gate (current orchestrator) | New home | Notes |
|---|---|---|
| Citation-does-not-support | **critic** check | Pure detection; repair can't author missing citations |
| Surface-or-evidence (refinement) | **critic** check | Unrepairable if both missing — substantive authoring required |
| Retroactive-budget (per-slice ≥3, global ≥4) | **critic** check + **integrator** safety net | Critic finds threshold breach; integrator's cap remains as last-line |
| SIDEWAYS auto-rewrite (≥3 `concept_writes` → `section_appends`) | **repairer** auto-fix | Mechanical rewrite — squarely in repair scope |
| H1→H2 normalization | **repairer** auto-fix | Mechanical — repair |
| Concept-existence-check (write on existing slug → rewrite to append) | **repairer** auto-fix | Mechanical — repair |
| Edge-label fidelity | **critic** check + **repairer** auto-fix when prose is clear | Detect; mechanical-fix if edge is unambiguous from prose |
| Plan-kind misclassification capture | **critic** check | Detection only; deciding correct kind is substantive |
| Bookkeeping-vs-substantive failure classification | **repairer** routing logic | Drives `follow_up_agent` selection |
| Append-by-slug fallback | **repairer** auto-fix | Mechanical |
| Forward-edge claims-require-surface | **critic** check | Substantive; unrepairable |
| Variant-axis classification coverage | **critic** check + **repairer** auto-fix if axes clear from prose | Detect; mechanical-add only if obvious |
| Skill-uptake survey (`skill_uptake` field) | **critic** check (presence) + **cycle-record.jsonl** (telemetry) | Surfaces telemetry, not blocking |

**Integrator runs every check one more time** as a safety net (in case critic missed or repairer over-fixed). Anything caught at the integrator level is a critic-coverage gap → meta-phase records in friction-ledger → critic prompt refined next cycle.

### Orphaned-artifact prevention

Audit rules so every artifact has a known consumer:

- **CYCLE.md "Open questions / caveats" sections** → integrator **promotes to** `scaffolding/open-questions.md` on landing. The cycle-planner consumes the ledger.
- **Critic warnings** (non-failing) → if not repaired, the **integrator** records them in `cycle-record.jsonl` warning counts. Meta-phase scans for warning-pattern accumulations and lifts persistent warning patterns into friction-ledger entries.
- **Meta-phase `no-go` decisions** → recorded in `scaffolding/friction-ledger.md` against the matching pattern (status: `addressed` with `no-go: <reason>`). Future meta-phases read the ledger before re-proposing.
- **Integrator batch reports** → consumed by **meta-phase** (for the cycle's gate-hits and deferral reasons) AND by **next cycle's cycle-planner** (for what deferred + needs follow-up).
- **Lowering-verifier's audit linkages** → land as metadata in the relevant `book/src/L_{n+1}-L_n/` lowering rule entries (per-rule `verified_against:` field). Cross-layer-cross-cutter reads them for coverage analysis.
- **Reports themselves** (post-integration) → audit trail only; not re-read. Stays on disk indefinitely (research record). Same discipline as commit history.

If any agent writes something that doesn't appear in this list, that's a new orphan — either route it (add to this section), or remove it.

### Report channel + single integrator

**Subagents do not edit the artifact directly.** All specialized agents (the 8 in Phase C) write only to a non-overlapping report channel under `reports/`. Each invocation gets its own subdirectory (`reports/<timestamp>-<agent>-<scope>/`) containing a `CYCLE.md` and any supporting documentation. Subagents have **no write access** to `book/`, `scaffolding/`, `skills/`, `prompts/`, or any other artifact area.

**A single unified integrator agent** is the sole writer of the artifact. The integrator's job:

1. Discover pending reports under `reports/` (any subdirectory without `integrated_at:` frontmatter).
2. Parse each report's proposed-changes section.
3. Apply changes to the artifact (book/, scaffolding/, etc.).
4. Handle conflicts between concurrent reports (multiple agents proposing changes to the same file, or proposing contradictory operator definitions).
5. Run validation — the equivalent of the current orchestrator's gates: surface-or-evidence, retroactive-budget, SIDEWAYS auto-rewrite, H1→H2 normalization, concept-existence check, etc.
6. Commit + push (matching the current push-after-commit discipline).
7. Mark each integrated report by adding `integrated_at: ${timestamp}`, `integration_commit: ${sha}`, and `integration_notes: …` to its frontmatter. Reports stay on disk as a research record — never deleted.

This separation eliminates the multi-writer coordination problem entirely. Specialized agents can run in parallel without locking; the integrator serializes their effects on the artifact.

#### Report directory layout

```
reports/
  README.md                                          (index, newest-first)
  2026-05-26T143012Z-abstractor-L1-L0-fusion/
    CYCLE.md                                        (frontmatter + proposed changes)
    evidence-cg-cycle-128.md                         (optional supporting docs)
    proposed-lowering-draft.md
  2026-05-26T143515Z-combinator-miner-krylov-step/
    CYCLE.md
    pattern-evidence.md
  2026-05-26T144203Z-harvester-arnoldi-step/
    CYCLE.md
    operator-spec.md
  2026-05-26T150811Z-integrator-batch-1/
    CYCLE.md                                        (integrator's own report: which reports consumed, what landed, what deferred)
```

After integration, the consumed reports gain frontmatter updates in-place; they're not moved. The integrator emits its own report describing the batch.

#### CYCLE.md format

```markdown
---
agent: abstractor                     # which agent emitted this
invoked_at: 2026-05-26T14:30:12Z
invoked_by: <session-id-or-human>
scope: L1>L0 lowering theme — fusion of axpy+dot chains
inputs:
  - book/src/L0/                      # what the subagent read
  - reference/palace/linalg/cg.cpp:42-67
status: pending                       # pending | integrated | rejected | superseded
integrated_at: null                   # set by integrator on apply
integration_commit: null              # set by integrator on commit
integration_notes: null               # integrator's notes (deferrals, conflicts, mods)
---

# REPORT: <one-line title>

## Summary
2–4 sentences. What this report proposes.

## Proposed changes
Structured. Either inline file edits (path + old_string + new_string per edit, or
section-append + content) OR free-prose description of changes the integrator should
make. Structured is preferred; integrator parses it.

## Supporting evidence
Citations, cross-references, links to other reports, pointers to supporting docs in
this report's own directory.

## Open questions / caveats
Things the subagent surfaces but cannot resolve in its narrow scope. The integrator
may route these to follow-up agent invocations.
```

#### Integrator authority and discipline

- **The integrator does NOT author original content.** It applies changes proposed by specialized agents. If the integrator notices that a proposed change is incomplete or contradicted by another report, it surfaces the issue in its own CYCLE.md and either defers (status: deferred) or rejects (status: rejected) the relevant subagent reports.
- **The integrator runs validation gates** before committing. The current orchestrator's gates (refinement surface-or-evidence, retroactive-budget, SIDEWAYS auto-rewrite, concept-existence-check, edge-label fidelity, etc.) become integrator validation rules. If a proposed change trips a gate, the integrator either applies an auto-fix (e.g., H1→H2 normalization, concept-existence-rewrite) or rejects the report with a clear reason.
- **The integrator commits + pushes** each batch. One commit per integrator invocation typically; the commit message names the reports consumed.

## 3. What stays

- **Reference checkouts** (`reference/palace/`, `reference/mfem/`, etc.) — local source-of-truth.
- **MCP codemap server** (`mcp/codemap/`) — Rust + tree-sitter tool, usable by any subagent via MCP.
- **mdBook output format** (`book.toml`, `cargo make book`, `cargo make book-serve`).
- **scaffolding/** workshop area (cross-cutting notes, decisions, roadmap).
- **problems/** channel (drive-by observations + out-of-role concerns) — sensitivity self-tuning concept may simplify under the new flow.
- **Methodology concepts** (`rotation`, `variant-absorption`, `constructed-operators`, `solve-monad`, `state-stratification`, `derived-view-hoisting`, `sequential-obstruction`, `tensor-field-lift`, `negative-result-slice`) — adapt content for the layer-not-slice framing but the ideas persist.
- **Skills** (`skills/*/SKILL.md`) — most carry over directly; framings around slice-vertical work need updating but the procedures (classify-variant-axis, verify-citation-range, plan-sideways-concept-emission, verify-refinement-surface, skill-selection) all apply.
- **L4 calculus draft** under `book/src/design/l4_calculus.md` — promote / fold into the new L4 layer document.
- **Meta-review records** (`book/src/meta-reviews/`) — immutable history; the methodology arc is part of the deliverable's audit trail.
- **log/** + **episodic.jsonl** — keep but possibly simplify; the new flow has fewer/larger work units, so per-cycle granularity may collapse to per-session.

## 4. What needs to change in the methodology surface

- **Per-slice prompt rules → per-layer prompt rules**. The Synthesizer prompt today is shaped around "advance this slice from L_n to L_{n+1}"; the new shape is "draft this operator at L_n" or "write the L_{n+1}>L_n lowering theme for X".
- **Critic checks (15)** were shaped around per-claim rotation_claim verification with file:line citation. Most generalize: citation-does-not-support, mutation-pattern-mismatch, missing-case, rotation-quality, variant-absorption, prose-rotation-alignment, setup-state-schema — all apply with light reframing. Some become irrelevant: per-building-block claim granularity is a slice-vertical concern.
- **Rotation_claim** itself — currently point-wise edge-bounded (`from_form → to_form` on a named edge with a single citation) — becomes a **lowering-rule claim**: "this lowering theme rewrites L_{n+1} forms of shape A into L_n forms of shape B, evidenced by these L_n cited ranges and these L_{n+1} reference instances." Many-to-many, not point-wise.
- **Push kinds**: forward/back/sideways/refinement collapse. New work shapes:
  - **Operator-draft**: rough or formalize an operator at L_n.
  - **Lowering-theme**: write or refine a theme in L_{n+1}>L_n.
  - **Lowering-instance**: test the L_{n+1}>L_n lowering against a specific L0 pattern (the equivalent of the current "verify a slice's L_{n+1}→L_n rotation").
  - **Cross-theme unification**: notice two themes share structure; consolidate.
  - **Pruning**: a roughed-in operator turned out not to be load-bearing; remove it.
- **Meta-review** survives as out-of-cycle friction integration but trigger needs rethink (was 12-cycle, what's a cycle now?). Candidate: time-based or work-volume-based; or human-triggered with an automatic friction-buildup warning.
- **Skills** — most carry over. Replace slice-specific language with layer-specific. `classify-variant-axis` becomes layer-agnostic (variant axes appear at every layer); `verify-refinement-surface` generalizes to "verify a lowering-rule has surface at both ends".
- **Friction signals are now first-class scaffolding artifacts**, not buried in `lessons.md` prose. The friction-ledger / skill-candidates / open-questions / cycle-record / problems-sensitivity files are **running state** the meta-phase reads and edits each cycle. Section 2 *Scaffolding layout* defines the read/write matrix.
- **Producers can propose skills** (skill-candidates.md is any-agent appendable). The old single-author-promotion bottleneck is gone.
- **Validation gates** map cleanly to critic / repairer / integrator phases — see Section 2 *Validation gates*.

## 5. Migration plan

### Phase A: design & alignment (THIS phase)

- Iterate on MIGRATION.md until you're confident in the target structure.
- Decide concrete file-layout names (`book/src/L4-L3/` vs `book/src/lowering/L4-L3/` vs flat).
- Decide what becomes of the existing slice corpus: archive in-place, move to `corpus/`, or interleave as a "phase-1 raw material" appendix.
- Decide subagent shape: 1 generalist or specialized layer-author / lowering-author / combinator-extractor / critic-equivalent agents.
- Surface open questions to resolve before any restructuring touches disk.

### Phase B: artifact skeleton + scaffolding bootstrap

**Artifact skeleton:**
- Build the new `book/src/L4/`, `book/src/L4-L3/`, … `book/src/L0/` directory layout with stub intro+dep-map per layer.
- Move existing slice content to `book/src/_phase1_corpus/` (or similar) — preserved as raw material, not deleted.
- Move existing concepts to a new layer-indexed structure OR keep flat (`book/src/concepts/`) and add layer-tags to each.
- Promote `design/l4_calculus.md` content into `book/src/L4/` intro + initial operator list.
- mdBook SUMMARY.md rewritten for the new TOC.

**Scaffolding bootstrap** (the running ledgers per Section 2 *Scaffolding layout*):
- Create `scaffolding/friction-ledger.md` and **seed it** from `lessons.md` (extract named patterns from the 100+ accumulated lessons; each becomes a friction-ledger entry with status `recurring` or `addressed`). The old `lessons.md` stays in place as historical record but becomes read-only.
- Create `scaffolding/skill-candidates.md` empty. Optionally seed a few candidates from observed-but-unrealized patterns in recent meta-reviews.
- Create `scaffolding/open-questions.md` and migrate the currently-open entries from `questions.md`. Closed entries stay archived in `questions.md` for the record.
- Rename `episodic.jsonl` → `scaffolding/cycle-record.jsonl` (move the file, no schema change initially; meta-phase prompts will reference the new path). Add a one-line README pointer at the old path.
- `scaffolding/problems-sensitivity.md` carries over verbatim — its current calibration history is valuable.
- `scaffolding/decisions/` and `scaffolding/test-linkages/` carry over.
- Update `scaffolding/README.md` index to reflect the new layout.

Single commit per phase milestone (artifact skeleton commit; scaffolding bootstrap commit) so the audit trail is clean.

### Phase C: subagent definitions

Define custom agents under `.claude/agents/`. Each agent definition: Claude-Code frontmatter (name, description, tools allowlist, model) + system prompt body adapted from current role prompts. Skills (`skills/`) referenced from agent prompts; built-in Skill machinery invokes them. MCP codemap server registration stays as-is — agents call MCP tools normally.

The roles are split fine-grained to follow the small-agent philosophy (per Section 2 *Agent role philosophy*). Each agent's "produce a small integratable change per invocation" means roughly one operator drafted, one lowering theme refined, one pattern proposed, or one observation surfaced.

#### Layer authoring (L_n layer documents)

- **`layer-intro-author.md`** — writes and maintains an L_n layer's introduction, semantics overview, and dep-map structure. The "shell" of the layer document; doesn't author individual operator definitions.
- **`harvester.md`** — takes a single roughed-in operator at L_n and **formalizes it**: definition, signature, algebraic laws, applicability. Promotes speculative entries to firm ones. Cleans up existing operator definitions when needed. **One operator per invocation.** Source material for the harvester comes from abstractor output, combinator-miner proposals, or cross-cutter observations.

#### Lowering pipeline (the rough-in → formalize → re-lift flow)

Three agents form the lowering authoring pipeline, mirroring the "roughed-in entries refined through use" principle:

- **`abstractor.md`** — looks at **L_n evidence** (existing L_n prose or, for L_1>L_0, raw Palace source), and **sketches an L_{n+1}>L_n lowering theme with speculative L_{n+1} abstractions**. Operates upward from evidence. The speculated L_{n+1} abstractions are **rough-in** placeholders — they don't need to exist yet as formalized operators. Output: a draft lowering theme + a list of speculative L_{n+1} operators that the theme would need.
- **`harvester.md`** (above) — consumes abstractor output (and other sources). Formalizes each speculative L_{n+1} operator into a proper L_{n+1} entry. Produces firm operator definitions to land in the L_{n+1} layer document.
- **`lifter.md`** — once L_{n+1} is formalized (post-harvester), **re-anchors the existing L_{n+1}>L_n lowering specs** to use the formalized vocabulary. Pure rewriting pass: the lowering's structure stays, only the vocabulary is firmed up. **One lowering theme per invocation.**

Validation:

- **`lowering-verifier.md`** — **verifies a lowering rule** against concrete L_n or L_0 evidence. Checks: does the L_n form on the right-hand side actually appear in cited evidence? does the rewrite preserve semantics? are the applicability conditions complete? Doesn't author content; only audits. The Critic-equivalent for the new flow.

#### Pattern recognition

- **`combinator-miner.md`** — scans the existing slice corpus + Palace source + the partial new artifact for **recurrent patterns**. Proposes whether each pattern should become a combinator **at this layer or the next higher layer** (the level decision is part of the proposal). Emits candidate operator proposals with provenance — handed off to `harvester` for formalization. **One pattern proposal per invocation.**

#### Cross-cutting (split into intra-layer and inter-layer)

- **`same-layer-cross-cutter.md`** — compares existing components **on the same level** for unification opportunities, redundancy, contradictions, and shared sub-patterns. Surfaces observations; doesn't enact unifications directly. **One observation per invocation.**
- **`cross-layer-cross-cutter.md`** — looks **up and down the stack** for coverage gaps, edge-label mismatches, missing lowerings for some L_{n+1} operator, consistency drift between layers. Surfaces observations; flags candidates for combinator-miner or lifter follow-up. **One observation per invocation.**

#### Reconciling overlaps

All 8 specialized agents write **only** to their own report subdirectory under `reports/`. The artifact (book/, scaffolding/, skills/, prompts/) is touched only by the **integrator** (see *Report channel + single integrator* in Section 2). The **critic** writes META.md (critique section only); the **repairer** writes META.md repair section AND may apply in-place fixes to CYCLE.md / supporting docs in the same directory.

The discipline is *one report per invocation per agent*, with the main session sequencing dispatches and the integrator serializing applications:

| Concern | abstractor | harvester | lifter | combinator-miner | same-layer | cross-layer | lowering-verifier |
|---|---|---|---|---|---|---|---|
| Drafts new lowering | ✓ | | | | | | |
| Adds L_{n+1} operator | | ✓ | | | | | |
| Refactors existing lowering | | | ✓ | | | | |
| Proposes pattern → combinator | | | | ✓ | | | |
| Notices same-level redundancy | | | | | ✓ | | |
| Notices cross-level mismatch | | | | | | ✓ | |
| Audits lowering claim against evidence (during dispatch) | | | | | | | ✓ |

Combinator-miner's report is a *proposal*; harvester reads it and emits a *formalization* report. Same-layer-cross-cutter emits an *observation* report; the main session decides which downstream agent to dispatch in response. The integrator consumes all of these and lands the actual artifact changes.

#### The 9th–13th agents: cycle-planner, critic, repairer, integrator, meta-phase

- **`cycle-planner.md`** — runs first in every cycle. Reads R&D goals (roadmap, layer-stack gaps), recent task-firing rates (counts of recent reports by agent type), and the priority list (`scaffolding/priorities.md`). Emits a dispatch plan as a report: `(agent, scope, deps)` tuples + overlap analysis + sequencing schedule. Does NOT mutate the artifact. Output report under `reports/<timestamp>-cycle-planner-<id>/CYCLE.md`.
- **`critic.md`** — runs once per report written during dispatch (scatter/gather). Reads the CYCLE.md and any co-located supporting docs; runs the critique checklist (citation validity, surface-or-evidence, rotation quality, variant-axis coverage, cross-reference integrity, edge-label fidelity, plan-kind consistency, skill-uptake survey). Writes the **critique section** of a co-located META.md with per-check status and concrete problems found. **Does NOT mutate the artifact, does NOT mutate CYCLE.md, does NOT attempt fixes, does NOT set `overall_status`** — META.md critique section is its only write.
- **`repairer.md`** — runs once per report whose META.md critique contains any warning or fail (scatter/gather). Reads CYCLE.md + META.md critique section. For each finding, decides repairable vs unrepairable per the bounded-authority rules in Section 2 *Repair*. Applies in-place fixes to CYCLE.md (or its supporting docs in the same directory) for repairable findings. Writes the **repair section** of META.md recording per-finding outcomes. Sets `overall_status` (ready / needs-revision / reject) + `follow_up_agent` routing. **Does NOT mutate the artifact** (book/, etc.).
- **`integrator.md`** — runs after repair. Sole writer of `book/` and `scaffolding/roadmap.md`. Reads pending reports + their META.md `overall_status`; applies `ready` ones, defers `needs-revision` ones, marks `reject` ones. Runs the orchestrator's old gates as a final safety net. Rebuilds book, repairs link-check / format breakage, commits + pushes. Marks consumed reports with `integrated_at` / `integration_commit` frontmatter. Emits its own batch report.
- **`meta-phase.md`** — runs after integration. Sole writer of `.claude/agents/`, `skills/`, `scaffolding/priorities.md`, and channel-format specs. Examines cycle evidence (planner conflicts, sub-agent open-questions, critic warnings/failures, unrepairable-finding patterns, integrator deferrals/rejections), records escalating trends against prior meta-phase history, proposes methodology adjustments, judges them, and decides go / no-go / ask per plan. `go` items are enacted directly in a separate methodology commit; `ask` items surface to the human. Output report under `reports/<timestamp>-meta-phase-cycle-<n>/CYCLE.md`.

Total agent count: **13** (cycle-planner + 8 specialized + critic + repairer + integrator + meta-phase).

Write-authority partition:

| Agent | Writes to |
|---|---|
| 8 specialized | `reports/<id>/CYCLE.md` + supporting docs in same dir |
| critic | `reports/<id>/META.md` (critique section only) |
| repairer | `reports/<id>/META.md` (repair section + `overall_status`), in-place edits to `reports/<id>/CYCLE.md` and supporting docs |
| integrator | `book/`, `scaffolding/roadmap.md`, log/, episodic.jsonl |
| meta-phase | `.claude/agents/`, `skills/`, `scaffolding/priorities.md`, channel-format specs |
| cycle-planner | `reports/<id>/CYCLE.md` (its own plan report) |

Note the repairer is the **only** agent (besides the specialized sub-agents themselves) with write authority to CYCLE.md / supporting docs in the report channel. This is bounded by the repair authority rules in Section 2 *Repair* — mechanical and surgical fixes only.

### Phase D: orchestrator decommission

- Stop running `orchestrator/`. The Python code stays in repo as historical reference (gitignored from build) — useful for understanding what discipline the loop encoded.
- Main Claude session takes over **dispatch coordination**: invokes subagents via `Agent` tool, decides routing between specialized agents based on incoming reports, decides when to invoke the integrator. Does NOT itself write to the artifact.
- The Python orchestrator's `_apply_integration_plan` function is the closest analog to the new **integrator agent**. The integrator carries over the validation logic (surface-or-evidence, retroactive-budget, SIDEWAYS auto-rewrite, concept-existence, edge-label fidelity, H1→H2 normalization, append-by-slug fallback) — same gates, different host. The integrator's prompt encodes them.
- The integration-plan JSON schema becomes a CYCLE.md proposed-changes convention. Integrator parses proposed-changes sections; subagents emit them per the format spec.

### Phase E: methodology document refresh

- CLAUDE.md rewrite for the new flow: layer-not-slice, subagent-not-orchestrator, the recovered-high-order-form deliverable framing.
- BOOTSTRAP.md frozen as the historical record of how the original loop came up; the new flow doesn't bootstrap via Phases 0–9+.
- Skills updated where the framing depended on slice-vertical work.
- meta-reviews/ index page updated to note the methodology transition.

### Phase F: pilot

- Pick 1–2 lowering themes (e.g., "in-place axpby mutation under state-monad threading"; "loop-recurrence → tensor-field op for embarrassingly-parallel fields").
- Use the new subagent flow to: draft the L4 operators those themes use; write the L4>L3 lowering for one theme; verify against the existing CG and GMRES slice content; iterate.
- The pilot's friction surfaces the next round of methodology adjustments.

**Pilot exit checklist** (don't move to Phase G until satisfied):
- All 6 phases of the cycle structure fired end-to-end at least 3 times.
- `friction-ledger.md` accumulated ≥3 named patterns from observed pilot friction.
- `skill-candidates.md` accumulated ≥1 candidate proposed by a non-meta-phase agent (validates the producer-channel works).
- Meta-phase shipped ≥1 `go` decision (prompt edit, skill, or priority update) — validates the friction → action path.
- At least 1 repairer auto-fix landed end-to-end (validates the critique/repair split is operational).
- At least 1 `unrepairable` finding got routed to a follow-up cycle and resolved (validates the deferral path).
- The integrator's safety-net gates caught at least one critic-coverage gap, and meta-phase added the missing check to the critic prompt (validates the gate→friction→prompt-refine loop).

If any item doesn't fire during Phase F, that's a pipeline gap — diagnose before scaling to G.

### Phase G: corpus harvest

- Once 1–2 themes are validated end-to-end, systematically harvest the existing slice corpus for combinators and lowering instances.
- Slices that map cleanly to existing combinators get absorbed (their content distributed across layer documents); slices that surface new combinators motivate L4 operator additions.
- Negative-result slices (sparse_triangular_solve) become non-lowering notes — "this L4 form has no L_n lowering because [genuine sequential dependency / Palace doesn't expose this primitive]".

## 6. Open questions

1. **File layout names.** `book/src/L4/` vs `book/src/layers/L4/` vs `book/src/L4-framework/`? Same question for lowering: `L4-L3/` vs `L4_to_L3/` vs `lowering/L4-L3/`.
2. **Slice corpus disposition.** Move to `book/src/_phase1_corpus/`? Keep at `book/src/spec/slices/` with a deprecation note? Move out of `book/src/` entirely to `corpus/`?
3. **Subagent shape — resolved 2026-05-26 user direction.** **13 agents total**: cycle-planner (serial pre-dispatch) + 8 specialized (parallel dispatch, write only to `reports/<id>/CYCLE.md`) + critic (scatter/gather post-dispatch, writes META.md critique section) + repairer (scatter/gather post-critique, writes META.md repair section + in-place fixes to CYCLE.md) + integrator (serial post-repair, writes book/ + roadmap) + meta-phase (serial post-integration, writes `.claude/agents/`, skills/, priorities, channel specs). Cycle structure is plan → dispatch → critique → repair → integrate → meta (Section 2 *Cycle structure*). The 8 specialized agents: layer-intro-author, harvester, abstractor, lifter, lowering-verifier (a domain-specific check during dispatch, distinct from the per-report critic), combinator-miner, same-layer-cross-cutter, cross-layer-cross-cutter. Open sub-questions: (a) bootstrap order — 13 at once or in phases? (b) cycle trigger — human-invoked vs periodic? (c) critic checklist as single agent vs multiple narrow critic-agents (verify-citations, verify-surface, verify-variant-axis, …) running in parallel per report? Lean single-agent-with-checklist for first pass; split if any single check needs its own context. (d) lowering-verifier (during dispatch — domain-specific evidence audit) vs critic (post-dispatch — checklist-based critique) — distinct or merge? Lean distinct: lowering-verifier authors content (audits + records evidence linkages); critic only finds problems. (e) repair-authority boundaries — when does a fix-attempt become "substantive authoring"? Worked examples in Section 2 *Repair* define the bar but edge cases will emerge during pilot. (f) meta-phase write-authority for `prompts/` — under the new flow, agent definitions live in `.claude/agents/` (not `prompts/`); the old `prompts/` becomes documentation only.
4. **Cycle semantics — partially resolved 2026-05-26.** A cycle = (one cycle-planner invocation) + (N sub-agent invocations producing reports per the plan) + (one integrator invocation). The cycle is the natural unit because the cycle-planner reasons about non-overlap across the N dispatches. Open sub-questions: (a) how is a cycle triggered (human-driven, time-based, work-volume-based)? (b) where does the priority list (`scaffolding/priorities.md`) get updated — manually, or by an end-of-cycle agent that scans the integrator's report for follow-up candidates? (c) episodic.jsonl per-cycle record: keep similar shape (one row per cycle with plan + dispatched + integrated counts), or evolve?
5. **Meta-review trigger — resolved 2026-05-26.** Meta-phase runs **every cycle**, as the sixth phase after integration. Most cycles will produce a minimal meta-phase output (nothing escalating, nothing to enact) — that's the steady state. The 12-cycle batched meta-review pattern is gone; methodology friction integrates continuously. Open sub-question: do we need a "deep meta-review" trigger for occasional cross-cutting passes that span dozens of cycles? Lean no — every-cycle meta-phase with running-history awareness covers it.
6. **Per-cycle commit discipline.** The orchestrator commits + pushes after every cycle. The new flow could commit after every subagent return, every meaningful operation, or only at session-end checkpoints. Tradeoff: granularity vs noise.
7. **Critic checks → critic/repairer mapping — partially resolved.** Section 2 *Validation gates* tabulates the 12 known orchestrator gates and their new homes. Open sub-question: are there gates implicit in the orchestrator code (not enumerated as 15-Critic-check items) that this table misses? Audit `orchestrator/orchestrator.py` `_apply_integration_plan` line-by-line during Phase D.
8. **problems/ sensitivity self-tuning — resolved 2026-05-26.** Becomes meta-phase responsibility. `scaffolding/problems-sensitivity.md` (already exists) carries over; meta-phase recalibrates per cycle using `cycle-record.jsonl` problem-filing rates. Open sub-question: target rate of 1/15 was tuned under the slice-based agent count; under the new flow with N specialized agents per cycle, the denominator changes — recalibrate the target during pilot.
9. **Integration-plan discipline — partially resolved.** Becomes the **CYCLE.md proposed-changes section** format. Open sub-question: structured-YAML/JSON within the markdown (more parseable for the integrator) vs free-form structured-markdown (more flexible for agents to write, requires integrator-side parsing). Lean toward structured fenced blocks inside markdown so the integrator gets parseable data and the agent gets natural-prose surrounding context.
10. **Skill format.** Stays SKILL.md? Claude-Code-native or our extended frontmatter? The two should be compatible already.
11. **Repo restructuring atomicity.** Do we keep the old orchestrator working alongside the new flow during transition, or hard-cut? Hard-cut is cleaner; coexistence allows verification.
12. **Tooling carry-over.** MCP codemap clearly stays. The Python orchestrator's `state.py` helpers (read_problems_sensitivity, list_refinement_candidates, etc.) — port to a `tools/` helper script the main session can call, or rewrite as needed?
13. **Ledger formats.** `friction-ledger.md` and `skill-candidates.md` are new — should they be free-prose markdown (easier to read/edit), structured-markdown with YAML frontmatter per section (parseable but more rigid), or JSONL (purely structured)? Lean structured-markdown with frontmatter per section: agents can scan with grep, meta-phase can parse via straightforward regex, humans can read top-down.
14. **`open-questions.md` vs REPORT-level open-questions.** Two layers: per-report caveats inside CYCLE.md (rich context) and global ledger in scaffolding (cross-cycle visibility). The integrator promotes per-report items into the ledger on landing. Open sub-question: does **every** REPORT caveat get promoted, or only those the integrator flags as cross-cutting? Lean every — under-promoting hides signal; over-promoting just gives meta-phase more to scan.
15. **`scaffolding/decisions/` and `test-linkages/` migration.** Existing under the old loop. Carry over verbatim or restructure for the layer-not-slice framing? Lean carry-over; the layer framing affects file *names* under these dirs more than the dirs themselves.

## 7. Risks and tensions

- **Losing structured integration-plan discipline — partially mitigated.** The integrator agent carries the gates forward (same logic, different host); structured proposed-changes blocks in CYCLE.md preserve parseability. Residual risk: the new integrator agent's prompt is substantial (carries all 10+ gates from the current orchestrator's `_apply_integration_plan` function) — verify it implements them correctly during Phase F pilot before harvesting at scale.
- **Critic-check distillation.** The 15 checks are a corpus of hard-won validation logic. Reframing them as main-session rules risks losing nuance; keeping them verbatim risks carrying slice-specific framings into a layer-shaped world.
- **Recovery from in-flight bad work.** The orchestrator commits per cycle and the integrator catches structural defects atomically. The new flow needs equivalent atomicity (probably: main-session checkpoint commits + manual rollback when subagent output looks broken).
- **Loss of episodic data continuity.** episodic.jsonl is 197+ entries deep; it's a research record. The new `cycle-record.jsonl` should mirror the old fields where compatible and add the new ones; longitudinal analysis can union both files as a single stream. Don't break the contract that "one cycle = one row."
- **Cost / time profile changes.** Per-cycle was many small API calls; subagent invocations are bigger but rarer. Net cost may be similar or lower; latency probably higher per work unit.
- **Methodology refresh burden.** CLAUDE.md is ~340 lines of accumulated direction; rewriting for the new flow is a substantial standalone effort. Could do it incrementally as the new flow proves itself, or up-front as part of Phase E.
- **Friction-signal fragmentation risk.** Multi-channel friction capture worked in the old loop because meta-review integrated across channels every 12 cycles. The new flow's friction-ledger is meant to be the single source of truth — but it depends on meta-phase aggregating discipline. If meta-phase skimps on the synthesis step ("nothing escalating today"), signals fragment back into individual report bodies. **Mitigation**: meta-phase prompt enforces ledger updates each cycle, even when no `go` decisions ship. Cycle-record.jsonl counts unrepairable findings; meta-phase must explain why none of them got ledger entries when count > 0.
- **Skill formation under-bias residual risk.** Even with the open candidates channel, agents may still under-propose if their prompts emphasize "complete the task" over "notice a pattern." Mitigation: per-agent prompt template includes a closing "Skill-candidate check" section asking the agent to consider whether anything they just did was procedural-and-recurring. Meta-phase tracks `skill-candidates.md` append rate per agent type; agents with persistently zero appends get prompt-tightening.
- **Ledger maintenance overhead.** Three new running ledgers (friction, skill-candidates, open-questions) plus the cycle-record means meta-phase has substantial bookkeeping each cycle. Risk: bookkeeping crowds out judgment. Mitigation: keep ledger entries SHORT (one-paragraph max per pattern/candidate/question); meta-phase prompt budgets time on bookkeeping vs analysis.
- **Repair authority creep.** "Mechanical and surgical fixes only" is a soft boundary. Over time the repairer may start absorbing more substantive content fixes ("the citation range is off by 30 lines; just fix it"). Mitigation: meta-phase periodically audits the repair section of recent METAs for scope creep; if found, tighten the repairer prompt with anti-patterns.

## 8. What this doc is for

This is a **working plan**, not a commitment. Iterate on it until the structure feels right before touching the artifact tree or the agent flow. Treat as a living document during Phase A; freeze (move into `book/src/meta-reviews/` or similar) once Phase B begins so subsequent phases have a stable reference target.
