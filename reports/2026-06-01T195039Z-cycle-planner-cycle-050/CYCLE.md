---
agent: cycle-planner
invoked_at: 2026-06-01T195039Z
scope: cycle-050 dispatch plan
status: pending
---

# Cycle 050 dispatch plan

## Goals selected this cycle

Cycle-050 is the REFACTOR-PASS ENACTMENT cycle (2nd primary cycle of meta-batch-15;
the batch-15 meta-phase fires after cycle-051). It consumes the cycle-049 D1/D2
replace-and-propagate maps + the D3 18-theme degenerate-lowering worklist. **Core planner
call: land ONLY the convention-INDEPENDENT, churn-free SAFE SLICE and HOLD all leaf-chapter
deletions for the batch-15 meta-phase** (analogous to the c042 fork-steering). The
`collapsed-leaf-disposition-convention-cohort-wide` OQ (delete-vs-redirect-stub for the L2/L3
`dot`/`scal`/`axpy`/`axpby`/`axpbypcz` leaves) is UNSETTLED and was explicitly routed to the
meta-phase by D1 AND D2; mass deletion now would pre-empt that ratification. So cycle-050
lands what is safe under EITHER ruling and touches NO held-for-deletion chapter: (1) author
the two L3 combinators (the propagation half — pure additions), (2) demote the 4 CLEAN
non-fold-family theme pairs (whose in-line home is a standalone entry NOT slated for
collapse), (3) verify-body-audit the 2 constructed-operator-gate pairs. The fold-family theme
demotions, the L3-leaf re-expression, and ALL leaf-chapter deletions sequence to cycle-051 /
the meta-phase.

## Deliverable-presence verification (paste-inline evidence)

Per the MANDATORY pre-dispatch four-step check (CLAUDE.md §Discipline; skill
`verify-dispatch-scope-not-already-discharged`). STOP-PROPOSING NEGATIVE LIST (`lu_solve`,
`back_solve`, `ls-update-column`, 4 NLEPS atoms; `apply_nonlinear_pencil` HELD) consulted —
no scope matches it.

- **D1 `book/src/L3/linear_combination.md` — AUTHOR (must be ABSENT):**
  `ls L3/linear_combination.md` → `No such file or directory`, `exit=2`. ABSENT ✓ — open by
  construction (new operator entry; the c049 D1 map mandates authoring it; the L3 cohort cites
  `linear_combination` zero times). Recruit.
- **D2 `book/src/L3/inner_product.md` — AUTHOR (must be ABSENT):**
  `ls L3/inner_product.md` → `No such file or directory`, `exit=2`. ABSENT ✓. The plain-text
  rough-in dep-map row already stands at `book/src/L3/index.md:29` (verified inline:
  `grep -n inner_product L3/index.md` → `29:| `inner_product` *(rough-in; no anchor yet)* …
  harvester authors `book/src/L3/inner_product.md` cycle-050`). Open by construction. Recruit.
- **D3 `assemble-diagonal` demotion — themes must be PRESENT, entries present, not held:**
  `ls` → `L3-L2/assemble-diagonal-body-identity.md`, `L2-L1/assemble-diagonal-leaf-identity.md`,
  `L3/assemble-diagonal.md`, `L2/assemble-diagonal.md` all present, `exit=0`. Both themes
  classified DEMOTE-to-inline (clean, no fold parent) in D3 worklist §B; the operator is NOT
  slated for collapse (no combinator parent). Recruit.
- **D4 `elementwise_product` demotion:** `ls` → `L3-L2/elementwise-product-body-identity.md`,
  `L2-L1/elementwise-product-leaf-identity.md`, `L3/elementwise_product.md`,
  `L2/elementwise_product.md` all present, `exit=0`. (Note the slug asymmetry: theme slugs are
  hyphenated `elementwise-product-*` per the c043 rename; the operator chapter keeps the
  underscore `elementwise_product.md` matching firm L1/L3 — confirmed both spellings on disk.)
  Clean DEMOTE, no fold parent. Recruit.
- **D5 `reciprocal` demotion:** `ls` → `L3-L2/reciprocal-body-identity.md`,
  `L2-L1/reciprocal-leaf-identity.md`, `L3/reciprocal.md`, `L2/reciprocal.md` present,
  `exit=0`. Clean DEMOTE, standalone elementwise leaf, no fold parent. Recruit.
- **D6 `normalize` demotion:** `ls` → `L3-L2/normalize-body-identity.md`,
  `L2-L1/normalize-leaf-identity.md`, `L3/normalize.md`, `L2/normalize.md` present, `exit=0`.
  D3 worklist §B: fused composite `nrm2 ∘ scal`, "demotes cleanly" (resolved third sub-shape,
  OQ ledger `:651`). NOT a fold member; demotes to its OWN entry. Recruit.
- **D7 count-ownership (`L3-L2/index.md` + `L2-L1/index.md` + `L3/index.md`):** indexes present
  (`ls L2-L1/index.md L3-L2/index.md L3/index.md` → all present). Open by construction
  (consolidated-tally write owner for the c050 wave — required by the count-ownership partition
  since ≥2 dispatches delete themes from / add entries to these indexes). Recruit.
- **D8 `divfree-projector` + `jacobi-smoother` VERIFY (audit, observation-only):** `ls` →
  `L3-L2/divfree-projector-body-identity.md`, `L2-L1/divfree-projector-leaf-identity.md`,
  `L3-L2/jacobi-smoother-body-identity.md`, `L2-L1/jacobi-smoother-leaf-identity.md` present,
  `exit=0`. These 4 themes are the verify-body-before-demoting pair (D3 read heads only). Audit
  is open by construction (no prior verdict on disk). Recruit.

**Structural-gate check:** no dispatch is blocked by a methodology gate. The leaf-chapter
deletions ARE structurally gated (the unsettled `collapsed-leaf-disposition-convention-cohort-wide`
OQ + the batch-15 meta-phase) — correctly NOT proposed this cycle (held). All 8 recruited
dispatches are convention-independent.

## Why the SAFE-SLICE / HOLD call (the load-bearing planner judgment)

The cycle-050 enactment naively spans: collapse ~6 L2 leaf chapters + ~6 L3 leaf chapters,
author 2 L3 combinators, demote 18 themes, propagate to L4. Three reasons this is the wrong
single-cycle bite:

1. **The leaf-chapter disposition is UNSETTLED and meta-phase-gated.** D1 (b.1) and D2 (b.1)
   both recommend delete-with-SUMMARY-removal (D1: redirect-stub for `scal` because it has live
   `normalize`/`elementwise_product` consumers) but BOTH explicitly route the cohort-wide rule
   to the batch-15 meta-phase (`collapsed-leaf-disposition-convention-cohort-wide`). Deleting
   the leaves now pre-empts a ratification that fires after c051. The c042 precedent (steer
   around the leaf-vs-fold fork; land the fork-independent slice) is the model.

2. **Theme demotion for the FOLD families is entangled with held chapters.** The L2>L1
   `-leaf-identity` ABSORB-into-combinator-note depends on re-anchoring inbound links from the
   held leaf chapters (`L2/dot.md` etc.); the L3>L2 `-body-identity` demote-to-inline lands on
   L3 leaves that are themselves slated to collapse into the new L3 combinators. Doing this now
   means re-anchoring chapters we will delete next batch — churn. **Decouple:** author the L3
   combinators WITH their own in-line §"Downward to L2" notes (the pre-built demotion home),
   and defer the fold-family theme demotion + L3-leaf re-expression to c051 (when it can land
   together with, or just before, the meta-ratified leaf disposition).

3. **The NON-fold families ARE clean and convention-independent.** `assemble-diagonal`,
   `elementwise_product`, `reciprocal`, `normalize` have NO fold parent (D3 worklist §B) — their
   operators stay standalone entries (not collapsed), so demoting their themes lands in-line
   notes on entries that are NOT held-for-deletion and touches no held chapter. This is the
   genuinely safe demotion slice. The 2 constructed-operator gates (`divfree`/`jacobi`) need a
   body-verify first (D3 read heads only) → audit this cycle, enact c051.

Net: cycle-050 makes real, non-reversible progress (2 new L3 combinator entries + 4 theme-pair
demotions = −8 degenerate themes) with ZERO pre-emption of the meta-phase and ZERO churn on
held chapters.

## Dispatches

1. **agent:** `harvester`
   **scope:** Author `book/src/L3/linear_combination.md` — the L3 iteration-rotation rendering
   of the firm L2 `linear_combination` combinator (inverted c049 D1). Whole-tensor variadic
   fold over `[(Scalar, Tensor[N])]`; `foldl (\acc (a,t) -> acc + scal a t) (zeros N) pairs` at
   the L3 field-op layer; **no sequential obstruction** (the fold is over the term list,
   element-local in N — `L3/axpy.md:58` establishes the BLAS-1 cohort carries no obstruction).
   Carry the same concatenation-homomorphism + multilinearity laws + empty-list-identity as the
   L2 entry, with the IEEE-754 summation non-law deferred to the L2>L1 fold-spec (KEEP, c049
   D1 (c)). Include an in-line **§"Downward to L2"** note: the L3 fold is value-thread-isomorphic
   to the L2 fold (identity-in-form across the edge) — this note is the pre-built home the four
   `{scal,axpy,axpby,axpbypcz}-body-identity` L3>L2 themes demote into at c051. Register the
   entry's OWN `L3/index.md` dep-map row (dual-registration: own row only; DEFER the tally to
   D7). L0 anchors inherited from the firm L2 combinator (cited c018 — `vector.cpp:702-712,
   726-730,745-758`, `vector.hpp:305-316`; do NOT re-localize). **Does NOT touch the L3 leaves**
   (`L3/scal.md` etc.) — their re-expression through this combinator is c051, gated on the leaf
   disposition.
   **deps:** none
   **rationale:** the propagation half of replace-and-propagate (c049 D1 (b.3)); HIGH fan-out
   (the combinator was never propagated to L3 — the L3 cohort re-derives base forms). Serves
   `refactor-pass-l3-linear-combination`, OQ `degenerate-lowering-demotion-worklist-cycle-050-consumable`.

2. **agent:** `harvester`
   **scope:** Author `book/src/L3/inner_product.md` — the L3 rendering of the firm L2
   `inner_product` combinator (inverted c049 D2). `inner_product :: Tensor[N] -> Tensor[N] ->
   Scalar` as a whole-tensor reduce-to-scalar field reduction with no sequential obstruction
   (the length-axis indices reduce in parallel in exact arithmetic; the pinned reduction tree is
   an L0 non-law). Conjugation / element-type / weight specializations (`dot` Hermitian, `tdot`
   unconjugated, `bilinear_form` M-weighted) read at fixed axis-values — specialization notes,
   NOT separate entries. **Upgrade the existing plain-text rough-in row at `book/src/L3/index.md:29`
   to a live link** (the file now exists). Carry an in-line **§"Downward to L2"** note (the home
   `dot-body-identity` demotes into at c051). **`nrm2` is the CONSUMER** (`√ ∘ abs ∘ inner_product`
   at y=x), NOT a member — its theme demotes onto the `nrm2` entry, NOT here (c051; do-NOT-merge
   consumer boundary, ledger `:595` carve-out, fork-invariant). **Does NOT touch the L3
   `dot`/`nrm2` leaves** (c051). L0 anchors inherited from the firm L2 combinator (cited c019).
   **deps:** none
   **rationale:** the propagation half for the `inner_product` family (c049 D2 (b.5)); HIGH
   fan-out. Serves `refactor-pass-l3-inner-product`.

3. **agent:** `lifter`
   **scope:** Demote the `assemble-diagonal` degenerate theme pair. Delete
   `book/src/L3-L2/assemble-diagonal-body-identity.md` + `book/src/L2-L1/assemble-diagonal-leaf-identity.md`;
   add the equivalent in-line **§"Downward to L2"** note on `book/src/L3/assemble-diagonal.md` and
   **§"Downward to L1"** note on `book/src/L2/assemble-diagonal.md` (operator-to-data extraction
   leaf, identity-in-form; PRESERVE the matrix-free approximate-diagonal non-law in the note —
   it is the one load-bearing fact); re-anchor any inbound links to the in-line notes; remove the
   two lines from `SUMMARY.md` (`:55` body-identity, `:101` leaf-identity). **DEFER both the
   `L3-L2/index.md` and `L2-L1/index.md` tallies to D7** (count-owner). NO leaf-chapter deletion
   (assemble-diagonal stays a standalone entry — no fold parent).
   **deps:** none
   **rationale:** clean convention-independent demotion (D3 worklist §B; touches no held
   chapter). Serves `refactor-pass-nonfold-demotion`, OQ `degenerate-lowering-cohort-is-18-not-12-cycle-050-must-cover-all`.

4. **agent:** `lifter`
   **scope:** Demote the `elementwise_product` degenerate theme pair. Delete
   `book/src/L3-L2/elementwise-product-body-identity.md` + `book/src/L2-L1/elementwise-product-leaf-identity.md`;
   add the in-line §"Downward to L2"/§"Downward to L1" notes on `book/src/L3/elementwise_product.md`
   + `book/src/L2/elementwise_product.md` (Hadamard binary leaf, identity-in-form); re-anchor
   inbound links; remove the two `SUMMARY.md` lines (`:59` body-identity, `:105` leaf-identity).
   **DEFER both index tallies to D7.** NO leaf-chapter deletion (standalone, no fold parent).
   NOTE the slug spelling: theme slugs hyphenated (`elementwise-product-*`), operator chapter
   underscore (`elementwise_product.md`) — do not "normalize" the chapter slug.
   **deps:** none
   **rationale:** clean demotion (D3 §B). Serves `refactor-pass-nonfold-demotion`.

5. **agent:** `lifter`
   **scope:** Demote the `reciprocal` degenerate theme pair. Delete
   `book/src/L3-L2/reciprocal-body-identity.md` + `book/src/L2-L1/reciprocal-leaf-identity.md`;
   add the in-line §"Downward to L2"/§"Downward to L1" notes on `book/src/L3/reciprocal.md` +
   `book/src/L2/reciprocal.md` (elementwise multiplicative-inverse leaf, identity-in-form);
   re-anchor inbound links; remove the two `SUMMARY.md` lines (`:58` body-identity, `:103`
   leaf-identity). **DEFER both index tallies to D7.** NO leaf-chapter deletion.
   **deps:** none
   **rationale:** clean demotion (D3 §B). Serves `refactor-pass-nonfold-demotion`.

6. **agent:** `lifter`
   **scope:** Demote the `normalize` degenerate theme pair. Delete
   `book/src/L3-L2/normalize-body-identity.md` + `book/src/L2-L1/normalize-leaf-identity.md`;
   add the in-line §"Downward to L2"/§"Downward to L1" notes on `book/src/L3/normalize.md` +
   `book/src/L2/normalize.md` (fused composite `nrm2 ∘ scal`, identity on the composite itself;
   the resolved third thin-identity sub-shape, OQ ledger `:651`); re-anchor inbound links; remove
   the two `SUMMARY.md` lines (`:60` body-identity, `:104` leaf-identity). **DEFER both index
   tallies to D7.** NO leaf-chapter deletion (fused composite, not a fold member — stays a
   standalone entry). NOTE: `normalize`'s body references `nrm2`/`scal` — leave those references
   as-is (their re-expression is the held fold-family c051 work; the `normalize` note describes
   the composite, not the constituents' lowering).
   **deps:** none
   **rationale:** clean demotion (D3 §B; "demotes cleanly"). Serves `refactor-pass-nonfold-demotion`.

7. **agent:** `layer-intro-author`
   **scope:** SOLE consolidated-count owner for the c050 wave. Update the consolidated tallies +
   §Working-Notes narratives in: (i) `book/src/L3-L2/index.md` — −4 body-identity themes
   (assemble-diagonal/elementwise-product/reciprocal/normalize deleted by D3–D6); (ii)
   `book/src/L2-L1/index.md` — −4 leaf-identity themes (same four); (iii) `book/src/L3/index.md` —
   +2 firm L3 combinator entries (`linear_combination` from D1, `inner_product` from D2 — the
   latter upgrades the existing rough-in row to firm). Reconcile the degenerate-cohort narrative:
   18 pairs → after the 4 clean non-fold pairs demote this cycle, **10 pairs remain** (the 4
   fold-family pairs `scal`/`axpy`/`axpby`/`axpbypcz` + `dot` + `nrm2` held for c051; the 2
   verify-pairs `divfree-projector`/`jacobi-smoother` pending D8) — state the c050-vs-c051 split
   explicitly so the count is not read as "stranded." Record that the L3 combinator entries are
   the propagation half (the L3 leaf re-expression is c051). D3–D6 add ONLY their own SUMMARY
   removals + in-line notes; D1/D2 add ONLY their own L3/index dep-map rows; **D7 owns every
   consolidated tally.**
   **deps:** D1, D2, D3, D4, D5, D6 (reads their landed deletions/additions to write accurate
   tallies)
   **rationale:** count-ownership partition (cycle-039 meta; `parallel-blind-shared-index-count-divergence`)
   — ≥2 dispatches mutate each index, so exactly one owner writes the consolidated counts. Serves
   `refactor-pass-c050-count-ownership`.

8. **agent:** `cross-layer-cross-cutter`
   **scope:** VERIFY-body audit (observation-only, NO book mutation) of the two
   constructed-operator-gate pairs `divfree-projector` + `jacobi-smoother`. Read the bodies of
   `L3-L2/divfree-projector-body-identity.md` + `L2-L1/divfree-projector-leaf-identity.md` +
   `L3-L2/jacobi-smoother-body-identity.md` + `L2-L1/jacobi-smoother-leaf-identity.md` and the
   corresponding L3/L2 entries IN FULL (D3 c049 read heads only). Confirm whether each is a
   genuine degenerate identity-in-named-terms lowering (→ DEMOTE-OK, enact c051) or whether the
   L2 form erases/renames a composition step (`divfree-projector`: four-step `WeakDiv → Z →
   ksp_solve → Grad`; `jacobi-smoother`: `op.dinv ⊙ x`) — in which case it is KEEP-substantive
   (off the worklist). Emit the verdict per pair. Observation-only; the actual demotion (if
   DEMOTE-OK) is c051.
   **deps:** none
   **rationale:** the verify-body-before-demoting requirement (D3 worklist §B + OQ
   `degenerate-lowering-cohort-is-18-not-12`). Serves `refactor-pass-divfree-jacobi-verify`.

## Overlap analysis

Pairwise (the operative test: same operator entry modified, OR same theme body rewritten, OR
one names a slug the other authors; distinct index ROWS are parallel-safe, the consolidated
TALLY is owned by D7):

- **D1 × D2:** disjoint files (`L3/linear_combination.md` vs `L3/inner_product.md`). Both add a
  row to `L3/index.md` — distinct rows (parallel-safe); both DEFER the `L3/index` tally to D7.
  NOT overlapping → parallel.
- **D1/D2 × D3/D4/D5/D6:** disjoint operators and disjoint files. D1/D2 author new L3 combinator
  entries + add `L3/index` rows; D3–D6 delete non-fold themes + edit non-fold L3/L2 entries +
  remove SUMMARY lines. The only shared file is `SUMMARY.md` (D2 may live-link its new L3 entry;
  D3–D6 remove theme lines) — these are **distinct, non-adjacent line edits** (additions to the
  L3 operator list vs removals from the L3-L2/L2-L1 theme lists), parallel-safe by the
  distinct-rows rule. NOT overlapping → parallel.
- **D3 × D4 × D5 × D6:** four disjoint operators (`assemble-diagonal` / `elementwise_product` /
  `reciprocal` / `normalize`); disjoint theme files, disjoint L3/L2 entry files. Each removes
  its OWN 2 SUMMARY lines (distinct, non-adjacent). All DEFER index tallies to D7. NOT
  overlapping → parallel. (`normalize` references `nrm2`/`scal` in its body but only reads them;
  it does not modify the held leaf chapters or the fold-family themes.)
- **D7 × D1/D2/D3/D4/D5/D6:** D7 is the consolidated-tally owner and reads the landed
  state of all six producers, then writes the `L3-L2/index.md` + `L2-L1/index.md` + `L3/index.md`
  consolidated counts + §Working-Notes narrative. The producers DEFER those tallies. D7 touches
  the count/narrative region; producers touch their own rows/SUMMARY lines — **partitioned, but
  D7 must read the landed deletions/additions to count correctly** → sequential AFTER D1–D6.
- **D8 × all:** observation-only, NO book mutation; reads divfree/jacobi themes + entries (which
  no other dispatch touches this cycle). NOT overlapping → parallel.

No two dispatches modify the same operator entry, rewrite the same theme body, or
author/forward-reference the same not-yet-existing slug. No forward-reference slug coordination
needed (D1/D2 author distinct top-level combinator slugs that the c049 maps already named
canonically: `L3/linear_combination`, `L3/inner_product`).

## Sequencing schedule

- **Wave 1 (parallel):** D1, D2, D3, D4, D5, D6, D8. All seven are mutually non-overlapping
  (disjoint files / distinct rows / observation-only). The four lifter demotions + two harvester
  authorings + one audit run together.
- **Wave 2 (after wave-1 reports land):** D7 (count-owner). It reads the landed deletions
  (D3–D6 removed 8 themes) and additions (D1/D2 added 2 L3 entries) to write the consolidated
  `L3-L2/index.md` / `L2-L1/index.md` / `L3/index.md` tallies + the degenerate-cohort
  §Working-Notes reconciliation. (Per the cycle structure: this wave ordering governs the
  DISPATCH order; there is one `integrator-finalize` at cycle end — the book is not rebuilt
  between waves.)

## Open questions / caveats

- **HOLD the leaf-chapter deletions for the batch-15 meta-phase — stated explicitly.** The L2
  `dot`/`axpy`/`axpby`/`axpbypcz` chapter deletions + the D1 `scal` redirect-stub + the L3-leaf
  collapses are NOT proposed this cycle. They are gated on the meta-phase ratifying
  `collapsed-leaf-disposition-convention-cohort-wide` (delete-vs-redirect-stub), which fires after
  cycle-051. This is the c042 fork-steering analog — make convention-independent progress now,
  let the meta-phase settle the convention, enact the deletions in batch-16.
- **The fold-family theme demotions are sequenced to cycle-051, not held indefinitely.** dot/nrm2
  → `inner_product`, scal/axpy/axpby/axpbypcz → `linear_combination` (ABSORB-into-combinator-note
  + re-anchor the held-leaf inbound links), plus the L3-leaf re-expression through the D1/D2 L3
  combinators. They are deferred because they entangle with the held leaf chapters (re-anchoring
  inbound links on chapters slated for deletion is churn). cycle-051 is the LAST cycle before the
  meta-phase; it can land the fold-family demotion + L3-leaf re-expression, leaving ONLY the leaf
  deletions (the genuinely meta-gated step) for batch-16. **Risk if c051 is tight:** the
  fold-family demotion is ~6 operators × 2 edges; if it does not all fit c051, the residue + the
  leaf deletions both fall to batch-16 — acceptable (the L3 combinators + clean demotions landed
  c050 are the irreversible-progress core).
- **D8 verdict feeds c051, not c050.** If D8 finds `divfree-projector` / `jacobi-smoother`
  KEEP-substantive (the L2 form erases a composition step), those 2 pairs leave the worklist
  entirely and the "18" denominator drops to 16 — record in the c051 plan / meta-phase intake.
- **L4-propagation (`l4-propagation-depth-linear-combination`) intentionally NOT scheduled.** The
  c049 D1 (b.4) note (express the krylov-step update group + chebyshev in-place axpy/scal through
  `linear_combination`) is "flag, don't force" low-priority (solvers-as-test-load regime). It
  rides above the L3 combinators that only land this cycle — premature until the L3 propagation
  is settled. Carries to c051+ as a low-priority flag.
- **Solvers-as-test-load (redirect program item 3) NOT scheduled this cycle.** The refactor pass
  (item 1) is the highest priority and fills the cycle; solvers are LOW-priority and must never
  preempt spine work. They begin only after the refactor pass settles (post-meta-phase).
- **Citation-drift firming touches (`inner-product-fold-specialization-citation-drift`) NOT
  scheduled** — they are a lifter/firming touch on a KEEP theme, low-value this cycle; carry to
  c051 or the meta-phase firming pass (the KEEP verdict stands regardless).
- **Methodology-adjustment watch (for the batch-15 meta-phase, ~1 cycle out):** the recurrence
  `specialized-agent-direct-write-to-book-during-dispatch` (D2 c049 leaked a dispatch-phase book
  write; repairer reverted + reconstructed clean) is flagged in the c049 integrator-signals for
  meta-phase assessment of whether a stronger prevention (producer-spec bullet / harness guard) is
  warranted. The c050 producers (esp. the 4 lifters doing deletions) are the same write-authority
  surface — if another leak occurs this cycle it strengthens the case; noted here so the
  meta-phase (end of this batch) has the data point.
