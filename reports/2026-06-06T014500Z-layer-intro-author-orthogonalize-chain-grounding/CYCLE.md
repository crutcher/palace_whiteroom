---
agent: layer-intro-author
invoked_at: 2026-06-06T014500Z
scope: graded-stack edge-typing — the orthogonalize lazy-tail chain grounding (D1, cycle-111, THE LEAD; §(g) GROUND-don't-remove)
status: pending
integrated_at: 2026-06-06T021500Z
integration_commit: 9e95b1e
integration_notes: "cycle-111 D1 (THE LEAD), report 1 of 2. Applied verbatim per the 2 ## Proposed changes anchor-prepend blocks — from-scratch edges: blocks on book/src/L2/orthogonalize.md + book/src/L1/orthogonalize.md (both had a BARE H1, zero pre-existing frontmatter). Reachable 119→122 (+3: L1/orthogonalize, L2-L1/orthogonalize-composition-lowering, L1-L0/orthogonalize-mutation-rotation flip in); detritus 140→137; STRONGER GARBAGE SIGNAL HOLDS 26; rank_violations HELD 0; untyped HELD 60. All per-report gates PASS/N/A. Repairer fixed one low-severity garbage-bucket-wording prose warning (edges: blocks untouched). cargo make book EXIT 0, linkcheck2 clean. OQ l3-orthogonalize-sub-chain-no-faithful-reachable-depender confirmed at open-questions.md:1494 (no duplicate). Batch-35 BATCH-CLOSING cycle."
---

# CYCLE: orthogonalize lazy-tail chain grounding (frontmatter-only)

## Summary

THE LEAD of the batch-closing cycle-111: ground the orthogonalize lazy-tail chain by typing
from-scratch `edges:` frontmatter blocks on two firm chapters that carry NO frontmatter
(`L2/orthogonalize`, `L1/orthogonalize`). This flips **+3 reachable** (119 → 122) and clears
**−3 detritus** (140 → 137); the **STRONGER GARBAGE SIGNAL `[GARBAGE*]` bucket HOLDS at 26** —
the three grounded nodes were in the WEAKER `[garbage?]` untyped-detritus bucket at baseline,
not the stronger-garbage bucket, so they transit `[garbage?]` → reachable directly. The typed
edges carry liveness from the already-root-reachable `L2/orthogonalize` (reached by
`L4/krylov-step →composes→ L2/orthogonalize` since c110 D1) down into three firm-content nodes
that were GC-garbage only because the edge into them was un-typed:

- `L1/orthogonalize` (the firm L1 leaf `L2/orthogonalize` lifts),
- `L2-L1/orthogonalize-composition-lowering` (the firm L2>L1 lowering theme, content firm c022),
- `L1-L0/orthogonalize-mutation-rotation` (the firm L1>L0 mutation-rotation home — its OQ
  saying "un-authored" is STALE; the file is on disk).

This is **§(g) GROUND-don't-remove** applied: every edge is a faithful, honestly-classified,
citation-grounded `depends-on` / `lowers-to` / `cites-evidence` into the reachable chain so
liveness propagates — no node removed, no edge forced.

**FRONTMATTER-ONLY.** Chapter bodies are firm since c019/c022 and were NOT touched (verified
`git status book/` clean after apply→lint→revert). All edits are emitted below as
proposed-changes; `book/` is clean.

**ROUTED AS A FINDING (NOT forced):** the L3 orthogonalize sub-chain (`L3/orthogonalize` +
`L3-L2/orthogonalize-variant-split`) has no faithful reachable depender and stays detritus —
see `## Open questions`. An `L4/krylov-step → L3/orthogonalize` edge would be UNFAITHFUL
(krylov-step composes the L2 surface directly; there is no L4 orthogonalize op).

## Verification of each typed relationship (read from chapter prose / L0 source BEFORE typing)

### (a) `L2/orthogonalize` — depends-on targets
- `L1/orthogonalize` — the firm L1 leaf this composition lifts. Body §:3-4 ("it lifts the firm
  L1 leaf [`orthogonalize`]"), §Dependencies :245-247 ("L1 leaf it lifts: `orthogonalize`
  (firm, cycle-012)"). On-disk `L1/orthogonalize.md` `## Status` (:219 pre-edit) = `firm`. ✓
- `L1/dot` — the `project` stage inner product `coeffs[j] = op.dot(w_eff(j), V[j])`. Body
  §Semantics :116 (`let coeffs = project op.variant op.dot w V`), §Dependencies :248-250
  ("[`dot`] (the `project` stage's inner product …)"). `L1/dot.md` on disk; firm. ✓
- `L1/axpy` — the `subtract` stage rank-1 update `w ← w − coeffs[j]·V[j]` = `axpy(...)`. Body
  §Semantics :117 (`let residual = subtract w coeffs V`), §Dependencies :250-251
  ("[`axpy`] (the `subtract` stage's rank-1 update … = `axpy(-coeffs[j], V[j], w)`)"). `L1/axpy.md`
  on disk; firm. ✓
- `L2-L1/orthogonalize-composition-lowering` (`kind: lowers-to`) — the firm L2>L1 lowering theme
  this named composition lowers through. Body §Dependencies :275-279 (the "L2>L1 lowering theme"
  paragraph names exactly this slug). File on disk (`32758` bytes, content firm c022). Mirrors
  `L2/krylov-step → L2-L1/krylov-step-kernel-defusion`. ✓
- reference: `concepts/orthogonalization` (:46-47, :259), `concepts/variant-absorption`
  (:50-51, :261-262), `concepts/sequential-obstruction` (:48, :263-264) — copied from body
  prose, NOT re-derived. (NB: `concepts/orthogonalization`'s coefficient/normalisation
  boundary is the c-019 known drift the L1 body flags as authoritative-here; reference edge is
  navigational, so no rank impact.)

### (b) `L1/orthogonalize` — depends-on targets (cites-evidence L0, self-verified on-disk this dispatch)
- `palace/linalg/orthog.hpp:41-53` — `OrthogonalizeColumnMGS`. Verified on-disk: function-name
  line `inline void OrthogonalizeColumnMGS(...)` at **41**, per-`j` body
  `H[j] = dot_op(w, V[j]); Mpi::GlobalSum(1, &H[j], comm); w.Add(-H[j], V[j])` at 49-51,
  closing brace at **53**. ✓ (matches chapter Evidence :255-259)
- `palace/linalg/orthog.hpp:57-74` — `OrthogonalizeColumnCGS` (the CGS pass). Verified on-disk:
  name line at **57**, empty-basis early return `if (m == 0) return` at 62-65, batched local
  dots 66-69, `Mpi::GlobalSum(m, H, comm)` at 70, batched `w.Add`s 71-73, closing the CGS pass
  before the `if (refine)` block at **74-75**. The `:57-74` range = the CGS (non-refine) pass. ✓
- `palace/linalg/orthog.hpp:75-88` — the CGS2 `refine` block. Verified on-disk: `if (refine)`
  at **75**, `dH` correction dots + `Mpi::GlobalSum(m, dH.data(), comm)` + accumulate
  `H[j] += dH[j]; w.Add(-dH[j], V[j])` at 77-87, the refine block closing brace at **88**
  (function's own closing `}` at 89). The `:75-88` range = the CGS2 second-pass refine block. ✓
- `palace/linalg/iterative.cpp:307-325` — `OrthogonalizeIteration` runtime dispatch. Verified
  on-disk: `template <typename VecType, typename ScalarType>` at **307**, function body
  `switch (type)` over `MGS / CGS / CGS2` (CGS2 = `OrthogonalizeColumnCGS(..., true)`) at
  313-324, closing brace at **325**. ✓ (chapter Evidence cites `:308-325` from the function-name
  line; `:307-325` includes the `template<>` line — both faithful, I cite `:307-325` to capture
  the full template decl, per the plan's per-node table)
- `L1-L0/orthogonalize-mutation-rotation` (`kind: lowers-to`) — the firm L1>L0 mutation-rotation
  home (in-place `w` overwrite + raw-pointer `H` write + per-variant collective shape). File on
  disk (`17462` bytes; the OQ saying "un-authored" / the body §:322-326 "not yet authored" note
  are STALE — the theme file exists). Body §Dependencies :170-171 names the slug. ✓
- reference: `L1/dot` (:163), `L1/axpy` (:165), `concepts/orthogonalization` (:35),
  `concepts/sequential-obstruction` (:36-37) — siblings/concepts the body cites.

## Proposed changes

```edit:book/src/L2/orthogonalize.md
[old]:
# orthogonalize

The L2 first-class composition naming the Gram-Schmidt **orthogonalize-against-basis**
[new]:
---
layer: L2
operator: orthogonalize
# Graded-stack scheme (authored from scratch, batch-35 c111; mirrors the c109 L2/krylov-step
# from-scratch authoring). This firm L2 named composition (`project ▷ subtract`) rests on the
# firm L1 leaf it lifts (`L1/orthogonalize`) plus the two firm L1 primitives its composition
# stages genuinely call (`L1/dot` for `project`, `L1/axpy` for `subtract`; body §:116-131,
# §Dependencies :245-251) — all depends-on. AND it lowers through the firm L2>L1 lowering theme
# `orthogonalize-composition-lowering` (lowers-to depends-on; mirrors L2/krylov-step →
# L2-L1/krylov-step-kernel-defusion). This node firm (rank 3); all three L1 depends-on targets
# carry rank: firm, the lowering theme is firm content (c022) — rank invariant holds firm→firm.
rank: firm
edges:
  depends-on:
    - L1/orthogonalize
    - L1/dot
    - L1/axpy
    - target: L2-L1/orthogonalize-composition-lowering
      kind: lowers-to             # the L2>L1 lowering theme this named composition lowers through
  reference:
    - concepts/orthogonalization
    - concepts/variant-absorption
    - concepts/sequential-obstruction
---

# orthogonalize

The L2 first-class composition naming the Gram-Schmidt **orthogonalize-against-basis**
```

```edit:book/src/L1/orthogonalize.md
[old]:
# orthogonalize

Mutation-lifted Gram-Schmidt orthogonalisation: given a stored basis `V[0..m-1]` and a
[new]:
---
layer: L1
operator: orthogonalize
# Graded-stack scheme (cycle-111, D1): firm L1 Gram-Schmidt leaf — the L0 implementation is
# read in full (header-only inline `orthog.hpp:18-90`) and the laws are standard Gram-Schmidt
# facts modulo recorded FP caveats (the firm-on-positive-structure escape; matches the BLAS-1
# floor `dot`/`nrm2`/`axpy`/`scal`). The blocking depends-on is the rank-terminal POSITIVE L0
# SOURCE (cites-evidence) — the three Gram-Schmidt kernel bodies + the runtime dispatch wrapper
# — which is what makes the `firm` rank well-founded. The lowers-to edge points at the firm
# L1>L0 mutation-rotation theme (the in-place `w` overwrite + raw-pointer `H` write home).
rank: firm
edges:
  depends-on:
    - target: palace/linalg/orthog.hpp:41-53
      kind: cites-evidence        # OrthogonalizeColumnMGS — per-j [dot, axpy] sequential body
    - target: palace/linalg/orthog.hpp:57-74
      kind: cites-evidence        # OrthogonalizeColumnCGS — batched dots, GlobalSum(m), batched w.Add
    - target: palace/linalg/orthog.hpp:75-88
      kind: cites-evidence        # CGS2 refine block — second CGS pass accumulating H[j] += dH[j]
    - target: palace/linalg/iterative.cpp:307-325
      kind: cites-evidence        # OrthogonalizeIteration — runtime MGS/CGS/CGS2 dispatch wrapper
    - target: L1-L0/orthogonalize-mutation-rotation
      kind: lowers-to             # the L1>L0 mutation-rotation home (in-place w + raw-pointer H)
  reference:
    - L1/dot
    - L1/axpy
    - concepts/orthogonalization
    - concepts/sequential-obstruction
---

# orthogonalize

Mutation-lifted Gram-Schmidt orthogonalisation: given a stored basis `V[0..m-1]` and a
```

## Linter measurement (apply → lint → revert, on a clean tree; isolated to my disjoint write-set)

My write-set (`book/src/L2/orthogonalize.md` + `book/src/L1/orthogonalize.md`) is disjoint from
D2's (`book/src/L1-L0/axpb*-mutation-rotation.md`). `git status --short book/` showed exactly my
two files modified when I linted — NO D2 contamination — so the delta below is my isolated +3.

| metric | before (clean `eaca075`) | after (my 2 edits) | delta |
|---|---|---|---|
| reachable from roots | 119 | **122** | **+3** ✓ (predicted +3) |
| RANK VIOLATIONS | 0 | **0** | HELD ✓ |
| untyped (WARNING) | 60 | 60 | HELD (both nodes already non-untyped via `## Status`; the win is Axis-2 reachability) |
| detritus | 140 | 137 | −3 (the three orthogonalize-chain nodes flip out of `[garbage?]`) |
| STRONGER GARBAGE SIGNAL `[GARBAGE*]` | 26 | 26 | HELD (the 3 grounded nodes were in the WEAKER `[garbage?]` bucket at baseline, not `[GARBAGE*]`; they transit `[garbage?]` → reachable directly) |

**The 3 nodes that flipped reachable** (confirmed via `--show-inbound`):
- `L1/orthogonalize` ` <- L2/orthogonalize` (+1)
- `L2-L1/orthogonalize-composition-lowering` ` <- L2/orthogonalize` (+1)
- `L1-L0/orthogonalize-mutation-rotation` ` <- L1/orthogonalize` (+1)

`L2/orthogonalize` itself was already reachable (` <- L3/orthogonalize, L4/krylov-step`) — the
edit gives it its typed block so it can carry liveness onward. The two routed-finding nodes
stayed garbage as expected: `L3/orthogonalize` `[GARBAGE*]` (deps `L2/orthogonalize ×2`, but
that is L3→L2, inbound TO L2, so no upward liveness), `L3-L2/orthogonalize-variant-split`
`[garbage?]`.

After measurement I reverted both files; **`git status book/` is clean** (verified).

## Supporting evidence
- L2 chapter prose: `book/src/L2/orthogonalize.md` §:3-14 (lifts L1 leaf + dot/axpy constituents),
  §Semantics :112-119 (`project`/`subtract` composition), §Dependencies :241-279 (the firm L1
  leaf + dot + axpy + the named L2>L1 lowering theme).
- L1 chapter prose: `book/src/L1/orthogonalize.md` §Context :11-18, §Dependencies :161-173
  (dot/axpy leaves; L1>L0 theme), §Evidence :247-295, §Status :219-227 (firm).
- L0 source, self-verified on-disk this dispatch: `palace/linalg/orthog.hpp:41-53` (MGS),
  `:57-74` (CGS pass), `:75-88` (CGS2 refine block), `palace/linalg/iterative.cpp:307-325`
  (`OrthogonalizeIteration` dispatch).
- Templates followed: `book/src/L2/krylov-step.md` (c109 from-scratch L2 typed block, the
  `depends-on` L1-leaves + `lowers-to` kernel-defusion shape), `book/src/L1/axpy.md` (c110
  from-scratch L1 leaf typed block, the `cites-evidence` L0 + `lowers-to` L1>L0-theme shape).
- Target-file existence verified: `L2-L1/orthogonalize-composition-lowering.md`,
  `L1-L0/orthogonalize-mutation-rotation.md`, `L3/orthogonalize.md`,
  `L3-L2/orthogonalize-variant-split.md`, `L1/dot.md`, `L1/axpy.md` all on disk.

## Open questions / caveats

**Routed finding (the §(g) faithful-edge-or-finding disposition; NOT forced this cycle).**
Appended to `scaffolding/open-questions.md` (append-only authority) as OQ
**`l3-orthogonalize-sub-chain-no-faithful-reachable-depender`**:

- The L3 orthogonalize sub-chain `L3/orthogonalize` (`[GARBAGE*]`, deps `L2/orthogonalize ×2`)
  + `L3-L2/orthogonalize-variant-split` (`[garbage?]`) **stays detritus** after my +3 grounding.
- **No faithful reachable depender exists.** The edge runs `L3/orthogonalize → L2/orthogonalize`
  (L3 depends-on L2), so grounding L2 does NOT carry liveness UP to L3. The only root-reachable
  consumer of the orthogonalize family — `L4/krylov-step` — deliberately composes
  `L2/orthogonalize` DIRECTLY (there is no L4 orthogonalize op). An `L4/krylov-step →
  L3/orthogonalize` edge would be UNFAITHFUL (the over-edge §(g) exists to prevent). Correctly
  declined per faithful-edge-or-finding.
- **The disposition question for the batch-35 meta-phase** (§(g) priority order GROUND →
  route-as-detritus → baseline-exception): is the L3 iteration-view (MGS `partial-obstruction` +
  CGS/CGS2 global-tensor-field lifts, firm content since c019/c022) (i) genuine detritus →
  tracked baseline-exception, OR (ii) a future dependency the spine will reach once a
  driver/feature column composes the L3 (rather than L2) orthogonalize surface → a future-column
  GROUND candidate (faithful edge only, not a forced one)?
- Recommend the meta-phase **bundle** this with the standing normalize/reciprocal
  internal-utility chain grounding-vs-baseline-exception call (8 of the 26 STRONGER-GARBAGE
  nodes, per the plan's OQ) and the c110 chebyshev/jacobi preconditioner-leg ratification — all
  the same §(g) absorbed-below-column-vs-baseline-exception family. (Same shape as the c109
  Group-B + c110 lazy-tail findings; the carried lazy-tail tail is now down to this sub-chain +
  the normalize/reciprocal chain.)

**Stale in-chapter note observed (NOT edited — body-edit out of scope).** `L1/orthogonalize.md`
§:322-326 ("L1>L0 lowering theme not yet authored") and §Dependencies :170-171's "forthcoming"
phrasing are STALE — `L1-L0/orthogonalize-mutation-rotation.md` exists on disk. Likewise
`L2/orthogonalize.md` §:275-279 calls the L2>L1 theme "forthcoming … does not yet exist", also
stale. These are body prose (firm since c019/c022, frontmatter-only scope this dispatch) — flag
for a future refresh, not edited here.
