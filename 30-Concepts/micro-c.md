---
type: concept
title: "Micro-C"
aliases: []
tags: []
created: 2026-10-07
updated: 2026-10-12
sources: ["[[10-Summaries/hsieh-2015-micro-c]]"]
---

# Micro-C

> Micro-C is a Hi-C variant that fragments crosslinked chromatin into mononucleosomes with micrococcal nuclease before proximity ligation, yielding nucleosome-resolution contact maps ([[10-Summaries/hsieh-2015-micro-c|Hsieh 2015]]).

> [!abstract] 한눈에
> Micro-C는 MNase로 chromatin을 mononucleosome 단위로 자른 뒤 proximity ligation을 하는 Hi-C 변형으로, nucleosome 해상도의 contact map을 만든다 ([[10-Summaries/hsieh-2015-micro-c|Hsieh 2015]]). 짧은 거리 접촉에는 강하지만 centromere clustering 같은 장거리 접촉은 잘 잡지 못해 Hi-C를 대체하기보다 보완한다 ([[10-Summaries/hsieh-2015-micro-c|Hsieh 2015]]).

## Definition

The original protocol uses MNase digestion to >95% mononucleosomes, biotin end-labelling, dilute ligation, exonuclease III removal of unligated ends and streptavidin pulldown ([[10-Summaries/hsieh-2015-micro-c|Hsieh 2015]]). An interspecies mixing control estimated ~10% spurious ligations ([[10-Summaries/hsieh-2015-micro-c|Hsieh 2015]]).

## Why it matters

- It fills the resolution gap between ~150-bp nucleosome mapping and ~1–4-kb restriction-enzyme Hi-C ([[10-Summaries/hsieh-2015-micro-c|Hsieh 2015]]).
- Its contact maps are now training data for sequence models: AlphaGenome's contact-map head is trained on Hi-C/Micro-C ([[10-Summaries/avsec-2026-alphagenome|AlphaGenome]]).

## Evidence and examples

**Chromosomal interaction domains (yeast)**

- Micro-C revealed gene-scaled chromosomal interaction domains (CIDs) in yeast ([[10-Summaries/hsieh-2015-micro-c|Hsieh 2015]]).
- CID boundaries fall mostly at +1 nucleosomes of promoters (~40% of boundary nucleosomes vs ~7% genome-wide), enriched for H3K18ac, H3K4me3, histone turnover, RSC and the cohesin loader Scc2 ([[10-Summaries/hsieh-2015-micro-c|Hsieh 2015]]).

**Gene compaction and transcription**

- Gene compaction is anticorrelated with transcription (r = −0.56), but transcription explains only 31% of its variance ([[10-Summaries/hsieh-2015-micro-c|Hsieh 2015]]).
- Mediator (*med1Δ*), Rtt109 and Rpd3 loss decompact genes independently of mRNA changes, while RSC and Scc2 inactivation compact them ([[10-Summaries/hsieh-2015-micro-c|Hsieh 2015]]).

**Nucleosome-level folding**

- There is no periodic 30-nm-fibre signal in vivo: contact decay has no 30-nm periodicity ([[10-Summaries/hsieh-2015-micro-c|Hsieh 2015]]).
- N/N+1 and N/N+2 contacts are similarly abundant, consistent with a sparse tri-/tetranucleosome motif ([[10-Summaries/hsieh-2015-micro-c|Hsieh 2015]]).
- The H4 N-terminal tail is needed for folding signal ([[10-Summaries/hsieh-2015-micro-c|Hsieh 2015]]).

**Use in sequence models**

- AlphaGenome's contact-map head beat Orca by 6.3% in contact-map Pearson r and 42.3% on cell-type-specific differences ([[10-Summaries/avsec-2026-alphagenome|AlphaGenome]]).

## Contested points

- **Complement, not replacement.** Micro-C captures long-range contacts such as centromere clustering poorly, so it complements rather than replaces Hi-C ([[10-Summaries/hsieh-2015-micro-c|Hsieh 2015]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/topologically-associating-domain|Topologically associating domain]] — Self-interacting ~100 kb–1 Mb neighbourhoods bounded by CTCF and cohesin.
> - `concept` [[30-Concepts/chromatin-loop|Chromatin loop]] — A focal point-to-point contact enriched above local background.
> - `concept` [[30-Concepts/multi-way-chromatin-interaction|Multi-way chromatin interaction]] — Three or more loci in simultaneous contact within one nucleus.
> - `hub` [[40-Topics/3d-genome|3D genome]] — Territories, compartments, domains and loops in the nucleus.

## All sources on this page

> [!info]- 2 summaries cited here
> - [[10-Summaries/avsec-2026-alphagenome|AlphaGenome 2026]]
> - [[10-Summaries/hsieh-2015-micro-c|Hsieh 2015]]
