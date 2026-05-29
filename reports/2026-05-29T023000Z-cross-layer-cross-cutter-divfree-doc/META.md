---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T031500Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-29T034500Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: repaired
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "Cross-layer observation — divfree.hpp Mult doc-comment irrotational-vs-divergence-free tension"

## Critique

### Checks run

**citation-validity — pass.** I independently verified every CRUX citation via `palace-codemap read_range` (no self-verification trust). All confirmed firsthand:
- `divfree.hpp:28-31` class doc — VERIFIED: "projection onto a divergence-free space satisfying Gᵀ M x = 0" (text on `:28-30`, trailing `//` on `:31`).
- `divfree.hpp:63-66` — VERIFIED: `:63` is `void Mult(VecType &y) const;`; `:64-66` is the method doc comment "compute the Nedelec dofs of the irrotational portion ... will satisfy ∇ x y = 0." The inversion relative to the class doc is real and exactly as described.
- `divfree.hpp:68-72` out-of-place wrapper `{ y = x; Mult(y); }` — VERIFIED.
- `divfree.cpp:155-190` `Mult` body — VERIFIED: the four-step trace (WeakDiv→Mult, SetSubVector BC-zero, ksp→Mult, Grad→AddMult `+1.0`) matches the source line-for-line, including the `Vector`/`ComplexVector` instantiations at `:189-190`.
- `divfree.cpp:119` "The system matrix for the projection is real and SPD." — VERIFIED at `:119`.
- `mixedvecgrad.cpp:202` — VERIFIED: `PopulateCoefficientContext(space_dim, Q, transpose, -1.0)` carries the negating `-1.0` at `:202`, substantiating `WeakDiv = -Gᵀ`.
- Firm-entry pins — VERIFIED: `book/src/L1/divfree-projector.md:137` (projector `P = I − Grad(GᵀMG)⁻¹GᵀM`), `:145-150` (stale-comment annotation, citing the comment as `:64-66`); `book/src/L1-L0/divfree-projector-mutation-rotation.md:175-181` (sub-pattern B citation, cites `:63-66`), `:460-468` (§Open-questions stale-comment bullet, cites `:63-66`).
- Scaffolding pins — VERIFIED: `integrator-signals.md:158` (OQ "unblocked", verbatim "a documentation-fidelity caveat in Palace source, NOT a theme defect"), `priorities.md:27` (plan item #6, struck/DISPATCHED), `cycle-019-resume-notes.md:88`. The report's claim that the slug is NOT in `open-questions.md` is also confirmed (grep returns zero hits in that file).

**surface-or-evidence — pass.** The Hodge/Helmholtz reasoning is grounded in the code, not asserted. The chain is concrete: `WeakDiv` carries `-1.0` (`mixedvecgrad.cpp:202`) ⟹ `WeakDiv = -Gᵀ` ⟹ the additive `Grad->AddMult(psi,y,1.0)` net-*removes* the gradient (irrotational) component ⟹ output is the divergence-free remainder `Gᵀ M y' = 0`. Each link cites the source site that materializes it. Strong independent corroboration the report did not exploit: Palace's OWN inline implementation comment at `divfree.cpp:176` reads "Compute the irrotational portion of y and subtract." — i.e. the source itself states the irrotational part is what gets subtracted, leaving the divergence-free remainder. This is a third L0 witness (beyond the class doc and the sign-trace) against the method doc-comment. Its omission is not a defect; it would have strengthened an already-sound case.

**rotation-quality — pass (verdict-soundness sense; not a structural rotation).** This is an observation/resolution report, not an algebraic-rotation proposal, so the rotation-quality check applies as "is verdict (a) resolve faithful." It is. The method-comment is genuinely inverted (verified firsthand), and the firm entries already pin the correct divergence-free semantics. **On the (a)/(b)/(c) adjudication: (a) resolve is correct.** The source is unambiguous — the class doc (`:28-31`), the implementation (`:155-190`), the sign trace (`mixedvecgrad.cpp:202`), AND the inline source comment (`:176`) are mutually consistent and decisive; only the single method doc-comment deviates. (b) re-anchor is unwarranted (the artifact's L1/L1-L0 "divergence-free" claim is already faithful, with citations). (c) non-actionable is wrong (the actionable step is OQ closure of a 2+-batch carry-forward — leaving it lingering is the migration defect CLAUDE.md warns against). The resolution genuinely CLOSES the OQ rather than prematurely papering over a real ambiguity: there is no real ambiguity, only a stale comment.

**variant-axis-coverage — pass (n/a to report shape).** No orthogonal variant axes to cover — this is a documentation-fidelity adjudication. The report does note the in-place/out-of-place `Mult` variant pair (`:63` in-place, `:68-72` out-of-place) but correctly treats them as out of scope for the doc-comment question (both inherit the same inverted method-comment semantics). Not applicable to this report-kind.

**cross-reference-integrity — pass.** All references resolve. The two firm slugs (`divfree-projector`, `divfree-projector-mutation-rotation`) exist and are wired into `SUMMARY.md` (`:66`, `:81`). The optional proposed-change is plain-text-safe: it replaces prose-text inside an existing §Open-questions bullet (citations stay as plain-text `file:line` form, no new live `[link]` introduced). The flagged minor citation-range divergence (`:63-66` in the L1-L0 theme vs `:64-66` in the L1 entry for the same comment site) is surfaced explicitly — NOT silently resolved — with a correct disposition (both defensible: `:63-66` bundles the declaration the comment documents, `:64-66` is the comment text alone; line `:63` IS the declaration, confirmed firsthand). Correctly deferred to a future normalization pass rather than acted on here.

**edge-label-fidelity — pass.** The report carries an L1↔L0 cross-cut framing and the prose discusses exactly that edge (L0 source doc-comment fidelity vs the L1/L1-L0 artifact's divergence-free claim). No edge-label mismatch.

**plan-kind-consistency — pass.** Declared as a cross-layer observation/resolution with an OPTIONAL one-line cross-link proposed-change; the content matches that shape. The proposed-change is well-formed: the OLD block matches the live file text at `book/src/L1-L0/divfree-projector-mutation-rotation.md:460-468` byte-for-byte (verified firsthand), and the NEW block changes zero semantics as claimed — it sharpens the prose (names the authoritative class-doc site, states the inversion explicitly, records the closure cycle) while leaving the divergence-free claim and all step citations unchanged. The report appropriately flags it skippable for a zero-edit closure, and correctly notes that the actual OQ-ledger close is meta-phase unify-pass authority (not this dispatch's, not integrator-per-report's).

**skill-uptake-survey — warning.** The report's shape implies relevant skills exist but none is referenced as invoked. `verify-citation-range` is the obvious fit for the firsthand `read_range` verification the report performed (and was extended cycle-012 with an inherited-citation sub-case directly relevant here, where the report adjudicates two firm entries that inherited the same stale-comment citation). The report says it verified citations "firsthand via codemap read_range" but does not name the skill. Pure-telemetry surface, non-blocking: the verification was done correctly; only the skill-invocation reference is absent.

### Issues found

1. **[low] Skill invocation not referenced (skill-uptake-survey).** CYCLE.md §Summary and §Supporting-evidence assert firsthand `read_range` citation verification but do not name `verify-citation-range` (whose cycle-012 inherited-citation sub-case is directly on-point for adjudicating the two firm entries' shared stale-comment citation). Telemetry only — the verification itself is sound. (CYCLE.md:20, :215.)

2. **[info] Stronger uncited L0 corroboration available (surface-or-evidence; not a defect).** Palace's own inline implementation comment `palace/linalg/divfree.cpp:176` — "Compute the irrotational portion of y and subtract." — is a third independent L0 witness that the irrotational component is the *removed* part, directly corroborating the inversion claim. The report cites the `Grad->AddMult` step (`:177-186`) but not the `:176` comment. The verdict stands without it; flagged as an available strengthening anchor for the optional proposed-change. (CYCLE.md:79-80, :230.)

3. **[info] Minor cross-entry citation-range divergence (cross-reference-integrity; correctly self-surfaced).** The two firm entries cite the same stale-comment site with a one-line boundary difference (`:63-66` in the L1-L0 theme at `:175` and `:460`; `:64-66` in the L1 entry at `:146`). Verified firsthand: `:63` is the `Mult` declaration, `:64-66` the comment proper — both citations defensible. The report flags this explicitly and defers it (no new OQ); recorded here for the integrator. Not blocking. (CYCLE.md:124-134, :260-266.)

4. **[info] Closure is recommendation-only, by correct authority partition.** The report adjudicates the OQ as resolved/closure-ready but does not (and cannot) close it — `scaffolding/open-questions.md` close/unify is meta-phase authority, and the slug is currently tracked only via `priorities.md:27` + `cycle-019-resume-notes.md:88` (not present in the OQ ledger, confirmed firsthand). The report correctly routes closure as Recommendation #1 and flags the lingering-without-migration defect to re-raise if the next meta-phase does not act. No defect; noted so the integrator/meta-phase do not assume the ledger close already happened. (CYCLE.md:138-148, :253-259.)

## Repair

### Fixes attempted

- **Finding**: [info, surface-or-evidence] A third independent L0 witness — Palace's own inline comment `palace/linalg/divfree.cpp:176` "Compute the irrotational portion of y and subtract." — corroborates the inversion (the irrotational component is the *removed* part). The report cited the adjacent `:177-186` step but not the `:176` comment.
  - **Decision**: repaired
  - **Action**: Verified the comment text firsthand via `palace-codemap read_range` (`divfree.cpp:174-188`) — confirmed `:176` reads exactly `// Compute the irrotational portion of y and subtract.`, sitting immediately above the `Grad->AddMult(... 1.0)` step (`:177-186`). Folded the `:176` witness in at three surgical sites in CYCLE.md, all additive (zero existing text removed, zero semantics changed):
    1. §"Which component the projector actually produces" step 4 (CYCLE.md ~:80) — added the inline-comment citation as a third L0 witness alongside the existing `:177-186` step citation.
    2. §"Supporting evidence" L0 list (CYCLE.md ~:230) — added a `divfree.cpp:176` bullet describing it as the third independent witness.
    3. §"Proposed-changes block" NEW replacement text only — added the `:176` confirmation clause after the implementation-realises-class-doc clause. The OLD block was left untouched, so it still matches `book/src/L1-L0/divfree-projector-mutation-rotation.md:460-468` byte-for-byte; the NEW block remains semantics-preserving (it now cites one additional corroborating L0 site, no claim change).

- **Finding**: [low/warning, skill-uptake-survey] `verify-citation-range` was effectively used (firsthand `read_range` verification) but not named in CYCLE.md. Telemetry only.
  - **Decision**: not-needed
  - **Rationale**: Pure telemetry, as the critic noted — the verification was performed correctly; only the skill-invocation reference is absent. Naming a skill retroactively in an append-only report's prose is not a mechanical citation/structure fix and would not change any content or claim. The critic surfaced it explicitly; no surgical edit improves the artifact. Non-blocking.

- **Finding**: [info, cross-reference-integrity] Minor cross-entry citation-range divergence between the two firm entries (`:63-66` in the L1-L0 theme vs `:64-66` in the L1 entry) for the same stale-comment site.
  - **Decision**: not-needed
  - **Rationale**: Both citations are defensible (verified firsthand by the critic: `:63` is the `Mult` declaration, `:64-66` the comment proper). The report self-surfaced this and correctly deferred it to a future harvester/verifier normalization pass — it concerns the artifact (`book/`), which the repairer must not touch, and the report itself is not in error.

- **Finding**: [info, plan-kind-consistency] Closure is recommendation-only by correct authority partition (OQ-ledger close is meta-phase unify-pass authority).
  - **Decision**: not-needed
  - **Rationale**: No defect — the report routes closure correctly as Recommendation #1. Authority-partition observation for the integrator/meta-phase, not a repairable item.

### Unrepairable findings

None. The one substantive enhancement (the `:176` witness) was a clean additive citation that slotted in without re-authoring any claim; all other items are telemetry / authority-partition notes / artifact-side deferrals that are correctly out of repair scope.

## Suggested resolution

`ready` — verdict (a) resolve is confirmed correct (critic passed citation-validity + 6 other checks, independently re-verified all CRUX citations). Notes for the integrator:

- The proposed-changes block is **OPTIONAL** (the report flags it skippable for a zero-edit closure); it is well-formed and the OLD block still matches the live file byte-for-byte after the repair. If applied, it now records the `:176` third-witness corroboration. The resolution stands on 4 (now 5, counting the `:176` comment) mutually-consistent L0 witnesses regardless.
- The actual OQ-ledger close of `divfree-mult-doc-irrotational-vs-divfree-stale` is **meta-phase unify-pass authority** (the slug is tracked via `priorities.md:27` + `cycle-019-resume-notes.md:88`, NOT yet in `open-questions.md`). The integrator-per-report should not assume the ledger close has happened; surface the closure-ready disposition to the meta-phase.
