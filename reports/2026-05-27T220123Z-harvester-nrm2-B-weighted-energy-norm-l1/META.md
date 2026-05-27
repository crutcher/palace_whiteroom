---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T220500Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
---

# META: verification of `nrm2_B-weighted-energy-norm` duplicate-resolution dispatch

## Critique

### Checks run

**1. citation-validity — pass.** Every L0, OQ, and priority citation in the report verifies against the cited evidence.
- `palace/linalg/operator.hpp:372-374` declares exactly one `Norml2(MPI_Comm comm, const VecType &x, const Operator &B, VecType &Bx)` template (verified by direct read; the SPD comment is at line 372, the template line is 373, the signature line is 374). A separate `grep -n "Norml2" operator.hpp` confirms only two references in that file: line 374 (the declaration) and line 380 (inside the `Normalize` body that calls it). No second `Norml2(..., B, ...)` overload exists.
- `palace/linalg/operator.cpp:599-619` provides exactly the two template specializations described — `Vector` at 599-607 and `ComplexVector` at 609-619 — each implementing the closed-form `√(xᴴ B x)` via `B.Mult(x, Bx); dot = Dot(comm, Bx, x); return std::sqrt(...)`. The `MFEM_ASSERT(dot > 0.0)` is at 604-605 (real) and 616-617 (complex with `<1e-9 * dot.real()` imaginary tolerance). All character-level citations in the dispatch agree with source.
- The cycle-003 OQ `nrm2-B-weighted-energy-norm-harvest` exists at `scaffolding/open-questions.md:198-207`, opened by `harvester` at cycle-003, status `open`, with the exact prose the dispatch summarises ("The L0 surface uses overloading...the B-weighted form requires an `apply`-style operator-application primitive...").
- The cycle-008 OQ `matrix-weighted-norm-and-bilinear-form-l1-rough-ins` exists at `scaffolding/open-questions.md:1357-1366`, opened by `layer-intro-author` at cycle-008, status `open`, with the exact "Candidate rough-in names: `L1/nrm2_weighted` and `L1/dot_bilinear`" content. The dispatch's claim that this OQ was filed from the L0 chapter is correct (the source field cites `reports/2026-05-27T173523Z-layer-intro-author-L0-bootstrap-bundle-4/CYCLE.md`).
- `scaffolding/priorities.md:30` reads exactly as quoted: "13. **nrm2_B-weighted-energy-norm-L1** — depends on `apply_linop` (now firm) and `dot` (firm cycle-002). Citation: open question `nrm2-B-weighted-energy-norm-harvest`."
- `scaffolding/priorities.md:37` reads exactly as quoted: "L1 cohort growth: `matrix-weighted-norm` + `bilinear-form` L1 rough-ins (cycle-008 OQ carried forward)..."
- `book/src/L1/nrm2.md:13` carries the sibling-boundary statement quoted verbatim ("The B-weighted overload `linalg::Norml2(comm, x, B, Bx)` at `palace/linalg/operator.cpp:600-619` is **not** part of this operator... a separate L1 operator candidate (forthcoming) that depends on both `dot` and the operator-application primitive `apply_linop`.").
- `book/src/L1/index.md:51` carries the Queued line "`nrm2_B :: (x, B) → √(xᴴ B x)` — energy norm; depends on `dot` and `apply_linop`. Recorded as a boundary in `nrm2`'s entry; deferred to a separate harvest. Slug: `nrm2-B-weighted-energy-norm-harvest`." — verbatim.
- `book/src/L0/linalg-operator-file.md:30-33` enumerates the four `linalg::` free functions, with `Norml2(comm, x, B, Bx)` named as the SPD-`B`-weighted norm anchored at `operator.cpp:600-619`. The dispatch cites this correctly.
- `SpectralNorm` is at `operator.hpp:398-401` as cited, and is correctly distinguished from `Norml2(...,B,...)` (power iteration, not energy norm).

**2. surface-or-evidence — pass.** This is not a refinement-shaped proposal; it is a duplication-resolution dispatch that explicitly produces **no new file** and **no `book/` mutations**. The only proposed changes are append-only OQ-resolution notes and a priority-closure note — both are scaffolding writes, not surface refinements. The dispatch correctly scopes itself: "this dispatch must not race with it [wave-1]" (line 77). The verdict (case (c) merge-and-rename) is supported by cite-evidence in §Supporting evidence (lines 87-94): same L0 anchor, same closed-form, same dependencies, same SPD precondition, same variant axes, same callsite cohort. This is the appropriate evidence-shape for a "these are the same operator" verdict.

**3. rotation-quality — pass (not applicable).** No new L_n form is proposed and no rotation is asserted. The dispatch is procedural cleanup, not a rotation claim. Marked pass per the "not applicable" convention.

**4. variant-axis-coverage — pass.** The dispatch's role here is to audit whether the wave-1 `matrix-weighted-norm` entry covered all variant axes the cycle-003 OQ `nrm2-B-weighted-energy-norm-harvest` would have requested. Direct comparison: cycle-003 OQ requested (a) the SPD-`B`-weighted norm `√(xᴴ B x)`, (b) workspace `Bx`, (c) dependency on `apply` (matrix-vector multiplication) once firm at L1, (d) SPD precondition; wave-1 covers all four: closed-form and SPD precondition at lines 67-69 of wave-1 CYCLE.md; workspace `Bx` discussion at lines 60-61 (treated as caller-supplied workspace; L1 absorbs); `apply_linop` dependency at lines 136-138. The element-type axis (real / complex) is covered at wave-1 lines 144-147 (collapses to one L1 operator). The dispatch correctly notes the `bilinear-form` half remains residual — but bilinear-form is genuinely a separate operator (see "Critical methodology checks" below), not a missing axis on `matrix-weighted-norm`. No hidden branches.

**5. cross-reference-integrity — pass.** All cross-references resolve:
- Wave-1 report path `reports/2026-05-27T215334Z-harvester-matrix-weighted-norm-l1/CYCLE.md` exists (verified via `ls`).
- All `book/src/L0/`, `book/src/L1/` file references resolve to extant files with the cited content.
- The two OQ slugs (`nrm2-B-weighted-energy-norm-harvest`, `matrix-weighted-norm-and-bilinear-form-l1-rough-ins`) resolve to extant ledger entries at the cited line ranges.
- Priority #13 and #17 resolve at `scaffolding/priorities.md` lines 30 and 36-40 respectively.
- The proposed new OQ slug `nrm2-b-weighted-energy-norm-and-matrix-weighted-norm-duplicate-target` follows the existing slug convention and does not collide with extant slugs.

**6. edge-label-fidelity — pass.** The dispatch claims priority #13 (`nrm2_B-weighted-energy-norm-L1`) is "closed-as-landed" by the wave-1 `matrix-weighted-norm` landing. Verification: priority #13 names the operator `nrm2_B-weighted-energy-norm-L1` with dependencies `apply_linop` and `dot` and citation to OQ `nrm2-B-weighted-energy-norm-harvest`. The cycle-003 OQ describes the operator-weighted norm `‖x‖_B = √(xᴴ B x)` at `operator.cpp:600-619`. Wave-1's `matrix-weighted-norm` is anchored at exactly `operator.cpp:599-619` (one-line broader range) with the same closed-form and the same two L1 dependencies. Priority #13 is therefore genuinely closed by the wave-1 landing — same operator, different slug. The close-as-landed verdict is faithful to the edge.

**7. plan-kind-consistency — pass.** The dispatch's declared verdict is `duplicate-of-sibling-wave-1-merge-and-rename` — not `firm` / `rough-in` / `theme` / `audit`. The content shape matches: no new operator content authored; only OQ-resolution and priority-closure scaffolding edits; explicit "Operator content: Not authored in this dispatch" (§Operator content, line 81). The no-new-file authority is appropriate given the duplication finding. The harvester role normally produces L_n entries, but the wave-1 sibling already produced the canonical entry; this dispatch correctly de-escalates to a procedural-cleanup posture rather than producing a competing entry.

**8. skill-uptake-survey — pass.** The dispatch identifies a planner-side deduplication-by-L0-anchor pattern (§Open questions item 3, lines 103-105; and §Open questions item 7, line 111) and routes it as a cycle-012 meta-phase watch-item rather than filing a new friction-ledger entry. This is appropriate proportionality: recurrence-1 is below the friction-ledger threshold (≥2 cycles or concrete-enough-to-write or pre-existing-entry), and meta-phase routing aggregates the observation with whatever cycle-011/012 evidence emerges. No skill-friction observed; no pre-existing skill (`classify-variant-axis`, `verify-citation-range`, `verify-refinement-surface`, etc.) would have prevented the duplication — this would be a new planner-side or meta-phase-side check, appropriately routed to meta-phase consideration rather than acted on in this dispatch.

### Critical methodology checks specific to this dispatch

**Duplication-confirmation rigor.** I verified each of the five identity claims against the wave-1 entry:

- *Same L0 anchor* — wave-1 lines 19-22: "L0 anchor: `palace::linalg::Norml2(MPI_Comm comm, const VecType &x, const Operator &B, VecType &Bx)` declared at `palace/linalg/operator.hpp:372-374`, implemented at `palace/linalg/operator.cpp:599-619` (two template specializations, real and complex)." Matches this dispatch's anchor exactly.
- *Same closed-form `√(xᴴ B x)`* — wave-1 line 67-68: `matrix_weighted_norm(x, B) = √(xᴴ B x)` for SPD `B`. Matches.
- *Same SPD applicability with SPSD-seminorm caveat* — wave-1 lines 100-101 (laws 1, 2 of wave-1's algebraic laws section) and lines 121-128 (Applicability conditions): "B must be positive-definite (SPD) for the operator to be a true norm (separation law 2). Without SPD, separation fails on the null space of B and the construct is a seminorm." Matches.
- *Same dependencies (`dot` + `apply_linop`)* — wave-1 lines 134-138 (Dependencies section) and line 144 (variant axes section header). Matches.
- *Same element-type variant axis (real/complex collapses to one L1 operator)* — wave-1 lines 144-147 (Variant axes): "element-type: `real` | `complex`... At L1 these collapse to a single operator with the same signature `(x: Tensor[N], B: LinearOperator[N, N]) → Scalar(real)`...". Matches.
- *Same M-orthonormalisation callsite cohort* — wave-1 lines 179-184: arpack.cpp, slepc.cpp, nleps.cpp all using the operator in `GetEigenvectorNorm`. Matches.

All five identity claims hold; the duplication verdict is rigorously supported.

**Bilinear-form correctly held separate.** The dispatch flags (§Open questions item 5, line 107) that `bilinear-form` is NOT a duplicate of `matrix-weighted-norm` despite shared surface appearance. Verification:
- `matrix-weighted-norm`: `√(xᴴ B x)`, single-arg in vector, SPD-required, outer `sqrt`, applies `B` to one vector. L0 anchor: `linalg::Norml2(comm, x, B, Bx)` at `operator.hpp:374` / `operator.cpp:599-619`.
- `bilinear-form`: `yᴴ A x`, two-arg in vectors (x and y), NO SPD requirement, NO outer `sqrt`, applies `A` to one of two distinct vectors. L0 anchor: `linalg::Dot(comm, x, A, y)` at `operator.hpp:386-394` / `operator.cpp:621-639` (verified directly — the implementation signature is `Dot(MPI_Comm comm, const ComplexVector &x, const Operator &A, const ComplexVector &y)`, takes both `x` and `y` as inputs, allocates `Ax` internally, returns `std::complex<double>`).
- L0 anchors differ (different lines, different signatures, different return type, different workspace ownership — internal vs. caller-supplied).
- L1 signature would differ (two-arg `(x, A, y)` vs. single-arg-plus-operator `(x, B)`).

The distinction is correct; bilinear-form genuinely needs its own L1 entry.

**Friction-ledger vs. meta-phase-routing proportionality.** The dispatch routes the deduplication-by-L0-anchor observation as a "watch-item for cycle-012 meta-phase planner-role refinement" rather than filing a friction-ledger entry now. I checked `scaffolding/friction-ledger.md` — no existing entry for `oq-duplicate-detection`, `deduplicate-by-L0-anchor`, or similar (grep `duplicate|deduplicat|same-operator|L0-anchor` returns no matches in the ledger). The proportionality judgment is appropriate:
- Recurrence-1: only one observation of the pattern (this cycle).
- The friction-ledger promotion bar (per CLAUDE.md §Skills "pattern observed ≥2 cycles OR candidate sketch concrete enough to write as SKILL.md OR friction-ledger entry exists") is not met.
- Meta-phase already runs after cycle-012 (3-cycle batch cadence post cycle-009) and naturally aggregates evidence; if cycle-010 or cycle-011 surfaces another OQ-duplication-by-L0-anchor case, that recurrence-2 evidence will land for meta-phase consideration concurrently.
- The watch-item routing is therefore *not* a workaround for under-filing; it is appropriate use of the 3-cycle aggregation cadence the methodology specifies.

### Issues found

None substantive. The dispatch performs its narrow procedural-cleanup role correctly: it verifies duplication against the wave-1 entry, scopes its own product to OQ-resolution and priority-closure notes only, declines to race with the wave-1 surface write, correctly distinguishes `bilinear-form` from `matrix-weighted-norm`, and proportionately routes its meta-observation to the cycle-012 meta-phase rather than over-filing.

Minor observations (informational, not action items for the repairer):

- (informational) The dispatch proposes a new OQ slug `nrm2-b-weighted-energy-norm-and-matrix-weighted-norm-duplicate-target` (§Proposed changes, line 48). This slug is long; if the integrator finds it unwieldy, a shorter form like `matrix-weighted-norm-duplicate-resolution` would be equivalent. This is integrator-style judgment, not a critique finding.
- (informational) Wave-1 also independently proposed an OQ `matrix-weighted-norm-naming-sweep` (wave-1 §Open questions item 1). This dispatch correctly notes it (§Open questions item 1, line 99) and does not duplicate it. The integrator should ensure only one of the two reports lands the naming-sweep OQ — but this is a routine integrator-finalize-staging concern, not a critique finding here.
- (informational) Both reports propose the same edit pattern on `book/src/L1/index.md` line 51 (remove the `nrm2_B` Queued line). Wave-1 already proposes this edit explicitly (wave-1 §Index update detail, "Change 1"). This dispatch correctly does NOT propose its own edit to `book/src/L1/index.md` (line 77: "No edits to `book/src/L1/index.md`"). The integrator-per-report ordering (wave-1 first, then this dispatch) will resolve cleanly — this dispatch only adds OQ-ledger and priority-resolution edits on top of wave-1's surface edits.
