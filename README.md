# Palace Whiteroom

A layered-spec multi-agent system that dissects [AWS Labs Palace](https://github.com/awslabs/palace) — a parallel C++ finite-element electromagnetic simulator — into an incremental impedance-matching stack of algorithmic representations (L0 cited source → L1 mutation-lifted → L2 fusion-unfolded algebra → L3 global tensor-field form → L4 formal graph-evaluation calculus). Every claim cites `file:line` against a local shallow-git checkout, and every layer rotation carries an explicit equivalence justification verified by an adversarial Critic. The output is a citation-grounded specification, not a port; a separate downstream effort consumes the L4 form to specify what a tensor library (`burn`) would need to realize it. The pipeline is six per-cycle and meta-cycle roles, each running in an isolated API context with its own system prompt.

## Status

- **Phase 6 DONE.** Phase 6+ continuation underway since meta-review #10.
- **Most recent milestone (meta-20, cycles 92–103):** **arnoldi_step landed at L4** (cycles 98–102) — the **first intermediate-tier algorithm extracted**, validating the meta-18 intermediate-tier prioritization directive end-to-end. Plus orchestrator hardening: `append_slice_index_row` fallback for new-slice rows; global retroactive counter (catches rotate-through-slices); skill_uptake_emitted episodic diagnostic; problems-sensitivity recalibrated 3→4 (0 problems filed in window, below 0.5× target).
- **Quantitative snapshot:** 103 normal cycles completed; 20 meta-reviews fired; 3 skills extracted; ~25 concepts on disk; **6 active slices**.

## Relative Progress

Reported against [`scaffolding/roadmap.md`](scaffolding/roadmap.md). The roadmap is reviewed by the Meta-Critic at every meta-cycle.

- **Solver pipelines** — 0/5 fully covered to L4 (no single physics pipeline complete; the shared Krylov footprint covers most of all 5).
- **Krylov solvers** — 2/4 at L4 (CG, GMRES; pending MINRES, BiCGStab).
- **Orthogonalisation** — 1/2 at L4 (MGS/CGS/CGS2; Householder QR pending as sibling slice).
- **Smoothers and preconditioners** — 1/6 at L4 (Chebyshev; pending Jacobi, SGS, ILU, AMS, multigrid).
- **Projections and auxiliary operators** — 0/2 at L4 (divfree at L3, L4 in flight; curl-curl pending).
- **Intermediate-tier algorithms** — **1/7 extracted (arnoldi_step ✓)**. Next likely picks per impact ranking: plane-rotation stream, polynomial-recurrence step.
- **FE assembly** — 0/4 (mesh + FE-space, sparse-assembly patterns, operator composition, boundary conditions).
- **Coordination and post-processing** — 0/4 (time-stepping, frequency sweep, eigenpair extraction, I/O).
- **Methodology infrastructure** — 6 roles; **3 skills** (classify-variant-axis, verify-citation-range, skill-selection); ~25 concepts; 15 numbered Critic checks; integrator channel set complete.
- **Phase progression** — 7/10+ phases done (Phases 0-6 complete; Phase 6+ in flight).

The dominant remaining surface is per-solver pipeline buildup. arnoldi_step's landing demonstrates the loop can now positively select intermediates over roots and drive them to L4 in a single 12-cycle window.

## The Layered Stack

- **L0** — cited source ranges in the Palace tree (`reference/palace/...`). Ground truth.
- **L1** — *mutation rotation*. Source operations re-expressed as pure functions with explicit input/output sets; mutation/aliasing made explicit or erased.
- **L2** — *fusion rotation*. Canonical algebraic decomposition; HPC tricks unfolded; load-bearing numerical choices preserved as claims.
- **L3** — *iteration rotation*. Per-element loops lifted to global tensor-field ops where possible; obstruction records (negative L3 results) where genuinely sequential.
- **L4** — *formal graph-evaluation calculus*. Top of the stack: state-stratification + monadic coordination + obstruction typing.

## Spec Slices

| Slice | Highest layer | Most recent activity |
|-------|---------------|----------------------|
| [CG](book/src/spec/slices/cg.md) | L4 | L3→L4 retroactive backfill (cycles 96-97) |
| [GMRES](book/src/spec/slices/gmres.md) | L4 | L1→L2→L3 per-building-block backfill (cycles 92-95) |
| [Orthogonalisation](book/src/spec/slices/orthog.md) | L4 | L1→L2 backfill (cycle 94) |
| [Chebyshev smoother](book/src/spec/slices/chebyshev.md) | L4 | L3→L4 retroactive (prior window) |
| [Divergence-free projection](book/src/spec/slices/divfree.md) | L3 | L4 in flight |
| [**Arnoldi step**](book/src/spec/slices/arnoldi_step.md) | **L4** | **L0→L4 extraction in one window (cycles 98-102)** — first intermediate-tier slice |

## Methodology Surface

- **Agent roles** — 6 (planner, explorer, synthesizer, critic, meta-critic per-cycle/meta-cycle + README builder meta-cycle finaliser).
- **Push kinds** — 4 (forward, back, sideways, **refinement**); plus orchestrator-driven escalate. Refinement is conservative; major discrepancies escalate to `problems/`.
- **Critic checks** — 15 numbered (`prompts/critic.md`). Recent additions: #13 (original-emission claim discipline + per-building-block granularity), #14 (rotation_claims-require-surface), #15 (skill-invocation visibility with structured `skill_uptake` field; per-verdict-envelope MUST-emit per meta-20).
- **Invocable skills** — 3 active under `skills/`:
  - `classify-variant-axis` — variant-axis classification (constructed-operator / parametric / scope-out / residual-axis).
  - `verify-citation-range` — L0 citation cross-symbol-boundary check.
  - `skill-selection` — meta-skill: pre-cycle survey of applicable skills for both Synthesizer and Critic.
- **Concepts on disk** — ~25, auto-maintained in `book/src/concepts/index.md` and `book/src/SUMMARY.md` on every `concept_writes mode=create`.
- **Self-tuning** — `problems/` filing rate auto-calibrates each meta-cycle to target 1/15 cycles; sensitivity (1-5 scale) lives at `scaffolding/problems-sensitivity.md` (now 4 — eager — after 12-cycle window saw 0 filings).

## Recent Meta-Reviews

- **Meta-20 (cycles 92–103):** **arnoldi_step at L4** (first intermediate-tier); `append_slice_index_row` integrator fallback; global retroactive counter; skill_uptake diagnostic instrumentation.
- **Meta-19 (cycles 86–91):** Third skill extraction (`skill-selection` meta-skill); hard-gate escalate-storm recovery via call_planner_with_addendum; SIDEWAYS auto-rewrite (closes 5-recurrence Synthesizer defect at integrator level).
- **Meta-18 (cycles 80–85):** Forward-frontier criterion; intermediate-tier prioritization (user directive); retroactive-budget hard gate (Planner + orchestrator auto-escalate).
- **Meta-17 (cycles 74–79):** chebyshev at L4; SIDEWAYS recurrence #4 → integrator-side enforcement; Critic check #15 (skill-invocation visibility).
- **Meta-16 (cycles 68–73):** Second skill extraction (`verify-citation-range`); per-building-block claim granularity rule.

## Reproducibility

- Build the book: `cargo make book` (one-time tooling install on first run).
- Live preview: `cargo make book-serve` (browse `book/book/html/`).
- Run the agent loop continuously: `orchestrator/.venv/bin/python -m orchestrator --continuous`. Requires `ANTHROPIC_API_KEY` in `.env` (see `.env.example`).
- Read per-cycle history: [`log/README.md`](log/README.md) (newest-first index); individual entries at `log/cycle-NNN.md` and `log/meta-NN-cycles-A-B.md`.
- Read structured per-cycle records: `episodic.jsonl` (one JSON line per cycle).

## Pointers

- [`scaffolding/roadmap.md`](scaffolding/roadmap.md) — abstract roadmap; the denominator for *Relative Progress*; includes intermediate-tier candidates with impact ranking.
- [`scaffolding/problems-sensitivity.md`](scaffolding/problems-sensitivity.md) — self-tuning sensitivity for `problems/` filings (target 1/15 cycles).
- [`book/src/concepts/dependency-map.md`](book/src/concepts/dependency-map.md) — concept dependency map; solid-outline = on disk, dashed-outline (`:::planned`) = future markers.
- [`CLAUDE.md`](CLAUDE.md) — agent operating instructions.
- [`BOOTSTRAP.md`](BOOTSTRAP.md) — phased build spec for the agent system.
- [`book/src/SUMMARY.md`](book/src/SUMMARY.md) — full TOC of the dissection artifact.
- [`book/src/meta-reviews/`](book/src/meta-reviews/) — immutable meta-review records (20 to date).
- [`prompts/`](prompts/) — six role/meta-cycle prompts.
- [`skills/`](skills/) — invocable agent procedures (verbs).
- [`scaffolding/`](scaffolding/) — agent-side workshop notes.
