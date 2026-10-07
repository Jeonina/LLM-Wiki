---
type: concept
title: scNMT-seq
aliases: [scNMT-seq, single-cell nucleosome methylation transcription sequencing]
tags: [joint-assay, single-cell-multiomics, triple-omics, dna-methylation, chromatin-accessibility, NOMe-seq, method]
created: 2026-05-12
updated: 2026-10-07
---

# scNMT-seq

> First single-cell triple-omics assay that simultaneously profiles **chromatin accessibility + DNA methylation + transcriptome** in the same cell. Uses NOMe-seq chemistry (GpC methyltransferase M.CviPI labels accessible DNA) over a [[gt-seq|G&T-seq]]-style physical DNA/RNA separation.

## Definition

Clark et al. 2018 ([[10-Summaries/clark-2018-scnmt-seq]]). Cell is lysed in M.CviPI buffer (15 min, 37°C); GpC sites in accessible DNA are methylated while endogenous CpG methylation is preserved. RNA is separated via biotinylated oligo-dT beads (G&T-seq mechanism) and processed by Smart-seq2. The remaining DNA is bisulfite-converted (scBS-seq). After alignment, A-C-G/T-C-G positions report endogenous CpG methylation; G-C-A/C/T positions report GpC accessibility; G-C-G and C-C-G positions are discarded.

## Why it matters

- **First parallel profiling of three molecular layers per cell** — establishes a reference design for any triple-omics extension.
- **GpC accessibility coverage (~15%) exceeds scATAC-seq (~9.4%)** with single-GpC-site (~1/16 bp) resolution; nucleosome positions visible from 180–200 bp oscillation in single-cell profiles.
- **Coupling between methylation and accessibility strengthens along the ESC → embryoid body pseudotime trajectory** — a single-cell observation about epigenetic-layer coupling dynamics that bulk cannot resolve.
- Bivalent (H3K4me3 + H3K27me3) promoters show heterogeneous accessibility clusters and are associated with low expression levels ([[10-Summaries/clark-2018-scnmt-seq]]).

## Variants and refinements

- **scNMT-seq** ([[10-Summaries/clark-2018-scnmt-seq]]).
- Conceptual successors that add a chromatin-modification layer: [[scchix-seq]], [[multi-tag]].
- Lineage cousin in DNA-methylation + accessibility space: [[splicool-seq]] (scaled, larger-throughput).

## Contested points

- Throughput limited (61 + 40 cells in the original paper); subsequent split-pool / combinatorial methods scale higher but typically drop one layer.
- Requires discarding G-C-G and C-C-G positions (~48% of CpG sites genome-wide) — a fundamental NOMe-seq trade-off.

## Added 2026-10-07

Camellia-seq extends scNMT-seq by also capturing expressed lineage-barcode transcripts from the cytoplasmic fraction (modified STRT-seq) while the nucleus undergoes GpC methyltransferase treatment and scBS-seq; in HSCs it covered ~70% of promoters and ~90% of gene bodies and gave ~100,000 UMIs from ~3,000 genes per cell [[10-Summaries/li-2023-darlin]]. It is plate-based, low-throughput and costly [[10-Summaries/li-2023-darlin]].

The scNMT-seq mouse gastrulation data (E4.5–E7.5) were used to fit and benchmark mist, which found higher methylation dispersion in early than late pseudotime stages and 3,927 differentially methylated genes not shared with GAM or polynomial regression ([[10-Summaries/duan-2026-mist]]).


## Related

- [[bisulfite-sequencing]]
- [[nome-seq]]
- [[scbs-seq]]
- [[chromatin-accessibility]]
- [[40-Topics/dna-methylation]]
- [[40-Topics/single-cell-multiomics]]
- [[gt-seq]]
- [[20-Entities/heather-lee]]
- [[40-Topics/single-cell-multiomics]]
- [[40-Topics/dna-methylation]]
