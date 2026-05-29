---
type: summary
title: "Hilal, Arava & Choudhury 2026 — Single-cell genomics and somatic variation in circulating and cardiac resident cells"
source: "[[00-Sources/papers/Single-Cell Genomics and Somatic Variation in Circulating and Cardiac Resident Cells]]"
source_kind: paper
author: Nazia Hilal, Maniteja Arava, Sangita Choudhury (corresponding)
published: 2026-01-02
ingested: 2026-05-27
doi: "10.1161/CIRCRESAHA.125.325797"
journal: "Circulation Research 138(1)"
tags: [review, cardiovascular, somatic-mosaicism, CHIP, cardiomyocytes, duplex-sequencing]
entities: ["[[20-Entities/sangita-choudhury]]"]
concepts: ["[[30-Concepts/clonal-hematopoiesis]]", "[[30-Concepts/somatic-mosaicism]]", "[[30-Concepts/duplex-sequencing]]", "[[30-Concepts/codec]]", "[[30-Concepts/nanoseq]]", "[[30-Concepts/meta-cs]]"]
topics: ["[[40-Topics/somatic-mosaicism]]", "[[40-Topics/clonal-hematopoiesis]]"]
---

**Citation:** Hilal, Arava & Choudhury (2026) — *Single-Cell Genomics and Somatic Variation in Circulating and Cardiac Resident Cells* — *Circulation Research* 138(1):e325797. [DOI](https://doi.org/10.1161/CIRCRESAHA.125.325797)

# Hilal 2026 — cardiac-resident somatic mutation review

> Cardiovascular-focused review of single-cell genomics and somatic variation, written from the perspective of cardiomyocyte mosaicism (rather than the dominant CHIP-from-blood angle). Frames two complementary lines of evidence: (1) **CHIP** — DNMT3A/TET2/ASXL1/JAK2 clones in HSCs that elevate atherosclerosis, HFpEF, and stroke risk via amplified inflammation; (2) **cardiac-resident mosaicism** — cardiomyocytes accumulate 4,000–30,000 SNVs per cell with age-dependent burden, endothelial cells of smokers show elevated COSMIC SBS4/29/40/92 signatures. References Hilal's own scWGS work showing higher SNV load in ischemic vs healthy cardiomyocytes. Catalogs the duplex-sequencing toolbox (TwinStrand, NanoSeq, BotSeqS, CODEC, Pro-Seq, META-CS) and emphasizes the SMaHT Network and EU SOMATICART as the consortium-scale data infrastructure for the field.

## Key claims

1. **Cardiomyocytes are not genetically uniform.** Healthy human cardiomyocytes carry 4,000–30,000 somatic SNVs per cell, increasing with age. Mutational signatures point to oxidative DNA damage as the dominant aging process; few SNVs are shared between cardiomyocytes, indicating mostly stochastic accumulation.
2. **CHIP is a systemic CVD risk factor.** Recent Chinese cohort: 18% CHIP prevalence in middle-aged adults; even <2% VAF clones raise CHD risk ~1.3× over 12 years. TET2-driven CHIP doubles HFpEF risk (Schuermans 2024). CHIP-linked vascular phenotypes now extend to heart failure, ischemic stroke, venous thrombosis.
3. **Smoking leaves a single-cell COSMIC signature in cardiac endothelium.** scWGS reveals SBS4 (tobacco), SBS29 (chewing tobacco), SBS40 (aging), SBS92 (smoking), ID3 (tobacco insertion-deletion) enrichment in cardiac endothelial cells from smokers.
4. **Duplex-sequencing toolbox enables ultra-rare variant detection.** TwinStrand (10⁻⁷ error rate, targeted), NanoSeq (restriction-enzyme-based, genome-wide), BotSeqS (dilution bottleneck, cost-effective), CODEC (intramolecular ligation linking both strands), Pro-Seq (proximity ligation), META-CS (Tn5-based dual-strand tagging). Each occupies a different point on accuracy/throughput/cost.
5. **Single-nucleus is needed for polyploid cardiomyocytes.** Cardiomyocytes are often multinucleated; nuclei-level genotyping enables intra-cell heterogeneity assessment that whole-cell methods cannot.
6. **Structural-variant mosaicism contributes to non-syndromic cardiac disease.** SCN5A (Long QT), GNAI2 (idiopathic VT), FBN1 (thoracic aneurysm in 3% of non-syndromic TAA) — somatic mutations in known Mendelian-disease genes manifest as adult-onset cardiac phenotypes when restricted to a tissue subset.

## Methods / evidence

Review of ~70 sources. Tabulates 9 sequencing/error-correction technologies (Table 1). Highlights SMaHT Network (NIH) and SOMATICART (EU) as reference-atlas initiatives. Cites the cardiomyocyte single-cell genomics literature (Wang/Walsh-lab 2022, Hsieh/Choudhury 2025 unpublished or in submission per the review).

## Surprising or load-bearing bits

- **The 4,000–30,000 SNVs per cardiomyocyte number is the headline.** Comparable to neuron mutation burdens; importantly, *cardiomyocytes are post-mitotic*, so this is not replication-error driven — it's oxidative damage accumulating in non-dividing cells over decades. Implications for heart failure pathogenesis remain open.
- **TET2-CHIP → HFpEF doubling (Schuermans 2024 JAMA Net Open).** A new connection (post-CANTOS/Jaiswal-era) that opens HFpEF — until recently considered ill-understood — to an inflammatory-clonal mechanism with potential anti-inflammatory therapy targeting.
- **Smoking signature persists in non-blood, non-lung tissue.** The cardiac endothelial SBS4 finding is methodologically important: it shows that smoking's mutagenic signature is *systemic*, not localized, and that cardiac mosaicism carries a smoking history readable from sequencing alone.
- **Limited bias-discussion.** The review under-discusses scWGA artifacts that confound rare-variant calling in cardiomyocytes (PTA helps; older MDA-based studies likely overestimated SNV burden). Worth cross-checking against [[10-Summaries/luquette-2025-pta-duplex-mosaicism]].

## Entities mentioned

- [[20-Entities/sangita-choudhury]] — corresponding author; cardiovascular somatic genomics

## Concepts touched

- [[30-Concepts/clonal-hematopoiesis]] — CHIP→CVD as central organizing concept
- [[30-Concepts/duplex-sequencing]] · [[30-Concepts/nanoseq]] · [[30-Concepts/codec]] · [[30-Concepts/meta-cs]] — duplex-toolbox catalog
- [[30-Concepts/mutational-signatures]] — SBS/ID assignments in cardiac endothelium

## Connections to other sources

- **Complementary to** [[10-Summaries/forsberg-2017-mosaicism-review]] — the cardiac-resident angle was largely missing from the 2017 framing; Hilal 2026 fills that gap.
- **Aligned with** [[10-Summaries/shao-2025-scDNA-mosaicism-review]] on the SMaHT framing.
- **Extends** [[10-Summaries/kennedy-2014-duplex-protocol]] etc. by cataloging the post-Kennedy duplex methods (NanoSeq, CODEC, META-CS) developed 2018–2024.

## Open questions

- What single-cell methods will scale cardiomyocyte genotyping to thousands/cell? PTA + duplex appears to be the leading combination but multi-nucleated cardiomyocytes complicate even per-nucleus analysis.
- Causal vs correlational status of cardiomyocyte SNV burden in heart failure: are these mutations *driving* dysfunction or *biomarking* it?

## Related

- [[40-Topics/somatic-mosaicism]] · [[40-Topics/clonal-hematopoiesis]]
- [[10-Summaries/forsberg-2017-mosaicism-review]] — earlier blood-centric review
- [[10-Summaries/shao-2025-scDNA-mosaicism-review]] — broader SMaHT-era survey
