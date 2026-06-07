---
agent: lowering-verifier
invoked_at: 2026-06-07T120000Z
scope: kernel-api/impl correspondence + consumer-faithfulness audit — eigsolve-impl (D2, narrowed per D2 contingency)
status: pending
integrated_at: 2026-06-07T112037Z
integration_commit: 331a5ed
integration_notes: "cycle-124 (batch-40 opener) D2. Applied clean. Audited D1's wiring: fresh verified_against block on the consumer chapter (5 entries) + one entry into eigsolve-impl's existing block (->8). realizes-kernel-api edges confirmed reference-class; consumer depends-on edges faithful. Edge-integrity + consumer-faithfulness PASS. No promotions/new edges. CONFIRMS (does not itself fire) D1's RE3/RE11 disposition."
inputs:
  - book/src/L3/eigsolve-impl.md (roadmap_goal kernel-impl; realizes-kernel-api → L3/eigsolve + L4/eigsolve)
  - book/src/L3/nleps-deflated-eigensolve.md (D1's new roadmap_goal consumer; proposed-changes in reports/2026-06-07T112037Z-harvester-deflate-nleps-consumer/CYCLE.md)
  - book/src/L3/eigsolve.md (kernel-api surface, partial-obstruction opaque-library-ownership)
  - reference/palace/palace/linalg/nleps.cpp:356-359,470-474,505-537,547-576,613-619 (codemap + citecheck verified)
  - reports/2026-06-07T112037Z-cycle-planner-c124/CYCLE.md:60-63 (D2 scope) + :121 (D2 contingency)
---

# CYCLE: Audit eigsolve-impl correspondence + nleps-deflated-eigensolve consumer faithfulness

## Summary

D2 audit, taking the **D2 contingency narrowing** (cycle-planner CYCLE.md:121): D1 landed the new
`L3/nleps-deflated-eigensolve` consumer at `roadmap_goal` and **did NOT promote `eigsolve-impl`**
off `roadmap_goal`, so there was no firm impl↔api correspondence-promotion to audit. The audit
therefore narrows to (1) the `realizes-kernel-api` edge-class integrity and (2) the new consumer's
`depends-on` edge faithfulness, with (3) a to-the-extent-auditable re-confirmation of the
impl↔api eigenpair correspondence premise. **Top-level verdict: fully-supported.**

- **Edge integrity: PASS.** `eigsolve-impl`'s `realizes-kernel-api` edges to BOTH `L3/eigsolve`
  and `L4/eigsolve` sit under the `reference:` frontmatter block on disk (lines 19-23),
  `reference`-class, NOT mistyped to `depends-on`. The impl does not block on the opaque API — the
  correspondence is navigational/free, as DIRECTIVE-3 requires.
- **Consumer faithfulness: PASS (not forced).** D1's `depends-on` edges from the consumer to
  `eigsolve-impl` / `L2/deflate` / `L2/gram` are each genuine constituent-use, confirmed against the
  cited `nleps.cpp` source: the seed-from-linear-eigensolve (`:470-474`), the Gram block
  (`:524-531`), and the Schur-form deflation projection (`:532-535`) are all present and composed
  exactly as the consumer claims.
- **RE11 disposition correct.** `eigsolve-impl` reaching root via its `realizes-kernel-api`
  `reference` edge AND (now) via D1's new blocking `depends-on` consumer is the INTENDED disposition.
  The new blocking edge GROUNDS the impl off the RE11 reference-only-reachable cohort — an
  improvement, not decay. No finding.

## Per-citation audit

### (1) Edge-class integrity — `eigsolve-impl` `realizes-kernel-api` edges

- **Citation**: `book/src/L3/eigsolve-impl.md:19-23`
- **Claim under audit**: the `realizes-kernel-api` edges from `eigsolve-impl` → `L3/eigsolve` and
  → `L4/eigsolve` are `reference`-class (a mistype to `depends-on` would be a DEFECT per my
  kernel-api-integrity §Discipline bullet).
- **Found**: lines 19-23 read `reference:` then `- target: L3/eigsolve / kind: realizes-kernel-api`
  and `- target: L4/eigsolve / kind: realizes-kernel-api`. BOTH are under the `reference:` block,
  NOT the `depends-on:` block (which holds only `krylov-step`/`lanczos_step`/`ksp_solve`/
  `apply_linop`/`orthogonalize`). The inline comment on `:21` explicitly states "reference-class
  (navigational, free — does NOT constrain rank, does NOT carry liveness; the impl does not block on
  the opaque API)."
- **Verdict**: **supports** — edge integrity PASS, no mistype.
- **Notes**: This is the standing kernel-api/impl integrity gate the c124 plan (CYCLE.md:31) flags
  as APPLYING to D2. Confirmed clean on disk.

### (2a) Consumer→impl seed edge faithfulness

- **Citation**: `reference/palace/palace/linalg/nleps.cpp:470-474`
- **Theme claim**: the consumer's `depends-on (composes)` edge to `eigsolve-impl` is the genuine
  linear-eigensolve **seed** of each new NEP eigenpair's initial guess, not a forced/manufactured
  edge.
- **Found**: `:471` is `v.AXPBYPCZ(0.5, eigenvectors[i1], 0.5, eigenvectors[i2], 0.0)` — the
  initial-guess vector `v` is formed by averaging two columns of `eigenvectors[]`, which are the
  **outputs of the linear eigensolve** (the realization `eigsolve-impl` constructs). `:474` is
  `eig_opInv = eig;` (the lagged preconditioner eigenvalue). So the NEP loop genuinely consumes the
  linear-eigensolve output to seed each new pair.
- **Verdict**: **supports** — the `eigsolve-impl` `depends-on` edge is faithful constituent-use.
- **Notes**: This is also the rank-capping dep — a faithful (not forced) rank-0 blocking dep
  legitimately caps the consumer at `roadmap_goal` per §(h) well-foundedness, which is why D1's
  honest landing is correct.

### (2b) Consumer→deflate / consumer→gram edge faithfulness

- **Citation**: `reference/palace/palace/linalg/nleps.cpp:505-537` (with `:524-531`, `:532-535`)
- **Theme claim**: the consumer composes `L2/deflate` (oblique projector) over `L2/gram` (all-pairs
  Gram) inside the deflated solve; these are genuine constituents (and the edge fires RE3 by making
  the faithful `deflate → gram` constituent edge reachable through a built consumer).
- **Found**: The `deflated_solve` lambda (`:505`) computes:
  - `:524-531` — the all-pairs Gram double-loop `SS(i,j) = linalg::Dot(GetComm(), X[i], X[j])` =
    `XᴴX`. **`gram` is a genuine constituent.**
  - `:532-535` — the Schur form `S = eig_opInv * I − H` (`:532`), `SS = −S.fullPivLu().solve(SS)`
    (i.e. `−S⁻¹(XᴴX)`, `:533`), `x2 = SS⁻¹·x2` (`:534`), and the back-projection
    `XSx2 = MatVecMult(X, S⁻¹·x2)` then `AXPY(-1, XSx2, x1)` (`:535-536`). **`deflate` (the
    Schur-modified NLEPS oblique projection) is a genuine constituent.**
  - `:515-518` — the `if (k == 0) return;` no-deflation early-out, matching the consumer's law-3
    "`k = 0` is the un-deflated bare-solve" claim.
- **Verdict**: **supports** — `deflate` and `gram` `depends-on` edges are faithful, not forced. RE3
  premise (the faithful `deflate → gram` edge surfaced on a real consumer) holds.
- **Notes**: The block-system header comment (`:508-513`) names the exact `SS = (B − A T⁻¹ U) =
  −X*X S⁻¹` Schur complement the `deflate` chapter describes — verbatim correspondence to the L2
  vocabulary.

### (2c) Deflation-scheme provenance

- **Citation**: `reference/palace/palace/linalg/nleps.cpp:356-359`
- **Theme claim**: the deflation scheme is SLEPc-NEP's with minimality index 1 (Effenberger 2013),
  solving an extended problem of size `n + k`.
- **Found**: `:356` "Using the deflation scheme used by SLEPc's NEP solver with minimality index
  set to 1."; `:357-358` Effenberger 2013 SIAM J. Matrix Anal. Appl. citation; `:359` "The
  deflation scheme solves an extended problem of size n + k, where n is the original problem size
  and k is the number of converged eigenpairs." Exact.
- **Verdict**: **supports**.
- **Notes**: anchors land `[ok]` (citecheck `:356-359` anchor `deflation` at lines [356, 359]).

### (2d) Basis extension / locked-vector invariance

- **Citation**: `reference/palace/palace/linalg/nleps.cpp:613-619` (with `:610-612`)
- **Theme claim**: the variadic-in-`k` deflation growth + append-only locked-vector invariance
  (consumer laws 2, 3).
- **Found**: `:610-611` normalize `scale = Norml2(v); v *= 1/scale`; `:612` `eigs.resize(k+1)`;
  `:613` `eigs[k] = eig`; `:614` `X.resize(k+1)`; `:615` `X[k] = v`; `:616`
  `H.conservativeResizeLike(...Zero(k+1,k+1))`; `:617` `H.col(k).head(k) = v2/scale`; `:618`
  `H(k,k) = eig`; `:619` `k++`. The growth is append-only (`conservativeResize`/`resize` preserve
  existing columns; only the new `k`-th column/entry is written) — locked-vector invariance holds.
- **Verdict**: **supports** — laws 2 (locked-vector invariance) and 3 (variadic-in-`k`) faithful.
- **Notes**: anchor `X.resize` lands `[ok]` at `:614` within `:613-619`. Minor: the consumer's
  Record-definition table cites `eigs[k]=eig` at `:612-613` and `X.resize` at `:614`; on disk
  `eigs.resize` is `:612`, `eigs[k]=eig` is `:613`, `X.resize` is `:614` — all in-range and the
  precise sub-cites are exact. No drift to carry.

## Applicability conditions

- **Condition**: the impl realizes the SAME eigenpairs the opaque SLEPc/ARPACK api defers to
  (impl↔api eigenpair correspondence premise).
- **Verifiable**: only to the extent the roadmap_goal impl's stated content allows. The impl is
  `roadmap_goal` (speculative reconstruction, no positive Palace claim); the prior c122 audit
  (`eigsolve-impl.md:161-191`, audited 2026-06-07T093000Z) already recorded the STRUCTURAL
  correspondence as faithful (thick-restart Krylov-Schur driver + inner basis-extension loop +
  Rayleigh-Ritz extraction realizes the kernel-api's opaque eigen-iteration; per-step body is the
  same `apply_linop ▷ ksp_solve ▷ scale_untransform`; obstruction PRESERVED), with empirical-match
  DEFERRED to firming. The kernel-api `L3/eigsolve` is confirmed on disk as `partial-obstruction` /
  opaque-library-ownership / role `kernel-api` (its `apply_shift_invert` body is identity-in-form to
  the impl's inner-step body, per `eigsolve.md:104`, `:126`).
- **Found counter-example?**: no. The consumer wiring did not change the impl or its correspondence;
  the premise stands exactly as the c122 audit left it.

## Algebraic laws (consumer composition-level laws spot-checked)

- **Law**: deflation complementarity (the deflated solve operates on the complement of `span(X)`).
  **Holds?**: yes — the Schur-modified projection at `:532-536` removes the `span(X)` component
  (the `−X S x2` back-subtraction), confirmed at the source.
- **Law**: `k = 0` reduces to the bare solve. **Holds?**: yes — the `if (k == 0) return;` early-out
  at `:515-518` leaves `x1 = opInv->Mult(b1)` un-deflated.
- **Law**: locked-vector invariance (append-only growth). **Holds?**: yes — `:613-619` only appends
  the `k`-th column; `conservativeResize` preserves prior entries.

## Proposed changes

Two `verified_against:` additions. Both YAML blocks below `python3 -c "import yaml; yaml.safe_load(...)"`-clean.

### (A) New block on D1's consumer chapter

D1's new chapter `book/src/L3/nleps-deflated-eigensolve.md` has no `verified_against:` block yet,
so this is a fresh fenced block appended at end of file (the consumer chapter D1 authors via its
`new:` block — the integrator appends this AFTER applying D1's chapter):

```edit:book/src/L3/nleps-deflated-eigensolve.md
[append at end of file]
```yaml
verified_against:
  - citation: reference/palace/palace/linalg/nleps.cpp:505-537
    verdict: supports
    audited_at: 2026-06-07T120000Z
    note: deflated_solve lambda (:505) genuinely composes deflate + gram — :524-531 is the all-pairs Gram SS(i,j)=Dot(X[i],X[j]) (gram constituent, faithful); :532-535 is the Schur form S=eig*I-H, SS=-S^-1(X^*X), back-projection X*(S^-1 .) (deflate constituent, faithful); :515-518 k==0 no-deflation branch matches the k=0-reduces-to-bare-solve law. depends-on edges to deflate/gram are NOT forced.
  - citation: reference/palace/palace/linalg/nleps.cpp:356-359
    verdict: supports
    audited_at: 2026-06-07T120000Z
    note: deflation-scheme comment — SLEPc NEP minimality-index-1 (:356), Effenberger 2013 (:357-358), extended problem of size n+k (:359); exact, anchors land [ok].
  - citation: reference/palace/palace/linalg/nleps.cpp:470-474
    verdict: supports
    audited_at: 2026-06-07T120000Z
    note: seed edge faithful — :471 v.AXPBYPCZ averages eigenvectors[i1],eigenvectors[i2] (the linear-eigensolve OUTPUTS), eig_opInv=eig at :474 (lagged precond eigenvalue). The NEP loop genuinely seeds each new pair from the linear eigensolve, so eigsolve-impl is a genuine depends-on constituent, NOT a forced/manufactured edge.
  - citation: reference/palace/palace/linalg/nleps.cpp:613-619
    verdict: supports
    audited_at: 2026-06-07T120000Z
    note: basis extension — eigs.resize(k+1)/eigs[k]=eig (:612-613), X.resize(k+1)/X[k]=v (:614-615), H.col(k).head(k)=v2/scale and H(k,k)=eig (:616-618), k++ (:619); the variadic-in-k growth + append-only locked-vector invariance (laws 2,3 faithful). anchor X.resize [ok] at :614.
  - citation: book/src/L3/eigsolve-impl.md
    verdict: realizes-kernel-api-faithful
    audited_at: 2026-06-07T120000Z
    note: edge integrity re-confirmed on disk — eigsolve-impl realizes-kernel-api edges to L3/eigsolve (lines 20-21) AND L4/eigsolve (lines 22-23) BOTH sit under the reference block, reference-class, NOT mistyped to depends-on. PASS. D1 did NOT promote eigsolve-impl (stays roadmap_goal); the consumer's new blocking depends-on edge GROUNDS the impl off RE11 (the intended RE11-discharge disposition, not decay).
```
```

### (B) One entry appended INTO the existing `eigsolve-impl.md` `verified_against:` block

`book/src/L3/eigsolve-impl.md` ALREADY carries a `verified_against:` block (lines 161-191, the c122
structural-correspondence audit). Do NOT add a second fenced block — INSERT this single list entry
INTO that block, immediately BEFORE its closing ` ``` ` fence (i.e. after the last existing
`arpack.cpp:369` entry's `note:` line at `:190`, before the closing fence at `:191`):

```edit:book/src/L3/eigsolve-impl.md
[insert as a new list item at the END of the existing `verified_against:` block — after the
arpack.cpp:369 entry (line 190), before the closing ``` fence (line 191)]
  - citation: book/src/L3/nleps-deflated-eigensolve.md
    verdict: realizes-kernel-api-faithful
    audited_at: 2026-06-07T120000Z
    note: c124-D2 follow-up — the new nleps-deflated-eigensolve consumer (c124-D1) wires the FIRST blocking depends-on edge to this impl (the linear-eigensolve seed, nleps.cpp:470-474). The seed edge is faithful (the NEP loop genuinely averages eigenvectors[] linear-eigensolve outputs at :471). This grounds eigsolve-impl off the RE11 reference-only-reachable cohort — the intended RE11-discharge disposition, NOT decay. The realizes-kernel-api edges to L3/eigsolve + L4/eigsolve stay reference-class (re-confirmed on disk); no mistype to depends-on. The impl stays roadmap_goal (D1 did not promote); the prior c122 structural correspondence audit (above) is unaffected.
```

No contradictions found — no theme-content edits proposed. No status flip (D1 left `eigsolve-impl`
at `roadmap_goal`; the D2 contingency holds and the impl correctly stays `roadmap_goal`).

## Supporting evidence

- `reference/palace/palace/linalg/nleps.cpp:356-359` (deflation scheme), `:470-474` (seed),
  `:505-537` (`deflated_solve` lambda incl. `:524-531` Gram, `:532-536` Schur projection),
  `:613-619` (basis extension) — all `Read` on-disk + `tools/citecheck/citecheck.py --anchor`
  verified this dispatch (`deflated_solve` `[ok]` :505; `compute_residual` `[ok]` :550;
  `X.resize` `[ok]` :614; `deflation` `[ok]` :356,:359).
- `book/src/L3/eigsolve-impl.md` (frontmatter `:19-23` edge block; existing `verified_against:`
  `:161-191`) — edge-class integrity + prior c122 structural audit.
- `book/src/L3/eigsolve.md` (`:4` `firmness: partial-obstruction`; `:104`/`:126` body
  identity-in-form to the impl's inner step) — kernel-api surface, opaque-library-ownership.
- `book/src/L3/nleps-deflated-eigensolve.md` (D1's proposed new chapter) —
  `reports/2026-06-07T112037Z-harvester-deflate-nleps-consumer/CYCLE.md:46-500`.
- `scaffolding/graded-stack-baseline-exceptions.md` RE3 (`:199`), RE11 (`:209`) — the discharge /
  grounding targets the D1 wiring fires (confirmed via D1's report; not re-modified by D2).

## Open questions / caveats

- **Empirical-match remains deferred (not a D2 finding).** Confirming the impl computes the same
  eigenpairs as the api modulo tolerance + the four non-determinism sources requires the impl to be
  firm (and ideally a test); it is `roadmap_goal`. The structural correspondence is faithful (c122
  audit + this re-confirmation). When `eigsolve-impl` later promotes (its `lanczos_step` constituent
  firms against positive structure + a blocking consumer wires in — both now partially satisfied:
  D1's consumer IS a blocking `depends-on`), a future lowering-verifier pass should upgrade the
  correspondence verdict from STRUCTURAL to empirical-match.
- **`lanczos_step` grounding is transitive, not a direct D1 edge.** D1's consumer references
  `lanczos_step` as `reference` (reached via `eigsolve-impl`'s Hermitian arm), so `lanczos_step`'s
  RE11 grounding flows over the chain `consumer →(depends-on) eigsolve-impl →(folds/depends-on)
  lanczos_step`. I confirmed `eigsolve-impl`'s `lanczos_step` edge is `depends-on`-class (`:11-12`,
  `kind: folds` under the `depends-on:` block), so the transitive chain is sound. Whether the
  reachability GC linter actually walks this chain to mark `lanczos_step` live is a linter-execution
  question for the integrator/meta-phase to confirm at GC time — outside D2's audit authority (I
  confirm the edge TYPES support it; I do not run the GC).
- **`deflate`/`gram` carry no frontmatter `edges:` block** (D1 §Open-questions). The RE3 "faithful
  `deflate → gram` edge" is documented in the L2 index/prose, and D1's consumer surfaces it by
  composing BOTH directly. I confirmed the SOURCE composition is genuine (`:524-531` Gram inside the
  `deflate` Schur solve), so the RE3 premise holds at the source level regardless of whether
  `deflate.md` later gets a typed frontmatter edge. Routing the typed-edge addition on `deflate.md`
  itself is a separate (out-of-D2-scope) `deflate`-chapter dispatch.
