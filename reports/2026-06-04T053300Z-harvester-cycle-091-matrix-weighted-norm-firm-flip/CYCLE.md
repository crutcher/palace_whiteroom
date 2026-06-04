---
agent: harvester
invoked_at: 2026-06-04T053300Z
scope: L1 operator: matrix-weighted-norm (firm-flip + L1/index + L4/index count-owner) — cycle-091 D1 (batch-29 LEAD wave-1)
status: pending
integrated_at: 2026-06-04T080000Z
integration_commit: 948247a
integration_notes: "cycle-091 D1 (batch-29 LEAD). matrix-weighted-norm §Status rough-in (test-coverage-bounded) → firm; L1/index counts 30→31 main / 37→38 grand (c080 reconciliation note discharged); L4/index :98 Folds-cell mwn label → firm c091. Applied clean by integrator-per-report; build clean (cargo make book exit 0, finalize applied one symmetric stale-label repair on magnetostatic.L4:41 — a D4 coverage gap, not on D1's files)."
inputs:
  - reports/2026-06-04T053300Z-cycle-planner-cycle-091/CYCLE.md (the cycle-091 plan; D1 scope)
  - reports/2026-06-04T032609Z-meta-phase-cycle-090/CYCLE.md (the batch-28 meta-phase GO; the firm-flip license)
  - book/src/L1/matrix-weighted-norm.md (the verb being flipped; §Status :110 + the two verified_against blocks)
  - book/src/L1/index.md (D1 SOLE owner — count header :31 / bullet :66 / dep-map :117 / OQ-partial :101 / normalize-bullet :40 stale-ref)
  - book/src/L4/index.md (D1 SOLE owner of matrix-weighted-norm-specific labels; reduce-verb-status lines deferred to D3)
---

# CYCLE: Flip matrix-weighted-norm rough-in→firm + own the L1/L4 index updates (cycle-091 D1)

## Summary

`matrix-weighted-norm` (`α = ‖x‖_B = √(xᴴ B x)` for SPD `B`; the L1 energy-norm primitive, the M-orthonormalisation norm in the generalised eigenvalue problem) has carried `rough-in (test-coverage-bounded)` since cycle-010. The batch-28 meta-phase (`reports/2026-06-04T032609Z-meta-phase-cycle-090/CYCLE.md`) GO'd promoting it to `firm`: both norm-axiom law-sides are discharged — the **structure-side** (laws 4 triangle / 6 Cauchy–Schwarz / 7 parallelogram) at cycle-088 as inner-product-space theorems over the **provably-SPD** `B = KM = GetInnerProductMatrix(0.0, 1.0, nullptr, M.get())` (the real SPD part of the FE mass matrix), and the **FP-side** (the two "Laws that do not hold" FP non-laws at `:69-70`) at cycle-089 by additive inheritance from firm `dot` + firm `apply_linop` through a deterministic IEEE-754 outer `√` (the `nrm2` firmness precedent extended by one firm constituent). Gate (a) — the missing 4-arg `Norml2(comm,x,B,Bx)` √-entry-point test — was judged **REDUNDANT** under the firm-on-positive-structure escape (everything it would confirm is already anchored; materially the `apply_linop` / `eigenfreq_qfactor_reduce` c082 / `sparameter_reduce` c083 / `solve_family` c086 situation). This dispatch (D1, the batch-29 LEAD wave-1) enacts the flip on the verb's own §Status and owns the L1/index + L4/index (matrix-weighted-norm-specific) maturity-label and count updates. It does NOT touch the L1>L0 theme (already firm), consumer files (D2), the reduce-verbs' own status (D3), or feature columns (D4).

## Proposed changes

### 1. book/src/L1/matrix-weighted-norm.md — flip §Status :110 to firm

The file has NO YAML frontmatter (it opens directly with `# matrix-weighted-norm`); maturity lives entirely in the `## Status` line `:110`. No `firmness:`/`status:`/`maturity:` field to flip. The two `verified_against:` blocks (`:145-171` and `:179-205`) are PRESERVED verbatim (they are the firm evidence). The flip restates `:110` + the gate prose `:112-115` as enacted-firm.

```edit:book/src/L1/matrix-weighted-norm.md
<<<OLD :110>>>
`rough-in (test-coverage-bounded)` — signature and algebraic laws are well-anchored by the L0 source (the closed-form `√(xᴴ B x)`, the SPD precondition, the assertion-based numerical-Hermiticity check, the dense and consistent eigensolver-backend callsite cohort), but no dedicated Palace test exercises the SPD-weighted overload at this exact entry point (`test/unit/test-vector.cpp:209-211` exercises only the unweighted `Vector::Norml2()` method form; no `test/unit/test-eigen*.cpp` or `test/unit/test-operator*.cpp` directly tests `linalg::Norml2(comm, x, B, Bx)`). Per `CLAUDE.md` "Tests as semantic supplement" and the cycle-009 meta-phase precedent (eigsolve rough-in pending test-coverage), the entry stays at rough-in.

**Promotion-to-firm gates** (any of):
<<<NEW :110>>>
`firm` — promoted from `rough-in (test-coverage-bounded)` by the batch-28 meta-phase GO (`reports/2026-06-04T032609Z-meta-phase-cycle-090/CYCLE.md` §Decisions "go 1"; enacted cycle-091, the batch-29 LEAD `matrix-weighted-norm-firm-flip-and-cascade-wave`). The signature and the algebraic laws are well-anchored by the L0 source (the closed-form `√(xᴴ B x)`, the SPD precondition, the assertion-based numerical-Hermiticity check, the dense and consistent eigensolver-backend callsite cohort), and **both norm-axiom law-sides are now discharged**:

- **Structure-side (cycle-088):** the inner-product-structure laws — **4 (triangle), 6 (Cauchy–Schwarz), 7 (parallelogram)** — are theorems about ANY inner-product-induced norm, and the SPD premise they require is satisfied **provably-by-construction** at the usage sites (`B = KM = GetInnerProductMatrix(0.0, 1.0, nullptr, M.get())`, "the real SPD part of the mass matrix" — comment at `palace/drivers/eigensolver.cpp:206-207`, the `GetInnerProductMatrix(0.0, 1.0, ...)` call `:212` `SetBMat` `:213`; the `1.0·M->Real()` positive-coefficient FE mass form `palace/models/spaceoperator.cpp:530-537`). They follow as inner-product-space theorems with no positive √-entry-point test (the structure-side analog of the firm-on-positive-structure escape, applied through the SPD construction).
- **FP-side (cycle-089):** the floating-point sub-claims at "Laws that do not hold" `:69-70` discharge to law-confidence by **inheritance** from the firm constituents `dot` (`book/src/L1/dot.md:79-80`) and `apply_linop` (`book/src/L1/apply_linop.md:62-63`) through a **deterministic IEEE-754** outer `√` (`palace/linalg/operator.cpp:606` real, `:618` complex) over **disjoint accumulators** (`B.Mult(x,Bx)` `:602` fully materialises `Bx` before `Dot(comm,Bx,x)` `:603` reads it) — the composition introduces **NO new floating-point property**. This is exactly the `nrm2` firmness precedent (`book/src/L1/nrm2.md:38`; `nrm2` is firm carrying the same two FP non-laws) extended by one additional firm constituent (`apply_linop`).

**The basis is the firm-on-positive-structure escape** (CLAUDE.md §Methodology invariants, the `rough-in (test-coverage-bounded)` bullet): an entry whose laws are syntactic-identity / theorem content on fully-specified positive source is `firm` even with no surrounding test, because the missing test does not gate such laws. Gate (a) below — a dedicated test of the 4-arg SPD-weighted `linalg::Norml2(comm,x,B,Bx)` √-entry-point — was judged **REDUNDANT** by the batch-28 meta-phase: everything it would confirm (the inner-product-space theorems + the inherited FP non-laws) is already anchored; there is NO law/property for which that test is the only evidence. This is materially the same disposition as the four prior escape promotions (`apply_linop`; `eigenfreq_qfactor_reduce` c082; `sparameter_reduce` c083; `solve_family` c086). **Scoping note (not a gate):** the SPD-ness of `B` is *construction-attested* (the only callers are the SPD-construction eigensolver path — `B = KM`, the real SPD part of the mass matrix) rather than runtime-verified; a non-SPD caller's absence is already recorded in §Applicability `:68`. This scoping is the note the escape *requires*, not an independent obstruction.

The original (now-discharged) promotion-to-firm gates are retained below as the discharge record:
<<<END>>>
```

The remaining `## Status` content (`:112-118`, the original `(a)/(b)/(c)` gate descriptions + the cycle-008 OQ note) stays verbatim as the discharge record — the (a) gate description already carries its own cycle-080 "Partially advanced" / "still needs a test" narration, and the (c) gate already records the cycle-088 STRUCTURE-SIDE + cycle-089 FP-side discharge. They are accurate as the historical gate record; the new §Status head (above) states the enacted disposition. The two `verified_against:` blocks (`:145-171` cycle-088 structure-side, `:179-205` cycle-089 FP-side) and the radicand-constituent test-evidence prose (`:143`) are UNCHANGED.

### 2. book/src/L1/index.md — D1 SOLE owner: count header :31, bullet :66 move, dep-map :117, OQ-partial :101, normalize-bullet :40 stale-ref

**2a. Count header `:31` — fold +1 into BOTH counts (30→31 main, 37→38 grand), discharge the pre-staged c080 reconciliation note.** Verified on disk: the dep-map table holds **37** firm rows currently (the lone `rough-in (test-coverage-bounded, …matrix-weighted-norm…)` row is the 38th non-firm row that flips); 30 main + 4 FE-assembly + 3 FE-space = 37 → 31 + 4 + 3 = 38.

```edit:book/src/L1/index.md
<<<OLD (head of :31)>>>
**Firm (30 main cohort; 37 firm grand total incl. the FE-assembly + FE-space sub-spines).** The 30 main-cohort firm operators are listed below; the FE-assembly sub-spine adds **4** more firm
<<<NEW>>>
**Firm (31 main cohort; 38 firm grand total incl. the FE-assembly + FE-space sub-spines).** The 31 main-cohort firm operators are listed below; the FE-assembly sub-spine adds **4** more firm
<<<END>>>
```

```edit:book/src/L1/index.md
<<<OLD (mid :31, the "= 37" derivations)>>>
30 main + 4 FE-assembly + 3 FE-space = 37; equivalently the dep-map table now holds **37** `firm` rows
<<<NEW>>>
31 main + 4 FE-assembly + 3 FE-space = 38; equivalently the dep-map table now holds **38** `firm` rows (incl. `matrix-weighted-norm` c091 — promoted rough-in (test-coverage-bounded)→firm by the batch-29 LEAD firm-flip-and-cascade wave, the main-cohort's 31st firm member)
<<<END>>>
```

```edit:book/src/L1/index.md
<<<OLD (tail of :31, the count-reconciliation note — DISCHARGE it)>>>
**Count-reconciliation note for the per-report integrator (cycle-080):** this tally is authored count-owner-blind to co-dispatched D1 (a `matrix-weighted-norm` lowering-verifier audit). IF D1's audit promotes `matrix-weighted-norm` rough-in→firm, fold its **+1** into BOTH the main-cohort count (30→31) and the grand total (37→38) when applying serially (and move its bullet from the §"Rough-in (test-coverage-bounded)" sub-list to the firm sub-list); this tally counts ONLY this dispatch's `eigenvalue-untransform` +1.
<<<NEW>>>
**Count-reconciliation note DISCHARGED (cycle-091, batch-29 LEAD):** the pre-staged c080 reconciliation +1 is now folded — `matrix-weighted-norm` was promoted rough-in (test-coverage-bounded)→firm by the firm-flip-and-cascade wave, its bullet moved from the §"Rough-in (test-coverage-bounded)" sub-list to the firm sub-list, and BOTH the main-cohort count (30→31) and the grand total (37→38) updated above.
<<<END>>>
```

Also update the count-header's narrative list of "main-cohort firm operators" to NAME the new member — the header's prose enumerates the 30 (now 31) main-cohort firm operators. Append `matrix-weighted-norm` to that enumeration:

```edit:book/src/L1/index.md
<<<OLD (the enumeration tail of :31, "…and the driven per-ω system-operator assembly (`assemble_frequency_operator`, c062):")>>>
the floquet-periodicity B-field correction gate, and the driven per-ω system-operator assembly (`assemble_frequency_operator`, c062):
<<<NEW>>>
the floquet-periodicity B-field correction gate, the driven per-ω system-operator assembly (`assemble_frequency_operator`, c062), and the SPD operator-weighted energy norm (`matrix-weighted-norm`, c091 — `‖x‖_B = √(xᴴ B x)`, promoted rough-in (test-coverage-bounded)→firm by the batch-29 LEAD firm-flip-and-cascade wave on the firm-on-positive-structure escape, both norm-axiom law-sides discharged c088 structure + c089 FP, gate (a) judged redundant):
<<<END>>>
```

**2b. Bullet `:66` — move from the §"Rough-in (test-coverage-bounded)" sub-list to the firm sub-list, re-anchored to firm.** Remove the matrix-weighted-norm bullet from under the `**Rough-in (test-coverage-bounded)**` header (`:64`) — leaving `bilinear-form` `:67` as the sole remaining entry there — and insert the re-anchored firm bullet into the firm prose list (placed after `normalize` `:40`, whose own bullet references matrix-weighted-norm's `normalize_B` sibling, so the adjacency is meaningful).

REMOVE from the rough-in sub-list (`:66`):

```edit:book/src/L1/index.md
<<<OLD :66 (delete this bullet)>>>
- [`matrix-weighted-norm`](./matrix-weighted-norm.md) — pure operator-weighted Euclidean norm `‖x‖_B = √(xᴴ B x)` for SPD `B`; the energy-norm primitive at L1; the M-orthonormalisation norm in the generalised eigenvalue problem. Rough-in status motivated by absence of dedicated test coverage on the SPD-weighted `linalg::Norml2(comm, x, B, Bx)` overload (`test/unit/test-vector.cpp` covers only the unweighted method form). Promotion to firm gated on (a) dedicated test coverage, (b) indirect coverage via eigensolver test outputs, or (c) algebraic-law completeness verification.

<<<NEW (the bullet is removed entirely from here)>>>
<<<END>>>
```

INSERT into the firm sub-list, after the `normalize` bullet (`:40`):

```edit:book/src/L1/index.md
<<<OLD (anchor: end of the normalize bullet :40)>>>
Carries an in-chapter **rough-in note** for the B-weighted sibling `normalize_B` (no fused Palace site; inherits `matrix-weighted-norm`'s test-coverage bound).
<<<NEW>>>
Carries an in-chapter note for the B-weighted sibling `normalize_B` (no fused Palace site; its `matrix-weighted-norm` constituent is now **firm** c091, so the formerly-inherited test-coverage bound is **lifted** — the note no longer cites a rough-in norm constituent; `normalize` itself stays firm).
- [`matrix-weighted-norm`](./matrix-weighted-norm.md) — pure operator-weighted Euclidean energy norm `‖x‖_B = √(xᴴ B x)` for SPD `B`; the energy-norm primitive at L1; the M-orthonormalisation norm in the generalised eigenvalue problem (`A x = λ B x`). Factors through firm [`dot`](./dot.md) + firm [`apply_linop`](./apply_linop.md) (the canonical L1 dependency pattern). Promoted rough-in (test-coverage-bounded)→**firm** cycle-091 (the batch-29 LEAD firm-flip-and-cascade wave) on the **firm-on-positive-structure escape**: both norm-axiom law-sides discharged — structure-side laws 4/6/7 as inner-product-space theorems over the provably-SPD `B = KM` (c088), FP-side `:69-70` by additive inheritance from firm `dot`/`apply_linop` through a deterministic IEEE-754 outer `√` (c089, the `nrm2` precedent + one firm constituent). Gate (a)'s missing 4-arg `Norml2(comm,x,B,Bx)` √-entry-point test judged REDUNDANT by the batch-28 meta-phase (everything it would confirm is already anchored); the SPD-construction-attested scoping note is the note the escape requires, NOT a gate.
<<<END>>>
```

**2c. Dep-map row `:117` — status cell → firm.**

```edit:book/src/L1/index.md
<<<OLD :117>>>
| [`matrix-weighted-norm`](./matrix-weighted-norm.md) | `(x: Tensor[N], B: LinearOperator[N, N]) → Scalar` (real-valued, SPD `B` required for norm) | `dot`, `apply_linop` | `rough-in (test-coverage-bounded, harvested-by: harvester:2026-05-27T215334Z-harvester-matrix-weighted-norm-l1)` |
<<<NEW :117>>>
| [`matrix-weighted-norm`](./matrix-weighted-norm.md) | `(x: Tensor[N], B: LinearOperator[N, N]) → Scalar` (real-valued, SPD `B` required for norm) | `dot`, `apply_linop` | `firm` (energy-norm primitive `‖x‖_B = √(xᴴ B x)`; promoted rough-in (test-coverage-bounded)→firm cycle-091 by the batch-29 LEAD firm-flip-and-cascade wave on the firm-on-positive-structure escape — both norm-axiom law-sides discharged c088 structure-side laws 4/6/7 over provably-SPD `B = KM` + c089 FP-side inheritance from firm `dot`/`apply_linop` through deterministic IEEE-754 `√`; gate (a) √-entry-point test judged redundant per the batch-28 meta-phase; SPD-construction-attested scoping note non-gating) |
<<<END>>>
```

**2d. OQ-partial note `:101` — re-anchor the matrix-weighted-norm half to firm-landed.**

```edit:book/src/L1/index.md
<<<OLD :101>>>
- (empty as of cycle-010) — the cycle-008 OQ `matrix-weighted-norm-and-bilinear-form-l1-rough-ins` is now `partially-answered`: both halves landed in cycle-010 wave-1 as rough-ins ([`matrix-weighted-norm`](./matrix-weighted-norm.md) and [`bilinear-form`](./bilinear-form.md)). The `SpectralNorm` (power-iteration) sibling and the L1>L0 lowering theme for both operators remain tracked under that OQ's residuals.
<<<NEW :101>>>
- (empty as of cycle-010) — the cycle-008 OQ `matrix-weighted-norm-and-bilinear-form-l1-rough-ins` is now `partially-answered`: both halves landed in cycle-010 wave-1 as rough-ins; the [`matrix-weighted-norm`](./matrix-weighted-norm.md) half is now **firm** (promoted cycle-091 by the batch-29 LEAD firm-flip-and-cascade wave), while the [`bilinear-form`](./bilinear-form.md) half remains rough-in (its own `lower-layer-shared-vocabulary` gate, tracked under D3's gram_reduce residual). The `SpectralNorm` (power-iteration) sibling and the L1>L0 lowering theme remain tracked under that OQ's residuals (the matrix-weighted-norm L1>L0 theme `matrix-weighted-norm-mutation-rotation` is itself firm).
<<<END>>>
```

### 3. book/src/L4/index.md — D1 SOLE owner of matrix-weighted-norm-specific labels; reduce-verb-status lines DEFERRED to D3

I re-anchor ONLY the standalone matrix-weighted-norm folded-primitive maturity LABEL that is unambiguous regardless of D3's verdict — the `:98` `domain_energy_reduce` Folds-cell annotation directly attached to the `[matrix-weighted-norm]` link. I do **NOT** change any reduce-verb's OWN status token, any reduce-verb gating-rationale sentence (whose final wording depends on D3's firm/stay verdict), the `:102` joint `(rough-in L1)` label (it also covers still-rough-in `bilinear-form`), or the `:57` "Rough-in at L4 (1)" count header. Those are DEFERRED for D3-verdict coordination (flagged below).

**3a. `:98` `domain_energy_reduce` dep-map row — re-anchor the standalone matrix-weighted-norm folded-primitive label in the Folds cell (firm), PRESERVE the reduce-verb's own `rough-in` status token + its gating rationale (D3's call).**

```edit:book/src/L4/index.md
<<<OLD (in the Folds cell of :98)>>>
| Folds: [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (rough-in — the domain-restricted energy numerator `½⟨field, M_idx field⟩`), [`participation_ratio`](../L1/participation_ratio.md) (firm — the `energyᵢ/e_total` quotient).
<<<NEW>>>
| Folds: [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (firm c091 — the domain-restricted energy numerator `½⟨field, M_idx field⟩`), [`participation_ratio`](../L1/participation_ratio.md) (firm — the `energyᵢ/e_total` quotient).
<<<END>>>
```

NOTE on `:98` Status cell: the rationale sentence "rough-in not firm because the folded domain-restricted energy form is the `matrix-weighted-norm` `rough-in (test-coverage-bounded)` primitive AND there is no dedicated per-domain energy-participation test" is `domain_energy_reduce`'s gating rationale. With matrix-weighted-norm now firm, that rationale either narrows (to the per-domain-test gate only) or is deleted (if D3 firms domain_energy_reduce). This is D3's re-judgment — **DEFERRED, flagged below.** I leave the `:98` Status cell unchanged in this wave-1 dispatch.

**3b. `:102` `gram_reduce`, `:59` domain_energy_reduce bullet, `:57` header — DEFERRED to D3 coordination (NOT edited this wave).**
- `:102` Folds cell opens `Folds (rough-in L1): [matrix-weighted-norm] …, [bilinear-form] …` — a JOINT label covering BOTH the now-firm matrix-weighted-norm AND the still-rough-in bilinear-form. Splitting it (firm matrix-weighted-norm / rough-in bilinear-form) is entangled with D3's gram_reduce re-judgment of its residual bilinear-form gate; the `:102` Status cell "gated rough-in because the folded L1 primitives are themselves rough-in" persists (bilinear-form stays rough-in). Leaving the `:102` row to D3-verdict coordination per the plan's "do NOT change any reduce-verb maturity label or the count header that depends on them."
- `:59` domain_energy_reduce prose bullet: "gated because the folded domain-restricted energy form is the `matrix-weighted-norm` `rough-in (test-coverage-bounded)` primitive" — same reduce-verb gating rationale as `:98` Status; DEFERRED to D3.
- `:57` "Rough-in at L4 (1)" header: the count "(1)" and whether domain_energy_reduce stays in the rough-in cohort is D3's verdict; the header's matrix-weighted-norm-gating phrasing depends on it. DEFERRED per the plan's explicit wave-2 coordination instruction.

## Operator content

This is a maturity flip on an already-fully-authored firm-apparatus chapter, not a fresh harvest — the signature, semantics, 12 algebraic laws, applicability conditions, dependencies, variant axes, evidence, and the two `verified_against:` blocks are all already on disk and PRESERVED. The flip restates only the `## Status` head and the cross-file maturity labels/counts. The firm entry, post-flip:

- **Slug + one-line:** `matrix-weighted-norm` — mutation-free SPD operator-weighted vector norm `α = ‖x‖_B = √(xᴴ B x)`.
- **Signature:** `matrix_weighted_norm :: (x: Tensor[N], B: LinearOperator[N, N]) -> Scalar` (result always real ≥ 0 under SPD `B`; `B` square `[N,N]`, Hermitian, SPD).
- **Algebraic laws (now firm):** 12 hold (non-negativity, separation, positive homogeneity `|α|`, triangle, reverse triangle, B-Cauchy–Schwarz, parallelogram, self-bilinear identity `‖x‖²_B = xᴴ B x`, identity-operator collapse `‖x‖_I = nrm2(x)`, diagonal-scaling structure, phase invariance, zero-in-argument). Stated absences hold (no B-linearity, no vector-side linearity, no norm contract for indefinite `B`, ULP-strict-CS-in-FP non-law, bit-determinism-across-B-representations non-law). The norm-axiom laws 4/6/7 are inner-product-space theorems (structure-side discharge c088); the two FP non-laws inherit additively from firm `dot`/`apply_linop` through a deterministic `√` (FP-side discharge c089).
- **Dependencies:** firm [`dot`](book/src/L1/dot.md) + firm [`apply_linop`](book/src/L1/apply_linop.md) (both firm — the canonical two-leaf L1 energy-norm factoring).
- **Status:** `firm` (promoted from `rough-in (test-coverage-bounded)` cycle-091 on the firm-on-positive-structure escape; gate (a) redundant per the batch-28 meta-phase GO).
- **Record definitions:** the signature names no record/struct (`Tensor[N]`, `LinearOperator[N,N]`, `Scalar` are L1 primitive shape-contract types, not records). No `## Record definition` obligation triggered.
- **Evidence:** the named √-overload `linalg::Norml2(comm,x,B,Bx)` (`palace/linalg/operator.hpp:372-374` decl, `palace/linalg/operator.cpp:599-619` real+complex specializations, `:606`/`:618` the outer `√`); the SPD-construction provenance `B = KM = GetInnerProductMatrix(0.0,1.0,nullptr,M.get())` (`palace/drivers/eigensolver.cpp:205-213`, comment `:206-207`; `palace/models/spaceoperator.cpp:530-537`); the three-backend eigensolver callsite cohort (ARPACK `palace/linalg/arpack.cpp:433-444,470`; SLEPc `palace/linalg/slepc.cpp:470-481,505`; NLEPS `palace/linalg/nleps.cpp:109-119,146`); the radicand-constituent test `test/unit/test-domainpostoperator.cpp:75-93`. The two `verified_against:` blocks (c088 structure-side, c089 FP-side) are the discharge evidence; the meta-phase GO is `reports/2026-06-04T032609Z-meta-phase-cycle-090/CYCLE.md`.

## Supporting evidence

- **The firm basis (the meta-phase GO):** `reports/2026-06-04T032609Z-meta-phase-cycle-090/CYCLE.md` §Decisions "go 1" — the firm-on-positive-structure escape applies; gate (a) judged REDUNDANT; the four prior escape promotions (`apply_linop` / `eigenfreq_qfactor_reduce` c082 / `sparameter_reduce` c083 / `solve_family` c086) are the precedent.
- **The two verified_against blocks (PRESERVED as the evidence):**
  - cycle-088 structure-side (`book/src/L1/matrix-weighted-norm.md:145-171`): laws 4/6/7 discharged as inner-product-space theorems over the provably-SPD `B = KM`; SPD-construction provenance at `eigensolver.cpp:205-213` + `spaceoperator.cpp:530-537`.
  - cycle-089 FP-side (`book/src/L1/matrix-weighted-norm.md:179-205`): the two FP non-laws inherit additively from firm `dot` (`dot.md:79-80`) + firm `apply_linop` (`apply_linop.md:62-63`) through a deterministic IEEE-754 `√` over disjoint accumulators; the `nrm2` firmness precedent (`nrm2.md:38`) extended by one firm constituent.
- **L0 anchor self-verification (citecheck, pre-emit):**
  - `operator.cpp:606 --anchor sqrt` → `[ok]` (the real-branch outer `√`).
  - `spaceoperator.cpp:530-537 --anchor GetInnerProductMatrix` → `[ok]` (the SPD construction `1.0·M->Real()`).
  - `eigensolver.cpp:206-207` is the SPD-comment ("the real SPD part of the mass matrix"); the `GetInnerProductMatrix` CALL is at `:212` and `SetBMat` at `:213` (direct on-disk Read confirmed). My restated Status prose cites the comment at `:206-207` (correct) and the call at `:212`/`:213` (correct) — distinct from the existing verified_against block's `:205-213` whole-block citation (preserved unchanged). I did NOT introduce the drifted `:206-207 --anchor GetInnerProductMatrix` form.
- **Count verification (on disk):** `grep -cE '^\| \[\`…\`\]\(…\) \|.*\| \`?firm' book/src/L1/index.md` → **37** firm dep-map rows currently; the lone matrix-weighted-norm `rough-in (test-coverage-bounded, …)` row flips → **38**. Confirms 30→31 main / 37→38 grand.

## Count deltas applied (old→new)

- **L1/index.md `:31` count header:** main cohort **30 → 31**; firm grand total **37 → 38**; dep-map firm-row count **37 → 38**. The c080 pre-staged reconciliation note is DISCHARGED (rewritten as discharged-record).
- **L1/index.md `:66` bullet:** moved from the §"Rough-in (test-coverage-bounded)" sub-list (leaving `bilinear-form` `:67` as the sole remaining entry there) to the firm sub-list (inserted after `normalize` `:40`), re-anchored to firm.
- **L1/index.md `:117` dep-map status cell:** `rough-in (test-coverage-bounded, …)` → `firm (…)`.
- **L1/index.md `:101` OQ-partial:** matrix-weighted-norm half re-anchored to firm-landed; bilinear-form half kept open.
- **L1/index.md `:40` normalize bullet:** the stale "inherits `matrix-weighted-norm`'s test-coverage bound" clause re-narrated to "bound lifted (matrix-weighted-norm now firm)" — a same-file stale-label catch under the `firm-promotion-coupled-re-anchor-needs-whole-book-cross-reference-grep` discipline (normalize itself stays firm).

## L4/index labels touched + the :57-header coordination flagged for D3

- **Touched (firm-flip, matrix-weighted-norm-specific):** `book/src/L4/index.md:98` — the `domain_energy_reduce` Folds-cell standalone matrix-weighted-norm label `(rough-in — the domain-restricted energy numerator …)` → `(firm c091 — …)`. This is the ONE unambiguous matrix-weighted-norm folded-primitive label that flips regardless of D3's verdict.
- **DEFERRED to D3-verdict coordination (NOT edited this wave-1 dispatch), flagged per the plan's wave-2 instruction:**
  - `:57` "Rough-in at L4 (1)" header — the count "(1)" and the matrix-weighted-norm-gating phrasing depend on whether D3 firms `domain_energy_reduce` (firm → "(0)" + move bullet to firm cohort; stay → "(1)" + re-narrate the gate to the per-domain-test-only residual). **D1 coordinates this header with D3's verdict.**
  - `:98` `domain_energy_reduce` Status-cell gating rationale + `:59` its prose bullet — the "rough-in because the folded … is the matrix-weighted-norm rough-in primitive" sentences are domain_energy_reduce's gating rationale, rewritten by D3's re-judgment.
  - `:102` `gram_reduce` row — the JOINT `(rough-in L1)` Folds label covers BOTH the now-firm matrix-weighted-norm AND the still-rough-in bilinear-form; the split + the persisting "gated rough-in (bilinear-form residual)" Status are entangled with D3's gram_reduce re-judgment (D3 predicts STAYS rough-in on the bilinear-form residual gate).

  **Coordination note for the integrator / D3:** since per-report integration serializes D1→D2→D3→D4, D3's gram_reduce/domain_energy_reduce verdicts land in the reduce-verb CHAPTER files (D3's scope), and the matching L4/index.md `:57`/`:59`/`:98`-Status/`:102` reduce-verb-status lines need to be reconciled to D3's verdict. Per the single-index-owner rule D1 is SOLE owner of L4/index.md — so these lines should be applied as a D1-owned follow-up keyed on D3's on-disk verdict. I have left them at their current (matrix-weighted-norm-rough-in-citing) wording so the integrator can apply the D3-coordinated reconciliation in one consistent pass once D3's verdict is known, rather than guessing it blind in wave-1.

## Open questions / caveats

- **L4/index `:57`/`:59`/`:98`-Status/`:102` reduce-verb-status reconciliation is owed, gated on D3's verdict** (the central wave-2 coordination). I deferred all reduce-verb gating-rationale lines + the `:57` count header rather than guess D3's firm/stay outcome for `domain_energy_reduce` and `gram_reduce`. Whoever applies the D3-coordinated L4/index reconciliation must: (i) if D3 firms `domain_energy_reduce`, flip `:57` "(1)"→"(0)", move its bullet to the firm cohort, update `:98` Status to firm; else re-narrate `:98` Status / `:59` bullet to "gated on the per-domain test only (matrix-weighted-norm now firm)"; (ii) split the `:102` joint `(rough-in L1)` label to "matrix-weighted-norm firm / bilinear-form rough-in" and keep gram_reduce's Status as D3 rules (predicted STAYS rough-in on the bilinear-form residual gate). Flagged so the matrix-weighted-norm-firm consequence is not lost in those lines.
- **The `firm-promotion-coupled-re-anchor-needs-whole-book-cross-reference-grep` discipline is exercised at ~30-file scale for the first time this cycle** (the batch-28 meta-phase watch-note). My in-file grep of L1/index.md caught the stale `:40` normalize-bullet clause beyond the planner-listed anchors (`:31`/`:66`/`:117`/`:101`); the broader consumer cross-reference re-anchor is D2's cluster. If any L1/L4-index matrix-weighted-norm label is missed, it surfaces as a c092 land-clean residue (the c087 solve_family precedent) — the per-anchor checklist above is scoped to minimize it.
- **No record-definition obligation** — the signature names only L1 primitive shape-contract types (`Tensor[N]`, `LinearOperator[N,N]`, `Scalar`), no record/struct, so the record-definition sub-check no-ops.
- **The L1>L0 theme `matrix-weighted-norm-mutation-rotation` is NOT touched** (already firm `:432` on disk; the verb flip does not change the theme's maturity) — per the hard constraint.
