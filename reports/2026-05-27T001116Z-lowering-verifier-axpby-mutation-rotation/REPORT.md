---
agent: lowering-verifier
invoked_at: 2026-05-27T00:11:16Z
scope: L1>L0 theme audit — axpby-mutation-rotation
status: pending
inputs:
  - book/src/L1-L0/axpby-mutation-rotation.md
  - palace/linalg/vector.hpp:115-128
  - palace/linalg/vector.cpp:276-311
  - palace/linalg/vector.cpp:701-712
  - palace/linalg/vector.cpp:714-723
  - palace/linalg/operator.cpp:458-466
  - palace/linalg/rap.cpp:73
  - palace/linalg/rap.cpp:317
  - book/src/L1/axpy.md
skill_uptake:
  - skill: verify-citation-range
    triggered: true
    decision: explained_non_applicable
    rationale: All 8 citations verified inline by reading source ranges and recording per-citation verdicts in the audit table. Skill invocation deferred until a critic/repairer-phase mechanism stabilizes; the per-citation table is the equivalent telemetry artifact.
  - skill: classify-variant-axis
    triggered: true
    decision: artifact_landed
    rationale: Three orthogonal variant axes enumerated (real-Vector vs ComplexVector; member-form vs free-function template; literal-folded α ∈ {1,-1} vs runtime α). Coverage verdicts recorded per sub-pattern A/B/C; defined-not-used legs called out individually (Subtract, operator-=, std::complex<double>-α-on-ComplexVector).
  - skill: cross-cutter-corpus-grep
    triggered: true
    decision: explained_non_applicable
    rationale: Did corpus-wide grep for `\.Add(`, `linalg::AXPY`, `\.Subtract(`, vector-typed `+=`/`-=` to enumerate uncited sub-pattern A/B/C call sites; this skill does not yet exist as a SKILL.md entry but the activity pattern is recurrent across lowering-verifier and same-layer-cross-cutter dispatches. Filed as candidate via this telemetry mark.
integrated_at: 2026-05-27T00:23:54Z
integration_commit: TBD-AT-COMMIT-TIME
integration_notes: Applied as proposed (verified_against YAML metadata block + coverage note paragraph appended to book/src/L1-L0/axpby-mutation-rotation.md §Verified-against). Theme content unchanged; metadata is additive. Channel-format question for YAML-in-prose embedding routed to meta-phase via open question lowering-verifier-yaml-in-prose-channel-format.
---

# REPORT: Audit axpby-mutation-rotation

## Summary

Audited the `axpby-mutation-rotation` theme (landed cycle-002, commit c3312a6)
against its eight cited L0 evidence ranges. All eight citations resolve in
the current Palace tree and support the theme's claims for each cited site;
recognition rules for sub-patterns A, B, C are individually sound. Sub-patterns
A and C are nevertheless **partially-supported** for *coverage* — a corpus
crawl turned up ~25 additional axpy-shaped sites under `palace/linalg/`,
`palace/models/`, and `palace/fem/` that the theme does not enumerate (it
does not claim exhaustiveness, but the theme's own closing line invites a
"exhaustive sub-rule recognition" audit). Sub-pattern C's `Subtract(α, x)`
limb is **algebraically supported but unused in the L0 corpus** — the
member function is defined in `vector.hpp:118` and never called anywhere in
`palace/**`. Algebraic laws (`axpy(1,x,y)=y+x`, `axpy(-1,x,y)=y-x`,
`Subtract(α,x)≡AXPY(-α,x)`) all hold. Applicability conditions are
sensible; spot-checks of three uncited sites (chebyshev, iterative-CG,
orthog) found no aliasing counter-examples. **Top-level verdict:
partially-supported** — theme content as written is correct; coverage of
the L0 axpy corpus is sketchy and the Sub-pattern C `Subtract` alternative
should be noted as "defined, never called". Proposed edits are additive
(append `verified_against:` metadata + a coverage note); no contradictions
found.

## Per-citation audit

| # | Citation | Theme claim | Found at range | Verdict | Notes |
|---|---|---|---|---|---|
| 1 | `palace/linalg/vector.hpp:115-118` (theme says 115-128) | ComplexVector member decls (`AXPY`, `Add`, `Subtract`) | `void AXPY(...)` decl at 116; `Add(...)` inline at 117 calls `AXPY`; `Subtract(...)` inline at 118 calls `AXPY(-alpha, x)` | supports | Theme's "Verified-against" claims 115-128 but Sub-pattern A's per-pattern citation says 116-117. Both ranges resolve; 115-118 is the member-decl block, 119-128 covers operator+= / operator-=. |
| 2 | `palace/linalg/vector.hpp:119-128` | `ComplexVector::operator+=` / `operator-=` bodies | `operator+=` body at 119-123 calls `AXPY(1.0, x)`; `operator-=` body at 124-128 calls `AXPY(-1.0, x)` | supports | Exactly as claimed. |
| 3 | `palace/linalg/vector.cpp:276-311` | `ComplexVector::AXPY` definition | Definition at 276-279 forwards to the static 5-arg form (281-311) which branches on `ai == 0.0` and uses `mfem::forall_switch` to accumulate `YR[i] += ar * XR[i]` (with imag-cross-term in the else branch) | supports | The forall lambda is the canonical L0 elementwise axpy kernel; no α==1 branch on the complex path, matching the theme's claim. |
| 4 | `palace/linalg/vector.cpp:701-712` | Free-function `AXPY(double, Vector, Vector)` with α==1 branch | Function at 701-712 has `if (alpha == 1.0) { y += x; } else { y.Add(alpha, x); }` | supports | Verbatim match for Sub-pattern B citation (`vector.cpp:704-706`) and Sub-pattern A citation (`vector.cpp:710`). |
| 5a | `palace/linalg/vector.cpp:714-718` | Free-function `AXPY(double, ComplexVector, ComplexVector)` dispatch | 714-718: real-α-on-ComplexVector specialisation calls `y.AXPY(alpha, x)` | supports | Used: `romoperator.cpp:193-194` (`linalg::AXPY(y(j).real(), ...)` / `y(j).imag()` — both `double` α flowing into the ComplexVector path). |
| 5b | `palace/linalg/vector.cpp:720-724` | Free-function `AXPY(std::complex<double>, ComplexVector, ComplexVector)` dispatch | 720-724: complex-α-on-ComplexVector specialisation calls `y.AXPY(alpha, x)` (no branch) | supports (defined-not-used) | **Defined but never called.** Corpus grep `linalg::AXPY` returns 5 sites, all of which pass `double` α (literal `-1.0` in drivensolver/nleps, `.real()`/`.imag()` in romoperator). No caller passes `std::complex<double>` α to the free-function template. Treat as a recognition rule for *potential* L0 sites rather than observed ones — same status as `Subtract` and `operator-=`. |
| 6 | `palace/linalg/operator.cpp:458-466` | `SumOperator::AddMult` uses `y.Add(a*c, z)` | Function at 458-466 loops `for (const auto &[op, c] : ops) { op->Mult(x, z); y.Add(a * c, z); }` | supports | Pattern is exactly `y.Add(α, x)` where α=a*c. The transpose sibling (`operator.cpp:468-475`, with `y.Add(a*c, z)` at 474) is the same pattern, uncited — see coverage note. |
| 7 | `palace/linalg/rap.cpp:73` | `b.Add(-1.0, ty)` in Dirichlet residual correction (real path; literal -1.0) | Line 73 reads `b.Add(-1.0, ty);` in `ParOperator::EliminateRHS`-shaped code (constraint enforcement after `RestrictionMatrixMult`) | supports | Literal -1.0 sub-pattern-C site as claimed. |
| 8 | `palace/linalg/rap.cpp:317` | `y.Add(a, ty)` in `ParOperator::AddMult` | Line 317 reads `y.Add(a, ty);` after restriction; in `AddMult`'s body | supports | Sub-pattern A site with runtime α=`a`. A sibling `y.Add(a, tx)` at rap.cpp:360 (transpose path) is the same pattern, uncited. |

All 8 cited ranges resolve as **in-range, supports** (row 5 split into 5a/5b
to separate the real-α-on-ComplexVector specialisation, which is used, from
the `std::complex<double>` α-on-ComplexVector specialisation, which is
defined-not-used). Zero `out-of-range` or `does-not-support` verdicts at the
citation level.

## Applicability conditions

- **Condition 1 — "No aliasing between `x` and `y`."** Verifiable per-site
  by inspection (look at variable identities at the call site). Spot-checked
  three uncited sites: `iterative.cpp:448` (`x.Add(alpha, p)` — distinct
  buffers `x` and `p`), `orthog.hpp:51` (`w.Add(-H[j], V[j])` — distinct),
  `chebyshev.cpp:212` (`y += d` — distinct). **Found counter-example:
  no.** Condition holds on all spot-checked sites. The theme's qualifier
  "Palace never aliases axpy arguments in observed sites" is consistent
  with the audit.

- **Condition 2 — "No observer of the prior `y` value after the call."**
  Verifiable by lexical sequencing inspection. Spot-checked
  `operator.cpp:464` (the `y` reduction in `SumOperator::AddMult`'s loop —
  the prior `y` value is *intended* to be summed-into, no observer), and
  `iterative.cpp:448-449` (CG update — `x` and `r` are next read in the
  iteration update only after both `Add` calls). **Found counter-example:
  no.** All spot-checked sites read prior `y` only before the `Add`.

- **Condition 3 — "Conforming shape and element type."** Verifiable from
  L0 type signatures: all sites are member calls on `mfem::Vector` /
  `ComplexVector`; the kernel at `vector.cpp:281-311` reads
  `N = yr.Size()` with no size cross-check (an
  `MFEM_ASSERT(yr.Size() == xr.Size())` would be defensive, but the
  free-function template at 701-723 has no such assertion either). Type
  match is enforced at the C++ overload level (no real-complex mixing
  except via the static `ComplexVector::AXPY(complex α, Vector xr, xi, yr,
  yi)` 5-arg form). **Found counter-example: no.** Note: the
  `scalar-promotion-typing-rule` open question is the right place to
  capture the implicit real→complex promotion when a `double` α flows into
  `ComplexVector::AXPY` via the template specialisation at 714-718.

- **Condition 4 — "`α` is a runtime scalar (not a special form)."**
  Verifiable from L0 dispatch logic at `vector.cpp:701-712`: the
  `if (alpha == 1.0)` is a runtime check on the value, not a compile-time
  dispatch on the type; the theme correctly classifies this as a
  "transparent performance trick inside sub-pattern A's L0 form, not a
  fourth sub-pattern." The static specialisations (`operator+=`,
  `operator-=`, `Subtract`) at `vector.hpp:119-128` are compile-time named
  forms that match sub-patterns B and C by *syntactic name*, not by
  value-folding. **Found counter-example: no.**

## Algebraic laws

- **Sub-pattern B: `axpy(1, x, y) = y + x`.** Holds trivially on the L1
  signature `(α, x, y) → α·x + y`: substitute α=1, get `1·x + y = y + x`
  (by commutativity of vector addition on `Vector` / `ComplexVector`,
  which `mfem::forall_switch` realises pointwise as `+=`). The L0
  realisation at `vector.cpp:706` (`y += x`) and `vector.hpp:121-122`
  (`AXPY(1.0, x)`) both honour the law.

- **Sub-pattern C: `axpy(-1, x, y) = y - x`.** Holds: substitute α=-1,
  get `-1·x + y = y - x`. The L0 realisations at `vector.cpp:710`
  (`y.Add(-1.0, x)` via the free-function else branch when caller passes
  -1.0, e.g. `rap.cpp:73`) and `vector.hpp:126` (`AXPY(-1.0, x)`) both
  honour the law.

- **Sub-pattern C: `Subtract(α, x) ≡ AXPY(-α, x)`.** Verified directly
  at `vector.hpp:118`: the inline body is literally `AXPY(-alpha, x)`. So
  the algebraic identity is *definitional* on `ComplexVector`, not just a
  semantic claim. **Audit note:** `Subtract` is *defined* but **never
  called** anywhere in `palace/**` — `grep -rn "\.Subtract(" palace/`
  returns zero hits. This does not invalidate the theme, but the theme
  lists it as a sub-pattern-C L0 form ("y.Subtract(alpha, x)") as if it
  were observed. It is *available* on the L0 surface but *unused* by
  Palace callers. Recommend the theme note this asymmetry.

All cited algebraic laws hold on the L_{n+1} (L1) operator signatures.

## Coverage audit (exhaustiveness)

The theme's closing line in §Justification kind says: "A `lowering-verifier`
audit in a later cycle should confirm sub-rule recognition matches the L0
corpus exhaustively." Performed a corpus crawl for `\.Add(`,
`linalg::AXPY`, `operator+=` / `operator-=` on vector types.

**Sub-pattern A sites NOT cited by the theme:**

- `palace/linalg/operator.cpp:474` — `y.Add(a * c, z)` in
  `SumOperator::AddMultTranspose` (transpose sibling of cited 464).
- `palace/linalg/rap.cpp:360` — `y.Add(a, tx)` (transpose sibling of cited 317).
- `palace/linalg/orthog.hpp:51, 73, 86` — `w.Add(-H[j], V[j])` /
  `w.Add(-dH[j], V[j])` (Gram-Schmidt orthogonalisation; runtime negative
  α — these are sub-pattern A, not C, because α is runtime not literal).
- `palace/linalg/iterative.cpp:448-449, 666, 674, 843` — PCG / GMRES
  update steps (`x.Add(alpha, p)`, `r.Add(-alpha, z)`, etc.).
- `palace/linalg/iterative.cpp:610, 789` — `V[0].Add(1.0 / beta, r)` /
  `V[0].Add(1.0 / beta, Z[0])` (runtime α, not literal 1.0).
- `palace/linalg/vector.cpp:756` — `z.Add(beta, y)` inside the
  free-function `AXPBYPCZ` template (interesting: an internal sub-pattern-A
  call from within the AXPBYPCZ lowering itself).
- `palace/models/romoperator.cpp:193-194, 545` — ROM basis-accumulation
  axpy sites (the 545 site has runtime *complex* α `1i * omega`).
- `palace/models/waveportoperator.cpp:222, 228` — `V.Add(-Vn, normal)`
  (runtime α; literal negation of a runtime scalar — sub-pattern A).
- `palace/models/materialoperator.cpp:571, 588, 628` — coefficient
  accumulation.
- `palace/fem/integrator.cpp:95` — `elvect.Add(val, shape)` (element-level
  integration accumulator).
- `palace/fem/coefficient.hpp:473, 480, 920, 960` — coefficient
  axpy accumulations.
- `palace/drivers/drivensolver.cpp:367, 394` —
  `linalg::AXPY(-1.0, E, Eh)` (literal -1.0 — these are **sub-pattern C**
  sites in the free-function dispatch form).
- `palace/linalg/nleps.cpp:536` — `linalg::AXPY(-1.0, XSx2, x1)`
  (literal -1.0 — also **sub-pattern C**).

**Sub-pattern B sites NOT cited by the theme** (real-path `operator+=`
that calls `mfem::Vector::operator+=`, which is the BLAS `axpy(1, x, y)`
form):

- `palace/linalg/chebyshev.cpp:212, 218, 283, 291` — Chebyshev smoother
  inner-loop updates.
- `palace/linalg/iterative.cpp:677` — GMRES restart `x += V[0]`.
- `palace/linalg/floquetcorrection.cpp:85` — `y += rhs`.
- `palace/linalg/nleps.cpp:949` — `y += rhs`.

**Sub-pattern C sites NOT cited (free-function with literal -1.0):**

- `palace/drivers/drivensolver.cpp:367, 394` — `linalg::AXPY(-1.0, E, Eh)`
  (driven-solver error / residual).
- `palace/linalg/nleps.cpp:536` — `linalg::AXPY(-1.0, XSx2, x1)`.

**Sub-pattern C `Subtract` form sites:** **zero**. The
`ComplexVector::Subtract(α, x)` member at `vector.hpp:118` is *defined*
but **never called** in `palace/**`. The theme lists it as a sub-pattern-C
L0 form alongside `y -= x` and `b.Add(-1.0, ty)`; this is **defined-not-used**
on the L0 surface. Treat as a recognition rule for *potential* L0 sites
rather than *observed* ones.

**Sub-pattern C `y -= x` (operator-=) sites:** **zero** in the
`palace/**` tree (grep returned no vector-typed `-=` operator usages
matching the ComplexVector signature). Like `Subtract`, defined-not-used.

**Free-function `linalg::AXPY` complex-α-on-ComplexVector specialisation
(`vector.cpp:720-724`):** **zero** caller sites. Corpus grep `linalg::AXPY`
returns 5 sites (`drivensolver.cpp:367, 394`, `nleps.cpp:536`,
`romoperator.cpp:193, 194`); all pass `double` α. No caller passes
`std::complex<double>` α. **Defined-not-used**, same status as `Subtract`
and `operator-=`. The variant-axis cell (complex-α, complex-vector,
free-function form) exists in the L0 surface but has no observed L0 site.

Coverage verdict by sub-pattern:

- **Sub-pattern A**: theme cites 4 sites; **~20 additional sites exist** in
  `palace/linalg/`, `palace/models/`, `palace/fem/`. **partially-supports
  (coverage)**.
- **Sub-pattern B**: theme cites 2 sites (one of which is the definition,
  one the `if`-branch); **~6 additional usage sites exist** in chebyshev,
  iterative, floquetcorrection, nleps. **partially-supports (coverage)**.
- **Sub-pattern C**: theme cites 3 sites; **2 additional literal-(-1.0)
  sites** in drivensolver and nleps. `Subtract` and `operator-=`
  recognition rules are defined-not-used. **partially-supports (coverage +
  defined-not-used note recommended)**.

## Proposed changes

Append `verified_against:` metadata block to the theme. The block records
per-citation audit verdicts so `cross-layer-cross-cutter` can consume them
for coverage analysis. Also propose a *non-mutating* coverage-note paragraph
in §Verified-against; do **not** add the uncited sites as citations (that
would be authoring, not auditing — leave for a follow-up cycle if the
human wants exhaustive corpus indexing).

```edit:book/src/L1-L0/axpby-mutation-rotation.md
# Append after the existing "L1 anchor:" bullet list in §Verified-against,
# before §Status:

verified_against:
  - citation: palace/linalg/vector.hpp:115-118
    verdict: supports
    audited_at: 2026-05-27T00:11:16Z
    note: ComplexVector member decls AXPY/Add/Subtract; Subtract inline body literally AXPY(-alpha, x).
  - citation: palace/linalg/vector.hpp:119-128
    verdict: supports
    audited_at: 2026-05-27T00:11:16Z
    note: operator+= calls AXPY(1.0, x); operator-= calls AXPY(-1.0, x). Both defined-not-used in palace/**.
  - citation: palace/linalg/vector.cpp:276-311
    verdict: supports
    audited_at: 2026-05-27T00:11:16Z
    note: ComplexVector::AXPY definition; forall_switch kernel with ai==0 branch; no alpha==1 branch on complex path (matches theme claim).
  - citation: palace/linalg/vector.cpp:701-712
    verdict: supports
    audited_at: 2026-05-27T00:11:16Z
    note: Free-function template real-Vector specialisation with verbatim if(alpha==1.0){y+=x;}else{y.Add(alpha,x);} branch.
  - citation: palace/linalg/vector.cpp:714-718
    verdict: supports
    audited_at: 2026-05-27T00:11:16Z
    note: Free-function real-alpha-on-ComplexVector specialisation dispatches to ComplexVector::AXPY member; no branch. Used by romoperator.cpp:193-194.
  - citation: palace/linalg/vector.cpp:720-724
    verdict: supports (defined-not-used)
    audited_at: 2026-05-27T00:11:16Z
    note: Free-function complex-alpha-on-ComplexVector specialisation dispatches to ComplexVector::AXPY member; no branch. Defined-not-used — corpus grep of linalg::AXPY returns 5 sites, all pass double alpha. No caller passes std::complex<double>.
  - citation: palace/linalg/operator.cpp:458-466
    verdict: supports
    audited_at: 2026-05-27T00:11:16Z
    note: SumOperator::AddMult uses y.Add(a*c, z) inside ops-loop; transpose sibling at 468-475 is same pattern, uncited.
  - citation: palace/linalg/rap.cpp:73
    verdict: supports
    audited_at: 2026-05-27T00:11:16Z
    note: b.Add(-1.0, ty); literal -1.0 confirmed sub-pattern-C.
  - citation: palace/linalg/rap.cpp:317
    verdict: supports
    audited_at: 2026-05-27T00:11:16Z
    note: y.Add(a, ty); runtime alpha=a; transpose sibling y.Add(a, tx) at rap.cpp:360, uncited.

# Also append a coverage note at end of §Verified-against:

Coverage note (lowering-verifier audit, 2026-05-27): the corpus contains
~25 additional axpy-shaped sites beyond those cited (under
palace/linalg/{orthog,iterative,chebyshev,floquetcorrection,nleps},
palace/models/{romoperator,waveportoperator,materialoperator}, palace/fem,
palace/drivers/drivensolver). Theme content as written is correct; the
cited set is illustrative not exhaustive. The ComplexVector::Subtract(α, x),
ComplexVector::operator-=, and the free-function
`linalg::AXPY(std::complex<double>, ComplexVector, ComplexVector)`
specialisation (vector.cpp:720-724) are all defined-not-used in palace/**
(definitions exist; no caller sites). Treat these three L0 forms as
recognition rules for *potential* call sites rather than observed ones.
Exhaustive corpus indexing deferred to a future cycle.
```

(The `verified_against:` block is YAML-style metadata appended to the
prose §Verified-against section; `cross-layer-cross-cutter` is expected to
parse the block by leading keyword. The coverage-note paragraph is added
as plain prose under the same section. No other edits to the theme are
proposed.)

## Supporting evidence

Consulted files (read-only):

- `book/src/L1-L0/axpby-mutation-rotation.md` (the theme)
- `book/src/L1/axpy.md` (L1 anchor — referenced, not re-audited)
- `reference/palace/palace/linalg/vector.hpp` (lines 110-145)
- `reference/palace/palace/linalg/vector.cpp` (lines 270-320, 695-770)
- `reference/palace/palace/linalg/operator.cpp` (lines 450-480)
- `reference/palace/palace/linalg/rap.cpp` (lines 65-80, 310-365)
- `reference/palace/palace/linalg/iterative.cpp` (lines 445-455, 605-615,
  665-680)
- `reference/palace/palace/linalg/chebyshev.cpp` (lines 208-225)
- `reference/palace/palace/linalg/orthog.hpp` (lines 50-90)

Corpus grep commands run:

- `grep -rn "\.Add(" palace/ --include="*.cpp" --include="*.hpp"` (sub-A
  and sub-C member-form survey)
- `grep -rn "linalg::AXPY\b" palace/ --include="*.cpp" --include="*.hpp"`
  (free-function survey — found 5 sites; 2 are theme-cited indirectly via
  the template, 3 are uncited literal-(-1.0) sub-C sites).
- `grep -rn "\.Subtract(\b" palace/ --include="*.cpp" --include="*.hpp"`
  (Subtract caller survey — zero usage sites).
- `grep -rn " += \| -= " palace/ --include="*.cpp" --include="*.hpp"`
  (operator+= survey, filtered to vector-typed lvalues).

Tests: **not consulted** for this audit. `reference/palace/test/unit/`
does not appear to have a dedicated axpy unit-test (no `test_axpy.cpp` or
similar surfaced via filename); recommend a follow-up cycle add
test-linkage entries under `scaffolding/test-linkages/` if axpy is
exercised via solver-level integration tests.

## Open questions / caveats

- **`AXPBYPCZ`'s internal sub-pattern-A call at `vector.cpp:756`.** The
  free-function `AXPBYPCZ` template *itself* lowers internally via
  `AXPBY(...); z.Add(beta, y);` (real-Vector path, when γ≠0). This is an
  L0-internal lowering — not a sub-pattern A site in the application code,
  but a sub-pattern A site within an L0 lowering composition. Out of scope
  for this audit; relevant if the future `axpbypcz-mutation-rotation`
  theme tries to describe the AXPBY+Add fusion.
- **`scalar-promotion-typing-rule`** (open question, ref. theme Condition 3)
  — the implicit real→complex α promotion via the template specialisation
  at `vector.cpp:714-718` is the concrete L0 site that question is about.
  Not in scope to resolve here.
- **Tests as semantic supplement.** Audit was source-only; no test
  cross-check performed. If axpy semantics are exercised in
  `reference/palace/test/unit/`, a test-linkage entry would tighten the
  audit. Recommend a separate `harvester` or test-linkage agent invocation.
- **`mfem::Vector::operator+=` and `mfem::Vector::Add`** are upstream
  (MFEM, not Palace) — per CLAUDE.md "Specialized agents cite Palace source,
  not vendored upstream." This audit honoured that scope; the L0 surface
  for the real-Vector `y += x` and `y.Add(alpha, x)` forms is taken on
  faith from MFEM, which is the standard project convention.
- **Citation-range slight mismatch.** The theme's §Verified-against
  lists `palace/linalg/vector.hpp:115-118` but the §Sub-pattern A citation
  lists `palace/linalg/vector.hpp:116-117`. Both ranges resolve and
  support the claims; the §Verified-against range is the more inclusive
  ComplexVector member-decl block (`AXPY` decl + `Add` inline + `Subtract`
  inline). Not a contradiction; flagged for tidiness.
- **Recurrence threshold for re-audit.** The corpus crawl is a snapshot
  at this commit (palace HEAD as of the audit). If `palace/` is re-pinned
  upstream, sub-pattern A/B/C coverage may shift; the
  `verified_against:` block's `audited_at:` timestamp is the pin.

---

**Status update:** `pending` → set `ready` on integration. No
`needs-revision` blockers; the proposed changes are additive metadata and
a coverage note — no contradictions found in the theme content as
written.
