---
agent: same-layer-cross-cutter
invoked_at: 2026-05-29T19:48:49Z
scope: L1 cross-cut — shared rough-in→firm test-coverage gate of matrix-weighted-norm + bilinear-form
status: integrated
integrated_at: 2026-05-29T205500Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-028 position 6/7 (per-report). SURVEY/observation dispatch — NO book/ mutation (no proposed-changes block). Sole integration action = 4 OQ promotions. ASK-class verdict: BOTH matrix-weighted-norm + bilinear-form STAY rough-in (no dedicated test at the weighted entry point in the 23-file corpus; gates need an out-of-scope Palace-source change) — no promotion enacted. matrix-weighted-norm-mixed-element-type-variant OQ NARROWED (not closed — element-type axis shape-witnessed by test-orthog.cpp; residual = named-entry-point √+SPD-guard test). Surfaced the missing bilinear-form-mutation-rotation L1>L0 theme (NOT on disk) → routed as a fresh abstractor plan candidate. Build-relevant: no (no book rebuild needed for this report)."
---

# CYCLE: L1 observation — matrix-weighted-norm + bilinear-form share a test-coverage gate that the corpus does NOT close

## Summary

Comparing the two L1 matrix-weighted-reduction operators — `matrix-weighted-norm`
(`√(xᴴ B x)`, lowers to `linalg::Norml2(comm, x, B, Bx)`) and `bilinear-form`
(`xᴴ M y`, lowers to `linalg::Dot(comm, x, A, y)`) — surfaces a **shared
variant-axis-coverage gap**: both are held at `rough-in (test-coverage-bounded)`
on the same gating reason (algebraic-law confidence pending dedicated test
coverage of the weighted entry point), and a survey of the full Palace unit-test
corpus (`reference/palace/test/unit/`, 23 `test-*.cpp` files) confirms that
**neither operator's production weighted entry point is exercised by any
dedicated test**. There is no test at the `linalg::` weighted free-function
entry point (no `test-operator*.cpp` / `test-eigen*.cpp` glob match — operator-
*family* tests like `test-boundarymodeoperator.cpp` / `test-domainpostoperator.cpp`
do exist and are engaged below, but none exercises the weighted overload), and the
4-argument weighted overloads `linalg::Norml2(comm,x,B,Bx)` and
`linalg::Dot(comm,x,A,y)` appear **zero times** in the test tree (grep + codemap
`search_text` both confirm). What the corpus DOES have is (a) an indirect
real-energy-norm test (`test-domainpostoperator.cpp:83-93`, hand-computed
`½·Dᴴ E` to 1% rel) and (b) a weighted-orthogonalization test exercising the
*same algebraic shape* over BOTH real and complex vectors including the
real-weight-on-complex-vector lift (`test-orthog.cpp`, the
`OrthogonalizeColumn Weighted - Real`/`- Complex 1` cases) — but the latter
computes the weighted inner product via a **test-local reimplementation**
(`RealWeightedInnerProduct`), not via the named production overloads. The gate
therefore does NOT close cleanly; the recommendation is **STAY rough-in for both,
with sharpened, asymmetric promotion conditions** — and because promotion is an
**ask-class** decision (per the CLAUDE.md `rough-in (test-coverage-bounded)`
qualifier), it is surfaced, not enacted.

## Observation kind

**Variant-axis coverage gap** (shared across two same-layer operators). The two
operators jointly under-cover their element-type and M-symmetry variant axes at
the *named production entry point*; the corpus covers the algebraic shape but not
the entry points, and covers some variant-axis values (real, complex,
real-weight-on-complex) only through indirect / reimplemented paths.

## Specific finding

### Operators compared

- `book/src/L1/matrix-weighted-norm.md` — `matrix_weighted_norm(x, B) = √(xᴴ B x)`,
  status `rough-in (test-coverage-bounded)` (`:108-117`). Entry point at L0:
  `linalg::Norml2(comm, x, B, Bx)` (decl `palace/linalg/operator.hpp:372-374`,
  specs `palace/linalg/operator.cpp:599-619`). Its L1>L0 theme
  `book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md` is **firm** (cycle-026
  stub→firm; cycle-027 `verified_against:` 19-entry audit landed — confirmed on
  disk, theme `## Status` line `:434`).
- `book/src/L1/bilinear-form.md` — `bilinear_form(x, M, y) = xᴴ M y`, status
  `rough-in (lower-layer-shared-vocabulary, cycle-010-wave-1)` (`:321`). Entry
  point at L0: `linalg::Dot(comm, x, A, y)` (decl `palace/linalg/operator.hpp:386-394`,
  defs `palace/linalg/operator.cpp:621-639`). **Its L1>L0 mutation-rotation theme is
  NOT yet authored** — verified on disk: no `book/src/L1-L0/bilinear-form-*.md`
  exists; it is named "forthcoming" as `bilinear-form-mutation-rotation` in
  `book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md:319-326` §Speculative
  L1 operators and in OQ line 769. (Correction to the dispatch framing, which
  stated "bilinear-form's theme status — verify on disk": the theme does **not**
  exist yet; only the matrix-weighted-norm theme is firm.)

These are **distinct operators, not redundant**: `matrix-weighted-norm` is the
diagonal-plus-√-plus-SPD case (`y = x`, outer √, SPD precondition); `bilinear-form`
is the off-diagonal general-`M` case (no SPD requirement, no √, returns possibly-
complex scalar). This is already correctly captured by `bilinear-form` law 8
(`book/src/L1/bilinear-form.md:214-220`: `nrm2_M(x)² = bilinear_form(x, M, x)`)
and `matrix-weighted-norm` §Dependencies (`:92`). No unification is proposed; the
finding is purely about their **shared, still-open, test-coverage gate**.

### (1) Variant-axis-completeness survey

`matrix-weighted-norm` variant axes (`book/src/L1/matrix-weighted-norm.md:94-106`):

| Axis | Value | Source-witnessed | Test-witnessed (entry point) | Test-witnessed (shape only) |
|---|---|---|---|---|
| element-type | `real` (`xᵀ B x`) | YES — real spec `palace/linalg/operator.cpp:599-607` | NO | YES (shape) — `test-orthog.cpp:46-51,313-315` real weighted IP |
| element-type | `complex` (`xᴴ B x`, real-B lane split) | YES — complex spec `palace/linalg/operator.cpp:609-619` | NO | YES (shape) — `test-orthog.cpp:53-68,368-376` real-W-on-complex via `ComplexWrapperOperator` |
| weight-rep of `B` | mass / curl-curl / diag / mg | YES — eigensolver cohort `arpack.cpp:438`, `slepc.cpp:475`, `nleps.cpp:114` | NO | partial — `test-orthog.cpp` dense `W` only |
| output-arg vs return | return-value (L1 picks) | YES — caller-supplied `Bx` reused, `arpack.cpp:470` | n/a (L1-level) | n/a |
| `B = I` degenerate | → `nrm2` | YES — opB-null fallback `arpack.cpp:442` | YES — `test-vector.cpp:209-211` (unweighted `Norml2`) | YES |

`bilinear-form` variant axes (`book/src/L1/bilinear-form.md:257-302`):

| Axis | Value | Source-witnessed | Test-witnessed (entry point) | Test-witnessed (shape only) |
|---|---|---|---|---|
| element-type of `M` | `real` (`Operator` weight) | YES — real overload `palace/linalg/operator.cpp:621-629` | NO | YES (shape) — `test-orthog.cpp:46-51` real-W functor |
| element-type of `M` | `complex` (`ComplexOperator` weight) | YES — complex overload `palace/linalg/operator.cpp:631-639` | NO | NO — no complex-weight-operator test (only real-W-on-complex-vector, a different axis value) |
| M-symmetry | `hermitian` (law 7, law 8) | YES — `Bttr` use site `palace/models/boundarymodeoperator.cpp:85` | NO — `test-boundarymodeoperator.cpp` has no Dot/Poynting/energy assertions | partial — `test-orthog.cpp` `W` is symmetric, exercises law-8-like vanishing |
| M-symmetry | `non-symmetric` (law 7 fails) | YES — `Atn` use site `palace/models/boundarymodeoperator.cpp:90` | NO | NO — no non-symmetric-weight test anywhere |
| precision-mode | `double` / `complex<double>` | YES (single precision surfaced) | NO | YES (shape) |
| output-arg-pattern | `return` (only realised mode) | YES | n/a | n/a |
| real-`x`/real-`M`/real-`y` (`xᵀ M y`) | **NOT surfaced by Palace** | NO (`book/src/L1/bilinear-form.md:85-89`) | NO | partial — `test-orthog.cpp:46-51` real-W IP returns `double` (closest analog) |

**Coverage-gap reading:**
- For `matrix-weighted-norm`, the *real* and *complex* element-type axis values
  AND the real-B-on-complex-x lift are all shape-covered by `test-orthog.cpp`
  (the production complex `Norml2` lane split `B.Mult(x.Real(),..); B.Mult(x.Imag(),..)`
  at `palace/linalg/operator.cpp:613-614` is the *same construction* as the test's
  `RealWeightedInnerProduct` complex `operator()` four-real-dot lift at
  `test-orthog.cpp:59-65`). This materially *narrows* the open question
  `matrix-weighted-norm-mixed-element-type-variant` (the real-`B`-on-complex-`x`
  case is no longer un-witnessed by any test) — but it does NOT verify the laws at
  the named `Norml2(comm,x,B,Bx)` entry point or against the outer √ + SPD guard.
- For `bilinear-form`, the gap is **worse**: the *complex-weight-operator* axis
  value (`ComplexOperator` `A`, `palace/linalg/operator.cpp:631-639`) and the
  *non-symmetric-`M`* axis value (`Atn`, law 7 failure) have **no test coverage at
  all** — not even shape. The two surfaced source use sites (`Bttr` Hermitian,
  `Atn` non-symmetric) are in `boundarymodeoperator.cpp` and `test-boundarymodeoperator.cpp`
  asserts nothing about them (confirmed: grep for `Dot|Poynting|energy|Bttr|Atn`
  in that test → NONE).

### (2) Test-coverage summary (dedicated tests, cited)

Dedicated tests that EXIST (all citecheck `--anchor` verified this invocation):

- `test/unit/test-domainpostoperator.cpp:83-93` — `GetElectricFieldEnergy(*E_field)`
  on a uniform field in a cube, asserted against the closed-form
  `½·ε₀·E₀²·V` to `WithinRel(..., 0.01)`. This is a **real-valued, SPD-mass-weighted
  energy** = `½·bilinear_form(E, M_ε, E)` (the energy-norm-squared, `bilinear-form`
  law 8 / `matrix-weighted-norm` law 8). **Indirect** coverage: it is a coarse
  units/integration check (the test's own TODO at `:31-32` says "can be
  expanded/improved to be a more robust test for the actual function, not just the
  units"), it goes through `DomainPostOperator::GetElectricFieldEnergy` (a
  `BilinearForm`-assembled mass form), NOT through the `linalg::` weighted overload,
  and it is real-only.
- `test/unit/test-orthog.cpp:46-51` (`RealWeightedInnerProduct::operator()` real),
  `:53-68` (complex four-real-dot lift), `:280-318` (`OrthogonalizeColumn Weighted -
  Real`), `:333-381` (`OrthogonalizeColumn Weighted - Complex 1`) — weighted
  orthogonalization over a dense symmetric `W`, real and complex vectors, with the
  real-W-on-complex lift via `ComplexWrapperOperator(&W, nullptr)` (`:368`). Asserts
  the weighted inner products vanish to `WithinAbs(0.0, 1e-12)` (`:317-318`,
  `:378-381`). **Shape-only / reimplemented**: the weight is applied via a
  test-local `RealWeightedInnerProduct` functor (`W.Mult` then unweighted
  `linalg::LocalDot`), NOT via `linalg::Dot(comm,x,A,y)` / `linalg::Norml2(comm,x,B,Bx)`.
- `test/unit/test-vector.cpp:209-211` — `vec1.Norml2()` real, hand-computed
  `√14`. Covers only the **unweighted** member form (= the `B = I` degenerate
  boundary).

Axes with NO test (entry-point granularity):

- `linalg::Norml2(comm, x, B, Bx)` named overload — **0 calls** in `test/unit/`
  (grep `Norml2\(.,.,.,.\)` → NONE; codemap `search_text Norml2` → only unweighted
  forms in tests).
- `linalg::Dot(comm, x, A, y)` named overload — **0 calls** in `test/unit/`
  (grep `linalg::Dot\(.,.,.,.\)` → NONE).
- `GetEigenvectorNorm` (the eigensolver M-orthonormalisation consumer) — **0
  references** in `test/unit/` (decl+def only in `arpack/slepc/nleps`).
- `bilinear-form` complex-weight (`ComplexOperator` `A`) — no test, any granularity.
- `bilinear-form` non-symmetric-`M` (law-7-failure witness) — no test, any granularity.
- `matrix-weighted-norm` outer √ + `MFEM_ASSERT(dot>0)` SPD guard against a known
  hand-computed weighted norm — no direct test.

### (3) Promotion recommendation per operator (ASK-class — surfaced, not enacted)

Both: **STAY `rough-in (test-coverage-bounded)`**, with sharpened conditions. The
shape coverage and the indirect energy test strengthen the entries but do not meet
the entry-point/law-verification bar the qualifier names. Sharpened gates:

- **`matrix-weighted-norm` — STAY rough-in; gate narrowed but not closed.**
  Promotion condition sharpened to a single remaining requirement: a dedicated test
  exercising `linalg::Norml2(comm, x, B, Bx)` (or `GetEigenvectorNorm`) on a known
  SPD `B` with a hand-computed `√(xᴴ B x)` (closing gate (a) of `:113`), since the
  element-type variant axis is now shape-witnessed by `test-orthog.cpp` (real +
  complex + real-B-on-complex lift) — discharging the bulk of gate (c) `:115` and
  materially answering OQ `matrix-weighted-norm-mixed-element-type-variant`
  (the real-`B`-on-complex-`x` plumbing is the SAME four-real-dot construction the
  test exercises). **Drop** the "real-B-on-complex-x is un-witnessed" framing from
  the OQ; the residual gate is purely the missing named-entry-point √+SPD-guard test.
- **`bilinear-form` — STAY rough-in; gate widened, not closed.** Two distinct
  uncovered axis values (complex-weight `ComplexOperator` `A`; non-symmetric-`M`
  law-7-failure) have no test at any granularity. Promotion condition sharpened to:
  (i) author the `bilinear-form-mutation-rotation` L1>L0 theme first (it does not
  exist — a firm lowering is a softer prerequisite than a test and is the
  matrix-weighted-norm precedent), AND (ii) a dedicated test of `linalg::Dot(comm,
  x, A, y)` covering at minimum the Hermitian-`M` (`Bttr`-like) and non-symmetric-`M`
  (`Atn`-like) cases, OR a literature-anchor upgrade raising law-7/law-8 confidence
  (the `ksp_solve`-equivalent escape named in the qualifier). The
  `bilinear-form` entry's own `## Status` `:334-344` repair note already invites the
  integrator to weigh "firm-promotion-eligible"; this finding answers that:
  **not eligible** on test grounds — its coverage is strictly worse than its
  sibling's, which itself stays rough-in.

This is an **ask-class** decision (the CLAUDE.md qualifier ties promotion to test
coverage that is partly out of project write-scope — there is no
`test-operator.cpp`, and adding one is a Palace-source change). The critic should
flag the promotion recommendation; the integrator may record a **deferred-contingent
gate** (the sharpened conditions above) and/or surface the ask to the human. **No
promotion is enacted here.**

## Recommendation

- **Defer promotion (record the sharpened gate).** Both operators STAY rough-in;
  the integrator records the per-operator sharpened promotion conditions above as a
  deferred-contingent gate against the plan item
  `matrix-weighted-norm + bilinear-form firm-promotion` (open-questions.md `:26`).
- **Update OQ `matrix-weighted-norm-mixed-element-type-variant`** (`:769`): the
  real-`B`-on-complex-`x` element-type variant is now shape-witnessed by
  `test-orthog.cpp` (real + complex + `ComplexWrapperOperator` lift); narrow the OQ
  to the residual named-entry-point √+SPD-guard test gap. (Append-only intake note
  — integrator/meta-phase migrates.)
- **Dispatch abstractor on `bilinear-form-mutation-rotation`** (the missing L1>L0
  theme) as the cheapest next step toward `bilinear-form` firmness — it is the
  matrix-weighted-norm precedent (firm theme over a rough-in operator) and is fully
  in write-scope, unlike the test gates. (This is the highest-fan-out follow-up; the
  theme is already named "forthcoming" in the sibling theme `:319-326` and OQ `:769`.)
- **Do NOT** dispatch harvester to unify the two operators — they are genuinely
  distinct (diagonal-√-SPD vs off-diagonal-general-`M`), already cross-referenced via
  law 8; unification would force the SPD/√ machinery onto the general bilinear form.

## Supporting evidence

L1 entries compared:
- `book/src/L1/matrix-weighted-norm.md:94-117` — variant axes + `## Status`
  rough-in gate (a)/(b)/(c).
- `book/src/L1/bilinear-form.md:257-302` (variant axes), `:319-344` (`## Status`
  rough-in + repair note inviting firm-eligibility judgment), `:85-89` (real-`M`
  case not surfaced), `:205-220` (laws 7, 8 conditional on M-symmetry).
- `book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md:319-326` — names
  `bilinear-form-mutation-rotation` as forthcoming + confirms internal-`Ax`-alloc
  vs caller-`Bx` distinction; `:434` firm `## Status`.
- (verified absent) no `book/src/L1-L0/bilinear-form-*.md` on disk.

Source entry points + use sites (citecheck `--anchor` verified this invocation):
- `palace/linalg/operator.cpp:599-607` real `Norml2` spec; `:609-619` complex spec
  (lane split `B.Mult(x.Imag(),Bx.Imag())` confirmed at `:614`).
- `palace/linalg/operator.cpp:621-639` `Dot(comm,x,A,y)` real `:621-629` /
  complex `:631-639` overloads; `palace/linalg/operator.hpp:386-394` decls.
- `palace/models/boundarymodeoperator.cpp:85` (`Bttr` Hermitian use site),
  `:90` (`Atn` non-symmetric use site).

Test corpus (citecheck `--anchor` verified this invocation):
- `test/unit/test-domainpostoperator.cpp:83-93` — `GetElectricFieldEnergy`
  hand-computed energy (indirect, real-only).
- `test/unit/test-orthog.cpp:46-51` (real weighted IP functor), `:53-68` (complex
  four-real-dot lift), `:368-376` (`ComplexWrapperOperator` lift) — shape-only,
  reimplemented weight.
- `test/unit/test-vector.cpp:209-211` — unweighted `Norml2()` (`B = I` boundary).
- Negative confirmations (grep over `reference/palace/test/unit/`): `Norml2(.,.,.,.)`
  → NONE; `linalg::Dot(.,.,.,.)` → NONE; `GetEigenvectorNorm` → NONE;
  `GetElectricFieldEnergy` → only `test-domainpostoperator.cpp:83`;
  `test-boundarymodeoperator.cpp` Dot/Poynting/energy → NONE.

OQ ledger:
- `scaffolding/open-questions.md:26` (migrated plan item
  `matrix-weighted-norm + bilinear-form firm-promotion`; the dispatch-named OQs
  `bilinear-form-variant-axis-test-coverage` and `bilinear-form-real-vector-coverage-gap`
  exist ONLY as constituent references here, not as standalone slugged entries),
  `:769` (active OQ `matrix-weighted-norm-mixed-element-type-variant`, plan c028 #4),
  `:201` (`matrix-weighted-norm-and-bilinear-form-l1-rough-ins`, partially answered),
  `:361` (mutation-rotation theme resolved c026), `:362` (verified_against follow-up
  resolved c027).

## Open questions / caveats

- **Dispatch-framing correction (verify-before-acting):** the task stated
  "bilinear-form's theme status — verify on disk (matrix-weighted-norm c026 +
  audited c027; bilinear-form's theme status)". On disk, **the bilinear-form L1>L0
  theme does not exist** — only `matrix-weighted-norm-mutation-rotation.md` is firm.
  The `bilinear-form-mutation-rotation` theme is "forthcoming." Any downstream action
  must not assume a firm bilinear-form lowering exists.
- **Is `test-orthog.cpp` shape coverage admissible as law-confidence evidence?**
  It exercises the *exact construction* of the production complex `Norml2` lane
  split (four real dots), real and complex, over a symmetric weight — strong
  evidence the element-type-variant collapse is faithful. But it is a test-local
  reimplementation, not a call into `linalg::Norml2`/`linalg::Dot`. Under the strict
  reading of the qualifier (test "at the exact entry point") it is shape-only; under
  a relaxed reading it could justify dropping the element-type half of the gate. This
  is the crux the human/critic should rule on. I have recommended the strict reading
  (STAY rough-in) but flagged the relaxed reading as the narrowing that materially
  answers the mixed-element-type OQ.
- **The two named OQs in the dispatch** (`bilinear-form-variant-axis-test-coverage`,
  `bilinear-form-real-vector-coverage-gap`) are NOT standalone ledger slugs — they
  live only as constituent references in the migrated plan item `:26`. If the
  meta-phase wants per-axis tracking, they may need re-slugging; flagged for the
  integrator/meta-phase, not resolved here.
- I did NOT write to `book/`. Per the dispatch-phase write-guard, the OQ updates and
  any entry edits implied above are emitted as recommendations for
  `integrator-per-report`, not applied. No proposed-changes block is included because
  this report surfaces an observation + ask, not a mechanical edit (the sharpened-gate
  text and OQ narrowing are integrator/meta-phase intake migrations, and the
  bilinear-form-mutation-rotation theme is a follow-up dispatch, not an edit to apply).
