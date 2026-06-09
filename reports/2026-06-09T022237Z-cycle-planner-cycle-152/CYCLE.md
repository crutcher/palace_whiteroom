---
agent: cycle-planner
invoked_at: 2026-06-09T022237Z
scope: cycle-152 dispatch plan (batch-50 MIDDLE 2/3 — D/E/F finalization-residue de-bulk scale-out)
status: pending
---

# Cycle 152 dispatch plan

## Goals selected this cycle

Scale out the batch-50 LEAD: the **D/E/F FINALIZATION-residue de-bulk campaign** (priorities item-1a, a GO). The c151 OPENER ran the A–F scan + the `concepts/rotation.md` PILOT (critic-verified sound). This cycle (c152, MIDDLE) and c153 (CLOSER) discharge the **26-file authoritative remaining-targets baseline** (F=13 + E=18 + D=1; 5 files overlap F+E) into disjoint, fully-parallel de-bulk dispatches, applying the `finalization-debulk` skill + the established PILOT pattern. This cycle handles **12 files** (the layer/lowering indexes L0–L3 + the L2 operator chapters); c153 handles the remaining **14** (L4 indexes + concept pages + L3/L1/L4 operator+theme chapters) and re-runs the A–F scan as the completion gate.

## Deliverable-presence verification

All 26 baseline files confirmed present on disk and carrying the expected residue sections (cwd `book/src`):

- **F-class section presence** (`grep '^## (Origin|Working Notes|Critic.s role)'`):
  - `concepts/constructed-operators.md` → `## Origin` + `## Working Notes`
  - `concepts/dependency-map.md` → `## Origin`
  - `concepts/index.md` → `## Working Notes`
  - `concepts/variant-absorption.md` → `## Critic's role` + `## Origin` + `## Working Notes`
  - `L0/index.md` `L1/index.md` `L1-L0/index.md` `L2/index.md` `L2-L1/index.md` `L3/index.md` `L3-L2/index.md` `L4/index.md` `L4-L3/index.md` → each `## Working Notes`
- **E-class date-parenthetical presence** (`grep -cE '2026-0[0-9]-[0-9]{2}'`, count>0 confirmed): black-box-vs-accelerated-kernels=1, constructed-operators=3, dependency-map=1, variant-absorption=5, L1/index=1, L2/index=1, L1/essential_dofs=1, L1-L0/essential-dofs-construction-rotation=1, L1/multigrid-relaxation-smoother=2, L2/correction_step=1, L2/inner_product=1, L2/linear_combination=1, L2/normalize=2, L2/reciprocal=1, L3/assemble_diagonal=3, L3/elementwise_product=2, L3/linear_combination=2, L4/assemble_frequency_operator=2.
- These are **de-bulk dispatches on a freshly-scanned baseline** (open by construction — the c151 OPENER produced this list this batch); the four-step already-discharged check is N/A (the work is the campaign itself, not a re-proposal). The PILOT (`concepts/rotation.md`) is the only file already discharged and is NOT in this list.

## Campaign discipline applied to EVERY dispatch (the c151 PILOT pattern, critic-verified)

Each dispatch invokes the `finalization-debulk` skill and applies:
- **STRIP wholesale:** `## Origin`, `## Working Notes`, `## Critic's role` slice-era process sections.
- **DO NOT touch `## Context` sections** — `## Context` is NOT an F-target (the c151 sweep proved it over-captures 121 legitimate per-operator orientation sections; F-class is ONLY `## Origin`/`## Working Notes`/`## Critic's role`). OQ `f-class-context-heading-orientation-vs-process-narrative`.
- **COUPLING-LIFT-AWARE:** a load-bearing static fact inside a stripped section (e.g. variant-absorption's "relationship to rotation.md" Working-Notes bullet) is LIFTED to a `## Relationship`/`## Structural fact` section, NOT deleted.
- **KEEP load-bearing structural prose on layer indexes** (L2-index fold-cohort / kernel-driver / gate-floor content) — only the slice-era `## Working Notes` cohort-growth/deleted-section log is stripped.
- **E-class:** rephrase-to-drop-the-date (drop the `2026-0X-XX` parenthetical, keep the section). KEEP governing-directive headers.
- **PRESERVE** every citation + every `[link]` + the no-frontmatter-rank `index.md` SOLE-rank-carrier dep-map status tokens EXACTLY. Inbound-anchor grep before removing any section.
- **De-dup consolidation** (where genuinely duplicated) acceptable per SEMANTIC-CONSOLIDATION "define once" — lossless only.
- **Overlap files (F+E) handled by ONE dispatch each** so a single agent applies both classes to that file.

## Dispatches — c152 WAVE (12 files, fully parallel)

- **D1 — `layer-intro-author`** — scope: de-bulk the **L0/L1 index cluster**: `book/src/L0/index.md` (F: strip `## Working Notes`), `book/src/L1/index.md` (F+E overlap: strip `## Working Notes` + drop date parenthetical), `book/src/L1-L0/index.md` (F: strip `## Working Notes`). Keep all dep-map SOLE-rank-carrier status tokens + load-bearing structural prose. — rationale: index files → layer-intro-author (owns the index narrative); clustered by adjacent layer.

- **D2 — `layer-intro-author`** — scope: de-bulk the **L2/L3 index cluster**: `book/src/L2/index.md` (F+E overlap: strip `## Working Notes` + drop date parenthetical; FOLDS IN OQ `reciprocal-stale-prose-slug-dot-l2-leaf-floor-ref` — the stale slug points at exactly this Working-Notes section being stripped, so the stale-slug reference is resolved by the strip), `book/src/L2-L1/index.md` (F), `book/src/L3/index.md` (F), `book/src/L3-L2/index.md` (F). KEEP the L2-index fold-cohort / kernel-driver / gate-floor load-bearing structural prose; strip ONLY the slice-era cohort-growth/deleted-section Working-Notes log. — rationale: index cluster; the stale-slug OQ resolves as a side-effect of the planned strip.

- **D3 — `harvester`** — scope: de-bulk the **L2 operator chapters (batch A)**: `book/src/L2/correction_step.md` (E), `book/src/L2/inner_product.md` (E), `book/src/L2/normalize.md` (E). E-class only — rephrase to drop the `2026-0X-XX` date parentheticals, keep the sections + all citations/links. — rationale: L2 operator chapters → harvester (matches operator-entry kind).

- **D4 — `harvester`** — scope: de-bulk the **L2 operator chapters (batch B)**: `book/src/L2/linear_combination.md` (E), `book/src/L2/reciprocal.md` (E). E-class only — drop date parentheticals, keep sections + citations/links. — rationale: L2 operator chapters → harvester; split from D3 to keep ≤4 files/dispatch and avoid two agents touching the same L2 chapters.

## c153 WAVE grouping (14 files — for the parent to drive next cycle; CLOSER also re-runs A–F scan)

- **C1 — `layer-intro-author`** — `book/src/L4/index.md` (F), `book/src/L4-L3/index.md` (F). Index cluster (L4).
- **C2 — `layer-intro-author`** — `book/src/concepts/constructed-operators.md` (F+E overlap), `book/src/concepts/dependency-map.md` (F+E overlap), `book/src/concepts/index.md` (F). Concept-page cluster A.
- **C3 — `layer-intro-author`** — `book/src/concepts/variant-absorption.md` (F+E+**D** overlap — `## Critic's role`+`## Origin`+`## Working Notes` strip, date-drop, AND the D-residual cycle-tags live here; COUPLING-LIFT the "relationship to rotation.md" Working-Notes bullet to a `## Relationship` section), `book/src/concepts/black-box-vs-accelerated-kernels.md` (E-only). Concept-page cluster B (carries the only D-class residue).
- **C4 — `harvester`** — `book/src/L3/assemble_diagonal.md` (E), `book/src/L3/elementwise_product.md` (E), `book/src/L3/linear_combination.md` (E), `book/src/L4/assemble_frequency_operator.md` (E). L3+L4 operator chapters.
- **C5 — `harvester`** — `book/src/L1/essential_dofs.md` (E), `book/src/L1/multigrid-relaxation-smoother.md` (E). L1 operator chapters.
- **C6 — `abstractor`** — `book/src/L1-L0/essential-dofs-construction-rotation.md` (E). L1>L0 lowering theme → abstractor (matches theme kind).
- **CLOSER gate** — after C1–C6 land, re-run the A–F book-wide residue scan as the completion gate (target: **F→0, E→governing-headers-only, D→methodology carve-out only**; the `methodology/goal-flow.md` + `meta-reviews/*` carve-out is NOT de-bulked).

## Overlap analysis

All c152 dispatches operate on **disjoint file sets** — no two dispatches touch the same file, the same operator entry, the same theme body, or the same index region:

- D1 files: `L0/index`, `L1/index`, `L1-L0/index` — distinct from all others.
- D2 files: `L2/index`, `L2-L1/index`, `L3/index`, `L3-L2/index` — distinct from all others.
- D3 files: `L2/correction_step`, `L2/inner_product`, `L2/normalize` — distinct operator chapters.
- D4 files: `L2/linear_combination`, `L2/reciprocal` — distinct operator chapters.
- D3/D4 partition L2 operator chapters with **no shared file** (correction_step/inner_product/normalize vs linear_combination/reciprocal). D2 touches `L2/index.md` (the index), NOT any L2 operator chapter — no overlap with D3/D4.
- **No shared consolidated-tally writer:** these are STRIP operations on independent files, not landings into a shared running-count. Each dispatch edits only its own files' sections. No `index.md` Working-Notes consolidated count is being *authored* (the Working-Notes blocks are being *removed*), so the parallel-blind-shared-index-count guard does not apply. The only cross-file relationship is OQ `reciprocal-stale-prose-slug-dot-l2-leaf-floor-ref`, fully internal to D2's `L2/index.md` strip (the stale slug lives in the very section D2 removes; `L2/reciprocal.md` itself is in D4 and is E-only — D4 does NOT touch any slug pointing at the L2/index section). No cross-dispatch slug forward-reference.
- **No SUMMARY.md edits** — de-bulk strips/rephrases section bodies; it does not add/remove chapters, so SUMMARY.md is untouched (no de-stub collision class).

**Verdict: all four c152 dispatches are PARALLEL (one wave).**

Inter-wave (c152 → c153): disjoint file sets, so no forward-reference ordering is forced. c153 is a separate cycle by design (campaign scale-out across the batch), not a forward-reference wave-2.

## Sequencing schedule

- **Wave 1 (parallel):** D1, D2, D3, D4 — all four de-bulk dispatches fire together; disjoint files.
- Then: 4 critics (parallel) → repairers as needed (parallel) → `integrator-per-report` ×4 (serial) → ONE `integrator-finalize` (rebuild book + commit + push). The de-bulk strips are content-removals; the finalize step-5d frontmatter-leak guard + step-5c KaTeX guard + linkcheck2 are the safety net (a stripped section that held an inbound `#anchor` would surface as a linkcheck2 break — each producer must inbound-anchor-grep before removing, per the campaign discipline).

## Open questions / caveats

- **Inbound-anchor grep is the load-bearing safety step.** Several stripped sections (esp. `## Working Notes` on the layer indexes) may be link targets from other chapters via `#working-notes` anchors. Each dispatch MUST grep the book for inbound anchors to its to-be-stripped sections before removing, and either (a) confirm none, or (b) lift the referenced content to a surviving section + repoint. The finalize linkcheck2 is the backstop, but catching it in-dispatch avoids a repair round.
- **D2 folds the `reciprocal-stale-prose-slug` OQ** — the stale slug is inside the `L2/index.md` Working-Notes section being stripped, so the strip resolves it. The integrator-per-report for D2 should mark that OQ RESOLVED-by-strip; flagging here so the meta-phase (batch-50, after c153) records the closure.
- **D-class is a single residual** living in `concepts/variant-absorption.md` (the cycle-tags), handled in c153 C3 — there is no standalone D-class dispatch.
- **c153 CLOSER re-scan is the campaign completion gate.** If the re-scan finds residue beyond the governing-headers / methodology-carve-out target, that is a c153 (or batch-50 meta-phase) follow-up, not a c152 concern.
