---
layer: L4
operator: eigenfreq_qfactor_reduce
firmness: rough-in
consumes:
  - book/src/L4/eigsolve.md (firm — the opaque eigen-solve cap producing the converged eigenpair family this reduction maps over; the upstream composition-root stage)
lowers_to:
  - the per-mode scalar maps (eigenvalue un-transform + κ participation ratio + f/κ quotient); identity-in-form on the body, no dedicated L4>L3 theme — in-line §"Lowers to". The two scalar-map halves now have firm L1 homes: the eigenvalue un-transform → book/src/L1/eigenvalue-untransform.md (firm, c080); the κ participation ratio → book/src/L1/participation_ratio.md (firm, c077)
variant_axes:
  - problem-type (linear-EVP | quadratic-EVP | nonlinear-EVP — THE load-bearing axis; selects the eigenvalue→ω un-transform; absorbed into the untransform dispatch)
  - loss-source (resistive-lumped-port witnessed; inductive-EPR the participation sibling — absorbed into the κ closure)
  - element-type (complex — pinned; eigenmodes intrinsically complex; f = Re ω, Q from |κ|)
---

# eigenfreq_qfactor_reduce

The L4 **eigenmode per-mode scalar-ratio reduction combinator**: reduce the converged
eigenpair family `[(λᵢ, Eᵢ)]` into a per-mode `(f, Q)` table, where the eigenfrequency
`fₘ = Re ωₘ` is the problem-type un-transform of the eigenvalue and the quality factor
`Qₘ = ωₘ/κₘ` is an energy/loss ratio (`κₘ = ½R·|Iₘⱼ|²/Eₘ`). It is the **eigenmode
output-product reduction** — the verb that turns the raw eigenpairs the eigensolver
returns into the eigenfrequency + Q-factor table the user ran the eigenmode solver to
compute.

`eigenfreq_qfactor_reduce` is a **pure value-producing reduction** (no `Solve` monad, no
carry, no convergence predicate — the eigenmode driver's per-mode readout map is
explicitly NOT a solve-iteration, [`solve_family`](./solve_family.md):146) — the
**reduce-to-scalar-TABLE** member of the L4 algebra-of-folds family, the sibling of the
reduce-to-matrix [`gram_reduce`](./gram_reduce.md) and the reduce-to-scalar
[`inner_product`](./inner_product.md). It rises to L4 as a **feature-surface verb the
backend wants** ([`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md)
§"The combinators rise regardless"; directive-1: L4 is the outward backend-lowering
target) — the output-product half of the eigenmode composition root
([`eigenmode.L4`](../feature/eigenmode.L4.md)) reaches the L4 surface through it.

It is **genuine NEW spine vocabulary, NOT a `gram_reduce` specialization** — c074 D6
probed and REFUSED the eigenmode-as-3rd-Gram-witness subsume: the eigenmode Q-factor is a
per-mode SCALAR-RATIO (rank-1, one `(f,Q)` row per mode), with no family-PAIR grid, the
wrong rank for a symmetric-Gram reduction (`gram_reduce.md:178-189`; OQ
`gram-reduce-third-witness-probe-eigenmode-driven-postprocess`, CLOSED-NEGATIVE). It is
the eigenmode output-product column's OWN reduction verb.

## Context

L4 is **vocabulary** (`L4/index.md:7-13`). `eigenfreq_qfactor_reduce` names the per-mode
scalar-ratio reduction the eigenmode driver runs on its converged eigenpair set. It
consumes the eigenpair family the opaque [`eigsolve`](./eigsolve.md) cap returns (the
eigenmode composition root's stage-2 output, `eigenmode.L4.md:31`), and maps each mode to
its `(f, Q)` table row:

- the eigenfrequency `fₘ = Re ωₘ`, where `ωₘ` is the eigenvalue un-transformed by problem
  type — `ω = √μ` for the linear EVP (`μ = -λ² = ω²`), `ω = λ/i` for the quadratic EVP
  (`λ = iω`);
- the quality factor `Qₘ = ωₘ/κₘ`, where the loss rate `κₘ = ½Rⱼ·|Iₘⱼ|²/Eₘ` is the mode
  coupling participation (the resistor self-energy `½R|I|²` over the mode total energy
  `Eₘ`), with the `κ = 0 ⇒ Q = ∞` (lossless-mode) guard.

The combinator is defined **in L4 vocabulary** (high→low discipline): its semantics,
signature, and laws are stated in terms of the eigenpair family it consumes and the
per-mode scalar maps it folds — NOT in terms of the L0 C++ readout loop. It is a
methodology-level combinator distilled from the eigenmode driver's readout loop + the
`MeasureLumpedPortsEig` Q-factor body; Palace's C++ writes the explicit per-mode loop,
not the L4 reduction form.

## Signature

    -- the eigenmode per-mode scalar-ratio reduction over the converged eigenpair set:
    eigenfreq_qfactor_reduce :: ProblemType                 -- selects the eigenvalue→ω un-transform
                             -> (Mode -> Scalar)            -- the per-mode loss rate κₘ (energy/loss ratio)
                             -> [Eigenpair]                 -- the converged eigenpair family [(λᵢ, Eᵢ)]
                             -> [(Scalar, Scalar)]          -- per mode: (fₘ = Re ωₘ, Qₘ = ωₘ / κₘ)
    eigenfreq_qfactor_reduce ptype kappa eigs =
      [ let omega = untransform ptype lambda               -- ω = √μ (linear) | λ/i (quadratic)
            f     = re omega                               -- eigenfrequency fₘ = Re ωₘ
            k     = kappa mode                             -- loss rate κₘ  (= ½R|Iₘⱼ|²/Eₘ)
            q     = if k == 0 then infinity else f / abs k -- quality factor Qₘ = ωₘ / κₘ
        in  (f, q)
      | (lambda, _E) <- eigs ]                             -- map over the eigenpair family (no inter-mode state)
      where
        untransform Linear    mu  = sqrt mu                -- μ = -λ² = ω²   (linear EVP)
        untransform Quadratic lam = lam / i                -- λ = iω         (quadratic EVP)

Shape contract (bunsen-style; named axes):

- `ptype : ProblemType` — the problem-type selector (`linear-EVP | quadratic-EVP |
  nonlinear-EVP`); read-only. Drives the `untransform` branch (`eigensolver.cpp:430-439`).
- `kappa : Mode -> Scalar` — the per-mode loss-rate closure `κₘ = ½Rⱼ·|Iₘⱼ|²/Eₘ` (the mode
  coupling participation; `postoperator.cpp:1188-1203`). Read-only. Absorbs the loss-source
  variant axis (resistive lumped port the witnessed source).
- `eigs : [Eigenpair]` — the converged eigenpair family ([`eigsolve`](./eigsolve.md)'s
  output; each `(λᵢ, Eᵢ)`). Read-only.
- result `[(Scalar, Scalar)]` — the per-mode `(fₘ, Qₘ)` table (one row per converged mode).

The shape contract makes structural what is conventional in the C++ readout loop:

1. **Each table row is independent (the map is a list homomorphism over modes).** No state
   threads between modes; the reduction collects (`eigensolver.cpp:424` readout loop carries
   no inter-mode accumulator).
2. **The un-transform is a pure per-mode scalar branch** keyed on `ProblemType` — not a
   cross-mode combine.

## Semantics

`eigenfreq_qfactor_reduce ptype κ eigs` maps each converged eigenpair to its `(f, Q)` row:
un-transform the eigenvalue to `ω` by problem type, take `f = Re ω`, compute the loss rate
`κₘ` (the participation ratio), and form `Q = ω/κ` (with the lossless `κ=0 ⇒ Q=∞` guard).
It is a `map`-then-collect with no `Solve` effect — a pure function `(ptype, κ, eigs) ->
[(Scalar, Scalar)]`.

The combinator's structural payoff: the eigenmode driver's per-mode readout — scattered
across the `eigensolver.cpp` readout loop (the un-transform) and the `postoperator.cpp`
`MeasureLumpedPortsEig` body (the Q-factor) — is ONE reduction over the eigenpair family.
The eigenfrequency and quality-factor halves are the two scalar projections of each mode;
the mode-field recovery (`Eᵢ`, `B = -1/(iω)∇×E`) is the eigenmode column's separate stage-3
field readout, NOT part of this `(f,Q)` scalar reduction.

This is the **reduce-to-scalar-table** rank between the reduce-to-scalar `inner_product`
(one scalar over a tensor) and the reduce-to-matrix `gram_reduce` (a matrix over a
family-PAIR grid): `eigenfreq_qfactor_reduce` produces a 1-D table of scalar tuples over a
family (rank-1, per-mode), the wrong rank for a Gram subsume — the c074 D6 closed-negative.

## Algebraic laws

Every law is a **syntactic identity on the per-mode map structure**, read off the two
positive readout sites (the eigenvalue un-transform + the Q-factor body).

1. **Map-independence / concatenation-homomorphism** (the defining fold law).
   `eigenfreq_qfactor_reduce p κ (a ++ b) = eigenfreq_qfactor_reduce p κ a ++
   eigenfreq_qfactor_reduce p κ b` — each row depends only on its own mode's `(λᵢ, κᵢ)`; no
   inter-mode state. Embarrassingly parallel over modes (the `solve_family` / `gram_reduce`
   grid-map homomorphism).
2. **Un-transform purity.** `f = Re(untransform ptype λ)` is a pure scalar map keyed on
   `ProblemType` — `√μ` (linear) vs `λ/i` (quadratic). The branch is absorbed into the
   `untransform` dispatch, not a cross-mode combine.
3. **Q is a scalar ratio, not a bilinear** (the do-NOT-merge-with-`gram_reduce` structural
   identity). `Qₘ = ωₘ/κₘ` is reduce-to-scalar per mode (the `f/|κ|` quotient), NOT a
   family-PAIR `xⱼᵀ K xᵢ` bilinear — there is no `symmetric_from_upper`, no rank-2 grid.
   This is the load-bearing distinction from [`gram_reduce`](./gram_reduce.md).
4. **Lossless-mode totality.** `κ = 0 ⇒ Q = ∞` (`mfem::infinity()`,
   `postoperator.cpp:1201-1202`) — a total edge case handled in the scalar map, NOT an
   error arm.

Laws that explicitly **do not** hold:

- **No cross-mode combine.** The reduction does not sum/reduce across modes — it is a
  per-mode map producing one table row each. (Contrast `inner_product`, which DOES reduce
  across the length axis.)
- **Not a symmetric-Gram reduction.** No family-PAIR grid, no symmetric mirror — the
  rank-1 vs rank-2 distinction from [`gram_reduce`](./gram_reduce.md) (c074 D6
  closed-negative; OQ `gram-reduce-third-witness-probe-eigenmode-driven-postprocess`).

## Dependencies

- [`eigsolve`](./eigsolve.md) (firm) — the opaque eigen-solve cap producing the converged
  eigenpair family this reduction maps over (the eigenmode composition root's stage-2
  output, [`eigenmode.L4`](../feature/eigenmode.L4.md):31).

Sibling data-algebra reduction combinators (the L4 algebra-of-folds family):

- [`gram_reduce`](./gram_reduce.md) (reduce-to-matrix) — the rank-2 family-PAIR Gram
  reduction; `eigenfreq_qfactor_reduce` is the rank-1 per-mode sibling (the c074 D6
  closed-negative non-subsume: different rank, scalar-ratio vs bilinear).
- [`inner_product`](./inner_product.md) (reduce-to-scalar) — the single-tensor reduction;
  `eigenfreq_qfactor_reduce`'s per-mode κ (the `½R|I|²/E` energy ratio) is a small inner
  weighted-reduction at the single-mode level.

## Lowers to

`eigenfreq_qfactor_reduce` lowers by **identity-in-form on the body** to the per-mode
scalar maps it folds (the eigenvalue un-transform `√μ`/`λ/i`, the κ participation ratio
`½R|I|²/E`, and the `f/κ` quotient). The reduction is a plain per-mode `map` of scalar
evaluations — there is no intervening L3/L2 absorption that reshapes the map. No dedicated
L4>L3 theme file — the in-line-marker route (the
[`inner_product`](./inner_product.md) / [`gram_reduce`](./gram_reduce.md) pattern); the
substantive downward content (the C++ readout loop, the problem-type un-transform branch
`eigensolver.cpp:430-439`, the κ computation `postoperator.cpp:1188-1203`) lives in the
eigenmode driver / postoperator L0 and the firm L1 scalar-map primitives. **Both scalar-map
halves now have firm L1 homes:** the eigenvalue un-transform `√μ`/`λ/i` →
[`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) (firm, c080); the κ participation
ratio `½R|I|²/E` → [`participation_ratio`](../L1/participation_ratio.md) (firm, c077). This entry
records the rotation direction in-line per high→low discipline; it does not author a theme.

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
1. **(gate-(a) — DISCHARGED, c080).** Both per-mode building blocks the verb folds now have firm L1
   homes: the **eigenvalue un-transform** is firm L1
   [`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) (c080 — the `√μ`/`λ/i` per-mode scalar
   branch keyed on EVP-degree, citing the verb's own un-transform site `eigensolver.cpp:430-439`),
   and the **κ-participation** half is firm L1
   [`participation_ratio`](../L1/participation_ratio.md) (c077 — the resistive κ loss-rate ratio
   `½R|I|²/E`, citing the verb's own κ site `postoperator.cpp:1188-1203`). The structure-firmness
   primitive-maturity gate is now fully discharged on both folded scalar maps; and
2. **(gate-(b) — STILL OPEN, out of write-scope).** the test asserts reduction-OUTPUT invariance over
   the randomly-populated `Measurement` cache, NOT the eigenpair→`(f,Q)` **assembly map** — the
   `(f, Q)` output scalars `cache.freq` / `cache.eigenmode_Q` / the lumped-port `quality_factor` are
   populated-but-not-CHECK-asserted in the idempotency test (the asserted `quality_factor` at
   `:335-342` is `interface_eps_i` dielectric Q, a different output product), so the assembly-level
   laws are still test-unconfirmed.

Promotion route (to `firm`): gate-(a) is **discharged** (both folded per-mode primitives are now firm
L1 — the eigenvalue un-transform [`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) c080 + the
κ-participation [`participation_ratio`](../L1/participation_ratio.md) c077); the SOLE remaining gate is
**(b)** a dedicated eigenmode-postprocess assembly test (exercising the un-transform + κ-from-`E`/`I`
computation, not just output-cache round-trip) OR a lowering-verifier pass raising the assembly-map
confidence to `inner_product`-equivalent. (Contrast the rank-2 sibling [`gram_reduce`](./gram_reduce.md),
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

verified_against:

```yaml
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

## Evidence

All L0 citations self-verified on-disk this dispatch via the codemap
(`mcp__palace-codemap__read_range` + `search_text` line pinpoints against
`reference/palace/`).

- **Eigenfrequency un-transform (positive site 1):** `palace/drivers/eigensolver.cpp:424`
  (the `for (int i = 0; i < num_conv; i++)` readout loop start), `:427`
  (`std::complex<double> omega = eigen->GetEigenvalue(i)`), `:430-434` (`omega =
  std::sqrt(omega)` — linear EVP `μ = -λ² = ω²`), `:435-439` (`omega /= 1i` — quadratic EVP
  `λ = iω`), `:458` (`post_op.MeasureAndPrintAll(i, E, B, omega, …)` — the per-mode
  measure+record), `:471` (loop close), `:472-475` (`MFEM_VERIFY(num_conv >= …n)`). Firm L1 home:
  [`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) (c080).
- **Quality-factor body (positive site 2):** `palace/models/postoperator.cpp:1171-1172`
  (`void PostOperator<solver_t>::MeasureLumpedPortsEig() const` def), `:1177` (`auto freq_re
  = measurement_cache.freq.real()` — `f = Re ω`), `:1188-1191` (the `κ_mj = ½R_j I_mj²/E_m`
  + `Q_mj = ω_m/κ_mj` formula comment), `:1196-1198` (`resistor_power = 0.5·|data.R|·Re(I·conj(I))`),
  `:1198-1199` (`mode_port_kappa = copysign(resistor_power/energy_electric_all, …)`),
  `:1200-1202` (`quality_factor = (κ==0) ? mfem::infinity() : freq_re/|κ|`), loop
  `:1180-1221`. Inductive-port participation sibling (NOT a Q): `:1215-1219`.
- **Feature-chapter forward-mine flags (the §reduction stage that flagged the mine):**
  `book/src/feature/eigenmode.L4.md:40,45,55,70`, `book/src/feature/eigenmode.L1.md:36,41,57,61`,
  `book/src/feature/eigenmode.L0.md:29,36`, `book/src/feature/lifecycle.L4.md:44`,
  `book/src/feature/lifecycle.L1.md:41`, `book/src/feature/lifecycle.L0.md:40,45`.
- **Sibling-combinator grounding:** `book/src/L4/gram_reduce.md` (the reduce-to-matrix
  sibling + the c074 D6 closed-negative non-subsume at `:178-189`),
  `book/src/L4/inner_product.md` (the reduce-to-scalar sibling),
  `book/src/concepts/black-box-vs-accelerated-kernels.md` §"The combinators rise regardless"
  (the L4-feature-surface-verb warrant).
- **No dedicated test** exercises the eigenmode postprocess Q-factor / eigenfrequency
  reduction (the `MeasureLumpedPortsEig` body + the readout loop are integration-level under
  the eigenmode `Solve(mesh)` driver, not unit-tested under `reference/palace/test/unit/`) —
  the rough-in test-gate.
- **Provenance:** harvested cycle-075 D3 from the eigenmode feature-column forward-mine flags
  (`eigenmode.L4.md:40` + the lifecycle output-product surface); c074 D6 established this is a
  per-mode scalar ratio (NOT a `gram_reduce` family-pair), so this is genuine NEW spine
  vocabulary (combinator-as-entry). WARRANT verdict: genuine L4 entry (the eigenmode
  output-product reduction verb; the reduce-to-scalar-table member of the L4 algebra-of-folds,
  a navigable L4 home for the eigenmode `(f,Q)` reduction — NOT a stranded mine, NOT a
  `gram_reduce` specialization).
