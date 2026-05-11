---
type: concept
title: LLM Wiki
aliases: [llm-maintained wiki, agentic wiki]
tags: [llm, knowledge-management, pattern]
created: 2026-05-07
updated: 2026-05-07
---

# LLM Wiki

> A pattern where an LLM incrementally builds and maintains a persistent, structured markdown knowledge base from raw sources, so answers compound across sessions instead of being re-derived.

## Definition

An LLM Wiki is a markdown vault organized into three layers — immutable raw sources, an LLM-maintained wiki, and a configuration document that fixes conventions — such that each new source triggers many cross-referenced edits across the wiki, not just a single summary file ([[10-Summaries/example-llm-wiki]]). The LLM acts as **maintainer**, not chatbot: reading sources, distilling them into pages (summaries, entities, concepts, topics, notes), and weaving them into an existing graph.

Two flat files anchor navigation without retrieval infrastructure: an `index.md` catalog and an append-only `log.md` ([[10-Summaries/example-llm-wiki]]).

## Why it matters

It changes the economics of knowledge work. Re-deriving answers from raw sources every query is wasteful when the same questions and connections recur. An LLM Wiki absorbs the per-source cross-reference cost (which humans defer indefinitely — see [[30-Concepts/maintenance-asymmetry]]) and exposes the human as **curator and questioner** rather than author and bookkeeper. The output is a [[30-Concepts/compounding-artifact]]: every ingest leaves the wiki measurably better.

## Variants and refinements

- **Karpathy's framing** ([[10-Summaries/example-llm-wiki]]) — three layers, flat markdown, no embeddings; navigation via `index.md` + `log.md`. The CLAUDE.md / AGENTS.md configuration document is part of the layer definition.

## Contested points

- Whether flat-file navigation scales. The seed source asserts it suffices; this is untested at large source counts.
- What "good" cross-referencing looks like. The seed source gives "10–15 pages per ingest" as a heuristic but doesn't specify quality criteria.

## Examples

- This vault is itself an instance — see `CLAUDE.md` for the operating instructions and `index.md` for the live catalog.

## Related

- [[30-Concepts/three-layer-architecture]] — the structural skeleton of an LLM Wiki.
- [[30-Concepts/compounding-artifact]] — what an LLM Wiki produces.
- [[30-Concepts/maintenance-asymmetry]] — the asymmetry that makes the pattern work.
- [[30-Concepts/ingest-workflow]] — the procedure that drives compounding.
- [[40-Topics/llm-tooling-patterns]]
- [[40-Topics/knowledge-management]]
- [[20-Entities/andrej-karpathy]]
