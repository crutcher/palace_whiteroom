---
verifies: ../REPORT.md
critiqued_at: 2026-06-07T23:38:17Z
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

# META: verification of "Refresh stale `cg_solve` worked-example call form at L4 krylov-step"

## Critique

### Checks run

**citation-validity — pass.** `citecheck --scan` reports 11 ok / 1 "failing", but the single non-ok is an `[AMBIG]` on the bare-basename prose reference `krylov-step.md:192-197` (basename matches L2/L3/L4) — a path-hygiene lint, NOT a bounds/anchor error; the proposed-changes block, the `inputs:` frontmatter, and every load-bearing pinpoint use the full `book/src/L4/krylov-step.md` path. All five load-bearing pinpoints anchor-clear via `--anchor`: `book/src/L4/krylov-step.md:192-197` (anchor `iterate_while_with_prev s1 s0.beta` at 193), `iterate-while-with-prev.md:44-49` (anchor `bootstrap_step` at 45), `iterate-while-with-prev.md:52` (anchor `bootstrap_step\` first` at 52), `synthesis/iteration.md:291-297` (anchor at 291), `iterate-while-with-prev.md:233` (anchor `prototypical use` at 233). No `verified_against:` YAML block in this report (harvester, not lowering-verifier), so that sub-check no-ops.

**surface-or-evidence — pass.** This is a refinement-shaped change to an existing operator chapter that modifies surface (the `cg_solve` worked-example code block) AND carries fidelity evidence: the NEW form is anchored to the authoritative `iterate_while_with_prev` signature at `iterate-while-with-prev.md:44-49,52` and cross-checked against the c137-audited-faithful synthesis rendering at `synthesis/iteration.md:291-297`. No new record is named in a signature by this edit (the `cg_solve` signature line at `:180-181` is untouched; `CgState`/`CgConfig` already have definition homes), so the record-definition sub-check finds nothing to flag.

**rotation-quality — pass.** The proposal asserts NO new rotation; it is a call-form spelling refresh of an existing, already-firm Form-B rotation (the v0.5 first-iteration-unrolled CG solve). I verified the NEW form is identity-in-semantics to the OLD: same `s1`/`s0.beta` seeding, same `cg_steady_step opA eps beta_prev s` body, same predicate, same `residual_norm` threaded into the trajectory. The change is exactly the call-shape (bootstrap added as 1st arg; canonical boot/init/steady/cont order; bare-tuple `(r, s.beta)` step-return replaced by the record `{ state, prev, residual_norm }`). No algebra was altered — confirmed by direct comparison of OLD (`krylov-step.md:192-197`) vs NEW vs the synthesis rendering (`iteration.md:290-297`), which are field-for-field consistent.

**variant-axis-coverage — pass.** No variant axes are introduced or touched. The Form-A↔Form-B equivalence discussion (`krylov-step.md:201-203`) is untouched; this is a single-block within-body fix. Not applicable to a worked-example refresh.

**cross-reference-integrity — pass.** No `[link]` or slug changes. The report correctly asserts no dep-map (`book/src/L4/index.md`) edit and no `SUMMARY.md` edit are needed — `krylov-step` stays `firm`, no edge/status/cohort change. The OLD block was verified verbatim against the on-disk `book/src/L4/krylov-step.md:192-197` (exact match, including the trailing `in` and the `(r, s.beta)) in` close), so the edit will apply. Build-readiness guard: the firm-claim here is pre-existing (no firm body authored outside a fence) — the edit only swaps an indented code block already inside the existing ` ```text ` fence at `:178-199`, so the fence-truncation defect cannot apply.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried; this is an in-layer L4 chapter fidelity fix. Not applicable.

**plan-kind-consistency — pass.** Declared shape is a surgical mechanical fidelity fix (harvester, one operator). The content matches: a single `[old]→[new]` proposed-changes block, no status promotion, no new claims, explicit "no dep-map / no SUMMARY edit." Consistent with a `firm`-stays-`firm` within-body refresh.

**skill-uptake-survey — pass.** The report's verification leans on direct on-disk reads of the authoritative signature and the synthesis rendering, which is the appropriate procedure here; no obviously-matching skill is unreferenced. Telemetry only — non-blocking.

### Issues found

No blocking or warning issues. Two observations, neither a defect:

1. **(Non-blocking, path-hygiene)** The prose at the report's "The defect" section (`CYCLE.md:30`) references `krylov-step.md:192-197` by bare basename, which `citecheck` flags `[AMBIG]` (matches L2/L3/L4). The authoritative locations (frontmatter inputs, proposed-changes block) all use the full `book/src/L4/...` path, so the edit is unambiguous and applies correctly; this is cosmetic only.

2. **(Correctly handled, not an issue)** The secondary stale occurrence at `book/src/L4/iterate-while-with-prev.md:233` (the §Evidence "prototypical use" prose still spelling the old positional+tuple form `iterate_while_with_prev s1 s0.beta (\(s, _) -> ...) (\(s, beta_prev) -> ...)`) is genuinely stale (verified on-disk at `:233`) and is correctly routed to OQ `iterate-while-with-prev-evidence-prose-stale-cg-call-shape` for a follow-up dispatch rather than fixed out-of-scope, per the one-operator-per-invocation discipline. This is the right disposition.
