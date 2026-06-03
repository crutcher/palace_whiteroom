---
agent: combinator-miner
invoked_at: 2026-06-03T154000Z
scope: Harvest/mine — participation_ratio L1 primitive (firms eigenfreq_qfactor_reduce gate-a)
status: pending
integrated_at: 2026-06-03T154500Z
integration_commit: 8e54d0f4a22185f0fa1aed38cb930fdb19f8aaea
integration_notes: "Applied clean from the report's `new:` block (staging row 4/5). Firm L1 participation_ratio (energy-participation-ratio scalar-quotient; firm-on-positive-structure; numerator-energy-source + signed-vs-unsigned variant axes; NO L2 by warrant). Firms eigenfreq_qfactor_reduce gate-a (reduce verb STAYS rough-in, 2nd gate = dedicated reduction test). L1 count bumped 27->28 main / 34->35 grand (D5 closed to 29/36). DISPATCH-PHASE WRITE-PARTITION LEAK: combinator-miner authored book/ directly during dispatch; repairer reverted + repackaged the body verbatim into the `new:` block, applied byte-matched (revert-dispatch-phase-book-mutation skill); recovered clean, no content lost; friction data-point for batch-24 meta-phase. Build clean."
---

# CYCLE: Combinator candidate (harvested) — participation_ratio (L1)

## Summary

Palace's eigenmode postprocess computes **three** per-mode energy-participation quantities —
the resistive lumped-port loss rate `κ_mj = ½R_j|I_mj|²/E_m`, the inductive energy-participation
ratio `p_mj = ½L_j|I_mj|²/E_m`, and the surface-dielectric participation
`p_mj = ½t_j·Re{∫(ε_jE)ᴴE}/(E_elec+E_cap)` — each written inline as a `numerator/denominator`
division in two postprocess methods. All three are **one quotient of a pre-computed sub-energy
over a total mode energy**; they differ ONLY in how the numerator energy is computed (a
computation that lives strictly below the quotient) and whether a `copysign(·, Re I)` orientation
tag is attached. This is the `½X|I|²/E` / `energy/E_total` shape that the L4 reduction
[`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) folds via its
`kappa : Mode -> Scalar` closure parameter but has **no firm L1 home** (OQ
`participation-ratio-l1-primitive-as-eigenfreq-qfactor-firming-route`, c075 D3). I authored the
firm L1 home `book/src/L1/participation_ratio.md` (the shared scalar-quotient primitive) at
**`firm`** (firm-on-positive-structure — every law is a syntactic identity on the bare quotient,
read off three positive Palace sites; the no-dedicated-test caveat is non-gating per the
`reciprocal`/`apply_linop`/`eigsolve`-c022 precedent). This firms **gate-a** of the
`eigenfreq_qfactor_reduce` rough-in. NO L2 entry (the quotient is a bare scalar division — an L2
mirror would be the identity-in-named-terms smell the 2026-06-01 vocabulary-shift redirect warns
against). The `eigenfreq_qfactor_reduce` / eigenfrequency-qfactor-column re-anchor is double-gated
and NOT done here (coupled-column pass, later cycle) — NOTED only.

## Pattern instances

Three witnesses establish the ≥2-member `½X|I|²/E` cohort (the parametric-family family-detection
trigger: the SAME quotient shape represented 3× but unified 0×; verified via `palace-codemap`
`read_range` this dispatch):

- **Instance 1 — resistive lumped-port loss rate κ:** `palace/models/postoperator.cpp:1196-1199`
  — `resistor_power = 0.5*|data.R|*Re(I·conj(I))` (the `½R|I|²` self-energy numerator), then
  `vi.mode_port_kappa = copysign(resistor_power / energy_electric_all, I_mj.real())` (the SIGNED
  quotient). Defining comment `:1188-1191`.
- **Instance 2 — inductive energy-participation ratio p:** `postoperator.cpp:1148`
  (`vi.inductor_energy = 0.5*|data.L|*Re(I·conj(I))` — the `½L|I|²` self-energy, SAME shape as the
  resistor with `L` for `R`), then `:1217-1218`
  (`vi.inductive_energy_participation = copysign(vi.inductor_energy / energy_electric_all,
  I_mj.real())` — identical SIGNED quotient). Comment `:1209-1213`.
- **Instance 3 — surface-dielectric participation p:** `postoperator.cpp:1364` (`energy =
  surf_post_op.GetInterfaceElectricFieldEnergy(...)` — the `½t·Re{∫(εE)ᴴE}` surface-integral
  numerator), then `:1366` (`energy_participation_p = energy / energy_electric_all` — the UNSIGNED
  quotient). Comment `:1346-1357`; numerator integral `surfacepostoperator.cpp:332-345`.

Shared denominator: `E_m = E_elec + E_cap = domain_E_field_energy_all + lumped_port_capacitor_energy`
(`postoperator.cpp:1178-1179`, identical `:1358-1359`), computed once per mode.

## Proposed combinator (harvested as firm L1 entry this cycle)

- **Slug**: `participation_ratio`
- **Layer**: **L1** (with rationale below — NOT L2)
- **Signature sketch** (authored in full in the L1 entry):
  - `participation_ratio :: Scalar -> Scalar -> Scalar` (i.e. `energy / e_total`)
  - `participation_ratio_signed :: Scalar -> Scalar -> Scalar -> Scalar` (i.e. `copysign(energy/e_total, re_I)`)
- **Algebraic intuition**: numerator-linearity / scale-homogeneity (`p(k·e, t) = k·p(e,t)` — what
  lets the `R`/`L`/`t` scale factors and the numerator-energy SOURCE vary), denominator-shared
  invariance (all per-mode participations divide by the SAME once-computed `E_m`), sign-orientation
  factoring (the `copysign` is a post-quotient tag, not a term in the ratio). NO internal lossless
  guard — the `Q=∞` totality edge is the consumer's (`Q=ω/κ` step), not the quotient's. NOT a
  reduction (operands are already-reduced scalars).
- **Variant axes**: (1) **numerator-energy source** (resistive `½R|I|²` | inductive `½L|I|²` |
  surface-dielectric `½t·Re{∫(εE)ᴴE}`) — the load-bearing axis; the computation lives BELOW the
  quotient, the quotient is uniform over it; (2) **signed-vs-unsigned** (κ/EPR carry the
  `copysign(·, Re I)` orientation; surface-dielectric `p` is unsigned); (3) element-type (numerator
  energies are real reductions of complex fields; the ratio is real).

**This is a non-fold parametric family unified by a shared SHAPE, harvested directly as its firm
L1 home** (not left as a candidate, per the dispatch's harvester mandate). The three siblings are
the SAME `energy/E_total` quotient differing along the numerator-energy-source axis; the unifying
"law" is the quotient identity itself plus numerator-linearity (which is what makes the
numerator-source variable). This is NOT a fold (no reduce-over-a-collection, no combining-step
identity, no concatenation homomorphism) — it is a scalar arithmetic atom shared across three call
sites, the `reciprocal`/`nrm2`-class of elementary post-reduction primitives.

### Layer rationale (L1, not L2)

L1 is correct: `participation_ratio` is a bare scalar quotient of two already-reduced energies — a
mutation-lifted form of the inline `numerator/denominator` divisions Palace writes (the L1
mutation-rotation layer). It is NOT a composition of L1 base primitives (it IS a base primitive),
so there is no L2 fusion content to shift. An L2 entry would be a thin `p = e/t` mirror — exactly
the **identity-in-named-terms smell** the 2026-06-01 vocabulary-shift redirect flags as "the
vocabulary failed to shift". NO L2 entry; the in-line §"Downward to L0" records the bare-quotient
rotation (the `reciprocal` in-line-marker route, no dedicated L1>L0 theme).

### Over-unification guard

- The **numerator-energy computations** (`½X|I|²` self-energy; `½t·Re{∫(εE)ᴴE}` surface integral;
  `E_elec`/`E_cap` domain/cap energies) are a DIFFERENT cohort — energy *reductions*, below the
  quotient. They must NOT be subsumed into `participation_ratio` (which is the bare division). They
  are the eigenmode/energy-fields output-product column's separate energy-readout vocabulary
  (named, not authored; plan CYCLE-076 #5 `energy-fields-output-product-column`).
- The **`Q = ω/κ` / `Q = 1/(tanδ·p)` consumers** (with their `κ==0 ⇒ ∞` totality guards) are NOT
  this primitive — `participation_ratio` is the quotient; the `Q`-forming step is the L4
  reduction's job. Do not fold the `Q` edge case into the ratio.
- This is NOT a BLAS-1 reduction sibling (`dot`/`nrm2` reduce over a length axis; this consumes
  already-reduced scalars — no reduction inside).

## Proposed changes

### 1. New L1 entry (full file body — delivered via proposed-changes channel)

The firm L1 chapter body (status `firm`, firm-on-positive-structure), delivered through the
proposed-changes channel per the write-partition (repaired cycle-077: the dispatch phase had
written this body directly to `book/src/L1/participation_ratio.md`; that on-disk leak was reverted
and the verbatim body relocated here so the integrator applies it normally). Body uses indented
code blocks throughout — no nested triple-backtick fences, so the outer fence is intact.

```new:book/src/L1/participation_ratio.md
---
layer: L1
operator: participation_ratio
firmness: firm
depends_on: []
variant_axes:
  - numerator-energy-source (resistive-self-energy ½R|I|² | inductive-self-energy ½L|I|² | surface-dielectric ½t·Re{∫(εE)ᴴE}) — selects how the numerator energy is computed; the computation lives BELOW this ratio, the ratio is uniform over it
  - signed-vs-unsigned (κ / EPR carry a `copysign(·, Re I)` orientation sign keyed on the port current phase; the surface-dielectric `p` is unsigned) — a post-quotient orientation tag, not part of the quotient
  - element-type (the numerator energies are real-valued reductions of complex fields; the ratio is real)
---

# participation_ratio

The L1 **energy-participation-ratio primitive**: the dimensionless ratio of a
pre-computed sub-energy `energy` to a total mode energy `E_total`,

    p = energy / E_total          (signed variant: p = copysign(energy / E_total, Re I))

`participation_ratio` is the **single scalar quotient** shared by Palace's three
eigenmode-postprocess participation quantities — the resistive lumped-port loss rate
`κ_mj = ½R_j|I_mj|² / E_m`, the inductive energy-participation ratio `p_mj = ½L_j|I_mj|² / E_m`,
and the surface-dielectric participation `p_mj = ½t_j·Re{∫_{Γ_j}(ε_jE_m)ᴴE_m dS} / (E_elec + E_cap)`.
All three are **one quotient of a sub-energy over a total energy**; they differ only in
*how the numerator energy is computed*, a computation that lives strictly BELOW this ratio.

It is the **per-mode `κ` / `p` scalar building block** that the L4 eigenmode reduction
[`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) folds: the loss-rate closure
`κ : Mode -> Scalar` that combinator takes as a parameter IS a `participation_ratio` with the
resistive-self-energy numerator (`eigenfreq_qfactor_reduce.md:54-56,87-89`). This entry firms
the first of that combinator's two rough-in gates — the `½X|I|²/E` per-mode energy-ratio gate
(OQ `participation-ratio-l1-primitive-as-eigenfreq-qfactor-firming-route`, c075 D3).

## Context

L1 re-expresses Palace's source operations as pure functions (`L1/index.md:1-3`). The three
participation computations are scattered across `PostOperator::MeasureLumpedPortsEig` (the
resistive κ and inductive EPR) and `PostOperator::MeasureInterfaceEFieldEnergy` (the surface
dielectric `p`), each written as an inline `numerator / denominator` division with its own
numerator-energy computation spliced in. `participation_ratio` names the **shared quotient
step** as one pure function, leaving the numerator-energy computation to the caller (the
resistor/inductor self-energy `½X|I|²`, or the surface integral `½t·Re{∫(εE)ᴴE}`).

The operator is defined **in L1 vocabulary** (high→low discipline): its semantics, signature,
and laws are stated in terms of the two scalar energies it divides — NOT in terms of the L0
C++ postprocess loops. The forward narration of how this L1 quotient rewrites into the Palace
source sites is the §"Downward to L0" section.

This is **not** an `apply_linop` / BLAS-1-reduction sibling — the operands are already-reduced
real scalars (mode energies), not tensors; `participation_ratio` is the **scalar-quotient
post-reduction step** that consumes the outputs of energy reductions. It is the elementary
arithmetic atom of the eigenmode output-product readout, the way [`nrm2`](./nrm2.md) is the
elementary `√·` of a reduction.

## Signature

    -- the energy-participation ratio: a sub-energy over a total mode energy
    participation_ratio :: Scalar          -- energy   : the pre-computed sub-energy (numerator; ≥ 0)
                        -> Scalar          -- e_total  : the total mode energy (denominator; ≥ 0)
                        -> Scalar          -- p        : the dimensionless participation ratio energy / e_total
    participation_ratio energy e_total = energy / e_total

    -- the signed variant (lumped-port κ / EPR): orientation tag from the port current phase
    participation_ratio_signed :: Scalar       -- energy : the self-energy ½X|I|²  (X ∈ {R, L})
                              -> Scalar         -- e_total
                              -> Scalar         -- re_I  : Re(I_mj), the port current real part (orientation)
                              -> Scalar         -- p     : copysign(energy / e_total, re_I)
    participation_ratio_signed energy e_total re_I = copysign (energy / e_total) re_I

Shape contract (bunsen-style; named axes):

- `energy : Scalar` — the pre-computed numerator sub-energy. Real-valued and non-negative
  (a self-energy `½X|I|²` or a surface-integral energy). Read-only. The **numerator-energy
  source** variant axis selects how it is computed (resistive / inductive / surface-dielectric);
  that computation is BELOW this primitive.
- `e_total : Scalar` — the total mode energy denominator `E_m = E_elec + E_cap`
  (`postoperator.cpp:1178-1179`). Real-valued and non-negative. Read-only.
- `re_I : Scalar` (signed variant only) — the real part of the port current `I_mj`, used only
  as the `copysign` orientation argument. The sign is an orientation tag, NOT part of the ratio
  magnitude.
- result `p : Scalar` — the dimensionless participation ratio (a pure number; energies cancel
  units). For the κ usage it has units of energy-rate after the `Q = ω/κ` consumer applies ω;
  `participation_ratio` itself is the dimensionless `½R|I|²/E` shape (the `R` carries the rate
  dimension at the call site, not in the quotient).

The shape contract makes structural what is conventional in the three C++ sites: each is the
SAME quotient of a real numerator energy by the real total mode energy, with an optional
`copysign` orientation. There is no tensor operand and no reduction inside this primitive — the
reductions that produce `energy` and `e_total` happen before it.

## Semantics

`participation_ratio energy e_total` returns the dimensionless quotient `energy / e_total`.
It is a pure scalar function — no state, no effect, no tensor. The signed variant attaches a
`copysign(·, Re I)` orientation tag keyed on the port current phase (the lumped-port κ and
inductive-EPR convention) without changing the magnitude.

The three Palace participation quantities are recovered by supplying the numerator energy:

- **Resistive lumped-port loss rate** `κ_mj = participation_ratio_signed (½R_j·Re(I·conj I)) E_m (Re I)`
  — the resistor self-energy `½R|I|²` (`postoperator.cpp:1196-1198`) over the total mode energy,
  signed by the current phase (`:1198-1199`). The `Q = ω/κ` consumer is the L4 reduction's job,
  NOT this primitive.
- **Inductive energy-participation ratio** `p_mj = participation_ratio_signed (½L_j·Re(I·conj I)) E_m (Re I)`
  — the inductor self-energy `½L|I|²` (`postoperator.cpp:1148`) over the same total mode energy,
  signed (`:1217-1218`). SAME quotient as κ, different numerator self-energy (`L` for `R`).
- **Surface-dielectric participation** `p_mj = participation_ratio energy_surf (E_elec + E_cap)`
  — the surface energy `energy = ½t·Re{∫(εE)ᴴE}` (`GetInterfaceElectricFieldEnergy`,
  `surfacepostoperator.cpp:332-345`) over the total electric energy (`postoperator.cpp:1366`).
  Unsigned (no port current).

The operator's structural payoff: the three participation computations — written inline three
times in two postprocess methods — are ONE quotient. The differences (which self-energy, signed
or not) are the **numerator-energy source** and **signed** variant axes; the quotient itself is
uniform. The lossless guard (`E_total = 0` or `energy = 0`) is handled at the **consumer** (the
`Q = ω/κ` step: `κ = 0 ⇒ Q = ∞`, `postoperator.cpp:1200-1202`; `p = 0 ⇒ Q = ∞`, `:1367-1370`),
not inside this quotient — `participation_ratio` is the bare division, the `Q` totality edge
case belongs to the `Q`-forming consumer.

## Algebraic laws

Every law is a **syntactic identity on the scalar quotient**, read off the three positive sites.

1. **Quotient definition.** `participation_ratio e t = e / t` — the bare division (the three
   sites are each one `/`: `:1199`, `:1218`, `:1366`).
2. **Numerator-linearity / scale-homogeneity.** `participation_ratio (k·e) t = k · participation_ratio e t`
   — the ratio is linear in the numerator energy. This is what lets the numerator-energy source
   vary (the `R` / `L` / `t` scale factors at the call sites are pulled through the quotient).
3. **Denominator-shared invariance.** All per-mode participations of one mode share the SAME
   denominator `E_m` (`:1178-1179`, `:1358-1359` are the identical `domain_E_field_energy_all +
   lumped_port_capacitor_energy` expression) — the total mode energy is computed once and divided
   into each numerator. Sum-of-participations over loss channels with the same numerator-energy
   convention sums the numerators: `Σ_j p_j = (Σ_j energy_j) / E_m`.
4. **Sign-orientation factoring** (signed variant). `participation_ratio_signed e t s =
   sign(s) · |e/t|` (for `e, t ≥ 0`) — the orientation tag factors out of the magnitude; it is
   a post-quotient `copysign`, not a term inside the ratio (`std::copysign(resistor_power /
   energy_electric_all, I_mj.real())`, `:1198-1199`; same shape `:1217-1218`).
5. **Dimensionlessness** (for matched-unit energies). When numerator and denominator are both
   energies (the surface-dielectric and inductive-EPR cases), `p` is a pure number; for the
   resistive κ the `R` factor in the numerator carries the rate dimension, so κ has units of
   energy-rate — the quotient structure is identical, only the numerator's dimension differs.

Laws that explicitly **do not** hold:

- **No internal lossless guard.** `participation_ratio e 0` is the bare `e/0` — the `Q = ∞`
  totality handling is the **consumer's** (`Q = ω/κ` with `κ == 0 ⇒ ∞`), NOT this primitive's.
  This is the deliberate division of labor: `participation_ratio` is the quotient; the `Q`
  edge case lives in the `Q`-forming step.
- **Not a reduction.** The operands are already-reduced scalars; there is no length axis, no
  sum, no inner product inside this primitive (contrast [`dot`](./dot.md) / [`nrm2`](./nrm2.md),
  which DO reduce). The energy reductions that produce `energy` and `e_total` are separate
  upstream steps.

## Downward to L0

`participation_ratio` lowers by **identity-in-form on the quotient** to the three Palace
postprocess division sites — each is the literal `numerator / denominator` (plus an optional
`copysign`) this primitive names. There is no intervening reshape: the L1 quotient IS the C++
division. The substantive downward content is the **numerator-energy computations** that sit
below the quotient (the resistor/inductor self-energy `0.5 * |X| * Re(I·conj(I))`,
`postoperator.cpp:1148,1196-1198`; the surface integral `GetInterfaceElectricFieldEnergy`,
`surfacepostoperator.cpp:332-345`) and the **denominator construction** `E_m = E_elec + E_cap`
(`postoperator.cpp:1178-1179`) — those are separate energy-reduction steps, not part of this
quotient primitive. No dedicated L1>L0 theme file is authored: the rotation is the bare-quotient
identity (the [`reciprocal`](./reciprocal.md) / BLAS-1-leaf in-line-marker route); this entry
records the rotation direction in-line per high→low discipline.

The numerator-energy and total-energy computations are candidates for their own L1 energy
primitives (an energy-reduction cohort — `domain_E_field_energy`, the `½X|I|²` self-energy, the
surface-integral energy); those are the eigenmode/energy-fields output-product column's separate
energy-readout vocabulary, NOT this quotient. They are named here as the upstream producers, not
authored (the `energy-fields-output-product-column` plan item, CYCLE-076 #5).

## Status

`firm`. **Reasoning (firm-on-positive-structure):** the quotient structure is read directly off
three positive Palace sites — the resistive κ (`postoperator.cpp:1188-1203`), the inductive EPR
(`:1215-1219`), and the surface-dielectric `p` (`:1346-1373`) — establishing the ≥2-member
cohort (three witnesses). Every law (§Algebraic laws) is a **syntactic identity on the scalar
quotient** (a bare division plus an optional `copysign`), not a convergence/numerical claim. Per
the `apply_linop` / `jacobi-smoother` / `eigsolve` (cycle-022) firm-on-positive-structure
precedent, the **absence of a dedicated unit test** for the eigenmode participation postprocess
(the `MeasureLumpedPortsEig` / `MeasureInterfaceEFieldEnergy` bodies are integration-level,
exercised only through the full eigenmode `Solve(mesh)` driver — no `test/unit/` coverage) does
**not** gate firm: syntactic-identity quotient laws are not test-gated (the `eigsolve`-rough-in
case was driven by literature-inferred convergence semantics, absent here — this is bare
arithmetic on positive source).

The numerator-energy and total-mode-energy computations BELOW the quotient are deliberately
out of this primitive's scope (separate energy-reduction vocabulary, named not authored); their
absence does not gate this entry — `participation_ratio` is firm *as the quotient*, the way
`reciprocal` is firm as the bare `1/x` independent of what produces `x`.

**Coupled re-check (NOTE, not enacted this cycle):** firming `participation_ratio` discharges
**gate-a** of the L4 [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) rough-in
(its κ-participation closure now has a firm L1 home). That combinator's promotion is
**double-gated** (firm L1 home AND a dedicated eigenmode-postprocess reduction test, or a
lowering-verifier law-confidence pass) and remains `rough-in` until the second gate is
addressed; re-anchoring `eigenfreq_qfactor_reduce` (and the eigenfrequency-qfactor feature
column) is a coupled-column pass for a later cycle, NOT done here (OQ
`eigenfreq-qfactor-reduce-status-promotion-double-gated`).

## Evidence

All L0 citations self-verified on-disk this dispatch via the codemap
(`mcp__palace-codemap__read_range` + `search_text` line pinpoints against `reference/palace/`).

- **Resistive lumped-port loss rate κ (witness 1):** `palace/models/postoperator.cpp:1188-1191`
  (the `κ_mj = ½R_j I_mj²/E_m` + `Q_mj = ω_m/κ_mj` formula comment), `:1196-1197`
  (`resistor_power = 0.5 * std::abs(data.R) * std::real(I_mj * std::conj(I_mj))` — the `½R|I|²`
  self-energy numerator), `:1198-1199` (`vi.mode_port_kappa = std::copysign(resistor_power /
  energy_electric_all, I_mj.real())` — the SIGNED quotient `½R|I|²/E`), `:1200-1202` (the
  `Q = ω/κ` consumer with the `κ==0 ⇒ infinity()` guard — the totality handling that is the
  consumer's, NOT this primitive's).
- **Inductive energy-participation ratio (witness 2):** `palace/models/postoperator.cpp:1148`
  (`vi.inductor_energy = 0.5 * std::abs(data.L) * std::real(I_mj * std::conj(I_mj))` — the
  `½L|I|²` self-energy numerator, the SAME shape as the resistor at `:1196-1197` with `L` for
  `R`), `:1215-1219` (`vi.inductive_energy_participation = std::copysign(vi.inductor_energy /
  energy_electric_all, I_mj.real())` — the SIGNED quotient `½L|I|²/E`, identical quotient shape
  to κ). The defining comment `:1209-1213` (`p_mj = ½L_j I_mj²/E_m`).
- **Surface-dielectric participation (witness 3):** `palace/models/postoperator.cpp:1346-1357`
  (the `MeasureInterfaceEFieldEnergy` body + the `1/Q_mj = p_mj tan(δ)_j`, `p_mj = ½t_j
  Re{∫_{Γ_j}(ε_jE_m)ᴴE_m dS}/(E_elec + E_cap)` formula comment), `:1364` (`auto energy =
  surf_post_op.GetInterfaceElectricFieldEnergy(idx, *E)` — the surface-integral numerator),
  `:1366` (`auto energy_participation_p = energy / energy_electric_all` — the UNSIGNED quotient
  `energy/E_total`), `:1367-1370` (the `Q = 1/(tanδ·p)` consumer with the `p==0 || tanδ==0 ⇒
  infinity()` guard). The numerator surface integral is `SurfacePostOperator::
  GetInterfaceElectricFieldEnergy` (`palace/models/surfacepostoperator.cpp:332-345`).
- **Total mode energy denominator (shared):** `palace/models/postoperator.cpp:1178-1179`
  (`auto energy_electric_all = measurement_cache.domain_E_field_energy_all +
  measurement_cache.lumped_port_capacitor_energy` — the `E_m = E_elec + E_cap` total, computed
  ONCE per mode), identical expression at `:1358-1359` for the surface-dielectric case. The
  numerator self-energies and the denominator are computed by separate energy reductions
  (`domain_E_field_energy_all` set `:1034`; `lumped_port_capacitor_energy` accumulated `:1158`).
- **L4 fold consumer (the gate this firms):** `book/src/L4/eigenfreq_qfactor_reduce.md:54-56`
  (the `κₘ = ½Rⱼ·|Iₘⱼ|²/Eₘ` per-mode loss rate the combinator folds), `:87-89` (the `kappa :
  Mode -> Scalar` closure parameter), `:186-198` (the rough-in §Status naming the absent
  κ-participation L1 entry as gate-a). This entry IS that κ-participation L1 home.
- **Sibling-primitive grounding:** `book/src/L1/reciprocal.md` (the bare-elementwise-arithmetic
  firm-on-positive-structure precedent for a non-reducing scalar primitive),
  `book/src/L1/nrm2.md` (the elementary `√·`-post-reduction analog), `book/src/L1/index.md:56`
  (the `reciprocal` firm-on-positive-structure no-dedicated-test precedent cited here).
- **No dedicated test** exercises the eigenmode participation postprocess (the
  `MeasureLumpedPortsEig` / `MeasureInterfaceEFieldEnergy` bodies are integration-level under the
  eigenmode `Solve(mesh)` driver; no `reference/palace/test/unit/` coverage) — non-gating for the
  syntactic-identity quotient laws (firm-on-positive-structure).
- **Provenance:** harvested cycle-077 D4 from the c075 D3 OQ
  `participation-ratio-l1-primitive-as-eigenfreq-qfactor-firming-route`; three witnesses
  established by this dispatch (resistive κ + inductive EPR + surface-dielectric p, all the
  `½X|I|²/E` / `energy/E_total` quotient shape). WARRANT verdict: genuine firm L1 entry (the
  shared participation-ratio quotient, the κ-participation building block of
  `eigenfreq_qfactor_reduce`, firming its gate-a).
```

This report does the authoring per the dispatch's harvester mandate (the pattern is clear enough
to author its firm L1 home this cycle).

### 2. L1 dep-map row insert (own row only; alpha-within-BLAS-1-&-elementwise grouping, between `nrm2` and `reciprocal`)

```edit:book/src/L1/index.md
| [`nrm2`](./nrm2.md) | `(x) → √⟨x,x⟩` | `dot` | `firm` |
| [`participation_ratio`](./participation_ratio.md) | `(energy: Scalar, e_total: Scalar) → Scalar` (i.e. `energy / e_total`; signed variant `copysign(energy/e_total, Re I)`) | (leaf; scalar-quotient post-reduction primitive; consumes already-reduced energies, NOT a reduction; sibling to `reciprocal`/`nrm2` as an elementary arithmetic atom) | `firm` (energy-participation-ratio quotient; the shared `½X|I|²/E` / `energy/E_total` shape of the eigenmode κ/EPR/surface-dielectric participations; **numerator-energy-source** + **signed-vs-unsigned** variant axes; L0: `palace/models/postoperator.cpp:1196-1199` resistive κ + `:1148,1217-1218` inductive EPR + `:1364-1366` surface-dielectric p, shared denom `:1178-1179`, numerator integral `palace/models/surfacepostoperator.cpp:332-345`; harvested cycle-077; firm-on-positive-structure, no-dedicated-test caveat non-gating per `reciprocal`/`eigsolve`-c022 precedent; numerator-energy computations + `Q=ω/κ` totality-guard consumer deliberately out of scope below/above the quotient; **firms `eigenfreq_qfactor_reduce` gate-a**, the L4 fold's κ-participation closure now has a firm L1 home; NO L2 entry by warrant — bare scalar quotient, an L2 mirror is the identity-in-named-terms smell) |
| [`reciprocal`](./reciprocal.md) | `(x: Tensor[N]) → Tensor[N]` (i.e. elementwise `1/x[i]`) | (leaf; elementwise BLAS-1-shape primitive; partial at `x[i] = 0`) | `firm` (elementwise multiplicative-inverse; L0: `palace/linalg/vector.cpp:248-261` complex + upstream MFEM real via `using Vector = mfem::Vector` alias `palace/linalg/vector.hpp:20`; harvested cycle-033; four consumer sites: `palace/linalg/jacobi.cpp:80`, `palace/linalg/chebyshev.cpp:178,241`, `palace/fem/bilinearform.cpp:278`; firm-on-positive-structure, no-dedicated-test caveat non-gating; partial at `x[i] = 0`) |
```

### 3. SUMMARY.md sub-chapter row insert (BLAS-1 & elementwise grouping; alpha between nrm2 and reciprocal)

```edit:book/src/SUMMARY.md
  - [nrm2](./L1/nrm2.md)
  - [participation_ratio](./L1/participation_ratio.md)
  - [reciprocal](./L1/reciprocal.md)
```

### 4. Vocabulary-cohort firm-count bump (NOTE for integrator)

The L1 index §"Vocabulary cohort" main-cohort firm count rises 27 → **28** (and the grand total
34 → **35**). The integrator-per-report SHOULD update the count prose in `book/src/L1/index.md:31`
(and the "27 main-cohort"/"34 firm grand total" references) when applying this row — flagged here
rather than edited inline because the count prose is dense and the integrator owns the
count-discipline reconciliation (read each linked chapter's `## Status`). The new firm member is
the energy-participation-ratio scalar-quotient primitive (a BLAS-1-&-elementwise-grouping member).

## Supporting evidence

- **Three witnesses (all self-verified on-disk via `palace-codemap` `read_range` this dispatch):**
  - `palace/models/postoperator.cpp:1171-1230` (the `MeasureLumpedPortsEig` body — resistive κ
    `:1196-1199`, inductive EPR `:1215-1219`, shared denom `:1178-1179`).
  - `palace/models/postoperator.cpp:1340-1373` (the `MeasureInterfaceEFieldEnergy` body —
    surface-dielectric p `:1364-1366`, denom `:1358-1359`).
  - `palace/models/postoperator.cpp:1148` (the inductor self-energy numerator).
  - `palace/models/surfacepostoperator.cpp:332-345` (the surface-integral numerator
    `GetInterfaceElectricFieldEnergy`).
- **L4 fold consumer (the gate firmed):** `book/src/L4/eigenfreq_qfactor_reduce.md:54-56,87-89`
  (the κ-participation closure the combinator folds), `:186-198` (the rough-in §Status naming the
  absent κ-participation L1 entry as gate-a — now firmed by this entry).
- **Firm-on-positive-structure precedent cited:** `book/src/L1/reciprocal.md`,
  `book/src/L1/index.md:56` (the bare-arithmetic no-dedicated-test precedent),
  `book/src/L1/index.md:167` (the `eigsolve` c022 test-coverage-bounded→firm re-eval precedent).
- **No dedicated test** exercises the eigenmode participation postprocess (integration-level under
  the eigenmode `Solve(mesh)` driver; no `reference/palace/test/unit/` coverage) — non-gating.

## Open questions / caveats

(Appended to `scaffolding/open-questions.md` this dispatch.)

- **`eigenfreq-qfactor-reduce-status-promotion-double-gated`** (NEW; coupled re-check NOTE): firming
  `participation_ratio` discharges **gate-a** of the L4 `eigenfreq_qfactor_reduce` rough-in (its
  κ-participation closure now has a firm L1 home). The combinator's promotion is double-gated (firm
  L1 home AND a dedicated eigenmode-postprocess reduction test OR a lowering-verifier law-confidence
  pass) and the eigenvalue-un-transform sibling primitive (`√μ`/`λ/i`, `eigensolver.cpp:430-439`)
  is a SECOND folded-primitive gate not addressed here. Re-anchoring `eigenfreq_qfactor_reduce` +
  the eigenfrequency-qfactor feature column is a coupled-column pass for a later cycle. *Trigger:* a
  reduction-verb-firming cycle re-checks the coupled column together with the eigenvalue-un-transform
  primitive firming (folds into the existing `gram-reduce-status-promotion-double-gated` standing
  gate family).
- **`eigenvalue-untransform-l1-primitive`** (NEW; the SECOND folded-primitive of
  `eigenfreq_qfactor_reduce`): the per-mode eigenvalue→ω un-transform `ω = √μ` (linear EVP) / `ω =
  λ/i` (quadratic EVP), `eigensolver.cpp:430-439`, is the other scalar map the L4 reduction folds.
  It has no firm L1 home. Lower fan-out than `participation_ratio` (a 2-branch problem-type-keyed
  scalar map, single pipeline) — named not dispatched. *Trigger:* the coupled
  `eigenfreq_qfactor_reduce` re-check, or an eigenmode-column firming pass.
- **Caveat — numerator-energy cohort not authored:** the `½X|I|²` self-energy + `½t·Re{∫(εE)ᴴE}`
  surface integral + `E_elec`/`E_cap` domain/cap energy reductions BELOW the quotient are a
  separate energy-reduction vocabulary (the eigenmode/energy-fields output-product column's
  energy-readout). Named in the L1 entry's §"Downward to L0", NOT authored — they are the existing
  plan CYCLE-076 #5 `energy-fields-output-product-column` item. Their absence does not gate
  `participation_ratio` (firm as the quotient, the way `reciprocal` is firm as the bare `1/x`).
- **OQ resolved:** `participation-ratio-l1-primitive-as-eigenfreq-qfactor-firming-route` (c075 D3) —
  RESOLVED by this dispatch (firm L1 home authored, gate-a discharged). Marked CLOSED in the OQ
  append.
