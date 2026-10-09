---
type: summary
title: "Salman et al. 2026 — Mendel, a foundation model of human genetic variation, prioritizes regulatory variants and improves gene expression prediction"
source: "[[00-Sources/papers/Mendel, a foundation model of human genetic variation, prioritizes regulatory variants and improves gene expression prediction.pdf]]"
source_quality: full
source_sha256: "782bd8c323c4707055a68e78bbb1917af1729c344e01bdc08755dfe1b4d33ad7"
source_kind: paper
author: "Arham Salman, Haonan Feng, Peng Wei, Ryan Sun, Lang Wu, Wei Pan (corresponding), Chong Wu (corresponding)"
published: 2026-09-30
ingested: 2026-10-08
doi: "10.64898/2026.09.28.755183"
journal: "bioRxiv preprint"
tags: [Mendel, DNA-language-model, variant-centric, diploid-genotype, IUPAC-encoding, StripedHyena2, Evo-2, GTEx, WGS, cis-eQTL, fine-mapping, residual-difficulty, elastic-net, TWAS, sQTL, paQTL, preprint]
entities: []
concepts: ["[[dna-language-model]]", "[[variant-effect-prediction]]", "[[genomic-tokenization]]", "[[sequence-to-function-model]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]"]
---

**Citation:** Salman et al. (2026) — *Mendel, a foundation model of human genetic variation, prioritizes regulatory variants and improves gene expression prediction* — bioRxiv preprint, posted 2026-09-30. [DOI](https://doi.org/10.64898/2026.09.28.755183)

# Salman 2026 — Mendel

> Mendel is a 1 B-parameter StripedHyena2 model (Evo 2's architecture and byte tokenizer, 8,192-bp context) trained **from scratch** on GTEx v8 whole genomes with a **variant-centric objective**: each donor's diploid SNV genotype is written as one IUPAC ambiguity code (R = A/G, Y = C/T, …) between `^` and `&` markers inside reference-aligned sequence, and next-token loss is computed **only** on the genotype tokens. Batches draw the same locus from eight different donors ("locus-contrastive" sampling). One model per autosome, trained on 670 donors and tested on 85 held-out donors. Mendel recovers held-out genotypes at cohort-defined variant sites with 0.984 accuracy (Evo 2: 0.311), but the paper's real argument is about the **residual errors**: sites Mendel finds hard to predict are enriched for fine-mapped cis-eQTLs (AUROC 0.731 vs 0.545 for Evo 2 residuals), and using residual difficulty as an elastic-net penalty prior improves cis-expression prediction in all 50 GTEx tissues and beats a CADD-Phred prior in 49 of 50.

## Key claims

- **Genotype prediction.** Micro-averaged allele-prediction accuracy 0.984 vs 0.311 for Evo 2 (released 1 B checkpoint); site-macro 0.983 vs 0.311. Mendel beats Evo 2 in all 85 held-out donors and on every chromosome (0.95–0.99 vs 0.30–0.36). By MAF: rare 0.99 vs 0.31, low-frequency 0.97 vs 0.31, common 0.94 vs 0.29.
- **But accuracy is mostly the major allele.** Heterozygote allele-overlap rises from ~0.50 (rare) to 0.62 (low-frequency) to 0.92 (common). A model-free "two copies of the major allele" reference scores 1.0 / 0.5 / 0 on homozygous-major / heterozygous / homozygous-minor genotypes, so high rare-bin accuracy does not mean rare genotypes are recovered.
- **Residual difficulty marks regulatory variants.** Mean hard miscall (0–2 mismatched alleles, averaged over held-out donors): cis-eQTLs (PIP ≥ 0.9, Borzoi benchmark) mean 0.22, MAF- and TSS-matched low-PIP controls 0.12, random background 0.04. Under Evo 2 all three groups sit near 2.0 (means 1.56, 1.53, 1.55). Enrichment persists within MAF and TSS-distance strata and extends to sQTLs, paQTLs and ipaQTLs against Borzoi's released controls.
- **Prioritisation.** A random forest on 11 residual features separates high-PIP cis-eQTLs from matched controls with AUROC 0.731 / AP 0.682 (Evo 2: 0.545 / 0.523). Adding MAF, TSS distance and chromosome barely helps. Performance with only 8 donors (~0.74 AUROC) matches all 85.
- **Effect size vs PIP.** Residual difficulty correlates negatively with |eQTL effect size| (ρ = −0.308, n = 883) but positively with fine-mapping PIP (ρ = 0.156, n = 1,633); the authors read this as tracking fine-mapping evidence rather than effect magnitude.
- **Expression prediction.** Rank-based elastic-net penalty factors (less shrinkage for harder variants) raised mean squared CV Pearson r over an unweighted baseline in all 50 tissues (median relative gain 3.93%), gave more FDR-significant genes in 45 tissues, and beat CADD-Phred (via FAVOR) weighting in 49 of 50. In Colon Transverse, 35 of 39 genes improved (median Δr² = 0.0079).

## Methods / evidence

Data: SHAPEIT2-phased GTEx v8 WGS, 838 donors, GRCh38; a locus is a variant if any donor carries a non-reference allele, and that catalogue is marked in every donor's sequence. IUPAC encoding is unordered, so **phase is discarded** even though the input was phased. Donors split 80/10/10 (seed 42). Windows: 8,192 tokens, stride 4,096, kept only if they contain a variant event. Architecture: 25 layers, hidden 1,920, 15 heads, Evo 2 operator pattern; random init. Training per chromosome (chr1–22) on 4 H100s, global batch 8 windows, up to 200,000 steps (most chromosomes stopped at 50,000–155,000). Evaluation: up to 10,000 single-SNV events per donor per chromosome, scored with ≥ 4,096 tokens of preceding context; Mendel restricted to ten diploid symbols, Evo 2 to A/C/G/T read as homozygous calls. Residual scores use one window centred on each variant per donor. cis-eQTL matching: greedy nearest-neighbour on MAF and log TSS distance with a 0.05 MAF caliper (932 Mendel pairs). Expression models: 110 random genes (5 per chromosome), 105 evaluable, 4,896 gene–tissue pairs, nested 5×5 CV repeated five times, GTEx v10 residual expression.

Several P-value exponents and the Adam β/ε and peak learning-rate values were lost in PDF text extraction; Figures 2 and 4 are only partly legible (Figure 3 values match the text). Code is available on request, not public.

## Limitations

**Authors' own:**
- One model per chromosome for compute reasons; no trans-chromosomal inference.
- Evaluation is at variant loci ascertained in the full cohort, so generalisation to unseen loci is untested; prioritisation used random variant-level folds, and locus- or LD-block-held-out evaluation is still needed. Variant-level tests and bootstraps ignore LD.
- GTEx ancestry composition does not reflect global diversity; All of Us, Pan-UK Biobank and Million Veteran Program are named as next cohorts.
- Rare heterozygotes are recovered poorly but barely affect micro-averaged accuracy; up-weighting them is suggested.
- Training and inference are compute-heavy, which limited hyperparameter tuning.
- Train and test donors share population structure, so Mendel could succeed by learning the common allele and using LD proxies; the three downstream analyses are offered as evidence the residuals carry more than that.

**Reviewer notes:**
- The Evo 2 comparison is not like-for-like: Evo 2 was never trained to emit diploid IUPAC symbols and can at best score 0.5 at heterozygous sites, so the 0.984 vs 0.311 headline mostly shows task mismatch, not a better genome model. (synthesis)
- Residual difficulty rises strongly with MAF (ρ = 0.603); matching controls on MAF addresses this, but the expression prior is applied without such matching, so part of the gain could come from up-weighting common variants that carry more eQTL signal. (synthesis)
- Germline-only by design: the model learns which genotypes are expected at known polymorphic sites given local context. A somatic mutation at a non-catalogued site has no `^…&` slot at all, so Mendel as built cannot score it. (synthesis)

## Surprising or load-bearing bits

- **The useful output is the model's failure.** Variants that a population-trained model cannot predict from local haplotype context are the ones fine-mapping calls causal. One reading is that causal regulatory variants are less tightly tagged by local LD patterns, though the paper does not test this. (synthesis)
- **IUPAC codes as a diploid tokenizer.** Writing a genotype as one standard ambiguity symbol needs no vocabulary change and keeps sequence length fixed. The same trick appears in [[li-2025-bmfm-dna]] with custom characters. (synthesis)
- **Phase deliberately discarded.** Mendel reads phased data but encodes unordered genotypes; [[leib-2026-dnt]] takes the opposite route and models both haplotypes. (synthesis)
- **Sequence-to-variation vs sequence-to-function.** The authors position Mendel as complementary to Enformer, Borzoi and AlphaGenome: those predict a variant's effect, Mendel scores how unusual it is within local population variation.

## Concepts touched

- [[dna-language-model]] — variant-centric, loss-masked training on personal genomes; contrasts with dense reference-wide objectives.
- [[variant-effect-prediction]] — residual difficulty as an annotation-free signal for cis-eQTL, sQTL and paQTL prioritisation.
- [[genomic-tokenization]] — IUPAC diploid genotype tokens with boundary markers inside a byte-level vocabulary.
- [[sequence-to-function-model]] — Borzoi QTL benchmarks reused; framed as complementary information to track-prediction models.

## Connections to other sources

- Uses the QTL benchmark sets released with [[linder-2025-borzoi]]; positions itself against [[avsec-2021-enformer]] and [[avsec-2026-alphagenome]].
- Cites the reference-trained DNA LM line ([[ji-2021-dnabert]], [[dallatorre-2025-nucleotide-transformer]], [[nguyen-2023-hyenadna]], [[schiff-2024-caduceus]]) and early sequence-to-function models ([[zhou-2015-deepsea]], [[kelley-2016-basset]], [[kelley-2018-basenji]], [[chen-2022-sei]]).
- Other population-aware designs: [[long-2025-mutbert]] (allele-frequency inputs), [[li-2025-bmfm-dna]] (dbSNP-encoded symbols), [[liu-2026-ukbiobert]] (biobank variants), [[leib-2026-dnt]] (diploid haplotypes). [[benegas-2025-gpn-msa]] named population variation as its next step. (synthesis)

## Open questions

- Does residual-difficulty enrichment hold under LD-block- or chromosome-held-out evaluation, and at loci not in the training catalogue?
- Is residual difficulty mostly a measure of how poorly a variant is tagged by nearby variants? A direct comparison with LD scores would separate these explanations. (synthesis)
- Could a variant-centric objective be adapted to somatic data, e.g. predicting which cells in a single-cell genome dataset carry a mosaic allele, where the "population" is the cells of one person? (synthesis)

## Related

- [[dna-language-model]] · [[variant-effect-prediction]] · [[genomic-tokenization]] · [[40-Topics/sequence-models-and-foundation-models]] · [[linder-2025-borzoi]] · [[leib-2026-dnt]]
