# Cycle-040 resume notes (post-batch-11 meta-phase)

**Session restart REQUIRED before cycle-040 begins.** The batch-11 meta-phase (post-cycle-039) edited three agent role-specs; the new definitions must be loaded before the next dispatch.

## Agent-defs changed this meta-phase (why a restart is needed)

- **`.claude/agents/cycle-planner.md`** — NEW §Discipline bullet: *count-ownership convention*. When ≥2 parallel dispatches land into the same layer index AND it carries a consolidated running-count tally, assign the tally write to exactly ONE owner (prefer a co-dispatched `layer-intro-author`; else the last harvester in dependency order) and instruct the other dispatches to emit only their own dep-map / SUMMARY rows and DEFER the tally. Friction-ledger `parallel-blind-shared-index-count-divergence`.
- **`.claude/agents/harvester.md`** — NEW §Discipline bullet: do NOT write the layer-index consolidated running-count tally when another co-dispatched agent owns it this cycle (append only your own dep-map row + SUMMARY registration).
- **`.claude/agents/layer-intro-author.md`** — NEW §Discipline bullet: when designated the single-owner of the index count tally, compute the POST-COHORT total (all the cycle's landings, not just the one you touched) and write the single authoritative tally; the parallel producers defer to you.

## Why these matter for cycle-040

Cycle-040's active head #1 is the (B) substantive L3 cohort (`orthogonalize` / `chebyshev-smoother` / `apply_nonlinear_pencil`). If the planner dispatches ≥2 of these in parallel (each landing into `book/src/L3/index.md`), the count-ownership convention applies — assign ONE tally owner. The convention only takes effect if the restarted session has the new role-specs loaded.

## What did NOT change

- No new agent roles, no cycle-structure changes, no skill promotions/retirements.
- The restart is the context-reset mechanism (subsumes the retired `/compact` step per CLAUDE.md §Methodology invariants). Do NOT run a separate `/compact`.

## Batch-12 active head (cycle-040)

The c036 D2 (A) identity-in-form L3 cohort is **6-of-6 CLOSED** (L3 firm 9→15). The L3 frontier shifts to:
1. **(B) substantive L3 cohort** — `orthogonalize` L3 (suggested first; third `partial-obstruction` row), `chebyshev-smoother` L3 (subsumption-check vs existing L3 `chebyshev` FIRST), `apply_nonlinear_pencil` L3 (fold into eigsolve-variant, not standalone).
2. Audit slot — `verified_against:` audits for the (B) entries once firm; opportunistic minor citation tightens (floquet `:25-26`→`:25`; chebyshev-smoother `:101-110`→`:102-110`).
3. Open slot — L1-promotion track (`matrix-weighted-norm` / `bilinear-form`, would unblock `normalize_B` L3) / Phase-1 slice-reduction audit / L3-index overlay refresh (fifth obstruction profile + stale-snapshot compaction).

STOP-PROPOSING NEGATIVE LIST stays in force: `lu_solve`, `back_solve`, `ls-update-column`, 4 NLEPS atoms.

See `scaffolding/priorities.md` §Now (active) — cycle-040 for the full fan-out-ranked head.
