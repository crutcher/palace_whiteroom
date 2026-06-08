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

# META: verification of "L4 roadmap_goal extension — sharding-decompose-reduce solve-generalization sketch"

## Critique

This report is a `roadmap_goal` (rank 0) extension of an existing rank-0 chapter. Per the GRADED RESOLUTION LADDER directive, a rank-0 node is claim-free: it makes no positive algebraic claim, so the citation/surface/rotation/variant-axis checks are evaluated under the adapted rank-0 lens (verify provenance + intent + pulled-by + declared deps + SUMMARY wiring; verify that no *claim* leaked in; verify the edge-typing does not manufacture a rank violation). The five HARD GATES named in the dispatch (stays rank-0; `reference`-only edge-typing; MPI cited-not-lifted; honest NON-law; fenced pseudocode) are load-bearing and were each checked against the proposed-changes on disk.

### Checks run

**citation-validity — pass.** `citecheck --scan` on the report returned 10 ok, 2 AMBIG. The 2 AMBIG (`inner_product.md:154-157`, `linear_combination.md:146-151`) are exactly the two the report's prose pre-disclosed (CYCLE.md §Finding line 35, and §Open-questions): they are **bare-basename mentions in report PROSE**, not in the in-chapter edit blocks. I verified the claim that the in-chapter edits use unambiguous relative links: `grep` over `book/src/L4/sharding-decompose-reduce.md` shows every link is `./`-prefixed (`./inner_product.md`, `./linear_combination.md`, `./ksp_solve.md`, `./fold_solve.md`, `./krylov-step.md`, `./domain_energy_reduce.md`, `./gram_reduce.md`) or `../L2/gram.md` — ZERO bare-basename `](foo.md)` links in the chapter. So the AMBIG is a report-prose artifact only and does not enter the artifact; not a defect. The load-bearing Palace L0 cites all resolve + anchor via `citecheck --anchor`: `geodata.cpp:261-262` (anchor `Partition`), `:3230` (`GetMeshPartitioning`), `:3242` (`subdomain`), `rap.hpp:24` (`ParOperator`), `rap.cpp:116-126` (`RAP`), and the negative-anchor `romoperator.cpp:586` (`overlap`) all OK. The `verified_against:` YAML block in the chapter round-trips under `yaml.safe_load` (no leading-quote-scalar defect; every `note:` opens with prose). The `Partition` `:262`-vs-`:261-262` discrepancy the report self-notes (CYCLE.md:276) is a deferred-mechanism cite, in-range either way — correctly flagged as not-a-defect.

**surface-or-evidence — pass (rank-0 adapted).** This is not a refinement of an existing operator's surface; it is a claim-free `roadmap_goal` extension. Its "evidence" is the firm-root composition by name + the deferred-mechanism L0 cites, all of which resolve. Record-definition sub-check: the speculative signatures name `IndexBlock` / `Partition` / `LinOp[…]` / `Tensor[…]` — `LinOp`/`Tensor` are established semantic-surface types; `Partition`/`IndexBlock` are the speculative `roadmap_goal` types whose definition home IS this accreting chapter (they are sketched in-line, NO claim asserted), which is the correct disposition for rank-0 speculative forms. No signature-named record is stranded "described only by use."

**rotation-quality — pass (no-op for rank-0 sketch).** No algebraic/reduction rotation is *claimed* — the node is claim-free. The report is in fact scrupulous about the opposite: the load-bearing §Finding records that the solve case has NO free recovery law (strictly weaker than the reduce case's homomorphism), recorded as a config-conditional NON-law rather than a manufactured rotation. Not applicable to the rank-0 kind; marked pass.

**variant-axis-coverage — pass.** The relevant variant axis — block-diagonal (exact) vs coupled (approximate additive-Schwarz) vs overlapping (partition-of-unity-weighted) operator structure — is explicitly enumerated and scoped, not hidden. The coupled and overlapping branches are carried as EXPLICIT config-conditional NON-laws (proposed laws-block edits, CYCLE.md:142-152, 160-183), mirroring `domain_energy_reduce`'s `Σ pᵢ = 1` axis. No hidden branch.

**cross-reference-integrity — pass.** All 8 `reference:` slugs in the proposed frontmatter edit resolve on disk (`domain_energy_reduce`, `inner_product`, `linear_combination`, `gram_reduce`, `ksp_solve`, `fold_solve`, `krylov-step` under L4; `gram` under L2). The maturity claims are verified: `ksp_solve` / `fold_solve` / `krylov-step` are each `rank: firm` on disk, matching the report's "firm SOLVE roots" claim. **Edge-typing gate (load-bearing, verified):** the three NEW solve roots are added under `reference:` ONLY — there is no `depends-on` block on the node, so no firm→rank-0 `depends-on` is manufactured and `rank_violations` stays 0. This is the critical rank-invariant guard and it holds.

**edge-label-fidelity — pass.** No L_{n+1}→L_n lowering edge label is carried (this is an in-L4 roadmap_goal extension, not a lowering theme). Not applicable.

**plan-kind-consistency — pass.** Declared kind `roadmap_goal` (rank 0) matches content shape exactly: claim-free, every form prefixed `SPECULATIVE (roadmap_goal)`, the `## Status` block reaffirms rank-0, the promotion-pull OQ is held deferred (CYCLE.md:25, 200, 273), and the three speculative operators are explicitly recorded as accreting working-context, NOT landed as dep-map rough-in rows. The node STAYS rank-0 — verified against the unchanged `rank: roadmap_goal` / `status: roadmap_goal` frontmatter (no frontmatter rank edit is proposed). DIRECTIVE-1 boundary held: MPI/distributed (`rap.*`, `geodata.cpp`, MPI collectives) is cited as deferred-future MECHANISM only, in the accreting-context + Evidence sections, never lifted as active content.

**skill-uptake-survey — pass.** The report references `citecheck --anchor` self-verification (chapter Evidence line 249) — the relevant skill for the L0-citation shape is surfaced and invoked. No other skill-shaped obligation implied.

### Issues found

No issues. All 8 checks pass. The five HARD GATES verified clean against the on-disk proposed-changes:

1. Node STAYS rank-0 `roadmap_goal` — frontmatter `rank`/`status` unchanged; promotion-pull OQ held deferred.
2. NEW solve roots added under `reference:` ONLY (no `depends-on` block exists) — no `rank(firm)=3 > 0` violation manufactured; `rank_violations` stays 0.
3. MPI/distributed cited as deferred MECHANISM only (DIRECTIVE-1 boundary intact) — not lifted as active content.
4. The solve-case NON-law is stated HONESTLY (config-conditional: block-diagonal exact / coupled approximate / overlapping p.o.u.-weighted) — no false free-recovery claim; correctly mirrors `domain_energy_reduce`'s `Σ pᵢ = 1` non-law model, whose precedent lines (`:147-152`, `:172-178`) were verified to back the framing.
5. Pseudocode is FENCED ```text — verified; all speculative forms in the proposed edits sit in `​```text` fences, and the on-disk chapter's fence parity is balanced (KaTeX `$`-sigil-fence rule satisfied).

The 2 `citecheck --scan` AMBIG flags are report-PROSE-only bare-basename mentions, pre-disclosed by the report; the in-chapter edits use unambiguous `./`-relative links exclusively. Not a defect — noted for telemetry, not flagged.

All 8 checks pass, so `overall_status: ready` is set per the all-pass clean-report rule (no repairer will run).
