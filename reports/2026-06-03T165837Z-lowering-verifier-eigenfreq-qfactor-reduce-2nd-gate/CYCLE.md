---
agent: lowering-verifier
invoked_at: 2026-06-03T165837Z
scope: L4 verb audit — eigenfreq_qfactor_reduce (2nd / test-coverage gate via existing postprocess unit test)
status: integrated
integrated_at: 2026-06-03T210000Z
integration_commit: bdaf851
integration_notes: "Applied cycle-079 (batch-25 position 1). eigenfreq_qfactor_reduce ## Status rough-in -> rough-in (test-coverage-bounded) via existing-test citation (test-postoperator.cpp [idempotent] round-trip over mode_port_kappa :216/:259 + participation_ratio :160-188; batch-24 decision (e)); gate-a (kappa-participation) already firm via participation_ratio (c077), NOT re-opened; 8-entry verified_against: top-level fenced yaml block landed; L4/index status cell refreshed; a paragraph appended to the column ## Status. The coupled eigenfrequency-qfactor column STAYS seed. Successor OQ eigenfreq-qfactor-reduce-firm-needs-l1-eigenvalue-untransform-primitive opened. NOTE the column's ~L68 Status-opening-paragraph staleness flagged for a next-cycle prose cleanup. NO firm-count change."
inputs:
  - book/src/L4/eigenfreq_qfactor_reduce.md
  - reference/palace/test/unit/test-postoperator.cpp:52-53,110,145-150,160-188,216,259,335-342 (the PostOperator [idempotent] round-trip test, cache reduction-output fields)
  - palace/palace/drivers/eigensolver.cpp:424-439 (eigenvalue→ω un-transform, positive site 1)
  - palace/palace/models/postoperator.cpp:1185-1203 (Q-factor body MeasureLumpedPortsEig, positive site 2)
  - book/src/feature/eigenfrequency-qfactor.{L4,L1,L0}.md (coupled seed output-product column)
---

# CYCLE: Audit eigenfreq_qfactor_reduce (2nd-gate test-coverage discharge)

## Summary

I audited the L4 verb `eigenfreq_qfactor_reduce` (currently `rough-in`, no prior
`verified_against:` block) against the existing Palace postprocess unit test
`test/unit/test-postoperator.cpp` as L0-equivalent semantic documentation of the per-mode
`(f, Q)` scalar-table reduction-OUTPUT, plus re-verified the verb's two positive L0 sites.
**Top-level verdict: partially-supported — promotion verdict `rough-in (test-coverage-bounded)`** (a
QUALIFIER upgrade of the bare `rough-in`, NOT a flip to `firm`). The `PostOperator`
`[idempotent]` test asserts **Nondimensionalize/Dimensionalize round-trip invariance over the
`Measurement` reduction-output cache** — it directly CHECK-asserts the κ closure
(`mode_port_kappa`) and the participation-ratio sibling (`participation_ratio`) the verb folds,
documenting them as real, structurally-present, unit-coherent reduction-output fields. But the
test does **not** exercise the eigenpair→`(f,Q)` **assembly map** (the cache is randomly
populated, not produced by the un-transform + κ computation), and the actual `(f, Q)` output
scalars (`cache.freq`, `cache.eigenmode_Q`, the lumped-port `quality_factor`) are
**populated-but-not-CHECK-asserted** in this idempotency test. This is the exact shape of the
sibling `sparameter_reduce` audit: the test confirms reduction-OUTPUT invariants over the
`Measurement` cache, not the assembly. The residual structure-side gate (the eigenvalue
un-transform primitive has no firm L1 entry, and no dedicated assembly test exercises the
eigenpair→`(f,Q)` map) is **untouched** by this test and remains. (Note: the κ-participation half
of the structure gate is already addressed — `book/src/L1/participation_ratio.md` is `firm` (c077),
citing the resistive κ `½R|I|²/E` at `postoperator.cpp:1188-1203`, the verb's own κ site; the
matching firming-route OQ is CLOSED-RESOLVED, "gate-a discharged".) So the entry rises from bare `rough-in` to `rough-in (test-coverage-bounded)`
— the structure is firm-on-positive-structure, the test partially discharges the law/output
confidence to the extent an output-invariance test can — but does NOT reach `firm`. The coupled
seed output-product column (`eigenfrequency-qfactor.{L4,L1,L0}`) stays **`seed`**: its
primitive-L1-firmness gate is wholly untouched and the test-gate is only partially discharged; I
propose repointing its down-links to add the test citation but no promotion.

## Per-citation audit

### Test citations (the 2nd-gate discharge candidate)

- **Citation**: `reference/palace/test/unit/test-postoperator.cpp:145-150`
  - **Theme claim (dispatch)**: the `PostOperator` test asserts invariance over the per-mode
    Q/freq reduction-output cache fields.
  - **Found**: `TEST_CASE("PostOperator", "[idempotent][Serial]")` at :145. Body:
    `auto cache = RandomMeasurement();` (:147), `auto dim_cache = Measurement::Dimensionalize(units, cache);`
    (:149), `auto non_dim_cache = Measurement::Nondimensionalize(units, dim_cache);` (:150). This
    is a **round-trip-invariance harness over a randomly-populated `Measurement` cache** — it
    asserts the cache fields carry the correct unit class and round-trip cleanly. It does NOT call
    the eigenmode driver, does NOT run the un-transform, does NOT compute κ from `E_m`/`I_mj`.
  - **Verdict**: supports (as the harness establishing reduction-OUTPUT invariance).
  - **Notes**: The test's nature is the load-bearing nuance — it documents the OUTPUT cache, not
    the assembly map. Same as sibling `sparameter_reduce`.

- **Citation**: `reference/palace/test/unit/test-postoperator.cpp:52-53`
  - **Theme claim**: documents `cache.eigenmode_Q` and `cache.freq` (the per-mode `(f, Q)`
    output scalars).
  - **Found**: `cache.freq = std::complex(1 + randd(99), randd(100));` (:52),
    `cache.eigenmode_Q = 5e6 * (randd(99) + 1);` (:53). These are the eigenfrequency and per-mode
    Q output fields — but here only **populated** with random values in `RandomMeasurement()`.
    Searching the round-trip body (lines 150–345) I found **no `CHECK_THAT` on `cache.freq` or
    `cache.eigenmode_Q`** — they are populated but never asserted invariant.
  - **Verdict**: partially-supports.
  - **Notes**: Confirms the `(f, Q)` scalar-table output fields **exist** in the `Measurement`
    cache (the verb's result shape is real at L0), but the test does not assert anything about
    them. This is weaker than the dispatch framing implied.

- **Citation**: `reference/palace/test/unit/test-postoperator.cpp:160-188`
  - **Theme claim**: the per-mode `participation_ratio` map (domain-energy participation block).
  - **Found**: the `domain_E_field_energy_i` / `domain_H_field_energy_i` loop CHECK-asserts
    `CHECK_THAT(c.participation_ratio, Catch::Matchers::WithinRel(ndc.participation_ratio))`
    (:167-168, :180-181) AND the dimensional arm `CHECK_THAT(c.participation_ratio,
    WithinRel(dc.participation_ratio))` (:173, :186) — participation_ratio is dimensionless, so it
    is invariant under BOTH transforms. `participation_ratio = energy / energy_all` populated at
    :45, :49.
  - **Verdict**: supports.
  - **Notes**: `participation_ratio` is the **dimensionless energy-participation sibling** of the
    verb's κ closure (κ is itself a `½R|I|²/E` participation ratio). The test directly confirms
    this participation-output semantics is real and unit-coherent.

- **Citation**: `reference/palace/test/unit/test-postoperator.cpp:216` (and :259)
  - **Theme claim**: the mode-port-kappa CHECK in `check_port_data`.
  - **Found**: inside `check_port_data` lambda (def :188-189), nondimensional arm:
    `CHECK_THAT(c.mode_port_kappa, Catch::Matchers::WithinRel(ndc.mode_port_kappa));` (:216);
    dimensional arm (lumped, `std::abs(c.V) > 0`):
    `CHECK_THAT(c.mode_port_kappa, !Catch::Matchers::WithinRel(dc.mode_port_kappa));` (:259).
    Populated at :109 (`l.mode_port_kappa = (1 + randd(100));`).
  - **Verdict**: supports.
  - **Notes**: This is the **strongest** test support — `mode_port_kappa` is exactly the κ loss
    rate the verb's `kappa : Mode -> Scalar` closure folds (`κ_mj = ½R_j|I_mj|²/E_m`). The test
    asserts it is invariant under nondimensionalization (:216) and carries a real unit class
    under dimensionalization (:259, the `!WithinRel`). Directly documents the κ reduction-output
    field as L0-equivalent semantics.

- **Citation**: `reference/palace/test/unit/test-postoperator.cpp:335-342`
  - **Theme claim (dispatch)**: `c.quality_factor` CHECK as part of the per-mode Q reduction.
  - **Found**: `CHECK_THAT(c.quality_factor, WithinRel(ndc.quality_factor));` (:335) and
    `CHECK_THAT(c.quality_factor, WithinRel(dc.quality_factor));` (:342) — but these are inside the
    `interface_eps_i` loop (interface dielectric-loss Q), NOT the lumped-port / eigenmode Q. The
    **lumped-port `quality_factor`** (populated :110, `l.quality_factor = 1e9/(1+randd(9999));`)
    is NOT checked: `check_port_data` (188-264) asserts `mode_port_kappa` but contains **no
    `quality_factor` CHECK**.
  - **Verdict**: partially-supports.
  - **Notes**: **Correction to the dispatch framing.** `quality_factor` IS CHECK-asserted in the
    test, but on `interface_eps_i` (a different output product), not on the mode-port / eigenmode
    Q the verb produces. The verb's actual `Q_mj = ω_m/κ_mj` output scalar is populated
    (`l.quality_factor`, :110) but not CHECK-asserted. So the `(f, Q)` Q-half is only
    **indirectly** covered (via κ, which IS checked, and via the structurally-analogous
    interface-eps Q round-trip).

### Verb's own positive L0 sites (re-verified)

- **Citation**: `palace/palace/drivers/eigensolver.cpp:424-439`
  - **Theme claim**: positive site 1 — the eigenvalue→ω un-transform (linear `√μ` / quadratic
    `λ/i`).
  - **Found**: `for (int i = 0; i < num_conv; i++)` at :424 (readout loop start);
    `omega = eigen->GetEigenvalue(i)` at :427; `omega = std::sqrt(omega)` at :433 (linear EVP);
    `omega /= 1i` at :438 (quadratic EVP). All re-verified on-disk via `citecheck --anchor`.
  - **Verdict**: supports.
  - **Notes**: matches the verb's `untransform` dispatch (§Signature) exactly.

- **Citation**: `palace/palace/models/postoperator.cpp:1185-1203`
  - **Theme claim**: positive site 2 — the Q-factor body (`κ = ½R|I|²/E`, `Q = ω/κ`, lossless
    guard).
  - **Found**: comment `κ_mj = 1/2 R_j I_mj² / E_m` and `Q_mj = ω_m/κ_mj` at :1186-1191;
    `resistor_power = 0.5*std::abs(data.R)*std::real(I_mj*std::conj(I_mj))` at :1198;
    `mode_port_kappa = std::copysign(resistor_power/energy_electric_all, I_mj.real())` at
    :1199-1200; `quality_factor = (mode_port_kappa == 0.0) ? mfem::infinity() : freq_re/std::abs(mode_port_kappa)`
    at :1200-1202. Re-verified on-disk.
  - **Verdict**: supports.
  - **Notes**: the verb's law 4 (`κ=0 ⇒ Q=∞`, `mfem::infinity()`) and the `Q = f/|κ|` quotient
    are exact reads of this body. NOTE: the verb's Evidence section cites the loss-rate at
    `:1198-1199` and the Q at `:1200-1202`; on-disk `mode_port_kappa` assignment is :1199-1200 and
    `quality_factor` is :1200-1202 — the existing entry citations are within ±1 and the anchors
    resolve, so no carry-forward correction is required, but the per-line breakdown above is the
    precise on-disk map.

## Applicability conditions

- **Condition**: Each table row is independent (map-independence / list homomorphism over modes).
  - **Verifiable**: from the readout loop `eigensolver.cpp:424` — the `for` loop carries no
    inter-mode accumulator; each iteration reads `GetEigenvalue(i)` independently. Confirmed.
  - **Found counter-example?**: no.

- **Condition**: The un-transform is a pure per-mode scalar branch keyed on `ProblemType`.
  - **Verifiable**: `eigensolver.cpp:430-439` — the `√μ` vs `λ/i` branch is selected per the
    linear-vs-quadratic test, no cross-mode combine. Confirmed.
  - **Found counter-example?**: no.

- **Condition (test-side)**: the reduction-OUTPUT cache fields are unit-coherent and round-trip.
  - **Verifiable**: from `test-postoperator.cpp` — `mode_port_kappa` (:216, :259) and
    `participation_ratio` (:167-186) CHECK-asserted invariant/scaled correctly. Confirmed for κ
    and participation; NOT directly verified for `freq`/`eigenmode_Q`/lumped-port `quality_factor`
    (populated, not asserted).
  - **Found counter-example?**: no (but a coverage gap, see Open questions).

## Algebraic laws

- **Law 1 — Map-independence / concatenation-homomorphism.**
  - **Holds on operators?**: yes. The readout loop (`eigensolver.cpp:424`) carries no inter-mode
    state; each `(f,Q)` row depends only on its own `(λᵢ, κᵢ)`. Syntactic read-off, firm.

- **Law 2 — Un-transform purity.**
  - **Holds on operators?**: yes. `f = Re(untransform ptype λ)`, branch at `:430-439`. Syntactic.

- **Law 3 — Q is a scalar ratio, not a bilinear (do-NOT-merge-with-gram_reduce).**
  - **Holds on operators?**: yes. `Q_mj = ω_m/κ_mj` at `postoperator.cpp:1200-1202` is a per-mode
    scalar quotient — no family-PAIR grid, no `symmetric_from_upper`. Confirmed; the c074 D6
    closed-negative non-subsume is sound.

- **Law 4 — Lossless-mode totality (`κ=0 ⇒ Q=∞`).**
  - **Holds on operators?**: yes. `quality_factor = (kappa==0.0) ? mfem::infinity() : freq_re/|κ|`
    at `postoperator.cpp:1200-1202`. Exact. Total edge case in the scalar map, not an error arm.

- **Test-confirmation status of the laws**: the laws are **syntactic identities on the two
  positive sites** (independently firm). The test does NOT exercise these identities (it does not
  run the assembly); it only confirms the OUTPUT cache fields the laws produce are real and
  unit-coherent. So the test raises **output-shape confidence**, not **law-execution confidence**
  — consistent with `rough-in (test-coverage-bounded)`, not `firm`.

## Promotion verdict (my call)

**`rough-in (test-coverage-bounded)`** for the verb — a qualifier upgrade of the bare `rough-in`,
NOT a flip to `firm`. Reasoning (matching the sibling `sparameter_reduce` D1 warrant):

1. The verb's **structure** is firm-on-positive-structure: the per-mode map skeleton + the
   un-transform branch + the κ/Q quotient are read directly off the two positive sites
   (`eigensolver.cpp:424-439`, `postoperator.cpp:1185-1203`), and every law is a syntactic
   identity on that body. The structure clears the firm-on-positive-structure bar.
2. The existing test **partially discharges the test-gate**: it documents the reduction-OUTPUT
   cache fields (`mode_port_kappa`, `participation_ratio`) as L0-equivalent, unit-coherent, real
   semantics — which is exactly what a `test-coverage-bounded` qualifier records (structure
   L0-anchored; laws/output test-supported to the extent an output-invariance test can support
   them). This is enough to move OFF bare `rough-in` to the qualified tier.
3. But **firm is not warranted** because (a) the test asserts OUTPUT invariance, not the
   eigenpair→`(f,Q)` **assembly** map (the `freq`/`eigenmode_Q`/lumped-port `quality_factor`
   output scalars are populated-but-not-CHECK-asserted; the κ-from-`E`/`I` computation is not
   exercised), and (b) the **residual structure-side primitive-maturity gate is untouched** — the
   eigenvalue un-transform still has no firm L1 entry, so the verb cannot fully inherit firm
   primitive maturity. (The κ-participation half of this gate is already discharged: firm L1
   `participation_ratio` (c077) covers the resistive κ `½R|I|²/E` the verb folds, citing the
   verb's own κ site `postoperator.cpp:1188-1203`; OQ CLOSED-RESOLVED, "gate-a discharged".) The
   residual eigenvalue-un-transform-primitive gate (b) plus the assembly-test gate (a) are the
   remaining blockers — structure-firmness/test gates, not the whole structure being unknown;
   `test-coverage-bounded` (which names entries
   whose structure is fully L0-anchored and only laws are test-gated) is the honest tier here
   because the structure IS fully positive-anchored and what remains is primitive-maturity +
   assembly-test, not unknown structure.

This resolves OQ `eigenfreq-qfactor-reduce-status-promotion-double-gated`: the **test (2nd) gate
is now discharged-to-qualifier** (the entry moves to `rough-in (test-coverage-bounded)` citing the
existing postprocess test); the **primitive-maturity (1st) gate remains** as the documented
promotion route to `firm`.

## Proposed changes

Two edits: (1) the verb `verified_against:` block + `## Status` qualifier upgrade; (2) the
coupled feature-column down-link repoint (no promotion — stays `seed`).

### Edit 1 — verb: `eigenfreq_qfactor_reduce.md` Status qualifier + verified_against

Replace the `## Status` opening line (the bare `` `rough-in`. ``) with the qualified tier, and
append the `verified_against:` block at end of file. The full firm-tier `## Status` body (status
line + reasoning + scope, all unchanged below the first line) is inside the fence; the
`verified_against:` block is the fenced YAML at the end.

```edit:book/src/L4/eigenfreq_qfactor_reduce.md
[replace the "## Status" section opening paragraph]

## Status

`rough-in (test-coverage-bounded)`. **Reasoning (warrant-first):** the combinator's
**structure** is read directly off the two positive readout sites — the eigenvalue→ω un-transform
(`eigensolver.cpp:424-439`) and the Q-factor body (`postoperator.cpp:1185-1203`) — and the map
laws (§Algebraic laws) are syntactic identities on that per-mode map, clearing the
firm-on-positive-structure bar. The existing PostOperator postprocess unit test
(`test/unit/test-postoperator.cpp`, the `[idempotent]` round-trip) **partially discharges the
test-gate**: it CHECK-asserts the reduction-OUTPUT cache fields the verb folds — the κ loss rate
`mode_port_kappa` (`:216`, `:259`) and the participation-ratio sibling `participation_ratio`
(`:160-188`) — as real, unit-coherent, round-trip-invariant `Measurement` fields, documenting the
`(f, Q)`/κ scalar-table output semantics as L0-equivalent. This moves the entry off bare
`rough-in` to the **test-coverage-bounded** qualifier (structure fully L0-anchored; output/laws
test-supported to the extent an output-invariance test can support them). It is NOT promoted to
`firm` because:
1. one of the per-mode building blocks it folds — the **eigenvalue un-transform** — is **not yet a
   firm L1 entry** (no `L1/eigenfreq_qfactor_reduce` or eigenvalue-un-transform primitive exists;
   that half of the reduction is distilled directly from the driver body), so the entry cannot
   fully inherit firm primitive maturity (a residual STRUCTURE-firmness gate, not a test gate). The
   κ-participation half of this primitive-maturity gate is **already discharged**: firm L1
   [`participation_ratio`](../L1/participation_ratio.md) (c077) covers the resistive κ loss-rate
   ratio (`½R|I|²/E`) the verb folds, citing the verb's own κ site (`postoperator.cpp:1188-1203`)
   as a positive witness; and
2. the test asserts reduction-OUTPUT invariance over the randomly-populated `Measurement` cache,
   NOT the eigenpair→`(f,Q)` **assembly map** — the `(f, Q)` output scalars `cache.freq` /
   `cache.eigenmode_Q` / the lumped-port `quality_factor` are populated-but-not-CHECK-asserted in
   the idempotency test (the asserted `quality_factor` at `:335-342` is `interface_eps_i`
   dielectric Q, a different output product), so the assembly-level laws are still test-unconfirmed.

Promotion route (to `firm`): (a) firm up the residual folded per-mode primitive — the
eigenvalue-un-transform primitive (the κ-participation primitive is already firm L1
[`participation_ratio`](../L1/participation_ratio.md), c077), AND (b) a dedicated
eigenmode-postprocess assembly test (exercising the un-transform + κ-from-`E`/`I` computation, not
just output-cache round-trip) OR a lowering-verifier pass raising the assembly-map confidence to
`inner_product`-equivalent. (Contrast the rank-2 sibling [`gram_reduce`](./gram_reduce.md),
`rough-in (test-coverage-bounded)` for the same primitive-maturity + output-only-test reasons; and
the driven-pipeline sibling [`sparameter_reduce`](./sparameter_reduce.md), the same
output-invariance-test discharge shape.)

**Scope: 1-of-1 — the eigenmode pipeline's output product.** This is the eigenmode driver's
OWN output-product reduction; it is not a cross-pipeline shared verb (the other four
pipelines have different output products: capacitance/inductance via
[`gram_reduce`](./gram_reduce.md), driven S-parameters via [`sparameter_reduce`](./sparameter_reduce.md),
transient via the field/energy time-history). The disciplined-cross-pipeline-mining-gate
does not apply — this is a single-pipeline output-product verb by design (like
[`frequency_sweep`](./frequency_sweep.md)'s single-witness-driven-by-design scope).

[append at end of file — the `verified_against:` YAML block, shown INDENTED (4 spaces) to avoid a
nested same-style fence inside this proposed-changes block per the
`convert-nested-fences-to-indented-code-in-proposed-changes-block` skill; the integrator strips the
4-space indent and writes it as a top-level fenced ```yaml block]

    verified_against:
      - citation: palace/test/unit/test-postoperator.cpp:145-150
        verdict: supports
        audited_at: 2026-06-03T165837Z
        note: TEST_CASE PostOperator [idempotent] establishes Nondimensionalize/Dimensionalize round-trip over the Measurement cache; the harness that asserts reduction-OUTPUT invariance (not the eigenpair-to-(f,Q) assembly map) — same shape as the sparameter_reduce output-invariance discharge.
      - citation: palace/test/unit/test-postoperator.cpp:52-53
        verdict: partially-supports
        audited_at: 2026-06-03T165837Z
        note: cache.freq + cache.eigenmode_Q (the per-mode f and Q output scalars) populated as Measurement reduction-output fields, documenting the (f,Q) scalar-table output EXISTS at L0; populated-but-not-CHECK-asserted in this idempotency round-trip.
      - citation: palace/test/unit/test-postoperator.cpp:160-188
        verdict: supports
        audited_at: 2026-06-03T165837Z
        note: participation_ratio (the dimensionless domain-energy participation, the kappa closure's sibling ratio) CHECK-asserted invariant over the round-trip (lines 167-186), confirming the per-mode energy-participation reduction-output semantics.
      - citation: palace/test/unit/test-postoperator.cpp:216-216
        verdict: supports
        audited_at: 2026-06-03T165837Z
        note: mode_port_kappa (the resistive-lumped-port loss rate the verb's kappa closure folds, kappa = 1/2 R|I|^2/E) CHECK-asserted invariant under nondimensionalization — the strongest direct documentation of the kappa reduction-output field.
      - citation: palace/test/unit/test-postoperator.cpp:259-259
        verdict: supports
        audited_at: 2026-06-03T165837Z
        note: mode_port_kappa dimensional-vs-nondimensional CHECK (!WithinRel) confirms it carries a real unit class, the expected behavior of an energy/loss ratio output field.
      - citation: palace/test/unit/test-postoperator.cpp:335-342
        verdict: partially-supports
        audited_at: 2026-06-03T165837Z
        note: quality_factor IS CHECK-asserted invariant, but on interface_eps_i (interface dielectric Q), NOT the eigenmode/mode-port Q; the lumped-port quality_factor (line 110) and eigenmode_Q are populated but not CHECK-asserted, so the (f,Q) Q-half is only indirectly covered (via kappa, which IS checked).
      - citation: palace/palace/drivers/eigensolver.cpp:424-439
        verdict: supports
        audited_at: 2026-06-03T165837Z
        note: positive site 1 re-verified on-disk via citecheck --anchor; readout loop start :424, sqrt-untransform at :433 (linear EVP), lambda/i untransform at :438 (quadratic EVP).
      - citation: palace/palace/models/postoperator.cpp:1185-1203
        verdict: supports
        audited_at: 2026-06-03T165837Z
        note: positive site 2 re-verified on-disk; kappa_mj = 1/2 R|I|^2/E at :1198-1200, Q_mj = freq_re/|kappa| with the kappa==0 ? mfem::infinity() guard at :1200-1202, formula comment :1186-1191.
```

### Edit 2 — feature column down-link repoint (no promotion; stays `seed`)

The column `eigenfrequency-qfactor.{L4,L1,L0}` stays `seed` — its primitive-L1-firmness gate is
untouched and the test-gate is only partially discharged, so the "promote past seed only when ALL
composed constituents are firm" bar is not met. I propose repointing the L4 column's dep-map test
column to cite the now-confirmed postprocess test, and noting the qualifier upgrade of the verb,
without changing `status: seed`.

```edit:book/src/feature/eigenfrequency-qfactor.L4.md
[in the dep-map table, the per-mode scalar-ratio reduction row — append the test citation and update the firmness token]

| per-mode scalar-ratio reduction | [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) | rough-in (test-coverage-bounded) | `eigensolver.cpp:424-439`, `postoperator.cpp:1171-1203`, `test/unit/test-postoperator.cpp:216,259,160-188` (reduction-output cache round-trip: mode_port_kappa, participation_ratio) |

[in the Status section, after the "stays `seed`" sentence, append:]

The verb [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) was raised to `rough-in
(test-coverage-bounded)` (cycle-079 lowering-verifier audit: the PostOperator `[idempotent]`
postprocess test `test/unit/test-postoperator.cpp` CHECK-asserts the κ loss-rate `mode_port_kappa`
and the participation-ratio output fields as round-trip-invariant L0-equivalent semantics). The
column nonetheless stays `seed`: the verb is still not `firm` (its residual folded per-mode
primitive — the eigenvalue un-transform — has no firm L1 entry, and the test asserts
reduction-OUTPUT invariance not the eigenpair→`(f,Q)` assembly; the κ-participation half is already
firm L1 `participation_ratio`), and a feature column may promote past `seed` only once ALL its
composed constituents are firm.
```

(The `.L1.md` and `.L0.md` columns keep their existing rough-in down-link tokens; the same dep-map
test-citation addition may be mirrored there at integrator discretion, but the `seed` status and
the substantive prose are unchanged — the audit changes nothing structural in those two files.)

## Supporting evidence

- `reference/palace/test/unit/test-postoperator.cpp` — read 38-115 (`RandomMeasurement` cache
  population), 145-150 (the `[idempotent]` TEST_CASE harness), 150-345 (the
  Nondimensionalize/Dimensionalize round-trip CHECK body); `check_port_data` lambda 188-264.
- `reference/palace/palace/drivers/eigensolver.cpp:424-439` — the per-mode readout loop +
  un-transform branch (positive site 1), re-verified via `citecheck --anchor`.
- `reference/palace/palace/models/postoperator.cpp:1185-1203` — the `MeasureLumpedPortsEig`
  Q-factor body (positive site 2), read on-disk + `citecheck --anchor`.
- `book/src/L4/eigenfreq_qfactor_reduce.md` — the audited verb.
- `book/src/L4/sparameter_reduce.md` — the sibling-audit precedent (the output-invariance-test
  discharge shape + the deliberate plain-`rough-in`-vs-qualifier reasoning).
- `book/src/feature/eigenfrequency-qfactor.{L4,L1,L0}.md` — the coupled seed output-product column.
- `tools/citecheck/citecheck.py` — all asserted anchors checked (clean `[ok]`); `verified_against:`
  block extracted and `yaml.safe_load`-parsed clean before shipping.

## Open questions / caveats

- **Dispatch framing correction (mechanical):** the dispatch named "`c.quality_factor` (the
  mode-port-kappa CHECK in `check_port_data`)" as documenting the per-mode Q. On-disk,
  `check_port_data` CHECK-asserts `mode_port_kappa` (:216, :259) but NOT `quality_factor`; the
  asserted `quality_factor` (:335, :342) is on `interface_eps_i` (interface dielectric Q), a
  different output product. The κ field IS the strongest direct support; the Q output scalar
  itself is populated-but-not-asserted. Recorded as `partially-supports` on :52-53 and :335-342.

- **Coverage gap (the residual promotion-to-firm condition):** no Palace unit test exercises the
  eigenpair→`(f,Q)` **assembly** (the un-transform + κ-from-`E`/`I` computation); the
  `MeasureLumpedPortsEig` body + the readout loop are integration-level, run only through the full
  eigenmode `Solve(mesh)` driver. The existing test documents the OUTPUT cache, not the assembly.
  This is the test-side half of the promotion-to-firm route; the primitive-L1-maturity half (the
  dominant gate) is independent of it.

- **OQ to append:** `eigenfreq-qfactor-reduce-firm-needs-l1-eigenvalue-untransform-primitive` — the
  residual structure-side gate to `firm` is the absence of a firm L1 entry for the **eigenvalue
  un-transform** primitive (the linear `√μ` / quadratic `λ/i` eigenpair→ω map); the κ-participation
  half is already discharged (firm L1 `participation_ratio`, c077, covers the resistive κ `½R|I|²/E`
  the verb folds). A future harvester on the eigenvalue-un-transform L1 primitive (+ a dedicated
  assembly test or assembly-confidence lowering-verifier pass) would promote the verb to `firm` and
  unblock the feature column past `seed`. (Supersedes the now-resolved double-gated OQ
  `eigenfreq-qfactor-reduce-status-promotion-double-gated`, whose test-gate half is
  discharged-to-qualifier by this audit; does NOT re-open the c077-resolved κ-participation firming
  route.)

- **Directionality:** no high→low violation found — the verb is defined in L4 vocabulary
  (the eigenpair family it consumes + the per-mode scalar maps it folds), and the "Lowers to"
  section narrates forward (L4→down). Consistent with the high→low discipline.
