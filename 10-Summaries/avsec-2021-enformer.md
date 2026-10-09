---
type: summary
title: "Avsec et al. 2021 — Effective gene expression prediction from sequence by integrating long-range interactions"
source: "[[00-Sources/papers/Effective gene expression prediction from sequence by integrating long-range interactions]]"
source_quality: full
source_sha256: "281767d4cbe8def73227897395c6252843eac7256c40f560db9d6ed742cdabda"
source_kind: paper
author: "Žiga Avsec, Vikram Agarwal, Daniel Visentin, Joseph R. Ledsam, Agnieszka Grabska-Barwinska, Kyle R. Taylor, … , Pushmeet Kohli, David R. Kelley"
published: 2021-10-04
ingested: 2026-10-08
doi: "10.1038/s41592-021-01252-x"
journal: "Nature Methods 18:1196–1203"
tags: [Enformer, sequence-to-function, transformer, self-attention, long-range-regulation, CAGE, Basenji2, ExPecto, enhancer-promoter, eQTL, GTEx, MPRA, CAGI5, variant-effect-prediction, DeepMind, Calico]
entities: []
concepts: ["[[sequence-to-function-model]]", "[[variant-effect-prediction]]", "[[convolutional-neural-network]]", "[[cis-regulatory-element]]", "[[topologically-associating-domain]]", "[[transcription-factor-motif]]", "[[chip-seq]]", "[[dnase-seq]]", "[[chromatin-accessibility]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[computational-methods]]"]
---

**Citation:** Avsec et al. (2021) — *Effective gene expression prediction from sequence by integrating long-range interactions* — *Nature Methods*. [DOI](https://doi.org/10.1038/s41592-021-01252-x)

# Avsec 2021 — Enformer

> Enformer (enhancer + transformer) is a supervised [[sequence-to-function-model]] that takes 196,608 bp of one-hot DNA and predicts 5,313 human and 1,643 mouse genomic tracks (CAGE, DNase/ATAC, histone and TF ChIP-seq) at 128-bp resolution over the central 114,688 bp. It keeps the Basenji2 recipe (same targets, same splits, Poisson loss) but replaces the dilated-convolution tower with 11 transformer blocks, so each 128-bp bin can draw on elements up to ~100 kb away instead of ~20 kb. That raises mean CAGE-at-TSS correlation across genes from 0.81 to 0.85 and improves enhancer–gene prioritisation, eQTL concordance and MPRA variant-effect prediction, all from sequence alone.

## Key claims

- **Long receptive field matters.** Basenji2 and ExPecto see at most ~20 kb from the TSS. Enformer reaches ~100 kb, which the authors estimate raises the share of high-confidence enhancer–gene pairs within reach from 47% to 84%.
- **Expression accuracy.** Mean CAGE-at-TSS Pearson r across held-out protein-coding genes rose from 0.81 (Basenji2) to 0.85. The authors put replicate-level accuracy at 0.94, so this closes about one-third of the gap. Gains held across all four track types and were largest for CAGE. Against ExPecto on RNA-seq, Spearman r was 0.850 vs 0.812 across genes and 0.451 vs 0.368 across tissues.
- **Attention beats dilated convolution.** Swapping attention for dilated convolutions lost accuracy at all model sizes and data sizes tested. Restricting attention to Basenji2's receptive field also caused a large drop. Custom relative positional encodings (exponential, central-mask, gamma; symmetric plus asymmetric) beat sin/cos and absolute encodings.
- **Enhancer prioritisation from sequence.** On K562 CRISPRi enhancer–gene pairs (Gasperini 2019, Fulco 2019; >10,000 candidate enhancers), Enformer contribution scores beat Basenji2 and were comparable to, sometimes better than, the ABC score, which uses measured H3K27ac and Hi-C. Cell-type-specific scores beat cell-type-agnostic ones.
- **Learned insulation.** Averaged attention at 1,500 TAD boundaries showed more attention to boundaries and less across them. TF-MoDISco found the CTCF motif among contribution-score motifs with both positive and negative signs.
- **eQTLs.** For 379 of 648 CAGE datasets the maximum SLDP Z-score against GTEx increased (mean 6.3 → 6.9). On fine-mapped GTEx v8 eQTLs (PIP > 0.9 vs PIP < 0.01), random-forest classifiers on Enformer features beat Basenji2 in 47 of 48 tissues (mean auROC 0.729 → 0.747), at all TSS distances.
- **MPRA.** On the CAGI5 saturation-mutagenesis set, lasso on Enformer features had the best mean correlation of seven competition entries and beat the winning team (one-sided P = 0.002). Training-free Enformer scores performed comparably to the lasso model.

## Methods / evidence

Architecture: 7 convolutional blocks with attention pooling (196,608 bp → 1,536 positions of 128 bp), 11 transformer blocks (8 heads, key/query 64, value 192, Transformer-XL-style relative positional encodings), cropping of 320 positions per side, and two organism-specific output heads. Compared with Basenji2 it uses attention pooling instead of max pooling, twice the channels (1,536) and a 1.5× longer input. Training: human and mouse jointly, alternating batches, 34,021 human and 29,295 mouse training sequences, homology-aware 1 Mb split, 64 TPU v3 cores for 150,000 steps (~3 days), then 30,000 steps of human fine-tuning. Augmentation: ±3 bp shifts and reverse complement, also used at test time. Variant scoring: reference minus alternative prediction, summed across the sequence, averaged over strand and shifts. Code and the pretrained model are public (Apache 2.0, TF-Hub), along with precomputed scores for 1000 Genomes variants with MAF > 0.5%, compressed to 20 PCA scores (auROC 0.743 vs 0.747 with all features).

Weight: a strong, well-controlled comparison against Basenji2 on identical data, with ablations on attention, receptive field and positional encodings. Most comparisons are to Basenji2 and ExPecto, and many numbers sit in figures that are images in the clipping; the summary uses only values stated in the text and captions.

## Limitations

**Authors' own:**
- The model predicts only for cell types and assays in its training data and cannot generalise to new cell types or assays.
- Small functional datasets (CRISPR perturbation, MPRA) were used only for evaluation, not training.
- 128-bp bins were chosen because finer resolution would lengthen the sequence entering quadratic-cost attention and was intractable on available hardware.
- Both Enformer and Basenji2 struggle to predict eQTL sign for variants beyond the promoter (TSS distance > 1,000 bp) (Extended Data Fig. 10).

**Reviewer notes:**
- Gains on the headline metric are modest in absolute terms (0.81 → 0.85; auROC 0.729 → 0.747), and most expression gains come from across-gene correlation, which promoter features largely drive. (synthesis)
- Enhancer–gene evaluation uses K562 only, a cell line heavily represented in the training tracks, so the ABC-comparable result may not hold in less profiled cell types. (synthesis)
- Attention maps at TAD boundaries are averaged over heads and layers; they show correlation with insulation, not that the model uses insulation causally. (synthesis)

## Surprising or load-bearing bits

- A model given only DNA matched an enhancer-linking method (ABC) that takes measured H3K27ac and Hi-C as input, in the cell line where both were evaluated.
- The authors stress three advantages of sequence-only variant scoring: signed effects, no reliance on conservation, and the ability to score arbitrary synthetic sequences.
- Enformer set the template (conv stem + transformer + multi-track Poisson heads on long windows) that Borzoi and AlphaGenome later extend. (synthesis)
- For scDNA work, a model like this is a way to score somatic noncoding variants found in single cells, but only in the bulk cell types it was trained on. (synthesis)

## Concepts touched

- [[sequence-to-function-model]] — the reference long-range supervised model; attention replaces dilated convolutions.
- [[variant-effect-prediction]] — SLDP on GTEx eQTLs, fine-mapped eQTL classification, CAGI5 MPRA.
- [[convolutional-neural-network]] — retained as a stem; dilated-CNN ablation shows the gain comes from attention.
- [[cis-regulatory-element]] — enhancer–gene prioritisation from contribution scores.
- [[topologically-associating-domain]] — attention is reduced across TAD boundaries; CTCF motifs at boundaries.
- [[transcription-factor-motif]] — TF-MoDISco motifs; SP1 motif disruption at rs11644125 near *NLRC5*.
- [[chip-seq]] / [[dnase-seq]] / [[chromatin-accessibility]] — training targets.

## Connections to other sources

- Direct predecessors: [[kelley-2018-basenji]] (Basenji; the Basenji2 recipe it reuses), [[zhou-2018-expecto]] (ExPecto, beaten on RNA-seq), [[zhou-2015-deepsea]] (DeepSEA Beluga, beaten on SLDP), [[kelley-2016-basset]].
- Uses 3D-genome predictions from [[fudenberg-2020-akita]] (TAD boundaries) and names combination with such models as future work; [[zhou-2022-orca]] pursues that axis.
- Extended by [[linder-2025-borzoi]] (RNA-seq coverage, 32-bp bins, 524 kb) and [[avsec-2026-alphagenome]] (1 Mb, base resolution, multimodal).
- Enformer-derived models in this ingest: [[hingerl-2025-scooby]] and [[lal-2026-decima]] (single-cell outputs) and [[lin-2026-epinformer]] (which benchmarks against Enformer).
- TAD biology it echoes: [[dixon-2012-tads]]. H3K27ac as an enhancer mark: [[creyghton-2010-h3k27ac-enhancers]].

## Open questions

- How much of the remaining gap to replicate accuracy (0.85 vs 0.94) is reachable with sequence alone, versus cell-state information that sequence cannot carry? (synthesis)
- Distal variant effects remain poorly predicted in sign even with a 100 kb reach; is the bottleneck the receptive field, training data or the bin resolution? (synthesis)
- Generalising to unseen cell types was explicitly out of scope; later single-cell heads (scooby, Decima) try to address it.

## Related

- [[sequence-to-function-model]] · [[variant-effect-prediction]] · [[kelley-2018-basenji]] · [[linder-2025-borzoi]] · [[avsec-2026-alphagenome]] · [[40-Topics/sequence-models-and-foundation-models]]
