---
agent: cycle-planner
invoked_at: 2026-06-04T22:29:17Z
scope: cycle-096 dispatch plan
status: pending
---

# Cycle 096 dispatch plan

THIRD/FINAL primary cycle of meta-batch-30 (cycles 094/095/096; the batch-30 meta-phase fires
AFTER this cycle-096 finalize as a SEPARATE dispatch aggregating 094/095/096). The c095 cascade
(`bilinear-form`→`gram_reduce`→4-columns) + the P1 frontier-first edge-typing LANDED CLEAN:
the feature spine is now 11-firm / 1-seed (only `boundary-mode`), and the rank-violation count
dropped 22→1 (the lone residual is O1, a deferred-typing artifact). The graded-stack campaign's
mechanical-completion criterion is MET for the typed subset.

## Goals selected this cycle

Close batch-30 with the **P2 FIRST TRANCHE** — the high-fan-out *genuine-gap-author + carry-forward-close*
slice of corpus finalization, NOT the large slice-deletion campaign. Concretely: (1) author the
**ONE genuine gap** `L4/preconditioning-framework.md` firm-on-first-authoring (the only un-authored
home the 2026-06-04 slice audit found; unblocks 2 concept-page canonical-example refs); (2) close the
three c095 carry-forwards — O1 lazy-tail typing (rank_violations 1→0), the `read_status_line` linter
parse-bug fix, the `matrix-weighted-norm-mutation-rotation.md:317` within-theme stale residue; and
(3) repair the c094 `resolution-ladder.md` worked example that the c095 cascade FALSIFIED. The
**slice deletions + heavy citation-repoint are EXPLICITLY DEFERRED** to a batch-31 LEAD item — that
sub-phase repoints a deeply-interwoven ~30-anchor krylov-step / ~10-concept-page slice-citation web
and is too large to land clean in a batch-closing cycle (scoping decision justified below).

## Scoping decision: why P2 is a FIRST TRANCHE, not all-of-P2

The task framing asked whether c096 can do ALL of P2 or a well-scoped first tranche. **First tranche.**
Evidence (gathered this cycle):

- The 9-slice deletion is gated on repointing a **deeply-interwoven slice-citation web**. The firm
  `L2`/`L3`/`L4` `krylov-step` trio alone carries ~30 slice line-anchors (`cg.md` ranges,
  `gmres.md:459-471`/`:430-454`, `arnoldi_step.md:99-105`/`:194-213`/`:285-298`,
  `polynomial_recurrence_step.md:119-160`). Add ~6 `L4-L3/` krylov dissolution themes
  (`krylov-step-typed-wrapper-dissolution`, `iterate-while-dissolution`, `gmres-inner-loop-…`, …) and
  ~10 concept pages (`negative-result-slice`, `sequential-obstruction`, `plane-rotation-stream`, the
  givens family; plus the ~10 concept pages citing `cg_preconditioning_framework`).
- The deletions also require absorbing worked-example content into concept/theme homes (citing L0
  directly), migrating ~6 pending-lift OQs (incl. the cg `initial_res=(b·b)^{1/4}` likely-Palace-bug
  recorded nowhere but the slice), minting `roadmap_goal` chapters for not-yet-describable homes
  (e.g. `orthogonalize-mutation-rotation` L1>L0), and reconciling the `plane_rotation_stream`
  off-by-one. That is a multi-dispatch citation-absorption *campaign*, not a batch-closing cycle.
- The ONE author-gap that BLOCKS the deletion campaign (`L4/preconditioning-framework.md`) is
  independent and high-fan-out — landing it this cycle is the right first move (it lets the
  `cg_preconditioning_framework` slice's framework material become fully absorbed, making that slice
  deletable in the deferred tranche).

The deferred tranche is recorded in `priorities.md` as a batch-31 LEAD candidate. The completion
criterion (reachability GC shows `spec/slices/*` unreachable) is unchanged.

## Deliverable-presence verification (paste-inline evidence)

Per the MANDATORY pre-dispatch four-step check (CLAUDE.md / cycle-planner.md). All commands run this
cycle; literal output pasted.

**D1 — `book/src/L4/preconditioning-framework.md` (genuine gap, firm-on-first-authoring):** OPEN by
construction (no prior-cycle history — first authoring). Confirmed:
```
$ ls book/src/L4/preconditioning-framework.md
ls: cannot access 'book/src/L4/preconditioning-framework.md': No such file or directory
$ grep -c 'l4-preconditioning-framework-promotion.*RESOLVED\|...CLOSED' scaffolding/open-questions.md
0
```
Source-of-truth verified: the slice `book/src/spec/slices/cg_preconditioning_framework.md` reduction
header explicitly lists §L4 (lines 293-412) / §L4-v0.2 (413-471) / §L4-v0.3 (472-533) as
"RETAINED as load-bearing unique material (NOT yet lifted to a firm entry)" with the pending-lift
note naming `L4/preconditioning-framework` + OQ `l4-preconditioning-framework-promotion`. The 2 concept
canonical-example refs confirmed: `concepts/capability-typing.md:55` ("the canonical first use site")
+ `concepts/capability-typing.md:26`; `concepts/derived-view-hoisting.md` cites the slice's v0.3.
L0 anchor for the new chapter confirmed via codemap+disk: `BaseKspSolver::SetOperators(op, pc_op)` at
`palace/linalg/ksp.cpp:277`. PASS — recruit.

**D2 — `book/src/methodology/resolution-ladder.md` worked-example repair:** confirmed-stale content
present (not a no-op):
```
$ ls book/src/methodology/resolution-ladder.md
book/src/methodology/resolution-ladder.md
$ sed -n '131,134p' book/src/methodology/resolution-ladder.md
support is still soft**: `gram_reduce` did **not** promote, because it folds the
*off-diagonal* `bilinear-form` primitive, which is still `rough-in`. So `gram_reduce` stays
`rough-in`, and the four columns over it — `capacitance`, `inductance`, `electrostatic`,
`magnetostatic` — correctly stay `seed`. The next leaf to firm (`bilinear-form`, probe
```
This is FALSIFIED by the c095 cascade (`bilinear-form` firm, `gram_reduce` firm, the 4 columns firm).
Structural block check: none — `resolution-ladder.md` is meta-OWNED-by-batch-30? NO. It was authored
by `layer-intro-author` (D3, cycle-094) and is a reader-facing methodology page; per the c095 signals
it is "layer-intro-author-fixable now" (distinct from `goal-flow.md` which IS meta-phase-owned and
stays). PASS — recruit.

**D3 — O1 typing `book/src/L4-L3/solve-family-map-dissolution.md`:** OPEN (no typed frontmatter; linter
still reports O1):
```
$ ls book/src/L4-L3/solve-family-map-dissolution.md
book/src/L4-L3/solve-family-map-dissolution.md
$ grep -c '^rank:\|^edges:' book/src/L4-L3/solve-family-map-dissolution.md
0
$ python3 tools/graded-stack-lint/graded_stack_lint.py | grep 'solve-family-map-dissolution'
  [VIOLATION] L4/solve_family (firm) depends-on L4-L3/solve-family-map-dissolution (rough-in (test-coverage-bounded)) — a firm node rests on a rough-in (test-coverage-bounded) dep
```
HARD-gate-new safety verified: both endpoints firm on disk — `solve-family-map-dissolution.md:185`
§Status leads with `` `firm` — on the structural rotation``; `L4/solve_family` firm (c086);
`L4/ksp_solve` firm; `L4-L3/ksp-solve-driver-dissolution` is the cited per-member theme. So typing
`rank: firm` + `edges: depends-on: [L4/solve_family, L4/ksp_solve, L4-L3/ksp-solve-driver-dissolution]`
satisfies `rank(src) ≤ rank(dep)` immediately (this is the TRACKED-OPEN O1 promotion condition recorded
in `scaffolding/graded-stack-baseline-exceptions.md`). PASS — recruit.

**D4 — `read_status_line` linter parse-bug fix (`tools/graded-stack-lint/`):** bug confirmed at the
cited location (not already fixed):
```
$ sed -n '319,324p' tools/graded-stack-lint/graded_stack_lint.py
            blob = " ".join(lines[i + 1 : i + 6]).lower()
            for tok in ("partly-constructive", "rough-in (test-coverage-bounded)",
                        "rough-in", "roadmap_goal", "obstruction",
                        "partial-obstruction", "stub", "firm"):
                if tok in blob:
                    return tok
```
Blob-scans 5 lines in token-priority order with `rough-in*` ahead of `firm` (the bug). The exception
ledger documents 12 instances incl. O1. PASS — recruit (routing decision below).

**D5 — `matrix-weighted-norm-mutation-rotation.md:317` within-theme residue:** stale residue confirmed:
```
$ grep -n 'rough-in, test-coverage-bounded' book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md
317:operator (rough-in, test-coverage-bounded) into existing firm L1 vocabulary — `apply_linop` for the
```
`matrix-weighted-norm` is firm on disk (`L1/matrix-weighted-norm.md:110`, c091); this within-theme
prose-body residue narrates it as still rough-in. c095-signals flagged it as a c096 follow-up
(`matrix-weighted-norm-mutation-rotation-within-theme-stale-rough-in-residue`). PASS — recruit.

(No candidate matches the STOP-PROPOSING negative list — that list governs L3-backfill operator slugs;
none here is an L3 backfill.)

## D4 routing decision (tools/+methodology — meta-phase candidate)

The c095 signals offered D4 (`read_status_line` fix) as EITHER a c096 dispatch OR a batch-30 meta-phase
enactment. **Dispatch it in c096.** Rationale: (a) it is a self-contained `tools/`-only Python fix with
a precise spec already written in the exception ledger ("match only the leading inline-code token on the
first non-empty line after `## Status`"); (b) it is NOT a methodology-convention change — the typed-`rank:`
contract is unchanged, only the prose-fallback parse is corrected; (c) landing it this cycle means the
batch-30 meta-phase inherits a CORRECT linter for its own audit, rather than carrying a known false-positive
generator into the meta-phase. A `combinator-miner`/`same-layer-cross-cutter` is the wrong role (no book
content); route to `layer-intro-author` (it owns the linter per the c094 D2 precedent under that role) OR
keep it tool-scoped. I assign `layer-intro-author` (the c094 linter author-role) with a `tools/`-only scope.

## Dispatches

1. **agent:** `layer-intro-author`
   **scope:** P2 genuine-gap author — `book/src/L4/preconditioning-framework.md` (NEW, firm-on-first-authoring).
   Transcribe the `cg_preconditioning_framework` slice's unique-unlifted §L4 (the
   `KspParams`/`PcParams`/`OpBinding`/constructor-vs-body Haskell+TS form, slice lines 293-412), §L4-v0.2
   (capability typing — the `TrueOp`/`PcAssemblyOp` brands + `finestLevelUnwrap` brand-preservation +
   `pc_op = op` escape-hatch, lines 413-471), §L4-v0.3 (derived-view hoisting — the `pcBoundOp`
   stored-vs-bound-divergence derived view, lines 472-533) into a firm L4 entry, **re-citing L0 directly**
   (the `(op, pc_op)` binding at `palace/linalg/ksp.cpp:277` `BaseKspSolver::SetOperators` — disk-confirm
   the exact range; the slice's existing §L0 ranges are the localization map). HARD-gate-new: carry typed
   `rank: firm` + `edges:` frontmatter (`depends-on: [L4/ksp_solve]` + the constructed-operator concept
   refs as `reference`; an edge to a root is `reference`; satisfy `rank(u) ≤ min over depends-on deps` —
   `ksp_solve` is firm so firm-on-firm holds). Within proposed-changes, **re-point ONLY the canonical-example
   ref that the new firm chapter directly supersedes** — `concepts/capability-typing.md:26` + `:55` (currently
   "[cg_preconditioning_framework] L4 v0.2 ... the canonical first use site") to point the canonical-L4-example
   at `../L4/preconditioning-framework.md` (the refs the priorities item names as unblocked-by this chapter).
   NOTE (disk-confirmed this cycle): `concepts/derived-view-hoisting.md` does NOT actually cite the slice (its
   worked examples are CG/Chebyshev — the slice header's claim is its own framing); do NOT edit it. The OTHER
   ~9 concept pages that name the slice as introducing-slice/worked-example (`two_operator_split`,
   `constructed-operator-factory`, `complex-from-real-lift`, `finest-level-unwrap`, `counter-update`,
   `solver-as-operator`, `build-time-vs-run-time-stratification`, `rotation`, `dependency-map`) resolve FINE
   while the slice still exists — their repoint belongs to the DEFERRED deletion tranche, NOT this cycle.
   **Do NOT delete the slice** (deletion deferred to batch-31); do
   NOT touch `spec/index.md` or the SUMMARY slice rows. ADD the new chapter's SUMMARY row under `# L4`
   (alpha position within its kind-group) + its `L4/index.md` dep-map row — D1 is SOLE owner of these
   L4-index/SUMMARY edits this cycle (no other dispatch touches L4/index or the L4 SUMMARY section).
   **deps:** none.
   **rationale:** item-0 P2 — the ONE genuine gap the 2026-06-04 slice audit found; firm-on-first-authoring;
   high fan-out (unblocks `capability-typing.md` + `derived-view-hoisting.md` canonical-example refs that
   currently dangle on a to-be-deleted slice; the keystone that makes `cg_preconditioning_framework`
   deletable in the deferred tranche).

2. **agent:** `layer-intro-author`
   **scope:** c095 carry-forward — `book/src/methodology/resolution-ladder.md` worked-example repair.
   The worked example (lines ~99-134, the "well-foundedness invariant holds things back" illustration:
   `gram_reduce`/`domain_energy_reduce` capped at rough-in by rough-in `matrix-weighted-norm`/`bilinear-form`,
   the 4 columns held at `seed`) was FALSIFIED by the c095 cascade. Re-narrate to the post-cascade reality:
   EITHER (preferred) re-tell it as a COMPLETED rank-propagation success — "before c091/c095 the chain was
   capped; the cascade firmed `matrix-weighted-norm` (c091) then `bilinear-form` (c095), propagating rank up
   so `gram_reduce` promoted and the 4 columns reached firm" (the invariant now demonstrated by a discharge,
   not a block) — OR pick a still-pending example if one is cleaner. Keep the §rank-ladder + §invariant prose
   intact; only the worked example changes. This page is reader-facing methodology, NON-AUTHORITATIVE.
   **deps:** none.
   **rationale:** item-0 P3-residue (c095 carry-forward); OQ
   `bilinear-form-firm-flip-stale-narration-in-meta-owned-methodology-pages` (the
   `resolution-ladder.md` half — the `goal-flow.md:260-266` half stays for the meta-phase). A reader-facing
   page carrying a now-wrong worked example.

3. **agent:** `lifter`
   **scope:** O1 lazy-tail typing — `book/src/L4-L3/solve-family-map-dissolution.md`. Add typed
   `rank: firm` + `edges:` frontmatter (`depends-on: [L4/solve_family, L4/ksp_solve,
   L4-L3/ksp-solve-driver-dissolution]`; per §5 a lowering theme's edge is `depends-on` on both endpoints).
   Both endpoints firm on disk → the typed `rank: firm` satisfies the rank invariant immediately and clears
   O1 by construction (rank_violations 1→0). PURE edge-typing — NO maturity re-judgment, NO §Status prose
   change (the §Status already leads with `firm`). Optionally sweep any other firm-leading L4-L3 lowering
   theme that the lazy tail has reached and that has no typed frontmatter, ONLY if firm-on-firm holds (do
   not chase the whole directory — O1 is the deliverable). This is the TRACKED-OPEN O1 promotion condition
   in `scaffolding/graded-stack-baseline-exceptions.md`.
   **deps:** none.
   **rationale:** item-0 P2 — clears the lone residual rank violation, taking the typed subset to ZERO
   genuine rank gaps (the campaign's mechanical-completion for the typed frontier). Cheap, mechanical.

4. **agent:** `layer-intro-author`
   **scope:** `tools/`-only — fix the `read_status_line` token-priority parse bug in
   `tools/graded-stack-lint/graded_stack_lint.py:310-326`. Replace the 5-line blob-scan-in-priority-order
   with the leading-inline-code-token rule: read the FIRST non-empty line after `## Status` and match only
   its leading `` `token` `` (the project convention — the maturity word is the leading inline-code token),
   NOT a blob scan. Preserve the `derive_rank` precedence (explicit `rank:` token still wins over the prose
   fallback). Verify by re-running the linter (`--json`): the totals should be UNCHANGED on the typed subset
   (the typed `rank:` migration already routes around the bug for typed nodes) but untyped firm-leading nodes
   that previously mis-derived `rough-in` (the 12 ledger instances) should now read `firm`. Do NOT alter the
   typed-edge contract or any book content. Note in the report whether the fix changes the rank_violations /
   histogram counts (expected: it removes residual prose-fallback false positives for untyped tail nodes).
   **deps:** none.
   **rationale:** item-0 — the cycle's headline tooling friction
   (`graded-stack-lint-read-status-line-token-priority-bug`); 12 instances incl. O1; corroborated by D6/D7
   c095. Landing it gives the batch-30 meta-phase a correct linter for its own audit.

5. **agent:** `lifter`
   **scope:** within-theme stale-residue fix — `book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md:317`
   re-anchor the stale "operator (rough-in, test-coverage-bounded)" clause to the firm post-c091 reality
   (`matrix-weighted-norm` is firm, `L1/matrix-weighted-norm.md:110`). Surgical prose re-anchor only — the
   theme's structure is unchanged; this is the within-file/within-theme self-consistency discipline (the
   c091-cascade missed this one residue). Whole-file grep for any other surviving `mwn ... rough-in` narration
   in this theme and fix in the same pass (the c095 signal flagged this single :317 site; confirm it is the
   only one).
   **deps:** none.
   **rationale:** item-0 P2-adjacent (c095 carry-forward); OQ
   `matrix-weighted-norm-mutation-rotation-within-theme-stale-rough-in-residue`. A within-theme stale-prose
   residue from the c091 cascade.

## Overlap analysis

Pairwise (6 dispatches → 15 pairs). Two dispatches OVERLAP iff they modify the same operator entry /
rewrite the same theme body / write the same shared index region.

- **D1 × D2:** D1 writes `L4/preconditioning-framework.md` + `L4/index.md` + L4 SUMMARY + 2 concept pages
  (`capability-typing.md`, `derived-view-hoisting.md`); D2 writes `methodology/resolution-ladder.md`.
  Disjoint files. NON-OVERLAPPING.
- **D1 × D3:** D1 = L4 entry + L4 index/SUMMARY + concepts; D3 = `L4-L3/solve-family-map-dissolution.md`
  frontmatter only. Disjoint. NON-OVERLAPPING. (Both are L4-adjacent but D3 touches a single L4-L3 theme
  file's frontmatter, not L4/index or the L4 SUMMARY section D1 owns.)
- **D1 × D4:** D1 = book content; D4 = `tools/graded-stack-lint/` only. Disjoint. NON-OVERLAPPING.
- **D1 × D5:** D1 = L4 + concepts; D5 = `L1-L0/matrix-weighted-norm-mutation-rotation.md`. Disjoint.
  NON-OVERLAPPING.
- **D2 × D3:** `resolution-ladder.md` vs `solve-family-map-dissolution.md`. Disjoint. NON-OVERLAPPING.
- **D2 × D4:** methodology page vs `tools/`. Disjoint. NON-OVERLAPPING.
- **D2 × D5:** methodology page vs L1-L0 theme. Disjoint. NON-OVERLAPPING.
- **D3 × D4:** D3 types a theme `rank: firm`; D4 fixes the linter. **Soft interaction, NOT a file overlap:**
  D4 changes how the linter derives rank for UNTYPED nodes; D3 types O1's node so it bypasses the prose
  fallback entirely. They touch DIFFERENT files (the theme vs the tool). The linter-verification step in
  D4's report runs against the PRE-integration on-disk state (O1 still untyped at D4's read time, since
  reports don't see each other's proposed-changes); the finalize linter run sees BOTH landed. No conflict —
  both independently drive rank_violations toward 0. NON-OVERLAPPING (parallel-safe; flagged as a benign
  data-point for the finalize linter run).
- **D3 × D5:** L4-L3 theme frontmatter vs L1-L0 theme prose. Disjoint. NON-OVERLAPPING.
- **D4 × D5:** `tools/` vs L1-L0 theme. Disjoint. NON-OVERLAPPING.

Shared-index / single-owner check: only D1 touches a layer index (`L4/index.md`) + a SUMMARY section
(`# L4`). No other dispatch writes L4/index or the L4 SUMMARY section, so there is NO consolidated-tally
contention (the parallel-blind-shared-index guard does not bind — single writer). D1 is SOLE owner of the
L4-index/SUMMARY edits by construction. No dual-registration partition needed (only one landing into the
L4 index this cycle).

**Forward-reference check:** D1 authors `L4/preconditioning-framework.md` and itself re-points the 2 concept
pages that reference it — no SIBLING dispatch forward-references D1's new slug, so the cross-report
forward-reference-slug guard does not bind (D1 owns both the new file and its incoming concept refs).

**Verdict: ALL SIX DISPATCHES ARE NON-OVERLAPPING — fully parallel-safe (one wave).** Conflict-tolerance
philosophy: when in doubt mark PARALLEL; here there is no doubt (six disjoint file sets).

## Sequencing schedule

**Wave 1 (all parallel — D1, D2, D3, D4, D5):** all six dispatches are file-disjoint with no
forward-reference dependency. Single wave.

(No second wave needed. The integrator pipeline is unchanged: 5 producers → 5 critics → 5 repairers →
`integrator-per-report` ×5 serial → ONE `integrator-finalize`. The finalize runs the graded-stack linter on
the LANDED state — expected result after D3 lands O1-typing + D4 lands the parse fix: rank_violations = 0,
which is the batch-closing confirmation gate.)

## Open questions / caveats

- **The DEFERRED P2 slice-deletion tranche is the dominant remaining graded-stack phase** and should be a
  batch-31 LEAD candidate (recorded in `priorities.md`). I scoped it OUT of c096 deliberately (batch-closing
  cycle; the citation web is ~30 krylov-step anchors + ~6 dissolution themes + ~10 concept pages — a
  multi-dispatch campaign). The batch-30 meta-phase should pick it up as the next campaign LEAD. The c096 D1
  closes the one author-gap that blocks it.
- **D4 routing (tools/ vs meta-phase):** I dispatched the `read_status_line` fix in c096 rather than leaving
  it for the batch-30 meta-phase (rationale in the §D4 routing decision above — self-contained, spec already
  written, gives the meta-phase a correct linter). If the human/meta-phase prefers tools fixes to route
  through meta-phase write-authority, this is the one to reconsider — but it is `tools/`-only and the
  exception ledger already specifies the fix, so a producer dispatch is appropriate.
- **`goal-flow.md:260-266` stays for the meta-phase** (it is meta-phase-owned; carries the SAME stale
  "stay rough-in / stay seed" cascade narration as the `resolution-ladder.md` worked example D2 fixes). The
  batch-30 meta-phase goal-flow refresh should reconcile it. Flagged so the partition is explicit — D2 fixes
  ONLY the layer-intro-author-owned `resolution-ladder.md`.
- **Finalize linter expectation:** after D3 (O1 typed firm) + D4 (parse fix) land, the finalize
  `graded_stack_lint.py --json` run should report `rank_violations = 0`. If it reports MORE, a D3/D4
  proposed-change did not land (re-check per-report integration). This is the mechanical batch-closing
  confirmation gate the c095 exception ledger anticipated.
- **D1 firm-on-first-authoring gate:** `L4/preconditioning-framework.md` goes straight to `firm` per the
  2026-06-04 slice audit (the §L4/v0.2/v0.3 material is a structural read-off of positive Palace source +
  the existing firm `L1/ksp_solve` framework). If D1's author finds the v0.2 capability-typing or v0.3
  derived-view material rests on a non-firm or constructive sub-part, downgrade per the
  `partly-constructive` / `firm-on-positive-structure` conventions and state the gate — but the audit
  expectation is firm.
