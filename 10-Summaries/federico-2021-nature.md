---
type: summary
title: "Abascal 2021 — Somatic mutation landscapes at single-molecule resolution (NanoSeq)"
source: "[[00-Sources/papers/Somatic mutation landscapes at single-molecule resolution]]"
aliases: [Abascal 2021, NanoSeq, Federico 2021, Sanger NanoSeq]
tags: [duplex-sequencing, somatic-mosaicism, NanoSeq, post-mitotic-neurons, mutation-rate, foundational]
created: 2026-05-12
updated: 2026-05-12
---

**Citation:** Abascal et al. (2021) — *Somatic mutation landscapes at single-molecule resolution (NanoSeq)* — *Nature*. [DOI](https://doi.org/10.1038/s41586-021-03477-4)

# Abascal et al. 2021 — NanoSeq for non-dividing cells

> Federico Abascal, Luke M. R. Harvey, Emily Mitchell, Andrew R. J. Lawson, Stefanie V. Lensing, Peter Ellis, Andrew J. C. Russell, Raul E. Alcantara, Adrian Baez-Ortega, Yichen Wang, Eugene Jing Kwa, Henry Lee-Six, Alex Cagan, Tim H. H. Coorens, Michael Spencer Chapman, Sigurgeir Olafsson, Steven Leonard, David Jones, Heather E. Machado, Megan Davies, Nina F. Øbro, Krishnaa Mahubani, Kieren Allinson, Moritz Gerstung, Kourosh Saeb-Parsy, David G. Kent, Elisa Laurenti, Michael R. Stratton, Raheleh Rahbari, Peter J. Campbell, Robert J. Osborne\*, **Iñigo Martincorena\***. *Nature* **593**, 405–410 (2021). DOI: 10.1038/s41586-021-03477-4. Wellcome Sanger Institute.

## Thesis

**NanoSeq (nanorate sequencing)** is a duplex-sequencing protocol that **avoids end-repair-associated errors** to achieve **<5 errors per billion base pairs in single DNA molecules** — two orders of magnitude lower than typical somatic mutation loads. This enables **somatic-mutation studies in non-dividing cells** (post-mitotic neurons, polyclonal smooth muscle, differentiated cells) for the first time, independently of clonality. Demonstrates **somatic mutations accumulate at constant rate in post-mitotic neurons throughout life** — proving cell division is not required for mutagenesis.

## Mechanism

1. Standard duplex consensus sequencing uses unique molecular barcodes on both strands of each DNA molecule; both strands' consensus reads agree → real mutation. Theoretical error rate <10⁻⁹/bp.
2. **In practice**, mapping errors + accidental cross-strand copying during library prep (especially end-repair) violate the strand-independence assumption → real-world error rates higher.
3. **NanoSeq** introduces end-repair-aware library construction that eliminates these errors. Validated empirically to <5 errors/billion bp.

## Key claims

- Error rate **two orders of magnitude lower than somatic mutation loads** in human tissues → enables genome-wide somatic-mutation measurement in any cell population, regardless of clonality.
- **Post-mitotic neurons accumulate somatic mutations at constant rate throughout life** — directly demonstrates that mutational processes independent of cell division (oxidative damage, deamination, replication-independent mechanisms) contribute substantially to adult somatic mutagenesis. Rate and signatures similar to mitotically-active tissues.
- **Differentiated blood and colon cells have similar mutation loads/signatures to their corresponding stem cells** — despite mature blood cells having undergone many more divisions. Implies division-independent mutational processes dominate or that stem cells accumulate mutations as fast as their differentiated progeny in vivo.
- Smooth muscle (polyclonal, terminally differentiated) profiled at single-molecule resolution.

## Surprising / load-bearing for the review

- **NanoSeq is the methodological anchor for non-dividing-tissue somatic-mutation measurement** — the gap left by clonal-expansion methods (which require mitotic cells) and scWGA (which requires sufficient template).
- For the planned review's **§5 neuroscience applications**: NanoSeq's post-mitotic neuron finding **complements [[10-Summaries/taejeong-2018-science|Bae 2018]]'s observation of mutation-spectrum shift in neurogenesis**. Bae 2018: progenitor cells accumulate mutations during division at ~5 SNVs/day; NanoSeq: post-mitotic neurons continue accumulating at lower constant rate after division ceases. Together they bracket the lifelong neural mosaicism trajectory.
- For §6 (Limitations): NanoSeq's error-rate floor is the **field's current technological ceiling for somatic-mutation accuracy**. Anything below ~5 errors/billion bp requires further chemistry improvement.
- Same Sanger lineage that produced [[a-comprehensive-view-of-somatic-mosaicism-by-single-cell-dna-analysis|Luquette/Walsh SMaHT]] and the duplex-sequencing benchmark; this paper is upstream of those.

## Entities / concepts touched

[[duplex-sequencing]] · [[nanoseq]] · [[somatic-mosaicism]] · [[mutational-signatures]] · [[20-Entities/scott-kennedy]] · [[20-Entities/peter-park]] · [[40-Topics/duplex-sequencing]] · [[40-Topics/somatic-mosaicism]]

## Related summaries

- [[detecting-ultralow-frequency-mutations-by-duplex-sequencing]] — Kennedy/Loeb 2014 foundational DS.
- [[a-universal-duplex-sequencing-approach-for-accurate-detection-of-somatic-mutations]] — Alexandrov UDSeq.
- [[benchmarking-of-duplex-sequencing-approaches-to-reveal-somatic-mutation-landscapes]] — SMaHT cross-method DS benchmark.
- [[taejeong-2018-science]] — Bae 2018 fetal-brain progenitor mutation rates (complementary biology).

---
**Source:** [DOI](https://doi.org/10.1038/s41586-021-03477-4) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/33911282/)
