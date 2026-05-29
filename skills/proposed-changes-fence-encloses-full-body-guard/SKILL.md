# Skill: proposed-changes-fence-encloses-full-body-guard

**Audience**: `critic` (primary, build-readiness guard in the `cross-reference-integrity` check). Also a producer self-check for the 8 specialized agents that author firm chapters.

**Purpose**: catch the cycle-019 fence-truncation defect at critique time — a producer authors a fully-vetted, well-cited FIRM chapter body but leaves only the intro INSIDE the `edit:`/`new:` proposed-changes fenced block (the body authored as the report's OWN top-level sections, outside the fence), so the integrator lands only the enclosed intro while the dep-map/SUMMARY say `firm`. A silent body-truncation masked by the firm claim. Friction-ledger `firm-chapter-body-authored-outside-proposed-changes-fence`.

## When to invoke

- A report carries an `` ```edit:<path> `` or `` ```new:<path> `` proposed-changes block that purports to land a *full chapter* (a stub→firm or rough-in→firm promotion, or a fresh firm chapter).
- The report (or the dep-map / SUMMARY edit it relies on) asserts the chapter is `firm`.
- Especially when the report's prose carries substantial chapter-shaped sections (`## Context` … `## Evidence`) — confirm they are INSIDE the fence, not the report's own top-level sections.

## Procedure

1. **Enumerate the fence lines.** `grep -n '```' <report>/CYCLE.md`. Confirm:
   - Even parity (every opening fence has a closing fence).
   - Nested code fences inside a proposed-changes block (e.g. ` ```text ` shape blocks, ` ```yaml ` verified-against blocks) are balanced — a stray inner fence that closes the outer block early is the exact mechanism by which the body falls outside.

2. **Identify the proposed-changes block boundaries.** For each `` ```edit:<path> ``/`` ```new:<path> `` opening fence, find its matching closing ``` ``` ``` (accounting for balanced nested fences). The content BETWEEN them is what the integrator applies; everything outside is report prose that is NOT applied.

3. **Locate the LAST chapter section the report intends to land.** Typically `## Evidence` (or `## Status` if it is last). Confirm the block-closing fence sits on a line AFTER it — not before `## Context`.

4. **Cross-check the maturity claim (the load-bearing check).** If the report (or its dep-map/SUMMARY edit) asserts `firm`, the enclosed block MUST contain the firm apparatus INSIDE the fence:
   - `## Status` section,
   - Signature,
   - Algebraic-laws (or the theme's rewrite-rules),
   - Evidence.
   A `firm` claim whose proposed-changes block carries only an intro (apparatus present only in the report's surrounding prose) is the defect. Flag `fail`.

5. **For a backfill / full-file-replacement, confirm the WHOLE body is enclosed.** A `firm` stub→firm promotion that replaces the file must enclose every section the chapter should carry; spot-check that the closing fence is after the last intended section.

## Failure modes (what this catches)

- **Body-outside-fence (the primary defect):** `## Context`…`## Evidence` authored as the report's top-level sections; only the intro inside the `edit:` fence. Symptom on disk: an intro-only chapter with no `## Status` while dep-map/SUMMARY say firm. Recovery (integrator/repairer): full-file-replacement backfill enclosing the complete body.
- **Early-closing nested fence:** an inner ` ```text `/` ```yaml ` block whose close is read as the outer block's close, truncating everything after it. Symptom: partial body lands. Recovery: balance the nested fences; re-enclose.
- **Firm-claim / apparatus mismatch:** the dep-map/SUMMARY row flips to `firm` but the enclosed body lacks `## Status` + Signature + laws + Evidence. This is the downstream half of the same defect (the layer-intro-author surveys firmness from the cycle record, not the on-disk status) — guarding the upstream fence-enclosure here prevents it.

## Discipline

- **The check is mechanical** — fence-enumeration + parity + "is `## Status` inside the block?" scan. It is not a content judgment; it is a build-readiness judgment (will the firm body actually enter the artifact?).
- **It complements, not replaces, the citation/claim checks.** The cycle-019 critic validated the citations (correct) but missed that the body never entered the artifact. This guard catches the orthogonal failure: well-formed, well-cited content that is partially outside the apply boundary.
- **Producer self-check version:** before emitting, the authoring agent confirms its full firm body sits inside the `edit:`/`new:` fence — do NOT author chapter sections as the report's own top-level sections; only the enclosed block is applied.

## Cross-references

- Friction-ledger `firm-chapter-body-authored-outside-proposed-changes-fence` (cycle-019 root instance, surfaced cycle-020, addressed cycle-021 meta-phase).
- Critic `cross-reference-integrity` check (this guard is folded into it).
- Sibling candidate `verify-intro-firmness-survey-against-on-disk-status-lines` (the downstream symptom — folded into layer-intro-author Discipline rather than a standalone skill; this skill guards the upstream cause).
- OQ `firm-chapter-body-authored-outside-proposed-changes-fenced-block`.

## Provenance

- Promoted: cycle-021 meta-phase (batch-5, 2026-05-29).
- Pattern observed: 1 root instance (cycle-019 `orthogonalize` L2 harvest), surfaced via the cycle-020 backfill. The dispatch-prompt guidance held clean cycle-020/021 (zero recurrence) — promoted as the durable critic-side guard so the fix is structural, not per-dispatch-reminder-dependent.
- Proposer: critic (cycle-020, critique of `2026-05-29T034441Z-harvester-orthogonalize-l2-backfill`).
