---
type: summary
title: "Gabbutt et al. 2025 — Fluctuating DNA methylation tracks cancer evolution at clinical scale (EVOFLUx)"
source: "[[00-Sources/papers/Fluctuating DNA methylation tracks cancer evolution at clinical scale]]"
source_kind: paper
author: "Calum Gabbutt, Martí Duran-Ferrer, Heather E. Grant, … Darryl Shibata, José I. Martin-Subero, Trevor A. Graham (corresponding)"
published: 2025-09-10
ingested: 2026-08-17
doi: "10.1038/s41586-025-09374-4"
journal: "Nature 645:1005–1014"
tags: [EVOFLUx, fCpG, fluctuating-CpG, methylation-barcode, cancer-evolution, CLL, Richter-transformation, prognosis, bulk-methylation]
entities: []
concepts: ["[[methylation-clones-epimutation]]", "[[lineage-tracing]]", "[[epigenetic-aging]]", "[[bisulfite-sequencing]]", "[[intratumor-heterogeneity]]", "[[phylogenetic-inference]]"]
topics: ["[[dna-methylation]]", "[[cancer-clonal-evolution]]", "[[hematopoietic-malignancies]]"]
---

**Citation:** Gabbutt et al. (2025) — *Fluctuating DNA methylation tracks cancer evolution at clinical scale* — *Nature* 645, 1005–1014. [DOI](https://doi.org/10.1038/s41586-025-09374-4)

# Gabbutt 2025 — EVOFLUx

> Single-cell phylogenetics gives beautiful evolutionary histories for a handful of patients; **cost has restricted it to small cohorts, limiting clinical translation**. EVOFLUx takes the opposite route: infer quantitative evolutionary dynamics from a **bulk methylation array alone**, using **fluctuating CpGs (fCpGs)** — sites whose methylation stochastically flips on a timescale of years — as a natural barcode. Applied to **1,976 lymphoid cancer samples**.

## Key claims

- **fCpGs are a low-cost, high-temporal-resolution lineage marker.** Certain CpG sites fluctuate stochastically over years, functioning as a "methylation barcode" readable from routine clinical specimens.
- **Bulk input, quantitative output.** From a single bulk tumour methylation profile EVOFLUx infers initial tumour growth rate, malignancy age, epimutation rate, and subclonal structure — quantities previously requiring single-cell or single-cell-colony sequencing.
- **These quantities vary by orders of magnitude across lymphoid disease types** — growth rate, age, and epimutation rate are all disease-specific rather than universal constants.
- **Subclonal selection is infrequent within bulk samples.** A notable negative result: measurable selection within a sample is the exception, not the rule. The method also detects occasional cases of **multiple independent primary tumours**.
- **Faster initial growth in more aggressive subtypes**, and **evolutionary history is a strong independent prognostic factor** in two separate CLL series — the clinical payoff.
- **Richter transformation seeds itself decades early.** Phylogenetic analysis of aggressive Richter-transformed CLL found that the seed of the transformed clone "existed decades before presentation."
- **Orthogonally verified** using additional genetic data including long-read nanopore sequencing, plus clinical variables.

## Methods / evidence

1,976 well-characterised lymphoid cancer samples across a broad disease spectrum; two independent CLL series for the prognostic analysis; orthogonal verification by genetic data and nanopore sequencing.

Weight: the cohort size is the point — this is the first evolutionary-dynamics analysis at a scale where clinical association testing is meaningful. The prognostic claim is supported in two independent CLL series, which is stronger than most single-cohort biomarker reports.

## Surprising or load-bearing bits

- **"Decades before presentation" reframes when the disease begins.** A Richter clone whose seed predates diagnosis by decades means the clinically detectable transformation is the endpoint of a very long process — with obvious implications for early detection, and a direct parallel to the *in utero* origin of childhood ALL translocations ([[gawad-2014-all-clonal-origins]]). (synthesis)
- **Infrequent subclonal selection is a genuinely surprising negative.** The default mental model of tumour evolution is ongoing selection among competing subclones; at bulk resolution across 1,976 samples, that is mostly not what is measured. Whether this reflects biology or the resolution limit of bulk fCpG data is the key interpretive question. (synthesis)
- **Cost is the design constraint being solved, and it is stated explicitly** — single-cell approaches are too expensive for cohort-scale clinical work. EVOFLUx is a deliberate trade of per-cell resolution for statistical power and clinical applicability. That trade is the opposite of the one most of this corpus makes. (synthesis)
- **Methylation as clock beats methylation as classifier.** Where [[50-Notes/methylation-cancer-origin-classifiers|cancer-of-origin classifiers]] use methylation as a static fingerprint, EVOFLUx uses its *dynamics*. Same measurement, entirely different information extracted. (synthesis)
- **The rate framework has a plant ancestor.** [[shahryary-2020-alphabeta|AlphaBeta]] established forward/backward epimutation rates, neutral accumulation, and somatic origin in plants five years earlier; EVOFLUx is the human clinical realisation of the same premise. Neither cites the other's system, but they are the same idea. (synthesis)
- **Darryl Shibata as coauthor** connects this to the long line of work using methylation as a mitotic clock in human tissue.

## Concepts touched

- [[methylation-clones-epimutation]] — fCpGs as a natural barcode; evolutionary inference from epimutation dynamics.
- [[phylogenetic-inference]] — phylogenies from bulk methylation rather than from single-cell genotypes.

## Connections to other sources

- Plant-system ancestor of the epimutation-rate framework: [[shahryary-2020-alphabeta]].
- Mammalian single-cell epimutation lineage tracing: [[scherer-2025-nature]] (EPI-Clone), [[chen-2025-methyltree]] (MethylTree), [[xiao-2025-epitrace]].
- The expensive single-cell alternative it deliberately avoids: [[coorens-2021-nature]], [[lee-six-2018-hsc-dynamics]], [[cagan-2022-nature]].
- CLL epigenetics context: [[gaiti-2019-cll-epigenetic]]; blood clonal dynamics [[nam-2022-natgenet]], [[40-Topics/clonal-hematopoiesis]].
- Methylation as static classifier, for contrast: [[50-Notes/methylation-cancer-origin-classifiers]].
- Cancer phylogenetics from genotypes: [[jahn-2016-scite]], [[kaufmann-2022-medicc2]], [[lu-2024-cnaphylogeny-review]].
- Long-read verification: [[oxford-nanopore]], [[liu-2025-long-read-epigenome-review]].

## Open questions

- **Is infrequent subclonal selection biology or resolution?** Bulk fCpG data may simply lack the power to see selection that single-cell data would reveal — the paper's most consequential claim is also its most method-dependent. (synthesis)
- fCpG clocks saturate once gain and loss reach equilibrium, bounding how far back malignancy age can be read; the bound is not foregrounded.
- Lymphoid cancers only — whether fCpG dynamics behave the same in solid tumours with different proliferative and methylation-maintenance regimes is untested.
- The relationship between fCpG-inferred age and clinical age at diagnosis relies on an assumed constant fluctuation rate across a patient's lifetime.

## Related

- [[shahryary-2020-alphabeta]] · [[scherer-2025-nature]] · [[methylation-clones-epimutation]] · [[40-Topics/cancer-clonal-evolution]]
