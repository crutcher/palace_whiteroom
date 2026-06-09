---
agent: cycle-planner
invoked_at: 2026-06-09T045352Z
scope: cycle-154 dispatch plan (batch-51 OPENER, 1/3) + batch-51 convergence sketch
status: pending
---

# Cycle 154 dispatch plan — batch-51 OPENER (1/3)

## Goals selected this cycle

The human directive for batch-51: **"drive the finite maintenance backlog to convergence"** — clear the
remaining bounded hygiene work so only the perpetual maintenance floor + the consumer-gated deferred fronts
remain. This OPENER cycle does two things: (D1) the **once-per-batch full-hygiene sweep** (the standing
maintenance-floor item-1, including the comprehensive A–F residue-class scan) augmented with the
**authoritative CLASSIFICATION of the 61 untyped nodes** into carve-out-by-design vs genuine-edge-typing-target
(producing the dispositions (a)/(b)/(c) the c155/c156 enactment consumes); and (D2/D3) the **3 small migrated
fold-in de-bulks** (all LOW/hygiene `concepts/`+`feature/` touches). This is a CLASSIFICATION + bounded-hygiene
cycle, NOT a substantive frontier cycle — the in-scope forward-frontier R&D is complete (9th consecutive
batch), and the §CENTRAL ASK remains the human's call.

**Headline finding the classification establishes (parent-confirmed, re-verified on-disk this cycle):** the
`untyped=61` is DOMINATED by legitimately-untyped-BY-DESIGN pages, NOT genuine edge-typing debt. The exact
on-disk breakdown (`graded_stack_lint.py --json`, this cycle): **26 `L0/` + 26 `meta-reviews/` + 5 `methodology/`
+ 4 navigational (`SUMMARY`, `introduction`, `design/index`, `semantics/index`)**. ZERO genuine-untyped DAG
nodes remain after the carve-out. The lint's `node.untyped = (rank is None AND no typed edges)` is a WARNING
(warn-not-fail, line 635); `rank_violations = 0` holds; this breaks NO invariant. So "drive to convergence" =
**a lint carve-out-predicate refinement + a one-line methodology note**, NOT a 61-file authoring campaign.

## Deliverable-presence verification

All four-step checks run with pasted inline evidence (skill `verify-dispatch-scope-not-already-discharged`).

**D1 (`cross-layer-cross-cutter` full-hygiene sweep + 61-untyped classification)** — OPEN BY CONSTRUCTION
(audit-class; the per-batch maintenance-floor sweep fires once per batch at the OPENER; the c151 OPENER was the
prior batch's instance; no prior-cycle classification artifact exists for batch-51). No `book/` named-slug
deliverable (audit-only; the sweep's deliverable is a CLEAN-BILL verdict + the classification dispositions, not
a chapter). Baseline re-confirmed on-disk this cycle: `files 392, typed 331, untyped 61, roots 45,
rank_violations 0, unresolved_depends_on_targets 0, promotion_frontier 11, detritus 123, true_detritus 51,
reference_reachable 247, expected_unreachable_outside_dag 54` (matches the held batch-50 baseline exactly).

**D2 (`feature-l4-h1-convention-tail-normalize`)** — target files present; partial-state confirmed:
```
$ for f in feature/*.L4.md; do grep -m1 '^# ' $f; done   # output-product columns:
# capacitance — L4 composition-root                       <- MISSING (output product)
# inductance — L4 composition-root (output product)       <- HAS
# sparameters — L4 composition-root                        <- MISSING (output product)
# eigenfrequency-qfactor — L4 composition-root (output product)  <- HAS
# energy-fields — L4 composition-root (output product)     <- HAS
# waveguide-mode — L4 composition-root (output product)    <- HAS
```
The 6 output-product columns are `capacitance`/`inductance`/`sparameters`/`eigenfrequency-qfactor`/
`energy-fields`/`waveguide-mode`; **exactly 2 (`capacitance`, `sparameters`) are MISSING** the `(output product)`
tail. The normalize adds it to those 2; leaves the spine-ROOT (`lifecycle`, `krylov-iteration`), driver-leaf
(`driven`/`eigenmode`/`electrostatic`/`magnetostatic`/`transient`/`boundary-mode`), and kernel-composition
(`geometric-multigrid`, `matrix-free`) tails AS-IS. **OPEN** (the inconsistency is on-disk).

**D2 (`dependency-map-dateless-meta-review-n-refs-debulk`)** — `concepts/dependency-map.md` present; the
date-less E-sub-class confirmed on-disk:
```
$ sed -n '92,94p' concepts/dependency-map.md
... Codified meta-review #1; expanded with carry-through clause meta-review #2.
... levels-of-absorption refinement meta-review #3 (invariant / procedural / primitive-sequence).
```
Three `meta-review #N` clauses to rephrase-drop (carry-through facts already in `rotation.md`/`variant-absorption.md`).
**OPEN.** OQ-grep: `grep 'dependency-map.*RESOLVED' scaffolding/open-questions.md` → no matches (not yet closed).

**D2 (`constructed-operators-duplicate-concept-body-dedup`)** — `concepts/constructed-operators.md` present; the
DUPLICATE concept body confirmed on-disk:
```
$ grep -n '^## ' concepts/constructed-operators.md
... 167:## Relationship to burn's `Module`
171:## Use in GMRES / FGMRES
175:## Concept: constructed operators     <- DUPLICATE block start (re-states §11-171)
189:## When to use
202:## Canonical example
213:## Slices that use this methodology    <- DUPLICATE block end
```
The §175-213 block re-states the page's own earlier §11-171 (`## Context` / `## When to construct` /
`## Worked example` / `## Relationship to existing concepts`). De-dup the second block; verify no inbound
`book/`-internal anchor targets the duplicate headings. **OPEN.** Structural-block check: NONE — this is a
content-redundancy de-dup, not gated by any methodology invariant (a different defect class from process
accounting, per friction `completeness-claim-vs-comprehensive-scan`); the FINALIZATION static-state invariant
permits it (de-dup loses no spec/citation; baseline must HOLD EXACTLY).

STOP-PROPOSING negative-list check: none of the three de-bulks nor the sweep matches a disqualified slug
(`lu_solve`/`back_solve`/`ls-update-column`/`nleps_*`); all are hygiene touches, not L3 backfills.

## Dispatches

**D1 — `cross-layer-cross-cutter`** — scope: *batch-51 OPENER full-hygiene maintenance sweep + authoritative
classification of the 61 untyped nodes.* Two parts, single audit dispatch (no `book/` mutation expected):
  - **(part 1) the standing per-batch full-hygiene sweep** (maintenance-floor item-1): re-confirm the RE-set
    premises HELD (RE4 consumer-gated / the sharding §2g-extension member solve-generalization-consumer-gated /
    the RE11 reference-only-reachable cohort §2g-by-design); the **semantic-surface liveness refresh**
    (`semantics/index.md` §0.1 + SEMANTIC-CONSOLIDATION governing header KEEP + intact — no semantic rule lost);
    the **kernel-API/impl integrity check** (the 3 `realizes-kernel-api` edges stay `reference`-class:
    triangular-solve-obstruction, eigsolve-impl, fe-assemble-libceed-boundary-obstruction); the **DIRECTIVE-1
    MPI boundary** intact (no sharding/MPI in scope); the **FINALIZATION static-state-surface liveness**
    (producers not re-accreting process accounting); AND the **comprehensive book-wide A–F residue-class scan**
    (A `## Verified-against` / B `verified_against:` / C `reports/` / D inline cycle-tags / E directive-date +
    the date-less `meta-review #[0-9]` arm / F slice-era narrative; exact greps in `finalization-debulk` skill
    §"A–F residue-class scan"; `## Context` is NOT an F-target — the orientation-vs-process distinction). Show a
    clean book-wide GREP per residue class, not a self-characterized tally. **Note the 3 D2/D3 de-bulk targets
    are KNOWN-and-being-fixed-this-cycle** (the date-less `meta-review #N` E-sub-class + the duplicate-body) —
    the sweep confirms NO OTHER instances of those two sub-classes exist book-wide.
  - **(part 2) the authoritative 61-untyped classification** (the convergence deliverable): partition all 61
    `untyped` nodes (from `graded_stack_lint.py --show-untyped`) into the three disposition buckets, producing
    the authoritative dispositions the c155/c156 enactment consumes:
      - **(a) carve-out-by-design — the ~35 non-DAG pages:** the **26 `meta-reviews/`** (process records — a
        carve-out exactly like the existing `methodology/`/`design/` `OUTSIDE_DAG_PREFIXES`); the **5
        `methodology/`** (`goal-flow`, `graded-stack-scheme`, `overview`, `resolution-ladder`,
        `semantic-consolidation` — the reader-facing methodology MIRROR; ALREADY in `OUTSIDE_DAG_PREFIXES` for
        *reachability* but still flagged `untyped` because they carry no `rank:`/`edges:` — the untyped axis is
        separate from reachability); the **4 bare navigational** (`SUMMARY`, `introduction`, `design/index`,
        `semantics/index` — outside-DAG structural pages). Disposition: these belong OUTSIDE the `untyped`
        WARNING — analogous to the existing `expected_unreachable_outside_dag` category.
      - **(b) the 26 `L0/` leaf-layer disposition:** L0 is the **ground-truth leaf layer** — file-overview
        reference notes + convention/pattern intros (`linalg-vector-file`, `conventions-intro`, …), cited BY L1
        with NOTHING below to `depends-on`, carrying NO `## Status` line (verified: zero of the 26 have a
        `## Status` heading) and NO maturity rank because they ARE the ground truth (scheme §5 framing; the
        `resolution-ladder` treats L0 as the evidence floor). Disposition (planner-RESOLVED — see §"L0
        disposition read" below): **carve out `L0/` as the ground-truth leaf layer**, uniform with the
        `meta-reviews/` carve-out — NOT author 26 rank markers.
      - **(c) genuine-untyped DAG node remainder:** enumerate any node NOT in (a)/(b) that is a real DAG node
        carrying claims but lacking `rank:`/`edges:`. **Expected: ZERO** (the on-disk breakdown is exactly
        26+26+5+4 = 61, fully absorbed by (a)+(b)). If the sweep finds any, list it explicitly as the genuine
        edge-typing residue for c156.
    Deliverable: a CLEAN-BILL verdict (or itemized findings) + the explicit (a)/(b)/(c) node-lists, which the
    c155 lint-refinement and the c156 confirm consume. — rationale: maintenance-floor item-1 (the once-per-batch
    sweep) + the human's "drive the finite backlog to convergence" directive (the classification IS the
    convergence work — it establishes that the 61-untyped is carve-out-by-design, reducing the "large-looking"
    `p1-edge-typing-true-detritus-sweep` to a bounded tooling refinement).

**D2 — `layer-intro-author`** — scope: *the 3 small migrated fold-in de-bulks (concepts/ + feature/ hygiene
touches), bundled into one dispatch.* All three are LOW/hygiene `layer-intro-author`-owned touches with no
inter-dependency and no shared file region beyond the `concepts/` directory (distinct files):
  - **(i) `feature-l4-h1-convention-tail-normalize`** (`feature/capacitance.L4.md`, `feature/sparameters.L4.md`):
    append ` (output product)` to the L4 H1 of the 2 output-product columns currently missing it, making all 6
    output-product columns' L4 H1 tails uniform. Leave spine-ROOT / driver-leaf / kernel-composition tails AS-IS
    (the `heading-metadata-hygiene` skill: short distinguishing glosses are KEPT for TOC-navigability; this is a
    UNIFORMITY normalize, not a strip).
  - **(ii) `dependency-map-dateless-meta-review-n-refs-debulk`** (`concepts/dependency-map.md:92-93`):
    rephrase-to-drop the three date-less `meta-review #1/#2/#3` process clauses; the carry-through FACTS
    (rotation's carry-through clause; variant-absorption's levels-of-absorption refinement) are already stated
    in `rotation.md` / `variant-absorption.md` — keep the concept descriptions, drop the `meta-review #N`
    provenance tails. Discipline: `finalization-debulk` skill §"Date-LESS `meta-review #N` refs".
  - **(iii) `constructed-operators-duplicate-concept-body-dedup`** (`concepts/constructed-operators.md:175-213`):
    de-dup the second concept body (`## Concept: constructed operators` / `## When to use` / `## Canonical
    example` / `## Slices that use this methodology`) which re-states the page's own §11-171; keep the canonical
    first block. **Verify no inbound `book/`-internal anchor targets the duplicate headings** before deletion
    (`grep -rn 'constructed-operators.*#concept-constructed\|#when-to-use\|#canonical-example\|#slices-that-use'
    book/src/`); if an anchor targets a duplicate heading, re-point it to the canonical-block heading.
  - **Safety (all three):** the graded-stack baseline must HOLD EXACTLY (these are prose-only edits to
    non-DAG / feature-H1 surfaces — no node/edge/rank/status/semantics move); build EXIT 0; no `book/`-internal
    link broken. — rationale: maintenance-floor items 2/4/5 (the 3 migrated LOW/hygiene follow-ups); the human's
    "drive the finite backlog to convergence" directive names these 3 small de-bulks explicitly as part of the
    finite backlog.

## Overlap analysis

- **D1 × D2** — NON-overlapping. D1 is audit-class (reads the whole book + the lint JSON; produces a verdict +
  classification node-lists; **no `book/` mutation**). D2 writes 3 distinct `concepts/`+`feature/` files
  (`capacitance.L4`, `sparameters.L4`, `dependency-map`, `constructed-operators`). D1 does NOT write any file
  D2 touches. The only nominal contact: D1's A–F scan READS `dependency-map.md` + `constructed-operators.md`
  (the 2 files D2 edits), but D1 is explicitly briefed that those 2 de-bulk targets are KNOWN-and-being-fixed
  this cycle (so D1 confirms no OTHER instances exist, it does not re-flag the known ones as new findings) — a
  read-vs-write relationship, not a write-write conflict. **PARALLEL.** (Per the conflict-tolerance philosophy:
  even if D1's verdict prose and D2's edits mildly relate, that surfaces as a cheap integrator-signal data
  point, not a blocking conflict; false-sequentialization is the worse error here.)
- **D2-internal (i)/(ii)/(iii)** — the three de-bulks touch DISTINCT files (`feature/capacitance.L4.md` +
  `feature/sparameters.L4.md`; `concepts/dependency-map.md`; `concepts/constructed-operators.md`) — no shared
  region. Bundled into ONE dispatch for efficiency (all `layer-intro-author`-owned hygiene, all small), not for
  conflict reasons. No shared running-count / consolidated tally is touched (the feature H1 normalize is per-file
  text; the 2 concept de-dups are per-file prose) — the parallel-blind-shared-index guard does not apply.

No shared consolidated-tally / layer-index running-count is written by any dispatch this cycle (no harvester /
no new chapter landing into a layer index), so the dual-registration / count-owner partition does not apply.

## Sequencing schedule

**Single wave (both dispatches parallel).** D1 (audit + classification, no mutation) and D2 (3 distinct-file
hygiene de-bulks) are non-overlapping and have no forward-reference dependency on each other. One wave →
2 critics → repairer (only if a finding) → `integrator-per-report` ×2 (serial) → ONE `integrator-finalize`
(rebuild + commit + push + housekeeping; step-5c KaTeX + step-5d frontmatter-leak gates; baseline-HOLD-EXACTLY
tripwire). Expected baseline after this cycle: HELD EXACTLY (`untyped 61` UNCHANGED — the classification is a
verdict, it does not change any node's typing; the 3 de-bulks touch non-DAG/feature-H1 surfaces only).

## L0 disposition read (the methodology question — RESOLVED at the planner level)

**The question:** do the 26 `L0/` ground-truth notes get a leaf/`firm`-equivalent rank marker (so they read as
"typed"), OR are they formally carved out as the ground-truth leaf layer (like `meta-reviews/`)?

**My read — RESOLVABLE at the planner/tooling level, NO meta-phase methodology decision required: CARVE THEM
OUT.** The graded-stack scheme already implies this; it is not a new methodology call. Evidence:

1. **The scheme §5 + resolution-ladder already frame L0 as the ground-truth evidence floor that carries no
   maturity rank.** Scheme §1: the `rank:` total order is over *constructive resolution* (`roadmap_goal < stub <
   rough-in < firm`). L0 is not *constructively resolved* — it IS the ground truth that resolution rests on
   (`L0/index.md`: "L0 is the evidence floor. Every claim higher in the stack carries an L0 citation as its
   anchor."). A `firm`-equivalent rank on L0 would be a category error: `firm` means "rests only on firm deps,"
   but L0 rests on NOTHING in-book (it IS the bottom). The well-foundedness invariant `rank(u) ≤ min(deps)` is
   vacuous for a node with no `depends-on` deps below it.
2. **All 26 L0 files are file-overview reference notes / convention intros / pattern notes** (verified:
   `linalg-vector-file` = "a file-overview reference note for L1 entries"; none carries a `## Status` line; none
   carries `rank:`/`edges:`/`firmness:` frontmatter). NONE is a record-definition / concept DAG node that an L1
   entry would `depends-on` for *resolution* — they are cited as *evidence* (the `cites-evidence` relationship,
   which already lives on the L1 side as the L1 op's `depends-on … kind: cites-evidence` edge into L0). The
   resolution edge into ground truth is recorded ON THE CONSUMER (L1), not as an L0-outbound edge.
3. **This is structurally identical to the existing `methodology/` + `design/` `OUTSIDE_DAG_PREFIXES` carve-out**
   (lint line 735) and the `meta-reviews/` case in part (a): a layer of pages that is NOT in the resolution DAG,
   that should never carry rank/edges, and that should not read as either detritus or untyped-debt. Adding `L0/`
   (and `meta-reviews/`) to `OUTSIDE_DAG_PREFIXES` is the minimal, scheme-aligned fix — the same mechanism, one
   more prefix.

**The minor caveat I flag for the c155 enactment (NOT a blocker, NOT a meta-phase call):** the `untyped` flag
(`node.untyped = rank is None AND no typed edges`, line 571) is a SEPARATE axis from `is_likely_outside_dag`
(which governs only the reachability detritus-vs-expected-unreachable split). Today `methodology/` files are
`OUTSIDE_DAG` for *reachability* yet STILL counted `untyped` (they have no `rank:`/`edges:`). So carving `L0/` +
`meta-reviews/` into `OUTSIDE_DAG_PREFIXES` fixes their *reachability* classification but does NOT by itself drop
them from the `untyped` WARNING count. The convergence fix in (a) is therefore TWO coupled lint touches: (1)
extend `OUTSIDE_DAG_PREFIXES` to `("methodology/", "design/", "L0/", "meta-reviews/")` + add the 2 bare
navigational pages (`SUMMARY`, `introduction`) by name to an `OUTSIDE_DAG_EXACT` set; AND (2) make the `untyped`
summary count EXCLUDE `is_likely_outside_dag` pages (an outside-DAG page is untyped-BY-DESIGN, not pre-P1 debt) —
so the headline `untyped` reflects only genuine DAG-node typing debt. This is a small, well-contained
`tools/graded-stack-lint` definition refinement (Medium-cascade tooling, proposable — `feedback_tooling_changes_proposable`),
NOT a methodology decision, and it leaves all HARD invariants untouched (`rank_violations`,
`unresolved_depends_on_targets` are computed over `depends-on` edges, of which outside-DAG pages have none).

**Net: the L0 disposition is a planner-resolvable MECHANICAL call (carve-out, uniform with meta-reviews), and
the c155 enactment is a bounded `tools/` lint-definition refinement + a one-line scheme §5 note ("the L0
ground-truth leaf layer and the meta-reviews/ process-record layer are outside-DAG carve-outs; they carry no
rank because they are not constructively-resolved DAG nodes").** I do NOT route this to the meta-phase. (If the
c154 D1 classification surfaces any L0 file that IS a genuine record/concept DAG node — none expected — that
single file would be typed normally rather than carved out, and I'd flag it for the meta-phase; but the on-disk
evidence says zero.)

## Batch-51 convergence sketch (c155/c156)

The c154 OPENER establishes the authoritative classification; c155/c156 enact it and confirm convergence. The
remaining work is SMALL and bounded — this batch genuinely converges the finite maintenance backlog.

**c155 (batch-51 middle) — enact (a) + (b): the lint carve-out refinement.** ONE dispatch (a `tools/`-touch;
route as a `cross-layer-cross-cutter` or a direct tooling change per the orchestrator's preference — it is a
`tools/graded-stack-lint/graded_stack_lint.py` edit + a one-line `methodology/graded-stack-scheme.md` §5 note,
NOT a `book/src/` chapter, so it is outside the producer-role partition; likely the orchestrator applies the
tooling diff directly with the classification node-lists from c154 D1 as the spec). Content:
  - **(a)** extend `OUTSIDE_DAG_PREFIXES` → `("methodology/", "design/", "L0/", "meta-reviews/")`; add an
    `OUTSIDE_DAG_EXACT = {"SUMMARY", "introduction"}` set checked in `is_likely_outside_dag` (the `design/index`
    + `semantics/index` already match the `/index` suffix rule); make the `untyped` summary count EXCLUDE
    `is_likely_outside_dag(slug, node)` pages (the two coupled touches from §"L0 disposition read" caveat).
  - **(b)** the L0 leaf-layer disposition IS the `L0/` prefix addition in (a) — no separate file authoring; the
    one-line scheme §5 note records the carve-out rationale.
  - **Verification:** re-run `graded_stack_lint.py --json`; expect `untyped` to drop from 61 toward ~0 (61 −
    26 L0 − 26 meta-reviews − 5 methodology − 4 navigational = 0, IF no genuine-untyped remainder from c154
    (c)); `rank_violations 0` + `unresolved_depends_on_targets 0` + `files 392` + `typed 331` UNCHANGED (the
    refinement reclassifies the WARNING bucket, it does not move any node's rank/edges); `expected_unreachable_outside_dag`
    grows by the newly-carved L0/meta-reviews non-index pages. Add a regression assertion to the lint's
    self-test if one exists.

**c156 (batch-51 closer) — enact (c) (if any) + CONFIRM convergence.** Expected to be a confirm-only /
near-zero-dispatch cycle (the c154 classification expects ZERO genuine-untyped remainder, so (c) is likely
empty). If c154 D1 surfaced any genuine-untyped DAG node, c156 types it (one `edges:`+`rank:` block per node,
the standard P1 authoring — likely a tiny handful or zero). Then confirm: the `untyped` headline reflects only
genuine DAG-typing debt (≈0), the baseline HOLDS, the finite maintenance backlog is CONVERGED — only the
perpetual maintenance floor (the per-batch sweep + per-cycle tripwire) + the consumer-gated deferred fronts
(RE4 / sharding §2g / eigsolve-impl arm) remain. This closes the batch-51 convergence campaign and returns the
§CENTRAL ASK (10th time) to the human with the backlog now genuinely empty.

**Recommendation on the L0 disposition routing (the parent's explicit question):** **planner-resolvable
mechanical call, NOT a meta-phase methodology decision.** The graded-stack scheme already frames L0 as the
ground-truth evidence floor that carries no resolution rank; the carve-out is the scheme-aligned mechanism
already in use for `methodology/`/`design/`. I record the disposition here authoritatively; the c155 enactment
applies it as a bounded tooling refinement. (Should anything in c154 D1's classification contradict this — none
expected — that single contradiction routes to the meta-phase, but the on-disk evidence is unambiguous.)

## Open questions / caveats

- **The `untyped` summary-count semantics is the only subtle point** (flagged in §"L0 disposition read"):
  carving prefixes into `OUTSIDE_DAG_PREFIXES` fixes *reachability* classification but not the `untyped` count
  unless the count is also made to exclude outside-DAG pages. The c155 enactment must do BOTH coupled touches.
  This is recorded for the c155 dispatcher; it is a known, bounded lint-definition detail, not an open
  methodology question.
- **If c154 D1 surfaces a genuine-untyped DAG node** (NOT expected — the on-disk 26+26+5+4 = 61 is fully
  absorbed by the carve-out): that node is REAL edge-typing debt and routes to c156 as a normal P1
  `edges:`+`rank:` authoring (one block). I'll re-rank c156 accordingly when D1's classification lands. The
  expected case is (c) = empty.
- **No session restart needed** (the parent confirmed; batch-50 meta changed only the `finalization-debulk`
  skill + scaffolding — no agent-def / CLAUDE.md change). The c155 lint-refinement + scheme §5 note do not
  change any agent-def either, so no restart is forced mid-batch; the c155 dispatcher applies the tooling diff
  directly.
- **The §CENTRAL ASK is unchanged and remains the human's call.** This batch does NOT manufacture forward
  frontier work — it drives the *finite hygiene backlog* to convergence (the human's batch-51 directive),
  leaving the strategic direction (continue maintenance / re-open a consumer-gated front / (C) downstream-burn
  handoff / (D) re-scope) for the human at the batch-51 meta. The meta-phase's standing (C) recommendation is
  unaffected.
