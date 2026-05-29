---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T16:05:00Z
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
repaired_at: 2026-05-29T16:25:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: repaired
overall_status: ready
follow_up_agent: null
---

# META: verification of "Audit deflate-composition-lowering"

## Critique

### Checks run

**citation-validity — pass (LOAD-BEARING, independently re-run).** Ran `tools/citecheck/citecheck.py --scan` on the CYCLE.md: **40 ok, 1 failing** — the single "failing" is `[AMBIG] dot.md:43` (a bare-basename matching `book/src/{L1,L3}/dot.md` + `book/src/concepts/dot.md`). That ambiguity fires only on a prose back-reference shorthand at CYCLE.md:248 (`dot.md:43`); the load-bearing occurrences (inputs line 14, the audit body at :187, the proposed-changes `verified_against` entry at :369, and supporting-evidence at :413) are all fully-pathed `book/src/L1/dot.md:43` and resolve cleanly. So the AMBIG is a cosmetic prose-shorthand, not a bounds or resolution failure. All 9 decisive pinpoints were `--anchor`-checked against `reference/palace/` (resolved path `reference/palace/palace/linalg/nleps.cpp`, file = 952 lines as the report states): `:522` (`x2(j) = b2(j) - linalg::Dot`), `:529` (`SS(i, j) = linalg::Dot`), `:532` (regex `eig_opInv \* …Identity`), `:533` (`SS = -S.fullPivLu().solve(SS)`), `:534` (`x2 = SS.fullPivLu().solve(x2)`), `:535` (`XSx2 = MatVecMult`), `:536` (`linalg::AXPY(-1.0, XSx2, x1)`), `:329` (`ComplexVector MatVecMult`), `:614` (`X.resize(k + 1)`) — **all anchor-at-exact-line, zero drift**. The Schur comment `:512-513`, the lambda boundaries `:505`/`:537`, and the no-orthonormalization precondition `:609-615` (only `v *= 1.0/scale` at :610-611) all match the report verbatim. The sibling-noted codemap +1 drift at `:659+` does not touch any audited line (all ≤ :667 but the decisive ones are ≤ :614, and even `:664-667` verified exact on-disk); the report's "citecheck/on-disk is authoritative" framing is correct and the on-disk read confirms zero drift. **The load-bearing citation claim holds.**

**surface-or-evidence — pass.** This is a pure-audit (retroactive-evidence-backfill) report: the proposed change is an additive `verified_against:`/`gate_verdict:` metadata block appended to the theme; the `## Status` line and all body sections are explicitly left unchanged. No surface modification + no rotation_claim is made, so the refinement-shaped-proposal branch does not apply. Retroactive evidence framing is explicit ("I AUDIT only — I did not mutate the theme"). Allowed.

**rotation-quality — pass (not applicable / inherited).** This is an audit of an existing L2>L1 fan-down theme, not a fresh rotation proposal. The report does not assert a new rotation; it verifies the existing `coords ▷ (schur-)solve ▷ back-project` fan-down against L0. The fan-down's rotation-quality was adjudicated at the theme's landing (cycle-024); this audit only confirms per-line fidelity. No 1:1 renaming masquerading as a rotation is introduced.

**variant-axis-coverage — pass.** The theme's variant axis (`op.block ∈ {Galerkin, Schur}`) is the central object of the audit, and the report handles it explicitly: the Schur form is positively-sourced and verified per-line; the Galerkin (`S = I`) core is correctly held `partly-constructive` and is the subject of the gate verdict. The orthonormal-vs-oblique axis is also covered (the no-orthonormalization precondition at :609-615 is verified, establishing why Stage 3's `lu_solve` is load-bearing). No hidden branch — the report enumerates exactly the source's variants.

**cross-reference-integrity — pass.** Every book-internal reference resolves and is in-bounds: `book/src/L2/deflate.md` (502 lines; `:343-348`, `:386-391` both carry the negative anchor verbatim; Status `:362-415` valid — `:362` = `## Status`); `book/src/L1/lu_solve.md` (107 lines; `:45`, `:58`, `:59` confirmed — law 4 / law 5 / invertibility text matches, and `:45` independently names `Ar` "a ROM matrix", corroborating the gate finding); `book/src/L1/dot.md` (119 lines; `:43` is the conjugation convention as quoted); the theme file `book/src/L2-L1/deflate-composition-lowering.md` exists (341 lines) and is `partly-constructive`. The firm-body-inside-fence build-readiness guard does not apply — this report makes no `firm`-chapter claim; it is an audit producing additive metadata, and the proposed-changes block is a metadata-only YAML append (not a chapter body). The single nested-fence in the proposed-changes block (` ```edit ` wrapping ` ```yaml `) is documented inline by the report (CYCLE.md:395-397) and is a known integrator pattern; fence parity is balanced.

**edge-label-fidelity — pass.** The report's edge is L2>L1 (the theme's declared edge). All prose narrates the L2-composition-to-L1-leaf fan-down (the `deflate` L2 composition down into `dot`/`gram`/`lu_solve`/`linear_combination`/`axpy` leaves). No edge-label/prose mismatch. Upward/downward references to L0 source (nleps.cpp) and to the shared L1>L0 sibling (`nleps-deflated-solve-mutation-rotation`) are correctly characterized as the gate-sharing relationship, not as the theme's own edge.

**plan-kind-consistency — pass.** Declared kind is `audit` (lowering-verifier dispatch). Content shape matches: per-citation verdicts (all `supports`), an applicability-conditions table, a cited-laws section, a gate-verdict section, and an additive `verified_against:` proposal. The report correctly does NOT enact a promotion (out of lowering-verifier role) and does NOT claim to UNBLOCK (no positive site found) — it audits and recommends. This is exactly the audit shape, no mis-classification.

**skill-uptake-survey — warning (telemetry, non-blocking).** The report's shape implies two relevant skills. (1) `verify-citation-range` (cycle-024 mechanical `tools/citecheck/ --anchor`/`--scan` realization) — the report demonstrably USES the tool (every decisive line carries an explicit `citecheck --anchor → line N, zero drift` annotation) but does not name the skill by slug. (2) `partly-constructive-promotion-checklist` (cycle-015) — the report's gate-verdict reasoning references "the partly-constructive promotion checklist" via the theme's own prose but does not state it invoked the skill for its own gate assessment. This is a pure presence-survey miss (the procedures were clearly followed); flagging as telemetry only.

### Issues found

1. **(cosmetic, citation-validity) Prose-shorthand bare basename `dot.md:43`** — CYCLE.md:248. The `--scan` AMBIG flag fires here because the reference is written `dot.md:43` instead of the fully-pathed `book/src/L1/dot.md:43` used everywhere else in the report. Disambiguated by every other occurrence (:14, :187, :369, :413), so resolution is not in doubt — but the bare form is the one line that trips the mechanical scanner. Severity: trivial. Candidate one-token repair (prefix the path).

2. **(low, skill-uptake-survey) Skill slugs not named** — Summary (CYCLE.md:26-28) and Gate-verdict (CYCLE.md:253-292). The report uses `tools/citecheck/` and follows the partly-constructive promotion-checklist logic but does not cite `verify-citation-range` or `partly-constructive-promotion-checklist` by slug. Pure telemetry; the procedures were enacted. Severity: low.

3. **(none — confirmed sound, recorded for repairer/integrator) Gate-verdict negative-search is independently CORRECT and COMPLETE.** I re-ran the exhaustive search the report claims. `grep -rn 'fullPivLu' …/*.cpp` returns exactly the 6 `nleps.cpp` sites the report lists (`:533,534,535,563,665,667`), all Schur-wrapped (`S = λI − H` / `SS = −S⁻¹(XᴴX)`), none bare-Gram. `grep '\.solve(' …/*.cpp` returns exactly those 6 + the 3 `romoperator.cpp` sites (`:757,758,765`) and nothing else. `grep '\.inverse()'` returns only `geodata_impl.cpp:555` (3×3 geometry). LDLT/QR factor sites are only the 3 `romoperator.cpp` lines. The near-candidate is verified NOT a bare-Gram solve: `romoperator.cpp:74` = `Ar = Vᴴ A V` (exact), `:729-734` builds `Ar += Kr; Ar += iω·Cr; Ar += −ω²·Mr` (exact = the reduced operator pencil), and `:754` `if constexpr (false)` confirms the LDLT path `:757-758` is dead with the active solve at `:765` `Ar.fullPivHouseholderQr().solve(RHSr)` — a reduced-system solve, NOT a Gram `(XᴴX)⁻¹` solve. The "STAYS-GATED-correctly / NLEPS-scoped-acceptable" verdict is evidentially sound, and the report correctly does NOT claim to unblock or enact. No issue — recorded so the repairer/integrator can rely on the gate verdict.

4. **(none — confirmed sound) Additive-metadata scope is correct.** The proposed change appends `verified_against:`/`gate_verdict:` at EOF (after line 341); the `## Status` section (theme `:27`, `partly-constructive` inherited at `:12`) is not in the append region and is left unchanged. No `verified_against:` block pre-exists. Scope is exactly additive-metadata. No issue.

5. **(none — confirmed justified) OQ re-scope recommendation is well-founded.** The named OQ `deflate-composition-lowering-mutation-rotation-lowering-verifier-audit-followup` exists in `scaffolding/open-questions.md:327`, migrated-to-plan as a batch-6-firm-theme lowering-verifier audit — exactly the work performed. The audit half is genuinely discharged (per-line zero-drift + gate re-confirmed complete). The recommended re-scope to "promotion-watch" aligns with the already-deferred-contingent plan item `deflate-galerkin-core-promotion` (open-questions.md:35). The report only RECOMMENDS the re-scope (it does not write the ledger — correct for a lowering-verifier). No issue.

---

## Repair

### Fixes attempted

- **Finding (issue 1, cosmetic / citation-validity)**: bare-basename prose shorthand `dot.md:43` at CYCLE.md:248 trips the citecheck `--scan` AMBIG flag (matches `book/src/{L1,L3}/dot.md` + `book/src/concepts/dot.md`).
  - **Decision**: repaired.
  - **Action**: prefixed the token to the full path `book/src/L1/dot.md:43` in the algebraic-laws "Law (conjugation)" bullet (CYCLE.md §Algebraic laws). The fully-pathed form matches every other occurrence in the report (:14, :187, :369, :413). Re-ran `tools/citecheck/citecheck.py --scan` on the CYCLE.md: result went from `40 ok, 1 failing` (the `[AMBIG] dot.md:43`) to **`40 ok, 0 failing`** — the AMBIG is gone. The remaining bare basenames (`lu_solve.md`, `deflate.md`) resolve uniquely and never tripped AMBIG. This silences the spurious AMBIG so the integrator-per-report citecheck `--scan` gate passes clean.

- **Finding (issue 2, low / skill-uptake-survey)**: report follows `verify-citation-range` and `partly-constructive-promotion-checklist` procedures but does not name either skill by slug (telemetry-only, non-blocking).
  - **Decision**: repaired.
  - **Action**: added a one-line **Skill uptake** note to CYCLE.md §Summary (after "I AUDIT only…") naming both slugs and citing where each was enacted — `verify-citation-range` (the per-line `citecheck --anchor → line N, zero drift` annotations) and `partly-constructive-promotion-checklist` (the gate-verdict assessment of the constructive Galerkin-core sub-part against its named promotion condition). Re-ran `--scan` after the edit: still `40 ok, 0 failing` (no new bare tokens introduced). The procedures were demonstrably followed; this is a presence-survey note only, surface/content unchanged.

- **Finding (frontmatter check)**: `verifies:` frontmatter pointer.
  - **Decision**: not-needed.
  - **Rationale**: META.md frontmatter already reads `verifies: ../CYCLE.md` (line 2) — no stale `../REPORT.md` reference present, so no fix required.

### Unrepairable findings

None. The two flagged issues (one cosmetic AMBIG, one telemetry-only skill-survey note) are both mechanical/surgical and were repaired. Critic issues 3/4/5 are explicitly "none — confirmed sound" (gate-verdict negative-search independently re-verified complete; additive-metadata scope correct; OQ re-scope justified) and require no action.

## Suggested resolution

`overall_status: ready`. Notes for the integrator:
- The report is a pure-audit, fully-supporting. Its sole proposed change is the additive `verified_against:`/`gate_verdict:` YAML metadata block appended at EOF of `book/src/L2-L1/deflate-composition-lowering.md` — the `## Status` line stays `partly-constructive` (correctly held; gate did not unblock). The proposed-changes block uses a documented nested-fence pattern (` ```edit ` wrapping ` ```yaml `, fence parity balanced per critic's cross-reference-integrity check).
- Gate verdict **STAYS-GATED-correctly** was independently re-verified by the critic (exhaustive `*.cpp` dense-solve search; `romoperator.cpp:757-765` confirmed a ROM `Ar=VᴴAV` pencil solve, not a bare-Gram `(XᴴX)⁻¹` deflation solve). The integrator can rely on this verdict — no firming edits, no promotion.
- The report RECOMMENDS (does not write) re-scoping OQ `deflate-composition-lowering-mutation-rotation-lowering-verifier-audit-followup` to a pure promotion-watch; the integrator-per-report promotes Open questions per its role.
