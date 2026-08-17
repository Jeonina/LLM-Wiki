# Activity log

Append-only. Newest at the top. One entry per session — ingest, query, or maintenance pass.

---

# 2026-08-17 — Ingest: 23 clippings (tumour/lineage phylogenetics, integration & reference mapping, epimutation clocks)

**Sources ingested (23).** Three clusters, two of which were near-absent from the corpus.

*Tumour and lineage phylogenetics (11).* Cancer SNV trees: [[10-Summaries/ross-2016-onconem]] (nested effects models; the only method here that infers **unobserved** subpopulations), [[10-Summaries/el-kebir-2018-sphyr]] (*k*-Dollo), [[10-Summaries/singer-2018-sciphi]] (joint calling + tree by MCMC), [[10-Summaries/malikic-2019-phiscs]] (subperfect phylogeny; ILP *and* Boolean CSP), [[10-Summaries/foroughmand-2022-scelestial]] (Steiner-tree approximation with performance guarantees). CRISPR recorders: [[10-Summaries/gong-2022-dclear]], [[10-Summaries/seidel-2022-tidetree]], [[10-Summaries/sashittal-2023-startle]], [[10-Summaries/chu-2025-laml]], [[10-Summaries/seidel-2026-sciphy]]. Endogenous markers: [[10-Summaries/kwok-2022-mquad]].

*Integration, batch correction and reference mapping (10).* [[10-Summaries/haghverdi-2018-mnn]] and [[10-Summaries/butler-2018-seurat-cca]] (same *Nature Biotechnology* issue, 2 April 2018 — the field's origin), [[10-Summaries/hao-2021-seurat-wnn]], [[10-Summaries/gayoso-2021-totalvi]], [[10-Summaries/kang-2021-symphony]], [[10-Summaries/song-2021-scgcn]], [[10-Summaries/biancalani-2021-tangram]], [[10-Summaries/kleshchevnikov-2022-cell2location]], [[10-Summaries/lakkis-2022-scipenn]], [[10-Summaries/yuan-2024-linger]].

*Epimutation clocks (2).* [[10-Summaries/shahryary-2020-alphabeta]] (plants) and [[10-Summaries/gabbutt-2025-evoflux]] (human, clinical scale).

**Pages created (24).** 23 summaries plus one concept, [[30-Concepts/reference-atlas-mapping]] — reference mapping is a distinct operation from integration (the reference is frozen and asymmetric) and now has five methods pointing at it.

**Pages updated (23).** 9 concepts, 9 entities, 7 topics, plus `index.md`, `10-Summaries/index.md` and `catalog.md`. All updates carry dated `## Added 2026-08-17` sections.

**Correction to an earlier claim.** In the 2026-08-11 triage discussion I described `stuart-2021-natmethods` as "Seurat WNN". It is **Signac** (single-cell chromatin state analysis). The actual WNN paper — Hao et al. 2021, *Cell* — was absent from the corpus until this ingest and is now at [[10-Summaries/hao-2021-seurat-wnn]]. Any manuscript sentence citing "Seurat WNN" needs that citation, not Stuart 2021.

**Notable findings and tensions.**

- **Tree inference and error correction are the same problem**, reached independently in 2018 at two levels — read counts ([[10-Summaries/singer-2018-sciphi]]) and genotype matrices ([[10-Summaries/el-kebir-2018-sphyr]]). Neither cites the other's framing. The consequence is powerful and double-edged: a mutation can be called in a cell with zero variant reads because the tree says it belongs there — and when the tree is wrong, the same mechanism manufactures *correlated* false positives, which neither paper characterises.
- **Missing data can be informative.** [[10-Summaries/chu-2025-laml]] separates heritable missingness (inherited by descendants, phylogenetically informative) from dropout (not) — they look identical in the data and no prior method distinguished them. Recorded on [[30-Concepts/phylogenetic-inference]]; the same conflation of technical and biological zeros plausibly recurs across single-cell modalities.
- **Only one blinded benchmark exists in this literature.** The Allen Institute DREAM Challenge ([[10-Summaries/gong-2022-dclear]]) is organiser-scored on common data; every other tool paper here benchmarks itself, including the seven-method comparison in [[10-Summaries/foroughmand-2022-scelestial]]. Flagged on [[40-Topics/computational-methods]].
- **The reconstruction method changes the biology.** [[10-Summaries/seidel-2026-sciphy]] reports significant differences from UPGMA trees on the same data, "underscoring the impact of the reconstruction method on the inferred cellular relationships and growth dynamics" — the lineage-tracing counterpart of the caller-concordance problem in [[10-Summaries/ha-2023-natmethods]].
- **A new genre named: predicting a modality you never measured.** Five instances now in the corpus, five mechanisms, and only [[10-Summaries/lakkis-2022-scipenn]] returns an uncertainty estimate — so elsewhere an imputed value is indistinguishable from a measured one in the output matrix. Recorded on [[30-Concepts/reference-atlas-mapping]].
- **Every reference-based method shares one failure**: a cell state absent from the reference has nowhere correct to go — projected arbitrarily, silently redistributed, or confidently mislabelled. Also on [[30-Concepts/reference-atlas-mapping]].
- **"Most single cells are not independent"** ([[10-Summaries/yuan-2024-linger]]) — the effective sample size is far below the cell count. This applies to every method that treats cells as replicates, including the 3D-genome callers ingested on 2026-08-13.
- **The epimutation clock was quantified in plants first.** [[10-Summaries/shahryary-2020-alphabeta]] established neutral accumulation, somatic origin, and demonstrable age-dating in 2020; the mammalian epimutation-tracing literature generally *assumes* the neutrality AlphaBeta *tested*. Both it and [[10-Summaries/gabbutt-2025-evoflux]] share an unquantified limit: gain/loss equilibrium means the clock saturates.
- **Engineered recorders do not work in humans.** Every methodological advance in the CRISPR lineage literature — timing, phylodynamics, uncertainty — is unavailable for human somatic mosaicism, which is this corpus's central subject. Recorded on [[40-Topics/single-cell-lineage-tracing]].
- **Source limitations.** [[10-Summaries/malikic-2019-phiscs]] was clipped as abstract plus two figure captions; [[10-Summaries/seidel-2022-tidetree]] as appendices plus abstract, with no real-data application. Both summaries are marked accordingly and flagged for full-text re-ingest.

**Verification.** All 23 DOIs resolved against CrossRef and checked against source-file titles **before** writing, following the 2026-08-14 audit — 23/23 correct, no repeat of the cardilla/morriss failures. 0 broken wikilinks; 0 orphan pages; `10-Summaries/index.md` matches the directory exactly.

**Not done.** `catalog.md` received the 23 new entries but its ~93 pre-existing gaps remain — still awaiting the keep-both-or-merge decision flagged on 2026-08-14.

---

# 2026-08-14 — Maintenance: DOI audit + duplicate merge + index reconciliation

**DOI audit (all 277 summaries).** Every summary's DOI was resolved against the CrossRef API and the returned title compared against the **source-file title** (the clipping's own `title:` field) rather than the wiki's summary title — the source file is ground truth, the summary title is editorial. 271 verified clean.

Genuinely wrong DOIs — 2:

- **[[10-Summaries/cardilla-2025-spatial-methylome]]** carried `10.1038/s41586-025-09484-z`, which resolves to *"Long-distance remote epitaxy"* (Nature 2025) — an unrelated materials-science paper. Corrected to **`10.1038/s41586-025-09478-x`**, verified as *"Spatial joint profiling of DNA methylome and transcriptome in tissues"*.
- **`morriss-2024-spatial-genomics-clonal`** carried `10.1101/2024.10.07.617096`, resolving to an unrelated bioRxiv preprint on environment and diet. Root cause turned out to be a duplicate page, not a typo — see below.

Other DOI-layer fixes:

- **[[10-Summaries/telenius-1992-dop-pcr]]** — the DOI `10.1016/0888-7543(92)90147-K` contains parentheses, which truncated the markdown link at the first `)`. The DOI itself was correct; the rendered link was dead. Percent-encoded to `%2892%2990147-K`.
- **[[10-Summaries/ghorbani-2019-comp-epigenetics]]** — no DOI, and journal recorded as the mangled string `JournalOfAppliedBiologyAnd`. Added `10.7324/JABB.2019.70114` and the correct journal name.
- **[[10-Summaries/ma-2020-share-seq]]** — cited as "Ma (2020) … *?*". This page summarises a *Nature Reviews Genetics* research highlight **by Dorothy Clyde**, not the primary paper. Attribution corrected, DOI `10.1038/s41576-020-00308-6` added, and a note added pointing to the primary source [[10-Summaries/ma-2020-cell]].
- **[[10-Summaries/mcinnes-2018-umap]]** — CrossRef returns 404 for `10.48550/arXiv.1802.03426`. This is expected: arXiv DOIs are registered with DataCite, not CrossRef. Confirmed valid via the DataCite API. **No change.**
- **[[10-Summaries/tickle-2019-infercnv]]** — no DOI because it is software (Broad Institute Trinity CTAT), cited by GitHub URL. **No change; correct as-is.**

**Duplicate merged.** `morriss-2024-spatial-genomics-clonal` and [[10-Summaries/zhao-2022-nature]] both pointed at the *same source file* (`Spatial genomics enables multi-modal study of clonal heterogeneity in tissues`) whose own frontmatter URL is the Nature article. The Morriss page — created 2026-05-18 at `ingest_depth: abstract+intro` — named a middle author as first author, dated the paper 2024 instead of 2022, and carried a DOI belonging to a different preprint; its body text is generic enough to have been written from the title alone. The 2026-05-14 log entry had already flagged the pair as "one of them is misattributed … left both for now"; this resolves it. The page was deleted, its aliases and its one genuinely useful framing (slide-DNA-seq as the sequencing-side counterpart to in-situ genome sequencing) folded into `zhao-2022-nature`, and 6 inbound links repointed.

**Index reconciliation.**

- [[10-Summaries/index]] was missing all 20 summaries from the 2026-08-13 ingest, and carried a duplicate `zhao-2022-nature` row after the merge. Both fixed; the index now matches the directory exactly — 0 missing, 0 stale.
- [[catalog]] claimed to list "All papers in this wiki" while covering 162 of 277. The 20 new summaries were added, and the scope line was rewritten to describe it accurately as a curated reading path pointing to [[10-Summaries/index]] for complete coverage. **~93 pre-existing entries remain uncovered** — flagged rather than backfilled, because `catalog.md` and `10-Summaries/index.md` substantially overlap in purpose and whether to keep both is a schema question for the user.

**Verification.** 0 broken wikilinks (excluding illustrative `<slug>` placeholders in this log's own prose); 0 orphan pages; 277 summaries for 276 source files with 0 pending; 271/271 resolvable DOIs now matching their source titles.

---

# 2026-08-13 — Ingest: 20 bookmarked sources (WGA history, methylation protocols, single-cell 3D callers, single-molecule lesions)

**Sources ingested (20).** All had accumulated in `00-Sources/papers/` without summaries. They cluster into five groups.

*scDNA-seq methodology and applications (6).* [[10-Summaries/wang-2014-nuc-seq]] (nuc-seq — G2/M nuclei give MDA four template copies; 91% breadth, 9.73% ADO; punctuated CNAs vs gradual SNVs), [[10-Summaries/gawad-2014-all-clonal-origins]] (1,479 ALL cells; codominant clones in 5/6 patients; four-way ADO measurement; clone-detection design rule), [[10-Summaries/hou-2015-wga-comparison]] and [[10-Summaries/huang-2015-scwga-review]] (the two independent 2015 WGA benchmarks), [[10-Summaries/luquette-2021-scan2]] (SCAN2 — neuronal rate revised to 15 SNVs/yr, first indel rate), [[10-Summaries/liu-2024-hidef-seq]] (HiDEF-seq — unamplified single molecules, single-strand mismatch and damage signatures).

*Single-cell methylation (5).* [[10-Summaries/luo-2017-snmc-seq]] (snmC-seq founding paper — mCH in 100-kb bins as the sparsity workaround), [[10-Summaries/clark-2017-scbs-seq-protocol]] (PBAT protocol, ~50% CpG/cell), [[10-Summaries/guo-2015-scrrbs-protocol]] (one-tube scRRBS, ~70% CGIs, consistent CpGs across cells), [[10-Summaries/mulqueen-2018-sci-met]] (combinatorial indexing; alignment rate 68% vs the field's 25%), [[10-Summaries/zhang-2023-drop-bs]] (droplets; in-droplet bisulfite conversion yields 9× more library).

*Single-cell 3D genome (5).* [[10-Summaries/yu-2021-snaphic]] (loops), [[10-Summaries/xiong-2024-scghost]] (subcompartments), [[10-Summaries/park-2026-mintsc]] (multi-way interactions), [[10-Summaries/chakraborty-2022-dchic]] (differential compartments), [[10-Summaries/li-2014-chia-pet]] (the protein-anchored branch).

*Single-cell genome assembly (3).* [[10-Summaries/chitsaz-2011-velvet-sc]], [[10-Summaries/peng-2012-idba-ud]], [[10-Summaries/bankevich-2012-spades]] — a historical layer the corpus was missing entirely.

*Spatial (1).* [[10-Summaries/debnath-2026-ison]] (ISON — inferring spatial chromatin accessibility from ST + sc-multiome).

**Pages created (33).** 20 summaries; 4 concepts ([[30-Concepts/chromatin-loop]], [[30-Concepts/multi-way-chromatin-interaction]], [[30-Concepts/single-cell-genome-assembly]], [[30-Concepts/chia-pet]]); 9 entities ([[20-Entities/chongyuan-luo]], [[20-Entities/andrew-adey]], [[20-Entities/chang-lu]], [[20-Entities/ming-hu]], [[20-Entities/sunduz-keles]], [[20-Entities/ferhat-ay]], [[20-Entities/yijun-ruan]], [[20-Entities/pavel-pevzner]], [[20-Entities/zhana-duren]]).

**Pages updated (52).** 19 entity pages, 17 concept pages, 16 topic pages, plus `index.md`. All updates are dated `## Added 2026-08-13` sections.

**Notable findings and tensions.**

- **Chemistry sets biological constants.** SCAN2 revises the neuronal somatic SNV rate down to 15/year and attributes the revision to artifacts in older amplification chemistries ([[10-Summaries/luquette-2021-scan2]]). Read alongside the 2014 duplex-validation result that only 19.4–27.0% of single-cell-only mutation calls survive orthogonal confirmation ([[10-Summaries/wang-2014-nuc-seq]]), the corpus now has two independent demonstrations that single-cell-only calls need an arbiter.
- **HiDEF-seq refutes NanoSeq's single-strand calls** — ~18-fold inflated across nine matched samples ([[10-Summaries/liu-2024-hidef-seq]]). Flagged on [[30-Concepts/nanoseq]]; NanoSeq remains sound for double-strand burdens. This is the session's one direct contradiction between sources.
- **"MDA" is not one thing.** Three MDA kits diverged more on some metrics than the three chemistries did ([[10-Summaries/hou-2015-wga-comparison]]) — recorded on [[30-Concepts/scwga-chemistries]].
- **Binary A/B compartments are too coarse**, reached independently at bulk scale (~26% of significant changes involve no flip — [[10-Summaries/chakraborty-2022-dchic]]) and at single-cell scale (bulk A2 and B1 are not separable by single-cell scores — [[10-Summaries/xiong-2024-scghost]]).
- **A shared limitation across all four single-cell 3D callers**: every one reports features per *cell type*, not per cell, and assumes within-cluster homogeneity. The single-cell formulation currently buys statistical power rather than per-cell feature variability. Recorded on [[30-Concepts/single-cell-hi-c]] and [[40-Topics/3d-genome]].
- **All high-throughput methylation methods share an annotation dependency**: they cluster on mCH bins then label against snmC-seq reference DMRs rather than annotating de novo ([[10-Summaries/mulqueen-2018-sci-met]]; [[10-Summaries/zhang-2023-drop-bs]]). Recorded on [[30-Concepts/bisulfite-sequencing]].
- **Reduced representation is the road not taken.** scRRBS covers ~1M *consistent* CpGs per cell; the high-throughput successors cover ~1% *randomly*, so two cells rarely share a site. No benchmark in the corpus tests whether consistency beats coverage for cross-cell comparison ([[10-Summaries/guo-2015-scrrbs-protocol]]).
- **The protein-anchored 3D branch has no single-cell member** and instead serves as reference truth for single-cell loop callers — so those callers are scored against a bulk-defined truth, which penalises genuinely single-cell-specific loops by construction ([[10-Summaries/li-2014-chia-pet]]; [[10-Summaries/yu-2021-snaphic]]).
- **Source limitation.** [[10-Summaries/luquette-2021-scan2]] was clipped as abstract-only (58 lines, no methods or results). The summary is marked accordingly; the peer-reviewed Cell Genomics 2022 version should replace it.

**Verification.** 0 broken wikilinks across all 85 created/modified files (checked by extracting every wikilink target and diffing against the set of existing page basenames).

**Open maintenance item.** Link convention is mixed repo-wide: ~7,300 path-prefixed links (of the form `[[10-Summaries/<slug>]]`) versus bare links, despite `CLAUDE.md` preferring bare. The 2026-08-10 pass normalized only the pages written that day. This session's pages follow the prefixed majority. A repo-wide normalization is a large refactor and was **not** performed — flagged for a decision.

---

# 2026-08-10 — Maintenance: merge + link-convention normalization

Follow-up resolving the two items the rinse pass had flagged for a decision.

**Merged `lineage-tracing-somatic-mutations` into `lineage-tracing`.** The child page duplicated the parent, which already defined lineage tracing in terms of endogenous somatic mutations. Unique content was folded into a new `## Retrospective tracing from somatic mutations` section on the parent — the per-division mutation-inheritance rationale, the three routes to mutation calls (bulk colony/microdissection, single-cell PTA + duplex, and copy-number-based minimal event distance), the SCITE / SiFit / SCARLET tree-builders, and the three established applications. The child's aliases (`lineage tracing with somatic mutations`, `somatic lineage tracing`, `mutation-based lineage tracing`) and tags were absorbed into the parent's frontmatter, so old references still resolve. The `## Added 2026-08-10` heading was renamed to `## Endogenous mtDNA and engineered recorders`.

Inbound links rewritten in 11 files (`rodriguez-fraticelli-2026-lineage-tracing-review`, `wang-2026-multimodal-lineage-computational`, `scherer-2025-nature`, `coorens-2021-nature`, `lee-six-2018-hsc-dynamics`, `mckenna-2016-science`, `phylogenetic-inference`, `crispr-lineage-recording`, `cancer-clonal-evolution`, `single-cell-lineage-tracing`, `30-Concepts/index`). Redirection created duplicate targets on several `Related` lines and in one frontmatter list; these were de-duplicated across 50 files. The child page was deleted.

**Link convention normalized.** All 96 pages written today were converted from path-prefixed wikilinks (`[[30-Concepts/scwga]]`) to the bare form (`[[scwga]]`) that `CLAUDE.md` specifies — **2,250 links** rewritten. `[[00-Sources/...]]` links were deliberately left intact, because `tools/pending-sources.sh` parses the `source:` frontmatter field by that exact path and stripping the prefix would break source-coverage detection.

**Verification.** 0 broken wikilinks; 0 residual path-prefixed links in today's pages; `tools/pending-sources.sh` reports 0 pending of 256.

---

# 2026-08-10 — Maintenance: rinse pass (post-ingest)

Lint pass over the wiki following the 28-source ingest earlier the same day.

**Clean on arrival.** 0 orphan pages (every page has at least one inbound link), 0 index drift (every page appears in a catalog), 0 broken wikilinks, 0 pending sources (0 of 256).

**Fixed — mechanical.**

- `40-Topics/3d-genome.md` consolidated: two same-day sections merged into one; the `### Foundational Hi-C` sub-theme, which previously listed only single-cell papers, now leads with Lieberman-Aiden 2009, Dixon 2012 and Naumova 2013; a new `### Pipelines, storage, visualization` sub-theme collects HiC-Pro, Juicer, cooler, HiGlass, scHiCluster and Higashi; the stale "Synthesized notes — None yet" opener removed.
- `## Related` sections added to six topic pages that lacked them: `chromatin-architecture`, `single-cell-lineage-tracing`, `whole-genome-amplification`, `hematopoietic-malignancies`, `knowledge-management`, `llm-tooling-patterns`.
- `30-Concepts/lineage-tracing.md`: self-referential wikilink removed; duplicated/fragmented `## Related` block consolidated from seven bullets into three grouped lines.
- One bare claim on `30-Concepts/gene-regulatory-network.md` marked `(synthesis)`. Citation-density check over the 20 pages created today: 1 bare claim found, now 0.

**Fixed — substantive refinements from the new sources.**

- `40-Topics/3d-genome.md` gains two open questions: whether scHi-C imputation manufactures the per-cell variability it reports (neither scHiCluster nor Higashi quantifies the smoothing trade), and which TAD definition should be canonical given documented caller disagreement.
- `30-Concepts/scwga-chemistries.md`: the amplification-free branch was attributed only to DLP+ (Laks 2019). Added the founding mechanistic argument from Zahn 2017 — amplify-then-fragment forfeits duplicate detection — plus DOP-PCR's coverage-breadth saturation.
- `30-Concepts/lineage-tracing.md` "Contested points" refined: missing data splits into heritable and stochastic dropout with opposite implications, and homoplasy is an assay-design limit rather than an inference problem (both from Cassiopeia). Flagged that the heritable/stochastic distinction has not been made for scWGA allelic dropout anywhere in this corpus.

**Flagged, not resolved — needs a decision.**

- ~~**Possible merge:** `lineage-tracing` and `lineage-tracing-somatic-mutations` overlap substantially.~~ **Resolved same day** — merged, see the follow-up entry below.
- ~~**Mixed link convention:** 355 wikilinks use bare slugs rather than path prefixes.~~ **Resolved same day** — today's pages converted to the bare form, see below.
- **Incomplete summaries:** `welch-2019-liger` and `pliner-2018-cicero` remain metadata-only clippings with source-caveat blocks. Two `*(not bookmarked)*` markers remain, for Simpson 2017 (nanopore methylation) and SNARE-seq.

**Non-issue, checked.** 140 summary pages report no `updated:` field — this is correct: the summary template uses `ingested:` instead. Index pages report no `type:` field, also by template.

---

# 2026-08-10 — Ingest: 28 foundational & tooling sources (second batch)

**Sources ingested (28).** The corrected gap list from the manuscript reference audit, all now bookmarked and summarized.

*Foundational (5):* Lieberman-Aiden 2009 (Hi-C), Dixon 2012 (TADs), Zahn 2017 (DLP), Ramani 2017 (sciHi-C), Peric-Hupkes 2010 (LADs).
*Somatic mutation & lineage (3):* Alexandrov 2013 (mutational signatures), Xu 2012 (ccRCC single-cell exomes), Ludwig 2019 (mtDNA lineage tracing).
*Preprocessing & calling (5):* Li & Durbin 2009 (BWA), Li 2009 (SAMtools), Chen 2018 (fastp), Zhang 2008 (MACS), Meers 2019 (SEACR).
*Hi-C tooling (5):* Servant 2015 (HiC-Pro), Abdennur 2020 (cooler), Kerpedjiev 2018 (HiGlass), Zhou 2019 (scHiCluster), Zhang 2022 (Higashi).
*Integration & trajectory (4):* Korsunsky 2019 (Harmony), Welch 2019 (LIGER), Wolf 2019 (PAGA), Cao 2019 (MOCA / Monocle 3).
*Cancer & lineage inference (3):* Bakker 2016 (AneuFinder), Wang 2021 (MEDALT), Jones 2020 (Cassiopeia).
*Regulatory networks (3):* Pliner 2018 (Cicero), Kamimoto 2023 (CellOracle), Bravo 2023 (SCENIC+).

**Pages created (61).** 28 summaries in `10-Summaries/`; 19 concept pages (`read-alignment`, `mappability`, `duplicate-marking`, `quality-control-metrics`, `doublet-detection`, `sequencing-depth-and-coverage`, `peak-calling`, `hi-c-normalization`, `imputation`, `data-standards`, `dimensionality-reduction`, `clustering-algorithms`, `cell-type-annotation`, `batch-effect`, `trajectory-inference`, `gene-regulatory-network`, `copy-number-variation`, `chromosomal-instability`, `intratumor-heterogeneity`); 1 topic page (`40-Topics/computational-methods`); 13 entity pages (Heng Li, Job Dekker, Jesse Dixon, Leonid Mirny, Jian Ma, Cole Trapnell, Ken Chen, Jonathan Weissman, Nir Yosef, Samantha Morris, Soumya Raychaudhuri, Joshua Welch, Bradley Bernstein).

**Pages updated (~20).** Topics: `3d-genome`, `chromatin-architecture`, `cancer-clonal-evolution`, `single-cell-lineage-tracing`, `single-cell-multiomics`. Concepts: `topologically-associating-domain`, `chromatin-compartments`, `lamina-associated-domains`, `dlp-plus`, `single-cell-hi-c`, `mutational-signatures`, `lineage-tracing`, `phylogenetic-inference`. All four catalogs plus root `index.md` (count 225 → 253).

**Repair work.** 33 `*(not bookmarked)*` placeholders left by the first ingest were converted back to live wikilinks now that their targets exist — Lieberman-Aiden, Dixon, Zahn/DLP, Cooler, HiGlass, Higashi, scHiCluster, HiC-Pro, Harmony, LIGER, Cicero, MACS, SEACR, BWA, SAMtools, AneuFinder. Only Simpson 2017 (nanopore methylation) and SNARE-seq remain marked as unbookmarked. Twelve link targets were remapped to existing slugs (e.g. `allelic-dropout` → `allele-dropout`, `unique-molecular-identifier` → `umi-molecular-barcoding`, `somatic-mutation` → `somatic-mosaicism`); seven with no wiki page were de-linked to plain text (`heterochromatin`, `cohesin`, `data visualization`, `allele-specific analysis`, `X inactivation`, `kNN graph`).

**Verification.** `tools/pending-sources.sh`: **0 pending of 256** source files. Wiki-layer wikilink check: **0 broken links**.

**Notable findings and tensions.**

- *The n² rule propagates everywhere.* Hi-C resolution scales as reads² (Lieberman-Aiden), so 5–10% linear genome coverage becomes 0.25–1% of possible contacts per cell (scHiCluster). Clustering degrades below 25,000 contacts and collapses at 5,000 — below what sciHi-C's ~8,000–9,000 delivers. This single inequality explains why the scHi-C imputation literature exists.
- *Method choice is a hidden variable in this corpus.* Seven TAD callers disagree on one matrix (HiGlass); two Hi-C pipelines on identical raw data correlate at 0.83 (HiC-Pro); a ChIP-era peak caller emits ~900 false peaks on CUT&RUN data for an unexpressed factor (SEACR). Recorded in the new `40-Topics/computational-methods` page.
- *Ongoing chromosomal instability and a clonal karyotype are compatible.* Pooled cells reproduce the aCGH karyotype exactly while 56% of individual cells are unique (AneuFinder). Recurrent aneuploidy is evidence about selection, not stability.
- *Sampling depth determines heterogeneity findings.* Xu 2012 finds no subclones in 17 cells; DLP reaches ~0.05% subclone sensitivity with 6,000. Both results stand; the resolutions differ by two orders of magnitude. The same pattern governs trajectory topology — PAGA's basophil-origin ambiguity resolves only in the most densely sampled of three datasets.
- *Signature 1 links the epigenome to the mutational spectrum.* C>T at NpCpG from 5mC deamination is present in 25 of 30 cancer classes, making the most universal mutational process a chemical consequence of DNA methylation.
- *Two contradictions worth watching.* Imputation that enables per-cell clustering necessarily suppresses the cell-to-cell variability being measured, and neither scHiCluster nor Higashi quantifies the trade. And CellOracle's vector-field formulation structurally cannot represent proliferation or death, producing a documented false negative (Spi1 knockout erythroid depletion).

**Incomplete pages.** Two sources were clipped as metadata only and carry explicit source-caveat blocks: `welch-2019-liger` and `pliner-2018-cicero`. Both need a full-text re-clip before their Methods and Results sections can be written.

---

## 2026-08-10 — Ingest: 35 foundational & infrastructure papers (reference-gap fill)

**Trigger**: User audited three manuscript reference lists (114 unique refs) against the wiki, found 33 unbookmarked, saved them all, and asked for an ingest. Two previously-pending sources were swept in, for 35 total.

### Summaries created (35)

**Genome / WGA / variant calling (6)** — [[10-Summaries/telenius-1992-dop-pcr]] (DOP-PCR), [[10-Summaries/zong-2017-malbac-protocol]] (MALBAC protocol), [[10-Summaries/laks-2019-dlp-plus]] (DLP+, 51,926 amplification-free genomes), [[10-Summaries/mckenna-2010-gatk]] (GATK), [[10-Summaries/smukowski-heil-2023-loh]] (LOH), [[10-Summaries/eichler-2007-completing-sv-map]] (NHGRI SV proposal).

**3D genome (4)** — [[10-Summaries/naumova-2013-mitotic-chromosome]], [[10-Summaries/lupianez-2015-tad-disruption]], [[10-Summaries/spielmann-2018-sv-3d-genome]], [[10-Summaries/durand-2016-juicer]].

**Histone modifications (7)** — [[10-Summaries/bernstein-2006-bivalent-chromatin]], [[10-Summaries/rothbart-2014-histone-dna-language]], [[10-Summaries/heinz-2010-homer]], [[10-Summaries/roadmap-2015-111-epigenomes]], [[10-Summaries/kaya-okur-2019-cut-and-tag]], [[10-Summaries/wu-2021-sccut-tag]], [[10-Summaries/zhang-2022-sccut-tag-pro]], [[10-Summaries/gopalan-2022-multi-cut-and-tag]].

**DNA methylation (4)** — [[10-Summaries/jones-2012-dna-methylation-functions]], [[10-Summaries/tahiliani-2009-tet1-5hmc]], [[10-Summaries/kremer-2024-methscan]], [[10-Summaries/chen-2025-sctaps-sccaps-plus]], plus [[10-Summaries/flusberg-2010-smrt-methylation]] on the long-read side.

**Multi-omics & integration (6)** — [[10-Summaries/zhu-2020-multimodal-power-of-many]], [[10-Summaries/argelaguet-2021-integration-principles]], [[10-Summaries/hao-2024-seurat-v5]], [[10-Summaries/vandereyken-2023-spatial-multiomics]], [[10-Summaries/lim-2024-single-cell-omics-review]], [[10-Summaries/lake-2018-brain-snrna-scths]].

**Computational infrastructure (7)** — [[10-Summaries/mclean-2010-great]], [[10-Summaries/zhang-2021-chromap]], [[10-Summaries/traag-2019-leiden]], [[10-Summaries/mcinnes-2018-umap]], [[10-Summaries/gao-2021-copykat]], [[10-Summaries/tickle-2019-infercnv]].

### Graph touched (16 pages)

Concepts: [[30-Concepts/5hmc]], [[30-Concepts/taps]], [[30-Concepts/structural-variants]], [[30-Concepts/topologically-associating-domain]], [[30-Concepts/scwga-chemistries]], [[30-Concepts/cut-and-tag]], [[30-Concepts/scbs-seq]], [[30-Concepts/multimodal-integration-methods]], [[30-Concepts/enhancer-states]], [[30-Concepts/single-cell-variant-calling]].
Topics: [[40-Topics/dna-methylation]], [[40-Topics/3d-genome]], [[40-Topics/histone-modifications]], [[40-Topics/single-cell-multiomics]].
Notes: [[50-Notes/open-questions]] (new section — cross-cutting artifact confounds, untested method assumptions, biology left open, methods that do not exist).
Indexes: [[10-Summaries/index]] (+35 entries, count 190 → 225) and root [[index]].

### Notable findings

- **Four sources are metadata-only clippings** (DOP-PCR, MALBAC, UMAP, inferCNV are landing/abstract/README pages). Each summary carries an explicit source caveat; UMAP was never journal-published and inferCNV's README now opens with a deprecation notice redirecting to CopyKAT and Numbat.
- **Two prior wiki assumptions are now stale**: inferCNV is unsupported, and every bisulfite-based single-cell methylome in the corpus reports a 5mC+5hmC composite — a 22% confound in hippocampal neurons per scCAPS+.
- **Cell-line vs tissue aneuploidy** differs ~4–8× (5.2% vs 0.6–1.2%, DLP+); *TP53* loss reverses gain/loss direction without changing rate.
- **TADs are interphase-only** (Naumova), which reframes Lupiáñez boundary function as re-established every cycle and constrains what single-cell Hi-C can read from mitotic cells.
- **Three complementary multi-omics taxonomies** now coexist in the wiki: by throughput/depth (Zhu), by coupling mechanism (Vandereyken), by computational anchor (Argelaguet).

### Correction to the prior gap report

The reference-gap list given to the user before this ingest was **under-inclusive**. It matched DOIs anywhere in the wiki, so papers appearing only inside *other clippings' reference sections* counted as bookmarked. A stricter check (source-file title match) finds **~27 further references with no source file** — including SAMtools, BWA, fastp, MACS, SEACR, HiC-Pro, Cooler, HiGlass, Higashi, scHiCluster, Harmony, LIGER, Monocle3, PAGA, MEDALT, Cassiopeia, Cicero, CellOracle, SCENIC+, AneuFinder, Ginkgo(dup), Lieberman-Aiden 2009, Dixon 2012, Peric-Hupkes 2010, Alexandrov 2013, Zahn 2017 (DLP), Xu 2012, Ludwig 2019, Ramani 2017. Wikilinks to these were de-linked to plain text marked *(not bookmarked)* rather than left broken.

### Verified

- 0 pending sources (228 total source files); 0 broken wikilinks wiki-wide.

---

## 2026-06-29 — Draft: computational-framework-structure note (review main-section scaffold)

**Trigger**: User asked to draft the manuscript's computational-framework section after deciding (this session) not to mirror the 5-layer measurement frame.

### Page created (1)
- [[50-Notes/computational-framework-structure]] 🎯 — draft scaffold (not prose) for the paper's main section. Core argument: invert the 5-layer frame; organize computation by analysis task (shared substrate → layer-specific inference → cross-layer integration → frontier), climaxing in integration. Includes the **task × layer matrix** and a method-to-subsection mapping with 45 cited wiki pages (variant callers, chromVAR/cisTopic/scOpen/SCALE, DeepCpG/Melissa/scMET/Epiclomal, scChIX, MOFA+/MultiVI/GLUE/Cobolt/WNN, lähnemann grand-challenges). Tagged `draft` + `review-paper-anchor`.

### Existing pages touched
- [[50-Notes/index]] + root [[index]] Synthesis section — registered the new anchor note.

### Note
- Surfaced gap: accessibility & 3D layers still lack their own synthesis notes; 3D has thinner computational-tool coverage in the corpus (flagged as an open question in the draft).

---

## 2026-06-29 — Maintenance: organize 50-Notes (index + frontmatter standardization)

**Trigger**: User (writing the scDNA-seq review) felt 50-Notes was scattered; asked to tidy it before drafting the computational-framework note. Scope chosen: index + frontmatter standardization (no content merges); grouping by the paper's layer structure.

### Created
- [[50-Notes/index]] — new catalog (the folder lacked one; all other folders have it). Groups the 10 notes by the review's structure: **Cross-cutting framing** (regulatory-layers-overview, mosaicism-synthesis-gap, joint-assays-by-layer-pair) → **per-layer** (genetic: pta-inflection / single-cell-duplex / droplet-vs-single-molecule; methylation: methylation-cancer-classifiers; histone: mnase-vs-tn5; accessibility/3D: none yet, placeholder) → **meta/trackers** (synthesis-targets, open-questions). The two review-paper anchors flagged 🎯.

### Standardized
- Meta notes given descriptive titles + aliases: `Open Questions` → "Open questions — tensions and gaps by domain"; `Synthesis Targets` → "Synthesis targets — candidate cross-source syntheses".
- Deduped `sources:` arrays: methylation-cancer-origin-classifiers (kim-2017, smith-2013 ×2), mnase-vs-tn5 (klemm-2019 ×2), pta-inflection-point (evrony-2021, shao-2025 ×2).
- `updated: 2026-06-29` on the 5 touched notes.
- Root [[index]] "Browse the wiki" table: added a **Notes** row → [[50-Notes/index]] (was missing).

### Verified
- 10/10 notes catalogued; all index links resolve; 0 duplicate sources; 0 broken links wiki-wide.
- Note: the 3 genetic-layer notes (pta-inflection / single-cell-duplex / droplet-vs-single-molecule) overlap in scope but each holds a distinct angle (chronology / frontier-closing / breadth-depth) — kept separate, not merged.

---

## 2026-06-29 — Refactor: merge 9 concept/topic duplicate pairs into single Topic pages

**Trigger**: User: "merge the duplicate concept/topic pairs into single pages." Nine slugs existed as BOTH a `30-Concepts/` page and a `40-Topics/` page. User chose **merge-into-Topics** (survivor lives in `40-Topics/`, concept twin absorbed and deleted).

### Pairs merged (concept → topic survivor)
`3d-genome`, `clonal-hematopoiesis`, `dna-methylation`, `duplex-sequencing`, `histone-modifications`, `long-read-sequencing`, `scdna-seq`, `single-cell-multiomics`, `somatic-mosaicism`.

### Process
- **Content merge** (9 parallel agents, one per topic file): each rewrote `40-Topics/<slug>.md` to absorb ALL substantive content from the concept twin — definitions, mechanisms, examples, per-claim citations — deduped (not concatenated). Frontmatter kept `type: topic`; aliases/tags unioned (dropped awkward "X topic" placeholders); self-references to the deleted twin removed.
- **Link repointing** (central): every `[[30-Concepts/<slug>]]` and bare `[[<slug>]]` for the 9 → `[[40-Topics/<slug>]]`, wiki-wide (also fixes the cross-links the merged topic pages make to each other, and the root index "Start here" links).
- **Deleted** the 9 `30-Concepts/<slug>.md`; **pruned** their 9 lines from `30-Concepts/index.md`.
- Side effect: the concept/topic bare-link ambiguity (from the prior pass) is now structurally gone — one page per slug.

### Final state
- Concepts 169 → **160**; Topics **20** (unchanged count, survivors now richer: somatic-mosaicism 205 ln, single-cell-multiomics 191 ln, dna-methylation 148 ln, …).
- **0 broken links · 0 orphans · 0 self-links**; every survivor catalogued in `40-Topics/index.md`, concepts catalog complete (160/160).
- Note: shell is **zsh** — unquoted `$VAR` is NOT word-split in `for` loops; use `${=VAR}`. A first repoint attempt silently no-op'd because of this; redone correctly.

---

## 2026-06-29 — Maintenance: lint pass ("rinse the wiki")

**Trigger**: User said "rinse the wiki" — interpreted as a MAINTAIN lint pass. No new sources (0 pending of 193).

### Checks run
- **Broken links**: full-wiki sweep → **0 broken** (194 `source:` frontmatter links into `00-Sources/` all resolve; one apparent hit was the table-escaped `\|` pipe in the new Browse links, a regex artifact, not a real break).
- **Orphans**: 2 found, both linked in.
- **Index drift**: the three category catalogs were stale — 76 pages on disk missing from them.
- **Duplicates**: surfaced `g-t-seq.md` vs `gt-seq.md` (same method, both titled "G&T-seq") — **flagged for user, not merged**.

### Fixes (mechanical, no approval needed)
- **Orphans linked in**: [[20-Entities/jan-p-dumanski]] → added to [[10-Summaries/forsberg-2017-mosaicism-review]] (co-author) and [[40-Topics/somatic-mosaicism]]; [[10-Summaries/garrison-2023-bsmn-data]] → linked from [[40-Topics/brain-somatic-mosaicism]] consortium section.
- **Category catalog drift repaired** (via 3 parallel agents): [[20-Entities/index]] +37 entries (now 100/100), [[30-Concepts/index]] +33 (now 170/170), [[40-Topics/index]] +6 (now 20/20). All `updated:` bumped to 2026-06-29.
- **Root [[index]] refreshed**: stale "~130 papers" → "~190" (2 spots); "Browse the wiki" table cells (People/Concepts/Topics) were dead text → now link to the category catalogs; dates bumped.

### Follow-ups (user approved all three, same session)
- **Duplicate page merged**: consolidated `g-t-seq` + `gt-seq` (both titled "G&T-seq") into the canonical [[30-Concepts/gt-seq]] — kept gt-seq's slug but merged in g-t-seq's richer content (Macaulay 2015 original citation, trisomy-11/reversine-embryo/MTAP-PCDH7 biology, scNMT-seq lineage). Repointed all 8 inbound links, removed the duplicate catalog line, deleted `g-t-seq.md`. Now 20 files reference gt-seq; 0 g-t-seq refs remain.
- **Ambiguous bare links disambiguated**: 104 bare links across the 9 concept/topic slug pairs, all resolved to the **concept** page (`[[30-Concepts/<slug>]]`). Confirmed the wiki's standing convention — topic links always carry an explicit `[[40-Topics/...]]` prefix, so bare = concept. 0 ambiguous bare links remain.
- **Papers catalog created**: [[10-Summaries/index]] — 194 entries (1:1 with summary files), 16 thematic sections mirroring the Concepts/Topics catalogs. Root index Browse table's "Papers" cell now links to it. All four content categories now have complete catalogs.

### Final state
- Broken links: **0** (full-wiki sweep). Catalogs: Summaries 194/194, Entities 100/100, Concepts 170/170 (after merge), Topics 20/20. Ambiguous bare links: **0**. Orphans: **0**.

## 2026-06-26 — Synthesis: joint-assays-by-layer-pair note (review draft anchor)

**Trigger**: User drafting the review's joint-assay subsection; asked to capture the layer-pair organization in the wiki. Companion to the same-day D&D-seq/ResolveOME ingest.

### Page created (1)

- [[50-Notes/joint-assays-by-layer-pair]] — joint single-cell assays cataloged by which layer-pair they bridge (genotype-anchored first), climaxing on Duplex-Multiome; names the unmet SNV+methylation configuration and bridges to the computational problem. Per-claim inline citations.

### Existing pages touched

- [[index]] — added to Synthesis & open threads; updated regulatory-layers description to "five (or six) axes" with the TF-binding axis named.
- [[40-Topics/single-cell-multiomics]] — replaced the empty "Synthesized notes" placeholder with the new note.
- [[50-Notes/regulatory-layers-overview]], [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]] — cross-linked as methodological-integration companion.

### Decision recorded

- Review keeps a **5-layer** locus-state framework (genetic / accessibility / methylation / chromatin-state / 3D). TF/DNA-protein binding folds into the chromatin-state layer (protein occupancy), not a sixth axis — D&D-seq lives there. The wiki's regulatory-layers note retains the broader six-axis exposition for reference; the two are reconciled by treating TF occupancy as a sub-component of chromatin state.

## 2026-06-26 — Ingest: 2 new clippings (D&D-seq DNA–protein axis + ResolveOME genome+RNA)

**Trigger**: User added two papers via Obsidian and said "ingest new clipping." `tools/pending-sources.sh` found 2 pending of 193 sources. Context: this followed a literature-currency check (PubMed/web) of the user's review framework, which surfaced D&D-seq and ResolveOME as the two most framework-relevant new methods.

### Sources ingested

- [[10-Summaries/chi-2026-dd-seq]] — D&D-seq: nanobody-deaminase footprinting of DNA–protein interactions in single cells; D&D-GoT-ChA adds genotype + TF binding (Cell 2026; Landau lab). DOI 10.1016/j.cell.2026.05.014.
- [[10-Summaries/marks-2023-resolveome]] — ResolveOME: PTA whole-genome + full-transcriptome same-cell; AML quizartinib resistance + breast cancer PIK3CA (bioRxiv 2022/2023; West/Gawad, BioSkryb). DOI 10.1101/2022.04.29.489440.

### Pages created (4)

- **Concepts (2)**: [[30-Concepts/dd-seq]], [[30-Concepts/resolveome]].
- **Entity (1)**: [[20-Entities/jay-a-a-west]] (ResolveOME corresponding author, BioSkryb).
- Plus the 2 summaries above.

### Existing pages touched (graph weave)

- [[50-Notes/regulatory-layers-overview]] — **added a fifth molecular axis: DNA–protein (TF) binding** (D&D-seq). Retitled "four (or five)" → "five (or six)"; structural/physical became the sixth axis. Updated quick-map table.
- [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]] — added two rows to the cross-domain framing table (D&D-GoT-ChA targeted SNV+TF binding; ResolveOME genome-wide SNV+RNA); marked two "closest hypothetical combinations" as now realized.
- [[30-Concepts/got-cha]] — added D&D-GoT-ChA variant + Related link.
- [[30-Concepts/scdna-capabilities-framework]] — added ResolveOME + D&D-GoT-ChA rows to the capability table.
- [[40-Topics/single-cell-multiomics]] — added two new method sub-themes, concept links, entity.
- [[20-Entities/dan-a-landau]], [[20-Entities/franco-izzo]] — D&D-seq mentions (GoT → GoT-ChA → D&D-GoT-ChA trajectory).
- [[20-Entities/charles-gawad]] — ResolveOME mention.
- [[index]] — added both under Multi-Omics Joint Assays; new "Genotype + TF binding" line.

### Notable findings / tensions

- **D&D-seq directly supplies the "sixth axis" the prior literature-check recommended** — DNA-protein/TF occupancy, readable in *closed* chromatin (which scATAC misses). It is the mechanistic bridge between a mosaic mutation in a TF motif and downstream accessibility/expression change.
- **D&D-GoT-ChA and ResolveOME both narrow the synthesis gap further** but neither adds methylation; the SNV+methylation genome-wide same-cell configuration remains unmet (bisulfite C→T conflict persists).
- Both are from labs already central to the wiki (Landau; Gawad/PTA lineage) — tight graph integration, no orphans.

## 2026-06-02 — Ingest: 6 new clippings (scATAC imputation + joint DNA-RNA + lineage-tracing reviews)

**Trigger**: User said "ingest new clippings." `tools/pending-sources.sh` found 6 pending of 191 sources.

### Sources ingested

- [[10-Summaries/li-2021-scopen]] — scOpen: regularized NMF imputation for scATAC-seq (Nat Commun; Costa lab).
- [[10-Summaries/xiong-2019-scale]] — SCALE: VAE + Gaussian Mixture Model for scATAC-seq (Nat Commun; Q.C. Zhang lab).
- [[10-Summaries/olsen-2025-defnd-seq]] — DEFND-seq: scalable droplet whole-genome + RNA via nucleosome depletion on 10x Multiome (Nat Methods; Sims lab).
- [[10-Summaries/lindenhofer-2025-sdr-seq]] — SDR-seq: targeted Tapestri DNA + RNA, low ADO, variant phenotyping (Nat Methods; Steinmetz lab).
- [[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]] — lineage-tracing *technologies* review (Nat Rev Genet 2026).
- [[10-Summaries/wang-2026-multimodal-lineage-computational]] — lineage-tracing *computational* review (Nat Rev Genet 2026).

### Pages created (16)

- **Concepts (7)**: [[30-Concepts/scopen]], [[30-Concepts/scale]], [[30-Concepts/scatac-imputation]] (hub), [[30-Concepts/defnd-seq]], [[30-Concepts/sdr-seq]], [[30-Concepts/crispr-lineage-recording]], [[30-Concepts/phylogenetic-inference]].
- **Topic (1)**: [[40-Topics/single-cell-lineage-tracing]] (new backbone topic; static/evolvable × prospective/retrospective taxonomy).
- **Entities (7)**: [[20-Entities/ivan-costa]], [[20-Entities/qiangfeng-cliff-zhang]], [[20-Entities/peter-a-sims]], [[20-Entities/lars-steinmetz]], [[20-Entities/oliver-stegle]], [[20-Entities/alejo-rodriguez-fraticelli]], [[20-Entities/zheng-hu]].
- Plus the 6 summaries above.

### Existing pages touched (graph weave)

- [[30-Concepts/scatac-seq]] — added imputation note + Related links.
- [[30-Concepts/cistopic]] — noted cisTopic-impute is the imputation baseline scOpen/SCALE beat.
- [[30-Concepts/joint-single-cell-multi-omics]] — added DEFND-seq/SDR-seq breadth-vs-depth (ADO) variant.
- [[30-Concepts/got]] — SDR-seq generalizes genotyping-of-transcriptomes to direct gDNA readout.
- [[30-Concepts/pta]] — added ResolveOME/SMART-PTA joint WGS+RNA + DEFND-seq benchmark.
- [[30-Concepts/lineage-tracing]] — added synthetic/CRISPR + multimodal/computational branches and the two reviews.
- [[30-Concepts/mitochondrial-lineage-tracing]] — added caveats + method summaries + topic link.
- [[30-Concepts/methylation-clones-epimutation]] — added the methylome-beats-ATAC/RNA cross-modal claim.
- Topics [[40-Topics/single-cell-atac-seq]] and [[40-Topics/single-cell-multiomics]] — added new methods + sources.
- [[index]] — added new sources/concepts/topic across three sections.

### Notable findings / tensions

- **scATAC imputation is contested**: scOpen (NMF) reports beating SCALE (deep) on AUPR + memory; SCALE's edge is interpretability and batch-effect detection. Whether imputation clarifies or hallucinates remains an open methods question.
- **Breadth vs depth in joint DNA-RNA** mirrors the existing droplet-vs-single-molecule note: DEFND-seq = whole-genome but >90%+ ADO; SDR-seq = targeted but ~90% allele recovery (per-cell zygosity). Logged into [[50-Notes/droplet-vs-single-molecule-scdna]] family.
- The two NRG 2026 reviews are an explicit technology/algorithm pair (each cites the other); they anchor the new [[40-Topics/single-cell-lineage-tracing]] topic.
- Rodriguez-Fraticelli claims the **methylome outperforms ATAC and RNA for clonal inference** against ground-truth barcodes — a strong, trackable claim now flagged on [[30-Concepts/methylation-clones-epimutation]].

### Verification

- All wikilinks in the 6 summaries + 16 new pages + edited hubs verified to resolve (0 broken). Fixed 2 self-introduced typos pre-commit (`got.md` link, `scite` concept link).

---

## 2026-05-29 — Off-topic move + dedup sweep (9 duplicate summaries collapsed)

**Trigger**: User asked "anything else you missed?" after the prior pending-burndown session. Audit surfaced:
- 2 off-topic papers still in `00-Sources/papers/` (Collateral sensitivity E. coli, FoldPAthreader protein folding)
- 1 broken `source:` link in canonical `forsberg-2017-mosaicism-review.md` (pointed at non-existent `Lars_2017_NatureReviewsGenetics`)
- 1 stray `.moai/` directory inside `00-Sources/papers/` (MoAI session-memo artifact)
- **9 duplicate-summary pairs** (same paper, two different slugs)
- 1 mis-named summary (`hsieh-2026-mtdna-mosaicism.md` actually contained Glynos 2023 content)

### Actions

- Moved off-topic clippings to new `99-OffTopic/` directory; added to `.gitignore`.
- Fixed canonical Forsberg source: link to point at actual clipping.
- Removed stray `00-Sources/papers/.moai/` directory.
- Renamed misnamed file: moved `hsieh-2026-mtdna-mosaicism.md` (Glynos content) into `glynos-2023-mtdna-mosaicism.md` (which existed as a thinner stub); deleted the misnamed file; redirected 5 inbound refs.
- **Deleted the duplicate `forsberg-2017-mosaicism-clones.md` I created in part 1** (canonical `forsberg-2017-mosaicism-review.md` already existed; I missed it because the canonical's source: link was broken so pending-sources couldn't see the coverage).
- **8 additional dedup pairs collapsed** (kept richer/canonically-named file in each):

| Kept | Deleted |
|------|---------|
| luquette-2025-pta-duplex-mosaicism | luquette-2025-smaht-pta |
| tu-2021-scout-genotyper | tu-2021-scout |
| kim-2017-methylation-memory-review | kim-2017-dna-methylation-memory |
| mezger-2018-microfluidic-atac | mezger-2018-uatac |
| shen-2026-splicool-seq | shen-2025-splicool-seq |
| liu-2025-nanopore-lscc-svs | liu-2025-somagauss-lscc |
| liu-2025-long-read-epigenome-review | liu-2025-longread-epigenome-review |
| campbell-2015-mosaicism-review | ian-2015-trendsingenetics (content copied into canonical slug) |

### One ambiguous pair flagged for manual review

`zhao-2022-nature.md` and `morriss-2024-spatial-genomics-clonal.md` both point at the same source clipping ("Spatial genomics enables multi-modal study of clonal heterogeneity in tissues"), but Zhao 2022 (Nature) is the original Slide-DNA-seq paper while Morriss 2024 may be a follow-up (Slide-tags?). **One of them is misattributed**, but without checking the source clipping itself it's unclear which to keep. Left both for now.

### Pre-existing tech debt surfaced (not fixed this session)

- **343 broken wikilinks wiki-wide**, concentrated in: `catalog.md` (159 — uses obsolete first-name slug convention from before the great rename), `graphify-out/GRAPH_REPORT.md` (142 — auto-regenerates), and template files in `90-Meta/templates/` (~30 — template placeholders, expected). None caused by this session's edits.
- Recommend a focused lint pass to either regenerate `catalog.md` from current summaries or fix its slug references.

### Final state

- **0 pending** of 185 sources covered
- **186 summaries** (was 195+ with duplicates)
- 99-OffTopic/ holds 2 off-topic clippings

---

## 2026-05-27 (part 2) — pending-sources.sh fixed; backlog burn-down (187 → 2 pending)

**Trigger**: User flagged that 187 pending sources contradicted the "all ingested" claim. Re-audit revealed the legacy `tools/pending-sources.sh` produced 174 false positives by slug-matching filenames; only 13 were genuine, of which 6 turned out to be naming/frontmatter mismatches and 4 were truly missing on-topic ingests.

### Script fix

- Rewrote `tools/pending-sources.sh` to walk summary frontmatter `source:` links by basename rather than slugifying source filenames. Skips hidden directories (e.g. stray `.moai/`).
- Result: pending count drops from 187 → 8 immediately, then → 6 after 4 frontmatter fixes, then → 2 after 4 ingests. The 2 remaining are off-topic (Collateral sensitivity E. coli, FoldPAthreader protein folding) — awaiting user decision on whether to ingest, move out of 00-Sources, or annotate as off-scope.

### Frontmatter `source:` mismatches fixed (no new content — same paper, wrong link)

- `10-Summaries/chenghang-2012-science.md` — Zong/MALBAC 2012 paper now correctly points at `Genome-Wide Detection of Single-Nucleotide and Copy-Number Variations of a Single Human Cell.md`.
- `10-Summaries/andrewc-2020-science.md` — IGS paper now correctly points at `In situ genome sequencing resolves DNA sequence and structure in intact biological samples.md`.
- `10-Summaries/nam-2019-got.md` — GoT paper now correctly points at `Somatic mutations and cell identity linked by Genotyping of Transcriptomes.md`.
- `10-Summaries/ghorbani-2019-comp-epigenetics.md` — review now correctly points at `Computational-based approaches in epigenetic research...md`.
- `10-Summaries/izzo-2024-got-cha.md` — GoT-ChA paper now correctly points at `Mapping genotypes to chromatin accessibility profiles in single cells.md`.
- `10-Summaries/geisenberger-2025-scepi2-seq.md` — **had wrong source link entirely** (pointed at the SIMPLE-seq clipping; the SIMPLE-seq paper is covered by `bai-2024-simple-seq.md`). Fixed to point at `Single-cell multi-omic detection of DNA methylation and histone modifications...md`.

### New summaries ingested

- **[[10-Summaries/forsberg-2017-mosaicism-review]]** — Forsberg, Gisselsson & Dumanski 2017 NRG review. Structural-variant-centric framing of somatic mosaicism; ACE terminology; LOY as the most common human post-zygotic mutation; revertant mosaicism in Turner syndrome.
- **[[10-Summaries/hilal-2026-cardiac-somatic-review]]** — Hilal, Arava & Choudhury 2026 Circ Res. Cardiovascular somatic-variation review; cardiomyocyte 4–30k SNVs/cell; CHIP→HFpEF/stroke; duplex-sequencing toolbox catalog (TwinStrand, NanoSeq, CODEC, META-CS, Pro-Seq, BotSeqS).
- **[[10-Summaries/hsieh-2026-scmtmpm-scwmss]]** — Hsieh/Lareau/Ludwig 2026 Nat Comm. Introduces scmtMPM + scwMSS metrics for per-cell mtDNA mutational burden via mtscATAC-seq; pathogenic mtDNA variants held at sub-threshold VAF by negative selection in POLG hypermutators; MELAS m.3243A>G purifying selection with age.
- **[[10-Summaries/doughty-2024-single-molecule-chromatin-config]]** — Doughty/Bintu/Greenleaf 2024 bioRxiv. **Abstract-only ingest** (clipping is references-only); placeholder summary noting full-text re-read needed.

### Entities created

- `20-Entities/sangita-choudhury.md` (Hilal review corresponding author)
- `20-Entities/leif-ludwig.md` (Hsieh paper co-corresponding author, mtscATAC-seq co-developer)

### Notable findings / tensions

- **Existing file misnamed:** `10-Summaries/glynos-2023-mtdna-mosaicism.md` actually contains the **Glynos 2023** paper (Science Advances), not Hsieh 2026. The new Hsieh summary uses the distinct slug `hsieh-2026-scmtmpm-scwmss.md` to avoid collision. The misnamed file should be renamed `glynos-2023-mtdna-heteroplasmy.md` in a future lint pass (requires updating inbound links).
- **Bi & Weng review's missing axis:** confirmed via Hilal 2026 ingest that the dominant 2023–2024 multiomics reviews (Bi & Weng, Baysoy, Vandereyken, Wang) all omit the cardiac-resident mosaicism axis. The wiki now has both the blood-centric (Forsberg) and cardiac-centric (Hilal) reviews on this axis.
- **Forsberg 2017 framing largely lost the war:** structural-variant-centric mosaicism framing (LOY, CNVs as dominant) was correct at the cell-burden level but the 2018+ CHIP/SNV literature dominated subsequent discourse. Worth a synthesis note connecting Forsberg's framing to the duplex-sequencing-enabled SNV revolution of 2021+.
- **2 off-topic sources remain in `00-Sources/papers/`:** Collateral sensitivity (E. coli antibiotic resistance) and FoldPAthreader (protein folding). User decision needed: ingest as off-scope stubs, move out of sources, or leave pending.

### Graph touch count

This session: 18 files (6 new summaries, 2 new entities, 6 frontmatter fixes on existing summaries, 5 concept/topic touches, index, log, script).

---

## 2026-05-27 — Ingest: Creyghton 2010 (H3K27ac/enhancers) + Bi & Weng 2024 (multiomics review)

**Trigger**: Two new clippings dropped into `00-Sources/papers/`.

### Sources ingested

1. **Creyghton et al. 2010, PNAS** — *Histone H3K27ac separates active from poised enhancers and predicts developmental state.* Foundational ChIP-seq paper establishing H3K27ac as the discriminating mark between active and poised (= modern "primed") enhancers across mESC/NPC/proB/liver/iPS, and showing iPS reprogramming resets the enhancer landscape (Pearson 0.81 vs ES).
2. **Bi & Weng 2024, Fundamental Research** — *Single-cell epigenomics and proteomics methods integrated in multiomics.* Methods-catalog review organized by integration topology (horizontal/vertical/diagonal, Argelaguet frame) and protein-quantification lineage (NGS vs scMS). Overlaps heavily with the existing Baysoy/Vandereyken/Wang trio; main differentiator is the explicit CRISPR-perturbation family treatment and the named integration-topology taxonomy.

### Pages created

- `10-Summaries/creyghton-2010-h3k27ac-enhancers.md`
- `10-Summaries/bi-2024-multiomics-review.md`
- `20-Entities/rudolf-jaenisch.md` (corresponding author, Creyghton paper)
- `20-Entities/richard-a-young.md` (co-author; later super-enhancer concept builds on this framework)
- `20-Entities/menno-p-creyghton.md` (first author, Creyghton paper)
- `20-Entities/xiaocheng-weng.md` (corresponding author, Bi review)

### Pages updated

- `30-Concepts/enhancer-states.md` — added Creyghton 2010 as foundational source; explicit terminology-drift note that Creyghton's "poised" = modern "primed" (only 1.2% of his enhancers carried H3K27me3, so his class was not bivalent).
- `30-Concepts/histone-modifications.md` — cited Creyghton 2010 against H3K4me1 and H3K27ac canonical-mark entries.
- `30-Concepts/multimodal-integration-methods.md` — added Argelaguet horizontal/vertical/diagonal taxonomy from Bi 2024 to the paired/unpaired section.
- `40-Topics/single-cell-multiomics.md` — added Bi & Weng to the Reviews list.
- `index.md` — added enhancer-state pointer under scATAC section; added Bi & Weng to Multi-Omics review row; bumped updated date.

### Notable findings / tensions

- **Terminology drift (poised vs primed).** Creyghton 2010 used "poised" for H3K4me1+/H3K27ac− but found near-zero H3K27me3 enrichment, so his class is what the field later renamed "primed". The wiki's `enhancer-states` page already used the modern convention — now annotated with the historical source.
- **Bi review misses the scDNA-anchored multiomics axis.** Like the rest of the 2023–2024 review cluster, it does not include GoT / GoT-ChA / DAF-seq / Duplex-Multiome under "multiomics" — consistent with the wiki's central [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap|synthesis-gap thesis]].
- **Bi 2024 source frontmatter is mangled** (author list contains abstract fragments; no published date). Corrected in the summary frontmatter manually using DOI lookup.

### Graph touch count

11 files written/edited (2 summaries + 4 entities + 4 wiki pages + index).

---

## 2026-05-19 (part 8) — Methylation cancer-of-origin synthesis written; synthesis-target set complete

**Trigger**: Final synthesis-targets candidate — completes the set of 5.

### Note created

- **[[50-Notes/methylation-cancer-origin-classifiers]]** — EPICUP for CUP, Heidelberg MNP for brain tumors, emerging AML methylation classifiers. Argues clinical methylation classifiers exploit *epigenetic memory* — the property that tissue-of-origin methylation patterns survive tumorigenesis. Three reasons methylation outperformed alternatives: stability through tumorigenesis, per-CpG measurement granularity, FFPE compatibility + microarray maturity head start.
- **Explicit caveat**: this is the weakest of the 5 synthesis notes because the primary classifier papers (Moran 2016 *Lancet Oncology* for EPICUP; Capper 2018 *Nature* for MNP) are not yet ingested. Specific claims trace through Kim 2017 review rather than primary sources. Flagged for follow-up ingest.
- 49 wikilinks, 0 broken. 8 source summaries cited.

### Synthesis-targets backlog status

All 5 of the originally-listed candidates resolved (2026-05-19). New candidates added to synthesis-targets.md: spatial multi-omics, mtDNA mosaicism as lineage marker, single-molecule TF footprinting.

### Cumulative session output

- 5 substantive synthesis notes (regulatory-layers, single-cell-duplex, droplet-vs-single-molecule, pta-inflection-point, mnase-vs-tn5, methylation-cancer-origin).
- 22 stub pages.
- ~14 wiki pages upgraded to inline-citation density.
- Graphify rerun (1805 nodes, 142 communities).
- Quartz build broken-and-fixed (duplicate YAML keys).
- Wiki-wide broken-link cleanup (882 → 157).

---

## 2026-05-19 (part 7) — MNase vs Tn5 chromatin chemistry synthesis written

**Trigger**: 4th synthesis-targets candidate after PTA inflection.

### Note created

- **[[50-Notes/mnase-vs-tn5-chromatin]]** — compares the two single-cell histone-profiling chemistry lineages: MNase-tethered cleavage (Drop-ChIP / scChIC / sortChIC / scChIX / scEpi²) vs Tn5-tethered tagmentation (scCUT&Tag / nano-CUT&Tag / sciCUT&Tag / MulTI-Tag / 6-base-CUT&Tag). Quantitative table across 11 properties + chemistry-choice heuristic indexed by secondary measurement requirement.
- Key insight: the chemistry choice should follow the *secondary* readout. MNase pairs more naturally with TAPS methylation; Tn5 pairs with 10x Multiome ecosystem and enzymatic 5mC/5hmC. The decision is rarely about MNase vs Tn5 in isolation.
- 72 wikilinks, 0 broken. 10 source summaries cited.

### Meta-note updates

- `synthesis-targets.md`: MNase vs Tn5 target struck out.
- `index.md`: linked under Synthesis & open threads.

### Synthesis targets remaining

1 of 5 left: methylation-based cancer-of-origin classifiers.

---

## 2026-05-19 (part 6) — PTA inflection point synthesis written

**Trigger**: Continuing through synthesis-targets candidates after the droplet-vs-single-molecule note.

### Note created

- **[[50-Notes/pta-inflection-point]]** — pre-2020 MDA-era limitations → PTA chemistry (Gonzalez-Pena 2021) → SMaHT/BSMN-scale applications. Quantitative before/after table (coverage uniformity, allelic balance, per-cell genome coverage, FP rate). Frames PTA as a case study in how upstream chemistry improvements unlock orders-of-magnitude expansion of routine questions.
- Key reframe: PTA solved the *amplification noise* problem; Duplex-Multiome later solved the *strand-identity* problem. Orthogonal axes, both required for the modern mosaicism + epigenome workflow.
- 69 wikilinks, 0 broken. 16 source summaries cited.

### Meta-note updates

- `synthesis-targets.md`: PTA inflection target struck out.
- `index.md`: linked under Synthesis & open threads.

### Synthesis targets remaining

2 of 5 to go: MNase vs Tn5 chromatin profiling, methylation-based cancer-of-origin classifiers.

---

## 2026-05-19 (part 5) — Droplet vs single-molecule synthesis written

**Trigger**: Continued working through synthesis-targets.md candidates. Picked "Droplet-scale vs single-molecule scDNA-seq" because it mirrors the breadth-vs-depth tension central to the user's mosaicism × epigenome research.

### Note created

- **[[50-Notes/droplet-vs-single-molecule-scdna]]** — argues the gap is sustained by *physical* constraints (microfluidic compartmentalization destroys per-fiber context; single-molecule sequencing throughput-limited by ZMW/pore count), not by engineering. Quantitative comparison table (GoT-ChA vs scDAF-seq across 9 properties). Lists three candidate paths to close the gap (high-throughput Revio scDAF-seq, ONT combinatorial barcoding, droplet single-molecule hybrid) — none currently published.
- 84 wikilinks, 0 broken. 15 source summaries cited.
- Per inline-citation convention.

### Meta-note updates

- `synthesis-targets.md`: "Droplet-scale vs single-molecule scDNA-seq" struck out — promoted to full synthesis.
- `open-questions.md`: scDAF-seq vs GoT-ChA question and DLP+ vs PTA question both now point to the synthesis.
- `index.md`: new note linked under Synthesis & open threads.

### Surfaced insight

The breadth-depth tradeoff is the *root cause* of the [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap|mosaicism × epigenome synthesis gap]]. Resolving it would resolve the synthesis gap. The duplex synthesis ([[50-Notes/single-cell-duplex-sequencing]]) and this synthesis describe orthogonal axes of the scDNA-seq tradeoff space: fidelity (duplex) and depth-per-cell (this note).

### Synthesis targets remaining

3 of 5 candidates done. Remaining: MNase vs Tn5 chromatin profiling, PTA inflection point, methylation-based cancer-of-origin classifiers.

---

## 2026-05-19 (part 4) — Single-cell duplex synthesis written

**Trigger**: After resolving wiki broken-link backlog, the next concrete value-add was a synthesis note. The wiki's own `synthesis-targets.md` listed "Single-cell duplex sequencing" as "the major open methodological frontier"; the 2025 inflection (Duplex-Multiome + Luquette PTA-duplex pairing) made this synthesis newly tractable.

### Note created

- **[[50-Notes/single-cell-duplex-sequencing]]** — explains the 13-year duplex/scWGA incompatibility (strand identity vs amplification), the four duplex implementation strategies, PTA as the substrate for the SMaHT mosaicism workflow, and how 2025 closed the gap from two directions: PTA + bulk-duplex validation ([[10-Summaries/luquette-2025-pta-duplex-mosaicism]]) and same-molecule Duplex-Multiome ([[10-Summaries/kriz-2025-duplex-multiome]]).
- 67 wikilinks, 0 broken.
- Uses inline-citation density per the CLAUDE.md convention.

### Meta-note updates

- `synthesis-targets.md`: "Single-cell duplex sequencing" struck out — promoted to full synthesis.
- `open-questions.md`: "Single-cell + duplex" entry resolved, downgraded to sub-questions (Duplex-Multiome generalization, methylation-layer absence, cross-method single-cell duplex benchmark).
- `index.md`: new note linked under Synthesis & open threads.

### Open question surfaced

- The methylation layer is still missing from single-cell duplex. Duplex-Multiome reads accessibility + RNA + mutations. Closing this would give all four [[50-Notes/regulatory-layers-overview|regulatory layers]] — a concrete next-method opportunity.

---

## 2026-05-19 (part 3) — Citation upgrade + broken-link cleanup + stub pages

**Trigger**: User asked to upgrade wiki pages with inline citation per claim, then to incorporate the result into a clean wiki state.

### Citation pilot + convention (commit 9fd8f39)

- 3 high-traffic concept pages upgraded with inline `wiki link` per claim: `dna-methylation`, `lamina-associated-domains`, `chromatin-accessibility`. 130 wikilinks, 0 broken.
- CLAUDE.md updated: concepts/topics/notes now require sentence-level citation granularity (bullets cited individually, table cells cited per row, bare claims marked `(synthesis)` when no source).

### Quartz fix (commit 5b2ec90)

- 155 summaries had duplicated `source:` YAML keys from an earlier remap. Scripted dedup; Quartz builds again.

### Citation batch 2 (commit 71d23b4)

- 11 more pages upgraded by hand: concepts (somatic-mosaicism, histone-modifications, atac-seq, duplex-sequencing, 3d-genome) and topics (3d-genome, dna-methylation, histone-modifications, long-read-sequencing, duplex-sequencing, somatic-mosaicism). All verified clean.
- Bulk slug remap (24 entries) across 102 files to repair long-form summary slugs from the May 18 source-path remap.

### Broken-link cleanup (commit 5c979dc)

- 28-entry remap (auto-matched via title/alias Jaccard + manual overrides). Wiki-wide broken-link count: 882 → 248. Remaining 248 were genuine content gaps.

### Stub pages (commit 3f3c826)

- 22 stubs created for the most-frequently-referenced missing entities/concepts/topics:
  - Entities: Nicholas Navin, Joseph Ecker, Jay Shendure, Wolf Reik, Evan Macosko, Steven McCarroll, Aviv Regev, David Bennett, Alicia Schep
  - Concepts: joint-single-cell-multi-omics, multimodal-integration-methods, scwga-chemistries, methylation-clones-epimutation, genosenium, lineage-tracing-somatic-mutations, single-cell-variant-calling, strand-seq
  - Topics: mosaic-variant-calling, scdna-cancer-applications, clonal-hematopoiesis, brain-somatic-mosaicism, cancer-clonal-evolution
- Broken-link count: 248 → 157.

---

## 2026-05-19 (part 2) — Graphify rerun

**Trigger**: User asked to rerun graphify after May 19 ingests.

- Full incremental update: 690 doc/paper files, 32 chunks dispatched in parallel.
- Final graph: 1805 nodes, 3461 edges, 142 communities. 60 communities hand-labeled.
- New hyperedges: `hyper_locus_state_layers` (regulatory-layers note registers as a four-layer hub), `he_llps_chromatin_cancer` (biophysics cluster), brain-mosaicism cluster.
- Top god nodes: somatic mosaicism (65 edges), DNA methylation (54), scATAC-seq (46), single-cell multi-omics (41).

---

## 2026-05-19 — Regulatory-layers note + ingest 2 new clippings

**Trigger**: User asked whether regulatory interpretation has 4 layers (accessibility, methylation, histone marks, 3D genome). Confirmed; wrote synthesis note. Then user asked to ingest new clippings.

### Synthesis note created

- **[[50-Notes/regulatory-layers-overview]]** — entry point mapping the four molecular layers (accessibility / methylation / histone marks / 3D genome) plus a fifth structural-physical axis (lamina / phase separation / mechanics) to their concept pages and single-cell assays. Cross-layer dependency table; temporal/heritability table; methods-by-layer table. Synthesis flags relationships (synthesis tag) where not directly sourced.

### Ingested 2 new clippings (May 19 source files)

- **[[10-Summaries/van-steensel-2017-lads-review]]** — van Steensel & Belmont 2017 *Cell*. Canonical LAD review. Articulates cLAD/fLAD distinction, multivalent/redundant anchoring (multiple H3K9 methyltransferases, multiple NL proteins), three-compartment competition (NL/nucleoli/pericentromeric), and the tug-of-war model of LAD borders. **Key claim**: NL contact alone is probably *not* sufficient for repression — the heterochromatin compartment is what silences.
- **[[10-Summaries/wang-2023-multimodal-review]]** — Wang/Wu/Hong/Jin 2023 *Biophysical Reviews*. Methods catalog + integration-tool taxonomy. Notable for the "3-modality ceiling" prediction (already being broken by DOGMA-seq, Duplex-Multiome) and for the information-extraction angle (mono-omics data contains hidden additional modalities).

### Pending sources skipped (already ingested under different slugs)

Found 4 May 18 PDFs that the slug-based pending-sources.sh flagged but which were already ingested under author-year slugs: gibson-2019-chromatin-llps, ahn-2021-llps-cancer-looping, daugird-2024-viscoelastic-chromatin, qi-zhang-2021-nucleoli-coalescence. Maintenance note: tools/pending-sources.sh is stale relative to the May 18 remap; needs updating to handle author-year slugs (deferred).

### Graph touches (8 pages updated/created)

- Created entity pages: [[20-Entities/bas-van-steensel]], [[20-Entities/andrew-s-belmont]], [[20-Entities/wenfei-jin]]
- Updated [[30-Concepts/lamina-associated-domains]] — added van Steensel 2017 as canonical source; added Open questions section (cLAD/fLAD continuous-vs-categorical, three-compartment competition, laminopathy mechanisms)
- Updated [[40-Topics/chromatin-architecture]] — added van Steensel 2017 to Nuclear lamina lineage
- Updated [[40-Topics/single-cell-multiomics]] — added Wang 2023 to Reviews
- Updated [[index]] — added LADs review to Lamina lineage; added Reviews line to Multi-Omics Joint Assays; added regulatory-layers note to Synthesis section

### Open questions surfaced

- cLAD/fLAD: categorical or just tails of one distribution? Single-cell DamID suggests continuous.
- Three-compartment competition (NL/nucleoli/pericentromeric): if any heterochromatin compartment is sufficient for silencing, mosaic mutations that *shift* between compartments wouldn't change regulation — but mutations that disrupt anchoring entirely would. Empirically untested.
- For mosaicism interpretation: which regulatory layer is most informative if you can only measure one? Accessibility (Duplex-Multiome's bet) or methylation (stable cellular memory)?

---

## 2026-05-18 (part 3) — Deep re-ingest 4 biophysics papers (PDFs arrived)

**Trigger**: User dropped the 4 missing biophysics PDFs (converted to .md) — Gibson 2019, Ahn 2021, Daugird 2024, Qi & Zhang 2021. These were previously abstract-only ingests.

### Deep re-ingest

All 4 summaries rewritten with **verbatim quotes from source body** (Introduction + Results), replacing the prior abstract-only content. Each paper's claims now have direct supporting quotes that can serve as references in the user's writing.

- **Gibson et al. 2019** *Cell* — chromatin LLPS, H1 + linker length tuning, p300 dissolution, BRD4 immiscible phase. Highlights extracted; "10n+5 bp nucleosome spacing strongly favors phase separation" quoted; immiscibility quote "associate but do not coalesce" extracted.
- **Ahn et al. 2021** *Nature* — NUP98-HOXA9 LLPS-driven leukaemogenesis. Quantitative loop counts (232 N-IDR_WT-specific, 91% LLPS-anchored, 31% CTCF-overlap) extracted; FUS-IDR substitution + Phe→Ser mutagenesis evidence; single-molecule tracking confirmation.
- **Daugird et al. 2024** *Nat Commun* — direct quote "viscoelastic properties and accessibility of the interchromatin space remain constant" (THE money-quote for the user's locus-state mechanical sub-axis). Anomalous α ≈ 0.8 (~viscous liquid), fractal dimension 2.14–2.85, nuclear periphery as distinct biophysical environment.
- **Qi & Zhang 2021** *Nat Commun* — Hi-C polymer model with explicit nucleolar particles + NADs. Entropic barrier ~7 k_B T quantified; coarsening exponent 0.51 matches experiment; nucleation-and-arrest mechanism articulated.

### Ingest-depth field upgraded

All 4 frontmatters: `ingest_depth: abstract-only` → `ingest_depth: full-intro` or `full-intro+results`. Sources now point to the 4 new descriptive .md extracts in `00-Sources/papers/`.

### Cross-axis synthesis insight (carried over from earlier note)

These 4 papers together complete the **mechanical / phase-separation / viscoelastic** sub-axis of the DNA locus state framework:
- Gibson 2019: chromatin polymer is intrinsically LLPS-competent (epigenetic mark ↔ structural state coupling).
- Ahn 2021: genetic alteration (translocation) → IDR-fusion → LLPS → 3D rewiring (Genetic ↔ Structural cross-axis).
- Daugird 2024: live-cell measurement of viscoelastic properties — confirms in-vivo what the models predict.
- Qi & Zhang 2021: chromatin viscoelasticity quantitatively explains nuclear-body multi-droplet stability.

All claims in the user's locus-state Para 4 ("mechanical or viscoelastic states ... rigidity, condensation, elasticity, and fluid-like behavior, all of which are closely linked to transcriptional and epigenetic activity") now have direct verbatim references.

---

## 2026-05-18 (part 2) — Source-path remap + 7 more ingests

**Trigger**: Continuation of part-1 deferred tasks — fix stale `source:` paths and ingest remaining priority candidates.

### Source path remap (171 summaries updated)

Built source-title map from `00-Sources/papers/*.md` and rewrote `source:` field across all summaries using a **SequenceMatcher ratio threshold (≥0.55 with ≥0.10 margin over second-best)** to avoid false-positive matches.

- 171 summaries got accurate source-path updates pointing to new descriptive .md filenames.
- 38 summaries skipped (ambiguous or abstract-only ingests with no PDF — Gibson/Ahn/Daugird/Qi-Zhang/Mali/Luquette etc.).
- 2 manual fixes: `macaulay-2016-gt-seq-protocol` (Nat Protocols 2016, was wrongly pointing to 2015 paper), `macaulay-2015-gt-seq` (had duplicate source: lines).
- 1 duplicate resolved: `bizzotto-2022-brain-mosaicism-nrn.md` (older stub) deleted; `bizzotto-2022-brain-mosaicism-review.md` retained.

### Phase B continuation — 7 more abstract+intro ingests

- **Bae et al. 2017** *Science* — different mutational rates/mechanisms in pregastrulation vs neurogenesis; companion to Lodato 2017. [DOI](https://doi.org/10.1126/science.aan8690)
- **Gaiti et al. 2019** *Nature* — CLL epigenetic evolution; methylation disorder as lineage barcode. [DOI](https://doi.org/10.1038/s41586-019-1198-z)
- **Guo et al. 2013** *Genome Research* — scRRBS: founding single-cell methylome method, 1.5M CpGs/cell, digitized in haploid cells. [DOI](https://doi.org/10.1101/gr.161679.113)
- **Bartosovic et al. 2021** *Nat Biotech* — scCUT&Tag: droplet-based scaling of histone-mark and TF profiling. [DOI](https://doi.org/10.1038/s41587-021-00869-9)
- **Bartosovic et al. 2022** *Nat Biotech* — nano-CUT&Tag (nano-CT): multimodal single-cell chromatin profiling (3 modalities via nanobody-Tn5 fusions). [DOI](https://doi.org/10.1038/s41587-022-01535-4)
- **Cardilla et al. 2025** *Nature* — first whole-genome **spatial DNA methylome + transcriptome** co-profiling at near single-cell resolution. [DOI](https://doi.org/10.1038/s41586-025-09484-z)
- **Morriss et al. 2024** *bioRxiv* — spatial genomics for clonal heterogeneity in tissues. [DOI](https://doi.org/10.1101/2024.10.07.617096)

### Counts

- Summaries: 224 → 230 (+7 new − 1 bizzotto stub dedup)
- Coverage: spatial methylation + spatial genomics now represented; histone-mark axis filled with Bartosovic 2021/2022 (foundational scCUT&Tag lineage); brain mosaicism axis completed with Bae 2017 + Lodato 2017 pair.
- Remaining candidates for future ingest: Lareau 2020 (mtscATAC—was actually Ludwig 2020 already ingested), Forsberg 2016 (mosaicism review), spatial-cellular DNA-seq variants, ProSolo variant caller, DeepMosaic, ArchR-related, etc.

---

## 2026-05-18 — Maintenance pass: source PDF→MD conversion, summary naming unification, 7 new ingests

**Trigger**: User converted all 138 source PDFs to .md extracts with descriptive titles and removed duplicates (00-Sources/papers/ now contains 178 .md, no PDFs). Asked to (a) ingest truly new sources and (b) unify summary filenames.

### Phase A — Summary naming unification

- Audited 241 summaries: 203 already in `lastname-year-key.md` convention, 38 in descriptive-title format.
- **Deleted 24 stub summaries** that were thin duplicates of richer descriptive-title summaries (decision based on file size: descriptive files were 3-4× richer with proper Citation blocks).
- **Renamed 37 descriptive-title summaries** to `lastname-year-key.md` convention:
  - 13 unique renames (e.g., `clark-2018-scnmt-seq`, `liu-2025-nanopore-lscc-svs`, `hou-2016-sctrio-seq`, `kim-2017-methylation-memory-review`).
  - 24 dedup-renames (kept richer content, deleted stubs).
- Only `example-llm-wiki.md` remains in non-conventional form (deliberate — it's the Karpathy seed reference).

### Phase B — New ingests (7 abstract+intro based)

All marked `ingest_depth: abstract+intro` in frontmatter for future deep-ingest with full PDF text.

- **Lodato et al. 2017** *Science* — somatic mutations accumulate in aging postmitotic neurons; XP/Cockayne DNA-repair-defect patients show accelerated rate. [DOI](https://doi.org/10.1126/science.aao4426)
- **Macaulay et al. 2016** *Nature Protocols* — G&T-seq detailed bench protocol (companion to 2015 *Nat Methods* paper). [DOI](https://doi.org/10.1038/nprot.2016.138)
- **Ludwig et al. 2020** *Nature Biotechnology* — mtscATAC-seq: mtDNA heteroplasmy + chromatin accessibility per cell; mtDNA as natural lineage barcode. [DOI](https://doi.org/10.1038/s41587-020-0645-6)
- **Chen et al. 2017** *Science* — LIANTI: Tn5+T7 linear-amplification scWGA; foundational scWGA chemistry. [DOI](https://doi.org/10.1126/science.aak9787)
- **Abascal et al. 2021** *Nature* — NanoSeq: <5×10⁻⁹/base error rate via restriction-enzyme duplex; somatic mutations in non-dividing tissues. [DOI](https://doi.org/10.1038/s41586-021-03477-4)
- **Granja et al. 2021** *Nature Genetics* — ArchR: end-to-end scATAC-seq R package; 1.2M cells in 8h. [DOI](https://doi.org/10.1038/s41588-021-00790-6)
- **O'Roak et al. 2012** *Science* — Multiplex MIP targeted resequencing of 44 autism candidate genes; ~1% of sporadic ASD. [DOI](https://doi.org/10.1126/science.1227764)

### Phase C — Skipped / deferred

Off-topic sources skipped (Collateral sensitivity E. coli, FoldPAthreader protein folding). True wiki gaps remain ~10-15 sources to ingest later (e.g., Bartosovic 2021/2022 nano-CUT&Tag, Lareau 2020 mtscATAC, Bae 2017 pregastrulation mutations, Forsberg 2016 mosaicism review, spatial-cellular DNA-seq variants). All have abstract metadata in `00-Sources/papers/` ready for next pass.

### Stale `source:` paths (flagged)

Most pre-existing summaries reference old `[[00-Sources/papers/Author_Year_Journal]]` paths that no longer resolve since the user renamed sources to descriptive titles. Bulk source-path remap is a separate maintenance task — flagged for future pass. The new 7 summaries point to current paths.

### Counts

- Summaries: 241 → 224 (+7 new − 24 stub deletions)
- Sources: 178 .md (no PDFs)
- Coverage gap: ~10-15 truly-uncovered sources (next-pass candidates)

---

## 2026-05-15 — Ingest: scDamID lineage (Rooijers 2019 + de Luca & Kind 2021 + Mali 2025)

**Trigger**: User proposed a three-part **DNA locus state** framework (genetic / epigenetic / structural-physical) and asked whether the wiki covered it. Audit showed strong coverage of genetic + epigenetic axes and the 3D / chromatin-interaction sub-axis, but a clear gap on **spatial positioning (nuclear lamina)** and **biophysical state**. User chose to plug the lamina/DamID gap first.

**Sources ingested (3)**:

- `Simultaneous quantification of protein–DNA contacts and transcriptomes in single cells.md` — Rooijers K, Markodimitraki CM, Rang FJ, de Vries SS, Chialastri A, de Luca KL, Mooijman D, Dey SS, **Kind J**. *Nat Biotechnol* 37(7): 766–772 (2019). [DOI](https://doi.org/10.1038/s41587-019-0150-y). **scDam&T-seq** — joint scDamID + CEL-Seq2 mRNA via T7-IVT linear amplification. First single-cell coupling of NL contact to transcription; reveals fLAD-only (not cLAD) coupling.
- `Single-Cell DamID to Capture Contacts Between DNA and the Nuclear Lamina in Individual Mammalian Cells.md` — de Luca KL, **Kind J**. *Methods Mol Biol* 2157: 159–172 (2021). [DOI](https://doi.org/10.1007/978-1-0716-0664-3_9). Canonical bench protocol for scDamID with Dam-LMNB1.
- `Quantifying conformational heterogeneity of 3D genome organization in fruit fly.md` — Mali S, Tolokh IS, Cross E, **Onufriev AV**. *PLOS One* 20(7): e0326927 (2025). [DOI](https://doi.org/10.1371/journal.pone.0326927). Defines **Conformational Heterogeneity (C.H.)** metric; bulk-Hi-C vs scHi-C trained 3D models diverge at 1–10 Mb; lamin depletion raises C.H. genome-wide → predicts elevated transcriptional noise.

**New summary pages (3)**:
- `10-Summaries/rooijers-2019-scdamt-seq.md`
- `10-Summaries/de-luca-2021-scdamid-protocol.md`
- `10-Summaries/mali-2025-conformational-heterogeneity.md`

**New concept pages (5)**:
- `30-Concepts/damid.md` — DNA adenine methyltransferase identification; the assay family.
- `30-Concepts/scdamt-seq.md` — joint protein–DNA + transcriptome via IVT linear amplification.
- `30-Concepts/lamina-associated-domains.md` — LADs with cLAD vs fLAD distinction (load-bearing).
- `30-Concepts/nuclear-lamina.md` — the peripheral organizing surface.
- `30-Concepts/conformational-heterogeneity.md` — C.H. metric definition and use cases.

**New entity pages (4)**:
- `20-Entities/jop-kind.md` — Hubrecht; scDamID/scDam&T-seq lineage.
- `20-Entities/kim-de-luca.md` — Kind lab; protocol first author.
- `20-Entities/siddharth-dey.md` — UCSB; co-senior on scDam&T-seq.
- `20-Entities/alexey-onufriev.md` — Virginia Tech; biophysics; C.H. metric.

**Existing pages updated (3)**:
- `40-Topics/3d-genome.md` — added Nuclear lamina + Conformational heterogeneity sub-themes; added 4 new concepts and 2 new entities to core lists; added 2 new open questions on fLAD/cLAD differential coupling and bulk-vs-scHi-C orthogonality.
- `40-Topics/chromatin-architecture.md` — added "Nuclear lamina / spatial positioning" subsection under 3D genome.
- `index.md` — expanded "3D Genome at Single-Cell Resolution" section with lamina lineage + heterogeneity metric callouts; bumped updated date to 2026-05-15.

**Locus state framework coverage assessment (post-ingest)**:

| Axis | Sub-axis | Coverage |
|------|----------|----------|
| Genetic | CNV / SNV / allelic | **Strong** (CHISEL, MEDICC2, SCARLET, Monovar, SiFit, etc.) |
| Epigenetic | Methylation / histone / accessibility | **Strong** (~149 papers) |
| Structural/Physical | 3D / chromatin interaction | **Strong** (Hong 2025, Jiang 2026, Dip-C, sn-m3C-seq, scHi-C family) |
| Structural/Physical | Spatial positioning (lamina/LAD) | **Now adequate** (Rooijers + de Luca + Mali added) |
| Structural/Physical | Mechanical / viscoelastic / phase separation | **Still weak** (only Elliott 2025 partial; PubMed candidates: Gibson 2019 LLPS, Ahn 2021 phase-driven looping, Daugird 2024 viscoelastic chromatin, Qi & Zhang 2021 nucleoli) |

**Notable findings worth resurfacing**:

- **fLAD ≠ cLAD coupling** (Rooijers 2019): the negative lamina↔transcription coupling is restricted to H3K27me3-marked facultative LADs, NOT to H3K9me3 constitutive LADs. This is the cleanest single-cell evidence that lamina detachment is a regulatable axis, not a uniform repressive floor.
- **C.H. exposes scHi-C undersampling** (Mali 2025): with only ~20 single-cell maps, scHi-C-trained 3D models *miss* the dense weak TAD-TAD contacts captured by bulk Hi-C. Methodological recommendation — incorporate bulk Hi-C as supplementary restraint until scHi-C cohorts grow.
- **Lamin depletion → predicted transcriptional noise**: testable via scDam&T-seq or scNMT-seq in lamin-knockdown vs WT cells. Mammalian transferability supported (Ulianov 2019).

**Next ingest candidates** (Part 3c biophysical gap): Gibson et al. 2019 *Cell* (chromatin LLPS), Ahn et al. 2021 *Nature* (phase separation drives oncogenic loops), Daugird et al. 2024 *Nat Commun* (viscoelastic chromatin lattice light-sheet), Qi & Zhang 2021 *Nat Commun* (nucleoli coalescence).

---

## 2026-05-15 — Ingest: Biophysical / LLPS cluster (Gibson 2019 + Ahn 2021 + Daugird 2024 + Qi & Zhang 2021) — abstract-based

**Trigger**: User asked for autonomous continuation to fill the Part 3c (biophysical / mechanical / phase-separation) gap of the DNA locus-state framework. No local PDFs available; ingest uses PubMed metadata + abstracts already in conversation context. Each summary explicitly marks `ingest_depth: abstract-only` in frontmatter so re-ingest with PDFs later will deepen them.

**Sources ingested (4)**:

- **Gibson et al. 2019** *Cell* 179(2): 470–484. [DOI](https://doi.org/10.1016/j.cell.2019.08.037). Foundational chromatin LLPS — histone-tail-driven, H1-tuned, p300-dissolved, BRD4-phase-switched.
- **Ahn et al. 2021** *Nature* 595: 591–595. [DOI](https://doi.org/10.1038/s41586-021-03662-5). NUP98-HOXA9 IDR-driven LLPS induces CTCF-independent chromatin loops at proto-oncogenes; IDR identity interchangeable (FUS-IDR swap works) → LLPS *competence* is the load-bearing property.
- **Daugird et al. 2024** *Nat Commun* 15: 4178. [DOI](https://doi.org/10.1038/s41467-024-48562-0). Live-cell lattice light-sheet single-molecule imaging measures chromatin viscoelasticity directly; interchromatin accessibility constant across density regimes; transcription locally stabilizes nucleosomes.
- **Qi & Zhang 2021** *Nat Commun* 12: 6824. [DOI](https://doi.org/10.1038/s41467-021-27123-9). Hi-C-parameterized polymer model — viscoelastic chromatin network arrests nucleolus coalescence via entropic barrier; explains stable multi-droplet architecture of nuclear bodies.

**New summary pages (4)**:
- `10-Summaries/gibson-2019-chromatin-llps.md`
- `10-Summaries/ahn-2021-llps-cancer-looping.md`
- `10-Summaries/daugird-2024-viscoelastic-chromatin.md`
- `10-Summaries/qi-zhang-2021-nucleoli-coalescence.md`

**New concept pages (2)**:
- `30-Concepts/chromatin-phase-separation.md` — LLPS as the mechanical/phase-separation sub-axis of locus state.
- `30-Concepts/chromatin-mechanical-properties.md` — viscoelasticity, rigidity, condensation; the third sub-axis of structural-physical locus state.

**New entity pages (2)**:
- `20-Entities/michael-rosen.md` — UTSW/HHMI; LLPS field founder; corresponding on Gibson 2019.
- `20-Entities/bin-zhang.md` — MIT Chemistry; polymer-physics theory; corresponding on Qi & Zhang 2021.

**Existing pages updated (3)**:
- `40-Topics/chromatin-architecture.md` — added "Biophysical / phase-separation / mechanical state" subsection with all 4 papers.
- `40-Topics/3d-genome.md` — added "Phase separation × 3D architecture" sub-section + 2 concepts (chromatin-phase-separation, chromatin-mechanical-properties) to core list.
- `index.md` — added "Biophysical / LLPS" callout line under 3D Genome at Single-Cell Resolution.

**Locus state framework — final coverage (post-3c ingest)**:

| Axis | Sub-axis | Coverage |
|------|----------|----------|
| Genetic | CNV / SNV / allelic | **Strong** |
| Epigenetic | Methylation / histone / accessibility | **Strong** (~149 papers) |
| Structural/Physical | 3D / chromatin interaction | **Strong** |
| Structural/Physical | Spatial positioning (lamina/LAD) | **Adequate** (Kind lineage) |
| Structural/Physical | Mechanical / viscoelastic / LLPS | **Now adequate** (4 anchor papers; abstract-based — flag for PDF re-ingest) |

**Cross-axis synthesis insight (new)**:

Ahn 2021 is the cleanest example of a **genetic alteration that reshapes the structural-physical axis via biophysics**: a translocation (genetic change) creates an IDR-fusion protein (sequence change) that phase-separates (biophysical state) and rewires 3D architecture (structural state). This single paper anchors a cross-axis coupling that the framework predicts. Worth promoting to a `50-Notes/` synthesis when a few more cross-axis examples accumulate.

**Caveat — ingest depth**: all 4 summaries are abstract-based. Each frontmatter carries `ingest_depth: abstract-only`. When PDFs become available, re-ingest will replace the placeholder Methods/evidence content with quantitative parameters (binding constants, viscosity scales, loop resolution thresholds).

**Commit + push**: this ingest will be pushed together with the 2026-05-15 scDamID lineage commit in a single batch.

---

## 2026-05-14 — Ingest: Dean 2002 MDA + Kapadia & Goodell 2024 (stem cell aging) + DOI-link retrofit (89 summaries)

**Trigger**: User requested ingest of two new sources and asked that paper summaries carry clickable DOI/URL links back to the original publications.

**Sources ingested (2)**:

- `Comprehensive human genome amplification using multiple displacement amplification.md` — Dean FB, Hosono S, Fang L, Wu X, Faruqi AF, Bray-Ward P, Sun Z, Zong Q, Du Y, Du J, Driscoll M, Song W, Kingsmore SF, Egholm M, Lasken RS. *PNAS* 99(8): 5261–5266 (2002). [DOI](https://doi.org/10.1073/pnas.082089499). The founding MDA paper — Φ29 polymerase + random hexamers → <3-fold WGA bias vs. 4–6 orders of magnitude for PCR-based methods. Anchor citation for the entire scWGA branch of single-cell genomics.
- `Kapadia_2024_NatAging - Tissue mosaicism following stem cell aging.pdf` — Kapadia CD, Goodell MA. *Nature Aging* 4(3): 295–308 (2024). [DOI](https://doi.org/10.1038/s43587-024-00589-0). Review of stem cell aging × somatic mosaicism in lockstep, using HSC as exemplar. Provides quantitative anchor numbers: 14–17 coding mutations/HSC/year, 50,000–200,000 HSC pool, >95% adults >50 have detectable CH by duplex sequencing. Introduces "adaptive oncogenesis" frame.

**New summary pages (2)**:
- `10-Summaries/dean-2002-mda.md`
- `10-Summaries/kapadia-2024-stem-cell-aging.md`

**New entity page (1)**:
- `20-Entities/margaret-goodell.md` — corresponding author of Kapadia 2024; Baylor HSC biologist

**Existing pages updated (3)**:
- `30-Concepts/mda.md` — added Dean 2002 as founding paper citation in definition + Related
- `30-Concepts/clonal-hematopoiesis.md` — added quantitative HSC mutation accumulation block (14–17 mut/year, pool size 50K–200K), adaptive oncogenesis framing, broad pathology spectrum
- `30-Concepts/somatic-mosaicism.md` — added "universal in aged tissue" claim with Kapadia 2024 citation

**DOI/URL link retrofit (81 summaries)**:

Wrote `tools/add-doi-links.py` to retrofit clickable source links into existing summary pages. Strategy:
1. Skip files already containing an https:// link in body.
2. If frontmatter has a `doi:` field → insert `**Source:** [DOI](https://doi.org/...)` before `## Related`.
3. Else if `sources:` points to a `.md` clipping in `00-Sources/papers/` carrying a `source:` URL → insert `**Source:** [Open paper](...)`.
4. Else flag as needing PubMed lookup.

Results from 234 total summaries:
- 8 already had links (the 3 newly created scRNA-seq summaries + 5 inherited)
- **81 auto-fixed** from existing frontmatter `doi:` field (45) or `.md` clipping URLs (36)
- **145 remain — PDF-only sources without DOI metadata.** These need PubMed lookup by title/author/year. Slugs follow `author-year-journal` convention, so batch PubMed query is feasible in a follow-up session.

Post-retrofit: 89 of 234 summaries (38%) carry clickable source links. The remaining 145 are catalogued and ready for batch PubMed processing.

**Tool created**: `tools/add-doi-links.py` — idempotent, dry-run-capable. Re-runnable as more `doi:` fields or `.md` clippings are added.

**Follow-up (same day)**: Wrote `tools/pubmed-lookup.py` to batch-resolve the remaining 145 via NCBI E-utilities with strict author+title+year verification. After two iterations of query refinement (cleaning special chars, shortening to 4–6 significant words, requiring first-author surname match in PubMed authors list) and manual additions for 7 PubMed-indexed papers via MCP search:

- **232 of 234 summaries now carry working DOI + PubMed links (99%)**.
- 2 remaining: `example-llm-wiki.md` (placeholder seed, no real paper) and `ghorbani-2019-comp-epigenetics.md` (Journal of Applied Biology & Biotechnology, not PubMed-indexed). Both intentionally skipped.

According to PubMed, all DOIs were verified by author + year + title-word overlap before insertion.

**Notable findings / tensions surfaced**:
- Frontmatter inconsistency across summaries: some have rich metadata (`doi:`, `journal:`, `published:`, `entities:`, `concepts:`), some have minimal (`sources:` + a few tags). The retrofit succeeded only where structured metadata was already present. A future maintenance pass could normalize frontmatter across the corpus.
- 138 PDF source files in `00-Sources/papers/` carry no metadata recoverable without opening the PDF. PubMed lookup by reconstructed citation is the next logical step.

---

## 2026-05-14 — Ingest: scRNA-seq foundational papers (Tang 2009, Macosko 2015, Svensson 2017)

**Trigger**: User is drafting the introduction of a scDNA-seq review paper (multi-omics focus). Wiki audit showed strong coverage of somatic mutation / mosaicism but a gap on (i) scRNA-seq foundations and (ii) bulk-vs-single-cell framing for RNA. Three canonical papers fetched via PubMed MCP to close that gap.

**Sources ingested (3)**:

- `Tang_2009_NatureMethods.md` — Tang, Barbacioru, Wang et al. (Surani lab, Gurdon). First scRNA-seq from a single mouse blastomere. [DOI](https://doi.org/10.1038/nmeth.1315). PMID 19349980. *Abstract-only ingest — no PMC full text available.*
- `Macosko_2015_Cell.md` — Macosko, Basu, Satija et al. (McCarroll/Regev/Shalek, Broad/Harvard). Drop-seq — droplet scRNA-seq of 44,808 mouse retinal cells. [DOI](https://doi.org/10.1016/j.cell.2015.05.002). PMID 26000488, PMC4481139. *Full text ingested.*
- `Svensson_2017_NatureMethods.md` — Svensson, Natarajan, Ly et al. (Teichmann lab, EMBL-EBI/Sanger). First unified scRNA-seq power analysis: 15 protocols, 18,123 samples, ERCC spike-ins. [DOI](https://doi.org/10.1038/nmeth.4220). PMID 28263961, PMC5376499. *Full text ingested.*

**New summary pages (3)**:
- `10-Summaries/tang-2009-scrna-seq.md`
- `10-Summaries/macosko-2015-drop-seq.md`
- `10-Summaries/svensson-2017-power-analysis.md`

**New concept pages (2)**:
- `30-Concepts/scrna-seq.md` — foundational concept page covering bulk-vs-single-cell, history, design axes, limitations, and the review framing for "why scRNA-seq at all"
- `30-Concepts/drop-seq.md` — Drop-seq method, bead architecture, performance numbers, successor methods

**New entity page (1)**:
- `20-Entities/fuchou-tang.md` — first author of the founding paper and current Peking University PI; cross-linked to scTrio-seq

**Existing pages updated (3)**:
- `30-Concepts/umi-molecular-barcoding.md` — added Svensson 2017 sublinear-saturation caveat (UMI exponent ≈0.8) and Drop-seq as canonical scRNA usage
- `30-Concepts/pseudo-bulk.md` — added "pseudo-bulk ≠ original bulk" framing, connecting to scRNA-seq's resolution of the bulk-composition confound
- `index.md` — added "Single-Cell Transcriptomics" section between Mosaicism and Multi-Omics; updated date

**Notable findings / tensions surfaced**:
- The wiki is heavily scDNA + epigenomics-focused; scRNA-seq fundamentals were a real gap for the user's intended review intro. Now closed at the foundational level.
- Two entity pages mentioned but not yet created (intentional, low priority): `evan-macosko`, `steven-mccarroll`, `aviv-regev`, `valentine-svensson`, `sarah-teichmann`. These can be added in a future ingest or maintenance pass; their summary pages already reference them.
- Svensson 2017's UMI-saturation finding (exponent ≈0.8) is a nuance worth flagging in any quantitative scRNA-seq discussion in the review — it complicates the "UMI = absolute molecule count" story.
- No contradiction with existing content; all new pages cross-link cleanly into the multi-omics topic and the GoT/DR-seq/scTrio-seq family.

**Method note**: PubMed MCP `get_full_text_article` returned 71k characters that exceeded the inline token limit; output was saved to a tool-results file, then extracted via `jq` into individual source files. Tang 2009 has no PMC entry → ingested at abstract level with a note in the source file.

---

## 2026-05-13 — Ingest batch 19 (31 markdown source files)

**Trigger**: User correctly pointed out that I had reported "corpus complete" while ignoring 37 markdown source files in `00-Sources/papers/`. Of these, 6 were already covered by prior summaries; 31 were genuinely uningested. This session closes that gap.

**Sources ingested (31)** — all `.md` web-clipped article archives:

Duplex/scDNA methodology:
- `A comprehensive view of somatic mosaicism by single-cell DNA analysis.md` → Luquette/Coorens/Walsh/Park/Abyzov 2025 SMaHT PTA scDNA
- `A Universal Duplex Sequencing Approach for Accurate Detection of Somatic Mutations.md` → Nandi/Alexandrov 2025 UDSeq
- `Accurate single-cell genotyping utilizing information from the local genome territory.md` → Tu/Xie 2021 SCOUT
- `Benchmarking of duplex sequencing approaches to reveal somatic mutation landscapes.md` → Zhang/Coorens 2025 SMaHT 6-platform benchmark
- `Detecting ultralow-frequency mutations by Duplex Sequencing.md` → Kennedy/Loeb 2014 Nat Protoc

scATAC analysis tools:
- `chromVAR_ inferring transcription-factor-associated accessibility from single-cell epigenomic data.md` → Schep/Greenleaf 2017
- `cisTopic_ cis-regulatory topic modeling on single-cell ATAC-seq data.md` → Bravo/Aerts 2019
- `Comprehensive analysis of single cell ATAC-seq data with SnapATAC.md` → Fang/Ren 2021
- `EpiScanpy_ integrated single-cell epigenomic analysis.md` → Danese/Theis 2021
- `High-throughput chromatin accessibility profiling at single-cell resolution.md` → Mezger/Greenleaf 2018 µATAC-seq
- `scATAC-seq generates more accurate and complete regulatory maps than bulk ATAC-seq.md` → Gur/Hughes 2025
- `Unsupervised clustering and epigenetic classification of single cells.md` → Zamanighomi/Wong 2018 scABC

Single-cell methylation:
- `DNA methylation_ an epigenetic mark of cellular memory - Experimental & Molecular Medicine.md` → Kim/Costello 2017
- `High‐throughput single‐cell DNA methylation and chromatin accessibility co‐profiling with SpliCOOL‐seq.md` → Shen/Fan 2025
- `scTEM-seq_ Single-cell analysis of transposable element methylation to link global epigenetic heterogeneity with transcriptional programs.md` → Hunt/Lee 2022
- `Simultaneous single-cell analysis of 5mC and 5hmC with SIMPLE-seq.md` → Bai/Yi 2024
- `Sequencing DNA methylation and hydroxymethylation at co-occurring chromatin features.md` → Tavares/Balasubramanian 2026 6-base-CUT&Tag

Histone modifications / chromatin profiling:
- `DeepHistone_ a deep learning approach to predicting histone modifications.md` → Yin/Jiang 2019
- `Scalable single-cell profiling of chromatin modifications with sciCUT&Tag.md` → Janssens/Henikoff 2023
- `scChIX-seq infers dynamic relationships between histone modifications in single cells.md` → Yeung/van Oudenaarden 2023
- `Single-cell chromatin immunocleavage sequencing (scChIC-seq) to profile histone modification.md` → Ku/Zhao 2019
- `Single-cell multi-omic detection of DNA methylation and histone modifications reconstructs the dynamics of epigenomic maintenance.md` → Geisenberger/van Oudenaarden 2025 scEpi²-seq

Long-read / single-molecule footprinting:
- `Direct transposition of native DNA for sensitive multimodal single-molecule sequencing.md` → Nanda/Ramani 2024 SMRT-Tag/SAMOSA-Tag
- `Profiling the epigenome using long-read sequencing.md` → Liu/Conesa 2025 NatGenet review
- `Single-molecule targeted accessibility and methylation sequencing of centromeres, telomeres and rDNAs in Arabidopsis.md` → Mo/Zhai 2023 STAM-seq
- `Nanopore Sequencing Unveils Somatic Structural Variations as Biomarkers in Laryngeal squamous cell carcinoma Genomes.md` → Liu 2025 SomaGauss-SV LSCC

3D genome:
- `Harmonizing single-cell 3D genome data with STARK and scNucleome.md` → Jiang/Wu 2026 STARK
- `Navigating the 3D genome at single-cell resolution_ techniques, computation, and mechanistic landscapes.md` → Hong/Dao 2025 review

Brain mosaicism + mtDNA + applications:
- `Genetic mosaicism in the human brain_ from lineage tracing to neuropsychiatric disorders - Nature Reviews Neuroscience.md` → Bizzotto/Walsh 2022 NRN review
- `High-throughput single-cell analysis reveals progressive mitochondrial DNA mosaicism throughout life.md` → Glynos/Chinnery 2023
- `Single-cell mosaicism analysis reveals cell-type-specific somatic mutational burden in Alzheimer's Dementia.md` → Kousi/Kellis 2022

**Pages created**: 31 summaries in `10-Summaries/`. No new entity pages (all link to existing entities).

**BibTeX**: 23 new entries added. 8 keys already existed (bizzotto2022, kousi2022, nanda2024, mezger2018, ku2019, mo2023, kennedy2014, hong2025).

**Index update**: New "Batch 19 markdown sources" subsection with 31 entries.

**Retroactive citation flags (the big ones)**:
- §1/§5.2 brain mosaicism → MUST cite `bizzotto2022` NRN review (Walsh-authored, canonical 2022 brain mosaicism reference).
- §3.1.3 duplex methods → MUST cite `zhang2025duplex` SMaHT 6-platform benchmark + `nandi2025udseq` for the newest duplex chemistry; `kennedy2014` for protocol-level detail.
- §3.1 PTA application → `luquette2025` SMaHT lung+colon as the cohort-scale PTA demonstration.
- §3.2 scATAC tools → MUST cite `schep2017` chromVAR, `bravo2019` cisTopic, `fang2021` SnapATAC as the canonical analysis tool trio.
- §3.3 methylation methods → `bai2024` SIMPLE-seq (5mC + 5hmC single-cell), `shen2025` SpliCOOL-seq, `hunt2022` scTEM-seq.
- §3.4 histone modifications → MUST cite `janssens2023` sciCUT&Tag, `yeung2023` scChIX-seq, `ku2019` scChIC-seq, `geisenberger2025` scEpi²-seq.
- §3.5 3D genome → `jiang2026stark` STARK benchmark, `hong2025navigate3d` review.
- §3.3 LRS → `liu2025lrs` long-read epigenome review, `nanda2024` SMRT-Tag, `mo2023` STAM-seq.
- §4 computational tools → `danese2021` EpiScanpy, `tu2021scout` SCOUT, `zamanighomi2018` scABC.
- §5.2 AD + brain → `kousi2022` Alzheimer scDNA mosaicism (already cited).
- §5.3 mtDNA mosaicism → `glynos2023` for mechanistic basis of heteroplasmy drift.

**Corpus state — TRULY complete now**:
- Total source files: 174 (137 PDF + 37 MD)
- Total summaries created: 198 (covers all on-topic sources)
- Permanently skipped (5): Chin_2025 oversized, David_2020/Matthew_2020 corrupted PDFs, Joanna_2023/Kailong_2024 off-topic
- Duplicate skipped (1): Benjamin_2024_bioRxiv preprint of Doughty Nature

**Lesson for future me**: When the user requests "ingest all papers," `.md` clipped articles count as papers too. The discovery script should glob `*.pdf|*.md` not just `*.pdf`. Apologies for the earlier "corpus complete" claim.

---

## 2026-05-13 — Draft session: §1, §5, §6, §7, §8 written

**Trigger**: User "let's make a draft" + "yes, continue" after corpus complete.

**Sections drafted**:
- `sections/01-introduction.tex` — ~1,200 words. Frames somatic mosaicism, scDNA-seq history, multi-omics convergence, explicit positioning vs Shao 2025 NRG competitor, locus-state framing introduction, roadmap.
- `sections/05-applications.tex` — ~1,800 words across 4 subsections (cancer / brain / CH+aging / development).
- `sections/06-limitations.tex` — ~1,400 words across 4 subsections (amplification artifacts / modality combinatorics / throughput / analytical fragmentation).
- `sections/07-future.tex` — ~1,200 words across 4 subsections (chemistry consolidation / modality breadth / scale & access / analytical unification).
- `sections/08-conclusion.tex` — ~500 words. Synthesizes locus-state argument, lists landmark biological observations enabled by scDNA-seq.

**main.tex updated**: all five new sections wired in; "pending" placeholders removed.

**Citation validation**: All 83 unique \citep keys across new sections resolve to references.bib. One missing key fixed (`lee2019scm3c` → `lee2019`).

**Draft completeness**: Manuscript now has §1 + §2 + §3.1-3.5 + §4 + §5 + §6 + §7 + §8 — full structure complete in first draft form. Estimated total length ~9,000-10,000 words plus references.

**Not done in this session**:
- pdflatex local compile (not installed; user must compile)
- Retroactive citation pass on §3.1-3.5 with new bibkeys from batches 12-18
- Figure design and inclusion
- Cross-section consistency review (e.g., §1 promises five-layer locus state — §3 sections should match)

---

## 2026-05-13 — Ingest batch 18 (14 papers ingested, founding scDNA + SMF expansion + reviews + triple-omics)

**Trigger**: User "continue ingesting if remains". Final candidates from the 14-paper backlog (after batches 16/17, excluding 5 known-skipped + 1 duplicate).

**Papers ingested (14)**:
- `Gilad_2021_AnnualReviewOfGenomicsAndHumanGenetics` = **Evrony/Hinch/Luo 2021** — scDNA-seq applications review with fidelity/co-presence/phenotypic-association framework.
- `Ian_2015_TrendsInGenetics` = **Campbell/Lupski 2015** — somatic mosaicism developmental-timing + transmission-genetics review.
- `Lars_2017_NatureReviewsGenetics` = **Forsberg/Gisselsson/Dumanski 2017** — post-zygotic variation + mLOY review.
- `Nicholas_2011_Nature` = **Navin/Wigler 2011 SNS** — founding tumor scDNA-seq. Punctuated-evolution model.
- `Nicolas_2022_NatureMethods` = **Altemose/Streets/Straight 2022 DiMeLo-seq** — long-read antibody-directed pA-Hia5 protein-DNA mapping.
- `Nour_2020_eLife` = **Abdulhay/Ramani 2020 SAMOSA** — PacBio + EcoGII m6A oligonucleosome footprinting.
- `Roghayeh_2019_JABB` = **Ghorbani/Shokri-Gharelo 2019** — generic computational epigenetics review (low-impact journal, flagged as low-priority citation).
- `Rujin_2020_CellSystems` = **Wang/Jiang 2020 SCOPE** — scDNA-seq CNV normalization with ploidy estimation.
- `Runsheng_2024_PNAS` = **He/Xie 2024 FOODIE** — DddB deaminase footprinting for single-cell/single-molecule TF binding.
- `Ruth_2022_NatureCommunications` = **Nichols/Adey 2022 sciMETv2** — combinatorial-indexing scDNA methylation.
- `Sandy_2019_NatureReviewsGenetics` = **Klemm/Shipony/Greenleaf 2019** — chromatin accessibility regulatory-epigenome review.
- `Siddharth_2015_NatureBiotechnology` = **Dey/van Oudenaarden 2015 DR-seq** — founding no-separation parallel scDNA+scRNA.
- `Yu_2016_CellResearch` = **Hou/Tang 2016 scTrio-seq** — founding single-cell triple-omics (genome+methylome+transcriptome) in HCC.
- `Zachary_2013_NatureReviewsGenetics` = **Smith/Meissner 2013** — DNA methylation in mammalian development review.

**Pages created**: 14 summaries in `10-Summaries/`. No new entity/concept pages.

**BibTeX**: 7 new entries (`navin2011`, `altemose2022`, `abdulhay2020`, `ghorbani2019`, `wang2020scope`, `he2024foodie`, `nichols2022`). 7 keys already existed (`evrony2021`, `campbell2015`, `forsberg2017`, `klemm2019`, `dey2015`, `hou2016`, `smith2013`).

**Index update**: New "Batch 18 founding scDNA + SMF expansion + reviews + triple-omics" subsection in index.md with 14 entries.

**Retroactive citation flags (~14)**:
- §1/§2 introduction → MUST cite `evrony2021` framework (fidelity/co-presence/phenotypic-association) as a structural model for arguing why scDNA-seq is uniquely required.
- §1/§2 clinical-genetics framing → `campbell2015` and `forsberg2017` provide complementary developmental and post-zygotic-variation contexts.
- §1/§5 tumor scDNA history → MUST cite `navin2011` as the founding tumor scDNA-seq paper; precedes Monovar, SCITE, ChISEL, MEDICC2.
- §3.1 parallel scDNA+scRNA → cite the 2015 trio: `macaulay2015` (G&T-seq physical separation), `dey2015` (DR-seq no separation), and `hou2016` (scTrio-seq triple-omics) — establishes the design-principle taxonomy.
- §3.3 SMF expansion → add `altemose2022` (DiMeLo-seq antibody-directed pA-Hia5), `abdulhay2020` (SAMOSA), `he2024foodie` (FOODIE) — these flesh out the SMF family alongside SMAC-seq, nanoNOMe, Fiber-seq, DAF-seq.
- §3.3 methylation methods → add `nichols2022` sciMETv2 alongside Luo snmC-seq2; represents the combinatorial-indexing branch of scMethylation.
- §3.3 conceptual foundation → `smith2013` is the canonical methylation-in-development reference, complementing Schübeler 2015.
- §3.2 chromatin accessibility intro → cite `klemm2019` for the canonical regulatory-epigenome framing.
- §4 CNV-calling methods → add `wang2020scope` SCOPE alongside CHISEL, MEDICC2, Ginkgo.
- §5 cancer/CH applications → Navin 2011 establishes the tumor scDNA history; Forsberg 2017 frames CH and mLOY in the post-zygotic variation context.

**Corpus complete**: All on-topic PDFs have now been ingested.
- Total PDFs in `00-Sources/papers/`: 137
- Summaries created across all sessions: ~132 papers ingested
- Permanently skipped (5): Chin_2025 (oversized), David_2020 (corrupted), Matthew_2020 (corrupted), Joanna_2023 (off-topic antimicrobial), Kailong_2024 (off-topic protein folding)
- Duplicate skipped (1): Benjamin_2024_bioRxiv (preprint of Doughty Nature)

**Notes**: This batch closed several remaining gaps simultaneously: (i) Navin 2011 founding tumor scDNA — closed; (ii) full 2015 founding-multimodal trio (G&T-seq + DR-seq + scTrio-seq) — closed; (iii) extended SMF family (DiMeLo-seq + SAMOSA + FOODIE alongside SMAC/Fiber/nanoNOMe/DAF-seq) — closed; (iv) Klemm and Smith review citations — closed; (v) Evrony 2021 application-framework citation — closed. The corpus is now operationally complete. Next session should focus on §5 draft writing, retroactive citation pass on §3, or lint maintenance.

---

## 2026-05-13 — Ingest batch 17 (11 papers ingested + 1 duplicate, founding multimodal + reviews + GoT family + DAF-seq)

**Trigger**: User "continue ingesting". Targeted priority candidates from the 31-paper backlog.

**Papers ingested (11)**:
- `Iain_2015_NatureMethods` = **Macaulay/Voet 2015 G&T-seq** — founding parallel scDNA+scRNA via oligo-dT bead separation. THE foundational multimodal scDNA paper. Major §3.1 anchor.
- `Ricard_2020_GenomeBiology` = **Argelaguet/Stegle 2020 MOFA+** — scalable variational extension of MOFA for multimodal+multigroup integration.
- `Alev_2023_NatureReviewsMolecularCellBiology` = **Baysoy/Fan/Satija 2023** — comprehensive multi-omics technology landscape review.
- `Diane_2025_NatureReviewsGenetics` = **Shao/Kriz/Walsh 2025** — NRG review on scDNA-seq for somatic mosaicism. **DIRECT COMPETITOR REVIEW** — user's manuscript must explicitly position against this.
- `Yilei_2025_NatureReviewsGenetics` = **Fu/Timp/Sedlazeck 2025** — long-read methylation computational analysis review.
- `Lukas_2023_NatureReviewsGenetics` = **Heumos/Theis 2023** — best-practices for single-cell analysis across modalities.
- `Katy_2023_NatureReviewsGenetics` = **Vandereyken/Voet 2023** — methods+applications review of single-cell and spatial multi-omics. Voet-authored, very scDNA-aware.
- `Anna_2019_Nature` = **Nam/Landau 2019 GoT** — founding genotyping-of-transcriptomes. Applied to CALR-mutated MPNs.
- `Franco_2024_Nature` = **Izzo/Landau 2024 GoT-ChA** — GoT extension to scATAC-seq via genomic-DNA amplification. JAK2-V617F MPN.
- `Elliott_2025_NatureBiotechnology` = **Swanson/Stergachis 2025 DAF-seq** — deaminase-based single-molecule chromatin fiber sequencing with simultaneous sequence + footprint readout. scDAF-seq variant covers 99% of cell's genome with haplotype resolution.
- `Charles_2016_NatureReviewsGenetics` = **Gawad/Koh/Quake 2016** — canonical early scDNA-seq state-of-the-science review.

**Duplicate (1)**:
- `Benjamin_2024_bioRxiv` — bioRxiv preprint of Benjamin_2024_Nature (Doughty SMF/TF paper), already ingested as `doughty-2024-smf-tf` in batch 16. Skipped to avoid duplicate summary.

**Pages created**: 11 summaries in `10-Summaries/`. No new entity pages — all reference existing entities (Voet, Stegle, Walsh, Landau, Stergachis, Quake, Sedlazeck, Theis).

**BibTeX**: 2 new entries added (`argelaguet2020`, `heumos2023`). All other 9 keys already existed (`macaulay2015`, `baysoy2023`, `shao2025`, `fu2025`, `vandereyken2023`, `nam2019`, `izzo2024`, `swanson2025`, `gawad2016`).

**Index update**: New "Batch 17 multimodal founding + reviews + GoT family + DAF-seq" subsection in index.md with 11 entries.

**Retroactive citation flags (~14)**:
- §1/§2 introductions → MUST cite `shao2025` as the direct competitor review; user's manuscript should distinguish its multi-omics scope from Shao's mosaicism-only focus.
- §3.1 multimodal scDNA+scRNA → MUST cite `macaulay2015` G&T-seq as the founding paper of the entire parallel-omics family.
- §3.1/§3.2 multimodal review citations → cite `vandereyken2023` (Voet's review) for the design-principle taxonomy and `baysoy2023` for the technology landscape.
- §3.3 methylation arm → add `fu2025` for long-read methylation computational analysis.
- §3.3 SMF → MUST cite `swanson2025` DAF-seq as the latest single-molecule chromatin fiber method with sequence-preserving footprinting (a fundamental advantage over Fiber-seq m6A approach for somatic mosaicism applications).
- §4 multimodal integration → MUST cite `argelaguet2020` MOFA+ alongside Cobolt/MultiVI/GLUE as the factor-analysis branch of integration.
- §4 best-practices and analysis workflows → cite `heumos2023` for analysis-pipeline recommendations.
- §5 cancer/CH applications → MUST cite `nam2019` GoT and `izzo2024` GoT-ChA when discussing genotype-to-phenotype linking in MPN/CH studies.
- §1 introductory historical context → cite `gawad2016` as the early-period scDNA-seq foundational review.
- §6/§7 future-perspectives → DAF-seq and Duplex-Multiome both demonstrate the convergence of somatic-mutation detection with chromatin readout in single cells; `swanson2025` + `kriz2025` together support this argument.

**Corpus state**: 118 summary pages now. Remaining unsummarized in `00-Sources/papers/`: ~19 candidates (down from 31). After excluding 5 known-skipped (Chin/David/Matthew corrupted or oversized, Joanna/Kailong off-topic) and 1 duplicate (Benjamin_2024_bioRxiv), about 13 PDFs of substantive content remain.

**Notes**: This batch resolved several long-standing citation gaps: (i) G&T-seq founding multimodal scDNA — closed; (ii) MOFA+ factor-analysis integration — closed; (iii) GoT/GoT-ChA family for CH/MPN genotype-to-phenotype — closed; (iv) DAF-seq state-of-the-art single-molecule chromatin — closed. The Shao 2025 NRG review ingest is operationally critical: user must explicitly position relative to this competitor in §1.

---

## 2026-05-13 — Ingest batch 16 (12 papers, multiome + scATAC founding + cancer + brain mosaicism)

**Trigger**: User "Continue ingesting". All 12 candidates on-topic — no off-topic or corrupted files this batch.

**Papers ingested (12)**:
- `Andrea_2025_bioRxiv` = **Kriz/Walsh/Lee 2025 Duplex-Multiome** — strand-tagged duplex sSNV layer on snATAC+snRNA. Profiled >51,400 postmortem brain nuclei; cell-type-specific age-related mutation rates and developmental lineage discovery. Major §5 brain anchor.
- `Assaf_2015_NatureBiotechnology` = **Rotem/Bernstein/Weitz 2015 Drop-ChIP** — founding single-cell ChIP-seq. DBM microfluidics + 1,152-barcode library + bulk IP.
- `Benjamin_2024_Nature` = **Doughty/Greenleaf/Bintu 2024** — single-molecule footprinting links TF binding to gene expression. 26M single-molecule measurements; thermodynamic + kinetic models from sequence.
- `Charissa_2018_Cell` = **Kim/Navin 2018 TNBC chemoresistance** — longitudinal scDNA+scRNA on 20 TNBC patients during NAC. Resistance is pre-existing genomic + acquired transcriptional. §5 cancer canonical.
- `Chongyuan_2018_NatureCommunications` = **Luo/Ecker 2018 snmC-seq2** — improved scWGBS protocol with SAP treatment + optimized random priming. Backbone of subsequent brain methylome atlases.
- `Craig_2019_NatureGenetics` = **Frankell/Fitzgerald 2019 OCCAMS EAC landscape** — 551 EAC WGS + RNA-seq, 77 drivers, CDK4/6 sensitivity in 50%+. Bulk-cohort context for cancer scDNA work.
- `Darren_2015_Science` = **Cusanovich/Shendure 2015 sci-ATAC-seq** — founding combinatorial-indexing scATAC, companion to Buenrostro 2015. Architectural foundation of all subsequent sci-* methods.
- `Dirk_2015_Nature` = **Schübeler 2015 methylation review** — conceptual frame: methylation as informative rather than instructive at distal regulatory elements.
- `Eran_2025_Neuron` = **Mukamel/Ecker 2025 brain aneuploidy** — repurposed 415k snmC-seq3/snm3C-seq profiles to call somatic aneuploidies; chr16 trisomy enrichment (human chr21 syntenic) recurrent in mouse brain, particularly OPCs.
- `Han_2022_NatureMethods` = **Yuan/Kelley 2022 scBasset** — sequence-based CNN modeling of scATAC-seq; cell embeddings from 1,344-bp peak-centric sequence prediction.
- `Hanqing_2023_Nature` = **Liu/Ecker 2023 mouse brain atlas** — 301k snmC-seq3 + 176k snm3C-seq methylome+3D-genome profiles, 4,673 cell groups across 117 brain regions.
- `Henry_2018_Nature` = **Lee-Six/Campbell 2018 HSC dynamics** — 140 single-HSPC colony WGS phylogeny; estimates active human HSC pool at 50k–200k; first whole-life clonal reconstruction from spontaneous somatic SNVs.

**Pages created**: 12 summaries in `10-Summaries/`. No new entity/concept pages this batch — all link to existing ones (Walsh, Lee, Ecker, Navin, Shendure, Campbell, Bernstein).

**BibTeX**: 1 new entry (`leesix2018`). All other 11 keys (`kriz2025`, `rotem2015`, `doughty2024`, `kim2018`, `luo2018`, `frankell2019`, `cusanovich2015`, `schubeler2015`, `mukamel2025`, `yuan2022`, `liu2023`) already present and reused.

**Index update**: New "Batch 16 multiome + scATAC founding + cancer + brain mosaicism" subsection in index.md before "Wiki seed", with 12 entries.

**Retroactive citation flags (~12)**:
- §3.2 scATAC-seq history → MUST cite both `buenrostro2015` AND `cusanovich2015` (the dual founding moment of scATAC, 22 May 2015 Science issue) — NOT cite Buenrostro alone.
- §3.2 scChIP-seq mention → add `rotem2015` (Drop-ChIP founding).
- §3.3 SMF discussion → add `doughty2024` as a representative *mechanistic* application of SMF (vs. assay-development citations).
- §3.3 methylome assays → add `luo2018` snmC-seq2 alongside existing snmC-seq references.
- §3.3 methylation conceptual framing → add `schubeler2015` review for "methylation as consequence vs cause."
- §3.5 brain 3D-genome → add `liu2023` mouse brain atlas as the largest snm3C-seq production.
- §4 scATAC analysis methods → add `yuan2022` scBasset (deep-CNN sequence model).
- §5 brain mosaicism → MUST cite `kriz2025` Duplex-Multiome as the SOTA snATAC+snRNA + duplex consensus approach; cite `mukamel2025` for aneuploidy via methylome.
- §5 cancer applications → add `kim2018` TNBC chemoresistance as canonical longitudinal scDNA+scRNA cancer study.
- §5 cancer driver-landscape context → optional add `frankell2019` for EAC bulk-cohort reference.
- §5 clonal-hematopoiesis / normal-tissue lineage → MUST cite `leesix2018` as founding colony-WGS HSC phylogeny.

**Corpus state**: 107 summary pages now. Remaining unsummarized in `00-Sources/papers/`: ~13 candidates including Alex_2022, Anna_2022 (likely Nam), Andrew_2011, Benjamin_2024_bioRxiv, Chenghang_2012 (Zong MALBAC — verify against existing zong2012), Chongyi_2017 (Chen LIANTI — verify against chen2017), Cristiana_2019, David_2021, Dongsung_2019, Federico_2019/2021, Hongshan_2013 (Guo scRRBS — verify against guo2013), Hyobin_2023, Iain_2014, Jan_2020, Jeffrey_2021. Several likely already in bib via founding-method keys — needs verification on next batch.

**Notes**: This batch hit four major founding-citation gaps simultaneously: (i) sci-ATAC-seq Cusanovich; (ii) Drop-ChIP Rotem; (iii) snmC-seq2 Luo; (iv) Lee-Six HSC WGS phylogeny. Combined with prior Buenrostro 2015 ingest, the §3.2 scATAC origin story is now fully cited. The §5 brain-mosaicism section now has a complete trio of recent state-of-the-art anchors: Kriz Duplex-Multiome (sSNV via duplex+multiome), Mukamel (aneuploidy via methylome), Peter brain Fiber-seq (chromatin via SMF) — all cite-ready.

---

## 2026-05-13 — Ingest batch 15 (11 papers ingested, 1 off-topic, pure ingest)

**Trigger**: User "Continue ingesting". Computational/methods-review-heavy batch covering remaining bioinformatics tools and field reviews.

**Papers ingested (11)**:
- `Bin_2024_CancerPathogenesisTherapy` = **Lu 2024 CNA phylogeny review** — Surrey-based review of cancer phylogenetic inference using CNAs.
- `Felix_2011_Bioinformatics` = **Krueger 2011 Bismark** — the founding bisulfite aligner. Closes major §3.3 tool-citation gap.
- `Mckinzie_2023_ScientificData` = **Garrison 2023 BSMN data resources** — 400+TB BSMN consortium data descriptor.
- `Monica_2022_ComputationalStructuralBiotechnologyJournal` = **Valecha/Posada 2022** — scDNA SNV-calling review.
- `Siyuan_2024_GenomeBiology` = **Luo/von Meyenn 2024** — scATAC computational-methods benchmark (8 pipelines, 10 metrics).
- `Waleed_2023_GenomicsProteomicsBioinformatics` = **Iqbal/Zhou 2023** — scDNA methylome computational-tools review (UPenn/CHOP).
- `Wenjie_2025_BriefingsInBioinformatics` = **Sun 2025 scMitoMut** — beta-binomial mtDNA mutation caller (Perié lab, Curie).
- `Yan_2024_BriefingsInBioinformatics` = **Xiao/Wei 2024** — 12-method multi-omics integration benchmark (Tsinghua).
- `Hamim_2016_NatureMethods` = **Zafar 2016 Monovar** — founding scDNA SNV caller (Nakhleh + Navin labs). Existing `zafar2016` bibkey already present.
- `Hamim_2017_GenomeBiology` = **Zafar 2017 SiFit** — finite-sites tumor phylogeny (Nakhleh + Navin labs). Existing `zafar2017` bibkey already present.
- `Boying_2021_GenomeBiology` = **Gong/Purdom 2021 Cobolt** — MVAE multimodal integration (Berkeley). Predecessor of MultiVI.

**Off-topic/skipped**:
- `Kailong_2024_GenomeBiology` — **Zhao 2024 FoldPAthreader** — protein folding pathway prediction. Completely unrelated to scDNA/mosaicism/multi-omics. Second off-topic file detected in corpus (first was Joanna_2023). Suggests an eventual full corpus-lint pass to catch any other off-topic files.

**Pages created**: 11 summaries in `10-Summaries/`.

**BibTeX added**: 9 new entries (`lu2024cnaphylogeny`, `krueger2011bismark`, `garrison2023bsmn`, `valecha2022review`, `luo2024scatacbenchmark`, `iqbal2023methylomereview`, `sun2025scmitomut`, `xiao2024multiomicsbenchmark`, `gong2021cobolt`). Pre-existing keys reused: `zafar2016`, `zafar2017`.

**Index updated**: New "Batch 15 bioinformatics tools + reviews + benchmarks" subsection.

**Retroactive citation flags** (for next revision pass):
- §3.3 must cite `krueger2011bismark` at the entry point of every methylation processing pipeline discussion.
- §4 multimodal integration must cite `gong2021cobolt` as the Cobolt origin, alongside MultiVI/GLUE/MOFA+.
- §4 SNV-calling must cite `zafar2016` (Monovar) as the founding scDNA SNV caller.
- §4 phylogeny must cite `zafar2017` (SiFit) alongside SCITE/SCARLET in the finite-vs-infinite-sites comparison.
- §4 + §6 should cite `valecha2022review` and `iqbal2023methylomereview` as the canonical computational-methods reviews for SNV-calling and methylome-analysis respectively.
- §3.1 mtDNA should cite `sun2025scmitomut` alongside MAESTER/mgatk/Hsieh.
- §5 (brain mosaicism) must cite `garrison2023bsmn` as the consortium data-resource reference.
- §4 + §6 should cite `lu2024cnaphylogeny` and `luo2024scatacbenchmark` for tool-comparison best-practices.

**Notes**: Cumulative session total now ~57 summaries (batches 11–15). Remaining unsummarized corpus ~25 papers — increasingly skewed toward applications, specialized methods (Andrew_2011 = Hashimshony CEL-seq? CIRCLE-seq?), and earlier-vintage methods I haven't reviewed yet. Two off-topic detections total (Joanna_2023, Kailong_2024) — suggests final corpus lint pass to confirm no others lurk.

---

## 2026-05-13 — Ingest batch 14 (11 papers ingested, 1 corrupted, pure ingest)

**Trigger**: User "Continue ingesting". Targeted batch on remaining bioinformatics tools, tumor phylogeny, and §3.2 single-molecule extensions. 11 of 12 candidates successfully ingested; 1 PDF corrupted.

**Papers ingested (11)**:
- `August_2017_NucleicAcidsResearch` = **Huang 2017 MosaicHunter** — Wei-lab Bayesian unpaired postzygotic-SNM caller (PKU). Direct predecessor of MosaicForecast/DeepMosaic; the Wei → Park → Gleeson lab lineage clusters here.
- `Camila_2020_PLOSComputationalBiology` = **de Souza 2020 Epiclomal** — probabilistic clustering of sparse scBS-seq (Shah lab, BC Cancer). Introduces "epiclone" concept.
- `Chantriolnt_2019_GenomeBiology` = **Kapourani 2019 Melissa** — Bayesian clustering + imputation of single-cell methylomes (Sanguinetti lab, Edinburgh).
- `Chantriolnt_2021_GenomeBiology` = **Kapourani 2021 scMET** — Bayesian quantification of methylation heterogeneity (Vallejos + Sanguinetti, Edinburgh).
- `Cyril_2024_CellReportsMethods` = **Peter 2024 brain Fiber-seq** — Fiber-seq adapted for FACS-sorted NeuN+/− human brain nuclei (Akbarian + Stergachis labs).
- `Gryte_2020_CellSystems` = **Satas 2020 SCARLET** — single-cell tumor phylogeny with CN-constrained mutation losses (Raphael lab, Princeton).
- `Katharina_2016_GenomeBiology` = **Jahn 2016 SCITE** — founding MCMC-based single-cell tumor-phylogeny method (Beerenwinkel lab, ETH).
- `Stephanie_2024_GenomeResearch` = **Bohaczuk 2024 targeted Fiber-seq** — CRISPR-enriched Fiber-seq for mosaic-variant chromatin impact (Stergachis lab, UW). Case studies: DMPK CTG-repeat in DM1; HBG1/HBG2 base-editing for sickle cell.
- `Xian_2020_GenomeBiology` = **Mallory 2020** — review of scDNA CNA-detection methods (Nakhleh + Navin labs).
- `Yuhsin_2026_NatureCommunications` = **Hsieh 2026** — single-cell mtDNA mosaicism via mtscATAC-seq + POLG-D274A KI cells (Ludwig + Lareau labs, Charité Berlin / MSKCC). **First 2026-dated source in corpus.**
- `Yunhao_2019_GenomeResearch` = **Wang 2019 MeSMLR-seq** — foundational methyltransferase + Nanopore single-molecule footprinting in yeast (Au lab, OSU). Predates SMAC-seq and Fiber-seq.

**Corrupted/skipped**:
- `Matthew_2020_GenomeBiology` — PDF corrupted (`Couldn't find trailer dictionary`, `Couldn't read xref table`). Flagged for re-attempt with different extraction tool.

**Pages created**: 11 summaries in `10-Summaries/`.

**BibTeX added**: 11 new entries (`huang2017mosaichunter`, `desouza2020epiclomal`, `kapourani2019melissa`, `kapourani2021scmet`, `peter2024brainfiberseq`, `satas2020scarlet`, `jahn2016scite`, `bohaczuk2024targetedfiberseq`, `mallory2020review`, `hsieh2026mtdna`, `wang2019mesmlr`).

**Index updated**: New "Batch 14 computational tools + tumor phylogeny + mosaic chromatin" subsection.

**Retroactive citation flags** (for next revision pass):
- §4 mosaic-caller family must cite `huang2017mosaichunter` as the founding unpaired caller alongside the Ha 2023 benchmark recommendations.
- §3.3 + §4 methylation-clustering paragraph should cite the trio `desouza2020epiclomal`, `kapourani2019melissa`, `kapourani2021scmet` for the three statistical philosophies (mixture-model vs region-profile vs heterogeneity-quantification).
- §3.2 Fiber-seq paragraph should cite `peter2024brainfiberseq` for brain application and `bohaczuk2024targetedfiberseq` for targeted-mosaic chromatin readout.
- §4 phylogenetic-methods paragraph should cite `jahn2016scite` as the founding SCITE reference and `satas2020scarlet` as the joint SNV+CNA extension.
- §4 CNA-detection paragraph should cite `mallory2020review` as the canonical method-survey reference.
- §3.1 mtDNA paragraph should cite `hsieh2026mtdna` alongside `lareau2021` and `miller2022maester` for the latest per-cell mtDNA-mosaicism quantification framework.
- §3.2 single-molecule-footprinting family paragraph should cite `wang2019mesmlr` as historical predecessor of SMAC-seq / Fiber-seq.

**Notes**: First 2026-dated paper enters the corpus (Hsieh 2026 in Nat Commun) — confirming our cutoff is current. After this batch ~36 unsummarized papers remain. Next batches will continue toward §5 application coverage and remaining specialized methods.

---

## 2026-05-13 — Ingest batch 13 (12 papers, pure ingest, founding-methods continuation)

**Trigger**: User "Continue ingesting". Targeted batch focused on remaining NBT/NatMethods/NatGenetics/GenomeRes/GenomeBiol founders. All 12 highly relevant — second consecutive zero-failure batch.

**Papers ingested (12)**:
- `Charles_2014_PLOSOne` = **de Bourcy 2014** (Quake lab) — first systematic WGA-chemistry benchmark (MDA vs MALBAC vs NEB-WGA/PicoPLEX).
- `Jason_2015_Nature` = **Buenrostro 2015** — founding **scATAC-seq** paper on Fluidigm C1 (parallel to Cusanovich 2015 sci-ATAC-seq). Closes a major §3.2 founding-citation gap.
- `Ashley_2020_NatureBiotechnology` = **Sanders 2020 scTRIP** — Strand-seq tri-channel SV calling (Korbel lab, EMBL).
- `Simone_2020_NatureBiotechnology` = **Zaccaria 2021 CHISEL** — allele/haplotype-specific CNV from <0.05× scDNA (Raphael lab, Princeton).
- `Xiaoxu_2023_NatureBiotechnology` = **Yang 2023 DeepMosaic** — CNN-based mosaic-variant caller (Gleeson lab, UCSD).
- `Yu_2025_NatureBiotechnology` = **Xiao 2025 EpiTrace** — chromatin-accessibility-based mitotic-age clock from scATAC-seq.
- `Zhijie_2022_NatureBiotechnology` = **Cao 2022 GLUE** — graph-linked unified embedding for unpaired multi-omics (Gao lab, PKU).
- `Isac_2020_NatureMethods` = **Lee 2020 nanoNOMe** — nanopore joint chromatin-accessibility + methylation (Timp lab, JHU).
- `Xiao_2017_NatureMethods` = **Dong 2017 SCcaller + SCMDA** — scWGS variant caller with allelic-bias correction (Vijg lab, Einstein).
- `Jin_2023_NatureGenetics` = **Bae 2023 CODEC** — concatenated single-duplex sequencing (Adalsteinsson lab, Broad).
- `Maurizio_2018_GenomeResearch` = **Pellegrino 2018** — founding Mission Bio Tapestri droplet scDNA in AML.
- `Tom_2022_GenomeBiology` = **Kaufmann 2022 MEDICC2** — WGD-aware CN phylogeny (Schwarz lab, BIH Berlin).

**Pages created**: 12 summaries in `10-Summaries/`.

**BibTeX added**: 11 new entries (`debourcy2014`, `sanders2020sctrip`, `zaccaria2021chisel`, `yang2023deepmosaic`, `xiao2025epitrace`, `cao2022glue`, `lee2020nanonome`, `dong2017sccaller`, `bae2023codec`, `pellegrino2018tapestri`, `kaufmann2022medicc2`). Pre-existing key reused: `buenrostro2015`.

**Index updated**: New "Batch 13 founding methods + cancer + computational" subsection.

**Retroactive citation flags** (for next revision pass):
- §3.2 must cite `buenrostro2015` as the founding scATAC-seq reference, alongside `cusanovich2015` sci-ATAC-seq.
- §3.1 should cite `debourcy2014` in the WGA-chemistry-comparison paragraph.
- §3.1 Strand-seq paragraph should cite `sanders2020sctrip` for SV calling.
- §3.1 CNV/allele-specific discussion should cite `zaccaria2021chisel` alongside `laks2019` DLP+.
- §4 mosaic-caller family must cite `yang2023deepmosaic` and `dong2017sccaller` alongside MosaicForecast / MosaicHunter / LiRA / SCAN-SNV.
- §3.3 + §4 lineage-tracing section should cite `xiao2025epitrace` as chromatin-clock sibling to MethylTree/EPI-Clone.
- §4 multimodal-integration paragraph should cite `cao2022glue` alongside MOFA, MultiVI, Cobolt.
- §3.2 + §3.3 should cite `lee2020nanonome` in long-read joint-assay paragraph alongside SMAC-seq.
- §3.1 duplex paragraph should cite `bae2023codec` as the third major duplex chemistry (after `schmitt2012` Duplex Sequencing and `abascal2021` NanoSeq).
- §3.1 targeted-panel droplet paragraph + §5 cancer applications should cite `pellegrino2018tapestri` as the founding Tapestri reference.
- §5 cancer applications + §4 phylogenetic tools should cite `kaufmann2022medicc2` (paired with `zaccaria2021chisel`).

**Notes**: Two cumulative session totals: 24 summaries (batches 12+13) covering the largest remaining founding-method gaps. After this batch, the unsummarized corpus is heavily weighted toward applications and computational variants. Anticipated next batch: §5 application anchors (cancer-specific, neuroscience-specific, development/embryo).

---

## 2026-05-13 — Ingest batch 12 (12 papers, pure ingest, strongest batch)

**Trigger**: User "Continue ingesting". Batch targeted long-standing citation gaps in founding-method references and computational tools. All 12 PDFs identified as highly relevant — first batch in this session with zero off-topic / corrupted / off-scope entries.

**Papers ingested (12)**:
- `Takashi_2013_Nature` = **Nagano 2013 single-cell Hi-C** — the founding scHi-C paper (Babraham/Weizmann/Cambridge). Closes the long-standing §3.5 founding-citation gap.
- `Michael_2012_PNAS` = **Schmitt 2012 Duplex Sequencing** — founding paper for double-strand consensus error correction (Loeb lab, UW). Closes §3.1 duplex-sequencing founding-citation gap; existing `schmitt2012` bibkey already present.
- `Sai_2020_Cell` = **Ma 2020 SHARE-seq** — Regev/Buenrostro joint scATAC + scRNA combinatorial-indexing method, introduces DORCs and chromatin-potential concept.
- `Wenfei_2015_Nature` = **Jin 2015 scDNase-seq** — single-cell DNase-I hypersensitivity (Zhao lab, NIH), with FFPE-compatibility demo on follicular thyroid carcinoma. Existing `jin2015` bibkey already present.
- `Tal_2023_NatureMethods` = **Ashuach 2023 MultiVI** — scvi-tools deep-generative model for paired+unpaired multimodal integration.
- `Stephen_2018_NatureCommunications` = **Clark 2018 scNMT-seq** — founding triple-omics (methylation + accessibility + transcription) single-cell assay (Reik/Stegle labs). Existing `clark2018` bibkey already present.
- `Kai_2024_NatureMethods` = **Zhang 2024 SnapATAC2** — Ren-lab Rust-based matrix-free spectral embedding for million-cell single-cell omics.
- `Zohar_2020_NatureMethods` = **Shipony 2020 SMAC-seq** — Greenleaf-lab single-molecule long-read accessibility via dual m6A + 5mC methyltransferases + Nanopore.
- `Tyler_2022_NatureBiotechnology` = **Miller 2022 MAESTER** — mtDNA-variant enrichment from 3' scRNA-seq (van Galen/Sankaran labs); maegatk toolkit.
- `Yanmei_2020_NatureBiotechnology` = **Dou 2020 MosaicForecast** — Park/Walsh-lab read-phasing-based mosaic caller (no matched control); 80-90% validation rate on brain WGS.
- `Jinzhuang_2023_NatureBiotechnology` = **Dou 2023 Monopogen** — LD-refinement SNV caller for any single-cell modality (Ken Chen lab, MD Anderson).
- `Yoojin_2023_NatureMethods` = **Ha 2023 mosaic-caller benchmark** — Yonsei/POSTECH 11-strategy benchmark on 354K control-positive mosaic SNVs; recommends M2SMH meta-strategy.

**Pages created**: 12 summaries in `10-Summaries/`.

**BibTeX added**: 7 new entries (`ashuach2023multivi`, `zhang2024snapatac2`, `shipony2020smac`, `miller2022maester`, `dou2020mosaicforecast`, `dou2023monopogen`, `ha2023benchmark`). Pre-existing keys reused: `nagano2013`, `schmitt2012`, `ma2020`, `jin2015`, `clark2018`.

**Index updated**: New "Batch 12 founding-method + tools" subsection in `index.md`.

**Retroactive citation flags** (for next revision pass):
- §3.5 should cite `nagano2013` as the founding scHi-C reference (currently cites Ramani sciHi-C without crediting Nagano).
- §3.1 should cite `schmitt2012` as the duplex-sequencing founding reference alongside `abascal2021` (NanoSeq extension).
- §3.2 should cite `ma2020` SHARE-seq in the joint scATAC+scRNA paragraph alongside `cao2018` sci-CAR.
- §3.2 should cite `jin2015` scDNase-seq alongside `buenrostro2015` scATAC-seq and `cusanovich2015` sci-ATAC-seq as the three foundational scAccessibility methods.
- §3.2 should cite `shipony2020smac` alongside `stergachis2020` in the single-molecule-footprinting family paragraph.
- §3.3 should cite `clark2018` scNMT-seq as the founding triple-omics reference (already cited in passing but worth elevating).
- §4 should cite `ashuach2023multivi`, `zhang2024snapatac2` in computational tools.
- §4 mosaic-caller list should be expanded with `dou2020mosaicforecast`, `dou2023monopogen`, `ha2023benchmark` — Ha 2023 is the authoritative benchmark and should be the headline reference.
- §3.1 mtDNA paragraph should cite `miller2022maester` alongside `lareau2021`.

**Notes**: This batch covers the largest "founding paper" gap in the corpus. After this batch, the remaining unsummarized papers in `00-Sources/papers/` skew toward applications, less-prominent methods, and computational/benchmark variants. Next batches will likely shift toward §5 application anchors.

---

## 2026-05-13 — Ingest batch 11 (11 papers, pure ingest)

**Trigger**: User requested "continue ingesting". Pure ingest, no drafting this round. Focus on filling remaining methodology gaps and §5 application anchors.

**Papers ingested (11)**:
- `Longzhi_2018_Science` = **Tan 2018 Dip-C** — diploid haplotype-resolved single-cell 3D genome (Xie lab). Major §3.5 anchor; ~5× more contacts/cell than scHi-C.
- `Sebastien_2014_NatureMethods` = **Smallwood 2014 scBS-seq** — founding genome-wide single-cell bisulfite method (Reik / Kelsey labs).
- `Veronica_2021_PNAS` = **Gonzalez-Pena 2021 PTA** — primary template-directed amplification; current scWGA state-of-the-art (Gawad lab).
- `Tongtong_2022_Nature` = **Zhao 2022 slide-DNA-seq** — spatial scDNA-seq from intact tissue sections (Chen + Buenrostro labs). Major §3.5/§5 anchor for spatial axis.
- `Sebastian_2017_eLife` = **Pott 2017 scNOMe-seq** — single-cell joint methylation + accessibility + nucleosome phasing via GpC-MTase footprinting.
- `Christof_2017_GenomeBiology` = **Angermueller 2017 DeepCpG** — deep-learning imputation of single-cell methylation (Stegle / Reik labs).
- `Tyler_2015_NatureMethods` = **Garvin 2015 Ginkgo** — web platform for single-cell CNV analysis (Wigler / Schatz labs).
- `Junyue_2018_Science` = **Cao 2018 sci-CAR** — founding joint scATAC + scRNA via combinatorial indexing (Shendure lab).
- `Bora_2020_CancerCell` = **Lim, Lin & Navin 2020** — cancer + single-cell genomics review (Navin lab).
- `Masaki_2019_MolecularPsychiatry` = **Nishioka 2019** — brain somatic mutations × psychiatric research review (Iwamoto / Kato, RIKEN).
- `Mengyang_2025_NatureMethods` = **Chen 2025 MethylTree** — methylation-epimutation lineage tracing from sparse scBS-seq (Wang lab, Westlake).

**Skipped — off-topic**:
- `Joanna_2023_NatureCommunications` = Liu/Linington 2023 — collateral sensitivity profiling in antimicrobial-resistant *E. coli* / cephalosporin resistance. NOT scDNA / mosaicism / multi-omics. Flag as off-topic; should not have been in source folder. Possibly mislabeled. Leave PDF in `00-Sources/papers/` but do not summarize.

**Wiki pages created (11 summaries)**:
`tan-2018-science.md`, `smallwood-2014-natmethods.md`, `gonzalez-pena-2021-pnas.md`, `zhao-2022-nature.md`, `pott-2017-elife.md`, `angermueller-2017-genomebiol.md`, `garvin-2015-natmethods.md`, `cao-2018-science.md`, `lim-2020-cancercell.md`, `nishioka-2019-molpsych.md`, `chen-2025-methyltree.md`.

**Bibliography**: 7 new BibTeX entries (tan2018, angermueller2017, garvin2015, zhao2022slide, lim2020, nishioka2019, chen2025methyltree). Pre-existing keys: smallwood2014, gonzalez2021, pott2017, cao2018.

**Findings / cross-section connections noted**:
- Tan 2018 Dip-C should be retroactively added to §3.5 — it's the haplotype-resolved single-cell 3D-genome reference that §3.5 currently doesn't cite explicitly.
- Smallwood 2014 scBS-seq should be added to §3.3 historical line — predates and parents the snmC-seq2/3 chemistry. Currently §3.3 jumps from scRRBS to snmC-seq2 without mentioning scBS-seq.
- Gonzalez-Pena 2021 PTA is *already* cited in §3.1 via `gonzalez2021` — now properly summarized.
- Zhao 2022 slide-DNA-seq opens the spatial scDNA axis explicitly. Add to §3.5 (spatial genomics) and §5 (cancer, tissue-resolved clonal architecture). Currently §3.5 mentions IGS (Payne 2021) as the spatial reference; slide-DNA-seq is the higher-throughput counterpart.
- Cao 2018 sci-CAR should be retroactively added to §3.2 / §2 joint-assay table — currently in references.bib but not explicitly cited. It's the founding joint scATAC + scRNA method.
- Chen 2025 MethylTree complements Scherer 2025 EPI-Clone: both use methylation for lineage, but MethylTree uses sparse genome-wide scBS-seq while EPI-Clone uses targeted scTAM-seq. Add to §3.3 lineage-tracing block.
- Off-topic Joanna_2023 paper detected — first non-relevant source found in the corpus. Suggests doing a corpus-scan lint pass next session to identify any other off-topic files.

**Pending after this session**:
- Source files unsummarized: ~70 of 174 (or ~69 if we exclude Joanna_2023 as off-topic).
- Draft sections pending: §5 (applications), §6 (limitations), §7 (future perspectives), §8 (conclusion).
- §5 anchors are now overflowing — cancer (Kim, Cortés-López, Nam 2019/2022, Izzo, Frankell, Lim 2020 review), neuroscience (Lodato 2015/2018, Bae 2018/2022, Miller 2022, McConnell 2017, Mukamel 2025, Nishioka 2019), development (Coorens 2021, Argelaguet 2019, McKenna 2016, Chen 2025 MethylTree four-cell-stage), aging/CH (Vijg 2020, Cagan 2022, Lee-Six 2018, Scherer 2025, Mitchell 2022), spatial cancer (Zhao 2022). Easily draftable.

---

## 2026-05-13 — Draft §3.5 + §4 (no new ingest)

**Trigger**: User confirmed continuation; both sections fully anchored after batch-10 ingest. Pure drafting session.

**Draft sections written**:
- `60-Draft/sections/03-5-3d-genome.tex` — ~1700 words. Five subsections: scHi-C and extensions (Nagano 2013, Ramani 2017 sciHi-C, Dip-C); joint methylome + 3D-contact (Lee 2019 sn-m3C-seq, Liu 2023 brain atlas); in-situ genome sequencing (Payne 2021 IGS); data integration and analysis (Hong/Dao 2025 review, STARK/scNucleome); mosaicism implications (3D is most cell-state-dependent layer; genotype + 3D joint readout is least-developed axis; nucleolar regions underserved). Anchored by nagano2013, ramani2017, lee2019, liu2023, payne2021, lieberman2009, hong2025, bersaglieri2019, kriz2025.

- `60-Draft/sections/04-computational.tex` — ~2100 words. Five subsections: single-cell variant calling (Monovar, SCAN-SNV, LiRA, ProSolo + SiFit for tumor phylogeny); single-modality preprocessing tools (ArchR, Signac, cisTopic, chromVAR, EpiScanpy, snmC pipeline, scHi-C tools); multimodal integration (MOFA, Seurat WNN, Cobolt); sequence-based prediction + foundation models (scBasset, scGPT, Enformer, Sei, DeepHistone); locus-state inference status — what is established, what remains underdeveloped (genotype + epigenome joint readouts especially). Anchored by zafar2016, luquette2019, lodato2018, lahnemann2021, zafar2017, granja2021, stuart2021, derop2024, yuan2022, cui2024, gong2021, argelaguet2019, macaulay2014, gonzalez2021, falconer2012, sanders2017.

**main.tex**: §3.5 and §4 placeholders replaced with `\input{}`. Date string updated — 8 sections drafted (§1, §2, §3.1, §3.2, §3.3, §3.4, §3.5, §4), only §5–§8 pending.

**Findings / cross-section connections noted**:
- §3.5 closes the methods sweep through the five locus-state layers. The chapter now has internal continuity: each modality section ends with a locus-state interpretation block and points forward to §4's integration framework.
- §4 explicitly articulates the locus-state-inference status at end: which joint-modality readouts are established, which are missing. Genotype + methylation, genotype + chromatin state, genotype + 3D contact are flagged as the principal remaining joint-readout gaps. This is the cleanest statement of the field's near-term computational frontier and may be worth foreshadowing in §2.
- §4 introduces the foundation-model framing (scGPT, scBasset, Enformer) that §7 future-perspectives can build on without redundancy.

**Pending after this session**:
- Source files unsummarized: ~80 of 174 (no change — pure drafting).
- Draft sections pending: §5 (applications: cancer, neuroscience, development, aging), §6 (limitations), §7 (future perspectives), §8 (conclusion).
- §5 is well-anchored by existing ingest: cancer (Kim 2018, Cortés-López 2023, Nam 2019/2022, Izzo 2024, Frankell 2019); neuroscience (Lodato 2015/2018, Bae 2018/2022, Miller 2022, McConnell 2017 BSMN, Mukamel 2025); development (Coorens 2021, Argelaguet 2019, McKenna 2016 GESTALT); aging (Vijg 2020, Cagan 2022, Lee-Six 2018); CH (Scherer 2025 EPI-Clone, Mitchell 2022). Draftable next session.

---

## 2026-05-13 — Ingest batch 10 (11 papers, pure ingest)

**Trigger**: User requested "continue ingesting" — pure ingest batch with no drafting this round. Focus on remaining methodology papers, with priority on §3.5 (3D genome) and §4 (computational) anchors.

**Papers ingested (11)**:
- `Dongsung_2019_NatureMethods` = **Lee 2019 sn-m3C-seq** — founding single-nucleus joint methylome + 3D-contact assay; 4,238 human PFC nuclei resolved into 14 cell types from methylome alone (Ecker / Dixon labs). **High-priority §3.5 anchor.**
- `Iain_2014_PLOSGenetics` = **Macaulay & Voet 2014** — scWGA methods review.
- `Florian_2024_NatureBiotechnology` = **De Rop 2024 PUMATAC** — systematic benchmark of 8 scATAC-seq protocols across 47 experiments using PBMCs (Aerts + Heyn labs). Initial extraction returned syntax errors but image rendering completed; readable.
- `David_2021_NatureCommunications` = **Lähnemann 2021 ProSolo** — joint single-cell + bulk SNV caller with explicit FDR control.
- `Han_2022_NatureMethods` = **Yuan & Kelley 2022 scBasset** — sequence-based CNN for scATAC.
- `Hamim_2016_NatureMethods` = **Zafar 2016 Monovar** — first single-cell-aware SNV caller.
- `Hamim_2017_GenomeBiology` = **Zafar 2017 SiFit** — finite-sites tumor phylogeny inference.
- `Haotian_2024_NatureMethods` = **Cui 2024 scGPT** — transformer foundation model pretrained on 33M cells.
- `Jan_2020_Cell` = **Vijg & Dong 2020** — Cell Perspective on somatic mutation and aging mechanisms.
- `Boying_2021_GenomeBiology` = **Gong 2021 Cobolt** — multimodal VAE for joint-modality + single-modality scRNA + scATAC integration.
- `Cristiana_2019_Cells` = **Bersaglieri 2019** — nucleolar genome organization review.

**Skipped**: `David_2020_GenomeBiology.pdf` (PDF corrupted — syntax errors, no trailer dictionary, xref table unreadable). Re-attempt with different extraction tool in a later session.

**Wiki pages created (11 summaries)**:
`lee-2019-natmethods.md`, `macaulay-2014-plosgenet.md`, `derop-2024-natbiotech.md`, `lahnemann-2021-natcomm.md`, `yuan-2022-natmethods.md`, `zafar-2016-natmethods.md`, `zafar-2017-genomebiol.md`, `cui-2024-natmethods.md`, `vijg-2020-cell.md`, `gong-2021-genomebiol.md`, `bersaglieri-2019-cells.md`.

**Bibliography**: 10 new BibTeX entries added (lee2019 already existed in bib; macaulay2014, derop2024, lahnemann2021, yuan2022, zafar2016, zafar2017, cui2024, vijg2020, gong2021, bersaglieri2019 added).

**Findings / cross-section connections noted**:
- Lee 2019 sn-m3C-seq is the methodological parent of the Liu 2023 brain-atlas snm3C-seq application. Strong §3.5 anchor — can build §3.5 around this + Liu 2023 + Nagano 2013 + Ramani 2017 + Payne 2021 IGS (all already-summarized).
- §4 computational framework now richly anchored: SCAN-SNV (Luquette 2019), LiRA (Lodato 2018), ProSolo (Lähnemann 2021), Monovar (Zafar 2016) for variant calling; ArchR (Granja 2021), Signac (Stuart 2021), SnapATAC, cisTopic, chromVAR, EpiScanpy, PUMATAC for scATAC; scBasset (Yuan 2022), scGPT (Cui 2024) for sequence-based / foundation models; MOFA (Argelaguet 2018), Cobolt (Gong 2021) for integration; SiFit/SCITE/OncoNEM for tumor phylogeny. Fully draftable next session.
- Vijg 2020 LOY framing is useful for §5 aging applications — 2.5–43.6% of men 40–70 in UK Biobank carry mosaic LOY, with broad disease associations. Add to §5 outline.
- Bersaglieri 2019 is tangential but useful for §6 limitations (nucleolar regions / NAD compartment underserved by current single-cell 3D methods).

**Pending after this session**:
- Source files unsummarized: ~80 of 174 remain (David_2020 to be re-attempted; Chin_2025 to be re-attempted).
- Draft sections pending: §3.5, §4, §5, §6, §7, §8.
- §3.5 now fully anchored (Lee 2019, Liu 2023, Nagano 2013, Ramani 2017, Payne 2021, Hong/Dao 2025).
- §4 now fully anchored.

---

## 2026-05-13 — Ingest batch 9 (11 papers) + draft §3.1

**Trigger**: User chose interleaved pattern ("ingest ~10 + draft §3.1") for the next cycle. Picked 12 unsummarized candidates; Chin_2025 exceeded 100MB extraction limit and was skipped.

**Papers ingested (11)**:
- `Aaron_2016_Science` = **McKenna 2016 GESTALT** — CRISPR combinatorial-barcode lineage tracing in zebrafish (Shendure lab).
- `Alex_2022_Nature` = **Cagan 2022** — 16-mammalian-species crypt WGS; mutation rate × lifespan = constant end-of-life burden (Sanger).
- `Anna_2022_NatureGenetics` = **Nam 2022** — GoT + methylome on DNMT3A-R882 clonal hematopoiesis; PRC2-target hypomethylation mechanism (Landau lab).
- `Assaf_2015_NatureBiotechnology` = **Rotem 2015 Drop-ChIP** — founding scChIP-seq via microfluidic droplets (Bernstein + Weitz labs).
- `Benjamin_2024_Nature` = **Doughty 2024** — SMF on engineered enhancers; TF cooperativity from nucleosome eviction by activation domains (Greenleaf + Bintu labs).
- `Charissa_2018_Cell` = **Kim 2018** — TNBC chemoresistance scDNA + scRNA in 20 patients; resistant genotypes pre-existing, resistant transcriptomes acquired (Navin lab).
- `Craig_2019_NatureGenetics` = **Frankell 2019** — 551-EAC OCCAMS bulk-cohort WGS; 77 driver genes. NOT single-cell — bulk counterpoint useful for §5 framing.
- `Darren_2015_Science` = **Cusanovich 2015 sci-ATAC-seq** — founding combinatorial-indexing scATAC method (Shendure lab).
- `Dirk_2015_Nature` = **Schübeler 2015** — canonical DNA-methylation function review.
- `Ester_2012_NatureMethods` = **Falconer 2012 Strand-seq** — founding directional-strand single-cell method; SCE at 23bp (Lansdorp lab).
- `Henry_2018_Nature` = **Lee-Six 2018** — 140 HSPC colonies; human HSC pool size 50K–200K, first direct in-vivo estimate (Sanger / Campbell).

**Skipped**: `Chin_2025_Nature.pdf` (>100MB; PDF extraction limit exceeded). Re-add to candidate list for next batch and use `pages` parameter or extract via different tool.

**Wiki pages created (11 summaries)**:
`mckenna-2016-science.md`, `cagan-2022-nature.md`, `nam-2022-natgenet.md`, `rotem-2015-natbiotech.md`, `doughty-2024-nature.md`, `kim-2018-cell.md`, `frankell-2019-natgenet.md`, `cusanovich-2015-science.md`, `schubeler-2015-nature.md`, `falconer-2012-natmethods.md`, `lee-six-2018-nature.md`.

**Draft section written**:
- `60-Draft/sections/03-1-genotype.tex` — ~2700 words. Six subsections: scWGA chemistries (DOP-PCR, MDA, MALBAC, LIANTI, PTA, Strand-seq/DLP+, single-cell-derived clones + LCM-WGS); single-cell readout topologies (postmitotic-neuron pipeline, cancer scDNA+scRNA, mtDNA, targeted-panel for joint assays); population-level duplex methods (NanoSeq + SMaHT benchmarking) as complement; computational variant calling (SCAN-SNV, LiRA); synthetic lineage tracing (GESTALT) as transgenic complement to natural mutations; locus-state interpretation. Anchored by dean2002, zong2012, chen2017, gonzalez2021, falconer2012, sanders2017, laks2019, abascal2021, leeSix2018, coorens2021, cagan2022, lodato2015, lodato2018, bae2018, bae2022, miller2022nature, evrony2012, kim2018, lareau2021, nam2019, izzo2024, cortes2023, nam2022, scherer2025, schmitt2012, kennedy2014, luquette2019, mckenna2016.

**Bibliography**: 10 new BibTeX entries — leeSix2018, cagan2022, mckenna2016, rotem2015, kim2018, frankell2019, schubeler2015, nam2022, doughty2024. (falconer2012 and cusanovich2015 already existed.)

**main.tex**: §3.1 placeholder replaced with `\input{}`. Date string updated to reflect 6 sections drafted. Only §3.5, §4, §5, §6, §7, §8 remain.

**Findings / cross-section connections noted**:
- Nam 2022 is unusually load-bearing for the review's central conceptual claim: joint genotype + methylome + transcriptome same-cell readout uncovers DNMT3A-R882 mechanism (PRC2-target hypomethylation) that no single modality alone reveals. Re-flag this in §2 conceptual framework if revising.
- Cagan 2022 places single-neuron genosenium (Lodato 2018) in a deep mammalian-constraint context — mutation rate is evolutionarily tuned to lifespan, not species-specific. Useful framing for §5 aging applications.
- Doughty 2024 connects single-molecule footprinting (§3.2) to TF mechanism (§3.4) by showing that TF cooperativity emerges from nucleosome eviction rather than physical TF-TF interactions. Cross-reference inserted in §3.4 already covers the relationship.
- Frankell 2019 is the only non-single-cell paper in this batch; valuable as a contrast in §5 framing (when does single-cell add value? when does bulk cohort still own the question?).

**Pending after this session**:
- Source files unsummarized: ~81 of 174 remain (Chin_2025 re-added).
- Draft sections pending: §3.5 (3D genome), §4 (computational), §5 (applications), §6, §7, §8.
- §3.5 anchored by Nagano 2013, Ramani 2017, Lee 2019 (sn-m3C-seq), Liu 2023 (snm3C atlas), Payne 2021 (IGS), Hong/Dao 2025 review — all already ingested. Can be drafted next session without further ingest.

---

## 2026-05-13 — Ingest batch 8 (11 papers) + draft §3.3 and §3.4

**Trigger**: User confirmed continuation plan ("okay let me do thtat") for interleaved ingest + drafting. Targeted Walsh-lab single-neuron foundational + lineage-tracing primary candidates; actual identification revealed broader scope including a Signac methods paper and an EPI-Clone lineage-tracing paper.

**Papers ingested (11)**:
- `Michael_2015_Science` = **Lodato 2015** — foundational scWGS of 36 neurons; somatic SNVs as lineage markers tracing back to pregastrulation founders (Walsh lab).
- `Michael_2017_Science` = **McConnell 2017** — founding BSMN review (Walsh, Vaccarino, Abyzov, TJ Bae, Park, Gleeson, et al.).
- `Michael_2018_Science` = **Lodato 2018** — LiRA pipeline; "genosenium" age-related sSNV accumulation; CS/XP acceleration; three NMF signatures (Walsh lab).
- `Michael_2022_Nature` = **Miller 2022** — somatic SNV excess in AD neurons; Signature C (oxidative damage); transcription-coupled NER strand bias (Walsh lab + Eunjung Lee).
- `Michael_2025_Nature` = **Scherer 2025 EPI-Clone** — transgene-free methylation-based lineage tracing via scTAM-seq (Rodríguez-Fraticelli + Velten labs). NOT a Walsh-lab paper — filename-prefix surprise.
- `Lovelace_2019_NatureCommunications` = **Luquette 2019 SCAN-SNV** — spatial allele-balance model for MDA scDNA-seq SNV calling (Park lab).
- `Tim_2021_Nature` = **Coorens 2021** — 511 LCM-WGS samples across 3 adults; asymmetric zygote daughter contributions; 301-crypt patches (Sanger / Stratton).
- `Tim_2021_NatureMethods` = **Stuart 2021 Signac** — Seurat-compatible single-cell chromatin toolkit (Satija lab). NOT a lineage paper — filename-prefix surprise.
- `Mariela_2023_CellStemCell` = **Cortés-López 2023 GoT-Splice** — four-modality joint assay (genotype + short-read RNA + long-read isoform + CITE-seq) in SF3B1-mutant MDS (Landau lab).
- `Ricard_2019_Nature` = **Argelaguet 2019** — scNMT-seq mouse gastrulation; MOFA decomposition; asymmetric epigenetic logic of germ-layer specification (Reik / Stegle / Marioni).
- `Hanqing_2023_Nature` = **Liu 2023** — whole-mouse-brain snmC-seq3 + snm3C-seq atlas; 301K methylomes + 176K joint methylome+3D; 4,673 cell groups; 2.6M DMRs (Ecker lab).

**Wiki pages created (11 summaries)** under `10-Summaries/`:
`lodato-2015-science.md`, `mcconnell-2017-science.md`, `lodato-2018-science.md`, `miller-2022-nature.md`, `luquette-2019-natcomm.md`, `coorens-2021-nature.md`, `stuart-2021-natmethods.md`, `cortes-lopez-2023-cellstemcell.md`, `argelaguet-2019-nature.md`, `liu-2023-nature.md`, `scherer-2025-nature.md`.

**Draft sections written**:
- `60-Draft/sections/03-3-methylation.tex` — ~2500 words. Subsections: single-cell bisulfite chemistries (scRRBS, scBS-seq, snmC-seq2/3, sciMETv2, TAPS, scTAM-seq); joint methylome readouts (scTrio-seq, scNMT-seq, snm3C-seq); methylation-based lineage tracing (drift, epimutation, EPI-Clone); mosaicism implications. Anchored by guo2013, smallwood2014, luo2018, liu2023, hou2016, clark2018, argelaguet2019, gaiti2019, scherer2025, scTAMseq2022, mulqueen2018, liu2019taps, lee2019. Closes with the point that scWGS-grade-genotype + methylome joint readout on the same cell remains the most underdeveloped joint axis.
- `60-Draft/sections/03-4-chromatin-state.tex` — ~2500 words. Subsections: CUT&RUN/CUT&Tag at single-cell resolution (Bartosovic 2021, Wu 2021, Kaya-Okur 2019); multiplexed multi-mark readouts (nano-CT, MulTI-Tag, scChIX-seq); TF occupancy (uliCUT&RUN, scCUT&Tag for Olig2/CTCF; cross-reference to scDAF-seq footprinting); polycomb and heterochromatic marks (scChIC-seq); locus-state interpretation (regulatory-element classification, cell-state inference, boundary-element function). Anchored by bartosovic2021, bartosovic2023, kaya2019, hainer2019, ku2019, ku2024, zhu2021, ku2021scchix, plus cross-refs to scDAF-seq and Duplex-Multiome.

**Bibliography**: 18 new BibTeX keys added to `references.bib` (lodato2015, mcconnell2017, miller2022nature, luquette2019, coorens2021 already existed but kept, stuart2021, cortes2023, argelaguet2019, liu2023, scherer2025, scTAMseq2022, karemaker2018, smallwood2014, mulqueen2018, ku2024, ku2019, wu2021, kaya2019, zhu2021, hainer2019, jeong2023, bartosovic2024, ku2021scchix/MulTI-Tag, tehranchi2018/CUT&RUN protocol).

**main.tex**: §3.3 and §3.4 placeholders replaced with `\input{}` directives. Date string updated. Five sections now drafted; §3.1, §3.5, §4–§8 remain.

**Findings / tensions noted**:
- Two filename-prefix surprises (Michael_2025 = Scherer EPI-Clone, not Walsh; Tim_2021_NatMethods = Stuart Signac, not lineage). Flagged in summaries.
- Synthesis gap restated more precisely: even with Duplex-Multiome closing the scWGS + chromatin gap, no published method reads scWGS-grade genotype + methylome on the same cell. This is a distinct sub-gap and is now explicit in §3.3.
- EPI-Clone clarifies that lineage and state information can be encoded in the same modality — supports the locus-state framework's claim that joint reading should be statistical, not necessarily separate-modality.

**Pending after this session**:
- Source files unsummarized: ~92 of 174 remain.
- Draft sections pending: §3.1, §3.5, §4, §5, §6, §7, §8.
- §3.1 needs the Evrony 2012 ingest before drafting can proceed; existing wiki content (MALBAC/LIANTI/PTA/scTrio + Lodato 2015/2018/Bae 2018/2022/Miller 2022) is now sufficient to draft most of it.

---

## 2026-05-13 — Draft v0: §1 + §2 + §3.2 of the review paper

**Trigger**: User confirmed PI identity (TJ Bae, Korea University) and requested parallel ingest + drafting. Scope decision: draft the three strongest-anchored sections this session (§1 Introduction, §2 Conceptual framework, §3.2 Chromatin accessibility / fiber-seq family) before further ingest; this preserves context budget for prose quality and produces a defensible draft chunk to share with the PI.

**Created in `60-Draft/`** (inside the wiki, git-tracked, LaTeX format):
- `main.tex` — preamble, title block, abstract, section includes, placeholders for sections §3.1, §3.3, §3.4, §3.5, §4–§8.
- `sections/01-introduction.tex` — ~3000 words. Subsections: mosaicism is the rule; bulk seq flattens structure; scDNA-seq emergence; toward single-cell multi-omics; existing reviews leave a gap; locus-state framework as this review's contribution.
- `sections/02-conceptual-framework.tex` — ~3000 words. Subsections: defining the locus state (5 components: sequence / methylation / accessibility / chromatin state / 3D); why mosaicism requires locus-state thinking; current state of joint locus-state measurement (with table of 18 representative methods and their locus-state coverage); regulatory interpretation layers; conceptual contribution.
- `sections/03-2-fiber-seq.tex` — ~2500 words. Subsections: single-molecule chromatin footprinting (from bulk to single cell); Fiber-seq's four principles (all-or-none actuation, co-actuation, boundary nucleosome positioning, single-molecule TF footprints); DAF-seq and scDAF-seq; the broader footprinting family (SAMOSA, SMRT-Tag, STAM-seq, HiDef-seq); conventional scATAC/scDNase/scTHS/scNOMe; locus-state interpretation of accessibility methods.
- `references.bib` — ~80 BibTeX entries curated from existing wiki summaries. Covers foundational mosaicism, brain mosaicism primary papers, duplex sequencing, scWGA chemistries, joint assays, existing reviews, atlas references, accessibility methods, chromatin state, 3D genome, single-molecule footprinting family, methylation lineage, snmC-seq.
- `README.md` — folder structure, build instructions (`pdflatex main; bibtex main; pdflatex main; pdflatex main`), notes on style (neutral voice, locus-state framework as conceptual contribution, synthesis-gap claim revised in light of Duplex-Multiome), TODO for next drafting session.

**Notable framing choices**:
- **Neutral field-wide voice throughout**, per user request. Bae 2018/2022 cited like any other reference; no lab-positioning language anywhere in the draft prose.
- **Conceptual contribution = locus-state framework**, not method-gap-identification. This is the revised novelty argument after Duplex-Multiome (Kriz 2025) and Mukamel 2025 closed the previously-claimed methodological gap (see [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]]).
- **Five-component locus state** (sequence / methylation / accessibility / chromatin state / 3D) is the organizing structure throughout the draft; each modality in §3 is presented as measuring particular components of the locus state.
- **Table of 18 methods × 5 components** in §2 makes the joint-measurement coverage question explicit, marks the 2025 gap-closing methods (Duplex-Multiome, scDAF-seq, Mukamel) directly.

**Total drafted**: ~8500 words across three sections. Remaining draft sections: 5 modality sub-sections (§3.1, §3.3, §3.4, §3.5) + §4–§8 (computational, applications, limitations, future, conclusion).

**Next drafting priorities**: §3.3 (methylation) and §3.4 (chromatin state) are draftable from existing wiki content without further ingest. §3.1 (genotype-centric) benefits from ingest of Walsh-lab single-neuron foundational papers (Lodato 2015/2018, Evrony 2012/2015) before drafting. §3.5 (3D genome) and §4 (computational) draftable from current wiki.

**Pending sources**: 103 of 174. Mass ingest continues as a parallel track; next batch should target the Walsh-lab foundational papers + lineage-tracing primary papers + brain organoid mosaicism.

---

## 2026-05-13 — Seventh ingest: 12-paper mass batch across §3.1, §3.3, §4.3, §4.5, §4.6, §5 — synthesis-gap closure

**Trigger**: User requested "ingest many papers as possible" after the 6th-batch neuro-mosaicism set. Strategy chosen: a 12-paper compact-summary batch across multiple review sections rather than one focused domain, to maximize §-coverage breadth.

**Major framing shift this session**: one of the 12 papers — [[10-Summaries/kriz-2025-duplex-multiome|Kriz 2025 *bioRxiv* / Duplex-Multiome]] (Walsh + Lee labs) — **methodologically closes the central gap articulated in [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]]**. Duplex-Multiome integrates duplex consensus sequencing into the 10X Multiome platform to jointly measure somatic SNVs + snATAC + snRNA in the same nucleus, scaled to 51,400 brain nuclei. **The "no single-cell assay yet exists" framing the synthesis note had used is now factually outdated.** The note was substantially revised to acknowledge this and reframe the review's contribution from method-gap-identification to conceptual-framework-articulation (DNA-centric locus-state framing as the interpretive lens for what these new assays measure).

**Ingested (12 papers)**:

**§3.1 — scWGA chemistry foundational**:
- [[10-Summaries/chenghang-2012-science]] — Zong/Xie 2012 *Science*: **MALBAC foundational**. Quasilinear preamp + exponential PCR; 93% coverage / 76% SNV detection from SW480 single cell.
- [[10-Summaries/chen-2017-lianti]] — Chen/Xie 2017 *Science*: **LIANTI**. Tn5+T7 linear amplification, 97% coverage / 17% ADO, micro-CNV resolution ~10 kb. Established post-lysis C→T deamination as the dominant single-cell SNV false-positive class.

**§3.3 — Single-cell methylome**:
- [[10-Summaries/guo-2013-scrrbs]] — Guo/Tang 2013: **scRRBS foundational**. 0.5–1.5M CpG sites per single mESC; first single-cell observation of asymmetric pronuclear demethylation kinetics. Chemistry behind [[sctrio-seq]].
- [[10-Summaries/luo-2018-snmc-seq2]] — Luo/Ecker 2018: **snmC-seq2**, improved chemistry that became the chassis for the BICCN mouse-brain methylome atlas and the [[mukamel-2025-aneuploidy-brain|Mukamel 2025]] aneuploidy work.

**§4.3 — Computational tools**:
- [[10-Summaries/granja-2021-archr]] — Granja/Greenleaf 2021: **ArchR**. R-based scATAC pipeline; 1.2M cells in 8h on a laptop; synthetic-doublet detection AUC 0.918.

**§4.5 — Lineage tracing**:
- [[10-Summaries/gaiti-2019-cll-epigenetic]] — Gaiti/Landau 2019 *Nature*: **epimutation as molecular clock** in CLL. 2,652 cells, methylation-based lineage trees, SF3B1 subclone emergence ~6 years before clinical sampling.
- [[10-Summaries/ludwig-2020-mtscatac-seq]] — Lareau/Sankaran 2021: **mtscATAC-seq**. ~20× higher mtDNA coverage than standard scATAC; mtDNA mutations as endogenous lineage barcodes in thousands of cells.

**§4.6 — Joint chromatin multimodal**:
- [[10-Summaries/bartosovic-2021-sccut-tag]] — Bartosovic/Castelo-Branco 2021: **scCUT&Tag in mouse brain** via 10x droplet platform. Histone marks + Olig2/Rad21 TFs.
- [[10-Summaries/bartosovic-2022-nano-cut-tag]] — Bartosovic 2023: **nano-CT**. Nanobody-Tn5 fusions enable simultaneous ATAC + 2 histone marks per nucleus. Chromatin velocity in oligodendrocyte lineage.
- [[10-Summaries/hyobin-2023-naturebiotechnology]] — Jeong/Korbel 2023: **scNOVA**. Strand-seq + haplotype-aware nucleosome occupancy infers gene-activity changes from SVs. CLL Wnt-subclone identification, T-ALL chromothripsis → Notch inhibitor targeting.

**§3.1 + §6 — Duplex sequencing for non-dividing tissue**:
- [[10-Summaries/abascal-2021-nanoseq]] — Abascal/Martincorena 2021 *Nature*: **NanoSeq**. <5 errors/billion bp; post-mitotic neurons accumulate mutations at constant rate throughout life — proves cell division not required for mutagenesis.

**§1 + §6 — Synthesis-gap-closing (preprint)**:
- [[10-Summaries/kriz-2025-duplex-multiome]] — Kriz/Walsh/Lee 2025 *bioRxiv*: **Duplex-Multiome**. Joint somatic SNVs + snATAC + snRNA-seq per nucleus, 51,400 human brain nuclei. 2% VAF sensitivity at 92% precision. **The first single-cell assay covering point mutations + chromatin + RNA genome-wide at scale**. Closes the gap previously articulated in the wiki's synthesis note.

**Updated existing pages**:
- [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]] — **major revision**. Added Duplex-Multiome as anchor #5 with detailed explanation; revised TL;DR with status update; revised the post-table summary to articulate the conceptual-vs-methodological gap distinction; updated the synthesis table to include Duplex-Multiome (🟢 marked) and mtscATAC-seq.
- `index.md` — added 7 new sub-sections under "Primary methods papers": scWGA chemistry, methylome foundational, joint-assay additions, lineage tracing, duplex (additional), SV single-cell, computational tools, **gap-closing methods (2025)**. Updated synthesis-note pointer to reflect status change.

**Notable findings / framings**:
- **The conceptual landscape has shifted in the past ~6 months.** Both [[10-Summaries/mukamel-2025-aneuploidy-brain|Mukamel 2025]] (atlas-scale aneuploidy + methylation, mouse brain) and [[10-Summaries/kriz-2025-duplex-multiome|Kriz 2025]] (SNV + chromatin + RNA, human brain) appeared in 2025. They make the planned review's novelty argument *significantly* sharper but also force the review to reframe: the "no joint-assay exists" claim is now wrong; the "no conceptual framework exists for interpreting joint measurements" claim is the defensible novelty.
- **The Walsh lab's continued anchor role**: Bae 2018/2022 (when Bae was at Mayo Clinic / Abyzov lab, BSMN/Walsh consortium) + Luquette/Walsh SMaHT + Andrea Kriz 2025 Duplex-Multiome — all Walsh-lab-affiliated. The neuro-mosaicism methodological program flows through this lab. The user's PI (TJ Bae) has direct ties to this network.
- **LIANTI's "post-lysis cytosine deamination" characterization** is the canonical reference for why single-cell SNV calling is hard. Every duplex-sequencing paper since 2017 cites it.
- **NanoSeq's post-mitotic neuron finding** (mutation accumulation at constant rate without division) bookends [[10-Summaries/bae-2017-pregastrulation-mutations|Bae 2018's]] finding (mutation rate ~5/day during neurogenesis division). Together they cover the lifelong brain mosaicism trajectory.
- **Landau lab's three-paper methodology arc**: GoT (Anna 2019) for SNV+RNA → epimutation lineage (Gaiti 2019) for methylation clock → GoT-ChA (Franco 2024) for SNV+chromatin. The §4.5 + §4.6 anchors for personalized cancer lineage in human disease.
- **mtDNA as endogenous lineage marker** is methodologically distinct from nuclear-mutation lineage (Bae 2018 clonal expansion) and engineered-scar lineage (CRISPR scar) — three independent pillars of single-cell lineage reconstruction for §4.5.

**Pending after this ingest**: 104 of 175. The next batch should target: (a) lineage tracing primary papers PI mentioned (CRISPR scar methods — Cai, Zhou, Loveless), (b) brain organoid mosaicism, (c) remaining Walsh-lab single-neuron foundational papers (Lodato 2015, Lodato 2018, Evrony 2012/2015, McConnell 2013).

**Skipped this session**: per-paper graph touches at depth (compact summaries used to enable 12-paper throughput); new entity pages for first authors. The wiki has many orphan-link entities now from accumulated batches — natural target for a future lint pass.

---

## 2026-05-12 — Sixth ingest: PI-priority neuro-mosaicism batch (Bae 2018, Bae 2022, Mukamel 2025 + Hainer 2019 uliCUT&RUN)

**Trigger**: User requested the 4-paper neuro-mosaicism batch flagged in the fifth-ingest log's "Next" section. Goal: anchor §1 (somatic mosaicism opening) and §5 (neuroscience applications) of the planned review with primary papers, and strengthen the [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]] novelty claim.

**Filename surprise**: `Sarah_2019_Cell.pdf` turned out to be **not** a Walsh-lab neuro-mosaicism paper but Hainer et al. 2019 *Cell* "Profiling of Pluripotency Factors in Single Cells and Early Embryos" — i.e., **uliCUT&RUN**, an ultra-low-input CUT&RUN method paper. Still wiki-valuable (sits between bulk CUT&RUN and sciCUT&Tag), so summarized but flagged as not-mosaicism. No primary Lodato 2015 or 2018 Walsh-lab papers are yet in 00-Sources/ — a future neuro batch should target them.

**Ingested (4 papers)**:
- [[10-Summaries/bae-2017-pregastrulation-mutations]] — Bae et al. 2018 *Science* 359:550. First-author Taejeong Bae (Abyzov lab, Mayo Clinic); senior authors Abyzov + Vaccarino. **Clonal-cell-population approach** (31 clones from 3 fetal brains), 200–400 SNVs/cell, mutation rate ~1.3/division pre-gastrulation vs ~8.6/division during neurogenesis (3 orders of magnitude higher than adult germline). **Mutation spectrum shifts CpG-deamination → oxidative damage** between the two developmental windows. 10% depletion of mosaic SNVs in fetal-brain DNase-hypersensitive sites — direct chromatin-state × mutation-distribution evidence.
- [[10-Summaries/taejeong-2022-science]] — Bae et al. 2022 *Science* 377:511. BSMN cohort: 131 brains across normal/Tourette/SCZ/ASD phenotypes at ≥200×. **~6% of brains hypermutable** (>101 SNVs), age-associated (16% >60y vs 2% <40y, P=8.2×10⁻³). Cancer-implicated gene mutations (NRAS, DNMT3A, TET2, MTOR, IDH2) overrepresented in hypermutable brains. **NRAS-driven clonal expansion in striatal interneurons of brain NC7** validated at 94% in single nuclei. **ASD brains enriched for somatic mutations creating MEIS TF binding motifs in fetal-brain enhancer-like regions** — the field's leading direct mosaic-mutation-to-regulatory-element causal pathway.
- [[10-Summaries/mukamel-2025-aneuploidy-brain]] — Mukamel et al. 2025 *Neuron* 113:2814. Salk + UCSD (Ecker lab). **snmC-seq logic for CNV detection extended to 415,103 BICCN mouse brain cells**. 0.175–0.349% aneuploidy rate. **Trisomy 16 (mouse syntenic with human chr21) 13-fold enriched** (P<10⁻³⁰⁰), cell-type-specifically concentrated in OPCs, Pons neurons, pericytes. **This is the scTrio-seq CNV-from-methylation trick scaled to atlas size** — a major new anchor for the synthesis claim.
- [[10-Summaries/sarah-2019-cell]] — Hainer et al. 2019 *Cell* 177:1319. uliCUT&RUN ultra-low-input CUT&RUN: TF mapping from 10 cells, single cells, blastocysts. Demonstrated NANOG binding in mouse blastocysts **depends on BRG1 in vivo** despite being BRG1-independent in cultured cells — a methodological lesson about bulk reference vs primary tissue.

**Created (new pages)**:
- 4 summary pages.
- 1 entity page: [[20-Entities/taejeong-bae]] — flags possible identity match with the wiki user's "Bae Lab" affiliation (per auto-memory `claude_group1@baelab.org`) but does not assume it; explicit ask for user confirmation.

**Updated existing pages**:
- [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]] — **major expansion**. Added Mukamel 2025 as a new direction ("Aneuploidy + epi at atlas scale, brain"), reorganized the synthesis table from 4 anchors to 6 (adding Mukamel + Bae 2022 ASD MEIS-motif), added a "Brain-mosaicism-specific anchors" section linking the five neuro-mosaicism summaries that anchor §1 + §5 of the planned review.
- [[30-Concepts/somatic-mosaicism]] — added 4 new examples (Bae 2018, Bae 2022 hypermutability, Bae 2022 ASD MEIS-motif, Mukamel 2025 chr16 trisomy enrichment).
- `index.md` — added 3 new entries under "Somatic mosaicism (primary papers)" and a new "Single-cell chromatin profiling (ultra-low-input)" sub-section for Hainer 2019.

**Notable findings / framings**:
- **The Mukamel 2025 paper is the most consequential addition to the synthesis note**. It demonstrates that **single-cell DNA methylation atlases can jointly yield CNV/aneuploidy calls at 1,000× the scale of scTrio-seq** — making "no single-cell assay jointly measures mosaic alteration + epi at scale" a weaker version of the claim than previously articulated. The updated synthesis is now: **no single-cell assay jointly measures point mutations + chromatin/methylation genome-wide at single-cell scale**; aneuploidy + methylation IS now achievable at atlas scale.
- **The Bae 2022 ASD MEIS-motif finding** is the field's leading direct-causal-pathway result for mosaic mutations in psychiatric disease. It interprets the somatic mutations via *bulk* fetal-brain epigenome reference. The synthesis note now flags this as the prototype "bulk-epigenome-annotated mosaicism" pathway — defensible for now, but the synthesis can argue that confirming the same locus is in an open-chromatin state in the actual mutant cell would require a future joint assay.
- **The Taejeong Bae authorship** likely overlaps with the wiki user's PI affiliation (baelab.org). Flagged on entity page for confirmation — the connection matters for the review paper's authority and is worth mentioning in the introduction.
- **Bae 2018's 10% depletion of mosaic SNVs in fetal-brain DHS sites** is direct same-cell-lineage chromatin × mutation evidence — biased away from accessible regions because of better DNA-repair efficiency in open chromatin, NOT negative selection. This is exactly the kind of direct epi × mutation coupling the planned review aims to articulate. Important reference for §3.1 + §6 + §7.
- **Two structural gaps remain after this ingest**:
  1. No Lodato 2015 / Lodato 2018 / Evrony 2012 / Evrony 2015 / McConnell 2013 — the foundational scWGS-based single-neuron mosaicism papers — are in the wiki yet, despite being referenced by Bae 2018/2022.
  2. No Bizzotto primary papers (only the review). Bizzotto/Walsh have multiple primary papers that would deepen the Walsh-lab mosaicism program coverage.

**Pending after this ingest**: 116 of 175. The next batch should target either (a) the foundational scWGS-based single-neuron papers (Lodato 2015, 2018; Evrony 2012, 2015; McConnell 2013), or (b) lineage-tracing primary papers for §4.5 (Spencer Chapman 2021, Coorens 2021, Fasching 2021).

**Skipped this session**:
- New entity pages for Eran Mukamel, Joseph Ecker (Salk). They will appear as orphan links until a future lint pass.
- Per-summary deep graph touches (5–15 pages each). This batch focused graph work on the synthesis note + somatic-mosaicism concept page — the highest-leverage targets.

**Recommendation for the review draft after this batch**:
- §1 (somatic mosaicism opening) can now cite Bae 2018 + Bae 2022 + Mukamel 2025 + Kousi/Kellis + Luquette/Walsh as primary-source-anchored statements about brain mosaicism scope and mechanism.
- §5 (neuroscience applications) has all five neuro-mosaicism summaries above as direct anchors.
- The synthesis note in 50-Notes/ can be cited directly from §6 (limitations) and §7 (future perspectives) — it's now a defensible standalone artifact with 6 anchor methods and ~80 lines of analysis.

---

## 2026-05-12 — Fifth ingest: PI-priority gap closure (Fiber-seq foundational + 6 joint-assay primary papers)

**Trigger**: User shared review-paper outline + PI feedback. PI asks for: (1) somatic-mosaicism opening framing, (2) fiber-seq family promoted in §3.2, (3) expanded §4.6 joint-assay coverage, (4) novelty claim "mutation + epi + DNA-centric at single-cell" with no precedent in existing review literature.

**Audit before ingest**: 95 wiki pages already existed. Strong coverage for DAF-seq, GoT/GoT-ChA, duplex/nanoseq, somatic mosaicism (DNA-only framing). Three critical gaps surfaced:
1. **Stergachis 2020 Fiber-seq foundational paper unread** — `AndrewB_2020_Science.pdf` in `00-Sources/` had no summary; concept page `fiber-seq.md` only referenced it indirectly via the Elliott 2025 DAF-seq paper.
2. **Mosaicism + epigenetics linkage absent** — `somatic-mosaicism.md` had zero mentions of methylation, chromatin, or epigenetics. `50-Notes/` was empty.
3. **§4.6 joint-assay primary papers absent** — no concept pages for sci-CAR, SHARE-seq, scNMT-seq, G&T-seq, DR-seq, scTrio-seq, or IGS.

**Pending sources discovered**: 129 of 175 — user had added many web clippings + primary PDFs between sessions. Scope decision: ingest only the 9 papers directly aligned with PI feedback (3 Stergachis-prefixed + 6 joint-assay), defer the other 120 to future batches by domain.

**Ingested (9 papers)**:
- **Fiber-seq family / chromatin foundational**:
  - [[10-Summaries/andrewb-2020-science]] — Stergachis et al. 2020 *Science*: Fiber-seq foundational paper. m6A-MTase chromatin stenciling, all-or-none actuation, boundary nucleosome model, single-molecule CTCF footprinting (only 30% of accessible CTCF sites bound on any given fiber).
  - [[10-Summaries/andrewc-2020-science]] — Payne et al. 2021 *Science*: IGS (In Situ Genome Sequencing). **NOT a Stergachis paper despite filename collision** — Andrew C. Payne, Buenrostro/Boyden/Chen labs at MIT/Broad. Genome-wide DNA + 3D spatial coordinates in single cells.
  - [[10-Summaries/andrew-2011-cellresearch]] — Bannister & Kouzarides 2011 *Cell Research*: foundational histone modifications review. **NOT Stergachis** — Andrew J. Bannister, Gurdon Institute.
- **Joint-assay primary papers (DNA + RNA / methylation + RNA / accessibility + RNA)**:
  - [[10-Summaries/macaulay-2015-gt-seq]] — Macaulay 2015 *Nat Methods*: G&T-seq, first single-cell joint DNA+RNA assay; separation-based.
  - [[10-Summaries/dey-2015-dr-seq]] — Dey 2015 *Nat Biotechnol*: DR-seq, one-pot alternative to G&T-seq.
  - [[10-Summaries/cao-2018-sci-car]] — Cao 2018 *Science*: sci-CAR, combinatorial-indexing scATAC + scRNA.
  - [[10-Summaries/ma-2020-share-seq]] — NRG perspective on Ma 2020 *Cell*: SHARE-seq + chromatin potential.
  - [[10-Summaries/clark-2018-scnmt-seq]] — Clark 2018 *Nat Commun*: scNMT-seq, first triple-omics (methylation + accessibility + RNA).
  - [[10-Summaries/hou-2016-sctrio-seq]] — Hou 2016 *Cell Research*: scTrio-seq, alternative triple-omics (CNV + methylation + RNA) — closest existing precedent for the PI's novelty claim.

**Created (new pages)**:
- 9 summary pages.
- 8 new concept pages: [[30-Concepts/sci-car]], [[30-Concepts/share-seq]], [[30-Concepts/scnmt-seq]], [[30-Concepts/gt-seq]], [[30-Concepts/dr-seq]], [[30-Concepts/sctrio-seq]], [[30-Concepts/igs]] (the eighth: existing fiber-seq.md was substantially rewritten — see Updated).

**Updated existing pages**:
- [[30-Concepts/fiber-seq]] — rewrote major sections with primary-source content (Stergachis 2020): operating point, all-or-none actuation, co-actuation in cis, boundary nucleosome model, single-molecule CTCF footprinting. Concept page grew from 44 to ~110 lines.
- [[30-Concepts/somatic-mosaicism]] — added "Mosaicism × epigenome — an open synthesis gap" section articulating the PI's novelty claim: scTrio-seq is the closest precedent (CNV + methylation + RNA), but no single-cell assay yet jointly measures point mutations + chromatin/methylation genome-wide. GoT-ChA is targeted; DAF-seq is single-fiber bulk-genome but ≤12 cells deeply benchmarked. The neuro-mosaicism field uses bulk epigenome annotations, not paired single-cell measurements. This is the gap the planned review can articulate.
- [[40-Topics/single-cell-multiomics]] — added 7 new joint-assay concept-page links to "Core concepts" section, and 4 new sub-theme sections for foundational joint DNA+RNA, joint chromatin + RNA, triple-omics, and spatial single-cell DNA.
- `index.md` — added two new sections: "Primary methods papers (joint DNA + epigenome + RNA assays)" and "Histone-modification foundational reviews", plus the Fiber-seq foundational paper entry under "Primary methods papers (multi-omics + genotyping)".

**Notable findings / framings**:
- **The mosaicism × epigenome novelty PI is pushing for has a concrete prior**: [[10-Summaries/hou-2016-sctrio-seq|scTrio-seq]] (Hou 2016) demonstrated CNV + methylation + RNA per cell, found that **CNVs drive expression dosage proportionally but do NOT alter local methylation**. This is the cleanest single-cell evidence that genomic alteration and epigenetic state are *partly decoupled* at the per-cell scale — a result only visible because all three layers were in the same cell. The wiki's [[30-Concepts/somatic-mosaicism]] page now flags this and the analogous gap for point mutations.
- **The Andrew_* filename collision was a near-miss**: `AndrewB_2020_Science.pdf` (Stergachis Fiber-seq), `AndrewC_2020_Science.pdf` (Payne IGS), and `Andrew_2011_CellResearch.pdf` (Bannister histone-mods review) share filename prefixes but are three unrelated papers from three labs. The wiki concept pages now flag this to prevent future cross-reference errors.
- **Two methodological lineages for joint DNA-anchored assays**: separation-based (G&T-seq → scNMT-seq; Reik / Kelsey / Stegle lineage) vs one-pot (DR-seq → scTrio-seq; van Oudenaarden / Tang lineage). Combinatorial-indexing (sci-CAR / SHARE-seq / 10x Multiome) is a third lineage that traded DNA for chromatin to scale throughput.
- **For §3.2 of the review**: fiber-seq concept page is now ready as primary-source-anchored. The Stergachis 2020 → Elliott 2025 (DAF-seq) → COLO829 low-VAF mosaic variant lineage is now traceable end-to-end through wiki pages.
- **For §4.6**: the joint-assay landscape now has 7 concept pages (G&T-seq, DR-seq, sci-CAR, SHARE-seq, scNMT-seq, scTrio-seq, IGS) on top of the existing GoT, GoT-ChA, DAF-seq, SpliCOOL-seq, scTEM-seq, scEpi²-seq, 6-base-CUT&Tag coverage. The DNA-anchored vs chromatin-anchored axis is now articulable.

**Skipped this session (deliberate scope discipline)**:
- 120 other pending sources (mostly fitting other domains: neuro-mosaicism primary papers, mtDNA/lineage tracing, computational tools, neuro-pathology). Natural future batches by domain.
- New entity pages for paper authors (Stephen J. Clark, Junyue Cao, Andrew C. Payne, Andrew J. Bannister, Yu Hou, Siddharth Dey, Iain Macaulay). The summaries link to them but the entity pages don't exist yet — they will appear as `[[]]` orphans in Obsidian until a lint pass.
- Per-summary deep graph touches (the CLAUDE.md ingest workflow asks for 5–15 page touches per source; this session focused those touches on the high-leverage pages — fiber-seq, somatic-mosaicism, single-cell-multiomics topic, index.md). Lighter graph touches for the 6 joint-assay papers can happen in a follow-up lint.

**Next**:
- User can now draft outline §3.2 (fiber-seq family with Stergachis 2020 as anchor) and §4.6 (joint-assay landscape with 7 newly-anchored concept pages).
- Natural promotion target for `50-Notes/`: the "Mosaicism × epigenome — open synthesis gap" section in [[30-Concepts/somatic-mosaicism]] is now substantive enough to spin out into a dedicated note page once it is the subject of a focused query or draft.
- Backlog: 120 sources still pending. PI hasn't flagged a third priority area yet; suggest the user prioritize by review-section need rather than mass ingest.

---

## 2026-05-12 — Fourth ingest: 31 web-clipping primary papers (methylation, ATAC, histone marks, 3D, long-read, duplex)

- **Discovered:** 31 `.md` web clippings in `00-Sources/papers/` (saved from journal websites and bioRxiv). All previously unsummarized. (The pending-sources script initially showed 32 entries due to a glob quirk around a filename containing parentheses; only 31 unique files exist.)
- **Strategy:** skim depth as planned for primary-paper batches (per third ingest log "Next" section). One ~250–400-word summary per clipping; aggressive cross-referencing with concept and entity pages.
- **Ingested clippings:**
  - **Duplex sequencing / mosaicism** (5): [[10-Summaries/kennedy-2014-duplex-protocol]] (Kennedy/Loeb 2014 founding DS), [[10-Summaries/nandi-2025-udseq]] (UDSeq, Alexandrov 2025), [[10-Summaries/zhang-2025-smaht-duplex-benchmark]] (SMaHT six-method benchmark), [[10-Summaries/luquette-2025-pta-duplex-mosaicism]] (SMaHT 102-nucleus PTA + DS), [[10-Summaries/glynos-2023-mtdna-mosaicism]] (Glynos/Chinnery 2023 single-cell mtDNA drift).
  - **Mosaicism biology** (2): [[10-Summaries/bizzotto-2022-brain-mosaicism-review]] (Bizzotto/Walsh NRN review), [[10-Summaries/kousi-2022-ad-mosaicism]] (Kousi/Kellis 2022).
  - **Methylation methods** (6): [[10-Summaries/hunt-2022-sctem-seq]], [[10-Summaries/bai-2024-simple-seq]], [[10-Summaries/shen-2026-splicool-seq]], [[10-Summaries/tavares-2026-6-base-cut-tag]] (6-base-CUT&Tag), [[10-Summaries/geisenberger-2025-scepi2-seq]] (scEpi²-seq), [[10-Summaries/kim-2017-methylation-memory-review]] (Kim/Costello memory review).
  - **scATAC-seq tooling** (7): [[10-Summaries/schep-2017-chromvar]] (chromVAR), [[10-Summaries/bravo-2019-cistopic]] (cisTopic), [[10-Summaries/fang-2021-snapatac]] (SnapATAC), [[10-Summaries/danese-2021-episcanpy]] (EpiScanpy), [[10-Summaries/zamanighomi-2018-scabc]] (scABC), [[10-Summaries/mezger-2018-microfluidic-atac]] (µATAC-seq), [[10-Summaries/gur-2025-scatac-vs-bulk]] (scATAC vs bulk).
  - **Histone modifications** (4): [[10-Summaries/ku-2019-scchic-seq]] (scChIC-seq), [[10-Summaries/yeung-2023-scchix-seq]] (scChIX-seq), [[10-Summaries/janssens-2023-scicut-tag]] (sciCUT&Tag), [[10-Summaries/yin-2019-deephistone]].
  - **3D genome** (2): [[10-Summaries/hong-2025-sc3d-genome-review]] (Hong/Dao 2025 review), [[10-Summaries/jiang-2026-stark-scnucleome]] (STARK + scNucleome).
  - **Long-read methods** (4): [[10-Summaries/liu-2025-long-read-epigenome-review]] (Liu/Conesa 2025 NRG review), [[10-Summaries/abdulhay-2020-samosa]] (SMRT-Tag/SAMOSA-Tag), [[10-Summaries/liu-2025-nanopore-lscc-svs]] (SomaGauss-SV in LSCC), [[10-Summaries/mo-2023-stam-seq]] (STAM-seq plant HRRs).
  - **scWGA variant caller** (1): [[10-Summaries/tu-2021-scout-genotyper]] (SCOUT).
- **Created (new pages in this ingest, ~110 total):**
  - 31 summary pages.
  - 4 new topic pages: [[40-Topics/duplex-sequencing]], [[40-Topics/single-cell-atac-seq]], [[40-Topics/histone-modifications]], [[40-Topics/3d-genome]].
  - ~70 new concept pages spanning: duplex methods (codec, nanoseq, hidef-seq, umi-molecular-barcoding, mutational-signatures); methylation chemistry (taps, 5hmc, nome-seq, sctem-seq, simple-seq, splicool-seq, scepi2-seq, 6-base-cut-and-tag, viral-mimicry, transposable-elements, decitabine, uhrf1, epigenetic-memory, cancer-of-unknown-primary, epigenetic-aging, scbs-seq, allele-specific-methylation); scATAC-seq tools (chromvar, cistopic, snapatac, episcanpy, scabc, micro-atac-seq, scatac-seq, scanpy, anndata, pseudo-bulk, tn5-tagmentation, combinatorial-indexing, icell8-nanowell, latent-dirichlet-allocation, jaccard-similarity, nystrom-method, k-medoids, transcription-factor-motif, de-novo-motif-discovery, cis-regulatory-element, replication-timing, enhancer-states); histone modifications (histone-modifications, chip-seq, cut-and-tag, cut-and-run, chic-seq, sortchic, scchic-seq, scchix-seq, scicut-tag, multi-tag, chromatin-velocity, deephistone, convolutional-neural-network); 3D genome (3d-genome, single-cell-hi-c, topologically-associating-domain, chromatin-compartments, sc-sprite, dip-c, stark, sscce, empty-cells-algorithm); long-read (oxford-nanopore, pacbio, smrt-tag, samosa-tag, samosa, stam-seq, nanopore-adaptive-sampling, highly-repetitive-regions, structural-variants, somagauss-sv, laryngeal-squamous-cell-carcinoma, lung-adenocarcinoma); mosaicism biology (mitochondrial-heteroplasmy, kimura-distribution, mitochondrial-lineage-tracing, focal-cortical-dysplasia, mtor-pathway, autism-spectrum-disorder, alzheimers-disease); variant calling (scout-variant-caller, monovar, sccaller, allele-dropout).
  - ~30 new entity pages: scott-kennedy, lawrence-loeb, ludmil-alexandrov, joseph-gleeson, tim-coorens, lovelace-luquette, alexej-abyzov, peter-park, flora-vaccarino, smaht-network, patrick-chinnery, james-stewart, sara-bizzotto, manolis-kellis, li-huei-tsai, heather-lee, chengqi-yi, xiaoying-fan, joseph-costello, shankar-balasubramanian, biomodal, alexander-van-oudenaarden, chun-xiao-song, dan-xie, stein-aerts, bing-ren, jason-buenrostro, sandy-klemm, wing-hung-wong, keji-zhao, steven-henikoff, jake-yeung, ana-conesa, vijay-ramani, jixian-zhai, hua-jun-wu, jim-hughes, maria-colome-tatche, rui-jiang, jifeng-liu, fuying-dao.
- **Updated existing pages:** [[40-Topics/somatic-mosaicism]], [[40-Topics/dna-methylation]], [[40-Topics/long-read-sequencing]], [[40-Topics/chromatin-architecture]], [[40-Topics/single-cell-multiomics]] (added new sources, concepts, entities, sub-themes). [[20-Entities/christopher-walsh]], [[20-Entities/william-greenleaf]], [[20-Entities/fabian-theis]] (added new paper mentions). [[index]] heavily reorganized with new sections for duplex sequencing, methylation methods, scATAC-seq tooling, histone modifications, 3D genome, and long-read methods.
- **Notable findings / framings**:
  - **The duplex-sequencing field has converged**: six methods in the SMaHT benchmark ([[10-Summaries/zhang-2025-smaht-duplex-benchmark]]) give concordant mutation-rate and signature estimates despite distinct chemistries. The implications: (a) cross-platform meta-analysis is now legitimate within SMaHT-class studies; (b) accuracy is no longer the differentiator — pick the method by input requirement / cost / target footprint.
  - **The single-cell + duplex gap remains**: every duplex method requires intact dsDNA, but scWGA loses strand identity. Closing this is the single biggest open methodological frontier in mosaicism research — flagged in [[40-Topics/duplex-sequencing]] open questions.
  - **Two distinct paradigms for joint methylation + chromatin readout** are crystallizing: (i) bisulfite-replacement chemistries (TAPS, 6-base-seq) that preserve adaptors and combine with CUT&Tag/sortChIC (scEpi²-seq, 6B-C&T); (ii) split-pool combinatorial-indexing methods (SpliCOOL-seq, SIMPLE-seq) that scale to 10⁴–10⁵ cells. These differ in throughput vs per-cell modality count.
  - **MNase-based vs Tn5-based single-cell chromatin** is the next clean comparative axis ([[40-Topics/histone-modifications]]). MNase (sortChIC family) preserves nucleosome positioning; Tn5 (CUT&Tag family) is higher-throughput. scChIX-seq + scEpi²-seq (van Oudenaarden lab) bet on MNase; MulTI-Tag + sciCUT&Tag (Henikoff lab) bet on Tn5.
  - **Long-read epigenomics is a separate field now**: Liu/Conesa 2025 NRG review ([[10-Summaries/liu-2025-long-read-epigenome-review]]) plus Fu/Sedlazeck/Timp 2025 NRG (already ingested) plus the Hong/Dao 2025 sc-3D review define the boundaries. LRS-exclusive territory: HRRs (centromeres, telomeres, rDNAs), allele-specific methylation, multi-modal single-fiber chromatin readouts.
  - **The "viral mimicry decoupling" finding** in scTEM-seq is therapeutically consequential: a subgroup of decitabine-treated AML cells coordinately upregulates TEs, but **methylation loss alone doesn't predict response** — other factors (SETDB1, TF availability) gate viral mimicry. This argues for richer patient stratification than methylation alone.
  - **Smoking × somatic SV burden** in LSCC ([[10-Summaries/liu-2025-nanopore-lscc-svs]]) is a clean quantitative finding that depended on long-read sequencing; short-read methods could not have shown the SV-class burden correlation.
  - **Repeat expansion as cancer driver via spatial proximity** (LSCC paper) is mechanistically interesting and connects [[40-Topics/somatic-mosaicism]] to [[40-Topics/3d-genome]] — most repeat-expansion biology has historically been in inherited neurological disease.
- **Notable cleanup**: the pending-sources output listed the 5mC/5hmC paper twice (a glob quirk with parentheses in filenames). Verified only one unique file exists. Wiki has 31 unique summaries, not 32.
- **Tooling note**: no new tooling work; existing Quartz + Graphify pipelines untouched.
- **Pending in `00-Sources/papers/`**: 122 - 31 = ~91 primary PDFs still unsummarized. Natural future batches: (a) brain mosaicism primary papers (Lodato 2018 Science, Miller 2022 Nature, etc.); (b) methylation-clock primary papers; (c) lineage-tracing primary papers; (d) 3D-genome primary papers (Dip-C, sn-m3C, HiRES); (e) duplex-sequencing protocol papers for the six SMaHT methods individually.
- **Next**: future ingest sessions can continue the primary-paper skim approach. Natural promotion target for `50-Notes/`: "Single-cell duplex sequencing — the open methodological frontier" (would synthesize the gap identified across [[10-Summaries/shao-2025-scDNA-mosaicism-review]], [[10-Summaries/luquette-2025-pta-duplex-mosaicism]], and [[10-Summaries/zhang-2025-smaht-duplex-benchmark]]).

---

## 2026-05-11 — Third ingest: 11 scDNA-seq / multi-omics / chromatin / methylation reviews

- **Discovered:** 133 new papers landed in `00-Sources/papers/` (user ran `download_papers.py` to pull a scDNA literature corpus). At user direction, **scoped this ingest to the 11 review papers** that will scaffold the topic layer for the remaining 122 primary papers to slot into later. Depth strategy: full-depth read of each review; skim approach for future primary-paper batches.
- **Ingested reviews:**
  - [[10-Summaries/shao-2025-scDNA-mosaicism-review]] — Shao/Walsh 2025 keystone scDNA-seq review.
  - [[10-Summaries/gawad-2016-scgenome-review]] — Gawad/Quake 2016 foundational scDNA review.
  - [[10-Summaries/evrony-2021-scDNA-applications-review]] — Evrony 2021 capabilities framework.
  - [[10-Summaries/forsberg-2017-mosaicism-review]] — Forsberg 2017 mosaicism in health/disease.
  - [[10-Summaries/campbell-2015-mosaicism-review]] — Campbell/Lupski 2015 mosaicism transmission genetics.
  - [[10-Summaries/klemm-2019-chromatin-accessibility-review]] — Klemm/Greenleaf 2019 chromatin accessibility.
  - [[10-Summaries/smith-2013-methylation-development]] — Smith/Meissner 2013 DNA methylation in development.
  - [[10-Summaries/fu-2025-longread-methylation]] — Fu/Sedlazeck/Timp 2025 long-read methylation.
  - [[10-Summaries/baysoy-2023-multiomics-landscape]] — Baysoy/Fan/Satija 2023 multi-omics landscape.
  - [[10-Summaries/vandereyken-2023-scmultiomics-review]] — Vandereyken/Voet 2023 single-cell + spatial multi-omics.
  - [[10-Summaries/heumos-2023-best-practices]] — Heumos/Theis 2023 best practices.
- **Created:** 11 summaries + 13 entities + 25 concepts + 5 topics = **54 new wiki pages** beyond the source PDFs.
  - Entities: [[20-Entities/diane-d-shao]], [[20-Entities/christopher-walsh]], [[20-Entities/charles-gawad]], [[20-Entities/stephen-quake]], [[20-Entities/gilad-evrony]], [[20-Entities/lars-forsberg]], [[20-Entities/james-lupski]], [[20-Entities/william-greenleaf]], [[20-Entities/alexander-meissner]], [[20-Entities/fritz-sedlazeck]], [[20-Entities/winston-timp]], [[20-Entities/rong-fan]], [[20-Entities/rahul-satija]], [[20-Entities/thierry-voet]], [[20-Entities/fabian-theis]].
  - Method concepts: [[30-Concepts/scdna-seq]], [[30-Concepts/scwga]], [[30-Concepts/mda]], [[30-Concepts/pta]], [[30-Concepts/malbac]], [[30-Concepts/dop-pcr]], [[30-Concepts/dlp-plus]], [[30-Concepts/meta-cs]], [[30-Concepts/duplex-sequencing]], [[30-Concepts/scdna-capabilities-framework]], [[30-Concepts/atac-seq]], [[30-Concepts/dnase-seq]], [[30-Concepts/bisulfite-sequencing]], [[30-Concepts/long-read-sequencing]], [[30-Concepts/single-cell-multiomics]], [[30-Concepts/gt-seq]], [[30-Concepts/cite-seq]], [[30-Concepts/spatial-multiomics]].
  - Biology concepts: [[30-Concepts/somatic-mosaicism]], [[30-Concepts/post-zygotic-variation]], [[30-Concepts/microchimerism]], [[30-Concepts/developmental-mutation-timing]], [[30-Concepts/gonadal-mosaicism]], [[30-Concepts/lineage-tracing]], [[30-Concepts/clonal-hematopoiesis]], [[30-Concepts/dna-methylation]], [[30-Concepts/cpg-island]], [[30-Concepts/dnmt]], [[30-Concepts/tet-enzymes]].
  - New topics: [[40-Topics/scdna-seq]], [[40-Topics/somatic-mosaicism]], [[40-Topics/whole-genome-amplification]], [[40-Topics/dna-methylation]], [[40-Topics/long-read-sequencing]].
- **Updated existing pages:** [[40-Topics/single-cell-multiomics]], [[40-Topics/chromatin-architecture]], [[40-Topics/hematopoietic-malignancies]] — added new concept and source links; `index.md` heavily reorganized into the now-substantial methods/biology/wiki sections.
- **Tooling**: Quartz server bg task `bscsqurx6` crashed when a Chrome `*.crdownload` partial-download file appeared in `00-Sources/papers/`. Hardened the Quartz `ignorePatterns` in `.quartz/quartz.config.ts` to filter `*.crdownload`, `*.tmp`, `*.part`, `.DS_Store`, `~$*`, `*.py`, `*.sh`, `*.csv` before restarting.
- **Notable findings / framings**:
  - **Two organizing axes of the field** emerge clearly from the reviews: (a) technology-organized (Diane 2025, Charles 2016 — chemistries and tradeoffs); (b) application/capability-organized (Gilad 2021 — fidelity/co-presence/phenotypic-association). Both are useful; the [[scdna-capabilities-framework]] is the better entry point for newcomers choosing a method for their question.
  - **The PTA inflection point**: scWGA technology went from "useful for CNVs, bad for SNVs" (MDA/MALBAC) to "useful for both" (PTA, ~95% coverage with high allelic balance) over ~5 years. This is the methodological backbone of the current scDNA-seq generation, including [[10-Summaries/swanson-2025-daf-seq|scDAF-seq]].
  - **Single-strand DNA damage as a major scWGA failure mode** is more visible now than in 2016: ~70k ssDNA lesions per cell per day means single-strand dropout produces catastrophic false-positive rates without duplex protection ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]). This argues for duplex methods becoming the future direction.
  - **The mosaicism cluster** (Lars 2017 + Ian 2015 + Diane 2025) now connects directly to the **MPN cluster** ([[10-Summaries/nam-2019-got]] + [[10-Summaries/izzo-2024-got-cha]]) via [[clonal-hematopoiesis]] — JAK2V617F CH is the on-ramp to MPN, and GoT–ChA's pre-disease chromatin priming finding fits directly into the Lars 2017 framing of mosaicism as both biology and disease driver.
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
  - Summaries: [[10-Summaries/nam-2019-got]], [[10-Summaries/izzo-2024-got-cha]], [[10-Summaries/swanson-2025-daf-seq]].
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

## 2026-05-21 — Dedup pass on 10-Summaries/

Removed 41 duplicate summary files (40 DOI-based pairs + 1 tavares slug variant). For each pair, the descriptive lastname-year-shortdescriptor slug was kept; when the journal-named twin had richer content, its body was moved into the descriptive slug. Updated 717 wikilinks across 188 files. `10-Summaries/` went from 232 → 191 files. `index.md` cleaned of duplicate entries. No broken wikilinks remain to dropped slugs (verified).

## 2026-05-21 — Lint pass

- Auto-fixed 5 broken-link typos (`dou-2020-monovar`→`mosaicforecast`, `clonal-evolution`→`cancer-clonal-evolution`, `mtDNA-lineage-tracing`→`mitochondrial-lineage-tracing`, etc.).
- Caught one missed dedup pair (`kousi-2022-alzheimer-mosaicism` collapsed into `kousi-2022-ad-mosaicism`); rewired 11 inbound links.
- Unlinked 743 dead `[[...]]` references across 182 wiki files (converted to plain text). Damage to non-wiki files (CLAUDE.md, .quartz docs, .claude rules, templates) reverted.
- Linked 22 orphan summaries from natural topic pages (mosaic-variant-calling, scdna-cancer-applications, somatic-mosaicism, scdna-seq, chromatin-architecture, histone-modifications, single-cell-multiomics, single-cell-atac-seq, 3d-genome, brain-somatic-mosaicism, dna-methylation, whole-genome-amplification). Linked `taejeong-bae` entity from his summaries.
- Final state: 0 broken wikilinks, 0 orphans.
- Reconciled PTA-vs-MDA cost contradiction: `pta.md` "Contested points" updated to reflect v1→v2 cost trajectory (PTA v2 ~$5/cell now cheapest); `scwga.md` cost row now cites Shao 2025 Table 1.
- Open substantive items not auto-fixed (per CLAUDE.md MAINTAIN spec): `scatac-seq.md` is thin relative to peers; `single-molecule-footprinting.md` missing samosa/stam-seq/smrt-tag cross-refs; `got.md` headline (88% genotyping) should acknowledge expression-dependence ceiling that motivated GoT-ChA.

## 2026-05-21 — Lint shelf cleanup

Tackled the three substantive items left from the morning lint pass:
- Expanded `30-Concepts/scatac-seq.md` from 25 → ~70 lines (platforms, quality metrics, contested points, variants, examples, related). Now references 16 summaries including derop-2024 PUMATAC, luo-2024 benchmark, buenrostro-2015, cusanovich-2015, the multimodal family (sci-CAR, SHARE-seq, scNMT-seq, GoT-ChA), and the analysis tool stack (chromVAR, cisTopic, SnapATAC2, ArchR, EpiScanpy).
- `30-Concepts/single-molecule-footprinting.md` now lists the full methylation-stencil family (fiber-seq, samosa, samosa-tag, stam-seq, smrt-tag, targeted-fiberseq) alongside the deamination family (daf-seq, FOODIE), matching the variant lists on fiber-seq.md and daf-seq.md.
- `30-Concepts/got.md` now explicitly acknowledges the expression-and-distance ceiling: 88% CALR genotyping is locus-favorable; low-expression / distal drivers like JAK2 drop to ~7-10% via cDNA, which is what motivated circularization-GoT and then GoT-ChA. Resolves the framing tension with got-cha.md.

State: 0 broken wikilinks, 0 orphans.
