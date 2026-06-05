---
verifies: ../CYCLE.md
critiqued_at: 2026-06-05T093000Z
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

# META: verification of energy-fields config-record edge (FOLD decision)

## Critique

This report is a **FEATURE-SURFACE composition-root** maintenance dispatch (a record-edge wiring + FOLD adjudication on an existing `feature/energy-fields.L4.md` output-product leaf column), so the adapted feature-surface checklist applies: rotation-quality and variant-axis-coverage no-op, surface-or-evidence is read as "driver/constituent-range + down-links", and cross-reference-integrity is load-bearing.

### Checks run

**citation-validity (LOAD-BEARING) — pass.** Every L0 citation was confirmed on-disk via codemap `read_range`:
- `config::DomainPostData` at `configfile.hpp:283-295` — the `struct DomainPostData` body opens at 283; the `std::map<int, DomainEnergyData> energy` map lands at line 290 (8th line of the block), exactly as cited. The `:290` pinpoint is correct (no off-by-one).
- `config::DomainEnergyData` at `configfile.hpp:263-270` — `struct DomainEnergyData` opens at 263; the per-index `attributes` vector at 267, in-range. Correct.
- `config::DomainData` at `configfile.hpp:313-326` with `postpro : DomainPostData` at `:322` — verified: the struct opens at 313, the `DomainPostData postpro = {};` field is at line 322 (read of 320-324 places it as the 3rd line). Correct.
- `Measurement::DomainData` at `postoperatorcsv.hpp:74-79` — verified: `struct DomainData { int idx; double energy; double participation_ratio; };`, an exact match to the report's quoted `{ int idx; double energy; double participation_ratio; }`. Correct, and the run-time/measurement-stratum framing matches the struct (plain scalar result row).

The artifact-side claims also verify: `config-record.md` schema does list `domains : config::DomainData` at line 81; SUMMARY.md wires `config-record` at :304 and `energy-fields.L4` at :41; the three named sibling conventions (`sparameters.L4.md:17-18`, `capacitance.L4.md:13-14`, `eigenfrequency-qfactor.L4.md:15-16`) each carry the `depends-on → concepts/config-record / kind: uses-record` edge with the input-signature comment + "(the IoData surface)" exactly as described. All edit-block `[old]` anchors are unique on disk (the `The projection is read-only...` paragraph: 1 hit; the `feature/eigenfrequency-qfactor.L4` reference line: 1 hit; the cites-evidence/reference block in energy-fields.L4.md matches the read). No drift found.

**surface-or-evidence (record-definition sub-check) — pass.** This is the load-bearing check for this dispatch. The FOLD decision is **sound**. (1) The INPUT record `PostprocessConfig` is correctly adjudicated as a readonly construction-stratum **projection** of the `IoData` umbrella, not a distinct data shape: the L0 backing `config::DomainPostData` genuinely hangs off `config::DomainData.postpro` (`:322`), which is `IoData.domains.postpro` (`domains : config::DomainData` is line 81 of the schema the umbrella page already defines). The "sub-record of the IoData umbrella" justification for routing the `uses-record` edge to `concepts/config-record` rather than minting a new page is correct and matches the per-driver-projection model the umbrella page already documents. (2) The OUTPUT `[DomainData]` element type is correctly identified as `Measurement::DomainData` (the run-time result row), already given an in-chapter `## Record definition` (energy-fields.L4.md:90-113) under the single-consumer ≥2-bar — a valid definition home; no missing home. (3) The `config::DomainData` (config domains) vs `Measurement::DomainData` (energy result row) name-collision is **real** (two structurally-unrelated structs share the unqualified name `DomainData` — verified both: `configfile.hpp:313-326` is a domains record of `attributes`/`materials`/`current_dipole`/`postpro`; `postoperatorcsv.hpp:74-79` is a 3-scalar result row) and **correctly handled** — the report documents the collision in the config-record edit and correctly maps the signature's `[DomainData]` to the measurement struct while `PostprocessConfig` routes through `config::DomainData.postpro` without being the `config::DomainData` struct itself. Both records have definition homes; no signature-named record is left described-only-by-use.

**rotation-quality — pass (not applicable to feature-surface kind).** A feature composition-root rotates nothing; it recomposes already-firm vocabulary and adds a record edge. No algebraic/reduction rotation is claimed. No-op per the adapted checklist.

**variant-axis-coverage — pass (not applicable to feature-surface kind).** The column's own variant axis (electric vs magnetic field-kind) lives in the constituent `domain_energy_reduce` op and is already documented in the chapter; this dispatch only adds a record edge and introduces no new axis. No-op per the adapted checklist.

**cross-reference-integrity (load-bearing for this kind) — pass.** Both new edge targets exist on disk: `concepts/config-record.md` (the `uses-record` target, wired at SUMMARY.md:304) and `feature/energy-fields.L4` (the reciprocal back-ref target, wired at SUMMARY.md:41). The new prose markdown link `../concepts/config-record.md` resolves to an existing file. No new file is created, so no SUMMARY change is needed (correctly noted). No dangling reference introduced. Maturity is not overclaimed: `config-record` is `rank: firm`, `energy-fields.L4` is `rank: firm`, so the new `depends-on` edge satisfies the well-foundedness invariant `rank(u) ≤ rank(v)` (3 ≤ 3) — no rank violation. The reciprocal `reference:` edge from the record page constrains nothing (navigational), correct.

**edge-label-fidelity — pass.** The proposed edge `depends-on → concepts/config-record, kind: uses-record` is discussed precisely in the prose: the comment names the input signature and the `IoData.domains.postpro.energy` sub-record path; the prose note in the Inputs bullet points at the umbrella page for the data-shape definition. The reciprocal `reference:` back-ref from config-record is the correct (navigational, non-constraining) reverse direction for a record-named-by-use, matching the 11 existing sibling back-refs. Edge direction and kind are consistent with the prose throughout.

**plan-kind-consistency — pass.** Declared kind is a feature-surface composition-root maintenance edit (FOLD adjudication + record-edge wiring on an existing firm column). The content matches: no new chapter, no new claims, only a `depends-on` record edge + a reciprocal back-ref + a documentation paragraph. No mis-classification; the energy-fields column remains `status` driven by its own composition (correctly untouched).

**skill-uptake-survey — pass.** The report's shape (record-definition FOLD-vs-own-page adjudication, citation confirmation via codemap) implies the record-definition obligation discipline; the report explicitly invokes the ≥2-consumer bar, the OWN-COMPOSITION framing, the graded-stack rank/edge-typing scheme, and confirms all anchors via palace-codemap `read_range`/`search_text`. Adequate telemetry; no missing skill reference. (Pure presence check, non-blocking.)

### Issues found

None. All eight checks pass. The FOLD decision is well-founded: `PostprocessConfig` is a genuine readonly sub-record projection of the `IoData` umbrella (every L0 anchor confirmed via codemap, the `.postpro` chain verified), the output `Measurement::DomainData` is correctly homed in-chapter, the `config::DomainData` vs `Measurement::DomainData` name-collision is real and correctly disambiguated, both new edge targets exist with no rank violation and no SUMMARY/build impact, and the edit anchors are unique on disk. The report is clean and build-safe.
