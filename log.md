# Activity log

Append-only. Newest at the top. One entry per session — ingest, query, or maintenance pass.

---

## 2026-05-12 — Fourth ingest: 31 web-clipping primary papers (methylation, ATAC, histone marks, 3D, long-read, duplex)

- **Discovered:** 31 `.md` web clippings in `00-Sources/papers/` (saved from journal websites and bioRxiv). All previously unsummarized. (The pending-sources script initially showed 32 entries due to a glob quirk around a filename containing parentheses; only 31 unique files exist.)
- **Strategy:** skim depth as planned for primary-paper batches (per third ingest log "Next" section). One ~250–400-word summary per clipping; aggressive cross-referencing with concept and entity pages.
- **Ingested clippings:**
  - **Duplex sequencing / mosaicism** (5): [[10-Summaries/detecting-ultralow-frequency-mutations-by-duplex-sequencing]] (Kennedy/Loeb 2014 founding DS), [[10-Summaries/a-universal-duplex-sequencing-approach-for-accurate-detection-of-somatic-mutations]] (UDSeq, Alexandrov 2025), [[10-Summaries/benchmarking-of-duplex-sequencing-approaches-to-reveal-somatic-mutation-landscapes]] (SMaHT six-method benchmark), [[10-Summaries/a-comprehensive-view-of-somatic-mosaicism-by-single-cell-dna-analysis]] (SMaHT 102-nucleus PTA + DS), [[10-Summaries/high-throughput-single-cell-analysis-reveals-progressive-mitochondrial-dna-mosaicism-throughout-life]] (Glynos/Chinnery 2023 single-cell mtDNA drift).
  - **Mosaicism biology** (2): [[10-Summaries/bizzotto-2022-brain-mosaicism]] (Bizzotto/Walsh NRN review), [[10-Summaries/single-cell-mosaicism-analysis-reveals-cell-type-specific-somatic-mutational-burden-in-alzheimer-s-dementia]] (Kousi/Kellis 2022).
  - **Methylation methods** (6): [[10-Summaries/sctem-seq-single-cell-analysis-of-transposable-element-methylation-to-link-global-epigenetic-heterogeneity-with-transcriptional-programs]], [[10-Summaries/simultaneous-single-cell-analysis-of-5mc-and-5hmc-with-simple-seq]], [[10-Summaries/high-throughput-single-cell-dna-methylation-and-chromatin-accessibility-co-profiling-with-splicool-seq]], [[10-Summaries/sequencing-dna-methylation-and-hydroxymethylation-at-co-occurring-chromatin-features]] (6-base-CUT&Tag), [[10-Summaries/single-cell-multi-omic-detection-of-dna-methylation-and-histone-modifications-reconstructs-the-dynamics-of-epigenomic-maintenance]] (scEpi²-seq), [[10-Summaries/dna-methylation-an-epigenetic-mark-of-cellular-memory-experimental-molecular-medicine]] (Kim/Costello memory review).
  - **scATAC-seq tooling** (7): [[10-Summaries/chromvar-inferring-transcription-factor-associated-accessibility-from-single-cell-epigenomic-data]] (chromVAR), [[10-Summaries/cistopic-cis-regulatory-topic-modeling-on-single-cell-atac-seq-data]] (cisTopic), [[10-Summaries/comprehensive-analysis-of-single-cell-atac-seq-data-with-snapatac]] (SnapATAC), [[10-Summaries/episcanpy-integrated-single-cell-epigenomic-analysis]] (EpiScanpy), [[10-Summaries/unsupervised-clustering-and-epigenetic-classification-of-single-cells]] (scABC), [[10-Summaries/high-throughput-chromatin-accessibility-profiling-at-single-cell-resolution]] (µATAC-seq), [[10-Summaries/scatac-seq-generates-more-accurate-and-complete-regulatory-maps-than-bulk-atac-seq]] (scATAC vs bulk).
  - **Histone modifications** (4): [[10-Summaries/single-cell-chromatin-immunocleavage-sequencing-scchic-seq-to-profile-histone-modification]] (scChIC-seq), [[10-Summaries/scchix-seq-infers-dynamic-relationships-between-histone-modifications-in-single-cells]] (scChIX-seq), [[10-Summaries/scalable-single-cell-profiling-of-chromatin-modifications-with-scicut-tag]] (sciCUT&Tag), [[10-Summaries/deephistone-a-deep-learning-approach-to-predicting-histone-modifications]].
  - **3D genome** (2): [[10-Summaries/navigating-the-3d-genome-at-single-cell-resolution-techniques-computation-and-mechanistic-landscapes]] (Hong/Dao 2025 review), [[10-Summaries/harmonizing-single-cell-3d-genome-data-with-stark-and-scnucleome]] (STARK + scNucleome).
  - **Long-read methods** (4): [[10-Summaries/profiling-the-epigenome-using-long-read-sequencing]] (Liu/Conesa 2025 NRG review), [[10-Summaries/direct-transposition-of-native-dna-for-sensitive-multimodal-single-molecule-sequencing]] (SMRT-Tag/SAMOSA-Tag), [[10-Summaries/nanopore-sequencing-unveils-somatic-structural-variations-as-biomarkers-in-laryngeal-squamous-cell-carcinoma-genomes]] (SomaGauss-SV in LSCC), [[10-Summaries/single-molecule-targeted-accessibility-and-methylation-sequencing-of-centromeres-telomeres-and-rdnas-in-arabidopsis]] (STAM-seq plant HRRs).
  - **scWGA variant caller** (1): [[10-Summaries/accurate-single-cell-genotyping-utilizing-information-from-the-local-genome-territory]] (SCOUT).
- **Created (new pages in this ingest, ~110 total):**
  - 31 summary pages.
  - 4 new topic pages: [[40-Topics/duplex-sequencing]], [[40-Topics/single-cell-atac-seq]], [[40-Topics/histone-modifications]], [[40-Topics/3d-genome]].
  - ~70 new concept pages spanning: duplex methods (codec, nanoseq, hidef-seq, umi-molecular-barcoding, mutational-signatures); methylation chemistry (taps, 5hmc, nome-seq, sctem-seq, simple-seq, splicool-seq, scepi2-seq, 6-base-cut-and-tag, viral-mimicry, transposable-elements, decitabine, uhrf1, epigenetic-memory, cancer-of-unknown-primary, epigenetic-aging, scbs-seq, allele-specific-methylation); scATAC-seq tools (chromvar, cistopic, snapatac, episcanpy, scabc, micro-atac-seq, scatac-seq, scanpy, anndata, pseudo-bulk, tn5-tagmentation, combinatorial-indexing, icell8-nanowell, latent-dirichlet-allocation, jaccard-similarity, nystrom-method, k-medoids, transcription-factor-motif, de-novo-motif-discovery, cis-regulatory-element, replication-timing, enhancer-states); histone modifications (histone-modifications, chip-seq, cut-and-tag, cut-and-run, chic-seq, sortchic, scchic-seq, scchix-seq, scicut-tag, multi-tag, chromatin-velocity, deephistone, convolutional-neural-network); 3D genome (3d-genome, single-cell-hi-c, topologically-associating-domain, chromatin-compartments, sc-sprite, dip-c, stark, sscce, empty-cells-algorithm); long-read (oxford-nanopore, pacbio, smrt-tag, samosa-tag, samosa, stam-seq, nanopore-adaptive-sampling, highly-repetitive-regions, structural-variants, somagauss-sv, laryngeal-squamous-cell-carcinoma, lung-adenocarcinoma); mosaicism biology (mitochondrial-heteroplasmy, kimura-distribution, mitochondrial-lineage-tracing, focal-cortical-dysplasia, mtor-pathway, autism-spectrum-disorder, alzheimers-disease); variant calling (scout-variant-caller, monovar, sccaller, allele-dropout).
  - ~30 new entity pages: scott-kennedy, lawrence-loeb, ludmil-alexandrov, joseph-gleeson, tim-coorens, lovelace-luquette, alexej-abyzov, peter-park, flora-vaccarino, smaht-network, patrick-chinnery, james-stewart, sara-bizzotto, manolis-kellis, li-huei-tsai, heather-lee, chengqi-yi, xiaoying-fan, joseph-costello, shankar-balasubramanian, biomodal, alexander-van-oudenaarden, chun-xiao-song, dan-xie, stein-aerts, bing-ren, jason-buenrostro, sandy-klemm, wing-hung-wong, keji-zhao, steven-henikoff, jake-yeung, ana-conesa, vijay-ramani, jixian-zhai, hua-jun-wu, jim-hughes, maria-colome-tatche, rui-jiang, jifeng-liu, fuying-dao.
- **Updated existing pages:** [[40-Topics/somatic-mosaicism]], [[40-Topics/dna-methylation]], [[40-Topics/long-read-sequencing]], [[40-Topics/chromatin-architecture]], [[40-Topics/single-cell-multiomics]] (added new sources, concepts, entities, sub-themes). [[20-Entities/christopher-walsh]], [[20-Entities/william-greenleaf]], [[20-Entities/fabian-theis]] (added new paper mentions). [[index.md]] heavily reorganized with new sections for duplex sequencing, methylation methods, scATAC-seq tooling, histone modifications, 3D genome, and long-read methods.
- **Notable findings / framings**:
  - **The duplex-sequencing field has converged**: six methods in the SMaHT benchmark ([[10-Summaries/benchmarking-of-duplex-sequencing-approaches-to-reveal-somatic-mutation-landscapes]]) give concordant mutation-rate and signature estimates despite distinct chemistries. The implications: (a) cross-platform meta-analysis is now legitimate within SMaHT-class studies; (b) accuracy is no longer the differentiator — pick the method by input requirement / cost / target footprint.
  - **The single-cell + duplex gap remains**: every duplex method requires intact dsDNA, but scWGA loses strand identity. Closing this is the single biggest open methodological frontier in mosaicism research — flagged in [[40-Topics/duplex-sequencing]] open questions.
  - **Two distinct paradigms for joint methylation + chromatin readout** are crystallizing: (i) bisulfite-replacement chemistries (TAPS, 6-base-seq) that preserve adaptors and combine with CUT&Tag/sortChIC (scEpi²-seq, 6B-C&T); (ii) split-pool combinatorial-indexing methods (SpliCOOL-seq, SIMPLE-seq) that scale to 10⁴–10⁵ cells. These differ in throughput vs per-cell modality count.
  - **MNase-based vs Tn5-based single-cell chromatin** is the next clean comparative axis ([[40-Topics/histone-modifications]]). MNase (sortChIC family) preserves nucleosome positioning; Tn5 (CUT&Tag family) is higher-throughput. scChIX-seq + scEpi²-seq (van Oudenaarden lab) bet on MNase; MulTI-Tag + sciCUT&Tag (Henikoff lab) bet on Tn5.
  - **Long-read epigenomics is a separate field now**: Liu/Conesa 2025 NRG review ([[10-Summaries/profiling-the-epigenome-using-long-read-sequencing]]) plus Fu/Sedlazeck/Timp 2025 NRG (already ingested) plus the Hong/Dao 2025 sc-3D review define the boundaries. LRS-exclusive territory: HRRs (centromeres, telomeres, rDNAs), allele-specific methylation, multi-modal single-fiber chromatin readouts.
  - **The "viral mimicry decoupling" finding** in scTEM-seq is therapeutically consequential: a subgroup of decitabine-treated AML cells coordinately upregulates TEs, but **methylation loss alone doesn't predict response** — other factors (SETDB1, TF availability) gate viral mimicry. This argues for richer patient stratification than methylation alone.
  - **Smoking × somatic SV burden** in LSCC ([[10-Summaries/nanopore-sequencing-unveils-somatic-structural-variations-as-biomarkers-in-laryngeal-squamous-cell-carcinoma-genomes]]) is a clean quantitative finding that depended on long-read sequencing; short-read methods could not have shown the SV-class burden correlation.
  - **Repeat expansion as cancer driver via spatial proximity** (LSCC paper) is mechanistically interesting and connects [[40-Topics/somatic-mosaicism]] to [[40-Topics/3d-genome]] — most repeat-expansion biology has historically been in inherited neurological disease.
- **Notable cleanup**: the pending-sources output listed the 5mC/5hmC paper twice (a glob quirk with parentheses in filenames). Verified only one unique file exists. Wiki has 31 unique summaries, not 32.
- **Tooling note**: no new tooling work; existing Quartz + Graphify pipelines untouched.
- **Pending in `00-Sources/papers/`**: 122 - 31 = ~91 primary PDFs still unsummarized. Natural future batches: (a) brain mosaicism primary papers (Lodato 2018 Science, Miller 2022 Nature, etc.); (b) methylation-clock primary papers; (c) lineage-tracing primary papers; (d) 3D-genome primary papers (Dip-C, sn-m3C, HiRES); (e) duplex-sequencing protocol papers for the six SMaHT methods individually.
- **Next**: future ingest sessions can continue the primary-paper skim approach. Natural promotion target for `50-Notes/`: "Single-cell duplex sequencing — the open methodological frontier" (would synthesize the gap identified across [[10-Summaries/diane-2025-naturereviewsgenetics]], [[10-Summaries/a-comprehensive-view-of-somatic-mosaicism-by-single-cell-dna-analysis]], and [[10-Summaries/benchmarking-of-duplex-sequencing-approaches-to-reveal-somatic-mutation-landscapes]]).

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
