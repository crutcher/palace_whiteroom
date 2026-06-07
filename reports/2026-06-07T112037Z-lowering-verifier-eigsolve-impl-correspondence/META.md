---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T123000Z
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
overall_status: ready
---

# META: verification of "Audit eigsolve-impl correspondence + nleps-deflated-eigensolve consumer faithfulness" (D2)

## Critique

### Checks run

- **citation-validity — pass.** `citecheck --scan` reports 10 ok, 3 nominal failures, all benign: two are bare `CYCLE.md:121` / `CYCLE.md:31` *report-to-report* self-references (cycle-planner provenance pointers, not source citations), and one is an `[AMBIG] eigsolve.md:104` basename collision that resolves unambiguously to `book/src/L3/eigsolve.md` by context. Every load-bearing Palace pinpoint was anchor-confirmed on disk: `nleps.cpp:470-474` (`AXPBYPCZ` @471), `:524-531` (`Dot` @529), `:505-537` (`deflated_solve` @505), `:356-359` (`Effenberger` @357), `:613-619` (`X.resize` @614), `:515-518` (`k == 0` @515) — all `[ok]`. The `verified_against:` YAML round-trip sub-check is the load-bearing check for this report-kind: BOTH proposed blocks (A, the fresh block for the consumer chapter; B, the single inserted list entry for `eigsolve-impl.md`) `yaml.safe_load`-clean with no leading-quote scalar fault. No drift to carry.
- **surface-or-evidence — pass (audit-kind, retroactive-evidence backfill).** This report authors NO operator/theme surface; it proposes two `verified_against:` evidence blocks — the canonical pure-retroactive-evidence-backfill shape, which the role-spec explicitly allows. No record is named in any signature (no record-definition sub-check triggered).
- **rotation-quality — pass (not applicable to audit-kind).** No algebraic/structural rotation is asserted; the report audits an existing impl↔api correspondence and consumer edge faithfulness. No-op.
- **variant-axis-coverage — pass (not applicable to audit-kind).** No new operator/theme with variant axes is authored. No-op.
- **cross-reference-integrity — pass.** The on-disk edge block of `book/src/L3/eigsolve-impl.md:19-23` confirms the audit's central claim: both `realizes-kernel-api` edges (→ `L3/eigsolve` at lines 20-21, → `L4/eigsolve` at lines 22-23) sit under the `reference:` block, NOT `depends-on:` — matching block (A)/(B)'s line claims exactly. The kernel-api `book/src/L3/eigsolve.md` is confirmed `partial-obstruction` / role `kernel-api` on disk (`:4`, `:191`). The existing `verified_against:` block in `eigsolve-impl.md` spans `:161-191` with the last `arpack.cpp:369` note at `:190` and the closing fence at `:191` — exactly matching block (B)'s insertion instruction (insert after `:190`, before `:191`). The consumer chapter `book/src/L3/nleps-deflated-eigensolve.md` is correctly NOT yet on disk — it is D1's proposed `new:` chapter; block (A)'s `edit:` is sequenced to append AFTER the integrator applies D1, which the report states explicitly.
- **edge-label-fidelity — pass.** No L_{n+1}→L_n lowering edge label is carried; the edges under audit are `realizes-kernel-api` (reference-class) and `depends-on` (composes), and the prose discusses exactly those.
- **plan-kind-consistency — pass.** Declared kind is `lowering-verifier` audit (`status: pending`, `verdict: fully-supported`); content is per-citation audit + `verified_against:` proposals with no theme-content edits and no status flip. Shape matches the audit kind. The D2-contingency narrowing (D1 left `eigsolve-impl` at `roadmap_goal`, so no firm correspondence-promotion to audit) is correctly handled — no over-claim: the report does NOT promote anything and explicitly preserves `roadmap_goal` and the `partial-obstruction` API.
- **skill-uptake-survey — pass.** The report references its tooling uptake explicitly (Supporting evidence cites `tools/citecheck/citecheck.py --anchor` runs and the `yaml.safe_load` round-trip on both proposed blocks) — appropriate for an audit-kind report.

### Issues found

No blocking issues. One minor (non-load-bearing) prose-imprecision, recorded for telemetry only:

- **`reports/.../CYCLE.md` §(2b) / §Algebraic-laws — Schur back-projection sub-range undercount by one line.** The prose variably cites the deflate back-projection as `:532-535` (e.g. §2b "the Schur form deflation projection (`:532-535`)") and `:532-536` (the `## Per-citation` body). On disk `:532` is the Schur `S = eig_opInv*I − H`, `:533-535` is `SS = -S⁻¹(...)` / `x2 = SS⁻¹·x2` / `XSx2 = MatVecMult(...)`, and `:536` is the `AXPY(-1, XSx2, x1)` back-subtraction — so the full deflate span is `:532-536`; the `:532-535` form omits the `:536` AXPY line. This is NOT a drift finding: the load-bearing proposed `verified_against:` citation (block A, entry 1) uses the enclosing range `:505-537`, which is in-range and anchor-`[ok]`, and the §2b body itself elsewhere uses the correct `:532-536`. Severity: cosmetic; the audit verdict and all proposed blocks are unaffected.

All 8 checks pass; `overall_status: ready` set (clean report, no repairer will run).
