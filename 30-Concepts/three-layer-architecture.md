---
type: concept
title: Three-layer architecture (LLM Wiki)
aliases: [sources-wiki-schema, three layers]
tags: [llm-wiki, architecture]
created: 2026-05-07
updated: 2026-05-07
---

# Three-layer architecture (LLM Wiki)

> The structural skeleton of an [[llm-wiki]]: immutable **sources**, an LLM-maintained **wiki**, and a fixed **schema/configuration** document that specifies the conventions.

## Definition

The three layers separate concerns by mutability and ownership ([[10-Summaries/example-llm-wiki]]):

1. **Sources** — raw inputs (papers, articles, images, data). Read-only for the LLM. Truth lives here; if a source is wrong, that fact is recorded in a summary, not by editing the source.
2. **Wiki** — the LLM's output: per-source summaries, entity pages, concept pages, topic pages, synthesized notes. Mutable. This is where compounding happens.
3. **Schema / configuration** — a `CLAUDE.md` (Claude) or `AGENTS.md` (other tools) document that fixes folder layout, frontmatter, link conventions, and the workflows for ingest / query / maintain. Changes only on user request.

## Why it matters

The separation prevents the LLM from corrupting raw inputs (a category of error the human would have to detect after the fact) and gives ingestion a stable target shape. The configuration layer also makes the pattern **portable across LLMs** — point a different agent at the same vault and the same rules apply.

## Variants and refinements

- **Karpathy's formulation** ([[10-Summaries/example-llm-wiki]]) — names the configuration layer explicitly (`CLAUDE.md` / `AGENTS.md`) and treats it as part of the architecture rather than an implementation detail.

## Contested points

- The seed source does not address what happens when the schema layer itself needs to evolve mid-stream — e.g., adding a new page type after summaries already exist. Migration policy is undefined.

## Examples

- In this vault: `00-Sources/` (layer 1), `10-Summaries/` through `50-Notes/` (layer 2), `CLAUDE.md` plus `90-Meta/templates/` (layer 3).

## Related

- [[llm-wiki]]
- [[ingest-workflow]]
- [[40-Topics/llm-tooling-patterns]]
