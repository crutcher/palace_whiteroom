---
agent: lifter
invoked_at: 2026-06-07T190246Z
scope: §1.2.2-R residual operator-VALUE codomain sweep — calculus-codomain sites the c130 sweep did not reach
status: pending
integrated_at: 2026-06-07T192500Z
integration_commit: 3f19e0b5aeab590d7d0a9a1adf6b28cef88a2552
integration_notes: |
  Applied clean as the sole report of cycle-131 (batch-42 position 2/3, §1.2.2/closure-signature
  POLISH PASS). 4 §1.2.2-R operator-VALUE-codomain spelling-fidelity edits applied faithfully
  across book/src/L2/matrix-free-operator-apply.md:72, book/src/L2/index.md:143 (dep-map mirror row),
  and book/src/L4/assemble_frequency_operator.md (:137, :146). Pure prose/signature fidelity — NO
  status/rank/edge/maturity change; graded-stack baseline HELD (rank_violations=0, unresolved=0,
  reachable=163, reference_reachable=247). The §1.2.2-R operator-VALUE-codomain CONVERT cohort is
  EXHAUSTED: `grep -rnE '\-> *LinearOperator\['` over book/src/{L4,L3,L2}+lowering dirs = 0 hits.
  cargo make book EXIT 0, zero build-repairs. 1/1 staging row == 1 dispatched-ready (112th
  consecutive clean staging). Recommend the batch-42 meta-phase (fires after c132) formally mark
  the §1.2.2-R operator-VALUE-codomain axis COMPLETE (re-confirm with the arrow-codomain grep).
inputs:
  - book/src/semantics/index.md  (the pinned §1.2.2-R ruling :97-104; the bracketed exemplar §1.2.2:89-95)
  - book/src/L2/matrix-free-operator-apply.md
  - book/src/L4/assemble_frequency_operator.md
  - book/src/L4-L3/fe-assemble-fold-dissolution.md
---

# CYCLE: §1.2.2-R residual operator-VALUE codomain sweep

## Summary
Pure prose/signature FIDELITY pass applying the pinned §1.2.2-R ruling
([`semantics/index.md`](../../book/src/semantics/index.md) §1.2.2-R, `:97-104`; bracketed
exemplar `LinOp[(N: ...), $N]` defined §1.2.2 `:89-95`) to the residual calculus-codomain
sites the c130 sweep left untouched. Two genuine opaque-`LinearOperator[…]` codomain smells
convert to the bracketed square form: the L2 combinator constructor codomain in
`matrix-free-operator-apply.md:72`, and two result-codomain prose sites in
`assemble_frequency_operator.md` (`:137`, `:146`) that lagged the already-bracketed signature
codomain at `:99`. The deliberate carve-outs (the `{K, C, M}` rank-1 record FIELDS at `:103-105`/`:121`,
and the law-prose / conceptual-noun mentions at `:69`/`:215`/`:335`) are KEPT per §1.2.2-R clause 2.
The optional `fe-assemble-fold-dissolution.md:3` touch is KEPT (operand-monoid-carrier bare-word noun,
not a codomain). NO status/rank/edge/maturity change. After this pass the §1.2.2-R **convert** cohort
is exhausted (finding for the meta-phase, below).

## Per-site decisions

### CONVERT

- **`matrix-free-operator-apply.md:72`** — `-> LinearOperator[(N: ...)]` is the codomain of the
  calculus-level (L2) combinator **constructor** signature (`:71-72`). Opaque type-application form,
  no in/out arrow → the §1.2.2-R clause-1 smell (`semantics/index.md:101`). The operator is **square**
  (the `apply` line `:75` confirms domain ≡ range, both `(N: ...)`). CONVERT to the square bracketed
  form `LinOp[(N: ...), $N]` (the exemplar at §1.2.2:93 / the compliant sibling already at
  `assemble_frequency_operator.md:99`).

- **`assemble_frequency_operator.md:137`** — `result — LinearOperator[N, N] — the combined operator A(ω)`.
  This is the result-codomain prose for the verb whose signature codomain is `LinOp[(N: ...), $N]` at
  `:99` — a calculus-level result annotation (§1.2.2-R clause-1 "a calculus-level result annotation
  `op_w = … : LinOp[…]`", `semantics/index.md:101`). It lags the bracketed `:99` form. CONVERT to
  `LinOp[(N: ...), $N]`. (The bare-word "itself a `LinearOperator`" on `:138` is a conceptual noun — no
  dim slots — and is KEPT, same class as `:215`.)

- **`assemble_frequency_operator.md:146`** — `the single return slot is LinearOperator[N, N]`. The
  return-slot is the verb's result codomain; same §1.2.2-R clause-1 calculus-level result annotation,
  lagging `:99`. CONVERT to `LinOp[(N: ...), $N]`.

### KEEP

- **`assemble_frequency_operator.md:103-105`** — `{ K, C, M } : LinearOperator[N, N]` record FIELDS.
  KEEP. §1.2.2-R clause-2 (`semantics/index.md:102`): a plain operator-VALUE record FIELD whose dim is a
  genuine flat-dof length is the deliberate c129-D2 within-chapter dual-spelling, out of scope for the
  closure-returning-signature convention. (The `A2` field `:106` is already the bracketed closure form.)

- **`assemble_frequency_operator.md:121`** — `fam.K, fam.C, fam.M — LinearOperator[N, N]` shape-precondition
  prose. KEEP. Direct prose reference to the `:103-105` record fields (the carve-out), §1.2.2-R clause-2.

- **`assemble_frequency_operator.md:215`** (law 6) and **`:335`** (dependencies prose), plus **`:69`**.
  KEEP. Law-prose / conceptual-noun + operand-monoid-carrier mentions of the rank-1 record-field operands
  the combination folds over — bare conceptual nouns, not calculus-signature codomains. §1.2.2-R
  one-line discriminator (`semantics/index.md:104`): not an operator-value in a codomain position.

- **`fe-assemble-fold-dissolution.md:3`** (optional touch) — `reduce the per-term LinearOperator[N,N]
  contributions by operator-+`. KEEP. The mention names the per-term **operand-monoid carriers** being
  reduced (the operand values folded over), not a calculus-signature codomain — a bare-word/operand noun
  of the same class as `assemble_frequency_operator.md:69`/`:335`. The prompt gates this touch on "only if
  a genuine codomain, not a bare-word noun"; it is a bare-word noun → no touch.

## Proposed changes

```edit:book/src/L2/matrix-free-operator-apply.md
[old]:
    matrix-free-operator-apply
      :: ElemRestriction -> Basis -> GeomData -> Coefficient
      -> LinearOperator[(N: ...)]
    -- one term's element-local→global linear operator, as a contraction-chain fold
[new]:
    matrix-free-operator-apply
      :: ElemRestriction -> Basis -> GeomData -> Coefficient
      -> LinOp[(N: ...), $N]
    -- one term's element-local→global linear operator, as a contraction-chain fold
```

```edit:book/src/L2/index.md
[old]:Coefficient -> LinearOperator[(N: ...)]`
[new]:Coefficient -> LinOp[(N: ...), $N]`
```
(REPAIRER-ADDED, c131 repair: the L2 dep-map API-list **mirror row** for
`matrix-free-operator-apply` carries the identical `mk-operator :: … -> LinearOperator[(N: ...)]`
constructor-codomain in the opaque form — the index-mirror of the chapter signature converted at
`matrix-free-operator-apply.md:72`. Same §1.2.2-R clause-1 codomain smell; converted to the same
square bracketed spelling for chapter↔index agreement. The adjacent `apply A :: Tensor[(N: ...)] ->
Tensor[(N: ...)]` on the same row is domain/range type-application, NOT a codomain smell → left
untouched. Mirror-row conversion of the same shape as the c130 D2 `L4-L3/index.md:46` mirror fix.)

```edit:book/src/L4/assemble_frequency_operator.md
[old]:
- result — `LinearOperator[N, N]` — the combined operator `A(ω)`, square on the
  same axis `N`; itself a `LinearOperator` the per-ω inner solve applies (the
  apply/assemble duality, law 6).
[new]:
- result — `LinOp[(N: ...), $N]` — the combined operator `A(ω)`, square on the
  same axis `N`; itself a `LinearOperator` the per-ω inner solve applies (the
  apply/assemble duality, law 6).
```

```edit:book/src/L4/assemble_frequency_operator.md
[old]:
the single return slot is `LinearOperator[N, N]`).
[new]:
the single return slot is `LinOp[(N: ...), $N]`).
```

## Discipline notes
- Pure §1.2.2-R fidelity rewrite; signatures/prose only, no decomposition / signature-shape / status /
  rank / edge / maturity change (the prompt's "prose/signature FIDELITY only" bound).
- The two `assemble_frequency_operator` converts re-spell **result-codomain prose** to agree with the
  already-bracketed signature codomain `:99` (and the `:293` body-prose signature, which is already
  `LinOp[(N: ...), $N]`) — bringing the within-chapter result annotations into agreement with the
  bracketed signature, the analog of the c130 within-chapter lag fixes.
- The `{K, C, M}` record-field carve-out (KEEP at `:103-105`/`:121`) is the c129-D2 dual-spelling, pinned
  into §1.2.2-R clause-2 (`semantics/index.md:102`); I preserved it intact (it is genuine rank-1 flat-dof,
  not a closure-returning signature).
- USE+LINK discipline: cited the §1.2.2-R ruling + the §1.2.2:89-95 bracketed exemplar by reference; did
  not restate the rule in any chapter.

## Supporting evidence
- The ruling: `semantics/index.md:97-104` (§1.2.2-R, the convert/keep discriminator); the bracketed square
  exemplar `LinOp[(N: ...), $N]` defined at `:93`; the rank-1-KEEP clause at `:95`/`:102`/`:104`.
- The compliant sibling already in-chapter: `assemble_frequency_operator.md:99` (signature codomain) and
  `:106`/`:127` (the `A2` closure field). The converts bring `:137`/`:146` into agreement with these.
- Convert-site anchors self-verified on-disk this dispatch via `citecheck --anchor` (`matrix-free-operator-apply.md:72`
  anchor `LinearOperator` [ok]; `assemble_frequency_operator.md:137` anchor `result` [ok]; `:146` anchor
  `return slot` [ok]). KEEP-site lines (`:103-105`, `:121`, `:69`, `:215`, `:335`,
  `fe-assemble-fold-dissolution.md:3`) read on-disk this dispatch and classified per the §1.2.2-R one-line
  discriminator.

## Open questions / caveats
- **§1.2.2-R convert cohort now exhausted (finding for the meta-phase).** A whole-`book/src/` grep for the
  opaque type-application spelling (`LinearOperator[` with dim slots) leaves, after this pass, ONLY the
  three deliberate KEEP classes: (i) L1/L0 genuine rank-1 flat-dof signatures (§1.2.2:95, keep); (ii) the
  `{K, C, M}`-style operator-VALUE record FIELDS (§1.2.2-R clause-2, c129-D2 dual-spelling); (iii) law-prose /
  conceptual-noun / operand-monoid-carrier mentions (the one-line discriminator excludes them — not codomain
  positions). No calculus-level operator-VALUE **codomain** opaque smell remains. The meta-phase should
  re-confirm via the whole-book grep and, if clean, mark the §1.2.2-R closure-signature compliance sweep
  COMPLETE for the operator-VALUE-codomain axis.
  - **REPAIRER NOTE (c131 repair).** The critic narrowly DISPUTED this exhaustion finding: one calculus-level
    constructor-codomain mirror was missed — the L2 dep-map API-list row at `book/src/L2/index.md:143`, the
    index-mirror of the `matrix-free-operator-apply.md:72` signature this pass converts. The repairer added a
    proposed-change converting that mirror row to the same square bracketed spelling (above). **With
    `L2/index.md:143` now converted, the operator-VALUE-codomain axis IS complete** — the dispute is resolved
    and the meta-phase may mark it COMPLETE. **Re-confirmation grep:** use the arrow-codomain pattern
    `grep -rn -- '-> *LinearOperator\['` over `book/src/{L4,L3,L2}` + the lowering dirs (a plain `LinearOperator[`
    grep drowns the codomain hits in operand/field/L1-realization noise); it should return clean after this
    repair's edits land.
- No contradiction surfaced between any firmed signature and the prose it annotates; no abstractor rerun
  warranted (pure lift).
