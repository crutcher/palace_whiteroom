---
agent: lowering-verifier
invoked_at: 2026-06-07T093000Z
scope: cycle-122 D6 — TWO DIRECTIVE-3 kernel-API/impl correspondence audits (libceed + eigsolve)
status: pending
inputs:
  - book/src/L1/libceed-quadrature-kernel-impl.md (kernel-impl, roadmap_goal)
  - book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md (kernel-api, obstruction opaque-library-ownership)
  - book/src/L3/eigsolve-impl.md (kernel-impl, roadmap_goal)
  - book/src/L3/eigsolve.md (kernel-api, partial-obstruction)
  - reports/2026-06-07T071941Z-harvester-libceed-substrate-ops/CYCLE.md (D4 — the now-resolved 4 substrate ops)
  - reports/2026-06-07T071941Z-cycle-planner-cycle-122/CYCLE.md (D6 row)
  - reference/palace (slepc.cpp, arpack.cpp, fem/libceed/integrator.{cpp,hpp}, fem/bilinearform.cpp, fem/integrator.hpp, fem/libceed/operator.cpp, test/unit/test-libceed.cpp)
integrated_at: 2026-06-07T071941Z
integration_commit: 17cdafe9d9515c72045691b07420fbdfa25af81a
integration_notes: "cycle-122 D6. Applied clean. verified_against: blocks appended to libceed-quadrature-kernel-impl (8) + eigsolve-impl (7); D4-confirmed stale-prose re-anchor on the libceed impl. realizes-kernel-api edges + kernel-api statuses confirmed unchanged. 0 gate hits. See reports/cycle-122-integrator-staging/STAGING.md."
---

# CYCLE: Audit the libceed + eigsolve realizes-kernel-api correspondences (DIRECTIVE-3 standing integrity gate)

## Summary

Two DIRECTIVE-3 kernel-API/impl correspondence audits, both **STRUCTURAL** reviews (both impls are
rank-0 `roadmap_goal`, so the `empirical-match` justification is correctly deferred to firming — the
audit's question is "does the sketched constructive pipeline faithfully match the opaque-API contract,
and is the linkage structurally well-formed?", not "does it compute bit-identical output today?").

- **(A) libCEED** `L1/libceed-quadrature-kernel-impl` (kernel-impl) ↔ `L1-L0/fe-assemble-libceed-boundary-obstruction` (kernel-api):
  **VERDICT — FAITHFUL (structural correspondence holds; linkage well-formed; API status preserved).**
  The constructive `A = Gᵀ B_𝒟ᵀ D B_𝒟 G` five-stage pipeline genuinely realizes the opaque libCEED
  element-quadrature leaf the API documents; the five stages map exactly onto the API's leaf-kernel
  signature (`integrator.hpp:58-61`) and the Palace operator-field wiring (`integrator.cpp:423-445`).
  The `realizes-kernel-api` edge is `reference`-class (NOT depends-on). The API stays `obstruction
  (opaque-library-ownership)`, undowngraded. All impl L0 anchors verify against `reference/palace`.
  **One STALE-PROSE finding (D4-flagged, confirmed):** the consumer's frontmatter `depends-on` NOTE
  comment (lines 33-39) and the "Speculative L1 operators (rough-in; ...)" section (lines 166-177) call
  the four substrate targets "rough-in; no anchor yet" — they are now `roadmap_goal` (authored c122 D4,
  with anchors). Route as a navigational re-anchor for the integrator/repairer (D4 deliberately did not
  edit to avoid the same-file collision the planner flagged SEQUENTIAL).

- **(B) eigsolve** `L3/eigsolve-impl` (kernel-impl) ↔ `L3/eigsolve` (kernel-api, partial-obstruction):
  **VERDICT — FAITHFUL (structural correspondence holds; linkage well-formed; API status preserved).**
  The constructive thick-restart Krylov-Schur driver + inner basis-extension loop + Rayleigh-Ritz
  extraction genuinely realizes the opaque SLEPc `EPSSolve` / ARPACK `naupd` RCI loop the API records
  as a `sequential-obstruction`. The decisive evidence `slepc.cpp:635 EPSSetType(eps, EPSKRYLOVSCHUR)`
  verifies EXACTLY — the default opaque eigen-iteration IS Krylov-Schur, the algorithm the impl
  reconstructs. The impl correctly **preserves the obstruction** (it constructs what the loop *would*
  be, it does not claim Palace authors a loop). The `realizes-kernel-api` edge is `reference`-class; the
  sibling `realizes-kernel-api → L4/eigsolve` is too. The API stays `partial-obstruction`, undowngraded.
  Well-foundedness holds (rank-0 impl on firm constituents + rank-0 `lanczos_step`). All Palace anchors
  verify. **Minor anchor nit:** the impl's ARPACK `ido==99` break citation `:330-333` is off-by-one on
  the END (the `ido==99` block is `:331-334`, break at `:333` is in-range) — non-load-bearing, noted.

Net: both correspondences are GO; both API surfaces correctly retain their obstruction disposition;
both `realizes-kernel-api` edges are correctly `reference`-class; the four roadmap_goal impl nodes rest
well-foundedly on their (roadmap_goal/firm) substrate. The DIRECTIVE-3 dual-surface integrity holds for
both kernels. I append a `verified_against:` correspondence-audit block to EACH impl (proposed-changes),
and route the one stale-prose re-anchor.

---

## (A) libCEED correspondence audit

### Per-citation audit (impl L0 anchors against reference/palace)

All anchors verified by direct on-disk `awk` read of `reference/palace/palace/...` (the doubled
`palace/palace/` source tree). Path convention confirmed: source files cite `palace/fem/...`
(→ `reference/palace/palace/fem/...`); test files cite `palace/test/...`
(→ `reference/palace/test/...`, SINGLE `palace/` — the test tree is NOT doubled).

- **Citation**: `palace/fem/libceed/integrator.cpp:423-445` (impl §Verified-against; "AssembleCeedOperator master assembler signature")
  - **Theme claim**: the master assembler with inputs `trial_restr/test_restr/trial_basis/test_basis/geom_data/geom_data_restr` — the five inputs that wire `Gᵀ Bᵀ D B G`.
  - **Found**: `:423` `void AssembleCeedOperator(... CeedElemRestriction trial_restr, CeedElemRestriction test_restr, CeedBasis trial_basis, CeedBasis test_basis, CeedVector geom_data, CeedElemRestriction geom_data_restr, CeedOperator *op)` (signature `:423-427`). Exact match.
  - **Verdict**: supports.

- **Citation**: `palace/fem/libceed/integrator.cpp:451-512` (apply-QFunction + operator-field wiring; `geom_data` input, `q_w`, active in/out fields)
  - **Theme claim**: the `B G` (input) / `Bᵀ Gᵀ` (output) field chains around the pointwise `D`; `geom_data` input, optional `q_w` quad-weight, `AddOperatorActiveInputFields :492` / `AddOperatorActiveOutputFields :493`.
  - **Found**: `geom_data` input `CeedQFunctionAddInput(apply_qf, "geom_data", ..., CEED_EVAL_NONE)` `:457-458`; `q_w` `CEED_EVAL_WEIGHT` `:462`; `AddOperatorActiveInputFields(...)` `:492`, `AddOperatorActiveOutputFields(...)` `:493`. (Impl cites the `q_w` sub-line as `:459-462`; on disk the AddInput spans `:460-463` within the `info.trial_ops & EvalMode::Weight` guard `:460-463` — in-range, the cited block is the right region.)
  - **Verdict**: supports.

- **Citation**: `palace/fem/libceed/integrator.cpp:340-419` (build-QFunction `f_build_geom_factor_*`; `grad_x` Jacobian, `q_w` weight, `geom_data` output)
  - **Theme claim**: geometry factor from `grad_x` (Jacobian, `CEED_EVAL_GRAD` :390) × quad weight (`q_w`, `CEED_EVAL_WEIGHT` :388) → `geom_data` (:397) — the `geom_factor_build` stage.
  - **Found**: `attr` `CEED_EVAL_INTERP` `:387`; `q_w` `CEED_EVAL_WEIGHT` `:388`; `grad_x` `space_dim*dim` `CEED_EVAL_GRAD` `:389-390`; `MFEM_VERIFY(geom_data_size == 2 + space_dim * dim, ...)` `:395-396`; `CeedQFunctionAddOutput(build_qf, "geom_data", ...)` `:397`. Exact.
  - **Verdict**: supports.

- **Citation**: `palace/fem/libceed/integrator.cpp:215-308` (`QuadratureDataAssembly` + `f_apply_*` pointwise kernels — the `D` per-quad-point contraction)
  - **Found**: `void QuadratureDataAssembly(...)` begins at `:220` (within the cited `:215-308` range). Supports (the cited range start `:215` is two lines before the function head — a range bound, not drift).
  - **Verdict**: supports.

- **Citation**: `palace/fem/libceed/integrator.hpp:14-23` (`enum EvalMode { Weight, None, Interp, Grad, Div, Curl }`)
  - **Found**: `:15-23` `enum EvalMode : unsigned int { Weight = 1<<0, None = 1<<1, Interp = 1<<2, Grad = 1<<3, Div = 1<<4, Curl = 1<<5 }`. Exact match (the comment header is at `:14`).
  - **Verdict**: supports.

- **Citation**: `palace/fem/integrator.hpp:58-61` (`BilinearFormIntegrator::Assemble` pure-virtual leaf-kernel contract)
  - **Theme claim (impl AND api)**: the boundary the obstruction theme documents; the dispatch this impl realizes.
  - **Found**: `:58-61` `virtual void Assemble(Ceed ceed, CeedElemRestriction trial_restr, CeedElemRestriction test_restr, CeedBasis trial_basis, CeedBasis test_basis, CeedVector geom_data, CeedElemRestriction geom_data_restr, CeedOperator *op) const = 0;`. Exact — and this is THE shared anchor: the impl's `A(space,term)` signature and the API's documented leaf contract are the SAME `Assemble` pure-virtual. The correspondence pivots on this line.
  - **Verdict**: supports (decisive shared anchor).

- **Citation**: `palace/fem/bilinearform.cpp:64-70` (Palace-supplied restriction/basis inputs `trial_restr :64`, `test_restr :66`, `trial_basis :68`, `test_basis :69`)
  - **Found**: `:64-69` exactly as cited (`GetCeedElemRestriction` `:64-67`, `GetCeedBasis` `:68-69`); the leaf call `integ->Assemble(...)` `:75`; the fold `op->AddSubOperator(sub_op)` `:77`. Exact.
  - **Verdict**: supports.

### Theme claim ↔ kernel-API contract correspondence

The API surface (`fe-assemble-libceed-boundary-obstruction`) documents the contract: the per-term leaf
`A(term_i)` is built by `integ->Assemble` (pure-virtual `integrator.hpp:58-61`) producing an opaque
`CeedOperator` that "encapsulates the element-local quadrature contraction — basis evaluation at
quadrature points, the geometric-factor / coefficient weighting, and the contract-back to element dofs"
(API §"libCEED-owned (leaf)" lines 109-126). The impl decomposes EXACTLY that contract:

| kernel-API contract (the opaque `Assemble`→`CeedOperator`) | kernel-impl stage (`A = Gᵀ B_𝒟ᵀ D B_𝒟 G`) |
|---|---|
| "contract-back to element dofs" / restriction inputs `trial_restr`/`test_restr` (`bilinearform.cpp:64-66`) | **G / Gᵀ** `element_restrict` — the gather/scatter-add |
| "basis evaluation at quadrature points" / basis inputs `trial_basis`/`test_basis` (`:68-69`) | **B / Bᵀ** `basis_apply` — keyed on the `EvalMode` the term's `𝒟` selects (`integrator.hpp:14-23`) |
| "geometric-factor / coefficient weighting" (the pointwise quad contraction) | **D** `quad_point_contract` — pointwise `geom_data ⊙ ·` (`integrator.cpp:451-512`) |
| `geom_data`/`geom_data_restr` inputs (`integrator.hpp:60` / `bilinearform.cpp:76`) | **geom_factor_build** — the build-QFunction (`integrator.cpp:340-419`) producing `geom_data` |
| COO→CSR full-assembly materialization (`CeedOperatorAssembleCOO`, `operator.cpp:483`) | the impl's "full assembly materializes `A` by applying the pipeline to the identity columns" (impl L1-form lines 134-138) |

The impl's five stages are in 1:1 structural correspondence with the API's documented leaf-kernel field
roles — **the impl genuinely realizes the API contract** (a faithful from-our-primitives version of the
opaque boundary). The decomposition is read directly off `AssembleCeedOperator` (impl §Justification
"structural"; not reconstructed from negative anchors), which I confirmed at `integrator.cpp:423-445`.

### Linkage integrity (the DIRECTIVE-3 invariant checks)

1. **`realizes-kernel-api` edge is `reference`-class (NOT depends-on)?** **YES.** Impl frontmatter
   `edges.reference[0]: target: L1-L0/fe-assemble-libceed-boundary-obstruction, kind: realizes-kernel-api`
   (lines 20-21). It is under `reference:`, not `depends-on:`. The impl's `depends-on:` block (lines
   26-40) lists ONLY the four substrate ops — NOT the opaque API. **The impl does not block on the
   opaque API.** Correct.
2. **API surface stays its obstruction status (NOT downgraded)?** **YES.** API frontmatter
   `status: obstruction`, `sub_kind: opaque-library-ownership` (lines 4-5); §Status line 30
   `obstruction (opaque-library-ownership) — kernel-api`. The role-label is additive; the disposition
   is intact. The API explicitly states (line 36-37) "The role-label does NOT change the obstruction
   disposition." Correct.
3. **API keeps `fe_assemble` firm (no downgrade of the fold)?** **YES.** API §"`fe_assemble` stays
   FIRM" (lines 48-63) is intact; the impl's `realizes-leaf → L1/fe_assemble` edge is `reference`-class
   (line 22-23) and the impl §Status (lines 79-82) confirms `fe_assemble` "does not depend on this
   impl." Correct.
4. **Well-foundedness (rank-0 impl on its substrate)?** **YES (vacuous, correct).** Impl is
   `rank: roadmap_goal` (line 17). Its four `depends-on` substrate targets are authored `rank:
   roadmap_goal` by D4 (confirmed in D4's report frontmatter blocks). `rank(impl=0) ≤ rank(substrate=0)`
   holds vacuously — a rank-0 node may rest on anything. The consumer correctly STAYS roadmap_goal
   (cannot exceed its least-resolved dep). This is the intended grounded-future state, not a defect.

### Empirical-anchor readiness (deferred to firming, but the anchor exists and is strong)

The empirical-match justification is correctly DEFERRED (impl is roadmap_goal). I nonetheless verified
the empirical anchor the D6 row + D4 name, so the future firming audit has a confirmed target:
`test/unit/test-libceed.cpp:284` `TestCeedOperatorFullAssemble` EXISTS on disk
(`reference/palace/test/unit/test-libceed.cpp:284`), and `:298` asserts
`mat_diff->MaxNorm() < 1.0e-12 * std::max(mat_ref.MaxNorm(), 1.0)` — the assembled libCEED matrix
matches the MFEM reference to 1e-12. This is exactly the empirical-match the correspondence will rest on
at firming. (NOTE the path convention: this is `palace/test/...` = SINGLE `palace/` under `reference/`,
NOT the doubled `palace/palace/` source path — D4's citation `palace/test/unit/test-libceed.cpp:284` is
CORRECT relative to `reference/`.)

### libCEED findings

- **FAITHFUL** — the structural correspondence holds; the impl realizes the API contract stage-for-stage.
- **STALE PROSE (route to integrator/repairer, D4-confirmed)** — the consumer
  `libceed-quadrature-kernel-impl.md` frontmatter `depends-on` NOTE comment (lines 33-39: each target
  tagged "(rough-in; no anchor yet)") and the body §"Speculative L1 operators (rough-in; harvester
  promotion targets)" (lines 166-177) describe the four substrate ops as "rough-in; no anchor yet." As
  of D4 they are `roadmap_goal` chapters WITH codemap-verified anchors. This is a navigational text
  refresh (not a claim change): re-anchor to "roadmap_goal (authored c122 D4)". I did NOT edit the file
  (it is my audit target; the planner marked D4↔D6 SEQUENTIAL same-file; the `verified_against:` block I
  append is the only impl-file edit I propose, and it is append-only at end-of-file). See Proposed
  changes Note-1.

---

## (B) eigsolve correspondence audit

### Per-citation audit (impl Palace anchors against reference/palace)

- **Citation**: `palace/linalg/slepc.cpp:630-654` — `SlepcEPSSolverBase::SetType`; **the decisive `:635 EPSSetType(eps, EPSKRYLOVSCHUR)`**
  - **Theme claim** (impl §Intent line 48, §Evidence line 142): the decisive evidence that the default opaque eigen-iteration IS Krylov-Schur — the algorithm this impl reconstructs.
  - **Found**: `:634 case Type::KRYLOVSCHUR:` → `:635 PalacePetscCall(EPSSetType(eps, EPSKRYLOVSCHUR));`. Also `EPSPOWER :638`, `EPSSUBSPACE :641`, `EPSJD :644`; the `TOAR/STOAR/QARNOLDI/SLP/NLEIGS` arm `MFEM_ABORT(...)` `:652`. EXACT match — `:635` lands precisely on `EPSSetType(eps, EPSKRYLOVSCHUR)`.
  - **Verdict**: supports (DECISIVE — this is the anchor the whole impl-algorithm choice rests on; zero drift).

- **Citation**: `palace/linalg/slepc.cpp:687-709` — `SlepcEPSSolverBase::Solve`; the opaque `EPSSolve(eps)`
  - **Theme claim**: the kernel-api's "no Palace loop" anchor — what the impl's outer driver realizes; `Customize() :693`, `EPSSolve(eps) :694`, `EPSGetConverged :695`, `RescaleEigenvectors :707`.
  - **Found**: `:693 Customize();`, `:694 PalacePetscCall(EPSSolve(eps));`, `:695 EPSGetConverged(eps, &num_conv)`, `:707 RescaleEigenvectors(num_conv)`. Exact.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/slepc.cpp:731-736` — `GetBV`; `EPSGetBV(eps, &bv) :734`
  - **Found**: `:734 PalacePetscCall(EPSGetBV(eps, &bv));`. Exact (impl cites `:734`).
  - **Verdict**: supports.

- **Citation**: `palace/linalg/slepc.cpp:602-628` — `SetProblemType`; `EPS_HEP :607` etc.
  - **Found**: `EPS_HEP :607`, `EPS_NHEP :610`, `EPS_GHEP :613`, `EPS_GHIEP :616`, `EPS_GNHEP :619`. Exact (the `problem-symmetry` axis source — selects `lanczos_step` Hermitian vs `krylov-step` non-Hermitian).
  - **Verdict**: supports.

- **Citation**: `palace/linalg/arpack.cpp:318` — `naupd(...)` RCI basis-iteration driver; `:315-339` callback loop
  - **Found**: `:315 while (true)` → `:318 naupd(fcomm, ido, ...)` → `:323 if (ido == 1 || ido == -1)` dispatching `:325 ApplyOp(...)`, `:327 else if (ido == 2)` → `:329 ApplyOpB(...)`, `:331 else if (ido == 99)` → `:333 break;`. The `naupd :318` and the loop `:315-339` are exact.
  - **Verdict**: supports. **Minor nit**: the impl (eigsolve-impl line — not present; the API entry `eigsolve.md` and the impl both phrase "breaking on `ido == 99` (`:330-333`)") — the `ido==99` block is `:331-333`/`:334`, with `break;` at `:333`. The cited range `:330-333` starts one line early (`:330` is the close-brace of the `ido==2` block). NON-LOAD-BEARING (the `break` at `:333` IS in-range); flag as a 1-line range-start nicety, not a drift on a load-bearing anchor.

- **Citation**: `palace/linalg/arpack.cpp:270, :273, :278`
  - **Found**: `:270 iparam[2] = (a_int)arpack_it;  // Maximum number of Arnoldi iterations`; `:273 iparam[6] = sinvert ? 3 : 1;  // Problem mode`; `:278 ::arpack::which which_option = ::arpack::which::largest_magnitude;`. Exact.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/arpack.cpp:369` — `neupd(...)` post-iteration extraction; `:342 num_it`
  - **Found**: `:369 neupd(fcomm, rvec, howmny_option, ...)`; `:342 int num_it = (int)iparam[2];`. Exact.
  - **Verdict**: supports.

### Theme claim ↔ kernel-API contract correspondence

The API surface (`L3/eigsolve`, partial-obstruction) records: the per-step body `apply_shift_invert =
apply_linop(op.operand) ▷ ksp_solve(op.inv) ▷ scale_untransform [▷ project]` **lifts** (whole-tensor,
identity-in-form to firm L2), but the **eigen-iteration loop does NOT lift** — it is a witnessed
`sequential-obstruction` rooted in opaque-library-ownership ("there is no Palace-authored eigen-step
kernel / eigen-iteration driver pair analogous to `(krylov-step, ksp_solve)`"). The impl constructs
exactly that missing pair. The impl's own correspondence table (eigsolve-impl lines 102-109) maps:

| kernel-API (`L3/eigsolve`) | kernel-impl (`eigsolve-impl`) | my verification |
|---|---|---|
| `apply_shift_invert op v` (body; LIFTS) | inner `krylov-step`/`lanczos_step` body — verbatim `apply_linop ▷ ksp_solve ▷ scale_untransform`, then `orthogonalize` | The API's body (eigsolve.md §Signature lines 52-63) and the impl's inner step (eigsolve-impl lines 86-96) are the SAME three-stage composition. Faithful. |
| `eigen_iterate op st0 apply_shift_invert` (OPAQUE fold; obstruction) | `iterate_while_L3` thick-restart driver ▷ inner basis-extension loop (CONSTRUCTED) | The impl replaces the opaque fold with an authored loop while **preserving the obstruction marker** (eigsolve-impl lines 110-111). Faithful — it does not claim Palace authors a loop. |
| SLEPc `EPSSolve`/`EPSKRYLOVSCHUR` (`slepc.cpp:694`,`:635`) | outer thick-restart driver realizing Krylov-Schur | `:635 EPSKRYLOVSCHUR` verified EXACTLY → the impl's Krylov-Schur choice is grounded in the decisive anchor. |
| ARPACK `naupd` RCI driver (`arpack.cpp:318`); `iparam[2]` (`:270`) | inner basis-extension loop to dim `ncv` | `naupd :318` + `iparam[2] :270` verified. Faithful. |
| SLEPc `BV` (`slepc.cpp:734 EPSGetBV`) | the `BV : Tensor[(B: ncv), (S: ...), complex]` basis carry | `EPSGetBV :734` verified. Faithful. |
| `extract_eigpairs` (`slepc.cpp:715 l*gamma`) / ARPACK `neupd` (`:369`) | `rayleigh_ritz` + `extract_eigpairs` (`λ = σ + 1/θ`; Higham un-scale) | `:715 return l * gamma` + `neupd :369` verified. Faithful. |

**The impl genuinely realizes the API contract.** Critically, it does so the RIGHT way for a
partial-obstruction API: it constructs the loop the library owns ("here is the loop rendered in our
vocabulary, IF we were to author it instead of calling the library") while leaving the API's obstruction
disposition intact. The impl §"Correspondence" (lines 110-111) explicitly states "The impl preserves
the obstruction the api records — it does not dissolve it" — which is the correct DIRECTIVE-3 posture.

### Linkage integrity (the DIRECTIVE-3 invariant checks)

1. **`realizes-kernel-api` edge is `reference`-class (NOT depends-on)?** **YES.** Impl frontmatter
   `edges.reference` carries `target: L3/eigsolve, kind: realizes-kernel-api` (lines 20-21) AND
   `target: L4/eigsolve, kind: realizes-kernel-api` (lines 22-23) — both under `reference:`. The impl's
   `depends-on:` block (lines 8-18) lists ONLY firm/roadmap_goal constituents (`krylov-step`,
   `lanczos_step`, `ksp_solve`, `apply_linop`, `orthogonalize`) — NOT the opaque API. The impl does not
   block on the opaque API. Correct. (The impl §Pulled-by lines 121 EXPLICITLY notes the
   `realizes-kernel-api` edge is reference-class/free so does not carry liveness — exemplary self-aware
   linkage discipline.)
2. **API surface stays `partial-obstruction` (NOT downgraded)?** **YES.** API frontmatter
   `firmness: partial-obstruction` (line 4); §Status line 191 `partial-obstruction — kernel-api` with
   the explicit "The `partial-obstruction` status is UNCHANGED — the loop is genuinely
   opaque-library-owned; the impl constructs what the loop *would* be, it does not make this node's loop
   non-opaque." Correct.
3. **Well-foundedness (rank-0 impl on its constituents)?** **YES.** Impl `rank: roadmap_goal` (line 6).
   Its `depends-on` constituents verified on disk: `L3/krylov-step` firm, `L3/ksp_solve` firm,
   `L3/apply_linop` firm, `L2/orthogonalize` firm (rank 3), plus the co-cycle `L3/lanczos_step`
   roadmap_goal (rank 0, confirmed `rank: roadmap_goal`). `rank(impl=0) ≤ min(deps)` holds (0 ≤
   everything). A rank-0 node may rest on anything, incl. firm AND other rank-0 nodes. The graded-stack
   linter reports **0 rank violations** with all three (eigsolve-impl, lanczos_step,
   libceed-quadrature-kernel-impl) as `[GARBAGE*]` — the intended grounded-future disposition (only
   inbound is the free `realizes-kernel-api` reference edge, awaiting the c122/c123 blocking consumers
   RE3 deflate / RE8 krylov-iteration). Correct.
4. **Obstruction PRESERVED on the impl's own loops?** **YES.** The impl classifies its OWN inner
   basis-extension + outer thick-restart loops as each a `sequential-obstruction` (eigsolve-impl line
   111; `edges.reference → concepts/sequential-obstruction` line 26). It does not launder the
   obstruction away by constructing it. Correct.

### eigsolve findings

- **FAITHFUL** — the structural correspondence holds; the impl realizes the API's opaque Krylov-Schur
  loop in our `(krylov-step, ksp_solve)` vocabulary, with the decisive `slepc.cpp:635 EPSKRYLOVSCHUR`
  anchor verified exactly, and the obstruction correctly preserved.
- **MINOR ANCHOR NIT (non-load-bearing)** — the `ido==99` break range `:330-333` (appearing in both
  `eigsolve.md` §Evidence line 221 "breaking on `ido == 99` (`:330-333`)" and the impl's inherited
  framing) starts one line early; the `ido==99` block is `:331-334`, `break;` at `:333`. The break IS
  in-range so the claim is supported; flag only as a tidy-up for a future lifter (carry-forward
  `arpack.cpp:330-333` → `:331-334` for the `ido==99` block), NOT a finding that blocks the audit.
- **`realizes-leaf` label disposition (D6 row asks)** — the D6 row asks me to adjudicate the
  `realizes-leaf` label (keep distinct / fold into plain `reference` / reuse `realizes-kernel-api`).
  **Recommendation: KEEP DISTINCT, as documentation.** `realizes-leaf` (libceed-impl → `fe_assemble`)
  and `realizes-kernel-api` (impl → obstruction API) carry genuinely different semantics: the former is
  "I am the constructive interior of a firm fold's opaque LEAF"; the latter is "I correspond to a
  documented opaque-API CONTRACT." Both are `reference`-class and the linters ignore the `kind:` token
  (it is documentation), so the label choice is FREE and has zero linter blast radius. Keeping them
  distinct preserves reviewer-legible intent (a reader can tell "realizes a firm fold's leaf" from
  "realizes an obstruction-API contract"). No relabel needed; this is a navigational/documentation
  nicety, deferrable to the meta if a uniform vocabulary is later wanted.

---

## Applicability conditions (both impls)

- **(A) libCEED impl applicability** (impl lines 140-154): (1) standard FE basis with a tabulated
  `CeedBasis`; (2) `𝒟 ∈ {Identity, Gradient, Curl, Divergence}`; (3) single-machine per-`Ceed` device.
  - **Verifiable?** Conditions (1)/(2) are verifiable against the firm `weak_form_term` de-Rham axis and
    `EvalMode` (`integrator.hpp:14-23`, verified). Condition (3) is the DIRECTIVE-1 single-machine
    boundary (read `ParMesh` single-rank) — consistent with project scope. **No counter-example found.**
    The GSLIB point-interp carve-out (impl line 147: a DIFFERENT facility, NOT realized here) is correct
    and consistent with the `interpolator` obstruction sibling.
- **(B) eigsolve impl applicability** (impl variant_axes lines 28-33): eigen-algorithm /
  problem-symmetry / spectral-transformation / problem-type / restart-shape.
  - **Verifiable?** The problem-symmetry axis (Hermitian → `lanczos_step` vs non-Hermitian →
    `krylov-step`) is grounded in `SetProblemType` `EPS_HEP/NHEP/GHEP/...` (`slepc.cpp:602-628`,
    verified). The eigen-algorithm axis (Krylov-Schur default) is grounded in `SetType`
    (`slepc.cpp:630-654`, verified). The spectral-transformation/problem-type axes are inherited from
    the kernel-api (eigsolve.md variant_axes). **No counter-example found.**

## Algebraic laws (both impls — sketched, deferred to firming)

Both impls correctly mark their laws "sketch — to be confirmed at promotion" / "SPECULATIVE
reconstruction" and DEFER `empirical-match` to firming (libceed impl §Justification "structural";
eigsolve-impl §Justification line 115 "empirical-match is deferred ... the lowering-verifier's c122
audit"). As a STRUCTURAL audit, I do not assert the laws hold on the operators (the operators are
roadmap_goal); I confirm only that the law SKETCHES are the standard restriction/basis/contraction
algebra (libceed) and the standard Krylov-Schur/Rayleigh-Ritz algebra (eigsolve), correctly flagged as
unconfirmed. This is the correct disposition for a rank-0 correspondence review. The decisive
syntactic-identity body law for eigsolve (`apply_shift_invert = apply_linop(M) ▷ ksp_solve ▷ ·×γ`) IS
already firm at the kernel-api (eigsolve.md law 1, read from `arpack.cpp:579-581`) — the impl inherits
it faithfully.

## Proposed changes

Append a `verified_against:` correspondence-audit block to EACH impl chapter (append-only, end of
file — the only impl-file edit this audit makes; the impls are my audit targets and remain
content-stable otherwise). The `note:` values are self-checked: no leading quote of either kind.

```edit:book/src/L1/libceed-quadrature-kernel-impl.md
[append at end of file]
```yaml
verified_against:
  - citation: book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md
    verdict: realizes-kernel-api-faithful
    audited_at: 2026-06-07T093000Z
    note: STRUCTURAL correspondence audit (impl is roadmap_goal; empirical-match deferred to firming). The five-stage A = Gᵀ B_𝒟ᵀ D B_𝒟 G pipeline maps 1:1 onto the kernel-api leaf contract (integrator.hpp:58-61 Assemble pure-virtual; restriction/basis/geom_data field roles). realizes-kernel-api edge confirmed reference-class (NOT depends-on); API stays obstruction(opaque-library-ownership), undowngraded; fe_assemble stays firm.
  - citation: reference/palace/palace/fem/libceed/integrator.cpp:423-445
    verdict: supports
    audited_at: 2026-06-07T093000Z
    note: AssembleCeedOperator master assembler signature with trial_restr/test_restr/trial_basis/test_basis/geom_data/geom_data_restr inputs (:423-427) — the five inputs wiring Gᵀ Bᵀ D B G; on-disk awk read, exact.
  - citation: reference/palace/palace/fem/integrator.hpp:58-61
    verdict: supports
    audited_at: 2026-06-07T093000Z
    note: BilinearFormIntegrator::Assemble pure-virtual leaf-kernel contract (= 0) — the SHARED anchor on which the impl-realizes-api correspondence pivots (the impl's A(space,term) IS the constructive interior of this opaque dispatch); exact.
  - citation: reference/palace/palace/fem/libceed/integrator.cpp:340-419
    verdict: supports
    audited_at: 2026-06-07T093000Z
    note: build-QFunction f_build_geom_factor_* — attr CEED_EVAL_INTERP (:387), q_w CEED_EVAL_WEIGHT (:388), grad_x CEED_EVAL_GRAD (:389-390), geom_data output + 2+space_dim*dim verify (:395-397); the geom_factor_build stage; exact.
  - citation: reference/palace/palace/fem/libceed/integrator.cpp:451-512
    verdict: supports
    audited_at: 2026-06-07T093000Z
    note: apply-QFunction/operator-field wiring — geom_data input (:457-458), q_w CEED_EVAL_WEIGHT (:462), AddOperatorActiveInputFields (:492) / AddOperatorActiveOutputFields (:493); the B G input / Bᵀ Gᵀ output chains around the pointwise D; in-range.
  - citation: reference/palace/palace/fem/libceed/integrator.hpp:14-23
    verdict: supports
    audited_at: 2026-06-07T093000Z
    note: enum EvalMode { Weight None Interp Grad Div Curl } (:15-23) — the B basis-eval modes the term's 𝒟 selects; exact.
  - citation: reference/palace/palace/fem/bilinearform.cpp:64-70
    verdict: supports
    audited_at: 2026-06-07T093000Z
    note: Palace-supplied restriction/basis inputs trial_restr :64 test_restr :66 trial_basis :68 test_basis :69; leaf call integ->Assemble :75; fold AddSubOperator :77; exact (the G/B operands + the firm fold L0 home).
  - citation: reference/palace/test/unit/test-libceed.cpp:284
    verdict: empirical-anchor-confirmed-deferred
    audited_at: 2026-06-07T093000Z
    note: TestCeedOperatorFullAssemble exists (:284); :298 asserts mat_diff MaxNorm < 1.0e-12 * max(mat_ref MaxNorm, 1.0) — assembled libCEED matrix matches MFEM reference to 1e-12. The empirical-match target for the FIRMING audit (deferred; impl is roadmap_goal). Path is palace/test/... single-palace under reference/, NOT doubled.
```
```

```edit:book/src/L3/eigsolve-impl.md
[append at end of file]
```yaml
verified_against:
  - citation: book/src/L3/eigsolve.md
    verdict: realizes-kernel-api-faithful
    audited_at: 2026-06-07T093000Z
    note: STRUCTURAL correspondence audit (impl is roadmap_goal; empirical-match deferred to firming). The thick-restart Krylov-Schur driver + inner basis-extension loop + Rayleigh-Ritz extraction faithfully realizes the kernel-api opaque eigen-iteration; the per-step body is the same apply_linop ▷ ksp_solve ▷ scale_untransform composition. Obstruction PRESERVED (impl constructs the loop the library owns, does not dissolve it). realizes-kernel-api edge confirmed reference-class (NOT depends-on); API stays partial-obstruction, undowngraded.
  - citation: reference/palace/palace/linalg/slepc.cpp:630-654
    verdict: supports
    audited_at: 2026-06-07T093000Z
    note: DECISIVE — SlepcEPSSolverBase::SetType; :635 EPSSetType(eps, EPSKRYLOVSCHUR) lands EXACTLY (zero drift). The default opaque eigen-iteration IS Krylov-Schur, the algorithm this impl reconstructs; EPSPOWER :638, EPSSUBSPACE :641, EPSJD :644, MFEM_ABORT arm :652.
  - citation: reference/palace/palace/linalg/slepc.cpp:687-709
    verdict: supports
    audited_at: 2026-06-07T093000Z
    note: SlepcEPSSolverBase::Solve — the opaque library iteration EPSSolve(eps) :694, Customize() :693, EPSGetConverged :695, RescaleEigenvectors :707; the no-Palace-loop anchor the impl's outer driver realizes; exact.
  - citation: reference/palace/palace/linalg/slepc.cpp:602-628
    verdict: supports
    audited_at: 2026-06-07T093000Z
    note: SetProblemType — EPS_HEP :607 / EPS_NHEP :610 / EPS_GHEP :613 / EPS_GHIEP :616 / EPS_GNHEP :619; the problem-symmetry axis selecting lanczos_step (Hermitian) vs krylov-step (non-Hermitian); exact.
  - citation: reference/palace/palace/linalg/slepc.cpp:731-736
    verdict: supports
    audited_at: 2026-06-07T093000Z
    note: GetBV — EPSGetBV(eps, &bv) :734; the SLEPc Krylov-basis-vectors object the impl's BV carry realizes; exact.
  - citation: reference/palace/palace/linalg/arpack.cpp:315-339
    verdict: supports
    audited_at: 2026-06-07T093000Z
    note: ARPACK RCI loop — while(true) :315, naupd :318, ApplyOp dispatch on ido==1||-1 :323-326, ApplyOpB on ido==2 :327-330, break on ido==99 :331-334 (break at :333). The library-owned inner basis-extension loop the impl reconstructs. NOTE the eigsolve.md/impl framing cites the ido==99 break as :330-333 — off-by-one on the range start (:330 is the ido==2 close-brace); break IS in-range; carry-forward to :331-334 for a future lifter (non-load-bearing).
  - citation: reference/palace/palace/linalg/arpack.cpp:369
    verdict: supports
    audited_at: 2026-06-07T093000Z
    note: neupd(...) post-iteration eigenpair extraction (:369) — the impl's rayleigh_ritz + extract_eigpairs; num_it = iparam[2] :342; iparam[2] arpack_it :270; iparam[6] = sinvert?3:1 :273; which::largest_magnitude :278; exact.
```
```

### Note-1 (route to integrator/repairer — stale-prose re-anchor, NOT a claim change)

The consumer `book/src/L1/libceed-quadrature-kernel-impl.md` carries STALE navigational prose now that
D4 has authored the four substrate ops as `roadmap_goal` chapters with anchors:
- frontmatter `depends-on` NOTE comment lines 33-39 — each target tagged "(rough-in; no anchor yet)";
- body §"Speculative L1 operators (rough-in; harvester promotion targets)" lines 166-177.
Both should be re-anchored to "roadmap_goal (authored c122 D4)". This is a text refresh (the
`depends-on` edges and the rank-0 disposition are unchanged and CORRECT). I did NOT apply it (it is my
audit target; the only impl-file edit I propose is the append-only `verified_against:` block above; the
planner marked D4↔D6 SEQUENTIAL on this file). Route to the integrator-per-report (it applies D4's
edits to this file's index rows + may touch the consumer) or a c123 lifter. D4's report flags the
identical item (D4 §Open-questions, "Flag for the integrator / D6").

## Supporting evidence

Source files consulted (all under `reference/palace/`, on-disk `awk` reads):
- `palace/linalg/slepc.cpp` (`:602-654`, `:687-709`, `:711-716`, `:731-736`) — eigsolve kernel-api loop/type/extraction sites.
- `palace/linalg/arpack.cpp` (`:270`, `:273`, `:278`, `:315-339`, `:342`, `:369`) — ARPACK RCI driver.
- `palace/fem/libceed/integrator.cpp` (`:25`, `:215-220`, `:340-397`, `:423-465`, `:488-495`) — libceed assembler/build/apply QFunctions.
- `palace/fem/libceed/integrator.hpp` (`:14-23`) — EvalMode.
- `palace/fem/integrator.hpp` (`:58-61`) — the leaf-kernel pure-virtual contract (shared anchor).
- `palace/fem/bilinearform.cpp` (`:64-78`) — the fold + leaf call + restriction/basis inputs.
- `palace/fem/libceed/operator.cpp` (`:455`, `:483`, `:487-488`) — COO→CSR materialization.
- `palace/test/unit/test-libceed.cpp` (`:284`, `:298`) — the empirical full-assemble anchor (1e-12).
- `tools/graded-stack-lint/graded_stack_lint.py` — 0 rank violations; the three impl/constituent nodes `[GARBAGE*]` by design.

Audit-target chapters: `book/src/L1/libceed-quadrature-kernel-impl.md`,
`book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md`, `book/src/L3/eigsolve-impl.md`,
`book/src/L3/eigsolve.md`. Constituents confirmed firm/roadmap_goal:
`book/src/L3/{krylov-step,ksp_solve,apply_linop}.md` (firm), `book/src/L2/orthogonalize.md` (firm),
`book/src/L3/lanczos_step.md` (roadmap_goal). `book/src/L4/eigsolve.md` exists (sibling
realizes-kernel-api target).

## Open questions / caveats

- **Both audits are STRUCTURAL, not empirical** — both impls are rank-0 `roadmap_goal`, so the
  `empirical-match` justification is correctly deferred. My `realizes-kernel-api-faithful` verdict means
  "the constructive decomposition structurally corresponds to the documented opaque-API contract and the
  linkage is well-formed," NOT "the impl computes bit-identical output today." The empirical audit fires
  at the FIRMING flip (when the substrate / `lanczos_step` materialize). For libceed the empirical target
  is confirmed-on-disk (`test-libceed.cpp:284`, 1e-12); for eigsolve the empirical target is the
  eigenpair correspondence modulo tolerance + the four L1 non-determinism sources (deferred).
- **The libceed `[UNRESOLVED]` linter edges resolve when D4 lands** — at audit time the four substrate
  files are in D4's proposed-changes (not yet on disk), so the linter still reports
  `[UNRESOLVED] libceed-quadrature-kernel-impl -> {element_restrict,basis_apply,quad_point_contract,geom_factor_build}`.
  This is the expected mid-cycle state (D6 Wave-2 reads D4's report; integration is Phase 5). NOT a
  finding — once D4 lands, the 6 `unresolved_depends_on_targets` drop to 2 (the D1/D2 AMR verbs). I
  audited the correspondence against D4's authored substrate semantics (its report), which is the correct
  Wave-2 input.
- **Stale-prose re-anchor (Note-1) is routed, not applied** — the consumer's "rough-in; no anchor yet"
  prose is stale post-D4. Routed to integrator/repairer (D4 flagged the identical item). A
  navigational-only refresh; the edges/rank are correct.
- **`ido==99` break range `:330-333`** appears in both `eigsolve.md` §Evidence and the impl framing;
  the block is `:331-334` (break at `:333`, in-range). Carry-forward correction `:330-333` → `:331-334`
  for a future land-clean lifter (per `lifter-scope-content-correction-boundary`). Non-load-bearing;
  does not block the audit verdict.
- **`realizes-leaf` label** — recommend KEEP DISTINCT (documentation; free; zero linter blast radius;
  preserves reviewer-legible "realizes a firm fold's leaf" vs "realizes an obstruction-API contract").
  No action required this cycle; defer any uniform-vocabulary decision to the batch-39 meta.
- **No directionality violation** — both impl chapters narrate the constructive realization (the
  from-our-primitives version) and the correspondence forward (impl → API contract); no reverse-lift
  prose in chapter content. Clean.
