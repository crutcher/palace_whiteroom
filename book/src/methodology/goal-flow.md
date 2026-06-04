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
> single-constituent (`gram_reduce`) gate — but did not flip them. **The remaining lever is now a
> single convergent foundation-blocker: the `matrix-weighted-norm` √-entry-point cascade**, which
> gates `gram_reduce` (→ four columns) AND `domain_energy_reduce` (→ energy-fields) — 5 of the 6
> stay-seed columns converge on it. The in-scope law-confidence route is exhausted for the
> all-primitives-firm cohort (the norm-axiom laws may genuinely be inner-product-structure theorems
> the source only numerically asserts, not syntactic identities); the next probe is a scoped
> literature-anchor pass on those norm axioms — the cheap test of whether that one gate is
> dischargeable at all, before any heavy ~30-file cascade wave.

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

### Scope, in one line

Single-machine (CPU → GPU via backend devices); MPI / multi-rank distribution is out
of scope (flagged once, then read as single-rank). **All five solver pipelines and
MFEM-equivalent FE assembly are in scope.** Unimplemented Palace stubs are documented as
obstruction themes, not targeted for filling in.
