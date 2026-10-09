---
type: summary
title: "Medvedev et al. 2025 — BioToken and BioFM: Biologically-Informed Tokenization Enables Accurate and Efficient Genomic Foundation Models"
source: "[[00-Sources/papers/BioToken and BioFM – Biologically-Informed Tokenization Enables Accurate and Efficient Genomic Foundation Models.pdf]]"
source_quality: full
source_sha256: "7d9156564579fb6993659b5f794e8acda9817772a1c442045046fe333476fef4"
source_kind: paper
author: "Aleksandr Medvedev (corresponding), Karthik Viswanathan, Praveenkumar Kanithi (corresponding), Kirill Vishniakov, Prateek Munjal, Clément Christophe, … Shadab Khan (corresponding)"
published: 2025-11-03
ingested: 2026-10-08
doi: "10.1101/2025.03.27.645711"
journal: "bioRxiv preprint (first posted 2025-03-27; clipped text = version posted 2025-11-03)"
tags: [BioToken, BioFM, M42, DNA-language-model, tokenization, variant-tokens, annotation-tokens, decoder-only, Mistral, 1000-Genomes, personal-genomes, variant-effect-prediction, eQTL, sQTL, meQTL, Enformer, SpliceTransformer, Evo2, BEND, GLRB, TraitGym, Dart-Eval, promoter-generation, preprint]
entities: []
concepts: ["[[dna-language-model]]", "[[genomic-tokenization]]", "[[variant-effect-prediction]]", "[[sequence-to-function-model]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[dna-methylation]]", "[[computational-methods]]"]
---

**Citation:** Medvedev et al. (2025) — *BioToken and BioFM – Biologically-Informed Tokenization Enables Accurate and Efficient Genomic Foundation Models* — *bioRxiv preprint*. [DOI](https://doi.org/10.1101/2025.03.27.645711)

# Medvedev 2025 — BioToken / BioFM

> BioToken changes what goes *into* a [[dna-language-model]]. Instead of the reference genome alone, BioToken writes real personal genomes: each sequence has one of 50 phased 1000 Genomes individuals' variants applied, alternate alleles become separate **variant tokens** (Ǎ, Ť, Ǧ, Č), and GENCODE v38 **annotation tokens** mark transcript, exon and CDS starts and ends inline. BioFM is a 265 M-parameter decoder-only Mistral-style model (23 layers, 6,144-token context) trained by next-token prediction on 333 B such tokens. With frozen embeddings and a linear probe, it reports the best average AUROC on a new 8-task Variant Benchmark (0.780 vs 0.727 for NT-500M-v2), beats Enformer on expression and eQTL and SpliceTransformer on sQTL, and beats Evo2-7B on 5 of 8 tasks with about 1/100 of the pretraining compute.

## Key claims

- **Variant Benchmark (linear probe, 11 chromosome-split folds).** BioFM's overall AUROC is 0.780, then NT-500M-v2-MS 0.727, Evo2-7B 0.726, Caduceus 0.705, HyenaDNA 0.700, Evo2-1B 0.691 and NT-500M-1000G 0.674. It is best on 6 of 8 tasks, with clear margins on common vs synthetic-rare variants (0.746 vs 0.69) and expression (0.786 vs 0.74). It does not beat CADD, AlphaMissense or GPN-MSA on pathogenicity, and no other GFM did either in their tests.
- **Against specialized models.** Linear probing at matched 12 kb context matches Enformer on expression. After LoRA fine-tuning, BioFM beats Enformer at 98 kb context (median AUROC 0.812 vs 0.782; Wilcoxon p = 0.002 across 11 folds). On Borzoi's eQTLs it scores 0.697 vs Enformer's 0.674. On Borzoi's sQTLs it scores a median tissue AUROC of 0.676 vs SpliceTransformer's 0.629 and wins in every tissue cluster.
- **Ablation: annotations matter most.** A nucleotide-only model of the same size and compute (ACGT-265M) does clearly worse on all four external variant benchmarks. Removing annotation or variant tokens at test time, or training without them, lowers AUROC, most for coding pathogenicity and splicing. The authors call annotations "the primary factor".
- **Other benchmarks.** GLRB: BioFM's linear probe (mean AUROC 0.793) beats NT-500M-v2-MS fine-tuned at 12–66 kb (0.746). Dart-Eval: best on Yoruba caQTLs but not African caQTLs. TraitGym: best on Mendelian traits, second on complex traits (AUPRC).
- **Without its special tokens** (GUE, full fine-tuning, no annotations or variants), BioFM ranks second overall. DNABERT-2 is better on epigenetic marks and TF binding, and NT-500M-v2 on promoters.
- **Context use.** BioFM uses its full 6 kb window per strand, and expression and rare-variant performance had not saturated at 12 kb total. Caduceus plateaus near 3 kb. Evo2 degrades past 1 kb on 4 of 6 tasks with mean pooling, so Evo2 was run at 1 kb with intermediate layers (19 and 24) to give it favourable conditions.
- **Last layer is enough.** BioFM's last-layer embeddings are as good as or better than intermediate layers, unlike NT and Evo2, which need a per-task layer search.
- **Promoter generation.** Instruction-tuned on EPDNew (gene sequence + "P" token → promoter, −249/+50 bp), BioFM produced promoters whose 2-mer composition converged to wild type over 10 epochs. TATA-vs-non-TATA MCC was 0.28 at the end; it peaked near 0.38 early, while outputs were CC/GG-enriched.
- **Data scaling.** Checkpoints at 8.6 B to 103.1 B pretraining tokens (≈2.5 to ≈35 genomes) differ most when few fine-tuning samples are available, with diminishing returns.

## Methods / evidence

Vocabulary (Table A3): D, N, A, T, G, C, special tokens, four variant tokens, and six annotation tokens (start/end CDS, transcript, exon). Pretraining: 542,688 regions of 6,144 nt from autosomes and chrX (regions >50% N excluded), 1,000 nt overlap plus a random 0–1,000 nt shift. A random individual's SNVs and indels are applied and one haplotype is picked. Reverse-complement augmentation at p = 0.5 flips strand-specific annotations correctly. RoPE θ is raised from 10^4 to 10^5. AdamW with peak learning rate 7.2e-4 and cosine schedule, batch 64, 2 epochs, hidden 640, 32 heads with 8 GQA groups. Variant embedding for causal models: forward upstream and reverse-complemented downstream halves, each ending at the variant, averaged for reference and alternate and then concatenated. Encoder models get the variant centred. A logistic-regression probe is used to isolate embedding quality. Ablations and UMAP use smaller 67 M and 134 M models.

Weight: a broad, carefully controlled evaluation. All GFMs share one protocol, the matched-compute ACGT-265M baseline isolates the tokenizer, distance-matched negatives address annotation leakage, and Evo2 is given favourable settings. All main results are linear probes, except the LoRA comparison with Enformer and GUE fine-tuning.

## Limitations

**Authors' own:**
- Depends on high-quality annotations and variant calls, which many organisms lack.
- Scaling with more variant data (all ~3,200 1000 Genomes samples, biobanks) is untested.
- Annotation tokens can leak information, since eQTLs and sQTLs sit closer to transcript and exon boundaries than random controls. With distance-matched negatives every model dropped, but BioFM stayed best.
- Dart Yoruba caQTL gains may partly reflect two Yoruba samples (NA19258, NA18930) in pretraining.

**Reviewer notes:**
- The ancestry task uses 1000 Genomes individuals, and 50 of them, including their full variant sets, were in pretraining. The paper does not say whether they were excluded from that task, so the ancestry result may be partly memorization. (synthesis)
- Results text describes variant tokens for "SNVs and insertions", while the Discussion says SNVs, insertions *and deletions* and the vocabulary includes a "D" token. How deletions are encoded is not spelled out. (synthesis)
- The GUE data source is given as the ML-Bioinfo-CEITEC/genomic_benchmarks repository, which is Genomic Benchmarks, not GUE. Table A5 task names (EM, PD, TF, CPD) match GUE, so this is probably a citation slip. (synthesis)

## Surprising or load-bearing bits

- **Personal genomes, not the reference.** Training on real individual haplotypes with explicit variant tokens addresses the problem that MLM or next-token objectives on the reference genome mostly memorize reference sequence and see under 1% variation. (synthesis)
- **"Tokenization" here means adding prior knowledge.** Unlike the BPE vs k-mer vs learned-chunk debate, BioToken keeps single nucleotides and adds annotation and variant tokens. The gain comes from that added knowledge, not from how the sequence is segmented. (synthesis)
- A 265 M model probed linearly at 12 kb matched or beat Enformer at 98 kb on variant-expression tasks, which narrows the gap between general DNA LMs and supervised [[sequence-to-function-model]] tools. The comparison uses Enformer embeddings, not its trained output heads. (synthesis)

## Concepts touched

- [[genomic-tokenization]] — annotation and variant tokens as an inductive-bias tokenizer.
- [[variant-effect-prediction]] — new Variant Benchmark covering coding and noncoding pathogenicity, eQTL, sQTL, meQTL, ancestry and common vs rare variants.
- [[dna-language-model]] — decoder-only, personal-genome pretraining, last-layer embeddings.
- [[sequence-to-function-model]] — head-to-head with Enformer and SpliceTransformer.
- [[dna-methylation]] — meQTL prediction from GRASP with GC- and chromosome-matched negatives.

## Connections to other sources

- Supervised comparators: [[avsec-2021-enformer]]; eQTL and sQTL sets from [[linder-2025-borzoi]]; expression set from [[zhou-2015-deepsea]].
- GFM baselines: [[dallatorre-2025-nucleotide-transformer]], [[nguyen-2023-hyenadna]], [[schiff-2024-caduceus]], [[zhou-2023-dnabert-2]], [[fishman-2025-gena-lm]]. Pathogenicity reference: [[benegas-2025-gpn-msa]].
- Same M42 group as [[vishniakov-2025-gene42]]; cites Vishniakov et al.'s "Genomic foundationless models" critique as motivation.
- Contrast with segmentation-focused tokenizers: [[chen-2023-genomicbert]], [[kim-2026-dnachunker]], [[chen-2026-genart]]. Those papers report weak zero-shot variant scoring for learned chunking, while BioFM targets variants directly. (synthesis)

## Open questions

- Would adding chromatin or methylation tokens, which the authors propose, help regulatory-variant tasks beyond what gene-structure annotations give? (synthesis)
- How much of the gain survives when annotations are predicted rather than taken from GENCODE, for example in non-model organisms? (synthesis)
- Could the same personal-genome and variant-token idea represent somatic variants from single-cell DNA data, such as mosaic SNVs relative to a germline haplotype? (synthesis)

## Related

- [[dna-language-model]] · [[genomic-tokenization]] · [[variant-effect-prediction]] · [[avsec-2021-enformer]] · [[linder-2025-borzoi]] · [[40-Topics/sequence-models-and-foundation-models]]
