---
type: summary
title: "Vishniakov et al. 2025 — Gene42: Long-Range Genomic Foundation Model With Dense Attention"
source: "[[00-Sources/papers/Gene42- Long-Range Genomic Foundation Model With Dense Attention.pdf]]"
source_quality: full
source_sha256: "6fabd07ecfe314af8ae2a333a480270a26c703b3d71fdc4bc72b73e53f5b8f8b"
source_kind: paper
author: "Kirill Vishniakov, Boulbaba Ben Amor (co-first; corresponding), Engin Tekin, Nancy A. ElNaker, Karthik Viswanathan, Aleksandr Medvedev, … Shadab Khan"
published: 2025-03-20
ingested: 2026-10-08
doi: "10.48550/arXiv.2503.16565"
journal: "arXiv preprint (arXiv:2503.16565v1, cs.LG)"
tags: [Gene42, DNA-language-model, decoder-only, LLaMA, dense-attention, long-context, RoPE, continuous-pretraining, character-tokenization, Cerebras, perplexity, biotype-classification, ClinVar, DeepSEA, species-classification, M42, Inception]
entities: []
concepts: ["[[dna-language-model]]", "[[genomic-tokenization]]", "[[variant-effect-prediction]]", "[[chromatin-accessibility]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[computational-methods]]"]
---

**Citation:** Vishniakov, Ben Amor et al. (2025) — *Gene42: Long-Range Genomic Foundation Model With Dense Attention* — arXiv preprint. [DOI](https://doi.org/10.48550/arXiv.2503.16565)

# Vishniakov 2025 — Gene42

> Gene42 (M42, Inception Institute of AI and Cerebras, Abu Dhabi) is a family of decoder-only, LLaMA-style DNA language models that keep **full dense self-attention** and single-nucleotide (character) tokens, and reach a **192,000-bp context** by continued pre-training. A 500M (Gene42-B) and a 1.1B (Gene42-L) model are first trained on 4,096-bp GRCh38 sequences on a Cerebras CS-2. Gene42-L is then extended stepwise (8k → 16k → 32k → 65k → 131k → 192k) by raising the RoPE base frequency. The paper argues that dense attention, not only state-space or convolutional operators, can handle genome-scale context, and reports top or near-top scores on Genomic Benchmarks, the NT benchmark, DeepSEA (TF and DHS), a ClinVar pathogenicity task and HyenaDNA's species classification.

## Key claims

- **Long-context perplexity.** On 1% held-out GRCh38, models trained only at short context (4k–32k) show rising perplexity on long inputs. Gene42-L-65k and -192k reach a best perplexity of 1.61 (reconstruction accuracy 0.789) at 65 kb. The 192k model gives 1.78 (0.723) at 131 kb and 1.85 (0.70) at 192 kb. The authors compare this with HyenaDNA's reported 2.9–3 at 100 kb–1 Mb, and note that the 65-kb model is best at next-base prediction.
- **Biotype classification from frozen embeddings (Ensembl, XGBoost, F1).** Gene42-L-65k 0.782, -32k 0.771, Gene42-B 0.763, against NT 2.5B 0.759, HyenaDNA-medium 0.709, NT 50M 0.681 and DNABERT-2 0.654. Longer Gene42 context gives higher F1.
- **Genomic Benchmarks (8 tasks, top-1 accuracy).** Gene42-B trained on human + multispecies with a 192k-bp listed context averages 89.3% against HyenaDNA 88.5% and Caduceus 86.5%. The 1.1B model trained on human only averages 88.1% (32k) and 86.4% (192k), so the largest, longest model is not the best here. The text says Gene42 is state of the art on 5 of 8 datasets, and quotes 95.3% on coding-vs-intergenomic against DNABERT 92.5% and HyenaDNA 91.3%.
- **NT benchmark (18 tasks).** NT Multispecies 2.5B is best on 8 datasets (including all splice tasks), Gene42-B (500M, 4 kb, human only) on 8, and HyenaDNA-1k on 2. Histone-mark MCC averages: Gene42-B 0.627, HyenaDNA-1k 0.615, NT 2.5B 0.573; Gene42-L-192k falls to 0.465. All baseline numbers are copied from the NT leaderboard.
- **ClinVar pathogenicity (64.5k train / 8.8k test, 1-kb inputs).** Gene42-L fine-tuned reaches AUC-ROC 0.931 (1,000 steps) and 0.925 (2,000 steps), with accuracy 81.4% and 85.2%. Baselines copied from an earlier study by one of the authors: GENA-LM 100M AUC 0.892 and accuracy 90.6%, NT 500M accuracy 78.2%, HyenaDNA AUC 0.608. Zero-shot Gene42-B gives AUC 0.513 (chance). A random forest on Gene42 embeddings gives AUC 0.915.
- **DeepSEA chromatin profiles (919 labels, median AUC).** At 1 kb, Gene42-L gives TF 0.967 and DHS 0.934, slightly above HyenaDNA (0.964, 0.930) and DeepSEA (0.958, 0.923). Histone marks are worse: 0.839 against HyenaDNA 0.863 and DeepSEA 0.856. At 8 kb, Gene42 HM (0.836) is well below BigBird (0.887) and HyenaDNA (0.893). Fine-tuning all layers beats head-only fine-tuning by about 20–25 AUC points (e.g., TF 96.7 vs 73.1).
- **Species classification (HyenaDNA five-mammal task).** Gene42-L reaches 66.9% at 1 kb (HyenaDNA 61.1%, RMT + GENA-LM 61.4%) and 99.5% at 32 kb (HyenaDNA 93.4%, RMT + GENA-LM 99.2%). HyenaDNA reaches 97.9% at 250 kb, where a dense transformer was reported as infeasible.

## Methods / evidence

Architecture: LLaMA-2-style decoder with RoPE, SwiGLU and RMSNorm. Gene42-B: 16 layers, hidden 1,408, 500M parameters. Gene42-L: 24 layers, hidden 2,048, 32 heads, 1.1B parameters. Tokenization: one token per nucleotide. Pre-training data: GRCh38 split 99/1, 3.5M sequences of 4,096 tokens (14.5B tokens); an HRG+S variant adds 8.1B tokens from 14 vertebrate genomes taken from the GENA-LM multispecies list. Optimiser AdamW, cosine decay; context extension raises the RoPE base frequency from 10k to 15M, with few iterations per stage (e.g., 200 cosine iterations for the 65k and 192k stages). Fine-tuning: full-model AdamW, LR 1e-4, 2–3 epochs. Models on HuggingFace (`inceptionai`).

Weight: a benchmark-driven preprint. Almost all baseline numbers come from earlier papers or leaderboards, not reruns under matched protocols. No ablation isolates dense attention, model size or multispecies data, and the long-context models are not tested on a task that needs >32 kb. The "bold = best" markings in Tables 3–6 do not survive the text extraction, so claims of "best" rely on the paper's prose.

## Limitations

**Authors' own:**
- Dense attention carries quadratic compute and memory cost; HyenaDNA's Hyena operator is more efficient, with a performance trade-off.
- The 192k model's perplexity at 131–192 kb is higher than the 65k model's best; the authors think larger models may be needed.

**Reviewer notes:**
- The longest models do worse on short tasks: Gene42-L-192k drops to 86.4% on Genomic Benchmarks and 0.465 histone MCC on NT, so extending context appears to cost short-range quality, which the paper does not discuss. (synthesis)
- The ClinVar comparison is mixed rather than a clear win: GENA-LM 100M has higher accuracy (90.6% vs 85.2%) while Gene42 has higher AUC, and the baselines come from a different study. (synthesis)
- The appendix "multi-species" table lists 14 genomes whose names all start with "A" (fish, birds, panda, anole), which looks like the first 14 alphabetical entries of the GENA-LM list rather than a designed panel. (synthesis)

## Surprising or load-bearing bits

- **Dense attention at 192 kb is feasible** with RoPE base-frequency scaling and a wafer-scale accelerator, which removes "attention can't go long" as the reason to use state-space models in genomics. Whether it is *better* than SSMs at long range is not shown here. (synthesis)
- **Histone marks remain the weak spot** for this nucleotide-level decoder on DeepSEA, while TF and DHS are slightly ahead of other models, the reverse of GENA-LM, whose long context mainly helped histone marks. (synthesis)
- **Zero-shot pathogenicity was chance** (AUC 0.513); every useful score needed supervised fine-tuning or a classifier on embeddings.

## Concepts touched

- [[dna-language-model]] — decoder-only, dense-attention, long-context DNA LM.
- [[genomic-tokenization]] — single-nucleotide character tokens, following HyenaDNA, to keep SNP-level resolution.
- [[variant-effect-prediction]] — supervised ClinVar pathogenicity classification; zero-shot near chance.
- [[chromatin-accessibility]] — DeepSEA DHS prediction as a benchmark target.

## Connections to other sources

- Main comparators: [[nguyen-2023-hyenadna]] (character tokenization and the species benchmark), [[schiff-2024-caduceus]], [[dallatorre-2025-nucleotide-transformer]] (NT benchmark), [[zhou-2023-dnabert-2]], [[fishman-2025-gena-lm]] (multispecies data source and RMT species result).
- DeepSEA labels from [[zhou-2015-deepsea]].
- Co-author Aleksandr Medvedev and the M42 affiliation recur in [[medvedev-2025-biofm]]. (synthesis)
- Other long-context designs in this ingest: [[ma-2025-hybridna]], [[duan-2025-janusdna]], [[li-2026-generator]]. (synthesis)

## Open questions

- Does the 192k model beat a 32k model on any task that truly needs >100 kb, such as expression or enhancer–promoter prediction? None is tested. (synthesis)
- How much of the short-task drop in the 192k model comes from base-frequency scaling versus too few continued-pretraining steps? (synthesis)
- Is the published version (if any) different from this v1 preprint? (synthesis)

## Related

- [[dna-language-model]] · [[genomic-tokenization]] · [[nguyen-2023-hyenadna]] · [[fishman-2025-gena-lm]] · [[40-Topics/sequence-models-and-foundation-models]]
