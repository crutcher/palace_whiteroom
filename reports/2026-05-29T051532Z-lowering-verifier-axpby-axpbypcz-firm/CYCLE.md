---
agent: lowering-verifier
invoked_at: 2026-05-29T05:22:35Z
scope: L1>L0 theme audit — axpby-mutation-rotation + axpbypcz-mutation-rotation (BLAS-1 lowering floor closure)
status: integrated
integrated_at: 2026-05-29T06:14:03Z
integration_commit: 881f200
integration_notes: "cycle-021 finalize (staging row #3; status partially-applied BY DESIGN — SPLIT verdict). Theme 1 axpby-mutation-rotation ENACTED firm (3 edits: re-audited fenced verified_against block — 9 anchors line-exact, refreshed 2026-05-27→2026-05-29 + romoperator/drivensolver corpus-census note; ## Status rough-in→firm; dep-map :18 row flipped firm + L0-anchor column expanded). Theme 2 axpbypcz-mutation-rotation GATED — auditor UNBLOCKED (drafted corrections (1)-(6) + verified_against + firm Status) but did NOT enact per the cycle-012 gated-promotion discipline; ZERO edits to axpbypcz file; routed to cycle-022 plan item axpbypcz-mutation-rotation-callsite-correction-and-firm (3 confirmed call-site classification errors: nleps.cpp:343-344 D→A, romoperator.cpp:188-189 D→A, slepc.cpp:1986 γ≠0→γ=0, all critic read_range-confirmed). BLAS-1 L1>L0 floor reaches 7/8 firm (axpbypcz remains rough-in); floor OQ NOT closed. L1>L0 themes 15→16. retroactive-budget 0; clean build."
inputs:
  - book/src/L1-L0/axpby-mutation-rotation.md
  - book/src/L1-L0/axpbypcz-mutation-rotation.md
  - book/src/L1/axpby.md (firm L1 anchor)
  - book/src/L1/axpbypcz.md (firm L1 anchor)
  - book/src/L1-L0/scal-mutation-rotation.md (firm-sibling shape reference, cycle-020)
  - book/src/L1-L0/index.md (dep-map)
  - L0 evidence: palace/linalg/vector.{hpp,cpp}, operator.cpp, rap.cpp, arpack.cpp,
    slepc.cpp, nleps.cpp, timeoperator.cpp, romoperator.cpp (all read_range-verified)
---

# CYCLE: Audit axpby-mutation-rotation + axpbypcz-mutation-rotation

## Summary

I audited the last two rough-in BLAS-1 L1>L0 lowering themes against their cited L0
evidence, independently `read_range`-confirming **every** anchor (decls, bodies,
kernels, and the full call-site corpus census for both AXPY and AXPBYPCZ).

**Verdicts split:**

- **`axpby-mutation-rotation` — fully-supported → PROPOSE FIRMING.** Every cited
  L0 range verifies line-exact. The cycle-003 `verified_against:` block holds under
  re-audit (all 9 anchors re-confirmed). The coverage note's defined-not-used claims
  (complex `linalg::AXPY` overload; `Subtract`/`operator-=`) are accurate — the
  `linalg::AXPY` corpus is exactly 5 sites, all `double` alpha. No contradictions.
  One pre-existing scope/naming nuance (the theme is *named* `axpby` but its body
  covers the **AXPY/`axpy`** family; `axpby`/`axpbypcz` appear only as forward refs)
  is flagged as a caveat, not a blocker.

- **`axpbypcz-mutation-rotation` — partially-supported → KEEP rough-in; firming
  GATED.** All decl/body/kernel citations verify line-exact and the structural
  decomposition (4 sub-patterns + γ==0 mixed-justification sub-rule) is sound. BUT
  **three call-site classifications are factually wrong** and the theme makes
  positive claims about observed γ≠0 sites that the corpus does not contain:
  1. `nleps.cpp:343-344` is classified **sub-pattern D (real-on-complex)**; it is
     actually **sub-pattern A (real-real)** — it passes `.Real()`/`.Imag()` *real*
     `Vector` halves, not `ComplexVector`s.
  2. `romoperator.cpp:188-189` — same error (classified D, is A; `V` is
     `std::vector<Vector>`, `u.Real()` is a `Vector` half).
  3. `slepc.cpp:1986` is classified **sub-pattern C, γ≠0 (runtime)**; it is actually
     **γ=0** (the 5th/γ argument is a literal `0.0`; the `−γ/σ` the theme read as γ
     is the **β** scalar in the 3rd slot).
  Net consequence the theme gets backwards: **sub-pattern D is defined-not-used
  (zero observed sites, same status as sub-pattern B), and NO observed call site
  exercises γ≠0 — every AXPBYPCZ site in the corpus uses literal γ=0.** A theme
  asserting observed γ≠0 / sub-pattern-D sites cannot be firmed as-written. I propose
  the exact corrections; firming is routed to a follow-up dispatch (abstractor/lifter)
  that applies them, then flips the status.

**BLAS-1 L1>L0 floor closure (`blas1-l1-l0-lowering-theme-gap`):** firming `axpby`
closes 7 of 8 BLAS-1 themes (dot/scal/nrm2/assemble-diagonal/axpby firm;
axpbypcz still rough-in pending the call-site corrections). The floor is **NOT yet
fully closed** — note for the meta-phase: one corrected-then-firmed dispatch on
`axpbypcz-mutation-rotation` closes it.

## Per-citation audit

### axpby-mutation-rotation

| Citation | Theme claim | Found (read_range) | Verdict |
|---|---|---|---|
| `vector.hpp:115-118` | ComplexVector AXPY/Add/Subtract decls; `Subtract(α,x){AXPY(-α,x);}` | L115 comment, L116 `AXPY`, L117 `Add{AXPY(α,x)}`, L118 `Subtract{AXPY(-α,x)}` — verbatim | supports |
| `vector.hpp:119-128` | `operator+=`→`AXPY(1.0,x)`; `operator-=`→`AXPY(-1.0,x)` | L119-123 `+=`, L124-128 `-=` — verbatim | supports |
| `vector.cpp:276-311` | ComplexVector::AXPY def; `ai==0` branch; no α==1 branch on complex path | L276-311 def; `if(ai==0.0)` two-real-kernel else complex-kernel; no α-value branch | supports |
| `vector.cpp:701-712` | free-fn real-Vector `if(alpha==1.0){y+=x;}else{y.Add(alpha,x);}` | L701 `template<>`, L702 sig, L704 `if(alpha==1.0)`, L706 `y+=x`, L710 `y.Add(alpha,x)`, L712 `}` — verbatim | supports |
| `vector.cpp:704-706` (sub-pat B) | `if(alpha==1.0){y += x;}` | exact (L704/706) | supports |
| `vector.cpp:714-718` | free-fn real-α-on-ComplexVector dispatches to member; no branch | L715 sig, L717 `y.AXPY(alpha,x)` | supports |
| `vector.cpp:720-724` (defined-not-used) | free-fn complex-α-on-ComplexVector; no branch; no caller | L721 sig, L723 `y.AXPY(alpha,x)`; corpus census of `linalg::AXPY` = 5 sites all `double` α → confirmed defined-not-used | supports (defined-not-used) |
| `operator.cpp:458-466` | `SumOperator::AddMult` `y.Add(a*c,z)` | L458 sig, L464 `y.Add(a*c,z)`, L466 `}`; transpose sibling `AddMultTranspose` L468-475 has identical `y.Add(a*c,z)` at L474 (uncited, as the existing note states) | supports |
| `rap.cpp:73` | `b.Add(-1.0,ty)` literal -1.0 (sub-pat C) | exact | supports |
| `rap.cpp:317` | `y.Add(a,ty)` runtime α (sub-pat A) | exact | supports |

All 9 verified_against anchors + the two inline sub-pattern anchors re-confirmed
line-exact. **No drift.** Note: the AXPY real-real free-function template spans
L701-712 (the cited range is exact); the `if(alpha==1.0)` test is at L704 (exact).

### axpbypcz-mutation-rotation

| Citation | Theme claim | Found (read_range) | Verdict |
|---|---|---|---|
| `vector.hpp:133-136` | member `AXPBYPCZ` decl + `(*this)=α·x+β·y+γ·(*this)` comment | L133 comment, L134-136 decl — verbatim | supports |
| `vector.hpp:313-316` | free-fn template decl `z=α·x+β·y+γ·z` | L313 comment, L314-316 decl — verbatim | supports |
| `vector.cpp:381-386` | outer member trampoline to static form on Real()/Imag() halves | L381-385 def (`AXPBYPCZ(...Real(),...Imag())` at L385), L386 blank — enclosing range OK | supports |
| `vector.cpp:388-455` | static member body; γ==0 outer branch; imaginary inner branches | L388-455 def; `if(gamma==0.0)` at L402; γ==0 path `Write` (L404-405, no prior-z read); γ≠0 path `ReadWrite` (L431-432); inner `ai==0&&bi==0` fast-paths both branches; γ≠0 adds `gi==0` to inner test (L433) — exactly as described | supports |
| `vector.cpp:402-426` (sub-pat C γ==0 branch) | γ==0 branch range | `if(gamma==0.0)` opens at L402; the γ==0 block closes at L429 (else at ~L429). 402-426 *under-covers* by ~3 lines (omits the close of the imaginary-else kernel) — illustrative but should tighten to 402-429 | partially-supports (range too tight) |
| `vector.cpp:745-758` | free-fn real-real with γ==0 branch | L745 `template<>`, L746 sig, L749 `if(gamma==0.0)`, L751 `add(alpha,x,beta,y,z)`, L755-756 slow-path `AXPBY(alpha,x,gamma,z); z.Add(beta,y)`, L758 `}` — verbatim | supports |
| `vector.cpp:749-751` (γ==0 fast-path) | MFEM 5-arg `add(α,x,β,y,z)` | exact | supports |
| `vector.cpp:760-765` | free-fn complex-complex one-line delegate (defined-not-used) | L760 `template<>`, L761 sig, L764 `z.AXPBYPCZ(alpha,x,beta,y,gamma)`, L765 `}` — verbatim; corpus census confirms no complex-scalar caller → defined-not-used as claimed | supports (defined-not-used) |
| `vector.cpp:767-772` | free-fn real-on-complex one-line delegate (sub-pat D) | L767 `template<>`, L768 sig, L771 `z.AXPBYPCZ(alpha,x,beta,y,gamma)`, L772 `}` — verbatim. **Overload exists and is correctly cited; but see call-site errors below — it has ZERO observed callers** | supports (decl); **but defined-not-used, contra theme** |
| `vector.cpp:729` | MFEM `add(...)` kernel reused by γ==0 fast-path | L729 `add(alpha,x,beta,y,y)` (AXPBY real-real) | supports |
| Call-site `timeoperator.cpp:139` | sub-pat A, γ=0, z aliases x | `AXPBYPCZ(-1.0, rhs1, dJ_coef(t), NegJ, 0.0, rhs1)` — γ=0 literal, rhs1 read+written; real `Vector`s → A | supports |
| Call-site `timeoperator.cpp:217` | sub-pat A, γ=0 | `AXPBYPCZ(1.0, RHS2, dt, k1, 0.0, k2)` — γ=0 literal | supports |
| Call-site `timeoperator.cpp:273` | sub-pat A, γ=0 | `AXPBYPCZ(1.0, b2, saved_gamma, x1, 0.0, x2)` — γ=0 literal (note: `saved_gamma` is the **β** here, not γ) | supports |
| Call-site `arpack.cpp:772` | sub-pat C, γ=0 | `y2.AXPBYPCZ(sigma, x1, gamma, x2, 0.0)` — γ slot literal `0.0` (the `gamma` var is the **β**); ComplexVector receiver → C | supports |
| Call-site `arpack.cpp:787` | sub-pat C, γ=0 | `y2.AXPBYPCZ(sigma/gamma, y1, 1.0, x1, 0.0)` — γ=0 literal | supports |
| Call-site `nleps.cpp:471` | sub-pat C, γ=0 | `v.AXPBYPCZ(0.5, ev[i1], 0.5, ev[i2], 0.0)` — γ=0 literal, ComplexVector | supports |
| Call-site `nleps.cpp:676` | sub-pat C, γ=0 | `z.AXPBYPCZ(-delta_eig, w, -1.0, u, 0.0)` — γ=0 literal | supports |
| Call-site `nleps.cpp:693` | sub-pat C, γ=0 | `v_trial.AXPBYPCZ(1.0, v, alpha, du, 0.0)` — γ=0 literal | supports |
| **Call-site `slepc.cpp:1986`** | **sub-pat C, γ≠0 (runtime)** | `ctx->y1.AXPBYPCZ(gamma/sigma, y2, -gamma/sigma, x1, 0.0)` — the 5th/γ arg is **literal `0.0`**; `-gamma/sigma` is the **β** (4th slot). **This is γ=0, NOT γ≠0.** | **does-not-support** |
| **Call-site `nleps.cpp:343-344`** | **sub-pat D (real-on-complex), γ=1.0** | `AXPBYPCZ(y(j).real(), X[j].Real(), -y(j).imag(), X[j].Imag(), 1.0, z.Real())` — `X[j].Real()`, `z.Real()` are real `Vector` halves → dispatches to the **real-real free-function (sub-pat A)**, not D. (γ=1.0 literal is correct, but the sub-pattern is A.) | **does-not-support (wrong sub-pattern)** |
| **Call-site `romoperator.cpp:188-189`** | **sub-pat D (real-on-complex), γ=1.0** | `AXPBYPCZ(y(j).real(), V[j], y(j+1).real(), V[j+1], 1.0, u.Real())` — `V` is `std::vector<Vector>`, `u.Real()` a `Vector` half → **real-real (sub-pat A)**, not D. (Confirmed by the odd-`n` companion `linalg::AXPY(y(j).real(), V[j], u.Real())` at romoperator.cpp:193-194 hitting the real-`Vector` AXPY overload.) | **does-not-support (wrong sub-pattern)** |

**Corpus census (complete, via `search_text "AXPBYPCZ"`):** the only AXPBYPCZ call
sites in `palace/**` are timeoperator{139,217,273}, arpack{772,787},
nleps{343,344,471,676,693}, slepc{1986}, romoperator{188,189}. **Every one passes a
literal `0.0` in the γ slot.** Therefore: (a) the γ≠0 path of every sub-pattern is
defined-not-used; (b) sub-pattern D (double scalars on *ComplexVector* x,y,z) has no
caller — the two sites the theme attributes to D are real-real (sub-pattern A);
(c) sub-pattern B (complex scalars) likewise has no caller (correctly noted as such).

## Applicability conditions

### axpby-mutation-rotation

| Condition | Verifiable? | Counter-example? |
|---|---|---|
| 1. No x/y aliasing | Yes — L0 kernel reads `x[i]`, writes `y[i]`; verified all cited sites pass distinct buffers | No |
| 2. No observer of prior `y` after call | Partial — lexical-sequencing argument; not mechanically checkable from a single range, but all cited sites overwrite-then-not-read | No (in cited corpus) |
| 3. Conforming shape + element type, real→complex promotion | Yes — overload set (Vector vs ComplexVector) enforces; promotion via the real-α-on-ComplexVector overload at vector.cpp:714-718 | No |
| 4. α is a runtime scalar; B/C are literal/named-form recognition | Yes — the `alpha==1.0` runtime branch (L704) is inside sub-pat A's L0 form, correctly framed as a transparent trick, not a 4th sub-pattern | No |

All four conditions are complete and correct.

### axpbypcz-mutation-rotation

| Condition | Verifiable? | Counter-example? |
|---|---|---|
| 1. No x/y/z aliasing (+ timeoperator:139 exception) | Yes — exception is real: timeoperator:139 reads+writes `rhs1` with γ=0, reducing to `axpby(-1.0, rhs1, dJ_coef, NegJ)` which the MFEM `add(α,x,β,y,z)` kernel handles alias-safe. The MFEM-alias-safety claim is flagged for MFEM-doc confirmation (carried OQ) | No — but MFEM-alias claim is unverified-against-MFEM (out of Palace scope) |
| 2. No observer of prior `z` after call | Partial (same lexical-sequencing argument as axpby #2) | No (in cited corpus) |
| 3. Conforming shape/type; real-on-complex promotion via 767-772 | Yes — overload exists. **BUT** condition #3 asserts the promotion overload is exercised by the corpus; per the call-site audit it is **not** (defined-not-used). The condition is sound as a *recognition rule*; the prose implying it is observed needs the same defined-not-used caveat as sub-pattern B | Yes — the "exercised" framing (sub-pat D observed) is contradicted |
| 4. γ==0 syntactic recognition on literal | Yes — every site uses literal `0.0`; matches the L0 `gamma==0.0` value-branch at L402/L749 | No |
| 5. No α==0/β==0 L0 branch (recognition-only at L1) | Yes — confirmed: the AXPBYPCZ member body branches only on γ (and on imaginary-scalar shape), never on α==0/β==0 value | No |

Conditions are structurally complete; #3's "observed promotion" framing inherits the
sub-pattern-D misclassification and must be corrected alongside it.

## Algebraic laws (cited)

### axpby-mutation-rotation (sub-rules)
| Law / sub-rule | Holds on operators? |
|---|---|
| sub-pat B: `axpy(1,x,y) = y+x` | Holds — `if(alpha==1.0){y+=x;}` (vector.cpp:704-706); `operator+=` ≡ `AXPY(1.0,x)` (vector.hpp:119-123) |
| sub-pat C: `axpy(-1,x,y)=y-x`, `Subtract(α,x)≡AXPY(-α,x)` | Holds — `Subtract` inline body `AXPY(-α,x)` (vector.hpp:118); `operator-=`≡`AXPY(-1.0,x)` (vector.hpp:124-128) |

### axpbypcz-mutation-rotation (mixed-justification γ==0 sub-rule)
| Law / sub-rule | Holds on operators? |
|---|---|
| γ==0: `axpbypcz(α,x,β,y,0,z)=axpby(α,x,β,y)` (law #1 of L1/axpbypcz) | Holds — real-real γ==0 fast-path calls `add(α,x,β,y,z)` (vector.cpp:751), same kernel as AXPBY real-real `add(α,x,β,y,y)` (vector.cpp:729); complex member γ==0 path shifts `ReadWrite`→`Write` and drops `γ·Z_prev` cross-terms (vector.cpp:402-429). Structural+algebraic mixed framing is sound |
| γ≠0 load-bearing IEEE-order non-law | Holds — γ≠0 slow path `AXPBY(α,x,γ,z); z.Add(β,y)` (vector.cpp:755-756) sums in a different order than the fused γ==0 `add`; correctly recorded as load-bearing in L1/axpbypcz "Laws that do not hold". (Note: this path is defined-not-used in the observed corpus, but the non-law is still a correct property of the L0 source) |

All cited laws hold on the operator signatures. The γ==0 mixed-justification framing
is sound and matches the L0 control flow.

## Proposed changes

### Theme 1 — axpby-mutation-rotation: FIRM IT (fully supported)

Replace the cycle-003 `verified_against:` block with a re-audited cycle-021 block
(all anchors re-confirmed line-exact; same verdicts, refreshed timestamps + the
re-audit attestation), and flip `## Status` rough-in → firm.

```edit:book/src/L1-L0/axpby-mutation-rotation.md
[replace the existing `verified_against:` fenced region — lines 173-209 of the
current file, the raw-YAML-in-prose block — with this fenced YAML block]
```yaml
verified_against:
  - citation: palace/linalg/vector.hpp:115-118
    verdict: supports
    audited_at: 2026-05-29T05:22:35Z
    note: Re-confirmed cycle-021. ComplexVector AXPY/Add/Subtract decls; Subtract inline body AXPY(-alpha, x) at hpp:118.
  - citation: palace/linalg/vector.hpp:119-128
    verdict: supports
    audited_at: 2026-05-29T05:22:35Z
    note: operator+= -> AXPY(1.0,x) (119-123); operator-= -> AXPY(-1.0,x) (124-128). Defined-not-used in palace/**.
  - citation: palace/linalg/vector.cpp:276-311
    verdict: supports
    audited_at: 2026-05-29T05:22:35Z
    note: ComplexVector::AXPY def; ai==0 two-real-kernel else complex-kernel; no alpha==1 value-branch on complex path.
  - citation: palace/linalg/vector.cpp:701-712
    verdict: supports
    audited_at: 2026-05-29T05:22:35Z
    note: Free-fn real-Vector specialisation; if(alpha==1.0){y+=x;}else{y.Add(alpha,x);} at 704-710. Range line-exact.
  - citation: palace/linalg/vector.cpp:714-718
    verdict: supports
    audited_at: 2026-05-29T05:22:35Z
    note: Free-fn real-alpha-on-ComplexVector dispatches to member AXPY at 717; no branch.
  - citation: palace/linalg/vector.cpp:720-724
    verdict: supports
    audited_at: 2026-05-29T05:22:35Z
    note: Free-fn complex-alpha-on-ComplexVector dispatches to member AXPY at 723; defined-not-used (linalg::AXPY corpus = 5 sites, all double alpha: nleps:536, romoperator:193-194, drivensolver:367,394).
  - citation: palace/linalg/operator.cpp:458-466
    verdict: supports
    audited_at: 2026-05-29T05:22:35Z
    note: SumOperator::AddMult uses y.Add(a*c,z) at 464; transpose sibling AddMultTranspose 468-475 identical at 474 (uncited).
  - citation: palace/linalg/rap.cpp:73
    verdict: supports
    audited_at: 2026-05-29T05:22:35Z
    note: b.Add(-1.0, ty); literal -1.0 confirmed sub-pattern C.
  - citation: palace/linalg/rap.cpp:317
    verdict: supports
    audited_at: 2026-05-29T05:22:35Z
    note: y.Add(a, ty); runtime alpha=a; transpose sibling y.Add(a, tx) at rap.cpp:360 (uncited).
```
```

```edit:book/src/L1-L0/axpby-mutation-rotation.md
[replace the `## Status` body, current lines 226-229]
`firm` — all three sub-pattern recognition rules (A bare axpy / B `α==1` / C
`α==-1` & `Subtract`) are verified against the L0 corpus, every cited range is
line-exact, and the `linalg::AXPY` corpus census (5 sites, all `double` α)
confirms the complex-α free-function overload and the `Subtract` / `operator-=` /
`operator+=` member forms are defined-not-used recognition rules. No constructive
sub-part — nothing is reconstructed from negative anchors. (Re-audited cycle-021,
lowering-verifier.) Residual: exhaustive indexing of the ~25 additional
axpy-shaped `y.Add(α,x)` / `y += x` sites under
`palace/linalg/{orthog,iterative,chebyshev,...}` + `palace/models/` is a coverage
*completeness* nicety, not a correctness gate — the recognition rules are firm; the
cited set is illustrative. Carried as OQ `axpby-corpus-coverage-exhaustive-indexing`.
```

```edit:book/src/L1-L0/index.md
[update the axpby-mutation-rotation dep-map row, current line 18]
| [axpby-mutation-rotation](./axpby-mutation-rotation.md) | `L1/axpy` (+ `axpby`/`axpbypcz` fwd-ref) | `palace/linalg/vector.{hpp,cpp}`, `operator.cpp`, `rap.cpp` | firm *(structural; 3 sub-patterns A/B/C; `α==1`/`α==-1` algebraic sub-rules; complex-α + Subtract forms defined-not-used)* |
```

### Theme 2 — axpbypcz-mutation-rotation: KEEP rough-in; firming GATED on call-site corrections

The structural decomposition is firm and all decl/body/kernel anchors verify
line-exact, but the theme asserts observed γ≠0 and sub-pattern-D call sites that the
corpus does not contain. **Do NOT firm as-written.** I propose the exact corrections
below and route firming to a follow-up dispatch (abstractor/lifter, cycle-022) that
applies them and then flips the status — mirroring the cycle-012
`partly-constructive` gated-promotion discipline (UNBLOCK, don't ENACT).

Correction set (the follow-up dispatch applies these, then firms):

1. **Reclassify `nleps.cpp:343-344` from sub-pattern D to sub-pattern A.** Move the
   citation out of sub-pattern D and into sub-pattern A's call-site list. It passes
   `X[j].Real()` / `X[j].Imag()` / `z.Real()` / `z.Imag()` — real `Vector` halves
   with `double` scalars (γ=1.0 literal) → real-real free-function. It is a γ≠0
   *real-real* site (the only one), so it is also the corpus's sole observed exercise
   of sub-pattern A's γ≠0 slow-path `AXPBY(α,x,γ,z); z.Add(β,y)`.
2. **Reclassify `romoperator.cpp:188-189` from sub-pattern D to sub-pattern A.** `V`
   is `std::vector<Vector>` (real), `u.Real()` is a `Vector` half (confirmed by the
   odd-`n` companion `linalg::AXPY(y(j).real(), V[j], u.Real())` at
   romoperator.cpp:193-194). γ=1.0 literal → real-real γ≠0 site.
3. **Correct `slepc.cpp:1986` from γ≠0 to γ=0.** The 5th argument is a literal
   `0.0`; the `-ctx->gamma/ctx->sigma` the theme read as γ is the **β** scalar in the
   4th slot. Reclassify as sub-pattern C, γ=0.
4. **Downgrade sub-pattern D to defined-not-used.** With (1)+(2) removed, sub-pattern
   D has zero observed callers. Mark it defined-not-used (same status as sub-pattern
   B), citing the corpus census. The overload at vector.cpp:767-772 stays a correct
   *recognition rule*.
5. **Add a corpus-census observation:** every observed AXPBYPCZ site uses literal
   γ=0 *except* the two real-real sites at nleps:343-344 and romoperator:188-189
   (γ=1.0). So the only observed γ≠0 path is sub-pattern A's real-real slow-path; the
   complex member-form γ≠0 path (and sub-patterns B/D entirely) are defined-not-used.
   This *strengthens* the load-bearing IEEE-order non-law: the γ≠0 slow-path
   `AXPBY; z.Add` IS exercised (at the two real-real sites), so the cross-branch
   summation-order divergence is a live, not merely potential, reproduction concern.
6. **Tighten the sub-pattern-C γ==0 branch citation** from `vector.cpp:402-426` to
   `vector.cpp:402-429` (the γ==0 block closes at 429; 402-426 omits the imaginary
   else-kernel close).

Proposed `verified_against:` block to append once corrections (1)-(6) land (the
follow-up dispatch appends this and flips status):

```yaml
verified_against:
  - citation: palace/linalg/vector.hpp:133-136
    verdict: supports
    audited_at: 2026-05-29T05:22:35Z
    note: ComplexVector::AXPBYPCZ member decl + (*this)=a*x+b*y+g*(*this) comment.
  - citation: palace/linalg/vector.hpp:313-316
    verdict: supports
    audited_at: 2026-05-29T05:22:35Z
    note: free-fn template decl z=a*x+b*y+g*z.
  - citation: palace/linalg/vector.cpp:381-386
    verdict: supports
    audited_at: 2026-05-29T05:22:35Z
    note: outer member trampoline to static form on Real()/Imag() halves.
  - citation: palace/linalg/vector.cpp:388-455
    verdict: supports
    audited_at: 2026-05-29T05:22:35Z
    note: static member body; gamma==0 outer branch at 402 (Write, no prior-z read) vs gamma!=0 (ReadWrite); inner ai==0&&bi==0 (+gi==0 on gamma!=0) imaginary-scalar fast-paths.
  - citation: palace/linalg/vector.cpp:402-429
    verdict: supports
    audited_at: 2026-05-29T05:22:35Z
    note: gamma==0 branch (tightened from 402-426); Write access, no gamma*Z_prev cross-terms.
  - citation: palace/linalg/vector.cpp:745-758
    verdict: supports
    audited_at: 2026-05-29T05:22:35Z
    note: free-fn real-real; gamma==0 fast-path add(a,x,b,y,z) at 751; gamma!=0 slow-path AXPBY(a,x,g,z); z.Add(b,y) at 755-756.
  - citation: palace/linalg/vector.cpp:760-765
    verdict: supports
    audited_at: 2026-05-29T05:22:35Z
    note: free-fn complex-complex one-line delegate; defined-not-used (no complex-scalar caller in corpus census).
  - citation: palace/linalg/vector.cpp:767-772
    verdict: supports
    audited_at: 2026-05-29T05:22:35Z
    note: free-fn real-on-complex one-line delegate (sub-pattern D); DEFINED-NOT-USED. Theme's prior nleps:343-344 + romoperator:188-189 D-classification was wrong (those are real-real, sub-pattern A).
  - citation: palace/linalg/vector.cpp:729
    verdict: supports
    audited_at: 2026-05-29T05:22:35Z
    note: MFEM add(a,x,b,y,y) at AXPBY real-real; same kernel reused by axpbypcz gamma==0 fast-path add(a,x,b,y,z).
  - citation: palace/models/timeoperator.cpp:139
    verdict: supports
    audited_at: 2026-05-29T05:22:35Z
    note: sub-pattern A, gamma=0 literal, z(rhs1) aliases x(rhs1). Applicability-condition-1 exception.
  - citation: palace/models/timeoperator.cpp:217
    verdict: supports
    audited_at: 2026-05-29T05:22:35Z
    note: sub-pattern A, gamma=0 literal.
  - citation: palace/models/timeoperator.cpp:273
    verdict: supports
    audited_at: 2026-05-29T05:22:35Z
    note: sub-pattern A, gamma=0 literal (saved_gamma is the beta scalar, not gamma).
  - citation: palace/linalg/arpack.cpp:772
    verdict: supports
    audited_at: 2026-05-29T05:22:35Z
    note: sub-pattern C, gamma=0 literal (the `gamma` variable is the beta slot).
  - citation: palace/linalg/arpack.cpp:787
    verdict: supports
    audited_at: 2026-05-29T05:22:35Z
    note: sub-pattern C, gamma=0 literal.
  - citation: palace/linalg/nleps.cpp:471
    verdict: supports
    audited_at: 2026-05-29T05:22:35Z
    note: sub-pattern C, gamma=0 literal.
  - citation: palace/linalg/nleps.cpp:676
    verdict: supports
    audited_at: 2026-05-29T05:22:35Z
    note: sub-pattern C, gamma=0 literal; alpha=-delta_eig, beta=-1 literals.
  - citation: palace/linalg/nleps.cpp:693
    verdict: supports
    audited_at: 2026-05-29T05:22:35Z
    note: sub-pattern C, gamma=0 literal.
  - citation: palace/linalg/slepc.cpp:1986
    verdict: supports
    audited_at: 2026-05-29T05:22:35Z
    note: CORRECTED: sub-pattern C, gamma=0 (5th arg literal 0.0). Prior theme classification "gamma!=0 runtime" was wrong; -gamma/sigma is the beta scalar.
  - citation: palace/linalg/nleps.cpp:343-344
    verdict: supports
    audited_at: 2026-05-29T05:22:35Z
    note: CORRECTED: sub-pattern A (real-real), gamma=1.0 literal. X[j].Real()/Imag(), z.Real()/Imag() are real Vector halves -> real-real free-fn, NOT sub-pattern D. Sole observed gamma!=0 site (exercises the AXPBY; z.Add slow-path).
  - citation: palace/models/romoperator.cpp:188-189
    verdict: supports
    audited_at: 2026-05-29T05:22:35Z
    note: CORRECTED: sub-pattern A (real-real), gamma=1.0 literal. V is std::vector<Vector>, u.Real() a Vector half (confirmed by AXPY companion at 193-194). NOT sub-pattern D.
```

After the corrections land, the proposed `## Status` flip for the follow-up dispatch:

```
`firm` — 4 sub-patterns (A real-real / B complex free-fn / C complex member / D
real-on-complex) + the mixed-justification γ==0 algebraic sub-rule; all decl/body/
kernel ranges line-exact; full call-site corpus census applied. Sub-patterns B and D
are defined-not-used recognition rules (no observed callers). The only observed γ≠0
path is sub-pattern A's real-real slow-path (nleps:343-344, romoperator:188-189),
which makes the load-bearing IEEE-order cross-branch non-law a live reproduction
concern. (Firmed cycle-022 after lowering-verifier call-site corrections.)
```

**Until the follow-up dispatch lands, leave `axpbypcz-mutation-rotation` `## Status`
as `rough-in` and its dep-map row unchanged.** (Per role spec: a partly-supported
audit UNBLOCKS but does not ENACT promotion.)

## Supporting evidence

Files consulted (all via codemap `read_range` / `search_text`, relative to `reference/`):
- `palace/linalg/vector.hpp:113-137`, `305-317` — member + free-fn AXPY/AXPBY/AXPBYPCZ decls.
- `palace/linalg/vector.cpp:276-311` — ComplexVector::AXPY def.
- `palace/linalg/vector.cpp:315-360` — ComplexVector::AXPBY def (L1 axpby surface; boundary context).
- `palace/linalg/vector.cpp:381-455` — ComplexVector::AXPBYPCZ member trampoline + static body.
- `palace/linalg/vector.cpp:695-773` — free-fn AXPY/AXPBY/AXPBYPCZ template specialisations + `add(...)` kernels.
- `palace/linalg/operator.cpp:456-476` — SumOperator::AddMult + AddMultTranspose.
- `palace/linalg/rap.cpp:70-76`, `314-320` — ParOperator Dirichlet residual + AddMult.
- `palace/linalg/arpack.cpp:768-789` — sub-pattern C γ=0 sites.
- `palace/linalg/slepc.cpp:1984-1988` — slepc AXPBYPCZ (γ=0 correction).
- `palace/linalg/nleps.cpp:336-346`, `471`, `676`, `693`, `536` — member-form + the misclassified real-real sites + AXPY companion.
- `palace/models/timeoperator.cpp:137-141` — aliasing exception site.
- `palace/models/romoperator.cpp:176-194` — `ProlongatePROMSolution`; the misclassified real-real sites + AXPY companion.
- `search_text "AXPBYPCZ"` + `"linalg::AXPY("` — complete call-site censuses.

## Open questions / caveats

1. **(BLOCKER for axpbypcz firming, routed to cycle-022)** The three call-site
   misclassifications in `axpbypcz-mutation-rotation` (sub-pattern D ×2 → A;
   slepc γ≠0 → γ=0) must be corrected by a follow-up abstractor/lifter dispatch
   before the theme can be firmed. I have specified the exact corrections (1)-(6)
   above. This is the cycle-012 gated-promotion pattern: I UNBLOCK (confirm structure
   + give the exact edits) but do not ENACT (the theme has known-wrong content; I do
   not flip its status). **Plan item for the meta-phase / cycle-planner:
   `axpbypcz-mutation-rotation-callsite-correction-and-firm`.**

2. **BLAS-1 L1>L0 floor (`blas1-l1-l0-lowering-theme-gap`) is NOT fully closed by
   this cycle.** Firming `axpby` brings it to 7/8 (dot, scal, nrm2,
   assemble-diagonal, axpby firm). `axpbypcz` remains rough-in pending OQ #1. The
   floor closes with one more (corrected-then-firmed) dispatch.

3. **Scope/naming nuance on `axpby-mutation-rotation` (caveat, not blocker):** the
   theme is *named* `axpby-mutation-rotation` but its body covers the **AXPY/`axpy`**
   family (sub-patterns A/B/C are all `axpy`-shaped; `α·x + y`). The `axpby` and
   `axpbypcz` L1 forms appear only as forward references. The L1 `axpby` operator's
   actual L0 surface (`ComplexVector::AXPBY` + the `linalg::AXPBY` free-function
   family at vector.cpp:315-360, 727-743) is **not** the subject of this theme — and
   per the L1/axpby entry, that surface is uniformly delegating with *no*
   constant-folding sub-patterns (purely structural). So there is arguably a missing
   theme: a dedicated `axpby` (the fused 2-scalar form) lowering, distinct from this
   `axpy`-family theme. I did not firm-block on this (the theme content is correct for
   what it covers, and the L1/axpby entry already states its lowering is "structural,
   no sub-patterns"), but flag it: consider renaming this theme `axpy-mutation-rotation`
   and noting that the fused-`AXPBY` lowering is a trivial structural identity covered
   in-line by the L1/axpby entry. **OQ: `axpby-theme-covers-axpy-family-naming`.**

4. **MFEM `add(α,x,β,y,z)` alias-safety (carried, out of Palace scope):** the
   axpbypcz applicability-condition-1 exception (timeoperator:139, z aliases x with
   γ=0) relies on MFEM's `add` kernel being alias-safe when the destination matches an
   input. This is an MFEM-library property, not verifiable from Palace source. Carried
   as the theme's existing flagged OQ; per CLAUDE.md "symbols resolving into MFEM are
   logged as open questions", left as-is. Not a firm-blocker (the value-correctness of
   the in-place per-element kernel is self-evident; the concern is only bit-level).

5. **`vector.cpp:402-426` → `402-429` range tightening** (cosmetic, folded into
   correction (6)): the sub-pattern-C γ==0 branch closes at 429, not 426.
