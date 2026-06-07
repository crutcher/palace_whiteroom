---
agent: layer-intro-author
invoked_at: 2026-06-07T054924Z
scope: RE10 discharge — ground L1/interpolator off detritus via two faithful depends-on edges
status: pending
integrated_at: 2026-06-07T054924Z
integration_commit: ae2e2f4
integration_notes: "Applied clean. RE10 DISCHARGED — L1/interpolator grounded via divfree-projector + waveguide_mode_reduce depends-on(uses) edges."
---

# CYCLE: D8 — re10-interpolator-ground

## Summary

DISCHARGE RE10 by GROUNDING `book/src/L1/interpolator.md` (currently a detritus node — reachability GC `[GARBAGE*]`, inbound only from its own equally-detritus `interpolator-construction-rotation` lowering theme, a non-rooted mutual pair) with **two faithful `depends-on (kind: uses)` edges from reachable consumers**:

1. `book/src/L1/divfree-projector.md → book/src/L1/interpolator.md` (`kind: uses`) — divfree-projector's `Grad` discrete-gradient step IS `interpolator`'s exact L0 lift (`GetDiscreteInterpolator`), `palace/linalg/divfree.cpp:117`. Within-L1 primary edge.
2. `book/src/L4/waveguide_mode_reduce.md → book/src/L1/interpolator.md` (`kind: uses`) — the `Bz = curl(Et)/(iω)` formation constructs the discrete-curl `CurlOp` via `GetDiscreteInterpolator`, `palace/drivers/boundarymodesolver.cpp:319-323`. An L4→L1 altitude-skip (precedented by RE2/RE8/c110 altitude-skip cases — the consumer is a feature-surface reduce verb whose readout calls the L1 interpolator directly; no intervening L3/L2 absorption reshapes the call).

Both consumer nodes (`L1/divfree-projector`, `L4/waveguide_mode_reduce`) are confirmed REACHABLE (neither appears in the GC garbage list); both are `rank: firm`. `interpolator` is `rank: firm`. So every new `depends-on` edge satisfies the well-foundedness invariant `rank(u) ≤ rank(v)` at firm/firm, and the inbound edges propagate liveness into `interpolator` (and transitively into `interpolator-construction-rotation` via its existing inbound edge from `interpolator`). This is the §2f GROUND disposition (preferred over remove/route): the detritus node is a genuine, citation-grounded dependency of reachable goal nodes whose only defect was a missing typed `depends-on` edge.

Verifications performed this dispatch:
- `citecheck --anchor`: `palace/linalg/divfree.cpp:117` anchor `Grad` → `[ok]`; `palace/drivers/boundarymodesolver.cpp:319-323` anchor `Interpolator` → `[ok]` (at `:322`).
- On-disk source read (codemap `read_range`): `divfree.cpp:117` = `Grad = &nd_fespace.GetDiscreteInterpolator(h1_fespaces.GetFinestFESpace());`; `boundarymodesolver.cpp:319-323` = `const auto &CurlOp = mode_op.GetCurlSpace().GetDiscreteInterpolator(mode_op.GetNDSpace());` — both are genuine `interpolator`-operator calls (the `GetDiscreteInterpolator` member `interpolator` lifts, per `L1/interpolator.md:42-43`). Faithful-edge confirmed, not forced.
- Linter (`graded_stack_lint.py --show-inbound`): pre-edit `L1/interpolator` = `[GARBAGE*]`, inbound only `<- L1-L0/interpolator-construction-rotation`. Both consumers absent from garbage list (reachable).

FULL `book/src/L1/...` target paths used to disambiguate the bare-basename `interpolator` AMBIG the planner flagged.

## Proposed changes

### 1. `book/src/L1/divfree-projector.md` — add inbound `depends-on (kind: uses)` edge to interpolator + §Dependencies prose

```edit:book/src/L1/divfree-projector.md
[old]:
  depends-on:
    - target: L1-L0/divfree-projector-mutation-rotation
      kind: lowers-to             # the L1>L0 mutation-rotation home
    - L1/ksp_solve                # the inner projected-H1 solve (step 3)
    - L1/apply_linop              # step-1 WeakDiv apply + step-4 Grad apply
    - L1/axpy                     # step-4 additive gradient correction
[new]:
  depends-on:
    - target: L1-L0/divfree-projector-mutation-rotation
      kind: lowers-to             # the L1>L0 mutation-rotation home
    - L1/ksp_solve                # the inner projected-H1 solve (step 3)
    - L1/apply_linop              # step-1 WeakDiv apply + step-4 Grad apply
    - L1/axpy                     # step-4 additive gradient correction
    - target: book/src/L1/interpolator.md
      kind: uses                  # the Grad discrete-gradient operator IS interpolator's L0 lift (GetDiscreteInterpolator, palace/linalg/divfree.cpp:117)
```

```edit:book/src/L1/divfree-projector.md
[old]:
- [`apply_linop`](./apply_linop.md) — the `WeakDiv·y` (step 1) and `Grad·ψ`
  (step 4) linear-operator applications.
- [`axpy`](./axpy.md) — the `y + Grad·ψ` gradient correction (step 4, fused as
  `Grad->AddMult(ψ, y, 1.0)`, the apply-and-accumulate idiom).
[new]:
- [`apply_linop`](./apply_linop.md) — the `WeakDiv·y` (step 1) and `Grad·ψ`
  (step 4) linear-operator applications.
- [`axpy`](./axpy.md) — the `y + Grad·ψ` gradient correction (step 4, fused as
  `Grad->AddMult(ψ, y, 1.0)`, the apply-and-accumulate idiom).
- [`interpolator`](./interpolator.md) — the construction of the `P.Grad` discrete
  gradient operator. `Grad` is the de-Rham discrete grid-transfer operator
  `interpolator` constructs (`Grad = &nd_fespace.GetDiscreteInterpolator(...)`,
  `palace/linalg/divfree.cpp:117`); the projector *uses* this constructed `LinOp`
  in steps 1/4 (`uses` edge — a build-time construction dependency on the
  interpolator operator, distinct from the run-time `apply_linop` application).
```

### 2. `book/src/L4/waveguide_mode_reduce.md` — add inbound `depends-on (kind: uses)` edge to interpolator + §Dependencies prose

```edit:book/src/L4/waveguide_mode_reduce.md
[old]:
  depends-on:
    - target: L4/eigsolve
      kind: composes               # consumes the converged eigenpair family eigsolve returns
    - target: palace/drivers/boundarymodesolver.cpp:272-340
      kind: cites-evidence
[new]:
  depends-on:
    - target: L4/eigsolve
      kind: composes               # consumes the converged eigenpair family eigsolve returns
    - target: book/src/L1/interpolator.md
      kind: uses                   # the Bz = curl(Et)/(iω) formation constructs the discrete-curl CurlOp via GetDiscreteInterpolator (boundarymodesolver.cpp:319-323); an L4→L1 altitude-skip (RE2/RE8/c110 precedent)
    - target: palace/drivers/boundarymodesolver.cpp:272-340
      kind: cites-evidence
```

```edit:book/src/L4/waveguide_mode_reduce.md
[old]:
The per-mode field maps this folds — the VD back-transform `(Et, En)`, the Poynting
power-normalization, and the discrete-curl `Bz` formation — bottom out in
`ModeOperator` / `ModeEigenSolver` boundary-mode model methods at L0
(`mode_op.ApplyVDBackTransform` / `ComputePoyntingPower` / `GetDiscreteInterpolator`);
their dedicated L1 homes are deferred (OQ
`waveguide-mode-reduce-field-map-l1-homes`).
[new]:
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
dependency on the firm L1 interpolator (the RE2/RE8/c110 altitude-skip precedent: the
reduce verb's readout calls the L1 operator directly, with no intervening L3/L2
absorption reshaping the call).
```

## Supporting evidence

- **Source sites verified (codemap on-disk `read_range` + `citecheck --anchor`):**
  - `palace/linalg/divfree.cpp:117` — `Grad = &nd_fespace.GetDiscreteInterpolator(h1_fespaces.GetFinestFESpace());` — the `Grad` discrete-gradient is `interpolator`'s L0 lift (`GetDiscreteInterpolator`, the member `L1/interpolator.md:42-43` formalizes). `citecheck` anchor `Grad` → `[ok]`.
  - `palace/drivers/boundarymodesolver.cpp:319-323` — `const auto &CurlOp = mode_op.GetCurlSpace().GetDiscreteInterpolator(mode_op.GetNDSpace());` inside the `IsPropagating` arm, used by `CurlOp.Mult(et.Real/Imag, ...)` to form `Bz`. `citecheck` anchor `Interpolator` → `[ok]` (at `:322`).
- **Reachability / well-foundedness:** `L1/interpolator` `rank: firm`; consumers `L1/divfree-projector` `rank: firm` and `L4/waveguide_mode_reduce` `rank: firm`, both confirmed reachable (absent from GC garbage list). New edges satisfy `rank(u) ≤ rank(v)` at firm/firm; liveness now propagates into `interpolator` and (transitively) `interpolator-construction-rotation`.
- **Existing prose already names both consumers** (so the edges make the prose's claims structural, not new content): `L1/interpolator.md:23` lists `L1/divfree-projector` as a `reference` consumer; `:35-38`, `:249-252`, `:266-267` name the divfree `Grad` step and the boundary-mode discrete-curl `Bz` readout. The edges were the missing typed-`depends-on` defect, exactly the §2f GROUND case.
- **Disposition:** §2f priority order (1) GROUND — preferred. No remove (not genuine detritus), no false/forced edge (both calls are genuine `GetDiscreteInterpolator` = `interpolator` invocations).

## Open questions / caveats

- **`L1/interpolator.md`'s own `reference` list at `:23` carries a backward "consumer:" note** to `L1/divfree-projector` (a navigational see-also pointing the *other* direction). The authoritative forward `depends-on (uses)` edge now lives on the consumer (`divfree-projector → interpolator`), per the "edge belongs on the consumer" discipline. The existing `:23` reference note is harmless (free navigational) and is left as-is; no edit to `interpolator.md` is in scope this dispatch (the GROUND is the two inbound edges on the consumers). Flag for a future dep-map refresh if the redundant backward note should be trimmed.
- **RE10 discharge confirmation runs on the LANDED tree (c122).** Per the planner's standing every-batch RE-premise-re-check, the authoritative `STRONGER 27→25` / `+2 reachable` confirmation runs after these edges land; this dispatch performed the pre-edit linter read (interpolator `[GARBAGE*]`, inbound only the mutual lowering theme) and the source/well-foundedness verification, but the post-landing re-measure is the c122 planner's duty.
- **Altitude-skip class (edge 2):** the `L4 → L1` edge is an altitude skip (skips L3/L2). This is faithful here — the reduce verb's `Bz` readout calls the L1 interpolator construction DIRECTLY in the C++ (`boundarymodesolver.cpp:319-323`), and `waveguide_mode_reduce` "lowers by identity-in-form on the body" with "no intervening L3/L2 absorption" (its own §Lowers-to, `:226-236`), so there is no L3/L2 node to route through. Precedented by RE2/RE8/c110 altitude-skip cases. If a future L3/L2 interpolator-application home is authored for this readout, the edge would be re-anchored to it (not expected — the call is a direct construction-then-apply).
