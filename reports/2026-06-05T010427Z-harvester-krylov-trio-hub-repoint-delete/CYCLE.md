---
agent: harvester
invoked_at: 2026-06-05T010427Z
scope: graded-stack P2 slice-deletion campaign COMPLETION — krylov trio hub-repoint + delete {cg,gmres,arnoldi_step}
status: integrated
integrated_at: 2026-06-05T010427Z
integration_commit: cdbd8d851e1108ba48b1b54fff9d011968f462d2
integration_notes: "Applied clean by integrator-per-report (cycle-099 staging row 2/3), batch-31 P2 slice-deletion campaign COMPLETION. D2: repointed ALL 31 inbound Class-A markdown links + Class-B plain-text hub mentions, reconciled the arnoldi end-bound (iterative.cpp:73-118 → :73-109), DELETED the 3 slice files cg/gmres/arnoldi_step, removed the SUMMARY '# Phase 1 corpus' section + the introduction.md:23 inbound link, DELETED book/src/spec/index.md (corpus empty). Both inbound-link sweeps confirmed ZERO on the applied tree. Slice corpus 3→0; spec/slices/ EMPTY. cargo make book EXIT 0; step-5b rank_violations 0 GATE PASSES; no newly-orphaned node; slice-node count now ZERO. Recommended-CLOSE OQs: krylov-trio-slice-corpus-3to0-campaign-complete-retire-carveout-and-skill (the CAMPAIGN-COMPLETE trigger), krylov-trio-class-B-plaintext-mention-residue-batch31-cleanup (for batch-31 meta unify/enact)."
inputs:
  - cycle-099 D2 dispatch (coordinated owner, deps D1; D1 absorbs cg.md:27-141 into L4/krylov-step.md Form B + re-anchors that file's cg.md pointers §Semantics:82/§Status:152/§Evidence:171)
  - inbound-link preflight (paste-inline below): 31 inbound markdown links = 25 Class-A consumer/prose links + 6 corpus rows
  - firm homes verified: book/src/L1-L0/ksp-solve-mutation-rotation.md Sub-pattern C (GMRES, iterative.cpp:543-705 / inner Arnoldi loop within :563-683); book/src/concepts/sequential-obstruction.md (MGS obstruction); book/src/L2/krylov-step.md (names CG/GMRES/Arnoldi canonical instances)
  - arnoldi reconcile: iterative.cpp:73-118 → :73-109 (real-form GeneratePlaneRotation body-close at :109; complex specialization begins :111) — codemap + on-disk Read confirmed
---

# CYCLE: krylov-trio hub-repoint + slice-corpus deletion (3→0)

## Summary

This is dispatch D2 of cycle-099, the COMPLETION of the graded-stack P2 slice-deletion campaign. D1 (applied before me) closed the last firm-home gap by absorbing the CG L4-v0.5 first-iteration-unrolling material (`cg.md:27-141`) into `book/src/L4/krylov-step.md` Form B, and re-anchored that file's three cg.md pointers (§Semantics :82, §Status :152, §Evidence :171). With that absorption, **all material in the three slices `{cg,gmres,arnoldi_step}` is now fully firm-homed** — every slice-range citation can be dropped (CG: absorbed into Form B; GMRES inner-loop: firm L0 at `ksp-solve-mutation-rotation.md` Sub-pattern C; Arnoldi MGS obstruction: firm at `concepts/sequential-obstruction.md`).

I propose: **(1)** drop the Class-B "remains live in the reduced slice" / slice-range evidence parentheticals across the firm krylov-step hub + themes, repointing GMRES/Arnoldi citations to their firm homes; **(2)** repoint the 25 Class-A markdown links (concept consumer-bullets + `L0/ksp-factory-file.md`) to the firm CG/GMRES home `L2/krylov-step.md`; **(3)** reconcile the arnoldi plane-rotation end-bound `iterative.cpp:73-118 → :73-109`; **(4)** delete the 3 slice files; **(5)** remove the SUMMARY `# Phase 1 corpus` section + `spec/index.md` (the corpus is now EMPTY). **This completes the campaign's BUILD-CRITICAL / mechanical-completion criterion** — all 31 inbound markdown links are repointed/removed, all 3 slice files deleted, the SUMMARY `# Phase 1 corpus` Part + `spec/index.md` removed, the slices are reachability-GC-unreachable (no inbound `depends-on` edge), and the rank invariant holds with zero slice nodes. The firm homes are all confirmed on disk, so the repoint set lands clean. On apply, the slice corpus goes **3 → 0**. **Residue (NON-build-breaking, tracked follow-up):** ~50 plain-text (non-link) slice-range *evidence-provenance* mentions remain across firm chapters (8+ in `L2/krylov-step.md` alone — e.g. `:7`, `:58`, `:69`, `:79`, `:81`, `:86`, `:117`, `:120`, `:121`, `:172` carry `cg.md:…`/`gmres.md:…`/`arnoldi_step.md:…` plain-text ranges; many are deliberate frozen "Original pre-reduction slice ranges" historical narration, the same KIND as the `meta-reviews/*` historical-mention convention). These resolve to nothing on deletion (plain text, not links), so they do NOT break the build; the residual Class-B plain-text-mention cleanup is flagged as a tracked follow-up for the batch-31 meta-phase (see Open questions).

This is a **hub-repoint + deletion** dispatch, not an operator harvest — no new operator algebra; it composes already-firm vocabulary and removes detritus (graded-stack reachability-GC: the 3 slices carry no inbound `depends-on` frontmatter edge, only navigational links + plain-text evidence mentions, all of which this dispatch retires).

## Inbound-link preflight (paste-inline, the c098-missed-8-links guard)

`grep -rnE '\]\([^)]*slices/(cg|gmres|arnoldi_step)\.md' book/src --include='*.md'` enumerated **31 inbound links** (excluded by SOURCE-path, never by link-target text):

**Class-A consumer/prose links (25; all repointed in step 2):**
```
concepts/apply_BA.md:39            -> gmres
concepts/apply_linop.md:114        -> cg
concepts/apply_linop.md:116        -> gmres
concepts/axpy.md:38                -> cg
concepts/axpy.md:40                -> gmres
concepts/constructed-operators.md:220 -> gmres   (prose "See [gmres slice]")
concepts/constructed-operators.md:224 -> gmres
concepts/derived-view-hoisting.md:16  -> cg      (prose "[CG L4]")
concepts/dot.md:74                 -> cg
concepts/dot.md:76                 -> gmres
concepts/first-iteration-unrolling.md:9  -> cg   (prose "[cg slice]")
concepts/first-iteration-unrolling.md:77 -> cg
concepts/gmres.md:3                -> gmres      (prose "[the gmres slice]")
concepts/nrm2.md:37                -> cg
concepts/nrm2.md:38                -> gmres
concepts/orthogonalization.md:94   -> gmres
concepts/plane-rotation-stream.md:38  -> gmres
concepts/scal.md:37                -> cg
concepts/scal.md:39                -> gmres
concepts/solve-monad.md:39         -> gmres
concepts/state-stratification.md:28   -> gmres
concepts/variant-absorption.md:202    -> cg
concepts/variant-absorption.md:203    -> gmres
L0/ksp-factory-file.md:56          -> cg, gmres  (TWO links on one line)
```
**Corpus rows (6; removed in step 5):** `SUMMARY.md:292-294`, `spec/index.md:15-17`.

**Not touched (hard constraints):** `meta-reviews/2026-05-26-cycles-116-127.md:57` + `meta-reviews/2026-05-24-cycles-19-21.md:11` — confirmed PROSE, not live links (`grep -noE '\]\([^)]*slices/' meta-reviews/...` returns nothing); frozen historical narration, stays true after deletion. `L4/krylov-step.md` cg.md pointers — D1 owns. `domain_energy_reduce.md` — D3 owns.

**Coverage assertion:** every one of the 25 Class-A links + 6 corpus rows is repointed or removed below; zero surviving inbound `](..slice..)` links remain before any deletion is proposed.

## Step 3 — arnoldi end-bound reconcile (do FIRST; independent, closes OQ residue)

`book/src/L2-L1/incremental-least-squares-composition-lowering.md:112`: `iterative.cpp:73-118` over-runs into the complex `GeneratePlaneRotation` specialization. Verified against source: template `:72`, real-form signature `GeneratePlaneRotation(const T dx,...)` `:73`, real-form body-close `}` `:109`; the complex `std::complex<T>` overload begins at `:111`. Canonical real-form range is `:73-109`. Closes OQ `plane-rotation-givens-l0-citation-range-reconcile` end-bound residue.

```edit:book/src/L2-L1/incremental-least-squares-composition-lowering.md
(`GeneratePlaneRotation` `iterative.cpp:73-118`, `ApplyPlaneRotation` `iterative.cpp:227-241`) are
```
replace with:
```text
(`GeneratePlaneRotation` `iterative.cpp:73-109`, `ApplyPlaneRotation` `iterative.cpp:227-241`) are
```

## Step 1 — Class-B plain-text evidence-citation mention repoints

The slice-range parentheticals are dropped; GMRES/Arnoldi citations repoint to firm homes (CG material is now in Form B; nothing of the trio remains on disk to cite). Firm homes:
- **GMRES inner-loop body** (`gmres.md:459-471`, `:430-454`, `:594-606`/`:587-592`/`:551-554` v0.6, `:122-133` v0.2, `:215-219` v0.4, `:673-747` v0.7, `:435-454`): firm L0 home `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C — `GmresSolver<OperType>::Mult` `iterative.cpp:543-705`; outer restart loop + inner Arnoldi loop `iterative.cpp:563-683`.
- **Arnoldi step body** (`arnoldi_step.md:99-105`, `:285-298`, `:178-213`, `:99-109`/:146/:158/:197): firm L0 home is the same Sub-pattern C inner Arnoldi loop; the L2 Arnoldi instance is firm-homed at `book/src/L2/krylov-step.md` §Evidence.
- **Arnoldi MGS sequential-obstruction** (`arnoldi_step.md:194-213`): firm concept home `book/src/concepts/sequential-obstruction.md` §"MGS as sequential-obstruction" + §Examples (the GMRES `ls_update_column`/`back_solve`/MGS catalog).
- **CG step bodies / drivers** (`cg.md:*`): absorbed into `book/src/L4/krylov-step.md` Form B (D1) + firm L0 `ksp-solve-mutation-rotation.md` Sub-pattern B (`iterative.cpp:360-486`, kernel for-loop `:427-464`).

### 1a. `book/src/L2/krylov-step.md`

`:7` — surgically drop the three slice-range clauses, keep firm-home clauses:
```edit:book/src/L2/krylov-step.md
The Phase-1 slice corpus exhibits a recurring pattern: every iterative method written as a per-step kernel composed of (at most) five primitive groups, threaded by an outer fold. CG (the firm CG step-body evidence lives in this entry's §Evidence and lowers to L0 at `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern B — `iterative.cpp:360-486`; the L4-v0.5 first-iteration-unrolled rendering remains live at `book/src/spec/slices/cg.md:27-141`; original pre-reduction slice ranges `cg.md:103-115, :172-188, :393-425`), GMRES (`gmres.md:459-471`), Chebyshev (`book/src/L4/chebyshev.md` §Semantics `innerStep` — the polynomial-recurrence kernel), Arnoldi (`arnoldi_step.md:99-105, :285-298`), and the three polynomial-recurrence sites
```
replace with:
```text
The Phase-1 slice corpus (now fully lifted into firm entries — the three krylov slices `{cg,gmres,arnoldi_step}` were deleted cycle-099 once all material reached firm homes) exhibited a recurring pattern: every iterative method written as a per-step kernel composed of (at most) five primitive groups, threaded by an outer fold. CG (the firm CG step-body evidence lives in this entry's §Evidence and lowers to L0 at `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern B — `iterative.cpp:360-486`; the L4-v0.5 first-iteration-unrolled rendering is firm-homed at `book/src/L4/krylov-step.md` Form B), GMRES (firm L0 `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C — `iterative.cpp:543-705`), Chebyshev (`book/src/L4/chebyshev.md` §Semantics `innerStep` — the polynomial-recurrence kernel), Arnoldi (firm L0 Sub-pattern C inner Arnoldi loop within `iterative.cpp:563-683`; L2 instance in this entry's §Evidence), and the three polynomial-recurrence sites
```

`:69`:
```edit:book/src/L2/krylov-step.md
The kernel can carry a **first-iteration branch** internally (CG v0.4 form; the L0 `if (!it) { p = z; } else { AXPBY(...beta/beta_prev...); }` branch at `iterative.cpp:434-441`) or be unrolled out to a separate `cg_first_step` kernel before `iterate_while_with_prev` (CG v0.5 form, live at `book/src/spec/slices/cg.md:27-141`). Both are valid `krylov-step` shapes; the variant axis `first-iteration-unrolled` is a *step-shape* variant, not a *step-body* variant. Each form has a fixed (different) record schema; the unrolled form's steady-state record drops `β_prev` (the `forget_beta_prev` projection making the v0.4↔v0.5 equivalence formal is at `book/src/spec/slices/cg.md:120-133`). The choice is documented at [`concepts/first-iteration-unrolling`](../concepts/first-iteration-unrolling.md). (Original pre-reduction slice ranges: `cg.md:172-188`, `:393-425`, `:381-391`.)
```
replace with:
```text
The kernel can carry a **first-iteration branch** internally (CG v0.4 form; the L0 `if (!it) { p = z; } else { AXPBY(...beta/beta_prev...); }` branch at `iterative.cpp:434-441`) or be unrolled out to a separate `cg_first_step` kernel before `iterate_while_with_prev` (CG v0.5 form, firm-homed at `book/src/L4/krylov-step.md` Form B). Both are valid `krylov-step` shapes; the variant axis `first-iteration-unrolled` is a *step-shape* variant, not a *step-body* variant. Each form has a fixed (different) record schema; the unrolled form's steady-state record drops `β_prev` (the `forget_beta_prev` projection making the v0.4↔v0.5 equivalence formal is firm-homed in the `book/src/L4/krylov-step.md` Form B narration). The choice is documented at [`concepts/first-iteration-unrolling`](../concepts/first-iteration-unrolling.md).
```

`:119`:
```edit:book/src/L2/krylov-step.md
4. **first-iteration-unrolled vs. branch-in-body** — CG v0.4 keeps the `if it == 0 then s.r else axpby ...` branch inside the kernel (L0 anchor `iterative.cpp:434-441`); CG v0.5 (live at `book/src/spec/slices/cg.md:39-106`) splits `cg_first_step` and `cg_steady_step` and threads `β_prev` via `iterate_while_with_prev`. Both forms are valid `krylov-step` shapes; the variant axis selects which. (Original pre-reduction slice ranges: `cg.md:172-188`, `:393-425`.)
```
replace with:
```text
4. **first-iteration-unrolled vs. branch-in-body** — CG v0.4 keeps the `if it == 0 then s.r else axpby ...` branch inside the kernel (L0 anchor `iterative.cpp:434-441`); CG v0.5 (firm-homed at `book/src/L4/krylov-step.md` Form B) splits `cg_first_step` and `cg_steady_step` and threads `β_prev` via `iterate_while_with_prev`. Both forms are valid `krylov-step` shapes; the variant axis selects which.
```

`:138`:
```edit:book/src/L2/krylov-step.md
- CG L2 / L4 / L4-v0.5 step bodies — the firm L0 terminal home is `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern B (the inner CG body `iterative.cpp:360-486`; the per-step kernel for-loop `iterative.cpp:427-464`). The L4-v0.5 first-iteration-unrolling rendering (`cg_first_step` / `cg_steady_step`) remains the unique live material retained in the reduced slice at `book/src/spec/slices/cg.md:27-141`. (Original pre-reduction slice ranges: `cg.md:103-115` L2 step body, `:172-188` L4 `cg_step`, `:393-425` L4 v0.5 split.)
```
replace with:
```text
- CG L2 / L4 / L4-v0.5 step bodies — the firm L0 terminal home is `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern B (the inner CG body `iterative.cpp:360-486`; the per-step kernel for-loop `iterative.cpp:427-464`). The L4-v0.5 first-iteration-unrolling rendering (`cg_first_step` / `cg_steady_step`) is firm-homed at `book/src/L4/krylov-step.md` Form B (cycle-099 absorption).
```

`:139`:
```edit:book/src/L2/krylov-step.md
- `book/src/spec/slices/gmres.md:459-471` (GMRES L4 `inner_loop` body — Arnoldi-step + LS-update + counter-increment + convergence-test).
```
replace with:
```text
- GMRES `inner_loop` body (Arnoldi-step + LS-update + counter-increment + convergence-test) — firm L0 home `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C (`GmresSolver<OperType>::Mult` `iterative.cpp:543-705`; inner Arnoldi loop within `iterative.cpp:563-683`).
```

`:141`:
```edit:book/src/L2/krylov-step.md
- `book/src/spec/slices/arnoldi_step.md:99-105` (L1 Arnoldi step procedure), `:285-298` (L4 `arnoldiStep` monadic form).
```
replace with:
```text
- Arnoldi step procedure / `arnoldiStep` monadic form — firm L0 home `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C inner Arnoldi loop (within `iterative.cpp:563-683`); the MGS sub-step sequential-obstruction is firm at `book/src/concepts/sequential-obstruction.md` §"MGS as sequential-obstruction".
```

`:146`:
```edit:book/src/L2/krylov-step.md
- CG `cg_solve` calling `iterate_while` / `iterate_while_with_prev` — the v0.5 driver remains live in the reduced slice at `book/src/spec/slices/cg.md:86-106`; the L0 outer composition is `BaseKspSolver::Mult` at `ksp.cpp:296-310` wrapping the inner CG for-loop `iterative.cpp:427-464` (recognised at `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-patterns A/B). (Original pre-reduction slice ranges: `cg.md:208-220`, `:430-446`.)
```
replace with:
```text
- CG `cg_solve` calling `iterate_while` / `iterate_while_with_prev` — the v0.5 driver is firm-homed at `book/src/L4/krylov-step.md` Form B; the L0 outer composition is `BaseKspSolver::Mult` at `ksp.cpp:296-310` wrapping the inner CG for-loop `iterative.cpp:427-464` (recognised at `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-patterns A/B).
```

`:147`:
```edit:book/src/L2/krylov-step.md
- `book/src/spec/slices/gmres.md:430-454` (GMRES `solve_loop` + `restart_cycle` + `inner_loop` nested folds).
```
replace with:
```text
- GMRES `solve_loop` + `restart_cycle` + `inner_loop` nested folds — firm L0 home `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C outer restart loop (`iterative.cpp:563-683`).
```

`book/src/L2/index.md:131-134` (Pattern-instances sub-list — the dep-map pattern-instance list lives in the L2 **index**, not `krylov-step.md`; repairer corrected the edit-target file path cycle-099, on-disk-verified):
```edit:book/src/L2/index.md
    - `spec/slices/cg.md:103-115`, `:172-188`, `:393-425`
    - `spec/slices/gmres.md:459-471`
    - `book/src/L4/chebyshev.md` §Semantics `innerStep` (firm cycle-015; absorbed the former `spec/slices/chebyshev.md:354-362`)
    - `spec/slices/arnoldi_step.md:99-105`, `:285-298`
```
replace with:
```text
    - CG step bodies — firm `book/src/L4/krylov-step.md` Form B + L0 Sub-pattern B (`iterative.cpp:360-486`)
    - GMRES `inner_loop` — firm L0 Sub-pattern C (`iterative.cpp:543-705`)
    - `book/src/L4/chebyshev.md` §Semantics `innerStep` (firm cycle-015; absorbed the former `spec/slices/chebyshev.md:354-362`)
    - Arnoldi step — firm L0 Sub-pattern C inner Arnoldi loop (within `iterative.cpp:563-683`)
```

`book/src/L2/index.md:129` (Consumed-by note, slice-section names — same file-path correction as the block above: the Consumed-by note lives in the L2 **index**, not `krylov-step.md`; repairer corrected the edit-target file path cycle-099, on-disk-verified):
```edit:book/src/L2/index.md
  - **Consumed-by**: L4 `iterate_while` + `solve-monad` outer driver (cg.md §L4, gmres.md §L4, `book/src/L4/chebyshev.md` §Semantics (firm cycle-015; absorbed the former chebyshev §L4), arnoldi_step.md §L4).
```
replace with:
```text
  - **Consumed-by**: L4 `iterate_while` + `solve-monad` outer driver (firm `book/src/L4/krylov-step.md` §Semantics Form A/Form B for CG; firm L0 Sub-pattern C for GMRES/Arnoldi; `book/src/L4/chebyshev.md` §Semantics (firm cycle-015; absorbed the former chebyshev §L4)).
```

### 1b. `book/src/L3/krylov-step.md`

`:93` (drop the arnoldi_step obstruction-doc anchor → sequential-obstruction concept):
```edit:book/src/L3/krylov-step.md
this obstruction is **below `krylov-step`'s body** — the body calls `op.orthog` as an opaque closure — and is documented at `book/src/spec/slices/arnoldi_step.md:194-213`, not introduced by this entry.
```
replace with:
```text
this obstruction is **below `krylov-step`'s body** — the body calls `op.orthog` as an opaque closure — and is documented at [`concepts/sequential-obstruction`](../concepts/sequential-obstruction.md) §"MGS as sequential-obstruction", not introduced by this entry.
```

`:123`:
```edit:book/src/L3/krylov-step.md
This is why slice-level restart logic is structured as an *outer* loop around the `krylov-step`-folding inner loop at L3 (per `book/src/spec/slices/gmres.md:435-454`), not as a flattened single fold.
```
replace with:
```text
This is why restart logic is structured as an *outer* loop around the `krylov-step`-folding inner loop at L3 (per the GMRES outer restart loop, firm L0 `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C, `iterative.cpp:563-683`), not as a flattened single fold.
```

`:158`:
```edit:book/src/L3/krylov-step.md
**Below-body sequential-obstruction**: the MGS variant carries a sequential obstruction inside `op.orthog` per `book/src/spec/slices/arnoldi_step.md:194-213`; this obstruction is below `krylov-step`'s body — the kernel sees `op.orthog` as an opaque closure.
```
replace with:
```text
**Below-body sequential-obstruction**: the MGS variant carries a sequential obstruction inside `op.orthog` per [`concepts/sequential-obstruction`](../concepts/sequential-obstruction.md) §"MGS as sequential-obstruction"; this obstruction is below `krylov-step`'s body — the kernel sees `op.orthog` as an opaque closure.
```

`:188`:
```edit:book/src/L3/krylov-step.md
- `book/src/L3-L2/krylov-step-body-identity.md` §Verified-against (line 125; lifted from the original `book/src/spec/slices/cg.md:341-362` per the cycle-009 corpus reduction, preserved there with the verbatim Claim-2 quote at original slice line 360) — the cycle-002 combinator-miner identity-in-form claim (Claim 2: "step body lifts as identity"). The L2 primitive vocabulary is L3-native by signature shape; this is the upstream evidence for both the L4>L3 wrapper-dissolution audit and the L3>L2 body-identity ratification.
```
replace with:
```text
- `book/src/L3-L2/krylov-step-body-identity.md` §Verified-against (line 125; the cycle-002 combinator-miner Claim-2 verbatim quote was lifted there per the cycle-009 corpus reduction and is its terminal firm home) — the cycle-002 combinator-miner identity-in-form claim (Claim 2: "step body lifts as identity"). The L2 primitive vocabulary is L3-native by signature shape; this is the upstream evidence for both the L4>L3 wrapper-dissolution audit and the L3>L2 body-identity ratification.
```

`:189`:
```edit:book/src/L3/krylov-step.md
- `book/src/spec/slices/arnoldi_step.md:178-213` — corroborating evidence for the Arnoldi step. Three uncontested primitives lift as identity; `op.orthog` under MGS carries the below-body sequential obstruction. Audited cycle-006; confirms the body's identity-in-form claim.
```
replace with:
```text
- Arnoldi step — corroborating evidence for the Arnoldi step (firm L0 home `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C inner Arnoldi loop, within `iterative.cpp:563-683`). Three uncontested primitives lift as identity; `op.orthog` under MGS carries the below-body sequential obstruction (firm at [`concepts/sequential-obstruction`](../concepts/sequential-obstruction.md)). Audited cycle-006; confirms the body's identity-in-form claim.
```

`:196` (the big CG slice-instance bullet):
```edit:book/src/L3/krylov-step.md
- CG L2 / L4 / L4-v0.5 step bodies — lifted into firm `book/src/L2/krylov-step.md` §Evidence (line 138; the terminal firm home, carrying all three CG step-body ranges `cg.md:103-115` L2 / `:172-188` L4 Form A / `:393-425` L4-v0.5 Form B) per the cycle-009 corpus reduction. The firm `book/src/L4/krylov-step.md` §Evidence (lines 170-171) restates the L4 Form A / Form B step bodies but cites them transitively via the L2 entry (it carries no terminal source range of its own), so the terminal anchor is L2:138. The L4-v0.5 first-iteration-unrolling form remains the unique live material retained in the reduced slice at `book/src/spec/slices/cg.md:27-141`. (Original pre-reduction ranges: `cg.md:103-115`, `:172-188`, `:393-425`.) The L3 form is the wrapper-dissolved image of the L4 body.
```
replace with:
```text
- CG L2 / L4 / L4-v0.5 step bodies — firm-homed at `book/src/L2/krylov-step.md` §Evidence (the L2 terminal home, lowering to L0 Sub-pattern B `iterative.cpp:360-486`) and `book/src/L4/krylov-step.md` §Semantics Form A / Form B (the L4-v0.5 first-iteration-unrolling rendering absorbed into Form B cycle-099). The L3 form is the wrapper-dissolved image of the L4 body.
```

`:197`:
```edit:book/src/L3/krylov-step.md
- `book/src/spec/slices/gmres.md:459-471` (GMRES L4 `inner_loop` body).
```
replace with:
```text
- GMRES `inner_loop` body — firm L0 home `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C (`iterative.cpp:543-705`).
```

`:199`:
```edit:book/src/L3/krylov-step.md
- `book/src/spec/slices/arnoldi_step.md:99-105`, `:285-298` (L1 Arnoldi step + L4 monadic form).
```
replace with:
```text
- Arnoldi step + monadic form — firm L0 home `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C inner Arnoldi loop (within `iterative.cpp:563-683`).
```

`:204` (CG driver bullet):
```edit:book/src/L3/krylov-step.md
- CG `cg_solve` calling the L4 `iterate_while` / `iterate_while_with_prev` — lifted into firm `book/src/L2/krylov-step.md` §Evidence "Outer-driver consumer sites" (line 146; the terminal firm home, carrying both `cg.md:208-220` and `:430-446`) per the cycle-009 corpus reduction. (The firm `book/src/L4/krylov-step.md` carries no `cg_solve`-driver source citation of its own — the L4 entry names the driver pattern via `concepts/solve-monad.md` and inherits its evidence transitively through the L2 entry — so the terminal anchor is L2:146.) The L4-v0.5 `cg_solve` driver (with `iterate_while_with_prev`) remains live in the reduced slice at `book/src/spec/slices/cg.md:86-106`. (Original pre-reduction ranges: `cg.md:208-220`, `:430-446`.) At L3 these dissolve to the tail-recursive form per the upstream theme.
```
replace with:
```text
- CG `cg_solve` calling the L4 `iterate_while` / `iterate_while_with_prev` — firm-homed at `book/src/L2/krylov-step.md` §Evidence "Outer-driver consumer sites" (the L2 terminal home, lowering to L0 `BaseKspSolver::Mult` `ksp.cpp:296-310` wrapping the inner CG for-loop `iterative.cpp:427-464`) and `book/src/L4/krylov-step.md` Form B (the L4-v0.5 `cg_solve` driver with `iterate_while_with_prev`, absorbed cycle-099). At L3 these dissolve to the tail-recursive form per the upstream theme.
```

`:205`:
```edit:book/src/L3/krylov-step.md
- `book/src/spec/slices/gmres.md:430-454` (GMRES restart/inner-loop nested folds; at L3 each fold dissolves independently).
```
replace with:
```text
- GMRES restart/inner-loop nested folds (at L3 each fold dissolves independently) — firm L0 home `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C outer restart loop (`iterative.cpp:563-683`).
```

### 1c. `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`

`:231`:
```edit:book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md
- `book/src/L3-L2/krylov-step-body-identity.md` §Verified-against (line 125; lifted from the original `book/src/spec/slices/cg.md:341-362` per the cycle-009 corpus reduction) — the combinator-miner cycle-002 evidence for L2>L3 body identity. Claim 2 ("step body lifts as identity") is the cited support, preserved there with the verbatim claim quote. Re-read for the cycle-006 audit; assertion confirmed.
```
replace with:
```text
- `book/src/L3-L2/krylov-step-body-identity.md` §Verified-against (line 125; the terminal firm home of the cycle-002 Claim-2 verbatim quote, lifted there per the cycle-009 corpus reduction) — the combinator-miner cycle-002 evidence for L2>L3 body identity. Claim 2 ("step body lifts as identity") is the cited support, preserved there with the verbatim claim quote. Re-read for the cycle-006 audit; assertion confirmed.
```

`:232`:
```edit:book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md
- `book/src/spec/slices/arnoldi_step.md:178-213` — L2>L3 lift for arnoldi step. Three uncontested primitives plus the variant-dependent `op.orthog` obstruction (which is localised below the step body, not at the body level). Confirms the audit.
```
replace with:
```text
- Arnoldi step L2>L3 lift — three uncontested primitives plus the variant-dependent `op.orthog` obstruction (localised below the step body, not at the body level). Firm L0 home `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C inner Arnoldi loop; the MGS obstruction firm at [`concepts/sequential-obstruction`](../concepts/sequential-obstruction.md). Confirms the audit.
```

`:233`:
```edit:book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md
- `book/src/L3/krylov-step.md` §Algebraic-laws non-lift catalogue (lifted from the original `book/src/spec/slices/cg.md:347-350` Claim 1 per the cycle-009 corpus reduction; `arnoldi_step.md:194-213` remains the valid live anchor) — the negative L3 result for the *outer* loop. Cited for completeness; the outer-loop obstruction is independent of the step-body rotation handled by this theme.
```
replace with:
```text
- `book/src/L3/krylov-step.md` §Algebraic-laws non-lift catalogue (the cycle-002 Claim-1 negative result, lifted there + into [`concepts/sequential-obstruction`](../concepts/sequential-obstruction.md) per the cycle-009 corpus reduction) — the negative L3 result for the *outer* loop. Cited for completeness; the outer-loop obstruction is independent of the step-body rotation handled by this theme.
```

### 1d. `book/src/L4-L3/iterate-while-dissolution.md`

`:120`:
```edit:book/src/L4-L3/iterate-while-dissolution.md
Slices whose termination needs `SimState.it` fold `it` into the carry (`book/src/spec/slices/cg.md:101` — the v0.5 predicate `\(s, _) -> s.it < config.max_it && not s.converged`).
```
replace with:
```text
Consumers whose termination needs `SimState.it` fold `it` into the carry (the CG v0.5 predicate `\(s, _) -> s.it < config.max_it && not s.converged`, firm-homed at `book/src/L4/krylov-step.md` Form B).
```

`:155`:
```edit:book/src/L4-L3/iterate-while-dissolution.md
- `book/src/spec/slices/arnoldi_step.md:194-213` — the live `sequential-obstruction` anchor for the outer loop surviving at L3.
```
replace with:
```text
- [`concepts/sequential-obstruction`](../concepts/sequential-obstruction.md) §"MGS as sequential-obstruction" — the firm `sequential-obstruction` anchor for the outer loop surviving at L3.
```

### 1e. `book/src/L4-L3/iterate-while-with-prev-dissolution.md`

`:124`:
```edit:book/src/L4-L3/iterate-while-with-prev-dissolution.md
This is the expected outcome for Krylov-family iterations at L3 per [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the live anchor is `book/src/spec/slices/arnoldi_step.md:194-213`.
```
replace with:
```text
This is the expected outcome for Krylov-family iterations at L3 per [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the firm anchor is its §"MGS as sequential-obstruction".
```

`:130`:
```edit:book/src/L4-L3/iterate-while-with-prev-dissolution.md
The Form-B `iterate_while_with_prev` consumer is CG v0.5 (`book/src/spec/slices/cg.md:100-108`); a slice-specialised CG-Form-B dissolution would instantiate this theme's pruned form under the CG four-scalar consumer, but is not re-derived here.
```
replace with:
```text
The Form-B `iterate_while_with_prev` consumer is CG v0.5 (firm-homed at `book/src/L4/krylov-step.md` Form B); a CG-Form-B dissolution would instantiate this theme's pruned form under the CG four-scalar consumer, but is not re-derived here.
```

`:138`:
```edit:book/src/L4-L3/iterate-while-with-prev-dissolution.md
(CG v0.5: `s.converged` is set inside `cg_steady_step` from the freshly-computed `res'`; `beta_prev` is the `prev` parameter but is never read by the predicate; the predicate-on-carry-only is at `cg.md:101`, the `beta_prev`-as-`prev`-parameter at `cg.md:102-103`: `book/src/spec/slices/cg.md:101-103`).
```
replace with:
```text
(CG v0.5: `s.converged` is set inside `cg_steady_step` from the freshly-computed `res'`; `beta_prev` is the `prev` parameter but is never read by the predicate; the predicate-on-carry-only + the `beta_prev`-as-`prev`-parameter pattern is firm-homed at `book/src/L4/krylov-step.md` Form B).
```

`:142`:
```edit:book/src/L4-L3/iterate-while-with-prev-dissolution.md
If a slice needs an "already-converged-before-first-step" guard, it lives outside the combinator (CG v0.5's outer initial-convergence test, `book/src/spec/slices/cg.md:92`) and outside this lowering.
```
replace with:
```text
If a consumer needs an "already-converged-before-first-step" guard, it lives outside the combinator (CG v0.5's outer initial-convergence test, firm-homed at `book/src/L4/krylov-step.md` Form B) and outside this lowering.
```

`:174`:
```edit:book/src/L4-L3/iterate-while-with-prev-dissolution.md
- `book/src/spec/slices/arnoldi_step.md:194-213` — the live `sequential-obstruction` anchor for the steady loop surviving at L3.
```
replace with:
```text
- [`concepts/sequential-obstruction`](../concepts/sequential-obstruction.md) §"MGS as sequential-obstruction" — the firm `sequential-obstruction` anchor for the steady loop surviving at L3.
```

`:182`:
```edit:book/src/L4-L3/iterate-while-with-prev-dissolution.md
- `book/src/spec/slices/cg.md:100-108` — the canonical v0.5 CG slice using `iterate_while_with_prev` (the call site); the `cg_first_step` / `cg_steady_step` split (`:52-108`) is the prototypical bootstrap/steady pair; `:101-103` the predicate-on-carry-only (`:101`) + `beta_prev`-as-`prev`-parameter (`:102-103`) pattern. (Re-anchored from the firm L4 cap's historical `cg.md:441-446` citation, which predates the cycle-009 corpus reduction of the cg slice to 165 lines.)
```
replace with:
```text
- `book/src/L4/krylov-step.md` Form B — the canonical v0.5 CG form using `iterate_while_with_prev` (the call site); the `cg_first_step` / `cg_steady_step` split is the prototypical bootstrap/steady pair, with the predicate-on-carry-only + `beta_prev`-as-`prev`-parameter pattern. (Firm-homed there cycle-099, absorbing the former `cg.md:27-141` slice material; supersedes the historical `cg.md:441-446` citation predating the corpus reduction.)
```

### 1f. `book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md`

`:11` (the prose body — repoint all gmres.md range citations to the firm v0.6 home; the slice no longer exists):
```edit:book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md
The CG precedent for rendering a solve loop as a direct `iterate_while` invocation (the v0.4 form `iterate_while s0' (\s -> s.it < config.max_it && not s.converged) (\s -> cg_step opA eps s)`) was lifted into the firm L4 entry [`L4/krylov-step`](../L4/krylov-step.md) §Semantics (Form A; the `krylov-step` body folded by `iterate_while`) when the cg slice was reduced — the cg slice (`book/src/spec/slices/cg.md`, now 166 lines) retains only its unique L4 v0.5 first-iteration-unrolling material (which uses `iterate_while_with_prev`); the GMRES slice (likewise reduced — its v0.1 `inner_loop` was lifted into firm entries per the slice stub-header) renders its inner loop as an inline tail-recursive `Solve`-monad function in the retained §L4 self-rotation progression: the earliest retained form is v0.2 at `gmres.md:122-133`, and the v0.6 form (the migration's direct input) is at `gmres.md:594-606` with `check_stop` at `gmres.md:587-592` and the `StopReason` sum type at `gmres.md:551-554`. Both the CG and GMRES forms are tail-recursive value-threading folds; the migration is the recognition that the GMRES form is an `iterate_while` invocation with the witness-into-carry hoist applied to the v0.6 `StopReason` structure. The migrated v0.7 form is appended to the slice's §L4 progression as the v0.7 section (cycle-020 wave-1 lifter).
```
replace with:
```text
The CG precedent for rendering a solve loop as a direct `iterate_while` invocation (the v0.4 form `iterate_while s0' (\s -> s.it < config.max_it && not s.converged) (\s -> cg_step opA eps s)`) is firm-homed in [`L4/krylov-step`](../L4/krylov-step.md) §Semantics (Form A; the `krylov-step` body folded by `iterate_while`); the CG v0.5 first-iteration-unrolling material (which uses `iterate_while_with_prev`) is firm-homed there as Form B (cycle-099 absorption). The GMRES inner-loop `Solve`-monad rendering (v0.2 through the migrated v0.7 form) was firm-homed at L0 in `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C (`GmresSolver<OperType>::Mult` `iterative.cpp:543-705`; outer restart + inner Arnoldi loop `iterative.cpp:563-683`); the v0.6→v0.7 witness-into-carry migration is the recognition that the GMRES form is an `iterate_while` invocation with the witness hoist applied to the v0.6 `StopReason` structure. Both the CG and GMRES forms are tail-recursive value-threading folds.
```

`:166`:
```edit:book/src/L4-L3/fgmres-inner-loop-iterate-while-migration.md
- `book/src/spec/slices/gmres.md:594-606` (v0.6 `inner_loop`), `:587-592` (v0.6 `check_stop`), `:551-554` (the `StopReason` sum type), and the appended §L4 v0.7 self-rotation section (`gmres.md:673-747`) — the v0.6 inline tail-recursive `Solve`-monad form that the cycle-020 wave-1 lifter migration re-rendered to the migrated v0.7 form, plus the authored v0.7 form itself. The FGMRES specialisation applies the variant-axis collapses to that migrated form. The LHS is no longer speculative — it is the firm migrated form shared with the now-firm gmres sibling.
```
replace with:
```text
- GMRES v0.6 `inner_loop` / `check_stop` / `StopReason` sum type + the migrated v0.7 form — firm L0 home `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C (`GmresSolver<OperType>::Mult` `iterative.cpp:543-705`; inner Arnoldi loop within `iterative.cpp:563-683`). The FGMRES specialisation applies the variant-axis collapses to that migrated form. The LHS is no longer speculative — it is the firm migrated form shared with the gmres sibling.
```

`:176`:
```edit:book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md
- `book/src/spec/slices/gmres.md:594-606` (v0.6 `inner_loop`), `:587-592` (v0.6 `check_stop`), `:551-554` (the `StopReason` sum type), and the appended §L4 v0.7 self-rotation section — the v0.6 inline tail-recursive `Solve`-monad form that the cycle-020 wave-1 lifter migration re-rendered to the LHS shape above, plus the authored v0.7 form itself. The earliest retained form (v0.2) is at `gmres.md:122-133`; the v0.1 form was lifted into firm entries before this theme firmed (slice stub-header). The LHS is no longer speculative — it is the migrated form.
```
replace with:
```text
- GMRES v0.6 `inner_loop` / `check_stop` / `StopReason` sum type + the migrated v0.7 form — firm L0 home `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C (`GmresSolver<OperType>::Mult` `iterative.cpp:543-705`; outer restart + inner Arnoldi loop `iterative.cpp:563-683`). The LHS is no longer speculative — it is the migrated form.
```

`:179`:
```edit:book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md
- `book/src/spec/slices/cg.md:215-219` — precedent rendering pattern (CG v0.4 `iterate_while s0' (\s -> s.it < config.max_it && not s.converged) (\s -> cg_step opA eps s)`). The GMRES migration applies the same pattern with the witness-augmented carry.
```
replace with:
```text
- `book/src/L4/krylov-step.md` §Semantics Form A — precedent rendering pattern (CG v0.4 `iterate_while s0' (\s -> s.it < config.max_it && not s.converged) (\s -> cg_step opA eps s)`, firm-homed there). The GMRES migration applies the same pattern with the witness-augmented carry.
```

### 1g. `book/src/L3-L2/krylov-step-body-identity.md`

`:125` (the §Verified-against bullet — terminal firm home of the verbatim Claim-2 quote; drop the dead-range note but KEEP the verbatim quote which lives HERE):
```edit:book/src/L3-L2/krylov-step-body-identity.md
This verbatim quote was lifted into this §Verified-against bullet per the cycle-009 corpus reduction and is preserved here as the terminal firm home — the upstream `L4-L3/krylov-step-typed-wrapper-dissolution.md` §"Audit of cycle-002 identity-in-form claim" and the firm `L3/krylov-step.md` §dep-map (line 188) both point at this bullet as the lifted-in anchor for the CG body-identity evidence. (Original pre-reduction slice range `cg.md:341-362`, with the verbatim claim at original slice line 360 and its justification at original slice lines 353-358; the `cg.md` slice is now a 165-line stub and that range no longer resolves.) Re-read for the cycle-006 audit; assertion confirmed.
```
replace with:
```text
This verbatim quote was lifted into this §Verified-against bullet per the cycle-009 corpus reduction and is preserved here as the **terminal firm home** of the CG body-identity evidence — the upstream `L4-L3/krylov-step-typed-wrapper-dissolution.md` §"Audit of cycle-002 identity-in-form claim" and the firm `L3/krylov-step.md` §dep-map both point at this bullet as the lifted-in anchor. (The `cg.md` slice from which it was originally lifted was deleted cycle-099 once all its material reached firm homes; this bullet now carries the quote in full, so nothing is lost.) Re-read for the cycle-006 audit; assertion confirmed.
```

`:126`:
```edit:book/src/L3-L2/krylov-step-body-identity.md
- `book/src/spec/slices/arnoldi_step.md:178-213` — combinator-miner cycle-002 evidence for the Arnoldi step's L2>L3 lift. The three uncontested primitives (`apply_BA`, `subdiag_norm`, `normalize`) lift as identity (lines 184-190); the fourth (`orthogonalize` under MGS) carries a [sequential-obstruction](../concepts/sequential-obstruction.md) (lines 192-213). **The obstruction is below the kernel body** — it is a property of the `op.orthog` primitive under the MGS variant, not of the `krylov-step` body that calls `op.orthog` as an opaque closure. The body's identity-in-form claim survives the obstruction.
```
replace with:
```text
- Arnoldi step L2>L3 lift (combinator-miner cycle-002 evidence; firm L0 home `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C inner Arnoldi loop). The three uncontested primitives (`apply_BA`, `subdiag_norm`, `normalize`) lift as identity; the fourth (`orthogonalize` under MGS) carries a [sequential-obstruction](../concepts/sequential-obstruction.md) (firm at its §"MGS as sequential-obstruction"). **The obstruction is below the kernel body** — it is a property of the `op.orthog` primitive under the MGS variant, not of the `krylov-step` body that calls `op.orthog` as an opaque closure. The body's identity-in-form claim survives the obstruction.
```

`:128`:
```edit:book/src/L3-L2/krylov-step-body-identity.md
- `book/src/spec/slices/gmres.md:459-471` — the GMRES `inner_loop` body. Same kernel-body pattern modulo the `op.orthog` variant absorption; same identity-in-form rotation on the body.
```
replace with:
```text
- GMRES `inner_loop` body (firm L0 home `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C, `iterative.cpp:543-705`). Same kernel-body pattern modulo the `op.orthog` variant absorption; same identity-in-form rotation on the body.
```

### 1h. `book/src/L1/orthogonalize.md` `:306`

```edit:book/src/L1/orthogonalize.md
- Slice `book/src/spec/slices/arnoldi_step.md:5` names "a firm `L1/orthogonalize` (or
```
replace with:
```text
- The (now-deleted) `arnoldi_step` slice named "a firm `L1/orthogonalize` (or
```

### 1i. `book/src/L1-L0/minres-iteration.md` `:144`

```edit:book/src/L1-L0/minres-iteration.md
- `book/src/spec/slices/arnoldi_step.md` — the four-line Arnoldi
  inner-body kernel (`apply → orthog → norm → scal`) is the structural
  parent of the Lanczos three-term recurrence; one-line variant axis
```
replace with:
```text
- The Arnoldi inner-body kernel (`apply → orthog → norm → scal`; firm L0 home
  `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C inner Arnoldi loop)
  is the structural parent of the Lanczos three-term recurrence; one-line variant axis
```

### 1j. `book/src/L3/apply_linop.md` `:186,:187,:189`

`:186`:
```edit:book/src/L3/apply_linop.md
- `book/src/spec/slices/cg.md:58, :75` — CG L4 v0.5 step bodies (`cg_first_step` and `cg_steady_step`); each has `let Ap = apply opA p'` as the per-step matvec call. (Note: cg.md is the post-cycle-010-reduction stub form (165 lines); the L1/L2/L3/L4 v0.1-v0.4 content was lifted to firm entries per CLAUDE.md §Methodology invariants "Phase 1 corpus reduces as material is lifted"; the v0.5 first-iteration-unrolling rotation is the unique material retained.)
```
replace with:
```text
- CG L4 v0.5 step bodies (`cg_first_step` and `cg_steady_step`; firm-homed at `book/src/L4/krylov-step.md` Form B, cycle-099); each has `let Ap = apply opA p'` as the per-step matvec call. The L0 matvec home is `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern B (`iterative.cpp:360-486`).
```

`:187`:
```edit:book/src/L3/apply_linop.md
- `book/src/spec/slices/gmres.md:459-471` — GMRES L4 `inner_loop` body; `apply_linop` at the Arnoldi-step matvec.
```
replace with:
```text
- GMRES `inner_loop` body; `apply_linop` at the Arnoldi-step matvec — firm L0 home `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C (`iterative.cpp:543-705`).
```

`:189`:
```edit:book/src/L3/apply_linop.md
- `book/src/spec/slices/arnoldi_step.md:99-109, :146, :158, :197` — Arnoldi step procedure (line 99 `apply_BA : w ← apply_linop(T, V[j])`; line 146 `apply_linop(T, V[j]) — pure functional form`; line 158 cross-cutting prose; line 197 L3-form rendering `w ← apply_linop(T, V[j]) -- field-side, global`); `apply_linop` at the Krylov-basis extension matvec.
```
replace with:
```text
- Arnoldi step procedure — `apply_BA : w ← apply_linop(T, V[j])`, the pure-functional form, and the L3-form rendering `w ← apply_linop(T, V[j])` (field-side, global); `apply_linop` at the Krylov-basis extension matvec. Firm L0 home `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C inner Arnoldi loop (within `iterative.cpp:563-683`).
```

### 1k. `book/src/L4/iterate-while.md` `:229,:230`

`:229`:
```edit:book/src/L4/iterate-while.md
- `book/src/spec/slices/cg.md:215-219` — the canonical `iterate_while` call site at L4 v0.4 (`iterate_while s0' (\s -> s.it < config.max_it && not s.converged) (\s -> cg_step opA eps s)`).
```
replace with:
```text
- `book/src/L4/krylov-step.md` §Semantics Form A — the canonical `iterate_while` call site at L4 v0.4 (`iterate_while s0' (\s -> s.it < config.max_it && not s.converged) (\s -> cg_step opA eps s)`, firm-homed there).
```

`:230`:
```edit:book/src/L4/iterate-while.md
- `book/src/spec/slices/cg.md:267-269,277` — the L3↔L4 correspondence notes that explicitly map Palace's `for (; it < max_it && !converged; it++)` to `iterate_while`. **L0 evidence**: `reference/palace/palace/linalg/iterative.cpp:427` (the PCG main-loop predicate-driven `for`-loop) is the canonical Palace iteration shape this combinator names.
```
replace with:
```text
- The L3↔L4 correspondence (firm-homed at `book/src/L4/krylov-step.md` + `book/src/L4-L3/iterate-while-dissolution.md`) explicitly maps Palace's `for (; it < max_it && !converged; it++)` to `iterate_while`. **L0 evidence**: `reference/palace/palace/linalg/iterative.cpp:427` (the PCG main-loop predicate-driven `for`-loop) is the canonical Palace iteration shape this combinator names.
```

### 1l. `book/src/L4/iterate-while-with-prev.md` `:233`

```edit:book/src/L4/iterate-while-with-prev.md
- `book/src/spec/slices/cg.md:393-446` — the canonical v0.5 CG slice using this combinator. The `cg_first_step` / `cg_steady_step` split is the prototypical Form B pair; the call at line 441 `iterate_while_with_prev s1 s0.beta (\(s, _) -> ...) (\(s, beta_prev) -> ...)` is the prototypical use. **Note on closure-argument convention**: the L4 row's `steady_step` signature `((α, β) -> ...)` adopts the *carry-first, prev-second* convention. This matches the [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md) pseudo-code at `first-iteration-unrolling.md:34-37` (`\(s, carry) -> (steady_step ... carry s, extract_carry s)` — `s` precedes `carry`) AND the cg.md v0.5 call site at `cg.md:443` (`\(s, beta_prev) -> ...` — `s` precedes `beta_prev`). The L4 row's convention is therefore consistent with both upstream renderings; no v0.6 self-rotation on cg.md is needed.
```
replace with:
```text
- `book/src/L4/krylov-step.md` Form B — the canonical v0.5 CG form using this combinator (firm-homed there cycle-099). The `cg_first_step` / `cg_steady_step` split is the prototypical Form B pair; the call `iterate_while_with_prev s1 s0.beta (\(s, _) -> ...) (\(s, beta_prev) -> ...)` is the prototypical use. **Note on closure-argument convention**: the L4 row's `steady_step` signature `((α, β) -> ...)` adopts the *carry-first, prev-second* convention. This matches the [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md) pseudo-code at `first-iteration-unrolling.md:34-37` (`\(s, carry) -> (steady_step ... carry s, extract_carry s)` — `s` precedes `carry`) AND the CG v0.5 call site (`\(s, beta_prev) -> ...` — `s` precedes `beta_prev`). The L4 row's convention is therefore consistent with both renderings.
```

## Step 2 — Class-A markdown-link repoints (25 links → firm home `L2/krylov-step.md`)

Per the c097/c098 consumer-bullet precedent, the "Slices that use this primitive" consumer bullets repoint to the firm CG/GMRES home `book/src/L2/krylov-step.md` (which names CG/GMRES/Arnoldi as canonical Krylov instances in its §Context). Descriptive tails preserved. Each `[cg]`/`[gmres]` link → `[krylov-step (CG / GMRES instance)](../L2/krylov-step.md)`.

```edit:book/src/concepts/nrm2.md
- [cg](../spec/slices/cg.md) — residual norm `‖r‖` per iteration.
- [gmres](../spec/slices/gmres.md) — initial residual norm `β`, Arnoldi
```
replace with:
```text
- [`krylov-step` (CG instance)](../L2/krylov-step.md) — residual norm `‖r‖` per iteration.
- [`krylov-step` (GMRES instance)](../L2/krylov-step.md) — initial residual norm `β`, Arnoldi
```

```edit:book/src/concepts/dot.md
- [cg](../spec/slices/cg.md) — `⟨r, z⟩` (β numerator) and `⟨p, A p⟩` (α
  denominator).
- [gmres](../spec/slices/gmres.md) — orthogonalization coefficients
```
replace with:
```text
- [`krylov-step` (CG instance)](../L2/krylov-step.md) — `⟨r, z⟩` (β numerator) and `⟨p, A p⟩` (α
  denominator).
- [`krylov-step` (GMRES instance)](../L2/krylov-step.md) — orthogonalization coefficients
```

```edit:book/src/concepts/axpy.md
- [cg](../spec/slices/cg.md) — `x ← x + α p` (`x.Add(α, p)`), `r ← r − α A p`
  (`r.Add(-α, Ap)`).
- [gmres](../spec/slices/gmres.md) — basis-correction sum `x ← x + Σ y_k
```
replace with:
```text
- [`krylov-step` (CG instance)](../L2/krylov-step.md) — `x ← x + α p` (`x.Add(α, p)`), `r ← r − α A p`
  (`r.Add(-α, Ap)`).
- [`krylov-step` (GMRES instance)](../L2/krylov-step.md) — basis-correction sum `x ← x + Σ y_k
```

```edit:book/src/concepts/apply_BA.md
- [gmres](../spec/slices/gmres.md) — the per-Arnoldi-step operator;
```
replace with:
```text
- [`krylov-step` (GMRES instance)](../L2/krylov-step.md) — the per-Arnoldi-step operator;
```

```edit:book/src/concepts/scal.md
- [cg](../spec/slices/cg.md) — `p ← (β/β_prev) p` before adding `z`
  (fused at L0 with the subsequent `p += z`).
- [gmres](../spec/slices/gmres.md) — basis normalization `v_{j+1} ←
```
replace with:
```text
- [`krylov-step` (CG instance)](../L2/krylov-step.md) — `p ← (β/β_prev) p` before adding `z`
  (fused at L0 with the subsequent `p += z`).
- [`krylov-step` (GMRES instance)](../L2/krylov-step.md) — basis normalization `v_{j+1} ←
```

```edit:book/src/concepts/apply_linop.md
- [cg](../spec/slices/cg.md) — single application per inner iteration
  (`A p`).
- [gmres](../spec/slices/gmres.md) — single application per Arnoldi
```
replace with:
```text
- [`krylov-step` (CG instance)](../L2/krylov-step.md) — single application per inner iteration
  (`A p`).
- [`krylov-step` (GMRES instance)](../L2/krylov-step.md) — single application per Arnoldi
```

```edit:book/src/concepts/orthogonalization.md
- [gmres](../spec/slices/gmres.md) — orthogonalising the new Arnoldi vector against the
```
replace with:
```text
- [`krylov-step` (GMRES instance)](../L2/krylov-step.md) — orthogonalising the new Arnoldi vector against the
```

```edit:book/src/concepts/variant-absorption.md
- [cg](../spec/slices/cg.md) — three axes all absorbed parametrically.
- [gmres](../spec/slices/gmres.md) — six axes; side absorbed via
```
replace with:
```text
- [`krylov-step` (CG instance)](../L2/krylov-step.md) — three axes all absorbed parametrically.
- [`krylov-step` (GMRES instance)](../L2/krylov-step.md) — six axes; side absorbed via
```

```edit:book/src/concepts/plane-rotation-stream.md
- [`gmres` slice](../spec/slices/gmres.md) — consumer (per-step driver and back-solve).
```
replace with:
```text
- [`krylov-step` (GMRES instance)](../L2/krylov-step.md) — consumer (per-step driver and back-solve).
```

```edit:book/src/concepts/state-stratification.md
- [slice: gmres §L4](../spec/slices/gmres.md) — `SimState` / `OpParams` / `Krylov` for restarted GMRES and FGMRES.
```
replace with:
```text
- [`krylov-step` (GMRES instance)](../L2/krylov-step.md) — `SimState` / `OpParams` / `Krylov` for restarted GMRES and FGMRES.
```

```edit:book/src/concepts/solve-monad.md
- [slice: gmres §L4](../spec/slices/gmres.md) — restarted GMRES / FGMRES coordination over `SimState`, with `Krylov` threaded as a `let`-bound bundle inside each `restart_cycle`.
```
replace with:
```text
- [`krylov-step` (GMRES instance)](../L2/krylov-step.md) — restarted GMRES / FGMRES coordination over `SimState`, with `Krylov` threaded as a `let`-bound bundle inside each `restart_cycle`.
```

For `gmres.md:3` concept page — repoint the lead prose link to the firm home:
```edit:book/src/concepts/gmres.md
Generalized Minimum Residual method. See [the gmres slice](../spec/slices/gmres.md) for the L1 mathematical statement and the slice's progression up the layer stack.
```
replace with:
```text
Generalized Minimum Residual method. See the firm [`krylov-step` (GMRES instance)](../L2/krylov-step.md) for the GMRES kernel decomposition and [`ksp_solve`](../L2/ksp_solve.md) for the outer-driver composition; the L0 ground truth is `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C (`GmresSolver<OperType>::Mult`, `iterative.cpp:543-705`).
```

For `constructed-operators.md:220` (prose) + `:224` (bullet):
```edit:book/src/concepts/constructed-operators.md
re-inspects `side`. See [gmres slice](../spec/slices/gmres.md).
```
replace with:
```text
re-inspects `side`. See the firm [`krylov-step` (GMRES instance)](../L2/krylov-step.md).
```

```edit:book/src/concepts/constructed-operators.md
- [gmres](../spec/slices/gmres.md) — preconditioner side via `apply_BA`.
```
replace with:
```text
- [`krylov-step` (GMRES instance)](../L2/krylov-step.md) — preconditioner side via `apply_BA`.
```

For `derived-view-hoisting.md:16` (prose worked-example anchor):
```edit:book/src/concepts/derived-view-hoisting.md
In [CG L4](../spec/slices/cg.md) the residual norm `res = sqrt|beta|` is a derived view of the iteration's stored inner product `beta`. Two design choices:
```
replace with:
```text
In the firm [`krylov-step` (CG instance)](../L2/krylov-step.md) the residual norm `res = sqrt|beta|` is a derived view of the iteration's stored inner product `beta`. Two design choices:
```

For `first-iteration-unrolling.md:9` (prose) + `:77` (bullet):
```edit:book/src/concepts/first-iteration-unrolling.md
- **CG / PCG**: `p_k = r_k + (β_k/β_{k-1})·p_{k-1}` for `k ≥ 1`, with `p_0 = r_0` (no `β_{-1}`). See [`cg slice`](../spec/slices/cg.md) §L4 v0.5.
```
replace with:
```text
- **CG / PCG**: `p_k = r_k + (β_k/β_{k-1})·p_{k-1}` for `k ≥ 1`, with `p_0 = r_0` (no `β_{-1}`). See the firm [`krylov-step` (CG instance)](../L2/krylov-step.md) + [`L4/krylov-step`](../L4/krylov-step.md) Form B.
```

```edit:book/src/concepts/first-iteration-unrolling.md
- [`cg`](../spec/slices/cg.md) §L4 v0.5 — first slice to adopt.
```
replace with:
```text
- [`krylov-step` (CG instance)](../L2/krylov-step.md) — CG L4 v0.5 (firm-homed at [`L4/krylov-step`](../L4/krylov-step.md) Form B) was the first form to adopt the unrolling.
```

For `L0/ksp-factory-file.md:56` (TWO links on one line → firm L2/L1 homes):
```edit:book/src/L0/ksp-factory-file.md
The solver classes themselves (`CgSolver`, `GmresSolver`, `FgmresSolver`) live in `palace/linalg/iterative.{hpp,cpp}` and are the L2 / L1 anchors for [`spec/slices/cg`](../spec/slices/cg.md) and [`spec/slices/gmres`](../spec/slices/gmres.md).
```
replace with:
```text
The solver classes themselves (`CgSolver`, `GmresSolver`, `FgmresSolver`) live in `palace/linalg/iterative.{hpp,cpp}` and are the L0 anchors for the firm [`L2/krylov-step`](../L2/krylov-step.md) kernel + [`L1/ksp_solve`](../L1/ksp_solve.md) / [`L2/ksp_solve`](../L2/ksp_solve.md) outer driver.
```

## Step 4 — DELETE the 3 slice files (zero surviving inbound links confirmed)

After steps 1–2, the preflight grep returns zero `](..slice..)` links. Graded-stack reachability-GC detritus confirmed: the three slices carry no inbound `depends-on` frontmatter edge (only the navigational links + plain-text evidence mentions retired above). Propose deletion:

```delete:book/src/spec/slices/cg.md
```
```delete:book/src/spec/slices/gmres.md
```
```delete:book/src/spec/slices/arnoldi_step.md
```

## Step 5 — SUMMARY + spec/index removal; spec/index.md disposition

The corpus is now EMPTY (chebyshev was the prior reduction; these three were the last). **Producer decision: option (a) — remove `spec/index.md` entirely + the `# Phase 1 corpus` SUMMARY section + its link to `spec/index.md`.** Rationale: the corpus is gone; a stub `spec/index.md` would be a claim-free orphan with no referents, and graded-stack reachability-GC favors removing detritus over stubbing it. Git history is the record. **Flagged for critic: this is a producer judgment (lean-(a)); if the critic prefers (b) a one-line "corpus fully lifted; see git history" stub, that is a clean fallback.**

**Inbound `](spec/index.md)` link census (run before deleting spec/index.md):** `grep -rnoE '\]\([^)]*spec/index\.md\)' book/src` returns exactly TWO live links — `SUMMARY.md:291` and `introduction.md:23`. Both removed/repointed below. (All `book/src/meta-reviews/*` + `concepts/variant-absorption.md:103` references are PROSE inline-code `book/src/spec/index.md`, NOT `](` links — they stay true after deletion, frozen historical narration.)

**(5a) SUMMARY.md — remove the whole `# Phase 1 corpus` Part** (exact on-disk text, verified lines 290-294):
```edit:book/src/SUMMARY.md
# Phase 1 corpus (slice-vertical; raw material for combinator extraction)
- [Index — Slice Status](./spec/index.md)
  - [Arnoldi step](./spec/slices/arnoldi_step.md)
  - [CG — Preconditioned Conjugate Gradient](./spec/slices/cg.md)
  - [GMRES](./spec/slices/gmres.md)
```
replace with:
```text
```
(This removes the entire now-empty Phase-1-corpus Part: header + `[Index — Slice Status]` parent link + the three slice children. The blank line between this Part and the following `# Concepts (shared library)` Part is preserved by the surrounding context.)

**(5b) introduction.md:23 — remove the now-dangling navigation bullet** (the slice-status table it pointed to is gone):
```edit:book/src/introduction.md
- [Specification → Slice Status](./spec/index.md) — the table of slices and how far each has been pushed up the stack.
- [Concepts](./concepts/index.md) — shared primitives and abstract concepts referenced across multiple slices.
```
replace with:
```text
- [Concepts](./concepts/index.md) — shared primitives and abstract concepts referenced across multiple slices.
```

**(5c) Delete spec/index.md:**
```delete:book/src/spec/index.md
```

**Linkcheck2 guard:** removing `spec/index.md` requires removing BOTH live inbound links (`SUMMARY.md:291`, `introduction.md:23`) — done in 5a/5b. Integrator should re-confirm `grep -rnoE '\]\([^)]*spec/index\.md\)' book/src` returns nothing after apply, and `grep -rnoE '\]\([^)]*slices/(cg|gmres|arnoldi_step)\.md' book/src` returns nothing (zero surviving slice links) before the three deletes land.

## Supporting evidence

- **Firm GMRES L0 home:** `book/src/L1-L0/ksp-solve-mutation-rotation.md:371-441` (Sub-pattern C, `GmresSolver<OperType>::Mult` `iterative.cpp:543-705`; outer restart loop + inner Arnoldi loop `iterative.cpp:563-683`). Verified: `iterative.cpp:543-705 --anchor GmresSolver` → `[ok]` (anchor at 544/548/550); `iterative.cpp:563` = `for (; it < max_it; restart++)`, `:683` = `}` (restart-loop close).
- **Firm CG L0 home:** Sub-pattern B (`iterative.cpp:360-486`, kernel for-loop `:427-464`).
- **Firm MGS-obstruction home:** `book/src/concepts/sequential-obstruction.md` §"MGS as sequential-obstruction" (`:37-`) + §Examples (`:18-24`, GMRES `ls_update_column`/`back_solve`/MGS catalog).
- **Firm CG-Form-B home:** `book/src/L4/krylov-step.md` Form B (D1's cycle-099 absorption of `cg.md:27-141`).
- **Arnoldi reconcile:** `reference/palace/palace/linalg/iterative.cpp:72` template, `:73` real-form `GeneratePlaneRotation` signature, `:109` real-form body-close `}`, `:111` complex `std::complex<T>` overload begins. `:73-109 --anchor GeneratePlaneRotation` → `[ok]`. Confirms `:73-118` over-runs into the complex specialization; `:73-109` is canonical.
- **CG/GMRES/Arnoldi as canonical instances of the firm `L2/krylov-step`:** `book/src/L2/krylov-step.md:7` (the §Context names exactly CG / GMRES / Chebyshev / Arnoldi as the five pattern instances).

## Open questions / caveats

- **Campaign COMPLETE (corpus 3→0) — flag for integrator-finalize / batch-31 meta-phase.** On apply, `book/src/spec/slices/` is empty and `spec/index.md` is removed. Per the dispatch directive: **retire the `annotated-and-retained` carve-out** (CLAUDE.md §Methodology invariants "Phase 1 corpus reduces as material is lifted" canonical-instance carve-out) and **retire skill `phase-1-slice-reduction-audit`** (no corpus left to audit). The graded-stack `roadmap_goal` rank-0 chapter is now the in-discipline replacement for `annotated-and-retained`.
- **`L2/index.md:89` D3-flag — verified NON-STALE, no fix.** The "bilinear-form × rough-in co-mention" is the `inner_product` dep-map row reading `bilinear-form (M-weighted member, firm — promoted cycle-095)`. It says **firm**, not rough-in. D3's plausibly-non-stale judgment confirmed; left untouched.
- **`L2/index.md:131-134` dep-map pattern-instance sub-list** — repointed in step 1a (these are plain-text slice-range mentions in the L2 index, in my scope per the dispatch's `L2/index.md` listing). No table-row or cohort-bullet count changes (no operators added/removed); the running-count tally is untouched.
- **SUMMARY/introduction exact-text:** the step-5 removal blocks reproduce the EXACT on-disk text (verified: `SUMMARY.md:290` header `# Phase 1 corpus (slice-vertical; raw material for combinator extraction)`, parent `- [Index — Slice Status](./spec/index.md)`; `introduction.md:23` nav bullet). The three `spec/index.md:15-17` Class-A corpus rows vanish with the file delete (5c) — no separate row edit needed.
- **Second live inbound link to `spec/index.md` found + handled:** `introduction.md:23` (`[Specification → Slice Status](./spec/index.md)`) — would have been a dangling-link linkcheck2 hard error if I'd deleted spec/index.md without it. Removed in 5b. (This is the analog of the c098 missed-inbound-links lesson, applied to the spec/index.md deletion rather than the slice deletion.)
- **spec/index.md disposition is a producer judgment (lean-(a) full removal).** Surfaced for critic ratification; (b) one-line stub is the clean fallback if the critic prefers retaining a tombstone. Either keeps linkcheck2 green (both inbound links — `SUMMARY.md:291` + `introduction.md:23` — removed in step 5).
- **Build-critical completion is FULL; one residue is tracked.** The campaign's mechanical-completion criterion IS met: all 25 Class-A markdown links + all 6 corpus rows repointed/removed (zero surviving inbound `](..slice..)` and `](spec/index.md)` links — critic-simulated-clean), the arnoldi end-bound reconciled, the 3 slice files deleted, SUMMARY `# Phase 1 corpus` Part + `spec/index.md` removed, slices reachability-GC-unreachable, rank invariant holds with zero slice nodes. **Scoped correction (repairer, cycle-099):** the earlier "all Class-B mentions repointed / FULL completion / no partial" phrasing OVERSTATED the Class-B coverage — this dispatch repoints only a subset of the plain-text (non-link) slice-range mentions. **~50 plain-text slice-range evidence-provenance mentions remain** across firm chapters (8+ in `L2/krylov-step.md`: `:7`, `:58`, `:69`, `:79`, `:81`, `:86`, `:117`, `:120`, `:121`, `:172`; also D1-owned `L4/krylov-step.md:105/152/170/171`; `L2-L1/krylov-step-kernel-defusion.md`; `L4/iterate-while*.md`). Many are deliberate frozen "Original pre-reduction slice ranges" historical narration (same KIND as the `meta-reviews/*` convention). **None break the build** (plain text resolves to nothing on deletion). See the dedicated follow-up item below.
- **TRACKED FOLLOW-UP for batch-31 meta-phase — residual Class-B plain-text-mention cleanup.** ~50 plain-text slice-range mentions (`(cg|gmres|arnoldi_step)\.md:[0-9]` non-link occurrences; census `grep -rnE '(cg|gmres|arnoldi_step)\.md:[0-9]' book/src --include='*.md' | grep -vE '\]\('`) survive in firm chapters as stale-but-harmless pointers to the now-deleted slices. They do NOT gate the campaign's mechanical completion (build-critical = the markdown-link set, which IS complete). The batch-31 meta-phase should MIGRATE this into the plan and decide: **(a)** a dedicated Class-B plain-text-mention cleanup pass into batch-32 (repoint each to its firm home), or **(b)** accept-as-historical-provenance (the `meta-reviews/*` frozen-historical-mention convention), possibly per-mention. Either way the build stays green.
