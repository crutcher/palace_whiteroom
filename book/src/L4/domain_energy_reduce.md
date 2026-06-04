---
layer: L4
operator: domain_energy_reduce
rank: firm
edges:
  depends-on:
    - L1/participation_ratio
    - L1/matrix-weighted-norm
  reference:
    - L4/eigenfreq_qfactor_reduce
    - L4/gram_reduce
    - L4/inner_product
variant_axes:
  - field-kind (electric ½⟨E, M_i E⟩ | magnetic ½⟨B, M_i B⟩ — THE load-bearing axis; selects which domain-restricted operator family M_i and which field; the reduction runs twice, once per kind, producing two tables; absorbed into the (M_i, field) pair)
  - element-type (the field may be complex; the energy form sums the real + imaginary radicand contributions, so energyᵢ is a real ≥ 0 reduction of a possibly-complex field; the table is real)
  - partition-coverage (config-conditional: whether the configured domain set partitions the field support — gates the Σ pᵢ = 1 law, NOT the verb's shape)
---

# domain_energy_reduce

The L4 **per-domain energy-table reduction combinator**: reduce a single solution field against a
configured domain-operator map `{idx → M_idx}` into a per-domain `(energyᵢ, pᵢ)` scalar table, where the
per-domain energy `energyᵢ = ½⟨field, M_idx field⟩` is the domain-RESTRICTED SPD energy form and the
participation ratio `pᵢ = energyᵢ / e_total` is the per-domain energy over the whole-domain total. It is
the **domain field-energy output-product reduction** — the verb that turns a solved field into the
per-domain field-energy table with participation ratios the user ran the simulation to inspect (where
field energy concentrates).

`domain_energy_reduce` is a **pure value-producing reduction** (no `Solve` monad, no carry, no
convergence predicate — a post-processing readout, like the eigenmode `(f,Q)` readout). It is the
**reduce-to-scalar-TABLE** rank-1 member of the L4 algebra-of-folds family — the **per-DOMAIN sibling**
of the per-MODE [`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md). Both produce a rank-1 table
of scalar tuples over a family (per-mode vs per-domain), distinct from the rank-2 family-PAIR
[`gram_reduce`](./gram_reduce.md) and rank-2 port-projection
[`sparameter_reduce`](./sparameter_reduce.md). It rises to L4 as a **feature-surface verb the backend
wants** ([`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md)
§"The combinators rise regardless"; directive-1: L4 is the outward backend-lowering target) — the
output-product half of the [`energy-fields`](../feature/energy-fields.L4.md) composition root reaches the
L4 surface through it.

It is **genuine NEW spine vocabulary, NOT a `participation_ratio` fold-inline** — the Wave-1 D4
confirm-probe (cycle-079) probed and REFUSED the bare-`participation_ratio`-fold subsume: the per-domain
numerator `energyᵢ = ½⟨field, M_idx field⟩` is itself a domain-restricted SPD energy reduction (the
load-bearing content), so the verb folds TWO L1 primitives per row, not one. The firm
[`participation_ratio`](../L1/participation_ratio.md):188-191 explicitly disclaims that numerator-energy
reduction as out-of-scope "separate energy-reduction vocabulary, named not authored" — that
named-not-authored vocabulary IS this verb. It is the energy-fields column's OWN reduction verb.

## Context

L4 is **vocabulary** (`L4/index.md:7-13`). `domain_energy_reduce` names the per-domain energy-table
reduction the field-energy postprocess runs on a solved field. It consumes a field-bearing driver
column's solution field (the `electrostatic` / `magnetostatic` / per-step driver field — the energy
table is driver-AGNOSTIC, the same reduction regardless of producer) and the configured
domain-operator map, and maps each configured domain attribute `idx` to its table row:

- the per-domain energy `energyᵢ = ½⟨field, M_idx field⟩`, the domain-restricted SPD energy form (the
  [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) squared radicand `⟨x, B x⟩` with `B = M_idx`
  the operator restricted to one domain attribute);
- the participation ratio `pᵢ = energyᵢ / e_total`, the firm
  [`participation_ratio`](../L1/participation_ratio.md) with the per-domain energy numerator over the
  whole-domain total `e_total` (the un-restricted energy of the same field).

The combinator is defined **in L4 vocabulary** (high→low discipline): its semantics, signature, and laws
are stated in terms of the field and domain-operator map it consumes and the two per-domain scalar maps
it folds — NOT in terms of the L0 C++ readout loop. It is a methodology-level combinator distilled from
the `MeasureDomainFieldEnergy` per-domain loop + the `GetDomainElectric/MagneticFieldEnergy` energy form;
Palace's C++ writes the explicit per-domain loop, not the L4 reduction form.

## Signature

    -- the per-domain energy-table reduction over a solved field against a domain-operator map:
    domain_energy_reduce :: DomainOpMap            -- the configured domain-operator map {idx → M_idx}
                         -> Field                  -- the solved field (E/B; possibly complex)
                         -> Scalar                 -- e_total : the whole-domain total energy (denominator)
                         -> [DomainData]           -- per domain: (idx, energyᵢ = ½⟨field, M_idx field⟩, pᵢ = energyᵢ / e_total)
    domain_energy_reduce doms field e_total =
      [ let energy_i = restricted_energy m_idx field    -- ½⟨field, M_idx field⟩ (the domain-restricted SPD form)
            p_i      = if e_total > 0                    -- the UNIFORM denominator guard (chosen; see §Algebraic laws)
                       then energy_i / e_total           -- the participation_ratio quotient
                       else 0                            -- lossless / energy-free total ⇒ p_i = 0
        in  DomainData idx energy_i p_i
      | (idx, m_idx) <- doms ]                           -- map over the configured domain set (no inter-domain state)
      where
        restricted_energy m field = 0.5 * inner_product field (m `apply` field)   -- ⟨field, M field⟩, real ≥ 0

Shape contract (bunsen-style; named axes):

- `doms : DomainOpMap` — the configured domain-operator map `{idx → M_idx}` (the C++ `DomainPostOperator::M_i`,
  `domainpostoperator.hpp:42`). Read-only. Defines which domains get their own energy row (the reduction's
  index domain) and the domain-restricted SPD operator `M_idx` per domain. See §Record definition.
- `field : Field` — the solved field the energy reduces (the producing driver column's `V`/`E` for the
  electric table, `A`/`B` for the magnetic table; `postoperator.cpp:1032, 1057`). Read-only. May be complex
  (the energy form sums the real + imaginary radicand contributions, `domainpostoperator.cpp:267-272`).
- `e_total : Scalar` — the whole-domain total energy of the same field (the un-restricted
  [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)-squared over the full operator; the
  `GetElectricFieldEnergy` / `GetMagneticFieldEnergy` result, `postoperator.cpp:1033, 1058`). Real ≥ 0.
  Read-only. The shared denominator — computed ONCE, divided into each per-domain numerator.
- result `[DomainData]` — the per-domain energy table (one `DomainData` row per configured domain), each
  carrying `(idx, energyᵢ, pᵢ)`. The `DomainData` element type is defined in
  [`energy-fields.L4`](../feature/energy-fields.L4.md) §"Record definition" (the OUTPUT row, distinct from
  the `DomainOpMap` INPUT; OQ `record-DomainData-needs-definition-home`).

The shape contract makes structural what is conventional in the C++ readout loop:

1. **Each table row is independent (the map is a list homomorphism over domains).** No state threads
   between domains; the reduction collects per-domain rows (`postoperator.cpp:1036-1042` electric loop,
   `:1061-1066` magnetic loop — neither carries an inter-domain accumulator).
2. **The folded numerator is a per-domain RESTRICTED energy**, not a pre-reduced scalar — the load-bearing
   distinction from a bare `participation_ratio` fold: the verb computes `energyᵢ` (a domain-restricted
   `matrix-weighted-norm`-squared) AND the quotient, two folded primitives per row.

## Semantics

`domain_energy_reduce doms field e_total` maps each configured domain to its `(energyᵢ, pᵢ)` row: compute
the domain-restricted energy `energyᵢ = ½⟨field, M_idx field⟩` (the `matrix-weighted-norm`-squared
restricted to domain `idx`), then form the participation `pᵢ = energyᵢ / e_total` (with the
`e_total = 0 ⇒ pᵢ = 0` total-guard). It is a `map`-then-collect with no `Solve` effect — a pure function
`(doms, field, e_total) -> [DomainData]`.

The combinator's structural payoff: the field-energy postprocess's per-domain readout — the
`MeasureDomainFieldEnergy` body that loops over `dom_post_op.M_i`, calls
`GetDomainElectric/MagneticFieldEnergy` per domain, and divides by the whole-domain total — is ONE
reduction over the domain set. The per-domain energy and participation halves are the two scalar
projections of each domain row.

The reduction runs **twice** in the field-energy postprocess — once for the electric field
(`postoperator.cpp:1036-1042`, producing the `domain_E_field_energy_i` table) and once for the magnetic
field (`:1061-1066`, producing `domain_H_field_energy_i`) — the **field-kind** being the load-bearing
variant axis. Each invocation is the SAME reduction shape with `(M_idx, field)` selecting the kind; the
verb is uniform over the axis.

This is the **reduce-to-scalar-table** rank between the reduce-to-scalar
[`inner_product`](./inner_product.md) (one scalar over a tensor) and the rank-2
[`gram_reduce`](./gram_reduce.md) (a matrix over a family-PAIR grid): `domain_energy_reduce` produces a
1-D table of scalar tuples over a domain family (rank-1, per-domain) — the per-domain sibling of the
per-mode [`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md). The upstream is a SINGLE solution
field, not a solution family — there is no family-PAIR `xⱼᵀ K xᵢ` bilinear, no `symmetric_from_upper`
(the load-bearing distinction from `gram_reduce`; the c074 D6 do-NOT-over-unify guard, honored).

## Algebraic laws

Every law is a **syntactic identity on the per-domain map structure**, read off the positive
`MeasureDomainFieldEnergy` loop + the domain-restricted energy form.

1. **Map-independence / concatenation-homomorphism** (the defining fold law).
   `domain_energy_reduce (a ++ b) field e_total = domain_energy_reduce a field e_total ++
   domain_energy_reduce b field e_total` (treating `doms` as the iterated map entries) — each row depends
   only on its own domain's `(idx, M_idx)`; no inter-domain state. Embarrassingly parallel over domains
   (the `eigenfreq_qfactor_reduce` / `gram_reduce` grid-map homomorphism), read off the per-domain
   `emplace_back` loop (`postoperator.cpp:1036-1042`) carrying no accumulator.
2. **Per-domain energy is a domain-restricted `matrix-weighted-norm`-squared.**
   `energyᵢ = ½⟨field, M_idx field⟩` is the [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)
   squared radicand `⟨x, B x⟩` at `B = M_idx`, halved — `0.5 * LocalDot(field, M_idx·field)`
   (`domainpostoperator.cpp:262-274` electric / `:284-296` magnetic). Real ≥ 0 for SPD `M_idx`. This is
   the second folded primitive the bare-`participation_ratio` fold could not absorb.
3. **Numerator-scale-homogeneity in the quotient.** `pᵢ = energyᵢ / e_total` is linear in the numerator
   energy (the firm [`participation_ratio`](../L1/participation_ratio.md) numerator-linearity law) —
   inherited unchanged from the folded quotient primitive.
4. **Shared-denominator invariance.** All per-domain participations of one table share the SAME `e_total`
   (`GetElectricFieldEnergy(field)` / `GetMagneticFieldEnergy(field)`, `postoperator.cpp:1033, 1058`;
   `domain_E_field_energy_all = energy` set once at `:1034`, `domain_H_field_energy_all` at `:1059`) —
   the whole-domain total is computed ONCE per field and divided into each per-domain numerator (the
   `participation_ratio` denominator-shared-invariance law, per-domain instance).
5. **Total-guard totality (the UNIFORM guard — chosen, see below).** `e_total ≤ 0 ⇒ pᵢ = 0` — a total
   edge case handled in the scalar map, NOT an error arm (parallel to `eigenfreq_qfactor_reduce`'s
   `κ = 0 ⇒ Q = ∞` lossless-totality).

Laws that explicitly **do NOT** hold (or hold only config-conditionally):

- **`Σ pᵢ = 1` is CONFIG-CONDITIONAL, NOT an unconditional identity (D4 flag #3).** The participations sum
  to one ONLY when the configured domain set **partitions the field's support** —
  `Σᵢ energyᵢ = e_total ⟺ {M_idx}` partition the whole-domain operator `M`. Palace configures domains
  freely (overlapping, partial-coverage, or partitioning); when the domains do not partition the support,
  `Σ pᵢ < 1` (uncovered energy) or `Σ pᵢ > 1` (overlap double-counting). The verb makes NO partition
  claim; the `partition-coverage` variant axis records the precondition. (Contrast a true partition-of-unity
  reduction where the sum-to-one is structural.)
- **No cross-domain combine.** The reduction does not sum/reduce across domains into a single scalar — it
  is a per-domain map producing one table row each. (The whole-domain total `e_total` is computed by a
  SEPARATE un-restricted energy reduction upstream, NOT by summing the per-domain rows — see law 4.)
- **Not a symmetric-Gram reduction.** No family-PAIR grid, no symmetric mirror — the rank-1 vs rank-2
  distinction from [`gram_reduce`](./gram_reduce.md) (the single solution field is not a family; the c074
  D6 over-unification guard).

### On the uniform total-guard (D4 flag #2)

The two C++ passes guard the participation division **inconsistently**:

- **electric** (`postoperator.cpp:1039`): `participation_ratio = std::abs(energy_i) > 0.0 ? energy_i / energy : 0.0`
  — guards on the **numerator** `energy_i`;
- **magnetic** (`:1064`): `participation_ratio = std::abs(energy) > 0.0 ? energy_i / energy : 0.0`
  — guards on the **denominator** `energy`.

The L4 verb adopts ONE uniform guard: the **denominator guard** `e_total > 0 ⇒ pᵢ = energyᵢ/e_total, else 0`
(the magnetic convention). Rationale: the denominator guard is the actual division-by-zero protection (a
zero-`e_total` field has no total energy to participate in, so `pᵢ = 0` is the only meaningful value); and
it SUBSUMES the numerator-guard case, because a domain with `energyᵢ = 0` under a positive `e_total` already
yields `pᵢ = 0/e_total = 0` without needing a separate numerator test. The electric pass's numerator guard
is incidental (it produces the same `0` for a zero-numerator domain that the denominator guard produces),
so picking the denominator guard loses no source-witnessed behavior while removing the inconsistency. The
inconsistency itself is noted as a Palace source observation (the two passes should agree; flagged in the
report's Open questions for a possible `problems/` drive-by).

## Dependencies

- [`participation_ratio`](../L1/participation_ratio.md) (firm, c077) — the per-domain participation quotient
  `pᵢ = energyᵢ / e_total` this reduction folds (the second of the two folded primitives; the firm L1 home
  for the quotient half).
- [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (firm c091) — the
  domain-restricted SPD energy form `½⟨field, M_idx field⟩` this reduction folds as the per-domain
  numerator (the first folded primitive; promoted to firm by the batch-29 firm-flip-and-cascade wave,
  discharging this verb's former inherited-rough-in gate — both folded primitives are now firm).

Sibling data-algebra reduction combinators (the L4 algebra-of-folds family):

- [`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md) (firm, c082) — the per-MODE scalar-table
  reduction; `domain_energy_reduce` is the per-DOMAIN sibling (same rank-1 scalar-table shape, different
  family index: mode vs domain). Together they are the two rank-1 scalar-table members of the
  algebra-of-folds. (The sibling reached `firm` because BOTH its folded primitives have firm L1 homes —
  `eigenvalue-untransform` c080 + `participation_ratio` c077 — so the firm-on-positive-structure escape
  applies to it; `domain_energy_reduce` does NOT yet share that property, see §Status.)
- [`gram_reduce`](./gram_reduce.md) (reduce-to-matrix) — the rank-2 family-PAIR Gram reduction; the
  do-NOT-merge over-unification guard (single field, not a family; rank-1 table, not a rank-2 grid).
- [`inner_product`](./inner_product.md) (reduce-to-scalar) — the single-tensor reduction; the per-domain
  energy `½⟨field, M_idx field⟩` is a weighted inner product at the single-domain level.

## Record definition

`DomainOpMap` — the configured domain-operator map this reduction's INPUT iterates (the index domain +
per-domain restricted SPD operators). It is the C++ `DomainPostOperator::M_i` (`domainpostoperator.hpp:42`).

| field | type | meaning |
|---|---|---|
| key `idx` | `int` | the domain attribute index (which configured domain this entry describes; becomes the `DomainData.idx` of the produced row) |
| value `M_idx` | `(LinearOperator?, LinearOperator?)` | the per-domain restricted SPD energy operators — a pair `(M_elec, M_mag)`: the electric-energy operator (the ε-weighted mass restricted to domain `idx`) and the magnetic-energy operator (the µ⁻¹-weighted mass restricted to domain `idx`); either may be null (a domain with no operator of that kind contributes `0` energy) |

- **Stratum.** `DomainOpMap` is **construction-time** stratum: the map is built once at `DomainPostOperator`
  construction from the postprocess domain config (the configured domain-attribute set + the material
  operator) and is `readonly` during the per-readout reduction. The reduction iterates it; it does not
  mutate it.
- **L0 source home.** The backing C++ member is
  `std::map<int, std::pair<std::unique_ptr<Operator>, std::unique_ptr<Operator>>> M_i`
  (`palace/models/domainpostoperator.hpp:42`): the key is the domain attribute `int`, the value pair is
  `(electric-energy operator, magnetic-energy operator)`. The electric energy of domain `idx` reads
  `it->second.first` (`domainpostoperator.cpp:262-266`); the magnetic reads `it->second.second`
  (`:284-288`); a null operator returns `0.0` energy (`:262-264, :284-286`).
- **Signatures that name it.** `domain_energy_reduce :: DomainOpMap -> Field -> Scalar -> [DomainData]`
  (this verb). Currently a **single-consumer** record (only this verb takes `DomainOpMap` as input — the
  [`energy-fields`](../feature/energy-fields.L4.md) column composes the verb but does not itself name
  `DomainOpMap`, it names the construction-time `PostprocessConfig` that BUILDS the map and the `DomainData`
  OUTPUT row). So `DomainOpMap` is defined in-chapter here (the single-consumer record-definition home per
  the record-definition obligation). It is DISTINCT from `Measurement::DomainData` (the OUTPUT row, defined
  in `energy-fields.L4.md` §"Record definition", watched by OQ `record-DomainData-needs-definition-home`):
  `DomainOpMap` is the input `{idx → M_idx}`, `DomainData` is the output `(idx, energy, p)`. Flagged for a
  ≥2-consumer promote-watch in Open questions in case a per-domain output-surface chapter names it.

## Lowers to

`domain_energy_reduce` lowers by **identity-in-form on the body** to the per-domain scalar maps it folds
(the domain-restricted energy form `½⟨field, M_idx field⟩` and the participation quotient
`energyᵢ / e_total`). The reduction is a plain per-domain `map` of scalar evaluations — there is no
intervening L3/L2 absorption that reshapes the map. No dedicated L4>L3 theme file — the in-line-marker
route (the [`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md) /
[`inner_product`](./inner_product.md) / [`gram_reduce`](./gram_reduce.md) pattern); the substantive
downward content — the C++ per-domain readout loop (`postoperator.cpp:1036-1042` electric,
`:1061-1066` magnetic), the domain-restricted energy form
(`domainpostoperator.cpp:255-275` / `:277-297`), and the whole-domain total construction
(`postoperator.cpp:1033, 1058`) — lives in the field-energy postoperator L0 and the (firm / rough-in) L1
folded primitives' own L1>L0 rotations. This entry records the rotation direction in-line per high→low
discipline; it does not author a theme.

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

**Scope: 1-of-1 — the field-energy output product, driver-AGNOSTIC.** This is the field-energy
postprocess's reduction; it is driver-agnostic (the SAME per-domain reduction reduces any field-bearing
driver's field — electrostatic `V`/`E`, magnetostatic `A`/`B`, the eigenmode/driven/transient per-step
fields), which is why it is a standalone output-product verb rather than a per-driver stage-3. The
disciplined-cross-pipeline-mining-gate does not apply — this is a single-output-product reduction verb by
design (like [`sparameter_reduce`](./sparameter_reduce.md)'s single-witness-driven-by-design scope), the
per-domain sibling of the per-mode [`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md).

## Evidence

All L0 citations self-verified on-disk this dispatch via `tools/citecheck/citecheck.py --anchor`
(against `reference/palace/`). NOTE: the `palace-codemap` `read_range` was **+1 drifted** on the
`MeasureDomainFieldEnergy` opening-brace boundary — the participation-ratio guard lines are on-disk
`:1039` (electric) / `:1064` (magnetic), NOT the codemap-reported `:1038`/`:1063`; the citations below
are the citecheck-confirmed on-disk numbers.

- **Per-domain energy-table reduction (positive structure):**
  `palace/models/postoperator.cpp:1021-1099` (the `MeasureDomainFieldEnergy()` body), `:1025-1026`
  (`reserve(dom_post_op.M_i.size())` — the domain set being iterated), `:1031-1032` (the electric field
  selection `auto &field = V ? *V : *E`), `:1033` (`auto energy = dom_post_op.GetElectricFieldEnergy(field)`
  — the whole-domain total `e_total`), `:1034` (`domain_E_field_energy_all = energy` — the shared
  denominator set once), `:1036-1042` (the per-domain electric loop:
  `for (const auto &[idx, data] : dom_post_op.M_i) { auto energy_i = GetDomainElectricFieldEnergy(idx, field);
  … emplace_back(DomainData{idx, energy_i, participation_ratio}); }`), `:1039` (the electric participation
  guard `participation_ratio = std::abs(energy_i) > 0.0 ? energy_i / energy : 0.0` — guards the NUMERATOR).
- **Magnetic per-domain loop (the field-kind variant + the inconsistent guard):**
  `palace/models/postoperator.cpp:1056-1057` (the magnetic field selection `auto &field = A ? *A : *B`),
  `:1058` (`auto energy = dom_post_op.GetMagneticFieldEnergy(field)` — the magnetic total), `:1059`
  (`domain_H_field_energy_all = energy`), `:1061-1066` (the per-domain magnetic loop, same shape with
  `GetDomainMagneticFieldEnergy`), `:1064` (the magnetic participation guard
  `participation_ratio = std::abs(energy) > 0.0 ? energy_i / energy : 0.0` — guards the DENOMINATOR; the
  INCONSISTENCY with the electric `:1039` numerator-guard — D4 flag #2, resolved to the uniform denominator
  guard).
- **Domain-restricted energy form `½⟨field, M_idx field⟩` (the folded numerator primitive):**
  `palace/models/domainpostoperator.cpp:255-275` (`DomainPostOperator::GetDomainElectricFieldEnergy(int idx,
  const GridFunction &E)`), `:262-264` (`if (!it->second.first) return 0.0` — null-operator domain
  contributes 0), `:266` (`it->second.first->Mult(E.Real(), D)` — the `M_idx·field` application), `:267`
  (`double dot = linalg::LocalDot(E.Real(), D)` — the `⟨field, M_idx field⟩` inner product), `:268-272`
  (the imaginary radicand contribution for complex fields — `if (E.HasImag()) { … dot += LocalDot(E.Imag(),D) }`),
  `:274` (`return 0.5 * dot` — the `½⟨field, M_idx field⟩` energy form, the `matrix-weighted-norm`-squared
  restricted to domain `idx`); magnetic counterpart `GetDomainMagneticFieldEnergy` `:277-297` (same shape,
  `it->second.second` the magnetic operator, `:296` the `return 0.5 * dot`).
- **`DomainOpMap` record (the input map):** `palace/models/domainpostoperator.hpp:42`
  (`std::map<int, std::pair<std::unique_ptr<Operator>, std::unique_ptr<Operator>>> M_i;` — the
  `{idx → (M_elec, M_mag)}` domain-operator map).
- **Whole-domain total `e_total` (the un-restricted energy, the shared denominator):**
  `palace/models/postoperator.cpp:1033` (`GetElectricFieldEnergy(field)`), `:1058`
  (`GetMagneticFieldEnergy(field)`) — the un-restricted [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)-squared
  over the full operator, supplied as the denominator (NOT part of the per-domain map; a separate upstream
  energy reduction).
- **Supporting test (L0-equivalent, the energy-form constituent):**
  `reference/palace/test/unit/test-domainpostoperator.cpp:83`
  (`double energy_nondim = dom_post_op.GetElectricFieldEnergy(*E_field)` — the whole-domain electric energy),
  `:87-91` (the SI-energy assertion `U = ½·ε₀·E₀²·sx·sy·sz`) — a positive unit-test witness for the
  energy-FORM (the `½⟨field, M field⟩` shape, whole-domain instance), supporting the folded numerator
  primitive's correctness. It does NOT exercise the per-domain restriction or the participation assembly
  (the rough-in test-gate, §Status point 2).
- **Folded L1 primitives:** [`participation_ratio`](../L1/participation_ratio.md) (firm c077 — the
  `energyᵢ/e_total` quotient half; :188-191 disclaims the numerator-energy reduction as "named not authored"
  = THIS verb), [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (rough-in (test-coverage-bounded) —
  the `½⟨field, M field⟩` energy-form half).
- **Sibling-combinator grounding:** [`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md) (the
  per-MODE rank-1 scalar-table sibling), [`gram_reduce`](./gram_reduce.md) (the rank-2 over-unification
  guard), [`inner_product`](./inner_product.md) (the reduce-to-scalar base of the per-domain energy);
  `book/src/concepts/black-box-vs-accelerated-kernels.md` §"The combinators rise regardless" (the
  L4-feature-surface-verb warrant).
- **Composing feature column:** [`energy-fields.L4`](../feature/energy-fields.L4.md) (seed c078 — the
  output-product column that composes this verb; forward-refs this slug at `:8,48,62,134,156` — authoring
  this chapter resolves those plain-text refs to live links).
- **Provenance:** harvested cycle-079 D3 from OQ `domain_energy_reduce-l4-verb-needs-authoring` (c078 D1);
  Wave-1 D4 combinator-miner confirm-probe verdict DISTINCT-VERB-WARRANTED (the per-domain numerator is a
  domain-restricted SPD energy reduction, so the verb folds TWO L1 primitives per row, refusing the bare
  `participation_ratio`-fold-inline subsume). WARRANT verdict: genuine NEW L4 spine vocabulary — the
  field-energy output-product reduction verb, the per-DOMAIN rank-1 scalar-table sibling of the per-MODE
  `eigenfreq_qfactor_reduce`, completing the L4 algebra-of-folds family; NOT a `participation_ratio` fold,
  NOT a `gram_reduce` specialization.

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
