---
agent: lifter
invoked_at: 2026-06-03T193247Z
scope: feature-column re-anchor — eigenfrequency-qfactor.{L4,L1} (clear c080 D3-staleness; re-anchor eigenvalue-un-transform gate onto firm L1 eigenvalue-untransform)
status: pending
inputs:
  - book/src/feature/eigenfrequency-qfactor.L4.md
  - book/src/feature/eigenfrequency-qfactor.L1.md
  - book/src/L1/eigenvalue-untransform.md (firm, landed c080 D2)
  - book/src/L1/participation_ratio.md (firm, landed c077)
  - book/src/L4/eigenfreq_qfactor_reduce.md (rough-in (test-coverage-bounded); §Status already re-anchored c080)
  - scaffolding/open-questions.md:1011-1016 (OQ-1016 + the resolved gate-(a) chain)
integrated_at: 2026-06-03T194359Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-081 batch-25 position 3/3 (LAST primary cycle of batch-25; the batch-25 meta-phase fires AFTER this finalize). Applied clean via the proposed-changes channel — 7 edits across eigenfrequency-qfactor.{L4,L1}.md (the D3-staleness clear: dropped the stale 'no firm L1 entry' claim, live-linked firm L1 eigenvalue-untransform, flipped two dep-map cells rough-in->firm, re-anchored the seed-rationale onto gate-(b)). ZERO firm-count/status change (both columns stay seed; verb eigenfreq_qfactor_reduce stays rough-in (test-coverage-bounded)). Closed OQ-1016; residual gate-(b) lives at OQ-1013 (open, out of write-scope). cargo make book exit 0, zero build-repair. Single staging row == 1 dispatched-ready (no completeness gap)."
---

# CYCLE: Re-anchor eigenfrequency-qfactor.{L4,L1} — clear the c080 D3-staleness clause

## Summary

Pure-rewriting hygiene pass closing **OQ-1016** (`eigenfrequency-qfactor-L4-column-promotion-coupled-to-D2-untransform-firming`, open-questions.md:1016). The eigenfrequency-qfactor output-product feature column (L4 + L1) still carried the cycle-080 D3-reconciled prose asserting the eigenvalue-un-transform half of the folded reduction "has no firm L1 entry" — a clause that went stale the SAME cycle when c080 D2 landed the firm L1 primitive [`eigenvalue-untransform`](book/src/L1/eigenvalue-untransform.md) (`firmness: firm`, on-disk confirmed) and marked the L4 verb's gate-(a) discharged. D3 applied as-proposed (no over-reach) and logged the follow-up; this is that follow-up.

Three loci of staleness in each column file: the composing-frontmatter qualifier (L1 only), the inline `seed`-rationale prose, the dep-map cell for the eigenvalue-un-transform row, and the §Status block. After this pass: the eigenvalue-un-transform half is narrated as firm L1 with a live link to `book/src/L1/eigenvalue-untransform.md`; the SOLE remaining `seed`/`firm`-blocker is re-anchored onto **gate-(b)** — the eigenpair→`(f,Q)` **assembly test** (OQ `eigenfreq-qfactor-reduce-firm-needs-assembly-test`, open-questions.md:1013), which is out of write-scope (no positive eigenpair→`(f,Q)` assembly test exists in the corpus). The L4 verb STAYS `rough-in (test-coverage-bounded)` (its §Status was already re-anchored by c080 D2 — no change needed there); the column STAYS `seed`. **Zero status/count change** — pure prose + dep-map-cell hygiene.

The L0 column (`eigenfrequency-qfactor.L0.md`) is out of scope and correctly carries no staleness: it is a pure L0-source site-map with no L1-maturity claim (verified — no "no firm L1 entry"/"rough-in" maturity prose).

## Proposed changes

### Change 1 — `book/src/feature/eigenfrequency-qfactor.L4.md`

#### 1a. Frontmatter `composes` (L4 column) — keep the verb's own qualifier accurate

(No edit — the L4 frontmatter `composes` entry for `eigenfreq_qfactor_reduce.md` already reads `(rough-in — the per-mode scalar-ratio reduction combinator)`, which is the verb's true bare qualifier-family and unaffected by the L1-primitive firming. The drift was in the L1 column's frontmatter, fixed in Change 2a.)

#### 1b. The composition stage-(2) prose — re-anchor the un-transform half to firm L1

```edit:book/src/feature/eigenfrequency-qfactor.L4.md
[old]: 2. **The per-mode scalar-ratio reduction** — [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) (**rough-in**). The L4 per-mode scalar-ratio reduction combinator `eigenfreq_qfactor_reduce ptype κ eigs` maps each converged eigenpair to its `(f, Q)` table row: the eigenfrequency `fₘ = Re ωₘ` is the problem-type un-transform of the eigenvalue (`ω = √μ` for the linear EVP `μ = -λ² = ω²`; `ω = λ/i` for the quadratic EVP `λ = iω`), and the quality factor `Qₘ = ωₘ/κₘ` is the energy/loss ratio (`κₘ = ½Rⱼ·|Iₘⱼ|²/Eₘ`, the resistive-lumped-port participation; `κ = 0 ⇒ Q = ∞` lossless-mode guard). The reduction is a pure per-mode `map`-then-collect over the eigenpair family — **no inter-mode state, no `Solve` effect** (the eigenmode driver's readout loop is explicitly NOT a solve-iteration, [`solve_family`](../L4/solve_family.md):146). The **problem-type** un-transform (`√μ` vs `λ/i`) is the load-bearing variant axis, absorbed into the reduction's `untransform` dispatch. L0: the eigenvalue→ω un-transform `eigensolver.cpp:430-439`, the Q-factor body (`κₘ = ½R|I|²/E`, `Qₘ = ωₘ/κₘ`, the `κ=0 ⇒ Q=∞` guard) `postoperator.cpp:1188-1203`.
[new]: 2. **The per-mode scalar-ratio reduction** — [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) (**rough-in (test-coverage-bounded)**). The L4 per-mode scalar-ratio reduction combinator `eigenfreq_qfactor_reduce ptype κ eigs` maps each converged eigenpair to its `(f, Q)` table row: the eigenfrequency `fₘ = Re ωₘ` is the problem-type un-transform of the eigenvalue (`ω = √μ` for the linear EVP `μ = -λ² = ω²`; `ω = λ/i` for the quadratic EVP `λ = iω`), and the quality factor `Qₘ = ωₘ/κₘ` is the energy/loss ratio (`κₘ = ½Rⱼ·|Iₘⱼ|²/Eₘ`, the resistive-lumped-port participation; `κ = 0 ⇒ Q = ∞` lossless-mode guard). Both folded per-mode scalar maps are now **firm L1**: the eigenvalue un-transform is firm L1 [`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) (cycle-080), the κ-participation half is firm L1 [`participation_ratio`](../L1/participation_ratio.md) (cycle-077). The reduction is a pure per-mode `map`-then-collect over the eigenpair family — **no inter-mode state, no `Solve` effect** (the eigenmode driver's readout loop is explicitly NOT a solve-iteration, [`solve_family`](../L4/solve_family.md):146). The **problem-type** un-transform (`√μ` vs `λ/i`) is the load-bearing variant axis, absorbed into the reduction's `untransform` dispatch. L0: the eigenvalue→ω un-transform `eigensolver.cpp:430-439`, the Q-factor body (`κₘ = ½R|I|²/E`, `Qₘ = ωₘ/κₘ`, the `κ=0 ⇒ Q=∞` guard) `postoperator.cpp:1188-1203`.
```

#### 1c. The "Why this is a distinct output-product column" `seed`-rationale prose (line 55)

```edit:book/src/feature/eigenfrequency-qfactor.L4.md
[old]: The whole output product therefore lowers cleanly outward to the L4 backend surface: `eigenfrequency_qfactor = eigenfreq_qfactor_reduce (ptype, κ) ∘ eigenmode_eigenpairs` — a one-reduction tail on the eigenmode driver column. The column is `seed` (not promoted past it) because [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) is `rough-in (test-coverage-bounded)` — of its two folded per-mode primitives the κ-participation-ratio half is already firm L1 [`participation_ratio`](../L1/participation_ratio.md) (cycle-077), but the eigenvalue-un-transform half has no firm L1 entry and the postprocess test asserts reduction-OUTPUT invariance rather than the eigenpair→`(f, Q)` assembly; a feature column may promote past `seed` only once ALL its composed constituents are firm.
[new]: The whole output product therefore lowers cleanly outward to the L4 backend surface: `eigenfrequency_qfactor = eigenfreq_qfactor_reduce (ptype, κ) ∘ eigenmode_eigenpairs` — a one-reduction tail on the eigenmode driver column. The column is `seed` (not promoted past it) because [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) is `rough-in (test-coverage-bounded)`. Both of its folded per-mode primitives are now firm L1 — the κ-participation-ratio half is firm L1 [`participation_ratio`](../L1/participation_ratio.md) (cycle-077) and the eigenvalue-un-transform half is firm L1 [`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) (cycle-080), so the verb's structure-side gate-(a) is fully discharged. The SOLE remaining gate is **(b)** the eigenpair→`(f, Q)` **assembly test**: the existing postprocess test asserts reduction-OUTPUT invariance over the measurement cache rather than the eigenpair→`(f, Q)` assembly map itself, so the assembly-level laws are still test-unconfirmed (OQ `eigenfreq-qfactor-reduce-firm-needs-assembly-test`; the assembly test is integration-level under the eigenmode `Solve(mesh)` driver with no `test/unit/` home, hence out of write-scope). A feature column may promote past `seed` only once ALL its composed constituents are firm; the verb stays `rough-in (test-coverage-bounded)` on gate-(b) alone, so the column stays `seed`.
```

#### 1d. The eigenfrequency-un-transform dep-map cell (line 63) — re-anchor to firm L1 + status firm

```edit:book/src/feature/eigenfrequency-qfactor.L4.md
[old]: | eigenfrequency un-transform (folded) | [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) §Semantics | rough-in | `eigensolver.cpp:430-439` |
[new]: | eigenfrequency un-transform (folded) | [`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) (firm L1; folded by [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md)) | firm | `eigensolver.cpp:430-439` |
```

#### 1e. The §Status block (lines 68–78) — re-anchor the `seed`-rationale onto gate-(b) alone

```edit:book/src/feature/eigenfrequency-qfactor.L4.md
[old]: `seed` — an output-product **leaf feature column** authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the rank-1 per-mode-table sibling of the rank-2 Gram output products [capacitance](./capacitance.L4.md) / [inductance](./inductance.L4.md). The composition is sound: stage (1) consumes the [`eigenmode.L4`](./eigenmode.L4.md) driver column's converged eigenpair family; stage (2) composes the [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) per-mode scalar-ratio reduction at the problem-type un-transform + resistive-lumped-port κ. The verb is `rough-in (test-coverage-bounded)` (cycle-079 lowering-verifier audit). The column stays `seed` (does not promote) because the verb is still not `firm`: of its two folded per-mode primitives, the κ-participation-ratio half is already firm L1 [`participation_ratio`](../L1/participation_ratio.md) (cycle-077), but the eigenvalue-un-transform half has no firm L1 entry, and the postprocess test asserts reduction-OUTPUT invariance rather than the eigenpair→`(f, Q)` assembly itself — a feature column may promote past `seed` only once ALL its composed constituents are firm. This chapter carries the *compositional* claim (the `(f, Q)` table = the per-mode scalar-ratio reduction over the eigenmode driver's eigenpair family), not the constituents' per-op algebraic claims (those live in [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) and the [`eigenmode.L4`](./eigenmode.L4.md) driver column). The defining structural fact: a rank-1 per-mode scalar-ratio table, NOT a `gram_reduce` family-PAIR grid (c074 D6 closed-negative). Evidence: the L0 readout / Q-factor ranges `eigensolver.cpp:424-439` (the eigenvalue un-transform) + `postoperator.cpp:1171-1203` (`MeasureLumpedPortsEig`, the Q-factor) realizing the reduction, all anchors confirmed on-disk via palace-codemap `read_range` this dispatch, plus the constituent down-links.

The verb [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) was raised to `rough-in
(test-coverage-bounded)` (cycle-079 lowering-verifier audit: the PostOperator `[idempotent]`
postprocess test `test/unit/test-postoperator.cpp` CHECK-asserts the κ loss-rate `mode_port_kappa`
and the participation-ratio output fields as round-trip-invariant L0-equivalent semantics). The
column nonetheless stays `seed`: the verb is still not `firm` (its residual folded per-mode
primitive — the eigenvalue un-transform — has no firm L1 entry, and the test asserts
reduction-OUTPUT invariance not the eigenpair→`(f,Q)` assembly; the κ-participation half is already
firm L1 `participation_ratio`), and a feature column may promote past `seed` only once ALL its
composed constituents are firm.
[new]: `seed` — an output-product **leaf feature column** authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the rank-1 per-mode-table sibling of the rank-2 Gram output products [capacitance](./capacitance.L4.md) / [inductance](./inductance.L4.md). The composition is sound: stage (1) consumes the [`eigenmode.L4`](./eigenmode.L4.md) driver column's converged eigenpair family; stage (2) composes the [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) per-mode scalar-ratio reduction at the problem-type un-transform + resistive-lumped-port κ. The verb is `rough-in (test-coverage-bounded)` (cycle-079 lowering-verifier audit; gate-(a) discharged cycle-080). The column stays `seed` (does not promote) because the verb is still not `firm` — but its structure-side gate is now fully discharged: BOTH folded per-mode primitives are firm L1, the κ-participation-ratio half via [`participation_ratio`](../L1/participation_ratio.md) (cycle-077) and the eigenvalue-un-transform half via [`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) (cycle-080). The SOLE remaining gate is **(b)** the eigenpair→`(f, Q)` **assembly test** (OQ `eigenfreq-qfactor-reduce-firm-needs-assembly-test`): the existing postprocess test asserts reduction-OUTPUT invariance over the measurement cache rather than the eigenpair→`(f, Q)` assembly map itself, so the assembly-level laws are still test-unconfirmed; the assembly test is integration-level under the eigenmode `Solve(mesh)` driver with no `test/unit/` home, hence out of write-scope (a lowering-verifier law-confidence pass on the verb is the in-scope promotion route). A feature column may promote past `seed` only once ALL its composed constituents are firm. This chapter carries the *compositional* claim (the `(f, Q)` table = the per-mode scalar-ratio reduction over the eigenmode driver's eigenpair family), not the constituents' per-op algebraic claims (those live in [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) and the [`eigenmode.L4`](./eigenmode.L4.md) driver column). The defining structural fact: a rank-1 per-mode scalar-ratio table, NOT a `gram_reduce` family-PAIR grid (c074 D6 closed-negative). Evidence: the L0 readout / Q-factor ranges `eigensolver.cpp:424-439` (the eigenvalue un-transform) + `postoperator.cpp:1171-1203` (`MeasureLumpedPortsEig`, the Q-factor) realizing the reduction, all anchors confirmed on-disk via palace-codemap `read_range` this dispatch, plus the constituent down-links.

The verb [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) was raised to `rough-in
(test-coverage-bounded)` (cycle-079 lowering-verifier audit: the PostOperator `[idempotent]`
postprocess test `test/unit/test-postoperator.cpp` CHECK-asserts the κ loss-rate `mode_port_kappa`
and the participation-ratio output fields as round-trip-invariant L0-equivalent semantics). The
column nonetheless stays `seed`: the verb is still not `firm`, gated SOLELY on gate-(b) (the
eigenpair→`(f,Q)` assembly test asserts the eigenpair→`(f,Q)` assembly map, distinct from the
existing reduction-OUTPUT invariance test; out of write-scope, a lowering-verifier law-confidence
pass is the in-scope route). Its structure-side gate-(a) is fully discharged — both folded per-mode
primitives are firm L1, the eigenvalue un-transform via
[`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) (cycle-080) and the κ-participation half
via [`participation_ratio`](../L1/participation_ratio.md) (cycle-077). A feature column may promote
past `seed` only once ALL its composed constituents are firm.
```

### Change 2 — `book/src/feature/eigenfrequency-qfactor.L1.md`

#### 2a. Frontmatter `composes` qualifier (line 8)

```edit:book/src/feature/eigenfrequency-qfactor.L1.md
[old]:   - book/src/L4/eigenfreq_qfactor_reduce.md (rough-in — the per-mode scalar-ratio reduction; L1 sees the unfolded per-mode map)
[new]:   - book/src/L4/eigenfreq_qfactor_reduce.md (rough-in (test-coverage-bounded) — the per-mode scalar-ratio reduction; L1 sees the unfolded per-mode map; both folded per-mode scalar maps firm L1: eigenvalue-untransform c080 + participation_ratio c077)
```

#### 2b. The eigenfrequency-un-transform dep-map cell (line 59) — re-anchor to firm L1 + status firm

```edit:book/src/feature/eigenfrequency-qfactor.L1.md
[old]: | eigenfrequency un-transform | [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) §Semantics (L4 home; L1 unfolded map) | rough-in | `eigensolver.cpp:430-439` |
[new]: | eigenfrequency un-transform | [`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) (firm L1; folded by [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md)) | firm | `eigensolver.cpp:430-439` |
```

#### 2c. The §Status block (line 64) — re-anchor the un-transform half to firm L1 + gate-(b) framing

```edit:book/src/feature/eigenfrequency-qfactor.L1.md
[old]: `seed` — the L1 pure-function composition root for the eigenfrequency / Q-factor output product (the output-product **leaf feature column**), authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the L1 counterpart of the [eigenfrequency-qfactor.L4](./eigenfrequency-qfactor.L4.md) composition root. It consumes the [`eigenmode.L1`](./eigenmode.L1.md) driver column's converged eigenpair set, then maps each mode to its `(f, Q)` row (the problem-type eigenvalue un-transform + the resistive-port κ participation ratio + the `f/κ` quotient). The reduction's L4 home [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) is `rough-in` (its folded per-mode primitives are not yet firm L1 entries, no dedicated eigenmode-postprocess test) — consistent with the column being `seed`, not a firm composition. The chapter carries the compositional claim only; per-op algebraic claims live in the linked chapters. The defining structural fact carried from L4: a rank-1 per-mode scalar-ratio table, NOT a `gram_reduce` family-PAIR grid (c074 D6 closed-negative). Evidence: the L0 readout / Q-factor ranges `eigensolver.cpp:424-439` + `postoperator.cpp:1171-1203` realizing the reduction, plus the constituent down-links.
[new]: `seed` — the L1 pure-function composition root for the eigenfrequency / Q-factor output product (the output-product **leaf feature column**), authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the L1 counterpart of the [eigenfrequency-qfactor.L4](./eigenfrequency-qfactor.L4.md) composition root. It consumes the [`eigenmode.L1`](./eigenmode.L1.md) driver column's converged eigenpair set, then maps each mode to its `(f, Q)` row (the problem-type eigenvalue un-transform + the resistive-port κ participation ratio + the `f/κ` quotient). The reduction's L4 home [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) is `rough-in (test-coverage-bounded)`: both of its folded per-mode primitives are now firm L1 — the eigenvalue un-transform via [`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) (cycle-080) and the κ participation ratio via [`participation_ratio`](../L1/participation_ratio.md) (cycle-077), so its structure-side gate-(a) is fully discharged. The verb stays `rough-in (test-coverage-bounded)` gated SOLELY on gate-(b) (a dedicated eigenpair→`(f, Q)` assembly test, distinct from the existing reduction-OUTPUT invariance test; OQ `eigenfreq-qfactor-reduce-firm-needs-assembly-test`, out of write-scope) — consistent with the column being `seed`, not a firm composition. The chapter carries the compositional claim only; per-op algebraic claims live in the linked chapters. The defining structural fact carried from L4: a rank-1 per-mode scalar-ratio table, NOT a `gram_reduce` family-PAIR grid (c074 D6 closed-negative). Evidence: the L0 readout / Q-factor ranges `eigensolver.cpp:424-439` + `postoperator.cpp:1171-1203` realizing the reduction, plus the constituent down-links.
```

## Discipline notes

- **Pure-rewriting hygiene pass — zero status/count change.** The L4 verb `eigenfreq_qfactor_reduce` STAYS `rough-in (test-coverage-bounded)` (its §Status was already re-anchored by c080 D2 — gate-(a) discharged, gate-(b) open — so no edit was needed in that file). Both feature-column files STAY `seed`. No `## Status` line is flipped, so the **index-table status-cell guard** (lifter.md cycle-057 bullet) does NOT fire — there is no promotion to mirror in any `L*/index.md` / feature-Part index. (Confirmed: the feature columns remain `seed`; the only cells touched are the *constituent down-link* dep-map cells INSIDE the column files, lines 63 / 59, which are the column's own internal site-map, not a separate hand-maintained layer-index table.)
- **What changed and why.** Every edit drops the now-false claim "the eigenvalue-un-transform half has no firm L1 entry" (introduced by c080 D3's reconciled prose, stale the same cycle) and re-anchors that half onto the firm L1 primitive `book/src/L1/eigenvalue-untransform.md` (landed c080 D2, `firmness: firm`, verified on-disk this dispatch) via a live markdown link `../L1/eigenvalue-untransform.md`. The residual `seed`/`firm`-blocker is re-narrated onto **gate-(b)** alone (the eigenpair→`(f,Q)` assembly test) — matching the L4 verb's own already-re-anchored §Status framing (`eigenfreq_qfactor_reduce.md:213-221`: "gate-(a) is **discharged** … the SOLE remaining gate is **(b)**").
- **Live-link target verified on-disk.** `book/src/L1/eigenvalue-untransform.md` exists (18806 bytes, `firmness: firm`), so per the lifter live-link discipline + the `upgrade-plain-text-ref-to-live-link-when-target-on-disk` skill the re-anchor uses a live markdown link, not plain text. Relative path `../L1/eigenvalue-untransform.md` matches the existing `../L1/participation_ratio.md` sibling-link convention already in both columns.
- **No re-architecting.** This is a vocabulary/maturity re-anchor only — the column's composition (eigenmode driver column ∘ per-mode scalar-ratio reduction), its rank-1-not-Gram structural claim, and its dep-map shape are all preserved. No decomposition, sub-pattern, or signature changed (consistent with "structural rewrite, not authorship").
- **L0 column out of scope, confirmed clean.** `eigenfrequency-qfactor.L0.md` carries no L1-maturity claim (grep: no "no firm L1 entry"/"rough-in" maturity prose — only L0-source site-map + a `seed` status tied to L0 anchors), so it needs no re-anchor; the planner correctly scoped only L4 + L1.

## Supporting evidence

- **The firm L1 primitive (the re-anchor target):** `book/src/L1/eigenvalue-untransform.md` — `firmness: firm`, the `√μ`/`λ/i` per-mode scalar branch keyed on `EvpDegree`, firm-on-positive-structure (every law a syntactic identity on `eigensolver.cpp:430-439`). Landed c080 D2. Its §Status:200-207 already records the coupled re-anchor discharging gate-(a) of the L4 verb.
- **The firm L1 sibling (κ-participation half, c077):** `book/src/L1/participation_ratio.md` — `firmness: firm`, already-firm before this pass (no re-open).
- **The L4 verb (already re-anchored c080 D2):** `book/src/L4/eigenfreq_qfactor_reduce.md:185-221` — `rough-in (test-coverage-bounded)`, §Status states gate-(a) discharged (both folded primitives firm L1) + gate-(b) the sole remaining gate. This pass aligns the feature-column prose to that already-current verb framing.
- **OQ chain:** `scaffolding/open-questions.md:1011` (`eigenvalue-untransform-l1-primitive` CLOSED-RESOLVED c080 D2), `:1012` (gate-(a) OQ CLOSED-RESOLVED c080 D2), `:1013` (`eigenfreq-qfactor-reduce-firm-needs-assembly-test` — the live successor, gate-(b)), `:1016` (OQ-1016 — the D3-staleness follow-up this dispatch closes).
- **L0 anchors self-verified this dispatch** via `tools/citecheck/citecheck.py`: `palace/drivers/eigensolver.cpp:430-439 --anchor 'std::sqrt'` → anchor at `:433` in-range `[ok]`; `palace/models/postoperator.cpp:1188-1203 --anchor 'quality_factor'` → anchor at `:1200` in-range `[ok]`. Both dep-map-cell L0 ranges (unchanged by this pass) confirmed.

## Open questions / caveats

- **Closes OQ-1016** (`eigenfrequency-qfactor-L4-column-promotion-coupled-to-D2-untransform-firming`, open-questions.md:1016) — the D3-staleness follow-up. The feature-column prose + dep-map cells are now re-anchored to the firm L1 eigenvalue-un-transform; the residual blocker is correctly the single gate-(b). Recommend the integrator mark OQ-1016 CLOSED-RESOLVED (cycle-081 D1 lifter).
- **No abstractor reread needed.** The firmed-up primitive's signature (`EvpDegree -> Complex -> Complex`) matches the un-transform the column already narrated (`√μ` / `λ/i` per-mode scalar map); the re-anchor is purely vocabulary/maturity. No signature contradiction surfaced.
- **gate-(b) remains open and out of write-scope** (`eigenfreq-qfactor-reduce-firm-needs-assembly-test`, open-questions.md:1013). The in-scope promotion route is a lowering-verifier law-confidence pass on `eigenfreq_qfactor_reduce` (now that BOTH folded primitives are firm L1) — flagged for a future reduction-verb-firming cycle, NOT this hygiene pass. When gate-(b) discharges and the verb promotes to `firm`, a follow-up pass would flip BOTH feature columns `seed`→`firm` (and that flip WOULD then require the index-cell guard — noted for that future dispatch).
