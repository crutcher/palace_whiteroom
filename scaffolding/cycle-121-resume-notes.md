# Cycle-121 resume notes (OUT-OF-BAND RESCOPE meta-phase → batch-39 lift-through campaign)

**⟢ SESSION RESTART REQUIRED before cycle-121. This SUPERSEDES the batch-38 meta-phase's "NO SESSION RESTART REQUIRED" note** (that note was written post-c120-finalize, BEFORE the 2026-06-07 out-of-band re-scope; it is now stale).

The OUT-OF-BAND RESCOPE meta-phase (fired off-schedule 2026-06-07 to enact three new user directives answering the batch-38 plateau ASK) made **`.claude/agents/*` role-spec edits AND a CLAUDE.md edit** — both session-start-loaded config. A restart is required so the new agent definitions + operational guide are loaded before c121.

## Restart-triggering edits

**CLAUDE.md:**
- §Scope — rewritten with the three re-scope directives (MPI/sharding deferred future direction with the non-destabilization gate; the geometric-multigrid preconditioner + AMR now in active scope; the enum-stub-vs-spine-dependency-opaque-kernel split).
- §Methodology invariants — NEW invariant "Kernel-API vs kernel-IMPLEMENTATION distinction" (spine-dependency opaque-library kernels get BOTH a `kernel-api` surface + a `kernel-impl` node, linked by a `realizes-kernel-api` `reference`-class edge).

**`.claude/agents/` (7 role-specs):**
- `cycle-planner.md` — NEW 2026-06-07-RESCOPE banner: the lift-through frontier (geometric-multigrid preconditioner = LEAD; constructive spine-dependency kernels; AMR; RE-discharge tail); STOP-PROPOSING LIFTED for the in-scope set; MPI/sharding stays OUT.
- `harvester.md` — NEW banner: kernel-API/impl distinction (author the `kernel-impl`, keep the `kernel-api`, link `realizes-kernel-api` `reference`-class) + lift-through-deferred discipline.
- `abstractor.md` — NEW banner: same kernel-API/impl + lift-through (supersedes "obstruction theme = no constructive form" for spine-dependency opaque-library kernels; enum-stub carve-out preserved).
- `combinator-miner.md` — NEW banner: kernel-impl shared-substrate mining (smoother recurrence / matrix-free contraction / Krylov iteration) + lift-through.
- `lowering-verifier.md` — NEW banner: audit the impl-realizes-API correspondence + confirm the link is `reference`-class.
- `layer-intro-author.md` — NEW banner: kernel-API/impl chapter-kind mechanics (sensible-default; no new SUMMARY/linter machinery) + the geometric-multigrid preconditioner feature-surface column.
- `meta-phase.md` — NEW §Standing-book-targets duty: kernel-API/impl integrity + the lift-through (RE-discharge) campaign tracking + the DIRECTIVE-1 (MPI boundary) guard.

## Non-restart-affecting edits (scaffolding + memory + book-mirror)

- `scaffolding/priorities.md` — active head reshaped into the CYCLE-121/batch-39 lift-through campaign (5 plan items; geometric-multigrid LEAD).
- `scaffolding/friction-ledger.md` — NEW `plateau-as-scope-boundary-not-project-boundary` entry (recurrence-3, addressed by the re-scope).
- `scaffolding/open-questions.md` — banner migrating the now-activated deferred families (eigsolve/SLEPc, chebyshev/preconditioning, assemble-diagonal, FE-assembly libCEED, fem/FE-space, NLEPS/orthogonalize) to the plan; MPI/sharding stays deferred.
- 4 NEW memories (`project_rescope_2026_06_07`, `project_sharding_mpi_deferred`, `project_lift_through_deferred_in_scope`, `project_kernel_api_impl_distinction`) + 2 updated (`project_blackbox_vs_accelerated_kernels` extended, `project_unimplemented_palace_components` carve-out-note) + MEMORY.md pointers.
- `book/src/methodology/goal-flow.md` — batch-39 re-scope arc paragraph + a new §"kernel-API vs kernel-implementation" methodology section + one-line scope update; `cargo make book` EXIT 0.
- `scaffolding/cycle-record.jsonl` — out-of-band rescope-directive meta-phase record appended.

## What the c121 planner does

Plan against the CYCLE-121/batch-39 lift-through campaign head in `scaffolding/priorities.md`. The geometric-multigrid preconditioner is the LEAD (HIGH fan-out — discharges RE1/RE5/RE7/RE9 by composing the level-stack + smoother + diagonal-preconditioner chains by name). The constructive spine-dependency kernels (libCEED quadrature / triangular-solve+GS-SSOR relaxation / SLEPc eigsolve — each with the kernel-API/impl distinction) are parallel HIGH fronts; AMR is a strong grounded front; the cheap openers (RE10 interpolator-ground + waveguide-mode drift cleanup) fold in as low-fan-out parallel picks. Items 1-3 are a wide wave sharing the mesh→fe_space→smoother→Krylov substrate (lift the shared cores once). **MPI/sharding stays OUT of active scope.**

(No `/compact` step — the restart resets primary context, per CLAUDE.md §Methodology-invariants.)
