---
verifies: ../REPORT.md
critiqued_at: 2026-05-28T03:49:07Z
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

# META: verification of "L3 index intro refresh"

## Critique

### Checks run

**citation-validity** — pass. Every load-bearing claim carries a pointer and all checked pointers resolve in-range. The `[old]` block in `## Proposed changes` matches `book/src/L3/index.md:9-15` verbatim (confirmed character-for-character incl. the four bullets) so the edit is mechanically anchored. The 8-operator inventory in §"Supporting evidence" matches the dep-map table (`index.md:19-28`) and the 8 actual files in `book/src/L3/` exactly (apply_linop, axpby, axpbypcz, axpy, dot, krylov-step, nrm2, scal — 8 firm, no extras, no omissions). The naming-reconcile evidence pointers resolve: `apply_linop.md:20` carries the `index.md:11-14` advertisement back-reference, and `apply_linop.md:24` carries the verbatim "matvec, axpy, dot, nrm2 as field operations" quote plus "`apply_linop` is the matvec generalisation" — the report's framing-adoption claim is accurate. `concepts/sequential-obstruction.md` (referenced in the new prose) exists. The krylov-step kernel signature `(op, K, s) -> (K', s', outputs)` asserted in the new prose matches `krylov-step.md:36`. One minor citation-completeness gap noted under Issues (the back-reference census is incomplete) but it does not produce any invalid pointer.

**surface-or-evidence** — pass (not a refinement-shaped proposal). This is a Part-overview prose refresh of `## Semantics (overlay)`, modifying index/overview surface directly. It is not a change to an operator/theme's algebraic content and carries no rotation_claim, so the rotation-evidence coupling requirement is inapplicable. The proposal modifies surface (overlay prose) and is grounded in already-firm dep-map state — it is the prose-side reconciliation of changes the dep-map already absorbed. Allowed.

**rotation-quality** — pass (not applicable to overview-refresh shape). The report asserts no new algebraic/structural/reduction rotation; it reorganizes an inventory line and adds a naming alias. The identity-in-form rotations it references (L3→L1 per cohort entry) are pre-existing firm content, not asserted here. No renaming-as-rotation claim is made. Marked pass per "inapplicable to report-kind".

**variant-axis-coverage** — pass. The refresh is inventory prose, not an operator with orthogonal variant axes to enumerate. The one variant-flavored phrase in the new prose — "square and rectangular operators, real and complex, all operator representations absorbed" for `apply_linop` — is consistent with the `apply_linop.md` frontmatter variant_axes block (element-type real|complex; transpose-mode; accumulate-mode orthogonal; operator-representation absorbed). The prose compresses these accurately (it surfaces the absorbed axis and two of the orthogonal axes; it does not claim full coverage, it is orientation prose). No hidden branch is introduced.

**cross-reference-integrity** — pass. All slugs named in the new prose resolve: apply_linop, axpy, axpby, axpbypcz, dot, nrm2, scal, krylov-step all exist as `book/src/L3/*.md`. The `concepts/sequential-obstruction.md` reference resolves. The lowering-theme references in §"Supporting evidence" (`book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`, `book/src/L3-L2/krylov-step-body-identity.md`) are named for orientation and resolve. The new prose itself introduces no `[link]` markdown links (it names slugs in backticks, consistent with the existing overlay style), so no link can break.

**edge-label-fidelity** — pass (no edge label). This is an L3-internal overview refresh; it carries no L_{n+1}→L_n edge label requiring prose-to-label agreement. The cross-layer mentions (krylov-step lifts from L4, lowers to L2) are correctly directioned and confined to §"Supporting evidence" orientation, not asserted as the proposal's edge.

**plan-kind-consistency** — pass. Declared shape is a layer-intro-author Part-overview refresh (observation/overview-edit kind), and the content matches: one `edit:` block against `index.md` only, no dep-map rows touched, no operator authoring, explicit deferral of the Vocabulary-cohort subsection with role-spec rationale. The report correctly scopes out operator-entry touch-ups (the apply_linop back-reference re-pointing) as harvester/lifter territory. No firm-operator content masquerading as overview, and vice versa.

**skill-uptake-survey** — pass (telemetry only). The report's shape (Part-overview prose refresh closing two prose-cleanup OQs) does not strongly imply a specific skill invocation. `verify-citation-range` would have been a natural fit for the back-reference-preservation argument; it is not referenced. Non-blocking surface note only.

### Issues found

1. **Incomplete back-reference census** — `CYCLE.md` §"Supporting evidence" → "Back-reference safety" (lines 69) and §"Open questions / caveats" (line 75). The report enumerates back-references to the overlay line only in `apply_linop.md` (lines 20, 24, 150, 173). It misses `book/src/L3/scal.md`, which also cites the overlay line/tokens in **three** places: `scal.md:26` and `scal.md:49` cite `index.md:11-14` / `index.md:13`, and `scal.md:137` quotes the verbatim "matvec, axpy, dot, nrm2 ... as field operations" string. Severity: low. The refresh **preserves** the tokens "matvec" and "axpy, dot, nrm2" in the new prose, so all `scal.md` references remain semantically valid (the same non-breaking property the report argues for `apply_linop.md` holds for `scal.md` too) — this is not a correctness defect in the edit, only an omission in the report's accounting. A complete census strengthens the back-reference-safety argument and the integrator's line-drift routing note.

2. **`scal.md:137` framing goes slightly stale** — consequence of the refresh, surfaced at `book/src/L3/scal.md:137`. That line reads "the index lists three of the six BLAS-1 primitives by name; the others, including `scal`, are implied by the 'etc.' reading". After this refresh the index names the **full** cohort (all of axpy/axpby/axpbypcz/scal/dot/nrm2 plus apply_linop), so "three of the six ... the others implied" becomes inaccurate. Severity: low/cosmetic. It does not invalidate any citation (the cited content — naming BLAS-1 primitives as field operations — is preserved and enriched), and the `scal.md` entry is an operator entry outside layer-intro-author authority, so it is correctly out of scope for this dispatch. Worth a one-line routing note for a future lifter sweep (parallel to the `apply_linop.md` re-pointing note the report already filed), so the integrator can bundle it.

3. **Line-number drift acknowledged but routing is slightly under-specified** — `CYCLE.md` §"Open questions / caveats" (line 75). The report correctly notes the first bullet expands and the advertised tokens drift off line 13, and correctly argues the citations target content not a code range so they stay semantically valid. The drift affects `apply_linop.md` (4 sites) AND `scal.md` (3 sites, per Issue 1) — the report's drift note only counts the `apply_linop.md` sites. Severity: low. Same non-blocking nature the report assigns; flagged so the repairer/integrator can decide whether to widen the routing note to cover both files.

4. **`apply_linop.md:150` cited as a back-reference but it is `:13` not `:11-14`** — minor precision note on `CYCLE.md:69`. The report lists `apply_linop.md:150` among sites citing `index.md:13`. Verified: line 150 does cite `index.md:13` with the verbatim token string — accurate. (Line 20 cites `:11-14`; lines 24, 150, 173 cite `:13`.) No defect; recording the verification so the repairer need not re-walk it.
