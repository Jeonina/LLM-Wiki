---
type: concept
title: Three-layer architecture (LLM Wiki)
aliases: [sources-wiki-schema, three layers]
tags: [llm-wiki, architecture]
created: 2026-05-07
updated: 2026-10-12
---

# Three-layer architecture (LLM Wiki)

> The structural skeleton of an [[llm-wiki]]: immutable **sources**, an LLM-maintained **wiki**, and a fixed **schema/configuration** document that specifies the conventions ([[10-Summaries/example-llm-wiki|Karpathy]]).

> [!abstract] 한눈에
> LLM Wiki는 읽기만 하는 원자료(sources), LLM이 쓰고 고치는 wiki, 그리고 규칙을 정하는 schema 문서(`CLAUDE.md`/`AGENTS.md`)의 세 층으로 나뉜다 ([[10-Summaries/example-llm-wiki|Karpathy]]). schema 자체가 도중에 바뀔 때 기존 페이지를 어떻게 옮길지는 아직 정해져 있지 않다 ([[10-Summaries/example-llm-wiki|Karpathy]]).

## Definition

The three layers separate concerns by mutability and ownership ([[10-Summaries/example-llm-wiki|Karpathy]]).

## Why it matters

- The separation prevents the LLM from corrupting raw inputs, a category of error the human would have to detect after the fact (synthesis).
- It gives ingestion a stable target shape (synthesis).
- The configuration layer makes the pattern **portable across LLMs**: point a different agent at the same vault and the same rules apply (synthesis).

## The three layers

| Layer | Contents | Mutability | In this vault | Source |
|---|---|---|---|---|
| 1. Sources | Raw inputs (papers, articles, images, data). Truth lives here; if a source is wrong, that fact is recorded in a summary, not by editing the source | Read-only for the LLM | `00-Sources/` | ([[10-Summaries/example-llm-wiki\|Karpathy]]) |
| 2. Wiki | The LLM's output: per-source summaries, entity pages, concept pages, topic pages, synthesized notes. This is where compounding happens | Mutable | `10-Summaries/` through `50-Notes/` | ([[10-Summaries/example-llm-wiki\|Karpathy]]) |
| 3. Schema / configuration | A `CLAUDE.md` (Claude) or `AGENTS.md` (other tools) document that fixes folder layout, frontmatter, link conventions, and the workflows for ingest / query / maintain | Changes only on user request | `CLAUDE.md` plus `90-Meta/templates/` | ([[10-Summaries/example-llm-wiki\|Karpathy]]) |

## Evidence and examples

- **Karpathy's formulation** names the configuration layer explicitly (`CLAUDE.md` / `AGENTS.md`) and treats it as part of the architecture rather than an implementation detail ([[10-Summaries/example-llm-wiki|Karpathy]]).
- In this vault: `00-Sources/` (layer 1), `10-Summaries/` through `50-Notes/` (layer 2), `CLAUDE.md` plus `90-Meta/templates/` (layer 3) (synthesis).

## Contested points

- The seed source does not address what happens when the schema layer itself needs to evolve mid-stream — e.g., adding a new page type after summaries already exist. Migration policy is undefined ([[10-Summaries/example-llm-wiki|Karpathy]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/llm-wiki|LLM Wiki]] — An LLM incrementally builds and maintains a persistent markdown knowledge base from raw sources.
> - `concept` [[30-Concepts/ingest-workflow|Ingest workflow]] — The per-source procedure: read, summarize, propagate across the graph, update index, log.
> - `hub` [[40-Topics/llm-tooling-patterns|LLM tooling patterns]] — Design patterns for using LLMs as durable, convention-following software components.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/example-llm-wiki|example-llm-wiki]]
