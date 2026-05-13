---
type: summary
title: "Hou 2016 — scTrio-seq: single-cell triple-omics in hepatocellular carcinomas"
aliases: ["Hou 2016 scTrio-seq", "scTrio-seq", "single-cell triple omics"]
tags: [scTrio-seq, triple-omics, scDNA-scRNA-methylome, scRRBS, HCC, founding-method, Tang-lab, Peking-University]
created: 2026-05-13
updated: 2026-05-13
sources: ["Yu_2016_CellResearch.pdf"]
---

Hou, Guo, Cao, Li et al. (Tang lab; Peking University) developed **scTrio-seq**, the founding method for **single-cell triple-omics** — simultaneous profiling of genome (CNVs via scRRBS read depth), DNA methylome (scRRBS), and transcriptome (scRNA-seq) from the same individual mammalian cell. Workflow: mild cytoplasmic-only lysis releases mRNA; centrifugation separates mRNA-containing supernatant from nucleus-containing precipitate; mRNA → scRNA-seq, nucleus → scRRBS. Applied to 25 single HCC tumor cells: identified two subpopulations distinguishable by CNV, methylome, AND transcriptome. Large-scale CNVs caused proportional gene-expression changes (gain → up, loss → down) but did NOT affect DNA methylation in those regions — important cross-omic correlation finding.

## Why this matters

**Founding triple-omics paper** for scDNA + scMethylome + scRNA from the same cell — preceded scNMT-seq (Clark 2018, which adds chromatin accessibility and uses scBS-seq). Anchors §3.1 (parallel multi-omics) and §5 cancer applications. The Tang lab is a major figure in Chinese single-cell genomics — Fuchou Tang co-developed scRNA-seq (2009 founding paper) and the early scRRBS methodology. Existing bibkey check needed.

## Related

- [[10-Summaries/macaulay-2015-gt-seq]]
- [[10-Summaries/dey-2015-dr-seq]]
- [[10-Summaries/clark-2018-scnmt]]
- [[10-Summaries/guo-2013-scrrbs]]
- [[20-Entities/fuchou-tang]]
