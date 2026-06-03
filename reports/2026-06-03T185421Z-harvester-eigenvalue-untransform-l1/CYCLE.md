---
agent: harvester
invoked_at: 2026-06-03T185421Z
scope: L1 operator: eigenvalue-untransform
status: pending
inputs:
  - dispatch cycle-080 D2 (the residual structure-side gate to firming eigenfreq_qfactor_reduce)
  - L0: palace/drivers/eigensolver.cpp:424-439 (the readout-loop eigenvalue→ω un-transform branch)
  - firm sibling: book/src/L1/participation_ratio.md (c077 — the κ-participation half, already firm; NOT re-opened)
  - coupled re-anchor: book/src/L4/eigenfreq_qfactor_reduce.md (gate-a discharge; verb STAYS rough-in)
  - record home: book/src/concepts/config-record.md:61-77 (ProblemType already defined — cross-cutting, cross-referenced not redefined)
  - OQs resolved: eigenvalue-untransform-l1-primitive, eigenfreq-qfactor-reduce-firm-needs-l1-eigenvalue-untransform-primitive
integrated_at: 2026-06-03T192132Z
integration_commit: 7edbd3d
integration_notes: "Applied clean (D2, COUNT OWNER, staging row 1). NEW firm L1 eigenvalue-untransform created; L1 firm 29→30 main / 36→37 grand (+1). Coupled re-anchor of L4 eigenfreq_qfactor_reduce marks gate-(a) DISCHARGED (both folded per-mode scalar maps now firm L1); verb STAYS rough-in (test-coverage-bounded), NOT promoted. Owns L1/index.md tally + SUMMARY.md alpha-insert. Build exit 0, linkcheck2 clean. retroactive-budget 0, gate hits 0. Closes OQs eigenvalue-untransform-l1-primitive + eigenfreq-qfactor-reduce-firm-needs-l1-eigenvalue-untransform-primitive; opens successor eigenfreq-qfactor-reduce-firm-needs-assembly-test (gate-(b))."
---

# CYCLE: Formalize eigenvalue-untransform at L1

## Summary

The L4 verb `eigenfreq_qfactor_reduce` folds two per-mode scalar maps to build each `(f, Q)`
table row: the κ-participation ratio (already firm L1 `participation_ratio`, c077) and the
**eigenvalue→ω un-transform** — the map that recovers the physical angular frequency `ω` from
the eigenvalue the eigensolver returns. That second scalar map had no firm L1 home; it was
distilled directly from the eigensolver readout loop. This dispatch lands it as a new firm L1
primitive `eigenvalue-untransform`: the per-mode scalar branch `ω = √μ` (linear EVP) | `ω = λ/i`
(quadratic EVP), keyed on the EVP-degree of the solved pencil. Its laws are syntactic identities
on the fully-specified positive source (the `if (!C && !has_A2) { sqrt } else { /= 1i }` branch at
`eigensolver.cpp:430-439`), so it lands `firm` under the firm-on-positive-structure escape. It is
**L1-leaf-only** (no L2 entry — a bare per-mode scalar branch; an L2 mirror is the
identity-in-named-terms smell). The dispatch also re-anchors `eigenfreq_qfactor_reduce`'s §"Lowers
to" + dep-map + §Status to point at this firm entry and marks its gate-(a) **discharged**; the verb
STAYS `rough-in (test-coverage-bounded)` (gate-(b), the eigenpair→`(f,Q)` assembly test, is still
open and out of write-scope).

## Proposed changes

```new:book/src/L1/eigenvalue-untransform.md
---
layer: L1
operator: eigenvalue-untransform
firmness: firm
depends_on: []
variant_axes:
  - evp-degree (linear-EVP `ω = √μ` (μ = -λ² = ω², the squared eigenvalue) | quadratic-EVP `ω = λ/i` (λ = iω)) — THE load-bearing axis; selects which inverse map recovers ω. The L0 selector is the structural predicate `!C && !has_A2` (no damping operator AND no nonlinear A2 ⇒ linear; otherwise quadratic), NOT a literal `ProblemType` read
  - element-type (the eigenvalue and ω are both `std::complex<double>`; the map is complex-valued — the eigenfrequency `f = Re ω` projection is the consumer's, not this primitive's)
---

# eigenvalue-untransform

The L1 **eigenvalue→ω un-transform primitive**: the per-mode scalar map that recovers the
physical angular frequency `ω` from the raw eigenvalue the eigensolver returns, inverting the
problem-specific spectral transformation the eigensolver solved under,

    ω = untransform(degree, eigenvalue)
      = √μ        when degree = linear-EVP     (μ = -λ² = ω², the squared eigenvalue)
      = λ / i     when degree = quadratic-EVP  (λ = iω)

`eigenvalue-untransform` is the **second per-mode scalar building block** that the L4 eigenmode
reduction [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) folds: the
`untransform : EvpDegree -> Complex -> Complex` map the combinator applies to each eigenvalue
before taking `f = Re ω` (`eigenfreq_qfactor_reduce.md:73,80-81`). It is the sibling of the firm
[`participation_ratio`](./participation_ratio.md) (the κ-participation half, c077) — together the
two firm the **structure side** of that combinator's rough-in: this entry firms the eigenvalue
un-transform gate, `participation_ratio` already firmed the `½X|I|²/E` energy-ratio gate.

## Context

L1 re-expresses Palace's source operations as pure functions (`L1/index.md:1-3`). The eigensolver
returns each converged eigenvalue in the coordinates of whatever spectral transformation it solved
under — the **squared** angular frequency `μ = ω²` for the symmetric linear generalized EVP, or the
**imaginary-scaled** `λ = iω` for the quadratic (damped / nonlinear) polynomial EVP. The readout
loop un-transforms each eigenvalue back to the physical `ω` with a two-way branch before any
downstream measurement (`eigensolver.cpp:430-439`). `eigenvalue-untransform` names that branch as
one pure scalar function.

The operator is defined **in L1 vocabulary** (high→low discipline): its semantics, signature, and
laws are stated in terms of the eigenvalue scalar it maps and the EVP-degree it is keyed on — NOT
in terms of the L0 C++ readout loop. The forward narration of how this L1 map rewrites into the
Palace source branch is the §"Downward to L0" section.

This is **not** a BLAS-1 reduction or an `apply_linop` sibling — there is no tensor operand and no
length axis; it is a **scalar→scalar post-solve readout map**, the eigenmode-output-product
counterpart of [`participation_ratio`](./participation_ratio.md) (the other scalar readout map the
same L4 verb folds). It is the elementary algebraic atom that recovers `ω` the way `participation_ratio`
is the elementary atom that forms the κ/EPR ratio — both consume opaque scalars the eigensolver /
energy reductions produced and live above no tensor.

## Record definition

This primitive's signature names one selector type, **`EvpDegree`** — the binary EVP-degree axis
`linear-EVP | quadratic-EVP`. It is **single-consumer at L1** (only this primitive keys on it as a
standalone axis), so it is defined here rather than on a concept page:

| field/value | type | meaning |
|---|---|---|
| `linear-EVP` | `EvpDegree` | the symmetric generalized EVP `K x = μ M x` solving for `μ = ω²` (no damping operator `C`, no nonlinear `A2`); recovered by `ω = √μ` |
| `quadratic-EVP` | `EvpDegree` | the polynomial / damped EVP solving for `λ = iω` (a damping operator `C` is present, or a nonlinear `A2(ω)` term is interpolated); recovered by `ω = λ/i` |

The L0 selector is **not** a stored enum field — it is the structural predicate `!C && !has_A2`
read off the operator family at solve time: `C = space_op.GetDampingMatrix(...)` and
`has_A2 = (A2 != nullptr)` (`eigensolver.cpp:41,52-53`); the branch tests `if (!C && !has_A2)`
(`:430`). `EvpDegree` is the L1 abstraction of that predicate (linear ⟺ both absent). It is
**distinct from `ProblemType`**: the L4 verb's signature names the upstream `ProblemType` selector
(the six-member `enum class ProblemType : char`, defined as a cross-cutting record on
[`config-record`](../concepts/config-record.md):61-77, `palace/utils/labels.hpp:18-26`), but the
eigenvalue un-transform is keyed on the narrower derived EVP-degree, not the full `ProblemType` —
`EIGENMODE` problems can be either linear or quadratic depending on whether damping/nonlinear terms
are configured. `ProblemType` is cross-referenced (not redefined here); `EvpDegree` is the
in-chapter single-consumer selector this primitive actually branches on.

## Signature

    -- the eigenvalue→ω un-transform: recover the physical angular frequency from the raw eigenvalue
    eigenvalue_untransform :: EvpDegree        -- degree     : selects the inverse spectral map (linear | quadratic)
                           -> Complex          -- eigenvalue : the raw eigenvalue the eigensolver returned (μ or λ)
                           -> Complex          -- omega      : the physical angular frequency ω
    eigenvalue_untransform Linear    mu  = sqrt mu       -- μ = -λ² = ω²   (linear EVP)
    eigenvalue_untransform Quadratic lam = lam / i       -- λ = iω         (quadratic EVP)

Shape contract (bunsen-style; named axes):

- `degree : EvpDegree` — the EVP-degree selector (`linear-EVP | quadratic-EVP`). Read-only.
  Selects the inverse map. The L0 realization derives it from the operator family
  (`!C && !has_A2 ⇒ linear`, `eigensolver.cpp:430`).
- `eigenvalue : Complex` — the raw eigenvalue the eigensolver returned (`std::complex<double> omega
  = eigen->GetEigenvalue(i)`, `eigensolver.cpp:427`): the squared frequency `μ` in the linear case,
  the imaginary-scaled `λ` in the quadratic case. Read-only.
- result `omega : Complex` — the physical angular frequency `ω`. The eigenfrequency `f = Re ω` is
  the **consumer's** projection (the L4 verb / the postprocess `freq_re`), not part of this map.

The shape contract makes structural what is conventional in the C++ readout loop: each branch is one
closed-form scalar inverse of the spectral transformation the corresponding EVP class solved under.
There is no tensor operand and no reduction — the un-transform is a pure per-eigenvalue scalar map.

## Semantics

`eigenvalue_untransform degree eigenvalue` returns the physical angular frequency `ω` by applying
the inverse of the spectral transformation under which the eigensolver returned the eigenvalue:

- **Linear EVP** (`degree = linear-EVP`): the symmetric generalized problem `K x = μ M x` solves for
  `μ = -λ² = ω²`, the squared angular frequency; un-transform by the principal square root
  `ω = √μ` (`eigensolver.cpp:431-433`).
- **Quadratic EVP** (`degree = quadratic-EVP`): the damped / polynomial problem solves for the
  eigenvalue `λ = iω`; un-transform by dividing out the imaginary unit `ω = λ/i = -iλ`
  (`eigensolver.cpp:436-438`).

It is a pure scalar function — no state, no effect, no tensor. The map is total over the complex
plane in both branches (`std::sqrt` of a complex is the principal branch; `/ 1i` is exact complex
division), so there is no edge-case guard inside this primitive.

The operator's structural payoff: the eigensolver's per-mode `ω`-recovery — written as an inline
two-way branch in the readout loop, with the selector derived structurally from the presence of the
damping/nonlinear operators — is ONE scalar map keyed on the EVP-degree. The difference between the
two arms (square-root vs imaginary-division) is the **evp-degree** variant axis; the map is uniform
in structure (a per-eigenvalue closed-form inverse). The `f = Re ω` projection, the `B = -1/(iω)∇×E`
field recovery, and the Q-factor are all **downstream consumers** of the un-transformed `ω`, NOT part
of this primitive.

## Algebraic laws

Every law is a **syntactic identity on the per-eigenvalue scalar map**, read off the two positive
branches of the readout loop.

1. **Branch definition.** `eigenvalue_untransform Linear μ = √μ` and
   `eigenvalue_untransform Quadratic λ = λ/i` — the two literal closed forms (`:433`, `:438`).
2. **Inverse-of-the-transform round-trip.** Each branch is the inverse of the spectral map the
   eigensolver solved under: linear `ω = √(ω²)` recovers `ω` (principal branch, for `Re ω ≥ 0`);
   quadratic `ω = (iω)/i` recovers `ω` exactly. The un-transform composed with the forward transform
   is the identity on the principal domain.
3. **Linear-branch square-root homogeneity.** `√(k²·μ) = k·√μ` for `k > 0` — the scale factor pulls
   through the principal square root (the property that makes the `μ = ω²` recovery scale-correct
   under nondimensionalization).
4. **Quadratic-branch C-linearity.** `eigenvalue_untransform Quadratic (a·λ) = a · eigenvalue_untransform
   Quadratic λ` — division by `i` is `ℂ`-linear, so the quadratic arm commutes with complex scaling
   (the property that makes the nondimensional↔dimensional `λ`-rescaling pass through the un-transform).
5. **Element-type purity.** Both arms map `Complex → Complex` with no real/imag coupling beyond the
   closed-form scalar operation; the eigenfrequency `f = Re ω` real projection is applied by the
   consumer AFTER this map, not inside it.

Laws that explicitly **do not** hold:

- **No cross-branch identity.** The linear and quadratic arms are NOT the same function — `√μ ≠ μ/i`
  in general. The evp-degree axis is load-bearing (it selects genuinely different inverse maps), not
  a transparent variant. Picking the wrong arm silently returns a wrong frequency.
- **Not a reduction, not element-wise over a tensor.** The operand is a single already-extracted
  scalar eigenvalue; there is no length axis, no sum, no tensor (contrast [`dot`](./dot.md) /
  [`nrm2`](./nrm2.md), which DO reduce; contrast [`reciprocal`](./reciprocal.md), which maps
  element-wise over a tensor). This is a scalar→scalar map, the per-mode counterpart of
  [`participation_ratio`](./participation_ratio.md).
- **Square-root branch non-totality of the inverse-uniqueness, NOT of the function.** `√μ` is total
  (principal branch always returns), but the round-trip law (2) holds only on the principal domain
  `Re ω ≥ 0`; the eigensolver's target shift makes this the physical domain, so the readout never
  hits the ambiguous case — a precondition on the consumer, not a partiality of this map.

## Downward to L0

`eigenvalue_untransform` lowers by **identity-in-form on the scalar branch** to the eigensolver
readout loop's un-transform — each arm is the literal C++ scalar operation this primitive names
(`omega = std::sqrt(omega)` for the linear arm, `omega /= 1i` for the quadratic arm). There is no
intervening reshape: the L1 scalar map IS the C++ branch. The substantive downward content is the
**EVP-degree selector derivation** — the L0 branch keys on `!C && !has_A2` (the structural predicate
that `C = GetDampingMatrix(...)` is null AND no nonlinear `A2` was interpolated), which the L1
`EvpDegree` axis abstracts; that derivation reads the operator family assembled upstream
(`eigensolver.cpp:41,52-53`), a separate construction step, NOT part of this scalar map. No dedicated
L1>L0 theme file is authored: the rotation is the bare-scalar-branch identity (the
[`participation_ratio`](./participation_ratio.md) / [`reciprocal`](./reciprocal.md) in-line-marker
route); this entry records the rotation direction in-line per high→low discipline.

The un-transformed `ω` feeds three downstream consumers, all separate steps NOT part of this map: the
eigenfrequency projection `f = Re ω` (the L4 verb / postprocess `freq_re`), the magnetic-field
recovery `B = -1/(iω)∇×E` (`eigensolver.cpp:449`), and the Floquet B-correction scale `1/ω`
(`:454`). Those are named here as the consumers, not authored.

## Status

`firm`. **Reasoning (firm-on-positive-structure):** the un-transform structure is read directly off
the single positive Palace site — the readout-loop branch
`if (!C && !has_A2) { omega = std::sqrt(omega); } else { omega /= 1i; }`
(`eigensolver.cpp:430-439`), with the selector operators `C`/`has_A2` constructed at `:41,52-53`.
Every law (§Algebraic laws) is a **syntactic identity on the scalar branch** (two literal closed-form
complex operations and their inverse-of-the-transform round-trip), not a convergence or numerical
claim. Per the `apply_linop` / `participation_ratio` (c077) / `eigsolve` (cycle-022)
firm-on-positive-structure precedent, the **absence of a dedicated unit test** for the eigenmode
readout (the readout loop is integration-level, exercised only through the full eigenmode
`Solve(mesh)` driver — no `test/unit/` coverage) does **not** gate firm: syntactic-identity scalar
laws are not test-gated (the `eigsolve`-rough-in case was driven by literature-inferred *convergence*
semantics, absent here — this is bare closed-form arithmetic on positive source).

**No L2 entry by warrant.** `eigenvalue-untransform` is a bare per-mode scalar branch (two closed-form
inverses keyed on a binary axis). An L2 mirror would be an identity-in-named-terms re-statement — the
degenerate-mirror smell the 2026-06-01 vocabulary-shift redirect names; there is no fusion content,
no iteration, no base-primitive composition to unfold at L2. It stops at L1 as a leaf (the
[`participation_ratio`](./participation_ratio.md) / [`reciprocal`](./reciprocal.md) NO-L2 precedent).
The downstream `f = Re ω` / `B = -1/(iω)∇×E` consumers are separate readout steps with their own homes,
not L2 reshapes of this map.

**Coupled re-anchor (enacted this dispatch — see proposed-changes):** firming `eigenvalue-untransform`
discharges **gate-(a)** of the L4 [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md)
rough-in (the eigenvalue un-transform now has a firm L1 home, completing the κ-participation +
un-transform pair — `participation_ratio` discharged the κ half c077, this entry discharges the
un-transform half). That combinator's promotion is **double-gated** and remains
`rough-in (test-coverage-bounded)` until gate-(b) (a dedicated eigenpair→`(f,Q)` assembly test, or a
lowering-verifier law-confidence pass) is addressed — out of this dispatch's write-scope. The verb is
re-anchored to a live link + gate-(a) marked discharged in this dispatch; it is NOT promoted to firm.

## Evidence

All L0 citations self-verified on-disk this dispatch via the codemap
(`mcp__palace-codemap__read_range` + `search_text` + `tools/citecheck/citecheck.py --anchor` line
pinpoints against `reference/palace/`).

- **Eigenvalue un-transform (the positive site):** `palace/drivers/eigensolver.cpp:424` (the
  `for (int i = 0; i < num_conv; i++)` readout loop start), `:427`
  (`std::complex<double> omega = eigen->GetEigenvalue(i)` — the raw eigenvalue extraction),
  `:430` (`if (!C && !has_A2)` — the EVP-degree selector predicate), `:431-433`
  (`// Linear EVP has eigenvalue μ = -λ² = ω².` + `omega = std::sqrt(omega)` — the linear arm),
  `:435-438` (`// Quadratic EVP solves for eigenvalue λ = iω.` + `omega /= 1i` — the quadratic arm).
  citecheck `--anchor 'std::sqrt'` → `:433`; `--anchor 'omega /= 1i'` → `:438`; `--anchor
  'GetEigenvalue'` → `:427`; all in-range, on-disk confirmed.
- **EVP-degree selector operators (the construction the predicate reads):**
  `palace/drivers/eigensolver.cpp:41` (`auto C = space_op.GetDampingMatrix<ComplexOperator>(...)`),
  `:52-53` (`auto A2 = funcA2(target); bool has_A2 = (A2 != nullptr);`). citecheck `:41-53 --anchor
  'has_A2'` → `:53`, in-range, on-disk confirmed.
- **Downstream consumers of the un-transformed ω (separate steps, NOT this map):**
  `palace/drivers/eigensolver.cpp:449` (`B *= -1.0 / (1i * omega)` — the `B = -1/(iω)∇×E` field
  recovery), `:454` (`floquet_corr->AddMult(E, B, 1.0 / omega)` — the Floquet B-correction scale),
  `:457-458` (`post_op.MeasureAndPrintAll(i, E, B, omega, ...)` — the per-mode measure that takes
  `f = Re ω`).
- **L4 fold consumer (the gate this firms):** `book/src/L4/eigenfreq_qfactor_reduce.md:51-53` (the
  `ω = √μ` / `ω = λ/i` per-mode un-transform the combinator folds), `:68,73,80-81` (the
  `ProblemType -> ... untransform ptype lambda` signature + the `untransform Linear/Quadratic`
  branch), `:195-198` (the rough-in §Status naming the absent eigenvalue-un-transform L1 entry as
  gate-(a)). This entry IS that un-transform L1 home.
- **Firm sibling (the κ-participation half, already firm — NOT re-opened):**
  `book/src/L1/participation_ratio.md` (c077; the `½X|I|²/E` energy-ratio half of the same L4 verb's
  rough-in; this entry is its eigenvalue-un-transform sibling, the two together firming the structure
  side of `eigenfreq_qfactor_reduce`'s rough-in).
- **`ProblemType` record home (cross-cutting, cross-referenced not redefined):**
  `book/src/concepts/config-record.md:61-77` (the `enum class ProblemType : char` six-member
  definition, `palace/utils/labels.hpp:18-26`). The L1 selector `EvpDegree` is the narrower
  derived axis (the in-chapter single-consumer §Record definition), distinct from `ProblemType`.
- **Sibling-primitive grounding:** `book/src/L1/reciprocal.md` (the bare-scalar-map
  firm-on-positive-structure NO-L2 precedent for a non-reducing scalar primitive),
  `book/src/L1/nrm2.md` (the elementary `√·` analog), `book/src/L1/index.md:36` (the
  `participation_ratio` firm-on-positive-structure no-dedicated-test + NO-L2 precedent cited here).
- **No dedicated test** exercises the eigenmode readout un-transform (the `eigensolver.cpp` readout
  loop is integration-level under the eigenmode `Solve(mesh)` driver; no `reference/palace/test/unit/`
  coverage) — non-gating for the syntactic-identity scalar laws (firm-on-positive-structure).
- **Provenance:** harvested cycle-080 D2 from the OQs `eigenvalue-untransform-l1-primitive` +
  `eigenfreq-qfactor-reduce-firm-needs-l1-eigenvalue-untransform-primitive` (the residual structure
  side of `eigenfreq_qfactor_reduce`'s gate-(a)). WARRANT verdict: genuine firm L1 leaf entry (the
  eigenvalue→ω un-transform scalar map, the second per-mode building block of
  `eigenfreq_qfactor_reduce`, firming the un-transform half of its gate-(a); NO L2 by warrant).
```

```edit:book/src/L4/eigenfreq_qfactor_reduce.md
lowers_to:
  - the per-mode scalar maps (eigenvalue un-transform + κ participation ratio + f/κ quotient); identity-in-form on the body, no dedicated L4>L3 theme — in-line §"Lowers to". The two scalar-map halves now have firm L1 homes: the eigenvalue un-transform → book/src/L1/eigenvalue-untransform.md (firm, c080); the κ participation ratio → book/src/L1/participation_ratio.md (firm, c077)
```

```edit:book/src/L4/eigenfreq_qfactor_reduce.md
`eigenfreq_qfactor_reduce` lowers by **identity-in-form on the body** to the per-mode
scalar maps it folds (the eigenvalue un-transform `√μ`/`λ/i`, the κ participation ratio
`½R|I|²/E`, and the `f/κ` quotient). The reduction is a plain per-mode `map` of scalar
evaluations — there is no intervening L3/L2 absorption that reshapes the map. No dedicated
L4>L3 theme file — the in-line-marker route (the
[`inner_product`](./inner_product.md) / [`gram_reduce`](./gram_reduce.md) pattern); the
substantive downward content (the C++ readout loop, the problem-type un-transform branch
`eigensolver.cpp:430-439`, the κ computation `postoperator.cpp:1188-1203`) lives in the
eigenmode driver / postoperator L0 and the firm L1 scalar-map primitives. **Both scalar-map
halves now have firm L1 homes:** the eigenvalue un-transform `√μ`/`λ/i` →
[`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) (firm, c080); the κ participation
ratio `½R|I|²/E` → [`participation_ratio`](../L1/participation_ratio.md) (firm, c077). This entry
records the rotation direction in-line per high→low discipline; it does not author a theme.
```

```edit:book/src/L4/eigenfreq_qfactor_reduce.md
`rough-in (test-coverage-bounded)`. **Reasoning (warrant-first):** the combinator's
**structure** is read directly off the two positive readout sites — the eigenvalue→ω un-transform
(`eigensolver.cpp:424-439`) and the Q-factor body (`postoperator.cpp:1185-1203`) — and the map
laws (§Algebraic laws) are syntactic identities on that per-mode map, clearing the
firm-on-positive-structure bar. The existing PostOperator postprocess unit test
(`test/unit/test-postoperator.cpp`, the `[idempotent]` round-trip) **partially discharges the
test-gate**: it CHECK-asserts the reduction-OUTPUT cache fields the verb folds — the κ loss rate
`mode_port_kappa` (`:216`, `:259`) and the participation-ratio sibling `participation_ratio`
(`:160-188`) — as real, unit-coherent, round-trip-invariant `Measurement` fields, documenting the
`(f, Q)`/κ scalar-table output semantics as L0-equivalent. This moves the entry off bare
`rough-in` to the **test-coverage-bounded** qualifier (structure fully L0-anchored; output/laws
test-supported to the extent an output-invariance test can support them). It is NOT promoted to
`firm` because:
1. **(gate-(a) — DISCHARGED, c080).** Both per-mode building blocks the verb folds now have firm L1
   homes: the **eigenvalue un-transform** is firm L1
   [`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) (c080 — the `√μ`/`λ/i` per-mode scalar
   branch keyed on EVP-degree, citing the verb's own un-transform site `eigensolver.cpp:430-439`),
   and the **κ-participation** half is firm L1
   [`participation_ratio`](../L1/participation_ratio.md) (c077 — the resistive κ loss-rate ratio
   `½R|I|²/E`, citing the verb's own κ site `postoperator.cpp:1188-1203`). The structure-firmness
   primitive-maturity gate is now fully discharged on both folded scalar maps; and
2. **(gate-(b) — STILL OPEN, out of write-scope).** the test asserts reduction-OUTPUT invariance over
   the randomly-populated `Measurement` cache, NOT the eigenpair→`(f,Q)` **assembly map** — the
   `(f, Q)` output scalars `cache.freq` / `cache.eigenmode_Q` / the lumped-port `quality_factor` are
   populated-but-not-CHECK-asserted in the idempotency test (the asserted `quality_factor` at
   `:335-342` is `interface_eps_i` dielectric Q, a different output product), so the assembly-level
   laws are still test-unconfirmed.

Promotion route (to `firm`): gate-(a) is **discharged** (both folded per-mode primitives are now firm
L1 — the eigenvalue un-transform [`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) c080 + the
κ-participation [`participation_ratio`](../L1/participation_ratio.md) c077); the SOLE remaining gate is
**(b)** a dedicated eigenmode-postprocess assembly test (exercising the un-transform + κ-from-`E`/`I`
computation, not just output-cache round-trip) OR a lowering-verifier pass raising the assembly-map
confidence to `inner_product`-equivalent. (Contrast the rank-2 sibling [`gram_reduce`](./gram_reduce.md),
`rough-in (test-coverage-bounded)` for the same primitive-maturity + output-only-test reasons; and
the driven-pipeline sibling [`sparameter_reduce`](./sparameter_reduce.md), the same
output-invariance-test discharge shape.)
```

```edit:book/src/L4/eigenfreq_qfactor_reduce.md
- **Eigenfrequency un-transform (positive site 1):** `palace/drivers/eigensolver.cpp:424`
  (the `for (int i = 0; i < num_conv; i++)` readout loop start), `:427`
  (`std::complex<double> omega = eigen->GetEigenvalue(i)`), `:430-434` (`omega =
  std::sqrt(omega)` — linear EVP `μ = -λ² = ω²`), `:435-439` (`omega /= 1i` — quadratic EVP
  `λ = iω`), `:458` (`post_op.MeasureAndPrintAll(i, E, B, omega, …)` — the per-mode
  measure+record), `:471` (loop close), `:472-475` (`MFEM_VERIFY(num_conv >= …n)`). Firm L1 home:
  [`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) (c080).
```

```edit:book/src/L1/index.md
- [`participation_ratio`](./participation_ratio.md) — energy-participation-ratio scalar quotient `p = energy / E_total` (signed variant `copysign(energy/E_total, Re I)`); the shared `½X|I|²/E` shape of the eigenmode resistive-κ / inductive-EPR / surface-dielectric participations, differing only in the numerator-energy source (the **numerator-energy-source** + **signed-vs-unsigned** variant axes). A scalar-quotient post-reduction atom (consumes already-reduced energies, NOT a reduction; sibling to `nrm2`/`reciprocal`); firms gate-a of the L4 [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) fold. NO L2 entry by warrant (a bare scalar quotient — an L2 mirror is the identity-in-named-terms smell). Firm-on-positive-structure (no-dedicated-test caveat non-gating). Harvested cycle-077.
- [`eigenvalue-untransform`](./eigenvalue-untransform.md) — eigenvalue→ω un-transform scalar map `ω = untransform(degree, eigenvalue)`: `√μ` (linear EVP, `μ = -λ² = ω²`) | `λ/i` (quadratic EVP, `λ = iω`), keyed on the **evp-degree** variant axis (the L0 selector is the structural predicate `!C && !has_A2`, NOT a literal `ProblemType` read — defined as the in-chapter single-consumer `EvpDegree` record). A scalar→scalar post-solve readout map (no tensor, no reduction; sibling to `participation_ratio`/`reciprocal` as an elementary arithmetic atom); the SECOND per-mode building block the L4 [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) fold folds (with `participation_ratio`), firming the eigenvalue-un-transform half of that verb's gate-(a). NO L2 entry by warrant (a bare per-mode scalar branch — an L2 mirror is the identity-in-named-terms smell). Firm-on-positive-structure (no-dedicated-test caveat non-gating per `participation_ratio`/`reciprocal`/`eigsolve`-c022). Harvested cycle-080.
```

Dep-map table — insert the new `eigenvalue-untransform` row in alpha position (between `dot` and `elementwise_product`). The `old_string` is the single existing `dot` row; the `new_string` is that same `dot` row followed by the new row:

```edit:book/src/L1/index.md
| [`dot`](./dot.md) | `(x, y) → ⟨x, y⟩` (hermitian for complex) | (leaf) | `firm` |
| [`eigenvalue-untransform`](./eigenvalue-untransform.md) | `(degree: EvpDegree, eigenvalue: Complex) → Complex` (i.e. `ω = √μ` (linear EVP) \| `λ/i` (quadratic EVP)) | (leaf; scalar→scalar post-solve readout map; consumes a single eigenvalue scalar, NOT a reduction and NOT element-wise over a tensor; sibling to `participation_ratio`/`reciprocal` as an elementary arithmetic atom) | `firm` (eigenvalue→ω un-transform; the second per-mode scalar map the L4 [`eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md) fold folds — **firms the eigenvalue-un-transform half of that verb's gate-(a)**, the κ-participation half being firm L1 [`participation_ratio`](./participation_ratio.md) c077; **evp-degree** THE load-bearing variant axis (linear `√μ` / quadratic `λ/i`), L0 selector is the structural predicate `!C && !has_A2` not a literal `ProblemType` (in-chapter `EvpDegree` single-consumer §Record definition; `ProblemType` cross-referenced to [`config-record`](../concepts/config-record.md)); L0: `palace/drivers/eigensolver.cpp:430-439` the branch + `:41,52-53` the selector operators + `:427` eigenvalue extraction; harvested cycle-080; firm-on-positive-structure, no-dedicated-test caveat non-gating per `participation_ratio`/`reciprocal`/`eigsolve`-c022; NO L2 entry by warrant — bare per-mode scalar branch, an L2 mirror is the identity-in-named-terms smell) |
```

```edit:book/src/SUMMARY.md
  - [dot](./L1/dot.md)
  - [eigenvalue-untransform](./L1/eigenvalue-untransform.md)
  - [elementwise_product](./L1/elementwise_product.md)
```

## Consolidated-tally bump (count-owner — this dispatch)

```edit:book/src/L1/index.md
**Firm (30 main cohort; 37 firm grand total incl. the FE-assembly + FE-space sub-spines).** The 30 main-cohort firm operators are listed below; the FE-assembly sub-spine adds **4** more firm (`fe_assemble` c054 + `weak_form_term` c061 + `eliminate_essential_bc` + `eliminate_rhs` both c055 — see the §"Firm (FE-assembly sub-spine)" subsection), and the FE-space sub-spine adds **3** more firm (`fe_space` c064 + `fe_collection` c065 + `essential_dofs` c066 — see the §"Firm (FE-space sub-spine)" subsection), bringing the L1 firm grand total to **37** (cycle-080 D2 added the main-cohort's 30th firm member `eigenvalue-untransform`, the eigenvalue→ω un-transform scalar map `√μ`/`λ/i` — the SECOND per-mode scalar building block the L4 `eigenfreq_qfactor_reduce` fold folds, firming the eigenvalue-un-transform half of that verb's gate-(a); was 36 after cycle-077: 29 main + 4 FE-assembly + 3 FE-space; cycle-077 D5 added the main-cohort's 29th firm member `port_projection`, the port-mode linear-functional projection `⟨s, E⟩`; cycle-077 D4 added the 28th firm member `participation_ratio`, the energy-participation-ratio scalar-quotient primitive; cycle-066 D1 added the FE-space sub-spine's third firm member `essential_dofs`, the boundary-attribute→essential-true-dof-set constructor). Count discipline: the grand total is computed by reading each linked chapter's `## Status` line, not the index cells — 30 main + 4 FE-assembly + 3 FE-space = 37; equivalently the dep-map table now holds **37** `firm` rows (incl. `eigenvalue-untransform` c080, `assemble_frequency_operator` c062, `port_projection` c077, `fe_assemble` c054, `fe_space` c064, `fe_collection` c065, and `essential_dofs` c066). All firm rows are now on-table; there is no off-table firm operator. **Count-reconciliation note for the per-report integrator (cycle-080):** this tally is authored count-owner-blind to co-dispatched D1 (a `matrix-weighted-norm` lowering-verifier audit). IF D1's audit promotes `matrix-weighted-norm` rough-in→firm, fold its **+1** into BOTH the main-cohort count (30→31) and the grand total (37→38) when applying serially (and move its bullet from the §"Rough-in (test-coverage-bounded)" sub-list to the firm sub-list); this tally counts ONLY this dispatch's `eigenvalue-untransform` +1. The 30 main-cohort firm operators are element-wise updates, BLAS-1 reductions, the fused-normalise primitive, the energy-participation-ratio scalar-quotient primitive (`participation_ratio`, c077), the eigenvalue→ω un-transform scalar map (`eigenvalue-untransform`, c080 — the `√μ`/`λ/i` per-mode un-transform keyed on EVP-degree, the second per-mode scalar building block of `eigenfreq_qfactor_reduce`), the port-mode linear-functional projection (`port_projection`, c077), the opaque-operator gate, the constructed-operator solve gate, the eigenmode-solve gate, the polynomial-smoother gate, the divergence-free projector gate, the nonlinear-pencil interior atom, the NEP deflated-residual extension, the small-dense direct-solve gate, the NEP deflated-solve extension, the NEP quasi-Newton Jacobian action, the NEP quasi-Newton eigenvalue-correction step, the GMRES/FGMRES restart-correction back-solve, the GMRES/FGMRES per-column running-QR leaf, the diagonal-preconditioner-apply Jacobi smoother, the elementwise multiplicative-inverse primitive, the elementwise (Hadamard) pointwise-product primitive, the floquet-periodicity B-field correction gate, and the driven per-ω system-operator assembly (`assemble_frequency_operator`, c062):
```

## Operator content

The full firm chapter body is authored inside the `new:book/src/L1/eigenvalue-untransform.md`
proposed-changes block above. Summary of the operator:

- **Slug + one-line**: `eigenvalue-untransform` — the per-mode eigenvalue→ω un-transform scalar map
  `ω = √μ` (linear EVP) | `ω = λ/i` (quadratic EVP), keyed on EVP-degree.
- **Signature**: `eigenvalue_untransform :: EvpDegree -> Complex -> Complex` (scalar→scalar; named
  axes `degree` / `eigenvalue` / `omega`).
- **Semantics**: inverse of the spectral transformation the eigensolver solved under — principal
  square root for the linear (`μ = ω²`) EVP, imaginary-division for the quadratic (`λ = iω`) EVP.
- **Algebraic laws**: branch definition, inverse-of-transform round-trip, linear-branch
  square-root homogeneity, quadratic-branch ℂ-linearity, element-type purity. Non-laws: no
  cross-branch identity (evp-degree is load-bearing), not a reduction / not element-wise.
- **Record definition**: in-chapter `EvpDegree` single-consumer selector; `ProblemType`
  cross-referenced to `concepts/config-record.md` (cross-cutting, NOT redefined).
- **Status**: `firm` (firm-on-positive-structure; no-dedicated-test caveat non-gating). NO L2 by
  warrant.
- **Evidence**: `palace/drivers/eigensolver.cpp:430-439` (the branch), `:41,52-53` (the selector
  operators), `:427` (eigenvalue extraction), all self-verified on-disk via citecheck `--anchor`.

## Supporting evidence

- L0 positive site `palace/drivers/eigensolver.cpp:424-439` — confirmed on disk; the dispatch hint
  range matched exactly (no drift). citecheck `--anchor` confirmations: `std::sqrt`→`:433`,
  `omega /= 1i`→`:438`, `GetEigenvalue`→`:427`, `has_A2`→`:53` (all in-range).
- `book/src/L1/participation_ratio.md` (c077) — the firm κ-participation sibling; this dispatch is
  its un-transform sibling, the two firming the structure side of `eigenfreq_qfactor_reduce`'s
  gate-(a). NOT re-opened.
- `book/src/L4/eigenfreq_qfactor_reduce.md:51-53,68,73,80-81,195-198` — the fold consumer + the
  gate-(a) text re-anchored this dispatch.
- `book/src/concepts/config-record.md:61-77` — the `ProblemType` cross-cutting record-definition
  home (cross-referenced, not redefined; `EvpDegree` is the narrower derived in-chapter axis).

## Open questions / caveats

- **RESOLVED: `eigenvalue-untransform-l1-primitive`** — landed firm this dispatch.
- **RESOLVED: `eigenfreq-qfactor-reduce-firm-needs-l1-eigenvalue-untransform-primitive`** —
  gate-(a) of `eigenfreq_qfactor_reduce` is now fully discharged (both folded scalar maps —
  `eigenvalue-untransform` c080 + `participation_ratio` c077 — are firm L1). The verb STAYS
  `rough-in (test-coverage-bounded)`; only gate-(b) (the eigenpair→`(f,Q)` assembly test, or a
  lowering-verifier law-confidence pass) remains.
- **APPEND OQ `eigenfreq-qfactor-reduce-firm-needs-assembly-test` (gate-(b), out of write-scope):**
  `eigenfreq_qfactor_reduce` is now single-gated on gate-(b) — a dedicated eigenmode-postprocess
  assembly test exercising the un-transform + κ-from-`E`/`I` computation (not just the
  `test-postoperator.cpp` output-cache round-trip), OR a lowering-verifier pass raising the
  assembly-map confidence to `inner_product`-equivalent. The assembly test is integration-level under
  the eigenmode `Solve(mesh)` driver with no `test/unit/` home, so it may be out of project
  write-scope (the same shape as the `gram_reduce` / `sparameter_reduce` gate-(b)). A
  lowering-verifier dispatch on `eigenfreq_qfactor_reduce` (now that BOTH folded primitives are firm)
  is the in-scope promotion route.
- **Count-reconciliation flag (for the per-report integrator):** see the consolidated-tally edit's
  inline note — this dispatch is the SOLE count-owner of `book/src/L1/index.md` tally + `SUMMARY.md`;
  the co-dispatched D1 lowering-verifier defers its possible `matrix-weighted-norm` +1 firm delta to
  this tally. The tally as authored counts ONLY this dispatch's `eigenvalue-untransform` +1
  (30 main / 37 grand). If D1 promotes `matrix-weighted-norm`, fold +1 into both counts (31 main / 38
  grand) and move its §Vocabulary-cohort bullet from "Rough-in (test-coverage-bounded)" to the firm
  sub-list when applying serially.
- **Selector-naming caveat (resolved in-chapter, flagged for reviewer awareness):** the L4 verb's
  signature names `ProblemType` as the un-transform selector, but the L0 branch keys on the narrower
  derived predicate `!C && !has_A2` (EVP-degree), not a literal `ProblemType` read. The L1 entry
  names the honest L0 selector (`EvpDegree`) and notes the L4-verb's `ProblemType` is the upstream
  abstraction. No contradiction — the L4 `ProblemType` selector dispatches to the EVP-degree at the
  un-transform site; the two are consistent (an `EIGENMODE` `ProblemType` can be linear or quadratic
  by configured damping/nonlinear terms).
