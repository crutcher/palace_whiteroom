---
agent: lowering-verifier
invoked_at: 2026-06-08T053000Z
scope: L3 kernel-impl↔kernel-api correspondence re-audit — eigsolve-impl-realizes-kernel-api-reaudit-lanczos (Hermitian inner-loop arm, coupled to the c139 lanczos advance)
status: integrated
integrated_at: 2026-06-08T165758Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-139 (batch-45 OPENER, 1/3). Audit-class FULLY-SUPPORTED; appended 8 verified_against: Hermitian-arm entries to book/src/L3/eigsolve-impl.md (195->227 lines; YAML round-trips clean, single top key, 16 entries; the 6 Palace anchors land EXACT); realizes-kernel-api stays reference-class, kernel-api L3/eigsolve stays partial-obstruction undowngraded. 0 NEW OQ."
inputs:
  - book/src/L3/eigsolve-impl.md (kernel-impl node, status roadmap_goal)
  - book/src/L3/eigsolve.md (kernel-api node, firmness partial-obstruction)
  - book/src/L3/lanczos_step.md (the Hermitian-arm constituent, status roadmap_goal on disk)
  - book/src/L1/index.md:202 (the lanczos_step dep-map row — coupled-citation cross-check)
  - reference/palace/palace/linalg/slepc.cpp:602-654, :687-709, :731-736
  - reference/palace/palace/linalg/arpack.cpp:315-339, :369
---

# CYCLE: Audit eigsolve-impl-realizes-kernel-api-reaudit-lanczos

## Summary

Re-audit of the DIRECTIVE-3 kernel-impl↔kernel-api correspondence between `book/src/L3/eigsolve-impl.md` (the `kernel-impl` node, `status: roadmap_goal`) and `book/src/L3/eigsolve.md` (the `kernel-api` node, `firmness: partial-obstruction`), focused on the **Hermitian inner-loop arm** the cycle-139 wave-1 lanczos advance touches. This is an audit-class dispatch — I author NO book content; I verify on-disk facts and append a `verified_against:` block.

**Top-level verdict: FULLY-SUPPORTED.** All four required integrity invariants hold on disk:
1. The `realizes-kernel-api` edge eigsolve-impl → eigsolve is **`reference`-class** (under `reference:` at `eigsolve-impl.md:19-21`, NOT `depends-on`). No mistype; no manufactured rank constraint.
2. The kernel-api `L3/eigsolve` **stays `partial-obstruction`, undowngraded** (`eigsolve.md:4` `firmness: partial-obstruction`; `:191` §Status carries the `kernel-api` role-label and the explicit "status is UNCHANGED" clause). The impl existing does not let us claim the opaque SLEPc/ARPACK boundary is implemented.
3. **No semantic restatement** — the impl LINKS authoritative semantics (`semantics/index.md` §1.2.1–§1.2.2 / §3.7 / §3.8 USED+linked at `eigsolve-impl.md:24,159`; the body laws referenced from the firm L2/L3 entries, not re-derived). The §"Correspondence to the kernel-API" table at `:102-109` cites the api by role/anchor, it does not copy the api's law text.
4. The impl's **Hermitian arm correctly references `lanczos_step` as a still-`roadmap_goal` constituent** — the correspondence is internally consistent with lanczos staying speculative; the `roadmap_goal → stub` promotion condition correctly does **not fire** this cycle.

One coupled-citation cross-check finding (non-defect, already addressed by the wave-1 D2 proposed changes): the eigsolve-impl on-disk `L1/index.md:179` citations (lines 129, 155) are **drifted** — the `lanczos_step` dep-map row is at `L1/index.md:202`, not `:179` (`:179` is `nleps_deflated_residual`). The c139 D2 advance's proposed `:179→:202` fix is **correct and confirmed against on-disk reality**; it applies at integration. Recorded here as confirmation, not a new finding (out of this audit's content-scope).

## Per-citation audit

- **Citation**: `book/src/L3/eigsolve-impl.md:19-21` (the `reference:` block, `realizes-kernel-api` edge to `L3/eigsolve`)
  - **Theme claim**: the impl realizes the kernel-api via a `reference`-class (free, non-blocking) edge that does NOT constrain rank or carry liveness.
  - **Found**: the edge sits under `reference:` (line 19), `target: L3/eigsolve` (line 20), `kind: realizes-kernel-api` (line 21) with an inline comment explicitly stating "reference-class (navigational, free — does NOT constrain rank, does NOT carry liveness; the impl does not block on the opaque API)." The sibling `realizes-kernel-api` → `L4/eigsolve` (lines 22-23) is likewise under `reference:`.
  - **Verdict**: supports.
  - **Notes**: DIRECTIVE-3 invariant-1 holds. There is NO `depends-on` edge to either the L3 or L4 kernel-api — a `depends-on` would mis-type the correspondence-for-review as a build dependency and rank-pin the impl to the obstruction. None present.

- **Citation**: `book/src/L3/eigsolve.md:4` + `:191` (kernel-api firmness/status)
  - **Theme claim**: the kernel-api stays `partial-obstruction`, undowngraded by the impl existing.
  - **Found**: `:4` `firmness: partial-obstruction`. `:191` §Status: "`partial-obstruction` — **`kernel-api`** (DIRECTIVE-3 role-label …) … The `partial-obstruction` status is UNCHANGED — the loop is genuinely opaque-library-owned; the impl constructs what the loop *would* be, it does not make this node's loop non-opaque." The opaque-library-ownership `sequential-obstruction` on the eigen-iteration loop is intact across §Semantics phase 2 (`:88-96`), §"Iteration-rotation marker" (`:119-126`), and the §"Algebraic laws" non-law list (`:144`).
  - **Verdict**: supports.
  - **Notes**: DIRECTIVE-3 invariant-2 holds. The claim-free obstruction discipline is preserved; the api documents the opaque boundary, makes no implemented-claim.

- **Citation**: `book/src/L3/eigsolve-impl.md:24, :159` (semantics links) + `:102-109` (correspondence table)
  - **Theme claim**: the impl USES + LINKS authoritative semantics and laws, it does not RE-STATE them.
  - **Found**: `:24` `reference: semantics/index` "§1.2.1–§1.2.2 named-shape-group convention; §3.7 iterate_while; §3.8 demand-pruning — USED + linked, not restated"; `:159` repeats the same link in §Evidence with "USED + linked, not restated". §Justification-kind (`:113-115`) defers the empirical-match (eigenpair-equality) audit to firming rather than asserting it. The correspondence table (`:102-109`) names api anchors per-row; it does not transcribe the api's law derivations.
  - **Verdict**: supports.
  - **Notes**: SEMANTIC-CONSOLIDATION USE+LINK-don't-restate discipline holds. No degenerate semantic-restatement smell.

- **Citation**: `book/src/L3/eigsolve-impl.md:11-12, :30, :81-84, :93` (the Hermitian arm) + `book/src/L3/lanczos_step.md:5`
  - **Theme claim**: the Hermitian/symmetric arm correctly references `lanczos_step` as its (still-`roadmap_goal`) constituent; the correspondence is internally consistent with lanczos staying speculative.
  - **Found**: `lanczos_step.md:5` `status: roadmap_goal` / `:6` `rank: roadmap_goal` ON DISK (the c139 wave-1 advance is in-place sharpening only — it did NOT promote lanczos off `roadmap_goal`). In eigsolve-impl: the `folds` `depends-on` to `L3/lanczos_step` (`:11-12`) is annotated "roadmap_goal co-cycle constituent; rank-0, may be rested on by this rank-0 node" — a well-founded rank-0-on-rank-0 edge per the graded-stack invariant. The body gate `if op.hermitian then lanczos_step … else krylov-step` (`:81-83`) and the problem-symmetry axis "hermitian = lanczos_step three-term recurrence, EPS_HEP/EPS_GHEP / non-hermitian = full arnoldi krylov-step" (`:30`) are mutually consistent. The band-3 collapse note (`:93`) and the orthogonalize-collapse note (`:154`) describe lanczos as a specialization, consistent with it being speculative.
  - **Verdict**: supports.
  - **Notes**: DIRECTIVE-3 invariant-4 holds. Because `lanczos_step` stays `roadmap_goal`, the impl's `roadmap_goal → stub` promotion condition (`:40`, `:136`) does NOT fire this cycle — confirmed; the impl correctly stays `roadmap_goal`.

- **Citation**: `reference/palace/palace/linalg/slepc.cpp:607` (EPS_HEP), `:613` (EPS_GHEP), `:635` (EPSKRYLOVSCHUR), `:694` (EPSSolve); `reference/palace/palace/linalg/arpack.cpp:318` (naupd), `:369` (neupd)
  - **Theme claim**: the impl's Hermitian-arm + opaque-loop anchors land at the cited lines.
  - **Found**: all six anchors return `1 ok, 0 failing` under `citecheck --anchor`. EPS_HEP/EPS_GHEP are the problem-symmetry tokens that select the `lanczos_step` arm; EPSKRYLOVSCHUR/EPSSolve/naupd/neupd are the opaque-loop anchors the impl reconstructs.
  - **Verdict**: supports.
  - **Notes**: zero drift on the Hermitian-arm-relevant Palace anchors.

## Applicability conditions

- **Condition**: "the `realizes-kernel-api` edge must be `reference`-class, not `depends-on`" (DIRECTIVE-3 every-batch integrity invariant).
  - **Verifiable**: directly from `eigsolve-impl.md` frontmatter — the edge is under `reference:` (line 19). Verified.
  - **Found counter-example?**: no.

- **Condition**: "the kernel-api stays `partial-obstruction`; the impl does not downgrade it."
  - **Verifiable**: `eigsolve.md:4` + `:191`. Verified — explicit "UNCHANGED" clause.
  - **Found counter-example?**: no.

- **Condition**: "the impl rests only on rank-≥0 deps; rank-0-on-rank-0 is well-founded."
  - **Verifiable**: the `lanczos_step` constituent is `roadmap_goal` (rank 0) and the impl is `roadmap_goal` (rank 0); `rank(u) ≤ rank(v)` holds with equality (0 ≤ 0). The firm deps (`krylov-step`, `ksp_solve`, `apply_linop`, `orthogonalize`) are rank-3, satisfying `0 ≤ 3`. Verified.
  - **Found counter-example?**: no — the theme's own rank (`roadmap_goal`) does not exceed `min(endpoint ranks)`. A `roadmap_goal` may rest on anything.

- **Condition**: "the impl's `roadmap_goal → stub` promotion fires only when a blocking `depends-on` consumer wires in AND `lanczos_step` materializes against positive structure."
  - **Verifiable**: `lanczos_step` is still `roadmap_goal` on disk → second clause unmet → promotion correctly does not fire. Verified. (The prior c124-D2 `verified_against` entry notes the first blocking consumer — `nleps-deflated-eigensolve` — already wired; but the second clause gates, so the impl stays `roadmap_goal`.)
  - **Found counter-example?**: no.

## Algebraic laws (if cited)

Not a law-bearing audit. The impl's body-composition correspondence (`apply_linop ▷ ksp_solve ▷ scale_untransform`, then `orthogonalize`) is a SPECULATIVE reconstruction flagged as such (`eigsolve-impl.md:54, :100`); the empirical-match (eigenpair-equality) audit is explicitly DEFERRED to firming (`:115`). No positive law claim is asserted that this audit must check — consistent with the impl being `roadmap_goal`. The kernel-api's own body laws (`eigsolve.md:128-151`) are syntactic identities on positive C++ source owned by the firm L2/L3 entries; the impl correctly does not restate them.

## Proposed changes

Append the `verified_against:` audit block to the kernel-impl chapter. This RE-AUDITS the Hermitian arm coupled to the c139 lanczos advance; it adds to (does not replace) the prior c122 + c124-D2 entries.

```edit:book/src/L3/eigsolve-impl.md
[append to the existing verified_against: YAML block — new entries, after the c124-D2 entry at line 194]
```yaml
verified_against:
  - citation: book/src/L3/eigsolve.md:189-195
    verdict: realizes-kernel-api-faithful
    audited_at: 2026-06-08T053000Z
    note: c139-wave2 re-audit of the Hermitian inner-loop arm. (1) realizes-kernel-api edge eigsolve-impl -> eigsolve CONFIRMED reference-class on disk (eigsolve-impl.md:19-21 under reference:, NOT depends-on); no mistype, no manufactured rank constraint. (2) kernel-api status STAYS partial-obstruction + kernel-api role-label (eigsolve.md:4 firmness, :191 Status); UNDOWNGRADED by the impl existing. (3) No semantic restatement -- impl LINKS semantics/index.md sec3.7/3.8 + the L2/L3 laws, does not re-state. (4) Hermitian arm internally consistent with lanczos staying roadmap_goal -- op.hermitian -> lanczos_step (eigsolve-impl.md:81-82), problem-symmetry axis EPS_HEP/EPS_GHEP -> lanczos_step (:30), folds depends-on rank-0-on-rank-0 well-founded (:11-12). Obstruction PRESERVED.
  - citation: book/src/L3/lanczos_step.md:5
    verdict: supports
    audited_at: 2026-06-08T053000Z
    note: lanczos_step on-disk status roadmap_goal / rank roadmap_goal (NOT advanced off roadmap_goal -- the c139 D2 advance is in-place sharpening only). Therefore eigsolve-impl roadmap_goal->stub promotion condition does NOT fire this cycle; impl stays roadmap_goal; rank-0-on-rank-0 dependency well-founded.
  - citation: reference/palace/palace/linalg/slepc.cpp:607
    verdict: supports
    audited_at: 2026-06-08T053000Z
    note: EPS_HEP lands exact (citecheck --anchor OK). The Hermitian problem-symmetry token that selects the lanczos_step three-term arm.
  - citation: reference/palace/palace/linalg/slepc.cpp:613
    verdict: supports
    audited_at: 2026-06-08T053000Z
    note: EPS_GHEP lands exact (citecheck --anchor OK). The generalized-Hermitian token, the second lanczos_step-selecting pencil.
  - citation: reference/palace/palace/linalg/slepc.cpp:635
    verdict: supports
    audited_at: 2026-06-08T053000Z
    note: EPSKRYLOVSCHUR lands exact (citecheck --anchor OK). The default opaque eigen-iteration algorithm the impl reconstructs (thick-restart driver).
  - citation: reference/palace/palace/linalg/slepc.cpp:694
    verdict: supports
    audited_at: 2026-06-08T053000Z
    note: EPSSolve lands exact (citecheck --anchor OK). The opaque library iteration the kernel-api records as un-renderable; the impl's outer driver is the constructed equivalent.
  - citation: reference/palace/palace/linalg/arpack.cpp:318
    verdict: supports
    audited_at: 2026-06-08T053000Z
    note: naupd lands exact (citecheck --anchor OK). The ARPACK RCI inner basis-extension driver, library-owned in Palace.
  - citation: reference/palace/palace/linalg/arpack.cpp:369
    verdict: supports
    audited_at: 2026-06-08T053000Z
    note: neupd lands exact (citecheck --anchor OK). The post-iteration eigenpair extraction the impl's rayleigh_ritz/extract_eigpairs realizes.
```
```

No content edits to either chapter are warranted by this audit — both nodes are correct as-is. The one stale-citation residue (`L1/index.md:179`) is already corrected by the c139 wave-1 D2 proposed changes (`:179→:202`); see §Open questions for the cross-check confirmation. Integration should ensure the D2 citation fix and this `verified_against` append land in the SAME cycle so the audit block and the corrected `:202` citation are consistent.

## Supporting evidence

- `book/src/L3/eigsolve-impl.md` — the kernel-impl node under audit (frontmatter edges `:7-27`; §Status `:134-136`; correspondence table `:102-109`; Hermitian arm `:81-84`; §Evidence verified_against `:161-195`).
- `book/src/L3/eigsolve.md` — the kernel-api node (`:4` firmness; `:191` §Status kernel-api role-label + UNCHANGED clause; §Semantics phase-2 opaque loop `:88-96`).
- `book/src/L3/lanczos_step.md:5-6` — the Hermitian-arm constituent, on-disk `roadmap_goal` (the gating fact).
- `book/src/L1/index.md:202` — the on-disk `lanczos_step` dep-map row (the corrected citation target); `:89` secondary mention; `:179` is `nleps_deflated_residual` (the drifted target eigsolve-impl currently cites).
- `tools/citecheck/citecheck.py --anchor` — clean `OK` on slepc.cpp:607/613/635/694 + arpack.cpp:318/369 (the Hermitian-arm + opaque-loop anchors).
- `reference/palace/palace/linalg/slepc.cpp:602-628` (problem-type tokens), `:630-654` (algorithm set), `:687-709` (Solve/EPSSolve); `arpack.cpp:315-339` (RCI loop), `:369` (neupd) — the opaque-loop sites the impl reconstructs and the api records as un-liftable.

## Open questions / caveats

- **COUPLED-CITATION CROSS-CHECK (confirmation, not a new finding).** The eigsolve-impl on-disk cites the `lanczos_step` rough-in row at `L1/index.md:179` (lines 129 and 155). On disk, the `lanczos_step` dep-map row is at **`L1/index.md:202`**; `:179` is the `nleps_deflated_residual` row. So the on-disk eigsolve-impl `:179` citation IS drifted. The c139 wave-1 D2 advance proposed exactly this fix (`:179→:202`) — **confirmed correct against on-disk reality**. No action needed from this audit beyond flagging that the D2 citation fix and this audit block should land in the same cycle (the integrator already serializes per-report; both target eigsolve-impl.md). Mechanically: `grep -n 'L1/index.md:179' book/src/L3/eigsolve-impl.md` → lines 129, 155; both are the `lanczos_step` row reference and both should read `:202`.
- **No promotion this cycle (correct).** The impl stays `roadmap_goal`; the `roadmap_goal → stub` condition is two-armed (blocking consumer AND lanczos-against-positive-structure) and the second arm is unmet while `lanczos_step` remains `roadmap_goal`. The eigsolve-impl firm flip + its wide cascade remain a future gated wave — nothing to queue here beyond noting the gate is correctly held.
- **Empirical-match deferred (correct).** The eigenpair-equality correspondence (impl computes the same eigenpairs as the opaque api, modulo the four non-determinism sources the L1 entry catalogs) is explicitly deferred to firming (`eigsolve-impl.md:115`). It is NOT auditable while the impl is `roadmap_goal` — this audit is the STRUCTURAL correspondence + edge-integrity check, which is the appropriate scope at rank 0.
- **RE11 disposition intact.** Per the kernel-API/impl audit guidance, a kernel-impl reaching root via its `realizes-kernel-api` `reference` edge is the INTENDED RE11 disposition; the prior c124-D2 entry already grounded the impl off the reference-only-reachable cohort via the `nleps-deflated-eigensolve` blocking consumer. No decay; no node to flag.
