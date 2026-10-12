---
type: topic
title: LLM tooling patterns
aliases: [agentic patterns, llm patterns]
tags: [llm, patterns]
created: 2026-05-07
updated: 2026-10-12
paper_section: ["A"]
---

# LLM tooling patterns

> Reusable design patterns for using LLMs as durable software components — not as one-shot responders, but as agents that maintain state, follow conventions, and produce artifacts that outlive a conversation.

> [!abstract] 한눈에
> LLM Wiki 패턴에서 LLM은 매번 원자료에서 답을 다시 만들지 않고, 소스·위키·스키마 세 층으로 나뉜 markdown 위키를 꾸준히 고쳐 나가는 관리자 역할을 맡는다 ([[10-Summaries/example-llm-wiki|Karpathy (paraphrase)]]). 사람은 저자가 아니라 큐레이터이자 질문자가 된다 ([[10-Summaries/example-llm-wiki|Karpathy (paraphrase)]]).

## Key points

- **The LLM builds a persistent wiki instead of re-deriving answers from raw sources.** It incrementally maintains structured markdown that compounds with each new source ([[10-Summaries/example-llm-wiki|Karpathy (paraphrase)]]).
- **Three layers keep the pattern portable.** Immutable raw sources, the LLM-maintained wiki, and a configuration document (`CLAUDE.md` / `AGENTS.md`) that fixes conventions ([[10-Summaries/example-llm-wiki|Karpathy (paraphrase)]]).
- **The per-source ingest procedure drives compounding.** Read → summarize → propagate → log ([[10-Summaries/example-llm-wiki|Karpathy (paraphrase)]]).
- **The human's role shifts from author to curator.** ([[10-Summaries/example-llm-wiki|Karpathy (paraphrase)]]).

## Start here

> [!cards]
> - `concept` [[30-Concepts/llm-wiki|LLM Wiki]] — Pattern for LLM-as-maintainer of a markdown knowledge base.
> - `concept` [[30-Concepts/three-layer-architecture|Three-layer architecture]] — Sources / wiki / schema separation that makes the LLM Wiki portable.
> - `concept` [[30-Concepts/ingest-workflow|Ingest workflow]] — The per-source procedure that drives compounding.
> - `concept` [[30-Concepts/maintenance-asymmetry|Maintenance asymmetry]] — The asymmetry between human and LLM maintenance costs that makes these patterns viable.

## Sources and people

- [[20-Entities/andrej-karpathy]] — proposed the LLM Wiki pattern ([[10-Summaries/example-llm-wiki|Karpathy (paraphrase)]]).
- **LLM-as-maintainer:** [[10-Summaries/example-llm-wiki|Karpathy (paraphrase)]] — paraphrase of Karpathy's LLM Wiki proposal.
- No synthesized notes yet — promote one once ≥3 sources connect across this topic.

## Open questions

- How do these patterns compose? Is "LLM Wiki" a building block for larger LLM-as-knowledge-worker systems, or is it terminal?
- What does **observability** look like for an LLM-maintained artifact? How does the user know the LLM is doing the propagation step honestly?
- Are there patterns where the LLM should *not* be the maintainer — e.g., where ground truth must be human-asserted?

## Related

> [!cards]
> - `hub` [[40-Topics/knowledge-management|Knowledge management]] — How knowledge is captured, organized, refined, and re-used over time.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/example-llm-wiki|example-llm-wiki]]
