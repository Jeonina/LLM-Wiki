---
type: summary
title: "Li et al. 2026 — GENERator: A Long-Context Generative Genomic Foundation Model"
source: "[[00-Sources/papers/GENERator- A Long-Context Generative Genomic Foundation Model.pdf]]"
source_quality: full
source_sha256: "f18a052344cb458b494061e2fbe7078243c860b4da59192482185548709f037d"
source_kind: paper
author: "Wei Wu, Qiuyi Li, Yuanyuan Zhang (co-first; Li project lead), Zhihao Zhan, Ruipu Chen, Mingyang Li, … Yuwen Liu, Hui Xiong, Zheng Wang (co-senior, corresponding)"
published: 2026-02-04
ingested: 2026-10-08
doi: "10.21203/rs.3.rs-8686063/v1"
journal: "Research Square preprint (v1)"
tags: [GENERator, DNA-language-model, generative, decoder-only, LLaMA, 6-mer, k-mer-tokenization, BPE, long-context, eukaryote, RefSeq, sequence-recovery, zero-shot-VEP, ClinVar, Evo2, CRE-design, UMI-STARR-seq, DeepSTARR, central-dogma, Alibaba]
entities: []
concepts: ["[[dna-language-model]]", "[[genomic-tokenization]]", "[[variant-effect-prediction]]", "[[cis-regulatory-element]]", "[[transcription-factor-motif]]", "[[highly-repetitive-regions]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[computational-methods]]"]
---

**Citation:** Wu, Li, Zhang et al. (2026) — *GENERator: A Long-Context Generative Genomic Foundation Model* — Research Square preprint. [DOI](https://doi.org/10.21203/rs.3.rs-8686063/v1)

# Li 2026 — GENERator

> GENERator (Alibaba Cloud with CAAS Shenzhen, USTC, HKUST and Mila) is a LLaMA-style decoder-only DNA language model (1.2B and 3B parameters) with 6-mer tokens and a 16,384-token context (98,304 bp), pre-trained by next-token prediction on 386 billion nucleotides of gene-centric eukaryotic RefSeq sequence. Its contribution is as much a set of controlled design findings for *causal* DNA models — 6-mers beat single-nucleotide and BPE tokens at a fixed token budget, state-space models do not exploit their longer nominal context, and gene-centric training beats whole-genome training despite worse pre-training loss — as it is a model. It outperforms Evo2-1B on sequence recovery and zero-shot ClinVar at far lower inference cost, and its prompt-conditioned *Drosophila* enhancer designs were tested experimentally.

## Key claims

- **Tokenizer sweep (sequence recovery, 1,024 input tokens, 30-nt prediction).** Among 1- to 8-mers and BPE (vocabularies 512–8,192), the 6-mer tokenizer was best. All BPE variants stayed below 0.30 accuracy against a 0.25 random baseline. The authors argue BPE's nested vocabulary penalises valid prefixes (G, GC, GCC when the target is GCCT) under next-token prediction, so BPE's reported advantage in masked models does not carry over to causal ones.
- **Longer single-nucleotide context was not used.** A 1.2B Mamba-2 with 98k nominal context reached 0.378 recovery accuracy at the same token count as a 1-mer transformer (0.381), and 0.382 with six times more tokens, against 0.432 for the 6-mer transformer at equal nucleotide input. Evo2 showed the same flat response to 6× more input tokens (Fig. S5).
- **Sequence recovery against baselines** (6,144-bp prompt, 30-nt continuation, 30,000 sequences across six eukaryotic groups; Table S1). Overall accuracy: GENERator-1B 0.515, Evo2-1B 0.504, GENERator-3B 0.561, Evo2-7B 0.595; masked models 0.276–0.326; HyenaDNA 0.297. Total runtime: 0.37 h (GENERator-1B) against 7.21 h (Evo2-1B), and 0.62 h (3B) against 27.12 h (Evo2-7B). Evo2-40B could not be evaluated.
- **Zero-shot ClinVar** (GPN-MSA's curated set; Table S2), scoring the log-likelihood ratio after marginalising 6-mer token probabilities to per-nucleotide probabilities. AUROC: GENERator-3B 0.921, Evo2-7B 0.921, GENERator-1B 0.910, Evo2-1B 0.867, NT-v2 0.665, HyenaDNA 0.503. Alignment-based methods stay ahead: GPN-MSA 0.970, CADD 0.966, phyloP-100v 0.927.
- **Gene-centric pre-training.** A control model trained on all eukaryotic RefSeq sequence reaches lower pre-training loss but is worse on nearly every downstream task; the authors attribute the lower loss to easily predicted repeats, homopolymers and N runs.
- **Fine-tuned benchmarks** (GENERator-1B, 10-fold CV, per-model hyperparameter grid): highest average on revised and original NT tasks, Genomic Benchmarks and the new Gener tasks, ranking first on 32 of 47 tasks and second on 10 (Fig. S1). Revised NT examples: promoter-all MCC 0.795 against NT-v2 0.780; H3K9me3 0.509 against 0.467. Enformer stays ahead on the revised NT enhancer task (0.614 against 0.594). Taxonomic classification of 96-kb sequences: weighted F1 0.999 against NT-v2 0.981. Evo2 was not fine-tuned (no open fine-tuning code, prohibitive compute).
- **Central-dogma test.** After fine-tuning on cytochrome P450 and histone coding sequences, 99.9% of generated sequences translate with no premature stop or frameshift; ProGen2 perplexity matches natural family members; AlphaFold3 plus Foldseek find PDB folds at TM-score > 0.8 with sequence identity below 0.3.
- **Regulatory-element design.** Fine-tuned on DeepSTARR with `<high>/<mid>/<low>` prefix tokens, plus a separate fine-tuned activity predictor (Pearson 0.71 developmental, 0.80 housekeeping, against DeepSTARR's 0.68 and 0.74). About 40,000 candidates per promoter class were ranked, and 12,026 oligos (designs, 400 natural controls, 26 DREAM designs) were measured by UMI-STARR-seq in S2 cells. Measured against predicted activity gave R² 0.48 (Dev) and 0.83 (Hk), and the three prompt groups separated clearly. The best housekeeping design exceeded the strongest natural sequence by 35% and the best DREAM design by 78%; the best developmental design was more than twice the strongest natural sequence but 45% below the best DREAM design. The weakest `<low>` designs were more than 100-fold below the weakest natural sequences, and the high-activity group showed 15-fold enrichment over random sampling.
- **Motif signatures in designs.** ara and caup motifs were enriched in high-activity designs for both promoter classes; mirr, Optix and Stat92E were specific to developmental designs and pnr, Dref and msl-1 to housekeeping ones, which the authors read as promoter-class compatibility. Base-level contribution scores also marked high-contribution regions matching no known motif.

## Methods / evidence

Architecture (Table S12): 1B = 26 layers, hidden 2,048; 3B = 30 layers, hidden 3,072; grouped-query attention (32 heads, 4 KV heads), RoPE, SiLU, vocabulary 4,128. Pre-training: 2M tokens per batch (128 × 16,384), 6 epochs (~185,000 steps), a random 0–5-nt start offset each epoch to vary 6-mer phase, AdamW with peak learning rate 4e-4, FlashAttention and ZeRO; the 1B model took about 11,800 A100-hours at 46% MFU and the 3B about 29,600. Corpus: annotated gene loci (CDS, introns, UTRs, annotated flanking regulatory regions) across protozoa, fungi, plants, invertebrates, other vertebrates and mammals, with protein-coding loci contributing about 340 of the 386 billion bp. Assay: UMI-STARR-seq quantified with DESeq2; over 99.6% of oligos detected, replicate R² ≥ 0.94. Data are in GSA (PRJCA056161) and weights on HuggingFace (`GenerTeam`).

Weight: unusually complete for a DNA-LM paper, with controlled tokenizer and architecture sweeps, re-run baselines under per-model hyperparameter searches, a large experimental test, and supplementary tables carrying the actual numbers. The long-context claims, though, rest mainly on sequence recovery at prompts of about 6 kb and on taxonomic classification, not on regulatory tasks that would need the full 98 kb.

## Limitations

**Authors' own:**
- Training covers eukaryotes only; prokaryotic and viral genomes are excluded, with a companion model (GENERanno) for prokaryotic annotation.
- Cross-species variant-effect validation is limited by the absence of ClinVar-like resources outside human.
- Fine-tuning benchmarks use only the 1B model; the 3B model was expected to do better but was too costly to evaluate.
- Alignment-based methods still outperform GENERator on ClinVar.

**Reviewer notes:**
- The ClinVar set is weighted toward coding and splice-proximal variants, which suits gene-centric training; the claim of matching phyloP holds on AUPRC (0.939 against 0.937) but not AUROC (0.921 against 0.927). (synthesis)
- Because pre-training covers annotated gene loci, with most bases in protein-coding loci, distal intergenic enhancers are largely absent from pre-training, which matters for non-coding regulatory variants. (synthesis)
- Generation-length figures differ between the text (30 nt), the Fig. 2B caption (50 bp) and the appendix (512 bp), and the all-sequence corpus is about 2 trillion bp in Methods but 1.9T in Table S15. (synthesis)

## Surprising or load-bearing bits

- **Tokenization depends on the training objective.** BPE helps masked DNA models and breaks causal ones; this is the clearest controlled evidence in this batch that NLP defaults should not be copied. (synthesis)
- **Nominal context is not effective context.** Neither Mamba-2 nor Evo2 gained from six times more single-nucleotide input on sequence recovery, which challenges the long-context framing of several state-space DNA models, at least for generation. (synthesis)
- **Lower pre-training loss, worse model.** Whole-genome training lowers perplexity through repeats, so loss is not a safe selection signal across corpora.
- **Both ends of the activity range.** One prompt-conditioned model produced strong enhancers and very weak silencer-like sequences, both outside the natural range in the tested library.

## Concepts touched

- [[dna-language-model]] — causal, 6-mer, gene-centric eukaryotic generator used for both scoring and design.
- [[genomic-tokenization]] — controlled k-mer / BPE / single-nucleotide sweep; 6-mer best for next-token prediction.
- [[variant-effect-prediction]] — alignment-free zero-shot ClinVar scoring by k-mer marginalisation.
- [[cis-regulatory-element]] — prompt-conditioned enhancer and silencer design with experimental readout.
- [[transcription-factor-motif]] — motif enrichment and base-level contribution scores in designed sequences.
- [[highly-repetitive-regions]] — repeats and low-complexity sequence depress pre-training loss without helping downstream tasks.

## Connections to other sources

- Compared with [[nguyen-2023-hyenadna]], [[schiff-2024-caduceus]], [[zhou-2023-dnabert-2]], [[sanabria-2024-grover]], [[dallatorre-2025-nucleotide-transformer]] and [[avsec-2021-enformer]]; Evo2 is the main generative comparator and has no summary in this wiki.
- Variant data and the alignment-based baseline come from [[benegas-2025-gpn-msa]].
- Cites [[ma-2025-hybridna]] as an SSM hybrid and [[avsec-2026-alphagenome]] as a convolution-augmented single-nucleotide model; HybriDNA in turn cites an earlier arXiv version of GENERator as concurrent work.
- The finding that extra state-space context goes unused sits in tension with [[duan-2025-janusdna]] and [[ma-2025-hybridna]], which report gains from longer single-nucleotide context, though on different tasks and objectives. (synthesis)

## Open questions

- Would gene-centric training hurt on distal regulatory tasks, where the excluded intergenic sequence is the signal? Not tested.
- Does the 98-kb context help any task here beyond taxonomic classification? (synthesis)
- Would the designed enhancers behave the same in a different cell type or species, given the oracle and the assay are both *Drosophila* S2? (synthesis)

## Related

- [[dna-language-model]] · [[genomic-tokenization]] · [[cis-regulatory-element]] · [[variant-effect-prediction]] · [[benegas-2025-gpn-msa]] · [[40-Topics/sequence-models-and-foundation-models]]
