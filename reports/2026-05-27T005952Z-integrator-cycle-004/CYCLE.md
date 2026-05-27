---
agent: integrator
invoked_at: 2026-05-27T00:59:52Z
scope: cycle-004 batch integration
status: applied
inputs:
  - reports/2026-05-27T004641Z-layer-intro-author-concepts-dot-rewrite/
  - reports/2026-05-27T004641Z-layer-intro-author-L1-index-refresh/
  - reports/2026-05-27T004641Z-harvester-scal-L1/
  - reports/2026-05-27T004641Z-harvester-apply_linop-L1/
  - reports/2026-05-27T004641Z-harvester-axpbypcz-L1/
  - reports/2026-05-27T004641Z-abstractor-MINRES-L1-L0/
  - reports/2026-05-27T004641Z-abstractor-BiCGStab-L1-L0/
integrated_at: 2026-05-27T01:00:00Z
integration_commit: b8332b98300205740c4be4a9b1a2b30a2743dee3
---

# REPORT: Integrator batch — cycle-004

## Summary

Cycle-004 wave-1 integration: **7 reports, all `ready` post-repair, all applied**. New theme category `obstruction` introduced at L1>L0 (2 themes); L1 vocabulary expanded from 4 to 7 firm operators plus 6 rough-in (obstruction) operators; L1 layer intro refreshed; `concepts/dot.md` rewritten to fix three cycle-003 contradictions; one secondary edit (`L1/dot.md:17` back-pointer softening). Zero safety-net gate hits. Zero structural conflicts at integration — the parallel-when-in-doubt philosophy held cleanly through 7 wave-mates with substantial file overlap.

## Reports applied

| Report | Agent | Scope | Status | Follow-up |
|---|---|---|---|---|
| `concepts-dot-rewrite` | layer-intro-author | rewrite `book/src/concepts/dot.md` + softening edit `L1/dot.md:17` | ready | null |
| `L1-index-refresh` | layer-intro-author | refresh `book/src/L1/index.md` intro + dep-map prose | ready | null |
| `harvester-scal-L1` | harvester | firm L1 operator: `scal` (9 laws, 1 axis + sub-axis) | ready | null |
| `harvester-apply_linop-L1` | harvester | firm L1 operator: `apply_linop` (7 laws, 3 axes + 1 collapsed) | ready | null |
| `harvester-axpbypcz-L1` | harvester | firm L1 operator: `axpbypcz` (12 laws, 2 axes + 1 internal-L0) | ready | null |
| `abstractor-MINRES-L1-L0` | abstractor | **obstruction** L1>L0 theme `minres-iteration` + 3 rough-in ops | ready | meta-phase |
| `abstractor-BiCGStab-L1-L0` | abstractor | **obstruction** L1>L0 theme `bicgstab-iteration` + 3 rough-in ops | ready | meta-phase |

## Reports deferred / rejected

None.

## Artifact changes

### Created (5 files) and rewritten (2 files)

- `book/src/L1/scal.md` (new)
- `book/src/L1/apply_linop.md` (new)
- `book/src/L1/axpbypcz.md` (new)
- `book/src/L1-L0/minres-iteration.md` (new)
- `book/src/L1-L0/bicgstab-iteration.md` (new)
- `book/src/concepts/dot.md` (rewrite — whole-file replacement)
- `book/src/L1/index.md` (rewrite — full intro refresh + extended dep-map)

### Edited (2 files)

- `book/src/L1/dot.md` — 1-line softening of back-pointer warning at line 17.
- `book/src/SUMMARY.md` — 5 new chapter lines (3 firm L1 + 2 L1>L0 themes). L1>L0 themes alphabetical (`bicgstab-iteration` then `minres-iteration`) per planner anchor-merge note.

The L1/index.md write merges (a) the intro refresh structure (Context / Semantics / new Vocabulary-cohort subsection / Working Notes) with (b) the dep-map verbatim from the refresh, then extended with 9 new rows: 3 firm (`scal`, `apply_linop`, `axpbypcz`) + 6 rough-in obstruction (3 from MINRES theme + 3 from BiCGStab theme).

### Scaffolding updates

- `scaffolding/open-questions.md` — 25 new questions appended; 9 marked `answered`.
- `scaffolding/roadmap.md` — Layered-spec progress section updated for cycle-004 (7 firm + 6 rough-in obstruction L1 operators; 3 L1>L0 themes; new obstruction-theme classification noted).
- `scaffolding/cycle-record.jsonl` — 1 line appended for cycle-004 integration record.
- `scaffolding/integrator-signals.md` — cycle-004 section prepended above cycle-003 (newest-first per file format) with all 6 subsections (Unblocked, New dependencies, Resolution implications, Suggested next dispatches, Wave-conflict observations, Integration-tooling friction).

### Log

- `log/cycle-004.md` — created (legacy cycle-4 file renamed to `log/cycle-004-legacy.md` to preserve historical record).
- `log/README.md` — cycle-004 entry prepended to the newest-first index.

## Safety-net gates — hit count by gate type

| Gate | Hits |
|---|---|
| retroactive-budget per-slice ≥3 | 0 |
| retroactive-budget global ≥4 | 0 |
| concept_writes on existing slug | 0 |
| forward-edge claim without surface | 0 |
| edge-label / prose mismatch | 0 |
| H1 reuses page heading | 0 |
| append on missing slug | 0 |
| variant-axis missing on multi-variant operator | 0 (apply_linop 3+1; axpbypcz 2+1; both correctly classified) |
| bookkeeping incomplete | 0 |
| SUMMARY.md chapter registration auto-fix | 0 (all reports proposed SUMMARY edits) |

**Total gate hits: 0.**

## Wave-conflict observations

- **L1/index.md row-append at scale**: 9 dep-map row appends from 5 wave-mates (3 harvesters add firm rows; 2 abstractors add 3 rough-in rows each). Each row distinct → merged cleanly in dep-map row order (firm first, rough-in by emit order: MINRES then BiCGStab per planner note). **Positive signal that the parallel-when-in-doubt philosophy generalises from 2-wave-mates (cycle-003) to 5-wave-mates (cycle-004) on the same shared file.**
- **SUMMARY.md L1 Part**: 3 firm-operator chapter lines chained after `axpby` line; no conflict.
- **SUMMARY.md L1>L0 Part**: 2 theme chapter lines both wanted `append-after axpby-mutation-rotation`. Resolved alphabetically per planner pre-decision (`bicgstab-iteration`, `minres-iteration`). Zero friction at integration.
- **L1/dot.md two-writer pseudo-conflict**: only `concepts-dot-rewrite` writes (1-line edit); planner conflict analysis was over-cautious. No actual conflict.
- **L1/index.md merged refresh + append**: the `L1-index-refresh` report rewrote the intro structure while 5 wave-mates appended dep-map rows. Refresh preserved the dep-map table verbatim per its own discipline; integrator extended the preserved table with 9 new rows. Clean composition.

## Build status

`cargo make book` — see commit (run after writes). Pre-existing katex-link warnings unchanged. No new breakage.

## Open questions promoted (25 new) — see `scaffolding/open-questions.md`

## Open questions answered (9) — see `scaffolding/open-questions.md`

## Notes for meta-phase

1. **New theme category `obstruction`**. Cycle-004 introduces `L1>L0 themes where the L0 anchor is empty`. Two themes in this cycle (MINRES, BiCGStab) both grouped under one Palace `MFEM_ABORT` branch. Friction-ledger candidate `advertised-but-unimplemented-krylov-solvers` filed.
2. **MFEM-as-L0-substrate policy** is now load-bearing. Three downstream open questions and the entire MINRES/BiCGStab L1>L0 surface depend on this decision. Routes to meta-phase as an `ask` item.
3. **Subagent-skips-Edit pattern recurred** — cycle-002 (haiku) and cycle-004 (opus). Crossed model tier. Routes to meta-phase under open question `subagent-skips-edit-on-explicit-instruction`.
4. **`scalar-promotion-typing-rule` cross-operator pattern at 5 operators**. Well past any threshold for promotion above per-operator prose. Cycle-planner should escalate.
5. **`vocabulary-cohort-subsection-as-layer-intro-pattern`** — cycle-004 introduced a new sub-section (Firm / Rough-in / Queued split) in L1 intro. Candidate for promotion to standard layer-intro pattern.
