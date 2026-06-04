# METHODOLOGY-CHANGELOG.md

Archive of **superseded** methodology directives and the **history tails** extracted from `CLAUDE.md` during the cycle-087/batch-27 de-bulk pass (2026-06-04). Nothing here is live methodology — it is the provenance record for directives the active `CLAUDE.md` now states in compressed form, or that a later directive retired outright.

The authoritative live rules are in `CLAUDE.md`; the agent role-specs under `.claude/agents/` carry the producer-side mechanics; `git log` is the full historical record. This file exists so that a search for a retired term (`foundation_solidity`, `rectangular floor`, `/compact`, etc.) lands on the breadcrumb instead of a dangling reference.

---

## SUPERSEDED by the VOCABULARY-SHIFT REDIRECT (2026-06-01)

The VOCABULARY-SHIFT REDIRECT (`CLAUDE.md` §Methodology invariants first bullet; full spec `METHODOLOGY-REDIRECT.md`) explicitly retired the two directives below. They were moved here from the live invariants list because leaving them inline read as still-active.

### Uniform pull-up L0→L4; foundation-solidity is a ranking weight (user directive 2026-05-31, post-cycle-040) — SUPERSEDED

The goal is a **uniform climb of the whole stack** — each layer advanced on **solid foundations below it**, NOT a single layer raced ahead of its support. This **restores the founding L0→L4 impedance-matching intent** and corrects the cycle-036-audit-driven "fill out L3 specifically" pressure, which grew L3 to 18 entries while only 5 had a same-named L2 parent and only 2 of 18 carried an L3>L2 rotation theme — a **middle-heavy stack standing on a missing floor**. **Soft weight, not a hard gate** (user decision 2026-05-31): foundation-solidity is a **strong fan-out ranking factor**, not a blocking precondition. Concretely:
- An L_{n+1} entry's ranking value is **discounted** when its L_n parent and/or its L_{n+1}>L_n rotation theme are absent or non-firm; **completing a foundation gap** (an absent L_n parent under an existing L_{n+1} entry; an unwritten L_{n+1}>L_n rotation) is **rewarded** — it ranks at or above further same-layer width or higher-layer expansion when both are eligible.
- The planner picks the **lowest incomplete layer first** when work is otherwise comparable in fan-out, so the frontier advances as a roughly level front rather than a spike.
- **Exceptions are allowed with stated rationale** (it is a weight, not a gate) — a high-fan-out higher-layer item may still be picked over a low-value foundation backfill, but the planner must say why.
- This **strengthens** "Lower-level shared vocabulary takes priority" and tilts the standing tension between "Identity-lowerings still require both L levels" and "Identity rotations across non-adjacent layers are annotated in-line" **toward present-floor coherence**. The concrete first instance is the **L2 floor under the L3 BLAS-1 / elementwise / smoother cohort**: 13 L3 entries (`dot`/`axpy`/`nrm2`/`scal`/`axpby`/`axpbypcz`, `assemble-diagonal`/`jacobi-smoother`/`divfree-projector`/`elementwise_product`/`reciprocal`/`normalize`, `chebyshev`) currently lift directly from L1 via the inline non-adjacent transitive-identity annotation, with **no L2 entry**. Under this directive, building those L2 floor entries (+ their L2>L1 identity themes) and the missing L3>L2 rotation themes is **high-fan-out foundation work, ranked above further L3 (B) substantive width**. The fan-out impact model (`scaffolding/roadmap.md` §Intermediate-tier `impact_score`) carries the matching `foundation_solidity` factor; `scaffolding/priorities.md` active head + High-fan-out backlog were reshaped to this directive (2026-05-31). This is a **ranking rebalance, not a pause** — foundation work and continued frontier work proceed together, the stack self-corrects toward rectangular cycle-by-cycle.

**Why retired:** the VOCABULARY-SHIFT REDIRECT names "the 'rectangular' success metric was the bug" and supersedes "its `foundation_solidity` / count-ownership / dual-registration rectangular-floor machinery." The live successor is the redirect's vocabulary-shift framing + "Lower-level shared vocabulary takes priority" (which the redirect keeps). Memory `project_uniform_pullup_foundation_first` is itself marked superseded by `project_vocabulary_shift_redirect`.

### Identity-lowerings still require both L levels (user directive 2026-05-27, mid-cycle-009) — SUPERSEDED

When the lower-layer form is identity-in-form to the upper-layer form — i.e., the operator's body at L_n is value-thread-isomorphic to its body at L_{n+1} and the rewrite is trivial — **the operator still gets its own entry at the lower layer.** Rationale: **each layer is coherent within itself.** A reader navigating L_n should not have to jump up to L_{n+1} to find the operator; the L_n entry exists, uses L_n vocabulary, and the L_{n+1}>L_n theme between them notes the identity. The cycle-006 audit's decision NOT to land `book/src/L3/krylov-step.md` on the rationale "L3 form is identity to L2 form" is now SUPERSEDED by this directive. Practical consequence: when a harvester or abstractor finds that a lower-layer form is identity-in-form, the work product is still an L_n entry (using L_n vocabulary) plus a thin L_{n+1}>L_n identity theme noting the no-op rewrite. Cycle-010+ harvester on `book/src/L3/krylov-step.md` is the precedent backfill; audit other L3 candidates (apply_linop, etc.) for the same pattern.

**Why retired:** the VOCABULARY-SHIFT REDIRECT explicitly supersedes "Identity-lowerings still require both L levels" — a degenerate identity-in-named-terms lowering is now a **smell** (the vocabulary failed to shift), to be resolved as a thin in-line note or a combinator re-expression, NOT a mirrored entry + thin theme. The live convention for genuine non-adjacent identity relationships is "Identity rotations across non-adjacent layers are annotated in-line" (kept in `CLAUDE.md`).

---

## History tails extracted from still-live invariants

These rules remain live in `CLAUDE.md` in compressed form; the verbose history they carried is parked here.

### `/compact` retirement detail (user directive 2026-05-29)

Live rule (compressed in `CLAUDE.md`): primary-context reset is covered by the post-meta session restart; there is no separate `/compact` step.

Extracted history: this superseded the 2026-05-27 "Compactify primary context after every meta-phase" directive. The meta-phase routinely enacts role-spec changes, so the parent restarts the Claude Code session before the next cycle (per friction-ledger `new-agent-defs-need-session-restart`); a restart resets the primary conversation entirely, which subsumes what the old `/compact` step did. The retired directive ran `/compact` at the end of each meta-phase to trim accumulated dispatch transcripts; it is removed because it is redundant with the restart. Producer-side home: `.claude/agents/meta-phase.md` §Post-meta session restart.

### Models — prior per-agent split (subsumed 2026-05-31)

Live rule (in `CLAUDE.md` §Models): all agents on `claude-opus-4-8`.

Extracted history: this subsumed the prior split (`cycle-planner` on `claude-haiku-4-5-20251001` "cheap routing"; all other agents on `claude-opus-4-7`). The cycle-planner haiku→opus escalation that the batch-10 meta-phase surfaced as an ASK (friction-ledger `cycle-planner-stale-priorities-line-recruitment`) was enacted as part of this blanket upgrade.

### Lower-level shared vocabulary takes priority — stale concrete-state tail (post-batch-1)

Live rule (in `CLAUDE.md`): when choosing between (a) expanding higher-layer vocabulary and (b) populating lower-layer shared utility, prefer (b).

Extracted (now-stale) concrete state, as of post-batch-1: `book/src/L3/` was empty (placeholder only) despite the krylov-step lowering chain being fully firm via L4>L3>L2 with no interposed L3 row; the cycle-006 "no L3 row needed for krylov-step" verdict was superseded — krylov-step should still get an L3 entry. Cycle-010+ planner should weight L3 / L2 / L1 firm operator additions above further L4 vocabulary expansion when both are eligible. Lower-layer rough-ins (the 1 firm L2 operator after 1 firm L4 chain promotes; the 0 firm L3 operators) signal the lower vocabulary needs more weight in scheduling. (This concrete snapshot is cycle-006/010-era and no longer reflects the artifact state; the principle survives, the snapshot does not.)
