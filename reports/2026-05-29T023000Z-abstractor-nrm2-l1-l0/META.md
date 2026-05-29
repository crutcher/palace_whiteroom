---
verifies: ../REPORT.md
critiqued_at: 2026-05-29T02:47:31Z
critic_version: 1
checks:
  citation-validity: fail
  surface-or-evidence: warning
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: fail
  edge-label-fidelity: pass
  plan-kind-consistency: warning
  skill-uptake-survey: warning
repaired_at: 2026-05-29T03:05:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: repaired
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: repaired
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "L1>L0 theme firm-up — nrm2-mutation-rotation (stub→firm)"

## Critique

### Checks run

**citation-validity — FAIL.** I independently re-read every cited range via `palace-codemap read_range`/`search_text` (audit sub-case — producer self-verification not trusted). The structural chain is real, but the report's single headline claim is wrong. The report asserts, repeatedly and as a *correction*, that the load-bearing body line is `palace/linalg/vector.hpp:258` and that this corrects the L1 entry's `255-260` range (CYCLE.md lines 28, 88-89 inline comment, 115-116, 247-248, 271, 300). The actual line is **`vector.hpp:259`**: `search_text` for `std::sqrt\(std::abs\(Dot` returns exactly one hit at line 259; the template signature `inline auto Norml2(MPI_Comm comm, const VecType &x)` is at line 257; the body `return std::sqrt(std::abs(Dot(comm, x, x)));` is at 259. So the report is off-by-one, and the line it "corrects to" (258) is a blank/brace line, not the load-bearing line. Worse, `259` is *inside* the L1 entry's `255-260` range, so the framing that `258` "corrects" `255-260` is doubly wrong — there was nothing to correct (the L1 entry `nrm2.md:53` already cites `259` correctly). All other ranges verify: `communication.hpp:246` (`GlobalOp` sig) / `:248` (`MPI_Allreduce(MPI_IN_PLACE, buff, len, mpi::DataType<T>(), op, comm)`) — confirmed; `communication.hpp:267-270` (`GlobalSum`→`GlobalOp(.., MPI_SUM, ..)`) — confirmed; `errorindicator.hpp:43` (`auto Norml2(MPI_Comm comm) const { return linalg::Norml2(comm, local); }`) — confirmed verbatim; `iterative.cpp:408` (`beta_rhs = linalg::Norml2(comm, b);`) and `:631` (`Hj[j + 1] = linalg::Norml2(comm, w);`) — confirmed; `test-vector.cpp:209-211` (`norm1 = vec1.Norml2(); ... WithinRel(std::sqrt(14.0))`) — confirmed; `operator.hpp:374` (B-weighted overload decl) — confirmed (report's `372-374` brackets it, fine). The `Dot` leaf cited as `vector.hpp:247-252`: the `inline auto Dot` sig is at 248 and the body runs 250-252 — the `247-252` range is acceptable (247 is the leading comment), minor. The single failing citation is the load-bearing one, so this check fails.

**surface-or-evidence — WARNING.** This is a refinement-shaped proposal (stub→firm on an existing theme); it modifies surface (authors the full theme body) and rests on structural/algebraic evidence — the surface-or-evidence shape is satisfied in principle. The warning is on the `std::abs`-guard classification, which the prompt asked me to ground adversarially. The *verdict* (load-bearing numerical / defensive guard, no-op in exact arithmetic) is sound and matches the existing L0 corpus. But the report's **complex-path mechanism sub-claim is not grounded in the code path the chain actually executes** (CYCLE.md lines 173-178): it claims `std::abs(complex)` "folds the residual imaginary part" of a self-dot whose imaginary part is "floating-point ~ε". The cited self-dot path zeroes the imaginary part *exactly*: `ComplexVector::Dot` at `vector.cpp:264-267` returns `{re, (this == &y) ? 0.0 : ...}`, and the L0 tricks page (`transparent-vs-load-bearing-tricks.md:13`) already records this self-aliasing fast path. For `Dot(comm, x, x)` the imaginary part is exactly `0.0`, so `std::abs(std::complex{re, 0.0})` degenerates to `|re|` — the same sign-strip as the real path, NOT a residual-imaginary-folding modulus. The report over-describes a role that the cited code path eliminates. The classification verdict survives; the complex-path narrative does not.

**rotation-quality — PASS.** Lowering direction is correctly high→low: the theme narrates the L1→L0 forward rewrite ("how `nrm2(x)` expands into the L0 chain"), LHS is L1, RHS is L0, consistent with the "Layers are defined high→low" invariant. The four-stage chain (`Dot` → `MPI_Allreduce` → `std::abs` → `std::sqrt`) faithfully reflects source: `Norml2` body is `sqrt(abs(Dot(...)))` (vector.hpp:259), `Dot` is `LocalDot` + `Mpi::GlobalSum` (vector.hpp:248-253), `GlobalSum`→`GlobalOp`→`MPI_Allreduce` (communication.hpp:267-270, 246-249) — all confirmed. The rotation is a genuine expansion (one pure L1 step → four L0 stages), not a rename, and it correctly hides the MPI collective at L1.

**variant-axis-coverage — PASS.** The element-type axis (real / complex) is handled correctly and consistently with the firm L1 entry: it collapses to one L1 operator (`nrm2 :: Tensor[N] -> Scalar(real)`) and appears at L0 as two template specialisations differing only at the `Dot` leaf and the meaning of `std::abs`. The collapse is explicitly stated (CYCLE.md lines 38-40, 71-75, 211-213) and matches `L1/nrm2.md:74-79`. The B-weighting axis is correctly scoped *out* as a different operator with a different L1 referent, not a hidden branch. No undocumented variant branches.

**cross-reference-integrity — FAIL.** Two distinct problems. (1) **Both "carry-forward corrections" the report records are stale — they target a corpus state that no longer exists.** The report claims (CYCLE.md lines 192-197, 327-333) that `concepts/nrm2.md` "claims Palace uses BLAS-style scaled summation"; the page has *already been corrected* — `concepts/nrm2.md:9` now reads "it does **not** use scaled summation... BLAS-style scaled-summation `nrm2`... is **not present** in Palace." Likewise the report claims (CYCLE.md lines 187-189, 318-321) the L0 page "does **not yet** carry a 'defensive guards' treatment"; `transparent-vs-load-bearing-tricks.md:22` *already has* a "Defensive non-negativity guard" worked example for `linalg::Norml2` under load-bearing tricks, with the property-it-buys stated and `L1/nrm2` listed in its "Referenced from" (line 37). Recording these as future-correction working-notes is the discipline-correct *channel*, but the asserted defects are false, so the OQ carry-forwards would mislead a downstream planner into redundant work. (2) The forward-ref targets themselves all resolve (`L1/matrix-weighted-norm.md`, `L1-L0/dot-mutation-rotation.md`, `L1/dot.md`, `concepts/nrm2.md`, `L0/transparent-vs-load-bearing-tricks.md` all exist as live-link homes — verified on disk), so the live-link usage is sound; the failure is the two false cross-referenced claims, not dangling links.

**edge-label-fidelity — PASS.** The dep-map / index.md row (CYCLE.md lines 280-284) carries the L1>L0 edge for `nrm2-mutation-rotation` with L1 anchor `L1/nrm2 (firm)` and L0 anchors `vector.hpp`, `communication.hpp`, `errorindicator.hpp`; the prose discusses exactly that L1→L0 edge throughout. No edge-label/prose mismatch.

**plan-kind-consistency — WARNING.** The declared kind is `firm` (theme stub→firm promotion) and the body shape mostly matches a firm theme: structural decomposition, exhaustive citations, three surface forms, variant collapse, explicit `Status: firm` rationale, correctly noting it is `firm` not `partly-constructive` (no negative-anchor reconstruction). Two consistency snags. (a) The SUMMARY.md edit (CYCLE.md lines 286-288) adds `- [nrm2-mutation-rotation](./L1-L0/nrm2-mutation-rotation.md)` as if a *new* row, but the entry **already exists** in SUMMARY.md at line 83 as `- [nrm2-mutation-rotation (stub)](./L1-L0/nrm2-mutation-rotation.md)`. As written this either duplicates the SUMMARY link (a hard mdBook build error) or silently requires the integrator to reconcile (drop the `(stub)` marker on the existing row); the report does not acknowledge the existing row or frame the edit as an in-place marker removal. (b) The index.md row edit (CYCLE.md line 282) is a *replacement* of the existing stub-status row, but the proposed-changes block is shaped like an append; the integrator must treat it as a row replacement. Both are mechanical but unflagged, so the proposed-changes blocks are not unambiguously well-formed.

**skill-uptake-survey — WARNING.** The proposal's shape strongly implies relevant skills exist and should have been invoked: `verify-citation-range` (the report makes an explicit citation-correction claim — the very claim that turned out wrong; the skill's audit sub-case would have caught the 258-vs-259 off-by-one), `verify-rotation-citation` (L1→L0 rotation with cited anchors), and `find-tests-for-region` (the test-vector.cpp:209-211 semantic anchor). The report's "Verified-against" / "Supporting evidence" sections claim self-verification "via `palace-codemap` read_range / search_text" but reference no skill invocation. Pure presence check (non-blocking), but the absence is notable precisely because the un-skilled self-verification missed the load-bearing line number.

### Issues found

1. **[HIGH] Load-bearing-line citation is wrong; the headline "correction" is itself an error.** CYCLE.md lines 28, 88 (inline `// vector.hpp:258`), 115-116, 247-248, 271, 300 all cite the body line as `vector.hpp:258`. Verified actual: `vector.hpp:259` (`return std::sqrt(std::abs(Dot(comm, x, x)));`; template sig at 257). The report frames `258` as correcting the L1 entry's `255-260`; in fact `259 ∈ [255,260]` and the L1 entry (`L1/nrm2.md:53`) already cites `259` correctly — there was nothing to correct. Every `258` occurrence should be `259`. Severity high: it is the single load-bearing line of a `firm`-status theme and is asserted as a correction.

2. **[MEDIUM] Stale carry-forward: `concepts/nrm2.md` BLAS-scaled-summation "false claim" no longer exists.** CYCLE.md lines 192-197 and 327-333 assert the concept page claims BLAS scaled summation. `concepts/nrm2.md:9` already states the opposite ("does **not** use scaled summation... **not present** in Palace"). The OQ carry-forward targets a corrected state; it would send a downstream planner on redundant work.

3. **[MEDIUM] Stale carry-forward: L0 tricks page already has the "defensive guards" treatment.** CYCLE.md lines 187-189 and 318-321 assert `L0/transparent-vs-load-bearing-tricks.md` lacks a defensive-guards subsection. The page already classifies the `std::abs` guard under "Load-bearing numerical tricks" at line 22 (a worked "Defensive non-negativity guard" example for `linalg::Norml2`), with `L1/nrm2` in its "Referenced from" (line 37). The flagged follow-up is unnecessary as stated.

4. **[MEDIUM] SUMMARY.md edit collides with an existing row.** CYCLE.md lines 286-288 add a new `nrm2-mutation-rotation` SUMMARY row, but SUMMARY.md:83 already has `- [nrm2-mutation-rotation (stub)](./L1-L0/nrm2-mutation-rotation.md)`. As written this risks a duplicate-link build error; the intended action is to drop the `(stub)` marker on the existing row. Report does not acknowledge the existing entry.

5. **[LOW-MEDIUM] abs-guard complex-path mechanism over-claims.** CYCLE.md lines 173-178 describe `std::abs(complex)` as folding a residual imaginary part (~ε) of the self-dot. The cited self-dot path zeroes the imaginary part exactly: `ComplexVector::Dot` (`vector.cpp:264-267`) returns `{re, (this==&y)?0.0:...}`; the L0 page (`transparent-vs-load-bearing-tricks.md:13`) records this fast path. For `Dot(comm, x, x)` the imaginary part is exactly `0.0`, so `std::abs` degenerates to `|re|` — the same sign-strip as the real path. The load-bearing verdict stands; the residual-imaginary-folding mechanism does not apply to the path the chain executes.

6. **[LOW] index.md row is a replacement, not an append.** CYCLE.md line 282 replaces the existing stub-status `nrm2-mutation-rotation` row in `L1-L0/index.md:27`-adjacent table (the index currently has no nrm2 row visible in the read range — verify integrator inserts/replaces consistently). Mechanical; flagged for integrator clarity.

7. **[LOW] `Dot` leaf range slightly loose.** CYCLE.md lines 96-97, 117-118, 249 cite `vector.hpp:247-252` for the `Dot` template; the `inline auto Dot` sig is at 248 and body 250-252 (247 is the leading comment). In-range and acceptable, noted for completeness.

8. **[INFO] Skill invocation not referenced.** No `verify-citation-range` / `verify-rotation-citation` / `find-tests-for-region` invocation cited despite the report's shape implying them; the missed load-bearing line number is exactly what the citation-range audit sub-case exists to catch. Telemetry only, non-blocking.

## Repair

### Fixes attempted

- **Finding**: [citation-validity FAIL] The load-bearing body line is cited as `vector.hpp:258` and framed as a correction to the L1 entry's `255-260`; actual line is `259`, which is already inside `[255,260]` (nothing to correct).
  - **Decision**: repaired
  - **Action**: Independently verified via `palace-codemap read_range palace/linalg/vector.hpp:246-270` + `search_text std::sqrt\(std::abs\(Dot` → single hit at line **259**; 258 is the opening brace `{`, sig at 257. Changed all 5 `258` occurrences → `259` in CYCLE.md (lines 88 inline comment, 115 Citations note, 247 Verified-against, 271 Status rationale, 300 Supporting-evidence). Replaced the stale "corrects to 258" framing: Status rationale (CYCLE.md:271-272) now states 259 is "inside the L1 entry's already-correct `255-260` range"; Supporting-evidence (CYCLE.md:300-303) now states the L1 citation was never wrong and this report "merely pins the exact body line."

- **Finding**: [cross-reference-integrity FAIL] Two stale carry-forward working-notes: (1) `concepts/nrm2.md` claims BLAS scaled-summation; (2) `L0/transparent-vs-load-bearing-tricks.md` lacks a defensive-guards treatment.
  - **Decision**: repaired
  - **Action**: Verified both via Read. `concepts/nrm2.md:9` ALREADY states `linalg::Norml2` computes naive `√⟨x,x⟩` and does **not** use scaled summation ("not present in Palace"). `L0/transparent-vs-load-bearing-tricks.md:22` ALREADY carries the "Defensive non-negativity guard" worked example for `linalg::Norml2`, with `L1/nrm2` in "Referenced from" (line 37). Removed/corrected the stale notes: (a) in the artifact-bound `nrm2-mutation-rotation.md` edit block, rewrote the §verdict "forthcoming treatment" line and the stale concept-page note (CYCLE.md:186-196) to reflect the already-landed L0 treatment and already-corrected concept page; (b) in Open questions, rewrote the abs-guard OQ note (CYCLE.md:316-322) to point at the existing `tricks.md:22` example ("no new subsection needed") and replaced the stale concept-page carry-forward (CYCLE.md:329-334) with an "already reconciled — carry-forward dropped" note so no downstream planner is sent on redundant work.

- **Finding**: [surface-or-evidence WARNING] Complex-path mechanism over-claims: describes `std::abs(complex)` folding a residual imaginary ~ε, but the cited self-dot path zeroes the imaginary part exactly.
  - **Decision**: repaired
  - **Action**: Verified `ComplexVector::Dot` via `read_range palace/linalg/vector.cpp:258-272` — self-dot returns `{re, (this == &y) ? 0.0 : ...}`, i.e. imaginary part **exactly `0.0`** for `Dot(x,x)`. This is a small surgical wording fix (the load-bearing verdict and the surface/evidence shape are intact; only the mechanism sentence was wrong, and the correct mechanism — the self-aliasing fast path — is already documented at `tricks.md:13`). Rewrote both occurrences: the Summary one-liner (CYCLE.md:34-35) and the complex-path bullet in the artifact-bound classification block (CYCLE.md:173-178) now state the guard performs the *same* sign-strip as the real path (`std::abs(std::complex{re,0.0}) = |re|`), citing the `this==&y` fast path at `vector.cpp:264-267`. No substantive re-argument required.

- **Finding**: [plan-kind-consistency WARNING] The SUMMARY.md edit is shaped as a new-row append, but `SUMMARY.md:83` already has a `nrm2-mutation-rotation (stub)` row — a naive append would duplicate the link (build error).
  - **Decision**: repaired
  - **Action**: Verified `SUMMARY.md:83` current text = `- [nrm2-mutation-rotation (stub)](./L1-L0/nrm2-mutation-rotation.md)`. Rewrote the proposed-change block (CYCLE.md:292-303) as an explicit in-place de-stub: a `replace … with …` instruction that drops `(stub)` from the existing row and explicitly warns the integrator NOT to append a second link.

### Not-needed / verified-clean

- **[LOW, finding 6] index.md row replacement-vs-append.** The critic flagged this as "verify integrator inserts/replaces consistently." Verified `book/src/L1-L0/index.md` has **no** existing `nrm2-mutation-rotation` row (`grep` returns nothing), so the report's index.md edit is a clean new-row addition into the table, not a replacement — no collision, no repair needed. (Contrast SUMMARY.md, which DID have an existing stub row.)
- **[LOW, finding 7] `Dot` leaf range `247-252` slightly loose.** Critic itself ruled this in-range and acceptable; not a defect. Left as-is.
- **rotation-quality / variant-axis-coverage / edge-label-fidelity** — critic `pass`; not touched.
- **skill-uptake-survey** — `warning` is telemetry-only (non-blocking, no artifact defect); nothing to repair mechanically.

### Unrepairable findings

None. All four flagged findings (two FAIL, two WARNING) were mechanical/surgical and are `repaired`. The surface-or-evidence over-claim was a wording fix grounded in an already-documented code path (not substantive re-argument), so it did not need to be deferred.

## Suggested resolution

`ready`. All critic findings are now `pass` / `repaired` / `not-needed`.

Integrator notes:
- The SUMMARY.md change is an **in-place de-stub** of the existing `:83` row (drop `(stub)`), NOT an append — apply per the rewritten proposed-change block to avoid a duplicate-link build error.
- The `L1-L0/index.md` change is a genuine **new-row append** (no pre-existing nrm2 row) — apply normally.
- This promotes the existing `nrm2-mutation-rotation` stub → `firm`; ensure the stub's frontmatter `status: stub` is dropped/updated to `firm` when the body is applied.
- The two carry-forward OQ notes have been corrected to "already reconciled" — do NOT migrate them into the plan as actionable work (the targeted defects do not exist).
