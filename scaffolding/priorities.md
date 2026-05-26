# Priorities

Short next-up list. Meta-phase and cycle-planner co-edit. Cycle-planner reads each cycle to inform dispatch selection.

**Discipline:**
- Keep under 10 items.
- Each item: one line, slug + one-sentence rationale.
- Meta-phase adds when friction-ledger surfaces an actionable target.
- Integrator removes when an item lands in the artifact.

## Now (active)

1. **bootstrap-L1-vocabulary** (in progress: `axpy` landed pilot-1) — harvest the core L1 operators (~~axpy~~, dot, nrm2, scal, apply_linop) into `book/src/L1/`. They exist as concepts; promote to firm L1 entries.
2. **bootstrap-L1-L0-theme-axpby** — abstractor sketches the in-place `x.Add(α, y)` → `x_{k+1} = x_k + α·y` rewrite as the first L1>L0 lowering theme.
3. **mine-krylov-iteration-step** — combinator-miner scans Phase 1 corpus (cg, gmres, chebyshev) for the recurring Krylov-step shape; propose an L2 combinator.

## Near (queued)

4. **bootstrap-L4-state-stratification** — write the L4 layer intro / dep-map that exposes the sim-state vs operator-params vs ephemeral distinction.
5. **lowering-verifier-axpy-theme** — once #2 lands, audit it against Palace evidence.

## Watch list (deferred)

- Phase 1 slice corpus move to `book/src/_phase1_corpus/` — 64 cross-references need rewriting; defer until pilot validates flow.
- `lessons.md` retirement — keep as historical record post-Phase-E.

## Recently landed

(none yet — first entries will accumulate as integrator clears priority items)
