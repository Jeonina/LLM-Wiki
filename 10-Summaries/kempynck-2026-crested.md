---
type: summary
title: "Kempynck et al. 2026 — CREsted: modeling genomic and synthetic cell-type-specific enhancers across tissues and species"
source: "[[00-Sources/papers/CREsted_ modeling genomic and synthetic cell-type-specific enhancers across tissues and species]]"
source_quality: full
source_sha256: "328ee9eb46094194c411be7fe1712621c1235e111b9af3ea953aac793e908508"
source_kind: paper
author: "Niklas Kempynck, Seppe De Winter, Casper H. Blaauw, Vasileios Konstantakos, Eren Can Ekşi, Sam Dieltiens, … Stein Aerts (15 authors)"
published: 2026-04-02
ingested: 2026-10-08
doi: "10.1038/s41592-026-03057-2"
journal: "Nature Methods"
tags: [CREsted, enhancer, enhancer-code, sequence-to-function, scATAC-seq, pseudobulk, peak-regression, topic-model, CNN, TF-MoDISco, contribution-scores, enhancer-design, in-silico-evolution, zebrafish, Borzoi, fine-tuning, HyenaDNA, Nucleotide-Transformer, glioblastoma, melanoma, Aerts-lab]
entities: ["[[20-Entities/stein-aerts]]"]
concepts: ["[[sequence-to-function-model]]", "[[scatac-seq]]", "[[cis-regulatory-element]]", "[[enhancer-states]]", "[[transcription-factor-motif]]", "[[pseudo-bulk]]", "[[convolutional-neural-network]]", "[[latent-dirichlet-allocation]]", "[[dna-language-model]]", "[[copy-number-variation]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[40-Topics/single-cell-atac-seq]]", "[[40-Topics/computational-methods]]"]
---

**Citation:** Kempynck et al. (2026) — *CREsted: modeling genomic and synthetic cell-type-specific enhancers across tissues and species* — *Nature Methods*. [DOI](https://doi.org/10.1038/s41592-026-03057-2)

# Kempynck 2026 — CREsted

> CREsted (*cis*-regulatory element sequence training, explanation and design) is a scverse-compatible Python package from the Aerts lab that turns a scATAC-seq atlas into a **multi-class sequence-to-accessibility model** and then uses it to read and write enhancers. It has four modules: preprocessing (pseudobulk peak heights per cell type, or cisTopic topics), training (dilated CNN by default for regression, plain CNN for topic classification, or transfer learning from Enformer/Borzoi), interpretation (integrated gradients, ISM, tfmodisco-lite, pattern clustering, TF matching by scRNA expression) and design (in silico evolution or motif implantation with a new L2-distance cost). The paper's main argument is that **small, purpose-trained models beat large pretrained ones at fine cell-type resolution**: a CREsted CNN matches double-fine-tuned Borzoi on mouse cortex, base Borzoi cannot separate neuron subclasses, and fine-tuned DNA language models (HyenaDNA, Nucleotide Transformer) do worse than either. Designed enhancers were tested in zebrafish embryos.

## Key claims

- **Two-step training and cell-type normalisation.** Train on all consensus peaks, then fine-tune on cell-type-specific peaks (Gini index > mean + 1 s.d.). Training directly on specific peaks is worse. CPM tracks are rescaled with constitutive peaks (high signal, low Gini) to remove bias against cell types with many peaks. The regression loss is cosine similarity across cell types plus log-MSE.
- **Mouse motor cortex (DeepBICCN2).** Trained on 440,993 consensus then 73,326 specific peaks, it reached Spearman 0.79 and Pearson 0.82 on held-out chromosomes, and beat default (6 M parameters) and large (22 M) gReLU models on all and specific peaks (P < 0.001). Sliding-window prediction over the *Chsy3* locus correlated with the observed track at r = 0.75, and a mouse Pvalb model scored the chicken *UACA* locus at r = 0.62. On 171 in vivo-validated cortex enhancers it had precision 0.77 and recall 0.79. Pattern clustering recovered known regulators (TBR1, NFI, RFX3, EGR, SOX10, SPI1, LHX6 and others) and a CAGGTG E-box specific to Sst-Chodl cells; mutating it to CAGCTG shifted a validated enhancer's predicted activity to all MGE interneurons.
- **Human PBMC (DeepPBMC).** Pearson 0.71 on cell-type-specific test peaks. It recovered all experimentally validated TF sites in a *CD79A* and a *TCRα* enhancer and most of the *IFNB1* enhanceosome (missing p50, c-Jun and one of four IRF sites), with 34% more important nucleotides than Borzoi. Predicted TF instances had average precision 0.75 against ChIP-seq, with low recall that improved when restricted to UniBind direct-binding peaks (except GATA3). Gradient contributions recovered motifs better than ISM. Precision and recall beat pycisTarget and pyChromVAR. In silico EBF1 site removal at *Tcf3* tracked accessibility after EBF1 degradation (r = 0.55 control, 0.60 degraded).
- **Cancer MES-like states.** DeepCCL (melanoma, GBM and control cell lines) groups MES-like states across cancer types, with AP-1, TEAD, RUNX, NFI and ATF/CREB shared. A topic model on glioma biopsies (DeepGlioma, 14,275 cells, 24 topics) shows the cell-line MES program is only partly present in tumours: AP-1 and CREB/ATF are shared, TEAD is cell-line-specific, SOX and RFX are biopsy-specific. Comparing contribution scores instead of predictions is argued to reduce copy-number confounding, and contribution correlations were stable across CNV and neutral regions (epiAneufinder calls). An ensemble of ChromBPNet models gave the same grouping with lower performance.
- **Pretrained models.** DeepBICCN2 generally matched double-fine-tuned Borzoi; fine-tuned Borzoi kept slightly better generalisation on consensus peaks. On an external whole-mouse-brain dataset both beat base Borzoi, which struggled to separate GABAergic and glutamatergic subclasses and had much lower average precision on the 171 validated enhancers. Fine-tuning HyenaDNA (small-32k) and Nucleotide Transformer (500M-1000g) gave worse models than fine-tuned Borzoi or CREsted from scratch, despite higher parameter counts in some cases.
- **Zebrafish design (DeepZebrafish).** Trained on a developmental atlas with 639 cell type × timepoint classes; 74% of 54 validated enhancers got high, specific predictions. After 30 rounds of in silico evolution with an L2 target-vector cost, all designed cardiac and somatic muscle enhancers (three tested per target) were specifically active in vivo, cardiac ones at lower efficiency. Only one of three endothelial designs was strong and specific. Dual-specificity designs often worked but with lower efficiency, and magnitude control was poor. Muscle enhancers used MEF, TEAD and E-box; cardiac ones added GATA and NKX.

## Methods / evidence

Datasets: Zemke et al. mouse motor cortex scATAC (ENCODE), De Rop et al. PBMC, melanoma and new OmniATAC-seq on three GBM lines (A172, M059J, LN229, GEO GSE292617), a glioma biopsy scATAC set, Sun et al. zebrafish development atlas. Default input 2,114 bp with peak height from the central 1,000 bp. Chromosome hold-out splits; a ten-split benchmark and a non-peak-augmented model showed little sensitivity. Input size from 132 bp to 4,228 bp had limited effect on recovered motifs. Borzoi transfer used replicate 0 shrunk to 2,048-bp input. In vivo testing: Tol2 reporter plasmids injected into zebrafish eggs, scored at 48 hpf by three researchers for specificity only (not strength). Code, models (including legacy DeepMEL, DeepFlyBrain, mouse liver and chicken brain models) and data are public.

Weight: a software paper with broad demos and real in vivo design validation, but the validation is small (three enhancers per design target, qualitative scoring). Many comparisons are shown in figures or supplementary figures that are images in the clipping; this page reports the numbers stated in the text only.

## Limitations

**Authors' own:**
- Multi-class models can use one class's activator motif as negative evidence for another class, so some motifs get false negative (repressor-like) contributions; the E-box in excitatory neurons is flagged as possible "model leakage".
- Precise control of enhancer strength in design is "nontrivial". Reporter assays scored specificity only, since copy number per cell is not controlled.
- Large gene-expression models are better for multi-CRE, long-range questions; CREsted targets local enhancer codes.
- ChIP-seq recall was low, partly attributed to indirect binding.

**Reviewer notes:**
- The pretrained-model comparison is one dataset (mouse cortex), one Borzoi replicate cut down to 2 kb input, and one size each of HyenaDNA and NT. Borzoi's main advantage, long context, is removed by the 2-kb crop. (synthesis)
- Models are trained on pseudobulked accessibility, so they predict a cell type's enhancer usage, not a single cell's. That fits enhancer design but not cell-to-cell heterogeneity. (synthesis)
- The CNV-robustness argument for contribution scores is useful for scATAC data from aneuploid tumours, but it is shown on one glioma cohort. (synthesis)

## Surprising or load-bearing bits

- **Small beats big at fine resolution.** A few-million-parameter CNN trained on the atlas matched fine-tuned Borzoi and clearly beat base Borzoi and fine-tuned DNA language models for neuron subclasses. This is a direct data point against "just fine-tune a foundation model" for cell-type enhancer codes.
- **Contribution scores as a CNV-robust comparison.** Comparing what the model attends to, rather than raw accessibility, lets cell lines and aneuploid tumours be compared without copy-number artefacts.
- **Cell-line MES programs are not the tumour MES program.** TEAD is a cell-line feature; SOX and RFX appear only in biopsies.
- **Cross-species scoring without data.** A mouse model scored a chicken locus at r = 0.62, which follows from conserved interneuron enhancer codes.

## Entities mentioned

- [[20-Entities/stein-aerts]] — senior author; lab built CREsted and the earlier DeepMEL/DeepFlyBrain models.

## Concepts touched

- [[sequence-to-function-model]] — multi-class scATAC accessibility models, trained from scratch or by transfer from Enformer/Borzoi.
- [[dna-language-model]] — HyenaDNA and Nucleotide Transformer fine-tuned for cell-type accessibility underperformed.
- [[scatac-seq]] / [[pseudo-bulk]] — pseudobulk peak heights with constitutive-peak scaling as training targets.
- [[cis-regulatory-element]] / [[enhancer-states]] — enhancer code reading and synthetic enhancer design.
- [[transcription-factor-motif]] — tfmodisco-lite patterns, ChIP-seq/UniBind validation, comparison with pycisTarget and chromVAR.
- [[latent-dirichlet-allocation]] — cisTopic topics as classification targets for continuous tumour states.
- [[convolutional-neural-network]] — dilated CNN as the default architecture.
- [[copy-number-variation]] — contribution scores stable across CNV regions.

## Connections to other sources

- Transfer learning from [[linder-2025-borzoi]] and [[avsec-2021-enformer]]; compares against an ensemble of [[pampari-2024-chrombpnet]] models.
- gLM baselines: [[nguyen-2023-hyenadna]], [[dallatorre-2025-nucleotide-transformer]].
- Built on Aerts-lab tools: [[bravo-2019-cistopic]] (pycisTopic), [[bravo-2023-scenicplus]] (motif collection, TF matching). PBMC data from [[derop-2024-natbiotech]].
- Motif-enrichment baseline: [[schep-2017-chromvar]]. CNV calls with [[ramakrishnan-2023-epianeufinder]]; glioma topics batch-corrected with [[korsunsky-2019-harmony]]; zebrafish preprocessing with [[zhang-2024-snapatac2]].
- Frozen vs fine-tuned pretrained features: same direction as [[fan-2026-gfetm]], [[hingerl-2025-scooby]] and [[lal-2026-decima]] — base models need adaptation for cell-type resolution. (synthesis)
- Regulatory element design from an expression model: [[lal-2026-decima]] (in silico only). CREsted is the one in this group with in vivo validation. (synthesis)
- Local accessibility model at single-cell level: [[yuan-2022-scbasset]]. (synthesis)

## Open questions

- Would long-context fine-tuning (full 524-kb Borzoi input) change the pretrained-model comparison? (synthesis)
- Can enhancer strength, not only specificity, be designed reliably?
- How do the false-negative contributions from multi-class training affect discovery of real repressors?

## Related

- [[sequence-to-function-model]] · [[cis-regulatory-element]] · [[scatac-seq]] · [[pampari-2024-chrombpnet]] · [[linder-2025-borzoi]] · [[bravo-2023-scenicplus]] · [[40-Topics/sequence-models-and-foundation-models]] · [[40-Topics/single-cell-atac-seq]]
