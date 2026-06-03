---
agent: cycle-planner
invoked_at: 2026-06-03T143647Z
scope: cycle-076 dispatch plan
status: pending
---

# Cycle 076 dispatch plan

## Goals selected this cycle

Cycle-076 is the **FIRST primary cycle of meta-batch-24** (cycles 076/077/078). The batch-23 meta-phase reshaped the plan and named the **Feature-Part by-kind reorg wave** as THE STRUCTURAL LEAD (HIGH, user directive 1), explicitly flagging it as a STRUCTURAL wave best run as its OWN cycle (the cycle-071 pattern) — **do NOT bundle with forward-frontier authoring**. I honor that: **cycle-076 is the reorg-only structural cycle.** The only co-dispatch is the LOW/hygiene micro-pass (pick #8) on file regions DISJOINT from the reorg's shared structural surface — it is independent and cheap, and deferring it costs nothing but also gains nothing, so it rides this otherwise-light cycle. All forward-frontier authoring (the record-definition cohort #2, the participation-ratio/port-projection verb-firming #3/#4, the energy-fields + boundary-mode columns #5/#6) is **deferred to cycle-077+** so the new columns land directly into the reorg's by-kind groupings (the active-head sequencing directive).

## Dispatches

### D1 — `layer-intro-author` — the Feature-Part by-kind reorg wave (THE LEAD, HIGH; active-head pick #1)

- **agent**: `layer-intro-author`
- **scope**: One-time pure-structural reorg of the flat 10-column `# Feature surfaces — entry points` Part into **3 by-kind sub-chapter groupings** following the cycle-071 layer-Part structural-reorg pattern. Concretely:
  1. **Author 3 NEW group-intro pages** (all ABSENT-verified on disk — see Deliverable-presence verification):
     - `book/src/feature/spine-root.md` — the **spine-ROOT (lifecycle)** grouping intro (the top-level `main → BaseSolver` composition root that the per-feature columns hang under; 1 column: lifecycle).
     - `book/src/feature/driver-leaf.md` — the **driver-leaf** grouping intro (the 5 sim-driver columns; alpha-within-kind: driven, eigenmode, electrostatic, magnetostatic, transient).
     - `book/src/feature/output-product.md` — the **output-product** grouping intro (the family-reduction columns; alpha-within-kind: capacitance, eigenfrequency-qfactor, inductance, sparameters).
     (Slugs are the canonical group slugs for this reorg; if the author prefers `*-index.md`-style slugs they MUST still be ABSENT-verified at dispatch — but `spine-root.md` / `driver-leaf.md` / `output-product.md` are the recommended canonical slugs and are confirmed absent.)
  2. **Nest `book/src/SUMMARY.md`** — restructure the flat `# Feature surfaces — entry points` block (currently `SUMMARY.md:7-38`, an `Overview` + 30 flat column-level entries) into 3 nested sub-chapter groupings, each headed by its group-intro page, with the column-level entries nested beneath their group. **Within each column the 3 level rows STAY high→low (L4 → L1 → L0)** — the deliberate FEATURE-SURFACE exception (do NOT alphabetize the L4/L1/L0 rows). The columns sort **alpha-within-each-kind**. The top-level `Overview` (`feature/index.md`) stays.
  3. **Re-sort the `feature/index.md` matrix** — the matrix already carries `*output products*` + `*spine ROOT*` sub-headers (index.md table rows). Convert to the 3-grouping structure consistent with the SUMMARY nesting (driver-leaf / output-product / spine-ROOT), each group's rows **alpha-within-kind**, **within-column high→low PRESERVED** (do not touch the 3 level-link cells' order). Update the index prose line "the Feature Part does not use by-kind nesting yet (small-Part guard)" → reflect that by-kind nesting is now applied (directive-1 codification).
- **deps**: none (sole structural owner this cycle).
- **rationale**: User directive 1, the batch-23 meta-phase's named HIGH structural lead. Brings the now-10-column Feature Part under the project-wide directive-3 by-kind grouping convention (`feedback_mdbook_subchapter_grouping_and_alpha_api`), makes it navigable, and UNBLOCKS clean by-grouping landing of the deferred boundary-mode + energy-fields columns (cycle-077+). **PURE STRUCTURAL: ZERO count/status changes** (the cycle-071 discipline — no chapter-body edits, no `## Status` touches, no citation edits; only SUMMARY nesting + 3 new intro pages + index-matrix re-sort + the one stale "small-Part guard" prose line). Routed `layer-intro-author` (it owns group intros + the index narrative + the Feature-Part convention per its §FEATURE-SURFACE spec). Single dispatch (not a parallel set over disjoint groupings) BECAUSE the SUMMARY.md `# Feature surfaces` block + `feature/index.md` matrix are ONE shared mutable structural region — splitting it across parallel writers would re-create the parallel-blind-shared-index hazard for zero throughput gain on a light cycle.

### D2 — `lifter` — LOW/hygiene micro-pass (active-head pick #8; DISJOINT from the reorg)

- **agent**: `lifter`
- **scope**: Two cosmetic/hygiene fixes on file regions disjoint from D1's structural surface:
  1. **`driven.L4.md` plain-text → live-link upgrade** — now that `book/src/L4/sparameter_reduce.md` is on disk (verified), upgrade the plain-text `sparameter_reduce` references in `book/src/feature/driven.L4.md` (lines 55, 98, 140, 157) to live links `[`sparameter_reduce`](../L4/sparameter_reduce.md)` where they are genuine references (skill `upgrade-plain-text-ref-to-live-link-when-target-on-disk`). NOTE: line 98 ("`sparameter_reduce` is NOT authored in this chapter, mirroring how the…") and line 157's "*(output-product column; not authored here)*" annotation are deliberate forward-ref-to-sibling-column framing — the lifter judges whether each is a referenceable mention (upgrade) or a structural note about authorship locus (the slug is now real, so even these may carry a live link to `../L4/sparameter_reduce.md` since the target exists; lifter applies judgment per the skill). The `sparameters.{L4,L1,L0}.md` refs are ALREADY live links (verified on disk — D1 of c075 landed them live), so NO work there.
  2. **`electrostatic.L1.md:65` `seed (exemplar)` prose self-qualifier normalization** — re-token the in-prose `seed (exemplar)` self-qualifier (`electrostatic.L1.md:65`: "…consistent with the column being a `seed (exemplar)`, not a firm composition") → bare `seed` (the batch-22-meta-codified uniform token; the prose names the sub-kind separately). OQ `feature-column-self-status-qualifier-drift-in-prose` (c075 D5, the distinct-from-cross-ref-drift sub-kind). This is a PROSE self-qualifier, NOT a `## Status:` line token (that was already bare `seed`).
- **deps**: none (touches `driven.L4.md` body + `electrostatic.L1.md:65` prose — DISJOINT from D1's SUMMARY/index/group-intro structural surface AND from each other's file).
- **rationale**: Active-head pick #8 + the c075 integrator-signals follow-on. LOW fan-out (keeps the surfaces from drifting), but cheap and independent — rides the light reorg cycle. Routed `lifter` (the on-disk→live-link upgrade + token re-anchor is exactly its remit; skill `upgrade-plain-text-ref-to-live-link-when-target-on-disk`).

## Deliverable-presence verification

Per the MANDATORY pre-dispatch four-step check (paste-inline-evidence). D1's 3 group-intro slugs are open-by-construction (NEW structural pages with no prior-cycle history) — the relevant check is ABSENCE. D2's targets are EXISTS-and-stale (the work is an upgrade/re-token of present files).

**D1 — group-intro slugs ABSENT (must not already exist):**
```
$ ls book/src/feature/spine-root.md book/src/feature/driver-leaf.md book/src/feature/output-product.md
ls: cannot access 'book/src/feature/spine-root.md': No such file or directory
ls: cannot access 'book/src/feature/driver-leaf.md': No such file or directory
ls: cannot access 'book/src/feature/output-product.md': No such file or directory
$ ls book/src/feature/*.index.md book/src/feature/_*.md
ls: cannot access 'book/src/feature/*.index.md': No such file or directory
ls: cannot access 'book/src/feature/_*.md': No such file or directory
```
All 3 recommended canonical group-intro slugs ABSENT — D1 authors them fresh. The 10 column files (electrostatic/magnetostatic/driven/transient/eigenmode/capacitance/inductance/sparameters/eigenfrequency-qfactor/lifecycle ×{L4,L1,L0}) + `index.md` all EXIST (verified via `ls book/src/feature/`) — D1 only re-sorts their SUMMARY/index references, does NOT touch their bodies (pure-structural). The flat `# Feature surfaces` SUMMARY block is at `SUMMARY.md:7-38` (verified, 30 flat column entries + Overview), confirming the reorg target is the flat-to-nested restructure. OQ `feature-part-by-kind-nesting-output-product-cohort-grouping` is CLOSED-CODIFIED (grep of open-questions.md line 939) and migrated to plan CYCLE-076 #1 — the directive is enacted, not stale.

**D2 — `sparameter_reduce.md` link-target EXISTS (so upgrade is valid):**
```
$ ls -la book/src/L4/sparameter_reduce.md
-rw-rw-r-- 1 crutcher crutcher 22733 Jun  2 22:38 book/src/L4/sparameter_reduce.md
```
Target on disk → live-link upgrade is valid (not a dead link). Plain-text refs confirmed present in `driven.L4.md:55,98,140,157` (grep pasted in localization). The `sparameters.{L4,L1,L0}.md` refs are ALREADY live links (grep shows `[`sparameter_reduce`](../L4/sparameter_reduce.md)` form) → NO work there, scope correctly narrowed to `driven.L4.md`. The `seed (exemplar)` prose self-qualifier confirmed present at `electrostatic.L1.md:65` (grep pasted). OQ `feature-column-self-status-qualifier-drift-in-prose` is a c075 D5 needs-more follow-on (integrator-signals line 49), NOT closed → open, valid to dispatch.

**Structural-block check:** Neither dispatch is methodology-blocked. D1 is a user-directed enactment (no gate). D2 is cosmetic hygiene (no gate). Neither touches a STOP-PROPOSING-list slug (the negative list is L1/L2/L3 operator slugs — `lu_solve`/`back_solve`/`ls-update-column`/4 NLEPS atoms/`L2,L3 fe_assemble`/`L2 fold_solve`; none is a feature-surface structural or hygiene target).

## Overlap analysis

Two dispatches this cycle.

- **D1 ∩ D2**: NON-overlapping.
  - D1 writes: 3 NEW `feature/{spine-root,driver-leaf,output-product}.md` pages + `book/src/SUMMARY.md` (`# Feature surfaces` block nesting) + `book/src/feature/index.md` (matrix re-sort + one prose line).
  - D2 writes: `book/src/feature/driven.L4.md` (link bodies, lines 55/98/140/157) + `book/src/feature/electrostatic.L1.md` (line 65 prose).
  - ZERO shared file. D1 does NOT touch any column chapter body (pure-structural — only SUMMARY/index references to them); D2 touches only two column-chapter bodies. The closest contact is conceptual (both are "Feature-Part" work) but byte-disjoint. **PARALLEL-safe.**
  - One borderline: D1's `feature/index.md` matrix re-sort references the driven + electrostatic columns' level-link cells, and D2 edits the driven.L4 / electrostatic.L1 chapter BODIES — but D1 edits the index's LINK CELLS (which point AT the chapters), not the chapter bodies; D2 edits chapter bodies, not the index. No shared region. Per the conflict-tolerance philosophy (when in doubt, PARALLEL), these go parallel; any mild contact is a cheap integrator merge data-point.
- No shared running-count / consolidated-tally hazard: D1 is the SOLE author of the SUMMARY/index structural surface (single dispatch, no co-writer), so the parallel-blind-shared-index guard is N/A this cycle (it triggers only with ≥2 parallel writers into one index). D2 writes no index/SUMMARY/tally.
- No cross-report forward-reference / canonical-slug coordination needed: D1's group-intro slugs are not referenced by D2; D2's link target (`sparameter_reduce.md`) is already on disk (not a sibling-authored forward-ref).

## Sequencing schedule

**Single wave (both parallel):**
- **Wave 1 (parallel)**: D1 (reorg) ‖ D2 (hygiene micro-pass).

No forward-reference ordering between them (D2 does not reference D1's new group-intro slugs; D1 does not consume D2's link upgrades). Both land in the one `integrator-per-report` serial pass, then the single `integrator-finalize` rebuilds the book (the SUMMARY nesting + 3 new intro pages must `linkcheck2`-resolve — D1's responsibility to wire each new group-intro page into SUMMARY.md so it is not orphaned).

## Open questions / caveats

- **Light cycle by design.** This is a deliberately small cycle (the structural lead is best run alone per the active-head directive + the cycle-071 precedent). The forward-frontier work (record-definition cohort #2 [HIGH], participation-ratio #3, port-projection #4, energy-fields #5, boundary-mode #6, cross-link wiring #7) is all DEFERRED to cycle-077/078 so the new columns + restructured surface land cleanly into the reorg's groupings. cycle-077 should lead with the **record-definition-pages-first-cohort (#2, HIGH)** + the two verb-firming picks (#3/#4) now that the structural surface is settled.
- **D1 group-intro slug naming.** I recommend the canonical slugs `spine-root.md` / `driver-leaf.md` / `output-product.md` (all ABSENT-verified). If the layer-intro-author selects different slugs (e.g. `*-group.md`), the integrator must verify SUMMARY wiring + no orphan; the names are not load-bearing as long as the 3 groupings exist, each with an intro page, and within-column high→low is preserved.
- **D2 line-98/157 judgment.** `driven.L4.md:98` ("`sparameter_reduce` is NOT authored in this chapter…") and `:157` ("*(output-product column; not authored here)*") are deliberate authorship-locus notes. The slug is NOW real on disk, so a live link is technically valid, but the lifter applies the skill's judgment (a structural note about where-it-is-authored may legitimately stay a bare-code mention while the genuine references at `:55`/`:140` upgrade). Not a blocker — a critic `cross-reference-integrity` check confirms whichever the lifter chooses resolves.
- **No friction-ledger escalating pattern requires a fresh plan candidate this cycle.** The batch-23 friction items (overall_status token discipline, staging-log applied_at, per-report-integrator misnarration) were all ADDRESSED by the batch-23 meta-phase enactments (now in effect post-restart). The codemap +1-drift pattern (recurrence-6, held) is not triggered by this cycle's pure-structural + hygiene work (no NEW source citations authored). Nothing to append beyond marking #1/#8 dispatched.
