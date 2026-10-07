---
type: summary
title: "Lee et al. 2025 — Spatial joint profiling of DNA methylome and transcriptome in tissues"
aliases: ["Lee 2025 spatial methylome", "Cardilla 2025", "spatial-DMT"]
source: "[[00-Sources/papers/Spatial joint profiling of DNA methylome and transcriptome in tissues]]"
source_quality: full
source_sha256: "65780a7c4bf0a5693beb4196a7f36684fb262fe25942fdd528e286493496a647"
source_kind: paper
author: "Chin Nien Lee, Hongxiang Fu, Angelysia Cardilla, Wanding Zhou, Yanxiang Deng (corresponding)"
published: 2025-09-03
ingested: 2026-05-18
updated: 2026-10-07
doi: "10.1038/s41586-025-09478-x"
journal: "Nature"
tags: [spatial-DMT, spatial-omics, methylation, transcriptome, near-single-cell, EM-seq, DBiT, microfluidic-barcoding, non-CpG-methylation, PMD, mitotic-history, embryogenesis, brain, Deng-lab, Zhou-lab]
entities: []
concepts:
  - "[[30-Concepts/spatial-multiomics]]"
  - "[[30-Concepts/em-seq]]"
  - "[[30-Concepts/non-cg-methylation]]"
  - "[[30-Concepts/tn5-tagmentation]]"
  - "[[30-Concepts/5hmc]]"
  - "[[30-Concepts/transcription-factor-motif]]"
  - "[[30-Concepts/multimodal-integration-methods]]"
  - "[[30-Concepts/trajectory-inference]]"
  - "[[30-Concepts/cell-type-annotation]]"
topics:
  - "[[40-Topics/dna-methylation]]"
  - "[[40-Topics/single-cell-multiomics]]"
---

**Citation:** Lee et al. (2025) — *Spatial joint profiling of DNA methylome and transcriptome in tissues* — *Nature*. [DOI](https://doi.org/10.1038/s41586-025-09478-x)

> **Attribution corrected 2026-10-07:** first author is Chin Nien Lee (Crossref and the source clipping agree); Cardilla is third author. Senior authors are Wanding Zhou and Yanxiang Deng (corresponding), both at the University of Pennsylvania. The slug `cardilla-2025-…` is kept so existing links resolve.

# Lee et al. 2025 — spatial-DMT

> **Spatial-DMT** reads whole-genome DNA methylation and the polyadenylated transcriptome from the **same fixed-frozen tissue section** on a 50 × 50 microfluidic barcode grid (2,500 pixels; 10, 20 or 50 μm). It combines DBiT-style deterministic in situ barcoding with Tn5 tagmentation after HCl histone stripping, biotin-dT in situ reverse transcription, streptavidin separation of cDNA from gDNA, and **EM-seq** enzymatic conversion with splint ligation for the DNA library. In E11 and E13 mouse embryos and P21 mouse brain it yields 136,639–281,447 CpGs and 1,890–4,626 genes per pixel. Methylation clusters (from MethSCAn VMRs) and RNA clusters capture different aspects of identity, and WNN integration resolves more structure than either alone. The biology shown (methylation–expression coupling of both signs, E11→E13 demethylation of upregulated genes, mCG vs mCA gene-specific regulation in the hippocampus, PMD-based mitotic-history maps) is all correlative and demonstration-scale.

## Key claims

- **Chemistry.** Fixed sections are permeabilised, treated with 0.1 N HCl to remove histones, and tagmented twice (two 60-min rounds) with Tn5 carrying a universal ligation linker, a multi-tagmentation strategy adopted from slide-DNA-seq. mRNA is captured in situ by a poly-biotinylated dT primer with UMIs. Barcodes A1–A50 and B1–B50 flow through perpendicular channels and are ligated to both gDNA fragments and cDNA, defining 2,500 pixels. After reverse crosslinking, streptavidin beads pull cDNA away from the gDNA supernatant. cDNA goes through template switching and Nextera XT. gDNA goes through EM-seq (TET2 oxidation + APOBEC deamination), splint ligation of an SLP5 adapter with ten random H nucleotides, and PCR with uracil-tolerant VeraSeq Ultra and a C→T-modified P7 primer (N70X-HT). Barcodes were designed so that no crosstalk is possible after C-to-T deamination. EM-seq was chosen over bisulfite to minimise DNA damage.
- **Reproducibility.** Replicate E11 embryo maps with matched body parts correlated at Pearson r = 0.9836 (DNA methylation) and r = 0.9752 (RNA), and co-embedded by body part. Marker genes (*Frem1* face, *Ank3* brain, *Trim55* heart) showed the expected spatial patterns.
- **DNA data quality.** 2.8–3.9 billion raw reads per sample; after knee-plot pixel filtering and QC, 32.2–65.7% of reads (887,671,712–1,882,630,968) were retained, giving 355,069–753,052 reads per pixel across 1,699–2,493 pixels. Mean CpGs covered per pixel: 136,639–281,447, which the authors call comparable to published single-cell methylome studies. Duplication rates were ~20–53%. Mitochondrial retention was below 1%; linker-sequence conversion exceeded 99%; no poly(A), poly(T) or TSO contamination was found in DNA libraries. CpG retention was 70–80%; mCA was < 1% in embryos and ≈ 3–4% in the P21 brain, matching known postnatal neuronal non-CpG methylation. CpG coverage was uniform across genomic features, and methylation by chromatin state matched reference datasets.
- **RNA data quality.** 23,822–28,695 genes detected per map; mean genes per pixel from 1,890 (E11, 10 μm; 3,596 UMIs) to 4,626 (E11, 50 μm; 16,709 UMIs), comparable to earlier spatial transcriptomic studies. Larger pixels capture more UMIs because they contain more cells.
- **The two modalities define identity independently and complementarily.** In the E11 embryo, VMR-methylation clusters and RNA clusters were each anatomically coherent; WNN integration matched histology (craniofacial W0, hindbrain–spinal cord W2, heart W6). Modality weights showed some clusters driven mainly by expression (W6, heart) and others by methylation (W11, craniofacial). RNA had the broader dynamic range.
- **Methylation–expression coupling has both signs.** Cluster-specific expression often coincided with low methylation at neighbouring VMRs (*Runx2* craniofacial, *Mapt* brain/spinal cord, *Trim55* heart). But *Ank3*, *Atp11c*, *Cyfip2*, *Lmln* and *Khdrbs2* showed expression positively correlated with VMR methylation; *Ank3* was both highly expressed and highly methylated in brain.
- **TF motifs in hypomethylated VMRs match expressed TFs.** Heart (W6) hypomethylated VMRs were enriched for *Hand2*, *Tbx20* and *Meis1* motifs, and those TFs were expressed there; brain/spinal cord showed *Ebf1* and *Pbx1*; craniofacial *Sox9*, *Ebf1* and *Zeb2*. *Ebf1* was expressed and motif-enriched in all three regions; the authors note EBF1 has been reported as a TET2 partner.
- **10 μm near-single-cell map.** A 10 μm map of E11 face and forebrain, integrated with a scRNA-seq time-lapse reference (Qiu 2024), resolved pallial ventricular-zone telencephalon progenitors (W11) and GABAergic cortical interneurons in the mantle zone (W7), plus olfactory sensory neurons (W5) next to the forebrain and olfactory epithelium (W10).
- **Temporal dynamics (E11 vs E13).** Pseudotime on pixels traced oligodendrocyte progenitor migration from subpallium to pallium; loss of methylation accompanied both activation (*Nrg3*) and silencing (*Pdgfra*). E13 RNA co-clustered with a published spatial ATAC–RNA E13 reference into 11 matching populations. Genes upregulated at E13 showed notable methylation loss, e.g. *Usp9x*, *Ank3*, *Shank2* (brain) and *Ctnna1*, *Pecam1*, *Lamb1* (heart). Methylation writers, readers and erasers (*Dnmt1*, *Dnmt3a*, *Mecp2*, *Tet1*) were more highly expressed at E13.
- **mCG vs mCA in the P21 brain.** Global mCA and mCG were lower in DG, CA1/2 and CA3 than cortex. *Prox1* (DG) and *Bcl11b* expression associated with both mCG and mCA; *Ntrk3* (CA1/2, DG) and *Satb1* (cortex) correlated with mCG but not mCA. *Cux1* silencing correlated with both CA and CG hypermethylation in CA3, but only with CA hypermethylation in CA1/2. Across both contexts, negative correlations outnumbered positive ones. Integration with Zeisel 2018 scRNA-seq placed cortical excitatory types in the expected layers (TEGLU7/8/4/3 → layers 2/3, 4, 5, 6), hippocampal types in CA1/2 and CA3, DGGRC2 in DG and DEGLU1 in thalamus; cluster-aggregated methylation correlated with single-cell methylome profiles (Liu 2021 atlas).
- **Regional and mitotic-history features.** Ventricular vs mantle zone of the hindbrain–spinal cord differed in methylation at neural-progenitor promoters and enhancers (H3K4me1-marked; mEnhA9 enhancers) with FOXO4, NEUROG2 and HOXC9 sites. Pixels in one WNN cluster (W7) differed by location: forebrain hypomethylation enriched for FOXI1 sites, spinal-cord hypomethylation for TLX1. **PMD methylation**, which erodes with successive divisions, was higher in forebrain and hindbrain–spinal cord and lower in the embryonic heart, with gradients from heart centre to periphery and from mantle to ventricular zone. In P21 brain, cortex had higher PMD methylation than the DG, consistent with ongoing neurogenesis in the subgranular zone.
- **Methylation splits RNA-identical cells.** Within RNA cluster R3, methylation clusters D0 and D4 differed at low-methylation sites enriched for facial and cardiac morphogenesis motifs, with limited expression differences, which the authors read as epigenetically primed subpopulations.

## Methods / evidence

Tissues: commercial Zyagen C57 E11 and E13 sagittal frozen sections (7–10 μm) and P21 C57BL/6 coronal brain cryosections (8–10 μm). Fixation in 1% formaldehyde; PDMS microfluidic chips (20 or 50 μm channels) made by SU-8 photolithography; sequencing on NovaSeq 6000 and NovaSeq X Plus, 150 bp paired-end. RNA: barcodes and UMIs from Read 2, STARsolo v2.7.10b to mm10, Seurat v5.1.0 SCTransform, 30 PCs, Leiden clustering. DNA: BISCUIT v0.3.14 to mm10; methylation as continuous 0–1 values per CG/CH site; MethSCAn VMRs (top 2% variance) with min-sites set from the knee plot; iterative-PCA imputation of VMR residuals; first 10 PCs for clustering. Integration: Seurat WNN (FindMultiModalNeighbors); E11–E13 RNA by SCT integration (3,000 features), methylation by CCA on common VMRs; Wilcoxon signed-rank tests between stages. Motifs: MethSCAn diff then HOMER findMotifsGenome (motif lengths 5–12). CpG enrichment: knowYourCG with fold enrichment (observed/expected) to avoid inflated odds ratios. VMR–gene correlation: Pearson with Benjamini–Hochberg; GO by clusterProfiler. Data: GEO GSE270498; code github.com/zhou-lab/Spatial-DMT-2024 and Zenodo.

Weight: a technology paper with strong QC (replicate correlations, conversion and contamination controls, coverage comparisons against sciMETv2 and other single-cell datasets, concordance with scRNA-seq, spatial ATAC–RNA and Allen ISH references). The biological claims rest on one or two sections per condition and are correlative, as the authors say. The 50 μm and 20 μm pixels contain several cells, so only the 10 μm map approaches single-cell resolution. In the clipped source the footnote list is misaligned with the in-text citation numbers from about ref. 45 onward (e.g. the PMD reference appears as ref. 45 in the list but is cited as [^50] in the text), so individual citations should be checked against the published article. (synthesis)

## Limitations

**Authors' own:**
- Methylation–expression associations are correlative.
- The enzymatic conversion does not distinguish 5mC from 5hmC; methods measuring the full set of cytosine modifications could fix this.
- Lower-resolution pixels need better spatial deconvolution to resolve mixed signals and limit bias.
- The protocol is for fixed-frozen tissue; FFPE adaptation, better tagmentation and better processing pipelines are future work. Broader tissues, stages and species are needed to show generalisability.
- Two tagmentation rounds were a compromise between DNA yield, experimental time and RNA degradation risk.

**Reviewer notes:**
- About a third to two thirds of DNA reads are discarded after QC, and 2.8–3.9 billion raw reads per section make the "cost-effective" claim in the Discussion hard to judge without a cost comparison. (synthesis)
- Pixel-level methylation is still sparse (≈ 0.14–0.28 M CpGs per pixel), so most analyses depend on VMR aggregation and imputation; cluster-level results are more robust than single-pixel ones. (synthesis)
- No genetic or perturbation test links any of the methylation changes (e.g. at positively correlated genes such as *Ank3*) to expression, and 5hmC, which is abundant in brain, is folded into the "methylation" signal. (synthesis)

## Surprising or load-bearing bits

- **Methylation adds identity that RNA misses.** Some WNN clusters are weighted mainly by methylation, and two methylation clusters within one RNA cluster differ at morphogenesis-motif sites with little expression change.
- **Positive methylation–expression coupling is common enough to report**, both across space (*Ank3*, *Atp11c*, *Cyfip2*, *Lmln*, *Khdrbs2*) and in time (*Nrg3* activation with methylation loss vs *Pdgfra* silencing with methylation loss).
- **PMD methylation as a spatial proliferation map.** The same data that give cell identity also give a mitotic-history read-out, without any extra assay.
- **mCG and mCA act gene-specifically and region-specifically**, e.g. *Cux1* tracks both marks in CA3 but only mCA in CA1/2.
- **Barcode design under deamination.** Because EM-seq converts unmethylated C in the barcodes too, the barcodes and P7 primer were redesigned so the spatial code survives C→T conversion. (synthesis)

## Concepts touched

- [[spatial-multiomics]] — first spatial assay for whole-genome DNA methylation, paired with the transcriptome.
- [[em-seq]] — enzymatic conversion applied to the spatially barcoded gDNA to limit DNA damage.
- [[non-cg-methylation]] — mCA ≈ 3–4% in P21 brain vs < 1% in embryo; mCG vs mCA gene-specific associations.
- [[tn5-tagmentation]] — HCl histone removal plus two rounds of tagmentation to fragment gDNA in tissue.
- [[5hmc]] — not separated from 5mC by the method.
- [[transcription-factor-motif]] — HOMER motif enrichment in hypomethylated VMRs.
- [[multimodal-integration-methods]] — WNN integration of VMR and RNA modalities.
- [[trajectory-inference]] — pixel pseudotime of oligodendrogenesis.
- [[cell-type-annotation]] — integration and deconvolution against scRNA-seq references.

## Connections to other sources

- Analysis stack: [[kremer-2024-methscan]] (VMRs), [[hao-2021-seurat-wnn]] (WNN), [[hao-2024-seurat-v5]] (Seurat v5).
- Conversion chemistry: [[vaisvila-2021-em-seq]]; bisulfite-based single-cell predecessors [[guo-2013-scrrbs]], [[smallwood-2014-natmethods]], [[luo-2017-snmc-seq]].
- QC comparator and splint-ligation lineage: [[nichols-2022-scimet-v2]].
- Multi-tagmentation strategy from slide-DNA-seq: [[zhao-2022-nature]].
- Single-cell methylome + transcriptome co-assays without space: [[clark-2018-scnmt-seq]], [[bai-2024-simple-seq]].
- Brain methylome atlas context: [[liu-2023-mouse-brain-methylome-3d]] (the paper itself compares against the earlier Liu 2021 atlas). (synthesis)
- Cited as the spatial answer to calls for in situ methylation profiling in [[zhu-2020-multimodal-power-of-many]] and [[vandereyken-2023-scmultiomics-review]]; spatial-assay context in [[debnath-2026-ison]].

## Open questions

- How many cells does a 10 μm pixel actually hold, and how much of the forebrain/olfactory resolution survives at single-pixel rather than cluster level? (synthesis)
- Would separating 5mC from 5hmC change the positive-correlation genes in brain? (synthesis)
- Can spatial-DMT run on FFPE tumour sections, which would make spatial methylation classifiers possible? The authors list FFPE adaptation as future work.

## Related

- [[40-Topics/dna-methylation]] · [[30-Concepts/spatial-multiomics]] · [[40-Topics/single-cell-multiomics]] · [[30-Concepts/bisulfite-sequencing]] · [[30-Concepts/em-seq]]
- [[10-Summaries/guo-2013-scrrbs]] · [[10-Summaries/smallwood-2014-natmethods]] · [[10-Summaries/bai-2024-simple-seq]] · [[10-Summaries/clark-2018-scnmt-seq]] · [[10-Summaries/zhao-2022-nature]]
