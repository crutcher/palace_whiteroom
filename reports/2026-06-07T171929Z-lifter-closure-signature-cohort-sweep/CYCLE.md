---
agent: lifter
invoked_at: 2026-06-07T171929Z
scope: L4 closure-signature non-compliant-cohort re-spell sweep + 2 stale-token corrections — highorder-signature-noncompliant-cohort-c129-lifter-sweep
status: integrated
integrated_at: 2026-06-07T193500Z
integration_commit: f153841
integration_notes: |
  cycle-129 D2 (WAVE-2, dep D1). Applied clean by integrator-per-report (staging row 2). Re-spelled the 7 opaque LinearOperator[...] high-order/closure codomain sites to the bracketed LinOp[(N: ...), $N] form across L4/assemble_frequency_operator.md (4: :99,:106,:127,:293), L4/fe_assemble.md (3: :60,:71,:35) + the 2 narrative L4/index.md rows (:61 eliminate_bc reconcile, :62 fe_assemble); + 2 evidenced stale-token corrections — mk_matrix_free_operator roadmap_goal->firm (c127) in fe_assemble.md:16,164; boundary-mode.L4 rough-in->firm in lifecycle.L4.md:72 (both nodes already firm on disk). RESOLVES OQ highorder-signature-noncompliant-cohort-c129-lifter-sweep + fe-assemble-stale-mk-matrix-free-roadmap-goal-token + lifecycle-l4-stale-boundary-mode-rough-in-token (RESOLVED markers = batch-41 meta unify-authority). DELIBERATE within-chapter plain operator-VALUE rank-1 dual-spelling PRESERVED -> routed to META-owned OQ closure-signature-l4-constructor-restatement-compliance-cohort-sweep. NO status/rank/edge change (pure prose/signature re-spell + 2 stale-prose maturity-token corrections; underlying nodes already firm; constructs-via edge stays reference-class). Build EXIT 0; ZERO finalize build-repairs. All totals HELD vs c127/c128.
inputs:
  - book/src/L4/assemble_frequency_operator.md
  - book/src/L4/fe_assemble.md
  - book/src/L4/index.md
  - book/src/L4/eliminate_bc.md (read-only consult — NOT edited; already compliant per D1)
  - book/src/feature/lifecycle.L4.md
  - book/src/feature/boundary-mode.L4.md (read-only verify rank: firm)
  - book/src/L4/mk_matrix_free_operator.md (read-only verify status: firm + the Op[...] exemplar :58-65)
  - book/src/semantics/index.md §1.2.2 (:88-95) + §1.3.1 (D1's pinned ruling)
  - reports/2026-06-07T171604Z-layer-intro-author-transformer-codomain-adjudication/CYCLE.md (D1 — the scope-gate ruling)
  - reports/2026-06-07T171246Z-cycle-planner-cycle-129/CYCLE.md (D2 scope)
---

# CYCLE: Re-anchor closure-signature non-compliant cohort to §1.3.1 + 2 stale-token fixes

## Summary

Cycle-129 D2 (WAVE-2, dep D1). A pure-rewrite fidelity sweep that re-spells the
OPAQUE high-order/closure-returning signature codomains `LinearOperator[N, N]`
in the two L4 FE-constructor chapters + their `L4/index.md` narrative mirror rows
into the §1.3.1-compliant bracketed operator-value spelling, plus two stale
maturity-token corrections that touch the same two chapters. **D1's ruling is the
scope gate:** a bracketed operator-value codomain (`Op[…]` / `LinOp[…]`) is
ALREADY COMPLIANT (the bracket carries the in/out arrow); the non-compliant smell
is specifically the OPAQUE type-application form `LinearOperator[N, N]` (no in/out
arrow → hides the higher-order intent). The fix is to RE-SPELL the opaque form,
NOT to wrap in outer parens. **`eliminate_essential_bc` is OUT of the sweep** —
its chapter codomain (`eliminate_bc.md:83-84`) and the `L4/index.md` TABLE rows
`:110`/`:114`/`:115` are already bracketed `LinOp[(S: ...), $S]` and stand
untouched; only the `L4/index.md` NARRATIVE row `:61` spells `eliminate_essential_bc`
in the opaque form and is moved to agree with the canonical bracketed chapter/TABLE
form.

**Spelling decision (matching the already-compliant TABLE rows + §1.2.2).** Per
semantics §1.2.2 (`semantics/index.md:88-95`), `LinearOperator[M, N]` is the
**rank-1 L1/L0 flat-dof-vector** spelling, faithful only at L1/L0; the L4/L3/L2
calculus rendering of a **square / endomorphic** operator value is
`LinOp[(S: ...), $S]` (binds one group, uses it for the range). Both target
chapters' opaque codomains are square operators on the chapter's axis `N`, so the
canonical re-spell is **`LinOp[(N: ...), $N]`** — exactly matching the
already-compliant `L4/index.md` TABLE rows for these same chapters (`:110`
`assemble_frequency_operator` `LinOp[(S: ...), $S]`; `:115` `fe_assemble`
`LinOp[(S: ...), $S]`), keeping the chapter's own axis name `N`. The `A2`
closure-RETURNING field `Scalar -> LinearOperator[N, N]` re-spells to
`Scalar -> LinOp[(N: ...), $N]` (a function from scalar to a square operator
value). This is the §1.2.2 square-op form D1 explicitly sanctioned as the fix
target (alternative to `Op[Tensor[$N] → Tensor[$N]]`); the square-op form is
chosen for consistency with the chapters' existing TABLE-row spelling.

**Bounded scope (NOT over-rewritten):** the plain operator-VALUE record fields
`K / C / M : LinearOperator[N, N]` (`assemble_frequency_operator.md:103-105`) and
the plain result-line `LinearOperator[N, N]` descriptions (`:121`, `:137`) are NOT
closure-returning / high-order signatures — they are out of THIS sweep's cohort
(the §1.3.1 closure-signature compliance question, not the §1.2.2 flat-vector
rendering question). They are left untouched per D1's enumerated scope + the
planner's "do not over-rewrite plain value fields" instruction. A separate
whole-book §1.2.2 flat-vector→calculus-rendering decision (the META-owned
`closure-signature-l4-constructor-restatement-compliance-cohort-sweep` OQ) governs
those; flagged in §Open questions.

## Proposed changes

### 1. `book/src/L4/assemble_frequency_operator.md` — re-spell the 4 opaque high-order/closure sites

The signature codomain (`:99`), the `A2` closure-returning record field (`:106`),
its shape-contract prose restatement (`:127`), and the "Downward to L1" restated
signature (`:293`). All four are opaque-`LinearOperator[N, N]` high-order /
closure-returning forms; re-spelled to `LinOp[(N: ...), $N]`.

```edit:book/src/L4/assemble_frequency_operator.md
[old]:    assemble_frequency_operator
      :: FrequencyOperatorFamily[N] -> Scalar -> LinearOperator[N, N]
[new]:    assemble_frequency_operator
      :: FrequencyOperatorFamily[N] -> Scalar -> LinOp[(N: ...), $N]
```

```edit:book/src/L4/assemble_frequency_operator.md
[old]:      , A2 : Scalar -> LinearOperator[N, N]  -- frequency-dependent extra term (closure over ω)
[new]:      , A2 : Scalar -> LinOp[(N: ...), $N]  -- frequency-dependent extra term (closure over ω)
```

```edit:book/src/L4/assemble_frequency_operator.md
[old]:- `fam.A2` — `Scalar -> LinearOperator[N, N]` — the frequency-dependent extra term,
[new]:- `fam.A2` — `Scalar -> LinOp[(N: ...), $N]` — the frequency-dependent extra term,
```

```edit:book/src/L4/assemble_frequency_operator.md
[old]:`assemble_frequency_operator :: FrequencyOperatorFamily[N] -> Scalar -> LinearOperator[N, N]`,
[new]:`assemble_frequency_operator :: FrequencyOperatorFamily[N] -> Scalar -> LinOp[(N: ...), $N]`,
```

### 2. `book/src/L4/fe_assemble.md` — re-spell the 3 opaque high-order sites + 2 stale-token corrections

The `fe_assemble` signature codomain (`:60`) and the `assemble_term` leaf signature
(`:71` in §Signature; `:35` in §Context point 2) are opaque operator-value
codomains; re-spelled to `LinOp[(N: ...), $N]`.

```edit:book/src/L4/fe_assemble.md
[old]:    fe_assemble :: FiniteElementSpace[N] -> [WeakFormTerm] -> LinearOperator[N, N]
    fe_assemble space terms = foldr (\t acc -> assemble_term space t + acc) zero terms
[new]:    fe_assemble :: FiniteElementSpace[N] -> [WeakFormTerm] -> LinOp[(N: ...), $N]
    fe_assemble space terms = foldr (\t acc -> assemble_term space t + acc) zero terms
```

```edit:book/src/L4/fe_assemble.md
[old]:    assemble_term :: FiniteElementSpace[N] -> WeakFormTerm -> LinearOperator[N, N]

Shape contract
[new]:    assemble_term :: FiniteElementSpace[N] -> WeakFormTerm -> LinOp[(N: ...), $N]

Shape contract
```

```edit:book/src/L4/fe_assemble.md
[old]:2. **The per-term assembly leaf is an opaque black-box-kernel input.** `assemble_term :: FiniteElementSpace[N] -> WeakFormTerm -> LinearOperator[N,N]` is the element-local→global quadrature contraction (restriction + basis-apply + quadrature) — **libCEED-owned**, not Palace-authored.
[new]:2. **The per-term assembly leaf is an opaque black-box-kernel input.** `assemble_term :: FiniteElementSpace[N] -> WeakFormTerm -> LinOp[(N: ...), $N]` is the element-local→global quadrature contraction (restriction + basis-apply + quadrature) — **libCEED-owned**, not Palace-authored.
```

**Stale-token correction 1 (`fe-assemble-stale-mk-matrix-free-roadmap-goal-token`).**
`mk_matrix_free_operator` is `firm` since c127 (verified on-disk this dispatch:
`book/src/L4/mk_matrix_free_operator.md:4-5` `status: firm` / `rank: firm`); the
two prose tokens still describe it as `roadmap_goal`. The `constructs-via`
`reference`-class relationship is correct regardless — only the maturity TOKEN is
stale. NO edge/rank/frontmatter change.

```edit:book/src/L4/fe_assemble.md
[old]:    - target: L4/mk_matrix_free_operator
      kind: constructs-via   # NAVIGATIONAL `reference` (NOT depends-on): the matrix-free constructive interior of this fold's per-term `assemble_term` leaf under the `UseFullAssembly`-false dispatch. `mk_matrix_free_operator` is a rank-0 `roadmap_goal`; a firm node may `reference` it (free, no liveness/rank constraint — scheme §1g) but must NOT `depends-on` it (would violate well-foundedness). This is the pull-to-root that keeps `mk_matrix_free_operator` reachable / not-garbage.
[new]:    - target: L4/mk_matrix_free_operator
      kind: constructs-via   # NAVIGATIONAL `reference` (NOT depends-on): the matrix-free constructive interior of this fold's per-term `assemble_term` leaf under the `UseFullAssembly`-false dispatch. `mk_matrix_free_operator` is `firm` (c127); a firm node may `reference` it (free, no liveness/rank constraint — scheme §1g) and a `reference` edge carries no rank constraint regardless of the target's rank. This is the pull-to-root that keeps `mk_matrix_free_operator` reachable / not-garbage.
```

```edit:book/src/L4/fe_assemble.md
[old]:The opaque per-term leaf `assemble_term` has a **matrix-free constructive interior** under the `partial matrix-free` (`UseFullAssembly`-false) dispatch (`palace/fem/bilinearform.cpp:143`): the L4 backend-lowering operator-constructor [`mk_matrix_free_operator`](./mk_matrix_free_operator.md) (`roadmap_goal`, c126 D1), whose `apply` is the firm [`L2/matrix-free-operator-apply`](../L2/matrix-free-operator-apply.md) contraction chain `A = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G`. This is a **navigational `reference` (`constructs-via`), NOT a `depends-on`** — `fe_assemble` folds `assemble_term` as an *opaque black-box-kernel input* (its firmness is in the fold apparatus, not the leaf interior); the matrix-free interior is the backend-lowering surface a future L4 feature column will firm, pulled to a root by this navigational edge. A firm node may reference a rank-0 `roadmap_goal` (free, scheme §1g); it must not block on it.
[new]:The opaque per-term leaf `assemble_term` has a **matrix-free constructive interior** under the `partial matrix-free` (`UseFullAssembly`-false) dispatch (`palace/fem/bilinearform.cpp:143`): the L4 backend-lowering operator-constructor [`mk_matrix_free_operator`](./mk_matrix_free_operator.md) (`firm`, c127), whose `apply` is the firm [`L2/matrix-free-operator-apply`](../L2/matrix-free-operator-apply.md) contraction chain `A = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G`. This is a **navigational `reference` (`constructs-via`), NOT a `depends-on`** — `fe_assemble` folds `assemble_term` as an *opaque black-box-kernel input* (its firmness is in the fold apparatus, not the leaf interior); the matrix-free interior is the backend-lowering surface the firm `mk_matrix_free_operator` constructor + its firm `matrix-free-operator-apply` lowering supply, pulled to a root by this navigational edge. The `constructs-via` edge stays `reference` (navigational, free) — a `reference` edge carries no rank constraint regardless of the target's rank.
```

### 3. `book/src/L4/index.md` — re-spell the 2 narrative-row opaque sites + the `eliminate_bc` reconcile

The two chapter-list NARRATIVE rows (`:61` `eliminate_bc`, `:62` `fe_assemble`)
carry opaque applied-spelling signatures. Per D1's ruling the canonical form is the
already-bracketed chapter/TABLE spelling, so the opaque narrative is the side that
moves. (On-disk re-localized; the OQ's `:61,62` line-pointers were verified to land
on these exact narrative rows. The bracketed TABLE rows `:110`/`:114`/`:115` and the
`:101` `chebyshev` `LinOp[E]` row are already compliant and untouched; `:119` was
done by the c128 finalize and is untouched.)

**`eliminate_bc` narrative row `:61`** — the embedded `eliminate_essential_bc`
signature is opaque `LinearOperator[N,N] -> LinearOperator[N,N]`; re-spelled to
agree with the canonical bracketed chapter form `eliminate_bc.md:83-84`
(`LinOp[(S: ...), $S] -> LinOp[$S, $S]`) and the TABLE row `:114`. (The `eliminate_rhs`
codomain `Tensor[N]` in the same row is a plain tensor result, not an operator value
— out of scope, untouched.)

```edit:book/src/L4/index.md
[old]:that pins essential (Dirichlet) dofs into an assembled operator (`eliminate_essential_bc :: LinearOperator[N,N] -> LinearOperator[N,N]`, zero the essential rows/cols + set the eliminated diagonal per policy)
[new]:that pins essential (Dirichlet) dofs into an assembled operator (`eliminate_essential_bc :: LinOp[(S: ...), $S] -> LinOp[$S, $S]`, zero the essential rows/cols + set the eliminated diagonal per policy)
```

**`fe_assemble` narrative row `:62`** — the embedded `assemble_term` leaf signature
is opaque `LinearOperator[N,N]`; re-spelled to `LinOp[(N: ...), $N]` to match the
now-swept `fe_assemble.md:71`/`:35` chapter form.

```edit:book/src/L4/index.md
[old]:The opaque per-term libCEED quadrature leaf `assemble_term :: FiniteElementSpace[N] -> WeakFormTerm -> LinearOperator[N,N]` rises as a **black-box-kernel `readonly` input** ([`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md) case 1
[new]:The opaque per-term libCEED quadrature leaf `assemble_term :: FiniteElementSpace[N] -> WeakFormTerm -> LinOp[(N: ...), $N]` rises as a **black-box-kernel `readonly` input** ([`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md) case 1
```

### 4. `book/src/feature/lifecycle.L4.md` — stale-token correction 2

`boundary-mode.L4` is `rank: firm` on disk (verified this dispatch:
`book/src/feature/boundary-mode.L4.md:5` `rank: firm`); the constituent-down-links
dispatch-table cell `:72` still marks it `rough-in`. One-cell maturity-token
correction; NO frontmatter/rank/edge change to any node.

```edit:book/src/feature/lifecycle.L4.md
[old]:| dispatch → eigenmode / driven / transient / boundary-mode columns | [eigenmode.L4](./eigenmode.L4.md) / [driven.L4](./driven.L4.md) / [transient.L4](./transient.L4.md) / [boundary-mode.L4](./boundary-mode.L4.md) (sibling references) | firm / firm / firm / rough-in | `palace/main.cpp:264, 261, 273, 276` |
[new]:| dispatch → eigenmode / driven / transient / boundary-mode columns | [eigenmode.L4](./eigenmode.L4.md) / [driven.L4](./driven.L4.md) / [transient.L4](./transient.L4.md) / [boundary-mode.L4](./boundary-mode.L4.md) (sibling references) | firm / firm / firm / firm | `palace/main.cpp:264, 261, 273, 276` |
```

## Discipline notes

- **Pure-rewrite / fidelity sweep + 2 maturity-token corrections — NO frontmatter
  status/rank/edge change to ANY chapter.** Every edit re-spells PROSE / signature
  text or corrects a prose maturity TOKEN describing a node that is ALREADY firm on
  disk (`mk_matrix_free_operator` firm c127; `boundary-mode.L4` `rank: firm`). No
  DAG-node rank moves; the linter baseline holds unchanged (consistent with the
  planner's "NO RE fires" note). The `constructs-via` edge in `fe_assemble.md`
  frontmatter stays `kind: constructs-via` (a `reference`-class edge) — only its
  inline comment's stale `roadmap_goal` wording was corrected; the edge structure /
  class is unchanged.
- **Bounded prose-token correction, evidenced + recorded** (lifter scope-boundary,
  CLAUDE.md §Discipline "L0-evidence-driven prose correction is in-scope when
  bounded + evidenced + recorded"). The two stale-token fixes are bounded
  maturity-snapshot corrections supported by the on-disk frontmatter of the
  described nodes (`mk_matrix_free_operator.md:4-5`; `boundary-mode.L4.md:5`), not
  re-architecture. Recorded here.
- **`eliminate_essential_bc` LEFT UNTOUCHED in its chapter + the TABLE rows, per
  D1's ruling.** `eliminate_bc.md:83-84` is already the bracketed compliant
  `LinOp[(S: ...), $S] -> ... -> LinOp[$S, $S]` and was NOT edited (read-only
  consult). The `L4/index.md` TABLE rows `:110` / `:114` / `:115` (all bracketed
  `LinOp[(S: ...), $S]`) were NOT edited. Only the `L4/index.md` NARRATIVE row
  `:61` — which spelled `eliminate_essential_bc` in the OPAQUE form — was moved to
  agree with the canonical bracketed chapter/TABLE form (the reconcile direction
  D1 pinned: bracketed-is-compliant ⇒ the opaque narrative is the side that moves).
- **Spelling = `LinOp[(N: ...), $N]`** (the §1.2.2 square-operator calculus
  rendering, D1-sanctioned), chosen over `Op[Tensor[$N] → Tensor[$N]]` because
  these codomains are operator-VALUES (the assembled `K` / `A(ω)`), not freshly-built
  closure constructors, and because it matches the already-compliant TABLE rows for
  the same two chapters (`:110`/`:115` use `LinOp[(S: ...), $S]`). Chapter axis `N`
  preserved (TABLE rows used `S`; both are §1.2.2-valid group names — keeping `N`
  preserves chapter-internal consistency).
- **USE+LINK to §1.3.1 / §1.2.2 already established in both chapters** (the
  `mk_matrix_free_operator` exemplar `:58` already cites §1.3.1; both target
  chapters already reference `semantics/index.md`). No convention RE-statement
  added — the re-spelled signatures simply conform.

## Supporting evidence

- D1's pinned ruling: `reports/2026-06-07T171604Z-layer-intro-author-transformer-codomain-adjudication/CYCLE.md`
  (bracketed = already compliant; opaque `LinearOperator[...]` = the smell → re-spell,
  not wrap; `eliminate_essential_bc` OUT of sweep; reconcile-direction pinned).
- `book/src/semantics/index.md:88-95` (§1.2.2) — the square-operator calculus
  spelling `LinOp[(S: ...), $S]` + the rank-1 `LinearOperator[M, N]` is L1/L0-faithful-only
  rule (the fix-target sanction).
- `book/src/L4/mk_matrix_free_operator.md:4-5` (`status: firm` / `rank: firm`,
  c127), `:58-65` (the `Op[Tensor[(N: ...)] → Tensor[(N: ...)]]` constructor exemplar
  + the §1.3.1 USE+LINK precedent).
- `book/src/feature/boundary-mode.L4.md:5` (`rank: firm`) — the stale-token-2 ground.
- `book/src/L4/eliminate_bc.md:83-84` (the bracketed canonical `eliminate_essential_bc`
  signature the index narrative `:61` reconciles to) — read-only consult, NOT edited.
- `book/src/L4/index.md:110,114,115` — the already-compliant bracketed TABLE rows
  (untouched), the spelling-consistency template for the re-spelled chapters/narratives.

## Open questions / caveats

- **Plain operator-VALUE `LinearOperator[N, N]` sites NOT swept (deliberately out
  of THIS cohort).** `assemble_frequency_operator.md:103-105` (the `K/C/M` fixed-basis
  record fields), `:121`/`:137` (plain result-line descriptions), and
  `fe_assemble.md:77` (the `result — LinearOperator[N, N]` shape-contract line) are
  plain operator-value spellings, NOT closure-returning / high-order signatures.
  D1's enumerated scope + the planner's "do not over-rewrite plain value fields"
  instruction keep them out of this §1.3.1 closure-signature sweep. Whether ALL L4
  `LinearOperator[N, N]` operator-value spellings should additionally be rendered in
  the §1.2.2 calculus form `LinOp[(N: ...), $N]` is the separate META-owned
  whole-book OQ `closure-signature-l4-constructor-restatement-compliance-cohort-sweep`
  — NOT this dispatch's scope. Flagging for the batch-41 meta: after this sweep, the
  two chapters carry a MIX (high-order codomains in `LinOp[...]` calculus form; plain
  value fields still in `LinearOperator[N, N]` rank-1 form). That mix is consistent
  with the current scope boundary (§1.3.1 closure-signature compliance is discharged;
  the §1.2.2 flat-vector-rendering question is the meta's cohort sweep), but a reader
  may notice the within-chapter dual-spelling — the meta's cohort sweep is where it
  resolves to one form.
- No abstractor reread needed: every re-spell is a notation conformance with the
  identical semantics (the operator-value codomain is unchanged in meaning); no
  signature SHAPE changed, no LHS/RHS shifted, no decomposition altered.
