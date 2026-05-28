---
agent: same-layer-cross-cutter
invoked_at: 2026-05-28T193754Z
scope: L-phase1-corpus cross-cut — chebyshev-phase1-slice-reduction
status: integrated
integrated_at: 2026-05-29T003000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-014 position 8/8 (final per-report). PARTIAL reduction of spec/slices/chebyshev.md (439→195 lines; §L1/§L2/§L3/Consumers/OQs/Concept-refs stubbed; §L4 calculus-form RETAINED verbatim; single H1 + single H2 ## L4 at line 43; start-boundary-trap gate cleared). NOT a corpus REMOVAL — slice persists as §L4-only; REMOVALS stay 8/10. Full removal GATED on cycle-015 (re-point krylov-step §L4 citations onto L4/chebyshev anchors + L4/chebyshev firming) via OQ chebyshev-slice-l4-full-removal; §L4 line ranges intentionally STALE-until-re-point. Build clean (slice renders; krylov-step §L4 inbound citations not consumed until gated removal batch)."
inputs:
  - book/src/spec/slices/chebyshev.md (audited slice; 439 lines)
  - book/src/L1/chebyshev-smoother.md (firm, cycle-012; Evidence block)
  - book/src/L2/chebyshev-iteration.md (firm, cycle-012; Evidence block)
  - book/src/L3/chebyshev.md (partial-obstruction, cycle-013; full read)
  - book/src/L4/chebyshev.md (rough-in, cycle-013; full read)
  - book/src/L1-L0/chebyshev-smoother-mutation-rotation.md (firm, cycle-013)
  - book/src/L2-L1/chebyshev-iteration-fusion.md (firm, cycle-013)
  - book/src/concepts/state-stratification.md:47-61 (four-stratum Chebyshev worked example)
  - book/src/concepts/derived-view-hoisting.md:21-43 (control-flow-boundary Chebyshev worked example)
  - book/src/L2/krylov-step.md (firm; cites slice §L4 line ranges as pattern-instance evidence)
  - book/src/spec/slices/cg_preconditioning_framework.md (§L4-retention precedent header)
  - reports/2026-05-28T193325Z-lowering-verifier-chebyshev-lowering-themes-lowering-verifier-followup/CYCLE.md (sibling: L1>L0 CONFIRMS-WITH-REFINEMENT, L2>L1 CONFIRMS)
skill_invoked: phase-1-slice-reduction-audit
---

# CYCLE: L-phase1-corpus observation — chebyshev slice reduction (partial)

## Summary

Audited `book/src/spec/slices/chebyshev.md` (439 lines, 8 H2 sections) against the
firm/landed chebyshev layered cohort (L1/L2 firm cycle-012; L3 partial-obstruction +
L4 rough-in cycle-013; L1>L0 + L2>L1 firm cycle-013 and confirmed by the sibling
cycle-014 lowering-verifier audit). All seven of the slice's substantive content
blocks are now **content-absorbed** by firm/landed entries — including the two
concept-page worked-example lifts (`state-stratification` four-stratum example,
`derived-view-hoisting` control-flow-boundary example) that the slice's own
reduction-status header (lines 10-14) listed as pending. **However, full reduction is
blocked by a citation-redirect dependency, not a content gap**: the firm `L2/krylov-step`
operator (a DISTINCT operator from the chebyshev cohort) cites five specific slice §L4 /
§L2 line ranges (`chebyshev.md:354-362`, `:330-353`, `:355-362`, `:308-323`, `:421-436`)
as canonical pattern-instance evidence; reducing/removing the slice would dangle those
firm-entry citations. Compounded by the `L4/chebyshev` entry being `rough-in` (its
`forM_`/`foldM` wrapper vocabulary is itself queued for a cycle-015 `iterate-while`
re-anchor). Verdict: **`partially-absorbed`** — reduce the slice's §L1/§L2/§L3 to
stub-and-pointer (those are fully redirectable to the firm cohort), **RETAIN §L4 verbatim**
until (a) the `krylov-step` citations re-point and (b) the L4 entry firms. This mirrors
the `cg_preconditioning_framework` §L4-retention precedent the dispatch named.

## Observation kind

**Variant-axis coverage gap** — specifically, a *slice-reduction-eligibility* gap: the
slice's content is fully covered by firm/landed entries, but the incoming-citation
surface (firm `krylov-step` → slice §L4 line ranges) is not yet redirected, and one
absorbing entry (`L4/chebyshev`) is `rough-in`. The residual is a citation-graph
dependency + a downstream-status dependency, not unlifted content.

## Specific finding

### Section-anchor table (step 1 — both ends verified via `grep -n "^## "` + `"^# "` + `"^### "`)

| Heading | start | end (next−1 / EOF) |
|---|---|---|
| `# Slice: chebyshev` (H1 + reduction-status header + intro prose) | 1 | 33 |
| `## L1` (State / Setup / Apply / Operator-kind) | 34 | 101 |
| `## Consumers` | 102 | 105 |
| `## Open questions` | 106 | 117 |
| `## Concept references (reduced)` | 118 | 121 |
| `## L2 — primitive composition` | 122 | 228 |
| `## L3 — tensor-field form (partial obstruction)` | 229 | 286 |
| `## L4 — calculus form` | 287 | 439 (EOF) |

(No mid-file intra-slice H1 — the only H1 is the title at line 1. The cycle-012
HIGH-severity START-boundary trap does not apply here; single-H1 slice.)

### Supersession map (step 2 — one row per section)

| Section | range | status | firm-entry pointer(s) |
|---|---|---|---|
| H1 header + intro | 1–33 | `full` | self-describing reduction header; collapses to stub front-matter. Intro prose → `L1/chebyshev-smoother.md` overview + `concepts/chebyshev-iteration.md`. |
| `## L1` | 34–101 | `full` | `L1/chebyshev-smoother.md` (firm) — Evidence block re-cites `chebyshev.cpp`/`.hpp` ranges INDEPENDENTLY (it cites `slices/chebyshev.md:34-116` only as "cycle-001-era content this entry promotes", i.e. provenance, redirectable to git history). |
| `## Consumers` | 102–105 | `full` | `L1/chebyshev-smoother.md` Evidence (`gmg.cpp:52-59`, `distrelaxation.cpp:21-36`) + `L1-L0/chebyshev-smoother-mutation-rotation.md` (consumer sites). |
| `## Open questions` | 106–117 | `full` | All three OQs (no unit test; spectrum_estimate backend; dead-code complex transpose kernels) are carried in `L1/chebyshev-smoother.md`, `L3/chebyshev.md` §Status caveat + §Variant axes, and the cycle-014 lowering-verifier audit (`:101-110,:150-159` dead-code recognition). |
| `## Concept references (reduced)` | 118–121 | `full` | Navigable via `concepts/index.md`; each concept page cited inline in the firm L1–L4 entries' Dependencies blocks. |
| `## L2 — primitive composition` | 122–228 | `full` | `L2/chebyshev-iteration.md` (firm) — §Semantics `sweep` IS this body; Evidence re-cites `chebyshev.cpp:215-217,:286-288` independently; cites `slices/chebyshev.md:122-228` as promotion provenance only. |
| `## L3 — tensor-field form` | 229–286 | `full` | `L3/chebyshev.md` (partial-obstruction) — Evidence cites `slices/chebyshev.md:229-285` as "the cycle-001-era §L3 this entry promotes"; the tensor-field body, both sequential obstructions, the what-lifts table are all transcribed. |
| `## L4 — calculus form` | 287–439 | `partial` (content absorbed; **citation-blocked + downstream-rough-in**) | `L4/chebyshev.md` (rough-in) transcribes the §L4 verbatim (its Evidence cites `slices/chebyshev.md:287-439`). BUT firm `L2/krylov-step.md` cites slice §L4 line ranges directly (see Residual gaps). |

### Residual gaps (step 3 — only the `partial` row)

The §L4 row (287–439) is the sole blocker to full reduction. Two distinct sub-blockers,
neither a content gap:

1. **Incoming firm-entry citations into slice §L4 line ranges (the load-bearing blocker).**
   The firm `L2/krylov-step` operator — which is NOT the chebyshev cohort, but factors
   chebyshev as one of its five canonical "kernel + driver" pattern instances — cites
   these slice line ranges:
   - `L2/krylov-step.md:7, :79, :85, :140` → `chebyshev.md:354-362` (the `innerStep` body / polynomial-recurrence kernel).
   - `L2/krylov-step.md:58` → `chebyshev.md:355-362` (the `op.scalars (k, scalar_state)` auxiliary stage).
   - `L2/krylov-step.md:118` → `chebyshev.md:308-323` (the `ChebOp<E, S>` type making the variant a type-level distinction).
   - `L2/krylov-step.md:148` → `chebyshev.md:330-353` (the `apply` with `forM_`/`foldM`).
   - `L2/krylov-step.md:77` → `chebyshev.md:421-436` (the derived-view treatment of `initial_guess`-as-control).
   - Also: `L2/index.md:35`, `L3/krylov-step.md:198,:206`, `L3/apply_linop.md:188`,
     `L3-L2/krylov-step-body-identity.md:127` all cite `chebyshev.md:354-362` / `:330-353`.
   These are firm-entry citations into §L4 line ranges. Reducing §L4 to a stub orphans
   them. **The fix is a citation re-point** (re-anchor `krylov-step`'s pattern-instance
   evidence onto `L4/chebyshev.md`'s `apply` / `innerStep` / `ChebOp<E,S>` anchors, which
   now carry the same material), sequenced BEFORE the §L4 stub. This is a `krylov-step`-side
   lifter/lowering edit, out of this audit's authority — surfaced as OQ.

2. **The `L4/chebyshev` entry is `rough-in`, not firm (downstream-status blocker).**
   Per the dispatch caveat: the L4 row's `forM_`/`foldM` wrapper iteration vocabulary is
   not anchored at L4 and competes with the firm `iterate-while` family; a cycle-014
   combinator-miner recommended re-expressing the bounded loops via `iterate_while_pure` /
   `iterate-while-with-prev`, with the firming re-anchor queued for cycle-015
   (`L4/chebyshev.md:400-419` §Status wrapper caveat). Until L4 firms, the slice §L4 is the
   most-stable detailed source for the `forM_`/`foldM` rendering that `krylov-step` cites.
   This is exactly the `cg_preconditioning_framework` situation (retain §L4 until the L4
   entry firms), EXCEPT chebyshev is one step further along: the L4 entry EXISTS and
   transcribes the content (cg_preconditioning_framework has no L4 entry at all).

**Not residual (resolved this audit):** the slice's reduction-status-header pending-lift
bullets 3–4 (extend `state-stratification` + `derived-view-hoisting` with the §L4 worked
examples) ARE done — `concepts/state-stratification.md:47-61` carries the four-stratum
Chebyshev example; `concepts/derived-view-hoisting.md:21-43` carries the control-flow-boundary
example. The header is stale on this point.

### Verdict

**`partially-absorbed`.** Reduce §L1 (34–101), §Consumers (102–105), §Open questions
(106–117), §Concept references (118–121), §L2 (122–228), §L3 (229–286) to a
stub-and-pointer; **RETAIN §L4 (287–439) verbatim** plus a thin retain-rationale header,
until the two §L4 sub-blockers close. **§L4 retention IS needed** (the explicit answer the
dispatch asked for).

## Recommendation

1. **Defer the full reduction; enact the partial reduction in a later cycle** via an
   integrator-applied proposed-changes block (this audit does not mutate `book/`). The
   partial-reduction proposed-changes are sketched below.
2. **Dispatch a lifter on `L2/krylov-step.md` (+ `L3/krylov-step.md`, `L3/apply_linop.md`,
   `L3-L2/krylov-step-body-identity.md`, `L2/index.md`) to re-point the
   `chebyshev.md:354-362 / :330-353 / :355-362 / :308-323 / :421-436` pattern-instance
   citations onto the now-firm-content `L4/chebyshev.md` anchors** (`apply`, `innerStep`,
   `ChebOp<E,S>`, the `initial_guess` derived-view §). Sequence this BEFORE the §L4 stub.
   This is the citation-redirect that unblocks §L4 removal. (`krylov-step`-side, not
   chebyshev-cohort-side — a clean cross-operator citation sweep, precedent: the cycle-014
   `lifter-krylov-step-typed-wrapper-dissolution-cg-md-citation-sweep` dispatch.)
3. **After the cycle-015 `L4/chebyshev` `iterate-while` re-anchor firms the L4 entry AND
   the krylov-step citations re-point, re-run this audit** to remove §L4 and complete the
   slice's full reduction (→ stub-and-pointer, then eventual delete per the monotonic-corpus-
   reduction invariant).
4. **Drop the stale pending-lift bullets 3–4 from the slice header** (the concept-page
   worked examples are landed) as part of the partial-reduction edit.

## Proposed changes (partial reduction — for a later integrator-per-report dispatch; NOT applied here)

Reduce the six fully-absorbed sections to stub-and-pointer; retain §L4 verbatim. Per the
skill's step-4 discipline, ranges derive from the step-1 anchor table; the §L4 START anchor
is the unique-text heading `## L4 — calculus form` (`grep -c` = 1, confirmed) so the retained
span is text-anchored, not line-number-anchored.

```edit:book/src/spec/slices/chebyshev.md
[REPLACE lines 1–286 (H1 header through end of §L3, i.e. from `# Slice: chebyshev`
 through the line immediately before `## L4 — calculus form` at line 287) with the
 stub below. RETAIN lines 287–439 (`## L4 — calculus form` through EOF) VERBATIM,
 prefixed by the retain-rationale note shown after the stub.]

~~~markdown
# Slice: chebyshev (reduced — §L1/§L2/§L3 absorbed; §L4 retained)

> **Reduction status (cycle-014+):** the §L1, §Consumers, §Open-questions, §L2, and
> §L3 content of this cycle-001-era slice is **fully absorbed** by the firm/landed
> chebyshev layered cohort and is reduced here to pointers. The §L4 "calculus form"
> below is **RETAINED verbatim** — see the retain-rationale note immediately above it.
>
> **Fully-absorbed sections (now pointers):**
> - **§L1** → `book/src/L1/chebyshev-smoother.md` (firm, cycle-012). Re-cites the
>   `palace/linalg/chebyshev.{cpp,hpp}` ranges independently.
> - **§Consumers / §Open-questions** → `L1/chebyshev-smoother.md` Evidence
>   (`gmg.cpp:52-59`, `distrelaxation.cpp:21-36`) + `L1-L0/chebyshev-smoother-mutation-rotation.md`
>   (consumer sites, dead-code complex-transpose recognition rules).
> - **§L2** → `book/src/L2/chebyshev-iteration.md` (firm, cycle-012) — §Semantics
>   `sweep` IS the §L2 primitive composition; `L2-L1/chebyshev-iteration-fusion.md`
>   (firm, cycle-013) is the upward fusion.
> - **§L3** → `book/src/L3/chebyshev.md` (partial-obstruction, cycle-013) — the
>   tensor-field body lifts; the inner `k`-recurrence + outer `pc_it` sweep are
>   witnessed sequential obstructions.
> - Concept worked-examples lifted: `concepts/state-stratification.md` §"fourth
>   stratum" and `concepts/derived-view-hoisting.md` §"Chebyshev initial-guess branch".
>
> **§L4 RETAINED (not yet removable):**
> - The §L4 `ChebOp<E,S>` / `apply`-as-`Solve`-monad form is transcribed into
>   `book/src/L4/chebyshev.md`, but that entry is `rough-in` (its `forM_`/`foldM`
>   wrapper vocabulary is queued for a cycle-015 `iterate-while` re-anchor), AND the
>   firm `book/src/L2/krylov-step.md` cites this slice's §L4 line ranges
>   (`:354-362`, `:330-353`, `:355-362`, `:308-323`, `:421-436`) as canonical
>   pattern-instance evidence. Full §L4 removal is gated on (a) re-pointing those
>   `krylov-step` citations onto the `L4/chebyshev.md` anchors and (b) the L4 entry
>   firming. OQ `chebyshev-slice-l4-full-removal`.
>
> _(§L4 START anchor `## L4 — calculus form` is a unique heading; the retained span is
>  text-anchored, stable under upstream edits.)_
~~~

[Then, immediately before the retained `## L4 — calculus form` heading, insert:]

~~~markdown
> **§L4 retain rationale (cycle-014):** retained verbatim because the firm
> `book/src/L2/krylov-step.md` (a distinct operator) cites the line ranges below
> (`:354-362` innerStep, `:330-353` apply, `:355-362` op.scalars, `:308-323`
> ChebOp<E,S>, `:421-436` initial-guess derived-view) and the absorbing
> `book/src/L4/chebyshev.md` is `rough-in`. Remove after the krylov-step citation
> re-point + L4 firming (OQ `chebyshev-slice-l4-full-removal`).
~~~
```

Note for the applying integrator: the §L4 line ranges that `krylov-step` cites
(`:354-362` etc.) are RELATIVE to the CURRENT (pre-reduction) file. The partial
reduction collapses §L1–§L3 (lines 1–286), so post-edit the §L4 content shifts upward
by the reduction delta — **the `krylov-step` citations MUST be re-pointed in the same
batch as this reduction is applied, or they will silently drift to wrong line ranges.**
This sequencing constraint is why recommendation 2 (re-point first) is load-bearing.

## Supporting evidence

- `book/src/spec/slices/chebyshev.md` — section-anchor enumeration (`grep -n "^## "`
  → 7 H2 at 34/102/106/118/122/229/287; `grep -n "^# "` → single H1 at line 1;
  `wc -l` = 439). Both boundaries of every section verified.
- `book/src/L1/chebyshev-smoother.md:341` — Evidence cites `slices/chebyshev.md:34-116`
  as "cycle-001-era L1 slice content this entry promotes" (provenance, redirectable) +
  independent `gmg.cpp:52-59` / `distrelaxation.cpp:21-36` consumer cites.
- `book/src/L2/chebyshev-iteration.md:264-267` — Evidence cites `slices/chebyshev.md:122-228`
  as promotion provenance + independent `chebyshev.cpp:215-217,:286-288` cites.
- `book/src/L3/chebyshev.md:520-523` §Evidence — cites `slices/chebyshev.md:229-285` as
  "the cycle-001-era §L3 this entry promotes"; full tensor-field body + both obstructions
  + what-lifts table transcribed (partial-obstruction status, lines 429-448).
- `book/src/L4/chebyshev.md:468-472` §Evidence — cites `slices/chebyshev.md:287-439` as
  "the cycle-001-era §L4 calculus form this entry promotes"; §Status (400-419) carries the
  `rough-in` wrapper caveat (forM_/foldM not anchored; cycle-015 iterate-while re-anchor queued).
- `book/src/L2/krylov-step.md:7,:58,:77,:79,:85,:118,:140,:148` — the firm-entry incoming
  citations into slice §L4/§L2 line ranges (the load-bearing reduction blocker).
- `book/src/concepts/state-stratification.md:47-61` + `book/src/concepts/derived-view-hoisting.md:21-43`
  — the two §L4 worked-example lifts, CONFIRMED landed (resolves slice-header pending bullets 3-4).
- `book/src/spec/slices/cg_preconditioning_framework.md` reduction-status header — the
  §L4-retention precedent (fully-absorbed sections collapse; §L4/§L4-v0.2/§L4-v0.3
  RETAINED as load-bearing unique material pending an L4 entry). Chebyshev is one step
  further: its L4 entry exists but is rough-in + citation-blocked.
- Sibling cycle-014 audit `reports/2026-05-28T193325Z-lowering-verifier-chebyshev-lowering-themes-lowering-verifier-followup/CYCLE.md`
  — L1>L0 CONFIRMS-WITH-REFINEMENT, L2>L1 CONFIRMS; both lowering themes firm and
  citation-grounded, so the §L1/§L2/§L3 reduction relies on confirmed-firm lower-edge
  rotations.

## Open questions / caveats

- **OQ `chebyshev-slice-l4-full-removal`** (NEW): the slice's §L4 (lines 287–439) cannot
  be removed until (a) the firm `L2/krylov-step` (+ `L3/krylov-step`, `L3/apply_linop`,
  `L3-L2/krylov-step-body-identity`, `L2/index`) citations into `chebyshev.md:354-362 /
  :330-353 / :355-362 / :308-323 / :421-436` are re-pointed onto the `L4/chebyshev.md`
  anchors, AND (b) the `L4/chebyshev` entry firms (cycle-015 `iterate-while` re-anchor).
  Recommend a lifter dispatch on `krylov-step` for the citation re-point (item 2),
  sequenced before any §L4 stub. Route the §L4 removal to a re-run of THIS audit
  post-cycle-015.
- **Sequencing hazard (load-bearing).** The §L4 line ranges `krylov-step` cites are
  relative to the current file. If the partial reduction (collapsing §L1–§L3) lands
  WITHOUT re-pointing the `krylov-step` citations in the same batch, those citations
  drift to wrong content (the §L4 shifts upward by the reduction delta). Either re-point
  first (preferred) or defer the entire partial reduction until the citation re-point is
  ready. Flagged so the integrator does not apply the §L1–§L3 collapse in isolation.
- **`L1/chebyshev-smoother.md:343` `rho_0` correction note** + **`L2/chebyshev-iteration.md:260`
  slice §L2 line-160 `delta/(2·theta)` error note**: the firm entries explicitly flag that
  the slice §L1/§L2 carry small transcription errors corrected in the firm entries. This
  is additional evidence the firm entries are AUTHORITATIVE over the slice §L1/§L2 (the
  slice is provenance, not ground truth) — reinforces the `full` supersession verdict for
  those sections.
- **`spec/index.md:19` + `SUMMARY.md:100`** carry slice-level metadata / TOC entries that
  the partial reduction does not invalidate (the slice file persists, just reduced). Full
  removal (later cycle) would require updating both — note for the eventual removal dispatch.
- **Did NOT mutate `book/`** (per dispatch discipline). The proposed-changes block above is
  a sketch for a later integrator-per-report dispatch, gated on the OQ resolution.
- **No `partly-constructive` / negative-anchor reasoning involved** — this is a pure
  citation-graph + downstream-status reduction-eligibility audit; no reconstruction claims.
