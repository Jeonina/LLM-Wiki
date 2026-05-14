---
type: summary
title: "Bae 2023 — Single duplex DNA sequencing with CODEC detects mutations with high sensitivity"
aliases: ["Bae 2023 CODEC", "CODEC", "Concatenating Original Duplex"]
tags: [CODEC, duplex-sequencing, error-correction, single-duplex, Adalsteinsson-lab, Broad, mosaicism, cfDNA, sperm-mutation]
created: 2026-05-13
updated: 2026-05-13
sources: ["Jin_2023_NatureGenetics.pdf"]
---

Bae, Liu, Roberts, Nguyen, Tabrizi, Rhoades, Blewett, Xiong, Gydush, Shea, An, Patel, Cheng, Sridhar, Liu, Lassen, Skytte, Grońska-Pęski, Shoag, **Evrony**, Parsons, Mayer, Makrigiorgos, Golub and Adalsteinsson (Broad/MIT, MGH, Koch Institute) developed **CODEC** (Concatenating Original Duplex for Error Correction), a hybrid duplex-sequencing chemistry that **physically links the Watson and Crick strands** of each DNA insert into a single sequence-able molecule via an adapter-quadruplex linker. Each Illumina NGS read pair is then self-sufficient for forming a consensus between both strands of the original duplex — without needing 100-fold over-sampling to recover both strands by chance (as in classical Duplex Sequencing or NanoSeq).

Result: ~1,000-fold higher accuracy than NGS, using up to 100-fold fewer reads than duplex sequencing. Compatible with targeted panels *and* WGS, where prior duplex methods (NanoSeq) were limited to ~29% of the genome due to dideoxy-end-repair constraints. Demonstrations: mutation frequency 2.72×10⁻⁸ in sperm of a 39-year-old; somatic mutations acquired with age in blood cells; single-duplex tumor mutations in cfDNA liquid biopsies; microsatellite instability with 10× greater sensitivity; mutational-signature recovery with 100× fewer reads.

## Why this matters

The most recent major advance in duplex sequencing, completing the trajectory Schmitt 2012 → NanoSeq 2021 → CODEC 2023. CODEC's WGS-compatibility is a step-change for mosaicism work: bulk WGS at single-duplex resolution becomes economically viable. Anchors §3.1 (duplex chemistries family), §6 (limitations — CODEC partly resolves the depth-vs-coverage tradeoff that bulk duplex had) and §7 (future perspectives — CODEC + cfDNA is a credible path to non-invasive mosaicism monitoring). Important authorship note: Gilad Evrony is a co-author, linking this to the brain-mosaicism community.

---
**Source:** [DOI](https://doi.org/10.1038/s41588-023-01376-0) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/37106072/)

## Related

- [[10-Summaries/schmitt-2012-pnas]]
- [[10-Summaries/abascal-2021-nature]]
- [[10-Summaries/hoang-2016-pnas]]
- [[30-Concepts/codec]]
- [[30-Concepts/duplex-sequencing]]
