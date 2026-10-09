---
type: summary
title: "Zhang et al. 2025 — DeepGene: An Efficient Foundation Model for Genomics Based on Pan-Genome Graph Transformer"
source: "[[00-Sources/papers/DeepGene- An Efficient Foundation Model for Genomics Based on Pan-Genome Graph Transformer.pdf]]"
source_quality: full
source_sha256: "23e74433246b5927a3cca2a54d86cc120c70846a13e5b4cfeb53ebf7d5103642"
source_kind: paper
author: "Xiang Zhang (corresponding), Mingjie Yang, Xunhang Yin, Yining Qian, Fei Sun"
published: 2025-09-25
ingested: 2026-10-08
updated: 2026-10-08
doi: "10.1109/TCBBIO.2025.3614354"
journal: "IEEE Transactions on Computational Biology and Bioinformatics 22(6):3143–3152 (Nov/Dec 2025)"
tags: [DeepGene, dna-language-model, pan-genome, HPRC, Minigraph, variation-graph, BPE, RoPE, BERT, masked-language-model, length-extrapolation, GUE, efficiency]
entities: []
concepts: ["[[dna-language-model]]", "[[genomic-tokenization]]", "[[structural-variants]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]"]
---

**Citation:** Zhang et al. (2025) — *DeepGene: An Efficient Foundation Model for Genomics Based on Pan-Genome Graph Transformer* — *IEEE Transactions on Computational Biology and Bioinformatics* 22(6):3143–3152. [DOI](https://doi.org/10.1109/TCBBIO.2025.3614354)

# Zhang 2025 — DeepGene

> DeepGene is a small BERT-style DNA language model (85M base, 118M large) **pretrained on the Human Pangenome Reference Consortium draft pangenome graph** of 47 ancestrally diverse individuals, rather than on a single reference genome or on thousands of redundant linear genomes. The Minigraph (rGFA) variation graph is made acyclic, each node is BPE-tokenised, tokens get graph-derived positions (a node's first token is placed relative to its predecessors' positions and lengths), and the graph is cut into 128-token subgraphs for masked-language-model training with rotary position embeddings. The claims are efficiency (best GUE average, 67.79, with far fewer parameters and training tokens than Nucleotide Transformer) and length extrapolation (pretrained on ≤128-token, ~700 bp windows, yet highest F1 at 5 kb promoter detection). The full tables show the GUE "win" is a near-tie at the top and comes almost entirely from yeast and mouse tasks; on human promoter, core-promoter and splice tasks DeepGene is never top-2.

## Key claims

- **Best GUE average, but by a hair.** Averaged over the 28 GUE tasks (Table IV): DeepGene (118M) 67.79, NT-2500M-multi 66.93, DeepGene (85M) 66.92, DNABERT-2 66.80, DNABERT 3-mer 61.62, NT-2500M-1000g 61.41, NT-500M-1000g 58.23, NT-500M-human 55.43. The base model is 0.01 below NT-2500M-multi. The authors' "95% fewer parameters and less than one-fifth of the training data" holds against NT-2500M-multi (2,537M parameters, 300B tokens vs 118M and 39B).
- **Top-2 counts contradict the prose.** The text says DeepGene (118M)'s 13 top-2 finishes are "the most among all models", but Table IV credits NT-2500M-multi with 15 and DNABERT-2 with 12; the base model has 9.
- **Scale and cost (Table IV).** Parameters / relative inference FLOPs (500 bp input) / training tokens / pretraining data: DeepGene 85M / 1.00 / 26B / 5B bp; DeepGene (118M) 118M / 1.41 / 39B / 5B bp; DNABERT-2 117M / 1.33 / 262B / 32.5B bp; NT-2500M-multi 2,537M / 25.86 / 300B / 174B bp; DNABERT 86–89M / ~4.3 / 122B / 3B bp. The 118M model is slightly costlier at inference than DNABERT-2.
- **Strong on yeast and mouse.** DeepGene (118M) is first on 6 of 10 yeast epigenetic-mark tasks (H3K14ac 61.65, H3K4me2 51.67, H3K4me3 57.73, H3K79me3 69.04, H3K9ac 62.62, H4ac 60.45) and second on 2 (H3K36me3, H3K4me1); the largest gains over DNABERT-2 are H3K4me2 (51.67 vs 31.13) and H3K4me3 (57.73 vs 36.27). The base model is first on mouse TF tasks 2 (81.91) and 3 (69.76). DeepGene (118M) is second on COVID variant classification (F1 72.28 vs NT-2500M-multi 73.04).
- **Weak on human regulatory elements.** All five human top-2 finishes come from human TF prediction, where DNABERT-2 wins every task. On promoter detection (all / non-TATA / TATA) DeepGene scores 85.19 / 92.58 / 64.22 (118M: 84.36 / 92.70 / 63.01) vs NT-2500M-multi 91.01 / 94.00 / 79.43; core-promoter "all" is 65.09–65.17 vs DNABERT 3-mer 70.92; splice reconstruction 84.10–84.86 vs NT-2500M-multi 89.35.
- **Pan-genome versus reference mismatch.** The authors attribute the "relatively moderate" human results to GUE being built on the human reference genome while DeepGene is trained on pangenome graphs — a bias they call a double-edged sword that hurts human tasks but helps other species.
- **Length extrapolation (Fig. 4).** On EPDnew human promoter detection at 60, 300, 2,000 and 5,000 bp (F1), mean scores across lengths are DeepGene 81.18, DNABERT-2 80.95, DNABERT 3-mer 74.95, DNABERT 6-mer 74.39 — but DNABERT's means omit 5 kb, where it could not run for compute reasons. DeepGene is lowest of the four models at 60 bp, beats DNABERT by "more than 11%" at 2,000 bp (the figure caption says "more than 10%"), and slightly beats DNABERT-2 at 2,000 and 5,000 bp. Per-length values are given only as bars. RoPE is credited, with the note that it needs no extra parameters, unlike DNABERT-2's ALiBi.
- **Cheap to train.** The base model pretrains in 34 h (20 epochs × ~6,000 s) and the 118M model in 68 h (30 epochs × ~8,000 s) on four 40 GB A100s; H3 fine-tuning (11,971 training sequences of 500 bp, batch 32) takes ~25 s per epoch, with ~3.6 s per evaluation.

## Methods / evidence

Corpus: the HPRC draft human pangenome (47 individuals) in its Minigraph rGFA form; >5 billion bp, >1 billion BPE tokens, ~10 million 128-token subgraphs (≤126 sequence tokens plus [CLS]/[SEP]/[PAD]). Graph processing: rGFA converted to a directed graph using segment orientation; the "small number of cycles" found despite DAG claims are removed with a strongly-connected-components step; node tokens positioned by Eq. 1, which writes the first token of a node as the **minimum** over predecessors of (predecessor start + length). The worked example in Fig. 2(c) instead places the merge node after its longer branch (position 8 rather than 4), i.e. a maximum / longest-path rule, so equation and figure disagree. Tokens on parallel branches share position indices, which is what lets RoPE see the graph. Model: BERT-base (12 layers, 768 hidden, 12 heads, FFN 3,072) with RoPE, 85M, batch 4,096, peak LR 4×10⁻⁴; large variant 16 layers, FFN 3,328, 118M, LRs scaled by 3/4; BERT MLM masking (15%, 80/10/10). Fine-tuning on linear sequences with a [CLS] MLP head, full-parameter; GUE uses MCC (F1 for virus); per-task epochs in Table I (5–10 epochs; mouse TF <2k steps). The base model fine-tunes at batch 32 with a 50-step warm-up; the 118M model at batch 256 with the same step count (so ~8× more epochs) and 20% warm-up. Baselines: DNABERT (3- to 6-mer), DNABERT-2, and four NT variants on GUE; the paper does not say whether baseline scores were re-run or taken from the DNABERT-2 paper. Long promoters: EPDnew hg38, windows −29/+30, −249/+50, −1000/+999, −2000/+2999 around the TSS, negatives built as in GENA-LM, 3:1:1 split (35,518 / 11,839 / 11,839), batch 128, 3 epochs; only DNABERT and DNABERT-2 are compared, because NT could not be fully fine-tuned with the authors' compute.

Weight: a modest-compute IEEE paper whose main benchmark (GUE) is short-sequence classification; single runs, no error bars, and the headline average separates four models by under 1 point. (synthesis)

## Limitations

**Authors' own:**
- BPE vocabulary relies on reference-genome statistics; a tokenizer built from pangenome graphs is needed.
- The graph is sparse, with few haplotypes; more individuals (e.g. 1000 Genomes) should help.
- Human-only data; multi-species pangenomes are future work.
- Length extrapolation alone is not enough for very long sequences; sparse or linear attention would be needed.
- Nucleotide Transformer was excluded from the long-sequence comparison for compute reasons.

**Reviewer notes:** (at most three, each marked `(synthesis)`)
- Pretraining sees the graph but fine-tuning and inference use plain linear sequences, so it is unclear whether the model uses graph structure at all or simply benefits from extra haplotype sequence; there is no ablation against the same model trained on the GRCh38 linear reference. (synthesis)
- The headline average gap (67.79 vs 66.93, with 66.92 and 66.80 just behind) is reported from single runs without seeds or error bars; the two DeepGene variants were fine-tuned with different batch sizes, epoch counts and warm-up; and the prose's "most top-2 finishes" claim is contradicted by its own Table IV. (synthesis)
- The pan-genome is motivated as capturing SNPs, indels and structural variants, but there is no variant-level evaluation (e.g. variant effect or SV-aware tasks) to show the model encodes population variation. (synthesis)

## Surprising or load-bearing bits

- **The only model in this ingest pretrained on a pangenome graph.** Others use linear references, multi-species genomes or 1000 Genomes haplotypes (NT, which the authors say has 98% redundancy). (synthesis on the ingest)
- **Human-only pretraining helps yeast and mouse tasks more than human tasks** — e.g. +20 MCC over DNABERT-2 on yeast H3K4me2/H3K4me3, but 15–16 MCC below NT-2500M-multi on TATA promoters vs NT-2500M-multi. The authors read this as diversity-driven transfer; GUE human-task difficulty or a reference/pangenome mismatch are alternatives. (synthesis)
- **Graph positions for linear transformers**: assigning each token a position derived from the DAG lets a standard RoPE transformer consume branching sequence without a graph neural network.
- **Efficiency is in data, not inference.** DeepGene uses 39B training tokens vs DNABERT-2's 262B, but its 118M variant's inference FLOPs (1.41) are slightly above DNABERT-2's (1.33). (synthesis)

## Concepts touched

- [[dna-language-model]] — a compact BERT-style MLM trained on a human pangenome graph; argues for data diversity over scale, with a GUE average (67.79) narrowly above NT-2500M-multi.
- [[genomic-tokenization]] — BPE applied within variation-graph nodes, with graph-derived positions; authors call for pangenome-native tokenizers.
- [[structural-variants]] — the pangenome is motivated by its capture of SNPs, indels and SVs, but their effect on learned representations is not tested.

## Connections to other sources

- Built and benchmarked on the DNABERT line: [[ji-2021-dnabert]], [[zhou-2023-dnabert-2]] (GUE benchmark, BPE, ALiBi); DNABERT-2 averages 66.80 here and wins all five human TF tasks.
- Compared with Nucleotide Transformer variants: [[dallatorre-2025-nucleotide-transformer]]; NT-2500M-multi stays best on human promoter, splice and COVID tasks.
- Long-promoter negatives follow the GENA-LM recipe: [[fishman-2025-gena-lm]].
- Opposite design choice — scale parameters to 7B on the NT multi-species data — is [[ellington-2024-aido-dna]], which beats DNABERT-2 by a much wider GUE margin (73.3 average). (synthesis)

## Open questions

- Does pangenome pretraining help variant-centric tasks (pathogenicity, eQTL, SV impact) more than GUE-style element classification? (synthesis)
- Would the same recipe with a pangenome-derived tokenizer and more haplotypes close the gap on human promoter and splice tasks?
- Which positioning rule (Eq. 1's minimum or Fig. 2(c)'s longest branch) does the released code implement? (synthesis)

## Related

- [[dna-language-model]] · [[genomic-tokenization]] · [[zhou-2023-dnabert-2]] · [[ji-2021-dnabert]] · [[dallatorre-2025-nucleotide-transformer]] · [[40-Topics/sequence-models-and-foundation-models]]
