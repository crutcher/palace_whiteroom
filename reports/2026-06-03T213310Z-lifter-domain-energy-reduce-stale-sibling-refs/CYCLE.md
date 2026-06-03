---
agent: lifter
invoked_at: 2026-06-03T213310Z
scope: L4>L4 sibling-maturity reference hygiene — domain_energy_reduce stale sibling refs
status: pending
inputs:
  - book/src/L4/domain_energy_reduce.md
  - book/src/L4/eigenfreq_qfactor_reduce.md (firm c082 — sibling whose stale rough-in refs are corrected)
  - book/src/L4/sparameter_reduce.md (firm c083 — sibling; verified no stale maturity ref)
  - book/src/L4/gram_reduce.md (rough-in (test-coverage-bounded) — sibling; refs verified accurate, untouched)
integrated_at: 2026-06-03T214250Z
integration_commit: 9b9d27d
integration_notes: |
  Applied clean by integrator-per-report (1 staging row, status applied). 2 surgical prose edits to
  book/src/L4/domain_energy_reduce.md — sibling-verb maturity-reference correction (eigenfreq_qfactor_reduce
  (rough-in)→(firm, c082)) + §Status gating-logic re-narration. ZERO status/count/citation change
  (domain_energy_reduce's own ## Status `rough-in` + frontmatter firmness UNCHANGED). All gate hits 0;
  retroactive-budget 0; citecheck 5 ok / 0 failing. Build (cargo make book) exit 0, no repair, no stub.
---

# CYCLE: Re-anchor domain_energy_reduce stale sibling-verb maturity refs

## Summary
Pure-rewriting hygiene pass on `book/src/L4/domain_energy_reduce.md`. Cycles 082/083 promoted two sibling
reduce verbs to `firm` (`eigenfreq_qfactor_reduce` c082, `sparameter_reduce` c083). This chapter — itself
correctly still `rough-in` — carried stale references describing `eigenfreq_qfactor_reduce` as `rough-in`
at two loci. The load-bearing one (line ~290) was not merely stale wording but factually wrong about the
gating logic: it asserted the now-firm sibling is "also rough-in for the same primitive-maturity +
no-dedicated-test reasons," which mis-states WHY `domain_energy_reduce` itself stays rough-in. Two surgical
prose edits correct (a) the sibling-list maturity parenthetical (line 212) and (b) the §Status contrast
parenthetical (line 290), re-narrating the latter so `domain_energy_reduce`'s rough-in status is correctly
attributed to its OWN folded `matrix-weighted-norm` energy-form (rough-in test-coverage-bounded; the
√-entry-point gate) — and the now-firm sibling becomes the *contrast* showing the firm-on-positive-structure
escape applies when both folded L1 primitives are firm (which `domain_energy_reduce` lacks). `domain_energy_reduce`'s
OWN `## Status` token stays `rough-in` (UNCHANGED). No L0 citations re-anchored (no `path:lo-hi` pinpoint touched).
`sparameter_reduce` and `gram_reduce` references verified accurate and left untouched.

## Proposed changes

```edit:book/src/L4/domain_energy_reduce.md
[old]: - [`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md) (rough-in) — the per-MODE scalar-table
  reduction; `domain_energy_reduce` is the per-DOMAIN sibling (same rank-1 scalar-table shape, different
  family index: mode vs domain). Together they are the two rank-1 scalar-table members of the
  algebra-of-folds.
[new]: - [`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md) (firm, c082) — the per-MODE scalar-table
  reduction; `domain_energy_reduce` is the per-DOMAIN sibling (same rank-1 scalar-table shape, different
  family index: mode vs domain). Together they are the two rank-1 scalar-table members of the
  algebra-of-folds. (The sibling reached `firm` because BOTH its folded primitives have firm L1 homes —
  `eigenvalue-untransform` c080 + `participation_ratio` c077 — so the firm-on-positive-structure escape
  applies to it; `domain_energy_reduce` does NOT yet share that property, see §Status.)
```

```edit:book/src/L4/domain_energy_reduce.md
[old]: Promotion route: (a) firm up the folded domain-restricted [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)
energy form, AND (b) a dedicated per-domain energy-participation test OR a lowering-verifier pass raising
the map-law confidence to `inner_product`-equivalent (the batch-24 meta-phase ruled the 2nd gate is
dischargeable in write-scope by a `find-tests-for-region` pass CITING the existing
`test-domainpostoperator.cpp` postprocess coverage). (Contrast the per-mode sibling
[`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md), also `rough-in` for the same
primitive-maturity + no-dedicated-test reasons.)
[new]: Promotion route: (a) firm up the folded domain-restricted [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)
energy form, AND (b) a dedicated per-domain energy-participation test OR a lowering-verifier pass raising
the map-law confidence to `inner_product`-equivalent (the batch-24 meta-phase ruled the 2nd gate is
dischargeable in write-scope by a `find-tests-for-region` pass CITING the existing
`test-domainpostoperator.cpp` postprocess coverage). (Contrast the per-mode sibling
[`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md), now `firm` (c082): it cleared the
firm-on-positive-structure escape precisely because BOTH its folded primitives have firm L1 homes —
[`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) (c080) and the firm
[`participation_ratio`](../L1/participation_ratio.md) (c077). `domain_energy_reduce` stays `rough-in`
because its OWN per-domain numerator — the folded domain-restricted
[`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) energy form — is itself `rough-in
(test-coverage-bounded)` at the √-overload entry point (gate (a) above), so the same escape does NOT yet
apply here; the firm sibling is the contrast that shows what clearing gate (a) would buy, NOT a peer at
the same maturity.)
```

## Discipline notes
- **Pure rewriting / bounded prose-correction, both evidenced and recorded.** Two changes:
  - **Line 212 maturity token** — `(rough-in)` → `(firm, c082)`. Stale-token correction; the on-disk
    sibling status is `firmness: firm` (`book/src/L4/eigenfreq_qfactor_reduce.md:4`). A trailing
    explanatory clause was added to keep the now-firm contrast self-consistent with the §Status edit.
  - **Line 290 factual correction** — the parenthetical asserted the now-firm sibling is "also `rough-in`
    for the same primitive-maturity + no-dedicated-test reasons." This is factually wrong on current
    on-disk maturity AND wrong about the gating logic: it implied `domain_energy_reduce`'s rough-in status
    is shared/symmetric with the sibling's, when in fact the sibling cleared the firm-on-positive-structure
    escape (its two folded primitives `eigenvalue-untransform` c080 + `participation_ratio` c077 are both
    firm L1 — `book/src/L4/eigenfreq_qfactor_reduce.md:185-211`), whereas `domain_energy_reduce`'s folded
    numerator `matrix-weighted-norm` is still `rough-in (test-coverage-bounded)` (the √-entry-point gate,
    already correctly stated in this chapter's frontmatter `:7` and §Status point 1 `:274-278`). The
    re-narration attributes `domain_energy_reduce`'s rough-in to its OWN folded-primitive gate (per the
    dispatch's critical scope bound) and repositions the sibling as the *contrast*, consistent with the
    §Status point-1 logic already on-disk.
- **Supporting citation for the correction:** `book/src/L4/eigenfreq_qfactor_reduce.md:4` (firmness: firm),
  `:185-211` (the firm-on-positive-structure reasoning naming both firm L1 folded primitives —
  eigenvalue-untransform c080 + participation_ratio c077). These are artifact-internal status reads, not L0
  source re-anchors.
- **CRITICAL SCOPE BOUND honored:** `domain_energy_reduce`'s own `## Status` token (`:268` `rough-in`) and
  frontmatter `firmness: rough-in` (`:4`) are UNCHANGED — its folded `matrix-weighted-norm`-squared energy
  form is still rough-in, so the firm-on-positive-structure escape does not apply to it. No promotion.
- **No L0 citation re-anchored.** No `path:lo-hi` pinpoint was touched; both edits are artifact-internal
  prose about sibling-chapter maturity. citecheck `--anchor` not invoked because no new/changed L0 pinpoint
  citation is emitted (the only line-number references in the edited spans — `c080`/`c077`/`c082` cycle
  tags — are cross-cycle provenance, not source ranges).
- **No index-table status-cell update needed.** This pass flips NO `## Status` line, so the index-cell
  promotion-time guard (friction-ledger `index-table-status-cell-drifts-when-theme-file-promoted`) does not
  fire — `domain_energy_reduce` stays `rough-in` in both the chapter and any index cell.

## Supporting evidence
- `book/src/L4/eigenfreq_qfactor_reduce.md:4` — `firmness: firm` (c082 promotion).
- `book/src/L4/eigenfreq_qfactor_reduce.md:185-211` — firm-on-positive-structure reasoning; both folded L1
  primitives (eigenvalue-untransform c080, participation_ratio c077) firm.
- `book/src/L4/sparameter_reduce.md:4` — `firmness: firm` (c083); verified the only `domain_energy_reduce`
  reference to it (line 298, "single-witness-driven-by-design scope") is a scope-SHAPE claim, NOT a
  maturity claim, so it is accurate and untouched.
- `book/src/L4/gram_reduce.md:4` — `firmness: rough-in (test-coverage-bounded)`; the chapter's gram_reduce
  references (lines 31, 132, 178-180, 217) are rank-2/over-unification-guard shape claims, accurate,
  untouched.
- `book/src/L4/domain_energy_reduce.md:7, :274-278` — the chapter's OWN already-correct statement that its
  rough-in maturity is inherited from the folded `matrix-weighted-norm`; the line-290 re-narration is made
  consistent with this.

## Open questions / caveats
- None blocking. The two edits are a pure-rewriting + bounded factual-correction hygiene pass within the
  stated scope; no decomposition, signature, or structural change. The chapter's own gating narration
  (§Status points 1–2, the matrix-weighted-norm-inherited rough-in) was already correct and required no
  rework — only the sibling-contrast parenthetical was stale. No abstractor reread indicated.
- Minor watch (NOT actioned, out of scope): line 298 cites `sparameter_reduce` as the precedent for
  "single-witness-driven-by-design scope." `sparameter_reduce` is now firm (c083); its scope-design shape
  is unchanged by the promotion, so the analogy still holds. If a future pass wants the precedent to also
  read as firm, it could add a `(firm c083)` tag there, but the current text makes NO maturity claim about
  it so this is optional polish, not a correctness fix — left untouched to keep this pass minimal.
