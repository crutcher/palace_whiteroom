# Cycle-085 resume notes (post-batch-26 meta-phase; SESSION RESTART REQUIRED)

**Why a restart:** the batch-26 meta-phase enacted role-spec + CLAUDE.md changes. The parent
orchestrator must **restart the Claude Code session before cycle-085** so the new definitions
load. (The restart also resets the primary conversation context — there is no separate
`/compact` step.)

## Agent-defs / methodology files that changed

- **`.claude/agents/layer-intro-author.md` §FEATURE-SURFACE** — added the **OWN-COMPOSITION
  column-promotion rule** (USER DIRECTIVE 2026-06-03; memory `project_feature_column_promotion_rule`).
  A feature column promotes off `seed` when its OWN composition + directly-owned constituents
  are firm; cross-linked SIBLING columns are references, NOT blocking constituents. Supersedes
  the prior "promote only once ALL composed constituents are firm" rule (which created the
  `eigenmode`↔`eigenfrequency-qfactor` mutual-blocking deadlock). When flipping a column's
  `status:`, re-author its promotion-rule prose to the OWN-composition rule + flip the matching
  `feature/index.md` matrix cell in the same dispatch.

- **`CLAUDE.md` §Extraction-goal (FEATURE-SURFACE SPINE)** — the authoritative codification home
  for the same OWN-COMPOSITION column-promotion rule (a new bullet after "Two sub-kinds").

## What cycle-085 does first (the batch-27 LEAD)

`scaffolding/priorities.md` §CYCLE-085 active head #1 — **`feature-column-seed-deadlock-break-re-evaluation`**:
a `layer-intro-author` pass (per column or tight cohort) re-evaluating ALL 13 FEATURE-SURFACE
SPINE columns under the new rule — re-author each column's promotion-rule prose + flip the
`status:` token (and the `feature/index.md` cell) of every column whose OWN composition +
directly-owned constituents are now firm. Columns that clearly qualify: the driver columns with
firm assemble+solve constituents (`eigenmode` = firm `fe_assemble`×3 + firm `eigsolve`;
`electrostatic`/`magnetostatic`/`driven`/`transient` per the 5-driver→L4 AFFIRMED-COMPLETE survey
c082 — verify each); the output-product columns whose reduce verb is now firm
(`eigenfrequency-qfactor` — `eigenfreq_qfactor_reduce` firm c082; `sparameters` —
`sparameter_reduce` firm c083). Columns that stay `seed`: `capacitance`/`inductance`
(`gram_reduce` rough-in), `energy-fields` (`domain_energy_reduce` rough-in), `boundary-mode` if
its own readout has no firm home.

## Standing context

- The stale `eigenmode.L4:55` clause flagged by the directive is already clean (the on-disk prose
  correctly calls `eigenfreq_qfactor_reduce` firm c082 and names the deadlock the new rule breaks).
- The `matrix-weighted-norm` √-entry-point ~30-file cascade is the convergent foundation-blocker
  for the remaining reduce-verb tail (A3 `gram_reduce` / A4 `domain_energy_reduce`); held NO-GO
  this batch, re-weigh trigger: a √-entry-point test OR a literature-anchor law-confidence pass.
