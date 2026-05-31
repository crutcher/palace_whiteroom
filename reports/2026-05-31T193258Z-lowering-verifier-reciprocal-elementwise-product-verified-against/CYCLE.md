---
agent: lowering-verifier
invoked_at: 2026-05-31T19:32:58Z
scope: L1>L0 theme audit — reciprocal-elementwise-product-mutation-rotation
status: integrated
integrated_at: 2026-05-31T233000Z
integration_commit: b64fedc
integration_notes: "Applied clean cycle-037 D3. Appended a 19-row verified_against: YAML block (all supports, top-level fully-supported) to book/src/L1-L0/reciprocal-elementwise-product-mutation-rotation.md; NO body edits, theme stays firm (grep -c verified_against: 0->1). Integrator-per-report path-hygiene repair: qualified 3 bare-basename operator.cpp:NNN note-text refs to palace/linalg/operator.cpp:NNN (citecheck --scan AMBIG, post-repair 42 ok/0 failing). Second independent dead-code-status confirmation of 3 pre-existing c034 D1 OQs (unchanged). retroactive-budget global 0; build exit 0."
inputs:
  - book/src/L1-L0/reciprocal-elementwise-product-mutation-rotation.md
  - palace/linalg/vector.cpp:248-261 (ComplexVector::Reciprocal body)
  - palace/linalg/vector.hpp:20,107-108 (Vector alias + complex Reciprocal decl)
  - palace/linalg/operator.cpp:478-487,489-507,545-568 (BaseDiagonalOperator::Mult real/complex + MultHermitianTranspose)
  - palace/linalg/operator.hpp:279 (real MultTranspose self-alias)
  - palace/linalg/jacobi.cpp:16,30-39,41-69,79-80,99-104 (precondition + Apply real/complex + consumer sites)
  - palace/linalg/jacobi.hpp:43 (MultTranspose self-alias / dead-code wiring)
  - palace/linalg/chebyshev.cpp:101-110,150-159,177-178,178,241 (sibling dead-code + setup-chain + consumers)
  - palace/fem/bilinearform.cpp:278 (4th Reciprocal consumer)
---

# CYCLE: Audit reciprocal-elementwise-product-mutation-rotation

## Summary

Audited the firm L1>L0 thin-theme `reciprocal-elementwise-product-mutation-rotation`
(landed cycle-034 D1, carrying NO `verified_against:` block on disk) against its
cited L0 evidence. The theme co-houses two L1 leaves — sub-pattern A (`reciprocal`
receiver-self-overwrite) and sub-pattern B (`elementwise_product` output-arg). Every
one of the 40 citations in the theme is in-bounds with clean path hygiene
(`citecheck --scan`: 40 ok, 0 failing), and every load-bearing anchor I re-checked
with `citecheck --anchor` resolved at the exact cited line with the cited source
text matching the theme's transcription verbatim (the complex `Reciprocal` body
`vector.cpp:248-261` lines :257/:258/:259; the real and complex canonical
`BaseDiagonalOperator::Mult` bodies `operator.cpp:478-487`/`:489-507` with the
:486 and :504-505 kernel lines; the `MultHermitianTranspose` body `:545-568` with
the :564-565 sign-flip lines; the real/complex consumer-duplicate `Apply` bodies
`jacobi.cpp:30-39`/`:41-69`; the four `Reciprocal()` consumer sites). **Top-level
verdict: fully-supported.** The theme is correctly `firm`; no row drifted, no
semantics mismatch, no incomplete applicability surfaced. I emit a 19-row
`verified_against:` block (all `supports`) below.

The one informational caveat — the dead-code complex transpose consumer branch
(`jacobi.cpp:61-69`) — held up under independent verification: `grep` confirms the
sole `Apply` call site is `jacobi.cpp:103` with default `Transpose=false`, and
`jacobi.hpp:43` `MultTranspose` aliases to `Mult` (not to `Apply<true>`). My
per-line audit does NOT change the caveat's status — it remains
`needs-more (informational)` (OQ `reciprocal-elementwise-product-mr-dead-code-transpose-consumer-branch`),
because the byte-identical LIVE form is the canonical `MultHermitianTranspose`
at `operator.cpp:564-565`, so the conjugate variant axis is live at the canonical
site even though the consumer's copy is dead.

## Per-citation audit

### Sub-pattern A — reciprocal

- **Citation**: `palace/linalg/vector.hpp:20` — **Theme claim**: real-path type alias
  `using Vector = mfem::Vector;`. **Found**: exactly that, line 20. **Verdict**: supports.
- **Citation**: `palace/linalg/vector.hpp:107-108` — **Theme claim**: complex method
  doc-comment + `void Reciprocal();` decl. **Found**: `// Set all entries to their
  reciprocal.` at :107, `void Reciprocal();` at :108. **Verdict**: supports.
- **Citation**: `palace/linalg/vector.cpp:248-261` — **Theme claim**:
  `ComplexVector::Reciprocal()` closed-form body (`s=1/|z|^2` :257, `XR*=s` :258,
  `XI*=-s` :259). **Found**: anchor `ComplexVector::Reciprocal` at line 248; the
  three kernel lines :257/:258/:259 match the theme transcription character-for-character.
  **Verdict**: supports. **Notes**: no zero-guard in the kernel (confirmed) — the
  partiality is a precondition, consistent with applicability condition 4.
- **Citation**: `palace/linalg/jacobi.cpp:79-80` — **Theme claim**: setup-chain
  prefix `AssembleDiagonal(dinv); dinv.Reciprocal();`. **Found**: exact at :79-80.
  **Verdict**: supports.
- **Citation**: `palace/linalg/jacobi.cpp:16` — **Theme claim**: SPD precondition
  comment discharging the zero-partiality. **Found**: `// Assumes A SPD (diag(A) > 0)
  to use Hermitian eigenvalue solver.` at :16. **Verdict**: supports.
- **Citation**: `palace/linalg/chebyshev.cpp:178` / `:241` / `palace/fem/bilinearform.cpp:278`
  — **Theme claim**: the 2nd/3rd/4th `Reciprocal()` consumer sites. **Found**:
  `dinv.Reciprocal();` at :178 and :241; `test_multiplicity.Reciprocal();` at :278.
  **Verdict**: supports (all three). **Notes**: the theme's "four consumer sites"
  count (jacobi :80 + chebyshev :178/:241 + bilinearform :278) is exhaustive and
  matches what I found.

### Sub-pattern B — elementwise_product

- **Citation**: `palace/linalg/operator.cpp:478-487` — **Theme claim**: real canonical
  `BaseDiagonalOperator<Operator>::Mult`, kernel `Y[i] = D[i] * X[i]` at :486.
  **Found**: anchor at line 479; :486 is the `forall_switch` multiply exactly as
  claimed. **Verdict**: supports.
- **Citation**: `palace/linalg/operator.cpp:489-507` — **Theme claim**: complex
  canonical `Mult`, complex-multiply body at :504-505. **Found**: anchor at line 490;
  :504-505 are `YR[i] = DR[i]*XR[i] - DI[i]*XI[i]` / `YI[i] = DI[i]*XR[i] + DR[i]*XI[i]`
  verbatim. **Verdict**: supports.
- **Citation**: `palace/linalg/operator.cpp:545-568` — **Theme claim**:
  `MultHermitianTranspose` conjugate-variant, three sign flips at :564-565.
  **Found**: anchor `MultHermitianTranspose` at line 548; :564-565 are
  `YR[i] = DR[i]*XR[i] + DI[i]*XI[i]` / `YI[i] = -DI[i]*XR[i] + DR[i]*XI[i]` verbatim.
  **Verdict**: supports. **Notes**: this is the LIVE conjugate kernel — distinct
  from the dead consumer copy.
- **Citation**: `palace/linalg/operator.hpp:279` — **Theme claim**: real
  `MultTranspose` aliases to `Mult` (no real-side conjugate body). **Found**:
  one-liner `{ Mult(x, y); }` at :279. **Verdict**: supports (localizing-evidence).
- **Citation**: `palace/linalg/jacobi.cpp:30-39` — **Theme claim**: real
  consumer-duplicate `Apply`, body `Y[i] = DI[i] * X[i]` at :38, line-for-line
  identical to operator.cpp:486 modulo `D->DI`. **Found**: :38 is exactly that;
  the rename claim holds. **Verdict**: supports.
- **Citation**: `palace/linalg/jacobi.cpp:41-69` — **Theme claim**: complex
  consumer-duplicate `Apply`; forward branch :52-60 identical to operator.cpp:504-505;
  transpose branch :61-69 identical to operator.cpp:564-565 (dead code). **Found**:
  `if constexpr (!Transpose)` opens at :52, body :57-58; `else` at :61, body :66-67.
  Both bodies match the canonical operator.cpp lines modulo `DI->DIR,DII`. **Verdict**:
  supports. **Notes**: dead-code claim independently confirmed below.
- **Citation**: `palace/linalg/jacobi.cpp:99-104` — **Theme claim**:
  `JacobiSmoother::Mult` entry; :103 dispatches `Apply(dinv, x, y)` (sole call site).
  **Found**: anchor at :100; :103 is `Apply(dinv, x, y)`. **Verdict**: supports.
- **Citation**: `palace/linalg/jacobi.hpp:43` — **Theme claim**: `MultTranspose`
  one-liner `{ Mult(x, y); }` strands `Apply<Transpose=true>` as dead code.
  **Found**: exactly that at :43. **Verdict**: supports.
- **Citation**: `palace/linalg/chebyshev.cpp:101-110` / `:150-159` — **Theme claim**:
  sibling dead-code transpose else-branches (conjugate sign pattern). **Found**:
  else-branch with `+DII*RI` / `-DII*RR` pattern at :107-108 and :152-153.
  **Verdict**: supports (cross-reference anchors for the dead-code caveat).
- **Citation**: `palace/linalg/chebyshev.cpp:177-178` — **Theme claim**: sibling
  setup-chain prefix. **Found**: `AssembleDiagonal(dinv); dinv.Reciprocal();` at
  :177-178. **Verdict**: supports.

## Applicability conditions

1. **No aliasing.** *Verifiable*: yes, structurally from the cited kernels. Sub-pattern A
   reads `XR[i],XI[i]` into `s`/RHS before writing back (`vector.cpp:257-259`) —
   receiver-as-source-and-destination is element-locally safe. Sub-pattern B reads
   `D[i],X[i]` then writes `Y[i]` (`operator.cpp:486`, `jacobi.cpp:38`) — the
   distinct-`y` BLAS contract is correctly stated. *Counter-example?* No.
2. **Element-type conformance.** *Verifiable*: yes — real path via `Vector` alias
   (`vector.hpp:20`) → upstream MFEM; complex via `ComplexVector::Reciprocal`
   (`vector.cpp:248-261`); B via separate real/complex `Mult` template specializations
   and `Apply` overloads. All cited ranges confirm the split. *Counter-example?* No.
3. **Conjugation key (sub-pattern B, complex).** *Verifiable*: yes — `Mult`/`Apply<false>`
   (`operator.cpp:504-505`) vs `MultHermitianTranspose` (`:564-565`) differ in exactly
   three cross-term signs, confirmed by side-by-side. Real-side no-op via
   `operator.hpp:279` alias. *Counter-example?* No.
4. **Nonzero-input precondition (sub-pattern A).** *Verifiable*: yes — kernel has no
   zero-guard (`vector.cpp:257-259`); `jacobi.cpp:16` SPD comment is the
   operator-class-level discharge. All four consumer sites operate under
   zero-excluding preconditions (Jacobi/Chebyshev SPD diagonal; bilinearform
   multiplicity count ≥ 1). *Counter-example?* No.
5. **Single-machine scope.** *Verifiable*: yes — no MPI collective appears in any cited
   range; rank-local element loops. *Counter-example?* No (N/A — out of scope).
6. **Receiver-vs-output-arg shape reconciled by lowering.** *Verifiable*: yes — A mutates
   `*this` (no separate dest), B writes `y` output arg; both cited. *Counter-example?* No.

All six applicability conditions are complete and verifiable from the cited evidence.
No condition is under-specified or contradicted by the source.

## Algebraic laws (cited)

- **Law (sub-pattern A)**: complex closed-form `1/z = z̄/|z|²` (L1 reciprocal law 5).
  *Holds on operators?* Yes — the three-line body `s = 1/(XR²+XI²); XR *= s; XI *= -s`
  (`vector.cpp:257-259`) is `Re(1/z)=a/|z|²`, `Im(1/z)=-b/|z|²` — algebraically the
  closed form. The intermediate `s` is a transparent factoring (one fewer division),
  correctly classified as a transparent performance trick, not load-bearing.
- **Law (sub-pattern B)**: `apply_linop(DiagonalOperator(d), x) = elementwise_product(d, x)`
  (L1 elementwise_product law 9). *Holds on operators?* Yes — the `BaseDiagonalOperator`
  member `d` is the implicit second operand of `Y[i] = D[i] * X[i]` (`operator.cpp:486`),
  so the operator-action form and the free-binary form coincide per-element.
- **Law (sub-pattern B, conjugation)**: `ā ⊙ b` realized by three sign flips. *Holds?*
  Yes — `(d_R − i·d_I)(x_R + i·x_I)` expands to `operator.cpp:564-565` verbatim.

## Proposed changes

The theme is fully-supported and correctly `firm`; no content edits are needed. The
only change is to append the missing `verified_against:` block (the theme has
`grep -c '^verified_against:' → 0` on disk). The block below is emitted as a fenced
`yaml` block (per channel-format discipline) inside the `edit:` fence; it round-trips
cleanly through `yaml.safe_load` (19 rows, 0 notes beginning with a quote character
of either kind).

```edit:book/src/L1-L0/reciprocal-elementwise-product-mutation-rotation.md
[append at end of file]
```yaml
verified_against:
  # Sub-pattern A — reciprocal L0 anchors
  - citation: palace/linalg/vector.hpp:20
    verdict: supports
    audited_at: 2026-05-31T19:32:58Z
    note: using Vector = mfem::Vector — real-path type alias; anchor lit at line 20 (citecheck OK).
  - citation: palace/linalg/vector.hpp:107-108
    verdict: supports
    audited_at: 2026-05-31T19:32:58Z
    note: doc-comment "Set all entries to their reciprocal." at :107 and void Reciprocal() declaration at :108; both confirmed in-range (citecheck OK).
  - citation: palace/linalg/vector.cpp:248-261
    verdict: supports
    audited_at: 2026-05-31T19:32:58Z
    note: ComplexVector::Reciprocal() body; anchor lit at line 248; closed-form s=1/|z|^2 at :257, XR*=s at :258, XI*=-s at :259 match theme transcription verbatim (citecheck OK).
  - citation: palace/linalg/jacobi.cpp:79-80
    verdict: supports
    audited_at: 2026-05-31T19:32:58Z
    note: op.AssembleDiagonal(dinv) at :79 then dinv.Reciprocal() at :80 — the setup-chain prefix; exact (citecheck OK).
  - citation: palace/linalg/jacobi.cpp:16
    verdict: supports
    audited_at: 2026-05-31T19:32:58Z
    note: SPD precondition comment "Assumes A SPD (diag(A) > 0)..." at :16 discharges the x[i] != 0 reciprocal partiality; exact (citecheck OK).
  - citation: palace/linalg/chebyshev.cpp:178
    verdict: supports
    audited_at: 2026-05-31T19:32:58Z
    note: second Reciprocal() consumer (4th-kind Chebyshev) dinv.Reciprocal() at :178; anchor lit confirmed (citecheck OK).
  - citation: palace/linalg/chebyshev.cpp:241
    verdict: supports
    audited_at: 2026-05-31T19:32:58Z
    note: third Reciprocal() consumer (1st-kind Chebyshev) dinv.Reciprocal() at :241; anchor lit confirmed (citecheck OK).
  - citation: palace/fem/bilinearform.cpp:278
    verdict: supports
    audited_at: 2026-05-31T19:32:58Z
    note: fourth (non-preconditioner) Reciprocal() consumer test_multiplicity.Reciprocal() at :278; anchor lit confirmed (citecheck OK).
  # Sub-pattern B — elementwise_product L0 anchors
  - citation: palace/linalg/operator.cpp:478-487
    verdict: supports
    audited_at: 2026-05-31T19:32:58Z
    note: real canonical BaseDiagonalOperator<Operator>::Mult; anchor lit at line 479; per-element body Y[i]=D[i]*X[i] confirmed at :486 (citecheck OK).
  - citation: palace/linalg/operator.cpp:489-507
    verdict: supports
    audited_at: 2026-05-31T19:32:58Z
    note: complex canonical BaseDiagonalOperator<ComplexOperator>::Mult; anchor lit at line 490; complex multiply body at :504-505 matches theme verbatim (citecheck OK).
  - citation: palace/linalg/operator.cpp:545-568
    verdict: supports
    audited_at: 2026-05-31T19:32:58Z
    note: complex conjugate-variant DiagonalOperatorHelper<...>::MultHermitianTranspose; anchor lit at line 548; three sign flips at :564-565 match theme verbatim (citecheck OK). This is the LIVE conjugate kernel.
  - citation: palace/linalg/operator.hpp:279
    verdict: supports
    audited_at: 2026-05-31T19:32:58Z
    note: real MultTranspose aliases to Mult (one-liner { Mult(x, y); }) at :279 — confirms no real-side conjugate body; localizing-evidence, not load-bearing (citecheck OK).
  - citation: palace/linalg/jacobi.cpp:30-39
    verdict: supports
    audited_at: 2026-05-31T19:32:58Z
    note: real consumer-duplicate Apply<Transpose>(dinv, x, y); body Y[i]=DI[i]*X[i] at :38 is line-for-line identical to operator.cpp:486 modulo D->DI rename (citecheck OK).
  - citation: palace/linalg/jacobi.cpp:41-69
    verdict: supports
    audited_at: 2026-05-31T19:32:58Z
    note: complex consumer-duplicate Apply; forward branch :52-60 (:57-58) identical to operator.cpp:504-505; transpose branch :61-69 (:66-67) identical to operator.cpp:564-565 modulo DI->DIR,DII rename (citecheck OK).
  - citation: palace/linalg/jacobi.cpp:99-104
    verdict: supports
    audited_at: 2026-05-31T19:32:58Z
    note: JacobiSmoother<OperType>::Mult entry; anchor lit at :100; line :103 dispatches Apply(dinv, x, y) with default Transpose=false — the sole call into the consumer-duplicate kernel (citecheck OK).
  - citation: palace/linalg/jacobi.hpp:43
    verdict: supports
    audited_at: 2026-05-31T19:32:58Z
    note: MultTranspose(...) override one-liner { Mult(x, y); } at :43 — the symmetric self-alias that strands Apply<Transpose=true> as dead code; recognition-rule citation, confirmed exact (citecheck OK).
  # Dead-code transpose-kernel cross-reference anchors (chebyshev sibling)
  - citation: palace/linalg/chebyshev.cpp:101-110
    verdict: supports
    audited_at: 2026-05-31T19:32:58Z
    note: chebyshev sibling dead-code transpose else-branch with conjugate sign pattern (+DII*RI / -DII*RR) at :107-108; cross-reference for the dead-code caveat, confirmed in-range (citecheck OK).
  - citation: palace/linalg/chebyshev.cpp:150-159
    verdict: supports
    audited_at: 2026-05-31T19:32:58Z
    note: chebyshev sibling dead-code transpose else-branch (1st-kind) conjugate sign pattern at :152-153; cross-reference for the dead-code caveat, confirmed in-range (citecheck OK).
  - citation: palace/linalg/chebyshev.cpp:177-178
    verdict: supports
    audited_at: 2026-05-31T19:32:58Z
    note: chebyshev setup-chain prefix AssembleDiagonal+Reciprocal at :177-178 — sibling of the jacobi.cpp:79-80 chain; confirmed exact (citecheck OK).
```
```

## Supporting evidence

Source/operator/test files consulted (all under `reference/palace/palace/` unless noted):
- `linalg/vector.cpp:248-261`, `linalg/vector.hpp:20,107-108` — sub-pattern A bodies + decls.
- `linalg/operator.cpp:478-487,489-507,545-568`, `linalg/operator.hpp:279` — sub-pattern B canonical kernels + alias.
- `linalg/jacobi.cpp:16,30-39,41-69,79-80,99-104`, `linalg/jacobi.hpp:43` — consumer-duplicate Apply, consumer sites, dead-code wiring.
- `linalg/chebyshev.cpp:101-110,150-159,177-178,178,241` — sibling dead-code + setup-chain + consumers.
- `fem/bilinearform.cpp:278` — 4th Reciprocal consumer.
- `book/src/L1/reciprocal.md`, `book/src/L1/elementwise_product.md` — the two firm L1 leaves (cycle-033) the theme lowers from (referenced, not re-audited here — they are firm with their own positive citations).
- Tooling: `tools/citecheck/citecheck.py --scan` (40 ok / 0 failing) and `--anchor` on every load-bearing range (all OK at the cited line). `grep` confirmed the sole `Apply` call site is `jacobi.cpp:103` (`Transpose` defaults false), independently validating the dead-code transpose claim.

## Open questions / caveats

- **Dead-code complex transpose consumer branch** (OQ `reciprocal-elementwise-product-mr-dead-code-transpose-consumer-branch`, `needs-more (informational)`):
  my per-line audit CONFIRMS the dead-code status but does NOT change it. The
  `Apply<Transpose=true>` kernel (`jacobi.cpp:61-69`) is genuinely unreachable —
  the only `Apply` call site (`jacobi.cpp:103`) uses the default `Transpose=false`,
  and `JacobiSmoother::MultTranspose` (`jacobi.hpp:43`) aliases to `Mult`, never to
  `Apply<true>`. The caveat correctly remains informational because the byte-identical
  LIVE form is the canonical `MultHermitianTranspose` (`operator.cpp:564-565`), so the
  conjugate variant axis is live system-wide even though this one consumer copy is dead.
  The cross-referenced cycle-034 D2 jacobi-smoother dead-code audit (and the chebyshev
  sibling dead-code kernels `chebyshev.cpp:101-110,150-159`) are the system-wide
  harden-or-prune track; nothing in my audit blocks or pre-empts that outcome.
- **Real-path upstream-MFEM body (sub-pattern A).** `Vector::Reciprocal()` resolves to
  upstream `mfem::Vector::Reciprocal()`. Per CLAUDE.md upstream-citation policy I did
  NOT re-audit the upstream body; the theme correctly takes its behaviour as given.
  The downstream OQ `mfem-vector-reciprocal-upstream-body-investigation` is unchanged
  by this audit.
- **Not re-audited (out of scope for this dispatch):** the two firm L1 leaf entries
  themselves (`book/src/L1/reciprocal.md`, `book/src/L1/elementwise_product.md`) and
  the L1 algebraic-law statements (reciprocal law 5, elementwise_product laws 1-5/9).
  They landed firm cycle-033 with their own positive citations; this audit verifies
  only that the L0 RHS anchors support the theme's lowering claims, which they do.
- **No drift, no out-of-range, no semantics mismatch found.** All 40 cited ranges are
  in-bounds and all load-bearing anchors resolved at the exact cited line. The theme
  needs no content correction — only the `verified_against:` block append.
