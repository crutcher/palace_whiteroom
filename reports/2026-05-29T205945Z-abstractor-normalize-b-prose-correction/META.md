---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T23:57:19Z
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
repaired_at: 2026-05-29T24:00:00Z
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

# META: verification of "L1>L0 + L1 prose correction — normalize_B 'no fused B-Normalize' defect"

## Critique

### Checks run

**citation-validity (pass).** The load-bearing positive anchor is `palace/linalg/operator.hpp:377-384` (definition of the fused 4-arg `Normalize(comm, x, B, Bx)` template). I verified the source via `mcp__palace-codemap__read_range` over `palace/linalg/operator.hpp:370-390` — line 378 is exactly `inline double Normalize(MPI_Comm comm, VecType &x, const Operator &B, VecType &Bx)`, line 380 binds `double norm = Norml2(comm, x, B, Bx)`, line 381 is `MFEM_ASSERT(norm > 0.0, ...)`, line 382 is `x *= 1.0 / norm`, line 383 is `return norm`. The four pinpoint anchors the report's body asserts (378 def, 380 reduction, 382 rescale, 383 return) all land inside the cited :377-384 range. I re-ran the three `citecheck --anchor` probes mechanically — all three return `ok` with anchors at lines 378, 380, 382 within `palace/linalg/operator.hpp:377-384`, confirming the report's pinpoint discipline. The negative anchor (zero 4-arg callsites) was verified two ways: `mcp__palace-codemap__get_call_sites name=Normalize` returns exactly 3 hits (`operator.cpp:661`, `operator.cpp:673`, `waveportoperator.cpp:693`), and `search_text` for `Normalize\s*\(` in `*.cpp` returns those same 3 plus the unrelated `void Normalize(...)` declaration at `waveportoperator.cpp:120`. I spot-read `operator.cpp:658-680` (both calls are 2-arg `Normalize(comm, u)` in a power-iteration body) and `waveportoperator.cpp:688-700` (a 5-arg `GridFunction`-tuple `Normalize`, plainly unrelated). The three B-weighted reduction callsites the report cites alongside (`arpack.cpp:438`, `slepc.cpp:475`, `nleps.cpp:114`) all check out as 4-arg `linalg::Norml2(comm, x, *opB, Bx)` calls (B-weighted reduction, not rescale). The full `citecheck --scan` over the report returns 21 ok + 3 `AMBIG` — the 3 `AMBIG` are basename-only shorthand (`operator.hpp:378`, `operator.hpp:377-384`, `operator.cpp:661`) in the report's own evidence-narration prose at lines 53-68; all references in the proposed-changes `edit:` blocks (which become artifact content) consistently use the full `palace/linalg/...` path. The basename-only shorthand is a report-prose hygiene issue (the report does the right thing in the edits), worth a minor note but does not affect what lands in the artifact.

**surface-or-evidence (pass).** The proposal is refinement-shaped (changes to existing operator/theme text in two firm chapters). Both arms of the rule are satisfied: (a) the proposal modifies surface — 3 edits to `book/src/L1-L0/normalize-mutation-rotation.md` (rough-in-note rewrite, chapter-intro parenthetical, promotion-gate tightening) + 4 edits to `book/src/L1/normalize.md` (chapter-intro one-liner, rough-in-note item 1, promotion-gate sentence, closing sentence) — AND (b) the proposal carries rotation-claim-equivalent evidence: on-disk read of `operator.hpp:370-389`, 3 `citecheck --anchor` probes, exhaustive grep for the negative anchor. The report is *also* legitimately a "retroactive evidence backfill" case — the cycle-028 lowering-verifier audit F1 finding is the documented predicate the report responds to, with the verifier's `verified_against:` row `does-not-support` cited as the source of the routed correction. Either framing is sufficient; this report carries both.

**rotation-quality (pass — not applicable to a prose-correction).** The report is a prose-only correction; no algebraic/structural/reduction rotation is asserted, no L_{n+1} representation is claimed to compress an L_n form. The check is vacuous for this report shape (the report explicitly preserves the existing firm rotations — it neither tightens nor loosens any structural claim, only the surrounding factual prose about the L0 surface). Mark pass.

**variant-axis-coverage (pass).** The `normalize` operator's element-type axis (real / complex) is established firm in the existing `book/src/L1/normalize.md` Variant-axes section and the existing `book/src/L1-L0/normalize-mutation-rotation.md` Variant-axes section. The prose correction does not touch the variant-axes discussion of either file. The rough-in `normalize_B` note inherits its (B SPD-vs-not) implicit axis from the unchanged context. No hidden branch introduced; no existing branch erased. The B-vs-not axis itself is the *subject* of the corrected note (the note records the situation of `normalize_B` cleanly: B-weighted def exists, no callsite). No fail.

**cross-reference-integrity (pass).** I verified every cross-reference touched by the edits resolves on disk. The edits reference: `../L1/matrix-weighted-norm.md`, `./matrix-weighted-norm-mutation-rotation.md`, `./matrix-weighted-norm.md`, `./scal.md`, `./nrm2.md` (these last two in unchanged surrounding context) — all are existing firm or rough-in chapters in the book tree. The previously-internally-inconsistent state (theme cites :377-384 as a consumer at line 290-293 while denying the function exists at line 285-287 + line 51) is the exact contradiction the edits restore consistency for: after the edits, line 51 acknowledges the fused overload's existence with a forward-reference to the rough-in note, the rough-in note (formerly lines 283-293) acknowledges the def site is the *definition* of the fused 4-arg form, and the cross-theme citation at line 290-293 still resolves to the same range but no longer contradicts the surrounding claim. Internal consistency is restored. **Build-readiness fence guard**: I enumerated fences via `grep -n '^```'` — 14 fences total, even parity (7 well-formed `edit:` blocks at 82-116, 118-126, 128-145, 152-158, 160-166, 168-174, 176-182), no nested triple-fence inside any edit block (the report uses 4-space-indented inner code per its own transport-convention note at lines 42-45, consistent with the cycle-024 `convert-nested-fences-to-indented-code-in-proposed-changes-block` skill). This report is NOT claiming a firm-status promotion (no status changes asserted), so the firm-body-inside-fence guard is a no-op for the body content; the fence-parity check is what matters, and it passes.

**edge-label-fidelity (pass).** The report's scope/title carries `L1>L0` and `L1` as the two edited surfaces. The 3 edits to `book/src/L1-L0/normalize-mutation-rotation.md` are L1>L0 surface; the 4 edits to `book/src/L1/normalize.md` are L1 surface. The prose in each edit addresses material at the edge it labels (the L1>L0 edits discuss the rotation's RHS / L0 form / rough-in speculative note; the L1 edits discuss the firm operator chapter's intro / rough-in sibling note). No edge-label-vs-prose mismatch.

**plan-kind-consistency (pass).** The report self-declares as "prose-only correction" (line 30) and explicitly states no status changes — line 184-194 states `## Status changes — None`, both files' `## Status` stays `firm`, `normalize_B` stays rough-in. The Speculative-operators-proposed section (line 196-201) explicitly states `None`. The dispatch brief framed this as a prose-only F1 correction with no status change; the content matches that framing. The promotion-gate edit (Edit 1's third sub-edit at lines 128-145 and Edit 2's third sub-edit at lines 168-174) keeps the gate OPEN — explicitly stating "the mere *existence* of the fused free function ... does NOT promote it" and "Until a callsite surfaces, `normalize_B` is tracked as a queued candidate ... NOT a firm operator." The gate-tightening is in the *strict-improvement* direction: the new wording accepts an additional explicit qualifying form (a 4-arg callsite) AND retains the original (inline rescale shape), which the report's Open-questions note at lines 258-263 correctly characterises as "slightly looser AND slightly more correct" — the evidence-set widens (more shapes qualify) but the **bar to promotion is stricter** (definition existence alone is no longer enough — a positive *callsite* is required). That matches the dispatch brief's expectation. Plan-kind matches content.

**skill-uptake-survey (pass).** The report invokes (a) `citecheck` with `--anchor` for deterministic anchor verification (3 probes recorded at lines 60-63 + lines 211-214), realising the cycle-024 mechanical citation-bounds-and-anchor surface; (b) the transport convention from `convert-nested-fences-to-indented-code-in-proposed-changes-block` is named at lines 42-45 (4-space-indented inner code, no nested triple fences). The friction-ledger reference `firm-chapter-body-authored-outside-proposed-changes-fence` is also cited at line 45 as the defect being avoided. The skill that would be most relevant for "abstractor making a prose-only F1 correction to a firm chapter" doesn't have a dedicated SKILL.md (this is a relatively uncommon dispatch shape — typically an integrator-time fix or a separate report — and the abstractor handles it cleanly here without one). No new skill candidate is proposed; that is consistent with the report's incremental scope.

### Issues found

- **Minor — basename-only references in the report's evidence-narration prose (NOT in the edit blocks).** The report's §"On-disk verification" (lines 53-68) and §"Supporting evidence" (lines 212-218) use basename-only shorthand like `operator.hpp:378`, `operator.hpp:377-384`, `operator.cpp:661`. These trigger 3 `AMBIG` hits in `citecheck --scan` because the Palace tree has two `operator.hpp` files (`palace/linalg/operator.hpp` and `palace/fem/libceed/operator.hpp`). All `palace/linalg/operator.hpp` references in the actual `edit:` blocks (which become artifact content) use the full path — so the artifact remains hygienic. The issue is report-prose-hygiene only. Severity: low / cosmetic. Location: `CYCLE.md:53-68` and `CYCLE.md:212-218`.

- **Minor — `operator.cpp` line-range inconsistency.** The report uses `:599-619` in Edit 1's new prose (line 109) and `:600-619` in the existing-and-preserved Edit 2 line (line 165). Both ranges are within the actual two `Norml2` overloads (line 599 = first `template <>`, line 600 = body start through line 619 = end of second overload). The inconsistency is pre-existing in the surrounding artifact (the L1>L0 theme uses `:599-619`, the L1 entry uses `:600-619`), and the edits preserve each file's local convention rather than unifying them. Not introduced by this dispatch; flagging for the repairer's consideration if it would prefer to normalise. Severity: low / cosmetic. Location: `CYCLE.md:109` vs `CYCLE.md:165`.

- **Observation — verifier's `verified_against:` row at `:466-469` carries verdict `does-not-support` for `palace/linalg/operator.hpp:377-384` and will become stale after this prose correction lands.** The report explicitly notes this in Open-questions (lines 236-244) and correctly defers a row-update to a future lowering-verifier re-audit (the row is a historical audit-as-of-timestamp record, not a live claim). This is per-spec — abstractor authority does not extend to amending lowering-verifier ledger rows. Flagging only so the meta-phase / next-cycle planner sees the audit-row staleness as a known followup, not for repair here. Severity: not-an-issue / process-note. Location: `book/src/L1-L0/normalize-mutation-rotation.md:466-469` (post-integration state).

## Repair

### Fixes attempted

All 8 critic checks returned `pass`. The Issues-found block lists three explicitly-non-blocking observations; each is evaluated below.

- **Finding**: `citation-validity` — basename-only references in report's evidence-narration prose (CYCLE.md:53-68, 212-218) trigger 3 `AMBIG` hits in `citecheck --scan`.
  - **Decision**: not-needed.
  - **Rationale**: Critic check is `pass`. The AMBIG hits are confined to **report-prose** (evidence narration), not the `edit:` blocks. All citations that become artifact content use full `palace/linalg/...` paths, so nothing ambiguous reaches `book/`. Reports are not artifact and post-integration become append-only historical record. Rewriting the report prose would be cosmetic-only with no downstream consequence.

- **Finding**: `cross-reference-integrity` — `operator.cpp` line-range inconsistency: report uses `:599-619` (Edit 1 prose, CYCLE.md:109) vs `:600-619` (Edit 2 line, CYCLE.md:165).
  - **Decision**: not-needed.
  - **Rationale**: Critic check is `pass`. The inconsistency is **pre-existing in the artifact** (L1>L0 theme uses `:599-619`, L1 entry uses `:600-619`) and the report explicitly preserves each file's local convention rather than unifying — that is an intentional non-introduction. Both ranges are mechanically valid (within the actual two `Norml2` overloads). Normalising would be substantive cross-file convention-unification, which exceeds mechanical repair authority and is properly handled by a same-layer-cross-cutter dispatch.

- **Finding**: `cross-reference-integrity` (observation) — verifier's `verified_against:` row at `normalize-mutation-rotation.md:466-469` carries `does-not-support` verdict for `palace/linalg/operator.hpp:377-384` and becomes stale after this prose correction lands.
  - **Decision**: not-needed.
  - **Rationale**: Critic explicitly flags this as "not-an-issue / process-note" and "not for repair here". Repairer cannot author lowering-verifier ledger row updates (substantive authoring, out of mechanical scope; also, row updates are historical audit-as-of-timestamp records owned by lowering-verifier dispatches). The report itself correctly defers via its Open-questions section. Recorded as integrator note below.

### Unrepairable findings

None. No critic check returned `warning` or `fail`; the three observations are all non-blocking process-notes that the critic itself excluded from repair scope.

## Suggested resolution

`ready` — apply this report.

**Integrator note** (record, do not enact): after this prose correction lands, the lowering-verifier's `verified_against:` row at `book/src/L1-L0/normalize-mutation-rotation.md:466-469` (verdict `does-not-support` against `palace/linalg/operator.hpp:377-384`) will be stale. The row is a historical audit-as-of-timestamp record, not a live claim, so it is safe to land this report without amending the row. A future lowering-verifier dispatch on `normalize-mutation-rotation` should refresh the row in light of the corrected understanding (the fused 4-arg `Normalize` DOES exist at the cited range, but with zero callsites — the F1 finding the report routes into chapter prose). This is a future-cycle follow-up, not a repair gate.
