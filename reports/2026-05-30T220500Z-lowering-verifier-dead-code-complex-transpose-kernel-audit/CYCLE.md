---
agent: lowering-verifier
invoked_at: 2026-05-30T220500Z
scope: L1>L0 dead-code complex-transpose kernel cohort — verdict-only audit (jacobi + chebyshev + axpby)
status: pending
integrated_at: 2026-05-31T01:30:00Z
integration_commit: 4655e1b
integration_notes: |
  cycle-034 D2 — verdict-only audit, NO `book/` artifact changes; applied clean. Audit verdicts: jacobi `:61-69` supports (template-dead correctly recorded); chebyshev `:101-110` supports + `:150-159` supports-with-citation-hygiene-note (overshoots by 4 lines; precise body is `:147-155` — INFORMATIONAL, routed forward as low-priority hygiene OQ `chebyshev-smoother-mutation-rotation-applyorderk-true-citation-tighten` at scaffolding/open-questions.md:489); axpby ComplexVector::Subtract does-not-support-planner-mischaracterization (defined-not-used recognition rule, NOT a transpose kernel — the audited theme's existing framing is correct). OQ closed: `jacobi-mutation-rotation-dead-code-complex-transpose-kernel-lowering-verifier-audit` (at scaffolding/open-questions.md:485). D2 verdict strengthens D1's caveat on jacobi `:61-69` template-dead — D1's per-theme OQ pointer `reciprocal-elementwise-product-mr-dead-code-transpose-consumer-branch` cross-references this audit's resolution. Planner-scope-precision callout (CYCLE.md:185 — "the cycle-034 dispatch scope conflated two distinct shapes of dead code under one umbrella") recorded as a methodology observation for the BATCH-10 meta-phase (NOT this finalize's cycle, since c034 is batch-10 position 1). Build-relevant: no. retroactive-budget 0. Wave-conflict: none. Per-report integrator confirmed clean.
inputs:
  - book/src/L1-L0/jacobi-smoother-mutation-rotation.md
  - book/src/L1-L0/chebyshev-smoother-mutation-rotation.md
  - book/src/L1-L0/axpby-mutation-rotation.md
  - book/src/L1-L0/axpbypcz-mutation-rotation.md
  - palace/linalg/jacobi.cpp:41-71 (real + complex Apply templates)
  - palace/linalg/jacobi.hpp:1-47 (JacobiSmoother class + MultTranspose self-alias)
  - palace/linalg/chebyshev.cpp:60-156 (ApplyOrder0 + ApplyOrderK templates, real + complex)
  - palace/linalg/chebyshev.hpp:50-141 (ChebyshevSmoother + ChebyshevSmoother1stKind classes; both MultTranspose2 aliases)
  - palace/linalg/vector.hpp:115-128 (ComplexVector AXPY/Add/Subtract member API)
  - palace/linalg/vector.cpp:313-379 (ComplexVector::AXPBY both signatures)
  - palace/linalg/vector.cpp:713-743 (linalg::AXPY/AXPBY free-function specialisations)
  - codemap get_call_sites Apply / ApplyOrder0 / ApplyOrderK / Subtract
  - codemap search_text Apply<true> / ApplyOrder0<true> / ApplyOrderK<true> / \.Subtract\s*\(
---

# CYCLE: Audit dead-code complex-transpose kernel cohort (jacobi + chebyshev + axpby)

## Summary

Verdict-only negative-finding audit of three "dead-code complex-transpose kernel" caveats currently recorded in the firm smoother / vector-axpy themes:

- **jacobi** — `palace/linalg/jacobi.cpp:61-69` (the `Transpose=true` `else` branch of the complex `Apply` template inside the file-private anonymous namespace).
- **chebyshev** — `palace/linalg/chebyshev.cpp:101-110` (`ApplyOrder0<true>` else branch) and `:150-159` (`ApplyOrderK<true>` else branch).
- **axpby** — `palace/linalg/vector.hpp:118` `ComplexVector::Subtract` (+ the related `operator-=`, complex-`α` free-function `linalg::AXPY` overload).

**Top-level verdict — fully-supported, with one planner-scope mischaracterization and two minor citation-hygiene observations:**

1. **jacobi `:61-69`**: confirmed dead — `Apply<true>` has zero call sites; `MultTranspose` (jacobi.hpp:43) self-aliases to `Mult` which calls `Apply` with the default `Transpose=false`; caveat in `book/src/L1-L0/jacobi-smoother-mutation-rotation.md` (lines 144-222, 310-336, 569-600) is present, accurate, and well-anchored.
2. **chebyshev `:101-110, :150-159`**: confirmed dead — `ApplyOrder0<true>` and `ApplyOrderK<true>` have zero call sites; both `ChebyshevSmoother::MultTranspose2` (palace/linalg/chebyshev.hpp:73-76) and `ChebyshevSmoother1stKind::MultTranspose2` (palace/linalg/chebyshev.hpp:138-141) self-alias to `Mult2`; `Mult2` calls the kernels with default `Transpose=false`; caveat in `book/src/L1-L0/chebyshev-smoother-mutation-rotation.md` (lines 134-156, 239-243, 371-373) is present and accurate; one minor end-of-range overshoot on the `:150-159` citation (precise body is `:147-155` — 3 lines short on start, 4 lines over on end). Recommendation: tighten in a future hygiene pass; not verdict-blocking.
3. **axpby `ComplexVector::Subtract` variant forms**: **planner-scope mischaracterization** — `Subtract` is NOT a dead-code complex-transpose kernel. It is a **defined-not-used in-place AXPY-with-negated-alpha wrapper** (`Subtract(α, x) { AXPY(-α, x); }`) — a member-API recognition rule, not a `Transpose=true` template branch. The axpby theme (lines 215-238) correctly records `ComplexVector::Subtract`, `operator-=`, and the complex-`α` `linalg::AXPY` overload as **defined-not-used recognition rules for *potential* call sites**, which is the right call. The two patterns (template-dead `Transpose=true` branch vs. defined-not-used member-API recognition rule) are distinct shapes of dead code, and the planner conflated them. **No edit to the axpby theme is needed**; the caveat is already correctly framed.

## Per-citation audit

### Jacobi cohort

- **Citation**: `palace/linalg/jacobi.cpp:61-69`
- **Theme claim** (`book/src/L1-L0/jacobi-smoother-mutation-rotation.md:597-600`): "Dead-code complex transpose kernel. `palace/linalg/jacobi.cpp:61-69` is the `Transpose=true` complex-`dinv` Hermitian-transpose elementwise kernel; it is unreachable under the symmetric `MultTranspose → Mult` wiring. Same defined-not-used status as the complex-`α` AXPY overload in axpby."
- **Found**: Lines 61-69 ARE the `else` block of the `Apply(ComplexVector&, ComplexVector&, ComplexVector&)` template specialisation, which only executes when the template arg `Transpose=true`. The `else`-branch body computes the **conjugate-transpose** complex element-wise product (`YR[i] = DIR[i]*XR[i] + DII[i]*XI[i]`, `YI[i] = -DII[i]*XR[i] + DIR[i]*XI[i]` — note the swapped signs on the imaginary parts vs. the `Transpose=false` branch at lines 53-60).
- **Reachability check**:
  - `mcp__palace-codemap__get_call_sites(name="Apply")` returns exactly one site: `palace/linalg/jacobi.cpp:103` (inside `JacobiSmoother<OperType>::Mult`).
  - The call site at line 103 omits the template argument — `Apply(dinv, x, y)` — so `Transpose` resolves to its default `false`.
  - `mcp__palace-codemap__search_text(pattern="Apply<true>")` returns zero hits across the whole Palace tree.
  - `JacobiSmoother::MultTranspose` (jacobi.hpp:43) is an inline one-liner: `void MultTranspose(const VecType &x, VecType &y) const override { Mult(x, y); }` — it forwards verbatim to `Mult`, so even consumers calling `MultTranspose` end up in `Apply<false>`.
  - No other in-tree symbol named `Apply` could plausibly resolve to this anonymous-namespace template (the codemap call-site query is name-only, and the only hit is the one in the same file — namespace-local templates have only intra-TU visibility, which the codemap correctly observes).
- **Negative-finding exhaustiveness check** (per `establish-negative-finding-exhaustiveness` skill):
  - Stated terms searched: `Apply` (suffix `::` matching), `Apply<true>`.
  - Broadened sweep: searched for any explicit template instantiation of `Apply` with a non-default `Transpose` argument; none found.
  - Residual token accounting: the only consumer surface is `JacobiSmoother::Mult` / `MultTranspose`, both of which are accounted for; the `Apply` anonymous-namespace template has no external linkage.
  - Positive-API confirmation: `JacobiSmoother::Mult` IS the live consumer (line 103); `MultTranspose` IS aliased to it. The forward (non-transpose) `Apply<false>` IS reachable.
- **Verdict**: **supports**. The dead-code claim is correct; the citation range is precise (`:61-69` is exactly the `else` block).
- **Notes**: The Transpose=true branch differs from Transpose=false only in the sign pattern, consistent with the conjugate-transpose of the action of a complex diagonal operator. The mathematical content is well-defined; it just has no caller.

### Chebyshev cohort

- **Citation**: `palace/linalg/chebyshev.cpp:101-110`
- **Theme claim** (`book/src/L1-L0/chebyshev-smoother-mutation-rotation.md:134-156, 371-373`): "Dead-code complex transpose kernels. `palace/linalg/chebyshev.cpp:101-110, :150-159` are the conjugate-transpose complex element-wise kernels; they are unreachable under the symmetric `MultTranspose2 → Mult2` wiring."
- **Found**: Lines 101-110 contain the closing brace of the `if (!Transpose)` branch (line 101 = `}`) immediately followed by the `else` block (`:102-110`) inside `ApplyOrder0<bool Transpose>(...)`'s complex-vector overload (`ApplyOrder0(const double sr, const ComplexVector &dinv, const ComplexVector &r, ComplexVector &d)` at `:82-83`). The `else`-branch body lambda (`:104-109`) computes the conjugate-transpose complex elementwise product `DR[i] = sr * (DIR[i]*RR[i] + DII[i]*RI[i])`, `DI[i] = sr * (-DII[i]*RR[i] + DIR[i]*RI[i])`.
- **Reachability check**:
  - `mcp__palace-codemap__search_text(pattern="ApplyOrder0<true>")` returns zero hits.
  - The two `Mult2` implementations (`ChebyshevSmoother::Mult2` at `:191-220`, `ChebyshevSmoother1stKind::Mult2` at `:261-293`) call `ApplyOrder0(...)` without a template arg (line 209 and line 279 respectively), so `Transpose` defaults to `false`.
  - `ChebyshevSmoother::MultTranspose2` (palace/linalg/chebyshev.hpp:73-76) and `ChebyshevSmoother1stKind::MultTranspose2` (palace/linalg/chebyshev.hpp:138-141) both forward verbatim to `Mult2` with the inline comment `// Assumes operator symmetry`. The transpose dispatch never reaches `ApplyOrder0<true>`.
- **Verdict**: **supports-with-citation-hygiene-note**. The dead-code claim is correct. The citation `:101-110` includes line 101 (the closing brace of the `if (!Transpose)` branch) as containing context. The precise dead-code `else` body is `:102-110`. This is acceptable as a "containing context" range (the `else` is clearly the body, and the `if/else` split line is informative), but a tighter `:102-110` would be more precise. Not verdict-blocking.

- **Citation**: `palace/linalg/chebyshev.cpp:150-159`
- **Theme claim**: same as above — the second dead-code kernel is `ApplyOrderK<true>` (the higher-order recurrence kernel).
- **Found**: Lines 150-155 are inside the `else` block of `ApplyOrderK<bool Transpose>(const double sd, const double sr, const ComplexVector &dinv, const ComplexVector &r, ComplexVector &d)` (the complex-vector overload at `:127-128`). The `else` block actually starts at line 147 (`else`) / 148 (`{`); the body lambda is at `:149-154`; the closing `}` of the `else` block is at `:155`. Lines 156-159 in the cited range are: 156 = function closing `}`, 157 = blank, 158 = `}  // namespace`, 159 = blank.
- **Reachability check**:
  - `mcp__palace-codemap__search_text(pattern="ApplyOrderK<true>")` returns zero hits.
  - Both `Mult2` implementations call `ApplyOrderK(...)` without a template arg (line 216 in `ChebyshevSmoother::Mult2`, line 288 in `ChebyshevSmoother1stKind::Mult2`), defaulting to `Transpose=false`.
  - Same `MultTranspose2 → Mult2` aliases described above.
- **Verdict**: **supports-with-citation-hygiene-note**. Dead-code claim correct. Citation overshoots: precise body is `:147-155`; the cited `:150-159` is shifted by ~3 lines on start (missing `else` keyword and opening `{`) and ~4 lines on end (capturing function-closing `}` + blank + namespace-closing `}` + blank). The claim is still grounded — the kernel-body lambda lines `:152-153` sit inside the cited range — but the range is loose. Recommend tightening to `:147-155` in a future hygiene pass.

### Axpby / axpbypcz cohort

- **Citation**: `palace/linalg/vector.hpp:118` — `ComplexVector::Subtract(α, x) { AXPY(-α, x); }`.
- **Planner-scope claim**: `ComplexVector::Subtract` variant forms are sibling "dead-code complex-transpose kernels" cited in the axpby/axpbypcz mutation-rotation theme.
- **Found**: `Subtract` is **not a transpose kernel**. It is a one-line in-place AXPY-with-negated-alpha wrapper defined at `vector.hpp:118`:
  ```
  void Subtract(std::complex<double> alpha, const ComplexVector &x) { AXPY(-alpha, x); }
  ```
  It computes `(*this) += (-α) * x`, i.e. `(*this) -= α * x`. There is no `Transpose=true` template branch in any AXPY-family kernel — the in-place addition kernels in `vector.cpp` (the body of `ComplexVector::AXPY` near `:280-310`) are direct elementwise and don't have a transpose axis.
- **What the theme actually says** (`book/src/L1-L0/axpby-mutation-rotation.md:215-238`): The theme records `ComplexVector::Subtract`, `ComplexVector::operator-=`, and the complex-`α` `linalg::AXPY` free-function overload (`vector.cpp:720-724`) as **defined-not-used recognition rules for *potential* call sites**. Status is `firm` with no constructive sub-part. This is a separate shape of dead code: **member-API defined-but-uncalled** vs. **template-dead `Transpose=true` branch**.
- **Reachability check** (for completeness on `Subtract`):
  - `mcp__palace-codemap__get_call_sites(name="Subtract")` returns empty (`{"sites":[]}`).
  - `mcp__palace-codemap__search_text(pattern="\.Subtract\s*\(")` returns zero hits.
  - Confirmed defined-not-used in palace/**.
- **Verdict**: **does-not-support-planner-mischaracterization**. `ComplexVector::Subtract` is not a transpose kernel, and the axpby theme does not (and should not) record it as one. The planner conflated two distinct dead-code shapes; the axpby theme's existing handling is correct. **No caveat edit needed.**
- **Notes**: The cross-theme observation in the jacobi caveat at `:600` ("Same defined-not-used status as the complex-`α` AXPY overload in axpby") IS reasonable cross-reference shorthand — both are "defined-not-used in palace/**" — but the underlying mechanism differs (template-dead branch vs. member-API uncalled). The themes describe the difference accurately; only the cycle-034 planner scope description was loose.

## Applicability conditions

For the jacobi + chebyshev caveats, the "dead code under symmetric wiring" claim depends on the following conditions, all of which hold in the cited L0:

- **Condition 1**: `MultTranspose` (or `MultTranspose2`) is wired to forward verbatim to `Mult` (or `Mult2`) — **Verifiable**: palace/linalg/jacobi.hpp:43; palace/linalg/chebyshev.hpp:73-76; palace/linalg/chebyshev.hpp:138-141. **Found counter-example?** No.
- **Condition 2**: `Mult` (or `Mult2`) calls the kernel template (`Apply` / `ApplyOrder0` / `ApplyOrderK`) without an explicit `Transpose=true` argument — **Verifiable**: palace/linalg/jacobi.cpp:103; palace/linalg/chebyshev.cpp:209, :216 (4th-kind); palace/linalg/chebyshev.cpp:279, :288 (1st-kind). **Found counter-example?** No.
- **Condition 3**: No other consumer in palace/** explicitly instantiates the template with `Transpose=true` — **Verifiable**: codemap `search_text` for `Apply<true>`, `ApplyOrder0<true>`, `ApplyOrderK<true>` all return zero. **Found counter-example?** No.
- **Condition 4** (load-bearing for the semantic interpretation): The aliasing reads as **transpose** (not Hermitian-transpose) — verified in the theme: real `dinv` makes the distinction vacuous for real `OperType`; for complex `dinv` the conjugate-transpose would be the Hermitian-transpose action, but no consumer site exercises this. **Found counter-example?** No.

For the axpby `Subtract` recognition rule, the "defined-not-used in palace/**" claim is verifiable via `get_call_sites("Subtract")` returning empty. **Found counter-example?** No.

## Algebraic laws (if cited)

The themes' algebraic-justification dependence on the dead-code caveats is minimal — the caveat does NOT carry a law; it carries a **negative observation**. The law content in the theme's "Algebraic laws" sections is for the LIVE forward (non-transpose) path and is unaffected by the dead-code caveat. The transpose-aliasing law (sub-pattern D in jacobi, sub-pattern C in chebyshev) is the **symmetric-wiring self-alias** law: `MultTranspose ≡ Mult` under operator symmetry. Holds trivially given the inline override.

## Proposed changes

**None.** All three caveats are correctly recorded.

- Jacobi: caveat is present, citation is precise.
- Chebyshev: caveat is present, citations are correct (with one minor end-of-range overshoot on `:150-159` flagged as a hygiene observation — recommend tightening to `:147-155` in a future hygiene pass; not blocking).
- Axpby: planner scope mischaracterized `Subtract` as a transpose kernel; the theme's existing treatment of `Subtract` (defined-not-used recognition rule) is correct and needs no edit.

```yaml
verified_against:
  - citation: palace/linalg/jacobi.cpp:61-69
    verdict: supports
    audited_at: 2026-05-30T220500Z
    note: jacobi Apply<true> Transpose=true else-branch is template-dead; codemap get_call_sites Apply returns single site jacobi.cpp:103 inside Mult which omits the template argument (defaults Transpose=false); search_text Apply<true> returns zero hits; jacobi.hpp:43 MultTranspose self-aliases to Mult — symmetric-wiring alias confirmed
  - citation: palace/linalg/jacobi.hpp:43
    verdict: supports
    audited_at: 2026-05-30T220500Z
    note: MultTranspose inline override forwards verbatim to Mult — this is the symmetric-wiring alias that renders the Transpose=true template branch unreachable from Palace consumer call-sites
  - citation: palace/linalg/chebyshev.cpp:101-110
    verdict: supports-with-citation-hygiene-note
    audited_at: 2026-05-30T220500Z
    note: ApplyOrder0<true> Transpose=true else-branch is template-dead; the precise else-block body is :102-110 — the cited :101-110 includes line 101 (closing brace of the if (!Transpose) branch) as containing context which is acceptable but slightly overcaptures; codemap search_text ApplyOrder0<true> returns zero hits; palace/linalg/chebyshev.hpp:73-76 MultTranspose2 self-aliases to Mult2 with comment Assumes operator symmetry
  - citation: palace/linalg/chebyshev.cpp:150-159
    verdict: supports-with-citation-hygiene-note
    audited_at: 2026-05-30T220500Z
    note: ApplyOrderK<true> Transpose=true else-branch is template-dead; the precise else-block body is :147-155 — the cited :150-159 overshoots by 3 lines on start (misses the else keyword and opening brace) and by 4 lines on end (includes the function closing brace plus blank+namespace closer); claim is still grounded since the kernel body lambda lines :152-153 sit inside the cited range; consider tightening to :147-155 in a future hygiene pass
  - citation: palace/linalg/chebyshev.hpp:73-76
    verdict: supports
    audited_at: 2026-05-30T220500Z
    note: ChebyshevSmoother MultTranspose2 inline override forwards to Mult2 — symmetric-wiring alias for the 4th-kind smoother
  - citation: palace/linalg/chebyshev.hpp:138-141
    verdict: supports
    audited_at: 2026-05-30T220500Z
    note: ChebyshevSmoother1stKind MultTranspose2 inline override forwards to Mult2 — symmetric-wiring alias for the 1st-kind smoother covers the same dead-code conclusion
  - citation: palace/linalg/vector.hpp:118
    verdict: does-not-support-planner-mischaracterization
    audited_at: 2026-05-30T220500Z
    note: planner scope listed ComplexVector::Subtract variant forms as the axpby cohort sibling of the jacobi/chebyshev dead-code complex-TRANSPOSE kernels; Subtract is NOT a transpose kernel — it is a defined-not-used in-place AXPY-with-negated-alpha wrapper Subtract(alpha,x){AXPY(-alpha,x);}; the axpby theme correctly records it as a recognition rule for potential call sites not as a dead transpose kernel; planner conflated two distinct shapes of dead code (template-dead Transpose=true branch vs defined-not-used member-API recognition rule); no caveat edit needed in the axpby theme
```

The above `verified_against:` block records the verdict for this audit. **NO theme edit is proposed** — these entries are for the audit report; they may be optionally appended to the respective theme files by `integrator-per-report` if the integrator deems this audit's verdicts worth carrying forward into each theme's running `verified_against:` block. I have not emitted a proposed-changes `edit:` block because all three themes' caveats are already correct as-stated; the verdicts here serve as an audit-trail record rather than a chapter-level edit.

## Supporting evidence

- `palace/linalg/jacobi.cpp:30-71` — real + complex `Apply` templates (the kernels under audit).
- `palace/linalg/jacobi.cpp:102-105` — `JacobiSmoother::Mult` body; the sole `Apply` call site, template arg omitted.
- `palace/linalg/jacobi.hpp:39-44` — `Mult` / `MultTranspose` overrides; `MultTranspose` is the inline self-alias.
- `palace/linalg/chebyshev.cpp:81-156` — `ApplyOrder0` and `ApplyOrderK` template definitions for both real and complex.
- `palace/linalg/chebyshev.cpp:191-220` — `ChebyshevSmoother::Mult2`; calls `ApplyOrder0`/`ApplyOrderK` without template arg.
- `palace/linalg/chebyshev.cpp:261-293` — `ChebyshevSmoother1stKind::Mult2`; same pattern.
- `palace/linalg/chebyshev.hpp:50-76` — `ChebyshevSmoother` class; `MultTranspose2 → Mult2`.
- `palace/linalg/chebyshev.hpp:110-142` — `ChebyshevSmoother1stKind` class; `MultTranspose2 → Mult2`.
- `palace/linalg/vector.hpp:115-128` — `ComplexVector::AXPY` / `Add` / `Subtract` / `operator±=` member API (the "defined-not-used recognition rules" the axpby theme cites).
- `palace/linalg/vector.cpp:313-379` — `ComplexVector::AXPBY` both signatures (the in-place AXPBY implementation; non-transpose, no `Transpose` template axis).
- `palace/linalg/vector.cpp:713-743` — `linalg::AXPY` / `AXPBY` free-function specialisations (the complex-`α` overloads the axpby theme cites as recognition rules).
- `book/src/L1-L0/jacobi-smoother-mutation-rotation.md:144, 191-193, 222, 310-336, 569-600` — jacobi caveat sites (all checked; all present and accurate).
- `book/src/L1-L0/chebyshev-smoother-mutation-rotation.md:134-156, 239-243, 353-355, 371-373` — chebyshev caveat sites (all checked; all present and accurate).
- `book/src/L1-L0/axpby-mutation-rotation.md:215-238` — axpby "defined-not-used recognition rule" framing (correct as-stated; not a transpose kernel).
- Citecheck runs (representative):
  - `python3 tools/citecheck/citecheck.py reference/palace/palace/linalg/jacobi.cpp:61-69 --anchor 'DIR'` → OK; anchor at lines [66, 67] within range.
  - `python3 tools/citecheck/citecheck.py reference/palace/palace/linalg/chebyshev.cpp:101-110 --anchor 'else'` → OK; anchor at line [102] within range.
  - `python3 tools/citecheck/citecheck.py reference/palace/palace/linalg/chebyshev.cpp:147-155 --anchor 'sd'` → OK; the body-precise range.
- Codemap negative-finding queries:
  - `get_call_sites("Apply")` → one site: `jacobi.cpp:103`.
  - `search_text("Apply<true>")` → zero hits.
  - `search_text("ApplyOrder0<true>")` → zero hits.
  - `search_text("ApplyOrderK<true>")` → zero hits.
  - `get_call_sites("Subtract")` → zero sites.
  - `search_text("\.Subtract\s*\(")` → zero hits.

## Open questions / caveats

- **OQ resolution**: the motivating OQ `jacobi-mutation-rotation-dead-code-complex-transpose-kernel-lowering-verifier-audit` (filed cycle-033 D1) is **resolved by this audit**. Routed to integrator-per-report for closure with disposition `resolved`. The audit confirms all three caveats are correctly recorded with one minor citation-hygiene observation on the chebyshev `:150-159` range.
- **Citation-hygiene follow-up (low-priority)**: the chebyshev theme's `:150-159` citation could be tightened to `:147-155` for body-precision. Optional; the claim is still well-grounded under the loose range. Filing as a new OQ `chebyshev-smoother-mutation-rotation-applyorderk-true-citation-tighten` — low fan-out, hygiene-only.
- **Planner-scope-framing note (for cycle-034 meta-phase)**: the cycle-034 dispatch scope conflated two distinct shapes of dead code under one umbrella (the template-dead `Transpose=true` branch in jacobi/chebyshev kernels vs. the defined-not-used member-API recognition rules in axpby). The umbrella is plausible — both are "dead code in Palace consumer call-sites" — but the underlying mechanism differs (compiler-elided template specialisation vs. unused symbol definitions). Recommend the meta-phase note this as a planner-scope-precision observation. Not a friction-ledger entry (too low-grade); just a callout for batch-9 meta or cycle-034's own meta-phase if the same conflation recurs.
