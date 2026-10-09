---
type: topic
title: Sequence models and foundation models
aliases: [genomic foundation models, sequence-based prediction, scFM, foundation models, sequence models]
tags: [foundation-model, dna-language-model, sequence-to-function, single-cell-foundation-model, deep-learning]
created: 2026-10-08
updated: 2026-10-09
paper_section: ["4.4"]
description: "Hub for §4.4: supervised sequence-to-function models, DNA language models, single-cell epigenome and multimodal foundation models (64 papers, 2026-10-08), plus evidence for the genotype, histone and somatic-variant gaps (10 papers, 2026-10-09)."
---

# Sequence models and foundation models

> Models that learn from DNA sequence or from large single-cell epigenome corpora and transfer to new tasks: supervised [[sequence-to-function-model]]s, self-supervised [[dna-language-model]]s, and [[single-cell-foundation-model]]s for accessibility, methylation, 3D contacts and RNA+ATAC. This hub gathers the 64 papers from the review's foundation-model list (§4.4 and the future-perspective paragraph), ingested on 2026-10-08.

## Core concepts

- [[sequence-to-function-model]] — supervised prediction of functional tracks from sequence (DeepSEA → AlphaGenome).
- [[dna-language-model]] — self-supervised models of DNA sequence (DNABERT → Evo 2).
- [[single-cell-foundation-model]] — pretrained models of single-cell accessibility, methylation, Hi-C and RNA+ATAC.
- [[genomic-tokenization]] — k-mers, BPE, single nucleotides, learned chunks, variant and region tokens.
- [[variant-effect-prediction]] — scoring variants from model outputs, likelihoods or embeddings.

## Where this sits in the review (synthesis)

- **Every DNA layer except genotype and histone has a pretrained model here.** Accessibility (Atacformer, CLM-access, EpiFoundation, EpiZoo, GET), methylation (scDNAm-GPT; bulk CpGPT and MethylGPT) and 3D (HiCFoundation, Evo2HiC) are covered; no model in this set is pretrained on histone-modification profiles or on single-cell genotypes (CNV/SNV).
- **Sequence priors are entering single-cell epigenomics.** GFETM, EpiZoo, CpGPT and Evo2HiC all reuse DNA-LM embeddings ([[10-Summaries/fan-2026-gfetm]]; [[10-Summaries/li-2026-epizoo]]; [[10-Summaries/delimacamillo-2024-cpgpt]]; [[10-Summaries/fang-2025-evo2hic]]).
- **Variant scoring is germline-centred.** Benchmarks are eQTL, caQTL and ClinVar; somatic and single-cell genotype inputs are largely untested (see [[variant-effect-prediction]]).

## Evidence for the three gaps (added 2026-10-09)

Papers found by a verified literature search (Europe PMC, PubMed, arXiv; 2026-10-08) to test whether the gaps above were search gaps or real absences. All three held for single-cell data. ChromBERT (Yu 2026, Cell Genomics), a bulk ChIP-seq model with histone channels, is pending a clipping.

### Genotype layer — no single-cell genotype foundation model

- CoT applies self-attention directly to single-cell DNA copy-number profiles but trains from scratch on each dataset with an MSE reconstruction loss and no pretraining or transfer, so even the closest transformer for the scDNA genotype layer is not a foundation model ([[10-Summaries/liu-2024-cot]])
- MutationProjector is a pretrained genotype model reused frozen across clinical tasks, but its input is binary gene-level mutation/amplification/deletion calls over a fixed 468-gene panel from 30,328 bulk tumours, so single-cell DNA would need gene-level per-cell calls, explicit handling of allelic dropout and missing genes, and some way to represent clone structure ([[10-Summaries/kong-2026-mutationprojector]])
- TESSERA is a pretrained, frozen, reusable genotype model with masked SNV- and CNA-segment objectives and SNV–CNA contrastive alignment, but its tokens are bulk, purity-adjusted profiles of about 10,000 TCGA tumours, so it has no cell-level or clone-level input and was never tested on single-cell copy-number profiles ([[10-Summaries/sidhom-2026-tessera]])

### Histone layer — no single-cell histone foundation model

- CANDI is the nearest histone-inclusive pretrained epigenome model, but it is self-supervised on bulk ENCODE tracks (35 assays across 361 merged cell types), is never called a foundation model and has no single-cell input, so it does not close the single-cell histone gap ([[10-Summaries/foroozandeh-2025-candi]])
- The first scHPTM imputation benchmark could test only borrowed, non-pretrained scRNA/scATAC tools, because no imputation or cross-modality method exists for single-cell histone data; none of them improved both signal and clustering, and the authors list neighbouring-bin, cell-type-prior and multi-mark models as missing ([[10-Summaries/morenogonzalez-2025-schistone-imputation]])

### Somatic variants — sequence models are applied to somatic variants more than they are tested on them

- In the first genome-wide noncoding clonal-haematopoiesis driver scan, discovery is purely statistical. The only DNA sequence model, AlphaGenome, is used afterwards to guess cis target genes with no benchmark or validation, so CH variants remain unevaluated as a sequence-model test set ([[10-Summaries/weinstock-2025-ch-noncoding-drivers]])
- A DNA language model is benchmarked on somatic variants, but only on curated cancer driver vs passenger point mutations (likely coding). The test set has 71 xenograft mutations, and swapping in HyenaDNA or DeepSEA features changes AUROC by less than 1 point ([[10-Summaries/zeng-2025-somatic-driver-lm]])
- AlphaGenome was applied to real normal-tissue somatic SNVs and short indels from human and mouse colonic crypts, but no variant effect was measured, so the near-zero predictions were never checked against ground truth and the model's somatic calibration stays untested ([[10-Summaries/fischbach-2026-alphagenome-aging]])
- A sequence-to-function model (Akita) is applied at cohort scale to somatic tumour SVs, but only as an unbenchmarked screen. It is never checked against tumour contact maps and is supported only by enhancer overlap and single-sample expression outliers ([[10-Summaries/gjoni-2026-pediatric-tumor-3d]])
- In a held-out test on somatic T-ALL noncoding indels and ITDs in TAL1 downstream enhancer I, AlphaGenome scored these variants significantly lower than other TAL1 enhancer variants (P = 3.32 × 10^-7) although measured TAL1 expression did not differ (P = 0.35), and it did not predict the exon-4 short-isoform transcription seen in patient xenografts ([[10-Summaries/terekhanova-2026-tal1-enhancer]])

## Sources, by sub-theme

### Supervised sequence-to-function models (16)

Predict measured chromatin, expression or contact tracks from DNA sequence; see [[sequence-to-function-model]].

- [[10-Summaries/zhou-2015-deepsea]] — **DeepSEA** (2015): DeepSEA: multitask CNN predicting 919 chromatin profiles from 1 kb sequence; TF median AUC 0.958, >95% accuracy on confident allelic-imbalance SNPs
- [[10-Summaries/kelley-2016-basset]] — **Basset** (2016): Basset: CNN predicting DNase hypersensitivity in 164 cell types from 600 bp; mean AUC 0.895 vs 0.780 gkm-SVM; SAD scores enrich PICS-causal GWAS SNPs
- [[10-Summaries/kelley-2018-basenji]] — **Basenji** (2018): Basenji: dilated CNN predicting 4,229 coverage tracks (DNase, ChIP, CAGE) in 128 bp bins from 131 kb; gene CAGE r 0.85; SED scores enrich GTEx eQTLs 3.2–5.8×
- [[10-Summaries/zhou-2018-expecto]] — **ExPecto** (2018): ExPecto: DeepSEA-style CNN plus spatial basis plus per-tissue linear models predicts expression in 218 tissues from 40 kb (Spearman 0.819); scores 140 M promoter mutations
- [[10-Summaries/fudenberg-2020-akita]] — **Akita** (2020): Akita: CNN predicting Hi-C/Micro-C maps at 2 kb from ~1 Mb sequence (test Pearson 0.61); reveals orientation-specific CTCF grammar and buffered mouse B2 SINEs
- [[10-Summaries/avsec-2021-enformer]] — **Enformer** (2021): Enformer — conv+transformer seq-to-function model, 196 kb in, 5,313 tracks at 128 bp; CAGE gene r 0.81→0.85 vs Basenji2, better eQTL/MPRA scoring
- [[10-Summaries/zhou-2022-orca]] — **Orca** (2022): Orca: multiscale CNN predicting Micro-C from 4 kb within 1 Mb up to 256 Mb incl. trans (Pearson 0.73–0.85); predicts SV effects; TSS sequences drive A compartments
- [[10-Summaries/chen-2022-sei]] — **Sei** (2022): Sei: 4 kb CNN predicting 21,907 chromatin profiles (AUROC 0.972), clustered into 40 sequence classes for directional variant scoring, heritability and HGMD mechanisms
- [[10-Summaries/pampari-2024-chrombpnet]] — **ChromBPNet** (2024): ChromBPNet — ~6M-param bias-factorized BPNet CNN for base-resolution ATAC/DNase; removes Tn5/DNase-I bias, gives TF footprints, competitive with Enformer on caQTLs
- [[10-Summaries/gao-2024-epigept]] — **EpiGePT** (2024): EpiGePT — context-conditioned transformer (TF expression × motif input) predicts 8 epigenomic tracks in unseen cell types; DNase PCC 0.787 cross-cell-type, HiChIP-guided attention
- [[10-Summaries/linder-2025-borzoi]] — **Borzoi** (2025): Borzoi — Enformer-derived U-net predicting RNA-seq coverage (524 kb, 32 bp); one model scores expression, splicing and polyA variants; eQTL AUROC 0.794 vs 0.747
- [[10-Summaries/fang-2025-evo2hic]] — **Evo2HiC** (2025): Evo2HiC: Evo 2 (7B) distilled into a 3.6M CNN guided by bulk Hi-C; +10.9% Spearman over Orca, Hi-C enhancement beats HiCARN2 in 157/177 species
- [[10-Summaries/boshar-2025-ntv3]] — **NTv3** (2025): NTv3 — Nucleotide Transformer successor: U-Net, single-base tokens, 1 Mb context, post-trained on ~16k tracks/24 species; beats Borzoi, SegmentNT, SpliceAI.
- [[10-Summaries/avsec-2026-alphagenome]] — **AlphaGenome** (2026): AlphaGenome — 1 Mb input, 1-bp output, 11 modalities incl. splice junctions and contact maps; matches or beats specialists on 25/26 variant-effect benchmarks
- [[10-Summaries/lin-2026-epinformer]] — **EPInformer** (2026): EPInformer — 0.4M-param promoter–enhancer transformer using sequence + DNase/H3K27ac/Hi-C; beats Enformer/Borzoi on CAGE and ABC on CRISPRi enhancer–gene links
- [[10-Summaries/sun-2026-succeed]] — **SUCCEED** (2026): SUCCEED — lightweight CNN+transformer pretrained supervised on 6,389 ENCODE tracks; reused as encoder for epigenome, ATAC denoising and Hi-C prediction tasks
### Sequence-to-single-cell models (3)

Sequence-to-function models whose outputs are single cells or cell-type pseudobulks.

- [[10-Summaries/hingerl-2025-scooby]] — **scooby** (2025): scooby — Borzoi + LoRA + cell-embedding decoder predicts single-cell RNA/ATAC profiles; beats seq2cells (0.77→0.87) and maps eQTLs to cell types
- [[10-Summaries/kempynck-2026-crested]] — **CREsted** (2026): CREsted — Aerts-lab package for scATAC sequence-to-accessibility enhancer models and design; small CNN matches fine-tuned Borzoi, zebrafish enhancers validated in vivo
- [[10-Summaries/lal-2026-decima]] — **Decima** (2026): Decima — Borzoi fine-tuned on 8,856 sc/snRNA pseudobulks (22M cells) predicts cell-type/disease expression; beats Borzoi on sc-eQTLs in 19/21 cell types
### DNA language models (self-supervised) (31)

Pretrained on sequence alone; see [[dna-language-model]] and [[genomic-tokenization]].

- [[10-Summaries/ji-2021-dnabert]] — **DNABERT** (2021): DNABERT: BERT-base masked LM on human genome with overlapping k-mers; fine-tunes to promoter/TFBS/splice SOTA (ENCODE 690 TF mean acc/F1 >0.9)
- [[10-Summaries/zhou-2023-dnabert-2]] — **DNABERT-2** (2023): DNABERT-2: 117M BPE-tokenised multi-species BERT with ALiBi; matches NT-2500M-multi on new GUE benchmark (66.80 vs 66.93) at 21x fewer params
- [[10-Summaries/nguyen-2023-hyenadna]] — **HyenaDNA** (2023): HyenaDNA: attention-free Hyena long-convolution causal DNA LM, single-nt tokens, up to 1M context; SOTA on 12/18 NT and 7/8 GenomicBenchmarks with ≤7M params
- [[10-Summaries/chen-2023-genomicbert]] — **genomicBERT** (2023): genomicBERT: 89M MosaicBERT with a 4k SentencePiece-Unigram DNA vocabulary, 10k pretraining steps; near-parity with DNABERT-2 on 5 tasks at far lower compute
- [[10-Summaries/ellington-2024-aido-dna]] — **AIDO.DNA** (2024): AIDO.DNA — 7B encoder-only DNA LM, single-nucleotide tokens, 4 kb context on NT's 796-genome data; GUE avg 73.3 vs 67.7 (DNABERT-2).
- [[10-Summaries/schiff-2024-caduceus]] — **Caduceus** (2024): Caduceus: bidirectional, reverse-complement-equivariant Mamba DNA LM (~2M params, 131k context); beats NT-v2 and Enformer on distal (>100 kb) eQTL VEP
- [[10-Summaries/sanabria-2024-grover]] — **GROVER** (2024): GROVER: human-only BERT DNA LM with BPE vocabulary (600 cycles) chosen by next-k-mer prediction; shows TF-IDF frequency baselines explain much of NT/GUE
- [[10-Summaries/su-2025-atgc-gen]] — **ATGC-Gen** (2025): ATGC-Gen — plain GPT/BERT transformers with cross-modal conditioning for regulatory-sequence modelling; beats diffusion and flow-matching baselines on promoter, enhancer and a new ChIP-seq benchmark.
- [[10-Summaries/li-2025-bmfm-dna]] — **BMFM-DNA** (2025): BMFM-DNA (IBM): ModernBERT trained on dbSNP-variant-encoded genome (121 symbols); beats its reference twin on 5/6 tasks, roughly matches DNABERT-2
- [[10-Summaries/medvedev-2025-biofm]] — **BioFM** (2025): BioToken/BioFM: 265M decoder trained on 1000G personal genomes with variant and GENCODE annotation tokens; beats Enformer/SpliceTransformer on eQTL/sQTL by linear probe
- [[10-Summaries/zhang-2025-deepgene]] — **DeepGene** (2025): DeepGene — 85M/118M BERT with RoPE pretrained on the HPRC 47-individual Minigraph pangenome graph; the 118M variant tops the GUE average (67.79 vs NT-2500M-multi 66.93) on yeast/mouse wins but trails on human promoter/splice tasks, and edges DNABERT-2 on 2–5 kb promoter detection.
- [[10-Summaries/fishman-2025-gena-lm]] — **GENA-LM** (2025): BERT/BigBird DNA LM family with BPE tokens (median 9 bp) and recurrent memory; 4.5–36 kb context, top average on the 18-task NT benchmark at 330M params
- [[10-Summaries/benegas-2025-gpn-msa]] — **GPN-MSA** (2025): GPN-MSA: 86M masked DNA LM over a 100-vertebrate alignment; beats NT-2.5B, HyenaDNA, CADD, phyloP on most VEP benchmarks; ~9B human SNVs scored
- [[10-Summaries/vishniakov-2025-gene42]] — **Gene42** (2025): Decoder-only LLaMA-style DNA LM keeping dense attention to 192 kb at single-nucleotide resolution via RoPE-based continued pretraining; best biotype F1 0.782
- [[10-Summaries/ma-2025-hybridna]] — **HybriDNA** (2025): Decoder-only Transformer–Mamba2 hybrid (7:1 blocks) at 300M/3B/7B, 131 kb single-nucleotide context; leads most GUE tasks and designs enhancers beating HyenaDNA
- [[10-Summaries/duan-2025-janusdna]] — **JanusDNA** (2025): Bidirectional hybrid Mamba/MoE DNA model with 'Janus' full-token two-sided objective; ~2M activated params lead 12/18 NT tasks and 8/9 DNALongBench eQTL tissues
- [[10-Summaries/long-2025-mutbert]] — **MutBERT** (2025): MutBERT: 86M encoder fed 1000 Genomes allele-frequency 'probabilistic genome'; 3rd on 23 tasks behind much larger NT models; eQTL AUROC 0.615
- [[10-Summaries/ding-2025-nucel]] — **NucEL** (2025): NucEL: 93M ModernBERT DNA encoder trained with ELECTRA replaced-token detection on single nucleotides; best GUE (75.16), GB and revised-NT averages from human-only data
- [[10-Summaries/dallatorre-2025-nucleotide-transformer]] — **Nucleotide Transformer** (2025): Nucleotide Transformer: 50M–2.5B BERT DNA LMs (6-mer, 1000G/850 species); fine-tuned NT matches/beats BPNet on 18/18 tasks; NT-v2 250M best (MCC 0.769)
- [[10-Summaries/ayanian-2025-strand]] — **STRAND** (2025): STRAND (Mayo/Cerebras): ~1B decoder DNA LM trained on raw aligned exome reads + reference; claims SOTA on NT and new ClinVar/RA/IBD tasks
- [[10-Summaries/dealmeida-2025-segmentnt]] — **SegmentNT** (2025): SegmentNT — fine-tunes Nucleotide Transformer with a 1D U-Net head to segment 14 genomic element classes at base resolution; avg MCC 0.45 at 30 kb, 0.16 with random encoder.
- [[10-Summaries/kim-2026-dnachunker]] — **DNAChunker** (2026): DNAChunker: 172M masked DNA LM with learned two-stage dynamic chunking (BiMamba router + Transformer); best NT-benchmark average (MCC 0.772) from human-only pretraining
- [[10-Summaries/leib-2026-dnt]] — **DNT** (2026): DNT: single-stream diploid tokenization (zygosity, indels, optional phase) on NTv3 + contrastive phase loss; cis/trans compound-het AUROC 0.649 vs ~0.5
- [[10-Summaries/brixi-2026-evo2]] — **Evo 2** (2026): Evo 2 — autoregressive DNA language model, 7B/40B params, 1 Mb context, all domains of life; zero-shot variant effects from likelihood change, plus genome-scale generation
- [[10-Summaries/li-2026-generator]] — **GENERator** (2026): 1.2B/3B LLaMA-style 6-mer generative DNA model on 386 Gb of gene-centric eukaryotic DNA; beats Evo2-1B on recovery/ClinVar at ~19x speed, designs validated enhancers
- [[10-Summaries/chen-2026-genart]] — **GenART** (2026): GenART: 350M/1B hierarchical DNA LM with a trainable CNN+Gumbel-softmax tokenizer, tunable per task; best NT and GUE averages and 0.629 recall of GENCODE boundaries
- [[10-Summaries/lin-2025-genos]] — **Genos** (2026): BGI mixture-of-experts DNA LM (1.25B/10.27B total, 0.33B/2.87B active) on 636 human pangenome assemblies at 1-Mb context; best mutation-hotspot and ClinVar AUCs
- [[10-Summaries/salman-2026-mendel]] — **Mendel** (2026): Mendel: 1B StripedHyena2 trained on GTEx genotypes as IUPAC tokens; residual errors flag fine-mapped cis-eQTLs (AUROC 0.731) and improve TWAS in 50/50 tissues
- [[10-Summaries/aspidova-2026-moderngena]] — **ModernGENA** (2026): ModernGENA: GENA-LM rebuilt on ModernBERT (135M/377M, 32k BPE, vertebrate TSS windows); top NT rank under 500M and faster inference, weak on splice sites
- [[10-Summaries/shen-2026-omnina]] — **OmniNA** (2026): OmniNA — LLaMA-style DNA+text model pretrained on 91.7M NCBI nt sequences with their annotations; fine-tuned as QA on 23 tasks, F1 0.90 vs EVE 0.81 on 48 genes.
- [[10-Summaries/liu-2026-ukbiobert]] — **UKBioBERT** (2026): UKBioBERT: DNABERT-2 continued-pretrained on 13M UK Biobank variants; fused with Enformer (UKBioFormer) beats Performer on 63% of predictable genes
### Epigenome foundation models (9)

Pretrained on accessibility, methylation or Hi-C profiles; see [[single-cell-foundation-model]].

- [[10-Summaries/delimacamillo-2024-cpgpt]] — **CpGPT** (2024): CpGPT: transformer on 155k bulk Illumina-array methylomes, loci keyed by NTv2 sequence embeddings; zero-shot imputation/array conversion, CpGPTGrimAge3 top mortality HR in 3 held-out cohorts
- [[10-Summaries/ying-2024-methylgpt]] — **MethylGPT** (2024): MethylGPT: scGPT-style transformer over a fixed 49,156-CpG vocabulary on 154k bulk array methylomes; masked-value R 0.929, age MedAE 4.45 y, robust to 70% missing
- [[10-Summaries/leroy-2025-atacformer]] — **Atacformer** (2025): Atacformer: ELECTRA-pretrained transformer on scATAC treating cells as unordered sets of 890k region tokens; reads fragments directly, CRAFT RNA–ATAC, icTSS promoter discovery
- [[10-Summaries/liu-2025-clm-access]] — **CLM-access** (2025): CLM-access: BERT-style scATAC model on 2.8M cells with 2,000 patch tokens over 1.15M cCREs; ablations show binarised peak-level BCE essential; beats scATAnno/Cellcano, BABEL
- [[10-Summaries/wu-2025-epifoundation]] — **EpiFoundation** (2025): EpiFoundation: scATAC transformer on non-zero peak tokens, pretrained on 100k-cell 10x Multiome MiniAtlas to predict paired binary RNA; top integration metrics, 2× Gene Activity correlation
- [[10-Summaries/fu-2025-get]] — **GET** (2025): GET — transformer over motif-scored accessible peaks, pretrained on scATAC pseudobulks of 213 cell types; predicts expression in unseen cell types (r=0.94) and TF–TF interactions
- [[10-Summaries/liang-2025-scdnam-gpt]] — **scDNAm-GPT** (2025): scDNAm-GPT: Mamba model pretrained on ~1M scWGBS cells with CpG-centred 6-mer fuzzy tokens; 80–87% cell-type accuracy on unseen sets, pseudotime, cfDNA tumour signal
- [[10-Summaries/li-2026-epizoo]] — **EpiZoo** (2026): EpiZoo: 2.6B-param MoE scATAC model on 20.9M human+mouse cells with DNABERT-2 sequence-aware cCRE tokens; transfers to macaque/fish/fly/maize, scores cancer variants, predicts cell-type accessibility
- [[10-Summaries/wang-2026-hicfoundation]] — **HiCFoundation** (2026): HiCFoundation — ViT masked autoencoder pretrained on Hi-C maps; frozen encoder fine-tuned for loops (F1 0.816), enhancement, epigenome-from-Hi-C and scHi-C
### Multimodal foundation models (5)

RNA + ATAC single-cell models, and sequence-conditioned multimodal models.

- [[10-Summaries/wang-2025-omnireg-gpt]] — **OmniReg-GPT** (2025): 270M causal DNA LM with 12 local + 2 global attention blocks, 20-kb pretraining in 60 h on 4 RTX 3090s; frozen embeddings drive expression, scATAC and 2-Mb Hi-C heads
- [[10-Summaries/liu-2025-scarf]] — **SCARF** (2025): SCARF: Mamba-based RNA+ATAC foundation model pretrained on 2.7M paired 10x Multiome cells (X-Omics); best FOSCTTM/matching on PBMC vs GLUE/Seurat/Harmony
- [[10-Summaries/liu-2025-scmomer]] — **scMomer** (2025): scMomer: 3-stage RNA+ATAC framework (scBERT + ViT-ATAC, pseudo-paired fusion, RNA→ATAC distillation) for RNA-only inference; pseudo-bulk ATAC PCC 0.981
- [[10-Summaries/li-2026-clm-x]] — **CLM-X** (2026): CLM-X: BEiT-3 multiway Transformer pretrained on 36M scRNA + 2.8M scATAC + 377k pseudo-paired cells; best RNA↔ATAC translation (lowest RMSE 7/7 datasets)
- [[10-Summaries/yu-2026-scdynomics]] — **scDynOmics** (2026): scDynOmics: ~80M-param Linformer transformer with TF-guided attention, pretrained on 752k mouse multiome cells (promoter-ATAC per gene); LoRA adapters + IG attribution

### Gap evidence (10, added 2026-10-09)

- [[10-Summaries/liu-2024-cot]] — (genotype gap) Liu 2024 (Brief Bioinform): CoT, a transformer autoencoder on scDNA read counts trained per dataset; GMM clones + clone-level HMM CNA calls; beats rcCAE on 10x breast data
- [[10-Summaries/kong-2026-mutationprojector]] — (genotype gap) Kong 2026 (Cancer Discov): MutationProjector, a graph-attention FM over 468 panel genes × 8 molecular networks, pretrained on 30,328 bulk tumours; predicts ICI/chemo response
- [[10-Summaries/sidhom-2026-tessera]] — (genotype gap) Sidhom 2026 (bioRxiv): TESSERA, a cancer-genome FM pretrained on TCGA bulk WES SNVs + ABSOLUTE CNA segments; frozen embeddings reused for typing, prognosis, chemo selection
- [[10-Summaries/foroozandeh-2025-candi]] — (histone gap) Foroozandeh 2025 CANDI: self-supervised masked-assay transformer that imputes and denoises bulk ENCODE histone/accessibility tracks as raw counts with calibrated uncertainty
- [[10-Summaries/morenogonzalez-2025-schistone-imputation]] — (histone gap) Moreno-González 2025 SCIBED: benchmark of 10 scRNA/scATAC imputers on sortChIC/scCUT&Tag histone data; no method improves both signal and clustering
- [[10-Summaries/weinstock-2025-ch-noncoding-drivers]] — (somatic variants gap) Age-association scan of ~147M variants in ~490K UKB blood WGS finds 35 novel CH drivers (32 noncoding, incl. TERT promoter, UGT2B7, IGH); AlphaGenome used only for gene assignment
- [[10-Summaries/zeng-2025-somatic-driver-lm]] — (somatic variants gap) GenomeBert: small k-mer BERT DNA LM with XGBoost on REF−ALT embeddings; cancer somatic point-mutation driver vs passenger, AUROC 84.6% on 71-mutation xenograft set
- [[10-Summaries/fischbach-2026-alphagenome-aging]] — (somatic variants gap) Fischbach 2026 — AlphaGenome RNA-seq scores for Cagan 2022 colon-crypt somatic SNVs/indels sit 10^3–10^4× below the aging transcriptome; argues against mutation accumulation
- [[10-Summaries/gjoni-2026-pediatric-tumor-3d]] — (somatic variants gap) SuPreMo-Akita scores ~300k somatic SVs from 1,843 CBTN paediatric tumours for predicted 3D-contact disruption; 5 recurrent hotspots, ABC enhancer weighting; no benchmark
- [[10-Summaries/terekhanova-2026-tal1-enhancer]] — (somatic variants gap) Terekhanova 2026 — T-ALL somatic indels/ITDs reactivate a TAL1 progenitor enhancer (short isoform, exon-4 TSS); AlphaGenome under-predicts this held-out region

### Earlier wiki sources on the same theme

- [[10-Summaries/angermueller-2017-genomebiol]] — DeepCpG, sequence + neighbouring CpGs for single-cell methylation imputation.
- [[10-Summaries/yuan-2022-scbasset]] — scBasset, sequence-based scATAC model.
- [[10-Summaries/fan-2026-gfetm]] — GFETM, DNA-LM embeddings inside a scATAC topic model.
- [[10-Summaries/cui-2024-natmethods]] — scGPT, the transcriptome foundation-model template.

## Open questions

- Would a DNA LM trained on single-cell genotypes, with allele dropout and amplification error, help somatic variant calling? No such model exists in this set (synthesis).
- Do pseudo-paired multimodal pretraining corpora (scMomer, CLM-X) transfer as well as truly paired ones (SCARF)? Untested (synthesis).
- Self-supervised DNA LMs often do not beat supervised or simple baselines on regulatory tasks (see [[dna-language-model]] › Contested points); when is pretraining worth its cost?

## Related

- [[40-Topics/computational-methods]] · [[40-Topics/single-cell-atac-seq]] · [[40-Topics/dna-methylation]] · [[40-Topics/3d-genome]] · [[40-Topics/single-cell-multiomics]] · [[40-Topics/mosaic-variant-calling]]
- [[50-Notes/computational-framework-structure]]
