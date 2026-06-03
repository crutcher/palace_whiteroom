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
