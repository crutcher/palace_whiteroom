# Palace Whiteroom

A layered-spec multi-agent system that dissects [AWS Labs Palace](https://github.com/awslabs/palace) — a parallel C++ finite-element electromagnetic simulator — into an incremental impedance-matching stack of algorithmic representations (L0 cited source → L1 mutation-lifted → L2 fusion-unfolded algebra → L3 global tensor-field form → L4 formal graph-evaluation calculus). Every claim cites `file:line` against a local shallow-git checkout, and every layer rotation carries an explicit equivalence justification verified by an adversarial Critic. The output is a citation-grounded specification, not a port; a separate downstream effort consumes the L4 form to specify what a tensor library (`burn`) would need to realize it. The pipeline is six per-cycle and meta-cycle roles, each running in an isolated API context with its own system prompt.

## Status

- **Phase 6 DONE.** Phase 6+ continuation underway since meta-review #10.
- **Most recent milestone (meta-17, cycles 74–79):** chebyshev reached L4 — the fourth slice to complete the full layer stack after cg, gmres, orthog. Integrator-side enforcement of concept-existence checks landed (recurrence #4 of SIDEWAYS mode=create-on-existing forced the loud-failure conversion).
- **Quantitative snapshot:** 79 normal cycles completed; 17 meta-reviews fired; 2 skills extracted (`classify-variant-axis`, `verify-citation-range`); 24 concepts on disk.

## The Layered Stack

The dissection lifts each slice through five layers; each rotation removes one specific impedance.

- **L0** — cited source ranges in the Palace tree (`reference/palace/...`). Ground truth.
- **L1** — *mutation rotation*. Source operations re-expressed as pure functions with explicit input/output sets; in-place mutation and aliasing made explicit or erased.
- **L2** — *fusion rotation*. Canonical algebraic decomposition with HPC/SIMD tricks unfolded back into base primitives; load-bearing numerical choices preserved as explicit claims.
- **L3** — *iteration rotation*. Per-element loops lifted to global tensor-field operations where possible; obstruction records (negative L3 results) where genuinely sequential.
- **L4** — *formal graph-evaluation calculus*. Top of the stack: small, formally-defined calculus distinguishing simulator state, operator internal parameters, and ephemeral intermediates with explicit monadic coordination.

## Spec Slices

| Slice | Highest layer | Most recent activity |
|-------|---------------|----------------------|
| [CG](book/src/spec/slices/cg.md) | L4 | L4 stack closed + derived-view-hoisting tightenings (cycles 74, 76) |
| [GMRES](book/src/spec/slices/gmres.md) | L4 | L3→L4 emission (cycle 75); state-stratification + solve-monad form |
| [Orthogonalisation](book/src/spec/slices/orthog.md) | L4 | L2→L3 lift to global tensor-field ops (cycle 77) |
| [Chebyshev smoother](book/src/spec/slices/chebyshev.md) | L4 | **L3→L4 landed (cycle 78)** — fourth slice past full stack |
| [Divergence-free projection](book/src/spec/slices/divfree.md) | L3 | L4 in flight; sequential-obstruction recorded |

## Methodology Surface

- **Agent roles** — 5 (planner, explorer, synthesizer, critic, meta-critic) running in isolated API contexts with prompts under `prompts/`. A sixth meta-cycle-only prompt (`prompts/readme_builder.md`) regenerates this README at every meta-cycle end.
- **Critic checks** — 15 numbered checks (`prompts/critic.md`). Recent additions: `#13` original-emission claim discipline with per-building-block granularity, `#14` rotation_claims-require-surface (symmetric inverse of #13), `#15` skill-invocation visibility (meta-17).
- **Invocable skills** — 2 active under `skills/`:
  - `classify-variant-axis` — given a variant axis with N values, classify each as constructed-operator / parametric / scope-out / residual-axis (meta-11 extraction).
  - `verify-citation-range` — verify L0 citation `<path>:<lo>-<hi>` doesn't cross the named symbol's lexical boundary; intra-function ±1-3 line drift OK, cross-function-boundary drift not OK (meta-16 extraction).
- **Concepts on disk** — 24, categorized: 3 methodology, 4 algorithm, 10 primitive, 6 layer-pattern, 1 auxiliary. Auto-maintained in `book/src/concepts/index.md` and `book/src/SUMMARY.md` on every `concept_writes mode=create`.
- **Notable infrastructure from meta-17:** integrator-side enforcement converted silent concept-existence skips into loud `_record_fail` events with structured push-back; Planner retroactive-backfill budget restored forward-dispatch bias after a 2/6 → 5/6 regression.

## Recent Meta-Reviews

- **Meta-17 (cycles 74–79):** chebyshev at L4; SIDEWAYS recurrence #4 forced integrator-side enforcement; Critic check #15 added for skill-uptake visibility.
- **Meta-16 (cycles 68–73):** orthog L1→L2; gmres restored cleanly through L3; per-building-block claim granularity rule added; **second skill extraction** (`verify-citation-range`).
- **Meta-15 (cycles 62–67):** Self-tightening termination criterion added after 5 consecutive cg L4→L4 grind; edge-label fidelity rule; Critic check #12 trigger by structural condition rather than declarative label.
- **Meta-14 (cycles 56–61):** orthog reached L4; retroactive_claims dropped 5/6 → 2/6 from meta-13 tightening; Critic check #14 added (rotation_claims-require-surface).
- **Meta-13 (cycles 50–55):** CG preconditioned-variant advanced L1→L4; rotation-as-renaming recurrence #2 caught by Critic; refined verdict-downgrade rule distinguished bookkeeping from substantive failures.

## Reproducibility

- Build the book: `cargo make book` (one-time tooling install on first run).
- Live preview: `cargo make book-serve` (browse `book/book/html/`).
- Run the agent loop continuously: `orchestrator/.venv/bin/python -m orchestrator --continuous`. Requires `ANTHROPIC_API_KEY` in `.env` (see `.env.example`).
- Read per-cycle history: `LOG.md` (human-readable, newest first).
- Read structured per-cycle records: `episodic.jsonl` (one JSON line per cycle).
- Read the spec deliverable: `cargo make book-serve` then browse the rendered mdBook.

## Pointers

- [`CLAUDE.md`](CLAUDE.md) — agent operating instructions; methodology surface.
- [`BOOTSTRAP.md`](BOOTSTRAP.md) — phased build spec for the agent system.
- [`book/src/SUMMARY.md`](book/src/SUMMARY.md) — full TOC of the dissection artifact.
- [`book/src/meta-reviews/`](book/src/meta-reviews/) — immutable meta-review records (17 to date).
- [`prompts/`](prompts/) — five role prompts plus `readme_builder.md` (this README's source).
- [`skills/`](skills/) — invocable agent procedures (verbs).
- [`scaffolding/`](scaffolding/) — agent-side workshop notes (cross-cutting, decision logs).
