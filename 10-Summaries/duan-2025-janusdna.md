---
type: summary
title: "Duan et al. 2025 — JanusDNA: A Powerful Bi-directional Hybrid DNA Foundation Model"
source: "[[00-Sources/papers/JanusDNA- A Powerful Bi-directional Hybrid DNA Foundation Model.pdf]]"
source_quality: full
source_sha256: "d1db3f7433fd495537ed5c89f292b0e96a26192e4c5596a7fe23fb33d3390d42"
source_kind: paper
author: "Qihao Duan, Bingding Huang, Zhenqiao Song, Irina Lehmann, Lei Gu, Roland Eils, … Benjamin Wild (corresponding: Lehmann, Gu, Eils, Wild)"
published: 2025-10-28
ingested: 2026-10-08
doi: "10.48550/arXiv.2505.17257"
journal: "arXiv preprint (arXiv:2505.17257v4, cs.LG; under review)"
tags: [JanusDNA, DNA-language-model, bidirectional, Janus-modeling, Mamba, mixture-of-experts, MoE, FlexAttention, hybrid-architecture, long-context, single-nucleotide, reverse-complement, eQTL, DNALongBench, Genomic-Benchmarks, NT-benchmark, Charite, BIH]
entities: []
concepts: ["[[dna-language-model]]", "[[genomic-tokenization]]", "[[variant-effect-prediction]]", "[[transcription-factor-motif]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[histone-modifications]]", "[[computational-methods]]"]
---

**Citation:** Duan et al. (2025) — *JanusDNA: A Powerful Bi-directional Hybrid DNA Foundation Model* — arXiv preprint (v4). [DOI](https://doi.org/10.48550/arXiv.2505.17257)

# Duan 2025 — JanusDNA

> JanusDNA (Berlin Institute of Health at Charité, MPI Heart and Lung Research, with Shenzhen and CMU co-authors) proposes **Janus modelling**, a pre-training objective that predicts *every* token from both its left and right context. Two independent causal stacks of Mamba + FFN/MoE layers read the sequence left-to-right and right-to-left; a single FlexAttention layer with a hand-built mask then fuses them so that the prediction for position *t* sees only forward states before *t* and backward states after *t*. This gives the full-token loss of autoregressive training with the bidirectional context of masked language modelling. Pre-trained only on the human reference genome at single-nucleotide resolution, small JanusDNA models (0.4–7.7M activated parameters) lead most of the NT benchmark and eight of nine DNALongBench eQTL tissues against size-matched Caduceus and a 252M Enformer.

## Key claims

- **Janus objective learns faster than MLM.** In a one-layer bidirectional Mamba + FlexAttention model trained 10k steps on 131,072-token hg38 windows (batch 1), Janus modelling gave higher last-token prediction accuracy than the same model trained with 15% masking, at three hidden sizes (Fig. 3; values only in figure). Janus pre-training ran about twice as fast (~27 min per 1,000 steps).
- **Janus vs causal at matched size (Tables 6–7).** On middle-token prediction after 10k steps, Janus reached 0.456 / 0.482 / 0.488 (hidden 32 / 64 / 128) against causal 0.443 / 0.456 / 0.465. Janus was also slightly better on last-token prediction (0.491 vs 0.484 at the largest size), which the authors read as richer representations from bidirectional training.
- **Genomic Benchmarks (8 tasks).** Best on 3 of 8 (e.g., human non-TATA promoters 0.957 vs ConvNova 0.951 and Caduceus 0.946), close on the rest. The authors call this benchmark saturated.
- **NT benchmark (18 tasks, 10-fold CV).** JanusDNA-MLP (~2.0M activated parameters) is best on 12 of 18, mainly histone marks: H3K4me3 MCC 0.688 vs ConvNova 0.566 and NT-v2 500M 0.410; H3K14ac 0.729 vs 0.644 and 0.551. NT-v2 still wins promoters (0.976 vs 0.970) and splice sites (all 0.983 vs 0.967; donor 0.985 vs 0.948), which the authors attribute to training-data scale and diversity.
- **Long-range eQTL (DNALongBench, AUROC).** JanusDNA-MLP without mid-attention (7.7M activated) beats Caduceus-PH (7.7M) and Enformer (252M, numbers from DNALongBench) in 8 of 9 tissues, e.g., nerve tibial 0.914 vs 0.842 and 0.683; muscle skeletal 0.864 vs 0.789 and 0.621. Adipose subcutaneous is closer (0.769 vs Caduceus 0.759, Enformer 0.736).
- **Design ablations.** MoE lowered training perplexity; a mid-stack attention layer helped only at hidden size 32 and was neutral or harmful at 72–128, so the default omits it. An MLP after fusion improved NT and eQTL scores. Post-hoc reverse-complement averaging improved histone, enhancer and promoter tasks but **hurt splice sites** (e.g., donors 0.921 → 0.874), consistent with splicing being strand-specific.
- **Cross-species check.** On mouse TF binding (GUE), JanusDNA-72 (2.0M activated) pre-trained on human only scored 0.619 / 0.850 / 0.875 / 0.843 / 0.502 MCC on the five tasks, comparable to DNABERT-2 (117M).
- **Scale claim.** The hybrid can process up to 1 Mbp at single-nucleotide resolution on one 80-GB GPU (stated, not benchmarked in the paper).

## Methods / evidence

Architecture: two independent 8-layer stacks, each layer one Mamba block plus FFN, with MoE (16 experts, top-routed, auxiliary load-balancing loss coefficient 0.2) replacing half the FFNs; fusion by FlexAttention (4 heads) over the concatenated 2T forward/backward states with a four-case mask (Eq. 6); same-token representations are summed after fusion. Pre-training: hg38 only (to isolate architecture), single-nucleotide tokens, AdamW, cosine schedule; 1,024-bp models (hidden 32 or 72) for 10k steps and a 131,072-bp model (hidden 144; 7.66M activated / 35.5M total parameters) for 50k steps; about 3–9 h on H800 GPUs. Benchmarks follow the Caduceus protocol and copy its baseline numbers for Genomic Benchmarks and NT; Caduceus-PH was re-fine-tuned for eQTL; Enformer eQTL numbers come from DNALongBench. eQTL fine-tuning: 3 epochs, one run per tissue.

Weight: a clever objective with a careful matched-parameter design, but the headline comparisons are against very small baselines (Caduceus, HyenaDNA, ConvNova at ~0.4–2M parameters) or copied numbers. The "250× more activated parameters" claim compares against Enformer and NT, which were trained for different purposes and data. Several result figures (Figs 3, 5, 6) are images in the extracted text.

## Limitations

**Authors' own:**
- Pre-training is restricted to the human reference genome; variants (1000 Genomes) and other species are future work.
- No multimodal input (chromatin accessibility, histone marks, single-cell transcriptomes), so cell-type-specific regulation is out of scope.
- No experimental validation of predictions; limited compute meant single eQTL runs per tissue.
- Reverse-complement averaging can mislead for strand-specific elements such as splice sites.

**Reviewer notes:**
- The DNALongBench text says eQTL inputs are 450,000 bp, while the model was pre-trained at 131k and the Caduceus-PH weights linked in the appendix are a `seqlen-1k` checkpoint, although the main text says the 131k one was used; how much context each model actually saw is unclear. (synthesis)
- Pre-training data is called HG38 but the cited reference [32] is GRCh37. (synthesis)
- Enformer eQTL numbers are taken from another paper and Enformer is a supervised track predictor, not a fine-tuned LM, so "beats the expert model" mixes evaluation regimes. (synthesis)

## Surprising or load-bearing bits

- **Every-token bidirectional loss without masking.** The attention mask lets one fusion layer produce a leakage-free prediction for each position from both directions, which removes the 15%-token inefficiency of BERT-style training. This is the reusable idea. (synthesis)
- **Tiny models, big histone-mark gains.** A 2M-activated-parameter model beats a 500M NT-v2 by >0.1 MCC on several histone marks, which suggests NT-benchmark histone tasks reward architecture and single-nucleotide resolution more than scale. (synthesis)
- **RC equivariance is task-dependent**: averaging forward and reverse-complement embeddings helps symmetric regulatory tasks and hurts splicing.

## Concepts touched

- [[dna-language-model]] — bidirectional hybrid Mamba/MoE/attention model with a new full-token objective.
- [[genomic-tokenization]] — single-nucleotide tokens chosen for SNP-level resolution.
- [[variant-effect-prediction]] — DNALongBench eQTL classification across nine GTEx tissues.
- [[transcription-factor-motif]] — reverse-complement handling for non-palindromic motifs (GATA/TATC example); mouse TF-binding check.

## Connections to other sources

- Built on and compared with [[schiff-2024-caduceus]] (protocol, baselines, bidirectional Mamba) and [[nguyen-2023-hyenadna]] (unidirectional SSM).
- Baselines also include [[zhou-2023-dnabert-2]], [[dallatorre-2025-nucleotide-transformer]], [[ji-2021-dnabert]] and [[avsec-2021-enformer]] (eQTL "expert model").
- Cites [[ma-2025-hybridna]] as a unidirectional Transformer–Mamba2 hybrid; JanusDNA's answer to the same causal-context problem is bidirectional training rather than HybriDNA's echo embeddings. (synthesis)

## Open questions

- Does Janus modelling keep its advantage at 100M+ parameters and on multispecies data, where MLM baselines are strongest? (synthesis)
- Can a Janus-trained model still generate sequences, or does the bidirectional objective give up the generative use that causal models (HybriDNA, GENERator) keep? (synthesis)
- The 1-Mbp capacity claim is not exercised by any benchmark here.

## Related

- [[dna-language-model]] · [[genomic-tokenization]] · [[schiff-2024-caduceus]] · [[ma-2025-hybridna]] · [[avsec-2021-enformer]] · [[40-Topics/sequence-models-and-foundation-models]]
