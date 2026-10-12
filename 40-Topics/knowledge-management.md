---
type: topic
title: Knowledge management
aliases: [km, personal knowledge management, pkm]
tags: [knowledge, wiki]
created: 2026-05-07
updated: 2026-10-12
paper_section: ["A"]
---

# Knowledge management

> How knowledge is captured, organized, refined, and re-used over time — and the failure modes (decay, orphaning, contradiction) that any system must defend against.

> [!abstract] 한눈에
> 사람이 관리하는 위키는 새 페이지마다 따라붙는 상호 참조 작업이 밀리면서 무너지고, LLM이 그 작업을 맡으면 지식 베이스가 소스가 늘 때마다 함께 자란다 ([[10-Summaries/example-llm-wiki|Karpathy (paraphrase)]]).

## Key points

- **Human-maintained wikis decay because maintenance cost grows faster than content value.** The marginal cross-referencing edits get deferred and abandoned ([[10-Summaries/example-llm-wiki|Karpathy (paraphrase)]]).
- **A compounding knowledge base updates existing content with each new input.** One new source triggers many edits across the graph, not a single summary file ([[10-Summaries/example-llm-wiki|Karpathy (paraphrase)]]).
- **Two flat files can replace embedding-based retrieval.** `index.md` (catalog) and `log.md` (chronological record) make the wiki navigable ([[10-Summaries/example-llm-wiki|Karpathy (paraphrase)]]).
- **The evidence is argumentative.** The source is a design proposal, not a measured result ([[10-Summaries/example-llm-wiki|Karpathy (paraphrase)]]).

## Start here

> [!cards]
> - `concept` [[30-Concepts/compounding-artifact|Compounding artifact]] — Knowledge bases whose value grows with each addition because new inputs trigger updates across existing content.
> - `concept` [[30-Concepts/maintenance-asymmetry|Maintenance asymmetry]] — The gap between human and LLM tolerance for cross-reference work; explains why human-maintained wikis decay.
> - `concept` [[30-Concepts/llm-wiki|LLM Wiki]] — One concrete approach: an LLM-maintained markdown vault.
> - `concept` [[30-Concepts/three-layer-architecture|Three-layer architecture]] — Sources / wiki / schema separation.
> - `concept` [[30-Concepts/ingest-workflow|Ingest workflow]] — The per-source procedure.

## Sources and people

- [[20-Entities/andrej-karpathy]] — proposed the LLM Wiki framing of knowledge management ([[10-Summaries/example-llm-wiki|Karpathy (paraphrase)]]).
- **LLM-maintained knowledge bases:** [[10-Summaries/example-llm-wiki|Karpathy (paraphrase)]] — paraphrase of Karpathy's LLM Wiki proposal.
- No synthesized notes yet.

## Open questions

- At what scale does flat-file + `index.md` navigation stop working? Where is the threshold for adding retrieval infrastructure?
- How do you measure whether a knowledge base is actually compounding, vs. just accumulating?
- What's the right policy for resolving contradictions between sources, beyond "flag and defer"?
- Schema evolution: how do you migrate a knowledge base when its conventions change?

## Related

> [!cards]
> - `hub` [[40-Topics/llm-tooling-patterns|LLM tooling patterns]] — Reusable design patterns for using LLMs as durable software components.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/example-llm-wiki|example-llm-wiki]]
