---
agent: layer-intro-author
invoked_at: 2026-06-02T19:19:30Z
scope: methodology GOAL+FLOW chapter v1 seed (book/src/methodology/goal-flow.md)
status: pending
integrated_at: 2026-06-02T193833Z
integration_commit: 33a56f6
integration_notes: "cycle-067 D4 — applied clean. NEW methodology/goal-flow.md (directive-4 v1 seed; NON-AUTHORITATIVE synthesized GOAL+FLOW mirror, mandatory 4-facet header present) + SUMMARY.md row under # Methodology after overview.md. 2 OQs promoted (ownership-transfer + single-chapter-vs-split). Ownership transfers to the meta-phase post-seed (restart-pending). citecheck no-op by design (no L0 citations). Build-relevant; cargo make book exit 0; page renders. Staging row: cycle-067-integrator-staging/STAGING.md."
---

# CYCLE: Methodology GOAL+FLOW chapter (v1 seed)

## Summary

Seeds the reader-facing **Methodology GOAL+FLOW chapter** at `book/src/methodology/goal-flow.md` (directive-4 enactment, plan-tag `methodology-goal-flow-chapter-v1-seed`). The chapter is a **synthesized, NON-AUTHORITATIVE descriptive mirror** of the project's emergent goal + how it is met — a single chapter (author's structural judgment for v1, per the dispatch spec's "single chapter preferred").

Two sections:
- **GOAL** — the integrated view of what the book is *for*: the L4→L0 incremental impedance-matching stack; L4 as the outward backend-lowering feature surface (its semantics aligned with external GPU-tensor-accelerator + distributed backends; must be COMPLETE over the in-scope feature set — all 5 solver pipelines + FE assembly); the layered representational/vocabulary shifts (NOT a rectangular projection); each layer complete/concise/correct in itself; lowerings as translations not renames.
- **FLOW** — how those goals are met: the 5-phase primary cycle + every-3rd-cycle meta-phase cadence; warrant-first / anti-mirror / replace-and-propagate discipline; the solver-test-load as a low-priority test-load on the shared spine; citation grounding; the black-box / accelerated-kernel three-way disposition.

A **mandatory non-authoritative / synthesized-view / review-point header** sits at the top. The chapter notes that **ownership transfers to the meta-phase post-seed** (refreshed each batch). Plus one `SUMMARY.md` row under the existing `# Methodology` Part, after `overview.md`.

This is the dispatch phase — proposed-changes only; the integrator applies. I did NOT mutate `book/`.

## Proposed changes

Two file edits: (1) create `book/src/methodology/goal-flow.md`; (2) insert one `SUMMARY.md` row.

```edit:book/src/methodology/goal-flow.md
[new]:
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
```

```edit:book/src/SUMMARY.md
[old]:
# Methodology
- [Overview](./methodology/overview.md)
[new]:
# Methodology
- [Overview](./methodology/overview.md)
- [Goal & Flow](./methodology/goal-flow.md)
```

## Supporting evidence

Authoritative sources read and synthesized from (NOT cited as L0 — this is a
methodology mirror, not an operator entry):

- `CLAUDE.md` (repo root) — Extraction goal (L0–L4 + lowering layers); the 5-phase
  primary cycle + every-3rd-cycle meta-phase cadence (§"Cycle structure"); citation
  discipline; optimization-trick distinction; scope (all 5 solvers + FE assembly,
  single-machine, MPI out-of-scope); §"Methodology invariants" vocabulary-shift
  redirect bullet; black-box/accelerated-kernel memory bullet.
- `METHODOLOGY-REDIRECT.md` (2026-06-01) — §1 the principle (1a–1d: representational
  shifts, layer-complete-in-itself, lowerings-are-translations, degenerate-lowering
  smell); §2 supersession of the rectangular target; §5 solvers-as-low-priority-test-load;
  §6 what "complete" means.
- `scaffolding/priorities.md` — the plan-is-the-work-artifact framing; warrant-first /
  anti-mirror / replace-and-propagate discipline in live use (c057/c059 warrant-first
  abstractor leads; the `solve_family` / `fold_solve` MAP/FOLD combinators); the
  solver-test-load arc (batch-16/17/18 enactments).
- Project memory — `project_l4_is_backend_lowering_target.md` (L4 = outward
  backend-lowering feature surface, every in-scope feature must reach L4),
  `project_blackbox_vs_accelerated_kernels.md` (the three-way disposition),
  `project_vocabulary_shift_redirect.md`, `feedback_methodology_goal_flow_chapter.md`
  (this chapter's own non-authoritative / synthesized-mirror / meta-phase-ownership
  charter), `feedback_mdbook_subchapter_grouping_and_alpha_api.md`.
- `book/src/introduction.md` + `book/src/methodology/overview.md` — matched tone and
  the existing L0–L4 framing; this chapter deepens what `overview.md` points at without
  displacing `CLAUDE.md` as the operational source.
- `book/src/SUMMARY.md` lines 4-5 — the existing `# Methodology` Part with only
  `overview.md`; insertion is after it (directive-3 wiring active-immediately).

## Open questions / caveats

- **Single-chapter vs split:** authored as one `goal-flow.md` per the dispatch spec's
  "single chapter preferred for v1." If the meta-phase finds GOAL and FLOW each growing
  past the ~200-line orientation budget on later refreshes, splitting into `goal.md` +
  `flow.md` (two SUMMARY rows) is the natural next move — flagged for the meta-phase as
  the inheriting owner.
- **mdBook sub-chapter grouping (directive 2026-06-02):** the Methodology Part now has
  two flat chapters (`overview`, `goal-flow`). If the per-Part by-kind sub-chapter
  reorg lands, the Methodology Part is small enough that flat is fine for now; no group
  intro is needed yet. Noted so the reorg pass does not over-structure a 2-chapter Part.
- **Drift-watch is the meta-phase's standing job:** I synthesized the supersession
  relationships (rectangular → vocabulary-shift; the batch-14 "L4-complete / pivot" ASK
  retired) from the redirect + priorities banners as of 2026-06-02. These are the
  most-recently-moved pieces of the goal; if a later source movement contradicts the
  chapter, the source wins and the meta-phase corrects the chapter (per the header). I
  did not invent any goal content not present in a source.
- **No L0 citations in this chapter by design** — it is a methodology mirror, not an
  operator/theme entry, so the citation-validity check no-ops on it; the critic should
  verify only that the non-authoritative header is present, the SUMMARY wiring resolves,
  and no claim contradicts the named sources.
- **`overview.md` overlap:** the existing `methodology/overview.md` says "read
  `CLAUDE.md` for the methodology" and points at the same sections. This chapter does
  NOT duplicate that pointer-page role — it is the synthesized integrated view, where
  `overview.md` is the navigational stub. If the meta-phase later wants to fold
  `overview.md` into this chapter (or vice-versa), that is a meta-phase consolidation
  call, not in this seed's scope.
```
