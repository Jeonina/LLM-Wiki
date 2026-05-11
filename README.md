# LLM Wiki

A personal knowledge base where Claude is the maintainer. You curate sources and ask questions; Claude reads, distills, links, and keeps the graph clean.

Based on [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#llm-wiki).

## How it works

Three layers:

- **Sources** — raw inputs you drop into `00-Sources/`. Immutable.
- **Wiki** — the markdown knowledge graph (`10-Summaries/`, `20-Entities/`, `30-Concepts/`, `40-Topics/`, `50-Notes/`). Claude owns this.
- **Schema** — `CLAUDE.md` + `90-Meta/templates/`. The conventions Claude follows.

Two special files at the vault root:

- **`index.md`** — the catalog. Claude updates it on every ingest.
- **`log.md`** — append-only record of every ingest, query, and lint pass.

Claude's full operating manual is in `CLAUDE.md`.

---

## One-time setup

1. **Open this folder as an Obsidian vault.**
   - Obsidian → *Open folder as vault* → pick `LLM-Wiki/`.
   - Obsidian will create `.obsidian/` for its config. That's fine — it lives alongside the wiki.
   - Recommended Obsidian settings: turn on *Files & Links → Use [[Wikilinks]]* (it's the default) and *New link format → Shortest path when possible*.

2. **Open this same folder in Claude Code.**
   ```
   cd /Users/jeonina/Desktop/Claude/scDNA/LLM-Wiki
   claude
   ```
   Claude reads `CLAUDE.md` automatically — that's what makes it act as a wiki maintainer instead of a generic assistant.

That's it. No databases, no embeddings, no servers.

---

## Daily workflow

### Add a source

Drop the file into the appropriate `00-Sources/` subfolder:

```
00-Sources/articles/   → web articles, blog posts, transcripts (markdown or text)
00-Sources/papers/     → academic PDFs
00-Sources/books/      → book PDFs or per-chapter markdown
00-Sources/images/     → diagrams, screenshots, figures
00-Sources/data/       → CSVs, JSON, anything tabular
```

Naming: keep the original filename or rename to something readable. The slug Claude uses for the summary page is derived from the filename (lowercased, spaces → hyphens).

For sources you have only as URLs, either save them as markdown into `00-Sources/articles/` first, or tell Claude the URL and ask it to fetch and save.

### Ingest

In Claude Code, say:

> Ingest the new sources.

Claude will:

1. Run `tools/pending-sources.sh` (or its own diff) to find unsummarized files.
2. Read each one.
3. Write a `10-Summaries/<slug>.md` page.
4. **Touch 5–15 other pages** — entities, concepts, topics — adding cross-links and dated mentions.
5. Update `index.md`.
6. Append an entry to `log.md`.
7. Tell you what it did and what tensions or gaps it noticed.

You can also be specific: *"Ingest only `00-Sources/papers/foo.pdf`"* or *"Ingest, but focus on entities and skip concept pages this round."*

### Query

Ask any question. Claude will search the wiki first and answer with citations to the wiki pages (which themselves cite sources). If the wiki doesn't have it, Claude will say so and may pull from raw sources or ask you for more.

If a query produces a synthesis worth keeping, Claude will offer to promote it into `50-Notes/`.

### Maintenance pass

Every once in a while, run:

> Lint the wiki.

Claude will check for contradictions, stale claims, orphaned pages, missing cross-references, index drift, and broken links. Mechanical fixes happen automatically; substantive issues come back as a punch list for you to weigh in on.

### Tweak the schema

If you want different page types, different folders, different frontmatter — edit `CLAUDE.md`. That's the contract Claude follows. Templates live in `90-Meta/templates/` and are referenced from `CLAUDE.md`.

---

## A worked first run

There's an example article seeded at `00-Sources/articles/example-llm-wiki.md`. Try this:

1. Open the vault in Claude Code.
2. Say: *"Ingest the new sources."*
3. Watch Claude create the summary, the entity pages it references, the concept pages, update `index.md`, and log the activity.
4. Then ask: *"What does the wiki say about [some concept from the seeded article]?"* — Claude should answer from the wiki pages, not the raw source.
5. Delete the seeded source + its summary if you want a clean slate, or keep it as a worked example.

---

## File reference

```
LLM-Wiki/
├── CLAUDE.md                  Maintainer instructions (the contract)
├── README.md                  This file
├── index.md                   Catalog of all wiki pages
├── log.md                     Append-only activity log
├── 00-Sources/                Raw sources (immutable)
├── 10-Summaries/              One summary page per source
├── 20-Entities/               People, orgs, places, products, projects
├── 30-Concepts/               Ideas, theories, definitions
├── 40-Topics/                 Broad themes
├── 50-Notes/                  Synthesized findings worth keeping
├── 90-Meta/templates/         Page templates
└── tools/
    └── pending-sources.sh     Lists sources not yet summarized
```

---

## Tips

- **Be patient on first ingests.** A serious source might touch 20 pages. That's the system working as designed.
- **Read the log.** `log.md` is your audit trail. If Claude does something you didn't expect, the explanation is there.
- **Don't edit `00-Sources/`** by hand once Claude has read them. If a source needs correcting, do it before ingest, or ingest a v2 alongside.
- **Version-control the vault.** `git init` inside `LLM-Wiki/` and commit after each ingest. You'll thank yourself.
- **Schema drift is normal.** As the wiki grows, you'll want new page types or new conventions. Edit `CLAUDE.md` and tell Claude what changed.
