---
agent: lifter
invoked_at: 2026-05-29T18:02:38Z
scope: L2 ksp_solve §Semantics materialise_iterate cite-tightening — re-anchor the restart-correction forward-reference to the now-firm L2 incremental-least-squares operator
status: integrated
integrated_at: 2026-05-29T21:15:00Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-027 finalize. 2 surgical cite/cross-ref upgrades in L2/ksp_solve.md (both ends firm same-layer L2, no forward-edge): Edit-1 §Dependencies :123 plain-text incremental-least-squares → live link [incremental-least-squares](./incremental-least-squares.md), 'queued'→'firm', correction-shape K.y→V·y/Z·y; Edit-2 §Semantics phase-3 :83 added live-link cross-reference resolving the K.V·K.y correction story to the firm operator's back_solve output. Surfaced NEW c028 OQ l2-incremental-least-squares-self-description-still-says-queued-after-firming (the producer entry incremental-least-squares.md:13 still self-describes as 'queued ... motif' despite status:firm — out of this report's one-operator scope). retroactive-budget 0; clean build; live links resolve (target on-disk firm)."
inputs:
  - book/src/L2/ksp_solve.md
  - book/src/L2/incremental-least-squares.md
---

# CYCLE: Re-anchor ksp_solve §Semantics materialise_iterate → firm L2 incremental-least-squares

## Summary
The L2 `ksp_solve` driver (`book/src/L2/ksp_solve.md`, firm) describes its
§Semantics phase-3 `materialise_iterate` as folding the restart-cycle correction
`K.V · K.y` (GMRES) / `Z·y` (FGMRES) into the running iterate `s.x`, and its
§Dependencies row names the running-QR / Givens stream that *produces* that
correction. At authoring time (cycle-021) that producing composition was only a
**queued** L2 candidate, so both references are plain-text (a backtick-only
`incremental-least-squares` mention in §Dependencies, and no link at all in the
§Semantics phase-3 prose). The L2 `incremental-least-squares` operator firmed on
disk in cycle-026 (`book/src/L2/incremental-least-squares.md`, `status: firm`),
and its own §Consumers / §Status / §Evidence already point back at this exact
`materialise_iterate` site. This is a **pure cite/cross-ref upgrade**: the
structure, semantics, signature, laws, and variant axes of `ksp_solve` are
unchanged. Two edits — (1) §Dependencies: the plain-text "queued
`incremental-least-squares`" becomes a live link with the now-stale "queued"
qualifier dropped; (2) §Semantics phase-3: the `materialise_iterate` description's
`K.V · K.y` / `Z·y` correction story gains a live-link cross-reference to the firm
producing composition, so the restart-correction provenance resolves under
`linkcheck2`. No L0 line-citation is restated — only book-internal relative
cross-references are added.

## On-disk verification (not already-satisfied)
- `book/src/L2/ksp_solve.md:123` (§Dependencies) — current text: ``...and the queued
  `incremental-least-squares` (the GMRES running-QR / Givens stream that produces the
  restart-cycle correction `K.y`)...``. This is a **backtick-only plain-text mention**
  (`incremental-least-squares`), NOT a live `[...](...)` link, and it carries the now-
  stale "queued" qualifier. Confirmed via grep (single occurrence on line 123).
- `book/src/L2/ksp_solve.md:83` (§Semantics phase-3 "Final-iterate materialisation")
  — current text names the correction `K.V · K.y` but contains **no reference** (plain-
  text or link) to the producing composition; it cross-links only `krylov-step` and
  `solve-monad`. Confirmed via grep (single occurrence of the `materialise_iterate`
  phase prose on line 83).
- Neither site is already a live link → **not already-satisfied**; the upgrade is live.
- `book/src/L2/incremental-least-squares.md` exists on-disk (`status: firm`, cycle-026)
  with H1 `# incremental-least-squares` (line 1) → the relative link
  `./incremental-least-squares.md` resolves under `linkcheck2`. Confirmed via `ls`.
- Link style matched to the existing same-dir L2 cross-references in this file (e.g.
  ``[`orthogonalize`](./orthogonalize.md)`` at line 123, ``[`krylov-step`](./krylov-step.md)``
  throughout): backticked slug + `./<slug>.md` relative target.

## Proposed changes

```edit:book/src/L2/ksp_solve.md
[old]: - L2 named compositions appear only *transitively* through the kernel: [`orthogonalize`](./orthogonalize.md) (the `op.orthog` surface, present for GMRES/FGMRES) and the queued `incremental-least-squares` (the GMRES running-QR / Givens stream that produces the restart-cycle correction `K.y`) are folded by `krylov-step`, not called directly by the driver.
[new]: - L2 named compositions appear only *transitively* through the kernel: [`orthogonalize`](./orthogonalize.md) (the `op.orthog` surface, present for GMRES/FGMRES) and [`incremental-least-squares`](./incremental-least-squares.md) (the firm GMRES/FGMRES running-QR / Givens stream that produces the restart-cycle correction `V·y` / `Z·y`) are folded by `krylov-step`, not called directly by the driver.
```

```edit:book/src/L2/ksp_solve.md
[old]: 3. **Final-iterate materialisation** (`materialise_iterate`). For non-restarted methods (CG, Chebyshev) the running iterate `s.x` is updated in-kernel each step, so `materialise_iterate` is identity (the terminal `s_n.x` is already correct). For restarted methods (GMRES, FGMRES) the externally-visible iterate is folded in once per restart cycle from the basis correction `K.V · K.y`; `materialise_iterate` folds the last partial restart-cycle's correction into `s.x`. This "iterate folded at restart boundaries, not per step" placement is the same the [`krylov-step`](./krylov-step.md) §Semantics restart discussion and [`solve-monad`](../concepts/solve-monad.md) §"Worked example — GMRES" describe.
[new]: 3. **Final-iterate materialisation** (`materialise_iterate`). For non-restarted methods (CG, Chebyshev) the running iterate `s.x` is updated in-kernel each step, so `materialise_iterate` is identity (the terminal `s_n.x` is already correct). For restarted methods (GMRES, FGMRES) the externally-visible iterate is folded in once per restart cycle from the basis correction `K.V · K.y`, the `back_solve` output of the firm [`incremental-least-squares`](./incremental-least-squares.md) running-QR composition (the coordinate vector `y` reconstructed against the basis `V`/`Z`); `materialise_iterate` folds the last partial restart-cycle's correction into `s.x`. This "iterate folded at restart boundaries, not per step" placement is the same the [`krylov-step`](./krylov-step.md) §Semantics restart discussion and [`solve-monad`](../concepts/solve-monad.md) §"Worked example — GMRES" describe.
```

[No status-line change: `ksp_solve` is already `firm` and stays `firm`. No
signature/semantics/laws/variant-axis change — the body composition, the four
phases, the predicate, and the result extraction are untouched. The `back_solve`
term used in the new §Semantics prose is the firm `incremental-least-squares`
operator's own terminal-projection name (its §Signature line 81–83), so the
cross-reference is self-consistent with the target entry.]

## Discipline notes
- **Pure cite/cross-ref upgrade**, per the lifter role-spec "Touch evidence pointers
  only when re-anchoring a citation that broke" / "firm up the vocabulary". A
  forward-reference that was correctly plain-text under the
  `rough-in-forward-reference-must-be-plain-text-not-live-link` convention (the target
  did not exist at cycle-021 authoring) is now upgradeable to a live link because the
  target firmed on-disk (cycle-026). This is the
  `upgrade-plain-text-ref-to-live-link-when-target-on-disk` situation (skill, cycle-024):
  on-disk firm target → live link.
- **"queued" qualifier dropped** in the §Dependencies edit: the word described the
  pre-cycle-026 maturity state ("queued second named-composition motif", echoing the
  target entry's own pre-firm self-description) and is now factually stale — the
  operator is firm. Dropping it and saying "firm" is a bounded, L0-of-the-artifact-
  evidenced prose correction (the target's `status: firm` frontmatter is the evidence),
  within the cycle-012 `lifter-scope-content-correction-boundary` allowance: it fixes a
  drifted/stale claim, is bounded (one qualifier word + a link), and is recorded here.
- **`K.y` → `V·y` / `Z·y` correction-shape tightening** in the §Dependencies edit:
  the old prose said the stream "produces the restart-cycle correction `K.y`", but the
  externally-visible correction is the basis-times-coordinates product `V·y` (GMRES) /
  `Z·y` (FGMRES) — `y` is the back-solved coordinate vector, not the correction itself.
  This matches the target entry's §Signature `correction_basis · y` (line 131) and its
  §Semantics `x += Σ_k s[k]·V[k]` / `x += Σ_k s[k]·Z[k]` (`iterative.cpp:666` / `:843`),
  and is already the exact wording used in this same file's §Semantics phase-3
  ("basis correction `K.V · K.y`", line 83). Bounded terminology alignment with the
  firm target + this file's own phase-3 prose; no structural change.
- **No L0 line-citation restated.** Both edits add only book-internal relative
  cross-references (`./incremental-least-squares.md`). The `V·y` / `Z·y` / `back_solve` /
  `y` vocabulary is sourced from the firm target entry's own signature/semantics, not
  newly asserted against `reference/palace/`. Hence no `--anchor` run is applicable to
  this dispatch's edits (there is no new `path:lo-hi` pinpoint to verify); the
  `--scan` path-hygiene/bounds check on this CYCLE.md is the relevant gate.
- High→low discipline preserved: the edits stay in L2 vocabulary (the L2 driver
  consuming the L2 named composition); no L3/L4 vocabulary introduced, no lift-direction
  prose added to the chapter.

## Supporting evidence
- `book/src/L2/incremental-least-squares.md` — the firm (cycle-026) producing
  composition. Its §Consumers (`ksp_solve` — "§Semantics phase-3 `materialise_iterate`
  folds the last partial restart cycle's correction `V·y` / `Z·y` … into the running
  iterate `s.x`", lines 329–332), §Status (names "[`ksp_solve`](./ksp_solve.md)
  `materialise_iterate` consumes", lines 381–382), and §Evidence (back-link to
  `book/src/L2/ksp_solve.md` §Semantics phase-3 `materialise_iterate` `:63`, `:83`,
  lines 507–509) already point at the two sites this dispatch upgrades — the
  cross-reference is now bidirectional + live.
- `book/src/L2/ksp_solve.md:63`, `:83`, `:123` — the three on-disk `materialise_iterate`
  / `incremental-least-squares` mention sites (signature body, §Semantics phase-3,
  §Dependencies). Lines 83 and 123 are the two upgraded here; line 63 is the inline
  signature comment (`-- fold restart-cycle correction into s.x (identity for CG)`),
  which carries no slug reference and needs no change.
- OQ `l2-ksp-solve-materialise-iterate-incremental-least-squares-cite-tightening`
  (marked NOW-ACTIONABLE in cycle-026 integrator-signals) — the dispatch trigger.

## OQ disposition
- **Close** OQ `l2-ksp-solve-materialise-iterate-incremental-least-squares-cite-tightening`.
  The forward-reference is upgraded to a live link at both the §Dependencies and
  §Semantics phase-3 sites; the firm L2 `incremental-least-squares` target resolves
  under `linkcheck2`. No residual: this was the last plain-text mention of the
  composition from the `ksp_solve` driver (the signature comment at line 63 carries no
  slug). The integrator-per-report applying this report should mark the OQ closed.

## Open questions / caveats
- None blocking. The firmed-up `incremental-least-squares` signature does NOT
  contradict what `ksp_solve` §Semantics phase-3 assumed: the target's §Signature
  terminal projection `back_solve :: LsqState' -> { y, correction_basis }` and its
  reconstruction `correction_basis · y` (`V·y` / `Z·y`) is exactly the `K.V · K.y` /
  `Z·y` correction the `ksp_solve` phase-3 prose names. No LHS/RHS shape shift, no
  applicability-condition change → a pure lift (no abstractor reread needed).
- **Fan-out unblocked:** this live cross-link closes the producer→consumer reference
  for the restart-correction machinery, which is the connective tissue the downstream
  GMRES/FGMRES restart-machinery and `krylov-step` re-closure work depends on — those
  passes can now navigate `ksp_solve` §Semantics phase-3 → firm `incremental-least-squares`
  `back_solve` directly rather than chasing a plain-text "queued" mention. Noted for
  the planner's fan-out ranking.
- The §Dependencies parenthetical now says "firm GMRES/FGMRES running-QR" (was "GMRES
  running-QR"); the FGMRES arm was already implicit in this file (the solver-method
  axis lists FGMRES) and is explicit in the target entry's `op.basis_kind = Z` axis, so
  this is alignment, not a new claim.
