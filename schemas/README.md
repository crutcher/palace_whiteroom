# Schemas

JSON Schemas (draft-07) for the typed outputs the per-cycle and meta-cycle agents produce. Built in Phase 3 of `BOOTSTRAP.md`.

| Schema | Producer | Purpose |
|---|---|---|
| [`exploration_finding.json`](exploration_finding.json) | Explorer (per-cycle) | L0 citations + L1 dataflow/mutation claims for one slice scope |
| [`rotation_claim.json`](rotation_claim.json) | Synthesizer (per-cycle) | A single per-edge `Li → Li+1` rotation claim with substantive justification |
| [`critic_verdict.json`](critic_verdict.json) | Critic (per-cycle) | pass / revise / reject verdict with per-claim issues and optional cross-cycle lesson |
| [`refinement_plan.json`](refinement_plan.json) | Meta-Critic (meta-cycle) | Cascade-categorized friction + LOW direct actions + MEDIUM plan items + HIGH escalations |

Each schema has a hand-crafted positive example under `examples/<name>.example.json`. The example pairs serve two purposes:

- **Phase 3 DONE check** — every schema validates a positive example via any draft-07 validator. The inline Python `jsonschema` invocation used at commit time is:

  ```bash
  python3 -c "
  import json
  from jsonschema import Draft7Validator, FormatChecker
  for s, x in [
      ('schemas/exploration_finding.json', 'schemas/examples/exploration_finding.example.json'),
      ('schemas/rotation_claim.json',      'schemas/examples/rotation_claim.example.json'),
      ('schemas/critic_verdict.json',      'schemas/examples/critic_verdict.example.json'),
      ('schemas/refinement_plan.json',     'schemas/examples/refinement_plan.example.json'),
  ]:
      schema = json.load(open(s)); example = json.load(open(x))
      Draft7Validator.check_schema(schema)
      errors = list(Draft7Validator(schema, format_checker=FormatChecker()).iter_errors(example))
      print('OK ' if not errors else 'FAIL', s)
      for e in errors: print('  -', list(e.absolute_path), e.message)
  "
  ```

- **Agent prompt-time reference** — the role prompts (`prompts/<role>.md`, Phase 4) tell agents to emit JSON validating against the corresponding schema. The example shows what good output looks like in concrete terms; agents see both the schema and the example.

## Discipline

- **No `additionalProperties: false`.** Schemas are permissive — agents may attach extra metadata (e.g., `cycle_id`, timing info) without schema violations. The contract is "must include these fields with these types"; what additional fields exist is the orchestrator's concern.
- **Required fields are minimal but load-bearing.** Each schema's `required` list is what the role's contract guarantees. Optional fields exist for substantive content the role may or may not produce on a given cycle (e.g., `push_back_proposal`, `lesson`).
- **`enum` constraints** pin the role's vocabulary. Extending an enum is a Medium-cascade change (Meta-Critic plan item), not a unilateral agent decision.

## Examples are illustrative, not normative

The example JSON files describe one *plausible* output for a CG-scoped slice exploration / rotation / verdict / meta-review. They're not exhaustive coverage of the schema and they're not "correct" in any deep sense — they're shape demonstrations. If the schema and an example disagree on intent, the schema wins.
