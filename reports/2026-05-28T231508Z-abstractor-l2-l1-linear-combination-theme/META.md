---
verifies: ./CYCLE.md
critiqued_at: 2026-05-28T233500Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-28T234500Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: unrepairable
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of L2>L1 theme `linear-combination-fold-specialization`

## Critique

### Checks run

**citation-validity — warning.** The Palace L0 anchors are concrete `(file, start, end)` triples and I re-`read_range`-confirmed the load-bearing ranges directly via `palace-codemap` this invocation: `vector.cpp` real-real `AXPBYPCZ` (the `if (gamma == 0.0) { add(alpha, x, beta, y, z); } else { AXPBY(alpha, x, gamma, z); z.Add(beta, y); }` block) lands exactly as transcribed at CYCLE.md:169-171; `AXPY` (`if (alpha == 1.0) { y += x; } else { y.Add(alpha, x); }`) and `AXPBY` (`add(alpha, x, beta, y, y)`) confirmed at the cited ranges; `vector.hpp` confirms the three free-fn decls and the arity ceiling (the next decl after `AXPBYPCZ` is `Sqrt` — no arity-4 fused kernel); `timeoperator.cpp:217` confirms `AXPBYPCZ(1.0, RHS2, dt, k1, 0.0, k2)` with the `// k2 = rhs2 + dt k1` comment (the γ=0 fall-through witness). The co-located `lowering-verifier` deep-audit independently `read_range`-confirmed the same set (plus `nleps.cpp:343-344`, `romoperator.cpp:188-189`) as **supports**, matching the report's "Self-verified" notes. The one substantive citation-vs-prose mismatch is the "sums all three" overstatement (Issue 1), which I confirmed against BOTH the directly-read source (the `gamma == 0.0` branch is the two-term `add(alpha, x, beta, y, z)` — `γ·z` is not passed) AND the report's own table. Two soft anchors are honestly fenced: the scal-order anchor `vector.cpp:203-227` (`operator*=`) is cited only in the summation table (CYCLE.md:193) as an "analogue" alongside the AXPY range — loose (Issue 4); and the complex overload ranges `:732-744`/`:760-769` carry a verified-delegation-but-upstream-rounding caveat. Warning, not fail: the anchors are real and verified; the lone prose mismatch is the one-word item the repairer will fix.

**surface-or-evidence — pass.** This is a new ADD (a firm L2>L1 lowering theme), not a refinement of an existing operator/theme, so the strict refinement-shaped surface-or-evidence gate does not bind. The theme carries full surface (the arity-dispatch rewrite table CYCLE.md:113-131, the two arity-2 sub-selections, the arity-3→arity-2 fall-through, the summation-order table) backed by positive Palace anchors. Not a pure rotation_claim. Pass.

**rotation-quality — pass.** Genuine structural rotation, not a rename. The L2 form is one variadic fold over an arbitrary-length `[(Scalar, Tensor[N])]` list; the L1 form is a finite closed set of four fixed-arity primitives plus an iterated chain. The theme's content is the fusion-selection rule that collapses the variadic abstraction onto the bounded fixed-arity hardware vocabulary AND exposes a load-bearing-numerical summation-order constraint the abstract fold hides. The L2 form is strictly more abstract (one operator vs four cases + a tail-fold). Direction is correct (more-abstract L2 → more-concrete L1). Pass.

**variant-axis-coverage — pass.** Orthogonal axes: (i) arity (0/1/2/3/≥4), (ii) the arity-2 unit-vs-general second-coefficient sub-axis, (iii) the γ==0 vs γ≠0 specialization within arity 3, (iv) real-vs-complex element type. All are tabulated or explicitly handled: arity fully in CYCLE.md:113-131; arity-2 sub-selection at :146-158; γ zero/nonzero at :160-180 and the summation table :196-197; real/complex at applicability condition 5 (:242-248). The arity-≥4 case is covered and its chunking freedom honestly scoped as value-free / bit-pinned in Open questions. No hidden branches. Pass.

**cross-reference-integrity — warning.** I resolved every `[link]` target on disk this invocation. The four RHS L1 leaves `book/src/L1/{scal,axpy,axpby,axpbypcz}.md` all **EXIST** (confirmed by direct `ls book/src/L1/`), so the RHS terminals resolve cleanly. `book/src/concepts/scalar-promotion.md` (condition 5) and `scaffolding/decisions/axpby-as-primitive.md` (Speculative-L1-operators §) both **EXIST**. The sibling-format precedent `book/src/L2-L1/chebyshev-iteration-fusion.md` and registration targets `book/src/L2-L1/index.md` + `book/src/SUMMARY.md` all exist. The ONE dangling reference is the LHS link `../L2/linear_combination.md` (referenced repeatedly: CYCLE.md:47-49, :65, :276, the abs-path variant :397): `book/src/L2/linear_combination.md` is **MISSING** on disk (confirmed — `book/src/L2/` contains only `chebyshev-iteration.md`, `index.md`, `krylov-step.md`). BOTH the report's own Status/Verified-against notes and the lowering-verifier audit state this file is a **same-cycle harvester-sibling proposed-change not yet on disk** — it strands unless the harvester report (`reports/2026-05-28T231026Z-harvester-linear-combination-L2/`) is integrated together with or before this theme. This is the genuine integration-ordering hazard (Issue 2). Warning rather than fail: it is a single known forward-dependency that both upstream agents already documented, not a typo, and its resolution is an integrator ordering constraint, not an in-report fix.

**edge-label-fidelity — pass.** The scope/frontmatter declares the L2>L1 edge, and the prose narrates that exact edge forward (high→low) throughout: LHS is the L2 variadic `linear_combination` (CYCLE.md:62-78), RHS is the L1 fixed-arity BLAS-1 set (:80-102), the rewrite arrows `⇒` go L2→L1 (:113-131), and every section discusses the L2→L1 lowering. The reverse-direction lifting note is correctly quarantined under Open questions with an explicit "working notes only — NOT in the high→low chapter body" marker (:335-344). No layer-number or direction mismatch. Pass.

**plan-kind-consistency — pass.** Declared `theme`, `status: firm`. Content shape (arity-dispatch lowering rule + summation-order property + algebraic justification + citations) matches `theme`. The firm claim is well-supported for the real-real path (positively anchored, lowering-verifier verdict fully-supported). Two peripheral sub-parts are honestly soft: the ≥4 iterated-chain (inferred from vocabulary; no Palace site combines ≥4 — but witnessed live as the γ=1 two-per-step chain at nleps/romoperator) and the complex same-operand-order condition (upstream/MFEM, not Palace-confirmable). Those are scoped caveats on the periphery, not the core rewrite, so `firm` is defensible; I raise the `partly-constructive` question as a low-severity issue for the integrator to weigh rather than as a kind violation. Pass.

**skill-uptake-survey — pass.** The report DOES reference relevant skill invocation: it cites `verify-citation-range` producer-self-verification discipline (CYCLE.md:282-283) for its L0 anchors and applies the load-bearing-vs-transparent numerical classification per CLAUDE.md (:233-234, :264-266). The lowering-verifier-audit-as-standard-follow-up shape is also named (:329-331). Pure telemetry; uptake is present. Pass.

### Issues found

1. **PROSE OVERSTATEMENT (verified) — CYCLE.md line 200, severity: medium.** The prose reads: "the `γ==0` fused branch sums **all three** contributions in one strided pass, whereas the `γ≠0` branch computes `α·x + γ·z` first and folds `β·y` in afterward." When `γ==0` the third term `γ·z` is dropped, so the branch sums **two** contributions (`α·x + β·y`), not three. I confirmed this directly against source (`palace-codemap read_range` of `palace/linalg/vector.cpp` this invocation): the `if (gamma == 0.0)` branch of the real-real `AXPBYPCZ` is exactly `add(alpha, x, beta, y, z)` — the MFEM 5-arg `add(a, v1, b, v2, vout)` kernel is a TWO-term linear-combine writing `z ← α·x + β·y`; `z`/`gamma` is NOT passed as a third addend. Cross-checked against the report's own internals: (a) the report's transcribed source at CYCLE.md:169 matches the read (`if (gamma == 0.0) { add(alpha, x, beta, y, z); }`); (b) the report's own summation-order TABLE at CYCLE.md:196 correctly says the `γ == 0` row is a "single fused pass `add(α, x, β, y, z)`" (two-term); (c) the report's own prose at CYCLE.md:162-164 says "the `γ·z` term drops." So line 200 is internally inconsistent with lines 169, 196, and 162-164 of the same report. The co-located lowering-verifier independently flagged the identical word against its own `read_range` of `vector.cpp:751`. The TABLE is correct; only the one prose word is wrong. **One-word/one-clause fix:** "sums all three contributions in one strided pass" → "sums its two surviving contributions (`α·x + β·y`) in one strided pass" (the lowering-verifier's Edit 1 at CYCLE-lowering-verifier.md:234-243 proposes exactly this wording, and additionally tightens the comparison framing to "for the same three-term value"). Repairer: apply.

2. **LHS FORWARD-DEPENDENCY / INTEGRATION-ORDER HAZARD — CYCLE.md:47-49, :276, :313, :397; severity: medium (integrator-facing, not a content defect).** The LHS link `../L2/linear_combination.md` (and the abs-path variant at CYCLE.md:397) points at a file the report itself states is "firm (harvested this cycle)" — i.e. a same-cycle harvester-sibling proposed-change. The lowering-verifier confirmed this file is **not yet on disk** (CYCLE-lowering-verifier.md §"Per-citation audit" for that path, and Open-question 1: "the live link strands unless the harvester report is integrated together with (or before) this theme"). The four laws this theme leans on (laws 2/5/6/7 + the IEEE non-law) were verified by the lowering-verifier directly against the harvester report, so the SUBSTANCE is sound; the hazard is purely link-resolution ordering. **Carry-forward for the integrator: apply `reports/2026-05-28T231026Z-harvester-linear-combination-L2/` (the L2 `linear_combination` harvester) together with or BEFORE this theme**, else `../L2/linear_combination.md` is a dangling link in the built book. Not repairable in-report (the fix is integrator sequencing or waiting on the sibling); record only.

3. **COMPLEX-PATH OPERAND-ORDER SUB-CLAIM IS UPSTREAM-ONLY — CYCLE.md:188-189 and applicability condition 5 (:242-248); severity: low.** The summation-order table preamble (:188-189) and condition 5 (:246-248) assert the complex overloads "delegate to MFEM member ops ... with the **same operand order** as the real path." The lowering-verifier confirmed the *delegation* is real (the complex overloads at `vector.cpp:732-744` / `:760-769` call `y.AXPBY(...)` / `z.AXPBYPCZ(...)`) but that the rounding-schedule/operand-order *parity* is internal to MFEM's `ComplexVector` member ops and **not confirmable from Palace source** (CYCLE-lowering-verifier.md Open-question 2 + the two `partially-supports` verified_against rows). Per CLAUDE.md (cite Palace; log upstream as OQ), the bit-faithful summation-order table is fully verified ONLY for the real-real path. The theme largely already scopes this ("real-real path; the complex paths delegate ..."), but the bare "same operand order" sub-claim should carry an explicit upstream-unverified marker (e.g. "(MFEM-internal; not Palace-confirmed)") on condition 5 / the table preamble, OR be demoted to an Open question. Repairer: a marker is a small surgical insert; otherwise record for the integrator.

4. **`scal` SUMMATION-TABLE ANCHOR IS AN "analogue" — CYCLE.md line 193, severity: low.** The `scal(α, x)` table row cites "`vector.cpp:702-712` analogue / `:203-227` (`operator*=`)". The `:702-712` range is the AXPY body (cited verbatim for the axpy row directly below it), so labeling it the scal anchor "analogue" is loose; the load-bearing scal anchor is `operator*=` at `:203-227`. The lowering-verifier did not separately audit `:203-227`. Low severity (scal's single-scaled-pass order is uncontroversial and the `operator*=` anchor is the real one), but the "analogue" pointer could be tightened to cite `:203-227` cleanly as the scal order anchor and drop the AXPY-range "analogue" co-citation.

5. **`partly-constructive` STATUS CANDIDACY (non-blocking status question) — CYCLE.md frontmatter `status: firm` / Status §:318-331; severity: low.** Two sub-parts are soft in the senses above: the arity-≥4 iterated chain is inferred from vocabulary (no single Palace call combines ≥4 terms; it is witnessed only as the live γ=1 two-per-step accumulate chain, which is strong but is a reconstruction of the ≥4 lowering rather than a direct ≥4 site), and the complex operand-order parity is upstream-only (Issue 3). The core real-path arity-1/2/3 rewrite is firmly anchored and lowering-verifier-confirmed. This profile — firm structure with named, citation-fenced caveats on specific peripheral sub-parts — resembles the `partly-constructive` pattern. I am NOT asserting `firm` is wrong (both caveats are peripheral, honestly disclosed in Open questions, and the lowering-verifier's overall verdict is fully-supported), but I surface the question for the integrator: is `firm` correct, or is `partly-constructive` with an explicit promotion condition (anchor a ≥4 Palace site if one ever appears; confirm or scope-out the complex operand order) the more precise status? Lean: `firm` is acceptable given the live γ=1 witnesses; record the question, do not block.

### Cross-check of the lowering-verifier's three flags

(a) **"sums all three" → "sums two" overstatement:** independently confirmed (Issue 1) against the report's own transcribed source line CYCLE.md:169 (`add(alpha, x, beta, y, z)` is a two-term combine) and its own table CYCLE.md:196 — not merely deferred to the verifier. Repairable, one-word.
(b) **LHS forward-dependency stranding:** confirmed and recorded as Issue 2 with the explicit integrator carry-forward (apply the harvester sibling first/together).
(c) **complex same-operand-order is upstream/MFEM-only:** confirmed and recorded as Issue 3 with a suggested marker.

---

## Repair

### Fixes attempted

1. **Finding (Issue 1, citation-validity, medium):** PROSE OVERSTATEMENT at CYCLE.md:200 — "the `γ==0` fused branch sums **all three** contributions in one strided pass" but with `γ==0` the third term `γ·z` is dropped (two-term combine `α·x + β·y`).
   - **Decision:** repaired.
   - **Verification:** `palace-codemap read_range` of `palace/linalg/vector.cpp:745-758` this invocation — the real-real `AXPBYPCZ` `if (gamma == 0.0)` branch is exactly `add(alpha, x, beta, y, z)`, the MFEM 5-arg two-term linear-combine `z ← α·x + β·y`; `γ`/`z` is NOT passed as a third addend. Cross-confirmed against the report's own table (CYCLE.md:196, two-term) and its own prose (CYCLE.md:162-164, "`γ·z` term drops").
   - **Action:** Edit at CYCLE.md §"Summation-order recording" (was line 200): "sums all three contributions in one strided pass" → "sums its two surviving contributions (`α·x + β·y`) in one strided pass (the `γ·z` term is dropped — `add(α, x, β, y, z)` is a two-term combine)". The summation-order TABLE at :196 was already correct and is untouched.

2. **Finding (Issue 2, cross-reference-integrity, medium — integrator-facing):** the LHS link `../L2/linear_combination.md` points at a same-cycle harvester-sibling proposed-change not yet on disk.
   - **Decision:** unrepairable (integrator sequencing, not an in-report content fix). The link is CORRECT post-integration; changing it would be wrong. Recorded below for the integrator.

3. **Finding (Issue 3, citation-validity, low):** complex-path condition 5 / summation-table preamble assert the complex overloads use "the same operand order as the real path" — that parity is MFEM-internal, not Palace-confirmable.
   - **Decision:** repaired.
   - **Verification:** `read_range` of `vector.cpp:732-744` and `:760-769` this invocation confirms the complex overloads call `y.AXPBY(...)` / `z.AXPBYPCZ(...)` (delegation to MFEM `ComplexVector` member ops); the operand-order/rounding-schedule parity is internal to those member ops and not visible in Palace source.
   - **Action:** Two surgical markers added — (a) summation-table preamble (§"Summation-order recording"): "...delegate to MFEM member ops, and their operand-order parity with the real path is MFEM-internal — not Palace-confirmed"; (b) applicability condition 5: "...their operand order is presumed to match the real path but that parity is MFEM-internal (not Palace-confirmed) — bit-faithful summation order is verified only for the real-real path."

4. **Finding (Issue 4, citation-validity, low):** the `scal` summation-table row cites the AXPY range `:702-712` as an "analogue"; the real `scal` anchor is `operator*=` at `vector.cpp:203-227`.
   - **Decision:** repaired.
   - **Verification:** `read_range` of `vector.cpp:702-712` confirms that range is the `AXPY` body (`if (alpha == 1.0) { y += x; } else { y.Add(alpha, x); }`), already cited verbatim for the axpy row directly below; the scal scaled-pass anchor is `operator*=` at `:203-227`.
   - **Action:** Edit at the `scal(α, x)` table row (§"Summation-order recording"): "`vector.cpp:702-712` analogue / `:203-227` (`operator*=`)" → "`vector.cpp:203-227` (`operator*=`)" (drop the loose AXPY-range "analogue" co-citation).

5. **Finding (Issue 5, plan-kind-consistency, low):** `partly-constructive`-vs-`firm` status candidacy.
   - **Decision:** not-needed. The critic leans `firm` acceptable — the arity-1/2/3 real-path rewrite is positively anchored and lowering-verifier-confirmed (verdict fully-supported), and the two soft sub-parts (arity-≥4 iterated chain; complex operand-order) are peripheral, honestly disclosed in Open questions, and the arity-≥4 chain is witnessed live as the `γ=1` two-per-step accumulate (`nleps.cpp:343-344`, `romoperator.cpp:188-189`). `firm` stands. No status change.

### Unrepairable findings

- **Issue 2 (LHS forward-dependency / integration-order hazard).** The link `../L2/linear_combination.md` (and the abs-path variant in the Speculative-operators §) resolves only after the same-cycle harvester sibling lands. This is an integrator sequencing constraint, not an in-report fix — the link is correct as written post-integration. Routed to the integrator (not a follow-up agent): see Suggested resolution. `follow_up_agent: null`.

## Suggested resolution

`overall_status: ready`. The three content-level findings (Issues 1, 3, 4) are repaired surgically; Issue 5 leaves `firm` standing.

**INTEGRATION-ORDERING NOTE (integrator-per-report, load-bearing):** This theme's LHS link `../L2/linear_combination.md` is a same-cycle harvester-sibling proposed-change. **Apply `reports/2026-05-28T231026Z-harvester-linear-combination-L2/` (the L2 `linear_combination` harvester) BEFORE or in the same per-report staging pass as this theme**, so `book/src/L2/linear_combination.md` exists on disk and the link resolves at `cargo make book`. Otherwise this chapter ships a dangling LHS link. The four L2 laws this theme leans on (laws 2/5/6/7 + the IEEE non-law) were verified by the lowering-verifier directly against the harvester report, so the substance is sound — the hazard is purely link-resolution ordering. All four RHS L1 leaves (`book/src/L1/{scal,axpy,axpby,axpbypcz}.md`) and the registration targets (`L2-L1/index.md`, `SUMMARY.md`) already exist on disk.
