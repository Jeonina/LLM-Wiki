---
type: concept
title: Maintenance asymmetry (humans vs. LLMs)
aliases: [cross-reference asymmetry, the boredom asymmetry]
tags: [llm-wiki, knowledge-management]
created: 2026-05-07
updated: 2026-05-07
---

# Maintenance asymmetry (humans vs. LLMs)

> The observation that a wiki's bottleneck is not writing pages but performing the cross-reference edits *between* them — a task humans batch and abandon, but an LLM will do every time.

## Definition

Each new page in a wiki should ideally trigger updates to many existing pages: backlinks, refined definitions, new mentions, contradiction flags. Humans defer these edits because the marginal cost is high relative to the marginal value of any single edit, and over time the deferred work piles up until maintenance stops entirely. The marginal cost of maintenance grows faster than the marginal value of the content ([[10-Summaries/example-llm-wiki]]).

LLMs, in contrast, do not get bored. The same 10–15 cross-reference edits per ingest that exhaust a human are routine for an LLM, which is why the [[llm-wiki]] pattern works at all.

## Why it matters

This is the load-bearing observation behind the entire design. Without the asymmetry, an LLM Wiki is just a notes folder with autocomplete. With it, the LLM can sustain the maintenance discipline that produces a [[compounding-artifact]].

The asymmetry also reframes the human's role: from author and bookkeeper (the parts the LLM does better) to **curator and questioner** (judgement calls about what matters and what to ask).

## Variants and refinements

- **Karpathy's framing** ([[10-Summaries/example-llm-wiki]]) — names the human side ("humans defer, batch, eventually stop") and the LLM side ("LLMs do not get bored") as the explicit asymmetry.

## Contested points

- The seed source asserts the asymmetry but does not address LLM **failure modes** in maintenance — e.g., quietly contradicting itself across pages, drifting style, or hallucinating cross-references. These are real maintenance costs that move to the LLM side.

## Examples

- An ingest of a paper that mentions five entities should result in five entity-page updates *plus* concept refinements. The human version of this rule lasts until ingest #4; the LLM version lasts indefinitely.

## Related

- [[llm-wiki]]
- [[compounding-artifact]]
- [[ingest-workflow]]
- [[40-Topics/knowledge-management]]
