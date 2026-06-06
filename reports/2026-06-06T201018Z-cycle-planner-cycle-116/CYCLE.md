---
agent: cycle-planner
invoked_at: 2026-06-06T201018Z
scope: cycle-116 dispatch plan
status: pending
---

# Cycle 116 dispatch plan

## Goals selected this cycle

Cycle-116 is the SECOND primary cycle of meta-batch-37 (cycles 115/116/117; the batch-37 meta-phase fires AFTER c117's finalize) and the post-OUT-OF-BAND-meta-phase restart. The plan's CYCLE-116 active head defines TWO sequenced campaigns; cycle-116 executes **campaign 1 in full — the `semantic-consolidation-campaign` LEAD** (directive A, HIGH fan-out): the physical path-move of the active-management semantic surface out of `design/` + its ~187-occurrence cross-reference rewrite, then the 27-file restatement-cohort relocation sweep (Tier B + Tier C; Tier A landed c115 D3). Campaign 2 (`open-all-feature-fronts`, directive B) is sequenced WHOLLY to cycle-117: the directive places it "post consolidation," it is a wide multi-front fan-out that warrants a full cycle for shared-substrate exploration, and its substrate (the `design/` → new-home path) is exactly what cycle-116 is moving — opening it before the move lands would force the new feature chapters to be re-anchored. Two dispatches, two waves (the path-move and the cohort sweep OVERLAP on the cohort files' link lines, so they are sequential).

**Path-move decision (the directive's planner's-call): MOVE, do not SUMMARY-reorder-only.** Move `book/src/design/l4_calculus.md` → `book/src/semantics/index.md`, with the full link + prose-citation rewrite, `cargo make book` EXIT 0 + linkcheck2 clean as the hard gate. Rationale + link-risk reasoning in `## Path-move decision` below.

## Path-move decision (move vs SUMMARY-reorder-only) + link-risk reasoning

**Decision: physical MOVE to `book/src/semantics/index.md`.** The directive grants discretion ("OR keep the path and just leave the SUMMARY-reorder-only state if the move's link-risk is judged not worth it"). I judge the move worth it:

- **Substantive intent.** Directive A's intent is that the semantic surface have "its own home" out of `design/`. The SUMMARY-reorder (enacted off-band) already declares a top-level `# Semantic surface` Part (`SUMMARY.md:51-52`) — but the file's URL still resolves under `/design/`, and `book/src/design/index.md` still hosts it as a "Design Artifact" (verified: `design/index.md:9` lists it, noting "Physical path move out of `design/` is the cycle-116 LEAD"). Keeping the path leaves a structural/URL mismatch the directive explicitly wants closed. The off-band meta-phase did the link-safe half and DEFERRED the move to this LEAD precisely so it could run as a dedicated, gated dispatch.
- **Link-risk is bounded and uniformly-shaped.** The references (verified on disk) are TWO classes:
  - **53 live markdown links** `(../design/l4_calculus.md)`. Every content file is exactly ONE level under `book/src/` (L2, L3, L4, L2-L1, L3-L2, L4-L3, concepts, feature, methodology — all `book/src/<dir>/<file>.md`), so the relative path is uniformly `../design/l4_calculus.md` → uniformly `../semantics/index.md`. No path-depth variance to hand-resolve. (The lone `[`../design/l4_calculus.md`](../design/l4_calculus.md)` self-link form rewrites the same way.)
  - **~40 prose-text citations** `book/src/design/l4_calculus.md:NNN-MMM` (inline-code, NOT markdown links — they are absolute-from-repo-root path references, several with `:line` ranges + `§N.N` section refs). These do NOT break linkcheck (they are text), but MUST be rewritten for accuracy to `book/src/semantics/index.md:NNN-MMM`. The `:line` ranges are PRESERVED unchanged (the file content is moved verbatim, only the directory changes — line numbers are stable).
- **Hard gate catches any miss.** `linkcheck2` flags any unrewritten live link as a hard build error; `cargo make book` EXIT 0 is the dispatch's required gate. The risk of a silent break is near-zero for the link class. The prose-citation class is non-breaking even if one is missed (it would be a stale-but-resolvable text path, caught by a follow-up grep).
- **Total edit surface: 97 files** (the `grep -rl 'design/l4_calculus' book/src` count) + the `git mv` + `design/index.md` reframe (drop the hosting bullet) + `SUMMARY.md` link target (`design/l4_calculus.md` → `semantics/index.md`). Mechanical and find/replace-shaped; well within a single dedicated `layer-intro-author` dispatch.

**New home: `book/src/semantics/index.md`.** Chosen over `semantic-surface/index.md` for brevity; it is a fresh directory (no collision — `book/src/semantics/` does not exist). The surface keeps its full content verbatim (header, §0/§0.1 active-management discipline, §1.2.1/§1.2.2 named-shape-groups, §3.x, §4.1) — only the directory changes.

## Deliverable-presence verification (paste-inline evidence)

Linter baseline confirmed on disk (matches resume-notes + c115 finalize record):
`python3 tools/graded-stack-lint/graded_stack_lint.py` →
`files scanned: 356 | untyped (WARNING): 61 | feature roots: 36 | reachable from roots: 133 | DETRITUS (126) | STRONGER GARBAGE SIGNAL (23) | RESULT: 0 rank violation(s), 126 detritus, 61 untyped`.
(Matches `files=356, reachable=133, rank_violations=0, untyped=61, unresolved=0, promotion_frontier=8, detritus=126, roots=36, STRONGER=23`. The only delta vs c115 is the new `methodology/semantic-consolidation.md` expository page, benign/outside-DAG.)

**D1 (path-move) — open by construction (a fresh mechanical move; no prior cycle attempted it).** Confirming the move target + reference surface:
- `ls book/src/design/l4_calculus.md` → EXISTS (source). `ls book/src/semantics` → does not exist (clean destination, no collision).
- `grep -rl 'design/l4_calculus' book/src | wc -l` → **97** files reference it.
- Link-form breakdown (pasted above in §Path-move decision): 53 live `(../design/l4_calculus.md)` links (uniform one-level depth) + ~40 prose `book/src/design/l4_calculus.md[:NNN]` citations.
- `book/src/SUMMARY.md:51-52` carries the `# Semantic surface — calculus, rules & abstractions` Part → `./design/l4_calculus.md` (the link target to rewrite). `book/src/design/index.md:9` still hosts the bullet (to drop). `cargo make book` EXIT 0 was confirmed by the off-band meta-phase post-reorder.

**D2 (Tier B + Tier C cohort sweep) — OPEN (Tier A trimmed c115 D3; Tier B/C still carry the markers):**
- Tier A trimmed-check: `grep -c 'carries the same-shape contract' book/src/{L4,L3,L2}/linear_combination.md` → **0, 0, 0** (Tier A done c115 D3, integrated `0666e5a`; NOT re-proposed).
- Tier B residual markers present: `grep -l 'NOT rank-1\|not rank-1' …` → returns all 5 Tier-B files (`L3/blas1-intro.md`, `L2-L1/linear-combination-fold-specialization.md`, `L3/nrm2.md`, `concepts/elementwise-product.md`, `L2/nrm2.md`) — OPEN.
- Cohort residual total: `grep -rl 'NOT rank-1\|not rank-1\|carries the same-shape contract\|accidentally read as' book/src/{L2,L3,L4,concepts,L2-L1}` → **24** files (= 27 cohort − 3 Tier-A-done = Tier B 5 + Tier C 19). Matches the c115 D3 FINDING inventory exactly.
- All Tier B + Tier C named files verified EXISTS on disk (`L2/{axpy,dot,inner_product}.md`, `L3/dot.md`, `L4/{dot,sparameter_reduce}.md`, etc. all present).
- OQ `named-shape-groups-general-rule-restatement-cohort-extent` — promoted (not closed) c115 D3, now governed by the semantic-consolidation directive; this dispatch discharges it. (Not on the STOP-PROPOSING negative list; the negative list is the L3-cohort-growth slugs — none of these are it.)

**No structural block:** the semantic surface (c) is verified-complete on disk (`design/l4_calculus.md:24` §0.1 active-management discipline present; `:73` §1.2.1; `:303` §4.1) — so the cohort trim has its relocation target. Nothing is gated.

## Dispatches

**D1 (`layer-intro-author`, WAVE-1) — semantic-surface PHYSICAL PATH MOVE + the ~187-occurrence cross-reference rewrite.**
- **scope:** `git mv book/src/design/l4_calculus.md book/src/semantics/index.md` (move verbatim — content unchanged, only the directory). Then rewrite ALL 97 referencing files:
  - (a) the **53 live markdown links** `(../design/l4_calculus.md)` → `(../semantics/index.md)` (uniform — every content file is one level deep). Includes the Tier-B inline `[`l4_calculus`](../design/l4_calculus.md)` link forms.
  - (b) the **~40 prose-text citations** `book/src/design/l4_calculus.md` → `book/src/semantics/index.md` (preserve any `:NNN-MMM` line ranges + `§N.N` section refs UNCHANGED — content moved verbatim, line numbers stable).
  - (c) `book/src/SUMMARY.md:52` link target `./design/l4_calculus.md` → `./semantics/index.md`.
  - (d) `book/src/design/index.md` — DROP the hosting bullet (`:9`) for the surface (it now lives at `semantics/index.md`, not a design artifact); leave a one-line "moved to the `# Semantic surface` Part" pointer note if useful. `design/index.md` itself stays in the `# Design Artifacts` SUMMARY Part.
  - **GATE (mandatory):** `cargo make book` EXIT 0 + linkcheck2 clean. Any residual `design/l4_calculus` reference (re-grep `grep -rl 'design/l4_calculus' book/src` → must be 0) is a miss to fix before reporting.
- **deps:** none (wave-1 opener).
- **rationale:** campaign-1(a), the LEAD's mechanical core; HIGH fan-out (the surface is the home all L4/L3/L2 content cites for semantics). Directive A's "its own home out of `design/`." Plan-tag `semantic-consolidation-campaign`.

**D2 (`layer-intro-author`, WAVE-2, dep: D1) — the 24-file restatement-cohort relocation sweep (Tier B + Tier C).**
- **scope:** apply the c115-D3 Tier-A pattern (`reports/2026-06-06T185234Z-layer-intro-author-named-shape-groups-relocation/CYCLE.md` is the canonical precedent) to the remaining 24 cohort files. For EACH: trim the GENERAL named-shape-groups teaching (the "NOT rank-1" / "carries the same-shape contract" general-rule echo, any binding/use restatement, any `Tensor[N]` anti-pattern teaching or "earlier rendering" migration note) out of the shape-precondition prose, leaving (i) the op's OWN concise shape fact ("congruent over one group `S` of arbitrary/unknown rank; element-local at every position of `S`; result shares `S`") and (ii) a §1.2.1 (or §1.2.2 for operator-shape domain≠range entries) back-link to the surface at its NEW path `../semantics/index.md`.
  - **Tier B (5 files, mid-weight — already LINK §1.2.1, drop the residual general echo):** `book/src/L2/nrm2.md:77`, `book/src/L3/nrm2.md:59`, `book/src/L2-L1/linear-combination-fold-specialization.md:35`, `book/src/L3/blas1-intro.md:20`, `book/src/concepts/elementwise-product.md:9,18`.
  - **Tier C (19 files, light — the bare "(arbitrary, unknown rank — NOT rank-1)" parenthetical):** `book/src/L2/{axpy,axpby,axpbypcz,scal,dot,normalize,reciprocal,elementwise_product,inner_product,gram}.md`; `book/src/L3/{dot,inner_product,normalize,reciprocal,elementwise_product}.md`; `book/src/L4/{dot,inner_product,nrm2,sparameter_reduce}.md`. (Line anchors per the c115 D3 FINDING §Cohort-wide extent — on-disk-confirm each before editing; codemap/grep line hints may drift ±1.)
  - **DIRECTIVE NOTE (resolves the c115 D3 open Tier-C judgment):** c115 D3's read was "Tier C is below the bar (keep)." The semantic-consolidation directive (a semantic rule lives ONCE at the surface; a restatement at a functional-unit scope is a smell) SUPERSEDES that read — the "NOT rank-1" parenthetical IS a general-rule echo and is RELOCATED (trimmed to the surface, replaced by the op's own "admits any rank" + back-link). Sweep Tier C, do not skip it. The directive is explicit: "the 27-file restatement-cohort relocation sweep … Tier B ~5 files + Tier C ~19 files."
  - (c) **confirm** (verify, no edit) the surface's §0.1 active-management discipline + §1.2.1/§1.2.2/§4.1 general rule is present + complete at the NEW path (it is — D1 moved it verbatim); each trimmed entry's back-link resolves to `../semantics/index.md`.
  - **GATE:** `cargo make book` EXIT 0 + linkcheck2 clean; re-grep `grep -rl 'NOT rank-1\|not rank-1\|carries the same-shape contract' book/src` → should drop to ~0 (any remaining must be a genuine per-op shape fact, not a general echo — note it if so).
- **deps:** D1 (the back-links D2 writes/keeps must point to the NEW `../semantics/index.md` path — D2 runs against the moved file).
- **rationale:** campaign-1(b)+(c), the cohort consolidation; HIGH fan-out (governs how the whole BLAS-1 / fold / reduce cohort states shape semantics). Discharges OQ `named-shape-groups-general-rule-restatement-cohort-extent`. Plan-tag `semantic-consolidation-campaign`.

## Overlap analysis

**D1 ↔ D2: OVERLAPPING → sequential (D2 after D1).** Two reasons:
1. **Same-file edits.** The 24 cohort files D2 trims are a SUBSET of the 97 files D1 rewrites (every cohort file carries a `../design/l4_calculus.md` link line that D1 rewrites). In the Tier-B files the SAME REGION is touched by both: the shape-precondition bullet D2 trims CONTAINS the `[`l4_calculus`](../design/l4_calculus.md)` link D1 rewrites. Same file + (for Tier B) same region = genuine overlap, not distinct-row appends.
2. **Path dependency.** D2's back-links must resolve to the NEW path `../semantics/index.md`. If D2 ran first (or parallel), it would write/keep links to the OLD `../design/l4_calculus.md` path, which D1 then has to re-sweep — a redundant double-edit and a window where D2's links are stale. Running D2 against the moved file is correct-by-construction.

No other overlaps (only two dispatches). No consolidated-tally / shared-index collision: neither dispatch touches a `feature/index.md` matrix or a layer-index running count (the cohort trim is per-entry prose; the move is mechanical link-rewrite). No new-slug forward-reference between dispatches (D2 references the surface's NEW slug `semantics/index.md`, which D1 creates this cycle — **canonical-slug coordination: BOTH dispatch scopes name `book/src/semantics/index.md` explicitly** so D2 does not guess; D1 authors it, D2 links to it).

## Sequencing schedule

- **Wave 1 (1 dispatch):** D1 — the physical path move + 97-file cross-reference rewrite. Hard gate: `cargo make book` EXIT 0, linkcheck2 clean, `grep -rl 'design/l4_calculus' book/src` → 0.
- **Wave 2 (1 dispatch, after D1's report lands so the per-report integrator wires the moved file + D2 links to the new path):** D2 — the Tier B + Tier C cohort relocation sweep against the moved surface.

Then the standard tail: 2 critics (parallel) → repairers as needed → `integrator-per-report` ×2 (serial) → ONE `integrator-finalize` (rebuild + commit + push + housekeeping; re-runs the linters at step-5b — baseline expected HELD: the move + trim are reachability/rank-neutral, frontmatter-untouched).

## Open questions / caveats

- **All-fronts wave (campaign 2) is sequenced WHOLLY to cycle-117.** Confirmed not begun this cycle: the directive places it "post consolidation," it is a wide 5+-front fan-out (waveguide-mode / boundary-mode / fe_space siblings / mesh-wrapper single-machine / any other in-scope deferral) warranting a full cycle for shared-substrate lifting, and several of those new chapters will link the semantic surface — authoring them before the path move lands would force a re-anchor. The cycle-117 planner opens it as the wide wave (route: `layer-intro-author` for feature columns + fe_space siblings; `harvester` for mesh-wrapper ops). The mesh-wrapper front is single-machine ONLY (`Par*`/distributed OUT per §Scope; MFEM-opaque mesh-refinement leaves stay obstruction-documented, NOT forced). Substrate-not-on-disk fronts land as `roadmap_goal` rank-0 chapters, not forced firm claims.
- **Linter baseline is expected to HELD after this cycle** (`reachable=133, rank_violations=0, detritus=126`). Both dispatches are prose/link edits + a file move — they do NOT touch frontmatter `edges:`/`rank:`, and the linters read frontmatter + relative-path resolution, not SUMMARY ordering or prose-citation text. The `files` count holds (a move is not a new file; `untyped` holds — `semantics/index.md` is the same outside-DAG expository page as `design/l4_calculus.md` was). The finalize step-5b re-measure is authoritative; if the move accidentally drops the surface from the linter's outside-DAG expected-unreachable set (path-pattern match on `design/`), that is a benign linter-path-pattern note for the scheduled batch-37 meta (the linter's `expected-unreachable` matcher keys on `methodology/design/index/group-intro` page paths — the new `semantics/` path may not match, flipping the surface from "expected-unreachable" to a benign `[garbage?]`/untyped entry; NOT an artifact defect, but worth a one-line meta note + a possible one-line linter-matcher extension). **Flagged for the c117 planner + batch-37 meta-phase.**
- **Tier-C bar resolved by directive, recorded.** The c115 D3 dispatch left the Tier-C relocation as an open judgment ("my read: keep"). I have RESOLVED it toward RELOCATE per the semantic-consolidation directive (a restatement at functional-unit scope is a smell). D2's scope states this explicitly so the producer does not re-litigate. If the producer finds a specific Tier-C parenthetical that is genuinely an irreducible per-op shape fact (not a general echo), it should KEEP it and note the exception — faithful-trim-or-finding, not blind deletion.
- **Two carried graded-stack linter-maintenance OQs** (`graded-stack-prose-status-inference-masks-untyped` + `plateau-probe-linter-roots-36-vs-columns-40`) remain ask-class `tools/`-code changes for the scheduled batch-37 meta (after c117), NOT enacted this cycle. The new `semantics/`-path-vs-`expected-unreachable`-matcher note above joins them.
