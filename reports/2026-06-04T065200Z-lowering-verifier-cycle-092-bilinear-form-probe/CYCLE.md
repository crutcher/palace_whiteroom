---
agent: lowering-verifier
invoked_at: 2026-06-04T065200Z
scope: L1 operator firmability dischargeability probe — bilinear-form
status: pending
inputs:
  - book/src/L1/bilinear-form.md
  - palace/linalg/operator.cpp:621-639 (matrix-weighted Dot overload bodies)
  - palace/linalg/operator.hpp:385-394 (decls + yᴴ A x comment)
  - palace/models/boundarymodeoperator.cpp:85 (Hermitian-M y=x use site)
  - palace/models/boundarymodeoperator.cpp:90 (non-Hermitian-M use site)
  - book/src/L1/dot.md (firm constituent)
  - book/src/L1/apply_linop.md (firm constituent)
  - book/src/L1/matrix-weighted-norm.md (firm c091 SPD-diagonal sibling)
integrated_at: 2026-06-04T080000Z
integration_commit: 7604c43dbd46e9dc645d458e45173a484a488364
integration_notes: |
  cycle-092 (batch-29 position 2/3). Applied clean by integrator-per-report; verdict DISCHARGE.
  §Status of book/src/L1/bilinear-form.md narrowed to record the cycle-092 firm-on-positive-structure
  DISCHARGE + a 9-entry verified_against: block appended (8 supports + 1 partially-supports). The verb
  STAYS rough-in BY DESIGN (frontmatter firmness:rough-in UNFLIPPED — the probe is the gate-TEST; the
  firm flip is the separate gated c093/batch-30 cascade wave). Repair FIRED pre-integration (one
  prose-only OOB citation misattribution fixed: matrix-weighted-norm.md:251-257 -> bilinear-form.md:251-257);
  the proposed-changes block itself was clean. The per-report integrator additionally corrected one in-edit
  L0 anchor :386-394 -> :385-394 to match the report's own verified line-range. No cascade / no out-of-scope
  touch (book/src/L1/bilinear-form.md ONLY). Promoted OQ bilinear-form-firm-flip-and-cascade-wave (the
  c093/batch-30 candidate). Build exit 0, zero dead links, no finalize build-repair. A law-confidence STATE
  ADVANCE, NOT a count flip.
---

# CYCLE: Audit bilinear-form (firmability dischargeability probe)

## Summary

This is a SCOPED dischargeability probe (the c088/c089 matrix-weighted-norm pattern) on the
L1 `bilinear-form` operator — currently `rough-in (lower-layer-shared-vocabulary,
cycle-010-wave-1)` on disk (frontmatter `:4`; §Status `:323`) — the sole residual gate on
`gram_reduce` (rough-in) and 4 stay-seed feature columns
(capacitance/inductance/electrostatic/magnetostatic). The ONLY question is whether
`bilinear-form` can be discharged to `firm` via the **firm-on-positive-structure escape**
WITHOUT a dedicated positive test at the 4-arg matrix-weighted `Dot` overload entry point.

**Verdict: DISCHARGE.** The escape applies. Laws 1-6 (`:182-201`) are pure
linearity/annihilation/identity-specialisation — syntactic read-off compositions of the firm
`dot` + firm `apply_linop` laws, with ZERO inner-product-norm THEOREM content (materially
cleaner than `matrix-weighted-norm`, whose gating laws WERE norm-axiom theorems needing two
probes). Laws 7/8 (`:205-220`) are M-symmetry-CONDITIONAL with both witnesses on-disk (`Bttr`
Hermitian `:85`, `Atn` non-Hermitian `:90` — both confirmed real on disk this cycle); law 8's
positivity content is the SPD diagonal `bilinear_form(x,B,x)` that the firm `matrix-weighted-norm`
sibling (c091) already discharged. The "narrow variant-axis coverage from 2 use sites" gate is
genuinely REDUNDANT under the escape — the missing test would only re-confirm an un-surfaced
real-M-real-y shape (which Palace does NOT surface at all — `:85-89`) or re-confirm
already-inherited FP non-laws (`:229-234`). Per the c088/c089 discipline, I do NOT flip the
frontmatter and do NOT trigger the cascade; I propose a `verified_against:` block + a §Status
narrowing, and RECOMMEND queuing `bilinear-form-firm-flip-and-cascade-wave` as a c093/batch-30
candidate.

## Per-citation audit

### Citation: palace/linalg/operator.cpp:621-639
- **Theme claim** (`:27-43`, `:298-300`, §Evidence `:384-388`): the two matrix-weighted `Dot`
  overload bodies allocate a workspace `ComplexVector Ax(A.Height())`, write `A·x` into it
  (real-A overload splits `x` into Real/Imag and applies `A` to each; complex-A overload calls
  `A.Mult(x, Ax)` directly), then return `Dot(comm, Ax, y)`.
- **Found** (read on disk + `citecheck --anchor 'Dot'` → `[ok]`, anchor at 621/628/631/637): EXACT
  match. `:621-629` real-A: `ComplexVector Ax(A.Height()); Ax.UseDevice(true); A.Mult(x.Real(),
  Ax.Real()); A.Mult(x.Imag(), Ax.Imag()); return Dot(comm, Ax, y);`. `:631-639` complex-A:
  `ComplexVector Ax(A.Height()); Ax.UseDevice(true); A.Mult(x, Ax); return Dot(comm, Ax, y);`.
- **Verdict**: supports. The closed-form L1 `xᴴ M y` = `dot(x, apply_linop(M, y))` is a SYNTACTIC
  composition of the two firm constituents; the L0 body realises exactly that composition (modulo
  the second-argument-conjugation lowering reconciliation the chapter already documents `:119-145`).
- **Notes**: the finer §Evidence sub-ranges `:621-629`/`:631-639` reconcile with the §Context
  enclosing `:621-639` — same block, split by overload. No drift.

### Citation: palace/linalg/operator.hpp:385-394
- **Theme claim** (`:28`, `:155-158`, §Evidence `:380-383`): two `linalg::Dot(comm, x, A, y)`
  overload declarations (real-`A` at 388-389, complex-`A` at 393-394) with the comment at line 386
  documenting the form as `yᴴ A x`; the comment matches the impl (no comment-vs-impl ambiguity).
- **Found** (read on disk + `citecheck --anchor 'bilinear form'` → `[ok]`, anchor at 386/391): EXACT.
  Line 386 `// Compute the bilinear form inner product yᴴ A x for a real operator A and complex
  vectors.`; decls at 388-389 (`const Operator &A`) and 393-394 (`const ComplexOperator &A`).
- **Verdict**: supports. The comment `yᴴ A x` matches the impl (`Dot(comm, Ax, y)` with the
  free-function's second-arg conjugation = `yᴴ A x`). The §Context `:28` cite of `:386-394` and the
  §Evidence `:380-383` cite of `:385-394` both land correctly (the `:385` start is the blank line /
  comment boundary; `:386` is the comment line).
- **Notes**: the alleged "second gating reason" (comment-vs-impl conjugation disagreement) was
  already disproven and removed (`:336-346`, `:155-158`); I independently re-confirmed the L0 source
  is self-consistent. NOT a gate.

### Citation: palace/models/boundarymodeoperator.cpp:85
- **Theme claim** (`:209-211`, §Evidence `:396-402`, §Variant-axes `:278`): Hermitian-`M` use site
  `linalg::Dot(comm, et, *Bttr, et)` — the Poynting-power contribution, `Bttr` a symmetric mass
  matrix; a `y=x` form anchoring law 8's PSD-at-`y=x` / Cauchy-Schwarz-tight case.
- **Found** (read on disk): EXACT. `:85` = `std::complex<double> P = 0.5 * std::conj(kn) / omega *
  linalg::Dot(comm, et, *Bttr, et);`. The call is `bilinear_form(et, Bttr, et)` — a genuine `y=x`
  matrix-weighted form with a Hermitian (symmetric mass-matrix) weight.
- **Verdict**: supports. Anchors law 7's Hermitian branch AND law 8's PSD-at-`y=x` diagonal case.
- **Notes**: this is a `y=x` site — directly relevant to the §Status claim that "Cauchy-Schwarz at
  `y=x` is unexercised". The PSD-at-`y=x` *positivity* is what `matrix-weighted-norm` already firmed.

### Citation: palace/models/boundarymodeoperator.cpp:90
- **Theme claim** (`:212-213`, §Evidence `:403-408`, "Laws that do not hold" `:224-228`):
  non-Hermitian-`M` use site `linalg::Dot(comm, en, Atn, et)` — `Atn` a `ComplexWrapperOperator`
  around a non-symmetric MFEM `HypreParMatrix`; the witness for the general-`M` asymmetry non-law.
- **Found** (read on disk): EXACT. `:88-90` constructs `ComplexWrapperOperator Atn(...)` from
  `Atnr`/`Atni` HypreParMatrix pointers, then `:90` = `P += std::complex<double>(0.0, 1.0) / (2.0 *
  omega) * linalg::Dot(comm, en, Atn, et);`. The weight is genuinely non-Hermitian and the call
  arguments `en`/`et` differ (not a `y=x` form).
- **Verdict**: supports. Anchors law 7's non-Hermitian branch (the conditional law's premise FAILS
  here) and the "general-`M` symmetry does not hold" non-law (`:224-228`).
- **Notes**: confirms the M-symmetry-property axis has TWO genuine witnesses (one each branch) — so
  the conditional laws 7/8 are anchored, not speculative.

### Citation: book/src/L1/dot.md (firm constituent)
- **Theme claim**: bilinear-form laws 1 (conj-linearity in `x`) and 7 (Hermitian symmetry) are
  inherited from `dot`'s firm conjugate-linearity-left + Hermitian-symmetry laws.
- **Found** (read on disk): `dot.md:65` law 6 `dot(x,y) = conj(dot(y,x))` (Hermitian symmetry);
  `:66` law 7 `dot(α·x₁+x₂, y) = conj(α)·dot(x₁,y) + dot(x₂,y)` (conjugate-linearity left); §Status
  `:100` `firm`. CONFIRMED firm + the cited laws present.
- **Verdict**: supports. The inherited-law chain is real and the source is firm.

### Citation: book/src/L1/apply_linop.md (firm constituent)
- **Theme claim**: bilinear-form laws 2 (linearity in `y`) and 3 (operator-side bilinearity) are
  inherited from `apply_linop`'s firm linearity + operator-side linearity (laws 5, 6).
- **Found** (read on disk): `apply_linop.md:50` law 1 linearity in `x`; `:54` law 5 sum-operator
  distributes; `:55` law 6 scaled-operator scalar absorption; §Status `:87` `firm`. CONFIRMED.
- **Verdict**: supports. `apply_linop(M, α·y₁+y₂) = α·M y₁ + M y₂` (law 1) composes with `dot`
  linearity-in-2nd-arg to give bilinear-form law 2; `apply_linop` laws 5/6 give bilinear-form law 3.

### Citation: book/src/L1/matrix-weighted-norm.md (firm c091, SPD-diagonal sibling)
- **Theme claim** (`bilinear-form.md:251-257`): `matrix-weighted-norm` is the SPD `y=x` sibling
  `nrm2_B(x,B) = √bilinear_form(x,B,x)`; its `matrix-weighted-norm` half of the shared OQ is now
  resolved (promoted firm c091).
- **Found** (read on disk): §Status `:108-115` `firm` — promoted c091 via the batch-28 meta-phase GO;
  explicitly discharges the SAME 4-arg-overload no-test gate (a) as REDUNDANT under the
  firm-on-positive-structure escape, citing the c082/c083/c086/`apply_linop` prior promotions.
- **Verdict**: supports. This is the directly-applicable prior: the SPD-diagonal positivity content
  (bilinear-form law 8) is already firm in the sibling — bilinear-form does not re-establish it.

## Applicability conditions

Walking each condition the theme states (`:305-319`):

- **Condition**: `M` must be a linear operator (nonlinear weights unsupported).
  **Verifiable**: yes — `apply_linop` (firm) is defined only for linear `M` (its law 1 IS linearity,
  `apply_linop.md:36, 50`). **Counter-example?**: no.
- **Condition**: `M`'s codomain axis matches `x`'s length axis; domain axis matches `y`'s.
  **Verifiable**: yes — the L0 `Ax(A.Height())` allocation + `A.Mult(x,...)` / `Dot(comm,Ax,y)`
  composition enforce exactly these shape contracts (`operator.cpp:624-628/634-637`).
  **Counter-example?**: no.
- **Condition**: **No SPD requirement on `M`** — well-defined for any linear `M`; laws 7/8 hold
  *conditionally* on M-symmetry. **Verifiable**: yes — the non-Hermitian witness `Atn` (`:90`) proves
  the operator IS applied to non-symmetric `M`, so the no-SPD-requirement claim is positively
  witnessed. **Counter-example?**: no — this is the load-bearing distinction from `matrix-weighted-norm`
  (which DOES require SPD because of its √-step); bilinear-form correctly carries no such requirement.
- **Condition**: element types of `x`, `M`, `y` compatible per the §Signature table.
  **Verifiable**: yes — the two L0 overloads (real-`A`, complex-`A`, both against complex vectors)
  are the only surfaced element-type combinations; the real-`M`-real-`y` `xᵀMy` row is explicitly
  NOT surfaced (`:85-89`). **Counter-example?**: no.

No applicability condition is contradicted by the cited evidence.

## Algebraic laws (cited)

For each law: does it hold on the operators per the firm constituent signatures, and is it
syntactic-identity content (escape applies) or norm-axiom-theorem content (escape does NOT cover)?

- **Law 1 (conjugate-linearity in `x`, `:182-184`)**: HOLDS. `bf(α·x₁+x₂, M, y) = dot(α·x₁+x₂, My)`
  = (dot law 7 `dot.md:66`) `conj(α)·dot(x₁,My) + dot(x₂,My)`. **Syntactic read-off** of dot law 7.
  Escape applies.
- **Law 2 (linearity in `y`, `:185-187`)**: HOLDS. `bf(x,M,α·y₁+y₂) = dot(x, M(α·y₁+y₂))` =
  (apply_linop law 1 `apply_linop.md:50`) `dot(x, α·My₁+My₂)` = (dot linearity-in-2nd) `α·dot(x,My₁)
  + dot(x,My₂)`. **Syntactic composition** of apply_linop law 1 + dot linearity. Escape applies.
- **Law 3 (operator-side bilinearity, `:188-191`)**: HOLDS. `bf(x, α·M₁+M₂, y) = dot(x,
  (α·M₁+M₂)y)` = (apply_linop laws 5+6 `apply_linop.md:54-55`) `dot(x, α·M₁y+M₂y)` =
  `α·dot(x,M₁y)+dot(x,M₂y)`. **Syntactic read-off**. Escape applies.
- **Law 4 (zero-vector annihilation, `:192-194`)**: HOLDS as corollary of laws 1,2 at zero
  coefficient. **Syntactic**. Escape applies.
- **Law 5 (zero-operator annihilation, `:195-196`)**: HOLDS as corollary of law 3 at α=0, M₂=0.
  **Syntactic**. Escape applies.
- **Law 6 (identity-weight specialisation, `:197-201`)**: HOLDS. `bf(x,I,y) = dot(x, apply_linop(I,y))
  = dot(x,y)` since `apply_linop(I,y)=y` (identity is the unit linear map). **Definitional /
  syntactic**. Escape applies. (This is the load-bearing `dot(x,y)=bf(x,I,y)` subsumption identity.)
- **Law 7 (Hermitian-`M` symmetry, `:205-213`)**: HOLDS **conditionally** under premise `Mᴴ=M`:
  `conj(bf(y,M,x)) = conj(yᴴMx) = xᴴMᴴy = xᴴMy = bf(x,M,y)`. **Conditional syntactic identity** under
  a STATED premise (the matrix-weighted analogue of dot law 6 Hermitian-symmetry). Both branches
  witnessed on-disk (`Bttr` `:85`, `Atn` `:90`). Escape applies (conditional-law + premise-guard,
  exactly the matrix-weighted-norm structure-side disposition). NOT a norm-axiom theorem.
- **Law 8 (PSD at `y=x` for SPD `M`, `:214-220`)**: HOLDS **conditionally** under premise `M` SPD:
  `bf(x,M,x) = xᴴMx ∈ ℝ, ≥0`. This is the ONLY law with genuine inner-product-NORM-axiom (positivity)
  content — BUT (i) it is premise-guarded (M SPD), not an unconditional claim; (ii) the SPD-diagonal
  `xᴴBx≥0` is precisely what the firm `matrix-weighted-norm` sibling (c091) already discharged via
  its structure-side probe c088; (iii) it has an on-disk `y=x` witness (`Bttr` `:85`). So law 8's
  theorem content does NOT introduce an independent gate — it is inherited from the firm sibling for
  the SPD-restricted diagonal and stated conditionally for the general entry. Escape covers it.

**Conclusion on the escape question**: laws 1-6 are pure linearity syntactic read-offs over firm
`dot`+`apply_linop` (the `apply_linop`/`solve_family`/`matrix-weighted-norm` firm-on-positive-structure
class) with NO norm-axiom theorem content; laws 7/8 are conditional with on-disk witnesses, and law
8's sole positivity content is the firm-sibling-inherited SPD diagonal. NO law carries semantic
content the escape does not cover. The "narrow variant-axis coverage from 2 use sites" gate is
REDUNDANT: a real-M-real-y test cannot exist (the shape is un-surfaced by Palace, `:85-89`), and
Cauchy-Schwarz at `y=x` is a FP-strictness non-law already inherited from `dot` + `apply_linop`
(`:229-234`) — a test would only re-confirm already-anchored properties, establishing nothing
independent. **DISCHARGE.**

## Independent on-disk re-confirmations (no-drift duty)

- `operator.cpp:621-639` — read on disk + `citecheck --anchor 'Dot'` → `[ok]` (621/628/631/637).
- `operator.hpp:385-394` — read on disk + `citecheck --anchor 'bilinear form'` → `[ok]` (386/391).
- `boundarymodeoperator.cpp:85`/`:90` — read on disk; both verbatim (`*Bttr` Hermitian y=x; `Atn`
  `ComplexWrapperOperator` non-Hermitian).
- **2-call-site count**: `grep -rn 'linalg::Dot(' palace/ | grep -v test/` → exactly 2 hits with the
  4-arg matrix-weighted signature (`boundarymodeoperator.cpp:85`/`:90`); ALL other `linalg::Dot`
  hits across `postoperator.cpp`/`nleps.cpp`/`iterative.cpp` are the 3-arg unweighted overload.
  CONFIRMED on-disk-accurate.
- **No-test claim**: `grep -rn 'linalg::Dot' test/unit/` → all hits (`test-romoperator.cpp`,
  `test-orthog.cpp`) are 3-arg unweighted; no 4-arg matrix-weighted exercise; no `*bilinearform*`
  test file. The direct-positive-test promotion route is genuinely ABSENT — the same situation as
  matrix-weighted-norm's gate (a). CONFIRMED.
- Constituent firmness: `dot.md:100` firm; `apply_linop.md:87` firm; `matrix-weighted-norm.md:108`
  firm (c091). All three CONFIRMED firm on-disk.

## Proposed changes

Two edits to `book/src/L1/bilinear-form.md` ONLY (per the hard constraint — NO frontmatter
`status:`/`firmness:` flip, NO cascade, NO touch to `gram_reduce`/feature columns/the L1>L0 theme).

### Edit 1 — append a `verified_against:` block at end of file

```edit:book/src/L1/bilinear-form.md
[append at end of file]
```yaml
verified_against:
  - citation: palace/linalg/operator.cpp:621-639
    verdict: supports
    audited_at: 2026-06-04T065200Z
    note: both matrix-weighted Dot overload bodies (real-A split real/imag + Dot(comm,Ax,y); complex-A direct A.Mult + Dot(comm,Ax,y)) confirmed verbatim on disk; the closed-form xᴴ M y = dot(x, apply_linop(M, y)) is a syntactic composition of firm dot + firm apply_linop
  - citation: palace/linalg/operator.hpp:385-394
    verdict: supports
    audited_at: 2026-06-04T065200Z
    note: two decls + the yᴴ A x comment (line 386) confirmed verbatim; matches the impl, no comment-vs-impl conjugation ambiguity
  - citation: palace/models/boundarymodeoperator.cpp:85
    verdict: supports
    audited_at: 2026-06-04T065200Z
    note: Hermitian-M y=x witness Dot(comm, et, *Bttr, et) confirmed on disk; anchors law 7 Hermitian branch + law 8 PSD-at-y=x diagonal case
  - citation: palace/models/boundarymodeoperator.cpp:90
    verdict: supports
    audited_at: 2026-06-04T065200Z
    note: non-Hermitian-M witness Dot(comm, en, Atn, et) with Atn a ComplexWrapperOperator over a non-symmetric HypreParMatrix confirmed on disk; anchors law 7 non-Hermitian branch (the general-M-asymmetry non-law)
  - citation: book/src/L1/dot.md:65-66
    verdict: supports
    audited_at: 2026-06-04T065200Z
    note: dot firm Hermitian-symmetry (law 6) + conjugate-linearity-left (law 7) are the inherited sources for bilinear-form laws 1 and 7; dot Status firm confirmed at dot.md:100
  - citation: book/src/L1/apply_linop.md:50-55
    verdict: supports
    audited_at: 2026-06-04T065200Z
    note: apply_linop firm linearity (law 1) + operator-side linearity (laws 5,6) are the inherited sources for bilinear-form laws 2 and 3; apply_linop Status firm confirmed at apply_linop.md:87
  - citation: book/src/L1/matrix-weighted-norm.md:108-115
    verdict: supports
    audited_at: 2026-06-04T065200Z
    note: matrix-weighted-norm firm c091 is the SPD diagonal sibling bilinear_form(x,B,x); its discharge of the same 4-arg-overload no-test gate (a) as REDUNDANT under the firm-on-positive-structure escape is the directly-applicable prior for law 8 PSD content
  - citation: book/src/L1/bilinear-form.md:182-201
    verdict: supports
    audited_at: 2026-06-04T065200Z
    note: laws 1-6 are pure linearity/annihilation/identity-specialisation - syntactic read-offs over firm dot + apply_linop with NO norm-axiom theorem content; the firm-on-positive-structure escape applies directly
  - citation: book/src/L1/bilinear-form.md:205-220
    verdict: partially-supports
    audited_at: 2026-06-04T065200Z
    note: laws 7,8 are M-symmetry-CONDITIONAL with both witnesses on-disk (Bttr Hermitian, Atn non-Hermitian); law 8 positivity content is the SPD diagonal already discharged by the firm matrix-weighted-norm sibling - conditional, not an independent gate
```
```

### Edit 2 — narrow the §Status to record the discharge (do NOT flip the maturity token)

Replace the §Status promotion-gate paragraph (`:323-335`, the lines from "`rough-in
(lower-layer-shared-vocabulary, cycle-010-wave-1)` — the structural" through the end of the
numbered gate item 1 at "...Cauchy–Schwarz at `y = x` is unexercised.") with the text below.
The maturity token STAYS `rough-in` per the c088/c089 discipline (the firm flip is a separate
gated wave). The existing cycle-010 critic repair-note paragraph (`:336-346`) is retained
unchanged below the new text.

```edit:book/src/L1/bilinear-form.md
[replace lines 323-335]
`rough-in (lower-layer-shared-vocabulary, cycle-010-wave-1)` — the structural
signature is anchored at L0 (`palace/linalg/operator.hpp:385-394`,
`palace/linalg/operator.cpp:621-639`), and the laws are inherited cleanly
from the firm L1 dependencies `dot` and `apply_linop`.

**Firmability discharged (cycle-092 dischargeability probe; `verified_against:`
block below).** A scoped `lowering-verifier` probe (the c088/c089
`matrix-weighted-norm` pattern) judged that the **firm-on-positive-structure
escape** (CLAUDE.md §Methodology invariants, the `rough-in
(test-coverage-bounded)` bullet) APPLIES to this operator:

1. **Laws 1-6 (`:182-201`) are syntactic read-offs over firm constituents.**
   They are pure linearity / annihilation / identity-specialisation —
   `bilinear_form(x, M, y) = dot(x, apply_linop(M, y))` is a syntactic
   composition of the firm `dot` (`book/src/L1/dot.md:100` firm) and firm
   `apply_linop` (`book/src/L1/apply_linop.md:87` firm) laws, with **NO
   inner-product-norm theorem content**. This is materially cleaner than
   `matrix-weighted-norm` was (whose gating laws WERE norm-axiom theorems
   — triangle / Cauchy–Schwarz / parallelogram — needing two probes c088+c089);
   `bilinear-form` has none. The escape promotes laws that are
   syntactic-identity content on fully-specified positive source even with no
   surrounding test (the `apply_linop` / `solve_family` c086 /
   `eigenfreq_qfactor_reduce` c082 / `sparameter_reduce` c083 /
   `matrix-weighted-norm` c091 precedents).
2. **Laws 7-8 (`:205-220`) are M-symmetry-CONDITIONAL with both witnesses
   on-disk.** Law 7 (Hermitian symmetry under `Mᴴ = M`) and law 8 (PSD at
   `y = x` for SPD `M`) are premise-guarded conditional identities; both
   branches are positively witnessed — Hermitian `Bttr`
   (`palace/models/boundarymodeoperator.cpp:85`, a `y = x` form) and
   non-Hermitian `Atn` (`palace/models/boundarymodeoperator.cpp:90`). Law 8's
   sole positivity content is the SPD-diagonal `xᴴ B x ≥ 0`, which the firm
   `matrix-weighted-norm` sibling (c091) already discharged via its
   structure-side probe c088 — it is inherited, not an independent gate.
3. **The narrow-variant-axis-coverage gate is REDUNDANT under the escape.**
   The two surfaced use sites are the only matrix-weighted `Dot` call sites in
   the whole tree (`grep` confirms exactly 2: `boundarymodeoperator.cpp:85`/`:90`),
   and no `test/unit/*` exercises the 4-arg overload (the direct-test route is
   genuinely absent — the same situation as `matrix-weighted-norm`'s gate (a),
   which the batch-28 meta-phase judged REDUNDANT). The one shape the coverage
   gate names — real-`M`-real-`y` `xᵀ M y` — is **not surfaced by Palace at
   all** (`:85-89`); a test of it cannot exist and would only confirm a
   hypothetical extension. Cauchy–Schwarz at `y = x` is a floating-point
   strictness **non-law** (`:229-234`) already inherited from `dot` +
   `apply_linop`; a test would only re-confirm an already-anchored property.

**The maturity token stays `rough-in` in THIS dispatch by design** (the
c088/c089 discipline): the probe is the gate-TEST, and the firm flip + the
coupled `gram_reduce` firm re-judgment + the 4-column
(capacitance/inductance/electrostatic/magnetostatic) unblock + the ~30-file
cross-reference re-anchor is a **separate gated wave**
(`bilinear-form-firm-flip-and-cascade-wave`, a c093/batch-30 candidate). What
this probe establishes: the verb IS firmable via the escape; nothing
structural blocks it; the residual coverage gate is redundant.
```

(The `~~~`-vs-backtick note: the actual edit emits standard triple-backtick fences for the
```yaml``` block; the YAML content was validated with `python3 -c "import yaml;
yaml.safe_load(...)"` → 9 entries, clean parse, no leading-quote `note:` violations.)

## Supporting evidence

- `palace/linalg/operator.cpp:621-639` — matrix-weighted `Dot` overload bodies (read + citecheck).
- `palace/linalg/operator.hpp:385-394` — decls + `yᴴ A x` comment line 386 (read + citecheck).
- `palace/models/boundarymodeoperator.cpp:85`/`:90` — the 2 use sites (read on disk).
- `palace/linalg/nleps.cpp:675` + `postoperator.cpp` + `iterative.cpp` — confirmed all unweighted
  3-arg `Dot`, not matrix-weighted (the 2-call-site count is exact).
- `test/unit/test-orthog.cpp`, `test/unit/test-romoperator.cpp` — only 3-arg `Dot` (no-test claim).
- `book/src/L1/dot.md:65-66, 100` — firm constituent, inherited laws.
- `book/src/L1/apply_linop.md:50-55, 87` — firm constituent, inherited laws.
- `book/src/L1/matrix-weighted-norm.md:108-115` — firm c091 SPD-diagonal sibling; the directly-
  applicable escape prior.

## Open questions / caveats

- **RECOMMENDATION — queue `bilinear-form-firm-flip-and-cascade-wave` as a c093/batch-30 candidate.**
  This probe DISCHARGES: `bilinear-form` is firmable via the firm-on-positive-structure escape. Per
  the hard constraint I did NOT flip the maturity and did NOT trigger the cascade. The follow-up
  gated wave (which a c093 planner / the batch-29 meta-phase should schedule) is: (i) flip
  `bilinear-form` frontmatter `firmness: rough-in` → `firm` + drop the rough-in token in §Status;
  (ii) the coupled `gram_reduce` firm re-judgment (its SOLE residual gate clears — the escape applies
  exactly as it did for its reduce-verb siblings `domain_energy_reduce` c091 / `eigenfreq_qfactor_reduce`
  c082 / `sparameter_reduce` c083); (iii) the 4-column re-evaluation
  (capacitance/inductance/electrostatic/magnetostatic flip seed→firm under the OWN-COMPOSITION rule
  once `gram_reduce` firms); (iv) the whole-book cross-reference re-anchor.

- **Whole-book cross-reference residue the firm flip will stale (enumerated, NOT touched this
  dispatch).** Per the firm-promotion-coupled-re-anchor guard, I ran `grep -rln 'bilinear-form'
  book/src` — the flip will stale ~30 files. The genuinely-stale-on-flip set (files asserting
  `bilinear-form`'s OWN maturity at the rough-in token, vs files that correctly mention a still-rough-in
  *consumer*) MUST be judged by the cascade-wave lifter, not me (I am scoped to the operator's own
  file ONLY). The convergent consumer cluster to re-judge: `feature/capacitance.L1.md:33,35` (calls
  `bilinear-form` "rough-in"), the other 3 feature `*.L1.md`/`*.L0.md`/`*.L4.md` column files,
  `L4/gram_reduce.md`, `L4/domain_energy_reduce.md`, `L2/gram.md`, `L2/inner_product.md`,
  `L2-L1/gram-fold-specialization.md`, `L2-L1/inner-product-fold-specialization.md`, `L1/index.md`
  (dep-map + count headers), `L1-L0/bilinear-form-mutation-rotation.md` (the firm L1>L0 theme — verify
  it does not assert the OPERATOR rough-in). This enumeration is for the cascade-wave planner; I do
  NOT edit any of them.

- **`bilinear-form.md:251-257` self-note (in the bilinear-form Dependencies §, NOT touched):**
  the existing text already says "the `bilinear-form` half remains open"; on the firm flip the
  cascade lifter should update that clause. Flagged, not edited (out of my single-file scope).

- **No direction-of-definition violation.** The theme narrates L1 forward (the L1 closed-form `xᴴ M y`
  defined in L1 vocabulary; the L1>L0 composition is correctly framed as a lowering PREVIEW, `:111-117`,
  not a reverse-direction definition). Clean.
