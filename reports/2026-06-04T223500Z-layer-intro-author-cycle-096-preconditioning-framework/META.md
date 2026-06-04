---
verifies: ../CYCLE.md
critiqued_at: 2026-06-04T231500Z
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

# META: verification of L4 preconditioning-framework (D1, cycle-096)

## Critique

### Checks run

**citation-validity — pass.** `citecheck --scan` reports 11 ok / 0 failing (bounds + path-hygiene clean). I disk-verified the load-bearing anchors via `--anchor` and codemap `read_range`, since this is firm-on-first-authoring re-citing L0 directly (citation rigor paramount):
- `palace/linalg/ksp.cpp:276-293` `BaseKspSolver::SetOperators` — `--anchor 'SetOperators'` hits line 277, matching the report's "decl at :277, body :278-293" narrative; `read_range 274-314` confirms the `}` close at 293. The unwrap branch `if (mg_op && !mg_pc) ⇒ pc->SetOperator(mg_op->GetFinestOperator())` is the `:284-287` if-statement (report's claim), `mg_op`/`mg_pc` dynamic_casts at 282-283. Verified on disk.
- `palace/linalg/ksp.cpp:296-310` const `Mult` body — `--anchor 'ksp_mult'` hits 308/309 (`ksp_mult++` / `ksp_mult_it += ...`), matching the report.
- `palace/linalg/ksp.cpp:264-273` direct-injection ctor — `--anchor 'SetPreconditioner'` hits 272 (the bind), matching.
- `palace/linalg/ksp.cpp:25-99` `ConfigureKrylovSolver` (anchor 28) and `:125-235` `ConfigurePreconditionerSolver` (anchor 127) — both verified.
- `palace/linalg/ksp.hpp:30-76` `BaseKspSolver` class, `:40/:41` ksp/pc members, `:46` `ksp_mult,ksp_mult_it` counters — all anchor-verified on disk (hpp:46 `--anchor 'ksp_mult'` hits 46; class body matches the cited `unique_ptr<IterativeSolver> ksp` / `unique_ptr<Solver> pc` / `mutable int ksp_mult, ksp_mult_it` / `SetOperators` decl / `Mult` decl).
No `verified_against:` block present (not a lowering-verifier audit), so that sub-check no-ops. The "Slice provenance" line-ranges (v0.2 "428-485", v0.3 "487-548") differ from the slice header's own numbers ("413–471", "472–533"), but these are absorbed-source breadcrumbs the report explicitly frames as "NOT cited," and the slice header itself flags its line numbers as "pre-insert / section-relative … anchors stable by heading name." The actual `## L4 v0.2` heading is at slice line 428, matching the report's start. Not a citation-validity defect.

**surface-or-evidence — pass.** This is a NEW firm chapter (not a refinement of an existing operator), so the refinement-shaped surface+rotation_claim gate is satisfied by the fact that the chapter authors new surface backed by direct L0 evidence. Record-definition sub-check: the chapter's signatures NAME seven record types (`KspParams` / `PcParams` / `Ksp` / `Pc` / `OpBinding` / `Counters` / `BaseKspSolver`). All have a definition home: the in-chapter `## Record definition` section (lines 120-187) gives the TS shape (fields + types) AND a table with stratum (construction/sim-state/run-time), meaning, and L0 home for each. Single-consumer justification is correct (only this chapter names them in signatures). The record-definition obligation is discharged completely — fields, types, construction-vs-run-time stratum, and L0 backing struct (`palace/linalg/ksp.hpp:30-76`) all present.

**rotation-quality — pass.** The chapter asserts genuine structural rotations, not renaming: (1) build-time vs run-time stratification hides the construction primitives from the monadic body (state hiding); (2) capability-typing brands `TrueOp`/`PcAssemblyOp` make a role-swap a type error the C++ `Operator*` layer cannot catch (strictly more abstract / more equational than the C++ convention); (3) derived-view hoisting of `pcBoundOp` eliminates a stored-vs-bound divergence by computing the unwrap on demand (coarser substitution / compression). Each makes the L4 form more abstract/equational than the L0 C++. Not a 1:1 mapping.

**variant-axis-coverage — pass.** Five variant axes are declared in frontmatter and discussed in §Variant axes (krylov-method, pc-type, multigrid, scalar-field, op-pc_op-coincidence). Each is explicitly accounted for: krylov-method/pc-type/scalar-field absorbed at construction (body-uniform); multigrid drives the `finestLevelUnwrap` branch of `pcBoundOp` (covered, with the L0 `mg_op && !mg_pc` site cited); op-pc_op-coincidence is the explicit `pc_op = op` escape hatch (§Capability typing). No hidden branches.

**cross-reference-integrity — pass.** Verified on disk: `L4/ksp_solve.md` exists and the down-link resolves; all 9 referenced concept pages exist (`state-stratification`, `solve-monad`, `capability-typing`, `derived-view-hoisting`, `constructed-operator-factory`, `finest-level-unwrap`, `complex-from-real-lift`, `variant-absorption`, `solver-as-operator`). The capability-typing.md repoint `[old]` anchors at lines 26 and 55 match the on-disk text exactly; the `[new]` targets `../L4/preconditioning-framework.md` (correct relative path from `concepts/`). The SUMMARY.md `[old]` anchor (lines 72-73: `ksp_solve` then `solve_family`) matches disk; the new row inserts alpha-correctly between them (`ksp_solve` < `preconditioning-framework` < `solve_family`). The L4/index.md `[old]` anchor is the `restart_cycle` row (line 119); the new row inserts immediately before it, between the `Outcome` row (118) and `restart_cycle` (119) — alpha-correct in the "Outer-driver caps & coordination combinators" kind-group (`Outcome` < `preconditioning-framework` < `restart_cycle`: o < p < r). Build-readiness guard: the firm chapter's `## Status` + Signature + Algebraic-laws + Evidence are all INSIDE the section-1 `edit:` fence (opens line 40, closes line 379; `## Status` at 365); 22 fences total = even parity, nested `ts`/`text` fences balanced. No fence-truncation defect. The new chapter file does not yet exist on disk (correct for a new file).

**edge-label-fidelity — pass.** The frontmatter edge `depends-on: L4/ksp_solve (caps-the-binding)` and the L0 `cites-evidence` edge to `ksp.cpp:276-293` are both discussed in the prose exactly (§Context, §Status, §Evidence all narrate the ksp_solve cap relationship and the SetOperators binding). No edge-label/prose mismatch.

**plan-kind-consistency — pass.** Declared kind is firm (`rank: firm`, `firmness: firm`). Content shape matches: complete Signature, Record definition, Capability-typing, Derived-view-hoisting, five Algebraic laws, Variant axes, Evidence, Status. No rough-in placeholders or TODO sub-parts. The firm-on-positive-structure / syntactic-identity escape is correctly invoked (every law is a read-off over positive `BaseKspSolver` source + the firm `ksp_solve` cap; no constructive sub-part rests on a negative anchor). Rank invariant: `rank(preconditioning-framework=firm=3) ≤ rank(L4/ksp_solve=firm=3)` holds — `ksp_solve.md` carries `firmness: firm` (verified on disk), which maps to rank 3 (see note in Issues). The `cites-evidence` L0 edge is to source, not a ladder node, so it does not constrain rank. Reachable: `depends-on` to `ksp_solve` (firm cap, itself reachable from the solver feature roots) wires it into the live graph. No mis-classification.

**skill-uptake-survey — pass (telemetry).** The report's shape (firm L0 re-citation) implies the citation-verification skill family; the report states all L0 citations were "self-verified this cycle via codemap read + citecheck --anchor, on-disk" (line 421) and the partly-constructive/firm-on-positive-structure escape is invoked by name. Skill uptake is referenced. Pure presence check, non-blocking.

### Issues found

None blocking. One observation, non-defect:

- **`L4/ksp_solve.md` carries `firmness: firm` but no explicit `rank:` token** (`book/src/L4/ksp_solve.md:1-15`). The rank invariant the report relies on (`rank(ksp_solve)=firm=3`) holds via the `firmness: firm → rank 3` mapping, which is sound mid-campaign (the HARD-gate-new typed frontmatter is being rolled out incrementally and not all firm chapters carry the explicit `rank:` field yet). The dependency IS firm, so the invariant is satisfied. This is a campaign-state observation about the dep chapter (out of this report's write-scope), not a defect in D1 — flagging only so the graded-stack edge-typing campaign picks up the `ksp_solve` rank-token backfill. No action required on this report.
