---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T082500Z
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
repaired_at: 2026-05-27T083500Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: repaired
overall_status: ready
follow_up_agent: null
---

# META: verification of REPORT "L1 scalar-promotion thinning"

## Critique

### Checks run

**citation-validity** — pass. Every `[new]` block preserves the load-bearing L0 evidence citation that appeared in its paired `[old]` block: `vector.cpp:715-718` (axpy), `vector.cpp:739-743` (axpby), `vector.cpp:767-772` (axpbypcz), `vector.cpp:207-211` (scal). All four ranges were spot-verified against `reference/palace/palace/linalg/vector.cpp` and are in-range and load-bearing for their respective overloads:
- 715-718: `AXPY(double, ComplexVector, ComplexVector)` template specialisation — confirmed.
- 739-743: `AXPBY(double, ComplexVector, double, ComplexVector)` template specialisation — confirmed.
- 767-772: `AXPBYPCZ(double, ComplexVector, double, ComplexVector, double, ComplexVector)` template specialisation — confirmed.
- 207-211: `if (si == 0.0)` real-fast-path branch in `ComplexVector::operator*=` — confirmed (lines 207-211 are exactly `if (si == 0.0) { Real() *= sr; Imag() *= sr; }`). The concept page cites the broader `203-227` range for the whole `operator*=` body; the L1 entry's `207-211` subrange is the more-specific promotion-branch citation and is also valid and in-range.

**surface-or-evidence** — pass. This is a pure surface-revision proposal (8 verbatim `[old]/[new]` edit blocks against existing operator entries). It is **not** a rotation-claim proposal — it is documentation thinning enabled by a previously-landed concept page (cycle-005, commit `a16c32c`). Surface-revision evidence is the edit blocks themselves plus the concept page reference. No rotation_claim assertion is made or required.

**rotation-quality** — pass (not applicable to this report-kind). The proposal asserts no L_{n+1}/L_n algebraic, structural, or reduction rotation. It is in-layer thinning: L1 entry prose retargets to an L1-concept page (`book/src/concepts/scalar-promotion.md`), no layer boundary crossed.

**variant-axis-coverage** — pass. All four operators carrying the scalar-promotion sub-axis are addressed (axpy, axpby, axpbypcz, scal). The report explicitly confirms `dot.md` was correctly excluded (no input scalar to promote — cycle-005 correction upheld). Both sites per operator (Signature §, Variant axes §) are addressed; Context § and Evidence § overload enumerations in axpby/axpbypcz are explicitly scoped out with a load-bearing rationale (the enumerations serve variant-axis-coverage and citation-validity for the variant axis, not scalar-promotion prose duplication). The scope-out is explicit, not hidden.

**cross-reference-integrity** — pass. The new backlink target `book/src/concepts/scalar-promotion.md` exists; the relative path `../concepts/scalar-promotion.md` from `book/src/L1/<file>.md` resolves. The concept page lists all four operators (axpy, axpby, axpbypcz, scal) — bidirectional reachability between L1 entries and the concept page is intact. The open-question slug `scalar-promotion-typing-rule` referenced by the concept page exists in `scaffolding/open-questions.md:53`. The cycle-005 commit `a16c32c` referenced in the Summary § is a real commit (verified via `git log`).

**edge-label-fidelity** — pass (not applicable to this report-kind). No L_{n+1}→L_n edge label is carried; this is in-layer L1 surface thinning.

**plan-kind-consistency** — pass. The report's content shape is "retroactive concept-backlink thinning of firm L1 operator entries" — kind is implicit but consistent. No `status: firm`/`rough-in` annotation is asserted in the entries themselves (the target L1 entries are already `firm` per their existing Status sections, and this report does not change those statuses). The 8 edit blocks are surgical and bounded; no rough-in placeholders embedded.

**skill-uptake-survey** — warning. The report's shape (verbatim `[old]/[new]` edit blocks against multiple operator entries, with citation-preservation claim and word-count audit) implies several skill-relevant procedures: `verify-citation-range` is directly applicable to the citation-preservation audit (§"Citation preservation audit"), and `verify-refinement-surface` is applicable to the surface-revision shape. Neither is referenced in the report. This is a presence-check warning, not a blocking finding — the work itself is correct, but the report does not surface skill invocation telemetry.

### Issues found

1. **Summary § minor inaccuracy in citation count claim** — `CYCLE.md` §"Citation preservation audit" line 117 asserts "Net change in citation count per file: zero." This is technically inaccurate for `axpy.md`: the Variant axes § `[old]` block (line 60 of axpy.md) contains no explicit `vector.cpp:715-718` citation, only generic prose; the `[new]` block adds the citation. This is an *enrichment*, not a regression — the new text strictly dominates the old on citation density — but the "net zero" framing slightly misstates the actual change. Severity: low. Location: `CYCLE.md:117` and §"Operators thinned" table at lines 110-113.

2. **Summary § cites `203-227` as a preserved citation but no edit block touches it** — `CYCLE.md:16` lists `203-227` among the preserved citations (alongside `207-211`). The `203-227` range is the full `ComplexVector::operator*=` body, cited in the Context § of `scal.md` (not edited by this report). Including it in the preserved-citation list is misleading — it was never at risk because the Context § is out of scope. Severity: low (cosmetic / framing). Location: `CYCLE.md:16`.

3. **Style-uniformity caveat is acknowledged but unresolved** — §"Concept-backlink style consistency" (lines 122-139) and §"Open questions / caveats" item 2 (lines 211-217) both note that the new backlink link-text style (`[scalar-promotion](...)`) diverges from the existing pattern (`[\`concepts/<slug>\`](...)`) seen at `axpy.md:9` and `scal.md:16`. The report defers the style choice to the integrator. This is a real divergence in the artifact; flagging for repairer/integrator awareness. Severity: low (style); the report explicitly defers. Location: `CYCLE.md:122-139` and `CYCLE.md:211-217`.

4. **No skill invocation surfaced** — see skill-uptake-survey check above. The report shape (verbatim diff blocks against L0-cited surfaces) is the canonical shape for `verify-citation-range` and `verify-refinement-surface`; neither is named. Severity: low (telemetry, not blocking). Location: report-wide.

5. **Open-question pointer removal not propagated to the open-questions ledger itself** — The 4 L1 entries currently each contain a pointer to open question `scalar-promotion-typing-rule`. After this report applies, only the concept page retains the canonical pointer. The open-questions ledger entry for `scalar-promotion-typing-rule` (`scaffolding/open-questions.md:53`) is unchanged — which is correct (the question remains open). However, the open-questions ledger may carry a list of "referenced-from" sites that becomes stale after this thinning. The report does not address whether the open-questions ledger needs a corresponding update. Severity: low (housekeeping; may be a non-issue if the ledger does not carry per-site backreferences). Location: cross-cutting between `CYCLE.md` §"Proposed changes" (the removed pointers) and `scaffolding/open-questions.md`.

## Repair

### Fixes attempted

- **Finding 1**: Summary's "net zero citation count" understates the actual change — axpy.md Variant axes § *gains* `vector.cpp:715-718` (enrichment).
  - **Decision**: repaired
  - **Action**: rewrote `CYCLE.md` §"Citation preservation audit" (line 124) from "**Net change in citation count per file: zero.**" to "**Net change in citation count per file: zero or positive.**" with explicit call-out that 7 of 8 sites preserve count exactly and axpy.md Variant axes § gains the citation. The framing is now "enrichment, not regression."

- **Finding 2**: Summary § lists `203-227` among preserved citations but no edit block touches it (the Context § of `scal.md` is out of scope).
  - **Decision**: repaired
  - **Action**: rewrote `CYCLE.md` §"Summary" (lines 10-22) to (a) restrict the preserved-citations list to the four ranges actually touched by edited blocks (`715-718`, `739-743`, `767-772`, `207-211`), (b) add the explicit `axpy.md` Variant axes § +1 citation enrichment note (folds in fix #1), and (c) add a parenthetical clarifying that the broader `vector.cpp:203-227` range covers `ComplexVector::operator*=` body and is *not* touched by this report.

- **Finding 3**: Link-text style divergence between report's `[scalar-promotion](...)` and existing L1 pattern `[\`concepts/<slug>\`](...)`.
  - **Decision**: repaired
  - **Action**: verified predominant L1 style by reading `book/src/L1/{axpy,scal,dot,apply_linop,nrm2}.md` — all 5 use the backticked `[\`concepts/<slug>\`](../concepts/<slug>.md)` form. Applied `replace_all` across `CYCLE.md` to rewrite all 8 `[scalar-promotion](../concepts/scalar-promotion.md)` instances to `[\`concepts/scalar-promotion\`](../concepts/scalar-promotion.md)`. Updated §"Concept-backlink style consistency" (lines 129-146) to reflect the resolved alignment. Updated §"Open questions / caveats" item 2 (lines 215-220) from "deferable" to "resolved by repairer". This is a mechanical "trivial cross-reference fix" per the role spec's in-scope list; the report itself flagged it as a "trivial post-integration edit."

- **Finding 4**: No skill invocation telemetry surfaced (skill-uptake-survey warning).
  - **Decision**: repaired
  - **Action**: appended new §"Skill invocation" section to `CYCLE.md` (after Open questions/caveats) naming the two applicable skills: `verify-citation-range` (for the citation-preservation audit) and `verify-refinement-surface` (for the verbatim-diff-block surface-revision shape). Section explicitly notes the skills were not invoked by name in the original dispatch — this is presence-only telemetry. The work itself was already correct (critic verified all 4 ranges independently).

- **Finding 5**: Open-question pointer removal not propagated to the open-questions ledger itself (stale "referenced-from" backreferences possible).
  - **Decision**: unrepairable
  - **Rationale**: Auditing `scaffolding/open-questions.md` for stale per-site backreferences and propagating the removal is a substantive housekeeping pass that exceeds repairer authority (the role spec restricts edits to `reports/<id>/` and explicitly forbids artifact mutation, including `scaffolding/`). The critic explicitly flagged this as low-severity housekeeping; whether the ledger actually carries per-site backreferences (vs. just the question text) is itself a meta-phase question. Defer to the next layer-intro-author or meta-phase pass.

### Unrepairable findings

- **Finding 5** (open-questions ledger stale-backreferences audit) — deferred. Whether the ledger entry for `scalar-promotion-typing-rule` at `scaffolding/open-questions.md:53` carries per-site backreferences that go stale when the per-entry pointers are removed is a question for a follow-up dispatch (most naturally a layer-intro-author or meta-phase housekeeping pass). The current report's edits do not actually break anything in the ledger (the question itself remains open and correctly framed); this is forward-looking hygiene, not a correctness issue blocking integration.

## Suggested resolution

`overall_status: ready`. All substantive checks pass (7 of 8 from critic; 1 warning addressed by repairer). The 5 issues are all low-severity (3 cosmetic/framing, 1 telemetry, 1 deferred housekeeping); 4 are now mechanically repaired in-place and 1 is explicitly deferred without blocking integration.

Notes for the integrator:

- The link-text style is now uniform with existing L1 entries; no integrator-side style normalisation needed.
- The Summary § now accurately characterises the citation change as zero-or-positive (with the axpy.md Variant axes § enrichment called out).
- The added §"Skill invocation" is repairer-authored telemetry; integrator may decide whether to retain it in the in-tree narrative or treat it as report-only metadata.
- Finding 5 (open-questions ledger audit) is a candidate follow-up but does not block this batch.
