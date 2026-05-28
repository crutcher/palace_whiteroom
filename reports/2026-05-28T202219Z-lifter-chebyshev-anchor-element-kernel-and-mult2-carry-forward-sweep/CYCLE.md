---
agent: lifter
invoked_at: 2026-05-28T202219Z
scope: chebyshev-anchor-element-kernel-and-mult2-carry-forward-sweep — re-anchor inherited citation drift in the firm L1/L2 chebyshev operator entries
status: integrated
integrated_at: 2026-05-29T0030Z
integration_commit: 1af0c3d
integration_notes: "Applied cycle-015 (per-report position 3). Citation-only sweep — 7 verified anchor corrections across L2/chebyshev-iteration.md (5 sites) + L1/chebyshev-smoother.md (2 sites); inherited element-kernel + Mult2 drift fixed against L0 palace/linalg/chebyshev.cpp. No status/law/signature change (both entries stay firm). OQ chebyshev-anchor-element-kernel-and-mult2-carry-forward-sweep resolved. One non-blocking OLD-string transcription slip re-read+applied against true disk text; all 7 sites landed. Book build clean."
inputs:
  - book/src/L2/chebyshev-iteration.md
  - book/src/L1/chebyshev-smoother.md
  - reference/palace/palace/linalg/chebyshev.cpp (L0 verification, via palace-codemap read_range)
  - OQ chebyshev-anchor-element-kernel-and-mult2-carry-forward-sweep (cycle-014 lowering-verifier finding)
---

# CYCLE: Re-anchor chebyshev-anchor-element-kernel-and-mult2-carry-forward-sweep

## Summary
Pure citation-sweep (mechanical re-anchor) of the inherited upstream-anchor drift
the cycle-014 chebyshev lowering-verifier flagged in the two firm chebyshev
**operator** entries — `book/src/L2/chebyshev-iteration.md` and
`book/src/L1/chebyshev-smoother.md`. Three drifted anchors are corrected against
the verified L0 source `palace/linalg/chebyshev.cpp`: the element-fused kernel
`ApplyOrder0` (`:69-78` → **`:68-78`**), `ApplyOrderK` (`:114-123` →
**`:112-123`**), and the 4th-kind `ChebyshevSmoother::Mult2` body-range START
(`:191`, the opening brace → **`:190`**, the signature line). No claim, law,
signature, or structural change — only citation ranges firm up.

**Two OQ-claims refined against the actual current anchor set** (both
verification-driven, recorded here, not silent):
1. The OQ predicted the element-kernel drift at "FOUR sites (lines 35, 143, 245,
   247)" in the L2 file **and** "the same drift at TWO sites (lines 245, 247)" in
   the L1 file. Verification (`grep`) shows the L1 entry contains **no**
   element-kernel anchors at all — the kernels are L2 detail; the L1 entry names
   only the closed-form action. The OQ's "L1 lines 245, 247" was a
   mis-transcription of the L2 file's two Evidence-section kernel-cite sites
   (which are indeed at L2 lines 245, 247). L1's only drifted anchors are the two
   `Mult2` body cites.
2. The `Mult2` START correction `:191 → :190` applies **only** to the 4th-kind
   `ChebyshevSmoother::Mult2` (currently cited `:191-220`). The 1st-kind
   `ChebyshevSmoother1stKind::Mult2` is cited `:261-293`; verification shows its
   signature genuinely starts at `:261` (the first signature line; the wrap
   continues `:262`, brace at `:263`), so `:261-293` is already anchored to the
   signature line — **no drift, left unchanged.**

Net: **7 citation sites corrected** (5 in L2, 2 in L1), touching 3 distinct
drifted anchors.

## L0 verification (palace-codemap read_range, palace/linalg/chebyshev.cpp)

| construct | verified lines | drifted cite | correct cite |
|---|---|---|---|
| `ApplyOrder0` | `:68` blank → `:69` `template <bool Transpose = false>` → `:70` `inline void ApplyOrder0(...)` → `:78` body stmt (`D[i] = sr * DI[i] * R[i]`) → `:79` `}` | `:69-78` | **`:68-78`** |
| `ApplyOrderK` | `:112` blank → `:113` `template <bool Transpose = false>` → `:114` `inline void ApplyOrderK(...)` → `:123` body stmt (`D[i] = sd * D[i] + ...`) → `:124` `}` | `:114-123` | **`:112-123`** |
| `ChebyshevSmoother::Mult2` (4th) | `:189` `template <typename OperType>` → `:190` `void ChebyshevSmoother<OperType>::Mult2(...) const` → `:191` `{` → `:220` `}` | `:191-220` | **`:190-220`** |
| `ChebyshevSmoother1stKind::Mult2` (1st) | `:261` `void ChebyshevSmoother1stKind<OperType>::Mult2(const VecType &x, VecType &y,` → `:262` `VecType &r) const` → `:263` `{` → `:293` `}` | `:261-293` | `:261-293` (no drift) |

The corrected kernel ranges each shift their START back one line, from the
`inline void Apply…` declarator to the leading blank line preceding the
`template <bool Transpose = false>` parametrization that the kernel signature
depends on. Both END lines (`:78`, `:123`) are unchanged (the body statement
line; the closing brace is excluded, matching the pre-drift convention). The
4th-kind `Mult2` START shifts from the opening brace (`:191`) back to the
signature line (`:190`); its END (`:220`) is unchanged. These are exactly the
ranges the cycle-014 lowering-verifier specified as correct.

## Proposed changes

### book/src/L2/chebyshev-iteration.md

```edit:book/src/L2/chebyshev-iteration.md
[old]:
The HPC element-fused kernels in the L0 source — `ApplyOrder0` (one elementwise
pass computing `d = sr · dinv · r`) and `ApplyOrderK` (one elementwise pass
computing `d = sd · d + sr · dinv · r`, `palace/linalg/chebyshev.cpp:69-78,
:114-123`) — are **transparent fusions** at L2: they compute the same value as
[new]:
The HPC element-fused kernels in the L0 source — `ApplyOrder0` (one elementwise
pass computing `d = sr · dinv · r`) and `ApplyOrderK` (one elementwise pass
computing `d = sd · d + sr · dinv · r`, `palace/linalg/chebyshev.cpp:68-78,
:112-123`) — are **transparent fusions** at L2: they compute the same value as
```

```edit:book/src/L2/chebyshev-iteration.md
[old]:
3. **Fusion transparency of the elementwise kernels.** `ApplyOrderK(sd, sr,
   dinv, r, d)` (one elementwise pass `d ← sd·d + sr·dinv·r`,
   `palace/linalg/chebyshev.cpp:114-123`) equals the base composition `axpby(sd,
[new]:
3. **Fusion transparency of the elementwise kernels.** `ApplyOrderK(sd, sr,
   dinv, r, d)` (one elementwise pass `d ← sd·d + sr·dinv·r`,
   `palace/linalg/chebyshev.cpp:112-123`) equals the base composition `axpby(sd,
```

```edit:book/src/L2/chebyshev-iteration.md
[old]:
`firm` — the primitive composition is a direct transcription of both `Mult2`
bodies (`palace/linalg/chebyshev.cpp:191-220, :261-293`), with the
[new]:
`firm` — the primitive composition is a direct transcription of both `Mult2`
bodies (`palace/linalg/chebyshev.cpp:190-220, :261-293`), with the
```

```edit:book/src/L2/chebyshev-iteration.md
[old]:
- `palace/linalg/chebyshev.cpp:69-78` — `ApplyOrder0` (real): one elementwise
  pass `D[i] = sr · DI[i] · R[i]` (= `scal(sr, elementwise_product(dinv, r))`).
- `palace/linalg/chebyshev.cpp:114-123` — `ApplyOrderK` (real): one elementwise
[new]:
- `palace/linalg/chebyshev.cpp:68-78` — `ApplyOrder0` (real): one elementwise
  pass `D[i] = sr · DI[i] · R[i]` (= `scal(sr, elementwise_product(dinv, r))`).
- `palace/linalg/chebyshev.cpp:112-123` — `ApplyOrderK` (real): one elementwise
```

### book/src/L1/chebyshev-smoother.md

```edit:book/src/L1/chebyshev-smoother.md
[old]:
`chebyshev_smoother` lifts the `ChebyshevSmoother<OperType>::Mult2` /
`ChebyshevSmoother1stKind<OperType>::Mult2` member-method family
(`palace/linalg/chebyshev.cpp:191-220, :261-293`) — which writes into the
[new]:
`chebyshev_smoother` lifts the `ChebyshevSmoother<OperType>::Mult2` /
`ChebyshevSmoother1stKind<OperType>::Mult2` member-method family
(`palace/linalg/chebyshev.cpp:190-220, :261-293`) — which writes into the
```

```edit:book/src/L1/chebyshev-smoother.md
[old]:
- `palace/linalg/chebyshev.cpp:191-220` — 4th-kind `Mult2` body: the `pc_it`
[new]:
- `palace/linalg/chebyshev.cpp:190-220` — 4th-kind `Mult2` body: the `pc_it`
```

## Discipline notes
- **Pure rewriting pass.** Only citation ranges firm up. No claim, law, signature,
  variant-axis, dependency, or structural change. The `Mult2` body-range END
  (`:220`), the 1st-kind range (`:261-293`), and all surrounding prose are
  untouched.
- This is a **carry-forward sweep**: it re-anchors the upstream OPERATOR-entry
  anchors that the cycle-014 chebyshev lowering-verifier's audit of the
  *lowering themes* found to have inherited the drift from. The lowering themes
  themselves (the L1>L0 / L2>L1 chebyshev themes) are out of this dispatch's
  scope — they were the cycle-014 verifier's subject; this dispatch fixes the
  operator entries they inherit from, per the OQ's named-site list.
- **Two bounded prose-precision refinements recorded** (per the lifter
  L0-evidence-driven correction-boundary, friction-ledger
  `lifter-scope-content-correction-boundary`): the OQ's site count was refined
  against the actual current anchor set (L1 has no element-kernel anchors;
  1st-kind `Mult2` is not drifted). These are not edits to the artifact — they
  are scope refinements of the OQ's predicted edit set, recorded so the
  integrator applies exactly the 7 verified corrections and not the 4+2 the OQ
  literally predicted. Each is L0-citation-backed (the `grep` survey + the
  `read_range` signature-line verification above).
- No re-architecture: the drift is purely in the START line of three anchors;
  no decomposition, sub-pattern, or signature changed. No abstractor/harvester
  reread is triggered.

## Supporting evidence
- L0 source verification: `palace/linalg/chebyshev.cpp` lines 66-80, 110-125,
  188-222, 259-262, 291-294 (read via `palace-codemap read_range`), tabulated in
  the "L0 verification" section above.
- Drifted-anchor occurrence survey: `grep -n` over both files (5 sites in L2, 2
  in L1; see Summary).
- Originating finding: OQ `chebyshev-anchor-element-kernel-and-mult2-carry-forward-sweep`
  (cycle-014 chebyshev lowering-verifier).
- Affected firm operator entries: `book/src/L2/chebyshev-iteration.md` (Status
  `firm`, cycle-012 ratified), `book/src/L1/chebyshev-smoother.md` (Status
  `firm`, cycle-012 ratified).

## Open questions / caveats
- **Closes OQ `chebyshev-anchor-element-kernel-and-mult2-carry-forward-sweep`**
  once the 7 proposed corrections land. The OQ named "4+2 sites"; the verified
  actual set is "5 (L2) + 2 (L1) = 7 corrections across 3 distinct anchors" — the
  integrator should reconcile the OQ to the verified set (not the literal 4+2)
  when promoting it to resolved.
- No contradiction surfaced between the corrected ranges and the entries' claims:
  the kernel bodies, the `Mult2` body, and every algebraic law remain syntactic
  identities on the now-correctly-anchored source. No abstractor reread needed.
- One latent observation (NOT in this dispatch's scope, NOT acted on): the L2
  entry's other Evidence cites (`:49-66` ApplyOp, `:194-219` / `:264-292` sweep
  bodies, `:215-217` / `:286-288` scalar closed forms) were NOT named by the OQ
  and were NOT audited here. If the cycle-014 verifier's drift was systemic to
  the whole chebyshev anchor block (rather than just the three named anchors), a
  follow-up full-entry anchor audit may be warranted — but the OQ scoped this
  dispatch to the element-kernel + `Mult2` carry-forward only, so those cites are
  left as-is.
