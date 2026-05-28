---
agent: lifter
invoked_at: 2026-05-27T23:46:48Z
scope: L4>L3 theme authoring — `fgmres-inner-loop-iterate-while-migration` (sister theme to cycle-008 GMRES form; closes cycle-010 OQ `fgmres-inner-loop-iterate-while-migration-lifter-candidate`)
status: integrated
integrated_at: 2026-05-28T013333Z
integration_commit: 8bb16b7
integration_notes: cycle-011 wave-2 pass 5; first L4>L3 rough-in sister-theme in the artifact; sibling to cycle-008 GMRES theme; L4>L3 layer transitions from 2-theme to 3-theme status; closes cycle-010 OQ fgmres-inner-loop-iterate-while-migration-lifter-candidate (status open → answered-by-rough-in-theme); 4 proposed-changes applied cleanly; 0 safety-net gate hits; firm-promotion of check_stop_into_carry remains deferred per nleps-spec-gap-as-check-stop-into-carry-reuse-blocker; pattern at recurrence-2 of cycle-008 sibling shape
inputs:
  - book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md
  - reports/2026-05-27T215535Z-combinator-miner-check-stop-into-carry-mcp-pilot/CYCLE.md
  - book/src/L4/iterate-while.md
  - book/src/spec/slices/gmres.md (v0.6 inner_loop; lines 539-672 retained)
  - reference/palace/palace/linalg/iterative.cpp (GMRES :614-650; FGMRES :734-833)
  - reference/palace/palace/linalg/iterative.hpp (FgmresSolver subclass :222-270)
---

# CYCLE: Author `fgmres-inner-loop-iterate-while-migration` (sister theme)

## Summary

This dispatch authors **`book/src/L4-L3/fgmres-inner-loop-iterate-while-migration.md`** as a firm sibling theme to the cycle-008 rough-in [`gmres-inner-loop-iterate-while-migration`](../../book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md). The two themes describe how the FGMRES (resp. GMRES) inner Arnoldi loop in `palace/linalg/iterative.cpp` lowers from the speculative L4 v0.7 `iterate_while`-rendered form to the L3 tail-recursive value-threading worker. The cycle-010 combinator-miner audit (`reports/2026-05-27T215535Z-combinator-miner-check-stop-into-carry-mcp-pilot/CYCLE.md`) confirmed that the FGMRES 3-condition stop test at `palace/linalg/iterative.cpp:823-828` is **textually identical** to the GMRES site at `:644-649`, and that the FGMRES inner-loop body is structurally equivalent to GMRES with `pc_side` hard-pinned to `RIGHT` and `flexible` hard-pinned to `true` (the FGMRES subclass relation, `iterative.hpp:222-270`).

The theme is authored at **`rough-in` status**, inheriting the upstream gmres.md §L4 v0.6→v0.7 self-rotation dependency from its sister. The new theme cites the GMRES + FGMRES sites jointly; explicitly states the variant-axis collapse (`pc_side` and `flexible` pinned; `gs_orthog` and `max_dim` free); references `check_stop_into_carry` as the **candidate combinator** the joint lowering would invoke, with promotion **deferred per the cycle-010 verdict** (lower-edge "second reuse" — sister-algorithm twin in one TU is not yet sufficient evidence for firm L4 promotion).

SUMMARY.md and `book/src/L4-L3/index.md` are extended with the new theme entry. The cycle-008 GMRES theme requires **no v0.7-vocabulary re-anchoring** — its v0.6 vocabulary references are still current; the L4 vocabulary referenced (`iterate_while`, `Solve`, `Krylov`, `StopReason`, `Maybe`) is unchanged at v0.7. The only forward reference in the GMRES theme that this dispatch could refine is the §"Speculative L4 operators" section's "defer until second reuse" promotion language — this dispatch's existence corroborates the cycle-010 audit's *lower-edge* reading and is recorded inline in the new theme's §Status. No surgical edits are proposed to the cycle-008 theme; the cycle-010 audit verdict (recorded in OQ `nleps-spec-gap-as-check-stop-into-carry-reuse-blocker`'s cycle-010 revisit note, ledger lines 1538 / 1760) is the canonical record of the lower-edge interpretation.

## Proposed changes

### New theme file: `book/src/L4-L3/fgmres-inner-loop-iterate-while-migration.md`

```edit:book/src/L4-L3/fgmres-inner-loop-iterate-while-migration.md
[old]: <new file>
[new]:
# fgmres-inner-loop-iterate-while-migration

The L4>L3 lowering theme for the **FGMRES** inner Arnoldi loop, under the (speculative) re-rendering of `gmres.md` §L4's `inner_loop` as a direct invocation of the firm L4 [`iterate-while`](../L4/iterate-while.md) combinator. **Sibling theme** to [`gmres-inner-loop-iterate-while-migration`](./gmres-inner-loop-iterate-while-migration.md): the two themes share the wrapper-dissolution shape, the body-primitive sequence, and the speculative `check_stop_into_carry` helper; they differ on **variant-axis collapse** (FGMRES pins `pc_side = RIGHT` and `flexible = true`; GMRES leaves both free) and on **per-iteration preconditioner adaptation** (FGMRES allocates a per-iteration `Z[j]` workspace; GMRES uses the single workspace `r` unless `op.flexible`). The theme is **rough-in** for the same reason its sibling is: it depends on an upstream self-rotation on `gmres.md` §L4 (v0.6→v0.7) that has not yet been authored.

## Slug

`fgmres-inner-loop-iterate-while-migration`

## Context

Palace's `FgmresSolver<OperType>` (declared at `palace/linalg/iterative.hpp:222`) is a subclass of `GmresSolver<OperType>` that hard-pins the right-preconditioning side and allocates per-iteration adaptive-preconditioner workspace. The class inherits the entire GMRES state surface (`max_dim`, `gs_orthog`, `pc_side`, `V`, `H`, `s`, `sn`, `cs` per `iterative.hpp:243-253`) plus a `mutable std::vector<VecType> Z` member (its own, not inherited; `iterative.hpp:256-257`). The constructor `FgmresSolver(MPI_Comm, int)` pins `pc_side = PreconditionerSide::RIGHT` (`iterative.hpp:263-266`); the `SetPreconditionerSide` override at `iterative.hpp:268-273` `MFEM_VERIFY`s the same constraint.

The inner loop at `palace/linalg/iterative.cpp:794-829` is **textually nearly identical** to the GMRES inner loop at `:615-650` — the cycle-010 MCP-pilot combinator-miner audit confirmed the 3-condition break sites are textually identical (`:644-649` vs `:823-828`), and the per-step body is identical modulo (a) `ApplyBA`'s third argument (`pc_side` for GMRES, hard-coded `PreconditionerSide::RIGHT` for FGMRES) and (b) the workspace vector (`r` for GMRES, `Z[j]` for FGMRES — the adaptive-preconditioner output that FGMRES stores per-step to use during back-substitution).

The cycle-008 abstractor's [`gmres-inner-loop-iterate-while-migration`](./gmres-inner-loop-iterate-while-migration.md) theme captures the upstream rotation generically: the L4 GMRES `inner_loop` migration produces an `iterate_while`-invocation with the witness-into-carry hoist via `check_stop_into_carry`. **The same rotation applies to FGMRES**, with two variant-axis simplifications:

- **`pc_side`** is collapsed to the single value `RIGHT` at the constructor level. The GMRES theme's variant-pass-through claim ("`pc_side` is inspected only inside `apply_BA`") is FGMRES-trivial: the apply_BA call site reads a fixed value, and the variant-absorption is structurally complete at the FGMRES subclass level rather than inside `apply_BA`.
- **`flexible`** is collapsed to `true`. The GMRES theme's `if op.flexible then K { Z = K.Z `with` (K.j, z) } else K` carry-update simplifies to the unconditional `K { Z = K.Z `with` (K.j, z) }` in the FGMRES instantiation.

The remaining two GMRES variant axes (`gs_orthog ∈ {MGS, CGS, CGS2}` and `max_dim`) are still free at FGMRES. They pass through the rotation unchanged.

This theme parallels its sibling in shape: the L4 wrapper machinery dissolves into L3 value-threading; the body's primitive sequence (apply_BA, orthogonalize, ls_update_column, modify-it, carry-update) survives textually unchanged from L4 to L3 modulo the wrapper rotation. The FGMRES-specific additions over the sibling are (a) the `pc_side`/`flexible` variant collapses noted above, (b) a per-iteration `Z` allocation in the carry that mirrors the workspace use, and (c) a different initial-residual policy (FGMRES uses `true_beta = nrm2(comm, Z[0])` after `InitialResidual` rather than the LS-proxy `s[j+1]`; this difference lives in `restart_cycle`, **not** in `inner_loop`, and is correctly scoped out of this theme).

The theme does NOT cover the upstream gmres.md §L4 self-rotation itself — that is a separate lifter dispatch on `gmres.md §L4`; this theme is its L4>L3 post-condition for the FGMRES specialisation.

## L4 form (LHS)

The migrated FGMRES inner loop, as it would appear under the same speculative `gmres.md` §L4 v0.7 form, parameterised on the FGMRES variant-axis collapse:

```text
-- The Krylov carry shape is shared with GMRES; FGMRES pins `flexible = true` so
-- the Z field is always populated. `stop_reason :: Maybe StopReason` is the
-- hoisted convergence-witness field (v0.7 addition; written by check_stop_into_carry).
type Krylov = {
  V :: Vec[],
  Z :: Vec[],                       -- always populated under FGMRES (flexible = true)
  H :: Dense,
  s :: DenseVec,
  cs :: DenseVec,
  sn :: DenseVec,
  j :: int,
  beta :: real,
  stop_reason :: Maybe StopReason
}

-- OpParams for FGMRES has pc_side = RIGHT and flexible = true pinned at
-- construction; the inner_loop reads neither axis. The migrated form:
fgmres_inner_loop :: OpParams -> Convergence -> Krylov -> Solve (Krylov, StopReason)
fgmres_inner_loop op conv K0 = do
  result <- iterate_while
              K0
              (\K -> isNothing K.stop_reason)                      -- predicate reads carry only
              (\K -> do                                            -- step body, Solve-threaded
                let (w, z)      = apply_BA op K.j (K.V `at` K.j)   -- pc_side = RIGHT inside apply_BA
                let K1          = K { Z = K.Z `with` (K.j, z) }    -- unconditional under FGMRES
                let (v_next, h) = orthogonalize op (K1.V `slice` (0, K1.j)) w
                let K2          = K1 { V = K1.V `with` (K1.j + 1, v_next) }
                let K3          = ls_update_column K2 h
                modify (\s -> s { it = s.it + 1 })
                s <- get
                let K4          = check_stop_into_carry op conv K3 s.it     -- writes stop_reason
                let K5          = if isNothing K4.stop_reason
                                    then K4 { j = K4.j + 1 }
                                    else K4
                pure { state: K5, residual_norm: K5.beta, breakdown_token: bt_of K5 }
              )
  -- result :: { final_state: Krylov, trajectory: [{ residual_norm, breakdown_token }] }
  let K_final = result.final_state
  pure (K_final, fromJust K_final.stop_reason)
```

The same three load-bearing structural moves over the v0.6 inline form as the sibling theme (predicate-reads-carry-only, `check_stop_into_carry` witness-hoist, `{ residual_norm, breakdown_token }` extras) apply. The two FGMRES-specific simplifications visible in the LHS are:

1. **`Z` is unconditional in the carry-update** (line `let K1 = K { Z = K.Z `with` (K.j, z) }`) — no `if op.flexible then ... else K` branch. The GMRES sibling has the branch; FGMRES collapses it.

2. **`apply_BA` reads a fixed `pc_side` inside** — at the FGMRES subclass level, the apply_BA call is `apply_BA op K.j ...` where `op.pc_side` is structurally pinned to `RIGHT` by the constructor. The migration does not invent a new call shape; the variant axis is absorbed one layer up.

The body's primitive sequence — `apply_BA`, `orthogonalize`, `ls_update_column`, `modify`, `check_stop_into_carry`, carry-update — is **textually identical** to the GMRES sibling's body modulo the two simplifications above.

## L3 form (RHS)

The L3 form dissolves the wrapper per [`krylov-step-typed-wrapper-dissolution`](./krylov-step-typed-wrapper-dissolution.md) §"L3 form" and per the sibling [`gmres-inner-loop-iterate-while-migration`](./gmres-inner-loop-iterate-while-migration.md) §"L3 form": the `Solve` monad becomes explicit `(K, s) -> (K', s')` positional threading; `iterate_while` becomes a tail-recursive worker; the trajectory accumulator is pruned per the FGMRES consumer pattern (the outer `restart_cycle` reads `final_state` only ⇒ trajectory is `[]`).

```text
fgmres_inner_loop_L3 :: OpParams -> Convergence -> Krylov -> SimState -> (Krylov, StopReason, SimState)
fgmres_inner_loop_L3 op conv K0 s0 =
  let (K_final, s_final) = fgmres_inner_loop_L3_worker op conv K0 s0
  in (K_final, fromJust K_final.stop_reason, s_final)

fgmres_inner_loop_L3_worker :: OpParams -> Convergence -> Krylov -> SimState -> (Krylov, SimState)
fgmres_inner_loop_L3_worker op conv K s =
  if isNothing K.stop_reason
    then
      let (w, z)      = apply_BA op K.j (K.V `at` K.j)              -- L3-native global op chain; pc_side fixed
      let K1          = K { Z = K.Z `with` (K.j, z) }                -- unconditional under FGMRES
      let (v_next, h) = orthogonalize op (K1.V `slice` (0, K1.j)) w   -- L3 obstruction internal to orthog under MGS
      let K2          = K1 { V = K1.V `with` (K1.j + 1, v_next) }
      let K3          = ls_update_column K2 h                          -- L3 sequential obstruction on small-dense state
      let s'          = s { it = s.it + 1 }                            -- dissolved modify
      let K4          = check_stop_into_carry op conv K3 s'.it         -- L3-native: pure scalar comparison + record update
      let K5          = if isNothing K4.stop_reason
                          then K4 { j = K4.j + 1 }
                          else K4
      in fgmres_inner_loop_L3_worker op conv K5 s'
    else (K, s)
```

The four structural differences from the L4 form are identical to the sibling theme's: (1) `Solve` dissolves to explicit `s` threading; (2) `iterate_while` dissolves to the tail-recursive worker; (3) trajectory accumulator dissolves to nothing under Law 1; (4) `stop_reason` carry-field threads positionally through the worker. The body-level primitive sequence is **textually identical to the GMRES sibling's L3 worker body** modulo the two FGMRES simplifications (the unconditional Z capture and the implicit `pc_side = RIGHT`).

### What does NOT change in the rotation

The body's primitive sequence — `apply_BA` (constructed-operator linop chain), `orthogonalize` (variant-dispatched, internal MGS obstruction), `ls_update_column` (small-dense sequential obstruction), `check_stop_into_carry` (pure scalar comparison + record update; L3-native), the unconditional `K { Z = K.Z `with` (K.j, z) }` capture, and the carry-update `K5 = K4 { j = K4.j + 1 }` (pure record update) — is **textually identical** between the L4 body and the L3 body. The FGMRES variant-axis profile is the GMRES profile with `pc_side` and `flexible` removed; the two remaining axes pass through unchanged:

- **`gs_orthog ∈ {MGS, CGS, CGS2}`** — absorbed inside `orthogonalize` per `gmres.md:120`. The wrapper rotation does not branch on `gs_orthog`; the body-primitive call is identical on both sides.
- **`max_dim`** (restart frequency / per-cycle basis dimension) — folded into the `stop_reason` carry-field via `check_stop_into_carry` per `gmres.md:121`. Both L4 and L3 forms read it via the same `check_stop_into_carry op conv K3 s'.it` call. Outer-loop restart frequency itself lives one level up at `restart_cycle`, not in the inner loop, and is correctly scoped out of this theme.

The GMRES variant-absorption table at `gmres.md:118-124` reduces under FGMRES to just these two rows; the basis for the pass-through claims is the GMRES table modulo the FGMRES pinning.

### What this lowering does NOT cover

- **The upstream gmres.md §L4 v0.6→v0.7 self-rotation** that re-renders `inner_loop` as the `iterate_while` invocation. Same disposition as the sibling theme — a separate `lifter` dispatch on `gmres.md §L4` would author this; both this theme and its sibling are L4>L3 post-conditions.
- **The FGMRES outer-loop `restart_cycle` initial-residual policy** — FGMRES computes `true_beta = nrm2(comm, Z[0])` after `InitialResidual` (per `iterative.cpp:756-765`) rather than the LS-proxy `beta` read inside the inner loop. This is the FGMRES "true residual at restart" check (and the drift-warning compare against the recursion-formula `beta`, `iterative.cpp:772-780`). This policy lives in `restart_cycle`, **not** in `inner_loop`, and is out of this theme's scope. The sibling GMRES theme has the same scoping — `restart_cycle` is one level up.
- **L3>L2 lowering on the body** — identity-in-form per the same cycle-002 assertion that backs the krylov-step and GMRES themes; the L3>L2 hop is trivial completion.
- **The `ls_update_column` sequential obstruction** at L3 — body-primitive level, not wrapper level; survives the wrapper dissolution unchanged.
- **The orthog-internal MGS obstruction** — same disposition as the sibling theme.

## Applicability conditions

The rewrite is valid when all five conditions of the sibling [`gmres-inner-loop-iterate-while-migration`](./gmres-inner-loop-iterate-while-migration.md) §"Applicability conditions" hold, **plus** one FGMRES-specific condition:

1–5: Inherited verbatim from the sibling theme. (`Solve` effect domain is exactly `SimState`; `OpParams` and `Convergence` are closure-captured; body primitives are L3-native or carry their own classification; consumer observes `final_state`-equivalent quantities only; `check_stop_into_carry` is pure on `(OpParams, Convergence, Krylov, int)`.)

6. **The FGMRES subclass constraint `pc_side = RIGHT` and `flexible = true` is structurally enforced at the `OpParams` construction site, not at the inner-loop call site.** This is the rotation's basis for collapsing the GMRES sibling's `pc_side`-variant and `flexible`-variant cases into a single FGMRES-specialised body. If a future FGMRES variant relaxed either constraint (e.g., a left-preconditioned FGMRES), the theme would specialise back to the GMRES sibling's branched form.

If a future FGMRES variant violates the inherited conditions (e.g., a recursion that touches `SimState` outside the `it` counter, or a non-`SimState`-shaped monad), the theme needs refinement.

## Justification kind

**`structural`** with secondary **`reduction-chain`** and **`empirical-match`** components — identical kind signature to the sibling theme, and identical reasoning. The FGMRES variant-axis collapses are themselves structural (subclass-level pinning) and reduce the body's wrapper-dissolution to a tighter case of the GMRES rewrite. The body's identity-in-form on its primitive sequence is the same combinator-miner cycle-002 assertion that backs the sibling theme and `krylov-step-typed-wrapper-dissolution`.

**Abstraction-direction note**: L4 is the higher-abstraction layer (typed records, monadic effect, structural predicate-on-carry-only discipline, demand-prunable trajectory) and L3 is the lower-abstraction layer (positional values threaded explicitly, branch-on-stop-reason in tail recursion, trajectory dissolved per consumer). The rotation direction is L4 → L3.

## Speculative L4 operators

The same speculative L4 helper `check_stop_into_carry` from the sibling theme is invoked at the same callsite shape in this FGMRES specialisation. The cycle-010 MCP-pilot combinator-miner audit (`reports/2026-05-27T215535Z-combinator-miner-check-stop-into-carry-mcp-pilot/CYCLE.md`) confirmed the FGMRES site at `iterative.cpp:823-828` is textually identical to the GMRES site at `:644-649`; the joint lowering produces a structurally identical `check_stop_into_carry` callsite shape across both themes. **This is the second-reuse evidence the cycle-008 promotion criterion ("defer until second slice needs it") was waiting on**, in the lower-edge reading.

**Promotion remains deferred**, per the cycle-010 audit's verdict: GMRES and FGMRES are sister algorithms inside one translation unit on a single solver-family pair (FGMRES is "GMRES with right-preconditioning allowed to vary per iteration"), so the structural population that would stress the helper's signature in a *new* dimension is unchanged. The current OQ-ledger entry `nleps-spec-gap-as-check-stop-into-carry-reuse-blocker` (cycle-009, last-revisited cycle-010 — see `scaffolding/open-questions.md:1536-1538`) remains the canonical blocker for *firm* L4 promotion; a non-`GmresSolverBase` Krylov consumer (e.g., a literature-anchored MINRES inner loop, or NLEPS once spec'd) is required.

In the L4 [dep-map](../L4/index.md), this would still be annotated as the cycle-008 rough-in (no change to vocabulary status from authoring this sibling theme alone):

`| check_stop_into_carry *(rough-in; no anchor yet; sister-reuse confirmed cycle-010; firm promotion blocked on non-GmresSolverBase consumer per OQ nleps-spec-gap-as-check-stop-into-carry-reuse-blocker)* | OpParams -> Convergence -> Krylov -> int -> Krylov (with stop_reason field updated) | rough-in |`

Per cycle-006 friction-ledger `rough-in-rows-must-be-plain-text-when-anchor-missing`, the dep-map row remains plain text.

## Verified-against

L0 evidence (the FGMRES inner-loop pattern this theme abstracts):

- `reference/palace/palace/linalg/iterative.cpp:794-829` — FGMRES `Mult` inner Arnoldi loop. The `int j = 0; for (;; j++, it++) { ... if (converged || j + 1 == max_dim || it + 1 == max_it) { it++; break; } }` shape is the L0 form whose three-way break corresponds at L4 to the witness-into-carry `Maybe StopReason` (three constructors: `Conv` from `converged = (beta < eps)` at line 823; `MaxDim` from `j + 1 == max_dim` at line 824; `MaxIt` from `it + 1 == max_it` at line 824).
- `reference/palace/palace/linalg/iterative.cpp:821-823` — `beta = std::abs(s[j + 1]); CheckDot(beta, ...); converged = (beta < eps);`. The L0 per-step residual-proxy computation; surfaces at L4 as the `K.beta` carry-field write and the `bt_of K5` extras computation.
- `reference/palace/palace/linalg/iterative.cpp:806-819` — the per-step body sequence (`ApplyBA(PreconditionerSide::RIGHT, A, B, V[j], w, Z[j], ...)`, `OrthogonalizeIteration`, `Norml2`, `ApplyPlaneRotation` ×j, `GeneratePlaneRotation`, `ApplyPlaneRotation` ×2). Maps to the L4/L3 body's `apply_BA → orthogonalize → ls_update_column` chain; identity-in-form across L4>L3. The `Z[j]` workspace argument is the FGMRES-specific per-iteration preconditioner-output capture; collapses to the unconditional `K { Z = K.Z `with` (K.j, z) }` carry-update at L4.
- `reference/palace/palace/linalg/iterative.hpp:222-270` — `FgmresSolver<OperType>` subclass declaration. Establishes the `pc_side = RIGHT` pinning at the constructor (line 263-266) and the `SetPreconditionerSide` verification (line 268-273). This is the structural source for FGMRES variant-axis collapse `pc_side ∈ {RIGHT}` (vs. the GMRES `pc_side ∈ {LEFT, RIGHT, NONE}` axis).

L4 source (the LHS of this rewrite):

- `book/src/spec/slices/gmres.md:539-672` — the v0.6 `inner_loop` + `check_stop` form. The upstream lifter migration would re-render this to the LHS shape above; the FGMRES specialisation applies the variant-axis collapses to the migrated form. **Caveat**: this theme's LHS is speculative; if the upstream migration picks a different shape, the LHS needs revision.
- `book/src/L4/iterate-while.md` §Signature, §Semantics, §"Predicate-on-extras anti-pattern", §Algebraic laws Law 1 — the firm L4 row this theme's LHS invokes. Same usage as the sibling theme.
- `book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md` — the sibling theme. This dispatch inherits the wrapper-dissolution rotation, the body-identity-in-form claim, the applicability conditions 1–5, and the speculative-helper invocation. The FGMRES specialisation adds applicability condition 6 and the two variant-axis collapses.

L4>L3 precedent (the theme this dispatch parallels):

- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` §"L3 form (RHS)", §"Audit of cycle-002 identity-in-form claim", §"What the L3 form for `iterate_while` looks like" — the cycle-006 firm theme. Same usage as the sibling: this dispatch inherits the wrapper-dissolution rotation and the body-identity-in-form claim.

Cycle-010 audit evidence:

- `reports/2026-05-27T215535Z-combinator-miner-check-stop-into-carry-mcp-pilot/CYCLE.md` — the MCP-pilot combinator-miner audit confirming the GMRES + FGMRES textually-identical 3-condition fingerprint. §"Pattern instances" lines 21-41 cite both sites with line ranges (GMRES `:644-649`, FGMRES `:823-828`); §"Tally" confirms 2 strong instances + 5+ non-instances; §"Routing recommendation" recommends this lifter dispatch as cycle-011 follow-up. **This dispatch is the cycle-011 enactment of that routing.**

Concept references:

- `book/src/concepts/derived-view-hoisting.md` §"Worked example: CG residual norm" — the §3.8 collapse rule. FGMRES's `K.beta` is the analogue of CG's `res = sqrt|beta|`; same disposition as the GMRES sibling.
- `book/src/concepts/sequential-obstruction.md` — referenced for completeness; same disposition as the sibling.
- `book/src/concepts/variant-absorption.md` — the FGMRES subclass-level variant pinning is a level-(b) absorption: the `pc_side` axis is read at exactly one site (the constructor) and the body never branches on it.

Open-question disposition:

- **`fgmres-inner-loop-iterate-while-migration-lifter-candidate`** (cycle-010, opened by combinator-miner) — this dispatch is the cycle-011 enactment. **Status update proposal**: change to `answered-by-rough-in-theme`. The theme is authored; the upstream gmres.md migration is the firmer follow-up; the theme firms when the migration lands and aligns with the LHS shape, identical conditions to the sibling.
- **`gmres-inner-loop-iterate-while-migration`** (cycle-007, `answered-by-rough-in-theme` cycle-008) — this theme is a second consumer of the speculative `check_stop_into_carry` helper at the same callsite shape; status unchanged.
- **`nleps-spec-gap-as-check-stop-into-carry-reuse-blocker`** (cycle-009, last-revisited cycle-010) — this theme corroborates the cycle-010 audit's lower-edge "second reuse" reading; the *firm-promotion* blocker (non-`GmresSolverBase` consumer required) is unchanged. Status remains `open`.
- **`variant-absorption-vs-instance-counting-policy`** (cycle-009, meta-phase scope) — this theme is a second data point for the reading (a)+(b) hybrid policy: GMRES + FGMRES are absorbed via a single L1 slice (`ksp_solve.md`) but counted as distinct lifter themes at L4>L3 (the sibling and this). Routes to cycle-012 meta-phase for codification.

## Status

`rough-in` — same status as the sibling theme, for the same upstream-dependency reason: the LHS is speculative on the upstream `gmres.md §L4 v0.6→v0.7` self-rotation; if that rotation lands with the witness-into-carry hoist applied via `check_stop_into_carry` (option (a) in the sibling's rough-in caveats), this theme firms against it. If the rotation picks alternative-combinator option (b) `iterate_while_with_stop_witness` or re-run-at-outer-level option (c), the LHS needs revision. The RHS (L3 form) is structurally derived from the LHS and inherits the wrapper-dissolution shape; it does not depend on the upstream choice beyond the LHS alignment.

**Cycle-010 lower-edge "second reuse" corroboration**: the existence of this theme as a sibling that invokes `check_stop_into_carry` at the same callsite shape is the lower-edge corroborating evidence for the cycle-008 promotion criterion. Per cycle-010 audit, this does **not** unblock firm L4 promotion of the helper (the strong-reuse evidence — a non-`GmresSolverBase` Krylov consumer — is still required, tracked by OQ `nleps-spec-gap-as-check-stop-into-carry-reuse-blocker`).

**Lowering-verifier follow-up** (cycle-012+ candidate, after the upstream gmres.md migration lands and both this and the sibling theme firm): confirm that the L3 forms produced by applying both themes to the migrated `gmres.md §L4 v0.7 inner_loop` are pairwise consistent with `gmres.md §L3`'s inner-step shape (which currently has the v0.6 inline form's L3 lowering implicit in the §L3 obstruction record). If the verifier finds a mismatch (e.g., the v0.7 `check_stop_into_carry` does not lift cleanly to the §L3 shape for FGMRES specifically), the theme is refined.

**Non-blocking on**: the upstream gmres.md migration. This theme is authored speculatively against the same v0.7 shape its sibling assumes; landing one without the other is permitted.
```

### SUMMARY.md update

```edit:book/src/SUMMARY.md
[old]:
# L4 > L3 — Lowering
- [Overview](./L4-L3/index.md)
- [krylov-step-typed-wrapper-dissolution](./L4-L3/krylov-step-typed-wrapper-dissolution.md)
- [gmres-inner-loop-iterate-while-migration](./L4-L3/gmres-inner-loop-iterate-while-migration.md)
[new]:
# L4 > L3 — Lowering
- [Overview](./L4-L3/index.md)
- [krylov-step-typed-wrapper-dissolution](./L4-L3/krylov-step-typed-wrapper-dissolution.md)
- [gmres-inner-loop-iterate-while-migration](./L4-L3/gmres-inner-loop-iterate-while-migration.md)
- [fgmres-inner-loop-iterate-while-migration](./L4-L3/fgmres-inner-loop-iterate-while-migration.md)
```

### L4-L3/index.md theme table update

```edit:book/src/L4-L3/index.md
[old]:
| `gmres-inner-loop-iterate-while-migration` *(rough-in; this dispatch creates the anchor file at `./gmres-inner-loop-iterate-while-migration.md`)* | L4 migrated GMRES inner-loop form: `inner_loop op conv K0 = iterate_while K0 (\K -> isNothing K.stop_reason) (\K -> ...body... ; pure { state, residual_norm, breakdown_token })` with `check_stop_into_carry` writing the witness into the carry's `stop_reason` field. | L3 tail-recursive value-threading worker `gmres_inner_loop_L3_worker op conv K s` with the `Solve` monad dissolved to explicit `s` threading, trajectory pruned to `[]` per Law 1 (consumer reads only `(K_final, K_final.stop_reason)`), and the `iterate_while` combinator dissolved per the parallel `krylov-step-typed-wrapper-dissolution` theme. | `structural` + secondary `reduction-chain` and `empirical-match` | `rough-in` (cycle-008 abstractor; depends on upstream gmres.md §L4 v0.6→v0.7 self-rotation, routed to cycle-008+ lifter on `gmres.md §L4`) |
[new]:
| `gmres-inner-loop-iterate-while-migration` *(rough-in; this dispatch creates the anchor file at `./gmres-inner-loop-iterate-while-migration.md`)* | L4 migrated GMRES inner-loop form: `inner_loop op conv K0 = iterate_while K0 (\K -> isNothing K.stop_reason) (\K -> ...body... ; pure { state, residual_norm, breakdown_token })` with `check_stop_into_carry` writing the witness into the carry's `stop_reason` field. | L3 tail-recursive value-threading worker `gmres_inner_loop_L3_worker op conv K s` with the `Solve` monad dissolved to explicit `s` threading, trajectory pruned to `[]` per Law 1 (consumer reads only `(K_final, K_final.stop_reason)`), and the `iterate_while` combinator dissolved per the parallel `krylov-step-typed-wrapper-dissolution` theme. | `structural` + secondary `reduction-chain` and `empirical-match` | `rough-in` (cycle-008 abstractor; depends on upstream gmres.md §L4 v0.6→v0.7 self-rotation, routed to cycle-008+ lifter on `gmres.md §L4`) |
| [`fgmres-inner-loop-iterate-while-migration`](./fgmres-inner-loop-iterate-while-migration.md) | Sister-form to the GMRES theme above, specialised for `FgmresSolver<OperType>` (`iterative.cpp:734-836`, `iterative.hpp:222-270`): `pc_side` pinned to `RIGHT` and `flexible` pinned to `true` at the constructor; unconditional `K { Z = K.Z `with` (K.j, z) }` carry-update; otherwise identical L4 form. | Sister-form to the GMRES L3 theme above, specialised for FGMRES: identical wrapper dissolution; body simplifies to the FGMRES collapsed shape (`pc_side`/`flexible` variant rows removed). Textually identical break-site at `iterative.cpp:823-828` (cycle-010 MCP-pilot audit). | `structural` + secondary `reduction-chain` and `empirical-match` | `rough-in` (cycle-011 lifter; same upstream gmres.md §L4 v0.6→v0.7 dependency as the GMRES sister) |
```

## Discipline notes

This dispatch is a pure structural authoring of a sister theme — no operator was modified; the GMRES sibling theme's vocabulary was not touched. The cycle-010 audit's verdict (lower-edge "second reuse"; sister-algorithm twinning in one TU does not unblock firm L4 promotion) is honoured throughout the new theme:
- `check_stop_into_carry` remains `rough-in` in the dep-map row text (no firm-promotion proposal).
- The new theme's §Status carries the lower-edge corroboration note and explicitly defers firm promotion to the `nleps-spec-gap-as-check-stop-into-carry-reuse-blocker` OQ.
- No edit is proposed to the GMRES sibling theme — its v0.6 vocabulary references are still current; the L4 v0.7 vocabulary the theme assumes is unchanged (the speculative `check_stop_into_carry` helper signature is the same, and the predicate-on-carry-only / extras-record shapes are L4 v0.7-stable per `book/src/L4/iterate-while.md` §Signature).

**Re-anchoring scope check**: per the role spec, I checked whether the cycle-008 GMRES theme references any rough-in vocabulary that has since firmed up. The theme's L4 vocabulary references are: `iterate_while` (firm cycle-007, no change), `iterate-while-with-prev` (firm cycle-007, no change, not referenced in the lowering itself), `Solve` monad (firm; from `concepts/solve-monad.md`), `Krylov` carry record (still rough-in in `gmres.md §L4 v0.7`), `Maybe StopReason` (still rough-in; same upstream dependency), and `check_stop_into_carry` (still rough-in per cycle-010 verdict). None of these have firmed since cycle-008; no re-anchoring is needed. The cycle-008 theme stays as-is.

**Variant-axis discipline note**: this dispatch surfaces a small policy question — when an L4>L3 theme specialises another via subclass-level variant pinning, should the specialisation be a *sibling theme* (this dispatch's choice) or a *parameterised theme* (one file, parameterised on the variant axes)? The cycle-008 abstractor's promotion criterion language and the cycle-010 audit's routing both suggested the sister-theme approach. The parameterised-theme alternative would be more compact but loses the variant-absorption story (the FGMRES `pc_side` and `flexible` collapses are themselves structural facts worth documenting). The sister-theme approach is also consistent with the cycle-008 `ksp-solve-mutation-rotation` theme's sub-pattern structure (sub-patterns A/B/C/D for the four solver bodies; one theme file with named sub-patterns). The sister-theme approach is chosen here on the basis that the L4>L3 lowering for FGMRES is structurally distinct enough (different OpParams shape, different variant-axis profile) to merit a top-level entry rather than a sub-pattern of the GMRES theme. This is **non-load-bearing** — a future abstractor could merge the two themes into a parameterised one without loss. Surfaced as a discipline note rather than an OQ because the choice is reversible.

## Supporting evidence

- **Combinator-miner cycle-010 audit** (`reports/2026-05-27T215535Z-combinator-miner-check-stop-into-carry-mcp-pilot/CYCLE.md`): confirms textually-identical 3-condition break sites for GMRES (`iterative.cpp:644-649`) and FGMRES (`iterative.cpp:823-828`); recommends this lifter dispatch as the cycle-011 routing.
- **Cycle-008 abstractor sibling** (`book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md`): the structural template this theme parallels.
- **MCP verification reads**: `palace/linalg/iterative.cpp:614-650` (GMRES inner loop), `:734-836` (FGMRES inner loop), `palace/linalg/iterative.hpp:222-270` (FgmresSolver subclass declaration with `pc_side` pinning).
- **Slice v0.6 anchor**: `book/src/spec/slices/gmres.md:539-672` (the v0.6 `inner_loop` + `check_stop` form that the speculative v0.7 self-rotation would migrate).
- **L4 vocabulary anchors**: `book/src/L4/iterate-while.md` (firm); `book/src/concepts/solve-monad.md` (firm); `book/src/concepts/derived-view-hoisting.md` (firm).

## Open questions / caveats

### Same upstream dependency as the sibling

The LHS depends on the speculative `gmres.md §L4 v0.6→v0.7` self-rotation that has not yet been authored. **Same disposition as the cycle-008 sibling theme**: both this and the sibling are L4>L3 post-conditions on the upstream migration; both firm when the migration lands; both need refinement if the migration picks an alternative shape (option (b) `iterate_while_with_stop_witness` or option (c) re-run-at-outer-level). Surfaced as a status-block note rather than a new OQ because the upstream dependency is already tracked (the sibling's rough-in status implicitly carries it).

### Sister-theme vs. parameterised-theme policy (discipline-note-grade)

Discussed in §Discipline notes above. Not surfaced as an OQ because the choice is reversible by a future abstractor without loss of evidence; the sister-theme approach is consistent with `ksp-solve-mutation-rotation`'s sub-pattern precedent and with the cycle-010 audit's routing recommendation.

### Lower-edge "second reuse" — firm promotion still blocked

The cycle-010 audit's lower-edge reading of the "second reuse" criterion is honoured here: the sister-algorithm twin GMRES + FGMRES does **not** unblock firm L4 promotion of `check_stop_into_carry`. Tracked by OQ `nleps-spec-gap-as-check-stop-into-carry-reuse-blocker` (cycle-009, last-revisited cycle-010); a non-`GmresSolverBase` Krylov consumer is the required evidence. No change proposed to that OQ's status.

### FGMRES outer-loop scoping note

The FGMRES `restart_cycle` has a distinct initial-residual policy from GMRES (FGMRES uses `true_beta = nrm2(comm, Z[0])` after `InitialResidual`; GMRES uses the LS-proxy or the recomputed residual depending on `pc_side`). The drift-warning compare at `iterative.cpp:772-780` (FGMRES) and `iterative.cpp:592-600` (GMRES — already flagged in the gmres.md slice's open questions, line 19) is the observability hook on this policy. **Not in this theme's scope** — both belong to `restart_cycle`, one level up from `inner_loop`. Surfaced here because if a future abstractor authors an FGMRES `restart_cycle` lowering theme, the drift-warning compare is a candidate `check_stop_into_carry`-adjacent observability hook to fold into the witness layer. Flagged for forward-reference only; not a current dispatch's OQ.

### Variant-absorption-vs-instance-counting (forward to meta-phase)

This dispatch produces a second data point for the cycle-009 OQ `variant-absorption-vs-instance-counting-policy`: GMRES and FGMRES are absorbed at L1 (one `ksp_solve` operator covers both) but counted as distinct themes at L4>L3 (this theme + the sibling). The reading-(a)+(b)-hybrid is consistent with cycle-010's lower-edge verdict. Routes to cycle-012 meta-phase for codification — same routing as the cycle-010 audit's note on this OQ.
