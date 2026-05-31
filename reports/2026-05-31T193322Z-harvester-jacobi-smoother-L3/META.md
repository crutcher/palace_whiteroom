---
verifies: ../CYCLE.md
critiqued_at: 2026-05-31T193930Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-31T194530Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of harvester jacobi-smoother L3 backfill

## Critique

### Checks run

**citation-validity — pass.** `python3 tools/citecheck/citecheck.py --scan` on the report returned `21 ok, 0 failing (21 citations checked)`. I independently re-ran `--anchor` on every load-bearing pinpoint against the on-disk source (not codemap): the key witness `Y[i] = DI[i] * X[i]` at `palace/linalg/jacobi.cpp:38` confirmed `[ok]` (anchor at line 38); `Apply(dinv, x, y)` at `:99-104` confirmed at line 103; `!this->initial_guess` precondition at `:102` confirmed; `MultTranspose ... { Mult(x, y); }` at `jacobi.hpp:43` confirmed; `JACOBI` consumer at `ksp.cpp:198-200` confirmed at line 198. I also read the source ranges directly: the setup chain `op.AssembleDiagonal(dinv); dinv.Reciprocal();` (`:79-80`), the `omega == 0.0` estimated-damping block (`:84-89`, `GetLambdaMax`), and the `if (omega != 1.0) { dinv *= omega; }` ω-fold (`:90-93`, the `dinv *= omega;` at `:92`) all match the report's law-3/law-4/law-5 claims exactly. The complex `Apply<Transpose>` branch (`:41-70`) confirms the `Transpose=true` branch (`:61-69`) computes the conjugate-`dinv` apply and is dead code under the `MultTranspose -> Mult` wiring — the report's "dead-code Hermitian non-realisation" non-law is faithful to source. Note: the report renames the opaque setup sub-action `GetLambdaMax` as `spectrum_estimate` for L3/L1 vocabulary; acceptable (it is named as opaque/out-of-scope). No YAML `verified_against:` block is emitted by this report (harvester, not lowering-verifier), so that sub-check is not applicable. Every factual claim carries an in-range, anchor-confirmed citation.

**surface-or-evidence — pass.** This is not a refinement of an existing operator/theme surface; it authors a NEW L3 chapter (`book/src/L3/jacobi-smoother.md`) as an identity-in-form backfill of the firm L1 home. It is the constructed-operator-gate analog of the firm `apply_linop`/`krylov-step`/`ksp_solve` L3 backfills (a new-layer-coherence entry, not a modification of an in-place surface). The check is satisfied: the entry adds surface (a full firm chapter) and its evidence is the transported L1 evidence plus directly-re-verified L0 pinpoints; it is not a pure retroactive rotation_claim against an unchanged surface.

**rotation-quality — pass (with a framing note).** The report explicitly does NOT claim an algebraic/structural/reduction rotation across the L3>L1 edge — it claims an **identity-in-form** rotation (value-thread-isomorphic; same signature, same six laws, same three non-laws, same variant profile). The rotation-quality check fails a proposal only when it ASSERTS a compaction rotation that is really a rename/1:1 map. Here the report is candid that the L3>L1 hop is a "layer-coherence rotation, not an algebraic one" and routes the substantive rotation to the L1>L0 leaf-mutation theme (`reciprocal-elementwise-product-mutation-rotation`). This is the sanctioned `Identity-lowerings still require both L levels` pattern, not a disguised rename masquerading as a rotation. Pass: the identity-in-form claim is honestly labeled and matches the precedent cohort (`dot`/`scal`/`apply_linop`).

**variant-axis-coverage — pass.** The entry declares two orthogonal axes (element-type real|complex; damping-mode default|fixed|estimated) and one absorbed axis (operator-representation), all collapsed into the opaque `JacobiSmoother[N]` closure with the absorption explicitly scoped (frontmatter `variant_axes:` block + §Variant axes). I cross-checked against source: both element-type instantiations are witnessed (`template class JacobiSmoother<Operator>; <ComplexOperator>;` at `:106-107`), the three damping modes are witnessed (the `omega == 0.0` / `omega != 1.0` branches at `:84-93`), and the complex path is a true-complex apply (`:41-70`). No hidden branch: the `sf_max` is correctly classed as a construction parameter, not a variant axis. The profile matches the L1 entry's claimed two-orthogonal-plus-one-absorbed framing.

**cross-reference-integrity — warning.** Build-readiness fence guard PASSES: `grep -n '\`\`\`'` shows exactly 6 fence lines (3 balanced pairs: `edit:L3/jacobi-smoother.md` 27→206, `edit:SUMMARY.md` 208→212, `edit:L3/index.md` 214→217), no nested ```text fences, even parity. The firm apparatus is fully ENCLOSED in the first fence: `## Signature` (62), `## Semantics` (82), `## Algebraic laws` (96), `## Status` (153), `## Evidence` (178) all sit inside 27–206 — no fence-truncation defect (the cycle-019/021/024 recurrence-3 pattern is NOT present here). All `[link]` targets in the chapter body resolve on disk (apply_linop, krylov-step, ksp_solve, eigsolve, chebyshev, dot/scal, L1/jacobi-smoother, L1/assemble-diagonal, L1-L0/reciprocal-elementwise-product-mutation-rotation, concepts/{sequential-obstruction,constructed-operators,variant-absorption}). The SUMMARY.md insertion anchors are valid (current SUMMARY has `scal` (28) and `chebyshev` (29) adjacent; the edit inserts `jacobi-smoother` between them, matching the fence context). The L3 index dep-map edit is a well-formed 5-cell row appended after the existing `eigsolve` row (current line 31). **The warning is one live link to a not-yet-on-disk target:** `[\`divfree-projector\`](./divfree-projector.md)` at CYCLE.md line 52 (chapter §Context) is a LIVE link, but `book/src/L3/divfree-projector.md` does NOT exist on disk (only `book/src/L1/divfree-projector.md` and `book/src/L1-L0/divfree-projector-mutation-rotation.md` exist; SUMMARY.md has no L3 divfree row). This is the parallel cycle-037 D1 backfill the report itself flags at lines 176 and 240 ("appended by D1", "if both D1 and D2 land"). Per `rough-in-forward-reference-must-be-plain-text-not-live-link`, a live link to an off-disk target is a `linkcheck2` hard-fail — so this entry is build-safe ONLY if D1's `book/src/L3/divfree-projector.md` lands in the same integration batch. The integration order coupling is undeclared as a hard dependency in the frontmatter `inputs:` (divfree-projector is listed only as a sibling, not a build prerequisite). See Issue 1.

**edge-label-fidelity — pass.** The report carries the edge label L3>L1 (identity-in-form on the constructed-operator-gate apply) and L1>L0 (the substantive leaf-mutation rotation, routed to `reciprocal-elementwise-product-mutation-rotation`). The prose discusses exactly those edges: §"Downward to L1", §"Lowers to", and the §Status all narrate the L3→L1 identity hop and correctly defer the L1→L0 `elementwise_product → forall_switch` rotation to the L1>L0 theme. No L4 edge is claimed (correctly — "no standalone L4 entry"). The edge labels and the prose are in register; no L2>L1-vs-L3>L1 mismatch.

**plan-kind-consistency — pass.** Declared kind is firm L3 operator (frontmatter `firmness: firm`). The content shape matches: full Signature / Semantics / Algebraic-laws (6 + 3 non-laws) / Variant-axes / Status / Lowers-to / Lifts-from / Evidence, no rough-in placeholders, no unresolved TODO. The `firm` status is justified by the firm-on-positive-structure escape (every L3 law is a syntactic identity transported from the firm L1 entry whose laws read off positive source — elementwise multiply at `:38`, setup chain at `:79-93`, transpose alias at `hpp:43`, instantiations at `:106-107`), consistent with the `apply_linop`/`ksp_solve` constructed-operator-gate precedent (no `test-jacobi.cpp` does not gate firm for syntactic-identity laws). The "thinnest constructed-operator gate, no L3 obstruction" framing is faithful to the L1 evidence: the apply IS a single `mfem::forall_switch` elementwise product with no cross-element dependency, no reduction, no sweep, no convergence test — there genuinely is no loop in the apply to obstruct. Defined in L3 vocabulary (whole-tensor field op, no element loop exposed), high→low, with the non-adjacent identity annotated in-line per the cycle-012 convention. Classification is correct.

**skill-uptake-survey — pass (telemetry).** The report references the mechanical citation-verification path (`tools/citecheck/citecheck.py --anchor` / `--scan`) repeatedly (frontmatter, §Evidence, §Supporting evidence) — consistent with the cycle-024 citecheck realization of `verify-citation-range`. It also names `upgrade-plain-text-ref-to-live-link-when-target-on-disk` in the Open-questions (line 241) as the integrator path for the `jacobi-smoother-mutation-rotation` plain-text reference. The `proposed-changes-fence-encloses-full-body-guard` is a critic-side skill (not producer-invoked); no producer omission. No missing-skill signal.

### Issues found

**Issue 1 (cross-reference-integrity, medium severity, build-readiness) — live link to an off-disk sibling chapter.** CYCLE.md line 52 (chapter body §Context) renders `[\`divfree-projector\`](./divfree-projector.md)` as a LIVE markdown link, but `book/src/L3/divfree-projector.md` does not exist on disk (only the L1 and L1-L0 divfree forms exist; no L3 divfree entry in SUMMARY.md). This will be a `linkcheck2` hard-fail at `integrator-finalize` UNLESS the parallel cycle-037 D1 dispatch lands `book/src/L3/divfree-projector.md` in the same integration batch. The report acknowledges D1 is parallel ("appended by D1", lines 176/240) but does not declare it as a hard build prerequisite in the frontmatter `inputs:` (divfree-projector is listed only as a constructed-operator-gate sibling, not a build dependency). Candidate repair: either demote the line-52 reference to plain text (per `rough-in-forward-reference-must-be-plain-text-not-live-link`), or record the D1-must-land-first integration ordering explicitly. The repairer/integrator decides; flagged here as the one genuine build risk.

**Issue 2 (cross-reference-integrity, low severity, missed live-link upgrade) — `jacobi-smoother-mutation-rotation` left plain-text though it exists on disk.** The chapter renders `jacobi-smoother-mutation-rotation` as plain text at lines 58, 170, and 216 (dep-map cell). The report's Open-questions (line 241) states it left this plain-text because it "did not verify its on-disk presence." The file DOES exist: `book/src/L1-L0/jacobi-smoother-mutation-rotation.md`. Plain-text is the safe fallback (not a defect, no build risk), but this is a missed live-link-upgrade opportunity per the `upgrade-plain-text-ref-to-live-link-when-target-on-disk` skill the report itself names. Candidate repair: upgrade the three plain-text occurrences to live links `[\`jacobi-smoother-mutation-rotation\`](../L1-L0/jacobi-smoother-mutation-rotation.md)` (and the dep-map cell relative path). Non-blocking.

**Issue 3 (plan-kind-consistency / scope, informational, no severity) — un-audited L4 verdict carried by analogy.** §Lifts-from and Open-question line 242 assert "no standalone L4 entry" for jacobi-smoother by analogy to the firm `apply_linop`/`ksp_solve` constructed-operator-gate L4 verdicts, without a dedicated cycle-010-style L4-candidacy audit specific to jacobi-smoother. The report is transparent about this ("the analogy is strong but is not a separately-recorded audit verdict"). The analogy is sound (the gate is strictly thinner than `apply_linop`, itself confirmed-not-needed at L4), and the no-L4 claim does not affect the firm L3 status. Recorded as informational telemetry only — not a defect, the report already flags it for a future cross-layer-cross-cutter pass.

---

## Repair

### Fixes attempted

- **Finding (Issue 1)**: cross-reference-integrity (Medium / build-readiness) — CYCLE.md line 52 (chapter §Context) rendered `[\`divfree-projector\`](./divfree-projector.md)` as a LIVE link, but `book/src/L3/divfree-projector.md` does not exist on disk (deferred c036 (A) candidate; the parallel c037 D1 backfill, not guaranteed to land in the same batch). A live link to an off-disk chapter is a `linkcheck2` hard-fail.
  - **Decision**: repaired.
  - **Action**: downgraded the line-52 reference to a plain-text inline-code reference (`\`divfree-projector\`` with an explicit "not yet on disk this cycle, per `rough-in-forward-reference-must-be-plain-text-not-live-link`" note) in the `edit:book/src/L3/jacobi-smoother.md` fence (§Context, CYCLE.md line 52). Verified with `ls` first: `L3/divfree-projector.md`, `L3/reciprocal.md`, `L3/elementwise_product.md`, `L3/normalize.md` are all MISSING; only `divfree-projector` was actually referenced as a live link in the CYCLE.md (the other three deferred slugs the dispatch note conflated do not appear as live links anywhere in this report). The build-readiness coupling on D1 is now removed — this entry is build-safe independent of D1's integration order.

- **Finding (Issue 2)**: cross-reference-integrity (Low) — `jacobi-smoother-mutation-rotation` left plain-text at three chapter sites (§Downward line 58, §Lowers-to line 170, L3-index dep-map cell line 216), though `book/src/L1-L0/jacobi-smoother-mutation-rotation.md` exists on disk → a missed live-link upgrade.
  - **Decision**: repaired.
  - **Action**: confirmed the target exists (`ls book/src/L1-L0/jacobi-smoother-mutation-rotation.md` → EXISTS), then upgraded all three chapter-body/dep-map occurrences to live links `[\`jacobi-smoother-mutation-rotation\`](../L1-L0/jacobi-smoother-mutation-rotation.md)` per skill `upgrade-plain-text-ref-to-live-link-when-target-on-disk` (CYCLE.md lines 58, 170, 216). Also rewrote the report's own Open-question note (line 241) to record the repair and reflect the verified on-disk presence. (The two further `jacobi-smoother-mutation-rotation` mentions in the report's prose Open-questions at line 241 are report-narrative, not chapter content / live-link sites, and were left as prose.)

- **Finding (Issue 3)**: plan-kind-consistency / scope (informational) — "no L4 entry" verdict carried by analogy to the firm `apply_linop`/`ksp_solve` gates, not a dedicated cycle-010-style L4-candidacy audit.
  - **Decision**: not-needed (no edit). The report is transparent about the by-analogy basis and already flags it for a future cross-layer-cross-cutter pass; authoring a dedicated L4-candidacy audit is substantive content outside repair authority, and the critic recorded this as informational telemetry (no severity), not a defect. No status reduction warranted.

### Post-repair verification

- **Fence parity** (`proposed-changes-fence-encloses-full-body-guard`): intact — 6 fence lines, 3 balanced pairs (`edit:book/src/L3/jacobi-smoother.md` 27→206, `edit:book/src/SUMMARY.md` 208→212, `edit:book/src/L3/index.md` 214→217); no nested `text` fences introduced; full firm body remains enclosed. The edits were all single-line in-place substitutions inside existing fences — no fence boundary moved.
- **Live-link resolution**: every remaining live link in all three proposed-changes fences resolves to an on-disk target. The only two non-resolving links are the chapter's self-references to `jacobi-smoother.md` (the new file this report authors), which the integrator materializes on apply — expected and correct. `divfree-projector.md` no longer appears as a live link anywhere.

### Unrepairable findings

None. Both cross-reference-integrity findings were mechanical link link-vs-plain-text fixes within repair authority; Issue 3 is informational (no edit needed).

## Suggested resolution

`ready` — the one build-readiness risk (the off-disk `divfree-projector` live link) is removed; the missed live-link upgrade is applied. The integrator can apply this report's proposed-changes without a D1-must-land-first ordering constraint. Note for the integrator: the `divfree-projector` reference is now intentionally plain-text; if the parallel D1 `book/src/L3/divfree-projector.md` lands in the same batch, a follow-up may re-upgrade it to a live link (per `upgrade-plain-text-ref-to-live-link-when-target-on-disk`), but this is optional and non-blocking.
