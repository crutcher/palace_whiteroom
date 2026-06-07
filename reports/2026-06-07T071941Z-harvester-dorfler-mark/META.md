---
verifies: ../REPORT.md
critiqued_at: 2026-06-07T074500Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: warning
  skill-uptake-survey: pass
repaired_at: 2026-06-07T080000Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: repaired
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: repaired
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "Formalize dorfler_mark at L1"

## Critique

### Checks run

**citation-validity — pass.** `citecheck --scan` reports 35/35 citations in bounds. All load-bearing
anchors were re-verified directly on-disk against `reference/palace/...` (the producer's stated reason
for the on-disk read — codemap `read_range` +1/+3 drift on this file's comment/brace boundaries — is
respected; I verified against the on-disk file, not `read_range`, per the cross-reference-integrity
discipline). Spot-confirmed exact: `dorfler.cpp:20` (`std::sort` ascending), `:28` (`std::partial_sum`),
`:34-36` (pivot comment + `std::lower_bound` on `(1-fraction)*local_total`), `:38` (`error_threshold`),
`:160-162` (the over-mark comment — text matches verbatim: "Always choose the lower threshold value…
Would rather over mark than under mark, as Dörfler marking is the smallest set that covers at least the
specified fraction of the error"), `:163` (`error_threshold = min_threshold`), `:167-169`
(`MFEM_VERIFY(error_marked >= fraction * error.total, … Dorfler marking predicate failed!)`),
`:173` (`ComputeDorflerCoarseningThreshold` taking `mfem::ParMesh` — the coarsening-sibling claim is
correct). `basesolver.cpp:103-115` MarkedElements verifies exactly (`:103` sig, `:106` Reserve, `:107`
loop, `:109` `e[i] >= threshold`, `:111` Append, `:114` return); the caller `:220-233` verifies
(`:223-224` `ComputeDorflerThreshold(comm, indicators.Local(), refinement.update_fraction)`, `:225`
MarkedElements). `configfile.hpp:97-119` RefinementData verifies (`:117-118` Dörfler comment, `:119`
`update_fraction = 0.7`). `dorfler.hpp:21-29` verifies (criterion spec + Dörfler-1996 citation +
declaration). The `verified_against:` YAML block (CYCLE.md :397-437) round-trips cleanly under
`yaml.safe_load` (10 entries; every `note:` begins with prose, no leading-quote scalar issue). All
on-disk anchors hold; no drift found.

**surface-or-evidence — pass.** This is a refinement-shaped proposal (rough-in dep-map row → firm full
chapter) backed by positive L0 source read in full; not a pure rotation_claim. The record-definition
sub-check: two records are named in the signature. `IndexSet[N]` is defined in-chapter (§Record
definition) with fields/meaning/L0 home — correct single-consumer in-chapter home. `θ : Real` is
correctly noted as a scalar (not a record) whose config home is `RefinementData`; the producer does NOT
attempt to define `RefinementData` here (it is ≥2-consumer cross-cutting) and instead flags
`record-RefinementData-needs-concept-definition-home` in Open questions, routing it to a
`concepts/RefinementData.md` page — exactly the record-definition-obligation discipline for a
multi-consumer record. No "described only by USE" gap.

**rotation-quality — pass (with a localization nuance, see Issues).** This is an L1 harvest
(mutation→pure-function lift), not an inter-layer algebraic rotation, so the rotation check is the
L0→L1 mutation-elimination: the imperative `ComputeDorflerThreshold ▷ MarkedElements` (in-place sort /
square / partial_sum on copies + threshold bisection + append loop) is lifted to the pure
`dorfler_mark(θ, e) → IndexSet`, hiding the threshold pivot as an internal quantity. That is a genuine
state-hiding compression (the L1 form drops the threshold scalar, the mutable buffers, and the bisection
machinery), not a rename. Pass.

**variant-axis-coverage — pass.** Axes are enumerated and dispositioned: fraction θ (continuous
parameter, not behavioural — marking shape is θ-uniform); rank multiplicity (single-rank-absorbed,
multi-rank deferred per DIRECTIVE-1, explicitly scoped out, not a hidden branch); refinement-vs-
coarsening (the `ComputeDorflerCoarseningThreshold` sibling is explicitly NOT folded — distinct input
`mfem::ParMesh` + derefinement opportunities, verified on-disk at `:173`, flagged
`dorfler-coarsening-threshold-sibling-verb` for a future harvest). No hidden branches.

**cross-reference-integrity — warning.** The on-disk targets that exist resolve (`nrm2.md`,
`reciprocal.md`, `set_subvector_zero.md`, `amr-estimate-mark-refine.md`, `feature/lifecycle.L4.md`).
Three referenced targets are MISSING on disk: (a) `book/src/L1/flux_recovery_estimate.md` — linked
multiple times in prose and the dep-map; this is the D1 sibling landing the SAME cycle, and the producer
correctly frames it as a forward-reference resolving when D1 lands (acceptable per the same-cycle-cohort
convention, but a build-time risk if D1 slips); (b) `book/src/L1/amr-estimate-mark-intro.md` — the
producer's `edit:book/src/SUMMARY.md` block registers a NEW sub-chapter group whose intro page does NOT
exist, which is a hard `linkcheck2` error unless the integrator materializes it in the SAME finalize;
the producer flags this explicitly (OQ + the SUMMARY-group-intro-needed note) and routes it to the
integrator/layer-intro-author; (c) `book/src/concepts/RefinementData.md` — correctly NOT linked as a
live `[link]` (only named as a future OQ target), so not itself a broken link. Warning (not fail)
because every missing target is explicitly flagged and routed by the producer; the load-bearing risk is
the SUMMARY group-intro, which MUST land same-finalize.

**edge-label-fidelity — pass.** The `lowers-to` edge to `L1-L0/amr-estimate-mark-refine` is an L1>L0
edge and the prose (§Downward to L0) discusses exactly that L1→L0 lowering (the pure set-selection →
imperative `ComputeDorflerThreshold ▷ MarkedElements`). The `cites-evidence` edges point at L0 source.
No edge-label/prose mismatch.

**plan-kind-consistency — warning.** Declared kind is `firm` via the firm-on-positive-structure escape.
The escape is correctly invoked (every law is a syntactic identity on fully-read positive source; the
no-dedicated-test caveat is non-gating, matching the `set_subvector_zero`/`reciprocal` precedent; the
`MFEM_VERIFY` at `:167-169` is a positive in-source post-condition stronger than a test). The structure
is genuinely firm. The warning is narrower (see Issues): law 4's *single-rank mechanism* is mis-located
to `:163` (a multi-rank-only line), which is a precision issue inside an otherwise-firm entry, not a
mis-classification of the entry's kind.

**skill-uptake-survey — pass.** The producer references the c108 §5 L1-op→theme grounding convention,
the firm-on-positive-structure precedents, and the on-disk-bypass-of-codemap-drift practice; the
`partly-constructive-promotion-checklist`-class reasoning is applied via the firm-on-positive-structure
escape. No missing skill invocation implied by the shape.

### Issues found

1. **[plan-kind-consistency / rotation-quality, low-medium] Law 4's single-rank mechanism is cited to a
   multi-rank-only line (`dorfler.cpp:163`).** CYCLE.md :209-214 (law 4) and :169-180 (§Semantics
   over-mark paragraph) pin the load-bearing over-mark tie-break to `error_threshold = min_threshold`
   (`:163`). On-disk, `:163` is the **bracket selection at the END of the cross-rank bisection** — it
   chooses the lower of `min_threshold`/`max_threshold`. At single-rank (the reading this entry adopts
   per DIRECTIVE-1) `min_threshold == max_threshold == error_threshold` (`:64-67`, GlobalMin/Max over
   one rank are identities), so `:163` is the **identity** — it returns the local pivot already computed
   at `:36-38`. The genuinely single-rank, genuinely load-bearing over-coverage property law 4 asserts
   ("the marked set covers ≥θ, realized by choosing the *lower* threshold / over-marking") is actually
   produced by the **`std::lower_bound` pivot at `:36`** (the first prefix position leaving (1−θ) below
   it ⇒ the smallest E achieving ≥θ coverage), and *confirmed* by the `MFEM_VERIFY` at `:167-169`. So
   law 4's CLAIM is correct and load-bearing at single-rank, but its CITED mechanism (`:163`) is the
   multi-rank tie-break, which is degenerate single-rank. The fix is to re-anchor law 4's single-rank
   mechanism to the `:36` lower_bound (with `:167-169` as the post-condition witness) and note that
   `:163` is the multi-rank bracket selection that degenerates to identity single-rank. Location:
   CYCLE.md §Semantics :169-180, §Algebraic-laws law 4 :209-214, and the index-row "over-mark tie-break
   `:163`" at :442. Severity low-medium: the law is true and load-bearing; only the source-line
   localization is off for the single-rank reading the entry commits to.

2. **[cross-reference-integrity, medium] SUMMARY edit registers a new sub-chapter group whose intro
   page does not exist.** CYCLE.md :445-448 (`edit:book/src/SUMMARY.md`) adds
   `- [AMR estimate & mark](./L1/amr-estimate-mark-intro.md)` as a group header, but
   `book/src/L1/amr-estimate-mark-intro.md` is MISSING on disk. A SUMMARY entry pointing at a
   nonexistent file is a hard `linkcheck2`/`mdbook build` failure. The producer flags this explicitly
   (OQ "SUMMARY group-intro `amr-estimate-mark-intro.md` needed", :499-508) and routes the materialize
   to the integrator/layer-intro-author. Load-bearing for build-readiness: the integrator MUST either
   create the intro (a stub seed suffices) in the same finalize, or place `dorfler_mark` under an
   existing group. Location: CYCLE.md :445-448, :499-508.

3. **[cross-reference-integrity, low] `flux_recovery_estimate.md` forward-reference is unresolved on
   disk.** CYCLE.md links `[flux_recovery_estimate](./flux_recovery_estimate.md)` in prose/dep-map
   (:76, :82, :251, the index row), but the target does not yet exist — it is the D1 sibling of this
   same cycle. Acceptable under the same-cycle-cohort convention (both endpoints land together), but a
   build-time risk if D1 does not land in the same finalize. Location: CYCLE.md :76, :82, :251, :442.

4. **[citation-validity, informational — NOT a defect] Empty-mesh guard citation slightly conflated.**
   CYCLE.md :143-144 attributes the `N=0` empty-set guard to "the L0 guards `estimates.size() > 0`,
   `dorfler.cpp:35,38`". On-disk, `:35` guards `sum.size() > 0` (→ `local_total = 0.0`) and `:38`
   guards `estimates.size() > 0` (→ `error_threshold = 0.0`); the producer's gloss collapses both into
   "estimates.size() > 0". Both lines genuinely implement the empty-mesh guard, so the citation
   supports the claim; the minor wording imprecision is noted for completeness, not flagged as a
   citation failure.

### Notes for the repairer

- Issue 1 is the load-bearing one: it does not block `firm` (the structure is firm; the law is true),
  but the single-rank entry should cite `:36` (lower_bound) as law 4's single-rank mechanism and
  reframe `:163` as the multi-rank bracket-selection that degenerates to identity single-rank. This is
  a surgical re-anchoring of two prose spans + the index-row token, fully within repair authority.
- Issue 2 is a cross-report/integrator concern already flagged by the producer; the repairer may
  surface it but the materialize-the-intro action is the integrator's. No CYCLE.md edit needed beyond
  confirming the flag is prominent.
- Issue 3 is same-cycle-cohort expected; no repair needed beyond the existing forward-ref framing.
- The `Tensor[N]` flat rank-1 convention is CORRECT and independently confirmed against the live
  semantic surface `book/src/semantics/index.md` §1.2 (lines 68, 85, 95, 314): `Tensor[N]` is reserved
  for genuinely rank-1 flat vectors, and at L1/L0 the rank-1 spelling is faithful. The per-element
  indicator vector has no rank-agnostic congruence to assert, so a named shape group would be wrong
  here. (Note: CLAUDE.md's prose still names the surface `book/src/design/l4_calculus.md`, which no
  longer exists on disk; the report correctly cites the live `book/src/semantics/index.md` path.) No
  action.

## Repair

### Fixes attempted

- **Finding 1 (Issue 1, plan-kind-consistency / rotation-quality, low-medium):** law 4's single-rank
  over-mark MECHANISM was mis-cited to `dorfler.cpp:163` (the multi-rank bisection bracket selection
  `error_threshold = min_threshold`, which degenerates to identity single-rank since
  `min_threshold == max_threshold == error_threshold` `:64-67`). The genuinely single-rank over-coverage
  is produced by the `std::lower_bound` pivot at `:36`, witnessed by the `MFEM_VERIFY` post-condition
  `:167-169`.
  - **Decision:** repaired.
  - **Action:** verified on-disk against `reference/palace/palace/utils/dorfler.cpp` (`:34-38` =
    pivot/threshold block; `:160-163` = the always-choose-lower bracket selection; `:167-169` =
    `MFEM_VERIFY` coverage post-condition — critic's analysis confirmed exactly). Surgically
    re-anchored law 4's single-rank mechanism to `:36` (keeping `:167-169` as the post-condition
    witness) and reframed `:163` as the multi-rank bracket-selection tie-break that degenerates to
    identity single-rank, in four spans: CYCLE.md §Semantics "the load-bearing over-mark tie-break"
    paragraph; §Algebraic laws law 4; the `edit:book/src/L1/index.md` row token ("over-mark lower-bound
    pivot `:36` … multi-rank bracket-selection tie-break `:163` … degenerates"); and the
    `verified_against` notes for `:36` (now flags it as law 4's single-rank mechanism) and `:163` (now
    flags it as the multi-rank tie-break degenerating to the `:36` pivot single-rank). The law's CLAIM
    was already correct + load-bearing — only the source-line localization for the single-rank reading
    was off; the `firm` rank is undisturbed (structure firm, claim true).

- **Finding 2 (Issue 2, cross-reference-integrity, medium):** the `edit:book/src/SUMMARY.md` block
  registered a NEW `AMR estimate & mark` sub-chapter group whose intro page
  `book/src/L1/amr-estimate-mark-intro.md` does NOT exist on disk → hard `linkcheck2`/`mdbook` missing-file
  error at rebuild. Creating a group-intro page is authoring (beyond repairer mechanical scope).
  - **Decision:** repaired (build-clean fallback).
  - **Action:** changed the SUMMARY registration from the nested-under-nonexistent-group-intro form to a
    **flat top-level registration** — `- [dorfler_mark](./L1/dorfler_mark.md)` pointing only at the
    on-disk chapter, with an inline REPAIRER NOTE in the edit block giving the integrator the exact
    placement (a top-level entry within the `# L1` Part, which mdbook accepts) and the deferred re-nest
    instruction. Also refined the producer's existing OQ `SUMMARY group-intro amr-estimate-mark-intro.md
    needed` to record the applied flat fallback + route the group-intro authoring + re-nest to the c123
    layer-intro-author (NOT required for this finalize — the flat fallback keeps `linkcheck2` green
    without it). Coordinated with D1: the note instructs D1's `flux_recovery_estimate` to take the SAME
    flat fallback so both avoid the identical broken link, and both re-nest together once the group-intro
    lands.
    NOTE on structure: the live L1 SUMMARY is entirely by-kind group-nested (no pre-existing flat list);
    the flat top-level entry is the minimal build-clean move that introduces no new (unauthored)
    group-intro and makes no semantic group-placement claim. The by-kind grouping convention is honored
    on the deferred re-nest, not violated — the flat entry is an explicitly-transient build-clean state.

- **Finding 3 (Issue 3, cross-reference-integrity, low):** `flux_recovery_estimate.md` forward-reference
  unresolved on disk.
  - **Decision:** not-needed.
  - **Rationale:** same-cycle-cohort (D1 lands the target this cycle); the producer's forward-ref framing
    is correct and the convention permits it. No edit required.

- **Finding 4 (Issue 4, citation-validity, informational):** empty-mesh guard citation gloss collapses
  `:35` (`sum.size() > 0`) and `:38` (`estimates.size() > 0`) into "estimates.size() > 0".
  - **Decision:** not-needed.
  - **Rationale:** the critic explicitly flagged this as NOT a defect — both lines genuinely implement
    the empty-mesh guard, so the citation supports the claim. Cosmetic wording only; left as authored to
    avoid out-of-scope content churn.

### Unrepairable findings

None. Both warning-level findings were mechanically/surgically repairable within repair authority
(Issue 1 = citation re-anchor verified on-disk; Issue 2 = the safe build-clean flat-registration
fallback, with the authoring portion — the group-intro page — explicitly deferred to c123
layer-intro-author, not blocking this finalize).

## Suggested resolution

`overall_status: ready`. All eight checks now pass-or-repaired-or-not-needed; the two warnings are
resolved (Issue 1 re-anchored; Issue 2 made build-clean via flat registration). Notes for the integrator:

- The SUMMARY edit is now a **flat** top-level `- [dorfler_mark](./L1/dorfler_mark.md)` entry — place it
  within the `# L1` Part (after `- [Overview](./L1/index.md)` is fine). Do NOT recreate the nested
  `AMR estimate & mark` group header (its intro page does not exist).
- Coordinate the cross-report cohort: D1's `flux_recovery_estimate` should land the SAME flat fallback
  this finalize. Both forward-references (`flux_recovery_estimate.md`, `dorfler_mark.md`) then resolve.
- Carry forward the two firm-flip / cross-report OQs the producer flagged: the
  `amr-estimate-mark-refine` theme `rough-in → firm` flip once BOTH L1 endpoints are on disk firm, and
  the c123 layer-intro-author authoring of `amr-estimate-mark-intro.md` + the deferred re-nest of both
  flat lines under the group header.
- The new record/sibling OQs (`record-RefinementData-needs-concept-definition-home`,
  `dorfler-coarsening-threshold-sibling-verb`) are correctly out-of-scope and routed.
