---
verifies: ../REPORT.md
critiqued_at: 2026-06-03T191500Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-03T192600Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "Formalize eigenvalue-untransform at L1"

## Critique

### Checks run

**citation-validity — warning.** Ran `citecheck.py --scan` on the report: `21 ok, 0 failing`. All
load-bearing L0 pinpoints confirmed via `--anchor` against `reference/palace/`: `:430` (`!C &&
!has_A2` selector), `:433` (`std::sqrt`), `:438` (`omega /= 1i`), `:427` (`GetEigenvalue`), `:53`
(`has_A2` selector op). Read `eigensolver.cpp:424-460` directly — the un-transform branch is exactly
as the entry describes (linear `μ=ω²` → `√`, quadratic `λ=iω` → `/= 1i`, selector derived from
`!C && !has_A2`). The L4 cross-refs `eigenfreq_qfactor_reduce.md:51-53,68,73,80-81,195-198` and
`concepts/config-record.md:61-77` all back their claims (the `:51-53` prose genuinely carries the
`ω=√μ`/`ω=λ/i` per-mode un-transform content; the literal token "untransform" appears at :73, but
the cited claim is supported by the :51-53 prose, so this is not a drift). **One genuine drift,
non-load-bearing:** the downstream-consumer citation `eigensolver.cpp:448` for `B *= -1.0 / (1i *
omega)` is off by one — the statement is at **line 449** (lines 447/448 are the two `Curl.Mult`
calls). `--anchor '1i * omega'` resolves to 449, +1 outside 448. This is a downstream-consumer
pointer (a "separate step, NOT this map", per the entry's own framing in §"Downward to L0" and
§Evidence), so it does not touch the firm verdict or any law — but it is a real off-by-one in a cited
pointer, hence `warning` not `pass`. The `:448` pinpoint appears twice (§"Downward to L0" line 210 and
§Evidence line 264); both carry the same +1 drift.

**surface-or-evidence — pass.** This is a new firm L1 primitive (not a refinement of an existing
operator), so the rotation-claim-on-modified-surface rule applies to its own evidence: the entry is
backed by the positive L0 site `eigensolver.cpp:430-439` (the literal branch) plus the selector-op
construction `:41,52-53`. **Record-definition sub-check:** the signature names two record-ish types.
`EvpDegree` is given an in-chapter `## Record definition` section (fields + types + meaning, single-
consumer justified) — definition home present. `ProblemType` is cross-referenced to the existing
on-disk `concepts/config-record.md:61-77` (verified present), not redefined — correct ≥2-consumer
disposition. The honest-framing point is handled correctly: the entry does NOT overclaim a
`ProblemType` field read — it explicitly states the L0 selector "is **not** a stored enum field — it
is the structural predicate `!C && !has_A2`" and names `EvpDegree` as the narrower derived axis. No
signature-named record lacks a home.

**rotation-quality — pass.** No L_{n+1}→L_n rotation is asserted here (this is a leaf L1 primitive
landing; the downward-to-L0 relation is an explicit identity-in-form on the scalar branch, correctly
routed in-line per the `participation_ratio`/`reciprocal` no-theme precedent, not claimed as a
rotation). The NO-L2 disposition (a bare per-mode scalar branch ⇒ an L2 mirror would be the
identity-in-named-terms smell) is the correct anti-rectangular-floor call under the 2026-06-01
vocabulary-shift redirect. Inapplicable-as-rotation, marked pass.

**variant-axis-coverage — pass.** Two axes declared: `evp-degree` (the load-bearing linear/quadratic
axis) and `element-type` (Complex). The evp-degree axis is exhaustively covered — both arms (`√μ`,
`λ/i`) are authored with laws, and a "no cross-branch identity" non-law explicitly marks the axis
load-bearing. The element-type axis is scoped (Complex→Complex, the `f=Re ω` real projection
explicitly assigned to the consumer, not this map). No hidden branch — the source has exactly the
two-way `if/else`, both covered.

**cross-reference-integrity — pass.** All sibling links resolve on disk (`participation_ratio.md`,
`reciprocal.md`, `nrm2.md`, `dot.md`, `elementwise_product.md`, `eigenfreq_qfactor_reduce.md`,
`config-record.md`). The dep-map alpha insertion is correct: on-disk row order is `dot`(113) →
`elementwise_product`(114), so the new row lands alpha-between them; the SUMMARY insert (dot /
eigenvalue-untransform / elementwise_product, 175→176) is likewise alpha-correct. The coupled
re-anchor of `eigenfreq_qfactor_reduce.md` (§"Lowers to" + dep-map + §Status gate-(a) marked
discharged, verb STAYS `rough-in (test-coverage-bounded)`) is coherent — it does not promote the verb
to firm, leaving gate-(b) open. **Tally arithmetic verified against on-disk state:** index.md
currently reads "Firm (29 main / 36 grand)"; the report's edit bumps to "30 main / 37 grand" with
`was 36 after cycle-077: 29 main + 4 FE-assembly + 3 FE-space` — internally consistent +1. The
count-reconciliation note for the D1 `matrix-weighted-norm` sibling is conditional ("IF D1
promotes... fold +1") and pre-applies nothing (counts only its own +1), so it is harmless: if D1's
verdict is +0 the note degrades to a no-op; if +1 it gives the integrator the correct fold
instruction. Not harmful.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried (leaf entry + in-line
downward-to-L0 identity note). The coupled L4 re-anchor discusses the L4→L1 gate-(a) discharge, and
the prose matches that exact relationship. Inapplicable, marked pass.

**plan-kind-consistency — pass.** Declared kind is a firm L1 operator. The content shape matches: full
signature, semantics, five algebraic laws, status reasoning, evidence — no rough-in placeholders. The
`firm` maturity rests on the firm-on-positive-structure escape, and that is **sound here**: I checked
each of the five laws against the cited source and each is a syntactic / closed-form arithmetic
identity on the two literal positive branches (`√` and `/i`) — branch definition (literal `:433`/`:438`),
inverse-of-transform round-trip (closed-form, scoped to the principal domain), sqrt homogeneity,
ℂ-linearity of `/i`, element-type purity. None carries convergence semantics, iteration, or inner-
product content. This is genuinely the same shape as the `participation_ratio`/`reciprocal`/`eigsolve`-c022
precedent the entry cites, and genuinely DISTINCT from a `matrix-weighted-norm`-style law (which would
carry sesquilinear `xᴴMx` content that is not bare closed-form scalar arithmetic). The two cycle-080
verdicts (this firm landing vs. a D1 audit that rules OUT the same escape on non-syntactic inner-
product grounds) are independently defensible — the escape turns on whether the laws are bare closed-
form, and here they are.

**skill-uptake-survey — pass.** The report invokes the mechanical citation tooling
(`tools/citecheck/citecheck.py --anchor`, `mcp__palace-codemap__read_range`/`search_text`) for
localization and self-verification, the appropriate procedure for a firm-landing harvester. No
relevant skill is implied-but-unreferenced.

### Issues found

1. **Off-by-one citation drift on the downstream-consumer pointer `eigensolver.cpp:448`** (CYCLE.md
   §"Downward to L0" line ~210 and §Evidence line ~264; also appears in the report's §"Supporting
   evidence" framing). The statement `B *= -1.0 / (1i * omega)` is at **line 449**, not 448 (lines
   447/448 are the two `Curl.Mult` calls). `--anchor '1i * omega'` → 449 (+1 outside the cited range).
   Severity: low — this is a downstream-consumer pointer that the entry itself frames as "a separate
   step, NOT this map"; it backs no law and does not touch the firm verdict. Corrected line in hand:
   `:449`. (Note `:454` Floquet, `:457-458` measure, and ALL load-bearing un-transform pinpoints are
   correct — this is the sole drift.)

2. **(Informational, not a defect) `citecheck --anchor 'untransform'` false-drift on
   `eigenfreq_qfactor_reduce.md:51-53`.** The literal token "untransform" appears at :73, not :51-53,
   so a naive anchor run reports drift — but the cited claim (the `ω=√μ`/`ω=λ/i` per-mode un-transform)
   IS supported by the :51-53 prose ("the eigenvalue un-transformed by problem type — `ω = √μ`... `ω =
   λ/i`..."). The citation is correct; flagging only so the repairer does not "fix" a valid pointer.
   No action needed.

## Repair

### Fixes attempted

- **Finding**: Off-by-one citation drift on the downstream-consumer pointer `eigensolver.cpp:448`
  for `B *= -1.0 / (1i * omega)` — the statement is at line 449 (447/448 are the two `Curl.Mult`
  calls). Appears twice (§"Downward to L0" line 210, §Evidence line 264).
- **Decision**: repaired
- **Action**: Verified on-disk against `reference/palace/palace/drivers/eigensolver.cpp` —
  `grep` confirms `447: Curl.Mult(E.Real(), B.Real())`, `448: Curl.Mult(E.Imag(), B.Imag())`,
  `449: B *= -1.0 / (1i * omega)`. Bumped both `:448` → `:449` in the proposed-changes
  block (`new:book/src/L1/eigenvalue-untransform.md` body), at CYCLE.md §"Downward to L0"
  (line 210) and §Evidence (line 264). Both are downstream-consumer pointers ("separate steps,
  NOT this map") that back no law and do not touch the firm verdict — surgical line-range bump
  within repair authority (citation line range off by a small offset).

### Deliberately NOT touched (critic DO-NOT-OVER-FIX notes, heeded)

- The `citecheck --anchor 'untransform'` "drift" on `eigenfreq_qfactor_reduce.md:51-53` is a
  FALSE alarm (literal token at :73, but the cited `ω=√μ`/`ω=λ/i` claim is genuinely backed by
  the :51-53 prose). Left as-is — valid pointer.
- The load-bearing un-transform pinpoints (`:430` selector, `:433` `std::sqrt`, `:438`
  `omega /= 1i`, `:427`, `:53`) and the `:454` / `:457-458` consumer pointers are all CORRECT.
  Left untouched.
- The D1 (`matrix-weighted-norm`) count-reconciliation note is conditional ("IF D1 promotes...")
  and degrades to a no-op when D1's actual verdict is +0. Harmless; left for the integrator.

### Unrepairable findings

None.

## Suggested resolution

`ready`. The sole citation-validity warning (a +1 off-by-one on a non-load-bearing
downstream-consumer pointer, appearing twice) is repaired in place against on-disk source; all
seven other checks pass. The firm L1 landing, the coupled `eigenfreq_qfactor_reduce.md` re-anchor
(gate-(a) marked discharged, verb STAYS `rough-in (test-coverage-bounded)`), and the +1 tally
bump (29→30 main / 36→37 grand) are coherent and ready to integrate. Note for the integrator: the
D1 conditional fold-instruction is a no-op unless D1's verdict is +1.
