---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T08:51:50Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-07T09:05:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: unrepairable
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: needs-revision
follow_up_agent: integrator-per-report
---

# META: verification of "L1 — AMR estimate/mark group-intro (deferred c122 navigational hygiene)"

## Critique

### Checks run

**citation-validity — pass.** This is a `navigational-container (group intro)` page: it makes no new operator-algebra claim and restates only the one-line semantics of two already-firm, already-cited verbs (per the precedent group-intro shape, the citation check largely no-ops). The orientation prose carries a small number of bare-file orientation pointers (`palace/drivers/basesolver.cpp` for `SolveEstimateMarkRefine`) and one load-bearing pinpoint, `palace/utils/configfile.hpp:97-119`, for the `RefinementData` / `update_fraction` (θ) IoData surface. I read that range on disk: it is exactly `struct RefinementData { ... double update_fraction = 0.7; ... }` (the Dörfler update fraction documented there) — the citation precisely backs the claim, and it matches the same range already cited in the firm `dorfler_mark` dep-map row (`L1/index.md:209`). No off-by-one, in-range. The supporting-evidence Status-line citations (`flux_recovery_estimate.md:250`, `dorfler_mark.md:281`) were verified on disk (see plan-kind-consistency). Pass.

**surface-or-evidence — pass.** Not a refinement-shaped proposal: the page authors no surface change to an existing operator/theme and makes no rotation_claim. It is a pure navigational container (the precedent `fe-space-intro.md` / `mesh-construction-intro.md` kind). The record-definition sub-check: the prose names the `RefinementData` config record, but the page is NOT the definition home and does not purport to be — it correctly routes the record to its cross-cutting concept-page home `concepts/RefinementData.md` (the ≥2-consumer case), so the record-definition obligation is satisfied by reference (modulo that page's existence — tracked under cross-reference-integrity). Pass.

**rotation-quality — pass (not applicable to navigational-container kind).** A group-intro rotates nothing; it indexes already-firm vocabulary via `reference`-only edges. No rotation claim is asserted. No-op.

**variant-axis-coverage — pass (not applicable to navigational-container kind).** The page has no variant axes of its own; the flux-channel (Grad/Curl) axis lives in `flux_recovery_estimate` (and is already covered there). The intro merely names it in passing. No hidden branch.

**cross-reference-integrity — warning.** Of the four outbound links in the proposed file, three resolve on disk now: `./flux_recovery_estimate.md`, `./dorfler_mark.md` (both in `book/src/L1/`), and `../L1-L0/amr-estimate-mark-refine.md` (exists, `status: firm`). The fourth, `../concepts/RefinementData.md`, does NOT exist on disk at critique time — it is created by the co-dispatched D4 this same cycle. This is a genuine cross-dispatch ordering dependency: a live SUMMARY/mdBook link to a missing file is a hard `linkcheck2` error, so if D4 does not land (dropped at repair/integration) the build breaks unless the link is defanged. The producer flagged this explicitly in Open questions with a clear defang fallback and integrator-sequencing instruction. The GATE itself (group-intro file created BEFORE SUMMARY nests it) is correctly observed — the SUMMARY `[new]` block points the new grouping link at the freshly-created `amr-estimate-mark-intro.md`, and `grep` confirms that file is not yet referenced anywhere in SUMMARY (no duplicate/placeholder). Marking `warning` (not `fail`) because the dependency is real but explicitly identified with a defang fallback; it is an integration-sequencing item, not an authoring defect.

**edge-label-fidelity — pass.** The frontmatter declares `reference`-only edges to `L1/dorfler_mark` and `L1/flux_recovery_estimate` (no `rank:`, no `depends-on`), exactly matching the navigational-container precedent and the actual two members the prose discusses. The prose correctly characterizes the sibling estimate▷mark dataflow as a `reference`/dataflow relation, NOT a `depends-on` (the marker is agnostic to indicator provenance) — consistent with the on-disk `dorfler_mark` dep-map row which also records `flux_recovery_estimate`/`refine` as `reference`, not deps. Edge labels and prose agree. Pass.

**plan-kind-consistency — pass.** Declared kind is `navigational-container (group intro)` and the content shape matches exactly: no `rank:`, `reference`-only edges, one-paragraph orientation, per-member lines, trailing "Chapters are listed alphabetically." — mirroring `fe-space-intro.md` verbatim in structure. Both members are genuinely `firm` on disk: `flux_recovery_estimate.md` frontmatter `rank: firm`/`status: firm`, `## Status` line (`:250`) reads `` `firm` (AMR estimate verb; ...) ``; `dorfler_mark.md` frontmatter `rank: firm`, `## Status` line (`:281`) reads `` `firm` — the operator's structure is read directly from positive Palace source ... ``. The L1/index.md de-stale (dropping "Rough-in" from the dep-map TABLE group-header `:208`) is justified — the anchor matches exactly and uniquely (`grep -c = 1`), the verb rows (`:209-210`) already read `firm`, and the parallel narrative cohort header (`:134`) already reads `Firm (AMR estimate/mark vocabulary)`. The producer's analysis of the two-separate-headers situation is correct. Pass.

**skill-uptake-survey — pass.** The relevant procedural disciplines (the `new-summary-kind-grouping-placeholder-link-duplicate-file-build-break` GATE, the `index-table-status-cell-drifts-when-theme-file-promoted` drift class, the `fe-space-intro.md`/`mesh-construction-intro.md` precedent) are all named in the report. No dedicated skill is implied beyond these documented disciplines, which are referenced. Telemetry-only check; nothing blocking.

### Issues found

1. **`../concepts/RefinementData.md` does not exist at critique time** — `reports/.../CYCLE.md` proposed file `book/src/L1/amr-estimate-mark-intro.md`, closing paragraph (proposed-changes line ~111). Severity: medium (build-blocking IF the co-dispatched D4 does not land this cycle). The link targets a concept page created by the co-dispatched D4 (`RefinementData` record-definition page) in the same wave. The producer has already flagged this in Open questions with an explicit defang fallback (drop the link to plain text / drop the sentence) and an integrator-sequencing instruction (apply D4 before D1, or defang). This is a cross-dispatch ordering coupling, not an authoring error — surfaced for the repairer/integrator to confirm D4 landing or apply the defang. All other outbound links resolve on disk.

### Notes (non-issues)

- The report-prose Summary section (CYCLE.md lines 16-18) writes the member links as `../book/src/L1/...` (wrong relative depth), but these are in the report narrative, NOT in the proposed-changes block; the actual proposed file content uses the correct `./flux_recovery_estimate.md` / `./dorfler_mark.md`. No artifact impact.
- The SUMMARY `[old]` anchor (FE-space sub-spine block through the two flat AMR verbs, lines 239-246) matches the on-disk SUMMARY exactly and uniquely; the L1/index.md `[old]` header anchor (`:208`) matches exactly and uniquely. Both edits will apply cleanly. The shared-file SUMMARY coupling with D2/D4 (disjoint regions) is correctly flagged for the integrator and is parallel-safe by per-report on-disk re-read.

## Repair

### Fixes attempted

- **Finding**: `../concepts/RefinementData.md` does not exist on disk at critique time — the proposed group-intro `book/src/L1/amr-estimate-mark-intro.md` links to a concept page created by the co-dispatched D4 (RefinementData record-definition page) this same cycle; a live link to a missing file is a hard `linkcheck2` build error.
  - **Decision**: unrepairable (deferred-to-integration / not-a-repair).
  - **Rationale**: This is a cross-dispatch ordering coupling, NOT an authoring defect. The link is a legitimate same-cycle forward-reference: D4 lands `concepts/RefinementData.md` THIS cycle, so the correct resolution is integration sequencing, not a content edit. Deleting/defanging the link now would corrupt a valid forward-reference if D4 lands (the expected case). The repairer's authority is mechanical/surgical fixes that do not author content or resolve cross-dispatch coupling that only the integrator can sequence — this exceeds repair scope. No edit applied to the report.

### Unrepairable findings

- **cross-reference-integrity (medium)** → routed to **`integrator-per-report`**. **Required action: apply D4 (the `concepts/RefinementData.md` record-definition page) BEFORE D1 (this group-intro)** so the `../concepts/RefinementData.md` cross-link resolves at `cargo make book` rebuild. Do NOT delete the link if D4 is landing — it is a legitimate same-cycle forward-reference. **Fallback (only if D4 is dropped at repair/integration):** apply the producer's flagged defang — drop the `../concepts/RefinementData.md` cross-link to plain text / drop the sentence — to keep the build green. The GATE (group-intro file created before SUMMARY nests it) is already correctly observed; this is purely an inter-report apply-ordering item, no content work.

## Suggested resolution

`needs-revision` because of one unrepairable cross-dispatch ordering coupling — but there is **no content work** to do. The integrator (`integrator-per-report`) must serialize the per-report applies so **D4 (RefinementData concepts page) is applied BEFORE D1 (this AMR estimate/mark group-intro)**. With that ordering, all four outbound links resolve and the build is green. If D4 is not landing this cycle, apply the producer's defang fallback instead (drop the RefinementData cross-link to plain text). All other checks are clean: both members (`flux_recovery_estimate`, `dorfler_mark`) are firm on disk, the new-grouping GATE is observed, the navigational-container kind + `reference`-only edge labels are correct, and all anchors match exactly.
