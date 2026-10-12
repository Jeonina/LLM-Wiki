---
type: concept
title: Structural variants
aliases: [SVs, large genomic rearrangements]
tags: [genome, SV, CNV, inversion, translocation, cancer]
created: 2026-05-12
updated: 2026-10-12
---

# Structural variants (SVs)

> Large (>50 bp by some definitions; >1 kb by others) genomic rearrangements — deletions, insertions, duplications, inversions, translocations, tandem repeats — that are major drivers of cancer and developmental disease and harder to detect than SNVs with short-read sequencing ([[10-Summaries/eichler-2007-completing-sv-map|HGSV 2007]]; [[10-Summaries/spielmann-2018-sv-3d-genome|Spielmann 2018]]).

> [!abstract] 한눈에
> SV는 단일 염기 치환이 아닌 모든 유전체 변화를 말하며, copy 수가 바뀌는 CNV와 copy 수가 그대로인 balanced SV(inversion, 상호 전좌 등)로 나뉜다 ([[10-Summaries/eichler-2007-completing-sv-map|HGSV 2007]]; [[10-Summaries/spielmann-2018-sv-3d-genome|Spielmann 2018]]). Single-cell에서는 WGA chimera가 가짜 접합을 만들어 SV 검출이 CNV보다 늦게 발전했고, 그래서 Strand-seq나 long-read 같은 다른 경로가 쓰인다 ([[10-Summaries/huang-2015-scwga-review|Huang 2015]]; [[10-Summaries/sanders-2020-sctrip|scTRIP]]).

## Definition

SV covers "all genomic changes that are not single base-pair substitutions" — insertions, deletions, inversions, duplications and translocations, including CNVs ([[10-Summaries/eichler-2007-completing-sv-map|HGSV 2007]]). CNV is the *unbalanced* subset; inversions, reciprocal translocations and copy-number-neutral insertions are **balanced** ([[10-Summaries/spielmann-2018-sv-3d-genome|Spielmann 2018]]).

SV classes:

- **Deletions** / **insertions** (>50 bp)
- **Duplications** (often tandem)
- **Inversions** (reversed orientation)
- **Translocations** (inter-chromosomal)
- **Mobile element insertions** (LINE-1, Alu, SVA)
- **Repeat expansions** (HD CAG, FXTAS CGG, somatic STR expansions in cancer)

## Why it matters

- SVs cause many monogenic diseases (Duchenne deletions, haemophilia A inversion, *MYC* translocations in lymphoma).
- They drive cancer (TP53 deletions, BCR-ABL fusion in CML).
- They often have a **larger functional impact per event than SNVs** but are harder to detect.
- Long-read sequencing dramatically improves SV detection sensitivity.

## Mechanisms and interpretation

- **Five phenotypic mechanisms**: gene dosage, gene disruption, fusion genes at junctions, position effects on nearby regulation, and unmasking of recessive alleles on the remaining allele ([[10-Summaries/eichler-2007-completing-sv-map|HGSV 2007]]) — the last of which is what [[10-Summaries/smukowski-heil-2023-loh|LOH]] does somatically.
- **Position relative to TAD boundaries determines pathogenicity**, not size or copy-number direction: intra-TAD SVs alter enhancer dosage, while inter-TAD SVs cause TAD fusion, neo-TAD formation or TAD shuffling ([[10-Summaries/spielmann-2018-sv-3d-genome|Spielmann 2018]]); this was causally demonstrated in [[10-Summaries/lupianez-2015-tad-disruption|Lupiáñez 2015]]. See [[30-Concepts/topologically-associating-domain]].
- **Frequency of 3D position effects is phenotype-specific**: ~7% of balanced translocations in neurodevelopmental disorders disrupt TADs, but **57%** of congenital limb-malformation CNVs act through cis-regulatory position effects ([[10-Summaries/spielmann-2018-sv-3d-genome|Spielmann 2018]]).

## Detection approaches

| Approach | Example | What it adds or misses | Source |
|---|---|---|---|
| Short-read paired-end clustering | [[10-Summaries/chen-2009-breakdancer\|BreakDancer]] | BreakDancerMax clusters anomalously mapped read pairs with a Poisson confidence score (deletions, insertions, inversions, intra- and inter-chromosomal translocations); BreakDancerMini runs a sliding-window Kolmogorov–Smirnov test on normal pairs to catch 10–100 bp indels; together they cover 10 bp–1 Mb | ([[10-Summaries/chen-2009-breakdancer\|BreakDancer]]) |
| Bulk nanopore tumour–normal | [[10-Summaries/liu-2025-nanopore-lscc-svs\|Liu 2025]]; [[30-Concepts/somagauss-sv\|SomaGauss-SV]] | Somatic SV detection in LSCC with long reads | ([[10-Summaries/liu-2025-nanopore-lscc-svs\|Liu 2025]]) |
| Template-strand inheritance (Strand-seq) | [[30-Concepts/strand-seq\|Strand-seq]], scTRIP, [[10-Summaries/weber-2023-mosaicatcher-v2\|MosaiCatcher v2]] | Haplotype-phased single-cell SVs without relying on improved amplification; MosaiCatcher v2 breakpoint resolution is limited to 100 kb by read binning, and it genotypes inversions and any other SV with at least 500 bp of uniquely mappable sequence | ([[10-Summaries/falconer-2012-natmethods\|Falconer 2012]]; [[10-Summaries/sanders-2020-sctrip\|scTRIP]]; [[10-Summaries/weber-2023-mosaicatcher-v2\|MosaiCatcher v2]]) |
| PTA with duplex validation | [[10-Summaries/luquette-2025-pta-duplex-mosaicism\|Luquette 2025]] | Chromosomal rearrangements (including TCR loci) at single-cell scale | ([[10-Summaries/luquette-2025-pta-duplex-mosaicism\|Luquette 2025]]) |
| Long-read single-cell WGS (dMDA + PacBio HiFi) | [[10-Summaries/hard-2023-long-read-scwgs\|Hård 2023]] | Many more bulk-confirmed SVs per cell than Illumina dMDA; unsuited to inversions and duplications because of intramolecular dMDA chimeras | ([[10-Summaries/hard-2023-long-read-scwgs\|Hård 2023]]) |
| Single-cell Hi-C contacts | [[10-Summaries/galasso-2026-map3c\|map3C]]; EagleC in [[10-Summaries/chang-2025-droplet-hi-c\|Droplet Hi-C]] | Contacts far from restriction cut sites, with soft-clipped junctions, flag breakpoints at 1-bp resolution; Droplet Hi-C calls SVs from CNV-corrected per-cell contact matrices | ([[10-Summaries/galasso-2026-map3c\|map3C]]; [[10-Summaries/chang-2025-droplet-hi-c\|Chang 2025]]) |
| Long reads from a single-cell Multiome library | [[10-Summaries/pancikova-2025-splongget\|SPLONGGET]]; Severus on pseudobulks | Resolves transgene integration and calls somatic SVs | ([[10-Summaries/pancikova-2025-splongget\|SPLONGGET]]) |
| Duplex sequencing | [[10-Summaries/zhang-2025-smaht-duplex-benchmark\|SMaHT duplex benchmark]] | Current duplex methods cannot detect CNVs or SVs, because chimeric-read background exceeds the true somatic SV rate; only Illumina-based duplex methods support indel calling | ([[10-Summaries/zhang-2025-smaht-duplex-benchmark\|Zhang 2025]]) |

### Why single-cell SV calling lagged single-cell CNV calling

- **Chimeras.** Chimera formation during φ29's branching amplification joins non-contiguous sequences, and this is named as the reason structural variations are difficult to observe at single-cell level, while CNVs from hundreds of kilobases to megabases are detectable relatively easily ([[10-Summaries/huang-2015-scwga-review|Huang 2015]]).
- **Chimeras as an assembly-graph problem.** [[10-Summaries/chitsaz-2011-velvet-sc|Velvet-SC]] worked around them by discarding read pairing entirely; [[10-Summaries/bankevich-2012-spades|SPAdes]] promoted chimera detection and removal to a named pipeline stage and thereby recovered the use of read pairs ([[10-Summaries/chitsaz-2011-velvet-sc|Velvet-SC]]; [[10-Summaries/bankevich-2012-spades|SPAdes]]).
- This is why [[30-Concepts/strand-seq|Strand-seq]] and scTRIP took a completely different route — template-strand inheritance rather than improved amplification — to single-cell SV detection ([[10-Summaries/falconer-2012-natmethods|Falconer 2012]]; [[10-Summaries/sanders-2020-sctrip|scTRIP]]) (synthesis).

### Sequence models and foundation models

- Orca predicts multiscale 3D effects of SVs by comparing reference and variant chromosome sequences up to 256 Mb, reproducing TAD fusion, enhancer hijacking and new-boundary insulation at PAX3/WNT6/IHH and KCNJ2–SOX9 ([[10-Summaries/zhou-2022-orca|Orca]]).
- Akita-based in-silico mutagenesis (SuPreMo) has been run on about 300,000 somatic SVs from paediatric brain tumours, including translocations ([[10-Summaries/gjoni-2026-pediatric-tumor-3d|Gjoni 2026]]).
- DNAChunker's learned tokenization stays more stable than BPE under GIAB HG002 Tier1 SVs across all size bins from <50 bp to >5 kbp, though similarity falls to about 0.3 for SVs >5 kbp ([[10-Summaries/kim-2026-dnachunker|DNAChunker]]).
- DeepGene's authors motivate pangenome-graph pretraining by the pan-genome's capture of SNPs, insertions, deletions and structural variants across individuals ([[10-Summaries/zhang-2025-deepgene|DeepGene]]).

## Evidence and examples

**Single-cell genome and Strand-seq**

- MosaiCatcher v2 detected all 10 WGS-validated copy-number-imbalanced SVs, with no false positives or false negatives ([[10-Summaries/weber-2023-mosaicatcher-v2|MosaiCatcher v2]]).
- Long-read single-cell WGS found an average of 5473 bulk-confirmed SVs per cell versus 327 in Illumina dMDA cells, with precision of 0.73 for deletions and 0.66 for insertions ([[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]).
- Nanopore sequencing of LSCC found a smoking × deletion-burden correlation and a repeat expansion regulating *TP53BP2*/*FBXO28* ([[10-Summaries/liu-2025-nanopore-lscc-svs|Liu 2025]]).

**Single-cell Hi-C**

- In 63 K562 LiMCA cells, map3C plus EagleC filtering gave 61 breakpoints, 23 matching WGS SVs (precision 0.30, recall 0.0033) ([[10-Summaries/galasso-2026-map3c|map3C]]).
- In a primary glioblastoma, Droplet Hi-C found a malignant-specific translocation that moved *IKZF1*, without its promoter, onto *EGFR* ecDNA, and *IKZF1* transcription dropped ([[10-Summaries/chang-2025-droplet-hi-c|Chang 2025]]).
- Per-cell contact features (hub index, i.e. the Gini coefficient of interchromosomal contacts; copy number; *trans*-to-*cis* ratio) separated ecDNA from homogeneously staining regions (HSRs), which aggregate Hi-C and adjnTIF could not ([[10-Summaries/chang-2025-droplet-hi-c|Chang 2025]]).

**Long-read single-cell multiome**

- SPLONGGET assembled the ~5 kb tisagenlecleucel (CTL019) CAR vector de novo with Flye from LTR-containing reads, then used supplementary alignments to place integration sites across nearly all chromosomes, consistent with a polyclonal CAR-T population ([[10-Summaries/pancikova-2025-splongget|SPLONGGET]]).
- Severus called 1,362 somatic SVs from pseudobulks of the same B-ALL samples ([[10-Summaries/pancikova-2025-splongget|SPLONGGET]]).

**Short-read bulk**

- Read-pair signal is geometrically limited: only 43.2% of 844 simulated chr17 SVs had two or more anomalous pairs at 100× physical coverage ([[10-Summaries/chen-2009-breakdancer|BreakDancer]]).
- Insertions longer than 100 bp were undetectable with 200 bp inserts and 50 bp reads ([[10-Summaries/chen-2009-breakdancer|BreakDancer]]).

## Contested points

- **Balanced SV is systematically under-ascertained.** 1–20% of all SV was estimated to be balanced and invisible to array methods ([[10-Summaries/eichler-2007-completing-sv-map|HGSV 2007]]); array CGH additionally has "low efficacy in mosaic individuals," and short-read WGS misses breakpoints in the repetitive regions where breakpoints preferentially occur ([[10-Summaries/spielmann-2018-sv-3d-genome|Spielmann 2018]]).
- **De novo SV rates are unresolved.** Estimates range 0.05–0.16 per generation, and three analyses of the same ASD dataset reached three different conclusions about non-coding SV contribution ([[10-Summaries/spielmann-2018-sv-3d-genome|Spielmann 2018]]).
- **Long-read scWGS is class-limited.** Nearly all called inversions and duplications were false positives caused by intramolecular dMDA chimeras ([[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]).
- **Chimera rate has no standard assay.** It is named as a WGA evaluation axis, but no standard assay for measuring it exists in the corpus ([[10-Summaries/huang-2015-scwga-review|Huang 2015]]) (synthesis).
- **Model predictions are unvalidated on SVs.** SuPreMo's predicted contact disruptions were not validated against tumour Hi-C ([[10-Summaries/gjoni-2026-pediatric-tumor-3d|Gjoni 2026]]); DeepGene fine-tunes every downstream task on linear sequences and reports no variant-level evaluation showing the model uses pangenome SV information ([[10-Summaries/zhang-2025-deepgene|DeepGene]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/topologically-associating-domain|Topologically associating domain]] — Self-interacting Hi-C domains whose boundaries decide whether an SV rewires regulation.
> - `concept` [[30-Concepts/strand-seq|Strand-seq]] — Single-strand sequencing that detects single-cell SVs without relying on amplification fidelity.
> - `concept` [[30-Concepts/somagauss-sv|SomaGauss-SV]] — Somatic SV workflow for tumour-vs-normal nanopore long reads.
> - `hub` [[40-Topics/somatic-mosaicism|Somatic mosaicism]] — Genetically distinct cell lineages within one individual.
> - `hub` [[40-Topics/long-read-sequencing|Long-read sequencing]] — PacBio HiFi and nanopore reads spanning kilobases or more.

## All sources on this page

> [!info]- 22 summaries cited here
> - [[10-Summaries/bankevich-2012-spades|Bankevich 2012]]
> - [[10-Summaries/chang-2025-droplet-hi-c|Chang 2025]]
> - [[10-Summaries/chen-2009-breakdancer|Chen 2009]]
> - [[10-Summaries/chitsaz-2011-velvet-sc|Chitsaz 2011]]
> - [[10-Summaries/eichler-2007-completing-sv-map|Eichler 2007]]
> - [[10-Summaries/falconer-2012-natmethods|Falconer 2012]]
> - [[10-Summaries/galasso-2026-map3c|Galasso 2026]]
> - [[10-Summaries/gjoni-2026-pediatric-tumor-3d|Gjoni 2026]]
> - [[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]
> - [[10-Summaries/huang-2015-scwga-review|Huang & Xie 2015]]
> - [[10-Summaries/kim-2026-dnachunker|DNAChunker 2026]]
> - [[10-Summaries/liu-2025-nanopore-lscc-svs|Liu 2025]]
> - [[10-Summaries/lupianez-2015-tad-disruption|Lupiáñez 2015]]
> - [[10-Summaries/luquette-2025-pta-duplex-mosaicism|Luquette 2025]]
> - [[10-Summaries/pancikova-2025-splongget|Pančíková 2025 (bioRxiv preprint)]]
> - [[10-Summaries/sanders-2020-sctrip|Sanders 2020]]
> - [[10-Summaries/smukowski-heil-2023-loh|Smukowski Heil 2023]]
> - [[10-Summaries/spielmann-2018-sv-3d-genome|Spielmann 2018]]
> - [[10-Summaries/weber-2023-mosaicatcher-v2|Weber 2023]]
> - [[10-Summaries/zhang-2025-deepgene|DeepGene 2025]]
> - [[10-Summaries/zhang-2025-smaht-duplex-benchmark|Zhang 2025]]
> - [[10-Summaries/zhou-2022-orca|Orca 2022]]
