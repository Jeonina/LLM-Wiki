---
type: concept
title: Compounding artifact
aliases: [compounding knowledge base]
tags: [llm-wiki, knowledge-management]
created: 2026-05-07
updated: 2026-10-12
---

# Compounding artifact

> A knowledge object whose value grows with each addition because new inputs trigger updates across existing content, not just appended pages ([[10-Summaries/example-llm-wiki|LLM Wiki seed]]).

> [!abstract] 한눈에
> Compounding artifact는 새 source를 넣을 때마다 요약 한 장만 늘어나는 것이 아니라 기존 entity·concept·topic 페이지까지 함께 고쳐지는 지식 베이스다 ([[10-Summaries/example-llm-wiki|LLM Wiki seed]]). 다만 이 효과가 실제로 쌓이고 있는지를 재는 지표는 아직 없다 ([[10-Summaries/example-llm-wiki|LLM Wiki seed]]).

## Definition

A compounding artifact is a knowledge base in which ingesting a new source produces **two** kinds of value: the new summary itself, *and* a wave of refinements to existing entity, concept, and topic pages it touches ([[10-Summaries/example-llm-wiki|LLM Wiki seed]]). The framing is deliberately contrasted with **one-shot retrieval**, where each query re-derives an answer from raw sources and leaves no residue ([[10-Summaries/example-llm-wiki|LLM Wiki seed]]).

The mechanism that makes compounding work is the per-ingest cross-reference pass — see [[ingest-workflow]] and [[maintenance-asymmetry]] (synthesis).

## Why it matters

It reframes what the wiki is *for*. The goal isn't to store sources; it's to produce a graph whose connectivity grows superlinearly with the source count (synthesis). A single isolated summary is not yet wiki content — it becomes wiki content when the rest of the graph reflects it (synthesis).

This is also the criterion by which to judge an ingest: did it leave the wiki measurably better, or did it just add a file? (synthesis)

## Variants and refinements

- **Karpathy's framing** — explicitly contrasts compounding with re-derivation from raw sources every time ([[10-Summaries/example-llm-wiki|LLM Wiki seed]]).

## Evidence and examples

**In the wiki**

- A new source on retrieval-augmented generation should not just produce a summary; it should update the [[llm-wiki]] concept page (with how RAG relates), update any topic on retrieval, and add a "see also" from the prior LLM Wiki summary (synthesis).

**Amplification artifacts that compound into published rates**

- MDA artifacts inflated the published neuronal SNV accumulation rate: SCAN2 on MDA neurons gave 31 sSNVs/year, falling to ~19–22 after removing artifact signature B, versus 16.5 with PTA ([[10-Summaries/luquette-2022-neuron-scan2-indels|Luquette 2022]]).
- LiRA's fitted error decay (p = 1/2) points to lesions on the original DNA before amplification as a dominant artifact source ([[10-Summaries/bohrson-2019-lira|LiRA]]).

## Contested points

- The seed source asserts compounding without quantifying it. There is no proposed metric for "is this wiki actually compounding?" beyond the heuristic of touching 10–15 pages per ingest ([[10-Summaries/example-llm-wiki|LLM Wiki seed]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/llm-wiki|LLM Wiki]] — The persistent, LLM-maintained wiki pattern this concept describes.
> - `concept` [[30-Concepts/maintenance-asymmetry|Maintenance asymmetry]] — Why cross-referencing is cheap for an LLM and tedious for people.
> - `concept` [[30-Concepts/ingest-workflow|Ingest workflow]] — The per-source pass that spreads updates across the graph.
> - `hub` [[40-Topics/knowledge-management|Knowledge management]] — How this wiki is built and maintained.

## All sources on this page

> [!info]- 3 summaries cited here
> - [[10-Summaries/bohrson-2019-lira|Bohrson 2019]]
> - [[10-Summaries/example-llm-wiki|example-llm-wiki]]
> - [[10-Summaries/luquette-2022-neuron-scan2-indels|Luquette 2022]]
