---
type: summary
title: "Spix et al. 2025 — High-coverage allele-resolved single-cell DNA methylation profiling reveals cell lineage, X-inactivation state, and replication dynamics"
source: "[[00-Sources/papers/High-coverage allele-resolved single-cell DNA methylation profiling reveals cell lineage, X-inactivation state, and replication dynamics]]"
source_quality: full
source_sha256: "7bc201f6a285a25f95288da5847f738314fcb7afc62f71d5c37c9259d5099523"
source_kind: paper
author: "Nathan J. Spix, Walid Abi Habib, Zhouwei Zhang, Emily Eugster, Hsiao-yun Milliron, David Sokol, KwangHo Lee, Paula A. Nolte, Jamie L. Endicott, Kelly F. Krzyzanowski, Toshinori Hinoue, Jacob Morrison, Benjamin K. Johnson, Wanding Zhou, Hui Shen, Peter W. Laird (corresponding)"
published: 2025-07-08
ingested: 2026-10-07
doi: "10.1038/s41467-025-61589-1"
journal: "Nature Communications 16:6273"
tags: [scDEEP-mC, scWGBS, PBAT, random-priming, allele-resolved-methylation, hemi-methylation, X-inactivation, replication, S-phase, maintenance-methylation, NMF, BISCUIT, solo-WCGW, copy-number]
entities: []
concepts: ["[[bisulfite-sequencing]]", "[[scbs-seq]]", "[[allele-specific-methylation]]", "[[replication-timing]]", "[[cpg-island]]", "[[uhrf1]]", "[[dnmt]]", "[[copy-number-variation]]", "[[doublet-detection]]", "[[cell-type-annotation]]"]
topics: ["[[dna-methylation]]"]
---

**Citation:** Spix et al. (2025) — *High-coverage allele-resolved single-cell DNA methylation profiling reveals cell lineage, X-inactivation state, and replication dynamics* — *Nature Communications* 16:6273. [DOI](https://doi.org/10.1038/s41467-025-61589-1)

# Spix 2025 — scDEEP-mC

> Most scWGBS methods trade per-cell coverage for throughput, forcing analysts into large bins, clustering or imputation. **scDEEP-mC** (Laird lab) goes the other way: a plate-based PBAT protocol tuned for library complexity — cells sorted straight into bisulfite reagent (no post-conversion cleanup loss), seven rounds of first-strand random priming with **base-composition-matched nonamers** (built for the bisulfite-converted genome, G only in CpG context), exonuclease cleanup, and directional second-strand priming — reaching **~30% of CpGs at 20 M reads/cell**. That coverage makes per-cell, per-allele, per-strand calls possible: **hemi-methylation**, **X-inactivation state** (even without phased SNPs, via NMF), and **S-phase cells** identified from copy number plus allele-resolved discordance.

## Key claims

- **Highest sequencing efficiency of the methods compared** — scDEEP-mC vs public high-coverage scWGBS datasets (scBS-seq, scM&T-seq, scTrio-seq, PBAL, snmC-seq2, Cabernet), all reprocessed through one BISCUIT pipeline with 2 M reads subsampled per library: minimal adapter contamination, very high alignment rates, reduced GC bias vs other random-priming methods. snmC-seq2 is comparably efficient but its low library yield limits depth; Cabernet (tagmentation + enzymatic conversion) reaches comparable coverage but showed incomplete CpY conversion in 43% (human) and 49% (mouse) of reads.
- **Interpretable cell typing in primary tissue** (mouse intestinal epithelium): mean beta over 50,286 cell-type-specific hypomethylated regions (lifted over from Loyfer et al.'s human atlas) assigns epithelial vs immune cells and flags doublets; promoter-level hierarchical clustering resolves mature vs less-differentiated enterocytes (e.g. *Abcg5* vs *Nkx1-2*/*Satb2* promoters unmethylated) and T vs B cells (*Itk*/*Cd3* vs *Blnk*); rank-2 NMF on raw betas of the 75% most variable CpGs recovers the same groups plus doublets and putative G2 cells.
- **Allele-resolved methylation (ARM) without custom references**: a bisulfite-aware Nextflow pipeline phases reads by within-read heterozygous SNPs (discovered de novo or supplied). De novo SNPs: precision 93.5% / recall 67.4% vs the Mouse Genome Project; read assignment on synthetic data: precision 99.97%, recall 76.8%. ~1 million allele-resolved CpGs per cell, ~10,000 with both strands covered; one cell defines all three DMRs on both alleles of imprinted *Gnas*.
- **Hemi-methylation at TF sites**: *Cdx2* sites more hemi-methylated than expected in epithelial cells, *Gata3* in immune cells, and *Sox2* sites relatively high in epithelium — noted against prior evidence that SOX2 demethylates by inhibiting maintenance of hemi-methylated DNA.
- **Maintenance lags at late-replicating DNA**: across 13 replication-timing partitions, early-passage fibroblasts show more hemi-methylation in late-replicating loci; very-late-passage (TERT-immortalised) cells show substantial methylation loss there, and both retain proportional hemi-methylation enrichment.
- **Replicating cells found without BrdU/EdU**: fraction of reads in early-replicating regions + ARM discordance separates G1, S, putative G2 and doublets (discordance >3%). In S-phase, newly 4n regions carry high intermediate methylation that declines as replication proceeds; in G2, it is lower but still above G1.
- **X-inactivation per cell**: in a C57BL/6 × BALB/c F1 female, allele-specific CGI methylation calls Xa/Xi per cell; only CGIs near *Xist* and *Dxz4* were methylated on Xa and unmethylated on Xi; *Nap1l3* (an escapee) was unmethylated on both. **Rank-2 NMF without phased SNPs** recovered cell groups and alleles matching ground truth (R² = 0.99).
- **Culture drift, not Xi loss**: in serially passaged female human fibroblasts, ARM variance on chrX collapsed with passage; NMF alleles showed late-passage cells mostly methylated on one allele and very-late-passage cells on the other, both alleles present and no chrX loss by copy number — interpreted as drift toward one X-inactivation state. Very-late passage also harboured chr8 and chr10q deletion subclones with differing solo-WCGW methylation (replicative history).

## Methods / evidence

Cells: 175 mouse intestinal (8-week CB6F1/J female, FACS on CD45.2/EpCAM) and 292 human fibroblasts (AG06561; early, late, TERT-immortalised very late passage), sorted into 3 µL Zymo CT conversion reagent in 96-well plates. Sequencing ~30–35 M 150 bp PE reads/cell (limited returns above 35 M). Processing: cutadapt, BISCUIT directional alignment, dupsifter, removal of reads with >1 CpY retention and MAPQ <40, removal of anomalously high-coverage regions.

Weight: a strong technical paper — the cross-method comparison reprocesses all public data uniformly and subsamples to equal depth, which is unusually fair. Biological demonstrations are proof-of-concept on small cell numbers (hundreds), one mouse and one fibroblast line; the X-inactivation "drift" interpretation is inferred from cultures not directly descended from each other (the authors note this).

## Surprising or load-bearing bits

- **Coverage changes the analytical regime**: at ~30% CpGs per cell, individual promoters and imprinted DMRs are readable in one cell, so the cluster/bin/impute workflow becomes optional rather than mandatory (synthesis).
- **Replication state is a confounder hiding in every scWGBS dataset**: S/G2 cells carry transient intermediate methylation from not-yet-maintained daughter strands; at low coverage this would look like epigenetic heterogeneity (synthesis).
- **Doublet signatures are methylation-native**: high ARM discordance and intermediate allele-specific X methylation flag doublets without genotype mixing.
- **Primer design trade-off**: nonamers assume CpH is unmethylated, which could bias against high-mCH regions (e.g. neurons) — though mCH calls themselves remain accurate since only nine bases per read come from the primer.

## Concepts touched

- [[allele-specific-methylation]] — extends ASM to single cells from short-read bisulfite data, including strand-resolved hemi-methylation and SNP-free X-allele inference.
- [[replication-timing]] — copy-number read skew toward early-replicating regions identifies S-phase cells; late replication links to incomplete remethylation.
- [[uhrf1]] / [[dnmt]] — maintenance methylation dynamics observed directly in unperturbed single replicating cells (synthesis: the hemi-methylated intermediate these enzymes resolve).
- [[scbs-seq]] — scDEEP-mC is a PBAT descendant that removes the post-bisulfite cleanup and redesigns priming.
- [[doublet-detection]] — methylation discordance as a doublet metric.

## Connections to other sources

- PBAT/scBS-seq lineage it improves on and benchmarks against: [[smallwood-2014-natmethods]], [[clark-2017-scbs-seq-protocol]]; scTrio-seq [[hou-2016-sctrio-seq]]; snmC-seq2 [[luo-2018-snmc-seq2]] (scM&T-seq, PBAL and Cabernet have no wiki summaries).
- Allele-aware bisulfite calling, earlier tooling with Laird as co-author: [[liu-2012-bis-snp]] (Bis-SNP genotypes SNPs from bisulfite reads; scDEEP-mC instead phases reads by within-read SNPs without a custom reference) (synthesis).
- Methylation-based clonal/lineage reasoning that would benefit from per-cell coverage: [[chen-2025-methyltree]], [[scherer-2025-nature]], [[gabbutt-2025-evoflux]].
- Contrast with the throughput-first, window-aggregating route: [[nichols-2022-scimet-v2]], [[rylaarsdam-2025-amethyst]]; and with imputation as a sparsity fix: [[liang-2026-scmeth-imputation-benchmark]].
- Copy number from single-cell reads, as in scDNA-seq CNV callers: [[copy-number-variation]].

## Open questions

- Throughput is plate-limited (hundreds of cells) and deep sequencing per cell is costly; whether miniaturisation preserves complexity is untested.
- Hemi-methylation enrichment at TF sites is reported per cell group but without functional follow-up; how much of it is S/G2 contamination vs stable asymmetric methylation is not separated (synthesis).
- SNP-free NMF X-inference was validated on one F1 mouse with known phasing; performance in outbred human tissue with mosaic X-skewing is untested.

## Related

- [[allele-specific-methylation]] · [[replication-timing]] · [[smallwood-2014-natmethods]] · [[40-Topics/dna-methylation]]
