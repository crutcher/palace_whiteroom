---
verifies: ../REPORT.md
critiqued_at: 2026-06-07T233000Z
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
overall_status: ready
---

# META: verification of synthesis-iteration-library-defs (Wave-2 iteration library def bodies)

## Critique

### Checks run

**citation-validity** — pass. The report's claims are anchored to the authoritative L4 chapter bodies it renders, and the cited ranges resolve and back the claims. Spot-checked: `iterate-while.md:38-43` is indeed the Solve-threaded signature; `:64-90` the two small-step rules; `:92-98` the `iterate_while_pure` sugar — all faithfully rendered. `krylov-step.md:94-116` is the Form-A dataflow body (rendered verbatim in structure incl. the `optionally_apply_auxiliary` / `krylov_update` / `derived_views` / `modify (it+1)` sequence); `:129-199` is the CG Form-B worked example. `chebyshev.md:152-194` is the `apply` body; `:228-245` the `setup` body; `:299-301` the transpose triviality. Clustering-type schemas trace to `concepts/krylov.md:36-43,58-67`, `concepts/step-outputs.md`, `concepts/prev-carry.md`. This is an implementation-VIEW chapter that re-cites no new L0 (correctly — it links to the L4 chapters, which themselves carry the L0 anchors), so the citation surface is the set of `../L4/<op>.md` back-links, all of which exist on disk. No `verified_against:` block is present (not a lowering-verifier audit), so that sub-check no-ops.

**surface-or-evidence** — pass. This is the SYNTHESIS implementation-rendering kind: its "evidence" is the authoritative L4 chapter body it renders plus the back-links to it, exactly as the §SYNTHESIS directive prescribes (link-to-authoritative, render-the-code-form). Every rendered def carries a `reference`-class back-link to its `../L4/<op>.md` home; the laws/semantics are NOT restated (the report explicitly says "the laws/semantics live in that chapter, not here"). Record-definition sub-check: the chapter renders three records (`Krylov`, `StepOutputs`, `PrevCarry`) plus the inline `CgState` and `ChebOp`/`ChebSim` types. Each has a definition home — the three clustering types link to their `concepts/<record>.md` authoritative pages (which exist and are `firm`), and the inline `CgState`/`ChebOp` types are rendered with full field schemas in-chapter (they are the synthesized type-def form, consistent with the type-placement rule). No record is described only by use.

**rotation-quality** — pass (no-op for kind, with the substantive fidelity-spot-check performed and clean). A Synthesis library chapter rotates nothing — it recomposes/renders already-firm L4 vocabulary as code (analogous to the feature-surface no-op). The KEY obligation per the dispatch was the FIDELITY of the rendered bodies to their L4 ground truth; I spot-checked three:
- `iterate_while` (report :217-229) vs `iterate-while.md` small-step rules (:80-98): faithful — the `if cont a then do { step; recurse; pure (cons-extras) } else pure {final_state, []}` shape matches the Solve-threaded reduction rule exactly, and `iterate_while_pure` (:227-229) matches the §Semantics sugar `(iterate_while a p (\x -> pure {state: f x})).final_state`.
- `krylov_step` Form A (report :291-307) vs `krylov-step.md:94-116`: faithful — the five-group dataflow (`apply_linop` → `optionally_apply_auxiliary` → `krylov_update` → `derived_views` → `modify (it+1)` → `pure {krylov, outputs}`) is line-for-line the L4 body, with the auxiliary-stage branch comment correctly absorbed.
- `chebyshev` `apply`/`sweep` (report :409-444) vs `chebyshev.md:152-194`: faithful — the nested `iterate_while_pure` folds with step-count predicates (`s.it <= op.pc_it`, `c.k <= op.order - 1`), the `where`-clause `sweep`, the `initial_guess` first-sweep branch, and the field-algebra operators (`.*.`, `.+.`, `.-.`, `.*`, `α₀`) are preserved verbatim. `setup` (:389-404) matches `chebyshev.md:228-245` including the `sf_min_eff` fallback formula.

**variant-axis-coverage** — pass (no-op for kind). A Synthesis library chapter has no variant axes of its own; the axes live in the rendered operators' own L4 chapters (krylov-step's six axes, chebyshev's two). The rendering correctly surfaces both `krylov-step` forms (A branch-in-body, B first-iteration-unrolled) and both chebyshev kinds (via `scalars4`/`scalars1` + the `Variant` type), so no axis is hidden in the render.

**cross-reference-integrity** — pass. All `[link]` targets resolve: the four `../L4/<op>.md` operator chapters exist; the eight `concepts/*.md` reference edges (`krylov`, `step-outputs`, `prev-carry`, `sim-state`, `op-params`, `solve-monad`, `first-iteration-unrolling`, `derived-view-hoisting`) all exist on disk. The forward references to sibling synthesis libraries (`./types.md`, `./data-algebra.md`, `./coordination.md`, `./index.md`) are Wave-1/sibling-wave chapters not yet on disk — these resolve only after the rest of the Synthesis Part lands; flagged below as a sequencing dependency, not a broken-link failure (the report correctly scopes SUMMARY.md wiring to the shell). The firm-body-inside-fence guard does not apply — this is a `navigational-container`, not a `firm` chapter claim.

**edge-label-fidelity** — pass. No L_{n+1}→L_n edge labels are carried; all frontmatter edges are `reference`-class (implementation-VIEW links to authoritative chapters), which the report asserts and which I confirm — there are no `depends-on`/`lowers-to`/`composes` edges in the proposed frontmatter. The kernel-boundary `## Kernel boundaries` section correctly defers `#extern` placement to the owning libraries (`data-algebra`/`coordination`) rather than mis-placing it here.

**plan-kind-consistency** — pass. Declared kind is `navigational-container` (synthesis library, def bodies rendered); content shape matches — rendered def bodies + clustering-type renderings + a kernel-boundaries section, no rank claim, no algebraic-law restatement. The `status: stub` → `navigational-container` flip is consistent with the Wave-1→Wave-2 transition (shell was the stub; body is now rendered). No firm-claim-with-placeholders mis-classification.

**skill-uptake-survey** — pass (telemetry). No dedicated Synthesis-rendering skill exists yet; the report invokes the §SYNTHESIS directive conventions directly (topological order, `where`-clauses, code-doc blocks, `$`-sigil-fence). The KaTeX `$`-sigil-fence rule is honored: all pseudocode carrying `$S`/`$V` sigils is inside ` ```text ` fences (the report explicitly confirms this and I verified the rendered blocks are fenced). No skill gap worth flagging.

### Issues found

No blocking or warning-level issues. Three sub-threshold observations recorded for the integrator/repairer (all non-blocking, none changing a check verdict):

1. **`cg_solve` Form-B call shape diverges from `krylov-step.md`'s worked example — but in the CORRECT direction (it resolves an inter-chapter inconsistency).** The report's `cg_solve` (CYCLE.md:362-368) calls `iterate_while_with_prev` with the canonical 4-arg order `(boot, init, steady, cont)` matching the authoritative `iterate-while-with-prev.md:44-49` signature. The `krylov-step.md:192-197` worked example uses an OLDER, inconsistent call shape `iterate_while_with_prev s1 s0.beta (cont) (steady)` (init, prev, cont, steady — a 4-arg form that does not match its own combinator's signature chapter). The report's rendering is faithful to the combinator's canonical signature, not to the stale krylov-step worked-example call. This is the report correctly rendering against the load-bearing signature source; the divergence is a fidelity IMPROVEMENT, not a drift. (Drive-by: the `krylov-step.md:193` worked-example call shape is itself stale vs `iterate-while-with-prev.md` — a candidate for a future same-layer-cross-cutter note, out of this report's scope.)

2. **The `krylov_update` / `op.orthog` / `derived_views` deep-link-vs-inline question (CYCLE.md Open-questions:470) is a genuine, acceptably-flagged judgment call, not a gap.** The §SYNTHESIS directive says deep-linked-UNCHANGED lower artifacts are rendered inline. Here the report renders `krylov_update`/`optionally_apply_auxiliary`/`derived_views` as named helper calls with a link-and-comment rather than inlining the per-slice L1-primitive sequence — justified because (a) the L4 chapter itself (`krylov-step.md:107`) keeps them as named calls and defers primitive enumeration to L2 (the per-slice CG/GMRES bundle update genuinely differs), and (b) the concrete CG primitive sequence IS already exhibited inline in the Form-B `cg_steady_step` render. This is a defensible reading of "unchanged" (the abstract named-helper IS the L4 form here); the flag-for-Wave-3 disposition is appropriate. Not a fidelity failure.

3. **Sequencing dependency: the `edit:` block's `[old]` payload is the un-landed Wave-1 shell, and the file does not yet exist on disk** (no `book/src/synthesis/` directory; SUMMARY.md has no synthesis entries). The report explicitly handles both apply-paths (shell-landed-first → apply the `[old]→[new]` diff; shell-not-landed → apply as full new file) in Open-questions:472. The forward `reference` edges to `synthesis/types`, `synthesis/index`, `data-algebra`, `coordination` will only resolve once those sibling chapters land. This is a Wave-ordering reconciliation for the integrator, not a content defect — recorded so integrator-per-report applies the correct path and does not flag the not-yet-resolving sibling links as broken at apply time.

(Cosmetic, noted by the report itself and not a finding: ASCII-ized `alpha`/`beta` field names in the rendered `Krylov_CG` vs the unicode `α`/`β` in `concepts/krylov.md` — a faithful code-rendering choice; and the unicode `α₀`/`.*.` operators preserved verbatim from `chebyshev.md` inside `text` fences.)
