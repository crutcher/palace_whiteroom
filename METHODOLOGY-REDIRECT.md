# Methodology redirect — 2026-06-01 (vocabulary-shift stack · translational lowerings · solvers as test-load)

**Status:** user directive, 2026-06-01. Peer artifact to `MIGRATION.md` (the 2026-05-26 structural redirect). This document is the *full spec*; `CLAUDE.md` §Methodology invariants carries the operational distillation and the supersession pointers.

**What it does:** corrects a drift in how the layered stack is built. The construction machinery, in trying to make cross-layer lowerings explicit and auditable, accidentally optimized for lowerings that are *trivial to verify* — and the easiest lowering to verify is the identity / 1:1-named map. That preference propagated downward into the **layers**, forcing each layer to carry the same named operators as its neighbor (a **rectangular projection** up the stack). A rectangular stack has no conciseness gradient between layers, so it generated **no pressure to abstract** — which is why combinators were mined and then stranded (e.g. `linear_combination` lifted once at L2, never propagated, while `axpy`/`axpby`/`axpbypcz` were re-stated in base form at L1, L2, and L3).

This redirect replaces the rectangular target with the founding intent: a stack of **genuine representational + vocabulary shifts**, joined by **translational** lowerings.

---

## 1. The principle

**1a — The stack is a sequence of representational shifts, not a projection.** Climbing one layer changes both the *representation* and the *component vocabulary* of the pieces. Different named operators, different combinators, different semantic organization at each level — **by design**. Two adjacent layers sharing a named operator is permitted only when that operator is genuinely primitive at both; it is never a goal, and a layer that mirrors its neighbor's vocabulary wholesale has failed to shift.

**1b — Each layer is complete, concise, and correct *in itself*.** A layer is a self-contained representation in its *own* vocabulary. The **conciseness** constraint is the engine of the methodology: a layer forced to express itself concisely is forced to **factor out in-layer utility combinators and abstractions**. This is where pieces like `linear_combination` (the `axpy`/`axpby`/`axpbypcz`/`scal` family), `inner_product` (the `dot`/`nrm2` family), and their kin are supposed to come from — and where they are supposed to **live and be used**, not sit beside the base forms they should replace. In-layer abstraction is mined *inward* to simplify the layer; it is distinct from the cross-layer lowering themes.

**1c — Lowerings are translations, not renames.** Each lowering (`L_{n+1} > L_n`) is itself complete, concise, and correct — and it is a **translation across vocabularies and semantic organizations**, not a 1:1 named-term correspondence. A good lowering shows how a concise higher-layer form *reorganizes* into the concise lower-layer form, whose named pieces may be entirely different. The "concise + correct + complete" constraint on the lowering applies **pressure on the layer designs**: the layer vocabularies should be chosen so the translation between them is clean and expressible. The constraint is *not* satisfied by making the layers identical so the translation becomes a rename.

**1d — A degenerate (identity-in-named-terms) lowering is a smell, not a deliverable.** If a lowering turns out to be a 1:1 rename, that is evidence the vocabulary **failed to shift** between those layers — investigate it, do not enshrine it. Two legitimate outcomes of the investigation: (i) the piece is genuinely primitive at both layers and needs no elaborate per-layer restatement (a thin note suffices, not a full mirrored entry + a thin theme); or (ii) the higher layer should be expressing the piece through a more abstract combinator that *is* that layer's concise vocabulary, making the lowering a real translation. What is **not** an acceptable outcome is manufacturing a mirrored entry at each layer plus a thin "body-identity" theme to connect them.

---

## 2. What this supersedes or revises

| Artifact | Disposition |
|---|---|
| **"Uniform pull-up L0→L4; foundation-solidity is a ranking weight" (2026-05-31)** and its **"rectangular" success metric** | **Superseded.** "The stack self-corrects toward rectangular" is the bug, not the goal. The `foundation_solidity` ranking weight, the count-ownership and dual-registration machinery, and the L2-floor / L3>L2-rotation "fill the middle" campaign were built to *manufacture* rectangularity. Retire the rectangular target; keep only the parts that serve in-layer conciseness and translational lowerings (see §4). |
| **"Identity-lowerings still require both L levels" (2026-05-27)** | **Superseded by 1d.** A genuine identity-in-named-terms across layers is now a smell to investigate, not a mandate to mirror the entry at both levels. The conclusion it reaches must be a thin note or a combinator re-expression — not a mirrored base-form entry + a thin connecting theme. |
| **Leaf-vs-fold fork, ratified (b) "keep the base-form leaf alongside the fold, cited-not-merged, for layer coherence" (batch-12 meta-phase)** | **Reversed → fold/combinator-primary.** The concise form (the combinator) is what a layer carries; the leaves are specialization *notes under* the combinator, not standalone mirrored entries. Layer coherence is served by the layer's own concise vocabulary, not by re-stating every base-form leaf. |
| **Thin "body-identity" `L3>L2` / `L2>L1` themes (cycles 041–045)** | **Demoted.** These are the 1:1 named lowerings 1d names as a smell. They exist only because the layers were forced flat. They are refactored away (folded into combinator specialization notes / thin in-line notes) as part of §3. |
| **"Identity rotations across non-adjacent layers are annotated in-line" (cycle-012)** | **Retained, generalized.** The in-line-note treatment of a degenerate rotation is the *correct* lightweight outcome of a 1d investigation. It generalizes from non-adjacent to adjacent: a degenerate adjacent rotation is also an in-line note, not a manufactured theme. |
| **Combinator-miner role** | **Strengthened (see §4).** Its job is in-layer abstraction; it must now **replace-and-propagate**, not mine-and-strand. |
| **"Lower-level shared vocabulary takes priority" (2026-05-27)** | **Retained, reinforced.** Consistent with 1b — but now the priority is *abstraction-bearing* shared vocabulary, not base-form floors. |

Nothing in `MIGRATION.md` (the L4→L0 impedance-matching stack, the 6-phase cycle, the citation discipline, the per-layer mdBook Part structure) is superseded. This redirect changes *what good layer content and good lowering content look like*, not the pipeline that produces them.

---

## 3. The refactor pass (the already-built rectangular floors)

The L2/L3 base-form leaves and their thin body-identity themes built in cycles 041–048 are the materialized drift. They are **refactored**, not left in place. Concretely, over subsequent cycles:

- **Collapse base-form leaf entries into in-layer combinators.** The `axpy`/`axpby`/`axpbypcz`/`scal` family becomes specialization notes under an in-layer `linear_combination` combinator at each layer where the family appears; `dot`/`nrm2` under `inner_product`; and so on as the combinator-miner identifies the families. The combinator is the entry; the leaves are notes.
- **Propagate the combinator upward.** Where a combinator is the concise form at L2, the L3 and L4 expressions are built *in terms of it* (or its layer-N analog), not re-derived in base form. The combinator climbs; the base form does not.
- **Demote the thin body-identity themes** to in-line notes (per 1d / the retained-generalized cycle-012 convention) or remove them where the combinator re-expression makes them vacuous.
- **Re-audit every lowering touched** under 1c/1d: confirm it now reads as a translation (or is correctly a thin in-line note), not a manufactured rename.

The refactor is sequenced and fan-out-ranked like any other work; it is not a single big-bang rewrite. It precedes new forward-frontier construction in priority (a stack built on the corrected shape is the foundation everything else rests on).

---

## 4. Combinator-miner re-mandate: replace-and-propagate

The combinator-miner's deliverable is no longer "here is a pattern that could be a combinator at this layer or the next." It is:

1. **Identify the in-layer family** (driven by the conciseness pressure of 1b).
2. **Propose the combinator as the layer's entry**, with the family members as specialization notes — i.e. *replace*, not sit-beside.
3. **Propose the propagation**: which higher layers should express their forms through this combinator (or its analog) rather than re-deriving base forms.
4. **Flag any lowering that would become degenerate** under the new combinator as a 1d smell to convert to a translation or an in-line note.

`harvester`, `abstractor`, `layer-intro-author`, and `cycle-planner` role-specs carry the matching producer/planner-side bullets (conciseness-drives-abstraction; lowerings-are-translations; the degenerate-lowering smell check). These role-spec edits trigger the standard session restart before they take effect.

---

## 5. Solvers as a low-priority test-load

Begin pulling the five solver pipelines (electrostatic, magnetostatic, eigenmode, driven, transient) — and the FE-assembly / mesh / FE-space half that is equally in scope — **up through the layers**, with these constraints:

- **Low priority.** The shared spine (the inner-kernel vocabulary, now under refactor) remains primary. Solver-lifting never preempts spine work.
- **Solvers are a test-load on the shared framework.** Their purpose in being lifted is to *exercise and stress-test the shared vocabulary*, surfacing where it is missing, awkward, or insufficiently abstract. What a solver pipeline cannot cleanly say in the existing shared vocabulary is a finding about the **spine**, fed back as spine work.
- **A solver advances a layer only when it can be cleanly described** in that layer's vocabulary. If lifting a pipeline a layer would require forcing or distorting the shared spine, **you do not do it** — the spine's integrity is primary. Solvers advance opportunistically, when the spine already makes the description clean, never on a forced or rectangular schedule.

This also corrects the denominator error in the "L4 substantially complete" assessment (batch-14 meta-phase): that claim was *complete relative to the already-lifted inner-kernel cohort*, not relative to the in-scope target. By the project's own scope ("Solvers in scope: all 5"; "Mesh / FE-space construction in scope"), the construction phase is not winding down — the shared spine is built (and being refactored to the correct shape), and the per-pipeline + assembly breadth is the remaining frontier, now pursued as a low-priority test-load. The batch-14 strategic ASK ("is layer-construction done / pivot to burn?") is **answered**: continue building the shared spine on the corrected (vocabulary-shift) model, with solvers as a low-priority test-load; no pivot to the downstream burn effort yet.

---

## 6. What "complete" means now

- **A layer is complete** when every operator that *belongs at that layer* is expressed in that layer's own concise vocabulary (combinators where conciseness demands them; base forms only where genuinely primitive), and each such operator has a lowering that reads as a clean translation (or a justified thin in-line note). It is **not** complete by mirroring the layer below.
- **A lowering is complete** when it faithfully translates the higher layer's vocabulary into the lower layer's, with applicability conditions and the reorganization made explicit — not when it renames.
- **The stack is complete** when the in-scope target (all five solver pipelines + FE assembly, atop the shared spine) is expressed this way end-to-end. The shared spine being substantially built is a milestone, not completion.

---

## 7. Enactment

1. This document + the `CLAUDE.md` distillation land first (no cycle work; durable methodology).
2. Role-spec edits (combinator-miner, harvester, abstractor, cycle-planner, layer-intro-author) per §4 — **session restart required** before they take effect.
3. The batch-15 program (reshaped in `scaffolding/priorities.md`): **(i)** the refactor pass (§3) — highest priority; **(ii)** continued shared-spine abstraction under the corrected model; **(iii)** solvers as the low-priority test-load (§5).
4. The batch-14 meta-phase's "L4 near-exhaustion / strategic-pivot ASK" framing is retired (answered by §5).
