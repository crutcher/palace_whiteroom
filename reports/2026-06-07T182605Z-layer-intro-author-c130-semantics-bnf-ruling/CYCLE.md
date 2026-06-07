---
agent: layer-intro-author
invoked_at: 2026-06-07T182605Z
scope: semantic-surface §1.3 BNF op-with-params promotion + §1.2.2 cohort-sweep RULING (c130 D1 LEAD)
status: pending
integrated_at: 2026-06-07T210500Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-130 (batch-42 OPENER, 1/3) D1 applied clean. §1.3 op-with-params BNF introducer + §1.2.2-R ruling block landed on book/src/semantics/index.md; no status/rank/edge change. Build EXIT 0; graded-stack baseline HELD (rank_violations 0, unresolved 0). 2 OQs promoted (closure-signature-op-with-params-bnf-promotion RESOLVED-BY-LANDING [BNF half], closure-signature-cohort-sweep-1.2.2-R-scope-gate). The BNF half of the closure-signature introduction-form is discharged end-to-end."
---

# CYCLE: semantics/index.md — §1.3 BNF `op-with-params` introducer + §1.2.2 cohort-sweep ruling

## Summary

Two coupled edits to the semantic surface `book/src/semantics/index.md`, the c130 batch-42 polish-pass LEAD:

- **(a) `op-with-params` BNF introducer — GO.** I add the `op-with-params { … ; λ … } : Op[…]` introducer production to the §1.3 `e ::=` expression grammar block, sitting it directly beside its existing `apply A e` eliminator. Rationale: the §3.5 `apply` reduction rule already *uses* the redex term `op-with-params p` (line 229), and §1.3.1's prose/example (line 163) already gives the full introduction form `op-with-params { p₁ = e₁, … ; λ(x: τ_in). e_body }` — so the §1.3 grammar was the **only** place where the operator-value term form was un-generated, leaving the reduction rule mentioning a term the grammar can't produce. Promoting the introducer closes that asymmetry. This is a single new `|` alternative inside an existing BNF block — **no section/rule renumbering**, so the c128-D1 "avoid the strawman BNF-renumbering" caution is respected. Closes OQ `closure-signature-introduction-form-into-bnf-and-role-discipline-bullet` (BNF-promotion half; friendly slug `closure-signature-op-with-params-bnf-promotion`).
- **(b) §1.2.2 cohort-sweep RULING — PINNED.** I add a crisp **per-site decision rule** (a short ruling block) to the §1.2.2 region so D2 (the lifter sweep, WAVE-2) can apply it mechanically: a **calculus-level operator-VALUE codomain** (an operator constructor/transformer return, or a theme-LHS signature codomain at L4/L3/L2) → spell bracketed (`LinOp[(N: ...), $N]` / `Op[τ_in → τ_out]`); the opaque `LinearOperator[N,N]` type-application form is the **non-compliant smell** → re-spell to bracketed, do NOT paren-wrap. A **genuine rank-1 flat-dof form** (an L1/L0 vector, or a plain operator-VALUE *record field* where the dim is a genuine flat-dof length) is **KEPT** per §1.2.2:95 — the convention governs closure-RETURNING calculus signatures, not genuine rank-1 L1/L0 forms.

USE+LINK only — the ruling block points at the already-settled §1.2.2 / §1.3.1 / §1.3.1-table-row machinery; it does not restate the convention, it states the *per-site application decision* in one place so the sweep has a single scope-gate to read. Prose/BNF only; NO L4-chapter edits (D2 owns the chapter sweep).

## Proposed changes

### (a) §1.3 BNF — add the `op-with-params` introducer production

```edit:book/src/semantics/index.md
[old]:
    | op(e₁, ..., eₙ)                        -- primitive operator application
    | apply A e                              -- operator application
    | return e                               -- monadic return (Sim)
[new]:
    | op(e₁, ..., eₙ)                        -- primitive operator application
    | op-with-params { l₁ = e₁, ..., lₖ = eₖ ; λ(x: τ_in). e } : Op[τ_in → τ_out]
                                             -- operator-VALUE introducer: a record of closed-over
                                             -- !-params paired with a body lambda (§1.3.1); its
                                             -- eliminator is `apply` below (§3.5)
    | apply A e                              -- operator application (eliminates an Op value, §3.5)
    | return e                               -- monadic return (Sim)
```

### (b) §1.2.2 — pin the cohort-sweep per-site RULING

```edit:book/src/semantics/index.md
[old]:
This generalizes the rank-1 spelling `LinearOperator[M, N]` (where `M`, `N` are genuine flat dof-vector lengths) to the rank-agnostic case. At **L1/L0**, Palace operators act on flat dof-vectors and the concrete `LinearOperator[M, N]` / `Tensor[N]` rank-1 spelling is faithful — keep it there; the `LinOp[(R: ...), (D: ...)]` form is the L4/L3/L2 calculus rendering.
[new]:
This generalizes the rank-1 spelling `LinearOperator[M, N]` (where `M`, `N` are genuine flat dof-vector lengths) to the rank-agnostic case. At **L1/L0**, Palace operators act on flat dof-vectors and the concrete `LinearOperator[M, N]` / `Tensor[N]` rank-1 spelling is faithful — keep it there; the `LinOp[(R: ...), (D: ...)]` form is the L4/L3/L2 calculus rendering.

##### 1.2.2-R — the operator-VALUE spelling ruling (the cohort-sweep scope-gate)

This is the **canonical per-site decision** a whole-book closure-signature compliance sweep applies. It is the *application* of §1.2.2 + §1.3.1 (the bracketed-operator-value ruling and its table); it does not restate them. For each occurrence of an operator-value in a signature or a lowering-theme LHS:

1. **Calculus-level operator-VALUE codomain → bracketed form (CONVERT if opaque).** An operator-value in a **codomain / return position** of an L4/L3/L2 signature or a lowering-theme LHS — an operator **constructor** `mk :: A -> Op[X → Y]`, an operator **transformer** `t :: Op[X → Y] -> Op[X' → Y']`, or a calculus-level result annotation `op_w = … : LinOp[…]` — carries higher-order intent and is spelled in the **bracketed operator-value form**: `LinOp[(R: ...), (D: ...)]` (or square `LinOp[(N: ...), $N]`), or `Op[τ_in → τ_out]`. The bracket already groups the in/out arrow, so the codomain is **already compliant** and wants **no outer parens** (§1.3.1:153, :158). The **non-compliant smell** is the opaque type-application form `LinearOperator[N, N]` / `LinearOperator (Tensor[…])` — a bare type name applied to dim slots, **no in/out arrow**, the higher-order intent hidden. The fix is to **re-spell** it bracketed; wrapping the opaque form in outer parens does NOT make it compliant (§1.3.1:154).
2. **Genuine rank-1 flat-dof form → KEEP rank-1 (do NOT convert).** A genuine **rank-1 flat-dof** form is KEPT exactly as written per §1.2.2:95 ("at L1/L0 … keep it there"). This covers (i) any **L1/L0** operator/vector signature (`LinearOperator[M, N]` / `Tensor[N]` over genuine flat dof-vector lengths), and (ii) a **plain operator-VALUE record FIELD** at L4/L3 whose dim is a genuine flat-dof length (the deliberate c129-D2 within-chapter dual-spelling — e.g. an `assemble_frequency_operator` `{ K, C, M }` field, a `divfree-projector` `{ P.M, P.WeakDiv, P.Grad }` field). The convention governs closure-**RETURNING calculus signatures**, NOT genuine rank-1 L1/L0 forms; a record field that merely *holds* a rank-1 operator value is not a closure-returning signature and is out of scope.

**One-line discriminator for the sweep:** *is this an operator-value in a calculus-level (L4/L3/L2) signature/theme-LHS codomain position, spelled opaquely?* → **CONVERT to bracketed**. *Is it an L1/L0 form, or a record field holding a genuine rank-1 operator value?* → **KEEP**.
```

## Supporting evidence

On-disk facts verified in `book/src/semantics/index.md` (read in full this dispatch):

- **§1.3 `e ::=` block** (lines 105–126): contains `op(e₁, ..., eₙ)` (`:119`) and `apply A e` (`:120`) but **no** `op-with-params` introducer — confirming the asymmetry the prompt flags.
- **§3.5 operator application** (lines 224–230): the reduction rule `apply (op-with-params p, λx. e) v → e[p/params, v/x]` (`:229`) *uses* the redex term `op-with-params p` — so the term form is already load-bearing in the reduction relation, but ungenerated by the §1.3 grammar.
- **§1.3.1 introduction form** (lines 160–166): `op-with-params { p₁ = e₁, …, pₖ = eₖ ; λ(x: τ_in). e_body } : Op[τ_in → τ_out]` (`:163`) — the prose/example form already settled (c128 D1); the BNF promotion just lifts this into the grammar.
- **§1.3.1 bracketed-operator-value ruling + table** (`:153`, `:154`, `:158`): the operator-constructor/transformer-already-compliant ruling + the opaque-`LinearOperator[N,N]`-is-the-smell row — the §1.2.2-R ruling block cites these rather than restating them.
- **§1.2.2:95** (the rank-1 KEEP rule): "At **L1/L0** … the concrete `LinearOperator[M, N]` / `Tensor[N]` rank-1 spelling is faithful — keep it there" — the source of the (2) KEEP arm.
- **Plan provenance:** `scaffolding/priorities.md` CYCLE-130 head, D1 [LEAD] bullet (the (a)+(b) scope + the explicit "scope-gate for D2" framing + the c129-D2 dual-spelling KEEP sites `assemble_frequency_operator.md:103-105`, `divfree-projector` fields).
- **OQ:** `closure-signature-introduction-form-into-bnf-and-role-discipline-bullet` (open-questions.md:244, :1964) — BNF-promotion half migrated to plan Backlog Low, `layer-intro-author` semantic-surface authoring call. RESOLVED by this dispatch's (a).

## Open questions / caveats

- **OQ RESOLUTION MARKER (append authority noted).** This dispatch RESOLVES the BNF-promotion half of `closure-signature-introduction-form-into-bnf-and-role-discipline-bullet` (a.k.a. `closure-signature-op-with-params-bnf-promotion`) by adding the introducer to the §1.3 grammar (GO). I am leaving the formal ledger close to the meta-phase (it holds unify/close authority and the slug is currently parked in the plan Backlog Low), rather than appending a half-resolution marker that the meta-phase would then have to reconcile — flagging it here is the cleaner hand-off. **Recommended ledger action:** close `closure-signature-introduction-form-into-bnf-and-role-discipline-bullet` fully (both halves now landed — role-discipline-bullet enacted batch-41 meta, BNF-promotion landed c130) once this report integrates.
- **Scope-gate hand-off to D2.** The §1.2.2-R ruling block is authored as D2's single scope-gate. The one-line discriminator at the end of the block is the mechanical test D2 applies per site. D2's enumerated convert-sites (`fe-assemble-fold-dissolution.md:30,37`, `mk-matrix-free-operator-dissolution.md:151`, `fe_assemble.md:77`, `frequency_sweep.md:151`) and keep-sites (`assemble_frequency_operator.md:103-105`, `divfree-projector` fields) all fall cleanly on one side of the discriminator — no ambiguous site surfaced in my read. D2 should still on-disk re-localize each line (the plan notes OQ line numbers have drifted before).
- **Heading level of the ruling block.** I used `#####` (h5) for `1.2.2-R` to nest it under the §1.2.2 `####` (h4) sub-section without competing with the §1.2.3 `####` sibling. If the surface's heading-depth convention prefers a non-numbered bold lead-in over an h5, the integrator may demote it to a `**1.2.2-R — …**` bold paragraph; the content is unchanged either way. No SUMMARY.md entry is needed (sub-sub-sections are not separately listed).
- **No new notation introduced.** Both edits reuse existing settled notation (`Op[τ_in → τ_out]`, `LinOp[(R: ...), (D: ...)]`, the `op-with-params { … ; λ … }` form). The BNF introducer line is a verbatim grammar-ization of the §1.3.1:163 prose form. Per the USE+LINK discipline, the ruling block cites §1.2.2:95 / §1.3.1:153–158 rather than re-teaching the convention.
