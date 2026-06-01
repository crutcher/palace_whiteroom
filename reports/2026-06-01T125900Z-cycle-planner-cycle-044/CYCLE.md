---
agent: cycle-planner
invoked_at: 2026-06-01T125900Z
scope: cycle-044 dispatch plan
status: pending
---

# Cycle 044 dispatch plan

Cycle-044 is the **SECOND primary cycle of meta-batch-13** (cycles 043/044/045; the batch-13 meta-phase fires AFTER cycle-045's finalize, as a separate dispatch — NOT this cycle).

## Goals selected this cycle

State after cycle-043: the `l2-floor-under-l3-leaf-cohort` is effectively COMPLETE (L2 firm 21; axpy-family + normalize floors landed; chebyshev already-floored via `chebyshev-iteration`); the leaf-vs-fold fork is RATIFIED in-artifact; L2>L1 firm 19, L3>L2 firm 14-of-18. Two consequences drive this cycle, both under the `foundation_solidity` weight:

1. **Discharge the cohort-completion debt** the c043 floors created — exactly mirroring the c042→c043 sweep. The 4 NEW-floor L3 entries (`axpy`/`axpby`/`axpbypcz`/`normalize`) still assert "no interposed L2 entry / direct L3>L1 hop / no L3-L2 theme" (verified-stale on-disk below); the deferred `l3-index-audit-block-citation-drift` index-wide re-pin is still open; and 12 chapter bodies still carry the old `l2-floor-under-l3-blas1-cohort` directive slug. ONE consolidated `lifter` sweep (D1, the lead — HIGH).
2. **Resume the substantive L3↔L2 frontier** now that the floor cohort rests under it. The two highest-fan-out substantive moves that pass the deliverable-presence check: (a) an **audit-first subsumption check** on `chebyshev-smoother` L3 (strong prior toward subsumed-by-firm-L3-`chebyshev` — observation-only, per the c036 D2 audit-first precedent), and (b) closing the FIRST substantive `l3-l2-rotation-theme-coverage-gap` entry — the **`orthogonalize` L3>L2 MGS-vs-CGS rotation theme** (a genuine iteration-rotation, not a thin identity) + its deferred-since-c040 **`verified_against:` audit**.

`apply_nonlinear_pencil` L3 is NOT dispatched (it folds into a future eigsolve-variant pass per the plan + c040 integrator-signals, not a standalone L3 row). The STOP-PROPOSING NEGATIVE LIST is honored (no scope touches `lu_solve`/`back_solve`/`ls-update-column`/the 4 NLEPS atoms).

## Deliverable-presence verification

Per the MANDATORY paste-inline-evidence procedure (CLAUDE.md / role-spec §Discipline). Literal command output per dispatch below.

### D1 — consolidated lifter sweep (re-anchor 4 NEW-floor L3 + index-citation-drift + directive-slug residual)

**Step 1 (file existence — the 4 NEW-floor L3 entries the sweep re-anchors):**
```
$ ls -la book/src/L3/{axpy,axpby,axpbypcz,normalize}.md
-rw-rw-r-- 1 ... 18304 May 27 17:23 book/src/L3/axpy.md
-rw-rw-r-- 1 ... 16056 May 27 17:24 book/src/L3/axpby.md
-rw-rw-r-- 1 ... 15053 May 27 17:25 book/src/L3/axpbypcz.md
-rw-rw-r-- 1 ... 35461 May 31 15:05 book/src/L3/normalize.md
```
**Step 2 (maturity / the staleness IS present — these are firm L3 entries asserting now-false "no L2 floor" clauses):**
```
$ grep -niE "no interposed L2|direct L3>L1|no L3-L2|directly because" book/src/L3/{axpy,axpby,axpbypcz,normalize}.md
axpy.md:97:    ...The L3>L1 rotation is direct; no L2 intermediate is required...
axpby.md:101:   ...The L3>L1 rotation is direct; no L2 intermediate is required because `axpby` is an L1 leaf...
axpbypcz.md:106:  ...The L3>L1 rotation is direct; no L2 intermediate is required.
normalize.md:6:   lowers_to: ...no L3-L2/L3-L1 theme — see Lowers-to
normalize.md:27:  - **Downward** to L1: ...with **no interposed L2 entry and no `L3-L2`/`L3-L1` theme file**...
normalize.md:131: ...**no interposed L2 entry, no `L3-L2`/`L3-L1` theme file**...
```
These clauses are STALE: the c043 floors `book/src/L2/{axpy,axpby,axpbypcz,normalize}.md` (firm) + the L3>L2 `book/src/L3-L2/{axpy,axpby,axpbypcz,normalize}-body-identity.md` themes (firm) all landed cycle-043 — verified present:
```
$ for f in axpy axpby axpbypcz normalize; do printf "L2/%s.md:%s L3-L2/%s-body-identity.md:%s\n" "$f" "$(test -f book/src/L2/$f.md&&echo OK)" "$f" "$(test -f book/src/L3-L2/$f-body-identity.md&&echo OK)"; done
L2/axpy.md:OK L3-L2/axpy-body-identity.md:OK
L2/axpby.md:OK L3-L2/axpby-body-identity.md:OK
L2/axpbypcz.md:OK L3-L2/axpbypcz-body-identity.md:OK
L2/normalize.md:OK L3-L2/normalize-body-identity.md:OK
```
**Step 2b (index-citation-drift sub-target — `l3-index-audit-block-citation-drift`, opened c043 D1, OQ ledger:937, surfaced-not-enacted):** the cycle-036 audit-block shift left cross-entry `L3/index.md:NN` drift in L3 operator entries (037-040): `reciprocal` cites `:41`/`:40-45`, `assemble-diagonal` cites `:39`(×4)/`:38-43`, `jacobi-smoother` cites `:39`(×3)/`:38-43`, `elementwise_product` cites `:41`/`:53`/`:40-45`, `normalize` cites `:44`/`:45`/`:43-48`, `orthogonalize` cites `:47`. Live audit lines are `:45`(header)/`:46`((A)list)/`:47`((A)L1-gated)/`:48`((B))/`:49`((C)). Confirmed open in OQ ledger.
**Step 2c (directive-slug residual — `l2-floor-directive-slug-rename-book-chapter-body-residual`):** the old `l2-floor-under-l3-blas1-cohort` slug persists in 12 chapter bodies as stale §Status/provenance prose (NOT "renamed-from" provenance — genuine staleness; sample `L2/dot.md:20` "directive `l2-floor-under-l3-blas1-cohort`"):
```
$ grep -rl "l2-floor-under-l3-blas1-cohort" book/src/ | sort
book/src/L2/assemble-diagonal.md   book/src/L2/axpbypcz.md   book/src/L2/dot.md
book/src/L2/elementwise_product.md book/src/L2-L1/nrm2-leaf-identity.md
book/src/L2/nrm2.md   book/src/L2/reciprocal.md   book/src/L2/scal.md
book/src/L3/assemble-diagonal.md   book/src/L3/elementwise_product.md
book/src/L3-L2/nrm2-body-identity.md   book/src/L3/reciprocal.md
TOTAL: 12 files
```
**Step 3 (OQ-ledger RESOLVED-grep):**
```
$ grep -n "l3-index-audit-block-citation-drift" scaffolding/open-questions.md
937: ...Out of c043 D1's bounded (A)/(B)/(C) scope — surfaced (not enacted)... Trigger: a single lifter dispatch... route to a future cycle.   [OPEN — not RESOLVED/CLOSED]
```
The c043 integrator-signals (signals:51-55) explicitly route all three sub-targets to "cycle-044" as ONE bundled sweep. **Not stale; explicitly-routed-open.**
**Step 4 (structural-block check):** NONE — these are lifter re-anchors / citation re-pins / text renames on firm entries; no methodology gate. **ALL CHECKS PASS.**

### D2 — chebyshev-smoother L3 subsumption check (audit-first, observation-only)

**Step 1 (file existence — the candidate L3 entry is ABSENT, so the audit decides whether to author it):**
```
$ ls book/src/L3/chebyshev-smoother.md
ls: cannot access 'book/src/L3/chebyshev-smoother.md': No such file or directory
```
**Step 2 (the subsumption RISK — firm L3 `chebyshev` already covers the smoother):** `book/src/L3/chebyshev.md` (firmness: partial-obstruction) self-describes as "the **iteration-rotation** rendering of the **Chebyshev smoother**" (chebyshev.md:16-17), is "value-thread-isomorphic to the L1 `chebyshev-smoother`" (chebyshev.md:91,328), and already cites `palace/linalg/chebyshev.cpp` + `chebyshev.hpp` (chebyshev.md:196,307). The L1 home `book/src/L1/chebyshev-smoother.md` EXISTS. Strong prior: `chebyshev-smoother` L3 is **subsumed** → likely NO-LAND verdict.
**Step 3 (OQ-ledger):** `l3-substantive-cohort-from-c036-audit` (priorities.md:107) names `chebyshev-smoother` L3 as "preceded by a subsumption check against existing L3 `chebyshev`"; c040 integrator-signals (signals:162) "DO THIS FIRST before any `chebyshev-smoother` L3 harvest." Open, audit-gated — not discharged.
**Step 4 (structural-block check / framing):** This is an **audit-first** dispatch (cross-layer-cross-cutter), NOT a reflexive harvest — exactly the c036 D2 reframe precedent (the audit either confirms subsumption [NO-LAND] or carves out a distinct smoother-driver aspect that warrants a chapter). Observation-only; no artifact mutation. **ALL CHECKS PASS** (open by audit-gate; framing correct).

### D3 — orthogonalize L3>L2 substantive rotation theme

**Step 1 (file existence — the deliverable is ABSENT):**
```
$ ls book/src/L3-L2/orthogonalize-composition.md book/src/L3-L2/orthogonalize-body-identity.md
ls: cannot access '...orthogonalize-composition.md': No such file or directory
ls: cannot access '...orthogonalize-body-identity.md': No such file or directory
```
(Current L3-L2 themes on disk = 14: assemble-diagonal/axpby/axpbypcz/axpy/divfree-projector/dot/elementwise-product/jacobi-smoother/krylov-step/ksp-solve-outer-driver/normalize/nrm2/reciprocal/scal — `orthogonalize` is NOT among them; it is one of the 4 remaining `l3-l2-rotation-theme-coverage-gap` entries, the **substantive** one.)
**Step 2 (inputs firm — both LHS and RHS present):**
```
$ grep -m1 'firmness:' book/src/L3/orthogonalize.md  →  firmness: partial-obstruction   (LHS, c040, firm-body)
$ grep -A2 '## Status' book/src/L2/orthogonalize.md   →  `firm` — the composition is a `project ▷ subtract` pipeline... (RHS, c019, firm)
```
**Step 3 (OQ-ledger):** `l3-l2-rotation-theme-coverage-gap` (priorities.md:91, High fan-out, TOP-of-tier under `foundation_solidity`) explicitly names `orthogonalize` MGS-vs-CGS as a substantive theme to author. Not RESOLVED.
**Step 4 (structural-block check):** NONE — both endpoints firm; the rotation is substantive (the MGS sequential-obstruction vs CGS/CGS2-lift split is the iteration-rotation content). **ALL CHECKS PASS.**

### D4 — orthogonalize L3 verified_against audit

**Step 1+2 (the audit block is ABSENT on the firm L3 entry):**
```
$ grep -c 'verified_against' book/src/L3/orthogonalize.md
0
```
`book/src/L3/orthogonalize.md` is firm-body (partial-obstruction, c040) but carries ZERO `verified_against:` blocks.
**Step 3 (OQ-ledger / routing):** the c040 integrator-signals (signals:163) routed "the `orthogonalize` L3 `verified_against:` audit" to cycle-041 ("gated on the D1 entry being firm-on-disk"); the entry firmed c040 but the audit was never run (no `verified_against` on disk). Open, overdue.
**Step 4 (structural-block check):** NONE — append-only `verified_against:` evidence block against the MGS/CGS/CGS2 variant split; no body edits, status preserved. **ALL CHECKS PASS.**

**Negative-list cross-check:** none of D1–D4 touch `lu_solve`/`back_solve`/`ls-update-column`/`nleps_deflated_residual`/`nleps_deflated_solve`/`nleps_jacobian_action`/`nleps_eigenvalue_correction`. Clear.

## Dispatches

### D1 — `lifter` — consolidated cycle-044 cohort-completion sweep (THE LEAD; HIGH)
- **agent:** `lifter`
- **scope:** ONE bundled sweep, three sub-parts (all firm-entry re-anchors / citation re-pins / text renames — no substantive authoring):
  - **(i) Re-anchor the 4 NEW-floor L3 entries** `book/src/L3/{axpy,axpby,axpbypcz,normalize}.md` from "L3>L1 direct / no interposed L2 / no L3-L2 theme" → "L3>L2>L1 through the now-present adjacent L2 floor + the `<op>-body-identity` L3>L2 theme." Mirror the c043 D1 re-anchor of the c042 cohort EXACTLY (the `reciprocal`/`assemble-diagonal`/`jacobi-smoother`/`divfree-projector` re-anchors are the working template — see `book/src/L3/reciprocal.md:131` for the target prose shape). Sites per entry: the `lowers_to:` frontmatter, §"Downward to L1", §"Lowers to", and any related-entries line. For `axpy`/`axpby`/`axpbypcz` (fold-PARENTED arity members), cite the same-named L2 floor as a leaf-of-`linear_combination`; for `normalize` (FUSED-COMPOSITE, NO fold-parent), cite the L2 floor as consuming `nrm2`+`scal` (NO fold-parent) — per the OQ `l3-{axpy,axpby,axpbypcz,normalize}-lowers-to-staleness-after-l2-floor` (signals:51) + the converging-signal append (OQ ledger:953). Retain the cycle-012 non-adjacent-identity convention where it still applies (the new edges ARE per-adjacent-edge L3>L2; the in-line note now cites the composed `<op>-body-identity ∘ <op>-leaf-identity` edges).
  - **(ii) `l3-index-audit-block-citation-drift` index-wide re-pin** (OQ ledger:937): re-anchor every `L3/index.md:NN` citation in the L3 operator entries (`reciprocal`/`assemble-diagonal`/`jacobi-smoother`/`elementwise_product`/`normalize`/`orthogonalize`) against the LIVE audit-block lines (`:45` header / `:46` (A)-list / `:47` (A)-L1-gated / `:48` (B) / `:49` (C)), verifying each re-pin with `tools/citecheck --anchor` against on-disk `L3/index.md`. (The L3-L2 / L2-L1 cohort already cites the correct `:46` — confirm-not-touch.)
  - **(iii) Directive-slug residual** `l2-floor-directive-slug-rename-book-chapter-body-residual` (signals:52): rewrite the old `l2-floor-under-l3-blas1-cohort` → `l2-floor-under-l3-leaf-cohort` in the 12 chapter-body §Status/provenance-prose sites listed in the Step-2c grep above. **Text-only rename of stale prose** — do NOT touch any "renamed cycle-043 from X" historical-provenance sentences (those correctly document prior renames; the grep targets are the bare `directive \`l2-floor-under-l3-blas1-cohort\`` mentions, e.g. `L2/dot.md:20`, `L3/reciprocal.md:131`).
- **deps:** none
- **rationale:** serves the `l2-floor-under-l3-leaf-cohort` (cohort-completion debt) + `l3-l2-rotation-theme-coverage-gap` (citation hygiene on the freshly-doubled L3>L2 cohort) + the batch-12 slug-normalization realization. HIGH because it closes the layer-coherence backfill for the WHOLE final-slice floor cohort in one dispatch; the c043 integrator-signals explicitly recommend this exact bundle for c044. Scope-bounded: ~4 L3 entries × ~4 sites + ~6 index-drift re-pins + 12 one-line slug renames ≈ well under the ~62-block c043 D1 sweep — comfortably one dispatch. Plan-tag `cycle-044-floor-cohort-completion-lifter-sweep`.

### D2 — `cross-layer-cross-cutter` — chebyshev-smoother L3 subsumption check (audit-first; observation-only)
- **agent:** `cross-layer-cross-cutter`
- **scope:** Determine whether a standalone `book/src/L3/chebyshev-smoother.md` is warranted or is **subsumed** by the firm L3 `book/src/L3/chebyshev.md` (partial-obstruction). The firm L3 `chebyshev` already self-describes as "the iteration-rotation rendering of the **Chebyshev smoother**", value-thread-isomorphic to L1 `chebyshev-smoother`, citing `palace/linalg/chebyshev.cpp` + `chebyshev.hpp`. Localize the smoother surface via codemap (CONFIRMED anchors: `ChebyshevSmoother`/`ChebyshevSmoother1stKind` classes at `palace/linalg/chebyshev.hpp:23`/`:86`; template instantiations `chebyshev.cpp:295-299`). Compare the `ChebyshevSmoother` apply surface against what firm L3 `chebyshev` + L1 `chebyshev-smoother` already cover. Emit one of: **(A) SUBSUMED / NO-LAND** (the existing firm L3 `chebyshev` is the smoother's L3 home — record the subsumption verdict + close the `chebyshev-smoother` L3 candidacy in the OQ ledger; strong prior), or **(B) a distinct carved-out aspect** (e.g. a smoother-as-`B`-preconditioner driver shape not captured by the kernel-body L3 `chebyshev`) that warrants its own chapter — in which case scope the future harvest precisely. **Observation-only; NO artifact mutation** (per the c036 D2 audit-first precedent: a cross-layer-cross-cutter observation is the input to the land/no-land decision, not the chapter itself).
- **deps:** none
- **rationale:** serves `l3-substantive-cohort-from-c036-audit` ((B) cohort) under `foundation_solidity ≥ 1` (the L2 floor now exists). The c040 integrator-signals mandate this subsumption check FIRST before committing a harvester to a possibly-redundant chapter. Audit-first framing is the role-spec-required handling for a cohort-boundary candidate. Plan-tag `chebyshev-smoother-l3-subsumption-check`.

### D3 — `abstractor` — orthogonalize L3>L2 substantive rotation theme
- **agent:** `abstractor`
- **scope:** Author the missing **substantive** L3>L2 rotation theme for `orthogonalize` (slug `book/src/L3-L2/orthogonalize-composition.md` — substantive, NOT a `-body-identity` thin-identity; pick the slug that matches the substantive-rotation convention, coordinating with the existing L2>L1 `orthogonalize-composition-lowering`). Narrate FORWARD (L3→L2, high→low per the layers-defined-high→low invariant): how the firm L3 `orthogonalize` (partial-obstruction) lowers into the firm L2 `orthogonalize` (`project ▷ subtract` composition). The substantive content is the **variant-conditional iteration-rotation split**: MGS is a `sequential-obstruction` (the inner `j`-loop second `dot` feeds the next iteration — `orthog.hpp:46-52`), CGS/CGS2 lift cleanly; the runtime dispatch is `OrthogonalizeIteration` `iterative.cpp:313-323` (`switch(type)`, inspected once); GMRES site `iterative.cpp:630-632`, FGMRES site `iterative.cpp:809-811`; `test-orthog.cpp:99-120` witnesses the variants. (These anchors are pre-localized from the firm L3/L2 `orthogonalize` entries — read those two on-disk entries + the cited orthog.hpp/iterative.cpp ranges; the codemap localization loop is unnecessary.) **Dual-registration (NEW this cycle, per the c043 dual-registration friction):** the producer adds BOTH (a) its index-table ROW in `book/src/L3-L2/index.md` AND (b) its own §Vocabulary-cohort BULLET in that index — and does NOT touch the consolidated tally (the count-owner adds only the tally). Wire SUMMARY.md.
- **deps:** none (independent of D1/D2/D4 — distinct file region; see overlap analysis). Owns the `L3-L2/index.md` consolidated count this cycle (14→15 firm L3>L2; sole tally-owner since it is the only count-moving dispatch into that index).
- **rationale:** serves `l3-l2-rotation-theme-coverage-gap` (TOP-of-tier High fan-out under `foundation_solidity`): closes the FIRST of the 4 remaining substantive L3>L2 entries (the iteration-rotation, L3's defining content). Substantive (not thin-identity) — the MGS/CGS rotation carries real obstruction analysis. Plan-tag `l3-l2-rotation-theme-coverage-gap` (orthogonalize substantive slice).

### D4 — `lowering-verifier` — orthogonalize L3 verified_against audit
- **agent:** `lowering-verifier`
- **scope:** Append the machine-readable `verified_against:` evidence block to firm `book/src/L3/orthogonalize.md` (currently 0 blocks). Audit the per-citation `verdict`/`audited_at` against the MGS/CGS/CGS2 variant split (the firm-body entry's existing anchors: `orthog.hpp:18-23`/`:22`/`:46-52`/`:62-64`, `iterative.cpp:313-323`/`:630-632`/`:809-811`, `test-orthog.cpp:99-120`/`:123`/`:154-159`/`:234`). Confirm the variant-conditional obstruction claim (MGS sequential / CGS-CGS2 lift) is supported per-line; NO body edits, status `partial-obstruction` preserved. The deferred-since-c040 follow-up.
- **deps:** none (append-only to `L3/orthogonalize.md`; that file is also a citation-re-pin target of D1-(ii), see overlap analysis — D4 appends a frontmatter/footer `verified_against:` block, D1 re-pins an inline `L3/index.md:47` citation; distinct regions, but sequenced to be safe).
- **rationale:** serves the audit/per-line-evidence track (firms the (B)-cohort confidence on the `orthogonalize` L3 entry). LOW fan-out but overdue and cheap. Plan-tag `orthogonalize-l3-verified-against-audit`.

## Overlap analysis

Pairwise (two dispatches OVERLAP iff they modify the same operator entry / rewrite the same theme body / one names operators the other proposes):

- **D1 × D2:** NO overlap. D1 mutates firm L3 operator entries + L3/index citations + L2/L3 chapter slug-prose; D2 is observation-only (no artifact mutation). D2 reads `L3/chebyshev.md` (which D1 does NOT touch). PARALLEL.
- **D1 × D3:** NO overlap at the operational level. D1's index work is on **`L3/index.md`** self-cites + L3-operator-entry citations TO `L3/index.md` (the audit-block drift, confirmed confined to L3 operator entries per OQ:937). D3 adds a NEW theme file `L3-L2/orthogonalize-composition.md` + a ROW + a §Vocabulary bullet to **`L3-L2/index.md`** (a DIFFERENT index file). D1 explicitly does NOT touch the `L3-L2/index.md` consolidated count (the OQ scopes the drift to `L3/index.md:NN` citations; "the L3-L2/L2-L1 cohort already cites the correct `:46`" — confirm-not-touch). Distinct index files, distinct theme files. PARALLEL.
- **D1 × D4:** **Shared file `book/src/L3/orthogonalize.md`** — D1-(ii) re-pins an inline `L3/index.md:47`→`:47`(live) citation in `orthogonalize.md`; D4 appends a `verified_against:` block to `orthogonalize.md`. These are distinct regions (inline body citation vs appended evidence block), so they are *technically* non-conflicting — but they are edits to the SAME FILE, which the role-spec treats as genuinely overlapping (same operator entry). **SEQUENTIAL: D1 before D4** (D1 lands the citation re-pin; D4 appends to the re-pinned file). Conservative-sequentialize here because it is a real same-file edit, not a distinct-dep-map-row case.
- **D2 × D3:** NO overlap. D2 observation-only on the chebyshev surface; D3 authors the orthogonalize theme. PARALLEL.
- **D2 × D4:** NO overlap (D2 observation-only; D4 appends to `L3/orthogonalize.md`). PARALLEL.
- **D3 × D4:** NO overlap. D3 creates `L3-L2/orthogonalize-composition.md` + touches `L3-L2/index.md`; D4 appends to `L3/orthogonalize.md`. Distinct files. (Both concern the `orthogonalize` operator conceptually — D3's new theme could be cross-referenced from D4's audit — but D4 audits the EXISTING L3 entry's anchors, which do not depend on D3's new theme existing; forward-references stay plain-text per convention. They could be sequenced D3→D4 to let D4 cite the new theme as a live link, but that is a forward-reference nicety, not a conflict.) PARALLEL — but see Sequencing for the D3-before-D4 forward-reference ordering preference.

Count-ownership (cycle-039 meta-phase convention): the only count-moving index this cycle is `L3-L2/index.md` (14→15 firm), touched by exactly ONE dispatch (D3). D3 is therefore the SOLE consolidated-tally owner by construction — no partition needed (no co-dispatched agent lands into `L3-L2/index.md`). D1's index work is citation-drift re-pins on `L3/index.md` (no consolidated-count change — the L3 firm count is unchanged at 15 this cycle). Stated explicitly in D3's scope.

## Sequencing schedule

Two waves (the only true ordering constraint is D1→D4 same-file; D3-before-D4 is a soft forward-reference preference):

- **Wave 1 (parallel):** D1 (lifter sweep), D2 (chebyshev-smoother subsumption check), D3 (orthogonalize L3>L2 substantive theme).
- **Wave 2 (after D1 and D3 reports land):** D4 (orthogonalize verified_against audit) — SEQUENTIAL after D1 (same-file `L3/orthogonalize.md` edit) and after D3 (so D4 may cite the new `orthogonalize-composition` L3>L2 theme as a live link rather than plain-text; if D3 slips, D4 falls back to plain-text forward-reference per convention).

The book is NOT rebuilt between waves; there is exactly ONE `integrator-finalize` at cycle end (the waves order *dispatches* by same-file / forward-reference dependency, not multiple finalizes). Pipeline: planner → D1/D2/D3/D4 (2 waves) → 4 critics → repairers → `integrator-per-report` ×N (serial) → ONE `integrator-finalize`.

## priorities.md updates this cycle

I will mark the c044 picks against the existing plan items (the active head is reshaped via these annotations rather than a wholesale rewrite, since the batch-13 meta-phase owns the next full reshape after c045):
- `l2-floor-under-l3-leaf-cohort` (High) — the cohort-completion debt (4 NEW-floor L3 re-anchors) is dispatched as c044 D1.
- `l3-l2-rotation-theme-coverage-gap` (High) — the FIRST substantive entry (`orthogonalize`) dispatched c044 D3; index-citation hygiene folded into D1.
- `l3-substantive-cohort-from-c036-audit` (Medium) — `chebyshev-smoother` subsumption check dispatched c044 D2 (audit-first, likely NO-LAND).
- New caveat appended: the `orthogonalize` L3 `verified_against:` audit (c040-deferred) dispatched c044 D4.

## Open questions / caveats

- **`chebyshev-smoother` L3 strong-prior NO-LAND.** The firm L3 `chebyshev` (partial-obstruction) already self-describes as the iteration-rotation rendering of the Chebyshev *smoother* and is value-thread-isomorphic to L1 `chebyshev-smoother`. I expect D2 to return SUBSUMED. I have framed D2 as observation-only so a NO-LAND verdict is cheap and clean; if it instead carves out a distinct smoother-driver aspect, that becomes a c045 harvest candidate. Flagging so the integrator/meta-phase is not surprised by a zero-new-chapter D2.
- **Cohort-count reconciliation for `chebyshev` (12-of-13 + naming-exception) is meta-phase-owned** (OQ `chebyshev-floor-cohort-count-reconciliation`, routed to batch-13 meta-phase per signals:49). I did NOT dispatch any reconciliation this cycle — it is correctly meta-phase territory (the denominator renumber + the `normalize` fused-composite sub-shape classification, OQ `normalize-fused-composite-no-fold-parent-sub-shape`). Noted for the batch-13 meta-phase (fires after c045).
- **Dual-registration convention codification is meta-phase-owned** (c043 dual-registration friction, signals:64). I have applied the convention *inline* in D3's scope ("producer adds BOTH the table row AND its own cohort bullet; the count-owner adds only the consolidated tally") as the c043 integrator-signals direct, but the standing CODIFICATION (a cycle-planner dispatch-design note + an abstractor/harvester role-spec note) is for the batch-13 meta-phase. Since this is a fresh-intake friction not yet in a role-spec, I surface it here so the meta-phase catches it at batch end (per the cadence note: the friction-ledger entry may not land until the batch boundary). D3 is the only theme producer this cycle (single producer), so the dual-registration risk is low this cycle regardless.
- **Slate is 4 (under the 12 cap).** I held the cycle to the two clean frontier moves (cohort-completion debt + the substantive L3↔L2 resume) rather than padding. The `concepts/axpby.md` page (OQ `concepts-axpby-page-unauthored`, non-blocking, signals:57) and the c040 `L4/orthogonalize` monad-surface sketch (deferred-contingent) are eligible LOW-fan-out fillers but were not worth a dispatch slot against the cap this cycle; they remain available for c045.
