---
type: concept
title: Compounding artifact
aliases: [compounding knowledge base]
tags: [llm-wiki, knowledge-management]
created: 2026-05-07
updated: 2026-05-07
---

# Compounding artifact

> A knowledge object whose value grows with each addition because new inputs trigger updates across existing content, not just appended pages.

## Definition

A compounding artifact is a knowledge base in which ingesting a new source produces **two** kinds of value: the new summary itself, *and* a wave of refinements to existing entity, concept, and topic pages it touches ([[10-Summaries/example-llm-wiki]]). The framing is deliberately contrasted with **one-shot retrieval**, where each query re-derives an answer from raw sources and leaves no residue.

The mechanism that makes compounding work is the per-ingest cross-reference pass — see [[ingest-workflow]] and [[maintenance-asymmetry]].

## Why it matters

It reframes what the wiki is *for*. The goal isn't to store sources; it's to produce a graph whose connectivity grows superlinearly with the source count. A single isolated summary is not yet wiki content — it becomes wiki content when the rest of the graph reflects it.

This is also the criterion by which to judge an ingest: did it leave the wiki measurably better, or did it just add a file?

## Variants and refinements

- **Karpathy's framing** ([[10-Summaries/example-llm-wiki]]) — explicitly contrasts compounding with re-derivation from raw sources every time.

## Contested points

- The seed source asserts compounding without quantifying it. There is no proposed metric for "is this wiki actually compounding?" beyond the heuristic of touching 10–15 pages per ingest.

## Examples

- A new source on retrieval-augmented generation should not just produce a summary; it should update the [[llm-wiki]] concept page (with how RAG relates), update any topic on retrieval, and add a "see also" from the prior LLM Wiki summary.

## Related

- [[llm-wiki]]
- [[maintenance-asymmetry]]
- [[ingest-workflow]]
- [[40-Topics/knowledge-management]]
