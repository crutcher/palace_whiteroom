# Design: integration-plan accumulation, not git-merge unification

**Captured:** 2026-05-23 (during meta-review #5 enactment).
**Status:** future-design note, not enacted. Phase 8 prerequisite.
**Origin:** user observation: *"What if the scattered agents accumulated integration plans; which were then integrated serially? As they are instructed to collect cross-cutting concerns, they seem likely to generate merge conflicts. Perhaps unification shouldn't be being done via git merge."*

## The problem

The current orchestrator (`config.toml`'s `max_parallel_slices = 1`) runs cycles **serially**. Each cycle commits before the next starts. No merge conflicts arise because there is no concurrency.

Phase 8 (per `BOOTSTRAP.md`) introduces parallel slices: multiple cycles operating on different slices concurrently. The current commit model has each cycle write to **cycle-owned paths**:

- `episodic.jsonl` — append-only; concurrent appends conflict on file lock or interleave per-line (mostly tolerable).
- `LOG.md` — prepended; concurrent prepends conflict on the `---` anchor.
- `lessons.md` — append-only; concurrent appends mostly tolerable.
- `book/src/spec/slices/<slice>.md` — per-slice; **safe** for parallel writes since each cycle owns its slice.
- `book/src/concepts/<concept>.md` — **shared** across slices; concurrent cycles that touch the same concept conflict.
- `book/src/concepts/dependency-map.md` — **shared**; every concept addition updates it.
- `problems/<timestamp>.md` — per-filename; safe.
- `scaffolding/concept-dependency-map.md` — shared WIP version; concurrent writes conflict.

The shared paths (`concepts/<concept>.md`, `dependency-map.md`, `lessons.md`, `LOG.md`, `scaffolding/concept-dependency-map.md`) are exactly the **cross-cutting integration surface** that the methodology is designed to accumulate on. They are also the paths that will conflict under parallel cycles.

Git merge handles textual conflicts via line-diff alignment. It does NOT handle **semantic** integration: "ensure node X exists in this mermaid graph", "append this lesson if not already present", "merge these two additions to a concept's *Levels* section without duplicating the existing prose". Git's union-merge driver helps for append-only files (lessons.md), but graph updates and concept-page edits need semantic awareness git doesn't have.

## User's proposal

> "Scattered agents accumulated integration plans, which were then integrated serially."

Instead of each agent committing its own changes:

1. Each agent emits an **integration plan**: a structured description of what it wants to add / change to shared paths. Not a raw diff — a *plan*.
2. The orchestrator (or a dedicated integrator role) processes plans serially.
3. The serial integration applies plans in order, resolving cross-cutting concerns semantically.

This sidesteps git-merge conflicts entirely: agents never write to shared paths directly; they describe their intended additions; the integrator writes.

## Sketch of the architecture

A possible shape for integration plans:

```json
{
  "slice_writes": [
    {"path": "book/src/spec/slices/gmres/step.md", "file_creates": "...", "diff": "..."}
  ],
  "concept_writes": [
    {"name": "arnoldi_step", "create_if_missing": true, "body": "..."},
    {"name": "rotation", "add_section_at": "after:Working Notes", "body": "..."}
  ],
  "dependency_map_edges": [
    {"layer": "L1", "from": "arnoldi_step", "to": ["matvec", "dot", "axpy"]}
  ],
  "lessons": [
    "When ..."
  ],
  "log_entry": {"cycle_id": N, "headline": "...", "body": "..."}
}
```

The integrator's responsibilities:

- **Idempotent merges.** If two parallel cycles both add the `axpy` concept, the integrator detects the duplicate and uses one canonical version (or surfaces the conflict to meta-review).
- **Semantic graph edits.** "Add edge X→Y" is idempotent; two plans both adding the edge produce one edge, not a duplicate.
- **Append-with-dedupe for lessons.** Identical lessons collapse; near-duplicates surface as friction.
- **LOG.md prepend with proper ordering.** All cycles' LOG entries get prepended in cycle-id order, not file-arrival order.
- **Concept-section merging.** Two plans proposing additions to the *same* concept page at *different* anchor points are merged side-by-side; same anchor → flagged as a conflict for the integrator (or for meta-review) to resolve.

## What this is NOT

- **Not a database.** The repo still holds plain markdown files; the integrator just writes them coherently. No structured store; no schema migration; no query layer.
- **Not a CRDT.** Plans are structured but not necessarily commutative — order matters in some cases (e.g., second plan extending a section the first created). The integrator's serial-application order is the resolution mechanism.
- **Not a replacement for the current commit-per-cycle discipline.** In the serial case (current state), the integrator is a pass-through. The architecture is forward-compatible.

## When this becomes load-bearing

- **Now (serial cycles):** the current direct-write model works. Integration plans are unnecessary overhead.
- **Phase 8 (parallel slices, N>1):** integration plans become necessary. Without them, parallel runs either conflict (git merge breaks) or block on shared-file locks (serializing the very thing parallelism was supposed to enable).
- **Multi-host distributed runs (post-Phase 8):** integration plans + serial integrator + git is approximately a write-conflict-free distributed system. Comparable architectures: event sourcing with a single projector.

## Concrete next steps when this is enacted

(For the future Phase 8 implementer or a meta-review that decides to land this.)

1. **Define the integration-plan schema** as `schemas/integration_plan.json`. Validate Synthesizer output against it.
2. **Refactor `call_synthesizer`** to return an integration plan (or to be invoked by an integrator that builds the plan from claims + slice writes).
3. **Add the integrator** as either:
   - A new orchestrator subsystem (probably right; minimal authority change).
   - A new agent role (likely overkill; the integrator's work is mechanical given the plan).
4. **Update `prompts/synthesizer.md`** to describe the new output shape: instead of `{diff, file_creates, rotation_claims}`, the Synthesizer emits `{slice_writes, concept_writes, dependency_map_edges, lessons, log_entry, rotation_claims}` (integration plan).
5. **Critic feedback channel.** When the integrator detects a cross-cycle conflict (e.g., two plans proposing different bodies for the same concept page section), surface as a friction signal that the next meta-review aggregates.

## Why this isn't enacted now

1. **No friction yet.** Serial cycles don't generate conflicts. The methodology principle "friction-from-use" says to wait for the real problem.
2. **Substantial refactor.** Schema, orchestrator subsystem, Synthesizer prompt, plus all integrator logic. Probably 500-1000 LOC + new tests.
3. **Phase 8 is not the current focus.** Phase 6 (smoke test) is still in progress; Phases 7 (execution grounding) and 8 (parallel slices) come after.

## Related concepts and observations

- The user's `constructed-operators.md` observation, the carry-through clause, and now this integration-plan thinking are **the user's third methodology-architecture contribution** in this session. Pattern: human supplies architectural shapes the Meta-Critic alone doesn't generate (it integrates friction signals it sees; it doesn't propose architectures that don't already have friction). This is consistent with the "human as active participant in methodology evolution" framing.
- The `book/src/concepts/dependency-map.md` file's maintenance protocol (Synthesizer updates it when emitting a new concept) is **most likely to be the first conflict point** under parallel cycles. Two cycles each adding a new concept = two writes to the same map. Worth treating dependency-map.md as the canary if Phase 8 lands before this.
- The Meta-Critic's recent terminology drift around "SIDEWAYS" (meta-review #4 called three FORWARDs "SIDEWAYS") is unrelated but suggests Meta-Critic prompts may need explicit project-structure context. Mentioned here only because a similar prompt update would benefit the integrator (the integrator role, if it exists, would need to know which files are shared vs. per-slice).
