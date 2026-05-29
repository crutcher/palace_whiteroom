---
verifies: ../REPORT.md
critiqued_at: 2026-05-29T072712Z
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
repaired_at: 2026-05-29T074512Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: repaired
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "Formalize nleps_deflated_residual at L1"

## Critique

### Checks run

**citation-validity — pass.** Every pinpoint citation in the entry was re-verified line-exact against `palace/linalg/nleps.cpp` via `palace-codemap read_range`. The load-bearing lambda body `:547-576` matches verbatim: comment `:547-549` ("Evaluate the deflated residual r = T(lam) vv + T(lam) X (lam I - H)^-1 vv2, with rr2 = X^* vv"); lambda capture `[this, &k, &H, &X]` at `:550`; `A2_out = (*funcA2)(std::abs(lam.imag()))` `:556`; `BuildParSumOperator({1.0+0.0i, lam, lam*lam, 1.0+0.0i}, {opK, opC, opM, A2_out.get()}, true)` `:557`; `A->Mult(vv, rr)` `:559`; `if (k > 0)` `:560`; `S = lam * Eigen::MatrixXcd::Identity(k, k) - H` `:562`; `XSvv2 = MatVecMult(X, S.fullPivLu().solve(vv2))` `:563`; `A->AddMult(XSvv2, rr, 1.0)` `:564`; `rr2.conservativeResize(k)` `:565`; `rr2(j) = linalg::Dot(GetComm(), vv, X[j])` `:568`; `else { rr2.resize(0); }` `:572-574`; `return std::sqrt(std::abs(linalg::Dot(GetComm(), rr, rr)) + rr2.squaredNorm())` `:575`. Call sites confirmed exact: `:587` `compute_residual(eig, v, v2, u, u2, A2n)`, `:702` `compute_residual(eig_trial, ...)`. Supporting ranges confirmed in-bounds and as described: `:329-347` (`MatVecMult` = AXPBYPCZ linear-combination), `:606-619` (deflation growth — normalization at `:610-611`, `X.resize(k+1)` at `:614`, `X[k]=v` `:615`, `H` updates `:616-618`, `k++` `:619`), `:294-302` (block-structure comment `[v, v2]`), `:354-362` (Jarlebring–Koskela–Mele 2018 + Effenberger 2013 + SLEPc-NEP minimality index 1). In-book refs confirmed: `apply_nonlinear_pencil.md:98` (firm-on-positive-structure status — verbatim escape language), `:109` (the deferred deflation-extension follow-up note "the deflation extension `U(λ)v₂` (560-570) is the deferred follow-up" — exact), `dot.md:43` (conjugation convention), `L2/index.md:54-55` (deflate/gram rough-in rows). `tools/citecheck/` present. No out-of-range or fabricated citations.

**surface-or-evidence — pass.** This is a NEW firm L1 operator (new surface — a `new:book/src/L1/nleps_deflated_residual.md` file), not a refinement of an existing entry, so the refinement-shape clause is satisfied by construction: new operator text + exhaustive positive citation. The firm-not-`partly-constructive` judgment is sound: every constituent is read from a positive source site (`Mult`/`AddMult` at `:559`/`:564`, `fullPivLu().solve` at `:563`, the `Dot` loop at `:565-570`, the `sqrt` norm at `:575`). There is NO sub-part materialized from negative anchors — the `(λI−H)⁻¹` solve that would be the natural `partly-constructive` candidate is read directly from `fullPivLu().solve`, not reconstructed. The single test-coverage caveat (NLEPS has zero dedicated unit tests) is correctly framed as inherited-and-non-gating via the `apply_nonlinear_pencil` firm-on-positive-structure precedent, because all laws are syntactic identities, not convergence-semantics facts.

**rotation-quality — pass.** Not the primary shape for an L1 operator entry (the rotation lives in the future L1>L0 theme, correctly deferred), but the entry's core algebraic claim is a genuine compaction. I verified the load-bearing collapse claim against source: `A` is built once at `:557`; `:559` writes `rr = T(λ)·vv`; `:563` forms `XSvv2 = X·(λI−H)⁻¹·vv₂`; `:564` accumulates `rr += T(λ)·XSvv2` using the SAME `A`. By linearity of the fixed operator `A`, `rr = T(λ)·(vv + X·(λI−H)⁻¹·vv₂)` — so the two-call destination-buffer accumulation collapses to one pure `apply_nonlinear_pencil` of a corrected vector. This is state-hiding + composition compression (destination buffers and the Mult/AddMult split erased into a single applicative form), not a 1:1 rename. The claim is correct and the rotation is real.

**variant-axis-coverage — pass.** The deflation-present axis (`k = 0` un-deflated | `k > 0` deflated) is the source's own `if (k > 0)` branch (`:560` / `:572-574`); the entry covers both — the `k = 0` degeneration to `apply_nonlinear_pencil + nrm2` is law 1 and is exact against the `else { rr2.resize(0); }` branch. The damping-present axis is correctly absorbed into the bound pencil `T` (inherited from `apply_nonlinear_pencil`'s `Maybe C`). The committed-vs-trial purpose distinction (`:587` vs `:702`) is correctly classified as non-structural. The single-algorithm (NLEPS-only) concentration is correctly framed as non-gating via the explicit `apply_nonlinear_pencil` precedent (also NLEPS-only and firm). No hidden branches: I read the full lambda body `:547-576` and every branch (k>0 / else) is represented.

**cross-reference-integrity — pass (build-readiness guard passes).** Fence enumeration on CYCLE.md (`grep -n '\`\`\`'`) returns 10 markers = even parity. The `new:` block spans `:46`→`:194` and encloses two balanced nested `text` fences (`:61-75` Signature, `:94-98` Semantics). Critically, the firm apparatus is INSIDE the fence: `## Signature` (CYCLE.md:59), `## Semantics` (:90), `## Algebraic laws` (:114), `## Status` (:157), `## Evidence` (:170) all fall between fence-open :46 and fence-close :194. The report's own top-level sections (`## Operator content` :215, `## Supporting evidence` :219, `## Open questions` :242) sit OUTSIDE the fence and are pointers/commentary, NOT the chapter body — this is the inverse of the cycle-019 fence-truncation defect (`firm-chapter-body-authored-outside-proposed-changes-fence`). Live links all resolve on disk: `apply_nonlinear_pencil.md`, `dot.md`, `nrm2.md`, `ksp_solve.md`, `eigsolve.md`, `apply_linop.md` (transitively via `nrm2`), `../L0/eigensolver-wrapper.md`. Forward-refs to not-on-disk slugs (`deflate`, `gram`, `lu_solve`) are correctly plain-text/inline-code, never live links — no `linkcheck2` break. Edit anchors confirmed: SUMMARY.md `:70` is the `apply_nonlinear_pencil` entry; L1/index.md `:29` reads "**Firm (13)** — ... and the nonlinear-pencil interior atom:" (count-bump target correctly identified). The most load-bearing semantic cross-check — the conjugation of the coordinate residual — resolves correctly and consistently with the established artifact convention (see Issue 1 for a prose-wording nuance that does not affect correctness): source `linalg::Dot(comm, x, y) = yᴴ x` (per the `vector.hpp:246` header comment "Calculate the parallel inner product yᴴ x" and the `vector.cpp:263-266` method `x.Dot(y) = x·conj(y)`), so `linalg::Dot(GetComm(), vv, X[j]) = X[j]ᴴ vv`, exactly the entry's claim; the `L2/index.md:50` `inner_product` row independently pins "Palace's free-function `Dot(comm,x,y) = yᴴ x` conjugates arg-2, the deliberate L1 re-order", corroborating both the source reading and the entry's `r₂ = Xᴴ·vv`.

**edge-label-fidelity — pass.** This is an L1 operator entry, not a lowering-theme edge; no `L_{n+1}→L_n` edge label is carried. The "Downward to L0" / future-L1>L0-theme discussion correctly defers the rotation narration rather than asserting an edge it does not author. Not applicable to this report-kind; no mismatch possible.

**plan-kind-consistency — pass.** Declared kind is `firm` L1 operator. Content shape matches: a complete chapter (one-line + Context + Signature with bunsen-style named-axes shape contract + 5-point Semantics + 5 holding laws / 3 explicit non-laws + Dependencies + Variant axes + Status + L1-vs-L0 + Evidence), no rough-in placeholders inside the firm body. The single not-yet-firm dependency (`lu_solve`) is correctly handled as a plain-text leaf whose absence gates only a dependency-name's link precision, not the operator's firmness — consistent with the firm declaration. No mis-classification.

**skill-uptake-survey — pass.** The report's §Supporting evidence states the entry's citations were self-verified via `read_range` + `tools/citecheck/citecheck.py` (regex anchors for pinpoint lines). The shape (citation-heavy firm harvest) implies `verify-citation-range`; the report references the citecheck tooling invocation explicitly. Pure presence check — telemetry surfaced, non-blocking.

### Issues found

1. **Conjugation-explanation wording oscillates between "arg-1-conjugated" and "arg-2-conjugating" for the same call — clarity, low severity.** (`book/src/L1/nleps_deflated_residual.md` §Semantics point 3, CYCLE.md:108; vs §Evidence `:568` entry, CYCLE.md:181; vs §Dependencies `dot` entry, CYCLE.md:137.) Semantics point 3 explains `r₂(j) = X[j]ᴴ vv` by saying `linalg::Dot(GetComm(), vv, X[j])` has a "free-function **arg-2-conjugating** order", while the Evidence and Dependencies entries describe the same call as "arg-1-conjugated per `book/src/L1/dot.md:43`". Both statements are individually correct under different framings — the C++ free-function `linalg::Dot(comm, x, y) = yᴴ x` conjugates its *second* C++ argument (here `X[j]`), and the L1 `dot` convention `⟨x,y⟩ = xᴴ y` names the conjugated argument *first* — and they converge on the same correct value `X[j]ᴴ vv`. But using "arg-1-conjugated" and "arg-2-conjugating" within the same entry for the identical source call, without naming which framing (C++ free-function order vs L1-convention order) each refers to, is a reader trap on the single most subtle point of the operator. The fix is a half-sentence disambiguation (e.g. "C++ free-function arg-2 = `X[j]`, conjugated, which is the L1-convention arg-1"). Numerically nothing is wrong; this is presentation only.

2. **`linear_combination` is referenced as plain-text though `book/src/L2/linear_combination.md` exists on disk — missed live-link opportunity, very low severity.** (`book/src/L1/nleps_deflated_residual.md` §Dependencies, CYCLE.md:139; §Supporting-evidence rationale, CYCLE.md:236.) The entry keeps `linear_combination` plain-text on the stated rationale that it is "an L2 operator, cited upward for context per high→low discipline" and groups it with the genuinely-absent `deflate`/`gram`/`lu_solve`. But unlike those three, `book/src/L2/linear_combination.md` is present on disk (verified), so a live link would resolve and not break `linkcheck2`. The plain-text choice is defensible under the high→low "don't live-link downward from L1 to L2" reading, so this is not a defect — but the §Supporting-evidence sentence implicitly lumps `linear_combination` with the not-on-disk forward-refs, which could mislead the integrator into thinking the file is absent. Worth a one-word correction (the file exists; the plain-text choice is a discipline call, not a missing-anchor necessity) or an explicit note that the plain-text is deliberate-despite-existence.

3. **`else` branch line attribution `:572-574` is slightly loose — cosmetic, negligible severity.** (`book/src/L1/nleps_deflated_residual.md` §Semantics point 5 + law 1 + Evidence, CYCLE.md:112/118/182.) The source `else { rr2.resize(0); }` occupies `:571-574` (the `else` at `:571`, brace/body `:572-574`); the entry cites `:572-574` for the branch and `:560` for the guard. The `:560` guard and the `rr2.resize(0)` statement are exact; only the `else`-keyword line is just outside the cited range. The cited range still contains the load-bearing statement (`rr2.resize(0)`), so the claim is supported — this is a one-line boundary slack, not a citation-validity failure.

---

## Repair

All 8 critic checks were `pass`; the three findings are non-blocking (clarity / very-low / cosmetic). All three were mechanically/surgically repairable within repair authority — no substantive authoring required, no content decisions. The book artifact was NOT mutated; only the report's CYCLE.md (pre-integration repair authority) and this META.md repair section were edited.

### Fixes attempted

1. **Finding 1 — conjugation-explanation wording oscillates between "arg-2-conjugating" and "arg-1-conjugated" for the identical `:568` call.**
   - **Decision**: repaired (maps to the critic's `variant-axis-coverage`/`cross-reference-integrity` checks — the conjugation convention is the load-bearing semantic cross-check; recorded under both).
   - **Action**: surgical half-sentence disambiguation in CYCLE.md §Semantics point 3 (the firm chapter body, `new:book/src/L1/nleps_deflated_residual.md` fence). Rewrote the point's lead-in to "the basis vector is the conjugated argument" and added an explicit two-framing label: under the C++ free-function order `linalg::Dot(comm, x, y) = yᴴ x` the **second** C++ argument (`X[j]`, "C++ arg-2") is conjugated, and that same operand is the **first** argument of the L1 `dot` convention `⟨x,y⟩ = xᴴ y` ("L1 arg-1-conjugated") — both descriptions name the same conjugated operand `X[j]`. The Evidence (`:568`) and Dependencies (`dot`) entries retain "arg-1-conjugated per `dot.md:43`", now unambiguous because point 3 labels both framings. No numerical claim changed (the value `X[j]ᴴ vv` was already correct and the critic independently confirmed it).

2. **Finding 2 — `linear_combination` referenced plain-text though `book/src/L2/linear_combination.md` exists on disk; §Supporting-evidence prose risked implying the file is missing.**
   - **Decision**: repaired (`cross-reference-integrity`). Repairer judgment per the instruction: verified the file exists (23 KB on disk) AND that the chapter-body reference should be a live link.
   - **Verification**: `book/src/L2/linear_combination.md` confirmed present; `deflate.md`/`gram.md`/`lu_solve.md` confirmed absent (those stay plain-text, correctly). Surveyed the artifact convention: other firm L1 entries (`ksp_solve.md`, `chebyshev-smoother.md`, `orthogonalize.md`) **already live-link upward to existing L2 chapters** (`[\`L2/krylov-step\`](../L2/krylov-step.md)`, `[\`chebyshev-iteration\`](../L2/chebyshev-iteration.md)`). The high→low discipline governs how *semantics are defined* (in-layer vocabulary), not whether an upward *cross-reference link* is live. The report's rationale conflated the two; the artifact precedent is decisive.
   - **Action**: upgraded `linear_combination` to a live link `[\`linear_combination\`](../L2/linear_combination.md)` at the canonical dependency-declaration site (§Dependencies, firm chapter body) and in the `edit:book/src/L1/index.md` dep-map cell. Both resolve from their respective file locations to `book/src/L2/linear_combination.md` (confirmed on disk) — zero dead-link risk; the genuinely-absent `deflate`/`gram`/`lu_solve` forward-refs were left plain-text. Corrected the report-prose (§Supporting evidence, §Operator content) that lumped `linear_combination` with the missing forward-refs, adding the explicit "this one IS on disk → live link" note so the integrator is not misled.

3. **Finding 3 — `else`-branch attribution `:572-574` is one line loose (the `else` keyword is at `:571`).**
   - **Decision**: repaired (`citation-validity`).
   - **Verification**: `palace-codemap read_range palace/linalg/nleps.cpp:559-576` confirmed the exact layout — `else` keyword at `:571`, `{` at `:572`, `rr2.resize(0);` at `:573`, `}` at `:574`. The precise full `else`-branch range is `:571-574`.
   - **Action**: mechanical range correction `:572-574` → `:571-574` at all four CYCLE.md occurrences (§Semantics point 5, §Algebraic-laws law 1, §Evidence entry, §L1-vs-L0). `grep` confirms zero remaining `:572-574` references. The load-bearing `rr2.resize(0)` was already inside the old range, so this only tightens the boundary to include the `else` keyword.

### Unrepairable findings

None. All three findings were mechanical/surgical and repaired in place. No follow-up agent required.

## Suggested resolution

`overall_status: ready`. All 8 critic checks passed and all three non-blocking findings were repaired surgically without authoring substantive content. Notes for the integrator:

- Post-repair `grep -c '\`\`\`'` on CYCLE.md = 10 (even fence parity preserved; the firm `new:` block and its two nested `text` fences are intact).
- The `edit:book/src/L1/index.md` dep-map cell now carries a live link `../L2/linear_combination.md`; apply the row as written — the link resolves on disk.
- The "Firm (13)" → "Firm (14)" count bump in `book/src/L1/index.md` (flagged by the producer at CYCLE.md:210-213) remains the integrator's prose call, unchanged by this repair.
- The two genuine forward-references that stay plain-text (`deflate`/`gram` chapter files, `lu_solve`) are correctly handled per `rough-in-forward-reference-must-be-plain-text-not-live-link`; do not promote them to live links until those slugs land on disk.
