---
verifies: ../CYCLE.md
critiqued_at: 2026-05-31T15:30:00Z
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
repaired_at: 2026-05-31T15:45:00Z
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

# META: verification of CYCLE.md — L1>L0 CG initial-residual quirk annotation

## Critique

### Checks run

**citation-validity — pass.** I re-ran the mechanical citecheck on the load-bearing pinpoints (`iterative.cpp:398-411` anchor `initial_guess`, `iterative.cpp:404-404` anchor `Dot`, `iterative.cpp:408-408` anchor `Norml2`, `iterative.cpp:411-411` anchor `initial_res`, `vector.hpp:257-260` anchor `Norml2`) — all five OK with anchor found in-range. Full-report scan: 26 ok / 0 failing. I then independently semantically-verified the chain on-disk: (a) `iterative.cpp:401-405` is the `B` arm with `ApplyB(B, b, p, ...)` followed by `beta_rhs = linalg::Dot(comm, p, b);` — confirmed; (b) `iterative.cpp:406-409` is the `!B` arm `else { beta_rhs = linalg::Norml2(comm, b); }` — confirmed; (c) `iterative.cpp:411` is `initial_res = std::sqrt(std::abs(beta_rhs));` applied uniformly to both arms — confirmed; (d) `vector.hpp:259` body of `Norml2` is `return std::sqrt(std::abs(Dot(comm, x, x)));` — confirmed, internal sqrt is real; (e) the composition therefore yields `initial_res = sqrt(|sqrt(|b·b|)|) = (b·b)^{1/4}` on the `!B && initial_guess` branch — mechanically correct. Cross-check at `iterative.cpp:395-397` (symmetric one-`Dot`-one-`sqrt`: `beta = linalg::Dot(comm, z, r); ... res = std::sqrt(std::abs(beta));`) — confirmed; this is the form the `!B` `initial_res` branch should have mirrored, supporting the "missing inner `Dot` substitution" likely-bug argument. The `CheckDot` helper at `iterative.cpp:21-32` and the GMRES `InitialResidual` helper at `iterative.cpp:252-285` (call site `:566-567`) both match the report's range citations. The `(b·b)^{1/4}` characterization is precisely grounded; no overstatement.

**surface-or-evidence — pass.** The proposal is a refinement-shaped additive Recognition note into a firm L1>L0 theme. It modifies surface (two `edit:` blocks against `book/src/L1-L0/ksp-solve-mutation-rotation.md`) AND is backed by rotation-claim evidence (the asymmetric L0 sites at `iterative.cpp:404` vs `:408`, the shared collapse at `:411`, the `Norml2` definition at `vector.hpp:259`). The annotation does not assert a new law; it adds a recognition-rule caveat about how the existing L1 `initial_res` field reconstructs from L0 in the quirky branch, with citations to every claim. Not pure rotation-claim-without-surface, not pure retroactive backfill — it's a properly evidenced surface annotation.

**rotation-quality — pass.** Not applicable in the strict "algebraic/structural compression" sense: this dispatch is an additive recognition-rule annotation on an already-firm theme, not a new rotation. The theme's existing structural rewrite (L1 `ksp_solve` ↦ L0 mutating Mult body) is untouched. The annotation correctly *documents what L0 does* (faithful reconstruction) rather than asserting what L0 *should* do — the "likely Palace bug" framing is a caveat on the recognition rule's relationship to algorithmic intent, NOT a correctness assertion that rewrites the rotation. The hedging is appropriate: "**likely Palace bug; upstream confirmation pending**" appears in the section header; the narrowed OQ scope ("file an upstream issue / git-blame the asymmetry") is explicit; the bug-fix sketch is marked "informational; we do not propose modifying Palace." Direction is forward L1→L0 throughout.

**variant-axis-coverage — pass.** The four-way axis matrix `(B / !B) × (initial_guess / !initial_guess)` is explicitly enumerated in the annotation prose (lines 95-99 of CYCLE.md): bug does NOT affect `!B && !initial_guess` (line 415 fall-through to `initial_res = res;` where `res = ‖b‖₂` correctly), does NOT affect `B && initial_guess` (`B` arm computes the intended `‖b‖_B`), affects ONLY `!B && initial_guess`. The GMRES analogue (`InitialResidual` at `:252-285`, called at `:566-567`) is correctly identified as a DIFFERENT control-flow region — the new Sub-pattern B note is scoped to `CgSolver<OperType>::Mult` only, and the existing theme's coverage of GMRES warm-vs-cold initial-residual (Sub-pattern C / `:566-567`) is explicitly noted as unaffected. MINRES/BiCGStab are correctly scoped out (per Open-questions caveat 3: those ship as `obstruction (enum-only-stub)` themes per cycle-030 sub-kind codification, so the asymmetry question does not arise at the firm-theme level). No hidden branches.

**cross-reference-integrity — pass.** Fence-parity guard: `grep -n '\`\`\`'` shows 6 fences (3 fenced blocks; even parity, all closed). The two `edit:` blocks target `book/src/L1-L0/ksp-solve-mutation-rotation.md` and enclose their full Recognition-note body + citation rows INSIDE the fence; the inner code samples (the C++ snippets quoting `iterative.cpp:401-405`, `:406-409`, and `vector.hpp:257-260`) are 4-space-indented code blocks WITHIN the markdown content, not nested fences — so the fence count of 6 is correct and no truncation defect is present. The body-firm-inside-fence guard passes: the new Recognition note and the two appended `Citations:` rows are fully enclosed in the `<<<OLD ... ===NEW ... >>>` block. All link references in the annotation (`cg-initial-residual-quirk-palace-bug-flag-lift-path` OQ slug, `mutable-workspace-pattern`, `L1/ksp_solve`) resolve to existing entries. The two new `Citations:` rows are well-formed and follow the theme's existing `\`path:lo-hi\` — prose-description` convention.

**edge-label-fidelity — pass.** The proposal carries no edge-label conflict; it's an L1>L0 annotation and the prose discusses L1→L0 throughout (the L1 `initial_res` field's reconstruction from the L0 `mutable`-member assignment). The edge label and discussion are consistent.

**plan-kind-consistency — pass.** Status `firm` is correctly preserved (additive annotation; no laws change, no signatures change, no operators are added, no status downgrade). The dispatch shape matches its declared kind: an abstractor surgical additive annotation into a firm L1>L0 theme, documented in §"Direction-discipline note" as not a status reduction and as recording a caveat on the recognition rule's relationship to algorithmic intent. The work product is two `edit:` blocks (surgical, OLD/NEW unique) and zero new vocabulary — consistent with an annotation-only dispatch.

**skill-uptake-survey — pass.** The report explicitly invokes `tools/citecheck/citecheck.py` with `--anchor` on all five load-bearing pinpoints and shows the OK output (§Verification, lines 159-175). This is exactly the cycle-024 mechanical realization called out in the critic checklist's citation-validity check, used here by the producer pre-emit. Surveying telemetry: skill uptake is current.

### Issues found

None blocking. One small observation, severity: trivial / informational only:

- **(trivial / informational, §Verification line 177)** — The mechanical verification narrative restates `iterative.cpp:401-405` as `if (B) { ApplyB(B, b, p, this->use_timer); beta_rhs = linalg::Dot(comm, p, b); }` (a one-line collapsed paraphrase of the four-line source span 401-405). This is faithful in *content* (the if-branch body is correct), but the paraphrase elides the `ScalarType beta_rhs;` declaration on line 400 (just outside the cited 401-405 range — declared in the enclosing scope at line 400, then assigned in both arms of the if/else at lines 404 and 408). The annotation in `edit:` (which is the load-bearing output) does NOT make this elision — it correctly cites `iterative.cpp:401-405` for the `B` arm and `:406-409` for the `!B` arm with separate anchor lines. So the elision is in the producer's verification narrative only, and does not propagate into the proposed-changes block. Not a defect of the annotation; just noting it in case the repairer would prefer the narrative match the source more literally. No action required from the integrator.

## Repair

### Fixes attempted

All 8 checks returned `pass` from the critic; no `warning`/`fail` findings to repair. Per-check decisions:

- **Finding**: citation-validity — pass (26 ok / 0 failing, all 5 anchors verified; full chain semantically re-walked).
  - **Decision**: not-needed
- **Finding**: surface-or-evidence — pass (refinement-shaped additive Recognition note with rotation-claim evidence).
  - **Decision**: not-needed
- **Finding**: rotation-quality — pass (additive recognition-rule annotation; hedging on "likely Palace bug" is appropriate).
  - **Decision**: not-needed
- **Finding**: variant-axis-coverage — pass (4-way `(B / !B) × (initial_guess / !initial_guess)` matrix enumerated; sibling KSPs scoped per cycle-030 sub-kind).
  - **Decision**: not-needed
- **Finding**: cross-reference-integrity — pass (fence parity 6/6 even; indented inner C++ snippets ≠ nested fences; all link refs resolve).
  - **Decision**: not-needed
- **Finding**: edge-label-fidelity — pass (L1→L0 direction consistent throughout).
  - **Decision**: not-needed
- **Finding**: plan-kind-consistency — pass (status `firm` preserved; abstractor surgical additive annotation matches kind).
  - **Decision**: not-needed
- **Finding**: skill-uptake-survey — pass (`tools/citecheck/citecheck.py --anchor` invoked on all 5 load-bearing pinpoints pre-emit; cycle-024 mechanical realization current).
  - **Decision**: not-needed

In addition, one trivial narrative polish was applied (NOT addressing any failing check):

- **Finding**: (trivial / informational, §Verification line 177) — narrative paraphrase of `iterative.cpp:401-405` elides the `ScalarType beta_rhs;` declaration on line 400 (outside the cited range).
  - **Decision**: repaired (cosmetic narrative-only; the load-bearing `edit:` block is unchanged).
  - **Action**: appended `(with `ScalarType beta_rhs;` declared on line 400, just above the cited range)` as a parenthetical clause to the §Verification "Semantic pass" sentence in CYCLE.md line 177. The `edit:` block in §Proposed changes is NOT touched (per dispatch instructions and the critic's explicit "Not a defect of the annotation" framing). On-disk source verified (`reference/palace/palace/linalg/iterative.cpp:398-412`): line 400 is indeed `ScalarType beta_rhs;`, line 401 opens `if (B)`, etc. — mechanical and unambiguous.

### Unrepairable findings

None.

## Suggested resolution

`ready` for integrator-per-report. All 8 critic checks pass, the report's proposed `edit:` blocks are fence-parity-clean and surgical, the additive Recognition-note annotation is well-scoped (Sub-pattern B at `book/src/L1-L0/ksp-solve-mutation-rotation.md`), and the OQ-ledger items are clearly demarcated. No follow-up agent required.
