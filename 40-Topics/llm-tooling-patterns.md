---
type: topic
title: LLM tooling patterns
aliases: [agentic patterns, llm patterns]
tags: [llm, patterns]
created: 2026-05-07
updated: 2026-05-07
---

# LLM tooling patterns

> Reusable design patterns for using LLMs as durable software components — not as one-shot responders, but as agents that maintain state, follow conventions, and produce artifacts that outlive a conversation.

## Core concepts

- [[30-Concepts/llm-wiki]] — pattern for LLM-as-maintainer of a markdown knowledge base.
- [[30-Concepts/three-layer-architecture]] — sources / wiki / schema separation that makes the LLM Wiki portable.
- [[30-Concepts/ingest-workflow]] — the per-source procedure that drives compounding.
- [[30-Concepts/maintenance-asymmetry]] — the asymmetry between human and LLM maintenance costs that makes these patterns viable.

## Key entities

- [[20-Entities/andrej-karpathy]] — proposed the LLM Wiki pattern.

## Sources, by sub-theme

### LLM-as-maintainer

- [[10-Summaries/example-llm-wiki]] — paraphrase of Karpathy's LLM Wiki proposal.

## Synthesized notes

_None yet — promote one once ≥3 sources connect across this topic._

## Open questions

- How do these patterns compose? Is "LLM Wiki" a building block for larger LLM-as-knowledge-worker systems, or is it terminal?
- What does **observability** look like for an LLM-maintained artifact? How does the user know the LLM is doing the propagation step honestly?
- Are there patterns where the LLM should *not* be the maintainer — e.g., where ground truth must be human-asserted?
