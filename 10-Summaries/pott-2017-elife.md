---
type: summary
title: "Pott 2017 — Simultaneous measurement of chromatin accessibility, DNA methylation, and nucleosome phasing in single cells (scNOMe-seq)"
source: "[[00-Sources/papers/Simultaneous measurement of chromatin accessibility, DNA methylation, and nucleosome phasing in single cells .pdf]]"
source_quality: full
source_sha256: "3fd4657869a9ff6afe4c9b8e73f573d429a7b863aa53ec1b7361f7eb8d05e0d1"
source_kind: paper
author: "Sebastian Pott (sole and corresponding author; University of Chicago)"
published: 2017-06-27
ingested: 2026-05-13
doi: "10.7554/eLife.23203"
journal: "eLife 6:e23203"
aliases: ["scNOMe-seq", "Pott 2017"]
tags: [scNOMe-seq, NOMe-seq, GpC-methyltransferase, M.CviPI, methylation, accessibility, nucleosome-phasing, CTCF-footprint, joint-assay, bisulfite, GM12878, K562]
entities: []
concepts: ["[[nome-seq]]", "[[single-molecule-footprinting]]", "[[chromatin-accessibility]]", "[[bisulfite-sequencing]]", "[[dnase-seq]]", "[[allele-dropout]]", "[[transcription-factor-motif]]", "[[scnmt-seq]]"]
topics: ["[[dna-methylation]]", "[[single-cell-multiomics]]", "[[chromatin-architecture]]"]
created: 2026-05-13
updated: 2026-10-07
---

**Citation:** Pott (2017) — *Simultaneous measurement of chromatin accessibility, DNA methylation, and nucleosome phasing in single cells* — *eLife* 6:e23203. [DOI](https://doi.org/10.7554/eLife.23203) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/28653622/)

# Pott 2017 — scNOMe-seq

> Pott adapts bulk NOMe-seq to single cells. Isolated nuclei are treated with the GpC methyltransferase M.CviPI, which methylates GpC in nucleosome-free DNA; single nuclei are then sorted by FACS, bisulfite-converted and sequenced. Each read reports **accessibility** (GpC methylation) and **endogenous CpG methylation** together, and because DNA is recovered whether or not it was accessible, a covered but unmethylated region is a true closed site rather than lost DNA. The proof of principle uses 12 treated GM12878 and 11 K562 cells: scNOMe-seq recovers DNase hypersensitive site (DHS) accessibility, shows that only about a third of covered DHSs are open in any one cell, detects CTCF footprints at individual motifs, separates the two cell types, and estimates per-cell nucleosome phasing (~187–200 bp).

## Key claims

- **Data scale.** 19 GM12878 cells (including seven untreated controls) and 11 K562 cells; each treated library was sequenced to at least 16 M reads, with 2.5–5 M reads left after deduplication. On average "6,679,864 (2.9%) of all cytosines in GpCs and 1,291,180 (3.6%) of all cytosines in CpGs were covered per cell".
- **DHS coverage per cell.** More than 85% of DHSs contain GpCs and are detectable in principle. Of these, "10.6% (20388/191566) and 17.3% (33182/191598) had one or more GpCs covered", and "5.2% (9083/174896) and 9.5% (16608/174828) were covered at four or more GpCs" in individual GM12878 and K562 cells. Later analyses use DHSs with ≥ 4 covered GpCs ("covered DHSs").
- **Accessibility tracks bulk DNase signal; CpG methylation is the inverse.** GpC methylation at covered DHSs correlated with bulk DNase I peak score, and CpG methylation was lowest at the strongest DHSs. Across DHS loci in GM12878, GpC and CpG methylation were weakly anti-correlated (Pearson r = −0.13). The single-cell correlation with DNase was lower than for bulk NOMe-seq in the same line.
- **Only a minority of DHSs are open in one cell.** About 50% of covered DHSs had < 25% GpC methylation. With a 40% GpC methylation threshold, "32–44% and 26–37% of all covered DHSs were determined to be accessible" in single GM12878 and K562 cells, and "even under the most lenient conditions less than 50%". DHSs with higher bulk DNase signal were accessible in more cells, which the author calls "direct evidence" that bulk DNase I peak height reflects the frequency of accessibility across cells; cell-to-cell variability concentrated at weak DHSs.
- **Promoter and gene-body patterns.** GpC accessibility rose just upstream of the TSS and in promoters (−500 to +150 bp) of highly expressed genes; CpG methylation dipped at the promoter, rose through the gene body, and gene-body methylation was highest in the most highly expressed quartile.
- **Cell-type separation.** Jaccard similarity of accessible DHSs (union set) and correlation of CpG methylation in 10 kb bins both clustered GM12878 and K562 cells by origin, and each cell type showed higher GpC methylation at its own DHSs. The author notes the separation "is confounded with experimental batches".
- **CTCF footprints at single loci.** Averaged and per-cell profiles showed accessibility rising toward CTCF ChIP-seq sites with a protected dip at the motif; EBF1 and PU.1 gave weaker versions. Using a footprint score (motif GpC methylation minus methylation of 50 bp flanks, accessible regions only), "two-thirds of CTCF motif instances within these accessible regions showed no GpC methylation". Footprinted motifs had higher motif scores (p = 5.429e-12, paired t-test). One locus showed the CTCF footprint in all four cells with coverage.
- **Nucleosome phasing per cell.** GpC and CpG methylation oscillated around well-positioned nucleosomes (top 5% of DANPOS calls from ENCODE MNase-seq). Autocorrelation of GpC methylation status at offsets of 3–400 bp gave phases "between 187 bp and 196 bp (mean = 196.7 bp)" in GM12878 and "between 188 bp and 200 bp (mean = 194.2 bp)" in K562, in agreement with bulk MNase-seq. Phasing varied by chromHMM state, shorter in regulatory and transcribed regions than in heterochromatin and repressed regions.

## Methods / evidence

Nuclei from 2–5 × 10^6 cells were isolated with IGEPAL CA-630 and a Dounce homogeniser, then 1 million nuclei were incubated with M.CviPI (NEB) and SAM for 8 min at 37 °C, topped up with enzyme and SAM for another 8 min. Hoechst 33342-stained nuclei were FACS-sorted (G1 DNA content gate) into 96-well plates containing EZ DNA Methylation Direct digestion buffer; lysis, bisulfite conversion (98 °C 8 min, 65 °C 3.5 h) and cleanup used the Zymo kit, and libraries were built with the Zymo Pico Methyl-seq kit (random primers diluted 1:2, 10 first-round cycles). Sequencing: 100 bp paired-end on HiSeq 2500 (K562) and HiSeq 4000 (GM12878). Reads were trimmed (trim_galore), each mate aligned separately with Bismark/bowtie2 in non-directional mode to hg38, deduplicated with samtools, and methylation extracted with bismark_methylation_extractor. GCG cytosines (ambiguous between GpC and CpG) were removed; non-conversion was < 1%, but reads with > 3 unconverted non-CpG/non-GpC cytosines were dropped because unconverted cytosines clustered on whole reads. ENCODE GM12878/K562 DHS, CTCF, EBF1, PU.1 ChIP-seq and MNase-seq tracks were lifted from hg19 to hg38. Phasing used a custom autocorrelation script (NucPhasing.py) and the local maximum between 100 and 300 bp. Data: GEO GSE83882.

Weight: a single-author proof of principle with a small number of cells from two well-characterised cell lines and no orthogonal per-cell ground truth. The bulk-concordance analyses are convincing; the per-cell accessible fraction depends on the 40% threshold and the ≥ 4 GpC rule (the author shows a range); cell-type separation is batch-confounded. There are small internal inconsistencies: the GM12878 phase mean (196.7 bp) lies above the stated range (187–196 bp), Fig. 2c labels 20,380 where the text says 20,388, and the Discussion cites Figure 3a for cell clustering where the clustering is in Figure 4a. (synthesis)

## Limitations

**Authors' own:**
- "Only a small number of nuclei were sequenced for each cell line", so cell-to-cell variation could not be studied in detail.
- GM12878/K562 separation "is confounded with experimental batches".
- scNOMe-seq "does not enrich for accessible chromatin regions and thus requires significantly more sequencing coverage" than scATAC-seq; commercial bisulfite and amplification kits were used, and optimisation could "increase the yield substantially".
- Whether per-cell variation in phasing distance "is of biological or technical nature" remains to be established.
- TF footprinting requires motifs that contain at least one GpC; cell lines were not authenticated or mycoplasma-tested; genotype was ignored when calling methylation.

**Reviewer notes:**
- Per-cell coverage of ~3% of GpCs and ~10–17% of DHSs means per-locus calls are sparse; the CTCF single-locus example rests on four covered cells. (synthesis)
- Per-cell "accessible fraction" assumes uniform M.CviPI activity across nuclei; the author argues against differential enzyme activity from similar genome-wide GpC levels, but no spike-in control measures it directly. (synthesis)
- Bisulfite conversion degrades DNA and cannot distinguish 5mC from 5hmC at CpGs. (synthesis)

## Surprising or load-bearing bits

- **True negatives in single-cell accessibility.** Count-based scATAC/scDNase cannot tell a closed site from a lost fragment; scNOMe-seq can, because a read covering a site reports its closed state. This is the basis for estimating the per-cell open fraction of DHSs.
- **Bulk DHS peak height ≈ frequency of opening across cells.** Fewer than half of covered DHSs are open in any single cell, and stronger bulk DHSs open in more cells.
- **Footprints on one read.** Each 100–200 bp read carries several GpCs, so a single molecule can show a protected TF motif flanked by accessible DNA, the property later exploited by single-molecule footprinting methods. (synthesis)

## Concepts touched

- [[nome-seq]] — first single-cell implementation of GpC MTase NOMe-seq.
- [[chromatin-accessibility]] — per-cell fraction of accessible DHSs; true negatives distinguishable from dropout.
- [[allele-dropout]] — framed explicitly as the problem that independent DNA recovery solves.
- [[bisulfite-sequencing]] — non-directional post-bisulfite library construction from single nuclei.
- [[dnase-seq]] — ENCODE DHSs as the reference set; bulk DNase signal predicts per-cell accessibility frequency.
- [[transcription-factor-motif]] — CTCF, EBF1, PU.1 JASPAR PWMs for footprinting.
- [[single-molecule-footprinting]] — short-read GpC footprints of CTCF on individual molecules.
- [[scnmt-seq]] — the later assay that adds the transcriptome to this readout.

## Connections to other sources

- Extended by [[clark-2018-scnmt-seq]], which adds RNA to the GpC/CpG readout, as the Discussion anticipates by pointing to scM&T-seq (Angermueller et al. 2016).
- Cited alongside the scBS-seq lineage: [[smallwood-2014-natmethods]] and [[farlik-2015-scwgbs]].
- Count-based single-cell accessibility comparators: [[cusanovich-2015-sciatac]] and [[buenrostro-2015-nature]].
- Later accessibility + methylation methods: [[nichols-2025-scimetv3]]; reviewed in [[ludwig-2019-sc-chromatin-modifications-review]] and [[vandereyken-2023-scmultiomics-review]].
- Single-molecule footprinting successors with other chemistries: [[andrewb-2020-science]] (m6A Fiber-seq), [[doughty-2024-smf-tf]] (bulk M.CviPI SMF), [[he-2024-foodie]] (deaminase). (synthesis)

## Open questions

- Is the per-cell variation in nucleosome phasing biological or technical?
- How does the per-cell accessible fraction of DHSs (~30–40%) compare with estimates from deaminase or m6A single-cell footprinting, which have far higher coverage? (synthesis)
- Does cell-type separation hold without batch confounding, in true heterogeneous tissue such as brain or primary tumours, which the author names as targets?

## Related

- [[nome-seq]] · [[single-molecule-footprinting]] · [[clark-2018-scnmt-seq]] · [[andrewb-2020-science]] · [[he-2024-foodie]] · [[40-Topics/dna-methylation]] · [[40-Topics/single-cell-multiomics]]
