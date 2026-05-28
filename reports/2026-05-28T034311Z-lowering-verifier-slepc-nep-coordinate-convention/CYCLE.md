---
agent: lowering-verifier
invoked_at: 2026-05-28T034311Z
scope: SLEPc-NEP coordinate-convention audit — eigsolve §5 scaling-coordinate convention (cycle-011 OQ eigsolve-slepc-nep-coordinate-convention-audit)
status: integrated
integrated_at: 2026-05-28T072500Z
integration_commit: 5964cb4
integration_notes: "Applied cycle-012 (report 4 of 8). SLEPc-NEP coordinate-convention audit; verdict resolved-with-refinement (two-mechanism finding; gamma/delta dead store). book/src/L1/eigsolve.md §5 prose refined + ## Verified-against section appended + carry-forward citation fix arpack.cpp:387->:383 at :116 + :222. Closes cycle-011 OQ eigsolve-slepc-nep-coordinate-convention-audit; with this the cycle-009 eigsolve OQ cluster is fully closed across cycles 010/011/012. 1 new low-priority OQ. 2 citation-carry-forward gate hits (both verified). Build exit 0."
inputs:
  - book/src/L1/eigsolve.md (Algebraic-laws §5, Variant-axes "scaling", Status block)
  - scaffolding/open-questions.md (OQ eigsolve-slepc-nep-coordinate-convention-audit, opened cycle-011 by repairer)
  - palace/linalg/slepc.cpp:711-730 (SlepcEPSSolverBase::GetEigenvalue / GetEigenvector)
  - palace/linalg/slepc.cpp:1194-1215 (SlepcPEPSolverBase::GetEigenvalue / GetEigenvector)
  - palace/linalg/slepc.cpp:1554-1575 (SlepcNEPSolverBase::GetEigenvalue / GetEigenvector)
  - palace/linalg/slepc.cpp:1618-1745 (SlepcNEPSolver::SetOperators, both overloads)
  - palace/linalg/slepc.cpp:1760-1798 (SlepcNEPSolver::GetResidualNorm / GetBackwardScaling)
  - palace/linalg/slepc.cpp:1801-1841 (__mat_apply_EPS_A0 / _A1 — scaled-coordinate witness)
  - palace/linalg/slepc.cpp:2000-2060 (__mat_apply_PEP_A0/_A1/_A2/_B — PEP companion-form callbacks)
  - palace/linalg/slepc.cpp:2096-2202 (__mat_apply_NEP_A/_J/_B, __pc_apply_NEP, __form_NEP_function, __form_NEP_jacobian)
  - palace/linalg/slepc.cpp:674, 1157, 1503 (EPS/PEP/NEP target-setting — the / gamma asymmetry)
  - palace/linalg/arpack.cpp:383-392 (ARPACK eig[i] *= gamma un-scale)
---

# CYCLE: Audit SLEPc-NEP coordinate-convention

## Summary

This audit resolves cycle-011 OQ `eigsolve-slepc-nep-coordinate-convention-audit`. The question: is the
"un-scale-at-accessor" eigenvalue-coordinate convention (L1 `eigsolve` §5 convention (b): "L1 returns
un-scaled, original-problem-coordinate eigenvalues") uniform across all 4 backends (ARPACK / SLEPc-EPS /
SLEPc-PEP / SLEPc-NEP), or does SLEPc-NEP break it?

**Verdict: confirms uniform in result-coordinates, with a refinement to the mechanism statement.** All four
backends return eigenvalues in original-problem coordinates at the L0 accessor boundary — convention (b) holds
uniformly. **But the L1 §5 prose is materially misleading about *how* NEP achieves this.** ARPACK/EPS/PEP solve
in *scaled* internal coordinates and un-scale at the accessor (`* gamma`); SLEPc-NEP solves in *un-scaled
(original-problem) coordinates end-to-end*, so its accessor correctly returns `l` directly with **no
un-scale needed** — not a missing `* gamma`. The `gamma`/`delta` that NEP `SetOperators` computes are an
effectively-dead store in the NEP eigenvalue-coordinate path (the function/jacobian callbacks build the
operator polynomial with raw operators and unit coefficients, and `NEPSetTarget` is called with un-scaled
`sigma`). The cycle-011 framing — "a genuine asymmetry... is there a missing `* gamma`?" — resolves to:
**no missing un-scale; the eigenvalues are already in original-problem coordinates.** The OQ resolves
**resolved-with-refinement**: L1 §5 should be tightened to state the per-backend mechanism precisely rather
than flagging the NEP path as "pending audit / manages its own coordinate handling separately."

## Per-citation audit

### Citation: palace/linalg/slepc.cpp:1554-1560 (SlepcNEPSolverBase::GetEigenvalue)
- **Theme claim (L1 §5)**: "SLEPc-NEP at `slepc.cpp:1554-1560` returns `l` directly without applying `* gamma`."
- **Found**: Confirmed. `GetEigenvalue(int i)` body (lines 1554-1560):
  ```cpp
  std::complex<double> SlepcNEPSolverBase::GetEigenvalue(int i) const
  {
    PetscScalar l;
    const int &j = perm.get()[i];
    PalacePetscCall(NEPGetEigenpair(nep, j, &l, nullptr, nullptr, nullptr));
    return l;
  }
  ```
  Returns `l` with no `* gamma`. (Note: NEP additionally indirects through a `perm` permutation array, which
  EPS/PEP `GetEigenvalue` do not — a minor extra detail, not coordinate-related.)
- **Verdict**: supports (range accurate; the cited line range 1554-1560 matches the function body exactly).
- **Notes**: Contrast with EPS `GetEigenvalue` (slepc.cpp:711-715) `return l * gamma;` and PEP
  `GetEigenvalue` (slepc.cpp:1194-1198) `return l * gamma;` — both verified, both apply `* gamma`.

### Citation: palace/linalg/slepc.cpp:1645-1651 (SlepcNEPSolver::SetOperators K-M overload — gamma computation)
- **Theme claim (L1 §5 parenthetical)**: NEP `SetOperators` at `:1645-1651` "DOES compute a non-trivial
  `gamma = std::sqrt(normK / normM)` when `type != ScaleType::NONE`."
- **Found**: Confirmed, with a slight range drift. The K-M `SetOperators` overload spans 1618-1677; the gamma
  computation is at lines 1649-1650:
  ```cpp
  gamma = std::sqrt(normK / normM);
  delta = 2.0 / normK;
  ```
  inside the `if (first && type != ScaleType::NONE)` block at 1642-1651. The cited range `1645-1651` lands
  inside the correct block (the `normK`/`normM` `SpectralNorm` calls are at 1644-1645, the guarded gamma/delta
  assignment at 1647-1651). Range is accurate enough (it captures the gamma assignment).
- **Verdict**: supports.
- **Notes**: This is the K-M (linear-NEP) overload. `delta = 2.0 / normK` here (the linear-case delta), vs.
  `delta = 2.0 / (normK + gamma * normC)` in the K-C-M overload.

### Citation: palace/linalg/slepc.cpp:1711-1719 (SlepcNEPSolver::SetOperators K-C-M overload — gamma computation)
- **Theme claim (L1 §5 parenthetical)**: same gamma computation at `:1711-1719`.
- **Found**: Confirmed. The K-C-M `SetOperators` overload spans 1680-1745; the gamma computation is at lines
  1715-1716: `gamma = std::sqrt(normK / normM); delta = 2.0 / (normK + gamma * normC);` inside the
  `if (first && type != ScaleType::NONE)` block (1707-1717). Cited range `1711-1719` lands inside the block.
- **Verdict**: supports.

### Citation (new, decisive — not in current L1 §5): the NEP function/jacobian callbacks build with RAW operators
- **What I checked**: `__form_NEP_function` (slepc.cpp:2170-2183) and `__form_NEP_jacobian` (2185-2202).
- **Found**: The function callback builds `A(λ) = K + λ C + λ² M + A2(Im{λ})` via
  ```cpp
  ctxF->opA = palace::BuildParSumOperator(
      {1.0 + 0.0i, lambda, lambda * lambda, 1.0 + 0.0i},
      {ctxF->opK, ctxF->opC, ctxF->opM, ctxF->opA2.get()}, true);
  ```
  Coefficients `{1, λ, λ², 1}` against the **raw, un-scaled** `opK, opC, opM, opA2` — **no `delta`
  premultiplier on operators, no `gamma` reparametrization of `λ`.** The jacobian (2185-2202) likewise builds
  `J(λ) = C + 2λM + A2'` with raw operators and unit/`2λ` coefficients. The shell-mult callbacks
  `__mat_apply_NEP_A` (2096-2106) and `__mat_apply_NEP_J` (2108-2118) just call `ctx->opA->Mult` /
  `ctx->opJ->Mult` — **no `*= delta`/`*= gamma` scaling.** `__mat_apply_NEP_B` (2120-2130) also does **not**
  apply `delta*gamma` (contrast PEP_B at 2059 which does).
- **Verdict**: supports the "NEP works in un-scaled coordinates" conclusion (this is the load-bearing evidence).
- **Notes**: This is the decisive contrast against EPS, whose shell callbacks DO scale (see below).

### Citation (new, contrast witness): EPS/PEP scale operators in callbacks; NEP does not
- **What I checked**: `__mat_apply_EPS_A0` (slepc.cpp:1801-1814), `__mat_apply_EPS_A1` (1816-1828).
- **Found**: EPS A0 (the K-action) applies `ctx->y1 *= ctx->delta;` (line 1810); EPS A1 (the M-action) applies
  `ctx->y1 *= ctx->delta * ctx->gamma;` (line 1825). So SLEPc-EPS solves the *scaled* generalized problem
  `δK·x = θ·(δγM)·x`, where the SLEPc-internal eigenvalue is `θ = λ/γ`; Palace un-scales via `return l * gamma`.
  (The PEP companion-form callbacks at 1841-2083 carry the analogous `delta*gamma`/`delta*gamma²` scaling;
  PEP_B at 2059 scales, EPS_B analogously.)
- **Verdict**: supports — establishes that the EPS/PEP `* gamma` un-scale is *necessary* because those
  backends genuinely solve a scaled problem, whereas NEP does not scale and therefore needs no un-scale.

### Citation (new, decisive — the target-setting asymmetry): EPS/PEP set target / gamma; NEP sets target un-scaled
- **What I checked**: `EPSSetTarget(eps, sigma / gamma)` (slepc.cpp:674), `PEPSetTarget(pep, sigma / gamma)`
  (1157), `NEPSetTarget(nep, sigma)` (1503).
- **Found**: EPS and PEP set the SLEPc spectral target divided by `gamma` (consistent with the solver seeing
  `θ = λ/γ`). NEP sets the target as the *un-scaled* `sigma` — NO `/ gamma`. This is the symmetric companion to
  NEP's `return l;` (no `* gamma` out, because no `/ gamma` in). End-to-end, the NEP backend's caller-facing
  eigenvalue coordinate is the original-problem coordinate.
- **Verdict**: supports — closes the loop: un-scaled target in ⇒ un-scaled eigenvalue out.

### Citation (new): NEP GetResidualNorm / GetBackwardScaling use raw operators with un-scaled λ
- **What I checked**: `SlepcNEPSolver::GetResidualNorm` (slepc.cpp:1760-1777), `GetBackwardScaling`
  (1779-1798), and the `GetError` dispatch (476-494) + `RescaleEigenvectors` (496-509).
- **Found**: `RescaleEigenvectors` (505-507) computes `res[i] = GetResidualNorm(GetEigenvalue(i), ...) / ‖x‖`.
  NEP's `GetResidualNorm` builds `‖(K + λC + λ²M + A2(λ))x‖` using **raw** `opK, opC, opM, A2` and the
  `l = GetEigenvalue(i)` value (1765-1776). This is internally consistent ONLY if `GetEigenvalue` returns
  the un-scaled `λ` (which `return l;` does, given the un-scaled target). The residual is in original-problem
  coordinates. `GetBackwardScaling` (1779-1798) recomputes `normK/normC/normM` independently of the
  scaling-time values, with a `// Make sure not to use norms from scaling` comment — i.e., it deliberately
  does NOT reuse the `SetOperators` gamma/delta norms.
- **Verdict**: supports — corroborates that the entire NEP error-reporting path operates in un-scaled coords,
  reinforcing that the NEP `gamma`/`delta` are not consumed for any eigenvalue-coordinate transform.

## Applicability conditions

The theme states convention (b) is "uniform across EPS / PEP / NLEPS — caller-observable eigenvalues are in
original-problem coordinates — with the SLEPc-NEP convention pending audit." Conditions audited:

- **Condition**: "un-scaling is performed at the L0 GetEigenvalue accessor boundary across the EPS / PEP /
  NLEPS backends" (ARPACK `arpack.cpp:383`, EPS `slepc.cpp:711-716`, PEP `slepc.cpp:1194-1203`, NLEPS
  `nleps.cpp:88-93`).
  - **Verifiable**: Verified for ARPACK (`eig[i] = eig[i] * gamma`, arpack.cpp:383 — confirmed), EPS
    (`return l * gamma`, slepc.cpp:715 — confirmed), PEP (`return l * gamma`, slepc.cpp:1198 — confirmed).
    NLEPS (nleps.cpp) not re-read this dispatch (out of scope — the OQ is SLEPc-NEP-specific; NLEPS is the
    separate Palace-owned `QuasiNewtonSolver`, not the SLEPc NEP backend).
  - **Found counter-example?**: No — for the three backends that scale internally, the `* gamma` un-scale is
    present and correct.
- **Condition (the one under audit)**: SLEPc-NEP "manages its own coordinate handling separately from the EPS
  / PEP un-scale-at-accessor pattern" and "the precise un-scaling convention for the NEP backend is flagged
  for follow-up audit."
  - **Verifiable**: Yes — fully verified via the function/jacobian callbacks (raw operators), the target
    setting (`NEPSetTarget(nep, sigma)`, un-scaled), and the residual path (raw operators with un-scaled λ).
  - **Found counter-example?**: No counter-example to convention (b) — the result IS in original-problem
    coordinates. **But the prose "manages its own coordinate handling separately" overstates the divergence:**
    NEP does not do any *separate* coordinate handling; it does *no* coordinate transform at all (it solves the
    original problem directly). The refinement below corrects this.

## Algebraic laws (if cited)

§5 is the scaling-coordinate convention law. Audited against the NEP operator signatures:

- **Law (L1 §5)**: For `ScaleType = NORM_2`, `EigResult.eigenvalues` is in original-problem coordinates
  (un-scaled), uniformly across backends.
- **Holds on operators?**: **Yes, for all 4 backends including NEP** — but via two distinct mechanisms:
  - ARPACK / EPS / PEP: solve `(δ-scaled, γ-reparametrized)` problem; un-scale eigenvalue `λ = γ·θ` at
    accessor (`* gamma`).
  - NEP: solve the *original* problem `(K + λC + λ²M + A2(λ))x = 0` directly (raw operators, unit
    coefficients, un-scaled target); accessor returns `λ` directly (no transform). The NEP `gamma`/`delta`
    computed at `SetOperators` are **not used** in the eigenvalue-coordinate path (dead store w.r.t. the
    coordinate convention; they are not re-read by the function/jacobian/target/residual paths).
  The law holds; the *uniform-mechanism* implication that §5's current prose carries ("un-scaling is performed
  at the GetEigenvalue accessor boundary across [all backends]") is **false for NEP** — NEP performs no
  un-scaling at the accessor because there is nothing to un-scale.

## Proposed changes

OQ verdict: **resolved-with-refinement.** Two edits — (1) a `verified_against:` metadata block appended to the
theme; (2) a §5 prose refinement correcting the NEP mechanism statement and dropping the "pending audit" flag.

### (1) Append verified_against metadata block

```edit:book/src/L1/eigsolve.md
[append at end of file]
~~~yaml
verified_against:
  - citation: palace/linalg/slepc.cpp:1554-1560
    verdict: supports
    audited_at: 2026-05-28T034311Z
    note: SlepcNEPSolverBase::GetEigenvalue returns l directly (no * gamma); range accurate.
  - citation: palace/linalg/slepc.cpp:1645-1651
    verdict: supports
    audited_at: 2026-05-28T034311Z
    note: NEP K-M SetOperators computes gamma=sqrt(normK/normM), delta=2/normK at 1649-1650; range captures it.
  - citation: palace/linalg/slepc.cpp:1711-1719
    verdict: supports
    audited_at: 2026-05-28T034311Z
    note: NEP K-C-M SetOperators computes gamma=sqrt(normK/normM), delta=2/(normK+gamma*normC) at 1715-1716.
  - citation: palace/linalg/slepc.cpp:711-716
    verdict: supports
    audited_at: 2026-05-28T034311Z
    note: EPS GetEigenvalue returns l * gamma (scaled-coords backend); confirmed.
  - citation: palace/linalg/slepc.cpp:1194-1203
    verdict: supports
    audited_at: 2026-05-28T034311Z
    note: PEP GetEigenvalue returns l * gamma (scaled-coords backend); confirmed.
  - citation: palace/linalg/arpack.cpp:383
    verdict: supports
    audited_at: 2026-05-28T034311Z
    note: ARPACK eig[i] = eig[i] * gamma un-scale at result extraction (line 383, inside the 381-384 nev loop); confirmed. NB book/src/L1/eigsolve.md:116,222 carry an inherited :387 miscitation — integrator carry-forward to correct in-artifact.
  - citation: palace/linalg/slepc.cpp:2170-2202
    verdict: supports
    audited_at: 2026-05-28T034311Z
    note: NEP __form_NEP_function/__form_NEP_jacobian build A(lambda)/J(lambda) from RAW operators with unit coeffs - no delta/gamma scaling; decisive evidence NEP solves original-problem coords.
  - citation: palace/linalg/slepc.cpp:674
    verdict: partially-supports
    audited_at: 2026-05-28T034311Z
    note: EPSSetTarget(eps, sigma / gamma) - EPS target in scaled coords; companion to PEP 1157 and contrast to NEP 1503.
  - citation: palace/linalg/slepc.cpp:1503
    verdict: supports
    audited_at: 2026-05-28T034311Z
    note: NEPSetTarget(nep, sigma) - un-scaled target in; symmetric companion to return l (un-scaled out). NEP coordinate convention is un-scaled end-to-end.
  - citation: palace/linalg/slepc.cpp:1801-1825
    verdict: supports
    audited_at: 2026-05-28T034311Z
    note: __mat_apply_EPS_A0/A1 apply *= delta and *= delta*gamma; EPS genuinely solves scaled problem (contrast NEP raw callbacks).
~~~
```

### (2) §5 prose refinement (correct the NEP mechanism statement; drop "pending audit")

**Seam (explicit replacement span).** §5 currently ends with two distinct elements: (i) the SLEPc-NEP
parenthetical block, beginning "SLEPc-NEP at `palace/linalg/slepc.cpp:1554-1560` returns `l` directly without
applying `* gamma`..." through "...flagged for follow-up audit — see `scaffolding/open-questions.md` entry on
NEP scaling gap below)", IMMEDIATELY FOLLOWED BY (ii) a pre-existing trailing sentence
"Resolved (cycle-011, lifter): ... `eigsolve-scaling-coordinate-convention`." The edit below replaces **only
element (i)** (the parenthetical); **element (ii) is left verbatim in place.** The replacement text ends with a
NEW "Resolved (cycle-012, lowering-verifier; OQ `eigsolve-slepc-nep-coordinate-convention-audit`)" sentence
that is to sit BEFORE the retained cycle-011 sentence (the two "Resolved" sentences resolve two different OQs —
cycle-011 closed the general `eigsolve-scaling-coordinate-convention` question; cycle-012 closes the
NEP-specific `eigsolve-slepc-nep-coordinate-convention-audit` follow-up — so both are retained, adjacent, in
cycle order). Net §5 tail after the edit:
[refined NEP parenthetical] → "Resolved (cycle-012, lowering-verifier; OQ
`eigsolve-slepc-nep-coordinate-convention-audit`)." → "Resolved (cycle-011, lifter): ...
`eigsolve-scaling-coordinate-convention`." Proposed replacement of element (i) (integrator or follow-up
lifter to apply):

```edit:book/src/L1/eigsolve.md
[replace ONLY the SLEPc-NEP parenthetical in Algebraic-laws §5; leave the trailing "Resolved (cycle-011, lifter)..." sentence verbatim and immediately after this block]
~~~text
SLEPc-NEP differs in *mechanism* but not in *result coordinate*: the SLEPc-NEP backend solves the
**original (un-scaled) problem directly** rather than a Higham-scaled problem, so its `GetEigenvalue`
(`palace/linalg/slepc.cpp:1554-1560`) correctly returns `l` with no `* gamma` un-scale — there is nothing
to un-scale. The NEP function/jacobian callbacks (`__form_NEP_function` / `__form_NEP_jacobian` at
`palace/linalg/slepc.cpp:2170-2202`) build `A(λ) = K + λC + λ²M + A2(Im{λ})` and its Jacobian from the **raw**
operators with unit/`λ`/`λ²` coefficients (no `δ` premultiplier, no `γ`-reparametrization of `λ`), and the
spectral target is set un-scaled (`NEPSetTarget(nep, sigma)` at `:1503`, contrast `EPSSetTarget(eps, sigma /
gamma)` at `:674` and `PEPSetTarget(pep, sigma / gamma)` at `:1157`). Consequently the `gamma = std::sqrt(normK
/ normM)` / `delta` that `SlepcNEPSolver::SetOperators` computes (`:1649-1650` linear, `:1715-1716` quadratic)
are an **unused (dead) store with respect to the eigenvalue-coordinate transform** — the NEP residual path
(`GetResidualNorm` / `GetBackwardScaling` at `:1760-1798`) recomputes operator norms independently and
deliberately does not reuse the scaling-time `gamma`/`delta` (see the `// Make sure not to use norms from
scaling` comment at `:1781`). The earlier "NEP gamma = 1" reading was wrong (gamma IS computed); the corrected
reading is "NEP computes gamma/delta but does not apply them to the eigenvalue coordinate — it solves and
returns in original-problem coordinates throughout." The un-scale-at-accessor convention (b) therefore holds
**uniformly across all four backends in result coordinates** — ARPACK / EPS / PEP via solve-scaled-then-un-scale
(`* gamma` at the accessor: `arpack.cpp:383`, `slepc.cpp:715`, `slepc.cpp:1198`), SLEPc-NEP via
solve-and-return-un-scaled (`slepc.cpp:1559`). Resolved (cycle-012, lowering-verifier; OQ
`eigsolve-slepc-nep-coordinate-convention-audit`).
~~~
```

**On the "flagged for follow-up audit" wording.** That phrasing ("the SLEPc-NEP detail is non-blocking and
flagged for follow-up audit") lives ONLY inside the §5 cycle-011 trailing "Resolved (cycle-011, lifter): ..."
sentence (eigsolve.md:116) — there is no separate §Status block copy of it (the §Status block at
eigsolve.md:165 records the OQ-cluster resolution but does not carry this NEP phrase). Per the seam spec above
the cycle-011 sentence is **retained verbatim** — it is an accurate historical record of what cycle-011 did
(flag the NEP detail for audit). The new cycle-012 "Resolved" sentence (added by the element-(i) replacement,
sitting immediately before the cycle-011 sentence) is what *closes* that flagged follow-up; it supersedes the
"flagged for follow-up" status in meaning without rewriting the cycle-011 record. No edit to the cycle-011
sentence's "flagged for follow-up" phrasing is needed.

### OQ status change

`scaffolding/open-questions.md` entry `eigsolve-slepc-nep-coordinate-convention-audit` → `status: resolved`
(resolved-with-refinement). The resolution: NEP solves the original (un-scaled) problem directly; `return l`
is correct; the NEP `SetOperators` gamma/delta are dead w.r.t. the coordinate transform. Convention (b) holds
uniformly across all 4 backends. (The integrator-per-report applies OQ status promotion per its authority.)

## Supporting evidence

Source files consulted (all via MCP codemap `read_range` / `search_text`, paths relative to `reference/`):

- `palace/linalg/slepc.cpp:711-730` — EPS GetEigenvalue (`return l * gamma`) / GetEigenvector.
- `palace/linalg/slepc.cpp:1194-1215` — PEP GetEigenvalue (`return l * gamma`) / GetEigenvector.
- `palace/linalg/slepc.cpp:1503` — `NEPSetTarget(nep, sigma)` (un-scaled target).
- `palace/linalg/slepc.cpp:1554-1575` — NEP GetEigenvalue (`return l`) / GetEigenvector.
- `palace/linalg/slepc.cpp:1618-1677` — NEP SetOperators K-M overload (gamma/delta at 1649-1650).
- `palace/linalg/slepc.cpp:1680-1745` — NEP SetOperators K-C-M overload (gamma/delta at 1715-1716).
- `palace/linalg/slepc.cpp:1760-1798` — NEP GetResidualNorm / GetBackwardScaling (raw operators, un-scaled λ).
- `palace/linalg/slepc.cpp:674`, `:1157` — EPS/PEP `SetTarget(..., sigma / gamma)` (scaled target).
- `palace/linalg/slepc.cpp:1801-1841` — `__mat_apply_EPS_A0/_A1` (`*= delta`, `*= delta*gamma`).
- `palace/linalg/slepc.cpp:2000-2060` — `__mat_apply_PEP_A0/_A1/_A2/_B` (PEP companion-form; PEP_B scales).
- `palace/linalg/slepc.cpp:2096-2202` — NEP shell callbacks + function/jacobian (raw operators, no scaling).
- `palace/linalg/slepc.cpp:476-509` — `GetError` / `RescaleEigenvectors` (calls GetResidualNorm with GetEigenvalue).
- `palace/linalg/arpack.cpp:383-392` — ARPACK `eig[i] = eig[i] * gamma` un-scale.

Operator-definition cross-reference: `book/src/L0/eigensolver-wrapper.md` (the 22-virtual `EigenvalueSolver`
surface; `GetEigenvalue` / `RescaleEigenvectors` / `GetScalingGamma` accessors). The `ScaleType` enum
(`palace/linalg/eps.hpp:25-29`) and `GetScalingGamma`/`GetScalingDelta` accessors
(`palace/linalg/eps.hpp:102-103`) confirm gamma/delta are exposed at L0 as `informational` accessors — matching
the L1 §Signature `scaling_gamma`/`scaling_delta` "informational only" framing, which this audit does not
disturb.

No test reference exists for the NEP scaling path (the L1 §Status notes the narrow `test-boundarymodeoperator.cpp`
coverage; no `test-eigensolver.cpp` exercises NEP scaling). The conclusion rests on direct source reading of the
control flow, not an empirical witness — see caveat below.

## Open questions / caveats

1. **No empirical witness for the NEP un-scaled-coordinate conclusion.** The verdict rests on tracing the
   control flow (raw-operator callbacks + un-scaled target + un-scaled residual path) rather than a test that
   constructs a known-eigenvalue NEP and asserts the returned eigenvalue is in original coordinates. The
   reading is unambiguous at the source level (there is no `delta`/`gamma` application anywhere in the NEP
   eigenvalue-coordinate path, confirmed by exhaustive `search_text` for `gamma|delta` across slepc.cpp — the
   only NEP-region hits are the dead `SetOperators` store at 1649-1650/1715-1716 and the independent norm
   recomputation in `GetBackwardScaling`). But per the L1 §Status rough-in caveat, treat as
   `source-read-confirmed, empirically-unwitnessed` until a `test-eigensolver.cpp` NEP case lands.

2. **Why does NEP compute gamma/delta at all if they are unused?** This is a latent dead-store / possible
   upstream-intent question. The `SetOperators` gamma/delta computation in NEP mirrors the PEP code structure
   (likely copy-adapted from `SlepcPEPSolver::SetOperators`), but the NEP solve path never consumes them. Two
   readings: (a) genuinely dead (the NEP path was written to solve un-scaled and the gamma/delta lines are
   vestigial), or (b) latent — intended for a future `NEPSetScale`-style wiring that was never completed. This
   does not affect the coordinate-convention verdict (either way the *current* eigenvalues are un-scaled), but
   it is a candidate `problems/` drive-by observation about possible dead code in Palace's NEP backend. I am
   NOT filing it (below the per-cycle filing bar for a single dispatch; flagging here for the integrator/critic
   to consider). If a future harvester firms up a `SlepcNEPSolver` L0 entry, it should note the dead store.

3. **NLEPS (`QuasiNewtonSolver`) is a separate backend from SLEPc-NEP.** The OQ and L1 §5 sometimes blur
   "NLEPS" (Palace-owned direct-Newton, `palace/linalg/nleps.cpp`) and "SLEPc-NEP" (SLEPc's nonlinear
   eigensolver, `SlepcNEPSolver` in slepc.cpp). They are *different* backends both targeting the nonlinear
   problem. This audit covers **SLEPc-NEP only** (the OQ's explicit scope). The L1 §5 "EPS / PEP / NLEPS
   uniform" wording uses "NLEPS" to mean the Palace-owned `nleps.cpp:88-93` path; the SLEPc-NEP backend is a
   *fifth* coordinate-handling site that §5 was treating as pending. The refinement above makes the 4-SLEPc/ARPACK
   picture explicit (ARPACK + EPS + PEP + NEP); the Palace-owned NLEPS at nleps.cpp is the separate direct-Newton
   path and is consistent (un-scaled via linear-eigensolver priming per the existing §5 citation
   `nleps.cpp:267, 314`), not re-audited here. A follow-up could confirm the NLEPS path with the same rigor, but
   it is outside this OQ's scope.

4. **Directionality check (high→low):** The theme being touched is `book/src/L1/eigsolve.md` (an L_n operator
   entry, not an L_{n+1}>L_n lowering theme). §5 is an L1 algebraic law stated in L1 vocabulary with L0
   citations for grounding — this is the correct high→low shape (L1 law, L0 evidence). No direction-of-definition
   violation observed; the §5 refinement keeps the law in L1 vocabulary and cites L0 source for the mechanism.
