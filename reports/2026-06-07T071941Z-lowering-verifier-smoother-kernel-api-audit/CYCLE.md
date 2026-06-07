---
agent: lowering-verifier
invoked_at: 2026-06-07T072951Z
scope: DIRECTIVE-3 kernel-API/impl correspondence audit — multigrid-relaxation-smoother ↔ triangular-solve-obstruction
status: pending
inputs:
  - book/src/L1/multigrid-relaxation-smoother.md  (kernel-impl, firm)
  - book/src/L1-L0/triangular-solve-obstruction.md  (kernel-api, obstruction (opaque-library-ownership))
  - reference/palace/palace/linalg/distrelaxation.cpp:1-156
  - reference/palace/palace/linalg/distrelaxation.hpp:1-92
  - reference/palace/palace/linalg/chebyshev.hpp:82
  - reference/palace/palace/linalg/amg.cpp:19,24
  - reference/palace/palace/linalg/ams.cpp:162
integrated_at: 2026-06-07T071941Z
integration_commit: 17cdafe9d9515c72045691b07420fbdfa25af81a
integration_notes: "cycle-122 D5. Applied clean. 8-entry verified_against: block appended to multigrid-relaxation-smoother + 2 off-by-one citation corrections (distrelaxation.cpp :103→:102, :121-152→:121-151). realizes-kernel-api edge reference-class + kernel-api status confirmed unchanged. 0 gate hits. See reports/cycle-122-integrator-staging/STAGING.md."
---

# CYCLE: Audit multigrid-relaxation-smoother realizes-kernel-api triangular-solve-obstruction

## Summary

This is the DIRECTIVE-3 (2026-06-07) kernel-API/impl correspondence audit for the
firm c121 **kernel-implementation** `book/src/L1/multigrid-relaxation-smoother.md`
(the Hiptmair distributive relaxation smoother) against its **kernel-api** surface
`book/src/L1-L0/triangular-solve-obstruction.md` (the kept
`obstruction (opaque-library-ownership)` theme, role-labelled `kernel-api`). The
five audit questions the dispatch poses all resolve favourably:
**(1) the impl genuinely REALIZES the relaxation-slot contract** the API documents
— at the correct granularity (same relaxation-step semantics, GS-free route),
honestly framed and with a correctly-disclosed scoped coverage (the impl is the
Hiptmair *distributive* realization, one of the relaxation-slot's realizations,
not a realization of every case the general `trsv` API names);
**(2) the `realizes-kernel-api` edge is `reference`-class** (under `reference:`, NOT
`depends-on`) — the integrity gate passes;
**(3) the API surface stays `obstruction (opaque-library-ownership)`** (NOT
downgraded; the `kernel-api` role-label was correctly added without a status
promotion);
**(4) the impl's L0 citations are faithful** to `reference/palace` — every per-leg
anchor citecheck-zero-drifts, with **two minor off-by-one carry-forward citation
corrections** found (the `for`-loop header line and the `MultTranspose2` range END);
**(5) the `pc_it` sweep sequential-obstruction (NL1) is faithfully documented**.

**Top-level verdict: FAITHFUL (correspondence holds).** The audit unblocks no
status flip (the impl is already firm; the API stays obstruction). The only
proposed changes are: append a `verified_against:` impl-realizes-API block to the
impl chapter, and the two off-by-one citation carry-forward corrections.

## Per-citation audit

### Impl L0 anchors (`distrelaxation.{cpp,hpp}`)

- **Citation**: `reference/palace/palace/linalg/distrelaxation.hpp:23-30`
  - **Theme claim**: header class declaration with the Hiptmair-distributive-relaxation
    comment (`:23-28`) + `class DistRelaxationSmoother : public Solver<OperType>` (`:30`).
  - **Found**: on disk lines 23-28 are exactly the comment "Hiptmair distributive
    relaxation smoother applying smoothers to both the operator in the primary space
    as well as its projection into an auxiliary space. Reference: Hiptmair … SIAM J.
    Numer. Anal. (1998)."; line 30 is `class DistRelaxationSmoother : public Solver<OperType>`.
    `citecheck --anchor 'class DistRelaxationSmoother'` ⇒ ok at :30.
  - **Verdict**: supports.
  - **Notes**: confirms the impl IS the Hiptmair distributive smoother — the positive
    Palace realization of the H(curl) relaxation slot.

- **Citation**: `reference/palace/palace/linalg/distrelaxation.cpp:13-36`
  - **Theme claim**: the ctor; the 4th-kind/1st-kind ChebyshevSmoother fold for `B`, `B_G`
    (`:21-34`), `B_G->SetInitialGuess(false)` (`:35`).
  - **Found**: template head :13, signature :14-18, `if (cheby_4th_kind)` fold building
    `ChebyshevSmoother` / `ChebyshevSmoother1stKind` for both `B` and `B_G` :21-34,
    `B_G->SetInitialGuess(false)` :35, closing brace :36 (read on disk).
    `citecheck --anchor 'SetInitialGuess(false)'` ⇒ ok at :35.
  - **Verdict**: supports.
  - **Notes**: the two point-smoothers are Chebyshev — **GS-free by construction**, the
    crux of the kernel-api correspondence. (The `:13` citecheck `[DRIFT]` is a benign
    range-START artifact: the `DistRelaxationSmoother` token is on :14, the template head
    on :13; the range `:13-36` is correct.)

- **Citation**: `reference/palace/palace/linalg/distrelaxation.cpp:38-69`
  - **Theme claim**: `SetOperators` — `A=&op`/`A_G=&op_G` capture (`:49-50`), auxiliary
    essential-dof set `dbc_tdof_list_G = PtAP_G->GetEssentialTrueDofs()` (`:61`),
    `B->SetOperator(op)`/`B_G->SetOperator(op_G)` (`:64-65`).
  - **Found**: `A = &op;` :49, `A_G = &op_G;` :50, `dbc_tdof_list_G = PtAP_G->GetEssentialTrueDofs();`
    :61, `B->SetOperator(op);` :64 / `B_G->SetOperator(op_G);` :65, closing brace :69.
    All four anchors citecheck ⇒ ok.
  - **Verdict**: supports.

- **Citation**: `reference/palace/palace/linalg/distrelaxation.cpp:101-119` (`Mult2`, the relaxation action)
  - **Theme claim**: primary leg `y = y + B(x − A·y)` (`:104-106`, `SetInitialGuess(initial_guess||it>0)` :105);
    auxiliary leg `y = y + G B_G Gᵀ(x − A·y)` (`A->Mult(y,r)` :109, `linalg::AXPBY(1.0,x,-1.0,r)` :110,
    `Gᵀ` :111, ess-pin :112-115, `B_G` :116, `G` prolong-add :117).
  - **Found**: every per-leg anchor verified on disk and via `citecheck --anchor`:
    `B->Mult2(x, y, r)` :106 ok; `SetInitialGuess(this->initial_guess` :105 ok;
    `A->Mult(y, r)` :109 ok; `AXPBY(1.0, x, -1.0, r)` :110 ok;
    `RealMultTranspose(*G, r, x_G)` :111 ok; `if (dbc_tdof_list_G)` :112 ok;
    `SetSubVector(x_G` :114 ok; `B_G->Mult2(x_G, y_G, r_G)` :116 ok;
    `RealAddMult(*G, y_G, y)` :117 ok; closing brace :119 (read on disk).
  - **Verdict**: supports.
  - **Notes**: **one off-by-one drift inside this region** — the chapter cites the sweep
    loop header `for (int it = 0; it < pc_it; it++)` at `:103`, but on disk the `for`
    statement is at **line 102** (line 103 is the opening `{`). The body anchors derived
    from it (:104-106, :108-117) are all correct; only the loop-header line number is +1.
    Two occurrences in the chapter (see §Per-citation drift findings). The body range
    `:101-119` itself is a defensible "relaxation action" range (signature at :99, `{` at
    :100, body+close-brace 101-119).

- **Citation**: `reference/palace/palace/linalg/distrelaxation.cpp:121-152` (`MultTranspose2`)
  - **Theme claim**: the reversed-order transpose action (basis for the "not symmetric in
    general" non-law and the SSOR forward+transpose-pair idiom).
  - **Found**: `MultTranspose2` body on disk spans line 121 (template head) → line 151
    (closing brace `}`); **line 152 is blank**. The reversed-order legs (auxiliary first
    :129-146, then primary `B->MultTranspose2` :149) are present and match the non-law claim.
  - **Verdict**: partially-supports (content correct; range END off-by-one).
  - **Notes**: **range-END +1 drift** — the chapter cites `:121-152`; the function's
    closing brace is at **line 151**. Correct range is `:121-151`. Two occurrences in the
    chapter (lines 223, 316). Carry-forward fix.

### Impl record-definition anchors (`distrelaxation.hpp:34-51`)

- **Citation**: `reference/palace/palace/linalg/distrelaxation.hpp:34-51` (the `DistRelaxSmoother[N,M]` record backing)
  - **Theme claim**: `pc_it` (`:36`), `G` (`:39`), `A`/`A_G` (`:42`), `dbc_tdof_list_G` (`:43`),
    `B`/`B_G` (`:46`/`:47`), scratch vectors `x_G,y_G,r_G,r` (`:50`).
  - **Found**: `const int pc_it;` :36; `const Operator *G;` :39 (comment "// Discrete gradient
    matrix (not owned)." at :38); `const OperType *A, *A_G;` :42; `const mfem::Array<int>
    *dbc_tdof_list_G;` :43; `mutable std::unique_ptr<Solver<OperType>> B;` :46; `… B_G;` :47;
    `mutable VecType x_G, y_G, r_G, r;` :50. All field-decl anchors citecheck ⇒ ok.
  - **Verdict**: supports.
  - **Notes**: every record field maps to a real backing member. Strata claims correct
    (`x_G/y_G/r_G/r` are per-call scratch, not L1 record fields — confirmed by the
    `mutable VecType` declaration at :50 + the comment "Temporary vectors for smoother
    application." at :49).

### Kernel-api correspondence anchors

- **Citation**: `reference/palace/palace/linalg/chebyshev.hpp:82`
  - **Theme claim**: Adams et al. 2003 polynomial-over-Gauss-Seidel citation — the realized
    relaxation is GS-free by design (avoids the triangular sweep the kernel-api names).
  - **Found**: `citecheck --anchor 'polynomial versus Gauss'` ⇒ ok at :82.
  - **Verdict**: supports. (Same anchor the kernel-api theme's own `verified_against` block
    carries at :490-493 — cross-consistent.)

- **Citation**: `reference/palace/palace/linalg/amg.cpp:24`
  - **Theme claim**: the GPU GS→l1-Jacobi flip; corroborates that the GS triangular sweep is
    the non-removable kernel engineered around.
  - **Found**: `citecheck --anchor 'relax_type = 18'` ⇒ ok at :24. (And :19 `l1-symm. GS`
    enum comment ⇒ ok; the kernel-api theme's own anchors :19/:24/:29 are cross-consistent.)
  - **Verdict**: supports.

### Kernel-api surface (the API contract being realized)

- **Citation**: `book/src/L1-L0/triangular-solve-obstruction.md` (whole theme)
  - **Theme claim** (impl side): "what the opaque GS-SSOR contract computes, this
    from-our-primitives composition computes by a GS-free route" (NL2 + Context).
  - **Found**: the API theme documents a general sparse-triangular relaxation sweep
    (`trsv`/`SpTrSV`/GS/SOR/SSOR) over the length-`N` field as the relaxation kernel the
    multigrid smoother slot calls, with NO positive Palace site (GS/SSOR sweeps live only
    inside HYPRE, `amg.cpp:19`/`ams.cpp:162`), and explicitly records that Palace fills the
    slot GS-free (Jacobi+Chebyshev, Adams-2003). The Status line (:545) is
    `obstruction (opaque-library-ownership)` — **kernel-api** (role-label added, status
    NOT downgraded). The Context+Status of BOTH chapters cross-reference each other
    consistently.
  - **Verdict**: supports (the correspondence is well-posed and the two surfaces are
    mutually consistent).
  - **Notes**: see §Correspondence assessment for the granularity + scoped-coverage analysis.

## Correspondence assessment (the DIRECTIVE-3 core question)

**Does the constructive impl genuinely realize the kernel-API contract?** YES, at the
correct granularity, with a correctly-disclosed scoped coverage.

1. **Granularity match — the API contract is the relaxation SLOT, not a byte-identical
   triangular substitution.** The kernel-api theme is explicit that Palace authors no
   triangular sweep and *deliberately* fills the multigrid relaxation slot with GS-free
   smoothers. So the contract the impl must realize is "a relaxation step that smooths
   high-frequency error in the multigrid smoother slot" — the *semantics* of the slot,
   not a literal `trsv`. The impl realizes exactly that, via the Hiptmair distributive
   composition (primary Chebyshev point-smoother `B` + auxiliary gradient-space Chebyshev
   correction `B_G`). The chapter frames this honestly (NL2: "what the opaque GS-SSOR
   contract computes, this from-our-primitives composition computes by a GS-free route")
   — it does NOT make the false claim of a byte-identical substitution. This is precisely
   the DIRECTIVE-3 intent: a reviewer reads BOTH the opaque contract (a) and the
   from-our-primitives version (b) and confirms they fill the same slot.

2. **Scoped coverage — correctly disclosed, NOT a hidden gap.** The general API names
   any sparse-triangular relaxation over the length-`N` field; the impl realizes the
   *Hiptmair distributive* case (H(curl)/auxiliary-space). It is therefore ONE realization
   of the relaxation slot, not a realization of every case the general `trsv` API could
   stand in for. This is the role-spec's "an impl that covers only part of the API's stated
   cases" situation — but it is **correctly disclosed**: the impl presents itself as the
   distributive smoother throughout, and references `chebyshev-smoother` / `jacobi-smoother`
   as the sibling point-smoother realizations of the same slot (the plain
   primary-space-only relaxation cases). The kernel-api theme itself enumerates these
   GS-free realizations (Jacobi, Chebyshev) in §(b2). So the impl+siblings cohort jointly
   realizes the relaxation-slot contract; this single impl node faithfully realizes its
   declared sub-case. **Not a finding** — recorded as a scoped-coverage note in the
   proposed `verified_against` block.

3. **Algebraic faithfulness of the realization.** All five algebraic laws (single-sweep
   decomposition, sweep iteration, zero-residual fixed point, auxiliary-leg linearity,
   initial-guess fast path) are syntactic identities read directly off the ordered `Mult2`
   body (verified at :101-119). The two stated non-laws (NOT additive between spaces; NOT
   symmetric in general) are correct: the auxiliary leg's residual is formed AFTER the
   primary update (`A->Mult(y, r)` at :109 reads the just-updated `y`), so the composition
   is multiplicative not additive Schwarz; and `MultTranspose2` (:121-151) applies the legs
   in reversed order with transposed point smoothers, so the single `Mult2` action is
   non-symmetric. Both verified on disk.

## Integrity gate (edge typing + API status)

- **`realizes-kernel-api` edge is `reference`-class.** Confirmed: in the impl frontmatter
  the edge `target: L1-L0/triangular-solve-obstruction, kind: realizes-kernel-api` is under
  the `reference:` key (lines 24-26), NOT under `depends-on:` (lines 15-23). The impl does
  NOT `depends-on` the opaque API. ✓ Integrity gate PASSES.
- **The four `depends-on` edges are to firm L1 primitives** (`chebyshev-smoother` firm,
  `apply_linop` firm, `axpby` firm, `interpolator` firm — all confirmed on disk). The opaque
  API is NOT among the blocking deps. Well-foundedness `rank(firm-impl) ≤ min(rank(firm
  deps))` holds (firm ≤ firm). ✓
- **The API surface stays `obstruction (opaque-library-ownership)`.** Confirmed: Status line
  :545 is `obstruction (opaque-library-ownership)` — kernel-api; the role-label was added
  WITHOUT a status promotion/downgrade (the chapter explicitly states "it stays
  obstruction-*kind* (NOT downgraded, NOT promoted to a constructive status)"). ✓
- **Graded-stack lint:** `python3 tools/graded-stack-lint/graded_stack_lint.py` ⇒ EXIT 0,
  **0 rank violations**. The kernel-api node `L1-L0/triangular-solve-obstruction` reports
  `[garbage?]` — this is the **by-design** DIRECTIVE-3 grounded-future disposition: a
  kernel-api node's only inbound edge is the free `realizes-kernel-api` reference (not a
  blocking `depends-on`), so it is unreachable over blocking edges. NOT a defect (matches
  the cycle-122 planner's grounded-future-node note). ✓

## Applicability conditions

The kernel-api theme is an obstruction theme; its applicability conditions (4 boundary
clauses + the load-bearing-obstruction note, §Applicability conditions :263-300) bound WHEN
the negative finding applies. The impl's realization sits exactly inside boundary clause 1
(the general sparse triangular-solve over the length-`N` field has no positive Palace site →
Palace fills the slot GS-free) — the impl IS the GS-free fill for the H(curl) case. No
counter-example: the impl does not author a triangular sweep (verified — the `Mult2` body
:101-119 contains only `B`/`B_G` Chebyshev applies, matvecs, AXPBY, transfer, and an
essential-dof pin; no forward/back substitution), so it does not contradict the obstruction.

| Condition (API boundary clause) | Verifiable? | Counter-example? |
|---|---|---|
| 1. General `trsv`/GS/SOR/ILU over length-`N` field has no positive site → fill GS-free | Yes — `Mult2` body :101-119 is GS-free (Chebyshev legs only) | No |
| 2. Small-dense GMRES back-substitution (`back_solve`) is firm, obstruction N/A | Yes — `back_solve.md` firm, distinct slug | No (out of impl scope) |
| 3. 2×2 block forward solve (`blockprecond.hpp:16-29`) is a red herring, not `trsv` | Yes — not touched by the impl | No |
| 4. HYPRE/STRUMPACK/SuperLU/MUMPS internal sweeps are opaque-library-owned | Yes — impl uses none of these | No |

## Algebraic laws (correspondence-relevant)

| Law / claim | Holds on the realization? |
|---|---|
| Impl realizes the relaxation-slot semantics the API names (GS-free route) | YES — `Mult2` body smooths via Chebyshev legs; same slot, no triangular sweep (NL2 framing correct) |
| GS-free by construction (the engineered-around choice the API documents) | YES — `B`,`B_G` are `ChebyshevSmoother`/`ChebyshevSmoother1stKind` (ctor :21-34); Adams-2003 anchor :82 |
| Multiplicative (not additive Schwarz) between primary/auxiliary spaces | YES — aux residual formed after primary update (`A->Mult(y,r)` :109) |
| Non-symmetric single action (SSOR-symmetric only as fwd+transpose pair) | YES — `MultTranspose2` :121-151 reverses leg order with transposed smoothers |

## Sequential-obstruction (NL1) faithfulness

The dispatch asks to confirm the `pc_it`-sweep sequential-obstruction note is faithfully
documented. **Confirmed.** NL1 (chapter lines 230-240) states the outer
`for (int it = 0; it < pc_it; it++)` loop threads `y` across sweeps (each sweep reads the
previous sweep's residual `x − A·y` at :106/:109) — a genuine sequential recurrence that
does NOT lift to a single global tensor-field expression, to be recorded as the L3-lift
`partial-obstruction` (the BODY lifts; the SWEEP loop does not), paralleling
`L3/chebyshev`. This matches the on-disk loop structure (`Mult2` :102-118: the loop body
mutates `y` in place across `it`). The note correctly scopes the obstruction to the loop,
NOT the body, and correctly states it does NOT gate the L1 firm status (at L1 the sweep is a
pure `pc_it`-fold parameter, law 2). The `reference:`-class edge to
`concepts/sequential-obstruction` is present in the frontmatter (line 28). ✓

NL3 (multigrid-integration test coverage only; firm via the firm-on-positive-structure
escape) is also faithful — there is no `test-distrelaxation.cpp` in the tree, and every law
is a syntactic identity on the fully-read positive `Mult2` body, so the missing dedicated
test does not gate firm (the `chebyshev-smoother`/`jacobi-smoother` no-dedicated-test
precedent). Not re-litigated here (the c121 firm promotion already invoked this escape; this
audit confirms the laws ARE syntactic identities on the read body).

## Per-citation drift findings (carry-forward citation corrections)

Two minor off-by-one citation drifts in the impl chapter (bounded, evidenced citation
corrections — in-scope per `lifter-scope-content-correction-boundary`). Both anchor tokens
remain in-range and the meaning-reads are correct, so neither weakens the audit; they are
flagged for the integrator carry-forward + included in the proposed changes.

- **DRIFT-1 (loop-header line +1).** The sweep loop `for (int it = 0; it < pc_it; it++)` is
  cited at `distrelaxation.cpp:103` at chapter lines **231** (NL1) and **310** (Evidence).
  On disk the `for` statement is at **line 102** (line 103 is the opening `{`).
  `citecheck --anchor 'for (int it'` ⇒ `[DRIFT] anchor at line 102 … suggested :102`.
  Fix: `:103` → `:102` in both occurrences.
- **DRIFT-2 (range-END +1).** `MultTranspose2` is cited as `:121-152` at chapter lines
  **223** (non-law) and **316** (Evidence). On disk the function's closing brace is at
  **line 151** (line 152 is blank). Fix: `:121-152` → `:121-151` in both occurrences.

## Proposed changes

### Change 1 — append the impl-realizes-API `verified_against:` block to the impl chapter

```edit:book/src/L1/multigrid-relaxation-smoother.md
[append at end of file]
```yaml
verified_against:
  - citation: reference/palace/palace/linalg/distrelaxation.hpp:23-30
    verdict: supports
    audited_at: 2026-06-07T072951Z
    note: Hiptmair-distributive-relaxation header comment + class decl; the kernel-impl IS the Hiptmair distributive smoother realizing the relaxation slot; citecheck --anchor zero-drift (comment :24, class :30).
  - citation: reference/palace/palace/linalg/distrelaxation.cpp:13-36
    verdict: supports
    audited_at: 2026-06-07T072951Z
    note: ctor — the two ChebyshevSmoother / ChebyshevSmoother1stKind point-smoothers B, B_G (GS-free by construction, realizing the kernel-api GS-free route); B_G->SetInitialGuess(false) :35; close brace :36; citecheck zero-drift.
  - citation: reference/palace/palace/linalg/distrelaxation.cpp:38-69
    verdict: supports
    audited_at: 2026-06-07T072951Z
    note: SetOperators — A/A_G capture (:49-50), auxiliary essential-dof set dbc_tdof_list_G (:61), B/B_G SetOperator (:64-65); close brace :69; citecheck zero-drift.
  - citation: reference/palace/palace/linalg/distrelaxation.cpp:101-119
    verdict: supports
    audited_at: 2026-06-07T072951Z
    note: Mult2 relaxation action body — primary leg y=y+B(x-Ay) (:104-106), auxiliary leg y=y+G B_G Gt(x-Ay) (A->Mult :109, AXPBY :110, Gt :111, ess-pin :112-115, B_G :116, G prolong-add :117); close brace :119; per-leg anchors all citecheck zero-drift.
  - citation: reference/palace/palace/linalg/distrelaxation.cpp:121-151
    verdict: supports
    audited_at: 2026-06-07T072951Z
    note: MultTranspose2 reversed-order transpose action (basis for the not-symmetric-in-general non-law + SSOR forward+transpose-pair idiom); function close brace at :151 on disk (chapter prose cites :152 — END +1 drift, see Change 2).
  - citation: reference/palace/palace/linalg/chebyshev.hpp:82
    verdict: supports
    audited_at: 2026-06-07T072951Z
    note: Adams et al. 2003 polynomial-versus-Gauss-Seidel citation — the kernel-api correspondence anchor that the realized relaxation is GS-free by design; citecheck --anchor zero-drift.
  - citation: reference/palace/palace/linalg/amg.cpp:24
    verdict: supports
    audited_at: 2026-06-07T072951Z
    note: GPU GS->l1-Jacobi flip (relax_type = 18) corroborating the GS triangular sweep is the non-removable kernel engineered around; citecheck --anchor zero-drift.
  - citation: book/src/L1-L0/triangular-solve-obstruction.md
    verdict: supports
    audited_at: 2026-06-07T072951Z
    note: kernel-api correspondence FAITHFUL — the impl realizes the relaxation-slot semantics the opaque GS-SSOR/sparse-triangular contract names, via a GS-free route; realizes-kernel-api edge is reference-class (NOT depends-on); the api theme stays obstruction (opaque-library-ownership). Scoped-coverage faithful (impl covers the Hiptmair distributive case; chebyshev/jacobi siblings realize the point-smoother cases of the same slot).
```
```

(Self-check: the YAML block above was extracted and parsed clean by
`python3 -c "import yaml; yaml.safe_load(...)"` ⇒ `YAML OK`. No `note:` value begins
with a quote character of either kind.)

### Change 2 — DRIFT-1 carry-forward citation correction (`:103` → `:102`, two sites)

```edit:book/src/L1/multigrid-relaxation-smoother.md
[line 231 — in non-law NL1]
  The `for (int it = 0; it < pc_it; it++)` loop (`distrelaxation.cpp:102`)
[line 310 — in §Evidence, Mult2 bullet]
  sweep loop (`:102`), primary leg `y = y + B(x − A·y)` (`:104-106`,
```

(On disk the `for (int it = 0; it < pc_it; it++)` statement is at line 102; line 103 is the
opening `{`. `citecheck --anchor 'for (int it'` ⇒ suggested `:102`.)

### Change 3 — DRIFT-2 carry-forward citation correction (`:121-152` → `:121-151`, two sites)

```edit:book/src/L1/multigrid-relaxation-smoother.md
[line 223 — in non-law "NOT symmetric in general"]
  (auxiliary→primary→primary-transpose, `:121-151`) apply the legs in the
[line 316 — in §Evidence]
- `palace/linalg/distrelaxation.cpp:121-151` — `MultTranspose2`, the reversed-order
```

(On disk `MultTranspose2`'s closing brace is at line 151; line 152 is blank.)

**No status flip is proposed.** The impl is already firm (c121); the kernel-api surface
stays `obstruction (opaque-library-ownership)`. The audit CONFIRMS the existing statuses —
it does not unblock a promotion. (No whole-book maturity-token re-anchor grep is required:
this audit promotes nothing.)

## Supporting evidence

Source / tool files consulted:

- `reference/palace/palace/linalg/distrelaxation.cpp:1-156` — full file read on disk (ctor
  :13-36, `SetOperators` :38-69, `Mult2` :98-119, `MultTranspose2` :121-151, explicit
  template instantiations :153-154).
- `reference/palace/palace/linalg/distrelaxation.hpp:1-92` — full file read on disk
  (Hiptmair comment :23-28, class decl :29-88, private member set :34-51).
- `reference/palace/palace/linalg/chebyshev.hpp:82`, `amg.cpp:19,24`, `ams.cpp:162` — the
  kernel-api correspondence + cross-consistency anchors (citecheck-verified).
- `book/src/L1/{chebyshev-smoother,apply_linop,axpby,interpolator,set_subvector_zero}.md` —
  the four firm `depends-on` constituents + the referenced essential-dof-pin atom
  (firmness/rank confirmed firm on disk).
- `book/src/concepts/sequential-obstruction.md`, `book/src/L4/preconditioning-framework.md`
  — the two `reference:`-class targets in the impl frontmatter (existence confirmed).
- `tools/citecheck/citecheck.py` (the shared authoritative line-map; every asserted anchor
  run through `--anchor`) + `tools/graded-stack-lint/graded_stack_lint.py` (EXIT 0,
  0 rank violations).

## Open questions / caveats

- **Scoped coverage is the only "partial" in the correspondence, and it is correctly
  disclosed — flagged for the standing DIRECTIVE-3 integrity tracking, not as a defect.**
  This single kernel-impl node realizes the *Hiptmair distributive* sub-case of the
  general relaxation-slot the kernel-api names. The point-smoother sub-cases (plain
  primary-space relaxation) are realized by the sibling firm `chebyshev-smoother` /
  `jacobi-smoother` chapters, which the kernel-api theme §(b2) already enumerates. There is
  currently **no `realizes-kernel-api` edge from `chebyshev-smoother` / `jacobi-smoother`
  to `triangular-solve-obstruction`** — only from `multigrid-relaxation-smoother`. If the
  meta-phase wants the relaxation-slot's GS-free realization cohort to be *jointly*
  navigable from the kernel-api surface, a follow-up could add free `realizes-kernel-api`
  `reference` edges from those two siblings as well (combinator-miner / abstractor scope).
  Optional — not blocking; the current single-impl edge is faithful and the siblings are
  reachable via the impl's own dependency edges. (Candidate for the batch-39 meta
  standing-duty review of the 3 DIRECTIVE-3 pairs.)

- **The kernel-api node's `[garbage?]` lint flag is by-design and tracked elsewhere.** As a
  DIRECTIVE-3 kernel-api node its only inbound is the free `realizes-kernel-api` reference;
  it is intentionally unreachable over blocking `depends-on` edges. The cycle-122 planner
  already accounts for this disposition (grounded-future / `[GARBAGE*]`-by-design). No
  action needed from this audit; noted so the integrator does not treat the flag as a
  regression.

- **The two off-by-one drifts (Change 2 / Change 3) are bounded carry-forward citation
  corrections.** They do not affect the audit verdict (anchor tokens in-range, meaning-reads
  correct). If the integrator prefers to route citation-only corrections through a `lifter`
  rather than apply them inline, the exact `file:line` residue set is enumerated in
  §Per-citation drift findings (chapter lines 231, 310 for DRIFT-1; lines 223, 316 for
  DRIFT-2).

- **No directionality / rank-invariant violation found.** The impl is an L1 entry (not a
  lowering theme), so the high→low theme-directionality check is N/A; the rank-invariant
  `rank(impl) ≤ min(rank(deps))` holds (firm ≤ firm, all four deps firm). The
  `realizes-kernel-api` edge correctly does NOT enter the rank computation (reference-class).
