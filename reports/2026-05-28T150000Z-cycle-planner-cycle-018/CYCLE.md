---
agent: cycle-planner
invoked_at: 2026-05-28T150000Z
scope: cycle-018 dispatch plan (third/final primary cycle of meta-batch-4)
status: pending
---

# Cycle-018 dispatch plan

## Goals selected this cycle

Cycle-018 is the **third/final primary cycle of meta-batch-4** (cycles 016/017/018; the batch-4 meta-phase fires AFTER this cycle's finalize, aggregating the full 3-cycle batch). The goals this cycle are to:

1. **Close the BLAS-1 unification on the constructive payoff**: cycle-017 combinator-miner landed the rough-in dep-map row for `linear_combination`; this cycle harvesters the firm L2 operator entry (signature, laws, empirical match), then abstractors the lowering theme narrating the four fixed-arity specializations. This is the highest-value frontier item opened by cycle-017.

2. **Clear ≥2-firm-instance gate and launch the new concept page**: cycle-017 cross-layer-cross-cutter's audit cleared the bar for `nested-constructed-operator-gate` concept page (eigsolve cycle-011 + divfree cycle-016 are the two firm instances). This concept unifies a recurring gate-carrying-gate pattern and blocks downstream divfree-theme correction work.

3. **Carry-forward the divfree-theme "first"-claim correction**: scoped append-only fix to the firm `book/src/L1-L0/divfree-projector-mutation-rotation.md` citing the previously-undiscovered earlier instance (cycle-011 eigsolve sub-pattern B). This depends on the nested-gate concept page landing first.

4. **Prioritize lower-layer shared vocabulary** (user directive 2026-05-27, mid-cycle-009; active guidance): dispatch L2 (harvester on `linear_combination`), L1>L0 lowering themes (abstractor), and concept pages (layer-intro-author) above further L4 expansion (the GMRES v0.6→v0.7 carry-forward is notable but deferred to cycle-019+ when L2/L3 saturation demands it).

## Dispatches

**Dispatch 1: `harvester` — `linear-combination-harvester-formalization`**
- **Agent:** harvester (opus)
- **Scope:** Formalize `linear_combination :: [(Scalar, Tensor[N])] -> Tensor[N]` as a firm L2 operator. Author `book/src/L2/linear_combination.md` with: (i) signature + shape precondition (list length ≥1); (ii) algebraic laws: empty-list identity (nil case), concatenation-homomorphism (the defining fold law), multilinearity (`linear_combination(coeffs_scaled)` and `linear_combination(flat_list)`), scalar-absorption (`[( α, [( β, x )])` = `[(α·β, x)]`), zero-coefficient term-drop (compile-time optimization, load-bearing for sparsity); (iii) **exact-arithmetic law**: permutation-invariance + IEEE-754 non-associative-reduction paired **non-law** (match the `axpby`/`axpbypcz` precedent from cycles-011/012); (iv) output-aliasing variant axis (in-place forms); (v) four fixed-arity specializations (arity-1 → `scal`, arity-2-coeff-1-fixed → `axpy`, arity-2 → `axpby`, arity-3 → `axpbypcz`); (vi) empirical_match citations from `test/unit/test-vector.cpp` per-arity assertions; (vii) SUMMARY-register at `book/src/L2/index.md` as a firm row (update the rough-in dep-map row that cycle-017 combinator-miner placed); (viii) state in prose that permutation-invariance is exact arithmetic, IEEE is the non-law, matching the precedent.
- **Deps:** none (independent)
- **Rationale:** Unblocked by cycle-017 combinator-miner's rough-in row. This is the constructive payoff of the human-raised BLAS-1 variadic-fold unification (OQ `blas1-variadic-linear-combination-fold-unification`). The four fixed-arity specializations already exist as firm L1 operators; the `linear_combination` firm entry makes the unification manifest at L2. Critical for next dispatch to unify the lowering theme.

---

**Dispatch 2: `layer-intro-author` — `nested-constructed-operator-gate` concept page**
- **Agent:** layer-intro-author (opus)
- **Scope:** Author `book/src/concepts/nested-constructed-operator-gate.md`. Document: (i) the shape: a constructed-operator closure field that itself carries another constructed-operator gate (e.g., divfree `P` with closure field `P.ksp : Solver[P.M]`, where `ksp_solve` is itself a constructed-operator gate); (ii) cross-layer fidelity rule: the inner gate's iteration stays interior to its own theme; (iii) instance index with three-deep transitivity listed: eigsolve → divfree → ksp (eigsolve's `E.projector` IS the divfree projector; divfree's `P.ksp` IS a ksp_solve gate; full chain: `eigsolve.projector.ksp`); (iv) sibling relations to `constructed-operator-factory` concept; (v) **two confirm-before-cite caveats**: (a) eigsolve is fully firm (`L1/eigsolve.md`) despite carrying a partly-constructive sub-part (`LinearSolveFailed` status value per cycle-013 record); (b) the latent `K.M⁻¹`-as-`Solver[K.M]` site in the ksp-solve closure needs L0 Palace confirmation before being listed as a third gate instance (check `palace/linalg/ksp.cpp` for the `Solver`-type assignment in the constructor or field initializer). EMIT proposed-changes block; do NOT write `book/src/` directly.
- **Deps:** none (concept page is independent)
- **Rationale:** Cycle-017 cross-layer-cross-cutter cleared the ≥2-firm-instance bar (eigsolve firm cycle-011, divfree firm cycle-016). The nested-gate pattern recurs and deserves a named concept home. This unblocks dispatch 3 (divfree-theme "first"-claim correction) which needs to cite the new concept page.

---

**Dispatch 3: `lifter` — divfree-theme "first"-claim correction**
- **Agent:** lifter (opus)
- **Scope:** Scoped append-only fix to the firm `book/src/L1-L0/divfree-projector-mutation-rotation.md` (file is append-only after `integrated_at: 80db8d6`). Three inaccurate "first"/"no other current L1 op" claims at lines `:108-113`, `:457-464`, and residual ledger prose. Correct each to cite the cycle-011 firm `book/src/L1-L0/eigsolve-mutation-rotation.md` sub-pattern B (`:213-258`) as the prior, richer instance. Update the in-line nesting note (currently ~`:457-464`) from the divfree-specific closure-field mention to a cross-reference to the new `book/src/concepts/nested-constructed-operator-gate.md` concept page. Verify the fix is append-only (no content deletion; only edits and cross-ref updates allowed in the append-only region post-`integrated_at:`).
- **Deps:** dispatch 2 (layer-intro-author on nested-gate concept page must land first so the cross-reference can be accurate)
- **Rationale:** Divfree-theme is firm (cycle-016); the premise it asserts ("first instance of closure-nesting") is refuted by the cycle-011 eigsolve precedent (discovered by cycle-017 cross-layer-cross-cutter audit). The fix is scoped and surgical — cite the prior instance, not a content rework. Depends on concept page landing so the in-line note can reference it accurately.

---

**Dispatch 4: `abstractor` — `L2-L1/linear-combination-fold-specialization` lowering theme**
- **Agent:** abstractor (opus)
- **Scope:** Author the L2>L1 lowering theme `book/src/L2-L1/linear-combination-fold-specialization.md`. Narrate: (i) how the variadic L2 fold `linear_combination :: [(Scalar, Tensor[N])] -> Tensor[N]` lowers into fixed-arity L1 specializations: **arity 1** → `scal(α, x)`, **arity 2 with fixed coefficient 1.0** → `axpy(α, x, y)`, **arity 2 general** → `axpby(α, x, β, y)`, **arity 3** → `axpbypcz(α, x, β, y, γ, z)`, **longer lists** → left-fold composition of `axpby` / `axpbypcz` chains (the `tail-recursive-accumulation` L2 combinator, or unfolding of the list); (ii) which L0 pinned summation order each call site fixes (single fused pass vs split-call chains) — this is the load-bearing numerical content (match the precedent style from cycle-013 chebyshev-iteration-fusion theme); (iii) Variant axes: output-aliasing (in-place = output parameter reuse), scalar-promotion (real→complex promotion for the arity-2 case matching `axpby`); (iv) Section note: the `inner_product` fold is a DIFFERENT combinator (conjugation-convention axis, reduce-to-scalar not reduce-to-tensor) — cite the OQ `inner-product-fold-sibling-candidate` for the sibling pattern, do NOT over-unify the two folds.
- **Deps:** dispatch 1 (harvester on `linear_combination` firm entry must land first)
- **Rationale:** Unblocked when harvester firms `linear_combination`. This lowering theme closes the BLAS-1 unification at the L2>L1 level, showing how the variadic fold decomposes into the fixed-arity specializations. Completes the work opened by cycle-017 combinator-miner + harvester.

---

**Dispatch 5: `combinator-miner` — `inner-product-fold-sibling-candidate`**
- **Agent:** combinator-miner (opus)
- **Scope:** Separate dispatch confirming that `inner_product :: (Tensor[N], Tensor[N]) -> Scalar` (or `dot` / `tdot` with conjugation variants) is a **different fold pattern** from `linear_combination` and should NOT be unified into one mega-combinator. Document: (i) `inner_product` is a **reduce-to-scalar** fold (`foldl (+) 0 (zipWith (*) x y)` for reals; weighted complex conjugate for Hermitian); (ii) `linear_combination` is a **reduce-to-tensor** fold (linear combination of vectors); (iii) the two differ fundamentally on output type and thus on algebraic properties (permutation-invariance applies to linear-combination by linearity; for inner-product, permutation-invariance is a TRIVIAL consequence of commutativity); (iv) **conjugation-convention axis** is orthogonal to the arity-axis that unifies the BLAS-1 family — it is the axis that distinguishes `dot` vs `tdot` variants. Propose a future L2 `inner_product` combinator as a sibling, with the conjugation axis as a variant axis (NOT arity). Rationale: prevents over-unification of fundamentally different fold patterns. Citation: OQ `inner-product-fold-sibling-candidate`.
- **Deps:** none (independent; informational observation)
- **Rationale:** Cycle-017 integrator-signals explicitly flagged the do-NOT-over-unify risk in the `inner-product-fold-sibling-candidate` OQ text (opened by combinator-miner this cycle). A separate dispatch documents the distinction and prevents future cycles from merging the two patterns. This is a carryover from cycle-017 unblocked items.

---

**Dispatch 6: (optional, wave 2) `lifter` — small follow-up citation review**
- **Agent:** lifter (opus)
- **Scope:** Conditional dispatch (cycle-planner defers to integrator judgment on whether to include). If dispatch 1 (harvester on `linear_combination`) lands with any new dependency edges or concept citations that need refreshing in existing L2 entries (`krylov-step`, `chebyshev-iteration`), a small lifter pass can roll the new-edges-found notifications into those entries. Likely low-friction; can be deferred to cycle-019 if cycle-018 has capacity constraints. Cite the STAGING log generated during cycle-018 integration.
- **Deps:** dispatch 1 (L2 new entry must land first)
- **Rationale:** Optional carry-forward; if harvester on `linear_combination` surfaces new dependency edges that L2/L3 entries should acknowledge, a same-cycle lifter pass keeps the cross-layer linkage fresh. Otherwise defer.

---

## Overlap analysis

**Dispatches 1 & 4 (harvester + abstractor on linear-combination):**
- Harvester authors `book/src/L2/linear_combination.md` (firm operator chapter).
- Abstractor authors `book/src/L2-L1/linear-combination-fold-specialization.md` (new lowering-theme chapter).
- **Output files are DISTINCT** (`L2/` vs `L2-L1/`); **input dependencies are sequential** (abstractor reads harvester's L2 entry to narrate the lowering).
- **Sequencing: wave 2 dependent on wave 1** → dispatch 1 (wave 1) must land before dispatch 4 (wave 2).

**Dispatch 2 & 3 (concept page + divfree-theme fix):**
- Dispatch 2 authors `book/src/concepts/nested-constructed-operator-gate.md` (new concept).
- Dispatch 3 edits `book/src/L1-L0/divfree-projector-mutation-rotation.md` (append-only fix to the firm theme, cross-references the concept).
- **Output files are DISTINCT**; **input dependency**: dispatch 3 reads dispatch 2's concept page to cross-reference it accurately.
- **Sequencing: wave 2 dependent on wave 1** → dispatch 2 (wave 1) must land before dispatch 3 (wave 2).

**Dispatch 5 (combinator-miner on inner-product sibling):**
- Combinator-miner authors `book/src/L2/index.md` a new **rough-in dep-map row** for `inner_product` (or annotates the existing `inner_product` concept to clarify it is a separate pattern).
- Overlap with dispatch 1: **both touch `book/src/L2/index.md` (L2 index's dep-map)** — one appends `linear_combination` (firm), the other appends `inner_product` (rough-in, or navigates the distinction note).
- **Sequencing: dispatch 5 CAN run in parallel with dispatch 1** if each appends to distinct rows of the dep-map. The per-report integrator re-reads the index from disk between writes; serial dispatch order (1→5) ensures the appends stack cleanly even if overlapping on the same file.
- **Conservative call: mark as PARALLEL** per the conflict-tolerance philosophy (user directive 2026-05-27) — same-file row-level appends at distinct anchors are handled cleanly by the serial integrator.

**Dispatch 6 (optional lifter follow-up):**
- Depends on dispatch 1 (harvest must complete); can run in parallel with dispatches 2, 3, 4, 5 if the integration of dispatch 1 is already complete (wave 2+ dependency).
- Likely low-friction; if included, schedule as wave 2.

**Summary:**
- **No overlapping SEMANTIC content** between pairs of dispatches.
- **Wave 1 (parallel):** dispatches 1, 2, 5 — three independent reports (harvester on linear-combination, layer-intro-author on concept, combinator-miner on sibling-pattern).
- **Wave 2 (parallel, depends on wave 1):** dispatches 3, 4 — lifter (divfree-theme fix, depends on concept page from dispatch 2), abstractor (lowering theme, depends on harvester's L2 entry from dispatch 1).
- **Optional wave 2+:** dispatch 6 (lifter follow-up, deferrable).

## Sequencing schedule

### Wave 1 (parallel)
- **Dispatch 1:** `harvester` — `linear-combination-harvester-formalization` (authors `book/src/L2/linear_combination.md`)
- **Dispatch 2:** `layer-intro-author` — `nested-constructed-operator-gate` concept page (authors `book/src/concepts/nested-constructed-operator-gate.md`)
- **Dispatch 5:** `combinator-miner` — `inner-product-fold-sibling-candidate` (appends to `book/src/L2/index.md` dep-map; distinct row-anchor from dispatch 1)

**Wave 1 reports apply in serial integration order** (per-report integrator re-reads disk before each edit, so same-file appends stack cleanly).

### Wave 2 (parallel, after wave 1 reports land)
- **Dispatch 3:** `lifter` — divfree-theme "first"-claim correction (depends on dispatch 2's concept page being live for cross-reference)
- **Dispatch 4:** `abstractor` — `L2-L1/linear-combination-fold-specialization` lowering theme (depends on dispatch 1's firm L2 entry being live)

**Wave 2 reports apply serially after wave 1** (per the integrator-per-report serial-dispatch model).

### Optional Wave 2+ (if capacity remains)
- **Dispatch 6:** `lifter` — citation-review follow-up (depends on dispatch 1 integration being complete). **Deferrable to cycle-019 if cycle-018 becomes capacity-constrained.**

## Open questions / caveats

1. **Dispatch 2 confirm-before-cite caveat (a):** eigsolve is **fully firm** despite carrying a partly-constructive sub-part (`LinearSolveFailed`). The layer-intro-author should cite `book/src/L1/eigsolve.md` with a note that the operator as a whole is firm; the status value being partly-constructive is a **sub-part constructive flag**, not an operator-level flag. (This is a lesson from cycle-013/015 eigsolve promotion; re-confirm in the new concept page that eigsolve-the-operator is firm.)

2. **Dispatch 2 confirm-before-cite caveat (b):** the latent `K.M⁻¹`-as-`Solver[K.M]` site in `book/src/L1-L0/ksp-solve-mutation-rotation.md` (or in the firm L1 `ksp_solve` entry) — the layer-intro-author should note in the concept page that a third gate instance (ksp-solve as a sub-field of the Matrix itself, if Palace implements it that way) remains **latent pending L0 confirmation**. The codemap verifier should grep `palace/linalg/ksp.cpp` for the Solver-type field assignment to close this caveat. **Do not list a third instance without positive L0 anchor.**

3. **Dispatch 4 (abstractor) note on the `tail-recursive-accumulation` combinator:** The longer-list case (arity ≥4) lowers via a left-fold of `axpby` / `axpbypcz` chains. If `tail-recursive-accumulation` already exists as a combinator or concept, cite it; if not, the abstractor may propose it as a follow-up combinator-miner dispatch. **Do not author it here; note it as an open pattern.**

4. **Cycle-018 build-gate alert:** Dispatch 2 authors a new concept page (`nested-constructed-operator-gate.md`), and dispatch 3 must cross-reference it by a live markdown link `[nested-constructed-operator-gate](../concepts/nested-constructed-operator-gate.md)`. The per-report integrator's `cross-reference-integrity` gate (cycle-015 role-spec checklist) will verify the link target exists. **If dispatch 2 lands before dispatch 3 is integrated, the link will resolve cleanly. If the order is reversed, the build will fail** — but the serial per-report dispatch ordering (dispatch 2 wave 1 → dispatch 3 wave 2) ensures the concept page is on-disk before the cross-reference is applied.

5. **Cycle-018 is the THIRD/FINAL primary cycle of meta-batch-4** (cycles 016/017/018; meta-phase fires after this cycle's finalize). Compactify-after-meta-phase applies after the batch-4 meta-phase commit lands (per CLAUDE.md §Methodology invariants). No compactification occurs mid-cycle or after cycle-018 integration — only after the batch-4 meta-phase enactment (separate commit).

6. **Batch-4 meta-phase signal carry-forward:** The cycle-017 integrator-signals appended a prominent **⚠ META-SIGNAL** (recurrence-3 `specialized-agent-direct-write-to-book-during-dispatch`) flagging that three distinct specialized agents have now leaked `book/` during dispatch (cycle-008 abstractor, cycle-012 layer-intro-author, cycle-017 harvester). The batch-4 meta-phase (after this cycle) should enact dispatch-phase write-guards across ALL 8 specialized agent specs and re-weigh a structural pre-dispatch clean-tree gate. This is already noted in integrator-signals; no action required in cycle-018 dispatch, but planner is aware.

7. **Cycle-017 build-repair precedent (rough-in forward-reference):** Cycle-017 had one build-repair: the combinator-miner used a **live markdown link** to the not-yet-authored `linear_combination.md` chapter (broken link, `linkcheck2` failed). The correct convention is a **plain-text forward-reference** (no markdown link). If cycle-018 dispatches author any new rough-in dep-map rows, use plain-text references, not live links. Harvester (dispatch 1) should be aware that if it introduces new rough-in references in the L2 index, they should be plain-text.

## Carry-forward items deferred to cycle-019+

The following high-value items remain in the priority queue and are deferred due to cycle-018 bandwidth allocation:

- **(`lifter`/`abstractor` large dispatch) `gmres.md §L4 v0.6→v0.7 self-rotation`** — firms both cycle-008 GMRES + cycle-011 FGMRES sister themes. Headline carry-forward; large multi-cycle scope. Reschedule cycle-019+.
- **(`harvester` large multi-cycle) NLEPS at L1+** — cycle-009 OQ; large. Carry-forward cycle-019+.
- **(`layer-intro-author`) bundle-6 #6 `fespace.{hpp,cpp}`** — input-side FE-space anchor. Deferred until more FE-frontier work pulls on it.
