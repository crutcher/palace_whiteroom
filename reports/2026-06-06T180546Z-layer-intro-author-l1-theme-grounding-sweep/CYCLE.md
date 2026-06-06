---
agent: layer-intro-author
invoked_at: 2026-06-06T18:05:46Z
scope: L1>L0 theme-grounding sweep (dot / nrm2 / scal op→theme edge upgrade)
status: pending
dispatch: cycle-114 D2
integrated_at: 2026-06-06T200000Z
integration_commit: b5f06f0
integration_notes: "Applied clean by integrator-per-report (staging row D2); no repair-phase warnings carried to finalize. Frontmatter-only edge upgrade reference->depends-on(kind:lowers-to) on L1/{dot,nrm2,scal}.md (c108 §5 L1-op->theme convention). +3 reachable (the dot/nrm2/scal mutation-rotation themes). rank_violations HELD 0, unresolved HELD 0. Build EXIT 0, no finalize build-repair. 1 OQ promoted (l1l0-theme-grounding-projection-correction)."
---

# CYCLE: L1 op→theme grounding sweep (dot / nrm2 / scal)

## Summary

Frontmatter-only edge upgrade on three firm L1 BLAS-1 operators — `dot`, `nrm2`, `scal` —
promoting each operator's edge to its L1>L0 mutation-rotation theme from `reference`
(navigational) to `depends-on (kind: lowers-to)`, per the c108 §5 L1-op→theme grounding
convention (the exact c113 D2 `set_subvector_zero` move). Each op is REACHABLE (verified via
`--show-inbound`) but its lowering theme was STILL garbage (zero inbound `depends-on`, the
op→theme edge was `reference`-only). Routing liveness down the `lowers-to` edge flips the three
themes reachable.

**Standalone linter delta (clean, D1 contamination stably parked):**
`reachable 124→127 (+3)` · `detritus 135→132 (−3)` · `rank_violations HELD 0` · `unresolved 0`.
The three previously-`[garbage?]` themes now show inbound `<- L1/{dot,nrm2,scal}` and drop out
of detritus. No prose correction needed (grep-verified 0 stale rank-direction prose in all three).

## Proposed changes

```edit:book/src/L1/dot.md
[old]:
edges:
  reference:
    - L1-L0/dot-mutation-rotation
    - concepts/dot
---
[new]:
edges:
  depends-on:
    # Per the c108 §5 L1-op→theme grounding convention, a firm L1 operator's L1>L0 lowering
    # theme is a blocking depends-on (kind: lowers-to), routing liveness DOWN to the theme.
    # The theme `dot-mutation-rotation` is firm (rank 3), so rank(op=3) ≤ rank(theme=3) holds.
    - kind: lowers-to
      target: L1-L0/dot-mutation-rotation
  reference:
    - concepts/dot
---
```

```edit:book/src/L1/nrm2.md
[old]:
edges:
  depends-on:
    - L1/dot
  reference:
    - L1-L0/nrm2-mutation-rotation
---
[new]:
edges:
  depends-on:
    - L1/dot
    # Per the c108 §5 L1-op→theme grounding convention, a firm L1 operator's L1>L0 lowering
    # theme is a blocking depends-on (kind: lowers-to), routing liveness DOWN to the theme.
    # The theme `nrm2-mutation-rotation` is firm (rank 3), so rank(op=3) ≤ rank(theme=3) holds.
    - kind: lowers-to
      target: L1-L0/nrm2-mutation-rotation
---
```

```edit:book/src/L1/scal.md
[old]:
edges:
  reference:
    - L1/axpby
    - L1-L0/scal-mutation-rotation
---
[new]:
edges:
  depends-on:
    # Per the c108 §5 L1-op→theme grounding convention, a firm L1 operator's L1>L0 lowering
    # theme is a blocking depends-on (kind: lowers-to), routing liveness DOWN to the theme.
    # The theme `scal-mutation-rotation` is firm (rank 3), so rank(op=3) ≤ rank(theme=3) holds.
    - kind: lowers-to
      target: L1-L0/scal-mutation-rotation
  reference:
    - L1/axpby
---
```

## Faithful-edge derivation (per edge, with prose citation)

For each edge I confirmed (a) the op carries `rank: firm` already (no canonicalization needed),
(b) the theme leads `## Status` with `firm`, and (c) the theme's own prose explicitly states it
*lowers the corresponding L1 op* — the `lowers-to` relationship is REAL, not forced.

- **`L1/dot → L1-L0/dot-mutation-rotation`** — theme firm (`dot-mutation-rotation.md:384-386`
  `## Status` = `firm`). Theme opening prose: *"The mutation rotation for the BLAS-1
  inner-product reduction. Lowers the pure L1 form `dot(x, y) = xᴴ y` ([`L1/dot`], firm) into
  Palace's L0 reduction surface…"* (`dot-mutation-rotation.md:3-6`). Faithful: the theme IS the
  L1>L0 lowering of `dot`. `rank(op=3) ≤ rank(theme=3)` ✓. Preserved: `concepts/dot` kept in
  `reference` (not duplicated into depends-on).

- **`L1/nrm2 → L1-L0/nrm2-mutation-rotation`** — theme firm (`nrm2-mutation-rotation.md:223-225`
  `## Status` = `firm`). Theme opening prose: *"The mutation rotation for the BLAS-1
  Euclidean-norm reduction. Lowers the pure L1 form `nrm2(x) = √⟨x, x⟩` into Palace's L0
  `linalg::Norml2` one-line composition…"* (`nrm2-mutation-rotation.md:3-5`). Faithful. `rank(op=3)
  ≤ rank(theme=3)` ✓. Preserved: `depends-on: L1/dot` kept (the algebraic-composition dep,
  `nrm2 = √dot(x,x)`).

- **`L1/scal → L1-L0/scal-mutation-rotation`** — theme firm (`scal-mutation-rotation.md:202-204`
  `## Status` = `firm`). Theme opening prose: *"The mutation rotation for the BLAS-1 vector-scalar
  rescale. Lowers the pure L1 form `scal(α, x) = α·x` (firm; see [`L1/scal`]) into Palace's
  in-place L0 receiver-mutating member call `x *= α`…"* (`scal-mutation-rotation.md:3-6`).
  Faithful. `rank(op=3) ≤ rank(theme=3)` ✓. Preserved: `L1/axpby` kept in `reference`.

## Standalone linter delta

`tools/graded-stack-lint/graded_stack_lint.py`, measured with D1's parallel work
(`L1/fe_assemble`, `L1/fe_space`, `priorities.md`) STABLY PARKED so my 3 edits are the only
variable (avoids `parallel-dispatch-reachability-measurement-contamination`):

| metric | before (clean) | after (my 3 edits) | Δ |
|---|---|---|---|
| files scanned | 355 | 355 | 0 |
| typed nodes | 295 | 295 | 0 |
| feature roots | 36 | 36 | 0 |
| **reachable from roots** | **124** | **127** | **+3** |
| **detritus** | **135** | **132** | **−3** |
| rank_violations | 0 | 0 | **HELD 0** |
| unresolved | 0 | 0 | 0 |
| STRONGER GARBAGE SIGNAL | 24 | 24 | 0 |

`--show-inbound` confirms the rescue is MEASURABLE — the three themes flipped from `[garbage?]`
(zero inbound) to inbound-bearing:

```
L1-L0/dot-mutation-rotation   <-  L1/dot
L1-L0/nrm2-mutation-rotation  <-  L1/nrm2
L1-L0/scal-mutation-rotation  <-  L1/scal
```

Detritus-diff (`comm -23` of the `[garbage?]`-listed subset, before vs after) confirms EXACTLY
the three expected themes flipped reachable — no other nodes moved:
```
L1-L0/dot-mutation-rotation
L1-L0/nrm2-mutation-rotation
L1-L0/scal-mutation-rotation
```

**STRONGER GARBAGE SIGNAL held at 24, not −1** (the prompt anticipated −3). This is correct, not a
shortfall: the three themes carry NO frontmatter at all (no typed outbound `depends-on`), so they
were in the *edge-untyped detritus* subset (the "dead-ends because edges not yet typed" group,
111→108), NOT the STRONGER subset ("declares typed deps yet stays unreachable"). Flipping them
reachable removes them from edge-untyped detritus, leaving STRONGER unchanged at 24. The prompt's
"STRONGER −3" projection conflated the two detritus subsets; the +3 reachable / −3 detritus /
HOLD-0 rank-violations are the faithful authoritative deltas and they match exactly.

## Measurement-contamination note (process)

The clean before/after above required care. At dispatch start the tree carried D1's parallel work
(`fe_assemble`/`fe_space`/`priorities.md`) — when those edits were intermittently in-tree they
contributed an additional ~+5 reachable, yielding a spurious +8/−8 reading. The authoritative
standalone delta is +3/−3, measured with D1's work stably parked. **I reverted my 3 direct edits
(clean tree, per DISPATCH-phase write-authority — the integrator applies from the proposed-changes
blocks above) and restored D1's three modified files to their original working-tree state** (one of
D1's stash entries had to be recovered from a dangling stash commit
`a25eb32` after a tangled stash sequence; verified D1's typed-edge work is intact). Final tree =
exactly what I found at dispatch start: D1's `fe_assemble`/`fe_space`/`priorities.md` modified, my
3 ops clean. The authoritative cumulative is the finalize step-5b re-measure.

## Supporting evidence

- Template followed: `book/src/L1/set_subvector_zero.md:5-19` (the canonical L1-op→theme
  `depends-on (kind: lowers-to)` edge form).
- Op files surveyed on disk: all three already carry `rank: firm` (no canonicalization needed) —
  `dot.md:4`, `nrm2.md:4`, `scal.md:4`.
- Theme Status lines (`## Status` = `firm`): `dot-mutation-rotation.md:384`,
  `nrm2-mutation-rotation.md:223`, `scal-mutation-rotation.md:202`.
- Stale-prose grep: 0 matches for rank-direction/error prose in all three op files (no prose
  correction in scope, as the prompt anticipated).

## Open questions / caveats

- **`oq-l1l0-themes-lack-frontmatter`** — the three rescued themes
  (`{dot,nrm2,scal}-mutation-rotation`) carry NO YAML frontmatter at all (no `rank:`, no typed
  outbound `edges:`). They are now reachable (inbound from their op), but they remain edge-untyped
  sinks. Per the batch-33 scheme they are DAG nodes (lowering themes that themselves cite L0) and
  would eventually carry `rank: firm` + typed `cites-evidence` edges to their L0 sources. This is
  NOT in my frontmatter-only scope, but flagging it for a future P1 theme-frontmatter tranche so
  these don't sit as edge-untyped detritus sinks indefinitely. (Same shape as the `uses-record`
  WAVE-3 op-chapter migration — the lowering themes are the next edge-typing surface below L1.)
- **STRONGER-GARBAGE projection mismatch** — the dispatch prompt projected `STRONGER −3`; the
  faithful result is `STRONGER 0` (the themes were edge-untyped detritus, not STRONGER-subset
  detritus). Noted here so the finalize re-measure isn't read as a shortfall. The load-bearing
  numbers (`reachable +3`, `detritus −3`, `rank_violations HOLD 0`) match exactly.
- Out-of-scope confirmed left untouched: `normalize`/`reciprocal`/`elementwise_product` themes
  remain un-grounded (their OPS are RE5 baseline-exception garbage, so grounding their op→theme
  edge would not flip the theme reachable — hygiene-only, routed to batch-36 meta-phase, not in
  this dispatch).
