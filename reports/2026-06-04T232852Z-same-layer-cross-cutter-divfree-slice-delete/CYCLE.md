---
agent: same-layer-cross-cutter
invoked_at: 2026-06-04T232852Z
scope: L1 cross-cut — absorb-and-delete spec/slices/divfree.md (graded-stack P2 slice-deletion, batch-31 tranche-1, dispatch D2)
status: integrated
integrated_at: 2026-06-04T232852Z
integration_commit: 8c3b94baa1ff30bb724c108631c394bf7a471a41
integration_notes: "Applied clean by integrator-per-report (D2); divfree slice DELETED + 3 L1/ re-anchors (ksp_solve:131 + Evidence bullet -> divfree-projector.md; no-op absorb, firm homes already carried divfree.cpp:175). Batch finalize cycle-097: cargo make book EXIT 0, step-5b rank_violations=0 (GATE PASS), no newly-orphaned node. retroactive-budget global 0."
---

# CYCLE: L1 observation — divfree-slice-detritus-GC

## Summary
Comparing the cycle-001-era slice `book/src/spec/slices/divfree.md` against its firm
homes `book/src/L1/divfree-projector.md` and `book/src/L1/ksp_solve.md`, the slice is
**reachability-GC detritus**: it carries ZERO line-anchor L0 citations, every fact it
states is already positively anchored to Palace source in the firm `divfree-projector.md`
(which superseded it at cycle-015), and the only live inbound links to it are three
navigational pointers (two in `ksp_solve.md`, one self-supersession footer in
`divfree-projector.md`) plus the two SUMMARY/index rows D5 owns. No `depends-on`
(blocking) edge targets it. The slice's own reduction-status header (cycle-012) claims a
six-item "load-bearing evidence ... cited by" list, but every claimed citer either does
not link the slice file at all (the four concept pages, `eigsolve.md`,
`eigensolver-wrapper.md`) or links it only as a redundant slice-precedent pointer
(`ksp_solve.md`). The header is stale; the slice is safe to delete after re-anchoring the
three live pointers.

## Observation kind
**Redundancy** — the slice and `L1/divfree-projector.md` are the same content; the firm
entry is the authoritative, positively-L0-anchored form and the slice is its un-cited
precursor. (Graded-stack framing: an unreachable, claim-duplicating node = detritus to
sweep.)

## Specific finding

### 1. Firm homes carry the positive L0 (slice has zero line-anchor cites) — VERIFIED inline

The slice `divfree.md` carries NO `path:start-end` line citations anywhere — its L0
references are bare prose (`palace/linalg/divfree.cpp` named without a range, e.g. slice
lines 120-124 "Call sites"). By contrast the firm `L1/divfree-projector.md` anchors every
step to Palace source. Paste-inline confirmation of the key facts and their firm-home L0
homes:

| Fact (slice prose) | Slice loc | Firm-home positive L0 cite |
|---|---|---|
| 4-step apply `WeakDiv→Z→ksp→Grad` | slice:63-66, :170-184 | `book/src/L1/divfree-projector.md:122-135` → `palace/linalg/divfree.cpp:155-187` (per-step: :159-168, :170-174, :175, :177-186) |
| ksp solve `M·ψ=rhs` (step 3) | slice:65, :179 | `book/src/L1/divfree-projector.md:128-129` → `palace/linalg/divfree.cpp:175`; also `book/src/L1/ksp_solve.md:131` cites `divfree.cpp:175` directly |
| WeakDiv sign convention (`+Grad·ψ`) | slice:44-45, :135-140 (flagged **unverified** OQ) | `book/src/L1/divfree-projector.md:139-150,193-204` → `palace/fem/integrator.hpp:217` + `palace/fem/integ/mixedvecgrad.cpp:202` (`-1.0`) vs :142 (no `-1.0`) — **positively resolved** cycle-014 audit |
| Construction (M/WeakDiv/Grad/bdr/ksp) | slice:39-56, :150-160 | `book/src/L1/divfree-projector.md:57-91` → `palace/linalg/divfree.cpp:43-152` (per-field ranges :84-110, :111-116, :117, :103-105/:51-81, :121-149) |
| empty-boundary synthetic pin | slice:47-51, :155 | `book/src/L1/divfree-projector.md:82-85` → `palace/linalg/divfree.cpp:51-81` |
| complex Re/Im block-diagonal | slice:86-92, :194-216 | `book/src/L1/divfree-projector.md:152-156,189-192` → `palace/linalg/divfree.cpp:159-184` |
| defining condition `Gᵀ M y'=0` | slice:31, :68-69 | `book/src/L1/divfree-projector.md:111-120,181-188` → `palace/linalg/divfree.hpp:28-31` |
| eigensolver call sites | slice:120-124 (no ranges) | `book/src/L1/divfree-projector.md:304-308` → `palace/drivers/eigensolver.cpp:260-262`, `arpack.cpp:586,...`, `slepc.cpp:1870,...` |

**No UNIQUE load-bearing content in the slice is uncovered by the firm homes.** The two
slice items that are NOT in the firm entry are both deliberately dropped, not load-bearing:
- The slice's L2/L3/L4 prose (slice:142-413) — superseded by `L2`/`L3`/`L4` divfree
  chapters + the `L1-L0/divfree-projector-mutation-rotation.md` theme; the firm entry's
  footer (line 325-327) already records the supersession. (L2/L3/L4 homes are out of my
  D2 absorb-scope and already firm; nothing to absorb.)
- The slice's three Open-questions (slice:126-140): the scope-attribution-to-driven/
  transient question and the WeakDiv-sign question are both **closed** — the sign OQ
  `divfree-weakdiv-sign-convention-l0-verify` was resolved cycle-014/015 (see
  `book/src/L1/divfree-projector.md:244-265`); the scope question is recorded in firm form at
  `book/src/L1/divfree-projector.md:1-9` (eigensolver-path only). The "no unit test" note is
  carried at `book/src/L1/divfree-projector.md:267-277`. **Nothing to absorb.**

**Conclusion:** absorb = no-op (firm homes already complete). Proceed directly to
re-anchor + delete.

### 2. Inbound `L1/` prose pointers — GREP-VERIFIED, re-anchor proposed

`grep -rn "divfree.md\|slices/divfree" book/src/ | grep -v "spec/slices/divfree.md:"` →
the only live-artifact `L1/` hits are:
- `book/src/L1/ksp_solve.md:131` — parenthetical `(per [`spec/slices/divfree`](../spec/slices/divfree.md) §L2 step 3)`. The bullet ALREADY carries the positive L0 cite `palace/linalg/divfree.cpp:175` inline; only the trailing slice-pointer parenthetical needs to drop / re-point to the firm L2 home.
- `book/src/L1/ksp_solve.md:143` — Evidence bullet `book/src/spec/slices/divfree.md — the slice-corpus precedent ...`. Re-point to the firm `book/src/L1/divfree-projector.md`.
- `book/src/L1/divfree-projector.md:325-327` — the "Slice-corpus precedent ... this firm entry supersedes its L1 content" footer linking `slices/divfree.md:24-100` / `:142-216`. Drop the slice link (the slice is being deleted; the footer's job is done).

### 3. Inbound concept pages — GREP-VERIFIED: ZERO slice-file links (planner's "~4" was the slice's stale self-list)

`grep -rn "divfree.md\|slices/divfree\|spec/slices/divfree" book/src/concepts/` → **no
output** (empty). The slice's reduction-header (slice:6-9) lists four concept pages as
"load-bearing evidence ... cited by", but those are forward-references FROM the slice. The
actual concept-page mentions of divfree (`grep "divfree" book/src/concepts/`) are all
either prose ("the `divfree` slice uses apply_linop ...", `book/src/concepts/apply_linop.md:43`,
`book/src/concepts/ksp_solve.md:34`) or links to the FIRM homes (`book/src/concepts/nested-constructed-operator-gate.md:46,86,
88,89` → `book/src/L1-L0/divfree-projector-mutation-rotation.md` + `book/src/L1/divfree-projector.md`) or
mermaid graph node-ids named `divfree` (`book/src/concepts/dependency-map.md:153,...` — node ids, not file
links). **No concept page links the slice file. No concept-page repoint is needed.**
(Recommendation to D5/meta: the slice's stale six-item header is itself a reason it reads
as load-bearing when it is not — deleting the file removes the misleading header.)

### 4. eigsolve / eigensolver-wrapper — GREP-VERIFIED: ZERO slice links
`grep -n "slices/divfree\|divfree.md" book/src/L1/eigsolve.md book/src/L0/eigensolver-wrapper.md` → exit 1 (no match). The slice-header's claim they cite it is stale prose; no repoint needed.

### 5. No `depends-on` blocking edge targets the slice (reachability-GC clear)
`grep -rn "depends-on\|depends_on" book/src/ | grep -i "slices/divfree\|divfree.md"` →
empty. The slice file has no frontmatter at all (bare `# Slice: divfree` heading). All
inbound references are `reference`-kind (navigational) — three live pointers (re-anchored
below) + two SUMMARY/index rows (D5) + two frozen meta-review history mentions (leave;
historical record, not a live link into the artifact). **Safe to delete.**

## Recommendation
**Dispatch integrator-per-report to apply the proposed-changes below** — three pointer
re-anchors + the slice deletion. This is mechanical detritus-GC; no follow-up combinator/
harvester dispatch is motivated (the firm content is complete).

## Proposed changes

### proposed-change 1 — re-anchor `L1/ksp_solve.md:131` (drop slice link, keep positive L0)
File: `book/src/L1/ksp_solve.md`
Replace:
```
- `palace/linalg/divfree.cpp:175` — `ksp->Mult(rhs, psi)` call site inside `DivFreeSolver<VecType>::Mult` — direct L0 evidence of the use pattern; the L2 form lifts this to `psi = ksp_solve(self.ksp, rhs)` (per [`spec/slices/divfree`](../spec/slices/divfree.md) §L2 step 3).
```
With:
```
- `palace/linalg/divfree.cpp:175` — `ksp->Mult(rhs, psi)` call site inside `DivFreeSolver<VecType>::Mult` — direct L0 evidence of the use pattern; the L2 form lifts this to `psi = ksp_solve(self.ksp, rhs)` (the projected H1 solve, step 3 of [`divfree-projector`](./divfree-projector.md)).
```

### proposed-change 2 — re-anchor `L1/ksp_solve.md:143` (slice-precedent Evidence bullet → firm home)
File: `book/src/L1/ksp_solve.md`
Replace:
```
- `book/src/spec/slices/divfree.md` — the slice-corpus precedent for the L1 / L2 `ksp_solve` use pattern.
```
With:
```
- `book/src/L1/divfree-projector.md` — the firm L1 consumer of `ksp_solve`: the projected H1 solve `M·ψ = rhs` (`palace/linalg/divfree.cpp:175`) is its constructed-operator inner solve.
```

### proposed-change 3 — drop slice link in `L1/divfree-projector.md` footer (lines 325-327)
File: `book/src/L1/divfree-projector.md`
Replace:
```
Slice-corpus precedent (cycle-001-era, cycle-012-reduced; this firm entry
supersedes its L1 content): `book/src/spec/slices/divfree.md:24-100` (L1 form),
`:142-216` (L2 primitive composition).
```
With:
```
Provenance: this firm entry superseded the cycle-001-era `divfree` slice (its L1
form at slice §L1, L2 primitive composition at slice §L2). The slice was deleted
in the batch-31 graded-stack slice-deletion campaign once this entry and the
`L2`/`L3`/`L4` divfree chapters + the `L1-L0/divfree-projector-mutation-rotation`
theme carried all of its content with positive L0 anchoring; git history is the
record.
```

### proposed-change 4 — DELETE the slice file
Delete: `book/src/spec/slices/divfree.md`
Justification: reachability-GC detritus (no `depends-on` inbound; all content positively
re-anchored in `L1/divfree-projector.md` + L2/L3/L4 divfree chapters; the three live
navigational pointers re-anchored in changes 1-3). The two `book/src/meta-reviews/*`
mentions are frozen historical records (cycle 10-18 narrative), not live artifact links,
and remain valid as history.

## Supporting evidence
- Slice: `book/src/spec/slices/divfree.md:1-413` (full read; zero `path:start-end` cites; reduction-header at :3-15 is stale).
- Firm home: `book/src/L1/divfree-projector.md:1-327` (full read; positive L0 throughout — apply :122-135, sign :139-150/:193-204, construction :57-91, status/promotion :232-277, evidence :279-323).
- Firm home: `book/src/L1/ksp_solve.md:131,:143` (the two re-anchor targets; `book/src/L1/ksp_solve.md:131` already carries `divfree.cpp:175` inline).
- Grep set (all run from repo root):
  - `grep -rn "divfree.md\|slices/divfree" book/src/ | grep -v "spec/slices/divfree.md:"` → only ksp_solve.md:131,:143 + divfree-projector.md (footer hit) + SUMMARY.md:295 + spec/index.md:18 + 2 meta-reviews.
  - `grep -rn "divfree.md\|slices/divfree\|spec/slices/divfree" book/src/concepts/` → EMPTY (no concept-page slice link).
  - `grep -n "slices/divfree\|divfree.md" book/src/L1/eigsolve.md book/src/L0/eigensolver-wrapper.md` → exit 1 (no match).
  - `grep -rn "depends-on\|depends_on" book/src/ | grep -i "slices/divfree\|divfree.md"` → EMPTY (no blocking edge).

## Open questions / caveats
- **D5 boundary respected.** I did NOT touch `book/src/SUMMARY.md:295` or
  `book/src/spec/index.md:18` (the two remaining inbound rows); D5 owns removing those when
  the file deletes. If D5 does not run in this tranche, the deletion in change 4 will leave
  two dangling `linkcheck2` errors — **change 4 must land in the same cycle as D5's
  SUMMARY/index row removals.** Flagging for the integrator-finalize build gate.
- **krylov-trio constraint respected.** `L1/ksp_solve.md` is an L1 operator entry, not a
  `krylov-step` file; the constraint "do NOT touch any krylov-trio file" targets
  `L4/krylov-step.md` / `L4-L3/krylov-step-typed-wrapper-dissolution.md` / `L2/krylov-step.md`,
  none of which I touched.
- **Stale slice-header observation (drive-by, no action needed by me):** the slice's
  cycle-012 reduction-header (slice:3-15) asserts six "load-bearing evidence ... cited by"
  links that no longer exist as file links (the concept pages, eigsolve, eigensolver-wrapper).
  This staleness is exactly why the slice reads as more connected than it is. Deleting the
  file resolves it; no separate fix required.
- **No CYCLE.md write-filter block encountered** (filename is `CYCLE.md`, per the rename
  convention).
