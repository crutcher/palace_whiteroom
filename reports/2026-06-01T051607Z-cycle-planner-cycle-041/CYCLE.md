---
agent: cycle-planner
invoked_at: 2026-06-01T051607Z
scope: cycle-041 dispatch plan
status: pending
---

# Cycle 041 dispatch plan

## Goals selected this cycle

Cycle-041 is the **SECOND primary cycle of meta-batch-12** (cycles 040/041/042; meta fires after 042). It executes the **first slice of the foundation-first L2-floor build** mandated by the USER DIRECTIVE 2026-05-31 (uniform pull-up L0→L4; foundation-solidity is a ranking weight). The lead frontier is the two NEW High-fan-out foundation items at the top of `priorities.md` §High fan-out: `l2-floor-under-l3-blas1-cohort` + `l3-l2-rotation-theme-coverage-gap`. This cycle builds the **L2 floor under the three most-reused BLAS-1 leaves** — `dot`, `nrm2`, `scal` — and the **adjacent thin-identity themes** (L2>L1 + L3>L2) for each, so that each of those three L3 entries rests on a present, adjacent L2 floor (per "Identity-lowerings still require both L levels"), replacing the current cycle-012 non-adjacent inline-identity skip directly from L3 to L1. The further-L3-width track (`l3-substantive-cohort-from-c036-audit`: `chebyshev-smoother`/`apply_nonlinear_pencil`) is DEMOTED (`foundation_solidity < 1`) and is NOT led this cycle.

**Lead trio rationale (why dot/nrm2/scal and not axpy this cycle):** all three are firm L1 leaves with their OWN firm L1>L0 mutation-rotation themes (the audited evidence basis the L2 floor entry inherits) AND firm L3 entries (the floor goes under a present consumer). `axpy` is deferred to a later foundation cycle because its L1>L0 lowering lives in the `axpby`-family theme (`axpby-mutation-rotation` / `axpbypcz-mutation-rotation`), not a standalone `axpy-mutation-rotation` — the axpy/axpby/axpbypcz arity-family L2 floor wants to be planned as one coherent unit (it maps onto the existing firm L2 `linear_combination` fold), and is best taken after the leaf-trio pattern is validated. Three operators keeps the cycle a clean, auditable first slice; the remaining 10 L2-floor entries follow in cycles 042+.

## Dispatches

Per-operator unit = **1 harvester (L2 floor entry) + 1 abstractor (the two adjacent thin-identity themes L2>L1 and L3>L2 for that operator)**. Three operators → 6 producer dispatches. Plus **1 layer-intro-author** as the sole count-owner for the three shared consolidated indices (`L2/index.md`, `L2-L1/index.md`, `L3-L2/index.md`). Total: **7 dispatches.**

1. **(`harvester`)** — **scope: L2 floor entry `book/src/L2/dot.md`** (fusion-rotation rendering of the BLAS-1 inner-product leaf at L2; identity-in-form to firm L1 [`dot`](../L1/dot.md)). **Source of truth:** the firm L1 entry `book/src/L1/dot.md` (authoritative on every Palace-surface fact + the complete L0 evidence list) + its firm L1>L0 theme `book/src/L1-L0/dot-mutation-rotation.md`. Canonical L0 anchors (from the firm L1 entry, on-disk-verified at dispatch per the codemap-is-localization-only rule): `palace/linalg/vector.hpp:110-113,242-244,247-253`, `vector.cpp:263-267,269-274,665-672,674-685`. **Framing note (load-bearing for the harvester):** this is the **same-named L2 leaf entry**, distinct from the existing firm L2 fold-parent [`inner_product`](../L2/inner_product.md) (which folds `dot`/`tdot`/`bilinear-form`). The L2 `dot` floor entry is the leaf rendered at the fusion layer; `inner_product` is its generalizing fold sibling (cite it as the fold-parent, do NOT merge — the codomain/fold distinction is load-bearing per the L2/index §"Fold-cohort boundary" note). Per the directive's per-operator judgment, where the L2 form is truly identity to L1 AND adds zero vocabulary the harvester may land a **thin identity L2 entry** (floor *presence*, not bulk). **D7 owns the L2/index consolidated tally + cohort bullets** — this harvester appends ONLY its own dep-map row + `## Status` body + SUMMARY registration; it does NOT touch the §Vocabulary-cohort "Firm at L2" running list count (defer to D7). **deps: none.**

2. **(`harvester`)** — **scope: L2 floor entry `book/src/L2/nrm2.md`** (fusion-rotation rendering of the Euclidean-norm leaf at L2; identity-in-form to firm L1 [`nrm2`](../L1/nrm2.md)). **Source of truth:** firm `book/src/L1/nrm2.md` + firm `book/src/L1-L0/nrm2-mutation-rotation.md`. Canonical L0 anchors: `palace/linalg/vector.hpp:255-260,262-270`. **Framing note:** `nrm2 = √ ∘ inner_product` at `y=x` (a *consumer* of `inner_product`, NOT an instance — per the L2/index §"Fold-cohort boundary"); the L2 `nrm2` floor entry renders the norm leaf at L2 and cites `inner_product` as the consumed fold, not a parent. Thin-identity L2 entry acceptable (floor presence). **D7 owns the L2/index tally** — append ONLY own dep-map row + body + SUMMARY; defer the count. **deps: none.**

3. **(`harvester`)** — **scope: L2 floor entry `book/src/L2/scal.md`** (fusion-rotation rendering of the scalar-vector-multiply leaf at L2; identity-in-form to firm L1 [`scal`](../L1/scal.md)). **Source of truth:** firm `book/src/L1/scal.md` + firm `book/src/L1-L0/scal-mutation-rotation.md`. Canonical L0 anchors: `palace/linalg/vector.hpp:98-99,262-270`, `vector.cpp:203-227`. **Framing note:** `scal` is the arity-1 member of the firm L2 `linear_combination` fold (`scal`/`axpy`/`axpby`/`axpbypcz`); cite `linear_combination` as the fold-parent (do NOT merge — the same fold-cohort boundary). Thin-identity L2 entry acceptable. **D7 owns the L2/index tally** — append ONLY own dep-map row + body + SUMMARY; defer the count. **deps: none.**

4. **(`abstractor`)** — **scope: the two adjacent thin-identity themes for `dot` — `book/src/L2-L1/dot-fold-specialization.md` (L2>L1) + `book/src/L3-L2/dot-body-identity.md` (L3>L2).** Both are identity-in-form (BLAS-1 leaf): the L2>L1 theme narrates forward how the L2 `dot` floor form lowers into the L1 `dot` primitive (identity-in-form on the reduction signature; the rotation work is the surrounding context, not the leaf); the L3>L2 theme narrates forward how the L3 `dot` whole-tensor reduction lowers into the L2 `dot` fusion form (identity-in-form — no per-element loop exposed at either layer, per the existing `krylov-step-body-identity` §"Applicability conditions" point-3 classification of `dot` as L3-native). **Final slug names to be confirmed at dispatch against the sibling-naming convention** (existing L2>L1 themes use `-fold-specialization` / `-composition-lowering`; existing L3>L2 themes use `-body-identity` / `-outer-driver`). **deps: 1** (references D1's `book/src/L2/dot.md` for the live L2 anchor; sequence so the per-report integrator can wire a live link rather than plain-text-defer). **D7 owns the L2-L1/index + L3-L2/index theme-list tallies** — this abstractor appends ONLY its two theme rows + bodies + SUMMARY registrations; defer the counts.

5. **(`abstractor`)** — **scope: the two adjacent thin-identity themes for `nrm2` — `book/src/L2-L1/nrm2-fold-specialization.md` (L2>L1) + `book/src/L3-L2/nrm2-body-identity.md` (L3>L2).** Same identity-in-form shape as D4 (the norm leaf carries the `√ ∘ inner_product`-at-`y=x` framing through both themes, narrated forward L_{n+1}→L_n). Slug names confirmed at dispatch. **deps: 2** (references D2's `book/src/L2/nrm2.md`). **D7 owns the index tallies** — append ONLY own theme rows + bodies + SUMMARY; defer.

6. **(`abstractor`)** — **scope: the two adjacent thin-identity themes for `scal` — `book/src/L2-L1/scal-fold-specialization.md` (L2>L1) + `book/src/L3-L2/scal-body-identity.md` (L3>L2).** Same identity-in-form shape (the scalar-vector-multiply leaf; cite `linear_combination` as the arity-family fold-parent). Slug names confirmed at dispatch. **deps: 3** (references D3's `book/src/L2/scal.md`). **D7 owns the index tallies** — append ONLY own theme rows + bodies + SUMMARY; defer.

7. **(`layer-intro-author`)** — **scope: SOLE count-owner this cycle for the three shared consolidated indices.** Refresh (a) `book/src/L2/index.md` §Vocabulary-cohort "Firm at L2" list + §Working-Notes narrative to fold in the three NEW L2 floor leaves (`dot`/`nrm2`/`scal`) AND author the consolidated firm-count narrative — the L2 firm cohort moves 9 → 12 (three thin-identity BLAS-1 floor leaves); explicitly note these are the **first L2-floor-under-L3 entries** landed under the 2026-05-31 foundation-first directive, distinct from the fold-parents `inner_product`/`linear_combination`. (b) `book/src/L2-L1/index.md` §Theme-list narrative + count for the three NEW L2>L1 thin-identity themes (L2>L1 firm 7 → 10). (c) `book/src/L3-L2/index.md` §Theme-list narrative + count for the three NEW L3>L2 thin-identity themes (L3>L2 firm 2 → 5 — and note this begins closing the `l3-l2-rotation-theme-coverage-gap`, from 2-of-18 toward 5-of-18). **Count-ownership convention (cycle-039 meta, batch-11):** D7 is the SOLE writer of every consolidated running-count / cohort tally in all three indices; D1–D6 append only their own non-aggregate rows (dep-map rows / theme rows / SUMMARY registrations / `## Status` bodies) and DEFER every tally to D7. **deps: 1, 2, 3, 4, 5, 6** (must run after all six producer landings so the consolidated counts reflect the full cohort; wave-3).

## Overlap analysis

Pairwise (the dispatch plan IS the overlap reasoning):

- **D1 × D2 × D3** (the three L2 harvesters): each creates a **distinct new file** (`L2/dot.md` / `L2/nrm2.md` / `L2/scal.md`) and appends a **distinct dep-map row** to `L2/index.md` + a **distinct SUMMARY line**. Distinct rows are non-overlapping (parallel-safe per the cycle-planner §Discipline "distinct dep-map rows → parallel" bullet). The ONLY shared-mutable-derived-value is the `L2/index.md` §Vocabulary-cohort consolidated firm-count — owned solely by D7 (count-ownership convention); D1/D2/D3 are instructed to defer it. → **PARALLEL.**
- **D4 × D5 × D6** (the three abstractors): each creates **two distinct new theme files** (one L2>L1, one L3>L2) and appends distinct rows to `L2-L1/index.md` + `L3-L2/index.md` + SUMMARY. No two abstractors touch the same theme body or the same row. Shared consolidated theme-counts owned by D7. → **PARALLEL with each other.**
- **D4 → D1, D5 → D2, D6 → D3** (each abstractor depends on its operator's L2 harvester): the L2>L1 theme references `book/src/L2/<op>.md` as its live L2 anchor, and that file does not exist until the harvester lands. **Forward-reference ordering, not a body conflict** — sequence the abstractor in a later wave so the per-report integrator wires a live link (vs. plain-text-defer). This is dispatch ORDERING, not a write-overlap.
- **D1 × D4, D2 × D5, D3 × D6** (harvester vs its operator's abstractor): the harvester writes the L2 operator entry; the abstractor writes the adjacent themes (different files). No shared file region except the indices (owned by D7). The dependency is forward-reference only (handled by wave ordering). → not a write-overlap.
- **D7 × everyone:** D7 is the SOLE writer of every consolidated tally in all three indices; D1–D6 write only their own non-aggregate rows. By construction (count-ownership partition) there is **no blind-parallel count divergence** — the c037/c038 failure mode (three parallel harvesters writing 12/13/12) is structurally avoided exactly as it was in c039 (D3 sole-owner precedent). D7 must run AFTER all six producers land so its counts are correct → wave-3.
- **No operator-name collision:** the three L2 floor slugs (`dot`/`nrm2`/`scal`) are leaf names already firm at L1 and L3; no dispatch proposes an operator another dispatch also names as its primary deliverable. The fold-parents (`inner_product`/`linear_combination`) are cited-not-modified by the harvesters.

No genuine write-overlap (same operator entry rewrite OR same theme body rewrite) exists between any two dispatches. All within-wave pairs are PARALLEL.

## Sequencing schedule

Three waves, ordered by forward-reference dependency (NOT multiple finalizes — there is exactly ONE `integrator-finalize` at cycle end; waves order dispatches so the per-report integrator can wire live links):

- **Wave 1 (parallel):** D1, D2, D3 — the three L2 floor harvesters. No deps; each lands a distinct `L2/<op>.md` + distinct index row.
- **Wave 2 (parallel):** D4, D5, D6 — the three abstractors (each authors its operator's L2>L1 + L3>L2 thin-identity themes). Each depends only on its own operator's wave-1 harvester (D4→D1, D5→D2, D6→D3); all three run in parallel within the wave since they touch distinct theme files.
- **Wave 3 (single):** D7 — the layer-intro-author sole count-owner. Runs after all six producers so the three indices' consolidated tallies (L2 9→12, L2>L1 7→10, L3>L2 2→5) reflect the complete cohort.

Pipeline reminder: planner → 7 dispatches (3 waves) → 7 critics → repairers (as needed) → `integrator-per-report` ×7 (serial) → ONE `integrator-finalize` (rebuild book + commit + push + housekeeping). The book is NOT rebuilt between waves.

## Deliverable-presence verification

Per the MANDATORY paste-inline-evidence pre-dispatch deliverable-presence check (cycle-036 meta strengthening; friction-ledger `cycle-planner-stale-priorities-line-recruitment`). Every named-artifact-slug scope below carries the LITERAL pasted command output proving the proposed deliverable is genuinely ABSENT and the upstream parents are firm. STOP-PROPOSING NEGATIVE LIST consulted (`lu_solve`/`back_solve`/`ls-update-column`/4 NLEPS atoms) — none of `dot`/`nrm2`/`scal` is on it.

### D1 — `book/src/L2/dot.md` (L2 floor entry)
1. **File existence (expect ABSENT):**
   ```
   $ for f in dot axpy nrm2 scal; do if [ -e "book/src/L2/$f.md" ]; then echo "PRESENT: book/src/L2/$f.md"; else echo "ABSENT: book/src/L2/$f.md"; fi; done
   ABSENT: book/src/L2/dot.md
   ABSENT: book/src/L2/axpy.md
   ABSENT: book/src/L2/nrm2.md
   ABSENT: book/src/L2/scal.md
   ```
   → `book/src/L2/dot.md` ABSENT. Genuinely open by construction (no prior L2-floor-entry history for this slug).
2. **Maturity / upstream-firmness check** — L1 parent firm + L3 consumer firm:
   ```
   $ awk '/^## Status/{getline; while($0 ~ /^[[:space:]]*$/){getline}; print; exit}' book/src/L1/dot.md
   `firm` — signatures are canonical, evidence is direct from the Palace source, and the algebraic laws listed are standard sesquilinear/bilinear facts modulo the explicitly-recorded floating-point caveats.
   $ grep -m1 '^firmness:' book/src/L3/dot.md
   firmness: firm
   $ awk '/^## Status/{getline; while($0 ~ /^[[:space:]]*$/){getline}; print; exit}' book/src/L1-L0/dot-mutation-rotation.md
   `firm` — the rewrite is the structural expansion of the L1 `dot` reduction into the L0
   ```
   → L1 `dot` firm, L3 `dot` firm, L1>L0 `dot-mutation-rotation` firm. The L2 floor entry's evidence basis is present and firm.
3. **OQ-ledger RESOLVED/CLOSED grep:**
   ```
   $ grep -niE "L2/(dot)" scaffolding/open-questions.md   # → no L2/dot resolution
   (no matches)
   ```
   The `l2.*dot` grep hits in the ledger are about the L2 `inner_product` FOLD + the subsumption-chain — NONE disposes an L2 `dot` FLOOR entry. No stale-closure.
4. **Structural-block check:** none. The directive 2026-05-31 ("Uniform pull-up L0→L4; foundation-solidity is a ranking weight") + the High-fan-out backlog item `l2-floor-under-l3-blas1-cohort` explicitly mandate this build; "Identity-lowerings still require both L levels" licenses the thin-identity floor entry. The cycle-012 "non-adjacent inline-identity" convention is **tilted toward present-floor coherence** by the 2026-05-31 directive (CLAUDE.md §Methodology invariants, the new bullet). NOT on the STOP-PROPOSING list. → RECRUIT.

### D2 — `book/src/L2/nrm2.md` (L2 floor entry)
1. **File existence:** `ABSENT: book/src/L2/nrm2.md` (pasted above, same `for`-loop). Genuinely open.
2. **Upstream firmness:**
   ```
   $ awk '/^## Status/{getline; while($0 ~ /^[[:space:]]*$/){getline}; print; exit}' book/src/L1/nrm2.md
   `firm` — signature is canonical and tightly constrained by the one-line L0 definition, evidence is direct from `palace/linalg/vector.hpp:255-260` ...
   $ grep -m1 '^firmness:' book/src/L3/nrm2.md
   firmness: firm
   $ awk '/^## Status/{getline; ...; exit}' book/src/L1-L0/nrm2-mutation-rotation.md
   `firm` — the rewrite is the structural expansion of the one-line L0 `Norml2` definition,
   ```
   → L1 firm, L3 firm, L1>L0 firm.
3. **OQ-ledger:** no `L2/nrm2` resolution (the `l2.*nrm2` grep hit is the `assemble-diagonal` audit-followup OQ that merely names nrm2 as a sibling-audit pairing — not an L2-floor disposition). No stale-closure.
4. **Structural-block:** none (same directive basis as D1). NOT on STOP-PROPOSING list. → RECRUIT.

### D3 — `book/src/L2/scal.md` (L2 floor entry)
1. **File existence:** `ABSENT: book/src/L2/scal.md` (pasted above). Genuinely open.
2. **Upstream firmness:**
   ```
   $ awk '/^## Status/{getline; ...; exit}' book/src/L1/scal.md
   `firm` — signature is canonical (matches BLAS-1 `dscal` / `zscal` ...) ...
   $ grep -m1 '^firmness:' book/src/L3/scal.md
   firmness: firm
   $ awk '/^## Status/{getline; ...; exit}' book/src/L1-L0/scal-mutation-rotation.md
   `firm` — the rewrite is a single structural buffer re-bind with one transparent
   ```
   → L1 firm, L3 firm, L1>L0 firm.
3. **OQ-ledger:** no `L2/scal` resolution (the `l2.*scal` grep hits are the `subsumption-chain-cross-cutting-concept` resolution — `scal≺axpy≺axpby≺axpbypcz` in `linear_combination` — and the `assemble-diagonal` sibling-pairing; neither disposes an L2 `scal` FLOOR entry). No stale-closure.
4. **Structural-block:** none. NOT on STOP-PROPOSING list. → RECRUIT.

### D4 / D5 / D6 — the L2>L1 + L3>L2 thin-identity themes
1. **File existence (expect ABSENT for every candidate slug):**
   ```
   $ for f in dot nrm2 scal; do for cand in "$f-fold-specialization" "$f-composition-lowering" "$f-fusion"; do [ -e "book/src/L2-L1/$cand.md" ] && echo "PRESENT: L2-L1/$cand.md"; done; done
   (no output → all ABSENT)
   $ ls book/src/L3-L2/
   index.md  krylov-step-body-identity.md  ksp-solve-outer-driver.md
   ```
   → No `dot`/`nrm2`/`scal` L2>L1 theme exists; the only two L3>L2 themes are `krylov-step-body-identity` + `ksp-solve-outer-driver` (the 2-of-18 the gap names). Every proposed theme slug is ABSENT. Open by construction.
2. **Upstream firmness:** the L2 floor entry each theme references is being created in wave-1 (D1/D2/D3, verified-open above); the L1 leaf + L3 entry each theme connects are firm (pasted in D1–D3). The theme's forward L2 anchor lands earlier in-cycle (wave-1 → wave-2 ordering) so the per-report integrator wires a live link.
3. **OQ-ledger:** the `l3-l2-rotation-theme-coverage-gap` item is OPEN (a High-fan-out plan item, NOT resolved) — these themes are exactly its mandated deliverable. No CLOSED disposition for any `<op>-fold-specialization` / `<op>-body-identity` slug.
4. **Structural-block:** none — thin-identity L3>L2 themes are explicitly the directive's mandate (`l3-l2-rotation-theme-coverage-gap`, "thin-identity where it is identity-in-form (the BLAS-1 cohort)"). → RECRUIT (sequenced wave-2 behind their operators' wave-1 harvesters).

### D7 — `book/src/L2/index.md` + `L2-L1/index.md` + `L3-L2/index.md` consolidated-count refresh
- **Open by construction (index refresh):** D7's deliverable is the consolidated-tally + narrative refresh that MUST follow the six wave-1/wave-2 landings (the counts move only because D1–D6 land). It is not a re-proposal of already-landed work — it is the count-ownership write that the convention assigns to exactly one owner. The on-disk current counts (L2 firm 9, L2>L1 firm 7, L3>L2 firm 2, from `counts_after` of the c040 cycle-record and the index dep-maps read this cycle) are the baseline D7 advances to 12 / 10 / 5. → RECRUIT (wave-3 sole count-owner).

All seven dispatches PASS the deliverable-presence check with pasted inline evidence; none is on the STOP-PROPOSING NEGATIVE LIST; framing is correct (foundation-first L2-floor build, thin-identity where identity-in-form, fold-parent cited-not-merged).

## priorities.md updates made this cycle

I marked the three lead-trio picks as DISPATCHED on the `l2-floor-under-l3-blas1-cohort` + `l3-l2-rotation-theme-coverage-gap` High-fan-out items, and recorded the cycle-041 active-head reshape under the USER DIRECTIVE 2026-05-31 banner (the cycle-040 body was historical). I did NOT do batch-level intake migration/compaction (meta-phase's standing pass). See `scaffolding/priorities.md` §Now (active) cycle-041 block.

## Open questions / caveats

- **`axpy`/`axpby`/`axpbypcz` L2-floor unit framing (for a cycle-042+ planner).** I deferred the `axpy` leaf this cycle because its L1>L0 lowering lives in the `axpby`-family theme, and the arity-family (`scal`/`axpy`/`axpby`/`axpbypcz`) maps onto the existing firm L2 `linear_combination` fold. A future foundation cycle should decide whether the four arity-family members get four thin same-named L2 floor entries (`L2/axpy.md` etc., consistent with the leaf-floor pattern this cycle establishes) OR whether `linear_combination` already discharges the floor for the family (in which case the L3 `axpy`/`axpby`/`axpbypcz` entries re-anchor their non-adjacent inline-identity to the `linear_combination` fold-parent rather than skipping straight to L1). The same question applies to `dot`/`nrm2` vs `inner_product` — this cycle resolves it in the "build the same-named leaf floor AND cite the fold-parent" direction (per the directive's "same-named L2 parent" framing); the meta-phase (post-c042) should ratify that this is the intended reading of `l2-floor-under-l3-blas1-cohort`, since it produces two L2 entries for the same leaf surface (the leaf floor + the generalizing fold). Noted here for the batch-12 meta-phase.
- **Thin-identity vs full-decomposition judgment is delegated to the harvester per-operator.** The directive says "where the L2 form is truly identity to L1 AND adds zero vocabulary, the harvester may land a thin identity L2 entry rather than a full decomposition." For `dot`/`nrm2`/`scal` I expect thin-identity (these are atomic BLAS-1 leaves with no fusion to unfold). If a harvester finds genuine fusion-rotation content to unfold (e.g. a reduction-tree / collective-topology absorption that is more than identity), it should author the fuller L2 entry and flag the surplus — that is useful foundation signal, not scope-creep.
- **L3>L2 theme-slug naming convention.** The existing two L3>L2 themes use `-body-identity` (`krylov-step-body-identity`) and `-outer-driver` (`ksp-solve-outer-driver`). I proposed `<op>-body-identity` for the BLAS-1 leaves (consistent with the identity-in-form classification already in `krylov-step-body-identity` §"Applicability conditions" point-3, which lists `dot`/`nrm2`/`scal` among the seven L3-native-by-signature primitives). The abstractors should confirm the slug against the convention at dispatch and may prefer a cohort-shared phrasing; the per-report integrator wires SUMMARY + live links regardless.
- **Cadence note.** Cycle-041 is the SECOND of meta-batch-12 (040/041/042); the batch-12 meta-phase fires after c042. The foundation-first directive landed mid-batch (post-c040), so the friction-ledger / priorities I read are at most ~1 primary cycle stale on this directive — no staleness concern this cycle. The 10 remaining L2-floor entries (`axpy`/`axpby`/`axpbypcz`/`assemble-diagonal`/`jacobi-smoother`/`divfree-projector`/`elementwise_product`/`reciprocal`/`normalize`/`chebyshev`) + their L3>L2 themes carry forward to c042+ as the continuing High-fan-out foundation frontier.
