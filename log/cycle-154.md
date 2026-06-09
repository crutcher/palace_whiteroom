# cycle-154 — OPENER 1/3 of meta-batch-51 — batch-51 CONVERGENCE OPENER; 3 small de-bulks + the load-bearing 61-untyped classification; baseline HELD EXACTLY

**Batch position:** OPENER 1/3 of meta-batch-51 (cycles 154/155/156). The batch-51 meta-phase
fires AFTER cycle-156's finalize, aggregating all three as a SEPARATE dispatch/commit; the cycle
counter does NOT reset. This finalize ran NO meta-phase housekeeping.

**Posture:** WIND TO MAINTENANCE — the maintenance-floor steady-state. With the batch-50 D/E/F
FINALIZATION-residue campaign COMPLETE and the book-wide A–F scan CLEAN, the floor reverts toward
near-empty: the once-per-batch full-hygiene sweep + the 3 tiny migrated backlog hygiene items.
This OPENER discharges all 3 backlog items AND surfaces the load-bearing classification that
shapes the batch-51 convergence.

## What landed

Two dispatches under the cycle-planner:

- **D1 (`cross-layer-cross-cutter`, `c154-hygiene-sweep-untyped-classification`) — AUDIT-CLASS, NO
  book mutation.** Ran the once-per-batch full-hygiene sweep with a **CLEAN BILL 8/8**, AND
  delivered the **load-bearing 61-untyped classification**:
  - **(a) 35 non-DAG carve-outs** — `meta-reviews/` + `methodology/` + navigational (`SUMMARY`/
    index-nav).
  - **(b) 26 `L0/` ground-truth leaves** — cited Palace/MFEM source-range chapters, the ground of
    the stack.
  - **(c) 0 genuine-untyped DAG nodes.**
  - 35 + 26 + 0 = **61**, matching the baseline `untyped` count exactly.
  - **`(c) = 0` is the result that shapes the convergence:** there is NO un-typed DAG node left to
    edge-type. So the batch-51 convergence (c155/c156) is a **PURE `tools/graded-stack-lint`
    carve-out refinement**, NOT a book-authoring/edge-typing campaign.
  - Audit-class → intentionally **NO staging row** (the c148 / c142 / c153-D1 precedent).

- **D2 (`layer-intro-author`, `c154-d2-three-small-debulks`) — 4 files / 5 ins / 47 del.** Three
  distinct-file hygiene de-bulks landed by direct edit (de-bulk convention):
  - **Fix 1 (`feature-l4-h1-convention-tail-normalize`):** `feature/capacitance.L4.md` +
    `feature/sparameters.L4.md` H1 lines gained `(output product)` — they were exactly the 2 of 6
    output-product columns lacking the gloss. All 6 output-product L4 H1s now uniformly carry it;
    driver-leaf / spine-ROOT / kernel-composition tails left as-is (TOC-navigability glosses per
    `heading-metadata-hygiene`).
  - **Fix 2 (`dependency-map-dateless-meta-review-n-refs-debulk`):** `concepts/dependency-map.md`
    lines 92–93 dropped the date-less `meta-review #N` process-attribution clauses; the static
    carry-through facts (already in `rotation.md` / `variant-absorption.md`) kept.
  - **Fix 3 (`constructed-operators-duplicate-concept-body-dedup`):** `concepts/
    constructed-operators.md` removed a pre-existing 42-line DUPLICATE concept body; the 2 unique
    links it carried (`apply_BA.md`, `L2/krylov_step.md`) lifted into the canonical
    §Use-in-GMRES-FGMRES block.

## Backlog items discharged

All 3 batch-51-head Backlog-Low hygiene items are DISCHARGED by D2 and REMOVED from
`scaffolding/priorities.md`:

- `feature-l4-h1-convention-tail-normalize`
- `dependency-map-dateless-meta-review-n-refs-debulk`
- `constructed-operators-duplicate-concept-body-dedup`

## Build + gates

- `cargo make book` (mdbook html + linkcheck2): **EXIT 0**, ZERO build-repairs. The de-dup removed
  4 duplicate headings — the critic verified zero inbound book/-internal `#`-anchor targets, so no
  broken internal link; the 2 unique links were lifted into the canonical block. Only pre-existing
  benign KaTeX potential-incomplete-link WARNs in untouched files.
- **Step-5c KaTeX `$`-sigil assertion: PASS** — `class="katex"` inside any `<pre>` = 0 across all
  392 built HTML pages.
- **Step-5d frontmatter-leak assertion: PASS** — no rendered page leaks its own frontmatter `key:`
  paragraph (grep over `book/book/html/` empty).
- **Step-5b graded-stack per-cycle tripwire (LANDED tree):** both block-conditions PASS —
  `rank_violations: 0`, NO newly-orphaned node, detritus escalate-guard NOT tripped. **ALL counts
  HELD EXACTLY vs baseline:** `files=392, typed=331, untyped=61, roots=45, rank_violations=0,
  unresolved_depends_on_targets=0, promotion_frontier=11, detritus=123, true_detritus=51,
  reference_reachable=72, expected_unreachable=54`. Trend: `rank_violations` …→0 (c152)→0 (c153)→0
  (c154); `unresolved` HELD 0 (c123…c154).

## Reconciliation

- **1 staging row == 1 dispatched-ready book-mutating report (D2)** — 131st consecutive clean
  staging. D1 is audit-class (NO book mutation) → correctly NO row.
- retroactive-budget global = 0; per-report gates all PASS/N/A; 0 implied-component stubs; SLICE
  CORPUS: 0; NO vocabulary firm-count flip; roadmap coverage UNCHANGED.
- The 1 consumed report's `integrated_at`/`integration_commit` touched; two-phase SHA-patch follows.
- NO `.claude/agents/` changes FROM THIS FINALIZE.

## The batch-51 convergence tee-up

The c154 D1 classification makes the convergence mechanical and book-content-free:

- **c155** — enact the lint carve-out **(a)+(b)**: extend the `tools/graded-stack-lint`
  `OUTSIDE_DAG` predicate to cover `L0/` + `meta-reviews/` + navigational AND make the `untyped`
  count EXCLUDE outside-DAG files; + a one-line `methodology/graded-stack-scheme.md` note. This
  mutates `tools/` + 1 methodology line, NOT `book/` DAG content — the
  `rank_violations`/`unresolved`/`detritus`/`true_detritus` baseline is UNAFFECTED; only the
  `untyped` REPORTING changes.
- **c156** — confirm convergence (`untyped` 61 → ~0), since **(c) genuine-untyped DAG = 0**.

The in-scope FEATURE-SURFACE SPINE remains L4-COMPLETE; the Synthesis VIEW is complete +
correspondence-audited; deferred fronts consumer-gated; no forced rectangular pull-up;
DIRECTIVE-1 MPI/distributed stays OUT.
