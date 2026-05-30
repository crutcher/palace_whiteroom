---
slug: verified-against-note-no-leading-quote-of-either-kind
promoted_at: cycle-030 meta-phase (batch-8) / 2026-05-30
promoted_from: scaffolding/skill-candidates.md (c030 repairer)
addresses_friction: verified-against-note-no-leading-quote-of-either-kind (recurrence-2 of the leading-quote channel-format hazard; generalizes the c028 leading-double-quote-only flag to leading-quote-of-either-kind)
status: promoted
---

# verified-against-note-no-leading-quote-of-either-kind

A producer- and critic- and repairer-facing channel-format skill for the `verified_against:` YAML block. Closes a `yaml.safe_load`-parse failure mode that recurred at cycle-030 in the single-quote variant, where the c028-codified rule "no `note:` value may begin with a literal DOUBLE quote" was too narrow — YAML's plain-scalar parser interprets a leading quote of EITHER kind (`'` or `"`) as opening a quoted scalar, and any trailing unquoted prose after the closing quote breaks the block.

## When to invoke

- **Producer (lowering-verifier, or any role emitting a `verified_against:` block):** before emitting the report, scan every `note:` value's first non-whitespace character.
- **Critic (citation-validity sub-check):** for any report carrying a proposed `verified_against:` block, extract the block and confirm it round-trips through `yaml.safe_load`.
- **Repairer:** when the critic flags `citation-validity: fail` with a YAML `ParserError: expected <block end>, but found '<scalar>'`, rephrase the affected `note:` values per the procedure below.

## Why

The channel-format rule for `verified_against:` `note:` values is: **no `note:` value may begin with a quote character of either kind (single `'` or double `"`)** — because YAML reads a leading quote as the start of a quoted scalar, then chokes on the trailing unquoted prose after the closing quote with `ParserError: expected <block end>, but found '<scalar>'` (verified on the cycle-030 D2 `bilinear-form-mutation-rotation` audit: full block fails `safe_load` at line 69 column 63 when two notes start with `'`).

The c028-codified rule named only the leading-DOUBLE-quote hazard. The cycle-030 D2 producer self-check explicitly claimed "no leading-double-quote note values (yaml.safe_load hazard avoided)" — exactly the narrower form — and the single-quote variant slipped past. This skill records the generalized rule so the producer self-check, the critic mechanical check, and the repairer fix all key on the same broadened predicate.

## Procedure

### Producer self-check (pre-emit)

1. For each `note:` value in the `verified_against:` block, scan its first non-whitespace character.
2. If it is `'` or `"`, rephrase the note to start with a non-quote character — embed the quoted term inside the body of the note, not at its start:
   - **Bad:** `note: 'The conjugation asymmetry...'; ...`
   - **Bad:** `note: "Why this is NOT a general trsv" ...`
   - **Good:** `note: section header "X" — the conjugation asymmetry; ...`
   - **Good:** `note: conjugation asymmetry header — the core theme content; the inherited reconciliation...`
3. Optionally, before shipping the report, run a mechanical round-trip check:

       python3 -c "import yaml; yaml.safe_load(open('<extracted-block>'))"

   A clean parse is the proof. A `ParserError` identifies the failing row by line + column.

### Critic check (citation-validity sub-step)

Extract the proposed `~~~yaml ... ~~~` (or ` ```yaml ... ``` `) block — or the 4-space-indented-code form destined for re-fencing at integration — and run:

    python3 -c "import yaml,sys; yaml.safe_load(open(sys.argv[1]))" <extracted-yaml-file>

If a `ParserError: expected <block end>, but found '<scalar>'` is raised:
- Flag `citation-validity: fail` with the ParserError's line + column.
- The defect is structural channel-format (not a citation-pointer defect, but it lives under `citation-validity` because the `verified_against:` block IS the citation surface).
- Identify which `note:` value's first non-whitespace character is `'` or `"`.

### Repairer fix

Mechanical: rephrase each affected `note:` value so the scalar begins with prose:

- **Pattern 1 (drop the leading quote, embed the quoted term):**
  `note: 'X — content; ...'` → `note: section header "X" — content; ...`
- **Pattern 2 (wrap the entire value in matching outer quotes, escaping inner ones):**
  `note: 'X — content with apostrophes'` → `note: "X — content with apostrophes"` (only if the value is short and inner double-quotes are escaped).

Pattern 1 is preferred — it converts the scalar to a plain (un-quoted) YAML string, which has no leading-character hazard and is the easiest to verify visually.

Preserve all other content byte-for-byte: keys, citation paths, verdicts, audited_at timestamps — only the affected `note:` value's prefix changes.

## Anti-patterns

- **Do not** flag a `note:` value as defective merely because it CONTAINS a `'` or `"` mid-string — the hazard is specifically a LEADING quote character. Mid-string quotes are safe in unquoted YAML plain scalars.
- **Do not** apply this rule to other YAML keys (citation paths, verdicts, etc.) — they have their own validity constraints (path-existence, enum membership); the leading-quote hazard is specifically a `note:`-value text-prose hazard because `note:` values are the only place where freeform prose carries adjacent quoted terms.
- **Do not** rely on a producer self-check that names only ONE of the two quote characters — the c028-narrower form is exactly what allowed the c030 recurrence. The check predicate is `note value's first non-whitespace character is in {`'`, `"`}`.

## Precedents

- **Cycle-028 D5 (incremental-ls-composition-lowering audit)**: leading-double-quote in two `note:` values; per-report integrator repaired by single-quote-wrapping (which works for double-quote-leading values, but does NOT generalize to single-quote-leading values).
- **Cycle-030 D2 (bilinear-form-mutation-rotation audit)**: leading-single-quote in two `note:` values; per-report integrator repaired by rephrasing each note to start with prose (Pattern 1 above).
- **Cycle-030 meta-phase (batch-8)**: codified the generalized rule in `.claude/agents/lowering-verifier.md` (producer-spec bullet) + `.claude/agents/critic.md` `citation-validity` (YAML round-trip sub-check) + this skill (deterministic repair).
