---
agent: lifter
invoked_at: 2026-05-31T14:15:00Z
scope: L1>L0 cite-precision pass — chebyshev-smoother-mutation-rotation second dead-code transpose kernel range (:150-159 → :147-155); cycle-035 D1
status: applied
inputs:
  - book/src/L1-L0/chebyshev-smoother-mutation-rotation.md
  - reference/palace/palace/linalg/chebyshev.cpp (lines ~95-160; on-disk verification)
  - reports/2026-05-31T013000Z-integrator-finalize-cycle-34/ (cycle-034 D2 lowering-verifier audit precedent)
  - scaffolding/open-questions.md:489 (the OQ this dispatch resolves)
integrated_at: 2026-05-31T18:01:20Z
integration_commit: PLACEHOLDER_SHA
integration_notes: |
  cycle-035 D1 — applied by integrator-per-report at 2026-05-31T15:10:00Z (staging row 1); housekept by integrator-finalize at 2026-05-31T18:01:20Z. Three surgical cite-precision edits applied to book/src/L1-L0/chebyshev-smoother-mutation-rotation.md (prose line 145, verified_against: block line 350, prose line 372 — :150-159 → :147-155); theme stays firm. OQ chebyshev-smoother-mutation-rotation-applyorderk-true-citation-tighten RESOLVED on landing; sibling informational OQ chebyshev-smoother-mutation-rotation-applyorder0-true-citation-tighten-sibling filed for the :101-110 → :102-110 future-cycle hook. Citecheck 8 ok / 0 failing; YAML round-trip on edited verified_against: block PASSES (note value begins with `d`, no leading quote — clears verified-against-note-no-leading-quote-of-either-kind friction-ledger). No book rebuild here; finalize ran cargo make book exit 0 in 90.81s. Single commit covering all 3 cycle-035 reports + housekeeping.
---

# CYCLE: chebyshev-smoother-mutation-rotation second-kernel cite tightening

## Summary

Cite-precision pass on `book/src/L1-L0/chebyshev-smoother-mutation-rotation.md`:
the firm theme cites the second dead-code complex-transpose elementwise kernel
(the `else`-block body inside `ApplyOrder0<Transpose=true>`) as
`palace/linalg/chebyshev.cpp:150-159` in three places (prose at line 145, the
`verified_against:` block citation at line 350, and prose at line 372). On-disk
verification confirms the precise dead `else`-block body is `:147-155` (line
147 = `else` keyword, line 148 = opening `{`, lines 149-154 = `forall_switch`
body, line 155 = closing `}` of the `else` block). The current `:150-159`
undershoots start by 3 lines (lands inside the lambda body, missing the `else`
+ opening brace + first 2 lambda lines) and overshoots end by 4 lines
(crosses line 155's `}`-of-`else` to land on `:159`, which is `}` of `namespace`
two construct boundaries past). The theme's structure / status / claim stay
unchanged (still firm); this is a hygiene-only tightening per the cycle-034 D2
audit. Single-citation surgical edit per the lifter "bounded prose-correction"
scope (a `path:lo-hi` drift on a recorded citation, supported by the L0 source
read this dispatch + the cycle-034 audit + citecheck `--anchor` confirmation).

## Verification (on-disk)

`reference/palace/palace/linalg/chebyshev.cpp:140-160` read directly (line
numbers as shown by the Read tool against the on-disk file, NOT codemap):

    140	    mfem::forall_switch(use_dev, N,
    141	                        [=] MFEM_HOST_DEVICE(int i)
    142	                        {
    143	                          DR[i] = sd * DR[i] + sr * (DIR[i] * RR[i] - DII[i] * RI[i]);
    144	                          DI[i] = sd * DI[i] + sr * (DII[i] * RR[i] + DIR[i] * RI[i]);
    145	                        });
    146	  }
    147	  else
    148	  {
    149	    mfem::forall_switch(use_dev, N,
    150	                        [=] MFEM_HOST_DEVICE(int i)
    151	                        {
    152	                          DR[i] = sd * DR[i] + sr * (DIR[i] * RR[i] + DII[i] * RI[i]);
    153	                          DI[i] = sd * DI[i] + sr * (-DII[i] * RR[i] + DIR[i] * RI[i]);
    154	                        });
    155	  }
    156	}
    157	
    158	}  // namespace

Precise dead `else`-block body: `:147-155`. Line 156 is `}` of the enclosing
function (the `ApplyOrderK<Transpose=true>` close); line 158 is `}` of the
anonymous `namespace` block — both BEYOND the `else`-block.

citecheck confirmation:

    $ python3 tools/citecheck/citecheck.py reference/palace/palace/linalg/chebyshev.cpp:147-155 --anchor 'else'
    1 ok, 0 failing (1 citations checked).
    [ok  ] reference/palace/palace/linalg/chebyshev.cpp:147-155  (anchor lit: 'else')
           anchor at line(s) [147] within range 147-155

    $ python3 tools/citecheck/citecheck.py reference/palace/palace/linalg/chebyshev.cpp:150-159 --anchor 'else'
    0 ok, 1 failing (1 citations checked).
    [DRIFT] reference/palace/palace/linalg/chebyshev.cpp:150-159  (anchor lit: 'else')
           anchor at line 147, -3 outside range 150-159
           suggested: reference/palace/palace/linalg/chebyshev.cpp:147-156

(Citecheck's suggested `:147-156` is the smallest range containing the anchor;
the audit's `:147-155` is the tighter still-correct range — it stops AT the
`else`-block close brace rather than crossing into the enclosing function's
close.)

## Proposed changes

Three call-sites of `:150-159` to tighten to `:147-155`. The `:101-110` sibling
range (first dead-code kernel, `ApplyOrder0<Transpose=true>` `else`-block) is
out of scope for this dispatch per dispatch directive and is left UNCHANGED.

```edit:book/src/L1-L0/chebyshev-smoother-mutation-rotation.md
[old]: `chebyshev_smoother(op, …)`,
[`L1/chebyshev-smoother`](../L1/chebyshev-smoother.md) §Algebraic laws). The
complex conjugate-`dinv` transpose kernels exist
(`palace/linalg/chebyshev.cpp:101-110, :150-159`) but are dead code under the
symmetric wiring — recognition rules for *potential* transpose sites, not
observed ones (see Open questions).
[new]: `chebyshev_smoother(op, …)`,
[`L1/chebyshev-smoother`](../L1/chebyshev-smoother.md) §Algebraic laws). The
complex conjugate-`dinv` transpose kernels exist
(`palace/linalg/chebyshev.cpp:101-110, :147-155`) but are dead code under the
symmetric wiring — recognition rules for *potential* transpose sites, not
observed ones (see Open questions).
```

```edit:book/src/L1-L0/chebyshev-smoother-mutation-rotation.md
[old]:   - citation: palace/linalg/chebyshev.cpp:101-110,150-159
    verdict: supports
    audited_at: 2026-05-28T19:33:25Z
    note: dead-code complex conjugate-dinv transpose kernels (recognition rules)
[new]:   - citation: palace/linalg/chebyshev.cpp:101-110,147-155
    verdict: supports
    audited_at: 2026-05-28T19:33:25Z
    note: dead-code complex conjugate-dinv transpose kernels (recognition rules); second-kernel range tightened from :150-159 to :147-155 (cycle-035 D1)
```

```edit:book/src/L1-L0/chebyshev-smoother-mutation-rotation.md
[old]: - **Dead-code complex transpose kernels.** `palace/linalg/chebyshev.cpp:101-110,
  :150-159` define conjugate-`dinv` transpose elementwise kernels that are
  unreachable under the symmetric `MultTranspose2 → Mult2` wiring. They are
  recognition rules for *potential* non-symmetric sites, not observed ones —
  same defined-not-used status as the
  [`axpby-mutation-rotation`](./axpby-mutation-rotation.md) `ComplexVector::Subtract`
  forms. Flag for the `lowering-verifier`.
[new]: - **Dead-code complex transpose kernels.** `palace/linalg/chebyshev.cpp:101-110,
  :147-155` define conjugate-`dinv` transpose elementwise kernels that are
  unreachable under the symmetric `MultTranspose2 → Mult2` wiring. They are
  recognition rules for *potential* non-symmetric sites, not observed ones —
  same defined-not-used status as the
  [`axpby-mutation-rotation`](./axpby-mutation-rotation.md) `ComplexVector::Subtract`
  forms. Flag for the `lowering-verifier`.
```

## Discipline notes

- **Scope**: bounded prose-correction (path:lo-hi citation drift). The change
  is supported by the L0 source read this dispatch (`chebyshev.cpp:140-160`),
  the cycle-034 D2 lowering-verifier audit precedent, and citecheck `--anchor`
  confirmation. It does NOT re-route the theme decomposition, change a
  signature, or alter the firm verdict — exactly the bounded shape the lifter
  prose-correction-boundary entry licenses.
- **Out-of-scope, but observed**: the sibling `:101-110` first-kernel citation
  has the SAME structural shape (the first dead `else`-block body is `:102-110`
  by the same logic — line 102 = `else`, line 110 = closing `}` of the first
  `else`). The dispatch directive explicitly says "Do NOT change the `:101-110`
  citation (only the `:150-159` → `:147-155` one)" so it is left as-is. If a
  future cycle wishes to tighten `:101-110` → `:102-110` for the same reason,
  the source verification is in §Verification above (lines 95-110 segment).
  Flagged as an Open question below — NOT enacted here.
- **YAML `note:` value hygiene**: the rewritten `verified_against:` note does
  NOT begin with a leading `'` or `"` quote (begins with `dead-code …`); safe
  for `yaml.safe_load` round-trip.
- **OQ closure**: the motivating OQ `chebyshev-smoother-mutation-rotation-applyorderk-true-citation-tighten`
  (`scaffolding/open-questions.md:489`) is **resolved-on-landing** by this
  dispatch — the integrator-per-report should close it as part of integration.

## Supporting evidence

- L0 source: `reference/palace/palace/linalg/chebyshev.cpp:140-160` (read
  on-disk; the dead `else`-block body is line-exact `:147-155`).
- Cycle-034 D2 lowering-verifier audit: `reports/2026-05-31T013000Z-integrator-finalize-cycle-34/`
  (the audit that established the tightening verdict; this dispatch enacts it).
- citecheck `--anchor 'else'` runs (see §Verification above): `:147-155` OK,
  `:150-159` DRIFT.
- OQ ledger entry: `scaffolding/open-questions.md:489`.

## Open questions / caveats

- **Sibling `:101-110` first-kernel range has the same shape**. By the same
  on-disk verification (lines 101-110: line 101 = `}`-of-`if`-branch, line 102
  = `else`, line 103 = `{`, lines 104-109 = `forall_switch` body, line 110 =
  `}` of `else`), the tight dead `else`-block body of the first kernel is
  `:102-110`, not `:101-110` (the current `:101-110` includes the trailing `}`
  of the preceding `if`-branch, a 1-line overshoot on start). This dispatch
  leaves it untouched per directive; a future lifter pass could tighten
  `:101-110` → `:102-110` with the same justification shape. Lower fan-out than
  the `:150-159` tightening this dispatch enacts (the `:101-110` drift is only
  1 line, vs. 3+4 lines for `:150-159`).
- **`citecheck.py --scan` self-check on this CYCLE.md** is documented in
  §Verification but the report-level `--scan` invocation may flag the on-disk
  source-listing block (lines 140-160 transcribed for context) and the
  `:101-110` mention in §Open questions / Discipline notes — those are
  illustrative context, not first-class citations being landed. The three
  citations BEING LANDED are the three `:147-155` replacements in the
  proposed-changes blocks, all anchor-verified above.
