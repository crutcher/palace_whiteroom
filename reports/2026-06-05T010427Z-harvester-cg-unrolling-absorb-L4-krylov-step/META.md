---
verifies: ../CYCLE.md
critiqued_at: 2026-06-05T012000Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-05T013000Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "Absorb the CG-concrete v0.5 first-iteration-unrolling worked datum into L4 `krylov-step` Form B"

## Critique

### Checks run

**citation-validity — warning.** Ran `citecheck --scan` (33 ok / 4 failing of 37) and `--anchor` on the load-bearing L0 pinpoints, plus a direct on-disk read of `iterative.cpp:358-486`. The four citecheck non-OK lines are NOT real bounds drift: three are `[AMBIG]` basename collisions in prose (`krylov-step.md`, `gmres.md` mentioned without a full path — these resolve correctly when the full path is supplied) and one is the `[OOB] cg.md:393-425`, which the report *explicitly and repeatedly* labels as the historical "pre-reduction range" / "formerly cited" (CYCLE.md:40, :169, :174) — a deliberate provenance breadcrumb, not a live claim. Every live L0 anchor verified exactly: `iterative.cpp:427` (`for (; it < max_it ...)`), `:434-441` (the `if (!it) { p = z; } else { AXPBY(1.0, z, beta/beta_prev, p); }` branch — `--anchor 'if (!it)'` → line 434 ✓), `:443` (`A->Mult(p, z)`), `:444` (`Dot(comm, z, p)`), `:446` (`alpha = beta/denom`), `:448-449` (`x.Add`/`r.Add`), `:451` (`beta_prev = beta`), `:460` (`beta = Dot(z, r)`), `:462` (`res = std::sqrt(std::abs(beta))`), `:360-486` (`CgSolver<OperType>::Mult`, `--anchor 'CgSolver'` → :361/:366/:368 ✓, closing `}` at :486 ✓). The transcribed cg.md:27-141 content matches the on-disk slice faithfully (the `CgState<S>` schema, `cg_first_step`/`cg_steady_step` bodies, `cg_solve` with `iterate_while_with_prev`, the three "what this rotation hides" points, the four-clause equivalence + `forget_beta_prev` projection, and the pcg variant all reproduce the slice verbatim-in-substance). The warning is driven not by these but by a recurring **factual mischaracterization** of the re-anchor target — see Issue 1.

**surface-or-evidence — pass.** This is refinement-shaped (modifies an existing firm chapter's surface) AND carries the rotation evidence (the v0.4↔v0.5 self-rotation with `forget_beta_prev`). The load-bearing question — is the absorbed material genuinely the CG-CONCRETE worked instance and NOT a duplicate of the abstract rotation in `concepts/first-iteration-unrolling.md`? — resolves cleanly. The concept page (`first-iteration-unrolling.md:19-37`) carries only the *generic* signatures (`first_step :: ... -> State -> StepResult`, `prev_state_field`, "PrevCarry threaded externally") with no CG body. The new subsection lands the concrete `axpby 1.0 s.r (s.beta / beta_prev) s.p`, the `alpha = s.beta / (dot Ap p')` CG arithmetic, the typed `CgState<S>` schema, and the pcg specialisation — material the concept page does NOT carry. The subsection cross-references the concept page for the abstract rotation rather than restating it (CYCLE.md:75, :79). Non-duplication confirmed. Record-definition sub-check: `CgState<S>` is named in the worked-example signatures and IS defined in-chapter (the `type CgState<S> = { ... }` block at the head of the subsection, fields + types + the `beta_prev`-elision note) — definition home present.

**rotation-quality — pass.** The worked example asserts an L4→L4 self-rotation (state hiding: `beta_prev` dropped from the steady-state schema; branch elision: the `if it==0` hoisted out). This is strictly more compact than Form A (the schema is one scalar lighter; the steady body is straight-line). It is not a 1:1 rename. The L4 notation follows the strawman convention: Haskell `::` arrow signatures, TS `{ field: type }` records, do/let-binding bodies, fenced as indented code. The firm-on-positive-structure escape is correctly applied — the claims (`forget_beta_prev` commutation, branch-hoisting observational identity) are syntactic L4-self-rotation identities on a fully-specified positive read closure (`CgSolver::Mult`, `iterative.cpp:360-486`); no convergence-semantics claim is made, so no test is gated. `firm` is the correct status (matches the existing Form A / Form B basis).

**variant-axis-coverage — pass.** The first-iteration-unrolled axis is the variant under treatment, and both arms (first-step / steady-step) are landed. The preconditioner axis is covered by the explicit `### Variant: pcg under v0.5` paragraph (`pcg_first_step`/`pcg_steady_step` + the `forget_z ∘ forget_beta_prev` four-way equivalence). No hidden branches: the report notes the `0/0`-avoidance branch is the one branch the rotation removes, and accounts for where it goes (static call-site obligation `beta_prev > 0`).

**cross-reference-integrity — warning.** The four edits' `old_string` anchors all match the on-disk artifact verbatim (line 82 §Semantics Form B paragraph with the dangling `cg.md:*` tail; line 152 §Status; line 171 §Evidence bullet — all confirmed present). The re-anchor targets resolve: `concepts/first-iteration-unrolling.md` exists; `L1-L0/ksp-solve-mutation-rotation.md` §"Sub-pattern B" exists at :159 with `iterative.cpp:360-486` at :163 and the per-step kernel `:427-464` at :217; the L2 §Evidence line-138 registry row exists and already records the CG L4-v0.5 material. The `[link]`s in the inserted prose (`../concepts/first-iteration-unrolling.md`, `../L1-L0/ksp-solve-mutation-rotation.md`) resolve. The warning is the same mischaracterization as Issue 1: the re-anchor prose calls `ksp-solve-mutation-rotation.md` the "firm L0 terminal home" but that chapter's `## Status` is `rough-in`, not `firm` — see Issue 1 for why this is a prose-fidelity warning and not a rank-invariant break.

**edge-label-fidelity — pass.** No cross-layer edge label is asserted by this dispatch; it is an in-L4 worked example plus an L4→L0 navigational reference. The L0-ground prose discusses exactly the CG body it cites (`iterative.cpp:434-441` branch, `:443` apply, `:446-449` updates, `:451` carry, `:460-462` readout). The "this is the CG witness of the L4 non-law (form-equivalence-under-monad-laws)" cross-reference points at the chapter's own §"Algebraic laws" (line 110), correctly.

**plan-kind-consistency — pass.** Declared kind is a `firm` worked-example absorption into an existing firm chapter. The content shape matches: fully-cited CG-concrete bodies, no rough-in placeholders, no speculative L_{n+1} sketch. The status reasoning (firm-on-positive-structure escape) is stated and correct.

**skill-uptake-survey — pass.** The report's shape (Phase-1 slice reduction prep + absorption) implies the `phase-1-slice-reduction-audit` skill; the report correctly scopes that the actual delete + SUMMARY repoint is D2's job (not this dispatch) and does the concept-page-grep non-duplication check the skill prescribes. citecheck `--anchor` usage is referenced (CYCLE.md:54-62). Telemetry only; no blocking.

### Issues found

**Issue 1 — `ksp-solve-mutation-rotation.md` mischaracterized as "firm" L0 terminal home (it is `rough-in`).** Severity: warning. Location: CYCLE.md §Summary:19, §"firm L0 terminal home" header:46, §Proposed-changes Edit-4 body:174, Open-questions:179, Supporting-evidence:190, and the inserted prose "**L0 ground.**" at the end of Edit 1 (which says "The terminal L0 home is [`ksp-solve-mutation-rotation`]..." without the word "firm", so the *inserted artifact text* is clean — the mischaracterization is in the report's own framing prose, and in the re-anchor rationale). The on-disk `## Status` of `book/src/L1-L0/ksp-solve-mutation-rotation.md` is `rough-in` ("the four sub-pattern recognition rules are sketched"). This does NOT break the rank invariant: the worked example's firm-on-positive-structure basis rests on the *positive C++ source directly* (`iterative.cpp:360-486`, ground truth = rank-firm), and the link to the rough-in dissection chapter is a navigational `reference`-class edge to where that source is mapped, not a `depends-on` rank claim. But the repeated assertion that the home is "firm" is a factual inaccuracy in the report prose that a reader (or the integrator) could propagate. Repair is a one-word correction in the framing prose (drop "firm" or replace with "the L0 terminal home, `iterative.cpp:360-486` ground truth dissected at [rough-in] `ksp-solve-mutation-rotation.md` Sub-pattern B"). The inserted artifact text itself does not carry the error, so the integrated chapter is not poisoned — this is a report-prose / META-honesty warning.

**Issue 2 — Edit-4 re-anchored §Evidence bullet still cites Phase-1 slices `gmres.md:459-471` / `arnoldi_step.md:285-298` as worked-example homes.** Severity: low / informational. Location: these appear in the §Status (line 152, carried forward by Edit 2) and §Evidence (lines 172-173, NOT touched by Edit 4 — Edit 4 only replaces the line-171 CG bullet). Both slices are in-bounds and exist on disk (747 / 302 lines), so the citations are valid *today*. The note is forward-looking: those two slices are themselves Phase-1 corpus on the P2 deletion campaign's path, so the same dangling-pointer problem this dispatch fixes for `cg.md` will recur for them. This is NOT a defect introduced by this dispatch (the lines pre-exist and are out of this dispatch's single-file CG-only scope), and not blocking — flagging only as a campaign-continuity breadcrumb for a future dispatch.

**Issue 3 — historical `cg.md:393-425` OOB pointer retained in two re-anchored locations.** Severity: low / informational. Location: Edit-4 body (CYCLE.md:174) and the §Status (the line-152 region) retain "(Original pre-reduction range was `cg.md:393-425`)". After D2 deletes `cg.md`, this parenthetical points at a deleted file's out-of-range line span. The report frames it as a provenance breadcrumb, which is a legitimate documentary choice (git history is the record), but once the file is gone the pointer resolves to nothing. Not blocking — it is a parenthetical historical note, not a live cross-reference, and `linkcheck2` only errors on missing-file `[link]`s, not on plain-text `file:line` provenance mentions. Flagging for awareness; a repairer may choose to soften it to "(pre-reduction; see git history)".

### Summary

The core absorption is sound: the L0 anchors verify exactly (citecheck `--anchor` clean on the load-bearing pinpoints), the cg.md:27-141 transcription is faithful, the non-duplication-vs-concept-page claim holds (the concept page is abstract-only; the worked example is CG-concrete), the L4 notation follows the strawman, the firm-on-positive-structure escape is correctly applied, and all four edit anchors + re-anchor targets resolve on disk. The two `warning` checks both trace to a single repairable prose inaccuracy (the rough-in L0 home called "firm"); the rank invariant is intact because the firm basis is the positive C++ source, not the rough-in dissection chapter. Issues 2 and 3 are informational campaign-continuity / provenance-staleness notes, not defects of this dispatch.

---

## Repair

### Fixes attempted

- **Finding (Issue 1 — drives both `citation-validity` and `cross-reference-integrity` warnings)**: the report's framing prose repeatedly calls the re-anchor target `book/src/L1-L0/ksp-solve-mutation-rotation.md` the "**firm** L0 terminal home," but its on-disk `## Status` is `rough-in`.
  - **Decision**: repaired.
  - **Action**: corrected the word "firm" wherever it modifies `ksp-solve-mutation-rotation.md` in CYCLE.md. Five sites edited (all framing / report-prose, NOT the inserted artifact text — which the critic confirmed was already clean):
    - frontmatter `inputs:` line (`:10`) — "(firm L0 terminal home: ...)" → "(the (rough-in) L0 terminal home: ...)".
    - §Summary (`:19`) — "the firm L0 terminal (`L1-L0/ksp-solve-mutation-rotation.md` ...)" → "the L0 terminal home (`L1-L0/ksp-solve-mutation-rotation.md` ...)".
    - §"...L0 terminal home" header (`:46`) — "### The firm L0 terminal home (re-anchor target)" → "### The L0 terminal home (re-anchor target; on-disk status `rough-in`)".
    - §Open-questions (`:179`) — "+ the firm L0 terminal (...)" → "+ the L0 terminal home (..., on-disk status `rough-in`)".
    - §Supporting-evidence (`:190`) — "Firm L0 terminal:" → "L0 terminal home (on-disk status `rough-in`):".
  - On-disk status verified directly: `book/src/L1-L0/ksp-solve-mutation-rotation.md:762-766` reads "`rough-in` — the four sub-pattern recognition rules are sketched; ...".
  - The Edit-4 proposed-change body (`:174`) needed no change: its only "firm" applies to `book/src/L2/krylov-step.md` (which IS firm — correct), and its reference to `ksp-solve-mutation-rotation.md` is the unqualified "The L0 ground is the same CG body as Form A: [`ksp-solve-mutation-rotation`](...)" — no "firm" mischaracterization in the artifact text.
  - The two surviving `firm` tokens in the report's reasoning prose (§Summary `:19`, §Open-questions `:183`, §Status proposed-text `:164`) are the **worked-example's own status** under the firm-on-positive-structure escape and the **L2 chapter** — both correct and left untouched.

### Rank-safety verification (per repair-prompt directive)

Confirmed the proposed worked-example subsection introduces **no `depends-on` edge to a rough-in node**, so the new content's rank stays 0 (and the chapter stays `firm` validly):

- `grep` over CYCLE.md for `depends-on` / `depends_on` / `edges:` / `edge:` returns **none** — no proposed change carries a typed-edge frontmatter block. The edits are pure prose + fenced L4 code + inline markdown `[link]`s + plain-text `file:line` citations.
- The link to the rough-in dissection chapter (`[`ksp-solve-mutation-rotation`](../L1-L0/ksp-solve-mutation-rotation.md)`, appearing in inserted Edit-1 prose and Edit-4 body) is a navigational markdown `[link]` — a **`reference`-class** edge (navigational, rank-free, the OWN-COMPOSITION class). It is NOT a `depends-on` rank claim.
- The L0 anchor is the `palace/linalg/iterative.cpp:360-486` (per-step `:427-464`, branch `:434-441`) source citation — a **`cites-evidence`** edge to ground-truth C++ source, which is rank-exempt (the firm-on-positive-structure basis).
- Therefore the worked example's `firm` law-confidence rests on positive source via a rank-exempt evidence edge, and the only edge to the rough-in node is `reference`-class. The rank invariant `rank(u) ≤ min(deps)` is not engaged by any rough-in dependency. No frontmatter fix was needed (none present to fix).

### Informational notes (acknowledged, not edited)

- **Issue 2 (low/informational)**: the re-anchored §Evidence/§Status text still cites Phase-1 slices `gmres.md:459-471` / `arnoldi_step.md:285-298` as plain-text worked-example homes. These are valid on disk today; they become stale-but-harmless plain-text provenance after D2 deletes those slices this cycle. This is the campaign's known plain-text-provenance residue — recorded here for the **batch-31 meta-phase follow-up**; D2 / finalize tracks it. Not fixed here (out of this single-file CG-only dispatch's scope, and not a defect introduced by this dispatch).
- **Issue 3 (low/informational)**: the historical `cg.md:393-425` OOB provenance parenthetical (Edit-4 body `:174`) points at the to-be-deleted slice file. It is explicitly framed as a historical-provenance breadcrumb (the chapter's own `:171`-style convention; git history is the record), and `linkcheck2` errors only on missing-file `[link]`s, not plain-text `file:line` mentions. Acceptable as-is; left untouched.

### Unrepairable findings

None. Both warning-driving findings traced to the single one-word framing inaccuracy, which is squarely mechanical (drop/qualify "firm") and was applied.

## Suggested resolution

`ready`. The firm-framing mischaracterization is corrected at all five report-prose sites; the on-disk `rough-in` status is now reflected accurately. Rank-safety is confirmed: the proposed changes carry no `depends-on` edge to the rough-in node (the link is `reference`-class; the L0 anchor is a rank-exempt `cites-evidence` edge), so the absorbed worked example's `firm` status and rank 0 are valid. The inserted artifact text was already clean of the error, so nothing in `book/` is affected by this repair (and the repairer touched only CYCLE.md, per the artifact-hands-off constraint). Integrator notes: (a) Issues 2 and 3 are plain-text provenance residue on the P2 slice-deletion campaign's path — D2 deletes `cg.md` this cycle, and the `gmres.md` / `arnoldi_step.md` plain-text pointers are a batch-31 meta-phase follow-up breadcrumb, not a blocker for applying this report.
