---
type: concept
title: LLM Wiki
aliases: [llm-maintained wiki, agentic wiki]
tags: [llm, knowledge-management, pattern]
created: 2026-05-07
updated: 2026-10-12
---

# LLM Wiki

> A pattern where an LLM incrementally builds and maintains a persistent, structured markdown knowledge base from raw sources, so answers compound across sessions instead of being re-derived ([[10-Summaries/example-llm-wiki|Karpathy]]).

> [!abstract] 한눈에
> LLM Wiki는 LLM이 원자료를 읽어 markdown 지식 베이스를 계속 고쳐 나가게 해서, 질문할 때마다 답을 처음부터 다시 만들지 않게 하는 방식이다 ([[10-Summaries/example-llm-wiki|Karpathy]]). 사람은 저자보다 큐레이터와 질문자 역할을 맡고, flat file만으로 규모가 커져도 탐색이 되는지는 아직 검증되지 않았다 ([[10-Summaries/example-llm-wiki|Karpathy]]).

## Definition

An LLM Wiki is a markdown vault organized into three layers — immutable raw sources, an LLM-maintained wiki, and a configuration document that fixes conventions — such that each new source triggers many cross-referenced edits across the wiki, not just a single summary file ([[10-Summaries/example-llm-wiki|Karpathy]]). The LLM acts as **maintainer**, not chatbot: reading sources, distilling them into pages (summaries, entities, concepts, topics, notes), and weaving them into an existing graph ([[10-Summaries/example-llm-wiki|Karpathy]]).

Two flat files anchor navigation without retrieval infrastructure: an `index.md` catalog and an append-only `log.md` ([[10-Summaries/example-llm-wiki|Karpathy]]).

## Why it matters

- It changes the economics of knowledge work: re-deriving answers from raw sources every query is wasteful when the same questions and connections recur ([[10-Summaries/example-llm-wiki|Karpathy]]).
- An LLM Wiki absorbs the per-source cross-reference cost, which humans defer indefinitely — see [[30-Concepts/maintenance-asymmetry]] ([[10-Summaries/example-llm-wiki|Karpathy]]).
- It exposes the human as **curator and questioner** rather than author and bookkeeper ([[10-Summaries/example-llm-wiki|Karpathy]]).
- The output is a [[30-Concepts/compounding-artifact]]: every ingest leaves the wiki measurably better (synthesis).

## Variants and refinements

- **Karpathy's framing** — three layers, flat markdown, no embeddings; navigation via `index.md` + `log.md` ([[10-Summaries/example-llm-wiki|Karpathy]]). The CLAUDE.md / AGENTS.md configuration document is part of the layer definition ([[10-Summaries/example-llm-wiki|Karpathy]]); see [[30-Concepts/three-layer-architecture]].
- The per-source procedure that drives compounding is the [[30-Concepts/ingest-workflow]].

## Evidence and examples

- This vault is itself an instance — see `CLAUDE.md` for the operating instructions and `index.md` for the live catalog.

## Contested points

- **Whether flat-file navigation scales.** The seed source asserts it suffices; this is untested at large source counts ([[10-Summaries/example-llm-wiki|Karpathy]]).
- **What "good" cross-referencing looks like.** The seed source gives "10–15 pages per ingest" as a heuristic but doesn't specify quality criteria ([[10-Summaries/example-llm-wiki|Karpathy]]). This vault's ingest workflow uses 5–15 instead, so the two ranges disagree at the low end (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/three-layer-architecture|Three-layer architecture]] — The structural skeleton of an LLM Wiki.
> - `concept` [[30-Concepts/compounding-artifact|Compounding artifact]] — What an LLM Wiki produces.
> - `concept` [[30-Concepts/maintenance-asymmetry|Maintenance asymmetry]] — The asymmetry that makes the pattern work.
> - `concept` [[30-Concepts/ingest-workflow|Ingest workflow]] — The procedure that drives compounding.
> - `entity` [[20-Entities/andrej-karpathy|Andrej Karpathy]] — Proposed the LLM Wiki pattern.
> - `hub` [[40-Topics/llm-tooling-patterns|LLM tooling patterns]] — LLMs as durable, stateful software components.
> - `hub` [[40-Topics/knowledge-management|Knowledge management]] — Capturing and re-using knowledge, and how such systems decay.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/example-llm-wiki|example-llm-wiki]]
