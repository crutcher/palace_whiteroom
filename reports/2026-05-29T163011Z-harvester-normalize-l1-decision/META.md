---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T165520Z
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
repaired_at: 2026-05-29T170145Z
repairer_version: 1
repairs:
  citation-validity: repaired
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

# META: verification of "Formalize normalize at L1" (cycle-026 dispatch 4, decision-first → firm L1 `normalize`)

## Critique

### Checks run

**citation-validity — pass (one minor pinpoint-drift warning, see Issues).** Ran `citecheck.py --scan` on the report: **33 ok / 0 failing**, matching the report's claim exactly. Re-ran `--anchor` on every load-bearing pinpoint and confirmed each against on-disk `reference/palace/` (the report correctly notes the codemap does not index `vector.hpp`, so on-disk is authoritative):
- **Positive source site** `vector.hpp:262-270` — `--anchor 'Normalize'` → [262,264], `'return norm'` → 269, `'1.0 / norm'` → 268, `'MFEM_ASSERT'` → 267. Read the source directly: the body is `auto norm = Norml2(comm, x); MFEM_ASSERT(norm > 0.0, "Zero vector norm in normalization!"); x *= 1.0 / norm; return norm;` — **verbatim** what the report transcribes. The function exists, is a free template returning the norm by value. Firm-on-positive-structure footing confirmed.
- **GMRES Arnoldi** `iterative.cpp:631-632` and `:811` — `--anchor 'Hj'` resolves both. Read source: `Hj[j + 1] = linalg::Norml2(comm, w); w *= 1.0 / Hj[j + 1];` at both sites (the `:811` site's surrounding lines are 808-812). The norm IS stored as the Hessenberg sub-diagonal AND reused to rescale — doubly load-bearing, exactly as claimed. Note the report cites `:632` and `:811` for the *rescale* line; on-disk the second site's rescale is at line 811 (confirmed by `--anchor`), so the report's `:811` pinpoint is correct (no brace-drift defect despite the dispatch warning).
- **Power iteration** `operator.cpp:660-661,673,676` — read source 655-679: `l = Normalize(comm, u)` at 673, consumed at 676 `res = std::abs(l - l0) / l0`. The returned norm genuinely IS the dominant-eigenvalue estimate driving the convergence test. Load-bearing claim holds.
- **NEP deflation** `nleps.cpp:610-611,617` — read source 607-618: `const auto scale = linalg::Norml2(GetComm(), v); v *= 1.0 / scale;` then `H.col(k).head(k) = v2 / scale;`. The norm `scale` rescales both `v` and the companion `v2` — doubly reused, accurately described as the inline un-fused form using the *unweighted* norm.
- **B-weighted negative-finding sites** — read `arpack.cpp:438`, `slepc.cpp:475`, `nleps.cpp:114`: all three are `return linalg::Norml2(comm, x, *opB, Bx);` — pure norm computations that return the value (error/eigenvector norms), NOT in-place rescales. The report's claim "no fused Normalize-with-B; these sites do not rescale" is correct. The header comment at `vector.hpp:262` ("possibly with respect to an SPD matrix B") is indeed present and aspirational (the sole overload takes no `B`).
- **In-artifact idiom-collapse witnesses** — verified `scal.md:65` (names `Normalize(x) = scal(1/nrm2(x), x)` and flags the harvest OQ), `scal.md:85` (the fused-`Normalize`-factors-at-L1 note), `orthogonalize-composition-lowering.md:229` (`nrm2`/`scal` basis-normalize step), `orthogonalize.md:158` (`scal (1/‖residual‖)` + Hessenberg sub-diagonal), `scal-mutation-rotation.md:48-49` (names the `linalg::Normalize` rescale). All land on supporting text. The one pinpoint that does NOT land is `matrix-weighted-norm.md:55` (see Issues) — the test-coverage statement it is cited for actually lives at `:108-110`.

**surface-or-evidence — pass.** This is a NEW firm operator (a new chapter `book/src/L1/normalize.md`), not a refinement of an existing operator/theme, so the refinement-surface-or-retroactive-backfill rule applies in its "new surface" form: the report proposes new artifact surface (a full firm chapter + index cohort bullet + dep-map row + SUMMARY entry) AND grounds every claim in positive L0 source. Not a pure rotation_claim. Pass.

**rotation-quality — pass.** The L1 form is strictly more abstract / more equational than the L0 form: the mutating free-function `linalg::Normalize(comm, x)` (in-place receiver overwrite, MPI communicator, reciprocal-then-multiply, return-by-value) rotates to a pure `normalize :: Tensor[N] -> (Scalar, Tensor[N])` with the in-place rescale, the communicator, the reciprocal-vs-divide trick, and the receiver overwrite all explicitly pushed down as L1>L0 lowering concerns. The returned-norm side-output is promoted to a first-class result component. This is genuine state-hiding + side-output-to-result-component compression, not a 1:1 rename. The signature faithfully captures the L0 source (verified against `vector.hpp:262-270`).

**variant-axis-coverage — pass.** The report identifies the element-type axis (real | complex) as the sole inherited axis and correctly argues no new axis is introduced by the fusion (the `Normalize` template is `VecType`-generic; the inner `Norml2` returns a real scalar in both cases; the `*= 1.0/norm` dispatches to the matching `operator*=`). It explicitly addresses and scopes-out: no constant-folding axis (the rescale `1/β` is a runtime value, never 0/1/-1 since `β > 0`), no extra reduction-order variant beyond `nrm2`'s inherited one. The B-weighted axis is explicitly scoped out as an in-chapter rough-in note with a stated promotion trigger. No hidden branches. The partiality at `x = 0` is correctly identified as a semantic addition rather than a variant axis.

**cross-reference-integrity — pass.** All live `[link]` references inside the `new:normalize.md` body resolve from the `book/src/L1/` location: `nrm2.md`, `scal.md`, `matrix-weighted-norm.md`, `orthogonalize.md`, `../L1-L0/scal-mutation-rotation.md`, `../L1-L0/nrm2-mutation-rotation.md`, `../L2-L1/orthogonalize-composition-lowering.md` — all confirmed on disk. The one not-yet-authored target (`normalize-mutation-rotation`, L1>L0) is correctly referenced as **plain text in backticks**, NOT a live link (confirmed no `[...](...)` form in the body; file confirmed absent) — correct per `rough-in-forward-reference-must-be-plain-text-not-live-link`. **Build-readiness fence guard:** ran `grep -n '^```'` → 10 fences = 5 balanced blocks (even parity). The `new:book/src/L1/normalize.md` block (lines 60-181) **ENCLOSES the full firm body** — `## Status` (157), `## Signature` (75), `## Algebraic laws` (101), `## Evidence` (166) are all inside the fence. No nested triple-backtick fences inside the body (it uses 4-space-indented code blocks for the template/signature), so no parity-breaking nested-fence variant. This is NOT the cycle-019 fence-truncation defect — the firm apparatus is inside the fence. The three `edit:` blocks (index cohort bullet, index dep-map row, SUMMARY) all have search-anchors that match on-disk exactly (`index.md:37`, `index.md:75`, `SUMMARY.md:67`). Chapter convention: sibling L1 chapters (`scal.md`, `nrm2.md`, `axpy.md`) carry no YAML frontmatter and use a `## Status` section — the new chapter follows this convention exactly (no frontmatter gap).

**edge-label-fidelity — pass / not strictly applicable.** This is an L1 operator entry, not a lowering theme carrying an L_{n+1}→L_n edge label. The body's "L1 vs L0 distinction" section and the references to `nrm2-mutation-rotation` / `scal-mutation-rotation` (both L1>L0) are correctly directed (the prose narrates L1→L0 lowering, matching the L1>L0 edge of the referenced themes). No mislabeled edge.

**plan-kind-consistency — pass.** Declared kind is a firm L1 operator (decision-first harvest deciding YES). The content shape matches: a full firm body with Signature, Semantics, six algebraic laws, Dependencies, Variant axes, a `## Status` line reading `firm` (firm-on-positive-structure), an Evidence block, and an L1-vs-L0 section. No rough-in placeholders in the firm claim. The B-weighted `normalize_B` is correctly classified DOWN to an in-chapter rough-in note (not mis-elevated to a firm sibling) with explicit dual justification (no fused Palace site + inherited `matrix-weighted-norm` test-coverage bound) and a stated promotion trigger — consistent with the report's own framing and with the `matrix-weighted-norm` status it inherits.

**skill-uptake-survey — pass.** The report's shape implies the `verify-citation-range` skill (now realized mechanically via `tools/citecheck/`); the report explicitly states it self-verified all load-bearing citations via `citecheck.py --anchor` (CYCLE.md:38,168-176,209). The decision-record shape implies the "promote a speculative L1 operator to firm only when small AND when it simplifies higher forms" directive checklist — the report walks all three criteria plus the firm-on-positive-structure escape explicitly (CYCLE.md:23-56). Skill/directive uptake is surfaced, not hidden.

### Decision assessment (load-bearing for this dispatch)

The YES verdict is **justified**. I independently confirmed each leg of the decision argument against source:
1. **Positive source site** — `linalg::Normalize` at `vector.hpp:262-270` exists verbatim and returns the norm; this qualifies as firm-on-positive-structure independent of the simplification argument (the `apply_nonlinear_pencil`/`lu_solve` precedent applies — the laws are syntactic identities on a read closure, not literature-inferred convergence semantics, so the absence of a dedicated `test-normalize` correctly does NOT gate the firm status).
2. **Returned-norm load-bearing at ≥3 consumers** — all three GENUINELY consume the returned norm: GMRES stores it as `Hj[j+1]` (Hessenberg sub-diagonal) at 631/811; power-iteration uses `l = Normalize(...)` as the eigenvalue estimate at 673 consumed at 676; NEP rescales both `v` and companion `v2/scale` at 610-611/617. A bare `scal(1/nrm2(x), x)` would discard this intermediate. The "distinct named operator, not a bare composition" argument holds.
3. **Collapses a recurring 2-op idiom** — confirmed the `nrm2 ∘ scal` idiom is currently spelled by hand at scal.md:65,85, scal-mutation-rotation.md:48-49, orthogonalize-composition-lowering.md:229, orthogonalize.md:158 (≥2 firm consumers).

The `normalize_B` down-classification to an in-chapter rough-in note is the **right call**: there is no fused Palace `Normalize`-with-B (the three B-weighted `Norml2` sites are error-norm `return` computations, not rescales), and a fused `normalize_B` cannot be firmer than its `matrix-weighted-norm` constituent (which is `rough-in (test-coverage-bounded)`). The stated promotion trigger (an inline `scale = Norml2(comm, v, B, Bv); v *= 1/scale` site surfacing) is concrete and correct.

### Issues found

1. **[minor / warning] Pinpoint-drift on `matrix-weighted-norm.md:55` inside the firm artifact body.** CYCLE.md:148 (inside the `new:book/src/L1/normalize.md` proposed-changes block) cites `book/src/L1/matrix-weighted-norm.md:55` as evidence that `matrix-weighted-norm` is `rough-in (test-coverage-bounded)` / has "no dedicated test on the SPD-weighted overload". On disk, `matrix-weighted-norm.md:55` is **law 5 (reverse triangle inequality)**, unrelated to test coverage. The supporting text (the `## Status` block with the `rough-in (test-coverage-bounded)` declaration and the "no dedicated Palace test exercises the SPD-weighted overload" sentence) is at `matrix-weighted-norm.md:108-110` (and the promotion-gate detail at :113-114, :143). The CLAIM is true (matrix-weighted-norm IS test-coverage-bounded), but the cited line does not land on the supporting text. Because this citation sits inside the `new:` block, it will be written into the firm `normalize.md` artifact as-is. Severity minor: `citecheck --scan` passes (the line is in-bounds and the path is clean — this is a semantic pinpoint miss, not a bounds/path error). Location: `CYCLE.md:148`, theme §"B-weighted sibling normalize_B — rough-in note", reason (2) "Inherited test-coverage bound". Suggested fix: change the pinpoint to `book/src/L1/matrix-weighted-norm.md:108-110` (the `## Status` block) or `:110` specifically.

2. **[trivial / observation] Garbled clause in the §Context `axpy` analogy.** CYCLE.md:69 (inside the `new:` block): "...a recognised composite that Palace ships as one symbol, with one extra load-bearing output (the recovered norm, analogous to `axpy`'s lack of any — but here the extra output is what justifies the fusion)." The parenthetical "analogous to `axpy`'s lack of any" is self-contradictory/awkward — it asserts `normalize` has an extra output that is "analogous to" `axpy` having NO extra output. The intended contrast (normalize is a fusion *like* axpy, but unlike axpy it carries an extra returned scalar) is muddled. Not a correctness defect, but it lands in the firm artifact prose. Location: `CYCLE.md:69`, §Context. Suggested fix: drop or rephrase the "analogous to `axpy`'s lack of any" clause to a clean contrast (e.g. "unlike `axpy`, which returns nothing, `normalize`'s extra returned scalar is what justifies naming the fusion").

3. **[informational, not a defect] Self-resolved OQ + plan-item closure asserted by a producer.** CYCLE.md:56,215 assert that OQs `normalize-as-fused-l1-primitive` and `normalize-and-normalize-b-weighted-l1-candidates` resolve decided-yes and that plan item `normalize-l1-primitive-harvest` (priorities.md:54) is completed. These are correct (the plan item at priorities.md:54 is exactly this harvest, "Held for cycle-020", and the OQs are the named ones) and the report frames them as resolutions for the integrator to enact — it does not itself mutate the OQ ledger or priorities.md (correct write-authority). No action needed; flagged only so the integrator-per-report promotes the OQ resolution and the finalize/meta-phase migrates the plan-item closure.

4. **[informational, not a defect] Firm-count edit correctly deferred.** The report correctly does NOT edit the "Firm (19)" prose at `index.md:31` — it flags the 19→20 bump for layer-intro-author (CYCLE.md:214). Verified the three `edit:` blocks touch only the cohort bullet (`index.md:37`), the dep-map row (`index.md:75`), and SUMMARY (`:67`); none touch the "Firm (19)" motif text. The dep-map currently has 19 firm rows, consistent with the count. No incorrect count edit was made. No action needed.

---

## Repair

### Fixes attempted

- **Finding (Issue 1, citation-validity warning)**: Pinpoint-drift inside the firm artifact body — CYCLE.md:148 cites `book/src/L1/matrix-weighted-norm.md:55` (which is law 5, reverse triangle inequality) for the test-coverage bound, but the supporting `## Status` text (the `rough-in (test-coverage-bounded)` declaration + "no dedicated Palace test exercises the SPD-weighted overload") lives at `matrix-weighted-norm.md:108-110`. The claim is true; only the pinpoint is wrong. Lands in the firm `normalize.md` body.
  - **Decision**: repaired
  - **Action**: In the `new:book/src/L1/normalize.md` proposed-changes block (CYCLE.md §"B-weighted sibling `normalize_B` — rough-in note", reason (2) "Inherited test-coverage bound"), changed the pinpoint `book/src/L1/matrix-weighted-norm.md:55` → `book/src/L1/matrix-weighted-norm.md:108-110`. Independently verified against on-disk `book/src/L1/matrix-weighted-norm.md`: `:55` is law 5; the `## Status` header is `:108`, the `rough-in (test-coverage-bounded)` declaration + the "no dedicated Palace test exercises the SPD-weighted overload" sentence span `:108-110`. The corrected pinpoint now lands on the supporting text. This is a small-offset pinpoint correction (the original agent slipped from the Status block to a law line) — squarely in repair scope.

- **Finding (Issue 2, trivial/observation)**: Garbled `axpy` analogy clause inside the firm artifact prose — CYCLE.md:69 reads "...one extra load-bearing output (the recovered norm, analogous to `axpy`'s lack of any — but here the extra output is what justifies the fusion)." The "analogous to `axpy`'s lack of any" parenthetical is self-contradictory (asserts an extra output that is "analogous to" `axpy` having NO extra output) and lands in the firm `normalize.md` body.
  - **Decision**: repaired
  - **Action**: In the `new:book/src/L1/normalize.md` proposed-changes block (§Context), rephrased to a clean contrast: "a recognised composite that Palace ships as one symbol. Unlike `axpy`, which returns nothing, `normalize` carries one extra load-bearing output (the recovered norm), and that extra returned scalar is what justifies naming the fusion." Surgical prose fix preserving the intended meaning (normalize is a fusion like axpy, but unlike axpy it carries a load-bearing returned scalar). No content/claim change — squarely in repair scope.

- **Finding (frontmatter check)**: stale `verifies: ../REPORT.md`.
  - **Decision**: not-needed
  - **Action**: META.md frontmatter already reads `verifies: ../CYCLE.md` (line 2). No stale reference present.

- **Issues 3 & 4 (informational, not defects)**: OQ/plan-item self-resolution framing and the correctly-deferred firm-count edit. The critic flagged both as no-action-needed integrator notes, not defects. No repair attempted; carried forward for the integrator-per-report (OQ promotion) and finalize/meta-phase (plan-item closure, firm-count refresh).

### Post-repair verification

Re-ran `tools/citecheck/citecheck.py --scan` on the repaired CYCLE.md: **33 ok, 0 failing (33 citations checked)** — unchanged from the critic's count. Both edits stayed within in-bounds, path-clean ranges (the `:108-110` pinpoint is in bounds for the 144-line `matrix-weighted-norm.md`); the prose fix touches no citation. No new citation regressions introduced.

### Unrepairable findings

None. Both flagged items were mechanical/surgical (a small-offset pinpoint correction and a self-contained prose fix), both applied. All 8 critic checks pass; no substantive authoring or content decision was required.

## Suggested resolution

`overall_status: ready` — integrator may apply this report's proposed-changes as-is. Both repairs land inside the `new:book/src/L1/normalize.md` block, so the firm chapter is written with the corrected pinpoint and clean prose. Integrator notes carried from the critic's informational issues:
- Promote the OQ resolutions on application: `normalize-as-fused-l1-primitive` and `normalize-and-normalize-b-weighted-l1-candidates` → decided-yes (firm `normalize`; in-chapter rough-in note for `normalize_B`); register the L1>L0 `normalize-mutation-rotation` theme as an OQ residual (stub-on-integration acceptable per the implied-component directive).
- Defer to finalize/meta-phase: close plan item `normalize-l1-primitive-harvest` (priorities.md:54); the `book/src/L1/index.md` "Firm (19)→(20)" motif/count refresh is layer-intro-author work (correctly NOT edited by this report).
