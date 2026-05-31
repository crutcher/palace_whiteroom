---
agent: lowering-verifier
invoked_at: 2026-05-31T210435Z
scope: L1>L0 theme audit — floquet-correction-mutation-rotation
status: integrated
integrated_at: 2026-05-31T235900Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean cycle-038 (D4). 29-row verified_against: YAML block (28 supports + 1 partially-supports) appended to firm book/src/L1-L0/floquet-correction-mutation-rotation.md; NO body edits, theme stays firm, citation NOT widened. The single partially-supports row (AddMult aliasing-tolerance cited to thin wrapper ksp.cpp:297 vs the true gated site iterative.cpp:361/:384-385 gated by floquetcorrection.cpp:61 SetInitialGuess(0)) applied as-is and routed to the OPEN follow-up OQ floquet-corrector-addmult-aliasing-applicability-audit (TRIGGER FIRED, sharpened, NOT closed) per UNBLOCK-not-ENACT discipline."
inputs:
  - book/src/L1-L0/floquet-correction-mutation-rotation.md
  - palace/linalg/floquetcorrection.cpp:20-88 (ctor, Mult, AddMult, instantiation)
  - palace/linalg/floquetcorrection.hpp:32-60 (class decl)
  - palace/linalg/ksp.cpp:297 + palace/linalg/iterative.cpp:361,384-385 (inner-ksp aliasing)
  - palace/models/materialoperator.{hpp:35,103,128, cpp:358}
  - palace/drivers/drivensolver.cpp:{138,208,289,332,464}; eigensolver.cpp:{237,450}
  - test/unit/test-schema.cpp:340-353; test/examples/runtests.jl:289-294
  - book/src/L1/floquet-correction.md (firm L1 anchor)
---

# CYCLE: Audit floquet-correction-mutation-rotation

## Summary

Audited the firm L1>L0 theme `floquet-correction-mutation-rotation` (525 lines,
4 sub-patterns A/B/C/D) which landed firm in cycle-036 D1 carrying **no**
`verified_against:` block (confirmed `grep -c '^verified_against:' → 0` on disk).
I emit a fenced `verified_against:` block covering all 29 cited evidence rows and
the L1 anchor. **Top-level verdict: partially-supported (one row), otherwise
fully-supported.** All 43 inline citations in the theme `--scan` clean (`43 ok, 0
failing`), in-bounds, and every anchor I `--anchor`-checked lit at the cited
token. The four sub-pattern rewrites (out-of-place `Mult`, AddMult-as-axpy
fusion, constructed-operator-gate closure materialisation, `<ComplexVector>`-only
scope-out) are each positively witnessed at their cited Palace sites and the
transcriptions match verbatim.

**The single audit finding** bears directly on the trigger-gated OQ
`floquet-corrector-addmult-aliasing-applicability-audit` (open-questions.md:899;
my dispatch IS its trigger): the theme's Applicability-condition-2 /
Sub-pattern-B aliasing-tolerance *mechanism* claim is attributed to
`palace/linalg/ksp.cpp:297`, but that site is a **thin wrapper** that delegates to
the inner `ksp->Mult(x, y)` (`:300`) — it does not itself exhibit the
reads-`x`-once-then-writes-`y` behaviour. The aliasing IS safe, but its true
mechanism + precondition live at `CgSolver::Mult` (`iterative.cpp:361`, else-branch
`:384-385`) gated by `SetInitialGuess(0)` (`floquetcorrection.cpp:61`). I record
that row as `partially-supports`, do NOT silently fix the theme, and leave the OQ
**open** (sharpened, not closed).

The `<ComplexVector>` element-type scope-out is consistent with every cited site:
the sole instantiation `:88`, all three construction-site declarations
(`drivensolver.cpp:138,289`; `eigensolver.cpp:237`), and the absence of any
`<Vector>` instantiation are positively confirmed.

## Per-citation audit

All ranges verified with `python3 tools/citecheck/citecheck.py` (on-disk source of
truth; `--scan` for bounds + `--anchor` for drift). Codemap `read_range` not relied
on for the no-drift assertion.

### Sub-pattern A — out-of-place apply (`Mult`)

- **Citation**: `palace/linalg/floquetcorrection.cpp:73-78`
  - **Theme claim**: two-step `Cross->Mult(x, rhs); ksp->Mult(rhs, y)` body realising the L1 value through output-arg mutation.
  - **Found**: verbatim — sig `:73-74`, brace `:75`, step 1 `:76`, step 2 `:77`, close `:78`.
  - **Verdict**: supports.
- **Citation**: `palace/linalg/floquetcorrection.hpp:49` — `mutable VecType rhs;` — **supports** (single scratch member, lit at `:49`).
- **Citation**: `palace/linalg/floquetcorrection.hpp:58` — `void Mult(...) const;` decl — **supports**.

### Sub-pattern B — apply-and-accumulate (`AddMult`)

- **Citation**: `palace/linalg/floquetcorrection.cpp:80-86`
  - **Theme claim**: `this->Mult(x, rhs); rhs *= a; y += rhs;` realises `y_new = axpy(a, floquet_correction(F, x), y)`.
  - **Found**: verbatim (`:83`/`:84`/`:85`). The algebraic `axpy(α, a, b) = α·a + b` unfolding is the literal body.
  - **Verdict**: supports.
- **Citation**: `palace/linalg/floquetcorrection.hpp:59` — `AddMult(..., ScalarType a = 1.0) const;` decl with default — **supports**.
- **Citation**: `palace/linalg/ksp.cpp:297`
  - **Theme claim** (Applicability condition 2 + Sub-pattern B prose lines 154-159): `BaseKspSolver::Mult` "accepts this aliasing — the CG iteration body reads `x` once into a residual register and thereafter writes `y` and internal workspace independently."
  - **Found**: `:297-310` is `BaseKspSolver<OperType>::Mult` but is a **thin timing+convergence wrapper** that delegates the actual solve to `ksp->Mult(x, y)` at `:300`. The reads-`x`-once-then-writes-`y` *mechanism* is NOT exhibited here. The real CG body is `CgSolver<OperType>::Mult` at `iterative.cpp:361`; under `SetInitialGuess(0)` (`floquetcorrection.cpp:61` → `initial_guess == false`) the else-branch at `:384-385` runs `r = b; x = 0.0;` — `b` is copied into workspace `r` **before** the aliased `x` is zeroed, which is precisely *why* the `b == x` aliasing is safe.
  - **Verdict**: **partially-supports**. The aliasing IS safe (so the theme's *conclusion* holds and the structural AddMult-as-axpy rewrite is fully supported), but the cited `:297` is insufficient evidence for the asserted mechanism; the substantiating sites (`iterative.cpp:361`, `:384-385`, `floquetcorrection.cpp:61`) are uncited. Carry-forward in Open questions; OQ remains open.

### Sub-pattern C — construction-site closure materialisation

- **Citation**: `palace/linalg/floquetcorrection.cpp:20-71` — ctor body — **supports**. Finer anchors all lit: M assembly `:26-39` (`ComplexParOperator` `:33` / dead-code `ParOperator` `:37`), Cross `:41-57` (`MaterialPropertyCoefficient` `:42`, `GetFloquetCross` `:43`, `ComplexParOperator` `:50-51` / dead-code `:55`), ksp+JacobiSmoother `:60-66` (`CgSolver` `:60`, `JacobiSmoother` `:65`), `SetOperators(*M,*M)` `:67`, scratch sizing `:69-70`. **Minor non-load-bearing nit**: theme body line 229 cites the M-block comment as `:25-26`, but the comment is at `:25` only (`:26` is the opening `{`); the enclosing range `:26-39` is itself correct, so this is a one-line over-extension, not a drift.
- **Citation**: `palace/linalg/floquetcorrection.cpp:67` — `SetOperators(*M, *M)` — **supports**.
- **Citation**: `palace/linalg/floquetcorrection.hpp:42-43` — `std::unique_ptr<OperType> M, Cross;` — **supports**.
- **Citation**: `palace/linalg/floquetcorrection.hpp:46` — `std::unique_ptr<BaseKspSolver<OperType>> ksp;` — **supports**.
- **Citation**: `palace/linalg/floquetcorrection.hpp:52-53` — ctor decl — **supports**.
- **Citation**: `palace/models/materialoperator.hpp:103,128` — `GetFloquetCross` accessors — **supports** (both lit).
- **Citation**: `palace/models/materialoperator.cpp:358` — `mat_kx(count).Set(1.0, wave_vector_cross)` — **supports**.
- **Citation**: `palace/models/materialoperator.hpp:35` — `wave_vector_cross` (`mfem::DenseMatrix`, real) — **supports** (substantiates Applicability condition 7).

### Sub-pattern D — element-type scope-out (`<ComplexVector>` only)

- **Citation**: `palace/linalg/floquetcorrection.cpp:88` — `template class FloquetCorrSolver<ComplexVector>;` — **supports**. Confirmed sole instantiation; no `<Vector>` line in the file.
- **Citation**: `palace/linalg/floquetcorrection.cpp:31` — first `if constexpr (is_same<OperType, ComplexOperator>)` — **supports**.
- **Citation**: `palace/linalg/floquetcorrection.cpp:35-38` — `else { ParOperator }` dead-code (M) — **supports**.
- **Citation**: `palace/linalg/floquetcorrection.cpp:48` — second `if constexpr` — **supports**.
- **Citation**: `palace/linalg/floquetcorrection.cpp:53-56` — `else { ParOperator }` dead-code (Cross) — **supports**.
- **Citation**: `palace/drivers/drivensolver.cpp:138-143` / `:289-294`, `palace/drivers/eigensolver.cpp:237-243` — all three construction sites declare `std::unique_ptr<FloquetCorrSolver<ComplexVector>>` and `make_unique<...<ComplexVector>>` — **supports** (no `<Vector>` anywhere in the call-site cohort; element-type scope-out is consistent with all cited sites).

### AddMult call-site cohort (all four)

- **Citation**: `palace/drivers/drivensolver.cpp:208-213` — `floquet_corr->AddMult(E, B, 1.0/omega)` `:212`, preceded by `B *= -1.0/(1i*omega)` `:207` — **supports** (Applicability condition 3 lexical-sequencing confirmed: `B` fully written by the rescale before AddMult accumulates).
- **Citation**: `palace/drivers/drivensolver.cpp:332-337` — AddMult `:336` — **supports**.
- **Citation**: `palace/drivers/drivensolver.cpp:464-469` — AddMult `:468` — **supports**.
- **Citation**: `palace/drivers/eigensolver.cpp:450-455` — AddMult `:454`, preceded by `B *= -1.0/(1i*omega)` `:449` — **supports**. **Four AddMult call sites total — the theme's exhaustiveness claim ("all four AddMult call sites") is confirmed.**

### Test / regression supplements

- **Citation**: `test/unit/test-schema.cpp:340-353` — `SECTION("FloquetWaveVector must be array")` — **supports** (config-surface semantic supplement, not a per-rewrite anchor).
- **Citation**: `test/examples/runtests.jl:289-294` — `cylinder/floquet` periodic regression — **supports** (L0-equivalent end-to-end supplement).

### L1 anchor

- **Citation**: `book/src/L1/floquet-correction.md` — firm L1 operator all four sub-patterns lower from — **supports**.

## Applicability conditions

| # | Condition | Verifiable from cited evidence? | Counter-example? |
|---|---|---|---|
| 1 | No aliasing between `x`, `y`, `rhs` at `Mult` | Yes — `rhs` is a construction-bound member (`hpp:49`, sized `cpp:69-70`), distinct from caller `x`/`y` | No |
| 2 | Inner ksp accepts input/output aliasing | **Partially** — see Sub-pattern B finding. Cited `ksp.cpp:297` is the wrapper; the aliasing-safety mechanism is at `iterative.cpp:361,384-385` gated by `floquetcorrection.cpp:61` `SetInitialGuess(0)`, both uncited. Aliasing IS safe; evidence site insufficient. | No (condition holds; citation gap only) |
| 3 | No observer of prior `y` after the in-place call | Yes — verified at all four AddMult sites: `B *= -1.0/(1i*omega)` (`:207`/`:449`) precedes AddMult, fully writing `B` before accumulation | No |
| 4 | Closure immutability across calls | Yes — `M`/`Cross`/`ksp` set once in ctor (`:20-71`), `unique_ptr` members read-only across calls | No |
| 5 | Step ordering `Cross → ksp` load-bearing | Yes — `Mult` body `:76-77` is the only cited ordering | No |
| 6 | Element-type conformance (single `<ComplexVector>`) | Yes — sole instantiation `:88`; all three driver decls bind `<ComplexVector>` (`drivensolver.cpp:138,289`, `eigensolver.cpp:237`) | No |
| 7 | Wave vector real-valued, spatially const per material | Yes — `wave_vector_cross` is `mfem::DenseMatrix` real (`materialoperator.hpp:35`); `mat_kx(count).Set(1.0, …)` (`cpp:358`) | No |
| 8 | Single-machine scope (`MPI_Comm` single-rank) | Yes — `rt_fespace.GetComm()` (`:60,65`) read single-rank per project scope; absent from L1 signature | No (out-of-scope flag, not a counter-example) |

## Algebraic laws (cited)

- **Law**: AddMult unfolds to `axpy(a, floquet_correction(F, x), y) = a·floquet_correction(F, x) + y`.
  - **Holds on operators?** Yes. The L0 body `:83-85` (`this->Mult(x, rhs); rhs *= a; y += rhs;`) is the literal `α·a + b` form with `α=a`, `a=floquet_correction(F,x)` (computed by `this->Mult`), `b=y`. The identity holds on the `<ComplexVector>` signature (complex scalar `a`, complex field accumulation). The *structural* buffer-economy claim (scratch member reused as transient scaled-output) is confirmed at the body; its *aliasing precondition* is the partially-supported row above.

## Proposed changes

Append the `verified_against:` block at end-of-file, following the sibling-theme
convention (`dot-mutation-rotation.md` places its fenced ` ```yaml ` block at EOF;
`reciprocal-elementwise-product-mutation-rotation.md` likewise). The block round-trips
through `yaml.safe_load` (29 rows; verdicts `supports` ×28 + `partially-supports` ×1)
and no `note:` value begins with a quote of either kind (self-checked per
`verified-against-note-no-leading-quote-of-either-kind`).

This is a metadata addition only — **no theme claim is changed** (the one
`partially-supports` finding is recorded as a finding + OQ, not auto-fixed).

````edit:book/src/L1-L0/floquet-correction-mutation-rotation.md
[append at end of file]

```yaml
verified_against:
  # Sub-pattern A — out-of-place apply (Mult)
  - citation: palace/linalg/floquetcorrection.cpp:73-78
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: Mult(const VecType &x, VecType &y) const two-step body; sig :73-74, brace :75, Cross->Mult(x, rhs) :76, ksp->Mult(rhs, y) :77, close :78 — matches theme transcription verbatim (citecheck OK, anchors lit).
  - citation: palace/linalg/floquetcorrection.hpp:49
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: mutable VecType rhs; the single scribbled scratch member confirmed at :49 (citecheck OK).
  - citation: palace/linalg/floquetcorrection.hpp:58
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: void Mult(const VecType &x, VecType &y) const; apply decl with const-ref x input and ref y output confirmed at :58 (citecheck OK).
  # Sub-pattern B — apply-and-accumulate (AddMult) + the load-bearing inner-ksp aliasing applicability
  - citation: palace/linalg/floquetcorrection.cpp:80-86
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: AddMult body; this->Mult(x, rhs) :83 (output rebind to scratch member), rhs *= a :84, y += rhs :85 — the axpy-into-floquet fusion reads verbatim; the algebraic axpy(a, floquet_correction(F,x), y) unfolding is the literal :83-85 body (citecheck OK).
  - citation: palace/linalg/floquetcorrection.hpp:59
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: void AddMult(const VecType &x, VecType &y, ScalarType a = 1.0) const; default a=1.0 (no-scale Mult-and-add) confirmed at :59 (citecheck OK).
  - citation: palace/linalg/ksp.cpp:297
    verdict: partially-supports
    audited_at: 2026-05-31T210435Z
    note: site exists and is BaseKspSolver<OperType>::Mult, but :297-310 is a thin wrapper delegating to inner ksp->Mult(x,y) at :300 — it does NOT itself exhibit the reads-x-once-then-writes-y aliasing-tolerance the theme attributes to it (Applicability condition 2 / Sub-pattern B prose lines 154-159). The aliasing mechanism + its initial_guess==false precondition actually live at CgSolver<OperType>::Mult iterative.cpp:361 (else-branch :384-385 `r = b; x = 0.0;` reads b before zeroing the aliased x) gated by SetInitialGuess(0) at floquetcorrection.cpp:61. Aliasing IS safe, but the cited :297 is insufficient evidence for the mechanism; carry-forward correction recorded in Open questions. Structural AddMult-as-axpy rewrite itself is fully supported.
  # Sub-pattern C — construction-site closure materialisation
  - citation: palace/linalg/floquetcorrection.cpp:20-71
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: ctor body; sig :20-23, M assembly :26-39 (ComplexParOperator wrap :33 / dead-code ParOperator :37), Cross assembly :41-57 (MaterialPropertyCoefficient :42, GetFloquetCross :43, ComplexParOperator :50-51 / dead-code :55), ksp+JacobiSmoother :60-66 (CgSolver :60, JacobiSmoother :65), SetOperators(*M,*M) :67, rhs sizing :69-70 — all finer anchors lit (citecheck OK). MINOR — theme body line 229 cites the M-block comment as :25-26 but it is at :25 only (:26 is the opening brace); non-load-bearing over-extension, range :26-39 itself correct.
  - citation: palace/linalg/floquetcorrection.cpp:67
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: ksp->SetOperators(*M, *M) — operator and preconditioner-target both bound to the RT mass M_RT, confirmed at :67 (citecheck OK).
  - citation: palace/linalg/floquetcorrection.hpp:42-43
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: std::unique_ptr<OperType> M, Cross; construction-bound closure operator fields confirmed at :42-43 (citecheck OK).
  - citation: palace/linalg/floquetcorrection.hpp:46
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: std::unique_ptr<BaseKspSolver<OperType>> ksp; inner constructed-operator-gate field confirmed at :46 (citecheck OK).
  - citation: palace/linalg/floquetcorrection.hpp:52-53
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: FloquetCorrSolver(...) constructor decl confirmed at :52-53 (citecheck OK).
  - citation: palace/models/materialoperator.hpp:103,128
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: GetFloquetCross per-attribute (:103) and all-attributes (:128) accessors both lit (citecheck OK).
  - citation: palace/models/materialoperator.cpp:358
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: mat_kx(count).Set(1.0, wave_vector_cross); per-attribute skew-symmetric wave-vector cross-product init confirmed at :358 (citecheck OK).
  - citation: palace/models/materialoperator.hpp:35
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: wave_vector_cross member (mfem::DenseMatrix, real-valued) confirmed at :35 — substantiates Applicability condition 7 (wave vector real-valued, spatially constant per material) (citecheck OK).
  # Sub-pattern D — element-type scope-out (<ComplexVector> only)
  - citation: palace/linalg/floquetcorrection.cpp:88
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: template class FloquetCorrSolver<ComplexVector>; the SOLE explicit instantiation — no <Vector> line anywhere; the scope-out is positively witnessed (citecheck OK).
  - citation: palace/linalg/floquetcorrection.cpp:31
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: first if constexpr (std::is_same<OperType, ComplexOperator>::value) — the reachable complex branch of M_RT assembly, anchor lit at :31 (citecheck OK).
  - citation: palace/linalg/floquetcorrection.cpp:35-38
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: else { ... ParOperator ... } real-branch dead-code of M_RT assembly confirmed at :35-38 (unreachable under <ComplexVector>-only instantiation) (citecheck OK).
  - citation: palace/linalg/floquetcorrection.cpp:48
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: second if constexpr — the reachable complex branch of Cross assembly, anchor lit at :48 (citecheck OK).
  - citation: palace/linalg/floquetcorrection.cpp:53-56
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: else { ... ParOperator ... } real-branch dead-code of Cross assembly confirmed at :53-56 (citecheck OK).
  - citation: palace/drivers/drivensolver.cpp:138-143
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: first construction site; std::unique_ptr<FloquetCorrSolver<ComplexVector>> :138 + make_unique<...<ComplexVector>> :141 — binds <ComplexVector>, no <Vector> (citecheck OK; corroborates Sub-pattern D and Applicability condition 6).
  - citation: palace/drivers/drivensolver.cpp:289-294
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: second construction site; same <ComplexVector> binding at :289/:292 (citecheck OK).
  - citation: palace/drivers/eigensolver.cpp:237-243
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: eigenmode construction site; <ComplexVector> binding at :237/:240 (citecheck OK).
  # AddMult call-site cohort (all four) — the apply-and-accumulate witnesses + Applicability condition 3 lexical sequencing
  - citation: palace/drivers/drivensolver.cpp:208-213
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: first AddMult call site floquet_corr->AddMult(E, B, 1.0/omega) :212, preceded by B *= -1.0/(1i*omega) at :207 — confirms Applicability condition 3 (prior B fully written by rescale before AddMult accumulates; no prior-y observer) (citecheck OK).
  - citation: palace/drivers/drivensolver.cpp:332-337
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: second AddMult call site AddMult(E, B, 1.0/omega) :336 (citecheck OK).
  - citation: palace/drivers/drivensolver.cpp:464-469
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: third AddMult call site AddMult(E, B, 1.0/omega) :468 (citecheck OK).
  - citation: palace/drivers/eigensolver.cpp:450-455
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: fourth AddMult call site AddMult(E, B, 1.0/omega) :454, preceded by B *= -1.0/(1i*omega) at :449 — confirms condition 3 lexical sequencing on the eigen path (citecheck OK). Four AddMult call sites total — theme exhaustiveness claim confirmed.
  # Test / regression supplements (L0-equivalent semantic documentation)
  - citation: test/unit/test-schema.cpp:340-353
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: SECTION("FloquetWaveVector must be array") JSON-schema validation for the Periodic FloquetWaveVector config at :340-353 — supporting (config-surface) evidence, not a per-rewrite anchor (citecheck OK).
  - citation: test/examples/runtests.jl:289-294
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: cylinder/floquet periodic end-to-end regression at :289-294 (testcase "cylinder","floquet.json","floquet") — L0-equivalent semantic supplement (citecheck OK).
  # L1 anchor
  - citation: book/src/L1/floquet-correction.md
    verdict: supports
    audited_at: 2026-05-31T210435Z
    note: the firm L1 floquet_correction operator all four sub-patterns lower from; firm at cycle-036 D1 (sibling-theme L1-anchor convention).
```
````

## Supporting evidence

- `reference/palace/palace/linalg/floquetcorrection.cpp:20-88` — ctor + `Mult` + `AddMult` + sole `<ComplexVector>` instantiation.
- `reference/palace/palace/linalg/floquetcorrection.hpp:32-60` — class decl + scratch member.
- `reference/palace/palace/linalg/ksp.cpp:297-310` — `BaseKspSolver::Mult` wrapper (the cited but insufficient aliasing site).
- `reference/palace/palace/linalg/iterative.cpp:361,384-385` — `CgSolver::Mult` body; the `initial_guess==false` else-branch that makes the `b==x` aliasing safe (the true mechanism site).
- `reference/palace/palace/models/materialoperator.{hpp:35,103,128, cpp:358}` — wave-vector cross-product machinery.
- `reference/palace/palace/drivers/drivensolver.cpp:{138,207-212,289,332,464-468}`, `eigensolver.cpp:{237,449-454}` — construction + AddMult call sites (4 AddMult total; B-rescale precedes each).
- `reference/palace/test/unit/test-schema.cpp:340-353`, `test/examples/runtests.jl:289-294` — semantic supplements.
- `book/src/L1-L0/dot-mutation-rotation.md`, `reciprocal-elementwise-product-mutation-rotation.md` — sibling `verified_against:` fence-placement convention.

## Open questions / caveats

- **`floquet-corrector-addmult-aliasing-applicability-audit` (open-questions.md:899) — SHARPENED, NOT CLOSED.** My dispatch is the OQ's trigger ("a lowering-verifier dispatch on the floquet-correction-mutation-rotation theme"). Finding: the aliasing-tolerance applicability (Applicability condition 2 / Sub-pattern B prose lines 154-159) **does hold** — the inner CG, constructed with `SetInitialGuess(0)` (`floquetcorrection.cpp:61`), runs the `else` branch `r = b; x = 0.0;` (`iterative.cpp:384-385`) which copies `b` into workspace `r` BEFORE zeroing the aliased `x`, so `ksp->Mult(rhs, rhs)` is safe. **However**, the theme cites only `ksp.cpp:297` (a thin delegating wrapper) for this claim; the cited site does NOT exhibit the mechanism. **Recommended carry-forward (route: abstractor or a follow-up lowering-verifier; do NOT auto-apply here):**
  1. Add citations `palace/linalg/iterative.cpp:361` (CgSolver::Mult body) and `:384-385` (the `r = b; x = 0.0;` aliasing-safe else-branch) to Sub-pattern B / Applicability condition 2.
  2. State the **load-bearing precondition** explicitly: the aliasing safety is contingent on `SetInitialGuess(0)` (`floquetcorrection.cpp:61` → `initial_guess == false`). With `initial_guess == true`, the `:379` `A->Mult(x, r)` path reads the aliased `x` while forming the residual — a different (and separately-arguable) safety case that the theme does not cover. The floquet ksp always sets `SetInitialGuess(0)`, so the condition is satisfied, but the precondition should be named.
  3. The OQ should remain OPEN until those two edits land; this audit confirms the *structure* and identifies the exact firming edits but does not enact them (per the partly-constructive/gated-unblock discipline; here the theme stays `firm` — the structural rewrite is fully supported — only the one applicability-citation is sharpened).
- **`floquet-correction-real-vector-instantiation-dead-code` (open-questions.md:898) — unaffected.** My audit confirms the `<ComplexVector>`-only scope-out is consistent across the sole instantiation `:88` and all three driver-site bindings; the `<Vector>` dead-code branches (`:35-38, :53-56`) are positively present as deliberate scope-out. No change.
- **Minor citation over-extension (non-blocking, NOT a verdict change).** Theme body line 229 cites the M-block comment as `:25-26`; the comment is at `:25` only (`:26` is the opening `{`). The enclosing range `:26-39` is correct. Recorded in the `cpp:20-71` row note; an abstractor may tighten line 229 to `:25` opportunistically. Not flagged as drift (the load-bearing range is correct).
- **Element-type scope `<ComplexVector>` only — confirmed consistent with all cited sites** (per dispatch directive). The sole instantiation `:88`, the three construction-site `std::unique_ptr<FloquetCorrSolver<ComplexVector>>` declarations, and the `if constexpr` reachable-complex / dead-real branches are all internally consistent. No real-typed driver site exists.
