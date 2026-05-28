---
verifies: ../REPORT.md
critiqued_at: 2026-05-28T151200Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-28T154500Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: unrepairable
  skill-uptake-survey: not-needed
overall_status: needs-revision
follow_up_agent: integrator-per-report
---

# META: verification of "Formalize divfree-projector at L1"

## Critique

### Checks run

**citation-validity — warning.** Verified every Palace source citation against `palace-codemap` `read_range`. The structural claims hold: the class doc (`divfree.hpp:28-31`, "Gᵀ M x = 0, … G … columns spanning the nullspace of the curl-curl operator") is quoted verbatim and correct; the `Mult(y)` / `Mult(x,y)=y=x;Mult(y)` declarations (`divfree.hpp:63-72`) are correct; the four-step apply (`divfree.cpp:155-186`) is faithfully transcribed (WeakDiv→Mult step1, `SetSubVector(...,0.0)` step2 at :173, `ksp->Mult(rhs,psi)` step3 at :175, `Grad->AddMult(psi,y,1.0)` additive correction step4); the construction range (`divfree.cpp:43-152`) and the empty-bdr MPI pin are correct; ALL 13 driver call sites (`eigensolver.cpp:262`, `arpack.cpp:586/752/766/783/791`, `slepc.cpp:1870/1961/1970/1982/1991/2088/2163`) resolve exactly. The slice cross-refs (`spec/slices/divfree.md`, 413 lines; ranges :13-15, :24-100, :135-140, :142-216 all in-range) check out. **However, several fine-grained single-line citations have drifted by 1-3 lines** (see Issues). None of the drifts changes a claim — each cited symbol/comment exists at very nearly the cited location — so this is a `warning`, not `fail`.

**surface-or-evidence — pass.** This is a new-operator harvest (promotion of a slice-resident form to a firm L1 entry), not a refinement of an existing operator/theme. It creates new surface (`book/src/L1/divfree-projector.md`) and a dep-map row; every claim is anchored to a positive source site. Refinement-shape checks do not apply.

**rotation-quality — pass.** The L1 form genuinely rotates the L0 mutation impedance: the in-place `Mult(VecType &y)` (destination buffer + threaded `psi`/`rhs` scratch members + construction-bound operator reads) is re-expressed as a single pure function `divfree_project(P, y) -> Field[N_nd]` over an opaque constructed-operator value, with the scratch buffers and destination binding hidden inside `P` / deferred to the L1>L0 lowering. This is state-hiding + threaded-state compression, not a rename or 1:1 mapping. The constructed-operator-gate framing (P as opaque structured arg, like `ksp_solve`/`eigsolve`/`chebyshev-smoother`) is the correct more-abstract L1 representation.

**variant-axis-coverage — pass.** Two variant axes are present and both addressed: (1) the `VecType ∈ {Vector, ComplexVector}` template axis (`divfree.cpp:189-190`) is covered — absorbed by polymorphism over field element type, with the block-diagonal real/imag action stated as a law and cited to the `if constexpr` branches; (2) the in-place `Mult(y)` vs out-of-place `Mult(x,y)` axis is covered — explicitly collapsed to the single pure function with the out-of-place form noted as `y=x; Mult(y)` (no silent aliasing). The empty-boundary-pin branch (`bdr_eff` synthetic single-dof vs user-supplied) is also handled and scoped to construction. No hidden branches.

**cross-reference-integrity — pass.** All `[link]` targets resolve: L1 deps `ksp_solve.md`, `apply_linop.md`, `axpy.md`, `eigsolve.md`, `chebyshev-smoother.md` all exist under `book/src/L1/`; concept refs `set_subvector_zero.md`, `constructed-operator-factory.md` exist under `book/src/concepts/`. The index.md dep-map edit anchors on the existing `chebyshev-smoother` row (line 73) verbatim and appends cleanly. The "Firm (10)→(11)" prose bump is correctly deferred to layer-intro-author (authority partition respected). Slice downstream-citer claims (`eigsolve.md`'s `DivFreeSolver[ComplexVector]` field, the three concept pages, `L0/eigensolver-wrapper`) match the slice header's own citer list.

**edge-label-fidelity — pass.** Not applicable in the strict sense (this is an L1 operator entry, not a lowering-theme edge). The entry consistently labels the future lowering as `L1-L0/divfree-projector-mutation-rotation` and the prose discusses that exact L1→L0 direction; no edge-label/prose mismatch.

**plan-kind-consistency — warning→pass (see note).** The declared kind is `firm`, and the content shape is firm: full signature with named-axis shape contract, four-step semantics, five algebraic laws + two load-bearing non-laws, dependencies, evidence. No rough-in placeholders. The firm-on-precedent justification (no dedicated `test-divfree.cpp`, leaning on the `chebyshev-smoother` precedent and distinguishing the `eigsolve` rough-in) is internally coherent and matches an established cycle-012 pattern. I mark this `pass` — but flag a substantive tension below (the "subtract" comment vs additive code) that bears on whether `firm` is the right status vs `partly-constructive`; that is a content judgment for the repairer/integrator, not a kind-misclassification.

**skill-uptake-survey — warning.** The report's shape implies several skills should have been invoked and names them only as future recommendations: `verify-citation-range` (recommended for the WeakDiv sign OQ, but NOT applied to the report's own 30+ citations despite the off-by-1/2/3 drifts that a `verify-citation-range` pass would have caught); `classify-variant-axis` (the variant-axis section is well-formed but the skill is not referenced); `phase-1-slice-reduction-audit` (correctly recommended as a follow-up, appropriately deferred). Pure telemetry — non-blocking — but the citation drift is direct evidence that a self-applied `verify-citation-range` pass was skipped.

### Issues found

1. **[citation drift, low severity] Fine-grained single-line citations off by 1-3 lines** — `book/src/L1/divfree-projector.md` Signature + Evidence sections.
   - `MixedVectorWeakDivergenceIntegrator` cited at `divfree.cpp:114` (Signature `P.WeakDiv` bullet, Algebraic-laws sign non-law, OQ); actual line is **113**.
   - `Grad = &nd_fespace.GetDiscreteInterpolator(...)` cited at `divfree.cpp:119` (Signature `P.Grad` bullet, Evidence); actual line is **117**.
   - `// The system matrix for the projection is real and SPD.` cited at `divfree.cpp:120` (Signature `P.M`, M-orthogonality law, Status, Evidence); actual line is **119**.
   - WeakDiv assembly block cited at `divfree.cpp:112-118` (Evidence); actual is **111-116**.
   - `ksp` rel-tol/abs-tol cited at `divfree.cpp:121-149` (range, OK) but the idempotence law cites the abs-tol=epsilon at `divfree.cpp:144-146`; actual `SetAbsTol(...epsilon())` is at line **141** (`SetRelTol` at 140, `SetMaxIter` at 142).
   - Step-4 real-branch `Grad->AddMult(ψ, y, 1.0)` cited in "Supporting evidence" at `:180/:184`; the real-branch AddMult is at **185** (:184 is the `{` of the else block; :180-181 are the complex-branch AddMults). The :178-184 range cited in Semantics step 4 omits the real-branch line (185).
   None of these alters a claim — each cited symbol exists at very nearly the stated location — but they are imprecise. Candidate for mechanical repair (bump the line numbers).

2. **[contradiction-resolution incompleteness, MEDIUM severity] A third "irrotational / subtract" anchor inside the transcribed apply is unaddressed** — `book/src/L1/divfree-projector.md` Open questions §"Header-comment vs class-doc characterization (NEW)" and Semantics step 4.
   The report frames the contradiction as a *two-way* split: header `Mult` comment (`divfree.hpp:63-66`, "irrotational portion … ∇×y=0") vs class doc (`divfree.hpp:28-31`, divergence-free `Gᵀ M x = 0`), adopting the class-doc reading and labeling the header comment "stale or mislabeled." But there is a **third in-`.cpp` comment the report transcribed but did not cite in the contradiction**: `divfree.cpp:177` reads `// Compute the irrotational portion of y and subtract.` This is the strongest in-code statement of intent, and it is doubly significant:
   - It corroborates the report's class-doc reading (it says **subtract** the irrotational part → the *result* is divergence-free), which actually strengthens the report's conclusion. The report leaves this supporting evidence on the table.
   - It simultaneously contradicts the literal code, which **adds** (`Grad->AddMult(psi, y, 1.0)`, `+1.0`). So the local code, its own comment, the header comment, and the class doc form a *three-way* tension, not two-way.
   The report's contradiction OQ and its separate WeakDiv-sign OQ are in fact the SAME tension and the report does not connect them: the additive `+1.0` is only consistent with "subtract the irrotational portion / produce divergence-free output" IF `WeakDiv` carries the negating sign so that `Grad·ψ = −(irrotational part of y)`. The soundness of the report's class-doc adoption therefore *depends on* the unverified WeakDiv-sign reading — but the report presents the two OQs as independent and presents the class-doc adoption as settled. This is a content/evidence-completeness gap, not a mechanical one. Recommend: cite `divfree.cpp:177` in the contradiction OQ; note it corroborates the divergence-free reading; and explicitly state that the additive-sign correctness (idempotence + the "subtract" intent) is contingent on the WeakDiv-sign OQ, linking the two carried OQs.

3. **[idempotence-derivation gap, LOW-MEDIUM severity] The `P∘P=P` derivation assumes the conclusion it shares with the sign OQ** — `book/src/L1/divfree-projector.md` Algebraic-laws §Idempotence.
   The derivation is: by the defining condition `Gᵀ M (P·y)=0`, `P·y` is divergence-free, so `WeakDiv·(P·y)=0` (step 1 yields zero residual), so `Grad·ψ=0`, so `P·(P·y)=P·y`. The step "`P·y` is divergence-free ⟹ `WeakDiv·(P·y)=0`" silently identifies the `WeakDiv` operator with the `Gᵀ M` of the defining condition (i.e. assumes `WeakDiv = Gᵀ M` up to the sign). That identification IS the sign-convention reading. The idempotence law is thus only as firm as the sign OQ — yet it is listed among the laws that justify the `firm` status with no caveat tying it to the sign OQ. The derivation also rests on the defining condition `Gᵀ M (P·y)=0` being *exactly* the property the projector establishes; that is sourced (`divfree.hpp:28-31`) but is the documented intent, not an independently verified algebraic identity of the four-step body. Recommend a one-line caveat in the idempotence law cross-linking the WeakDiv-sign OQ (the report does this for the modulo-ksp-tolerance caveat but not for the structural `WeakDiv≈Gᵀ M` assumption).

4. **[status-vs-evidence tension, MEDIUM severity — flag, not a defect to repair] `firm` may understate the carried caveats** — `book/src/L1/divfree-projector.md` Status.
   The entry carries (a) an unverified WeakDiv-sign reading that, per Issues 2-3, the idempotence law and the divergence-free output characterization both depend on; (b) a documented header/cpp-comment contradiction it resolves by judgment rather than positive source; (c) no dedicated test. The cycle-012 `partly-constructive` first-class status exists precisely for "firm in structural decomposition but carrying a named, citation-backed caveat on a sub-part with an explicit promotion condition." The sign-convention non-law arguably fits that mold (negative/absent positive anchor for the integrator sign + a stated promotion condition: a `verify-citation-range` pass on `MixedVectorWeakDivergenceIntegrator`). The report explicitly argues AGAINST `partly-constructive` ("a property of the constructed operators, not reconstructed sub-parts"), which is a defensible reading — the *structure* is fully read. I am not asserting the report is wrong; I am flagging that the `firm` vs `partly-constructive` call is load-bearing and currently rests on the sign OQ being below-L0-scope. This is an integrator-level status adjudication, surfaced here, not a mechanical repair.

5. **[skill-uptake, LOW severity] `verify-citation-range` not self-applied** — whole report. The off-by-1/2/3 drifts in Issue 1 are exactly what a self-applied `verify-citation-range` pass catches. The report recommends the skill for the *future* WeakDiv-sign verification but did not run it on its own 30+ citations. Telemetry only.

## Repair

### Fixes attempted

- **Finding (Issue 1): citation drift — fine-grained single-line citations off by 1-3 lines.**
  - **Decision**: repaired
  - **Action**: Verified each drifted citation against `palace-codemap` `read_range`, then corrected in `CYCLE.md` (the `book/src/L1/divfree-projector.md` proposed-changes block + Supporting evidence):
    - `MixedVectorWeakDivergenceIntegrator` `:114 → :113` (Signature `P.WeakDiv` bullet, Algebraic-laws sign non-law, OQ — 3 sites).
    - `Grad = …GetDiscreteInterpolator` `:119 → :117` (Signature `P.Grad` bullet, Evidence — 2 sites).
    - `// … real and SPD.` `:120 → :119` (Signature `P.M`, M-orthogonality law, Status, Evidence, Supporting evidence — 5 sites).
    - WeakDiv assembly block `:112-118 → :111-116` (Evidence).
    - abs-tol=epsilon `:144-146 → :140-142` with `:141` called out for the `SetAbsTol` line (Idempotence law).
    - Step-4 gradient correction range `:178-184 → :177-186`, with complex Re/Im branches at `:180-181` and the real branch at `:185` (Semantics step 4, contradiction OQ code-cite, Supporting evidence).
  - **Rationale**: pure line-offset corrections; each cited symbol/comment exists at the corrected line. No claim changed.

- **Finding (Issue 2): three-way `irrotational/subtract` contradiction — the in-apply comment `divfree.cpp:177` is unaddressed.**
  - **Decision**: repaired (partial, per dispatch guidance)
  - **Action**: Surgically ADDED a "Third in-`.cpp` anchor (added on repair)" paragraph to the §"Header-comment vs class-doc characterization" OQ in `CYCLE.md`. Cites `palace/linalg/divfree.cpp:177` (`// Compute the irrotational portion of y and subtract.`), notes it (i) corroborates the divergence-free class-doc reading and (ii) makes the tension three-way and contingent on the additive `+1.0`, and explicitly LINKS it to the existing `divfree-weakdiv-sign-convention-l0-verify` OQ and the already-flagged `lowering-verifier` follow-up. Did NOT resolve the WeakDiv sign question — that is the verifier's job.
  - **Rationale**: adding a missing citation that the transcribed source trivially supports + linking two carried OQs is mechanical/surgical; resolving the sign is out of scope.

- **Finding (Issue 3): `P∘P=P` derivation assumes the `WeakDiv≈GᵀM` sign reading without a caveat.**
  - **Decision**: repaired
  - **Action**: Appended a one-line "Caveat (added on repair)" to the Idempotence law in `CYCLE.md` stating the derivation step "`P·y` divergence-free ⟹ `WeakDiv·(P·y)=0`" is contingent on the WeakDiv sign-convention OQ and exact only once that OQ confirms `WeakDiv ≈ Gᵀ M`.
  - **Rationale**: a surgical cross-link to an already-carried OQ, mirroring the existing modulo-ksp-tolerance caveat. No new content authored.

- **Finding (Issue 4): `firm` vs `partly-constructive` status tension.**
  - **Decision**: unrepairable (escalate)
  - **Rationale**: per dispatch guidance, this is a load-bearing content judgment, not a mechanical fix. Given the now-explicit sign-OQ contingency carried by both the idempotence law and the divergence-free output characterization (Issues 2-3), the `firm` vs `partly-constructive` call is genuinely load-bearing and exceeds repair authority. The repairer does NOT unilaterally downgrade the status. Escalated to the integrator for status adjudication; this drives `overall_status: needs-revision`.

- **Finding (Issue 5): `verify-citation-range` not self-applied (skill-uptake telemetry).**
  - **Decision**: not-needed
  - **Rationale**: pure telemetry, non-blocking. The concrete consequence (the citation drifts) is fully repaired under Issue 1; nothing further to fix in the report.

### Unrepairable findings

- **Issue 4 — `firm` vs `partly-constructive` status adjudication.** Route to the **integrator** (`integrator-per-report` → escalate at finalize if needed). The structural decomposition is fully read (supports `firm`), but the additive-sign correctness, the idempotence law, and the divergence-free output characterization are now explicitly contingent on the unverified `divfree-weakdiv-sign-convention-l0-verify` OQ, whose promotion condition (a `verify-citation-range` / `lowering-verifier` pass on `MixedVectorWeakDivergenceIntegrator`) matches the cycle-012 `partly-constructive` mold. The integrator should decide whether to (a) keep `firm` (structure-is-read reading the report argues) or (b) downgrade to `partly-constructive` with the sign sub-part named + the existing promotion condition. The repair-phase edits (Issues 2-3) make either choice defensible by surfacing the contingency in-line; the call itself is content-level.

## Suggested resolution

`needs-revision`. The mechanical citation drifts (Issue 1) and the two surgical caveat/cross-link additions (Issues 2-3) are applied and leave the report internally consistent and citation-clean. The single open item is the **status adjudication** (Issue 4): the integrator should decide `firm` vs `partly-constructive` for `book/src/L1/divfree-projector.md` in light of the now-explicit WeakDiv-sign contingency, and — if it adopts `partly-constructive` — name the sign sub-part and carry the existing promotion condition (verify the `MixedVectorWeakDivergenceIntegrator` sign). Either way the entry is applyable; this is a status-field decision, not a content-blocker, so the report is not `reject`. The `divfree-weakdiv-sign-convention-l0-verify` OQ and the linked `lowering-verifier` follow-up for the future L1>L0 theme should be promoted as carried.
