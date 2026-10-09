---
type: summary
title: "Kong et al. 2026 — A Foundation Model of Cancer Genotype Enables Precise Predictions of Therapeutic Response"
source: "[[00-Sources/papers/A Foundation Model of Cancer Genotype Enables Precise Predictions of Therapeutic Response.pdf]]"
source_quality: full
source_sha256: "402b565b65bb9dfac402c0a9382bf6ae774a4d4129629b5050d3bb42b2aea7eb"
source_kind: paper
author: "JungHo Kong, Ingoo Lee, Dean Boecher, Akshat Singhal, Marcus R. Kelly, Jimin Moon, … Hannah Carter, Zhen Wang (corresponding), Trey Ideker (corresponding)"
published: 2026-10
ingested: 2026-10-09
doi: "10.1158/2159-8290.CD-25-1735"
journal: "Cancer Discovery 16(10):2021–2036 (first posted May 26, 2026)"
tags: [MutationProjector, cancer-genome-foundation-model, tumor-genotype, gene-panel, MSK-IMPACT, GENIE, TCGA, graph-attention-network, molecular-networks, masked-gene-prediction, immunotherapy-response, chemotherapy-response, metastasis, tissue-of-origin, biomarker-discovery, bulk-tumour, genotype-layer-gap]
entities: []
concepts: ["[[single-cell-foundation-model]]", "[[copy-number-variation]]", "[[mutational-signatures]]", "[[gene-regulatory-network]]", "[[cancer-of-unknown-primary]]", "[[dimensionality-reduction]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[40-Topics/computational-methods]]", "[[40-Topics/cancer-clonal-evolution]]", "[[40-Topics/scdna-seq]]"]
---

**Citation:** Kong et al. (2026) — *A Foundation Model of Cancer Genotype Enables Precise Predictions of Therapeutic Response* — *Cancer Discovery* 16(10):2021–36. [DOI](https://doi.org/10.1158/2159-8290.CD-25-1735)

# Kong 2026 — MutationProjector

> MutationProjector is a pretrained tumour-genotype model built for clinical gene-panel data. It treats each tumour as **468 MSK-IMPACT genes**, each with a binary state for somatic mutation, copy-number amplification (CNA) and copy-number deletion (CND). Three covariate nodes are added: TMB, aneuploidy and dominant mutational signature. A graph attention network then passes messages over eight molecular-interaction networks, with one attention head per network. Pretraining masks 15% of genes and asks the model to recover their alteration state, with auxiliary cancer-type and tumour-infiltrating-lymphocyte (TIL) labels. The corpus is **30,328 bulk solid tumours** from GENIE and TCGA across 10 cancer types. The frozen embedding then feeds a random forest for immunotherapy response, chemotherapy response, metastasis and tissue of origin, trained on small cohorts (94–1,974 patients). It is a reusable genotype-layer model, but at **gene-level, bulk-tumour** resolution.

## Key claims

- **Corpus.** The model was pretrained on 30,328 solid tumours of 10 types from AACR Project GENIE 15.0 and TCGA, with breast (8,163) and colorectal (6,152) the largest groups. Tumours carry on average 9.1 mutated, 15.9 amplified and 14 deleted genes among the sequenced genes. Covariates are TMB (reported, or computed with Maftools), arm-level aneuploidy (ASCETS) and seven dominant signatures (MESiCA for panels, SigProfiler for WES/WGS).
- **Knowledge graph.** Eight networks (BioPlex, SIGNOR, SignaLink, TRRUST, PhosphoSitePlus, UbiNet/UbiBrowser, ISLE/SynLethDB, DDRAM, STRING, PCNet, grouped into physical, transcriptional, phosphorylation, ubiquitination, genetic, DNA-repair and functional types) contribute **19,789 interactions** among the 468 genes.
- **Masked-gene reconstruction.** Under 10-fold cross-validation, overall AUPRC was **0.21 against 0.02 for random**, which the authors call a 9.7-fold improvement. Performance was stable across cancer types and similar on an external lung adenocarcinoma cohort. The model recovers co-occurrence (CCND1–CDKN2A copy-number events in head and neck cancer) and mutual exclusivity (BRAF–NRAS in melanoma).
- **Auxiliary heads.** Cancer-type AUPRC ranged from 0.36 (esophageal) to 0.94 (breast). TIL AUPRC was 0.42 inflamed, 0.64 excluded and 0.45 desert. These generally beat alternative configurations in ablations (no graph, a plain transformer, a feed-forward network, shuffled graphs, single graphs).
- **Embedding structure.** Tumours separate roughly by tissue, with a shared squamous cluster (LUSC, HNSC, ESCA). GENIE and TCGA samples co-cluster, which the authors read as minimal batch effect. Tissue still separates when the cancer-type head is removed. The embedding also separates HPV status and mRNA basal/luminal subtypes in bladder and breast, neither of which was an input. It adds information beyond tissue type for 95.7% of genes.
- **Immunotherapy.** A random forest trained on 94 anti-PD-1/PD-L1 patients was tested on three independent cohorts: bladder (n = 130, HR 0.71, P = 1.6 × 10⁻²), lung (n = 229, HR 0.74, P = 1.7 × 10⁻⁵) and melanoma (n = 144, HR 0.59, P = 5.8 × 10⁻³). It compared favourably with PD-L1 expression, TMB, MSI and KRAS, and with logistic regression, random forest and a supervised GNN without pretraining. The bladder test cohort was sequenced on FoundationOne, a different panel from MSK-IMPACT.
- **Chemotherapy, metastasis, tissue of origin.** Trained on 237 cisplatin-treated tumours and tested on 42 bladder tumours, the chemotherapy model gave HR 0.43 (P = 2.5 × 10⁻²). Metastasis prediction for LUAD, trained on 1,974 and tested on 128, reached AUPRC 0.84. Tissue of origin for metastases was trained on 272 and tested on 112. The paper reports 3,362 downstream patients in total.
- **Biomarkers from attention.** TMB was the top feature in every immunotherapy cohort. Less expected features were KMT2D and SWI/SNF genes (ARID1A, ARID2, SMARCA4). Pairs enriched in predicted non-responders were KRAS–STK11 (14%), KEAP1–STK11 (13%) and SMARCA4–STK11 (10%), although none of these genes alone was more frequent in non-responders. Of the high-attention gene pairs, 94% would not have been prioritised by a standard co-mutation analysis.

## Methods / evidence

Each gene is the element-wise sum of a learnable gene-identity token and a learnable "mutation embedding" over the possible combinations of mutation, CNA and CND. Masking replaces only the mutation embedding, so the model knows which gene it is predicting but not its state. TMB and aneuploidy are binned into five levels (as in scBERT), and covariate nodes connect to every gene in every head, like special tokens. The encoder is two GATv2Conv units (PyTorch Geometric) with eight heads, one per network, plus residuals and no self-loops, with 10-d gene and covariate features. The loss is a weighted BCE over masked genes, cancer type and TIL, with the TIL label taken from a ResNet H&E model. Training used AdamW, learning rate 0.001, batch size 64, 100 epochs and dropout 0.1. Pretraining was evaluated on an 80/20 split (24,262 / 6,066); all 30,328 tumours were then used to pretrain the model for downstream work. Downstream, the embedding is the input to a random forest with 100 trees and depth 10. For drug response, the top 20% of predicted scores are called "responders" and scored by log-rank test, and HRs are per SD of predicted probability from univariate Cox. Feature importance is the Spearman correlation of an attention-weighted linear probe. Code: github.com/idekerlab/MutationProjector.

Weight: a peer-reviewed paper with three independent immunotherapy test cohorts, a different-panel test (FoundationOne), and ablations against graph-free and non-pretrained baselines. Downstream training cohorts are small (94 and 237 patients), the chemotherapy test cohort has 42 patients, and comparators are classical ML and single biomarkers, not other genotype FMs. The text gives the tumour embedding dimension as 10 in Results but 180 in Methods ("Transfer Learning"), and does not explain the difference. (synthesis)

## Limitations

**Authors' own:**
- Pretraining covers 10 solid tumour types. Pancreatic, prostate and sarcoma data, and ICGC resources, could extend it.
- Pretraining uses genomics only. EHR annotations, radiology images and mRNA profiles could add to the pretraining step.
- Other clinical tasks, including liquid biopsy (ctDNA) for early detection, remain to be explored.

**Reviewer notes:**
- The input vocabulary is **fixed to 468 panel genes with binary states**. There are no positions, segment sizes, copy-number levels or allele fractions. Genes outside the panel and non-coding events cannot be represented, and aneuploidy enters only as a binned covariate. (synthesis)
- Downstream claims rest on a top-20% responder threshold and per-SD Cox HRs across cohorts of 42–229 patients. The paper does not report confidence intervals for the masked-gene AUPRC on the main split, and "state-of-the-art" means compared with classical ML and single biomarkers. (synthesis)
- Pretraining mixes self-supervision with supervised cancer-type and image-derived TIL labels. The representation is therefore not purely self-supervised, and part of its structure (tissue clustering) is directly supervised. The authors show tissue still separates without the cancer-type head. (synthesis)

## Surprising or load-bearing bits

- **Network priors as attention heads.** Assigning one head per interaction network forces each head to carry a distinct biological channel. Pretraining becomes "recover a masked gene from its network neighbours", which builds known biology into the inductive bias.
- **Combinations matter more than single genes.** KRAS, STK11 and KEAP1 were not individually enriched in immunotherapy non-responders, but their pairwise co-alterations were. This is the paper's main case for a joint genotype representation over single-gene rules.
- **Signals not in the input.** HPV status and mRNA basal/luminal subtypes are recoverable from DNA panel calls alone.
- **What it would take to use MutationProjector on single-cell DNA.** The input format is the easiest of the bulk genotype FMs to fill from cells. A per-cell CNA profile from a scDNA caller can be thresholded to gene-level amplification and deletion over the 468 genes, and targeted single-cell DNA panels give per-cell mutation calls for a subset of them. The problems are dropout, missing genes and covariates. Allelic dropout turns true mutations into apparent wild-type, which the model would read as "unaltered" rather than "unknown". Genes not covered by a single-cell panel would have to be handled with the mask token. Per-cell TMB and signatures are not well defined. Even then, each cell would be scored as if it were a whole tumour, and no step models clone structure. (synthesis)

## Concepts touched

- [[single-cell-foundation-model]] — a pretrained genotype FM, but on bulk gene-panel calls. It shows the genotype-layer FM pattern exists at bulk resolution only. (synthesis)
- [[copy-number-variation]] — CNA and CND per gene as masked targets. CCND1–CDKN2A co-amplification and deletion is a recovered dependency.
- [[mutational-signatures]] — seven dominant signatures (APOBEC, SBS1, SBS5, MMR, POLE, tobacco, UV) as covariate tokens. APOBEC is a top metastasis feature.
- [[gene-regulatory-network]] — transcriptional-regulation networks (TRRUST, SIGNOR, SignaLink) are among the eight graphs used for message passing.
- [[cancer-of-unknown-primary]] — tissue-of-origin prediction for metastases from panel genotype.
- [[dimensionality-reduction]] — UMAP of the final-layer embedding to read tissue, HPV and subtype structure.

## Connections to other sources

- Sister genotype-FM paper: [[sidhom-2026-tessera]] uses WES variant and segment tokens with masked reconstruction plus SNV–CNA contrastive alignment, and transfers to MSK-IMPACT panels. MutationProjector instead starts from panel gene calls and adds network priors. Both freeze the representation for clinical tasks, and both are bulk. (synthesis)
- The authors cite scBERT, Geneformer, scGPT and scFoundation as the RNA-side precedents. scGPT is [[cui-2024-natmethods]] in this wiki.
- Single-cell CNA callers that could, in principle, provide per-cell gene-level CNA states: [[garvin-2015-natmethods]], [[wang-2020-scope]], [[zaccaria-2021-chisel]]. The per-dataset scDNA transformer [[liu-2024-cot]] is the closest single-cell analogue and is not pretrained. (synthesis)
- Signature background: [[alexandrov-2013-mutational-signatures]].

## Open questions

- Does the embedding stay stable when the input comes from a different panel with partial gene overlap? The bladder FoundationOne test suggests yes, but missing genes are not discussed explicitly. (synthesis)
- Would masking-aware handling of "not covered" versus "wild-type" let the model accept sparse single-cell or ctDNA calls? (synthesis)
- How do MutationProjector and TESSERA compare head-to-head on the same tasks and cohorts? No such comparison exists yet. (synthesis)

## Related

- [[40-Topics/sequence-models-and-foundation-models]] · [[single-cell-foundation-model]] · [[copy-number-variation]] · [[sidhom-2026-tessera]] · [[liu-2024-cot]] · [[40-Topics/computational-methods]] · [[40-Topics/scdna-seq]]
