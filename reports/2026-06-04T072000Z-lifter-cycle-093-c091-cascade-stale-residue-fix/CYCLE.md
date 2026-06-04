---
agent: lifter
invoked_at: 2026-06-04T072000Z
scope: L1 land-clean — fix two stale-prose residues left by the c091 matrix-weighted-norm firm-flip cascade
status: pending
inputs:
  - book/src/L1/matrix-weighted-norm.md
  - book/src/L1/index.md
integrated_at: 2026-06-04T082000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: >-
  LAND-CLEAN (cycle-093, batch-29 position 3/3). Applied all 4 within-file
  stale-prose re-anchors: matrix-weighted-norm.md :150 Evidence-section
  conclusion + :122 gate-(c) body + :180-184 FP-residue paragraph (all stale
  "stays rough-in" conclusions re-anchored to the firm :110 §Status), plus
  L1/index.md:31 count-prose (37→38 grand-total, 30→31 main-cohort). ZERO
  status/count/dep-map/SUMMARY/header change — pure stale-prose re-anchor to the
  already-authoritative on-disk firm state; §Status :110 + the verified_against:
  YAML untouched. Closed 2 OQs
  (l1-index-firm-grand-total-37-stale-prose-clause-post-c091-cascade +
  matrix-weighted-norm-evidence-section-stale-rough-in-conclusion-post-c091-firm-flip;
  coverage of the latter extended by the repairer to :122/:180-184). Repairer
  fired a scope-extension (1→4 residues). Build exit 0, zero dead links, no
  build-repair. matrix-weighted-norm.md is now internally self-consistent.
---

# CYCLE: Re-anchor c091-cascade stale-prose residue (matrix-weighted-norm firm-flip)

## Summary
The cycle-091 batch-29 LEAD firm-flip-and-cascade wave promoted `matrix-weighted-norm` from `rough-in (test-coverage-bounded)` to `firm` (both norm-axiom law-sides discharged: structure-side laws 4/6/7 c088, FP-side `:69-70` c089; gate (a) judged redundant by the batch-28 meta-phase). The `## Status` (`matrix-weighted-norm.md:110`) and the authoritative count header (`L1/index.md:31`) were correctly flipped, but the flip left TWO stale prose references behind that contradict the now-firm reality. This land-clean dispatch re-anchors both to match the already-correct on-disk maturity + counts. **ZERO status / count-header / dep-map / SUMMARY change** — the operators are at their correct on-disk maturity; this fixes stale PROSE only.

**Residue 1 (internal contradiction):** `matrix-weighted-norm.md:150` — the Evidence-section "Radicand-constituent test evidence (cycle-080)" paragraph closes with a stale conclusion clause stating "the firm-on-positive-structure escape does not apply and the entry stays `rough-in (test-coverage-bounded)`". This directly contradicts the firm `## Status` at `:110` and the c088/c089 discharge record carried in the four `verified_against:` blocks at `:152-169`.

**Residue 2 (self-correcting count-prose):** `L1/index.md:31` — two stale count clauses inside the long cohort paragraph ("bringing the L1 firm grand total to **37**" and "The 30 main-cohort firm operators are...") contradict the same line's authoritative header ("31 main cohort; 38 firm grand total") and its own reconciliation note ("(30→31)" / "(37→38) updated above").

## Verification (done first, on-disk)
- `matrix-weighted-norm.md:108-115` — `## Status` reads `firm`, promoted by the batch-28 meta GO, enacted c091; both law-sides discharged (c088 structure / c089 FP); gate (a) judged REDUNDANT; basis = the firm-on-positive-structure escape. **Confirmed firm.**
- `matrix-weighted-norm.md:152-169` — the four `verified_against:` blocks ARE the discharge record (incl. the c088 `palace/drivers/eigensolver.cpp:205-213` SPD-construction entry, `audited_at: 2026-06-04T022000Z`, verdict `supports`: `KM = GetInnerProductMatrix(0.0,1.0,nullptr,M.get())` provably SPD by construction). These confirm the firm flip is the correct state — so the `:150` conclusion clause is genuinely stale, NOT the §Status being wrong.
- `matrix-weighted-norm.md:150` — confirmed the stale conclusion clause "...so the firm-on-positive-structure escape does not apply and the entry stays `rough-in (test-coverage-bounded)`." present verbatim, contradicting `:110`.
- `L1/index.md:31` — authoritative header "**Firm (31 main cohort; 38 firm grand total...)**"; count-discipline sentence "31 main + 4 FE-assembly + 3 FE-space = 38"; dep-map "**38** `firm` rows ... the main-cohort's 31st firm member"; reconciliation note "(30→31) and the grand total (37→38) updated above". The stale clauses "to **37**" and "The 30 main-cohort firm operators are" contradict these authoritative anchors on the same line.
- Citation basis: residue fixes re-anchor to the artifact's OWN already-verified firm state (the firm §Status + discharge record + authoritative count header), not new L0 pinpoint citations — the preserved L0 evidence citations (`operator.cpp:599-619`, etc.) are untouched verbatim.

## Proposed changes

### Residue 1 — matrix-weighted-norm.md:150 (Evidence-section stale conclusion)

Surgical: preserve all evidentiary content (the `test-domainpostoperator.cpp:75-93` radicand-constituent observation, the WithinRel 1% tolerance, the three-eigensolver-backend indirect-coverage note). Replace ONLY the stale conclusion clause that asserts the escape "does not apply" and the entry "stays rough-in" with the firm reality (escape DID apply; both law-sides discharged c088/c089; gate (a) redundant; entry IS firm). Do NOT touch `## Status` (`:110`), the `verified_against:` blocks (`:152-169`), or the frontmatter.

```edit:book/src/L1/matrix-weighted-norm.md
[old]: **Radicand-constituent test evidence (cycle-080), √-overload entry point still uncovered** — `test/unit/test-domainpostoperator.cpp:75-93` positively exercises the SPD-weighted radicand `⟨E, M_elec E⟩` + `½` scaling (the energy-form constituent that `domain_energy_reduce` folds) and asserts it against a closed form to 1% relative tolerance. This advances gate (a) from "no direct test evidence" to "radicand positively covered, √-overload named entry point (`linalg::Norml2(comm, x, B, Bx)`) still untested". The norm-axiom laws (4 triangle, 6 Cauchy–Schwarz, 7 parallelogram) carry genuine inner-product-structure content that the L0 source does not verify, so the firm-on-positive-structure escape does not apply and the entry stays `rough-in (test-coverage-bounded)`. Indirect coverage via the three eigensolver backends (ARPACK, SLEPc, NLEPS) is consistent but does not constitute algebraic-law verification.
[new]: **Radicand-constituent test evidence (cycle-080), √-overload entry point uncovered (gate (a) judged redundant cycle-091)** — `test/unit/test-domainpostoperator.cpp:75-93` positively exercises the SPD-weighted radicand `⟨E, M_elec E⟩` + `½` scaling (the energy-form constituent that `domain_energy_reduce` folds) and asserts it against a closed form to 1% relative tolerance. This advances gate (a) from "no direct test evidence" to "radicand positively covered, √-overload named entry point (`linalg::Norml2(comm, x, B, Bx)`) still untested". **The earlier reading — that the norm-axiom laws (4 triangle, 6 Cauchy–Schwarz, 7 parallelogram) carry inner-product-structure content the L0 source does not verify, so the firm-on-positive-structure escape does not apply — was superseded by the cycle-088/cycle-089 discharges (see `## Status`):** laws 4/6/7 are theorems about ANY inner-product-induced norm and the SPD premise they require is satisfied provably-by-construction at the usage sites (`B = KM`, the real SPD part of the mass matrix), so the structure-side laws hold as inner-product-space theorems with no positive √-entry-point test (the structure-side analog of the escape, cycle-088); the floating-point sub-claims `:69-70` discharge by additive inheritance from firm `dot` / `apply_linop` through a deterministic IEEE-754 outer `√` (cycle-089, the `nrm2` precedent). With both law-sides discharged, **the firm-on-positive-structure escape DID apply** and gate (a)'s √-entry-point test was judged REDUNDANT by the batch-28 meta-phase (everything it would confirm is already anchored) — the entry was promoted to `firm` cycle-091 (batch-29 LEAD). The radicand-constituent coverage here, and the consistent indirect coverage via the three eigensolver backends (ARPACK, SLEPc, NLEPS), are corroborating but were not the basis of the promotion.
```

### Residue 2 — L1/index.md:31 (stale count-prose clauses)

Two surgical replacements within the long cohort paragraph. Do NOT touch the authoritative header ("31 main cohort; 38 firm grand total"), the count-discipline sentence ("31 main + 4 FE-assembly + 3 FE-space = 38"), the dep-map clause ("**38** `firm` rows"), the reconciliation note, the historical "cycle-080 D2 added the main-cohort's 30th firm member" clause (correct history), or any dep-map row.

Clause A — the "bringing... to **37**" stale running-total (contradicts the "38" authoritative header on the same line):

```edit:book/src/L1/index.md
[old]: and the FE-space sub-spine adds **3** more firm (`fe_space` c064 + `fe_collection` c065 + `essential_dofs` c066 — see the §"Firm (FE-space sub-spine)" subsection), bringing the L1 firm grand total to **37** (cycle-080 D2 added the main-cohort's 30th firm member `eigenvalue-untransform`,
[new]: and the FE-space sub-spine adds **3** more firm (`fe_space` c064 + `fe_collection` c065 + `essential_dofs` c066 — see the §"Firm (FE-space sub-spine)" subsection), bringing the L1 firm grand total to **38** (cycle-080 D2 added the then-30th main-cohort firm member `eigenvalue-untransform`,
```

Clause B — the "The 30 main-cohort firm operators are" enumeration lead-in (the enumeration now includes `matrix-weighted-norm` c091 as the 31st, so "30" is stale; the reconciliation note one sentence earlier already says "(30→31) updated above"):

```edit:book/src/L1/index.md
[old]: BOTH the main-cohort count (30→31) and the grand total (37→38) updated above. The 30 main-cohort firm operators are element-wise updates, BLAS-1 reductions,
[new]: BOTH the main-cohort count (30→31) and the grand total (37→38) updated above. The 31 main-cohort firm operators are element-wise updates, BLAS-1 reductions,
```

### Residue 3 — matrix-weighted-norm.md:122 (gate-(c) body: header/body contradiction + stale "stays rough-in" conclusion)

**Repairer-added (cycle-093 repair).** Same c091-cascade stale-conclusion class as Residue 1. The gate-(c) bullet is inside the "Promotion-to-firm gates ... retained below as the discharge record" block (`:117`), but it carries (i) an internal header/body contradiction — the parenthetical header says "FP sub-claims still open" while its own body says "With the FP-side now discharged" — and (ii) a live current-conclusion ("the **sole** remaining driver of `rough-in (test-coverage-bounded)` is gate (a)" / "only the entry-point test remains") that was written at the cycle-089 D1-probe state and is now stale: the batch-28 meta GO judged gate (a) REDUNDANT (`:115`) and enacted the firm flip c091. The evidentiary content (the structure-side / FP-side discharge narration, the literature anchors, the zero-4-arg-`Norml2`-in-`test/unit/` finding) is preserved; only the stale "still open" header and the stale "stays rough-in / sole remaining driver" conclusion are re-anchored to the firm reality (gate (a) judged redundant, entry firm c091). Do NOT touch the §Status `:110`, the `verified_against:` YAML blocks, or the structure/FP-side discharge evidence.

Header parenthetical (stale "still open"):

```edit:book/src/L1/matrix-weighted-norm.md
[old]: - **(c) Algebraic-law completeness verification** (norm-axiom laws 4/6/7 STRUCTURE-SIDE DISCHARGED cycle-088; FP sub-claims still open): confirm laws 1-12 hold uniformly across the two L0 specializations, including the load-bearing SPD precondition.
[new]: - **(c) Algebraic-law completeness verification** (norm-axiom laws 4/6/7 STRUCTURE-SIDE DISCHARGED cycle-088; FP sub-claims DISCHARGED cycle-089; gate as a whole discharged — see §Status): confirm laws 1-12 hold uniformly across the two L0 specializations, including the load-bearing SPD precondition.
```

Body conclusion (stale "sole remaining driver is gate (a)" / "only the entry-point test remains"):

```edit:book/src/L1/matrix-weighted-norm.md
[old]: With the FP-side now discharged, the **sole** remaining driver of `rough-in (test-coverage-bounded)` is gate (a)'s direct √-entry-point test (`linalg::Norml2(comm,x,B,Bx)`): the corpus has ZERO references to the **SPD-weighted 4-arg overload** `Norml2(comm,x,B,Bx)` in `test/unit/` (the only `Norml2` hits are the unweighted 2-arg `linalg::Norml2(comm,x)` and the `mfem::Vector::Norml2()` method form — a different operator, `nrm2`; verified cycle-089). The structure-side (laws 4/6/7, cycle-088) and the FP-side (laws `:69-70`, cycle-089) are both closed; **only the entry-point test remains**. The combined discharge LICENSES — but does not itself enact — a future full-firm flip of the verb; that flip plus its ~30-file cascade is a separately-gated wave (recommended batch-29 LEAD `matrix-weighted-norm-firm-flip-and-cascade-wave`, see the cycle-089 D1 probe report).
[new]: With the FP-side now discharged, the only gate that had remained was gate (a)'s direct √-entry-point test (`linalg::Norml2(comm,x,B,Bx)`): the corpus has ZERO references to the **SPD-weighted 4-arg overload** `Norml2(comm,x,B,Bx)` in `test/unit/` (the only `Norml2` hits are the unweighted 2-arg `linalg::Norml2(comm,x)` and the `mfem::Vector::Norml2()` method form — a different operator, `nrm2`; verified cycle-089). The structure-side (laws 4/6/7, cycle-088) and the FP-side (laws `:69-70`, cycle-089) are both closed. **Gate (a) was subsequently judged REDUNDANT by the batch-28 meta-phase** (everything it would confirm is already anchored by the structure-side and FP-side discharges — see §Status `:115`), so the combined discharge enacted the full-firm flip of the verb at cycle-091 (the batch-29 LEAD `matrix-weighted-norm-firm-flip-and-cascade-wave`); the ~30-file cascade landed in that wave.
```

### Residue 4 — matrix-weighted-norm.md:180-184 (FP-residue paragraph: stale "stays rough-in" conclusion)

**Repairer-added (cycle-093 repair).** Same c091-cascade stale-conclusion class as Residue 1. The Evidence-section paragraph "FP-residue law-confidence DISCHARGE (cycle-089 D1 probe)" is live prose (NOT inside a frozen `verified_against:` YAML block — that frozen block follows at `:186-212` and is correctly left untouched). Its narration of the additive FP inheritance is correct and preserved; only its closing sentence — "The verb stays `rough-in (test-coverage-bounded)` pending ONLY gate (a)'s √-entry-point test." — is a live current-conclusion now stale against the firm `:110` §Status (gate (a) judged redundant c091). Re-anchor that one sentence; preserve the FP-inheritance evidentiary body.

```edit:book/src/L1/matrix-weighted-norm.md
[old]: outer `√`; no composition-specific FP property remains (the `nrm2` firmness precedent extended by
one firm constituent). The verb stays `rough-in (test-coverage-bounded)` pending ONLY gate (a)'s
√-entry-point test.
[new]: outer `√`; no composition-specific FP property remains (the `nrm2` firmness precedent extended by
one firm constituent). This FP-side discharge, together with the cycle-088 structure-side discharge,
left gate (a)'s √-entry-point test as the only outstanding gate — which the batch-28 meta-phase then
judged REDUNDANT (everything it would confirm is already anchored; see §Status), enacting the firm
flip at cycle-091.
```

## Discipline notes
- **Bounded prose-correction, both residues** (CLAUDE.md §lifter "L0-evidence-driven prose correction is in-scope when bounded + evidenced + recorded"). Both are stale-claim fixes re-anchoring to the artifact's OWN already-verified firm state — (i) supported by the on-disk firm `## Status` (`:110`) + the four `verified_against:` discharge blocks (`:152-169`) + the authoritative count header (`L1/index.md:31`); (ii) bounded (fixing a backward/stale conclusion + two stale ordinals, NOT re-architecting any decomposition or signature); (iii) recorded here, not silent.
- **Residue 1 is an internal-contradiction repair**, the most load-bearing class: the Evidence conclusion asserted the OPPOSITE maturity from the firm §Status on the same page. I preserved every piece of evidentiary content (the `test-domainpostoperator.cpp:75-93` radicand observation, the 1% WithinRel, the eigensolver-backend indirect-coverage note) and rewrote only the conclusion clause, framing the old reading as superseded-by-c088/c089 rather than deleting the history (keeps the discharge narrative legible).
- **Residue 2 distinguishes stale current-claims from correct history.** "37" / "The 30 main-cohort" are stale current totals; "cycle-080 D2 added the main-cohort's 30th firm member" is correct c080 history and was preserved (I tightened "30th main-cohort firm member" → "then-30th main-cohort firm member" in Clause A only to disambiguate the historical reading from the now-current 31, which is a clarity touch within the same bounded clause, not a count change). The authoritative "38"/"31"/reconciliation anchors on the same line were left untouched.
- **Index-cell-status-drift guard (CLAUDE.md §lifter): N/A.** No `## Status` flip in this dispatch — the c091 wave already flipped status + the index header. This is pure stale-PROSE re-anchor; the dep-map row + index header are already correct on-disk, so there is no status/index-cell desync to couple-fix.
- **Whole-book maturity-token grep (CLAUDE.md §lifter firm-promotion guard): N/A as a promotion.** No promotion happens here (the promotion was c091). The original dispatch fixed the two brief-pinned sites (`:150`, `index.md:31`); the repairer (cycle-093 repair) extended the SAME stale-conclusion re-anchor to the additional same-file live-prose sites a single-file grep surfaces — `:122` (gate-(c) header/body contradiction + stale "sole remaining driver / only the entry-point test remains" conclusion) and `:180-184` (the FP-residue paragraph's stale "stays rough-in" closing sentence). After these four edits, a same-file grep for the stale "stays `rough-in (test-coverage-bounded)`" / "escape does not apply" / "sole remaining driver" conclusion finds NO live-prose hits in `matrix-weighted-norm.md`; the only remaining "rough-in (test-coverage-bounded)" occurrences are inside the frozen `verified_against:` YAML audit notes (`:177`, `:191`-region), which are legitimately-preserved point-in-time verdicts (`audited_at` stamped), correctly out of scope. Scope is hard-constrained to the two named files; the cascade, gram_reduce, bilinear-form, normalize's note, and the feature columns were not touched.

## Supporting evidence
- `book/src/L1/matrix-weighted-norm.md:110` — firm `## Status` (the basis; batch-28 meta GO, enacted c091).
- `book/src/L1/matrix-weighted-norm.md:112-115` — the c088/c089 discharge narrative + the firm-on-positive-structure escape basis + gate-(a)-redundant judgment.
- `book/src/L1/matrix-weighted-norm.md:152-169` — the four `verified_against:` discharge blocks (incl. c088 `eigensolver.cpp:205-213` SPD-construction).
- `book/src/L1/index.md:31` — authoritative count header "31 main cohort; 38 firm grand total" + count-discipline sentence + reconciliation note (the basis for Residue 2).
- `reports/2026-06-04T032609Z-meta-phase-cycle-090/CYCLE.md` §Decisions "go 1" — the batch-28 meta-phase GO that judged gate (a) redundant (referenced in the firm §Status).

## Open questions / caveats
- None blocking. The two OQs this closes:
  - `matrix-weighted-norm-evidence-section-stale-rough-in-conclusion-post-c091-firm-flip` (Residue 1, filed by the repairer this cycle) — **closeable**: the Evidence conclusion now matches the firm §Status.
  - `l1-index-firm-grand-total-37-stale-prose-clause-post-c091-cascade` (Residue 2) — **closeable**: the stale "37"/"30 main-cohort" prose clauses now match the authoritative 38 / 31 anchors.
- No abstractor reread needed: the firmed-up signature did not change; this is a pure stale-prose re-anchor, no LHS/RHS shape change, no decomposition change.
- **Same-file residue accounting now COMPLETE (cycle-093 repair).** Beyond the two brief-pinned sites, the repairer re-anchored the two additional same-file live-prose sites a single-file grep surfaces — `:122` (gate-(c)) and `:180-184` (FP-residue paragraph) — both carrying the identical stale "stays `rough-in (test-coverage-bounded)`" current-conclusion class as `:150`. After integration, `matrix-weighted-norm.md` is internally self-consistent: the firm `## Status` (`:110`) has NO contradicting live-prose conclusion anywhere in the file; the only residual "rough-in (test-coverage-bounded)" strings are inside frozen `verified_against:` YAML audit notes (point-in-time verdicts, correctly preserved). No follow-up residue routing needed for this file.
