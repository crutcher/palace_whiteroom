---
verifies: ../CYCLE.md
critiqued_at: 2026-06-06T00:00:00Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
  rank-invariant: pass
  reachability: warning
repaired_at: 2026-06-06T00:30:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
  rank-invariant: not-needed
  reachability: repaired
overall_status: ready
follow_up_agent: null
---

# META: verification of cycle-110 D2 — L1 BLAS-leaf typing (axpy family)

## Critique

### Checks run

**citation-validity** — `warning`. The 14 `cites-evidence` L0 ranges were all re-verified with
`citecheck --anchor` against on-disk `reference/palace/...`: every one returns `[ok]` with the
anchor literal (`AXPY`/`AXPBY`/`AXPBYPCZ`) inside range. The ranges transcribe each chapter's own
`## Evidence` section verbatim. The two `lowers-to` targets exist on disk. So the *pointers* are
all valid. The `warning` is for one **load-bearing numeric claim that is not citation-supported**:
the report's headline measurement `reachable 107→119 (−12 detritus)` is **not the delta produced by
D2's edits** — see the reachability check below. A reported metric is a claim and must be backed by
a reproducible measurement; this one is misattributed.

**surface-or-evidence** — `pass`. Frontmatter-only; no prose claim changed (verified: the `[old]`
anchors are the existing H1 + lede of each chapter, the `[new]` is the same text with a frontmatter
prepend). This is pure edge/rank typing of already-firm chapters, not a refinement of operator
surface, so the rotation_claim obligation does not attach. Record-definition sub-check: no new
signature-named record is introduced.

**rotation-quality** — `pass`. Not applicable to a frontmatter-typing dispatch; no algebraic /
structural rotation is asserted (the underlying L1 forms already exist and are unchanged).

**variant-axis-coverage** — `pass`. The element-type (real|complex) + scalar-promotion axes are
fully enumerated in the chapter bodies (unchanged); the typing dispatch introduces no new branch.
The `cites-evidence` edges in fact cover both the real and complex overloads + member decls for
each leaf.

**cross-reference-integrity** — `pass`. Every edge-target slug resolves to a real
`book/src/<slug>.md`: the `lowers-to` themes (`L1-L0/{axpby,axpbypcz}-mutation-rotation`), the four
`reference` siblings/concepts per leaf (`L1/{axpy,axpby,axpbypcz,scal}`, `L2/linear_combination`,
`concepts/{axpy,scalar-promotion}`), and the inbound consumers the `--show-inbound` table names
(`L2/{krylov-step,linear_combination,axpy,axpby,axpbypcz}`, `L1/{divfree-projector,eliminate_rhs}`)
all exist. The "axpby theme covers axpy as the β=1 specialisation" claim is supported by the theme
prose: `L1-L0/axpby-mutation-rotation.md` is titled "axpy-shaped vector updates," carries a
"Sub-pattern A — bare axpy" section, and links `L1/axpy`. The `scal`/`apply_linop`/
`set_subvector_zero` convention citation is accurate — `set_subvector_zero.md` is the correct
precedent for the `depends-on: cites-evidence`(→L0) form used here (scal/apply_linop carry only
`reference:` edges; the report names set_subvector_zero for the cites-evidence pattern, which is
right).

**edge-label-fidelity** — `pass`. The `lowers-to` edges are L1→(L1>L0) lowering-theme edges and the
prose of each leaf discusses exactly that lowering (each chapter's "L1 vs L0 distinction" + Semantics
sections route in-place mutation to the named theme). The `cites-evidence` edges point at the L0
source the chapter cites. Directions are consistent.

**plan-kind-consistency** — `pass`. Declared as a frontmatter-only graded-stack typing tranche;
content is exactly frontmatter prepends. No mis-classification.

**skill-uptake-survey** — `pass`. The report invokes `citecheck --anchor` for citation provenance
and the graded-stack linter (`--show-inbound`, `--json`) for measurement; appropriate tooling for
the shape.

**rank-invariant (graded-stack §9)** — `pass`. `rank: firm` on each leaf is well-founded under the
firm-on-positive-structure escape: each chapter's `## Status` first line reads `` `firm` `` with a
fully-specified positive L0 source and syntactic-identity (standard BLAS-1) laws, and the blocking
`depends-on` edges are rank-terminal POSITIVE L0 source ranges (cites-evidence) — no sub-firm
`depends-on` dep. The `lowers-to` edges target `typed-no-rank` lowering themes (warn-not-fail; the
linter `continue`s, no violation). Independently reproduced: with D2's edits applied alone,
`RANK VIOLATIONS: none` and `rank_violations` HOLDS at 0. The inbound firm consumers
(`L2/krylov-step`, `L2/linear_combination`, `L2/{axpy,axpby,axpbypcz}`) now rest firm→firm instead
of firm→prose-fallback-firm; no regression.

**reachability (graded-stack §10)** — `warning`. The honest OQ-premise correction is **accurate
and verified**: the linter's prose-`## Status` rank fallback (`graded_stack_lint.py:425-437`,
priority `rank:` > `firmness:` > feature `status:` > prose `## Status`, via `read_status_line`
matching a token prefix) already ranked all three chapters `firm` from their `` `firm` `` prose
status lines, so `untyped` correctly HOLDS at 60 (the predicted 60→57 was wrong) and the firm
histogram HOLDS. That part is exemplary. **However, the +12 reachability attribution is wrong.** I
reproduced D2's three edits ALONE on a clean tree (clean baseline confirmed: reachable 107,
detritus 152, matching the report's BASELINE column) and ran the linter:

- **D2 alone: reachable 107→109 (+2), detritus 152→150 (−2).** The ONLY two nodes D2 alone pulls
  out of detritus are `L1-L0/axpby-mutation-rotation` and `L1-L0/axpbypcz-mutation-rotation` —
  exactly the two `lowers-to` targets.
- The other ten nodes the report claims D2 rescued — `L2/inner_product`,
  `L2-L1/inner-product-fold-specialization`, `L2/orthogonalize`,
  `L3/{apply_linop,dot,inner_product,nrm2}`, `L4/{dot,inner_product,nrm2}` — are **STILL detritus
  under D2 alone** (verified via `--json` detritus-set membership). Frontmatter typing of the axpy
  *leaves* cannot rescue the dot/nrm2/inner_product reduce chain, because nothing in that chain
  points INTO the axpy family; the leaves are downstream of L2 consumers, not the reduce verbs.

The +12/−12 the report measured is the **cumulative D1+D2** effect (D1 = the parallel reduce-cohort
grounding via krylov-step edges, which rescues the reduce chain). The report's own verification ran
the linter with D1's `book/src/L4/krylov-step.md` modification present in the working tree (it
acknowledges that file as D1's, but did not isolate it before measuring reachability), so the
attribution leaked D1's cascade into D2's column. This is a measurement-provenance defect, not a
content defect — the edits themselves are correct and the true D2 contribution (+2) is real.

### Issues found

1. **Misattributed reachability metric (+12 should be +2) — `CYCLE.md` §"Before / after linter
   numbers" + §"Nodes that LEFT detritus".** Severity: medium. The report attributes `reachable
   107→119 (−12 detritus)` to D2's axpy-family typing. Independent reproduction of D2's edits ALONE
   on a clean tree gives **reachable 107→109 (+2), detritus −2**; the only D2-rescued nodes are the
   two `lowers-to` themes `L1-L0/{axpby,axpbypcz}-mutation-rotation`. The ten reduce-chain nodes
   (`L2/inner_product`, `L2/orthogonalize`, `L2-L1/inner-product-fold-specialization`,
   `L3/{apply_linop,dot,inner_product,nrm2}`, `L4/{dot,inner_product,nrm2}`) listed as
   "newly reachable" remain detritus under D2 alone — they are D1's (reduce-cohort krylov-step
   grounding) cascade, which was present in the working tree (`book/src/L4/krylov-step.md`,
   D1's write) when the report measured. The integrator should **re-measure the true cumulative
   reachability at apply time** (after BOTH D1 and D2 land) rather than trust D2's reported +12, and
   should record D2's standalone contribution as +2. (The report's write-set-hygiene note is
   otherwise correct: D2's three files revert clean; only krylov-step — D1's — was modified.)

2. **`--show-inbound` quotation is accurate but supports the +2, not the +12 — `CYCLE.md` lines
   71-82.** Severity: low (corroborating, not a separate defect). The quoted inbound tables for the
   two themes and the axpy family reproduce exactly. They confirm the rescue of the two themes
   (+2) and the firm→firm inbound rests; they do NOT evidence the reduce-chain rescue the report
   bundles into the same paragraph. The prose conflates the two.

(No issue with the rank typing, the citation pointers, the OQ-premise/untyped-HOLDS-60 correction,
or the cross-references — those are all correct and well-evidenced. The book working tree was left
clean after reproduction; only `scaffolding/priorities.md` and the untracked report dirs remain,
none of which are mine.)

## Repair

### Fixes attempted

- **Finding**: Misattributed reachability metric — the report headlines `reachable 107→119
  (+12, −12 detritus)` and lists ten reduce-chain nodes as D2-rescued, but D2's edits ALONE on
  a clean tree give `reachable 107→109 (+2), detritus −2`, rescuing ONLY the two `lowers-to`
  themes `L1-L0/{axpby,axpbypcz}-mutation-rotation`; the ten reduce-chain nodes are D1's
  krylov-step cascade that contaminated D2's reading. (`reachability` warning + the
  `citation-validity` warning, which the critic flagged solely for this same unbacked numeric
  claim.)
- **Decision**: repaired
- **Action**: Corrected the reachability attribution in three places in CYCLE.md, all prose /
  table only — NO `edges:` proposed-change block touched:
  - §"Correction to the OQ premise" — narrowed the "whole BLAS-leaf lowering chain" claim to
    just the two themes; added a `[repairer correction, c110]` note stating D2's true
    standalone +2 and naming the D1 contamination.
  - §"Before / after linter numbers" — replaced the +12/−12 table row with the isolated
    D2-alone +2/−2, replaced the 12-node "left detritus" list with the correct 2-node list,
    added a `[repairer correction, c110]` note explaining why the ten reduce-chain nodes are
    D1's (the leaves are downstream of L2 consumers; nothing in the reduce chain points into
    the axpy family), and added the one-line note that the integrator must re-measure the true
    CUMULATIVE reachable at apply time (not an arithmetic D1+D2 sum).
  - §"Open questions / caveats" — corrected the embedded +12/−12 restatement to D2-alone +2/−2
    with a back-pointer to the correction.
- **Rationale for in-scope**: This is a measurement-attribution wording fix on a
  pre-integration report. The edges are all verified-correct (critic: 14/14 L0 ranges `[ok]`,
  every edge-target slug exists, `rank: firm` well-founded, `rank_violations` HELD 0); only the
  reported reachability number/attribution was wrong, and the correct standalone value (+2,
  rescuing the two named themes) was supplied by the critic's independent reproduction. No
  content authored, no claim invented — purely transcribing the verified correct measurement.

### Unrepairable findings

None.

## Suggested resolution

`ready`. Notes for the integrator:
- The corrected CYCLE.md records D2's **standalone** reachability contribution as **+2**
  (rescuing `L1-L0/axpby-mutation-rotation` + `L1-L0/axpbypcz-mutation-rotation`). The
  `reachable 107→119` headline is GONE — do not carry it forward.
- **Re-measure the true CUMULATIVE reachable at apply time** (after both D1 and D2 land) by
  running `tools/graded-stack-lint/graded_stack_lint.py` on the post-apply tree; it is not the
  arithmetic sum of the two columns (cohorts may overlap).
- The three `edges:` proposed-change blocks are verified-correct and untouched — apply as-is.
- The follow-up OQ `l1-l0-axpy-family-themes-need-scheme-frontmatter` (the two `lowers-to`
  target themes are still pre-scheme / `typed-no-rank`) is correct and stands.
