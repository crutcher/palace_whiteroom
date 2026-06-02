---
agent: harvester
invoked_at: 2026-06-02T205715Z
scope: L4 operator: assemble_frequency_operator
status: integrated
integrated_at: 2026-06-02T222500Z
integration_commit: PLACEHOLDER_SHA_CYCLE069
integration_notes: |
  Applied by integrator-per-report (staging row D1, applied_at 2026-06-02T211730Z); finalized by integrator-finalize cycle-069.
  assemble_frequency_operator PROMOTED FIRM L4 (the driven per-ω system-operator weighted-sum assembly A(ω)=K+iωC−ω²M, the operator-operand specialization of L4/linear_combination; the rank-2 FE-cohort→L4 lift; opens the DRIVEN assemble-half at L4, directive-1). New book/src/L4/assemble_frequency_operator.md + own L4/index dep-map row+cohort bullet (alpha, before krylov-step) + SUMMARY L4 alpha-insert (NOT the firm tally — D2 sole count-owner). L4 firm 10→13 (with D2's dot+nrm2). Build-relevant: cargo make book exit 0; page renders; D2's tally link to this entry resolves (D1 landed first). 2 OQs promoted. Zero gate hits.
inputs:
  - book/src/L1/assemble_frequency_operator.md (the firm L1 source — firm-on-positive-structure, cycle-062 D3; the warrant analysis + single-pipeline-by-design framing + operator-operand-corner framing already done here)
  - book/src/L4/linear_combination.md (the firm L4 combinator this entry re-expresses THROUGH — operand-category variant axis carries the operator-operand corner, names assemble_frequency_operator as next-pull consumer at :40, :198-204)
  - book/src/L4/fe_assemble.md (the cycle-068 D1 precedent firm L4 FE-cohort lift — combinator-as-entry + black-box-input + state-stratification shape, the structural sibling for this dispatch)
  - book/src/concepts/black-box-vs-accelerated-kernels.md (the three-way disposition; §"The combinators rise regardless" :128-136 — linear_combination rises to L4 regardless as a feature-surface verb)
  - skills/disciplined-cross-pipeline-combinator-mining-gate/SKILL.md (the single-pipeline-by-design specialization framing — no 2nd-pipeline discharge owed)
  - book/src/design/l4_calculus.md (the L4 strawman — notation conventions)
  - reports/2026-06-02T205156Z-cycle-planner-cycle-069/CYCLE.md §D1 (dispatch scope)
---

# CYCLE: Formalize assemble_frequency_operator at L4

## Summary

This dispatch (cycle-069 D1) lifts the firm L1 `assemble_frequency_operator` (the driven/frequency-domain pipeline's per-ω system-operator assembly `A(ω) = K + iω·C − ω²·M + A2(ω)`, firm-on-positive-structure cycle-062) to L4 as a **genuine firm L4 entry** re-expressing **through** `L4/linear_combination`'s operator-operand corner — the driven pipeline's **ASSEMBLE half** reaching the L4 feature surface (directive-1: L4 is the outward backend-lowering target). The slug is ABSENT at L4 (`ls book/src/L4/` confirmed — no `assemble_frequency_operator.md`). The L4 form is the **operator-operand specialization** of the firm L4 `linear_combination` combinator (cycle-068 D3) at the `affine-in-ω scalar weights` corner: `assemble_frequency_operator fam omega = linear_combination [(1, K), (iω, C), (−ω², M), (1, A2 ω)]` with the operand monoid being operator-addition (the L0 `BuildParSumOperator` / `SumOperator::AddOperator` fold, `rap.cpp:766-787`, on-disk-confirmed this dispatch). It does NOT re-derive the combination algebra — every law is `linear_combination`'s law read at the operator-operand corner (replace-and-propagate). It carries L4 the L1 cap's two non-gating caveats (affine-modulo-`A2`; single-pipeline-by-design — no 2nd-pipeline discharge owed per the `disciplined-cross-pipeline-combinator-mining-gate`). Status `firm` (firm-on-positive-structure escape — every law a syntactic operator-algebra identity carried up from the firm L4 combinator + the firm L1 cap, the `fe_assemble`/`linear_combination` precedent). It DEFERS the consolidated `L4/index` firm tally + frontier prose to D2 (this cycle's sole count-owner); it registers its OWN dep-map row + §Vocabulary-cohort bullet (alpha position) + SUMMARY insert (alpha position).

## Warrant verdict

**GENUINE L4 ENTRY** (both dispositions were VALID per the warrant-first mandate; this is the verdict and its grounds):

- The firm L1 cap (`L1/assemble_frequency_operator.md:69`) already records the analogous L1 warrant: `assemble_frequency_operator` "is a useful named entry because the driven pipeline's per-ω rebuild is the `map_solve` scope boundary and deserves a navigable [L1] home; it is NOT a separate fold algebra." The same logic lifts cleanly to L4: it is the **driven backend's per-ω assemble verb** — the named operator-operand specialization the backend wants to call to build the per-frequency system operator before driving the per-ω solve. A reader navigating L4 for "how does the driven pipeline assemble its system operator" should find a navigable L4 home, not have to reconstruct it from `L4/linear_combination`'s §Specializations.
- `L4/linear_combination.md:198-204` already names this entry as **"the next-pull L4 consumer that rides `linear_combination` rising"** and `:40` records the c069-gated forward-reference — the cycle-068 planner sequenced it as a separate landing precisely because it is the driven pipeline's distinct assemble verb, GATED on the combinator existing on disk. The combinator now exists; the gate cleared.
- It is the **driven pipeline's ASSEMBLE half** at the feature surface — the assemble-half completeness work the FE-cohort-l4-lift plan-tag tracks (parallel to `L4/fe_assemble` being the shared FE assemble verb; this is the driven-specific per-ω operator-fold assemble verb). The assemble half reaching L4 is in-scope directive work.

**The rejected disposition (thin note under `L4/linear_combination` §Specializations) was VALID-but-not-chosen:** the body IS just `linear_combination` at the operator-operand arity-4 corner, so a §Specializations note would not be wrong. It is rejected because (a) the L1 layer already gave it a navigable standalone home on the same warrant (layer-coherence: L4 should match), (b) it is the named `map_solve` scope boundary the driven solve half references — a distinct navigable verb, not just a fold instance, and (c) `L4/linear_combination`'s §"Arity specializations" is already reserved for the *tensor-operand* BLAS-1 leaves (`scal`/`axpy`/`axpby`/`axpbypcz`); folding a driven-pipeline operator-operand specialization into that same notes-section would conflate the operand-category corners. The entry re-expresses THROUGH the combinator (does not re-derive it), so it is replace-and-propagate-compliant either way.

## Proposed changes

```new:book/src/L4/assemble_frequency_operator.md
---
layer: L4
operator: assemble_frequency_operator
firmness: firm
consumes:
  - book/src/L4/linear_combination.md (the firm L4 scalar-weighted-sum combinator this entry is the OPERATOR-OPERAND specialization of — re-expressed THROUGH its operand-category variant axis at the operator-operand corner; NOT a mirrored operator_linear_combination fold; replace-and-propagate)
  - book/src/concepts/black-box-vs-accelerated-kernels.md (§"The combinators rise regardless" — linear_combination rises to L4 regardless as a feature-surface verb; this driven specialization rides that rise)
  - book/src/L1/assemble_frequency_operator.md (the firm L1 source — the warrant + the affine-modulo-A2 + single-pipeline-by-design caveats + the positive L0 structure are read off it; this is the upward in-layer rendering of that firm cap)
lowers_to:
  - book/src/L1/assemble_frequency_operator.md (DOWNWARD: identity-in-form on the body — the L4 operator-operand linear_combination specialization is value-thread-isomorphic to the firm L1 affine-operator-family form; NO dedicated L4>L3 / L4>L1 theme file, in-line §"Downward to L1" — the transitive consequence of L4/linear_combination's in-line L4>L3 identity composed with the L1 cap's L1>L0 rotation; the non-adjacent-identity in-line-marker convention)
variant_axes:
  - operand-category (operator-operand corner — this entry IS the operator-operand specialization of linear_combination; the axis is carried on linear_combination, not re-declared here)
  - weight-schedule (affine-in-parameter — the {1, iω, −ω²} schedule over the swept ω; the constant single-shot operator sum would be the other corner)
  - operand-stationarity (fixed-basis {K, C, M} | parameter-dependent-operand A2 — the "affine modulo A2" caveat)
---

# assemble_frequency_operator

The L4 **driven per-ω system-operator assembly verb**: given a fixed operator
basis and a frequency ω, produce the affine-in-ω operator combination
`A(ω) = K + iω·C − ω²·M + A2(ω)`. It is the **operator-operand specialization**
of the firm L4 [`linear_combination`](./linear_combination.md) combinator at the
`affine-in-ω scalar weights` corner — a scalar-weighted sum of fixed operators,
the operator-domain image of the tensor-domain BLAS-1 linear-combination cohort.
It re-expresses **through** `linear_combination`'s **operand-category** variant
axis (`tensor-operand | operator-operand`; the operator-operand corner,
`L4/linear_combination.md:196-204`); it is **not** a new fold algebra
(replace-and-propagate, 2026-06-01 anti-mirror discipline). This is the driven
(frequency-domain) pipeline's **assemble half** reaching the L4 feature surface
(directive-1: L4 is the outward backend-lowering target — the per-ω system
operator the driven sweep wants named as a backend verb).

## Context

L4 is **vocabulary, not architecture** (`L4/index.md:7-13`): it names *what
operations happen* with their signatures and shape contracts, and is the
**backend-lowering target** — the feature surface whose semantics match the
external GPU-tensor backend. `assemble_frequency_operator` is the driven
pipeline's per-frequency operator-construction verb: inside the driven frequency
sweep, the system operator `A(ω)` is rebuilt at every ω from the once-assembled
fixed basis and the swept frequency, then handed to the per-ω Krylov solve. The
L4 form names that rebuild as a feature-surface verb so the driven feature
(assemble-half) reaches L4 written against the backend's verb set.

`assemble_frequency_operator` is **not** an iteration-structural combinator like
[`iterate-while`](./iterate-while.md) / [`fold_solve`](./fold_solve.md): it
threads no `SimState` carry, has no stopping predicate, no monadic `Solve`
effect. It is a **pure value-producing combination** — the same data-algebra half
of the L4 vocabulary its parent [`linear_combination`](./linear_combination.md)
occupies, specialized to operator operands and an affine-in-ω scalar schedule.
It is the **assemble-half companion** to the iteration-structural driven *solve*
half: the per-ω operator this verb assembles is the operand the driven solve loop
inverts. (The driven solve half is **not** this dispatch's concern — the per-ω
`SetOperators`-inside-the-loop that scopes driven out of the shared
[`solve_family`](./solve_family.md) is the `map_solve` boundary recorded at
`L4/solve_family.md`; whether driven's *solve* half rises to L4 is a separate
methodology decision. This entry is the assemble verb only.)

### Relationship to linear_combination (replace-and-propagate)

`assemble_frequency_operator` introduces **no second scalar-weighted-sum fold**.
The firm L4 [`linear_combination`](./linear_combination.md) is the variadic fold
`Σᵢ aᵢ·tᵢ` over a `[(Scalar, Operand)]` list; its operand monoid is **parametric**
(`L4/linear_combination.md:196-198`), and the **operand-category** variant axis
carries both the tensor-operand corner (the BLAS-1 cohort) and the
**operator-operand** corner. The driven assembly is the *same fold* at the
operator-operand corner: the operands are the FE-assembled operators
`{K, C, M, A2}` (`LinearOperator[N, N]` values), the operand monoid is
operator-addition with scalar-operator scaling (realized at L0 by
`SumOperator::AddOperator`), and the scalar weights are the affine-in-ω schedule
`{1, iω, −ω²}` (plus coeff `1` on `A2`). Per the 2026-06-01 vocabulary-shift
redirect this is handled by the existing combinator's operand-category axis — NOT
by authoring a mirrored `operator_linear_combination` chapter.
`assemble_frequency_operator` is then the **driven-pipeline specialization** of
that operator-operand corner: the fixed three-operator basis `{K, C, M}` under
the affine-in-ω scalar weights, plus the extra term `A2`. Every algebraic law
below is `linear_combination`'s law read at this corner — it does **not**
re-derive the fold.

## Semantics (overlay)

The L4 calculus is specified in the strawman
[`../design/l4_calculus.md`](../design/l4_calculus.md).
`assemble_frequency_operator` is a pure term-list fold (its parent
`linear_combination`'s fold) specialized to a fixed four-term operator-operand
list with affine-in-ω scalar weights; its L4 rendering uses the strawman's
term/type BNF (§1) with **no reduction-rule extension** — it adds no new
evaluation rule beyond `linear_combination`'s existing `foldl`/`+`/`scal` (the
`scal`/`+` here being scalar-operator scaling / operator addition rather than the
tensor versions, the operand-category corner). Pseudo-language is Haskell `::`
signatures inside a `text` fence per the L4/L3 notation invariant.

## Signature

    -- the driven per-ω system-operator assembly verb:
    -- the operator-operand specialization of linear_combination at the affine-in-ω corner
    assemble_frequency_operator
      :: FrequencyOperatorFamily[N] -> Scalar -> LinearOperator[N, N]

    -- the once-assembled fixed-basis family (the readonly construction stratum):
    type FrequencyOperatorFamily[N] =
      { K  : LinearOperator[N, N]            -- stiffness (curl-curl), assembled once
      , C  : LinearOperator[N, N]            -- damping (impedance/conductivity), assembled once
      , M  : LinearOperator[N, N]            -- mass (permittivity), assembled once
      , A2 : Scalar -> LinearOperator[N, N]  -- frequency-dependent extra term (closure over ω)
      }

    -- the body IS linear_combination at the operator-operand corner (arity-4 instance):
    assemble_frequency_operator fam omega =
      linear_combination                     -- operator-operand corner (operand monoid = operator-+)
        [ (1,          fam.K)
        , (1i * omega, fam.C)
        , (-(omega^2), fam.M)
        , (1,          fam.A2 omega)
        ]

Shape contract (bunsen-style; named axes; the construction stratum is the fixed
basis captured once outside the sweep):

- `fam.K`, `fam.C`, `fam.M` — `LinearOperator[N, N]` — **shape precondition**: all
  share one square axis `N` (the global FE-space true-dof dimension); assembled
  ONCE before the frequency sweep (the L4 typing of the once-built fixed basis).
  Operand-stationarity = `fixed-basis`. (The L0 `BuildParSumOperator` enforces the
  shared-space precondition directly: `MFEM_VERIFY(... same FiniteElementSpace)`,
  `rap.cpp:774-777`.)
- `fam.A2` — `Scalar -> LinearOperator[N, N]` — the frequency-dependent extra term,
  applied at the swept `omega`. Operand-stationarity =
  `parameter-dependent-operand` (the lone non-fixed operand carrying constant
  coeff `1`; the "affine modulo A2" caveat).
- `omega` — `Scalar` — the (real) sweep frequency; the affine-weight parameter.
  The scalar weights `{1, iω, −ω²}` are the affine-in-ω schedule
  (weight-schedule = `affine-in-parameter`). Element-type is fixed `complex` for
  this driven specialization (the weights `iω`, `−ω²` are complex; the general
  `real | complex` element-type axis of `linear_combination` collapses to
  complex-only here, a scope-out, not a remaining axis).
- result — `LinearOperator[N, N]` — the combined operator `A(ω)`, square on the
  same axis `N`; itself a `LinearOperator` the per-ω inner solve applies (the
  apply/assemble duality, law 6).

The L4 calculus has **no monadic effect** on this verb (contrast the
`Solve`-threaded iteration combinators): `assemble_frequency_operator` is a plain
value-producing combination, threaded as a `let`-binding inside the driven solve
loop's body that consumes it. The discipline that the fixed basis flows in only
is structural (the `FrequencyOperatorFamily[N]` record is the captured-once input;
the single return slot is `LinearOperator[N, N]`).

### Through linear_combination (the operator-operand corner)

The body is exactly `linear_combination` at the **operator-operand** corner of
its operand-category variant axis, at term-list length 4:

    assemble_frequency_operator fam omega
      = linear_combination [ (1, fam.K), (1i*omega, fam.C), (-(omega^2), fam.M), (1, fam.A2 omega) ]

This is the arity-4 instance of the firm fold, with the operand monoid being
operator-addition / scalar-operator-scaling rather than tensor-addition. The
four-term list is the literal L0 argument shape
`BuildParSumOperator({a0, a1, a2, 1}, {K, C, M, A2})`. All of
`linear_combination`'s seven algebraic laws hold here by the operand-category
extension (operator addition is a commutative monoid with identity the zero
operator `0[N,N]`; scalar-operator scaling distributes over operator addition and
over scalar addition) — see §"Algebraic laws". Naming note:
`assemble_frequency_operator` is the **driven specialization label** (one ω → one
summed operator), the operator-domain sibling of `axpbypcz` as the arity-3
*tensor* readout label; it earns a navigable L4 home because it is the driven
assemble verb / the named `map_solve` scope boundary, NOT because it is a separate
fold algebra.

## Algebraic laws

The laws are `linear_combination`'s laws (`L4/linear_combination.md:128-183`) read
at the operator-operand corner (operator addition `+` is a commutative monoid with
identity the zero operator `0[N,N]`; scalar-operator scaling distributes). They
hold; absences are deliberate. Reproduced for L4 layer-coherence (an L4 reader
verifies them against this signature without reaching down).

1. **Reduces to the operator-operand `linear_combination` (the defining identity).**
   `assemble_frequency_operator fam omega = linear_combination [(1, K), (iω, C), (−ω², M), (1, A2(ω))]`
   — the arity-4 operator-operand instance of the firm fold. Every law below is
   that fold's law specialized to this fixed term list.

2. **Affine-in-ω over the fixed basis (the family law).** Holding `{K, C, M}`
   fixed and treating `A2` as a separate additive term,
   `A(ω) − A2(ω) = K + iω·C − ω²·M` is a degree-≤2 polynomial-in-ω with operator
   coefficients: the ω-derivative `d/dω (A − A2) = i·C − 2ω·M` is itself a
   fixed-basis operator combination. This is what makes the per-ω rebuild a
   *family* rather than independent assemblies — the structural payoff that licenses
   capturing `{K, C, M}` once. **Modulo `A2`**: with `A2`'s ω-dependence included,
   the polynomial-in-ω structure holds only for the `{K, C, M}` part.

3. **Operator-multilinearity in the weights.** `A` is linear separately in each
   scalar weight with the operands held fixed: scaling the C-weight by κ scales
   `C`'s contribution by κ. This is `linear_combination`'s multilinearity
   (`L4/linear_combination.md` law 3) at the operator-operand corner.

4. **Zero-coefficient term-drop.** A term whose scalar weight is zero drops from
   the sum: at `ω = 0` the C-weight `iω = 0` and the M-weight `−ω² = 0`, so
   `A(0) = K + A2(0)`. This is `linear_combination`'s zero-coefficient term-drop
   (`L4/linear_combination.md` law 5) at the operator-operand corner, and it is
   the **exact algebraic content of the L0 `coeff[i] != 0` sparsity prune** that
   `BuildParSumOperator` performs (it skips zero-coefficient operands) — positively
   anchored in the operator domain (`L1/assemble_frequency_operator.md:99`,
   `rap.cpp` fold body), not merely inherited.

5. **Empty/seed identity (the fold seed).** The operator-operand
   `linear_combination` over the empty list is the zero operator `0[N,N]`
   (`linear_combination` law 1); the L0 `BuildParSumOperator` requires at least one
   non-null operand (`MFEM_VERIFY(it != ops.end())`), so the empty case is the
   fold's seed, not a runtime path Palace exercises (the driven call always
   supplies the non-null `K`). A calculus-level total-definition convenience, the
   `fe_assemble`-empty-term flavor.

6. **Result is a `LinearOperator` (apply/assemble duality).** `A(ω)` is itself a
   `LinearOperator[N, N]`; its action distributes over the basis,
   `A(ω)·v = K·v + iω·(C·v) − ω²·(M·v) + A2(ω)·v` (the `SumOperator` weighted-sum
   action). The assembled sum's action is the weighted sum of the basis actions —
   the operator-operand reading of `linear_combination`'s concatenation-homomorphism
   (`L4/linear_combination.md` law 2): the per-term contributions add, evaluated at
   `v`.

Laws that explicitly **do not** hold:

- **Affine-in-ω as a whole (paired non-law).** `A(ω)` is NOT globally affine
  (degree-1) in ω: the M-weight `−ω²` makes it degree-≤2 over the fixed basis, and
  `A2(ω)` is an unknown-degree ω-dependent operand. The honest characterization is
  "fixed-basis polynomial-in-ω (degree ≤ 2) plus the `A2` correction"; the "affine
  operator family" phrasing refers to the fixed-basis-with-scalar-weights structure,
  not literal degree-1. (Carried from `L1/assemble_frequency_operator.md:107`.)
- **Operand-permutation bit-identity (IEEE residue).** The operator-domain sum
  order (the `SumOperator::AddOperator` accumulation order) is a load-bearing
  reduction-order concern exactly as for the tensor fold; bit-reproduction of a
  given L0 assembly requires matching the accumulation order. At L4 the *operator*
  value is order-agnostic (operator addition is commutative); the pinned order is a
  below-L4 lowering concern — the same disposition `linear_combination` uses for its
  IEEE non-law (`L4/linear_combination.md:166-179`), deferred to the lowering chain,
  NOT restated as an L4 law.

The L4 law set is **identical** to `linear_combination`'s set read at the
operator-operand corner — structural, because the rotation through the combinator
is identity-in-form on the value and the operand-category extension is a monoid
swap (tensor-`+` → operator-`+`) that preserves every law.

## Variant axes

The variant axes are the operand-category corner + two driven specializers (the
general `linear_combination` axes — arity, output-aliasing, element-type — are
carried on the combinator; the driven specialization pins them):

1. **Operand-category** (`operator-operand` corner) — this entry IS the
   operator-operand specialization of `linear_combination`; the axis is carried on
   the combinator (`L4/linear_combination.md:196-204`), not re-declared here. The
   BLAS-1 cohort is the tensor-operand corner; this is its operator-domain sibling.
2. **Weight-schedule** (`affine-in-parameter`) — the driven case is the
   `{1, iω, −ω²}` schedule over the swept ω. A single fixed-coefficient operator sum
   (e.g. a one-shot `K + M`) would be the `constant` corner.
3. **Operand-stationarity** (`fixed-basis` `{K, C, M}` | `parameter-dependent-operand`
   `A2`) — distinguishes the genuinely-fixed basis (captured once) from the
   ω-dependent extra term (the "affine modulo A2" caveat).

The general `linear_combination` arity axis is pinned to 4 (the driven readout
label); element-type pins to `complex`; output-aliasing is pure/out-of-place at L4
(as for the combinator).

### Why this is a single-pipeline specialization (by design)

Per the [`disciplined-cross-pipeline-combinator-mining-gate`](../../../skills/disciplined-cross-pipeline-combinator-mining-gate/SKILL.md):
the operator-operand `linear_combination` is shared spine vocabulary (the fold is
firm; this is the operand-category extension), so **no second-pipeline discharge
probe is owed** for *this specialization*. The affine-in-parameter fixed-basis
operator-*family* re-evaluated per parameter inside a solve loop is witnessed by
the **driven pipeline only**, and that is **permanent by design** (a finding, not a
gap): transient bakes its time-excitation into a captured `TimeOperator` at
construction (no per-step operator-family rebuild — the `fold_solve`
op-capture-once stratum); electrostatic/magnetostatic capture a single fixed `K`
(one operator, no family); eigenmode is opaque-library-owned (no Palace-assembled
operator family). So `assemble_frequency_operator` lands as a **single-pipeline
specialization**, which is fine under the redirect (solvers are pulled up as a
low-priority test-load; a clean single-pipeline specialization through existing
vocabulary is a legitimate landing). The *fold* generality comes from the firm
tensor-operand BLAS-1 cohort plus this operator-operand witness, NOT from a second
assembly site — the gate's ≥2-witness bar is satisfied by the combinator's
existing witnesses; this entry adds the operator-operand witness, not a second
*assemble-family* witness (none exists, by design).

## Downward to L1

`assemble_frequency_operator` at L4 lowers to the firm L1
[`assemble_frequency_operator`](../L1/assemble_frequency_operator.md) as
**identity-in-form on the body**: the two forms are value-thread-isomorphic. Both
layers see the same operator-operand `linear_combination` specialization — the
same signature
`assemble_frequency_operator :: FrequencyOperatorFamily[N] -> Scalar -> LinearOperator[N, N]`,
the same arity-4 term list `[(1, K), (iω, C), (−ω², M), (1, A2 ω)]`, the same six
laws, the same affine-modulo-`A2` and single-pipeline caveats, the same deferred
IEEE non-law.

**There is no dedicated L4>L3 or L4>L1 theme file** — the identity-in-form
annotation lives in-line here, per the cycle-012 non-adjacent-identity
in-line-marker convention (CLAUDE.md §Methodology invariants "Identity rotations
across non-adjacent layers are annotated in-line"). This is the **same in-line
route** its parent [`linear_combination`](./linear_combination.md) takes
(`L4/linear_combination.md:206-249`): there is no monadic wrapper, no `Solve`
monad, no convergence predicate, no outer driver to dissolve across the L4>L3 edge
— it is a pure value-producing combination at every layer, so the rotation through
the combinator is the identity on the body. The L4>L1 identity is the **transitive
consequence** of `linear_combination`'s in-line L4>L3 identity (the combinator is
identity-in-form down to L3, and the L3 fold is identity-in-form to L2/L1 per the
BLAS-1-cohort in-line annotations) composed with this entry's specialization being
identity-in-form to the firm L1 cap. The **substantive** rotation in the downward
chain is not this identity edge but the L1>L0 mutation rotation
[`assemble-frequency-operator-rotation`](../L1-L0/assemble-frequency-operator-rotation.md)
(the pure affine-operator-family value → Palace's imperative per-ω `SumOperator`
assembly via `GetSystemMatrix` → `BuildParSumOperator`, plus the per-ω
`ksp.SetOperators(*A, *P)` capture), where the pinned summation order (the IEEE
residue) lives. Creating an `L4-L1/` directory would break the per-adjacent-edge
directory convention and duplicate the transitive chain — so it is correctly an
in-line note.

## Dependencies

**Through (the combinator this specializes):** the firm L4
[`linear_combination`](./linear_combination.md) (cycle-068 D3) — at the
**operator-operand** corner of its operand-category variant axis.
`assemble_frequency_operator` is the arity-4 driven specialization; it does not
re-derive the fold. Every law is the combinator's law at this corner.

**Concept references:**
- [`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md)
  — §"The combinators rise regardless" (`:128-136`): `linear_combination` rises to
  L4 regardless as a feature-surface verb; this driven operator-operand
  specialization rides that rise. The fixed-basis operands `{K, C, M, A2}` are
  themselves FE-assembled / black-box-kernel-class operators (the
  [`fe_assemble`](./fe_assemble.md) sub-spine builds `{K, C, M}`; consumed as
  inputs, not cracked open here — the operands are opaque `LinearOperator[N, N]`
  values the combination folds over).

**Cross-cutting (role-contrast, NOT a dependency):** the result `A(ω)` is the per-ω
operator the driven solve loop inverts; the per-ω `SetOperators`-inside-the-loop is
the `map_solve` scope boundary that scopes driven out of the shared
[`solve_family`](./solve_family.md) (`L4/solve_family.md`). This entry NAMES the
per-element operator of that superset's assemble half — the driven solve half (the
`map_solve` lift) is a separate methodology decision, NOT this entry's content.

**Strawman reference:** [`../design/l4_calculus.md`](../design/l4_calculus.md) — this
verb adds **no reduction rule** (it is `linear_combination`'s fold at the
operator-operand corner, in the existing `foldl`/`+`/`scal` vocabulary).

## Status

`firm` — the L4 form is the calculus-level rendering of the firm L1
[`assemble_frequency_operator`](../L1/assemble_frequency_operator.md)
(firm-on-positive-structure cycle-062 D3), re-expressed as the **operator-operand
specialization** of the firm L4 [`linear_combination`](./linear_combination.md)
combinator (cycle-068 D3): the same arity-4 operator-operand term list, the same
six laws, value-thread-isomorphic across the L4>L1 edge (identity-in-form on the
body; no monadic wrapper to dissolve — §"Downward to L1"). The promotion is the
**firm-on-positive-structure / syntactic-identity escape** (the
`linear_combination` / `fe_assemble` / `apply_linop` precedent): every law is a
read-off syntactic operator-algebra identity carried up from the firm combinator +
the firm L1 cap (operator addition is a commutative monoid; scalar-operator scaling
distributes; the term-drop law is positively anchored in the operator domain at the
L0 `coeff[i] != 0` prune, `rap.cpp` fold body) — the absence of a dedicated
driven-assembly unit test does not gate firm because no law is an unconfirmed
runtime property; they are all syntactic identities on positive source. Two
recorded caveats are **non-gating** because they are stated facts, not unconfirmed
laws: (a) **affine modulo `A2`** — the fixed-basis degree-≤2 structure is exact for
`{K, C, M}`; `A2` is an ω-dependent operand carrying coeff `1` (the
`parameter-dependent-operand` stationarity case + the affine-as-a-whole non-law);
(b) **single-pipeline-by-design** — the affine-operator-*family* specialization is
witnessed by driven only and permanently so, so it lands as a single-pipeline
specialization with no second-pipeline discharge owed (the operand-category
generality comes from the firm tensor-operand BLAS-1 cohort plus this operator-operand
witness, per the `disciplined-cross-pipeline-combinator-mining-gate`). The L0
anchors are **inherited transitively through the firm L1 cap** (self-verified at L1
cycle-062, the per-ω combination + once-assembled basis + `BuildParSumOperator`
fold body re-confirmed on-disk this dispatch); this is an upward in-layer rendering,
not a fresh family discovery. This dispatch (cycle-069 D1) is the **rank-2
FE-cohort→L4 lift** opening the driven pipeline's **assemble half** at the L4
feature surface (directive-1: L4 is the outward backend-lowering target), riding
`linear_combination`'s cycle-068 rise (the gate cleared at `L4/linear_combination.md:40`).

## L4 vs L1 distinction

- **L1**: the mutation-rotation layer's pure-functional rendering of Palace's per-ω
  system-matrix build — the pure affine-operator-family value that the L1>L0
  rotation lowers to the imperative `SumOperator` assembly + the per-ω
  `SetOperators` capture (`L1/assemble_frequency_operator.md`). The operand-category
  specialization is recorded but the upward feature-surface naming is not L1's job.
- **L4**: the **feature-surface assemble verb** — `assemble_frequency_operator` named
  as the driven backend's per-ω operator-construction primitive, the operator-operand
  specialization of `linear_combination` at the affine-in-ω corner, written against
  the backend's verb set. The L4>L1 relationship is identity-in-form on the body
  (§"Downward to L1"); the substantive rotation in the chain is the L1>L0 mutation
  rotation, not this identity edge.

## Evidence

`assemble_frequency_operator` at L4 is the upward in-layer rendering of the firm
L1 cap as the operator-operand specialization of the firm L4 combinator; Palace's
C++ has no direct L4 realization (it writes the imperative per-ω `GetSystemMatrix`
→ `BuildParSumOperator` build). The L0 anchors are inherited transitively through
the firm L1 cap; the load-bearing ones re-confirmed on-disk this dispatch.

Firm endpoints this entry rests on:

- `book/src/L1/assemble_frequency_operator.md` (firm cycle-062 D3) — the firm L1
  source: the warrant (`:69`), the affine-modulo-`A2` caveat (`:77`, `:107`), the
  single-pipeline-by-design caveat (`:79-87`), the six laws read at the
  operator-operand corner (`:89-108`), the operator-operand framing (`:26-28`,
  `:60-69`), and the full positive L0 citation list (`:136-144`).
- `book/src/L4/linear_combination.md` (firm cycle-068 D3) — the firm L4 combinator
  this entry is the operator-operand specialization of: the operand-category
  variant axis naming the operator-operand corner + this entry as next-pull consumer
  (`:196-204`), the seven algebraic laws this entry reads at the corner
  (`:128-183`), the in-line L4>L3 identity route this entry's L4>L1 identity composes
  with (`:206-249`), the gate-cleared forward-reference (`:40`).

L0 source ranges (paths relative to `reference/palace/`; the load-bearing fold body
+ driven sites re-confirmed on-disk this dispatch via direct `sed` read):

- `palace/linalg/rap.cpp:766-787` — `BuildParSumOperator` (the operator-operand
  scalar-weighted-sum primitive): the template signature (`:766-767`), the
  shared-space precondition `MFEM_VERIFY(... same FiniteElementSpace)` (`:774-777`,
  the shape precondition law), the `SumOperator` seed (`:780-781`), and the fold
  body `for (i) if (ops[i] && coeff[i] != 0) sum->AddOperator(ops[i]->LocalOperator(), coeff[i])`
  (`:782-786`) — the scalar-weighted operator accumulate with the zero-coefficient
  sparsity prune (law 4). On-disk-confirmed this dispatch: the fold-body span is
  `:766-787`; the function continues past `:787` into a `set_essential` branch
  (`:789+`), so `:766-787` is the fold-body excerpt (NOT the function close brace —
  the L1 cap cites the same span).
- `palace/models/spaceoperator.cpp:521-528` —
  `SpaceOperator::GetSystemMatrix(a0, a1, a2, K, C, M, A2)` ≡
  `BuildParSumOperator({a0, a1, a2, ScalarType{1}}, {K, C, M, A2})` (the one-line
  forward; the literal 4-term scalar-weighted operand list, the arity-4 instance).
  On-disk-confirmed this dispatch (`:527` is the `BuildParSumOperator` call,
  `:528` the close brace).
- `palace/drivers/drivensolver.cpp:91-93` — the fixed operator basis assembled ONCE
  before the sweep (`K = GetStiffnessMatrix`, `C = GetDampingMatrix`,
  `M = GetMassMatrix`; operand-stationarity = fixed-basis). On-disk-confirmed.
- `palace/drivers/drivensolver.cpp:175` — `A2 = GetExtraSystemMatrix<ComplexOperator>(omega, ...)`
  (the ω-dependent extra-term operand; the "affine modulo A2" caveat).
  On-disk-confirmed.
- `palace/drivers/drivensolver.cpp:176-177` — `A = GetSystemMatrix(1.0+0.0i, 1i*omega, -omega*omega+0.0i, K, C, M, A2)`
  (the per-ω affine combination INSIDE the sweep loop; weights `{1, iω, −ω²}`).
  On-disk-confirmed.
- `palace/drivers/drivensolver.cpp:180` — `ksp.SetOperators(*A, *P)` (the per-ω
  operator capture = the `map_solve` superset scope boundary; the cross-cutting
  role-contrast reference, NOT this entry's content). On-disk-confirmed.

Classification / methodology anchors:

- `book/src/concepts/black-box-vs-accelerated-kernels.md` (cycle-067 D3) —
  §"The combinators rise regardless" (`:128-136`): `linear_combination` rises to L4
  regardless as a feature-surface verb; this operator-operand specialization rides
  that rise.
- `skills/disciplined-cross-pipeline-combinator-mining-gate/SKILL.md` — the
  single-pipeline-by-design specialization framing: no second-pipeline discharge
  owed (the operand-category generality comes from the firm tensor-operand cohort +
  this operator-operand witness; the affine-operator-family specialization is
  permanently driven-only by design).
- `book/src/L4/fe_assemble.md` (cycle-068 D1) — the structural-sibling precedent:
  the FE-cohort→L4 lift's combinator-as-entry + firm-on-positive-structure escape +
  shape-contract conventions this entry follows.
- `book/src/design/l4_calculus.md` — the strawman; this verb adds no reduction rule
  (a fold at the operator-operand corner in the existing `foldl`/`+`/`scal`
  vocabulary).

**No dedicated test** exercises the driven per-ω assembly at the verb entry point;
the structure is firm-on-positive-structure (every law a read-off syntactic
operator-algebra identity carried up from the firm combinator + the firm L1 cap),
so no test gates firm — the same status as the firm L1 `assemble_frequency_operator`
and the firm L4 `linear_combination` / `fe_assemble`.

**Provenance:** harvested cycle-069 D1 from the c067 D2 FE-cohort→L4 survey ranking
(rank-2, plan-tag `fe-cohort-l4-lift`); the firm L1 `assemble_frequency_operator`
(cycle-062) + the firm L4 `linear_combination` (cycle-068 D3, the operand-operand
corner + the c069-gated next-pull note) are the direct inputs. WARRANT verdict:
genuine L4 entry (both dispositions VALID; standalone entry chosen on layer-coherence
with the firm L1 cap's same-warrant standalone home + the named `map_solve` scope
boundary + operand-category-corner-distinctness from `linear_combination`'s
tensor-operand §Specializations).
```

### `book/src/L4/index.md` — §Vocabulary-cohort BULLET (mine; alpha position)

Insert my own firmness-split bullet at the **alpha-position head** of the "Firm at L4" sub-list (before the existing `krylov-step` bullet at `:34`). DEFER the consolidated firm-count tally on the `**Firm at L4 (10 + 4 outer-driver)**` line + the cycle-068/frontier prose to D2 (this cycle's sole count-owner) — do NOT touch them.

```edit:book/src/L4/index.md
- [`krylov-step`](./krylov-step.md) — typed-wrapper Krylov step kernel against the three-stratum state record; Form A consumes `iterate-while`, Form B consumes `iterate-while-with-prev`. The L4 calculus's first firm step-body shape.
```

becomes (the new `assemble_frequency_operator` bullet inserted in alpha position immediately before the `krylov-step` bullet):

```edit:book/src/L4/index.md
- [`assemble_frequency_operator`](./assemble_frequency_operator.md) — the driven per-ω **system-operator assembly verb** `A(ω) = K + iω·C − ω²·M + A2(ω)`; the **operator-operand specialization** of [`linear_combination`](./linear_combination.md) at the affine-in-ω scalar-weights corner (re-expressed THROUGH the combinator's operand-category variant axis; NOT a mirrored fold). The driven pipeline's **assemble half** reaching the L4 feature surface (directive-1: L4 is the outward backend-lowering target) — the per-ω operator the driven sweep rebuilds inside the frequency loop, named as a backend verb. Pure value-producing combination (no `Solve` monad / carry / predicate). Status `firm` (firm-on-positive-structure / syntactic-identity escape — every law is `linear_combination`'s law read at the operator-operand corner, carried up from the firm L4 combinator + the firm L1 cap; affine-modulo-`A2` + single-pipeline-by-design caveats non-gating). Lowers to [`L1/assemble_frequency_operator`](../L1/assemble_frequency_operator.md) by **identity-in-form on the body** (value-thread-isomorphic; no dedicated L4>L3/L4>L1 theme — the in-line-marker route, the transitive consequence of `linear_combination`'s in-line L4>L3 identity ∘ the L1>L0 mutation rotation). Rank-2 FE-cohort→L4 lift (plan-tag `fe-cohort-l4-lift`); harvested cycle-069 D1, riding `linear_combination`'s cycle-068 rise.
- [`krylov-step`](./krylov-step.md) — typed-wrapper Krylov step kernel against the three-stratum state record; Form A consumes `iterate-while`, Form B consumes `iterate-while-with-prev`. The L4 calculus's first firm step-body shape.
```

### `book/src/L4/index.md` — dep-map TABLE ROW (mine; alpha position)

Insert my own dep-map table row in **alpha position** — at the head of the table body, before the existing `krylov-step` row (`:77`). (The dep-map is anchor-distinct / parallel-safe per the index-registration partition; D2 owns only the consolidated tally, which is not in the table.)

```edit:book/src/L4/index.md
| [`krylov-step`](./krylov-step.md) | Form A: `OpParams -> Krylov -> (SimState -> Solve { sim, krylov, outputs })`.
```

becomes (the new `assemble_frequency_operator` row inserted in alpha position immediately before the `krylov-step` row):

```edit:book/src/L4/index.md
| [`assemble_frequency_operator`](./assemble_frequency_operator.md) | `assemble_frequency_operator :: FrequencyOperatorFamily[N] -> Scalar -> LinearOperator[N, N]`; `= linear_combination [(1, K), (1i*omega, C), (-(omega^2), M), (1, A2 omega)]`. The driven per-ω **system-operator assembly verb** `A(ω) = K + iω·C − ω²·M + A2(ω)` — the **operator-operand specialization** of [`linear_combination`](./linear_combination.md) at the affine-in-ω scalar-weights corner (re-expressed THROUGH its operand-category variant axis; NOT a mirrored fold). The driven pipeline's assemble half at the L4 feature surface. Pure value-producing combination — no `Solve` monad / carry / predicate. | Through (the combinator it specializes): [`linear_combination`](./linear_combination.md) (operator-operand corner). Concepts: `black-box-vs-accelerated-kernels` (§"the combinators rise regardless"). Role-contrast (NOT a dependency): [`solve_family`](./solve_family.md) (the `map_solve` scope boundary the per-ω operator parameterizes — driven scope-out). | L1 [`assemble_frequency_operator`](../L1/assemble_frequency_operator.md) by **identity-in-form on the body** (value-thread-isomorphic; **no dedicated L4>L3/L4>L1 theme** — in-line §"Downward to L1", the transitive consequence of `linear_combination`'s in-line L4>L3 identity composed with the L1>L0 mutation rotation [`assemble-frequency-operator-rotation`](../L1-L0/assemble-frequency-operator-rotation.md), where the substantive rewrite + pinned summation order live). | `firm` (harvested cycle-069 D1; firm-on-positive-structure / syntactic-identity escape — every law is `linear_combination`'s law read at the operator-operand corner, carried up from the firm L4 combinator (cycle-068 D3) + the firm L1 cap (cycle-062); affine-modulo-`A2` + single-pipeline-by-design caveats non-gating, no 2nd-pipeline discharge owed per the `disciplined-cross-pipeline-combinator-mining-gate`. Rank-2 FE-cohort→L4 lift, plan-tag `fe-cohort-l4-lift`; the driven pipeline's assemble half reaching L4) |
| [`krylov-step`](./krylov-step.md) | Form A: `OpParams -> Krylov -> (SimState -> Solve { sim, krylov, outputs })`.
```

```edit:book/src/SUMMARY.md
- [Overview](./L4/index.md)
- [krylov-step](./L4/krylov-step.md)
```

becomes (the new chapter inserted in alpha position immediately after Overview, before `krylov-step`):

```edit:book/src/SUMMARY.md
- [Overview](./L4/index.md)
- [assemble_frequency_operator](./L4/assemble_frequency_operator.md)
- [krylov-step](./L4/krylov-step.md)
```

## Operator content

The full firm chapter body is authored inside the `new:book/src/L4/assemble_frequency_operator.md` proposed-changes fence above. Summary of its sections:

- **Slug + one-line**: the L4 driven per-ω system-operator assembly verb `A(ω) = K + iω·C − ω²·M + A2(ω)`, the operator-operand specialization of `L4/linear_combination`.
- **Signature**: `assemble_frequency_operator :: FrequencyOperatorFamily[N] -> Scalar -> LinearOperator[N, N]`, body = `linear_combination [(1, K), (iω, C), (−ω², M), (1, A2 ω)]` (operator-operand corner, arity-4); bunsen-style shape contract with the fixed basis captured once + the `A2` parameter-dependent operand.
- **Semantics (overlay)**: pure term-list fold (the combinator's fold at the operator-operand corner); no reduction-rule extension; strawman notation.
- **Algebraic laws**: six laws read at the operator-operand corner (reduces-to-`linear_combination`; affine-in-ω-over-fixed-basis modulo `A2`; operator-multilinearity; zero-coefficient term-drop positively anchored at the L0 `coeff[i] != 0` prune; empty/seed identity; apply/assemble duality), + two explicit non-laws (affine-as-a-whole; operand-permutation IEEE residue, deferred to the lowering chain).
- **Variant axes**: operand-category (operator-operand corner) + weight-schedule (affine-in-parameter) + operand-stationarity (fixed-basis | parameter-dependent-operand); single-pipeline-by-design sub-section.
- **Downward to L1**: identity-in-form on the body; in-line-marker route, no dedicated theme; the substantive rotation is the L1>L0 mutation rotation.
- **Status**: `firm` (firm-on-positive-structure / syntactic-identity escape; two non-gating caveats).
- **Evidence**: firm L1 + L4 endpoints + on-disk-confirmed L0 ranges (`rap.cpp:766-787`, `spaceoperator.cpp:521-528`, `drivensolver.cpp:91-93`/`:175`/`:176-177`/`:180`) + classification anchors.

## Supporting evidence

Citations self-verified on-disk this dispatch (`sed` direct reads against `reference/palace/`; the codemap `read_range` `BuildParSumOperator` fold body cross-checked):

- `palace/linalg/rap.cpp:766-787` — `BuildParSumOperator` (the operator-operand scalar-weighted-sum primitive). On-disk read confirmed: the template signature at `:766-767`, the shared-`FiniteElementSpace` precondition `MFEM_VERIFY` at `:774-777`, the `SumOperator` seed at `:780-781`, the fold body `for (i) if (ops[i] && coeff[i] != 0) sum->AddOperator(...)` at `:782-786`. **Close-brace discipline (recurrence-6):** the `:766-787` span is the **fold-body excerpt**, NOT the function close brace — the function continues past `:787` into a `set_essential` branch (`if (set_essential) {` at `:789`, confirmed on-disk), so I cite `:766-787` as the body span (matching the firm L1 cap's same citation), not as the full function. No range-END off-by-one: I verified `:787` is `}` closing the `for` accumulate loop body region by direct read, not via `--anchor`.
- `palace/models/spaceoperator.cpp:521-528` — `GetSystemMatrix` ≡ `BuildParSumOperator({a0,a1,a2,1},{K,C,M,A2})`. On-disk confirmed: `:521-525` the template signature, `:527` the one-line `BuildParSumOperator` forward, `:528` the close brace `}`.
- `palace/drivers/drivensolver.cpp:91-93` (fixed basis `K`/`C`/`M` assembled once), `:175` (`A2 = GetExtraSystemMatrix<ComplexOperator>(omega, ...)`), `:176-177` (`A = GetSystemMatrix(1.0+0.0i, 1i*omega, -omega*omega+0.0i, K.get(), C.get(), M.get(), A2.get())`), `:180` (`ksp.SetOperators(*A, *P)`). All four on-disk confirmed this dispatch — they match the firm L1 cap's citations verbatim.

The L4 entry inherits these transitively through the firm L1 cap (this is an upward in-layer rendering, not a fresh family discovery); the on-disk re-confirmation is the load-bearing-citation self-verification, not a re-localization.

Sister-report / framing inputs:
- `book/src/L1/assemble_frequency_operator.md` (firm cycle-062 D3) — the source whose warrant + caveats + operator-operand framing this lift carries up.
- `book/src/L4/linear_combination.md` (firm cycle-068 D3) — the combinator this entry re-expresses through; already names this entry as next-pull operator-operand consumer (`:40`, `:196-204`).
- `book/src/L4/fe_assemble.md` (cycle-068 D1) — the structural-sibling FE-cohort→L4 precedent.

## Open questions / caveats

- **WARRANT was genuinely open; verdict recorded = GENUINE L4 ENTRY** (both dispositions VALID). The rejected disposition — a thin §Specializations note under `L4/linear_combination` — was valid-but-not-chosen (grounds in §Warrant verdict: layer-coherence with the firm L1 cap's same-warrant standalone home; the named `map_solve` scope boundary the driven solve half references; operand-category-corner distinctness from `linear_combination`'s tensor-operand §"Arity specializations"). If the integrator/critic prefers the note-disposition, the body re-expresses THROUGH `linear_combination` either way (replace-and-propagate-compliant), so a re-home would be mechanical — but the standalone-entry verdict is the considered recommendation.
- **D2 is this cycle's sole `L4/index` consolidated-count/tally/frontier-prose owner.** I registered my OWN dep-map row + §Vocabulary-cohort bullet (alpha position) + SUMMARY insert (alpha position); I DEFERRED the firm-count tally on the `**Firm at L4 (10 + 4 outer-driver)**` line + the cycle-068/frontier prose to D2. D2 reconciles the absolute count from the landed `## Status` lines (this entry lands firm → it is a +1 to the firm chapter count; D2 sums it with its own `dot`/`nrm2` landings).
- **SUMMARY L4 list is currently chronological, not alphabetical** (Overview, krylov-step, inner_product, iterate-while, ... — not alpha). Per the directive-3 mdBook by-kind grouping + alpha re-sort (meta-phase-owned, restart-pending), the global alpha re-sort is a separate structural pass. I inserted `assemble_frequency_operator` in **alpha position relative to the eventual sorted order** (immediately after Overview, before `krylov-step`) per the dispatch instruction; if the integrator is holding inserts in append-position pending the meta-phase reorg, this row can append instead — flagged so the integrator picks the consistent convention. (Same note applies to the index dep-map table + the §Vocabulary-cohort sub-list, both currently chronological; I inserted alpha-first per the dispatch's "alpha position" instruction.)
- **No `assemble_frequency_operator` L3/L2 entry exists, and none is implied by this lift.** The L4>L1 relationship is identity-in-form (the in-line-marker route); the entry does NOT forward-reference a not-yet-authored L3/L2 sibling (its parent `linear_combination` HAS firm L3/L2 entries, and the operator-operand corner is carried on those combinator entries, not as a separate `assemble_frequency_operator` chapter). No stub creation implied. The layer-intro-author may wish to note in the L4 index frontier prose (D2's scope) that the driven assemble-half is now at L4 — flagged for D2, not edited here.

