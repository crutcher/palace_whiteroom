---
verifies: ../CYCLE.md
critiqued_at: 2026-05-30T230030Z
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
repaired_at: 2026-05-30T231500Z
repairer_version: 1
repairs:
  citation-validity: not-needed
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

# META: verification of "Audit dead-code complex-transpose kernel cohort (jacobi + chebyshev + axpby)"

## Critique

### Checks run

**citation-validity — pass.** I re-ran the load-bearing citations mechanically via `tools/citecheck/citecheck.py --anchor`: `palace/linalg/jacobi.cpp:61-69` with anchor `DIR` resolved at lines [66, 67]; `palace/linalg/chebyshev.cpp:101-110` with anchor `else` resolved at line [102] (matching the report's narrative that line 102 begins the `else` block, with line 101 = the closing brace of the `if (!Transpose)` branch); `palace/linalg/chebyshev.cpp:147-155` with anchor `sd` resolved at lines [152, 153] (the kernel-body lambda lines that the audit identifies as the precise body). I then independently confirmed the three negative-reachability claims via codemap: `search_text("Apply<true>")`, `search_text("ApplyOrder0<true>")`, `search_text("ApplyOrderK<true>")` all returned zero hits; `get_call_sites("Apply")` returned exactly the single site `palace/linalg/jacobi.cpp:103`; `get_call_sites("Subtract")` returned zero sites. I also confirmed `ApplyOrder0` / `ApplyOrderK` are called from `Mult2` at lines 209/216 (`ChebyshevSmoother`) and 279/288 (`ChebyshevSmoother1stKind`) without template args — exactly matching the report. I read `palace/linalg/jacobi.hpp:39-47` and confirmed line 43 is the inline `MultTranspose(...){ Mult(x, y); }` self-alias; `palace/linalg/chebyshev.hpp:68-142` confirms the two `MultTranspose2 → Mult2` aliases at the cited ranges with the `// Assumes operator symmetry` comment. The `verified_against:` YAML round-trips cleanly through `yaml.safe_load` (7 entries, all parsing); no `note:` value begins with a leading quote of either kind.

**surface-or-evidence — pass.** This is a verdict-only negative-finding audit; the report explicitly proposes no surface edits. The verdict (caveats correctly recorded; one planner-scope mischaracterization on `Subtract`; one citation-hygiene observation on `:150-159`) is pure retroactive evidence backfill against existing firm theme caveats. This is the allowed shape per the §Checks "retroactive evidence backfill" carve-out.

**rotation-quality — pass.** Not applicable in the structural-rotation sense (no rotation is proposed). The caveat-fidelity sub-question asked in the dispatch framing — is "correctly recorded as a recognition-rule caveat" accurate for each kernel? — checks out. The jacobi caveat at `:597-604` and the chebyshev caveat at `:371-377` (with sub-pattern C apparatus at `:134-156`) frame both kernels exactly as "defined-not-used / unreachable under symmetric `MultTranspose[2] → Mult[2]` wiring; recognition rules for *potential* non-symmetric sites, not observed ones." That framing matches the verified L0 reality (template branch exists, no template-`<true>` call site exists, the symmetric self-alias is the recognition rule). The audit's distinction between "template-dead `Transpose=true` branch" (jacobi/chebyshev) and "defined-not-used member-API recognition rule" (axpby `Subtract`) is sound and is supported by the axpby theme's text at `book/src/L1-L0/axpby-mutation-rotation.md:215-238` which already frames `Subtract` / `operator-=` / complex-`α` `linalg::AXPY` overload as "defined-not-used recognition rules for *potential* call sites" — exactly the framing the audit defends, and a distinct shape from the jacobi/chebyshev template-dead branches.

**variant-axis-coverage — pass.** Variant axes for the audited cohort: real vs. complex `OperType`; `Transpose=false` vs. `Transpose=true`; in `chebyshev` additionally 4th-kind vs. 1st-kind `ChebyshevSmoother` / `ChebyshevSmoother1stKind`, and `ApplyOrder0` vs. `ApplyOrderK`. The audit covers all combinations explicitly: jacobi's two `OperType` instantiations (`palace/linalg/jacobi.cpp:67-68`, cited in the supporting-evidence list); chebyshev's 4th-kind and 1st-kind `Mult2` both showing template-arg-omitted call sites at four distinct lines (209/216 and 279/288); both `MultTranspose2` aliases (`chebyshev.hpp:73-76` and `:138-141`). No hidden branches.

**cross-reference-integrity — warning.** Substantive cross-refs are all good — the cited theme line ranges (`jacobi-smoother-mutation-rotation.md:597-604`, `chebyshev-smoother-mutation-rotation.md:134-156, 371-377`, `axpby-mutation-rotation.md:215-238`) resolve to the exact caveat text the report claims they contain. The `verified_against:` YAML block is fenced ` ```yaml` (line 119) and uses full-path citations throughout. **Warning:** `tools/citecheck/citecheck.py --scan` flagged 4 path-hygiene MISSes in the report's prose: `cheb.hpp:73-76`, `cheb.hpp:138-141`, `cheb.cpp:209`, `cheb.cpp:279` (in the "Reachability check" bullets at lines 67, 75-76, and the supporting-evidence list). These are informal shorthand for `palace/linalg/chebyshev.{cpp,hpp}` — the full paths ARE used elsewhere in the same report (lines 13-17, 67 same paragraph) so this is path-hygiene inconsistency in the prose, not a citation-correctness failure. The actual referenced line numbers (73-76, 138-141, 209, 279) are all confirmed correct against the full-path `chebyshev.{cpp,hpp}` files. Surfaced as `warning` because the shorthand is non-canonical in a citation-grounded artifact and would fail `--scan` on the report; not blocking the verdict.

**edge-label-fidelity — pass.** No edge label asserted; the audit is scoped to L1>L0 themes the artifact already carries and discusses each at its own layer label (jacobi/chebyshev L1>L0 themes, axpby L1>L0 theme).

**plan-kind-consistency — pass.** Verdict-only no-proposed-changes shape with a `verified_against:` block recording per-citation verdicts (`supports` / `supports-with-citation-hygiene-note` / `does-not-support-planner-mischaracterization`) is the correct shape for a lowering-verifier audit. The frontmatter `status: pending` (line 5) is the standard pre-critique state. The one new OQ filing (`chebyshev-smoother-mutation-rotation-applyorderk-true-citation-tighten`) and the OQ closure routing for `jacobi-mutation-rotation-dead-code-complex-transpose-kernel-lowering-verifier-audit` are both appropriate dispositions for a hygiene-only follow-up and a resolved audit OQ respectively (confirmed by `scaffolding/open-questions.md:485, :489, :831` — the ledger already reflects these dispositions, indicating the report's stated routing is real).

**skill-uptake-survey — pass.** The report explicitly references the `establish-negative-finding-exhaustiveness` skill at line 51 with all four sub-checks itemized (stated terms / broadened sweep / residual token accounting / positive-API confirmation). The `verify-citation-range` skill's mechanical realization is invoked at lines 169-172 (three `tools/citecheck/citecheck.py --anchor` runs). Both invocations are documented inline.

### Negative-finding exhaustiveness sub-audit

The audit meets the `establish-negative-finding-exhaustiveness` bar:
- **Stated terms searched** — `Apply<true>`, `ApplyOrder0<true>`, `ApplyOrderK<true>`, `\.Subtract\s*\(`; I re-ran the first three via codemap `search_text` and confirmed zero hits.
- **Broadened sweep** — `get_call_sites("Apply")` returned exactly one site (`jacobi.cpp:103`) and `get_call_sites("Subtract")` returned empty; this is the call-site name-matching broadened sweep beyond literal-pattern search.
- **Residual token accounting** — the audit identifies the only candidate consumer surface (`JacobiSmoother::Mult` / `MultTranspose`, the two `Mult2` / `MultTranspose2` pairs) and walks each through the template-arg-omitted call site that defaults `Transpose=false`. Anonymous-namespace TU-local scoping is invoked correctly to rule out external linkage.
- **Positive-API confirmation** — the live forward (non-transpose) paths are exhibited at the matching call sites (`Apply<false>` reachable, `ApplyOrder0<false>` / `ApplyOrderK<false>` reachable via `Mult2`).

### Issues found

- **(low / cross-reference-integrity)** `reports/2026-05-30T220500Z-lowering-verifier-dead-code-complex-transpose-kernel-audit/CYCLE.md:67, 75-76, 156-162` — informal `cheb.cpp` / `cheb.hpp` shorthand in narrative prose (e.g. "cheb.hpp:73-76", "cheb.hpp:138-141", "cheb.cpp:209", "cheb.cpp:279") for files whose full paths are `palace/linalg/chebyshev.{cpp,hpp}`. The full paths ARE used elsewhere in the same report (frontmatter inputs, sub-pattern audit bullets), and the `verified_against:` block at lines 119-148 uses full paths consistently — so this is a prose-hygiene inconsistency, not a citation-correctness defect. The line numbers themselves (73-76, 138-141, 209, 279) are all confirmed correct against the canonical files. `citecheck.py --scan` flags these as `[MISS]` because the shorthand `cheb.hpp` / `cheb.cpp` does not resolve under any `reference/` root. Severity low (hygiene-only; the verdict's correctness is unaffected); the repairer may wish to rewrite the shorthand to full paths.

- **(very-low / cross-reference-integrity, INFORMATIONAL)** `reports/2026-05-30T220500Z-lowering-verifier-dead-code-complex-transpose-kernel-audit/CYCLE.md:35, 116, 184` — The audit's main observation is itself a citation-hygiene one (`:150-159` overshoots; precise body is `:147-155`). I confirmed via `read_range chebyshev.cpp:145-160` that line 147 = `else`, 148 = `{`, 149-154 = body, 155 = `}` (closes `else`), 156 = `}` (closes function), 158 = `}  // namespace` — matching the audit's claim exactly. This is the audit FINDING, not a defect IN the audit; surfaced here only as informational verification that the audit's primary novel claim is accurate.

- **(no issue / verified)** The verdict-only no-proposed-changes shape, the `partial-mischaracterization` framing for the `Subtract` axpby planner-scope conflation, the new OQ filing for citation-tightening, and the resolved-routing for the motivating OQ are all consistent with `scaffolding/open-questions.md:485, :489, :831` and the audited themes' own text. The audit can stand as-is verdict-wise; the one path-hygiene warning is the sole repair candidate.

## Repair

### Fixes attempted

- **Finding**: (low / cross-reference-integrity) informal `cheb.cpp` / `cheb.hpp` shorthand in narrative prose triggers 4 `[MISS]` entries from `tools/citecheck/citecheck.py --scan` (`cheb.hpp:73-76`, `cheb.hpp:138-141`, `cheb.cpp:209`, `cheb.cpp:279`); full paths and line numbers are correct elsewhere in the report, this is path-hygiene only.
  - **Decision**: repaired.
  - **Action**: rewrote the shorthand to full reference-relative paths (`palace/linalg/chebyshev.cpp` / `palace/linalg/chebyshev.hpp`) at the 4 narrative-prose spots flagged by citecheck:
    - CYCLE.md:35 — "(cheb.hpp:73-76)" / "(cheb.hpp:138-141)" → "(palace/linalg/chebyshev.hpp:73-76)" / "(palace/linalg/chebyshev.hpp:138-141)" (Summary bullet 2).
    - CYCLE.md:67 — `cheb.hpp:73-76` / `cheb.hpp:138-141` → `palace/linalg/chebyshev.hpp:73-76` / `palace/linalg/chebyshev.hpp:138-141` (chebyshev reachability check).
    - CYCLE.md:100-101 — `cheb.hpp:73-76; cheb.hpp:138-141` and `cheb.cpp:209, :216 ... cheb.cpp:279, :288` → full `palace/linalg/...` form (Applicability conditions 1 and 2). Also normalized `jacobi.hpp:43` and `jacobi.cpp:103` in the same prose lines to `palace/linalg/jacobi.hpp:43` and `palace/linalg/jacobi.cpp:103` for consistency with surrounding text.
    - CYCLE.md:132 — `cheb hpp:73-76` (space-form variant inside the `verified_against:` YAML note for `chebyshev.cpp:101-110`) → `palace/linalg/chebyshev.hpp:73-76` for consistency, even though citecheck did not flag this form (the space breaks the path-token regex).
  - **Verification**: re-ran `python3 tools/citecheck/citecheck.py --scan reports/2026-05-30T220500Z-lowering-verifier-dead-code-complex-transpose-kernel-audit/CYCLE.md` → `36 ok, 0 failing (36 citations checked)`. All four prior `[MISS]` entries (`cheb.hpp:73-76`, `cheb.hpp:138-141`, `cheb.cpp:209`, `cheb.cpp:279`) have cleared. No line numbers were changed (the critic confirmed they are correct against the canonical `chebyshev.{cpp,hpp}` files).
  - **Rationale**: this is a path-hygiene fix within repair authority — the full paths were already correct elsewhere in the same report (frontmatter inputs, the `verified_against:` YAML block, the supporting-evidence list), the underlying line numbers were independently confirmed by the critic, and the rewrite is mechanical text substitution with no content authoring.

- **Finding**: (very-low / cross-reference-integrity, INFORMATIONAL) `:150-159` overshoots; precise body is `:147-155` (the audit's own primary novel claim — recorded only as informational verification by the critic, not an issue IN the audit).
  - **Decision**: not-needed.
  - **Rationale**: this is the audit's main finding, not a defect in the audit. The critic explicitly framed it as `INFORMATIONAL` and `not an issue` — the audit's report stands as the canonical record of this hygiene observation, and a future hygiene-pass dispatch on `book/src/L1-L0/chebyshev-smoother-mutation-rotation.md` (tracked as OQ `chebyshev-smoother-mutation-rotation-applyorderk-true-citation-tighten`) is the routed follow-up. Nothing for the repairer to fix.

### Unrepairable findings

None.

## Suggested resolution

`overall_status: ready`. The verdict-only audit's content is unchanged (the critic confirmed citation-validity, surface-or-evidence, rotation-quality, variant-axis-coverage, edge-label-fidelity, plan-kind-consistency, and skill-uptake-survey all pass; line numbers are all correct); only the prose-hygiene `cheb.{cpp,hpp}` shorthand was rewritten to canonical full reference-relative paths, and `citecheck --scan` now reports zero failing citations.

Notes for the integrator:
- This is a verdict-only audit with no `book/` proposed-changes, so `integrator-per-report` has no artifact edits to apply.
- The audit's recorded outcomes (OQ closure for `jacobi-mutation-rotation-dead-code-complex-transpose-kernel-lowering-verifier-audit`; new OQ filing for `chebyshev-smoother-mutation-rotation-applyorderk-true-citation-tighten`; planner-scope-precision callout for the cycle-034 batch's eventual meta-phase) should be routed as the audit itself describes — see CYCLE.md "Open questions / caveats" section.
- The `verified_against:` YAML block at CYCLE.md:119-149 may be optionally appended to the respective theme files' running `verified_against:` blocks per the audit's own §Proposed changes recommendation; that is an integrator-judgement call (the audit explicitly does not emit a proposed-changes `edit:` block).
