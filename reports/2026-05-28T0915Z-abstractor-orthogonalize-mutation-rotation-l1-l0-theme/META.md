---
verifies: ../REPORT.md
critiqued_at: 2026-05-28T16:05:00Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-28T16:40:00Z
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

# META: verification of "L1>L0 theme sketch — orthogonalize-mutation-rotation"

## Critique

### Checks run

**citation-validity — warning.** Every claim carries a pointer and all the substantive
claims are supported by the source, but several line-range bounds drift by 1–3 lines against
the actual `palace/linalg/orthog.hpp` text (verified via codemap `read_range` 1-95 and
38-89). The functions and bodies are real and the cited content is in-range, so no claim is
fabricated — but the precision is below the citation bar and three pointers land on the wrong
line. Concretely (all line numbers verified against the codemap read):
- `OrthogonalizeColumnMGS` actually spans lines **40–52** (template 38–39, signature 40–42,
  body 43–52). The report cites it as `orthog.hpp:41-53` (Sub-pattern A citation, CYCLE.md
  L111; Verified-against L256). Start is mid-signature (41), end (53) is the blank line past
  the closing brace at 52. Inherited from the L1 entry, which uses the same `:41-53`.
- The header comment "Note order is important for complex vectors" is at line **47**, not 48.
  The report cites `orthog.hpp:48` (Sub-pattern A citation, CYCLE.md L113). Line 48 is
  actually `H[j] = dot_op(w, V[j]);`. This is an inherited drift — the L1 entry
  (`book/src/L1/orthogonalize.md:66`) also cites the comment as `:48`; both are off by one.
- `OrthogonalizeColumnCGS` `refine=false` path cited `orthog.hpp:57-72` (Sub-pattern B,
  CYCLE.md L149; Verified-against L258). Function signature begins at 56; the early-return +
  dot loop + GlobalSum + w.Add loop are lines 61–73. The cited range starts mid-signature and
  ends at 72, dropping the closing `}` of the w.Add loop at 73. In-range for the claimed
  content, bounds loose.
- CGS2 `if (refine)` block cited `orthog.hpp:73-87` (Sub-pattern C, CYCLE.md L188). Actual
  block is **74–87** (`if (refine)` at 74, closing `}` at 87). Start 73 is the prior loop's
  `}`. Off by one at the start.
- **`H[j] += dH[j]` accumulate cited at `orthog.hpp:81` (Status section, CYCLE.md L288). The
  accumulate is actually at line 84.** Line 81 is `Mpi::GlobalSum(m, dH.data(), comm);`. This
  is the largest drift (3 lines) and points at the wrong statement.
- **The `for (int j = 0; j < m; j++)` signedness quirk cited at `orthog.hpp:76` (Supporting
  evidence, CYCLE.md L324). The `int`-typed loop is at line 77.** Line 76 is
  `std::vector<ScalarType> dH(m);`. Off by one.
- The `orthog.hpp:18-90` scope range (Summary L32; Status L283) is generous — substantive
  content ends at the CGS close at line 88; `:18-90` over-reaches by ~2 lines into the
  namespace/`#endif` tail. Acceptable as a bounding pointer, noted for consistency.
All non-`orthog.hpp` pointers verified clean: `iterative.cpp:307-325` (dispatch wrapper, exact),
`iterative.cpp:622/630/631-632` (GMRES Arnoldi, exact), `iterative.cpp:808-811` (FGMRES,
exact — the report's `:809` call and `:810-811` normalize match), `romoperator.cpp:51-66`
(ROM wrapper, forwards `j`, threads `dot_op`, exact), `test-orthog.cpp:99-120` (empty-basis
edge — the `Real Empty` TEST_CASE with `m = 0` and `CHECK_THAT(w, RangeEquals(w_orig))`,
exact).

**surface-or-evidence — pass.** This is a new theme (`book/src/L1-L0/orthogonalize-mutation-rotation.md`)
plus two index touches — net-new surface, not a refinement of an existing operator/theme. The
refinement-shaped-proposal rule does not apply. The theme creates surface AND grounds it in
positive source sites throughout; no pure-rotation-claim-without-surface problem.

**rotation-quality — pass.** The L1→L0 direction is narrated **forward** throughout: the
Summary ("lowers the L1 form forward into those L0 patterns"), the L0-form (RHS) prose ("the
L1 pair `(w', H)` materialises as mutation of the two caller-owned buffers"), and each
sub-pattern's justification all describe how the L1 form rewrites *down* to L0, never how L0
lifts up. The three reverse-direction notes (`m` off-by-one, `dH` scratch, B-weighted hook)
are correctly quarantined in "Open questions / caveats" and explicitly labelled
"reverse-direction note … kept out of the formal theme content per the high→low discipline" —
exactly per the layers-defined-high→low invariant. The rotation is a genuine state-hiding
compression (drops two destination buffers + `MPI_Comm` from the signature; collapses the
in-place `w` thread and raw-pointer `H` write into a returned pair), not a 1:1 rename.

**variant-axis-coverage — pass.** This is the strong point of the report. The three L0
loop-structures map correctly and exhaustively to the firm L1 `orthogonalize` MGS/CGS/CGS2
axis. Verified against the source: Sub-pattern A (MGS, single interleaved loop, `m`
reductions of size 1) matches `orthog.hpp:45-51` — one `j`-loop, dot→`GlobalSum(1,...)`→`w.Add`
per iteration, the in-place `w.Add` at iteration `j` read by the dot at `j+1`. Sub-pattern B
(CGS, split two-phase, 1 reduction of size `m`) matches `orthog.hpp:61-73` — `m==0` return,
all `m` dots against the original `w`, single `GlobalSum(m, H)`, then `m` `w.Add`s.
Sub-pattern C (CGS2, doubled two-phase, 2 reductions of size `m`) matches the `if (refine)`
block `orthog.hpp:74-87` — `dH` scratch, second dot loop, second `GlobalSum(m, dH.data())`,
`H[j] += dH[j]` accumulate + second `w.Add`. The reduction-ordering distinction is correctly
characterized: the interleaved-vs-batched-dots difference is a **dependency-structure /
collective-shape** distinction (m×1 vs 1×m vs 2×m), and the report correctly frames the
collective shape as load-bearing (applicability condition 5: "does not change the lowered
value, only the collective shape") while the MGS sequential dependency is correctly framed as
**structural** (the loop carry IS the `w^(j)` intermediate) and CGS2's re-application as
**algebraic** (idempotence law the FP breaks). The Householder fourth variant is scoped out
upstream in the L1 entry (no Palace path); the theme inherits that scoping correctly. No
hidden branch. The `int`-vs-`size_t` loop-index quirk is correctly flagged transparent.

**cross-reference-integrity — pass.** All `[link]` references resolve: `[L1/orthogonalize]`
(../L1/orthogonalize.md — exists, firm cycle-012), `[dot]`/`[axpy]` (../L1/dot.md,
../L1/axpy.md — both exist). The two sibling-theme precedents named in inputs
(`axpby-mutation-rotation.md`, `apply-linop-mutation-rotation.md`) exist in `book/src/L1-L0/`.
All named L0 symbols (`OrthogonalizeColumnMGS`, `OrthogonalizeColumnCGS`,
`OrthogonalizeIteration`, `OrthogonalizeColumn`, `IdentityInnerProduct`) verified to exist via
codemap. The slug `orthogonalize-mutation-rotation` is consistent across all three edit
blocks. The two index-edit blocks (`L1-L0/index.md` table row, `SUMMARY.md` list entry) have
well-defined homes (the L1-L0 theme table at index.md:17-24; the L1-L0 list at SUMMARY.md:57-65)
— note neither edit block carries an explicit insertion anchor, so the integrator must place
them within those blocks; this is routine, non-blocking.

**edge-label-fidelity — pass.** The declared edge is L1→L0 (slug `*-mutation-rotation`, dir
`book/src/L1-L0/`). The prose discusses exactly that edge throughout — L1 `(w', H)` lowering
to L0 in-place `w` + raw-pointer `H` across `orthog.hpp`. No edge/prose mismatch. The single
forward-looking mention of an L2 `krylov-step` lift is correctly framed as a downstream
consumer note, not a claim about this edge.

**plan-kind-consistency — pass.** Declared `status: firm` / `structural` (with one algebraic
sub-rule for CGS2). Content matches: every L0 form is read from a positive source site (no
negative anchors, no reconstruction, no rough-in placeholders), the dispatch wrappers and all
call-site families are read directly, and the variant loop-structures + collective shapes are
read off the bodies. The "Speculative L1 operators: None" and "no new vocabulary" are
consistent with a pure-lowering-of-firm-operator-onto-firm-leaves shape. The status correctly
avoids `partly-constructive` (nothing is materialized from negative anchors) — appropriate.

**skill-uptake-survey — warning.** The report's shape (a refinement/lowering surface with
rotation citations + variant-axis enumeration) implies several relevant skills exist
(`verify-rotation-citation`, `propose-rotation`, `classify-variant-axis`,
`verify-citation-range`). The report demonstrates the *codemap-first localization* uptake well
(explicit "read in full via codemap", `get_call_sites` results captured in Supporting
evidence — exactly the MCP-first-localization codification) and references a future
`lowering-verifier` audit. But it does not reference invocation of the citation-range /
rotation-citation skills, which would have caught the line-range drifts flagged under
citation-validity. Pure telemetry surface, non-blocking.

### Issues found

1. **[citation-validity, medium] `H[j] += dH[j]` accumulate cited at wrong line.** CYCLE.md
   Status section (L288) cites the CGS2 accumulate at `orthog.hpp:81`; the accumulate
   `H[j] += dH[j]` is actually at line **84**. Line 81 is `Mpi::GlobalSum(m, dH.data(), comm)`.
   Largest drift (3 lines), points at the wrong statement. Candidate fix: `:81` → `:84`.

2. **[citation-validity, low] `int`-loop signedness quirk cited at wrong line.** CYCLE.md
   Supporting evidence (L324) cites the `for (int j = 0; j < m; j++)` at `orthog.hpp:76`; it
   is actually at line **77** (line 76 is `std::vector<ScalarType> dH(m);`). Off by one.
   Candidate fix: `:76` → `:77`.

3. **[citation-validity, low] Header comment "Note order is important…" cited at wrong line.**
   Sub-pattern A citation (CYCLE.md L113) cites `orthog.hpp:48`; the comment is at line **47**
   (line 48 is `H[j] = dot_op(w, V[j]);`). Off by one. Inherited from
   `book/src/L1/orthogonalize.md:66`, which has the same `:48` drift — a fix here should note
   the upstream entry shares the error (out-of-role to edit the L1 entry; surface as a
   drive-by). Candidate fix: `:48` → `:47`.

4. **[citation-validity, low] MGS function range bounds.** Sub-pattern A / Verified-against
   cite `orthog.hpp:41-53`; the function is **40–52** (template 38–39). Start mid-signature,
   end one past the closing brace. Inherited from the L1 entry. Candidate fix: `:41-53` →
   `:40-52` (or `:38-52` to include the template).

5. **[citation-validity, low] CGS / CGS2 range bounds loose.** Sub-pattern B `:57-72` should
   be ~`:56-73` (signature 56–58; body through w.Add-loop close at 73). Sub-pattern C `:73-87`
   should be `:74-87` (block starts at the `if (refine)` on 74; 73 is the prior loop's `}`).
   Both in-range for claimed content; bounds imprecise.

6. **[citation-validity, low] `orthog.hpp:18-90` scope over-reaches.** Substantive content
   ends at the CGS close (line 88); `:18-90` includes ~2 lines of namespace/`#endif` tail.
   Cosmetic; used as a bounding pointer in Summary (L32) and Status (L283).

7. **[skill-uptake-survey, low] No citation-range / rotation-citation skill invocation
   referenced.** The line-range drifts in issues 1–6 are exactly what `verify-citation-range`
   targets; the report references codemap localization and a future `lowering-verifier` audit
   but not the citation-range verification skill. Telemetry only.

8. **[cross-reference-integrity, low / non-blocking] Index-edit blocks lack insertion
   anchors.** The `book/src/L1-L0/index.md` table-row edit and the `book/src/SUMMARY.md`
   list-entry edit give the new line but no positional anchor; the integrator must place them
   within the existing L1-L0 blocks (index.md:17-24, SUMMARY.md:57-65). Routine integration
   detail, recorded for the integrator.

### Drive-by observation (out-of-role)

The shared `orthog.hpp:48` / `:41-53` citation drift in issues 3–4 originates in the firm L1
entry `book/src/L1/orthogonalize.md` (lines 66 and 255) and is inherited by this theme. A fix
to this report should not silently diverge the two; the upstream L1 entry citation is also
off-by-one on the comment line and would benefit from the same correction (out of this
report's repair authority — flagged for the integrator / a future lifter touch).

## Repair

### Method note

I re-verified every flagged `orthog.hpp` pointer against the codemap ground truth
(`mcp__palace-codemap__read_range palace/linalg/orthog.hpp` over the 18-90 region plus
single-line confirmations). Per CLAUDE.md MCP-first-localization, the codemap is the
authoritative line index. The codemap's line numbers came out **one higher** than the
critic's candidate-fix numbers for the same statements, so where the critic and codemap
disagreed I repaired to the codemap value. Two of the critic's flagged drifts turned out to
be codemap-correct as the report already had them (see "Not repaired", below).

### Fixes attempted

- **Finding (issue 1)**: `H[j] += dH[j]` accumulate cited at `orthog.hpp:81` (wrong
  statement — `:81` is the dot-loop close `}`).
  - **Decision**: repaired.
  - **Action**: Status section — `:81` → `:85` (codemap confirms `H[j] += dH[j];` at line 85;
    the critic's `:84` was itself one low against the codemap). CYCLE.md Status.

- **Finding (issue 2)**: `for (int j ...)` signedness quirk cited at `orthog.hpp:76` (wrong
  statement — `:76` is the `if (refine)` block-open `{`).
  - **Decision**: repaired.
  - **Action**: Supporting evidence — `:76` → `:78` (codemap confirms `for (int j = 0; ...)`
    at line 78; critic's `:77` was one low). CYCLE.md Supporting evidence.

- **Finding (issue 5, CGS2 bounds)**: `if (refine)` block cited `orthog.hpp:73-87`; block
  actually starts at the `if (refine)` (line 75) and closes at line 88.
  - **Decision**: repaired.
  - **Action**: `:73-87` → `:75-88` in both occurrences (Sub-pattern C citation + Verified-
    against entry). CYCLE.md Sub-pattern C citations + Verified-against.

- **Finding (issue 5, CGS bounds)**: `OrthogonalizeColumnCGS` `refine=false` cited
  `orthog.hpp:57-72`; the body's `w.Add` loop closes at line 74, so `:72` dropped the tail.
  - **Decision**: repaired.
  - **Action**: `:57-72` → `:57-74` in both occurrences (Sub-pattern B citation + Verified-
    against entry). CYCLE.md Sub-pattern B citations + Verified-against.

- **Finding (issue 7, skill-uptake-survey)**: report did not reference invoking the
  citation-range / rotation-citation verification skills.
  - **Decision**: not-needed (telemetry only; non-blocking; no content defect to repair).

- **Finding (issue 8, index-edit insertion anchors)**: the `L1-L0/index.md` and `SUMMARY.md`
  edit blocks carry no positional anchor.
  - **Decision**: not-needed (routine integrator placement; critic flagged it as
    non-blocking; the homes are well-defined — index.md L1-L0 table + SUMMARY.md L1-L0 list).

### Not repaired (already codemap-correct)

- **Issue 3 (comment line)**: report cites the "Note order is important for complex vectors"
  comment at `orthog.hpp:48`. The codemap places that comment at **line 48** — the report is
  correct. The critic's `:47` candidate was a codemap-drift; no edit applied.
- **Issue 4 (MGS function range)**: report cites `OrthogonalizeColumnMGS` at `orthog.hpp:41-53`
  (signature line 41 → function close line 53). The codemap confirms this range; the critic's
  `:40-52` candidate was one low. No edit applied.
- **Issue 6 (`:18-90` scope over-reach)**: cosmetic bounding pointer over the header-only
  inline region; codemap shows substantive content closing ~line 89, so `:18-90` is a tight
  enough bound. Cosmetic-only per the critic; left as-is.

### Unrepairable findings

None. All citation-validity drifts were mechanical line-offset corrections within repair
authority (the original agent's line ranges slipped a few lines / one pointer landed on the
adjacent statement). No substantive authoring required.

## Suggested resolution

`ready`. The six flagged `orthog.hpp` pointers are resolved: 4 corrected to the codemap
ground truth, 2 confirmed already-correct (critic's candidates were themselves off-by-one
against the codemap). All non-`orthog.hpp` pointers were already verified clean by the critic.
The content checks all passed (firm/structural, variant axes exhaustive, recognition-set
closure confirmed). skill-uptake-survey and the index-anchor note are telemetry/routine and
need no repair.

Note for the integrator: the **drive-by observation** is still live but is genuinely
codemap-corrected here, not inherited as-drifted — the upstream L1 entry
`book/src/L1/orthogonalize.md` cites the same comment at `:48` and the MGS function at
`:41-53`, both of which the codemap confirms as **correct**. So there is no divergence to
worry about and no upstream off-by-one fix is required; the critic's drive-by was predicated
on the critic's own (one-low) line index. No follow-up lifter touch needed on that account.
