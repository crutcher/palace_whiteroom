# Palace Whiteroom

A layered-spec multi-agent system that dissects [AWS Labs Palace](https://github.com/awslabs/palace) — a parallel C++ finite-element electromagnetic simulator — into an incremental impedance-matching stack of algorithmic representations (L0 cited source → L1 mutation-lifted → L2 fusion-unfolded algebra → L3 global tensor-field form → L4 formal graph-evaluation calculus). Every claim cites `file:line` against a local shallow-git checkout, and every layer rotation carries an explicit equivalence justification verified by an adversarial Critic. The output is a citation-grounded specification, not a port; a separate downstream effort consumes the L4 form to specify what a tensor library (`burn`) would need to realize it. The pipeline is six per-cycle and meta-cycle roles, each running in an isolated API context with its own system prompt.

## Status

- **Phase 6 DONE.** Phase 6+ continuation underway since meta-review #10.
- **Most recent milestone (meta-21, cycles 104–115):** **Refinement push kind fired for the first time** (cycles 113, 115) — the user 2026-05-26 directive is end-to-end. **2 more intermediate-tier slices extracted** via retroactive-gate-retry redirects (plane_rotation_stream L1, sparse_triangular_solve L1 negative result) — 3 of 7 intermediate-tier candidates now in motion. Schema formalized self-edges (L_n→L_n, Ln→Ln); skill_uptake aggregate stats surfaced in episodic; integrator auto-normalizes H1→H2 on concept create→append rewrites.
- **Quantitative snapshot:** 115 normal cycles completed; 21 meta-reviews fired; 3 skills extracted; ~25 concepts on disk; **8 active slices**.

## Relative Progress

Reported against [`scaffolding/roadmap.md`](scaffolding/roadmap.md). The roadmap is reviewed by the Meta-Critic at every meta-cycle.

- **Solver pipelines** — 0/5 fully covered to L4 (no single physics pipeline complete; the shared Krylov footprint covers most of all 5).
- **Krylov solvers** — 2/4 at L4 (CG, GMRES; pending MINRES, BiCGStab).
- **Orthogonalisation** — 1/2 at L4 (MGS/CGS/CGS2; Householder QR pending as sibling slice).
- **Smoothers and preconditioners** — 1/6 at L4 (Chebyshev; pending Jacobi, SGS, ILU, AMS, multigrid).
- **Projections and auxiliary operators** — 0/2 at L4 (divfree at L2, L4 in flight; curl-curl pending).
- **Intermediate-tier algorithms** — **3/7 in motion**: arnoldi_step ✓ (L4), plane_rotation_stream (L1), sparse_triangular_solve (L1, negative result). Next likely picks per impact: polynomial-recurrence-step, diagonal-preconditioner-apply, residual-update, restart-machinery.
- **FE assembly** — 0/4 (mesh + FE-space, sparse-assembly patterns, operator composition, boundary conditions).
- **Coordination and post-processing** — 0/4 (time-stepping, frequency sweep, eigenpair extraction, I/O).
- **Methodology infrastructure** — 6 roles; **3 skills** (classify-variant-axis, verify-citation-range, skill-selection); ~25 concepts; 15 numbered Critic checks; self-edge rotation schema; integrator channel set complete.
- **Phase progression** — 7/10+ phases done (Phases 0-6 complete; Phase 6+ in flight).

The dominant remaining surface is per-solver pipeline buildup. The intermediate-tier prioritization continues to compound: 3 candidates in motion within 2 windows, validating the meta-18 impact-ranking heuristic.

## The Layered Stack

- **L0** — cited source ranges in the Palace tree (`reference/palace/...`). Ground truth.
- **L1** — *mutation rotation*. Source operations re-expressed as pure functions with explicit input/output sets; mutation/aliasing made explicit or erased.
- **L2** — *fusion rotation*. Canonical algebraic decomposition; HPC tricks unfolded; load-bearing numerical choices preserved as claims.
- **L3** — *iteration rotation*. Per-element loops lifted to global tensor-field ops where possible; obstruction records (negative L3 results) where genuinely sequential.
- **L4** — *formal graph-evaluation calculus*. Top of the stack: state-stratification + monadic coordination + obstruction typing.

## Spec Slices

| Slice | Highest layer | Most recent activity |
|-------|---------------|----------------------|
| [CG](book/src/spec/slices/cg.md) | L4 | L1→L2 (cycle 105); L2→L3 retries blocked on sequential-obstruction concept-append (cycles 106-107); L4 partial |
| [GMRES](book/src/spec/slices/gmres.md) | L4 | L3→L4 (cycle 110); L4→L4 self-tightening (cycle 104) |
| [Orthogonalisation](book/src/spec/slices/orthog.md) | L4 | Refinement (cycle 113 — first refinement push) |
| [Chebyshev smoother](book/src/spec/slices/chebyshev.md) | L4 | (prior window) |
| [Divergence-free projection](book/src/spec/slices/divfree.md) | L2 | L1→L2 retry redirect (cycle 111) |
| [Arnoldi step](book/src/spec/slices/arnoldi_step.md) | L4 | Refinement attempted (cycle 115 — revise on surface-or-evidence gap) |
| [**Plane rotation stream**](book/src/spec/slices/plane_rotation_stream.md) | **L1** | **L0→L1 extraction (cycle 108)** via retroactive-gate retry |
| [**Sparse triangular solve**](book/src/spec/slices/sparse_triangular_solve.md) | **L1** | **L0→L1 negative result (cycle 112)** via retroactive-gate retry |

## Methodology Surface

- **Agent roles** — 6 (planner, explorer, synthesizer, critic, meta-critic + README builder).
- **Push kinds** — 4 (forward, back, sideways, **refinement** — first fire cycle 113); plus orchestrator-driven escalate. Refinement is conservative; major discrepancies escalate to `problems/`.
- **Critic checks** — 15 numbered. Recent additions: #13 (per-building-block granularity), #14 (rotation_claims-require-surface), #15 (skill-uptake structured field; aggregate stats added meta-21).
- **Rotation-claim edge schema** — `L_n→L_{n+1}` plus self-edges `L_n→L_n` (added meta-21 for refinement / self-tightening cycles).
- **Invocable skills** — 3 active:
  - `classify-variant-axis` — variant-axis classification.
  - `verify-citation-range` — L0 citation cross-symbol-boundary check.
  - `skill-selection` — meta-skill: pre-cycle skill survey for Synthesizer and Critic.
- **Concepts on disk** — ~25, auto-maintained.
- **Self-tuning** — `problems/` filing rate auto-calibrates each meta-cycle to target 1/15; sensitivity now **5 (cap)** — 0 filings across two full windows; if next window is also 0, surface for review.

## Recent Meta-Reviews

- **Meta-21 (cycles 104–115):** Refinement push fires; 2 more intermediate-tier slices; self-edge schema; skill_uptake aggregates; H1→H2 auto-normalize; refinement surface-or-evidence rule.
- **Meta-20 (cycles 92–103):** arnoldi_step at L4 (first intermediate-tier); append_slice_index_row fallback; global retroactive counter; skill_uptake_emitted diagnostic.
- **Meta-19 (cycles 86–91):** Third skill (`skill-selection`); hard-gate escalate-storm recovery; SIDEWAYS auto-rewrite.
- **Meta-18 (cycles 80–85):** Forward-frontier criterion; intermediate-tier prioritization (user directive); retroactive-budget hard gate.
- **Meta-17 (cycles 74–79):** chebyshev at L4; integrator-side SIDEWAYS enforcement; skill-invocation visibility (#15).

## Reproducibility

- Build the book: `cargo make book` (one-time tooling install on first run).
- Live preview: `cargo make book-serve`.
- Run the agent loop continuously: `orchestrator/.venv/bin/python -m orchestrator --continuous`. Requires `ANTHROPIC_API_KEY` in `.env`.
- Read per-cycle history: [`log/README.md`](log/README.md) (newest-first index); individual entries at `log/cycle-NNN.md` and `log/meta-NN-cycles-A-B.md`.
- Read structured per-cycle records: `episodic.jsonl`.

## Pointers

- [`scaffolding/roadmap.md`](scaffolding/roadmap.md) — abstract roadmap; the *Relative Progress* denominator.
- [`scaffolding/problems-sensitivity.md`](scaffolding/problems-sensitivity.md) — self-tuning sensitivity for `problems/` filings.
- [`book/src/concepts/dependency-map.md`](book/src/concepts/dependency-map.md) — concept dependency map (solid = on disk, dashed `:::planned` = future).
- [`CLAUDE.md`](CLAUDE.md) — agent operating instructions.
- [`BOOTSTRAP.md`](BOOTSTRAP.md) — phased build spec.
- [`book/src/SUMMARY.md`](book/src/SUMMARY.md) — full TOC.
- [`book/src/meta-reviews/`](book/src/meta-reviews/) — immutable meta-review records (21 to date).
- [`prompts/`](prompts/) — six role/meta-cycle prompts.
- [`skills/`](skills/) — invocable agent procedures.
- [`scaffolding/`](scaffolding/) — agent-side workshop notes.
