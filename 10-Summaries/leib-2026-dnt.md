---
type: summary
title: "Leib et al. 2026 — DNT: Diploid Genomic Foundation Model"
source: "[[00-Sources/papers/DNT- Diploid Genomic Foundation Model.pdf]]"
source_quality: full
source_sha256: "3c2ca0b52e21afe081e05eaf857c2a8e83202a163acf6400208ee5a190e2fbf5"
source_kind: paper
author: "Guy Leib, Tal Zinger, Dan Ofer, Raizy Kellerman, Omri Nayshool, Dan Dominissini, … Gideon Rechavi (senior; no corresponding author marked in text)"
published: 2026-09-11
ingested: 2026-10-08
doi: "10.64898/2026.09.05.749576"
journal: "bioRxiv preprint"
tags: [DNT, diploid-encoding, DNA-language-model, phasing, haplotype, zygosity, compound-heterozygosity, cis-trans, Nucleotide-Transformer-v3, continual-pretraining, contrastive-phase-loss, 1000-Genomes, ClinVar, HGMD, CFTR, indels, preprint]
entities: []
concepts: ["[[dna-language-model]]", "[[variant-effect-prediction]]", "[[genomic-tokenization]]", "[[allele-dropout]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]"]
---

**Citation:** Leib et al. (2026) — *DNT: Diploid Genomic Foundation Model* — bioRxiv preprint, posted 2026-09-11. [DOI](https://doi.org/10.64898/2026.09.05.749576)

# Leib 2026 — DNT (diploid tokenization)

> DNT writes **both homologues of an individual genome into one reference-aligned token stream**: homozygous positions keep A/C/G/T, heterozygous positions become one atomic allele-pair symbol, short indels are aligned within `{…}` spans with gap padding so inserted and deleted bases survive, and phase can be kept either as ordered symbols or as an unordered symbol plus a direction marker. Nucleotide Transformer v3 checkpoints (8 M and 100 M parameters) are vocabulary-adapted (11 → 55 tokens) and continually pretrained on phased high-coverage 1000 Genomes sequences, with an auxiliary **Contrastive Phase Loss (CPL)** that pushes phase-reversed views apart. On a synthetic compound-heterozygous benchmark (cis vs trans pairs of HGMD pathogenic variants in the same recessive gene), every phase-blind model is at chance (≈ 0.49–0.53 AUROC) while the best diploid model reaches 0.649 ± 0.005 fine-tuned. The authors present this as a method that makes diploid genotype readable to a DNA LM, not as a general accuracy gain.

## Key claims

- **Phase-blind inputs cannot solve cis vs trans.** The vocabulary-adapted control, the haploid continual-pretraining control and the unphased diploid model give frozen-probe AUROC 0.491–0.512 and fine-tuned 0.506–0.533 at both scales (Table 1).
- **Phase tokens alone are not enough; CPL makes them used.** Marker-phase MLM: frozen 0.548 / 0.540 (8M / 100M). Adding CPL: 0.555 / 0.621. Full epoch (922,206 steps) with CPL: frozen 0.613 / 0.624, fine-tuned 0.649 / 0.639. Under MLM alone, original and homologue-swapped contexts have high cosine similarity, i.e. orientation is in the input but ignored.
- **Diploid encoding helps zygosity-sensitive ClinVar SNVs, phase does not.** On a mode-of-inheritance-aware ClinVar SNV benchmark (recessive pathogenic variants labelled negative when heterozygous, positive when homozygous; chr19–22 test), the phase-removed diploid model scores highest (0.853 at 8M) versus 0.812 for the haploid continuation; marker-phase CPL reaches 0.798, or 0.852 at full epoch. Reading the same trained model through diploid vs haploid input beats haploid in 10 of 11 arms, mean +0.106 AUROC (Wilcoxon P = 0.0029). 100M models are unexpectedly worse (0.746–0.830).
- **Indels.** Zero-shot ClinVar indel pathogenicity (939 benign, 2,065 pathogenic): mean AUROC 0.679 diploid vs 0.524 haploid; best values come from phase-blind conditions (0.727 marker-phase MLM 8M; 0.728 phase-removed 100M), and CPL lowers it. The "biallelic" (two-allele) readout sits near 0.21, which the authors show is a zygosity indicator anti-correlated with the labels, not a sequence signal.
- **No loss of general capability.** On GUE probes, diploid conditions match or exceed the base NTv3 (100M mean MCC: original 0.609, marker-phase CPL 0.654). Across 54 GFMBench-API benchmark-metric combinations the diploid CPL checkpoint beat its NTv3 baseline in 36 (8M) and 43 (100M).
- **CFTR case.** Zero-shot LLR separates pathogenic from benign ClinVar CFTR SNVs with AUROC 0.780 (150 vs 67). G542X scores pathogenic; variable-penetrance R117H scores benign-like. F508del gives distinct heterozygous and homozygous local profiles. Descriptive only.

## Methods / evidence

Corpus: high-coverage phased 1000 Genomes (~3,200 individuals including 602 trios); pedigree-aware split via union-find (2,001 connected components) into 2,560 train / 642 test individuals, stratified by superpopulation × component size. Regions: GENCODE v47 coding exons plus phastCons 100-way elements (log-odds > 500), padded to ≥ 4,094 bp and merged — 140,099 intervals, ~943 Mb (~30% of GRCh38). 110.9 M deduplicated records, 221.4 M 4,096-token windows, ~907 B tokens. New embeddings seeded from parent nucleotides, 5,000-step warm-up with frozen backbone. MLM 15% on whole diploid tokens; SNV-marker dropout 0.15; CPL λ = 0.5 with a 64-d projector (without it the loss is satisfied by a global sign flip, cosine −0.999). Ablations at 60,000 steps; full run on 8 H100s (~170 and ~580 GPU-hours). Compound-het benchmark: HGMD 2023.2 variants injected into 1000 Genomes haplotypes, 117 genes (28 recessive-eligible), 6,144-bp windows, 9,460 examples (6,669 / 980 / 1,811), no shared individuals, variants, pairs or cis-trans twins across splits; classifier on [e_A, e_B, e_A − e_B, e_A ⊙ e_B]. Code and checkpoints: github.com/scrcdnai-max/DNT-Diploid-Genomic-Foundation-Model; ClinVar benchmarks on Hugging Face; HGMD-derived records not redistributed.

Figures 1–4 are images in the PDF text; numbers above come from Tables 1–3, Extended Data and Supplementary Tables. The source `.md` clipping originally paired with this PDF was a mis-named copy of a different paper and was removed; this summary uses the PDF only.

## Limitations

**Authors' own:**
- Compound-heterozygous examples are synthetic (curated variants injected into population haplotypes); real patients differ in transcript, severity, penetrance, modifiers, ancestry and ascertainment.
- Statistically phased population data contain errors; trio, long-read and haplotype-resolved data would be better.
- 4,096-token windows capture mainly local configuration, despite NTv3 supporting longer contexts.
- Only SNVs and short indels; no structural variants, CNVs, repeat expansions, inversions or complex rearrangements. Hemizygous tokens are defined but unused; male X was rendered homozygous.
- ClinVar and HGMD over-represent well-studied genes, severe phenotypes and some populations. Only the NTv3 backbone was tested.
- The cis-trans task family guided model selection (validation split only), so independent cohorts are needed.

**Reviewer notes:**
- Internal inconsistencies: the Fig. 3 legend reports the diploid readout ahead in 9 of 10 arms (P = 0.0059) while Table 2 reports 10 of 11 (P = 0.0029); the abstract's 0.649 is the 8M fine-tuned score, whereas the text calls 0.624 (100M frozen) the strongest frozen result; ED Fig. 1 says the corpus snapshot used the marker-phase scheme with zero ordered-phase tokens, yet ordered-symbol models are reported. (synthesis)
- The best phase result, 0.649 AUROC on a synthetic task with a linear-separability-friendly classifier, shows that phase is recoverable, not that it is captured well; Supplementary Table 3 notes learning rate matters more than objective at full budget. (synthesis)
- The 0.853 vs 0.812 ClinVar comparison mixes two different trained models and two readouts with different row sets (haploid mode duplicates heterozygous records), which the authors acknowledge makes cross-mode comparison only partly interpretable. (synthesis)

## Surprising or load-bearing bits

- **"Phase in the input" ≠ "phase in the representation."** MLM leaves orientation unused because it barely helps predict masked tokens; a dedicated contrastive term is needed. This is a general lesson for any metadata token added to a DNA LM. (synthesis)
- **Dosage is the easy win, phase the hard one.** Simply giving the model zygosity (phase removed) lifts ClinVar SNV and indel scores; phase helps only on the task that cannot be solved without it.
- **Single-cell relevance.** The encoding is exactly the object a single-cell genome produces before calling — two homologues per locus — and heterozygous-site loss from [[allele-dropout]] in single-cell WGA would appear here as a false homozygous token. Whether a diploid DNA LM could be trained to flag such dropout, or to represent a somatic heterozygous variant on a known haplotype, is untested. (synthesis)

## Concepts touched

- [[dna-language-model]] — first single-stream diploid input for a nucleotide LM; continual pretraining of NTv3 with CPL.
- [[genomic-tokenization]] — unphased, ordered-phase and marker-phase tokenizers; gap-padded indel spans; 49-symbol union vocabulary.
- [[variant-effect-prediction]] — zygosity-aware ClinVar SNV/indel benchmarks and compound-heterozygous cis/trans classification.
- [[allele-dropout]] — not discussed by the paper; noted here because heterozygous-token fidelity is what single-cell allele dropout corrupts. (synthesis)

## Connections to other sources

- Backbone: [[boshar-2025-ntv3]] (Nucleotide Transformer v3); lineage [[dallatorre-2025-nucleotide-transformer]].
- Directly critiques population-level variant models: [[long-2025-mutbert]] encodes "where the genome is polymorphic rather than which two alleles a specific individual carries"; [[liu-2026-ukbiobert]] is listed with it. [[salman-2026-mendel]] (not cited) uses unordered IUPAC genotypes and drops phase, the design DNT's unphased tokenizer corresponds to. (synthesis for Mendel)
- Contrasts with [[schiff-2024-caduceus]], whose paired views are the two DNA strands, not the two homologues.
- Background models cited: [[ji-2021-dnabert]], [[zhou-2023-dnabert-2]], [[nguyen-2023-hyenadna]], [[avsec-2021-enformer]], [[linder-2025-borzoi]], [[avsec-2026-alphagenome]], [[benegas-2025-gpn-msa]], [[lin-2025-genos]].
- Physical phasing in single cells, e.g. [[strand-seq]], is the kind of haplotype-resolved input the authors call for. (synthesis)

## Open questions

- Does cis/trans discrimination hold on naturally occurring, trio- or long-read-phased compound heterozygotes?
- Can the scheme extend to hemizygous, copy-number and structural states, which matter for both clinical genetics and single-cell CNV data?
- Could a diploid DNA LM score a somatic variant in the context of the haplotype it arose on, as measured by single-cell or long-read phasing? (synthesis)

## Related

- [[dna-language-model]] · [[variant-effect-prediction]] · [[genomic-tokenization]] · [[40-Topics/sequence-models-and-foundation-models]] · [[boshar-2025-ntv3]] · [[salman-2026-mendel]] · [[long-2025-mutbert]]
