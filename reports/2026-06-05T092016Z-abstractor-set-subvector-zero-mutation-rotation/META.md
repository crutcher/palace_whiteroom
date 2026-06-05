---
verifies: ../CYCLE.md
critiqued_at: 2026-06-05T093500Z
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
overall_status: ready
---

# META: verification of CYCLE — L1>L0 theme set-subvector-zero-mutation-rotation

## Critique

### Checks run

**citation-validity (LOAD-BEARING) — pass.** `citecheck.py --scan` returns `17 ok, 0 failing`. I then directly read every load-bearing L0 pinpoint via codemap `read_range` (the prompt flags a ±1-drift sibling this batch, so I did not rely on the report's self-anchor assertions). The real body `vector.cpp:461-492` was read in full: line 461 = `void SetSubVector(Vector &x, ...)`; `rows.Read` gather at :466; `x.ReadWrite(use_dev)` destination at :467; `forall_switch` at :468; `X[id] = sr` at :472; close brace `}` at :474 — all EXACTLY as cited. Complex body: `template <>` at :476, signature at :477, two-buffer `XR`/`XI` at :483-484, `forall_switch` at :485, `XR[id] = sr` at :489, `XI[id] = 0.0` at :490, close brace `}` at :492 — all exact, zero drift. Declaration `vector.hpp:220-221` = `template <typename VecType>` / `void SetSubVector(VecType &x, ..., double s);` confirmed; anchor at 221 correct. Use-sites confirmed exactly: `divfree.cpp:173` (`SetSubVector(rhs, *bdr_tdof_list_M, 0.0)`), `gmg.cpp:194` (`SetSubVector(X[l-1], *dbc_tdof_lists[l-1], 0.0)`), `rap.cpp:186` (`SetSubVector(diag, dbc_tdof_list, 1.0)` — the non-zero parent, correctly NOT folded). The `verified_against:` YAML block round-trips under `yaml.safe_load` (9 entries; no leading-quote-scalar ParserError). All pinpoints verified; no off-by-one.

**surface-or-evidence — pass.** Refinement-shaped (a lowering theme over an existing firm L1 operator) with full positive-evidence backing. Both sub-patterns rest on positive L0 sites read in full; the load-bearing complex claim `XI[id] = 0.0` as a hard literal-`0.0` (independent of `sr`) is verbatim-confirmed at :490, and the whole-complex-dof-zeroing claim is grounded by `XR[id]=sr` (:489) + `XI[id]=0.0` (:490) together. Cohort C sites are each positively cited. No record named in the theme's signature requires a definition home (`DofSet`/`Tensor` are L1-vocabulary references defined in the L1 entry, not introduced here). Not a pure rotation_claim — it modifies/authors surface with evidence.

**rotation-quality (LOAD-BEARING) — pass.** A genuine mutation rotation, NOT an identity-in-named-terms anti-mirror smell. The L1 form is a value-in/fresh-out pure diagonal-projector application carrying no destination buffer, device dispatch, or index-gather mechanism; the L0 form materializes a destination by binding the receiver argument `x` as both source and destination (`x.ReadWrite`), gathers the abstract `DofSet` as a device pointer, and dispatches a `forall_switch` element-loop. The "crucial L0 facts the L1 form erases" section enumerates the genuine vocabulary shift (receiver-argument destination idiom, index-gather, device dispatch, complex two-buffer threading, hard-literal imaginary zero). The receiver-argument destination-binding (first-argument-as-destination — a third variant distinct from `scal`'s `*this` and `apply_linop`'s `y` output-arg) is a real, recurring rewrite theme, not a rename. The firm-on-positive-structure escape is correctly applied: the laws are syntactic identities on fully-specified positive source (the kernel writes the projector definition verbatim), so the absence of a dedicated unit test does not gate `firm` — matching the `apply_linop`/`scal` precedent, not the convergence-semantics situation.

**variant-axis-coverage — pass.** The element-type axis (real `Vector` / complex `ComplexVector`) is explicitly covered by the two sub-patterns A/B, with dispatch-by-static-`VecType` stated (Applicability cond. 3). The scalar-value axis is explicitly scoped: this theme lowers only `s = 0.0`; the `s ≠ 0` general parent (`rap.cpp:186` `1.0`) is named and deliberately excluded (cond. 4, §Speculative, Open questions). The device/host axis is noted as transparent. No hidden branches; the `s=0.0`-has-no-fast-path fact is explicitly recorded.

**cross-reference-integrity — pass.** All `[link]` targets resolve on disk: sibling themes `scal-mutation-rotation.md`, `reciprocal-elementwise-product-mutation-rotation.md`, `divfree-projector-mutation-rotation.md`; the L1 endpoint `L1/set_subvector_zero.md`; the concept page `concepts/set_subvector_zero.md`; and the L1 entry's existing `reference` siblings (`eliminate_essential_bc`, `eliminate_rhs`, `divfree-projector`) all exist. The `edit:` anchors are present and unique in their targets: the `index.md` `scal-mutation-rotation` row (line 60) + `**Construction-rotation**` marker (line 61) place the new row in alpha position; `SUMMARY.md` lines 253-254 anchor the alpha insertion; the L1 entry's `reference:` block (lines 18-21) and the three "(forthcoming)" prose notes (lines 140, 266, 280) exist to be de-staled to live links. The new file plus the de-stale repoint together close all three forward-refs with no dangling reference (live-link target created in the same proposed-changes set), so no `linkcheck2` hard error is expected.

**edge-label-fidelity — pass.** Typed-from-start (HARD-gate-new). The `depends-on` bucket correctly carries the L1 source entry (`kind: lowers-to`) + the three L0 evidence sites (`kind: cites-evidence`); siblings + consumer are `reference`. The edge direction is correct and the prose discusses exactly the L1>L0 edge it labels. The rank well-foundedness is sound: theme rank = min(L1-endpoint firm=3, L0 terminal) = firm, and `rank(theme) ≤ min(endpoints)` holds. The coupled de-stale correctly keeps the L1-entry→theme link a `reference` (downward navigational) NOT a `depends-on` — adding a `depends-on` from the firm entry to the theme would be both redundant and a rank-direction error, and the report explicitly reasons this through.

**plan-kind-consistency — pass.** Declared kind is a firm L1>L0 lowering theme; content shape matches — `## Status` firm with the firm-on-positive-structure justification, L1-form/L0-form/applicability/justification-kind sections, no rough-in placeholders. The `firm` claim is supported (syntactic identities on positive source), correctly distinguished from `rough-in (test-coverage-bounded)` and `partly-constructive`.

**skill-uptake-survey — pass.** The report references `citecheck.py --anchor` self-verification and the FE-source close-brace END-line guard for the body boundaries — the relevant procedural skills for a citation-heavy lowering theme are invoked.

### Issues found

None. Every load-bearing citation pinpoint was independently re-read and matches exactly (zero drift, including the suspect lines the prompt flagged). The rotation is genuine, the firm-on-positive-structure escape is correctly applied, variant axes are covered or explicitly scoped, all cross-references and edit-anchors resolve, edges are typed and rank-well-founded, and the `verified_against` YAML round-trips. A minor note for the integrator (NOT a defect): the two prose `edit:` blocks for `L1/set_subvector_zero.md` (§Semantics, §Downward) are written as resulting replacement text rather than find/replace pairs — standard CYCLE.md `edit:`-block convention, applied by the integrator; the new text aligns with the existing file structure.
