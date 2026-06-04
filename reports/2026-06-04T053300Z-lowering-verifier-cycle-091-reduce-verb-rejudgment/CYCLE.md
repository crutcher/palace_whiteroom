---
agent: lowering-verifier
invoked_at: 2026-06-04T053300Z
scope: L4 reduce-verb re-judgment — gram_reduce + domain_energy_reduce, coupled to the matrix-weighted-norm firm flip (cycle-091 D3, batch-29 cascade wave-2)
status: pending
integrated_at: 2026-06-04T080000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-091 D3 (batch-29 LEAD cascade). domain_energy_reduce rough-in → firm (per-DOMAIN realization of the per-MODE eigenfreq_qfactor_reduce c082 disposition; both folded primitives now firm L1 — matrix-weighted-norm c091 + participation_ratio c077; firm-on-positive-structure escape); L4 firm 17→18 main / 21→22 grand, L4 rough-in 1→0 (cohort empty). gram_reduce STAYS rough-in (test-coverage-bounded) on its sole residual off-diagonal bilinear-form gate. Applied clean by integrator-per-report; build clean (cargo make book exit 0)."
inputs:
  - reports/2026-06-04T053300Z-cycle-planner-cycle-091/CYCLE.md (the cycle-091 plan; D3 scope)
  - reports/2026-06-04T053300Z-harvester-cycle-091-matrix-weighted-norm-firm-flip/CYCLE.md (D1 — matrix-weighted-norm now firm; the deferred L4/index lines)
  - book/src/L4/gram_reduce.md (re-judged; folds firm matrix-weighted-norm + still-rough-in bilinear-form)
  - book/src/L4/domain_energy_reduce.md (re-judged; folds firm matrix-weighted-norm + firm participation_ratio)
  - book/src/L1/bilinear-form.md §Status (confirmed still rough-in on disk — the gram_reduce residual gate)
  - reference/palace/test/unit/test-domainpostoperator.cpp (the existing postprocess test — gate (b) evidence)
---

# CYCLE: Re-judge gram_reduce + domain_energy_reduce after the matrix-weighted-norm firm flip (cycle-091 D3)

## PROMINENT VERDICT FOR D4 (load-bearing for the energy-fields column)

**`domain_energy_reduce` → FLIPS to `firm` this cycle.** Both folded L1 primitives are now firm (`matrix-weighted-norm` firm c091 + `participation_ratio` firm c077), the assembly is bare scalar arithmetic over those two firm halves with no inner-product-axiom content, and gate (b) (no dedicated per-domain test) does NOT independently gate firm under the firm-on-positive-structure escape — this is materially the `eigenfreq_qfactor_reduce` c082 disposition (the verb's own §Status names that contrast as exactly what clearing gate (a) would buy). **→ D4 SHOULD FLIP the `energy-fields` column `seed`→`firm`** (its OWN reduce verb `domain_energy_reduce` is now firm + its other constituents participation_ratio/matrix-weighted-norm firm = OWN composition all-firm).

**`gram_reduce` → STAYS `rough-in (test-coverage-bounded)`.** ONE gate discharged (matrix-weighted-norm firm), the RESIDUAL `bilinear-form` gate remains (still `rough-in` on disk). **→ D4 KEEPS electrostatic/magnetostatic/capacitance/inductance at `seed`** (own gate `gram_reduce` stays rough-in).

## Summary

I re-judged the two coupled L4 reduce verbs now that D1 flipped `matrix-weighted-norm` to `firm`. `gram_reduce` folds the now-firm `matrix-weighted-norm` (diagonal) AND the still-rough-in `bilinear-form` (off-diagonal); a reduction is as firm as its least-firm folded primitive, so it STAYS `rough-in (test-coverage-bounded)` with the gate NARROWED to the sole residual `bilinear-form` constituent. `domain_energy_reduce` folds the now-firm `matrix-weighted-norm` (per-domain energy numerator) AND the firm `participation_ratio` (quotient); BOTH folded primitives now firm + the assembly carries no inner-product-axiom content + the existing `test-domainpostoperator.cpp:83-93` energy-form coverage is supporting → the firm-on-positive-structure escape applies exactly as it did for the per-mode sibling `eigenfreq_qfactor_reduce` (firm c082), so it FLIPS to `firm`. I own the reduce-verb-dependent `book/src/L4/index.md` reconciliation D1 deferred (the rough-in cohort drops to **0**, the firm cohort rises **17→18**, the `domain_energy_reduce` bullet moves to the firm cohort, the `gram_reduce` joint label splits firm/rough-in). Top-level verdict: **partially-supported with one promotion enacted (domain_energy_reduce→firm) and one honest residual-gate hold (gram_reduce stays rough-in).**

## Per-citation audit

### gram_reduce — folded-primitive maturity

- **Citation**: `book/src/L1/matrix-weighted-norm.md` §Status (D1-flipped to `firm` this cycle)
  - **Theme claim**: gram_reduce's diagonal entry `xᵢᵀ K xᵢ` is the `matrix-weighted-norm` radicand (the `√`-dropped squared energy); the verb inherits its maturity.
  - **Found**: D1 enacted the flip to `firm` (D1 report §1; verb §Status now `firm`). The diagonal-consumer claim is correct (gram_reduce.md:54-65, law 2 `:141-145`).
  - **Verdict**: supports (the diagonal primitive is now firm).
  - **Notes**: the `√`-dropped relationship (gram_reduce reduces to the radicand `xᵢᵀ K xᵢ`, not `√(xᵢᵀ K xᵢ)`) is stated correctly at `:55-56` and law 2 `:142-143`; unaffected by the flip.

- **Citation**: `book/src/L1/bilinear-form.md:4` (`firmness: rough-in`) + `:321` (`rough-in (lower-layer-shared-vocabulary, cycle-010-wave-1)`)
  - **Theme claim**: gram_reduce's off-diagonal entry `xⱼᵀ K xᵢ` is the `bilinear-form` primitive (the fold element); the verb inherits its rough-in maturity.
  - **Found** (on-disk Read, this dispatch): `bilinear-form.md:4` `firmness: rough-in`; `:319-325` §Status `rough-in (lower-layer-shared-vocabulary, cycle-010-wave-1)`, promotion gated on a still-open variant-axis-coverage question. **CONFIRMED still rough-in.** (Per the plan, D2 narrated bilinear-form's joint-OQ; its own status is NOT touched this cycle — it stays rough-in.)
  - **Verdict**: supports (the off-diagonal primitive is genuinely still rough-in → the residual gate is real).
  - **Notes**: this is the load-bearing finding — the residual gate is NOT a forcing-avoidance fiction; bilinear-form is rough-in on disk with its own independent (lower-layer-shared-vocabulary) gate.

### domain_energy_reduce — folded-primitive maturity + gate (b)

- **Citation**: `book/src/L1/matrix-weighted-norm.md` §Status (D1-flipped to `firm`)
  - **Theme claim**: the per-domain energy numerator `energyᵢ = ½⟨field, M_idx field⟩` is the `matrix-weighted-norm`-squared radicand restricted to one domain (`B = M_idx`); the verb's rough-in is INHERITED from it (domain_energy_reduce.md:7, :206-208, §Status point 1 :276-277).
  - **Found**: D1 enacted firm. The "matrix-weighted-norm-squared at B = M_idx" relationship is correct (law 2 `:149-153`; energy form `0.5 * LocalDot(field, M_idx·field)` at `domainpostoperator.cpp:262-274`).
  - **Verdict**: supports — gate (a) (the verb's §Status promotion-route point (a)) is DISCHARGED.

- **Citation**: `book/src/L1/participation_ratio.md` (firm, c077) + `:188-191`
  - **Theme claim**: the quotient half `pᵢ = energyᵢ/e_total` is the firm `participation_ratio`; `:188-191` disclaims the numerator-energy reduction as "named not authored" = this verb.
  - **Found** (on-disk Read, this dispatch): `participation_ratio.md:188-191` confirmed — firm "as the quotient", and critically `:184-186` establishes the governing precedent: "syntactic-identity quotient laws are not test-gated... bare arithmetic on positive source" (the `apply_linop`/`eigsolve`/firm-on-positive-structure precedent). The "named not authored" disclaimer (`:188-189`) names this verb as the home for the numerator reduction.
  - **Verdict**: supports — the quotient half is firm AND the precedent for "syntactic-identity map laws are not test-gated" is established right here.

- **Citation**: `reference/palace/test/unit/test-domainpostoperator.cpp:83-93` (gate (b) evidence)
  - **Theme claim** (§Status point 2, promotion-route (b)): no dedicated per-domain energy-participation test; the existing test asserts only the whole-domain `GetElectricFieldEnergy`; the batch-24 ruling makes the 2nd gate dischargeable by a lowering-verifier law-confidence pass citing this existing postprocess coverage.
  - **Found** (on-disk, this dispatch — `citecheck --anchor` + grep): `test-domainpostoperator.cpp:83` calls `GetElectricFieldEnergy(*E_field)` (the WHOLE-domain total `e_total`), `:90-93` asserts the SI energy `U = ½·ε₀·E₀²·sx·sy·sz` (`WithinRel(…, 0.01)`). I grepped the entire file (95 lines) and ALL of `test/unit/`: **NO call to `GetDomainElectricFieldEnergy` / `GetDomainMagneticFieldEnergy` anywhere** — the per-domain restricted form and the participation assembly are entirely test-uncovered; the test covers only the energy-FORM constituent at the whole-domain (denominator) instance.
  - **Verdict**: partially-supports — the test supports the energy-FORM constituent (whole-domain instance), NOT the per-domain reduction. This is the honest characterization the verb's §Status already gives (`:281-285`: "asserts the WHOLE-domain SI energy ... but NOT the per-domain reduction + participation assembly"). It is SUPPORTING evidence, not the firming basis.
  - **Notes**: gate (b) does NOT independently block firm — see §Algebraic laws below. The firming basis is the escape (both folded primitives firm + syntactic-identity map laws), not this test; the test is the energy-form witness that the escape's positive-structure rests on.

## Applicability conditions

### gram_reduce

- **Condition**: `K` symmetric/SPD (load-bearing for `G`-symmetry, `:98-99`, `:136`).
  - **Verifiable**: yes — read off the two positive PostprocessTerminals loops (`M_elec`/`M_mag` are SPD energy operators); unaffected by the flip.
  - **Found counter-example?**: no.
- **Condition**: `w i j = w j i` (symmetric weight, `:106`).
  - **Verifiable**: yes — both witnesses (`w = 1`; `w = 1/(IᵢIⱼ)`) are symmetric.
  - **Found counter-example?**: no.
- **Condition** (the gating one): the folded L1 primitives are firm.
  - **Verifiable**: yes — matrix-weighted-norm now firm; bilinear-form still rough-in on disk.
  - **Found counter-example?**: N/A — this is precisely the residual gate (bilinear-form NOT firm) that keeps gram_reduce rough-in.

### domain_energy_reduce

- **Condition**: `M_idx` SPD per domain (energyᵢ real ≥ 0, law 2 `:149-153`).
  - **Verifiable**: yes — read off `domainpostoperator.cpp:262-274` (`0.5 * LocalDot`, null-operator → 0); the same SPD-energy form matrix-weighted-norm rests on.
  - **Found counter-example?**: no.
- **Condition**: `Σ pᵢ = 1` is CONFIG-CONDITIONAL (holds only when configured domains partition the field support, `:166-174`).
  - **Verifiable**: yes — correctly stated as a non-unconditional-law / variant-axis precondition; does NOT gate the verb's shape or maturity (it's a per-config property, not a verb law).
  - **Found counter-example?**: N/A — explicitly not claimed as an identity.
- **Condition** (the formerly-gating one): both folded primitives firm.
  - **Verifiable**: yes — matrix-weighted-norm firm c091 + participation_ratio firm c077.
  - **Found counter-example?**: NO — this is exactly the condition that NOW HOLDS and clears the firm flip (the verb's §Status `:295-298` says it "stays rough-in because its OWN per-domain numerator ... is itself rough-in" — that condition is removed).

## Algebraic laws

### gram_reduce (STAYS rough-in — laws structurally firm, maturity capped by bilinear-form)

| Law | Holds on operators? |
|---|---|
| 1 Symmetry `Gⱼᵢ = Gᵢⱼ` (`:136-140`) | Holds — `bilinear_form xⱼ K xᵢ = bilinear_form xᵢ K xⱼ` for symmetric `K`; read-off identity. |
| 2 Diagonal-is-self-bilinear (`:141-145`) | Holds — `entry K xs i i = matrix_weighted_norm (xs!!i) K = bilinear_form (xs!!i) K (xs!!i)` modulo `√`; the now-firm diagonal-consumer identity. |
| 3 Weight factoring / bilinearity (`:146-148`) | Holds — read-off. |
| 4 Grid-map independence (`:149-151`) | Holds — embarrassingly-parallel, no inter-entry state. |

All four laws are syntactic identities on the fold structure (structure firm-on-positive-structure). **The maturity cap is NOT a law failure** — it is that the off-diagonal FOLD ELEMENT `bilinear-form` is itself rough-in (its laws stated-but-test-unconfirmed under its own `lower-layer-shared-vocabulary` gate). A reduction is as firm as its least-firm folded primitive → gram_reduce STAYS `rough-in (test-coverage-bounded)`. Honest outcome: one gate discharged (matrix-weighted-norm firm), one remains (bilinear-form rough-in).

### domain_energy_reduce (FLIPS firm — every law a syntactic identity over two firm halves)

| Law | Holds on operators? |
|---|---|
| 1 Map-independence / concatenation-homomorphism (`:143-148`) | Holds — read off the per-domain `emplace_back` loop (`postoperator.cpp:1036-1042`) carrying no accumulator; no inter-domain state. |
| 2 Per-domain energy = domain-restricted matrix-weighted-norm-squared (`:149-153`) | Holds — `½⟨field, M_idx field⟩` is the matrix-weighted-norm radicand at `B = M_idx`, halved (`domainpostoperator.cpp:262-274`). The folded primitive is now FIRM. |
| 3 Numerator-scale-homogeneity in the quotient (`:154-156`) | Holds — inherited from the firm `participation_ratio` numerator-linearity law. |
| 4 Shared-denominator invariance (`:157-161`) | Holds — `e_total` computed once (`postoperator.cpp:1033/1058`), divided into each numerator; the firm `participation_ratio` denominator-shared-invariance law, per-domain instance. |
| 5 Total-guard totality `e_total ≤ 0 ⇒ pᵢ = 0` (`:162-164`) | Holds — a literal edge-case in the scalar map (the chosen uniform denominator guard, `:182-199`), not an error arm; parallel to `eigenfreq_qfactor_reduce`'s `κ=0 ⇒ Q=∞`. |

**Firm-flip warrant.** Every law is a read-off syntactic identity on the per-domain map structure over the positive `MeasureDomainFieldEnergy` loop (`postoperator.cpp:1021-1099`, citecheck `[ok]`). Both folded primitives now have firm L1 homes (matrix-weighted-norm c091 + participation_ratio c077). The eigenpair→`(energyᵢ, pᵢ)` assembly is bare scalar arithmetic over those two firm halves with **no inner-product-axiom content** (the matrix-weighted-norm contrast that previously blocked it is removed — the norm's inner-product axioms are now discharged at the firm L1 home). This is materially IDENTICAL to the per-MODE sibling `eigenfreq_qfactor_reduce` (firm c082, both folded primitives firm + no inner-product-axiom content in the assembly). Gate (b) — the missing dedicated per-domain test — does NOT independently gate firm under the firm-on-positive-structure escape: syntactic-identity map laws over firm constituents are not test-gated (the `participation_ratio.md:184-186` / `apply_linop` / `eigsolve` precedent, established right at the quotient primitive's own firming). The existing `test-domainpostoperator.cpp:83-93` whole-domain energy-form assertion is supporting positive-structure evidence, NOT the firming basis. → **FLIP to `firm`.**

## Proposed changes

### Coordination note (read FIRST)

- **gram_reduce.md / domain_energy_reduce.md**: I own these two files' own §Status + frontmatter + the matrix-weighted-norm folded-primitive labels inside them. No overlap with any other dispatch.
- **L4/index.md**: D1 is SOLE owner of this file. D1 already edited `:98`'s **Folds-cell** standalone matrix-weighted-norm label to `(firm c091 — …)` (D1 report §3a) and DEFERRED to me: `:57` (rough-in count header), `:59` (domain_energy_reduce bullet), `:98` **Status-cell** gating rationale, `:102` (gram_reduce joint label). My L4/index edits below are written to apply AFTER D1's edits — every `old_string` matches the post-D1 on-disk text (I do NOT re-touch the `:98` Folds-cell D1 already flipped; I touch only the `:98` **Status-cell** rationale, a different part of the same row). Because my firm verdict ALSO requires incrementing the firm-cohort count (`:32` 17→18) and inserting a `domain_energy_reduce` firm-cohort bullet (the firm-side coupling of moving it out of the rough-in cohort), I propose those `:32`/firm-cohort-bullet edits too and flag them explicitly as the firm-side half of the deferred reconciliation, for the integrator to apply as the unified D3-coordinated L4/index pass within D1's single-owner file. **Same-line coordination flagged: NONE of my L4/index `old_string`s collide with D1's `:98` Folds-cell edit — D1 touched the Folds cell, I touch the Status cell + the count headers + the `:102` joint label + the `:59` bullet, all distinct text spans.**

### 1. book/src/L4/gram_reduce.md — STAYS rough-in; narrow the gate to the residual bilinear-form, re-anchor the matrix-weighted-norm folded-primitive labels to firm

**1a. Frontmatter `consumes:` (`:6`) — matrix-weighted-norm label → firm; PRESERVE bilinear-form rough-in (`:7`).**

```edit:book/src/L4/gram_reduce.md
<<<OLD :6>>>
  - book/src/L1/matrix-weighted-norm.md (rough-in — the diagonal self-bilinear xᵢᵀ K xᵢ; the diagonal CONSUMER, the xⱼ=xᵢ specialization of the off-diagonal bilinear)
<<<NEW :6>>>
  - book/src/L1/matrix-weighted-norm.md (firm c091 — the diagonal self-bilinear xᵢᵀ K xᵢ; the diagonal CONSUMER, the xⱼ=xᵢ specialization of the off-diagonal bilinear)
<<<END>>>
```

(`:7` bilinear-form `(rough-in — the off-diagonal cross-bilinear …)` is UNCHANGED — bilinear-form stays rough-in.)

**1b. Context (`:54-59`) — re-narrate the diagonal as firm, off-diagonal stays rough-in.**

```edit:book/src/L4/gram_reduce.md
<<<OLD :54-59>>>
- the diagonal entry `xᵢᵀ K xᵢ` is the rough-in L1
  [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (`√` dropped — `gram_reduce`
  reduces to the *squared* energy `xᵢᵀ K xᵢ = 2Uₑ/ₘ(xᵢ)`, the matrix-weighted-norm's
  radicand);
- the off-diagonal entry `xⱼᵀ K xᵢ` is the rough-in L1
  [`bilinear-form`](../L1/bilinear-form.md) (`xᴴ M y` at `M = K`).
<<<NEW :54-59>>>
- the diagonal entry `xᵢᵀ K xᵢ` is the now-**firm** (c091) L1
  [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (`√` dropped — `gram_reduce`
  reduces to the *squared* energy `xᵢᵀ K xᵢ = 2Uₑ/ₘ(xᵢ)`, the matrix-weighted-norm's
  radicand);
- the off-diagonal entry `xⱼᵀ K xᵢ` is the still-rough-in L1
  [`bilinear-form`](../L1/bilinear-form.md) (`xᴴ M y` at `M = K`) — the sole remaining
  rough-in folded primitive, the residual gate (see §Status).
<<<END>>>
```

**1c. Dependencies (`:195-198`) — matrix-weighted-norm label → firm.**

```edit:book/src/L4/gram_reduce.md
<<<OLD :195-198>>>
- [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (rough-in) — the diagonal
  self-bilinear (radicand); the diagonal consumer.
- [`bilinear-form`](../L1/bilinear-form.md) (rough-in) — the off-diagonal cross-bilinear;
  the fold element.
<<<NEW :195-198>>>
- [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (firm c091) — the diagonal
  self-bilinear (radicand); the diagonal consumer.
- [`bilinear-form`](../L1/bilinear-form.md) (rough-in) — the off-diagonal cross-bilinear;
  the fold element. **The sole remaining rough-in folded primitive — the residual gate.**
<<<END>>>
```

**1d. §Status (`:225-248`) — STAYS rough-in; narrow the gate to bilinear-form only, record the matrix-weighted-norm gate discharged.**

```edit:book/src/L4/gram_reduce.md
<<<OLD :234-248>>>
the *structure* would satisfy the firm-on-positive-structure escape. BUT two factors
gate it to `rough-in (test-coverage-bounded)`:
1. the per-entry building blocks it folds — [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)
   and [`bilinear-form`](../L1/bilinear-form.md) — are themselves **rough-in** (their
   laws are stated-but-test-unconfirmed), so the entry inherits their reduced maturity;
2. there is **no dedicated Palace unit test** for the Gram reduction (the
   PostprocessTerminals bodies are integration-level, exercised only through the full
   `Solve(mesh)` driver), so the reduction-level laws are test-unconfirmed.

Promotion route: (a) the L1 [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) +
[`bilinear-form`](../L1/bilinear-form.md) primitives firm up, AND (b) a dedicated
family-pair Gram-reduction test OR a lowering-verifier pass raising the fold-law
confidence to `inner_product`-equivalent. (Contrast the firm-on-positive-structure
`frequency_sweep` / `fe_assemble`, whose folded primitives are themselves firm —
`gram_reduce`'s primitives are rough-in, which is the firm-vs-rough-in distinction
here.)
<<<NEW :234-248>>>
the *structure* would satisfy the firm-on-positive-structure escape. BUT the entry
inherits the maturity of its least-firm folded primitive — and after the cycle-091
matrix-weighted-norm firm flip, **one of the two folded gates is discharged and one
remains**:
1. the diagonal building block [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)
   is now **firm** (c091, the batch-29 firm-flip-and-cascade wave — both norm-axiom
   law-sides discharged on the firm-on-positive-structure escape) — **gate discharged**;
2. the off-diagonal building block [`bilinear-form`](../L1/bilinear-form.md) is still
   **rough-in** (its own `rough-in (lower-layer-shared-vocabulary, cycle-010-wave-1)`
   status, gated on a narrow-variant-axis-coverage question — confirmed on disk
   `bilinear-form.md:4,:321` this cycle) — **the sole RESIDUAL gate**, so the entry
   stays at its maturity;
3. there is additionally **no dedicated Palace unit test** for the Gram reduction (the
   PostprocessTerminals bodies are integration-level, exercised only through the full
   `Solve(mesh)` driver), so the reduction-level laws are test-unconfirmed.

A reduction is as firm as its least-firm folded primitive, so `gram_reduce` STAYS
`rough-in (test-coverage-bounded)` — NOT a forcing: the bilinear-form off-diagonal is
genuinely rough-in on disk (this is the honest partial outcome of the cascade, one of
two folded gates cleared).

Narrowed promotion route (cycle-091): the matrix-weighted-norm diagonal gate is
DISCHARGED (firm c091); the remaining gates are (a) the off-diagonal
[`bilinear-form`](../L1/bilinear-form.md) primitive firms up (its own
`lower-layer-shared-vocabulary` / variant-axis-coverage gate — a separate
dischargeability question, NOT in this cycle's scope), AND (b) a dedicated family-pair
Gram-reduction test OR a lowering-verifier pass raising the fold-law confidence to
`inner_product`-equivalent. (Contrast the per-DOMAIN sibling
[`domain_energy_reduce`](./domain_energy_reduce.md), which firmed this same cycle
because BOTH its folded primitives are now firm — matrix-weighted-norm c091 +
participation_ratio c077; `gram_reduce`'s off-diagonal bilinear-form is the one folded
primitive still rough-in, which is the firm-vs-rough-in distinction here.)
<<<END>>>
```

### 2. book/src/L4/domain_energy_reduce.md — FLIP to firm + verified_against block

**2a. Frontmatter `firmness:` (`:4`) → firm.**

```edit:book/src/L4/domain_energy_reduce.md
<<<OLD :4>>>
firmness: rough-in
<<<NEW :4>>>
firmness: firm
<<<END>>>
```

**2b. Frontmatter `consumes:` matrix-weighted-norm label (`:7`) → firm; gate-discharge narration.**

```edit:book/src/L4/domain_energy_reduce.md
<<<OLD :7>>>
  - book/src/L1/matrix-weighted-norm.md (rough-in (test-coverage-bounded) — the ½⟨field, M_i field⟩ domain-restricted SPD energy form, the first folded primitive; the verb's rough-in maturity is inherited from it. Cycle-080 lowering-verifier audit: its radicand constituent ⟨field, M_i field⟩ + ½ is now positively test-covered by test-domainpostoperator.cpp:75-93, but its √-overload named entry point linalg::Norml2(comm,x,B,Bx) stays test-uncovered, so the token is unchanged)
<<<NEW :7>>>
  - book/src/L1/matrix-weighted-norm.md (firm c091 — the ½⟨field, M_i field⟩ domain-restricted SPD energy form, the first folded primitive; promoted rough-in (test-coverage-bounded)→firm by the batch-29 firm-flip-and-cascade wave on the firm-on-positive-structure escape, so this verb's former inherited-rough-in gate is now DISCHARGED. The radicand constituent ⟨field, M_i field⟩ + ½ is positively test-covered by test-domainpostoperator.cpp:83-93 at the whole-domain instance; the √-overload entry point's missing test is judged redundant under the escape per the batch-28 meta-phase)
<<<END>>>
```

**2c. Dependencies matrix-weighted-norm label (`:206-208`) → firm.**

```edit:book/src/L4/domain_energy_reduce.md
<<<OLD :206-208>>>
- [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (rough-in (test-coverage-bounded)) — the
  domain-restricted SPD energy form `½⟨field, M_idx field⟩` this reduction folds as the per-domain
  numerator (the first folded primitive; the verb's `rough-in` maturity is INHERITED from it).
<<<NEW :206-208>>>
- [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (firm c091) — the
  domain-restricted SPD energy form `½⟨field, M_idx field⟩` this reduction folds as the per-domain
  numerator (the first folded primitive; promoted to firm by the batch-29 firm-flip-and-cascade wave,
  discharging this verb's former inherited-rough-in gate — both folded primitives are now firm).
<<<END>>>
```

**2d. §Status (`:268-300`) — FLIP to firm; restate as enacted with the escape warrant.**

```edit:book/src/L4/domain_energy_reduce.md
<<<OLD :268-300>>>
## Status

`rough-in`. **Reasoning (warrant-first):** the combinator's **structure** is read directly off the
positive `MeasureDomainFieldEnergy` per-domain loop (`postoperator.cpp:1021-1099`) — the per-domain map,
the domain-restricted energy form, the participation quotient, the shared denominator — and the map laws
(§Algebraic laws) are syntactic identities on that per-domain map. So the *structure* approaches the
firm-on-positive-structure escape. But two factors gate it to `rough-in` (D4 flag #1):

1. the per-domain numerator it folds — the domain-restricted energy form `½⟨field, M_idx field⟩` — is the
   [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) `rough-in (test-coverage-bounded)` primitive
   (restricted to one domain attribute), so the verb cannot exceed that constituent's maturity (the firm
   [`participation_ratio`](../L1/participation_ratio.md) quotient half is necessary but not sufficient — a
   reduction is as firm as its least-firm folded primitive);
2. there is **no dedicated Palace unit test** for the per-domain energy-participation readout (the
   `MeasureDomainFieldEnergy` body is integration-level, exercised only through a full driver
   `Solve(mesh)`; the existing `test-domainpostoperator.cpp:83` asserts the WHOLE-domain SI energy
   `GetElectricFieldEnergy`, supporting the energy-form constituent but NOT the per-domain reduction +
   participation assembly), so the reduction-level laws are test-unconfirmed.

Promotion route: (a) firm up the folded domain-restricted [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)
energy form, AND (b) a dedicated per-domain energy-participation test OR a lowering-verifier pass raising
the map-law confidence to `inner_product`-equivalent (the batch-24 meta-phase ruled the 2nd gate is
dischargeable in write-scope by a `find-tests-for-region` pass CITING the existing
`test-domainpostoperator.cpp` postprocess coverage). (Contrast the per-mode sibling
[`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md), now `firm` (c082): it cleared the
firm-on-positive-structure escape precisely because BOTH its folded primitives have firm L1 homes —
[`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) (c080) and the firm
[`participation_ratio`](../L1/participation_ratio.md) (c077). `domain_energy_reduce` stays `rough-in`
because its OWN per-domain numerator — the folded domain-restricted
[`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) energy form — is itself `rough-in
(test-coverage-bounded)` at the √-overload entry point (gate (a) above), so the same escape does NOT yet
apply here; the firm sibling is the contrast that shows what clearing gate (a) would buy, NOT a peer at
the same maturity.)
<<<NEW :268-300>>>
## Status

`firm` — promoted from `rough-in` by the cycle-091 batch-29 firm-flip-and-cascade wave (D3
lowering-verifier law-confidence pass), coupled to the [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)
firm flip. **Reasoning (warrant-first):** the combinator's **structure** is read directly off the
positive `MeasureDomainFieldEnergy` per-domain loop (`postoperator.cpp:1021-1099`) — the per-domain map,
the domain-restricted energy form, the participation quotient, the shared denominator — and every map law
(§Algebraic laws) is a syntactic identity on that per-domain map. The two factors that previously gated it
to `rough-in` are now both addressed:

1. **The formerly-rough-in folded numerator is now firm.** The per-domain numerator it folds — the
   domain-restricted energy form `½⟨field, M_idx field⟩` — is the
   [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) primitive (restricted to one domain attribute,
   `B = M_idx`), which was promoted to **firm** (c091) on the firm-on-positive-structure escape (both
   norm-axiom law-sides discharged). So **BOTH** folded primitives now have firm L1 homes —
   matrix-weighted-norm (c091) AND the firm [`participation_ratio`](../L1/participation_ratio.md) (c077) —
   removing the "least-firm folded primitive" cap that held the verb at rough-in.
2. **The missing dedicated test does NOT independently gate firm under the escape.** The
   `MeasureDomainFieldEnergy` body is integration-level, and the existing
   `test-domainpostoperator.cpp:83-93` asserts the WHOLE-domain SI energy `GetElectricFieldEnergy` (the
   energy-FORM constituent at the denominator instance, citecheck-confirmed this cycle — NO unit test
   calls the per-domain `GetDomainElectric/MagneticFieldEnergy` restricted form), so it is SUPPORTING
   positive-structure evidence, not the firming basis. The escape (CLAUDE.md §Methodology invariants, the
   `rough-in (test-coverage-bounded)` bullet) makes the missing per-domain test REDUNDANT: every map law
   is a syntactic identity over two firm halves, and syntactic-identity map laws over firm constituents
   are not test-gated (the [`participation_ratio.md`](../L1/participation_ratio.md):184-186 /
   `apply_linop` / `eigsolve` precedent). There is NO law for which that test is the only evidence — the
   batch-24 meta-phase ruling that the 2nd gate is dischargeable via the existing postprocess coverage is
   the in-scope route, exercised here.

This is materially the **same disposition as the per-MODE sibling**
[`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md) (firm c082): BOTH its folded primitives have
firm L1 homes ([`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) c080 +
[`participation_ratio`](../L1/participation_ratio.md) c077) and the per-mode assembly is bare scalar
arithmetic over two firm halves with no inner-product-axiom content. `domain_energy_reduce` now shares
that property exactly — its per-domain numerator's inner-product axioms are discharged at the firm
matrix-weighted-norm L1 home, and the `(energyᵢ, pᵢ)` assembly is bare scalar arithmetic over two firm
halves (the matrix-weighted-norm-squared energy form + the participation quotient) introducing no
inner-product-axiom content of its own. The earlier contrast (the firm sibling shows "what clearing gate
(a) would buy") is now realized: gate (a) is cleared, and the escape applies here as it did there.

(The off-diagonal contrast is [`gram_reduce`](./gram_reduce.md), which STAYS rough-in this same cycle
because its off-diagonal folded primitive [`bilinear-form`](../L1/bilinear-form.md) is still rough-in —
the firm-vs-rough-in distinction is which folded primitives are firm: `domain_energy_reduce`'s two are
both firm, `gram_reduce`'s off-diagonal bilinear-form is not.)
<<<END>>>
```

**2e. Append the `verified_against:` block at end of file (after `:378`).**

```edit:book/src/L4/domain_energy_reduce.md
[append at end of file]
```yaml
verified_against:
  - citation: book/src/L1/matrix-weighted-norm.md (§Status, firm c091 — D1)
    verdict: supports
    audited_at: 2026-06-04T053300Z
    note: first folded primitive (per-domain energy numerator, matrix-weighted-norm-squared at B=M_idx) now firm; the former inherited-rough-in gate is discharged
  - citation: book/src/L1/participation_ratio.md (firm c077, :184-191)
    verdict: supports
    audited_at: 2026-06-04T053300Z
    note: second folded primitive (the energyᵢ/e_total quotient) firm; :184-186 establishes that syntactic-identity quotient/map laws over firm constituents are not test-gated
  - citation: reference/palace/palace/models/postoperator.cpp:1021-1099
    verdict: supports
    audited_at: 2026-06-04T053300Z
    note: MeasureDomainFieldEnergy per-domain loop — the positive structure; every map law is a read-off syntactic identity on it (citecheck OK)
  - citation: reference/palace/palace/models/domainpostoperator.cpp:262-274
    verdict: supports
    audited_at: 2026-06-04T053300Z
    note: the 0.5*LocalDot(field, M_idx·field) domain-restricted energy form (matrix-weighted-norm-squared at B=M_idx), :274 the 0.5*dot return (citecheck OK)
  - citation: reference/palace/test/unit/test-domainpostoperator.cpp:83-93
    verdict: partially-supports
    audited_at: 2026-06-04T053300Z
    note: asserts the WHOLE-domain GetElectricFieldEnergy SI energy (the energy-FORM constituent, denominator instance) — supporting positive-structure evidence, NOT the per-domain restriction or participation assembly; the missing per-domain test is redundant under the firm-on-positive-structure escape
```
```

### 3. book/src/L4/index.md — reduce-verb reconciliation (D1 deferred; applies AFTER D1)

**3a. `:57` rough-in count header → (0); the cohort is now empty, the domain_energy_reduce bullet moves to the firm cohort.**

```edit:book/src/L4/index.md
<<<OLD (head of :57)>>>
**Rough-in at L4 (1)** — the per-domain energy-table reduction verb (gated on its `matrix-weighted-norm` rough-in folded primitive + no per-domain test), awaiting law confirmation. The eigenmode per-mode reduction [`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md) **promoted to `firm` cycle-082**
<<<NEW (head of :57)>>>
**Rough-in at L4 (0)** — the rough-in cohort is now empty: the per-domain energy-table reduction verb [`domain_energy_reduce`](./domain_energy_reduce.md) **promoted to `firm` cycle-091** (the batch-29 firm-flip-and-cascade wave — its formerly-rough-in folded numerator [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) firmed this cycle, so BOTH its folded primitives now have firm L1 homes — matrix-weighted-norm c091 + [`participation_ratio`](../L1/participation_ratio.md) c077 — and the firm-on-positive-structure escape applies exactly as it did for its per-MODE sibling), moving to the firm cohort above. The eigenmode per-mode reduction [`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md) **promoted to `firm` cycle-082**
<<<END>>>
```

**3b. `:59` domain_energy_reduce bullet — MOVE from the rough-in cohort to the firm cohort.** The bullet currently sits under the (now-empty) rough-in header. Remove it from `:59` and insert a firm-cohort bullet (after the `eigenfreq_qfactor_reduce` firm-cohort bullet at `:49`, its per-MODE sibling).

REMOVE from `:59` (the rough-in cohort):

```edit:book/src/L4/index.md
<<<OLD :59 (delete this bullet entirely)>>>
- [`domain_energy_reduce`](./domain_energy_reduce.md) *(rough-in; cycle-079 D3)* — the **per-domain energy-table reduction combinator**: reduce a single solution field against a configured domain-operator map `{idx → M_idx}` into a rank-1 per-domain `(energyᵢ, pᵢ)` scalar table, where `energyᵢ = ½⟨field, M_idx field⟩` is the domain-RESTRICTED SPD energy form and `pᵢ = energyᵢ / e_total` is the per-domain participation. The **reduce-to-scalar-table** member of the L4 algebra-of-folds — the **per-DOMAIN sibling** of the per-MODE [`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md), completing the family's rank-1 scalar-table corner (rank-1 per-domain table, NOT a [`gram_reduce`](./gram_reduce.md) family-PAIR grid — single field, not a family). It is **genuine NEW spine vocabulary, NOT a [`participation_ratio`](../L1/participation_ratio.md) fold-inline** — the c079 D4 confirm-probe returned DISTINCT-VERB-WARRANTED because the per-domain numerator is itself a domain-restricted SPD energy reduction (the load-bearing content), so the verb folds **two** L1 primitives per row (the [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)-squared restricted energy AND the firm [`participation_ratio`](../L1/participation_ratio.md) quotient); the firm `participation_ratio.md:188-191` disclaims that numerator-energy reduction as out-of-scope "named not authored" vocabulary = THIS verb. Pure value-producing reduction (no `Solve` monad / carry / predicate — a post-processing readout), driver-AGNOSTIC (the SAME reduction reduces any field-bearing driver's field). The output-product half of the [`energy-fields`](../feature/energy-fields.L4.md) composition root reaching the L4 surface. Status `rough-in`: structure firm-on-positive-structure on the `MeasureDomainFieldEnergy` per-domain loop (`postoperator.cpp:1021-1099`), but gated because the folded domain-restricted energy form is the [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) `rough-in (test-coverage-bounded)` primitive AND there is no dedicated per-domain energy-participation test (the firm `participation_ratio` half is necessary but not sufficient — a reduction is as firm as its least-firm folded primitive). The `Σ pᵢ = 1` partition-of-unity is **config-conditional** (holds only when the configured domains partition the field support), NOT an unconditional identity. **Scope: 1-of-1 output-product, driver-agnostic by design** (the disciplined-cross-pipeline-mining-gate does not apply — single-output-product reduction verb, like [`sparameter_reduce`](./sparameter_reduce.md)). Harvested cycle-079 D3 from OQ `domain_energy_reduce-l4-verb-needs-authoring` + the c079 D4 DISTINCT-VERB-WARRANTED probe.
<<<NEW :59 (the bullet is removed entirely from the rough-in cohort)>>>
<<<END>>>
```

INSERT into the firm cohort, after the `eigenfreq_qfactor_reduce` firm-cohort bullet (`:49`, its per-MODE sibling):

```edit:book/src/L4/index.md
<<<OLD (end of the :49 eigenfreq_qfactor_reduce firm bullet — anchor on its closing sentence)>>>
**Scope: 1-of-1 — the eigenmode pipeline's output product.** Harvested cycle-075 D3; promoted firm cycle-082 D2.
<<<NEW>>>
**Scope: 1-of-1 — the eigenmode pipeline's output product.** Harvested cycle-075 D3; promoted firm cycle-082 D2.
- [`domain_energy_reduce`](./domain_energy_reduce.md) — the **per-domain energy-table reduction combinator**: reduce a single solution field against a configured domain-operator map `{idx → M_idx}` into a rank-1 per-domain `(energyᵢ, pᵢ)` scalar table, `energyᵢ = ½⟨field, M_idx field⟩` (the domain-RESTRICTED SPD energy form) and `pᵢ = energyᵢ / e_total` (the per-domain participation). The **reduce-to-scalar-table** member of the L4 algebra-of-folds — the **per-DOMAIN sibling** of the per-MODE [`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md), completing the family's rank-1 scalar-table corner (rank-1 per-domain table, NOT a [`gram_reduce`](./gram_reduce.md) family-PAIR grid — single field, not a family). **Genuine NEW spine vocabulary, NOT a [`participation_ratio`](../L1/participation_ratio.md) fold-inline** (c079 D4 confirm-probe DISTINCT-VERB-WARRANTED): the per-domain numerator is itself a domain-restricted SPD energy reduction, so the verb folds **two** L1 primitives per row (the [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)-squared restricted energy AND the firm [`participation_ratio`](../L1/participation_ratio.md) quotient). Pure value-producing reduction (no `Solve` monad / carry / predicate), driver-AGNOSTIC. The output-product half of the [`energy-fields`](../feature/energy-fields.L4.md) composition root reaching the L4 surface. Status `firm` (promoted rough-in→firm cycle-091 by the batch-29 firm-flip-and-cascade wave on the **firm-on-positive-structure escape**: every map law is a read-off syntactic identity on the positive `MeasureDomainFieldEnergy` per-domain loop `postoperator.cpp:1021-1099`, and BOTH folded primitives now have firm L1 homes — matrix-weighted-norm c091 + participation_ratio c077 — so the assembly is bare scalar arithmetic over two firm halves with no inner-product-axiom content; the missing dedicated per-domain test is redundant under the escape, the existing `test-domainpostoperator.cpp:83-93` whole-domain energy-form coverage supporting. The exact `eigenfreq_qfactor_reduce` c082 disposition, now realized for the per-DOMAIN sibling). The `Σ pᵢ = 1` partition-of-unity stays **config-conditional** (partition precondition), NOT an unconditional identity — a per-config property, not a verb law. **Scope: 1-of-1 output-product, driver-agnostic by design.** Harvested cycle-079 D3; promoted firm cycle-091 D3.
<<<END>>>
```

**3c. `:32` firm count header → (18 + 4) (the firm-side half of the reconciliation).**

```edit:book/src/L4/index.md
<<<OLD (head of :32)>>>
**Firm at L4 (17 + 4 outer-driver)** — cycle-086 promoted the fixed-operator family-map combinator [`solve_family`](./solve_family.md)
<<<NEW (head of :32)>>>
**Firm at L4 (18 + 4 outer-driver)** — cycle-091 promoted the per-domain energy-table reduction combinator [`domain_energy_reduce`](./domain_energy_reduce.md) `rough-in` → `firm` (the batch-29 firm-flip-and-cascade wave — both its folded primitives now firm L1, matrix-weighted-norm c091 + participation_ratio c077, the firm-on-positive-structure escape, the per-DOMAIN realization of the per-MODE `eigenfreq_qfactor_reduce` c082 disposition; this emptied the L4 rough-in cohort). Before it, cycle-086 promoted the fixed-operator family-map combinator [`solve_family`](./solve_family.md)
<<<END>>>
```

**3d. `:98` Status cell — re-narrate domain_energy_reduce's gating rationale to firm (D1 already flipped the Folds-cell label at `:98`; I touch only the Status cell).** The Status cell currently ends `rough-in (harvested cycle-079 D3 … rough-in not firm because the folded domain-restricted energy form is the matrix-weighted-norm rough-in (test-coverage-bounded) primitive AND there is no dedicated per-domain energy-participation test …)`. Re-narrate to firm:

```edit:book/src/L4/index.md
<<<OLD (Status cell of :98)>>>
| `rough-in` (harvested cycle-079 D3 from OQ `domain_energy_reduce-l4-verb-needs-authoring` + the c079 D4 confirm-probe DISTINCT-VERB-WARRANTED; structure read off the positive `MeasureDomainFieldEnergy` per-domain loop `postoperator.cpp:1021-1099` + the energy form `domainpostoperator.cpp:255-297`; rough-in not firm because the folded domain-restricted energy form is the `matrix-weighted-norm` `rough-in (test-coverage-bounded)` primitive AND there is no dedicated per-domain energy-participation test (the firm `participation_ratio` half is necessary but not sufficient). Σ pᵢ = 1 is config-conditional (partition-precondition), NOT an unconditional identity. Genuine NEW spine vocabulary — the field-energy output-product reduction verb, the per-DOMAIN rank-1 scalar-table sibling of `eigenfreq_qfactor_reduce`, NOT a `participation_ratio` fold-inline, NOT a `gram_reduce` specialization) |
<<<NEW (Status cell of :98)>>>
| `firm` (harvested cycle-079 D3 from OQ `domain_energy_reduce-l4-verb-needs-authoring` + the c079 D4 confirm-probe DISTINCT-VERB-WARRANTED; structure read off the positive `MeasureDomainFieldEnergy` per-domain loop `postoperator.cpp:1021-1099` + the energy form `domainpostoperator.cpp:255-297`; promoted rough-in→firm cycle-091 D3 by the batch-29 firm-flip-and-cascade wave on the **firm-on-positive-structure escape** — both folded primitives now firm L1 (`matrix-weighted-norm` c091 + `participation_ratio` c077), every map law a read-off syntactic identity over two firm halves with no inner-product-axiom content, the missing dedicated per-domain test redundant under the escape (the existing `test-domainpostoperator.cpp:83-93` whole-domain energy-form coverage supporting); the exact `eigenfreq_qfactor_reduce` c082 disposition realized for the per-DOMAIN sibling. Σ pᵢ = 1 is config-conditional (partition-precondition), NOT an unconditional identity. Genuine NEW spine vocabulary — the field-energy output-product reduction verb, the per-DOMAIN rank-1 scalar-table sibling of `eigenfreq_qfactor_reduce`, NOT a `participation_ratio` fold-inline, NOT a `gram_reduce` specialization) |
<<<END>>>
```

**3e. `:102` gram_reduce JOINT Folds label — split: matrix-weighted-norm firm / bilinear-form rough-in; the Status stays rough-in (bilinear-form residual gate).** D1 deferred this whole row to me. The Folds cell opens `Folds (rough-in L1): [matrix-weighted-norm] …, [bilinear-form] …`. Split the joint `(rough-in L1)` label.

```edit:book/src/L4/index.md
<<<OLD (Folds cell head of :102)>>>
| Folds (rough-in L1): [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (diagonal self-bilinear `xᵢᵀ K xᵢ` — the diagonal CONSUMER, NOT a separate fold), [`bilinear-form`](../L1/bilinear-form.md) (off-diagonal cross-bilinear `xⱼᵀ K xᵢ`).
<<<NEW>>>
| Folds: [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (firm c091 — diagonal self-bilinear `xᵢᵀ K xᵢ`, the diagonal CONSUMER, NOT a separate fold), [`bilinear-form`](../L1/bilinear-form.md) (rough-in — off-diagonal cross-bilinear `xⱼᵀ K xᵢ`; the sole remaining rough-in folded primitive, the residual gate).
<<<END>>>
```

And the gram_reduce Status cell stays rough-in but narrows its rationale to the bilinear-form residual:

```edit:book/src/L4/index.md
<<<OLD (Status cell of :102)>>>
but gated rough-in because the folded L1 primitives are themselves rough-in AND no dedicated Gram-reduction test; promotion = L1 primitives firm + dedicated test/verifier pass.
<<<NEW (Status cell of :102)>>>
but STAYS rough-in (test-coverage-bounded) cycle-091: one of the two folded gates discharged (the diagonal `matrix-weighted-norm` firmed c091) but the off-diagonal `bilinear-form` is still rough-in (its own `lower-layer-shared-vocabulary` gate) — a reduction is as firm as its least-firm folded primitive, the honest partial cascade outcome (contrast the per-DOMAIN `domain_energy_reduce` which firmed c091 because BOTH its folded primitives are firm); narrowed promotion = `bilinear-form` firms + dedicated test/verifier pass.
<<<END>>>
```

## L4/index reconciliation summary (count deltas + lines)

| Line | Old | New | Driver |
|---|---|---|---|
| `:32` firm header | Firm at L4 (**17** + 4) | Firm at L4 (**18** + 4) | domain_energy_reduce firm flip (firm-side count) |
| `:49`→insert | (end of eigenfreq_qfactor_reduce firm bullet) | + new `domain_energy_reduce` firm-cohort bullet | bullet move (firm cohort) |
| `:57` rough-in header | Rough-in at L4 (**1**) | Rough-in at L4 (**0**) — cohort empty | domain_energy_reduce firm flip (rough-in-side count) |
| `:59` rough-in bullet | domain_energy_reduce *(rough-in)* bullet | DELETED (moved to firm cohort) | bullet move |
| `:98` Status cell | `rough-in` (…gated on matrix-weighted-norm rough-in + no test…) | `firm` (…escape, both primitives firm…) | domain_energy_reduce firm flip |
| `:102` Folds cell | `Folds (rough-in L1): [mwn] …, [bilinear-form] …` | `Folds: [mwn] (firm c091…), [bilinear-form] (rough-in…residual gate)` | gram_reduce joint-label split |
| `:102` Status cell | gated rough-in (both primitives rough-in…) | STAYS rough-in (mwn discharged, bilinear-form residual) | gram_reduce stays + narrowed gate |

**Net L4 maturity delta: firm 17→18, rough-in 1→0.** (D1 already flipped the `:98` Folds-cell standalone matrix-weighted-norm label to firm; my `:98` edit touches the distinct Status cell — no same-line collision.)

## Supporting evidence

- **gram_reduce residual gate (bilinear-form still rough-in):** `book/src/L1/bilinear-form.md:4` (`firmness: rough-in`), `:319-325` (§Status `rough-in (lower-layer-shared-vocabulary, cycle-010-wave-1)`) — on-disk Read this dispatch. L0 anchors: `palace/linalg/operator.cpp:621-639` (citecheck `[ok]`, the bilinear-form `Mult` overload).
- **domain_energy_reduce firm warrant:**
  - positive structure: `palace/models/postoperator.cpp:1021-1099` (`MeasureDomainFieldEnergy`, citecheck `[ok]`); the two participation guards `:1039` (electric, numerator-guard) / `:1064` (magnetic, denominator-guard) both citecheck `[ok]`; the shared denominator `:1033` `GetElectricFieldEnergy` citecheck `[ok]`.
  - energy form: `palace/models/domainpostoperator.cpp:262-274`, `:274` `0.5 * dot` (citecheck `[ok]`).
  - test: `reference/palace/test/unit/test-domainpostoperator.cpp:83` (`GetElectricFieldEnergy`, citecheck `[ok]`), `:90-93` (the SI-energy assertion). Whole-file + whole-`test/unit/` grep: NO `GetDomainElectric/MagneticFieldEnergy` call anywhere → per-domain restriction is test-uncovered (confirms the test is supporting-not-firming).
  - precedent: `book/src/L1/participation_ratio.md:184-191` (firm-as-quotient; "syntactic-identity quotient laws are not test-gated"); `book/src/L4/eigenfreq_qfactor_reduce.md` §Status + `L4/index.md:49` (firm c082, the per-MODE sibling, the same both-primitives-firm + no-axiom-content escape).
- **D1 coordination:** `reports/2026-06-04T053300Z-harvester-cycle-091-matrix-weighted-norm-firm-flip/CYCLE.md` §3 — D1 flipped matrix-weighted-norm to firm, flipped the `:98` Folds-cell label, and deferred `:57`/`:59`/`:98`-Status/`:102` + the firm-side count to me.

## Open questions / caveats

- **gram_reduce next gate (NOT in this cycle's scope):** the remaining gate after this cycle is `bilinear-form` firming. Its own status is `rough-in (lower-layer-shared-vocabulary, cycle-010-wave-1)`, gated on a narrow-variant-axis-coverage question (`bilinear-form.md:325-330`). When/if a future cycle firms bilinear-form, gram_reduce's residual gate clears and the electrostatic/magnetostatic/capacitance/inductance columns become unblockable. This is the natural batch-29 forward-frontier follow-up surfaced by this verdict — I have NOT added a fresh candidate (per the plan's matching note); the meta-phase will see it from this report.
- **`:32`/`:49`/firm-cohort-bullet edits are the firm-side half of the deferred reconciliation, applied within D1's single-owner L4/index.md.** D1 literally deferred `:57`/`:59`/`:98`-Status/`:102`; my firm verdict necessitates the symmetric firm-side `:32` (17→18) + the firm-cohort bullet insertion. I propose them so the integrator applies a COMPLETE, coherent L4/index reconciliation in one D3-coordinated pass (the rough-in cohort cannot empty without the firm cohort gaining the member). All my `old_string`s match the post-D1 on-disk text and none collide with D1's `:98` Folds-cell edit. Flagged for the integrator: apply D1's L4/index edits first, then this report's L4/index edits.
- **Inconsistent C++ participation guard (`:1039` numerator vs `:1064` denominator)** is a pre-existing Palace source observation already noted in domain_energy_reduce.md §"On the uniform total-guard" (`:182-199`) and resolved there to the uniform denominator guard; NOT introduced by this dispatch, no new `problems/` filing warranted (already documented).
- **No directionality violation found.** Both reduce-verb chapters narrate high→low (L4 verb defined in L4 vocabulary, lowering by identity-in-form to the L1 folded primitives); the §Status / §Lowers-to sections are forward (L4→L1). No reverse-lift prose.
