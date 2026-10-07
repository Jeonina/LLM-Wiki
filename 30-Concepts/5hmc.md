---
type: concept
title: 5-hydroxymethylcytosine (5hmC)
aliases: [5hmC, hydroxymethylcytosine]
tags: [methylation, TET, demethylation, brain]
created: 2026-05-12
updated: 2026-10-07
---

# 5-hydroxymethylcytosine (5hmC)

> An oxidative intermediate generated when TET enzymes hydroxylate 5-methylcytosine. ~10–30× less abundant than 5mC in most tissues, but particularly enriched in brain. Both an **intermediate** in active DNA demethylation and a **stable epigenetic mark** with regulatory function at enhancers and active gene bodies.

## Definition

TET (1/2/3) enzymes oxidize 5mC → 5hmC → 5fC → 5caC. 5fC and 5caC are excised by thymine-DNA glycosylase for base-excision repair, completing demethylation. 5hmC itself, however, is stable enough to act as a regulatory mark in differentiated tissues.

## Why it matters

- Bisulfite sequencing **conflates 5mC and 5hmC** — both read as C. Methods that distinguish them (hmC-CATCH, AbaSI-based scAba-seq, [[30-Concepts/simple-seq]], [[30-Concepts/6-base-cut-and-tag]]) reveal divergent regulatory roles.
- 5hmC marks active regulatory elements (enhancers, transcribed gene bodies).
- Loss of 5hmC is associated with cancer (in IDH-mutant glioma/AML, accumulated D-2-hydroxyglutarate competes with α-KG and inhibits TET; [[10-Summaries/kim-2017-methylation-memory-review]]).
- TET1 mutant mice show adult-neurogenesis deficits and memory impairment.

## Variants and refinements

- Type-1 5hmCG = basal-level, not co-occurring with 5mCG.
- Type-2 5hmCG = co-occurring with 5mCG on the same molecule, associated with active demethylation regions ([[10-Summaries/bai-2024-simple-seq]]).

## Origin and single-cell measurement

- **Enzymatic origin.** TET1 is a 2-oxoglutarate/Fe(II)-dependent dioxygenase that oxidizes 5mC to 5hmC in vitro and in cells; the catalytically dead H1671Y/D1673A mutant does not ([[10-Summaries/tahiliani-2009-tet1-5hmc]]).
- **Abundance.** 4–6% of cytosine species at MspI CpG sites in mouse ES cells (~1 base in 3,000 genome-wide, ~2 × 10⁶ per haploid genome); undetectable in activated T cells and dendritic cells ([[10-Summaries/tahiliani-2009-tet1-5hmc]]).
- **Bisulfite cannot see it.** Bisulfite conversion does not discriminate C from 5mC from 5hmC, so every bisulfite-based methylome — bulk or single-cell — reports a 5mC+5hmC composite ([[10-Summaries/jones-2012-dna-methylation-functions]]; [[10-Summaries/flusberg-2010-smrt-methylation]]).
- **Two routes to discrimination.** Polymerase-kinetic signatures in SMRT sequencing separate C/5mC/5hmC by PCA over IPD and pulse-width features ([[10-Summaries/flusberg-2010-smrt-methylation]]); enzymatic/chemical conversion does it at single-cell, single-base resolution ([[10-Summaries/chen-2025-sctaps-sccaps-plus]]).
- **5hmC alone classifies cell type.** Gene-body 5hmC clusters hippocampal neurons from non-neurons and annotates OPCs without any transcriptome; neurons carry 22.04% vs 9.29% in non-neurons ([[10-Summaries/chen-2025-sctaps-sccaps-plus]]).
- **Readers exist.** UHRF2 reads 5hmC and 5caC but not 5mC or 5fC; MBD3 and MeCP2 read 5hmC, and a Rett-syndrome MeCP2 mutation disrupts 5hmC but not 5mC binding — implying demethylation-independent function ([[10-Summaries/rothbart-2014-histone-dna-language]]).

## Added 2026-10-07

Bisulfite converts 5hmC to cytosine 5-methylenesulfonate (CMS) with ~99.7% efficiency; CMS resists deamination and is read as C, so bisulfite sequencing cannot separate 5hmC from 5mC, while anti-5mC antibodies do not recognise 5hmC ([[10-Summaries/huang-2010-5hmc-bisulfite]]). CMS also stalls Taq polymerase, most strongly at adjacent or closely spaced CMS residues, suggesting densely hydroxymethylated DNA may be under-represented in bisulfite data ([[10-Summaries/huang-2010-5hmc-bisulfite]]).

Like 5mC, 5hmC protects DNA fragments from bisulfite-induced degradation (~fourfold higher recovery of a C-rich fragment under heat denaturation), contributing to over-representation of modified sequence in WGBS [[10-Summaries/olova-2018-wgbs-library-bias]].

Because 5hmC is not maintained through replication, scAba-seq found strong per-chromosome strand bias of 5hmC that can identify sister cells; scMAB-seq (M.SssI pre-methylation before bisulfite) maps 5fC/5caC in single cells [[10-Summaries/ludwig-2019-sc-chromatin-modifications-review]].

Standard EM-seq does not separate 5mC from 5hmC; discrimination needs a 5hmC-only variant (T4-BGT without TET2) or ACE-seq, and 5fC/5caC cannot be read ([[10-Summaries/vaisvila-2021-em-seq]]).


## Related

- [[40-Topics/dna-methylation]] · [[30-Concepts/tet-enzymes]] · [[30-Concepts/simple-seq]] · [[30-Concepts/6-base-cut-and-tag]]
- [[10-Summaries/tahiliani-2009-tet1-5hmc]] · [[10-Summaries/chen-2025-sctaps-sccaps-plus]] · [[10-Summaries/flusberg-2010-smrt-methylation]]
