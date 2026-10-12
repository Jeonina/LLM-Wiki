---
type: concept
title: scNMT-seq
aliases: [scNMT-seq, single-cell nucleosome methylation transcription sequencing]
tags: [joint-assay, single-cell-multiomics, triple-omics, dna-methylation, chromatin-accessibility, NOMe-seq, method]
created: 2026-05-12
updated: 2026-10-12
---

# scNMT-seq

> First single-cell triple-omics assay that simultaneously profiles **chromatin accessibility + DNA methylation + transcriptome** in the same cell. Uses NOMe-seq chemistry (GpC methyltransferase M.CviPI labels accessible DNA) over a [[gt-seq|G&T-seq]]-style physical DNA/RNA separation ([[10-Summaries/clark-2018-scnmt-seq|Clark 2018]]).

> [!abstract] 한눈에
> scNMT-seq는 NOMe-seq 화학과 G&T-seq식 DNA/RNA 분리를 결합해 한 세포에서 chromatin accessibility, DNA methylation, transcriptome을 함께 읽은 첫 triple-omics assay다 ([[10-Summaries/clark-2018-scnmt-seq|Clark 2018]]). 처리량이 낮고 G-C-G·C-C-G 위치를 버려야 한다는 점이 주된 한계다 ([[10-Summaries/clark-2018-scnmt-seq|Clark 2018]]).

## Definition

Clark et al. 2018 ([[10-Summaries/clark-2018-scnmt-seq|Clark 2018]]):

- The cell is lysed in M.CviPI buffer (15 min, 37°C); GpC sites in accessible DNA are methylated while endogenous CpG methylation is preserved ([[10-Summaries/clark-2018-scnmt-seq|Clark 2018]]).
- RNA is separated via biotinylated oligo-dT beads (G&T-seq mechanism) and processed by Smart-seq2 ([[10-Summaries/clark-2018-scnmt-seq|Clark 2018]]).
- The remaining DNA is bisulfite-converted (scBS-seq) ([[10-Summaries/clark-2018-scnmt-seq|Clark 2018]]).
- After alignment, A-C-G/T-C-G positions report endogenous CpG methylation; G-C-A/C/T positions report GpC accessibility; G-C-G and C-C-G positions are discarded ([[10-Summaries/clark-2018-scnmt-seq|Clark 2018]]).

## Why it matters

- **First parallel profiling of three molecular layers per cell** — establishes a reference design for any triple-omics extension ([[10-Summaries/clark-2018-scnmt-seq|Clark 2018]]).
- **GpC accessibility coverage (~15%) exceeds scATAC-seq (~9.4%)** with single-GpC-site (~1/16 bp) resolution ([[10-Summaries/clark-2018-scnmt-seq|Clark 2018]]).

## Variants and successors

| Assay | What it adds or changes | Source |
|---|---|---|
| **scNMT-seq** | Accessibility + methylation + RNA from one cell | ([[10-Summaries/clark-2018-scnmt-seq\|Clark 2018]]) |
| Camellia-seq | Also captures expressed lineage-barcode transcripts from the cytoplasmic fraction (modified STRT-seq) while the nucleus undergoes GpC methyltransferase treatment and scBS-seq | ([[10-Summaries/li-2023-darlin\|Li 2023]]) |
| [[scchix-seq]], [[multi-tag]] | Conceptual successors that add a chromatin-modification layer | (synthesis) |
| [[splicool-seq]] | Lineage cousin in DNA-methylation + accessibility space, scaled to larger throughput | (synthesis) |

## Evidence and examples

- Nucleosome positions are visible from the 180–200 bp oscillation in single-cell profiles ([[10-Summaries/clark-2018-scnmt-seq|Clark 2018]]).
- **Coupling between methylation and accessibility strengthens along the ESC → embryoid body pseudotime trajectory** — a single-cell observation about epigenetic-layer coupling dynamics that bulk cannot resolve ([[10-Summaries/clark-2018-scnmt-seq|Clark 2018]]).
- Bivalent (H3K4me3 + H3K27me3) promoters show heterogeneous accessibility clusters and are associated with low expression levels ([[10-Summaries/clark-2018-scnmt-seq|Clark 2018]]).
- In HSCs, Camellia-seq covered ~70% of promoters and ~90% of gene bodies and gave ~100,000 UMIs from ~3,000 genes per cell ([[10-Summaries/li-2023-darlin|Li 2023]]).
- The scNMT-seq mouse gastrulation data (E4.5–E7.5) were used to fit and benchmark mist, which found higher methylation dispersion in early than late pseudotime stages and 3,927 differentially methylated genes not shared with GAM or polynomial regression ([[10-Summaries/duan-2026-mist|mist]]).

## Contested points

- Throughput is limited (61 + 40 cells in the original paper); subsequent split-pool / combinatorial methods scale higher but typically drop one layer ([[10-Summaries/clark-2018-scnmt-seq|Clark 2018]]).
- Camellia-seq, the lineage-barcode extension, is plate-based, low-throughput and costly ([[10-Summaries/li-2023-darlin|Li 2023]]).
- scNMT-seq requires discarding G-C-G and C-C-G positions (~48% of CpG sites genome-wide) — a fundamental NOMe-seq trade-off ([[10-Summaries/clark-2018-scnmt-seq|Clark 2018]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/nome-seq|NOMe-seq]] — GpC methyltransferase footprinting of accessible DNA, read with bisulfite.
> - `concept` [[30-Concepts/scbs-seq|scBS-seq]] — Single-cell bisulfite sequencing, the methylation arm of scNMT-seq.
> - `concept` [[30-Concepts/gt-seq|G&T-seq]] — Physical separation of genome and transcriptome from one cell.
> - `concept` [[30-Concepts/bisulfite-sequencing|Bisulfite sequencing]] — Conversion chemistry that reads 5mC as C and unmethylated C as T.
> - `concept` [[30-Concepts/chromatin-accessibility|Chromatin accessibility]] — How open DNA is to binding proteins and enzymes.
> - `entity` [[20-Entities/heather-lee|Heather Lee]] — Co-author of scNMT-seq.
> - `hub` [[40-Topics/dna-methylation|DNA methylation]] — Methylation chemistry, assays and analysis.
> - `hub` [[40-Topics/single-cell-multiomics|Single-cell multiomics]] — Joint measurement of several layers in one cell.

## All sources on this page

> [!info]- 3 summaries cited here
> - [[10-Summaries/clark-2018-scnmt-seq|Clark 2018]]
> - [[10-Summaries/duan-2026-mist|Duan 2026]]
> - [[10-Summaries/li-2023-darlin|Li 2023]]
