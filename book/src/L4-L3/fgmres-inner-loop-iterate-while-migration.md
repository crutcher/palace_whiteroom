# fgmres-inner-loop-iterate-while-migration

The L4>L3 lowering theme for the **FGMRES** inner Arnoldi loop, under the re-rendering of `gmres.md` §L4's `inner_loop` as a direct invocation of the firm L4 [`iterate_while`](../L4/iterate_while.md) combinator. **Sibling theme** to the now-firm [`gmres-inner-loop-iterate-while-migration`](./gmres-inner-loop-iterate-while-migration.md): the two themes share the wrapper-dissolution shape, the body-primitive sequence, and the speculative `check_stop_into_carry` helper; they differ on **variant-axis collapse** (FGMRES pins `pc_side = RIGHT` and `flexible = true`; GMRES leaves both free) and on **per-iteration preconditioner adaptation** (FGMRES allocates a per-iteration `Z[j]` workspace; GMRES uses the single workspace `r` unless `op.flexible`). The theme is **firm**: it depends on the *same* upstream `gmres.md` §L4 v0.6→v0.7 self-rotation its sibling depends on, recorded at the slice's §L4 v0.7 section (`gmres.md:673-747`). The rotation took option (a) — the witness-into-carry hoist via the (still-rough-in) `check_stop_into_carry` helper — which is the LHS this theme sketched, so no LHS revision was needed; the FGMRES specialisation applies the two variant-axis collapses to that firm migrated form.

## Slug

`fgmres-inner-loop-iterate-while-migration`

## Context

Palace's `FgmresSolver<OperType>` (declared at `palace/linalg/iterative.hpp:222`) is a subclass of `GmresSolver<OperType>` that hard-pins the right-preconditioning side and allocates per-iteration adaptive-preconditioner workspace. The class inherits the entire GMRES state surface (`max_dim`, `gs_orthog`, `pc_side`, `V`, `H`, `s`, `sn`, `cs` per `iterative.hpp:243-253`) plus a `mutable std::vector<VecType> Z` member (its own, not inherited; `iterative.hpp:256-257`). The constructor `FgmresSolver(MPI_Comm, int)` pins `pc_side = PreconditionerSide::RIGHT` (`iterative.hpp:263-266`); the `SetPreconditionerSide` override at `iterative.hpp:268-273` `MFEM_VERIFY`s the same constraint.

The inner loop at `palace/linalg/iterative.cpp:794-829` is **textually nearly identical** to the GMRES inner loop at `:615-650` — the 3-condition break sites are textually identical (`:644-649` vs `:823-828`), and the per-step body is identical modulo (a) `ApplyBA`'s third argument (`pc_side` for GMRES, hard-coded `PreconditionerSide::RIGHT` for FGMRES) and (b) the workspace vector (`r` for GMRES, `Z[j]` for FGMRES — the adaptive-preconditioner output that FGMRES stores per-step to use during back-substitution).

The now-firm [`gmres-inner-loop-iterate-while-migration`](./gmres-inner-loop-iterate-while-migration.md) theme captures the upstream rotation generically: the L4 GMRES `inner_loop` migration (authored as the slice §L4 v0.7 self-rotation, `gmres.md:673-747`) produces an `iterate_while`-invocation with the witness-into-carry hoist via `check_stop_into_carry`. **The same rotation applies to FGMRES**, with two variant-axis simplifications:

- **`pc_side`** is collapsed to the single value `RIGHT` at the constructor level. The GMRES theme's variant-pass-through claim ("`pc_side` is inspected only inside `apply_BA`") is FGMRES-trivial: the apply_BA call site reads a fixed value, and the variant-absorption is structurally complete at the FGMRES subclass level rather than inside `apply_BA`.
- **`flexible`** is collapsed to `true`. The GMRES theme's `if op.flexible then K { Z = K.Z `with` (K.j, z) } else K` carry-update simplifies to the unconditional `K { Z = K.Z `with` (K.j, z) }` in the FGMRES instantiation.

The remaining two GMRES variant axes (`gs_orthog ∈ {MGS, CGS, CGS2}` and `max_dim`) are still free at FGMRES. They pass through the rotation unchanged.

This theme parallels its sibling in shape: the L4 wrapper machinery dissolves into L3 value-threading; the body's primitive sequence (apply_BA, orthogonalize, ls_update_column, modify-it, carry-update) survives textually unchanged from L4 to L3 modulo the wrapper rotation. The FGMRES-specific additions over the sibling are (a) the `pc_side`/`flexible` variant collapses noted above, (b) a per-iteration `Z` allocation in the carry that mirrors the workspace use, and (c) a different initial-residual policy (FGMRES uses `true_beta = nrm2(comm, Z[0])` after `InitialResidual` rather than the LS-proxy `s[j+1]`; this difference lives in `restart_cycle`, **not** in `inner_loop`, and is correctly scoped out of this theme).

The theme does NOT cover the upstream gmres.md §L4 self-rotation itself — that is recorded at the slice's §L4 v0.7 section (`gmres.md:673-747`); this theme is its L4>L3 post-condition for the FGMRES specialisation.

## L4 form (LHS)

The migrated FGMRES inner loop, as it appears under the now-firm `gmres.md` §L4 v0.7 form (`gmres.md:673-747`), parameterised on the FGMRES variant-axis collapse:

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

- **`gs_orthog ∈ {MGS, CGS, CGS2}`** — absorbed inside `orthogonalize` per the v0.6 constructed-operator surface table row `orthogonalize | gs_orthog | MGS/CGS/CGS2 dispatch` (`gmres.md:649`; and the §L1 absorption list at `gmres.md:250`). The wrapper rotation does not branch on `gs_orthog`; the body-primitive call is identical on both sides.
- **`max_dim`** (restart frequency / per-cycle basis dimension) — folded into the `stop_reason` carry-field via `check_stop_into_carry` per the v0.6 surface table row `check_stop | max_it, max_dim | stop-witness producer` (`gmres.md:652`; and the `K.j + 1 == op.max_dim = Just StoppedMaxDim` guard at `gmres.md:591`). Both L4 and L3 forms read it via the same `check_stop_into_carry op conv K3 s'.it` call. Outer-loop restart frequency itself lives one level up at `restart_cycle` (`gmres.md:613-631`), not in the inner loop, and is correctly scoped out of this theme.

The GMRES variant profile (the v0.6 constructed-operator surface table at `gmres.md:645-654`, plus the §"Variant axes" sections at `gmres.md:172-176`, `:248-252`) reduces under FGMRES to just these two rows; the basis for the pass-through claims is the GMRES profile modulo the FGMRES pinning of `pc_side = RIGHT` (surface-table row `apply_BA | pc_side, (Mk if flexible)`, `gmres.md:648`) and `flexible = true` (surface-table row `apply_correction | pc_side, flexible`, `gmres.md:650`).

### What this lowering does NOT cover

- **The upstream gmres.md §L4 v0.6→v0.7 self-rotation** that re-renders `inner_loop` as the `iterate_while` invocation. Same disposition as the sibling theme — it is recorded at the slice's §L4 v0.7 section (`gmres.md:673-747`); both this theme and its sibling are its L4>L3 post-conditions.
- **The FGMRES outer-loop `restart_cycle` initial-residual policy** — FGMRES computes `true_beta = nrm2(comm, Z[0])` after `InitialResidual` (per `iterative.cpp:756-765`) rather than the LS-proxy `beta` read inside the inner loop. This is the FGMRES "true residual at restart" check (and the drift-warning compare against the recursion-formula `beta`, `iterative.cpp:772-780`). This policy lives in `restart_cycle`, **not** in `inner_loop`, and is out of this theme's scope. The sibling GMRES theme has the same scoping — `restart_cycle` is one level up.
- **L3>L2 lowering on the body** — identity-in-form (the same disposition that backs the krylov_step and GMRES themes); the L3>L2 hop is trivial completion.
- **The `ls_update_column` sequential obstruction** at L3 — body-primitive level, not wrapper level; survives the wrapper dissolution unchanged.
- **The orthog-internal MGS obstruction** — same disposition as the sibling theme.

## Applicability conditions

The rewrite is valid when all five conditions of the sibling [`gmres-inner-loop-iterate-while-migration`](./gmres-inner-loop-iterate-while-migration.md) §"Applicability conditions" hold, **plus** one FGMRES-specific condition:

1–5: Inherited verbatim from the sibling theme. (`Solve` effect domain is exactly `SimState`; `OpParams` and `Convergence` are closure-captured; body primitives are L3-native or carry their own classification; consumer observes `final_state`-equivalent quantities only; `check_stop_into_carry` is pure on `(OpParams, Convergence, Krylov, int)`.)

6. **The FGMRES subclass constraint `pc_side = RIGHT` and `flexible = true` is structurally enforced at the `OpParams` construction site, not at the inner-loop call site.** This is the rotation's basis for collapsing the GMRES sibling's `pc_side`-variant and `flexible`-variant cases into a single FGMRES-specialised body. If a future FGMRES variant relaxed either constraint (e.g., a left-preconditioned FGMRES), the theme would specialise back to the GMRES sibling's branched form.

If a future FGMRES variant violates the inherited conditions (e.g., a recursion that touches `SimState` outside the `it` counter, or a non-`SimState`-shaped monad), the theme needs refinement.

## Justification kind

**`structural`** with secondary **`reduction-chain`** and **`empirical-match`** components — identical kind signature to the sibling theme, and identical reasoning. The FGMRES variant-axis collapses are themselves structural (subclass-level pinning) and reduce the body's wrapper-dissolution to a tighter case of the GMRES rewrite. The body's identity-in-form on its primitive sequence is the same disposition that backs the sibling theme and `krylov-step-typed-wrapper-dissolution`.

**Abstraction-direction note**: L4 is the higher-abstraction layer (typed records, monadic effect, structural predicate-on-carry-only discipline, demand-prunable trajectory) and L3 is the lower-abstraction layer (positional values threaded explicitly, branch-on-stop-reason in tail recursion, trajectory dissolved per consumer). The rotation direction is L4 → L3.

## Speculative L4 operators

The same speculative L4 helper `check_stop_into_carry` from the sibling theme is invoked at the same callsite shape in this FGMRES specialisation. The FGMRES site at `iterative.cpp:823-828` is textually identical to the GMRES site at `:644-649`; the joint lowering produces a structurally identical `check_stop_into_carry` callsite shape across both themes.

**`check_stop_into_carry` stays rough-in.** GMRES and FGMRES are sister algorithms inside one translation unit on a single solver-family pair (FGMRES is "GMRES with right-preconditioning allowed to vary per iteration"), so the structural population does not stress the helper's signature in a *new* dimension. OQ `nleps-spec-gap-as-check-stop-into-carry-reuse-blocker` is the canonical blocker for *firm* L4 promotion; a non-`GmresSolverBase` Krylov consumer (e.g., a literature-anchored MINRES inner loop, or NLEPS once spec'd) is required.

In the L4 [dep-map](../L4/index.md), this is annotated as a rough-in:

`| check_stop_into_carry *(rough-in; no anchor yet; firm promotion blocked on non-GmresSolverBase consumer per OQ nleps-spec-gap-as-check-stop-into-carry-reuse-blocker)* | OpParams -> Convergence -> Krylov -> int -> Krylov (with stop_reason field updated) | rough-in |`

The dep-map row remains plain text (rough-in rows are plain text when the anchor is missing).

## Evidence

L0 evidence (the FGMRES inner-loop pattern this theme abstracts):

- `reference/palace/palace/linalg/iterative.cpp:794-829` — FGMRES `Mult` inner Arnoldi loop. The `int j = 0; for (;; j++, it++) { ... if (converged || j + 1 == max_dim || it + 1 == max_it) { it++; break; } }` shape is the L0 form whose three-way break corresponds at L4 to the witness-into-carry `Maybe StopReason` (three constructors: `Conv` from `converged = (beta < eps)` at line 823; `MaxDim` from `j + 1 == max_dim` at line 824; `MaxIt` from `it + 1 == max_it` at line 824).
- `reference/palace/palace/linalg/iterative.cpp:821-823` — `beta = std::abs(s[j + 1]); CheckDot(beta, ...); converged = (beta < eps);`. The L0 per-step residual-proxy computation; surfaces at L4 as the `K.beta` carry-field write and the `bt_of K5` extras computation.
- `reference/palace/palace/linalg/iterative.cpp:806-819` — the per-step body sequence (`ApplyBA(PreconditionerSide::RIGHT, A, B, V[j], w, Z[j], ...)`, `OrthogonalizeIteration`, `Norml2`, `ApplyPlaneRotation` ×j, `GeneratePlaneRotation`, `ApplyPlaneRotation` ×2). Maps to the L4/L3 body's `apply_BA → orthogonalize → ls_update_column` chain; identity-in-form across L4>L3. The `Z[j]` workspace argument is the FGMRES-specific per-iteration preconditioner-output capture; collapses to the unconditional `K { Z = K.Z `with` (K.j, z) }` carry-update at L4.
- `reference/palace/palace/linalg/iterative.hpp:222-270` — `FgmresSolver<OperType>` subclass declaration. Establishes the `pc_side = RIGHT` pinning at the constructor (line 263-266) and the `SetPreconditionerSide` verification (line 268-273). This is the structural source for FGMRES variant-axis collapse `pc_side ∈ {RIGHT}` (vs. the GMRES `pc_side ∈ {LEFT, RIGHT, NONE}` axis).

L4 source (the LHS of this rewrite):

- GMRES v0.6 `inner_loop` / `check_stop` / `StopReason` sum type + the migrated v0.7 form — firm L0 home `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C (`GmresSolver<OperType>::Mult` `iterative.cpp:543-705`; inner Arnoldi loop within `iterative.cpp:563-683`). The FGMRES specialisation applies the variant-axis collapses to that migrated form. The LHS is no longer speculative — it is the firm migrated form shared with the gmres sibling.
- `book/src/L4/iterate_while.md` §Signature, §Semantics, §"Predicate-on-extras anti-pattern", §Algebraic laws Law 1 — the firm L4 row this theme's LHS invokes. Same usage as the sibling theme.
- `book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md` (firm) — the sibling theme. This theme inherits the wrapper-dissolution rotation, the body-identity-in-form claim, the applicability conditions 1–5, and the speculative-helper invocation. The FGMRES specialisation adds applicability condition 6 and the two variant-axis collapses.

L4>L3 precedent (the theme this one parallels):

- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` §"L3 form (RHS)", §"What the L3 form for `iterate_while` looks like" — the firm precedent theme. This theme inherits the wrapper-dissolution rotation and the body-identity-in-form claim.

Concept references:

- `book/src/concepts/derived-view-hoisting.md` §"Worked example: CG residual norm" — the §3.8 collapse rule. FGMRES's `K.beta` is the analogue of CG's `res = sqrt|beta|`; same disposition as the GMRES sibling.
- `book/src/concepts/sequential-obstruction.md` — referenced for completeness; same disposition as the sibling.
- `book/src/concepts/variant-absorption.md` — the FGMRES subclass-level variant pinning is a level-(b) absorption: the `pc_side` axis is read at exactly one site (the constructor) and the body never branches on it.

## Status

`firm` — the theme's LHS is the firm migrated form from the shared upstream `gmres.md` §L4 v0.6→v0.7 self-rotation (recorded at the slice's §L4 v0.7 section, `gmres.md:673-747`). The rotation took option (a) — the witness-into-carry hoist via `check_stop_into_carry` — which is the LHS sketched here, so no LHS revision was needed; the FGMRES specialisation applies the two variant-axis collapses (`pc_side = RIGHT`, `flexible = true`) and the per-iteration `Z[j]` workspace to that firm form. The RHS (L3 form) is structurally derived from the LHS and inherits the firm [`krylov-step-typed-wrapper-dissolution`](./krylov-step-typed-wrapper-dissolution.md) rotation shape via the firm [`gmres-inner-loop-iterate-while-migration`](./gmres-inner-loop-iterate-while-migration.md) sibling. The one rough-in element in the LHS vocabulary — the `check_stop_into_carry` L4 helper — does not block this theme's firmness: it is a thin pure record-update wrapper around the firm v0.6 `check_stop`, and the theme is firm *as an L4>L3 dissolution theme* exactly as the gmres sibling is firm while `check_stop_into_carry` stays rough-in.

**`check_stop_into_carry` stays rough-in (no promotion).** GMRES and FGMRES are sister algorithms in one translation unit on a single solver-family pair, so the structural population does not stress the helper signature in a new dimension. The strong-reuse evidence — a non-`GmresSolverBase` Krylov consumer (e.g., a literature-anchored MINRES inner loop, or NLEPS once spec'd) — is still required, tracked by OQ `nleps-spec-gap-as-check-stop-into-carry-reuse-blocker`. The dep-map row stays plain-text (rough-in rows are plain text when the anchor is missing).
