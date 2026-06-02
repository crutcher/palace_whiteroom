---
agent: abstractor
invoked_at: 2026-06-02T091509Z
scope: L2 upward-propagation WARRANT for fe_assemble (record-only; anti-mirror; NO chapter forced)
status: pending
integrated_at: 2026-06-02T101500Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-063 D1 (batch-19 close-out). Applied record-only -- NO book change (fe_assemble NO-ENTRY-BY-WARRANT: declines an L2 floor, degenerate anti-mirror on both axes -- no-carry concatenation-homomorphism fold + opaque-libCEED per-term leaf). OQ l2-fe-assemble-NO-ENTRY-by-warrant appended to scaffolding/open-questions.md New-intake, routed to the batch-19 meta-phase for formal close + STOP-PROPOSING-negative-list addition (paralleling c060 D2 L2/fold_solve no-floor-warrant). No safety-net gate triggered (no proposed-changes block). citecheck --scan 17 ok / 0 failing."
inputs:
  - book/src/L1/fe_assemble.md (firm L1 — the bilinear-form assembly fold over weak_form_terms)
  - book/src/L2/index.md (L2 fusion vocabulary census — what exists to shift INTO)
  - palace/fem/bilinearform.cpp:61-107 (the AddSubOperator fold site — verified via palace-codemap read_range)
  - PRECEDENT(NO-ENTRY): solve_family c057 D1 (embarrassingly-parallel family loop → no genuine iteration content → dissolution-theme is the home)
  - PRECEDENT(L3-ENTRY): fold_solve c059 D1 (time-sweep carry IS a sequential-obstruction → genuine partial-obstruction form)
  - PRECEDENT(NO-FLOOR-WARRANT): fold_solve / weak_form_term at L2 (opaque leaf, no L2 composition; reports/2026-06-02T071603Z-cross-layer-cross-cutter-l2-fold-solve-no-floor-warrant/)
---

# CYCLE: L2 upward-propagation WARRANT for `fe_assemble` — NO-ENTRY (degenerate mirror)

## Summary

WARRANT-FIRST verdict, record-only, no chapter authored. **Verdict: NO-ENTRY.** `fe_assemble` does NOT warrant an L2 (fusion-layer) entry; an `L2/fe_assemble.md` would be a degenerate mirror of the firm L1 fold (§1d identity-in-named-terms smell). The L1 form `K = Σ_i A(space, term_i)` is **already a fold-by-role over an opaque leaf**, stated entirely in existing shared vocabulary (fold / sum-of-operators / list-homomorphism), and the L2 (fusion) rotation has **nothing to shift** for two mutually-reinforcing reasons:

1. **No sequential carry → no fusion/iteration content to expose, and no L3 obstruction to anticipate.** The L0 accumulation `op->AddSubOperator(sub_op)` (`palace/fem/bilinearform.cpp:77` domain branch / `:97` boundary branch) builds each per-term sub-operator independently and adds it to the composite; the fold is order-commutative (L1 entry law 4, term-position commutativity — `book/src/L1/fe_assemble.md:134-140`). This is the **`solve_family` axis** (embarrassingly-parallel reduction → no genuine iteration-rotation content). It is the **inverse of `fold_solve`**, whose time-sweep carry IS a sequential-obstruction; `fe_assemble` has no carry, so there is no `partial-obstruction` even at L3, let alone L2-fusion content.
2. **The per-term leaf `A(space, ·)` is opaque-library-owned (libCEED) → no L2 composition to unfold.** The fusion physically happens INSIDE libCEED (`CeedOperatorFullAssemble`, `palace/fem/libceed/operator.cpp:455-490`), below the Palace surface. This is the **`fold_solve`/`weak_form_term` axis** (opaque per-step leaf, no L2 base-primitive decomposition — exactly the `fold_solve` no-floor-warrant — informal label "c060 D2", actual provenance `reports/2026-06-02T071603Z-cross-layer-cross-cutter-l2-fold-solve-no-floor-warrant/`).

An L2 `fe_assemble` would restate `Σ_i A(space, term_i)` in identical fold vocabulary with the same opaque leaf — **no vocabulary shift**. Per the 2026-06-01 vocabulary-shift redirect, that is the degenerate-mirror smell, not a layer.

**GENUINE-FORM exit checked and declined:** the only candidate L2 combinator would be a generic "assembly fold," but the abstract term-axis fold is ALREADY shared L2 vocabulary (`linear_combination` is its `Tensor[N]`-codomain sibling; `fe_assemble` is the `LinearOperator[N,N]`-codomain analog of the same `foldl (+) zero (map leaf terms)` skeleton). What is `fe_assemble`-specific — `A`, `WeakFormTerm` — is precisely the opaque FE leaf that does NOT lift. No new cleanly-describable, ≥2-pipeline-serving L2 combinator emerges that is not just a renamed L1 fold. NO licensed batch-20 candidate.

**Disposition:** route the formal close to the **batch-19 meta-phase** (RESOLVED-BY-WARRANT, upward-descent complete) and add `L2/fe_assemble` to the STOP-PROPOSING negative list so future planners don't re-litigate.

## Verdict

**NO-ENTRY (record-only).** No `book/src/L2/fe_assemble.md`. No new SUMMARY.md chapter. No L2 dep-map row. No speculative L2 operators proposed. This CYCLE.md IS the work product (a thin warrant note + route-to-meta), per the dispatch instruction.

## Warrant reasoning (the two anti-mirror axes, with the precedent contrast)

The dispatch named the likely-NO axis precisely; the evidence confirms it on BOTH sub-axes. The contrast table:

| Operator | Loop/fold carry | Per-step/per-term leaf | Verdict at the asked layer | Why |
|---|---|---|---|---|
| `solve_family` (c057 D1) | embarrassingly-parallel family loop, NO carry | (n/a — family of solves) | **NO L3-ENTRY** | no genuine iteration-rotation content; dissolution theme is the home |
| `fold_solve` (c059 D1) | time-sweep carry IS sequential | opaque MFEM `ode->Step` leaf | **L3-ENTRY** (`partial-obstruction`) | the carry is a genuine sequential-obstruction the iteration rotation must record |
| `fold_solve` at L2 (c060 D2) | (outer-sweep erasure is the L3>L2 content) | opaque `ode->Step` leaf, NO L2 composition | **NO L2-FLOOR** (warrant) | per-step body does not decompose into L2 primitives → degenerate mirror |
| **`fe_assemble` at L2 (this verdict)** | **concatenation-homomorphism fold, NO carry** (commutative `AddSubOperator` accumulation) | **opaque libCEED `A(space,·)` leaf, NO L2 composition** | **NO L2-ENTRY** (warrant) | **BOTH** anti-mirror axes hold: no fusion content from the fold (no carry) AND no fusion content from the leaf (opaque-library-owned) → pure degenerate mirror |

`fe_assemble` is the **strongest NO-ENTRY of the four** — it fails the warrant on *both* the `solve_family` axis (no-carry fold) and the `fold_solve`/`weak_form_term` axis (opaque leaf). `fold_solve` earned its L3 entry on the carry; `fe_assemble` has no carry to earn one, and no leaf-composition to fuse.

### Axis 1 — the fold is a no-carry concatenation homomorphism (the `solve_family` axis)

`fe_assemble = foldr (\t acc -> A(space, t) + acc) zero terms = Σ_{t ∈ terms} A(space, t)` (`book/src/L1/fe_assemble.md:61-62`). The L0 realization accumulates one sub-operator per term into a composite via `op->AddSubOperator(sub_op)` and finalizes — verified exact via `palace-codemap read_range` (`palace/fem/bilinearform.cpp:71-77` domain loop: `integ->Assemble(...)` builds `sub_op`, then `op->AddSubOperator(sub_op)` at `:77`; `:87-97` boundary loop identical, `AddSubOperator` at `:97`; `op->Finalize()` at `:104`). The accumulation has **no sequential carry**: each `sub_op` is independent of every other, and the composite's action is the order-independent sum (L1 law 2 concatenation-homomorphism `:123-128`, law 4 term-position commutativity `:134-140`). Because addition is commutative and associative, the fold lifts cleanly to a global tensor-field sum — there is **no iteration-rotation obstruction at L3** (contra `fold_solve`'s `partial-obstruction`), hence a fortiori no fusion content for an L2 layer to expose. The L2 "fusion rotation" erases HPC tricks back into base-algebra composition; here the only "trick" is the OMP-per-thread composite build (`palace/fem/bilinearform.cpp:50-105`, one `Ceed` per thread) — which is exactly the kind of transparent parallelization that collapses without producing new L2 vocabulary (it is already absorbed as an L1>L0 lowering concern, `book/src/L1/fe_assemble.md:236-237`).

### Axis 2 — the per-term leaf `A` is opaque-library-owned (the `fold_solve`/`weak_form_term` axis)

`A(space, ·)` is the element-local→global assembly map (libCEED restriction + basis-apply + quadrature contraction); the kernel body is upstream-owned (`book/src/L1/fe_assemble.md:170-176`). Palace consumes it opaquely at the call boundary `integ->Assemble(...)` building one `CeedOperator` sub-operator (`palace/fem/bilinearform.cpp:67-70` / `:87-90`); the actual fusion (element batching, quadrature-point contraction, COO→CSR materialization) lives in libCEED (`CeedOperatorFullAssemble`, `palace/fem/libceed/operator.cpp:455-490`). This is the `obstruction (opaque-library-ownership)` boundary named in the dispatch. There is **no L2 base-primitive composition to unfold** — exactly the c060 D2 finding for `fold_solve`'s `ode->Step` leaf: the per-term body does not decompose into L2 primitives, so an L2 floor would carry the same opaque leaf as the L1 form, byte-for-byte. The PA/FA dual (`assembly-representation` variant axis) already collapses at L1 (`book/src/L1/fe_assemble.md:104-108`, `:180-185`; `book/src/L0/fem-bilinearform-file.md` §"The PA/FA dual collapses at L1") — that collapse is an L1>L0 absorption, NOT an L2 fusion, so it does not seed an L2 form either.

### Why the two axes together make it the cleanest NO-ENTRY

An L2 entry is warranted when the fusion rotation has genuine content to shift — either (a) the fold/loop has structure to re-express in shared L2 composition vocabulary (a named composition, a combinator), or (b) the per-step/per-term body opens into a composition of L2 base primitives. `fe_assemble` has neither: (a) the fold is the trivial no-carry sum (already shared vocabulary, nothing to name beyond the existing `linear_combination`-family fold skeleton), and (b) the leaf is opaque-library-owned (nothing to open). Both engines of L2 content are absent. The result would be `Σ_i A(space, term_i)` restated in the same fold vocabulary with the same opaque leaf = the §1d identity-in-named-terms degenerate mirror.

## GENUINE-FORM exit — checked and DECLINED (no licensed batch-20 candidate)

The dispatch licensed recording a batch-20 candidate IF a genuine fusion-layer shift surfaces — a cleanly-describable L2 assembly combinator serving ≥2 pipelines that is NOT just a renamed L1 fold. I checked and decline, for a precise reason:

- **The abstract term-axis fold is ALREADY L2 shared vocabulary.** `linear_combination` (firm cycle-018, `book/src/L2/linear_combination.md`) is the `foldl (\acc (a,t) -> acc + a·t) zeros pairs` term-axis fold producing `Tensor[N]`. `fe_assemble` is the **operator-codomain analog** of the very same `foldl (+) zero (map leaf terms)` skeleton — same fold, codomain `LinearOperator[N,N]` instead of `Tensor[N]`, kernel `A(space,·)` instead of scalar-multiply. A hypothetical "assembly-fold combinator" would therefore either (i) BE `linear_combination` generalized over codomain (which is a *higher-layer* unification question about the fold skeleton itself, not an `fe_assemble`-specific L2 form — and merging operator-sum into the scalar/tensor fold cohort would erase the codomain distinction the existing do-NOT-merge boundary protects, `book/src/L2/index.md:22-26`), or (ii) be a renamed `fe_assemble` fold = the degenerate mirror.
- **What is `fe_assemble`-specific is exactly what does NOT lift.** The genuinely-new content of `fe_assemble` is the FE vocabulary `WeakFormTerm` (firm cycle-061) + the opaque libCEED `A`. Neither admits an L2 fusion: `WeakFormTerm` is folded opaquely (the fold never cracks it open, `book/src/L1/fe_assemble.md:69-74`, `:206-214`), and `A` is library-owned. So the only `fe_assemble`-specific material is leaf material that is NOT L2 composition.
- **No ≥2-pipeline combinator emerges.** The two in-scope solver-K witnesses (electrostatic ∇/diffusion `palace/models/laplaceoperator.cpp:191-192`; magnetostatic ∇×/curl-curl `palace/models/curlcurloperator.cpp:179-181`) both reduce to the SAME no-carry fold over the SAME opaque `A` — they differ only in the `differential-operator` variant axis of `WeakFormTerm` (an L1 variant-axis concern, `book/src/L1/fe_assemble.md:161-169`), not in any L2 fusion structure. There is no cross-pipeline fusion pattern to combinator-ize.

Conclusion: no GENUINE-FORM. The L2 form is a degenerate mirror on both axes. **No batch-20 candidate recorded.**

## Route / disposition

1. **Route the formal close to the batch-19 meta-phase** (fires after this cycle's finalize — this is the last primary cycle before meta). Recommended meta action: mark the `fe_assemble` L2 upward-propagation question **RESOLVED-BY-WARRANT (NO-ENTRY)**, upward-descent complete — paralleling the c060→batch-18 close of the `fold_solve` L2 no-floor-warrant.
2. **Add `L2/fe_assemble` to the STOP-PROPOSING negative list** (meta-phase enactment, `scaffolding/priorities.md` / the negative list the planner consults) so future planners do not re-propose an `L2/fe_assemble` floor. Rationale string for the list: *"NO-ENTRY by warrant (c063 D1) — degenerate mirror on BOTH anti-mirror axes: no-carry concatenation-homomorphism fold (solve_family axis) AND opaque libCEED per-term leaf (fold_solve/weak_form_term axis); the abstract term-axis fold is already shared L2 vocabulary via linear_combination."*
3. **No authoring follow-up.** Explicitly do NOT dispatch a harvester/abstractor to author `book/src/L2/fe_assemble.md` — that manufactures the exact degenerate mirror the warrant rejects (§1d smell). No lifter re-anchor needed (no stale claim). No lowering-verifier deepening needed.
4. **No book mutation this cycle.** Record-only. No SUMMARY.md / dep-map / index touches (NO-ENTRY = no chapter to register).

## Supporting evidence (all citations self-verified against source)

- `palace/fem/bilinearform.cpp:61-107` — `BilinearForm::PartialAssemble` fold core; **verified exact via palace-codemap read_range**: `integ->Assemble(...)` builds `sub_op` (`:73-74` domain / `:93-94` boundary), `op->AddSubOperator(sub_op)` accumulates with the inline comment `// Sub-operator owned by ceed::Operator` (**`:77`** domain / **`:97`** boundary), `op->Finalize()` (**`:104`**). The accumulation is the no-carry, order-commutative composite build (Axis 1 keystone).
- `palace/fem/bilinearform.cpp:67-70` / `:87-90` — the `integ->Assemble(...)` opaque per-term call boundary into libCEED (Axis 2 keystone — the leaf Palace consumes opaquely).
- `palace/fem/libceed/operator.cpp:455-490` — `CeedOperatorFullAssemble`: the libCEED-owned COO→CSR materialization where the fusion physically lives (Axis 2; cited by `book/src/L1/fe_assemble.md:264-266`).
- `palace/models/laplaceoperator.cpp:191-192` — electrostatic ∇/diffusion witness `fe_assemble(h1_space, [diffusion(ε)])` (one of the two in-scope solver-K witnesses for the GENUINE-FORM ≥2-pipeline check).
- `palace/models/curlcurloperator.cpp:179-181` — magnetostatic ∇×/curl-curl witness (the second solver-K witness; differs only in the `differential-operator` L1 variant axis, not in any L2 fusion structure).
- `book/src/L1/fe_assemble.md` — firm L1 entry: signature `:61-62` (the fold), law 2 concatenation-homomorphism `:123-128`, law 4 term-position commutativity `:134-140`, opaque-fold-over-`WeakFormTerm` `:69-74` / `:206-214`, opaque libCEED leaf `A` `:170-176`, PA/FA-collapses-at-L1 `:104-108` / `:180-185`, OMP-per-thread transparent parallelization `:236-237`.
- `book/src/L2/index.md` — L2 fusion vocabulary census: the `linear_combination` term-axis fold `:24`, `:38`, `:77` (the existing shared fold skeleton `fe_assemble` is the operator-codomain analog of); the fold-cohort do-NOT-merge boundary `:22-26`, `:112` (why merging operator-sum into the scalar/tensor cohort is disallowed); the named-composition / fold-cohort / standalone-floor motifs `:19-30` (none of which `fe_assemble` would add genuinely-new content to).
- PRECEDENT `reports/2026-06-02T071603Z-cross-layer-cross-cutter-l2-fold-solve-no-floor-warrant/CYCLE.md` — the c060 D2 `fold_solve` L2 no-floor-warrant this verdict parallels (opaque per-step leaf, no L2 composition → degenerate mirror → RESOLVED-BY-WARRANT to meta).

## Open questions / caveats

- **This is a warrant-render, NOT a re-derivation of whether `A` could in principle decompose into L2 primitives.** The libCEED-boundary classification of `A` is itself an open question carried by the firm L1 entry (`book/src/L1/fe_assemble.md` §Dependencies / §Open questions — transitive-firm leaf vs. opaque-library-ownership vs. tensor-contraction respine). If a FUTURE producer establishes that `A` admits a genuine L2 tensor-contraction respine (i.e. Palace re-architects to expose the element-local quadrature kernel as a Palace-owned L2 composition rather than consuming libCEED opaquely), THAT would reopen this warrant — the L2 form would then have genuine fusion content (the de-fused restriction ▷ basis-apply ▷ quadrature-contract pipeline). No evidence of that surfaced; the current consumption is opaque (`integ->Assemble` → libCEED). This caveat parallels the c060 D2 caveat for `ode->Step`. It does NOT weaken the NO-ENTRY verdict for the *current* feature set — it names the single condition under which a future cycle could revisit.
- **The reverse (how an L2 form would lift FROM the L1 fold) is deliberately NOT recorded here** — per the high→low layer-definition discipline, lifting notes belong in working notes, and in the NO-ENTRY case there is no lift to support (there is no L2 target). This caveat is the only lifting-direction note and it is confined to §Open questions by design.
- **`weak_form_term` at L2:** the sibling dispatch / prior work established `weak_form_term` likewise owes no L2 floor (opaque leaf, no L2 composition content — the same Axis-2 reasoning). This verdict is consistent with that: `fe_assemble`'s NO-ENTRY does not strand `weak_form_term` (the fold quantifies over it opaquely at every layer; it is FE vocabulary that lives at L1 as the element type, not an L2 composition). Flagged for the batch-19 meta-phase to confirm the two NO-ENTRY warrants are recorded coherently together (the `fe_assemble` fold + its `weak_form_term` element both decline L2 floors for the same opaque-leaf reason).
