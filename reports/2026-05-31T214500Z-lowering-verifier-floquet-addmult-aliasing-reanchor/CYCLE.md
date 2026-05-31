---
agent: lowering-verifier
invoked_at: 2026-05-31T215306Z
scope: L1>L0 theme re-anchor (ENACT) — floquet-correction-mutation-rotation, Sub-pattern B / Applicability-condition-2 AddMult inner-ksp aliasing-tolerance mechanism
status: pending
integrated_at: 2026-05-31T222451Z
integration_commit: 1f178ff
integration_notes: "Applied clean by integrator-per-report (cycle-039 D2). 6 surgical edits re-anchored the AddMult aliasing mechanism from the ksp.cpp:297 delegation wrapper to the true gated CgSolver::Mult (iterative.cpp:361/:384-385) + SetInitialGuess(0) precondition (floquetcorrection.cpp:61); all verified_against rows now supports; theme stays firm. OQ floquet-corrector-addmult-aliasing-applicability-audit CLOSED. No build-repair needed (prose/citation/YAML only, no new live links)."
inputs:
  - book/src/L1-L0/floquet-correction-mutation-rotation.md
  - palace/linalg/iterative.cpp:360-386 (CgSolver::Mult — true aliasing-tolerance mechanism)
  - palace/linalg/floquetcorrection.cpp:61 (SetInitialGuess(0) — initial_guess==false precondition)
  - palace/linalg/ksp.cpp:297-300 (BaseKspSolver::Mult — delegation wrapper, re-framed)
  - OQ floquet-corrector-addmult-aliasing-applicability-audit (cycle-038 audit finding)
---

# CYCLE: Re-anchor floquet-correction-mutation-rotation AddMult inner-ksp aliasing-tolerance mechanism

## Summary

This is an ENACT dispatch (cycle-039 D2), not a routing audit: the cycle-038
lowering-verifier already audited `floquet-correction-mutation-rotation` and
found that Sub-pattern B / Applicability-condition-2 attributes the AddMult
inner-ksp **aliasing-tolerance mechanism** to `palace/linalg/ksp.cpp:297` — a
site that is a *thin delegation wrapper* (it just forwards `ksp->Mult(x, y)` at
`:300`) and does NOT itself exhibit the read-`x`-before-write mechanism the
theme prose claims. I re-verified the planner's pre-localized lines on-disk with
`tools/citecheck/citecheck.py --anchor` (NOT codemap read_range), confirmed the
TRUE mechanism is `CgSolver::Mult` (`iterative.cpp`, signature at `:361`,
else-branch `:382-386`), gated by `SetInitialGuess(0)` (`floquetcorrection.cpp:61`),
caught and corrected a +1 drift in the planner's hint for the CgSolver signature
line, and enact the widening edits: (1) re-frame the `ksp.cpp:297` reference as
the delegation wrapper and name the true mechanism + its precondition in the
Sub-pattern B prose, the Sub-pattern B Citations list, and Applicability
condition 2; (2) upgrade the `verified_against:` `ksp.cpp:297` row from
`partially-supports` to `supports` and add two new mechanism rows
(`iterative.cpp:360-386`, `floquetcorrection.cpp:61`). Theme stays **firm** (it
already was — the structural AddMult-as-axpy rewrite at `floquetcorrection.cpp:80-86`
is untouched; only the *evidence for the aliasing applicability sub-claim* was
incomplete). **Verdict: fully-supported after re-anchor.** OQ
`floquet-corrector-addmult-aliasing-applicability-audit` can be CLOSED — the
re-anchor reframes **all six** `ksp.cpp:297` mention sites (the Sub-pattern B
prose, the Sub-pattern B Citations list, Applicability condition 2, the
Verified-against L0 list, the `verified_against:` YAML row, and the §Status
firmness-justification paragraph), leaving no surviving wrapper-as-mechanism
attribution.

## On-disk re-verification (citecheck --anchor; the no-drift assertion)

Every line below was confirmed against `reference/palace` on-disk via
`tools/citecheck/citecheck.py` (on-disk source-of-truth, NOT codemap read_range
— per the codemap-read-range-plus-one-drift discipline). The planner's hint and
the on-disk reality DIVERGED on one line; I cite the on-disk line.

| Construct | Planner hint | On-disk (citecheck) | Verdict |
|---|---|---|---|
| `CgSolver<OperType>::Mult` signature | `iterative.cpp:360` | **`:361`** (`:360` is the `template <typename OperType>` line; `CgSolver<OperType>::Mult` anchor lit at `:361`) | **DRIFT +1 corrected** — cite `:361` |
| `if (this->initial_guess)` test | (implied) | `:377` (anchor `initial_guess` lit) | OK |
| `else { ... }` aliasing-safe branch | `:383-386` | `:382` (`else`) … `:386` (`}`); body `r = b;` `:384`, `x = 0.0;` `:385` | OK (range `:382-386`; statements `:384`/`:385`) |
| `r = b;` (read b before zero) | `:384` | `:384` (anchor `r = b` lit) | OK |
| `x = 0.0;` (zero aliased x) | `:385` | `:385` (anchor `x = 0.0` lit) | OK |
| `pcg->SetInitialGuess(0)` precondition | `floquetcorrection.cpp:61` | `:61` (anchor `SetInitialGuess(0)` lit) | OK |
| `BaseKspSolver::Mult` delegation wrapper | `ksp.cpp:297` | `:297` (sig); `:300` `ksp->Mult(x, y)` forwards | OK (wrapper, not mechanism) |
| `CgSolver` construction (`pcg`) | `floquetcorrection.cpp:60` | `:60` `make_unique<CgSolver<OperType>>` → `:66` wrapped in `BaseKspSolver` | OK (delegation chain intact) |

**Re-anchor rationale (the mechanism, narrated forward L1→L0).** In `AddMult`,
the nested `this->Mult(x, rhs)` re-binds `Mult`'s output to the construction-bound
scratch `rhs`; `Mult`'s step-2 is `ksp->Mult(rhs, y_arg == rhs)`, i.e. the inner
ksp is called with input RHS aliased to output destination (`b == x`). The
call-path is: `BaseKspSolver::Mult` (`ksp.cpp:297`, the wrapper) → `ksp->Mult(x, y)`
at `:300` → `CgSolver::Mult` (`iterative.cpp:361`). Because `pcg->SetInitialGuess(0)`
(`floquetcorrection.cpp:61`) set `initial_guess == false`, `CgSolver::Mult` takes
the else-branch (`:382-386`): `r = b;` (`:384`) copies the RHS into the residual
register **before** `x = 0.0;` (`:385`) zeros the aliased destination. The
read-before-zero is exactly what makes `b == x` aliasing safe. Had
`initial_guess` been true, the if-branch (`:377-381`) would compute
`A->Mult(x, r)` — reading `x` — which under aliasing would read the not-yet-set
RHS and break. So the aliasing tolerance is NOT an unconditional property of the
inner ksp; it is a **conditional** property gated by the `SetInitialGuess(0)`
setup choice. The `ksp.cpp:297` wrapper carries no aliasing logic at all — the
old prose attributed the mechanism to the wrong layer of the delegation chain.

## Per-citation audit

- **Citation**: `palace/linalg/ksp.cpp:297` (existing theme reference for the aliasing mechanism)
  - **Theme claim (pre-edit)**: this `BaseKspSolver::Mult` site exhibits the
    reads-`x`-once-then-writes-`y` aliasing tolerance.
  - **Found**: `:297-300` is a thin wrapper — `:299` `BlockTimer`, `:300`
    `ksp->Mult(x, y)` forwards verbatim to the inner solver; no aliasing logic.
  - **Verdict**: partially-supports → after re-frame as delegation wrapper, **supports**.
  - **Notes**: The site is real and IS on the call-path; it is just not the
    mechanism. Re-framed, not removed.

- **Citation**: `palace/linalg/iterative.cpp:360-386` (NEW — the true mechanism)
  - **Theme claim (post-edit)**: `CgSolver::Mult` else-branch copies `b`→`r`
    before zeroing the aliased `x`, making `b == x` aliasing safe.
  - **Found**: signature `:361`; `if (this->initial_guess)` `:377`; else `:382`;
    `r = b;` `:384`; `x = 0.0;` `:385`; `}` `:386`. Exactly as claimed.
  - **Verdict**: **supports**.
  - **Notes**: Planner hinted `:360` for the signature; on-disk anchor is `:361`
    (+1 drift; `:360` is the `template` line). Corrected — cite range `:360-386`
    to encompass template-line + signature + branch, with precise statements
    `:384`/`:385`.

- **Citation**: `palace/linalg/floquetcorrection.cpp:61` (NEW — the precondition)
  - **Theme claim (post-edit)**: `SetInitialGuess(0)` establishes the
    `initial_guess == false` precondition that selects the aliasing-safe else-branch.
  - **Found**: `:61` `pcg->SetInitialGuess(0);` (anchor lit). The `pcg` is the
    `CgSolver` made at `:60`, wrapped into `ksp` at `:66`.
  - **Verdict**: **supports**.
  - **Notes**: This makes the aliasing tolerance *conditional* (load-bearing on
    the setup choice), a more precise claim than the pre-edit unconditional one.

## Applicability conditions

- **Condition 2 (Inner ksp accepts input/output aliasing)** — as stated, cites
  only `ksp.cpp:297`. **Verifiable**: yes, but the cited site is the wrong layer.
  **Found counter-example?**: No counter-example to the *conclusion* (aliasing
  IS safe), but the *evidence* was misattributed. Re-anchored to name the
  delegation wrapper (`ksp.cpp:297`/`:300`), the mechanism (`iterative.cpp:361`,
  else-branch `:382-386`), and the `SetInitialGuess(0)` precondition
  (`floquetcorrection.cpp:61`). The condition is now precise: aliasing tolerance
  holds *because* `initial_guess == false`.
- Conditions 1, 3–8 — unchanged by this dispatch; cycle-038 audit confirmed them.

## Algebraic laws (if cited)

- **Law**: AddMult-as-axpy unfolding `axpy(α, a, b) = α·a + b` with
  `(α=a, a=floquet_correction(F, x), b=y)`. **Holds on operators?**: yes — the
  literal `:83-85` body (`this->Mult(x, rhs)`, `rhs *= a`, `y += rhs`) is the
  unfolding. Untouched by this re-anchor (the algebraic sub-rule was always
  fully supported; only the *structural aliasing applicability* sub-claim's
  evidence was incomplete).

## Proposed changes

Six surgical edits against `book/src/L1-L0/floquet-correction-mutation-rotation.md`.
Each `edit:` fence carries the FULL replaced region. Inner code is 4-space
indented (none needed here); the `verified_against:` block stays a ` ```yaml `
fence nested inside its `edit:` fence (edit-open → yaml-open → yaml-close →
edit-close, balanced).

### Edit 1 — Sub-pattern B prose (re-frame ksp.cpp:297 as wrapper, name the mechanism)

```edit:book/src/L1-L0/floquet-correction-mutation-rotation.md
Crucial L0 fact the L1 fusion erases: **the inner `this->Mult(x, rhs)` call binds
`Mult`'s output destination to the same scratch member `rhs` that `Mult`'s body
uses as its step-1 cross-product intermediate**. Inside the nested call, the
sequence is `Cross->Mult(x, this->rhs); this->ksp->Mult(this->rhs, y_arg =
this->rhs);` — i.e. `ksp->Mult(b, x)` with `b == x` (the input RHS and the
output buffer are the same `VecType`). This implies a **load-bearing aliasing
applicability condition** (see Applicability conditions): the inner CG solver
must accept input/output aliasing on its argument vectors.

The inner ksp is reached through a delegation chain, and the aliasing tolerance
lives at the *bottom* of it, not at the top. `F.ksp` is a
`BaseKspSolver<OperType>` whose `Mult` (`palace/linalg/ksp.cpp:297`) is a **thin
delegation wrapper** — it opens a `BlockTimer` and forwards `ksp->Mult(x, y)`
(`palace/linalg/ksp.cpp:300`) verbatim to the wrapped inner solver, carrying no
aliasing logic of its own. The wrapped inner solver is a `CgSolver<OperType>`
(constructed at `palace/linalg/floquetcorrection.cpp:60`, wrapped into `F.ksp`
at `:66`). The **actual aliasing-tolerance mechanism** is in
`CgSolver<OperType>::Mult(const VecType &b, VecType &x) const`
(`palace/linalg/iterative.cpp:361`): because the floquet setup calls
`pcg->SetInitialGuess(0)` (`palace/linalg/floquetcorrection.cpp:61`), the
`initial_guess == false` precondition holds, so `CgSolver::Mult` takes its
else-branch (`palace/linalg/iterative.cpp:382-386`):

    else
    {
      r = b;      // :384 — copy RHS into the residual register FIRST
      x = 0.0;    // :385 — THEN zero the (possibly aliased) destination
    }

The `r = b;` at `:384` reads `b` into the residual register **before** the
`x = 0.0;` at `:385` zeros the destination — so even when `b` and `x` alias the
same buffer (`rhs`), the read of `b` completes before the write of `x`, and the
solve proceeds correctly. The tolerance is therefore **conditional**: it holds
*because* `SetInitialGuess(0)` selected the else-branch. Had `initial_guess`
been true, the if-branch (`palace/linalg/iterative.cpp:377-381`) would compute
`A->Mult(x, r)` — reading `x` before `r = b` — which under `b == x` aliasing
would read the not-yet-set RHS and break the fusion. This conditional aliasing
tolerance is the source of the buffer economy that the AddMult fusion exists
for; reversing the fusion at L1 requires the same applicability guarantee — and
the guarantee in turn rests on the `SetInitialGuess(0)` setup choice.
```

### Edit 2 — Sub-pattern B Citations list (widen)

```edit:book/src/L1-L0/floquet-correction-mutation-rotation.md
Citations:

- `palace/linalg/floquetcorrection.cpp:80-86` — `AddMult(const VecType &x,
  VecType &y, ScalarType a) const` (signature `:80-81`, body `:82-86` with
  `this->Mult(x, rhs)` at `:83`, `rhs *= a` at `:84`, `y += rhs` at `:85`,
  close brace `:86`).
- `palace/linalg/floquetcorrection.hpp:59` — `void AddMult(const VecType &x,
  VecType &y, ScalarType a = 1.0) const;` (decl; default `a = 1.0` makes the
  no-scale apply-and-accumulate `Mult-and-add`).
- `palace/linalg/ksp.cpp:297` — `BaseKspSolver<OperType>::Mult(const VecType
  &x, VecType &y) const` (the **delegation wrapper** on the aliased call-path:
  `:300` forwards `ksp->Mult(x, y)` to the inner CG solver; carries no aliasing
  logic itself — this is the call-path, not the mechanism).
- `palace/linalg/iterative.cpp:361` — `CgSolver<OperType>::Mult(const VecType
  &b, VecType &x) const` (the **true aliasing-tolerance mechanism**; signature
  `:361`, the `template` line is `:360`). With `initial_guess == false` the
  else-branch (`:382-386`) runs `r = b;` (`:384`) **before** `x = 0.0;` (`:385`),
  copying the RHS into the residual register before zeroing the aliased
  destination — so `b == x` aliasing is safe. The `if (this->initial_guess)`
  test is at `:377`; the aliasing-unsafe if-branch is `:377-381`.
- `palace/linalg/floquetcorrection.cpp:61` — `pcg->SetInitialGuess(0)` (the
  `initial_guess == false` **precondition** that gates the aliasing-safe
  else-branch; `pcg` is the `CgSolver` made at `:60`, wrapped into `F.ksp` at
  `:66`). The aliasing tolerance is conditional on this setup choice.
```

### Edit 3 — Applicability condition 2 (re-frame)

```edit:book/src/L1-L0/floquet-correction-mutation-rotation.md
2. **Inner ksp accepts input/output aliasing (conditional on `SetInitialGuess(0)`).**
   The `AddMult` body's nested `this->Mult(x, rhs)` call binds `Mult`'s output
   argument to the scratch member, and `Mult`'s step-2 body `ksp->Mult(rhs,
   y_arg = rhs)` therefore calls the inner ksp with `b == x` (input RHS and
   output destination aliased to the same buffer). The inner `BaseKspSolver::Mult`
   (`palace/linalg/ksp.cpp:297`) is a thin delegation wrapper that forwards to
   `ksp->Mult(x, y)` (`:300`); the wrapped `CgSolver<OperType>::Mult`
   (`palace/linalg/iterative.cpp:361`) is what tolerates the aliasing — **but
   only because** `pcg->SetInitialGuess(0)` (`palace/linalg/floquetcorrection.cpp:61`)
   sets `initial_guess == false`, selecting the else-branch
   (`palace/linalg/iterative.cpp:382-386`) which copies `r = b;` (`:384`) before
   `x = 0.0;` (`:385`) — reading the RHS into the residual register before
   zeroing the aliased destination. **A lowering that re-derives the inner solve
   with `initial_guess == true` (the if-branch `:377-381`, which computes
   `A->Mult(x, r)` and reads `x` first) breaks the AddMult fusion under
   aliasing.** This condition is **specific to this theme** (the
   divfree-projector AddMult-free apply does not have this concern) and its
   safety rests on the `SetInitialGuess(0)` construction-time choice.
```

### Edit 4 — Verified-against L0 list (widen the ksp.cpp:297 entry)

```edit:book/src/L1-L0/floquet-correction-mutation-rotation.md
- `palace/linalg/ksp.cpp:297` — `BaseKspSolver<OperType>::Mult` (the
  **delegation wrapper** on the aliased AddMult call-path; `:300` forwards to
  the inner CG solver, carrying no aliasing logic itself).
- `palace/linalg/iterative.cpp:360-386` — `CgSolver<OperType>::Mult` (the
  **true aliasing-tolerance mechanism** the AddMult fusion requires; signature
  `:361`, `if (this->initial_guess)` `:377`, aliasing-safe else-branch
  `:382-386` with `r = b;` `:384` before `x = 0.0;` `:385`).
- `palace/linalg/floquetcorrection.cpp:61` — `pcg->SetInitialGuess(0)` (the
  `initial_guess == false` precondition that gates the aliasing-safe
  else-branch; makes the AddMult aliasing tolerance load-bearing-safe).
```

### Edit 5 — Upgrade the `verified_against:` ksp.cpp:297 row + add two mechanism rows

Replace the single `partially-supports` `ksp.cpp:297` row (currently in the
`# Sub-pattern B` group of the fenced `verified_against:` block) with the
upgraded `supports` wrapper row plus the two new mechanism rows. The block stays
one ` ```yaml ` fence; only these three rows change. Shown here as the
replacement for the existing single row:

```edit:book/src/L1-L0/floquet-correction-mutation-rotation.md
  - citation: palace/linalg/ksp.cpp:297
    verdict: supports
    audited_at: 2026-05-31T215306Z
    note: BaseKspSolver<OperType>::Mult :297 is the DELEGATION WRAPPER (call-path, not mechanism) — :299 BlockTimer, :300 ksp->Mult(x,y) forwards verbatim to the inner CgSolver::Mult. Re-anchored cycle-039 D2 — the AddMult aliasing-tolerance MECHANISM is at CgSolver::Mult, see the iterative.cpp:360-386 and floquetcorrection.cpp:61 rows below (citecheck OK).
  - citation: palace/linalg/iterative.cpp:360-386
    verdict: supports
    audited_at: 2026-05-31T215306Z
    note: CgSolver<OperType>::Mult(const VecType &b, VecType &x) sig at :361 (:360 is the template line; planner hinted :360 — +1 drift corrected to :361) — the TRUE aliasing-tolerance mechanism. With initial_guess==false the else-branch :382-386 runs r = b; (:384) x = 0.0; (:385) — copies b into r BEFORE zeroing the aliased x, so when AddMult passes b==x==rhs the read of b precedes the write of x and aliasing is safe. The if(this->initial_guess) test is at :377; the aliasing-unsafe if-branch is :377-381. citecheck OK on :361/:377/:384/:385.
  - citation: palace/linalg/floquetcorrection.cpp:61
    verdict: supports
    audited_at: 2026-05-31T215306Z
    note: pcg->SetInitialGuess(0) sets the initial_guess==false precondition that gates the CgSolver::Mult else-branch — without it the if-branch at iterative.cpp:377-381 reads x (A->Mult(x,r)) before r is set, which WOULD break b==x aliasing. This SetInitialGuess(0) is what makes the AddMult aliasing tolerance load-bearing-safe (citecheck OK, anchor lit).
```

(The `# Sub-pattern B` group comment and the surrounding `floquetcorrection.cpp:80-86`
/ `floquetcorrection.hpp:59` rows are unchanged; the three rows above replace the
single former `palace/linalg/ksp.cpp:297` `partially-supports` row in that group.)

### Edit 6 — §Status firmness-justification paragraph (re-frame the last ksp.cpp:297 mechanism-attribution)

The §Status "No partly-constructive caveat applies" paragraph is the **sixth and
final** `ksp.cpp:297` mention site, and the one that still names the *wrapper* as
the positive mechanism-evidence for the AddMult aliasing applicability — the
exact misattribution Edits 1/3/4 reframe at the other five sites. Re-frame it the
same way: `ksp.cpp:297` is the delegation wrapper / call-path; the positive
mechanism site is `CgSolver::Mult` (`iterative.cpp:361`, else-branch `:382-386`
with `r = b;` `:384` before `x = 0.0;` `:385`) gated by `SetInitialGuess(0)`
(`floquetcorrection.cpp:61`). Theme stays `firm` — the firm-on-positive-structure
justification is unchanged; only the cited positive site is corrected to the true
mechanism. (citecheck OK: `iterative.cpp:361`/`floquetcorrection.cpp:61` both
anchor-lit on-disk.)

```edit:book/src/L1-L0/floquet-correction-mutation-rotation.md
**No partly-constructive caveat applies.** This theme has a positive source
site for every step, including the AddMult fusion's load-bearing aliasing
applicability — its positive mechanism site is `CgSolver<OperType>::Mult`
(`palace/linalg/iterative.cpp:361`, the aliasing-safe else-branch
`:382-386` runs `r = b;` (`:384`) before `x = 0.0;` (`:385`)), gated by the
`pcg->SetInitialGuess(0)` precondition (`palace/linalg/floquetcorrection.cpp:61`);
`palace/linalg/ksp.cpp:297` is the `BaseKspSolver::Mult` delegation wrapper on
the call-path (it forwards `ksp->Mult(x, y)` at `:300`), not the mechanism. The L1
anchor is firm-on-positive-structure (the `divfree-projector` / `jacobi-smoother`
/ `chebyshev-smoother` precedent), so this theme is firm at birth.
```

## Supporting evidence

- `reference/palace/palace/linalg/iterative.cpp:358-402` — `CgSolver::Mult`
  signature + initialize block (read for the if/else aliasing mechanism).
- `reference/palace/palace/linalg/ksp.cpp:297-305` — `BaseKspSolver::Mult`
  wrapper (read to confirm it delegates, carries no aliasing logic).
- `reference/palace/palace/linalg/floquetcorrection.cpp:60-67` — `F.ksp` setup
  (`CgSolver` → `SetInitialGuess(0)` → `BaseKspSolver` wrap → `SetOperators`).
- `tools/citecheck/citecheck.py --anchor` runs (on-disk, source-of-truth):
  `iterative.cpp:361` (`CgSolver<OperType>::Mult`), `:377` (`initial_guess`),
  `:384` (`r = b`), `:385` (`x = 0.0`), `floquetcorrection.cpp:61`
  (`SetInitialGuess(0)`) — all lit. `iterative.cpp:360` anchor `CgSolver`
  reported `[DRIFT] +1`, corrected to `:361`.

## Open questions / caveats

- **OQ CLOSURE — `floquet-corrector-addmult-aliasing-applicability-audit`.** This
  dispatch enacts the cycle-038 audit's identified edits: the AddMult inner-ksp
  aliasing-tolerance mechanism is now correctly anchored to `CgSolver::Mult`
  (`iterative.cpp:361`, else-branch `:382-386`) gated by `SetInitialGuess(0)`
  (`floquetcorrection.cpp:61`), with `ksp.cpp:297` re-framed as the delegation
  wrapper. The `verified_against:` row is upgraded `partially-supports` →
  `supports`. **The OQ can be CLOSED** (integrator promotes). No residual
  evidence gap on the aliasing applicability sub-claim — the re-anchor covers
  **all six** `ksp.cpp:297` mention sites in the theme, including the §Status
  firmness-justification paragraph (Edit 6), so no surviving site names the
  delegation wrapper as the mechanism-evidence.
- **Planner-hint drift carry-forward (mechanical).** The cycle-039 planner
  pre-localized the `CgSolver::Mult` signature as `iterative.cpp:360`; on-disk
  `citecheck --anchor 'CgSolver'` resolves it to `:361` (`:360` is the
  `template <typename OperType>` line). I cite `:361` for the signature and the
  range `:360-386` (template-line through close-brace) in the verified_against
  block. This is the codemap-read-range-plus-one-drift-on-brace-boundary pattern
  the discipline warns about — on-disk citecheck is authoritative; recorded so
  the integrator carries the corrected line forward, not the hint.
- **Theme remains `firm`; structural rewrite untouched.** The AddMult-as-axpy
  structural rewrite (`floquetcorrection.cpp:80-86`) and all other sub-patterns
  (A/C/D) are unchanged. This re-anchor only completes the evidence for the
  Sub-pattern B aliasing applicability sub-claim, which was previously
  misattributed but whose *conclusion* (aliasing is safe) was always correct.
- **Pre-existing OQ retained (not in scope here):**
  `floquet-correction-real-vector-instantiation-dead-code` (Sub-pattern D
  `<Vector>` dead-code) is unaffected by this dispatch and stays open.
