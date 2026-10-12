---
type: concept
title: CpG island
aliases: [CpG islands, CGI]
tags: [epigenetics, regulation, methylation]
created: 2026-05-11
updated: 2026-10-12
---

# CpG island

> Short (typically 200–2000 bp) regions of unusually high CpG dinucleotide density and GC content that occur at the promoters of most housekeeping and developmental regulator genes. Constitutively *unmethylated*, in contrast to the global genome's ~60–80% CpG methylation. Hypermethylation of promoter CpG islands is a hallmark of tumorigenesis ([[10-Summaries/smith-2013-methylation-development|Smith & Meissner 2013]]).

> [!abstract] 한눈에
> CpG island는 CpG 밀도가 유난히 높고 대개 promoter에 놓이며 평소에는 methylation되지 않는 짧은 구간이고, 암에서는 이곳의 hypermethylation이 tumor suppressor를 끈다 ([[10-Summaries/smith-2013-methylation-development|Smith & Meissner 2013]]). scRRBS는 CGI를 겨냥해 세포마다 같은 CpG를 읽는 대신 CCGG 근처 밖의 CpG는 보지 못한다 ([[10-Summaries/guo-2015-scrrbs-protocol|Guo 2015]]).

## Definition

Mammalian genomes are globally CpG-depleted (~21% of expected CpG counts), an artifact of the elevated mutation rate of methylated CpG → TpG. CpG islands escape this depletion because they are unmethylated and therefore not exposed to deamination-driven mutation. Functional definition: GC content >50%, observed/expected CpG ratio >0.6, length >200 bp.

~60% of human genes have a CpG island at their promoter; **"orphan" CpG islands** outside promoters also occur and may serve enhancer-like functions.

## Why it matters

- Unmethylated CpG islands at promoters are markers of active or poised transcription.
- Hypermethylation of CpG islands is a major cancer-epigenetics phenomenon — silences tumor suppressors and is a clinical biomarker ([[10-Summaries/smith-2013-methylation-development|Smith & Meissner 2013]]).
- The maintenance of CpG islands as unmethylated requires *active* exclusion of DNMTs ([[dnmt]]) by TF binding, H3K4 methyltransferases, and possibly TET-mediated demethylation ([[tet-enzymes]]) as proofreading ([[10-Summaries/smith-2013-methylation-development|Smith & Meissner 2013]]).

## Types of CpG island

- **Promoter CpG islands** — most common; protected from methylation ([[10-Summaries/smith-2013-methylation-development|Smith & Meissner 2013]]).
- **Orphan CpG islands** — intragenic or distal; enhancer-like, more often regulated.
- **Methylation-sensitive vs methylation-insensitive promoters** — only ~50% of TSS-proximal CpG islands are silenced when methylated.

## Evidence and examples

**Cancer**

- Hypermethylation of the CDKN2A CpG island in glioblastoma → loss of tumor suppressor function.
- Hypermethylation of the MLH1 CpG island in colorectal cancer → microsatellite instability.

**Measuring CGIs in single cells**

- Reduced-representation bisulfite sequencing exists to enrich for CGIs: MspI digestion plus size selection sequences ~10% of the genome yet reproducibly covers >70% of promoters and >80% of CGIs ([[10-Summaries/guo-2015-scrrbs-protocol|Guo 2015]]).
- At single-cell scale, scRRBS recovers ~1 million CpGs per diploid cell including ~70% of mouse CGIs ([[10-Summaries/guo-2015-scrrbs-protocol|Guo 2015]]).
- Because MspI cuts the same sites in every cell, scRRBS covers *the same* CpGs across cells, whereas whole-genome methods sample randomly and two cells rarely share a site — which makes per-site cross-cell comparison mostly missing data ([[10-Summaries/guo-2015-scrrbs-protocol|Guo 2015]]).

**CpG density in 3D genome analysis**

- CpG density is strongly tied to A compartments, which is why CpG-guided single-cell compartment scores (scA/B) collapse toward CpG density at low contact numbers; scDIAGRAM uses CpG density only post hoc to orient A/B labels ([[10-Summaries/peng-2026-scdiagram|scDIAGRAM]]).

**CGIs in sequence models**

- Unsupervised GenART token boundaries recover UCSC CpG-island boundaries with recall 0.534 (±1 bp), lower than CDS (0.662) or exon (0.640) boundaries ([[10-Summaries/chen-2026-genart|GenART]]).
- Probing OmniNA layer by layer shows CpG content is best separated at layer 20, while conservation separates at layer 2 and non-B DNA structures at layer 23 — different biology lives at different depths ([[10-Summaries/shen-2026-omnina|OmniNA]]).

## Contested points

- Whether orphan CpG islands have distinct regulatory mechanisms or are simply unannotated TSSs.
- **The underappreciated advantage of scRRBS is consistency, not coverage.** No benchmark in the corpus tests whether same-site coverage across cells ([[10-Summaries/guo-2015-scrrbs-protocol|Guo 2015]]) translates into better cross-cell DMR detection, despite it being the strongest argument for the method (synthesis).
- **The structural cost of CGI enrichment:** CpGs outside CCGG-proximal fragments are invisible, which matters for the distal-enhancer discovery that whole-genome methylome work makes central ([[10-Summaries/luo-2017-snmc-seq|snmC-seq]]) (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/dnmt|DNMT]] — The methyltransferases actively excluded from CpG islands.
> - `concept` [[30-Concepts/tet-enzymes|TET enzymes]] — Possible demethylation proofreading that keeps CGIs unmethylated.
> - `hub` [[40-Topics/dna-methylation|DNA methylation]] — 5mC at CpG dinucleotides: assays, single-cell methods and analysis.

## All sources on this page

> [!info]- 6 summaries cited here
> - [[10-Summaries/chen-2026-genart|GenART 2026]]
> - [[10-Summaries/guo-2015-scrrbs-protocol|Guo 2015]]
> - [[10-Summaries/luo-2017-snmc-seq|Luo 2017]]
> - [[10-Summaries/peng-2026-scdiagram|Peng 2026]]
> - [[10-Summaries/shen-2026-omnina|OmniNA 2026]]
> - [[10-Summaries/smith-2013-methylation-development|Smith & Meissner 2013]]
