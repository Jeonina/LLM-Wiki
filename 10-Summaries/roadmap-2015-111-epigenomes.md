---
type: summary
title: "Roadmap Epigenomics Consortium 2015 — Integrative analysis of 111 reference human epigenomes"
source: "[[00-Sources/papers/Integrative analysis of 111 reference human epigenomes]]"
source_kind: paper
author: "Anshul Kundaje, Wouter Meuleman, Jason Ernst, Misha Bilenky, Angela Yen, ... Bradley E. Bernstein, Joseph F. Costello, Joseph R. Ecker, Martin Hirst, Alexander Meissner, Aleksandar Milosavljevic, Bing Ren, John A. Stamatoyannopoulos, Ting Wang, Manolis Kellis (corresponding)"
published: 2015-02-18
ingested: 2026-08-10
doi: "10.1038/nature14248"
journal: "Nature"
tags: [Roadmap-Epigenomics, chromatin-states, ChromHMM, reference-epigenome, GWAS-enrichment, imputation, bulk-reference, consortium]
entities: ["[[manolis-kellis]]", "[[bing-ren]]", "[[alexander-meissner]]", "[[joseph-costello]]", "[[joseph-ecker]]", "[[li-huei-tsai]]"]
concepts: ["[[chromatin-accessibility]]", "[[enhancer-states]]", "[[cis-regulatory-element]]", "[[lamina-associated-domains]]", "[[chromatin-compartments]]", "[[bisulfite-sequencing]]", "[[dnase-seq]]", "[[chip-seq]]", "[[pseudo-bulk]]"]
topics: ["[[histone-modifications]]", "[[dna-methylation]]", "[[chromatin-architecture]]"]
---

**Citation:** Roadmap Epigenomics Consortium et al. (2015) — *Integrative analysis of 111 reference human epigenomes* — *Nature* 518, 317–330. [DOI](https://doi.org/10.1038/nature14248)

# Roadmap 2015 — the bulk reference epigenome

> The reference map the epigenome field lacked: 111 primary-tissue and primary-cell epigenomes (plus 16 from ENCODE = 127 total), each with five core histone marks, jointly segmented into a common 15-state chromatin model, and used to show that GWAS variants for a trait concentrate in the enhancer marks of the tissue that trait belongs to.

## Key claims

- Scale: 2,805 genome-wide datasets generated (1,821 histone, 360 accessibility, 277 methylation, 166 RNA-seq); 150.21 billion mapped reads = 3,174-fold genome coverage. The integrative analysis uses 1,936 of them.
- A "reference epigenome" is defined by five core marks: **H3K4me3** (promoter), **H3K4me1** (enhancer), **H3K36me3** (transcribed), **H3K27me3** (Polycomb), **H3K9me3** (heterochromatin). 98 epigenomes add H3K27ac, 62 add H3K9ac, 53 have DNase, 95 have methylation, 56 have RNA-seq.
- A shared **15-state ChromHMM model** (8 active, 7 repressed) covers all 127 epigenomes; an 18-state model where H3K27ac exists separates strong-H3K27ac enhancers (higher accessibility, lower methylation, more TF binding).
- **~5% of each epigenome** carries enhancer/promoter signatures, ~2-fold enriched for conserved non-exonic elements. The **quiescent state covers ~68%** on average.
- Chromatin state captures expression differences that methylation and accessibility miss: TxFlnk/Enh/TssBiv/BivFlnk have similar accessibility but very different expression; Enh and ReprPC share intermediate methylation but differ in accessibility and expression.
- >18,000 **intermediate-methylation regions** (~57% mCpG) are enriched in genes, enhancer states and conserved regions; they persist within purified cell types, so they "probably reflect a stable state of **cell-to-cell variability** within a population of cells of the same type."
- Methylation dynamics are lineage-specific: ES-to-germ-layer differentiation produces ~2,200–4,400 distinct DMRs per lineage; ectodermal DMRs stay hypomethylated in neural progenitors across different hESC lines.
- **Developmental origin beats tissue environment**: keratinocytes, melanocytes and fibroblasts share a skin environment but cluster with their embryonic-origin relatives; keratinocytes share 1,392 DMRs (97% hypomethylated) with surface-ectoderm-derived breast cells.
- Variability: H3K4me1-associated states are the most tissue-specific (90% of instances in ≤5–10 epigenomes); active promoters and transcribed states are constitutive (90% in 60–75 epigenomes).
- At 2 Mb resolution, active-enhancer-rich segments occupy ~40% of the genome, and the two Hi-C compartments each subdivide further by state composition, with matching differences in gene density, CpG-island occupancy, **lamina association** and cytogenetic bands.
- 226 enhancer modules, 82 promoter modules and 129 dyadic modules of coordinated activity; 84 enriched motifs across 101 modules — versus only 10 motifs in 15 epigenomes when the same test is run per-epigenome. **Module-level analysis is what makes motif enrichment work.**
- Imputation: 4,315 imputed genome-wide datasets across 34 marks, of which **3,193 (74%) exist only as imputation**.
- Allelic bias is widespread: 24% of testable genes with exonic variants show allelic transcription in ES/ES-derived lines, and 71%/69% of those also show allelic epigenomic marks at promoters/Hi-C-linked enhancers; up to 11% of testable enhancers show allelic H3K27ac bias in tissues.
- **GWAS**: 58 studies enriched in H3K4me1 peaks of at least one tissue at 2% FDR; enrichments match known disease tissue (immune traits→immune cells, lipids→liver, fasting glucose→pancreatic islets). Late-onset Alzheimer's enriches in **immune** rather than brain enhancers. H3K27ac gives 47 studies, H3K4me3 only 25, DNase only 9, H3K36me3 15, and **H3K27me3/H3K9me3 give zero**.

## Methods / evidence

Uniform reprocessing: reads truncated to 36 bp and re-filtered with a 36-mer mappability track, subsampled to 30M reads per histone dataset (45M for the seven deeply profiled epigenomes, 50M for DNase) to remove depth artifacts; MACS2 peak calling against whole-cell extract; Hotspot for DNase; extensive QC (strand cross-correlation, inter-replicate correlation, cross-center MDS, imputed-vs-observed agreement) with outlier datasets flagged, removed or replaced.

The uniform-depth subsampling is the methodological point worth carrying: **cross-sample epigenomic comparison requires depth normalization or the differences are sequencing artifacts.** This is exactly the problem pseudo-bulk aggregation faces in single-cell epigenomics, where per-cluster cell number varies wildly.

Caveat the paper itself flags: IMR90 — the field's standard somatic reference at the time — is a **strong outlier** (elevated Het, ReprPC, EnhG; depleted Quies). Conclusions in older papers anchored on IMR90 inherit that.

## Surprising or load-bearing bits

- **Why this matters for single-cell work:** Roadmap is the bulk ground truth every single-cell epigenomic method is benchmarked against, and this paper is where its chromatin-state vocabulary (TssA, Enh, EnhBiv, ReprPC, Quies…) comes from. When [[granja-2021-archr|ArchR]] or [[stuart-2021-natmethods|Signac]] annotate a scATAC cluster by "overlap with Roadmap enhancers," this is the reference.
- The intermediate-methylation finding is the sharpest bulk-level argument *for* single-cell methylomics in the corpus: bulk data hits a 57%-methylated region and cannot say whether that is every cell at 57% or a mixture. Roadmap says the mixture reading is the likely one, and cannot go further. [[smallwood-2014-natmethods|scBS-seq]] and successors exist to resolve exactly this.
- Bivalent states (TssBiv, EnhBiv) show **broader methylation distributions in pluripotent cells**, which the authors attribute to cell-to-cell heterogeneity — again a bulk observation that only single-cell measurement can settle. Connects to [[bernstein-2006-bivalent-chromatin]].
- **Repressive marks carry no GWAS signal at all** (0 enriched studies for H3K27me3 and H3K9me3). Disease-variant interpretation is an active-chromatin problem.
- 74% of the released "data" is imputed. Any downstream analysis using Roadmap tracks should check whether the specific track was observed or predicted — a provenance issue rarely stated in papers that use these tracks.
- Chromatin state predicts expression better than accessibility or methylation individually, but the converse fails. This is the empirical basis for treating the epigenome as combinatorial rather than as independent layers — the framing behind [[regulatory-layers-overview]].

## Entities mentioned

- [[manolis-kellis]] — corresponding author, computational integration.
- [[bing-ren]], [[alexander-meissner]], [[joseph-costello]], [[joseph-ecker]] — Reference Epigenome Mapping Centers.
- [[li-huei-tsai]] — co-author; the Alzheimer's/immune-enhancer thread continues in [[miller-2022-nature]].

## Concepts touched

- [[enhancer-states]] — supplies the operational state vocabulary at population scale.
- [[lamina-associated-domains]] — 2 Mb segment clusters correlate with lamina association, linking chromatin state to nuclear position.
- [[pseudo-bulk]] — the depth-normalization discipline here is the precedent for pseudo-bulk comparison in single-cell data.
- [[chromatin-compartments]] — the A/B split is shown to be internally heterogeneous by chromatin-state composition.

## Connections to other sources

- The bulk counterpart to every single-cell chromatin method in this wiki; benchmark reference for [[gur-2025-scatac-vs-bulk]], which asks directly whether scATAC beats bulk ATAC on regulatory-map completeness.
- Cited as the epigenetic annotation resource in [[spielmann-2018-sv-3d-genome]].
- Its per-cell-type methylation dynamics are the population-level version of what [[luo-2018-snmc-seq2]] and [[nichols-2022-scimet-v2]] measure per cell.
- The GWAS-enrichment logic recurs in [[klemm-2019-chromatin-accessibility-review]].

## Open questions

- Intermediate methylation is attributed to cell-to-cell variability but never measured as such here. Which single-cell methylome dataset actually confirms the mixture model at these >18,000 regions? Not answered in this corpus.
- Does the 15-state model transfer to single-cell data at all, or does sparsity require a different state vocabulary? [[danese-2021-episcanpy]] and [[zhang-2024-snapatac2]] use it implicitly without addressing the question.

## Related

- [[bernstein-2006-bivalent-chromatin]] · [[enhancer-states]] · [[histone-modifications]] · [[gur-2025-scatac-vs-bulk]]
