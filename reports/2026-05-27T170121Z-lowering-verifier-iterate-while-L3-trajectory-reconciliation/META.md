---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T170121Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-27T170121Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of CYCLE.md (lowering-verifier audit — iterate_while L3 trajectory-accumulation reconciliation)

## Critique

### Checks run

**citation-validity**: pass. Spot-checked four of the load-bearing Palace citations against the source files. (i) `reference/palace/palace/linalg/iterative.hpp:52-55` — confirmed `mutable bool converged; mutable double initial_res, final_res; mutable int final_it;` exactly as cited. (ii) `reference/palace/palace/linalg/iterative.hpp:97-108` — confirmed the four `Get*` accessors `GetConverged`, `GetInitialRes`, `GetFinalRes`, `GetNumIterations` and the `final_res` comment at line 103-104 ("which may be an estimate to the true residual"). (iii) `reference/palace/palace/linalg/iterative.cpp:420-485` — confirmed PCG `for (; it < max_it && !converged; it++)` at 427, the in-loop `res = std::sqrt(std::abs(beta));` at 462, the conditional print under `print_opts.iterations` at 422-426, and the `final_res = res; final_it = it;` capture at 484-485. (iv) `reference/palace/palace/linalg/iterative.cpp:614-705` — confirmed GMRES inner `for (;; j++, it++)` at 615, the `beta = std::abs(s[j + 1])` at 642, the convergence break at 645, and `final_res = beta; final_it = it;` at 703-704. (v) `reference/palace/palace/linalg/ksp.cpp:296-310` — confirmed `BaseKspSolver::Mult` consuming exactly `GetConverged()` (line 301), `GetFinalRes() / GetInitialRes()` (line 306), `GetInitialRes()` (line 306), and `GetNumIterations()` (line 309) — the four-getter consumption pattern is exact. (vi) Internal Palace-whiteroom citations to `book/src/L4/iterate-while.md:28-43` (Signature), `:64-88` (small-step rules), `:123-133` (Law 1), `:180-198` (Lowers to, explicit deferral) all verified in-range and quote-accurate; `:222-232` for "Evidence" is in-range though the strawman-§3.7 anchor lives at 222-224 specifically. (vii) `book/src/L4/iterate-while-with-prev.md:137-147` (Law 2) verified; the cited L3 sketch range `:180-200` correctly shows the trajectory accumulator preserved (`[e₀] ++ trajectory`). (viii) `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:156-167` verified as the §"What the L3 form for iterate_while looks like" subsection with the single-`readout` tail-recursive sketch and no §3.8 citation. (ix) `book/src/concepts/derived-view-hoisting.md:14-19` verified — §"Worked example: CG residual norm" is the §3.8 instantiation as claimed. (x) OQ at `scaffolding/open-questions.md:1227-1239` verified — the cycle-006 framing (lines 1235-1239), the cycle-007 augmentation paragraph (post-1239), and the two candidate resolutions (a)/(b) all match the report's characterization. All citations resolve correctly and support the claims they anchor.

**surface-or-evidence**: pass. This is a lowering-verifier dispatch in audit mode, which the role spec allows to produce evidence + verdict without surface authoring. The CYCLE.md's Change 1 is an OQ-status update (allowed under any-agent-appendable scaffolding writes per CLAUDE.md write-authority partition); Change 2 is a `verified_against:` YAML block append to an existing theme (audit-trail metadata, not new surface); Change 3 is explicitly out-of-authority and deferred to a cycle-008+ lifter dispatch — the report names the proposed substantive edit only "for the lifter's reference, not as an edit applied here" (line 230). The audit does not author new themes, new dep-map rows, or new operator surface. Stays correctly in audit mode.

**rotation-quality**: pass (N/A to audit shape; verdict-quality check substituted). This dispatch does not propose a rotation — it audits an existing rotation's classification of a §3.8-induced collapse. The verdict's structural claim (L4 `[readout]` accumulator collapses to L3 single-readout under Law 1 demand-pruning when the consumer surface materializes only `final_state`-equivalent quantities) is the §3.8 pruning rule applied to a known consumer surface, which is a legitimate state-hiding / equation-driven rewrite — not a renaming, not a 1:1 mapping. The L3 form's "more compact" property holds (no accumulator allocation, no trajectory threading) and the rotation is genuinely consumer-demand-driven rather than algorithmic. The verdict-(b)-ruled-out argument (line 268) correctly identifies why demoting L4 would force a runtime "compute residuals?" flag and defeat the §3.8 generality — this is the correct rotation-quality reasoning even though the audit itself produces no rotation.

**variant-axis-coverage**: pass (N/A to audit shape with explicit-orthogonal-axis caveat). The audit's verdict is about a single property (trajectory collapse under §3.8) that is orthogonal to the three variant axes the firm L4 chapter already catalogues (pure-vs-Solve, extras-vs-no-extras, bootstrap-free-vs-carry-bootstrapped). The proposed new Condition 5 (consumer observes only `final_state`-equivalent quantities) is correctly framed as an applicability condition for the lowering theme rather than as a fourth variant axis on the L4 combinator, which is the right placement — the L4 combinator is invariant under consumer-demand differences; the L4>L3 lowering's *result shape* depends on consumer demand. No hidden branches; the audit explicitly enumerates verdict (a)/(b)/(c)/(d) and rules each out (or in) in §"Open questions / caveats" item 4.

**cross-reference-integrity**: pass. All in-report cross-references resolve. (i) `book/src/L4/iterate-while.md` and `book/src/L4/iterate-while-with-prev.md` both exist and contain the cited Law 1 / Law 2 ranges. (ii) `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` exists and contains the cited §"What the L3 form for iterate_while looks like" subsection at lines 156-167. (iii) `book/src/concepts/derived-view-hoisting.md` exists with the cited §"Worked example: CG residual norm". (iv) The verdict structure (a)/(b)/(c)/(d) is well-formed and exhaustive: (a) promote L3 to trajectory; (b) demote L4 to single-readout; (c) keep L3 single-readout, add §3.8-collapse citation; (d) insufficient evidence. The audit selects (c) and the supporting evidence chain (citations 5-8) directly supports the (c) verdict: citation 5 (PCG loop) and citation 6 (GMRES inner loop) demonstrate no per-iteration accumulator; citation 7 (KSP four-scalar surface) demonstrates the public extraction surface is pre-pruned; citation 8 (`BaseKspSolver::Mult` sole consumer) demonstrates one-and-only consumption pattern uses only the four scalars. The cross-codebase grep evidence (lines 252-258) supports the "sole consumer" claim with one call site each for the four getters in `palace/`. The SLEPc-prefixed disambiguation (lines 257-258) preempts a plausible false-positive on the grep. The OQ-closure framing (Change 1) cross-references the right cycle-007 augmentation text and the right two candidate-resolution branches.

**edge-label-fidelity**: pass. The dispatch's scope is "L4>L3 theme audit — iterate-while L3 trajectory-accumulation reconciliation" and the prose discusses exactly the L4>L3 edge throughout. The L4 form is `book/src/L4/iterate-while.md`'s firm trajectory-carrying signature; the L3 form is the cycle-006 theme's tail-recursive sketch; the rotation under audit is the L4>L3 hop and specifically how the §3.8 pruning rule renders at L3. The audit does not stray into L3>L2 (which is correctly scoped out at §"Open questions / caveats" item 3 — the body-side L3>L2 is the separate `book/src/L3-L2/krylov-step-body-identity.md` theme).

**plan-kind-consistency**: pass. The dispatch is `agent: lowering-verifier` and `status: pending` (i.e., this is the verifier's evidence-and-verdict output, not a `kind: firm` theme entry). The content shape matches: per-citation audit with verdicts, applicability-conditions walkthrough, algebraic-law check, proposed-changes block with explicit out-of-authority demarcation for the substantive patch. The recommendation that the substantive §3.8-citation patch be authored by a cycle-008+ `lifter` dispatch (lines 228-236) matches the lifter role spec exactly: per CLAUDE.md, the lifter "re-anchors a theme to firmed-up vocabulary" — patching `krylov-step-typed-wrapper-dissolution.md` §"What the L3 form for iterate_while looks like" to cite `book/src/L4/iterate-while.md` Law 1 and `book/src/concepts/derived-view-hoisting.md` §"Worked example" is precisely re-anchoring a cycle-006 rough-in theme to the cycle-007-firmed L4 vocabulary. The "low-cost dispatch (single file edit, no new operator promotion, no new theme)" framing matches the lifter's scope discipline. Plan-kind alignment is clean.

**skill-uptake-survey**: warning. The dispatch performed extensive citation-range verification (10 citations against ~6 source files, multiple `Read(offset, limit)` calls plus a cross-codebase grep at lines 252-258) but does not name `verify-citation-range` skill invocations, despite the report's procedural shape matching that skill's intent. The dispatch also performed variant-axis enumeration (the four verdict options (a)/(b)/(c)/(d) plus the new Condition 5) without naming `classify-variant-axis`. The dispatch explicitly notes at item 5 (line 270) that "Codemap MCP tools not used per dispatch instructions" — a deliberate scope-out that is correctly recorded as telemetry. The pattern here is a verifier doing exactly the skill-described work without referencing the skill names; this is the same skill-uptake gap the meta-phase has seen in prior cycles. Telemetry-only (per role spec, skill-uptake-survey is non-blocking).

### Issues found

1. **(Minor) Evidence-range citation `book/src/L4/iterate-while.md:222-232` is broader than necessary.** The actual L0 anchor citations called out in the report's text ("`iterative.cpp:427` (PCG outer loop) and `iterative.cpp:615` (GMRES inner)") live at lines 222-224 specifically; lines 225-232 contain `derived-view-hoisting`-related concept evidence and don't carry the L0-anchor claim. Tightening to `:222-224` would be more precise. Location: CYCLE.md line 32 (Citation 1).

2. **(Minor) Citation 3 quotes the L3 sketch but uses the inner-fence triple-backtick form `~~~` for the embedded snippet** while the rest of the report uses bare triple-backtick fences. Stylistic only — both render correctly in mdBook; no functional issue. Location: CYCLE.md lines 49-54.

3. **(Minor) Change 1's status update names `answered_at: cycle-007`** but per the cycle-counter convention in CLAUDE.md ("the cycle counter does NOT reset at meta-batch boundaries"), the canonical cycle-id for this dispatch's batch (cycle-007 wave-2) is correctly `cycle-007`. No issue — the cycle-id is correct; flagging only to confirm the integrator should not re-derive it from the report's timestamp.

4. **(Minor) The new OQ `iterate-while-log-effect-vs-trajectory-channel` (lines 262) is well-formed and orthogonal to the gap being closed** — it concerns the `Mpi::Print` side-effecting log channel (not modeled by the current `Solve = StateT SimState Identity` monad), which is a return-value-vs-effect-channel distinction independent of the trajectory accumulator's `final_state`-pruning. The OQ frames a future-question about extending `Solve` to a richer effect representation (e.g., `RWST` with a `DList LogEntry` writer channel). The orthogonality is correctly noted ("Not blocking on this cycle's resolution; the current single-readout L3 rendering is independently correct for Palace's *return-value* surface"). However, the OQ is filed inline in §"Open questions / caveats" rather than as a YAML-formatted block ready for direct lift into `scaffolding/open-questions.md`. The integrator-per-report will need to convert it to the canonical OQ frame (slug, opened_at, opened_by, status, relates_to) before appending. Not a fail — just a formatting note for downstream consumption. Location: CYCLE.md lines 262.

5. **(Minor) Change 2's `verified_against:` block is appended at end-of-file** but the cycle-006 theme already has frontmatter and structured sections; the integrator should confirm whether the existing theme convention places `verified_against:` in frontmatter (typical) or as a trailing block (less typical). Other cycle-007 lowering-verifier outputs may establish the precedent. Not a fail — flagging for integrator-per-report awareness. Location: CYCLE.md lines 184-225.

6. **(Skill-uptake telemetry — non-blocking)** The dispatch performed `verify-citation-range`-shaped work across 10 citations without naming the skill in its procedure. This is the same skill-uptake gap surfaced in earlier critic reports. No action required from repairer; flagging for meta-phase aggregate-evidence consumption.

## Repair

### Fixes attempted

- **Finding 1 — Evidence-range citation `:222-232` overly broad; should tighten to `:222-224`.**
  - **Decision**: repaired.
  - **Action**: CYCLE.md line 32 (Citation 1) — replaced `:222-232 (Evidence, Palace L0 citations)` with `:222-224 (Evidence, Palace L0 anchor citations for the canonical iteration shapes — tightened from :222-232 per critic Finding 1; lines 225-232 carry adjacent concept-evidence not the L0-anchor claim)`. Mechanical citation-range tightening per repair authority ("Citation line range off by a small offset").

- **Finding 2 — Inner-fence stylistic mismatch (`~~~` vs triple-backtick) at CYCLE.md lines 49-54.**
  - **Decision**: not-needed.
  - **Rationale**: critic explicitly classifies as "stylistic only — both render correctly in mdBook; no functional issue." The `~~~` fenced form is intentional here because the surrounding container is already a triple-backtick `text` fence containing the L3 sketch quote — `~~~` is the standard markdown convention for nesting fences without escape contortion. No edit warranted.

- **Finding 3 — `answered_at: cycle-007` confirmation note (CYCLE.md line 171).**
  - **Decision**: not-needed.
  - **Rationale**: critic explicitly notes "No issue — the cycle-id is correct; flagging only to confirm the integrator should not re-derive it from the report's timestamp." This is a flag-to-integrator awareness note, not a finding requiring repair. The CLAUDE.md cycle-counter convention is respected.

- **Finding 4 — New OQ `iterate-while-log-effect-vs-trajectory-channel` filed inline rather than as canonical YAML frame.**
  - **Decision**: repaired.
  - **Action**: CYCLE.md §"Open questions / caveats" item 1 — appended a canonical YAML frame (`slug`, `opened_at`, `opened_by`, `status`, `relates_to`) and a separable question-text block matching the cycle-006 / cycle-007 OQ conventions visible in `scaffolding/open-questions.md:1227-1239`. The frame is now in the lift-ready format the integrator-per-report can copy-paste directly into the open-questions ledger. Mechanical formatting fix per repair authority (append-by-slug hint where slug is obvious; canonical-frame normalization).

- **Finding 5 — `verified_against:` block placement (end-of-file vs frontmatter).**
  - **Decision**: not-needed.
  - **Rationale**: checked precedent. `book/src/L1-L0/axpby-mutation-rotation.md:173` and `book/src/L1-L0/apply-linop-mutation-rotation.md:353` both place `verified_against:` as a trailing YAML block at end-of-file (not in frontmatter). The cycle-006 wave-2 theme is structurally aligned with these L1-L0 themes (rough-in lowering with appended audit-trail). The CYCLE.md's Change 2 proposal correctly follows the established pattern. The third precedent (`book/src/L1-L0/bicgstab-iteration.md:64-80`) wraps the trailing YAML in a `## Verified-against` H2 section — a stylistic variant that is also acceptable. No edit warranted; the integrator can apply Change 2 as-proposed.

- **Finding 6 — Skill-uptake telemetry (verify-citation-range / classify-variant-axis not named).**
  - **Decision**: not-needed.
  - **Rationale**: critic explicitly notes "No action required from repairer; flagging for meta-phase aggregate-evidence consumption." Telemetry-only finding; surfaces to meta-phase, not to repair-action.

### Unrepairable findings

None. All six findings either repaired (Finding 1, Finding 4) or not-needed (Findings 2, 3, 5, 6 per critic's own framing or established precedent).

## Suggested resolution

`overall_status: ready`. All 7 critic checks pass (the one `warning` is `skill-uptake-survey` and is non-blocking per role spec). Two mechanical repairs applied to CYCLE.md (citation-range tightening, OQ canonical-frame normalization); four findings classified as not-needed per critic's own framing or established precedent.

Notes for the integrator-per-report:
- CYCLE.md's Change 1 (OQ closure for `iterate-while-l3-rendering-trajectory-accumulation-gap`) is append-only into `scaffolding/open-questions.md` at line ~1239, after the existing "Cycle-007 update" paragraph; status flip from `open` to `closed` per the proposed YAML block. The cycle-id is `cycle-007` (confirmed; do not re-derive from timestamp).
- CYCLE.md's Change 2 (`verified_against:` block appended to `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`) follows the L1-L0 lowering-theme precedent — trailing YAML block at end-of-file. Optional stylistic variant: wrap in `## Verified-against` H2 section per `bicgstab-iteration.md` precedent.
- New OQ `iterate-while-log-effect-vs-trajectory-channel` (filed in CYCLE.md §"Open questions / caveats" item 1, now in canonical YAML frame after repair) should be appended to `scaffolding/open-questions.md` as a standalone entry; the repair-added frame is lift-ready.
- CYCLE.md's Change 3 (substantive patch to `krylov-step-typed-wrapper-dissolution.md` §"What the L3 form for iterate_while looks like") is explicitly out-of-authority for the lowering-verifier role; should be routed to a cycle-008+ `lifter` dispatch per the report's own framing. The integrator-per-report should NOT apply Change 3 in this cycle.
