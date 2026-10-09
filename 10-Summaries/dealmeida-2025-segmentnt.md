---
type: summary
title: "de Almeida et al. 2025 — Annotating the genome at single-nucleotide resolution with DNA foundation models"
source: "[[00-Sources/papers/Annotating the genome at single-nucleotide resolution with DNA foundation models]]"
source_quality: full
source_sha256: "27d999c42dcc9fdba7e992f1e82ffa1dcdb6671fcb8fea6566818f2514475940"
source_kind: paper
author: "Bernardo P. de Almeida, Hugo Dalla-Torre, Guillaume Richard, Christopher Blum, Lorenz Hexemer, Maxence Gélard, … Uğur Şahin, Karim Beguir, Thomas Pierrot"
published: 2025-10-29
ingested: 2026-10-08
doi: "10.1038/s41592-025-02881-2"
journal: "Nature Methods"
tags: [SegmentNT, Nucleotide-Transformer, InstaDeep, BioNTech, dna-language-model, fine-tuning, semantic-segmentation, U-Net, genome-annotation, splice-sites, enhancers, promoters, CTCF, RoPE-context-extension, SegmentEnformer, SegmentBorzoi, multispecies, AUGUSTUS, SpliceAI]
entities: []
concepts: ["[[dna-language-model]]", "[[genomic-tokenization]]", "[[cis-regulatory-element]]", "[[jaccard-similarity]]", "[[sequence-to-function-model]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]"]
---

**Citation:** de Almeida et al. (2025) — *Annotating the genome at single-nucleotide resolution with DNA foundation models* — *Nature Methods*. [DOI](https://doi.org/10.1038/s41592-025-02881-2)

# de Almeida 2025 — SegmentNT

> **SegmentNT is not a new pretrained model: it fine-tunes the existing Nucleotide Transformer** (NT-Multispecies-v2, 500M, 6-mer tokens) by replacing its language-model head with a 63M-parameter 1D U-Net and training the whole network to segment DNA into **14 genic and regulatory element classes at single-nucleotide resolution** (multilabel, one binary mask per class, focal loss). It handles inputs up to 30 kb in training and generalises to 50 kb via NTK-aware RoPE rescaling. The same head on Enformer or Borzoi encoders (SegmentEnformer, SegmentBorzoi) reaches 196–524 kb and is better for regulatory elements, worse for splice sites. The core message is that self-supervised pretraining clearly pays off on this harder, nucleotide-level task: the same architecture with a random NT encoder reaches half the performance.

## Key claims

- **Pretraining is essential here.** At 3 kb, SegmentNT averages MCC 0.37 across 14 elements; the same model with a randomly initialised NT encoder reaches 0.16 and converges seven times slower. One-hot U-Nets of 63M/66M and 252M parameters reach 0.07–0.11; BPNet 0.10; original SpliceAI 0.18 and an up-scaled SpliceAI 0.27. Fine-tuning encoder and head together beats head-only, and the multispecies NT encoder beats the NT v1 2.5B 1000-Genomes encoder.
- **Longer context helps genic elements.** Average MCC rises from 0.37 (3 kb) to 0.42 (10 kb) to 0.45 (30 kb), mainly through protein-coding genes, 3′UTRs, exons and introns. SegmentNT-30kb is best at every evaluated length, peaking at 0.47 for 50 kb inputs and still 0.45 at 100 kb with RoPE rescaling. Without rescaling, SegmentNT-10kb drops to 0.07 at 100 kb (0.26 with rescaling).
- **Element-level difficulty.** Exons, splice sites, 3′UTRs and tissue-invariant promoters exceed MCC 0.5 at 3 kb; lncRNAs and CTCF sites are below 0.1. Enhancers are noisy (SegmentNT-10kb MCC 0.27 tissue-specific, 0.19 tissue-invariant). Mispredictions are enriched inside whole regulatory regions, not only at their edges.
- **Encoder choice is element-specific.** At 30 kb, SegmentNT (0.45) beats SegmentEnformer (0.34) and SegmentBorzoi (0.35) on average and on all gene elements, especially splice sites and poly(A) signals, where 128 bp / 32 bp binning hurts. Enformer and Borzoi encoders are better for lncRNAs, CTCF sites, promoters and enhancers, which the authors attribute to their supervised epigenomic pretraining. At native 196/524 kb they improve, but their averages stay below SegmentNT.
- **Versus AUGUSTUS.** On BEND single-isoform genes, SegmentNT-30kb is competitive (better on splice donors, similar on introns and acceptors, worse on CDS through lower precision). With all isoforms, and on whole test chromosomes where most windows lack genes, it outperforms AUGUSTUS on all gene elements with higher recall and precision; the gap is smaller at region level (SOV).
- **Versus SpliceAI and Pangolin.** On SpliceAI's mRNA test set adapted to 30 kb, auPRC is 0.93 (donor) and 0.93 (acceptor) vs 0.94/0.96 for SpliceAI and 0.94/0.94 for Pangolin. On SegmentNT's whole-chromosome test set it has higher MCC, i.e. fewer off-target calls. It is weaker than SpliceAI on non-coding RNA splice sites.
- **Regulatory elements.** SegmentNT beats sliding-window NT promoter/enhancer classifiers and DeePromoter on 30 kb inputs, and SegmentEnformer is best; segmentation is also much faster than sliding windows.
- **Cross-species.** The human model transfers best for exons and splice sites. A multispecies fine-tune (human + mouse, chicken, fly, zebrafish, worm; genic elements only) raises MCC on held-out human-distant animals (>100 Myr) from 0.49 to 0.57, matches on human-close species (0.64 vs 0.62), and on five unseen plants from 0.34 to 0.45, beating AUGUSTUS in all species except Arabidopsis.

## Methods / evidence

Labels: GENCODE V44 (level-3 transcripts removed; splice sites via HISAT2 script) for protein-coding gene, lncRNA, 5′/3′UTR, exon, intron, splice donor/acceptor, poly(A) signal; ENCODE SCREEN cCREs (790,000 enhancers, 34,000 promoters) split into tissue-invariant/specific using the Meuleman DHS index; CTCF-bound sites. Classes may overlap. Split: chr20/21 test, chr22 validation, homologous genes removed from test chunks (homologous distal regulatory elements not removed). Model: NT-v2 500M encoder → 2-down/2-up U-Net (2,048/4,096 kernels) → 2 logits per nucleotide per class; Adam 5e-5, batch 256, focal loss γ = 2; SegmentNT-3kb trained on 10.24 B tokens (8 H100s, 20 h), then progressively fine-tuned to 10, 20 and 30 kb (NTK-aware RoPE, s = 2.44 at 30 kb). Metrics: per-nucleotide MCC, auPRC, Jaccard, F1, and region-level SOV, over ten test-set samplings. Enformer and Borzoi were re-implemented in JAX (activations within 1e-5 of the originals). Weights and code are public (GitHub, Hugging Face).

Weight: a careful, well-ablated peer-reviewed methods paper with fair baselines in each sub-domain. Most per-element numbers are in figures and supplementary tables that are only referenced, not reproduced, in the clipped text. (synthesis)

## Limitations

**Authors' own:**
- NT context is limited (RoPE trained on 2,048 tokens ≈ 12 kb); performance falls beyond 50 kb.
- Homologous distal regulatory elements were not removed from the test set and "could still be inflating performance on these regions".
- Promoter/enhancer labels are a simplification of cell-type-specific activity; splitting by cell type is future work.
- No comparison with annotation pipelines that use experimental data or alignments (ChromHMM, Cactus), and Tiberius appeared during revision and was not compared.
- The multispecies model covers only genic elements and "should not be used for the prediction of regulatory elements".
- CNN baselines were not optimised for multi-element segmentation.

**Reviewer notes:** (at most three, each marked `(synthesis)`)
- Splice-site performance is lower on non-coding RNAs, which the authors themselves read as a possible correlative signal from coding sequence; much of the "annotation" skill may ride on CDS features. (synthesis)
- Labels for many non-model species come from Ensembl's own bioinformatic predictions, so "accuracy" there partly measures agreement with other predictors. (synthesis)
- The text gives the first one-hot U-Net as "63 million" parameters in Results but reports its score as "(66 million)", while Methods assign 66M to the linear-projection variant; the ablation labels are slightly inconsistent. (synthesis)

## Surprising or load-bearing bits

- **One of the clearest cases for DNA-LM pretraining.** Short-sequence classification benchmarks show small gains from pretraining; this harder segmentation task shows a 2× gain over random initialisation, and the authors argue for evaluating DNA LMs on more realistic tasks.
- **Training on longer windows helps shorter windows too** — SegmentNT-30kb beats the 3 kb and 10 kb models even on 3 kb inputs.
- **Resolution versus receptive field trade-off is explicit**: supervised long-range models (Enformer, Borzoi) win on regulatory classes, the base-resolution LM wins on splice sites and gene structure. NTv3 later tries to have both in one backbone. (synthesis)
- **Animal-only multispecies training improves plant annotation**, suggesting element sequence rules transfer across kingdoms.

## Concepts touched

- [[dna-language-model]] — fine-tuning a pretrained NT encoder (not new pretraining) for nucleotide-level segmentation.
- [[genomic-tokenization]] — 6-mer NT tokens are upsampled to per-nucleotide predictions by the U-Net head; Enformer/Borzoi binning (128/32 bp) is what limits splice-site calls.
- [[cis-regulatory-element]] — ENCODE cCRE promoters and enhancers as segmentation targets; best encoded by supervised Enformer/Borzoi features.
- [[sequence-to-function-model]] — Enformer and Borzoi reused as DNA encoders inside the segmentation framework.
- [[jaccard-similarity]] — one of four per-nucleotide segmentation metrics.

## Connections to other sources

- **Base model:** [[dallatorre-2025-nucleotide-transformer]] — SegmentNT fine-tunes NT-Multispecies-v2 (500M); its NT-v2 promoter/enhancer classifiers are also baselines.
- **Successor:** [[boshar-2025-ntv3]] — NTv3 reuses the SegmentNT annotation recipe (extended to 21 labels, 24 species) inside post-training and reports beating SegmentNT at 30 kb and 1 Mb.
- **Alternative encoders:** [[avsec-2021-enformer]], [[linder-2025-borzoi]].
- **Long-context LM alternatives cited:** [[nguyen-2023-hyenadna]], [[schiff-2024-caduceus]]; other LMs cited for pretraining debates: [[ji-2021-dnabert]], [[zhou-2023-dnabert-2]], [[fishman-2025-gena-lm]], [[benegas-2025-gpn-msa]].
- **Large-encoder contrast:** [[ellington-2024-aido-dna]] uses the same NT pretraining data but scales an encoder to 7B at 4 kb. (synthesis)

## Open questions

- Can SegmentNT-style segmentation score variant effects on gene structure (the authors' stated next step), e.g. splice-disrupting or SV-induced annotation changes in cancer genomes?
- How much would cell-type-resolved enhancer labels improve the weak enhancer and CTCF classes?
- Would a combined encoder (base-resolution LM plus supervised long-range features) dominate both families? NTv3 is one answer; a direct ablation is missing. (synthesis)

## Related

- [[dna-language-model]] · [[dallatorre-2025-nucleotide-transformer]] · [[boshar-2025-ntv3]] · [[avsec-2021-enformer]] · [[linder-2025-borzoi]] · [[cis-regulatory-element]] · [[40-Topics/sequence-models-and-foundation-models]]
