---
agent: combinator-miner
invoked_at: 2026-06-06T232937Z
scope: L4 reduce-verb home — waveguide_mode_reduce (output-product column completion)
status: integrated
integrated_at: 2026-06-07T003000Z
integration_commit: f3d99801dec34c7af0714338ec1a38a04de603cb
integration_notes: "Applied clean as c118 D5 (batch-38 opener). New firm L4 verb waveguide_mode_reduce.md (Data-algebra firm 21→22) + waveguide-mode.{L4,L1} column rough-in→FIRM (own-composition rule; feature_root: seed KEPT). HARD GUARD honored: distinct sibling of eigenfreq_qfactor_reduce, non-unify guard closed-negative. cargo make book EXIT 0; rank_violations=0; promotion_frontier 8→6 (the 2 waveguide-mode nodes promoted). 0 gate hits."
---

# CYCLE: Combinator candidate — waveguide_mode_reduce

## Summary

The **boundary-mode driver's per-mode propagation-mode reduction** — the verb that turns the converged eigenpair family `eigsolve` returns on the 2D-submesh GEP into the user-facing **waveguide-mode table** `[{kn, n_eff, (Et, En, Bz)}]` — has no firm L4 home. It is the **propagation-mode member of the L4 output-product reduce-verb algebra**, the fourth sibling alongside `eigenfreq_qfactor_reduce` (per-mode `(f, Q)` scalar table), `sparameter_reduce` (driven port-projection matrix), and `domain_energy_reduce` (per-domain `(energy, p)` scalar table). It is genuine NEW spine vocabulary: a **per-mode `map` carrying mode FIELDS** (the transverse H(curl) `Et`, the longitudinal H1 `En`, the longitudinal magnetic `Bz`), which is exactly what distinguishes it from its scalar-only siblings and is the load-bearing reason it must NOT be force-unified with `eigenfreq_qfactor_reduce` (the guard-OQ; see §Over-unification guard). I propose `waveguide_mode_reduce` as a firm **L4 reduce verb**, author its chapter, alpha-insert its `L4/index.md` dep-map row + `SUMMARY.md` entry, and bundle the coupled `waveguide-mode.{L4,L1}` column promotion `rough-in → firm` (the `sparameter_reduce`/`sparameters` c083 precedent — the verb's firming IS the column's own-reduce-verb promotion gate).

## Pattern instances

The output-product reduce-verb family — a parametric **constructed-reduction family** unified by a shared "reduce a solved family to its physical output product" contract, with `waveguide_mode_reduce` the missing propagation-mode member:

- Instance 1 (sibling, firm): `book/src/L4/eigenfreq_qfactor_reduce.md:17-43` — eigenmode per-mode `(f, Q)` scalar-table reduction over the `eigsolve` eigenpair family. **Same `eigsolve` solve-corner**, scalar-only result.
- Instance 2 (sibling, firm): `book/src/L4/sparameter_reduce.md:14-46` — driven per-port port-projection reduction to the scattering matrix over the `frequency_sweep` family. The column-promotion precedent (c083: verb firm ⇒ column off `seed`/`rough-in`).
- Instance 3 (sibling, firm): `book/src/L4/domain_energy_reduce.md` (per `book/src/L4/index.md:111`) — field-energy per-domain `(energy, p)` scalar-table reduction.
- Instance 4 (THIS candidate, currently unhomed): the boundary-mode propagation-mode reduction. L0: `palace/drivers/boundarymodesolver.cpp:272-340` (the two readout loops: the `kn`/`n_eff` print loop `:272-278`, the field-readout loop `:292-335`). Flagged 5× as rough-in with no L4 home: `book/src/feature/waveguide-mode.L4.md:36,49,83` + `:59` (the signature) and `book/src/feature/waveguide-mode.L1.md:47,76`, OQ `waveguide-mode-reduce-needs-l4-verb-home`.

The cohort is represented **4× at the feature/sibling surface but the propagation-mode member is unified 0× as a firm verb** — the family-detection trigger (N× represented, 0× the missing member homed).

## Proposed combinator

- **Slug**: `waveguide_mode_reduce`
- **Layer**: **L4** (with rationale below).
- **Class**: data-algebra reduce verb — the **propagation-mode member of the L4 output-product reduce-verb algebra** (a constructed-reduction family; reduce a solved eigenpair family to the physical output product). NOT a fold over a combining-step with an identity (no concatenation-homomorphism producing a single accumulator) — it is a per-mode `map`-then-collect, exactly the shape of its three firm siblings.

- **Signature sketch** (per `waveguide-mode.L4.md:59`; named-shape-groups notation per the semantic surface §1.2.1, `book/src/semantics/index.md`):

```text
waveguide_mode_reduce :: EigResult -> Scalar -> WaveguideModeTable
-- EigResult: the converged eigenpair family from eigsolve (2D-submesh ND⊕H1 GEP)
-- Scalar:    the operating angular frequency ω (the n_eff = kn/ω divisor + the Bz 1/ω scale)
-- per converged mode i:
--   kn_i   : Complex                          -- propagation constant (eigenvalue shift-invert un-transform)
--   n_eff_i: Complex                          -- = kn_i / ω
--   Et_i   : Tensor[N_nd,  complex]           -- transverse H(curl) mode field (flat ND dof-vector)
--   En_i   : Tensor[N_h1,  complex]           -- longitudinal H1 mode field   (flat H1 dof-vector)
--   Bz_i   : Maybe (Tensor[N_curl, complex])  -- longitudinal B (propagating modes only)
```

  Per-mode body (read off `boundarymodesolver.cpp:292-335`, all anchors self-verified on-disk this dispatch via codemap `read_range`):
  1. **eigenvalue un-transform → `kn`** — `eig.GetPropagationConstant(i)` (`boundarymodesolver.cpp:299`; print at `:275`);
  2. **`n_eff = kn / ω`** — `kn.real()/omega`, `kn.imag()/omega` (`boundarymodesolver.cpp:276`);
  3. **VD back-transform → `(Et, En)`** — `mode_op.ApplyVDBackTransform(e0, kn, et, en)` (`boundarymodesolver.cpp:300`), over the loaded eigenvector `eig.GetEigenvector(i, e0)` (`:297`);
  4. **power-normalize to `|P| = 1`** — `P = mode_op.ComputePoyntingPower(omega, kn, et, en)` (`:304`); `e0 *= 1/√|P|` when `|P| > 0` (`:305-308`);
  5. **conditional `Bz = curl(Et)/(iω)`** for propagating modes (`ModeEigenSolver::IsPropagating(kn)`, `:316`) — `bz.Real() = curl_eti; bz.Real() *= 1/ω; bz.Imag() = curl_etr; bz.Imag() *= -1/ω` (`:325-332`), the discrete curl interpolator `mode_op.GetCurlSpace().GetDiscreteInterpolator(...)` `:319-323`.

- **Algebraic intuition**
  - **Map-independence / concatenation-homomorphism** (the defining family law, shared with all three siblings): `waveguide_mode_reduce (a ++ b) ω = waveguide_mode_reduce a ω ++ waveguide_mode_reduce b ω` — each row depends only on its own `(λᵢ, xᵢ)`; the readout loop carries no inter-mode accumulator (`boundarymodesolver.cpp:292` for-loop, no carry). Embarrassingly parallel over modes.
  - **ω rides as a fixed scalar parameter** (not a per-mode datum) — the `n_eff` divisor + the `Bz` `1/ω` scale; factored out exactly as `sparameter_reduce` factors the swept-ω axis out (`sparameter_reduce.md:235-239` per-ω-axis caveat). The reduction is at a single ω.
  - **Totality of the normalization guard**: `|P| = 0 ⇒ no rescale` (the `if (std::abs(P_initial) > 0.0)` branch, `:305`) — a total edge case in the field map, not an error arm (the `κ=0 ⇒ Q=∞` analog from `eigenfreq_qfactor_reduce.md:141`).
  - **Conditional `Bz`** is a per-mode `Maybe` keyed on `IsPropagating(kn)` (`|Im kn| < 0.1|Re kn| ∧ |Re kn| > 0`, `modeeigensolver.cpp:516-519`) — a pure per-mode branch, not a cross-mode combine.

- **Variant axes**
  - **propagating vs evanescent mode** (the load-bearing axis): selects the `Bz` `Just`/`Nothing` arm (`IsPropagating(kn)`); absorbed into the per-mode `Maybe` branch.
  - **element-type** (complex — pinned; waveguide modes are intrinsically complex, `kn`/`n_eff`/`(Et,En,Bz)` all complex).
  - (NOT a variant: the ND/H1/curl field spaces are the fixed VD-back-transform output structure, not a selectable axis.)

- **Over-unification guard (HARD — the guard-OQ, explicitly honored)**
  `waveguide_mode_reduce` shares the **`eigsolve` solve-corner** with `eigenfreq_qfactor_reduce` (both reduce a converged eigenpair family the eigensolver returns). My combinator-miner instinct to unify them is **overridden here, and correctly so**: they are **distinct reduce verbs** and stay sibling members of the algebra, NOT one verb. WHY they stay distinct:
  - **Result kind differs (the load-bearing distinction).** `eigenfreq_qfactor_reduce` is a **scalar-only** per-mode table `[(f, Q)]` (`eigenfreq_qfactor_reduce.md:73` — `[(Scalar, Scalar)]`); `waveguide_mode_reduce` carries **mode FIELDS** `(Et, En, Bz)` — genuine flat rank-1 dof-vectors on the 2D-submesh ND/H1/curl spaces (`waveguide-mode.L4.md:63-65`). A field-carrying reduce is a different fold from a scalar-only reduce — the same same-shape-different-fold / `dot`-vs-`linear_combination` over-unification guard the siblings already enforce (`sparameter_reduce.md:43`, `concepts/black-box-vs-accelerated-kernels.md` §2).
  - **Different driver corner.** `eigenfreq_qfactor_reduce` reduces the **3D-domain eigenmode** driver's family; `waveguide_mode_reduce` reduces the **2D-submesh boundary-mode** driver's family (`CreateFromBoundary` 3D→2D projection) — the same driver-distinction boundary-mode carries against eigenmode (`waveguide-mode.L4.md:74`).
  - **Body differs.** `waveguide_mode_reduce`'s body is the VD back-transform + Poynting power-normalization + conditional curl `Bz` formation — none of which appears in the eigenfrequency/Q scalar map; `eigenfreq_qfactor_reduce`'s κ-participation Q-ratio does not appear here.

  Conclusion: same solve-corner, **different result kind + different body + different driver** ⇒ author as its OWN verb, cross-linked as a reduce-verb-algebra sibling (the c074-D6-closed-negative discipline the other siblings already applied). Recorded under OQ `waveguide-mode-reduce-vs-eigenfreq-qfactor-reduce-non-unify-closed-negative` below.

- **Layer placement rationale (L4, not adjacent)**
  - **L4, not L1**: the verb is the **structural per-mode map made a combinator** — the L4 form the outward backend consumes; the L1 chapter (`waveguide-mode.L1.md`) already carries the *unfolded* per-mode list comprehension. This is the exact L1-unfolded / L4-combinator split the three firm siblings instantiate (`eigenfreq_qfactor_reduce.md:60-65`). It rises to L4 as a feature-surface verb the backend wants (`concepts/black-box-vs-accelerated-kernels.md` §"The combinators rise regardless").
  - **L4, not a feature column**: the `waveguide-mode.{L4,L1}` columns are composition-ROOTS that *compose* this verb (`waveguide_mode = waveguide_mode_reduce (ω) ∘ boundary_mode_eigenpairs`, `waveguide-mode.L4.md:76`); the verb is their OWN reduce constituent and needs its own data-algebra home so the column promotes off `rough-in` (OWN-COMPOSITION rule).
  - **No L4>L3 theme**: like all three siblings, it lowers by **identity-in-form on the body** to the per-mode field/scalar maps it folds — a plain per-mode `map`, no intervening L3/L2 reshape. The in-line-marker route (`eigenfreq_qfactor_reduce.md:171-176`, `sparameter_reduce.md:222-233`), NOT a dedicated theme file.

## Proposed changes

This dispatch creates the L4 verb chapter directly in the proposed-changes channel (this is a harvester-shaped formalization of a flagged-and-scoped rough-in, dispatched to combinator-miner per the cycle-118 D5 plan; the chapter, the dep-map row, the SUMMARY entry, and the coupled column flip are bundled). The integrator applies all blocks.

### (1) Create the L4 verb chapter

```edit:book/src/L4/waveguide_mode_reduce.md
---
layer: L4
operator: waveguide_mode_reduce
firmness: firm
edges:
  rank: firm
  depends-on:
    - target: L4/eigsolve
      kind: composes               # consumes the converged eigenpair family eigsolve returns
    - target: palace/drivers/boundarymodesolver.cpp:272-340
      kind: cites-evidence
  reference:
    - L4/eigenfreq_qfactor_reduce   # sibling reduce verb (same eigsolve corner; scalar-only — the non-unify guard)
    - L4/sparameter_reduce          # sibling reduce-to-matrix verb
    - L4/domain_energy_reduce        # sibling reduce-to-scalar-table verb
    - feature/waveguide-mode.L4      # the composition root that composes this verb
variant_axes:
  - mode-propagation (propagating | evanescent — THE load-bearing axis; selects the Bz Just/Nothing arm via IsPropagating(kn); absorbed into the per-mode Maybe branch)
  - element-type (complex — pinned; waveguide modes intrinsically complex: kn/n_eff/(Et,En,Bz) all complex)
---

# waveguide_mode_reduce

The L4 **boundary-mode per-mode propagation-mode reduction combinator**: reduce the
converged eigenpair family `EigResult` the boundary-mode eigensolver returns (on the
2D-submesh `ND ⊕ H1` GEP) into the **waveguide-mode table**
`[{kn, n_eff, (Et, En, Bz)}]`, where each row un-transforms the eigenvalue to the
**propagation constant `kn`**, divides to the **effective index `n_eff = kn/ω`**,
VD-back-transforms the eigenvector to the **physical mode fields `(Et, En)`**,
power-normalizes the mode to `|P| = 1`, and (for propagating modes only) forms the
**longitudinal magnetic field `Bz = curl(Et)/(iω)`**. It is the **boundary-mode
output-product reduction** — the verb that turns the raw eigenpairs the boundary-mode
solver returns into the waveguide-mode table the user ran the solver to compute.

`waveguide_mode_reduce` is a **pure value-producing reduction** (no `Solve` monad, no
carry, no convergence predicate — the per-mode readout map is explicitly NOT a
solve-iteration, the [`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md):29-30
sibling pattern) — the **propagation-mode member** of the L4 output-product reduce-verb
algebra, the sibling of the scalar-only [`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md)
(per-mode `(f, Q)`), the reduce-to-matrix [`sparameter_reduce`](./sparameter_reduce.md)
(driven scattering matrix), and the per-domain [`domain_energy_reduce`](./domain_energy_reduce.md)
(`(energy, p)`). It rises to L4 as a **feature-surface verb the backend wants**
([`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md)
§"The combinators rise regardless"; directive-1: L4 is the outward backend-lowering
target) — the output-product half of the waveguide-mode composition root
([`waveguide-mode.L4`](../feature/waveguide-mode.L4.md)) reaches the L4 surface through it.

It is **genuine NEW spine vocabulary, NOT an `eigenfreq_qfactor_reduce` specialization**
(the over-unification guard — see §Algebraic laws / "do not hold"). The two reductions
share the [`eigsolve`](./eigsolve.md) solve-corner (both reduce a converged eigenpair
family), but they carry **different result kinds**: `eigenfreq_qfactor_reduce` is a
**scalar-only** per-mode table `[(f, Q)]`, while `waveguide_mode_reduce` carries mode
**FIELDS** `(Et, En, Bz)` — flat rank-1 dof-vectors on the 2D-submesh ND/H1/curl spaces.
Same solve-corner, different fold (field-carrying vs scalar-only), different driver
(2D-submesh boundary-mode vs 3D-domain eigenmode) — exactly the
same-operand-shape-different-fold over-unification guard
([`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md) §2).
It is the boundary-mode output-product column's OWN reduction verb.

## Context

L4 is **vocabulary** (`L4/index.md:7-13`). `waveguide_mode_reduce` names the per-mode
propagation-mode reduction the boundary-mode driver runs on its converged eigenpair set.
It consumes the eigenpair family the opaque [`eigsolve`](./eigsolve.md) cap returns on the
2D-submesh GEP (the boundary-mode composition root's solve-stage output,
[`waveguide-mode.L4.md`](../feature/waveguide-mode.L4.md):32-35), and maps each converged
mode to its waveguide-mode row:

- the **propagation constant `kn`** — the shift-invert un-transform of the eigenvalue
  (`eig.GetPropagationConstant(i)` exposes it un-transformed);
- the **effective index `n_eff = kn / ω`**;
- the **mode fields `(Et, En)`** — the VD back-transform of the eigenvector, then
  power-normalized so the Poynting power `|P| = 1`;
- the **longitudinal magnetic field `Bz = curl(Et)/(iω)`** for propagating modes only
  (`IsPropagating(kn)`).

The combinator is defined **in L4 vocabulary** (high→low discipline): its semantics,
signature, and laws are stated in terms of the eigenpair family it consumes and the
per-mode field/scalar maps it folds — NOT in terms of the L0 C++ readout loop. It is a
methodology-level combinator distilled from the boundary-mode driver's two readout loops
(the `kn`/`n_eff` print loop + the field-readout + `Bz`-formation loop); Palace's C++
writes the explicit per-mode loop, not the L4 reduction form.

## Signature

    -- the boundary-mode per-mode propagation-mode reduction over the converged eigenpair set:
    waveguide_mode_reduce :: EigResult            -- the converged eigenpair family (2D-submesh ND⊕H1 GEP)
                          -> Scalar               -- the operating angular frequency ω
                          -> WaveguideModeTable   -- per mode: {kn, n_eff, (Et, En, Bz)}
    waveguide_mode_reduce res w =
      [ let kn       = propagation_constant (res.eigenvalues ! i)   -- eigenvalue shift-invert un-transform
            n_eff    = kn / w                                       -- effective index
            (et, en) = vd_back_transform (res.eigenvectors ! i) kn  -- VD back-transform → physical (Et, En)
            (et', en') = power_normalize (et, en) w kn              -- normalize so |P| = 1 (Poynting power)
            bz       = if is_propagating kn                         -- conditional longitudinal B
                         then Just (curl et' / (1i * w))
                         else Nothing
        in  { kn, n_eff, et = et', en = en', bz }
      | i <- [0 .. res.converged - 1] ]                            -- map over converged modes (no inter-mode state)

Shape contract (using the named-shape-groups notation governed by the semantic surface
[`semantics`](../semantics/index.md) §1.2.1):

- `res : EigResult` — the converged eigenpair family ([`eigsolve`](./eigsolve.md)'s output
  on the 2D-submesh GEP; each `(λᵢ, xᵢ)`). Read-only. The `WaveguideModeTable` record is
  defined in its current in-chapter home
  ([`waveguide-mode.L4`](../feature/waveguide-mode.L4.md), §Inputs/outputs).
- `w : Scalar` — the operating angular frequency `ω`; read-only. Rides as a fixed scalar
  parameter (the `n_eff` divisor + the `Bz` `1/ω` scale), NOT a per-mode datum — the
  per-ω-axis-factored-out convention the SIBLING
  [`sparameter_reduce`](./sparameter_reduce.md) applies (`:235-239`).
- result `WaveguideModeTable` — the per-mode table, one row per converged mode, each
  `{kn, n_eff, (Et, En, Bz)}`. The mode fields `Et`/`En`/`Bz` are **genuine flat rank-1
  dof-vectors** on the 2D-submesh ND/H1/curl spaces — `Tensor[N_nd]` / `Tensor[N_h1]` /
  `Tensor[N_curl]` (complex), which is correct per the semantic surface §1.2.1 (NOT a
  named shape group); `kn`/`n_eff` are complex scalars; `Bz` is `Maybe` (propagating
  modes only).

The shape contract makes structural what is conventional in the C++ readout loops:

1. **Each table row is independent (the map is a list homomorphism over modes).** No state
   threads between modes; the reduction collects (`boundarymodesolver.cpp:292` readout
   loop carries no inter-mode accumulator).
2. **ω is a fixed parameter, not a per-mode input** — the reduction is at a single ω; the
   `n_eff` divide and the `Bz` `1/ω` scale apply the same ω to every row.

## Semantics

`waveguide_mode_reduce res ω` maps each converged eigenpair to its waveguide-mode row:
un-transform the eigenvalue to the propagation constant `kn`, divide to `n_eff = kn/ω`,
VD-back-transform the eigenvector to the physical fields `(Et, En)`, power-normalize so the
Poynting power `|P| = 1`, and (for propagating modes) form `Bz = curl(Et)/(iω)`. It is a
`map`-then-collect with no `Solve` effect — a pure function
`(EigResult, Scalar) -> WaveguideModeTable`.

The combinator's structural payoff: the boundary-mode driver's per-mode readout —
scattered across the `kn`/`n_eff` print loop (`boundarymodesolver.cpp:272-278`) and the
field-readout + `Bz`-formation loop (`:292-335`) — is ONE reduction over the eigenpair
family. The propagation scalars (`kn`, `n_eff`) and the mode fields (`Et`, `En`, `Bz`) are
the projections of each mode; unlike its scalar-only siblings, this reduction's rows carry
**field** payloads, which is its defining structural fact.

This is the **field-carrying** member of the output-product reduce-verb algebra: where
[`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md) and
[`domain_energy_reduce`](./domain_energy_reduce.md) produce scalar-only tables and
[`sparameter_reduce`](./sparameter_reduce.md) / [`gram_reduce`](./gram_reduce.md) produce
`Matrix[p,p]`, `waveguide_mode_reduce` produces a per-mode table whose rows mix complex
scalars (`kn`, `n_eff`) with rank-1 dof-vector fields (`Et`, `En`, `Bz`). The field
payload is the wrong shape for any scalar-table or matrix subsume — the load-bearing
non-unify (see §Algebraic laws / "do not hold").

## Algebraic laws

Every law is a **syntactic identity on the per-mode map structure**, read off the two
positive readout loops.

1. **Map-independence / concatenation-homomorphism** (the defining fold law).
   `waveguide_mode_reduce (a ++ b) ω = waveguide_mode_reduce a ω ++ waveguide_mode_reduce
   b ω` — each row depends only on its own mode's `(λᵢ, xᵢ)` and the fixed ω; no inter-mode
   state. Embarrassingly parallel over modes (the `eigenfreq_qfactor_reduce` /
   `domain_energy_reduce` grid-map homomorphism; `boundarymodesolver.cpp:292` carries no
   accumulator).
2. **Un-transform + effective-index purity.** `kn = propagation_constant λ` and
   `n_eff = kn/ω` are pure per-mode/scalar maps — the shift-invert un-transform exposed by
   `GetPropagationConstant` then a scalar divide by the fixed ω. No cross-mode combine.
3. **Power-normalization totality.** `|P| = 0 ⇒ no rescale` (the `if (|P| > 0)` branch,
   `boundarymodesolver.cpp:305`) — a total edge case in the field map, NOT an error arm
   (the `eigenfreq_qfactor_reduce` `κ=0 ⇒ Q=∞` lossless-totality analog, `:141`). When
   `|P| > 0` the mode field is scaled by `1/√|P|` so the normalized mode has `|P| = 1`.
4. **Conditional `Bz` (the per-mode `Maybe`).** `Bz = Just (curl(Et)/(iω))` iff
   `is_propagating kn` (`|Im kn| < 0.1|Re kn| ∧ |Re kn| > 0`,
   `modeeigensolver.cpp:516-519`), else `Nothing`. A pure per-mode branch keyed on `kn`,
   not a cross-mode combine. The `curl(Et)/(iω)` formation is
   `Bz.Real = curl(Et).Imag / ω`, `Bz.Imag = -curl(Et).Real / ω` (the `1/(iω)` complex
   division written out, `:325-332`).

Laws that explicitly **do not** hold:

- **No cross-mode combine.** The reduction does not sum/reduce across modes — it is a
  per-mode map producing one table row each. (Contrast `inner_product`, which DOES reduce
  across the length axis.)
- **NOT an `eigenfreq_qfactor_reduce` specialization (the over-unification guard).** The
  two share the [`eigsolve`](./eigsolve.md) solve-corner (both reduce a converged
  eigenpair family) and the per-mode-map shape, but the **result kind differs**:
  `eigenfreq_qfactor_reduce` produces a **scalar-only** `[(f, Q)]` table
  ([`eigenfreq_qfactor_reduce.md`](./eigenfreq_qfactor_reduce.md):73), while this verb
  produces rows carrying mode **FIELDS** `(Et, En, Bz)`. A field-carrying reduce is a
  DIFFERENT fold from a scalar-only reduce — same solve-corner, different fold (the
  `dot`-vs-`linear_combination` / `sparameter_reduce`-vs-`gram_reduce`
  same-shape-different-fold guard, `sparameter_reduce.md:43`,
  `concepts/black-box-vs-accelerated-kernels.md` §2). The bodies differ too (VD
  back-transform + Poynting normalization + curl `Bz` here; κ-participation Q-ratio there),
  and the drivers differ (2D-submesh boundary-mode vs 3D-domain eigenmode). Author as its
  OWN verb; do NOT subsume. (OQ
  `waveguide-mode-reduce-vs-eigenfreq-qfactor-reduce-non-unify-closed-negative`.)
- **Not a reduce-to-matrix.** No `Matrix[p,p]`, no symmetric mirror, no port grid — the
  contrast with [`sparameter_reduce`](./sparameter_reduce.md) / [`gram_reduce`](./gram_reduce.md).

## Dependencies

- [`eigsolve`](./eigsolve.md) (firm) — the opaque eigen-solve cap producing the converged
  eigenpair family this reduction maps over (the boundary-mode composition root's
  solve-stage output, [`waveguide-mode.L4`](../feature/waveguide-mode.L4.md):32-35).

Sibling data-algebra reduction combinators (the L4 output-product reduce-verb algebra):

- [`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md) (reduce-to-scalar-table,
  same `eigsolve` corner) — the scalar-only per-mode `(f, Q)` sibling; the load-bearing
  non-unify (field-carrying vs scalar-only; different driver corner).
- [`sparameter_reduce`](./sparameter_reduce.md) (reduce-to-matrix) — the driven
  port-projection sibling.
- [`domain_energy_reduce`](./domain_energy_reduce.md) (reduce-to-scalar-table) — the
  per-domain `(energy, p)` sibling.
- [`gram_reduce`](./gram_reduce.md) (reduce-to-matrix) — the bilinear symmetric-Gram
  sibling.

The per-mode field maps this folds — the VD back-transform `(Et, En)`, the Poynting
power-normalization, and the discrete-curl `Bz` formation — bottom out in
`ModeOperator` / `ModeEigenSolver` boundary-mode model methods at L0
(`mode_op.ApplyVDBackTransform` / `ComputePoyntingPower` / `GetDiscreteInterpolator`);
their dedicated L1 homes are deferred (OQ
`waveguide-mode-reduce-field-map-l1-homes`).

## Lowers to

`waveguide_mode_reduce` lowers by **identity-in-form on the body** to the per-mode
field/scalar maps it folds (the eigenvalue un-transform, the `n_eff` divide, the VD
back-transform, the Poynting power-normalization, and the conditional curl `Bz`). The
reduction is a plain per-mode `map` — there is no intervening L3/L2 absorption that
reshapes the map. No dedicated L4>L3 theme file — the in-line-marker route (the
[`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md):171-176 /
[`sparameter_reduce`](./sparameter_reduce.md):222-233 pattern); the substantive downward
content (the C++ two readout loops, the VD back-transform, the Poynting normalization, the
discrete-curl `Bz` formation) lives in the boundary-mode driver / model L0
(`boundarymodesolver.cpp:272-340`) and the boundary-mode model methods. This entry records
the rotation direction in-line per high→low discipline; it does not author a theme.

**ω axis caveat.** The operating frequency ω is factored OUT as a fixed scalar parameter:
the reduction applies one ω to every row (matching the single-frequency boundary-mode
solve), the `n_eff` divide and the `Bz` `1/ω` scale apply that same ω — the clean
separation the SIBLING [`sparameter_reduce`](./sparameter_reduce.md):235-239 applies for
its swept-ω axis (here ω is a single value, not a sweep).

## Status

`firm`. **Reasoning (firm-on-positive-structure / syntactic-identity escape):** the
combinator's **structure** is read directly off the two positive readout loops — the
`kn`/`n_eff` print loop (`boundarymodesolver.cpp:272-278`) and the field-readout +
`Bz`-formation loop (`:292-335`) — and **every** law (§Algebraic laws) is a **syntactic
identity** on the per-mode map: law 1 (concatenation-homomorphism) is a read-off of the
inter-mode-stateless readout loop (`:292`, no accumulator); law 2 (un-transform +
effective-index purity) is the literal `GetPropagationConstant(i)` (`:299`) + the scalar
`kn/ω` divide (`:276`); law 3 (power-normalization totality) is read literally off the
`if (std::abs(P_initial) > 0.0) { e0 *= 1/√|P| }` branch (`:305-308`); law 4 (conditional
`Bz`) is read off the `IsPropagating(kn)` branch (`:316`) + the `1/(iω)` curl formation
(`:325-332`) + the `IsPropagating` predicate body (`modeeigensolver.cpp:516-519`). The
per-mode **assembly** is the structural collect of these maps over the eigenpair family;
it carries **no axiom requiring an unverified mathematical property** — the VD
back-transform and the Poynting power are opaque boundary-mode model methods whose OUTPUTS
the reduction collects verbatim (the `eigsolve`-opaque-leaf / `sparameter_reduce`
cached-projection-crossing parallel: an evaluation-strategy detail the reduction abstracts
over, not an algebraic axiom). This is the same escape that landed the SIBLINGS
[`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md) (c082),
[`sparameter_reduce`](./sparameter_reduce.md) (c083), and
[`domain_energy_reduce`](./domain_energy_reduce.md) (c091) firm; the contrast is the c080/c091
[`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) audit, which RULED OUT the escape
because its norm-axiom laws are theorems conditional on an inner-product structure the L0
source only numerically asserts — **no such theorem-needing-proof exists in this verb's
per-mode map**.

**No dedicated assembly test.** The boundary-mode readout loops are integration-level under
the boundary-mode `Solve(mesh)` driver, not unit-tested under
`reference/palace/test/unit/` (the boundary-mode driver has no positive assembly test, the
same disposition as the `eigenfreq_qfactor_reduce` / `sparameter_reduce` readouts). Under
the firm-on-positive-structure escape the missing test is redundant: every per-mode map law
is a syntactic identity over the positive source + opaque model-method outputs, carrying no
residual untested semantic claim. The escape discharges the assembly-test gate (the SAME
route as the c082/c083/c091 sibling promotions).

**Scope: single-pipeline (boundary-mode) BY DESIGN.** This is the boundary-mode driver's
OWN output-product reduction; it is not a cross-pipeline shared verb (the other output
products: eigenmode `(f,Q)` via `eigenfreq_qfactor_reduce`, driven S-parameters via
`sparameter_reduce`, electrostatic/magnetostatic capacitance/inductance via `gram_reduce`,
field-energy per-domain via `domain_energy_reduce`). The propagating-vs-evanescent split is
a **variant axis** (the `Bz` `Just`/`Nothing` arm), NOT a 2nd pipeline. The
over-unification guard vs `eigenfreq_qfactor_reduce` (same `eigsolve` corner) is
CLOSED-NEGATIVE — author as its own verb (field-carrying ≠ scalar-only).

verified_against:

```yaml
verified_against:
  - citation: palace/drivers/boundarymodesolver.cpp:272-340
    verdict: supports
    audited_at: 2026-06-06T232937Z
    note: the two per-mode readout loops re-verified on-disk via codemap read_range. kn/n_eff print loop :272-278 (GetPropagationConstant :275, kn.real()/omega :276); field-readout loop :292-335 — eigenvector load eig.GetEigenvector(i, e0) :297, kn :299, VD back-transform ApplyVDBackTransform(e0, kn, et, en) :300, Poynting power ComputePoyntingPower :304, normalize e0 *= 1/sqrt(|P|) under if(|P|>0) :305-308, IsPropagating(kn) branch :316, discrete curl interpolator :319-323, Bz = curl(Et)/(iw) formation bz.Real()=curl_eti; bz.Real()*=1/omega; bz.Imag()=curl_etr; bz.Imag()*=-1/omega :325-332. Function returns :339-340. Every law is a syntactic read-off of this positive source.
  - citation: palace/models/modeeigensolver.cpp:516-519
    verdict: supports
    audited_at: 2026-06-06T232937Z
    note: ModeEigenSolver::IsPropagating(kn) body re-verified on-disk — return |kn.imag()| < 0.1*|kn.real()| && |kn.real()| > 0.0. The per-mode Maybe predicate (law 4); a pure per-mode branch on kn, not a cross-mode combine.
  - citation: book/src/L4/eigenfreq_qfactor_reduce.md:73
    verdict: supports
    audited_at: 2026-06-06T232937Z
    note: sibling result type [(Scalar, Scalar)] (scalar-only) — the load-bearing non-unify contrast; this verb carries mode FIELDS (Et,En,Bz). Same eigsolve corner, different result kind/fold (the over-unification guard, closed-negative).
  - citation: book/src/feature/waveguide-mode.L4.md:59
    verdict: supports
    audited_at: 2026-06-06T232937Z
    note: 'the signature waveguide_mode_reduce :: EigResult -> Scalar -> WaveguideModeTable + the rough-in verb gate (:83) + the per-mode body enumeration (:43-49); the WaveguideModeTable record''s current in-chapter home (§Inputs/outputs).'
```

## Evidence

All L0 citations self-verified on-disk this dispatch via the codemap
(`mcp__palace-codemap__read_range` + `search_text` line pinpoints against
`reference/palace/`).

- **The two per-mode readout loops (positive witness — the reduction itself):**
  `palace/drivers/boundarymodesolver.cpp:272-278` (the `kn`/`n_eff` print loop:
  `GetPropagationConstant(i)` `:275`, `kn.real()/omega` `:276`),
  `:292-335` (the field-readout + `Bz`-formation loop:
  `eig.GetEigenvector(i, e0)` `:297`, `kn` `:299`,
  `mode_op.ApplyVDBackTransform(e0, kn, et, en)` `:300`,
  `mode_op.ComputePoyntingPower(omega, kn, et, en)` `:304`,
  `e0 *= 1/√|P|` under `if (|P| > 0)` `:305-308`,
  `ModeEigenSolver::IsPropagating(kn)` branch `:316`,
  discrete-curl interpolator `:319-323`,
  `Bz = curl(Et)/(iω)` formation `:325-332`), return `:339-340`.
- **The `IsPropagating` predicate body (law 4):**
  `palace/models/modeeigensolver.cpp:516-519`.
- **Feature-chapter forward-mine flags (the §reduction stage that flagged the mine):**
  `book/src/feature/waveguide-mode.L4.md:36,49,59,83` (the signature + the rough-in verb
  gate + the constituent down-link table row), `book/src/feature/waveguide-mode.L1.md:47,76`.
- **Sibling-combinator grounding:** `book/src/L4/eigenfreq_qfactor_reduce.md`
  (the scalar-only same-`eigsolve`-corner sibling + the non-unify contrast),
  `book/src/L4/sparameter_reduce.md` (the reduce-to-matrix sibling + the per-ω-axis-factored
  convention + the column-promotion precedent),
  `book/src/L4/domain_energy_reduce.md` (the per-domain scalar-table sibling),
  `book/src/L4/gram_reduce.md` (the bilinear symmetric-Gram sibling),
  `book/src/concepts/black-box-vs-accelerated-kernels.md` §"The combinators rise
  regardless" (the L4-feature-surface-verb warrant) + §2 (the same-shape-different-fold
  over-unification guard), `book/src/L4/eigsolve.md` (the opaque eigen-solve cap producing
  the family this reduces).
- **No dedicated test** exercises the boundary-mode propagation-mode reduction (the readout
  loops are integration-level under the boundary-mode `Solve(mesh)` driver, not unit-tested
  under `reference/palace/test/unit/`) — redundant under the firm-on-positive-structure
  escape.
- **Provenance:** cycle-118 D5 (batch-38, output-product column completion) — formalizes
  the rough-in verb flagged 5× in the `waveguide-mode.{L4,L1}` feature columns
  (OQ `waveguide-mode-reduce-needs-l4-verb-home`). WARRANT verdict: genuine L4 entry (the
  boundary-mode output-product reduction verb; the field-carrying propagation-mode member of
  the L4 output-product reduce-verb algebra, a navigable L4 home — NOT a stranded mine, NOT
  an `eigenfreq_qfactor_reduce` specialization, over-unification-guard closed-negative).
```

### (2) Add the `L4/index.md` dep-map row (alpha-insert after `sparameter_reduce`, line 120 — `w` > `s`, end of the data-algebra group)

```edit:book/src/L4/index.md
| [`waveguide_mode_reduce`](./waveguide_mode_reduce.md) | `waveguide_mode_reduce :: EigResult -> Scalar -> WaveguideModeTable`; per converged mode `{kn, n_eff = kn/ω, (Et, En, Bz)}` where `kn` is the eigenvalue shift-invert un-transform, `(Et, En)` the VD-back-transform of the eigenvector power-normalized to `|P|=1`, and `Bz = curl(Et)/(iω)` for propagating modes only (`Maybe`). The boundary-mode **per-mode propagation-mode reduction combinator** — the **field-carrying** member of the L4 output-product reduce-verb algebra (sibling of the scalar-only [`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md), the reduce-to-matrix [`sparameter_reduce`](./sparameter_reduce.md), the per-domain [`domain_energy_reduce`](./domain_energy_reduce.md)). Per-mode `map` carrying mode FIELDS (Et/En/Bz flat rank-1 dof-vectors on the 2D-submesh ND/H1/curl spaces), NOT a scalar-only table — the load-bearing distinction from `eigenfreq_qfactor_reduce` (same `eigsolve` corner, DIFFERENT fold + driver; over-unification guard closed-negative). Pure value-producing reduction — no `Solve` monad / carry / predicate. | Consumes: the converged eigenpair family from [`eigsolve`](./eigsolve.md) (the boundary-mode composition root's solve-stage output). Concepts: `black-box-vs-accelerated-kernels` (§"the combinators rise regardless", §2 same-shape-different-fold guard). Sibling combinators: [`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md) (scalar-only same-corner sibling — the non-unify), [`sparameter_reduce`](./sparameter_reduce.md), [`domain_energy_reduce`](./domain_energy_reduce.md). Composed by: [`waveguide-mode.L4`](../feature/waveguide-mode.L4.md). Record `WaveguideModeTable` (current home: the waveguide-mode.L4 composition root §Inputs/outputs). | L1 the per-mode field/scalar maps (the eigenvalue un-transform + the `n_eff` divide + the VD back-transform + the Poynting power-normalization + the conditional curl `Bz`) by **identity-in-form on the body** (a plain per-mode `map`; **no dedicated L4>L3 theme** — the in-line-marker route; the substantive downward content is the two readout loops + the VD back-transform + Poynting + discrete-curl methods in the boundary-mode driver/model L0). | `firm` (formalized cycle-118 D5 from the `waveguide-mode.{L4,L1}` feature-column forward-mine flags + OQ `waveguide-mode-reduce-needs-l4-verb-home`; structure read off the two positive readout loops `boundarymodesolver.cpp:272-340` + the `IsPropagating` predicate `modeeigensolver.cpp:516-519`; firm on the **firm-on-positive-structure / syntactic-identity escape** — every per-mode map law a read-off syntactic identity over positive source + opaque boundary-mode-model-method outputs (VD back-transform / Poynting / discrete-curl, collected verbatim), carrying no inner-product-axiom content (the matrix-weighted-norm contrast), the missing dedicated assembly test redundant under the escape — the exact `eigenfreq_qfactor_reduce` c082 / `sparameter_reduce` c083 / `domain_energy_reduce` c091 sibling disposition. Single-pipeline (boundary-mode) BY DESIGN; propagating-vs-evanescent a variant axis not a 2nd pipeline. Genuine NEW spine vocabulary — the boundary-mode output-product reduction verb, the field-carrying propagation-mode member of the reduce-verb algebra, NOT an `eigenfreq_qfactor_reduce` specialization (over-unification guard closed-negative)) |
```

(Integrator: insert this row immediately after the `sparameter_reduce` row at `book/src/L4/index.md:120`, preserving the alpha order within the Data-algebra group. Also bump the group's firm-count header at `:44` "Firm at L4 (21 + 4 outer-driver)" → "(22 + 4 outer-driver)" if the count convention is maintained — verify the live count.)

### (3) Add the `SUMMARY.md` entry (alpha within the Data-algebra group, after `sparameter_reduce`)

```edit:book/src/SUMMARY.md
  - [waveguide_mode_reduce](./L4/waveguide_mode_reduce.md)
```

(Integrator: insert immediately after `  - [sparameter_reduce](./L4/sparameter_reduce.md)` at `book/src/SUMMARY.md:74`, before the `- [Outer-driver caps & coordination combinators]` group at `:75`.)

### (4) COUPLED COLUMN PROMOTION — flip `waveguide-mode.{L4,L1}` rough-in → firm

Flip both feature-column chapters' `rank` and the prose status. KEEP `feature_root: seed` (the permanent GC-root marker, NOT a ladder rung). Add the `waveguide-mode.L4` `depends-on (kind: composes)` → `L4/waveguide_mode_reduce` edge.

```edit:book/src/feature/waveguide-mode.L4.md
rank: firm
edges:
  depends-on:
    - target: feature/boundary-mode.L4
      kind: composes
    - target: L4/waveguide_mode_reduce
      kind: composes
    - target: palace/drivers/boundarymodesolver.cpp:273-340
      kind: cites-evidence
    - target: concepts/config-record
      kind: uses-record               # input signature: waveguide_mode :: BoundaryModeConfig -> WaveguideModeTable (the IoData surface)
```

(Integrator: replace the `waveguide-mode.L4.md` frontmatter `rank: rough-in` + the `depends-on` block `:6-14` with the above — adds the `L4/waveguide_mode_reduce` composes edge, keeps `feature_root: seed` at `:5`. Then update the prose: the §Status `rough-in` → `firm` and the constituent-down-link table row for `waveguide_mode_reduce` `:83` from `rough-in` to a live link `[\`waveguide_mode_reduce\`](../L4/waveguide_mode_reduce.md)` `firm`, and the inline "no firm L4 home yet" mentions `:36,49` to "the firm L4 reduce verb [\`waveguide_mode_reduce\`](../L4/waveguide_mode_reduce.md)". Promotion rationale: the column's OWN reduce verb is now firm — the OWN-COMPOSITION promotion gate clears, the `sparameters`/`sparameter_reduce` c083 precedent.)

```edit:book/src/feature/waveguide-mode.L1.md
rank: firm
```

(Integrator: flip `waveguide-mode.L1.md` frontmatter `rank: rough-in` → `firm` `:6`, keep `feature_root: seed` `:5`; update §Status `rough-in` → `firm` and the constituent-down-link row `:76` to reference the now-firm `waveguide_mode_reduce` L4 home, and the inline "no firm L4 verb home yet" mentions `:47` accordingly. Same OWN-COMPOSITION gate-clear rationale.)

**Fallback (if verb-firmness is judged insufficient for clean column promotion):** defer the (4) column flips to a follow-on `lifter` dispatch, landing only (1)-(3) (the firm verb chapter + dep-map row + SUMMARY entry) this cycle, and leave the columns at `rough-in` with their down-link rows updated to the now-firm verb link (the link resolves; only the column `rank` stays `rough-in`). The EXPECTED path is in-dispatch promotion — the verb is cleanly defined + exhaustively cited, and the OWN-COMPOSITION gate is exactly the `sparameter_reduce`/`sparameters` c083 situation where the column promoted with the verb.

## Supporting evidence

- L0 positive witness: `palace/drivers/boundarymodesolver.cpp:272-340` (the two readout
  loops), `palace/models/modeeigensolver.cpp:516-519` (the `IsPropagating` predicate) —
  both self-verified on-disk this dispatch via codemap `read_range`.
- Feature-column flags (the demand): `book/src/feature/waveguide-mode.L4.md:36,49,59,83`,
  `book/src/feature/waveguide-mode.L1.md:47,76`.
- Sibling reduce verbs (the family + the template + the non-unify contrast):
  `book/src/L4/eigenfreq_qfactor_reduce.md`, `book/src/L4/sparameter_reduce.md`,
  `book/src/L4/domain_energy_reduce.md`, `book/src/L4/gram_reduce.md`.
- Warrant: `book/src/concepts/black-box-vs-accelerated-kernels.md` §"The combinators rise
  regardless" + §2 (same-shape-different-fold guard).
- Consumed cap: `book/src/L4/eigsolve.md`.
- Semantic surface (USE+LINK, not re-stated): `book/src/semantics/index.md` §1.2.1
  (named-shape-groups; the chapter LINKS it for the `Tensor[N]`-is-correct-here judgment on
  the flat dof-vector fields, does not transcribe the rule).

## Open questions / caveats

Append to `scaffolding/open-questions.md`:

- `waveguide-mode-reduce-vs-eigenfreq-qfactor-reduce-non-unify-closed-negative` (CLOSED-NEGATIVE
  this dispatch) — the two reduce verbs share the `eigsolve` solve-corner but stay DISTINCT
  siblings: `waveguide_mode_reduce` carries mode FIELDS `(Et,En,Bz)`, `eigenfreq_qfactor_reduce`
  is scalar-only `[(f,Q)]`; different result kind/fold + different driver (2D-submesh
  boundary-mode vs 3D-domain eigenmode) + different body. Recorded as the over-unification
  guard outcome (the guard-OQ the dispatch scope hard-mandated); the same-layer-cross-cutter
  may re-probe but the closed-negative reasoning is the c074-D6-`gram_reduce` discipline.
- `waveguide-mode-reduce-field-map-l1-homes` (OPEN) — the per-mode field maps this verb folds
  (the VD back-transform `(Et,En)`, the Poynting power-normalization, the discrete-curl `Bz`
  formation) bottom out in `ModeOperator`/`ModeEigenSolver` boundary-mode model methods at L0
  (`mode_op.ApplyVDBackTransform` / `ComputePoyntingPower` / `GetDiscreteInterpolator`) and
  have no dedicated firm L1 homes yet. The verb is firm on the firm-on-positive-structure escape
  regardless (it collects opaque model-method outputs verbatim, the `eigsolve`-opaque-leaf
  pattern), but a future harvester pass could home the VD back-transform / Poynting /
  discrete-curl as L1 primitives if they recur (the discrete-curl interpolator is a candidate
  cross-pipeline shared primitive — flagged for combinator-miner re-probe).
- `waveguide-mode-reduce-needs-l4-verb-home` (RESOLVED this dispatch) — the OQ that flagged
  the missing L4 home is closed by this chapter; the coupled column promotion clears the
  OWN-COMPOSITION gate.
- Caveat: the dispatch scope named the L0 range as `:300-340`; the FULL reduction spans
  `:272-340` (the `kn`/`n_eff` print loop at `:272-278` precedes the field-readout loop at
  `:292-335`; the function returns `:339-340`). The chapter cites the full `:272-340` range.
  The dispatch's `:300-340` covers only the field-readout loop body; the `kn`/`n_eff` scalar
  un-transform (the first two row fields) lives in the earlier `:272-278` loop. END line on
  disk: the function returns at `:339-340`, NOT `:340` as a body line — the `:272-340` range
  is the body+return-brace span (verified on-disk).
- `WaveguideModeTable` record home: referenced by its CURRENT in-chapter home (the
  `waveguide-mode.L4` composition root §Inputs/outputs), NOT a `concepts/WaveguideModeTable.md`
  link (D6 owns that judgment this cycle, per the dispatch scope). The record has ≥2 consumers
  now (the L4 + L1 columns + this verb chapter) — a `concepts/` page MAY be warranted; deferred
  to D6.
