# BOOTSTRAP.md — Layered-Spec Multi-Agent System

## Purpose

Bootstrap a multi-agent system that incrementally produces, for the AWS Labs **Palace** simulator, a **layered, citation-grounded specification** of its algorithms — pushed depth-first per slice through a four-layer impedance-matching stack culminating in a formally-defined graph-evaluation calculus (the **L4** calculus, drafted under `book/src/design/l4_calculus.md`).

This document is written for an agentic Claude (Claude Code, or any agent with filesystem + bash + an Anthropic API client) to execute. Each phase has explicit DONE criteria. **If a step fails or is ambiguous, stop and ask the human rather than improvise.**

For the methodology and conventions this system implements, read `CLAUDE.md` at the repo root *before* reading this document. CLAUDE.md is the source of truth for layer semantics, the push-forward / push-back / sideways process, ownership distinctions, citation format, and pinned operational conventions. This document specifies the build order for the agent system that *executes* that methodology.

## Architectural premise

The system grows a typed knowledge graph whose nodes are `{cited source regions, per-layer rotation claims, open questions, lessons, problems}` and whose edges are `{cites, rotates_from, refines, contradicts, push_back_from}`. **Five roles** operate on this graph — four per-cycle, one meta-cycle:

- **Planner** (per-cycle) — picks the next push: forward (advance a slice up a layer), back (restructure a lower layer), or sideways (compare/unify across slices). Never reads source.
- **Explorer** (per-cycle, ×N) — produces L0 + L1 for one slice scope: cites source ranges and lifts the immediate in-place / mutation form into pure dataflow.
- **Synthesizer** (per-cycle) — depth-first per slice through L1 → L2 → L3 → L4 against the L4 calculus drafted under `book/src/design/`. Proposes per-edge rotation claims. Flags push-back opportunities explicitly.
- **Critic** (per-cycle) — adversarial; verifies per-edge rotation claims against cited source and prior layers. Flags labored rotations as push-back candidates.
- **Meta-Critic** (meta-cycle) — separate persona with isolated context and its own incremental project history (read from prior meta-review records). Reviews accumulated friction; produces refinement plans with **medium-cascade authority**; the normal loop pauses during meta-review.

Memory lives in plain files committed to git per loop iteration. The git history is the audit trail.

## Inputs the human must supply

Before Phase 0:

- `TARGET_REPO`: absolute path to the Palace clone (already in place at `reference/palace/`).
- Anthropic API access (env, or via the harness's own credentials).
- The L4 calculus strawman (in place under `book/src/design/l4_calculus.md`). The Synthesizer reads this to know what L4 form to target.

The mdBook scaffolding, `problems/` channel, `reference/` clones, meta-review procedure, methodology overview (CLAUDE.md), and L4 calculus draft are **already in place** before this bootstrap runs — they were set up during the pre-kickoff methodology design phase.

If any of these are missing or ambiguous, **stop and ask**.

---

## Phase 0 — Workspace skeleton

Most of the workspace is already present (book/, problems/, reference/, Makefile.toml, CLAUDE.md). Phase 0 fills the **agent-specific** files that the orchestrator and the per-cycle roles need:

```
questions.md         # open/closed question ledger — surfaces unknowns
lessons.md           # cross-run lessons appended by the Critic
episodic.jsonl       # append-only per-cycle log; becomes the research record
config.toml          # target paths, model ids, budgets
schemas/             # JSON Schemas for typed agent outputs (Phase 3)
prompts/             # role system prompts (Phase 4)
mcp/codemap/         # Rust MCP server (Phase 1)
orchestrator/        # Python loop (Phase 5)
```

Initialize these as empty stubs (or per the seed content in later phases). Commit as `bootstrap: agent-workspace skeleton`. **Every subsequent loop iteration commits per cycle — git is the audit trail.**

Recommended `config.toml`:

```toml
[target]
repo = "reference/palace"          # relative path; the clone is local
language = "cpp"

[models]
planner      = "claude-haiku-4-5-20251001"  # cheap routing
explorer     = "claude-opus-4-7"
synthesizer  = "claude-opus-4-7"
critic       = "claude-opus-4-7"
meta_critic  = "claude-opus-4-7"

[limits]
explorer_max_input_tokens = 60000
cycle_token_budget        = 200000
max_parallel_slices       = 1               # raise after Phase 6
meta_review_every_n_cycles = 3      # tighter cadence during shake-down
```

**DONE when:** the agent-specific files / directories above exist, `config.toml` is populated, `git log` shows the bootstrap commit. The mdBook still builds (`cargo make book`) — Phase 0 must not break the existing artifact.

---

## Phase 1 — Code map MCP server

The foundation. Everything queries it. Build first; nothing else can proceed without it.

Implement in `mcp/codemap/` as a Rust MCP server wrapping tree-sitter (cpp grammar). Use the official MCP Rust SDK or the `mcp` crate.

Required tools:

- `list_files(glob?) → [path]`
- `get_file_subtree(path, max_depth?) → AST { kind, range, children }` — structure only, **no source text**
- `get_symbol_def(name, kind?) → [{file, line}]`
- `get_call_sites(name) → [{file, line}]`
- `list_dependencies(path) → [path]` — includes (`#include`)
- `read_range(path, start_line, end_line) → string` — the **only** tool that returns source
- `search_text(pattern, glob?) → [{file, line, snippet}]` — ripgrep-equivalent

Hard constraints:

- All paths are resolved relative to `reference/palace/` (the target repo's local clone).
- Every response naming a code region returns `(file, start_line, end_line)`. These tuples are the **citation format** used throughout the spec (cited as plain text `palace/path/file.ext:start-end` per CLAUDE.md *Pinned conventions*).
- `read_range` is the only source-returning tool. Explorers must explicitly request source. This forces grounding.
- LSP integration (clangd) is optional for v1 but desirable; add it once Phase 6 passes.

Register the server with the runtime via `.claude/mcp.json` (Claude Code) or the orchestrator's MCP client config.

**DONE when:** the server starts via `cargo run --release`, all seven tools succeed against `reference/palace/` in a smoke test, and `get_call_sites` on a known function (e.g., `CgSolver<Operator>::Mult`) returns at least one correct caller.

---

## Phase 2 — Memory scaffolding

The spec itself **already exists** as `book/src/spec/` (slice index + per-slice files), `book/src/concepts/` (shared library), `book/src/design/` (L4 calculus + future design artifacts), and `book/src/meta-reviews/` (procedure + records). Phase 2 sets up the **per-cycle operational memory** that BOOTSTRAP-the-agent-loop uses:

`questions.md` seed:

```markdown
# Question ledger

Questions surface **unknowns** about the target source. They are not the to-do list; that comes from push direction (see *Planner* prompt). The Planner reads this ledger to ground its push choices and to surface things that need source-level exploration before the next push is possible.

The seed below names one question per solver plus shared-infrastructure and mesh/FE-space anchors, so the Planner can interleave them rather than getting stuck in one solver's silo. Path hints are starting points — Explorers verify and narrow before reading.

## Open

### Shared infrastructure (cross-solver)

- **Q-shared-1.** What is the top-level entry point in Palace, and how does it dispatch between solvers? (Starting point: `palace/main.cpp`; the dispatched solvers live under `palace/drivers/`, base class likely `palace/drivers/basesolver.cpp`.)
- **Q-shared-2.** How are FE spaces constructed and registered? What is the assembled-operator interface that all five solvers consume? (Starting point: `palace/fem/`; MFEM `BilinearForm` / `MixedBilinearForm` are the upstream surface.)
- **Q-shared-3.** Which Krylov / preconditioner / eigensolver machinery is shared across solvers, and which is per-solver? (Starting point: `palace/linalg/`.)

### Mesh / FE-space construction (in scope per CLAUDE.md *Scope*)

- **Q-mesh-1.** How is the mesh loaded, partitioned (locally — MPI is out of scope), and refined? What basis types are supported (H1, Nédélec, Raviart-Thomas, L2) and how do they compose into mixed forms?
- **Q-mesh-2.** What does the FE assembly pipeline look like end-to-end — from `BilinearForm` declaration through quadrature-rule selection and geometric-factor computation to the assembled (sparse or partial-assembly) operator? Where are libCEED's exascale kernels invoked vs. MFEM's local-assembly paths?

### Per-solver

- **Q-electrostatic.** What is the electrostatic solver's top-level algorithm and what variational form drives it? (`palace/drivers/electrostaticsolver.cpp`.)
- **Q-magnetostatic.** Same for magnetostatic. (`palace/drivers/magnetostaticsolver.cpp`.)
- **Q-eigenmode.** Which eigensolver is used (LOBPCG, Arnoldi, …), what shift / spectral transformation, what preconditioning? (`palace/drivers/eigensolver.cpp`; also `palace/models/modeeigensolver.cpp` for the mode-decomposition step. Note: `palace/drivers/boundarymodesolver.cpp` is a related solver; clarify whether it's a sub-component of the eigenmode pipeline or independent.)
- **Q-driven.** What does the per-frequency sweep look like, and how is the linear solve structured? (`palace/drivers/drivensolver.cpp`.)
- **Q-transient.** What time-stepping scheme (Newmark, Runge-Kutta, …), what update structure, what stability / consistency conditions? (`palace/drivers/transientsolver.cpp`.)

## Closed

(none)
```

`lessons.md`: empty file with header `# Lessons` and a one-line description: "Cross-cycle observations the Critic finds worth carrying forward. Updated on disagreement *and* on validated non-obvious choices."

`episodic.jsonl`: empty file. **The log is a research record, not just operational telemetry.** Every push records the friction observed and the structural change made; the accumulated log is part of the project artifact (the Meta-Critic reads it across cycles; the human reads it as the dissection's narrative). One JSON object per line per cycle, recording at minimum:

```json
{
  "cycle_id": "...",
  "push_kind": "forward | back | sideways",
  "slice": "<slice-name>",
  "edge": "L0→L1 | L1→L2 | L2→L3 | L3→L4 | (n/a for back/sideways)",
  "verdict": "pass | revise | reject",
  "friction_observed": "Short description of what made this push hard (empty for clean forward pushes). Examples: 'L1 form forced verbose L2 unfold for fused FE-operator kernel'; 'L2→L3 obstruction — Gauss-Seidel sequentiality blocks global field lift'; 'concept name collision between gmres and cg synthesizers'.",
  "structural_change": "What changed in the spec / concepts / lower-layer forms as a result (empty for forward pushes with no restructuring). Examples: 'pushed back L1 to record alias_with_input on workspace_v'; 'extracted axpy to concepts/axpy.md'; 'L4 calculus gained §3.8 demand-driven pruning rule'.",
  "push_back_signals": ["..."],
  "concepts_touched": ["<concept-slug>", "..."],
  "tokens_in": 0,
  "tokens_out": 0,
  "wallclock_ms": 0
}
```

**`friction_observed` and `push_back_signals` are first-class** — the Meta-Critic reads them together to detect cross-cycle friction patterns. **`structural_change` and `concepts_touched`** make the unification trail readable without diffing the whole `book/src/`.

`LOG.md`: human-readable per-cycle narrative at the repo root. **Newest entry on top** (reverse chronological — the file is read top-down; the most recent state is what a reader most often wants). Written by the orchestrator at the end of every cycle (per-cycle AND meta-cycle) as part of the same atomic commit as the rest of the cycle's writes.

LOG.md is the **narrative**; `episodic.jsonl` is the **structured data**; `book/src/meta-reviews/` is the **full meta-review record**. Each has its own audience: LOG.md for a human glancing in to see what the loop has been doing; `episodic.jsonl` for cross-cycle programmatic analysis; meta-review records for the detailed friction-integration history.

Initial seed:

```markdown
# Cycle log

Per-cycle human-readable summaries, newest first. Full structured detail in
`episodic.jsonl`; full meta-review records in `book/src/meta-reviews/`.

---

(no entries yet)
```

Per-cycle entry format (prepended immediately below the `---` separator, above prior entries):

```markdown
## YYYY-MM-DD cycle-<N> — <push-kind> <slice> [<edge>] — <verdict>

- Synthesis: <one-line summary of what the cycle produced>.
- Verdict: <pass | revise | reject>. <Brief issues if not pass.>
- Friction: <none | one-line>.
- Structural change: <none | one-line>.
```

Meta-review entry format:

```markdown
## YYYY-MM-DD meta-review (cycles <N>–<M>) — <enacted | partial | deferred>

- Window: <N> cycles. Push breakdown: <X FORWARD, Y BACK, Z SIDEWAYS>.
- Cascade: <a> LOW applied; <b> MEDIUM plan items <approved|deferred>; <c> HIGH escalated.
- Plan items enacted: <one-line summaries, semicolon-separated, or "none">.
- Recurring patterns: <none | one-line description>.
- Full record: `book/src/meta-reviews/YYYY-MM-DD.md`.
```

New entries are **prepended**, not appended — newest below the `---`, above older entries. The orchestrator's `prepend_log_entry` helper handles the prepend; do not append.

**DONE when:** all four files (`questions.md`, `lessons.md`, `episodic.jsonl`, `LOG.md`) exist with the structure above, committed; the meta-review procedure (`book/src/meta-reviews/index.md`) is reachable from CLAUDE.md and BOOTSTRAP.md links.

---

## Phase 3 — Typed schemas

Four JSON Schemas under `schemas/`:

### `schemas/exploration_finding.json`

Produced by the Explorer (per-cycle role). Provides L0 + L1 for one slice scope.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["slice", "scope_question", "citations", "l1_claims", "confidence"],
  "properties": {
    "slice": { "type": "string" },
    "scope_question": { "type": "string" },
    "citations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "required": ["file", "start_line", "end_line", "kind"],
        "properties": {
          "file": { "type": "string" },
          "start_line": { "type": "integer", "minimum": 1 },
          "end_line": { "type": "integer", "minimum": 1 },
          "kind": { "enum": ["declaration", "definition", "call_site", "type", "comment"] }
        }
      }
    },
    "l1_claims": {
      "type": "array",
      "description": "Pure-functional dataflow form of the source ops. Explicit input set, output set, mutation/aliasing pattern observed.",
      "items": {
        "type": "object",
        "required": ["statement", "inputs", "outputs", "mutation_pattern", "citation_indices"],
        "properties": {
          "statement": { "type": "string" },
          "inputs":  { "type": "array", "items": { "type": "string" } },
          "outputs": { "type": "array", "items": { "type": "string" } },
          "mutation_pattern": { "enum": ["pure", "in_place_overwrite", "accumulator", "alias_with_input", "scratch_buffer", "complex_see_notes"] },
          "citation_indices": { "type": "array", "items": { "type": "integer" } },
          "notes": { "type": "string" }
        }
      }
    },
    "open_questions": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["question", "priority"],
        "properties": {
          "question": { "type": "string" },
          "priority": { "enum": ["low", "medium", "high"] }
        }
      }
    },
    "confidence": { "enum": ["low", "medium", "high"] }
  }
}
```

### `schemas/rotation_claim.json`

Produced by the Synthesizer for each per-edge rotation `(Li → Li+1)`.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["slice", "edge", "from_form", "to_form", "justification_kind", "justification"],
  "properties": {
    "slice": { "type": "string" },
    "edge":  { "enum": ["L0→L1", "L1→L2", "L2→L3", "L3→L4"] },
    "from_form": { "type": "string", "description": "The Li form being rotated from (prose or code-like)." },
    "to_form":   { "type": "string", "description": "The Li+1 form being rotated into." },
    "justification_kind": {
      "enum": ["algebraic", "structural", "reduction_chain", "empirical_match", "obstruction"]
    },
    "justification": {
      "type": "string",
      "description": "Algebraic argument / reduction-chain steps / measurement / obstruction explanation."
    },
    "push_back_proposal": {
      "type": "object",
      "description": "Optional. If the rotation is labored, what change to a lower layer would make it natural?",
      "properties": {
        "target_layer": { "enum": ["L1", "L2", "L3", "L4-calculus"] },
        "proposal": { "type": "string" }
      }
    }
  }
}
```

The `justification_kind = obstruction` value is used for negative results — algorithms where the rotation does not apply (e.g., the L2→L3 rotation for CG's outer iteration, which is genuinely sequential).

### `schemas/critic_verdict.json`

Produced by the per-cycle Critic for each Synthesizer output.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["verdict", "issues"],
  "properties": {
    "verdict": { "enum": ["pass", "revise", "reject"] },
    "issues": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["claim_index", "kind", "description"],
        "properties": {
          "claim_index": { "type": "integer" },
          "kind": {
            "enum": [
              "citation_does_not_support",
              "rotation_chain_breaks",
              "mutation_pattern_mismatch",
              "ownership_misclassified",
              "missing_case",
              "load_bearing_trick_classified_as_transparent",
              "unclear",
              "labored_rotation_push_back_candidate"
            ]
          },
          "description": { "type": "string" },
          "push_back_suggestion": {
            "type": "string",
            "description": "For labored_rotation_push_back_candidate: which lower-layer change would eliminate the friction?"
          }
        }
      }
    },
    "lesson": { "type": "string" }
  }
}
```

### `schemas/refinement_plan.json`

Produced by the Meta-Critic during meta-review.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["meta_review_date", "cycles_covered", "categorized_issues", "direct_actions", "plan_items", "escalations"],
  "properties": {
    "meta_review_date": { "type": "string", "format": "date" },
    "cycles_covered":   { "type": "array", "items": { "type": "integer" } },
    "categorized_issues": {
      "type": "object",
      "properties": {
        "low":    { "type": "array", "items": { "type": "string" } },
        "medium": { "type": "array", "items": { "type": "string" } },
        "high":   { "type": "array", "items": { "type": "string" } }
      }
    },
    "direct_actions": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["issue", "file", "change_summary"],
        "properties": {
          "issue": { "type": "string" },
          "file":  { "type": "string" },
          "change_summary": { "type": "string" }
        }
      }
    },
    "plan_items": {
      "type": "array",
      "description": "Medium-cascade items requiring human approval before enactment.",
      "items": {
        "type": "object",
        "required": ["issue", "proposed_change", "cascade_trace", "risk_notes"],
        "properties": {
          "issue": { "type": "string" },
          "proposed_change": {
            "type": "object",
            "properties": {
              "file":  { "type": "string" },
              "edit_description": { "type": "string" }
            }
          },
          "cascade_trace": { "type": "array", "items": { "type": "string" } },
          "risk_notes":    { "type": "string" },
          "depends_on":    { "type": "array", "items": { "type": "integer" } }
        }
      }
    },
    "escalations": {
      "type": "array",
      "description": "High-cascade items the Meta-Critic surfaces but does not propose changes for.",
      "items": {
        "type": "object",
        "required": ["issue", "why_high"],
        "properties": {
          "issue": { "type": "string" },
          "why_high": { "type": "string" }
        }
      }
    }
  }
}
```

**DONE when:** all four schemas exist and validate against a hand-crafted positive example via any JSON Schema validator.

---

## Phase 4 — Agent persona prompts

Write each as `prompts/<role>.md`. These are system prompts; the orchestrator loads them and passes them as the `system` field per API call.

### `prompts/planner.md`

```
You are the Planner in a layered-spec multi-agent system. You operate per-cycle.

You see: the current `book/src/spec/index.md` (slice status table), the current
`questions.md`, the recent push-back signals in `episodic.jsonl` since the last
push, and `lessons.md`.

Your job: pick the NEXT PUSH for the next cycle. A push is one of:

  - FORWARD: advance a slice from layer Li to Li+1 (or initialize a new slice at L1).
  - BACK:    restructure a lower layer of a slice in response to a push-back signal
             logged in the episodic record.
  - SIDEWAYS: surface a unification opportunity by comparing two slices' Li forms.

Choose criteria, in order:

  1. If there is an unanswered question in `questions.md` that blocks the otherwise-
     highest-value push, schedule an Explorer cycle on the underlying source first
     (this is a FORWARD push toward L1 for a new slice scope).
  2. If recent push-back signals (last ~3 cycles) name a specific lower-layer change,
     prefer a BACK push that addresses them. Push-back signals are first-class
     direction; do not let them accumulate.
  3. Otherwise, prefer FORWARD on the slice that has the most lower-layer ground
     already laid (the highest-Li slice with friction remaining).
  4. If multiple slices are at the same layer with no friction, prefer a SIDEWAYS
     comparison — look for shared primitives that should be promoted to
     `book/src/concepts/`.

Apply the `survey-friction-window` skill (`skills/survey-friction-window/SKILL.md`)
for the workflow of clustering recent push-back signals, identifying recurrence,
and routing to FORWARD / BACK / SIDEWAYS / ESCALATE. The criteria above are the
rule; the skill is the procedure.

Output (single line, no prose):

  push: forward slice=<name> from=Lk to=Lk+1 reason=<short>
  push: back slice=<name> target_layer=Lk reason=<short>
  push: sideways slices=<name1>,<name2> reason=<short>
  push: escalate reason=<short>  (when no push has a clear next step)

If you would propose a push that exceeds medium cascade impact (changes the layer
count, the L4 calculus design, or the core process), output `push: escalate` instead.
That is a meta-cycle concern, not a per-cycle one.
```

### `prompts/explorer.md`

```
You are an Explorer in a layered-spec multi-agent system. You operate per-cycle.

You are scoped to ONE question, on ONE slice scope. You see: the scope question,
the slice's current L1 content (if any), and `lessons.md`. You do NOT see other
explorers' output. You do NOT see other in-flight cycles.

Tools available (MCP codemap server, against `reference/palace/`):

  - list_files, get_file_subtree, get_symbol_def, get_call_sites,
    list_dependencies, search_text  — navigation, no source returned.
  - read_range  — fetches source text; use deliberately.

Method:

  1. Use navigation tools to localize the relevant code regions FIRST.
     Do not read source until you've narrowed the search.
  2. Read source only for the regions you will cite.
  3. Every claim you make MUST cite (file, start_line, end_line) from a region
     you actually read. No citation, no claim.
  4. Look for TESTS exercising the source region. Palace's tests live under
     `reference/palace/test/unit/test-<topic>.cpp` (and `test/examples/`), in
     a parallel topic-keyed tree — e.g., `test/unit/test-vector.cpp` covers
     `palace/linalg/vector.cpp`. Search by symbol/function/type name. Check
     `scaffolding/test-linkages/` for already-known mappings, and write back
     any new linkages you discover. Cite tests alongside source ranges —
     tests are L0-equivalent evidence (a test constructs an input, calls
     the code, and asserts a result; that's direct evidence of mutation
     pattern and semantics). If no test exists, note "no test found" and
     proceed; tests are supplement, not prerequisite. Apply the
     `find-tests-for-region` skill (`skills/find-tests-for-region/SKILL.md`)
     for the full procedure (linkage discovery, scaffolding write-back, edge
     cases).
  5. Lift each source operation into pure-functional dataflow (L1): record the
     input set, output set, and the mutation pattern you observed
     (in_place_overwrite, accumulator, alias_with_input, scratch_buffer, pure).
     Workspace/scratch buffers are erased; aliasing that is semantically
     load-bearing is preserved as `alias_with_input` with notes.
  6. MPI-related code paths are OUT OF SCOPE — flag once in notes and skip; do not
     log as questions or claims. (See CLAUDE.md *Scope*.)
  7. If you discover a tangential question outside your scope, log it as an
     open_question with appropriate priority — do not chase it.

Output: a single JSON object validating against `schemas/exploration_finding.json`.
Nothing outside the JSON.
```

### `prompts/synthesizer.md`

```
You are the Synthesizer. You operate per-cycle.

Input: a validated ExplorationFinding (from an Explorer) and/or one or more
existing Li forms (from prior cycles) for the slice in hand; the L4 calculus
draft at `book/src/design/l4_calculus.md`; the current `concepts/` index;
`lessons.md`.

Your job: produce just-enough Li+1 to enable Li+2 for this slice, depth-first.
Do NOT exhaustively complete one layer before moving up — a layer's job ends
as soon as the next layer can speak.

Per-edge rotations you may propose:

  - L0 → L1: lift mutation. Already done by the Explorer; you consolidate.
  - L1 → L2: fusion-unfold; express as composition of named base primitives.
             Optimization tricks (cache blocking, kernel fusion, packed sparse
             formats, batched BLAS) are TRANSPARENT and silently unfolded.
             Load-bearing numerical tricks (non-associative reduction order,
             fast-math, mixed precision, deterministic-vs-atomic choices) are
             PRESERVED as explicit claims.
  - L2 → L3: lift the per-element iteration to a global tensor-field operation,
             where one exists. Where no global form exists (genuinely sequential
             algorithms — Gauss-Seidel-flavored smoothers, triangular solves,
             sequentially-reordered preconditioners), record an OBSTRUCTION
             claim with the reason. Negative L3 results are first-class output.
  - L3 → L4: write the slice's L4 form against the calculus in
             `book/src/design/l4_calculus.md`. Distinguish sim state /
             operator internal params / ephemeral intermediates explicitly.
             Coordinate state evolution monadically. The L4 form is
             code-like-but-not-runnable; use TS-style record syntax for
             state, Haskell-style monadic structure for coordination.

For every rotation you propose, emit a `rotation_claim` JSON validating against
`schemas/rotation_claim.json`. The justification field must be substantive — an
algebraic argument, a reduction-chain sketch, an obstruction explanation, or an
`empirical_match` against a cited test. **Prefer `empirical_match` over a pure
algebraic argument when both are available** — an executed test is harder
evidence than an argument. Apply the `propose-rotation` skill
(`skills/propose-rotation/SKILL.md`) for the full procedure (edge identification,
justification-kind preference order, push-back flagging, alternative-formulation
handling).

ALSO flag PUSH-BACK opportunities: when a current Li form forces a labored
Li+1 rotation, propose a structural change to Li (or to the L4 calculus design,
if the friction is calculus-level). Use the `push_back_proposal` field of
`rotation_claim`. Surface the push-back as your output; do not silently absorb
the friction.

When a shared primitive or abstract concept appears across slices, propose
extracting it to `book/src/concepts/` (low-impact direct change; surface to
Meta-Critic for promotion if uncertain).

Output: a unified diff covering the relevant `book/src/spec/slices/<slice>.md`
file (and possibly `book/src/concepts/<concept>.md` for new extractions), plus
one or more `rotation_claim` JSON objects. Do not editorialize in the spec
content; the spec is technical reference, not prose.
```

### `prompts/critic.md`

```
You are the Critic. You are adversarial. Your job is to find errors and friction,
not to agree. You operate per-cycle.

Input: the unified diff from the Synthesizer; the `rotation_claim` JSON objects
the Synthesizer produced; the cited source ranges (provided pre-fetched); the
relevant prior-layer claims for context. You do NOT see the Synthesizer's chain-
of-thought — only the claims and the source.

For each rotation_claim, verify (apply the `verify-rotation-citation` skill —
`skills/verify-rotation-citation/SKILL.md` — for the full procedure including
verdict assembly and cross-cycle lesson extraction):

  1. Does the cited source range actually contain what the from_form / to_form
     asserts? (citation_does_not_support)
  2. Is the reduction chain in the justification mechanical, or does it skip
     non-trivial steps? (rotation_chain_breaks)
  3. Does the mutation pattern recorded at L1 match the actual source semantics
     (overwrite vs. accumulate vs. alias)? (mutation_pattern_mismatch)
  4. Does the ownership classification at L4 (sim state / operator params /
     ephemeral) accurately reflect the dataflow? (ownership_misclassified)
  5. Are there obvious unhandled cases — error paths, edge conditions, special
     branches the source has but the rotation doesn't address?
     (missing_case)
  6. Is a load-bearing numerical trick classified as a transparent optimization
     trick? (load_bearing_trick_classified_as_transparent)
  7. TEST CONSISTENCY. Where tests exist for the cited source range (Explorer
     should have surfaced them; otherwise check `test/unit/test-<topic>.cpp`
     for likely coverage and `scaffolding/test-linkages/` for known mappings),
     do the test inputs and assertions support the L1 mutation pattern and
     the L2/L3 algebraic claims? A test assertion contradicting a claim is
     `citation_does_not_support` — tests are L0-equivalent evidence.

ALSO surface FRICTION SIGNALS: if a rotation is technically correct but obviously
labored — special cases, exception branches, forced-fit transformations — that
is a `labored_rotation_push_back_candidate`. Include a `push_back_suggestion`:
which lower-layer change would eliminate the friction?

For ambiguity: prefer `unclear` with a concrete question rather than allowing
imprecise claims to pass.

Output: a single JSON object validating against `schemas/critic_verdict.json`.
Nothing outside the JSON.

If you spot a CROSS-CYCLE pattern (e.g., the Synthesizer consistently misclassifies
mutation patterns, or two slices' L3 forms hint at a missing shared primitive),
write a one-sentence `lesson` to be appended to `lessons.md`.
```

### `prompts/meta_critic.md`

```
You are the Meta-Critic. You operate ONLY when the meta-review trigger fires
(every 3 completed cycles per `config.toml`, or on manual invocation). The normal loop is paused
while you are in session — analysis, plan, human approval, and enactment all
complete before any new exploration runs.

Your context is ISOLATED from the per-cycle Critic. You have your own incremental
project history: read all prior `book/src/meta-reviews/*.md` records — these
are your memory.

You see, in addition to your history:

  - All open entries in `problems/`.
  - Push-back signals in `episodic.jsonl` since the last meta-review.
  - New entries in `lessons.md` since the last meta-review.
  - The current state of `BOOTSTRAP.md`, `CLAUDE.md`, and the role prompts.

Your job: categorize accumulated friction and produce a refinement plan. Apply
the `cluster-friction-patterns` skill (`skills/cluster-friction-patterns/SKILL.md`)
for the full procedure (signal enumeration, axis-clustering, recurrence
identification against prior meta-review records, cascade routing).

Cascade categorization:

  LOW    — typo fixes, single-file clarifications, prompt-wording polish;
            apply directly; note in the meta-review record.
  MEDIUM — prompt revisions that change agent behavior; methodology adjustments
            within the established framework; updates to BOOTSTRAP.md workflow
            steps; restructuring of slice conventions; new `concepts/` entries
            promoted from inline definitions; **role-granularity shifts**
            (subdividing / merging / narrowing existing roles); **MCP server
            service changes** (adding tools, changing signatures, deprecating
            tools). BUNDLE INTO A REFINEMENT PLAN requiring human approval
            before enactment.
  HIGH   — changes to the layer count or layer semantics; revisions to the L4
            calculus design; changes to "what the spec is for" or the core
            push-forward / push-back process; **introduction of a new agent
            role** (a 6th — subdividing an existing role into two is Medium,
            not High). SURFACE AS ESCALATION; do not propose changes.

For each issue, decide its category. Err toward Medium-as-escalation rather than
Medium-as-direct-action when the cascade trace is uncertain. The bar is "the
human would want to weigh in."

Patterns that recur across meta-review records are first-class signal — a problem
resolved once that recurs evidences resolution failure; on the third recurrence,
escalate from Medium to High.

Output: a single JSON object validating against `schemas/refinement_plan.json`.
Plus, on completion of human review and enactment, produce a meta-review record
file at `book/src/meta-reviews/<YYYY-MM-DD>.md` per the procedure in
`book/src/meta-reviews/index.md`.
```

**DONE when:** all five prompt files exist; a manual read-through confirms each role's contract matches the schemas in Phase 3 and the methodology in CLAUDE.md.

---

## Phase 5 — Orchestrator

The loop. Implemented in `orchestrator/` (Python, raw Anthropic SDK). Sketch:

```python
# orchestrator/loop.py — sketch, not complete
def main_loop():
    while True:
        if cycle_count_since_meta_review() >= config.meta_review_every_n_cycles:
            run_meta_review()    # pause-the-world; see below
            reset_cycle_counter()

        run_normal_cycle()
        increment_cycle_counter()

def run_normal_cycle():
    push = call_planner()                              # returns push directive
    if push["kind"] == "escalate":
        surface_to_human(push); return

    if push["kind"] == "forward":
        if push["to"] == "L1":
            finding = call_explorer(push["slice"], push["scope_question"])
            validate(finding, EXPLORATION_FINDING)
            rotation_claims = call_synthesizer_consolidate(finding)
        else:
            rotation_claims = call_synthesizer_rotate(push["slice"], push["from"], push["to"])

    elif push["kind"] == "back":
        rotation_claims = call_synthesizer_restructure(push["slice"], push["target_layer"])

    elif push["kind"] == "sideways":
        rotation_claims = call_synthesizer_unify(push["slices"])

    cited_source = prefetch_citations(rotation_claims)
    verdict = call_critic(rotation_claims, cited_source)   # ISOLATED context

    # All writes first — single atomic commit per cycle below.
    if verdict["verdict"] == "pass":
        apply_diff_to_book(rotation_claims)
    else:
        for issue in verdict["issues"]:
            if issue["kind"] == "labored_rotation_push_back_candidate":
                log_push_back_signal(issue)
            else:
                update_questions_or_revise(issue)

    if lesson := verdict.get("lesson"):
        append_lessons(lesson)
    append_episodic(push, rotation_claims, verdict)
    prepend_log_entry(format_cycle_log_entry(push, rotation_claims, verdict))

    commit(f"cycle: {push['kind']} {push.get('slice', '...')} → {verdict['verdict']}")

def run_meta_review():
    """Pause-the-world meta-review. The normal loop is fully paused here."""
    plan = call_meta_critic()                # ISOLATED context; reads its history
    apply_direct_actions(plan["direct_actions"])

    if plan["plan_items"]:
        human_approval = await_human_review(plan)
        apply_plan_items(human_approval)

    if plan["escalations"]:
        surface_escalations_to_human(plan["escalations"])

    write_meta_review_record(plan, applied=...)
    annotate_resolved_problems(plan)
    prepend_log_entry(format_meta_review_log_entry(plan))
    commit("meta-review: <date>")
```

**Hard invariants** — violations defeat the architecture:

- All five roles run in **separate API calls with separate system prompts and isolated contexts**. Never reuse a conversation between roles.
- The Critic sees the claims and the cited source, **never the Synthesizer's chain-of-thought**.
- The Meta-Critic sees the meta-cycle inputs and prior meta-review records, **never the per-cycle agents' chains-of-thought**.
- The Synthesizer's per-cycle output is a **diff** against `book/src/`, not an overwrite.
- The normal loop **pauses fully** during meta-review. No new cycles between trigger-fire and meta-review completion.
- Commit every cycle, pass or fail. Commit each meta-review enactment.
- `read_range` is the only source-returning MCP tool. The Explorer must localize before reading.

**DONE when:** `python orchestrator/loop.py --one-cycle` runs one normal cycle end-to-end against `reference/palace/` and commits the result (pass OR revise — either counts as successful execution).

---

## Phase 6 — Smoke test and first real pass

CG has been hand-drafted as `book/src/spec/slices/cg.md` during the methodology design phase. To avoid a tautological validation — where the agent loop merely reproduces the hand-drafted slice — Phase 6 exercises the loop on a **slice that has not been hand-drafted**: GMRES (`palace/palace/linalg/iterative.cpp` — `GmresSolver`).

GMRES is the right choice because it (a) has substantive new structure (Hessenberg matrix, Givens rotations, restart logic) that exercises L4's record-and-pruning facilities more fully than CG; (b) is large enough that the multi-file slice subdirectory convention (`book/src/spec/slices/gmres/`) gets tested; and (c) shares enough structure with CG that the existing concepts library (axpy/dot/matvec/apply_linop) covers a substantial portion of its primitives, exercising the unification-via-concepts path.

Run `--one-cycle` with the Planner pre-conditioned to pick `push: forward slice=gmres from=L0 to=L1` (an Explorer cycle scoped to GMRES's `Mult` and helper methods). Then run subsequent cycles for L1→L2, L2→L3, L3→L4.

After the four edge rotations, inspect:

- The agent-produced `book/src/spec/slices/gmres/` (subdirectory shape, per the convention for large slices) has L0/L1/L2/L3/L4 content with citations to GMRES's source.
- The L2→L3 rotation handles the Krylov-basis loop correctly: per-step primitives (matvec, dot, axpy, basis-extension) lift to L3; the outer restart loop and the per-step Arnoldi orthogonalization sequence are negative-L3 obstructions (sequentiality).
- The L3→L4 rotation uses the v0.3 calculus correctly: residual norms, per-iteration data exposed as record outputs, demand-driven pruning expressed.
- Every rotation claim has a citation chain that, when followed, supports the claim. Hand-verify the first three claims.
- The Synthesizer's GMRES claims reference `concepts/` entries created during CG's hand-drafting (`axpy`, `dot`, `matvec`, `apply_linop`) and propose new ones (`givens_rotation`, `hessenberg_extend`, `arnoldi_step`) — unification through shared primitives is the goal.

Then run `--continuous` for ten cycles (extending GMRES through restart variants, or starting a third slice like `eigensolver_lobpcg`) and verify:

- Per-edge rotation claims and source citations accumulate monotonically; nothing is silently rewritten.
- Token spend per cycle is within `cycle_token_budget`.
- The episodic log records non-trivial `friction_observed` and `structural_change` on at least one push (a ten-cycle run with all friction fields empty signals the loop isn't exercising its full push vocabulary).
- At least one BACK push is scheduled and executed in response to a push-back signal — i.e., the loop demonstrates productive friction resolution, not just forward motion.
- At least one SIDEWAYS push surfaces a unification opportunity (e.g., extracting `arnoldi_step` to `concepts/` because GMRES and a future eigensolver share it).
- The meta-review trigger (every 3 cycles per `config.toml`) fires automatically during the run — expect 3 meta-reviews across the 10-cycle window.

**DONE when:** GMRES is pushed to L4 with all rotation chains explicit and verified; hand-verification passes for the first three rotation claims (against the source, not against a hand-drafted reference); the ten continuous cycles produce at least one BACK push, at least one concept-extracting SIDEWAYS push, and a meta-review that fires automatically and completes. "Completes cleanly" is **not** the bar — a run that records no friction events is a failure to exercise the loop, not a success. (See CLAUDE.md *Process* and the verification rubric below for why count-based "done" misses the point.)

**Note.** The hand-drafted CG slice (`book/src/spec/slices/cg.md`) remains as a calibration target — the methodology should not produce an *incompatible* version of CG when re-run, even if it doesn't exactly reproduce the hand-drafted prose. A follow-on validation step (after Phase 6 DONE) is to re-push CG through the loop and verify the agent-produced version overlaps the hand-drafted one by ≥80% on cited source ranges and uses the same `concepts/` primitives.

---

## Phase 7 — Execution grounding (optional, recommended)

If Palace can be built and run on the target host, execution grounding catches a class of errors (subtle conditionals, dispatch-table indirection, macro expansion, runtime polymorphism in template instantiations) that purely static reading misses.

Steps:

1. Add a minimal tracer to Palace — language-appropriate hooks logging function entry/exit and state-variable values for a small canonical CG run (e.g., a 100-DoF SPD problem).
2. Add an `execution_check(predicted_trace) → diff` tool to the codemap MCP server returning the diff between observed and predicted call sequences.
3. Extend `prompts/critic.md`: for any L3/L4 claim about the per-step algorithm, additionally check that the predicted control flow matches the observed trace.

**DONE when:** at least one Critic verdict cites an execution-trace mismatch, and the resulting rotation reaches `pass` on re-exploration.

---

## Phase 8 — Scale: parallel slices

Defer until Phase 6 passes cleanly. Then:

1. Modify the Planner to return up to N independent pushes per cycle (pushes that touch disjoint slices and disjoint layer-edges).
2. Run N synthesis cycles concurrently (the codemap MCP server is stateless and handles parallel clients).
3. Critic remains sequential, processing per-cycle outputs in arrival order. On conflicting concept-promotion proposals from parallel synthesizers, the second-arriving proposal becomes a push-back signal instead of being applied directly — let the next cycle re-explore.
4. Raise `max_parallel_slices` in `config.toml` incrementally; watch for token-budget overruns and concept-name collisions.

**DONE when:** running with `max_parallel_slices = 4` produces the same eventual layered spec (within reproducibility tolerance — see rubric) as the sequential run for the first five Palace solvers, AND:

- Concept name collisions between parallel synthesizers are detected and resolved into unified concept entries — not duplicated under different names.
- Push-back signals raised by one slice that affect a layer shared with another slice propagate as scheduled BACK pushes in the next cycle: no silent overwriting, no lost friction.
- Token spend stays within `cycle_token_budget * max_parallel_slices` under sustained load.

A parallel run that reproduces the sequential spec but bypasses the concepts library (parallel synthesizers proposing duplicates) has not demonstrated parallel scale — it has demonstrated that two synthesizers can run without crashing, which is necessary but not sufficient.

---

## Escalation triggers

**Stop and ask the human** if any of the following occurs:

- Tree-sitter has no grammar for a Palace dialect file (e.g., generated headers) — the codemap server can't localize.
- The Planner outputs `push: escalate` three cycles in a row — no productive next push exists; design-level intervention needed.
- The Critic rejects three consecutive Synthesizer outputs on the same per-edge rotation — likely a prompt bug or an L4 calculus design issue, not a content issue.
- An Explorer's input exceeds `explorer_max_input_tokens` on a single region — the region is too coarsely scoped; the slice needs to subdivide.
- The episodic log shows push-back signals being filed faster than they are resolved over twenty cycles — friction is accumulating without integration.
- Two parallel slices produce contradictory L3 forms for the same source range across consecutive cycles — the source may be ambiguous (heavy templates, macro expansion) and needs human triage.
- A meta-review surfaces three High-category escalations in one pass — design-level conversation is overdue.

---

## Verification rubric (definition of done for the whole system)

The system is "done" not when the spec is exhaustively complete, but when **friction has been worked out**: the lower layers are stable enough that adding a new algorithm at L1 propagates upward without forcing structural restructuring, and the rotation chain has been exercised end-to-end. CLAUDE.md *Process* is the framing source-of-truth; this rubric translates it into checks. Count-based criteria are necessary scaffolding; friction-resolution criteria are sufficient closure.

### Scaffolding criteria (necessary — the mechanics work)

- **Every rotation claim has at least one citation.** Random spot-check of ten claims yields ≥9 where the cited source supports the claim (manual review by a domain-competent human).
- **At least three Palace slices** (CG + two others — GMRES and an eigenmode or time-stepping slice) have been pushed end-to-end to L4 against the v0.2-or-later L4 calculus.
- **Negative L3 results are present and properly justified** for at least the Krylov methods, with the obstruction explanation reading as a genuine algorithmic constraint, not a missing rotation.
- **The concepts/ library** has at least the primitives required by the worked slices (`axpy`, `dot`, `matvec`, `apply_linop`, `norml2` at minimum), each with a signature, a definition, and use-by links to slices.
- **A second independent run from the same seed slice** produces a slice file that overlaps the first by ≥80% on cited `file:line` ranges (reproducibility check; lower than this suggests the prompts admit too much path-dependence).

### Closure criteria (sufficient — friction has been worked out)

- **A new slice at L1 propagates upward without forcing lower-layer restructuring.** Concretely: when a fourth slice is added (after the three required above), its L1→L2 rotation reuses ≥70% of existing concept entries; the L2→L3 and L3→L4 rotations encounter no obstructions that require revising lower layers of the already-completed slices. If they do, the system is not yet done — the friction needs another round of integration.
- **Push-back signals resolve within bounded cycles.** Over the meta-review window, every push-back signal raised is followed within ≤3 cycles by a BACK push that addresses it (or an explicit decision to absorb it, logged as a `lesson`). Signals accumulating without resolution mean the loop is generating friction faster than it integrates — an escalation trigger.
- **The L4 worked sample is end-to-end.** At least one slice carries an explicit rotation chain L0→L1→L2→L3→L4, with each rotation's justification readable and the Critic having verified each edge separately.
- **One meta-review has completed** with a refinement plan that the human approved and the loop enacted; the plan made non-trivial changes (not just typo fixes).
- **The episodic log shows non-trivial branching** — `friction_observed` populated on non-clean pushes, BACK pushes scheduled and executed, sideways comparisons that yielded concept-promotions or unification findings.
- **The concepts/ library is reused, not bypassed.** New slices reach for existing concept entries before proposing new ones; meta-review records show concept-name unifications rather than unchecked proliferation.

A system that satisfies the scaffolding criteria but where push-back signals accumulate without resolution, or where the concepts library is bypassed by parallel synthesizers proposing duplicates, has built the mechanics without exercising the loop. The closure criteria are what make the dissection actually work.

---

## Notes for the implementing agent

- The methodology consolidates in CLAUDE.md; the build order is in this file. **Read CLAUDE.md first.** If anything in this file contradicts CLAUDE.md, CLAUDE.md wins — flag the contradiction as a problem (`problems/`) for the next meta-review to resolve.
- Prefer extending existing files (the book/, problems/, schemas/, prompts/ structures) over creating parallel ones. The artifact lives in the book.
- Commit per phase during bootstrap; commit per cycle once the loop is running; commit per meta-review enactment.
- If you find yourself wanting to add features not in this document (a UI, an embedding store, a separate database, additional agent roles, structurally new layers, monad transformer stacks, …), **do not**. Finish bootstrap first. Anything that would be a layer-design change or process-model change is a High-cascade meta-review item, not a Phase 9.
- This document is itself a specification. If something here is ambiguous, treat that as the kind of question the agent system you're building would raise — log it in `problems/`, surface it to the human.
