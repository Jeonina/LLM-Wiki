---
type: summary
title: "Tang 2009 — mRNA-Seq whole-transcriptome analysis of a single cell"
aliases: ["Tang 2009", "Tang mRNA-Seq 2009", "first scRNA-seq"]
tags: [scRNA-seq, mRNA-Seq, founding-method, single-cell-transcriptomics, blastomere, Surani-lab, Gurdon-Institute]
created: 2026-05-14
updated: 2026-05-14
sources: ["Tang_2009_NatureMethods.md"]
---

**Citation:** Tang et al. (2009) — *mRNA-Seq whole-transcriptome analysis of a single cell* — *Nature Methods*. [DOI](https://doi.org/10.1038/nmeth.1315)

Tang, Barbacioru, Wang et al. (Surani lab, Gurdon Institute, Cambridge) reported the **first whole-transcriptome mRNA-Seq from a single mammalian cell** ([DOI](https://doi.org/10.1038/nmeth.1315)). Using a single mouse blastomere as input, they amplified poly-A mRNA via a SMART-style template-switching cDNA synthesis followed by PCR, then performed digital gene expression profiling on the SOLiD platform. The assay detected expression of **75% more genes (5,270 additional)** than parallel microarray analysis of the same cell, identified **1,753 previously unknown splice junctions** (≥5 reads), and revealed that **8–19% of multi-isoform genes expressed at least two isoforms simultaneously** in individual blastomeres or oocytes. Applied to *Dicer1⁻/⁻* and *Ago2⁻/⁻* oocytes, the method exposed 1,696 and 1,553 abnormally upregulated genes (619 shared), demonstrating that single-cell mRNA-Seq could resolve perturbation biology that bulk approaches miss for rare cell populations.

## Why this matters

Foundational citation for any scRNA-seq introduction. **Tang 2009 is the field's origin point** — the first demonstration that single-cell transcriptomes could be captured with sequencing rather than qPCR or microarray panels, opening the conceptual door to all downstream droplet (Drop-seq, 10x Chromium, inDrop), plate (Smart-seq2, CEL-seq2, MARS-seq), and combinatorial-indexing (sci-RNA-seq, SPLiT-seq) scRNA-seq methods catalogued in the wiki. For a multi-omics review, this paper anchors the "WHY single-cell at all" argument by showing what bulk averaging hides: gene-by-gene the single blastomere differs systematically from the microarray-detectable transcriptome, and isoform usage is more complex than population averages suggest. The 75%-more-genes claim against microarray is the canonical evidence that scRNA-seq is not just bulk-RNA-seq at lower scale — it accesses transcripts that microarrays cannot probe.

## Key claims and evidence

- A single mouse blastomere yielded **5,270 additional gene calls** vs. microarray on the same biological starting point — direct evidence of higher sensitivity at low input.
- **1,753 novel splice junctions** at ≥5-read threshold — single-cell mRNA-Seq is informative for isoform discovery, not only quantification.
- **Multi-isoform coexpression** (8–19% of multi-isoform genes) in single cells argues against the "one cell = one isoform" simplification.
- Dicer1/Ago2 knockout phenotypes were resolvable from single oocytes — *no pooling required*, opening rare-cell perturbation studies.

## Limitations (as relevant for review writing)

- Plate-based, low-throughput: tens of cells per study, not the thousands needed for unbiased atlas building. The throughput problem is solved later by [[10-Summaries/macosko-2015-drop-seq|Drop-seq (Macosko 2015)]].
- No UMI — quantitative comparisons across cells are still confounded by PCR amplification bias. UMIs enter the field with later protocols (see [[30-Concepts/umi-molecular-barcoding]]).
- Sensitivity is high relative to microarray but, as [[10-Summaries/svensson-2017-power-analysis|Svensson 2017]] later shows quantitatively, scRNA-seq capture efficiency is still far below true mRNA content (typically 10–25%).

## Related

- [[30-Concepts/scrna-seq]] — concept page this paper anchors
- [[10-Summaries/macosko-2015-drop-seq]] — high-throughput droplet successor
- [[10-Summaries/svensson-2017-power-analysis]] — protocol benchmarking that puts Tang-style plate methods in context
- [[20-Entities/fuchou-tang]] — first author, founder of single-cell genomics
- [[10-Summaries/dey-2015-dr-seq]] — DR-seq extends Tang-style scRNA to joint scDNA+scRNA
- [[10-Summaries/hou-2016-sctrio-seq]] — scTrio-seq extends to triple-omics
- [[40-Topics/single-cell-multiomics]]

## Citation

Tang F, Barbacioru C, Wang Y, Nordman E, Lee C, Xu N, Wang X, Bodeau J, Tuch BB, Siddiqui A, Lao K, Surani MA. *Nat Methods* 6(5): 377–82 (2009). PMID: 19349980. [DOI](https://doi.org/10.1038/nmeth.1315). According to PubMed.
