---
type: summary
title: "Example seed: paraphrase of Karpathy's LLM Wiki idea"
source: "[[00-Sources/articles/example-llm-wiki]]"
source_quality: full
source_sha256: "48bab45475273cb46837f78a087f917b9b43efbc9c318b21935a093239a96a7d"
source_kind: article
author: Unknown (paraphrase of Andrej Karpathy)
published: 2026
ingested: 2026-05-07
tags: [seed, llm-wiki, knowledge-management]
entities: ["[[20-Entities/andrej-karpathy]]"]
concepts:
  - "[[30-Concepts/llm-wiki]]"
  - "[[30-Concepts/three-layer-architecture]]"
  - "[[30-Concepts/compounding-artifact]]"
  - "[[30-Concepts/maintenance-asymmetry]]"
  - "[[30-Concepts/ingest-workflow]]"
topics:
  - "[[40-Topics/knowledge-management]]"
  - "[[40-Topics/llm-tooling-patterns]]"
---

**Citation:** Karpathy) et al. (2026) — *Example seed: paraphrase of Karpathy's LLM Wiki idea* — *?*.

# Example seed: paraphrase of Karpathy's LLM Wiki idea

> Thesis: an LLM should not re-derive answers from raw sources every time — it should incrementally build a persistent, structured wiki in markdown that compounds with each new source, with the human acting as curator and questioner rather than author and bookkeeper.

> [!abstract] 한눈에
> Karpathy의 LLM Wiki 아이디어를 풀어 쓴 글로, LLM이 원자료에서 매번 답을 다시 도출하지 말고 새 출처가 들어올 때마다 쌓여 가는 markdown 위키를 유지해야 한다고 주장한다. 사람이 위키를 버리는 이유는 글쓰기가 아니라 교차 참조 유지의 번거로움에 있다고 본다.

## Key claims

- The system has **three layers**: immutable raw sources, the LLM-maintained wiki, and a configuration document (`CLAUDE.md` / `AGENTS.md`) that fixes conventions.
- A new source triggers **many edits across the graph** — entity pages, concept refinements, topic indexes, contradiction flags — not just a single summary file.
- Two flat files, `index.md` (catalog) and `log.md` (chronological record), make the wiki navigable **without embedding-based retrieval**.
- The pattern generalizes across personal development, research, book annotation, team knowledge bases, competitive analysis, and hobby documentation.
- Traditional human-maintained wikis fail because **maintenance cost grows faster than content value**; the marginal cross-referencing edits get deferred and abandoned.

## Methods / evidence

Argumentative — no empirical study. The piece is a paraphrase of a design pattern proposal, leaning on intuition about why human-maintained wikis decay and on a structural claim about what an LLM can absorb that humans cannot (the per-source 10–15 cross-reference edits). Treat it as a design proposal, not a measured result.

## Surprising or load-bearing bits

- The **asymmetry** is the load-bearing observation: the bottleneck on traditional wikis isn't writing pages, it's the tedious cross-reference work after each new page. LLMs do not get bored. (See [[30-Concepts/maintenance-asymmetry]].)
- The deliberate choice of **flat markdown + two anchor files** instead of a vector store. Navigation by reading `index.md` is a bet that structured retrieval beats embedding-based retrieval for compounding knowledge.
- The user's role explicitly shifts from **author** to **curator** — this changes what "good" looks like for the human's contribution.

## Entities mentioned

- [[20-Entities/andrej-karpathy]] — proposed the pattern; cited as the originator of "LLM Wiki" as a named idea.

## Concepts touched

- [[30-Concepts/llm-wiki]] — the source defines the pattern itself.
- [[30-Concepts/three-layer-architecture]] — sources / wiki / schema; introduced as the structural skeleton.
- [[30-Concepts/compounding-artifact]] — framing that distinguishes this from one-shot retrieval.
- [[30-Concepts/maintenance-asymmetry]] — humans defer cross-reference work; LLMs do not.
- [[30-Concepts/ingest-workflow]] — the per-source procedure (read → summarize → propagate → log).

## Connections to other sources

- None yet — this is the first ingested source. Future sources should connect back here when they touch knowledge-management patterns or LLM-as-maintainer designs.

## Open questions

- The piece asserts that flat-file + `index.md` navigation suffices, but at what scale does this break? When does the wiki need real retrieval infrastructure?
- It does not address conflict resolution between contradictory sources beyond "flag it." Practical resolution policy is undefined.
- Schema evolution: how does the wiki adapt when the conventions in `CLAUDE.md` themselves change mid-stream?
