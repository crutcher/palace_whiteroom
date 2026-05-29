# convert-nested-fences-to-indented-code-in-proposed-changes-block

**Promoted:** cycle-024 meta-phase (batch-6). **Proposer:** repairer (cycle-023). **Friction-ledger:** `firm-chapter-body-authored-outside-proposed-changes-fence` (recurrence-2, nested-`text`-fence variant). **Companion (detection):** `proposed-changes-fence-encloses-full-body-guard` (critic-side; finds the defect, this skill fixes it).

**Audience:** repairer (the mechanical fix); also a producer self-check (the prevention is the producer-spec bullet "render inner code samples 4-space-indented, NOT nested fences").

## Motivating observation

A producer authors a firm chapter body inside a ` ```new:book/src/<...>.md ` (or ` ```edit:<...> `) proposed-changes block, but renders code/signature/sub-pattern samples as **nested ` ```text … ``` ` fenced blocks**. Under flat CommonMark fence-toggle parsing (how the integrator extracts the proposed-changes block), the **first bare inner ` ``` ` closes the outer `new:`/`edit:` block early** — stranding `## Status` and the entire firm apparatus OUTSIDE the captured content. The integrator then lands an intro-only stub while the dep-map row / `SUMMARY.md` already say `firm`. This is the same root defect as the cycle-019 "body authored as the report's own top-level sections outside the fence" case, in a different surface form (cycle-023 `lu-solve-mutation-rotation`).

The landed L1>L0 siblings (`book/src/L1-L0/dot-mutation-rotation.md`, `assemble-diagonal-mutation-rotation.md`) avoid this by rendering inner code as **4-space-indented code blocks**, which carry no fence delimiters and therefore cannot mis-toggle the outer block.

## Procedure (mechanical, surgical — preserve content byte-for-byte)

1. **Enumerate fences.** `grep -n '```' <report-CYCLE.md>`. If a `new:`/`edit:` proposed-changes block contains inner ` ```lang … ``` ` fences, the block will mis-toggle (the inner open/close are counted as outer toggles).
2. **Convert each nested fenced code block inside the proposed-changes block:** delete the opening ` ```lang ` line and the matching closing ` ``` ` line, and prefix **every** content line (including significant blank lines) with **4 spaces**. This is the CommonMark indented-code-block form the landed siblings use. Do this for every nested fence inside the block.
3. **Preserve all code content byte-for-byte.** Only the fence *mechanism* changes (fence-delimited → indent-delimited); not a single character of the code/signature text.
4. **Re-verify the toggle count.** `grep -c '```' <report>`: the count must equal exactly `2 × (number of proposed-changes blocks)`, all paired (one open + one close per block). Then confirm `## Status` (and the rest of the firm apparatus — Signature / Algebraic-laws / Evidence / any `verified_against:` block) now sit INSIDE the relevant block — i.e. the `## Status` header's line number is **less than** the block's closing-fence line number.
5. **Reference to copy the exact indent pattern from:** `book/src/L1-L0/dot-mutation-rotation.md`.

## Note on `verified_against:` YAML blocks

The lowering-verifier's `verified_against:` block is required to be a fenced ` ```yaml ` block (channel-format requirement, friction-ledger `lowering-verifier-yaml-in-prose-channel-format`) — but it lives in the **landed chapter file**, NOT necessarily nested inside a `new:`/`edit:` proposed-changes block. If a firm-flip proposal encloses a `verified_against:` block inside the proposed-changes fence, the same mis-toggle risk applies; in that case either (a) keep the `verified_against:` as the LAST thing in the block so its closing ` ``` ` coincides with the block's intended close, OR (b) render it 4-space-indented like other inner code. Prefer (b) for safety; the downstream `cross-layer-cross-cutter` parser keys on the `verified_against:` leading text, which survives either form.

## Failure mode this prevents

A `firm`-marked chapter shipping as an intro-only stub (no `## Status`, no laws, no Evidence) because the firm apparatus fell outside the apply boundary — a silent body-truncation masked by the dep-map/SUMMARY claiming firm.

## Cross-references

- `skills/proposed-changes-fence-encloses-full-body-guard/SKILL.md` — the critic-side detection guard (finds the defect at critique time).
- Friction-ledger `firm-chapter-body-authored-outside-proposed-changes-fence` — the pattern + both variants.
- Producer-spec bullet (harvester / abstractor / lifter / layer-intro-author / lowering-verifier §Discipline) — the prevention ("render inner code samples 4-space-indented, NOT nested fences").
