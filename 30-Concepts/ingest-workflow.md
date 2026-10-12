---
type: concept
title: Ingest workflow
aliases: [ingest, ingestion]
tags: [llm-wiki, workflow]
created: 2026-05-07
updated: 2026-10-12
---

# Ingest workflow

> The per-source procedure that drives compounding in an [[llm-wiki]]: read → summarize → propagate across the graph → update index → log ([[10-Summaries/example-llm-wiki|Karpathy]]).

> [!abstract] 한눈에
> Ingest는 새 source를 읽고 요약한 뒤, 그 내용을 기존 entity·concept·topic 페이지에 퍼뜨리고 index와 log를 갱신하는 절차다 ([[10-Summaries/example-llm-wiki|Karpathy]]). 요약만 쌓는 것과 달리 이 전파 단계가 있어야 wiki가 누적된다 ([[10-Summaries/example-llm-wiki|Karpathy]]).

## Definition

When a new source arrives, the LLM follows these steps in this vault:

1. Discovers pending sources (this vault uses `tools/pending-sources.sh`).
2. Reads each source in full.
3. Writes a per-source summary in `10-Summaries/` from the summary template.
4. **Propagates** — touches existing entity, concept, and topic pages that the source mentions, refines, or contradicts. Creates new pages where the entity/concept/topic does not yet exist. Adds dated mention bullets, refined definitions, contradiction flags. Heuristic: 5–15 cross-reference edits per ingest.
5. Updates `index.md` to list any new pages.
6. Appends an entry to `log.md`.
7. Reports back: what was ingested, what was created, what was touched, what tensions surfaced.

Step 4 is what makes this workflow distinct from "summarize and file" — see [[compounding-artifact]] and [[maintenance-asymmetry]] for why it is non-negotiable ([[10-Summaries/example-llm-wiki|Karpathy]]).

## Why it matters

Without the propagation step, ingestion produces orphaned summaries and the wiki does not compound (synthesis). The workflow encodes the discipline the LLM must follow even when no single edit feels load-bearing — because the cumulative effect across many ingests is what makes the wiki valuable (synthesis).

## Variants and refinements

- **This vault's `CLAUDE.md`** specifies the steps in detail, including the contradiction-handling rule: don't silently overwrite — flag in `## Open questions` or note the change in the log.
- **Karpathy's framing** gives the workflow at the level of "read → write summary → propagate → log" without prescribing exact step counts ([[10-Summaries/example-llm-wiki|Karpathy]]).
## Evidence and examples

- The 2026-05-07 first ingest in this vault: 1 source → 1 summary, 1 entity, 5 concepts, 2 topics, plus index and log updates.

## Contested points

- The "5–15 pages per ingest" heuristic is just that — a heuristic. The seed source does not justify the range ([[10-Summaries/example-llm-wiki|Karpathy]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/llm-wiki|LLM wiki]] — A persistent wiki an LLM maintains from sources, which ingest feeds.
> - `concept` [[30-Concepts/three-layer-architecture|Three-layer architecture]] — Sources, wiki and schema as separate layers.
> - `concept` [[30-Concepts/compounding-artifact|Compounding artifact]] — Why each ingest should leave the wiki better than before.
> - `concept` [[30-Concepts/maintenance-asymmetry|Maintenance asymmetry]] — Cross-referencing is tedious for people and cheap for an LLM.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/example-llm-wiki|example-llm-wiki]]
