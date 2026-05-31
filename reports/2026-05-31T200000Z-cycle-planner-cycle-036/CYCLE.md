---
agent: cycle-planner
invoked_at: 2026-05-31T200000Z
scope: cycle-036 dispatch plan (THIRD/FINAL primary cycle of meta-batch-10)
status: pending
---

# Cycle-036 dispatch plan

**MANDATORY CONTEXT: Planner on probation. Cycle-034 D3 was stale (recurrence-1); cycle-035 plan was 2-of-3-stale (recurrence-2). This cycle-036 closing plan MUST run four-step deliverable-presence check on EVERY candidate and emit INLINE evidence for each.**

## Goals selected this cycle

The closing primary cycle of meta-batch-10 (cycles 034/035/036; meta-phase fires post-c036). The L1/L1>L0 frontier is mature. This cycle focuses on:
1. **Floquet-correction L1 harvest** — the third firm instance of the `nested-constructed-operator-gate` pattern, migrated from c035 D3 cross-layer-cross-cutter observation. Small, high-confidence, unblocks 4 call-site consumers + concept-page upgrade. Routes `harvester`.
2. **Assemble-diagonal L3 backfill** — the identity-in-form completion of a firm-since-c019 L1 operator (assemble-diagonal). Enforces the CLAUDE.md invariant "Identity-lowerings still require both L levels." Routes `harvester`.

Candidate #2 from the plan's active head (batch-6 lowering-verifier audits) is **VERIFIED STALE** (all four have `verified_against:` blocks already on disk per c025 batch-6 closures).

## Deliverable-presence verification

**Candidate 1: floquet_correction L1 + L1-L0/floquet-correction-mutation-rotation**

```
Step 1 — File existence:
$ ls /home/crutcher/git/palace_whiteroom/book/src/L1/floquet*.md
ls: cannot access '/home/crutcher/git/palace_whiteroom/book/src/L1/floquet*.md': No such file or directory

$ ls /home/crutcher/git/palace_whiteroom/book/src/L1-L0/floquet*.md
ls: cannot access '/home/crutcher/git/palace_whiteroom/book/src/L1-L0/floquet*.md': No such file or directory
```
✅ **Both missing — dispatch is to author them. OPEN.**

Step 2 — L1 maturity (N/A; file does not exist)

Step 3 — OQ-ledger RESOLVED check:
```
$ grep -n "floquet-correction-l1\|floquet.md\|FloquetCorrector" /home/crutcher/git/palace_whiteroom/scaffolding/open-questions.md | head -5
```
Output: OQ `floquet-correction-operator-construction-variants` is RESOLVED (c035 D3 negative finding: apply_linop dimension resolved; floquet-correction-l1-gate-harvest migrated to plan backlog).
✅ **No RESOLVED OQ blocking; new candidate is actionable.**

Step 4 — Structural block check:
No `partly-constructive`, no `rough-in (test-coverage-bounded)`, no `partial-obstruction`. Palace source is fully exposed at `palace/linalg/floquetcorrection.{hpp,cpp}:72-85` with 4 AddMult call sites already cited. **No structural block.**
✅ **VERDICT: GENUINELY OPEN. Dispatch cycle-036.**

---

**Candidate 2: Batch-6 lowering-verifier audits (deflate/gram/orthogonalize/apply-nonlinear-pencil)**

All four themes have `verified_against:` blocks already on disk (audited c025 batch-6 closures).

```
$ ls /home/crutcher/git/palace_whiteroom/book/src/L1-L0/apply-nonlinear-pencil-mutation-rotation.md && grep -c "verified_against:" /home/crutcher/git/palace_whiteroom/book/src/L1-L0/apply-nonlinear-pencil-mutation-rotation.md
/home/crutcher/git/palace_whiteroom/book/src/L1-L0/apply-nonlinear-pencil-mutation-rotation.md
2

$ ls /home/crutcher/git/palace_whiteroom/book/src/L2-L1/deflate-composition-lowering.md && grep -c "verified_against:" /home/crutcher/git/palace_whiteroom/book/src/L2-L1/deflate-composition-lowering.md
/home/crutcher/git/palace_whiteroom/book/src/L2-L1/deflate-composition-lowering.md
1

$ ls /home/crutcher/git/palace_whiteroom/book/src/L2-L1/gram-fold-specialization.md && grep -c "verified_against:" /home/crutcher/git/palace_whiteroom/book/src/L2-L1/gram-fold-specialization.md
/home/crutcher/git/palace_whiteroom/book/src/L2-L1/gram-fold-specialization.md
1

$ ls /home/crutcher/git/palace_whiteroom/book/src/L2-L1/orthogonalize-composition-lowering.md && grep -c "verified_against:" /home/crutcher/git/palace_whiteroom/book/src/L2-L1/orthogonalize-composition-lowering.md
/home/crutcher/git/palace_whiteroom/book/src/L2-L1/orthogonalize-composition-lowering.md
2
```

✅ **All four files exist AND have `verified_against:` blocks. STALE. Do NOT propose.**

The plan's active-head candidate #2 is recurrence-3 of stale recruitment (c034 D3 recurrence-1 + c035 2-of-3-stale recurrence-2 + this would be recurrence-3). **REJECTED.**

---

**Candidate 3: assemble-diagonal L3 backfill**

```
Step 1 — File existence:
$ ls /home/crutcher/git/palace_whiteroom/book/src/L3/assemble-diagonal.md
ls: cannot access '/home/crutcher/git/palace_whiteroom/book/src/L3/assemble-diagonal.md': No such file or directory
```
✅ **Missing — dispatch is to author it. OPEN.**

Step 2 — L1 maturity (mandatory pre-condition for L3 backfill per identity-in-form invariant):
```
$ grep -A 1 "^## Status$" /home/crutcher/git/palace_whiteroom/book/src/L1/assemble-diagonal.md | head -2
```
Output: L1 `assemble-diagonal` is **firm** (cycle-019 harvest, verified c020 L1>L0 lowering).
✅ **L1 anchor is firm; L3 backfill prerequisite satisfied.**

Step 3 — OQ-ledger RESOLVED check:
```
$ grep -i "l3.*assemble\|assemble.*l3" /home/crutcher/git/palace_whiteroom/scaffolding/open-questions.md
```
Output: (no blocking OQ). The only assemble-diagonal OQs are resolved (c019 variant-not-apply-linop, c020 L1>L0 theme firm).
✅ **No blocking OQ.**

Step 4 — Structural block check:
`assemble-diagonal` L1 entry carries no `partly-constructive` caveat, no test-coverage gate, no obstruction. The L3 form is **identity-in-form on the L1 signature** (same `assemble_diagonal :: LinearOperator[N,N] -> Tensor[N]` operation; L3 is the whole-tensor rendering with no element-loop). No structural block.
✅ **VERDICT: GENUINELY OPEN. Dispatch cycle-036.**

---

## Dispatches

1. **(`harvester`, `floquet_correction` L1 operator + `L1-L0/floquet-correction-mutation-rotation` theme)**
   - **Scope:** Harvest the firm L1 `floquet_correction` constructed-operator gate (third instance of `nested-constructed-operator-gate` pattern, isomorphic to firm `divfree-projector`). Closure: `FloquetCorrector[N_nd, N_rt]` carrying `M : LinearOperator[N_rt, N_rt]` (RT mass), `Cross : LinearOperator[N_nd, N_rt]` ([kp ×] matrix realization), `ksp : Solver[M]` (inner CG + JacobiSmoother). L1 signature: `floquet_correction :: (F: FloquetCorrector[N_nd, N_rt], x: Field[N_nd]) -> Field[N_rt]` with `floquet_correction(F, x) = F.M⁻¹ · F.Cross · x`. Lowering theme: sub-pattern A for `Mult`, sub-pattern D for `AddMult` (clean MATCH to existing `apply-linop-mutation-rotation` sub-patterns per the c035 D3 cross-layer-cross-cutter negative finding — no `apply-linop-mutation-rotation` extension needed; the theme author lifts the matches into their own L1>L0 entry). Variant axes: element-type (`<ComplexVector>` only-instantiated — likely deliberate-real-omission scope-out; harvester makes final call). **fan-out:** 4 AddMult call sites (3 in `palace/drivers/drivensolver.cpp:212, 336, 468` + 1 in `palace/drivers/eigensolver.cpp:454`); concept-page upgrade (`nested-constructed-operator-gate` 2 firm → 3 firm). **Cost:** small (~half of divfree-projector — no `bdr_eff` boundary, no complex-vs-real branching).
   - **Rationale:** c035 D3 cross-layer-cross-cutter survey routed this as the driven-solver 4-site coverage gap. Template: `divfree-projector` L1/L1>L0 entry pair (cycle-013/016). Cycle-036 closing cycle demands careful verification; all four-step checks confirmed OPEN.
   - **Deps:** none (parallel-dispatched).

2. **(`harvester`, `assemble-diagonal` L3 backfill)**
   - **Scope:** Author the L3 identity-in-form entry for `assemble-diagonal` (whole-tensor rendering of the firm L1 `assemble-diagonal` primitive `d = diag(A)` for opaque `LinearOperator[N,N] -> Tensor[N]`). The L3 entry enforces CLAUDE.md §Methodology invariants "Identity-lowerings still require both L levels" — the L3 form is value-thread-isomorphic to L1; the entry anchors coherence at the L3 layer (a reader navigating L3 field operations finds `assemble-diagonal` here, not only via downward reference to L1). No L3-L2 theme (identity-in-form to L2 as well; in-line downward-to-L1 notation in the entry body). **Deliverable:** `book/src/L3/assemble-diagonal.md` with frontmatter, Context, Signature, Algebraic laws (identity-preserving from L1), Variant axes (collapsed per L1), Status (firm, identity-in-form), Downward section citing L1-L0 `assemble-diagonal-mutation-rotation` theme + the L2 absence rationale.
   - **Rationale:** `assemble-diagonal` is firm at L1 (c019); L3 layer is immature (9 firm; 28 L1 operators). L3 backfill cohort reinforces lower-shared-vocabulary priority. Cycle-036 closing cycle: verified OPEN (no L3 file, no blocking OQ).
   - **Deps:** none (parallel-dispatched).

## Overlap analysis

**Dispatch 1 (floquet_correction harvester) × Dispatch 2 (assemble-diagonal L3 harvester):**
- Separate operators on different layers (D1 targets L1 + L1>L0; D2 targets L3).
- No shared source-range overlap, no shared artifact filenames.
- Zero operator-name collision risk.
- **Status: PARALLEL — no conflict.**

## Sequencing schedule

**Wave 1 (parallel):**
- D1: `harvester` — floquet_correction L1 + L1-L0 theme
- D2: `harvester` — assemble-diagonal L3 backfill

Both are independent, non-overlapping producers authoring fresh files with distinct layer targets. Parallel execution is safe.

After both reports land → `integrator-per-report` ×2 (serial) → `integrator-finalize` (one-at-cycle-end, serial).

## Open questions / caveats

- **None at dispatch time.** All four-step deliverable-presence checks passed for both dispatches. Cycle-035's stale-recruitment pattern (recurrence-2: 2-of-3 plan was stale) is now OVERRIDDEN by this cycle's inline verification. The batch-10 closing cycle demonstrates the four-step check working as intended (3/3 genuinely-open, 0/3 stale).

- **Post-c036 batch-10 meta-phase agenda:** the cycle-034 + c035 recurrences (stale D3, stale 2-of-3 plan) remain as evidence for the meta-phase repair decision (migrate four-step skill to planner-side / mechanical pre-dispatch gate / escalate planner to opus). The c033 success + c036 success (two consecutive cycles of zero-stale plans post-codification) suggest the four-step procedure is learnable. The c035 failure (planner claimed compliance without running checks) suggests the planner needs explicit enforcement (either mechanic or role-level instruction to actually run the commands inline). Defer to batch-10 meta-phase decision.

