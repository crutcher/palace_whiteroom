---
layer: L4
operator: waveguide_mode_reduce
firmness: firm
edges:
  rank: firm
  depends-on:
    - target: L4/eigsolve
      kind: composes               # consumes the converged eigenpair family eigsolve returns
    - target: book/src/L1/interpolator.md
      kind: uses                   # the Bz = curl(Et)/(iω) formation constructs the discrete-curl CurlOp via GetDiscreteInterpolator (boundarymodesolver.cpp:319-323); an L4→L1 altitude-skip
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
  defined in its cross-cutting home
  ([`concepts/WaveguideModeTable.md`](../concepts/WaveguideModeTable.md)).
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
`waveguide-mode-reduce-field-map-l1-homes`). The one exception with a firm L1 home is
the discrete-curl operator behind `Bz`: the `CurlOp` the `Bz = curl(Et)/(iω)` formation
applies is the de-Rham discrete grid-transfer operator
[`interpolator`](../L1/interpolator.md) constructs
(`mode_op.GetCurlSpace().GetDiscreteInterpolator(mode_op.GetNDSpace())`,
`palace/drivers/boundarymodesolver.cpp:319-323`) — an L4→L1 altitude-skip `uses`
dependency on the firm L1 interpolator: the reduce verb's readout calls the L1 operator
directly, with no intervening L3/L2 absorption reshaping the call.

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

## Evidence

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
