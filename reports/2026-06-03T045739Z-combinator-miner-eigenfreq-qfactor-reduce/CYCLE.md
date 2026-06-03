---
agent: combinator-miner
invoked_at: 2026-06-03T045739Z
integrated_at: 2026-06-03T055824Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-075 D3. Applied clean — NEW L4 reduction-verb chapter book/src/L4/eigenfreq_qfactor_reduce.md (status rough-in): the eigenmode per-mode (f,Q) scalar-ratio reduce-to-scalar-TABLE, the THIRD L4 reduce-shape (distinct from rank-2 gram_reduce + per-column sparameter_reduce; the c074 D6 closed-negative non-subsume honored) + L4/index.md dep-map row (alpha between dot and fe_assemble) + SUMMARY.md entry (same slot). Two repairer-corrected pinpoints (postoperator.cpp:1198-1199 / :1200-1202) landed in Evidence. No collision with D1's sparameter_reduce (different alpha slot). citecheck 29 ok / 0 fail. retroactive 0. cargo make book exit 0, linkcheck2 clean."
scope: Mine + author new L4 reduction verb — eigenfreq_qfactor_reduce (eigenmode per-mode scalar-ratio postprocess)
status: pending
---

# CYCLE: Combinator candidate — eigenfreq_qfactor_reduce

## Summary

The eigenmode postprocess stage maps the converged eigenpair set into a per-mode
`(f, Q)` table — the user-facing eigenfrequency + quality-factor output product. This is
a **per-mode SCALAR-RATIO reduction** (rank-1: one row of scalars per mode), structurally
distinct from `gram_reduce`'s rank-2 family-PAIR Gram grid (c074 D6 closed-negative on
the eigenmode-as-3rd-Gram-witness probe; OQ
`gram-reduce-third-witness-probe-eigenmode-driven-postprocess`). It is the
**reduce-to-scalar-table** member of the L4 algebra-of-folds: the eigenfrequency is the
problem-type un-transform of the eigenvalue (`f = Re ω`, `ω = √μ` linear-EVP / `ω = λ/i`
quadratic-EVP), and the quality factor is an energy/loss ratio `Q_mj = ω_m/κ_mj` with
`κ_mj = ½R_j|I_mj|²/E_m`. I propose **`eigenfreq_qfactor_reduce` as a genuine NEW L4
combinator (combinator-as-entry per the VOCABULARY-SHIFT redirect)** — the eigenmode
output-product reduction verb, the third sibling in the L4 reduce-family alongside the
reduce-to-matrix `gram_reduce` and reduce-to-scalar `inner_product`. It is forward-referenced
(by the slug `eigenfrequency-qfactor`) at `feature/eigenmode.{L4,L1,L0}.md` and the
lifecycle output-product surface — a 5+-reference convergent forward-mine flag.

It belongs at **L4** (the backend-lowering feature surface) per directive-1: it is the
output-product half of the eigenmode composition root reaching L4, the verb the backend
wants as the eigenmode driver's reported product.

## Pattern instances

This is a **same-shape single-combinator** mine (one reduction over the per-mode family),
not a parametric family — but I ran both modes (below). Instances of the per-mode
scalar-ratio reduction shape:

- **Instance 1 (per-mode eigenfrequency readout):** `eigensolver.cpp:424-439` — the
  `for (int i = 0; i < num_conv; i++)` readout loop reads `omega = eigen->GetEigenvalue(i)`
  (`:427`) then un-transforms it by problem type to the eigenfrequency: `omega =
  std::sqrt(omega)` for the linear EVP `μ = -λ² = ω²` (`:430-434`) or `omega /= 1i` for the
  quadratic EVP `λ = iω` (`:435-439`). `f = Re ω`. This is the per-mode `f` half of the table.
- **Instance 2 (per-mode quality-factor readout — resistive lumped port):**
  `postoperator.cpp:1188-1203` (`MeasureLumpedPortsEig`, def at `:1171`) computes the mode
  coupling quality factor `Q_mj = ω_m/κ_mj` from the participation κ: `κ_mj = ½R_j|I_mj|²/E_m`
  (`:1188-1191` formula comment; `:1196-1198` `resistor_power = 0.5·|R|·Re(I·conj(I))`,
  `:1198-1199` `mode_port_kappa = copysign(resistor_power/energy_electric_all, …)`,
  `:1200-1202` `quality_factor = freq_re/|mode_port_kappa|`, with the `κ=0 ⇒ Q=∞`
  guard). `freq_re = Re ω` is read at `:1177` from the same per-mode `ω` of Instance 1.
- **Instance 3 (the per-mode collect — the reduction's outer map):** `eigensolver.cpp:458`
  `post_op.MeasureAndPrintAll(i, E, B, omega, error_abs, error_bkwd, num_conv)` — the
  per-mode measure+record call inside the readout loop (loop closes `:471`,
  `MFEM_VERIFY(num_conv >= ...n)` `:472-475`). This is the `map`-collect spine: each
  converged eigenpair → one `(f, Q, …)` table row, no state threaded between modes.
- **Instance 4 (forward-mine flags — 5+ convergent references):** the eigenmode feature
  column flags this exact reduction as a not-yet-authored output-product column at
  `feature/eigenmode.L4.md:40,45,55,70`, `feature/eigenmode.L1.md:36,41,57,61`,
  `feature/eigenmode.L0.md:29,36`, and the lifecycle root at `feature/lifecycle.L4.md:44`,
  `feature/lifecycle.L1.md:41`, `feature/lifecycle.L0.md:40,45`. ≥2 converging references
  → the stub-creation / authoring bar is clearly met (CLAUDE.md "Integration may
  materialize implied components").

(≥3 instances cleanly met; the forward-mine flags are the convergent demand signal.)

## Proposed combinator

- **Slug**: `eigenfreq_qfactor_reduce`
- **Layer**: **L4** (with rationale: the eigenmode output-product reduction is the
  feature-surface verb the backend wants — directive-1, L4 is the outward backend-lowering
  target; the output-product half of the eigenmode composition root
  (`feature/eigenmode.L4.md:40`) reaches the L4 surface through it. NOT L3/L2/L1: the
  reduction is a pure per-mode `map`+scalar-ratio with no iteration-rotation content (the
  only loop is the post-processing readout map, explicitly NOT a solve-iteration —
  `book/src/L4/solve_family.md:146`), so it lowers identity-in-form to its L1 scalar-map
  primitives, the `inner_product`/`gram_reduce` in-line-marker route; no intervening L2/L3
  reshape. It is the reduce-family sibling that lives where `gram_reduce`/`inner_product`
  live: L4.)

- **Signature sketch** (best guess; harvester firms up):

      -- the eigenmode per-mode scalar-ratio reduction over the converged eigenpair set,
      -- mapping each mode to its (eigenfrequency, quality-factor) table row.
      eigenfreq_qfactor_reduce :: ProblemType                 -- selects the eigenvalue→ω un-transform
                               -> (Mode -> Scalar)            -- the per-mode loss-rate κ_m (energy/loss ratio)
                               -> [Eigenpair]                 -- the converged eigenpair family [(λ_i, E_i)]
                               -> [(Scalar, Scalar)]          -- per mode: (f_m = Re ω_m, Q_m = ω_m / κ_m)
      eigenfreq_qfactor_reduce ptype kappa eigs =
        [ let omega = untransform ptype lambda             -- ω = √μ (linear) | λ/i (quadratic)
              f     = re omega                             -- eigenfrequency f_m = Re ω_m
              k     = kappa mode                           -- loss rate κ_m  (= ½R|I|²/E_m, the participation)
              q     = if k == 0 then infinity else f / abs k  -- quality factor Q_m = ω_m / κ_m
          in  (f, q)
        | (lambda, _E) <- eigs, let mode = ... ]
        where
          untransform Linear    mu  = sqrt mu              -- μ = -λ² = ω²
          untransform Quadratic lam = lam / i              -- λ = iω

  (The `κ_m` loss-rate is itself a small inner reduction — `½R·|I_mj|²/E_m` — a weighted
  ratio of a port-current self-energy `½R|I|²` to the mode total energy `E_m`; the harvester
  decides whether to thread it as a closure parameter (above) or inline it. The mode-field
  `E_i` and `B = -1/(iω)∇×E` recovery is the eigenmode feature column's stage-3 readout, NOT
  part of THIS reduction — the reduction is the `(f, Q)` scalar table specifically.)

- **Algebraic intuition**:
  - **Map-independence (the defining fold law).** Each table row depends only on its own
    mode's `(λ_i, κ_i)`; no state threads between modes (`eigensolver.cpp:424` readout loop
    carries no inter-mode accumulator). The reduction is a list homomorphism over the
    eigenpair family: `eigenfreq_qfactor_reduce p k (a ++ b) = eigenfreq_qfactor_reduce p k a
    ++ eigenfreq_qfactor_reduce p k b` (the concatenation-homomorphism the `solve_family` /
    `gram_reduce`-grid maps share — embarrassingly parallel over modes).
  - **Un-transform is a pure scalar map** parameterized by `ProblemType` (the variant axis
    absorbed): `f = Re(untransform ptype λ)`. Not associative/commutative across modes
    (it is a per-element map, no cross-mode combine).
  - **Q is a ratio, not a bilinear** — `Q_m = ω_m/κ_m` is reduce-to-SCALAR per mode (the
    `f/|κ|` quotient), NOT a reduce-to-matrix family-pair bilinear. This is the load-bearing
    distinction from `gram_reduce` (rank-1 scalar-ratio table vs rank-2 symmetric Gram grid)
    — there is no `symmetric_from_upper`, no family-PAIR `xⱼᵀ K xᵢ`.
  - **κ=0 ⇒ Q=∞ guard** (`postoperator.cpp:1201-1202`, `mfem::infinity()`) — a total
    (lossless-mode) edge case the reduction handles in the scalar map, not an error arm.

- **Variant axes**:
  - **problem-type** (`linear-EVP | quadratic-EVP | nonlinear-EVP`) — selects the
    eigenvalue→ω un-transform (`√μ` vs `λ/i`); absorbed into the `untransform` dispatch
    (`eigensolver.cpp:430-439`). The load-bearing axis.
  - **loss-source** (`resistive-lumped-port` witnessed; inductive-EPR is the participation
    sibling) — selects what feeds κ_m. Currently the resistive-lumped-port κ is the witnessed
    Q-source (`postoperator.cpp:1188-1203`); the inductive-port branch (`:1215-1219`) is the
    participation-ratio sibling, not a Q. Absorbed into the `κ_m` closure.
  - **element-type** (complex eigenvalue/eigenvector — pinned; eigenmodes are intrinsically
    complex). `f = Re ω`, `Q` from `|κ|`.

## Proposed changes

### 1. Dep-map row in `book/src/L4/index.md` (Data-algebra combinators & named verbs group; alpha position between `dot` and `fe_assemble`)

`eigenfreq_qfactor_reduce` sorts alphabetically after `dot` and before `fe_assemble`.
Anchor the insert TIGHTLY on the `fe_assemble` row start (my alpha-neighbor) so it does not
collide with D1's edit (see coordination note below):

```edit:book/src/L4/index.md
| [`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md) | `eigenfreq_qfactor_reduce :: ProblemType -> (Mode -> Scalar) -> [Eigenpair] -> [(Scalar, Scalar)]`; per mode `(f_m, Q_m)` where `f_m = Re ω_m` (the problem-type un-transform of the eigenvalue — `ω = √μ` linear-EVP / `ω = λ/i` quadratic-EVP) and `Q_m = ω_m / κ_m` (energy/loss ratio, `κ_m = ½R|I_mj|²/E_m`, `κ=0 ⇒ Q=∞`). The eigenmode **per-mode scalar-ratio reduction combinator** — the **reduce-to-scalar-table** member of the L4 algebra-of-folds (sibling of reduce-to-matrix [`gram_reduce`](./gram_reduce.md) + reduce-to-scalar [`inner_product`](./inner_product.md)). Rank-1 per-mode table, NOT a `gram_reduce` family-PAIR grid (c074 D6 closed-negative). Pure value-producing reduction — no `Solve` monad / carry / predicate (the per-mode readout map, explicitly NOT a solve-iteration). | Consumes: the converged eigenpair family from [`eigsolve`](./eigsolve.md) (the eigenmode composition root's stage-2 output). Concepts: `black-box-vs-accelerated-kernels` (§"the combinators rise regardless"). Sibling combinators: [`gram_reduce`](./gram_reduce.md), [`inner_product`](./inner_product.md). | L1 the per-mode scalar maps (the eigenvalue un-transform + the κ participation ratio + the `f/κ` quotient) by **identity-in-form on the body** (the reduction is a plain per-mode `map` of scalar evaluations; **no dedicated L4>L3 theme** — the in-line-marker route; the substantive downward content is the un-transform branch + the κ computation in the eigenmode driver / postoperator L0). | `rough-in` (harvested cycle-075 D3 from the eigenmode feature-column forward-mine flags `feature/eigenmode.L4.md:40` + the lifecycle output-product surface; structure read off the 2 positive readout sites eigenvalue-un-transform `eigensolver.cpp:424-439` + Q-factor `postoperator.cpp:1188-1203`; rough-in not firm because the per-mode κ participation primitive + un-transform are not yet firm L1 entries and there is no dedicated eigenmode-postprocess test. Genuine NEW spine vocabulary — the eigenmode output-product reduction verb, NOT a `gram_reduce` specialization, c074 D6 closed-negative) |
| [`fe_assemble`](./fe_assemble.md) | `fe_assemble :: FiniteElementSpace[N] -> [WeakFormTerm] -> LinearOperator[N, N]`;
```

(The `old_string` for the integrator's surgical Edit is anchored on the literal
`| [`fe_assemble`](./fe_assemble.md) | `fe_assemble :: FiniteElementSpace[N] -> [WeakFormTerm] -> LinearOperator[N, N]`;`
line start — the new row is prepended immediately before it. This anchor touches ONLY the
`fe_assemble` row prefix, so it does not collide with D1's row insert at a different alpha
position.)

### 2. SUMMARY.md insertion (L4 sub-list, Data-algebra group; alpha between `dot` and `fe_assemble`)

Insert a new bullet between `  - [dot](./L4/dot.md)` (line 42) and
`  - [fe_assemble](./L4/fe_assemble.md)` (line 43):

```edit:book/src/SUMMARY.md
  - [eigenfreq_qfactor_reduce](./L4/eigenfreq_qfactor_reduce.md)
```

Anchor TIGHTLY on the `fe_assemble` SUMMARY line (`  - [fe_assemble](./L4/fe_assemble.md)`)
— prepend the new bullet immediately before it. This is the same alpha-neighbor anchor
discipline as the dep-map row (avoids collision with D1's SUMMARY insert).

### 3. New chapter file (authored by THIS report — combinator-miner authored at dispatch per scope)

Per the dispatch scope ("mine + author the new L4 reduction verb
`book/src/L4/eigenfreq_qfactor_reduce.md`"), the full chapter body is supplied below as a
proposed-changes block for the integrator to materialize (the chapter file does not yet
exist — it is a `create`, not an `edit`). House style = `gram_reduce.md` / `fold_solve.md`.

```create:book/src/L4/eigenfreq_qfactor_reduce.md
---
layer: L4
operator: eigenfreq_qfactor_reduce
firmness: rough-in
consumes:
  - book/src/L4/eigsolve.md (firm — the opaque eigen-solve cap producing the converged eigenpair family this reduction maps over; the upstream composition-root stage)
lowers_to:
  - the per-mode scalar maps (eigenvalue un-transform + κ participation ratio + f/κ quotient); identity-in-form on the body, no dedicated L4>L3 theme — in-line §"Lowers to"
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
eigenmode driver / postoperator L0 and the (rough-in) L1 scalar-map primitives. This entry
records the rotation direction in-line per high→low discipline; it does not author a theme.

## Status

`rough-in`. **Reasoning (warrant-first):** the combinator's **structure** is read directly
off the two positive readout sites — the eigenvalue→ω un-transform (`eigensolver.cpp:424-439`)
and the Q-factor body (`postoperator.cpp:1188-1203`) — and the map laws (§Algebraic laws)
are syntactic identities on that per-mode map. So the *structure* approaches the
firm-on-positive-structure escape. But two factors gate it to `rough-in`:
1. the per-mode building blocks it folds — the κ participation ratio (`½R|I|²/E`) and the
   eigenvalue un-transform — are **not yet firm L1 entries** (no `L1/eigenfreq_qfactor_reduce`
   or κ-participation primitive exists; the reduction is distilled directly from the driver
   + postoperator bodies), so the entry cannot inherit firm primitive maturity;
2. there is **no dedicated Palace unit test** for the eigenmode postprocess Q-factor /
   eigenfrequency readout (the `MeasureLumpedPortsEig` body + the readout loop are
   integration-level, exercised only through the full eigenmode `Solve(mesh)` driver), so
   the reduction-level laws are test-unconfirmed.

Promotion route: (a) firm up the folded per-mode primitives (a κ-participation L1 entry +
the eigenvalue-un-transform primitive), AND (b) a dedicated eigenmode-postprocess test OR a
lowering-verifier pass raising the map-law confidence to `inner_product`-equivalent.
(Contrast the rank-2 sibling [`gram_reduce`](./gram_reduce.md), also `rough-in
(test-coverage-bounded)` for the same primitive-maturity + no-test reasons.)

**Scope: 1-of-1 — the eigenmode pipeline's output product.** This is the eigenmode driver's
OWN output-product reduction; it is not a cross-pipeline shared verb (the other four
pipelines have different output products: capacitance/inductance via
[`gram_reduce`](./gram_reduce.md), driven S-parameters via their own per-column projection,
transient via the field/energy time-history). The disciplined-cross-pipeline-mining-gate
does not apply — this is a single-pipeline output-product verb by design (like
[`frequency_sweep`](./frequency_sweep.md)'s single-witness-driven-by-design scope).

## Evidence

All L0 citations self-verified on-disk this dispatch via the codemap
(`mcp__palace-codemap__read_range` + `search_text` line pinpoints against
`reference/palace/`).

- **Eigenfrequency un-transform (positive site 1):** `palace/drivers/eigensolver.cpp:424`
  (the `for (int i = 0; i < num_conv; i++)` readout loop start), `:427`
  (`std::complex<double> omega = eigen->GetEigenvalue(i)`), `:430-434` (`omega =
  std::sqrt(omega)` — linear EVP `μ = -λ² = ω²`), `:435-439` (`omega /= 1i` — quadratic EVP
  `λ = iω`), `:458` (`post_op.MeasureAndPrintAll(i, E, B, omega, …)` — the per-mode
  measure+record), `:471` (loop close), `:472-475` (`MFEM_VERIFY(num_conv >= …n)`).
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
```

## Coordination with D1

D1 (running in parallel) ALSO adds a row to `book/src/L4/index.md` and a `SUMMARY.md` entry.
Both my edits are anchored TIGHTLY on my alpha-neighbor `fe_assemble` ONLY (the dep-map row
prepended before the literal `fe_assemble` row line; the SUMMARY bullet prepended before the
literal `  - [fe_assemble](./L4/fe_assemble.md)` line). As long as D1's row/entry is at a
DIFFERENT alpha position (a different anchor), the two surgical Edits do not collide; the
integrator applies them serially with a re-read between. If D1's slug ALSO sorts adjacent to
`fe_assemble` (unlikely — flag for the integrator to sequence and re-verify alpha order
after both apply). The integrator sequences both per the per-report serial discipline.

## Supporting evidence

(See the chapter body §Evidence above for the full citation list — all self-verified
on-disk via the codemap this dispatch.) Key anchors:
- `palace/drivers/eigensolver.cpp:424-439` (eigenvalue→ω un-transform), `:458,471-475`.
- `palace/models/postoperator.cpp:1171-1172,1177,1188-1203,1215-1221` (Q-factor / κ body).
- Forward-mine flags: `feature/eigenmode.{L4,L1,L0}.md`, `feature/lifecycle.{L4,L1,L0}.md`.
- Non-subsume precedent: `book/src/L4/gram_reduce.md:178-189` (c074 D6 closed-negative).
- No `test/unit/` test for the eigenmode postprocess Q/eigenfrequency readout.

## Open questions / caveats

- **κ-participation primitive not yet a firm L1 entry.** The loss rate `κₘ = ½R|I|²/E` (the
  mode coupling participation, `postoperator.cpp:1188-1203`) is folded as a closure
  parameter in this reduction but has no standalone L1 home yet. It is itself a small inner
  weighted-energy ratio (port self-energy / mode total energy) — a candidate future L1 (or
  L2) primitive. Filing this as a promotion-gate note, not a blocking issue (the reduction
  is `rough-in` precisely because its primitives are not firm). Recommend the harvester /
  cycle-planner consider a `participation-ratio` L1 primitive as the firming route — it
  would also serve the surface-dielectric participation Q at `postoperator.cpp:1346-1373`
  (a sibling participation/Q computation, the SAME `p/δ` energy-ratio shape) and the
  inductive-EPR branch (`:1215-1219`). NOT proposed as a rough-in row here (one pattern per
  invocation; this is a noted future primitive).
- **Run-mode check (parametric-family mode):** I ran parametric-family mode on this scan.
  The eigenmode Q-factor is NOT a parametric family with the capacitance/inductance Gram
  (c074 D6 closed-negative — different rank/result-type, the over-unification guard
  correctly refuses the merge). It is also NOT a fold family with `inner_product` (it is a
  per-mode map, not a reduce-across-the-length-axis). So same-shape single-combinator is the
  correct reportable class. The κ participation ratio + the surface-dielectric participation
  Q + the inductive EPR ARE a candidate participation-ratio sub-family (all `½X|I|²/E` or
  `p/δ` energy-ratio shapes) — but that is the FUTURE L1 primitive noted above, a separate
  pattern, not this dispatch's combinator.
- **Mode-field readout out of scope.** This reduction is the `(f, Q)` SCALAR table only; the
  per-mode field recovery (`Eᵢ`, `B = -1/(iω)∇×E`) is the eigenmode column's stage-3 field
  readout (`eigensolver.cpp:443-455`), a distinct reduction (or a no-reduce pass-through) —
  not folded here. The harvester should keep the field readout out of
  `eigenfreq_qfactor_reduce`'s signature.
