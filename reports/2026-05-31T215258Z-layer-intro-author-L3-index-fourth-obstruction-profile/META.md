---
verifies: ../CYCLE.md
critiqued_at: 2026-05-31T21:59:07Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-31T22:07:00Z
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

# META: verification of "L3 index — fourth obstruction profile + consolidated firm-count tally"

## Critique

### Checks run

**citation-validity — pass.** The report is intro/overview maintenance whose edits are prose; the only source-line citation in the proposed-changes is `palace/linalg/divfree.cpp:175`, carried unchanged from the already-integrated c038 §Working-Notes bullet. I confirmed it: `reference/palace/palace/linalg/divfree.cpp:175` is exactly `ksp->Mult(rhs, psi)` (the inner H1 solve, step 3 of the four-step apply), so the anchor is faithful. The intra-book doc-links and the self-referential `book/src/L3/index.md:NN` line citations are addressed under cross-reference-integrity below. `tools/citecheck/citecheck.py --scan` on the report returns `4 ok, 0 failing`. No `verified_against:` block in this report, so the YAML round-trip sub-check is not applicable.

**surface-or-evidence — pass.** This dispatch modifies surface (the §Semantics-overlay taxonomy prose + §Working-Notes tally) and the modification is anchored in evidence: Edit 1's shape-(d) framing is a faithful continuation of the `divfree-projector.md` §"Iteration-rotation marker" section (lines 233-265, confirmed below). No rotation_claim is asserted — this is taxonomy maintenance, not a new operator/theme rotation — so the refinement-surface rule is satisfied by the surface-change-plus-evidence path.

**rotation-quality — pass (not the primary axis for this report-kind).** No new algebraic/structural rotation is asserted. The report folds an existing, already-firm obstruction-profile observation (`divfree-projector`'s obstruction-carrying-by-reference, firm at c038) into the index taxonomy. The shape-(d) description correctly preserves the `nested-constructed-operator-gate` fidelity rule ("the gate neither introduces a new obstruction nor erases the inner one"), which I cross-checked against `book/src/concepts/nested-constructed-operator-gate.md` §"The cross-layer fidelity rule" (lines 37-55: the inner gate's iteration stays interior to its own lowering theme, does not leak into the outer gate). The spectrum positioning is also faithful — see edge-label-fidelity.

**variant-axis-coverage — pass (not applicable to intro maintenance).** No operator with orthogonal variant axes is authored here. The taxonomy enumerates obstruction *profiles* (a)/(b)/(c)/(d) exhaustively and the report explicitly distinguishes the firm vs partial-obstruction sub-classes and the "whose loop carries the obstruction" axis across (a)/(c)/(d). No hidden branches.

**cross-reference-integrity — warning.** All doc-links in Edit 1 resolve on disk (`./ksp_solve.md`, `./chebyshev.md`, `./eigsolve.md`, `./divfree-projector.md`, `./jacobi-smoother.md`, `./apply_linop.md`, `../concepts/nested-constructed-operator-gate.md` — all present). The fence guard passes: 4 fences, even parity, two balanced `edit:` blocks, no nested fences (`proposed-changes-fence-encloses-full-body-guard` clean — though this is prose-replacement, not a firm-body authoring, so the firm-body-inside-fence concern does not arise). Both `[old]:` strings match the on-disk `index.md` byte-for-byte (full-string match confirmed, not just prefix), so the edits anchor correctly and survive D1's dep-map ROW-append (lines 21-36 region, disjoint from both edit targets at line 15 and lines 57-58). **The warning is the `[normalize](./normalize.md)` live link in Edit 2 [new]:** `book/src/L3/normalize.md` does NOT exist on disk yet, and `book/src/SUMMARY.md` has no `L3/normalize` row (it has `L3/divfree-projector` at line 36 and `L1/normalize` at line 74, but no L3 normalize). This is a hard `linkcheck2` build-break IF applied before D1 lands. The report is fully aware and declared the dependency explicitly (Open-questions/caveats §1: "apply D1's `normalize.md` + dep-map row FIRST, then my edits"; with a defang fallback to plain-text + count rollback to "14 firm + 2" if D1 slips). This is a coordination requirement for the integrator, not a content defect — surfaced here so the integrator sequences D1 before D3. See Issues found #1.

**edge-label-fidelity — pass.** The count arithmetic is correct: the consolidated tally "15 firm + 2 partial-obstruction" enumerates exactly 15 named firm entries (krylov-step c010; apply_linop+axpy+axpby+axpbypcz+dot+nrm2+scal c011 = 8; ksp_solve c020; assemble-diagonal+jacobi-smoother c037 = 2; reciprocal+elementwise_product+divfree-projector c038 = 3; normalize c039 = 1 → 1+8+1+2+3+1 = 16... recount: krylov-step(1) + 7 BLAS-1 wait) — verified by direct enumeration: the 15 names are krylov-step, apply_linop, axpy, axpby, axpbypcz, dot, nrm2, scal, ksp_solve, assemble-diagonal, jacobi-smoother, reciprocal, elementwise_product, divfree-projector, normalize = 15 distinct firm entries; plus chebyshev + eigsolve = 2 partial-obstruction. The "14 after c038 + normalize = 15" framing is arithmetically sound. All 5 already-landed (A)-cohort operators (assemble-diagonal, jacobi-smoother, reciprocal, elementwise_product, divfree-projector) are confirmed firm on disk; normalize is the only one not yet landed (D1 in-flight). The fourth-profile spectrum positioning matches the exemplar verbatim: `divfree-projector.md:259-265` states "obstruction-carrying gate (with `ksp_solve`, `eigsolve`) rather than an obstruction-free leaf (`jacobi-smoother`, `apply_linop`, `dot`, `scal`)" and "`ksp_solve` authors its own fold; `eigsolve` delegates to an opaque library loop; `divfree-projector` delegates to its inner `ksp_solve` gate" — Edit 1's shape-(d) prose reproduces this distinction faithfully, including the between-obstruction-free-and-obstruction-authoring placement. The "Three firm shapes" → "Four firm shapes" reframe is consistent (Edit 1 [new] lead sentence says "Four firm shapes coexist"; Edit 2 [new] tally says "the §Semantics-overlay taxonomy now enumerates four firm obstruction shapes (a)/(b)/(c)/(d)"). Stale-count handling is correct: Edit 2 strips the c038 bullet's trailing "14 firm + 2" / "only normalize remains" / "5-of-6 landed" count sentence and the older c024/c037 inline snapshots are explicitly labeled "superseded snapshots ... not the live count" by the new authoritative tally bullet, so no contradicting live count is left standing.

**plan-kind-consistency — pass.** This is `layer-intro-author` intro/overview maintenance: no new operator chapter is authored (correct for the role), the edits touch only `book/src/L3/index.md` §Semantics-overlay + §Working-Notes, content is L3 vocabulary, and the high→low discipline holds (the taxonomy describes L3 obstruction profiles in L3 terms, with the substantive rotations correctly deferred to the L1>L0 themes named in the preserved narrative). No rough-in placeholders dressed as firm; no kind mis-classification.

**skill-uptake-survey — warning (telemetry only, non-blocking).** The report's shape implies two relevant skills that are not referenced by name: `proposed-changes-fence-encloses-full-body-guard` (the build-readiness fence concern the report itself reasons about in §Summary line 18 and the ordering caveat) and `upgrade-plain-text-ref-to-live-link-when-target-on-disk` / its inverse — the report's defang fallback ("defang my `./normalize.md` link to plain-text") is exactly the `rough-in-rows-must-be-plain-text-when-anchor-missing` convention, which it DOES cite by name. The fence-guard reasoning is present in substance but the skill is not invoked by slug. Pure presence check; surfaced as telemetry, not a defect.

### Issues found

1. **Build-ordering dependency on D1 — live link to not-yet-existing `book/src/L3/normalize.md`.** Location: CYCLE.md Edit 2 [new] (line 39) — `[`normalize`](./normalize.md)` and the "15 firm" count. Severity: medium (coordination, not content). `book/src/L3/normalize.md` is absent on disk and absent from `book/src/SUMMARY.md`; applying this report's Edit 2 before D1's `normalize.md` lands is a `linkcheck2` hard-fail and makes the "15 firm" count premature. The report declared this dependency clearly (Open-questions §1, with apply-ordering recommendation and a plain-text defang + count-rollback fallback). NOT a defect to repair — it is a sequencing instruction for the integrator: **apply D1 (normalize.md + dep-map row) before this report (D3); if D1 slips, defang the link to plain-text and roll the count back to "14 firm + 2 (normalize pending)".** Flagged so the integrator sequences correctly.

2. **Inherited stale self-citation `index.md:41` carried unchanged in the preserved c038 narrative.** Location: CYCLE.md Edit 2 [new] (line 38, preserved c038 bullet) — "(A) firm identity-in-form backfills of the cycle-036 D2 audit verdict (`book/src/L3/index.md:41`)". Severity: low (inherited, not newly introduced). The (A)-cohort verdict list is actually at `index.md:44` (line 41 is the "canonical write-up of when L3 lifts fail" sentence). This `:41` reference is carried verbatim from the already-integrated on-disk c038 bullet (the on-disk index.md line 57 has the same `:41`), so it is pre-existing inherited drift, not a regression this dispatch caused — and the report's NEW normalize bullet (line 39) correctly cites `:44`. The §Semantics-overlay verdict line has shifted (likely from prior row/bullet appends) since the c038 bullet was authored. Worth a one-character correction (`:41`→`:44`) in the preserved narrative if the repairer touches that bullet, but it is not load-bearing to this dispatch's claims and the report carries no new bad anchor.

3. **Skill-by-slug telemetry gap (non-blocking).** Location: CYCLE.md §Summary line 18 + Open-questions §1. The fence-readiness reasoning maps to `proposed-changes-fence-encloses-full-body-guard` and the defang fallback maps to a plain-text/live-link skill, but neither is named by slug. The report DOES name `rough-in-rows-must-be-plain-text-when-anchor-missing`. Surface only.

---

## Repair

### Fixes attempted

- **Finding 1 — cross-reference-integrity (warning): build-ordering dependency on D1 — live link to not-yet-existing `book/src/L3/normalize.md`.**
  - **Decision**: not-needed (coordination/apply-ordering note, not a content defect).
  - **Action**: NO edit. The report's Edit 2 `[normalize](./normalize.md)` live link and the "15 firm" count are correct *as written*, conditioned on D1 (`book/src/L3/normalize.md` + dep-map row) landing first in the same integrator batch. D1 IS a parallel cycle-039 dispatch and will be sequenced FIRST. Keeping the live link is the right call — defanging would be wrong, since D1 is landing. The report already declared the dependency with the correct fallback (defang to plain-text + roll count to "14 firm + 2" if D1 slips). **See the prominent integrator instruction in §Suggested resolution below.**

- **Finding 2 — edge-label-fidelity (low, inherited): stale self-citation `index.md:41` in the preserved c038 narrative bullet.**
  - **Decision**: repaired.
  - **Action**: In CYCLE.md Edit 2 `[new]` only, corrected the preserved c038 narrative's `(book/src/L3/index.md:41)` → `(book/src/L3/index.md:44)`. Verified on disk: the (A) identity-in-form L3 backfill verdict list is at `book/src/L3/index.md:44` (line 41 is the "canonical write-up of when L3 lifts fail" sentence; line 44 is `**(A) Identity-in-form L3 backfill candidates — 6 firm**`). The `:41` reference fell cleanly within this report's Edit 2 surface (it is in the `[new]` body of the bullet being rewritten), so it is in-scope for a surgical one-token fix. The fix is consistent with the report's NEW normalize bullet, which already cites `:44`. **The Edit 2 `[old]` string was NOT touched** — it retains `:41` so it continues to anchor byte-for-byte to the on-disk c038 bullet (on-disk line 57). Net on-disk effect after integration: the integrated c038 bullet's stale `:41` becomes the correct `:44`.

- **Finding 3 — skill-uptake-survey (warning): skill-by-slug telemetry gap.**
  - **Decision**: not-needed (telemetry only, non-blocking). The report exhibits the `proposed-changes-fence-encloses-full-body-guard` and plain-text/live-link reasoning in substance and names `rough-in-rows-must-be-plain-text-when-anchor-missing` by slug. Pure presence check; no edit.

### Post-repair verification

- **Fence parity** (`proposed-changes-fence-encloses-full-body-guard`): clean. 4 fences, even parity, two balanced `edit:book/src/L3/index.md` blocks (CYCLE.md lines 26–29 and 35–40), no nested fences. The repair edited prose *inside* the Edit 2 `[new]` body only — fence structure untouched.
- **Edit-2 context-anchor durability against D1's dep-map row-append**: confirmed. Edit 2's two `[old]` anchors (the c038 bullet head "Three firm L3 identity-in-form backfills landed cycle-038…" and the "Fourth-obstruction-profile taxonomy note pending" bullet) each appear EXACTLY ONCE on disk (verified by grep) and quote full bullet bodies — they re-locate uniquely regardless of the line-number shift D1 introduces by appending a `normalize` ROW to the dep-map table (lines 21–36 region, disjoint from the §Working-Notes c038/pending bullets at lines 57–58). Edit 1's §Semantics-overlay target (~line 15) is likewise disjoint from the dep-map region.

### Unrepairable findings

None. Finding 1 is a not-needed apply-ordering note (routed to the integrator below), Finding 2 was repaired, Finding 3 is not-needed telemetry.

## Suggested resolution

**Status: `ready`.**

**INTEGRATOR APPLY-ORDERING REQUIREMENT (load-bearing): apply D1 (`book/src/L3/normalize.md` + its dep-map ROW) BEFORE this report (D3).** This report's Edit 2 emits the live link `[normalize](./normalize.md)` and asserts the consolidated "15 firm + 2 partial-obstruction" tally — both correct ONLY when `book/src/L3/normalize.md` exists on disk and is wired into `SUMMARY.md`. D1 creates exactly that. If D1 and D3 are both ready this batch (expected), sequence D1 first and apply D3 unchanged.

**Contingency (only if D1 slips this batch):** per the report's own declared fallback, the integrator should defang the `./normalize.md` live link in Edit 2 to plain-text (`normalize *(rough-in; no anchor yet)*`) and roll the count back to "14 firm + 2 (normalize pending cycle-039)". This is the standard `rough-in-rows-must-be-plain-text-when-anchor-missing` defer. Do NOT apply Edit 2's live link / "15 firm" form if `normalize.md` is absent — that is a `linkcheck2` hard-fail.

**OQ closures** (integrator-per-report should mark in `scaffolding/open-questions.md` when applying, jointly with D1): `l3-index-fourth-obstruction-profile-obstruction-carrying-by-reference` RESOLVED (Edit 1 enacts shape (d)); `l3-cohort-growth-audit-c036-verdict` (A)-cohort portion CLOSED at 6-of-6 with `normalize`.

Otherwise no integrator concerns — both edits anchor uniquely and survive D1's row-append line shift.
