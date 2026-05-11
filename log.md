# Activity log

Append-only. Newest at the top. One entry per session — ingest, query, or maintenance pass.

---

## 2026-05-11 — Third ingest: 11 scDNA-seq / multi-omics / chromatin / methylation reviews

- **Discovered:** 133 new papers landed in `00-Sources/papers/` (user ran `download_papers.py` to pull a scDNA literature corpus). At user direction, **scoped this ingest to the 11 review papers** that will scaffold the topic layer for the remaining 122 primary papers to slot into later. Depth strategy: full-depth read of each review; skim approach for future primary-paper batches.
- **Ingested reviews:**
  - [[10-Summaries/diane-2025-naturereviewsgenetics]] — Shao/Walsh 2025 keystone scDNA-seq review.
  - [[10-Summaries/charles-2016-naturereviewsgenetics]] — Gawad/Quake 2016 foundational scDNA review.
  - [[10-Summaries/gilad-2021-annualreviewofgenomicsandhumangenetics]] — Evrony 2021 capabilities framework.
  - [[10-Summaries/lars-2017-naturereviewsgenetics]] — Forsberg 2017 mosaicism in health/disease.
  - [[10-Summaries/ian-2015-trendsingenetics]] — Campbell/Lupski 2015 mosaicism transmission genetics.
  - [[10-Summaries/sandy-2019-naturereviewsgenetics]] — Klemm/Greenleaf 2019 chromatin accessibility.
  - [[10-Summaries/zachary-2013-naturereviewsgenetics]] — Smith/Meissner 2013 DNA methylation in development.
  - [[10-Summaries/yilei-2025-naturereviewsgenetics]] — Fu/Sedlazeck/Timp 2025 long-read methylation.
  - [[10-Summaries/alev-2023-naturereviewsmolecularcellbiology]] — Baysoy/Fan/Satija 2023 multi-omics landscape.
  - [[10-Summaries/katy-2023-naturereviewsgenetics]] — Vandereyken/Voet 2023 single-cell + spatial multi-omics.
  - [[10-Summaries/lukas-2023-naturereviewsgenetics]] — Heumos/Theis 2023 best practices.
- **Created:** 11 summaries + 13 entities + 25 concepts + 5 topics = **54 new wiki pages** beyond the source PDFs.
  - Entities: [[20-Entities/diane-d-shao]], [[20-Entities/christopher-walsh]], [[20-Entities/charles-gawad]], [[20-Entities/stephen-quake]], [[20-Entities/gilad-evrony]], [[20-Entities/lars-forsberg]], [[20-Entities/james-lupski]], [[20-Entities/william-greenleaf]], [[20-Entities/alexander-meissner]], [[20-Entities/fritz-sedlazeck]], [[20-Entities/winston-timp]], [[20-Entities/rong-fan]], [[20-Entities/rahul-satija]], [[20-Entities/thierry-voet]], [[20-Entities/fabian-theis]].
  - Method concepts: [[30-Concepts/scdna-seq]], [[30-Concepts/scwga]], [[30-Concepts/mda]], [[30-Concepts/pta]], [[30-Concepts/malbac]], [[30-Concepts/dop-pcr]], [[30-Concepts/dlp-plus]], [[30-Concepts/meta-cs]], [[30-Concepts/duplex-sequencing]], [[30-Concepts/scdna-capabilities-framework]], [[30-Concepts/atac-seq]], [[30-Concepts/dnase-seq]], [[30-Concepts/bisulfite-sequencing]], [[30-Concepts/long-read-sequencing]], [[30-Concepts/single-cell-multiomics]], [[30-Concepts/gt-seq]], [[30-Concepts/cite-seq]], [[30-Concepts/spatial-multiomics]].
  - Biology concepts: [[30-Concepts/somatic-mosaicism]], [[30-Concepts/post-zygotic-variation]], [[30-Concepts/microchimerism]], [[30-Concepts/developmental-mutation-timing]], [[30-Concepts/gonadal-mosaicism]], [[30-Concepts/lineage-tracing]], [[30-Concepts/clonal-hematopoiesis]], [[30-Concepts/dna-methylation]], [[30-Concepts/cpg-island]], [[30-Concepts/dnmt]], [[30-Concepts/tet-enzymes]].
  - New topics: [[40-Topics/scdna-seq]], [[40-Topics/somatic-mosaicism]], [[40-Topics/whole-genome-amplification]], [[40-Topics/dna-methylation]], [[40-Topics/long-read-sequencing]].
- **Updated existing pages:** [[40-Topics/single-cell-multiomics]], [[40-Topics/chromatin-architecture]], [[40-Topics/hematopoietic-malignancies]] — added new concept and source links; `index.md` heavily reorganized into the now-substantial methods/biology/wiki sections.
- **Tooling**: Quartz server bg task `bscsqurx6` crashed when a Chrome `*.crdownload` partial-download file appeared in `00-Sources/papers/`. Hardened the Quartz `ignorePatterns` in `.quartz/quartz.config.ts` to filter `*.crdownload`, `*.tmp`, `*.part`, `.DS_Store`, `~$*`, `*.py`, `*.sh`, `*.csv` before restarting.
- **Notable findings / framings**:
  - **Two organizing axes of the field** emerge clearly from the reviews: (a) technology-organized (Diane 2025, Charles 2016 — chemistries and tradeoffs); (b) application/capability-organized (Gilad 2021 — fidelity/co-presence/phenotypic-association). Both are useful; the [[scdna-capabilities-framework]] is the better entry point for newcomers choosing a method for their question.
  - **The PTA inflection point**: scWGA technology went from "useful for CNVs, bad for SNVs" (MDA/MALBAC) to "useful for both" (PTA, ~95% coverage with high allelic balance) over ~5 years. This is the methodological backbone of the current scDNA-seq generation, including [[10-Summaries/elliott-2025-naturebiotechnology|scDAF-seq]].
  - **Single-strand DNA damage as a major scWGA failure mode** is more visible now than in 2016: ~70k ssDNA lesions per cell per day means single-strand dropout produces catastrophic false-positive rates without duplex protection ([[10-Summaries/diane-2025-naturereviewsgenetics]]). This argues for duplex methods becoming the future direction.
  - **The mosaicism cluster** (Lars 2017 + Ian 2015 + Diane 2025) now connects directly to the **MPN cluster** ([[10-Summaries/anna-2019-nature]] + [[10-Summaries/franco-2024-nature]]) via [[clonal-hematopoiesis]] — JAK2V617F CH is the on-ramp to MPN, and GoT–ChA's pre-disease chromatin priming finding fits directly into the Lars 2017 framing of mosaicism as both biology and disease driver.
  - **Schema note**: added `doi` and `journal` to summary frontmatter consistently across this batch. Template should be updated next maintenance pass.
- **Pending in `00-Sources/papers/`**: 122 primary papers, plus `download_papers.py` (user script — should be moved to `tools/` next maintenance).
- **Next**: future ingest sessions can skim the primary papers and slot them under the topic scaffolds created here. Natural batches: (a) WGA method papers (cite [[scwga]]/[[mda]]/[[pta]]/etc concepts); (b) brain mosaicism papers (cite [[somatic-mosaicism]]/[[lineage-tracing]]); (c) chromatin/methylation primary papers; (d) lineage-tracing in humans; (e) cancer single-cell studies.

---

## 2026-05-07 — Second ingest: three single-cell genomics method papers

- **Ingested:**
  - `00-Sources/papers/Anna_2019_Nature.pdf` — Nam et al., *Nature* 571:355–360, GoT method paper.
  - `00-Sources/papers/Franco_2024_Nature.pdf` — Izzo et al., *Nature* 629:1149–1157, GoT–ChA method paper.
  - `00-Sources/papers/Elliott_2025_NatureBiotechnology.pdf` — Swanson et al., *Nature Biotechnology*, DAF-seq / scDAF-seq method paper.
- **Created:** 3 summaries, 6 entities, 12 concepts, 3 topics — 24 pages total beyond the sources.
  - Summaries: [[10-Summaries/anna-2019-nature]], [[10-Summaries/franco-2024-nature]], [[10-Summaries/elliott-2025-naturebiotechnology]].
  - Entities: [[20-Entities/anna-s-nam]], [[20-Entities/franco-izzo]], [[20-Entities/dan-a-landau]], [[20-Entities/elliott-g-swanson]], [[20-Entities/andrew-b-stergachis]], [[20-Entities/landau-lab]].
  - Concepts (methods): [[30-Concepts/got]], [[30-Concepts/circularization-got]], [[30-Concepts/got-cha]], [[30-Concepts/daf-seq]], [[30-Concepts/fiber-seq]], [[30-Concepts/single-molecule-footprinting]], [[30-Concepts/dogma-seq]], [[30-Concepts/chromatin-accessibility]], [[30-Concepts/chromatin-actuation]].
  - Concepts (biology): [[30-Concepts/calr-mutation]], [[30-Concepts/jak2-v617f]], [[30-Concepts/myeloproliferative-neoplasm]], [[30-Concepts/unfolded-protein-response]], [[30-Concepts/hematopoietic-differentiation]].
  - Topics: [[40-Topics/single-cell-multiomics]], [[40-Topics/hematopoietic-malignancies]], [[40-Topics/chromatin-architecture]].
- **Updated:** `index.md` reorganized into Methods / Biology / Wiki concept subsections; added 6 new domain-specific open questions.
- **Tooling:** installed `poppler` via Homebrew so PDF ingestion works (the Read tool's bundled `pdftoppm` lookup didn't see Homebrew's PATH; extracted text via Bash `pdftotext -layout` instead, then read the text files with Read).
- **Notable findings / tensions:**
  - The three papers form a tight cluster around **co-measuring genotype with chromatin/expression in single cells**, with two distinct architectural traditions: **droplet-scale** (Landau lab: GoT → GoT–ChA) and **single-molecule, chromosome-length** (Stergachis lab: Fiber-seq → DAF-seq). The two trade off cell number against per-cell coverage — a clear axis for a future synthesis note.
  - The **maintenance-asymmetry** pattern paid off this ingest: many of the cross-references (Franco Izzo as co-author on Anna 2019 *and* first author on Franco 2024; the gDNA-vs-cDNA architectural decision Franco 2024 makes that obviates Anna 2019's circularization-GoT workaround) are exactly the kinds of links a human would batch and defer.
  - **Schema notes:** added a `doi` and `journal` field to summary frontmatter for paper sources, beyond what the template specifies. Templates should be updated next time we touch them — flagging here so this isn't silent drift.
- **Next:** await further sources. With three methods papers in, the natural promotion target for `50-Notes/` is a synthesis comparing droplet-scale vs single-molecule strategies for single-cell genotype-phenotype linking.

---

## 2026-05-07 — First ingest: Karpathy LLM Wiki seed

- **Ingested:** `00-Sources/articles/example-llm-wiki.md` (paraphrase of Andrej Karpathy's LLM Wiki proposal).
- **Created:** 1 summary, 1 entity, 5 concepts, 2 topics — 9 pages total beyond the source itself.
  - Summary: [[10-Summaries/example-llm-wiki]]
  - Entity: [[20-Entities/andrej-karpathy]]
  - Concepts: [[30-Concepts/llm-wiki]], [[30-Concepts/three-layer-architecture]], [[30-Concepts/compounding-artifact]], [[30-Concepts/maintenance-asymmetry]], [[30-Concepts/ingest-workflow]]
  - Topics: [[40-Topics/llm-tooling-patterns]], [[40-Topics/knowledge-management]]
- **Updated:** `index.md` — populated all category sections; added four open questions surfaced by the source.
- **Notable findings / tensions:**
  - The source asserts flat-file navigation suffices, but offers no scale threshold. Logged as open question.
  - The "5–15 cross-reference edits per ingest" heuristic is unjustified; treat as rule of thumb only.
  - Maintenance asymmetry favors LLMs but the source is silent on LLM failure modes (drift, hallucinated cross-refs). Worth watching as more sources arrive.
- **Next:** await further sources. The graph is thin enough that the second ingest should focus on new entities/concepts that connect *back* to the LLM Wiki cluster — that's the first real test of compounding.

---

## 2026-05-07 — Vault relocated

- Moved vault from `/Users/jeonina/Desktop/Claude/LLM-Wiki` to `/Users/jeonina/Desktop/Claude/scDNA/LLM-Wiki`.
- Updated path reference in `README.md`. The helper script (`tools/pending-sources.sh`) resolves the vault root relative to itself, so it kept working without changes.

---

## 2026-05-07 — Wiki bootstrapped

- Created folder structure: `00-Sources/`, `10-Summaries/`, `20-Entities/`, `30-Concepts/`, `40-Topics/`, `50-Notes/`, `90-Meta/templates/`, `tools/`.
- Wrote `CLAUDE.md` (operating instructions), `README.md` (human-facing), `index.md` (catalog), this log.
- Added templates for source, summary, entity, concept, topic, note pages.
- Added `tools/pending-sources.sh` to list sources not yet summarized.
- Seeded `00-Sources/articles/example-llm-wiki.md` so the first ingest has something to chew on.
- **Next:** user runs first ingest. See `README.md` step 3.
