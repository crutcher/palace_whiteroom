---
verifies: ../REPORT.md
critiqued_at: 2026-06-02T17:40:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-06-02T17:45:00Z
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

# META: verification of L1>L0 essential-dofs-construction-rotation theme

## Critique

### Checks run

**citation-validity — pass.** All L0 citations verified via the on-disk `Read` tool (NOT codemap, per the
confirmed ±1 drift this batch) and mechanically re-confirmed with `citecheck --scan` (23 ok, 0 failing).
Every load-bearing pinpoint lands exactly:
- `multigrid.hpp:92-101` — the dbc block runs `mfem::Array<int> dbc_marker;` (line 92) through the closing
  `}` (line 101). Exact.
- `bdr_attr_max` extraction `:95-97` — lines 95-97 (`mesh[...].Get().bdr_attributes.Size() ? .Max() : 0`).
  Exact.
- `AttrToMarker` call `:98` — line 98 (`dbc_marker = mesh::AttrToMarker(bdr_attr_max, *dbc_attr);`). Exact.
- `GetEssentialTrueDofs` `:99` (header) / `:99-100` (body) — the call spans lines 99-100, and the
  `dbc_tdof_lists->emplace_back()` out-parameter receiver is on line 100. Both the single-line `:99`
  start-reference and the `:99-100` span-reference are accurate.
- per-level reapply `:106-111` (h-refinement) / `:117-122` (p-refinement) — exact.
- `geodata.hpp:75-96` `mesh::AttrToMarker` — doc comment with `{0,1}`-membership + `-1`-wildcard contract
  `:75-78`, decl `:79-80`, iterable template wrapper `:82-88`, return-by-value template wrapper `:90-96`.
  All exact; the `-1`-singleton wildcard sentence is at `:77-78`. Exact.
- union-additivity witness `spaceoperator.cpp:187-198` — `aux_bdr_marker` declared at 187, the pointwise-OR
  over eight per-condition markers at 188-198. Exact (the `:187-198` span correctly includes the
  declaration line).
- standalone `CheckBoundaryProperties` `spaceoperator.cpp:169-206` — `bdr_attr_max` `:174`,
  `AttrToMarker(bdr_attr_max, dbc_attr)` `:175`, marker-OR union `:187-198`, `GetEssentialTrueDofs(...,
  aux_bdr_tdof_lists.emplace_back())` `:204-205`. All exact.
No drift in any cited range. The report carries no fenced `verified_against:` YAML block (it uses a prose
§Verified-against section), so the YAML round-trip sub-check is N/A.

**surface-or-evidence — pass.** This is a NEW firm theme (`new:book/src/L1-L0/essential-dofs-construction-rotation.md`),
not a refinement of an existing operator/theme, so the surface-vs-rotation_claim fork applies as
new-surface authoring: the proposal introduces real chapter surface (the L1>L0 theme body) and carries its
structural justification anchored at L0 throughout. Not a pure rotation_claim, not a retroactive
evidence-backfill — well-formed.

**rotation-quality — pass.** The L1→L0 is a genuine vocabulary translation, not a rename. The L1 form is a
referentially-transparent value `essential_dofs(space, bdr_attrs, bdr_attr_max) → DofSet[N]`; the L0 form is
an imperative attribute → marker → `GetEssentialTrueDofs` sequence with an out-parameter write
(`dbc_tdof_lists->emplace_back()` receiver read as a returned value). The translation hides imperative state
(the out-parameter mutation, the marker scratch array) and coarsens the dof structure to an opaque index
axis tagged by the space — this is state-hiding + coarser substitution, the pass shape, not a 1:1 named-term
map. The head-lowers/tail-opaque split is the correct realization of the 2026-06-01 vocabulary-shift
redirect: the Palace-authored construction head (`bdr_attr_max` extraction + `mesh::AttrToMarker`) lowers
positively, while the MFEM `GetEssentialTrueDofs` tail is documented as a read-as-given library boundary
(not re-mirrored), explicitly avoiding the identity-in-named-terms smell. Directly analogous to the c064
`fe-space-construction-rotation` construction-lowers / dof-bookkeeping-MFEM-owned split.

**variant-axis-coverage — pass.** The orthogonal axis (attribute resolution) is enumerated as a 2-case table
on the head: explicit list `[a₁,…]` → dense `{0,1}` marker (`geodata.hpp:76`) vs. all-boundaries wildcard
`[-1]` → all-ones marker (`geodata.hpp:77-78`). Both cases feed the same opaque tail unchanged. A second
potential axis — per-level hierarchy reapplication — is explicitly scoped OUT (assigned to the deferred
`fe_space_hierarchy` consumer, with the `multigrid.hpp:106-111`/`:117-122` reapply sites cited). No hidden
branches: the empty-boundary case (`bdr_attr_max = 0 ⇒ ∅`) is also covered as the empty-guard identity. Clean.

**cross-reference-integrity — pass.** All sibling links resolve on disk: `fe-space-construction-rotation.md`,
`fe-collection-construction-rotation.md`, `fe-assemble-libceed-boundary-obstruction.md`,
`eliminate_essential_bc.md`, `eliminate_rhs.md`. The forward-ref live-link `[L1/essential_dofs](../L1/essential_dofs.md)`
is to D1's entry which lands the SAME cycle (currently not on disk) — this is the sanctioned
integration-may-materialize same-cycle forward-reference pattern, flagged by the report for integrator
ordering awareness; not a defect. The `index.md` edit reproduces the `fe-space-construction-rotation` anchor
row verbatim (matches on-disk line 53 exactly) and appends the new row after it. The SUMMARY.md edit anchors
on lines 152-153 (`fe-space-construction-rotation` immediately followed by `fe-collection-construction-rotation`,
confirmed on disk) and inserts the new row between them — unambiguous. The L1-firm-tally update is correctly
DEFERRED to D4 (named count-owner), with the dual-registration note documenting why the L1-L0 index carries
no cohort-bullet / running-count section. Build-readiness fence guard: the `new:` block fence is balanced and
ENCLOSES the full firm apparatus (`## Status` + L1 form + L0 form + split + variant axis + Justification kind
+ Verified-against) inside the fence — no firm-body-outside-fence defect (the report's own top-level sections
are the dispatch-report scaffolding, distinct from the chapter body inside the fence). The nested fences are
indented-code-form (4-space `// palace/...` and signature blocks), no nested ``` markers, even parity.

**edge-label-fidelity — pass.** The edge is L1>L0 (LHS L1 `essential_dofs`, RHS L0 dbc block at
`multigrid.hpp:92-101`), narrated strictly forward (high→low): §"L1 form (LHS)" then §"L0 form (RHS)" then
the lowering split. The prose discusses exactly this edge; no L_{n+1}/L_n mismatch, and the high→low
direction invariant is respected (the reverse lifting note is correctly quarantined as a working note in
§Open-questions).

**plan-kind-consistency — pass.** Declared kind is a firm L1>L0 theme; content shape matches. The `firm`
status is correctly justified: the entire Palace-authored head is read off positive source, and the MFEM
tail is a witnessed library-ownership boundary read-as-given — explicitly NOT a constructed sub-part from
negative anchors, so NOT `partly-constructive` (the report draws this distinction precisely, citing the
`fe-space-construction-rotation` firm-on-positive-structure precedent and contrasting against the
`opaque-library-ownership` `fe-assemble-libceed-boundary-obstruction`). This matches D1's `essential_dofs`
status and the c064 precedent. No rough-in placeholders inside a firm entry. The no-dedicated-`test-multigrid.cpp`
caveat is correctly noted as non-gating per the firm-on-positive-structure precedent.

**skill-uptake-survey — warning.** The report's shape implies two relevant skills whose invocation is not
referenced: (i) `verify-rotation-citation` / `verify-refinement-surface` for the rotation+citation anchoring
that is the core of this theme, and (ii) `proposed-changes-fence-encloses-full-body-guard` (the producer-side
counterpart the report's careful in-fence body authoring would benefit from naming). The report does cite
`tools/citecheck/citecheck.py --anchor` for citation verification (good mechanical-tool uptake) and references
the precedent chapters, but does not name any skill invocation. This is a pure telemetry surface, non-blocking
— the underlying work is sound.

### Issues found

No blocking issues. The report is citation-clean (23/23 mechanical, all pinpoints exact on-disk), the rotation
is a genuine vocabulary translation with the correct head-lowers/tail-opaque split, the firm status is
correctly distinguished from partly-constructive, variant-axis coverage is complete with the hierarchy axis
explicitly scoped out, and all registration/cross-reference plumbing resolves (modulo the sanctioned same-cycle
forward-ref to D1's `essential_dofs.md`).

1. **(minor, skill-uptake-survey) No skill invocation referenced** — CYCLE.md §Supporting-evidence /
   §Justification-kind. The theme's rotation+citation+fence shape implies `verify-rotation-citation`,
   `verify-refinement-surface`, and `proposed-changes-fence-encloses-full-body-guard`; only the `citecheck`
   tool is named. Telemetry-only, non-blocking.

2. **(informational, not a defect) Same-cycle forward-ref dead-on-disk** — CYCLE.md L0-form / Verified-against,
   `[L1/essential_dofs](../L1/essential_dofs.md)`. Target lands this cycle via D1; the report flags it for
   integrator ordering. Noted here only so the integrator confirms D1 and D2 finalize together (per
   integration-may-materialize). Not a repair candidate.

## Repair

### Fixes attempted

No findings to repair. The critic returned 7 `pass` + 1 `warning`, and the single warning
(`skill-uptake-survey`) is pure telemetry — it notes the report names the `citecheck` mechanical tool but
does not invoke any skill by slug. This is a non-blocking surface observation, not a content defect, and is
out of repair scope (it would require authoring/altering producer-side telemetry, not a mechanical fix). All
substantive checks are clean:

- **citation-validity** — `not-needed`. 23/23 mechanical (`citecheck --scan`), every pinpoint exact on-disk
  with zero drift. Nothing to re-anchor.
- **surface-or-evidence** — `not-needed`. NEW firm theme introduces real L1>L0 chapter surface, structurally
  anchored at L0 throughout. Well-formed new-surface authoring.
- **rotation-quality** — `not-needed`. Genuine vocabulary translation (state-hiding + coarser dof
  substitution), correct head-lowers / tail-opaque split per the 2026-06-01 vocabulary-shift redirect — not
  an identity-in-named-terms rename.
- **variant-axis-coverage** — `not-needed`. Attribute-resolution axis enumerated as a 2-case table; hierarchy
  axis explicitly scoped out; empty-boundary guard covered.
- **cross-reference-integrity** — `not-needed`. All sibling links + index.md / SUMMARY.md anchor rows resolve
  on disk; fence parity even; L1-firm-tally correctly deferred to D4.
- **edge-label-fidelity** — `not-needed`. L1>L0 narrated strictly high→low; no edge mismatch.
- **plan-kind-consistency** — `not-needed`. `firm` status correctly justified (positive-source head + witnessed
  read-as-given MFEM tail), correctly distinguished from `partly-constructive`.
- **skill-uptake-survey** — `not-needed`. Telemetry-only warning; underlying work sound; not a mechanical-repair
  candidate.

### Unrepairable findings

None. No deferral required; nothing routed to a follow-up agent.

## Suggested resolution

`ready` — clean for integration. Citations on-disk-verified zero-drift, genuine vocabulary translation, firm
status correct. **Integrator note:** the forward-ref live-link `[L1/essential_dofs](../L1/essential_dofs.md)`
points at D1's same-cycle entry (not yet on disk) — this is the sanctioned integration-may-materialize
same-cycle forward-reference pattern. **Apply D1 before D2** so the link resolves; it will be live at
`integrator-finalize` book-build. No action beyond ordering awareness.
