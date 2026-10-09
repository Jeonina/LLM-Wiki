---
type: summary
title: "Sanabria et al. 2024 — DNA language model GROVER learns sequence context in the human genome"
source: "[[00-Sources/papers/DNA language model GROVER learns sequence context in the human genome - Nature Machine Intelligence]]"
source_quality: full
source_sha256: "5405ba71c06b0f76278228555dc832ce34fb5ad7eff0c477463c415263439953"
source_kind: paper
author: "Melissa Sanabria, Jonas Hirsch, Pierre M. Joubert, Anna R. Poetsch (corresponding author not marked in the clipping; model hosted by PoetschLab)"
published: 2024-07-23
ingested: 2026-10-08
doi: "10.1038/s42256-024-00872-0"
journal: "Nature Machine Intelligence (volume/pages not given in the clipping)"
tags: [GROVER, dna-language-model, BPE, byte-pair-encoding, tokenization, vocabulary-selection, next-k-mer-prediction, BERT, human-genome, hg19, TF-IDF-baseline, token-embeddings, self-similarity, CTCF, promoter-prediction, repeats, replication-timing, interpretability]
entities: []
concepts: ["[[dna-language-model]]", "[[genomic-tokenization]]", "[[transposable-elements]]", "[[replication-timing]]", "[[chip-seq]]", "[[transcription-factor-motif]]", "[[cpg-island]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[computational-methods]]"]
---

**Citation:** Sanabria et al. (2024) — *DNA language model GROVER learns sequence context in the human genome* — *Nature Machine Intelligence*. [DOI](https://doi.org/10.1038/s42256-024-00872-0)

# Sanabria 2024 — GROVER

> GROVER (Genome Rules Obtained Via Extracted Representations) is a BERT model trained only on the human genome (hg19), whose contribution is how the vocabulary was chosen. The authors build byte-pair-encoding (BPE) vocabularies over 100–5,000 merge cycles, train a model on each, and pick the vocabulary by an intrinsic task — fine-tuning to predict the next k nucleotides (k = 2–6) — rather than by any biological benchmark. Cycle 600 wins (601 tokens, mean length 4.07 nt). The paper then asks what the model learned: token embeddings mostly encode frequency, GC, AG and AC content and length; whole-window (CLS) embeddings separate repeat classes, chromatin states, element orientation and replication timing. GROVER beats NT, DNABERT-2, HyenaDNA and fixed k-mer models on promoter and CTCF-binding tasks designed to reduce frequency cues. The paper also shows that a frequency-only TF-IDF + random-forest baseline explains much of the standard NT and GUE benchmarks.

## Key claims

- **Vocabulary by intrinsic evaluation.** Next-k-mer prediction is independent of tokenisation, vocabulary size and architecture, so it can rank vocabularies without biasing toward a biological task. Models were most accurate between 400 and 800 BPE cycles; cycle 600 was chosen.
- **BPE-600 beats other models on next-k-mer prediction.** For next-6-mers, GROVER reached 2% accuracy, DNABERT-2 0.6% and fixed-k-mer BERT models including NT at most 0.4%. A TF-IDF model reached 1.1%, better than every pre-trained model except GROVER.
- **Masked-token performance.** GROVER's masked-token accuracy was 21% (75% within the top 60 predictions, 10% of the vocabulary). Perplexity was 72 (12% of vocabulary size) vs 65 (25%), 216 (21%) and 1,472 (36%) for 4-, 5- and 6-mer models.
- **What the vocabulary looks like.** 601 tokens; most token frequencies above 100,000 (median about 400,000); lengths from the single G to two 16-mers (A₁₆, T₁₆); 213 five-mers and 224 six-mers. CG never forms a token on its own. 97% of tokens start with A or T (60% expected), because BPE merges frequent A/T first. Per-token, 6-mers were predicted worst; the best tokens (>99% accuracy) were ATTACAGGC and TGTAATCCCAGC, the worst TTTAGG (<1%).
- **What token embeddings encode.** PCs of average trained embeddings correlate with token frequency (PC1, Spearman 0.88), GC content (PC2, −0.96), AG content (PC3, 0.94, read as strand information), length (PC4/PC6, 0.39/0.43) and AC content (PC5, −0.81). Maximum explainable variance was 3.5%, vs 15% for Word2Vec. Apart from repeat-specific tokens, no token maps to a specific functional element.
- **Context is learned at window level.** Self-similarity drops across layers for most tokens, which the authors read as contextual learning; repeat-localised tokens stay self-similar. UMAP of CLS embeddings for 510-token windows (~2.1 kb) separates LINEs, SINEs/Alus, LTRs, satellites and simple repeats, GM12878 ChromHMM states, element orientation relative to tokenisation direction, and K562 replication timing.
- **Fine-tuning tasks built against frequency shortcuts.** Prom300 with token-shuffled negatives: MCC 99.6% vs 79% for the next-best (4-mer model); TF-IDF 5-mer still got 67%. PromScan (1 kb windows from 10 kb around TSSs, unbalanced): 63% vs 52% for NT and 39% for TF-IDF 3-mers. CTCF binding (bound vs unbound JASPAR motif sites, HepG2 ChIP-seq; ~32,000 of ~85,000 motifs bound): 60% vs 59% for DNABERT-2 and 26% for TF-IDF 4-mers.
- **Standard benchmarks are largely frequency-explained.** On the human NT tasks, GROVER's enhancer MCCs (58%, 46%) were best among DNA LMs but close to or below TF-IDF (55%, 57%); NT promoter tasks reached up to 87% MCC from frequency alone. Splice sites were the main exception where DNA LMs clearly beat TF-IDF; there GROVER (94%) was slightly below NT and DNABERT (96%). On GUE tf4, GROVER 75% and DNABERT-2 77% vs NT 61%.

## Methods / evidence

Data: GRCh37/hg19, A/C/G/T only; chromosomes split into windows of 20–510 tokens (50% fixed at 510), 80/20 train/test. Tokeniser: BPE adapted from a published implementation, up to 5,000 cycles; fixed k-mer comparison models use non-overlapping 4-, 5- and 6-mers with identical training. Model: BERT encoder, 12 layers, 768-d embeddings, input up to 510 tokens plus five special tokens; masked-token pre-training on more than 5 million samples on A100 GPUs, batch 64, Adam. Next-k-mer task: chromosome 21, 500,000 sequences, 50 nt input, 4^k classes. Baselines NT, HyenaDNA and DNABERT-2 were fine-tuned from their released weights; DNABERT-2 was excluded from PromScan because of memory. TF-IDF features from k-mer or BPE-600 tokens feed a random forest (100–2,000 trees) as a context-free negative control. NT and GUE scores were partly taken from the source papers and partly re-run on human tasks only. Embedding analyses use PCA, UMAP, hierarchical clustering, Word2Vec (CBOW, 768-d) and per-layer self-similarity over 5,000 embeddings per token. Most numeric results are in figures (images in the clipping); values above are those stated in the text. Code and data: Zenodo 10.5281/zenodo.8373202; model at huggingface.co/PoetschLab/GROVER.

Weight: the paper is careful about shortcut baselines, which is unusual in this literature. Its own fine-tuning tasks are few (three), and two were designed by the authors. (synthesis)

## Limitations

**Authors' own:**
- Trained on one genome; using one species limits training data and "may be limited for smaller genomes", though the authors argue human-specific language rules (e.g. ~12% primate-specific Alu) justify it.
- Standard genome-biology benchmarks are largely predictable from token frequencies, so new tasks that test sequence context independent of frequency are needed.
- Token frequency remains the main feature learned (PC1) even after BPE balancing.
- Beyond repeats, tokens do not map clearly to specific functional elements; functional learning depends on larger context.

**Reviewer notes:**
- The pre-training hyperparameters in Methods look garbled: a learning rate written as "4⁻⁴", a "maximum input length of 50" (the next-k-mer setting) despite 510-token inputs, and masking described as 2.2% of tokens, far below BERT's 15%. Readers should check the code before reusing them. (synthesis)
- Vocabulary selection uses a 50-nt next-k-mer task on one chromosome, which may favour short-range statistics over the long-range context the paper wants to measure. (synthesis)
- Tokenisation is strand- and direction-specific (97% of tokens start with A/T, and embeddings separate elements by orientation), so the model is not reverse-complement symmetric, unlike [[schiff-2024-caduceus]]. (synthesis)

## Surprising or load-bearing bits

- **Frequency-only baselines are strong.** TF-IDF beat every pre-trained model except GROVER at next-6-mer prediction and nearly matched DNA LMs on NT enhancer and promoter tasks. This is a direct warning about how DNA-LM benchmarks are read.
- **The best vocabulary is small and short.** 601 tokens averaging ~4 nt, far fewer than DNABERT-2's 4,096 BPE tokens; the two papers optimise vocabulary for different criteria (intrinsic context prediction vs GUE performance and compute). (synthesis)
- **CG never becomes a token,** which follows from CpG depletion in the genome.
- **Orientation is learned.** CLS embeddings separate LINE and gene orientation and recover the known anticorrelation of LINE orientation with replication direction, from sequence alone.

## Concepts touched

- [[dna-language-model]] — human-only BERT DNA LM with interpretability focus.
- [[genomic-tokenization]] — the paper's core: BPE vocabulary selection by next-k-mer prediction; comparison with fixed k-mers.
- [[transposable-elements]] — repeat-specific tokens and window clusters for LINEs, SINEs/Alus, LTRs.
- [[replication-timing]] — window embeddings separate K562 replication timing and replication direction.
- [[chip-seq]] / [[transcription-factor-motif]] — CTCF bound-vs-unbound motif task from HepG2 ChIP-seq.
- [[cpg-island]] — CG dinucleotide depletion shapes the vocabulary (no CG token).

## Connections to other sources

- Compares against [[ji-2021-dnabert]] (argues overlapping k-mers make DNABERT learn token identity), [[dallatorre-2025-nucleotide-transformer]], [[nguyen-2023-hyenadna]] and [[zhou-2023-dnabert-2]].
- Shares BPE with [[zhou-2023-dnabert-2]] but chooses a much smaller vocabulary by a different criterion and trains on one species rather than 135. (synthesis)
- Its TF-IDF control echoes the point that many short-sequence DNA benchmarks are close to saturation, also visible in the HyenaDNA and Caduceus ablations ([[nguyen-2023-hyenadna]], [[schiff-2024-caduceus]]). (synthesis)

## Open questions

- Would the next-k-mer criterion pick the same vocabulary for other genomes or for multi-species training? (synthesis)
- How much of GROVER's CTCF-binding performance comes from context beyond the motif versus local sequence near it? The authors raise this as open.

## Related

- [[dna-language-model]] · [[genomic-tokenization]] · [[zhou-2023-dnabert-2]] · [[ji-2021-dnabert]] · [[dallatorre-2025-nucleotide-transformer]] · [[transposable-elements]] · [[40-Topics/sequence-models-and-foundation-models]]
