---
agent: cycle-planner
invoked_at: 2026-06-09T015655Z
scope: cycle-151 dispatch plan (batch-50 OPENER 1/3)
status: pending
---

# Cycle 151 dispatch plan

## Goals selected this cycle

Cycle-151 is the batch-50 OPENER. The batch-50 LEAD is a real campaign: **item-1a, the
`finalization-DEF-class-debulk-campaign`** — the LAST finalization-residue tail (a GO from the
batch-49 meta-phase), de-bulking the slice-era **F-class** process-narrative sections
(`## Origin`/`## Working Notes`/`## Critic's role`/`## Context` on 5 concept pages + 9 layer/lowering
`index.md` files) and the **E-class** directive-date provenance (~22 substantive files,
rephrase-to-drop-the-date). This OPENER does two things: (1) fires the **once-per-batch full-hygiene
sweep, NOW carrying the comprehensive A–F book-wide residue-class scan** (establishing the
authoritative residue baseline the campaign drives to zero); and (2) runs the **D/E/F campaign PILOT**
on `concepts/rotation.md` — the cleanest pure-process-narrative case — to verify the coupling-lift
judgment before scaling out per-file across c152/c153. No substantive frontier is dispatched (the
in-scope spine is L4-complete; deferred fronts stay consumer-gated; DIRECTIVE-1 MPI stays OUT).

## Deliverable-presence verification

Per the mandatory pre-dispatch deliverable-presence check, with pasted inline evidence:

**D1 — hygiene sweep + A–F scan (`cross-layer-cross-cutter`):** OPEN BY CONSTRUCTION — the
once-per-batch hygiene sweep is a standing per-batch duty (not a named-artifact-slug landing); it
audits, it does not author a `book/src/` file. No presence check applies. Baseline I pre-ran to
seed it (the campaign target is REAL, not stale):
```
A: grep -rlE '^## Verified-against' book/src            -> 0   (CLEAN)
B: grep -rlE '^verified_against:' book/src              -> 0   (CLEAN)
C: grep -rlE 'reports/[0-9]' book/src | grep -v meta-reviews -> 0 (CLEAN)
D: cycle/batch/wave tags (ex carve-outs) -> book/src/methodology/resolution-ladder.md,
   book/src/methodology/graded-stack-scheme.md, book/src/concepts/variant-absorption.md
E: 2026-0N-DD dates (ex carve-outs) -> 24 files
F: ^## (Origin|Working Notes|Critic's role) -> 14 files (5 concepts + 9 indexes)
```
The A/B/C classes are already clean; D/E/F are the live campaign target → the LEAD is genuinely open.

**D2 — pilot de-bulk `concepts/rotation.md` (`layer-intro-author`):**
1. File existence:
```
$ ls -la book/src/concepts/rotation.md
-rw-rw-r-- 1 crutcher crutcher 17220 Jun  8 15:20 book/src/concepts/rotation.md   (PRESENT)
```
2. Maturity / already-discharged: no `rank:`/`firmness:` frontmatter — it is a `reference`-edges-only
   concept page (frontmatter carries `edges: reference: [constructed-operators, variant-absorption]`),
   so there is NO `## Status` sole-rank-carrier token to protect on this file (safe). The
   process-narrative sections are STILL PRESENT (not yet de-bulked):
```
$ grep -nE '^## (Origin|Working Notes|Critic'"'"'?s role|Context)' book/src/concepts/rotation.md
10:## Context
87:## Critic's role     (references the DELETED prompts/critic.md)
95:## Origin
99:## Working Notes
```
   → the de-bulk is a no-op-free landing. NOT already discharged.
3. OQ-ledger RESOLVED-grep: the folded OQ is the campaign OQ `concept-page-context-origin-working-
   notes-narrative-debulk-scope` (ADJUDICATED → GO at batch-49 meta, migrated to item-1a; NOT closed
   — the campaign is the resolution). `rotation.md` is the named pilot file, not a closed slug.
4. Structural-block check: no methodology gate blocks this. The skill `finalization-debulk` (3 new
   meta-150 sections) governs; safety is NO node/edge/rank/status move + baseline-holds-exactly +
   build EXIT 0. `rotation.md` is not on any STOP-PROPOSING negative list (that list governs L3
   vocabulary backfills, not finalization de-bulk). PASSES all four checks.

## Dispatches

**D1 — `cross-layer-cross-cutter` — once-per-batch full-hygiene sweep + comprehensive A–F book-wide
residue-class scan (deps: none).**
Scope: run the standing per-batch maintenance-floor hygiene sweep, NOW including the comprehensive
**A–F residue-class scan** per `skills/finalization-debulk` §"The A–F residue-class scan". Emit the
authoritative book-wide residue baseline the batch-50 campaign drives to zero:
- A `grep -rlE '^## Verified-against' book/src` → expect 0
- B `grep -rlE '^verified_against:' book/src` → expect 0
- C `grep -rlE 'reports/[0-9]' book/src | grep -v meta-reviews` → expect 0
- D `grep -rlE 'cycle-[0-9]+|\bc[0-9]{2,3}\b|batch-[0-9]+|wave-[0-9]' book/src | grep -vE 'meta-reviews|methodology/goal-flow'`
  → enumerate the residue files; for the campaign, D-residual collapses to the methodology carve-out + the F-coupled `concepts/variant-absorption.md`
- E `grep -rlE '2026-0[0-9]-[0-9]{2}' book/src | grep -vE 'meta-reviews|methodology/goal-flow'` → enumerate (~24); split into (i) governing-directive-header keepers vs (ii) rephrase-to-drop-the-date targets
- F `grep -rlE "^## (Origin|Working Notes|Critic'?s role)" book/src | grep -vE 'meta-reviews|methodology/goal-flow'` → enumerate (the 14 = 5 concepts + 9 indexes)

Also run the per-cycle two-invariant tripwire (graded-stack linter `--json`: `rank_violations 0`,
no newly-orphaned node; detritus escalate-guard not tripped; totals held vs the c150 baseline
`files=392, typed=331, untyped=61, roots=45, rank_violations=0, unresolved_depends_on_targets=0,
promotion_frontier=11, detritus=123, true_detritus=51`). AUDIT-ONLY — moves no node/edge/rank/status,
authors no `book/src/` file. **Flag for the meta-phase:** the two `methodology/` D-class files
(`resolution-ladder.md`, `graded-stack-scheme.md`) carry worked-example cycle refs that fall OUTSIDE
the current goal-flow/meta-reviews grep carve-out but ARE methodology process-record content (the
batch-47 campaign deliberately left worked-example cycle refs in `methodology/` pages) — the A–F
scan's D/E carve-out grep should extend to `methodology/` generally, not just `goal-flow`; surface
as an OQ for the batch-50 meta so the "clean A–F scan" completion gate doesn't false-positive on
legitimate methodology process records.
Rationale: item-1 (maintenance floor) + the A–F-scan completeness gate codified at batch-49 meta;
establishes the residue baseline for the item-1a campaign.

**D2 — `layer-intro-author` — D/E/F campaign PILOT: de-bulk `book/src/concepts/rotation.md` (deps: none).**
Scope: de-bulk the slice-era process-narrative on the concept page `book/src/concepts/rotation.md`
per `skills/finalization-debulk` (the 3 new meta-150 sections). Concretely:
- **STRIP** the pure-process content of `## Context` (l.10), `## Critic's role` (l.87 — references
  the DELETED `prompts/critic.md`; pure retired-infrastructure process framing → delete the section),
  `## Origin` (l.95 — "Codified during the 2026-MM-DD meta-review …" slice-era enactment narrative),
  `## Working Notes` (l.99 — forward-process speculation "future meta-reviews should …" / "watch the
  next N cycles"). Also drop the **E-class** directive-date provenance woven into the page's prose
  (rephrase-to-drop-the-date; KEEP no governing-directive header here — this page has none).
- **LIFT** (coupling-lift-aware — this is the judgment the pilot VERIFIES) any genuine static
  structural/semantic fact buried in those sections — e.g. a "relationship to constructed-operators /
  variant-absorption" coupling — to an explicit `## Relationship to <X>` section (the pilot model is
  `L4/krylov-step.md`). The two `reference` edges to `constructed-operators` + `variant-absorption`
  are real spec content; if a stripped note anchored that coupling, re-home it as a named section,
  do NOT just delete it.
- **KEEP** the semantic DEFINITION of what "rotation" IS (the criteria, canonical examples, shape
  facts) — only the process framing is stripped, not the concept content. KEEP every citation/link
  exactly.
- **SAFETY:** `rotation.md` has NO `rank:`/`firmness:` frontmatter and NO `## Status` section, so
  there is no sole-rank-carrier token at risk; NO node/edge/rank/status move; the graded-stack
  baseline must HOLD EXACTLY; `cargo make book` EXIT 0; KaTeX `$`-sigil fence rule preserved.
Rationale: item-1a PILOT — the cleanest pure-process-narrative case, chosen to VERIFY the
coupling-lift judgment (strip-vs-lift per section) before scaling one `layer-intro-author` dispatch
per file across c152/c153. The pilot's strip/lift outcome is the template the scale-out follows.

## Overlap analysis

- **D1 × D2:** NON-OVERLAPPING. D1 is audit-only (greps + linter `--json`); it authors no `book/src/`
  file and touches no artifact region. D2 mutates exactly one file (`book/src/concepts/rotation.md`).
  D1's scan READS `rotation.md` among the F-class enumeration but does not write it; D2's de-bulk does
  not change D1's audit verdict for the rest of the corpus (D1 reports the pre-campaign baseline by
  design). No shared file region, no shared operator/slug ownership. → PARALLEL.

Only two dispatches this cycle and they do not conflict, so the overlap surface is trivial.

## Sequencing schedule

**Wave 1 (parallel):** D1 (hygiene sweep + A–F scan) ‖ D2 (pilot de-bulk `concepts/rotation.md`).

Single wave. Both land into the one `integrator-finalize`. The book is not rebuilt between them.

## Scale-out sketch for c152 / c153 (the forward plan)

The pilot (`concepts/rotation.md`) verifies the strip/lift template; c152/c153 scale it out
**one `layer-intro-author` dispatch per file, sensibly grouped**, all under the same
`finalization-debulk` skill discipline + the same SAFETY invariant (no node/edge/rank/status move,
baseline holds exactly, build EXIT 0). The remaining target set after the pilot:

- **F-class remaining concept pages (4):** `variant-absorption.md`
  (Context/Critic's-role/Origin/Working-Notes — the **coupling-lift exemplar**: lift its
  "relationship to `rotation.md`" Working-Notes bullet to a `## Relationship to rotation` section;
  this file is ALSO the D-residual subset, its remaining cycle-tags live only in these F-blocks),
  `constructed-operators.md` (Context/Origin/Working-Notes), `dependency-map.md` (Origin only —
  thinnest), `index.md` (Context/Working-Notes).
- **F-class layer/lowering indexes (9):** `L1/index.md`, `L2/index.md`, `L3/index.md`, `L4/index.md`,
  `L1-L0/index.md`, `L2-L1/index.md`, `L3-L2/index.md`, `L4-L3/index.md`, `L0/index.md` (each carries
  `## Context` + `## Working Notes`). **PRESERVE** the no-frontmatter-rank SOLE-rank-carrier dep-map
  status tokens + every citation/link exactly; **KEEP** load-bearing structural prose (the L2-index
  fold-cohort / kernel-driver / gate-floor enumerations) — only the slice-era cohort-growth-log /
  deleted-section-history is stripped (the L1-index pass model: 136→136 citations, baseline held).
  Folds in OQ `reciprocal-stale-prose-slug-dot-l2-leaf-floor-ref` (the stale slug points at the
  `L2/index.md` Working-Notes class being de-bulked — fix it when L2/index lands).
- **E-class substantive prose-date targets (~16 after excluding methodology carve-outs + the F-class
  indexes already counted):** the concept pages (`black-box-vs-accelerated-kernels.md`,
  `constructed-operators.md`, `dependency-map.md`, `variant-absorption.md` — co-de-bulk with their
  F-pass), and the operator/theme chapters (`L1/essential_dofs.md`,
  `L1-L0/essential-dofs-construction-rotation.md`, `L1/multigrid-relaxation-smoother.md`,
  `L2/{correction_step,inner_product,linear_combination,normalize,reciprocal}.md`,
  `L3/{assemble_diagonal,elementwise_product,linear_combination}.md`,
  `L4/assemble_frequency_operator.md`) — rephrase-to-drop-the-date, KEEP the structural fact.
  **EXCLUDE** as governing-directive-header / methodology carve-outs: `semantics/index.md` (its
  SEMANTIC-CONSOLIDATION header IS load-bearing), `methodology/{graded-stack-scheme,resolution-ladder,
  semantic-consolidation}.md`, `SUMMARY.md`.

**Proposed batching (one `layer-intro-author` dispatch per file; group by natural cohort to keep
each dispatch bounded and parallel-safe — distinct files never overlap):**

- **c152 wave (≈5–6 parallel `layer-intro-author` dispatches):** the 4 remaining F-class concept
  pages (`variant-absorption` [coupling-lift exemplar — do this one with care], `constructed-operators`,
  `dependency-map`, `index`) — each ALSO discharges its own E-class dates in the same pass; plus a
  start on the layer-index cohort (2–3 indexes, e.g. `L1/index.md`, `L2/index.md` [carries the OQ
  stale-slug fix], `L0/index.md`). All distinct files → fully parallel.
- **c153 wave (≈5–7 parallel `layer-intro-author` dispatches):** the remaining 6 layer/lowering
  indexes (`L3`, `L4`, `L1-L0`, `L2-L1`, `L3-L2`, `L4-L3`) + the E-class operator/theme chapters
  (`L1/essential_dofs`, `L1-L0/essential-dofs-construction-rotation`,
  `L1/multigrid-relaxation-smoother`, the L2/L3/L4 operator set) grouped 2–3 per dispatch by adjacent
  cohort. The CLOSER also re-runs the **A–F scan as the completion gate** — the campaign completes when
  F→0, E→governing-headers-only, D-residual→methodology carve-out only. All distinct files → parallel.

**Parallel-blind-shared-index guard:** the 9 layer/lowering `index.md` files are EACH owned by a
single de-bulk dispatch (one file = one owner) — there is no cross-file consolidated tally being
written here (this is de-bulk of existing prose, not new-chapter landing into a shared count), so the
dual-registration / count-owner partition does not apply. Each index dispatch owns its own file
entirely; no shared mutable aggregate.

## Open questions / caveats

- **Methodology-file D-class carve-out gap (flag for batch-50 meta, surfaced via D1).** The A–F scan's
  D/E carve-out grep currently excludes only `meta-reviews|methodology/goal-flow`, but
  `methodology/resolution-ladder.md` + `methodology/graded-stack-scheme.md` carry legitimate
  worked-example cycle refs (the batch-47 campaign deliberately left worked-example cycle refs in
  `methodology/` pages). The "clean A–F scan" completion gate will false-positive on these unless the
  carve-out grep is widened to `methodology/` generally (or those two files are explicitly enumerated
  as keepers). This is a scan-definition refinement for the meta-phase, NOT a de-bulk target — do not
  dispatch them.
- **Coupling-lift judgment is the pilot's deliverable.** The whole point of pilot-first is to confirm,
  on `rotation.md`, that the strip-vs-lift call per section is sound before scale-out. If the pilot
  surfaces a case where a `## Context`/`## Working Notes` block carries a genuine static coupling that
  is awkward to re-home (rather than cleanly strippable), that is a finding to carry into the c152
  scale-out scope (especially for `variant-absorption.md`, the explicit coupling-lift exemplar). The
  c152 dispatch scopes should be written AFTER reading the pilot's outcome.
- **No substantive frontier dispatched, by design.** The in-scope spine is L4-complete (8th
  consecutive in-scope-complete batch); the strategic §CENTRAL ASK (maintenance-with-residue-yield vs
  the meta-recommended downstream-burn handoff vs re-scope) is the HUMAN'S call and remains open — the
  batch-50 planner LEADS with item-1a + the maintenance floor only, per the batch-49 meta directive.
