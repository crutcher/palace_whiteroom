---
agent: lifter
invoked_at: 2026-06-07T192413Z
scope: L4-L3 §1.2.2-R residual style-uniformity touches — 2 deferred OWNER'S-CALL sites (BATCH-CLOSING)
status: pending
inputs:
  - book/src/semantics/index.md            # the §1.2.2-R ruling (the convert/keep discriminator)
  - book/src/L4-L3/fe-assemble-fold-dissolution.md       # site (i): :3 intro-prose operator-value mention
  - book/src/L4-L3/mk-matrix-free-operator-dissolution.md  # site (ii): :151 derived-product square-op spelling
integrated_at: 2026-06-07T193433Z
integration_commit: PLACEHOLDER_SHA
integration_notes: >-
  Applied clean by integrator-per-report (cycle-132 BATCH-CLOSING, batch-42). ONE prose-fidelity
  CONVERT landed at book/src/L4-L3/fe-assemble-fold-dissolution.md:3
  (LinearOperator[N,N] -> LinOp[(N: ...), $N], mirroring the file's own :30/:37 signature codomains);
  site (ii) mk-matrix-free-operator-dissolution.md:151 recorded NO-CHANGE (dual-spelling intentional,
  §1.2.2-R-compliant, critic-cleared owner's-call). NO status/rank/edge/maturity change. The §1.2.2-R
  operator-VALUE-codomain CONVERT axis is now FULLY EXHAUSTED end-to-end (arrow-codomain grep = 0 hits);
  the §1.2.2/closure-signature POLISH PASS is COMPLETE. cargo make book EXIT 0, ZERO build-repairs;
  all graded-stack totals HELD (rank_violations 0, reachable 163). OQs: intro-prose-monoid-carrier
  consistency RESOLVED + the CONVERT-axis-fully-exhausted exhaustion marker opened for the batch-42 meta.
---

# CYCLE: Re-anchor c132 residual §1.2.2-R style-uniformity touches

## Summary

This is the BATCH-CLOSING §1.2.2/closure-signature polish-pass cleanup of the last two benign §1.2.2-R
style-uniformity touches the c130/c131 sweeps deferred as OWNER'S-CALL. The operator-VALUE-codomain CONVERT
axis is already exhausted (arrow-codomain grep = 0 hits); these two are residual prose-fidelity / uniformity
choices, NOT codomain smells. Pure prose/signature FIDELITY — NO maturity/rank/edge change.

- **Site (i)** `fe-assemble-fold-dissolution.md:3` → **CONVERT**. The intro-prose `LinearOperator[N,N]`
  mention denotes precisely the per-term `assemble_term` contribution operator-value that the file's own two
  fenced signatures (`:30`, `:37`) already converted to `LinOp[(N: ...), $N]`. It carries explicit dim slots
  `[N,N]` (the §1.2.2-R opaque type-application smell), genuinely parallels the converted signatures, and is
  the carrier of the operator-`+` monoid being reduced — NOT a bare-word conceptual noun. Convert to mirror
  the file's own converted forms.
- **Site (ii)** `mk-matrix-free-operator-dissolution.md:151` → **NO-CHANGE** (KEEP the dual-spelling). Both
  spellings are §1.2.2-R-compliant bracketed operator-value forms (per §1.3.1's table both the square-op
  `LinOp[(N: ...), $N]` and the explicit-arrow `Op[Tensor[…] → Tensor[…]]` are compliant — neither is the
  opaque smell) and critic-cleared. The dual-spelling is intentional and semantically motivated, not drift —
  see §Discipline notes. Owner's-call NO-CHANGE.

## Proposed changes

### Site (i) — CONVERT `fe-assemble-fold-dissolution.md:3`

```edit:book/src/L4-L3/fe-assemble-fold-dissolution.md
[old]: and reduces the per-term `LinearOperator[N,N]` contributions by operator-`+` into one global operator.
[new]: and reduces the per-term `LinOp[(N: ...), $N]` contributions by operator-`+` into one global operator.
```

### Site (ii) — NO-CHANGE `mk-matrix-free-operator-dissolution.md:151`

No edit. `:151`'s derived-product L3 signature
`mk_matrix_free_operator_L3 :: (space, term, geom) -> LinOp[(N: ...), $N]` stays as the square-op spelling.
Rationale recorded in §Discipline notes (both compliant; dual-spelling intentional + critic-cleared).

## Discipline notes

**Site (i) — CONVERT (bounded prose/signature-fidelity re-anchor, §1.2.2-R).** Per the §1.2.2-R one-line
discriminator (`semantics/index.md:104`): *is this an operator-value in a calculus-level (L4/L3/L2)
signature/theme position, spelled opaquely?* → CONVERT to bracketed. The `:3` mention "reduces the per-term
`LinearOperator[N,N]` contributions by operator-`+` into one global operator" is the intro-prose statement of
the SAME per-term contribution type that the file's two fenced LHS signatures already converted:
`assemble_term :: FiniteElementSpace[N] -> WeakFormTerm -> LinOp[(N: ...), $N]` (`:37`) and the fold result
`fe_assemble :: … -> LinOp[(N: ...), $N]` (`:30`). The `:3` form is NOT a bare-word noun — it carries explicit
dim slots `[N,N]`, i.e. the §1.2.2-R "opaque type-application" smell (`LinearOperator[N,N]`: a bare type name
applied to dim slots, no in/out arrow), and it denotes precisely the rank-agnostic per-term operator-value
carrier of the operator-`+` monoid being reduced. So it genuinely parallels the converted signatures →
CONVERT, mirroring the file's own `:30`/`:37` forms. This is consistent with — not contrary to — the c131
lifter's `:3` bare-word KEEP precedent: that KEEP was for a bare-word conceptual NOUN with no dim slots; this
`:3` has dim slots driving the same codomain the file already converted, so the convert-only-if-it-parallels
test is met here where it was not there. The change is a pure prose-fidelity re-anchor (the per-term carrier
type now reads identically in the intro and in the two fenced signatures); no maturity / rank / edge change.

**Site (ii) — NO-CHANGE (KEEP dual-spelling).** The dual-spelling at this theme is intentional and
semantically motivated, not drift, and both spellings are §1.2.2-R-compliant + critic-cleared:

1. **The constructor sites are verbatim cap transcriptions and are NOT free to change.** `:104` and `:370`
   transcribe the firm L4 `mk_matrix_free_operator` cap's signature verbatim
   (`mk_matrix_free_operator :: FESpace -> WeakFormTerm -> GeomFactors -> Op[Tensor[(N: ...)] → Tensor[(N: ...)]]`),
   and `:122` quotes the cap's `Op[Tensor[(N: ...)] → Tensor[(N: ...)]]` operator type inline. These are
   fidelity-to-the-cap transcriptions of the §1.1 general operator-value `Op[τ_in → τ_out]` form; re-spelling
   them to `LinOp[(N: ...), $N]` would break verbatim fidelity to the L4 cap the theme cites (the cap spells the
   constructor codomain in the `Op[… → …]` form). They must mirror the cap, not the L3 derived-product line.
2. **`:151` is the theme's OWN L3-image derived-product signature, where the square-op `LinOp[(N: ...), $N]`
   form is the apt + more-precise spelling.** Per §1.2.2:93/§1.2.2-R, `LinOp[(N: ...), $N]` is the dedicated
   square/endomorphic operator-value spelling (one group bound, used for the range — domain ≡ range marked by
   `$N`). For "a square endomorphism over `Tensor[(N: ...)]`" it is MORE semantically precise than the
   arrow form, not less. Forcing `:151` to the arrow form would gain a single-spelling uniformity the
   cap-transcription sites cannot share anyway (they must keep the `Op[… → …]` cap form), at the cost of making
   the theme's own L3 signature less explicit about the square structure.
3. Both forms denote the same square endomorphism over the flat operator-domain shape `Tensor[(N: ...)]`; per
   §1.3.1's reconciliation table both are compliant bracketed operator-value spellings (the bracket carries the
   in/out arrow — no opaque type-application smell, no missing in/out arrow), and the critic cleared the
   dual-spelling. NO-CHANGE is the legitimate owner's-call outcome here.

No L0 prose-correction was needed; both sites are §1.2.2-R judgment calls, not drifted/backward claims.

## Supporting evidence

- `book/src/semantics/index.md:97-104` — the §1.2.2-R operator-VALUE spelling ruling: the convert/keep
  discriminator (`:101` the opaque `LinearOperator[N,N]` smell → CONVERT-to-bracketed; `:104` the one-line
  discriminator).
- `book/src/semantics/index.md:93` — §1.2.2 the square/endomorphic operator-value spelling `LinOp[(S: ...), $S]`
  (the form `:151` uses).
- `book/src/semantics/index.md:161-171` — §1.3.1 the reconciliation table: both `Op[τ_in → τ_out]` and the
  square-op `LinOp[(N: ...), $N]` are compliant bracketed operator-value spellings (site (ii) both-compliant
  basis).
- `book/src/L4-L3/fe-assemble-fold-dissolution.md:30,:37` — the file's own already-converted `LinOp[(N: ...), $N]`
  signatures that site (i)'s `:3` intro mention now mirrors.
- `book/src/L4-L3/mk-matrix-free-operator-dissolution.md:104,:122,:370` — the cap-transcription `Op[…]`
  constructor sites that the `:151` derived-product square-op spelling intentionally differs from.

## Open questions / caveats

None. Both decisions are bounded §1.2.2-R style-fidelity judgments fully supported by the on-disk semantic
surface; neither requires an abstractor reread. The §1.2.2-R operator-VALUE-codomain CONVERT axis is exhausted
after this pass (this site (i) was an intro-prose residual of the already-converted file, not a codomain in a
fenced signature). No maturity / rank / edge change. If site (i)'s integrator-applied change is the only
artifact mutation this cycle, site (ii)'s NO-CHANGE staging row should read "no artifact change (KEEP,
recorded)".
