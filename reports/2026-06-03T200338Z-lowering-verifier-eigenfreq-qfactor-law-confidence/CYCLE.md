---
agent: lowering-verifier
invoked_at: 2026-06-03T200338Z
scope: L4 verb law-confidence audit — eigenfreq_qfactor_reduce (the firm-on-positive-structure escape probe; gate-(b) law-confidence pass)
status: pending
integrated_at: 2026-06-03T203730Z
integration_commit: 0136fd6
integration_notes: "Applied via integrator-per-report (staging row 1, cycle-082). PROMOTED L4 verb eigenfreq_qfactor_reduce rough-in (test-coverage-bounded) → firm via the firm-on-positive-structure / syntactic-identity escape; L4 firm 14→15 main / 18→19 grand, L4 rough-in 2→1 (+1 test-coverage-bounded); coupled eigenfrequency-qfactor.{L4,L1} constituent-matrix refresh (column STAYS seed on the eigenmode.L4 driver-column gate); .L0 needed no edit. OQ eigenfreq-qfactor-reduce-firm-needs-assembly-test RESOLVED-BY-AUDIT; opened successor eigenmode-driver-column-seed-promotion-blocks-eigenfrequency-qfactor-column. retroactive-budget 0; cargo make book exit 0, zero build-repair."
inputs:
  - book/src/L4/eigenfreq_qfactor_reduce.md (the verb under audit — rough-in (test-coverage-bounded))
  - book/src/L1/eigenvalue-untransform.md (firm L1, c080 — the folded un-transform half)
  - book/src/L1/participation_ratio.md (firm L1, c077 — the folded κ-participation half)
  - book/src/L1/matrix-weighted-norm.md (the SIBLING c080 audit that RULED OUT the escape — the contrast case)
  - reference/palace/palace/models/postoperator.cpp:1171-1222 (MeasureLumpedPortsEig — the Q-factor assembly source)
  - reference/palace/palace/drivers/eigensolver.cpp:424-439 (the eigenvalue→ω un-transform readout)
  - book/src/feature/eigenfrequency-qfactor.{L4,L1,L0}.md (the coupled feature column — status seed)
  - book/src/L4/index.md (the consolidated firm/rough-in count + dep-map)
  - scaffolding/open-questions.md (OQ eigenfreq-qfactor-reduce-firm-needs-assembly-test)
---

# CYCLE: Audit eigenfreq_qfactor_reduce — law-confidence / firm-on-positive-structure escape

## Summary

Verdict: **PROMOTE the L4 verb `eigenfreq_qfactor_reduce` to `firm`** on the
**firm-on-positive-structure escape**. The audit-judgment question — whether the verb's
laws are syntactic identities / closed-form compositions over its now-firm folded
primitives + fully-specified positive assembly source, OR whether they carry genuine
assembly-correctness semantic content that only a dedicated assembly test could confirm —
resolves in favor of the escape. Each of the verb's four stated laws is a syntactic
identity on either (a) the per-mode map spine read off the positive readout loop
(`eigensolver.cpp:424`), (b) one of the two now-firm L1 folded primitives
(`eigenvalue-untransform` c080, `participation_ratio` c077), or (c) the bare `f/|κ|`
quotient with its `κ=0 ⇒ Q=∞` totality guard read literally off `postoperator.cpp:1200-1202`.
The eigenpair→`(f,Q)` **assembly** is bare scalar arithmetic composing two firm halves —
`quality_factor = freq_re / |mode_port_kappa|` — with **no axiom requiring an unverified
mathematical property**. This is the decisive contrast with the SIBLING c080
`matrix-weighted-norm` audit, which RULED OUT the escape precisely because its norm-axiom
laws (triangle / Cauchy–Schwarz / parallelogram) are mathematical theorems conditional on
an inner-product structure (SPD/Hermitian `B`) the L0 source only *numerically asserts*,
never structurally establishes. No such theorem-needing-proof exists in this verb's
assembly. The promotion is exactly the in-scope route the OQ
`eigenfreq-qfactor-reduce-firm-needs-assembly-test` names ("an in-scope lowering-verifier
law-confidence pass (now that both folded primitives are firm)").

**Coupled-column re-evaluation:** the feature column
`book/src/feature/eigenfrequency-qfactor.{L4,L1,L0}.md` (status `seed`) does **NOT** promote
past `seed` — the verb was a gating constituent but is NOT the only one: the column's other
composed constituent, the `eigenmode.L4` driver column, is itself `status: seed` (not
firm), and the column's own stated promotion rule is "promote past `seed` only once ALL its
composed constituents are firm." With the verb firm, the SOLE remaining column blocker is
the `eigenmode.L4` driver column's own seed→promotion. I record that precisely and update
the column's §Status reasoning (the verb-gate is gone; the driver-column gate remains).

**Count delta (I own it — sole dispatch touching the verb this cycle):** firm L4 cohort
`14 + 4` → `15 + 4`; rough-in cohort `2` → `1` (only `domain_energy_reduce` remains
rough-in; `solve_family` is `rough-in (test-coverage-bounded)`, separately counted in the
header narrative).

## Per-citation audit

### Folded primitive 1 — eigenvalue un-transform (firm L1, c080)

- **Citation**: `reference/palace/palace/drivers/eigensolver.cpp:424-439` (verb's own un-transform site); firm L1 home `book/src/L1/eigenvalue-untransform.md`.
- **Verb claim**: law 2 ("un-transform purity"): `f = Re(untransform ptype λ)` is a pure scalar branch keyed on `ProblemType` (`√μ` linear / `λ/i` quadratic), absorbed into the `untransform` dispatch, not a cross-mode combine.
- **Found** (on-disk, citecheck `--anchor`): readout loop start `:424`; `omega = std::sqrt(omega)` at `:433` (linear EVP, `μ = -λ² = ω²`); `omega /= 1i` at `:438` (quadratic EVP, `λ = iω`). The branch selector `if (!C && !has_A2)` at `:430`. These are the two literal closed-form complex operations the firm L1 `eigenvalue-untransform` names; every one of that primitive's laws is itself a syntactic identity on the scalar branch (it landed firm c080 on the same escape).
- **Verdict**: supports. The un-transform half of the assembly is a firm L1 closed-form scalar map; nothing about it is an untested semantic claim.
- **Notes**: `f = Re ω` is the consumer's projection (the verb's), applied AFTER the firm un-transform — a bare `.real()` read (`postoperator.cpp:1177` `freq_re = measurement_cache.freq.real()`), not a theorem.

### Folded primitive 2 — κ participation ratio (firm L1, c077)

- **Citation**: `reference/palace/palace/models/postoperator.cpp:1185-1203` (verb's own κ site); firm L1 home `book/src/L1/participation_ratio.md`.
- **Verb claim**: laws 3 ("Q is a scalar ratio, not a bilinear") + the κ definition `κₘ = ½Rⱼ·|Iₘⱼ|²/Eₘ`.
- **Found** (on-disk): `resistor_power = 0.5 * std::abs(data.R) * std::real(I_mj * std::conj(I_mj))` at `:1197` (the `½R|I|²` self-energy numerator); `mode_port_kappa = std::copysign(resistor_power / energy_electric_all, I_mj.real())` at `:1198-1199` (the SIGNED quotient — exactly `participation_ratio_signed` with the resistive-self-energy numerator). The firm L1 `participation_ratio` is the bare `energy / e_total` quotient (+ optional `copysign`); all its laws are syntactic identities on that division.
- **Verdict**: supports. The κ half is a firm L1 quotient; the verb folds it as a closure parameter (`kappa : Mode -> Scalar`).
- **Notes**: the κ numerator-energy computation lives BELOW the firm quotient (named-not-authored in `participation_ratio.md:188-191`); it is not part of the verb's per-mode map laws.

### The assembly composition — Q-factor (the gate-(b) crux)

- **Citation**: `reference/palace/palace/models/postoperator.cpp:1200-1202` (the `quality_factor` assembly).
- **Verb claim**: laws 1 ("map-independence / concatenation-homomorphism") + 4 ("lossless-mode totality `κ=0 ⇒ Q=∞`"), and the assembly `Qₘ = ωₘ/κₘ`.
- **Found** (on-disk, full body read `:1171-1222`): `vi.quality_factor = (vi.mode_port_kappa == 0.0) ? mfem::infinity() : freq_re / std::abs(vi.mode_port_kappa);` at `:1200-1202`. This is a bare scalar division `freq_re / |κ|` with a literal `== 0.0 ? ∞ :` totality guard. The enclosing `for (const auto &[idx, data] : fem_op->GetLumpedPortOp())` per-port loop (`:1180`) and the outer per-mode readout (`eigensolver.cpp:424`) carry NO inter-mode accumulator — each row depends only on its own mode's `(λᵢ, κᵢ)`, so the concatenation-homomorphism (law 1) is a structural read-off, not a derived theorem.
- **Verdict**: supports. The assembly is closed-form arithmetic composing two firm halves; the totality guard is read literally off source. There is **no residual untested semantic claim**: the only "correctness" content is whether `freq_re / |κ|` is the right formula, and that is *the positive source itself* (with the documenting comment `Q_mj = ω_m / κ_mj` at `:1190-1191`), not a property requiring a separate test.
- **Notes**: This is the precise point where the escape lives or dies. It lives: the assembly carries no axiom. Contrast the matrix-weighted-norm assembly below.

### Contrast citation — matrix-weighted-norm (escape RULED OUT, c080)

- **Citation**: `book/src/L1/matrix-weighted-norm.md` laws 4/6/7 + applicability conditions; L0 `palace/linalg/operator.cpp:616-617`.
- **Found**: that sibling audit (c080, same date) kept the entry `rough-in (test-coverage-bounded)` because laws 4 (triangle inequality), 6 (Cauchy–Schwarz), 7 (parallelogram identity) are **inner-product axioms** — theorems holding *conditional on B being SPD/Hermitian*, a property the L0 source only asserts numerically (`MFEM_ASSERT(|imag| < 1e-9·real)`), never structurally. Those carry genuine semantic content beyond the syntactic composition; the firm-on-positive-structure escape does NOT apply there.
- **Verdict**: supports (the contrast). The two audits are correctly separated: matrix-weighted-norm has theorem-laws over an unverified structure; `eigenfreq_qfactor_reduce` has only syntactic-identity laws over firm halves + a bare quotient. Same auditor judgment, opposite outcome, by the same test.

### Existing test evidence (carried forward from c079 audit — re-confirmed, NOT re-asserted as the firm basis)

- **Citation**: `palace/test/unit/test-postoperator.cpp:216`, `:259`, `:160-188` (the `[idempotent]` round-trip CHECK-asserting `mode_port_kappa` + `participation_ratio` as round-trip-invariant `Measurement` fields).
- **Verdict**: partially-supports (output-invariance only — same as c079). The test asserts reduction-OUTPUT invariance over a `RandomMeasurement()` cache; it never runs the eigenpair→`(f,Q)` assembly map. It is L0-equivalent documentation of the output fields' existence and unit-coherence, NOT the firming basis. **The firming basis is the firm-on-positive-structure escape, NOT this test** — I do not upgrade this test's verdict; I leave its `partially-supports` entries intact and add the assembly-source `supports` entries as the firm warrant.

## Applicability conditions

The verb states no formal "applicability conditions" section (unlike matrix-weighted-norm's SPD condition). The implicit conditions, walked through:

- **Condition**: the eigenpair family `[(λᵢ, Eᵢ)]` is already converged (consumed from the opaque `eigsolve` cap).
  - **Verifiable**: yes — `eigensolver.cpp:424` iterates `num_conv` already-converged pairs; the verb is a pure post-processing readout, explicitly NOT a solve-iteration (`solve_family.md:146`).
  - **Found counter-example?**: no.
- **Condition**: `κ = 0` (lossless mode) is total, returning `Q = ∞`.
  - **Verifiable**: yes — read literally off `:1200-1202` (`mfem::infinity()` guard). This is a TOTAL edge case in the scalar map, not an error arm — the verb's law 4 is exactly this.
  - **Found counter-example?**: no.
- **Condition**: the `ProblemType` selector correctly routes linear vs quadratic un-transform.
  - **Verifiable**: yes — the L0 selector is the structural predicate `!C && !has_A2` (`eigensolver.cpp:430`), abstracted as the verb's `ProblemType`/the firm L1 `EvpDegree` axis. The verb's signature names the upstream `ProblemType`; `eigenvalue-untransform` keys on the narrower derived `EvpDegree`. No counter-example; the wrong-arm case is a load-bearing NON-law correctly recorded (law: "no cross-branch identity").
  - **Found counter-example?**: no.

## Algebraic laws

Per-law verdict under the firm-on-positive-structure test (does the law hold on the verb's signature as a syntactic identity / closed-form composition over positive source + firm primitives, or does it require an unverified property?):

- **Law 1 — Map-independence / concatenation-homomorphism.**
  - **Holds on operators?**: YES, syntactic identity. The per-mode map spine carries no inter-mode accumulator (`eigensolver.cpp:424` readout loop; `postoperator.cpp:1180` per-port loop) — `reduce p κ (a ++ b) = reduce p κ a ++ reduce p κ b` is a read-off of the list-map structure, the same homomorphism `solve_family`/`gram_reduce` carry. No theorem.
- **Law 2 — Un-transform purity.**
  - **Holds on operators?**: YES, firm L1 composition. `f = Re(untransform ptype λ)` folds the firm L1 `eigenvalue-untransform` (c080) then a bare `.real()`. Each arm is a closed-form scalar inverse (`√μ`/`λ/i`); firm.
- **Law 3 — Q is a scalar ratio, not a bilinear.**
  - **Holds on operators?**: YES, firm L1 composition + bare quotient. `Qₘ = ωₘ/κₘ` where `κₘ` is the firm L1 `participation_ratio` and the `f/|κ|` step is bare division (`:1200-1202`). The rank-1 (no family-PAIR grid, no `symmetric_from_upper`) distinction from `gram_reduce` is the c074 D6 closed-negative — a structural fact, not a numerical claim.
- **Law 4 — Lossless-mode totality.**
  - **Holds on operators?**: YES, read literally off source. `κ=0 ⇒ Q=∞` is the `(vi.mode_port_kappa == 0.0) ? mfem::infinity() :` branch at `:1200-1202`. A total scalar-map edge case, not an error arm.
- **Non-laws (correctly recorded):** no cross-mode combine; not a symmetric-Gram reduction. Both are structural absences, not unverified properties — they strengthen the escape (the verb has FEWER axiom-laws than matrix-weighted-norm, not more).

**Net**: all four laws clear the firm-on-positive-structure bar; none carries inner-product-axiom-class content. The escape applies.

## Proposed changes

### Edit 1 — promote the verb to `firm` (frontmatter + §Status + verified_against)

The full firm `## Status` body + `verified_against:` block land INSIDE the fence below
(fence-parity guard honored — the closing `~~~` sits after the last line; the nested YAML
block is rendered as a triple-backtick fence in the actual file, shown here 4-space-indented
inside the proposed-changes block per the nested-fence guard).

~~~edit:book/src/L4/eigenfreq_qfactor_reduce.md
[replace frontmatter line 4]
firmness: firm
~~~

~~~edit:book/src/L4/eigenfreq_qfactor_reduce.md
[replace the entire `## Status` section — from the line `## Status` through the closing of the verified_against fenced block at the current line 267 — with the following firm body]
## Status

`firm`. **Reasoning (firm-on-positive-structure / syntactic-identity escape):** the
combinator's **structure** is read directly off the two positive readout sites — the
eigenvalue→ω un-transform (`eigensolver.cpp:424-439`) and the Q-factor body
(`postoperator.cpp:1185-1203`) — and **every** law (§Algebraic laws) is a **syntactic
identity** on the per-mode map: law 1 (concatenation-homomorphism) is a read-off of the
inter-mode-stateless readout loop (`eigensolver.cpp:424`, `postoperator.cpp:1180`); law 2
(un-transform purity) folds the **firm L1** [`eigenvalue-untransform`](../L1/eigenvalue-untransform.md)
(c080) then a bare `.real()`; law 3 (Q is a scalar ratio) folds the **firm L1**
[`participation_ratio`](../L1/participation_ratio.md) (c077) into the bare `f/|κ|` quotient
(`:1200-1202`); law 4 (lossless totality `κ=0 ⇒ Q=∞`) is read literally off the
`(κ == 0.0) ? mfem::infinity() :` branch (`:1200-1202`). The eigenpair→`(f,Q)` **assembly**
— `quality_factor = freq_re / std::abs(mode_port_kappa)` (`:1202`) — is bare scalar
arithmetic composing two firm halves; it carries **no axiom requiring an unverified
mathematical property**. This is the same escape that landed
[`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) (c080),
[`assemble_frequency_operator`](./assemble_frequency_operator.md), and
[`frequency_sweep`](./frequency_sweep.md) firm; the contrast is the SIBLING c080
[`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) audit, which RULED OUT the escape
precisely because its norm-axiom laws (triangle / Cauchy–Schwarz / parallelogram) are
theorems conditional on an inner-product structure (SPD/Hermitian `B`) the L0 source only
*numerically asserts*. No such theorem-needing-proof exists in this verb's assembly.

**Both structure-side gates were already discharged before this promotion:** both per-mode
building blocks the verb folds have firm L1 homes — the **eigenvalue un-transform** is firm
L1 [`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) (c080) and the
**κ-participation** half is firm L1 [`participation_ratio`](../L1/participation_ratio.md)
(c077). The earlier `rough-in (test-coverage-bounded)` qualifier was held only on the
absence of a dedicated eigenpair→`(f,Q)` **assembly test** (gate-(b)). The batch-25
meta-phase established the Palace corpus contains **no positive assembly test** (only
output-round-trip-invariance tests), so a new test is out of write-scope — and the OQ
`eigenfreq-qfactor-reduce-firm-needs-assembly-test` named **an in-scope lowering-verifier
law-confidence pass (now that both folded primitives are firm)** as the alternative
promotion route. This dispatch IS that pass: the audit finds the assembly-level laws are
syntactic identities over firm primitives + positive source, carrying no residual untested
semantic claim, so the firm-on-positive-structure escape discharges gate-(b). The existing
PostOperator postprocess unit test (`palace/test/unit/test-postoperator.cpp`, the `[idempotent]`
round-trip) remains supporting **output-invariance** documentation (the κ loss rate
`mode_port_kappa` `:216`/`:259`, the `participation_ratio` fields `:160-188`) — L0-equivalent
evidence the output fields exist and are unit-coherent — but it is **not** the firming basis;
the firming basis is the syntactic-identity escape.

**Scope: 1-of-1 — the eigenmode pipeline's output product.** This is the eigenmode driver's
OWN output-product reduction; it is not a cross-pipeline shared verb (the other four
pipelines have different output products: capacitance/inductance via
[`gram_reduce`](./gram_reduce.md), driven S-parameters via [`sparameter_reduce`](./sparameter_reduce.md),
transient via the field/energy time-history, field-energy via the per-DOMAIN sibling
[`domain_energy_reduce`](./domain_energy_reduce.md)). The disciplined-cross-pipeline-mining-gate
does not apply — this is a single-pipeline output-product verb by design (like
[`frequency_sweep`](./frequency_sweep.md)'s single-witness-driven-by-design scope).

verified_against:

    ```yaml
    verified_against:
      - citation: palace/drivers/eigensolver.cpp:424-439
        verdict: supports
        audited_at: 2026-06-03T200338Z
        note: positive site 1 (the un-transform readout) re-verified on-disk via citecheck --anchor; readout loop start line 424, std::sqrt at line 433 (linear EVP), omega /= 1i at line 438 (quadratic EVP); law 2 is a firm-L1 (eigenvalue-untransform c080) composition over this site, a syntactic identity not a theorem.
      - citation: palace/models/postoperator.cpp:1185-1203
        verdict: supports
        audited_at: 2026-06-03T200338Z
        note: positive site 2 (the Q-factor assembly) re-verified on-disk via citecheck --anchor; resistor_power = 0.5|R|Re(I conj I) at line 1197, mode_port_kappa signed quotient at lines 1198-1199 (firm L1 participation_ratio c077), quality_factor = (kappa==0) ? infinity() else freq_re/|kappa| at lines 1200-1202; the assembly is bare scalar arithmetic over two firm halves — firm-on-positive-structure escape applies (no inner-product-axiom content, the matrix-weighted-norm contrast).
      - citation: palace/models/postoperator.cpp:1171-1222
        verdict: supports
        audited_at: 2026-06-03T200338Z
        note: full MeasureLumpedPortsEig body read on-disk; the per-port loop line 1180 and per-mode readout (eigensolver.cpp line 424) carry NO inter-mode accumulator, so law 1 (concatenation-homomorphism) is a structural read-off of the list-map spine, not a derived theorem.
      - citation: palace/test/unit/test-postoperator.cpp:216-216
        verdict: partially-supports
        audited_at: 2026-06-03T200338Z
        note: mode_port_kappa CHECK-asserted invariant under nondimensionalization (output-invariance documentation of the kappa reduction-output field); supporting, NOT the firming basis (the firm-on-positive-structure escape is) — verdict unchanged from the c079 audit.
      - citation: palace/test/unit/test-postoperator.cpp:160-188
        verdict: partially-supports
        audited_at: 2026-06-03T200338Z
        note: participation_ratio CHECK-asserted round-trip-invariant (output-invariance documentation of the per-mode energy-participation reduction-output); supporting, NOT the firming basis — verdict unchanged from the c079 audit.
      - citation: book/src/L1/eigenvalue-untransform.md
        verdict: supports
        audited_at: 2026-06-03T200338Z
        note: firm L1 home of the folded un-transform half (c080); landed firm on the SAME firm-on-positive-structure escape, so law 2 is a firm-primitive composition.
      - citation: book/src/L1/participation_ratio.md
        verdict: supports
        audited_at: 2026-06-03T200338Z
        note: firm L1 home of the folded kappa-participation half (c077); the resistive kappa = 1/2 R|I|^2/E quotient the verb's kappa closure folds — firm, so law 3 is a firm-primitive composition.
    ```
~~~

### Edit 2 — L4 index consolidated count + cohort move (firm 14→15, rough-in 2→1)

~~~edit:book/src/L4/index.md
[replace the count token on line 32: `**Firm at L4 (14 + 4 outer-driver)**` → `**Firm at L4 (15 + 4 outer-driver)**` (only the parenthetical count changes; the cohort narrative is preserved as-is, with the addition below appended at the end of the firm bullet list after the `fe_assemble` bullet on line 48)]
**Firm at L4 (15 + 4 outer-driver)**
~~~

~~~edit:book/src/L4/index.md
[append a new firm-cohort bullet immediately AFTER the `fe_assemble` bullet (current line 48), before the blank line preceding the `solve-monad outer-driver vocabulary (4)` header]
- [`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md) — the eigenmode **per-mode scalar-ratio reduction combinator**: reduce the converged eigenpair family `[(λᵢ, Eᵢ)]` into a per-mode `(f, Q)` table, `fₘ = Re ωₘ` (the problem-type un-transform) and `Qₘ = ωₘ/κₘ` (the energy/loss ratio, `κ=0 ⇒ Q=∞`). The **reduce-to-scalar-table** member of the L4 algebra-of-folds (sibling of reduce-to-matrix [`gram_reduce`](./gram_reduce.md) + reduce-to-scalar [`inner_product`](./inner_product.md); per-MODE counterpart of the per-DOMAIN [`domain_energy_reduce`](./domain_energy_reduce.md)). Rank-1 per-mode table, NOT a `gram_reduce` family-PAIR grid (c074 D6 closed-negative). Pure value-producing reduction — no `Solve` monad / carry / predicate. Status `firm` (**firm-on-positive-structure / syntactic-identity escape**, cycle-082 lowering-verifier law-confidence pass — every law a read-off syntactic identity on the per-mode map: law 1 the inter-mode-stateless readout-loop homomorphism, law 2 a firm-L1 [`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) c080 composition, law 3 a firm-L1 [`participation_ratio`](../L1/participation_ratio.md) c077 composition into the bare `f/|κ|` quotient, law 4 the literal `κ=0 ⇒ ∞` totality guard; the assembly is bare scalar arithmetic over two firm halves, no inner-product-axiom content — the matrix-weighted-norm contrast). Lowers to the per-mode scalar maps by **identity-in-form on the body** (in-line-marker route; no dedicated L4>L3 theme). **Scope: 1-of-1 — the eigenmode pipeline's output product.** Harvested cycle-075 D3; promoted firm cycle-082 D2.
~~~

~~~edit:book/src/L4/index.md
[replace the rough-in section header on line 56: `**Rough-in at L4 (2)** — the first solver-test-load-driven combinator + the first output-product per-domain energy-table reduction verb, both awaiting law confirmation:` → the decremented header naming only the two remaining rough-in entries (solve_family is the test-coverage-bounded combinator; domain_energy_reduce the per-domain reduction verb still gated on its rough-in matrix-weighted-norm folded primitive)]
**Rough-in at L4 (1 + 1 test-coverage-bounded)** — the per-domain energy-table reduction verb (gated on its `matrix-weighted-norm` rough-in folded primitive + no per-domain test) plus the fixed-operator family-map combinator `solve_family` (`rough-in (test-coverage-bounded)`), both awaiting law confirmation. The eigenmode per-mode reduction [`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md) **promoted to `firm` cycle-082** (firm-on-positive-structure escape; both folded per-mode primitives firm L1 — `eigenvalue-untransform` c080 + `participation_ratio` c077 — and the assembly carries no inner-product-axiom content), moving to the firm cohort above:
~~~

~~~edit:book/src/L4/index.md
[in the dep-map row for eigenfreq_qfactor_reduce (current line 100), replace ONLY the final status cell — the `rough-in (test-coverage-bounded) (...)` parenthetical — with the firm status cell below; the signature / description / lowers-to cells are unchanged]
`firm` (harvested cycle-075 D3 from the eigenmode feature-column forward-mine flags `feature/eigenmode.L4.md:40` + the lifecycle output-product surface; structure read off the 2 positive readout sites eigenvalue-un-transform `eigensolver.cpp:424-439` + Q-factor `postoperator.cpp:1185-1203`; promoted firm cycle-082 D2 on the **firm-on-positive-structure / syntactic-identity escape** — every law a read-off syntactic identity on the per-mode map, both folded per-mode primitives firm L1 (`eigenvalue-untransform` c080 + `participation_ratio` c077), the eigenpair→`(f,Q)` assembly bare scalar arithmetic over two firm halves with no inner-product-axiom content (the matrix-weighted-norm contrast). The existing PostOperator `[idempotent]` postprocess test `palace/test/unit/test-postoperator.cpp` (`mode_port_kappa` :216/:259, `participation_ratio` :160-188) remains output-invariance documentation, NOT the firming basis. Genuine NEW spine vocabulary — the eigenmode output-product reduction verb, NOT a `gram_reduce` specialization, c074 D6 closed-negative)
~~~

### Edit 3 — feature column: verb-gate removed, driver-column gate remains; column STAYS `seed`

The column does NOT promote (its other constituent, the `eigenmode.L4` driver column, is
`seed`). Update the L4 column's §Status reasoning + the constituent matrix status cells +
the prose tail that named the verb as the gate.

~~~edit:book/src/feature/eigenfrequency-qfactor.L4.md
[in the frontmatter `composed_of:` list (line 8), update the verb's status note]
  - book/src/L4/eigenfreq_qfactor_reduce.md (firm — the per-mode scalar-ratio reduction combinator; promoted firm cycle-082, firm-on-positive-structure escape)
~~~

~~~edit:book/src/feature/eigenfrequency-qfactor.L4.md
[in the constituent matrix, replace the `eigenfreq_qfactor_reduce` status cell value `rough-in (test-coverage-bounded)` (line 62) with `firm`, and refresh the L0-site cell's trailing test note to read as output-invariance documentation rather than a gate]
| per-mode scalar-ratio reduction | [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) | firm | `eigensolver.cpp:424-439`, `postoperator.cpp:1171-1203` (the positive structure); `palace/test/unit/test-postoperator.cpp:216,259,160-188` (output-invariance documentation: mode_port_kappa, participation_ratio) |
~~~

~~~edit:book/src/feature/eigenfrequency-qfactor.L4.md
[in the constituent matrix, the folded `Q-factor κ participation` row (line 64) status cell `rough-in` → `firm` (its firm L1 home is participation_ratio c077; the row points at the verb §Semantics but the underlying primitive is firm)]
| Q-factor κ participation (folded) | [`participation_ratio`](../L1/participation_ratio.md) (firm L1; folded by [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md)) | firm | `postoperator.cpp:1188-1203` |
~~~

~~~edit:book/src/feature/eigenfrequency-qfactor.L4.md
[replace the §Body tail sentence (line 55) that gates the column on the verb's rough-in status, with the driver-column-gate version]
The whole output product therefore lowers cleanly outward to the L4 backend surface: `eigenfrequency_qfactor = eigenfreq_qfactor_reduce (ptype, κ) ∘ eigenmode_eigenpairs` — a one-reduction tail on the eigenmode driver column. The reduction verb [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) is now **`firm`** (promoted cycle-082 on the firm-on-positive-structure escape — both folded per-mode primitives firm L1 (`participation_ratio` c077 + `eigenvalue-untransform` c080) and the eigenpair→`(f, Q)` assembly carries no inner-product-axiom content). The column nonetheless STAYS `seed`: a feature column may promote past `seed` only once ALL its composed constituents are firm, and the column's OTHER constituent — the upstream [`eigenmode.L4`](./eigenmode.L4.md) driver column that produces the converged eigenpair family — is itself `status: seed` (not firm). The SOLE remaining column blocker is now the `eigenmode.L4` driver column's own seed→promotion (OQ `eigenmode-driver-column-seed-promotion-blocks-eigenfrequency-qfactor-column`); the verb-side gate (OQ `eigenfreq-qfactor-reduce-firm-needs-assembly-test`) is **discharged**.
~~~

~~~edit:book/src/feature/eigenfrequency-qfactor.L4.md
[in the §Status section (line 68), replace the verb-gate clause with the driver-column-gate clause — the verb is firm; the column's blocker is now the eigenmode.L4 driver column]
`seed` — an output-product **leaf feature column** authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the rank-1 per-mode-table sibling of the rank-2 Gram output products [capacitance](./capacitance.L4.md) / [inductance](./inductance.L4.md). The composition is sound: stage (1) consumes the [`eigenmode.L4`](./eigenmode.L4.md) driver column's converged eigenpair family; stage (2) composes the [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) per-mode scalar-ratio reduction at the problem-type un-transform + resistive-lumped-port κ. The reduction verb is now **`firm`** (cycle-082 lowering-verifier law-confidence pass; firm-on-positive-structure escape — both folded per-mode primitives firm L1, the κ-participation-ratio half via [`participation_ratio`](../L1/participation_ratio.md) (cycle-077) and the eigenvalue-un-transform half via [`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) (cycle-080), and the eigenpair→`(f, Q)` assembly is bare scalar arithmetic over two firm halves carrying no inner-product-axiom content). The column STAYS `seed` because a feature column may promote past `seed` only once ALL its composed constituents are firm, and the column's OTHER constituent — the upstream [`eigenmode.L4`](./eigenmode.L4.md) driver column — is itself `status: seed`. The SOLE remaining column blocker is the `eigenmode.L4` driver column's own seed→promotion (OQ `eigenmode-driver-column-seed-promotion-blocks-eigenfrequency-qfactor-column`). This chapter carries the *compositional* claim (the `(f, Q)` table = the per-mode scalar-ratio reduction over the eigenmode driver's eigenpair family), not the constituents' per-op algebraic claims (those live in [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) and the [`eigenmode.L4`](./eigenmode.L4.md) driver column). The defining structural fact: a rank-1 per-mode scalar-ratio table, NOT a `gram_reduce` family-PAIR grid (c074 D6 closed-negative). Evidence: the L0 readout / Q-factor ranges `eigensolver.cpp:424-439` (the eigenvalue un-transform) + `postoperator.cpp:1171-1203` (`MeasureLumpedPortsEig`, the Q-factor) realizing the reduction, all anchors confirmed on-disk via palace-codemap `read_range` + citecheck `--anchor` this dispatch, plus the constituent down-links.
~~~

Note for L1/L0 feature-column files: the L1 column (`eigenfrequency-qfactor.L1.md`) and L0
column (`eigenfrequency-qfactor.L0.md`) carry the same verb-gate prose in their §Status
sections (L1 line 64; L0 §Status). The integrator should apply the analogous status-note
refresh to those two files (verb now `firm`; column STAYS `seed` on the `eigenmode.L4`
driver-column gate). I do not re-author those full §Status bodies here to avoid
fence-bloat; the surgical change is identical: replace "the verb stays
`rough-in (test-coverage-bounded)` gated SOLELY on gate-(b)" with "the verb is now `firm`
(cycle-082); the column STAYS `seed` on the `eigenmode.L4` driver-column constituent gate."
The L1 column's constituent matrix row (line 60, `Q-factor κ participation` → `rough-in`)
should also flip to `firm` (firm L1 `participation_ratio`).

## Supporting evidence

- `reference/palace/palace/models/postoperator.cpp:1171-1222` — full `MeasureLumpedPortsEig` body read on-disk; the Q-factor assembly `:1197-1202` is bare scalar arithmetic (`resistor_power`, the signed κ quotient, the `(κ==0)?∞:freq_re/|κ|` guard). The per-port loop `:1180` and the per-mode outer loop carry no inter-mode accumulator.
- `reference/palace/palace/drivers/eigensolver.cpp:424-439` — the un-transform readout; `std::sqrt` at `:433`, `omega /= 1i` at `:438`, selector `if (!C && !has_A2)` at `:430`. All confirmed via `tools/citecheck/citecheck.py --anchor`.
- `book/src/L1/eigenvalue-untransform.md` (firm, c080) + `book/src/L1/participation_ratio.md` (firm, c077) — the two folded per-mode primitives; both landed firm on the same firm-on-positive-structure escape.
- `book/src/L1/matrix-weighted-norm.md` (the c080 sibling audit) — the contrast: escape RULED OUT there because its norm-axiom laws (triangle/Cauchy–Schwarz/parallelogram) are theorems over an unverified SPD/Hermitian structure. The opposite outcome under the same test confirms the auditor's discrimination is sound.
- `book/src/L4/assemble_frequency_operator.md` §Status + `book/src/L4/frequency_sweep.md` §Status — precedent firm-on-positive-structure escape statements (closed-form composition of firm constituents over positive source).
- `book/src/L4/index.md` — the consolidated count + dep-map; "counted from each linked chapter's `## Status` line" (c057-meta guard), so the firm count derives from the verb's promoted §Status.
- `scaffolding/open-questions.md:1015,1019` — the OQ `eigenfreq-qfactor-reduce-firm-needs-assembly-test` naming "an in-scope lowering-verifier law-confidence pass" as the promotion route this dispatch executes.

## Open questions / caveats

- **OQ `eigenfreq-qfactor-reduce-firm-needs-assembly-test` — RESOLVED-BY-AUDIT (cycle-082 D2).** The verb promotes to `firm` via the in-scope lowering-verifier law-confidence pass the OQ itself named as the alternative to an (out-of-scope) assembly test. The assembly-level laws are syntactic identities over the two now-firm folded primitives + the positive Q-factor source, carrying no residual untested semantic claim (the firm-on-positive-structure escape). The out-of-scope assembly test is no longer a gate; it would, if it ever existed, add empirical confirmation of the *output values* but not change the *law confidence* (the laws are syntactic, not numerical). Recommend the integrator mark this OQ resolved-by-audit and remove it from the trigger-gated backlog.
- **NEW OQ `eigenmode-driver-column-seed-promotion-blocks-eigenfrequency-qfactor-column` (cycle-082 D2).** With the verb firm, the `eigenfrequency-qfactor.{L4,L1,L0}` feature column's SOLE remaining blocker to promoting past `seed` is its OTHER composed constituent, the `eigenmode.L4` driver column, which is itself `status: seed`. The column cannot promote until the driver column does. *Trigger:* a driver-column seed→promotion pass on `eigenmode.{L4,L1,L0}`. Fold into the feature-surface-spine seed-promotion family.
- **Direction-of-definition:** the verb entry narrates forward (L4 → its per-mode scalar maps → L0 source) per high→low discipline; no reverse-lift content detected. No violation.
- **Inherited-citation drift check:** the c079/c080 `verified_against:` block cited the Q-factor body as `:1188-1203` in some places and `:1185-1203` in others; the verb's §Status/Evidence prose used `:1185-1203`. I confirmed on-disk via citecheck `--anchor` that the κ/Q assembly anchors sit at `:1197` (`resistor_power`), `:1198-1199` (`mode_port_kappa`), `:1200-1202` (`quality_factor`/`infinity`), all within `:1185-1203`; the formula comment is `:1186-1191`. My new `verified_against:` entries use `:1185-1203` (the enclosing block) consistently. The narrower `:1188-1203` used by `participation_ratio` (the κ comment-through-guard sub-range) is also in-range and not in conflict — both are correct enclosing ranges for the κ quotient; I did not "correct" the participation_ratio citation since it is not drifted, only narrower.
- **L1/L0 feature-column §Status surgical refresh** (noted in Edit 3) is left to the integrator as a parallel mechanical change to keep fence-count bounded; the substance is identical to the L4-column §Status edit (verb firm; column seed on the driver-column gate).
