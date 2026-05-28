---
agent: lifter
invoked_at: 2026-05-28T193413Z
scope: L4>L3 theme re-anchor — krylov-step-typed-wrapper-dissolution-cg-md-citation-sweep
status: integrated
integrated_at: 2026-05-29T003000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-014 position 7/8. 8/8 dangling cg.md pointers re-anchored in L4-L3/krylov-step-typed-wrapper-dissolution.md (theme lines 98/109/126/200/204/210/231/233; theme stays firm, no claim/structure change). Body-identity (Claim 2; 109/126/204/210/231) → L3-L2/krylov-step-body-identity.md:125; outer-loop sequential-obstruction (Claim 1; 98/200/233) → L3/krylov-step.md §Algebraic-laws + concepts/sequential-obstruction.md. Historical cg.md ranges retained as parenthetical provenance; arnoldi_step.md co-anchors (live slice) untouched. Theme-side OQ krylov-step-typed-wrapper-dissolution-cg-md-citation-sweep marked ANSWERED (finalize). Sibling residual on DISTINCT L3/krylov-step.md operator entry routed to cycle-015 OQ l3-krylov-step-cg-md-citation-sweep. Build clean."
inputs:
  - book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md
  - book/src/L3-L2/krylov-step-body-identity.md
  - book/src/spec/slices/cg.md
  - book/src/L3/krylov-step.md
  - book/src/spec/slices/arnoldi_step.md
---

# CYCLE: Re-anchor krylov-step-typed-wrapper-dissolution-cg-md-citation-sweep

## Summary
The L4>L3 theme `krylov-step-typed-wrapper-dissolution.md` still carries **8 dangling `cg.md:NNN-MMM` pointers** (theme lines 98, 109, 126, 200, 204, 210, 231, 233). The slice `book/src/spec/slices/cg.md` was reduced cycle-009 to a 165-line stub holding only the L4-v0.5 first-iteration-unrolling material; the L2→L3 rotation-claim content those pointers referenced (formerly at slice lines 341-362) **no longer exists in the slice** and was lifted into two firm entries. This is a pure citation re-anchor sweep applying the exact convention cycle-013's lifter established at theme line 20 (keep the historical range, annotate it as *lifted-and-superseded per the cycle-009 corpus reduction*, point at the firm home, note the still-live `arnoldi_step.md` co-anchor). No claims change, no structure changes, status stays `firm`.

The 8 dangling pointers split into two semantic families, each with a distinct firm home:

- **Body-identity (cycle-002 Claim 2, "step body lifts as identity")** — ranges `cg.md:341-362`, `cg.md:351-362`, `cg.md:352-362`. Lifted into firm [`L3-L2/krylov-step-body-identity`](../../book/src/L3-L2/krylov-step-body-identity.md), whose §Verified-against (line 125) preserves the `cg.md:341-362` range with the verbatim Claim-2 quote. Theme lines 109, 126, 204, 210, 231.
- **Outer-loop sequential-obstruction (cycle-002 Claim 1, the negative L3 result for the *outer* loop)** — ranges `cg.md:341-349`, `cg.md:347-350`. Lifted into firm [`L3/krylov-step`](../../book/src/L3/krylov-step.md) §Algebraic-laws non-lift catalogue + the [`sequential-obstruction`](../../book/src/concepts/sequential-obstruction.md) concept page; the co-cited `arnoldi_step.md:194-213` remains a **live** (non-reduced) anchor. Theme lines 98, 200, 233.

`arnoldi_step.md` (302 lines, reduced-status header but §L2/§L3 material retained) is **still live** — its `:178-213`, `:185-188`, `:194-213` pointers do NOT dangle and are left untouched.

## Proposed changes

All re-anchors apply the cycle-013 convention verbatim: the historical `cg.md` range is retained as a parenthetical lifted-evidence note (so the audit trail to the pre-reduction slice survives), immediately followed by the firm home it was lifted into and the live `arnoldi_step.md` co-anchor where one exists.

### Re-anchor 1 — §"What this lowering does NOT cover", outer-loop obstruction (line 98): `cg.md:341-349` (Claim 1)

```edit:book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md
[old]: - **Outer-loop sequential obstruction**. The fact that the *outer* `iterate_while` loop carries a `sequential-obstruction` at L3 (per `cg.md:341-349`, `arnoldi_step.md:194-213`) is a property of the loop, not of the step kernel. The step-body L4>L3 lowering described here is independent of the outer-loop obstruction. The loop obstruction is documented in the slice corpus's L3 sections and the `sequential-obstruction` concept page; this theme does not re-state it.
[new]: - **Outer-loop sequential obstruction**. The fact that the *outer* `iterate_while` loop carries a `sequential-obstruction` at L3 (the original CG evidence at `cg.md:341-349` has been lifted into the firm L3 entry [`L3/krylov-step`](../L3/krylov-step.md) §Algebraic-laws non-lift catalogue per the cycle-009 corpus reduction, and `arnoldi_step.md:194-213` remains the valid live anchor) is a property of the loop, not of the step kernel. The step-body L4>L3 lowering described here is independent of the outer-loop obstruction. The loop obstruction is documented in the firm L3 entry's non-lift catalogue and the [`sequential-obstruction`](../concepts/sequential-obstruction.md) concept page; this theme does not re-state it.
```

### Re-anchor 2 — §"Applicability conditions" condition 3 (line 109): `cg.md:351-362` (Claim 2)

```edit:book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md
[old]: 3. **The five primitive groups are L3-native or carry their own L3-edge classification.** Each of `apply_linop`, `axpy`, `axpby`, `axpbypcz`, `dot`, `nrm2`, `scal` is an L1 primitive whose L2>L3 lift is identity (per `cg.md:351-362`, `arnoldi_step.md:185-188`). The optional auxiliary stage (`op.orthog` under MGS) carries its own L3 obstruction (per `arnoldi_step.md:194-213`), which is independent of the `krylov-step` body rewrite. This dispatch's lowering does not introduce new L3 obstructions; it inherits the existing classification of its constituent primitives.
[new]: 3. **The five primitive groups are L3-native or carry their own L3-edge classification.** Each of `apply_linop`, `axpy`, `axpby`, `axpbypcz`, `dot`, `nrm2`, `scal` is an L1 primitive whose L2>L3 lift is identity (the original CG evidence at `cg.md:351-362` has been lifted into the firm theme [`L3-L2/krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md) §Verified-against per the cycle-009 corpus reduction; `arnoldi_step.md:185-188` remains the valid live anchor). The optional auxiliary stage (`op.orthog` under MGS) carries its own L3 obstruction (per `arnoldi_step.md:194-213`), which is independent of the `krylov-step` body rewrite. This dispatch's lowering does not introduce new L3 obstructions; it inherits the existing classification of its constituent primitives.
```

### Re-anchor 3 — §"Justification kind" (line 126): `cg.md:351-362` (Claim 2)

```edit:book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md
[old]: The combinator-miner's cycle-002 assertion (cited at `cg.md:351-362`) is justified as **`empirical-match`** at the L2>L3 edge — the slice corpus's L2 prose uses primitive-composition form that is L3-native by inspection, and the assertion is the recognition that no rewrite is needed. The L4>L3 hop covered here is a different rotation (typed wrapper to value-threaded form); it is **not** identity-in-form on the wrapper, only on the body. The two rotations compose to give an L4>L2 chain that is non-identity at the wrapper level and identity-in-form on the body — which is the harvester's "Lowers to" claim.
[new]: The combinator-miner's cycle-002 assertion (the original CG evidence at `cg.md:351-362` has been lifted into the firm theme [`L3-L2/krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md) §Verified-against per the cycle-009 corpus reduction) is justified as **`empirical-match`** at the L2>L3 edge — the slice corpus's L2 prose uses primitive-composition form that is L3-native by inspection, and the assertion is the recognition that no rewrite is needed. The L4>L3 hop covered here is a different rotation (typed wrapper to value-threaded form); it is **not** identity-in-form on the wrapper, only on the body. The two rotations compose to give an L4>L2 chain that is non-identity at the wrapper level and identity-in-form on the body — which is the harvester's "Lowers to" claim.
```

### Re-anchor 4 — §"What the L3 form for `iterate_while` looks like", closing prose (line 200): `cg.md:341-349` (Claim 1)

```edit:book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md
[old]: Both forms are tail-recursive value-threaded loops; the `Solve` monad has dissolved (the `sim` argument is positional, not monadic), and the `sequential-obstruction` of the outer loop survives at L3 (per `cg.md:341-349`) — the L3 form names the loop tail-recursively but does not claim it lifts to a global tensor-field op. This is the expected outcome for Krylov methods at L3 per `sequential-obstruction.md`. The unpruned form additionally allocates the trajectory list (an `O(N)` accumulator); the pruned form does not.
[new]: Both forms are tail-recursive value-threaded loops; the `Solve` monad has dissolved (the `sim` argument is positional, not monadic), and the `sequential-obstruction` of the outer loop survives at L3 (the original CG evidence at `cg.md:341-349` has been lifted into the firm L3 entry [`L3/krylov-step`](../L3/krylov-step.md) §Algebraic-laws non-lift catalogue per the cycle-009 corpus reduction; `arnoldi_step.md:194-213` remains the valid live anchor) — the L3 form names the loop tail-recursively but does not claim it lifts to a global tensor-field op. This is the expected outcome for Krylov methods at L3 per [`sequential-obstruction`](../concepts/sequential-obstruction.md). The unpruned form additionally allocates the trajectory list (an `O(N)` accumulator); the pruned form does not.
```

### Re-anchor 5 — §"Audit of cycle-002 identity-in-form claim", opening (line 204): `cg.md:351-362` / `cg.md:352-362` (Claim 2, OQ-ledger-recorded form)

The line quotes the open-questions ledger's recorded citation and then canonicalizes the range. Both `cg.md:351-362` and `cg.md:352-362` are Claim-2 (body-identity) ranges. The re-anchor preserves the historical OQ-ledger quote verbatim (it is a record of what the ledger recorded) and adds the lifted-home note where the canonicalized range now lives.

```edit:book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md
[old]: The open question `krylov-step-l3-identity-in-form-audit` (scaffolding/open-questions.md) records the combinator-miner cycle-002 assertion: "the L2→L3 rotation on the `krylov-step` body is identity-in-form, citing `cg.md:351-362` and `arnoldi_step.md:185-188`." (Note: the open-questions ledger records the citation as `cg.md:352-362`; the range that fully contains Claim 2 — including its `### Claim 2: step body lifts as identity` header at line 351 — is `cg.md:351-362`. This dispatch canonicalizes to the inclusive range.) This dispatch audits the assertion as the secondary half of its job.
[new]: The open question `krylov-step-l3-identity-in-form-audit` (scaffolding/open-questions.md) records the combinator-miner cycle-002 assertion: "the L2→L3 rotation on the `krylov-step` body is identity-in-form, citing `cg.md:351-362` and `arnoldi_step.md:185-188`." (Note: the open-questions ledger records the citation as `cg.md:352-362`; the range that fully contains Claim 2 — including its `### Claim 2: step body lifts as identity` header at line 351 — is `cg.md:351-362`. This dispatch canonicalizes to the inclusive range.) The CG half of this evidence (`cg.md:351-362`) has since been lifted into the firm theme [`L3-L2/krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md) §Verified-against per the cycle-009 corpus reduction; the historical slice ranges are retained here as the audit's provenance record, and `arnoldi_step.md:185-188` remains the valid live anchor. This dispatch audits the assertion as the secondary half of its job.
```

### Re-anchor 6 — §"Audit ... Evidence reviewed" item 1 (line 210): `cg.md:341-362` (Claim 2 re-read)

```edit:book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md
[old]: 1. `cg.md:341-362` (cited by combinator-miner; re-read for this audit) — the L2→L3 rotation claims for CG. Claim 2 ("step body lifts as identity") states verbatim: *"The L2→L3 rotation on the step body is therefore the **identity in form**: no unfolding, no global lift, no schema change."* The justification is that L2's primitive vocabulary (`apply_linop`, `axpy`, `axpby`, `dot`, scalar arithmetic) is already L3-native — each is a whole-tensor operation with no element loop exposed at L2. **Audit finding**: the assertion is well-supported; the L2 primitives are L3-native by inspection of their signatures (e.g., `apply_linop : LinOp -> Tensor[N] -> Tensor[N]` is a global field operation).
[new]: 1. `cg.md:341-362` (cited by combinator-miner; re-read for the cycle-006 audit; the range has since been lifted into the firm theme [`L3-L2/krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md) §Verified-against per the cycle-009 corpus reduction) — the L2→L3 rotation claims for CG. Claim 2 ("step body lifts as identity") states verbatim: *"The L2→L3 rotation on the step body is therefore the **identity in form**: no unfolding, no global lift, no schema change."* The justification is that L2's primitive vocabulary (`apply_linop`, `axpy`, `axpby`, `dot`, scalar arithmetic) is already L3-native — each is a whole-tensor operation with no element loop exposed at L2. **Audit finding**: the assertion is well-supported; the L2 primitives are L3-native by inspection of their signatures (e.g., `apply_linop : LinOp -> Tensor[N] -> Tensor[N]` is a global field operation).
```

### Re-anchor 7 — §"Verified-against", L3-evidence registry, body-identity row (line 231): `book/src/spec/slices/cg.md:341-362` (Claim 2)

```edit:book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md
[old]: - `book/src/spec/slices/cg.md:341-362` — the combinator-miner cycle-002 evidence for L2>L3 body identity. Claim 2 ("step body lifts as identity") is the cited support. Re-read for this audit; assertion confirmed.
[new]: - `book/src/L3-L2/krylov-step-body-identity.md` §Verified-against (line 125; lifted from the original `book/src/spec/slices/cg.md:341-362` per the cycle-009 corpus reduction) — the combinator-miner cycle-002 evidence for L2>L3 body identity. Claim 2 ("step body lifts as identity") is the cited support, preserved there with the verbatim claim quote. Re-read for the cycle-006 audit; assertion confirmed.
```

### Re-anchor 8 — §"Verified-against", L3-evidence registry, outer-loop row (line 233): `book/src/spec/slices/cg.md:347-350` (Claim 1)

```edit:book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md
[old]: - `book/src/spec/slices/cg.md:347-350` (Claim 1, outer-loop obstruction) — the negative L3 result for the *outer* loop. Cited for completeness; the outer-loop obstruction is independent of the step-body rotation handled by this theme.
[new]: - `book/src/L3/krylov-step.md` §Algebraic-laws non-lift catalogue (lifted from the original `book/src/spec/slices/cg.md:347-350` Claim 1 per the cycle-009 corpus reduction; `arnoldi_step.md:194-213` remains the valid live anchor) — the negative L3 result for the *outer* loop. Cited for completeness; the outer-loop obstruction is independent of the step-body rotation handled by this theme.
```

## Discipline notes

- **Pure citation re-anchor, no claim or structure change.** Every edit swaps a dangling `cg.md:NNN-MMM` slice-line pointer for the firm entry the content was lifted into, preserving the historical slice range as a parenthetical provenance note. No LHS/RHS shape change, no applicability-condition change, no justification-kind change. The theme's `firm` status is unchanged.
- **Convention inherited verbatim from cycle-013.** The lifted-evidence annotation pattern — "the original slice evidence at `cg.md:NNN-MMM` has been lifted into [firm entry] per the cycle-009 corpus reduction, and `arnoldi_step.md:NNN-MMM` remains the valid live anchor" — is exactly the phrasing the cycle-013 lifter applied at theme line 20 (`reports/2026-05-28T1447Z-lifter-krylov-step-theme-body-no-l3-row-drift-cycle-013/CYCLE.md` Re-anchor 1). This sweep completes the theme-wide consistency that cycle-013's report routed to OQ `krylov-step-typed-wrapper-dissolution-cg-md-citation-sweep`.
- **Two firm homes, by semantic family.** The body-identity content (Claim 2; theme lines 109/126/204/210/231) lives in firm `L3-L2/krylov-step-body-identity.md:125`, whose §Verified-against preserved the `cg.md:341-362` range with the verbatim Claim-2 quote when it was authored cycle-009. The outer-loop-obstruction content (Claim 1; theme lines 98/200/233) lives in firm `L3/krylov-step.md` §Algebraic-laws non-lift catalogue + `concepts/sequential-obstruction.md`. This split is faithful to the slice's original two-claim structure (Claim 1 = outer-loop negative result; Claim 2 = body-identity positive result).
- **`arnoldi_step.md` left untouched.** The slice is still live (302 lines; reduced-status header retains §L2/§L3 material). Its `:178-213`, `:185-188`, `:194-213` pointers resolve and are not dangling. The `first-iteration-unrolling.md:21-37` pointer at theme line 53 is not a `cg.md` pointer and is out of scope.
- **High→low direction preserved.** The theme remains defined L4 (LHS) into L3 (RHS); the re-anchors touch only citation pointers in the narrative, add no reverse-direction (L3→L4 lift) prose, and do not invert the rewrite direction. Friction-ledger `layer-definition-discipline-high-to-low`.
- **`sequential-obstruction.md` link upgraded inline.** Lines 98 and 200 referenced the concept page as bare prose `sequential-obstruction.md` / `\`sequential-obstruction.md\``; the re-anchor renders them as proper relative-path markdown links `[\`sequential-obstruction\`](../concepts/sequential-obstruction.md)`, consistent with every other reference to that page in the theme (e.g., line 18, 244). This is a bounded link-hygiene firm-up incidental to the obstruction re-anchor, not a content change.
- **"this audit" → "the cycle-006 audit" attribution sharpened (Re-anchors 6/7/8; disclosed).** Re-anchors 6 (line 210), 7 (line 231), and 8 (line 233) re-attribute "(re-)read for **this** audit" → "for **the cycle-006** audit." This is an intentional accuracy sharpening, not a pure citation-pointer swap: the §"Audit of cycle-002 identity-in-form claim" section IS the cycle-006 wave audit (confirmed by theme line 218 "the cycle-006 verdict", the §"Verified-against" provenance note at line 247 "carries the **cycle-006** evidence registry", and lines 253/257/293 all attributing the audit content to cycle-006), so "the cycle-006 audit" is factually correct where the original author's "this audit" was a now-stale local self-reference. Since the original phrasing was *not* wrong in its own authoring context, this is disclosed here as a deliberate incidental attribution-fix (repairer-added per cycle-014 critic Issue 1) rather than left silent. Bounded prose touch, no claim/structure/status change.

## Supporting evidence

- `book/src/spec/slices/cg.md` (165-line reduced stub; verified on disk) — the reduced slice. Its §"Firm entries that supersede this slice's ... content" (lines 5-14) lists `book/src/L3-L2/krylov-step-body-identity.md` (firm; cycle-009) and `book/src/L3/krylov-step.md` (firm; cycle-010) as the supersessors; the L2→L3 rotation-claim content formerly at slice lines 341-362 is absent from the stub (confirmed by grep: no "L2→L3 ... identity in form" claim survives the reduction except the L4-v0.5 self-rotation carry-through prose at lines 137/161).
- `book/src/L3-L2/krylov-step-body-identity.md:125` — firm home for the body-identity evidence (Claim 2), preserving `cg.md:341-362` with the verbatim Claim-2 quote ("*The L2→L3 rotation on the step body is therefore the **identity in form**: no unfolding, no global lift, no schema change.*").
- `book/src/L3/krylov-step.md` §Algebraic-laws (lines 108/129) + §Verified-against (line 188) — firm home for the outer-loop sequential-obstruction (Claim 1) and the body-identity evidence registry.
- `book/src/spec/slices/arnoldi_step.md` (302 lines; live) — the co-anchor `arnoldi_step.md:178-213`/`:185-188`/`:194-213` ranges remain valid; not re-anchored.
- `reports/2026-05-28T1447Z-lifter-krylov-step-theme-body-no-l3-row-drift-cycle-013/CYCLE.md` — the cycle-013 lifter that fixed lines 20/220 and established the lifted-evidence annotation convention this sweep extends, and whose `integration_notes` routed the theme-wide sweep to the OQ this dispatch addresses.

## Open questions / caveats

- **`L3/krylov-step.md` carries the same dangling `cg.md` pointers — OUT OF SCOPE for this theme dispatch, needs a sibling lifter.** While locating the firm home for the outer-loop-obstruction family, I found that the firm L3 entry `book/src/L3/krylov-step.md` itself still cites the now-dangling reduced-slice ranges at its lines 108 (`cg.md:341-349`), 129 (`cg.md:341-349`), 188 (`cg.md:341-362`), and 196 (`cg.md:103-115`, `:172-188`, `:393-425`), plus 202/204 (`cg.md:208-220`, `:430-446`). These dangle for the same cycle-009-reduction reason. They are in a different file (an L3 operator entry, not this L4>L3 theme) and re-anchoring them is a separate lifter dispatch — flagging here rather than touching out-of-scope `book/`. Recommend a follow-up OQ / cycle-015 lifter scope `l3-krylov-step-cg-md-citation-sweep`. (Note: my Re-anchor 1/4/8 point the theme's outer-loop pointers AT `L3/krylov-step.md` §Algebraic-laws as the firm home; that target's own internal `cg.md` pointers dangling does not invalidate it as the authoritative *narrative* home — the obstruction claim lives there in L3 vocabulary regardless of its own citation hygiene — but the sibling sweep should follow to close the loop fully.)
- **No abstractor reread needed.** The two firm entries (`L3-L2/krylov-step-body-identity.md`, `L3/krylov-step.md`) do not contradict any signature, LHS/RHS shape, or applicability condition the theme assumed. This was a pure vocabulary/citation re-anchor; the theme's `firm` status is correct and unchanged.
- **OQ `krylov-step-typed-wrapper-dissolution-cg-md-citation-sweep` closure.** This dispatch addresses that OQ in full for the theme file. Integrator may mark it `answered` with answer-link this CYCLE.md, contingent on the 8 re-anchors landing. The sibling `L3/krylov-step.md` sweep flagged above is the residual; recommend a NEW OQ for it rather than holding this one open.
