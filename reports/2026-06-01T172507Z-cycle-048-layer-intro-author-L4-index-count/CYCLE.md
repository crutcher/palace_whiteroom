---
agent: layer-intro-author
invoked_at: 2026-06-01T172507Z
scope: L4/index.md consolidated-count owner (cycle-048 D4, wave 3) — the tally + §Queued-prose flip + §Vocabulary-cohort narrative refresh that D1/D2 deferred
status: integrated
integrated_at: 2026-06-01T181949Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean (D4; cycle-048; sole L4/index count-owner). Firm-at-L4 tally (4 + 3 outer-driver)->(6 + 4 outer-driver) + outer-driver sub-header (3)->(4) + §Queued-at-L4 prose flip (L4 near-exhausted; R5 orthogonalize deferred-marginal kept plain-text; batch-14 meta-phase hand-off) + §Vocabulary-cohort narrative refresh. NO operator surface, no clobber of D1/D2 own rows/bullets. Opened 2 OQs (l4-near-exhaustion-assessment-batch-14; eigoutcome-vs-polymorphic-outcome-count-dependency). Count verified against disk (6 L4 chapters, 4 outer-driver rows). retroactive-budget 0; build clean, linkcheck2 green. integrator-finalize ALSO added the ksp-solve-driver-dissolution row to L4/index §'L4>L3 lowering themes' narrative sub-list (D4-flagged discoverability touch -- mechanical, not a build break)."
inputs:
  - book/src/L4/index.md (on-disk; the §Vocabulary-cohort header :32 + outer-driver sub-header :39 + §Queued-at-L4 prose :53-58)
  - reports/2026-06-01T172507Z-cycle-048-harvester-L4-ksp-solve-cap/CYCLE.md (D1 — firm L4/ksp_solve cap; OWN row+bullet; deferred tally + Queued prose to D4)
  - reports/2026-06-01T172507Z-cycle-048-harvester-L4-eigsolve-cap/CYCLE.md (D2 — firm L4/eigsolve cap + NEW EigOutcome outer-driver row; OWN row+bullet; deferred tally + Queued prose to D4)
  - reports/2026-06-01T172507Z-cycle-048-abstractor-ksp-solve-driver-dissolution/CYCLE.md (D3 — L4>L3 theme, lands in L4-L3/, does NOT affect the L4/index count; landed slug ksp-solve-driver-dissolution)
  - scaffolding/priorities.md (l4-l3-coverage-and-l4-expansion lead frontier; c046 survey "L4 mostly intentionally complete"; batch-14 meta-phase fires after c048)
  - scaffolding/open-questions.md :172 (l4-orthogonalize-cap-marginal-defer R5 — gated on a firm L4 Arnoldi consumer that does not exist)
---

# CYCLE: L4/index.md consolidated-count refresh (D4 — sole count-owner)

## Summary

I am the **sole `book/src/L4/index.md` consolidated-aggregate owner** for cycle-048 (count-ownership convention, cycle-039 meta; dual-registration partition, cycle-045 meta). D1 (`L4/ksp_solve`) and D2 (`L4/eigsolve`) each landed a NEW firm L4 cap this cycle and each wrote their OWN dep-map TABLE row + OWN §Vocabulary-cohort BULLET, **deferring the consolidated aggregates to me**. D2 additionally added a NEW `EigOutcome` outer-driver vocabulary row (the clean-addition `Outcome` extension). This report proposes the three deferred consolidated edits I own:

- **(a) Firm-at-L4 count tally** (§Vocabulary-cohort header `:32` + the outer-driver sub-header `:39`): `(4 + 3 outer-driver)` → `(6 + 4 outer-driver)`, reflecting the two new firm caps (`ksp_solve` + `eigsolve`) and D2's new `EigOutcome` outer-driver row.
- **(b) §Queued-at-L4 prose flip** (`:53-58`): the two iterative-solve CAP chapters are no longer queued — both authored this cycle. The §Queued section empties; I record that the L4 frontier is **substantially complete / near-exhausted** (only the R5 `orthogonalize` cap remains, marginal-deferred per OQ `l4-orthogonalize-cap-marginal-defer`, gated on a firm L4 Arnoldi consumer that does not exist), and tee the next-direction assessment up for the batch-14 meta-phase (fires after c048).
- **(c) §Vocabulary-cohort narrative motif refresh** (outer-driver sub-header `:39`): the `solve-monad` outer-driver cohort, previously "the outer-coordination surface the iterative-solve CAPs consume (both forthcoming cycle-048)", is now **anchored + consumed** by the two landed caps on disk, plus the `EigOutcome` clean-addition extension.

I do **NOT** author or rewrite D1's/D2's own dep-map rows or cohort bullets (producer-owned; they apply their own). I do **NOT** touch `L4/ksp_solve.md`, `L4/eigsolve.md`, or the L4-L3 theme.

### Arithmetic (stated explicitly, verified against on-disk + D1/D2 reports)

**Firm operator chapters in `book/src/L4/`:**
- On disk now (`ls book/src/L4/`): `krylov-step.md`, `iterate-while.md`, `iterate-while-with-prev.md`, `chebyshev.md` = **4 firm** (matches the current `(4 + …)` token).
- D1 adds `ksp_solve.md` (`status: firm`, verified ABSENT pre-dispatch — a genuine create).
- D2 adds `eigsolve.md` (`status: firm` — firm *as a cap*; it carries the same opaque-library obstruction L3 carries, but is a firm cap, NOT a qualified maturity; D2's frontmatter is `firmness: firm` and §Status is `firm`).
- **Post-cohort total: 4 + 2 = 6 firm operators.**

**`solve-monad` outer-driver vocabulary rows:**
- On disk now: `solve_loop`, `restart_cycle`, `Outcome` = **3** (matches the `(… + 3 outer-driver)` token + the sub-header `(3)`).
- D2 adds `EigOutcome` (its OWN new dep-map row — the clean-addition extension `EigOutcome = Continue | Done EigStatus`, alongside the canonical `Outcome`, NOT an override). D1 adds no new outer-driver vocabulary row (it consumes the existing three).
- **Post-cohort total: 3 + 1 = 4 outer-driver vocabulary rows.**

So `(4 + 3 outer-driver)` → `(6 + 4 outer-driver)`, and the sub-header `(3)` → `(4)`. Confirmed consistent with both producers' deferral notes (D1 §Open-questions "Firm-at-L4 step-vocabulary count becomes 5 … leaving `L4/eigsolve` as the sole remaining queued cap"; D2 §Open-questions "count becomes 6 … the outer-driver vocabulary gains the `EigOutcome` row (4 rows) … §Queued-at-L4 should empty").

## Proposed changes

### (a) + (c) Firm-at-L4 count tally + outer-driver narrative motif refresh

The §Vocabulary-cohort `Firm at L4` header carries the operator count; the outer-driver sub-header carries both the `(3)` outer-driver count and the "forthcoming cycle-048" motif. Both edits below.

```edit:book/src/L4/index.md
[old]:
**Firm at L4 (4 + 3 outer-driver)** — the typed-wrapper Krylov step kernel, the two value-threading loop combinators that drive it, and the fixed-degree polynomial smoother; plus the three `solve-monad` outer-driver vocabulary anchors:
[new]:
**Firm at L4 (6 + 4 outer-driver)** — the typed-wrapper Krylov step kernel, the two value-threading loop combinators that drive it, the fixed-degree polynomial smoother, and (cycle-048) the two iterative-solve outer-driver **caps** (`ksp_solve`, `eigsolve`); plus the four `solve-monad` outer-driver vocabulary anchors:
```

```edit:book/src/L4/index.md
[old]:
**`solve-monad` outer-driver vocabulary (3)** — the outer-coordination surface the iterative-solve CAPs (`L4/ksp_solve`, `L4/eigsolve`; both forthcoming cycle-048) consume. These are the `Solve = StateT SimState Identity` outer drivers per [`solve-monad`](../concepts/solve-monad.md); they sit *above* the `iterate-while` family (the per-step kernel-fold), coordinating the restart / convergence structure the kernel folds inside:
[new]:
**`solve-monad` outer-driver vocabulary (4)** — the outer-coordination surface the two iterative-solve CAPs **now consume**: [`ksp_solve`](./ksp_solve.md) and [`eigsolve`](./eigsolve.md) both landed firm cycle-048, anchoring and consuming this vocabulary (previously referenced from concept pages but not yet anchored by a per-operator cap). These are the `Solve = StateT SimState Identity` outer drivers per [`solve-monad`](../concepts/solve-monad.md); they sit *above* the `iterate-while` family (the per-step kernel-fold), coordinating the restart / convergence structure the kernel folds inside. The `eigsolve` cap (cycle-048) additionally registered `EigOutcome`, the clean-addition richer-termination extension of `Outcome` (a first-class partial-success arm, no `ksp_solve` analog):
```

### (b) §Queued-at-L4 prose flip

The two CAP chapters are landed this cycle, so the §Queued-at-L4 section no longer holds queued caps. The block below replaces the prose lead-in + the two bullets with a near-exhaustion statement, the marginal-deferred R5 `orthogonalize` note, and the batch-14 meta-phase hand-off.

```edit:book/src/L4/index.md
[old]:
**Queued at L4** — the two iterative-solve CAP chapters. The `solve-monad` outer-driver vocabulary (`solve_loop` / `restart_cycle` / `Outcome`) is now **anchored** (Firm-at-L4 cohort above; rows in the dep-map) — discharging the prior deferral for the outer-driver surface. What remains queued are the per-operator CAP chapters that consume this vocabulary:

- `L4/ksp_solve` *(cap; cycle-048 R2)* — the L4 outer-driver cap over [`L3/ksp_solve`](../L3/ksp_solve.md); consumes `solve_loop` / `restart_cycle` / `Outcome` (the `Outcome` is the sum-typed lift of the L3 soft-fail `Bool` per [`L3/ksp_solve`](../L3/ksp_solve.md):160). Gated on this anchor (now satisfied); not yet authored.
- `L4/eigsolve` *(cap; cycle-048+ R3)* — the L4 outer-driver cap over the `partial-obstruction` [`L3/eigsolve`](../L3/eigsolve.md); consumes the same outer-driver surface with a *richer* `Outcome`-sum termination (the partial-success `0 < converged < requested` case has no `ksp_solve` analog, per [`L3/eigsolve`](../L3/eigsolve.md):166 and [`L1/eigsolve`](../L1/eigsolve.md):78). Gated on this anchor (now satisfied); not yet authored. NOTE the L3 `eigsolve` entry's "no firm L4 cap exists" assertions remain TRUE this cycle — anchoring the outer-driver *rows* does not land the cap chapter.
[new]:
**Queued at L4 (0 — substantially complete)** — the two iterative-solve CAP chapters [`ksp_solve`](./ksp_solve.md) and [`eigsolve`](./eigsolve.md) **both landed firm cycle-048**, consuming the c047-anchored `solve-monad` outer-driver vocabulary; the queue is now empty of gated caps. The L4 frontier is **substantially complete / near-exhausted**: per the cycle-046 L4-survey read ("L4 mostly intentionally complete"), 13 of the 18 firm L3 operators are no-L4-by-design (the BLAS-1 / elementwise / smoother cohort whose L4 form would add no calculus beyond their firm L3 rendering), and after these two caps the only remaining L4-cap candidate is:

- `L4/orthogonalize` *(R5; marginal — deferred)* — would thread `{residual, coeffs}` through an Arnoldi step but adds no novel calculus beyond the MGS/CGS variant-split already recorded at [`L3/orthogonalize`](../L3/orthogonalize.md). **Deferred-marginal** per OQ `l4-orthogonalize-cap-marginal-defer` (R5): gated on a firm L4 Arnoldi consumer (a firm L4 `arnoldi_step` / GMRES-Arnoldi driver) that does not exist; it is not queued-as-gated-and-ready, only deferred-pending-a-consumer.

With the queue empty of ready caps, the **next forward-direction assessment is teed up for the batch-14 meta-phase** (fires after cycle-048): whether the L4 frontier is exhausted (the `l4-native-combinator-denominator-completeness-survey` reading), or width/depth consolidation is the next pick. This refresh does not pre-judge that assessment.
```

## Supporting evidence

- **Operators currently/post-cohort firm at L4** (with slugs): `krylov-step`, `iterate-while`, `iterate-while-with-prev`, `chebyshev` (on-disk, 4 firm) + `ksp_solve` (D1, new firm cap) + `eigsolve` (D2, new firm cap) = **6**. Verified the four on-disk chapters via `ls book/src/L4/` (no `ksp_solve.md`/`eigsolve.md` present pre-cohort — confirming both are genuine same-cycle creates landing before my finalize).
- **Outer-driver vocabulary rows** (with slugs): `solve_loop`, `restart_cycle`, `Outcome` (on-disk, c047, 3) + `EigOutcome` (D2's new clean-addition row) = **4**.
- **D1 deferral note** (`reports/.../harvester-L4-ksp-solve-cap/CYCLE.md` §Registration item (3) + §Open-questions): tally `(4 + 3 outer-driver)` ~:32 + §Queued prose flip ~:53-58 DEFERRED to D4.
- **D2 deferral note** (`reports/.../harvester-L4-eigsolve-cap/CYCLE.md` §Registration item (3) + §Open-questions): same tally + §Queued flip DEFERRED to D4; D2 owns its own `eigsolve` row, `EigOutcome` row, and cohort bullet.
- **D3 does not affect this count**: `reports/.../abstractor-ksp-solve-driver-dissolution/CYCLE.md` lands the L4>L3 theme in `L4-L3/` (slug `ksp-solve-driver-dissolution`), not in `L4/index.md`. The L4>L3 themes section of `L4/index.md` (the `**L4>L3 lowering themes**` sub-list :47-51) is NOT part of my consolidated count and is NOT owned by me this cycle — its refresh (adding the new `ksp-solve-driver-dissolution` row) belongs to D3's own registration or an integrator pass, per the dual-registration partition. I do not touch it.
- **R5 `orthogonalize` marginal-defer** verified against `scaffolding/open-questions.md:172` (`l4-orthogonalize-cap-marginal-defer` — "MARGINAL, defer. … adds no novel calculus beyond the MGS/CGS variant-split already recorded at L3 … *Trigger:* a firm L4 Arnoldi consumer … demands it") and `scaffolding/priorities.md:127` (the c046 survey ranked it R5-defer).

## Cross-reference integrity

- The two new `edit:` (a)+(c) blocks introduce live links `[`ksp_solve`](./ksp_solve.md)` and `[`eigsolve`](./eigsolve.md)` — both target files exist same-cycle (D1/D2 creates), so these are firm live links, not rough-in plain-text. The §Queued (b) block likewise links the two now-firm caps. Per the `rough-in-rows-must-be-plain-text-when-anchor-missing` convention, the only plain-text reference I keep is `L4/orthogonalize` (no anchor file — it is deferred-marginal, never created), which I write as plain text `L4/orthogonalize` (NOT a live link).
- My edits do not reference the L4>L3 theme by slug, so the D1/D3 slug-mismatch (`ksp-solve-outer-driver-dissolution` vs landed `ksp-solve-driver-dissolution`) does not touch any narrative I author. (Awareness-only, per the dispatch prompt; not my fix.)

## Open questions / caveats

- **L4-near-exhaustion assessment is teed up for the batch-14 meta-phase** (fires after cycle-048). With both iterative-solve caps landed and the §Queued section empty of ready caps, the L4 frontier is substantially complete (6 firm operators + 4 outer-driver vocabulary anchors; the c046 survey read L4 as "mostly intentionally complete"). The only remaining cap candidate, R5 `orthogonalize`, is deferred-marginal (gated on a non-existent firm L4 Arnoldi consumer). The meta-phase should assess the next forward direction — the `l4-native-combinator-denominator-completeness-survey` OQ (is the L4 vocabulary denominator now complete?) vs. width/depth consolidation vs. resuming the uniform L0→L4 climb elsewhere. My refresh records the near-exhaustion read but explicitly does NOT pre-judge the assessment.
- **`EigOutcome`-vs-canonical-`Outcome` disposition** (D2's OQ `outcome-sum-one-row-vs-per-cap-specialisation`, KEEP-OPEN). D2 registered `EigOutcome = Continue | Done EigStatus` as its OWN new L4 dep-map row — the **clean-addition** reading: an *extension* of the canonical c047 `Outcome` (`Continue | Done Bool`), NOT a contradiction (the `ksp_solve` cap still consumes the 3-arm `Outcome` unchanged). My count treats `EigOutcome` as a distinct fourth outer-driver vocabulary row, consistent with that reading. The batch-14 meta-phase should ratify the convention: **one-canonical-`Outcome` + per-cap `*Outcome` rows** (the current concrete shape — `Outcome` for `ksp_solve`, `EigOutcome` for `eigsolve`) vs. a **single polymorphic `Outcome α`** that subsumes both. If the meta-phase chooses the polymorphic form, the outer-driver count would re-collapse from 4 to 3 (one polymorphic `Outcome α` row) and my tally token would need a follow-up adjustment; I record this as a contingent count-dependency, not a blocker.
- **L4>L3 themes sub-list (`:47-51`) is NOT in my scope this cycle.** D3's new `ksp-solve-driver-dissolution` theme should add a row to that sub-list, but per the dual-registration partition that is D3's own registration / an integrator pass, not the consolidated-count owner's edit. I flag this so the integrator confirms the new L4>L3 theme is wired into the `**L4>L3 lowering themes**` sub-list (and that the slug there matches the landed `ksp-solve-driver-dissolution`) — it is not part of the (6 + 4) tally.

## Provenance

- Dispatched cycle-048 D4 (wave 3) as the sole `book/src/L4/index.md` consolidated-count owner.
- Consolidated aggregates only: the Firm-at-L4 tally `(4 + 3 outer-driver)` → `(6 + 4 outer-driver)`, the outer-driver sub-header `(3)` → `(4)` + narrative motif refresh, and the §Queued-at-L4 prose flip. D1/D2 own their own rows + bullets (not touched here).
- On-disk text read and matched verbatim before each `edit:` block (the §Vocabulary-cohort header, the outer-driver sub-header, the §Queued-at-L4 block — `book/src/L4/index.md` as of cycle-048, last modified Jun 1 10:09).
