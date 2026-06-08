---
kind: feature-surface
feature: driven
level: L1
feature_root: seed
rank: firm
edges:
  depends-on:
    - target: L1/fe_assemble
      kind: composes
    - target: L1/assemble_frequency_operator
      kind: composes
    - target: L1/ksp_solve
      kind: composes
    - target: palace/drivers/drivensolver.cpp:77-229
      kind: cites-evidence
  reference:
    - feature/sparameters.L1
---

# driven — L1 composition-root

The **driven (frequency-domain) simulation feature**, presented at L1 as a
pure-function composition of firm L1 operators. This is the **pure-function feature
surface**: the same composition root as the [L4 chapter](./driven.L4.md), but
expressed in L1 vocabulary (explicit per-operator pure functions, no L4 combinator
naming) — the form a reader navigating L1 sees when asking "what whole feature do
these L1 operators add up to?"

At L1 the driven feature is a pure function `config → frequency response` built from
three firm L1 operators, with the **mutation already lifted** (each operator is
mutation-free; the L0 in-place `ksp.Mult(RHS, E)` / per-ω `SetOperators` writes are
lifted to value-returning forms per the L1>L0 mutation rotation). Unlike the
fixed-operator [electrostatic](./electrostatic.L1.md) /
[magnetostatic](./magnetostatic.L1.md) columns (one `K` bound once, read by every
solve), the driven column **rebuilds the operator inside the per-ω comprehension** —
the operator is a per-member value, not a captured invariant. L1 has no outer-driver
combinator name (that naming is L4's [`frequency_sweep`](../L4/frequency_sweep.md));
at L1 the sweep is an explicit comprehension mapping the firm per-ω rebuild +
[`ksp_solve`](../L1/ksp_solve.md) over the swept frequencies.

## The composition

    -- inputs = config; output = the frequency response / S-parameters (the physical product)
    driven :: DrivenConfig -> FrequencyResponse
    driven cfg =
      let space = nd_space cfg
          k     = fe_assemble space [ curl_curl (reluctivity cfg) ]   -- (1a) stiffness K, assembled once
          c     = fe_assemble space [ damping cfg ]                    -- (1b) damping C, assembled once
          m     = fe_assemble space [ mass (permittivity cfg) ]        -- (1c) mass M, assembled once
          fam   = { K = k, C = c, M = m, A2 = \w -> extra_system_matrix space cfg w }
          es    = [ ksp_solve (assemble_frequency_operator fam w)      -- (2) per-ω rebuild + pure solve
                              (excitation cfg w)
                  | w <- sample_frequencies cfg ]
      in  sparameter_response es (ports cfg)                           -- (3) per-ω S-parameter / energy reduction

1. **Assemble the fixed basis `{K, C, M}` once** — [`fe_assemble`](../L1/fe_assemble.md)
   (**firm**). Three L1 assemble folds `K = Σ_i A(space, termᵢ)` etc. over the single
   weak-form term of each operator. Pure: consumes the Nédélec space + term list,
   produces fresh operators. The basis is bound once in the `let` and read by every
   per-ω rebuild — the once-captured construction stratum. L0: `K =
   GetStiffnessMatrix<ComplexOperator>(...)` (`drivensolver.cpp:91`), `C =
   GetDampingMatrix<ComplexOperator>(...)` (`:92`), `M =
   GetMassMatrix<ComplexOperator>(...)` (`:93`).

2. **Per-ω rebuild + pure solve** — the per-frequency body, composing two firm L1
   operators:
   - the per-ω operator rebuild [`assemble_frequency_operator`](../L1/assemble_frequency_operator.md)
     (**firm**) — the affine-in-ω combination `A(ω) = K + iω·C − ω²·M + A2(ω)`, the
     operator-operand `linear_combination` specialization, **rebuilt afresh at each ω**
     from the captured-once basis `fam`. L0: `A = GetSystemMatrix(1.0+0.0i, 1i*ω,
     −ω²+0.0i, K, C, M, A2)` (`drivensolver.cpp:176-177`), with the ω-dependent extra
     term `A2 = GetExtraSystemMatrix<ComplexOperator>(ω, ...)` (`:175`).
   - the per-ω pure solve [`ksp_solve`](../L1/ksp_solve.md) (**firm**) — `eᵢ =
     ksp_solve(A(ωᵢ), rhsᵢ)`, the mutation-lifted pure solve (the L1 form of the L0
     `ksp.Mult(RHS, E)`, the destination-buffer write lifted to a value-returning
     solve). The per-ω RHS `rhsᵢ` is the port-excitation vector at ωᵢ (L0
     `GetExcitationVector(excitation_idx, ω, RHS)`, `:194`). Crucially the **operator
     is re-bound per member**: the L0 `ksp.SetOperators(*A, *P)` sits *inside* the
     comprehension body (`:180`), not hoisted — the operator-varying property the L1
     comprehension makes explicit by computing `assemble_frequency_operator fam w`
     inside the comprehension rather than binding it once. L0: the loop `:168-170`,
     the per-ω solve `:196`.

3. **S-parameter / frequency-response reduction** — the per-ω reduction of the
   solution family `[eᵢ]` to the user-facing frequency response (S-parameters +
   per-frequency field/energy measurements), with the B-field recovery `B = −1/(iω)
   ∇×E`. This stage is the **driven output-product surface**, forward-ref'd to its own
   column (`sparameter_response` is NOT authored here, mirroring how the
   electrostatic/magnetostatic L1 columns forward-ref their capacitance/inductance
   reductions). It is a pure fold of per-ω measurements over the solution family. L0:
   the B-field recovery `Curl.Mult(...)` + `B *= −1.0/(1i*ω)` (`:205-207`), the per-ω
   measurement `MeasureAndPrintAll(...)` (`:216`).

## Inputs / outputs (the feature surface)

- **Input — config.** `DrivenConfig` (mesh + order → Nédélec H(curl) space; material
  coefficients → `K`/`C`/`M` terms + ω-dependent `A2`; swept frequency family → the
  comprehension domain; port-excitation set → the per-ω RHS; linear-solver config).
  All read-only.
- **Output — the physical product.** `FrequencyResponse` — the per-ω frequency
  response (S-parameters + per-frequency field/energy measurements). L0: the per-ω
  `MeasureAndPrintAll(...)` (`drivensolver.cpp:216`) + `MeasureFinalize(indicator)`
  (`:227`).

## L1 vs L4

The L1 and L4 composition roots express the **same feature**; they differ in
vocabulary:
- **L1** (this chapter): three explicit per-operator pure functions for the basis
  assemble + an explicit per-ω comprehension that rebuilds the operator
  ([`assemble_frequency_operator`](../L1/assemble_frequency_operator.md)) and solves
  ([`ksp_solve`](../L1/ksp_solve.md)) inside the comprehension body; the
  operator-varying property is the fact that the rebuild is *inside* the comprehension
  (not bound once before it).
- **L4** ([`driven.L4`](./driven.L4.md)): the per-ω comprehension is the
  [`frequency_sweep`](../L4/frequency_sweep.md) combinator (the operator-VARYING map
  made *structural*: the basis captured once, the per-member operator rebuilt inside
  the map by type — the `operator-capture = per-element` axis, the non-hoist
  contrasting `solve_family`'s fixed-operator hoist). The L4 form is the one the
  outward backend consumes; the L1 form is the pure-function decomposition the L4
  combinators name.

The L1→L0 direction (how each pure operator lowers to the in-place driver writes —
including the per-ω `SetOperators`-inside-the-loop capture) is the per-operator
L1>L0 rotation themes of the constituent ops (e.g.
[`assemble-frequency-operator-rotation`](../L1-L0/assemble-frequency-operator-rotation.md));
this composition root records only the L1 composition (high→low discipline).

## Constituent down-links

| Stage | L1 operator | Status | L0 site |
|---|---|---|---|
| assemble basis {K, C, M} once | [`fe_assemble`](../L1/fe_assemble.md) | firm | `drivensolver.cpp:91-93` |
| per-ω operator rebuild A(ω) | [`assemble_frequency_operator`](../L1/assemble_frequency_operator.md) | firm | `drivensolver.cpp:175-177` |
| per-ω solve | [`ksp_solve`](../L1/ksp_solve.md) | firm | `drivensolver.cpp:194, 196` |
| S-parameter reduction (output product) | `sparameter_response` *(output-product column; not authored here)* | forward-ref | `drivensolver.cpp:205-216` |

All three directly-composed L1 operators are firm ([`fe_assemble`](../L1/fe_assemble.md),
[`assemble_frequency_operator`](../L1/assemble_frequency_operator.md),
[`ksp_solve`](../L1/ksp_solve.md)). The stage-3 S-parameter reduction is the driven
output-product surface, presented as its own [`sparameters`](./sparameters.L1.md)
column — a **sibling cross-link (a reference)**, NOT a directly-owned constituent, so
it does not gate promotion (the `sparameters` column promotes independently on its own
firm reduce verb). The chapter carries the compositional claim only; per-op algebraic
claims live in the linked chapters.
