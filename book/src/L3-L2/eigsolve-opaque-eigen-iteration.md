# eigsolve-opaque-eigen-iteration

The L3>L2 lowering theme for the `eigsolve` **eigen-iteration loop**. The rewrite is **substantive
(non-identity)** and its erasure scope is the **third root**: **opaque-library-ownership**. The firm L3
[`eigsolve`](../L3/eigsolve.md) is a `partial-obstruction` whose per-step body
`apply_shift_invert = apply_linop ▷ ksp_solve ▷ scale_untransform [▷ project]` lifts cleanly
(identity-in-form to the firm L2 body), while its eigen-iteration loop — the Krylov-Schur restart, the
Arnoldi/Lanczos basis extension, the Rayleigh-Ritz extraction, the convergence test — is **entirely
inside SLEPc / ARPACK**. The L3 form names the loop `eigen_iterate` by role and attaches a first-class
[`sequential-obstruction`](../concepts/sequential-obstruction.md) **marker** rooted in
opaque-library-ownership (it cannot render the loop — Palace authors no recurrence). At L2 that loop
view is **erased**: the `eigen_iterate` fold is referenced by role only, and the named obstruction
shadows to the L2 §"Algebraic laws" non-laws (the "Opening of the eigen-iteration fold at L2" non-law
+ the fold-merge / restart-associativity non-laws). This is the **opaque-library** counterpart of the
sibling substantive themes [`ksp-solve-outer-driver`](./ksp-solve-outer-driver.md) (**unconditional** —
the whole operator IS a Palace-authored loop) and [`orthogonalize-variant-split`](./orthogonalize-variant-split.md)
(**variant-conditional** — one Palace-authored MGS branch). The distinguishing feature: the other two
substantive themes *render* the loop at L3 (a tail recursion) and L2 erases the rendering; **here L3
cannot render the loop at all** (no Palace recurrence exists), so the L3 "rendering" is itself only an
obstruction marker at the library boundary, and the L2 surface drops the marker. The per-step body is
identity-in-form across the hop (shared with the BLAS-1 `-body-identity` cohort discipline) — it is NOT
the substantive content of this hop.

## Slug

`eigsolve-opaque-eigen-iteration`

## Context

The `eigsolve` lowering chain spans the layer-edges of the artifact:

- **L1 firm** ([`L1/eigsolve`](../L1/eigsolve.md), cycle-022) — the opaque eigensolver-as-operator
  collapse `(E, control) -> EigResult`; the eigen-iteration loop, the per-step transformed-operator
  application, the inner linear solve, and the result extraction are all invisible (an eigensolve is
  one indivisible operator application). The eigensolver `E` is a black box mapping a problem to its
  eigenpairs.
- **L2 firm** ([`L2/eigsolve`](../L2/eigsolve.md), cycle-023) — the **named shift-invert
  spectral-transform composition**: the per-step body `apply_shift_invert = apply_linop ▷ ksp_solve`
  opened, and the eigen-iteration fold `eigen_iterate` **named by role only** (the iteration view
  erased). The RHS of this theme. This is a **partial-opening** named composition: it opens the fold
  body but leaves the fold itself opaque-library-owned — the structural reason the L3 backfill is
  `partial-obstruction`.
- **L2>L1 firm** ([`L2-L1/eigsolve-spectral-transform-composition`](../L2-L1/eigsolve-spectral-transform-composition.md),
  cycle-025) — the partial un-collapse of the L1 opacity into the named shift-invert composition;
  non-identity (the L1 opaque `E.linear` opened into the explicit inner `ksp_solve` inverting
  `(K − σM)`; the loop half stays collapsed). The body-half analogue of this theme on the L2↔L1 edge.
- **L3 firm `partial-obstruction`** ([`L3/eigsolve`](../L3/eigsolve.md), cycle-024) — the
  **iteration-rotation** view: the value-threaded `(E, control) -> EigResult` with the per-step body
  `apply_shift_invert` rendered as a whole-tensor value-threaded expression (it lifts), and the
  eigen-iteration loop rendered as an **explicit obstruction marker** — `eigen_iterate` named by role
  with a cited opaque-library `sequential-obstruction` (the loop does not lift and cannot even be
  rendered as a tail recursion, because Palace authors no loop). The **third** `partial-obstruction`
  L3 operator, and the first whose obstruction is rooted in opaque-library-ownership. The LHS of this
  theme.
- **L3>L2 firm — this theme.** Narrates how the L3 iteration-rotation form lowers into the L2 named
  composition. **Substantive (non-identity)** on the loop (the obstruction *marker* is erased and the
  named obstruction shadows to the L2 non-laws); identity-in-form on the per-step body.

This theme is the **third substantive L3>L2 theme**, after [`ksp-solve-outer-driver`](./ksp-solve-outer-driver.md)
(cycle-021, the first) and [`orthogonalize-variant-split`](./orthogonalize-variant-split.md) (cycle-044,
the second). All three share the structural shape "substantive iteration-rotation erasure" — the L3
iteration form dissolves into the L2 surface where the iteration view is erased and the obstruction
survives only as L2-vocabulary non-laws. The **distinguishing feature** of this theme is the erasure
scope: the loop is **opaque-library-owned**, living *entirely outside Palace*. See §"Erasure-scope
taxonomy contrast".

## L3 form (LHS)

The L3 form is reproduced from [`L3/eigsolve`](../L3/eigsolve.md) §"Value-threaded form (L3 rendering)"
— the value-threaded fold whose body is rendered explicitly and whose loop is named-by-role with an
obstruction marker:

    eigsolve :: (E, control) -> EigResult
    eigsolve E control =
      let (op, st0)  = setup E control                  -- bind K, M, [C, A2]; bind σ, mode; bind op.inv = E.linear; seed from control.initial_space
      let pairs      = eigen_iterate op st0 apply_shift_invert  -- OPAQUE library fold (SLEPc EPSSolve / ARPACK naupd RCI) — NOT renderable as iterate_while_L3
      in extract_eigpairs op pairs                       -- un-transform (l * gamma) + normalize + residual + count→status
      where
        apply_shift_invert op v =                        -- the per-step body that LIFTS (whole-tensor; identity-in-form to L2)
          let w  = apply_linop op.operand v
          let y  = ksp_solve op.inv w
          let y' = scale_untransform op y
          in if op.has_projector then apply_linop op.projector y' else y'

The L3 form is value-threaded (positional `(op, st)`; no `Solve` monad, no `readonly`, no L1 opacity).
It carries the **opaque-library `sequential-obstruction`** (per [`L3/eigsolve`](../L3/eigsolve.md)
§"Iteration-rotation marker"): the `eigen_iterate` fold does not lift to a closed-form whole-tensor
operation, **and unlike [`ksp-solve-outer-driver`](./ksp-solve-outer-driver.md) it cannot even be
rendered as an explicit `iterate_while_L3` tail recursion** — because Palace authors no eigen-iteration
recurrence at all. The `where`-bound `apply_shift_invert` is the only Palace-authored, L3-renderable
piece; `eigen_iterate` is named by role with the obstruction marker attached. This is the L3 entry's
reason to exist: **the body-lifts / loop-doesn't split, where the loop's non-lift is because Palace
authors no loop.**

## L2 form (RHS)

The L2 form is reproduced from [`L2/eigsolve`](../L2/eigsolve.md) §Signature — the named shift-invert
composition with the eigen-iteration fold named by role and the iteration view erased:

    eigsolve :: (E: EigSolver[problem], control: EigControl) -> EigResult[N, K_max]
    eigsolve E control =
      let (op, st)   = setup E control                       -- bind problem operators (K, M, [C, A2]); bind σ, mode; bind inner solver E.linear; seed basis
      let pairs      = eigen_iterate op st apply_shift_invert  -- the OPAQUE library eigen-iteration (SLEPc EPS / ARPACK RCI) — named by role, NOT opened
      in extract_eigpairs op pairs                            -- un-transform (shift / scaling) + normalize + residual + count→status
    where
      apply_shift_invert op v =
        let w  = apply_linop op.operand v        -- apply_linop against M (linear) / the PEP block L₁ operand (quadratic)
        let y  = ksp_solve op.inv w              -- inner ksp_solve inverting the shifted operator (K − σM)
        in scale_untransform op y                -- the per-backend γ / δ un-scale

The L2 form names the eigen-iteration fold `eigen_iterate` **by role** — it is the opaque library
iteration (SLEPc Krylov-Schur / ARPACK RCI Arnoldi) folding the per-step `apply_shift_invert`
application — and opens **only its body**. The iteration view is **erased** per
[`L2/index`](../L2/index.md) §Context: the L2 entry names the fold opaque and does not render it as
recursion. **No `sequential-obstruction` is named at L2.** The obstruction survives only as the L2
§"Algebraic laws" non-laws:

- **"Opening of the eigen-iteration fold at L2"** does not hold (unlike [`ksp_solve`](../L2/ksp_solve.md),
  whose Palace-authored fold IS opened at L2, `eigsolve`'s fold is the opaque library iteration and is
  not opened — there is no Palace-authored eigen-step kernel / eigen-iteration driver pair) — the L2
  statement of "the eigen-iteration is library-owned," without rendering the iteration.
- **"Fold-merge / restart associativity"** does not hold (the library Krylov-Schur restart re-seeds
  the basis; iterating two restart cycles is not iterating one double-length cycle) — the L2 statement
  of "the iteration is sequential and library-internal," without naming the iteration.

## Rewrite shape

The rewrite is the **substantive erasure of the opaque-library iteration view**, with the per-step body
identity-in-form. There is no "rendering to dissolve" subject here in the way the sibling themes have:
the L3 form does not render the loop as a tail recursion (Palace authors none), so the L3 loop view is
itself only an **obstruction marker at the library boundary**, and the substantive content of this hop
is the *erasure of that marker* — the L2 surface references the library fold by role and drops the
marker, shadowing it to the L2 non-laws.

1. **The per-step body is identity-in-form.** The L3 inner-step body — `apply_linop(op.operand, v)`,
   inner `ksp_solve(op.inv, ·)`, `scale_untransform`, optional `apply_linop(op.projector, ·)` — maps
   line-for-line to the L2 `apply_shift_invert` composition (the L2 §Signature `apply_shift_invert` is
   exactly this body with the same `apply_linop ▷ ksp_solve ▷ scale_untransform` three-stage shape).
   This is the same body-identity the BLAS-1 `-body-identity` cohort records for its leaves; it is
   **not the substantive content of this hop** (the body is the L2>L1 edge's open-vs-collapse subject,
   and is shared identity-in-form across the L3↔L2 edge). The single supporting surface adjustment is
   that L3 lists the optional divergence-free projection tail as an explicit `if op.has_projector`
   branch while L2 names it as a constituent of the composition's tail — information-preserving.

2. **The L3 opaque-library `sequential-obstruction` MARKER erases from the surface, shadowing to the
   L2 non-laws.** This is the load-bearing forward-narration step. At L3 the obstruction is named and
   first-class — `eigen_iterate` is named by role *with an attached obstruction marker* (the loop does
   not lift, and cannot be rendered as a tail recursion because Palace authors no loop). At L2 the
   iteration view is erased, so the obstruction marker is **not expressible** at the surface (the L2
   `eigen_iterate` is a plain role reference, no marker) — but it is not *gone*: it survives as the
   L2-vocabulary residue in the two §"Algebraic laws" non-laws above ("Opening of the eigen-iteration
   fold at L2" + "Fold-merge / restart associativity"). The L2 entry itself states the handoff
   explicitly (§Semantics phase 2 / §Status): "the **eigen-iteration loop does not lift** — it is
   opaque-library-owned … with **no Palace-authored eigen-step kernel / eigen-iteration driver pair**
   analogous to the `(krylov-step, ksp_solve)` pair … the L3 judgment is about the *loop* (a
   `sequential-obstruction` rooted in library-ownership)." This theme is the forward narration of that
   handoff: **obstruction marker named-at-the-library-boundary at L3 → marker erased to its non-law
   shadow at L2.**

The mapping at the fold's structural level:

| L3 line | L2 line | Mapping |
|---|---|---|
| `let (op, st0) = setup E control` | `let (op, st) = setup E control` | Identity (renamed `st0`→`st`). Same destructuring: bind problem operators `K`, `M`, `[C, A2]`; bind the shift `σ` and spectral-transform mode (STSINVERT/STPRECOND); bind the inner solver `op.inv = E.linear`; seed the eigen-iteration state from `control.initial_space`. L0 anchors `slepc.cpp:379-394` (shift-invert binding), `slepc.cpp:364-367` / `arpack.cpp:191-194` (`opInv = &ksp`). |
| `let pairs = eigen_iterate op st0 apply_shift_invert`  *(named-by-role + obstruction marker)* | `let pairs = eigen_iterate op st apply_shift_invert`  *(named-by-role only)* | **Substantive (non-identity).** The L3 `eigen_iterate` carries an explicit obstruction marker (the loop does not lift / is not renderable); the L2 `eigen_iterate` is a plain role reference with the iteration view erased. **This is the line where the iteration-rotation marker is erased — the heart of the hop.** Both reference the *same* opaque library fold (SLEPc `EPSSolve(eps)` `slepc.cpp:694`; ARPACK `naupd` RCI `arpack.cpp:318`, loop `:315-339`); neither opens it — but L3 marks it as the load-bearing obstruction, L2 drops the marker. |
| (the opaque-library `sequential-obstruction` named in §"Iteration-rotation marker") | (no surface statement; shadows to §"Algebraic laws" non-laws) | **Substantive (non-identity).** The L3 first-class obstruction marker is **erased** from the L2 surface (no rendered/marked iteration to attach it to) and survives only as the L2 "Opening of the eigen-iteration fold at L2" non-law + the "Fold-merge / restart associativity" non-law. |
| the `where`-bound `apply_shift_invert` body (`apply_linop ▷ ksp_solve ▷ scale_untransform [▷ project]`) | the `where`-bound `apply_shift_invert` body (same three-stage composition) | Identity-in-form. The per-step tensor-field body maps line-for-line; same `apply_linop`/`ksp_solve`/`scale_untransform` calls. Not the substantive content (shared with the BLAS-1 `-body-identity` cohort discipline). L0 witness `arpack.cpp:562-590` (`ApplyOp`) / `slepc.cpp:1847-1876` (`__pc_apply_EPS`). |
| `in extract_eigpairs op pairs` | `in extract_eigpairs op pairs` | Identity. Same firm-L1 readout: un-transform (`GetEigenvalue` `l * gamma`, `slepc.cpp:711-716`), normalize (`RescaleEigenvectors`, `slepc.cpp:707`), residual, count→`EigStatus`. Referenced from L1, unchanged across the hop. |

The mapping is total on the fold's structure, but it is **not** the identity-in-form mapping of the
BLAS-1 `-body-identity` cohort: the central line (the fold) carries a genuine erasure (obstruction
marker → non-law shadow). The surrounding lines (setup / body / extract) are identity modulo the
`st0`→`st` rename. The substantive content is the single fold line and its obstruction-marker shadow.

## The opaque-library distinction (why the loop has no L3 rendering)

The load-bearing distinction from the two sibling substantive themes: for
[`ksp-solve-outer-driver`](./ksp-solve-outer-driver.md) and
[`orthogonalize-variant-split`](./orthogonalize-variant-split.md), **Palace authors the loop**. The
L3 form *renders* it as an explicit `iterate_while_L3` (resp. MGS `jloop`) tail recursion, and the L2
surface erases the rendering to a role reference. The substantive content of those hops is the
dissolution of an explicit Palace-authored recursion.

For `eigsolve`, **Palace authors no loop.** The eigen-iteration is reverse-communication-interface
(RCI) at ARPACK — Palace's `while(true)` loop (`arpack.cpp:315-339`) is a *callback dispatcher*: it
calls the opaque ARPACK driver `naupd` (`arpack.cpp:318`) and dispatches the per-step matvec `ApplyOp`
only when `naupd` returns the reverse-communication tag `ido == 1 || ido == -1` (`arpack.cpp:323-326`),
breaking on `ido == 99` (`arpack.cpp:330-333`). All eigen-iteration *logic* (basis extension, restart,
Rayleigh-Ritz, convergence) is inside `naupd`. At SLEPc the entire iteration is one opaque call
`EPSSolve(eps)` (`slepc.cpp:694`, inside `SlepcEPSSolverBase::Solve` `:687-709`) — Palace supplies only
the PC-shell callback `__pc_apply_EPS` and the A0/A1 shell matvecs; there is no Palace loop at all.

So the L3 "rendering" of the loop is **not** a tail recursion — it is an **obstruction marker at the
library boundary**, naming `eigen_iterate` by role and citing the opaque-library `sequential-obstruction`.
The L3>L2 hop therefore does not dissolve a rendering (there is none); it **erases the marker**. This is
the **opaque-library** erasure scope: the third root after unconditional (Palace-authored loop IS the
operator) and variant-conditional (Palace-authored loop on one branch). The routing consequence (per
the CLAUDE.md obstruction sub-kind taxonomy): the underlying obstruction is `opaque-library-ownership`
— there is no Palace upstream change that would let L3 render the loop; the loop is permanently
library-owned. The theme's value is documenting the boundary and the erasure, not anticipating a future
rendering.

## Applicability conditions

The rewrite is valid when all of the following hold (satisfied for the firm L3 and L2 forms by
construction):

1. **The L3 form is the firm `L3/eigsolve` opaque-library `partial-obstruction`.** The value-threaded
   `(E, control) -> EigResult` with the per-step body `apply_shift_invert` rendered as a whole-tensor
   expression and the `eigen_iterate` loop named-by-role with the opaque-library obstruction marker. If
   a future Palace re-architecture exposed a Palace-authored eigen-iteration kernel/driver pair (highly
   unlikely — the iteration is SLEPc/ARPACK-owned), the erasure narration would need re-audit against
   the new loop. Per the opaque-library-ownership obstruction sub-kind (CLAUDE.md §Methodology
   invariants), there is no conventional promotion route; the theme stays as boundary documentation.
2. **The L2 form is the firm `L2/eigsolve` named shift-invert composition.** The
   `apply_shift_invert = apply_linop ▷ ksp_solve` body opened, with the `eigen_iterate` fold named by
   role and the iteration view erased per [`L2/index`](../L2/index.md) §Context, and the obstruction's
   shadow present as the "Opening of the eigen-iteration fold at L2" + "Fold-merge / restart
   associativity" non-laws. The firm L2 entry's §"Lifts to" records the reverse (L2 role-reference fold
   ⟷ L3 partial-obstruction marker) in-line; this theme narrates the forward L3→L2.
3. **The per-step body's L3>L2 rotation is identity-in-form.** This theme's substantive content is the
   *loop* (the opaque-library obstruction marker erasure), not the body. The body identity relies on
   the `apply_linop` / `ksp_solve` L3-native classification (`apply_linop` whole-tensor by signature
   shape; `ksp_solve` whole-tensor in / whole-tensor out by the firm L3 [`ksp_solve`](../L3/ksp_solve.md)
   signature), stable for the constituents `apply_shift_invert` is built from.
4. **The variant-axis profiles are aligned across the hop.** Both forms close over the same five-axis
   profile (three opened — spectral-transformation, problem-type, scaling; two collapsed/informational —
   backend-orchestration, element-type). The **backend-orchestration** axis (`arpack-rci | slepc-st-shell`)
   is the load-bearing one for this theme: **both** backend loops are opaque-library-owned, so the
   collapse of the axis at L2 is consistent with the obstruction-marker erasure (neither backend exposes
   a Palace-authored loop, so the axis collapses without exposing a renderable loop on either arm). The
   rotation does not interact with the spectral-transformation / problem-type / scaling axes (those shape
   the body's operand/inversion, not the loop).

## Justification kind

**`structural`** (dominant) with secondary **`obstruction`**.

**Structural (dominant)**: the substantive content is a structural fact about the layer surfaces — L3
attaches an obstruction marker to the `eigen_iterate` role reference (a structural form: the named
sequential-obstruction), L2 erases the marker to a plain role reference (a structural absence). The
opaque-library `sequential-obstruction`'s erasure-to-non-law-shadow is structural: the obstruction is a
property of the marked iteration view, so erasing the marking erases the named obstruction, leaving only
the L2-expressible residue (the fold-not-opened / non-mergeability non-laws). This is a claim about the
shapes of the two forms (marked role reference vs plain role reference; named obstruction vs non-law
shadow), not about algebraic laws on the body or step-semantics — hence structural. The contrast with
the body (identity-in-form) is itself a structural observation: the body's primitive sequence is
shape-invariant across the hop, the loop's iteration view (marker) is not.

**Obstruction (secondary)**: the obstruction is a first-class output of this theme (per the abstractor
discipline that negative results are first-class). The obstruction sub-kind is **opaque-library-ownership**
(per CLAUDE.md §Methodology invariants "Obstruction themes have two sub-kinds"): the eigen-iteration is
available to Palace ONLY through the SLEPc/ARPACK library boundary, never exposed as a standalone
Palace-authored callable. The negative anchors (the SLEPc `EPSSolve` single-call site, the ARPACK
`naupd` RCI callback-dispatch loop) witness the opaque-library-ownership boundary. This theme is NOT a
whole-operator obstruction (the operator IS implemented and its body IS lifted) — it is the L3>L2-edge
narration of a `partial-obstruction` L3 entry whose obstruction is the opaque-library loop. The
secondary `obstruction` kind records that the erased thing is a library-boundary obstruction, not a
Palace-authored recurrence.

**Abstraction-direction note**: L3 is the higher-abstraction layer for this edge (it has the iteration
rotation attempted and the opaque-library obstruction marked); L2 is the lower-abstraction layer (it
references the library fold by role and erases the marker). The rotation direction is L3 → L2: the L3
form lowers to the L2 form by **erasing** the obstruction marker to its non-law shadow and leaving the
body identity-in-form. This matches the methodology's high→low lowering direction; the reverse (how the
L2 role-reference fold + non-laws re-acquire the L3 obstruction marker) is a working-note / OQ concern,
recorded only in the L2 entry's §"Lifts to" and the L3 entry's in-line lift notes, not narrated here.

## Speculative L3 operators

**None.** This theme is the substantive opaque-library erasure rotation between two firm endpoints; no
new L3 vocabulary is introduced. The L3 form referenced in the LHS is the firm
[`L3/eigsolve`](../L3/eigsolve.md) entry; the L2 form referenced in the RHS is the firm
[`L2/eigsolve`](../L2/eigsolve.md) entry. The per-step body's `apply_linop` / `ksp_solve` /
`scale_untransform` constituents are firm at both layers ([`L3/apply_linop`](../L3/apply_linop.md),
[`L3/ksp_solve`](../L3/ksp_solve.md); the L2 siblings); they are referenced, not introduced. The
`eigen_iterate` fold is named-by-role at both layers (it is opaque-library-owned and never a Palace
callable); it is referenced, not introduced.

## Erasure-scope taxonomy contrast

The three substantive L3>L2 themes share the structural shape "iteration-rotation erasure" but differ
in **scope of the erasure** — the taxonomy axis the L3-L2 §Working-Notes flagged for the meta-phase:

| | [`ksp-solve-outer-driver`](./ksp-solve-outer-driver.md) | [`orthogonalize-variant-split`](./orthogonalize-variant-split.md) | `eigsolve-opaque-eigen-iteration` (this theme) |
|---|---|---|---|
| L3 form | explicit `iterate_while_L3` tail recursion + named outer-loop `sequential-obstruction` | `case op.variant`: CGS/CGS2 global statements + explicit MGS `jloop` tail recursion + named MGS `sequential-obstruction` | `eigen_iterate` named-by-role **with obstruction marker** (NOT a tail recursion — Palace authors no loop) |
| L2 form | `iterate_while (krylov-step op) …` named-by-role; obstruction erased | `project ▷ subtract` per-variant-sequenced; iteration view erased; difference disclosed as residual axis | `eigen_iterate` named-by-role only; obstruction marker erased |
| substantive content | iteration view erased; obstruction shadows to L2 fold non-laws | **MGS branch only:** iteration view erased; obstruction shadows to column-order non-law + `m×1` residual axis | obstruction **marker** erased; shadows to "Opening of the eigen-iteration fold at L2" + "Fold-merge / restart associativity" non-laws |
| erasure scope | **unconditional** — the whole operator IS a Palace-authored loop | **variant-conditional** — one Palace-authored MGS branch; CGS/CGS2 clean lifts | **opaque-library** — the loop lives *entirely outside Palace* (SLEPc `EPSSolve` / ARPACK RCI) |
| does L3 *render* the loop? | yes — explicit tail recursion | yes (MGS branch) — explicit `jloop` tail recursion | **no** — Palace authors no recurrence; L3 attaches an obstruction marker at the library boundary |
| obstruction root | trajectory scalars gate the next step (intrinsic step-boundary sequentiality) | MGS roundoff-orthogonality (numerical-stability-rooted) | **opaque-library-ownership** (the eigen-iteration is SLEPc/ARPACK-owned) |
| obstruction sub-kind | (Palace-authored loop; sequential-obstruction, not library) | (Palace-authored MGS branch; sequential-obstruction, not library) | **`opaque-library-ownership`** (per CLAUDE.md) — never re-promotable |

The distinguishing structural fact this theme records: **a substantive L3>L2 iteration-rotation
erasure can arise from a loop Palace never authored.** For the other two themes the L3 form renders a
Palace-authored recursion and L2 erases the rendering; here the L3 form can only *mark* a library
boundary, and L2 erases the mark. This is the **opaque-library** erasure root — the third corner of the
erasure-scope taxonomy (unconditional / variant-conditional / opaque-library). It is the L3>L2-edge
expression of the L3 entry's **opaque-library partial-obstruction** verdict: the partial-obstruction is
rooted in opaque-library-ownership, and so is this theme's substantive erasure.

## Verified-against

L3 evidence (the LHS):

- `book/src/L3/eigsolve.md` (firm `partial-obstruction`, cycle-024) — the L3 opaque-library form this
  theme references as LHS. §"Value-threaded form (L3 rendering)" (the `eigen_iterate` named-by-role with
  the obstruction marker; `apply_shift_invert` `where`-bound body), §"Iteration-rotation marker" (the
  body-lifts / loop-doesn't split, loop's non-lift because Palace authors no loop), §Status (the
  `partial-obstruction` reflecting the loop structure, rooted in opaque-library-ownership), §"Lowers to"
  + §"L3 vs L2 distinction" (records the L3>L2 hop as the body identity-in-form + the loop view erased —
  the same rotation this theme narrates forward; re-anchored by this dispatch to point at this theme for
  the substantive loop-erasure).
- `book/src/L3/apply_linop.md`, `book/src/L3/ksp_solve.md` (firm) — the L3 per-step body constituents,
  identity-in-form across the hop.

L2 evidence (the RHS):

- `book/src/L2/eigsolve.md` (firm, cycle-023) — the L2 named composition this theme references as RHS.
  §Signature (the `apply_shift_invert = apply_linop ▷ ksp_solve` body opened + the `eigen_iterate` fold
  named by role), §Semantics phase 2 (the fold body opened / the loop opaque + named-by-role), §"Algebraic
  laws" non-laws "Opening of the eigen-iteration fold at L2" + "Fold-merge / restart associativity" (the
  L2-vocabulary shadow of the erased opaque-library obstruction marker), §"Lifts to" (records the reverse
  direction in-line: L2 role-reference fold ⟷ L3 partial-obstruction marker; the predicted
  `partial-obstruction` L3 backfill this theme's LHS confirmed).

Sibling-theme evidence (the substantive-theme precedents + the body-edge sibling):

- `book/src/L3-L2/ksp-solve-outer-driver.md` (firm, cycle-021) — the first substantive L3>L2 theme; the
  structural precedent for the iteration-view erasure + obstruction-to-non-law shadow rotation. The
  **unconditional** erasure-scope corner. This theme's §"Erasure-scope taxonomy contrast" extends that
  precedent's contrast template to the opaque-library axis.
- `book/src/L3-L2/orthogonalize-variant-split.md` (firm, cycle-044) — the second substantive L3>L2 theme;
  the **variant-conditional** erasure-scope corner. Its §"Variant-split / unconditional-erasure contrast"
  is the two-corner table this theme extends to three corners.
- `book/src/L2-L1/eigsolve-spectral-transform-composition.md` (firm, cycle-025) — the body-half analogue
  on the adjacent L2↔L1 edge: the partial un-collapse of the L1 opacity into the named shift-invert
  composition (the body opened; the loop left collapsed). This theme is the L3↔L2-edge counterpart on the
  loop (the body is identity-in-form here; the loop's marker is erased).

L0 evidence (self-verified against `reference/palace/` source on-disk via `read_range` + `citecheck
--anchor` this dispatch; the codemap is localization-only, citecheck/on-disk is the citation source of
truth per the cycle-027 brace-drift guard):

- `reference/palace/palace/linalg/slepc.cpp:687-709` — `SlepcEPSSolverBase::Solve` (def `:687-709`): the
  **SLEPc eigen-iteration entry that does NOT lift / is NOT renderable.** `Customize()` (`:693`) then the
  entire opaque library iteration `EPSSolve(eps)` (`:694`); `EPSGetConverged(eps, &num_conv)` (`:695`);
  `RescaleEigenvectors(num_conv)` (`:707`). The decisive negative anchor for the opaque-library
  obstruction marker: the SLEPc eigen-iteration is a **single opaque library call** — there is no Palace
  loop at all to render.
- `reference/palace/palace/linalg/slepc.cpp:694` — `EPSSolve(eps)`: the opaque library eigen-iteration
  call (the fold L3 marks / L2 names by role). Anchor verified (`citecheck --anchor 'EPSSolve'`).
- `reference/palace/palace/linalg/arpack.cpp:315-339` — the **ARPACK RCI eigen-iteration loop that does
  NOT lift / is a callback dispatcher, not a renderable Palace recurrence.** The RCI `while(true)` loop
  (`:315`) calling the opaque ARPACK driver `naupd` (`:318`), dispatching `ApplyOp(&workd[ipntr[0]-1],
  &workd[ipntr[1]-1])` only on `ido == 1 || ido == -1` (`:323-326`), breaking on `ido == 99` (`:331`).
  The decisive negative anchor: Palace's loop body is a callback dispatcher — the eigen-iteration logic
  (basis extension, restart, convergence) is inside `naupd`. No Palace-authored eigen-step kernel /
  eigen-iteration driver pair.
- `reference/palace/palace/linalg/arpack.cpp:318` — `naupd(...)`: the opaque ARPACK driver (the fold L3
  marks / L2 names by role). Anchor verified (`citecheck --anchor 'naupd'`).
- `reference/palace/palace/linalg/arpack.cpp:562-590` — `ArpackEPSSolver::ApplyOp`: the **per-step body
  that LIFTS** (explicit Palace-owned shift-invert composition). Shift-invert branch `opM->Mult(x1, z1);
  opInv->Mult(z1, y1); y1 *= gamma` (`:579-581`); no-transform branch `opK->Mult(x1, z1); ...` (`:572-575`);
  divergence-free projection tail `opProj->Mult(y1)` (`:586`). The positive anchor that the body is
  Palace-authored and lifts (identity-in-form to the L2 body); contrasted with the un-renderable loop.
- `reference/palace/palace/linalg/slepc.cpp:1847-1876` — `__pc_apply_EPS`: the **SLEPc per-step body that
  LIFTS** (the shift-invert inverse-apply `y = (K − σM)⁻¹ x`). The inner solve `ctx->opInv->Mult(ctx->x1,
  ctx->y1)` (`:1858`); the un-scale tails (`:1861` / `:1865`); the projection tail `opProj->Mult(y1)`
  (`:1870`). The positive anchor that the SLEPc backend realizes the identical `apply_linop ▷ ksp_solve`
  body (the body identity-in-form, second assembly site).
- `reference/palace/palace/linalg/slepc.cpp:379-394` — `SlepcEigenvalueSolver::SetShiftInvert`: STPRECOND
  (`:384`) vs STSINVERT (`:388`); `STSetMatMode(st, ST_MATMODE_SHELL)` (`:391`). The setup-line spectral-
  transform binding (the identity setup-line of the hop).
- `reference/palace/palace/linalg/slepc.cpp:364-367` / `arpack.cpp:191-194` — `SetLinearSolver`: `opInv =
  &ksp` (the inner-solver binding `op.inv = E.linear`; the identity setup-line of the hop).
- `reference/palace/palace/linalg/slepc.cpp:711-716` — `SlepcEPSSolverBase::GetEigenvalue`: `return l *
  gamma` (`:715`) — the eigenvalue un-transform at the extraction boundary (the identity `extract_eigpairs`
  line of the hop).

Cross-cutting concept references (consumed unchanged across the rotation):

- `book/src/concepts/sequential-obstruction.md` (firm) — the canonical write-up of the loop obstruction;
  marked first-class at L3 (rooted in opaque-library-ownership), erased to the non-law shadow at L2.
- `book/src/concepts/solve-monad.md` — the (future, unauthored) L4 outer-coordination surface; the L1
  entry anchors it (sum-typed termination richer than `ksp_solve`'s soft-fail). The L2 named composition
  is the per-step body that L4 surface would fold; the eigen-iteration loop it would fold is library-owned.
- `book/src/concepts/solver-as-operator.md`, `book/src/concepts/constructed-operators.md`,
  `book/src/concepts/variant-absorption.md` — the inner `ksp_solve` consumed as an operator, the shifted
  constructed operator `(K − σM)`, the backend-orchestration absorption (both arms opaque-library-owned).

Strawman / combinator evidence:

- `book/src/semantics/index.md` §3.7 — the `iterate_while` conventions; the natural L4 composition
  target for the eigen-iteration loop *if* Palace authored it — but the loop is library-owned, so the
  L4/L3 treatment is the `partial-obstruction` case, NOT a clean `iterate_while` fold. The L3 form does
  not render the loop as `iterate_while_L3` (unlike `ksp_solve`); this theme records that absence as the
  opaque-library erasure-scope corner.

Open-questions ledger:

- `scaffolding/open-questions.md` slug `l3-l2-substantive-erasure-scope-taxonomy` (the meta-phase-flagged
  taxonomy question from the L3-L2 §Working-Notes) — this theme supplies the third corner
  (opaque-library) of the unconditional / variant-conditional / opaque-library axis. Surfaced in this
  CYCLE.md §Open questions for the meta-phase to consider naming the taxonomy across the substantive cohort.

## Status

`firm` — the theme's content is firm: both endpoints are firm ([`L3/eigsolve`](../L3/eigsolve.md)
cycle-024 `partial-obstruction`; [`L2/eigsolve`](../L2/eigsolve.md) cycle-023); the substantive
non-identity content (the opaque-library obstruction-marker erasure + the marker's shadow-to-non-laws)
is structurally grounded and citation-backed at both layers and the L0 source (the SLEPc `EPSSolve`
single-call site + the ARPACK `naupd` RCI callback-dispatch loop are the decisive negative anchors for
the un-renderable-loop / opaque-library-ownership claim); the per-step body's L3>L2 rotation is
identity-in-form (the `apply_linop ▷ ksp_solve ▷ scale_untransform` body maps line-for-line, witnessed
at both the ARPACK `ApplyOp` and SLEPc `__pc_apply_EPS` assembly sites); the rewrite-shape table is
total on the fold structure with the single non-identity line (the fold's obstruction-marker erasure)
explicitly delimited; no speculative L3 vocabulary is introduced; the four applicability conditions are
stated and confirmed. The erasure-scope taxonomy contrast positions this theme as the **third / final
erasure-scope root** (opaque-library) after the unconditional `ksp-solve-outer-driver` (cycle-021) and
the variant-conditional `orthogonalize-variant-split` (cycle-044), completing the substantive L3>L2
cohort across all three roots. This is the L3>L2-edge half of the `eigsolve` chain (L1-firm cycle-022 →
L2-firm cycle-023 → L3-firm `partial-obstruction` cycle-024 → L2>L1 cycle-025 → **this L3>L2 theme
cycle-045**).

Authored cycle-045 wave-1 (abstractor, D1), enacting **Layers are defined high→low** (LHS L3, RHS L2,
forward narration: the L3 obstruction marker erases into the L2 role-reference fold). Unlike the BLAS-1
`-body-identity` cohort (clean identity-lowerings) and the body-identity portion of this hop (the
`apply_shift_invert` body), the L3>L2 *loop* rotation here is **substantive** — the opaque-library
obstruction marker is erased and shadows down to the L2 "Opening of the eigen-iteration fold at L2" +
"Fold-merge / restart associativity" non-laws. The obstruction sub-kind is **opaque-library-ownership**
(per CLAUDE.md §Methodology invariants): there is no conventional promotion route; the theme documents
the library boundary and the erasure permanently.

## L3>L2 vs L2>L1 distinction (the body / loop division across two edges)

The `eigsolve` chain divides its substantive content across two adjacent edges, by subject:

- **L2>L1 ([`eigsolve-spectral-transform-composition`](../L2-L1/eigsolve-spectral-transform-composition.md),
  cycle-025; the BODY edge)**: the substantive content is the partial un-collapse of the L1 opacity into
  the named shift-invert composition — the L1 opaque `E.linear` opened into the explicit inner
  `ksp_solve`. The *body* is opened; the *loop* stays collapsed (named by role at both L2 and L1).
- **`eigsolve-opaque-eigen-iteration` (this theme, cycle-045; the LOOP edge)**: the substantive content
  is the opaque-library obstruction-marker erasure — the L3 marked `eigen_iterate` erased to the L2 plain
  role reference. The *loop* marker is erased; the *body* stays identity-in-form across the hop.

Together they record the full `eigsolve` story: the body is opened at L2>L1 and identity-in-form at
L3>L2; the loop is opaque-library-owned at every layer (named by role at L1/L2, marked as an obstruction
at L3, the marker erased at the L3>L2 hop). The body and the loop carry their substantive content on
*different edges* — the body on L2>L1, the loop-marker on L3>L2 — which is why neither edge is wholly
identity and neither is wholly substantive.
