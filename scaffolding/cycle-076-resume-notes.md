# Cycle-076 resume notes (batch-23 meta-phase → batch-24)

**SESSION RESTART REQUIRED before cycle-076.** The batch-23 meta-phase (post-cycle-075) edited `.claude/agents/` role-specs + `CLAUDE.md`; the parent must restart the Claude Code session so the new agent definitions load before the cycle-076 dispatch.

## Agent-defs / specs changed (why a restart is needed)

- **`.claude/agents/repairer.md`** — codified the canonical `overall_status` token set (`ready | needs-revision | reject`), forbidding `integrate`/synonyms (the recurring batch-23 slip).
- **`.claude/agents/critic.md`** — (1) the critic now sets `overall_status: ready` ON the all-pass clean report (closes the orchestrator-backfill gap — no repairer runs on a clean report) + a frontmatter-template comment line; (2) a new `surface-or-evidence` **record-definition sub-check** (DETECTS a signature-named record with no definition home — user directive 2).
- **`.claude/agents/integrator-per-report.md`** — (1) Process step 1 accepts `ready` from EITHER the critic (all-pass) or the repairer + normalizes a stray non-canonical synonym over a clean META; (2) alpha-position-insert bullet now names the FEATURE Part's by-kind groupings (user directive 1); (3) a narrate-from-on-disk-not-assumed-sibling-landing Discipline bullet; (4) the `applied_at`-is-advisory / row-order-is-authoritative annotation.
- **`.claude/agents/layer-intro-author.md`** — (1) §FEATURE-SURFACE: by-kind grouping applies to the Feature Part (3 kind groupings, within-column high→low preserved; new columns land in their grouping) (user directive 1); (2) the output-product↔driver stage-3 cross-linking convention (ratified); (3) the RECORD-definition page convention (≥2-consumer → `concepts/<record>.md`; flag undefined records) (user directive 2).
- **`.claude/agents/harvester.md`** — the record-definition obligation: define every record your signature names (single-consumer → in-chapter `## Record definition` section; ≥2-consumer → cross-ref the concept page / flag it) (user directive 2).
- **`.claude/agents/meta-phase.md`** — the standing directive-3 reorg-ownership now explicitly names the FEATURE-SURFACE Part (user directive 1).
- **`CLAUDE.md`** — §Extraction-goal: by-kind grouping applies to the Feature Part; §Methodology invariants: a new "record-definition obligation" bullet.

## What cycle-076 should pull first (from `priorities.md` CYCLE-076 active head)

The batch-24 frontier is reshaped into the CYCLE-076 active head:
1. `feature-part-by-kind-reorg-wave` (HIGH structural LEAD — run as its OWN cycle, the cycle-071 pattern; do NOT bundle with forward-frontier authoring).
2. `record-definition-pages-first-cohort` (HIGH — L4 record types + feature-surface config records).
3. `participation-ratio-l1-primitive` / 4. `port-projection-l1-home` (firm the two new rough-in reduction verbs' L1 gates).
5. `energy-fields-output-product-column` (cohort 5th-of-5) / 6. `boundary-mode-driver-leaf-column` (6th driver-leaf; gate already CLOSED-RATIFIED) — both post-reorg so they land in their grouping.
7. cross-link wiring / 8. plain-text→live-link upgrade (LOW hygiene).

No `/compact` step — the restart resets the primary context (per CLAUDE.md §Methodology invariants).
