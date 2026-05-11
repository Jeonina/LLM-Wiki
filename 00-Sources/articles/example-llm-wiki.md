# Example seed: a paraphrase of Karpathy's LLM Wiki idea

This is a seeded example source so you can run the first ingest and see the system populate. Delete it and its derived summary once you've understood the flow, or keep it as a worked example.

## Paraphrase

Andrej Karpathy describes a pattern he calls the **LLM Wiki**: instead of asking an LLM to re-derive answers from raw documents every time, you have the LLM incrementally build a persistent, structured knowledge base in markdown. The wiki sits between the user and the raw sources, and it compounds — every new source improves it.

The architecture has three layers. The **raw sources** are immutable: papers, articles, images, data files. The LLM never modifies them. The **wiki** is the LLM's output: pages for entities, concepts, topics, and synthesized notes, plus per-source summaries. A configuration document — `CLAUDE.md` for Claude, `AGENTS.md` for other tools — specifies how the LLM should behave: what folder structure to use, what frontmatter to apply, how to ingest, how to query, how to maintain.

When a new source arrives, the LLM reads it, writes a summary page, and then propagates the new information across the existing graph. A single ingest might touch ten or fifteen pages — adding mentions to entity pages, refining concept definitions, updating topic indexes, flagging contradictions with previously ingested sources. This is the part humans give up on. LLMs do not get bored.

Two special files anchor the system: `index.md`, which catalogs every page in the wiki and is updated on each ingest, and `log.md`, an append-only chronological record of activity. Together they make the wiki navigable without any embedding-based retrieval infrastructure.

The pattern works for personal development tracking, research deep-dives, book annotations, team knowledge bases, competitive analysis, and hobby documentation — anywhere knowledge accumulates over time and re-derivation from raw sources becomes wasteful.

## Why this works

Traditional wikis fail because the marginal cost of maintenance grows faster than the marginal value of the content. Each new page should ideally trigger updates to many existing pages, but humans batch these updates, defer them, and eventually stop. An LLM happily makes the fifteen edits, every time. The human's role shifts from author and bookkeeper to curator and questioner.

## Notable people and concepts

- **Andrej Karpathy** — proposed this pattern; previously known for his work on neural networks and on educational LLM material.
- **Three-layer architecture** — sources, wiki, schema.
- **Compounding artifact** — the framing that distinguishes this from one-shot retrieval.
- **`index.md` and `log.md`** — the navigational and historical anchors.
