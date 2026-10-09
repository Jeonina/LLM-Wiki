---
type: summary
title: "Lal et al. 2026 — Decoding sequence determinants of gene expression in diverse cellular and disease states"
source: "[[00-Sources/papers/Decoding sequence determinants of gene expression in diverse cellular and disease states]]"
source_quality: full
source_sha256: "ad0d0ee8187aa3a08f15cfb7a293a34435adf88042d5a99567333864b7eb6f12"
source_kind: paper
author: "Avantika Lal, Alexander Karollus, Laura Gunsalus, David Garfield, Surag Nair, Alex M. Tseng, … Gokcen Eraslan (16 authors, all Genentech)"
published: 2026-05-25
ingested: 2026-10-08
doi: "10.1038/s41592-026-03102-0"
journal: "Nature Methods"
tags: [Decima, Borzoi, sequence-to-function, pseudobulk, scRNA-seq, snRNA-seq, cell-type-specific-expression, disease-state, eQTL, sc-eQTL, GWAS, variant-effect, TF-MoDISco, attribution, regulatory-element-design, directed-evolution, Genentech]
entities: []
concepts: ["[[sequence-to-function-model]]", "[[variant-effect-prediction]]", "[[pseudo-bulk]]", "[[scrna-seq]]", "[[cis-regulatory-element]]", "[[transcription-factor-motif]]", "[[batch-effect]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[40-Topics/computational-methods]]"]
---

**Citation:** Lal et al. (2026) — *Decoding sequence determinants of gene expression in diverse cellular and disease states* — *Nature Methods*. [DOI](https://doi.org/10.1038/s41592-026-03102-0)

# Lal 2026 — Decima

> Decima fine-tunes all of **Borzoi** to predict a gene's expression across **8,856 pseudobulks** (cell type × tissue × disease × study) built from sc/snRNA-seq of **over 22 million cells**, covering 201 cell types, 271 tissues and 82 diseases. Each example is one gene: 524,288 bp of sequence starting 163,840 bp upstream of the TSS, plus a fifth input channel masking the gene body. Borzoi's output head is replaced by length-wise mean pooling and a linear layer to 8,856 log(CPM+1) values. The key change is the loss: Borzoi's Poisson + multinomial loss is applied **across pseudobulks for one gene**, not across positions, with the Poisson total down-weighted to 10⁻⁴, so the model is pushed to learn between-cell-type differences. Working at pseudobulk instead of single-cell resolution is what lets it train on atlas scale. Decima predicts held-out genes (mean Pearson 0.80 per pseudobulk, 0.58 per gene across pseudobulks), recovers lineage TF motifs through attributions, ranks single-cell eQTLs and their cell type above Borzoi, and is used in silico to design a Crohn's-fibroblast-biased promoter.

## Key claims

- **Held-out genes.** On 1,811 test genes (an ensemble of four models, one per Borzoi replicate), mean Pearson between measured and predicted expression was 0.80 across genes within a pseudobulk and 0.58 across pseudobulks within a gene. Classifying cell-type-specific genes (z ≥ 1) from predicted z scores gave mean AUROC 0.82.
- **Pretraining and fine-tuning both needed.** A randomly initialised Decima and a Decima with frozen Borzoi weights (head only) both "performed poorly" (Supplementary Table 2, not in the clipping). The pseudobulk-axis loss was critical. The gene mask mattered less. Accuracy held for cell types absent or rare in Borzoi's training data.
- **Versus single-cell models.** On the same cell types, Decima beat an earlier single-cell expression model and matched one that also takes scATAC-seq as input (Supplementary Fig. 10; the methods are not named in the main text).
- **Attributions find regulatory elements but decay with distance.** Input × gradient attributions are highest at promoters, then exon–intron junctions, then exons. Intronic CREs score above the rest of the intron. ENCODE CREs over 100 kb away score above background, but against CRISPRi enhancer–gene data the learned effects decay with distance like other sequence models. The authors conclude that the cell-type gains are not from better distal enhancer modelling.
- **Lineage TFs from differential attributions.** "DE attributions" (gradient of predicted log fold change between a positive and negative pseudobulk set) clustered with TF-MoDISco recovered RFX (ciliated), TEAD and GATA6 (type I pneumocytes), p63 (basal), SOX2 and GRHL (airway lineage) in seven lung epithelial types. In brain it recovered two repressors: MYT1L lowers non-neuronal genes in neurons, REST lowers neuronal genes in non-neurons. E2F came out for cycling vs resting Tregs, and GATA4/6 and TEAD1 for cardiac vs other fibroblasts (Pearson 0.53 on test-gene fold changes).
- **Single-cell eQTLs.** On fine-mapped OneK1K sc-eQTLs (PIP > 0.9, 20 matched negatives each), Decima beat Borzoi in 19 of 21 cell types and overall, and beat TSS distance. Predicted effect correlated with eQTL beta at Pearson 0.42 (n = 987). For variants with predicted |LFC| > 0.01 it rose to 0.58 (n = 447) with 87% sign agreement. For 513 variants that are eQTLs in only some cell types, predicted effects were higher in the matching cell type than in other expressing cell types (P = 1.1 × 10⁻⁷).
- **GTEx bulk eQTLs.** Positive correlation with beta in all tissues. Close to Borzoi, which was trained on those GTEx samples, and better than Borzoi in six tissues for classification and seven for correlation.
- **GWAS.** For 837 fine-mapped regulatory GWAS SNPs across 39 traits, AUPRC 0.23 against 10 matched controls each (TSS-distance baseline 0.14). 40% of GWAS variants scored significantly above their controls. Only 95 (11%) were also eQTLs, and 62% of those were detected vs 39% overall. Predicted cell types fit trait biology: autoimmune variants in T/NK cells, blood traits in erythroid progenitors and megakaryocytes, height in fibroblasts and vascular cells, triglycerides in enterocytes and hepatocytes.
- **Disease vs healthy.** Across 565 matched disease/healthy pseudobulk pairs, the mean Pearson between measured and predicted fold change on test genes was 0.24. Crohn's ileal fibroblasts reached 0.52. DE attributions found inflammatory motifs (JUN/FOS, STAT/IRF, C/EBP) in several diseases, weaker in chronic kidney disease, a TWIST1–homeodomain dimer motif in fibroblasts in fibrotic diseases, and NF-κB in Crohn's fibroblasts.
- **Design.** 100 rounds of in silico directed evolution of a 200-bp element in a safe-harbour locus gave a sequence predicted to drive 6.84-fold higher expression in Crohn's fibroblasts than other gut cell types and 4.31-fold higher than healthy fibroblasts. It contains TWIST1, TBP, C/EBP, STAT3, CREB3 and IRF motifs. Not tested experimentally.

## Methods / evidence

Training data: SCimilarity, a Human Brain Atlas, a skin atlas and an adult retina atlas, filtered to drop cell lines, cancers, organoids, unannotated and likely misannotated cell types, and tiny low-quality pseudobulks. Cells from different donors in the same study are summed. Gene splits follow Borzoi's regions, so all test genes are in Borzoi's test regions. Training: full model, Adam, learning rate 3 × 10⁻⁵, 15 epochs, ±5 kb shift augmentation, one A100 for about a day per replicate. Interpretation: input × gradient, TF-MoDISco (±10 kb of TSS), Tomtom against HOCOMOCO v12, motifs grouped with GimmeMotifs. Variant sets: OneK1K via eQTL Catalog, GTEx, and an in-house GWAS fine-mapping (DENTIST → PolyFun → SuSiE) over 39 traits. Code from Genentech on GitHub; weights and genome-wide predictions on Zenodo.

Weight: a large, broad atlas study with well-matched variant controls. Several key comparisons (ablations, single-cell model comparison, Borzoi GWAS comparison) are in supplementary tables and figures that are not in the clipping, so they are reported here only as the main text describes them. All authors were Genentech employees.

## Limitations

**Authors' own:**
- Experimental batch effects could create spurious regulatory sequences.
- Continuous cell states are forced into discrete pseudobulks. Donors within a study are merged, so person-to-person variation is not modelled.
- Captures only *cis* regulation around one gene. Output space is fixed to the training cell type/tissue/disease combinations; it does not transfer to unseen contexts.
- Disease vs healthy changes agree poorly across studies of the same disease, which caps how well disease effects can be learned.
- Does not learn distal enhancer–gene links better than earlier models; gains may come from cell-type-specific proximal motifs.
- Designed elements have not been tested experimentally.

**Reviewer notes:**
- Unlike [[hingerl-2025-scooby]], there is no cell embedding, so a new cell type or new dataset means retraining the output layer. Decima trades single-cell resolution for atlas breadth. (synthesis)
- The CRISPRi result means Decima's distal attributions (e.g., the 57-kb *JAZF1* variant) should be read as hypotheses, not as evidence that it models long-range regulation. (synthesis)
- Germline variants only. Somatic variants seen by single-cell DNA sequencing are not addressed, though the same scoring could in principle apply. (synthesis)

## Surprising or load-bearing bits

- **The loss is the method.** Moving the multinomial term from the position axis to the pseudobulk axis is what makes a bulk model learn cell-type differences.
- **Frozen Borzoi is not enough.** As in [[hingerl-2025-scooby]] and [[fan-2026-gfetm]], pretrained features alone did poorly; the whole trunk had to be fine-tuned. (synthesis)
- **Repressor motifs come out** (MYT1L, REST, ZEB2), not only activators.
- **Variant effect is not expression level.** *FES*, *SLC1A5* and *NFE2* are highly expressed in several cell types where Decima predicts only weak variant effects.

## Concepts touched

- [[sequence-to-function-model]] — a bulk-pretrained model (Borzoi) fine-tuned to atlas-scale pseudobulk expression.
- [[variant-effect-prediction]] — sc-eQTL, GTEx eQTL and GWAS scoring at cell-type resolution.
- [[pseudo-bulk]] — pseudobulk aggregation as the scalable training unit.
- [[scrna-seq]] — learns regulatory sequence from expression alone, without matched chromatin data.
- [[cis-regulatory-element]] — attributions over promoters, intronic CREs and distal CREs.
- [[transcription-factor-motif]] — TF-MoDISco motifs from differential attributions.
- [[batch-effect]] — named as a source of spurious learned sequence features.

## Connections to other sources

- Built on [[linder-2025-borzoi]]. Background seq-to-function lineage: [[zhou-2018-expecto]], [[chen-2022-sei]], [[avsec-2021-enformer]].
- Sister approach: [[hingerl-2025-scooby]] (Alexander Karollus is an author on both) adapts Borzoi to single cells through a cell-embedding decoder; Decima instead predicts thousands of pseudobulks across many atlases. (synthesis)
- Frozen-vs-fine-tuned pattern echoes [[fan-2026-gfetm]]. (synthesis)
- Synthetic regulatory element design parallels [[kempynck-2026-crested]], which designs and tests cell-type-specific enhancers from accessibility models. (synthesis)

## Open questions

- Would adding a cell-state representation (the authors suggest a transcriptome embedding) let Decima capture *trans* effects and generalise to unseen contexts?
- Do the designed disease-biased promoters work in cells?
- How much of the disease signal is batch or study structure rather than disease biology, given poor cross-study agreement? (synthesis)

## Related

- [[sequence-to-function-model]] · [[variant-effect-prediction]] · [[pseudo-bulk]] · [[linder-2025-borzoi]] · [[hingerl-2025-scooby]] · [[kempynck-2026-crested]] · [[40-Topics/sequence-models-and-foundation-models]]
