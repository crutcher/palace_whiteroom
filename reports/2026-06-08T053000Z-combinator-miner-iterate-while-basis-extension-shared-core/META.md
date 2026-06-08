---
verifies: ../CYCLE.md
critiqued_at: 2026-06-08T061500Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
overall_status: ready
---

# META: verification of combinator-miner iterate-while-basis-extension-shared-core (NO-COMBINATOR finding)

## Critique

### Checks run

**citation-validity — pass.** Every cited file exists on disk and every load-bearing line range resolves and supports its claim. I verified all eight cited chapters exist (`iterate-while-dissolution.md` 176L, `correction_step.md` 442L, `eigsolve-impl.md` 195L, `chebyshev.md` 549L, `geometric-multigrid-preconditioner.L1.md` 112L, `krylov-step.md` 225L, `ksp_solve.md` 207L, `nleps-deflated-eigensolve.md` 477L) — no range overruns a file boundary. The load-bearing pinpoints all check out: `eigsolve-impl.md:63-84` is exactly the outer thick-restart `iterate_while_L3` (`:65`) + inner basis-extension `iterate_while_L3` (`:78`) with `append_column s step` (`:84`), and `:56` carries `BV : Tensor[(B: ncv), (S: ...), complex]` verbatim; `chebyshev.md:225-248` is the two `kloop`/`itloop` tail recursions (`kloop` `:237-244`, `itloop` `:246-247`) over the fixed `(rN, dN, _stN, yN)` carry at `:234`; `chebyshev.md:35-49` confirms "not a Krylov method," "inner-product-free," "no convergence test," and explicitly names the loops "`iterate_while_pure_L3` tail recursions over those static ranges" (`:46-49`) — directly backing the report's `iterate_while_pure_L3` framing; `geometric-multigrid-preconditioner.L1.md:51-58` is the level-stack `vcycle` recursion and `:61-62` the outer `iterate pc_it` Richardson sweep, with `:89-98` the `correction_step` leg annotation; `correction_step.md:36-53` is the shared-body kernel/driver split, `:78-81` the explicit over-unification guard ("The Krylov shift-invert step ... is NOT a `correction_step`"), `:283-294` the `B`-specializations (Chebyshev `:283-289`); `iterate-while-dissolution.md:55` is the `iterate_while_L3` ground form and `:97-98` the exact `iterate_while_pure_L3 :: α -> (α -> Bool) -> (α -> α) -> α` signature that backs the report's "`extend_while` is definitionally `iterate_while_pure_L3` with `α = WorkingSet`" rejection; `ksp_solve.md:88,135` the canonical `iterate_while_L3 (krylov-step op)` kernel/driver pair; `nleps-deflated-eigensolve.md:111-120` the fourth `iterate_while_L3` consumer (outer `:111`, inner `:120`). No drift found.

**surface-or-evidence — pass (no-op for no-mutation finding).** This dispatch proposes no surface change (no operator/theme text, no dep-map row) — it is a clean NO-COMBINATOR finding recorded as an OQ. There is no rotation_claim-without-surface to flag because there is no claim of a new combinator at all; the report explicitly declines to register one. No record is named in a new signature (the records cited — `BV`, the Chebyshev carry tuple — are referenced from existing firm chapters, not introduced here), so the record-definition sub-check does not fire.

**rotation-quality — pass (not applicable).** No rotation is asserted. The finding's content is that the candidate "basis-extension fold" would be identity-in-named-terms to `iterate_while_pure_L3` (i.e. NOT a rotation) — the report correctly self-applies the degenerate-identity smell to reject it. There is nothing to grade for compaction because nothing new is proposed.

**variant-axis-coverage — pass (not applicable).** No new operator with variant axes is proposed. The report does engage the divergence axes (level-stack vs growing-basis vs fixed-degree carry) — its whole argument is that these axes do NOT collapse to one combinator — but there is no hidden-branch surface to audit.

**cross-reference-integrity — pass.** All `[link]`-style references resolve and the "already-lifted" anchor claims are accurate on disk. The two combinators the finding rests on are both confirmed `firm`: `correction_step.md` `## Status` (`:349`) reads "`firm` — direct transcription ... at four positive source sites," and `iterate-while-dissolution.md` `## Status` (`:167`) reads "`firm` — extraction of an already-firm sub-component." `krylov-step.md` `## Status` (`:166`) is `firm`. The report's claim that eigsolve's basis-extension is "already expressed through the firm `iterate_while_L3` driver ... the per-step kernel is already the firm `krylov-step`" is precise: the *driver* and *kernel* are firm even though the `eigsolve-impl.md` chapter that COMPOSES them is `roadmap_goal` (`:5` frontmatter + `:134` `## Status` `kernel-impl` rank-0). The report does not overclaim the chapter's maturity — it calls eigsolve-impl "the only genuine basis-extension instance" and rests its firmness claim on the substrate (driver+kernel), which is correct. The OQ block (`[FINDING — record durably] iterate-while-basis-extension-no-shared-combinator`) is well-formed: it carries a slug, the negative verdict, the per-instance carry-shape divergence, the disposition ("no dep-map row, no new chapter"), and an explicit re-open condition (a fourth genuinely-growing-working-set instance distinct from `BV`). The hard-constraint caveat (no V-cycle node manufactured — GMG firm c122, a new node would be a forbidden rectangular pull-up) is honored and accurate.

**edge-label-fidelity — pass (not applicable).** No L_{n+1}→L_n edge label is carried; this is a cross-instance mining finding, not a lowering theme. The report does correctly attribute the lowering relationships it cites (L4>L3 `iterate-while-dissolution`, L1→L2 `correction_step` downward annotation), each discussed at the layer it names.

**plan-kind-consistency — pass.** The declared shape is a combinator-miner finding (verdict (b): no new combinator). The content matches: no candidate is registered, the "Proposed combinator" section reads "**NONE**," and the outcome is an OQ rather than a dep-map row — exactly the role-spec's "a finding about the spine is a legitimate, valuable outcome" path. No mis-classification (it is not dressed up as a firm operator or a rough-in row).

**skill-uptake-survey — pass (telemetry).** The report's shape (verify-citation-range over ~10 cited ranges, over-unification guard application) implies the `verify-citation-range` and over-unification-discipline procedures, but a clean no-combinator finding has no surface to gate on a skill invocation. No skill reference is strictly required for a finding-only dispatch; surfaced as telemetry, not blocking.

### Issues found

None blocking. Two minor, non-blocking observations (NOT defects — recorded for completeness, no repair warranted):

1. **Carry-tuple field-order transposition (cosmetic, not a citation error).** The report writes the Chebyshev carry as `(r, d, y, st)` (CYCLE.md:64, :132, :160), while the on-disk form at `chebyshev.md:234` is `(rN, dN, _stN, yN)` — i.e. `(r, d, st, y)`. The four-element fixed-arity-tuple claim (the load-bearing point — "no growing working set") is fully correct; only the positional order of the last two fields is transposed in the prose. This does not affect the finding and is below the threshold of a citation-validity drift (the cited range is correct and supports the claim).

2. **eigsolve-impl maturity is `roadmap_goal`, not `firm` — but the report does not claim otherwise.** Worth noting explicitly so a downstream reader is not misled: the `eigsolve-impl.md` chapter is rank-0 `roadmap_goal` (`kernel-impl`), while the report's firmness claims attach only to the *constituents* it composes (`iterate_while_L3`, `krylov-step` — both firm). The report's wording ("already expressed through the firm `iterate_while_L3` driver") is accurate and does not overclaim the chapter. No issue.
