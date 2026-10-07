---
type: summary
title: "Barski et al. 2007 — High-Resolution Profiling of Histone Methylations in the Human Genome"
source: "[[00-Sources/papers/High-Resolution Profiling of Histone Methylations in the Human Genome]]"
source_kind: paper
author: "Artem Barski, Suresh Cuddapah, Kairong Cui, Tae-Young Roh, Dustin E. Schones, Zhibin Wang, Gang Wei, Iouri Chepelev, Keji Zhao (corresponding)"
published: 2007-05
ingested: 2026-10-07
doi: "10.1016/j.cell.2007.05.009"
journal: "Cell 129(4):823–837"
tags: [ChIP-seq, founding-method, histone-methylation, H3K4me3, H3K27me3, H3K36me3, H3K9me1, H4K20me1, H2BK5me1, H2A.Z, CTCF, Pol-II, bivalent-domains, enhancers, insulators, CD4-T-cells, Solexa, MNase]
entities: ["[[20-Entities/keji-zhao]]"]
concepts: ["[[chip-seq]]", "[[enhancer-states]]", "[[cis-regulatory-element]]", "[[dnase-seq]]", "[[peak-calling]]", "[[structural-variants]]"]
topics: ["[[histone-modifications]]", "[[chromatin-architecture]]"]
---

**Citation:** Barski et al. (2007) — *High-Resolution Profiling of Histone Methylations in the Human Genome* — *Cell* 129(4):823–837. [DOI](https://doi.org/10.1016/j.cell.2007.05.009)

# Barski 2007 — ChIP-seq of 20 histone methylations in human CD4⁺ T cells

> The paper that named **"ChIP-Seq"**: ChIP of MNase-generated native mononucleosomes, one-step adaptor ligation, 17 PCR cycles and direct sequencing on the Solexa 1G Genome Analyzer (>20 million tags of up to 36 bp per run), replacing ChIP-on-chip and the lab's SAGE-based GMAT. Applied to resting human CD4⁺ T cells for **20 histone lysine/arginine methylations, H2A.Z, Pol II and CTCF**, it produced a single-nucleosome-resolution atlas that assigned marks to promoters, gene bodies, enhancers and insulators — including several then-unexpected activation-associated monomethylations (H3K27me1, H3K9me1, H4K20me1, and a newly reported H2BK5me1).

## Key claims

- **Method validity**: replicate H3K4me3 ChIP-Seq experiments were highly correlated; ChIP-Seq reproduced GMAT patterns at much higher resolution and sensitivity (e.g. an H3K4me3 peak ~1.5 kb upstream of *IL2* where GMAT found a single tag; an *IL13* downstream enhancer peak missed by GMAT), attributed to native mononucleosomes and ~10-fold more tags. Tag counts are treated as directly proportional to a nucleosome's modification level.
- **Promoters** (12,726 genes in 12 expression groups of 1,000): H3K4me1/2/3 all elevated around TSSs, increasingly TSS-focused from mono- to trimethylation (peaks at −900/+1000, −500/+700, −300/+100 respectively); H3K4me3 dips at −200 to +50 (nucleosome loss) with phased peaks at +50, +210, +360. 35,961 Pol II islands; 37% of silent promoters had Pol II islands and 59% had H3K4me3 islands (poised or memory of past transcription); ~91% of Pol II islands coincided with H3K4me3 islands.
- **Activation-associated marks**: H3K4me1/2/3, H3K36me3 (3′-biased), and — less expected — H3K27me1, H3K9me1, H4K20me1 and H2BK5me1 (5′-biased in gene bodies) correlated positively with expression; H2A.Z at promoters correlated with activity (unlike yeast).
- **Repression-associated marks**: H3K27me2/3 and, modestly, H3K9me2/3 correlated with silencing; H3K79me3 modestly correlated with silencing in human T cells (contrary to yeast associations), and gene-body H2A.Z modestly with silencing. Sharp H3K9me3 peaks appeared in some active genes (*STAT1*, *STAT4*). H3R2 and H4R3 methylations showed no promoter preference.
- **Insulators**: 20,262 CTCF sites (8,308 intergenic, 6,305 genic, 5,649 within 2 kb of TSSs); CTCF sites demarcated active domains from H3K27me3 domains (e.g. *PPP5C*, *PAK4*, *GNAS* intron 1); CTCF islands were enriched for H3K4me1/2/3, H2A.Z and H3K9me1 (not H3K9me2/3).
- **Enhancers**: known T-cell enhancers (*IFNG* CNS1, CNS2, CNS22; *IL13* acetylation island 1) carried H3K4me1, H3K4me3 and H2A.Z; across 3,507 DNase HS sites excluding CTCF/Pol II sites, all three H3K4 methylation states, H2A.Z and H3K9me1 were enriched — explicitly disputing a contemporaneous claim that enhancers carry H3K4me1 but not H3K4me3.
- **Bivalency in differentiated cells**: 5,736 regions with overlapping H3K4me3 and H3K27me3 islands in resting CD4⁺ T cells; associated promoters had lower expression; zooming in, the two marks occupied essentially non-overlapping subregions.
- **Chromosome bands**: most G-band boundaries coincided with transitions in H3K4/K9/K27 methylation (Q bands: H3K4 depletion with broad H3K9me3; R bands: high H3K4 methylation) — read as evidence that some marks are stable through mitosis. H3K27me3 and H3K9me3 often complementary; H4K20me3 co-localised with H3K9me3 at centromere-proximal and *ZNF* repeat domains.
- **Translocation breakpoints**: 52 of 84 (62%) somatic breakpoints in T-cell cancers co-localised with H3K4me3, versus 26% of 180 breakpoints in non-T-cell cancers.
- **New transcription units**: mark combinations predicted unannotated TSSs (e.g. antisense near *DHX37*, downstream of *PRRG2*, upstream of *C12orf51*), confirmed by RT-PCR; *GNAS* alternative TSS usage inferred from H3K27me3 vs H3K4me3/H2A.Z.

## Methods / evidence

Resting CD4⁺ T cells (2 × 10⁷ per ChIP, ~200 ng DNA); native MNase chromatin for histone marks, formaldehyde-crosslinked sonicated chromatin for Pol II/CTCF; tags mapped with the Solexa pipeline and summarised in 200 bp windows (400 bp for CTCF/Pol II); "islands" = consecutive windows with >1 tag allowing one empty gap, ≥8 tags; expression from GNF SymAtlas; bivalent = overlapping H3K4me3/H3K27me3 islands within 1 kb of TSS.

Weight: a landmark resource with one cell type, one donor population, short reads and a simple window-threshold island caller (no input normalisation or statistical peak model). Correlations are descriptive; several "novel" mark-function associations depend on single antibodies. The CTCF/enhancer and breakpoint analyses are illustrative rather than statistically tested.

## Surprising or load-bearing bits

- **Monomethylation as an elongation signature** — H3K27me1, H3K9me1, H4K20me1 and H2BK5me1 track transcribed regions; the authors hypothesise the responsible enzymes travel with elongating Pol II.
- **The promoter–enhancer distinction is in the gene body, not the element**: both carry H3K4 methylation, H2A.Z and H3K9me1; active promoters add H3K27me1, H3K36me3, H4K20me1, H2BK5me1 downstream.
- **Silent promoters often look poised** (Pol II and H3K4me3 islands at 37% and 59%), and bivalency exists outside ES cells — both ideas later central to cell-state memory arguments (synthesis).

## Concepts touched

- [[chip-seq]] — founding paper: native MNase ChIP + direct short-read sequencing; coined the term.
- [[enhancer-states]] / [[cis-regulatory-element]] — enhancer and insulator chromatin signatures from DNase HS and CTCF sites.
- [[dnase-seq]] — DNase HS sites used as the unbiased enhancer reference.
- [[structural-variants]] — translocation breakpoints enriched in cell-type-specific active chromatin.

## Connections to other sources

- Same senior author's later single-cell histone method: [[ku-2019-scchic-seq]]; and single-cell DHS mapping from the same lab: [[jin-2015-nature]].
- Bivalent chromatin in ES cells, which this extends to differentiated T cells: [[bernstein-2006-bivalent-chromatin]].
- Enhancer chromatin states refined later: [[creyghton-2010-h3k27ac-enhancers]]; consortium-scale successor: [[roadmap-2015-111-epigenomes]].
- Histone–DNA crosstalk context: [[rothbart-2014-histone-dna-language]].
- Peak calling formalised after this window-based approach: [[zhang-2008-macs]]; single-cell descendants profiling the same marks: [[kaya-okur-2019-cut-and-tag]], [[rotem-2015-drop-chip]].

## Open questions

- Several associations (H2BK5me1, H3K79me3 with repression) rest on one antibody each in one cell type; antibody specificity is not independently validated here.
- Whether H3K4me3 at enhancers reflects enhancer biology or unannotated transcription initiation (e.g. eRNA TSSs) is unresolved in this data (synthesis).
- Bivalent "overlap" resolved into adjacent non-overlapping subregions at higher zoom — whether these are truly co-occupied nucleosomes in the same cell cannot be resolved by bulk ChIP (synthesis; later sequential/single-cell assays address this).

## Related

- [[chip-seq]] · [[bernstein-2006-bivalent-chromatin]] · [[20-Entities/keji-zhao]] · [[40-Topics/histone-modifications]]
