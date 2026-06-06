---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-06T17:38:46Z
scope: Axis-2 reachability — audit-first disposition of the un-baseline-excepted STRONGER GARBAGE SIGNAL members (13 after correction; cycle-113 D1, batch-36)
status: pending
integrated_at: 2026-06-06T180000Z
integration_commit: d88f003
integration_notes: OBSERVATION-ONLY (D1, staging row 2) — no book/ artifact mutation (no ## Proposed changes block). Audited the 13 un-baseline-excepted STRONGER GARBAGE SIGNAL members → 1 GROUNDABLE (L1/weak_form_term via L1/fe_assemble → L1/weak_form_term, routed as a c114 grounding-dispatch candidate with companion fe_assemble→fe_space / fe_space→fe_collection edges) + 12 baseline-exception recommendations carried to the batch-36 meta-phase: RE6 (axpy-family + scal absorbed into linear_combination, 6 nodes — MUST include arity-1 scal), RE7 (elementwise_product / assemble-diagonal / L3/jacobi-smoother diagonal-preconditioner cluster, 4 nodes — RE7-vs-RE1-extension id-split judgment), RE8 (L3/fold_solve / L3/krylov-step unconsumed iteration-views, 2 nodes — RE8-vs-RE2-extension id-split judgment). Appended 5 OQ sections to scaffolding/open-questions.md (RE6/RE7/RE8/weak_form_term by the producer + RE7-cluster-completeness-add-L3-jacobi-smoother by the per-report integrator carrying the repairer's post-repair RE7 correction). One cross-reference-integrity critic warning repaired (canonical token); citecheck 11 ok / 2 failing both NON-BLOCKING (observation-only prose, lands in no book/ artifact — fe_assemble.md:67-68 path-hygiene basename slip + graded-stack-baseline-exceptions.md:116-137 off-by-one EOF overshoot, both referents verified to resolve). No reachability delta from this dispatch (observation-only). Build EXIT 0. Committed in cycle-113 finalize atomic commit.
---

# CYCLE: Cross-layer observation — 13 un-excepted STRONGER-GARBAGE-SIGNAL members dispositioned

## Summary

The 25-member STRONGER GARBAGE SIGNAL set (typed nodes unreachable from any feature
root) has 8 of its members already in the RE1–RE5 ratified node-set. I audited the
**un-dispositioned remainder** prose-by-prose against §2f FAITHFUL-PATH-OR-FINDING.
After subtracting the 8 RE1–RE5 node-set members and the 4 explicitly out-of-scope /
already-handled members (`set-subvector-zero`, `L1/normalize`, `L2/scal`, `L3/scal`),
**13 members remain to disposition** (the corrected enumeration — the c113-D2 dispatch
brief said "11," but `L3/jacobi-smoother` was not in that count and is added here as a
13th RE7 member; see §Specific finding). The
clean split is **1 GROUNDABLE + 12 baseline-exception (RE6–RE8)**, with **0 genuine
GC-delete candidates** — every member is a faithful, firm dissection that is either a
genuine constituent of a reachable node (groundable) or an absorbed-below-column /
unconsumed-iteration-view (RE-exception). The dominant pattern is the **axpy-family
arity-specialization leaves absorbed into the reachable `linear_combination` combinator**
(combinator-primary: the combinator is the entry, the arity leaves are readout labels that
nothing composes BY NAME — the typed edge runs leaf→combinator, never combinator→leaf).
`L1/weak_form_term` is the one genuine grounding case: it is the **element type of the
reachable `L1/fe_assemble` fold** (`terms: [WeakFormTerm]`), a faithful signature
constituent currently carrying no inbound `depends-on` edge — the same groundable shape as
`L1-L0/set-subvector-zero-mutation-rotation` (the c113-D2 worked exemplar).

## Observation kind

**Coverage gap / Audit residue** — Axis-2 reachability dispositions never assigned to 11
typed-but-unreachable nodes. Per §2f the disposition priority is GROUND → ROUTE-as-detritus
→ baseline-exception; this audit assigns each member its faithful-path-or-finding outcome.

## Specific finding

### Per-member disposition table

Linter run this cycle: `reachable=123, rank_violations=0, untyped=60, STRONGER GARBAGE
SIGNAL=25`. Inbound edges from `graded_stack_lint.py --show-inbound`.

| member | current inbound depends-on (reachable?) | disposition | proposed edge OR RE-id + rationale | prose citation |
|---|---|---|---|---|
| **L1/weak_form_term** | **none** | **GROUNDABLE** | edge `L1/fe_assemble → L1/weak_form_term`, kind `composes` (signature constituent — the element type of the `terms: [WeakFormTerm]` fold argument). `L1/fe_assemble` IS reachable (7 feature columns at .L1). | `book/src/L1/fe_assemble.md:60` (sig `terms: [WeakFormTerm]`), `:71-72` ("Each element is a firm `weak_form_term`"); `book/src/L1/weak_form_term.md:21,25` ("the value `fe_assemble` folds over"; "the per-term value the `fe_assemble` fold quantifies over") |
| **L2/axpy** | none | RE6 | axpy-family arity-specialization leaf absorbed into `linear_combination`; edge runs `L2/axpy → L2/linear_combination` (leaf→combinator); nothing composes the leaf by name. | `book/src/L2/axpy.md:16-32,60-64` |
| **L2/axpby** | none | RE6 | same — arity-3 readout leaf of `L2/linear_combination`. | `book/src/L2/axpby.md` (same specialization-stub shape) |
| **L2/axpbypcz** | none | RE6 | same — arity-4 readout leaf of `L2/linear_combination`. | `book/src/L2/axpbypcz.md` |
| **L3/axpy** | `L3/orthogonalize` (UNREACHABLE — RE2 member) | RE6 | arity-2 readout leaf; speaks THROUGH `L3/linear_combination` (edge `L3/axpy → L3/linear_combination`, `→ L2/linear_combination`). Its only inbound is the RE2 (garbage) orthogonalize. | `book/src/L3/axpy.md:6-8,16,36` ("speak THROUGH the combinator, not as re-derived base forms") |
| **L3/axpby** | none | RE6 | arity-3 readout leaf of `L3/linear_combination`. | `book/src/L3/axpby.md` |
| **L3/axpbypcz** | none | RE6 | arity-4 readout leaf of `L3/linear_combination`. | `book/src/L3/axpbypcz.md` |
| **L2/elementwise_product** | `L3/elementwise_product` (UNREACHABLE) | RE7 | diagonal-operator-apply kernel of the preconditioner cohort (jacobi/chebyshev), absorbed into the RE1 `op.T` leg. Edge runs `L3→L2` (down); no reachable depender. | `book/src/L3/elementwise_product.md:22,109-113` (consumers = jacobi-smoother, chebyshev, L2/chebyshev-iteration — all RE1) |
| **L3/elementwise_product** | none | RE7 | same — the L3 iteration-rotation view of the diagonal-apply kernel; consumers are the RE1 absorbed preconditioner bodies (cross-ref, not reverse-dep). | `book/src/L3/elementwise_product.md:86,109-113` (law 9 `apply_linop(DiagonalOperator(d),x) = elementwise_product(d,x)`) |
| **L3/assemble-diagonal** | none | RE7 | the operator-to-data extraction that OPENS the `assemble_diagonal → reciprocal → elementwise_product` diagonal-preconditioner chain; the gate to Jacobi/Chebyshev/block-Jacobi — the RE1 absorbed leg. | `book/src/L3/assemble-diagonal.md:16` ("gate to diagonally-scaled preconditioners ... at the iteration-rotation layer") |
| **L3/jacobi-smoother** | `L2/jacobi-smoother` (UNREACHABLE — RE1 member) | RE7 | the L3 iteration-rotation view of the diagonal-preconditioner-apply gate; per-call body is one elementwise product `op.dinv ⊙ x = (ω · D⁻¹) ⊙ x` — the thinnest constructed-operator gate. Its only inbound is the RE1 (garbage) `L2/jacobi-smoother`; `depends-on: L1/jacobi-smoother` (`lowers-to`). Same diagonal-apply cluster as the `elementwise_product`/`assemble-diagonal` kernels it cross-refs; absorbed below the RE1 preconditioner leg. | `book/src/L3/jacobi-smoother.md:19` (per-call body `op.dinv ⊙ x`, "thinnest constructed-operator gate"), `:7` (`depends-on: L1/jacobi-smoother`), `:65` (obstruction-leaf, one elementwise product) |
| **L3/fold_solve** | none | RE8 | `partial-obstruction` iteration-view; `lifts_from: L4/fold_solve` (edge `L3→L4`, UP). The reachable consumers (transient/lifecycle .L1/.L4) compose `L4/fold_solve` directly; the L3 iteration-view is unconsumed. | `book/src/L3/fold_solve.md:5-8,18,31` ("fold-image of the L4 `fold_solve` combinator"; consumers compose L4) |
| **L3/krylov-step** | none | RE8 | iteration-view; `lifts_from: L4/krylov-step` (edge `L3→L4`, UP). The reachable `L4/krylov-step` (consumed by `L4/ksp_solve`) composes downward to L2 directly; the L3 iteration-view is unconsumed. | `book/src/L3/krylov-step.md:5-8,20,24,28-29` ("value-thread-isomorphic ... the L4 form's do-block dissolves to a let-chain") |

### The three structural classes (mirroring RE1–RE5 cluster logic)

1. **axpy-family arity-specialization leaves (6 nodes: L2/L3 axpy/axpby/axpbypcz).** The
   `linear_combination` combinator IS reachable at all three layers (`L4/linear_combination
   ← L4/eliminate_bc, L4/assemble_frequency_operator`; `L3/linear_combination ←
   L4/linear_combination`; `L2/linear_combination ← L3/linear_combination, ...`). The
   combinator is the entry; the arity forms are **readout labels** that speak THROUGH it.
   The typed edge ALWAYS runs leaf→combinator (`L3/axpy → L3/linear_combination →
   L2/linear_combination`), never combinator→leaf — so the leaves are absorbed below the
   reachable combinator and never marked. This is the textbook combinator-primary
   absorbed-leaf pattern (CLAUDE.md §VOCABULARY-SHIFT REDIRECT: "the combinator is the
   entry, leaves are specialization notes"). → **RE6**.
   - **NOTE (out-of-scope sibling):** `L2/scal` and `L3/scal` are the arity-1 members of
     the SAME family (also STRONGER-GARBAGE, also leaf→combinator) but are NOT in this
     dispatch's 11-member scope and NOT yet in RE1–RE5. They belong in the RE6 cluster by
     the identical rationale. Flagged for the meta-phase to include in RE6 (or as a
     companion RE6b) so the cluster is complete — leaving them stranded would re-trip the
     "count climbs without a ratified RE" re-open trigger.

2. **diagonal-preconditioner apply/extract kernels (4 nodes: L2/L3 elementwise_product,
   L3/assemble-diagonal, L3/jacobi-smoother).** These are the `assemble_diagonal → reciprocal →
   elementwise_product` diagonal-apply chain plus the L3 diagonal-apply gate
   (`L3/jacobi-smoother`, whose per-call body IS that single elementwise product
   `op.dinv ⊙ x`) — exactly the RE1 preconditioner leg absorbed
   into the constructed `op.T = A·M⁻¹`. Their declared consumers (jacobi-smoother,
   chebyshev, L2/chebyshev-iteration) are RE1 members; the relationship is cross-reference
   (`## Consumers`), NOT reverse-dependency. `L3/jacobi-smoother`'s only inbound is the RE1
   `L2/jacobi-smoother` (down-edge from the absorbed L2 leg), and its `depends-on:
   L1/jacobi-smoother` (`lowers-to`) does not introduce a reachable depender. The typed edge runs L3→L2 (down); no reachable
   node depends-on them by name. This is an RE1-shaped cluster (absorbed-below-column
   diagonal-apply kernels). → **RE7** (could equally be folded as an RE1-extension; I
   propose a distinct RE7 id because RE1's promotion condition is keyed to a
   preconditioner-construction *feature surface*, whereas these kernels also ride the
   `reciprocal`/RE5 chain — keeping them separable keeps the promotion conditions clean).

3. **unconsumed L3 iteration-views over reachable L4 combinators (2 nodes: L3/fold_solve,
   L3/krylov-step).** Both carry `lifts_from: L4/<op>` — the typed edge runs L3→L4 (UP),
   so grounding the L4 node does NOT carry liveness UP into the L3 iteration-view. The
   reachable consumers compose the **L4** combinator directly (transient/lifecycle compose
   `L4/fold_solve`; `L4/ksp_solve` composes `L4/krylov-step` then downward to L2). The L3
   iteration-rotation view is a real-but-currently-unconsumed dissection — faithful, firm
   (`fold_solve` is `partial-obstruction`), but no live depender. This is the RE2 shape
   (deliberately-composed-at-a-different-altitude iteration-view) generalized to the L4→L2
   skip. → **RE8** (distinct from RE2: RE2 is L3-composed-at-L2; this is
   L3-iteration-view-skipped-because-the-reachable-consumer-composes-at-L4).

## Recommendation

### (a) c114 grounding-dispatch finding list (route to `layer-intro-author` — the typed-edge home)

ONE faithful grounding edge to add (the only GROUNDABLE node among the 13), mirroring the c113-D2 `set-subvector-zero` grounding:

- **`L1/fe_assemble → L1/weak_form_term`**, `kind: composes` (signature constituent /
  fold element-type). Faithful because `weak_form_term` is literally the element type of
  `fe_assemble`'s `terms: [WeakFormTerm]` argument — the value the fold quantifies over
  (`book/src/L1/fe_assemble.md:60,71-72`; `book/src/L1/weak_form_term.md:21,25`). This is
  a genuine consumed-by-name constituent (a data-shape member of the signature), NOT a
  lowering and NOT a sibling reference — so it is a FAITHFUL `depends-on`, not a false
  grounding edge. Grounding `weak_form_term` also grounds its downstream
  `L1-L0/fe-assemble-libceed-boundary-obstruction` transitively (existing edge
  `weak_form_term → fe-assemble-libceed-boundary-obstruction`), retiring that
  obstruction-leg node from detritus as a free rider — no separate disposition needed.
  - **Adjacent context (out of my 11-member scope, same grounding pattern):** `L1/fe_space`
    and `L1/fe_collection` are edge-untyped detritus (NOT STRONGER-GARBAGE), and ground the
    same way — `fe_space` is `fe_assemble`'s `space: FiniteElementSpace[N]` argument
    (`fe_assemble.md:67-68`), `fe_collection` feeds `fe_space`. The c114 grounding dispatch
    should add `L1/fe_assemble → L1/fe_space` (composes) and `L1/fe_space →
    L1/fe_collection` (composes) in the same pass to ground the whole FE-vocabulary leg off
    the reachable `fe_assemble`. Flagged as a companion, not part of this audit's verdict.

### (b) batch-36 meta-phase RE6+ ratification recommendation

Three new reachability baseline-exception clusters, RE1–RE5 entry format:

| # | unreachable node(s) | why no faithful column→node edge exists | TRUE disposition | promotion condition |
|---|---|---|---|---|
| **RE6** | `L2/axpy`, `L2/axpby`, `L2/axpbypcz`, `L3/axpy`, `L3/axpby`, `L3/axpbypcz` (+ companion `L2/scal`, `L3/scal`) | the **combinator IS the entry**: `linear_combination` is reachable at L2/L3/L4 (`L4/linear_combination ← L4/eliminate_bc`); the arity forms are readout labels that speak THROUGH it. The typed edge ALWAYS runs leaf→combinator (`L3/axpy → L3/linear_combination`), never combinator→leaf. Forcing `linear_combination → axpy` would invert the combinator-primary direction (a combinator does not depend-on its own specialization leaves). | **baseline-exception** — combinator-primary arity-specialization leaves absorbed into the reachable `linear_combination` combinator (CLAUDE.md §VOCABULARY-SHIFT REDIRECT: combinator is the entry, leaves are specialization notes). | a future driver/feature column that names a *concrete arity form* as a separable composed verb via a faithful `depends-on` path (none expected — the combinator is the composition surface), OR the leaves are demoted to in-chapter `## Arity specializations` notes inside `linear_combination` (a real-but-deferred refactor that would remove them as standalone DAG nodes entirely). (New OQ proposed below.) |
| **RE7** | `L2/elementwise_product`, `L3/elementwise_product`, `L3/assemble-diagonal`, `L3/jacobi-smoother` | the `assemble_diagonal → reciprocal → elementwise_product` diagonal-apply chain plus the L3 diagonal-apply gate `L3/jacobi-smoother` (per-call body = that one elementwise product `op.dinv ⊙ x`) is **absorbed into the RE1 preconditioner leg** (the constructed `op.T = A·M⁻¹`); declared consumers (jacobi-smoother, chebyshev, L2/chebyshev-iteration) are RE1 members and the relationship is `## Consumers` cross-reference, not reverse-dependency. `L3/jacobi-smoother`'s only inbound is the RE1 `L2/jacobi-smoother`. Typed edge runs L3→L2 (down); no reachable node depends-on these kernels by name. | **baseline-exception** — diagonal-preconditioner apply/extract kernels (incl. the thinnest L3 diagonal-apply gate `L3/jacobi-smoother`) absorbed below the RE1 leg (RE1-shaped; kept separable because they also ride the RE5 `reciprocal` chain). | grounding of the RE1 preconditioner leg (a preconditioner-construction feature surface that names the diagonal-apply kernel as a constituent) carries liveness into this chain via the existing faithful `depends-on` edges; no edit to these nodes needed — they ground transitively when RE1 grounds. (Shares RE1's OQ.) |
| **RE8** | `L3/fold_solve` (`partial-obstruction`), `L3/krylov-step` | both carry `lifts_from: L4/<op>` — the typed edge runs L3→L4 (UP), so grounding the reachable L4 node does NOT carry liveness UP into the L3 iteration-view. The reachable consumers compose the **L4** combinator directly (transient/lifecycle compose `L4/fold_solve`; `L4/ksp_solve` composes `L4/krylov-step`); no consumer reaches the L3 iteration-view. Forcing `L4/fold_solve → L3/fold_solve` would assert a constituent-use that does not exist (the L4 combinator IS the iteration view at its altitude; the L3 form is the dissolution image, not a folded constituent). | **baseline-exception** — real-but-currently-unconsumed L3 iteration-views over reachable L4 combinators (RE2 shape generalized to the L4→L2 altitude skip). | a future driver/feature column that composes the L3 (iteration-rotation) form as a named constituent — e.g. a transient-march feature surface naming the explicit value-threaded sweep, or a Krylov-iteration-structural surface — via a *faithful* future column edge, NOT a forced edge. (New OQ proposed below.) |

**Cluster-completeness caveat for the meta-phase:** RE6 must include the arity-1 `scal`
members (`L2/scal`, `L3/scal`) even though they are outside this dispatch's assigned 11 —
they are the SAME combinator-leaf pattern and will otherwise persist as un-ratified
STRONGER-GARBAGE, tripping the documented re-open trigger ("count climbs without a new
ratified RE entry"). After RE6–RE8 land (RE7 now including `L3/jacobi-smoother` — the L3
diagonal-apply gate added in the corrected enumeration), the STRONGER-GARBAGE residual
should be: RE1–RE8 (the full ratified set) + the lazy-untyped tail + the demand-gated
`deflate` frontier — no un-dispositioned typed-but-unreachable node remaining except
`weak_form_term` (grounded by the c114 dispatch above).

## Supporting evidence

- Baseline-exception ledger (RE1–RE5 format + re-open triggers):
  `scaffolding/graded-stack-baseline-exceptions.md:116-137`.
- axpy-family combinator-primary absorption: `book/src/L3/axpy.md:6-8,16,36`;
  `book/src/L2/axpy.md:16-32,60-64`; combinator reachability via
  `graded_stack_lint.py --show-inbound` (`L4/linear_combination ← L4/eliminate_bc,
  L4/assemble_frequency_operator`; `L3/linear_combination ← L4/linear_combination`).
- diagonal-apply cluster: `book/src/L3/elementwise_product.md:22,86,109-113` (law 9 +
  consumers); `book/src/L3/assemble-diagonal.md:16,22` (gate to diagonal preconditioners).
- iteration-view cluster: `book/src/L3/fold_solve.md:5-8,18,31` (`lifts_from: L4/fold_solve`,
  fold-image); `book/src/L3/krylov-step.md:5-8,20,24,28-29` (`lifts_from: L4/krylov-step`,
  value-thread-isomorphic). L4 nodes confirmed reachable (absent from the GC garbage list).
- grounding case: `book/src/L1/fe_assemble.md:60,67-68,71-72` (signature constituents
  terms/space); `book/src/L1/weak_form_term.md:21,25` ("the value `fe_assemble` folds
  over"); `book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md:1-25`
  (obstruction-leg free rider).

## Open questions / caveats

- **RE7 vs RE1-extension judgment.** I propose RE7 as a distinct id rather than folding the
  diagonal-apply kernels into RE1, because RE1's promotion condition is keyed to a
  preconditioner-construction feature surface while these kernels also ride the RE5
  `reciprocal` chain. The meta-phase may prefer to extend RE1's node list instead — either
  is faithful; the cluster rationale is identical. Flagging the choice, not pre-deciding it.
- **RE8 vs RE2 judgment.** Same: RE8 could be read as an RE2-extension. I separated it
  because RE2 is specifically "L3-composed-at-L2 (orthogonalize)" whereas RE8 is
  "L3-iteration-view-skipped-because-the-reachable-consumer-composes-at-L4". The promotion
  conditions differ (RE2 wants an L3-orthogonalize-composing column; RE8 wants a
  transient-march / Krylov-iteration-structural column). Meta-phase to ratify the id split
  or merge.
- **`scal` cluster-completeness.** `L2/scal`/`L3/scal` are RE6-shaped but outside this
  dispatch's scope. I recommend including them in RE6; if the meta-phase scopes RE6 to
  exactly my 6 assigned axpy/axpby/axpbypcz nodes, `scal` will persist as un-ratified
  STRONGER-GARBAGE and should be explicitly noted as a known-residual to avoid a false
  re-open signal next batch.
- **No GC-delete candidates.** Per the GROUND-don't-remove directive, I applied GROUND
  first (→ weak_form_term) then baseline-exception (→ RE6/RE7/RE8); none of the 11 is a
  genuine detritus-delete. The axpy/scal leaves are the closest to deletable (they could be
  demoted to in-chapter notes inside `linear_combination`), but that is a refactor to
  propose, not a GC-sweep delete — recorded as RE6's promotion condition.
- **`L1/normalize` appears in the live STRONGER-GARBAGE list** (`graded_stack_lint.py`
  output line) but is NOT in my assigned 11 and is the consumer-side of the RE5
  normalize/reciprocal chain — already covered by RE5's transitive-grounding note. No action
  here; flagged only so the meta-phase doesn't read its presence as un-dispositioned.
