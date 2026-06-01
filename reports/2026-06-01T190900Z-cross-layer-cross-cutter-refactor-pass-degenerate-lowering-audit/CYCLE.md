---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-01T190900Z
scope: L3↔L2 + L2↔L1 cross-cut — cohort-wide degenerate-lowering classification (the cycle-050 demotion worklist)
status: integrated
integrated_at: 2026-06-01T210000Z
integration_commit: 92327f7
integration_notes: APPLIED clean (cycle-049 D3) — observation-only, NO book/ mutation (D3 proposed none; deliverable is the cycle-050 demotion worklist + the load-bearing scope finding, promoted as 3 OQs). HEADLINE FINDING the degenerate-lowering cohort is 18 themes (9 pairs) NOT 12 — the controlling cycle-050 scope input (demoting only 12 + stranding 6 re-creates the mirrored floor the redirect corrects); 2 themes divfree-projector/jacobi-smoother marked verify-body-before-demoting. D1/D2/D3 reconciliation CLOSED-as-agreement on nrm2-consumer-not-member (no divergence to escalate). Build-relevant no. FIRST cohort-wide degenerate-lowering audit under the 2026-06-01 VOCABULARY-SHIFT REDIRECT.
---

# CYCLE: Cross-layer observation — degenerate-identity-in-named-terms thin-theme cohort

## Summary

Auditing the full thin-theme cohort against the VOCABULARY-SHIFT REDIRECT §1d smell test (a
degenerate identity-in-named-terms lowering — LHS and RHS say the same thing in the same named
terms, no vocabulary shift — is a smell to resolve as a thin in-line note or combinator
re-expression, NOT a mirrored entry + thin theme), I confirm **all 12 planner-scoped leaf themes
are degenerate-smell** and produce the demotion worklist below. I cross-confirm the **5 substantive
themes STAY** (genuine wrapper-rotation / iteration-view-erasure / arity-or-conjugation-dispatch
vocabulary shifts) and the **2 combinator-own fold-specialization lowerings STAY** (D1/D2 KEEP
verdicts). **One material scope-boundary finding:** the degenerate-smell cohort is **18 themes (9
adjacent-edge pairs), not 12** — the planner scoped only the 6 BLAS-1-arity-family pairs; the other
6 pairs (`assemble-diagonal`, `divfree-projector`, `elementwise-product`, `jacobi-smoother`,
`normalize`, `reciprocal`, each with a `-body-identity` L3>L2 + a `-leaf-identity` L2>L1) carry the
identical self-describing smell and belong on the same worklist. Surfacing the full 18 so cycle-050
enactment is complete, not a 12-of-18 partial sweep that leaves 6 strays.

## Observation kind

**Consistency drift** (cohort-boundary classification) — the degenerate identity-in-named-terms
lowering smell is uniformly present across a larger cohort (18 themes) than the per-family dispatch
plan named (12). The cross-cut is the boundary call: which thin themes are degenerate-smell (demote)
vs. which are genuine translations (keep). Secondary kind: **coverage completeness** of the cycle-050
demotion enactment.

## Specific finding

### (1) The 12 planner-scoped leaf themes — ALL degenerate-smell, CONFIRMED

Every one self-describes as identity-in-named-terms with no vocabulary shift. The load-bearing
self-describing lines:

| Theme file | Self-describing degenerate-smell line (file:line) |
|---|---|
| `L3-L2/axpy-body-identity.md` | `:91-93` "the rewrite is the **identity on the leaf primitive's body**, with **no wrapper adjustment**: `axpy α x y ⇒ axpy α x y`"; `:99` mapping cell "Identity. Same signature, same single fused field operation." |
| `L3-L2/axpby-body-identity.md` | `:90-92` "identity on the leaf primitive's body, no wrapper adjustment: `axpby α x β y ⇒ axpby α x β y`"; `:99-100` "Identity. Same whole-tensor quaternary signature." |
| `L3-L2/axpbypcz-body-identity.md` | `:89-91` "identity on the leaf primitive's body … `axpbypcz α x β y γ z ⇒ axpbypcz α x β y γ z`"; `:97` "Identity. Same six-arg signature, same single fused field operation." |
| `L3-L2/scal-body-identity.md` | `:86-89` "identity on the leaf primitive's body, with no wrapper adjustment: `scal α x ⇒ scal α x`"; `:95` "Identity. Same signature, same single field operation." |
| `L3-L2/dot-body-identity.md` | `:74-84` mapping table "Identity. Same whole-tensor signature; the Haskell-arrow vs tuple presentation is notational only." |
| `L3-L2/nrm2-body-identity.md` | `:90-95` "identity on the leaf … no wrapper rotation"; **caveat — see (1b)** (`:102-103,109-110` one textual difference: inner-reduction name `dot` leaf at L3 vs `inner_product` fold at L2 at the diagonal). |
| `L2-L1/axpy-leaf-identity.md` | `:96-108` "the rewrite is the **identity on the leaf** … the mapping is total and bijective on the leaf. This is the identity-in-form property." |
| `L2-L1/axpby-leaf-identity.md` | `:95-107` "identity on the leaf … total and bijective on the leaf." |
| `L2-L1/axpbypcz-leaf-identity.md` | `:91-103` "identity on the leaf … total and bijective on the leaf." |
| `L2-L1/scal-leaf-identity.md` | `:63-73` "`scal α x ⇒ scal(α, x)` — arity 1: the identity row … **No abstraction is imposed and none is removed** — the L2 floor form and the L1 leaf form are the same operator, written in the same signature, at adjacent layers." |
| `L2-L1/dot-leaf-identity.md` | `:86-98` "identity on the leaf … total and bijective on the leaf. This is the identity-in-form property." |
| `L2-L1/nrm2-leaf-identity.md` | `:75-119` "identity-in-form on the primitive's signature … the mapping is total and trivial"; **caveat — see (1b)** (the `√∘abs` post-step / preserved-vs-absorbed framing change). |

Each of these is exactly the redirect's smell: a mirrored entry (the same-named L2/L1 floor) + a
thin theme whose whole content is "this is the identity." The named terms do not shift across the
edge.

### (1b) Two borderline themes carry a near-zero residual (still DEMOTE, but the in-line note is non-empty)

`nrm2-body-identity` (L3>L2) and `nrm2-leaf-identity` (L2>L1) are NOT pure-identity: each carries
**one** real framing change — the inner self-inner-product is named via the `dot` *leaf* at L3 and
via the `inner_product` *fold* at L2 (`nrm2-body-identity.md:102-103,109-110`), and the `std::abs`
defensive guard is "preserved-as-explicit-claim at L2 → absorbed-by-non-negativity-claim at L1"
(`nrm2-leaf-identity.md:99-113`). This is the diagonal-degeneration `dot(x,x) = inner_product(x,x)`
naming swap plus a resolution-drop of two scalar post-steps. **Verdict: still DEMOTE** — these are
not a *vocabulary shift on `nrm2` itself* (the operator signature `Tensor[N] -> Scalar` is identical
and the value is identical at every hop); the genuine content (the `abs` load-bearing-numerical
classification) already has a firm home at `L1-L0/nrm2-mutation-rotation.md` §"The `std::abs`
defensive guard — classification", and the diagonal naming swap is a one-line note. The in-line note
these collapse to is slightly longer than the pure-identity siblings' (it must mention the
`dot`-leaf/`inner_product`-fold diagonal equivalence and the abs preserved/absorbed framing), but it
is still an in-line note, not a mirrored entry + theme. Flagged so the cycle-050 abstractor/lifter
does not mistakenly KEEP these on the basis of "they carry one textual difference."

### (1c) SCOPE-BOUNDARY: the degenerate cohort is 18, not 12

The planner's scope named the 6 BLAS-1-arity-family pairs only. `ls book/src/L3-L2/` +
`ls book/src/L2-L1/` shows **6 more degenerate pairs** with the identical self-describing smell
(heads read this invocation; each opens with "The rewrite is **identity-in-form on the body**"):

- `L3-L2/assemble-diagonal-body-identity.md:3-7` + `L2-L1/assemble-diagonal-leaf-identity.md`
  (operator-to-data extraction leaf; "value-thread-isomorphic on the primitive")
- `L3-L2/divfree-projector-body-identity.md:3-8` + `L2-L1/divfree-projector-leaf-identity.md`
  (constructed-operator gate; "the four-step composition is explicit at both layers")
- `L3-L2/elementwise-product-body-identity.md:3-9` + `L2-L1/elementwise-product-leaf-identity.md`
  (Hadamard binary leaf; "no wrapper rotation")
- `L3-L2/jacobi-smoother-body-identity.md:3-8` + `L2-L1/jacobi-smoother-leaf-identity.md`
  (constructed-operator gate; "one elementwise product `op.dinv ⊙ x`")
- `L3-L2/normalize-body-identity.md:3-8` + `L2-L1/normalize-leaf-identity.md`
  (fused composite `nrm2 ∘ scal`; "identity on the composite itself")
- `L3-L2/reciprocal-body-identity.md:3-8` + `L2-L1/reciprocal-leaf-identity.md`
  (elementwise multiplicative-inverse leaf; "no wrapper rotation")

These are different *sub-shapes* (2 standalone leaves, 2 constructed-operator gates, 1 fused
composite, 1 operator-to-data leaf) but all are degenerate-identity-in-named-terms lowerings — the
same smell, the same resolution. Leaving them out of the cycle-050 worklist would demote 12 and
strand 6 identically-degenerate strays, re-creating the very middle-heavy mirrored-floor pattern the
redirect is correcting. **Recommendation: cycle-050 enactment treats all 18.** (The 6 extra were
landed cycles 037–039/042–045 under the now-superseded `l2-floor-under-l3-leaf-cohort`
foundation-first directive; they are exactly the "thin `-body-identity`/`-leaf-identity` themes …
refactored" the redirect names.)

### (2) The 5 substantive themes — GENUINE translations, CONFIRMED KEEP (do NOT demote)

| Theme file | Why it is a genuine translation (NOT degenerate) | Status |
|---|---|---|
| `L4-L3/krylov-step-typed-wrapper-dissolution.md` | Real wrapper rotation: typed records → positional tuples, `StateT SimState Identity` → explicit `s`-arg/`s'`-return, `OpParams readonly` → documented invariant, Form-A/B → carry-threading (`:1` summary). The two speculative L4 ops (`iterate_while`/`iterate_while_with_prev`) firm here. | firm (`:293`) |
| `L3-L2/krylov-step-body-identity.md` | NOT pure-identity: the **body** is identity-in-form but the **wrapper** carries TWO real rotations — L3 `(op,K,s)` positional tuple → L2 unified `IterState` record (state-hiding), and L3 tail-recursive `iterate_while_L3` → L2 outer-driver-by-role (abstraction-by-role) (`:1`, §Rewrite-shape items 1-2). The wrapper rotation IS the vocabulary shift. | firm |
| `L3-L2/ksp-solve-outer-driver.md` | Substantive: iteration-view erasure + named obstruction shadows down to L2 non-laws; "the L3>L2 rotation here is **substantive** — the iteration view is erased" (Status `:171`). Driver-complement of krylov-step-body-identity. | firm (`:171`) |
| `L3-L2/chebyshev-nested-recurrence.md` | Substantive Part B: nested-loop iteration-view erasure + two obstructions' shadow-to-non-laws (Status `:425`). | firm (`:425`) |
| `L3-L2/eigsolve-opaque-eigen-iteration.md` | Substantive: opaque-library obstruction-marker erasure + marker shadow-to-non-laws (Status `:410`). | firm (`:410`) |
| `L3-L2/orthogonalize-variant-split.md` | Substantive: MGS/CGS variant split + non-identity content (Status `:387`). | firm (`:387`) |

(Six rows — the krylov-step pair spans two edges. All carry a real vocabulary/organization shift, so
none is a smell; none goes on the demotion worklist.)

### (2b) The 2 combinator-own fold-specialization lowerings — GENUINE translations, KEEP (cross-confirm D1/D2)

| Theme file | Why it is a genuine translation | Cross-confirm |
|---|---|---|
| `L2-L1/linear-combination-fold-specialization.md` | Variadic `[(Scalar,Tensor[N])]` fold → bounded family of fixed-arity L1 leaves (`scal`/`axpy`/`axpby`/`axpbypcz`) by **arity-dispatch**, + `axpy`-vs-`axpby` unit-coefficient sub-selection, + `γ==0` arity-collapse, + **pinned-summation-order table** (load-bearing-numerical) (`:1-13,38-59`). The fold→dispatch IS the vocabulary shift; the named term (`linear_combination`) does not appear at L1. | D1's KEEP verdict (the `linear_combination` combinator entry these 4 leaves are absorbed under). |
| `L2-L1/inner-product-fold-specialization.md` | Reduce-to-scalar `inner_product` fold → `dot`/`tdot`/`bilinear-form` by **conjugation/element-type/weight dispatch**, + value-level `xᴴy ↔ yᴴx` conjugate-pair re-order, + **pinned reduction tree** (`:1-25,30-59`). The conjugation-dispatch + re-order IS the vocabulary shift. | D2's KEEP verdict (the `inner_product` combinator entry these leaves are absorbed under). |

## Recommendation

Dispatch the **cycle-050 abstractor/lifter enactment on the full 18-theme demotion worklist** below
(NOT 12). Each DEMOTE/ABSORB collapses the thin theme into an in-line note on the named L_n entry's
prose and removes the mirrored-entry + thin-theme pattern. The 5 substantive + 2 combinator-own
themes are explicitly OFF the worklist.

Recommended dispatch shape: one enactment dispatch per family (the abstractor/lifter that owns the
combinator re-expression), consuming this worklist as the pre-computed classification so no per-theme
re-derivation is needed. The `linear_combination` family (D1) and `inner_product` family (D2) each
own their arity/dot leaves; the 6 non-fold leaves (assemble-diagonal, divfree-projector,
elementwise-product, jacobi-smoother, normalize, reciprocal) have no combinator parent and DEMOTE to
their own L_n entry's prose.

## The demotion worklist (the cycle-050-consumable artifact)

Verdict legend: **DEMOTE-to-inline** = collapse the thin theme to an in-line "Downward to L_{n-1}"
note in the named L_n entry's prose; **ABSORB-into-combinator-note** = fold into the combinator
entry's specialization note (D1 `linear_combination` / D2 `inner_product`); **KEEP-substantive** =
off the worklist.

### A. The 12 planner-scoped leaf themes (BLAS-1 arity + inner-product family)

| Theme file | Verdict | One-line rationale | In-line home |
|---|---|---|---|
| `L3-L2/scal-body-identity.md` | DEMOTE-to-inline | arity-1 leaf, identity body, no wrapper | `book/src/L3/scal.md` §"Downward to L2" |
| `L3-L2/axpy-body-identity.md` | DEMOTE-to-inline | arity-2-coeff-1 leaf, identity body, no wrapper | `book/src/L3/axpy.md` §"Downward to L2" |
| `L3-L2/axpby-body-identity.md` | DEMOTE-to-inline | arity-2 leaf, identity body, no wrapper | `book/src/L3/axpby.md` §"Downward to L2" |
| `L3-L2/axpbypcz-body-identity.md` | DEMOTE-to-inline | arity-3 leaf, identity body, no wrapper | `book/src/L3/axpbypcz.md` §"Downward to L2" |
| `L3-L2/dot-body-identity.md` | DEMOTE-to-inline | reduce-to-scalar leaf, identity body, no wrapper | `book/src/L3/dot.md` §"Downward to L2" |
| `L3-L2/nrm2-body-identity.md` | DEMOTE-to-inline (note non-empty — see 1b) | identity on signature; one note: `dot`-leaf vs `inner_product`-fold diagonal naming | `book/src/L3/nrm2.md` §"Downward to L2" |
| `L2-L1/scal-leaf-identity.md` | ABSORB-into-combinator-note (D1) | arity-1 row of `linear_combination` fold; value+bit-exact, no residue | `book/src/L2/linear_combination.md` specialization note (arity-1 row) |
| `L2-L1/axpy-leaf-identity.md` | ABSORB-into-combinator-note (D1) | arity-2-coeff-1 row; fusion deferred to fold-parent | `book/src/L2/linear_combination.md` specialization note (arity-2-coeff-1 row) |
| `L2-L1/axpby-leaf-identity.md` | ABSORB-into-combinator-note (D1) | arity-2 row; fusion deferred to fold-parent | `book/src/L2/linear_combination.md` specialization note (arity-2 row) |
| `L2-L1/axpbypcz-leaf-identity.md` | ABSORB-into-combinator-note (D1) | arity-3 row; fusion deferred to fold-parent | `book/src/L2/linear_combination.md` specialization note (arity-3 row) |
| `L2-L1/dot-leaf-identity.md` | ABSORB-into-combinator-note (D2) | plain (M=I) Hermitian member of `inner_product` fold; fusion deferred | `book/src/L2/inner_product.md` specialization note (Hermitian/`dot` member) |
| `L2-L1/nrm2-leaf-identity.md` | DEMOTE-to-inline (note non-empty — see 1b) | consumer-NOT-member of `inner_product` (carved out, fork-invariant); `√∘abs` post-step framing change | `book/src/L2/nrm2.md` §"Downward to L1" (NOT the `inner_product` combinator note — nrm2 is a consumer) |

Note the **L3>L2 vs L2>L1 asymmetry on the fold-member leaves**: the L3>L2 `-body-identity` themes
DEMOTE-to-inline on the L3 entry (the L3 leaf has no fold-parent at L3 — `linear_combination`/
`inner_product` are L2 vocabulary), while the L2>L1 `-leaf-identity` themes for fold-MEMBERS
ABSORB-into-combinator-note (the L2 leaf IS a member of the L2 combinator fold, so its L2>L1 edge is
the combinator's arity/conjugation row). `nrm2` is the exception at BOTH edges: it is a *consumer*
of `inner_product`, not a member (RESOLVED carve-out, OQ ledger `:595`), so both its themes
DEMOTE-to-inline on the `nrm2` entries, not absorb into the combinator note.

### B. The 6 additional degenerate pairs (scope-boundary extension — see 1c)

| Theme file | Verdict | One-line rationale | In-line home |
|---|---|---|---|
| `L3-L2/assemble-diagonal-body-identity.md` | DEMOTE-to-inline | operator-to-data leaf, identity body | `book/src/L3/assemble-diagonal.md` §"Downward to L2" |
| `L2-L1/assemble-diagonal-leaf-identity.md` | DEMOTE-to-inline | no fold-parent (operator-to-data, not a fold member) | `book/src/L2/assemble-diagonal.md` §"Downward to L1" |
| `L3-L2/elementwise-product-body-identity.md` | DEMOTE-to-inline | Hadamard binary leaf, identity body | `book/src/L3/elementwise_product.md` §"Downward to L2" |
| `L2-L1/elementwise-product-leaf-identity.md` | DEMOTE-to-inline | standalone leaf, no fold-parent | `book/src/L2/elementwise_product.md` §"Downward to L1" |
| `L3-L2/reciprocal-body-identity.md` | DEMOTE-to-inline | elementwise inverse leaf, identity body | `book/src/L3/reciprocal.md` §"Downward to L2" |
| `L2-L1/reciprocal-leaf-identity.md` | DEMOTE-to-inline | standalone leaf, no fold-parent | `book/src/L2/reciprocal.md` §"Downward to L1" |
| `L3-L2/normalize-body-identity.md` | DEMOTE-to-inline | fused composite `nrm2 ∘ scal`, identity on composite | `book/src/L3/normalize.md` §"Downward to L2" |
| `L2-L1/normalize-leaf-identity.md` | DEMOTE-to-inline | fused composite of two same-layer floors, no fold-parent (third sub-shape, OQ `:651`) | `book/src/L2/normalize.md` §"Downward to L1" |
| `L3-L2/divfree-projector-body-identity.md` | DEMOTE-to-inline (verify — see OQ) | constructed-operator gate; four-step composition explicit at both layers | `book/src/L3/divfree-projector.md` §"Downward to L2" |
| `L2-L1/divfree-projector-leaf-identity.md` | DEMOTE-to-inline (verify — see OQ) | constructed-operator gate composition | `book/src/L2/divfree-projector.md` §"Downward to L1" |
| `L3-L2/jacobi-smoother-body-identity.md` | DEMOTE-to-inline (verify — see OQ) | constructed-operator gate; one elementwise product `op.dinv ⊙ x` | `book/src/L3/jacobi-smoother.md` §"Downward to L2" |
| `L2-L1/jacobi-smoother-leaf-identity.md` | DEMOTE-to-inline (verify — see OQ) | constructed-operator gate apply | `book/src/L2/jacobi-smoother.md` §"Downward to L1" |

### C. OFF the worklist (KEEP-substantive, listed for completeness)

`L4-L3/krylov-step-typed-wrapper-dissolution.md`, `L3-L2/krylov-step-body-identity.md`,
`L3-L2/ksp-solve-outer-driver.md`, `L3-L2/chebyshev-nested-recurrence.md`,
`L3-L2/eigsolve-opaque-eigen-iteration.md`, `L3-L2/orthogonalize-variant-split.md`,
`L2-L1/linear-combination-fold-specialization.md`, `L2-L1/inner-product-fold-specialization.md`.

Plus the non-thin L2>L1 composition lowerings NOT in this cohort and NOT audited here (they are not
degenerate identity-in-named-terms — flagged only so cycle-050 does not over-reach):
`L2-L1/krylov-step-kernel-defusion.md`, `L2-L1/ksp-solve-outer-driver-unfold.md`,
`L2-L1/orthogonalize-composition-lowering.md`, `L2-L1/deflate-composition-lowering.md`,
`L2-L1/eigsolve-spectral-transform-composition.md`,
`L2-L1/incremental-least-squares-composition-lowering.md`,
`L2-L1/gram-fold-specialization.md`, `L2-L1/chebyshev-iteration-fusion.md`.

## Supporting evidence

- Cohort listing: `ls book/src/L3-L2/` + `ls book/src/L2-L1/` + `ls book/src/L4-L3/` (this
  invocation).
- 12 leaf themes read in full: `L3-L2/{axpy,axpby,axpbypcz,scal,dot,nrm2}-body-identity.md`,
  `L2-L1/{axpy,axpby,axpbypcz,scal,dot,nrm2}-leaf-identity.md` — self-describing degenerate-smell
  lines tabulated in §(1).
- 6 additional pairs: heads of `L3-L2/{assemble-diagonal,divfree-projector,elementwise-product,
  jacobi-smoother,normalize,reciprocal}-body-identity.md` (`:3-9`) — all open "identity-in-form on
  the body."
- Substantive themes' Status lines: `L3-L2/ksp-solve-outer-driver.md:171` ("substantive — the
  iteration view is erased"), `chebyshev-nested-recurrence.md:425`,
  `eigsolve-opaque-eigen-iteration.md:410`, `orthogonalize-variant-split.md:387`,
  `L4-L3/krylov-step-typed-wrapper-dissolution.md:293`; `krylov-step-body-identity.md:1` +
  §Rewrite-shape (two wrapper rotations).
- Combinator-own lowerings: `L2-L1/linear-combination-fold-specialization.md:1-13,38-59`,
  `L2-L1/inner-product-fold-specialization.md:1-25,30-59`.
- Resolved adjudications: leaf-vs-fold fork `dot-l2-leaf-floor-vs-fold-only-design` RATIFIED (b)
  cohort-wide with `nrm2` carved out as consumer-not-member (`scaffolding/open-questions.md:594-595`);
  `normalize` third thin-identity sub-shape (`:651`); slug convention RATIFIED `-body-identity` /
  `-leaf-identity` (`:599`).
- D1/D2 wave-1 sibling reports: `reports/2026-06-01T190900Z-combinator-miner-refactor-pass-linear-combination-family/CYCLE.md`
  exists but is empty at audit time (sibling still in flight) — the D1/D2 KEEP verdicts on the two
  fold-specialization themes are cross-confirmed here from the theme content + the resolved
  leaf-vs-fold-fork ledger, NOT from the sibling reports (which had not yet landed).

## Open questions / caveats

- **D1/D2 sibling reports not yet readable at audit time.** The wave-1 D1 combinator-miner report
  dir exists but `CYCLE.md` was empty when read (sibling parallel-in-flight). My cross-confirm of the
  two fold-specialization KEEP verdicts rests on the theme content + the resolved
  `dot-l2-leaf-floor-vs-fold-only-design` ledger ratification, not on the sibling reports. The
  integrator should reconcile this worklist against the landed D1/D2 maps; I predict **agreement**
  (both fold-specialization themes are genuine arity/conjugation-dispatch translations), but flag the
  reconciliation as a required cross-check, not a settled fact.
- **`nrm2`-consumer-vs-member (the question the planner flagged D2 decides).** RESOLVED in the ledger
  (`:595`): `nrm2` is a *consumer* of `inner_product` at the diagonal `y=x`, NOT a fold member
  (do-NOT-merge per `L2/inner_product.md` §"Consumer (NOT an instance)"). Consequence for the
  worklist: both `nrm2` themes DEMOTE-to-inline on the `nrm2` entries — they do NOT
  ABSORB-into-combinator-note (a consumer has no combinator-membership row to fold into). If D2's
  landed map instead treats `nrm2` as a member, that is a divergence the integrator/meta-phase must
  catch — but the ledger carve-out is explicit and I follow it.
- **The 6 constructed-operator-gate / composite themes (B, divfree-projector + jacobi-smoother
  marked "verify").** `divfree-projector` (four-step composition `WeakDiv → Z → ksp_solve → Grad`)
  and `jacobi-smoother` (`op.dinv ⊙ x`) are gates, not BLAS-1 leaves; their bodies are *compositions*
  that happen to be explicit-at-both-layers (hence identity-in-named-terms today). I read only their
  heads. The cycle-050 enactor should confirm the body genuinely carries no vocabulary shift before
  demoting (a four-step composition that is identical at L3 and L2 IS degenerate, but verify the L2
  form does not erase/rename a step). `normalize` (`nrm2 ∘ scal` fused composite) is the resolved
  third sub-shape (`:651`) and demotes cleanly. `assemble-diagonal`/`elementwise-product`/
  `reciprocal` are clean leaf demotes.
- **Scope-boundary surfaced as a finding, not enacted.** I do not author or edit anything; the 18-vs-12
  finding is surfaced for the integrator/meta-phase to fold into the cycle-050 dispatch scope. If the
  planner intentionally scoped only the 6 BLAS-1 pairs for cycle-050 and means to handle the other 6
  in cycle-051, that is a valid sequencing choice — but it should be a *choice*, not an oversight, so
  I flag it.
- **No `book/` mutation performed** (DISPATCH-phase read-only audit; OQ-ledger-append-only discipline
  observed — this report is the surfaced artifact, no artifact file touched).
