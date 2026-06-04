---
name: foundation-blocker-dischargeability-probe
description: The cheap-probe-before-heavy-wave playbook for a convergent foundation-blocker. Before committing to a heavy firm-flip-and-cascade wave on a widely-consumed `rough-in (test-coverage-bounded)` operator, run a SCOPED single-file lowering-verifier probe that tests whether the firm-on-positive-structure escape applies — returning one of two clean outcomes (DISCHARGE → queue the cascade as a gated wave; CONFIRM-CEILING → record the explicit verdict, stay rough-in). The probe NEVER flips the maturity token and NEVER triggers the cascade. Audience: cycle-planner (sequences the probe-then-wave), lowering-verifier (runs the probe), meta-phase (GO/NO-GO the wave on the probe's verdict).
status: active
---

# foundation-blocker-dischargeability-probe

A **convergent foundation-blocker** is a `rough-in (test-coverage-bounded)` operator that gates a large downstream cascade — a widely-consumed primitive whose firm flip would unblock reduce-verbs and feature columns through it, but whose flip ALSO triggers a heavy ~30-file cross-reference re-anchor. Two costs are entangled: (1) the law-confidence question (can the verb flip at all?), and (2) the structural-wave cost (the wide cascade). This skill SEPARATES them: the cheap probe tests (1) in a single file BEFORE anyone pays (2).

This is the load-bearing FLOW pattern that converted the `matrix-weighted-norm` NO-GO from "held by inertia" to "GO by explicit derivation" without ever forcing the gate. The arc validated it by use across batches 27–29:
- **c088** — structure-side probe on `matrix-weighted-norm`'s norm-axiom laws (triangle / Cauchy–Schwarz / parallelogram): DISCHARGE (inner-product-space theorems on provably-SPD `B = KM`).
- **c089** — FP-side probe on the same verb (`:69-70` floating-point sub-claims): DISCHARGE (inherit verbatim/additively from firm `dot` + `apply_linop` via the deterministic-√ `nrm2` precedent).
- batch-28 meta-phase judged the sole remaining gate (a 4-arg √-entry-point test) REDUNDANT → the firm flip GO'd as the batch-29 LEAD; the c091 cascade LANDED CLEAN (3 firm promotions).
- **c092** — probe on `bilinear-form` (the next convergent blocker, sole residual gate on `gram_reduce`): DISCHARGE (laws 1-6 syntactic read-offs over firm `dot`+`apply_linop`, NO norm-axiom theorem content; laws 7-8 M-symmetry-conditional with on-disk witnesses) → the `bilinear-form-firm-flip-and-cascade-wave` GO'd as the batch-30 LEAD.

The probe's "likely outcome is a clean confirmation of the ceiling, which is itself the load-bearing finding" — a CONFIRM-CEILING converts a NO-GO from inertia-held to verdict-held, which is a genuine spec finding, not a failure.

## When to invoke

- A `cycle-planner` is weighing whether to dispatch a heavy firm-flip-and-cascade wave on a widely-consumed `rough-in (test-coverage-bounded)` operator (or whether to NO-GO-hold it). Run the probe FIRST as a cheap LEAD; the cascade is a SEPARATE gated wave.
- A `lowering-verifier` is dispatched on the scoped probe itself.
- A `meta-phase` is deciding GO/NO-GO on the heavy cascade wave and wants the dischargeability verdict in hand.

Do NOT invoke for a fresh authoring or a routine rough-in→firm where there is no wide cascade — that is the ordinary harvester/lifter path. This skill earns its keep ONLY when a heavy structural wave hangs on the law-confidence question.

## The probe (the SCOPED dispatch)

1. **Scope to ONE file.** The probe touches ONLY the operator's own chapter (`book/src/L*/<op>.md`). It does NOT touch consumers, reduce-verbs, feature columns, or any index. The cascade is a later, separate wave.

2. **Test the firm-on-positive-structure / syntactic-identity escape** (CLAUDE.md §Methodology invariants, the `rough-in (test-coverage-bounded)` "firm-on-positive-structure escape"). The two-condition rule: the escape applies iff **(i)** all folded/constituent primitives are firm AND **(ii)** the operator's laws are syntactic identities / read-offs over that firm structure, with NO smuggled-in mathematical-property content that only a (missing) positive test could confirm. Walk every law:
   - A law that is a **syntactic read-off** over firm constituents (pure linearity, annihilation, identity-specialization, concatenation-homomorphism inherited from a firm fold) → discharged-by-inheritance. Cite the firm constituent's law.
   - A law that is an **exact-arithmetic theorem** whose premise is **provably-by-construction** at the usage sites (e.g. an inner-product-space norm axiom on a provably-SPD operator with a positive L0 home for the SPD premise) → discharged-by-structure. Cite the theorem + the construction-attested premise.
   - A **floating-point** sub-claim that inherits verbatim/additively from firm constituents through a deterministic composition (disjoint accumulators, deterministic outer op) with NO composition-specific FP property arising → discharged-by-constituent-inheritance. Cite the constituent's FP caveat + the `nrm2`-style precedent.
   - A law that **genuinely needs a positive test** the corpus lacks (a true mathematical property the source only numerically asserts and no firm constituent supplies) → NOT discharged. This is a real ceiling.

3. **Judge the remaining test-gate REDUNDANT or LOAD-BEARING.** If every law is discharged by (read-off / structure / constituent-inheritance), the missing direct test would only re-confirm already-anchored properties — it is **REDUNDANT**, the escape APPLIES, the verb is firmable. If any law's only possible evidence is the missing test, the gate is **LOAD-BEARING** and holds the verb at rough-in. (Materially the same situation as the prior escape promotions `apply_linop` / `eigenfreq_qfactor_reduce` c082 / `sparameter_reduce` c083 / `solve_family` c086.)

4. **Land ONE of two clean outcomes — NEVER flip the token, NEVER cascade:**
   - **(a) DISCHARGE** → land a `verified_against:` YAML block (the discharge evidence per the verb's laws) + a §Status narrowing that RECORDS the discharge — but the frontmatter `firmness:` STAYS `rough-in`. The firm flip + the wide cascade is a SEPARATE gated wave; queue it as a candidate (an OQ + a plan item) for the next planner / meta-phase to schedule.
   - **(b) CONFIRM-CEILING** → land an explicit-verdict §Status note recording WHY the gate is load-bearing (which law, what test it needs, why the corpus lacks it); the verb stays `rough-in (test-coverage-bounded)`; the cascade stays NO-GO-with-verdict.

   HARD CONSTRAINT both outcomes: do NOT flip the maturity token in the probe dispatch; do NOT touch the cross-reference cascade, the downstream reduce-verbs, any feature column, or the L1>L0 theme.

## The gated cascade wave (the SEPARATE follow-up, only on outcome (a))

Sequence the cascade as its OWN dedicated structural wave (a batch LEAD slot, NOT bundled into a land-clean or forward-frontier cycle — the cycle-071 reorg-wave / c091 cascade precedent). Apply the cascade discipline:
- **the within-file self-consistency re-anchor** (friction-ledger `firm-flip-leaves-within-file-stale-narration-in-flipped-operators-own-entry`) — on the flip, re-read the flipped operator's OWN file end-to-end and re-anchor every stale "stays rough-in" conclusion narration (gate bodies, Evidence conclusions, FP-residue sentences, Dependencies self-notes), not just the §Status line;
- **the whole-`book/src/` cross-reference re-anchor** (friction-ledger `firm-promotion-coupled-re-anchor-needs-whole-book-cross-reference-grep`);
- the coupled downstream re-judgments (reduce-verbs whose folded primitive just firmed may now meet condition (i) — but CAUTION: verify ALL folded primitives are firm; a residual gate is the honest partial outcome, NOT a forcing);
- the feature-column re-evaluations under the OWN-COMPOSITION rule.

## The discipline this skill enforces

- **Separate the law-confidence question from the structural-wave cost.** Never NO-GO-hold a blocker on inertia, and never run the heavy wave before the cheap probe says the flip is licensed.
- **A clean CONFIRM-CEILING is a WIN, not a failure** — it is an explicit spec finding (the verb is correctly bounded at rough-in by a named, evidenced gate).
- **The probe never forces the gate.** Two clean outcomes, both honest.
- Cite the `matrix-weighted-norm` (c088/c089) and `bilinear-form` (c092) probes + the firm-on-positive-structure escape precedents as the directly-applicable priors.
