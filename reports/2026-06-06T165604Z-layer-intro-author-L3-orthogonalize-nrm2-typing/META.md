---
verifies: ../CYCLE.md
critiqued_at: 2026-06-06T170805Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: warning
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-06T172000Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: repaired
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of REPORT "L3 lazy-tail typed-edge migration — orthogonalize + nrm2"

## Critique

### Checks run

**citation-validity — pass.** This is a frontmatter-only typed-edge dispatch; its "claims" are the
edge derivations in §Faithful-edge derivation, each pinned to a prose-line range in the two on-disk
chapters. I cross-read every load-bearing pinpoint against the live files: `L3/orthogonalize.md`
§Status (`:448`, "`partial-obstruction` — the per-step body … lifts … but the MGS `j`-loop is a
witnessed `sequential-obstruction`") confirms `rank: partial-obstruction` + `obstruction_resolution:
firm`; §Dependencies "Same-layer (L3)" (`:366-374`) confirms the `dot`/`axpy` body primitives and the
explicit `nrm2`/`scal` NON-dependency exclusion (`:376-379`); §"Downward to L2" (`:80-92`,
`:407-414`) confirms the `L2/orthogonalize` identity-in-form + the substantive `orthogonalize-variant-split`
theme. For `L3/nrm2.md`: §"Lowers to" (`:85`), §"Downward to L2" (`:98`), §Evidence (`:173-174`) all
back the authored edges. The two source-line pinpoints the producer threads through (`iterative.cpp:630-632`,
`:809-811`) are pre-existing chapter evidence, not new claims of this dispatch, and are not re-asserted
with new bounds. No `verified_against:` block is newly authored in this CYCLE.md (the one in
`L3/orthogonalize.md` is pre-existing chapter content, untouched by this frontmatter-only edit), so the
YAML round-trip sub-check is not triggered. Citations are in-range and support their derivations.

**surface-or-evidence — pass (no-op for this kind).** This is not a refinement of operator/theme
surface text and asserts no new rotation_claim — it is pure frontmatter typed-edge hygiene migrating
legacy `lowers_to:`/`lifts_from:` to a typed `edges:` block. No surface body is touched. The
record-definition sub-check does not apply: the signature-named result records (`{ residual, coeffs }`,
`Scalar`) already have their definition homes in the existing (untouched) chapter §Signature sections.
Inapplicable; marked pass.

**rotation-quality — pass (not applicable).** No algebraic/structural rotation is asserted by a
frontmatter typed-edge migration; the chapters' rotation content is pre-existing and unmodified.
Inapplicable; marked pass.

**variant-axis-coverage — pass.** No new variant analysis. The pre-existing `variant_axes:` block on
both files is preserved verbatim per the producer's scope note (it follows the `edges:` block in the
new frontmatter), so the `gs_orthog`/`dot-hook`/`element-type` axes on orthogonalize and the
`element-type` axis on nrm2 are carried unchanged. Nothing hidden. Marked pass.

**cross-reference-integrity — pass.** Every authored edge target resolves to an existing on-disk
file: for `L3/orthogonalize` — `L2/orthogonalize`, `L3-L2/orthogonalize-variant-split`, `L3/dot`,
`L3/axpy` (depends-on) and `concepts/{sequential-obstruction,tensor-field-lift,variant-absorption,
orthogonalization}`, `L1/orthogonalize`, `L3/chebyshev`, `L3/eigsolve` (reference); for `L3/nrm2` —
`L1/nrm2`, `L2/nrm2`, `L3/dot` (depends-on) and `L4/nrm2`, `L2/inner_product`, `concepts/nrm2`
(reference). All 16 targets verified present. No firm-body-inside-fence concern (frontmatter-only;
no chapter body is authored inside the proposed-changes fence). Marked pass.

**edge-label-fidelity — warning.** The authored edges are themselves faithful to the chapters' own
prose + legacy fields, and the `kind:` qualifiers (`lowers-to`/`composes`) are correctly assigned
(`lowers-to` for the adjacent-layer/theme lowering edges; `composes` for same-layer body primitives).
RE2 is honored: only OUTBOUND edges were authored from `L3/orthogonalize`; no forced inbound edge was
manufactured to flip it reachable (verified against RE2 in `scaffolding/graded-stack-baseline-exceptions.md:129`).
The `L3/nrm2 → L2/nrm2` edge is a genuine adjacent-layer dependency (`L3/nrm2.md:98`, "L3 `nrm2`
lowers to L2 `nrm2` as identity-in-form"), so the +1 reachable is a faithful GROUND, not a
manufactured flip — and it is exactly the RE5 promotion mechanism (`baseline-exceptions.md:132`,
"grounding of the consuming leg … carries liveness down … via the existing faithful `depends-on`
edges"). HOWEVER, one derivation-prose claim is inaccurate and warrants a flag: the report repeatedly
states the same-layer `L3/dot`/`L3/axpy` `composes` edges "Mirror the `L3/dot` template's
same-layer-op-as-depends-on pattern" (CYCLE.md `:176`, and similar at `:78-81`). The `L3/dot.md`
template carries NO same-layer depends-on — its only `depends-on` is the next-layer `L2/inner_product`
(verified on disk: `L3/dot.md` edges block has `depends-on: [L2/inner_product]`, `reference: [L4/dot]`,
nothing same-layer). So `L3/dot` is not a precedent for a same-layer-op `depends-on`/`composes` edge.
The authored edges remain independently faithful (orthogonalize's own §Dependencies `:366-374`
explicitly names `dot`+`axpy` as body primitives), so this is a mis-stated precedent in the rationale,
not an unsupported edge — a warning, not a fail.

**plan-kind-consistency — pass.** This is genuinely typed-edge hygiene, not disguised new authoring.
No chapter body is rewritten, no new operator algebra is introduced, `variant_axes:` is preserved
verbatim, and the index/dep-map tables are explicitly deferred (CYCLE.md `:268-271`). The declared
shape (frontmatter `rank:` + `edges:` migration) matches the content. Marked pass.

**skill-uptake-survey — pass.** The producer references the relevant procedural surfaces — the
graded-stack scheme (`graded-stack-scheme.md` §1/§2/§5), the templates (`L2/krylov-step.md`,
`L2/orthogonalize.md`, `L3/dot.md`), and `citecheck --anchor` (cited as the on-disk self-verification
path in the touched chapters' evidence). No missing-skill telemetry. Marked pass.

### Rank-well-foundedness (graded-stack check 9)

Verified directly against on-disk dep ranks. `rank(u) ≤ rank(dep)` for every authored `depends-on`
edge (`reference` edges ignored, per scheme):

- **`L3/orthogonalize`** = `partial-obstruction` (sub-rank ≈2.5). Deps: `L2/orthogonalize` `rank: firm`
  (3) ✓; `L3/dot` `rank: firm` (3) ✓; `L3/axpy` `firmness: firm` (typed-no-rank → vacuous in the rank
  check) ✓; `L3-L2/orthogonalize-variant-split` carries NO frontmatter / NO `rank:` token (untyped →
  vacuous) ✓. No violation.
- **`L3/nrm2`** = `firm` (3). Deps: `L1/nrm2` `rank: firm` ✓; `L2/nrm2` `rank: firm` ✓; `L3/dot`
  `rank: firm` ✓. firm-rests-only-on-firm holds.

The `partial-obstruction` rank matches `L3/orthogonalize.md` §Status (`:448`). The producer's reported
`rank_violations HELD 0` is consistent with this hand-check.

### Reachability (graded-stack check 10) + baseline-exception conformance

The three CRITICAL claims check out:
- **RE2 honored** — `L3/orthogonalize` stays unreachable (GARBAGE), no forced inbound edge. Confirmed:
  all authored edges from this node are outbound; RE2 (`baseline-exceptions.md:129`) explicitly forbids
  a forced `L4/krylov-step → L3/orthogonalize` edge, and none was added. ✓
- **+1 reachable is a faithful `L2/nrm2` ground** — via the genuine adjacent-layer `L3/nrm2 → L2/nrm2
  (lowers-to)` edge from already-reachable `L3/nrm2`. This is the RE5 transitive-grounding-of-the-
  consuming-leg mechanism, not a manufactured flip. ✓
- **F1/F2/F3 sanity** — F1 (untyped HOLDS at 60 for legacy-edged files, not 60→58) is plausible and a
  genuinely useful campaign-tracker correction; the producer ties it to the linter's `read_any_edge`
  logic. F2 (the measurable rescue is `L2/nrm2`, not a self-flip) is consistent with the RE5 mechanism.
  F3 (`L3-L2/orthogonalize-variant-split` stays detritus, RE2-shadowed; the UPPER-endpoint `lowers-to`
  edge is structurally-correct-but-latent) is correct: the theme has no frontmatter and its only inbound
  is the now-authored edge from the RE2-unreachable `L3/orthogonalize`, so it remains garbage by RE2
  design — appropriately routed to an OQ rather than force-edged or deleted (GROUND-don't-remove
  disposition). All three findings are sound; none over-claims.

### Issues found

1. **edge-label-fidelity / mis-stated precedent (CYCLE.md §Faithful-edge derivation, `:176`; echoed
   `:78-81`).** Severity: low. The report justifies the same-layer `L3/dot`/`L3/axpy` `composes` edges
   as "Mirror[ing] the `L3/dot` template's same-layer-op-as-depends-on pattern." The on-disk `L3/dot.md`
   carries no same-layer `depends-on` (its sole `depends-on` is the next-layer `L2/inner_product`); it
   is therefore not a precedent for a same-layer-op edge. The authored edges remain faithful to
   orthogonalize's OWN §Dependencies (`:366-374`), so the edges are correct — only the cited precedent
   is wrong. Candidate for a one-line rationale correction (drop or re-target the "L3/dot template"
   precedent claim for the same-layer edges; the legitimate same-layer-`composes` precedent, if one is
   wanted, is the body-primitive convention itself, not L3/dot).

2. **OQ for the rank-linter maintainer (CYCLE.md §Open-questions, `:262-267`) — not a defect, noted
   for completeness.** The producer flags that it did not independently verify the linter keys off
   `obstruction_resolution: firm` for any downstream-satisfaction rule (no firm consumer currently
   `depends-on` `L3/orthogonalize`, so the path is untested here). This is honestly disclosed and
   correctly routed; it does not impeach the authored frontmatter (which is faithful to the scheme
   regardless). No action required of the report.

## Repair

### Fixes attempted

- **Finding**: edge-label-fidelity / mis-stated precedent (CYCLE.md `:176`, echoed `:78-81`) — the
  same-layer `L3/dot`/`L3/axpy` `composes` edges are justified as "mirror[ing] the `L3/dot` template's
  same-layer-op-as-depends-on pattern", but `L3/dot.md` on disk carries no same-layer `depends-on` (its
  only `depends-on` is the next-layer `L2/inner_product`), so it is not a precedent for a same-layer-op
  edge. The authored edges remain faithful to orthogonalize's own §Dependencies (`:366-374`).
- **Decision**: repaired.
- **Action**: Surgical one-passage rationale correction in CYCLE.md §Faithful-edge derivation,
  `L3/orthogonalize.md` derivation, the `depends-on: L3/dot, L3/axpy (kind: composes)` bullet (the
  `:176` line). Replaced the inaccurate "Mirrors the `L3/dot` template's same-layer-op-as-depends-on
  pattern" sentence with a corrected justification grounding the `composes` edges in orthogonalize's
  OWN §Dependencies "Same-layer (L3)" (`:366-374`) — naming the body-primitive convention itself as the
  basis, and explicitly noting that `L3/dot.md` carries no same-layer `depends-on` (its sole `depends-on`
  is `L2/inner_product`) so it is not the precedent. The proposed `edges:` blocks were NOT touched (they
  are correct and the inline `# same-layer body primitive` comments at `:78-81` are accurate as-is; the
  `:78-81` echo is the corresponding edge block, which states no precedent claim and needs no change).

### Unrepairable findings

None. The single warning was a mis-stated precedent in rationale prose (mechanical/surgical), repaired
in-place without authoring substantive content or touching the deliverable edges.

## Suggested resolution

`ready`. The lone low-severity edge-label-fidelity warning was a rationale-prose accuracy defect, not an
unsupported edge — the authored `edges:` blocks are independently faithful to each chapter's own
§Dependencies / legacy fields and were verified sound by the critic (rank-well-foundedness ✓,
reachability/RE2/RE5 ✓, all 16 edge targets present). The precedent claim is now corrected. Integrator
note: this is a frontmatter-only typed-edge migration (index/dep-map tables explicitly deferred per
CYCLE.md `:268-271`); the producer's OQs (rank-linter `obstruction_resolution: firm` keying; F3
`L3-L2/orthogonalize-variant-split` staying RE2-shadowed detritus) are honestly disclosed and route to
the OQ ledger, not blocking.
