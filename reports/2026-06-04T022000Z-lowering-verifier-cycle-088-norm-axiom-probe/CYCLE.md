---
agent: lowering-verifier
invoked_at: 2026-06-04T022000Z
scope: L1 verb law-confidence probe — matrix-weighted-norm-norm-axiom-law-confidence-probe
status: integrated
integrated_at: 2026-06-04T023456Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied cycle-088 D1 (LEAD). DISCHARGE (partial — structure-side): §Status gate-(c) bullet rewritten to record the structure-side discharge of laws 4/6/7 via standard inner-product-space theorems on the provably-SPD B = KM; 3 new verified_against: entries spliced into the existing YAML block. Verb STAYS rough-in (test-coverage-bounded) (FP sub-claims + √-entry-point test remain open). Touched book/src/L1/matrix-weighted-norm.md only. DISCHARGE outcome-(a) trigger fired → matrix-weighted-norm-full-firm-cascade-wave queued as a recommended c089 candidate (OQ). Build clean (cargo make book + linkcheck2 exit 0). Zero gate hits."
inputs:
  - book/src/L1/matrix-weighted-norm.md (laws 4 :54, 6 :56, 7 :57; §Status :108-117)
  - palace/linalg/operator.cpp:599-619 (Norml2 √-overload; real √ :606, complex √ :618)
  - palace/linalg/operator.hpp:372-374 (SPD-comment declaration)
  - palace/drivers/eigensolver.cpp:205-213 (B = KM = "real SPD part of the mass matrix")
  - palace/models/spaceoperator.cpp:530-537 (GetInnerProductMatrix → BuildParSumOperator of M->Real())
  - palace/linalg/arpack.cpp:202-206, 433-438 (SetBMat / GetEigenvectorNorm dispatch)
---

# CYCLE: Audit matrix-weighted-norm — norm-axiom law-confidence probe

## Summary

SCOPED literature-anchor probe on `book/src/L1/matrix-weighted-norm.md`'s three inner-product-structure laws (4 triangle `:54`, 6 Cauchy–Schwarz `:56`, 7 parallelogram `:57`). The single question: can a standard inner-product-norm LITERATURE anchor raise these laws' confidence to `inner_product`-equivalent WITHOUT a positive √-entry-point (`linalg::Norml2(comm,x,B,Bx)`) test? **Verdict: DISCHARGE (partial — structure-side).** One-line reason: laws 4/6/7 are inner-product-space THEOREMS that hold for ANY inner-product-induced norm, and the SPD premise they require is satisfied **provably-by-construction** at the usage sites (`B = KM` is documented as "the real SPD part of the mass matrix", a positive-coefficient FE mass matrix built via `GetInnerProductMatrix`), so the literature anchor is the in-scope structure-side analog of an assembly test — it legitimately closes the **structure-side** gate. The discharge is PARTIAL: it covers the laws' mathematical validity, NOT their floating-point sub-claims (the ULP-level strict-Cauchy–Schwarz and bit-determinism caveats at `:69-70` are numerical and remain test-bounded). The verb therefore does **not** flip to `firm`; it stays `rough-in (test-coverage-bounded)` with a narrowed §Status note recording exactly what the literature anchor discharged and what remains. The c080 D1 ruling ("firm-on-positive-structure escape INAPPLICABLE") is REFINED, not overturned: that ruling correctly observed the L0 source only numerically asserts the laws via `WithinRel`/`MFEM_ASSERT` — but the probe's literature lens shows the laws don't NEED an L0 positive site because they are consequences of the SPD structure, which DOES have a positive L0 home.

## Per-citation audit

- **Citation**: `palace/linalg/operator.cpp:599-619`
  - **Theme claim**: the named √-overload entry point; real √ at `:606`, complex √ at `:618`; the only L0 structure-checks are two `MFEM_ASSERT` round-off witnesses.
  - **Found**: confirmed exactly. `:602-606` real body `B.Mult(x,Bx); dot=Dot(comm,Bx,x); MFEM_ASSERT(dot>0.0,...); return std::sqrt(dot);`. `:609-619` complex body with comment `// For SPD B, xᴴ B x is real.` (`:612`), split `B.Mult` on `.Real()`/`.Imag()`, `MFEM_ASSERT(dot.real()>0.0 && std::abs(dot.imag())<1.0e-9*dot.real(),...)` (`:616`), `return std::sqrt(dot.real())` (`:618`). The two asserts are round-off witnesses (positivity + small-imaginary), NOT structural SPD proofs and NOT positive law sites.
  - **Verdict**: supports
  - **Notes**: `read_range` line indexing matched on-disk `Read` exactly; no codemap +1 drift on this block.

- **Citation**: `palace/linalg/operator.hpp:372-374`
  - **Theme claim**: declaration carries comment "Calculate the vector norm with respect to an SPD matrix B."
  - **Found**: confirmed — comment at `:372`, template decl `:373-374`. The SPD-ness is stated as intent in the comment; it is an API contract note, not a verified structural fact at this site.
  - **Verdict**: supports

- **Citation**: `palace/drivers/eigensolver.cpp:205-213` (NEW — the SPD-premise L0 home; load-bearing for this probe)
  - **Theme claim**: (theme §Applicability `:79` asserts) "across Palace's eigensolver corpus, `B` is the mass matrix or a curl-curl mass-weighted operator — both SPD by construction."
  - **Found**: directly confirmed and now precisely anchored. `:205-207` source comment: *"use an M-inner product ... The constructed matrix just references the real **SPD part of the mass matrix** (no copy is performed)."* `:212` `KM = space_op.GetInnerProductMatrix(0.0, 1.0, nullptr, M.get());` `:213` `eigen->SetBMat(*KM);`. So the `B` reaching `Norml2`'s `*opB` IS the scaled real mass matrix, named SPD in-source.
  - **Verdict**: supports — this is the positive L0 home of the SPD premise that the probe needed.
  - **Notes**: the SPD attestation here is a **source comment + constructive provenance**, not a runtime-checked invariant. See §Applicability for the SPD-vs-PSD adjudication.

- **Citation**: `palace/models/spaceoperator.cpp:530-537` (NEW — SPD construction provenance)
  - **Theme claim**: (implied by §Applicability `:79`) B is built as a mass-matrix inner product.
  - **Found**: confirmed. `GetInnerProductMatrix(a0=0.0, a2=1.0, K=nullptr, M)` returns `BuildParSumOperator({0.0,1.0},{nullptr, PtAP_M->Real()})` — i.e. `1.0 · M->Real()`, the real part of the mass matrix. The FE mass matrix `∫ ε φ_i·φ_j` is SPD for positive material coefficient `ε > 0`; the construction is the standard SPD mass form.
  - **Verdict**: supports
  - **Notes**: SPD-ness here is a property of the FE mass-form construction (positive-definite Gram matrix of basis functions weighted by a positive coefficient), a constructive structural fact — not a numerical assertion.

- **Citation**: `palace/linalg/arpack.cpp:202-206, 433-438`
  - **Theme claim**: `GetEigenvectorNorm` dispatches to `linalg::Norml2(comm, x, *opB, Bx)` (`:438`); `opB` set via `SetBMat` (`:202-206`).
  - **Found**: confirmed. `SetBMat` (`:202-206`) stores `opB = &B`; `GetEigenvectorNorm` (`:433-438`) routes to the weighted `Norml2` when `opB` non-null. Same pattern in slepc.cpp / nleps.cpp per existing Evidence section.
  - **Verdict**: supports

- **Citation**: theme §Status gate (a) test-absence claim (`:110-113, :143`)
  - **Theme claim**: no Palace unit test exercises `linalg::Norml2(comm,x,B,Bx)` at the entry point.
  - **Found**: confirmed — `grep -rn "Norml2" reference/palace/palace/test/unit/` returns ZERO hits. The corpus genuinely lacks any `Norml2` reference at all (weighted or unweighted at the free-function entry point). Gate (a) entry-point test is genuinely absent.
  - **Verdict**: supports

## Applicability conditions

- **Condition (SPD `B`, the load-bearing premise for the literature anchor)**: as stated `:49, :77, :79`.
  - **Verifiable**: YES — and this is the crux. The probe required adjudicating "is `B` provably SPD at the usage site, or only PSD / context-dependent?" Answer: **provably SPD by construction.** `B = KM = 1.0 · M->Real()` (`spaceoperator.cpp:530-537`), the real part of the FE mass matrix, named "the real SPD part of the mass matrix" in source (`eigensolver.cpp:206-207`). A positive-coefficient FE mass matrix is SPD (not merely PSD): its eigenvalues are strictly positive because the basis functions are linearly independent and `ε > 0`. The merely-PSD failure mode the probe warned of (B PSD ⇒ seminorm ⇒ triangle holds but definiteness fails) does NOT obtain at these sites.
  - **Found counter-example?**: NO. No usage site passes a merely-PSD or indefinite `B` to the weighted `Norml2` — the three eigensolver backends uniformly pass `*opB = KM` (the SPD mass form). The theme's own §Applicability `:79` ("SPD by construction ... satisfied uniformly") is now anchored to `eigensolver.cpp:206-207` + `spaceoperator.cpp:530-537`.
  - **Caveat preserved**: the SPD-ness is a *construction-time structural* fact + source-comment attestation, NOT a runtime-verified invariant (the only runtime check is the per-call `MFEM_ASSERT(dot>0.0)` round-off witness). For the inner-product-space theorems this is sufficient — they require SPD as a *premise*, and the premise is discharged by the construction, exactly as a firm-on-positive-structure read discharges a syntactic-identity law by reading the positive source closure.

## Algebraic laws (the probe core)

For each of the three probed laws, the question is: does the standard inner-product-space theorem legitimately anchor it WITHOUT a positive √-entry-point test?

- **Law 4 — Triangle inequality (`:54`)**: `‖x+y‖_B ≤ ‖x‖_B + ‖y‖_B`.
  - **Holds on operators?** YES, by the Minkowski inequality, which is a theorem for ANY norm induced by a (semi-)inner product. Given SPD `B`, `⟨x,y⟩_B := xᴴBy` satisfies the inner-product axioms (Hermitian-symmetric since `B` Hermitian; positive-definite since `B` SPD; sesquilinear from `dot`'s laws), so `‖·‖_B = √⟨·,·⟩_B` is an inner-product norm and Minkowski applies. **No Palace test needed** — this is not an empirical claim about Palace's arithmetic, it is a derivation from the SPD structure. DISCHARGED (structure-side).

- **Law 6 — Cauchy–Schwarz in the B-inner-product (`:56`)**: `|⟨x,y⟩_B| ≤ ‖x‖_B · ‖y‖_B`.
  - **Holds on operators?** YES, by the Cauchy–Schwarz inequality, a theorem for any (semi-)inner product. The B-inner-product is genuine (SPD `B`), so C–S holds with equality iff `x,y` linearly dependent mod null(B) (= {0} for SPD). **No Palace test needed.** DISCHARGED (structure-side). NOTE: the FP sub-claim at `:69` ("strict Cauchy–Schwarz can fail by ULP-level amounts due to compound non-associativity") is a SEPARATE numerical claim — it is about the *floating-point realization*, not the exact-arithmetic law, and is NOT discharged by the literature anchor. It remains a numerical caveat (genuinely test-bounded / inherited from `dot`+`apply_linop`).

- **Law 7 — Parallelogram identity (`:57`)**: `‖x+y‖_B² + ‖x−y‖_B² = 2‖x‖_B² + 2‖y‖_B²`.
  - **Holds on operators?** YES — and this one is even weaker in its premise: the parallelogram identity is a *purely algebraic* consequence of the (semi-)inner-product structure (it holds for any SPSD `B`, definiteness not required, as the theme correctly notes `:57`). It is the characterizing identity of inner-product-induced norms. Expanding `‖x±y‖_B² = ⟨x±y, x±y⟩_B` and using sesquilinearity gives the identity directly. **No Palace test needed.** DISCHARGED (structure-side).

**Adjudication of the c080 D1 ruling.** c080 D1 ruled the firm-on-positive-structure escape INAPPLICABLE because "the laws are inner-product-structure theorems the L0 source only numerically asserts via `WithinRel` checks, NOT syntactic identities like the solve_family element-independence read-off." This probe REFINES that ruling: the c080 observation is correct about the L0 *source* (the energy-units test only `WithinRel`-checks the radicand; the √-overload has no positive law site). But the probe's literature lens reframes the question — laws 4/6/7 do not NEED a positive L0 law site, because they are not facts ABOUT Palace's code; they are theorems about the induced norm that follow once the SPD premise is established, and the SPD premise DOES have a positive L0 home (`eigensolver.cpp:206-207` + `spaceoperator.cpp:530-537`). This is the structure-side analog of the firm-on-positive-structure escape: a positive structural read (B is the SPD mass form) discharges a derivable law (the norm axioms), exactly as a read of `solve_family`'s element-independence closure discharged its laws. The escape applies to the **structure-side** of these laws. It does NOT apply to the **floating-point side** (`:69-70` ULP / bit-determinism caveats), which is the genuinely test-bounded residue and is why the verb stays `rough-in (test-coverage-bounded)` rather than flipping `firm`.

## Proposed changes

Two changes, both confined to `book/src/L1/matrix-weighted-norm.md` (HARD CONSTRAINT: this file ONLY — no cascade). (1) Narrow the §Status note to record the structure-side discharge of laws 4/6/7 and what remains. (2) Add a `verified_against:` block recording the literature-anchor derivation + the SPD premise's L0 home. The verb token STAYS `rough-in (test-coverage-bounded)` (the FP sub-claims of gate (a)+(c) remain).

```edit:book/src/L1/matrix-weighted-norm.md
[replace the §Status gate-(c) bullet `:115` to record the structure-side discharge]

OLD:
- **(c) Algebraic-law completeness verification**: confirm laws 1-12 hold uniformly across the two L0 specializations, including the load-bearing SPD precondition. Some laws (3, 9, 12) follow trivially from dependencies; others (4, 6, 7) require the inner-product structure on `B`, which the L0 source does not directly verify.

NEW:
- **(c) Algebraic-law completeness verification** (norm-axiom laws 4/6/7 STRUCTURE-SIDE DISCHARGED cycle-088; FP sub-claims still open): confirm laws 1-12 hold uniformly across the two L0 specializations, including the load-bearing SPD precondition. Some laws (3, 9, 12) follow trivially from dependencies. The inner-product-structure laws — **4 (triangle), 6 (Cauchy–Schwarz), 7 (parallelogram)** — are now structure-side discharged by a literature anchor (cycle-088 D1 probe): they are theorems about ANY inner-product-induced norm, and the SPD premise they require is satisfied **provably-by-construction** at the usage sites — `B = KM = GetInnerProductMatrix(0.0, 1.0, nullptr, M.get())` references "the real SPD part of the mass matrix" (`palace/drivers/eigensolver.cpp:206-207`, `palace/models/spaceoperator.cpp:530-537`: `1.0·M->Real()`, the positive-coefficient FE mass form). Given the SPD premise (which HAS a positive L0 home), Minkowski / Cauchy–Schwarz / the parallelogram identity follow as inner-product-space theorems requiring no positive √-entry-point test — the structure-side analog of the firm-on-positive-structure escape, applied through the SPD construction. What this discharge does **NOT** cover, and why the verb stays `rough-in (test-coverage-bounded)`: the **floating-point** sub-claims at "Laws that do not hold" `:69-70` — strict Cauchy–Schwarz failing by ULP-level amounts (compound `dot`+`apply_linop` non-associativity) and bit-determinism across operator representations of `B` — are numerical claims about the realized arithmetic, not exact-arithmetic theorems, and remain genuinely test-bounded (inherited from `dot` / `apply_linop`). Gate (a)'s √-entry-point test (`linalg::Norml2(comm,x,B,Bx)`) also stays open: the corpus has ZERO `Norml2` references in `test/unit/` (verified cycle-088). So the structure-side of 4/6/7 is closed; the FP-side and the entry-point test are the residue keeping the verb at rough-in.
```

```edit:book/src/L1/matrix-weighted-norm.md
[append to the existing `verified_against:` YAML block — add four entries INSIDE the existing fence, before the closing ~~~ at :159; rendered as a fenced ```yaml block. Integrator: merge into the existing block's list, do not create a second block.]

    note: GetElectricFieldEnergy energy-units test positively covers the SPD-weighted radicand (E, M_elec E) + half scaling (law-8 self-bilinear constituent) via WithinRel against the closed-form half-eps0-E0^2-V; does NOT cover the outer sqrt nor the named entry point linalg::Norml2(comm,x,B,Bx)
  - citation: palace/drivers/eigensolver.cpp:205-213
    verdict: supports
    audited_at: 2026-06-04T022000Z
    note: cycle-088 probe — positive L0 home of the SPD premise; source comment :206-207 names KM as the real SPD part of the mass matrix, KM = GetInnerProductMatrix(0.0,1.0,nullptr,M.get()) then SetBMat(*KM); this is the B reaching Norml2's opB, provably SPD by construction not merely PSD
  - citation: palace/models/spaceoperator.cpp:530-537
    verdict: supports
    audited_at: 2026-06-04T022000Z
    note: cycle-088 probe — SPD construction provenance; GetInnerProductMatrix(0.0,1.0,nullptr,M) builds BuildParSumOperator with 1.0 times M-Real, the real part of the FE mass matrix; positive-coefficient mass form is SPD (strictly positive eigenvalues), discharging the SPD premise that laws 4/6/7 require
  - citation: book/src/L1/matrix-weighted-norm.md:54-57
    verdict: supports
    audited_at: 2026-06-04T022000Z
    note: cycle-088 probe STRUCTURE-SIDE DISCHARGE of laws 4 (triangle) 6 (Cauchy-Schwarz) 7 (parallelogram) via standard inner-product-space theorems applied to the provably-SPD B; these are theorems about any inner-product-induced norm, no positive sqrt-entry-point test needed; FP sub-claims at :69-70 (ULP strict-CS, bit-determinism) NOT covered and stay test-bounded; verb stays rough-in (test-coverage-bounded)
```

NOTE TO INTEGRATOR on the second edit: the existing block at `:145-159` ends its third entry with a `note:` that wraps to `:158`. The four lines I add begin by completing/duplicating the LAST existing `note:` line (the `operator.cpp:599-619` entry's note) only as an anchor for placement — IGNORE the leading `note:` line in my NEW block; it reproduces the existing `:158` note so you can see where to splice. Append my three new `- citation:` entries (eigensolver.cpp, spaceoperator.cpp, matrix-weighted-norm.md self-ref) as additional list items inside the SAME `verified_against:` block, before the closing `~~~` fence at `:159`. Do not create a second block. (If cleaner: just insert the three new `- citation:` items.)

## Supporting evidence

- `reference/palace/palace/linalg/operator.cpp:599-619` — √-overload, read on-disk; real √ `:606`, complex √ `:618`, asserts `:604`/`:616`. On-disk `Read` matched codemap line indexing (no +1 drift on this block).
- `reference/palace/palace/linalg/operator.hpp:372-374` — SPD-comment declaration; `:377-384` `Normalize` wrapper.
- `reference/palace/palace/drivers/eigensolver.cpp:205-213` — the SPD-premise positive L0 home (source comment "real SPD part of the mass matrix").
- `reference/palace/palace/models/spaceoperator.cpp:530-537` — `GetInnerProductMatrix` → `BuildParSumOperator` of `M->Real()`; the SPD mass-form construction.
- `reference/palace/palace/linalg/arpack.cpp:202-206, 433-438` — `SetBMat` / `GetEigenvectorNorm` dispatch (+ slepc.cpp:374,470-481,505; nleps.cpp:44,109-119,146 per existing Evidence cohort).
- `grep -rn Norml2 reference/palace/palace/test/unit/` → 0 hits (gate-(a) entry-point test genuinely absent).
- Prior: c080 D1 audit (the firm-on-positive-structure INAPPLICABLE ruling) — refined, not overturned, by this probe.

## Recommendation: queue the full-firm cascade wave

Per the probe's outcome-(a) instruction: the structure-side discharge of laws 4/6/7 removes the principal mathematical blocker on `matrix-weighted-norm`'s norm-axiom confidence. I RECOMMEND queuing **`matrix-weighted-norm-full-firm-cascade-wave` as a cycle-089 candidate**, gated on: (i) resolving the FP-side residue (the `:69-70` ULP / bit-determinism caveats) either by an inherited-from-`dot`/`apply_linop` confidence argument or a dedicated entry-point test, and (ii) the ~30-file cross-reference re-anchor that a `firm` flip would stale. This probe deliberately does NOT enact the cascade (HARD CONSTRAINT) — it lands the structure-side discharge only and leaves the verb at `rough-in (test-coverage-bounded)`.

## Open questions / caveats

- **FP-side residue is the remaining gate.** The literature anchor closes the exact-arithmetic structure-side of laws 4/6/7 but NOT the floating-point realization caveats (`:69` strict-Cauchy–Schwarz ULP failure, `:70` bit-determinism across `B` representations). Whether these inherit sufficient confidence from `dot` + `apply_linop` (both firm) to be considered discharged, or genuinely need a √-entry-point test, is the open decision a c089 cascade wave must settle. This probe judges them test-bounded (conservative).
- **SPD-ness is construction-attested, not runtime-verified.** The discharge rests on `B` being SPD by construction (FE mass form) + a source comment naming it SPD. There is no runtime SPD verification beyond the per-call `MFEM_ASSERT(dot>0.0)` round-off witness. For the inner-product-space theorems this is the correct kind of evidence (a premise discharged by structural read), but a reader should understand the SPD-ness is a property of the *construction path* the eigensolvers use, not a checked invariant of the `Norml2` callable in isolation — a future non-eigensolver caller passing a non-SPD `B` would void the premise (the theme's §Applicability indefinite-`B` absence `:68` already records this).
- **No direction-of-definition violation observed.** The theme narrates L1 (the pure energy-norm operator) and its laws in L1 vocabulary; no reverse-lift narration. No flag.
- **`verified_against:` splice is delicate** (existing block at `:145-159`). I emitted the three new list items with placement guidance; the integrator should confirm the merged block parses (`python3 -c "import yaml; yaml.safe_load(...)"`) — all my new `note:` values start with non-quote characters (`cycle-088 ...`) per the no-leading-quote rule, and I rendered the energy closed-form as `half-eps0-E0^2-V` to avoid YAML-hostile glyphs.
