---
agent: same-layer-cross-cutter
invoked_at: 2026-06-05T04:52:01Z
scope: cycle-100 D4 — batch-31 class-B deleted-slice plaintext-residue cleanup (priorities #2)
status: pending
integrated_at: 2026-06-05T051726Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied cycle-100 (staging row 4/4). Class-B slice-residue cleanup, 8 files: 2 repointed (L4/krylov-step.md GMRES inner_loop + arnoldiStep → absorbed-into-Form-A + live L0 + loop-migration home; arnoldi L0 range repairer-widened orthog.hpp:41-74 → :41-88), 6 struck (chebyshev cohort L1/L2/L3/L4 + L2/index.md:133 + L3/index.md:53,:99), 1 normalized (L1/orthogonalize.md). Left untouched the 2 triangular-solve-obstruction.md historical pointers + the out-of-scope CG Form-B cg.md:27-141 pointer (recorded in OQ concepts-index-and-depmap-orchestrator-era-framing-refresh). Build EXIT 0 (no live dead-slice markdown links remain); step-5b NO newly-orphaned node, rank_violations 0."
---

# CYCLE: book-wide observation — class-B deleted-slice plaintext residue

## Summary
Comparing the surviving deleted-slug pointers across the firm chapter cohort (the
consolidated cleanup dispatch for priorities item #2, the migrated OQs
`krylov-trio-class-B-plaintext-mention-residue-batch31-cleanup` +
`dependency-map-cg-precond-stale-mermaid-edges`), I find the residue partitions
into **three dispositionally-distinct classes**, not one. (a) Two **bare** dead-slice
pointers in `L4/krylov-step.md` (`gmres.md:459-471`, `arnoldi_step.md:285-298`) that
carry **no absorb-home and no L0 re-citation** — anomalous against the sibling CG
pointer in the same list, which already re-cites L0 directly; these I **repoint** to
the firm absorb-home + L0. (b) Six **chebyshev provenance notes** (across the firm
`L1`/`L2`/`L3`/`L4` chebyshev cohort + `L2/index` + `L3/index`) whose absorb-home is
already named in-context but which retain a stale dead-path `spec/slices/chebyshev.md:<range>`;
these I **strike** the dead path, preserving the narrative + git-history record. (c) Two
provenance notes already framed as "(now-deleted) / deleted cycle-097, git history
retains" (`L1/orthogonalize`, `L1-L0/triangular-solve-obstruction`) — accept-as-historical,
one light normalization only. The two **concept-index files** the task tagged
(`concepts/index.md`, `concepts/dependency-map.md`) are a **separate, larger finding**:
their residue is not a few dead pointers but **whole-file orchestrator/slice-era framing**
(decommissioned `prompts/*`, `concept_writes mode=create`, `spec/slices/*` grep recipes,
slice-slug Mermaid nodes) — out of micro-sweep scope; surfaced as a follow-up below. The
expected literal `cg_preconditioning_framework` Mermaid node does **not** exist in
`dependency-map.md`; that node's edges are keyed on the deleted **krylov-trio slugs**
(`gmres`/`orthog`/`arnoldi_step`), part of the legacy-framing finding. **Build is green
at baseline and every proposed edit is plaintext/inline-code — zero live markdown links
target a deleted slice** (the only two are fenced format-example placeholders `X`/`Y`,
which `linkcheck2` ignores).

## Observation kind
**Redundancy** — surviving plaintext provenance pointers to deleted files that the
firm absorb-homes now subsume; the residue is the un-cleaned tail of the graded-stack
P2 slice-deletion campaign (cycles 097/098/099).

## Specific finding

### Disposition tally
- **Repointed: 2 pointers** (both in `L4/krylov-step.md`).
- **Struck (dead-path removed, narrative + git-history kept): 6 pointers**
  (`L4/chebyshev.md`, `L3/chebyshev.md`, `L2/chebyshev-iteration.md`,
  `L1/chebyshev-smoother.md`, `L2/index.md`, `L3/index.md` [two occurrences on
  one file, lines 53 + 99]).
- **Kept-as-historical (1 light normalization): 1 pointer** (`L1/orthogonalize.md`);
  **2 pointers left untouched** (`L1-L0/triangular-solve-obstruction.md` :339 Related
  narrative + :533 frozen audit-YAML — both already document the cycle-097 deletion
  and "git history retains the slice"; striking the slug would damage the provenance
  record, same rationale the dispatch applies to `meta-reviews/`).
- **Surfaced (not edited — out of scope): 2 files** (`concepts/index.md`,
  `concepts/dependency-map.md`).

**Files touched by proposed-changes: 8.**

### Absorb-home facts established (for the repoints)
- GMRES L4 `inner_loop` body (former `gmres.md:459-471`) → firm L4 `krylov-step`
  Form A; L0 ground = `ksp-solve-mutation-rotation` §"Sub-pattern C — inner GMRES
  body" (`palace/linalg/iterative.cpp:543-705`); the firm L4>L3 home of the loop
  migration is `L4-L3/gmres-inner-loop-iterate-while-migration.md`.
- arnoldiStep monadic form (former `arnoldi_step.md:285-298`) → firm L4 `krylov-step`
  Form A; its orthogonalization constituent's L0 ground =
  `orthogonalize-mutation-rotation` (`palace/linalg/orthog.hpp:41-88` — full orthogonalization span: MGS `41-53` + CGS `57-74` + `refine` `75-88`).

## Recommendation
- **Apply these proposed-changes** (mechanical plaintext repoint/strike) via
  `integrator-per-report` — the firm absorb-homes already exist; this is tail cleanup,
  not authoring.
- **Dispatch `layer-intro-author` (next cycle) on the two concept-index files** —
  `concepts/index.md` + `concepts/dependency-map.md` carry pre-redirect
  orchestrator/slice-era framing (decommissioned `prompts/*` references,
  `concept_writes mode=create`, `spec/slices/*` grep recipes, ~40 Mermaid edges keyed
  on deleted slice-slug nodes `gmres`/`orthog`/`arnoldi_step`/`cg`/`gmres-L3`/`gmres-L4`).
  This is a **layer-intro/dep-map refresh**, not a residue micro-sweep — it needs the
  dep-map's node set re-derived against the live firm-chapter graph (and is a natural
  pairing with the graded-stack typed-edge campaign, priorities #0). Recorded under the
  migrated OQ `dependency-map-cg-precond-stale-mermaid-edges` (note: the OQ's literal
  `cg_preconditioning_framework` node premise is **inaccurate** — see Open questions).
- **Defer** the two `triangular-solve-obstruction.md` pointers — correctly historical.

## Proposed changes

### `book/src/L4/krylov-step.md` — repoint 2 bare dead-slice pointers
Lines 255-256 are the only entries in the "Four explicit L4 slice sections" list with
no absorb-home + no L0 (the CG entries above them already re-cite L0). Repoint to firm
home + L0.

```edit
FILE: book/src/L4/krylov-step.md
OLD:
  - `book/src/spec/slices/gmres.md:459-471` — GMRES L4 `inner_loop` body (Form A; Arnoldi-step + LS-update + counter-increment + convergence-test).
  - `book/src/spec/slices/arnoldi_step.md:285-298` — L4 `arnoldiStep` monadic form (Form A).
NEW:
  - GMRES L4 `inner_loop` body (Form A; Arnoldi-step + LS-update + counter-increment + convergence-test) — absorbed into this entry's Form A typing; L0 ground is [`ksp-solve-mutation-rotation`](../L1-L0/ksp-solve-mutation-rotation.md) §"Sub-pattern C — inner GMRES body" (`palace/linalg/iterative.cpp:543-705`), the loop-migration L4>L3 home being [`gmres-inner-loop-iterate-while-migration`](../L4-L3/gmres-inner-loop-iterate-while-migration.md). (Previously rendered in the now-deleted Phase-1 slice `gmres.md:459-471`, deleted cycle-099 graded-stack P2; git history is the record.)
  - L4 `arnoldiStep` monadic form (Form A) — absorbed into this entry's Form A typing; its orthogonalization constituent's L0 ground is [`orthogonalize-mutation-rotation`](../L1-L0/orthogonalize-mutation-rotation.md) (`palace/linalg/orthog.hpp:41-88` — the full orthogonalization span: MGS `41-53` + CGS `57-74` + the `refine` block `75-88`). (Previously rendered in the now-deleted Phase-1 slice `arnoldi_step.md:285-298`, deleted cycle-099 graded-stack P2; git history is the record.)
```

### `book/src/L4/chebyshev.md` — strike dead chebyshev §L4 path
```edit
FILE: book/src/L4/chebyshev.md
OLD:
  capability-typed sim-state, the initial-guess branch-vs-derived-view discussion)
  lived at the now-removed `book/src/spec/slices/chebyshev.md` §L4 (439-line form,
  `:287-439`); the slice was reduced and removed cycle-015 once its material became
  authoritative here (git history is the record per CLAUDE.md §Methodology
  invariants "Phase 1 corpus reduces as material is lifted"). The slice's `forM_`/`foldM` rendering of
NEW:
  capability-typed sim-state, the initial-guess branch-vs-derived-view discussion)
  was lifted from the cycle-001-era Phase-1 chebyshev §L4 (439-line form), reduced
  cycle-015 once its material became authoritative here and deleted cycle-099
  (graded-stack P2; git history is the record). The former §L4's `forM_`/`foldM` rendering of
```

### `book/src/L3/chebyshev.md` — strike dead chebyshev §L3 path
```edit
FILE: book/src/L3/chebyshev.md
OLD:
  obstructions, the what-lifts-vs-what-does-not table) lived at the now-removed
  `book/src/spec/slices/chebyshev.md` §L3 (439-line form, `:229-285`); the slice
  was reduced and removed cycle-015 once its material became authoritative here
  (git history is the record per CLAUDE.md §Methodology invariants "Phase 1
  corpus reduces as material is lifted").
NEW:
  obstructions, the what-lifts-vs-what-does-not table) was lifted from the
  cycle-001-era Phase-1 chebyshev §L3 (439-line form), reduced cycle-015 once its
  material became authoritative here and deleted cycle-099 (graded-stack P2; git
  history is the record per CLAUDE.md §Methodology invariants "Phase 1 corpus was
  lifted and deleted").
```

### `book/src/L2/chebyshev-iteration.md` — strike dead chebyshev §L2 path
```edit
FILE: book/src/L2/chebyshev-iteration.md
OLD:
- Provenance: the cycle-001-era §L2 slice content this entry promotes lived at
  the now-removed `book/src/spec/slices/chebyshev.md` §L2 (439-line form,
  `:122-228`); the slice was reduced and removed cycle-015 once its material
  became authoritative here (git history is the record per CLAUDE.md §Methodology
  invariants "Phase 1 corpus reduces as material is lifted").
NEW:
- Provenance: the cycle-001-era L2 content this entry promotes was lifted from the
  Phase-1 chebyshev §L2 (439-line form), reduced cycle-015 once its material became
  authoritative here and deleted cycle-099 (graded-stack P2; git history is the
  record per CLAUDE.md §Methodology invariants "Phase 1 corpus was lifted and
  deleted").
```

### `book/src/L1/chebyshev-smoother.md` — strike dead chebyshev §L1 path
```edit
FILE: book/src/L1/chebyshev-smoother.md
OLD:
- Provenance: the cycle-001-era §L1 slice content this entry promotes lived at
  the now-removed `book/src/spec/slices/chebyshev.md` §L1 (439-line form,
  `:34-116`); the slice was reduced and removed cycle-015 once its material became
  authoritative here, with the `rho_0` correction noted above (git history is the
  record per CLAUDE.md §Methodology invariants "Phase 1 corpus reduces as material
  is lifted").
NEW:
- Provenance: the cycle-001-era L1 content this entry promotes was lifted from the
  Phase-1 chebyshev §L1 (439-line form), reduced cycle-015 once its material became
  authoritative here (with the `rho_0` correction noted above) and deleted cycle-099
  (graded-stack P2; git history is the record per CLAUDE.md §Methodology invariants
  "Phase 1 corpus was lifted and deleted").
```

### `book/src/L2/index.md` — strike dead chebyshev innerStep path (absorb-home named in same cell)
```edit
FILE: book/src/L2/index.md
OLD:
    - `book/src/L4/chebyshev.md` §Semantics `innerStep` (firm cycle-015; absorbed the former `spec/slices/chebyshev.md:354-362`)
NEW:
    - `book/src/L4/chebyshev.md` §Semantics `innerStep` (firm cycle-015; absorbed the former Phase-1 chebyshev §L4 innerStep, deleted cycle-099; git history is the record)
```

### `book/src/L3/index.md` — strike two dead chebyshev paths (lines 53 + 99)
```edit
FILE: book/src/L3/index.md
OLD:
unblocked full reduction of the Phase-1 slice (`book/src/spec/slices/chebyshev.md`, removed cycle-015; material now authoritative across the firm `L1`–`L4` chebyshev cohort)) |
NEW:
unblocked full reduction of the Phase-1 chebyshev slice (reduced cycle-015, deleted cycle-099; material now authoritative across the firm `L1`–`L4` chebyshev cohort; git history is the record)) |
```

```edit
FILE: book/src/L3/index.md
OLD:
Landing this row + the L4 `chebyshev` row unblocked full reduction of the Phase-1 slice `book/src/spec/slices/chebyshev.md` (removed cycle-015; material now authoritative across the firm `L1`–`L4` chebyshev cohort).
NEW:
Landing this row + the L4 `chebyshev` row unblocked full reduction of the Phase-1 chebyshev slice (reduced cycle-015, deleted cycle-099; material now authoritative across the firm `L1`–`L4` chebyshev cohort; git history is the record).
```

### `book/src/L1/orthogonalize.md` — light normalization (already "(now-deleted)")
Already cites L0 directly and frames the slug as "(now-deleted)". Normalize the
remaining bare path to the standard git-history phrasing for consistency; no
re-citation needed.

```edit
FILE: book/src/L1/orthogonalize.md
OLD:
- **Provenance.** This firm L1 entry was the lift target of the (now-deleted) Phase-1 slice
  `spec/slices/orthog.md` (cycle-011 partial reduction → fully reduced and removed cycle-098,
  graded-stack P2 slice-deletion campaign). With this entry, the L2/L3/L4 dissections it
NEW:
- **Provenance.** This firm L1 entry was the lift target of the Phase-1 `orthog` slice
  (cycle-011 partial reduction → fully reduced and deleted cycle-098, graded-stack P2
  slice-deletion campaign; git history is the record). With this entry, the L2/L3/L4 dissections it
```

### NOT edited (kept-as-historical)
- `book/src/L1-L0/triangular-solve-obstruction.md:339` — Related narrative; already
  states "deleted in cycle-097 ... git history retains the slice." The inline-code
  slug is a load-bearing referent in a note that documents its own deletion. Leave.
- `book/src/L1-L0/triangular-solve-obstruction.md:533` — frozen audit-YAML `note`
  (`verdict: absorbed-and-deleted`, `audited_at: 2026-06-04`); a frozen record like
  git history. Leave.

## Supporting evidence
- Residue enumeration (16 `spec/slices/` plaintext hits, meta-reviews excluded):
  `grep -rnE 'spec/slices/' book/src --include=*.md | grep -v meta-reviews/`.
- Build-safety: the ONLY markdown links whose target contains `spec/slices/` are
  `book/src/concepts/index.md:42-43` (`[slice X](../spec/slices/X.md)` /
  `[slice Y](../spec/slices/Y.md)`), and both sit **inside** the ```` ```markdown ````
  fenced "Concept file format" example (fence opens line 27, closes line 47), so
  `linkcheck2` ignores them. Verified: `grep -roE '\]\((\.\./)*spec/slices/[^)]*\)'`
  returns only the X/Y placeholders.
- Baseline build green: `cargo make book` → "Build Done in 92.11 seconds"; the only
  warnings are pre-existing KaTeX "potential incomplete link" false-positives in
  `design/l4_calculus.md:142` (unrelated to this scope).
- Absorb-home L0 ranges:
  `book/src/L1-L0/ksp-solve-mutation-rotation.md:371-438` (Sub-pattern C, GMRES
  `Mult` `iterative.cpp:543-705`); `book/src/L1-L0/orthogonalize-mutation-rotation.md:74-151`
  (`orthog.hpp:41-88` — full orthogonalization span: MGS `41-53` + CGS `57-74` + `refine` `75-88`); firm theme `book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md`.
- Grep discipline: SOURCE-PATH exclusion form used throughout (`grep -v meta-reviews/`,
  `grep -v 'book/src/concepts/dependency-map.md:'`) — never link-target-text exclusion
  (the c098 grep bug); per skill `deleted-slug-inbound-live-link-sweep`.

## Open questions / caveats
- **Migrated-OQ premise correction.** The OQ `dependency-map-cg-precond-stale-mermaid-edges`
  describes "~22 stale Mermaid edges keyed off the deleted `cg_preconditioning_framework`
  node." That literal node does **not** exist in `concepts/dependency-map.md` — there is
  no `cg_preconditioning_framework` Mermaid node anywhere in `book/src`. The actual stale
  edges in `dependency-map.md` are keyed on the deleted **krylov-trio slice-slugs**
  (`gmres`, `orthog`, `arnoldi_step`, `cg`, `gmres-L3`, `gmres-L4`,
  `plane-rotation-stream`), ~40 edges across the L1/L2/L3/L4 sub-graphs. The
  `cg_preconditioning_framework` string survives only as **prose provenance** in three
  firm chapters (`concepts/rotation.md:136`, `L4/index.md:119`, `L4/preconditioning-framework.md:336`)
  where it correctly names the absorbed slice (c096) — those are accurate provenance, NOT
  residue. I recommend the next cycle-planner **re-scope this OQ** to "dependency-map.md
  legacy slice-slug Mermaid nodes" before dispatching the layer-intro-author follow-up.
- **Scope boundary.** I treated `concepts/index.md` + `concepts/dependency-map.md` as
  out-of-micro-sweep: their staleness is structural (whole-file orchestrator-era framing),
  not a few dead pointers, and `dependency-map.md` is wired into `SUMMARY.md:292` with an
  inbound citation from `L1-L0/minres-iteration.md:115` — a careful dep-map refresh, not a
  drive-by string-swap. If the integrator/planner prefers I fold a minimal
  `spec/slices/`-string strike into this dispatch anyway, that is a one-line judgment call;
  I erred toward not half-editing a legacy artifact that needs a coherent refresh.
- All eight edited files are firm chapters with no `integrated_at` constraint on the
  edited lines (provenance/evidence sections). The repoint links
  (`../L1-L0/...`, `../L4-L3/...`) all resolve to existing files — verified present.
