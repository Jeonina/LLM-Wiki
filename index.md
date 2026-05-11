---
title: Index
description: Catalog of every page in the wiki. Updated on every ingest and lint pass.
updated: 2026-05-11
---

# Index

This is the navigable catalog of the wiki. The maintainer (Claude) updates it on every ingest. Each entry: `- [[slug]] — one-line description`.

## Summaries

### Methods reviews (scDNA-seq / multi-omics / chromatin / methylation)

- [[10-Summaries/diane-2025-naturereviewsgenetics]] — Shao et al. 2025: keystone scDNA-seq review; current state of the field.
- [[10-Summaries/charles-2016-naturereviewsgenetics]] — Gawad/Quake 2016: foundational scDNA-seq review.
- [[10-Summaries/gilad-2021-annualreviewofgenomicsandhumangenetics]] — Evrony et al. 2021: applications-and-capabilities framework.
- [[10-Summaries/alev-2023-naturereviewsmolecularcellbiology]] — Baysoy/Fan/Satija 2023: multi-omics technological landscape.
- [[10-Summaries/katy-2023-naturereviewsgenetics]] — Vandereyken/Voet 2023: single-cell and spatial multi-omics methods.
- [[10-Summaries/lukas-2023-naturereviewsgenetics]] — Heumos/Theis 2023: best practices for single-cell analysis.
- [[10-Summaries/sandy-2019-naturereviewsgenetics]] — Klemm/Greenleaf 2019: chromatin accessibility canonical review.
- [[10-Summaries/zachary-2013-naturereviewsgenetics]] — Smith/Meissner 2013: DNA methylation in mammalian development.
- [[10-Summaries/yilei-2025-naturereviewsgenetics]] — Fu/Timp/Sedlazeck 2025: computational long-read methylation analysis.

### Mosaicism reviews

- [[10-Summaries/lars-2017-naturereviewsgenetics]] — Forsberg/Dumanski 2017: mosaicism in health and disease.
- [[10-Summaries/ian-2015-trendsingenetics]] — Campbell/Lupski 2015: developmental timing of mutations.

### Primary methods papers

- [[10-Summaries/anna-2019-nature]] — Nam et al. 2019: GoT method paper; CALR-mutated MPN.
- [[10-Summaries/franco-2024-nature]] — Izzo et al. 2024: GoT–ChA method paper; JAK2V617F MPN.
- [[10-Summaries/elliott-2025-naturebiotechnology]] — Swanson et al. 2025: DAF-seq / scDAF-seq.

### Wiki seed

- [[10-Summaries/example-llm-wiki]] — paraphrase of Andrej Karpathy's LLM Wiki proposal.

## Entities

### scDNA-seq, mosaicism, lineage tracing

- [[20-Entities/diane-d-shao]] — Boston Children's; keystone 2025 review first author.
- [[20-Entities/christopher-walsh]] — Walsh lab; human brain mosaicism program.
- [[20-Entities/charles-gawad]] — St Jude; foundational 2016 review first author.
- [[20-Entities/stephen-quake]] — Stanford; microfluidic single-cell genomics pioneer.
- [[20-Entities/gilad-evrony]] — NYU; applications-framework architect.
- [[20-Entities/lars-forsberg]] — Uppsala; mosaicism in health and disease.
- [[20-Entities/james-lupski]] — Baylor; clinical genetics of mosaicism.

### Multi-omics methods

- [[20-Entities/anna-s-nam]] — Weill Cornell; first author of GoT.
- [[20-Entities/franco-izzo]] — first author of GoT–ChA.
- [[20-Entities/dan-a-landau]] — senior author of GoT and GoT–ChA.
- [[20-Entities/landau-lab]] — NYGC/Weill Cornell group.
- [[20-Entities/thierry-voet]] — KU Leuven; G&T-seq co-developer.
- [[20-Entities/rong-fan]] — Yale; multi-omics landscape review.
- [[20-Entities/rahul-satija]] — NYGC; Seurat developer.
- [[20-Entities/fabian-theis]] — Helmholtz Munich; best-practices recommendations.

### Chromatin / single-molecule footprinting

- [[20-Entities/elliott-g-swanson]] — UW; DAF-seq co-first author.
- [[20-Entities/andrew-b-stergachis]] — UW; DAF-seq senior; Fiber-seq developer.
- [[20-Entities/william-greenleaf]] — Stanford; ATAC-seq co-developer.

### Methylation

- [[20-Entities/alexander-meissner]] — Harvard/Broad; methylation development.
- [[20-Entities/fritz-sedlazeck]] — Baylor; long-read methylation.
- [[20-Entities/winston-timp]] — Johns Hopkins; nanopore methylation.

### Other

- [[20-Entities/andrej-karpathy]] — proposed the LLM Wiki pattern.

## Concepts

### scDNA-seq methods

- [[30-Concepts/scdna-seq]] — umbrella for single-cell DNA sequencing.
- [[30-Concepts/scwga]] — single-cell whole-genome amplification.
- [[30-Concepts/mda]] — multiple displacement amplification (Φ29).
- [[30-Concepts/pta]] — primary template amplification; current gold standard.
- [[30-Concepts/malbac]] — hybrid PCR/isothermal scWGA.
- [[30-Concepts/dop-pcr]] — earliest PCR-based scWGA.
- [[30-Concepts/dlp-plus]] — Tn5-based high-throughput scWGA.
- [[30-Concepts/meta-cs]] — Tn5-based single-cell duplex.
- [[30-Concepts/duplex-sequencing]] — strand-paired single-molecule error correction.
- [[30-Concepts/scdna-capabilities-framework]] — Evrony fidelity/co-presence/phenotypic-association framework.

### Multi-omic methods

- [[30-Concepts/got]] — droplet single-cell genotype + transcriptome.
- [[30-Concepts/circularization-got]] — GoT extension for distal loci.
- [[30-Concepts/got-cha]] — droplet single-cell genotype + chromatin accessibility.
- [[30-Concepts/daf-seq]] — single-molecule chromatin + DNA via deaminase footprinting.
- [[30-Concepts/fiber-seq]] — bulk single-molecule chromatin via m6A stenciling.
- [[30-Concepts/single-molecule-footprinting]] — method class.
- [[30-Concepts/dogma-seq]] — chromatin + RNA + protein.
- [[30-Concepts/cite-seq]] — scRNA + surface protein via antibody-derived tags.
- [[30-Concepts/gt-seq]] — physical-separation scDNA + scRNA (G&T-seq).
- [[30-Concepts/single-cell-multiomics]] — umbrella concept.
- [[30-Concepts/spatial-multiomics]] — spatially-resolved multi-omic methods.

### Chromatin

- [[30-Concepts/chromatin-accessibility]] — open vs closed DNA.
- [[30-Concepts/chromatin-actuation]] — per-fiber open+bound state.
- [[30-Concepts/atac-seq]] — Tn5-based accessibility assay.
- [[30-Concepts/dnase-seq]] — original DNase I accessibility assay.

### Methylation

- [[30-Concepts/dna-methylation]] — 5mC and related modifications.
- [[30-Concepts/cpg-island]] — unmethylated promoter features.
- [[30-Concepts/dnmt]] — DNA methyltransferase enzymes.
- [[30-Concepts/tet-enzymes]] — active demethylation pathway.
- [[30-Concepts/bisulfite-sequencing]] — standard short-read methylation assay.
- [[30-Concepts/long-read-sequencing]] — PacBio + ONT direct modification detection.

### Mosaicism / disease biology

- [[30-Concepts/somatic-mosaicism]] — mosaic somatic variation.
- [[30-Concepts/post-zygotic-variation]] — broader umbrella term.
- [[30-Concepts/microchimerism]] — foreign cells in host.
- [[30-Concepts/developmental-mutation-timing]] — timing→tissue-distribution geometry.
- [[30-Concepts/gonadal-mosaicism]] — germline mosaicism; recurrence risk.
- [[30-Concepts/clonal-hematopoiesis]] — mosaic HSC clones in blood.
- [[30-Concepts/lineage-tracing]] — endogenous mutations as lineage barcodes.
- [[30-Concepts/calr-mutation]] — MPN driver mutation.
- [[30-Concepts/jak2-v617f]] — most common MPN driver.
- [[30-Concepts/myeloproliferative-neoplasm]] — disease class.
- [[30-Concepts/unfolded-protein-response]] — CALR-mutation transcriptional output.
- [[30-Concepts/hematopoietic-differentiation]] — HSPC hierarchy.

### Wiki / meta

- [[30-Concepts/llm-wiki]] — LLM-as-maintainer wiki pattern.
- [[30-Concepts/three-layer-architecture]] — sources / wiki / schema.
- [[30-Concepts/compounding-artifact]] — value-compounding knowledge.
- [[30-Concepts/maintenance-asymmetry]] — humans defer cross-references; LLMs don't.
- [[30-Concepts/ingest-workflow]] — per-source procedure.

## Topics

- [[40-Topics/scdna-seq]] — single-cell DNA sequencing (umbrella).
- [[40-Topics/somatic-mosaicism]] — mosaicism biology and disease.
- [[40-Topics/whole-genome-amplification]] — scWGA methods.
- [[40-Topics/dna-methylation]] — methylation biology and measurement.
- [[40-Topics/long-read-sequencing]] — PacBio and ONT enabling platform.
- [[40-Topics/single-cell-multiomics]] — methods measuring ≥2 modalities per cell.
- [[40-Topics/hematopoietic-malignancies]] — MPN and related.
- [[40-Topics/chromatin-architecture]] — single-cell and single-molecule chromatin.
- [[40-Topics/llm-tooling-patterns]] — LLM design patterns.
- [[40-Topics/knowledge-management]] — knowledge capture and refinement.

## Notes

_Empty — promote one once a query or synthesis pulls together ≥3 sources/pages._

Promising synthesis targets:
- **Droplet-scale vs single-molecule scDNA-seq tradeoffs** — could pull together Anna/Franco/Elliott + Diane 2025 + Gilad 2021 + Charles 2016.
- **The PTA inflection point** — comparison of pre-2020 MDA-era applications with current PTA-enabled work.
- **The capabilities-decision-tree** for choosing scDNA-seq method based on application (from [[30-Concepts/scdna-capabilities-framework]]).

## Open questions

_Tensions and gaps surfaced during ingest or lint. Resolve, then move out._

### scDNA-seq methods

- Where does scDAF-seq's per-cell ~99% coverage / ~10-cell throughput win over GoT–ChA's ~38% genotyping / 10⁵-cell throughput? ([[10-Summaries/elliott-2025-naturebiotechnology]] vs [[10-Summaries/franco-2024-nature]])
- Single-cell + single-molecule duplex sequencing at scale — currently META-CS only; cost-effective alternatives?
- Throughput vs depth: DLP+ (>10⁴ cells low coverage) vs PTA (384 cells, ~95% coverage). Right operating point per question?
- Standardization of QC metrics (especially ADO) across scWGA methods — flagged in [[10-Summaries/charles-2016-naturereviewsgenetics]], still partly unresolved.
- Imputation-based multi-omic integration (GoT–ChA + DOGMA via mt-variant bridges) — how well does it generalize beyond MPN? ([[10-Summaries/franco-2024-nature]])
- Why is intra-cell haplotype actuation divergence (~61%) nearly equal to inter-cell divergence (~63%)? ([[10-Summaries/elliott-2025-naturebiotechnology]])

### Mosaicism biology

- Tissue-specific mosaic mutation rates beyond skin/intestine/brain — still uncertain.
- Clinical VAF threshold for actionable mosaicism — empirical, no consensus.
- Whether age-related mosaic accumulation *causes* aging-related disease or is a *biomarker*.
- IRE1-XBP1 as a therapeutic target in CALR-mutant MPN ([[10-Summaries/anna-2019-nature]] hypothesis) — no clinical validation in wiki yet.
- Why is CALR fitness advantage differentiation-dependent in ET but already strong at HSPC level in MF? ([[10-Summaries/anna-2019-nature]])
- Is JAK2V617F cell-intrinsic chromatin priming causal for clonal expansion or downstream? ([[10-Summaries/franco-2024-nature]])
- Pre-implantation genetic screening from single embryo cell — preprint stage; awaiting clinical validation ([[10-Summaries/diane-2025-naturereviewsgenetics]]).

### Methylation / chromatin

- 5hmC: functional mark vs intermediate — unresolved.
- Methylation calling accuracy benchmarking across long-read platforms.
- Single-cell long-read methylation — emerging but not routine.
- Non-CpG methylation (mCpH) functional significance, especially in brain.

### Wiki

- Does flat-file + `index.md` navigation scale? (raised by [[10-Summaries/example-llm-wiki]])
- Practical contradiction-resolution policy beyond flagging. (raised by [[10-Summaries/example-llm-wiki]])
- Schema migration mid-stream. (raised by [[10-Summaries/example-llm-wiki]])
- Measuring whether a wiki is actually compounding vs accumulating. (raised by [[30-Concepts/compounding-artifact]])
