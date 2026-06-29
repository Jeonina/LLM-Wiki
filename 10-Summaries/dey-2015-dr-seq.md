---
type: summary
title: "Dey 2015 — DR-seq: Integrated genome and transcriptome sequencing of the same cell"
source: "[[00-Sources/papers/Integrated genome and transcriptome sequencing of the same cell]]"
aliases: [Dey 2015, DR-seq, gDNA-mRNA sequencing]
tags: [DR-seq, joint-assay, single-cell-multiomics, scDNA, scRNA-seq, quasilinear-amplification]
created: 2026-05-12
updated: 2026-05-12
---

**Citation:** Dey et al. (2015) — *DR-seq: Integrated genome and transcriptome sequencing of the same cell* — *?*. [DOI](https://doi.org/10.1038/nbt.3129)

# Dey et al. 2015 — DR-seq

> Siddharth S Dey, Lennart Kester, Bastiaan Spanjaard, Magda Bienko, Alexander van Oudenaarden. *Nature Biotechnology* **33**, 285–289 (March 2015). DOI: 10.1038/nbt.3129. (Same issue family as [[10-Summaries/macaulay-2015-gt-seq|G&T-seq]] — the two were published two months apart.)

## Thesis

DR-seq is the **one-pot** alternative to G&T-seq for joint single-cell DNA + RNA sequencing. It avoids physical separation of nucleic acids before amplification by performing **quasilinear whole-genome amplification (MALBAC-style)** on a cell whose mRNA has first been reverse-transcribed to single-stranded cDNA. The sample is split *after* the initial amplification — one half goes to IVT/RNA-seq, the other to PCR/DNA-seq. The trade-off: simpler workflow with less material loss, but DNA sequencing must computationally mask coding regions (because cDNA-derived amplicons contaminate the DNA pool there).

## Mechanism

1. Lyse single cell with poly-T primer carrying cell-barcode + 5′ Illumina adaptor + T7 promoter (Ad-1x).
2. Reverse-transcribe mRNA in situ.
3. **Seven rounds of quasilinear amplification** with Ad-2 (random 8-mer adaptor): amplifies BOTH gDNA and ssDNA cDNA simultaneously. Most amplicons carry Ad-2 on both ends; cDNA-derived amplicons carry Ad-2 on one end and Ad-1x on the other.
4. Split: half → IVT-based mRNA library (only cDNA-derived molecules are transcribed by T7); half → PCR amplification, sonication, and gDNA library prep.
5. Bioinformatics: gDNA reads computationally **masked to exclude coding sequences** before CNV calling, since reads from coding regions could come from either gDNA or cDNA.

## Key claims

- **E14 mouse ESCs benchmark**: 13 single cells; mRNA results comparable to CEL-seq (9,735 shared genes detected; similar ERCC spike-in dynamic range over 3 orders of magnitude).
- **Length-based identifiers (LBIs)** introduced: because quasilinear amplification primes cDNA randomly, the genomic priming position of the first Ad-2 amplicon serves as a UMI surrogate. Reduces CV of endogenous-gene expression for ~80% of genes, matching the noise reduction CEL-seq achieves with random-sequence UMIs.
- **SK-BR-3 breast cancer cells**: 21 single cells profiled, 12,205 genes detected, 7 with paired gDNA. **DR-seq CNV calls match bulk and DNA FISH** across loci spanning a copy-number spectrum (Kolmogorov–Smirnov test not different from FISH at *P* > 0.01).
- **Strong DNA copy number → gene expression correlation** (monotonic increase) genome-wide in single cells.
- **Inverse relationship between expression variability and copy number**: high-CV genes tend to sit on low-copy regions; high-copy regions buffer expression noise. Argued as evidence that **CNVs may drive expression-level variability between single cells**.

## Limitations the paper acknowledges

- Coding-region masking is necessary (small fraction of genome, but limits SNV detection in coding regions from gDNA half).
- RNA reads are biased toward the 3′ end (CEL-seq-like), unlike G&T-seq's full-length Smart-seq2 coverage.
- Quasilinear amplification GC bias slightly higher than MALBAC alone.

## Surprising / load-bearing

- The paper closes with explicit **forecasting of methylation+transcriptome and nucleosome+transcriptome single-cell coassays** — published Feb 2015, this is on the leading edge of the joint-assay wave that scNMT-seq (Feb 2018), sci-CAR (Aug 2018), and SHARE-seq (2020) would build on.
- For §4.6 coverage: DR-seq is the **one-pot foundational alternative** to G&T-seq, methodologically distinct. The pair (DR-seq vs G&T-seq) is the canonical fork in joint-assay design — one-pot simplicity vs separation flexibility.

## Entities / concepts touched

[[30-Concepts/scdna-seq]] · [[scwga]] · [[malbac]] · [[umi-molecular-barcoding]] · [[30-Concepts/single-cell-multiomics]] · [[20-Entities/alexander-van-oudenaarden]] · [[40-Topics/single-cell-multiomics]] · [[40-Topics/whole-genome-amplification]]

## Related summaries

- [[10-Summaries/macaulay-2015-gt-seq]] — separation-based contemporaneous alternative.
- [[10-Summaries/hou-2016-sctrio-seq]] — scTrio-seq, conceptual successor.

---
**Source:** [Open paper](https://www.nature.com/articles/nbt.3129)
