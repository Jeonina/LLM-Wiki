---
type: concept
title: Mutational signatures
aliases: [SBS signatures, COSMIC signatures]
tags: [somatic-mutation, mutational-process, cancer, aging]
created: 2026-05-12
updated: 2026-10-12
---

# Mutational signatures

> Characteristic patterns of single-base substitutions (SBS), decomposed into trinucleotide contexts (96 channels), that reflect specific mutagenic processes: aging-related deamination (SBS1, SBS5), UV exposure (SBS7), tobacco (SBS4), APOBEC activity (SBS2/13), DNA-repair deficiency and environmental mutagens ([[10-Summaries/alexandrov-2013-mutational-signatures|Alexandrov 2013]]).

> [!abstract] 한눈에
> Mutational signature는 염기 치환을 앞뒤 염기 문맥까지 96가지로 나눈 뒤 NMF로 분해해 얻은 반복 패턴이며, 노화·자외선·흡연 같은 돌연변이 원인을 서열만으로 거꾸로 읽게 해 준다 ([[10-Summaries/alexandrov-2013-mutational-signatures|Alexandrov 2013]]). 이제는 single-cell과 duplex 데이터로 클론 확장 없이도 정상 조직의 signature를 읽지만, 증폭 artefact가 실제 signature를 흉내 낼 수 있다는 점이 계속 문제가 된다 ([[10-Summaries/nandi-2025-udseq|UDSeq]]; [[10-Summaries/luquette-2022-neuron-scan2-indels|Luquette 2022]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [뇌 체세포 모자이크 교재](../60-Explainers/brain-somatic-mosaicism.html)
>
> [Duplex sequencing 시뮬레이터](../60-Explainers/duplex-sequencing.html)
<!-- /explainer-links -->

## Definition

Mutations are classified by central substitution × 5′/3′ flanking base into 96 categories, six pyrimidine-referenced base changes × 16 trinucleotide contexts ([[10-Summaries/alexandrov-2013-mutational-signatures|Alexandrov 2013]]). Non-negative matrix factorization across many tumor genomes yields recurring patterns ("signatures") associated with mutagenic processes ([[10-Summaries/alexandrov-2013-mutational-signatures|Alexandrov 2013]]). The Catalogue of Somatic Mutations in Cancer (COSMIC) curates the reference signature set, which originates in the founding study from the lab of [[20-Entities/ludmil-alexandrov|Ludmil Alexandrov]] ([[10-Summaries/alexandrov-2013-mutational-signatures|Alexandrov 2013]]).

## Why it matters

- Signatures reveal **mutagenic etiology** from sequence data alone: SBS4 in lung cancer marks tobacco, and SBS2/13 in breast cancer mark APOBEC.
- Signature analysis on duplex-sequencing data lets researchers read mutagenic exposure from normal tissues without clonal expansion ([[10-Summaries/nandi-2025-udseq|UDSeq]]).
- Signature 1A/B, C>T at NpCpG from spontaneous deamination of 5-methylcytosine, appears in 25 of 30 cancer classes, making the most universal mutational process in human cancer a direct chemical consequence of the epigenome ([[10-Summaries/alexandrov-2013-mutational-signatures|Alexandrov 2013]]).

## Signature classes

| Class | Context | Notes | Source |
|---|---|---|---|
| SBS (single-base substitution) | 96 trinucleotide channels | The standard; 21 validated signatures in the founding catalogue | ([[10-Summaries/alexandrov-2013-mutational-signatures\|Alexandrov 2013]]) |
| Strand-resolved SBS | 192 trinucleotide contexts | With per-strand single-molecule data, the pyrimidine/purine split carries real information instead of being collapsed; an `ss` suffix marks a single-strand mismatch signature and `ss*` a single-strand damage signature | ([[10-Summaries/liu-2024-hidef-seq\|HiDEF-seq]]) |
| DBS (doublet-base substitution) | Adjacent-pair substitutions | — | — |
| ID (insertion-deletion) | Indel contexts | ID4 (deletion-rich, unknown mechanism) and replication-linked ID1/ID2 are named examples | ([[10-Summaries/luquette-2022-neuron-scan2-indels\|Luquette 2022]]) |
| CN (copy number) and SV (structural variant) | — | Newer extensions | — |

## Reading signatures outside bulk tumours

| Approach | Example | What it shows | Source |
|---|---|---|---|
| PTA single cells with duplex validation | [[10-Summaries/luquette-2025-pta-duplex-mosaicism\|Luquette 2025]] | Exposure signatures (SBS4) in normal lung nuclei | ([[10-Summaries/luquette-2025-pta-duplex-mosaicism\|Luquette 2025]]) |
| PTA neurons, SNVs and indels | [[10-Summaries/luquette-2022-neuron-scan2-indels\|Luquette 2022]] | Age-correlated indel signatures; MDA artefact spectra | ([[10-Summaries/luquette-2022-neuron-scan2-indels\|Luquette 2022]]) |
| Low-false-positive scWGA | [[10-Summaries/xing-2021-meta-cs\|META-CS]] | De novo signatures that separate cell types | ([[10-Summaries/xing-2021-meta-cs\|META-CS]]) |
| scRNA-seq-derived mutations | [[10-Summaries/muyas-2024-scomatic\|SComatic]] | Signatures at cell-type resolution, after renormalising trinucleotide frequencies to callable regions | ([[10-Summaries/muyas-2024-scomatic\|SComatic]]) |
| Duplex sequencing of polyclonal populations | [[10-Summaries/nandi-2025-udseq\|UDSeq]] | Exposure-specific signatures without clonal expansion | ([[10-Summaries/nandi-2025-udseq\|UDSeq]]) |
| Bottleneck duplex sequencing | [[10-Summaries/hoang-2016-botseqs\|BotSeqS]] | Tissue-specific rare-mutation spectra in normal tissues | ([[10-Summaries/hoang-2016-botseqs\|BotSeqS]]) |
| Single-molecule bulk DNA | [[10-Summaries/maslov-2022-smm-seq\|SMM-seq]] | Age-associated de novo signatures in liver | ([[10-Summaries/maslov-2022-smm-seq\|SMM-seq]]) |
| Unamplified single strands | [[10-Summaries/liu-2024-hidef-seq\|HiDEF-seq]] | Single-strand mismatch and damage signatures | ([[10-Summaries/liu-2024-hidef-seq\|HiDEF-seq]]) |
| Simulation input | [[10-Summaries/kozlov-2022-cellphy\|CellPhy]] | COSMIC signatures 1 and 5 used to generate realistic somatic substitution spectra | ([[10-Summaries/kozlov-2022-cellphy\|CellPhy]]) |
| Foundation-model covariates | [[10-Summaries/kong-2026-mutationprojector\|MutationProjector]] | Seven dominant signatures (MESiCA for panels, SigProfiler for WES/WGS) fed as covariate nodes connected to all genes | ([[10-Summaries/kong-2026-mutationprojector\|MutationProjector]]) |

## Evidence and examples

**Founding catalogue**

- The founding study extracted 21 validated signatures from 4,938,362 mutations across 7,042 cancers of 30 classes ([[10-Summaries/alexandrov-2013-mutational-signatures|Alexandrov 2013]]).

**Exposure signatures**

- SBS4 (tobacco) was detected in lung tissue of a 74-year-old male via PTA-scDNA-seq with DS validation ([[10-Summaries/luquette-2025-pta-duplex-mosaicism|Luquette 2025]]).
- UDSeq reproduces exposure-specific signatures (AA-I/SBS22a, 4NQO, NNK, UV) in once-passaged polyclonal cell populations without clonal expansion (cosine 0.95–0.99 to clonal references), and in UV-exposed mice and NNK-exposed rats ([[10-Summaries/nandi-2025-udseq|UDSeq]]).
- Mutations called from scRNA-seq by SComatic reproduce UV SBS7 in cutaneous SCC (cosine 0.98 with WES), MMR and POLE signatures in hypermutated colorectal tumours, and SBS44 in cardiomyocytes ([[10-Summaries/muyas-2024-scomatic|SComatic]]).
- TC-motif cytosine bias in childhood ALL was read as APOBEC rather than AID activity, supported by the absence of a WRCY motif and the lack of correlation with VH-segment mutation; this is signature reasoning without a formal signature framework ([[10-Summaries/gawad-2014-all-clonal-origins|Gawad 2014]]).
- In MutationProjector, APOBEC signature emerged as a metastasis-predictive feature ([[10-Summaries/kong-2026-mutationprojector|MutationProjector]]).

**Aging and clocklike processes**

- SBS1 (5mC deamination at CpG) dominates early embryonic mutations, and SBS5 dominates aging neurons ([[10-Summaries/bizzotto-2022-brain-mosaicism-review|Bizzotto & Walsh 2022]]).
- A clocklike signature resembling cancer Signature 5 rises with age in postmitotic neurons (P = 1×10⁻¹¹), so this clocklike process does not require DNA replication ([[10-Summaries/lodato-2017-aging-neurons|Lodato 2018]]).
- In PTA-amplified neurons, indel signature ID4 was the most prevalent and most age-correlated (r = 0.82), while replication-linked ID1/ID2 were absent ([[10-Summaries/luquette-2022-neuron-scan2-indels|Luquette 2022]]).
- In bulk liver DNA assayed by SMM-seq (3 young, 3 aged donors), de novo NMF found a signature S1 that was enriched in the aged group and resembled SBS5 (cosine 0.904); a young-dominant S2 matched no COSMIC signature ([[10-Summaries/maslov-2022-smm-seq|SMM-seq]]).

**Tissue and cell-type spectra**

- In normal tissues measured by BotSeqS, rare-mutation spectra were tissue-specific and resembled spectra of cancers from the same organs ([[10-Summaries/hoang-2016-botseqs|BotSeqS]]).
- With low-false-positive single-cell calls, NMF found three signatures in 53 PBMCs: an HSPC-like signature (r = 0.976 with HSPC spectra), one specific to SHM+ B cells, and a T-cell signature whose contribution rose with SNV burden ([[10-Summaries/xing-2021-meta-cs|META-CS]]).
- PCA on trinucleotide spectra separated neurons from blood cells and most T cells from B cells ([[10-Summaries/xing-2021-meta-cs|META-CS]]).

**Strand-resolved signatures**

- SBS10ss (*POLE* proofreading deficiency) projects onto its samples' own dsDNA signatures at cosine 0.97 and onto COSMIC SBS10c at 0.90; SBS14ss covers combined MMR + proofreading deficiency; SBS30ss* is cytosine deamination damage ([[10-Summaries/liu-2024-hidef-seq|HiDEF-seq]]).
- This resolves **which chemical event initiated which mutation class**, previously inferable only indirectly from replication-timing asymmetry or from in vitro gap-filling assays lacking replication and repair context ([[10-Summaries/liu-2024-hidef-seq|HiDEF-seq]]).

## Contested points

- **Amplification artefacts mimic signatures.** WGA artefacts carry their own context biases that can mimic real signatures, so any per-cell signature claim requires an explicit artefact model ([[10-Summaries/alexandrov-2013-mutational-signatures|Alexandrov 2013]]; synthesis); MDA artefact SNVs match signatures B/scF ([[10-Summaries/luquette-2022-neuron-scan2-indels|Luquette 2022]]).
- **Burden thresholds must be set per tissue**, because mutation prevalence spans five orders of magnitude between cancer types ([[10-Summaries/alexandrov-2013-mutational-signatures|Alexandrov 2013]]; synthesis).
- **Not every de novo signature maps to COSMIC.** The young-dominant SMM-seq signature S2 matched no COSMIC signature ([[10-Summaries/maslov-2022-smm-seq|SMM-seq]]).
- **The mechanism of the dominant neuronal indel signature is unknown.** ID4 is deletion-rich and age-correlated, but its mechanism is unknown ([[10-Summaries/luquette-2022-neuron-scan2-indels|Luquette 2022]]).

## Related

> [!cards]
> - `hub` [[40-Topics/duplex-sequencing|Duplex sequencing]] — Strand-tagged single-molecule sequencing that reads rare mutations without clonal expansion.
> - `hub` [[40-Topics/somatic-mosaicism|Somatic mosaicism]] — Genetically distinct cell lineages within one organism, all from one zygote.

## All sources on this page

> [!info]- 14 summaries cited here
> - [[10-Summaries/alexandrov-2013-mutational-signatures|Alexandrov 2013]]
> - [[10-Summaries/bizzotto-2022-brain-mosaicism-review|Bizzotto & Walsh 2022]]
> - [[10-Summaries/gawad-2014-all-clonal-origins|Gawad 2014]]
> - [[10-Summaries/hoang-2016-botseqs|Hoang 2016]]
> - [[10-Summaries/kong-2026-mutationprojector|Kong 2026 (Cancer Discov)]]
> - [[10-Summaries/kozlov-2022-cellphy|Kozlov 2022]]
> - [[10-Summaries/liu-2024-hidef-seq|Liu 2024]]
> - [[10-Summaries/lodato-2017-aging-neurons|Lodato 2018]]
> - [[10-Summaries/luquette-2022-neuron-scan2-indels|Luquette 2022]]
> - [[10-Summaries/luquette-2025-pta-duplex-mosaicism|Luquette 2025]]
> - [[10-Summaries/maslov-2022-smm-seq|Maslov 2022]]
> - [[10-Summaries/muyas-2024-scomatic|Muyas 2024]]
> - [[10-Summaries/nandi-2025-udseq|Nandi 2025]]
> - [[10-Summaries/xing-2021-meta-cs|Xing 2021]]
