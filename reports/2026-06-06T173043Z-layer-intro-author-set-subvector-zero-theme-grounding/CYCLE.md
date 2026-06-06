---
agent: layer-intro-author
invoked_at: 2026-06-06T173043Z
scope: L1/set_subvector_zero — upgrade L1>L0 theme edge reference→depends-on(lowers-to) (P1 typed-edge grounding, c108 §5 L1-op→theme convention)
status: pending
integrated_at: 2026-06-06T180000Z
integration_commit: d88f003
integration_notes: Applied clean by integrator-per-report (D2, staging row 1). Upgraded one edge in book/src/L1/set_subvector_zero.md frontmatter from reference → depends-on(kind:lowers-to) to L1-L0/set-subvector-zero-mutation-rotation + corrected stale pre-c108 "rank-direction error" prose in 3 locations (§Status well-foundedness, §Downward, the frontmatter comment). The theme flipped out of STRONGER GARBAGE SIGNAL. Standalone + TRUE CUMULATIVE: reachable 123→124 (+1, the faithful L1-op→theme §5 ground), detritus 136→135 (−1), STRONGER GARBAGE SIGNAL 25→24 (−1). rank_violations HELD 0 (firm op rank 3 ≤ firm theme rank 3). untyped HELD 60, unresolved HELD 0. Promoted OQ stale-pre-c108-rank-direction-error-prose-on-L1-ops (sibling c104-era L1 leaves likely carry the same stale prose + un-upgraded reference edge — a systematic L1-op→theme grounding sweep for c114). Build EXIT 0, linkcheck2 clean, no finalize build-repair. Committed in cycle-113 finalize atomic commit.
---

# CYCLE: L1/set_subvector_zero theme-grounding edge

## Summary

D2 of cycle-113 (batch-36): apply ONE confirmed-faithful grounding edge. In
`book/src/L1/set_subvector_zero.md`, **upgrade** the dep-map edge to its L1>L0 lowering theme
`L1-L0/set-subvector-zero-mutation-rotation` from a `reference` (navigational, liveness-free) edge
to a `depends-on` edge with `kind: lowers-to`.

This applies the **c108-codified §5 L1-op→theme asymmetric grounding convention**
(`book/src/methodology/graded-stack-scheme.md` §5): an **L1 op** carries `lowers-to` AT its
**L1>L0 theme** as a blocking `depends-on` (unlike L2/L3 ops, which point operator→operator). The
theme is currently **reachable-dead** — it sits in the linter's STRONGER GARBAGE SIGNAL set
(declares typed deps, still unreachable) because it only receives an inbound `reference`, which
carries no liveness. Upgrading the op's outbound edge to `depends-on (kind: lowers-to)` makes the
theme a dependency of the reachable op, routing liveness DOWN to it → flips it reachable.

The edit ALSO corrects stale pre-c108 prose in the same file (in three places: the frontmatter
comment, §Status well-foundedness paragraph, §Downward) that asserted a `depends-on` to the theme
would be a "rank-direction error." That assertion **predates the §5 convention and is WRONG** — both
endpoints are `rank: firm`, so `rank(op=3) ≤ rank(theme=3)` and the edge is rank-clean; §5
deliberately routes liveness down via this edge.

**Standalone measured delta:** `reachable` 123→124 (+1), `detritus` 136→135 (−1), STRONGER GARBAGE
SIGNAL 25→24 (−1), `rank_violations` HELD 0. All exactly as the planner predicted.

**Tree state:** edit REVERTED to a clean tree; the proposed-changes blocks below are the
authoritative channel for the integrator to apply (DISPATCH-phase discipline — no direct `book/`
write).

## Faithful-edge derivation (re-verified from prose)

The `lowers-to` relationship is **real**, confirmed from both chapters' prose:

- **The theme IS the lowering of this op.** `L1-L0/set-subvector-zero-mutation-rotation.md` opens:
  "Lowers the pure L1 form [`set_subvector_zero`] … into Palace's L0 in-place index-set overwrite
  `linalg::SetSubVector(x, rows, 0.0)`" (§ intro, §"L1 form (LHS)" / §"L0 form (RHS)"). Its
  §Justification kind: "a clean syntactic-identity mutation rotation." This is a genuine
  cross-vocabulary translation (pure fresh-return → in-place receiver-argument zeroing), not an
  identity-in-named-terms smell.
- **The theme already carries the SYMMETRIC half of the §5 edge.** The theme's own frontmatter has
  `depends-on: - target: L1/set_subvector_zero / kind: lowers-to` (lines 9–10). The §5 convention
  is asymmetric — the theme→op `lowers-to depends-on` exists, but reachability requires the
  **op→theme** `lowers-to depends-on` (the upper endpoint pointing AT the theme). That op→theme
  edge is the one currently mis-typed as `reference`; this edit supplies it.
- **Well-foundedness holds (firm op ≤ firm theme).** `L1/set_subvector_zero` is `rank: firm` (line
  4). `L1-L0/set-subvector-zero-mutation-rotation` is `rank: firm` (line 6) and EXISTS. So
  `rank(op=3) ≤ rank(theme=3)` — the new `depends-on` introduces NO rank violation (confirmed:
  `rank_violations` HELD 0).
- **Reachability trace (verified on-disk).** `feature/eigenmode.L4 →(constrains-eigvec)
  L3/divfree-projector →(uses) L1/set_subvector_zero` — both intermediate edges exist as typed
  `depends-on` edges:
  - `feature/eigenmode.L4.md:13-14` — `- target: L3/divfree-projector / kind: constrains-eigvec`
    (a `depends-on` GROUNDING edge, c107).
  - `book/src/L3/divfree-projector.md:9-10` — `- target: L1/set_subvector_zero / kind: uses`
    (a `depends-on` GROUNDING edge, c107).
  So `L1/set_subvector_zero` is reachable; before this edit the theme pointed UP at the op (the
  theme→op `lowers-to`) so received no inbound liveness from a reachable node; the new op→theme
  `depends-on` flips the theme reachable.
- **Post-edit `--show-inbound` confirms the rescue is MEASURABLE:**
  `L1-L0/set-subvector-zero-mutation-rotation  <-  L1/set_subvector_zero` (new inbound
  `depends-on`), and the theme is no longer listed in the GARBAGE SIGNAL set.

This is `faithful-edge`, not `force-an-edge-to-flip-a-number`: the op genuinely `lowers-to` this
theme (the theme's whole content is the lowering of this op), and the §5 convention is the
established home for that edge.

## Proposed changes

### 1. Frontmatter — move the theme edge from `reference` to `depends-on (kind: lowers-to)` + correct the stale comment

```edit:book/src/L1/set_subvector_zero.md
[old]:
edges:
  depends-on:
    # A firm L1 operator's blocking dependency is its POSITIVE L0 SOURCE (rank-terminal
    # ground truth), not the not-yet-authored L1>L0 lowering theme. Repaired cycle-104
    # (repairer): the `firm` rank rests on the read-in-full L0 bodies + decl below, so the
    # well-foundedness invariant rank(u) ≤ rank(v) holds against rank-terminal evidence.
    - kind: cites-evidence
      target: palace/linalg/vector.cpp:461-474   # real SetSubVector body (X[id]=sr at :472)
    - kind: cites-evidence
      target: palace/linalg/vector.cpp:476-492   # complex body (XR[id]=sr :489, XI[id]=0.0 :490)
    - kind: cites-evidence
      target: palace/linalg/vector.hpp:220-221   # the `double s` SetSubVector declaration
  reference:
    - L1/eliminate_essential_bc
    - L1/eliminate_rhs
    - L1/divfree-projector
    - concepts/set_subvector_zero
    - L1-L0/set-subvector-zero-mutation-rotation   # the L1>L0 lowering theme (authored c105); downward navigational pointer, NOT a rank-blocking dependency (the theme depends-on THIS entry, not vice versa)
# The L1>L0 lowering theme `set-subvector-zero-mutation-rotation` is AUTHORED (c105); it is a
# `reference` edge above (downward navigational pointer) + live-link forward-refs in §Semantics /
# §Downward, NOT a blocking depends-on edge (the firmness grounds on the positive L0 read below;
# the theme depends-on this entry, so a depends-on from here to the theme would be a rank-direction
# error as well as redundant).
# The speculative L3 form `set-subvector-zero-mask-multiply` is a plain-text future-form note
# in §Downward, NOT a live reference edge (the seed does not exist).
[new]:
edges:
  depends-on:
    # A firm L1 operator's blocking dependencies are (a) its POSITIVE L0 SOURCE (rank-terminal
    # ground truth) via cites-evidence, and (b) its L1>L0 lowering theme via `lowers-to` (the
    # c108 §5 L1-op→theme grounding convention). The `firm` rank rests on the read-in-full L0
    # bodies + decl below; the well-foundedness invariant rank(u) ≤ rank(v) holds against the
    # rank-terminal evidence AND against the firm theme (rank(op=3) ≤ rank(theme=3)).
    - kind: cites-evidence
      target: palace/linalg/vector.cpp:461-474   # real SetSubVector body (X[id]=sr at :472)
    - kind: cites-evidence
      target: palace/linalg/vector.cpp:476-492   # complex body (XR[id]=sr :489, XI[id]=0.0 :490)
    - kind: cites-evidence
      target: palace/linalg/vector.hpp:220-221   # the `double s` SetSubVector declaration
    - kind: lowers-to
      target: L1-L0/set-subvector-zero-mutation-rotation   # the L1>L0 lowering theme (authored c105); per the c108 §5 L1-op→theme convention this is a blocking depends-on (kind: lowers-to), which routes liveness DOWN to the theme (flips it reachable)
  reference:
    - L1/eliminate_essential_bc
    - L1/eliminate_rhs
    - L1/divfree-projector
    - concepts/set_subvector_zero
# The L1>L0 lowering theme `set-subvector-zero-mutation-rotation` is AUTHORED (c105) and now
# carried as a `depends-on (kind: lowers-to)` edge above, NOT a `reference`. This applies the
# c108-codified §5 L1-op→theme asymmetric grounding convention (`book/src/methodology/graded-stack-scheme.md`
# §5; precedent: the `bc-elimination-post-composition-dissolution` / `divfree-projector-mutation-rotation`
# chain grounding, which established the L1-op→theme `lowers-to depends-on` edge that routes liveness
# DOWN to the theme). The edge is rank-clean — both this op and the theme are `rank: firm`
# (rank(op=3) ≤ rank(theme=3)), so it is NOT a rank-direction error (the earlier pre-c108 comment
# here asserting a "rank-direction error" predated the §5 convention and was WRONG). The firmness
# still grounds on the positive L0 read below; this edge additionally gives the theme its inbound
# liveness (the theme was reachable-dead with only an inbound `reference`).
# The speculative L3 form `set-subvector-zero-mask-multiply` is a plain-text future-form note
# in §Downward, NOT a live reference edge (the seed does not exist).
```

### 2. §Status — correct the well-foundedness paragraph's stale "rank-direction error" framing

```edit:book/src/L1/set_subvector_zero.md
[old]:
Well-foundedness: the `depends-on` edges are `cites-evidence` edges to the **positive L0 source**
(real `vector.cpp:461-474`, complex `:476-492`, decl `vector.hpp:220-221`), which is rank-terminal
ground truth — so the `firm` (rank 3) operator rests only on rank-terminal evidence and the
graded-stack invariant `rank(u) ≤ rank(v)` holds. (Repaired cycle-104: the earlier draft routed
the sole `depends-on` through the not-yet-authored L1>L0 theme `set-subvector-zero-mutation-rotation`,
which is both a dangling live link and a firm-resting-on-missing-dep rank violation; the firmness
in fact grounds on the positive L0 read, exactly as for the BLAS-1 leaves `reciprocal` /
`elementwise_product`, whose firmness does not block on their L1>L0 themes.) The L1>L0 lowering
theme [`set-subvector-zero-mutation-rotation`](../L1-L0/set-subvector-zero-mutation-rotation.md)
(authored c105) is a downward narration, not an upward rank-blocking dependency.
[new]:
Well-foundedness: the `depends-on` edges are (a) `cites-evidence` edges to the **positive L0
source** (real `vector.cpp:461-474`, complex `:476-492`, decl `vector.hpp:220-221`), which is
rank-terminal ground truth, and (b) a `lowers-to` edge to the firm L1>L0 lowering theme
[`set-subvector-zero-mutation-rotation`](../L1-L0/set-subvector-zero-mutation-rotation.md) (also
`rank: firm`). So the `firm` (rank 3) operator rests on rank-terminal evidence AND on a firm
theme, and the graded-stack invariant `rank(u) ≤ rank(v)` holds for both (`rank(op=3) ≤
rank(theme=3)`). The firmness *grounds* on the positive L0 read (exactly as for the BLAS-1 leaves
`reciprocal` / `elementwise_product`); the `lowers-to` theme edge applies the **c108 §5 L1-op→theme
asymmetric grounding convention** (`book/src/methodology/graded-stack-scheme.md` §5; precedent: the
`bc-elimination-post-composition-dissolution` / `divfree-projector-mutation-rotation` chain
grounding), routing liveness DOWN to the theme (which was reachable-dead with only an inbound
`reference`). (Note: an **earlier** c104 comment here asserted that a `depends-on` from this op to
the theme would be a "rank-direction error" — that predated the §5 convention and was WRONG; both
endpoints are firm, so the edge is rank-clean and is the deliberate liveness route, not a redundant
back-edge.)
```

### 3. §Downward to L0 — correct the "downward `reference` pointer, not a blocking edge" phrasing

```edit:book/src/L1/set_subvector_zero.md
[old]:
The lowering is the [`set-subvector-zero-mutation-rotation`](../L1-L0/set-subvector-zero-mutation-rotation.md)
L1>L0 theme (authored c105; this entry's firmness rests on the positive L0 read,
cited as `cites-evidence` deps, with the theme as a downward `reference` pointer, not a blocking
edge): it narrates how this
[new]:
The lowering is the [`set-subvector-zero-mutation-rotation`](../L1-L0/set-subvector-zero-mutation-rotation.md)
L1>L0 theme (authored c105; this entry's firmness rests on the positive L0 read,
cited as `cites-evidence` deps, with the theme carried as a `lowers-to` `depends-on` edge per the
c108 §5 L1-op→theme convention — the edge that routes liveness down to the theme): it narrates how
this
```

## Supporting evidence

- **Target op:** `book/src/L1/set_subvector_zero.md` — `rank: firm` (line 4); pre-edit the theme
  edge is at `reference:` line 22 with the stale "rank-direction error" comment lines 23–27.
- **Target theme:** `book/src/L1-L0/set-subvector-zero-mutation-rotation.md` — `rank: firm` (line
  6); already carries the symmetric `depends-on target: L1/set_subvector_zero kind: lowers-to`
  (lines 9–10).
- **§5 convention:** `book/src/methodology/graded-stack-scheme.md:236-245` — the batch-34
  clarification "Reachability ≠ well-foundedness for a lowering theme": "an **L1 op**'s
  `lowers_to:` points operator → its **L1-L0 theme** (so typing the L1 op rescues its theme
  automatically)"; "the bounded fix per affected theme is one edge."
- **Reachability chain (typed `depends-on` edges, on-disk):**
  `feature/eigenmode.L4.md:13-14` (`→ L3/divfree-projector`) and
  `book/src/L3/divfree-projector.md:9-10` (`→ L1/set_subvector_zero`).
- **Linter baseline (clean landed tree):** `files=355, typed=295, untyped=60, roots=36,
  reachable=123, rank_violations=0, unresolved=0, detritus=136, STRONGER GARBAGE SIGNAL=25`.
- **Linter after the edit (standalone, this dispatch only — D1 runs in parallel observation-only,
  no contamination):** `reachable=124 (+1), detritus=135 (−1), STRONGER GARBAGE SIGNAL=24 (−1),
  rank_violations=0 (HELD), unresolved=0, untyped=60, typed=295, roots=36`. `--show-inbound`
  confirms `L1-L0/set-subvector-zero-mutation-rotation <- L1/set_subvector_zero` and the theme is
  no longer in the GARBAGE SIGNAL list.

## Open questions / caveats

- **Candidate friction — stale pre-c108 "rank-direction error" prose may exist on OTHER L1 ops
  (flag for meta-phase).** This op carried an explicit c104-era comment asserting that an
  L1-op→L1-L0-theme `depends-on` would be a "rank-direction error" — a belief that was correct
  *before* the c108 §5 L1-op→theme convention but is now WRONG. Other firm L1 ops repaired in the
  same c104 era (`reciprocal`, `elementwise_product`, `scal`, and any L1 leaf whose firmness was
  re-grounded onto positive L0 reads and whose L1>L0 theme was demoted to a `reference`) likely
  carry the **same stale framing** and the **same un-upgraded `reference` edge to their L1>L0
  theme** — which means their themes are probably also reachable-dead in the same way. The
  STRONGER GARBAGE SIGNAL set (24 post-edit) includes `L1/normalize`, and the edge-untyped
  detritus includes many L1-L0 themes; a systematic sweep of L1-op→L1-L0-theme edges (upgrade
  `reference`→`depends-on (kind: lowers-to)` per §5, correcting the matching stale "rank-direction
  error" prose) is the natural next P1 tranche. **Recommend the meta-phase open a friction-ledger
  entry** (candidate name: `stale-pre-c108-rank-direction-error-prose-on-L1-ops`) and the
  cycle-planner schedule the L1-op→theme sweep as a batch-36/37 P1 tranche — each is a single
  faithful edge with the same measurable rescue shape as this one. (Out of this one-edge scope.)
- **Tree state:** edit was applied, measured, then REVERTED to a clean tree. The integrator should
  apply the three proposed-changes blocks above (all in one file, `book/src/L1/set_subvector_zero.md`).
