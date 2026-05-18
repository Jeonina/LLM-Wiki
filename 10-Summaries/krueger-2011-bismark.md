---
type: summary
title: "Krueger 2011 — Bismark: a flexible aligner and methylation caller for Bisulfite-Seq applications"
source: "[[00-Sources/papers/Bismark_ a flexible aligner and methylation caller for Bisulfite-Seq applications]]"
aliases: ["Krueger 2011 Bismark", "Bismark", "bisulfite aligner founding"]
tags: [Bismark, bisulfite-aligner, methylation-caller, BS-seq, founding-tool, Babraham, Reik-lab-adjacent]
created: 2026-05-13
updated: 2026-05-13
source: "[[00-Sources/papers/Bismark_ a flexible aligner and methylation caller for Bisulfite-Seq applications]]"
---

**Citation:** Krueger et al. (2011) — *Bismark: a flexible aligner and methylation caller for Bisulfite-Seq applications* — *Bioinformatics*. [DOI](https://doi.org/10.1093/bioinformatics/btr167)

Krueger and Andrews (Babraham Bioinformatics Group) published the founding **Bismark** aligner-and-methylation-caller for bisulfite sequencing (BS-Seq). The tool performs read mapping and methylation calling in a single pass: bisulfite reads are converted to C-to-T and G-to-A versions, then aligned to equivalently pre-converted forward and reverse genome references using four parallel Bowtie instances. Bismark uniquely determines the strand origin of each bisulfite read, handles both directional and non-directional libraries, and discriminates between CpG, CHG, and CHH contexts.

Output includes per-read mapping + methylation call string, optionally converted to comprehensive (all strands merged) or strand-specific methylation extractor files, suitable for downstream analysis or genome-browser import (SeqMonk, IGV). The 2011 benchmark on 15M Lister 2009 reads (mapped to NCBI36) showed mapping-efficiency 64.2% in 45 min — comparable to BS Seeker but with better unique-best-alignment specificity.

## Why this matters

The de-facto standard bisulfite-sequencing aligner in mammalian methylome studies for the past decade. Direct input to virtually every single-cell methylome paper that produces processed methylation calls — scBS-seq (Smallwood 2014), scNMT-seq (Clark 2018), scRRBS (Guo 2013), snmC-seq2/3 (Luo 2018, Liu 2021). Anchors §3.3 (methylation chemistry + processing pipeline) and §4 (computational methods — Bismark sits at the entry point of every methylation tool chain: Melissa, Epiclomal, scMET, MethylTree all consume Bismark output). Essential founding-citation for any methylation-section completeness.

---
**Source:** [DOI](https://doi.org/10.1093/bioinformatics/btr167) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/21493656/)

---
**Source:** [DOI](https://doi.org/10.1093/bioinformatics/btr167) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/21493656/)

## Related

- [[10-Summaries/smallwood-2014-natmethods]]
- [[10-Summaries/clark-2018-scnmt]]
- [[20-Entities/wolf-reik]]
- [[30-Concepts/bisulfite-sequencing]]
