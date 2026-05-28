---
agent: abstractor
invoked_at: 2026-05-28T143232Z
scope: L1>L0 eigsolve-mutation-rotation — GetConverged forwarder fix + 2 citation-drift refinements + gated partly-constructive→firm promotion of Sub-pattern B
status: integrated
integrated_at: 2026-05-28T200000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-013 finalize. Applied as-repaired (staging row 1). FIRST live partly-constructive→firm promotion — Sub-pattern B PROMOTED, theme now firm (structural). Option-b ## Status gate route was a deliberate FLAGGED decision; ratification OQ partly-constructive-to-firm-promotion-route-ratification routed to cycle-015 meta-phase. needs-revision META was a methodology-judgment item, NOT reject."
inputs:
  - book/src/L1-L0/eigsolve-mutation-rotation.md (firm; partly-constructive on Sub-pattern B)
  - embedded cycle-012 lowering-verifier audit block (lines 751-902), audit_verdict confirms-with-refinement
  - reports/2026-05-28T034311Z-lowering-verifier-eigsolve-mutation-rotation/ (the unblocking audit)
verdict: PROMOTED
---

# CYCLE: L1>L0 eigsolve-mutation-rotation — GetConverged forwarder fix + citation refinements + gated promotion

## Verdict (one line)

**PROMOTED** — the three audit-identified firming edits are applied in THIS pass (snippet fix is not deferred), so the cycle-012 audit's gate is satisfied and the Status-gate option (b) is met; the transient `partly-constructive` status is dropped while the permanent forward-looking-reconstruction content note stays in prose.

## Summary

`book/src/L1-L0/eigsolve-mutation-rotation.md` is a firm L1>L0 mutation-rotation theme carrying a `partly-constructive` caveat on Sub-pattern B's `LinearSolveFailed` materialisation. The cycle-012 `lowering-verifier` audit (embedded at lines 751-902, `audit_verdict: confirms-with-refinement`) confirmed the structural decomposition (all ten `opInv->Mult` callsites exhaustive; negative anchor `ksp.cpp:297-310` confirms `void` return) and identified exactly three firming edits, then **UNBLOCKED but did not ENACT** the promotion — gating it on a follow-up dispatch (this one) applying the edits first. This dispatch applies all three edits as proposed-changes blocks and drops the transient `partly-constructive` status gate.

The three edits, each verified against source via `mcp__palace-codemap__read_range` this cycle:

1. **Edit 2 — GetConverged forwarder snippet correction** (the gate's named blocker). The Sub-pattern B materialisation snippet (lines 269-280) shows `opInv->GetConverged()` as if callable on `opInv`'s type. It is NOT: `opInv` is a `BaseKspSolver<ComplexOperator>`, whose `ksp` member (the `IterativeSolver` carrying `GetConverged()`) is `protected` (`ksp.hpp:41`). `GetConverged()` is defined on `IterativeSolver` at `iterative.hpp:98` and is reachable only via that protected member. The materialisation therefore requires **either** a one-line public forwarder on `BaseKspSolver` mirroring the existing `GetRelTol` accessor (`ksp.hpp:64`: `double GetRelTol() const { return ksp->GetRelTol(); }`) **or** a `Mult` status-return. The corrected snippet shows the forwarder-based form and notes the alternative.

2. **Citation-drift refinement A — ARPACK SetWhichEigenpairs attribution.** Lines 236-239 (`SetWhichEigenpairs` body) is a trivial field-set (`which_type = type;`). The actual per-`WhichType` switch (with the `MFEM_ABORT` for TARGET_REAL/TARGET_IMAGINARY) lives in `SolveInternal` — the `switch (which_type)` at `arpack.cpp:279-305`, abort at `301-304`. Corrected the attribution in Sub-pattern A's bullet and citation list.

3. **Citation-drift refinement B — ARPACK ncv-clamp.** Applicability-condition 4 cites the clamp at `arpack.cpp:521-525`; the real clamp (`if (ncv > N) { ncv = ...; }`) is at `518-521`, with `N = linalg::GlobalSize(...)` fetched at `517` and the `arpack_it` default at `522-525`. Corrected.

After the edits, the theme-level status becomes `firm (structural)`; the content note that `LinearSolveFailed` is a forward-looking reconstruction built from negative anchors (since Palace's `void`-returning `Mult` does not positively produce it) **stays in the prose** as a permanent property of the rewrite.

## Source verification (this cycle, via mcp__palace-codemap__read_range)

- `palace/linalg/ksp.hpp:28-72` — `BaseKspSolver<OperType>` class. `ksp` member is `protected` (`ksp.hpp:41`: `std::unique_ptr<IterativeSolver<OperType>> ksp;`). Public surface (`ksp.hpp:50-71`) has `NumTotalMult`, `NumTotalMultIterations`, `GetRelTol`/`GetAbsTol`/`SetRelTol`/`SetAbsTol` (the forwarder family — `GetRelTol` at line 64: `double GetRelTol() const { return ksp->GetRelTol(); }`), `SetOperators`, `Mult`. **No `GetConverged` on the public surface.** Confirms audit `partially-supports` on `ksp.hpp:30-72`.
- `palace/linalg/iterative.hpp:98` — `bool GetConverged() const { return converged && (rel_tol > 0.0 || abs_tol > 0.0); }` on `IterativeSolver`. Reachable only via the protected `ksp` member. Confirms audit `supports` on `iterative.hpp:98`.
- `palace/linalg/arpack.cpp:236-239` — `SetWhichEigenpairs` body: `{ which_type = type; }` (trivial field-set). Confirms audit `partially-supports` on `arpack.cpp:236-308`.
- `palace/linalg/arpack.cpp:279-305` — `switch (which_type)` inside `SolveInternal`; `MFEM_ABORT` (TARGET_REAL/TARGET_IMAGINARY) at `301-304`. The actual per-`WhichType` switch.
- `palace/linalg/arpack.cpp:517` — `HYPRE_BigInt N = linalg::GlobalSize(comm, z1);`.
- `palace/linalg/arpack.cpp:518-521` — `if (ncv > N) { ncv = mfem::internal::to_int(N); }` (the ncv-clamp; assignment body at 520).
- `palace/linalg/arpack.cpp:522-525` — `if (arpack_it <= 0) { arpack_it = std::max(300, ...); }` (the `arpack_it` default). Confirms audit `supports` on `arpack.cpp:518-520`.

## Promotion judgment (the first live test of the mechanism)

**Decision: PROMOTED.** Reasoning, walked against the CLAUDE.md `partly-constructive` invariant and the theme's own `## Status` gate:

The theme's `## Status` gate (lines 895-902) offers promotion via either (a) an upstream Palace refactor capturing `ksp->GetConverged()` at the ten callsites, OR (b) "a `lowering-verifier` audit that confirms the partly-constructive shape is acceptable as a methodology-level pattern (per cycle-010 lifter Open Questions §3, which forwards the pattern to cycle-012 meta-phase for codification)."

Option (b) is now met on both clauses:
- The cycle-012 meta-phase **codified** `partly-constructive` as first-class status (CLAUDE.md §Methodology invariants "Theme/operator status `partly-constructive` is first-class", precedent named as exactly this theme's Sub-pattern B).
- The cycle-012 `lowering-verifier` audit (embedded, `audit_verdict: confirms-with-refinement`) **confirmed the structure** (ten callsites exhaustive via fresh `search_text`; negative anchor confirms `void` return) and **identified the exact firming edits**. Per the CLAUDE.md invariant: "The lowering-verifier may UNBLOCK such a promotion (confirm the structure + identify the exact firming edits) without ENACTING it — the follow-up dispatch applies the edits then drops the caveat." This dispatch is that follow-up.

**The apparent conflict** — the invariant's "Do NOT mark such an entry firm (the constructive sub-part isn't)" — resolves cleanly. The `partly-constructive` status exists *because* (i) a constructive sub-part has only negative-anchor support AND (ii) an open promotion condition remains. Condition (ii) is now closed: the promotion condition (a lowering-verifier audit accepting the shape as a methodology pattern) is MET. The status is described in the invariant as "a transient gate, not a permanent escape hatch — the promotion condition should eventually close." It has closed. What I am removing is the transient status gate, NOT the honest description of the reconstruction: the prose note that `LinearSolveFailed` is forward-looking, built from negative anchors because Palace's `void`-returning `Mult` does not positively produce it, **stays** (it is a permanent property of the rewrite, not a status gate). The negative anchors remain evidence FOR the faithful reconstruction; they never become a positive claim.

The cycle-012 audit's explicit instruction — "do not drop the partly-constructive caveat in the same pass that *defers* the snippet fix" — is satisfied: this pass APPLIES the snippet fix (Edit 2), it does not defer it.

So the "Do NOT mark firm" clause and the Status-gate option (b) do NOT conflict under the natural reading: "firm" here means "no open promotion condition + structural decomposition confirmed," which is now the case. A forced promotion was not necessary; the licensed reading is clean. Verdict stands: **PROMOTED**.

## Proposed changes

> NOTE TO integrator-per-report: these are old→new exact-string replacements against
> `book/src/L1-L0/eigsolve-mutation-rotation.md` at its current (pre-cycle-013) content.
> Apply all five blocks. No `book/`/scaffolding mutation was performed by this dispatch.

### Change 1 — Edit 2: GetConverged forwarder snippet correction (Sub-pattern B materialisation snippet, lines 262-291)

```edit:book/src/L1-L0/eigsolve-mutation-rotation.md
OLD:
The materialisation that the L1>L0 lowering would specify (when Palace
ships the refactor) consists of three changes per callsite:

```text
// Before (current Palace; status silently dropped):
opInv->Mult(b, x);              // void return; warning logged only

// After (L1-constructive materialisation; not yet in Palace source):
opInv->Mult(b, x);
if (!opInv->GetConverged()) {
  inner_failed = true;          // capture per-step inner failure
  break;                        // bubble out of the eigensolver outer loop
}
// Plus, at the eigensolver outer loop terminator:
//   if (inner_failed) return LinearSolveFailed;
//   else if (num_conv == nev) return Converged;
//   else if (num_conv > 0)   return PartialConverged;
//   else                     return MaxIterReached;
```

The proposed materialisation is **partly-constructive** in the
CLAUDE.md "Unimplemented Palace stub policy" sense: the L1 form names a
status case the L0 surface does not produce, but the materialisation
shape is well-defined (the `GetConverged()` accessor exists on
`IterativeSolver` and is already used inside `BaseKspSolver::Mult` to
guard the warning emission — so the upstream behaviour change is
mechanical and small). The L1>L0 theme records this as a **rewriting
requires upstream behaviour change** caveat (per cycle-010 lifter Open
Questions §3); the rewrite shape is recorded forward-looking, with the
current L0 surface noted as silent-on-this-case.
NEW:
The materialisation that the L1>L0 lowering would specify (when Palace
ships the refactor) consists of two upstream changes: a one-line
accessor on `BaseKspSolver` plus a status-capture at each callsite.

**Accessor prerequisite (the snippet's load-bearing correction).**
`GetConverged()` is **not** callable on `opInv`'s type. `opInv` is a
`BaseKspSolver<ComplexOperator>` whose public surface
(`palace/linalg/ksp.hpp:50-71`) exposes only `NumTotalMult`,
`NumTotalMultIterations`, the `GetRelTol` / `GetAbsTol` / `SetRelTol` /
`SetAbsTol` tolerance forwarders, `SetOperators`, and `Mult`. The
convergence flag lives on `IterativeSolver::GetConverged`
(`palace/linalg/iterative.hpp:98`), reachable only through the
**protected** `ksp` member (`palace/linalg/ksp.hpp:41`). So the
materialisation first needs **either** a one-line public forwarder on
`BaseKspSolver`, mirroring the existing `GetRelTol` accessor
(`palace/linalg/ksp.hpp:64` — `double GetRelTol() const { return
ksp->GetRelTol(); }`), **or** a `Mult` status-return:

```text
// Prerequisite (option 1): a one-line public forwarder on BaseKspSolver,
//   added next to the existing GetRelTol forwarder (ksp.hpp:62):
bool GetConverged() const { return ksp->GetConverged(); }

// Prerequisite (option 2, alternative): give Mult a status return
//   (changes the void signature at ksp.cpp:297 — larger surface change).
bool Mult(const VecType &b, VecType &x) const;   // returns ksp->GetConverged()
```

```text
// Before (current Palace; status silently dropped):
opInv->Mult(b, x);              // void return; warning logged only

// After (L1-constructive materialisation; not yet in Palace source).
//   Assumes the option-1 forwarder above is present:
opInv->Mult(b, x);
if (!opInv->GetConverged()) {   // <- the new public forwarder
  inner_failed = true;          // capture per-step inner failure
  break;                        // bubble out of the eigensolver outer loop
}
// Plus, at the eigensolver outer loop terminator:
//   if (inner_failed) return LinearSolveFailed;
//   else if (num_conv == nev) return Converged;
//   else if (num_conv > 0)   return PartialConverged;
//   else                     return MaxIterReached;
```

The materialisation is a **forward-looking reconstruction**: the L1 form
names a status case the current L0 surface does not produce. The shape
is nonetheless well-defined and the upstream behaviour change is
mechanical and small — `IterativeSolver::GetConverged`
(`palace/linalg/iterative.hpp:98`) already exists and is already used
inside `BaseKspSolver::Mult` to guard the warning emission
(`palace/linalg/ksp.cpp:301-307`); the only missing piece on the public
surface is the one-line forwarder (or the `Mult` status-return). The
L1>L0 theme records this as a **rewriting requires upstream behaviour
change** note (per cycle-010 lifter Open Questions §3); the rewrite
shape is recorded forward-looking, with the current L0 surface noted as
silent-on-this-case. This reconstruction is grounded in the
negative anchor `palace/linalg/ksp.cpp:297-310` (the `void` return) —
the negative anchor is evidence FOR the faithful reconstruction, not a
positive claim that Palace produces the status today.
```

### Change 2 — Sub-pattern A spectrum-target bullet: SetWhichEigenpairs switch attribution (lines 137-151)

```edit:book/src/L1-L0/eigsolve-mutation-rotation.md
OLD:
- **Spectrum target (Stage A3)** — the `WhichType` nine-way enum maps
  per-backend to backend-specific tokens (ARPACK's
  `::arpack::which::largest_real`, SLEPc's `EPS_LARGEST_REAL`, etc.).
  At L1 the spectrum target is a construction-bound parameter on `E`;
  the L1>L0 rewrite is the `SetWhichEigenpairs` setter call with the
  per-backend mapping (`palace/linalg/arpack.cpp:236-308` for the
  ARPACK mapping including the `MFEM_ABORT` for `TARGET_REAL` /
  `TARGET_IMAGINARY`; `palace/linalg/slepc.cpp:565-600` for the SLEPc
  EPS mapping). **Recognition note**: the `(ARPACK, TARGET_REAL)` and
  `(ARPACK, TARGET_IMAGINARY)` pairs are *unimplemented stubs* per the
  ARPACK `MFEM_ABORT` at `palace/linalg/arpack.cpp:300-304`; per
  CLAUDE.md "Unimplemented Palace stub policy" the L1 form treats
  these as constructor-time validity constraints — a `K`-construction
  attempting `ARPACK × TARGET_REAL` is ill-formed; the L1>L0 rewrite
  does **not** materialise this case.
NEW:
- **Spectrum target (Stage A3)** — the `WhichType` nine-way enum maps
  per-backend to backend-specific tokens (ARPACK's
  `::arpack::which::largest_real`, SLEPc's `EPS_LARGEST_REAL`, etc.).
  At L1 the spectrum target is a construction-bound parameter on `E`;
  the L1>L0 rewrite is the `SetWhichEigenpairs` setter call with the
  per-backend mapping. For ARPACK, `SetWhichEigenpairs`
  (`palace/linalg/arpack.cpp:236-239`) is a **trivial field-set**
  (`which_type = type;`); the actual per-`WhichType` token mapping —
  the `switch (which_type)` including the `MFEM_ABORT` for `TARGET_REAL`
  / `TARGET_IMAGINARY` — lives in `SolveInternal` at
  `palace/linalg/arpack.cpp:279-305`. For SLEPc the per-`WhichType`
  switch is in `SetWhichEigenpairs` itself
  (`palace/linalg/slepc.cpp:565-600`), an asymmetry vs ARPACK.
  **Recognition note**: the `(ARPACK, TARGET_REAL)` and
  `(ARPACK, TARGET_IMAGINARY)` pairs are *unimplemented stubs* per the
  ARPACK `MFEM_ABORT` at `palace/linalg/arpack.cpp:301-304`; per
  CLAUDE.md "Unimplemented Palace stub policy" the L1 form treats
  these as constructor-time validity constraints — a `K`-construction
  attempting `ARPACK × TARGET_REAL` is ill-formed; the L1>L0 rewrite
  does **not** materialise this case.
```

### Change 3 — Sub-pattern A citation list: SetWhichEigenpairs body citation (lines 183-185)

```edit:book/src/L1-L0/eigsolve-mutation-rotation.md
OLD:
- `palace/linalg/arpack.cpp:236-308` — `ArpackEigenvalueSolver::SetWhichEigenpairs`
  body (per-`WhichType` switch with `MFEM_ABORT` for unimplemented
  TARGET_REAL / TARGET_IMAGINARY).
NEW:
- `palace/linalg/arpack.cpp:236-239` — `ArpackEigenvalueSolver::SetWhichEigenpairs`
  body (trivial field-set `which_type = type;`).
- `palace/linalg/arpack.cpp:279-305` — `ArpackEigenvalueSolver::SolveInternal`
  per-`WhichType` `switch` (the actual ARPACK-token mapping, with
  `MFEM_ABORT` for unimplemented TARGET_REAL / TARGET_IMAGINARY at
  `301-304`).
```

### Change 4 — Applicability-condition 4: ncv-clamp citation (lines 549-552)

```edit:book/src/L1-L0/eigsolve-mutation-rotation.md
OLD:
4. **`E.K_max ≤ N`.** The requested mode count cannot exceed the
   operator dimension; `palace/linalg/arpack.cpp:521-525` clamps
   `ncv` (ARPACK's basis-size parameter) against the global dimension
   `N`. At L1 this is a precondition on `E`'s opaque type.
NEW:
4. **`E.K_max ≤ N`.** The requested mode count cannot exceed the
   operator dimension; `palace/linalg/arpack.cpp:518-521` clamps
   `ncv` (ARPACK's basis-size parameter) against the global dimension
   `N` (fetched via `N = linalg::GlobalSize(...)` at
   `palace/linalg/arpack.cpp:517`; the `arpack_it` default is set
   immediately after at `522-525`). At L1 this is a precondition on
   `E`'s opaque type.
```

### Change 5 — Promotion: drop the partly-constructive status gate

This change has four sub-edits (5a–5d) that together drop the transient
`partly-constructive` status gate while preserving the permanent
forward-looking-reconstruction content note.

#### 5a — Justification-kind summary paragraph (lines 594-602)

```edit:book/src/L1-L0/eigsolve-mutation-rotation.md
OLD:
The theme as a whole is `structural` with one **partly-constructive**
sub-rewrite (Sub-pattern B's `LinearSolveFailed` materialisation
requires upstream behaviour change). A `lowering-verifier` audit in a
later cycle should confirm sub-pattern recognition is exhaustive over
the eigensolver L0 corpus, specifically that:
NEW:
The theme as a whole is `structural`. Sub-pattern B's
`LinearSolveFailed` materialisation is a **forward-looking
reconstruction** (the L0 surface does not currently produce the
variant; the rewrite shape is recorded forward-looking, grounded in
the negative anchor `palace/linalg/ksp.cpp:297-310`); this is a
permanent property of the rewrite, not an open status gate. The
cycle-012 `lowering-verifier` audit (embedded below) confirmed
sub-pattern recognition is exhaustive over the eigensolver L0 corpus,
specifically that:
```

#### 5b — Status section header line (line 885)

```edit:book/src/L1-L0/eigsolve-mutation-rotation.md
OLD:
`firm (structural; partly-constructive on Sub-pattern B LinearSolveFailed materialisation)` —
the four sub-pattern recognition rules are sketched at the section
NEW:
`firm (structural)` —
the four sub-pattern recognition rules are sketched at the section
```

#### 5c — Status section body: LinearSolveFailed note (lines 890-893)

```edit:book/src/L1-L0/eigsolve-mutation-rotation.md
OLD:
rewrite and the status sum-type derivation are structurally complete.
The `LinearSolveFailed` materialisation is documented as
partly-constructive (the L0 source does not currently produce the
variant; the rewrite shape is recorded forward-looking).
NEW:
rewrite and the status sum-type derivation are structurally complete.
The `LinearSolveFailed` materialisation is a **forward-looking
reconstruction** — the L0 source does not currently produce the variant
(negative anchor `palace/linalg/ksp.cpp:297-310`: `void`-returning
`Mult`); the rewrite shape is recorded forward-looking, requiring the
one-line `BaseKspSolver::GetConverged` forwarder (or a `Mult`
status-return) per Sub-pattern B. This is a permanent honest property
of the rewrite, not a status gate.
```

#### 5d — Status section: replace the promotion-gate paragraph with the closure record (lines 895-902)

```edit:book/src/L1-L0/eigsolve-mutation-rotation.md
OLD:
Promotion to fully firm (i.e., dropping the `partly-constructive` caveat
on Sub-pattern B) is gated on either (a) an upstream Palace refactor
that captures `ksp->GetConverged()` at the ten callsites and
propagates the failure to the eigensolver outer-loop status, or (b) a
`lowering-verifier` audit that confirms the partly-constructive shape
is acceptable as a methodology-level pattern (per cycle-010 lifter Open
Questions §3, which forwards the pattern to cycle-012 meta-phase for
codification).
NEW:
**Promotion record (cycle-013).** This theme was promoted from
`firm (structural; partly-constructive on Sub-pattern B
LinearSolveFailed materialisation)` to `firm (structural)` via the
Status-gate option (b): the cycle-012 `lowering-verifier` audit
(embedded above, `audit_verdict: confirms-with-refinement`) confirmed
the structural decomposition (ten `opInv->Mult` callsites exhaustive;
negative anchor confirms `void` return) and the cycle-012 meta-phase
codified `partly-constructive` as a first-class methodology pattern
(per cycle-010 lifter Open Questions §3). The cycle-013 abstractor
dispatch
(`reports/2026-05-28T143232Z-abstractor-eigsolve-getconverged-forwarder-fix-and-gated-promotion/`)
then applied the three audit-identified firming edits — the
`GetConverged` forwarder snippet correction (Edit 2; the gate's named
blocker), the ARPACK `SetWhichEigenpairs` switch attribution
refinement, and the ARPACK ncv-clamp citation refinement. The transient
`partly-constructive` status gate is therefore closed. The honest
forward-looking-reconstruction content note (Sub-pattern B's
`LinearSolveFailed` is built from negative anchors because Palace's
`void`-returning `Mult` does not positively produce it) is a permanent
property and remains in the prose; it is not a status gate. Per the
CLAUDE.md "Theme/operator status `partly-constructive` is first-class"
invariant, the negative anchors are evidence FOR the faithful
reconstruction and do not license asserting a positive claim — a future
upstream Palace refactor that ships the forwarder + status-capture would
turn the forward-looking reconstruction into a positively-anchored
rewrite, but that is an enhancement, not a precondition for the firm
status.
```

## Speculative operators proposed

**None.** This dispatch corrects citations + a snippet and drops a status gate on an existing firm theme; it introduces no new vocabulary. (The theme's own §"Speculative L1 operators" remains "None" — unchanged.)

## Supporting evidence

All ranges read this cycle via `mcp__palace-codemap__read_range`:

- `palace/linalg/ksp.hpp:28-72` — `BaseKspSolver`; `ksp` member protected at 41; public surface 50-71; `GetRelTol` forwarder at 64; no `GetConverged`.
- `palace/linalg/iterative.hpp:98` — `IterativeSolver::GetConverged`.
- `palace/linalg/arpack.cpp:236-239` — `SetWhichEigenpairs` trivial field-set.
- `palace/linalg/arpack.cpp:279-305` — `SolveInternal` per-`WhichType` switch; `MFEM_ABORT` at 301-304.
- `palace/linalg/arpack.cpp:517` — `N = linalg::GlobalSize(...)`.
- `palace/linalg/arpack.cpp:518-521` — ncv-clamp.
- `palace/linalg/arpack.cpp:522-525` — `arpack_it` default.
- `book/src/L1-L0/eigsolve-mutation-rotation.md` — the theme under edit, including the embedded cycle-012 audit block (lines 751-902) and `## Status` section (883-911).

## Open questions / caveats

1. **(For meta-phase, informational — the mechanism worked.)** This was the first live test of the cycle-012 `partly-constructive` promotion mechanism. The reading was clean: the `## Status` gate's option (b) and the CLAUDE.md invariant's "Do NOT mark such an entry firm" clause did NOT conflict, because the invariant scopes "firm" to "no open promotion condition + structural decomposition confirmed," and the promotion condition (a lowering-verifier audit accepting the shape) had closed. No forced promotion was needed. The meta-phase may wish to note the precedent: a `partly-constructive` → `firm` promotion is a TWO-dispatch protocol — (i) lowering-verifier confirms + identifies the firming edits (UNBLOCK), (ii) a follow-up dispatch applies the edits + drops the gate (ENACT) — and the edits must be APPLIED in the enacting pass, never deferred.

2. **ncv-clamp exact boundary (cosmetic).** The audit note phrased the clamp as "518-520"; the literal block including the closing brace is `518-521` (assignment body at 520). I cited `518-521` for the full `if`-block in Change 4 to be exact. If the integrator or a future audit prefers the audit's `518-520` (assignment-inclusive, brace-exclusive) phrasing, either is defensible; the load-bearing facts (N at 517, clamp ~518-521, arpack_it default 522-525) are unaffected.

3. **The embedded cycle-012 audit YAML block (lines 762-881) was left as-is.** Its `partially-supports` entries on `ksp.hpp:30-72` and `arpack.cpp:236-308` accurately record the *pre-fix* state and the audit's reasoning, and the `audit_note` documents the gating decision. The audit block is a historical record of the cycle-012 audit; the fixes it identified are now applied in the prose above. I did not rewrite the audit record (it would falsify the historical audit). A future cleanup could append a one-line "resolved cycle-013" marker to those two YAML entries, but that is optional and out of scope for this gated-promotion dispatch.

4. **No `book/` or scaffolding mutation performed.** Per the cycle-012 write-authority phase-boundary lesson, this dispatch emitted proposed-changes only. integrator-per-report applies Changes 1-5.
