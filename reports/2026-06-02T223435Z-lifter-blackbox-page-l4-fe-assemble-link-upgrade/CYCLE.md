---
agent: lifter
invoked_at: 2026-06-02T223435Z
scope: concept-page cross-ref link-upgrade — black-box-vs-accelerated-kernels → L4/fe_assemble
status: integrated
integrated_at: 2026-06-02T233500Z
integration_commit: PLACEHOLDER_SHA
integration_notes: |
  Applied by integrator-per-report (staging row D5, applied_at 2026-06-02T232140Z); finalized by integrator-finalize cycle-070.
  black-box-vs-accelerated-kernels concept page fe_assemble L1→L4 link upgrade: two fe_assemble references re-pointed ../L1/fe_assemble.md → ../L4/fe_assemble.md (:69 case-1 sibling list + :143 See-also) + the :69 prose tightening "the assemble combinator" → "the risen assemble combinator" (backed by firm L4/fe_assemble.md:169). The two were the COMPLETE set of ../L1/fe_assemble links on the page (post-edit grep confirms zero remain; the L1 cap stays the firm lower home via the lowering chain). ENACTS+CLOSES OQ l4-fe-assemble-absent-forward-ref-for-blackbox-kernel-page (closed-ENACTED-c070-D5). Build-relevant: cargo make book exit 0; both upgraded targets resolve. 0 OQs promoted; 1 OQ closed-in-artifact. Zero gate hits; retroactive-budget 0.
inputs:
  - book/src/concepts/black-box-vs-accelerated-kernels.md
  - book/src/L4/fe_assemble.md
---

# CYCLE: Re-anchor black-box-vs-accelerated-kernels page → L4/fe_assemble

## Summary
`book/src/L4/fe_assemble.md` has been on disk and `firm` since cycle-068 (status confirmed at `L4/fe_assemble.md:167-171` — the assemble-fold combinator, firm-on-positive-structure escape). The concept page `book/src/concepts/black-box-vs-accelerated-kernels.md` still links the L1 cap (`../L1/fe_assemble.md`) in two places where the surrounding prose specifically means the *risen L4 combinator*. Both occurrences are case-1 black-box-taxonomy / See-also references that explicitly narrate the assemble fold **rising** to L4 with the libCEED quadrature leaf as an opaque-surface input. Per the skill `upgrade-plain-text-ref-to-live-link-when-target-on-disk` and the case-1 "RISES to L4" taxonomy, both are redirected to `../L4/fe_assemble.md`. Pure cross-ref completion; no structural change. Closes OQ `l4-fe-assemble-absent-forward-ref-for-blackbox-kernel-page`.

## Proposed changes

```edit:book/src/concepts/black-box-vs-accelerated-kernels.md
[old]: - the **per-element libCEED quadrature leaf** `A(space, ·)` inside
  [`fe_assemble`](../L1/fe_assemble.md) — the element-local→global
  assembly map (restriction + basis-apply + quadrature contraction), an
  upstream-owned (libCEED) opaque kernel that the assemble fold folds over
  *without cracking open*; it rises as an opaque-surface **input** to the
  assemble combinator;
[new]: - the **per-element libCEED quadrature leaf** `A(space, ·)` inside
  [`fe_assemble`](../L4/fe_assemble.md) — the element-local→global
  assembly map (restriction + basis-apply + quadrature contraction), an
  upstream-owned (libCEED) opaque kernel that the assemble fold folds over
  *without cracking open*; it rises as an opaque-surface **input** to the
  risen assemble combinator;
```

```edit:book/src/concepts/black-box-vs-accelerated-kernels.md
[old]: - [`fe_assemble`](../L1/fe_assemble.md) — the assemble fold (combinator,
  rises) over the libCEED quadrature leaf (black-box kernel, rises as input).
[new]: - [`fe_assemble`](../L4/fe_assemble.md) — the assemble fold (combinator,
  rises) over the libCEED quadrature leaf (black-box kernel, rises as input).
```

## Discipline notes
- **Judgment per occurrence (both → L4):**
  - `:68-73` (case-1 sibling list) — the prose explicitly states the leaf "rises as an opaque-surface **input** to the assemble combinator." Case-1 of the black-box/accelerated taxonomy is, by construction, about ops that RISE to L4 as opaque-surface primitives (the page's own §"Positive reframe" + the `eigsolve`/`ksp_solve`/`fold_solve` siblings on lines 60-75 all link `../L4/`). The combinator named here is the one that rises; its firm home is now `L4/fe_assemble`. Redirected to L4, and tightened "the assemble combinator" → "the risen assemble combinator" to keep the sentence's rise-claim self-consistent with the target (bounded prose touch, supported by the firm `L4/fe_assemble.md:169` "the canonical L4 assemble-construction shape").
  - `:143-144` (See also) — the parenthetical "the assemble fold (combinator, **rises**)" explicitly references the risen L4 combinator. The sibling See-also rows already link `../L4/` (e.g. line 140 `eigsolve` is the concept page, but the case dispositions all narrate the rise). Redirected to L4.
- No L1 cap reference is *kept* in these two spots: in both, the surrounding prose means the risen L4 feature surface, not the L1 pure-function cap. The L1 cap (`L1/fe_assemble.md`) remains the firm lower home and is still reachable via the L4 entry's own lowering chain; this page's two references were both about the rise.
- Layer-definition discipline honored: this is a concept page (not a lowering theme), so no high→low direction concern; the edits only re-point an existing forward-reference to its now-on-disk firm target.

## Supporting evidence
- `book/src/L4/fe_assemble.md:167-171` — `## Status: firm` (firm since cycle-068); confirms the upgrade target exists on disk.
- `book/src/L4/fe_assemble.md:169` — "the canonical L4 assemble-construction shape" / combinator-rises disposition; backs the "risen assemble combinator" wording.
- `book/src/L4/fe_assemble.md` frontmatter `consumes:` — names `book/src/concepts/black-box-vs-accelerated-kernels.md` "case 1" as a consumer, i.e. the link relationship is already declared from the L4 side; this pass completes the back-link.
- `book/src/concepts/black-box-vs-accelerated-kernels.md:60-75` — sibling black-box kernels (`eigsolve`, `ksp_solve`, `fold_solve`) all live-link `../L4/`, establishing the page convention that risen case-1 kernels point at L4.

## Open questions / caveats
- None. The firmed-up `L4/fe_assemble` signature does not contradict anything the concept page assumed (the page already described it as "the assemble fold (combinator, rises)", which is exactly the firm L4 combinator shape). Pure rewrite; no abstractor reread needed.
