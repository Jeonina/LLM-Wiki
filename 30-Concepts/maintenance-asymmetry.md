---
type: concept
title: Maintenance asymmetry (humans vs. LLMs)
aliases: [cross-reference asymmetry, the boredom asymmetry]
tags: [llm-wiki, knowledge-management]
created: 2026-05-07
updated: 2026-10-12
---

# Maintenance asymmetry (humans vs. LLMs)

> The observation that a wiki's bottleneck is not writing pages but performing the cross-reference edits *between* them — a task humans batch and abandon, but an LLM will do every time ([[10-Summaries/example-llm-wiki|LLM Wiki seed]]).

> [!abstract] 한눈에
> 위키 유지의 병목은 페이지 작성이 아니라 페이지 사이의 교차 참조 편집이다. 사람은 이 일을 미루다 결국 그만두지만 LLM은 지루해하지 않고 매번 해낸다 ([[10-Summaries/example-llm-wiki|LLM Wiki seed]]).

## Definition

Each new page in a wiki should ideally trigger updates to many existing pages: backlinks, refined definitions, new mentions, contradiction flags ([[10-Summaries/example-llm-wiki|LLM Wiki seed]]). Humans defer these edits because the marginal cost is high relative to the marginal value of any single edit, and over time the deferred work piles up until maintenance stops entirely. The marginal cost of maintenance grows faster than the marginal value of the content ([[10-Summaries/example-llm-wiki|LLM Wiki seed]]).

LLMs, in contrast, do not get bored ([[10-Summaries/example-llm-wiki|LLM Wiki seed]]). The same 10–15 cross-reference edits per ingest that exhaust a human are routine for an LLM, which is why the [[llm-wiki]] pattern works at all ([[10-Summaries/example-llm-wiki|LLM Wiki seed]]).

## Why it matters

- **It is the load-bearing observation behind the design.** Without the asymmetry, an LLM Wiki is just a notes folder with autocomplete; with it, the LLM can sustain the maintenance discipline that produces a [[compounding-artifact]] ([[10-Summaries/example-llm-wiki|LLM Wiki seed]]).
- **It reframes the human's role.** The human moves from author and bookkeeper (the parts the LLM does better) to **curator and questioner** (judgement calls about what matters and what to ask) ([[10-Summaries/example-llm-wiki|LLM Wiki seed]]).

## Variants and refinements

- **Karpathy's framing** — names the human side ("humans defer, batch, eventually stop") and the LLM side ("LLMs do not get bored") as the explicit asymmetry ([[10-Summaries/example-llm-wiki|LLM Wiki seed]]).

## Evidence and examples

- The seed source is argumentative, not a measured study ([[10-Summaries/example-llm-wiki|LLM Wiki seed]]).
- An ingest of a paper that mentions five entities should result in five entity-page updates *plus* concept refinements; the human version of this rule lasts until ingest #4, the LLM version indefinitely (synthesis).

## Contested points

- The seed source asserts the asymmetry but does not address LLM **failure modes** in maintenance — e.g., quietly contradicting itself across pages, drifting style, or hallucinating cross-references. These are real maintenance costs that move to the LLM side (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/llm-wiki|LLM Wiki]] — An LLM incrementally builds and maintains a persistent markdown knowledge base from raw sources.
> - `concept` [[30-Concepts/compounding-artifact|Compounding artifact]] — A knowledge object whose value grows because new inputs update existing content.
> - `concept` [[30-Concepts/ingest-workflow|Ingest workflow]] — The per-source procedure: read, summarize, propagate, index, log.
> - `hub` [[40-Topics/knowledge-management|Knowledge management]] — How knowledge is captured, refined and re-used, and how such systems decay.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/example-llm-wiki|example-llm-wiki]]
