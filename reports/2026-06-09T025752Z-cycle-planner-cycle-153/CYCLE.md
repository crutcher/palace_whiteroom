---
agent: cycle-planner
invoked_at: 2026-06-09T025752Z
scope: cycle-153 dispatch plan (batch-50 CLOSER 3/3 — D/E/F FINALIZATION-residue de-bulk campaign completion + A–F completion-scan gate)
status: pending
---

# Cycle 153 dispatch plan

## Goals selected this cycle

CLOSER (3/3) of meta-batch-50. The batch-50 LEAD is the D/E/F FINALIZATION-residue de-bulk campaign
(`priorities.md` item-1a — the LAST finalization-residue tail; the batch-47 directive's own scope,
incompletely executed; ADJUDICATED a de-bulk-target GO by the batch-49 meta-phase). Progress to date:
13/26 targets done (c151 pilot `concepts/rotation.md` + c152 12-file scale-out wave). This CLOSER
finishes the **remaining 13 D/E/F targets** + folds in the **2 residual cleanups** the c152 wave left
(both stale-prose-pointer cases pointing at the now-stripped `L2/index.md §Working-Notes` class) and
gates on the **comprehensive A–F book-wide completion scan** — the campaign-complete signal for the
batch-50 meta-phase. NO substantive frontier dispatch (item-1a + maintenance floor only, per the
§CENTRAL-ASK posture). NO node/edge/rank/status move; the graded-stack baseline must HOLD EXACTLY.

## Deliverable-presence verification

Per the mandatory pre-dispatch paste-inline-evidence check. All 14 wave targets + 2 residuals are de-bulk
edits to EXISTING files (open by construction as de-bulk targets — the campaign itself is the prior-cycle
trail; each carries LIVE residue confirmed below). Skip the maturity/OQ-RESOLVED/structural-block gates
(this is prose/section de-bulk, not a maturity promotion — no rank or status changes).

**File existence (`ls`):** all 16 EXIST.
```
book/src/L4/index.md : EXISTS
book/src/L4-L3/index.md : EXISTS
book/src/concepts/constructed-operators.md : EXISTS
book/src/concepts/dependency-map.md : EXISTS
book/src/concepts/index.md : EXISTS
book/src/concepts/variant-absorption.md : EXISTS
book/src/concepts/black-box-vs-accelerated-kernels.md : EXISTS
book/src/L3/assemble_diagonal.md : EXISTS
book/src/L3/elementwise_product.md : EXISTS
book/src/L3/linear_combination.md : EXISTS
book/src/L4/assemble_frequency_operator.md : EXISTS
book/src/L1/essential_dofs.md : EXISTS
book/src/L1/multigrid-relaxation-smoother.md : EXISTS
book/src/L1-L0/essential-dofs-construction-rotation.md : EXISTS
book/src/L2/normalize.md : EXISTS                          (residual 1)
book/src/L3-L2/fold-solve-time-step-body.md : EXISTS       (residual 2)
```

**LIVE residue present per target (the work is real, not a no-op):**
```
L4/index.md                              F:[151:## Working Notes]                            dates:0 cyctags:0
L4-L3/index.md                           F:[57:## Working Notes]                             dates:0 cyctags:0
concepts/constructed-operators.md        F:[178:## Origin; 182:## Working Notes]             dates:3 cyctags:0
concepts/dependency-map.md               F:[229:## Origin]                                   dates:1 cyctags:0
concepts/index.md                        F:[131:## Working Notes]                            dates:0 cyctags:0
concepts/variant-absorption.md           F:[113:## Critic's role; 121:## Origin; 125:## Working Notes]  dates:5 cyctags:1 (D-class)
concepts/black-box-vs-accelerated-kernels.md  F:[]                                           dates:1 (E: line 56 "2026-06-01 blanket directive" — drop-date-keep-fact)
L3/assemble_diagonal.md                  F:[]                                               dates:3 (E)
L3/elementwise_product.md                F:[]                                               dates:2 (E)
L3/linear_combination.md                 F:[]                                               dates:2 (E)
L4/assemble_frequency_operator.md        F:[]                                               dates:2 (E)
L1/essential_dofs.md                     F:[]                                               dates:1 (E)
L1/multigrid-relaxation-smoother.md      F:[]                                               dates:2 (E)
L1-L0/essential-dofs-construction-rotation.md  F:[]                                          dates:1 (E)
```

**Residual 1 — `L2/normalize.md` stale slug present (3 sites):** `grep -n 'dot-l2-leaf-floor-vs-fold-only-design'`
→ lines 39, 109, 158 (each pairs the dead slug with a dead `L2/index §Working-Notes` referent; the
load-bearing structural content — "normalize has NO fold-parent / composite-with-no-fold-parent /
fork-invariant" — is KEPT; only the dead cross-slug + retired §-pointer drop).

**Residual 2 — `L3-L2/fold-solve-time-step-body.md` dangling §Working-Notes pointer present (1 site):**
`grep -ni 'Working.Notes'` → line 15 ("the erasure-scope taxonomy, `L3-L2/index.md` §Working-Notes")
points at the now-stripped L3-L2/index Working-Notes; rephrase to drop the dead pointer, KEEP the
"carry-threaded sibling of the opaque-library root" classification.

**Inbound-anchor safety (grep before strip):** NO inbound `[link]#origin` / `#working-notes` /
`#critic-s-role` anchors to ANY of the F-class sections being stripped (constructed-operators,
variant-absorption, dependency-map, L4/index, concepts/index, L4-L3/index) — all 4 greps returned
`none`. Safe to strip wholesale.

**D-class (variant-absorption only):** the single cycle-tag cohort is the `## Origin`/`## Critic's role`
process narration (lines 18/20/33/50/84 — "Cycle 6 back-push", "Critic applied check #8", "Cycle 7's
GMRES counter-example", `prompts/critic.md` ref). The rotation.md peer-concept coupling (lines 13/22/129
"a peer concept to rotation.md" / "this concept's relationship to rotation.md") is the COUPLING-LIFT
target → a static `## Relationship` section (NOT stripped — lifted). The `concepts/rotation` `depends-on`
frontmatter edge (line 4) is PRESERVED.

## Dispatches

The c152 6-dispatch wave is confirmed sound (matches the by-kind / by-agent grouping the campaign has used).
The 2 residuals fold in by kind: `normalize.md` (an L2 operator chapter → `harvester`) into **C5**;
`fold-solve-time-step-body.md` (a lowering theme → `abstractor`) into **C6**. Result: 6 dispatches, 16 files.

1. **C1 — `layer-intro-author`** — scope: de-bulk the layer-index F-class — `book/src/L4/index.md`
   (strip `## Working Notes` @151) + `book/src/L4-L3/index.md` (strip `## Working Notes` @57). KEEP all
   load-bearing layer-index structural prose (fold-cohort / kernel-driver / gate-floor content, the
   no-frontmatter-rank dep-map SOLE-rank status tokens, every citation + `[link]`); strip ONLY the
   slice-era cohort-growth/deleted-section narrative. No inbound anchors to the stripped sections (verified).
   deps: none.
   rationale: item-1a F-class, the 2 layer indexes in the remaining set.

2. **C2 — `layer-intro-author`** — scope: de-bulk 3 concept pages — `concepts/constructed-operators.md`
   (F: strip `## Origin` @178 + `## Working Notes` @182; E: drop the 3 dates) + `concepts/dependency-map.md`
   (F: strip `## Origin` @229; E: drop the 1 date @231) + `concepts/index.md` (F: strip `## Working Notes`
   @131). A concept page states what the concept IS — slice-era process narrative is the de-bulk target;
   KEEP the definitional body + all citations/links. deps: none.
   rationale: item-1a F+E, the concept-page cohort (3 of 5; rotation.md done c151, variant-absorption is C3).

3. **C3 — `layer-intro-author`** — scope: de-bulk 2 concept pages, incl. the ONLY D-class residual —
   `concepts/variant-absorption.md` (F: strip `## Critic's role` @113 + `## Origin` @121 + `## Working
   Notes` @125; E: drop the 5 dates; **D: COUPLING-LIFT** the "peer concept / relationship to rotation.md"
   prose — lines 13/22/129 — into a static `## Relationship` section, PRESERVING the `concepts/rotation`
   `depends-on` frontmatter edge @4; strip the cycle-N process narration in the `## Origin`/`## Critic's
   role` body) + `concepts/black-box-vs-accelerated-kernels.md` (E: line 56 — rephrase to drop the
   "2026-06-01 blanket directive" date, KEEP the fact + the superseded-by note). deps: none.
   rationale: item-1a F+E+D; isolates the campaign's only D-class file + its coupling-lift judgment into
   one dispatch (the c151 rotation.md pilot validated this coupling-lift pattern — the worked precedent).

4. **C4 — `harvester`** — scope: E-class date-drop on 4 operator chapters — `L3/assemble_diagonal.md`
   (3 dates), `L3/elementwise_product.md` (2), `L3/linear_combination.md` (2), `L4/assemble_frequency_operator.md`
   (2). Drop the `2026-0X-XX` directive-date provenance by default; KEEP the fact + any governing-directive
   header; PRESERVE every citation/link + (for the no-frontmatter-rank chapters) the `## Status` SOLE-rank
   token. deps: none.
   rationale: item-1a E-class, the 4 firm-operator chapters in the remaining set.

5. **C5 — `harvester`** — scope: E-class date-drop on 2 L1 operator chapters — `L1/essential_dofs.md` (1
   date), `L1/multigrid-relaxation-smoother.md` (2 dates) — PLUS **residual 1**: `L2/normalize.md` —
   rephrase the 3 prose sites (lines 39, 109, 158) to drop the dead cross-slug
   `dot-l2-leaf-floor-vs-fold-only-design` + its retired `L2/index §Working-Notes` referent, KEEPING the
   load-bearing structural content (normalize has NO fold-parent; composite-with-no-fold-parent;
   fork-invariant camp) — the same fix D4 applied to `reciprocal.md` in c152. PRESERVE every citation/link.
   deps: none.
   rationale: item-1a E-class L1 cohort + the normalize residual (an L2 operator chapter → harvester-kind;
   `reciprocal.md` precedent confirms this is a harvester fix).

6. **C6 — `abstractor`** — scope: E-class date-drop on 1 lowering theme — `L1-L0/essential-dofs-construction-rotation.md`
   (1 date) — PLUS **residual 2**: `L3-L2/fold-solve-time-step-body.md` — rephrase line 15 to drop the
   dangling `L3-L2/index.md §Working-Notes` pointer (now stripped), KEEPING the "carry-threaded sibling
   of the opaque-library root" classification + all citations. deps: none.
   rationale: item-1a E-class lowering-theme + the fold-solve residual (a lowering theme → abstractor-kind).

## Overlap analysis

Pairwise across {C1, C2, C3, C4, C5, C6}: **fully disjoint file sets — no shared file region, no shared
operator/theme name.** Each dispatch owns a distinct, non-overlapping set of `book/src/**` files:

- C1: `L4/index.md`, `L4-L3/index.md`
- C2: `concepts/constructed-operators.md`, `concepts/dependency-map.md`, `concepts/index.md`
- C3: `concepts/variant-absorption.md`, `concepts/black-box-vs-accelerated-kernels.md`
- C4: `L3/assemble_diagonal.md`, `L3/elementwise_product.md`, `L3/linear_combination.md`, `L4/assemble_frequency_operator.md`
- C5: `L1/essential_dofs.md`, `L1/multigrid-relaxation-smoother.md`, `L2/normalize.md`
- C6: `L1-L0/essential-dofs-construction-rotation.md`, `L3-L2/fold-solve-time-step-body.md`

No two dispatches modify the same file. No shared consolidated-index tally is co-written: these are
de-bulk STRIPS of standalone narrative sections + in-prose date/slug-drops, NOT new chapter landings into
a shared layer index — the `parallel-blind-shared-index-count-divergence` guard does NOT apply (no
consolidated count is bumped; the de-bulk REMOVES the cohort-growth-log class, it does not append to it).
No cross-report forward-reference (no dispatch references another's not-yet-existing slug — all targets
pre-exist). No floor-landing-implies-adjacent-reanchor coupling (no node/rank/status moves). **All 6 are
PARALLEL.** Per the conflict-tolerance philosophy, even if a finalize-time link nicety surfaces it is
cheap integrator merge-handling, not a reason to false-sequentialize.

## Sequencing schedule

**Wave 1 (all parallel):** C1, C2, C3, C4, C5, C6 — disjoint file sets, no forward references.

Then the standard pipeline: 6 critics → repairers on warn/fail → `integrator-per-report` ×6 (serial) →
ONE `integrator-finalize`. The A–F completion-scan gate runs AT finalize (see below).

## A–F completion-scan gate (the campaign-complete signal)

Per OQ `af-scan-de-carveout-widen-methodology-general` and `priorities.md` item-1a's completion condition
("the campaign completes when the meta-150 A–F scan returns clean"). After the wave lands, run the
comprehensive book-wide A–F residue-class scan (the exact greps live in `skills/finalization-debulk`
§"A–F residue-class scan"), with the **carve-out grep WIDENED to `methodology/` generally** (not just
`meta-reviews|goal-flow`) — `methodology/resolution-ladder.md` + `methodology/graded-stack-scheme.md`
carry DELIBERATELY-KEPT worked-example cycle refs (the `## Status`-sole-rank-carrier note lives in
graded-stack-scheme.md; both are process-explainer mirrors, not finalized-component statements).

**Target end-state (the clean-scan signal):**
- **A** (`## Verified-against` sections) → 0 book-wide.
- **B** (`verified_against:` yaml) → 0 book-wide.
- **C** (`reports/` pointers) → 0 book-wide.
- **D** (inline `cycle-NNN`/`cNNN` tags) → **methodology/ carve-out ONLY** (this CLOSER strips the last
  non-carve-out D file, `concepts/variant-absorption.md`).
- **E** (directive-date provenance) → **governing-directive-header-only** (`semantics/index.md`'s
  SEMANTIC-CONSOLIDATION header + `SUMMARY.md` KEEP; all in-prose dates dropped).
- **F** (slice-era `## Origin`/`## Working Notes`/`## Critic's role` sections) → **0 book-wide** (this
  CLOSER strips the last F files: L4/index, L4-L3/index, the 4 remaining concept pages).

**Recommendation — make the A–F completion scan the `integrator-finalize`'s responsibility, NOT a
separate audit dispatch.** Rationale: (i) the scan is a sequence of mechanical book-wide greps (the skill
defines them verbatim) — no judgment authoring, so a dedicated cross-cutter dispatch adds a full
critic+repair+integrate round-trip for zero authored content; (ii) the finalize ALREADY runs the
maintenance-floor's per-cycle two-invariant tripwire + the step-5c/5d build gates + (this batch) is the
natural home for the once-per-batch full-hygiene A–F scan the batch-49 meta-phase codified into the
maintenance-floor sweep; (iii) the scan must run AFTER all 6 per-report integrations apply (it reads the
post-wave on-disk state), which is exactly the finalize's position. Instruct `integrator-finalize` to run
the A–F scan (widened carve-out) as a step, record the per-class counts in the cycle-record / staging log
+ batch CYCLE.md, and FLAG (do not auto-fix) any residual outside the target end-state for the batch-50
meta-phase. A clean scan = the campaign-complete signal the batch-50 meta-phase reads to declare item-1a
discharged. If the scan finds residual F/non-carve-out-D (i.e. the wave under-covered), that is a
meta-phase finding (re-open a tail), not a finalize repair.

## Safety invariants (every dispatch)

- NO node / edge / rank / status / frontmatter-rank move. De-bulk is prose + `## Section` strip +
  in-prose date/slug-drop + one coupling-lift (`## Relationship` add) ONLY.
- Graded-stack baseline must HOLD EXACTLY: `files=392, typed=331, untyped=61, rank_violations=0,
  unresolved_depends_on_targets=0, promotion_frontier=11, detritus=123, true_detritus=51`. Build EXIT 0;
  step-5c KaTeX + step-5d frontmatter-leak gates clean.
- PRESERVE every citation + every `book/`-internal `[link]` + every no-frontmatter-rank `index.md`/operator
  `## Status` SOLE-rank-carrier token. NEVER touch `## Context`. Inbound-anchor grep before any section
  strip (done for the F cohort — all `none`).
- Discipline: skill `finalization-debulk` (the 3 batch-49-clarified sections: concept-page/layer-index
  narrative STRIP, directive-date rephrase-to-drop, A–F scan completeness gate) + `heading-metadata-hygiene`.

## Open questions / caveats

- **`scaffolding/integrator-signals.md` tail is stale** — the most-recent in-file section is cycle-019
  (batch-5 era); the recent entries do not appear (the file's tail-trim note references git history, but
  the current batch's signals are not surfacing in-file). This did NOT block planning — the c152→c153
  handoff is fully specified in the prompt + grounded by my on-disk deliverable-presence checks — but the
  next meta-phase (batch-50, immediately after this finalize) should confirm `integrator-finalize` is
  appending current signals and that the file isn't over-trimmed. Flagging for the batch-50 meta-phase.
- **The A–F scan carve-out widening is a methodology refinement** (OQ `af-scan-de-carveout-widen-methodology-general`):
  the carve-out moves from `meta-reviews|goal-flow` to `methodology/` generally. If the batch-50 meta-phase
  ratifies this, it should be codified into the `finalization-debulk` skill's A–F scan section (currently
  it names the narrower carve-out). Recorded here so the meta-phase catches it (per the cadence note —
  friction-ledger entry not yet present).
- **Campaign-completion posture:** this CLOSER targets a clean A–F scan = item-1a discharged. The
  strategic §CENTRAL-ASK (8th-consecutive in-scope-complete; the (A)-maintenance vs (C)-burn-handoff fork)
  remains the HUMAN's open call and is NOT this cycle's concern — the batch-50 meta-phase re-surfaces it
  once the residue tail is exhausted.
