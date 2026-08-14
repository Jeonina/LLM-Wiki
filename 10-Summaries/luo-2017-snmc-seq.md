---
type: summary
title: "Luo et al. 2017 — Single-cell methylomes identify neuronal subtypes and regulatory elements in mammalian cortex (snmC-seq)"
source: "[[00-Sources/papers/Single-cell methylomes identify neuronal subtypes and regulatory elements in mammalian cortex]]"
source_kind: paper
author: "Chongyuan Luo, Christopher L. Keown, Laurie Kurihara, Jingtian Zhou, Yupeng He, Junhao Li, Rosa Castanon, Jacinta Lucero, Joseph R. Nery, Justin P. Sandoval, … Eran A. Mukamel, M. Margarita Behrens, Joseph R. Ecker (corresponding)"
published: 2017-08-11
ingested: 2026-08-13
doi: "10.1126/science.aan3351"
journal: "Science 357:600–604"
tags: [snmC-seq, mCH, non-CG-methylation, neuronal-subtypes, CG-DMR, superenhancer, cross-species-conservation, cortex]
entities: ["[[joseph-ecker]]", "[[chongyuan-luo]]"]
concepts: ["[[bisulfite-sequencing]]", "[[scbs-seq]]", "[[cpg-island]]", "[[cis-regulatory-element]]", "[[enhancer-states]]", "[[cell-type-annotation]]", "[[dimensionality-reduction]]", "[[transcription-factor-motif]]", "[[allele-specific-methylation]]"]
topics: ["[[dna-methylation]]", "[[brain-somatic-mosaicism]]", "[[single-cell-multiomics]]"]
---

**Citation:** Luo et al. (2017) — *Single-cell methylomes identify neuronal subtypes and regulatory elements in mammalian cortex* — *Science* 357, 600–604. [DOI](https://doi.org/10.1126/science.aan3351)

# Luo 2017 — snmC-seq

> The paper that made DNA methylation a **cell-typing modality** rather than a supplementary readout. The trick is **non-CG methylation (mCH)**: because neurons accumulate mCH over large domains during postnatal synaptogenesis, sparse single-cell coverage still estimates mCH accurately in **100-kb bins across >90% of the genome**. 6,000+ single neuronal methylomes → **16 mouse and 21 human** cortical neuron clusters, plus ~500,000 CG-DMRs marking regulatory elements per cell type.

## Key claims

- **mCH in coarse bins defeats sparsity.** Coverage is only 4.7% of the mouse genome and 5.7% of the human genome per cell (1.4M and 1.8M stringently filtered reads), yet 100-kb-bin mCH is accurate for >90% of the genome because mCH is modulated over large domains. Gene-body mCH is anticorrelated with expression and is *more* predictive of expression than mCG or chromatin accessibility.
- **Methylation reads the whole genome, unlike RNA.** The authors' framing: scRNA-seq mainly reports highly expressed transcripts, whereas methylome sequencing assays any region long enough to get coverage — **>97% of the genome** that RNA-seq does not directly assess.
- **Clustering is robust and not batch-driven.** tSNE on 100-kb mCH bins was invariant across a wide range of experimental and analysis parameters; validated by shuffling, downsampling, and density-based clustering; no significant association with batch (FDR > 0.1, χ²). A substantially similar embedding came from **mCG** bins alone, implying snmC-seq works for non-brain tissues lacking high mCH.
- **16 mouse / 21 human neuron clusters**, annotated by mCH depletion at marker genes (*Satb2*, *Gad1*, *Slc6a1*; layer markers *Cux2*, *Rorb*, *Deptor*, *Tle4*; interneuron markers *Pvalb*, *Lhx6*, *Adarb2*), cross-checked against layer-dissected neurons, purified PV⁺/VIP⁺/SST⁺ methylC-seq, and published snRNA-seq annotations.
- **Deep layers are more diverse than superficial layers in both species.** One cluster each for L2/3 and L4; seven mouse and ten human clusters for L5/L6/deep-layer.
- **A methylation-predicted cell type was validated by in situ hybridisation.** Cluster mDL-2 shares 24 marker genes with mL6-2 but is distinguished by 93 others; double ISH for *Sulf1* (shared) and *Tle4* (mL6-2-specific) confirmed a substantial population of L6 neurons expressing *Sulf1* but not *Tle4*. Since *Tle4*⁺ neurons project to thalamus while *Sulf1* marks both corticothalamic and corticocortical projections, mDL-2 likely differs in projection target — a **connectivity prediction from a methylome**.
- **575,524 mouse and 498,432 human CG-DMRs** (mean 263.6 and 282.8 bp, 5.8% and 5.0% of genome), of which **73.2% / 68.6% lie >10 kb from any annotated TSS** — overwhelmingly distal regulatory elements. mPv and mVip DMRs overlap ATAC-seq peaks and putative enhancers of matched purified populations.
- **Large CG-DMRs predict superenhancers**, e.g. at *Bcl11b*/*Ctip2* in deep-layer neurons (corroborated by broad H3K27ac) and *Prox1* in VIP⁺/NDNF⁺ neurons.
- **Inhibitory neuron regulatory elements are more conserved than excitatory ones.** Cross-species mCG correlation at CG-DMRs is significantly higher for inhibitory neurons (P < 0.001, Wilcoxon), partly explained by greater sequence conservation — which extends only within ~1 kb of the DMR centre, not into flanks.
- **Human neuronal diversity is expanded relative to mouse.** Multiple human clusters map to single mouse clusters (mL5-1, mL6-2, VIP, PV, SST), and a candidate human-specific inhibitory population (hPv-2) shows a distinct gene-specific mCH pattern and superenhancer-like mCG signature.
- **Species-specific TF activity shapes fine cell-type distinctions.** The NF1 motif is enriched in CG-DMRs of two human inhibitory clusters (hVip-2, hNdnf) but *depleted* in the homologous mouse clusters — conserved circuits at the tissue level, divergent at the subtype level.
- **Global mCH varies widely by cell type**: 1.3–3.4% in mouse, 2.8–6.6% in human. Layer-dependent mCH differences within PV⁺ and SST⁺ interneurons implicate layer-specific epigenetic regulation of synaptic function.

## Methods / evidence

snmC-seq applied to NeuN-antibody-labelled FACS-sorted single nuclei from 8-week mouse frontal cortex (dissected into superficial/middle/deep layers) and 25-year-old human frontal cortex: 3,377 mouse and 2,784 human methylomes. Orthogonal validation by ISH, comparison to purified-population methylC-seq, ATAC-seq/H3K27ac overlap, and snRNA-seq annotation concordance. Data at GEO GSE97179; code at mukamel-lab/snmcseq and methylpy.

Weight: cluster robustness is tested more thoroughly than in most contemporaneous single-cell papers. The human sample is n = 1 donor, so "human-specific" claims (hPv-2, NF1 enrichment) are single-individual observations.

## Surprising or load-bearing bits

- **mCH is the reason single-cell methylation works at all in brain.** The insight is not "methylation is cell-type specific" — that was known — but that a mark modulated over *megabase-scale domains* is robust to 5% genome coverage where a mark read at single-CpG resolution is not. This is the methylation analogue of the coarse-binning argument in [[zhou-2019-schicluster]] for Hi-C.
- **The mCG-only embedding result quietly generalises the method.** mCH is a neuronal peculiarity; showing that mCG bins also cluster means snmC-seq is not a brain-only assay.
- **Regulatory-element discovery from methylation alone** — half a million DMRs, mostly distal — makes the methylome a *substitute* for ATAC/ChIP in tissues where those are impractical, not just a correlate.
- **The inhibitory > excitatory conservation asymmetry** is a real evolutionary claim from an epigenomic assay, and the sequence-conservation explanation is only partial.
- **This is where [[lee-2019-natmethods|sn-m3C-seq]] and the 3D-genome brain literature get their cell labels.** [[yu-2021-snaphic|SnapHiC]] and [[xiong-2024-scghost|scGHOST]] both annotate prefrontal cortex cells using methylation clusters derived by this method — the labels are "independent of chromatin contacts," which is exactly what makes the 3D results interpretable.

## Entities mentioned

- [[joseph-ecker]] — corresponding author; the single-cell methylome programme.
- [[chongyuan-luo]] — first author; snmC-seq and snmC-seq2.

## Concepts touched

- [[bisulfite-sequencing]] — snmC-seq measures 5mC + 5hmC combined, like all BS methods.
- [[cis-regulatory-element]] — CG-DMRs as the discovery route to distal elements.
- [[cell-type-annotation]] — methylation as a primary typing modality.

## Connections to other sources

- Direct successor from the same lab: [[luo-2018-snmc-seq2]] (throughput and robustness).
- Predecessors in single-cell methylation: [[guo-2013-scrrbs]], [[smallwood-2014-natmethods]] ([[scbs-seq]]); protocols at [[guo-2015-scrrbs-protocol]] and [[clark-2017-scbs-seq-protocol]].
- Throughput alternatives: [[mulqueen-2018-sci-met]] (combinatorial indexing), [[nichols-2022-scimet-v2]], [[zhang-2023-drop-bs]] (droplet).
- Extends into 3D: [[lee-2019-natmethods]] (sn-m3C-seq — same lab, same cells, adds contacts); brain atlas at [[liu-2023-mouse-brain-methylome-3d]].
- Downstream consumers of its cell labels: [[yu-2021-snaphic]], [[xiong-2024-scghost]], [[park-2026-mintsc]].
- DMR-calling methods that supersede tile-averaging: [[kremer-2024-methscan]].
- Bulk reference context: [[roadmap-2015-111-epigenomes]], [[schubeler-2015-methylation-review]].

## Open questions

- **n = 1 human donor.** Whether hPv-2 is a human-specific population or an individual-specific one cannot be resolved here.
- The authors state that anatomical, physiological, and functional characterisation of the methylation-defined populations is still needed — the mDL-2 projection prediction is a hypothesis, not a tracing result.
- Bisulfite conflates 5mC and 5hmC; whether the neuronal mCH signal contains hmCH is not addressed (later resolved by [[chen-2025-sctaps-sccaps-plus]]-type chemistries).

## Related

- [[luo-2018-snmc-seq2]] · [[lee-2019-natmethods]] · [[40-Topics/dna-methylation]] · [[scbs-seq]]
