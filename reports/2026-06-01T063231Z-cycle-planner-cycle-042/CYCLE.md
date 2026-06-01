---
agent: cycle-planner
invoked_at: 2026-06-01T063231Z
scope: cycle-042 dispatch plan
status: pending
---

# Cycle 042 dispatch plan

## Goals selected this cycle

Continue the **foundation-first L2-floor build** (the 2026-05-31 `foundation_solidity` directive) but **steer around the leaf-vs-fold design fork** that cycle-041 surfaced and the batch-12 meta-phase (fires after THIS cycle) must adjudicate. Cycle-042 does **two** things: (1) **tees up the fork adjudication with real evidence** via a dedicated `same-layer-cross-cutter` audit of the leaf-vs-fold duality (does a same-named `L2/dot` leaf alongside the `inner_product` fold cause duplication explosion in adjacent layers, or is it a genuinely-distinct dual per "coalesce by use; duals OK if genuinely distinct"? what does the L3→L2→L1 chain look like under each reading?); and (2) **advances the fork-INDEPENDENT slice of the L2-floor cohort** — the 5 standalone members that have **NO fold-parent** (`reciprocal`/`elementwise_product` elementwise leaves; `assemble-diagonal`/`jacobi-smoother`/`divfree-projector` constructed-operator gates), whose floors are safe to build regardless of how the fork resolves. The fork-EXPOSED `axpy`/`axpby`/`axpbypcz` arity-family (which rides the `linear_combination` fold question, the SAME fork) is explicitly **HELD** for the meta-phase, avoiding rework-if-flipped.

**Why this shape and not "keep piling BLAS-1 leaf floors":** the cycle-041 carry-forward signal (`dot-l2-leaf-floor-vs-fold-only-design`, the LOAD-BEARING batch-12 meta-phase signal) governs the WHOLE 13-entry cohort. Continuing to build fork-contingent leaf-floor entries (`axpy` family) this cycle risks dissolving them if the meta-phase adopts fold-only. The 5 standalone members are provably outside that risk (see § Deliverable-presence verification: every one of them states in its firm L3 entry that it has "no interposed L2 entry and no `L3-L2`/`L3-L1` theme" and is NOT a fold member), so they are the correct foundation work to advance now while the fork is open.

## Dispatches

**D1 — `same-layer-cross-cutter` — leaf-vs-fold duality audit (FORK-EVIDENCE for the batch-12 meta-phase).**
- **scope:** Audit the L2 inner-product / linear-combination surface shape: does the cycle-041 **(b) same-named leaf-floor** reading (standalone `L2/dot`, `L2/scal` chapters cited-as-leaf-of-fold, NOT merged — landed c041 D1/D3) cause **duplication explosion in adjacent layers** (L2>L1 + L3>L2 themes per leaf AND per fold; dep-map row blow-up; reader having to reconcile leaf chapter vs fold chapter), or is the leaf a **genuinely-distinct dual** of the fold per the "coalesce by use; duals OK if genuinely distinct; not OK if they force duplication explosion in adjacent layers" methodology (CLAUDE.md §Process model + MEMORY multi-formulation)? Examine the concrete L3→L2→L1 chain under EACH reading for `dot` (leaf-floor: `L3/dot → L2/dot → L1/dot` + `dot-body-identity` + `dot-leaf-identity`; fold-only: `L3/dot → (no L2 dot) → L1/dot` with the L3>L2 identity re-homed as a non-adjacent in-line note + the fold `inner_product` carrying the only L2 surface). Tabulate the adjacent-layer chapter/theme/dep-map count delta between the two readings. Surface the wave-1 D1-vs-D2 contradiction (`reports/2026-06-01T051607Z-cycle-041-harvester-L2-dot` leaf-floor vs `...-harvester-L2-nrm2` fold-only) as the framing. **Deliverable:** a `same-layer-cross-cutter` observation CYCLE.md with a recommendation (leaf-floor / fold-only / hybrid) + the duplication-vs-distinctness verdict + the count delta, explicitly framed as **input to the batch-12 meta-phase adjudication** (the meta-phase decides; this dispatch supplies evidence). Do NOT mutate any artifact; this is an observation report. **Localization:** `book/src/L2/{dot,nrm2,scal,inner_product,linear_combination}.md`, `book/src/L2-L1/{dot-leaf-identity,nrm2-fold-specialization,scal-fold-specialization,inner-product-fold-specialization,linear-combination-fold-specialization}.md`, `book/src/L3-L2/{dot,nrm2,scal}-body-identity.md`, `book/src/L3/{dot,nrm2,scal}.md`, the two cited c041 reports, OQs `dot-l2-leaf-floor-vs-fold-only-design` / `l2-no-dot-leaf-floor-but-fold-is-the-l2-surface`.
- **deps:** none.
- **rationale:** The headline cycle-041 carry-forward signal. The meta-phase fires after this cycle and must adjudicate the fork that governs the entire BLAS-1 L2-floor cohort + the `axpy`-family framing; a planned evidence dispatch (count delta + duplication-vs-distinctness verdict) is worth far more to that adjudication than another fork-contingent leaf-floor that might get reworked. Serves `dot-l2-leaf-floor-vs-fold-only-design` (the OQ) + the `l2-floor-under-l3-blas1-cohort` cohort design.

**D2 — `harvester` — `book/src/L2/reciprocal.md` (fork-INDEPENDENT L2 floor; elementwise leaf, NO fold-parent).**
- **scope:** L2 fusion-rotation floor for `reciprocal` (elementwise multiplicative-inverse, `Tensor[N] -> Tensor[N]`). Re-anchor against the firm L1 `reciprocal` (`book/src/L1/reciprocal.md`) + firm L3 `reciprocal` (`book/src/L3/reciprocal.md`) + the L0 anchors already cited there (`palace/linalg/vector.cpp:255-260` complex kernel; `Reciprocal()` member surface). Per the cohort directive: where the L2 form is **truly identity to L1 and adds zero fusion vocabulary** (pure pointwise leaf, no HPC trick to erase), land a **thin identity L2 floor** — the point is floor *presence* under the firm L3 entry, not bulk. State explicitly: standalone elementwise leaf, **no fold-parent** (NOT a member of `inner_product` or `linear_combination`), so the leaf-vs-fold fork does not apply here.
- **deps:** none.
- **rationale:** `l2-floor-under-l3-blas1-cohort` (High fan-out), fork-independent slice. The L3 `reciprocal` entry currently says "no interposed L2 entry" — this builds the present floor the foundation-first directive wants. **D2 appends ONLY its own `L2/index.md` dep-map row + SUMMARY registration; DEFERS the consolidated tally to D11** (count-ownership convention).

**D3 — `harvester` — `book/src/L2/elementwise_product.md` (fork-INDEPENDENT L2 floor; elementwise binary, NO fold-parent).**
- **scope:** L2 fusion-rotation floor for `elementwise_product` (Hadamard binary `(Tensor[N], Tensor[N]) -> Tensor[N]`). Re-anchor against firm L1 `elementwise_product` + firm L3 `elementwise_product` + L0 (`palace/linalg/operator.cpp:478-507` `BaseDiagonalOperator::Mult`). Thin identity L2 floor (pure pointwise binary; no fusion vocabulary added). State: standalone, NO fold-parent. Cross-link the existing `concepts/elementwise-product.md` narrative.
- **deps:** none.
- **rationale:** Same as D2 — fork-independent cohort slice. **D3 appends ONLY its own dep-map row + SUMMARY; DEFERS tally to D11.**

**D4 — `harvester` — `book/src/L2/assemble-diagonal.md` (fork-INDEPENDENT L2 floor; operator-to-data gate, NO fold-parent).**
- **scope:** L2 fusion-rotation floor for `assemble-diagonal` (operator-to-data extraction `LinearOperator[N,N] -> Tensor[N]`). Re-anchor against firm L1 `assemble-diagonal` + firm L3 `assemble-diagonal` + L0 (`palace/linalg/operator.cpp:85-96`, `palace/linalg/rap.cpp:154-193`). **PRESERVE the load-bearing matrix-free high-order-Nedelec approximate-diagonal non-law** through the floor (per the OQ caveat-lifetime note: "the approximate-matrix-free non-law must be preserved through any future L1>L2 lift of `assemble_diagonal` — the L2 fusion-rotation must not erase the approximation"). This is an operator-to-data primitive (NOT an `apply_linop` variant), standalone, NO fold-parent.
- **deps:** none.
- **rationale:** `l2-floor-under-l3-blas1-cohort`, fork-independent. The diagonal-extraction floor unblocks the Jacobi/Chebyshev/block-Jacobi/polynomial-preconditioner L2 cohort. **D4 appends ONLY its own dep-map row + SUMMARY; DEFERS tally to D11.**

**D5 — `harvester` — `book/src/L2/jacobi-smoother.md` (fork-INDEPENDENT L2 floor; constructed-operator gate, NO fold-parent).**
- **scope:** L2 fusion-rotation floor for `jacobi-smoother` (diagonal-preconditioner action; constructed-operator gate `Mult(x,y)`). Re-anchor against firm L1 `jacobi-smoother` + firm L3 `jacobi-smoother` + L0 (`palace/linalg/jacobi.cpp:74-97` `Mult`; `:41-70` `Apply`). The L2 form is the constructed-operator-gate apply (one elementwise product `dinv ⊙ r` per the firm L3 framing). Note the `Apply<Transpose=true>` dead-code consumer branch (`jacobi.cpp:61-69`, OQ `reciprocal-elementwise-product-mr-dead-code-transpose-consumer-branch`) as a recognition-rule caveat if surfaced, NOT a status reduction. Standalone gate, NO fold-parent.
- **deps:** none.
- **rationale:** `l2-floor-under-l3-blas1-cohort`, fork-independent. **D5 appends ONLY its own dep-map row + SUMMARY; DEFERS tally to D11.**

**D6 — `harvester` — `book/src/L2/divfree-projector.md` (fork-INDEPENDENT L2 floor; constructed-operator gate, NO fold-parent).**
- **scope:** L2 fusion-rotation floor for `divfree-projector` (divergence-free Helmholtz projection; four-step constructed-operator gate delegating its only iteration to the inner `ksp_solve`). Re-anchor against firm L1 `divfree-projector` + firm L3 `divfree-projector` + L0 (`palace/linalg/divfree.cpp:155-187` impl; class doc `divfree.hpp:28-31` `Gᵀ M x = 0`). **Carry the inner-solve obstruction BY REFERENCE through the firm `ksp_solve` dependency** (per the firm L3 entry: "never introduced or erased here") — do NOT re-introduce it at L2. Honor the resolved `divfree-mult-doc-irrotational-vs-divfree-stale` disposition (the `divfree.hpp:64-66` per-method doc is inverted; the authoritative semantics are the divergence-free remainder, `Gᵀ M x = 0`). Standalone gate, NO fold-parent.
- **deps:** none.
- **rationale:** `l2-floor-under-l3-blas1-cohort`, fork-independent. **D6 appends ONLY its own dep-map row + SUMMARY; DEFERS tally to D11.**

**D7 — `abstractor` — `assemble-diagonal` L2>L1 + L3>L2 thin-identity themes.**
- **scope:** Author `book/src/L2-L1/assemble-diagonal-leaf-identity.md` (L2>L1) + `book/src/L3-L2/assemble-diagonal-body-identity.md` (L3>L2), both verified-ABSENT (see § Deliverable-presence). Thin-identity themes: the L2 floor (D4) is identity-in-form to the L1 leaf (signature-textually-identical operator-to-data map); the L3 body is identity-in-form to the L2 floor. Both narrate the rewrite **forward** (L2>L1: how the L2 form lowers to L1; L3>L2: how the L3 form lowers to L2), per the high→low invariant. Preserve the matrix-free approximate-diagonal non-law reference. **Slug-naming:** use `-leaf-identity` for the L2>L1 theme (mirroring the c041 D4 `dot-leaf-identity` landed convention; the D5/D6 `-fold-specialization` slugs are the outlier flagged for meta-phase normalization — do NOT replicate that outlier here).
- **deps:** D4 (the L2 floor must land first so the theme's L2 anchor resolves to a live link; forward-reference ordering → wave 2).
- **rationale:** `l3-l2-rotation-theme-coverage-gap` (High fan-out) + the L2>L1 leg of `l2-floor-under-l3-blas1-cohort`. Fork-independent (no fold-parent → no fork exposure). **D7 appends ONLY its own L2-L1/index + L3-L2/index dep-map rows + SUMMARY; DEFERS both index tallies to D11.**

**D8 — `abstractor` — `jacobi-smoother` L2>L1 + L3>L2 thin-identity themes.**
- **scope:** `book/src/L2-L1/jacobi-smoother-leaf-identity.md` + `book/src/L3-L2/jacobi-smoother-body-identity.md` (both verified-ABSENT). Thin-identity (constructed-operator-gate apply, identity-in-form across both edges). Same `-leaf-identity` / `-body-identity` slug convention as D7. Note the dead-code transpose branch caveat by reference if relevant; do NOT re-derive it.
- **deps:** D5 (L2 floor lands first).
- **rationale:** `l3-l2-rotation-theme-coverage-gap` + L2>L1 leg. Fork-independent. **Appends ONLY its dep-map rows + SUMMARY; DEFERS tallies to D11.**

**D9 — `abstractor` — `divfree-projector` L2>L1 + L3>L2 thin-identity themes.**
- **scope:** `book/src/L2-L1/divfree-projector-leaf-identity.md` + `book/src/L3-L2/divfree-projector-body-identity.md` (both verified-ABSENT). Thin-identity (four-step constructed-operator gate, identity-in-form; inner-solve obstruction carried by reference through `ksp_solve`, never introduced/erased at the theme edges). Same slug convention.
- **deps:** D6 (L2 floor lands first).
- **rationale:** `l3-l2-rotation-theme-coverage-gap` + L2>L1 leg. Fork-independent. **Appends ONLY its dep-map rows + SUMMARY; DEFERS tallies to D11.**

**D10 — `abstractor` — `reciprocal` + `elementwise_product` L2>L1 + L3>L2 thin-identity themes (the elementwise pair, one dispatch).**
- **scope:** Author FOUR thin-identity theme files: `book/src/L2-L1/reciprocal-leaf-identity.md`, `book/src/L3-L2/reciprocal-body-identity.md`, `book/src/L2-L1/elementwise-product-leaf-identity.md`, `book/src/L3-L2/elementwise-product-body-identity.md` (all verified-ABSENT). The two elementwise leaves are paired in ONE dispatch because they **share the single L1>L0 substantive theme** `reciprocal-elementwise-product-mutation-rotation` (firm) — pairing keeps the shared-reference handling coherent and avoids two abstractors touching the same upstream. Both pairs are pure pointwise identity-in-form across the L2>L1 and L3>L2 edges. Same `-leaf-identity`/`-body-identity` slug convention.
- **deps:** D2 + D3 (both elementwise L2 floors land first).
- **rationale:** `l3-l2-rotation-theme-coverage-gap` + L2>L1 leg, the two simplest elementwise leaves bundled. Fork-independent. **Appends ONLY its dep-map rows + SUMMARY; DEFERS tallies to D11.**

**D11 — `layer-intro-author` — SOLE count-owner of the L2 / L2-L1 / L3-L2 index consolidated tallies + cohort narratives.**
- **scope:** As the SOLE count-owner this cycle (count-ownership convention, cycle-039 meta), author the consolidated running-count tallies in `book/src/L2/index.md` (firm-op count + Vocabulary-cohort subsection: +5 floors → L2 firm 12→17), `book/src/L2-L1/index.md` (+up to 5 leaf-identity themes), and `book/src/L3-L2/index.md` (+up to 5 body-identity themes → advancing `l3-l2-rotation-theme-coverage-gap` 5-of-18 → 10-of-18), accounting for D2–D10's landings. Refresh the §Vocabulary-cohort / §Working-Notes narratives to describe the **fork-independent standalone-floor cohort** (elementwise leaves + constructed-operator gates, NO fold-parent) as a distinct motif from the c041 fold-parented BLAS-1-leaf cohort. **Surface the open leaf-vs-fold fork prominently in the L2/L2-L1/L3-L2 index §Working-Notes** (per c041 D7 precedent) so a reader sees the BLAS-1-leaf sub-cohort design is provisional pending the batch-12 meta-phase, while the standalone-floor sub-cohort (this cycle's landings) is fork-independent and design-final.
- **deps:** D2, D3, D4, D5, D6 (all floors), D7, D8, D9, D10 (all themes) — runs last so it tallies the complete cohort. (Wave 2; D11 reads on-disk landings, so it must follow every floor + theme dispatch in the per-report serial application order.)
- **rationale:** count-ownership convention — exactly ONE owner of each shared consolidated tally; D2–D10 defer. Prevents the `parallel-blind-shared-index-count-divergence` the convention addresses. **D11 is the ONLY dispatch that writes the three index tallies + Vocabulary-cohort lists.**

## Deliverable-presence verification

Per the MANDATORY paste-inline-evidence pre-dispatch check (cycle-036 meta-phase strengthening). Literal command output below.

**D1 (cross-layer audit) — open by construction (observation report, no named-artifact-slug deliverable; does not create a book/ file).** The cited files all EXIST (it audits firm entries). No file-creation slug to verify; the deliverable is a CYCLE.md observation. Skip is explicit: open by construction (audit/observation dispatch).

**D2 `L2/reciprocal.md`:**
- File existence: `ls book/src/L2/reciprocal.md` → `ls: cannot access 'book/src/L2/reciprocal.md': No such file or directory` (ABSENT — confirmed).
- Parents firm: `book/src/L1/reciprocal.md:103` → ``firm` — signature is canonical ...`; `book/src/L3/reciprocal.md:4` → `firmness: firm`. Both parents firm on-disk.
- OQ RESOLVED-grep: no `L2/reciprocal` or `reciprocal-l2-floor` RESOLVED/CLOSED disposition (the `reciprocal` RESOLVED hits are all L1 / L1>L0 / L3 work + the dead-code-transpose recognition-rule OQ — none names an L2 floor). Line clear.
- Structural-block check: NOT blocked — the firm L3 entry explicitly states "no interposed L2 entry" exists; the `l2-floor-under-l3-blas1-cohort` High-fan-out gate is OPEN; building the floor is the directed work. NOT on STOP-PROPOSING list. NOT fork-exposed (no fold-parent).

**D3 `L2/elementwise_product.md`:**
- File existence: `ls` → `No such file or directory` (ABSENT — confirmed).
- Parents firm: `book/src/L3/elementwise_product.md:4` → `firmness: firm`; `book/src/L1/elementwise_product.md` firm (entry present, `## Status` firm). Confirmed.
- OQ RESOLVED-grep: no `L2/elementwise_product` floor RESOLVED disposition. Clear.
- Structural-block: OPEN gate, NOT blocked, NOT on STOP-PROPOSING, NOT fork-exposed (no fold-parent; the `inner_product.md:387` "reciprocal boundary" mention is fold-boundary prose, not membership).

**D4 `L2/assemble-diagonal.md`:**
- File existence: `ls` → `No such file or directory` (ABSENT — confirmed).
- Parents firm: `book/src/L1/assemble-diagonal.md:93` → ``firm` — signature is canonical ...`; `book/src/L3/assemble-diagonal.md:4` → `firmness: firm`. Confirmed.
- OQ RESOLVED-grep: the `assemble-diagonal-mutation-rotation` RESOLVED hit is the L1>L0 THEME (cycle-020), NOT an L2 floor; the L2-abstractor caveat-lifetime note is an instruction TO this floor, not a closure. No `L2/assemble-diagonal` floor RESOLVED. Clear.
- Structural-block: OPEN gate, NOT blocked, NOT on STOP-PROPOSING, NOT fork-exposed (operator-to-data primitive, no fold-parent).

**D5 `L2/jacobi-smoother.md`:**
- File existence: `ls` → `No such file or directory` (ABSENT — confirmed).
- Parents firm: `book/src/L1/jacobi-smoother.md:374` `## Status` firm region; `book/src/L3/jacobi-smoother.md:4` → `firmness: firm`. Confirmed.
- OQ RESOLVED-grep: `jacobi-smoother-mutation-rotation-l1-l0` resolved cycle-033 (L1>L0 theme, NOT L2 floor). No `L2/jacobi-smoother` floor RESOLVED. Clear.
- Structural-block: OPEN gate, NOT blocked, NOT on STOP-PROPOSING, NOT fork-exposed (constructed-operator gate, no fold-parent).

**D6 `L2/divfree-projector.md`:**
- File existence: `ls` → `No such file or directory` (ABSENT — confirmed).
- Parents firm: `book/src/L1/divfree-projector.md:234` → ``firm`.`; `book/src/L3/divfree-projector.md:4` → `firmness: firm`. Confirmed.
- OQ RESOLVED-grep: `divfree-mult-doc-irrotational-vs-divfree-stale` resolved (a doc-comment disposition, honored as a CONSTRAINT on this floor, not an L2-floor closure); `divfree-projector-partly-constructive-to-firm-enactment` resolved cycle-015 (the L1 firm-flip). No `L2/divfree-projector` floor RESOLVED. Clear.
- Structural-block: OPEN gate, NOT blocked, NOT on STOP-PROPOSING, NOT fork-exposed (four-step constructed-operator gate, no fold-parent; inner-solve obstruction carried by reference, not introduced).

**D7 `L2-L1/assemble-diagonal-leaf-identity.md` + `L3-L2/assemble-diagonal-body-identity.md`:**
- File existence: `ls book/src/L2-L1/assemble-diagonal*.md` → `No such file or directory`; `ls book/src/L3-L2/assemble-diagonal-body-identity.md` → `No such file or directory` (both ABSENT — confirmed).
- Anchor (L2 floor) lands in-cycle via D4 (forward-reference ordering, wave 2). Structural-block: OPEN (`l3-l2-rotation-theme-coverage-gap` gate open), NOT blocked. NOT fork-exposed.

**D8 `L2-L1/jacobi-smoother-leaf-identity.md` + `L3-L2/jacobi-smoother-body-identity.md`:**
- File existence: `ls book/src/L2-L1/jacobi-smoother*.md` → `No such file or directory`; `ls book/src/L3-L2/jacobi-smoother-body-identity.md` → `No such file or directory` (both ABSENT — confirmed).
- Anchor lands via D5. Structural-block: OPEN, NOT blocked, NOT fork-exposed.

**D9 `L2-L1/divfree-projector-leaf-identity.md` + `L3-L2/divfree-projector-body-identity.md`:**
- File existence: `ls book/src/L2-L1/divfree-projector*.md` → `No such file or directory`; `ls book/src/L3-L2/divfree-projector-body-identity.md` → `No such file or directory` (both ABSENT — confirmed).
- Anchor lands via D6. Structural-block: OPEN, NOT blocked, NOT fork-exposed.

**D10 `L2-L1/{reciprocal,elementwise-product}-leaf-identity.md` + `L3-L2/{reciprocal,elementwise_product}-body-identity.md`:**
- File existence: `ls book/src/L2-L1/reciprocal*.md` / `elementwise_product*.md` → `No such file or directory`; `ls book/src/L3-L2/reciprocal-body-identity.md` / `elementwise_product-body-identity.md` → `No such file or directory` (all four ABSENT — confirmed).
- Anchors land via D2 + D3. Structural-block: OPEN, NOT blocked, NOT fork-exposed (both elementwise leaves, no fold-parent).

**D11 `L2/index.md` + `L2-L1/index.md` + `L3-L2/index.md` tallies — open by construction (count-owner refresh, not a new-slug creation).** The three index files EXIST (they carry the running tallies D11 updates). Skip is explicit: open by construction (count-ownership index refresh; the deliverable is a tally/narrative update accounting for the in-cycle landings, per the count-ownership convention).

**Cross-check — none of the proposed slugs is on the STOP-PROPOSING NEGATIVE LIST** (`lu_solve`, `back_solve`, `ls-update-column`, `nleps_deflated_residual`, `nleps_deflated_solve`, `nleps_jacobian_action`, `nleps_eigenvalue_correction`): confirmed, zero matches. **Framing check:** D1 is correctly audit-first (cross-cutter observation, not a reflexive harvest) per the cohort-boundary / representation-dependent-caveat guidance; D2–D10 are reflexive floor-builds on fork-INDEPENDENT operators (no audit-first reframe needed — the fork question does not apply to them, verified above).

## Overlap analysis

Pairwise (genuinely-overlapping = same operator entry rewritten OR same theme body OR same consolidated tally written by ≥2):

- **D1 vs all** — D1 is an observation report; it MUTATES NO ARTIFACT (cross-cutter dispatch-phase write-guard). It reads the BLAS-1-leaf cohort (`dot`/`nrm2`/`scal` + folds) which is **disjoint** from D2–D10's standalone-floor cohort (`reciprocal`/`elementwise_product`/`assemble-diagonal`/`jacobi-smoother`/`divfree-projector`). No overlap with anything. PARALLEL.
- **D2–D6 (the 5 floors) pairwise** — each creates a DISTINCT new file (`L2/reciprocal`, `L2/elementwise_product`, `L2/assemble-diagonal`, `L2/jacobi-smoother`, `L2/divfree-projector`). Each appends ONE DISTINCT dep-map row to `L2/index.md` and ONE DISTINCT SUMMARY line — distinct-row appends are NOT overlapping (per the §Discipline "append distinct rows = parallel" rule). The consolidated `L2/index.md` firm-count tally is written by D11 ONLY (count-ownership). PARALLEL.
- **D7–D10 (the theme dispatches) pairwise** — each creates DISTINCT new theme files in `L2-L1/` and `L3-L2/`. Distinct dep-map row appends to the two indices; consolidated tallies deferred to D11. No two touch the same theme body. PARALLEL with each other.
- **D7 vs D4 / D8 vs D5 / D9 vs D6 / D10 vs D2+D3** — each theme dispatch references its floor's L2 file as a live link; the floor must exist on disk first (forward-reference ordering). NOT an artifact-region overlap (the theme creates new files; it only READS the floor) — this is a SEQUENCING dependency, not a conflict. Handled by wave ordering.
- **D11 vs D2–D10** — D11 SOLE-writes the three index consolidated tallies + Vocabulary-cohort narratives; D2–D10 write ONLY their own distinct dep-map rows + SUMMARY lines and DEFER the tallies. By the count-ownership partition this is NOT an overlap (the partition is explicit per-dispatch). D11 must run AFTER all landings to tally the complete cohort — sequencing, not conflict.

No two dispatches rewrite the same operator entry or the same theme body or co-write the same consolidated tally. The only constraints are forward-reference sequencing (themes after their floors) and the count-owner running last.

## Sequencing schedule

- **Wave 1 (parallel):** D1, D2, D3, D4, D5, D6 — the audit + the 5 standalone L2 floors. Mutually disjoint (D1 mutates nothing; D2–D6 create distinct files + distinct rows). No forward-references among them.
- **Wave 2 (parallel, after wave-1 reports land):** D7 (after D4), D8 (after D5), D9 (after D6), D10 (after D2+D3) — the L2>L1 + L3>L2 thin-identity themes; each references its now-landed L2 floor as a live link. These four are mutually disjoint (distinct theme files).
- **Wave 2 tail / final per-report:** D11 (after D2–D10 all land) — the SOLE count-owner index refresh; must read the complete on-disk cohort. Ordered last in the per-report serial application sequence.

(Reminder per role-spec: there is exactly ONE `integrator-finalize` at cycle end; the waves order DISPATCHES by forward-reference, the book is NOT rebuilt between waves. D11 ordering is a per-report serial-application ordering so it tallies complete landings.)

## Open questions / caveats

- **The fork is the meta-phase's call, not mine.** This plan deliberately does NOT pre-decide the leaf-vs-fold fork; D1 supplies evidence and the batch-12 meta-phase (fires after this cycle) adjudicates. If the meta-phase adopts **fold-only**, the c041 BLAS-1-leaf floors (`dot`/`scal`) + their themes re-anchor, but **none of cycle-042's landings are affected** — D2–D10 build fork-INDEPENDENT standalone floors (verified: no fold-parent). This is the central design choice of the cycle and the reason the `axpy`/`axpby`/`axpbypcz` arity-family is HELD (it rides the `linear_combination` fold, the same fork).
- **Thin-floor judgment is delegated to the harvesters.** D2/D3 (elementwise leaves) and D4–D6 (constructed-operator gates) may each land a **thin identity L2 floor** if the L2 form adds zero fusion vocabulary over L1 (the cohort directive permits this — "the point is floor presence, not bulk"). If a harvester finds the L2 form is NOT identity-in-form (e.g. `divfree-projector`'s four-step composition exposes a genuine fusion the L1 form hides), it should land the fuller decomposition. I flag `divfree-projector` (D6) as the most likely to be non-thin (four-step gate) and `assemble-diagonal` (D4) as the one carrying the load-bearing approximate-matrix-free non-law that MUST survive the lift.
- **Slug-naming convention for the new themes.** I direct D7–D10 to use `-leaf-identity` (L2>L1) / `-body-identity` (L3>L2), matching the c041 D4 `dot-leaf-identity` / `dot-body-identity` landed convention. The c041 D5/D6 `-fold-specialization` slugs are the flagged outlier (OQs `nrm2-fold-specialization-slug-vs-consumer-framing-rename-candidate`, `scal-fold-specialization-slug-vs-leaf-identity-rename-candidate`) awaiting meta-phase normalization — I do NOT replicate that outlier. If the meta-phase normalizes the cohort slug convention differently, these new themes ride that same rename (cheap, slug-agnostic bodies).
- **Wave size at the cap-adjacent.** 11 dispatches (under the 12 cap). The c041 7-wide foundation wave ran clean under the split integrator; 11-wide with 5 floors + 4 theme dispatches + 1 audit + 1 count-owner is within validated bounds. The count-ownership partition held at 7-wide c041 (the broadest index-touching wave to date) — this cycle tests it at a comparable index-touch width (5 floors → L2/index; up to 9 theme files → L2-L1/index + L3-L2/index), all deferring to D11.
- **`elementwise_product` filename underscore vs hyphen.** The L1/L3 entries use `elementwise_product.md` (underscore); the concept page is `elementwise-product.md` (hyphen). I direct the L2 floor (D3) to match the L1/L3 entry filename (`L2/elementwise_product.md`, underscore) for cohort consistency; the L3>L2 theme (D10) likewise `elementwise_product-body-identity.md`. Flagging the underscore/hyphen split as a minor convention wrinkle for the meta-phase if it wants cohort-wide filename normalization (NOT blocking).
- **priorities.md updated this cycle** (per planner co-ownership): the cycle-042 active head is reshaped to this fork-aware foundation slice; the `l2-floor-under-l3-blas1-cohort` and `l3-l2-rotation-theme-coverage-gap` High-fan-out items are annotated with the cycle-042 picks (5 standalone-floor members + their themes) and the explicit HOLD on the fork-exposed `axpy`-family pending the batch-12 meta-phase adjudication.
