---
type: summary
title: "Zhao et al. 2025 — MambaCpG: an accurate model for single-cell DNA methylation status imputation using mamba"
source: "[[00-Sources/papers/MambaCpG_ an accurate model for single-cell DNA methylation status imputation using mamba]]"
source_kind: paper
author: "Qi Zhao, Ze Li, Qian Mao, Tingwei Chen, Yiran Zhang, Bingle Li, Zheng Zhao, Xiaoya Fan"
published: 2025-07-28
ingested: 2026-10-07
doi: "10.1093/bib/bbaf360"
journal: "Briefings in Bioinformatics 26(4):bbaf360"
tags: [MambaCpG, imputation, single-cell-methylation, state-space-model, Mamba, deep-learning, CpG-Transformer, DeepCpG, GraphCpG, long-range-dependency, scBS-seq, scRRBS, snmC-seq]
entities: []
concepts: ["[[30-Concepts/imputation]]", "[[30-Concepts/scbs-seq]]", "[[30-Concepts/bisulfite-sequencing]]", "[[30-Concepts/convolutional-neural-network]]", "[[30-Concepts/cpg-island]]"]
topics: ["[[40-Topics/dna-methylation]]", "[[40-Topics/computational-methods]]"]
---

**Citation:** Zhao et al. (2025) — *MambaCpG: an accurate model for single-cell DNA methylation status imputation using mamba* — *Briefings in Bioinformatics* 26(4):bbaf360. [DOI](https://doi.org/10.1093/bib/bbaf360)

# Zhao 2025 — MambaCpG

> Single-cell methylomes cover only 1–40% of CpGs per cell, so imputation is routine — but Transformer imputers (CpG Transformer) pay quadratic cost and must use small windows. MambaCpG swaps attention for **bidirectional Mamba (selective state-space) blocks**, which scale linearly, letting it use much wider windows (W = 1,024 CpGs for <200 cells, 256 for larger sets, vs 41 in CpG Transformer and 21 in GraphCpG). Each matrix entry is embedded from its methylation state, a CNN embedding of the 1,001-bp sequence around the CpG, a learnable cell embedding and a 2D positional encoding; training is BERT-style masking of 15% of observed sites. The claim: best on **large, very sparse** datasets, competitive on small ones, with fewer parameters and less memory.

## Key claims

- **Benchmark on seven public datasets** (chr10 test, chr5 validation, following CpG Transformer): 2i (12 cells) and Ser (20) mESC scBS-seq; HCC (25, scRRBS); MBL (30, scRRBS); Hemato (122 HSPCs, scBS-seq); Neuron-Mouse (690) and Neuron-Homo (780) snmC-seq. Sparsity ranges 0.7779–0.9842.
- **AUC (MambaCpG vs best competitor)**: top on Ser (91.42), Hemato (91.01), Neuron-Mouse (92.48 vs GraphCpG 91.52) and Neuron-Homo (94.20 vs 93.25); second to CpG Transformer on 2i (85.08 vs 85.81), HCC (97.67 vs 97.85) and MBL (92.30 vs 92.43). Top-or-runner-up in all 7 (CpG Transformer 5, GraphCpG 2, DeepCpG 0). MCC follows the same pattern.
- **Efficiency**: 125K parameters vs 284K for CpG Transformer; GPU memory similar on small datasets, significantly lower on large ones (on neuron datasets W had to be cut to 256 for MambaCpG but 128 for CpG Transformer).
- **Ablation (MBL)**: removing the CpG-state embedding drops AUC by 8.22, removing Mamba entirely by 8.82, the DNA embedding by 1.40; one-directional Mamba loses 2.19–2.32; cell and positional embeddings matter little (≤0.26 combined). Four stacked bi-Mamba layers were best.
- **Scales with cell number**: on Hemato subsets, CpG Transformer wins at 25 cells but barely improves with more; MambaCpG overtakes it by 100 cells. All models degrade when sparsity exceeds 0.985. Authors recommend MambaCpG for datasets >100 cells.
- **Long-range dependencies**: Integrated Gradients show focus on ±20 neighbouring CpGs (as CpG Transformer) plus selective contributions from CpGs >100 positions / >10,000 bp away, which CpG Transformer's window cannot reach.
- **Heterogeneity**: whole-chromosome hold-out performs worse than random per-chromosome sampling (worst on X and Y); cell-to-cell contribution scores partially cluster by Hemato cell type; cross-dataset transfer without fine-tuning groups human vs mouse. **Pretraining on 12–36 cells from other datasets did not improve AUC on 2i** nor save time — the authors recommend end-to-end training.

## Methods / evidence

Methylation matrix (cells × CpGs, values 1/0/−1) split into windows; embeddings concatenated, projected, positionally encoded, flattened, passed through 4 bi-Mamba layers (forward + flipped-reverse Mamba, residual + layer norm), sigmoid output; BCE loss on masked sites; AdamW, cosine schedule, single RTX 4090. Comparators: DeepCpG, CpG Transformer, GraphCpG (all deep models; no Melissa/CaMelia/LightCpG run).

Weight: margins on large datasets are ~1 AUC point; small-data results favour CpG Transformer. One test chromosome per dataset, no repeated splits or error bars in Table 2. Interpretability claims rest on attribution maps from a single dataset.

## Surprising or load-bearing bits

- **Window size is the real variable.** Linear-cost sequence models make wide CpG windows affordable; the >10 kb dependencies are a consequence of that. Whether they reflect biology (the authors cite prior reports of long-range methylation correlation) or dataset-specific structure is untested. (synthesis)
- **Pretraining doesn't transfer** at these data sizes — in contrast to foundation-model enthusiasm elsewhere in single-cell work.
- **Evaluation split matters**: the paper's own comparison shows random within-chromosome sampling inflates AUC relative to whole-chromosome hold-out.

## Concepts touched

- [[imputation]] — CpG-level single-cell methylation imputation; selective SSMs as a scalable alternative to attention.
- [[scbs-seq]] / [[bisulfite-sequencing]] — the sparsity problem across scBS-seq, scRRBS and snmC-seq.
- [[convolutional-neural-network]] — CNN sequence encoder for the 1,001-bp CpG context.

## Connections to other sources

- Predecessors it benchmarks: [[angermueller-2017-genomebiol]] (DeepCpG); cited alternatives [[kapourani-2019-melissa]] (Bayesian clustering-based imputation).
- **Disputed by an independent benchmark**: [[liang-2026-scmeth-imputation-benchmark]] found no universal winner, MambaCpG "volatile", and MambaCpG/CpG Transformer the most sensitive to random-split leakage — tempering this paper's "superior" framing.
- Data sources: [[smallwood-2014-natmethods]] (2i/Ser), [[hou-2016-sctrio-seq]] (HCC), [[luo-2017-snmc-seq]] (neurons).
- Other deep methylation models: [[spix-2025-scdeep-mc]].

## Open questions

- Gains of ~1 AUC on large datasets — significant under repeated chromosome hold-outs?
- Are >10 kb dependencies biological or memorised dataset structure?
- Whole-genome datasets with thousands of cells (atlas scale, e.g. [[nichols-2025-scimetv3]]) remain untested.

## Related

- [[imputation]] · [[liang-2026-scmeth-imputation-benchmark]] · [[angermueller-2017-genomebiol]] · [[40-Topics/dna-methylation]]
