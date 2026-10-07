---
type: summary
title: "Lareau, Ludwig et al. 2021 — mtscATAC-seq: massively parallel single-cell mtDNA genotyping + chromatin profiling"
aliases: ["Lareau 2021 mtscATAC-seq", "Ludwig 2020 mtscATAC-seq"]
source: "[[00-Sources/papers/Massively parallel single-cell mitochondrial DNA genotyping and chromatin profiling]]"
source_quality: full
source_sha256: "a6f46c5b5e0741e9ebc6bf6095877c8528d43077e0cb6fcddb57470eafa11673"
source_kind: paper
author: "Caleb A. Lareau, Leif S. Ludwig, Christoph Muus, Satyen H. Gohil, Tongtong Zhao, Zachary Chiang, Karin Pelka, Jeffrey M. Verboon, Wendy Luo, Elena Christian, Daniel Rosebrock, Gad Getz, Genevieve M. Boland, Fei Chen, Jason D. Buenrostro, Nir Hacohen, Catherine J. Wu, Martin J. Aryee, Aviv Regev, Vijay G. Sankaran (corresponding)"
published: 2020-08-12
ingested: 2026-05-18
updated: 2026-10-07
doi: "10.1038/s41587-020-0645-6"
journal: "Nature Biotechnology"
tags: [mtDNA, mtscATAC-seq, mgatk, mitochondrial-heteroplasmy, lineage-tracing, scATAC-seq, MERRF, CLL, colorectal-cancer, hematopoiesis, NUMT, Sankaran-lab, Buenrostro-lab]
entities:
  - "[[20-Entities/caleb-lareau]]"
  - "[[20-Entities/leif-ludwig]]"
  - "[[20-Entities/jason-buenrostro]]"
  - "[[20-Entities/aviv-regev]]"
concepts:
  - "[[30-Concepts/mitochondrial-heteroplasmy]]"
  - "[[30-Concepts/mitochondrial-lineage-tracing]]"
  - "[[30-Concepts/scatac-seq]]"
  - "[[30-Concepts/chromatin-accessibility]]"
  - "[[30-Concepts/single-cell-variant-calling]]"
  - "[[30-Concepts/monovar]]"
  - "[[30-Concepts/chromvar]]"
  - "[[30-Concepts/copy-number-variation]]"
  - "[[30-Concepts/hematopoietic-differentiation]]"
  - "[[30-Concepts/lineage-tracing]]"
  - "[[30-Concepts/phylogenetic-inference]]"
topics:
  - "[[40-Topics/single-cell-multiomics]]"
  - "[[40-Topics/somatic-mosaicism]]"
  - "[[40-Topics/single-cell-lineage-tracing]]"
  - "[[40-Topics/clonal-hematopoiesis]]"
  - "[[40-Topics/cancer-clonal-evolution]]"
  - "[[40-Topics/hematopoietic-malignancies]]"
---

**Citation:** Lareau, Ludwig et al. (2021; online 2020) — *Massively parallel single-cell mitochondrial DNA genotyping and chromatin profiling* — *Nature Biotechnology* 39:451–461. [DOI](https://doi.org/10.1038/s41587-020-0645-6) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/32788666/). A Correction was published 31 August 2023 ([10.1038/s41587-023-01942-1](https://doi.org/10.1038/s41587-023-01942-1)); its content is not in the clipped source.

> **Attribution:** first author is Caleb A. Lareau (co-first with Ludwig). Published online 12 Aug 2020, issue April 2021. The slug `ludwig-2020-…` is kept so existing links resolve.

# Lareau, Ludwig et al. 2021 — mtscATAC-seq

> Droplet scATAC-seq works on nuclei, which strips out mitochondria, so only ~1% of reads map to mtDNA, too few for per-cell mutation calling. mtscATAC-seq runs the 10x scATAC-seq workflow on **whole cells**: it fixes them in formaldehyde, lyses them without digitonin or Tween-20, and assigns reads that map to both mtDNA and NUMTs to the mitochondrial genome. Mean mtDNA coverage per cell rises ~20-fold (9.6× to 191.0×) while the chromatin profile stays largely intact. A companion caller, **mgatk**, picks clonal heteroplasmic variants by pooling evidence across thousands of cells (variance–mean ratio plus strand concordance) rather than genotyping each cell alone. The authors use the pair to (i) measure the cell-to-cell spread of a pathogenic MERRF allele and the chromatin features that track it, (ii) find hidden subclones in CLL and colorectal cancer, and (iii) trace clones through hematopoiesis in vitro (where clones show fate bias) and in vivo (where thousands of small clones show no detectable bias).

## Key claims

- **Protocol optimisation (GM11906 + TF1 cell-line mix).** Dropping digitonin and Tween-20 from lysis and wash buffers ("Condition A") raised the median mtDNA fraction per cell from 1.9% to 21.5%. Private homoplasmic variants (43 of them) showed that ~8.7% of barcodes carried the other line's variants at 60–90% heteroplasmy, i.e. mtDNA was leaking between cells. Fixation with 0.1% or 1% formaldehyde cut this cross-contamination ~3× and raised mtDNA fragment complexity by 69%. After doublet removal the empirical contamination rate was **0.19%**, close to short-read error rates. Fixation added no mtDNA mutations. Before doublet removal, 1% formaldehyde gave lower contamination (1.14%) than 0.1% (1.54%), so 1% for 10 min became the standard.
- **NUMT handling.** Low-coverage stretches of mtDNA came from homology with nuclear mitochondrial segments (NUMTs). The authors hard-masked NUMTs in the reference, which sends multi-mapping reads to mtDNA. They estimate only ~1 accessible NUMT fragment per cell (mean 1.4, median 1.0 in public GM12878 data; 22.6 × 0.041 = 0.93 from ENCODE/Roadmap DNase peaks), against ~5,000–10,000 mtDNA fragments per cell. Residual coverage variation correlated with GC content (r = 0.33).
- **Net performance.** Mean mtDNA coverage rose from 9.6× to 191.0× and median mtDNA read fraction from 1.9% to 36.8%. Median chromatin complexity fell modestly (87,569 to 73,864 unique fragments), reads in DNase peaks went from 74.1% to 72.3%, and 93.8% of 77,704 cell-type-specific peaks were recovered.
- **Pathogenic heteroplasmy varies widely between cells.** In 818 GM11906 cells (from a MERRF patient; ≥50× mtDNA coverage, ≥40% reads in peaks), 8344A>G heteroplasmy spanned 0–100% with a median of 38%, against 44% in bulk ATAC. Fluidigm scATAC-seq and in situ genotyping reproduced the distribution. Promoter accessibility scores of 32 genes correlated positively and 94 negatively with heteroplasmy (|ρ| > 0.2; <1% FDR). Loci near *NR2F2*, *TRMT5* and *SENP5*/*NCBP2-AS2* differed between high (>60%, n = 273), intermediate (10–60%, n = 228) and low (<10%, n = 313) bins. Among ChIP-seq-derived TF scores, MEF2A and MEF2C activity was strongly anticorrelated with heteroplasmy.
- **Haplotype-resolved subclones in the MERRF line.** A second variant, 8202T>C (*MT-CO2*, "probably damaging"; bulk 34%), was the one most correlated with 8344A>G. 456 of 818 cells carried both (>5%), and no cell carried 8344A>G alone. Of 5,230 reads covering both sites, 99.6% were all-mutant or all-wild-type. The authors infer at least two subclones, each spanning low to very high 8344A>G heteroplasmy.
- **mgatk.** Existing Bayesian genotypers assume a fixed ploidy and tie confidence to allele frequency, which suits neither variable mtDNA copy number nor low-frequency clonal variants. mgatk keeps variants with strand concordance (Pearson r of per-strand allele counts) ≥ 0.65, VMR ≥ 0.01, and confident detection (≥2 fragments on both strands) in ≥5 cells. The strand filter removes recurrent errors driven by one strand, which the authors attribute to sequencer photobleaching near G stretches. In 855 TF1 cells (expanded from 30 sorted cells), mgatk called 48 variants that separated 12 clones and supported a putative phylogeny. bcftools and FreeBayes lacked sensitivity or produced strand-discordant calls. Monovar failed outright because its likelihood uses a factorial of maximum depth, which overflows at this coverage. GATK's Fisher strand test gave tiny P values for every variant.
- **Benchmark against Smart-seq2 hematopoietic colonies.** Unsupervised mgatk recovered 64 of 76 (84.2%) variants found earlier with a supervised, colony-aware method. The missed variants were rarer (P = 0.00045). One earlier variant, 4214T>C, was nonzero on only one strand, which suggests it was an artifact. Simulations (q = empirical noise) gave high sensitivity, high PPV and low dropout for variants ≥5% heteroplasmy at ≥~50× per-cell coverage.
- **CLL: hidden diversity in a "monoclonal" cancer.** 23,467 cells from two patients (mean 55.5× mtDNA coverage; 11,423 unique nuclear fragments; 70.8% in peaks) yielded 43 mutations and 15 putative subclones in CD19⁺ leukemic cells, including one marked by 12067C>T in 0.4% of leukemic cells. Cells with 14858G>A lacked the dominant BCR clonotype (linked via mtDNA coverage in 5′ scRNA-seq). Every Patient 1 cell carried trisomy 12, inferred from chromatin read depth (8.1% vs 5.3% of autosomal reads on chr12), so the trisomy preceded the mtDNA diversity. Hundreds of peaks associated with subclones, including the *TIAM1* and *ZNF257* promoters. Six mutations that reached homoplasmy in subsets of CD19⁺ cells also appeared in T, NK and myeloid cells, which points to a multipotent progenitor of origin. Nuclear mutations in *LEF1* and *HCST* from exome sequencing corroborated this in Patient 2.
- **Colorectal cancer.** Chromatin-depth CNV calls (gains on chromosomes 6, 7, 8, 9 and 12) plus a homoplasmic 16147C>T marked the dominant malignant population, and further mtDNA variants split subclones within both tumor and immune cells.
- **In vitro hematopoiesis: clones show fate bias.** CD34⁺ cultures started from ~500 or ~800 cells gave 18,259 cells over 20 days (mean 74.8× mtDNA coverage). mgatk called 175 and 305 variants, 96.0% and 94.8% of them transitions. Heteroplasmy fold-changes were wider than homogeneous differentiation predicts (KS P < 2.2 × 10⁻¹⁶). Six MITOMAP-confirmed pathogenic variants (e.g. 12316G>A, 3243A>T) were ≤0.1% in bulk but >30% in some cells. Cells fell into 197 clones. Of 57 clones with ≥10 day-20 cells in the 800-cell culture, 10 were erythroid-biased and 21 monocytic-biased (z > 5). Their day-8 cells already showed more accessible GATA1/KLF1 or SPI1/CEBPA motifs, respectively. The signal weakened when restricted to the early progenitor cluster (n = 257).
- **In vivo hematopoiesis: many small, unbiased clones.** From a 47-year-old healthy donor, 7,474 bone-marrow CD34⁺ HSPCs and 8,591 PBMCs collected 3 months apart gave 351 and 130 variants (52 shared; 429 unique), each <1% in pseudobulk but often near-homoplasmic in single cells. Cells formed 257 clones (median 9 cells per clone in PBMCs, 12 in HSPCs), and 92% of clones held <1% of cells. Clones propagated from HSPCs to blood with fairly stable output. Clone lineage composition was consistent with random subsampling, unlike the in vitro bias. A rare-variant pass (variants in ≤3 HSPCs) found 923 more mutations, none overlapping the 429. Plasmacytoid dendritic cells had low mtDNA copy number.

## Methods / evidence

Wet lab: 10x Chromium scATAC v1 on fixed whole cells (1% formaldehyde, 10 min, glycine quench), NP40 lysis buffer without digitonin or Tween-20, otherwise the standard 10x protocol. Sequencing was matched to estimated nuclear library complexity, aiming for ≥20× deduplicated mtDNA coverage. The authors suggest ~1,000 cells can show subclones in malignancies and ~10,000 cells gave first insights into steady-state hematopoiesis. Alignment: CellRanger-ATAC to NUMT-masked hg19. Clones: Seurat shared-nearest-neighbour clustering on the square-root heteroplasmy matrix with cosine distance, with k and resolution tuned per dataset (e.g. k = 10, resolution 1.0 for TF1 and 3.5 in vivo). TF1 tree by neighbour-joining. Chromatin analyses: LSI/UMAP, chromVAR on 78 LCL ChIP-seq sets, Signac. CNVs from 10-Mb bins (2-Mb step) of fragment counts as z-scores. Orthogonal checks: Fluidigm C1 scATAC, padlock-probe in situ genotyping of 8344A>G, 5′ scRNA-seq with BCR/TCR, and whole-exome sequencing for CLL. Data are at GEO GSE142745. Code: github.com/caleblareau/mgatk and the mtscATACpaper_reproducibility repository.

Weight: the technical validation is strong, using a cell-line mix with private homoplasmic variants as ground truth for contamination, two orthogonal genotyping platforms, and comparisons against several callers. The biology is mostly n = 1 per setting (one MERRF line, two CLL patients, one CRC tumor, one healthy donor, two cultures). The authors frame it as demonstrations needing orthogonal validation across donors. Clone calls depend on per-dataset clustering choices. The reported numbers have small internal inconsistencies: the Smart-seq2 benchmark is 935 cells in Results but 895 in Methods, the silver standard is 78 variants in one sentence and 76 in the next, the simulation noise is written as q = 0.19 although the empirical rate is 0.19%, and the nuclear variant is "*HCST*" in Results but "*HSCT*" in Methods. (synthesis)

## Limitations

**Authors' own:**
- Biological conclusions "may require validation via orthogonal methodology across multiple donors".
- The protocol was optimised on hematopoietic cell suspensions. Other tissues may need further changes, and only one solid tumor (CRC) was tested.
- No general guidance on how many cells to profile: dominant clones are found first, and resolving rare clones needs more cells.
- mtDNA content varies by cell type, so the depth needed to detect low-frequency mutations varies too. Deeper sequencing would improve coverage.
- mgatk is unsuitable for 3′ scRNA-seq, which reads one strand only. The supervised approach used earlier is better powered for low-frequency variants when clone labels are known.
- In vitro fate bias may reflect limited cytokines in culture. The in vivo null result may reflect cell-type longevity or rare clones below detection. Power to find lineage-priming features in early progenitors was limited (n = 257).

**Reviewer notes:**
- The in vivo claim of no clonal output bias rests on one donor, one 3-month interval and clones with ≥10 cells, so it lacks power against modest or rare-clone bias. (synthesis)
- Clones are clusters of variant profiles, not verified lineages. With no ground truth beyond the TF1 and Smart-seq2 colony data, over- or under-splitting at the chosen resolutions is not quantified. (synthesis)
- Residual mtDNA transfer between cells (0.19%) and the low-heteroplasmy floor (~5% at ~50×) set a limit on resolving shallow subclones. Later callers such as MQuad and scMitoMut target exactly this regime. (synthesis)

## Surprising or load-bearing bits

- **Fixation is the trick that matters for clonality, not just yield.** Without it, ~8.7% of barcodes carry another cell's homoplasmic variants at intermediate heteroplasmy, which would look like heteroplasmic clonal markers. Any mtDNA-in-scATAC dataset collected without fixation should be read with this in mind. (synthesis)
- **mgatk calls variants across cells.** Strand concordance plus between-cell variance replaces per-cell genotype likelihoods. This is why it scales with cell number, and also why it fits scRNA-seq poorly, as MQuad later argued.
- **Monovar's failure here differs from the usual "diploid assumption" critique.** It crashed because its likelihood factorial overflows at mtDNA depths, a computational failure rather than only a modelling mismatch.
- **"Monoclonal" CLL has mtDNA subclones and multilineage-shared variants**, consistent with a CLL origin in an early progenitor.
- **In vitro vs in vivo.** Clear fate bias in culture, none detected in steady-state human blood with ~257 clones mostly under 1%. This matches the polyclonal picture from nuclear somatic-mutation phylogenies.
- **Pathogenic mtDNA variants hide in healthy cultures**: ≤0.1% in bulk but >30% in individual cells.

## Entities mentioned

- [[20-Entities/caleb-lareau]] — co-first author; developer of mgatk.
- [[20-Entities/leif-ludwig]] — co-first author; extends his 2019 mtDNA lineage-tracing work.
- [[20-Entities/jason-buenrostro]] — co-author; ATAC-seq and Fluidigm scATAC-seq lineage.
- [[20-Entities/aviv-regev]] — co-senior author.

## Concepts touched

- [[30-Concepts/mitochondrial-heteroplasmy]] — single-cell heteroplasmy spread of a pathogenic allele (8344A>G) and its chromatin correlates.
- [[30-Concepts/mitochondrial-lineage-tracing]] — first droplet-scale method, with contamination quantified and corrected by fixation.
- [[30-Concepts/scatac-seq]] / [[30-Concepts/chromatin-accessibility]] — whole-cell scATAC that keeps chromatin quality.
- [[30-Concepts/single-cell-variant-calling]] — mgatk's cross-cell VMR plus strand-concordance filter.
- [[30-Concepts/monovar]] — fails at mtDNA depths (factorial overflow).
- [[30-Concepts/chromvar]] — TF and ChIP-seq deviation scores linked to heteroplasmy and clone fate.
- [[30-Concepts/copy-number-variation]] — CNVs inferred from scATAC read depth (trisomy 12; CRC gains).
- [[30-Concepts/hematopoietic-differentiation]] / [[30-Concepts/lineage-tracing]] — clone-resolved fate bias in vitro, unbiased output in vivo.
- [[30-Concepts/phylogenetic-inference]] — neighbour-joining tree of TF1 subclones.

## Connections to other sources

- Extends [[ludwig-2019-mtdna-lineage-tracing]] from plate-based Smart-seq2/ATAC to droplet scale, and reanalyses its colony data as a benchmark.
- Successors and alternatives: [[miller-2022-maester]] (mtDNA from 3′ scRNA-seq, where mgatk does not apply), [[kwok-2022-mquad]] (argues mgatk's VMR is unreliable in scRNA-seq), [[sun-2025-scmitomut]] (per-cell beta-binomial calls), [[hsieh-2026-scmtmpm-scwmss]] (mutational-burden metrics on mtscATAC-seq data).
- The in vivo finding of many small, unbiased clones echoes [[lee-six-2018-hsc-dynamics]] (cited as ref. 35). (synthesis)
- Heteroplasmy biology background: [[glynos-2023-mtdna-mosaicism]].
- Built on [[buenrostro-2015-nature]] (Fluidigm scATAC used as orthogonal check). Analysis uses [[schep-2017-chromvar]] and Signac ([[stuart-2021-natmethods]]).
- Contrasts with targeted genotyping in [[nam-2019-got]], which requires known variants. mtscATAC finds variants de novo.
- Benchmarked as one of eight scATAC protocols in [[derop-2024-natbiotech]].

## Open questions

- Does the 2023 Correction change any numbers above? The clipped source does not include it.
- How well does the whole-cell, fixed protocol transfer to solid tissues and to nuclei-only (frozen) samples, where cytoplasmic mtDNA is lost? (synthesis)
- Is the in vivo absence of clonal lineage bias real, or a power limit of one donor and ≥10-cell clones? Larger multi-donor follow-ups would settle it. (synthesis)
- The 923 rare variants confined to ≤3 HSPCs may mark quiescent clones. Can they be told apart from residual noise without a ground truth?

## Related

- [[30-Concepts/mitochondrial-heteroplasmy]] · [[30-Concepts/mitochondrial-lineage-tracing]] · [[30-Concepts/scatac-seq]]
- [[ludwig-2019-mtdna-lineage-tracing]] · [[miller-2022-maester]] · [[kwok-2022-mquad]] · [[glynos-2023-mtdna-mosaicism]]
- [[40-Topics/single-cell-multiomics]] · [[40-Topics/somatic-mosaicism]] · [[40-Topics/single-cell-lineage-tracing]]
