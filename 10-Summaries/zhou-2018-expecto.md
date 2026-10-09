---
type: summary
title: "Zhou et al. 2018 — Deep learning sequence-based ab initio prediction of variant effects on expression and disease risk"
source: "[[00-Sources/papers/Deep learning sequence-based ab initio prediction of variant effects on expression and disease risk]]"
source_quality: full
source_sha256: "eca4fe5d8066d0991c6696d07411a1b1ae5c8b2ef76e790ea75e8deb578cb758"
source_kind: paper
author: "Jian Zhou, Chandra L. Theesfeld, Kevin Yao, Kathleen M. Chen, Aaron K. Wong, Olga G. Troyanskaya (corresponding)"
published: 2018-07-16
ingested: 2026-10-08
doi: "10.1038/s41588-018-0160-6"
journal: "Nature Genetics"
tags: [ExPecto, DeepSEA, sequence-to-function, gene-expression-prediction, variant-effect-prediction, eQTL, GTEx, GWAS, MPRA, luciferase, in-silico-mutagenesis, variation-potential, evolutionary-constraint, HGMD, TERT]
entities: []
concepts: ["[[sequence-to-function-model]]", "[[variant-effect-prediction]]", "[[convolutional-neural-network]]", "[[transcription-factor-motif]]", "[[chip-seq]]", "[[cis-regulatory-element]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[computational-methods]]"]
---

**Citation:** Zhou et al. (2018) — *Deep learning sequence-based ab initio prediction of variant effects on expression and disease risk* — *Nature Genetics*. [DOI](https://doi.org/10.1038/s41588-018-0160-6)

# Zhou 2018 — ExPecto

> ExPecto predicts tissue-specific gene expression from the 40 kb of sequence around each gene's TSS, without ever training on variant data. It has three stages: an upgraded DeepSEA-style CNN (2,000 bp input, twice the convolution layers) predicts 2,002 TF, histone and DNase profiles in 200 bp steps across ±20 kb; ten fixed exponential decay functions, split upstream and downstream, compress these 400,400 features to 20,020; and one L2-regularised linear model per tissue maps them to log RPKM in 218 tissues and cell types. On held-out chromosome 8 it reaches median Spearman 0.819. Variant effects are the predicted log fold change between alleles. The authors use this to prioritise GWAS variants (validated by luciferase for four immune diseases), compute effects for >140 million promoter-proximal mutations, and derive a per-gene "variation potential" that they interpret as the direction of evolutionary constraint and use to predict which allele is the disease risk allele.

## Key claims

- **Expression from sequence.** Median Spearman 0.819 between predicted and observed log RPKM across 218 tissues on chromosome 8 (990 genes), unchanged (0.821) after removing 184 genes with paralogs elsewhere. Tissue specificity is recovered: predictions match the same or similar tissues best.
- **Models pick relevant features unprompted.** Expression models weight TF and histone features over DNase features (P = 6.9 × 10⁻²⁵). The liver model's top tissue-specific features are seven TFs in HepG2; breast model features are ER-α and GR in T-47D and ECC-1; whole-blood features come from blood-derived lines.
- **eQTL direction.** For the top 500 strongest-predicted GTEx eQTL variants, ExPecto gets the direction right 92% of the time; the tissue-matched model is the most accurate. Results replicate on brain, primary immune cell and blood eQTL studies.
- **MPRA.** On lymphoblastoid MPRA data, the lymphoblastoid model reached AUROC 0.815 and beat all other tissue models.
- **Rare variants.** Among 16.5 million 1000 Genomes variants, high-effect predictions have the same MAF distribution as all variants, and strong predictions enrich for GTEx eQTLs at all frequencies.
- **GWAS prioritisation.** Across 3,000 GWAS (390,085 LD variants at r² > 0.75 to 15,571 lead SNPs), loci with stronger predicted effects replicated more often in other GWAS (P = 6.3 × 10⁻¹⁸⁹), and strong-effect LD variants were more often the exact replicated variant (P = 5.6 × 10⁻¹⁴).
- **Luciferase validation.** The top three prioritised SNPs with no prior functional evidence all changed reporter activity in the predicted direction, while none of the seven corresponding GWAS lead SNPs did: rs1174815 (IRGM; Crohn's, UC, IBD; P = 3 × 10⁻⁶), rs147398495 (near CCR1; Behçet's; P = 7 × 10⁻¹⁰) and rs381218 (HLA-DOA; chronic HBV; fourfold change, P = 1 × 10⁻⁹).
- **Mutation catalogue.** All single-nucleotide changes within 1 kb of each representative TSS (>140 million) were scored; >1.1 million had strong predicted effects. Expression-decreasing mutations cluster near −50 bp, the core-promoter position. Stronger-effect bases are more constrained in modern humans (P = 2.4 × 10⁻³⁶) and over evolution (P = 2.2 × 10⁻¹⁶).
- **Variation potential.** Low-magnitude genes are ubiquitous housekeeping genes (splicing, translation, protein folding, energy metabolism); high-magnitude genes are tissue- or condition-specific. Negative direction predicts active expression, positive predicts repression in that tissue (e.g., synaptic genes negative in brain, positive elsewhere). Putative positive- vs negative-constraint genes show opposite allele-frequency and conservation patterns (P < 1.6 × 10⁻¹⁴), not explained by expression level, and stronger-constraint genes are enriched for GWAS disease genes (P = 6.1 × 10⁻⁵³).
- **Risk allele prediction.** Strong-effect HGMD regulatory mutations are mostly predicted to decrease expression of positive-constraint genes (F7, F9, PROC, PROS1, APOA1, LDLR, UNC13D, BTK, HNF1A); the one predicted strong increase is at TERT, a negative-constraint gene. For GWAS risk alleles (37 reference, 63 alternative), the constraint violation score is predictive (AUROC 0.67, P = 0.002).

## Methods / evidence

CNN trained on ENCODE and Roadmap profiles predicts each 200 bp region from 2,000 bp of sequence; scanned in 200 bp steps over ±20 kb of the representative TSS (chosen as the most abundant FANTOM5 CAGE peak within 1 kb of a GENCODE v24 TSS; such TSSs are more conserved, P = 5.7 × 10⁻⁸). Spatial transformation uses prespecified exponential decays (decay constants listed as {0.01, 0.02, 0.05, 0.10, 0.20}, upstream and downstream separately). Expression models: L2-regularised linear regression fitted by gradient boosting (λ = 100, η = 0.01, 100 rounds), one per tissue. A ±20 kb window maximised accuracy; 50, 100 or 200 kb gave negligible gain. Variant effects sum chromatin-effect changes at nine 200 bp offsets within the 2 kb context. For MPRA, a 230 bp regulatory model with the element fixed at −100 bp was used. Luciferase: 230 nt fragments in pGL4.23 in BE(2)-C cells, 4–6 replicates, 2–5 experiments. Constraint inference: locfdr empirical-null Gaussian mixture on per-gene mean predicted effect; probability >0.5 assigns positive or negative constraint. Code: github.com/FunctionLab/ExPecto.

Weight: strong held-out design (whole-chromosome hold-out at every training stage, paralog control) and real wet-lab validation, but only three SNPs were tested by luciferase, all in a single neuroblastoma cell line. Figure panels are images in the clipping; per-tissue values are not reported here.

## Limitations

**Authors' own:**
- Accuracy and coverage could improve with more chromatin profiling (especially chromatin marks and TF binding), with data on ultra-distal regulation through long-range interactions, and with sequence-independent epigenetic mechanisms such as imprinting via DNA methylation.
- Training uses gene-level expression mapped to one representative TSS, an approximation to TSS-specific transcription.
- ExPecto predicts expression effects only; DeepSEA can flag variants with chromatin effects that do not change expression.

**Reviewer notes:**
- The variation-potential analysis covers only ±1 kb of the TSS, so the constraint inferences are about promoter-proximal regulation, not distal enhancers. (synthesis)
- The methods text says "ten exponential functions" but lists five decay constants; the ten presumably come from five constants × upstream/downstream. (synthesis)
- Luciferase validation used BE(2)-C neuroblastoma cells for immune-disease variants, so the reporter context is not the disease tissue. (synthesis)

## Surprising or load-bearing bits

- The linear, fixed-basis spatial layer makes variant effects an exact closed-form function of chromatin-effect differences and distance to TSS, which is why 140 million mutations are cheap to score.
- Expanding context beyond 40 kb did not help this architecture, whereas later end-to-end models (Basenji, Enformer) argue that longer context helps. The gap may reflect architecture rather than biology. (synthesis)
- Variation potential turns a predictive model into a constraint estimator: the sign of the average mutation effect tells you whether a gene is active, and therefore whether loss or gain of expression is the dangerous direction.

## Concepts touched

- [[sequence-to-function-model]] — two-stage design: sequence → chromatin profiles → expression.
- [[variant-effect-prediction]] — eQTL direction, MPRA, GWAS replication, luciferase validation, risk-allele prediction.
- [[convolutional-neural-network]] — DeepSEA architecture deepened and widened to 2 kb and 2,002 features.
- [[chip-seq]] — TF and histone ChIP-seq predictions carry more expression signal than DNase.
- [[cis-regulatory-element]] — core-promoter position (−50 bp) dominates expression-decreasing mutations.

## Connections to other sources

- Extends [[zhou-2015-deepsea]] (same lab) from chromatin to expression; compared against it for GWAS locus replication (Supplementary Fig. 17, not in the clipping).
- Contemporary to [[kelley-2018-basenji]], which predicts CAGE end-to-end from 131 kb instead of through a fixed spatial basis. (synthesis)
- Same lab's later model [[chen-2022-sei]] keeps the chromatin-profile-first approach but clusters predictions into sequence classes.
- Long-context successors [[avsec-2021-enformer]] and [[linder-2025-borzoi]] predict expression tracks directly. (synthesis)

## Open questions

- Would the variation-potential constraint signal hold if distal enhancers were included? (synthesis)
- How does a fixed exponential basis compare with learned long-range attention on the same eQTL benchmarks? (synthesis)
- The constraint violation score is modest for common GWAS variants (AUROC 0.67); what limits it — model error, LD, or pleiotropy?

## Related

- [[sequence-to-function-model]] · [[variant-effect-prediction]] · [[zhou-2015-deepsea]] · [[chen-2022-sei]] · [[kelley-2018-basenji]] · [[40-Topics/sequence-models-and-foundation-models]]
