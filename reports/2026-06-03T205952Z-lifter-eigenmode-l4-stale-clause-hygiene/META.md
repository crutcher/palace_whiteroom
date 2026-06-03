---
verifies: ../CYCLE.md
critiqued_at: 2026-06-03T211500Z
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

# META: verification of "Re-anchor eigenmode.L4 stale maturity clause"

## Critique

### Checks run

**citation-validity — pass.** Ran `python3 tools/citecheck/citecheck.py --scan CYCLE.md --quiet`: `8 ok, 1 failing`. The sole failing item is `[MISS] open-questions.md:1057` — and the report's flag of this as a false positive (CYCLE.md:26 / Supporting-evidence) is **correct**: citecheck searches only under `reference/{palace,bunsen,burn}`, `reference`, and `book/src`, so any `scaffolding/open-questions.md` working-notes reference is structurally unresolvable by the tool. This is a working-notes pointer, not an L0/book citation. I independently confirmed the referent exists: `scaffolding/open-questions.md:1057` carries the `eigenmode-driver-column-seed-promotion-blocks-eigenfrequency-qfactor-column` NEW marker, and `:1056` the verb-firming CLOSED-RESOLVED-BY-AUDIT marker. The on-disk firmness anchors verify: `book/src/L4/eigenfreq_qfactor_reduce.md:4` `firmness: firm` (confirmed). One minor imprecision noted (non-blocking): the report cites the verb's `## Status` body at `:185`, but the `## Status` header is at `:183` and the `` `firm`. `` body opens at `:185` — the report's `:185` points at the body line not the header, which is accurate-as-written for "the `## Status` body opens `` `firm`. ``" but mildly loose vs. its own `:185 ## Status` phrasing in the frontmatter inputs. The load-bearing fact (verb is firm) holds. No new pinpoint L0 citations are introduced by this hygiene pass (only maturity words + a grammatical re-phrase change), so there is no new `path:lo-hi` requiring an `--anchor` check.

**surface-or-evidence — pass.** This is a pure retroactive-evidence/hygiene re-anchor of an existing feature-surface chapter (not a new per-op claim). Adapted for the feature-surface composition-root kind: the chapter's evidence is the L0 driver range (`eigensolver.cpp:32-477`, untouched) + the constituent down-links (untouched). The edit corrects a stale *maturity word* against on-disk evidence (`eigenfreq_qfactor_reduce.md:4` firm), which is exactly the bounded L0-evidence-driven prose correction the lifter role permits. No record/struct is newly named in a signature (no new `EigenmodeConfig`/`EigenmodeResult` definition introduced — they pre-exist and are merely referenced), so the record-definition sub-check does not fire.

**rotation-quality — pass (not applicable to feature-surface kind).** A feature-surface composition-root rotates nothing — it recomposes already-firm vocabulary outward. No algebraic/structural rotation is asserted by this hygiene pass; formally a no-op for this kind.

**variant-axis-coverage — pass (not applicable to feature-surface kind).** The chapter's variant axes (problem-type, spectral-transformation) live in the composed constituents and are unchanged by this pass; a feature chapter has no variant axes of its own. The edits touch only maturity-word prose.

**cross-reference-integrity — pass (load-bearing for this kind).** Verified each down-link and slug the corrected prose relies on: (1) the OQ slug `eigenmode-driver-column-seed-promotion-blocks-eigenfrequency-qfactor-column` resolves to a real entry at `open-questions.md:1057`; (2) the constituent down-links (`../L4/fe_assemble.md`, `../L4/eigsolve.md`, `./eigenfrequency-qfactor.L4.md`, `../L4/eigenfreq_qfactor_reduce.md`) all exist on disk and the maturity claims match the on-disk `## Status` (eigsolve/fe_assemble firm; eigenfrequency-qfactor.L4 `status: seed`; eigenfreq_qfactor_reduce firm). No maturity overclaim — the corrected prose now says the verb is firm (matches disk) while the output-product column stays seed (matches disk, correct per the column-promotion rule on the reciprocal constituent). The seed-composing-firm-constituent situation is the correct composition-root state.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried by this feature-surface prose (the §Layer-definition discipline note correctly states no LHS/RHS direction is touched). The maturity claim the fix targets is verified against the exact on-disk source: `book/src/L4/eigenfreq_qfactor_reduce.md:4` `firmness: firm` — so the rough-in→firm wording correction is accurate, and the prose discusses the eigenmode driver column ↔ eigenfrequency-qfactor output-product column reciprocal relationship that the corrected clause actually describes.

**plan-kind-consistency — pass.** Declared shape is a LOW/hygiene pure-rewriting (lifter) pass. Content matches: maturity-word sync + minimal grammatical re-phrase, no new authorship, no new combinator, no rotation. The scope-bound was honored — verified `book/src/feature/eigenmode.L4.md:5` `status: seed` is UNCHANGED, and the promotion-rule logic is narrated against the CURRENT rule (not re-authored); the pending batch-26 directive is explicitly flagged as out-of-scope (CYCLE.md Open-questions), not pre-empted. The §Status block at `:74` was correctly left structurally intact (only an editorial-precision touch aligning to the verb-firm fact).

**skill-uptake-survey — pass.** The report references the mechanical `tools/citecheck/` line-map and the lifter §L0-evidence-driven-prose-correction discipline. For a maturity-word hygiene sync with no new citations, no further skill invocation is implied; pure telemetry, non-blocking.

### Issues found

No blocking issues. One non-blocking precision note:

- **(minor, citation-validity, CYCLE.md frontmatter input `:185` / Summary)** — the report twice phrases the verb-firm anchor as `:185 ## Status`, but the `## Status` header is at `:183` (the `` `firm`. `` text is at `:185`). The firm fact is correct and confirmed on disk; this is a header-vs-body line slip of 2, not a drifted claim. Repairer may tighten the wording if it runs, but it does not affect any check verdict.

The two proposed `[old]` blocks were confirmed to match `book/src/feature/eigenmode.L4.md:55` and `:74` exactly, and the `[new]` blocks faithfully mirror the already-landed precedent narration on the reciprocal `eigenfrequency-qfactor.L4.md:55` (verb now firm / column stays seed on the reciprocal cross-link, same OQ slug cited). All 8 checks pass; report is clean.
