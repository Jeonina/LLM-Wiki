---
type: concept
title: Decitabine
aliases: [DAC, 5-aza-2'-deoxycytidine, Dacogen]
tags: [chemotherapy, hypomethylating-agent, AML, MDS]
created: 2026-05-12
updated: 2026-10-12
---

# Decitabine

> A cytidine analog (5-aza-2'-deoxycytidine) that incorporates into DNA during replication and **covalently traps DNMT1**, causing genome-wide loss of DNA methylation through successive cell divisions. Standard-of-care for elderly AML and MDS patients.

> [!abstract] 한눈에
> Decitabine은 복제 중 DNA에 끼어들어 DNMT1을 붙잡아 세포가 분열할 때마다 methylation을 잃게 하는 hypomethylating agent다. single-cell methylome에서는 같은 약물에도 세포마다 반응이 다르게 나타난다 ([[10-Summaries/farlik-2015-scwgbs|Farlik 2015]]; [[10-Summaries/shen-2026-splicool-seq|SpliCOOL-seq]]).

## Why it matters

- Hypomethylating agent (HMA) used clinically since FDA approval 2006.
- Mechanism: traps DNMT1 ([[30-Concepts/dnmt|DNMT]]) → fails to methylate hemimethylated DNA during replication → passive demethylation.
- Triggers [[30-Concepts/viral-mimicry]] in responder cells.
- Patient response is highly variable; predictive biomarkers are an unmet need.
- Compared with azacitidine (5-aza-cytidine) in [[10-Summaries/shen-2026-splicool-seq|SpliCOOL-seq]]: both cause demethylation but in **distinct patterns** at single-cell resolution.

## Examples

- KG1a/HL60 AML cells ± DAC in [[10-Summaries/hunt-2022-sctem-seq|scTEM-seq]].
- Single-cell methylomes reveal per-cell heterogeneity in response to hypomethylating drugs. Two azacytidine-treated K562 single cells kept untreated-like methylation, which the authors suggest was because they had not divided ([[10-Summaries/farlik-2015-scwgbs|Farlik 2015]]).
- Under azacytidine, lineage-specific enhancers and TF sites demethylated faster than expected, and repressive chromatin slower ([[10-Summaries/farlik-2015-scwgbs|Farlik 2015]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/viral-mimicry|Viral mimicry]] — The interferon-like response hypomethylation triggers in responder cells.
> - `concept` [[30-Concepts/dnmt|DNMT]] — DNMT1 is the enzyme decitabine traps.
> - `hub` [[40-Topics/dna-methylation|DNA methylation]] — 5mC at CpG dinucleotides: assays, single-cell methods and analysis.
> - `hub` [[40-Topics/hematopoietic-malignancies|Hematopoietic malignancies]] — AML and MDS, where HMAs are standard therapy.

## All sources on this page

> [!info]- 3 summaries cited here
> - [[10-Summaries/farlik-2015-scwgbs|Farlik 2015]]
> - [[10-Summaries/hunt-2022-sctem-seq|Hunt 2022]]
> - [[10-Summaries/shen-2026-splicool-seq|Shen 2026]]
