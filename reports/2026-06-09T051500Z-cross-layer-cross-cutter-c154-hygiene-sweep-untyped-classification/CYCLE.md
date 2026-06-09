---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-09T050101Z
scope: cycle-154 D1 — batch-51 OPENER full-hygiene sweep + authoritative classification of the 61 untyped nodes
status: pending
---

# CYCLE: Cross-layer observation — batch-51 OPENER hygiene sweep + 61-untyped authoritative classification

## Summary

This is the batch-51 OPENER once-per-batch full-hygiene maintenance sweep (audit-class, NO `book/`
mutation) PLUS the authoritative partition of the 61 untyped nodes into the three disposition buckets the
c155/c156 convergence enactment consumes. **Verdict: CLEAN BILL — all hygiene items pass; the graded-stack
baseline HELD EXACTLY (`files=392, typed=331, untyped=61, roots=45, rank_violations=0,
unresolved_depends_on_targets=0, promotion_frontier=11, detritus=123, true_detritus=51,
reference_reachable=247, expected_unreachable_outside_dag=54`).** The A–F residue-class scan is clean except
the 2 KEEP governing-directive files + the 2 KNOWN-and-being-fixed-this-cycle D2 targets. The 61-untyped
partition is **(a) 35 non-DAG carve-outs + (b) 26 `L0/` ground-truth leaf layer + (c) ZERO genuine-untyped
DAG remainder** — arithmetic 35+26+0 = 61 exact. **(c) is EMPTY: batch-51 convergence is purely a
carve-out refinement (a bounded `tools/` lint-definition touch + a one-line scheme §5 note), NOT a 61-file
authoring campaign.**

## Observation kind

**Audit residue / consistency** — this is the standing maintenance-floor cross-layer sweep, not a single
coverage-gap finding. The cross-cutting observation is the authoritative classification: the `untyped=61`
WARNING is dominated by legitimately-untyped-BY-DESIGN pages (the ground-truth leaf layer + the non-DAG
process/methodology/navigational pages), with ZERO genuine edge-typing debt remaining.

## Specific finding

### Part 1 — standing per-batch hygiene checklist (8 items, all PASS)

1. **Graded-stack two-invariant tripwire** — `python3 tools/graded-stack-lint/graded_stack_lint.py
   --book-src book/src`: totals HELD exactly vs baseline. `RANK VIOLATIONS: none.`
   `unresolved_depends_on_targets: 0`. No new orphan (detritus 123 / true-detritus 51 / reference-reachable
   72 all HELD). Escalate-guard not tripped (warn-not-fail; `untyped` is a WARNING, not a failure).
   Full totals JSON HELD: `{files:392, typed:331, untyped:61, roots:45, rank_violations:0,
   unresolved_depends_on_targets:0, promotion_frontier:11, reachable:163, reference_reachable:247,
   detritus:123, true_detritus:51, expected_unreachable_outside_dag:54}`.

2. **RE-set premise re-check** — RE4 / sharding §2g member / RE11 reference-only-reachable cohort all
   consumer-gated and HELD. The reference-reachable detritus cohort (RE11) = 72 (baseline 72); true-detritus
   = 51 (baseline 51). eigsolve-impl gate NON-FIRING (`L3/eigsolve-impl` stays `roadmap_goal (kernel-impl)`;
   no blocking RE3-deflate / RE8-krylov-iteration consumer has wired in). No RE premise changed.

3. **Semantic-surface liveness** — `semantics/index.md` §0.1 (`## 0.1 Active-management discipline`,
   line 24) + the SEMANTIC-CONSOLIDATION governing header (line 3, "a semantic rule/def/abstraction lives
   ONCE, here…") both present and intact. No semantic rule lost or relocated.

4. **Kernel-API/impl integrity** — the 3 `realizes-kernel-api` edges all stay `reference`-class (free,
   navigational, NOT `depends-on`), confirmed in frontmatter `kind:` declarations + prose consistently:
   - `L1/libceed-quadrature-kernel-impl.md:14` → `L1-L0/fe-assemble-libceed-boundary-obstruction` (kernel-api)
   - `L1/multigrid-relaxation-smoother.md:26` → `L1-L0/triangular-solve-obstruction` (kernel-api)
   - `L3/eigsolve-impl.md:21` → `L3/eigsolve` (kernel-api) + `:23` → `L4/eigsolve` (L4 cap, navigational)
   `unresolved_depends_on_targets: 0` + `rank_violations: 0` confirm none is mis-typed as a blocking edge.

5. **DIRECTIVE-1 MPI boundary** — intact. The sharding node `L4/sharding-decompose-reduce.md` is
   `rank: roadmap_goal` / `status: roadmap_goal` with only `reference:`-class edges (verified frontmatter
   lines 4–7). No firm node `depends-on` it (else `rank_violations > 0`); no MPI/distributed primitive
   lifted into active scope. `Par*`/MPI mentions elsewhere are single-rank readings or roadmap_goal
   intent, not firm distributed dependencies. **FINALIZATION static-state liveness** — producers not
   re-accreting process accounting (the A–F scan below confirms book-wide cleanliness).

6. **A–F residue-class scan** — see the dedicated table below. A=B=C=D=F=0; E = 2 KEEP + 1 KNOWN D2 target.

7. **Promotion frontier** — 11 (baseline 11). HELD.

8. **`## Context`-is-NOT-an-F-target distinction** — confirmed honored: 133 `## Context` orientation
   sections exist book-wide (outside meta-reviews/methodology) and are correctly NOT flagged as process
   residue (meta-50 codified definition: orientation, not process accounting).

### Part 1 — A–F residue-class scan result (the comprehensive completeness gate)

Book-wide greps (per `finalization-debulk` skill §"A–F residue-class scan", meta-50-codified definitions):

| Class | Grep | Result | Disposition |
|---|---|---|---|
| **A** | `^## Verified-against` | **0** | clean |
| **B** | `^verified_against:` | **0** | clean |
| **C** | `reports/[0-9]` (excl meta-reviews) | **0** | clean |
| **D** | `cycle-[0-9]+\|\bc[0-9]{2,3}\b\|batch-[0-9]+\|wave-[0-9]` (excl meta-reviews + methodology/) | **0** | clean |
| **E** | `2026-0[0-9]-[0-9]{2}\|meta-review #[0-9]` (excl meta-reviews + methodology/) | **3 files** | see below |
| **F** | `^## (Origin\|Working Notes\|Critic'?s role)` (excl meta-reviews + methodology/) | **0** | clean |

**E-class breakdown (3 files, all accounted-for — NO new findings):**
- `concepts/dependency-map.md:92-93` — the date-LESS `meta-review #1/#2/#3` E-sub-class. **KNOWN +
  being-fixed THIS CYCLE by D2** (`dependency-map-dateless-meta-review-n-refs-debulk`). Not a new finding.
- `semantics/index.md:3` — the SEMANTIC-CONSOLIDATION governing-directive header (date is part of the
  directive attribution in a governing header). **KEEP by design** (1 of the 2 expected KEEP files).
- `SUMMARY.md:394+` — TOC entries for the `meta-reviews/` chapters (dates are the chapter TITLES — the
  navigational index to the carved-out process-record layer). **KEEP by design** (2nd expected KEEP file).

**Book-wide sub-class confirmation (the sweep's distinctive duty — show no OTHER instances exist):**
- Date-LESS `meta-review #N` sub-class: appears in **ONLY** `concepts/dependency-map.md` book-wide — no
  other instance. The D2 (ii) de-bulk fully clears this sub-class.
- Duplicate `## Concept:` self-restating block: appears in **ONLY** `concepts/constructed-operators.md`
  (line 175) book-wide — no other instance. The D2 (iii) de-dup fully clears this sub-class.

**A–F verdict: CLEAN** (the 3 E-matches are the 2 expected KEEP files + the 1 KNOWN D2 target; D2 closes
the only date-less `meta-review #N` instance + the only duplicate-concept-body instance book-wide).

### Part 2 — authoritative classification of the 61 untyped nodes

Source: `graded_stack_lint.py --book-src book/src --json` → `untyped` list (61 nodes). Arithmetic verified
**(a) 35 + (b) 26 + (c) 0 = 61** exact, zero uncategorized remainder.

**(a) non-DAG carve-outs — 35 nodes** (legitimately-untyped-BY-DESIGN; belong OUTSIDE the `untyped`
WARNING, analogous to the existing `OUTSIDE_DAG_PREFIXES` for `methodology/`+`design/`). All 35 verified:
zero have `## Status` / `rank:` / `firmness:` / `edges:` frontmatter; none is a layered-DAG
record/operator/theme node.

  - **26 `meta-reviews/`** (process records):
    `meta-reviews/2026-05-24`, `meta-reviews/2026-05-24-cycles-10-12`, `meta-reviews/2026-05-24-cycles-13-15`,
    `meta-reviews/2026-05-24-cycles-16-18`, `meta-reviews/2026-05-24-cycles-19-21`,
    `meta-reviews/2026-05-24-cycles-22-24`, `meta-reviews/2026-05-24-cycles-25-30`,
    `meta-reviews/2026-05-24-cycles-4-6`, `meta-reviews/2026-05-24-cycles-7-9`,
    `meta-reviews/2026-05-25-cycles-31-36`, `meta-reviews/2026-05-25-cycles-37-43`,
    `meta-reviews/2026-05-25-cycles-44-49`, `meta-reviews/2026-05-25-cycles-50-55`,
    `meta-reviews/2026-05-25-cycles-56-61`, `meta-reviews/2026-05-25-cycles-62-67`,
    `meta-reviews/2026-05-25-cycles-68-73`, `meta-reviews/2026-05-25-cycles-74-79`,
    `meta-reviews/2026-05-25-cycles-80-85`, `meta-reviews/2026-05-26-cycles-104-115`,
    `meta-reviews/2026-05-26-cycles-116-127`, `meta-reviews/2026-05-26-cycles-128-139`,
    `meta-reviews/2026-05-26-cycles-140-151`, `meta-reviews/2026-05-26-cycles-152-166`,
    `meta-reviews/2026-05-26-cycles-86-91`, `meta-reviews/2026-05-26-cycles-92-103`,
    `meta-reviews/index`.
  - **5 `methodology/`** (reader-facing methodology MIRROR; already in `OUTSIDE_DAG_PREFIXES` for
    *reachability* but still flagged `untyped` because they carry no `rank:`/`edges:`):
    `methodology/goal-flow`, `methodology/graded-stack-scheme`, `methodology/overview`,
    `methodology/resolution-ladder`, `methodology/semantic-consolidation`.
    *(Note: `methodology/graded-stack-scheme.md` contains `rank:`/`edges:` tokens at lines 74/93/124/148 —
    these are inside fenced code-block EXAMPLES documenting the scheme, NOT page frontmatter; the page
    itself carries no frontmatter rank. Confirmed untyped-by-design.)*
  - **4 navigational / structural pages**: `SUMMARY`, `introduction`, `design/index`, `semantics/index`.

**(b) the 26 `L0/` ground-truth leaf layer — 26 nodes** (CARVE OUT, uniform with the `meta-reviews/`
carve-out; L0 IS the ground-truth evidence floor — rank is over constructive resolution, vacuous for the
bottom layer). All 26 verified: zero have a `## Status` heading; zero have `rank:`/`firmness:`/`edges:`
frontmatter; zero carry `depends-on` (the resolution `cites-evidence` edge lives on the L1 consumer side).
All 26 are file-overview reference notes / class-overview / convention-or-pattern intro pages (H1 forms
verified: `# File — …`, `# Class — …`, `# Convention — …`, `# Overload set — …`, `# Conventions`,
`# File overviews`, `# Overload sets & class interfaces`, `# L0 — Cited Palace source ranges…`).
**No L0 file is a record/operator node needing a rank** (as expected — zero flagged).

    `L0/apply-linop-overload-set`, `L0/conventions-intro`, `L0/eigensolver-wrapper`,
    `L0/fem-bilinearform-file`, `L0/fem-libceed-operator-file`, `L0/fespace-file`,
    `L0/file-overviews-intro`, `L0/index`, `L0/ksp-factory-file`, `L0/kspsolver-base-class`,
    `L0/linalg-free-functions`, `L0/linalg-iterative-file`, `L0/linalg-operator-file`,
    `L0/linalg-orthog-file`, `L0/linalg-rap-file`, `L0/linalg-solver-file`, `L0/linalg-vector-file`,
    `L0/mfem-vector-types`, `L0/mfem-wrapper-solver`, `L0/mpi-globalsum-and-collectives`,
    `L0/mutable-workspace-pattern`, `L0/output-arg-vs-receiver`, `L0/overload-sets-and-classes-intro`,
    `L0/par-types-single-rank-reading`, `L0/preconditioner-classes-overview`,
    `L0/transparent-vs-load-bearing-tricks`.

**(c) genuine-untyped DAG-node remainder — ZERO nodes.** No node among the 61 is NEITHER (a) NOR (b). The
on-disk breakdown is exactly 26 `L0/` + 26 `meta-reviews/` + 5 `methodology/` + 4 navigational = 61, fully
absorbed by (a)+(b). **There is NO real record/operator/theme node missing rank+edges that SHOULD be
typed.** Convergence is purely a carve-out refinement — there is no c156 edge-typing/rank authoring target.

## Recommendation

- **Hygiene sweep: CLEAN BILL — no follow-up dispatch needed.** All 8 checklist items pass; baseline HELD
  exactly; A–F scan clean (modulo the 2 KEEP + 1 KNOWN-D2-target). The 2 D2 de-bulks (date-less
  `meta-review #N` + duplicate-concept-body) are the only book-wide instances of their sub-classes and are
  being fixed this cycle.
- **61-untyped classification: convergence is a bounded carve-out refinement, (c) is EMPTY.** Confirm the
  c155 enactment as a `tools/graded-stack-lint` definition refinement + a one-line `methodology/
  graded-stack-scheme.md` §5 note — NOT a book-authoring campaign. Specifically (per the planner's two
  coupled lint touches): (1) extend `OUTSIDE_DAG_PREFIXES` → `("methodology/", "design/", "L0/",
  "meta-reviews/")` + add `OUTSIDE_DAG_EXACT = {"SUMMARY", "introduction"}`; (2) make the `untyped` summary
  count EXCLUDE `is_likely_outside_dag` pages. Expected post-refinement: `untyped` drops 61 → ~0;
  `rank_violations 0` + `unresolved_depends_on_targets 0` + `files 392` + `typed 331` UNCHANGED.
- **c156: confirm-only / near-zero-dispatch.** Since (c) = ZERO, there is no genuine-untyped node to type;
  c156 confirms `untyped`-headline-≈0 + baseline-HOLD + the finite maintenance backlog CONVERGED.
- **Defer** the strategic §CENTRAL ASK to the human at the batch-51 meta (unchanged by this cycle).

## Supporting evidence

- Lint totals: `tools/graded-stack-lint/graded_stack_lint.py --book-src book/src` + `--json` (`/tmp/lint.json`
  this cycle) — totals block reproduced in Part 1 item 1.
- Untyped list: `--json` `untyped` key (61 nodes), partitioned by prefix; arithmetic 35+26+0=61 verified.
- L0 leaf-layer evidence: `grep -lE '^## Status' L0/*.md` → none; `grep -lE '^(rank|firmness|edges):'
  L0/*.md` → none; `grep -lE 'depends-on' L0/*.md` → none; per-file H1 forms all file/class/convention
  overview notes.
- Carve-out (a) evidence: `grep -lE '^## Status|^(rank|firmness|edges):' meta-reviews/*.md methodology/*.md
  SUMMARY.md introduction.md design/index.md semantics/index.md` → only `methodology/graded-stack-scheme.md`
  (resolved: code-block examples at lines 74/93/124/148, not page frontmatter).
- A–F greps reproduced verbatim in the Part-1 A–F table; sub-class book-wide confirmation greps:
  date-less `meta-review #N` → only `concepts/dependency-map.md`; `## Concept: constructed operators` → only
  `concepts/constructed-operators.md:175`.
- Kernel-API edges: `grep -rn 'realizes-kernel-api' book/src` — 3 impl→api edges, all `kind:
  realizes-kernel-api` reference-class in frontmatter (`L1/libceed-quadrature-kernel-impl.md:14`,
  `L1/multigrid-relaxation-smoother.md:26`, `L3/eigsolve-impl.md:21,23`).
- DIRECTIVE-1 gate: `L4/sharding-decompose-reduce.md:4-7` (`rank: roadmap_goal`, `reference:`-class edges).
- Semantic surface: `semantics/index.md:3` (SEMANTIC-CONSOLIDATION header) + `:24` (`## 0.1`).

## Open questions / caveats

- **The `untyped` summary-count semantics is the one subtle coupling for c155** (planner-flagged, re-confirmed
  here): adding prefixes to `OUTSIDE_DAG_PREFIXES` fixes *reachability* classification but does NOT by itself
  drop a page from the `untyped` WARNING count — `node.untyped = (rank is None AND no typed edges)` is a
  separate axis from `is_likely_outside_dag`. The c155 enactment must do BOTH coupled touches (extend the
  prefix set AND make the count exclude outside-DAG pages). This is a known, bounded `tools/` definition
  detail, not an open methodology question; it leaves all HARD invariants untouched (`rank_violations`,
  `unresolved_depends_on_targets` are over `depends-on` edges, of which outside-DAG pages have none).
- **No `book/` mutation performed** (audit-class dispatch, per the DISPATCH-phase write-authority partition).
  The CYCLE.md write succeeded (no filter block on the canonical `CYCLE.md` filename).
- **(c) = EMPTY is the load-bearing finding for the planner's convergence sketch**: it confirms batch-51
  convergence requires NO book-authoring — only the bounded lint refinement + the scheme §5 note. If any
  future content lands a genuine record/operator/theme node lacking rank+edges, it would re-populate (c);
  the on-disk evidence this cycle says zero.
