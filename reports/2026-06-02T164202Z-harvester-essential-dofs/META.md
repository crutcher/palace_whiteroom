---
verifies: ../CYCLE.md
critiqued_at: 2026-06-02T17:05:00Z
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
repaired_at: 2026-06-02T17:20:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
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

# META: verification of "Formalize essential_dofs at L1" (cycle-066 D1)

## Critique

### Checks run

**citation-validity — pass.** Mechanical scan clean: `citecheck.py --scan ... --quiet` reports `28 ok, 0 failing`. All five dispatch-flagged load-bearing pinpoints anchor-resolve via `--anchor`: `multigrid.hpp:95-97`/`bdr_attr_max` (line 95), `multigrid.hpp:99`/`GetEssentialTrueDofs` (line 99), `geodata.hpp:75-96`/`AttrToMarker` (decl+wrappers), `geodata.hpp:77-78`/`-1` (line 78), `spaceoperator.cpp:187-205`/`aux_bdr_marker` (lines 187/190/194/199/205). On-disk Read confirms meaning: `multigrid.hpp:92-101` is exactly the `if (dbc_attr && dbc_tdof_lists)` dbc block with the empty-guarded `bdr_attr_max` ternary (`:95-97`), `AttrToMarker(bdr_attr_max, *dbc_attr)` (`:98`), and `GetEssentialTrueDofs(dbc_marker, dbc_tdof_lists->emplace_back())` (`:99-100`); the per-level reapplication at `:106-111`/`:117-122` is verbatim as cited. `geodata.hpp:75-78` carries the documented marker contract (size `max_attr`, zero/one membership-indicator, `-1`-singleton ⇒ all-ones wildcard). `spaceoperator.cpp:169-206` is `CheckBoundaryProperties` with `bdr_attr_max` at `:174`, `AttrToMarker` at `:175`, the pointwise-OR over exactly eight per-condition markers at `:187-198`, and the per-level `GetEssentialTrueDofs(aux_bdr_marker, ...)` at `:202-205` — every cited claim is faithful. No `verified_against:` YAML block present, so that sub-check no-ops. (One sub-precision note recorded under Issues, non-blocking.)

**surface-or-evidence (the WARRANT) — pass.** This is a NEW operator, not a refinement, so the check reduces to: is `essential_dofs` a genuine self-standing operator rather than a degenerate MFEM forwarder / `fe_space` mirror? It is. The composition `bdr_attrs → (Palace-authored AttrToMarker) → marker → (MFEM-opaque GetEssentialTrueDofs) → DofSet[N]` has a real Palace-authored head witnessed at two independent positive sites (`multigrid.hpp:98` and `spaceoperator.cpp:175`), and the head carries non-trivial algebraic structure (membership-indicator, `-1` wildcard, dense-over-`bdr_attr_max`). The codomain `DofSet[N]` is exactly the bare opaque parameter `eliminate_essential_bc`/`eliminate_rhs` currently consume — de-opaquing that parameter is precisely the "earns a self-standing home" warrant. Crucially the entry does NOT crack open MFEM dof numbering (it explicitly defers to the read-as-given posture, §Context tail), so it avoids the identity-in-named-terms `dof_map`-mirror smell that `fe_space.md:92-107` documents — confirming it is distinct from `fe_space`, not a mirror. WARRANT=YES is well-founded.

**rotation-quality — pass (not the primary axis here).** This is an L1 operator entry, not a lowering theme; there is no L_{n+1}>L_n rotation claim to evaluate in THIS report (the rotation is forward-referenced to D2's `essential-dofs-construction-rotation`). The in-entry abstraction move — naming the open-coded two-call L0 idiom as a single pure typed-set constructor and treating its output as an immutable `DofSet[N]` value — is a genuine vocabulary shift (open-coded inline idiom → named pure function with laws), not a 1:1 rename. Pass; full rotation-quality adjudication is D2's burden.

**variant-axis-coverage — pass.** Two axes declared and both scoped: `attribute-wildcard` (`[-1]` all-boundaries vs explicit list, `geodata.hpp:77-78`) is a real branch in the cited contract and is covered by the wildcard-saturation law. `per-level-hierarchy-application` is explicitly scoped OUT to the `fe_space_hierarchy` consumer (the report is careful that the per-level fan-out is a hierarchy property, not a property of the single-space operator) — an explicit scope-out, not a hidden branch. No hidden axis surfaced: the `skip_invalid` parameter on `AttrToMarker` (`geodata.hpp:79`) is an upstream default-`false` knob never exercised by the cited call sites, so its omission is correct.

**cross-reference-integrity — pass.** All four live `[link]` cross-refs resolve on disk: `fe_space.md`, `fe_collection.md`, `eliminate_essential_bc.md`, `eliminate_rhs.md`. The new slug `essential_dofs.md` is verified ABSENT (correct for a `new:` block). The D2 forward-ref `essential-dofs-construction-rotation` is correctly plain-text (target ABSENT on disk — a live link would be a `linkcheck2` hard error). `fe_space_hierarchy` is referenced as plain-text "named-not-authored rough-in" (correct, not on disk). The `index.md` edit's `old`-side bullet matches line 89 verbatim; the `SUMMARY.md` insert anchors on the existing `eliminate_essential_bc` entry (line 118) with `essential_dofs` correctly absent. Not a firm-body-outside-fence case: the full firm body (Status/Signature/Algebraic-laws/Evidence) sits INSIDE the ```new:``` fence (lines 64-243), with §"Operator content" / §"Supporting evidence" outside being report-meta prose, not the chapter body.

**edge-label-fidelity — pass (not applicable to operator entry).** No L_{n+1}→L_n edge label on this operator report; the `lowers_to: L1-L0/essential-dofs-construction-rotation` frontmatter declares the downward edge and the §"Downward to L0" prose discusses exactly that L1>L0 edge (deferred to D2). Consistent.

**plan-kind-consistency (the firm vs partly-constructive call) — pass.** The `firm` tier is the correct call. Per CLAUDE.md's `partly-constructive` criteria, that status is reserved for a firm structure carrying a CONSTRUCTED sub-part materialized from NEGATIVE anchors (a status/result/error condition reconstructed from where Palace does NOT positively exhibit it). Here the MFEM tail (`GetEssentialTrueDofs`) is read-as-given from a witnessed POSITIVE library boundary — it is read, not constructed-from-absence — so the `partly-constructive` gate does not apply. This is exactly the firm-on-positive-structure posture of `fe_space.md` (firm, with its "MFEM-owned, read-as-given (NOT lifted)" §) and the `fe_collection`/`fe_assemble` precedents the report cites. The five stated laws are syntactic/structural identities on the fully-read Palace-authored marker head (with the dof-set-level monotonicity correctly attributed to the read-as-given MFEM contract, not asserted as a positive Palace claim); the two non-laws are correctly stated (no dof-set-level additivity; space-dependence across de-Rham families). The no-`test-multigrid.cpp` caveat is correctly classed non-gating (laws are syntactic identities on positive source, the `apply_linop`/`fe_space` situation, not the `eigsolve`-convergence-semantics situation). Content shape matches declared `firm`.

**skill-uptake-survey — warning.** The report's shape (firm L1 operator + citation-heavy + dual-registration + variant-axis-bearing) implies several relevant skills, and the report DOES evidence `verify-citation-range`'s mechanical realization (it states all citations were verified via `tools/citecheck/citecheck.py --anchor`, supporting-evidence section). However it does not reference `classify-variant-axis` (two variant axes are declared but the classification procedure is not cited) nor the `proposed-changes-fence-encloses-full-body-guard` (producer-side it is a critic guard, so this is expected-absent). Pure-presence telemetry: one expected skill cited, one variant-axis skill plausibly applicable but unreferenced. Non-blocking.

### Issues found

1. **(minor, citation-precision) "fully Palace-authored ... `geodata.hpp:75-96`" cites the declaration range, not the implementation.** CYCLE.md §Summary (line 33-36) and §Context (line 108-111) assert `AttrToMarker` is "fully Palace-authored" anchored to `geodata.hpp:75-96`. That range contains the contract comment (`:75-78`), the non-template decl (`:79-80`), and two template wrappers (`:82-97`) — the wrappers forward to the non-template `AttrToMarker(int, const int*, int, ...)` whose DEFINITION lives in `geodata.cpp`, not in the cited header range. The "Palace-authored" claim itself is TRUE (it is in `palace/utils/`, `mesh::` namespace, Palace's own function) and the laws rest only on the documented contract (size/zero-one/`-1`-wildcard), which the cited range DOES carry. The imprecision is solely that the word "fully ... authored" reads as if the body is shown in `:75-96` when only the contract+decl is. Severity: low. Suggested tightening: either cite the `geodata.cpp` definition alongside, or phrase as "Palace-owned (contract + decl `geodata.hpp:75-78`/`:79-80`; impl in `geodata.cpp`)." Does not affect any law or the warrant.

2. **(informational, not a defect) dual-registration tally deferral is correctly scoped.** The report registers its OWN index dep-map row + its OWN cohort bullet and DEFERS the consolidated running-count tally (FE-space sub-spine 2→3, grand-total 33→34, growth-log prose at `index.md:31`/`:78`) to D4 as the named count-owner. This matches the index-dual-registration partition; flagged here only so the integrator confirms D4 actually lands the tally (otherwise the §"Firm (FE-space sub-spine — 2 ...)" header at `index.md:78` will be stale post-apply). No action for this report.

3. **(informational) per-level-hierarchy-application axis is a scope-out, verify it stays one.** The second variant axis is declared then immediately attributed to the `fe_space_hierarchy` consumer. This is the correct call (the single-space operator does not own the per-level loop), but it means the axis is documentation-of-reuse, not a covered branch of THIS operator — appropriate, and the report is explicit about it. No defect; noted so a downstream reader does not mistake it for an uncovered branch.

## Repair

### Fixes attempted

- **Finding**: (Issue 1, minor citation-precision) "fully Palace-authored ... `geodata.hpp:75-96`" cites the declaration range, not the implementation — "fully ... authored" reads as if the `AttrToMarker` body is shown at `:75-96`, but that range is the contract comment (`:75-78`) + non-template decl (`:79-80`) + template wrappers (`:82-97`); the non-template definition lives in `geodata.cpp`.
  - **Decision**: repaired
  - **Action**: Verified the body location on-disk via `grep`/Read — the non-template `AttrToMarker(int max_attr, const int *attr_list, int attr_list_size, mfem::Array<int> &marker, bool skip_invalid)` definition is at `reference/palace/palace/utils/geodata.cpp:891-916` (the `-1`-singleton all-ones branch at `:899-902`; the membership-indicator loop at `:905-915`). Rephrased the two "fully Palace-authored" occurrences:
    - **artifact-bound** (lands in `book/src/L1/essential_dofs.md` via the `new:` block, §Context): "**fully Palace-authored** in `palace/utils/geodata.hpp:75-96`" → "**Palace-authored** (contract + decl `palace/utils/geodata.hpp:75-96`; body `palace/utils/geodata.cpp:891-916`)", with the `-1`-wildcard and membership-indicator claims co-cited to their body lines (`geodata.cpp:899-902`, `:905-915`).
    - **report-meta** (§Summary, for internal consistency): same "fully Palace-authored" → "Palace-authored (contract + decl `geodata.hpp:75-96`; body `geodata.cpp:891-916`)" with the `mesh::` namespace note retained.
  - The `book/src/L1/index.md` edit row was left unchanged — it says "Palace-authored `mesh::AttrToMarker`, `palace/utils/geodata.hpp:75-96`" (attributional adjective, not the "fully ... / impl-shown-here" reading the critic flagged), so it carries no imprecision to repair.

- **Finding**: (Issue 2, informational) dual-registration tally deferral to D4 — correctly scoped.
  - **Decision**: not-needed
  - **Rationale**: explicitly flagged by the critic as "No action for this report"; the report correctly defers the consolidated running-count tally to D4 (the named count-owner) per the index-dual-registration partition. The integrator should confirm D4 lands the 2→3 / 33→34 tally so the §"Firm (FE-space sub-spine)" header at `index.md:78` is not left stale — that is an integrator/D4 concern, not a repairable defect here.

- **Finding**: (Issue 3, informational) per-level-hierarchy-application axis is a scope-out.
  - **Decision**: not-needed
  - **Rationale**: critic confirms it is the correct call (documentation-of-reuse, not an uncovered branch); no defect.

- **Finding**: (skill-uptake-survey, warning) `classify-variant-axis` not cited by slug though two variant axes are declared.
  - **Decision**: not-needed
  - **Rationale**: pure-presence telemetry, explicitly non-blocking; the critic does not assert the classification is wrong (variant-axis-coverage passed). Adding a skill-slug citation is producer-side authoring, not a mechanical repair, and the survey is informational. No fix.

### Unrepairable findings

None. The single actionable finding (citation-precision) was mechanical — a verified co-citation of the on-disk `geodata.cpp` body location alongside the existing decl range, and a phrasing tightening — well within repair authority. All other findings are informational/telemetry with no defect.

## Suggested resolution

`ready`. Notes for the integrator:
- The citation-precision fix lands in the artifact body (`book/src/L1/essential_dofs.md` §Context) and adds two body-line co-citations (`geodata.cpp:891-916`, `:899-902`, `:905-915`); these are fresh `palace/...`-rooted pinpoints — a `citecheck.py --scan` over the applied file will pick them up, and the on-disk body was verified during repair (`AttrToMarker` definition confirmed at `geodata.cpp:891`).
- Confirm D4 (the named count-owner) lands the deferred FE-space-sub-spine tally (2→3 members; L1 firm grand-total 33→34) so the §"Firm (FE-space sub-spine)" header at `book/src/L1/index.md:78` is not stale post-apply (critic Issue 2).
