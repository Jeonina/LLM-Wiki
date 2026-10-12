---
type: summary
title: "Bae 2023 — Single duplex DNA sequencing with CODEC detects mutations with high sensitivity"
source: "[[00-Sources/papers/Single duplex DNA sequencing with CODEC detects mutations with high sensitivity]]"
source_quality: full
source_sha256: "1cb4b9e237bbdf911217661a6180e87abf12d507128aae8f18e0fdc463b4b634"
aliases: ["Bae 2023 CODEC", "CODEC", "Concatenating Original Duplex"]
tags: [CODEC, duplex-sequencing, error-correction, single-duplex, Adalsteinsson-lab, Broad, mosaicism, cfDNA, sperm-mutation]
created: 2026-05-13
updated: 2026-05-13
---

**Citation:** Bae et al. (2023) — *Single duplex DNA sequencing with CODEC detects mutations with high sensitivity* — *Nature Genetics*. [DOI](https://doi.org/10.1038/s41588-023-01376-0)

> [!abstract] 한눈에
> CODEC은 adapter로 DNA 이중가닥의 Watson 가닥과 Crick 가닥을 한 분자로 연결해, read pair 하나만으로 두 가닥의 consensus를 만드는 duplex sequencing 기법이다. 일반 NGS보다 약 1,000배 정확하면서도 duplex sequencing보다 read가 최대 100배 적게 들고, WGS에도 적용할 수 있다.

Bae, Liu, Roberts, Nguyen, Tabrizi, Rhoades, Blewett, Xiong, Gydush, Shea, An, Patel, Cheng, Sridhar, Liu, Lassen, Skytte, Grońska-Pęski, Shoag, **Evrony**, Parsons, Mayer, Makrigiorgos, Golub and Adalsteinsson (Broad/MIT, MGH, Koch Institute) developed **CODEC** (Concatenating Original Duplex for Error Correction), a hybrid duplex-sequencing chemistry that **physically links the Watson and Crick strands** of each DNA insert into a single sequence-able molecule via an adapter-quadruplex linker. Each Illumina NGS read pair is then self-sufficient for forming a consensus between both strands of the original duplex — without needing 100-fold over-sampling to recover both strands by chance (as in classical Duplex Sequencing or NanoSeq).

Result: ~1,000-fold higher accuracy than NGS, using up to 100-fold fewer reads than duplex sequencing. Compatible with targeted panels *and* WGS, where prior duplex methods (NanoSeq) were limited to ~29% of the genome due to dideoxy-end-repair constraints. Demonstrations: mutation frequency 2.72×10⁻⁸ in sperm of a 39-year-old; somatic mutations acquired with age in blood cells; single-duplex tumor mutations in cfDNA liquid biopsies; microsatellite instability and mutational signatures with 10× greater sensitivity; specific tumor mutations with up to 100× fewer reads.

## Why this matters

The most recent major advance in duplex sequencing, completing the trajectory Schmitt 2012 → NanoSeq 2021 → CODEC 2023. CODEC's WGS-compatibility is a step-change for mosaicism work: bulk WGS at single-duplex resolution becomes economically viable. Anchors §3.1 (duplex chemistries family), §6 (limitations — CODEC partly resolves the depth-vs-coverage tradeoff that bulk duplex had) and §7 (future perspectives — CODEC + cfDNA is a credible path to non-invasive mosaicism monitoring). Important authorship note: Gilad Evrony is a co-author, linking this to the brain-mosaicism community.

---
**Source:** [DOI](https://doi.org/10.1038/s41588-023-01376-0) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/37106072/)

## Related

- [[10-Summaries/schmitt-2012-pnas]]
- [[10-Summaries/abascal-2021-nanoseq]]
- hoang 2016 pnas
- [[30-Concepts/codec]]
- [[40-Topics/duplex-sequencing]]
