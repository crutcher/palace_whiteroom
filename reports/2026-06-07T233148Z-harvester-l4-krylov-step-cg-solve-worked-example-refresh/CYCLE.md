---
agent: harvester
invoked_at: 2026-06-07T233148Z
scope: L4 operator: krylov-step (cg_solve worked-example call-form refresh)
status: integrated
integrated_at: 2026-06-07T235126Z
integration_commit: f1b69f1
integration_notes: "cycle-138 (batch-44 BATCH-CLOSING). Applied the single [old]->[new] edit to book/src/L4/krylov-step.md:192-197 (stale cg_solve Form-B worked-example -> canonical iterate_while_with_prev boot/init/steady/cont arg order + record returns). krylov-step stays firm; no dep-map/SUMMARY edit; edit inside the pre-existing ```text fence. DISCHARGES OQ synthesis-l4-krylov-step-worked-example-cg-solve-stale-vs-iterate-while-with-prev-signature; promoted OQ iterate-while-with-prev-evidence-prose-stale-cg-call-shape. cargo make book EXIT 0; step-5c KaTeX assertion PASS. retroactive-budget 0."
inputs:
  - book/src/L4/krylov-step.md:192-198 (the stale cg_solve Form-B worked example)
  - book/src/L4/iterate-while-with-prev.md:44-52 (authoritative signature + canonical arg order)
  - book/src/synthesis/iteration.md:278-298 (the c137-audited faithful synthesis rendering of cg_solve)
  - OQ synthesis-l4-krylov-step-worked-example-cg-solve-stale-vs-iterate-while-with-prev-signature
  - c137 lowering-verifier audit (surfaced the latent drift)
---

# CYCLE: Refresh stale `cg_solve` worked-example call form at L4 krylov-step

## Summary
The `cg_solve` Form-B worked example in `book/src/L4/krylov-step.md` calls `iterate_while_with_prev`
in a **stale older positional+tuple form** that predates the authoritative `iterate_while_with_prev`
signature now firm at `book/src/L4/iterate-while-with-prev.md`. The c137 lowering-verifier audit
confirmed the SYNTHESIS rendering (`synthesis/iteration.md`) is already faithful to the CURRENT
signature; it is this L4 chapter's OWN worked example that drifted. This is a **surgical call-form
refresh only** — the example's semantics (CG v0.5 first-iteration-unrolled solve) are unchanged;
only the spelling of the `iterate_while_with_prev` invocation is updated to the canonical
boot/init/steady/cont arg order with record returns. `krylov-step` stays `firm`; no status,
signature, law, or evidence change. This discharges OQ
`synthesis-l4-krylov-step-worked-example-cg-solve-stale-vs-iterate-while-with-prev-signature`.

## The defect (what drifted)

The stale call (`krylov-step.md:192-197`):

```text
      let { final_state, trajectory } =
        iterate_while_with_prev s1 s0.beta
          (\(s, _) -> s.it < config.max_it && not s.converged)
          (\(s, beta_prev) ->
            let r = cg_steady_step opA eps beta_prev s in
            (r, s.beta)) in
```

is non-conformant with the authoritative signature in **three** ways:

1. **No `bootstrap_step` argument.** The authoritative signature
   (`iterate-while-with-prev.md:44-49`) takes `bootstrap_step` as its **first** argument;
   the stale call passes `s1` (an initial carry) where `bootstrap_step` belongs, omitting
   the bootstrap entirely.
2. **Wrong argument order.** The canonical order is **boot, init, steady, cont**
   (`iterate-while-with-prev.md:52` "bootstrap_step first, init second, steady_step third,
   cont fourth"). The stale call has the predicate (`cont`) in the **third** position and the
   steady body **last** — both misplaced.
3. **Bare-tuple step return.** The stale steady lambda returns `(r, s.beta)` — a positional
   2-tuple. The authoritative `steady_step` returns a **record** `{ state: α, prev: β, ...e }`
   (`iterate-while-with-prev.md:47`); the trajectory's extras (`residual_norm`) ride in the
   record, not in a tuple slot. The `cg_steady_step` result `r` is itself a
   `{ state, residual_norm }` record, so the bare tuple also drops the extras spelling.

The c137-audited faithful synthesis rendering (`synthesis/iteration.md:291-297`) is the reference
for the correct shape: boot first, init second, steady third (record return with `residual_norm`),
cont last.

## The fix (canonical call form)

The refreshed call, matching the authoritative signature and consistent with the faithful
synthesis rendering:

```text
      let { final_state, trajectory } =
        iterate_while_with_prev
          (\_ -> pure { state: s1, prev: s0.beta })            -- bootstrap: seed (s1, beta_prev = s0.beta)
          s1                                                    -- initial carry
          (\(s, beta_prev) ->                                  -- steady_step: (carry, prev)
            let r = cg_steady_step opA eps beta_prev s in
            pure { state: r.state, prev: s.beta, residual_norm: r.residual_norm })
          (\s -> s.it < config.max_it && not s.converged) in   -- cont: pure on carry, fires LAST
```

This is identity-in-semantics to the prior example: the same `cg_first_step` has already produced
`s1` and `res1`; the bootstrap seeds the carry `s1` with the initial `prev = s0.beta` (the
`beta_prev` the first steady step needs), each steady step threads `s.beta` forward as the next
`prev`, the predicate reads the carry only, and `residual_norm` rides the trajectory record. The
`residual_history` accumulation line below (`:198`) is unchanged — `trajectory.map(\t -> t.residual_norm)`
already reads the record's `residual_norm` field, which the refreshed steady-return now supplies
by name (the bare-tuple form had left this field-access implicitly dangling).

The leading prose at `:176` ("`iterate_while` over the pair `(state, beta_prev)`") still reads
correctly against the refreshed form — the `prev` is threaded as the closure carry exactly as
described; per the SEMANTIC CONSOLIDATION discipline this worked example continues to **link** to
`iterate-while-with-prev` for the combinator's semantics rather than restate them.

## Proposed changes

```edit:book/src/L4/krylov-step.md
[Replace the stale `iterate_while_with_prev` call (the indented code block at lines 192-197,
inside the `cg_solve` fenced block) with the canonical boot/init/steady/cont form.]

OLD (exact):
      let { final_state, trajectory } =
        iterate_while_with_prev s1 s0.beta
          (\(s, _) -> s.it < config.max_it && not s.converged)
          (\(s, beta_prev) ->
            let r = cg_steady_step opA eps beta_prev s in
            (r, s.beta)) in

NEW (exact):
      let { final_state, trajectory } =
        iterate_while_with_prev
          (\_ -> pure { state: s1, prev: s0.beta })            -- bootstrap: seed (s1, beta_prev = s0.beta)
          s1                                                    -- initial carry
          (\(s, beta_prev) ->                                  -- steady_step: (carry, prev)
            let r = cg_steady_step opA eps beta_prev s in
            pure { state: r.state, prev: s.beta, residual_norm: r.residual_norm })
          (\s -> s.it < config.max_it && not s.converged) in   -- cont: pure on carry, fires LAST
```

No dep-map edit (`book/src/L4/index.md`): `krylov-step` stays `firm`; no edge, status, or
cohort-bullet change — this is a within-body fidelity fix, not a promotion.

No SUMMARY.md edit: the chapter is already registered.

## Verification against authoritative signature (on disk)

- `book/src/L4/iterate-while-with-prev.md:44-49` — authoritative `Solve`-threaded signature:
  `bootstrap_step :: (α -> Solve { state: α, prev: β, ...e })` first; `init :: α` second;
  `steady_step :: ((α, β) -> Solve { state: α, prev: β, ...e })` third; `cont :: (α -> Bool)` fourth;
  returns `Solve { final_state: α, trajectory: [{ ...e }] }`. The refreshed call matches all four
  positions and the record-return shape.
- `book/src/L4/iterate-while-with-prev.md:52` — "the argument order: `bootstrap_step` first,
  `init` second, `steady_step` third, `cont` fourth" + "the `steady_step` closure-argument order
  `(α, β)` (carry first, prev second)". The refreshed steady lambda `\(s, beta_prev) -> ...` is
  carry-first, prev-second; confirmed.
- `book/src/synthesis/iteration.md:291-297` — the c137-audited faithful rendering of the SAME
  `cg_solve` call: bootstrap `(\_ -> pure { state: s1, prev: s0.beta })`, init `s1`, steady
  returning `pure { state: r.state, prev: s.beta, residual_norm: r.residual_norm }`, cont last.
  The refreshed L4 call is now consistent with this rendering (the synthesis rendering was correct;
  the L4 chapter's own example is brought into agreement with it).

The fix uses 4-space-indented code (the existing `cg_solve` block is fenced ` ```text `, so the
edit lands inside that fence). No `$`-sigil pseudocode is introduced (the example uses `$S` only in
the `cg_solve` type signature line, which is untouched and already inside the ` ```text ` fence —
KaTeX `$`-sigil-fence rule satisfied).

## Open questions / caveats

- **Secondary occurrence in `iterate-while-with-prev.md` is OUT of this single-operator scope but
  should be checked.** The combinator's own §Evidence at `book/src/L4/iterate-while-with-prev.md:233`
  describes "the prototypical use" as
  `iterate_while_with_prev s1 s0.beta (\(s, _) -> ...) (\(s, beta_prev) -> ...)` — the SAME stale
  positional+tuple shape, embedded in prose describing the CG v0.5 call. This is the combinator
  chapter's own evidence narration (not the krylov-step operator), so it is a separate
  single-operator scope. Flagging OQ
  `iterate-while-with-prev-evidence-prose-stale-cg-call-shape` so a follow-up dispatch refreshes
  that prose to the canonical form (it should read the boot/init/steady/cont shape, matching the
  refreshed krylov-step example and the synthesis rendering). NOT fixed here per the
  one-operator-per-invocation discipline.
