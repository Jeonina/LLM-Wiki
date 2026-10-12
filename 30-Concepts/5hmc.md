---
type: concept
title: 5-hydroxymethylcytosine (5hmC)
aliases: [5hmC, hydroxymethylcytosine]
tags: [methylation, TET, demethylation, brain]
created: 2026-05-12
updated: 2026-10-12
---

# 5-hydroxymethylcytosine (5hmC)

> An oxidative intermediate generated when TET enzymes hydroxylate 5-methylcytosine ([[10-Summaries/tahiliani-2009-tet1-5hmc|Tahiliani 2009]]). ~10–30× less abundant than 5mC in most tissues, but particularly enriched in brain. Both an **intermediate** in active DNA demethylation and a **stable epigenetic mark** with regulatory function at enhancers and active gene bodies.

> [!abstract] 한눈에
> 5hmC는 TET 효소가 5mC를 산화해 만드는 염기로, 탈메틸화의 중간체이면서 그 자체로 조절 표지 역할도 한다 ([[10-Summaries/tahiliani-2009-tet1-5hmc|Tahiliani 2009]]). bisulfite sequencing은 5hmC를 5mC와 똑같이 C로 읽기 때문에, 둘을 나누려면 효소·화학 변환이나 SMRT kinetics 같은 별도 방법이 필요하다 ([[10-Summaries/huang-2010-5hmc-bisulfite|Huang 2010]]; [[10-Summaries/chen-2025-sctaps-sccaps-plus|Chen 2025]]).

## Definition

TET (1/2/3) enzymes oxidize 5mC → 5hmC → 5fC → 5caC. 5fC and 5caC are excised by thymine-DNA glycosylase for base-excision repair, completing demethylation. 5hmC itself, however, is stable enough to act as a regulatory mark in differentiated tissues.

- **Enzymatic origin.** TET1 is a 2-oxoglutarate/Fe(II)-dependent dioxygenase that oxidizes 5mC to 5hmC in vitro and in cells; the catalytically dead H1671Y/D1673A mutant does not ([[10-Summaries/tahiliani-2009-tet1-5hmc|Tahiliani 2009]]). See [[30-Concepts/tet-enzymes]].
- **Not maintained through replication**, which is why single-cell 5hmC shows per-chromosome strand bias (see Evidence) ([[10-Summaries/ludwig-2019-sc-chromatin-modifications-review|Ludwig 2019]]).

## Why it matters

- Bisulfite sequencing **conflates 5mC and 5hmC** — both read as C. Methods that distinguish them (hmC-CATCH, AbaSI-based scAba-seq, [[30-Concepts/simple-seq]], [[30-Concepts/6-base-cut-and-tag]]) reveal divergent regulatory roles.
- 5hmC marks active regulatory elements (enhancers, transcribed gene bodies).
- Loss of 5hmC is associated with cancer (in IDH-mutant glioma/AML, accumulated D-2-hydroxyglutarate competes with α-KG and inhibits TET; [[10-Summaries/kim-2017-methylation-memory-review|Kim 2017]]).
- TET1 mutant mice show adult-neurogenesis deficits and memory impairment.
- **Readers exist.** UHRF2 reads 5hmC and 5caC but not 5mC or 5fC; MBD3 and MeCP2 read 5hmC, and a Rett-syndrome MeCP2 mutation disrupts 5hmC but not 5mC binding — implying demethylation-independent function ([[10-Summaries/rothbart-2014-histone-dna-language|Rothbart 2014]]).

## Variants

- Type-1 5hmCG = basal-level, not co-occurring with 5mCG ([[10-Summaries/bai-2024-simple-seq|SIMPLE-seq]]).
- Type-2 5hmCG = co-occurring with 5mCG on the same molecule, associated with active demethylation regions ([[10-Summaries/bai-2024-simple-seq|SIMPLE-seq]]).

## Measurement approaches

| Approach | What it reads | Separates 5hmC from 5mC? | Source |
|---|---|---|---|
| Bisulfite sequencing (bulk or single-cell) | 5mC+5hmC composite; 5hmC becomes CMS, which reads as C | No | ([[10-Summaries/jones-2012-dna-methylation-functions\|Jones 2012]]; [[10-Summaries/flusberg-2010-smrt-methylation\|Flusberg 2010]]; [[10-Summaries/huang-2010-5hmc-bisulfite\|Huang 2010]]) |
| Standard EM-seq | 5mC+5hmC | No; needs a 5hmC-only variant (T4-BGT without TET2) or ACE-seq; 5fC/5caC cannot be read | ([[10-Summaries/vaisvila-2021-em-seq\|EM-seq]]) |
| SMRT polymerase kinetics | C/5mC/5hmC by PCA over IPD and pulse-width features | Yes | ([[10-Summaries/flusberg-2010-smrt-methylation\|Flusberg 2010]]) |
| Enzymatic/chemical conversion (scTAPS / scCAPS+) | 5mC and 5hmC at single-cell, single-base resolution | Yes | ([[10-Summaries/chen-2025-sctaps-sccaps-plus\|Chen 2025]]) |
| [[30-Concepts/simple-seq]] | Joint single-cell 5mC and 5hmC on the same molecule | Yes | ([[10-Summaries/bai-2024-simple-seq\|SIMPLE-seq]]) |
| scAba-seq (AbaSI) | Single-cell 5hmC with per-chromosome strand bias | 5hmC-specific | ([[10-Summaries/ludwig-2019-sc-chromatin-modifications-review\|Ludwig 2019]]) |
| scMAB-seq (M.SssI pre-methylation before bisulfite) | 5fC/5caC in single cells | Maps oxidized forms | ([[10-Summaries/ludwig-2019-sc-chromatin-modifications-review\|Ludwig 2019]]) |
| Anti-5mC antibodies | 5mC | Do not recognise 5hmC | ([[10-Summaries/huang-2010-5hmc-bisulfite\|Huang 2010]]) |

## Evidence and examples

- **Abundance.** 4–6% of cytosine species at MspI CpG sites in mouse ES cells (~1 base in 3,000 genome-wide, ~2 × 10⁶ per haploid genome); undetectable in activated T cells and dendritic cells ([[10-Summaries/tahiliani-2009-tet1-5hmc|Tahiliani 2009]]).
- **5hmC alone classifies cell type.** Gene-body 5hmC clusters hippocampal neurons from non-neurons and annotates OPCs without any transcriptome; neurons carry 22.04% vs 9.29% in non-neurons ([[10-Summaries/chen-2025-sctaps-sccaps-plus|Chen 2025]]).
- **Sister-cell identification.** scAba-seq found strong per-chromosome strand bias of 5hmC that can identify sister cells ([[10-Summaries/ludwig-2019-sc-chromatin-modifications-review|Ludwig 2019]]).
- **Bisulfite chemistry of 5hmC.** Bisulfite converts 5hmC to cytosine 5-methylenesulfonate (CMS) with ~99.7% efficiency; CMS resists deamination and is read as C ([[10-Summaries/huang-2010-5hmc-bisulfite|Huang 2010]]).

## Contested points

- **Bisulfite data may under-represent dense 5hmC.** CMS stalls Taq polymerase, most strongly at adjacent or closely spaced CMS residues, suggesting densely hydroxymethylated DNA may be under-represented in bisulfite data ([[10-Summaries/huang-2010-5hmc-bisulfite|Huang 2010]]).
- **…but over-represented through fragment protection.** Like 5mC, 5hmC protects DNA fragments from bisulfite-induced degradation (~fourfold higher recovery of a C-rich fragment under heat denaturation), contributing to over-representation of modified sequence in WGBS ([[10-Summaries/olova-2018-wgbs-library-bias|Olova 2018]]). The two biases act in opposite directions, so the net effect on a given locus is unclear (synthesis).
- **Intermediate or stable mark?** 5hmC is both a demethylation intermediate and a stable mark in differentiated tissue; reader proteins that bind 5hmC but not 5mC support a demethylation-independent function ([[10-Summaries/rothbart-2014-histone-dna-language|Rothbart 2014]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/tet-enzymes|TET enzymes]] — The dioxygenases that oxidize 5mC to 5hmC, 5fC and 5caC.
> - `concept` [[30-Concepts/simple-seq|SIMPLE-seq]] — Joint single-cell 5mC and 5hmC at base resolution.
> - `concept` [[30-Concepts/6-base-cut-and-tag|6-base CUT&Tag]] — Histone marks with 5mC and 5hmC from the same molecules.
> - `hub` [[40-Topics/dna-methylation|DNA methylation]] — Methylation biology and single-cell methylome methods.

## All sources on this page

> [!info]- 11 summaries cited here
> - [[10-Summaries/bai-2024-simple-seq|Bai 2024]]
> - [[10-Summaries/chen-2025-sctaps-sccaps-plus|Chen 2025]]
> - [[10-Summaries/flusberg-2010-smrt-methylation|Flusberg 2010]]
> - [[10-Summaries/huang-2010-5hmc-bisulfite|Huang 2010]]
> - [[10-Summaries/jones-2012-dna-methylation-functions|Jones 2012]]
> - [[10-Summaries/kim-2017-methylation-memory-review|Kim & Costello 2017]]
> - [[10-Summaries/ludwig-2019-sc-chromatin-modifications-review|Ludwig & Bintu 2019]]
> - [[10-Summaries/olova-2018-wgbs-library-bias|Olova 2018]]
> - [[10-Summaries/rothbart-2014-histone-dna-language|Rothbart & Strahl 2014]]
> - [[10-Summaries/tahiliani-2009-tet1-5hmc|Tahiliani 2009]]
> - [[10-Summaries/vaisvila-2021-em-seq|Vaisvila 2021]]
