---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T071500Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
---

# META: verification of "L2>L1 + L3>L2 theme sketches — divfree-projector adjacent lowering edges"

## Critique

### Checks run

**citation-validity — pass.** `citecheck.py --scan` returned 14 ok / 0 failing (bounds + path hygiene clean). Every load-bearing pinpoint was anchor-verified mechanically: `divfree.cpp:185 --anchor AddMult` → `[185]`; `:177-186 --anchor AddMult` → `[180,181,185]` (matching the claimed complex Re/Im `:180-181` + real `:185`); `:175 --anchor ksp` → `[175]`; `:171-174 --anchor SetSubVector` → `[173]`; `:155-187 --anchor Mult` → `[155,162,163,167,175,180,181,185]`; `divfree.hpp:28-31 --anchor 'M x'` → `[29]` (the `Gᵀ M x = 0` class doc). The `krylov-step-body-identity.md:97 --anchor L3-native` self-cite resolved `[97]`. I also read `divfree.cpp:155-187` directly: step 1 `WeakDiv->Mult` (:162-163 complex / :167 real), step 2 `SetSubVector(rhs,...,0.0)` (:173), step 3 `ksp->Mult(rhs, psi)` (:175), step 4 `Grad->AddMult(psi,y,1.0)` (:180-181 complex / :185 real) — the four-step body is faithful to both theme bodies. The report carries no `verified_against:` YAML block (its "Verified-against" sections are plain prose lists, not a fenced/indented YAML payload), so the round-trip sub-check is not applicable.

**surface-or-evidence — pass.** Both proposals are `new:` theme chapters (net-new surface), not refinements of existing themes, so this is fresh-surface authoring with rotation/identity evidence attached, not a pure rotation_claim backfill. The L2>L1 theme states a genuine rotation with positive Palace evidence; the L3>L2 theme states an identity-in-form mapping with both-endpoints-isomorphic evidence. Surface present, evidence present.

**rotation-quality — pass.** The L2>L1 theme asserts exactly one genuine rotation: the L2 floor's de-fused `axpy(1.0, apply_linop(P.Grad, ψ), y)` re-fuses, lowering forward, into the single fused `Grad->AddMult(ψ, y, 1.0)`. This is a value-preserving kernel-fusion (state/intermediate hiding — the `g = P.Grad · ψ` materialization is re-absorbed), the canonical L2>L1 fusion-rotation content per the strawman conventions; it is NOT a rename or 1:1 mapping. The L3>L2 theme is explicitly identity-in-form (not claimed as a rotation) — appropriate for a fixed four-step composition explicit at both layers; the report correctly routes the one fusion to the L2>L1 edge and keeps L3>L2 pure-identity, avoiding a fake rotation. Both pass.

**variant-axis-coverage — pass.** The report scopes the variant axes explicitly: the element-type (real/complex) and operator-representation axes are absorbed into the opaque `DivFreeProjector` closure (stated in the L3>L2 §"L3 form"), and the in-place / out-of-place + destination-buffer axis is scoped to the L1>L0 mutation-rotation edge (L2>L1 §"L2 form (LHS)" — "pure / out-of-place … reappear only at the L1>L0 lowering"). The complex Re/Im step-4 branches (`:180-181`) and the real branch (`:185`) are both cited, so the element-type axis is covered at the rotation site, not hidden. No hidden branch.

**cross-reference-integrity — pass (one expected co-land dependency, not a defect).** All non-target cross-references resolve on disk: `L1/divfree-projector.md`, `L3/divfree-projector.md`, `L2/ksp_solve.md`, `L1/apply_linop.md`, `L1/axpy.md`, `L2-L1/dot-leaf-identity.md`, `L3-L2/dot-body-identity.md`, `L3-L2/krylov-step-body-identity.md`, the `nrm2/scal -body-identity` and `-fold-specialization` siblings, `L1-L0/divfree-projector-mutation-rotation.md`, and concepts `sequential-obstruction.md` + `nested-constructed-operator-gate.md` all exist. The four `edit:` insert anchors all resolve (SUMMARY rows `dot-body-identity`@43 / `eigsolve-spectral-transform-composition`@76; L2-L1 index `eigsolve-spectral-transform-composition`@22; L3-L2 index `scal-body-identity`@17). The single MISS is `book/src/L2/divfree-projector.md` (the D6 wave-1 floor) — both themes presuppose it as the co-landing LHS/RHS, the report declares this explicitly ("lands at this cycle's integration alongside this theme — wave-2 serial sequencing applies D6 before this theme"), so it is an integration-ordering dependency, not a dangling link. The fence-enclosure guard: 12 fences / 6 balanced blocks, both `## Status` lines (report :301, :551) sit INSIDE their `new:` fences (48–332, 334–583); the firm apparatus (Status + Signature + rewrite table + Verified-against) is enclosed. No fence-truncation defect.

**edge-label-fidelity — pass.** The L2>L1 theme's prose discusses exactly the L2→L1 edge: the rewrite table maps `L2/divfree-projector` rows to `L1/divfree-projector` rows, narrated forward (high→low), with the one re-fusion lowering L2's de-fused pair into L1's fused call. The L3>L2 theme's prose discusses exactly the L3→L2 edge (L3 gate → L2 floor, forward). Neither edge's prose drifts to the wrong pair; the step-4 fusion is correctly assigned to the L2>L1 edge in BOTH themes (the L3>L2 theme repeatedly defers it downward), which is the load-bearing edge-label discrimination here. Both narrate high→low per the "Layers are defined high→low" invariant; the reverse lift-direction material is correctly quarantined to §"Open questions / caveats" working notes, not the chapter bodies.

**plan-kind-consistency — pass.** Both entries declare `## Status: firm` and are theme-shaped (LHS form / RHS form / rewrite table / applicability conditions / justification kind / verified-against). The firm claim is justified: both endpoints are existing firm or firming-this-cycle vocabulary, the rotation/identity reads off positive Palace source with no negative-anchor reconstruction or literature inference, and no rough-in placeholders are present. The one genuine rotation (L2>L1) and the pure identity (L3>L2) are each content-shape-consistent with their declared kind.

**skill-uptake-survey — pass.** The report references `tools/citecheck/citecheck.py --anchor` invocation for all load-bearing L0 anchors (§"Supporting evidence" enumerates the anchor results), the realization of the `verify-citation-range` mechanical sub-check; it cites the `dot-leaf-identity` / `dot-body-identity` slug precedents and the `krylov-step-body-identity:97` structural template. Telemetry present; no blocking concern.

### Issues found

No blocking issues. Three observations, all informational / already-flagged-by-the-report (candidates for the repairer/integrator to note, none requiring content change at this edge):

1. **Co-land dependency on `L2/divfree-projector.md` (D6).** (`CYCLE.md` §"Verified-against" both themes, §Summary.) Both themes' LHS (L2>L1) / RHS (L3>L2) is the D6 wave-1 L2 floor, which does not yet exist on disk. The report declares the serial sequencing (D6 applies before these themes). Severity: low — this is an integration-ordering constraint the integrator must honor (apply D6 first, or the two new themes' relative links to `../L2/divfree-projector.md` will dangle at build). Not a report defect; surfaced so the integrator sequences correctly.

2. **Stale assertion in the firm L3 entry, correctly deferred.** (`CYCLE.md` §"Open questions / caveats" bullet 2.) `book/src/L3/divfree-projector.md:92-93` still asserts "`book/src/L2/divfree-projector.md` does not exist … no `L3-L2/divfree-projector-identity` theme" — these become stale once D6 + this `divfree-projector-body-identity` land. The report correctly flags this as a downstream-consistency touch on a firm L_n entry, OUT of abstractor write-authority, deferred to a lifter/harvester/integrator pass. Severity: low / informational — correctly NOT applied here; flagged so it is not lost.

3. **Count-ownership deferred to D11.** (`CYCLE.md` §"Supporting evidence" final bullet.) The report appends only the two theme rows + two SUMMARY registrations + two bodies, and explicitly does NOT touch the consolidated index tallies (L2-L1 "firm 7→10", L3-L2 "firm 2→5 / 5-of-18", cohort-growth-log). This respects the count-ownership partition (D11 owns tallies this cycle). Severity: none — correct behavior, noted for the integrator so the parallel-blind count is reconciled by the tally-owner, not double-counted.

---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T071500Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-01T073000Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

## Repair

### Fixes attempted

All 8 critic checks returned `pass`. The critic recorded no blocking issues — only three observations, each self-flagged by the report itself as an integration-ordering / deferred-touch / count-ownership note. None names a defect in the report content; none falls in repair authority (no missing citation, no off-by-N range, no dep-map gap, no broken link, no SIDEWAYS rewrite, no edge-label flip). No edits applied to CYCLE.md or supporting docs.

The three observations are integrator-facing, not repairer-facing:

- **Finding 1 — Co-land dependency on `L2/divfree-projector.md` (D6).**
  - **Decision**: not-needed (informational; integration-ordering constraint, not a report defect).
  - The MISS is the D6 wave-1 L2 floor not yet on disk. The report already declares the serial sequencing (apply D6 before these two themes). A repairer cannot create `book/src/L2/divfree-projector.md` (artifact write, out of authority) and would not — it is supplied by D6's own report. Surfaced to the integrator below as a sequencing note.

- **Finding 2 — Stale assertion in firm L3 entry (`L3/divfree-projector.md:92-93`), correctly deferred.**
  - **Decision**: not-needed (informational; correctly deferred by the report, out of abstractor authority — and out of repairer authority, which does not modify the artifact).
  - This is a downstream-consistency touch on a *firm L_n entry* in `book/`. Editing it is artifact mutation (forbidden to the repairer) AND it requires deciding the post-co-land wording — that is substantive, not mechanical. Routed below as a follow-up OQ for a lifter pass.

- **Finding 3 — Count-ownership deferred to D11.**
  - **Decision**: not-needed (correct behavior; the report deliberately omits tally touches per the count-ownership partition).
  - Nothing to repair — the omission is the intended behavior. Noted for the integrator so the tally-owner (D11) reconciles the parallel-blind count.

### Unrepairable findings

None. No finding required substantive authoring or contradicted artifact content; all three are informational and correctly handled by the report. The only deferred work (Finding 2's stale L3 assertion at `book/src/L3/divfree-projector.md:92-93`) is a downstream-consistency touch routed below — it does not gate this report and does not make it `needs-revision`, because the report under repair is internally complete and the stale assertion lives in a *different* (already-firm) entry that becomes stale only AFTER co-land.

## Suggested resolution

`overall_status: ready`. The report is clean (8/8 pass, zero blocking issues, no repairs needed). Integrator notes:

1. **Sequencing (Finding 1):** apply D6 (`book/src/L2/divfree-projector.md`) BEFORE these two themes in wave-2 serial order, or the new themes' `../L2/divfree-projector.md` links dangle at `cargo make book`. The report declares this dependency explicitly.
2. **Count reconciliation (Finding 3):** let D11 own the L2-L1 / L3-L2 consolidated tallies + cohort-growth-log; do not double-count from this report (it intentionally omits tally touches).
3. **Follow-up OQ (Finding 2):** after D6 + this `divfree-projector-body-identity` land, `book/src/L3/divfree-projector.md:92-93` ("`book/src/L2/divfree-projector.md` does not exist … no `L3-L2/divfree-projector-identity` theme") becomes stale. Record an open-questions entry routing a **lifter** (or next harvester/integrator touch on the L3 entry) to re-anchor lines 92-93 to the now-existing L2 floor + L3-L2 identity theme. This is a post-co-land consistency touch on a firm entry, out of both abstractor and repairer write-authority — it must not be lost.
