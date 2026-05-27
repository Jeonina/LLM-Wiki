---
type: summary
title: "Hsieh et al. 2026 — Single-cell multi-omic analysis of mitochondrial mutational mosaicism and dynamics (scmtMPM/scwMSS)"
source: "[[00-Sources/papers/Single-cell multi-omic analysis of mitochondrial mutational mosaicism and dynamics]]"
source_kind: paper
author: Yu-Hsin Hsieh, Pauline Kautz, Lena Nitsch, ..., Caleb A. Lareau, Leif S. Ludwig (corresponding)
published: 2026-03-16
ingested: 2026-05-27
doi: "10.1038/s41467-026-70399-y"
journal: "Nature Communications"
tags: [mtdna, mtscATAC-seq, mitochondrial-mosaicism, heteroplasmy, MELAS, POLG, scmtMPM, scwMSS]
entities: ["[[20-Entities/leif-ludwig]]", "[[20-Entities/caleb-lareau]]"]
concepts: ["[[30-Concepts/mitochondrial-heteroplasmy]]", "[[30-Concepts/mitochondrial-lineage-tracing]]", "[[30-Concepts/scatac-seq]]"]
topics: ["[[40-Topics/somatic-mosaicism]]"]
---

**Citation:** Hsieh et al. (2026) — *Single-cell multi-omic analysis of mitochondrial mutational mosaicism and dynamics* — *Nature Communications*. [DOI](https://doi.org/10.1038/s41467-026-70399-y)

# Hsieh 2026 — quantifying per-cell mtDNA mutational burden via scmtMPM and scwMSS

> NOTE on slug: The file `hsieh-2026-mtdna-mosaicism.md` already exists in this wiki, but its *content* is actually about **Glynos 2023** (random-drift mtDNA divergence in *Science Advances*), not Hsieh 2026. That file is mis-slugged and should be renamed `glynos-2023-mtdna-heteroplasmy.md` in a future lint pass. The present summary uses the distinct slug `hsieh-2026-scmtmpm-scwmss.md` to avoid collision.

> Introduces two single-cell metrics — **scmtMPM** (mtDNA mutations per million bp, depth-normalized) and **scwMSS** (heteroplasmy-weighted mitochondrial local-constraint score) — for quantifying genome-wide mtDNA mutational burden in individual cells via mtscATAC-seq. Validates on POLG D274A hypermutator HEK293 lines (~15× more variants than bulk-seq detected) and applies to PBMCs from healthy donors and MELAS patients. Key finding: **pathogenic and truncating mtDNA variants are systematically held at sub-threshold heteroplasmy** in hypermutator cells, indicative of strong negative selection acting well below the canonical 60–80% biochemical threshold.

## Key claims

1. **mtscATAC-seq detects ~15× more mtDNA variants per cell than bulk-seq.** POLG D274A KI36/KIA2 lines yield ~9,600 and ~11,400 unique variants vs 620 in control. Most are low-VAF (<1%), missed by bulk approaches due to averaging across cells.
2. **scmtMPM and scwMSS metrics quantify single-cell mutational burden.** scmtMPM normalizes variant count by sequencing depth (analog of nuclear TMB). scwMSS sums mtDNA local constraint scores weighted by VAF, providing functional-impact-aware burden estimate. Both correlate well in hypermutator cells and stabilize at moderate sequencing depths (~25k reads/cell).
3. **Negative selection acts at sub-threshold VAF.** Pathogenic MITOMAP variants and truncating variants remain at near-zero VAF in *POLG* D274A cells (Shannon entropy ≈ 0), while synonymous and missense variants show broad VAF distributions reaching 25–50%. Pairwise: pathogenic variants are mutually exclusive in single cells; truncating variants can co-occur but rarely >60% VAF.
4. **Galactose stress amplifies mtDNA copy number, not clonal selection.** *POLG* D274A cells under galactose (forces OXPHOS) show 2.3× increased mtDNA copy number but no shift in VAF distributions or clonal sweep — the compensation is quantitative (more mitochondria), not qualitative (selecting better ones).
5. **MELAS T cells show purifying selection against m.3243A>G with age.** In younger MELAS patients (29, 35 yr) the bimodal scmtMPM distribution disappears when m.3243A>G is excluded — confirming the variant drives the burden signal. In older patients (60, 80 yr) the bimodal pattern persists after excluding m.3243A>G, indicating new somatic variants accumulate to replace the lost pathogenic clone.
6. **Cells without detectable m.3243A>G have elevated scmtMPM.** Suggests highly pathogenic congenital variants may exert selective pressure that promotes accumulation of additional somatic mtDNA mutations — a previously unappreciated cross-variant interaction.

## Methods / evidence

mtscATAC-seq (Lareau/Ludwig 2021 protocol) with cell hashing; mgatk variant-calling; MITOMAP/gnomAD-derived constraint scoring. Cell systems: HEK293 with *POLG* D274A knock-ins (KI36, KIA2 alleles) and CTRL; PBMCs from 2 healthy donors (ages 5, 47) and 4 MELAS patients (29, 35, 60, 80). Depth: median raw mtDNA depth 45 (CTRL), 130 (KI36), 214 (KIA2). Joint readout: mtDNA variants + chromatin accessibility. Downsampling analysis demonstrates metric stability at ≥10k reads/cell.

## Surprising or load-bearing bits

- **Negative selection visible at sub-threshold VAF.** Traditional teaching: pathogenic mtDNA variants matter at 60–80% VAF (biochemical threshold). This paper shows selection acts even at <10% VAF in hypermutator cells, suggesting cells "sense" pathogenic variants before they reach biochemical impact.
- **Compensation is copy-number-based, not clonal.** The galactose experiment is the cleanest demonstration that hypermutator cells respond to OXPHOS stress by *amplifying* mitochondria rather than selecting cleaner mtDNA copies. Therapeutic implication: targeting mtDNA copy number may be more tractable than purging mutations.
- **Older MELAS = m.3243A>G replaced by other mutations.** Conceptually similar to clonal-replacement dynamics in CHIP. Once one pathogenic clone is purged, somatic mutation supply ensures the burden persists.
- **mtscATAC-seq joint readout enables nuclear-mitochondrial correlation.** Differentially accessible gene analysis identifies upregulation of ECM remodeling genes (CYR61, TGFBI), Zn-finger TFs, and downregulation of MGME1 (mitochondrial maintenance exonuclease) in POLG-mutant cells — connecting mtDNA mutational load to nuclear gene-regulatory rewiring.

## Entities mentioned

- [[20-Entities/leif-ludwig]] — corresponding author, BIH/MDC Berlin; mtDNA single-cell genetics
- [[20-Entities/caleb-lareau]] — co-corresponding author, MSKCC; mtscATAC-seq + mgatk developer

## Concepts touched

- [[30-Concepts/mitochondrial-heteroplasmy]] — adds quantitative per-cell burden framework
- [[30-Concepts/mitochondrial-lineage-tracing]] — methodology extension
- [[30-Concepts/scatac-seq]] — leverages mtscATAC-seq joint readout

## Connections to other sources

- **Extends** the mtscATAC-seq foundational work (Lareau 2021 Nat Biotech, not yet ingested).
- **Companion to** the mis-slugged Glynos 2023 paper at `[[10-Summaries/hsieh-2026-mtdna-mosaicism]]` — both address mtDNA heteroplasmy dynamics but from different angles (drift vs selection, healthy vs hypermutator).
- **Complementary to** [[10-Summaries/forsberg-2017-mosaicism-clones]] — addresses one mosaicism axis (mtDNA) explicitly excluded from that 2017 review's scope.

## Open questions

- How does scmtMPM extend to non-blood tissues where mtscATAC-seq has limited application? Required for cardiac/neural mtDNA studies.
- The pathogenic-variant-elevates-other-somatic-mutation observation in older MELAS — is this generic (mtDNA-damage-response failure?) or m.3243A>G-specific?

## Related

- [[40-Topics/somatic-mosaicism]] · [[30-Concepts/mitochondrial-heteroplasmy]] · [[30-Concepts/mitochondrial-lineage-tracing]]
- [[10-Summaries/forsberg-2017-mosaicism-clones]] — mtDNA mosaicism was excluded from this 2017 review
