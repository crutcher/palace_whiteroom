# Methodology — Goal & Flow

> **⟢ NON-AUTHORITATIVE — synthesized descriptive view; a review point, not a source.**
>
> This chapter is a **synthesized mirror** of the project's emergent goal and the
> process that pursues it. It is **not** a directive source. It is synthesized FROM
> the authoritative sources — `CLAUDE.md` (repo root), `METHODOLOGY-REDIRECT.md`
> (the 2026-06-01 vocabulary-shift redirect), the project memory, and
> `scaffolding/priorities.md` (the plan) — plus the emergent state of the artifact.
>
> **If this chapter contradicts any of those sources, the source wins and this
> chapter is corrected.** A contradiction surfacing here is a *drift signal*, not a
> decision to adjudicate. Read this chapter to orient; read the sources to act.
>
> **Ownership:** this chapter is seeded by `layer-intro-author`; after the seed,
> **ownership transfers to the `meta-phase`**, which refreshes it each batch from the
> authoritative sources. It exists to give the human a periodic review window onto the
> integrated goal as it is understood at the time of writing.

## GOAL — what the book is for

The artifact is an **incremental stack of representations** that lifts AWS Labs
**Palace** — a C++/HPC finite-element electromagnetic simulator that evolves fields
by array iteration with in-place mutation — into a **citation-grounded, layered
specification**. **No port is produced.** The output is the specification; a separate
downstream effort uses it to build burn components.

### The L4→L0 impedance-matching stack

The stack is a sequence of five representations, each re-expressing the one below it
after rotating **one specific impedance** — a single mismatch between Palace's
HPC-mutation cost model and an immutable-tensor, monadic, graph-evaluated host. Each
rotation is explicitly stated and verified.

- **L0** — cited Palace/MFEM source ranges. **Ground truth.**
- **L1** — *mutation rotation*. Source operations re-expressed as pure functions.
- **L2** — *fusion rotation*. L1 unfolded back into composition of base algebraic
  primitives; transparent HPC tricks (fusion, tiling, packing) erased to their
  unfolded form, load-bearing numerical tricks preserved as explicit claims.
- **L3** — *iteration rotation*. Per-step bodies re-expressed as global tensor-field
  operations where the iteration permits; where a loop genuinely resists the rotation,
  the **obstruction is recorded** (a `partial-obstruction` or `sequential-obstruction`
  finding) rather than forced.
- **L4** — a small, formally-defined **graph-evaluation calculus**. Vocabulary, not
  architecture: high-order combinators, state monads, immutable tensors.

Between adjacent layers, **lowering layers** (`L_{n+1} > L_n`) describe the rewrite
themes that take an `L_{n+1}` form into its `L_n` form, batched by theme rather than
edge-by-edge.

### L4 is the outward backend-lowering feature surface

L4 is **the feature surface** of the specification. Its semantics are chosen to align
with the external targets the downstream effort lowers *toward* — GPU-tensor and
tensor-accelerator backends, and distributed backends. Because L4's vocabulary matches
those backends, L4 is the natural surface from which to lower outward.

The load-bearing consequence: **every in-scope feature must reach L4.** This is not
only the solver pipelines — the **FE-assembly / FE-space / mesh-construction** half of
Palace is equally in scope and must reach L4 too. A feature stranded at a lower layer
is a hole to close. (NO-L2-floor warrants and similar lower-layer "this needs no
intermediate entry" judgments govern only the *downward* mirror question between
adjacent lower layers; they never excuse a feature from reaching L4.)

### The shape of the stack: vocabulary shifts, not a rectangular projection

Climbing one layer changes **both the representation and the component vocabulary** —
different named operators, different combinators, different semantic organization at
each level, **by design**. The stack is a sequence of **genuine representational +
vocabulary shifts**, not a rectangular projection in which every layer carries the same
named operators as its neighbor.

This shape is load-bearing, and it follows three principles:

1. **Each layer is complete, concise, and correct *in itself*.** A layer is a
   self-contained representation in its own vocabulary. The **conciseness** constraint
   is the engine of the methodology: a layer forced to express itself concisely is
   forced to factor out **in-layer utility combinators** (e.g. `linear_combination`
   over the `axpy`/`axpby`/`scal` family; `inner_product` over the `dot`/`nrm2`
   family). The combinator is the layer's entry; its specializations are notes *under*
   it — not standalone mirrored base-form entries beside it.

2. **Lowerings are translations, not renames.** Each `L_{n+1} > L_n` lowering is itself
   complete, concise, and correct, and it shows how a concise higher-layer form
   **reorganizes** into the concise lower-layer form — whose named pieces may be
   entirely different.

3. **A degenerate (identity-in-named-terms) lowering is a smell, not a deliverable.** A
   1:1 rename between layers is evidence the vocabulary *failed to shift*. The
   resolution is either a thin in-line note (the piece is genuinely primitive at both
   layers) or a combinator re-expression that makes the lowering a real translation —
   **never** a manufactured mirrored entry plus a thin connecting theme.

> Two adjacent layers sharing a named operator is permitted only when that operator is
> genuinely primitive at both — never as a goal. (This vocabulary-shift shape is the
> 2026-06-01 redirect; it **supersedes** the earlier "uniform pull-up → rectangular"
> framing, whose "the stack self-corrects toward rectangular" success metric was the
> bug, not the goal.)

### What "complete" means

- **A layer is complete** when every operator that *belongs at that layer* is expressed
  in that layer's own concise vocabulary, and each has a lowering that reads as a clean
  translation (or a justified thin in-line note). It is **not** complete by mirroring
  the layer below.
- **A lowering is complete** when it faithfully translates the higher layer's vocabulary
  into the lower layer's, with applicability conditions and the reorganization made
  explicit — not when it renames.
- **The stack is complete** when the in-scope target — **all five solver pipelines**
  (electrostatic, magnetostatic, eigenmode, driven, transient) **plus FE assembly** —
  is expressed this way end-to-end. The shared inner-kernel spine being substantially
  built is a *milestone*, not completion.

> **Where the L4 surface stands (as of 2026-06-03, batch-23).** **Both halves of the
> assemble+solve deliverable now reach L4 across all five pipelines.** The assemble half
> arrived in batch-21 (the `fe_assemble` assemble-fold combinator, the driven
> `assemble_frequency_operator`, the BLAS-1 data-algebra combinators `linear_combination`
> / `inner_product` with their kept named verbs `dot` / `nrm2`); the solve half closed in
> batch-22 with the driven pipeline's last gap — the per-ω frequency sweep that rebuilds
> the operator each step landed as its own single-witness L4 form (`frequency_sweep`),
> joining `ksp_solve` / `eigsolve` / `solve_family` / `fold_solve`. This was a *feature
> reaching L4*, distinct from mining a *shared generalized* combinator (which still needs
> ≥2 witnesses): a single in-scope feature getting its own L4 form does not over-unify.
> The shared inner-kernel + solver-driver + FE-assembly spine is now substantially built
> across the assemble+solve target — a milestone, not completion (the feature-surface
> spine and the remaining solver/output breadth continue).

> **The feature-surface spine (opened batch-22, scaled batch-23, column build-out COMPLETE batch-24).** Parallel to the bottom-up L4→L0
> vocabulary, a **top-down feature-surface spine** presents Palace's entry-point features
> (the 5 simulation drivers, the top-level lifecycle ROOT, the output/postprocess
> products, wave-port/boundary-mode) as **composition-root chapters** at L4+L1+L0 under a
> `# Feature surfaces` Part. A feature chapter takes config in, produces the physical
> product out, and its body is the *composition of the already-firm decomposed vocabulary*
> at that level, linking DOWN to the constituents — it composes the vocabulary, it does
> not replace it. The L4 feature surfaces ARE the outward backend-lowering entry points.
> As of **batch-24 the spine's column build-out is COMPLETE — thirteen columns, all at
> `seed`**: the 6 driver-leaf columns (electrostatic / magnetostatic / driven / transient /
> eigenmode / boundary-mode), the lifecycle meta-feature ROOT, and all 5 output-product
> columns (capacitance / inductance / sparameters / eigenfrequency-qfactor / energy-fields),
> nested into the directive-3 by-kind groupings (spine-ROOT / driver-leaf / output-product),
> each grouping with an intro page, the matrix alpha-within-kind, the within-column high→low
> ordering preserved as the deliberate exception. The output-product cohort surfaced that
> **the L4 algebra-of-folds has four distinct reduce-shapes** — bilinear symmetric-Gram
> (`gram_reduce`, capacitance + inductance), per-port linear-projection (`sparameter_reduce`,
> driven S-parameters), per-mode scalar-table (`eigenfreq_qfactor_reduce`, eigenmode
> frequency+Q), and per-domain scalar-table (`domain_energy_reduce`, the driver-agnostic
> energy-fields product) — a case where *refusing* an over-unification (the eigenmode-Q and
> S-params are NOT symmetric-Gram) was itself the load-bearing finding: each output product
> authors its OWN reduction verb. A second convention-shaping finding: **`energy-fields` is
> driver-AGNOSTIC** — the same per-domain field-energy reduction applies to *any*
> field-bearing driver's solution, so it is the explicit exception to the otherwise-1:1
> output-product↔driver cross-link convention (no single producing driver; a generic
> cross-link to the field-bearing driver set; no per-driver up-link). Records/structs named
> in signatures now get a definition home in themselves (the record-definition obligation) —
> a new `record` concepts Kind, ratified batch-24, carries the data-shape pages.

> **The seed-firming "ceiling" proved CONDITIONAL (batch-25→26).** With the columns
> complete-at-`seed`, batch-25 turned to **firming the seed surface**. The reduce verbs'
> *first* (test-coverage) gate is dischargeable in write-scope by citing the existing Palace
> postprocess unit tests as L0-equivalent documentation — both `sparameter_reduce` and
> `eigenfreq_qfactor_reduce` advanced to `rough-in (test-coverage-bounded)` this way, and a
> fourth reduce verb (`domain_energy_reduce`, the per-domain energy-table fold) was authored;
> a new firm L1 primitive `eigenvalue-untransform` (the per-mode eigenvalue→ω map) discharged
> the *structure*-side gate of `eigenfreq_qfactor_reduce`. The batch-25 reading was that the
> verbs' *second* gate (full `firm`) needs a **positive assembly test** absent from the Palace
> corpus, so the surface was at an in-scope ceiling. **Batch-26 showed that ceiling is
> conditional, not absolute.** A `lowering-verifier` *law-confidence* pass — the in-scope
> route — promoted BOTH `eigenfreq_qfactor_reduce` (c082) and `sparameter_reduce` (c083) to
> full `firm` via the **firm-on-positive-structure / syntactic-identity escape**: when a reduce
> verb's folded L1 primitives are *all* firm AND its assembly is bare scalar arithmetic with no
> law that smuggles in an unverified mathematical property, the laws are syntactic identities
> over firm structure and the missing assembly test does not gate them (the same escape that
> firms `apply_linop` / `participation_ratio`). The two-condition rule is sharp: it applies iff
> (i) all folded primitives are firm and (ii) the assembly is axiom-free arithmetic. It does
> NOT yet apply to `gram_reduce` / `domain_energy_reduce` — their folded `matrix-weighted-norm`
> energy/Gram forms are still rough-in (a reduction is as firm as its least-firm primitive),
> gated behind the `matrix-weighted-norm` √-entry-point cascade whose norm-axiom laws genuinely
> ARE theorems the source only numerically asserts (the escape was ruled inapplicable there).
> So the in-scope law-confidence route is now exhausted for the two all-primitives-firm verbs;
> the remaining reduce-verb tail is foundation-gated on that one cascade.

> **The column-promotion deadlock was broken (batch-26, user directive).** A subtler obstacle
> than the firming ceiling: even with two reduce verbs now firm, *no feature column could
> promote off `seed`*. The emergent per-column rule was "promote only once ALL constituents are
> firm" — and because the output-product↔driver reciprocal cross-linking counted a sibling
> *column* as a constituent, it created a **mutual-blocking deadlock** (`eigenmode` driver stays
> seed because it reduces into `eigenfrequency-qfactor`; that output-product column stays seed
> because its `eigenmode` constituent column is seed — each names the other as the blocker),
> making `seed` a permanent terminal state. The user directive redefines column promotion: a
> column promotes off `seed` when its **OWN composition + directly-owned constituents** are
> firm; **cross-linked sibling columns are references, not blocking constituents.** A driver
> column promotes on its own firm solve/assemble combinators + readout; an output-product column
> on its own firm reduce verb — independent of the column it cross-links. The columns are
> composition-roots over already-firm vocabulary, so the drive on the *constituent vocabulary*
> was always real and correct; the inter-column rule was the over-constraint. Under the new
> rule the first columns lift off `seed` (the all-13-column re-evaluation is the next lead): the
> driver columns with firm assemble+solve constituents (`eigenmode` composes firm `fe_assemble`
> + firm `eigsolve`), and the output-product columns whose reduce verb is now firm
> (`eigenfrequency-qfactor`, `sparameters`). The frontier otherwise returns to the **bottom-up
> vocabulary + the standing 5-driver→L4 backend-lowering completeness picture** as the
> highest-fan-out work.

> **The deadlock-break LANDED — six columns lifted off `seed` (batch-27).** The all-12-column
> re-evaluation under the OWN-COMPOSITION rule landed (c085): **six feature columns promoted
> `seed`→`firm` — the first feature columns ever off the terminal `seed` state.** The three
> driver-leaf columns whose own solve+assemble combinators are firm (`eigenmode`, `driven`,
> `transient`), the two output-product columns whose own reduce verb is firm
> (`eigenfrequency-qfactor` via `eigenfreq_qfactor_reduce`, `sparameters` via `sparameter_reduce`),
> and the spine-ROOT `lifecycle` (its own driver-agnostic `fold_solve` composition firm; the five
> per-driver columns are sibling references). The `eigenmode`↔`eigenfrequency-qfactor`
> mutual-blocking deadlock is broken. **The seed-firming ceiling is again CONDITIONAL, not absolute**
> — the columns were never truly stuck; the inter-column rule was the over-constraint, and the
> spine-promotion mechanism is now validated end-to-end. On-disk verification OVERRODE the plan's
> expectation that `electrostatic`/`magnetostatic` would flip: their own composition includes
> `gram_reduce` (rough-in), so they correctly STAY `seed` on a genuine own-constituent gate, not a
> sibling blocker. Six columns stay `seed` on real own-constituent gates: `electrostatic` /
> `magnetostatic` / `capacitance` / `inductance` (own `gram_reduce` rough-in), `energy-fields` (own
> `domain_energy_reduce` + `matrix-weighted-norm` rough-in), `boundary-mode` (own waveguide-mode
> readout unhomed). A third firm-on-positive-structure promotion this arc (`solve_family`, c086 —
> element-independence read off the `const BaseKspSolver::Mult` body, the escape now reaching the
> solve-family combinator) narrowed `electrostatic`/`magnetostatic` from a two-constituent to a
> single-constituent (`gram_reduce`) gate — but did not flip them. **The remaining lever at this
> point in the arc was a single convergent foundation-blocker: the `matrix-weighted-norm`
> √-entry-point cascade** (since discharged-and-landed batch-29, see below), which
> gated `gram_reduce` (→ four columns) AND `domain_energy_reduce` (→ energy-fields) — 5 of the 6
> stay-seed columns converged on it. The in-scope law-confidence route is exhausted for the
> all-primitives-firm cohort (the norm-axiom laws may genuinely be inner-product-structure theorems
> the source only numerically asserts, not syntactic identities); the next probe is a scoped
> literature-anchor pass on those norm axioms — the cheap test of whether that one gate is
> dischargeable at all, before any heavy ~30-file cascade wave.
>
> **Both norm-axiom law-sides discharged — the firm flip is now LICENSED (batch-28).** The two
> scoped dischargeability probes the prior batch queued BOTH discharged the `matrix-weighted-norm`
> norm-axiom law confidence. The **structure-side** (c088) showed the three inner-product-structure
> laws (triangle / Cauchy–Schwarz / parallelogram) are inner-product-space THEOREMS that hold for
> any inner-product-induced norm, with their SPD premise satisfied **provably-by-construction** at
> the usage sites (`B = KM` is the real SPD part of the FE mass matrix — a positive L0 home for the
> premise) — exact-arithmetic theorems, not a numerically-asserted claim, so no √-entry-point test
> gates them. The **FP-side** (c089) showed the floating-point sub-claims inherit verbatim/additively
> from the firm constituents `dot` + `apply_linop` through a deterministic IEEE-754 outer √ over
> disjoint accumulators — exactly the `nrm2` firmness precedent (itself firm) extended by one firm
> constituent, with no composition-specific FP property arising. With **both** sides discharged, the
> verb's `rough-in (test-coverage-bounded)` rested on a *single* remaining gate: the missing direct
> test of the 4-arg SPD-weighted `Norml2(comm,x,B,Bx)` √-entry-point. The batch-28 meta-phase judged
> that gate **REDUNDANT** — it would only re-confirm properties already anchored by structure +
> constituent-inheritance, and no law is left for which it is the only evidence. This is materially
> the same situation as the four prior firm-on-positive-structure escape promotions (`apply_linop`,
> `eigenfreq_qfactor_reduce`, `sparameter_reduce`, `solve_family`). **The escape applies → the firm
> flip is GO.** The full `firm` flip plus its ~30-file cross-reference cascade became the batch-29
> LEAD (LANDED CLEAN c091, see below); firming `matrix-weighted-norm` was the convergent foundation-unblock for the downstream
> `gram_reduce` / `domain_energy_reduce` reduce verbs and, through them, 5 of the 6 stay-`seed`
> feature columns (`electrostatic` / `magnetostatic` / `capacitance` / `inductance` / `energy-fields`).
> The arc illustrates the FLOW's load-bearing pattern: a heavy cascade wave is *gated on cheap
> dischargeability probes first* — the probes converted a NO-GO-held-by-inertia blocker into a
> GO-by-explicit-derivation flip, without ever forcing the gate.

> **The √-cascade LANDED; the foundation-blocker tail is being worked off systematically
> (batch-29).** The GO firm flip + cascade LANDED CLEAN (c091): a single 4-dispatch structural
> wave flipped `matrix-weighted-norm` to `firm` and propagated the cascade across ~30 files,
> yielding **three** firm promotions — the planned `matrix-weighted-norm` (L1) PLUS two bonus
> cascade-yield promotions (`domain_energy_reduce`, the per-domain energy-table fold, to firm L4;
> the `energy-fields` feature column to firm) — with the honest residual gates preserved at that
> point (`gram_reduce` and `bilinear-form` were still `rough-in`; four columns still `seed`). The
> long-held √-foundation-blocker is discharged. With the diagonal `matrix-weighted-norm` now firm,
> the convergent foundation-blocker collapsed onto the SINGLE remaining primitive **`bilinear-form`**
> (the off-diagonal operator-weighted form, the sole residual gate on `gram_reduce`). The same
> cheap-probe pattern was applied immediately (c092): a scoped dischargeability probe on
> `bilinear-form` returned **DISCHARGE** — and materially CLEANER than `matrix-weighted-norm`
> (laws 1-6 are pure-linearity syntactic read-offs over the firm `dot` + `apply_linop` +
> `matrix-weighted-norm` constituents, with NO inner-product-norm theorem content needing a
> structure-side probe; laws 7-8 are M-symmetry-conditional with both on-disk witnesses). The
> `bilinear-form` firm flip + its cascade — a BIGGER fan-out than the `matrix-weighted-norm`
> cascade (four columns flip, not one) — was queued as the next gated wave, and **LANDED CLEAN at
> cycle-095 (batch-30, see below).** The probe-then-wave playbook (now a named procedure, skill
> `foundation-blocker-dischargeability-probe`) was run down the foundation tail one convergent
> blocker at a time: `matrix-weighted-norm` discharged-and-landed (c091), `bilinear-form`
> discharged-and-landed (c095). With the `bilinear-form` cascade landed, the convergent
> foundation-blocker tail of the reduce-verb cohort is **worked off**; this supersedes the prior
> batches' "single convergent blocker is the `matrix-weighted-norm` √-cascade" framing entirely.

> **The `bilinear-form` cascade LANDED + the artifact gained two mechanically-checkable health
> axes (batch-30 — the GRADED-STACK campaign).** Two arcs composed across cycles 094/095/096.
> **(1) The `bilinear-form` cascade (c095).** The queued wave landed in a single 7-dispatch cycle:
> `bilinear-form` (L1) → `firm` (the firm-on-positive-structure escape), clearing `gram_reduce`'s
> sole residual gate so `gram_reduce` (L4) → `firm`, propagating under the OWN-COMPOSITION rule to
> **four output-product/driver feature columns** (`capacitance` / `inductance` / `electrostatic` /
> `magnetostatic`) flipping `seed` → `firm` — the feature spine reaching 11-firm / 1-seed (only
> `boundary-mode` stays `seed`, its waveguide-mode readout unhomed). The reduce-verb foundation tail
> is now worked off. **(2) The two-axis artifact-health model.** Following the 2026-06-04 user
> directive (full spec `METHODOLOGY-GRADED-STACK.md`), the artifact gained **two orthogonal,
> mechanically-checkable health axes**, replacing eyeball maturity-tracking and the frozen Phase-1
> corpus with typed, linted invariants:
> - **Axis 1 — resolution + well-foundedness.** The maturity ladder is a total order with a rank
>   (`roadmap_goal = 0 < stub = 1 < rough-in = 2 < firm = 3`; `partly-constructive` /
>   `rough-in (test-coverage-bounded)` are sub-rank ≈2.5; `obstruction` a separate rankable kind),
>   and the **well-foundedness invariant** holds for every blocking `depends-on` edge `u → v`:
>   `rank(u) ≤ rank(v)` — *an entry is at most as resolved as its least-resolved dependency*
>   (`firm` rests only on `firm`). This subsumes the lived "as firm as its least-firm folded
>   primitive" rule (the `k=3` case) and the feature OWN-COMPOSITION rule, now mechanical. The new
>   **rank-0 `roadmap_goal` chapter** is the in-discipline replacement for the retired
>   `annotated-and-retained` slice: a real, claim-free book chapter carrying intent + pulled-by
>   provenance + declared deps, so *intent* has a native home (links resolve) and never has to be
>   parked in a frozen slice.
> - **Axis 2 — reachability / liveness.** The **feature-surface spine columns are the GC root set**
>   (`seed` is a root marker, NOT a ladder rung); reachability from the roots over `depends-on` edges
>   is liveness, and an unreachable node is **garbage** — the detritus hunt and the orphaned-intent
>   hunt are one mark-sweep from the roots.
>
>   The **shared substrate** is one typed dependency graph: each edge is `depends-on` (blocking —
>   constrains rank AND carries liveness) or `reference` (navigational — free; an edge to a *root*
>   is `reference`, which is exactly where OWN-COMPOSITION comes from). **Two linters under `tools/`**
>   check the two axes (the rank check + the reachability GC); `integrator-finalize` runs them every
>   cycle and the rank invariant is a **hard gate for new work** (no new violation admitted). The
>   campaign typed the feature-root closure + the high-fan-out frontier first (incremental, lazy
>   tail), opened a **bounded baseline-exception ledger** for the pre-existing rank violations, and
>   burned it down: the rank linter independently rediscovered the hand-tracked firm-rests-on-rough-in
>   cascade as **22 violations at the c094 baseline → 1 (c095, after the `bilinear-form` cascade
>   cleared ~10 genuine gaps and the typed-frontmatter retyping cleared ~11 prose-parse false
>   positives) → 0 (c096)** — the typed subset is now well-founded with zero rank gaps. The first
>   `roadmap_goal`-adjacent vocabulary gap, the firm L4 `preconditioning-framework`, was authored;
>   the Phase-1 slice corpus depopulation (safe and mechanical — the slices sat in the
>   reachability-GC detritus mass, deletable once their load-bearing citations were repointed to
>   non-slice homes) was queued as the next batch's lead **and is now COMPLETE (batch-31, below)**.
>   The two axes together *define* artifact health: every node reachable from a root, and the rank
>   invariant holding everywhere.

> **The Phase-1 slice corpus is fully lifted and DELETED — the graded-stack health campaign is
> discharged (batch-31).** The campaign's last open phase, P2 corpus depopulation, completed across
> cycles 097/098/099: the 9 Phase-1 slices were absorbed (each slice's load-bearing claims repointed
> to firm non-slice homes citing L0 directly, the one genuinely-unlifted datum — the CG v0.5 worked
> example — absorbed firm into `L4/krylov-step.md`) and **DELETED — the corpus went 9 → 0 and
> `book/src/spec/` no longer exists**. This eliminates the *frozen second source of truth* the
> graded-stack model was built to dissolve: a slice was a representation NOT beholden to
> combinator-refactoring or fusion, a brake on the very vocabulary-shift freedom the redirect grants
> the layers. Throughout the deletion `rank_violations` stayed **0** (the typed subset is well-founded)
> and every `cargo make book` was green. Two transient mechanisms of the now-finished campaign were
> retired: the `annotated-and-retained` carve-out (which had made permanent slice-retention the
> standard landing state — superseded by the rank-0 `roadmap_goal` chapter, which gives intent a
> *refactorable* home that climbs instead of freezing) and the `phase-1-slice-reduction-audit` skill
> (archived; no slices remain to audit). The same batch ran a non-book-artifact orphan review,
> removing the decommissioned pre-redirect process scaffolding (`orchestrator/`, `prompts/`,
> `schemas/`, the legacy `lessons.md` / `questions.md` ledgers, the stale root `README.md`) — the
> "corpus shrinks monotonically; git history is the record" discipline applied beyond `book/`. With
> the graded-stack campaign discharged, the lead returns to the standing forward frontier: bottom-up
> vocabulary + the 5-driver→L4 backend-lowering completeness picture + the last `seed` feature column.

> **The standing forward frontier is substantially EXHAUSTED — the in-scope stack is L4-complete for
> backend-lowering; the lead pivots to the typed-edge campaign (batch-32).** Across cycles 100/101/102
> the standing forward frontier was worked to its clean-gated floor. The two highest-fan-out L1>L0
> mutation-rotation lowering floors firmed (`apply-linop-mutation-rotation`, every matvec;
> `ksp-solve-mutation-rotation`, all five driver pipelines — both via the firm-on-positive-structure /
> syntactic-identity escape), and the *one* genuine remaining FE-cohort L4 hole the c100 completeness
> survey had narrowed to — **boundary-condition elimination** — closed at c101: `eliminate_bc` rose to
> a firm L4 post-assembly combinator (the OWN-COMPOSITION reading, a separable verb that consumes the
> already-assembled operator) with a firm `bc-elimination-post-composition-dissolution` L4>L3 theme.
> With that, **every in-scope feature surface — all 5 solver drivers + FE-assembly + 5 output-products
> + BC-elimination — reaches firm L4**, the outward backend-lowering entry surface. The linter's
> `promotion_frontier` is now entirely **obstruction-/demand-gated** (the `bicgstab`/`minres` enum-only
> stubs Palace never implements; the opaque-library `eigsolve` convergence-reason map; the demand-gated
> `deflate` Galerkin-core and `boundary-mode` column) — there is no clean-gated bottom-up pick left,
> and the redirect forbids manufacturing a rectangular pull-up. So the lead **pivots** to the
> meta-phase-owned work that the now-thin content frontier makes highest-leverage: the **authoritative
> artifact-wide typed-edge campaign** (graded-stack P1). The two health axes were *defined* batch-30
> and the rank invariant held at 0 throughout batch-32, but the edges themselves are still largely
> *untyped* (142 of 352 files), so the reachability GC reads most of the artifact as "detritus" only
> because it cannot traverse absent typed edges. Typing each edge `depends-on` (rank-constraining +
> live) vs `reference` (navigational + free) — the pass that *is* the audit — converts the artifact
> into a fully mechanically-checkable typed DAG, reclassifies the prose-as-slug false-positive targets,
> and lets the GC distinguish genuine garbage from untyped-but-live. This is the batch-33 lead.

> **The typed-edge campaign rolled out and the reachability axis became MEASURABLE (batch-33).** Across
> cycles 103/104/105 the P1 typed-edge campaign LED every cycle: c103 typed the concepts substrate +
> every navigational container (`untyped` 142→78) and created the first record-home `dofset`; c104 typed
> the six internal record-concept pages firm and added the feature-column `uses-record` edges that the
> consuming columns genuinely rest on; c105 landed the content tail (all twelve config-input columns now
> carry the `uses-record` edge to `config-record`). The rank invariant HELD at 0 throughout. But the
> campaign surfaced — and the batch-33 meta-phase fixed — the tooling gap that had made the whole
> reachability axis *invisible*: the linter's hand-rolled frontmatter reader parsed only the inline-flow
> edge form, not the multi-line **block-mapping** form the producers actually author, so the
> `uses-record` rescue edges (correct on disk) were never GC-traversed. With the parser fixed (and
> `kind: navigational-container` now honored), the linter reads the TRUE picture for the first time:
> reachability climbed from 36 (just the roots) to 81, `config-record` correctly shows all twelve inbound
> edges, and the residual "detritus" dropped from 229 to 163 as the navigational containers were
> reclassified out of the garbage bucket. The six internal solve/BC record shapes remain (correctly)
> unreachable — they are named in no feature-column signature; they reach the roots only via op-chapter
> `uses-record` edges (`column →(composes) op →(uses-record) record`), the **WAVE-3** tranche that is the
> batch-34 lead. The lesson the arc records: the two health axes were *defined* batch-30, but an axis is
> only as real as the linter's ability to read the edges that carry it — typing the artifact and making
> the GC actually traverse those types are the same project, and batch-33 closed the gap between them.
>
> **The reachability axis was GROUNDED across the live spine, and a new GC disposition emerged (batch-34).**
> With the linter now reading the true picture, cycles 106/107/108 drove reachability from 81 to **102** with
> the rank invariant HELD at 0 and `unresolved_depends_on_targets` driven to 0: c106 landed the WAVE-3
> op-chapter `uses-record` typing (the solve-kernel pair + `solve_family`/`fold_solve`/`eliminate_bc`),
> rescuing five of the six internal solve records and making `krylov-step` root-reachable; c107 grounded the
> firm-but-absorbed BC-elimination + divfree clusters from the feature-spine roots; c108 ran a systematic
> `lowers-to` grounding pass down the BC + divfree lowering chains so the L1/L0 lowering homes became
> reachable. The arc's load-bearing lesson is a **new disposition for the GC sweep** (a 2026-06-05 user
> directive, now codified): *when an unreachable node is a genuine future or absorbed dependency of a
> reachable goal node, **ground** it — type the faithful, honestly-classified `depends-on` edge into the
> reachable chain — rather than removing it or filing it as detritus.* The priority is ground → route-as-
> detritus → delete, and grounding is always faithful-edge-or-finding (c108 correctly *declined* a would-be
> over-edge: the BC theme does not `lowers-to` `essential_dofs`, which reaches root via its own construction
> theme). Grounding is the reachability-axis analogue of the `roadmap_goal` chapter on the resolution axis:
> both keep a genuinely-wanted node legally in the artifact instead of dropping it. The residual is a bounded
> ~10-theme L2-L1 lowering cohort that stays garbage for one structural reason (the L2/L3 `lowers-to`
> convention points operator→operator, never operator→theme) — the natural batch-35 lead, a one-edge-per-theme
> grounding pass.
>
> **The grounding campaign ran to its faithful limit, and the residual garbage was named (batch-35).** Cycles
> 109/110/111 drove reachability from 102 to **122** (rank invariant HELD at 0 throughout): c109 grounded the
> four on-spine L2-L1 lowering themes; c110 grounded the reduce-to-scalar chain (`dot`/`nrm2`/`inner_product`)
> and the orthogonalize leg with a *single* faithful `L4/krylov-step` body edit that cascaded the whole chain;
> c111 grounded the orthogonalize chain down to L0. The batch's load-bearing lesson is the **boundary of
> grounding**: not every unreachable firm node *can* be grounded, because not every one has a faithful reachable
> depender. The reduce/orthogonalize verbs *do* (the solve body genuinely calls them), so they were grounded.
> But the chebyshev/jacobi preconditioner leg is *absorbed into the constructed `op.T`* (the kernel folds
> `apply_linop op.T`, never naming a concrete preconditioner), the L3 orthogonalize iteration-view is composed
> only at its L2 surface (krylov-step composes `L2/orthogonalize`, not the L3 view), and `L2/gram` is reached
> only through the demand-gated `deflate`. Forcing an edge for any of these would *invert a real dependency
> direction or assert a constituent-use that does not exist* — the over-edge the priority order exists to
> prevent. So the third disposition activated: these firm-but-absorbed/unconsumed nodes go into an explicit
> **reachability baseline-exception set** (a new Axis-2 ledger kind, parallel to the now-burned-down Axis-1
> rank-violation set), each enumerated with a *non-fix-forward promotion condition* — a future faithful column
> edge, a demand-gate trigger, or transitive grounding of its consuming leg. The lesson: the reachability axis
> reaches a *faithful floor*, not zero garbage; the disciplined response to that floor is a tracked, bounded
> exception set with promotion conditions, exactly as `partly-constructive` is the bounded transient gate on the
> resolution axis. (A separate, out-of-band 2026-06-06 directive also sharpened the L4 calculus notation: named
> shape groups `Tensor[(S: ...)]` replace the bare `Tensor[N]`-as-same-shape leak, which silently pinned
> shape-generic operators to rank-1.)
>
> **The reachability axis reached its plateau, and the residual garbage was fully named (batch-36).** Cycles
> 112/113/114 drove reachability from 122 to **132** (rank invariant HELD at 0 throughout), all of it
> frontmatter-only Axis-2 grounding: c112 typed the L3 reduce/orthogonalize/linear_combination mid-nodes and
> ground `L2/nrm2` via a faithful adjacent-layer edge; c113 ground `set_subvector_zero`'s lowering theme and ran
> an **audit-first** sweep that characterized every remaining typed-but-unreachable node; c114 ground the
> FE-assemble cluster (the element/space/collection vocabulary) and the `dot`/`nrm2`/`scal` L1>L0 themes. The
> batch's load-bearing move was the audit: rather than blindly typing the lazy tail (which the c112 finding showed
> does not even move the `untyped` count, because the linter shim-counts legacy-edged files as typed), c113
> *characterized* the 13 un-baseline-excepted STRONGER-garbage nodes and dispositioned each — 1 groundable (landed
> c114), 12 baseline-exceptions. The batch-36 meta-phase ratified those 12 into **RE6** (the axpy/`scal`
> arity-specialization leaves absorbed below the reachable `linear_combination` combinator — combinator-primary,
> so the leaf-to-combinator edge direction means nothing composes a concrete arity *by name*), **RE7** (the
> diagonal-preconditioner apply/extract kernels absorbed into the RE1 leg), and **RE8** (the L3 iteration-views
> over reachable L4 combinators, an L4→L2 altitude-skip distinct from RE2's L3-composed-at-L2 shape). With RE6-RE8
> ratified, **the entire STRONGER-garbage set of 23 is now fully tracked — zero undispositioned members** — the
> reachability axis has reached its *faithful floor* exactly as the resolution axis reached `firm`-rests-on-`firm`.
> The lesson the arc closes: a campaign that has run to its faithful limit is *complete* when every residual is
> either grounded or carries a tracked promotion condition, not when garbage hits zero — and recognizing that
> plateau (rather than forcing unfaithful edges to drive a number down) is the disciplined end-state. The forward
> vocabulary frontier is likewise substantially exhausted (the promotion frontier is all obstruction-/demand-gated;
> all 40 feature columns are off `seed`); the project is approaching a natural completion plateau on both axes.

> **The plateau was independently confirmed, then the human set TWO new directions (batch-37 opener + out-of-band).**
> Cycle-115 ran an INDEPENDENT plateau-probe (a `cross-layer-cross-cutter` re-derivation that did NOT trust the
> batch-36 assessment): it **confirmed exhaustion-of-current-scope** on all three fronts — no missed faithful ground,
> all 8 promotion-frontier members genuinely obstruction-/demand-gated, no unfiled in-scope coverage hole (the
> `build_mesh` Mesh-wrapper candidate is a *tracked* deferral, not a hole). The verdict is **exhaustion of the scope
> as-was, NOT terminal** — and the human then issued two directives that set the next two moves. **(A) Semantic
> consolidation:** the spec's *semantic* definitions (the calculus grammar, shape semantics + named shape groups,
> the pseudo-language notation invariant, monad/ownership/reduction conventions) become a **first-class
> actively-managed surface**, held under the same liveness/unification/consolidation discipline the graded stack
> applies to *vocabulary* — a semantic rule lives ONCE on the surface (`book/src/semantics/index.md`, promoted out
> of "strawman" status and ordered BEFORE the `# L4` Part), and functional-unit entries USE + LINK rather than
> RE-STATE (a restatement is the semantic analog of a degenerate-identity-lowering smell). **(B) Open all remaining
> feature fronts simultaneously:** the human fires the demand-gate for ALL deferred fronts at once
> (`waveguide-mode` · `boundary-mode` promotion · the `fe_space` siblings · the mesh-wrapper vocabulary · any other
> in-scope deferral) — the rationale is **shared-exploration lifting** (the fronts are variants sharing
> implementation cores, so one wide fan-out lifts the shared substrate once). The sequencing is consolidation FIRST,
> then the all-fronts wide wave. So the "plateau" was not an end-state but a decision point: the disciplined
> recognition that the clean-gate scope was exhausted is exactly what let the human choose the next scope
> deliberately.

> **Both directives landed, and the "plateau" reopened into a concrete forward campaign (batch-37 close).** The
> consolidation campaign landed across cycle-116: the semantic surface physically moved out of `design/` to
> `book/src/semantics/index.md` (with the ~97-file cross-reference rewrite), and the 27-file named-shape-groups
> restatement cohort was fully swept (Tier A+B+C) so functional-unit entries now USE+LINK the single semantic home
> rather than RE-STATE it. The all-fronts wide wave landed across cycle-117: a single multi-dispatch fan-out opened
> the last in-scope deferred feature fronts together — a sixth output-product column (`waveguide-mode`), the
> `boundary-mode` driver column promoted off `seed`, and three new firm L1 ops (`build_mesh`, `fe_space_hierarchy`,
> the de-Rham `interpolator`) — so the shared **mesh→fe_space substrate** was lifted once across all the related
> fronts. The wave did NOT re-plateau the project: it homed a new substrate that now needs its L1>L0 lowering
> themes and its inbound grounding consumers, which is exactly a high-fan-out forward campaign (batch-38: the three
> construction-rotation themes + the faithful `lifecycle → build_mesh` grounding edge + the `waveguide_mode_reduce`
> L4 verb home + the record-definition homes). The reachability GC handled the wave's three new detritus L1 ops by
> the §2f triage: `build_mesh` is GROUNDABLE (it is literally the lifecycle composition-root's `config→mesh` stage,
> so the faithful `lifecycle → build_mesh` composes edge grounds it), while `fe_space_hierarchy` and `interpolator`
> have no faithful inbound consumer yet and were tracked as reachability baseline-exceptions (RE9, RE10) with
> concrete promotion conditions — the disciplined "ground-don't-remove, baseline-except-don't-force" priority order
> in live use. The lesson of the whole arc: an honest plateau is a scope decision, and opening the deferred scope
> exposes the next layer of substrate-and-grounding work rather than ending the project.

> **The directives' campaign was consumed, and the plateau was confirmed a third time (batch-38 close).** Cycles
> 118/119/120 ran the mesh→fe_space substrate campaign to completion and then re-confirmed the plateau. Cycle-118
> (the opener, six clean dispatches) homed the three L1>L0 construction-rotation themes for the new substrate ops,
> ground `build_mesh` off detritus via the faithful `lifecycle → build_mesh` composes edge (the §2f preferred
> GROUND, since `build_mesh` literally *is* the lifecycle composition-root's `config→mesh` stage), homed the
> `waveguide_mode_reduce` L4 verb (promoting the sixth output-product column off rough-in), and landed the
> `Mesh`/`WaveguideModeTable` record-definition pages. Cycle-119 cleared the honest grounding/hygiene tail — the
> analogous L4 lifecycle sibling edge and an interpolator citation over-range. Cycle-120 was an
> *observation-only* plateau-probe (a `cross-layer-cross-cutter` re-derivation that did not trust the c118/c119
> finalizes) that re-confirmed the terminal-state on both axes (rank invariant clean; the STRONGER-garbage set
> maps exhaustively to the ratified reachability baseline-exceptions; no in-scope coverage hole). The probe's
> load-bearing finding was a **stale baseline-exception premise**: RE10 (the de-Rham `interpolator`) had been
> ratified as "no faithful inbound consumer yet," but the now-firm `waveguide_mode_reduce` (and the firm
> `divfree-projector`) *do* consume it by name — so a correct baseline-exception had silently become a missed
> GROUND the moment its consumer firmed. The batch-38 meta-phase discharged RE10 (migrating the faithful grounding
> to the next batch) and installed a new standing guard: the every-batch baseline-exception review must
> re-verify each "no faithful consumer" premise against any consumer that firmed in the batch. The lesson the arc
> adds: a tracked baseline-exception is not a permanent disposition — it carries a promotion condition precisely
> *because* the world can change under it, and the every-batch re-check is what converts a now-stale exception
> back into an honest grounding rather than letting it ossify into permanent garbage. With the directives' work
> fully consumed and the plateau confirmed a third consecutive time (batch-36 → batch-37 → batch-38), the project
> stands at a genuine terminal-state-of-current-scope: the disciplined recognition that the next move is again a
> deliberate scope decision for the human, not a forced internal frontier.

> **The plateau ENDED — the human re-scoped (out-of-band, 2026-06-07).** The batch-38 (third-consecutive) plateau
> ASK was answered not with a winding-down but with a **generative re-scope**: three directives that reopen a clear
> high-fan-out forward campaign by lifting three postures that had together *manufactured* the plateau. **(1) MPI /
> sharding is a deferred future direction, not active work** — the MPI implementation rests on a sharding theory
> assuming a lifetime structure the spine has deeply re-written, so lifting the MPI-associated version could be
> *destructive* to the abstraction spine; it is recorded as a future goal (and the sharding *math* as an
> exploratory-only-if-non-destabilizing decomposition abstraction), but MPI/distributed stays out of active scope.
> **(2) The existing deferred IN-SCOPE work is lifted through** — the STOP-PROPOSING posture that had parked the
> RE1-RE10 baseline-exceptions + the demand-gated vocabulary is LIFTED; the forward frontier is now *building the
> grounded in-scope consumers and discharging the exceptions* (the geometric-multigrid preconditioner — the highest
> fan-out, discharging RE9/RE1/RE5/RE7 by composing the level-stack + smoother + diagonal-preconditioner chains by
> name; then AMR; then the residual RE-cohort consumers). The reachability baseline-exception set, which batch-35→36
> had correctly named the *faithful floor*, is thereby reframed: it was a faithful floor *under the then-current scope*,
> and each exception carried a promotion condition precisely because a future consumer could fire it — the re-scope
> fires them. **(3) Spine-dependency opaque-library kernels are lifted with a constructive implementation, preserving
> a kernel-API vs kernel-implementation distinction** (see the FLOW section below) — revising "document obstructions,
> don't fill them" for the *spine-dependency* opaque-library kernels (the libCEED quadrature leaf, the
> triangular-solve/GS-SSOR relaxation, the SLEPc eigsolve loop), while the enum-only-stub carve-out (MINRES/BiCGStab)
> is preserved unchanged. The lesson the arc closes: a plateau confirmed three times is still a *scope* boundary, not a
> *project* boundary — and the disciplined recognition of the clean-gate floor is exactly what let the human re-scope
> deliberately into the deferred-but-in-scope substrate (the constructive kernels, the multigrid preconditioner, AMR)
> that the earlier postures had been holding back. The vocabulary-shift redirect and the graded-stack machinery — *how*
> vocabulary is expressed — are unchanged; the re-scope governs *what* is now the frontier.

> **The lift-through campaign LANDED and the plateau is broken (batch-39).** Cycles 121/122/123 executed the
> re-scope's forward campaign. Cycle-121 ran a wide all-fronts fan-out that broke the batch-36→38 plateau: the
> geometric-multigrid preconditioner column landed (the highest-fan-out lift-through consumer), the constructive-kernel
> frontier opened (three `kernel-impl` nodes — libCEED quadrature, eigsolve Lanczos/Arnoldi, the relaxation smoother —
> each linked to its kept kernel-API surface by a `realizes-kernel-api` reference edge), the AMR front opened, and
> reachability jumped +17 in one cycle. Cycle-122 wired the consumers (the four libCEED contraction-substrate ops; the
> AMR estimate/mark verbs; the `correction_step` L2 combinator with replace-and-propagate), firm-flipped the GMG column
> and the AMR theme, drove `unresolved_depends_on_targets` to 0, and confirmed BOTH kernel-API correspondence audits
> FAITHFUL. Cycle-123 closed the batch: the krylov-iteration infrastructure feature column composed the L3
> iteration-rotation form *by name*, a REAL `depends-on` reachability flip that discharged RE2 + RE8. Across the batch
> the in-scope RE set burned down from a permanent floor to a discharge target — **8 of the original 10 discharged or
> grounded** (RE1/RE2/RE5/RE7/RE8/RE9/RE10), leaving RE3 (deflate/NLEPS, consumer-gated) + RE6 (axpy-arity,
> refactor-gated). The batch's two scheme questions were adjudicated by the meta-phase: **(a)** a `detritus` count that
> climbs as a function of *correct* modelling (firm nodes reachable only via deliberate `reference` edges — the
> combinator-primary leaves, the kernel-impl→kernel-API links) is NOT decay — these are the new Axis-2 baseline-exception
> kind **RE11**, tracked not read-as-garbage; the `reference`-carries-no-liveness rule stays unchanged (making
> `reference` carry liveness would break the combinator-primary model). **(b)** A composition-root's rank is *capped* by
> its least-resolved blocking dep; firm-on-positive-structure escapes the test-coverage gate, not the well-foundedness
> cap — so the krylov-iteration column is correctly rough-in over its partial-obstruction deps (the GMG column was firm
> only because *its* deps were firm). The lesson the arc adds: a re-scope that names the *consumers* (build this
> preconditioner, this iteration column) discharges baseline-exceptions far more cleanly than chasing the exceptions
> directly — the exceptions are a downstream readout of which consumers exist, and they fall out when the consumers land.

> **The constructive-kernel layer began to take shape (batch-40).** Cycles 124/125/126 advanced the
> first of the two post-lift-through directions the human set ("A then B": deepen the constructive-kernel /
> matrix-free layer, then audit 5-driver L4-completeness). Cycle-124 built the `nleps-deflated-eigensolve` L3
> consumer — a real `depends-on` composition-root that *fired* RE3 (making the `deflate → gram` constituent
> edge reachable) and *grounded* the eigsolve-impl / Lanczos-step kernel-implementations (their first faithful
> consumer) — and *discharged* RE6 by eliminating the eight axpy-family arity leaves into their combinator's
> arity-specialization notes (delete-not-ground, the higher-value disposition). Cycle-125 completed the libCEED
> contraction substrate (the four element-local ops firm, the quadrature kernel-implementation firm) and landed
> the first matrix-free L2 combinator. Cycle-126 capped the surface with an L4 backend-lowering
> operator-*constructor* (`mk_matrix_free_operator`, a claim-free `roadmap_goal` pulled to a feature root by a
> reference-class chain). The matrix-free backend-lowering surface now spans three layers — L1 implementation,
> L2 combinator, L4 constructor — which is exactly the burn/GPU-relevant build the re-scope opened. With this,
> the original ten reachability baseline-exceptions stand nine-of-ten discharged or grounded (only the
> consumer-gated GMRES running-QR view remains), and the live exception cohort is the *deliberate*
> reference-only-reachable substrate — firm nodes correctly off the `depends-on` spine until a firm `fe_assemble`
> body composes them by name, which is the batch-41 "A" deepening's job. The lesson the arc adds: a deletion that
> *folds* a node into its successor is a cleaner discharge than a grounding edge — it removes the node from the
> graph entirely — but it surfaced a new de-link surface (frontmatter typed edges, invisible to the markdown
> link-checker), a reminder that as the dependency graph became load-bearing, every destructive refactor must
> sweep the typed edges, not only the prose links.

> **The "A then B" arc completed — the in-scope spine is L4-COMPLETE (batch-41).** Cycles 127/128/129
> finished the two-step forward direction the human set after the lift-through. "A" (cycle-127): the
> matrix-free / element-local constructive-kernel layer landed fully firm across three layers — the L1
> contraction substrate, the L2 combinator, and the L4 operator-constructor (`mk_matrix_free_operator`
> firm-flipped off `roadmap_goal` once a feature-surface composition-root pulled it by a faithful
> `depends-on` chain) — which grounded the libCEED-substrate reachability baseline-exception exactly as
> its promotion condition predicted, and folded the inner-product reduce-family (`dot`/`nrm2`) into its
> combinator. "B" (cycle-128): the 5-driver L4-completeness capstone audited whether every simulation
> driver (electrostatic / magnetostatic / eigenmode / driven / transient) plus the lifecycle root reaches
> L4 by composing firm vocabulary *by name* — and returned ALL-PASS, with the only two non-trivial
> constituents (the SLEPc eigensolve loop, the transient per-step ODE body) being tracked opaque-boundaries
> rather than coverage gaps: **no gap.** A mid-batch user directive (the calculus is high-order;
> closure-returning signatures group the closure or use the `Op[τ_in → τ_out]` operator-value spelling, never
> the opaque type-application form) was codified onto the semantic surface as §1.3.1 and completed
> end-to-end. The lesson the arc adds, and the reason this is a juncture rather than just another batch:
> a top-down completeness audit against the firm bottom-up vocabulary is how the project *recognizes
> done-ness* — when the feature-surface roots all reach L4 by name, the in-scope artifact is complete for
> its in-scope purpose, and the forward question becomes a strategic one (wind to maintenance, or open a
> deferred-and-gated direction like the sharding-math) rather than a coverage-filling one. The capstone's
> own recommendation is to wind the in-scope spine to maintenance.

## FLOW — how the goal is met

The stack is **not the deliverable** — it is a research artifact whose construction
yields the understanding that *is* the deliverable. Layers exist to expose friction;
the valuable signal lives in the friction. Construction proceeds **push-forward** (one
operator / theme / slice at a time, a layer's job ending as soon as the next can
speak), **push-back** (when a different framing of the layer below would make the layer
above dramatically easier, restructure the lower layer), and **sideways** (when a slice
is blocked, move to a parallel one and surface unification opportunities).

### The cycle: 5-phase primary + every-3rd-cycle meta-phase

Two cadences drive construction.

**Primary cycle (5 phases), every cycle — the forward-frontier loop:**

1. **Plan** — the planner reads the plan (`scaffolding/priorities.md`), roadmap,
   friction-ledger, and open questions, and emits a fan-out-ranked dispatch plan.
2. **Dispatch** — up to ~12 specialized agents run in parallel where non-overlapping,
   each emitting a single `CYCLE.md` of *proposed changes*; **no agent mutates the book
   in this phase.**
3. **Critique** — a critic runs an 8-check checklist per report (citation validity,
   surface-or-evidence, rotation quality, variant-axis coverage, cross-reference
   integrity, and more).
4. **Repair** — a repairer applies mechanical, surgical fixes to flagged reports.
5. **Integrate** — applied serially per report into the book, then a single finalize
   pass rebuilds, commits, and pushes. **Spec growth is monotonic and visible in
   `git log`; every cycle commits, pass or fail.**

**Meta-phase, after every 3rd primary cycle** — examines evidence **aggregated across
the 3-cycle batch**, records escalating friction patterns, and adjusts methodology
(role specs, skills, the plan). The 3-cycle window is intentional: single-cycle noise
washes out, so only persistent patterns surface as real friction.

### The construction disciplines

- **Citations are mandatory.** Every claim carries a `(file, start, end)` source range.
  No citation, no claim. Existing Palace unit tests are L0-equivalent semantic
  documentation and are cited alongside source.
- **Warrant-first / anti-mirror.** Before authoring a lower-layer image of a
  higher-layer form, an agent *first* judges whether that image is a genuine concise
  form at the lower layer. If it would only mirror the layer above, the correct output
  is a recorded NO-ENTRY warrant — not a manufactured rectangular entry.
- **Replace-and-propagate (combinator mining).** When a recurrent family is found, the
  mined combinator *replaces* the base forms as the layer's entry (the leaves become
  specialization notes) and *propagates* upward — combinators are not mined and left
  stranded beside the base forms they should subsume.
- **Optimization tricks vs. base algebra.** Transparent performance tricks are erased to
  their unfolded form with a one-line note; load-bearing numerical tricks
  (non-associative reductions, mixed precision, deterministic accumulation) are
  preserved as explicit algebraic claims with the property they buy called out.
- **Semantic consolidation — USE + LINK, don't RE-STATE.** Semantic rules/defs/abstractions
  *about the language* live ONCE on the [semantic surface](../semantics/index.md); a
  functional-unit entry keeps its own concrete fact + a link, and does not transcribe the
  general rule. A restatement at functional-unit scope is the semantic analog of a
  degenerate-identity-lowering smell, resolved by relocation-to-the-surface + a back-link.
  See [Semantic consolidation](./semantic-consolidation.md).

### Solvers as a low-priority test-load on the shared spine

The five solver pipelines and the FE-assembly half are pulled **up through the layers**
as a **low-priority test-load** on the shared inner-kernel spine — never at the cost of
forcing the spine:

- The shared spine remains primary; solver-lifting never preempts spine work.
- A solver **advances a layer only when it can be cleanly described** in that layer's
  existing shared vocabulary. If lifting a pipeline would require forcing or distorting
  the spine, **it is not done** — the spine's integrity is primary.
- **What a solver pipeline cannot cleanly say is a finding about the spine**, fed back
  as spine work. The test-load's purpose is exactly to stress-test the shared
  vocabulary and surface where it is missing, awkward, or insufficiently abstract.

### The black-box / accelerated-kernel disposition

Opaque or special operations are dispositioned three ways, by **judgment of abstraction
value** — not merely "does it decompose":

1. **Black-box kernel** — no useful decomposition, a clean opaque surface, non-local
   iterative exploration (e.g. `eigsolve`, the FE quadrature leaf). It **rises to L4 as
   an opaque-surface primitive** — the positive reframe of an "opaque-library
   obstruction."
2. **Named abstraction that decomposes but is literature-standard and aids downstream
   algorithm simplification** (e.g. `dot`, `nrm2`). It is **kept and rises to L4 as a
   named verb**, with its kernel tied below.
3. **Pure accelerated kernel** — a fused special case existing only for speed, with no
   abstraction value (e.g. the per-case `axpy` family). It is **stopped low**; the
   subsuming combinator (`linear_combination`, `inner_product`) rises instead.

Combinators must reach L4 regardless of how their specialized leaves are dispositioned.

### The kernel-API vs kernel-implementation distinction (2026-06-07 re-scope)

A black-box / opaque-library kernel that is **a dependency of something firm in the spine** AND has **a
well-understood implementation in terms of the semantics already built** is no longer left only as an opaque
obstruction. It gets **two linked surfaces, preserved for review:**

1. A **kernel-API surface** — the existing obstruction theme, repositioned as "the API." It stays claim-free
   (`status: obstruction (opaque-library-ownership)`, role-labelled `kernel-api`) and documents the opaque contract
   the spine calls: signature, semantics, the library boundary.
2. A **kernel-implementation** — a new constructive chapter realizing the kernel **from the artifact's already-firm
   primitives** (normal resolution rank, role-labelled `kernel-impl`), with ordinary `depends-on` edges to its
   constituents.

The two are joined by a **`realizes-kernel-api`** edge (impl → API) of the *navigational* `reference` class — the
implementation does **not** depend on the opaque API (it is a *correspondence to review*, not a build dependency), so
the link constrains neither rank nor liveness. A reviewer reads both the black-box contract and the from-our-primitives
version side by side and checks they match; the `lowering-verifier` audits the correspondence. The founding kernels are
the libCEED element-quadrature leaf (impl = matrix-free FE operator application as tensor contractions), the
triangular-solve / GS-SSOR relaxation (impl behind the multigrid smoother), and the SLEPc eigsolve loop (impl =
constructive Lanczos/Arnoldi/Krylov-Schur in the existing `lanczos_step` / `krylov-step` vocabulary).

**Carve-out:** enum-only-stubs (config tokens routed to an abort, e.g. MINRES/BiCGStab) are *not* external-kernel
callouts and are *not* spine dependencies — they stay single-node obstructions and get no implementation. The
dual-surface trigger is the conjunction *spine-dependency AND well-understood-in-our-semantics*.

### Scope, in one line

Single-machine (CPU → GPU via backend devices); MPI / multi-rank distribution is out
of *active* scope (a deferred future direction; flagged once, then read as single-rank).
**All five solver pipelines, MFEM-equivalent FE assembly, the geometric-multigrid
preconditioner, and AMR are in scope** (the last two single-machine-valid — parallelism by
composition). *Enum-only* Palace stubs are documented as obstruction themes, not targeted
for filling in; *spine-dependency opaque-library kernels* get a constructive implementation
alongside their kernel-API obstruction surface (the distinction above).
