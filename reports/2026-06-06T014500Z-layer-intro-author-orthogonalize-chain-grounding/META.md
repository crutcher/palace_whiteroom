---
verifies: ../CYCLE.md
critiqued_at: 2026-06-06T030000Z
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
  reachability: pass
repaired_at: 2026-06-06T033000Z
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
  reachability: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "orthogonalize lazy-tail chain grounding (frontmatter-only)"

## Critique

### Checks run

**citation-validity — warning.** The 4 L0 `cites-evidence` ranges on `L1/orthogonalize` were spot-checked against on-disk source (both `Read` and codemap `read_range`, which agree). All four are correct and in-range: `palace/linalg/orthog.hpp:41-53` = `OrthogonalizeColumnMGS` (name line at 41, per-`j` body `H[j]=dot_op(...); GlobalSum; w.Add` at 49-51, closing `}` at 53); `:57-74` = the `OrthogonalizeColumnCGS` non-refine pass (name at 57, early `m==0` return 62-65, batched local dots 66-69, `GlobalSum(m,H,comm)` at 70, batched `w.Add` 71-73, with `if(refine)` opening at 75); `:75-88` = the CGS2 refine block (`if(refine)` at 75, correction dots+`GlobalSum`+accumulate `H[j]+=dH[j]; w.Add(-dH[j],V[j])` at 77-87, refine-block `}` at 88, function `}` at 89); `palace/linalg/iterative.cpp:307-325` = `OrthogonalizeIteration` (template line at 307, `switch(type)` over MGS/CGS/CGS2 with CGS2 = `OrthogonalizeColumnCGS(...,true)`, closing `}` at 325). The `:307-325`-vs-body-`:308-325` one-line difference is genuine and faithfully justified (307 = `template<...>`, 308 = function-name line; the codemap confirms both). Path prefix `palace/linalg/...` is the established book convention (83 prior uses; codemap root drops the outer `palace/`). The single source-citation set is clean. **The warning is NOT a source-citation defect — it is a self-measurement claim in the report that the linter contradicts** (see Issue 1): the report's Summary and measurement table claim "STRONGER GARBAGE SIGNAL 26 → 23 (−3)", but independent reproduction shows the stronger-garbage `[GARBAGE*]` bucket holds at 26 → 26; the −3 came from the weaker `[garbage?]` (untyped-detritus) bucket. A claim asserted in the report that the evidence does not support is a citation-validity miss.

**surface-or-evidence — pass.** This is a graded-stack edge-typing dispatch (frontmatter-only; bodies firm since c019/c022 and untouched). It is pure evidence/edge backfill — no surface modification — which is allowed. The `L1/orthogonalize` `cites-evidence` edges resolve to real positive L0 sites (verified above); the `L2/orthogonalize` `depends-on` edges are real constituents of the chapter's own `project ▷ subtract` composition (body §Semantics :116-117: `project op.variant op.dot w V` = dot, `subtract w coeffs V` = axpy; §Dependencies :245-251 names exactly the three L1 slugs + the lowering theme). No record signature lacking a definition home. Pass.

**rotation-quality — pass (no-op for the kind).** No new algebraic/structural rotation is asserted; this dispatch types edges on already-firm chapters whose rotations were established at c019/c022. Not applicable to a frontmatter-only edge-typing report.

**variant-axis-coverage — pass.** The orthogonalize variant axis (MGS/CGS/CGS2 + the canonical/B-weighted `dot`-hook) is already fully covered in the firm chapter bodies (L1 §Semantics, L2 §Variant axes); this report adds no surface and introduces no hidden branch. Not applicable to the edge-typing scope.

**cross-reference-integrity — pass.** All 10 edge target slugs verified on disk: `L1/orthogonalize`, `L1/dot`, `L1/axpy`, `L2-L1/orthogonalize-composition-lowering`, `L1-L0/orthogonalize-mutation-rotation`, `concepts/orthogonalization`, `concepts/variant-absorption`, `concepts/sequential-obstruction` (L2 edges); plus `L3/orthogonalize`, `L3-L2/orthogonalize-variant-split` (referenced in the routed finding). The 4 L0 `cites-evidence` targets resolve to real source. All exist.

**edge-label-fidelity / well-foundedness — pass.** The `L2/orthogonalize` `depends-on` targets are real constituents (the body's `project`/`subtract` composition genuinely calls `dot`/`axpy`, and lifts the L1 leaf). Rank invariant holds: `L1/dot` carries `rank: firm`, `L1/axpy` carries `rank: firm` (confirmed it got the c110 frontmatter), `L1/orthogonalize` is made `firm` by this same report (well-founded on the rank-terminal positive L0 `cites-evidence`), and `L2-L1/orthogonalize-composition-lowering` is firm content (c022). `L2/orthogonalize` `firm` (rank 3) rests only on firm deps → firm→firm. Reproduced lint: `0 rank violation(s)` HELD before and after. The `lowers-to` edge directions are correct (L2→L2-L1, L1→L1-L0).

**plan-kind-consistency — pass.** Declared kind is a graded-stack edge-typing / grounding dispatch (frontmatter-only). Content matches: two from-scratch `edges:` blocks, a linter measurement, a routed finding. No firm/rough-in mismatch; both chapters were already firm and stay firm.

**skill-uptake-survey — pass (telemetry).** No dedicated edge-typing skill is implied beyond the `graded_stack_lint.py` tool invocation, which the report uses and documents. The faithful-edge-or-finding (§(g) GROUND-don't-remove) discipline is followed and cited. No missing skill reference.

**rank-invariant — pass.** Reproduced: `0 rank violation(s)` at baseline and after applying the proposed edits to a scratch copy. Every `depends-on` edge is firm→firm (L2/orthogonalize firm resting on L1/dot firm, L1/axpy firm, L1/orthogonalize firm, lowering theme firm; L1/orthogonalize firm resting on rank-terminal L0 source).

**reachability — pass (independently reproduced).** Applied both proposed edits to a scratch copy, ran `graded_stack_lint.py` (+ `--show-inbound`), reverted my two files (left D2's pre-existing working-tree modifications untouched; `git status` of my two files clean). Result: `reachable from roots: 119 → 122` (+3) exactly as claimed; `detritus 140 → 137` (−3). The 3 flipping nodes confirmed via `--show-inbound`: `L1/orthogonalize <- L2/orthogonalize`, `L2-L1/orthogonalize-composition-lowering <- L2/orthogonalize`, `L1-L0/orthogonalize-mutation-rotation <- L1/orthogonalize`. `L2/orthogonalize <- L3/orthogonalize, L4/krylov-step` (already reachable via L4). The routed-finding nodes stay garbage as predicted (`L3/orthogonalize` `[GARBAGE*]`, `L3-L2/orthogonalize-variant-split` `[garbage?]`). D2's parallel edits (`L1-L0/axpby-mutation-rotation.md`, `axpbypcz-mutation-rotation.md`) are reachability-neutral and on disjoint files — the +3 is isolated to D1. **Faithful-path-or-finding discipline confirmed correct:** the `l3-orthogonalize-sub-chain-no-faithful-reachable-depender` decline is correct behavior. The L3→L2 edge runs inbound to L2 (does not carry liveness up to L3); `L4/krylov-step` composes the L2 surface directly (L3/orthogonalize body §:76 confirms "The L2 krylov-step consumer absorbs"); an `L4→L3` edge would be unfaithful. Declining to force it is right, not a gap.

### Issues found

**Issue 1 (warning) — measurement mislabel: "STRONGER GARBAGE 26→23 (−3)" is not reproducible; the actual stronger-garbage count HOLDS at 26.** Location: `CYCLE.md` Summary (line 16 region implicitly) and the §"Linter measurement" table, line 177 (`STRONGER GARBAGE SIGNAL | 26 | 23 | −3`), and the §Open-questions reference to "8 of the 26 STRONGER-GARBAGE nodes". Independent reproduction (apply edits → `graded_stack_lint.py` → revert): the `[GARBAGE*]` "declares typed deps yet unreachable" bucket is **identical before and after my edits — 26 nodes both times** (full lists diffed, byte-identical). The three nodes this report grounds (`L1/orthogonalize`, `L2-L1/orthogonalize-composition-lowering`, `L1-L0/orthogonalize-mutation-rotation`) are at baseline classified `[garbage?]` — the **weaker** untyped-detritus signal — NOT `[GARBAGE*]`; they never transit the stronger-garbage bucket (untyped detritus → reachable directly). The real, correct deltas are `reachable +3 (119→122)` and `detritus −3 (140→137)`, both of which I confirm. Severity: low-to-moderate — the headline scientific result (+3 reachable, 0 rank violations) is correct and fully reproducible; only the attribution of the −3 to the stronger-garbage bucket is wrong. The mislabel matters because it overstates the "stronger garbage signal" progress (the report frames the grounding as clearing high-signal garbage when it actually cleared low-signal untyped-detritus) and the figure is propagated into the carried meta-phase OQ framing ("down to this sub-chain + the normalize/reciprocal chain" against the 26-node STRONGER-GARBAGE backlog). Repair: correct the table row to `STRONGER GARBAGE SIGNAL | 26 | 26 | HELD` and re-cast the −3 as a `[garbage?]`/detritus reduction (the existing `detritus 140 → 137 | −3` row is already correct and can carry the win); adjust the Summary/OQ prose accordingly. This is a measurement-fidelity edit, not a content defect.

**Issue 2 (informational, not blocking) — stale in-chapter body notes acknowledged but un-tracked beyond this report.** Location: `CYCLE.md` §Open-questions final paragraph; underlying `book/src/L1/orthogonalize.md` §:322-326 + §Dependencies :170-171 ("L1>L0 lowering theme not yet authored" / "forthcoming") and `book/src/L2/orthogonalize.md` §:275-279 ("forthcoming … does not yet exist"). The report correctly observes these are STALE (`L1-L0/orthogonalize-mutation-rotation.md` and `L2-L1/orthogonalize-composition-lowering.md` both exist on disk, verified) and correctly scopes the body edit out (frontmatter-only dispatch). No defect in this report — flagging only so the stale-body-note observation is not lost; it warrants a future body-refresh dispatch or an OQ entry, since the report routes the L3 finding to OQ but leaves the stale-note observation only in the report prose.

## Repair

### Fixes attempted

- **Finding (Issue 1, warning)**: measurement mislabel — CYCLE.md Summary + §"Linter measurement" table (line 177) + adjacent prose claim "STRONGER GARBAGE SIGNAL 26 → 23 (−3)", but the `[GARBAGE*]` stronger-garbage bucket HOLDS at 26 → 26; the reproducible −3 is in the weaker `[garbage?]` untyped-detritus bucket, and the correct deltas are reachable 119→122 (+3) / detritus 140→137 (−3).
  - **Decision**: repaired
  - **Action**: corrected the measurement table row (`STRONGER GARBAGE SIGNAL [GARBAGE*] | 26 | 26 | HELD`, with the explanation that the 3 grounded nodes were in the weaker `[garbage?]` bucket and transit `[garbage?]` → reachable directly) and the `detritus` row (now annotated as the `[garbage?]` flip); also corrected the Summary (CYCLE.md §Summary) to state the `[GARBAGE*]` bucket HOLDS at 26 and re-cast the win as +3 reachable / −3 detritus. (`CYCLE.md` §Summary + §"Linter measurement" table.) This is a pure wording/measurement-fidelity edit; the `edges:` proposed-change blocks were NOT touched.
  - **Checked, no edit needed**: the routed OQ `l3-orthogonalize-sub-chain-no-faithful-reachable-depender` in `scaffolding/open-questions.md` (line 1494ff) does not assert a "STRONGER GARBAGE −3"; it correctly reports "+3 → reachable 122" and correctly classifies `L3/orthogonalize` as `[GARBAGE*]` and `L3-L2/orthogonalize-variant-split` as `[garbage?]`. No misattribution there — left as-is. Likewise the CYCLE.md §Open-questions "8 of the 26 STRONGER-GARBAGE nodes" reference (normalize/reciprocal chain) keeps the count 26, which remains accurate since the bucket HOLDS — left as-is.

- **Finding (Issue 2, informational)**: stale in-chapter body notes, correctly scoped out by the report.
  - **Decision**: not-needed (the critic flagged it as no-defect/informational; no repair authority action required).

### Unrepairable findings

None. The single warning was a mechanical measurement-wording mislabel, fully within repair authority.

## Suggested resolution

`ready`. The headline result (+3 reachable, 0 rank violations, all 4 L0 ranges verified, all edges firm→firm) was reproduced clean by the critic; the only defect was the −3 bucket attribution, now corrected to `[GARBAGE*]` HOLDS 26 / detritus −3 / reachable +3. Integrator note for the batch-35 meta-phase: the STRONGER-GARBAGE `[GARBAGE*]` backlog is unchanged at 26 by this cycle (the orthogonalize chain cleared weaker `[garbage?]` detritus), so the routed OQ's "down to this sub-chain + the normalize/reciprocal chain" framing is read against an unchanged 26-node stronger-garbage count.
