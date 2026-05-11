---
type: topic
title: Knowledge management
aliases: [km, personal knowledge management, pkm]
tags: [knowledge, wiki]
created: 2026-05-07
updated: 2026-05-07
---

# Knowledge management

> How knowledge is captured, organized, refined, and re-used over time — and the failure modes (decay, orphaning, contradiction) that any system must defend against.

## Core concepts

- [[30-Concepts/compounding-artifact]] — knowledge bases whose value grows with each addition because new inputs trigger updates across existing content.
- [[30-Concepts/maintenance-asymmetry]] — the gap between human and LLM tolerance for cross-reference work; explains why human-maintained wikis decay.
- [[30-Concepts/llm-wiki]] — one concrete approach: an LLM-maintained markdown vault.

## Key entities

- [[20-Entities/andrej-karpathy]] — proposed the LLM Wiki framing of knowledge management.

## Sources, by sub-theme

### LLM-maintained knowledge bases

- [[10-Summaries/example-llm-wiki]] — paraphrase of Karpathy's LLM Wiki proposal.

## Synthesized notes

_None yet._

## Open questions

- At what scale does flat-file + `index.md` navigation stop working? Where is the threshold for adding retrieval infrastructure?
- How do you measure whether a knowledge base is actually compounding, vs. just accumulating?
- What's the right policy for resolving contradictions between sources, beyond "flag and defer"?
- Schema evolution: how do you migrate a knowledge base when its conventions change?
