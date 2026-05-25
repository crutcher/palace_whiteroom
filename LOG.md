# Cycle log

Per-cycle human-readable summaries, newest first. Full structured detail in `episodic.jsonl`; full meta-review records in `book/src/meta-reviews/`.

Per-cycle entry format:

```
## YYYY-MM-DD cycle-<N> — <push-kind> <slice> [<edge>] — <verdict>

- Synthesis: <one-line summary of what the cycle produced>.
- Verdict: <pass | revise | reject>. <Brief issues if not pass.>
- Friction: <none | one-line>.
- Structural change: <none | one-line>.
```

Meta-review entry format:

```
## YYYY-MM-DD meta-review (cycles <N>–<M>) — <enacted | partial | deferred>

- Window: <N> cycles. Push breakdown: <X FORWARD, Y BACK, Z SIDEWAYS>.
- Cascade: <a> LOW applied; <b> MEDIUM plan items <approved|deferred>; <c> HIGH escalated.
- Plan items enacted: <one-line summaries, or "none">.
- Recurring patterns: <none | one-line description>.
- Full record: `book/src/meta-reviews/YYYY-MM-DD.md`.
```

New entries are **prepended** immediately below the `---` separator, above prior entries.

---

## 2026-05-25 meta-review (cycles 37–43) — enacted — first skill extraction

- Window: 7 cycles. Initial Meta-Critic emission failed JSON parse; retry succeeded. All three meta-10 architecture changes worked end-to-end: Planner self-tightening fired on cycle 37; slice_index_updates channel adopted; plan_kind classification surfaced 5-of-7 retroactive_claims cycles.
- Cascade: 1 LOW; 3 MEDIUM plan items enacted + 1 bonus build-config; 0 HIGH.
- Plan items enacted: (LOW) SIDEWAYS channel-selection pre-emit gate (recurrence #3 of mode=create-on-existing across cycles 22/25/40); (1) Retroactive-claims quoted-prose requirement — log_synthesis.retroactive_claim_evidence must quote on-disk lines per claim; Critic check #12 added; (2) variant-absorption.md "Structurally-distinct variants in otherwise-uniform families" section (Householder/FGMRES pattern + two fix paths); (3) **FIRST SKILL EXTRACTION**: skills/classify-variant-axis/SKILL.md — promoted variant-axis classification procedure from inline Synthesizer prose to invocable skill (validates the user-directed skill-extraction directive from meta-pass prompt update). Bonus: book.toml traverse-parent-directories=true so citation links to reference/ and skill links to skills/ are buildable.
- Watch: does the skill get consulted, or does the Synthesizer rely only on the 2-line inline summary?
- Full record: `book/src/meta-reviews/2026-05-25-cycles-37-43.md`.

## 2026-05-25 cycle-43 — forward gmres [L2→L3] — pass

- Synthesis: Emit retroactive L2→L3 rotation_claims for the gmres slice's existing on-disk L3 section (field-side lifts for initial_residual / apply_BA / orthogonalize-CGS / apply_correction, plus the ls_update_column and back_solve sequential-obstruction records). No new structural writes; the L3 content already exists at book/src/spec/slices/gmres.md §'L3 — global tensor-field form'. Per-claim citations point at that section and at the concepts it references.
- Verdict: pass.
- Friction: none.
- Structural change: none.
## 2026-05-25 cycle-42 — back orthog — pass

- Synthesis: Orthog slice already has L1+L2 content on disk from a prior cycle; this cycle backfills the missing L0→L1 rotation_claims (variant absorption, dot_op hook, normalization-out, MGS/CGS/CGS2 substitutability) against the existing prose with file:line citations into palace/linalg/orthog.hpp and test-orthog.cpp.
- Verdict: pass.
- Friction: none.
- Structural change: none.
## 2026-05-25 cycle-41 — back orthog — revise

- Synthesis: orthog L0→L1 retroactive rotation claims: variant-parametric primitive with local-dot + routine-owns-reduction contract; three claims covering state-hiding (per-variant kernel sequencing), variant absorption (algorithm tag absorbed at one dispatch site), and inner-product abstraction (dot_op hook); confirmed against test-orthog substitutability tests.
- Verdict: revise.
- Friction: Claim 1 explicitly discloses that variant-absorption level (c) (primitive-sequence) is NOT achieved — the L2 chains for MGS / CGS / CGS2 differ in shape and in number/size of collectives. The disclosure is per the variant-absorption discipline and is acceptable in principle, BUT the spec surface that would carry this disclosure is not in the diff. Without the L1/L2 text on disk, the partial absorption is silent rather than declared. Re-emit with the disclosure visible in the spec text (a 'Residual axes' or 'Primitive-sequence divergence' subsection at L2 listing the three concrete chains)..
- Structural change: none.
## 2026-05-25 cycle-40 — sideways orthog,chebyshev — revise

- Synthesis: Initial L1 push on the orthogonalization slice — invariant, variant-parametric procedure absorbing CGS/MGS/CGS2/Householder, consumer interface. Extracted two concept entries: orthogonalization (the kernel family) and chebyshev-iteration (companion concept opened for a future slice; flagged as inner-product-free CG counterpart).
- Verdict: revise.
- Friction: slice_write rejected (path exists; use mode=diff): book/src/spec/slices/orthog.md; concept_write create skipped (already exists; use append-section): orthogonalization; Related to the above: variant-absorption check (#9) fails at level (c) for Householder. The slice claims all three levels of absorption but the primitive-sequence level only holds for the three Gram-Schmidt variants. This is silent partial absorption — the residual axis (Householder's reflector-accumulation state) is not declared in L1 as a variant-conditional state field, nor is the divergence in primitive sequence acknowledged at L1..
- Structural change: none.
## 2026-05-25 cycle-39 — forward chebyshev [L1→L2] — pass

- Synthesis: Chebyshev L1→L2 rotation_claims emitted retroactively against the existing L2 section in book/src/spec/slices/chebyshev.md (lines covering setup unfold, apply unfold, primitive inventory, and variant absorption).
- Verdict: pass.
- Friction: none.
- Structural change: none.
## 2026-05-25 cycle-38 — forward divfree [L1→L2] — pass

- Synthesis: divfree L1→L2: retroactive rotation_claims for the on-disk L2 (apply_linop · set_subvector_zero · ksp_solve · axpy chain); dep-map edges divfree → {apply_linop, set_subvector_zero, ksp_solve, axpy}; index status row bumped to L2.
- Verdict: pass.
- Friction: none.
- Structural change: applied: 1 dep-map edge(s), 2 lesson(s); 5 rotation_claim(s).
## 2026-05-25 cycle-37 — forward gmres [L4→L4] — pass

- Synthesis: GMRES L4→L4 tightening: extracted the convergence test into a `Convergence` constructed-operator surface (third absorption surface alongside `apply_BA` / `apply_correction`); new concept `convergence-test`; inner loop now closes over `Convergence` rather than re-reading `op.rel_tol`/`op.abs_tol`/`s.initial_res`.
- Verdict: pass.
- Friction: none.
- Structural change: applied: 1 concept_write(s), 2 dep-map edge(s), 1 lesson(s); 2 rotation_claim(s).
## 2026-05-25 meta-review (cycles 31–36) — enacted — PHASE 6 DONE

- Window: 6 cycles. **GMRES reached L4** (cycles 31/32/34 — multiple emissions converged the L4 form). The meta-9 refined downgrade rule worked end-to-end: 4 of 6 cycles held pass via `bookkeeping_incomplete` instead of false-downgrading the L4 milestone. **All five Phase 6 DONE criteria are now satisfied.**
- Cascade: 1 LOW; 3 MEDIUM plan items enacted; 0 HIGH.
- Plan items enacted: (LOW) Concept existence-check strengthened with explicit list of existing concept pages; (1) `slice_index_updates` dedicated channel — schema + `state.update_slice_index_row()` + integrator + prompt update — recurrence #2 of `file_edits` anchor mismatch on `spec/index.md` triggers the mechanical channel intervention per meta-9 watch; (2) `plan_kind` enum field — classify cycles as `new_content` / `retroactive_claims` / `tightening` / `back_correction` so 0-substantive-writes passes are distinguishable from no-ops; (3) Planner self-rotation tightening heuristic — consume open `L_n→L_n` friction in the next push rather than defer.
- Phase 6 DONE: 5 active slices, 22 concepts on disk, GMRES at L4 with the expected character (outer-loop obstruction + per-step positive lift + L4 calculus binding). Next decision is human-side: continue Krylov accumulation, pivot to mesh/FE slices, or move to Phase 7 (execution grounding).
- Full record: `book/src/meta-reviews/2026-05-25-cycles-31-36.md`.

## 2026-05-25 cycle-36 — back gmres — pass

- Synthesis: GMRES slice already exists with L0-L4 content; no edits needed. Emitting retroactive L0→L1 rotation_claims covering the L0 cited regions → L1 state schema + building blocks + procedure rotation, with variant-absorption disclosure.
- Verdict: pass.
- Friction: none.
- Structural change: none.
## 2026-05-25 cycle-35 — forward gmres [L4→L4] — revise

- Synthesis: Cycle on gmres L4→L4: tighten the L4 form by collapsing the over-articulated StopTag/hit_limit_converged plumbing into a single typed Outcome flowed through SimState, removing the calculus-level friction flagged as an open question; preserves variant absorption and sequential-obstruction placement.
- Verdict: revise.
- Friction: The Outcome ADT {Continue, Done Bool} carrying a boolean converged flag is itself slightly labored — Done Bool re-encodes the same information that (K.beta < ε) would expose at the call site. If solve_loop pattern-matches Outcome to decide recursion, the boolean payload is only consumed by the caller's final return shape. Consider whether solve_loop can return the terminal SimState directly and let the caller inspect (s.beta < ε) once, eliminating the boolean payload entirely..
- Structural change: applied: 1 lesson(s); 2 rotation_claim(s).
## 2026-05-25 cycle-34 — forward gmres [L3→L4] — pass

- Synthesis: gmres L3→L4: state-stratified SimState / OpParams / Krylov; monadic outer/inner coordination via Solve = StateT SimState; sequential obstructions (ls_update_column, back_solve) typed as pure functions on Krylov. Extracted `state-stratification` and `solve-monad` concepts as canonical L4 vocabulary for solver slices.
- Verdict: pass.
- Friction: concept_write create skipped (already exists; use append-section): state-stratification; concept_write create skipped (already exists; use append-section): solve-monad; file_edit rejected (old_string not found in book/src/spec/index.md): '| [gmres](./slices/gmres.md) | L3 | 2026-05-26 | L3 — global field-side lifts (`'; bookkeeping_incomplete: 5 substantive writes landed; only bookkeeping (index/TOC) write(s) failed. Verdict held pass per meta-9 item 2; next cycle on this slice should re-attempt the bookkeeping update..
- Structural change: none.
## 2026-05-25 cycle-33 — forward divfree [L1→L2] — pass

- Synthesis: divfree L1→L2 already realized in current slice content (apply_linop, set_subvector_zero, ksp_solve, axpy chain); cycle formalizes rotation_claims, extracts set_subvector_zero and ksp_solve concept entries, and registers dependency-map edges.
- Verdict: pass.
- Friction: concept_write create skipped (already exists; use append-section): set_subvector_zero; concept_write create skipped (already exists; use append-section): ksp_solve; file_edit rejected (old_string not found in book/src/spec/index.md): '| [divfree](./slices/divfree.md) | L1 | 2026-05-23 | initial L1; eigensolver-pat'; bookkeeping_incomplete: 4 substantive writes landed; only bookkeeping (index/TOC) write(s) failed. Verdict held pass per meta-9 item 2; next cycle on this slice should re-attempt the bookkeeping update..
- Structural change: none.
## 2026-05-25 cycle-32 — forward gmres [L3→L4] — pass

- Synthesis: GMRES L4: typed SimState/OpParams/Krylov stratification, monadic outer/inner coordination, sequential obstructions surfaced as plain functional recurrences on small-dense state; FGMRES absorbed via constructed-operator helpers.
- Verdict: pass.
- Friction: concept_write create skipped (already exists; use append-section): state-stratification; concept_write create skipped (already exists; use append-section): solve-monad; file_edit rejected (old_string not found in book/src/spec/index.md): '| [gmres](./slices/gmres.md) | L3 | 2026-05-24 | L3 added: field-side primitives'; bookkeeping_incomplete: 7 substantive writes landed; only bookkeeping (index/TOC) write(s) failed. Verdict held pass per meta-9 item 2; next cycle on this slice should re-attempt the bookkeeping update..
- Structural change: none.
## 2026-05-25 cycle-31 — forward gmres [L3→L4] — pass

- Synthesis: GMRES L3→L4: typed state stratification (SimState / OpParams / Krylov), monadic outer/inner coordination over SimState with Krylov as let-bound bundle, constructed-operator helpers absorb pc_side/gs_orthog/flexible by typing, sequential obstructions appear as pure functions on small-dense state. Extracted concepts: state-stratification, solve-monad.
- Verdict: pass.
- Friction: file_edit rejected (old_string not found in book/src/spec/index.md): '| [gmres](./slices/gmres.md) | L3 | 2026-05-25 | GMRES + FGMRES; L3 lifts field-'; bookkeeping_incomplete: 8 substantive writes landed; only bookkeeping (index/TOC) write(s) failed. Verdict held pass per meta-9 item 2; next cycle on this slice should re-attempt the bookkeeping update..
- Structural change: none.
## 2026-05-25 meta-review (cycles 25–30) — enacted

- Window: 6 cycles (first under depth-6 cadence). **GMRES reached L3** (cycle 30): outer-loop sequential obstruction (negative L3 per Phase 6 charter), per-step body positive lift via support-operator template. SIDEWAYS dispatch contract from meta-8 worked (comparison_slices populated). But 4 of 6 cycles auto-downgraded — every downgrade was a *bookkeeping-only* failure (substantive content landed; spec/index.md row update failed). The downgrade rule was conflating two distinct failure categories.
- Cascade: 1 LOW; 3 MEDIUM plan items enacted; 0 HIGH.
- Plan items enacted: (LOW) SIDEWAYS channel-selection guidance — Synthesizer should prefer section_appends on existing compared slices; (1) `file_edits` anchor verification — `spec/index.md` row updates must copy verbatim from live file, fall back to omitting bookkeeping write if anchor unverifiable; (2) **Refined downgrade rule** — integrator now tracks bookkeeping vs substantive failures; pass-with-bookkeeping-only-failure holds pass and sets `bookkeeping_incomplete` flag instead of downgrading; (3) SIDEWAYS output discipline section — typical shape is section_appends to both slices + concept_writes for shared primitives + optional dep-map edges; NOT mode=create on existing slices.
- Phase 6 substantially complete: GMRES L1+L2+L3 ✓ (with expected L3 character — obstruction on outer loop, positive lift on per-step body); L4 remaining. SIDEWAYS fired; multi-revision BACK; 9 meta-reviews; 5 active slices.
- Full record: `book/src/meta-reviews/2026-05-24-cycles-25-30.md`.

## 2026-05-25 cycle-30 — forward gmres [L2→L3] — revise

- Synthesis: GMRES L2→L3: field-side primitives lift to global tensor-field form via the support-operator template; `ls_update_column` and `back_solve` recorded as small-dense-state sequential obstructions (first-class L3 results). Extracted `tensor-field-lift` and `sequential-obstruction` concepts.
- Verdict: revise.
- Friction: file_edit rejected (old_string not found in book/src/spec/index.md): '| `gmres` | L2 | 2026-05-24 | L1 dataflow + L2 primitive composition; variant ab'; verdict auto-downgraded pass→revise: one or more writes did not land (original Critic verdict was 'pass'; see verdict_original in episodic).
- Structural change: none.
## 2026-05-25 cycle-29 — back chebyshev — pass

- Synthesis: Chebyshev L0→L1 already on disk; cycle is a no-op for slice writes — verifying the existing L1 against rotation-quality criteria and emitting the per-claim rotation_claims that were missing from the initial commit.
- Verdict: pass.
- Friction: none.
- Structural change: none.
## 2026-05-25 cycle-28 — forward chebyshev [L1→L2] — revise

- Synthesis: chebyshev L1→L2 unfold: Richardson-like sweep expressed as copy/zero/elementwise_product/scal/axpy/apply_linop composition; variant absorption preserved at primitive-sequence level (only the scalar generator branches on variant); fused-kernel realization treated as transparent optimization; non-associative reduction order preserved.
- Verdict: revise.
- Friction: file_edit rejected (old_string not found in book/src/spec/index.md): '| `chebyshev` | L1 | 2026-11-19 | 4th-kind & 1st-kind polynomial smoothers absor'; verdict auto-downgraded pass→revise: one or more writes did not land (original Critic verdict was 'pass'; see verdict_original in episodic).
- Structural change: none.
## 2026-05-25 cycle-27 — back divfree — pass

- Synthesis: divfree L0→L1 already complete on disk (slice carries L1 + L2 sections); cycle records the rotation_claims that were missing from the prior emission and brings the dependency map / status table in sync.
- Verdict: pass.
- Friction: none.
- Structural change: applied: 1 lesson(s); 1 rotation_claim(s).
## 2026-05-25 cycle-26 — forward divfree [L1→L2] — revise

- Synthesis: divfree L1→L2: composed apply as apply_linop(WeakDiv) → set_subvector_zero → ksp_solve → apply_linop(Grad) + axpy. Extracted set_subvector_zero and ksp_solve as new concept entries; appended divfree-use section to apply_linop. Sign convention and BC ordering preserved as load-bearing L2 claims; MG-vs-AMG preconditioner choice and partial-vs-full assembly recorded as transparent optimizations.
- Verdict: revise.
- Friction: file_edit rejected (old_string not found in book/src/spec/index.md): '| `divfree` | L1 | C-7 | Divergence-free projector. Constructed-operator absorpt'; verdict auto-downgraded pass→revise: one or more writes did not land (original Critic verdict was 'pass'; see verdict_original in episodic).
- Structural change: none.
## 2026-05-25 cycle-25 — sideways gmres,orthog — revise

- Synthesis: Established gmres and orthog slices at L1 with concept entries; the parent gmres slice scopes orthogonalization-variant axes to the orthog slice via forward reference, achieving variant absorption (a/b/c) on the GMRES axes (preconditioner side, restart, flexibility) and explicitly deferring the orthogonalization axes to the kernel slice.
- Verdict: revise.
- Friction: slice_write rejected (path exists; use mode=diff): book/src/spec/slices/gmres.md; slice_write rejected (path exists; use mode=diff): book/src/spec/slices/orthog.md; concept_write create skipped (already exists; use append-section): orthogonalization; verdict auto-downgraded pass→revise: one or more writes did not land (original Critic verdict was 'pass'; see verdict_original in episodic).
- Structural change: none.
## 2026-05-24 meta-review (cycles 22–24) — enacted

- Window: 3 cycles. **All clean passes.** SIDEWAYS fired (cycle 22 — anti-procrastination clause worked); orthog L1→L2 landed (cycle 23); gmres L1→L2 re-emitted cleanly via section_appends (cycle 24, fixing the cycle-21 downgrade).
- Cascade: 1 LOW direct action; 3 MEDIUM plan items enacted; 0 HIGH.
- Plan items enacted: (1) SIDEWAYS dispatch contract — Planner must name ≥2 slices in `slices=a,b` + comparison axis; orchestrator parser populates `comparison_slices` list; precondition rejects degenerate SIDEWAYS as escalate (cycle 22 fired with slice='unknown' because parser ignored slices= field); (2) Critic exercised_checks promoted from prose to structured field in critic_verdict schema (REQUIRED on pass verdicts; all 11 checks should appear with explicit outcomes); (3) Mutation pseudocode discipline codified in Synthesizer prompt — L2 in-place primitives need explicit `t ← copy(x)`, not raw `t = x`. **LOW** direct action: concept_writes channel-selection rule extended to verify existence before mode=create.
- Phase 6 substantially complete: GMRES at L1+L2 on disk; SIDEWAYS fired; 8 meta-reviews; only GMRES at L3/L4 remains as a concrete Phase 6 deliverable.
- Full record: `book/src/meta-reviews/2026-05-24-cycles-22-24.md`.

## 2026-05-24 cycle-24 — forward gmres [L1→L2] — pass

- Synthesis: GMRES L1→L2: unfolded the six L1 building blocks into the axpy/dot/nrm2/scal/apply_linop/givens primitive vocabulary as a `## L2 — primitive composition` section appended to the slice; extracted four support-operator concepts (apply-linop, dot, nrm2, orthogonalization); preserved variant absorption at L2 (primitive-sequence shape-invariant across pc_side × gs_orthog × flexible).
- Verdict: pass.
- Friction: concept_write create skipped (already exists; use append-section): nrm2; concept_write create skipped (already exists; use append-section): dot.
- Structural change: applied: 4 concept_write(s), 5 dep-map edge(s), 2 lesson(s); 5 rotation_claim(s).
## 2026-05-24 cycle-23 — forward orthog [L1→L2] — pass

- Synthesis: orthog L1→L2: unfolded the three variants into named primitive chains (dot, allreduce_sum, axpy, gemv_basis), preserving load-bearing collective shape and MGS ordering while marking BLAS-fusion / kernel-packing transparent; extracted gemv_basis as a new L2 concept with axpy dependency; added dependency-map edges for orthog→{dot, axpy, gemv-basis, allreduce-sum}.
- Verdict: pass.
- Friction: none.
- Structural change: applied: 1 concept_write(s), 2 dep-map edge(s), 2 lesson(s); 4 rotation_claim(s).
## 2026-05-24 cycle-22 — sideways unknown — pass

- Synthesis: L0→L1 obstruction: slice `unknown` dispatched with no exploration input and no prior content; emitted minimal stub + obstruction rotation_claim + push-back proposing a dispatch-layer guard against empty-subject cycles.
- Verdict: pass.
- Friction: none.
- Structural change: applied: 1 slice_write(s), 1 lesson(s); 1 rotation_claim(s).
## 2026-05-24 meta-review (cycles 19–21) — enacted

- Window: 3 cycles. **GMRES finally landed**: cycle 20 created gmres.md (180 lines L1) and incremental-least-squares concept; cycle 21 extracted 7 support concepts (apply_linop, axpy, dot, givens, nrm2, scal, trsv — bottom-up vocabulary). Cycle 21's L2 prose for gmres.md was beautiful but didn't apply (section-append topology not covered by any channel).
- Cascade: 0 LOW; 3 MEDIUM plan items enacted + 1 bonus integrator fix; 0 HIGH.
- Plan items enacted: (1) `section_appends` channel — the third edit topology (alongside file-creation and in-place edit); `state.append_section(path, heading, content)` with idempotency on heading line; (2) Synthesizer prompt documents the integrator's 5-phase order so plans can be designed to take advantage of structural→relational ordering; (3) `prompts/planner.md` criterion 4 rewritten: concrete trigger ("≥2 slices same edge with pass + no open friction → SIDEWAYS is DEFAULT") + anti-procrastination ("if SIDEWAYS hasn't fired in ≥10 cycles AND trigger conditions hold, MUST emit SIDEWAYS next"). **Bonus**: `add_dependency_map_edge` auto-initializes empty mermaid blocks in layer sections that have prose only (directly resolves cycle-21's 8 edge crashes).
- Diff-apply pattern now closed across THREE sub-modes: new files (file_creates), in-place edits (file_edits), section appends (section_appends). The diff channel survives only as last-resort.
- SIDEWAYS escalation: if cycles 22+ still don't fire SIDEWAYS, the anti-procrastination clause is broken and requires a further meta-cycle.
- Full record: `book/src/meta-reviews/2026-05-24-cycles-19-21.md`.

## 2026-05-24 cycle-21 — forward gmres [L1→L2] — revise

- Synthesis: GMRES L1→L2: unfolded the five L1 building-blocks (initial_residual, apply_BA, orthogonalize, ls_update_column, back_solve, apply_correction) into named base primitives (apply_linop, axpy, dot, nrm2, scal, givens_generate/apply2, trsv). Extracted seven concept entries for the BLAS-style vocabulary. orthogonalize_column remains opaque pending the orthog slice. Numerical-claim register distinguishes load-bearing claims (Givens algorithm, replay-then-generate order, β as |s[j+1]|) from transparent fusions.
- Verdict: revise.
- Friction: slice_write diff failed for book/src/spec/slices/gmres.md: git apply failed:
STDERR:
error: No valid patches in input (allow with "--allow-empty")

DIFF:
--- a/book/src/spec/slices/gmres.md
+++ b/book/src/spec/slices/gmres.md
@@
 - `CheckDot` NaN/Inf gating semantics (referenced from the inner loop's residual checks) is cross-cutting across all iterative solvers and not pinned here.
 
+## L2 — primitive composition
+
+The L2 form unfolds each L1 building-block into a sequence of named base primitives — `apply_linop`, `axpy`, `dot`, `nrm2`, `scal`, `givens_generate`, `givens_apply2`, `trsv` — plus the dispatched orthogonalisation kernel (deferred to the `orthog` slice). Optimization-transparent fusions (e.g., MGS's dot+axpy fused inner step, packed-rotation registers) are silent; load-bearing numerical choices (rotation algorithm, in-place column update order) are explicit.
+
+### Primitive vocabulary
+
+See `concepts/` for canonical definitions:
+- [`apply_linop`](../../concepts/apply_linop.md) — `y ← L · x` for an abstract linear operator `L`.
+- [`axpy`](../../concepts/axpy.md) — `y ← α·x + y`.
+- [`dot`](../../concepts/dot.md) — `α ← ⟨x, y⟩`.
+- [`nrm2`](../../concepts/nrm2.md) — `α ← ‖x‖₂`.
+- [`scal`](../../concepts/scal.md) — `x ← α·x`.
+- [`givens_generate`](../../concepts/givens.md#generate) — `(cs, sn) ← G(dx, dy)`. Cites L0.3.
+- [`givens_apply2`](../../concepts/givens.md#apply) — in-place 2-vector update `(dx, dy) ← (cs·dx + sn·dy, −s̄n·dx + cs·dy)`. Cites L0.4.
+- [`trsv`](../../concepts/trsv.md) — triangular solve `T · y = s`.
+- `orthogonalize_column(gs_orthog, V[0..j], w) → (w', h)` — dispatched at L1 into one of `mgs / cgs / cgs2`; L2 internals live in the `orthog` slice.
+
+### Building-block unfoldings
+
+**`initial_residual(op, b, x)`** (cites L0.5).
+
+```
+initial_residual(op, b, x):
+  if not op.initial_guess:
+    x ← 0                                                     // scal(0, x) or zero-fill
+    if op.pc_side == LEFT and op.B != null:
+      r0 ← apply_linop(op.B, b)                               // r0 = M·b
+    else:
+      r0 ← b                                                  // copy
+  else:
+    t ← apply_linop(op.A, x)                                  // t = A·x
+    axpy(-1, t, b_copy=b)        // r = b − A·x  (b unchanged; r0 holds result)
+    r0 ← b_copy
+    if op.pc_side == LEFT and op.B != null:
+      r0 ← apply_linop(op.B, r0)                              // r0 ← M·(b − A·x)
+  return (r0, x)
+```
+
+**`apply_BA(op, v)`** (cites L0.6). Canonical primitive sequence; `pc_side` selects which two `apply_linop` calls compose and which intermediate is exposed as `z`.
+
+```
+apply_BA(op, v):
+  if op.B == null:
+    w ← apply_linop(op.A, v); z ← ⊥
+  elif op.pc_side == LEFT:
+    t ← apply_linop(op.A, v); w ← apply_linop(op.B, t); z ← ⊥
+  else:  // RIGHT
+    z ← apply_linop(op.B, v); w ← apply_linop(op.A, z)
+  return (w, z)
+```
+
+**`orthogonalize(gs_orthog, V[0..j], w) → (w', h[0..j])`** (cites L0.7). Dispatches to the `orthog` slice. The L2 contract here: input `w`, basis prefix `V[0..j]`; output `w'` orthogonal to `span(V[0..j])` (to working precision per `gs_orthog`) and `h` the projection coefficients. The final normalisation step `h[j+1] ← nrm2(w'); scal(1/h[j+1], w')` is explicit in the L2 procedure below, not absorbed into `orthogonalize_column`.
+
+**`ls_update_column(K, j, h)`** (cites L0.3, L0.4). Incremental triangularisation of the Hessenberg column via stored Givens rotations.
+
+```
+ls_update_column(K, j, h):
+  // 1. Replay previously-recorded rotations on the new column.
+  for k in 0 .. j-1:
+    givens_apply2(h[k], h[k+1], K.cs[k], K.sn[k])
+  // 2. Generate a fresh rotation from the column tail (h[j], h[j+1]).
+  (K.cs[j], K.sn[j]) ← givens_generate(h[j], h[j+1])
+  // 3. Apply it to the column itself: h[j+1] is annihilated.
+  givens_apply2(h[j], h[j+1], K.cs[j], K.sn[j])
+  // 4. Apply the same rotation to the RHS pair (s[j], s[j+1]); s[j+1] was 0.
+  givens_apply2(K.s[j], K.s[j+1], K.cs[j], K.sn[j])
+  // 5. Store the rotated column into H and advance β.
+  K.H[:, j] ← h
+  K.beta ← |K.s[j+1]|
+  return K
+```
+
+The order (replay-then-generate-then-apply) is load-bearing: the new rotation must be generated *after* the prior rotations have been replayed on the new column, so `h[j+1]` is the post-replay tail.
+
+**`back_solve(K, j) → y`** (cites L0.12). The active block of `H` is now upper-triangular by construction of step 3 above.
+
+```
+back_solve(K, j):
+  // K.H[0..j, 0..j] is upper-triangular; K.s[0..j] is the rotated RHS.
+  y ← trsv(upper=K.H[0..j, 0..j], rhs=K.s[0..j])
+  return y
+```
+
+**`apply_correction(op, K, y, j, x)`** (cites L0.12, L0.13).
+
+```
+apply_correction(op, K, y, j, x):
+  if op.flexible:
+    for k in 0 .. j:
+      axpy(y[k], K.Z[k], x)                                   // x ← x + y[k]·Z[k]
+  elif op.pc_side == RIGHT and op.B != null:
+    t ← 0
+    for k in 0 .. j:
+      axpy(y[k], K.V[k], t)                                   // t = Σ y[k]·V[k]
+    Mt ← apply_linop(op.B, t)
+    axpy(1, Mt, x)                                            // x ← x + M·t
+  else:  // LEFT or no preconditioner
+    for k in 0 .. j:
+      axpy(y[k], K.V[k], x)
+  return x
+```
+
+### Inner-loop primitive sequence
+
+At step `j` of the inner (Arnoldi) loop the L2 primitive chain is:
+
+```
+(w, z) ← apply_BA(op, V[j])                  // 1–2 apply_linop
+if flexible: Z[j] ← z
+(w', h[0..j]) ← orthogonalize_column(gs, V[0..j], w)   // → orthog slice
+h[j+1] ← nrm2(w'); scal(1 / h[j+1], w'); V[j+1] ← w'    // basis-vector normalisation
+ls_update_column(K, j, h)                    // (j) givens_apply2 replays + 1 givens_generate + 2 givens_apply2
+```
+
+This shape is invariant across the four variant combinations `pc_side × flexible`: only `apply_BA` and the `Z[j] ← z` capture differ, exactly as the L1 absorption claims.
+
+### Numerical-claim register
+
+Load-bearing (preserved across L1→L2):
+- **Rotation algorithm.** `givens_generate` is LAPACK-style scaled (avoids overflow on large `|dx|`, `|dy|`); a naïve `(c,s) = (dx, dy)/√(dx²+dy²)` is not equivalent under finite precision.
+- **Column-update order in `ls_update_column`.** Replay-then-generate-then-apply (above). Reordering breaks the triangularisation invariant.
+- **CGS2 refinement semantics** (deferred to `orthog` slice) is load-bearing for backward stability of GMRES.
+- **β as `|s[j+1]|`.** The residual proxy used for the convergence test is the rotated-RHS tail, not a re-evaluated `‖b − A·x_j‖`. The two agree only up to LS-step accuracy.
+
+Transparent (silently unfolded):
+- Storage layout of `V` (row-major vs. column-major; packed vs. separate vectors).
+- Fusion of `dot`+`axpy` inside MGS, or of the final `nrm2`+`scal` for `V[j+1]`.
+- Whether `givens_apply2` is implemented as four FMAs or as a packed BLAS rot-call.
+- Whether `back_solve`'s `trsv` runs on a CPU triangular kernel or a dense GEMV-then-divide chain — `H` is `O(max_dim²)` and `max_dim` is small, so the choice has no algorithmic consequence.
+
+## Open questions (extends earlier list)
+
+- The exact loop structure of MGS / CGS / CGS2 (collective shape, refinement test) is deferred to the `orthog` slice. The L2 form here treats `orthogonalize_column` as one opaque primitive.
+- `back_solve`'s handling of a near-singular leading block (when GMRES has effectively converged but the LS system is rank-deficient) is not pinned at L2; the L0 code uses a straight back-substitution and relies on the convergence test to catch the case.
; dependency_map_edge failed for apply_linop: no ```mermaid block in section '## L2 —'; dependency_map_edge failed for axpy: no ```mermaid block in section '## L2 —'; dependency_map_edge failed for dot: no ```mermaid block in section '## L2 —'; dependency_map_edge failed for nrm2: no ```mermaid block in section '## L2 —'; dependency_map_edge failed for scal: no ```mermaid block in section '## L2 —'; dependency_map_edge failed for givens: no ```mermaid block in section '## L2 —'; dependency_map_edge failed for trsv: no ```mermaid block in section '## L2 —'; dependency_map_edge failed for gmres: no ```mermaid block in section '## L2 —'; verdict auto-downgraded pass→revise: one or more writes did not land (original Critic verdict was 'pass'; see verdict_original in episodic).
- Structural change: none.
## 2026-05-24 cycle-20 — forward gmres [L0→L1] — pass

- Synthesis: gmres L0→L1 — cited 16 regions; L1 schema separates SimState / OpParams / Krylov (per-cycle ephemeral); six L1 building blocks (initial_residual, apply_BA, orthogonalize, ls_update_column, back_solve, apply_correction) absorb all four variant axes at single dispatch sites; extracted concept incremental-least-squares; extended constructed-operators with GMRES usage section.
- Verdict: pass.
- Friction: none.
- Structural change: applied: 1 slice_write(s), 2 concept_write(s), 2 dep-map edge(s), 2 lesson(s); 5 rotation_claim(s).
## 2026-05-24 cycle-19 — forward chebyshev [L0→L1] — pass

- Synthesis: L0→L1 consolidation for chebyshev: tighten 1st-kind state schema (theta/delta persist, lambda_max/min are transient), clarify variant encoding via class identity, and flag unreachable complex-transpose template specializations.
- Verdict: pass.
- Friction: none.
- Structural change: applied: 1 lesson(s); 2 rotation_claim(s).
## 2026-05-24 cycle-18 — back orthog — revise

- Synthesis: L0→L1 for orthog: orthogonalize_column primitive with variant∈{MGS,CGS,CGS2} absorbed parametrically; dot_op hook absorbs inner-product weighting; MPI collective shape disclosed as residual L2 cost axis.
- Verdict: revise.
- Friction: slice_write rejected (path exists; use mode=diff): book/src/spec/slices/orthog.md; verdict auto-downgraded pass→revise: one or more writes did not land.
- Structural change: none.
## 2026-05-24 cycle-17 — forward divfree [L0→L1] — revise

- Synthesis: divfree L0→L1 consolidated: corrected Mult(x,y) mutation pattern from alias_with_input to pure (per 2026-05-24 lesson on out-of-place wrappers); confirmed WeakDiv sign convention from explorer citations; surfaced NLEPS-exposes-but-doesn't-use observation as open question.
- Verdict: revise.
- Friction: slice_write diff failed for book/src/spec/slices/divfree.md: git apply failed:
STDERR:
error: patch fragment without header at line 18: @@ -90,8 +90,15 @@

DIFF:
--- a/book/src/spec/slices/divfree.md
+++ b/book/src/spec/slices/divfree.md
@@ -56,9 +56,9 @@
 
 ### Mutation pattern
 
 - Single-argument `Mult(y)`: `in_place_overwrite` on `y`; `psi`, `rhs` are
   `scratch_buffer` members.
-- Two-argument `Mult(x, y)`: `alias_with_input` viewed as a pure function
-  `y = P x`; implemented as `y ← x; Mult(y)`. No aliasing between `x` and
-  `y` is assumed.
+- Two-argument `Mult(x, y)`: `pure` (function `y = P x`); implemented as
+  `y ← x; Mult(y)`. The wrapper does not assume or rely on aliasing
+  between `x` and `y` — it is copy-then-apply-in-place.
 
 ## Variant axes (absorption status)
 
@@ -90,8 +90,15 @@
 - Scope description attributes use to driven/transient solvers; only
   eigensolver-path callers are visible. Stale doc, or missing call site
   outside the inspected glob?
 - No direct unit test (`test-divfree.cpp` does not exist); coverage is
   indirect via `test/examples/`. A synthetic invariant check (post-Mult,
   `WeakDiv · y` is zero on non-essential dofs to ksp tolerance) would be
   the natural unit-test surface if one were added.
-- `WeakDiv` sign-convention claim (that `MixedVectorWeakDivergenceIntegrator`
-  encodes the negative-divergence sign, making `+Grad·ψ` the correction)
+- `WeakDiv` sign-convention claim (that `MixedVectorWeakDivergenceIntegrator`
+  encodes the negative-divergence sign, making `+Grad·ψ` the correction)
+  is confirmed: `PopulateCoefficientContext` is called with factor `-1.0`
+  at `mixedvecgrad.cpp:202`, and the integrator header comment at
+  `integrator.hpp:217` states `a(u,v) = -(Q u, grad v)`.
+- `NonLinearEigenvalueSolver` exposes `SetDivFreeProjector` and stores
+  `opProj` (`nleps.cpp:38-42`) but no `opProj->Mult` call site is visible
+  inside the NLEPS iteration in this revision. Either the projection
+  step is intentionally elided on the NLEPS path or the wire-up is
+  incomplete.
; verdict auto-downgraded pass→revise: one or more writes did not land.
- Structural change: none.
## 2026-05-24 cycle-16 — forward orthog [L0→L1] — revise

- Synthesis: orthog L0→L1 refinement: corrected miscited 'SLEPc wrapper' to the ROM/PROM `romoperator.cpp:49-68` dispatch, disclosed the two-wrapper structure (GMRES uses m=j+1, ROM uses m=j) as caller-index convention not primitive divergence, added per-variant m==0 micro-difference as L2-level residual, refined citation ranges per Explorer verification.
- Verdict: revise.
- Friction: slice_write diff failed for book/src/spec/slices/orthog.md: git apply failed:
STDERR:
error: corrupt patch at line 78

DIFF:
--- a/book/src/spec/slices/orthog.md
+++ b/book/src/spec/slices/orthog.md
@@ -49,12 +49,17 @@
 - **Inner-product weighting (`InnerProductW` template hook).** Absorbed as the `dot_op`
   argument. Default is the unweighted local dot; callers (e.g. weighted GMRES) pass a
   custom local inner product. The contract — `dot_op` is *local*, routine owns reduction —
   is uniform across variants.
 
 **Residual axes (disclosed, not absorbed at L1).**
 
 - MPI collective shape differs by variant (MGS: m reductions of size 1; CGS: 1 reduction
   of size m; CGS2: 2 reductions of size m). This is a performance axis surfaced at L2,
   not an L1 semantic difference. MPI structure is out of scope for this project per
   CLAUDE.md; recorded here as a cost annotation only.
+- Empty-basis (m==0) handling differs textually per variant (CGS has explicit early
+  return; MGS relies on the loop body never executing). Both satisfy the L1 contract
+  (w unchanged, H empty); the difference is a micro-implementation detail at L2, not
+  an L1 distinction.
 - Normalization of `w'` is **not** part of this primitive; callers normalize. Header TODO
   notes this asymmetry; we preserve current convention.
 
 **State / mutation pattern.** `H` is written (CGS2 accumulates across two passes; MGS/CGS
 write once). `w` is updated in place (MGS: m sequential rank-1 updates; CGS: one batched
 update from saved `H`; CGS2: two batched updates). `V_basis` is read-only throughout.
 
-**Caller interface.** GMRES/FGMRES use a single dispatch helper
-`OrthogonalizeIteration(type, comm, V, w, Hj, j)` that forwards to this primitive with
-`m = j+1`. The Arnoldi step calls it uniformly regardless of variant; the variant lives
-as a runtime field on the solver.
+**Caller interface.** Two independent dispatch wrappers forward to this primitive:
+
+- **GMRES/FGMRES path.** `OrthogonalizeIteration(type, comm, V, w, Hj, j)` in
+  `iterative.cpp` calls the primitive with `m = j+1` (orthogonalize new vector against
+  the leading `j+1` basis columns including the just-added one's predecessors). Uses
+  the default identity dot.
+- **ROM/PROM path.** `OrthogonalizeColumn(type, comm, V, w, Rj, j, dot_op)` in
+  `romoperator.cpp` calls the primitive with `m = j` and a caller-supplied weighted
+  `dot_op`. The `m = j` vs `m = j+1` difference is a caller-side index convention
+  (how many columns the caller has populated when invoking), not a primitive-level
+  difference; the primitive takes `m` directly.
+
+Both wrappers inspect `type` exactly once at the dispatch switch; the rest of the
+caller logic is uniform. The two wrappers are a structural duplication candidate
+(out of scope here).
 
 ### Citations
 
 - `palace/linalg/orthog.hpp:18-23` — header contract (input V normalized, output w not
   normalized, `dot_op` is local + routine owns reduction).
-- `palace/linalg/orthog.hpp:25-36` — MGS variant.
-- `palace/linalg/orthog.hpp:38-53` — CGS / CGS2 variant (toggled by `refine` flag).
-- `palace/linalg/orthog.hpp:55-89` — block / SLEPc-facing wrappers (same shape).
+- `palace/linalg/orthog.hpp:26-37` — `IdentityInnerProduct` default `dot_op` (LocalDot;
+  confirms local-then-reduce contract).
+- `palace/linalg/orthog.hpp:39-53` — `OrthogonalizeColumnMGS` (per-j single-element
+  reduce + rank-1 update).
+- `palace/linalg/orthog.hpp:55-87` — `OrthogonalizeColumnCGS` (single size-m reduce;
+  `refine=true` performs the second pass and accumulates `H += dH`).
 - `palace/utils/labels.hpp:163-170` — `enum Orthogonalization { MGS, CGS, CGS2 }`.
 - `palace/linalg/iterative.cpp:307-326` — `OrthogonalizeIteration` dispatch helper.
-- `test/unit/test-orthog.cpp:70-97`, `:123-160` — parametric tests over all three variants
-  + custom inner product, asserting the substitutable contract.
+- `palace/models/romoperator.cpp:49-68` — `OrthogonalizeColumn` (ROM/PROM dispatch
+  wrapper; forwards a caller-supplied weighted `dot_op`; `m = j`).
+- `palace/models/romoperator.cpp:224`, `:643` — PROM basis-extension call sites.
+- `test/unit/test-orthog.cpp:71-97` — variant-parametric test harness.
+- `test/unit/test-orthog.cpp:99-121` — m==0 early-exit (all variants leave w unchanged).
+- `test/unit/test-orthog.cpp:123-162` — real basis, ⟨w',V_i⟩ < 1e-12 across variants.
+- `test/unit/test-orthog.cpp:164-232` — multi-column orthogonality + preservation.
+- `test/unit/test-orthog.cpp:234-274` — complex case.
+- `test/unit/test-orthog.cpp:276-330` — custom `RealWeightedInnerProduct` exercises
+  the non-identity `dot_op` hook.
 
 ### Test linkage
 
 `test/unit/test-orthog.cpp` ↔ `palace/linalg/orthog.hpp` (new linkage; record in
 `scaffolding/test-linkages` when promoted). Tests confirm:
@@ -100,11 +119,14 @@
 CGS-instability stress cases (near-rank-deficient bases that distinguish CGS from CGS2
 numerically) are **not** covered by the unit tests; the variants are tested as
 substitutable, not as numerically distinguishable.
 
 ### Open questions
 
 - Lift normalization into the primitive's contract, or preserve the caller-normalizes
   convention? Header has a TODO; deferred.
 - Surface MPI collective shape as a formal cost annotation at L2 when that slice lands.
+- De-duplicate the two dispatch wrappers (`iterative.cpp::OrthogonalizeIteration` and
+  `romoperator.cpp::OrthogonalizeColumn`)? They differ only in (a) `dot_op` forwarding
+  and (b) caller index convention. Out of scope here; flagged for a future cycle.
 
 ## L1 → L2
 
 (Deferred to next cycle on this slice.)
; verdict auto-downgraded pass→revise: one or more writes did not land.
- Structural change: none.
## 2026-05-24 meta-review (cycles 13–15) — enacted (with 2 implementation deviations)

- Window: 3 cycles. Push breakdown: 2 FORWARD, 1 BACK, 0 SIDEWAYS. All three on `gmres`. All three diff-applies FAILED (corrupt patch / line-count mismatch) — recurrence #2 of the diff-hygiene problem fired the escalation watch.
- Cascade: 0 LOW; 4 MEDIUM plan items approved and enacted; 0 HIGH escalated.
- Plan items enacted: (1) **`file_creates` channel** added to Synthesizer output (orchestrator-side) bypassing unified-diff for new files — deviation from Meta-Critic's "MCP server tool" proposal, same intent simpler implementation; (2) anti-grind heuristic in `prompts/planner.md` (3 consecutive revises with novel friction → rotate); (3) orchestrator-side **verdict downgrade** rule (apply failure → pass becomes revise) — deviation from Meta-Critic's "Critic-side rule" proposal (Critic verdicts before apply; failure visible only orchestrator-side); (4) **first lessons-promotion** fired: FGMRES per-step variant lesson → new "Limits of constructed-operator absorption" section in `constructed-operators.md` + cross-ref in `variant-absorption.md`.
- Watch updates: diff-apply mismatch recurrence #2 → enacted file_creates intervention (watch resets for new failure modes); pass-with-failed-diff → orchestrator hard rule (should not recur structurally); same-slice grind → anti-grind heuristic (watch whether it fires in cycle 16+); variant-absorption cluster reaches recurrence #4 (still same-slice; cross-slice recurrence escalates to High); NEW watch: Meta-Critic implementation-location proposals were deflected twice this round.
- Full record: `book/src/meta-reviews/2026-05-24-cycles-13-15.md`.

## 2026-05-24 cycle-15 — back gmres — pass

- Synthesis: 2 rotation_claim(s); diff applied
- Verdict: pass.
- Friction: diff-apply failed: git apply failed:
STDERR:
error: corrupt patch at line 90

DIFF:
--- /dev/null
+++ b/book/src/spec/slices/gmres.md
@@ -0,0 +1,93 @@
+# Slice: gmres
+
+Generalized Minimal Residual method for solving Ax = b where A is a general
+(possibly non-symmetric, possibly indefinite) linear operator. Krylov subspace
+projection method that minimizes the residual 2-norm over an affine Krylov
+subspace.
+
+## L0 — mutation reference
+
+Canonical reference: Saad, *Iterative Methods for Sparse Linear Systems*, 2nd
+ed., Algorithm 6.9 (GMRES) and 6.11 (Restarted GMRES). Palace's hypre/PETSc
+wrappers expose this as a black-box; the L0 mutation reference is the textbook
+pseudocode (mutable arrays for the Krylov basis V, the upper-Hessenberg H̄, the
+residual-rotated RHS vector g, and the Givens parameters (c_i, s_i)).
+
+The pseudocode threads loop counters, mutable Hessenberg entries, mutable
+Givens-rotated RHS, mutable basis-column writes, and a happy-breakdown early
+exit. This is the L0 form; the slice does not duplicate the textbook listing.
+
+## L1 — invariant form
+
+**Inputs.** Operator `A : V → V` (linear), right-hand side `b ∈ V`, initial
+guess `x_0 ∈ V`, preconditioner `M` (possibly identity), restart length `m ∈
+ℕ_{≥1}`, tolerance `τ > 0`, max outer restarts `k_max`.
+
+**Side convention.** A preconditioner side (left / right / split / none) is
+fixed at solver construction. The L1 statement is written for an effective
+operator `Â` and effective RHS `b̂` constructed once from `(A, M, side)`;
+downstream L1 does not re-inspect `side`. See
+`book/src/concepts/constructed-operators.md`.
+
+**Statement (one restart cycle).** Given current iterate `x`, with `r =
+b̂ − Â x` and `β = ‖r‖_2`:
+
+1. Build an orthonormal basis `V_m = [v_1, …, v_m]` of the Krylov subspace
+   `𝒦_m(Â, r) = span{r, Â r, Â² r, …, Â^{m−1} r}`, with `v_1 = r / β`, such
+   that there exists an upper-Hessenberg matrix `H̄_m ∈ ℝ^{(m+1)×m}` with
+   `Â V_m = V_{m+1} H̄_m`.
+2. Select `y_m ∈ ℝ^m` minimizing `‖β e_1 − H̄_m y‖_2`.
+3. Update `x ← x + V_m y_m`.
+4. The new residual norm equals the least-squares residual
+   `‖β e_1 − H̄_m y_m‖_2`; this is monitored against `τ` and may trigger
+   early termination of the inner cycle before reaching dimension `m`
+   (happy breakdown when an Arnoldi sub-diagonal vanishes; convergence when
+   the running residual estimate falls below `τ‖b̂‖_2`).
+
+The outer loop restarts steps 1–4 with the updated `x` until convergence or
+`k_max` cycles. Flexible variants (where the right-preconditioner is allowed
+to change between Arnoldi steps) replace step 1's invariant with the
+flexible-Arnoldi invariant `Â Z_m = V_{m+1} H̄_m` where `Z_m`'s columns are
+the per-step preconditioned basis; this is out of scope for this slice (see
+Open Questions).
+
+**Invariants.**
+- (Orthonormality) `V_m^T V_m = I_m`.
+- (Arnoldi relation) `Â V_m = V_{m+1} H̄_m`.
+- (Optimality) `x_m − x_0 ∈ 𝒦_m(Â, r_0)` minimizes `‖b̂ − Â x‖_2` over
+  that affine subspace.
+- (Monotonicity within a cycle) `‖r_{j+1}‖_2 ≤ ‖r_j‖_2`.
+
+**Outputs.** Final iterate `x`, achieved residual norm, iteration count,
+convergence flag.
+
+## State partition (for L4 staging)
+
+- **Sim state.** `x` (the iterate).
+- **Operator-internal / per-solve.** The Krylov basis `V_{·}`, the
+  Hessenberg `H̄_{·}`, the least-squares state used to extract `y` and the
+  running residual estimate, the Givens / orthogonalization scratch — all
+  live for one restart cycle and are reset across restarts. The L1
+  statement treats these as existentially quantified ("there exists
+  `H̄_m`…"); they are realized as mutable per-solve workspace at L2.
+- **Ephemeral.** The matvec output buffer `Â v_j`, dot-product reductions
+  inside Arnoldi.
+
+## Open questions / out of scope
+
+- Flexible GMRES (FGMRES): variable right-preconditioner per Arnoldi step.
+  Separate slice — different Arnoldi invariant.
+- Choice of orthogonalization scheme (CGS / CGS2 / MGS / Householder) is
+  an L2 implementation axis, not an L1 axis; the L1 invariant
+  `V_m^T V_m = I_m` is identical across schemes (modulo floating-point
+  loss-of-orthogonality, which is a numerical-quality claim about the L2
+  realization, not about L1).
+- Block GMRES (multiple RHS): separate slice.
+- Adaptive restart-length policies: separate slice.
.
- Structural change: applied diff (89 lines); 2 rotation_claim(s).
## 2026-05-24 cycle-14 — forward gmres [L1→L2] — revise

- Synthesis: 5 rotation_claim(s); no diff applied
- Verdict: revise.
- Friction: diff-apply failed: git apply failed:
STDERR:
error: corrupt patch at line 143

DIFF:
--- /dev/null
+++ b/book/src/spec/slices/gmres.md
@@ -0,0 +1,142 @@
+# Slice: gmres
+
+GMRES (Generalized Minimal RESidual) for solving `A x = b` with a general
+(possibly non-symmetric, possibly indefinite) linear operator `A`. The
+slice covers right-preconditioned, restarted GMRES(m) with classical or
+modified Gram-Schmidt orthogonalization, and a flexible-preconditioner
+(FGMRES) variant. Left preconditioning and unrestarted GMRES are recovered
+as degenerate cases (restart = ∞; constructed preconditioner = identity
+or wrapped on the left).
+
+## L0 — sources
+
+Pending. Explorer has not yet landed L0 facts for this slice; this push
+establishes L1 and L2 forward from textbook GMRES (Saad & Schultz 1986;
+Saad, *Iterative Methods for Sparse Linear Systems*, ch. 6) so that
+downstream rotations have a target. L0 citations will be back-filled
+from `palace/` source once Explorer reaches this slice.
+
+## L1 — unified statement
+
+**Inputs.** Linear operator `A`, right-hand side `b`, initial guess `x0`,
+preconditioner operator `M` (constructed once at solve start —
+see [constructed-operators](../../concepts/constructed-operators.md)),
+tolerances `(rtol, atol)`, restart length `m`, max outer iterations.
+
+**Constructed operator absorbs variants.** The variant axes
+— preconditioner side (left / right / split), flexibility
+(fixed `M` vs. per-step `M_k`), and identity-vs-nontrivial — are absorbed
+into `M` at construction time. The per-step procedure calls `M.apply(v)`
+uniformly and does not re-inspect the variant. See
+[variant-absorption](../../concepts/variant-absorption.md).
+
+**Invariant.** GMRES(m) produces, at the end of each inner cycle, the
+iterate `x_m ∈ x_0 + K_m(A M, r_0)` (right-preconditioned Krylov
+subspace) that minimizes the Euclidean residual norm `‖b - A x‖` over
+that affine subspace. Equivalently: with `V_m` an orthonormal basis of
+`K_m(A M, r_0)` and `H̄_m` the `(m+1) × m` upper-Hessenberg matrix
+satisfying the Arnoldi identity `A M V_m = V_{m+1} H̄_m`, the iterate is
+`x_m = x_0 + M V_m y_m` where `y_m = argmin_y ‖ β e_1 - H̄_m y ‖_2` and
+`β = ‖r_0‖`.
+
+**Procedure (one inner cycle, length up to m).**
+
+1. Form initial residual `r_0 = b - A x_0`, `β = ‖r_0‖`, `v_1 = r_0 / β`.
+2. For `j = 1, …, m` (early-exit when the residual estimate meets
+   tolerance):
+   - Apply the operator chain to produce the next Krylov direction:
+     `w = A · M.apply(v_j)`.
+   - Orthogonalize `w` against `{v_1, …, v_j}` (the orthogonalization
+     variant — CGS / MGS / CGS2 — is bound at solver construction and
+     applied uniformly here), yielding the new Hessenberg column
+     and `v_{j+1}`.
+   - Maintain an incremental least-squares solution for the projected
+     subproblem `min_y ‖β e_1 - H̄_j y‖`, exposing the current residual
+     estimate.
+3. Form `x_m = x_0 + M.apply(V_m y_m)` and either return (converged /
+   max iters) or restart with `x_0 ← x_m`.
+
+**Termination.** `‖r_k‖ ≤ max(rtol · ‖b‖, atol)`, or outer iteration
+budget exhausted. The residual estimate from the projected least-squares
+is exact for the true residual norm up to orthogonalization quality;
+slices that need a guaranteed bound recompute `‖b - A x‖` explicitly at
+restart boundaries.
+
+## L2 — primitive composition
+
+Bound at solver construction (not re-inspected per step):
+- `M : LinOp` — the constructed preconditioner (absorbs side / flexibility).
+- `orth : OrthogonalizationStrategy` — CGS / MGS / CGS2, exposing
+  `orth.extend(V_j, w) → (h_col, v_next)` that returns the new Hessenberg
+  column and the next basis vector.
+- `lsq : ProjectedLeastSquares` — an incremental solver for
+  `min_y ‖β e_1 - H̄_j y‖` exposing `lsq.push(h_col) → residual_estimate`
+  and `lsq.solve() → y`. (The internal representation — Givens-rotated
+  QR of `H̄_j`, normal-equations, or otherwise — is L3 implementation
+  detail; L2 sees only `push` / `solve` / `residual_estimate`.)
+
+Per-step primitive chain (one Arnoldi step `j`):
+
+```text
+z_j      = M.apply(v_j)                       # apply_linop
+w        = A.apply(z_j)                       # apply_linop
+(h_j, v_{j+1}) = orth.extend(V_j, w)          # orthogonalization step
+ρ_j      = lsq.push(h_j)                      # incremental LS update,
+                                               # returns residual estimate
+```
+
+At cycle close (length-`k` cycle, either converged or restart):
+
+```text
+y        = lsq.solve()                        # k-vector
+u        = matvec(V_k, y)                     # linear combination of basis
+                                               # vectors: u = Σ y_i v_i
+δx       = M.apply(u)                         # apply_linop
+x        = axpy(1, δx, x_0)                   # x ← x_0 + δx
+```
+
+At cycle open:
+
+```text
+Ax_0     = A.apply(x_0)                       # apply_linop
+r_0      = axpy(-1, Ax_0, b)                  # r_0 ← b - A x_0
+β        = norm(r_0)                          # √dot(r_0, r_0)
+v_1      = scale(1/β, r_0)                    # axpy-family
+```
+
+The primitives invoked — `apply_linop`, `axpy`, `dot`, `norm`, `scale`,
+`matvec` (in the sense of a basis-times-coefficients linear combination)
+— are the standard support-operator vocabulary; orthogonalization itself
+is a slice-local concept (see below).
+
+## Open questions / out of scope
+
+- Choice of `orth` (CGS / MGS / CGS2) and its numerical-stability
+  trade-offs are bound at construction and not re-inspected; the
+  algebraic claim that all three produce the same L1 minimum-residual
+  iterate (up to round-off) is taken for granted here and is the subject
+  of a separate orthogonalization-strategy slice.
+- Happy breakdown (`h_{j+1,j} = 0`): treated as convergence (the Krylov
+  subspace is `A M`-invariant; the current `y` is exact). Spec'd in L1
+  as part of the early-exit path; mechanism for detection lives at L2
+  inside `orth.extend`.
+- L3 (global tensor-field form) and L4 (state-typed monadic form) are
+  pending; the projected least-squares state is the non-obvious piece
+  and may force an obstruction claim at L2→L3 (the Hessenberg column is
+  sequentially extended).
+
+## Concepts referenced
+
+- [apply_linop](../../concepts/apply_linop.md)
+- [axpy](../../concepts/axpy.md)
+- [dot](../../concepts/dot.md)
+- [constructed-operators](../../concepts/constructed-operators.md)
+- [variant-absorption](../../concepts/variant-absorption.md)
+
+Slice-local concept (to be extracted when a second slice needs it):
+`orthogonalization-strategy` — the CGS/MGS/CGS2 family as a uniform
+interface `extend(V, w) → (h_col, v_next)`. Likely shared with
+block-GMRES, Arnoldi eigensolvers, and FOM.
; Variant absorption via constructed M is claimed at all three levels, but FGMRES (flexible / per-step M_k) is a known counterexample to clean absorption: the L1 update formula x_m = x_0 + M V_m y_m is INCORRECT for FGMRES — flexible GMRES must store the preconditioned basis Z_m = [z_1, …, z_m] (with z_j = M_j v_j) separately because there is no single M to apply at cycle close. The cycle-close primitive chain ( u = matvec(V_k, y); δx = M.apply(u); x = axpy(1, δx, x_0) ) therefore does NOT have the same shape across variant values: fixed-M cycle close goes through M.apply once, flexible-M cycle close skips M.apply entirely and uses δx = matvec(Z_k, y). This is variant-absorption check (c) primitive-sequence-divergence, undeclared. Either declare flexible-M as a residual axis with its own cycle-close shape, or push back: introduce Z as an additional bound state in L1 (the 'preconditioned basis' stream) so the cycle-close primitive becomes δx = matvec(Z_k, y) uniformly (and fixed-M is the case Z_j = M.apply(v_j) recomputed-or-cached).; Prose-rotation-alignment is good (L1 says 'incremental least-squares update', not 'Givens'). However, the residual estimate ρ_j returned by lsq.push is the projected-LS residual, which is NOT the true residual ‖b - A x_j‖ when orthogonalization loses orthogonality — the L1 termination prose acknowledges this ('exact ... up to orthogonalization quality') but the L2 interface presents ρ_j as if it were the convergence-test input with no further qualification. The slice should either (a) make the residual_estimate's semantics part of the interface contract (it's the projected-LS residual, valid as a convergence proxy under maintained orthogonality), or (b) declare a separate true-residual recomputation primitive at restart boundaries (which the L1 prose hints at but L2 does not surface). Currently L2 under-specifies the contract.; Same issue as claim 1: the cycle-close chain u = matvec(V_k, y); δx = M.apply(u) is only valid for fixed-M. For FGMRES, δx = matvec(Z_k, y) directly with no M.apply, because each z_j was produced by a different M_j. The claim that the rotation is mechanical and one-to-one holds only after the L1 state schema is fixed to thread Z (see push-back on claim 1)..
- Structural change: none.
## 2026-05-24 cycle-13 — forward gmres [L0→L1] — pass

- Synthesis: 4 rotation_claim(s); diff applied
- Verdict: pass.
- Friction: diff-apply failed: git apply failed:
STDERR:
error: corrupt patch at line 159

DIFF:
--- /dev/null
+++ b/book/src/spec/slices/gmres.md
@@ -0,0 +1,212 @@
+# Slice: gmres
+
+Scope: GMRES and FGMRES iterative linear solvers (palace/linalg/iterative.{hpp,cpp}).
+Covers the restarted Arnoldi process with Givens-rotation-maintained least-squares
+residual, the three Gram-Schmidt orthogonalization variants (MGS, CGS, CGS2), and
+the GMRES/FGMRES split (fixed vs. variable preconditioner).
+
+## L0 citations
+
+- `palace/linalg/iterative.hpp:152-216` — `GmresSolver<OperType>` declaration
+- `palace/linalg/iterative.hpp:219-275` — `FgmresSolver<OperType>` declaration
+- `palace/linalg/iterative.cpp:227-241` — `GeneratePlaneRotation` (real / complex)
+- `palace/linalg/iterative.cpp:243-250` — `ApplyPlaneRotation`
+- `palace/linalg/iterative.cpp:252-283` — `InitialResidual`
+- `palace/linalg/iterative.cpp:285-303` — `ApplyBA`
+- `palace/linalg/iterative.cpp:305-325` — `OrthogonalizeIteration` (dispatch over MGS/CGS/CGS2)
+- `palace/linalg/iterative.cpp:489-518` — `GmresSolver::Initialize`
+- `palace/linalg/iterative.cpp:519-542` — `GmresSolver::Update`
+- `palace/linalg/iterative.cpp:544-706` — `GmresSolver::Mult`
+- `palace/linalg/iterative.cpp:708-731` — `FgmresSolver::Update`
+- `palace/linalg/iterative.cpp:733-870` — `FgmresSolver::Mult`
+- `palace/linalg/iterative.cpp:73-108` — `CheckDot` / norm reductions reused throughout
+- `palace/linalg/orthog.hpp:41-89` — Gram-Schmidt kernel called by `OrthogonalizeIteration`
+- `test/unit/test-orthog.cpp:75-103` — orthogonality invariant tested across MGS/CGS/CGS2
+
+## L1 form
+
+### State schema
+
+The solver's persistent configuration is
+
+    GmresState = {
+      max_dim   : Nat,                          -- restart length
+      gs_orthog : {MGS, CGS, CGS2},
+      pc_side   : {LEFT, RIGHT},                -- FGMRES fixes this to RIGHT
+      basis     : KrylovBasis                   -- (see concepts/krylov-basis.md)
+    }
+
+The `basis` bundle is the Synthesizer-introduced abstraction that packs the
+Arnoldi basis V, the upper-Hessenberg matrix H (column-major, leading dim
+max_dim+1), and the Givens-rotation least-squares state (s, cs, sn). FGMRES
+extends the bundle with a second basis Z storing preconditioned vectors:
+
+    FgmresState = GmresState with {
+      pc_side  := RIGHT,                        -- structurally fixed
+      basis_pc : KrylovBasis                    -- Z[k] = B_k · V[k]
+    }
+
+All entries of `basis` and `basis_pc` are ephemeral workspace: they are
+resized lazily by Initialize/Update and not part of the mathematical
+invariant.
+
+### Mathematical invariant
+
+After m Arnoldi steps from initial residual r₀ = M(b − A·x₀) (where M is the
+identity, left-preconditioner B, or right-preconditioner action encoded via
+the constructed preconditioned-operator — see L1 procedure below), the basis
+satisfies
+
+    Â · V_m  =  V_{m+1} · H̄_m,                  V_{m+1}^* · V_{m+1} = I,
+
+where Â is the preconditioned operator (the role played by `apply_op` below;
+the specific composition is a constructed-operator detail — see
+concepts/constructed-operators.md) and H̄_m is (m+1)×m upper-Hessenberg. The
+approximate solution at step m minimises the preconditioned residual norm
+over the affine Krylov subspace x₀ + V_m · ℝ^m; the minimisation reduces to
+a small (m+1)×m least-squares problem on H̄_m whose running solution is
+maintained incrementally in (s, cs, sn).
+
+### L1 procedure (uniform across GMRES and FGMRES)
+
+The variant axis (fixed vs. flexible preconditioner) is absorbed via
+constructed operators at solve start (concepts/constructed-operators.md):
+the caller binds `apply_op` and a `record_pc(j, v)` hook from the
+preconditioner-side configuration; the per-step procedure is then identical.
+
+    solve(A, B, b, x₀, cfg) :=
+      let (apply_op, residual_in, record_pc, reconstruct) =
+            build_preconditioned_ops(A, B, cfg.pc_side, cfg.variant)
+      in  outer_loop (x₀, it=0, restart=0)
+
+    outer_loop (x, it, restart) :=
+      let r        = residual_in(b, x, restart, cfg.initial_guess)
+      let beta     = norm(r)
+      let eps      = convergence_threshold(beta, b, B, cfg, restart, it)
+      if  beta < eps  then  return (x, converged=true, it)
+      let basis    = basis_with_first(r / beta, beta)
+      let (basis', j, converged) = inner_loop(basis, apply_op, record_pc, it, eps, cfg)
+      let x'       = reconstruct(x, basis', j)
+      if converged ∨ it+j+1 ≥ cfg.max_it  then  return (x', converged, it+j+1)
+      else  outer_loop (x', it+j+1, restart+1)
+
+    inner_loop (basis, apply_op, record_pc, it, eps, cfg) :=
+      iterate j = 0,1,2,... until termination:
+        let w           = apply_op(basis.V[j])         -- record_pc(j, ·) fires inside
+        let (basis_w, hcol) =
+              orthogonalize(cfg.gs_orthog, basis.V[0..j], w)
+        let h_norm      = norm(basis_w)
+        let v_next      = basis_w / h_norm
+        let basis'      = basis.append_column(v_next, hcol, h_norm)
+        let basis''     = basis'.update_least_squares(j)   -- incremental update
+        let beta_j      = basis''.residual_estimate(j)
+        let converged   = beta_j < eps
+        terminate when converged ∨ j+1 = cfg.max_dim ∨ it+j+1 = cfg.max_it
+
+### Variant absorption
+
+Per concepts/variant-absorption.md, the axes are:
+
+- **pc_side ∈ {LEFT, RIGHT, none}** × **flexible? ∈ {no (GMRES), yes (FGMRES)}**.
+  Absorbed via *constructed operators* (concepts/constructed-operators.md):
+  `build_preconditioned_ops` returns the tuple
+  (apply_op, residual_in, record_pc, reconstruct) wired for the active
+  combination.
+    - GMRES/none      : apply_op = A;        record_pc = noop; reconstruct = x + Σ s_k V_k
+    - GMRES/LEFT      : apply_op = B∘A;      record_pc = noop; reconstruct = x + Σ s_k V_k
+    - GMRES/RIGHT     : apply_op = A∘B;      record_pc = noop; reconstruct = x + B·(Σ s_k V_k)
+    - FGMRES (RIGHT,flex): apply_op = A∘B_j; record_pc = store B_j·V[j] in Z[j];
+                           reconstruct = x + Σ s_k Z_k
+  All four routes satisfy criteria (a), (b), (c) of variant-absorption.md:
+  the L1 invariant is uniform, the procedure mentions pc_side only inside
+  `build_preconditioned_ops` (single dispatch site), and the per-step
+  primitive sequence is identical.
+- **gs_orthog ∈ {MGS, CGS, CGS2}**. Absorbed *parametrically* — passed to
+  `orthogonalize`, which returns the same shape (hcol of length j+1, w
+  with the projection removed). The choice affects only the inner
+  primitive sequence of `orthogonalize` (a single MPI-reduce vs. two
+  reduces), not the GMRES procedure.
+- **restart vs. full**. Absorbed via the outer/inner split. A non-restarted
+  run is the special case max_dim ≥ max_it; the outer loop terminates after
+  one pass either way.
+- **initial_guess ∈ {true, false}**. Absorbed inside `residual_in`, which
+  takes `cfg.initial_guess` and the restart index and returns r;
+  downstream code does not re-inspect the flag.
+
+### Termination and outputs
+
+Outputs are (x_out, converged, iteration_count, final_residual_estimate).
+The least-squares state inside `basis` provides the cheap residual estimate
+|s_{j+1}| without an explicit matvec.
+
+### Open questions
+
+- No direct unit test for GmresSolver / FgmresSolver under test/unit/;
+  only configuration-level coverage via test-romoperator.cpp. (low)
+- max_dim defaults to max_it; potentially O(max_it²) memory for the V
+  basis when only max_it is set. Latent footgun or intentional? (low)
+- FgmresSolver inherits pc_side from GmresSolver and then asserts RIGHT;
+  the field is structurally dead. The L1 state schema above already
+  removes it from FgmresState. (medium — schema-level question, not
+  blocking the L1 form)
+- Forward to L2: the *incremental least-squares update* role named in
+  `inner_loop.update_least_squares(j)` is implemented at L2 via a Givens
+  QR maintained against the new Hessenberg column. That mechanism is
+  hidden from L1.
.
- Structural change: applied diff (158 lines); 4 rotation_claim(s).
## 2026-05-24 meta-review (cycles 10–12) — enacted

- Window: 3 cycles. Push breakdown: 3 FORWARD, 0 BACK, 0 SIDEWAYS. (Meta-Critic loosely called these "SIDEWAYS" — they're not; SIDEWAYS push count remains 0.)
- Cascade: 0 LOW; 3 MEDIUM plan items approved and enacted; 0 HIGH escalated.
- Plan items enacted: strengthened diff-hygiene checklist in `prompts/synthesizer.md` (cycle 12 corrupt-patch was recurrence #1); Critic check #11 + frictionless-pass sanity note in `prompts/critic.md` (covers setup-schema variant absorption + surfaces pass-without-exercise); "Lessons promotion" subsection added to `book/src/meta-reviews/index.md` (formalizes ad-hoc concept-promotion pattern from prior meta-reviews).
- First batch under apply-on-revise: 3 slice files landed on disk (orthog, divfree; chebyshev failed diff-apply, recoverable from episodic). Surface finally accumulating.
- Watch updates: diff-apply mismatch now at recurrence #1 (if #2 in cycle 13+, escalate to MCP file-creation tool); new "pass-without-exercise" watch from frictionless cycles; new "Meta-Critic SIDEWAYS terminology drift" observation (not a plan item).
- Full record: `book/src/meta-reviews/2026-05-24-cycles-10-12.md`.

## 2026-05-24 cycle-12 — forward chebyshev [L0→L1] — pass

- Synthesis: 3 rotation_claim(s); diff applied
- Verdict: pass.
- Friction: diff-apply failed: git apply failed:
STDERR:
error: corrupt patch at line 113

DIFF:
--- /dev/null
+++ b/book/src/spec/slices/chebyshev.md
@@ -0,0 +1,118 @@
+# Slice: chebyshev
+
+Chebyshev polynomial smoother applying `p_k(D^{-1} A)` to damp
+high-frequency error on an SPD operator with extracted diagonal
+preconditioner `D = diag(A)`. Used as the per-level smoother in
+geometric multigrid and distributive-relaxation preconditioners.
+
+Two polynomial variants are exposed, selected at construction:
+
+- **4th-kind** (Phillips & Fischer 2022): requires only `lambda_max`.
+- **1st-kind** (Adams-style): requires the spectral window
+  `[lambda_min, lambda_max]`.
+
+The variants share an outer Richardson-like residual/accumulator
+scaffold and differ only in the scalar recurrence that builds the
+polynomial. Variant absorption is via **constructed-operator**: the
+caller chooses 4th- vs. 1st-kind at construction, and the resulting
+smoother exposes a uniform `apply_linop` interface; the per-iteration
+procedure does not re-inspect the variant.
+
+## L1
+
+### State
+
+- Captured at `setup` (immutable through `apply_linop` calls):
+  - `A` — SPD operator (by reference).
+  - `dinv` — vector of `1 / diag(A)`, length `A.height`.
+  - `lambda_max` — scalar, scaled spectral upper bound.
+  - `lambda_min` — scalar, only for 1st-kind; from user `sf_min` or
+    Phillips & Fischer (2022) eq. 2.24 default
+    `1.69 / (order^{1.68} + 2.11*order + 1.98)`.
+  - `order`, `pc_it`, `variant ∈ {4th-kind, 1st-kind}` — fixed.
+- Ephemeral per `apply_linop` call: residual `r`, direction `d`
+  (both length `A.height`); workspace.
+
+### Setup (pure of `(A, sf_max[, sf_min], order, pc_it, variant)`)
+
+1. `dinv := reciprocal(extract_diagonal(A))`.
+2. `lambda_max := sf_max * spectrum_estimate(A, dinv)`, where
+   `spectrum_estimate` returns the dominant eigenvalue magnitude of
+   `D^{-1} A` via a Hermitian spectral-norm primitive (power
+   iteration; SLEPc when configured). See
+   `concepts/spectrum-estimate.md`.
+3. If `variant = 1st-kind`: also set `lambda_min` (from `sf_min` or
+   the default formula); precompute `theta := (lambda_max +
+   lambda_min)/2`, `delta := (lambda_max - lambda_min)/2`.
+
+### Apply (`apply_linop`: given rhs `x`, accumulator `y`, optional `initial_guess`)
+
+Repeat `pc_it` times the Richardson-like sweep:
+
+1. Compute residual: `r := x - A*y` (or `r := x`, `y := 0` on the
+   first iteration when `initial_guess = false`).
+2. Apply the order-`order` polynomial of `D^{-1} A` to `r`,
+   accumulating into `y`. The polynomial is a degree-`order`
+   parameterized recurrence:
+   - **Initial direction** (`k = 0`):
+     `d := alpha_0 * dinv .* r` for a variant-dependent scalar `alpha_0`.
+   - **Inner steps** (`k = 1 .. order - 1`):
+     `y := y + d`
+     `r := r - A*d`
+     `d := sd_k * d + sr_k * dinv .* r`
+     with variant-dependent scalars `(sd_k, sr_k)`.
+   - **Final update**: `y := y + d`.
+
+The polynomial coefficients `(alpha_0, sd_k, sr_k)` are determined
+by `variant` and the spectral bounds; their concrete recurrences are
+L2 detail (the closed-form `k`-indexed coefficients for 4th-kind and
+the three-term Chebyshev recurrence centered at `theta` with
+half-width `delta` for 1st-kind).
+
+`MultTranspose` aliases `Mult` under the symmetry assumption.
+
+### Operator-kind support
+
+Real (`Operator`) and complex (`ComplexOperator`) instantiations
+share the L1 procedure; the complex case uses `conj(dinv)` in the
+transpose path.
+
+## Consumers
+
+- `gmg.cpp` (geometric multigrid): per-level relaxation.
+- `distrelaxation.cpp` (distributive relaxation): smoother.
+
+The smoother is a leaf in the preconditioner stack: it consumes `A`
+(plus its diagonal) and produces a `Solver<OperType>` exposing
+`apply_linop`.
+
+## Open questions
+
+- No direct unit test under `test/unit/`; behavior exercised through
+  multigrid integration only.
+- `spectrum_estimate` has a build-flag-dependent backend (power
+  iteration vs. SLEPc); L2 unfold will need to acknowledge both.
+- MPI involvement is confined to `spectrum_estimate` (parallel norms
+  inside power iteration); the polynomial recurrence itself is
+  local.
+
+## Concept references
+
+- `concepts/apply-linop.md` — the apply interface.
+- `concepts/axpy.md`, `concepts/elementwise-product.md` —
+  primitives used by the inner recurrence.
+- `concepts/extract-diagonal.md`, `concepts/reciprocal.md` — setup
+  primitives.
+- `concepts/spectrum-estimate.md` — dominant-eigenvalue estimate.
+- `concepts/constructed-operators.md` — variant absorption route.
+- `concepts/variant-absorption.md` — invariant/procedural/primitive
+  axes.
.
- Structural change: applied diff (112 lines); 3 rotation_claim(s).
## 2026-05-24 cycle-11 — forward divfree [L0→L1] — pass

- Synthesis: 3 rotation_claim(s); diff applied
- Verdict: pass.
- Friction: none.
- Structural change: applied diff (122 lines); 3 rotation_claim(s).
## 2026-05-24 cycle-10 — forward orthog [L0→L1] — pass

- Synthesis: 1 rotation_claim(s); diff applied
- Verdict: pass.
- Friction: none.
- Structural change: applied diff (111 lines); 1 rotation_claim(s).
## 2026-05-24 meta-review (cycles 7–9) — enacted (with constructed-operators bonus)

- Window: 3 cycles. Push breakdown: 1 FORWARD, 2 BACK, 0 SIDEWAYS. Still no SIDEWAYS — same-slice grind continues (8 consecutive GMRES cycles).
- Cascade: 0 LOW; 3 MEDIUM plan items approved and enacted; 0 HIGH escalated; **plus** 1 user-introduced bonus concept (constructed operators).
- Plan items enacted: variant-absorption "Levels of absorption" section (invariant / procedural / primitive-sequence) in `book/src/concepts/variant-absorption.md`; prose-rotation alignment subsection in `prompts/synthesizer.md`; new Critic check #10 in `prompts/critic.md`. Bonus: new `book/src/concepts/constructed-operators.md` peer concept with cross-refs from `rotation.md`, `variant-absorption.md`, and both role prompts.
- Recurring patterns: rotation-as-renaming did **not** recur this batch (recur-#2-escalate trigger still armed, not fired). Variant absorption recurred for the second time within its own concept's life on the same slice (cycle 7 + cycle 9) — strengthened the fix per protocol; cross-slice recurrence (10+) would escalate to High.
- New watch item: same-slice grind (8 consecutive GMRES cycles) is structurally blocking the Phase 6 SIDEWAYS criterion. Human should consider seeding a second slice next batch.
- Full record: `book/src/meta-reviews/2026-05-24-cycles-7-9.md`.

## 2026-05-24 cycle-9 — back gmres — revise

- Synthesis: 1 rotation_claim(s); no diff applied
- Verdict: revise.
- Friction: The variant absorption is mostly clean, but the update-basis selector `W ∈ {V, Z}` driven by `side` is a conditional smuggled into the invariant and the solution-update step. It surfaces as two places in L1 where `side` is re-inspected (Arnoldi step 1 AND solution update step 3), which is a hint that the Z/V distinction is not fully absorbed. Also, the `M : j → LinearOperator` unification of GMRES/FGMRES is asserted but the spec then says `Z[j] = M_j^{-1} V[j]` only for 'right/flexible' — there is no separate FGMRES parameter, but the spec still distinguishes flexible behavior textually..
- Structural change: none.
## 2026-05-24 cycle-8 — back gmres — revise

- Synthesis: 1 rotation_claim(s); no diff applied
- Verdict: revise.
- Friction: The rotation does perform genuine state-hiding (Givens sequence, s vector, Hessenberg storage, index j → hidden behind 'maintain QR factorization … incrementally') so it passes the rotation-quality check. However, L1 step 2 still mentions 'maintaining a QR factorization of \bar H_m via Givens rotations' and 'read off the last entry of the rotated right-hand side' — this is L0 machinery leaking through. A cleaner L1 would say only 'solve the least-squares problem incrementally, with the current residual norm available without forming y_m' and defer Givens to L2. As-is the rotation is correct but the L1 prose is half-rotated..
- Structural change: none.
## 2026-05-24 cycle-7 — forward gmres [L1→L2] — revise

- Synthesis: 3 rotation_claim(s); no diff applied
- Verdict: revise.
- Friction: The L1→L2 rotation for iterate update treats the right-precond unwrap as a special-case extra M.apply tacked onto the gemv, while FGMRES is the 'clean' path with no extra apply. This is a parametric variant the slice claims is absorbed (W_m = V_m vs W_m = Z_m), but the unwrap step breaks the unification: for GMRES-right you do gemv then M.apply; for FGMRES you do gemv only; for GMRES-left you do gemv only but the iterate is in preconditioned coordinates. The 'one canonical primitive sequence per parameter value' framing the synthesizer claims is therefore three sequences, not two, and the side=right-fixed-M case is the labored one..
- Structural change: none.
## 2026-05-24 meta-review (cycles 4–6) — enacted (with carry-through revision)

- Window: 3 cycles. Push breakdown: 1 FORWARD, 2 BACK, 0 SIDEWAYS. **First BACK pushes of the loop.**
- Cascade: 0 LOW; 4 MEDIUM plan items approved (3 as-proposed, 1 modified per user feedback); 0 HIGH escalated.
- Plan items enacted: claim granularity + canonicalization in `prompts/synthesizer.md`; rotation self-check (pre-emit) **with carry-through allowance** in `prompts/synthesizer.md`; new `book/src/concepts/variant-absorption.md` + Synthesizer reference + Critic check #9; bonus: new "Carry-through" section in `book/src/concepts/rotation.md` per user feedback.
- Recurring patterns: rotation-as-renaming **recurred once** (cycle 4 from cycle 3) — producer-side check added per protocol; if it recurs again, escalate to High. NEW watch: date drift between Meta-Critic JSON (hallucinated 2026-06-14) and actual run date (2026-05-23/24 UTC).
- Cleared from watch list: Meta-Critic file-path drift (paths correct this round).
- Full record: `book/src/meta-reviews/2026-05-24-cycles-4-6.md`.

## 2026-05-24 cycle-6 — back gmres — revise

- Synthesis: 2 rotation_claim(s); no diff applied
- Verdict: revise.
- Friction: The L0→L1 rotation does real work (state hiding: V, H, s/sn/cs, the enum dispatch, and the Givens accumulator are all hidden behind 'four concerns'), so it is a genuine rotation under criterion (a). However, the FGMRES paragraph is bolted onto the end of L1 rather than absorbed: the rotation 'GMRES is x_m = x_0 + V_m y_m' has to be locally patched to 'x_m = x_0 + Z_m y_m' for FGMRES, which suggests the L1 form should have been stated as 'x_m = x_0 + W_m y_m where W_m is the *update basis* (= V_m for GMRES, = Z_m for FGMRES) and A W_m = V_{m+1} H̄_m'. That unified form would make FGMRES a parameter choice rather than a variant..
- Structural change: none.
## 2026-05-24 cycle-5 — back gmres — revise

- Synthesis: 1 rotation_claim(s); no diff applied
- Verdict: revise.
- Friction: The L1 description threads V, H, g, cs, sn, x, j all together through a single monolithic step 2 loop. This is fine for L1 (rotation criterion (a) state-hiding will happen at L1→L2 by introducing an arnoldi_step primitive that hides H/cs/sn/g update), but the current Procedure is written in a way that fuses (i) Arnoldi orthogonalization, (ii) Givens update, (iii) residual monitor into one numbered list. Consider whether step 2.5 and 2.6 should be presented as a separable 'projected-problem update' sub-procedure even at L1 — this would make the L1→L2 boundary cleaner. Not blocking, but worth flagging..
- Structural change: none.
## 2026-05-24 cycle-4 — forward gmres [L1→L2] — revise

- Synthesis: 4 rotation_claim(s); no diff applied
- Verdict: revise.
- Friction: Claim 2 mixes two distinct primitives (trsv_upper and gemv) into a single L1→L2 edge and then immediately equivocates in the justification ('whether the gemv is realized as one BLAS-2 call or k axpys is a transparent optimization'). This is the friction signal: if the gemv ↔ k-axpys choice is transparent, then the L2 form is not canonical — two different L2 expressions denote the same semantics. Either pin gemv as the L2 primitive and demote axpy-panel to L3 implementation, or split the solution-assembly rotation into its own edge with an explicit primitive choice.; The L1→L2 Arnoldi rotation is essentially a renaming: each L1 line maps to a single named BLAS primitive with identical sequentiality and identical threaded state (w, V columns, H column). Per rotation.md, a rotation should (a) hide state, (b) admit coarser substitution, or (c) compress threaded state. None of these holds here — w is still threaded, the MGS sequential dependency is still exposed, H[i,j] is still indexed elementwise. The genuine rotation would be to an `arnoldi_step(A, V, H, j) -> v_{j+1}` primitive that hides the index/loop and admits MGS↔CGS2 substitution at the L2 grain. As written, L2 is L1 with BLAS names sprinkled in..
- Structural change: none.
## 2026-05-24 meta-review (cycles 1–3) — enacted

- Window: 3 cycles. Push breakdown: 3 FORWARD, 0 BACK, 0 SIDEWAYS.
- Cascade: 1 LOW applied; 3 MEDIUM plan items approved and enacted; 0 HIGH escalated.
- Plan items enacted: diff-hygiene note in `prompts/synthesizer.md`; slice-scoping rule + claim coverage in `book/src/spec/index.md`; rotation_claim coverage requirement; new `book/src/concepts/rotation.md` (rotation quality criteria) + Critic verification check #8.
- Recurring patterns: none yet (first meta-review). Watch list: Meta-Critic file-path drift, rotation-quality false positives.
- Full record: `book/src/meta-reviews/2026-05-24.md`.

## 2026-05-24 cycle-3 — forward gmres [L1→L2] — revise

- Synthesis: 0 rotation_claim(s); no diff applied
- Verdict: revise.
- Friction: The L2 'Per-iteration composition' block is essentially the L1 inner loop rewritten with primitive names — the rotation L1→L2 collapses to a renaming rather than a genuine algebraic compression. Symptom: the outer composition still has to thread V, H, g, cs, sn through `arnoldi_with_givens` as an opaque bundle, and the per-iteration block exposes index arithmetic (H[0..j+1, j], V[:,0..j]) at L2..
- Structural change: none.
## 2026-05-24 cycle-2 — forward gmres [L0→L1] — pass

- Synthesis: 0 rotation_claim(s); diff applied
- Verdict: pass.
- Friction: diff-apply failed: git apply failed:
STDERR:
error: corrupt patch at line 118

DIFF:
--- a/book/src/spec/slices/gmres.md
+++ b/book/src/spec/slices/gmres.md
@@ -0,0 +1,166 @@
+# gmres
+
+## L1 — Mutation-level decomposition
+
+### State (per solver instance, all `mutable`, persisted across `Mult` calls)
+
+- `V`: `std::vector<VecType>` of length `max_dim+1` — Krylov basis vectors. Each entry sized to `A->Height()` on demand. `V[j+1]` with `Size()==0` indicates not-yet-allocated.
+- `H`: packed Hessenberg matrix, column-major, leading dimension `max_dim+1`. Column `j` lives at `H.data() + j*(max_dim+1)`, rows `0..j+1`.
+- `s`: least-squares RHS, length up to `max_dim+1`. After step `j`, `|s[j+1]|` is the recursion-estimated residual norm.
+- `cs[0..max_dim)`: real cosines of accumulated Givens rotations.
+- `sn[0..max_dim)`: scalar (real or complex) sines of accumulated Givens rotations.
+- `r`: residual scratch, length `A->Height()`. Doubles as preconditioner-apply scratch.
+- (FGMRES only) `Z`: second basis of length `max_dim+1`, storing `B V[j]` per step.
+
+### Configuration (immutable post-construction)
+
+- `max_dim`: restart dimension (GMRES(m), m = max_dim). Defaults to `max_it` on first `Initialize`.
+- `max_it`: global iteration cap across restart cycles.
+- `rel_tol`, `abs_tol`: convergence thresholds; effective `eps = max(rel_tol * initial_res, abs_tol)`.
+- `gs_orthog ∈ {MGS, CGS, CGS2}`: orthogonalization variant.
+- `pc_side ∈ {LEFT, RIGHT, NONE}`: preconditioner side. FGMRES forces RIGHT.
+- `initial_guess`: if false, `x` is zeroed before solving.
+
+### Mutation: `Initialize()` — lazy allocation
+
+- **Pattern**: in-place overwrite (idempotent no-op on matching sizes).
+- First call: size `V` to `max_dim+1`; allocate `V[0..init_size)` at `A->Height()`, where `init_size=5`; size `s,cs,sn` to `min(init_size+1, max_dim+1)`; size `H` to `(max_dim+1) * min(init_size, max_dim)`.
+- Subsequent calls: assert operator height and `max_dim` unchanged; otherwise no-op.
+- Citations: `palace/linalg/iterative.cpp:488–515`.
+
+### Mutation: `Update(j)` — incremental growth
+
+- **Pattern**: in-place overwrite, called from Arnoldi inner loop when `V[j+1].Size()==0`.
+- Grow basis: allocate `V[j+1 .. min(j+1+add_size, max_dim+1))` at `A->Height()`, `add_size=10`.
+- Grow `H` to `(max_dim+1) * min(j+1+add_size, max_dim)` entries.
+- Grow `s,cs,sn` to `min(j+2+add_size, max_dim+1)`.
+- Citations: `palace/linalg/iterative.cpp:518–541`.
+
+### Mutation: `Mult(b, x)` — outer restart loop
+
+- **Pattern**: complex; coordinates Arnoldi inner loop, restart, and convergence.
+- Pseudocode (per restart cycle, indexed by `restart`):
+  1. `InitialResidual(pc_side, A, B, b, x, r, V[0])` populates `r`:
+     - `LEFT`: `r = B(b - A x)` (or `B b` if `!initial_guess`).
+     - `RIGHT`/`NONE`: `r = b - A x` (or `b` if `!initial_guess`).
+  2. `beta = ||r||_2` (MPI-collective via `linalg::Norml2`).
+  3. On `restart==0`: `initial_res = beta`; `eps = max(rel_tol*initial_res, abs_tol)`.
+  4. On `restart>0`: compare `beta` (recomputed) to `s[0]` from previous cycle; warn if divergence exceeds threshold (residual recursion drift).
+  5. If `beta < eps`: set `converged=true`, break outer loop.
+  6. `V[0] = r / beta`; zero `s`; `s[0] = beta`.
+  7. **Arnoldi inner loop** for `j = 0, 1, ...` (see below).
+  8. On inner-loop exit (any reason): **solution reconstruction** (see below).
+  9. If `converged`, break outer; else next restart cycle.
+- Outer termination: `it >= max_it` OR `converged`.
+- Citations: `palace/linalg/iterative.cpp:543–705`.
+
+### Mutation: Arnoldi inner step (per `j`)
+
+- **Pattern**: complex (basis extension + Hessenberg column build + Givens QR update).
+- (a) `w := V[j+1]`; if `w.Size()==0` call `Update(j)`.
+- (b) **Matvec with preconditioner dispatch** via `ApplyBA(pc_side, A, B, V[j], w, r)`:
+  - `LEFT`: `r = A V[j]; w = B r` → Krylov basis for `B A`.
+  - `RIGHT`: `r = B V[j]; w = A r` → Krylov basis for `A B`.
+  - `NONE`: `w = A V[j]`.
+  - FGMRES (RIGHT only): `Z[j] = B V[j]; w = A Z[j]` — `Z[j]` is preserved, not scratch.
+- (c) **Orthogonalize** `w` against `V[0..j]` via `OrthogonalizeIteration(gs_orthog, comm, V, w, Hj, j+1)`:
+  - `MGS`: sequential — for `k=0..j`: `Hj[k] = <V[k], w>` (MPI GlobalSum per `k`); `w -= Hj[k] V[k]`. `j+1` collectives.
+  - `CGS`: batched — `Hj[0..j] = V[0..j]^H w` with one MPI GlobalSum over `j+1` dot products; then `w -= sum_k Hj[k] V[k]`.
+  - `CGS2`: CGS followed by one refinement pass, accumulating into `Hj`.
+- (d) `Hj[j+1] = ||w||_2` (MPI-collective); `w /= Hj[j+1]`. This finalizes column `j` of `H`.
+- (e) **Apply previous rotations to new column**: for `k=0..j-1`: `ApplyPlaneRotation(Hj[k], Hj[k+1], cs[k], sn[k])`.
+  - Real: `(dx,dy) ← (cs*dx + sn*dy, -sn*dx + cs*dy)`.
+  - Complex: `(dx,dy) ← (cs*dx + sn*dy, -conj(sn)*dx + cs*dy)`.
+- (f) **Generate new rotation** zeroing subdiagonal: `GeneratePlaneRotation(Hj[j], Hj[j+1], cs[j], sn[j])` (LAPACK `lartg`-style, scaled to avoid over/underflow).
+- (g) **Apply new rotation** to `Hj[j..j+1]` and to `s[j..j+1]`. Now `Hj[j+1] = 0` (triangularized) and `|s[j+1]|` = current minimum-residual norm. Set `beta = |s[j+1]|`.
+- (h) Increment `it`.
+- (i) **Inner termination check**: `converged := (beta < eps)`; break if `converged OR j+1 == max_dim OR it == max_it`.
+- Citations: `palace/linalg/iterative.cpp:227–326, 562–611, 653–683`; `palace/linalg/orthog.hpp:41–88`.
+
+### Mutation: solution reconstruction (on inner-loop exit)
+
+- **Pattern**: accumulator (back-substitution + linear combination).
+- Let `j_final` be the index at break. Solve `R y = s` in place, where `R` is the upper-triangular part of `H[0..j_final+1, 0..j_final]`:
+  ```
+  for i = j_final down to 0:
+      s[i] /= H[i,i]
+      for k = 0 .. i-1:
+          s[k] -= H[k,i] * s[i]
+  ```
+- Basis combination:
+  - `LEFT` or `NONE`: `x += sum_{k=0..j_final} s[k] * V[k]`.
+  - `RIGHT` (GMRES): `r = sum_{k=0..j_final} s[k] * V[k]`; `V[0] = B r` (scratch reuse); `x += V[0]`.
+  - `RIGHT` (FGMRES): `x += sum_{k=0..j_final} s[k] * Z[k]` — direct, no second `B` apply.
+- Citations: `palace/linalg/iterative.cpp:613–651, 734–866`.
+
+### FGMRES delta from GMRES
+
+- Adds second basis `Z` of size `max_dim+1`, allocated alongside `V` in `Initialize`/`Update`.
+- Forces `pc_side = RIGHT`.
+- Arnoldi step (b) saves `Z[j] = B V[j]` (not discarded as scratch).
+- Initial residual uses `Z[0]` as buffer.
+- Solution reconstruction sums `s[k] Z[k]` directly into `x` (rationale: with a variable preconditioner, the basis for `A B` would not be recoverable by reapplying `B` to `V`).
+- Citations: `palace/linalg/iterative.cpp:734–866, 877–880`.
+
+### Type instantiation
+
+- `GmresSolver<OperType>`, `FgmresSolver<OperType>` explicitly instantiated for `OperType ∈ {Operator, ComplexOperator}`.
+- `ScalarType = double` or `std::complex<double>` via `IterativeSolver` typedef; `RealType = double` (so `cs` is always real, `sn` follows `ScalarType`).
+- Complex specialization touches: `GeneratePlaneRotation`/`ApplyPlaneRotation` (conjugation in `dy` update); `InnerProductHelper` (Hermitian inner product, order-sensitive).
+
+### Open questions (deferred)
+
+- No dedicated unit test for `GmresSolver`/`FgmresSolver` under `test/unit/`; restart/Givens/back-sub paths covered only implicitly via `test-romoperator.cpp` configured-KSP path.
+- `Update` clamp behavior at `j+1+add_size > max_dim`: `needed_cols` clamps to `max_dim` while loop writes column `j ≤ max_dim-1`; likely safe by the `j+1==max_dim` break but un-audited.
.
- Structural change: applied diff (117 lines); 0 rotation_claim(s).
## 2026-05-24 cycle-1 — forward cg_solver_integration [L0→L1] — revise

- Synthesis: 1 rotation_claim(s); no diff applied
- Verdict: revise.
- Friction: The slice mixes three distinct concerns at L1: (a) top-level ProblemType dispatch to BaseSolver subclasses, (b) IoData DEFAULT→CG resolution, (c) ConfigureKrylovSolver/BaseKspSolver composition. The fact that the middle link (driver Solve() → BaseKspSolver construction) is unverified and left as an open question suggests this slice is trying to span too much. The 'end-to-end linkage' diagram has a '(per driver) constructs BaseKspSolver' step that is hand-waved..
- Structural change: none.
